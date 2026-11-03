#!/usr/bin/env python3
"""Re-run the PubMed per-term counts behind the NAMs search vocabulary (issue #14428).

OpenScientist job ``e7bed1f0-eb28-4981-aace-6559505b2ad0`` reported a table of
PubMed title/abstract counts for 22 NAM search terms (finding F4 of its
``final_report.md``, queried 2026-10-15). This script re-runs each of those
queries exactly as the job ran them, recorded in the job's
``provenance/iter4_transcript.json``, and puts the current count beside the
reported one. It also counts the terms added for the NAMs landscape analysis,
which have no reported count.

The table's labels do not always describe the query that was run. A ``*`` in a
label does not always mean PubMed truncation (``digital twin*`` was run as the
singular and plural phrases), and two queries include an abbreviation with
other meanings (``AOP``, ``IATA``). The ``note`` column records each such case;
the queries themselves are left as the job ran them, so the counts stay
comparable.

Usage::

    uv run python scripts/nams_term_counts.py
    uv run python scripts/nams_term_counts.py --out docs/reports/data/nams-term-counts-2026-10-19.tsv

An NCBI API key (``NCBI_API_KEY``) raises the E-utilities rate limit from 3 to
10 requests per second and is picked up automatically if set.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import logging
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import httpx

log = logging.getLogger("nams_term_counts")

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
JOB_ID = "e7bed1f0-eb28-4981-aace-6559505b2ad0"
MAX_RETRIES = 4

COLUMNS = [
    "label",
    "query",
    "reported_count",
    "current_count",
    "change",
    "percent_change",
    "source",
    "note",
    "queried_on",
]


@dataclass(frozen=True)
class Term:
    label: str
    query: str
    reported_count: int | None
    source: str
    note: str = ""


REPORT = f"OpenScientist {JOB_ID}, final_report.md F4"
ADDED = "Added for #14428"

TERMS: list[Term] = [
    Term("in silico", '"in silico"[tiab]', 107016, REPORT),
    Term(
        "iPSC / hiPSC",
        '"induced pluripotent stem cell"[tiab] OR "induced pluripotent stem cells"[tiab] '
        "OR iPSC[tiab] OR hiPSC[tiab]",
        34747,
        REPORT,
        "Also matches the spelled-out phrase.",
    ),
    Term("organoid*", "organoid*[tiab]", 27714, REPORT),
    Term("spheroid*", "spheroid*[tiab]", 26598, REPORT),
    Term(
        "high-throughput screening",
        '"high-throughput screening"[tiab] OR "high throughput screening"[tiab]',
        24698,
        REPORT,
    ),
    Term(
        "QSAR",
        'QSAR[tiab] OR "quantitative structure-activity relationship"[tiab]',
        16013,
        REPORT,
    ),
    Term(
        "3D bioprint*",
        '"3D bioprinting"[tiab] OR bioprinted[tiab] OR bioprinting[tiab]',
        8150,
        REPORT,
        "No truncation, and bioprinting/bioprinted do not require 3D.",
    ),
    Term(
        "PBPK / PBK",
        'PBPK[tiab] OR PBK[tiab] OR "physiologically based pharmacokinetic"[tiab] '
        'OR "physiologically based kinetic"[tiab]',
        7401,
        REPORT,
    ),
    Term(
        "adverse outcome pathway*",
        '"adverse outcome pathway"[tiab] OR "adverse outcome pathways"[tiab] OR AOP[tiab]',
        4709,
        REPORT,
        "No truncation. AOP[tiab] has other meanings, so the count may include unrelated records.",
    ),
    Term(
        "digital twin*",
        '"digital twin"[tiab] OR "digital twins"[tiab]',
        4137,
        REPORT,
        "No truncation: singular and plural phrases only.",
    ),
    Term(
        "organ-on-chip*",
        '"organ-on-a-chip"[tiab] OR "organ-on-chip"[tiab] OR "organ on a chip"[tiab] '
        'OR "organs-on-chips"[tiab]',
        3736,
        REPORT,
        "No truncation: four spelled-out phrases.",
    ),
    Term(
        "virtual patient / cohort",
        '"virtual patient"[tiab] OR "virtual patients"[tiab] OR "virtual cohort"[tiab]',
        2688,
        REPORT,
        'Does not include the plural "virtual cohorts".',
    ),
    Term(
        "microphysiological system*",
        '"microphysiological system"[tiab] OR "microphysiological systems"[tiab]',
        1604,
        REPORT,
        "No truncation: singular and plural phrases only.",
    ),
    Term("read-across", '"read-across"[tiab] OR "read across"[tiab]', 1049, REPORT),
    Term("ToxCast / Tox21", "ToxCast[tiab] OR Tox21[tiab]", 855, REPORT),
    Term(
        "IVIVE / QIVIVE",
        'IVIVE[tiab] OR QIVIVE[tiab] OR "in vitro to in vivo extrapolation"[tiab]',
        816,
        REPORT,
    ),
    Term(
        "alternatives to animal testing",
        '"alternatives to animal testing"[tiab] OR "alternative to animal testing"[tiab]',
        517,
        REPORT,
    ),
    Term(
        "tissue chip*",
        '"tissue chip"[tiab] OR "tissue chips"[tiab]',
        380,
        REPORT,
        "No truncation: singular and plural phrases only.",
    ),
    Term(
        "HTTr",
        '"high-throughput transcriptomics"[tiab] OR "high throughput transcriptomics"[tiab] OR HTTr[tiab]',
        272,
        REPORT,
    ),
    Term(
        "in silico clinical trial*",
        '"in silico clinical trial"[tiab] OR "in silico clinical trials"[tiab] OR "in silico trial"[tiab]',
        262,
        REPORT,
        'No truncation. Does not include the plural "in silico trials".',
    ),
    Term(
        "IATA",
        'IATA[tiab] OR "integrated approaches to testing and assessment"[tiab]',
        246,
        REPORT,
        "IATA[tiab] also matches the International Air Transport Association.",
    ),
    Term("FDA Modernization Act", '"FDA Modernization Act"[tiab]', 136, REPORT),
    Term("in vitro", '"in vitro"[tiab]', None, ADDED),
    Term("complex in vitro", '"complex in vitro"[tiab]', None, ADDED),
    Term("precision medicine", '"precision medicine"[tiab]', None, ADDED),
    Term(
        "patient-specific",
        '"patient-specific"[tiab] OR "patient specific"[tiab]',
        None,
        ADDED,
    ),
    Term(
        "real-world evidence",
        '"real-world evidence"[tiab] OR "real world evidence"[tiab]',
        None,
        ADDED,
        "Evidence only. The report's 34,290 (F6) combined real-world data and evidence.",
    ),
]


def _api_params() -> dict[str, str]:
    params = {"tool": "dismech-nams-term-counts", "email": "dismech-audit@example.com"}
    key = os.environ.get("NCBI_API_KEY")
    if key:
        params["api_key"] = key
    return params


def _pause() -> float:
    return 0.11 if os.environ.get("NCBI_API_KEY") else 0.34


def pubmed_count(client: httpx.Client, query: str) -> int:
    """Return PubMed's record count for ``query``, retrying transient failures."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": "0",
        **_api_params(),
    }
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        if attempt:
            time.sleep(2**attempt)
        log.debug("query (attempt %d): %s", attempt + 1, query)
        try:
            response = client.get(ESEARCH_URL, params=params)
            if response.status_code == 429 or response.status_code >= 500:
                last_error = RuntimeError(f"HTTP {response.status_code}")
                log.debug("  HTTP %d, will retry", response.status_code)
                continue
            response.raise_for_status()
            result = response.json()["esearchresult"]
            if "ERROR" in result:
                raise RuntimeError(f"PubMed rejected {query!r}: {result['ERROR']}")
            count = int(result["count"])
            log.debug("  count: %d", count)
            # How PubMed actually read the query, e.g. what a * expanded to.
            log.debug("  PubMed read it as: %s", result.get("querytranslation", "?"))
            return count
        except (httpx.TransportError, ValueError, KeyError) as error:
            last_error = error
            log.debug("  failed: %r, will retry", error)
    raise RuntimeError(
        f"could not count {query!r} after {MAX_RETRIES + 1} attempts: {last_error}"
    )


def build_rows(
    terms: list[Term], counts: list[int], queried_on: str
) -> list[dict[str, str]]:
    rows = []
    for term, count in zip(terms, counts, strict=True):
        if term.reported_count is None:
            change = percent = ""
        else:
            change = f"{count - term.reported_count:+d}"
            percent = (
                f"{(count - term.reported_count) / term.reported_count * 100:+.1f}"
            )
        rows.append(
            {
                "label": term.label,
                "query": term.query,
                "reported_count": ""
                if term.reported_count is None
                else str(term.reported_count),
                "current_count": str(count),
                "change": change,
                "percent_change": percent,
                "source": term.source,
                "note": term.note,
                "queried_on": queried_on,
            }
        )
    return rows


def print_summary(rows: list[dict[str, str]]) -> None:
    width = max(len(row["label"]) for row in rows)
    print(
        f"{'term':<{width}}  {'reported':>9}  {'current':>9}  {'change':>8}  {'%':>6}"
    )
    for row in rows:
        reported = f"{int(row['reported_count']):,}" if row["reported_count"] else "-"
        print(
            f"{row['label']:<{width}}  {reported:>9}  {int(row['current_count']):>9,}  "
            f"{row['change'] or '-':>8}  {row['percent_change'] or '-':>6}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--out", type=Path, help="Write the full table (with queries and notes) as TSV."
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print each query sent to PubMed and the count it returned (to stderr).",
    )
    args = parser.parse_args(argv)
    # Only this script's logger goes to DEBUG: httpx's own debug output is noisy
    # and its request URLs would include NCBI_API_KEY.
    logging.basicConfig(level=logging.WARNING, format="%(message)s")
    log.setLevel(logging.DEBUG if args.debug else logging.WARNING)

    queried_on = datetime.datetime.now(datetime.UTC).date().isoformat()
    counts = []
    with httpx.Client(timeout=45.0) as client:
        for index, term in enumerate(TERMS):
            if index:
                time.sleep(_pause())
            log.debug("[%d/%d] %s", index + 1, len(TERMS), term.label)
            counts.append(pubmed_count(client, term.query))

    rows = build_rows(TERMS, counts, queried_on)
    print_summary(rows)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as handle:
            writer = csv.DictWriter(
                handle, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nWrote {len(rows)} rows to {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
