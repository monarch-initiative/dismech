#!/usr/bin/env python3
"""Regenerate every Part III figure in ``docs/reports/physiomap-assessment-2026-08-23.md``.

Part III of that report analyses the published PhysioMap v1.1.1 release. Those numbers are
not in the PhysioMap paper, so they are only as trustworthy as the code that produced them.
This script is that code.

It exists because the first published revision of the report got one analysis wrong: the
lesion-reachability depth distribution treated ``primary_intervention`` as a single
identifier, but 27 of the 866 benchmark rows carry *two* semicolon-separated lesion
variables (ARSA, CTNS, KYNU, PKLR — the same four genes the paper excludes from its inverse
benchmark for exactly that reason). The bad parse invented a "27 unresolvable ids" row and
skewed the reachability split. A committed script makes that class of error checkable.

Usage::

    git clone https://github.com/bio-ontology-research-group/physiomap /tmp/physiomap
    uv run python scripts/physiomap_release_analysis.py /tmp/physiomap

Reads only two paths inside the clone, both committed in the PhysioMap release:

* ``web/physiomap-1.1.1.json``            — the projected causal knowledge graph
* ``benchmarks/results/e1b_forward_pairs.tsv`` — the 866 adjudicated benchmark pairs

``--dismech <repo root>`` regenerates the Part IV dismech-side counts instead, including
the §4.1 modifier census whose scope was previously stated only in prose.

Nothing is written; every figure is printed with the report section it belongs to.
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import re
import sys
from pathlib import Path

WEB_PAYLOAD = "web/physiomap-1.1.1.json"
FORWARD_PAIRS = "benchmarks/results/e1b_forward_pairs.tsv"

# Paper-reported axiom counts (§1.8), for the reconciliation check in §3.
PAPER_COUNTS = {
    "causal": 2270,
    "production": 85,
    "constitution": 4,
    "quantitative": 9,
    "modulation": 19,
}


def load(root: Path) -> tuple[dict, list[dict]]:
    payload = root / WEB_PAYLOAD
    pairs = root / FORWARD_PAIRS
    for path in (payload, pairs):
        if not path.exists():
            sys.exit(f"not found: {path}\nPass the root of a PhysioMap clone.")
    with payload.open() as handle:
        graph = json.load(handle)
    with pairs.open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return graph, rows


def header(text: str) -> None:
    print(f"\n{'=' * 78}\n{text}\n{'=' * 78}")


def counts_and_reconciliation(graph: dict) -> None:
    header("§3 — release inventory and reconciliation with the paper")
    stats = graph["stats"]
    release = {
        "causal": stats["n_causal"],
        "production": stats["n_production"],
        "constitution": stats["n_constitutive"],
        "quantitative": stats["n_quantitative"],
        "modulation": stats["n_modulation"],
    }
    print(
        f"  nodes: {stats['n_nodes']}   largest SCC: {stats['big_scc_size']}   SCCs: {stats['n_sccs']}"
    )
    for key, value in release.items():
        paper = PAPER_COUNTS[key]
        flag = (
            ""
            if value == paper
            else f"   <-- paper reports {paper} (delta {paper - value})"
        )
        print(f"  {key:14} {value:5}{flag}")
    print(
        f"  release relation total: {sum(release.values())}   paper: {sum(PAPER_COUNTS.values())}"
    )


def node_anatomy(graph: dict) -> None:
    header("§3.1 — node anatomy")
    nodes = graph["nodes"]
    for label, key in (("scale", "scale"), ("system", "system")):
        print(f"  {label} distribution:")
        for name, count in collections.Counter(n.get(key) for n in nodes).most_common():
            print(f"     {name!s:28} {count:5}")
    print("  entity ontology prefix:")
    prefixes = collections.Counter(
        (n.get("entity_iri") or "NONE").split(":")[0] for n in nodes
    )
    for name, count in prefixes.most_common():
        print(f"     {name:10} {count:5}")
    print("  PATO quality reuse (top 5):")
    for name, count in collections.Counter(
        n.get("quality_iri") for n in nodes
    ).most_common(5):
        print(f"     {name!s:18} {count:5}")


def edge_signs_and_provenance(graph: dict) -> None:
    header("§3.2 / §3.3 — signs and provenance")
    edges = graph["causal_edges"]
    signs = collections.Counter(e.get("sign") for e in edges)
    print(f"  signs: {dict(signs)}   ({100 * signs['?'] / len(edges):.1f}% are '?')")
    print("  all provenance lines:")
    for name, count in collections.Counter(
        e.get("prov_source") for e in edges
    ).most_common():
        print(f"     {count:5}  {name}")
    print("  the 21 '?' edges:")
    labels = {n["id"]: n["label"] for n in graph["nodes"]}
    for edge in edges:
        if edge.get("sign") == "?":
            src = labels.get(edge["source"], edge["source"])
            tgt = labels.get(edge["target"], edge["target"])
            print(f"     {src[:44]:46} -> {tgt[:40]}")


def topology(graph: dict) -> None:
    header("§3.6 — degree roles and the source->sink fan")
    edges = graph["causal_edges"]
    nodes = {n["id"]: n for n in graph["nodes"]}
    out_deg = collections.Counter(e["source"] for e in edges)
    in_deg = collections.Counter(e["target"] for e in edges)

    def is_source(nid: str) -> bool:
        return in_deg[nid] == 0

    def is_sink(nid: str) -> bool:
        return out_deg[nid] == 0

    pure_source = sum(1 for n in nodes if is_source(n) and not is_sink(n))
    pure_sink = sum(1 for n in nodes if is_sink(n) and not is_source(n))
    internal = sum(1 for n in nodes if not is_source(n) and not is_sink(n))
    isolated = sum(1 for n in nodes if is_source(n) and is_sink(n))
    total = len(nodes)
    for label, value in (
        ("pure source (in-degree 0)", pure_source),
        ("pure sink (out-degree 0)", pure_sink),
        ("internal (both)", internal),
        ("isolated (neither)", isolated),
    ):
        print(f"  {label:30} {value:5}  ({100 * value / total:.1f}%)")
    fan = [e for e in edges if is_source(e["source"]) and is_sink(e["target"])]
    print(
        f"  pure-source -> pure-sink edges: {len(fan)} ({100 * len(fan) / len(edges):.1f}% of edges)"
    )
    print("  top pure sources by out-degree:")
    labels = {n: nodes[n]["label"] for n in nodes}
    sources = [n for n in nodes if is_source(n) and out_deg[n] > 0]
    for nid in sorted(sources, key=lambda x: -out_deg[x])[:8]:
        print(f"     out={out_deg[nid]:3}  {labels[nid][:60]}")

    print("  scale transitions:")
    order = [
        "molecular",
        "subcellular",
        "cellular",
        "tissue",
        "organ",
        "organ_system",
        "organism",
    ]
    rank = {s: i for i, s in enumerate(order)}
    scale = {n: nodes[n].get("scale") for n in nodes}
    up = down = same = 0
    for edge in edges:
        a, b = scale.get(edge["source"]), scale.get(edge["target"])
        if a in rank and b in rank:
            if rank[b] > rank[a]:
                up += 1
            elif rank[b] < rank[a]:
                down += 1
            else:
                same += 1
    print(f"     finer->coarser {up}   same-scale {same}   coarser->finer {down}")


def duplicates_and_conflicts(graph: dict) -> None:
    header("§3.8 — duplicate traits and sign conflicts")
    nodes = graph["nodes"]
    # The report's predicate: group only nodes carrying BOTH an entity and a quality IRI.
    # Reported alongside are the two looser predicates, since they give different totals
    # while leaving the same-label conclusion unchanged.
    for label, pred in (
        (
            "both entity_iri and quality_iri",
            lambda n: n.get("entity_iri") and n.get("quality_iri"),
        ),
        ("all nodes", lambda n: True),
        ("entity_iri present", lambda n: n.get("entity_iri")),
    ):
        groups: dict[tuple, list] = collections.defaultdict(list)
        for node in nodes:
            if pred(node):
                groups[(node.get("entity_iri"), node.get("quality_iri"))].append(node)
        collisions = {k: v for k, v in groups.items() if len(v) > 1}
        same_label = [
            v for v in collisions.values() if len({x["label"] for x in v}) == 1
        ]
        print(
            f"  [{label:32}] collisions={len(collisions):4}  "
            f"same-label groups={len(same_label)}  redundant nodes={sum(len(v) - 1 for v in same_label)}"
        )
    groups = collections.defaultdict(list)
    for node in nodes:
        if node.get("entity_iri") and node.get("quality_iri"):
            groups[(node["entity_iri"], node["quality_iri"])].append(node)
    for members in groups.values():
        if len(members) > 1 and len({m["label"] for m in members}) == 1:
            print(f"     x{len(members)}  {members[0]['label'][:58]}")
            print(f"          {[m['id'] for m in members]}")

    pairs = collections.Counter(
        (e["source"], e["target"]) for e in graph["causal_edges"]
    )
    labels = {n["id"]: n["label"] for n in nodes}
    for (src, tgt), count in pairs.items():
        if count > 1:
            signs = [
                e["sign"]
                for e in graph["causal_edges"]
                if e["source"] == src and e["target"] == tgt
            ]
            if len(set(signs)) > 1:
                print(
                    f"  SIGN CONFLICT: {labels[src][:40]} -> {labels[tgt][:34]}  signs={signs}"
                )


def parse_lesions(field: str) -> list[str]:
    """Split ``primary_intervention`` into lesion variable ids.

    27 of the 866 rows hold two lesion variables separated by ``;`` (ARSA, CTNS, KYNU,
    PKLR). Each entry is ``<variable> <direction>``; the trailing direction token is
    dropped. Failing to split here is the bug this script was written to prevent.
    """
    out = []
    for part in field.split(";"):
        part = part.strip()
        if part:
            out.append(part.rsplit(" ", 1)[0].strip())
    return out


def benchmark_depth(graph: dict, rows: list[dict]) -> None:
    header("§3.7 — lesion-to-readout depth over the 866 adjudicated pairs")
    ids = {n["id"] for n in graph["nodes"]}
    adjacency = collections.defaultdict(list)
    for edge in graph["causal_edges"]:
        adjacency[edge["source"]].append(edge["target"])
    for edge in graph.get("production_edges", []):
        src = edge.get("source") or edge.get("producer")
        tgt = edge.get("target") or edge.get("product")
        if src and tgt:
            adjacency[src].append(tgt)

    cache: dict[str, dict[str, int]] = {}

    def distances(start: str) -> dict[str, int]:
        if start not in cache:
            dist = {start: 0}
            queue = collections.deque([start])
            while queue:
                node = queue.popleft()
                for nxt in adjacency.get(node, ()):
                    if nxt not in dist:
                        dist[nxt] = dist[node] + 1
                        queue.append(nxt)
            cache[start] = dist
        return cache[start]

    multi = sum(1 for r in rows if ";" in r["primary_intervention"])
    genes = sorted({r["gene"] for r in rows if ";" in r["primary_intervention"]})
    print(
        f"  rows with multiple lesion variables: {multi}  (genes: {', '.join(genes)})"
    )

    for mode in ("min-over-lesions", "first-lesion-only"):
        depths: collections.Counter[int] = collections.Counter()
        unreachable = unresolved = 0
        for row in rows:
            lesions = parse_lesions(row["primary_intervention"])
            if mode == "first-lesion-only":
                lesions = lesions[:1]
            lesions = [item for item in lesions if item in ids]
            target = row["physiomap_variable"].strip()
            if not lesions or target not in ids:
                unresolved += 1
                continue
            found = [
                d
                for d in (distances(item).get(target) for item in lesions)
                if d is not None
            ]
            if found:
                depths[min(found)] += 1
            else:
                unreachable += 1
        reachable = sum(depths.values())
        within2 = sum(v for k, v in depths.items() if k <= 2)
        within4 = sum(v for k, v in depths.items() if k <= 4)
        print(
            f"  [{mode:18}] reachable={reachable:4} ({100 * reachable / len(rows):.1f}%)  "
            f"unreachable={unreachable:4} ({100 * unreachable / len(rows):.1f}%)  unresolved={unresolved}"
        )
        print(
            f"       one-hop={depths[1]} ({100 * depths[1] / reachable:.1f}% of reachable)   "
            f"<=2: {100 * within2 / reachable:.1f}%   <=4: {100 * within4 / reachable:.1f}%"
        )


# --------------------------------------------------------------------------------------
# Part IV — the dismech side of the comparison
# --------------------------------------------------------------------------------------

# Directories walked for the Part IV counts. kb/groupings is excluded: a Grouping has no
# `pathophysiology` block, so it contributes no nodes, edges or modifiers.
KB_DIRS = ("kb/disorders", "kb/modules", "kb/comorbidities")

# The modifier census counts `modifier:` on the three ontology-bound descriptor lists that
# hang off a pathophysiology node, and nowhere else. Descriptor lists elsewhere in an entry
# (phenotypes, biochemical, treatments, ...) also carry `modifier:`, so a whole-file count
# is a larger number measuring a different thing. Naming the scope here is the point: the
# figure in §4.1 is about polarity attached to *pathograph nodes*, which is what the
# unsigned-edge argument is contrasted against.
MODIFIER_SECTIONS = ("biological_processes", "molecular_functions", "cell_types")

# Words in a `downstream[].description` that suggest the edge is negative in sign. Crude by
# construction — it cannot separate "A inhibits B" from "A causes impaired B", which imply
# opposite edge signs — so the report cites it as evidence that polarity language is
# pervasive in the prose, never as a measurement of how many edges are negative.
NEGATIVE_HINT = re.compile(
    r"\b(inhibit|suppress|decreas|reduc|block|impair|loss of|deplet|antagoni)"
)


def dismech_counts(repo_root: Path) -> None:
    header("§4 / §4.1 / §4.3 — dismech pathograph counts")
    print(f"  directories: {', '.join(KB_DIRS)}")
    print(
        f"  modifier scope: pathophysiology[].{{{', '.join(MODIFIER_SECTIONS)}}}[].modifier"
    )

    try:
        import yaml
    except ImportError:  # pragma: no cover - PyYAML is a project dependency
        sys.exit("PyYAML is required; run under `uv run`.")

    nodes = edges = files = neg = skipped = 0
    modifiers: collections.Counter[str] = collections.Counter()
    cyclic: set[str] = set()
    self_loops: list[tuple[str, str]] = []

    for directory in KB_DIRS:
        for path in sorted((repo_root / directory).glob("*.yaml")):
            try:
                with path.open() as handle:
                    entry = yaml.safe_load(handle)
            except Exception as exc:
                # A metrics script that drops a file silently undercounts without
                # saying so, which is the failure shape this script exists to prevent.
                skipped += 1
                print(f"  SKIPPED (unparsable): {path.name}: {exc}")
                continue
            if not isinstance(entry, dict):
                skipped += 1
                print(f"  SKIPPED (not a mapping): {path.name}")
                continue
            pathophysiology = entry.get("pathophysiology") or []
            if not pathophysiology:
                continue
            files += 1
            names = {p.get("name") for p in pathophysiology if isinstance(p, dict)}
            adjacency: dict[str, set[str]] = collections.defaultdict(set)
            for node in pathophysiology:
                if not isinstance(node, dict):
                    continue
                nodes += 1
                name = node.get("name")
                for section in MODIFIER_SECTIONS:
                    for item in node.get(section) or []:
                        if isinstance(item, dict) and item.get("modifier"):
                            modifiers[item["modifier"]] += 1
                for edge in node.get("downstream") or []:
                    if not isinstance(edge, dict):
                        continue
                    edges += 1
                    if NEGATIVE_HINT.search((edge.get("description") or "").lower()):
                        neg += 1
                    target = edge.get("target")
                    if target in names:
                        if target == name:
                            self_loops.append((path.name, name))
                        else:
                            adjacency[name].add(target)
            if _has_cycle(names, adjacency):
                cyclic.add(path.name)

    if not files:
        sys.exit(f"no entries with a pathophysiology block under {repo_root}")
    print(f"  pathophysiology nodes: {nodes}")
    print(f"  downstream edges:      {edges}")
    print(f"  files with a non-empty pathophysiology block: {files}")
    print(f"  files skipped: {skipped}")
    print(
        f"  files with a multi-node cycle: {len(cyclic)} ({100 * len(cyclic) / files:.1f}%)"
    )
    print(f"  self-loop edges: {len(self_loops)}")
    for name, node in self_loops:
        print(f"     {name}: {node!r} -> itself")
    share = f" ({100 * neg / edges:.1f}%)" if edges else ""
    print(f"  negative-language edge descriptions: {neg}{share}")
    print("  modifier census:")
    for name, count in modifiers.most_common():
        print(f"     {name:22} {count:6}")


def _has_cycle(names: set, adjacency: dict) -> bool:
    """True if the intra-file pathograph contains a multi-node cycle (self-loops excluded)."""
    color: dict = {}
    for start in names:
        if color.get(start, 0) != 0:
            continue
        stack = [(start, iter(adjacency.get(start, ())))]
        color[start] = 1
        while stack:
            node, children = stack[-1]
            advanced = False
            for child in children:
                state = color.get(child, 0)
                if state == 1:
                    return True
                if state == 0:
                    color[child] = 1
                    stack.append((child, iter(adjacency.get(child, ()))))
                    advanced = True
                    break
            if not advanced:
                color[node] = 2
                stack.pop()
    return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "physiomap_root",
        type=Path,
        nargs="?",
        help="Root of a PhysioMap repository clone (regenerates the Part III figures)",
    )
    parser.add_argument(
        "--dismech",
        type=Path,
        metavar="REPO_ROOT",
        help="Root of this repository (regenerates the Part IV dismech-side figures)",
    )
    args = parser.parse_args()

    if not args.physiomap_root and not args.dismech:
        parser.error("pass a PhysioMap clone path, --dismech <repo root>, or both")

    if args.physiomap_root:
        graph, rows = load(args.physiomap_root)
        counts_and_reconciliation(graph)
        node_anatomy(graph)
        edge_signs_and_provenance(graph)
        topology(graph)
        duplicates_and_conflicts(graph)
        benchmark_depth(graph, rows)

    if args.dismech:
        dismech_counts(args.dismech)


if __name__ == "__main__":
    main()
