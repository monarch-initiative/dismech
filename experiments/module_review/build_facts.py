#!/usr/bin/env python3
"""Build the per-batch fact sheets a module reviewer starts from.

Everything here is computed from the repository, with no judgement in it: the
shape of each module's causal graph, what its nodes bind, who conforms to it,
what the repository's own deterministic checks already say, and which other
modules look like siblings. The review itself is the part a script cannot do;
this exists so that every reviewer starts from the same facts and none of them
re-derives a corpus-wide count by hand.

    uv run python experiments/module_review/build_facts.py experiments/module_review/2026-11-28

Writes ``facts/<batch>.md`` (one sheet per module, read by the reviewer) and
``facts/modules.json`` (the same facts, read by ``aggregate.py``).
"""

from __future__ import annotations

import collections
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader

ROOT = Path.cwd()
MODULE_DIR = ROOT / "kb" / "modules"
CONFORMER_DIRS = ("kb/disorders", "kb/comorbidities", "kb/modules")
ROLE_RANK = {
    "trigger": 0,
    "amplifier": 1,
    "central_effector": 2,
    "effector": 3,
    "consequence": 4,
}
CORE_KEYS = {
    "name",
    "description",
    "category",
    "creation_date",
    "notes",
    "pathophysiology",
    "module_categories",
}
TERM_SLOTS = (
    ("biological_processes", "BP"),
    ("molecular_functions", "MF"),
    ("cellular_components", "CC"),
    ("cell_types", "CL"),
    ("locations", "LOC"),
    ("genes", "GENE"),
    ("chemical_entities", "CHEM"),
)


def load(path: Path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def conforms_refs(node) -> list[str]:
    value = node.get("conforms_to") if isinstance(node, dict) else None
    return [v.strip() for v in as_list(value) if isinstance(v, str) and v.strip()]


def descriptor_terms(node, slot) -> list[tuple[str, str, str]]:
    out = []
    for item in as_list(node.get(slot)):
        if not isinstance(item, dict):
            continue
        term = item.get("term") or {}
        out.append(
            (
                term.get("id") or "-",
                term.get("label") or item.get("preferred_term") or "?",
                item.get("modifier") or "",
            )
        )
    return out


def term_ids(node) -> set[str]:
    ids = set()
    for slot, _ in TERM_SLOTS:
        for tid, _, _ in descriptor_terms(node, slot):
            if tid != "-":
                ids.add(tid)
    return ids


def strongly_connected(
    nodes: list[str], edges: dict[str, list[str]]
) -> list[list[str]]:
    """Tarjan; returns components that are real cycles (size > 1, or a self-loop)."""
    index, low, on_stack, stack, out, counter = {}, {}, set(), [], [], [0]

    def visit(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on_stack.add(v)
        for w in edges.get(v, []):
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1 or v in edges.get(v, []):
                out.append(sorted(comp))

    for v in nodes:
        if v not in index:
            visit(v)
    return out


def run_tool(args: list[str]) -> str:
    proc = subprocess.run(
        ["uv", "run", "python", *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    return proc.stdout


def main(run_dir: str) -> None:
    run = ROOT / run_dir
    batches = yaml.safe_load((run / "batches.yaml").read_text())["batches"]
    stems = sorted(p.stem for p in MODULE_DIR.glob("*.yaml"))
    assigned = [m for b in batches for m in b["modules"]]
    dupes = [m for m, n in collections.Counter(assigned).items() if n > 1]
    missing = sorted(set(stems) - set(assigned))
    unknown = sorted(set(assigned) - set(stems))
    if dupes or missing or unknown:
        sys.exit(
            f"batches.yaml does not partition kb/modules: dupes={dupes} missing={missing} unknown={unknown}"
        )
    batch_of = {m: b["id"] for b in batches for m in b["modules"]}

    modules = {stem: load(MODULE_DIR / f"{stem}.yaml") for stem in stems}
    texts = {
        stem: (MODULE_DIR / f"{stem}.yaml").read_text(encoding="utf-8")
        for stem in stems
    }

    collections_of = collections.defaultdict(list)
    for path in sorted((ROOT / "kb" / "module_collections").glob("*.yaml")):
        doc = load(path)
        for member in doc.get("module_members") or []:
            collections_of[member.get("module")].append(path.stem)

    # --- who conforms to what --------------------------------------------------
    links = collections.defaultdict(
        lambda: collections.defaultdict(list)
    )  # module -> node -> [(kind, stem, node)]
    files_per_module = collections.defaultdict(set)
    co_conform = collections.Counter()
    unresolved = collections.defaultdict(list)
    for directory in CONFORMER_DIRS:
        kind = directory.split("/")[1]
        for path in sorted((ROOT / directory).glob("*.yaml")):
            text = path.read_text(encoding="utf-8")
            if "conforms_to" not in text:
                continue
            doc = load(path) or {}
            seen = set()
            for node in doc.get("pathophysiology") or []:
                for ref in conforms_refs(node):
                    module, _, target = ref.partition("#")
                    module, target = module.strip(), target.strip()
                    if module not in modules:
                        continue
                    names = {
                        n.get("name")
                        for n in modules[module].get("pathophysiology") or []
                    }
                    if target not in names:
                        unresolved[module].append(
                            f"{path.stem}#{node.get('name')} -> {ref}"
                        )
                    links[module][target].append((kind, path.stem, node.get("name")))
                    files_per_module[module].add((kind, path.stem))
                    seen.add(module)
            for a in seen:
                for b in seen:
                    if a < b:
                        co_conform[(a, b)] += 1

    # --- the repository's own conformance-content report ------------------------
    content = collections.defaultdict(
        lambda: collections.defaultdict(collections.Counter)
    )
    tsv = run_tool(["scripts/check_conformance_content.py", "--format", "tsv"])
    for row in csv.DictReader(tsv.splitlines(), delimiter="\t"):
        module, _, target = (row.get("anchor") or "").partition("#")
        content[module][target][row.get("kind")] += 1

    # --- sibling candidates by shared ontology terms -----------------------------
    terms_of = {
        s: set().union(
            *[term_ids(n) for n in d.get("pathophysiology") or []] or [set()]
        )
        for s, d in modules.items()
    }

    def shared_terms(a, b):
        union = terms_of[a] | terms_of[b]
        return (len(terms_of[a] & terms_of[b]) / len(union)) if union else 0.0

    facts = {}
    for stem in stems:
        doc = modules[stem]
        nodes = doc.get("pathophysiology") or []
        names = [n.get("name") for n in nodes]
        edges = {
            n.get("name"): [e.get("target") for e in n.get("downstream") or []]
            for n in nodes
        }
        resolvable = {k: [t for t in v if t in names] for k, v in edges.items()}
        indeg = collections.Counter(t for v in resolvable.values() for t in v)
        other_names = {
            sec: {i.get("name") for i in doc.get(sec) or [] if isinstance(i, dict)}
            for sec in ("phenotypes", "biochemical", "histopathology")
        }
        roots = [n for n in names if indeg[n] == 0]
        reach, frontier = set(roots), list(roots)
        while frontier:
            for nxt in resolvable.get(frontier.pop(), []):
                if nxt not in reach:
                    reach.add(nxt)
                    frontier.append(nxt)
        node_rows, dangling, role_inversions, self_loops = [], [], [], []
        edges_total = edges_with_evidence = 0
        for n in nodes:
            nm = n.get("name")
            out_edges = []
            for e in n.get("downstream") or []:
                tgt = e.get("target")
                edges_total += 1
                edges_with_evidence += bool(e.get("evidence"))
                flag = ""
                if tgt == nm:
                    flag = " !SELF-LOOP"
                    self_loops.append(nm)
                elif tgt not in names:
                    where = [sec for sec, vals in other_names.items() if tgt in vals]
                    flag = f" ->{where[0]}" if where else " !DANGLING"
                    if not where:
                        dangling.append(f"{nm} -> {tgt}")
                else:
                    ra, rb = (
                        ROLE_RANK.get(n.get("role")),
                        ROLE_RANK.get(
                            next(x for x in nodes if x.get("name") == tgt).get("role")
                        ),
                    )
                    if ra is not None and rb is not None and rb < ra:
                        role_inversions.append(
                            f"{nm} [{n.get('role')}] -> {tgt} [{next(x for x in nodes if x.get('name') == tgt).get('role')}]"
                        )
                out_edges.append(
                    {
                        "target": tgt,
                        "flag": flag.strip(),
                        "evidence": len(e.get("evidence") or []),
                        "described": bool(e.get("description")),
                        "hypothesis_groups": e.get("hypothesis_groups") or [],
                        "causal_link_type": e.get("causal_link_type"),
                    }
                )
            node_rows.append(
                {
                    "name": nm,
                    "role": n.get("role"),
                    "biological_scale": n.get("biological_scale"),
                    "node_class": n.get("node_class"),
                    "terms": {
                        tag: descriptor_terms(n, slot)
                        for slot, tag in TERM_SLOTS
                        if n.get(slot)
                    },
                    "evidence": len(n.get("evidence") or []),
                    "conforms_to": conforms_refs(n),
                    "downstream": out_edges,
                    "conformer_links": len(links[stem].get(nm, [])),
                    "conformer_examples": [
                        f"{k}/{s}#{c}" for k, s, c in links[stem].get(nm, [])[:5]
                    ],
                    "conformance_content": dict(content[stem].get(nm, {})),
                }
            )
        treatments = []
        for t in doc.get("treatments") or []:
            for tm in t.get("target_mechanisms") or []:
                tgt = tm.get("target")
                treatments.append(
                    {
                        "treatment": t.get("name"),
                        "target": tgt,
                        "effect": tm.get("treatment_effect"),
                        "resolves": tgt in names
                        or any(tgt in v for v in other_names.values()),
                    }
                )
            if not t.get("target_mechanisms"):
                treatments.append(
                    {
                        "treatment": t.get("name"),
                        "target": None,
                        "effect": None,
                        "resolves": None,
                    }
                )
        mentioned = sorted(
            other
            for other in stems
            if other != stem
            and re.search(
                rf"(?<![A-Za-z0-9_]){re.escape(other)}(?![A-Za-z0-9_])", texts[stem]
            )
        )
        by_terms = sorted(
            ((shared_terms(stem, o), o) for o in stems if o != stem), reverse=True
        )[:6]
        by_conf = sorted(
            (
                (n, (set(pair) - {stem}).pop())
                for pair, n in co_conform.items()
                if stem in pair
            ),
            reverse=True,
        )[:6]
        kinds = collections.Counter(k for k, _ in files_per_module[stem])
        facts[stem] = {
            "module": stem,
            "batch": batch_of[stem],
            "name": doc.get("name"),
            "lines": texts[stem].count("\n") + 1,
            "creation_date": str(doc.get("creation_date")),
            "module_categories": doc.get("module_categories") or [],
            "collections": collections_of.get(stem, []),
            "other_sections": {
                k: (len(v) if isinstance(v, list) else 1)
                for k, v in doc.items()
                if k not in CORE_KEYS
            },
            "hypotheses": [
                {
                    "id": h.get("hypothesis_group_id"),
                    "status": h.get("status"),
                    "label": h.get("hypothesis_label"),
                }
                for h in doc.get("mechanistic_hypotheses") or []
            ],
            "discussion_kinds": dict(
                collections.Counter(d.get("kind") for d in doc.get("discussions") or [])
            ),
            "nodes": node_rows,
            "graph": {
                "node_count": len(nodes),
                "edge_count": edges_total,
                "edges_with_evidence": edges_with_evidence,
                "roots": roots,
                "leaves": [n for n in names if not resolvable.get(n)],
                "unreachable_from_roots": [n for n in names if n not in reach],
                "isolated": [n for n in names if indeg[n] == 0 and not edges.get(n)],
                "cycles": strongly_connected(names, resolvable),
                "self_loops": self_loops,
                "dangling_targets": dangling,
                "role_order_inversions": role_inversions,
                "role_counts": dict(
                    collections.Counter(n.get("role") or "(none)" for n in nodes)
                ),
                "nodes_without_any_term": [
                    r["name"] for r in node_rows if not r["terms"]
                ],
                "nodes_without_process_or_function": [
                    r["name"]
                    for r in node_rows
                    if not (r["terms"].get("BP") or r["terms"].get("MF"))
                ],
                "nodes_without_evidence": [
                    r["name"] for r in node_rows if not r["evidence"]
                ],
                "duplicate_node_names": [
                    n for n, c in collections.Counter(names).items() if c > 1
                ],
            },
            "treatment_targets": treatments,
            "conformers": {
                "links": sum(len(v) for v in links[stem].values()),
                "files": len(files_per_module[stem]),
                "files_by_kind": dict(kinds),
                "unresolved_anchors": unresolved.get(stem, [])[:10],
                "nodes_never_conformed_to": [
                    n for n in names if not links[stem].get(n)
                ],
            },
            "siblings": {
                "named_in_this_file": mentioned,
                "names_this_module": sorted(
                    o
                    for o in stems
                    if o != stem
                    and re.search(
                        rf"(?<![A-Za-z0-9_]){re.escape(stem)}(?![A-Za-z0-9_])", texts[o]
                    )
                ),
                "most_shared_terms": [
                    {"module": o, "jaccard": round(s, 2)} for s, o in by_terms if s > 0
                ],
                "most_shared_conformer_files": [
                    {"module": o, "files": n} for n, o in by_conf
                ],
            },
        }

    out_dir = run / "facts"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "modules.json").write_text(
        json.dumps(facts, indent=1, sort_keys=True) + "\n"
    )
    for batch in batches:
        chunks = [
            f"# Fact sheets for batch {batch['id']}: {batch['theme']}\n",
            "Computed by `build_facts.py`; see the README for how to read each line.\n",
        ]
        for stem in batch["modules"]:
            chunks.append(render(facts[stem]))
        (out_dir / f"{batch['id']}.md").write_text("\n".join(chunks))
    print(
        f"wrote facts for {len(facts)} modules in {len(batches)} batches to {out_dir}"
    )


def render(f: dict) -> str:
    g, c, s = f["graph"], f["conformers"], f["siblings"]
    lines = [
        f"\n## {f['module']}",
        f"- file: `kb/modules/{f['module']}.yaml` ({f['lines']} lines); name: {f['name']}; created {f['creation_date'][:10]}",
        f"- module_categories: {', '.join(f['module_categories']) or '(none)'}; collections: {', '.join(f['collections']) or '(none)'}",
        f"- other sections: {', '.join(f'{k}={v}' for k, v in f['other_sections'].items()) or '(none)'}",
    ]
    if f["hypotheses"]:
        lines.append(
            "- hypotheses: "
            + "; ".join(f"{h['id']} [{h['status']}]" for h in f["hypotheses"])
        )
    if f["discussion_kinds"]:
        lines.append(
            "- discussions: "
            + ", ".join(f"{k}={v}" for k, v in f["discussion_kinds"].items())
        )
    lines.append(
        f"- graph: {g['node_count']} nodes, {g['edge_count']} edges ({g['edges_with_evidence']} with their own evidence); "
        f"roles {g['role_counts']}"
    )
    lines.append(f"- roots: {g['roots'] or '(none: every node has an incoming edge)'}")
    lines.append(f"- leaves: {g['leaves'] or '(none)'}")
    for key, label in (
        ("cycles", "cycles"),
        ("self_loops", "self-loops"),
        ("dangling_targets", "DANGLING targets (resolve to nothing in this file)"),
        ("isolated", "isolated nodes (no edge in or out)"),
        ("unreachable_from_roots", "unreachable from any root"),
        ("role_order_inversions", "edges running against role order"),
        ("duplicate_node_names", "duplicate node names"),
        ("nodes_without_any_term", "nodes binding no ontology term"),
        (
            "nodes_without_process_or_function",
            "nodes binding no GO process or function",
        ),
        ("nodes_without_evidence", "nodes with no evidence"),
    ):
        if g[key]:
            lines.append(f"- {label}: {g[key]}")
    lines.append(
        f"- conformers: {c['links']} links from {c['files']} files {c['files_by_kind'] or ''}"
        + (
            f"; never conformed to: {c['nodes_never_conformed_to']}"
            if c["nodes_never_conformed_to"]
            else ""
        )
    )
    if c["unresolved_anchors"]:
        lines.append(
            f"- conformers naming a node this module does not have: {c['unresolved_anchors']}"
        )
    lines.append(
        "- siblings: named here "
        + (", ".join(s["named_in_this_file"]) or "(none)")
        + "; names this module: "
        + (", ".join(s["names_this_module"]) or "(none)")
    )
    lines.append(
        "- most shared ontology terms: "
        + (
            ", ".join(f"{x['module']} ({x['jaccard']})" for x in s["most_shared_terms"])
            or "(none)"
        )
    )
    lines.append(
        "- most shared conformer files: "
        + (
            ", ".join(
                f"{x['module']} ({x['files']})"
                for x in s["most_shared_conformer_files"]
            )
            or "(none)"
        )
    )
    lines.append("\nNodes, in file order:\n")
    for i, n in enumerate(f["nodes"], 1):
        lines.append(
            f"{i}. **{n['name']}** role={n['role']} scale={n['biological_scale']} node_class={n['node_class']} "
            f"evidence={n['evidence']} conformer_links={n['conformer_links']}"
            + (
                f" conformance_content={n['conformance_content']}"
                if n["conformance_content"]
                else ""
            )
            + (f" conforms_to={n['conforms_to']}" if n["conforms_to"] else "")
        )
        for tag, terms in n["terms"].items():
            lines.append(
                f"   - {tag}: "
                + "; ".join(
                    f"{tid} {label}" + (f" [{mod}]" if mod else "")
                    for tid, label, mod in terms
                )
            )
        for e in n["downstream"]:
            extra = [f"evidence={e['evidence']}"]
            if e["flag"]:
                extra.append(e["flag"])
            if e["hypothesis_groups"]:
                extra.append(f"hypothesis_groups={e['hypothesis_groups']}")
            if e["causal_link_type"]:
                extra.append(e["causal_link_type"])
            lines.append(f"   - -> {e['target']} ({', '.join(extra)})")
        if n["conformer_examples"]:
            lines.append(f"   - conformers e.g.: {', '.join(n['conformer_examples'])}")
    if f["treatment_targets"]:
        lines.append("\nTreatment targets:\n")
        for t in f["treatment_targets"]:
            lines.append(
                f"- {t['treatment']}: {t['effect']} -> {t['target']}"
                + (
                    ""
                    if t["resolves"] or t["target"] is None
                    else "  !DOES NOT RESOLVE"
                )
                + ("  (no target_mechanisms)" if t["target"] is None else "")
            )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
