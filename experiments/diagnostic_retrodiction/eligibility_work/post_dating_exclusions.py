"""Write post_dating_exclusions.tsv: frame rows of cases excluded after dating.

Two kinds of exclusion are decided only once a case has been dated:
  INSUFFICIENT_PRE_CUTOFF_LITERATURE  literature_check.tsv rules the case below
                                      the packet minimum (check_pretest_era.py)
  WRONG_SPECIMEN                      dating_human_review.tsv records EXCLUDE_CASE
                                      with a note starting "WRONG_SPECIMEN"
  any code in post_dating_decisions.tsv
                                      exclusions decided after dating that are not
                                      review outcomes (e.g. NOT_NEW_ANALYTE), with
                                      who decided and when

Every frame row of such a case (cases.tsv source_frame_rows) is listed, keyed by
its index among the flagged frame rows, which is what build_eligibility.py
joins on. build_eligibility.py turns those rows into EXCLUDE; build_cases.py
then marks the case EXCLUDED in cases.tsv without renumbering any case.

Columns: flagged_idx, case_id, code, detail.

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/post_dating_exclusions.py
"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> None:
    frame = read_tsv(EXP / "frame.tsv")
    flagged_idx = {n: i for i, n in enumerate(
        n for n, r in enumerate(frame, 1) if r["flag_nongenetic_specimen"] == "TRUE")}
    cases = {c["case_id"]: c for c in read_tsv(EXP / "cases.tsv")}
    excl = {}
    for r in read_tsv(EXP / "literature_check.tsv"):
        if r["lit_ruling"] == "INSUFFICIENT_PRE_CUTOFF_LITERATURE":
            excl[r["case_id"]] = ("INSUFFICIENT_PRE_CUTOFF_LITERATURE",
                                  f'{r["lit_count"]} PubMed records with an abstract on or before '
                                  f'{r["cutoff_date"]}, below the packet minimum of {r["packet_minimum"]} '
                                  f'(literature_check.tsv)')
    for r in read_tsv(EXP / "dating_human_review.tsv"):
        if r["decision"] == "EXCLUDE_CASE":
            if not r["notes"].startswith("WRONG_SPECIMEN"):
                sys.exit(f"{r['case_id']}: EXCLUDE_CASE note does not name a known reason")
            if r["case_id"] in excl:
                sys.exit(f"{r['case_id']}: excluded twice")
            excl[r["case_id"]] = ("WRONG_SPECIMEN",
                                  f'human dating review {r["review_date"]}: {r["notes"].split(":", 1)[1].strip()}')
    for r in read_tsv(EXP / "post_dating_decisions.tsv"):
        if r["case_id"] in excl:
            sys.exit(f"{r['case_id']}: excluded twice")
        excl[r["case_id"]] = (r["code"], f'{r["detail"]} ({r["decided_by"]}, {r["decision_date"]})')
    out = []
    for cid in sorted(excl):
        code, detail = excl[cid]
        for n in cases[cid]["source_frame_rows"].split(";"):
            out.append({"flagged_idx": flagged_idx[int(n)], "case_id": cid, "code": code, "detail": detail})
    with open(HERE / "post_dating_exclusions.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["flagged_idx", "case_id", "code", "detail"],
                           delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(out, key=lambda r: r["flagged_idx"]))
    print(f"{len(excl)} cases, {len(out)} frame rows: " + ", ".join(f"{c} {excl[c][0]}" for c in sorted(excl)))


if __name__ == "__main__":
    main()
