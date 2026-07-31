#!/usr/bin/env python3
"""dismech#7175: Mondo -> dismech curation-target flow (bounded to the neighborhood).

Comprehensive Mondo coverage would be ~20k+ terms, most out of dismech scope by design.
Instead this bounds to the NEIGHBORHOOD of what dismech already curates: for each MONDO
term used as a disorder ``disease_term`` anchor OR a ``has_subtypes[].subtype_term``
anchor, find its direct is_a children in Mondo that dismech does NOT curate. Reads as
"dismech has the parent X but not its Mondo subtypes X1, X2 ..." -- high-signal curation
targets with low noise.

Covered set = every MONDO id dismech anchors, at the disease level (``disease_term``) OR
the subtype level (``has_subtypes[].subtype_term``); a child already curated as either is
not flagged. Obsolete children are dropped.

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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISORDERS = os.path.join(ROOT, "kb", "disorders")
BROAD = 15  # anchors with more uncovered children than this are broad/mis-anchor noise


def anchor_mondo_ids(doc):
    """Yield every MONDO id this disorder anchors: disease_term + has_subtypes subtype_term."""
    term = ((doc or {}).get("disease_term") or {}).get("term") or {}
    tid = term.get("id")
    if tid and tid.startswith("MONDO:"):
        yield tid
    for st in (doc or {}).get("has_subtypes") or []:
        stt = (st.get("subtype_term") or {}).get("term") or {}
        sid = stt.get("id")
        if sid and sid.startswith("MONDO:"):
            yield sid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv")
    args = ap.parse_args()

    a = get_adapter("sqlite:obo:mondo")
    obs = set(a.obsoletes())

    # covered: MONDO id -> dismech disorder name(s) that anchor it (disease- or subtype-level)
    covered = {}
    for path in sorted(glob.glob(os.path.join(DISORDERS, "*.yaml"))):
        doc = yaml.safe_load(open(path))
        name = os.path.basename(path)[:-5]
        # A disorder's disease_term anchor is what we look for children of; subtype anchors
        # only expand the "covered" set (so a subtype already in the KB isn't re-flagged).
        term = ((doc or {}).get("disease_term") or {}).get("term") or {}
        disease_anchor = term.get("id") if str(term.get("id")).startswith("MONDO:") else None
        for mid in anchor_mondo_ids(doc):
            covered.setdefault(mid, [])
            if mid == disease_anchor:
                covered[mid].append(name)
    covered_ids = set(covered)
    # parents to expand = disease-level anchors (those with a disorder name attached)
    parents = {mid for mid, names in covered.items() if names}

    # all is_a children of the disease-level anchors, in one query
    rels = list(a.relationships(objects=list(parents), predicates=[IS_A]))
    gap_pairs = [(child, parent) for child, _p, parent in rels
                 if child.startswith("MONDO:") and child not in covered_ids and child not in obs]

    # bulk-resolve every label we need in one pass (one-at-a-time label() is pathologically slow)
    need = set(parents) | {c for c, _ in gap_pairs}
    lab = dict(a.labels(list(need)))

    gaps = defaultdict(list)  # parent MONDO -> [(child_id, child_label)]
    for child, parent in gap_pairs:
        gaps[parent].append((child, lab.get(child) or ""))

    rows = []
    for parent, kids in gaps.items():
        for cid, clabel in kids:
            for dis in covered[parent]:
                rows.append((dis, parent, lab.get(parent) or "", cid, clabel))

    # Tier by uncovered-children count: broad/mis-anchor noise vs high-signal targets.
    per_anchor = {(covered[parent][0], parent): len(kids)
                  for parent, kids in gaps.items() if covered[parent]}
    broad = {k: v for k, v in per_anchor.items() if v > BROAD}
    clean = {k: v for k, v in per_anchor.items() if 1 <= v <= BROAD}
    broad_children = sum(broad.values())
    clean_children = sum(clean.values())

    n_parents = len([p for p in gaps if covered[p]])
    n_children = sum(len(v) for p, v in gaps.items() if covered[p])
    print("# Mondo -> dismech neighborhood gaps (uncovered direct is_a children)\n")
    print(f"covered anchors (disease + subtype level): {len(covered_ids)}")
    print(f"disease-level anchors expanded: {len(parents)}")
    print(f"anchors with >=1 uncovered Mondo child: {n_parents}")
    print(f"total uncovered child subtypes: {n_children}")
    broad_pct = (100 * broad_children / n_children) if n_children else 0
    print(f"\n## Tiers by uncovered-child count (BROAD={BROAD})")
    print(f"  broad (> {BROAD} children): {len(broad)} anchors -> {broad_children} children "
          f"({broad_pct:.0f}% -- broad/mis-anchor noise)")
    print(f"  clean (1..{BROAD}):        {len(clean)} anchors -> {clean_children} children "
          f"(high-signal targets)")

    print("\n## Anchors with the most uncovered Mondo children (top 25)")
    for parent, kids in sorted(gaps.items(), key=lambda x: -len(x[1]))[:25]:
        if not covered[parent]:
            continue
        dis = ", ".join(covered[parent])
        print(f"  {dis} ({parent} {lab.get(parent) or ''}): {len(kids)} uncovered")
        for cid, clabel in sorted(kids)[:8]:
            print(f"       - {cid} {clabel}")
        if len(kids) > 8:
            print(f"       ... +{len(kids) - 8} more")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("dismech_disorder\tparent_mondo\tparent_label\tuncovered_child_mondo\tchild_label\n")
            fh.writelines("\t".join(r) + "\n" for r in sorted(rows))
        print(f"\n[wrote {args.tsv} ({len(rows)} rows)]")


if __name__ == "__main__":
    main()
