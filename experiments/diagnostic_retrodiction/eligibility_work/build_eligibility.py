"""Regenerate eligibility.tsv and eligibility_review.tsv from frame.tsv plus the
judgment tables in this directory.

Inputs (all committed):
  ../frame.tsv            the frozen sampling frame
  ov1.txt ... ov7.txt     per-row judgments, ``idx|CODE|ambiguous(0/1)|FIRST/IMPROVEMENT/NA|detail``
  wrong.txt               IMPLICIT rows judged WRONG_SPECIMEN, ``idx|what the assay is run on``
  infectious_names.txt    names of kb/disorders entries that declare an
                          ``infectious_agent`` (read from kb/ at the pinned
                          commit; kb/ was byte-identical to it)

``idx`` is the 0-based position of a row among the frame rows with
flag_nongenetic_specimen TRUE, in frame order. The frame is frozen, so the
index is stable; this script checks the flagged-row count before using it.
The judgment files are applied in filename order and a later file wins: only
row 144 (PML-RARA) is judged differently in two files, and ov7 is the decision.

Each row's reason is assembled in this order:
  1. a judgment-table entry                                    [judged]
  2. otherwise a provisional rule category from the test's
     identity (name + bound term label)                        [rule]
  3. otherwise the profiling-platform pattern                  [rule]
  4. otherwise NOT_PRIMARY_ROUTE                               [scanned-default]
An IMPLICIT-basis row listed in wrong.txt becomes WRONG_SPECIMEN regardless.

Usage:
    python experiments/diagnostic_retrodiction/eligibility_work/build_eligibility.py
    python .../build_eligibility.py --check    # compare with the committed files
"""
from __future__ import annotations

import argparse
import collections
import csv
import io
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
FLAGGED_ROWS = 3311
SEED = 20261111
KB_GAPS = [("Lambert-Eaton Myasthenic Syndrome", "VGCC antibody"),
           ("Essential Thrombocythemia", "CALR"),
           ("Hereditary Spherocytosis", "EMA binding")]

# --- provisional rule categories (test identity only) ------------------------
GERMLINE = re.compile(r"sequenc|genetic (test|analys|confirm|diagnos)|gene panel|multigene|exome|genome|genotyp|"
                      r"mutation (analysis|testing|screen)|molecular genetic|variant (testing|analysis)|"
                      r"targeted (gene|variant)|familial variant|carrier test|deletion/duplication|MLPA|"
                      r"chromosom|karyotyp|microarray|\bDNA testing\b|molecular (testing|confirmation|diagnosis)\b", re.I)
INFECT = re.compile(r"virus|viral|\bHIV\b|\bHAV\b|\bHBV\b|\bHCV\b|HBsAg|hepatitis [A-E]\b|bacteri|culture|PCR|NAAT|"
                    r"nucleic acid|serolog|antigen detection|antigen test|IgM antibod|parasit|plasmodium|malaria|"
                    r"borrelia|treponem|\bRPR\b|VDRL|interferon[- ]gamma release|IGRA|quantiferon|smear|"
                    r"agglutination|complement fixation|neutralization|microscopy for|spirochet|fung|candida|"
                    r"aspergill|galactomannan|beta-D-glucan|toxin assay|organism|pathogen|rickettsi|francisella|"
                    r"toxoplasm|cytomegalo|\bCMV\b|\bEBV\b|epstein|leptospir|brucell|coxiella|chlamyd|mycoplasm|"
                    r"mycobacter|tubercul|\bAFB\b|blood film for|paired[- ]serum|avidity|seroconversion", re.I)
TISSUE = re.compile(r"biops|bone marrow|marrow|fibroblast|muscle (tissue|enzyme|histo)|skin |tissue|histolog|"
                    r"histopath|immunohistochem|\bIHC\b|cultured cell|amniocyte|amniotic|chorionic villus|"
                    r"\bCVS\b|liver (enzyme activity|homogenate)|leukocyte pellet|explant|aspirate|lymph node|"
                    r"electron microscop|immunofluorescence on|direct immunofluorescence", re.I)
ROUTINE = re.compile(r"^(?:serum |plasma |blood |urine |urinary |elevated |low |reduced |increased |decreased |raised |high |"
                     r"mildly |markedly |total |fasting |random |spot )*"
                     r"(complete blood count|full blood count|\bCBC\b|blood count|hemoglobin|haemoglobin|hematocrit|"
                     r"platelet count|platelets|thrombocytopenia|anemia|anaemia|leukocyte count|white (blood )?cell count|"
                     r"neutrophil count|lymphocyte count|leukocytosis|neutropenia|lymphopenia|eosinophil(ia| count)|"
                     r"erythrocyte sedimentation|\bESR\b|c-reactive protein|\bCRP\b|creatinine|\bBUN\b|blood urea|urea|"
                     r"electrolytes|sodium|potassium|chloride|bicarbonate|glucose|calcium|phosph(ate|orus)|magnesium|"
                     r"albumin|total protein|bilirubin|\bALT\b|\bAST\b|aminotransferase|transaminase|alkaline phosphatase|"
                     r"\bALP\b|gamma-glutamyl|\bGGT\b|liver function|liver enzymes|lactate dehydrogenase|\bLDH\b|"
                     r"creatine kinase|\bCK\b|creatine phosphokinase|ferritin|lactate|lactic acid|ammonia|uric acid|"
                     r"urate|cholesterol|triglyceride|lipid|urinalysis|proteinuria|hematuria|basic metabolic|"
                     r"comprehensive metabolic|metabolic panel|renal function|kidney function|routine)", re.I)
PLATFORM = re.compile(r"organic[- ]acid|amino[- ]acid|acylcarnitine|acylglycine|newborn|dried[- ]blood|tandem mass|"
                      r"metabolic (screen|profil|work)|biochemical (screen|profil)|metabolite (screen|panel|profil)|"
                      r"purine|pyrimidine|transferrin (isoform|isoelectric|glycoform|glycosyl)|isoelectric focusing|"
                      r"glycan|oligosacchar|glycosaminoglycan|carbohydrate-deficient transferrin|apolipoprotein C-III|"
                      r"metabolom|sterol (profil|analys)|bile acid profil|steroid (profil|metabolite profil)|"
                      r"peroxisomal (metabolite|screen|metabolic)", re.I)

DEFAULT = {
    "ROUTINE?": ("ROUTINE_NONSPECIFIC", "routine non-specific laboratory measure, not the defining test"),
    "TISSUE_REQUIRED?": ("TISSUE_REQUIRED", "test identity names tissue, marrow, biopsy or cultured cells"),
    "INFECTIOUS_AGENT": ("INFECTIOUS_AGENT", "pathogen-directed test (culture, antigen, nucleic acid or pathogen-specific serology)"),
    "INFECTIOUS_AGENT?": ("INFECTIOUS_AGENT", "pathogen-directed test"),
    "IN_INFECTIOUS_ENTRY": ("NOT_PRIMARY_ROUTE", "host-response marker in an infectious-disease entry; the route is pathogen detection"),
    "CHECK_SOMATIC_OR_GERMLINE": ("GERMLINE_SEQUENCING", "genetic test of constitutional DNA"),
    "GERMLINE_SEQUENCING?": ("GERMLINE_SEQUENCING", "genetic test of constitutional DNA"),
}
COLS = ["disease", "test", "decision", "reason", "first_or_improvement", "specimen_check"]


def provisional(r: dict, infectious: set[str]) -> str:
    ident = f"{r['row_name']} | {r['diagnosis_term_label'] or r['biomarker_term_label']}"
    if r["is_genetic"] == "TRUE" and r["somatic_variant"] == "TRUE" and GERMLINE.search(ident):
        return "CHECK_SOMATIC_OR_GERMLINE"
    if GERMLINE.search(ident):
        return "GERMLINE_SEQUENCING?"
    if TISSUE.search(ident):
        return "TISSUE_REQUIRED?"
    if r["disease_name"] in infectious and INFECT.search(ident):
        return "INFECTIOUS_AGENT"
    if INFECT.search(ident):
        return "INFECTIOUS_AGENT?"
    if r["disease_name"] in infectious:
        return "IN_INFECTIOUS_ENTRY"
    if ROUTINE.search(r["row_name"].strip()):
        return "ROUTINE?"
    return "JUDGE"


def load_tables() -> tuple[dict, dict, set]:
    ov = {}
    for f in sorted(HERE.glob("ov*.txt")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                i, code, amb, foi, detail = line.split("|", 4)
                ov[int(i)] = (code, amb == "1", foi, detail)
    wrong = dict((int(i), d) for i, d in (l.split("|", 1) for l in
                 (HERE / "wrong.txt").read_text(encoding="utf-8").splitlines() if l.strip()))
    infectious = {l.strip() for l in (HERE / "infectious_names.txt").read_text(encoding="utf-8").splitlines() if l.strip()}
    return ov, wrong, infectious


def build() -> tuple[str, str, list[dict]]:
    with open(EXP / "frame.tsv", newline="", encoding="utf-8") as f:
        flagged = [r for r in csv.DictReader(f, delimiter="\t") if r["flag_nongenetic_specimen"] == "TRUE"]
    if len(flagged) != FLAGGED_ROWS:
        sys.exit(f"frame.tsv has {len(flagged)} flagged rows, expected {FLAGGED_ROWS}; "
                 "the judgment indices no longer line up")
    ov, wrong, infectious = load_tables()
    out = []
    for i, r in enumerate(flagged):
        p = provisional(r, infectious)
        tag = "judged"
        if i in ov:
            code, amb, foi, detail = ov[i]
        elif p in DEFAULT:
            (code, detail), amb, foi, tag = DEFAULT[p], False, "NA", "rule"
        elif PLATFORM.search(f"{r['row_name']} {r['diagnosis_term_label'] or r['biomarker_term_label']}"):
            code, amb, foi, tag = "NOT_DATABLE", False, "NA", "rule"
            detail = ("multi-analyte profiling platform shared across many disorders, "
                      "not a disease-specific test datable to one primary publication")
        else:
            code, amb, foi, tag = "NOT_PRIMARY_ROUTE", False, "NA", "scanned-default"
            detail = ("not identified as a post-1985 primary diagnostic route: a supportive, characterizing, "
                      "monitoring or research marker, or a long-established analyte")
        spec = "NA"
        if r["specimen_basis"] == "IMPLICIT":
            spec = "WRONG_SPECIMEN" if i in wrong else "CONFIRMED"
            if i in wrong:
                code, amb, foi, tag = "WRONG_SPECIMEN", False, "NA", "judged"
                detail = f"implicit class {r['implicit_class']} assumed blood, but {wrong[i]}"
        decision = "INCLUDE" if code == "INCLUDE" else "EXCLUDE"
        label = "PRIMARY_ROUTE" if code == "INCLUDE" else code
        amb = amb and decision == "EXCLUDE"
        out.append(dict(disease=r["disease_name"], test=r["row_name"], decision=decision,
                        reason=f"{label}{' (ambiguous)' if amb else ''}: {detail} [{tag}]",
                        first_or_improvement=foi if decision == "INCLUDE" else "NA",
                        specimen_check=spec, _code=label, _amb=amb, _ic=r["implicit_class"]))
    for d, t in KB_GAPS:
        out.append(dict(disease=d, test=t, decision="EXCLUDE", reason="KB_GAP: test not recorded in dismech",
                        first_or_improvement="NA", specimen_check="NA", _code="KB_GAP", _amb=False, _ic=""))

    def tsv(rows: list[list[str]]) -> str:
        buf = io.StringIO()
        csv.writer(buf, delimiter="\t", lineterminator="\n").writerows(rows)
        return buf.getvalue()

    elig = tsv([COLS] + [[o[c] for c in COLS] for o in out])
    inc = [o for o in out if o["decision"] == "INCLUDE"]
    sampled = {id(o) for o in random.Random(SEED).sample(inc, round(0.2 * len(inc)))}
    review = tsv([COLS + ["review_basis"]] +
                 [[o[c] for c in COLS] + ["SAMPLED_INCLUDE" if id(o) in sampled else "AMBIGUOUS_EXCLUDE"]
                  for o in out if id(o) in sampled or o["_amb"]])
    return elig, review, out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="compare with the committed files instead of writing; exit 1 on any difference")
    a = ap.parse_args()
    elig, review, out = build()
    targets = {EXP / "eligibility.tsv": elig, EXP / "eligibility_review.tsv": review}
    if a.check:
        bad = [p.name for p, text in targets.items() if p.read_bytes() != text.encode("utf-8")]
        print("differs: " + ", ".join(bad) if bad else "both files byte-identical to the committed versions")
        sys.exit(1 if bad else 0)
    for p, text in targets.items():
        p.write_bytes(text.encode("utf-8"))
    c = collections.Counter((o["decision"], o["_code"]) for o in out)
    for (d, code), n in sorted(c.items()):
        print(f"{d}\t{code}\t{n}")
    print("WRONG_SPECIMEN by implicit_class:",
          dict(collections.Counter(o["_ic"] for o in out if o["specimen_check"] == "WRONG_SPECIMEN")))


if __name__ == "__main__":
    main()
