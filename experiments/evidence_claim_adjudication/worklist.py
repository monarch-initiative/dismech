"""Print one assertion of a run's frame, with its pairs, for the judge (README.md, "Who judges").

Reads only ``judge_sheet.csv`` and ``assertion_sheet.csv`` in the run folder. It never opens
``fenced_sheet.csv``, the sealed folder or any other file that carries a checker label, so it
is safe to run in the judging session. Below an assertion's own pairs it lists the quotes on
the rows nested in it, which is the same context the second reader's sheet gives.

Usage:

    python experiments/evidence_claim_adjudication/worklist.py --run <run folder> --list
    python experiments/evidence_claim_adjudication/worklist.py --run <run folder> --list --batch 1
    python experiments/evidence_claim_adjudication/worklist.py --run <run folder> /pathophysiology/0
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

PAIR_FIELDS = [
    "reference",
    "reference_title",
    "evidence_source",
    "quote_role",
    "directness",
    "supports",
]


def read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--run", required=True, type=Path, help="the run folder")
    parser.add_argument(
        "--list", action="store_true", help="list assertions in entry order"
    )
    parser.add_argument(
        "--batch", type=int, help="with --list, only this judging batch"
    )
    parser.add_argument(
        "assertion_path", nargs="?", help="for example /pathophysiology/0"
    )
    args = parser.parse_args()

    assertions = read(args.run / "assertion_sheet.csv")
    pairs = read(args.run / "judge_sheet.csv")

    if args.list:
        for row in assertions:
            if args.batch and int(row["batch"]) != args.batch:
                continue
            print(
                f"batch {row['batch']}  {row['pairs']:>2} pairs  {row['assertion_path']}"
            )
        return 0
    if not args.assertion_path:
        parser.error("give an assertion path, or --list")

    found = [row for row in assertions if row["assertion_path"] == args.assertion_path]
    if not found:
        print(f"{args.assertion_path} is not in this run's frame.")
        return 1
    row = found[0]
    print(
        f"{row['assertion_path']}  ({row['assertion_type']}, batch {row['batch']}, {row['pairs']} pairs)"
    )
    print()
    print(row["claim"])
    for pair in (p for p in pairs if p["assertion_path"] == args.assertion_path):
        print()
        print(f"--- {pair['key']}")
        for field in PAIR_FIELDS:
            if pair.get(field):
                print(f"{field}: {pair[field]}")
        print(f"quote: {pair['quote']}")
        if pair.get("explanation"):
            print(f"explanation: {pair['explanation']}")
    nested = [
        p for p in pairs if p["assertion_path"].startswith(args.assertion_path + "/")
    ]
    if nested:
        print()
        print("Quotes on the rows nested in this one (each is judged on its own row):")
        for pair in nested:
            print(f"  {pair['evidence_path']} | {pair['reference']} | {pair['quote']}")
    if row["pairs"] == "0":
        print()
        print("This assertion has no quote at all.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
