#!/usr/bin/env python3
"""dismech#7175 content evaluation: Monarch KG <-> dismech gene-disease comparison.

For every disorder with a MONDO primary anchor AND curated genes, compare dismech's gene
set against the Monarch KG's gene-disease edges for that MONDO term (Causal + Correlated
gene-to-disease associations, via the Monarch v3 API).

dismech genes are read from BOTH the top-level ``genetic[].gene_term`` and the
``has_subtypes[].genes[]`` blocks (both model disease genes per CLAUDE.md), so a gene
curated only on a subtype is not falsely reported as a coverage gap.

Emits, per disease:
  - overlap        : genes in both
  - kg_only        : genes the KG links to the disease but dismech does not  (dismech COVERAGE GAP)
  - dismech_only   : genes dismech curates but the KG does not link          (dismech -> KG candidate / to verify)

Robustness: KG fetches paginate over the full result set (offset/total), and a fetch that
exhausts its retries RAISES rather than being cached as an empty result -- so a network
failure is never silently indistinguishable from "the KG has no edges" (that distinction is
load-bearing for the no-edge headline). Such diseases are counted as fetch_errors and skipped.

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
PAGE = 500


def norm(hgnc):
    """Normalize dismech 'hgnc:11025' and KG 'HGNC:11025' to a common key."""
    return hgnc.replace("hgnc:", "HGNC:") if hgnc else hgnc


def _gene_from_term(gene_term):
    term = (gene_term or {}).get("term") or {}
    tid = term.get("id")
    if tid and tid.lower().startswith("hgnc:"):
        return norm(tid), (term.get("label") or (gene_term or {}).get("preferred_term") or "")
    return None, None


def dismech_genes(doc):
    out = {}
    for g in (doc or {}).get("genetic") or []:
        key, label = _gene_from_term(g.get("gene_term"))
        if key:
            out[key] = label
    # genes may also be modeled on subtypes (has_subtypes[].genes[])
    for st in (doc or {}).get("has_subtypes") or []:
        for g in st.get("genes") or []:
            gt = g.get("gene_term") or g  # subtype gene may carry gene_term or be a descriptor
            key, label = _gene_from_term(gt if "term" in gt else {"term": gt.get("term")})
            if key:
                out.setdefault(key, label)
    return out


def _fetch_page(cat, mondo_id, offset):
    params = urllib.parse.urlencode({"category": cat, "object": mondo_id,
                                     "limit": PAGE, "offset": offset})
    url = f"{API}?{params}"
    last = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=45) as resp:
                return json.load(resp)
        except Exception as e:
            last = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"KG fetch failed after retries: {url}: {last}")


def kg_genes(mondo_id, cache):
    if mondo_id in cache:
        return cache[mondo_id]
    genes = {}
    for cat in GENE_CATS:
        offset = 0
        while True:
            data = _fetch_page(cat, mondo_id, offset)
            for it in data.get("items", []):
                subj = it.get("subject", "")
                if subj.startswith("HGNC:"):
                    genes[subj] = it.get("subject_label") or ""
            offset += PAGE
            if offset >= (data.get("total") or 0):
                break
            time.sleep(0.1)
        time.sleep(0.1)
    cache[mondo_id] = genes  # only cached on full success (a failed fetch raised above)
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
        term = ((doc or {}).get("disease_term") or {}).get("term") or {}
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
    n_kg_has_data, fetch_errors = 0, []
    for i, (name, mid, dgenes) in enumerate(targets, 1):
        try:
            kg = kg_genes(mid, cache)
        except RuntimeError as e:
            fetch_errors.append((name, mid, str(e)))
            continue
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

    # Tiered analysis: separate broad/grouping-anchor noise from interpretable gaps.
    BROAD = 30

    def cnt(s):
        return 0 if not s else len(s.split(";"))
    R = [{"disorder": r[0], "mondo": r[1], "nd": r[2], "nk": r[3], "nov": r[4],
          "kg_only": r[5], "dismech_only": r[6], "nko": cnt(r[5]), "ndo": cnt(r[6])}
         for r in rows]
    no_kg = [r for r in R if r["nk"] == 0]
    broad = [r for r in R if r["nk"] > BROAD]
    clean = [r for r in R if 0 < r["nk"] <= BROAD]
    clean_kg_only = sum(r["nko"] for r in clean)

    print("\n# Monarch KG <-> dismech gene-disease comparison")
    print(f"diseases compared (MONDO + curated genes): {len(targets)}")
    print(f"  fetch errors (skipped, NOT counted as no-edge): {len(fetch_errors)}")
    for name, mid, err in fetch_errors[:10]:
        print(f"     ! {name} ({mid}): {err}")
    print(f"  with >=1 KG gene edge: {n_kg_has_data}")
    print(f"  dismech gene assertions total: {tot['dismech_genes']}")
    print(f"  KG gene assertions total:      {tot['kg_genes']}")
    print(f"  overlap:                       {tot['overlap']}")
    print(f"  KG-only (dismech coverage gap, RAW): {tot['kg_only']}")
    print(f"  dismech-only (KG candidate/verify):  {tot['dismech_only']}")

    print("\n## Tiers by KG gene count")
    print(f"  no KG gene edge:            {len(no_kg)}")
    print(f"  broad-anchor (n_kg>{BROAD}):      {len(broad)}  "
          f"(contribute {sum(r['nko'] for r in broad)} of raw kg_only -> anchoring problem, not gaps)")
    print(f"  clean (1..{BROAD}):              {len(clean)}  "
          f"(clean kg_only = {clean_kg_only} real coverage-gap candidates)")

    print(f"\n## Broad-anchor diseases (n_kg>{BROAD}) -- likely broad/mis-anchor (top 15 by n_kg)")
    for r in sorted(broad, key=lambda x: -x["nk"])[:15]:
        print(f"  {r['disorder']} ({r['mondo']}) n_kg={r['nk']} n_dismech={r['nd']}")

    print("\n## Top clean coverage gaps (dismech missing genes KG has; top 20 by kg_only)")
    for r in sorted(clean, key=lambda x: -x["nko"])[:20]:
        if r["nko"]:
            print(f"  {r['disorder']} ({r['mondo']}) nd={r['nd']} nk={r['nk']} ov={r['nov']}: {r['kg_only']}")

    zero = [r for r in clean if r["nov"] == 0 and r["nd"] > 0 and r["nk"] > 0]
    print(f"\n## Zero-overlap disagreements (dismech & KG both have genes, none shared): {len(zero)}")
    for r in sorted(zero, key=lambda x: -(x["nd"] + x["nk"]))[:20]:
        print(f"  {r['disorder']} ({r['mondo']}): dismech[{r['dismech_only']}] vs KG[{r['kg_only']}]")

    if args.tsv:
        with open(args.tsv, "w") as fh:
            fh.write("disorder\tmondo_id\tn_dismech\tn_kg\tn_overlap\tkg_only\tdismech_only\n")
            fh.writelines("\t".join(str(x) for x in r) + "\n" for r in rows)
        print(f"\n[wrote {args.tsv} ({len(rows)} rows)]")


if __name__ == "__main__":
    main()
