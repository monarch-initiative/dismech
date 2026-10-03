#!/usr/bin/env python3
"""Reduce the VAMR assay's supplementary tables to one row per fit.

Spath et al. 2026 (doi:10.1016/j.neuro.2026.103414) report a concentration-
response fit for each of 17 chemicals on each of 26 behavioural endpoints, in
each of two exposure arms. Those fits live in supplementary tables S3 (acute)
and S4 (developmental) of the publisher's workbook, which carries ~40 columns
of `tcplfit2` output per row.

This script keeps the columns needed to read a hit off a row, and adds the
verdict under the hit rule the paper states: a hit call of at least 0.9 and
fewer than two curve-fit flags.

The workbook is not committed -- it is a publisher asset, and the article is
CC BY but the supplement's terms are not stated -- so the script downloads it.
Its output is `docs/reports/data/vamr-endpoint-hit-calls-2026-10-03.tsv`,
which is committed, and `--check` verifies the committed file still matches.

    uv run python scripts/vamr_endpoint_hit_calls.py --check
    uv run python scripts/vamr_endpoint_hit_calls.py --out path/to.tsv
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
import urllib.request
from pathlib import Path

WORKBOOK_URL = (
    "https://ars.els-cdn.com/content/image/1-s2.0-S0161813X26000355-mmc3.xlsx"
)

DEFAULT_OUT = Path("docs/reports/data/vamr-endpoint-hit-calls-2026-10-03.tsv")

# Sheet name -> the value written to the `exposure` column.
SHEETS = {
    "S3_AC50_VAMR_acute": "acute",
    "S4_AC50_VAMR_dev": "developmental",
}

# The workbook spells the two ratio endpoints with underscores; the article and
# its figures use slashes.
ENDPOINT_RENAMES = {"ASH_1_5": "ASH1/5", "ASR_2_3": "ASR2/3"}

COLUMNS = [
    "chemical",
    "exposure",
    "endpoint",
    "hitcall",
    "ac50_uM",
    "acc_uM",
    "bmd_uM",
    "fit_method",
    "top_over_cutoff",
    "flags",
    "n_flags",
    "passes_hit_rule",
]

HITCALL_FLOOR = 0.9
MAX_FLAGS = 2


def _number(value: object) -> str:
    """Format a numeric cell, leaving blanks and the sheet's 'NA' empty."""
    if value in (None, "NA", ""):
        return ""
    return f"{float(value):.6g}"


def _flags(value: object) -> str:
    """The sheet writes no flags as an empty cell in S4 and as '-' in S3."""
    if value in (None, "-", ""):
        return ""
    return str(value)


def fetch_workbook(url: str = WORKBOOK_URL) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=300) as response:
        return response.read()


def build_rows(workbook_bytes: bytes) -> list[list[str]]:
    import openpyxl

    workbook = openpyxl.load_workbook(io.BytesIO(workbook_bytes), read_only=True)
    rows: list[list[str]] = []
    for sheet_name, exposure in SHEETS.items():
        sheet = list(workbook[sheet_name].iter_rows(values_only=True))
        header = list(sheet[0])
        for raw in sheet[1:]:
            record = dict(zip(header, raw))
            if not record.get("chemical"):
                continue
            flags = _flags(record.get("flag"))
            n_flags = len(flags.split(",")) if flags else 0
            try:
                hitcall = float(record["hitcall"])
            except (TypeError, ValueError):
                hitcall = float("nan")
            passes = hitcall >= HITCALL_FLOOR and n_flags < MAX_FLAGS
            endpoint = str(record["endpoint"])
            rows.append(
                [
                    str(record["chemical"]).strip(),
                    exposure,
                    ENDPOINT_RENAMES.get(endpoint, endpoint),
                    f"{hitcall:.4f}",
                    _number(record.get("ac50")),
                    _number(record.get("acc")),
                    _number(record.get("bmd")),
                    str(record.get("fit_method") or ""),
                    _number(record.get("top_over_cutoff")),
                    flags,
                    str(n_flags),
                    "yes" if passes else "no",
                ]
            )
    return rows


def render(rows: list[list[str]]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")
    writer.writerow(COLUMNS)
    writer.writerows(rows)
    return buffer.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare against the committed file instead of writing it.",
    )
    parser.add_argument("--workbook", type=Path, help="Use a local copy of mmc3.xlsx.")
    args = parser.parse_args(argv)

    if args.workbook:
        workbook_bytes = args.workbook.read_bytes()
    else:
        print(f"Downloading {WORKBOOK_URL}", file=sys.stderr)
        workbook_bytes = fetch_workbook()

    text = render(build_rows(workbook_bytes))

    if args.check:
        if not args.out.exists():
            print(f"MISSING: {args.out}", file=sys.stderr)
            return 1
        if args.out.read_text() != text:
            print(f"DRIFT: {args.out} does not match the workbook", file=sys.stderr)
            return 1
        print(f"OK: {args.out} matches the workbook")
        return 0

    args.out.write_text(text)
    print(f"Wrote {args.out} ({len(text.splitlines()) - 1} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
