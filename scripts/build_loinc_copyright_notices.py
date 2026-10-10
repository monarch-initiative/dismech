"""Extract LOINC's third-party copyright notices into cache/loinc/.

LOINC records, for codes that identify an instrument owned by a third party
(PHQ-9, MoCA, the Barthel Index ...), that owner's copyright notice in the
EXTERNAL_COPYRIGHT_NOTICE field. LOINC's terms of use require the notice to
travel with the code. The Monarch KG, which dismech validates LOINC labels
against, does not carry the field; the Tuva Project's public LOINC table does.

This script downloads the table pinned in data/loinc/MANIFEST.yaml, verifies its
sha256, and writes two normalised files:

  cache/loinc/external_copyright_notices.csv  notice_id,notice
  cache/loinc/external_copyright_codes.csv    curie,notice_id

Only codes that carry a notice are written; a code absent from the codes file
has none. notice_id is a short hash of the notice text, so ids are stable across
rebuilds unless a notice's wording changes.

Usage:
  uv run python scripts/build_loinc_copyright_notices.py           # verify pin, rebuild
  uv run python scripts/build_loinc_copyright_notices.py --repin   # accept a new download
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import sys
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "data" / "loinc" / "MANIFEST.yaml"
DOWNLOAD = ROOT / "data" / "loinc" / "terminology__loinc.csv.gz"
CACHE_DIR = ROOT / "cache" / "loinc"
NOTICES = CACHE_DIR / "external_copyright_notices.csv"
CODES = CACHE_DIR / "external_copyright_codes.csv"


def notice_id(text: str) -> str:
    return "N" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:10]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--repin", action="store_true", help="accept the downloaded file and rewrite the manifest pin")
    args = parser.parse_args()

    manifest = yaml.safe_load(MANIFEST.read_text())
    DOWNLOAD.parent.mkdir(parents=True, exist_ok=True)
    if not DOWNLOAD.exists() or args.repin:
        with urllib.request.urlopen(manifest["url"]) as resp:
            DOWNLOAD.write_bytes(resp.read())
    digest = hashlib.sha256(DOWNLOAD.read_bytes()).hexdigest()

    if digest != manifest["sha256"]:
        if not args.repin:
            print(
                f"sha256 mismatch for {DOWNLOAD.name}: pinned {manifest['sha256']}, got {digest}.\n"
                "The source changed. Re-run with --repin to accept it, then review both diffs.",
                file=sys.stderr,
            )
            return 1
        text = MANIFEST.read_text()
        text = text.replace(manifest["sha256"], digest).replace(
            f'snapshot_date: "{manifest["snapshot_date"]}"', f'snapshot_date: "{datetime.now(UTC).date().isoformat()}"'
        )
        MANIFEST.write_text(text)
        print(f"repinned {MANIFEST.relative_to(ROOT)} to {digest}")

    reader = csv.reader(io.TextIOWrapper(gzip.open(DOWNLOAD), encoding="utf-8"))
    header = next(reader)
    code_col = header.index("loinc")
    notice_col = header.index("external_copyright_notice")

    notices: dict[str, str] = {}
    codes: list[tuple[str, str]] = []
    for row in reader:
        text = " ".join(row[notice_col].split())
        if not text:
            continue
        nid = notice_id(text)
        notices[nid] = text
        codes.append((f"LOINC:{row[code_col]}", nid))

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with NOTICES.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["notice_id", "notice"])
        w.writerows(sorted(notices.items()))
    with CODES.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["curie", "notice_id"])
        w.writerows(sorted(codes))
    print(f"{len(codes)} codes carry one of {len(notices)} distinct notices")
    return 0


if __name__ == "__main__":
    sys.exit(main())
