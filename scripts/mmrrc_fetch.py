#!/usr/bin/env python3
"""Fetch MMRRC holdings from IMSR and MGI's mouse-to-HGNC report into data/mmrrc/.

IMSR (the International Mouse Strain Resource, findmice.org) lists every MMRRC
holding with its MGI allele and marker IDs. Its summary page loads results from
``report.json``; we page through that endpoint filtered to repository MMRRC.
Pages are large (2-40 MB of HTML-in-JSON), so each one is validated and re-fetched
if truncated. Existing valid pages are kept, so an interrupted run resumes.

Raw files are gitignored. ``scripts/mmrrc_join.py`` reads them.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

IMSR = "https://www.findmice.org/report.json"
HOMOLOGY = "https://www.informatics.jax.org/downloads/reports/HGNC_AllianceHomology.rpt"
PAGE = 1000


def get(url: str, timeout: int = 600) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "dismech-mmrrc-join"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def valid(path: Path) -> bool:
    try:
        json.loads(path.read_bytes())["report"]["summaryRows"]
        return True
    except Exception:
        return False


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default="data/mmrrc", type=Path)
    ap.add_argument("--delay", default=1.0, type=float, help="seconds between requests")
    args = ap.parse_args(argv)

    pages = args.out / "imsr"
    pages.mkdir(parents=True, exist_ok=True)
    total = json.loads(get(f"{IMSR}?repositories=MMRRC&results=1&startIndex=0"))["report"]["totalCount"]
    print(f"IMSR reports {total} MMRRC holdings", file=sys.stderr)

    for start in range(0, total, PAGE):
        path = pages / f"p{start}.json"
        for attempt in range(3):
            if path.exists() and valid(path):
                break
            url = (f"{IMSR}?repositories=MMRRC&results={PAGE}&startIndex={start}"
                   "&sort=nameFormatter&dir=asc")
            try:
                path.write_bytes(get(url))
            except Exception as exc:  # network hiccup: retry
                print(f"  {path.name}: {exc}", file=sys.stderr)
            time.sleep(args.delay * (attempt + 1))
        else:
            sys.exit(f"could not fetch a complete {path.name}")
        print(f"  {path.name} ok", file=sys.stderr)

    (args.out / "HGNC_AllianceHomology.rpt").write_bytes(get(HOMOLOGY))
    (args.out / "FETCHED").write_text(time.strftime("%Y-%m-%dT%H:%M:%SZ\n", time.gmtime()))
    print("done", file=sys.stderr)


if __name__ == "__main__":
    main()
