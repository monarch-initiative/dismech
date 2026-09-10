#!/usr/bin/env python3
"""Build the committed NCBI Bookshelf title index under ``cache/bookshelf/``.

Two point-of-reference collections on the NCBI Bookshelf are PubMed-indexed as
*books* rather than journal articles, so PubMed's ``[book]`` field selects every
chapter of each exactly, with no title heuristics::

    genereviews[book]     ~960 chapters   (expert-authored, peer-reviewed,
                                            Mendelian disease; updated on a
                                            rolling schedule)
    statpearls[book]      ~9,600 chapters (point-of-care summaries across all
                                            of clinical medicine; lighter
                                            editorial process)

This script asks PubMed for the full PMID list of each collection and then
``esummary`` for the title, Bookshelf accession (``NBK…``) and publication date
of every record, and writes them as sorted CSV files:

    cache/bookshelf/genereviews.csv
    cache/bookshelf/statpearls.csv
    cache/bookshelf/MANIFEST.yaml      snapshot date and per-source counts

Why commit it
-------------
``scripts/check_genereviews_baseline.py`` matches disorder entry names against
these titles. With the index committed, that check is a pure-offline string
comparison, so it runs inside the automated PR reviewer -- whose sandbox
permits ``just`` and ``uv run`` but blocks ``curl`` and web fetches (PR #11592
is the review that could not verify a "no GeneReviews chapter exists" claim for
that reason, twice). The same file also lets ``scripts/tag_references.py``
decide *deterministically* whether a cited PMID is a GeneReviews or StatPearls
chapter, instead of grepping the cached abstract for the word "GeneReviews"
(which also matches a journal article that merely cites one).

Staleness is reported, not gated: a chapter published after the snapshot is
missed until the next refresh, and ``check_genereviews_baseline.py --online``
exists for that case. Refresh with ``just refresh-bookshelf-index``; the diff
is reviewable (rows are sorted by PMID, and the file carries no per-row
timestamps, so an unchanged chapter is an unchanged line).

Rate limits: NCBI allows 3 requests/s without a key and 10/s with
``NCBI_API_KEY`` set. Both esearch and esummary are throttled accordingly and a
429 is retried with backoff. A full rebuild is roughly 30 requests.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_DIR = REPO_ROOT / "cache" / "bookshelf"
MANIFEST_NAME = "MANIFEST.yaml"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
USER_AGENT = "dismech-bookshelf-index (https://github.com/monarch-initiative/dismech)"

#: Bookshelf collections indexed here. The key is the PubMed ``[book]`` value
#: and the CSV stem; the value is the ``booktitle`` esummary reports, which the
#: builder asserts against so a query that ever started returning something
#: else is noticed rather than silently indexed.
SOURCES: dict[str, str] = {
    "genereviews": "GeneReviews(®)",
    "statpearls": "StatPearls",
}

#: GeneReviews keeps withdrawn chapters on PubMed with this suffix on the
#: title. They are indexed (a curator may cite one) but flagged so the
#: baseline check does not call an untagged retired chapter a blocking gap.
RETIRED_MARKER = "RETIRED CHAPTER"

FIELDNAMES = ["pmid", "nbk", "retired", "pubdate", "title"]

ESUMMARY_BATCH = 400


class NcbiClient:
    """Minimal throttled E-utilities client (POST, JSON, retry on 429)."""

    def __init__(self, api_key: str | None = None, *, sleep: float | None = None):
        self.api_key = api_key
        # 10 req/s with a key, 3 without; stay under both with margin.
        self.sleep = sleep if sleep is not None else (0.12 if api_key else 0.4)

    def call(self, endpoint: str, **params: str) -> dict:
        params = {"retmode": "json", **params}
        if self.api_key:
            params["api_key"] = self.api_key
        data = urllib.parse.urlencode(params).encode()
        last_error: Exception | None = None
        for attempt in range(6):
            request = urllib.request.Request(
                EUTILS + endpoint, data=data, headers={"User-Agent": USER_AGENT}
            )
            try:
                with urllib.request.urlopen(request, timeout=90) as response:
                    payload = json.load(response)
                time.sleep(self.sleep)
                return payload
            except urllib.error.HTTPError as exc:
                last_error = exc
                if exc.code == 429 or exc.code >= 500:
                    time.sleep(2.0 * (attempt + 1))
                    continue
                raise
        raise RuntimeError(f"NCBI {endpoint} kept failing: {last_error}")


def esearch_book_pmids(client: NcbiClient, source: str) -> list[str]:
    """Every PMID in the ``<source>[book]`` collection, in PubMed order."""
    result = client.call(
        "esearch.fcgi", db="pubmed", term=f"{source}[book]", retmax="10000"
    )["esearchresult"]
    ids = list(result.get("idlist", []))
    count = int(result.get("count", len(ids)))
    if count > len(ids):
        raise RuntimeError(
            f"{source}[book] has {count} records but esearch returned {len(ids)}; "
            "the 10,000 retmax ceiling has been reached -- page the query."
        )
    return ids


def esummary_rows(
    client: NcbiClient, pmids: list[str], expected_booktitle: str
) -> list[dict]:
    rows: list[dict] = []
    for start in range(0, len(pmids), ESUMMARY_BATCH):
        batch = pmids[start : start + ESUMMARY_BATCH]
        result = client.call("esummary.fcgi", db="pubmed", id=",".join(batch))["result"]
        for uid in result.get("uids", []):
            record = result[uid]
            booktitle = record.get("booktitle", "")
            if booktitle != expected_booktitle:
                raise RuntimeError(
                    f"PMID:{uid} reports booktitle {booktitle!r}, expected "
                    f"{expected_booktitle!r}; refusing to index it."
                )
            accessions = [
                a["value"]
                for a in record.get("articleids", [])
                if a.get("idtype") == "bookaccession"
            ]
            title = record.get("title", "").strip()
            rows.append(
                {
                    "pmid": uid,
                    "nbk": accessions[0] if accessions else "",
                    "retired": "1" if RETIRED_MARKER in title.upper() else "0",
                    "pubdate": record.get("pubdate", "").strip(),
                    "title": title,
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    rows = sorted(rows, key=lambda r: int(r["pmid"]))
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(path: Path, counts: dict[str, int], snapshot_date: str) -> None:
    lines = [
        "# Generated by scripts/build_bookshelf_index.py -- do not hand-edit.",
        "# Refresh with `just refresh-bookshelf-index`.",
        f"snapshot_date: '{snapshot_date}'",
        "source: PubMed E-utilities (esearch `<name>[book]` + esummary)",
        "collections:",
    ]
    for source, booktitle in SOURCES.items():
        lines += [
            f"  {source}:",
            f"    file: {source}.csv",
            f"    query: '{source}[book]'",
            f"    booktitle: '{booktitle}'",
            f"    records: {counts[source]}",
        ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build(index_dir: Path, *, sources: list[str], client: NcbiClient) -> dict[str, int]:
    index_dir.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = {}
    for source in sources:
        pmids = esearch_book_pmids(client, source)
        rows = esummary_rows(client, pmids, SOURCES[source])
        if len(rows) != len(pmids):
            raise RuntimeError(
                f"{source}: esearch gave {len(pmids)} ids, esummary {len(rows)} records"
            )
        write_csv(index_dir / f"{source}.csv", rows)
        counts[source] = len(rows)
        print(
            f"{source}: {len(rows)} chapters -> {index_dir / (source + '.csv')}",
            file=sys.stderr,
        )
    return counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--index-dir", type=Path, default=INDEX_DIR)
    parser.add_argument(
        "--source",
        action="append",
        choices=sorted(SOURCES),
        help="rebuild only this collection (repeatable; default: all)",
    )
    args = parser.parse_args(argv)

    sources = args.source or list(SOURCES)
    client = NcbiClient(os.environ.get("NCBI_API_KEY"))
    counts = build(args.index_dir, sources=sources, client=client)

    manifest = args.index_dir / MANIFEST_NAME
    # A partial rebuild (--source) recounts the untouched collections from disk
    # so the manifest always describes the files beside it.
    for source in SOURCES:
        if source not in counts:
            csv_path = args.index_dir / f"{source}.csv"
            counts[source] = (
                sum(1 for _ in csv_path.open(encoding="utf-8")) - 1
                if csv_path.exists()
                else 0
            )
    write_manifest(manifest, counts, _dt.date.today().isoformat())
    print(f"manifest -> {manifest}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
