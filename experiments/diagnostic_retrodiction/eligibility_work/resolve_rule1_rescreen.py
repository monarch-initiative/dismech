"""Resolve the rule-1 re-screen: screener A vs B2, with C2 breaking ties.

Screener B2 (../eligibility.screenerB2.tsv) re-screened the 32 rows of
../screenerB2_input.tsv blind. On the rows where B2's decision differs from
screener A's, screener C2 (../eligibility.screenerC2.tsv, a fresh session given
prompts/screenerC2.md) decided again, and the majority of A, B2 and C2 is
final: the same 2-of-3 rule as resolve_facts.py.

  A   build_eligibility.py's build with resolution rounds up to, but not
      including, this one (so the FACTS resolution, ov9, is in A's vote)
  B2  ../eligibility.screenerB2.tsv
  C2  ../eligibility.screenerC2.tsv

Where A is outvoted, the row is written to ov10_rule1_rescreen.txt with the
reason of a majority screener (C2 when it is in the majority, otherwise B2),
marked ``(screener majority, rule-1 re-screen)``. A row that becomes INCLUDE
takes its subset from that screener; the script stops if that subset is not
already in subset_v2.txt, so subsets are never written silently.

Prints agreement and Cohen's kappa for A vs B2 on the 32 rows, rebuilds, and
writes ../eligibility_rule1_rescreen.tsv: every disputed row with the three
votes, the majority, and A's decision before and after.

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/resolve_rule1_rescreen.py
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
ROUND = "ov10_rule1_rescreen.txt"


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    sys.path.insert(0, str(HERE))
    from build_eligibility import build

    key = lambda r: (r["disease_name"], r["row_type"], r["row_name"])
    frame = [r for r in read_tsv(EXP / "frame.tsv") if r["flag_nongenetic_specimen"] == "TRUE"]
    idx = {key(r): i for i, r in enumerate(frame)}
    _, _, base = build(upto=ROUND)
    b2 = {key(r): r for r in read_tsv(EXP / "eligibility.screenerB2.tsv")}
    expected = {key(r) for r in read_tsv(EXP / "screenerB2_input.tsv")}
    if set(b2) != expected:
        sys.exit("eligibility.screenerB2.tsv does not cover exactly the screenerB2_input.tsv rows")

    table = Counter((base[idx[k]]["decision"], b2[k]["decision"]) for k in b2)
    n = len(b2)
    ii, ie, ei, ee = (table[("INCLUDE", "INCLUDE")], table[("INCLUDE", "EXCLUDE")],
                      table[("EXCLUDE", "INCLUDE")], table[("EXCLUDE", "EXCLUDE")])
    po = (ii + ee) / n
    pa, pb = (ii + ie) / n, (ii + ei) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    print(f"A vs B2 on {n} rows: agreement {ii + ee}/{n} = {po:.4f}; expected {pe:.4f}; "
          f"kappa {(po - pe) / (1 - pe):.4f}")
    print(f"  A INCLUDE: B2 INCLUDE {ii}, B2 EXCLUDE {ie};  A EXCLUDE: B2 INCLUDE {ei}, B2 EXCLUDE {ee}")

    disputed = [k for k in b2 if base[idx[k]]["decision"] != b2[k]["decision"]]
    c2 = {key(r): r for r in read_tsv(EXP / "eligibility.screenerC2.tsv")}
    if set(c2) != set(disputed):
        sys.exit(f"eligibility.screenerC2.tsv must cover exactly the {len(disputed)} disputed rows")
    subsets = {int(l.split("|", 1)[0]): l.split("|", 1)[1].strip()
               for l in (HERE / "subset_v2.txt").read_text().splitlines() if l[:1].isdigit()}

    lines, votes_by_row = [], {}
    for k in disputed:
        i = idx[k]
        votes = {"A": base[i]["decision"], "B2": b2[k]["decision"], "C2": c2[k]["decision"]}
        majority, count = Counter(votes.values()).most_common(1)[0]
        votes_by_row[i] = (votes, majority)
        if votes["A"] == majority:
            continue
        src_name, src = ("C2", c2[k]) if votes["C2"] == majority else ("B2", b2[k])
        m = re.match(r"([A-Z_0-9]+)( \(ambiguous\))?: (.*?)(?: \[[a-z-]+\])?$", src["reason"], re.S)
        if not m:
            sys.exit(f"cannot parse screener {src_name}'s reason for {k}: {src['reason']}")
        code = "INCLUDE" if m.group(1) == "PRIMARY_ROUTE" else m.group(1)
        detail = " ".join(m.group(3).split()).replace("|", "/")
        foi = (src.get("first_or_improvement") or "FIRST") if code == "INCLUDE" else "NA"
        if code == "INCLUDE":
            want = (src.get("subset") or "ALL").strip()
            have = subsets.get(i, "ALL")
            if want != have:
                sys.exit(f"row {i} becomes INCLUDE with subset {want!r} (from {src_name}) but subset_v2.txt "
                         f"gives {have!r}; record the subset in subset_v2.txt first")
        lines.append(f"{i}|{code}|{'1' if m.group(2) else '0'}|{foi}|screener {src_name}, in the "
                     f"{count}-of-3 majority: {detail} (screener majority, rule-1 re-screen)")

    (HERE / ROUND).write_text(
        "# Rule-1 re-screen: rows where screener B2 disagreed with A, resolved by the majority of\n"
        "# A, B2 and C2 (resolve_rule1_rescreen.py). Only rows where A was outvoted are listed.\n"
        "# idx|CODE|ambiguous|FIRST/IMPROVEMENT/NA|detail\n" + "\n".join(lines) + ("\n" if lines else ""),
        encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "build_eligibility.py")], check=True, stdout=subprocess.DEVNULL)
    final = read_tsv(EXP / "eligibility.tsv")

    with open(EXP / "eligibility_rule1_rescreen.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease_name", "row_type", "row_name", "A_decision", "B2_decision", "C2_decision",
                    "majority", "changed", "before_reason", "after_reason"])
        for k in sorted(disputed, key=lambda k: idx[k]):
            i = idx[k]
            votes, majority = votes_by_row[i]
            w.writerow([*k, votes["A"], votes["B2"], votes["C2"], majority,
                        "TRUE" if final[i]["decision"] != base[i]["decision"] else "FALSE",
                        base[i]["reason"], final[i]["reason"]])
    moved = [i for i in range(len(frame)) if final[i]["decision"] != base[i]["decision"]]
    stray = [i for i in moved if i not in votes_by_row]
    if stray:
        sys.exit(f"rows outside the re-screen changed decision: {stray}")
    inc = [r for r in final if r["decision"] == "INCLUDE"]
    print(f"disputed rows: {len(disputed)}; A outvoted: {len(lines)}; decisions changed: {len(moved)}")
    print(f"final INCLUDE rows: {len(inc)}; diseases: {len({r['disease'] for r in inc})}")


if __name__ == "__main__":
    main()
