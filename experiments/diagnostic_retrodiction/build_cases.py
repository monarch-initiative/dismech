"""Collapse the INCLUDE rows of eligibility.tsv into one case per disease-test pair.

A dismech entry often records one test twice (a diagnosis row and a
biochemical row, or serum and CSF versions of one antibody). Those rows become
one case. The same test recorded under different entries stays as one case
per entry, linked by ``test_group``. CASE_MAP below assigns every INCLUDE row
to its case by hand; the script stops if an INCLUDE row is unassigned, if an
assigned row is not INCLUDE, or if the rows of one case disagree on subset or
first_or_improvement.

cases.tsv columns:
  case_id               C001...
  disease               dismech entry name
  mondo_id              from frame.tsv
  test                  the test, named once for the case
  subset                rule 1 subset, or ALL
  test_class            AUTOANTIBODY / ENZYME_ACTIVITY / METABOLITE / SOMATIC_VARIANT /
                        CELL_SURFACE_MARKER / SECRETED_PROTEIN / OTHER
  first_or_improvement  FIRST or IMPROVEMENT
  test_group            the test across entries; cases sharing it are the same test
  source_frame_rows     1-based data-row numbers in frame.tsv (header not counted),
                        ';'-separated

Also writes known_positives_cases.tsv: for each pair in known_positives.tsv,
whether it is in cases.tsv (matched as check_recall.py matches pairs: the
disease pattern as a case-insensitive substring of the entry name, the test
pattern as a regex over the row's name, term labels, measurements and
readouts), the case it lands in, and, when absent, the eligibility decision
and reason of every frame row the pair matches.

Usage:
    python experiments/diagnostic_retrodiction/build_cases.py
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASSES = {"AUTOANTIBODY", "ENZYME_ACTIVITY", "METABOLITE", "SOMATIC_VARIANT",
           "CELL_SURFACE_MARKER", "SECRETED_PROTEIN", "OTHER"}

# (test, test_class, test_group, [flagged-row indices]) -- one tuple per case.
# Flagged-row index = position among frame rows with flag_nongenetic_specimen TRUE.
CASE_MAP = [
    ("ADAMTS13 activity", "ENZYME_ACTIVITY", "ADAMTS13 activity", [175, 177]),
    ("plasma p-tau217", "SECRETED_PROTEIN", "plasma p-tau217", [305]),
    ("CSF amyloid-beta 42", "SECRETED_PROTEIN", "CSF amyloid-beta 42", [306]),
    ("anti-NMDA receptor IgG (serum and CSF)", "AUTOANTIBODY", "anti-NMDA receptor IgG", [334, 336]),
    ("anti-interferon-omega autoantibodies", "AUTOANTIBODY", "anti-type I interferon autoantibodies", [473, 474]),
    ("anti-GM-CSF autoantibodies", "AUTOANTIBODY", "anti-GM-CSF autoantibodies", [479, 480]),
    ("monolysocardiolipin:cardiolipin ratio", "METABOLITE", "monolysocardiolipin:cardiolipin ratio", [576]),
    ("urinary N-acetylaspartic acid", "METABOLITE", "urinary N-acetylaspartic acid", [735, 737]),
    ("anti-tissue transglutaminase IgA", "AUTOANTIBODY", "anti-tissue transglutaminase IgA", [769]),
    ("CSF glucose (hypoglycorrhachia)", "METABOLITE", "CSF glucose for GLUT1 deficiency", [822]),
    ("anti-neurofascin antibodies", "AUTOANTIBODY", "anti-neurofascin antibodies", [840]),
    ("anti-contactin-1 antibodies", "AUTOANTIBODY", "anti-contactin-1 antibodies", [841]),
    ("ADAMTS13 activity", "ENZYME_ACTIVITY", "ADAMTS13 activity", [973, 975]),
    ("anti-MDA5 antibodies", "AUTOANTIBODY", "anti-MDA5 antibodies", [1060]),
    ("leukocyte telomere length by flow-FISH", "OTHER", "leukocyte telomere length by flow-FISH", [1136]),
    ("leukocyte telomere length by flow-FISH", "OTHER", "leukocyte telomere length by flow-FISH", [1138]),
    ("anti-PLA2R antibodies", "AUTOANTIBODY", "anti-PLA2R antibodies", [1432]),
    ("anti-PF4/heparin IgG immunoassay", "AUTOANTIBODY", "anti-PF4/heparin IgG", [1549]),
    ("TREC newborn screening", "OTHER", "TREC newborn screening", [1764]),
    ("TREC newborn screening", "OTHER", "TREC newborn screening", [1766]),
    ("leukocyte telomere length by flow-FISH", "OTHER", "leukocyte telomere length by flow-FISH", [1836]),
    ("dried-blood-spot acid alpha-glucosidase activity", "ENZYME_ACTIVITY", "acid alpha-glucosidase activity", [1967]),
    ("anti-LGI1 antibodies", "AUTOANTIBODY", "anti-LGI1 antibodies", [2012]),
    ("anti-CASPR2 antibodies", "AUTOANTIBODY", "anti-CASPR2 antibodies", [2013]),
    ("anti-GABAB receptor antibodies", "AUTOANTIBODY", "anti-GABAB receptor antibodies", [2014]),
    ("anti-AMPA receptor antibodies", "AUTOANTIBODY", "anti-AMPA receptor antibodies", [2015]),
    ("serum VEGF-D", "SECRETED_PROTEIN", "serum VEGF-D", [2041, 2042]),
    ("MOG-IgG cell-based assay", "AUTOANTIBODY", "MOG-IgG", [2070]),
    ("anti-PLA2R antibodies", "AUTOANTIBODY", "anti-PLA2R antibodies", [2144, 2145]),
    ("plasma DOPA:DHPG ratio", "METABOLITE", "plasma DOPA:DHPG ratio", [2158, 2161]),
    ("leukocyte thymidine phosphorylase activity", "ENZYME_ACTIVITY", "thymidine phosphorylase activity", [2242]),
    ("plasma thymidine and deoxyuridine", "METABOLITE", "plasma thymidine and deoxyuridine", [2243, 2244, 2245]),
    ("anti-MuSK antibodies", "AUTOANTIBODY", "anti-MuSK antibodies", [2311]),
    ("CSF hypocretin-1", "SECRETED_PROTEIN", "CSF hypocretin-1", [2338]),
    ("CSF hypocretin-1", "SECRETED_PROTEIN", "CSF hypocretin-1", [2339]),
    ("plasma copeptin (hypertonic-saline stimulated)", "SECRETED_PROTEIN", "plasma copeptin", [2367, 2370]),
    ("AQP4-IgG", "AUTOANTIBODY", "AQP4-IgG", [2373]),
    ("TPP1 enzyme activity", "ENZYME_ACTIVITY", "TPP1 enzyme activity", [2374]),
    ("MOG-IgG", "AUTOANTIBODY", "MOG-IgG", [2428]),
    ("AQP4-IgG", "AUTOANTIBODY", "AQP4-IgG", [2429]),
    ("CSF glucose (hypoglycorrhachia)", "METABOLITE", "CSF glucose for GLUT1 deficiency", [2514, 2515]),
    ("flow cytometry for GPI-anchored proteins", "CELL_SURFACE_MARKER", "flow cytometry for GPI-anchored proteins", [2516]),
    ("JAK2 V617F", "SOMATIC_VARIANT", "JAK2 V617F", [2627]),
    ("serum 7-alpha-hydroxy-4-cholesten-3-one (C4)", "METABOLITE", "serum 7-alpha-hydroxy-4-cholesten-3-one", [2669]),
    ("alpha-aminoadipic semialdehyde", "METABOLITE", "alpha-aminoadipic semialdehyde", [2763, 2764]),
    ("leukocyte telomere length by flow-FISH", "OTHER", "leukocyte telomere length by flow-FISH", [2828]),
    ("erythrocyte plasmalogens", "METABOLITE", "erythrocyte plasmalogens", [2841]),
    ("erythrocyte plasmalogens", "METABOLITE", "erythrocyte plasmalogens", [2843]),
    ("erythrocyte plasmalogens", "METABOLITE", "erythrocyte plasmalogens", [2844]),
    ("TREC newborn screening", "OTHER", "TREC newborn screening", [2956]),
    ("serum 7-dehydrocholesterol", "METABOLITE", "serum 7-dehydrocholesterol", [2992]),
    ("anti-HMGCR antibodies", "AUTOANTIBODY", "anti-HMGCR antibodies", [3033]),
    ("anti-GAD65 antibodies", "AUTOANTIBODY", "anti-GAD65 antibodies", [3046]),
    ("anti-amphiphysin antibodies", "AUTOANTIBODY", "anti-amphiphysin antibodies", [3048]),
    ("anti-glycine receptor antibodies", "AUTOANTIBODY", "anti-glycine receptor antibodies", [3049]),
    ("AQP4-IgG", "AUTOANTIBODY", "AQP4-IgG", [3158]),
    ("basal plasma copeptin", "SECRETED_PROTEIN", "plasma copeptin", [3269]),
]


def row_identity(row: dict) -> str:
    return " ".join(row.get(k) or "" for k in
                    ("row_name", "diagnosis_term_label", "measurements", "biomarker_term_label", "readouts"))


def load_pairs(path: Path) -> list[dict]:
    pairs = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) >= 3:
            pairs.append({"disease": cols[0].strip(), "test": cols[1].strip(),
                          "label": cols[3].strip() if len(cols) > 3 else cols[1].strip()})
    return pairs


def main() -> None:
    with open(HERE / "frame.tsv", newline="", encoding="utf-8") as f:
        frame_all = list(csv.DictReader(f, delimiter="\t"))
    flagged_rownum = [n for n, r in enumerate(frame_all, 1) if r["flag_nongenetic_specimen"] == "TRUE"]
    flagged = [frame_all[n - 1] for n in flagged_rownum]
    with open(HERE / "eligibility.tsv", newline="", encoding="utf-8") as f:
        elig = list(csv.DictReader(f, delimiter="\t"))
    for fr, e in zip(flagged, elig):
        if (fr["disease_name"], fr["row_name"]) != (e["disease"], e["test"]):
            sys.exit("eligibility.tsv no longer lines up with the flagged frame rows")

    include = {i for i, e in enumerate(elig[:len(flagged)]) if e["decision"] == "INCLUDE"}
    assigned = [i for *_, rows in CASE_MAP for i in rows]
    problems = []
    if len(assigned) != len(set(assigned)):
        problems.append(f"rows assigned twice: {sorted(i for i, c in Counter(assigned).items() if c > 1)}")
    if set(assigned) - include:
        problems.append(f"assigned rows that are not INCLUDE: {sorted(set(assigned) - include)}")
    if include - set(assigned):
        problems.append(f"INCLUDE rows with no case: {sorted(include - set(assigned))}")
    for test, cls, group, rows in CASE_MAP:
        if cls not in CLASSES:
            problems.append(f"{test}: unknown test_class {cls}")
        if len({flagged[i]["disease_name"] for i in rows}) != 1:
            problems.append(f"{test}: rows {rows} span more than one entry")
        for col in ("subset", "first_or_improvement"):
            if len({elig[i][col] for i in rows}) != 1:
                problems.append(f"{test}: rows {rows} disagree on {col}")
    if problems:
        sys.exit("\n".join(problems))

    cases, case_of_row = [], {}
    for n, (test, cls, group, rows) in enumerate(CASE_MAP, 1):
        cid = f"C{n:03d}"
        r0 = flagged[rows[0]]
        cases.append({"case_id": cid, "disease": r0["disease_name"], "mondo_id": r0["mondo_id"], "test": test,
                      "subset": elig[rows[0]]["subset"], "test_class": cls,
                      "first_or_improvement": elig[rows[0]]["first_or_improvement"], "test_group": group,
                      "source_frame_rows": ";".join(str(flagged_rownum[i]) for i in rows)})
        for i in rows:
            case_of_row[flagged_rownum[i]] = cid
    cols = ["case_id", "disease", "mondo_id", "test", "subset", "test_class", "first_or_improvement",
            "test_group", "source_frame_rows"]
    with open(HERE / "cases.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(cases)

    # known positives
    elig_by_rownum = {flagged_rownum[i]: elig[i] for i in range(len(flagged))}
    kb_gap = {e["disease"]: e for e in elig[len(flagged):]}
    out = []
    for p in load_pairs(HERE / "known_positives.tsv"):
        rx = re.compile(p["test"], re.I)
        hits = [n for n, r in enumerate(frame_all, 1)
                if p["disease"].lower() in (r["disease_name"] or "").lower() and rx.search(row_identity(r))]
        in_cases = sorted({case_of_row[n] for n in hits if n in case_of_row})
        if in_cases:
            status, why = "IN_CASES", ""
        elif not hits:
            gap = next((e for d, e in kb_gap.items() if p["disease"].lower() in d.lower()), None)
            status = "KB_GAP" if gap else "NOT_IN_FRAME"
            why = gap["reason"] if gap else "no frame row matches the pair"
        else:
            status = "EXCLUDED"
            why = " || ".join(
                f"{frame_all[n - 1]['disease_name']} / {frame_all[n - 1]['row_name']}: "
                + (f"{elig_by_rownum[n]['decision']} {elig_by_rownum[n]['reason']}" if n in elig_by_rownum
                   else "not flagged in the frame")
                for n in hits)
        out.append({"label": p["label"], "disease_pattern": p["disease"], "status": status,
                    "cases": ";".join(in_cases), "why_absent": why})
    with open(HERE / "known_positives_cases.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["label", "disease_pattern", "status", "cases", "why_absent"],
                           delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    print(f"cases: {len(cases)} from {len(assigned)} INCLUDE rows; "
          f"entries: {len({c['disease'] for c in cases})}; test groups: {len({c['test_group'] for c in cases})}")
    print("\nby test_class:")
    for cls, c in Counter(c["test_class"] for c in cases).most_common():
        print(f"  {c:3d}  {cls}")
    groups = Counter(c["test_group"] for c in cases)
    print("\ntest groups with more than one case:")
    for g, c in sorted(groups.items(), key=lambda x: (-x[1], x[0])):
        if c > 1:
            print(f"  {c}  {g}: " + "; ".join(x["disease"] for x in cases if x["test_group"] == g))
    print(f"  ({sum(1 for c in groups.values() if c == 1)} groups have one case)")
    print("\nknown positives:", dict(Counter(o["status"] for o in out)))
    for o in out:
        print(f"  {o['status']:9s} {o['label']:22s} {o['cases'] or (o['why_absent'][:200])}")


if __name__ == "__main__":
    main()
