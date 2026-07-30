#!/usr/bin/env python3
"""dismech#7175 content evaluation: Monarch KG <-> dismech gene-disease comparison.

For every disorder with a MONDO primary anchor AND curated genes (genetic[].gene_term),
compare dismech's gene set against the Monarch KG's gene-disease edges for that MONDO
term (Causal + Correlated gene-to-disease associations, via the Monarch v3 API).

Emits, per disease:
  - overlap        : genes in both
  - kg_only        : genes the KG links to the disease but dismech does not  (dismech COVERAGE GAP)
  - dismech_only   : genes dismech curates but the KG does not link          (dismech -> KG candidate / to verify)

Usage:
    uv run python scripts/kg_gene_gap_audit.py --limit 5                 # pilot
    uv run python scripts/kg_gene_gap_audit.py --tsv research/kg_gene_gap.tsv   # full run

Network: Monarch v3 API (api-v3.monarchinitiative.org). Resumable via --cache.
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
GENE_CATS = ["biolink:CausalGeneToDiseaseAssociation",
             "biolink:CorrelatedGeneToDiseaseAssociation"]


def norm(hgnc):
    """Normalize dismech 'hgnc:11025' and KG 'HGNC:11025' to a common key."""
    return hgnc.replace("hgnc:", "HGNC:") if hgnc else hgnc


def dismech_genes(doc):
    out = {}
    for g in (doc or {}).get("genetic") or []:
        gt = g.get("gene_term") or {}
        term = gt.get("term") or {}
        tid = term.get("id")
        if tid and tid.lower().startswith("hgnc:"):
            out[norm(tid)] = term.get("label") or gt.get("preferred_term") or ""
    return out


def kg_genes(mondo_id, cache):
    if mondo_id in cache:
        return cache[mondo_id]
    genes = {}
    for cat in GENE_CATS:
        params = urllib.parse.urlencode({"category": cat, "object": mondo_id, "limit": 500})
        url = f"{API}?{params}"
        for attempt in range(3):
            try:
                with urllib.request.urlopen(url, timeout=45) as resp:
                    data = json.load(resp)
                break
            except Exception:
                if attempt == 2:
                    data = {"items": []}
                time.sleep(2 * (attempt + 1))
        for it in data.get("items", []):
            subj = it.get("subject", "")
            if subj.startswith("HGNC:"):
                genes[subj] = it.get("subject_label") or ""
        time.sleep(0.1)
    cache[mondo_id] = genes
    return genes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="only process the first N (pilot)")
    ap.add_argument("--tsv", help="write per-disease TSV")
    ap.add_argument("--cache", default=os.path.join(ROOT, "research", ".kg_gene_cache.json"))
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
        dt = (doc or {}).get("disease_term") or {}
        term = dt.get("term") or {}
        mid = term.get("id")
        if not mid or not mid.startswith("MONDO:"):
            continue
        genes = dismech_genes(doc)
        if not genes:
            continue
        targets.append((os.path.basename(path)[:-5], mid, genes))
    if args.limit:
        targets = targets[: args.limit]

    rows, tot = [], Counter()
    n_kg_has_data = 0
    for i, (name, mid, dgenes) in enumerate(targets, 1):
        kg = kg_genes(mid, cache)
        dset, kset = set(dgenes), set(kg)
        overlap = dset & kset
        kg_only = kset - dset
        dismech_only = dset - kset
        if kg:
            n_kg_has_data += 1
        tot["dismech_genes"] += len(dset)
        tot["kg_genes"] += len(kset)
        tot["overlap"] += len(overlap)
        tot["kg_only"] += len(kg_only)
        tot["dismech_only"] += len(dismech_only)
        rows.append((name, mid, len(dset), len(kset), len(overlap),
                     ";".join(f"{g}({kg[g]})" for g in sorted(kg_only)),
                     ";".join(f"{g}({dgenes[g]})" for g in sorted(dismech_only))))
        if i % 25 == 0:
            json.dump(cache, open(args.cache, "w"))
            print(f"  ...{i}/{len(targets)}", flush=True)
    json.dump(cache, open(args.cache, "w"))

    print(f"\n# Monarch KG <-> dismech gene-disease comparison")
    print(f"diseases compared (MONDO + curated genes): {len(targets)}")
    print(f"  with >=1 KG gene edge: {n_kg_has_data}")
    print(f"  dismech gene assertions total: {tot['dismech_genes']}")
    print(f"  KG gene assertions total:      {tot['kg_genes']}")
    print(f"  overlap:                       {tot['overlap']}")
    print(f"  KG-only (dismech coverage gap):{tot['kg_only']}")
    print(f"  dismech-only (KG candidate):   {tot['dismech_only']}")

    top_gap = sorted(rows, key=lambda r: -len(r[5].split(';')) if r[5] else 0)[:20]
    print(f"\n## Top dismech coverage gaps (most KG-only genes)")
    for name, mid, nd, nk, no, kgonly, donly in top_gap:
        if kgonly:
            print(f"  {name} ({mid}): {kgonly}")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("disorder\tmondo_id\tn_dismech\tn_kg\tn_overlap\tkg_only\tdismech_only\n")
            for r in rows:
                fh.write("\t".join(str(x) for x in r) + "\n")
        print(f"\n[wrote {args.tsv} ({len(rows)} rows)]")


if __name__ == "__main__":
    main()
