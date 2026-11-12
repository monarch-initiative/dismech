"""Merge the two dating agents' results into dating.tsv, dating_flags.tsv and
dating_spotcheck.tsv.

Inputs:
  cases.tsv                             one row per case
  dating_checks/agentA.checked.tsv      check_dating.py run on dating.agentA.tsv
  dating_checks/agentB.checked.tsv      check_dating.py run on dating.agentB.tsv

A case's discovery PMID is ACCEPTED only when both agents give the same PMID and
both agents' quotes pass (quote_ok TRUE). Its discovery_date and date_precision
are check_dating.py's, read from PubMed; cutoff_date is 31 December of the year
before discovery_date.

dating_flags.tsv lists every case that needs a person: the agents disagree, a
quote failed, or an earlier paper looks like the real discovery report. The
assessments in FLAG_NOTES were written after reading the abstracts.
earlier_pmids is the main source of earlier candidates. A few came from
targeted searches when the earlier_pmids query (the entry's own name) missed
an expected report; each flag says which. An ACCEPTED case that carries such a
flag has dating_status ACCEPTED_FLAGGED, and its cutoff should not be used
until the flag is resolved.

mechanistic_readiness is "yes PMID:N" when a paper dated on or before the
cutoff links the molecule the test reads to the disease's mechanism, so that a
curator working only from pre-cutoff literature could have proposed the test;
"no" when the searches found none. These are judgments, listed in READINESS.
The script checks every cited PMID's PubMed date is on or before the cutoff.
Bookshelf chapters (GeneReviews and similar) are never used: PubMed dates them
1993, the start of the book series, whatever their real publication date.
Readiness is given only for cases with a cutoff, i.e. ACCEPTED or
ACCEPTED_FLAGGED.

dating_spotcheck.tsv is a seeded 20% sample (seed 20261111) of the unflagged
ACCEPTED cases.

Usage:
    python experiments/diagnostic_retrodiction/build_dating.py   # needs NCBI_API_KEY
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import random
import sys
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261111

# (disease, test) -> (flag_type, candidate_pmid or "", candidate_source, assessment)
FLAG_NOTES = {
    ("Acquired Thrombotic Thrombocytopenic Purpura", "ADAMTS13 activity"): (
        "DISAGREE", "", "",
        "A's 9531594 (Blood, Apr 1998) is a case report of acquired protease deficiency with an IgG "
        "inhibitor; B's 9828245 (NEJM, Nov 1998) is the multicentre study. earlier_pmids also offers "
        "10097823 (Bailliere's, Jun 1998, four chronic relapsing cases). A's is the earliest primary "
        "report. All three are 1998, so the cutoff is 1997-12-31 whichever is chosen."),
    ("Childhood Absence Epilepsy", "CSF glucose (hypoglycorrhachia)"): (
        "DISAGREE", "", "",
        "A's 20621801 (2010) is a twin case report with absence epilepsy and a moderately low CSF/serum "
        "glucose ratio; B's 10592074 (1999) is two GLUT1-deficiency children with atypical absences. "
        "Neither establishes the test in a childhood absence epilepsy cohort. Unresolved; needs a "
        "targeted search for the first cohort report."),
    ("Heparin-Induced Thrombocytopenia", "anti-PF4/heparin IgG immunoassay"): (
        "DISAGREE", "1514184", "targeted search",
        "A's 8282825 (JCI, Jan 1994) shows patient antibodies bind immobilised heparin/PF4 complexes; "
        "B's 8191560 (Transfusion, May 1994) compares the PF4/heparin ELISA with functional tests, and "
        "lists A's paper among its own earlier hits. A targeted search found 1514184 (Amiral, Thromb "
        "Haemost 1992, letter), 'Platelet factor 4 complexed to heparin is the target for antibodies "
        "generated in heparin-induced thrombocytopenia', which likely precedes both. It has no "
        "abstract, so its content is not verified here. Cutoff 1993-12-31 (agents) vs 1991-12-31."),
    ("Optic Neuritis", "MOG-IgG"): (
        "DISAGREE", "", "",
        "A's 22204662 (Mader, Dec 2011) tested MOG-IgG by cell-based assay in NMO and high-risk NMO, "
        "explicitly including recurrent optic neuritis; B's 22371853 (Rostasy, 2012) is the first "
        "optic-neuritis-only cohort. A's is earlier and covers the subset. Cutoff 2010 vs 2011."),
    ("Optic Neuritis", "AQP4-IgG"): (
        "DISAGREE", "15589308", "earlier_pmids (agent B)",
        "A's 15589308 (Lennon 2004) tested NMO and 'syndromes that suggest high risk', which include "
        "recurrent optic neuritis; it appears in B's own earlier_pmids. B's 18434643 (Matiello 2008) is "
        "a prognostic study in recurrent ON. A's is the real discovery report. Cutoff 2003 vs 2007."),
    ("Transverse Myelitis", "AQP4-IgG"): (
        "DISAGREE", "15589308", "earlier_pmids (agent B)",
        "As for optic neuritis: Lennon 2004 (A) included high-risk syndromes such as longitudinally "
        "extensive myelitis and appears in B's earlier_pmids; B's 16453327 (Weinshenker 2006) is a "
        "prognostic LETM study. A's is the real discovery report. Cutoff 2003 vs 2005."),
    ("Paroxysmal Nocturnal Hemoglobinuria", "flow cytometry for GPI-anchored proteins"): (
        "DISAGREE", "", "",
        "A's 3845321 (Kinoshita, NEJM 1985) used cytofluorographic analysis with anti-DAF and found "
        "antigen-deficient granulocyte/monocyte subpopulations absent in other diseases: the first flow "
        "report. B's 8652849 (Hall & Rosse 1996) established CD55/CD59 flow as the diagnostic test. The "
        "1983 papers in earlier_pmids (6576376, 6225118) used immunoprecipitation, not flow. Under rule "
        "5, A. Cutoff 1984-12-31 vs 1995-12-31."),
    ("Statin Toxicity", "anti-HMGCR antibodies"): (
        "DISAGREE", "", "",
        "A's 20496415 (Christopher-Stine 2010) first reported the autoantibody, to 200/100-kd proteins, by "
        "immunoprecipitation; B's 21360500 (Mammen 2011) identified the antigen as HMGCR and introduced "
        "the ELISA. The same antibody, first detectable in 2010; whether 'the test' is the antibody or "
        "the anti-HMGCR assay is a judgment. Cutoff 2009 vs 2010."),
    ("Stiff Person Syndrome", "anti-amphiphysin antibodies"): (
        "DISAGREE", "", "",
        "A's 8381208 (Folli, NEJM Feb 1993) reported the autoantibody to a 128-kd synaptic protein; B's "
        "8245793 (De Camilli, J Exp Med Dec 1993) identified it as amphiphysin. Both 1993, so the "
        "cutoff is 1992-12-31 either way; A's is the first report of the antibody."),
    ("Stiff Person Syndrome", "anti-glycine receptor antibodies"): (
        "DISAGREE", "18852446", "targeted search",
        "A's 21148607 (Mas 2011) opens by saying GlyR antibodies 'were reported in a patient with PERM'; "
        "B's 23090334 (McKeon 2013) is a later spectrum study. A targeted search found 18852446 "
        "(Hutchinson, Neurology 2008), 'Progressive encephalomyelitis, rigidity, and myoclonus: a novel "
        "glycine receptor antibody', which is that original report. Neither agent's paper is the "
        "discovery. Cutoff 2007-12-31 if Hutchinson is right."),
    ("Celiac Disease", "anti-tissue transglutaminase IgA"): (
        "EARLIER_DISCOVERY_CANDIDATE", "9212111", "earlier_pmids (both agents)",
        "Both agents chose 9836104 (Ital J Gastroenterol, Oct 1998), a screening study. 9212111 "
        "(Dieterich, Nat Med Jul 1997) identified tTG as the endomysial autoantigen and, per the Gut "
        "commentary 9391261, already showed raised IgA by tTG ELISA in coeliac sera and not controls. "
        "That is the discovery report. Cutoff 1997-12-31 vs 1996-12-31."),
    ("Barth syndrome", "monolysocardiolipin:cardiolipin ratio"): (
        "EARLIER_DISCOVERY_CANDIDATE", "15805542", "earlier_pmids (both agents)",
        "Both agents chose 16873891 (Houtkooper 2006), which measured MLCL/CL in cultured skin "
        "fibroblasts, not an accessible specimen. 15805542 (Valianpour 2005) found MLCL accumulation in "
        "patients' lymphocytes, among other tissues: the earlier, blood-based report, though its "
        "abstract gives no ratio. Cutoff 2005-12-31 vs 2004-12-31."),
    ("Smith-Lemli-Opitz syndrome", "serum 7-dehydrocholesterol"): (
        "EARLIER_DISCOVERY_CANDIDATE", "7684480", "targeted search; 8256825 in earlier_pmids",
        "Both agents chose 8259166 (Tint, NEJM Jan 1994). earlier_pmids has 8256825 (Tint, Am J Med "
        "Genet letter, Sep 1993), and a targeted search found 7684480 (Irons, Lancet letter, May 1993), "
        "'Defective cholesterol biosynthesis in Smith-Lemli-Opitz syndrome'. Both are letters without "
        "abstracts, so their content is not verified here, but by title both report the defect before "
        "the NEJM paper. Cutoff 1993-12-31 vs 1992-12-31."),
    ("Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect", "erythrocyte plasmalogens"): (
        "EARLIER_DISCOVERY_CANDIDATE", "4010717", "targeted search",
        "Both agents chose 1955304 (1991), a case report that cites erythrocyte plasmalogens as how the "
        "child was diagnosed: not a discovery report. A targeted search found 4010717 (Heymans, NEJM "
        "1985, letter), 'Rhizomelic chondrodysplasia punctata: another peroxisomal disorder', and "
        "2452243 (Hoefler 1988, 'Biochemical abnormalities in RCDP'). The earlier_pmids query missed "
        "both because it searched the entry's own name. Heymans has no abstract to verify. Cutoff "
        "1990-12-31 vs 1984-12-31."),
    ("Rhizomelic Chondrodysplasia Punctata Type 1", "erythrocyte plasmalogens"): (
        "EARLIER_DISCOVERY_CANDIDATE", "4010717", "targeted search",
        "Same as the plasmalogen-synthesis-defect row: agents' 1955304 is a 1991 case report; Heymans "
        "1985 (4010717) is the likely discovery report."),
    ("Rhizomelic Chondrodysplasia Punctata Type 5", "erythrocyte plasmalogens"): (
        "EARLIER_DISCOVERY_CANDIDATE", "4010717", "targeted search",
        "Same as the plasmalogen-synthesis-defect row: agents' 1955304 is a 1991 case report; Heymans "
        "1985 (4010717) is the likely discovery report."),
}

# (disease, test) -> "no" or a PMID (string) supporting "yes"
READINESS = {
    ("Alzheimer Disease", "plasma p-tau217"): "21342022",
    ("Alzheimer Disease", "CSF amyloid-beta 42"): "7699397",
    ("Anti-NMDA Receptor Encephalitis", "anti-NMDA receptor IgG (serum and CSF)"): "16407105",
    ("Autoimmune Polyendocrine Syndrome Type 1", "anti-interferon-omega autoantibodies"): "no",
    ("Autoimmune Pulmonary Alveolar Proteinosis", "anti-GM-CSF autoantibodies"): "8171324",
    ("Barth syndrome", "monolysocardiolipin:cardiolipin ratio"): "15805542",
    ("Canavan disease", "urinary N-acetylaspartic acid"): "no",
    ("Celiac Disease", "anti-tissue transglutaminase IgA"): "9212111",
    ("Chronic Inflammatory Demyelinating Polyneuropathy", "anti-neurofascin antibodies"): "21267074",
    ("Chronic Inflammatory Demyelinating Polyneuropathy", "anti-contactin-1 antibodies"): "21267074",
    ("Congenital Thrombotic Thrombocytopenic Purpura", "ADAMTS13 activity"): "2665869",
    ("Dermatomyositis", "anti-MDA5 antibodies"): "no",
    ("Dyskeratosis Congenita Autosomal Recessive 2", "leukocyte telomere length by flow-FISH"): "16822458",
    ("Dyskeratosis Congenita Autosomal Recessive 6", "leukocyte telomere length by flow-FISH"): "16822458",
    ("Glomerulonephritis", "anti-PLA2R antibodies"): "16159900",
    ("Immunodeficiency 18", "TREC newborn screening"): "11715066",
    ("Immunodeficiency 19", "TREC newborn screening"): "11715066",
    ("Inherited Aplastic Anemia", "leukocyte telomere length by flow-FISH"): "16822458",
    ("Late-Onset Pompe Disease", "dried-blood-spot acid alpha-glucosidase activity"): "7603530",
    ("Limbic Encephalitis", "anti-LGI1 antibodies"): "17395141",
    ("Limbic Encephalitis", "anti-CASPR2 antibodies"): "17395141",
    ("Limbic Encephalitis", "anti-GABAB receptor antibodies"): "no",
    ("Limbic Encephalitis", "anti-AMPA receptor antibodies"): "17262855",
    ("Lymphangioleiomyomatosis", "serum VEGF-D"): "15252306",
    ("MOGAD", "MOG-IgG cell-based assay"): "16934337",
    ("Membranous nephropathy", "anti-PLA2R antibodies"): "16159900",
    ("Menkes Disease", "plasma DOPA:DHPG ratio"): "3233105",
    ("Mitochondrial Neurogastrointestinal Encephalomyopathy", "leukocyte thymidine phosphorylase activity"): "no",
    ("Mitochondrial Neurogastrointestinal Encephalomyopathy", "plasma thymidine and deoxyuridine"): "9924029",
    ("Myasthenia Gravis", "anti-MuSK antibodies"): "3352902",
    ("Narcolepsy-Cataplexy Syndrome", "CSF hypocretin-1"): "10481909",
    ("Narcolepsy", "CSF hypocretin-1"): "10481909",
    ("Neurohypophyseal Diabetes Insipidus", "plasma copeptin (hypertonic-saline stimulated)"): "17426098",
    ("Neuromyelitis Optica Spectrum Disorder with Anti-AQP4 Antibodies", "AQP4-IgG"): "no",
    ("Neuronal Ceroid Lipofuscinosis 2", "TPP1 enzyme activity"): "9295267",
    ("Paroxysmal Dyskinesia", "CSF glucose (hypoglycorrhachia)"): "16149086",
    ("Polycythemia Vera", "JAK2 V617F"): "15102479",
    ("Primary Bile Acid Malabsorption", "serum 7-alpha-hydroxy-4-cholesten-3-one (C4)"): "3181435",
    ("Pyridoxine-Dependent Epilepsy", "alpha-aminoadipic semialdehyde"): "15944906",
    ("Revesz Syndrome", "leukocyte telomere length by flow-FISH"): "16822458",
    ("Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect", "erythrocyte plasmalogens"): "2452243",
    ("Rhizomelic Chondrodysplasia Punctata Type 1", "erythrocyte plasmalogens"): "2452243",
    ("Rhizomelic Chondrodysplasia Punctata Type 5", "erythrocyte plasmalogens"): "2452243",
    ("Severe Combined Immunodeficiency", "TREC newborn screening"): "11715066",
    ("Smith-Lemli-Opitz syndrome", "serum 7-dehydrocholesterol"): "7684480",
    ("Stiff Person Syndrome", "anti-GAD65 antibodies"): "7271246",
    ("X-Linked Nephrogenic Diabetes Insipidus", "basal plasma copeptin"): "11091117",
}


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, cols: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def pubmed_dates(pmids: list[str]) -> dict[str, dict]:
    key = os.environ.get("NCBI_API_KEY", "").strip()
    if not key:
        sys.exit("NCBI_API_KEY is not set; it is needed to check readiness PMIDs' dates.")
    body = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(pmids), "retmode": "json",
                                   "tool": "dismech-retrodiction", "api_key": key}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi", data=body), timeout=60) as r:
            res = json.load(r)["result"]
    except Exception as e:  # type only: the request body carries the key
        sys.exit(f"esummary failed ({type(e).__name__})")
    return {u: res[u] for u in res.get("uids", [])}


def earliest_date(summary: dict) -> dt.date | None:
    """Earliest of PubMed's pubdate and epubdate, filling a missing month/day with 1."""
    months = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
    out = []
    for field in ("pubdate", "epubdate"):
        parts = (summary.get(field) or "").split()
        if parts and parts[0][:4].isdigit():
            y = int(parts[0][:4])
            m = months.get(parts[1][:3].lower(), 1) if len(parts) > 1 else 1
            d = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 1
            out.append(dt.date(y, m, d))
    return min(out) if out else None


def main() -> None:
    key = lambda r: (r["disease"], r["test"])
    cases = read_tsv(HERE / "cases.tsv")
    a = {key(r): r for r in read_tsv(HERE / "dating_checks" / "agentA.checked.tsv")}
    b = {key(r): r for r in read_tsv(HERE / "dating_checks" / "agentB.checked.tsv")}
    if {key(c) for c in cases} != set(a) or set(a) != set(b):
        sys.exit("agent files do not cover exactly the cases in cases.tsv")
    unknown = set(FLAG_NOTES) - set(a)
    if unknown:
        sys.exit(f"FLAG_NOTES names unknown cases: {sorted(unknown)}")

    rows, flags = [], []
    for c in cases:
        k = key(c)
        ra, rb = a[k], b[k]
        pa, pb = (r["discovery_pmid"].replace("PMID:", "").strip() for r in (ra, rb))
        both_quotes = ra["quote_ok"] == "TRUE" and rb["quote_ok"] == "TRUE"
        accepted = pa == pb and both_quotes and ra["pubmed_date"] != "NA"
        note = FLAG_NOTES.get(k)
        if accepted and note and note[0] != "EARLIER_DISCOVERY_CANDIDATE":
            sys.exit(f"{k}: accepted, but flagged as {note[0]}")
        if not accepted and not note:
            kind = "DISAGREE" if pa != pb else "QUOTE_FAIL"
            sys.exit(f"{k}: {kind} with no assessment in FLAG_NOTES")
        status = "NOT_ACCEPTED" if not accepted else ("ACCEPTED_FLAGGED" if note else "ACCEPTED")

        row = {"disease": c["disease"], "mondo_id": c["mondo_id"], "test": c["test"], "subset": c["subset"],
               "test_class": c["test_class"], "test_group": c["test_group"], "analyte": ra["analyte"],
               "discovery_pmid": "NA", "discovery_date": "NA", "date_precision": "NA", "cutoff_date": "NA",
               "mechanistic_readiness": "NA", "first_or_improvement": c["first_or_improvement"],
               "quote_ok": "TRUE" if both_quotes else "FALSE", "dating_status": status, "case_id": c["case_id"]}
        if accepted:
            d = dt.date.fromisoformat(ra["pubmed_date"])
            row.update(discovery_pmid=f"PMID:{pa}", discovery_date=ra["pubmed_date"],
                       date_precision=ra["date_precision"], cutoff_date=f"{d.year - 1}-12-31")
            if k not in READINESS:
                sys.exit(f"{k}: accepted but has no READINESS judgment")
            row["mechanistic_readiness"] = "no" if READINESS[k] == "no" else f"yes PMID:{READINESS[k]}"
        rows.append(row)
        if note:
            flag_type, cand, source, assessment = note
            flags.append({"case_id": c["case_id"], "disease": c["disease"], "test": c["test"],
                          "flag_type": flag_type, "dating_status": status,
                          "agentA_pmid": f"PMID:{pa}", "agentA_date": ra["pubmed_date"], "agentA_quote_ok": ra["quote_ok"],
                          "agentB_pmid": f"PMID:{pb}", "agentB_date": rb["pubmed_date"], "agentB_quote_ok": rb["quote_ok"],
                          "candidate_pmid": f"PMID:{cand}" if cand else "", "candidate_source": source,
                          "assessment": assessment})

    # readiness PMIDs must predate the cutoff
    cited = sorted({v for v in READINESS.values() if v != "no"})
    summaries = pubmed_dates(cited)
    bad = []
    for r in rows:
        ready = r["mechanistic_readiness"]
        if ready.startswith("yes"):
            pm = ready.split(":")[1]
            s = summaries.get(pm)
            if s is None:
                bad.append(f"{r['disease']}: PMID {pm} not found")
                continue
            if "Bookshelf" in (s.get("pubtype") or []) or s.get("booktitle"):
                bad.append(f"{r['disease']}: PMID {pm} is a Bookshelf record")
            d = earliest_date(s)
            if d is None or d > dt.date.fromisoformat(r["cutoff_date"]):
                bad.append(f"{r['disease']}: PMID {pm} dated {d}, after cutoff {r['cutoff_date']}")
    if bad:
        sys.exit("readiness PMID check failed:\n  " + "\n  ".join(bad))

    cols = ["disease", "mondo_id", "test", "subset", "test_class", "test_group", "analyte", "discovery_pmid",
            "discovery_date", "date_precision", "cutoff_date", "mechanistic_readiness", "first_or_improvement",
            "quote_ok", "dating_status", "case_id"]
    write_tsv(HERE / "dating.tsv", cols, rows)
    write_tsv(HERE / "dating_flags.tsv", list(flags[0].keys()), flags)
    unflagged = [r for r in rows if r["dating_status"] == "ACCEPTED"]
    sample = random.Random(SEED).sample(unflagged, round(0.2 * len(unflagged)))
    sample_ids = {r["case_id"] for r in sample}
    write_tsv(HERE / "dating_spotcheck.tsv", cols, [r for r in rows if r["case_id"] in sample_ids])

    from collections import Counter
    print("dating_status:", dict(Counter(r["dating_status"] for r in rows)))
    print("flags:", dict(Counter(f["flag_type"] for f in flags)))
    print("readiness:", dict(Counter(r["mechanistic_readiness"].split()[0] for r in rows)))
    print(f"spot-check: {len(sample)} of {len(unflagged)} unflagged accepted cases:",
          ", ".join(f"{r['case_id']} {r['disease']}" for r in rows if r["case_id"] in sample_ids))


if __name__ == "__main__":
    main()
