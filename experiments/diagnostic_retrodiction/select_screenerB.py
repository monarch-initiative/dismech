"""Select the rows for the second, blinded eligibility screener (screener B).

Selection, from the frame rows with flag_nongenetic_specimen TRUE:
  - every flagged row whose disease_name has at least one INCLUDE row in
    eligibility.tsv, and
  - a random sample of 300 of the remaining flagged rows (seed 20261112).

screenerB_input.tsv carries only frame.tsv's own columns, so no decision,
reason, specimen check or review flag reaches screener B. Rows are shuffled
(same seed) so the two selection groups are not ordered apart. A row is
identified by (disease_name, row_type, row_name), which is unique among flagged
rows, for joining screener B's answers back to eligibility.tsv.

The selection still differs between the groups in shape: diseases in the first
group contribute all their flagged rows, while the sample is mostly one row
per disease. A screener who notices that can infer which group a row is from.

Usage:
    python experiments/diagnostic_retrodiction/select_screenerB.py
"""
from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261112
N_OTHER = 300


def main() -> None:
    with open(HERE / "frame.tsv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = list(reader.fieldnames or [])
        flagged = [r for r in reader if r["flag_nongenetic_specimen"] == "TRUE"]
    keys = [(r["disease_name"], r["row_type"], r["row_name"]) for r in flagged]
    if len(set(keys)) != len(keys):
        sys.exit("flagged rows are not unique on (disease_name, row_type, row_name)")

    with open(HERE / "eligibility.tsv", newline="", encoding="utf-8") as f:
        include_diseases = {r["disease"] for r in csv.DictReader(f, delimiter="\t")
                            if r["decision"] == "INCLUDE"}
    missing = include_diseases - {r["disease_name"] for r in flagged}
    if missing:
        sys.exit(f"INCLUDE diseases not among flagged frame rows: {sorted(missing)}")

    group_a = [r for r in flagged if r["disease_name"] in include_diseases]
    others = [r for r in flagged if r["disease_name"] not in include_diseases]
    rng = random.Random(SEED)
    group_b = rng.sample(others, N_OTHER)
    selected = group_a + group_b
    rng.shuffle(selected)

    with open(HERE / "screenerB_input.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(selected)
    print(f"INCLUDE diseases: {len(include_diseases)}; their flagged rows: {len(group_a)}; "
          f"sampled other rows: {len(group_b)}; total: {len(selected)}")


if __name__ == "__main__":
    main()
