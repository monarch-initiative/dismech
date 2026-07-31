#!/usr/bin/env python3
"""dismech#7175: Mondo -> dismech curation-target flow (bounded to the neighborhood).

Comprehensive Mondo coverage would be ~20k+ terms, most out of dismech scope by design.
Instead this bounds to the NEIGHBORHOOD of what dismech already curates: for each MONDO
term used as a disorder ``disease_term`` anchor, find its direct is_a children in Mondo
that dismech does NOT curate. Reads as "dismech has the parent X but not its Mondo
subtypes X1, X2 ..." -- high-signal curation targets with low noise.

Covered set = all disorder disease_term MONDO anchors (a child already curated by another
dismech entry is not flagged). Obsolete children are dropped.

Usage:
    uv run python scripts/mondo_to_dismech_gaps.py --tsv research/mondo_to_dismech_gaps.tsv
"""
from __future__ import annotations

import argparse
import glob
import os
from collections import defaultdict

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv")
    args = ap.parse_args()

    a = get_adapter("sqlite:obo:mondo")
    obs = set(a.obsoletes())

    # covered: MONDO id -> dismech disorder name(s)
    covered = {}
    for path in sorted(glob.glob(os.path.join("kb", "disorders", "*.yaml"))):
        doc = yaml.safe_load(open(path))
        term = ((doc or {}).get("disease_term") or {}).get("term") or {}
        mid = term.get("id")
        if mid and mid.startswith("MONDO:"):
            covered.setdefault(mid, []).append(os.path.basename(path)[:-5])
    covered_ids = set(covered)

    # all is_a children of covered terms, in one query
    rels = list(a.relationships(objects=list(covered_ids), predicates=[IS_A]))
    gap_pairs = [(child, parent) for child, _p, parent in rels
                 if child.startswith("MONDO:") and child not in covered_ids and child not in obs]

    # bulk-resolve every label we need in one pass (one-at-a-time label() is pathologically slow)
    need = set(covered_ids) | {c for c, _ in gap_pairs}
    lab = {cid: name for cid, name in a.labels(list(need))}

    gaps = defaultdict(list)  # parent MONDO -> [(child_id, child_label)]
    for child, parent in gap_pairs:
        gaps[parent].append((child, lab.get(child) or ""))

    rows = []
    for parent, kids in gaps.items():
        for cid, clabel in kids:
            for dis in covered[parent]:
                rows.append((dis, parent, lab.get(parent) or "", cid, clabel))

    n_parents = len(gaps)
    n_children = sum(len(v) for v in gaps.values())
    print(f"# Mondo -> dismech neighborhood gaps (uncovered direct is_a children)\n")
    print(f"covered disorder anchors: {len(covered_ids)}")
    print(f"anchors with >=1 uncovered Mondo child: {n_parents}")
    print(f"total uncovered child subtypes: {n_children}")

    print(f"\n## Anchors with the most uncovered Mondo children (top 25)")
    for parent, kids in sorted(gaps.items(), key=lambda x: -len(x[1]))[:25]:
        dis = ", ".join(covered[parent])
        print(f"  {dis} ({parent} {lab.get(parent) or ''}): {len(kids)} uncovered")
        for cid, clabel in sorted(kids)[:8]:
            print(f"       - {cid} {clabel}")
        if len(kids) > 8:
            print(f"       ... +{len(kids) - 8} more")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("dismech_disorder\tparent_mondo\tparent_label\tuncovered_child_mondo\tchild_label\n")
            for r in sorted(rows):
                fh.write("\t".join(r) + "\n")
        print(f"\n[wrote {args.tsv} ({len(rows)} rows)]")


if __name__ == "__main__":
    main()
