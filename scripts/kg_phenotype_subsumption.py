#!/usr/bin/env python3
"""dismech#7175: subsumption-aware refinement of the disease-phenotype comparison.

The exact-id disease-phenotype audit (kg_phenotype_gap_audit.py) undercounts agreement
because HPO is a deep hierarchy: a dismech term that is a parent/child of a KG-annotated
term reads as a mismatch. This script re-scores agreement using the HP is_a hierarchy
(OAK sqlite:obo:hp), OFFLINE from the phenotype cache the exact audit already populated
(research/.kg_pheno_cache.json) -- no API calls.

A dismech HP term d is classified against the KG set K for its disease:
  EXACT         d in K
  MORE_SPECIFIC some k in K is an ancestor of d   (dismech finer than KG)
  MORE_GENERAL  d is an ancestor of some k in K    (dismech coarser than KG)
  UNMATCHED     none of the above -> truly novel dismech phenotype (refined dismech_only)

"Semantic overlap" = EXACT + MORE_SPECIFIC + MORE_GENERAL.

Usage:
    uv run python scripts/kg_phenotype_subsumption.py --tsv research/kg_phenotype_subsumption.tsv
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from collections import Counter

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISORDERS = os.path.join(ROOT, "kb", "disorders")
CACHE = os.path.join(ROOT, "research", ".kg_pheno_cache.json")


def dismech_phenos(doc):
    out = {}
    for p in (doc or {}).get("phenotypes") or []:
        term = ((p.get("phenotype_term") or {}).get("term")) or {}
        tid = term.get("id")
        if tid and tid.startswith("HP:"):
            out[tid] = term.get("label") or ""
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv")
    args = ap.parse_args()

    if not os.path.exists(CACHE):
        raise SystemExit("phenotype cache missing; run kg_phenotype_gap_audit.py first")
    kg_cache = json.load(open(CACHE))  # {MONDO: {HP: label}}
    adapter = get_adapter("sqlite:obo:hp")

    # Build the disease list with dismech + KG phenotype sets.
    diseases = []
    all_terms = set()
    for path in sorted(glob.glob(os.path.join(DISORDERS, "*.yaml"))):
        doc = yaml.safe_load(open(path))
        term = ((doc or {}).get("disease_term") or {}).get("term") or {}
        mid = term.get("id")
        if not mid or not mid.startswith("MONDO:"):
            continue
        d = dismech_phenos(doc)
        if not d:
            continue
        k = set(kg_cache.get(mid, {}))
        diseases.append((os.path.basename(path)[:-5], mid, d, k))
        all_terms |= set(d) | k

    # Memoize reflexive is_a ancestors for every HP term we touch.
    anc = {}
    for t in all_terms:
        try:
            anc[t] = set(adapter.ancestors(t, predicates=[IS_A]))
        except Exception:
            anc[t] = {t}

    rows, tot = [], Counter()
    ex_overlap_tot = 0
    for name, mid, d, k in diseases:
        A_K = set()
        for kk in k:
            A_K |= anc.get(kk, {kk})
        cls = Counter()
        unmatched = []
        for term, label in d.items():
            if term in k:
                cls["exact"] += 1
            elif anc.get(term, {term}) & k:
                cls["more_specific"] += 1
            elif term in A_K:
                cls["more_general"] += 1
            else:
                cls["unmatched"] += 1
                unmatched.append(f"{term}({label})")
        sem = cls["exact"] + cls["more_specific"] + cls["more_general"]
        tot["dismech"] += len(d)
        tot["exact"] += cls["exact"]
        tot["more_specific"] += cls["more_specific"]
        tot["more_general"] += cls["more_general"]
        tot["unmatched"] += cls["unmatched"]
        ex_overlap_tot += cls["exact"]
        rows.append((name, mid, len(d), len(k), cls["exact"], cls["more_specific"],
                     cls["more_general"], cls["unmatched"], sem, ";".join(sorted(unmatched))))

    nd = tot["dismech"]
    print("# Subsumption-aware disease-phenotype agreement (HP is_a)")
    print(f"diseases: {len(diseases)}   dismech HP assertions: {nd}\n")
    print(f"  EXACT match:        {tot['exact']:6d}  ({100*tot['exact']/nd:.1f}%)")
    print(f"  + MORE_SPECIFIC:    {tot['more_specific']:6d}  (dismech finer than KG)")
    print(f"  + MORE_GENERAL:     {tot['more_general']:6d}  (dismech coarser than KG)")
    sem = tot['exact'] + tot['more_specific'] + tot['more_general']
    print(f"  = SEMANTIC overlap: {sem:6d}  ({100*sem/nd:.1f}%)")
    print(f"  UNMATCHED (truly novel dismech HP): {tot['unmatched']:6d}  ({100*tot['unmatched']/nd:.1f}%)")
    print(f"\n  exact-only rate {100*tot['exact']/nd:.1f}%  ->  subsumption-aware {100*sem/nd:.1f}%  "
          f"(+{100*(sem-tot['exact'])/nd:.1f} pts recovered as granularity differences)")

    print(f"\n## Diseases with the most truly-novel (UNMATCHED) dismech phenotypes")
    for r in sorted(rows, key=lambda x: -x[7])[:20]:
        if r[7]:
            print(f"  {r[0]} ({r[1]}): unmatched={r[7]} of nd={r[2]} (kg={r[3]})")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("disorder\tmondo_id\tn_dismech\tn_kg\texact\tmore_specific\t"
                     "more_general\tunmatched\tsemantic_overlap\tunmatched_terms\n")
            for r in rows:
                fh.write("\t".join(str(x) for x in r) + "\n")
        print(f"\n[wrote {args.tsv} ({len(rows)} rows)]")


if __name__ == "__main__":
    main()
