#!/usr/bin/env python3
"""Pilot analysis for issue #5000: how much of dismech's PMID-backed evidence
could be classified by a CEBM/GRADE-style level of evidence.

This does NOT modify any kb/ files or the schema. It:

1. Walks kb/disorders/*.yaml and kb/modules/*.yaml (excluding *.history.yaml)
   and recursively collects every EvidenceItem-shaped dict (has `reference`
   and `evidence_source`).
2. Extracts the unique set of PMID: references.
3. Batch-queries NCBI EFetch (db=pubmed, rettype=xml) for the MEDLINE
   `PublicationTypeList` of each PMID -- this is a structured field curated
   by NLM indexers, distinct from (and more reliable than) the MeSH
   `*_headings* keywords` already cached in references_cache/*.md.
4. Cross-tabulates evidence_source x publication_type-derived CEBM-ish
   bucket and writes a JSON summary + prints a report to stdout.

Usage:
    uv run python scripts/cebm_pilot_analysis.py --out research/cebm_pilot_data.json
    uv run python scripts/cebm_pilot_analysis.py --sample 2000   # faster dev run
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterator

import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_DIRS = [REPO_ROOT / "kb" / "disorders", REPO_ROOT / "kb" / "modules"]
EUTILS_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
BATCH_SIZE = 200
RATE_DELAY_S = 0.35  # NCBI: max 3 req/s without an API key

# Bucketing of MEDLINE PublicationType strings into a rough CEBM-oriented tier.
# This is a coarse pilot mapping, not a final classification scheme.
LEVEL_1_SR = {"Meta-Analysis", "Systematic Review"}
LEVEL_2_RCT = {"Randomized Controlled Trial", "Controlled Clinical Trial", "Pragmatic Clinical Trial"}
LEVEL_3_OBS = {
    "Clinical Trial",
    "Clinical Trial, Phase I",
    "Clinical Trial, Phase II",
    "Clinical Trial, Phase III",
    "Clinical Trial, Phase IV",
    "Clinical Trial Protocol",
    "Comparative Study",
    "Multicenter Study",
    "Observational Study",
    "Cohort Studies",
}
LEVEL_4_CASE = {"Case Reports", "Historical Article"}
GUIDELINE = {"Practice Guideline", "Guideline", "Consensus Development Conference", "Consensus Development Conference, NIH"}
NARRATIVE_REVIEW = {"Review"}
NON_EVIDENTIARY = {"Letter", "Comment", "Editorial", "News", "Biography", "Retraction of Publication", "Retracted Publication"}


def load_kb_evidence() -> list[dict[str, Any]]:
    """Return a flat list of {file, reference, evidence_source, supports, section} dicts.

    `section` is the top-level Disease/Grouping slot the evidence item was found
    under (e.g. "pathophysiology", "treatments", "clinical_trials", "phenotypes"),
    which lets us separate mechanism-assertion evidence from treatment-efficacy
    evidence -- CEBM levels of evidence are designed for the latter.
    """
    items: list[dict[str, Any]] = []
    for kb_dir in KB_DIRS:
        for path in sorted(kb_dir.glob("*.yaml")):
            if path.name.endswith(".history.yaml"):
                continue
            try:
                doc = yaml.safe_load(path.read_text())
            except yaml.YAMLError as e:
                print(f"WARN: could not parse {path}: {e}", file=sys.stderr)
                continue
            if not isinstance(doc, dict):
                continue
            for top_key, top_val in doc.items():
                for ev in _find_evidence_items(top_val):
                    items.append({"file": str(path.relative_to(REPO_ROOT)), "section": top_key, **ev})
    return items


def _find_evidence_items(node: Any) -> Iterator[dict[str, Any]]:
    """Recursively yield dict nodes that look like an EvidenceItem."""
    if isinstance(node, dict):
        if "reference" in node and ("evidence_source" in node or "supports" in node):
            yield {
                "reference": node.get("reference"),
                "evidence_source": node.get("evidence_source", "HUMAN_CLINICAL"),
                "supports": node.get("supports"),
            }
        for v in node.values():
            yield from _find_evidence_items(v)
    elif isinstance(node, list):
        for v in node:
            yield from _find_evidence_items(v)


def fetch_publication_types(pmids: list[str]) -> dict[str, list[str]]:
    """Batch-fetch MEDLINE PublicationType tags for a list of bare PMIDs."""
    result: dict[str, list[str]] = {}
    total_batches = (len(pmids) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(0, len(pmids), BATCH_SIZE):
        batch = pmids[i : i + BATCH_SIZE]
        batch_no = i // BATCH_SIZE + 1
        print(f"  batch {batch_no}/{total_batches} ({len(batch)} PMIDs)...", file=sys.stderr)
        params = {
            "db": "pubmed",
            "id": ",".join(batch),
            "rettype": "xml",
            "retmode": "xml",
        }
        for attempt in range(3):
            try:
                resp = requests.get(EUTILS_EFETCH, params=params, timeout=60)
                resp.raise_for_status()
                break
            except requests.RequestException as e:
                print(f"    retry {attempt+1}: {e}", file=sys.stderr)
                time.sleep(2)
        else:
            print(f"    FAILED batch starting at {batch[0]}, skipping", file=sys.stderr)
            time.sleep(RATE_DELAY_S)
            continue

        try:
            root = ET.fromstring(resp.content)
        except ET.ParseError as e:
            print(f"    XML parse error: {e}", file=sys.stderr)
            time.sleep(RATE_DELAY_S)
            continue

        for article in root.iter("PubmedArticle"):
            pmid_el = article.find(".//MedlineCitation/PMID")
            if pmid_el is None or not pmid_el.text:
                continue
            pmid = pmid_el.text.strip()
            pub_types = [
                pt.text.strip()
                for pt in article.findall(".//PublicationTypeList/PublicationType")
                if pt.text
            ]
            result[pmid] = pub_types
        # Some IDs come back as PubmedBookArticle (NCBI Bookshelf) - no PublicationTypeList; leave absent.
        time.sleep(RATE_DELAY_S)
    return result


def bucket(pub_types: list[str]) -> str:
    types = set(pub_types)
    if types & LEVEL_1_SR:
        return "L1_SYSTEMATIC_REVIEW_META_ANALYSIS"
    if types & LEVEL_2_RCT:
        return "L2_RCT"
    if types & GUIDELINE:
        return "GUIDELINE"
    if types & LEVEL_3_OBS:
        return "L3_TRIAL_OR_OBSERVATIONAL"
    if types & LEVEL_4_CASE:
        return "L4_CASE_REPORT_SERIES"
    if types & NARRATIVE_REVIEW:
        return "NARRATIVE_REVIEW"
    if types & NON_EVIDENTIARY:
        return "NON_EVIDENTIARY"
    if not types:
        return "UNKNOWN_NO_PUBTYPE"
    return "JOURNAL_ARTICLE_UNCLASSIFIED"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(REPO_ROOT / "research" / "cebm_pilot_data.json"))
    ap.add_argument("--sample", type=int, default=0, help="If >0, only query this many unique PMIDs (for dev runs)")
    ap.add_argument(
        "--pubtype-cache",
        default=str(REPO_ROOT / "research" / "cebm_pilot_pubtypes_cache.json"),
        help="Local cache of pmid -> [PublicationType,...] to avoid re-querying NCBI on reruns",
    )
    args = ap.parse_args()

    print("Loading evidence items from kb/disorders and kb/modules...", file=sys.stderr)
    items = load_kb_evidence()
    print(f"  {len(items)} total EvidenceItem-shaped nodes found", file=sys.stderr)

    pmid_items = [it for it in items if isinstance(it["reference"], str) and it["reference"].startswith("PMID:")]
    print(f"  {len(pmid_items)} are PMID-backed", file=sys.stderr)

    unique_pmids = sorted({it["reference"].split(":", 1)[1] for it in pmid_items}, key=int)
    print(f"  {len(unique_pmids)} unique PMIDs", file=sys.stderr)

    if args.sample:
        unique_pmids = unique_pmids[: args.sample]
        print(f"  --sample set: querying only {len(unique_pmids)} PMIDs", file=sys.stderr)

    cache_path = Path(args.pubtype_cache)
    pub_types_by_pmid: dict[str, list[str]] = {}
    if cache_path.exists():
        pub_types_by_pmid = json.loads(cache_path.read_text())
        print(f"  loaded {len(pub_types_by_pmid)} cached pubtypes from {cache_path}", file=sys.stderr)

    to_fetch = [p for p in unique_pmids if p not in pub_types_by_pmid]
    if to_fetch:
        print(f"Querying NCBI EFetch for PublicationTypeList ({len(to_fetch)} uncached PMIDs)...", file=sys.stderr)
        fetched = fetch_publication_types(to_fetch)
        pub_types_by_pmid.update(fetched)
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(pub_types_by_pmid, indent=2, sort_keys=True))
    print(
        f"  have publication types for {sum(1 for p in unique_pmids if p in pub_types_by_pmid)}/{len(unique_pmids)} PMIDs",
        file=sys.stderr,
    )

    pmid_bucket: dict[str, str] = {pmid: bucket(pub_types_by_pmid.get(pmid, [])) for pmid in unique_pmids}

    crosstab: dict[str, Counter] = defaultdict(Counter)
    bucket_totals: Counter = Counter()
    section_bucket: dict[str, Counter] = defaultdict(Counter)
    section_totals: Counter = Counter()

    for it in pmid_items:
        pmid = it["reference"].split(":", 1)[1]
        if pmid not in pmid_bucket:
            continue  # not in sampled set
        b = pmid_bucket[pmid]
        crosstab[it["evidence_source"]][b] += 1
        bucket_totals[b] += 1
        section_bucket[it["section"]][b] += 1
        section_totals[it["section"]] += 1

    n_evidence_items_covered = sum(bucket_totals.values())

    report = {
        "total_evidence_items_all_sources": len(items),
        "total_pmid_backed_evidence_items": len(pmid_items),
        "unique_pmids_total": len(unique_pmids),
        "unique_pmids_queried": len(unique_pmids),
        "unique_pmids_with_pubtype_data": sum(1 for p in unique_pmids if p in pub_types_by_pmid),
        "evidence_items_covered_by_this_run": n_evidence_items_covered,
        "bucket_totals_unique_pmids": dict(Counter(pmid_bucket.values())),
        "bucket_totals_evidence_items": dict(bucket_totals),
        "crosstab_evidence_source_x_bucket": {k: dict(v) for k, v in crosstab.items()},
        "section_totals": dict(section_totals),
        "crosstab_section_x_bucket": {k: dict(v) for k, v in section_bucket.items()},
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True))
    print(f"\nWrote {out_path}", file=sys.stderr)

    print("\n=== SUMMARY ===")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
