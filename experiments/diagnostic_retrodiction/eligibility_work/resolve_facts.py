"""Resolve the FACTS disagreements between screeners A and B by majority with C.

For every row of ../eligibility_disagreements.tsv with cause FACTS:
  A  screener A's decision in eligibility.tsv as built under rules version 2
     (read from --base-ref, the commit that published version 2)
  B  ../eligibility.screenerB.tsv
  C  ../eligibility.screenerC.tsv
The majority of the three decisions is final. Where it differs from A, the row
is overridden in ov9_resolution.txt with the reason of a screener in the
majority (C when C is in it, otherwise B), marked ``(screener majority)``.
Rows where A is already in the majority are left exactly as they are.

The script then rebuilds eligibility.tsv and eligibility_review.tsv with
build_eligibility.py and writes ../eligibility_resolution.tsv, listing every
decision that differs from --base-ref.

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/resolve_facts.py
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


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def git_tsv(ref: str, path: Path) -> list[dict]:
    text = subprocess.run(["git", "show", f"{ref}:{path.relative_to(REPO).as_posix()}"], cwd=REPO,
                          check=True, capture_output=True, text=True).stdout
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--base-ref", default="70c47e11be0", help="commit holding the version 2 build")
    a = ap.parse_args()

    key = lambda r: (r["disease_name"], r["row_type"], r["row_name"])
    frame = [r for r in read_tsv(EXP / "frame.tsv") if r["flag_nongenetic_specimen"] == "TRUE"]
    idx = {key(r): i for i, r in enumerate(frame)}
    base = git_tsv(a.base_ref, EXP / "eligibility.tsv")
    facts = [r for r in read_tsv(EXP / "eligibility_disagreements.tsv") if r["cause"] == "FACTS"]
    b_rows = {key(r): r for r in read_tsv(EXP / "eligibility.screenerB.tsv")}
    c_rows = {key(r): r for r in read_tsv(EXP / "eligibility.screenerC.tsv")}
    missing = [key(r) for r in facts if key(r) not in c_rows]
    if missing:
        sys.exit(f"screener C has no decision for: {missing}")

    lines, resolved = [], {}
    for r in facts:
        k = key(r)
        i = idx[k]
        votes = {"A": base[i]["decision"], "B": b_rows[k]["decision"], "C": c_rows[k]["decision"]}
        majority, n = Counter(votes.values()).most_common(1)[0]
        resolved[i] = (votes, majority)
        if votes["A"] == majority:
            continue
        src = "C" if votes["C"] == majority else "B"
        reason = (c_rows if src == "C" else b_rows)[k]["reason"]
        m = re.match(r"([A-Z_0-9]+)( \(ambiguous\))?: (.*?)(?: \[[a-z-]+\])?$", reason, re.S)
        if not m:
            sys.exit(f"cannot parse screener {src} reason for {k}: {reason}")
        code, amb, detail = m.group(1), "1" if m.group(2) else "0", " ".join(m.group(3).split())
        code = "INCLUDE" if code == "PRIMARY_ROUTE" else code
        detail = detail.replace("|", "/")
        foi = "FIRST" if code == "INCLUDE" else "NA"
        lines.append(f"{i}|{code}|{amb}|{foi}|screener {src}, in the {n}-of-3 majority: {detail} (screener majority)")

    (HERE / "ov9_resolution.txt").write_text(
        "# FACTS disagreements resolved by majority of screeners A, B and C (resolve_facts.py).\n"
        "# Only rows where A was outvoted are listed; applied after rule 2, as the final judgment.\n"
        "# idx|CODE|ambiguous|FIRST/IMPROVEMENT/NA|detail\n" + "\n".join(lines) + "\n", encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "build_eligibility.py")], check=True, stdout=subprocess.DEVNULL)

    final = read_tsv(EXP / "eligibility.tsv")
    with open(EXP / "eligibility_resolution.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease_name", "row_type", "row_name", "A_decision", "B_decision", "C_decision",
                    "majority", "before_decision", "before_reason", "after_decision", "after_reason"])
        changed = 0
        for i, (o, n) in enumerate(zip(base, final)):
            if o["decision"] == n["decision"]:
                continue
            if i not in resolved:
                sys.exit(f"row {i} changed decision but is not a FACTS row")
            votes, majority = resolved[i]
            fr = frame[i]
            w.writerow([fr["disease_name"], fr["row_type"], fr["row_name"], votes["A"], votes["B"],
                        votes["C"], majority, o["decision"], o["reason"], n["decision"], n["reason"]])
            changed += 1
    inc = [r for r in final if r["decision"] == "INCLUDE"]
    print(f"FACTS rows: {len(facts)}; A outvoted: {len(lines)}; decisions changed: {changed}")
    print(f"final INCLUDE rows: {len(inc)}; diseases: {len({r['disease'] for r in inc})}")


if __name__ == "__main__":
    main()
