"""Split dating.tsv into dev, test and pending case lists.

Only cases with a verified cutoff (literature_check.tsv lit_ruling PASS) are
split. Cases whose cutoff is still unverified (UNVERIFIED_CUTOFF) go to
pending_cases.txt; each joins the test set once its cutoff is verified.

Dev set, one case per test_class:
  - A candidate is a verified case that is the only case of its test_group
    among all cases in dating.tsv (verified and pending). So no dev case
    shares a test with any test or pending case, and the dev set holds one
    case per group by construction.
  - A class contributes a dev case only if, after removing it, the class
    still has at least one verified case for the test set. This spans as
    many classes as the verified cases allow without emptying a class from
    the test set.
  - Classes are visited in sorted order; within a class one candidate is
    drawn with random.Random(SEED).choice over the case_ids sorted.

Test set: every other verified case.

Outputs list case_ids, one per line, in case_id order.
"""
import csv
import random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261111


def main() -> None:
    rows = list(csv.DictReader(open(HERE / "dating.tsv", newline="", encoding="utf-8"), delimiter="\t"))
    ruling = {r["case_id"]: r["lit_ruling"]
              for r in csv.DictReader(open(HERE / "literature_check.tsv", newline="", encoding="utf-8"),
                                      delimiter="\t")}
    verified = [r for r in rows if ruling[r["case_id"]] == "PASS"]
    pending = [r for r in rows if ruling[r["case_id"]] == "UNVERIFIED_CUTOFF"]
    if len(verified) + len(pending) != len(rows):
        raise SystemExit("dating.tsv holds a case that is neither PASS nor UNVERIFIED_CUTOFF")

    group_size = defaultdict(int)
    for r in rows:
        group_size[r["test_group"]] += 1
    by_class = defaultdict(list)
    for r in verified:
        by_class[r["test_class"]].append(r)

    rng = random.Random(SEED)
    dev = []
    for cls in sorted(by_class):
        candidates = sorted(r["case_id"] for r in by_class[cls] if group_size[r["test_group"]] == 1)
        if not candidates or len(by_class[cls]) < 2:
            continue
        dev.append(rng.choice(candidates))
    test = [r["case_id"] for r in verified if r["case_id"] not in dev]

    for name, ids in (("dev_set.txt", dev), ("test_set.txt", test),
                      ("pending_cases.txt", [r["case_id"] for r in pending])):
        (HERE / name).write_text("".join(f"{i}\n" for i in sorted(ids)), encoding="utf-8")

    cls_of = {r["case_id"]: r for r in rows}
    print(f"verified={len(verified)} dev={len(dev)} test={len(test)} pending={len(pending)}")
    for i in sorted(dev):
        print(f"  {i}  {cls_of[i]['test_class']:<17} {cls_of[i]['test_group']}  ({cls_of[i]['disease']})")


if __name__ == "__main__":
    main()
