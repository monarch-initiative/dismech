"""Select the rows for the second, blinded eligibility screener (screener B).

Selection, from the frame rows with flag_nongenetic_specimen TRUE:
  - every flagged row whose disease_name has at least one INCLUDE row in
    eligibility.tsv, and
  - a comparison group sampled by whole disease: diseases with no INCLUDE row
    are taken in random order (seed 20261112), each contributing all of its
    flagged rows, until the group has at least 300 rows.

screenerB_input.tsv carries only frame.tsv's own columns, so no decision,
reason, specimen check or review flag reaches screener B. Rows are shuffled
(same seed) so the two selection groups are not ordered apart. A row is
identified by (disease_name, row_type, row_name), which is unique among flagged
rows, for joining screener B's answers back to eligibility.tsv.

Both groups are made of complete diseases, so a disease never appears with only
some of its rows. The groups can still differ in their distribution of rows
per disease; the script prints both so that can be checked.

Usage:
    python experiments/diagnostic_retrodiction/select_screenerB.py
"""
from __future__ import annotations

import csv
import random
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261112
MIN_COMPARISON_ROWS = 300


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
    by_disease: dict[str, list[dict]] = {}
    for r in others:
        by_disease.setdefault(r["disease_name"], []).append(r)
    candidates = list(by_disease)  # frame order, so the shuffle is reproducible
    rng = random.Random(SEED)
    rng.shuffle(candidates)
    group_b: list[dict] = []
    chosen: list[str] = []
    for d in candidates:
        if len(group_b) >= MIN_COMPARISON_ROWS:
            break
        chosen.append(d)
        group_b.extend(by_disease[d])
    selected = group_a + group_b
    rng.shuffle(selected)

    with open(HERE / "screenerB_input.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(selected)
    def dist(rows: list[dict]) -> str:
        per = Counter(Counter(r["disease_name"] for r in rows).values())
        return ", ".join(f"{k} row{'s' if k > 1 else ''}: {v}" for k, v in sorted(per.items()))

    print(f"INCLUDE group: {len(include_diseases)} diseases, {len(group_a)} rows ({dist(group_a)})")
    print(f"comparison group: {len(chosen)} diseases, {len(group_b)} rows ({dist(group_b)})")
    print(f"total: {len(selected)} rows")


if __name__ == "__main__":
    main()
