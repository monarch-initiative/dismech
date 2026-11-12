"""Split dating.tsv into dev, test and pending case lists, with the dev set frozen.

The dev set is read from the committed dev_set.txt and is never redrawn. It was
drawn once (commit e76ffea9ec2, "alias fix, stratified split, draft README")
as one verified case per test_class, from cases that are the only case
of their test_group, with random.Random(20261111). Redrawing it after more
cases were verified would change which cases the protocol was developed on, so
this script now only checks it:

  - every dev case must still be in dating.tsv with a verified cutoff
    (literature_check.tsv lit_ruling PASS); otherwise the script fails;
  - every dev case must still be the only case of its test_group, so no test or
    pending case shares a test with a dev case; otherwise the script fails.

Test set: every other verified (PASS) case.
Pending: every case whose cutoff is still unverified (UNVERIFIED_CUTOFF); each
joins the test set once its cutoff is verified.

dev_set.txt is rewritten only if its sorted content would differ, which the
checks above rule out, so the file stays byte-identical.

Outputs list case_ids, one per line, in case_id order.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_tsv(name: str) -> list[dict]:
    with open(HERE / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    rows = read_tsv("dating.tsv")
    ruling = {r["case_id"]: r["lit_ruling"] for r in read_tsv("literature_check.tsv")}
    by_id = {r["case_id"]: r for r in rows}
    verified = [r for r in rows if ruling[r["case_id"]] == "PASS"]
    pending = [r for r in rows if ruling[r["case_id"]] == "UNVERIFIED_CUTOFF"]
    if len(verified) + len(pending) != len(rows):
        raise SystemExit("dating.tsv holds a case that is neither PASS nor UNVERIFIED_CUTOFF")

    dev_text = (HERE / "dev_set.txt").read_text(encoding="utf-8")
    dev = dev_text.split()
    group_size = Counter(r["test_group"] for r in rows)
    problems = []
    for cid in dev:
        if cid not in by_id:
            problems.append(f"{cid}: no longer in dating.tsv")
        elif ruling[cid] != "PASS":
            problems.append(f"{cid}: lit_ruling is {ruling[cid]}, not PASS")
        elif group_size[by_id[cid]["test_group"]] != 1:
            problems.append(f"{cid}: test_group {by_id[cid]['test_group']!r} now has other cases")
    if problems:
        raise SystemExit("frozen dev set is no longer valid:\n  " + "\n  ".join(problems))

    test = [r["case_id"] for r in verified if r["case_id"] not in dev]
    expected_dev = "".join(f"{i}\n" for i in sorted(dev))
    if expected_dev != dev_text:
        raise SystemExit("dev_set.txt is not in canonical form (sorted, one id per line)")
    for name, ids in (("test_set.txt", test), ("pending_cases.txt", [r["case_id"] for r in pending])):
        (HERE / name).write_text("".join(f"{i}\n" for i in sorted(ids)), encoding="utf-8")

    print(f"verified={len(verified)} dev={len(dev)} (frozen) test={len(test)} pending={len(pending)}")
    for i in sorted(dev):
        r = by_id[i]
        print(f"  {i}  {r['test_class']:<17} {r['test_group']}  ({r['disease']})")
    per = defaultdict(Counter)
    for r in rows:
        part = "dev" if r["case_id"] in dev else ("test" if ruling[r["case_id"]] == "PASS" else "pending")
        per[r["test_class"]][part] += 1
    for cls in sorted(per):
        c = per[cls]
        print(f"  {cls:<20} dev={c['dev']} test={c['test']} pending={c['pending']}")


if __name__ == "__main__":
    main()
