#!/usr/bin/env python3
"""Find phenopacket-store cohorts for dismech entries, matched by disease *identity*.

This is the rare-disease counterpart to :mod:`discover_datasets`, and it is
built on a stronger guarantee.

GEO discovery has to match on words, because a GEO series carries no coded
disease. That is why searching a causal gene there is dangerous: a GEO hit for
gene X is usually a study *about something else* that used gene X (searching
``FTL`` for neuroferritinopathy returns Alzheimer and medulloblastoma series).

A phenopacket-store cohort is different in kind. Each case carries:

* a coded disease term (``OMIM:608776``), not a title string
* the source ``PMID`` it was curated from
* HPO-coded phenotypic features

So a cohort can be matched to a dismech entry on **identifier equality** --
the entry's MONDO term resolved to its OMIM xrefs, compared against the
disease IDs the cohort's cases actually carry. Gene agreement alone is
reported but never sufficient.

Relevance tiers
---------------
``DISEASE_ID_MATCH``
    The cohort's coded disease is an OMIM/MONDO xref of the entry's own
    ``disease_term``. Safe to curate.
``GENE_ONLY``
    The causal gene matches but the coded disease does not. The cohort is
    about a *different* disease caused by the same gene -- report, never
    auto-propose.

Usage
-----
    # refresh the bulk release (one download, no GitHub API rate limit)
    uv run python scripts/discover_phenopackets.py --refresh

    # candidates for one entry
    uv run python scripts/discover_phenopackets.py Achondroplasia

    # propose across many entries, writing a triage file
    uv run python scripts/discover_phenopackets.py --slugs-file mendelian.txt \\
        --out research/dataset_proposals/pps1.json

    # coverage report: which entries a cohort exists for
    uv run python scripts/discover_phenopackets.py --coverage
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
DATA_DIR = REPO_ROOT / "data" / "phenopacket-store"
ARCHIVE = DATA_DIR / "all_phenopackets.zip"
INDEX_PATH = DATA_DIR / "cohort_index.json"
XREF_CACHE = REPO_ROOT / "cache" / "mondo_omim_xrefs.json"
RELEASES = "https://api.github.com/repos/monarch-initiative/phenopacket-store/releases/latest"

MIN_CASES = 2


def fetch_release() -> None:
    """Download the latest all_phenopackets.zip release asset."""
    with urllib.request.urlopen(RELEASES, timeout=60) as resp:
        rel = json.loads(resp.read())
    asset = next((a for a in rel.get("assets", []) if a["name"] == "all_phenopackets.zip"), None)
    if not asset:
        sys.exit("No all_phenopackets.zip asset in the latest release.")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Downloading phenopacket-store {rel['tag_name']} ({asset['size'] / 1e6:.1f} MB)...")
    urllib.request.urlretrieve(asset["browser_download_url"], ARCHIVE)
    (DATA_DIR / "RELEASE").write_text(rel["tag_name"] + "\n")
    print(f"Wrote {ARCHIVE}")


def build_index() -> dict:
    """Summarise each cohort: coded diseases, PMIDs, case count, HPO breadth."""
    if not ARCHIVE.exists():
        sys.exit(f"{ARCHIVE} not found; run with --refresh first.")

    cohorts: dict[str, dict] = defaultdict(
        lambda: {"n_cases": 0, "diseases": Counter(), "labels": {}, "pmids": Counter(), "hpo_terms": set()}
    )
    with zipfile.ZipFile(ARCHIVE) as z:
        for name in z.namelist():
            if not name.endswith(".json") or name.count("/") < 2:
                continue
            cohort = name.split("/")[1]
            try:
                pk = json.loads(z.read(name))
            except Exception:
                continue
            c = cohorts[cohort]
            c["n_cases"] += 1
            for dz in pk.get("diseases") or []:
                term = dz.get("term") or {}
                if term.get("id"):
                    c["diseases"][term["id"]] += 1
                    c["labels"][term["id"]] = term.get("label", "")
            for interp in pk.get("interpretations") or []:
                term = (interp.get("diagnosis") or {}).get("disease") or {}
                if term.get("id"):
                    c["diseases"][term["id"]] += 1
                    c["labels"][term["id"]] = term.get("label", "")
            for ref in (pk.get("metaData") or {}).get("externalReferences") or []:
                if str(ref.get("id", "")).startswith("PMID:"):
                    c["pmids"][ref["id"]] += 1
            for feat in pk.get("phenotypicFeatures") or []:
                tid = (feat.get("type") or {}).get("id")
                if tid and not feat.get("excluded"):
                    c["hpo_terms"].add(tid)

    out = {
        k: {
            "n_cases": v["n_cases"],
            "diseases": dict(v["diseases"]),
            "labels": v["labels"],
            "pmids": dict(v["pmids"]),
            "n_hpo_terms": len(v["hpo_terms"]),
        }
        for k, v in cohorts.items()
    }
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    return out


def load_index() -> dict:
    if INDEX_PATH.exists():
        return json.loads(INDEX_PATH.read_text())
    return build_index()


OLS4_TERM = "https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id="


def mondo_xrefs(mondo_id: str, cache: dict) -> list[str]:
    """OMIM/Orphanet xrefs for a MONDO term.

    Uses the OLS4 REST API rather than the local OAK sqlite adapter: OAK is
    currently unimportable under this project's Python (pyhornedowl raises
    ``AttributeError: 'typing.Union' object attribute '__doc__' is read-only``),
    which makes every OAK-backed lookup silently return nothing.
    """
    if not mondo_id:
        return []
    if mondo_id in cache:
        return cache[mondo_id]

    xrefs: list[str] = [mondo_id]  # cohorts sometimes code MONDO directly
    try:
        with urllib.request.urlopen(OLS4_TERM + urllib.parse.quote(mondo_id), timeout=45) as resp:
            data = json.loads(resp.read())
        terms = (data.get("_embedded") or {}).get("terms") or []
        for x in (terms[0].get("obo_xref") or []) if terms else []:
            db, xid = (x.get("database") or "").upper(), (x.get("id") or "").strip()
            if not xid:
                continue
            if db == "OMIM":
                xrefs.append(f"OMIM:{xid}")
            elif db in ("ORPHANET", "ORPHA"):
                xrefs.append(f"ORPHA:{xid}")
                xrefs.append(f"Orphanet:{xid}")
    except Exception as exc:
        print(f"WARN  MONDO xref lookup failed for {mondo_id}: {exc}", file=sys.stderr)
        return xrefs

    cache[mondo_id] = sorted(set(xrefs))
    return cache[mondo_id]


def entry_genes(entry: dict) -> list[str]:
    genes = []
    for g in entry.get("genetic") or []:
        sym = (((g.get("gene_term") or {}).get("term") or {}).get("label") or g.get("name") or "").strip()
        if re.fullmatch(r"[A-Z0-9orf\-]{2,12}", sym):
            genes.append(sym)
    return list(dict.fromkeys(genes))


def match_entry(slug: str, index: dict, xcache: dict) -> list[dict]:
    path = KB_DIR / f"{slug}.yaml"
    if not path.exists():
        return []
    entry = yaml.safe_load(path.read_text()) or {}
    mondo = (((entry.get("disease_term") or {}).get("term") or {}).get("id") or "").strip()
    accepted = set(mondo_xrefs(mondo, xcache))

    results = []
    for gene in entry_genes(entry):
        c = index.get(gene)
        if not c or c["n_cases"] < MIN_CASES:
            continue
        coded = set(c["diseases"])
        overlap = coded & accepted
        results.append(
            {
                "cohort": gene,
                "gene": gene,
                "n_cases": c["n_cases"],
                "diseases": c["diseases"],
                "labels": c["labels"],
                "pmids": sorted(c["pmids"]),
                "n_hpo_terms": c["n_hpo_terms"],
                "relevance": "DISEASE_ID_MATCH" if overlap else "GENE_ONLY",
                "matched_ids": sorted(overlap),
                "entry_mondo": mondo,
            }
        )
    return results


def to_record(m: dict, disease_name: str, release: str) -> dict:
    top_id, _ = max(m["diseases"].items(), key=lambda kv: kv[1])
    label = m["labels"].get(top_id, "")
    rec = {
        "accession": f"phenopacket-store:{m['cohort']}",
        "title": f"phenopacket-store {m['cohort']} cohort: {label}" if label else f"phenopacket-store {m['cohort']} cohort",
        "description": (
            f"GA4GH phenopacket cohort for {m['cohort']}, comprising {m['n_cases']} published "
            f"case-level phenopackets coded to {top_id} ({label}) with {m['n_hpo_terms']} distinct "
            f"HPO terms across the cohort. Each case is curated from a peer-reviewed report and "
            f"carries its source PMID."
        ),
        "organism": {"preferred_term": "human", "term": {"id": "NCBITaxon:9606", "label": "Homo sapiens"}},
        "data_type": "PHENOPACKETS",
        "sample_count": m["n_cases"],
    }
    if m["pmids"]:
        rec["publication"] = m["pmids"][0]
    today = dt.datetime.now(dt.UTC).date().isoformat()
    rec["notes"] = (
        f"Matched to this entry by disease identifier, not by name: the cohort's coded disease "
        f"({', '.join(m['matched_ids'])}) is an xref of the entry's MONDO term {m['entry_mondo']}. "
        f"phenopacket-store release {release}; indexed {today}. "
        f"Source PMIDs: {', '.join(m['pmids'][:8])}{' and others' if len(m['pmids']) > 8 else ''}."
    )
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("disorder", nargs="?")
    ap.add_argument("--slugs-file", type=Path)
    ap.add_argument("--out", type=Path, help="write a proposal JSON for triage")
    ap.add_argument("--refresh", action="store_true", help="re-download the release and rebuild the index")
    ap.add_argument("--reindex", action="store_true", help="rebuild the index from the existing archive")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--include-gene-only", action="store_true",
                    help="also emit GENE_ONLY matches (never auto-approved)")
    args = ap.parse_args()

    if args.refresh:
        fetch_release()
        build_index()
        print(f"Indexed {len(load_index())} cohorts.")
        if not (args.disorder or args.slugs_file or args.coverage):
            return 0
    if args.reindex:
        build_index()

    index = load_index()
    release = (DATA_DIR / "RELEASE").read_text().strip() if (DATA_DIR / "RELEASE").exists() else "unknown"
    xcache = json.loads(XREF_CACHE.read_text()) if XREF_CACHE.exists() else {}

    slugs: list[str] = []
    if args.disorder:
        slugs = [args.disorder]
    elif args.slugs_file:
        slugs = [s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()]
    elif args.coverage:
        slugs = sorted(p.stem for p in KB_DIR.glob("*.yaml"))
    else:
        ap.error("pass a disorder slug, --slugs-file, --coverage, or --refresh")

    proposals, n_direct, n_gene = [], 0, 0
    for i, slug in enumerate(slugs, 1):
        matches = match_entry(slug, index, xcache)
        direct = [m for m in matches if m["relevance"] == "DISEASE_ID_MATCH"]
        gene_only = [m for m in matches if m["relevance"] == "GENE_ONLY"]
        n_direct += len(direct)
        n_gene += len(gene_only)
        if not matches:
            continue

        entry = yaml.safe_load((KB_DIR / f"{slug}.yaml").read_text()) or {}
        disease_name = (entry.get("name") or slug).replace("_", " ")
        chosen = direct + (gene_only if args.include_gene_only else [])
        if chosen and args.out is not None:
            proposals.append({
                "slug": slug,
                "disease_name": disease_name,
                "n_candidates": len(matches),
                "records": [
                    {"approved": m["relevance"] == "DISEASE_ID_MATCH",
                     "relevance": m["relevance"],
                     "matched_ids": m["matched_ids"],
                     "reject_reason": None if m["relevance"] == "DISEASE_ID_MATCH" else
                                      f"gene {m['gene']} matches but the cohort codes "
                                      f"{sorted(m['diseases'])} , not an xref of {m['entry_mondo']}",
                     "record": to_record(m, disease_name, release)}
                    for m in chosen
                ],
            })
        if not args.out:
            for m in matches:
                flag = "OK " if m["relevance"] == "DISEASE_ID_MATCH" else "GENE"
                ids = ", ".join(f"{k}={v}" for k, v in list(m["diseases"].items())[:3])
                print(f"  [{flag}] {slug}: cohort {m['cohort']}  n={m['n_cases']}  {ids}")
        if args.slugs_file and i % 50 == 0:
            print(f"  ...{i}/{len(slugs)}", file=sys.stderr, flush=True)

    XREF_CACHE.parent.mkdir(parents=True, exist_ok=True)
    XREF_CACHE.write_text(json.dumps(xcache, indent=2, sort_keys=True) + "\n")

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(proposals, indent=2) + "\n")
        total = sum(len(p["records"]) for p in proposals)
        print(f"\nWrote {args.out}: {total} records across {len(proposals)} entries")
    print(f"\nDISEASE_ID_MATCH: {n_direct}   GENE_ONLY (withheld): {n_gene}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
