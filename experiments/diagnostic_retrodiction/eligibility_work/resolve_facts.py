"""Resolve the FACTS disagreements between screeners A and B by majority with C.

For every row of ../eligibility_disagreements.tsv with cause FACTS:
  A  screener A's decision under the current rules: build_eligibility.py's
     build with the resolution itself left out
  B  ../eligibility.screenerB.tsv
  C  ../eligibility.screenerC.tsv
The majority of the three decisions is final. Where it differs from A, the row
is overridden in ov9_resolution.txt with the reason of a screener in the
majority, marked ``(screener majority)``. C's reason is used when C is in the
majority, unless it rests on version 2's computed pre-test-era count (removed
in version 3), in which case B's reason is used. Rows where A is already in the
majority are left exactly as they are.

The script then rebuilds eligibility.tsv and eligibility_review.tsv and writes
../eligibility_resolution.tsv, listing every decision the resolution changed
relative to A.

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/resolve_facts.py
"""
from __future__ import annotations

import argparse
import csv
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


def uses_removed_count(reason: str) -> bool:
    return "(v2 rule 2)" in reason or "PubMed record" in reason


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.parse_args()
    sys.path.insert(0, str(HERE))
    from build_eligibility import build

    key = lambda r: (r["disease_name"], r["row_type"], r["row_name"])
    frame = [r for r in read_tsv(EXP / "frame.tsv") if r["flag_nongenetic_specimen"] == "TRUE"]
    idx = {key(r): i for i, r in enumerate(frame)}
    _, _, base = build(apply_resolution=False)
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
        candidates = [s for s in ("C", "B") if votes[s] == majority
                      and not uses_removed_count((c_rows if s == "C" else b_rows)[k]["reason"])]
        if not candidates:
            sys.exit(f"no majority screener gives a usable reason for {k}")
        src = candidates[0]
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
