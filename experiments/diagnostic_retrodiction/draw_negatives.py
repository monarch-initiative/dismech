"""Draw the expanded negative controls, assign their cutoffs, and check their literature.

Pool: coverage.tsv rows with frame_flagged_rows 0 (no frame row flagged as an
accessible, non-germline test) and n_measurable >= 1 (at least one pathograph
node passing the coverage audit's measurable-node rule), leaving out the six
original negatives, sorted by kb_file. The pool does not read coverage.tsv's
``source`` column, so rerunning coverage_audit/audit.py with the drawn
diseases in negatives.tsv (which relabels them NEGATIVE) does not change it.

Draw: one random.Random(SEED) stream. Its first call,
rng.sample(pool, N_DRAW), is the original draw of 12 (negatives N07-N18 in
order). Each later draw continues the same stream with rng.choice over the
pool entries not yet drawn, sorted by kb_file. A drawn disease is replaced by
the next draw when it is listed in REPLACED, or when it fails the literature
check at its slot's cutoff. A replacement takes the slot (Nnn) of the disease
it replaces, and with it that slot's cutoff.

Cutoffs: each negative slot N01-N18 takes the cutoff of one test case. The
slot-to-case assignment was drawn once (2026-11-16) with
random.Random(SEED).sample(test cases sorted by case_id, 18), one case per
slot in slot order, and is frozen in SLOT_CASE, so later changes to the test
set do not reshuffle the slots. A slot reads its case's current cutoff from
dating.tsv, so a re-dated case moves its slot's cutoff. This is a provisional
reading of the decision "the cutoff of a seeded random matched test case": no
matching criterion has been defined yet, so the draw is unmatched (README,
Decisions).

Screen: a drawn disease is rejected, and its slot redrawn, when its standard
diagnostic criteria include an accessible-specimen test (screen()):
  - an item of its kb entry's diagnosis[] or definitions[] (pinned commit)
    that census.classify flags as a non-germline accessible-specimen test;
  - a measurable node whose own description calls it diagnostic, a criterion
    or a screening test;
  - a recorded judgment in SCREEN_JUDGMENT, for criteria the entry does not
    record.

Literature check: check_pretest_era.py on each negative at its slot's cutoff,
with the same query construction and packet_minimum as the cases. A negative
below packet_minimum is INSUFFICIENT_PRE_CUTOFF_LITERATURE and its slot is
redrawn (drawn slots only; an original negative that fails is reported).

Usability for the primary H3 analysis is a judgment per disease (USABILITY
below), made by reading each drawn disease's measurable nodes.

Writes negatives.tsv, negatives_replaced.tsv and negatives_literature_check.tsv.
NCBI_API_KEY is needed by check_pretest_era.py.

Usage:
    uv run python experiments/diagnostic_retrodiction/draw_negatives.py
"""
import csv
import json
import re
import random
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import census  # noqa: E402
SEED = 20261114
N_DRAW = 12
ORIGINAL = [  # (disease, kb_file)
    ("Hypermobile Ehlers-Danlos Syndrome", "kb/disorders/Hypermobile_Ehlers-Danlos_Syndrome.yaml"),
    ("Kawasaki Disease", "kb/disorders/Kawasaki_Disease.yaml"),
    ("Sarcoidosis", "kb/disorders/Sarcoidosis.yaml"),
    ("Behcet's Disease", "kb/disorders/Behcets_Disease.yaml"),
    ("Complex Regional Pain Syndrome Type 1", "kb/disorders/Complex_Regional_Pain_Syndrome_Type_1.yaml"),
    ("Takayasu Arteritis", "kb/disorders/Takayasu_Arteritis.yaml"),
]
ORIGINAL_FILES = {f for _, f in ORIGINAL}

# Drawn diseases replaced by decision, with the reason.
REPLACED = {
    "kb/disorders/Maculopapular_Cutaneous_Mastocytosis.yaml":
        "replaced by the experimenter (2026-11-16): slot N12 redrawn",
    "kb/disorders/SRD5A3-Congenital_Disorder_of_Glycosylation.yaml":
        "replaced by the experimenter (2026-11-16): slot N13 redrawn",
}

NO_NODE = "no measurable node (coverage audit NO_MEASURABLE_NODE)"
# kb_file -> (h3_usable, basis, monogenic_germline). Every negative needs an entry.
USABILITY = {
    "kb/disorders/Hypermobile_Ehlers-Danlos_Syndrome.yaml": ("no", NO_NODE, "no"),
    "kb/disorders/Kawasaki_Disease.yaml": ("yes", "measurable nodes are nonspecific inflammation and blood counts; "
                                                  "accessible but not confirmatory", "no"),
    "kb/disorders/Sarcoidosis.yaml": ("yes", "measurable node is a nonspecific blood count; accessible but not "
                                             "confirmatory", "no"),
    "kb/disorders/Behcets_Disease.yaml": ("no", NO_NODE, "no"),
    "kb/disorders/Complex_Regional_Pain_Syndrome_Type_1.yaml": ("no", NO_NODE, "no"),
    "kb/disorders/Takayasu_Arteritis.yaml": ("yes", "measurable node is ESR; accessible but not confirmatory", "no"),
    "kb/disorders/Blepharophimosis_Intellectual_Disability_Syndrome_MKB_Type.yaml": (
        "no", "only measurable node is a serum-stimulation response of patient lymphoblastoid cells in culture, "
              "not a measurement in an accessible specimen", "yes"),
    "kb/disorders/Choroid_Plexus_Neoplasm.yaml": (
        "no", "only measurable node is CSF overproduction by tumour epithelium, a process no assay measures "
              "(listed as spurious in coverage_audit/FINDINGS.md)", "no"),
    "kb/disorders/Maculopapular_Cutaneous_Mastocytosis.yaml": ("yes", "serum tryptase; supportive, not confirmatory", "no"),
    "kb/disorders/SRD5A3-Congenital_Disorder_of_Glycosylation.yaml": (
        "yes", "serum transferrin glycoform pattern; the entry calls it the group screening test but not a "
               "reliable diagnostic", "yes"),
    "kb/disorders/Angiomatoid_Fibrous_Histiocytoma.yaml": ("yes", "nonspecific inflammatory markers", "no"),
}
for _f, _node in [  # drawn diseases whose node is a nonspecific accessible readout (judged 2026-11-16)
        ("Dystroglycanopathy", "elevated serum creatine kinase"),
        ("Mitochondrial_DNA_Depletion_Syndrome_17", "low plasma citrulline"),
        ("NAD_P_HX_Epimerase_Deficiency", "increased CSF lactate"),
        ("Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant", "elevated serum creatine kinase"),
        ("Lung_Disease_Immunodeficiency_and_Chromosome_Breakage_Syndrome",
         "decreased vaccine antibody response; increased IgM"),
        ("Inclusion_Body_Myopathy_with_Paget_Disease_of_Bone_and_Frontotemporal_Dementia",
         "elevated circulating creatine kinase"),
        ("Severe_X-linked_Mitochondrial_Encephalomyopathy", "increased CSF lactate")]:
    USABILITY[f"kb/disorders/{_f}.yaml"] = ("yes", "measurable node is a nonspecific accessible-specimen "
                                                   f"readout: {_node}", "yes")
USABILITY.update({  # replacement and redrawn negatives, judged 2026-11-16 from their measurable nodes
    "kb/disorders/Juvenile_Idiopathic_Arthritis.yaml": (
        "yes", "ESR, ANA and serum interferon-gamma are nonspecific accessible readouts; diagnosis is clinical", "no"),
    "kb/disorders/Soil_Transmitted_Helminthiases.yaml": (
        "no", "infectious disease confirmed by stool microscopy, a confirmatory test in a specimen outside the "
              "frame; infectious-agent entries are excluded as cases, so it is not a no-test negative", "no"),
    "kb/disorders/Congenital_Merosin-deficient_Muscular_Dystrophy_1A.yaml": (
        "yes", "measurable node is a nonspecific accessible-specimen readout: elevated serum creatine kinase", "yes"),
    "kb/disorders/Aortitis.yaml": (
        "yes", "ESR is a nonspecific accessible readout (the G-CSF node is not a measurement)", "no"),
    "kb/disorders/Hereditary_Angioedema.yaml": (
        "no", "C1-inhibitor level and function and C4 in plasma are accessible confirmatory tests in clinical use, "
              "so it is not a no-test negative", "yes"),
    "kb/disorders/Kearns-Sayre_Syndrome.yaml": (
        "yes", "CSF protein is a nonspecific accessible readout; the defining lesion is a mitochondrial DNA "
               "deletion, usually sporadic", "no"),
    "kb/disorders/Psoriasis.yaml": ("yes", "leukocytosis is a nonspecific accessible readout; diagnosis is clinical", "no"),
    "kb/disorders/Melanotic_Neuroectodermal_Tumor_of_Infancy.yaml": (
        "yes", "urinary vanillylmandelic acid is accessible and supportive; diagnosis is by biopsy", "no"),
    "kb/disorders/Peeling_Skin_Syndrome.yaml": (
        "yes", "measurable node is a nonspecific accessible-specimen readout: elevated circulating IgE", "yes"),
    "kb/disorders/Deficiency_of_the_Interleukin-1_Receptor_Antagonist.yaml": (
        "yes", "leukocytosis is a nonspecific accessible readout; diagnosis is genetic", "yes"),
    "kb/disorders/Congenital_Hydrocephalus.yaml": (
        "no", "its measurable nodes are CSF secretion and absorption processes, which no assay measures", "no"),
    "kb/disorders/Lipoprotein_Glomerulopathy.yaml": (
        "yes", "raised serum apolipoprotein E is supportive; diagnosis is by renal biopsy", "yes"),
    "kb/disorders/Myofibrillar_Myopathy.yaml": (
        "yes", "elevated serum creatine kinase is nonspecific; diagnosis is by muscle biopsy and genetics", "yes"),
})


def read_tsv(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def pool() -> list[dict]:
    rows = read_tsv(HERE / "coverage.tsv")
    return sorted((r for r in rows if r["frame_flagged_rows"] == "0" and r["n_measurable"]
                   and int(r["n_measurable"]) >= 1 and r["kb_file"] not in ORIGINAL_FILES),
                  key=lambda r: r["kb_file"])


class Drawer:
    def __init__(self) -> None:
        self.pool = pool()
        self.rng = random.Random(SEED)
        self.first = self.rng.sample(self.pool, N_DRAW)
        self.drawn = {r["kb_file"] for r in self.first}

    def next(self) -> dict:
        left = [r for r in self.pool if r["kb_file"] not in self.drawn]
        r = self.rng.choice(left)
        self.drawn.add(r["kb_file"])
        return r


SLOT_CASE = {  # frozen 2026-11-16 from random.Random(SEED).sample(sorted test cases, 18)
    "N01": "C008", "N02": "C022", "N03": "C051", "N04": "C053", "N05": "C041", "N06": "C043",
    "N07": "C012", "N08": "C042", "N09": "C002", "N10": "C039", "N11": "C056", "N12": "C018",
    "N13": "C033", "N14": "C057", "N15": "C001", "N16": "C054", "N17": "C027", "N18": "C028",
}


def slot_cutoffs(n: int) -> list[dict]:
    dating = {r["case_id"]: r for r in read_tsv(HERE / "dating.tsv")}
    test = set((HERE / "test_set.txt").read_text().split())
    out = []
    for i in range(1, n + 1):
        cid = SLOT_CASE[f"N{i:02d}"]
        if cid not in test:
            sys.exit(f"N{i:02d}: matched case {cid} is no longer a test case; redraw its slot's case")
        out.append(dating[cid])
    return out


# Phase 1 uses the slot cutoffs of its first run (2026-11-16), so that it consumes the seeded stream as
# it did then; phase 2 uses each slot's current cutoff (a re-dated case moves it).
PHASE1_CUTOFF = {
    "N01": "1987-12-31", "N02": "2000-12-31", "N03": "1993-12-31", "N04": "1987-12-31", "N05": "2007-12-31",
    "N06": "2004-12-31", "N07": "2011-12-31", "N08": "1984-12-31", "N09": "2019-12-31", "N10": "2010-12-31",
    "N11": "2005-12-31", "N12": "1991-12-31", "N13": "2000-12-31", "N14": "2010-12-31", "N15": "1997-12-31",
    "N16": "1992-12-31", "N17": "2005-12-31", "N18": "2008-12-31",
}


# kb_file -> reason: standard diagnostic criteria with an accessible-specimen test the kb entry does not record
SCREEN_JUDGMENT = {
    "kb/disorders/Aortitis.yaml":
        "the large-vessel vasculitis criteria it falls under include ESR (giant cell arteritis criteria)",
    "kb/disorders/Kearns-Sayre_Syndrome.yaml":
        "the classic diagnostic criteria include CSF protein above 100 mg/dL; mtDNA deletion is also detectable "
        "in blood or urine",
    "kb/disorders/Melanotic_Neuroectodermal_Tumor_of_Infancy.yaml":
        "raised urinary vanillylmandelic acid is part of the standard work-up",
    "kb/disorders/Wiskott_Aldrich_Syndrome.yaml":
        "its diagnostic criteria include thrombocytopenia with small platelets on a blood count and smear",
    "kb/disorders/Cocaine_Intoxication.yaml": "confirmed by urine toxicology",
    "kb/disorders/Primary_Hyperoxaluria_Type_1.yaml": "urinary oxalate (and glycolate) excretion is the standard test",
    "kb/disorders/Staphylococcus_Aureus_Pneumonia.yaml": "confirmed by blood and sputum culture",
    "kb/disorders/Chorea-acanthocytosis.yaml":
        "acanthocytes on a blood smear (and loss of chorein on red-cell western blot) are standard findings",
    "kb/disorders/Shiga_Toxin-Associated_Hemolytic_Uremic_Syndrome.yaml":
        "defined by blood findings (schistocytes, thrombocytopenia) and stool Shiga toxin testing",
}
DIAG_WORDS = re.compile(r"\b(diagnos\w*|criteri\w*|screening)\b", re.I)
_ENTRY_CACHE: dict[str, dict] = {}


def _entry(kb_file: str) -> dict:
    if kb_file not in _ENTRY_CACHE:
        commit = (HERE / "PINNED_COMMIT").read_text().strip()
        out = subprocess.run(["git", "-C", str(HERE), "show", f"{commit}:{kb_file}"],
                             capture_output=True, text=True, check=True).stdout
        _ENTRY_CACHE[kb_file] = yaml.safe_load(out) or {}
    return _ENTRY_CACHE[kb_file]


def screen(kb_file: str, measurable_nodes: str) -> str | None:
    """Reason the disease fails the accessible-test screen, or None."""
    if kb_file in SCREEN_JUDGMENT:
        return "SCREEN (judgment): " + SCREEN_JUDGMENT[kb_file]
    d = _entry(kb_file)
    for sec in ("diagnosis", "definitions"):
        for it in d.get(sec) or []:
            ident = " ".join(str(it.get(k) or "") for k in ("name", "preferred_term"))
            full = " ".join(str(v) for v in it.values() if isinstance(v, str))
            if census.classify(ident, full, [], "", {})["flag_nongenetic_specimen"] == "TRUE":
                return f"SCREEN ({sec}): '{it.get('name', '?')}' is an accessible-specimen test"
    names = {x.strip() for x in measurable_nodes.split(";") if x.strip()}
    for sec in ("pathophysiology", "phenotypes", "biochemical"):
        for it in d.get(sec) or []:
            if it.get("name") in names and DIAG_WORDS.search(str(it.get("description") or "")):
                return f"SCREEN (node): measurable node '{it['name']}' is described as diagnostic"
    return None


LIT_CACHE_FILE = HERE.parents[1] / "tmp" / "negatives_lit_cache.json"
LIT_CACHE: dict[tuple, dict] = {}


def literature(rows: list[dict]) -> dict[str, dict]:
    """check_pretest_era.py on (kb_file, disease, mondo_id, cutoff) rows; returns kb_file -> result row.

    Each (kb_file, cutoff) pair is checked once per run. A disease with no MONDO ID cannot be checked
    and is ruled NO_MONDO_ID, which counts as a failure."""
    todo = []
    for r in rows:
        k = (r["kb_file"], r["cutoff_date"])
        if k in LIT_CACHE:
            continue
        if not r["mondo_id"].startswith("MONDO:"):
            LIT_CACHE[k] = {"kb_file": r["kb_file"], "disease": r["disease"], "cutoff_date": r["cutoff_date"],
                            "lit_count": "NA", "lit_ruling": "NO_MONDO_ID"}
        else:
            todo.append(r)
    if todo:
        LIT_CACHE.update({(r["kb_file"], r["cutoff_date"]): r for r in _run_check(todo)})
        LIT_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        LIT_CACHE_FILE.write_text(json.dumps([[list(k), v] for k, v in LIT_CACHE.items()]))
    return {r["kb_file"]: LIT_CACHE[(r["kb_file"], r["cutoff_date"])] for r in rows}


def _run_check(rows: list[dict]) -> list[dict]:
    with tempfile.TemporaryDirectory() as d:
        inp, out = Path(d) / "in.tsv", Path(d) / "out.tsv"
        write_tsv(inp, [{"kb_file": r["kb_file"], "disease": r["disease"], "test": "NEGATIVE",
                         "mondo_id": r["mondo_id"], "cutoff_date": r["cutoff_date"], "quote_ok": "TRUE",
                         "literature_alias": "NA"} for r in rows])
        subprocess.run([sys.executable, str(HERE / "check_pretest_era.py"), str(inp), "--out", str(out)],
                       check=True, stdout=subprocess.DEVNULL)
        return read_tsv(out)


def main() -> None:
    if LIT_CACHE_FILE.exists():  # gitignored run cache: the same (disease, cutoff) is not re-checked
        LIT_CACHE.update({tuple(k): v for k, v in json.loads(LIT_CACHE_FILE.read_text())})
    cov = {r["kb_file"]: r for r in read_tsv(HERE / "coverage.tsv")}
    import sqlite3
    mondo = sqlite3.connect(f"file:{Path.home() / '.data/oaklib/mondo.db'}?mode=ro", uri=True)

    def label(mid: str) -> str:
        r = mondo.execute("select value from statements where subject=? and predicate='rdfs:label'", (mid,)).fetchone()
        return r[0] if r else "NA"
    drawer = Drawer()
    cut = slot_cutoffs(len(ORIGINAL) + N_DRAW)
    slots = [(f"N{i:02d}", "ORIGINAL", cov[f]) for i, (_, f) in enumerate(ORIGINAL, 1)]
    slots += [(f"N{i:02d}", "DRAW_SEED_20261114", r) for i, r in enumerate(drawer.first, len(ORIGINAL) + 1)]
    replaced = []

    phase = {"n": 1}

    def entry(slot, origin, r):
        c = cut[int(slot[1:]) - 1]
        date = PHASE1_CUTOFF[slot] if phase["n"] == 1 else c["cutoff_date"]
        return {"slot": slot, "origin": origin, "kb_file": r["kb_file"], "disease": r["disease"],
                "mondo_id": r["mondo_id"], "matched_case": c["case_id"], "cutoff_date": date}

    current = [entry(*s) for s in slots]
    for e in current:
        if e["kb_file"] in REPLACED:
            replaced.append({**e, "phase": 1, "reason": REPLACED[e["kb_file"]]})
            e.update(entry(e["slot"], "DRAW_SEED_20261114_NEXT", drawer.next()))
    while True:
        lit = literature(current)
        failed = [e for e in current if lit[e["kb_file"]]["lit_ruling"] != "PASS"]
        redraw = [e for e in failed if e["origin"] != "ORIGINAL"]
        if not redraw:
            break
        for e in redraw:
            replaced.append({**e, "phase": 1, "reason": f"literature check {lit[e['kb_file']]['lit_ruling']} "
                                            f"({lit[e['kb_file']]['lit_count']} records) at {e['cutoff_date']}"})
            e.update(entry(e["slot"], "DRAW_SEED_20261114_NEXT", drawer.next()))

    # Phase 2 (added 2026-11-16): the accessible-test screen. Applied after phase 1 so that phase 1
    # consumes the seeded stream exactly as before and reproduces the slots it gave; a slot whose
    # disease fails the screen is redrawn from the same stream, and the new draw must pass both the
    # screen and the literature check.
    phase["n"] = 2
    for e in current:
        e["cutoff_date"] = cut[int(e["slot"][1:]) - 1]["cutoff_date"]
    while True:
        changed = False
        for e in current:
            if e["origin"] == "ORIGINAL":
                continue
            why = screen(e["kb_file"], cov[e["kb_file"]]["measurable_nodes"])
            if why:
                replaced.append({**e, "phase": 2, "reason": why})
                e.update(entry(e["slot"], "DRAW_SEED_20261114_SCREENED", drawer.next()))
                changed = True
        lit = literature(current)
        for e in current:
            if e["origin"] != "ORIGINAL" and lit[e["kb_file"]]["lit_ruling"] != "PASS":
                replaced.append({**e, "phase": 2, "reason": f"literature check {lit[e['kb_file']]['lit_ruling']} "
                                                            f"({lit[e['kb_file']]['lit_count']} records) at {e['cutoff_date']}"})
                e.update(entry(e["slot"], "DRAW_SEED_20261114_SCREENED", drawer.next()))
                changed = True
        if not changed:
            break

    missing = [(e["kb_file"], cov[e["kb_file"]]["measurable_nodes"]) for e in current if e["kb_file"] not in USABILITY]
    if missing:
        sys.exit("no usability judgment for:\n  " + "\n  ".join(f"{f}: {m}" for f, m in missing))
    out, lit_rows = [], []
    for e in current:
        r, lr = cov[e["kb_file"]], lit[e["kb_file"]]
        f = e["kb_file"]
        if f in USABILITY:
            usable, basis, mono = USABILITY[f]
        else:
            sys.exit(f"{f}: no usability judgment; read its measurable nodes ({r['measurable_nodes']}) "
                     "and add it to USABILITY")
        out.append({"slot": e["slot"], "disease": e["disease"], "kb_file": f, "mondo_id": e["mondo_id"],
                    "mondo_label": label(e["mondo_id"]), "origin": e["origin"],
                    "measurable_nodes": r["measurable_nodes"] or "NA", "h3_usable": usable,
                    "h3_usable_basis": basis, "monogenic_germline": mono,
                    "matched_case": e["matched_case"], "cutoff_date": e["cutoff_date"],
                    "lit_count": lr["lit_count"], "lit_ruling": lr["lit_ruling"]})
        lit_rows.append({"slot": e["slot"], **lr})
    write_tsv(HERE / "negatives.tsv", out)
    write_tsv(HERE / "negatives_replaced.tsv", replaced)
    write_tsv(HERE / "negatives_literature_check.tsv", lit_rows)
    usable = [o for o in out if o["h3_usable"] == "yes" and o["lit_ruling"] == "PASS"]
    print(f"{len(out)} negatives; replaced {len(replaced)}; H3 usable {len(usable)}")
    for o in out:
        print("\t".join([o["slot"], o["origin"], o["h3_usable"], o["lit_ruling"], o["lit_count"],
                         o["cutoff_date"], o["disease"]]))


if __name__ == "__main__":
    main()
