"""Split dating.tsv into dev and test sets by test_group.

Groups are sorted by name, shuffled with random.Random(SEED), then taken in
that order into the dev set until it holds at least DEV_CASES cases; every
remaining group goes to the test set. Cases sharing a test_group always land
in the same set, so the dev set can exceed DEV_CASES when the last group
taken has more than one case. Outputs list case_ids, one per line, in
case_id order.
"""
import csv
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261111
DEV_CASES = 5

rows = list(csv.DictReader(open(HERE / "dating.tsv", newline="", encoding="utf-8"), delimiter="\t"))
groups: dict[str, list[str]] = {}
for r in rows:
    groups.setdefault(r["test_group"], []).append(r["case_id"])
order = sorted(groups)
random.Random(SEED).shuffle(order)

dev, test = [], []
for g in order:
    (dev if len(dev) < DEV_CASES else test).extend(groups[g])
for name, ids in (("dev_set.txt", dev), ("test_set.txt", test)):
    (HERE / name).write_text("".join(f"{i}\n" for i in sorted(ids)), encoding="utf-8")
print(f"groups={len(order)} dev={len(dev)} test={len(test)}")
print("dev groups:", [g for g in order if groups[g][0] in dev])
