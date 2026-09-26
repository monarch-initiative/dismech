#!/usr/bin/env python3
"""Census of AOP-derivable causal chains in the dismech knowledge base.

An Adverse Outcome Pathway needs two things a dismech pathograph may or may not
have: Key Events that are *measured*, and Key Event Relationships that are
*cited*. This script counts, per entry, the longest run of consecutive
pathophysiology nodes satisfying each requirement, and both together.

Backs docs/reports/aop-derivable-measurable-chains-2026-09-10.md. Run it rather
than trusting the numbers in that report, which go stale with every curation PR.

    just aop-chain-census                 # the report's tables
    just aop-chain-census --format tsv    # one row per entry
    just aop-chain-census --list-joint 3  # entries clearing the joint screen
"""

from __future__ import annotations

import argparse
import collections
import csv
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from dismech import kb_cache
from dismech.yaml_io import safe_load_path

ROOTS = ("kb/disorders", "kb/modules")
MODEL_SECTIONS = ("experimental_models", "animal_models", "computational_models")


def longest_path(nodes: set[str], edges: list[tuple[str, str]]) -> list[str]:
    """Longest simple path in the subgraph of `edges` induced by `nodes`."""
    adj: dict[str, list[str]] = collections.defaultdict(list)
    for src, dst in edges:
        if src in nodes and dst in nodes and src != dst:
            adj[src].append(dst)
    best: list[str] = []

    def walk(node: str, seen: list[str]) -> None:
        nonlocal best
        path = seen + [node]
        if len(path) > len(best):
            best = path
        for nxt in adj[node]:
            if nxt not in seen:
                walk(nxt, path)

    for node in nodes:
        walk(node, [])
    return best


def scan(root_dir: pathlib.Path) -> list[dict]:
    """One record per entry that has at least one causal edge."""
    rows = []
    for root in ROOTS:
        for path in sorted((root_dir / root).glob("*.yaml")):
            doc = safe_load_path(path)
            if not isinstance(doc, dict):
                continue

            # Node universe: pathophysiology nodes only. A `downstream` target
            # naming a phenotype terminates a chain and is not counted toward
            # its length -- phenotypes carry no `downstream` edges of their own,
            # so including them would lengthen chains under one screen and not
            # the other.
            patho = {
                n.get("name")
                for n in (doc.get("pathophysiology") or [])
                if isinstance(n, dict) and n.get("name")
            }

            all_edges: list[tuple[str, str]] = []
            cited_edges: list[tuple[str, str]] = []
            every_edge = every_edge_cited = 0
            for node in doc.get("pathophysiology") or []:
                if not isinstance(node, dict):
                    continue
                for edge in node.get("downstream") or []:
                    if not isinstance(edge, dict) or not edge.get("target"):
                        continue
                    pair = (node.get("name"), edge["target"])
                    every_edge += 1
                    if edge.get("evidence"):
                        every_edge_cited += 1
                    if pair[1] not in patho:
                        continue
                    all_edges.append(pair)
                    if edge.get("evidence"):
                        cited_edges.append(pair)
            if not all_edges:
                continue

            linked: set[str] = set()
            measured: set[str] = set()
            multi: collections.Counter = collections.Counter()
            blocks = collections.Counter()
            blocks_linked = collections.Counter()
            for section in MODEL_SECTIONS:
                for model in doc.get(section) or []:
                    if not isinstance(model, dict):
                        continue
                    blocks[section] += 1
                    links = [
                        link
                        for link in (model.get("modeled_mechanisms") or [])
                        if isinstance(link, dict) and link.get("target")
                    ]
                    if links:
                        blocks_linked[section] += 1
                    for link in links:
                        target = link["target"]
                        linked.add(target)
                        multi[target] += 1
                        if link.get("readouts"):
                            measured.add(target)

            rows.append(
                {
                    "file": str(path.relative_to(root_dir)),
                    "edges": every_edge,
                    "edges_cited": every_edge_cited,
                    "patho_edges": len(all_edges),
                    "patho_edges_cited": len(cited_edges),
                    "blocks": blocks,
                    "blocks_linked": blocks_linked,
                    "has_linked_model": bool(linked),
                    "n_multi_experimental": sum(
                        1
                        for m in (doc.get("experimental_models") or [])
                        if isinstance(m, dict)
                    ),
                    "n_linked_models": sum(blocks_linked.values()),
                    "chain_measured": longest_path(measured, all_edges),
                    "chain_cited": longest_path(patho, cited_edges),
                    "chain_multi": longest_path(
                        {t for t, c in multi.items() if c >= 2}, all_edges
                    ),
                    "chain_joint": longest_path(measured, cited_edges),
                }
            )
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--root", default=".", type=pathlib.Path)
    ap.add_argument("--format", choices=("markdown", "tsv"), default="markdown")
    ap.add_argument(
        "--list-joint",
        type=int,
        metavar="N",
        help="list entries whose joint-screen chain is at least N nodes",
    )
    args = ap.parse_args()

    kb_cache.default_off()
    rows = scan(args.root)

    if args.format == "tsv":
        w = csv.writer(sys.stdout, delimiter="\t")
        w.writerow(
            [
                "file",
                "edges",
                "edges_cited",
                "chain_measured",
                "chain_cited",
                "chain_multi",
                "chain_joint",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    r["file"],
                    r["edges"],
                    r["edges_cited"],
                    len(r["chain_measured"]),
                    len(r["chain_cited"]),
                    len(r["chain_multi"]),
                    len(r["chain_joint"]),
                ]
            )
        return 0

    if args.list_joint:
        hits = sorted(
            (r for r in rows if len(r["chain_joint"]) >= args.list_joint),
            key=lambda r: -len(r["chain_joint"]),
        )
        print(
            f"{len(hits)} entries with a joint-screen chain of >= {args.list_joint} nodes\n"
        )
        for r in hits:
            print(
                f"{len(r['chain_joint'])}  {r['file']}  ({r['edges_cited']}/{r['edges']} edges cited)"
            )
            print("     " + " -> ".join(r["chain_joint"]))
        return 0

    blocks = collections.Counter()
    blocks_linked = collections.Counter()
    for r in rows:
        blocks.update(r["blocks"])
        blocks_linked.update(r["blocks_linked"])

    print(f"Entries with at least one causal edge: {len(rows)}")
    total = sum(r["edges"] for r in rows)
    cited = sum(r["edges_cited"] for r in rows)
    ptot = sum(r["patho_edges"] for r in rows)
    pcit = sum(r["patho_edges_cited"] for r in rows)
    print(
        f"Causal edges: {total:,}, carrying evidence: {cited:,} ({100 * cited / total:.0f}%)"
    )
    print(
        f"  of those, node-to-node (target is a pathophysiology node): {ptot:,}, "
        f"cited {pcit:,} ({100 * pcit / ptot:.0f}%)\n"
    )

    print(
        "| Model section | Model blocks | Blocks with `modeled_mechanisms` | Entries with one | Entries with a linked one |"
    )
    print("|---|---|---|---|---|")
    for section in MODEL_SECTIONS:
        with_any = sum(1 for r in rows if r["blocks"][section])
        with_linked = sum(1 for r in rows if r["blocks_linked"][section])
        print(
            f"| `{section}` | {blocks[section]:,} | {blocks_linked[section]:,} "
            f"| {with_any:,} | {with_linked:,} |"
        )

    print()
    print(
        f"- {sum(1 for r in rows if r['n_multi_experimental'] >= 2):,} entries carry >=2 `experimental_models` blocks."
    )
    print(
        f"- {sum(1 for r in rows if r['n_linked_models'] >= 2):,} entries carry >=2 pathograph-linked models of any kind."
    )
    print(
        f"- {sum(1 for r in rows if r['has_linked_model']):,} entries carry at least one pathograph-linked model."
    )

    print("\n| Longest chain | Every node measured | Every edge cited | Both |")
    print("|---|---|---|---|")
    for n in (2, 3, 4, 5):
        a = sum(1 for r in rows if len(r["chain_measured"]) >= n)
        b = sum(1 for r in rows if len(r["chain_cited"]) >= n)
        c = sum(1 for r in rows if len(r["chain_joint"]) >= n)
        print(f"| >= {n} nodes | {a:,} | {b:,} | {c:,} |")

    print("\n| Longest chain | >=2 models on every node |")
    print("|---|---|")
    for n in (3, 4, 5):
        print(
            f"| >= {n} nodes | {sum(1 for r in rows if len(r['chain_multi']) >= n):,} |"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
