#!/usr/bin/env python3
"""Find datasets via OmicsDI, restricted to repositories not already mined.

OmicsDI is an aggregator, so most of what it returns is already covered.
Measured across six disease queries (600 hits):

    biostudies-literature     313   52%
    biostudies-arrayexpress   177   30%   <- already mined (ArrayExpress)
    pride / metabolights / ega / geo  44   7%   <- already mined
    everything else            66   11%   <- genuinely new

So OmicsDI is used here only as a *router* to repositories this project has
no other route into, via an explicit allowlist:

``metabolomics_workbench``
    The most valuable of them. Metabolomics is the right assay for inborn
    errors of metabolism -- exactly the entries GEO failed on, where the only
    GEO candidate for maple syrup urine disease was a BCKD-*kinase* study
    that had to be rejected as the mechanistic opposite.
``massive``, ``dbgap``
    Proteomics and controlled-access human cohorts; both already have
    verifier resolvers.

Excluded on purpose:

* ``biostudies-arrayexpress``, ``pride``, ``metabolights``, ``ega``, ``geo`` --
  duplicates of sources with their own discovery path here.
* ``biostudies-literature`` -- supplementary files attached to papers rather
  than deposited datasets, and the single largest bucket; curating them would
  swamp the KB with figure/table records.
* ``jpost``, ``iprox``, ``gpmdb``, ``panorama``, ``biomodels``, ``ecrin-mdr-crc``,
  ``project`` -- no resolver, so an accession could not be verified. Reported
  in the summary, never curated.

Matching uses the shared narrow rules (:mod:`disease_title_match`): the disease
must be named in the dataset's own title, genes are never searched, and
sibling-disease qualifier conflicts are vetoed.

Usage
-----
    uv run python scripts/discover_omicsdi.py Phenylketonuria
    uv run python scripts/discover_omicsdi.py --slugs-file x.txt --out proposals.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from disease_title_match import compile_phrases, entry_phrases, match_title

REPO_ROOT = Path(__file__).resolve().parents[1]
KB_DIR = REPO_ROOT / "kb" / "disorders"
SEARCH = "https://www.omicsdi.org/ws/dataset/search"
USER_AGENT = "dismech-dataset-discovery (https://github.com/monarch-initiative/dismech)"

# OmicsDI source -> dismech accession prefix. Only sources we can both reach
# and verify. Everything else is counted and reported, never curated.
SOURCE_TO_PREFIX = {
    "metabolomics_workbench": "metabolomics_workbench",
    "massive": "massive",
    "dbgap": "dbgap",
}

PAGE_SIZE = 100
THROTTLE_S = 0.35


def clean_description(value: str, limit: int = 600) -> str:
    """Strip source markup and truncate only at a sentence or word boundary."""
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]*>", " ", text)
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    window = text[: limit + 1]
    sentence_end = max(window.rfind(". "), window.rfind("? "), window.rfind("! "))
    if sentence_end >= limit // 3:
        return window[: sentence_end + 1]
    return window[:limit].rsplit(" ", 1)[0].rstrip(" ,;:")


def http_json(url: str, retries: int = 3):
    last: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except Exception as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    print(f"WARN  OmicsDI request failed ({last})", file=sys.stderr)
    return None


def normalise_accession(source: str, raw_id: str) -> str:
    prefix = SOURCE_TO_PREFIX[source]
    local = raw_id.strip()
    if prefix == "dbgap" and not local.lower().startswith("phs"):
        return ""
    return f"{prefix}:{local}"


def search(disease_name: str) -> list[dict]:
    q = urllib.parse.quote(disease_name)
    data = http_json(f"{SEARCH}?query={q}&size={PAGE_SIZE}")
    return (data or {}).get("datasets") or []


def to_record(acc: str, hit: dict, matched: str, today: str) -> dict:
    rec: dict = {"accession": acc, "title": (hit.get("title") or "").strip()}
    desc = clean_description(hit.get("description") or "")
    if desc:
        rec["description"] = desc
    rec["notes"] = (
        f"Located via OmicsDI, which aggregates across omics repositories; this record comes from "
        f"{hit.get('source')}. Only repositories with no other discovery route in this project and "
        f"with a working accession resolver are curated from OmicsDI -- GEO, ArrayExpress, PRIDE, "
        f"MetaboLights and EGA hits are excluded as duplicates of dedicated passes. Matched because "
        f'the disease is named in the dataset\'s own title ("{matched}"). Retrieved {today}.'
    )
    return rec


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("disorder", nargs="?")
    ap.add_argument("--slugs-file", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--max-per-entry", type=int, default=3)
    args = ap.parse_args()

    slugs = (
        [args.disorder]
        if args.disorder
        else (
            [s.strip() for s in args.slugs_file.read_text().splitlines() if s.strip()]
            if args.slugs_file
            else []
        )
    )
    if not slugs:
        ap.error("pass a disorder slug or --slugs-file")

    today = dt.datetime.now(dt.UTC).date().isoformat()
    proposals: list[dict] = []
    seen_sources: Counter = Counter()
    skipped_sources: Counter = Counter()
    n_kept = n_conflict = 0

    for i, slug in enumerate(slugs, 1):
        path = KB_DIR / f"{slug}.yaml"
        if not path.exists():
            continue
        entry = yaml.safe_load(path.read_text()) or {}
        phrases, cores = entry_phrases(entry, slug)
        if not phrases:
            continue
        disease_name = (entry.get("name") or slug).replace("_", " ")

        hits = search(disease_name)
        time.sleep(THROTTLE_S)
        keep = []
        for h in hits:
            source = (h.get("source") or "").lower()
            seen_sources[source] += 1
            if source not in SOURCE_TO_PREFIX:
                skipped_sources[source] += 1
                continue
            title = (h.get("title") or "").strip()
            if not title:
                continue
            matched, conflict = match_title(title, compile_phrases(phrases), cores)
            if not matched:
                continue
            if conflict:
                n_conflict += 1
                continue
            acc = normalise_accession(source, h.get("id") or "")
            if acc:
                keep.append((acc, h, matched))

        keep = keep[: args.max_per_entry]
        n_kept += len(keep)
        if keep:
            if args.out is not None:
                proposals.append(
                    {
                        "slug": slug,
                        "disease_name": disease_name,
                        "n_candidates": len(keep),
                        "records": [
                            {
                                "approved": True,
                                "matched_phrase": m,
                                "source": h.get("source"),
                                "record": to_record(a, h, m, today),
                            }
                            for a, h, m in keep
                        ],
                    }
                )
            else:
                for a, h, m in keep:
                    print(
                        f"  [OK] {slug}: {a}  ({h.get('source')})  {(h.get('title') or '')[:70]}"
                    )
        if args.slugs_file and i % 100 == 0:
            print(f"  ...{i}/{len(slugs)}  kept={n_kept}", file=sys.stderr, flush=True)

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(proposals, indent=2) + "\n")
        print(
            f"\nWrote {args.out}: {sum(len(p['records']) for p in proposals)} records "
            f"across {len(proposals)} entries"
        )

    print(
        f"\nkept: {n_kept}   vetoed (qualifier conflict): {n_conflict}", file=sys.stderr
    )
    print("sources skipped as duplicate/unverifiable:", file=sys.stderr)
    for s, c in skipped_sources.most_common(12):
        print(f"  {s:28s} {c}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
