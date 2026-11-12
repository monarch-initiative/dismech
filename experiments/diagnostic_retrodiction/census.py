"""Census of diagnostic tests, biochemical markers, and prevalence across kb/disorders/.

Read-only: never writes into kb/. For every disorder entry, emits one TSV row
per diagnosis[] entry and one per biochemical[] entry (a disease with neither
still gets one ROW_TYPE=NONE row, so it is represented). Disease-level facts
(mondo_id, prevalence, has_differential_diagnoses) are repeated on every row
for that disease.

A row is flagged FLAG_NONGENETIC_SPECIMEN when it resolves to an accessible
specimen (blood, urine, CSF, dried blood spot) and is not a *germline* genetic
test. Only germline/inherited genotyping is excluded: a row whose variant is
somatic, acquired or clonal (SOMATIC_VARIANT) stays flagged, because a somatic
driver assayed in blood is a clonal-marker test rather than an inherited-disease
genotype. So FLAG = specimen AND NOT (IS_GENETIC AND NOT SOMATIC_VARIANT).

SPECIMEN_BASIS makes every inference visible, in precedence order:

  STATED   the row's own prose names the specimen
  LOINC    no prose statement, but a bound LOINC code's system axis names one
  IMPLICIT neither, but the analyte class is blood-based by construction
           (IMPLICIT_CLASS names which rule fired)
  NONE     nothing resolved; the row is never flagged

IS_GENETIC is read from the test's *identity* only - its name plus the labels
of the terms bound to it - not from narrative prose. SOMATIC_VARIANT and the
STATED specimen still read the full text.

These remain text-match heuristics over curation prose: the schema has no
specimen slot and no germline/somatic slot on Diagnosis, and the LOINC system
axis is parsed out of the Long Common Name because the cache stores no
structured SYSTEM field. Read SPECIMEN_BASIS, IMPLICIT_CLASS, IS_GENETIC and
SOMATIC_VARIANT before trusting FLAG_NONGENETIC_SPECIMEN.

A row the frame misses is not always a matcher failure: the dismech entry may
simply not record the test. check_recall.py distinguishes the two.

Usage:
    uv run python experiments/diagnostic_retrodiction/census.py \
        --out experiments/diagnostic_retrodiction/frame.tsv
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Any

import yaml

# Leading \b only: these are stems, not whole words, so a trailing \b would
# reject suffixed forms (chromosom|al, sequenc|ing, genom|ic, mutat|ional).
GENETIC_RE = re.compile(
    r"\b(gene\w*|genom\w*|sequenc\w*|mutat\w*|variant\w*|allel\w*|chromosom\w*|"
    r"exom\w*|karyotyp\w*|genotyp\w*|\bdna\b|\bngs\b|next[- ]generation sequencing)",
    re.I,
)

# Maps surface forms onto the four specimen categories the census is asked
# for; serum/plasma and the separated cell fractions are blood-derived and are
# folded into BLOOD rather than reported separately. "Cerebral spinal fluid" is
# LOINC's own spelling of CSF and must be matched alongside "cerebrospinal".
SPECIMEN_CATEGORIES = {
    "BLOOD": re.compile(
        r"\b(blood|serum|plasma|leukocyte\w*|lymphocyte\w*|erythrocyte\w*|"
        r"red blood cell\w*|white blood cell\w*|rbc|wbc|platelet\w*)\b",
        re.I,
    ),
    "URINE": re.compile(r"\b(urine|urinary)\b", re.I),
    "CSF": re.compile(r"\b(cerebral spinal fluid|cerebrospinal fluid|csf)\b", re.I),
    "DRIED_BLOOD_SPOT": re.compile(r"\b(dried blood spot|dbs)\b", re.I),
}

#: Analyte classes that are blood-based by construction, used only when no
#: specimen is stated in prose and none is coded in LOINC. Each is a claim about
#: the assay's substrate, not about the disease.
IMPLICIT_BLOOD_CLASSES = {
    # An autoantibody or isotype-specific immunoassay is run on serum or CSF;
    # serum is the default draw, so the accessible specimen is blood.
    "AUTOANTIBODY": re.compile(
        r"auto-?antibod\w*|antibod\w*|\banti-[A-Za-z0-9]|seropositiv\w*|"
        r"serolog\w*|\bIg[GAME]\b",
        re.I,
    ),
    # Enzyme activity is assayed in plasma, leukocytes, or dried blood spots.
    # The optional short token admits an isoform qualifier between the enzyme
    # and the word activity ("Hexosaminidase A activity").
    "ENZYME_ACTIVITY": re.compile(
        r"(?:enzym\w*|[A-Za-z0-9]+ase|ADAMTS13)(?:\s+[A-Za-z0-9]{1,4}\b)?\s+activit\w*|"
        r"activit\w*\s+assay|enzym\w*\s+assay",
        re.I,
    ),
    # Circulating metabolite/sterol biomarkers. Deliberately specific rather
    # than a bare "sterol", which would also match plain cholesterol and turn a
    # cellular lipid-accumulation node into a blood test.
    "CIRCULATING_METABOLITE": re.compile(
        r"oxysterol\w*|cholestane|7-?ketocholesterol|dehydrocholesterol|"
        r"\b7-?DHC\b|lyso-?g[bl]\d|globotriaosylsphingosine|"
        r"glucosylsphingosine|metanephrin\w*|normetanephrin\w*",
        re.I,
    ),
    # Flow cytometry needs a cell suspension; in these diseases that is blood.
    # "EMA" is spelled out rather than matched bare, which would also hit the
    # European Medicines Agency.
    "FLOW_CYTOMETRY": re.compile(
        r"flow cytometr\w*|immunophenotyp\w*|\bFACS\b|eosin-?5|EMA binding|"
        r"EMA dye|maleimide",
        re.I,
    ),
}

#: Specimens that are not accessible draws. If one of these is named in a
#: test's *identity* and no accessible specimen is stated or coded, the IMPLICIT
#: rules are suppressed: an enzyme activity assay run on cultured fibroblasts is
#: a tissue assay, and inferring blood from the analyte class alone would
#: overrule the entry.
#:
#: Matched against identity text only, never narrative prose. Against prose this
#: fired on disease biology rather than on the assay: Gaucher's Lyso-Gb1 row was
#: suppressed by its own caveat about "the dominant tissue toxin", which says
#: nothing about where the metabolite is measured.
NONACCESSIBLE_SPECIMEN_RE = re.compile(
    r"fibroblast\w*|biops\w*|bone marrow|\bmarrow\b|amniocyte\w*|amniotic|"
    r"chorionic villus|\bCVS\b|skin|muscle|liver|renal|kidney|brain|"
    r"cultured cell\w*|tissue|autops\w*|saliva|stool|f[ae]ces|sputum",
    re.I,
)

#: Hematologic context, for the somatic-driver implicit rule: a somatic driver
#: variant in a blood cancer or blood disorder is genotyped from blood or
#: marrow, so blood is the accessible specimen. Checked against the disease's
#: own name, parents and categories.
HEMATOLOGIC_RE = re.compile(
    r"leukemi\w*|lymphom\w*|myelom\w*|myeloprolifer\w*|myelodysplas\w*|"
    r"polycythemi\w*|thrombocythemi\w*|myelofibros\w*|h[ae]moglobinuri\w*|"
    r"histiocytos\w*|mastocytos\w*|an[ae]mi\w*|neutropeni\w*|"
    r"thrombocytopeni\w*|h[ae]matolog\w*|erythrocytos\w*|erythroleukemi\w*",
    re.I,
)

# Explicit post-zygotic vocabulary. "mosaic" is included because somatic
# mosaicism is a somatic origin (HP:0001442).
SOMATIC_VOCAB_RE = re.compile(r"\b(somatic|clonal|clonality|mosaic\w*)\b", re.I)

# Hallmark somatic driver tokens. The gene symbols are deliberately only the
# MPN drivers, NOT a general oncogene list: many oncogenes also cause germline
# developmental syndromes curated in this KB (germline BRAF -> CFC/Noonan,
# germline KIT, germline PTPN11), so a bare symbol does not imply a somatic
# claim. BRAF therefore qualifies only through its V600E hotspot, which is how
# the request named it.
SOMATIC_MARKER_RE = re.compile(
    r"\b(JAK2|CALR|MPL)\b|\bV617F\b|\bV600E\b|\bBCR[-\s]?ABL\w*\b", re.I
)

# "acquired" alone is not evidence of a somatic variant: it is ordinary medical
# English for non-inherited ("community-acquired pneumonia", "acquired aplastic
# anemia"), and the autoantibody diseases in this corpus are named with it
# ("Acquired Thrombotic Thrombocytopenic Purpura") while having no variant at
# all. Require it near variant vocabulary, in either order.
ACQUIRED_VARIANT_RE = re.compile(
    r"\bacquired\b(?:\W+\w+){0,6}\W+(?:variant|mutation|mutations|lesion|clone|clonal)\b"
    r"|\b(?:variant|mutation|mutations|lesion|clone|clonal)\b(?:\W+\w+){0,6}\W+acquired\b",
    re.I,
)

FIELDS = [
    "disease_name",
    "mondo_id",
    "row_type",
    "row_name",
    "diagnosis_term_id",
    "diagnosis_term_label",
    "measurements",
    "biomarker_term_id",
    "biomarker_term_label",
    "readouts",
    "specimen_hits",
    "specimen_basis",
    "implicit_class",
    "is_genetic",
    "somatic_variant",
    "flag_nongenetic_specimen",
    "prevalence",
    "has_differential_diagnoses",
]


def clean(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip().replace("\t", " ")


def mondo_id(disease: dict) -> str:
    term_id = clean((disease.get("disease_term") or {}).get("term", {}).get("id"))
    if term_id.startswith("MONDO:"):
        return term_id
    for mapping in (disease.get("mappings") or {}).get("mondo_mappings") or []:
        if mapping.get("mapping_predicate") in ("skos:exactMatch", "skos:narrowMatch"):
            candidate = clean((mapping.get("term") or {}).get("id"))
            if candidate.startswith("MONDO:"):
                return candidate
    return ""


def prevalence_summary(disease: dict) -> str:
    parts = []
    for p in disease.get("prevalence") or []:
        bits = [
            clean(p.get("population")),
            clean(p.get("measure_type")),
            clean(p.get("prevalence_class")),
            clean(p.get("rate_per_100000")),
        ]
        parts.append("|".join(b for b in bits if b))
    return " ;; ".join(parts)


LOINC_CACHE = Path("cache/loinc/terms.csv")


def load_loinc_labels(path: Path = LOINC_CACHE) -> dict[str, str]:
    """CURIE -> Long Common Name from the committed label cache.

    Cache-first and offline, like every other term check here. A code absent
    from the cache simply yields no system axis rather than a network call.
    """
    labels: dict[str, str] = {}
    if not path.exists():
        return labels
    with path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            curie = (row.get("curie") or "").strip()
            if curie:
                labels[curie] = (row.get("label") or "").strip()
    return labels


def loinc_system_text(label: str) -> str:
    """The system (specimen) axis of a LOINC Long Common Name.

    The cache stores only the Long Common Name, so the axis is parsed out of it
    rather than read from a structured SYSTEM field. Two shapes carry it:
    ``Component [Property] in System by Method`` and the panel form
    ``... panel - Serum``. Everything after the last `` in `` up to a `` by ``
    is taken as the system.
    """
    parts = []
    panel = re.search(r"\s-\s([A-Za-z][A-Za-z' ]*)$", label)
    if panel:
        parts.append(panel.group(1))
    matches = list(re.finditer(r"\bin\s+", label))
    if matches:
        tail = label[matches[-1].end():]
        parts.append(re.split(r"\s+by\s+", tail)[0])
    return " ".join(parts)


def specimen_categories(text: str) -> list[str]:
    """Specimen categories named in ``text``, most specific label winning.

    A dried blood spot is reported as DRIED_BLOOD_SPOT alone, not also as
    BLOOD, so the two stay countable separately.
    """
    hits = [cat for cat, pat in SPECIMEN_CATEGORIES.items() if pat.search(text)]
    if "DRIED_BLOOD_SPOT" in hits and "BLOOD" in hits:
        hits.remove("BLOOD")
    return sorted(hits)


def classify(
    identity_text: str,
    full_text: str,
    loinc_codes: list[str],
    disease_context: str,
    loinc_labels: dict[str, str],
) -> dict[str, str]:
    """Genetic/somatic reads and a specimen with its basis, for one row.

    ``is_genetic`` is read from ``identity_text`` only - the test's own name and
    term labels. Reading it from narrative prose produced false positives that
    suppressed the flag: the acquired-TTP plasma activity assay was excluded as
    a genetic test because its ``results`` field mentioned that a result "may
    prompt repeat or genetic evaluation", a downstream referral rather than
    this test.

    Specimen resolution is a precedence chain, recorded in ``specimen_basis``:
    STATED (named in the row's prose) > LOINC (the system axis of a bound code)
    > IMPLICIT (an analyte class that is blood-based by construction) > NONE.
    """
    is_genetic = bool(GENETIC_RE.search(identity_text))
    somatic = bool(
        SOMATIC_VOCAB_RE.search(full_text)
        or SOMATIC_MARKER_RE.search(full_text)
        or ACQUIRED_VARIANT_RE.search(full_text)
    )
    germline_genetic = is_genetic and not somatic

    stated = specimen_categories(full_text)
    coded = specimen_categories(
        " ".join(loinc_system_text(loinc_labels.get(c, "")) for c in loinc_codes)
    )

    implicit_class = ""
    if not NONACCESSIBLE_SPECIMEN_RE.search(identity_text):
        if somatic and HEMATOLOGIC_RE.search(disease_context):
            implicit_class = "SOMATIC_HEME_DRIVER"
        else:
            for name, pattern in IMPLICIT_BLOOD_CLASSES.items():
                if pattern.search(identity_text):
                    implicit_class = name
                    break

    if stated or coded:
        hits = sorted(set(stated) | set(coded))
        basis = "STATED" if stated else "LOINC"
        # Only reported when it actually supplied the specimen, so the column
        # never implies an inference the frame did not make.
        implicit_class = ""
    elif implicit_class:
        hits, basis = ["BLOOD"], "IMPLICIT"
    else:
        hits, basis = [], "NONE"

    return {
        "specimen_hits": ",".join(hits),
        "specimen_basis": basis,
        "implicit_class": implicit_class,
        "is_genetic": str(is_genetic).upper(),
        "somatic_variant": str(somatic).upper(),
        "flag_nongenetic_specimen": str(bool(hits) and not germline_genetic).upper(),
    }


def reference_range_codes(item: dict) -> list[str]:
    """LOINC CURIEs named by an item's reference_ranges[].loinc_term."""
    return [
        clean((r.get("loinc_term") or {}).get("id"))
        for r in item.get("reference_ranges") or []
        if (r.get("loinc_term") or {}).get("id")
    ]


def diagnosis_rows(disease: dict, ctx: str, loinc_labels: dict[str, str]) -> list[dict]:
    rows = []
    for d in disease.get("diagnosis") or []:
        term = (d.get("diagnosis_term") or {}).get("term", {})
        measurements, codes = [], []
        for m in d.get("measurements") or []:
            mt = m.get("term", {})
            label = clean(m.get("preferred_term")) or clean(mt.get("label"))
            cid = clean(mt.get("id"))
            measurements.append(f"{label} [{cid}]" if cid else label)
            if cid:
                codes.append(cid)
        measurements_str = "; ".join(x for x in measurements if x)
        codes += reference_range_codes(d)

        # The test's own identity: its name and the labels of the terms bound to
        # it. Narrative prose is deliberately excluded here (see classify).
        identity = " ".join(
            x
            for x in [
                clean(d.get("name")),
                clean((d.get("diagnosis_term") or {}).get("preferred_term")),
                clean(term.get("label")),
                measurements_str,
                " ".join(loinc_labels.get(c, "") for c in codes),
            ]
            if x
        )
        full = " ".join(
            x
            for x in [
                identity,
                clean(d.get("description")),
                clean(d.get("notes")),
                clean(d.get("markers")),
                clean(d.get("results")),
            ]
            if x
        )
        rows.append(
            {
                "row_type": "DIAGNOSIS",
                "row_name": clean(d.get("name")),
                "diagnosis_term_id": clean(term.get("id")),
                "diagnosis_term_label": clean(term.get("label")),
                "measurements": measurements_str,
                "biomarker_term_id": "",
                "biomarker_term_label": "",
                "readouts": "",
                **classify(identity, full, codes, ctx, loinc_labels),
            }
        )
    return rows


def biochemical_rows(disease: dict, ctx: str, loinc_labels: dict[str, str]) -> list[dict]:
    rows = []
    for b in disease.get("biochemical") or []:
        term = (b.get("biomarker_term") or {}).get("term", {})
        readouts = []
        for r in b.get("readouts") or []:
            bits = [
                clean(r.get("target")),
                clean(r.get("relationship")),
                clean(r.get("direction")),
                clean(r.get("interpretation")),
            ]
            readouts.append("|".join(x for x in bits if x))
        readouts_str = "; ".join(x for x in readouts if x)

        codes = [clean((b.get("loinc_term") or {}).get("id"))] if (
            b.get("loinc_term") or {}
        ).get("id") else []
        codes += reference_range_codes(b)

        identity = " ".join(
            x
            for x in [
                clean(b.get("name")),
                clean((b.get("biomarker_term") or {}).get("preferred_term")),
                clean(term.get("label")),
                clean((b.get("loinc_term") or {}).get("label")),
                " ".join(loinc_labels.get(c, "") for c in codes),
            ]
            if x
        )
        full = " ".join(
            x
            for x in [
                identity,
                clean(b.get("description")),
                clean(b.get("notes")),
                clean(b.get("context")),
                readouts_str,
            ]
            if x
        )
        rows.append(
            {
                "row_type": "BIOCHEMICAL",
                "row_name": clean(b.get("name")),
                "diagnosis_term_id": "",
                "diagnosis_term_label": "",
                "measurements": "",
                "biomarker_term_id": clean(term.get("id")),
                "biomarker_term_label": clean(term.get("label")),
                "readouts": readouts_str,
                **classify(identity, full, codes, ctx, loinc_labels),
            }
        )
    return rows


def census_rows(path: Path, loinc_labels: dict[str, str]) -> list[dict]:
    disease = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not disease:
        return []

    common = {
        "disease_name": clean(disease.get("name")),
        "mondo_id": mondo_id(disease),
        "prevalence": prevalence_summary(disease),
        "has_differential_diagnoses": str(bool(disease.get("differential_diagnoses"))).upper(),
    }

    # Disease-level context for the somatic-driver implicit rule: is this a
    # hematologic disease? Read from the entry's own name, parents, categories.
    ctx = " ".join(
        [clean(disease.get("name"))]
        + [clean(p) for p in disease.get("parents") or []]
        + [clean(c) for c in disease.get("categories") or []]
        + [clean(disease.get("category"))]
    )

    rows = diagnosis_rows(disease, ctx, loinc_labels) + biochemical_rows(
        disease, ctx, loinc_labels
    )
    if not rows:
        rows = [
            {
                "row_type": "NONE",
                "row_name": "",
                "diagnosis_term_id": "",
                "diagnosis_term_label": "",
                "measurements": "",
                "biomarker_term_id": "",
                "biomarker_term_label": "",
                "readouts": "",
                "specimen_hits": "",
                "specimen_basis": "NONE",
                "implicit_class": "",
                "is_genetic": "",
                "somatic_variant": "",
                "flag_nongenetic_specimen": "FALSE",
            }
        ]
    return [{**common, **row} for row in rows]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    ap.add_argument(
        "--out",
        type=Path,
        default=Path("experiments/diagnostic_retrodiction/frame.tsv"),
        help="TSV output path (default: experiments/diagnostic_retrodiction/frame.tsv); "
        "pass - for stdout",
    )
    a = ap.parse_args()

    loinc_labels = load_loinc_labels()
    paths = sorted(a.kb_dir.glob("*.yaml"))
    out_lines = ["\t".join(FIELDS)]
    flagged = 0
    for path in paths:
        for row in census_rows(path, loinc_labels):
            if row["flag_nongenetic_specimen"] == "TRUE":
                flagged += 1
            out_lines.append("\t".join(row[f] for f in FIELDS))

    text = "\n".join(out_lines) + "\n"
    if str(a.out) == "-":
        print(text, end="")
    else:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(text)
        print(f"wrote {len(out_lines) - 1} rows from {len(paths)} files to {a.out} "
              f"({flagged} flagged nongenetic-specimen)")


if __name__ == "__main__":
    main()
