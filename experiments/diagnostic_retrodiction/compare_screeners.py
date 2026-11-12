"""Compare screener A (eligibility.tsv) with screener B (eligibility.screenerB.tsv).

This is the version-1 comparison. Both inputs are read with ``git show`` from
commit 528cef7e51a, where the comparison was made and eligibility.tsv held
screener A's version-1 decisions, so the script reproduces
eligibility_disagreements.tsv exactly however eligibility.tsv has changed since.
``--ref`` points it at another commit; its hand-written NOTES only fit 528cef7e51a.

Rows are joined on (disease_name, row_type, row_name). eligibility.tsv has no
row_type column, so its first 3,311 rows are matched to the flagged frame rows
by position, which build_eligibility.py guarantees; the disease and test names
are checked on every row.

Prints Cohen's kappa for INCLUDE/EXCLUDE, raw agreement, the 2x2 table, and
disagreement counts by (A reason, B reason). Writes eligibility_disagreements.tsv
with one row per disagreement. ``note`` names the section of
eligibility_rules.md each side applied, and ``cause`` classifies the
disagreement:

  WORDING_AMBIGUITY    both readings fit the rule as written; the rule text
                       does not settle the case
  FACTS                the screeners read the same rule the same way but judged
                       the clinical or literature facts differently
  A_DEPARTS_FROM_RULE  screener A's decision contradicts the written rule

The notes and causes are hand-assigned (NOTES below); the script fails if a
disagreement has no note, or if a note no longer matches a disagreement.

Usage:
    python experiments/diagnostic_retrodiction/compare_screeners.py
"""
from __future__ import annotations

import argparse
import collections
import csv
import io
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
COMPARISON_REF = "528cef7e51a"

W, F, X = "WORDING_AMBIGUITY", "FACTS", "A_DEPARTS_FROM_RULE"
SUB = "Standing decisions: subtype antibody in a broader entry"
NOTES: dict[tuple[str, str, str], tuple[str, str]] = {
    ("Limbic Encephalitis", "BIOCHEMICAL", "LGI1 Antibodies"): (W,
        f"A: inclusion rule (the antibody diagnoses this form of limbic encephalitis). B: {SUB}. "
        "The rule does not say when an entry counts as broader."),
    ("Limbic Encephalitis", "BIOCHEMICAL", "CASPR2 Antibodies"): (W,
        f"A: inclusion rule. B: {SUB}. Same unresolved scope question as LGI1."),
    ("Limbic Encephalitis", "BIOCHEMICAL", "GABAB Receptor Antibodies"): (W,
        f"A: inclusion rule. B: {SUB}. Same unresolved scope question as LGI1."),
    ("Limbic Encephalitis", "BIOCHEMICAL", "AMPAR GluR1/GluR2 Antibodies"): (W,
        f"A: inclusion rule. B: {SUB}. Same unresolved scope question as LGI1."),
    ("Myasthenia Gravis", "BIOCHEMICAL", "Anti-MuSK Antibodies"): (W,
        f"A: inclusion rule (route for AChR-seronegative MG). B: {SUB}. "
        "Whether a seronegative subset is a subtype or part of the disease is not defined."),
    ("Narcolepsy", "BIOCHEMICAL", "CSF Orexin/Hypocretin-1"): (W,
        f"A: inclusion rule (alternative to MSLT). B: {SUB} (type 1 within narcolepsy). "
        "The rule names antibodies only; it does not say whether it covers non-antibody subtype markers."),
    ("Statin Toxicity", "DIAGNOSIS", "Anti-HMGCR antibody testing"): (W,
        f"A: inclusion rule (diagnosis without muscle biopsy). B: {SUB} (necrotizing myopathy within statin toxicity)."),
    ("Anti-NMDA Receptor Encephalitis", "BIOCHEMICAL", "Serum Anti-NMDAR IgG"): (W,
        "A: inclusion rule. B: exclusion 7 DISEASE_DEFINED_BY_TEST. The rule does not say whether a "
        "description a year or two before the test counts as a pre-test diagnostic era."),
    ("Anti-NMDA Receptor Encephalitis", "BIOCHEMICAL", "CSF Anti-NMDAR IgG"): (W,
        "A: inclusion rule. B: exclusion 7 DISEASE_DEFINED_BY_TEST. Same question as the serum row."),
    ("MOGAD", "DIAGNOSIS", "Serum MOG-IgG Antibody Testing"): (W,
        "A: inclusion rule (cases were earlier diagnosed as MS/NMOSD/ADEM). B: exclusion 7 "
        "DISEASE_DEFINED_BY_TEST. The rule does not say whether patients diagnosed under another name "
        "count as a pre-test era."),
    ("Chronic Kidney Disease", "DIAGNOSIS", "Estimated glomerular filtration rate"): (W,
        "A: FIRST or IMPROVEMENT (IMPROVEMENT over measured clearance). B: exclusion 8 PRE_1985 "
        "(Cockcroft-Gault 1976). The rules allow IMPROVEMENT over an earlier accessible-specimen test "
        "but do not say how that interacts with PRE_1985 when the earlier test predates 1985."),
    ("Chronic Granulomatous Disease", "DIAGNOSIS", "Neutrophil oxidative burst testing (DHR / NBT)"): (W,
        "A: FIRST or IMPROVEMENT (DHR flow replaced NBT). B: exclusion 8 PRE_1985 (NBT 1967). "
        "Same IMPROVEMENT-vs-PRE_1985 gap; the row also names both tests."),
    ("Heparin-Induced Thrombocytopenia", "DIAGNOSIS", "Functional platelet activation assay"): (W,
        "A: FIRST or IMPROVEMENT (serotonin-release assay 1986). B: exclusion 8 PRE_1985 "
        "(aggregation tests). Same IMPROVEMENT-vs-PRE_1985 gap."),
    ("Membranous nephropathy", "DIAGNOSIS", "Serology and target-antigen work-up"): (W,
        "A: inclusion rule (PLA2R serology). B: exclusion 5 TISSUE_REQUIRED (antigen staining of the "
        "biopsy). The combined-row standing decision covers biochemical-plus-molecular rows only, not a "
        "serology-plus-tissue row."),
    ("Sezary Syndrome", "DIAGNOSIS", "Peripheral blood flow cytometry with KIR3DL2, CD7, and CD26 assessment"): (W,
        "A: inclusion rule, dated to consensus criteria. B: exclusion 9 NOT_DATABLE (markers from several "
        "reports). The rule does not say whether a consensus criteria document counts as the one primary "
        "publication."),
    ("Pyridoxine-Dependent Epilepsy", "DIAGNOSIS", "Alpha-AASA Biomarker and ALDH7A1 Testing"): (X,
        "A: inclusion rule. B: standing decision for combined biochemical-plus-molecular rows "
        "(GERMLINE_SEQUENCING, ambiguous). B applied the written rule; A's INCLUDE contradicts it."),
    ("Sezary Syndrome", "BIOCHEMICAL", "KIR3DL2-positive circulating tumor T cells"): (F,
        "A: inclusion rule (part of the flow route). B: exclusion 10 NOT_PRIMARY_ROUTE (one marker "
        "among several). Differ on whether this single marker is the route."),
    ("FAS-related Autoimmune Lymphoproliferative Syndrome", "DIAGNOSIS", "Serum biomarker analysis"): (F,
        "A: inclusion rule (replaced the Fas apoptosis assay). B: exclusion 10 NOT_PRIMARY_ROUTE "
        "(accessory criteria). Differ on the biomarkers' weight in the revised criteria."),
    ("FAS-related Autoimmune Lymphoproliferative Syndrome", "BIOCHEMICAL", "Elevated Serum Vitamin B12"): (F,
        "A: inclusion rule. B: exclusion 10 NOT_PRIMARY_ROUTE (accessory criterion). Same as the panel row."),
    ("FAS-related Autoimmune Lymphoproliferative Syndrome", "BIOCHEMICAL", "Elevated Serum IL-10"): (F,
        "A: inclusion rule. B: exclusion 10 NOT_PRIMARY_ROUTE (accessory criterion). Same as the panel row."),
    ("Traumatic Brain Injury", "BIOCHEMICAL", "Serum GFAP"): (F,
        "A: inclusion rule (replaced CT). B: exclusion 10 NOT_PRIMARY_ROUTE (triages CT; does not "
        "diagnose TBI). Differ on what the test establishes."),
    ("Traumatic Brain Injury", "BIOCHEMICAL", "Serum UCH-L1"): (F,
        "A: inclusion rule. B: exclusion 10 NOT_PRIMARY_ROUTE. Same as GFAP."),
    ("Alzheimer Disease", "DIAGNOSIS", "Cerebrospinal Fluid Analysis"): (F,
        "A: inclusion rule (replaced clinical criteria/autopsy). B: exclusion 10 NOT_PRIMARY_ROUTE "
        "(adjunct, uneven uptake). Differ on clinical uptake."),
    ("Alzheimer Disease", "BIOCHEMICAL", "Amyloid Beta (Aβ42)"): (F,
        "A: inclusion rule. B: exclusion 10 NOT_PRIMARY_ROUTE. Same as the CSF analysis row."),
    ("Autoimmune Autonomic Ganglionopathy", "DIAGNOSIS", "Ganglionic AChR antibody testing with assay-aware interpretation"): (F,
        "A: inclusion rule (replaced autonomic testing). B: exclusion 10 NOT_PRIMARY_ROUTE (autonomic "
        "testing still establishes the failure). Differ on whether the antibody replaces that testing."),
    ("Autoimmune Autonomic Ganglionopathy", "BIOCHEMICAL", "Serum Ganglionic Acetylcholine Receptor Antibodies"): (F,
        "A: inclusion rule. B: exclusion 10 NOT_PRIMARY_ROUTE. Same as the diagnosis row."),
    ("Dihydropyrimidine Dehydrogenase Deficiency", "DIAGNOSIS", "Uracil phenotyping"): (F,
        "A: inclusion rule (replaced the PBMC enzyme assay). B: exclusion 10 NOT_PRIMARY_ROUTE "
        "(pre-treatment screening, confirmed by genotype or enzyme). Differ on whether uracil is "
        "diagnostic or screening."),
    ("Dihydropyrimidine Dehydrogenase Deficiency", "BIOCHEMICAL", "Plasma uracil concentration"): (F,
        "A: inclusion rule. B: exclusion 10 NOT_PRIMARY_ROUTE. Same as the diagnosis row."),
    ("Microscopic Polyangiitis", "BIOCHEMICAL", "MPO-ANCA (p-ANCA)"): (F,
        "A: inclusion rule (serologic diagnosis). B: exclusion 5 TISSUE_REQUIRED (biopsy still "
        "recommended). Differ on what guidelines require."),
    ("Stiff Person Syndrome", "BIOCHEMICAL", "CSF Anti-GAD65 Antibodies"): (F,
        "A: inclusion rule (same 1988 test as serum). B: exclusion 10 NOT_PRIMARY_ROUTE (CSF is "
        "supportive; serum is the route). Differ on the CSF assay's role."),
    ("Late-Onset Pompe Disease", "BIOCHEMICAL", "Reduced but not absent acid alpha-glucosidase activity"): (F,
        "A: exclusion 8 PRE_1985 (row read as the leukocyte/fibroblast assay). B: inclusion rule (row "
        "read as the DBS assay). Differ on which assay the row records."),
}


def code(reason: str) -> str:
    return re.match(r"([A-Z_0-9]+)", reason).group(1)


def at_ref(ref: str, name: str) -> list[dict]:
    rel = (HERE / name).relative_to(REPO).as_posix()
    text = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=REPO, check=True,
                          capture_output=True, text=True).stdout
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ref", default=COMPARISON_REF, help="commit to read both screeners' files from")
    args = ap.parse_args()
    with open(HERE / "frame.tsv", newline="", encoding="utf-8") as f:
        frame = [r for r in csv.DictReader(f, delimiter="\t") if r["flag_nongenetic_specimen"] == "TRUE"]
    a_rows = at_ref(args.ref, "eligibility.tsv")[:len(frame)]
    for fr, a in zip(frame, a_rows):
        if (fr["disease_name"], fr["row_name"]) != (a["disease"], a["test"]):
            sys.exit("eligibility.tsv rows no longer line up with the flagged frame rows")
    a_by_key = {(fr["disease_name"], fr["row_type"], fr["row_name"]): a for fr, a in zip(frame, a_rows)}
    b_rows = at_ref(args.ref, "eligibility.screenerB.tsv")

    table = collections.Counter()
    dis = []
    for b in b_rows:
        k = (b["disease_name"], b["row_type"], b["row_name"])
        if k not in a_by_key:
            sys.exit(f"screener B row not in the flagged frame: {k}")
        a = a_by_key[k]
        table[(a["decision"], b["decision"])] += 1
        if a["decision"] != b["decision"]:
            dis.append((k, a, b))

    n = len(b_rows)
    ii, ie, ei, ee = (table[("INCLUDE", "INCLUDE")], table[("INCLUDE", "EXCLUDE")],
                      table[("EXCLUDE", "INCLUDE")], table[("EXCLUDE", "EXCLUDE")])
    po = (ii + ee) / n
    pa, pb = (ii + ie) / n, (ii + ei) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    kappa = (po - pe) / (1 - pe)

    missing = [k for k, _, _ in dis if k not in NOTES]
    stale = set(NOTES) - {k for k, _, _ in dis}
    if missing or stale:
        sys.exit(f"notes out of date: missing {missing}, stale {sorted(stale)}")

    with open(HERE / "eligibility_disagreements.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["disease_name", "row_type", "row_name", "A_decision", "A_reason",
                    "B_decision", "B_reason", "cause", "note"])
        for k, a, b in sorted(dis, key=lambda d: (NOTES[d[0]][0], d[0])):
            w.writerow([*k, a["decision"], a["reason"], b["decision"], b["reason"], *NOTES[k]])

    print(f"rows compared: {n}")
    print(f"raw agreement: {ii + ee}/{n} = {po:.4f}")
    print(f"expected agreement: {pe:.4f}; Cohen's kappa: {kappa:.4f}")
    print("\n               B INCLUDE  B EXCLUDE")
    print(f"A INCLUDE      {ii:9d}  {ie:9d}")
    print(f"A EXCLUDE      {ei:9d}  {ee:9d}")
    print("\ndisagreements by (A reason, B reason):")
    for (ra, rb), c in collections.Counter((code(a["reason"]), code(b["reason"])) for _, a, b in dis).most_common():
        print(f"  {c:3d}  {ra} -> {rb}")
    print("\nby cause:", dict(collections.Counter(NOTES[k][0] for k, _, _ in dis)))


if __name__ == "__main__":
    main()
