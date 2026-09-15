#!/usr/bin/env python3
"""Prototype: project every dismech pathograph into one cross-disease mega-graph.

Every disorder, module and comorbidity entry carries its own pathograph, and a
mechanism that recurs across diseases is re-curated once per disease. This
script collapses all of them into a single graph by giving each disease-local
node a **canonical mechanism identity**, then reports what that merge costs and
what it buys. It is a measurement instrument for
``docs/superpowers/plans/2026-09-15-mega-pathograph-projection.md``, not a
published artifact: nothing in ``kb/`` depends on it and it writes nothing.

The identity ladder (see the plan for the argument):

1. ``module_node``   -- a ``kb/modules/`` node is its own canonical identity.
2. ``conforms_to``   -- a disorder node that declares conformance *is* an
                        instance of that module node. Curator-asserted, so this
                        is the gold standard and the evaluation label.
3. ``hp_term``       -- a phenotype grounded in HP is identified by its term.
4. ``core_terms``    -- an identity-bearing grounding (GO / CHEBI / HGNC / NCIT
                        / ECTO) keyed together with its CL/UBERON *context*.
5. ``name_only``     -- normalized node name, within a node type. Weakest rung;
                        never merges across node types.

Context prefixes (CL, UBERON) deliberately cannot carry identity on their own:
keying on them alone collapses 207 unrelated nodes onto "neuron" and
manufactures self-loops out of causally distinct events.

Edges are taken from ``dismech.graph.build_causal_graph`` rather than re-derived,
so bare-name target resolution, phenotype sequelae, treatment and environmental
links behave exactly as they do on the rendered pages.

Usage::

    uv run python scripts/megagraph_prototype.py                 # summary JSON
    uv run python scripts/megagraph_prototype.py --min-support 2 # backbone only
    uv run python scripts/megagraph_prototype.py --format tsv    # merged edges
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from dismech.graph import build_causal_graph, iter_variant_items
from dismech.yaml_io import safe_load

#: Sections whose items can appear as pathograph nodes.
SECTIONS = (
    "pathophysiology",
    "phenotypes",
    "environmental",
    "genetic",
    "treatments",
    "biochemical",
    "experimental_models",
    "computational_models",
    "variants",
)

#: Prefixes that can carry a node's identity on their own.
CORE_PREFIXES = frozenset({"GO", "CHEBI", "HP", "NCIT", "HGNC", "PR", "ECTO"})
#: Prefixes that qualify an identity but never establish one.
CONTEXT_PREFIXES = frozenset({"CL", "UBERON"})

#: Dropped before name normalization -- they carry no discriminating content.
STOPWORDS = frozenset({"the", "of", "and", "in", "a", "to", "with", "due"})

#: Slots holding *links to other nodes*; their terms belong to the edge, not
#: to this node's identity.
_LINK_SLOTS = frozenset(
    {
        "evidence",
        "downstream",
        "sequelae",
        "reports_on",
        "target_mechanisms",
        "influences_mechanisms",
        "modeled_mechanisms",
    }
)


def normalize_name(value: Any) -> str:
    """Lowercase, strip punctuation, drop stopwords, order-insensitive."""
    tokens = re.sub(r"[^a-z0-9]+", " ", str(value).lower()).split()
    return " ".join(sorted({t for t in tokens if t not in STOPWORDS}))


def collect_terms(item: Any) -> dict[str, set[str]]:
    """Map ontology prefix -> CURIEs bound anywhere inside one section item."""
    found: dict[str, set[str]] = defaultdict(set)

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            term = value.get("term")
            if isinstance(term, dict) and term.get("id"):
                curie = str(term["id"])
                found[curie.split(":")[0].upper()].add(curie)
            for key, nested in value.items():
                if key not in _LINK_SLOTS:
                    walk(nested)
        elif isinstance(value, list):
            for entry in value:
                walk(entry)

    walk(item)
    return found


def entry_files(kb_dir: Path) -> list[tuple[str, Path]]:
    """Every entry file, modules first so their anchors exist before use."""
    out: list[tuple[str, Path]] = []
    for sub in ("modules", "disorders", "comorbidities"):
        directory = kb_dir / sub
        if directory.is_dir():
            out.extend((sub, path) for path in sorted(directory.glob("*.yaml")))
    return out


def module_anchors(files: list[tuple[str, Path]]) -> set[str]:
    """``<stem>#<Node Name>`` for every module pathophysiology node."""
    anchors: set[str] = set()
    for sub, path in files:
        if sub != "modules":
            continue
        doc = safe_load(path.read_text()) or {}
        for node in doc.get("pathophysiology") or []:
            if isinstance(node, dict) and node.get("name"):
                anchors.add(f"{path.stem}#{node['name']}")
    return anchors


def canonical_key(
    *,
    sub: str,
    stem: str,
    name: str,
    node_type: str,
    item: dict[str, Any],
    anchors: set[str],
) -> tuple[tuple, str]:
    """Return ``(identity key, which rung of the ladder fired)``."""
    terms = collect_terms(item) if item else {}
    core = tuple(sorted({t for p in CORE_PREFIXES for t in terms.get(p, ())}))
    context = tuple(sorted({t for p in CONTEXT_PREFIXES for t in terms.get(p, ())}))

    if sub == "modules" and node_type == "pathophysiology":
        return ("MODULE", f"{stem}#{name}"), "module_node"
    conforms = item.get("conforms_to") if item else None
    if node_type == "pathophysiology" and conforms in anchors:
        return ("MODULE", str(conforms)), "conforms_to"
    if node_type == "phenotype" and terms.get("HP"):
        return ("HP", tuple(sorted(terms["HP"]))), "hp_term"
    if core:
        return (node_type.upper(), core, context), "core_terms"
    return (node_type.upper(), normalize_name(name)), "name_only"


def build(kb_dir: Path) -> dict[str, Any]:
    """Project every entry's pathograph into one merged graph."""
    files = entry_files(kb_dir)
    anchors = module_anchors(files)

    node_key: dict[tuple[str, str], tuple] = {}
    members: dict[tuple, list[tuple[str, str]]] = defaultdict(list)
    entries_per_key: dict[tuple, set[str]] = defaultdict(set)
    types_per_key: dict[tuple, Counter] = defaultdict(Counter)
    rung = Counter()
    edges: dict[tuple, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    raw_nodes = raw_edges = orphans = entries = 0

    for sub, path in files:
        try:
            doc = safe_load(path.read_text())
        except Exception:  # a malformed entry is check-duplicate-keys' problem
            continue
        if not isinstance(doc, dict):
            continue
        entries += 1
        entry = ("MOD:" if sub == "modules" else "") + path.stem

        lookup: dict[str, dict[str, Any]] = {}
        for section in SECTIONS:
            for item in doc.get(section) or []:
                if isinstance(item, dict) and item.get("name"):
                    lookup.setdefault(item["name"], item)
        for _parent, variant in iter_variant_items(doc):
            if isinstance(variant, dict) and variant.get("name"):
                lookup.setdefault(variant["name"], variant)

        graph = build_causal_graph(doc)
        orphans += len(graph.orphan_targets)
        for name, info in graph.nodes.items():
            raw_nodes += 1
            key, why = canonical_key(
                sub=sub,
                stem=path.stem,
                name=name,
                node_type=info.node_type,
                item=lookup.get(name, {}),
                anchors=anchors,
            )
            rung[why] += 1
            node_key[(entry, name)] = key
            members[key].append((entry, name))
            entries_per_key[key].add(entry)
            types_per_key[key][info.node_type] += 1
        for edge in graph.edges:
            raw_edges += 1
            source = node_key.get((entry, edge.source))
            target = node_key.get((entry, edge.target))
            if source is None or target is None:
                continue
            edges[(source, target)][edge.predicate].add(entry)

    return {
        "entries": entries,
        "raw_nodes": raw_nodes,
        "raw_edges": raw_edges,
        "orphan_targets": orphans,
        "node_key": node_key,
        "members": members,
        "entries_per_key": entries_per_key,
        "types_per_key": types_per_key,
        "rung": rung,
        "edges": edges,
    }


def support(edges: dict[tuple, dict[str, set[str]]]) -> dict[tuple, int]:
    """Number of distinct entries asserting each merged edge."""
    return {k: len(set().union(*v.values())) for k, v in edges.items()}


def components(edges: dict[tuple, Any]) -> list[int]:
    adjacency: dict[tuple, set[tuple]] = defaultdict(set)
    for source, target in edges:
        adjacency[source].add(target)
        adjacency[target].add(source)
    seen: set[tuple] = set()
    sizes: list[int] = []
    for start in adjacency:
        if start in seen:
            continue
        stack, size = [start], 0
        seen.add(start)
        while stack:
            current = stack.pop()
            size += 1
            for neighbour in adjacency[current]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append(neighbour)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def summarize(graph: dict[str, Any], min_support: int) -> dict[str, Any]:
    edges = graph["edges"]
    counts = support(edges)
    kept = {k: c for k, c in counts.items() if c >= min_support}
    backbone: set[tuple] = set()
    for source, target in kept:
        backbone.update((source, target))
    members = graph["members"]
    hubs = sorted(((len(v), str(k)) for k, v in members.items()), reverse=True)[:10]
    top = sorted(
        ((c, (str(a)[:60], str(b)[:60])) for (a, b), c in counts.items()), reverse=True
    )[:10]
    module_only = sum(
        1 for (a, b), c in counts.items() if c > 1 and "MODULE" in (a[0], b[0])
    )
    return {
        "entries": graph["entries"],
        "raw_nodes": graph["raw_nodes"],
        "merged_nodes": len(members),
        "compression": round(1 - len(members) / max(graph["raw_nodes"], 1), 3),
        "identity_rung": dict(graph["rung"]),
        "keys_spanning_2plus_entries": sum(
            1 for v in graph["entries_per_key"].values() if len(v) > 1
        ),
        "keys_mixing_node_types": sum(
            1 for c in graph["types_per_key"].values() if len(c) > 1
        ),
        "raw_edges": graph["raw_edges"],
        "orphan_targets": graph["orphan_targets"],
        "merged_edges": len(edges),
        "edges_2plus_entries": sum(1 for c in counts.values() if c >= 2),
        "edges_5plus_entries": sum(1 for c in counts.values() if c >= 5),
        "multi_support_edges_touching_a_module": module_only,
        "self_loops": sum(1 for a, b in edges if a == b),
        "backbone_nodes": len(backbone),
        "backbone_edges": len(kept),
        "component_sizes": components(edges)[:6],
        "largest_merged_nodes": hubs,
        "best_supported_edges": top,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--kb-dir", default="kb", type=Path)
    parser.add_argument(
        "--min-support",
        type=int,
        default=2,
        help="Entries an edge needs before it counts toward the backbone.",
    )
    parser.add_argument("--format", choices=("summary", "tsv"), default="summary")
    args = parser.parse_args()

    graph = build(args.kb_dir)
    if args.format == "tsv":
        counts = support(graph["edges"])
        print("support\tpredicates\tsource\ttarget")
        for (source, target), count in sorted(counts.items(), key=lambda kv: -kv[1]):
            if count < args.min_support:
                continue
            predicates = ",".join(sorted(graph["edges"][(source, target)]))
            print(f"{count}\t{predicates}\t{source}\t{target}")
        return 0

    print(json.dumps(summarize(graph, args.min_support), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
