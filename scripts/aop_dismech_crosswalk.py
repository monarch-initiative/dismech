#!/usr/bin/env python3
"""Cross-walk AOP-Wiki Key Events onto dismech pathograph nodes, for any AOP.

Given a set of Key Events (an AOP's, or a list of ids) and a set of dismech
entries, this script reports which pathophysiology nodes and phenotypes of each
entry match each Key Event, on what basis, and whether the node's
``biological_scale`` agrees with the Event's level of biological organization.
For the Key Event Relationships among those Events it reports whether the
entry's causal edges assert them. It reports; it changes nothing, and it does
not propose curation.

It generalizes ``scripts/aop_parkinsonism_crosswalk.py``, which stays as it is
and still reproduces its 2026-10-25 report. That script types its twelve Key
Events in and matches each with hand-written rules; this one reads the Key
Events from the ``aop-wiki-cli`` cache and matches them automatically, and
takes hand-written rules from a file when a curator has them.

What the AOP side is read from
------------------------------
The parsed cache ``aop-wiki-cli`` writes for one AOP-Wiki XML export:
``<data-dir>/outputs/cache/<MM-DD-YYYY>/all_events_*.json``, ``all_aops_*.json``
and ``all_kers_*.json``. The data directory and the date are always given
explicitly; nothing here downloads or parses the XML. ``all_kers_*.json``
exists only after a KER command has run for that date; without it the Key
Event Relationship part is skipped.

How a node is matched to a Key Event
------------------------------------
Automatically, from the Event's own record, strongest basis first:

- ``term``: the node binds an id one of the Event's components names (its
  biological process or object), in any term-bearing field;
- ``conforms_to``: the node conforms to a module node that binds such an id;
- ``label``: a cell type or location of the node has the label of the Event's
  cell or organ term. The cache carries those two terms as labels only, so this
  says where the node happens, not what it is about: a weak basis, to discount
  unless a stronger one also fired. Root-like labels AOP-Wiki uses as
  placeholders (``organ``, ``eukaryotic cell``) are ignored;
- ``name``: every content word of the Event's title is in the node's name.
  The weakest basis; discount it.

An entry phenotype matches when it binds an HP or MP id a component names.

With ``--rules FILE``, a Key Event listed in the file is matched by its rules
instead (see ``conf/aop_crosswalk/parkinsonism.yaml`` for the format), and the
automatic matching is not applied to it. Each match records the bases that
fired, so a reader can tell a binding match from a word match.

    python scripts/aop_dismech_crosswalk.py --data-dir ~/aop-data --date 10-03-2026 \\
        --aop 40 --entry Contact_Dermatitis
    python scripts/aop_dismech_crosswalk.py ... --ke-ids 396,826 --all --format tsv
    python scripts/aop_dismech_crosswalk.py ... --aop 3 --rules conf/aop_crosswalk/parkinsonism.yaml
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import deque
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dismech import kb_cache
from dismech.kb_cache import load_document
from dismech.qc_plugins import CAUSAL_PREDICATES
from dismech.repo_root import repo_root

MAX_INDIRECT_HOPS = 3
DATE = re.compile(r"^\d{2}-\d{2}-\d{4}$")

# AOP-Wiki level -> dismech biological_scale. dismech's TISSUE covers tissue and organ.
SCALE_FOR_LEVEL = {
    "Molecular": "MOLECULAR",
    "Cellular": "CELLULAR",
    "Tissue": "TISSUE",
    "Organ": "TISSUE",
    "Individual": "ORGANISM",
}
TERM_FIELDS = (
    "biological_processes",
    "molecular_functions",
    "cellular_components",
    "cell_types",
    "locations",
    "chemical_entities",
)
PHENOTYPE_PREFIXES = ("HP:", "MP:")
# Cell and organ term labels AOP-Wiki uses as placeholders. A label basis on one says
# nothing about the node, so they are not matched.
PLACEHOLDER_LABELS = frozenset({
    "cell", "eukaryotic cell", "native cell", "organ", "tissue", "anatomical structure",
    "multicellular organism", "organism",
})
# Words in a Key Event title that name a direction or kind of change, not the thing
# changed. They are left out of the name basis.
TITLE_STOPWORDS = frozenset({
    "a", "an", "and", "by", "in", "into", "of", "on", "or", "the", "to", "with", "via",
    "leading", "leads", "increase", "increased", "decrease", "decreased", "activation",
    "activated", "inhibition", "inhibited", "impaired", "reduced", "reduction",
    "elevated", "altered", "alteration", "loss", "binding",
})


# ---------------------------------------------------------------------------
# The AOP side: the aop-wiki-cli cache.


def cache_dir(data_dir: Path, date: str) -> Path:
    if not DATE.match(date):
        raise SystemExit(f"--date takes MM-DD-YYYY, as aop-wiki-cli does; got {date!r}")
    return data_dir / "outputs" / "cache" / date


def load_cache(data_dir: Path, date: str, kind: str) -> dict | None:
    """One of the cache files (``events``, ``aops``, ``kers``), or None if absent."""
    path = cache_dir(data_dir, date) / f"all_{kind}_{date}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def _curie(term: dict) -> str | None:
    source_id = (term or {}).get("source_id")
    if not source_id:
        return None
    if ":" in source_id:
        return source_id
    source = (term or {}).get("source")
    return f"{source}:{source_id}" if source else source_id


def key_event(event: dict) -> dict:
    """The parts of a cached Event the matching uses."""
    ids = set()
    for component in event.get("ecs") or []:
        for part in ("biological_process", "biological_object"):
            curie = _curie(component.get(part) or {})
            if curie:
                ids.add(curie)
    return {
        "id": str(event["ke_id"]),
        "title": event.get("title") or "",
        "level": event.get("level_of_biological_organization"),
        "term_ids": sorted(ids),
        "cell_label": ((event.get("cell_term") or {}).get("term") or "").lower() or None,
        "organ_label": ((event.get("organ_term") or {}).get("term") or "").lower() or None,
    }


def select_key_events(
    events: dict, aops: dict | None, aop_ids: list[str], ke_ids: list[str]
) -> list[str]:
    chosen: list[str] = []
    for aop_id in aop_ids:
        if not aops or aop_id not in aops:
            raise SystemExit(f"AOP {aop_id} is not in the cache")
        chosen += [str(e) for e in aops[aop_id].get("event_ids") or []]
    chosen += ke_ids
    missing = [ke for ke in chosen if ke not in events]
    if missing:
        raise SystemExit(f"Key Event(s) not in the cache: {', '.join(missing)}")
    return list(dict.fromkeys(chosen))


def select_kers(
    kers: dict, aops: dict | None, aop_ids: list[str], key_events: list[str]
) -> dict[str, dict]:
    """The KERs to check: those the AOPs list, or else those joining two listed Events."""
    if aop_ids:
        ids = [k for a in aop_ids for k in (aops[a].get("kers") or {})]
    else:
        wanted = set(key_events)
        ids = [
            k
            for k, r in kers.items()
            if str((r.get("upstream_ke") or {}).get("id")) in wanted
            and str((r.get("downstream_ke") or {}).get("id")) in wanted
        ]
    chosen = {}
    for ker in dict.fromkeys(ids):
        record = kers.get(ker)
        if not record:
            continue
        chosen[ker] = {
            "upstream": str(record["upstream_ke"]["id"]),
            "downstream": str(record["downstream_ke"]["id"]),
            "aops": [str(a) for a in record.get("aop_ids") or []],
            "cited": bool(re.sub(r"<[^>]+>|&nbsp;|\s", "", record.get("references") or "")),
        }
    return chosen


# ---------------------------------------------------------------------------
# The dismech side.


def _term_ids(node: dict, key: str) -> set[str]:
    return {(item.get("term") or {}).get("id") for item in node.get(key) or []} - {None}


def _term_labels(node: dict, key: str) -> set[str]:
    return {
        ((item.get("term") or {}).get("label") or "").lower()
        for item in node.get(key) or []
    } - {""}


def _conforms_to(node: dict) -> list[str]:
    value = node.get("conforms_to")
    if not value:
        return []
    return value if isinstance(value, list) else [value]


class Modules:
    """Module nodes by ``<module>#<node name>``, read on first use."""

    def __init__(self, root: Path):
        self.root = root
        self.nodes: dict[str, dict] = {}
        self.loaded: set[str] = set()

    def node(self, ref: str) -> dict | None:
        module = ref.partition("#")[0]
        if module not in self.loaded:
            self.loaded.add(module)
            path = self.root / "kb" / "modules" / f"{module}.yaml"
            if path.exists():
                for node in load_document(path).get("pathophysiology") or []:
                    self.nodes[f"{module}#{node['name']}"] = node
        return self.nodes.get(ref)


# ---------------------------------------------------------------------------
# Matching.


def _title_words(title: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", title.lower())
    return [w for w in words if len(w) > 2 and w not in TITLE_STOPWORDS]


def _has_word(name: str, word: str) -> bool:
    """``word`` is in ``name`` as a word, allowing a plural on either side."""
    stem = word.removesuffix("s")
    return re.search(rf"\b{re.escape(stem)}s?\b", name) is not None


def match_automatic(node: dict, ke: dict, modules: Modules) -> list[str]:
    """The bases on which ``node`` matches Key Event ``ke`` from the Event's own record."""
    bases: list[str] = []
    wanted = set(ke["term_ids"])

    for field in TERM_FIELDS:
        shared = _term_ids(node, field) & wanted
        if shared:
            bases.append(f"term {','.join(sorted(shared))} ({field})")

    for ref in _conforms_to(node):
        module_node = modules.node(ref)
        if module_node is None:
            continue
        shared = set().union(*(_term_ids(module_node, f) for f in TERM_FIELDS)) & wanted
        if shared:
            bases.append(f"conforms_to {ref} (term {','.join(sorted(shared))})")

    for label, field in ((ke["cell_label"], "cell_types"), (ke["organ_label"], "locations")):
        if label and label not in PLACEHOLDER_LABELS and label in _term_labels(node, field):
            bases.append(f"label {label} ({field})")

    words = _title_words(ke["title"])
    name = node["name"].lower()
    if words and all(_has_word(name, w) for w in words):
        bases.append("name " + ",".join(words))
    return bases


def match_rules(node: dict, rules: dict) -> list[str]:
    """The bases on which ``node`` matches a Key Event under its hand-written rules.

    The order, and the basis strings, are those of
    ``aop_parkinsonism_crosswalk.match_key_event``, so the two agree on its rules.
    """
    name = node["name"].lower()
    description = (node.get("description") or "").lower()
    name_pattern = rules.get("name_pattern")
    bases: list[str] = []

    for conformance in _conforms_to(node):
        for prefix in rules.get("conforms_to_prefixes") or []:
            whole_module = prefix.endswith("#")
            node_part = conformance.split("#", 1)[1].lower() if "#" in conformance else ""
            if conformance.startswith(prefix) and (
                not whole_module or (name_pattern and re.search(name_pattern, node_part))
            ):
                bases.append(f"conforms_to {conformance}")
                break

    go_ids = set(rules.get("go_ids") or [])
    shared_go = (
        _term_ids(node, "biological_processes") | _term_ids(node, "molecular_functions")
    ) & go_ids
    if shared_go:
        bases.append("GO " + ",".join(sorted(shared_go)))

    def holds(condition: dict) -> bool:
        for field, key in (
            ("cell_types", "cell_types_any"),
            ("locations", "locations_any"),
            ("biological_processes", "processes_any"),
        ):
            if key in condition and not (_term_ids(node, field) & set(condition[key])):
                return False
        if "name_pattern" in condition and not re.search(condition["name_pattern"], name):
            return False
        return not (
            "description_pattern" in condition
            and not re.search(condition["description_pattern"], description)
        )

    conditions = rules.get("conditions") or []
    for condition in conditions:
        if not condition.get("only_if_unmatched") and holds(condition):
            bases.append(condition["label"])

    if name_pattern and re.search(name_pattern, name):
        bases.append("name")

    if not bases:
        for condition in conditions:
            if condition.get("only_if_unmatched") and holds(condition):
                bases.append(condition["label"])
    return bases


def level_agreement(node: dict, ke: dict) -> str:
    scale = node.get("biological_scale")
    expected = SCALE_FOR_LEVEL.get(ke["level"])
    if not scale:
        return "node has no scale"
    if not expected:
        return f"Event level {ke['level']} has no dismech scale"
    return "agrees" if scale == expected else "differs"


# ---------------------------------------------------------------------------
# One entry.


def causal_graph(nodes: list[dict]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for node in nodes:
        for edge in node.get("downstream") or []:
            if edge.get("predicate", "causes") in CAUSAL_PREDICATES:
                graph.setdefault(node["name"], []).append(edge["target"])
    return graph


def shortest_path(
    graph: dict[str, list[str]], sources: set[str], targets: set[str]
) -> list[str] | None:
    best: list[str] | None = None
    for source in sorted(sources):
        queue = deque([(source, [source])])
        while queue:
            current, path = queue.popleft()
            if len(path) - 1 >= MAX_INDIRECT_HOPS:
                continue
            for nxt in graph.get(current, []):
                if nxt in path:
                    continue
                if nxt in targets:
                    if best is None or len(path) + 1 < len(best):
                        best = path + [nxt]
                    continue
                queue.append((nxt, path + [nxt]))
    return best


def match_entry(
    record: dict, key_events: dict[str, dict], rules: dict[str, dict], modules: Modules
) -> dict[str, dict[str, dict]]:
    """Key Event id -> matched node or phenotype name -> what matched."""
    matches: dict[str, dict[str, dict]] = {ke: {} for ke in key_events}
    nodes = record.get("pathophysiology") or []
    phenotypes = [
        (p.get("name"), ((p.get("phenotype_term") or {}).get("term") or {}).get("id"))
        for p in record.get("phenotypes") or []
    ]
    for ke_id, ke in key_events.items():
        rule = rules.get(ke_id)
        for node in nodes:
            bases = match_rules(node, rule) if rule else match_automatic(node, ke, modules)
            if bases:
                matches[ke_id][node["name"]] = {
                    "kind": "node",
                    "bases": bases,
                    "scale": node.get("biological_scale"),
                    "level": level_agreement(node, ke),
                }
        if rule:
            wanted = set((rule.get("phenotypes") or {}).get("term_ids") or [])
            label = (rule.get("phenotypes") or {}).get("label", "phenotype")
            found = {name: [label] for name, tid in phenotypes if tid in wanted}
        else:
            wanted = {t for t in ke["term_ids"] if t.startswith(PHENOTYPE_PREFIXES)}
            found = {name: [f"phenotype {tid}"] for name, tid in phenotypes if tid in wanted}
        for name in sorted(found):
            # A phenotype named like a matched node would overwrite it.
            key = f"{name} (phenotype)" if name in matches[ke_id] else name
            matches[ke_id][key] = {"kind": "phenotype", "bases": found[name]}
    return matches


def ker_coverage(
    record: dict, matches: dict[str, dict[str, dict]], kers: dict[str, dict]
) -> dict[str, dict]:
    """Whether the entry's causal edges assert each KER, between the nodes matched to its Events."""
    graph = causal_graph(record.get("pathophysiology") or [])
    found = {}
    for ker, info in kers.items():
        up = set(matches.get(info["upstream"], {}))
        down = set(matches.get(info["downstream"], {}))
        direct = sorted((s, t) for s in up for t in graph.get(s, []) if t in down and t != s)
        if direct:
            found[ker] = {"status": "direct", "edges": direct}
        elif up & down:
            found[ker] = {"status": "same node", "nodes": sorted(up & down)}
        elif up and down:
            via = shortest_path(graph, up, down)
            found[ker] = {"status": "indirect", "path": via} if via else {"status": "no path"}
        else:
            found[ker] = {
                "status": "key event absent",
                "absent": [
                    ke
                    for ke, side in ((info["upstream"], up), (info["downstream"], down))
                    if not side
                ],
            }
    return found


def crosswalk(
    record: dict,
    path: Path,
    key_events: dict[str, dict],
    kers: dict[str, dict],
    rules: dict[str, dict],
    modules: Modules,
) -> dict:
    matches = match_entry(record, key_events, rules, modules)
    return {
        "path": str(path),
        "name": record.get("name"),
        "nodes": len(record.get("pathophysiology") or []),
        "key_events": matches,
        "key_events_present": sorted(ke for ke, m in matches.items() if m),
        "kers": ker_coverage(record, matches, kers),
    }


# ---------------------------------------------------------------------------
# Output.


def render_summary(result: dict, out) -> None:
    kes, kers = result["key_events"], result["kers"]
    print(
        f"AOP-Wiki snapshot {result['snapshot']}; {len(kes)} Key Events; "
        f"{len(result['entries'])} dismech entries",
        file=out,
    )
    if result["rules"]:
        print(f"Rules from {result['rules']} for KE {', '.join(result['ruled'])}", file=out)
    for ke_id, ke in kes.items():
        present = [e for e in result["entries"] if e["key_events"][ke_id]]
        terms = ", ".join(ke["term_ids"]) or "none"
        print(
            f"\nKE{ke_id} {ke['title']} [{ke['level']}; component terms: {terms}]"
            f"  {len(present)}/{len(result['entries'])} entries",
            file=out,
        )
        for entry in present:
            print(f"  {Path(entry['path']).stem}", file=out)
            for name, match in entry["key_events"][ke_id].items():
                if match["kind"] != "node":
                    level = ""
                elif match["scale"]:
                    level = f" [{match['scale']}: {match['level']}]"
                else:
                    level = " [no scale]"
                kind = "" if match["kind"] == "node" else " (phenotype)"
                print(f"    {name}{kind}{level}: {'; '.join(match['bases'])}", file=out)
    if kers is None:
        print("\nNo all_kers cache for this date; Key Event Relationships not checked.", file=out)
        return
    print("\nKey Event Relationship coverage", file=out)
    for ker, info in kers.items():
        counts: dict[str, int] = {}
        for entry in result["entries"]:
            status = entry["kers"][ker]["status"]
            counts[status] = counts.get(status, 0) + 1
        print(
            f"  KER{ker} KE{info['upstream']}->KE{info['downstream']} "
            f"(AOP {','.join(info['aops'])}; {'cited' if info['cited'] else 'UNCITED'})  "
            + " ".join(f"{s.replace(' ', '-')}={n}" for s, n in sorted(counts.items())),
            file=out,
        )


def render_tsv(result: dict, out) -> None:
    print("entry\tkey_event\tmatched\tkind\tscale\tlevel\tbases", file=out)
    for entry in result["entries"]:
        stem = Path(entry["path"]).stem
        for ke_id, found in entry["key_events"].items():
            for name, match in found.items():
                print(
                    f"{stem}\tKE{ke_id}\t{name}\t{match['kind']}\t{match.get('scale') or ''}"
                    f"\t{match.get('level') or ''}\t{'; '.join(match['bases'])}",
                    file=out,
                )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=os.environ.get("AOP_WIKI_CLI_DATA_DIR"),
        help="aop-wiki-cli data directory (default: $AOP_WIKI_CLI_DATA_DIR)",
    )
    parser.add_argument("--date", required=True, help="snapshot date, MM-DD-YYYY")
    parser.add_argument("--aop", action="append", default=[], help="AOP id; repeatable")
    parser.add_argument("--ke-ids", default="", help="comma-separated Key Event ids")
    parser.add_argument("--entry", action="append", default=[], help="dismech entry slug; repeatable")
    parser.add_argument("--all", action="store_true", help="every entry in kb/disorders/")
    parser.add_argument("--rules", type=Path, help="hand-written matching rules (YAML)")
    parser.add_argument(
        "--root", type=Path, default=None, help="dismech checkout (default: the one at or above cwd)"
    )
    parser.add_argument("--format", choices=["summary", "json", "tsv"], default="summary")
    args = parser.parse_args(argv)

    if args.data_dir is None:
        parser.error("give --data-dir or set AOP_WIKI_CLI_DATA_DIR")
    ke_ids = [k.strip() for k in args.ke_ids.split(",") if k.strip()]
    if not (args.aop or ke_ids):
        parser.error("give --aop or --ke-ids")
    if bool(args.entry) == args.all:
        parser.error("give --entry (repeatable) or --all, not both")

    events = load_cache(args.data_dir, args.date, "events")
    if events is None:
        raise SystemExit(f"no events cache for {args.date} under {args.data_dir}")
    aops = load_cache(args.data_dir, args.date, "aops")
    kers_cache = load_cache(args.data_dir, args.date, "kers")

    chosen = select_key_events(events, aops, args.aop, ke_ids)
    key_events = {ke: key_event(events[ke]) for ke in chosen}
    kers = select_kers(kers_cache, aops, args.aop, chosen) if kers_cache is not None else {}
    if args.root is None:
        args.root = repo_root()
    rules = {}
    if args.rules:
        loaded = yaml.safe_load(args.rules.read_text()) or {}
        if not isinstance(loaded.get("key_events"), dict):
            raise SystemExit(f"{args.rules}: expected a top-level key_events: mapping of Key Event ids")
        rules = {str(k): v for k, v in loaded["key_events"].items()}

    if args.all:
        kb_cache.default_off()  # one walk of the corpus; nothing to reuse
        paths = sorted((args.root / "kb" / "disorders").glob("*.yaml"))
    else:
        paths = [args.root / "kb" / "disorders" / f"{slug}.yaml" for slug in args.entry]
        missing = [str(p) for p in paths if not p.exists()]
        if missing:
            raise SystemExit(f"no such entry: {', '.join(missing)}")
    modules = Modules(args.root)
    entries = [
        crosswalk(load_document(p), p.relative_to(args.root), key_events, kers, rules, modules)
        for p in paths
    ]
    result = {
        "snapshot": args.date,
        "rules": str(args.rules) if args.rules else None,
        "ruled": sorted(k for k in key_events if k in rules),
        "key_events": key_events,
        "kers": kers if kers_cache is not None else None,
        "entries": entries,
    }

    if args.format == "json":
        json.dump(result, sys.stdout, indent=1)
        print()
    elif args.format == "tsv":
        render_tsv(result, sys.stdout)
    else:
        render_summary(result, sys.stdout)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
