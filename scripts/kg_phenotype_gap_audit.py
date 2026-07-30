#!/usr/bin/env python3
"""dismech#7175 content evaluation: Monarch KG <-> dismech disease-phenotype comparison.

For every disorder with a MONDO primary anchor AND curated phenotypes
(phenotypes[].phenotype_term), compare dismech's HP set against the Monarch KG's
DiseaseToPhenotypicFeatureAssociation edges for that MONDO term (v3 API).

Emits, per disease:
  - overlap        : HP terms in both (EXACT id match)
  - kg_only        : HP the KG annotates but dismech does not  (dismech COVERAGE GAP)
  - dismech_only   : HP dismech curates but the KG does not     (dismech -> KG candidate / to verify)

IMPORTANT caveat: matching is EXACT HP id only. HPO is a deep hierarchy, so a
dismech term that is a parent/child of the KG term reads as a mismatch here. Exact
overlap is therefore a LOWER BOUND on true semantic agreement; treat kg_only /
dismech_only as candidate lists, not confirmed gaps. Subsumption-aware matching is a
documented follow-up.

Usage:
    uv run python scripts/kg_phenotype_gap_audit.py --limit 5                     # pilot
    uv run python scripts/kg_phenotype_gap_audit.py --tsv research/kg_phenotype_gap.tsv
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import time
import urllib.parse
import urllib.request
from collections import Counter

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISORDERS = os.path.join(ROOT, "kb", "disorders")
API = "https://api-v3.monarchinitiative.org/v3/api/association"
CAT = "biolink:DiseaseToPhenotypicFeatureAssociation"


def dismech_phenos(doc):
    out = {}
    for p in (doc or {}).get("phenotypes") or []:
        pt = p.get("phenotype_term") or {}
        term = pt.get("term") or {}
        tid = term.get("id")
        if tid and tid.startswith("HP:"):
            out[tid] = term.get("label") or pt.get("preferred_term") or ""
    return out


def kg_phenos(mondo_id, cache):
    if mondo_id in cache:
        return cache[mondo_id]
    phenos = {}
    offset = 0
    while True:
        params = urllib.parse.urlencode(
            {"category": CAT, "subject": mondo_id, "limit": 500, "offset": offset})
        url = f"{API}?{params}"
        data = {"items": [], "total": 0}
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url, timeout=45) as resp:
                    data = json.load(resp)
                break
            except Exception:
                if attempt == 2:
                    data = {"items": [], "total": 0}
                time.sleep(2 * (attempt + 1))
        for it in data.get("items", []):
            obj = it.get("object", "")
            if obj.startswith("HP:"):
                phenos[obj] = it.get("object_label") or ""
        offset += 500
        if offset >= (data.get("total") or 0):
            break
        time.sleep(0.1)
    cache[mondo_id] = phenos
    time.sleep(0.1)
    return phenos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--tsv")
    ap.add_argument("--cache", default=os.path.join(ROOT, "research", ".kg_pheno_cache.json"))
    args = ap.parse_args()

    cache = {}
    if os.path.exists(args.cache):
        try:
            cache = json.load(open(args.cache))
        except Exception:
            cache = {}

    targets = []
    for path in sorted(glob.glob(os.path.join(DISORDERS, "*.yaml"))):
        doc = yaml.safe_load(open(path))
        term = ((doc or {}).get("disease_term") or {}).get("term") or {}
        mid = term.get("id")
        if not mid or not mid.startswith("MONDO:"):
            continue
        ph = dismech_phenos(doc)
        if not ph:
            continue
        targets.append((os.path.basename(path)[:-5], mid, ph))
    if args.limit:
        targets = targets[: args.limit]

    rows, tot = [], Counter()
    n_kg_has = 0
    for i, (name, mid, dph) in enumerate(targets, 1):
        kg = kg_phenos(mid, cache)
        dset, kset = set(dph), set(kg)
        overlap, kg_only, dismech_only = dset & kset, kset - dset, dset - kset
        if kg:
            n_kg_has += 1
        tot["dismech"] += len(dset); tot["kg"] += len(kset)
        tot["overlap"] += len(overlap); tot["kg_only"] += len(kg_only)
        tot["dismech_only"] += len(dismech_only)
        rows.append((name, mid, len(dset), len(kset), len(overlap),
                     ";".join(f"{h}({kg[h]})" for h in sorted(kg_only)),
                     ";".join(f"{h}({dph[h]})" for h in sorted(dismech_only))))
        if i % 25 == 0:
            json.dump(cache, open(args.cache, "w")); print(f"  ...{i}/{len(targets)}", flush=True)
    json.dump(cache, open(args.cache, "w"))

    def cnt(s):
        return 0 if not s else len(s.split(";"))
    R = [dict(disorder=r[0], mondo=r[1], nd=r[2], nk=r[3], nov=r[4],
             kg_only=r[5], dismech_only=r[6], nko=cnt(r[5]), ndo=cnt(r[6])) for r in rows]
    BROAD = 60
    no_kg = [r for r in R if r["nk"] == 0]
    broad = [r for r in R if r["nk"] > BROAD]
    clean = [r for r in R if 0 < r["nk"] <= BROAD]

    print(f"\n# Monarch KG <-> dismech disease-phenotype comparison (EXACT HP id match)")
    print(f"diseases compared (MONDO + phenotypes): {len(targets)}")
    print(f"  with >=1 KG phenotype edge: {n_kg_has}")
    print(f"  dismech HP assertions: {tot['dismech']}")
    print(f"  KG HP assertions:      {tot['kg']}")
    print(f"  overlap (exact):       {tot['overlap']}")
    print(f"  kg_only (coverage gap, RAW):   {tot['kg_only']}")
    print(f"  dismech_only (KG candidate):   {tot['dismech_only']}")
    print(f"\n## Tiers by KG phenotype count")
    print(f"  no KG phenotype edge:     {len(no_kg)}")
    print(f"  broad (n_kg>{BROAD}):          {len(broad)}  (contribute {sum(r['nko'] for r in broad)} of raw kg_only)")
    print(f"  clean (1..{BROAD}):           {len(clean)}  (clean kg_only = {sum(r['nko'] for r in clean)})")

    print(f"\n## Top clean coverage gaps (dismech missing HP the KG has; top 20)")
    for r in sorted(clean, key=lambda x: -x["nko"])[:20]:
        if r["nko"]:
            print(f"  {r['disorder']} ({r['mondo']}) nd={r['nd']} nk={r['nk']} ov={r['nov']}: {r['kg_only'][:300]}")

    print(f"\n## Highest exact-agreement diseases (sanity check; top 10 by overlap)")
    for r in sorted(R, key=lambda x: -x["nov"])[:10]:
        print(f"  {r['disorder']}: overlap={r['nov']} nd={r['nd']} nk={r['nk']}")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("disorder\tmondo_id\tn_dismech\tn_kg\tn_overlap\tkg_only\tdismech_only\n")
            for r in rows:
                fh.write("\t".join(str(x) for x in r) + "\n")
        print(f"\n[wrote {args.tsv} ({len(rows)} rows)]")


if __name__ == "__main__":
    main()
