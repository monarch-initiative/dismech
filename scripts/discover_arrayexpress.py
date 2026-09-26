#!/usr/bin/env python3
"""Find ArrayExpress **native** submissions that are specifically about a disease.

ArrayExpress is not an independent source for this project. Measured across
eight disease queries, **72.7% of its records are ``E-GEOD-*``** -- GEO series
re-accessioned on import (``E-GEOD-19431`` *is* ``GSE19431``). Curating those
would put the same experiment in an entry twice under two accessions that both
resolve, which no verifier could flag.

This script therefore indexes the collection and **discards every GEO import**,
keeping only submissions native to ArrayExpress/BioStudies (``E-MTAB``,
``E-MEXP``, ``E-TABM``, and other non-GEOD prefixes). That is roughly a quarter
of the collection and is genuinely additional to the GEO work.

Matching rules are shared with EGA discovery via :mod:`disease_title_match`:
the disease must be named in the study's own title, gene fallback is never
used, and sibling-disease qualifier conflicts are vetoed.

Usage
-----
    uv run python scripts/discover_arrayexpress.py --refresh
    uv run python scripts/discover_arrayexpress.py Cystic_Fibrosis
    uv run python scripts/discover_arrayexpress.py --slugs-file x.txt --out proposals.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from disease_title_match import compile_phrases, entry_phrases, match_title

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
DATA_DIR = REPO_ROOT / "data" / "arrayexpress"
INDEX_PATH = DATA_DIR / "native_studies.json"
SEARCH = "https://www.ebi.ac.uk/biostudies/api/v1/search"
USER_AGENT = "dismech-dataset-discovery (https://github.com/monarch-initiative/dismech)"

PAGE = 1000
MAX_PAGES = 120

# Imported from GEO on ingest; already covered by GEO discovery.
GEO_IMPORT_PREFIX = "E-GEOD-"


def http_json(url: str, retries: int = 3):
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except Exception as exc:
            last = exc
            time.sleep(2.0 * (attempt + 1))
    print(f"WARN  BioStudies request failed: {url} ({last})", file=sys.stderr)
    return None


def refresh_index() -> dict:
    studies: dict[str, dict] = {}
    skipped_geo = 0
    for page in range(1, MAX_PAGES + 1):
        data = http_json(f"{SEARCH}?collection=arrayexpress&pageSize={PAGE}&page={page}")
        hits = (data or {}).get("hits") or []
        if not hits:
            break
        for h in hits:
            acc = (h.get("accession") or "").strip()
            if not acc:
                continue
            if acc.startswith(GEO_IMPORT_PREFIX):
                skipped_geo += 1
                continue
            studies[acc] = {
                "title": (h.get("title") or "").strip(),
                "release_date": h.get("release_date") or "",
            }
        if page % 10 == 0:
            print(f"  page {page}: {len(studies)} native kept, {skipped_geo} GEO imports skipped",
                  file=sys.stderr, flush=True)
        if len(hits) < PAGE:
            break
        time.sleep(0.15)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(studies, indent=1, sort_keys=True) + "\n")
    (DATA_DIR / "RETRIEVED").write_text(
        f"{dt.datetime.now(dt.UTC).date().isoformat()}\nnative={len(studies)} geo_imports_skipped={skipped_geo}\n"
    )
    print(f"Wrote {INDEX_PATH}: {len(studies)} native studies "
          f"({skipped_geo} GEO imports excluded)")
    return studies


def load_index() -> dict:
    if not INDEX_PATH.exists():
        sys.exit(f"{INDEX_PATH} not found; run with --refresh first.")
    return json.loads(INDEX_PATH.read_text())


def to_record(acc: str, s: dict, matched: str, retrieved: str) -> dict:
    return {
        "accession": f"arrayexpress:{acc}",
        "title": s["title"],
        "notes": (
            f"ArrayExpress native submission (BioStudies), matched because the disease is named in "
            f"the study's own title (\"{matched}\"). GEO-imported E-GEOD records are excluded from "
            f"this source by design, since they duplicate GEO series under a second accession. "
            f"ArrayExpress index retrieved {retrieved}."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("disorder", nargs="?")
    ap.add_argument("--slugs-file", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--max-per-entry", type=int, default=3)
    args = ap.parse_args()

    if args.refresh:
        refresh_index()
        if not (args.disorder or args.slugs_file):
            return 0

    index = load_index()
    stamp = (DATA_DIR / "RETRIEVED").read_text().splitlines()[0] if (DATA_DIR / "RETRIEVED").exists() else "unknown"

    slugs = [args.disorder] if args.disorder else (
        [s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()] if args.slugs_file else []
    )
    if not slugs:
        ap.error("pass a disorder slug or --slugs-file")

    proposals, n_hit, n_conf = [], 0, 0
    for i, slug in enumerate(slugs, 1):
        path = KB_DIR / f"{slug}.yaml"
        if not path.exists():
            continue
        entry = yaml.safe_load(path.read_text()) or {}
        phrases, cores = entry_phrases(entry, slug)
        if not phrases:
            continue
        patterns = compile_phrases(phrases)

        keep = []
        for acc, s in index.items():
            if not s["title"]:
                continue
            matched, conflict = match_title(s["title"], patterns, cores)
            if not matched:
                continue
            if conflict:
                n_conf += 1
                continue
            keep.append((acc, s, matched))
        keep.sort(key=lambda t: -len(t[2]))
        keep = keep[: args.max_per_entry]
        n_hit += len(keep)

        if keep and args.out is not None:
            proposals.append({
                "slug": slug,
                "disease_name": (entry.get("name") or slug).replace("_", " "),
                "n_candidates": len(keep),
                "records": [
                    {"approved": True, "matched_phrase": m, "record": to_record(a, s, m, stamp)}
                    for a, s, m in keep
                ],
            })
        elif keep:
            for a, s, m in keep:
                print(f"  [OK] {slug}: arrayexpress:{a}  [{m}]  {s['title'][:80]}")
        if args.slugs_file and i % 300 == 0:
            print(f"  ...{i}/{len(slugs)}", file=sys.stderr, flush=True)

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(proposals, indent=2) + "\n")
        print(f"\nWrote {args.out}: {sum(len(p['records']) for p in proposals)} records "
              f"across {len(proposals)} entries")
    print(f"\nTITLE_MATCH: {n_hit}   CONFLICT (vetoed): {n_conf}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
