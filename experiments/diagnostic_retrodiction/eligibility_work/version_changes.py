"""List every row whose eligibility decision differs between two builds.

Compares a version 1 eligibility.tsv (default: the copy committed before
version 2) with the version 2 build (default: the commit that published it),
both read with ``git show``, and
writes ../eligibility_v2_changes.tsv with one row per changed decision:

  disease_name, row_type, row_name, v1_decision, v1_reason,
  v2_decision, v2_reason, rule

``rule`` is the version 2 rule named by the ``(v2 rule N)`` marker at the end of
the new reason. A changed decision with no marker is an error, because version
2 is only allowed to change decisions through rules 1-5. Frame rows are matched
by position (both files list the flagged frame rows in frame order, which
build_eligibility.py checks); the appended KB_GAP rows by disease and test.

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/version_changes.py \
        [--v1-ref <git ref>]   # default 638510c70fa, the commit that froze v1's tables
        [--v2-ref <git ref>]   # default 70c47e11be0, the version 2 build; later
                               # changes (the screener resolution) are not version 2
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
REPO = EXP.parents[1]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--v1-ref", default="638510c70fa")
    ap.add_argument("--v2-ref", default="70c47e11be0")
    a = ap.parse_args()
    rel = (EXP / "eligibility.tsv").relative_to(REPO).as_posix()
    v1_text = subprocess.run(["git", "show", f"{a.v1_ref}:{rel}"], cwd=REPO, check=True,
                             capture_output=True, text=True).stdout
    v1 = list(csv.DictReader(io.StringIO(v1_text), delimiter="\t"))
    v2_text = subprocess.run(["git", "show", f"{a.v2_ref}:{rel}"], cwd=REPO, check=True,
                             capture_output=True, text=True).stdout
    v2 = list(csv.DictReader(io.StringIO(v2_text), delimiter="\t"))
    with open(EXP / "frame.tsv", newline="", encoding="utf-8") as f:
        frame = [r for r in csv.DictReader(f, delimiter="\t") if r["flag_nongenetic_specimen"] == "TRUE"]
    if len(v1) != len(v2) or len(v1) < len(frame):
        sys.exit(f"row counts differ: v1 {len(v1)}, v2 {len(v2)}, flagged frame {len(frame)}")

    out = []
    for i, (o, n) in enumerate(zip(v1, v2)):
        if (o["disease"], o["test"]) != (n["disease"], n["test"]):
            sys.exit(f"row {i} does not line up between versions")
        if o["decision"] == n["decision"]:
            continue
        m = re.search(r"\(v2 rule (\d)\)", n["reason"])
        if not m:
            sys.exit(f"row {i} changed decision without a v2 rule marker: {n['reason']}")
        row_type = frame[i]["row_type"] if i < len(frame) else "NA"
        out.append([n["disease"], row_type, n["test"], o["decision"], o["reason"],
                    n["decision"], n["reason"], f"rule {m.group(1)}"])

    with open(EXP / "eligibility_v2_changes.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease_name", "row_type", "row_name", "v1_decision", "v1_reason",
                    "v2_decision", "v2_reason", "rule"])
        w.writerows(out)
    from collections import Counter
    print(f"decisions changed: {len(out)}")
    for (rule, d1, d2), c in sorted(Counter((r[7], r[3], r[5]) for r in out).items()):
        print(f"  {rule}: {d1} -> {d2}  {c}")


if __name__ == "__main__":
    main()
