"""List every row whose eligibility decision differs between two builds.

Two comparisons are defined, one per rules version:

  --version 2   v1 build (commit 638510c70fa) -> v2 build (commit 70c47e11be0)
                writes ../eligibility_v2_changes.tsv
  --version 3   final v2 build, after the screener resolution (commit
                ed61c89ef68) -> the v3 build (commit 03b1f051556)
                writes ../eligibility_v3_changes.tsv

Both sides of each comparison are read with ``git show``, so rerunning it
reproduces the committed file whatever the working tree holds. Later
resolution rounds (eligibility_rule1_rescreen.tsv) are recorded separately.

Columns: disease_name, row_type, row_name, old_decision, old_reason,
new_decision, new_reason, rule. ``rule`` says which change of rules made the
decision move, and every changed decision must have one:

  version 2: the ``(v2 rule N)`` marker on the new reason
  version 3: "rule 2 removed" when the old reason carried version 2's computed
             count ``(v2 rule 2)``; "INSUFFICIENT_PRE_CUTOFF_LITERATURE" when
             the new reason is that computed exclusion

A changed decision that fits none of these is an error. Frame rows are matched
by position (both files list the flagged frame rows in frame order, which
build_eligibility.py checks).

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/version_changes.py [--version 2|3]
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
REPO = EXP.parents[1]
REL = (EXP / "eligibility.tsv").relative_to(REPO).as_posix()
COMPARISONS = {
    2: ("638510c70fa", "70c47e11be0", "eligibility_v2_changes.tsv"),
    3: ("ed61c89ef68", "03b1f051556", "eligibility_v3_changes.tsv"),
}
OLD_NEW_COLS = {2: ("v1", "v2"), 3: ("v2", "v3")}


def read_version(ref: str | None) -> list[dict]:
    if ref is None:
        with open(EXP / "eligibility.tsv", newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f, delimiter="\t"))
    text = subprocess.run(["git", "show", f"{ref}:{REL}"], cwd=REPO, check=True,
                          capture_output=True, text=True).stdout
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def attribute(version: int, old: dict, new: dict) -> str | None:
    if version == 2:
        m = re.search(r"\(v2 rule (\d)\)", new["reason"])
        return f"rule {m.group(1)}" if m else None
    if "(v2 rule 2)" in old["reason"]:
        return "rule 2 removed"
    if new["reason"].startswith("INSUFFICIENT_PRE_CUTOFF_LITERATURE"):
        return "INSUFFICIENT_PRE_CUTOFF_LITERATURE"
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--version", type=int, choices=sorted(COMPARISONS), default=2)
    a = ap.parse_args()
    old_ref, new_ref, out_name = COMPARISONS[a.version]
    old, new = read_version(old_ref), read_version(new_ref)
    with open(EXP / "frame.tsv", newline="", encoding="utf-8") as f:
        frame = [r for r in csv.DictReader(f, delimiter="\t") if r["flag_nongenetic_specimen"] == "TRUE"]
    if len(old) != len(new) or len(old) < len(frame):
        sys.exit(f"row counts differ: old {len(old)}, new {len(new)}, flagged frame {len(frame)}")

    rows = []
    for i, (o, n) in enumerate(zip(old, new)):
        if (o["disease"], o["test"]) != (n["disease"], n["test"]):
            sys.exit(f"row {i} does not line up between builds")
        if o["decision"] == n["decision"]:
            continue
        rule = attribute(a.version, o, n)
        if rule is None:
            sys.exit(f"row {i} changed decision with no version {a.version} rule to account for it:\n"
                     f"  old: {o['reason']}\n  new: {n['reason']}")
        row_type = frame[i]["row_type"] if i < len(frame) else "NA"
        rows.append([n["disease"], row_type, n["test"], o["decision"], o["reason"],
                     n["decision"], n["reason"], rule])

    o_tag, n_tag = OLD_NEW_COLS[a.version]
    with open(EXP / out_name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease_name", "row_type", "row_name", f"{o_tag}_decision", f"{o_tag}_reason",
                    f"{n_tag}_decision", f"{n_tag}_reason", "rule"])
        w.writerows(rows)
    print(f"{out_name}: {len(rows)} decisions changed")
    for (rule, d1, d2), c in sorted(Counter((r[7], r[3], r[5]) for r in rows).items()):
        print(f"  {rule}: {d1} -> {d2}  {c}")


if __name__ == "__main__":
    main()
