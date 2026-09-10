#!/usr/bin/env python3
"""Census of the epilepsy entries in dismech, with a pediatric-onset verdict.

The question this answers is "which disorder entries are pediatric epilepsies?"
It is answered in three deterministic tiers rather than by hand-listing, so the
numbers can be regenerated after every curation wave:

1. **MONDO epilepsy closure.** The entry's ``disease_term`` (or a
   ``has_subtypes[].subtype_term`` or an exact/narrow ``mondo_mappings`` term)
   is a reflexive ``is_a`` descendant of ``MONDO:0005027`` (epilepsy). This is
   the authoritative tier: MONDO says the entry *is* an epilepsy.
2. **Epilepsy-named, outside the closure.** The entry name or the MONDO label
   contains *epilep*, *seizure*, or *DEE*, but MONDO does not place the term
   under epilepsy (e.g. ``CDKL5 Deficiency Disorder``, the UNC13A pair). These
   are entries the KB treats as epilepsies and MONDO does not, and the report
   lists them so the disagreement is visible.
3. **Seizures as a core feature.** Outside tiers 1 and 2, a phenotype bound to
   an HP seizure term carries ``frequency`` OBLIGATE or VERY_FREQUENT. These are
   broader syndromes (tuberous sclerosis, Angelman, lissencephaly) in which
   epilepsy is a defining part of the picture without being the disease name.

Each tier-1 named syndrome is then assigned its ILAE 2022 age-at-onset group
(``ILAE_AGE_GROUP`` below, keyed by KB file stem) from the Task Force position
papers: neonates and infants (PMID:35503712), childhood (PMID:35503717),
idiopathic generalized epilepsies (PMID:35503716), variable age (PMID:35503725).
Entries whose MONDO label is a numbered ``developmental and epileptic
encephalopathy`` are grouped as gene-defined DEEs; DEE onset is in infancy or
early childhood by definition. The pediatric verdict is derived from that
group. Anything not in the map falls back to the entry's own onset annotations.

The AAP list of pediatric epilepsy types
(https://www.aap.org/en/patient-care/epilepsy/understanding-pediatric-epilepsy/understanding-pediatric-epilepsy-types-of-pediatric-epilepsy/)
is cross-referenced in ``AAP_TYPES`` so the coverage of that list is a table,
not a claim.

The mechanism-module conformance of every listed entry is counted too: it is
what decides whether a module collection for the epilepsies has anything to
point at.

Usage:
    uv run python scripts/pediatric_epilepsy_census.py                  # markdown to stdout
    uv run python scripts/pediatric_epilepsy_census.py --out research/pediatric_epilepsy_census.md
    uv run python scripts/pediatric_epilepsy_census.py --json           # machine-readable

Requires the local MONDO SQLite build (``sqlite:obo:mondo``); OAK downloads it
on first use.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field

from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A

from dismech.yaml_io import safe_load

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISORDERS_DIR = os.path.join(ROOT, "kb", "disorders")
GROUPINGS_DIR = os.path.join(ROOT, "kb", "groupings")

EPILEPSY = "MONDO:0005027"
GENETIC_DEE = "MONDO:0100062"

# HP seizure terms accepted for the tier-3 "core feature" test. Seizure
# (HP:0001250) and its commonest children; the point is to catch entries
# that bound the phenotype at a more specific level than the parent.
SEIZURE_HP = {
    "HP:0001250",  # Seizure
    "HP:0002197",  # Generalized-onset seizure
    "HP:0002373",  # Febrile seizure (within the age range of 3 months to 6 years)
    "HP:0011097",  # Epileptic spasm
    "HP:0032794",  # Motor seizure
    "HP:0002069",  # Bilateral tonic-clonic seizure
    "HP:0001327",  # Photosensitive tonic-clonic seizure
    "HP:0010818",  # Generalized tonic seizure
    "HP:0011150",  # Myoclonic absence seizure
    "HP:0002123",  # Generalized myoclonic seizure
    "HP:0032807",  # Generalized atonic seizure
    "HP:0002384",  # Focal impaired awareness seizure
    "HP:0011146",  # Dialeptic seizure
    "HP:0007359",  # Focal-onset seizure
    "HP:0002133",  # Status epilepticus
    "HP:0011169",  # Generalized clonic seizure
    "HP:0032677",  # Generalized non-motor (absence) seizure
    "HP:0011172",  # Complex febrile seizure
}

NAME_PATTERN = re.compile(r"(?i)epilep|seizure|\bDEE\b")

# ILAE 2022 age-at-onset group for named syndromes, keyed by KB file stem.
#   NEONATAL_INFANTILE  Zuberi et al. 2022  PMID:35503712
#   CHILDHOOD           Specchio et al. 2022  PMID:35503717
#   IGE                 Hirsch et al. 2022  PMID:35503716 (CAE is also a
#                       childhood syndrome; JAE/JME/GTCA start in adolescence)
#   VARIABLE            Riney et al. 2022  PMID:35503725
#   ETIOLOGY_PEDIATRIC  etiology-specific syndromes the neonatal/infantile
#                       and childhood papers describe (KCNQ2-DEE, PDE, PNPO,
#                       CDKL5, PCDH19, GLUT1, Sturge-Weber, gelastic seizures
#                       with hypothalamic hamartoma) plus Rasmussen
#                       encephalitis, which is childhood-onset but is not on
#                       the ILAE 2022 syndrome list.
#   UMBRELLA            index-level entries, not a syndrome
ILAE_AGE_GROUP: dict[str, str] = {
    # neonates and infants
    "Benign_Neonatal_Seizures": "NEONATAL_INFANTILE",
    "Benign_Familial_Infantile_Epilepsy": "NEONATAL_INFANTILE",
    "Generalized_Epilepsy_with_Febrile_Seizures_Plus": "NEONATAL_INFANTILE",
    "Myoclonic_Epilepsy_in_Infancy": "NEONATAL_INFANTILE",
    "Early-Infantile_Developmental_and_Epileptic_Encephalopathy": "NEONATAL_INFANTILE",
    "Epilepsy_of_Infancy_with_Migrating_Focal_Seizures": "NEONATAL_INFANTILE",
    "Infantile_Spasms": "NEONATAL_INFANTILE",
    "Dravet_syndrome": "NEONATAL_INFANTILE",
    # childhood
    "Self-Limited_Epilepsy_with_Autonomic_Seizures": "CHILDHOOD",
    "Childhood_Occipital_Visual_Epilepsy": "CHILDHOOD",
    "Photosensitive_Occipital_Lobe_Epilepsy": "CHILDHOOD",
    "Self-Limited_Epilepsy_with_Centrotemporal_Spikes": "CHILDHOOD",
    "Childhood_Absence_Epilepsy": "CHILDHOOD",
    "Epilepsy_with_Myoclonic_Absences": "CHILDHOOD",
    "Jeavons_Syndrome": "CHILDHOOD",
    "Epilepsy_with_Myoclonic_Atonic_Seizures": "CHILDHOOD",
    "SLC6A1-Related_Disorder": "CHILDHOOD",
    "Lennox-Gastaut_Syndrome": "CHILDHOOD",
    "DEE_with_Spike-Wave_Activation_in_Sleep": "CHILDHOOD",
    "Landau-Kleffner_Syndrome": "CHILDHOOD",
    "Febrile_Infection-Related_Epilepsy_Syndrome": "CHILDHOOD",
    "Hemiconvulsion-Hemiplegia-Epilepsy_Syndrome": "CHILDHOOD",
    # idiopathic generalized epilepsies
    "Juvenile_Absence_Epilepsy": "IGE",
    "Juvenile_Myoclonic_Epilepsy": "IGE",
    "Epilepsy_with_Generalized_Tonic-Clonic_Seizures_Alone": "IGE",
    # variable age at onset
    "Familial_Focal_Epilepsy_With_Variable_Foci": "VARIABLE",
    "DEPDC5-Related_Epilepsy": "VARIABLE",
    "Familial_Sleep_Related_Hypermotor_Epilepsy": "VARIABLE",
    "Autosomal_Dominant_Epilepsy_with_Auditory_Features": "VARIABLE",
    "Temporal_Lobe_Epilepsy": "VARIABLE",
    "Mesial_Temporal_Lobe_Epilepsy_with_Hippocampal_Sclerosis": "VARIABLE",
    "Progressive_Myoclonus_Epilepsy": "VARIABLE",
    "Progressive_Myoclonic_Epilepsy_Type_7": "VARIABLE",
    "Progressive_Myoclonic_Epilepsy_Type_8": "VARIABLE",
    "Lafora_Disease": "VARIABLE",
    "Unverricht-Lundborg_Disease": "VARIABLE",
    "Northern_Epilepsy": "VARIABLE",
    "MERRF_Syndrome": "VARIABLE",
    "Pentanucleotide_Repeat_Familial_Adult_Myoclonus_Epilepsy": "VARIABLE",
    "Photosensitive_Epilepsy": "VARIABLE",
    "Post-Traumatic_Epilepsy": "VARIABLE",
    # etiology-specific, pediatric onset
    "KCNQ2_Developmental_and_Epileptic_Encephalopathy": "ETIOLOGY_PEDIATRIC",
    "Pyridoxine-Dependent_Epilepsy": "ETIOLOGY_PEDIATRIC",
    "PNPO_Deficiency": "ETIOLOGY_PEDIATRIC",
    "CDKL5_Deficiency_Disorder": "ETIOLOGY_PEDIATRIC",
    "PCDH19_Clustering_Epilepsy": "ETIOLOGY_PEDIATRIC",
    "GLUT1_Deficiency_Syndrome": "ETIOLOGY_PEDIATRIC",
    "Sturge-Weber_Syndrome": "ETIOLOGY_PEDIATRIC",
    "Hypothalamic_Hamartoma_with_Gelastic_Seizures": "ETIOLOGY_PEDIATRIC",
    "Rasmussen_Encephalitis": "ETIOLOGY_PEDIATRIC",
    # umbrella / index entries
    "Epilepsy": "UMBRELLA",
    "Genetic_Developmental_and_Epileptic_Encephalopathy": "UMBRELLA",
    "Undetermined_Early_Onset_Epileptic_Encephalopathy": "UMBRELLA",
}

PEDIATRIC_GROUPS = {
    "NEONATAL_INFANTILE",
    "CHILDHOOD",
    "IGE",
    "ETIOLOGY_PEDIATRIC",
    "DEE",
}

# Adolescent-onset IGE syndromes are pediatric in the AAP sense (onset before
# 18) but not in the ILAE "childhood" sense; the verdict keeps them and says so.

# The AAP "Types of Pediatric Epilepsy" list, in page order, mapped to KB stems.
AAP_TYPES: list[tuple[str, list[str], str]] = [
    ("Childhood Absence Epilepsy", ["Childhood_Absence_Epilepsy"], ""),
    (
        "Childhood Epilepsy with Centrotemporal Spikes (Benign Rolandic Epilepsy)",
        ["Self-Limited_Epilepsy_with_Centrotemporal_Spikes"],
        "",
    ),
    (
        "Doose Syndrome (Myoclonic Atonic Epilepsy)",
        ["Epilepsy_with_Myoclonic_Atonic_Seizures", "SLC6A1-Related_Disorder"],
        "Both entries carry MONDO:0014633 as disease_term; the SLC6A1 entry is the gene-defined form.",
    ),
    ("Dravet Syndrome", ["Dravet_syndrome"], ""),
    (
        "Early Infantile Developmental & Epileptic Encephalopathy",
        ["Early-Infantile_Developmental_and_Epileptic_Encephalopathy"],
        "Grouping Early_Infantile_Developmental_and_Epileptic_Encephalopathies lists the gene-defined members.",
    ),
    (
        "Epilepsy in Infancy with Migrating Focal Seizures",
        ["Epilepsy_of_Infancy_with_Migrating_Focal_Seizures"],
        "",
    ),
    ("Epilepsy with Eyelid Myoclonia (Jeavons Syndrome)", ["Jeavons_Syndrome"], ""),
    (
        "Epilepsy with Generalized Tonic-Clonic Seizures Alone",
        ["Epilepsy_with_Generalized_Tonic-Clonic_Seizures_Alone"],
        "",
    ),
    ("Epilepsy with Myoclonic-Absences", ["Epilepsy_with_Myoclonic_Absences"], ""),
    (
        "Epileptic Encephalopathy with Continuous Spike and Wave during Sleep (CSWS)",
        ["DEE_with_Spike-Wave_Activation_in_Sleep", "Landau-Kleffner_Syndrome"],
        "ILAE 2022 folds Landau-Kleffner syndrome into DEE-SWAS; both are kept as entries.",
    ),
    (
        "FIRES (Febrile Illness-related Epilepsy Syndrome)",
        ["Febrile_Infection-Related_Epilepsy_Syndrome"],
        "",
    ),
    (
        "Genetic Epilepsy with Febrile Seizures Plus",
        ["Generalized_Epilepsy_with_Febrile_Seizures_Plus"],
        "",
    ),
    ("Infantile Spasms (West Syndrome)", ["Infantile_Spasms"], ""),
    ("Juvenile Absence Epilepsy", ["Juvenile_Absence_Epilepsy"], ""),
    ("Juvenile Myoclonic Epilepsy", ["Juvenile_Myoclonic_Epilepsy"], ""),
    ("Lennox-Gastaut Syndrome (LGS)", ["Lennox-Gastaut_Syndrome"], ""),
    ("Myoclonic Epilepsy of Infancy", ["Myoclonic_Epilepsy_in_Infancy"], ""),
    ("Panayiotopoulos Syndrome", ["Self-Limited_Epilepsy_with_Autonomic_Seizures"], ""),
    (
        "Progressive Myoclonic Epilepsies",
        [
            "Progressive_Myoclonus_Epilepsy",
            "Lafora_Disease",
            "Unverricht-Lundborg_Disease",
            "Progressive_Myoclonic_Epilepsy_Type_7",
            "Progressive_Myoclonic_Epilepsy_Type_8",
            "Northern_Epilepsy",
            "MERRF_Syndrome",
        ],
        "Umbrella entry plus the curated members; the neuronal ceroid lipofuscinoses sit in their own grouping.",
    ),
    (
        "Reflex Epilepsies",
        ["Photosensitive_Epilepsy", "Photosensitive_Occipital_Lobe_Epilepsy"],
        "PARTIAL: only the photosensitive reflex epilepsies are curated; the reflex-epilepsy umbrella (MONDO:0017768) and reading/startle/hot-water forms have no entry.",
    ),
    (
        "Self-Limited Familial and Non-Familial Neonatal-Infantile Seizures",
        ["Benign_Neonatal_Seizures", "Benign_Familial_Infantile_Epilepsy"],
        "PARTIAL: SeLNE and SeLIE are curated; the SCN2A self-limited familial neonatal-infantile form appears only as a phenotype-spectrum mention inside the SCN2A DEE entry.",
    ),
    (
        "Sleep-related Hypermotor Epilepsy (SHE)",
        ["Familial_Sleep_Related_Hypermotor_Epilepsy"],
        "PARTIAL: the familial (CHRNA4/KCNT1/DEPDC5) form is curated; sporadic SHE is not a separate entry.",
    ),
    (
        "Temporal Lobe Epilepsy",
        [
            "Temporal_Lobe_Epilepsy",
            "Mesial_Temporal_Lobe_Epilepsy_with_Hippocampal_Sclerosis",
        ],
        "",
    ),
]

PEDIATRIC_ONSET_CATEGORIES = {
    "ANTENATAL",
    "PRENATAL",
    "CONGENITAL",
    "NEONATAL",
    "INFANTILE",
    "CHILDHOOD",
    "JUVENILE",
    "PEDIATRIC",
}
ADULT_ONSET_CATEGORIES = {"YOUNG_ADULT", "ADULT", "MIDDLE_AGE", "LATE", "LATE_ONSET"}


@dataclass
class Entry:
    stem: str
    name: str
    mondo_id: str | None
    mondo_label: str | None
    tier: int
    ilae_group: str
    pediatric: str  # YES / NO / VARIABLE / UMBRELLA / UNKNOWN
    onset_categories: list[str]
    conforms_to: list[str] = field(default_factory=list)
    in_grouping: list[str] = field(default_factory=list)


def _descendants(adapter, term: str) -> set[str]:
    return set(adapter.descendants(term, predicates=[IS_A], reflexive=True))


def _term_ids(data: dict) -> set[str]:
    ids: set[str] = set()
    primary = ((data.get("disease_term") or {}).get("term") or {}).get("id")
    if primary:
        ids.add(primary)
    for sub in data.get("has_subtypes") or []:
        sid = ((sub.get("subtype_term") or {}).get("term") or {}).get("id")
        if sid:
            ids.add(sid)
    for mapping in (data.get("mappings") or {}).get("mondo_mappings") or []:
        if mapping.get("mapping_predicate") in ("skos:exactMatch", "skos:narrowMatch"):
            mid = (mapping.get("term") or {}).get("id")
            if mid:
                ids.add(mid)
    return ids


def _normalize_frequency(value) -> str | None:
    if value is None:
        return None
    text = str(value).upper()
    if "OBLIGATE" in text or text == "HP_0040280":
        return "OBLIGATE"
    if "VERY_FREQUENT" in text or "VERY FREQUENT" in text or text == "HP_0040281":
        return "VERY_FREQUENT"
    return text


def _core_seizure(data: dict) -> bool:
    for phenotype in data.get("phenotypes") or []:
        term = ((phenotype.get("phenotype_term") or {}).get("term") or {}).get("id")
        if term in SEIZURE_HP and _normalize_frequency(phenotype.get("frequency")) in (
            "OBLIGATE",
            "VERY_FREQUENT",
        ):
            return True
    return False


def _grouping_index() -> dict[str, list[str]]:
    """Map disease name -> epilepsy groupings that list it."""
    index: dict[str, list[str]] = defaultdict(list)
    for path in sorted(glob.glob(os.path.join(GROUPINGS_DIR, "*.yaml"))):
        stem = os.path.basename(path)[:-5]
        if not re.search(r"(?i)epilep", stem):
            continue
        with open(path, encoding="utf-8") as fh:
            grouping = safe_load(fh) or {}
        for member in grouping.get("members") or []:
            index[member.get("member")].append(stem)
    return index


def _classify_group(stem: str, mondo_label: str | None, tier: int, in_dee: bool) -> str:
    if stem in ILAE_AGE_GROUP:
        return ILAE_AGE_GROUP[stem]
    label = (mondo_label or "").lower()
    if in_dee or "epileptic encephalopathy" in label:
        return "DEE"
    if tier == 1:
        return "OTHER_CLOSURE"
    return "NOT_A_SYNDROME"


def _verdict(group: str, onset_categories: list[str]) -> str:
    if group == "UMBRELLA":
        return "UMBRELLA"
    if group in PEDIATRIC_GROUPS:
        return "YES"
    if group == "VARIABLE":
        return "VARIABLE"
    onsets = set(onset_categories)
    if onsets & PEDIATRIC_ONSET_CATEGORIES:
        return "YES"
    if onsets & ADULT_ONSET_CATEGORIES:
        return "NO"
    return "UNKNOWN"


def collect(adapter) -> list[Entry]:
    epilepsy = _descendants(adapter, EPILEPSY)
    dee = _descendants(adapter, GENETIC_DEE)
    groupings = _grouping_index()
    entries: list[Entry] = []
    for path in sorted(glob.glob(os.path.join(DISORDERS_DIR, "*.yaml"))):
        stem = os.path.basename(path)[:-5]
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        data = safe_load(text) or {}
        if not isinstance(data, dict):
            continue
        ids = _term_ids(data)
        term = (data.get("disease_term") or {}).get("term") or {}
        mondo_id, mondo_label = term.get("id"), term.get("label")
        name = data.get("name") or stem
        tier = 0
        if ids & epilepsy:
            tier = 1
        elif (
            NAME_PATTERN.search(stem)
            or NAME_PATTERN.search(name)
            or NAME_PATTERN.search(mondo_label or "")
        ):
            tier = 2
        elif _core_seizure(data):
            tier = 3
        if not tier:
            continue
        onsets = sorted(set(re.findall(r"onset_category:\s*([A-Z_]+)", text)))
        group = _classify_group(stem, mondo_label, tier, bool(ids & dee))
        entries.append(
            Entry(
                stem=stem,
                name=name,
                mondo_id=mondo_id,
                mondo_label=mondo_label,
                tier=tier,
                ilae_group=group,
                pediatric=_verdict(group, onsets),
                onset_categories=onsets,
                conforms_to=sorted(
                    set(re.findall(r'conforms_to:\s*"?([a-z0-9_]+)', text))
                ),
                in_grouping=groupings.get(name, []),
            )
        )
    return entries


def _link(stem: str) -> str:
    return f"[`{stem}`](../kb/disorders/{stem}.yaml)"


def render_markdown(entries: list[Entry]) -> str:
    out: list[str] = []
    out.append("# Pediatric epilepsy census")
    out.append("")
    out.append(
        "Generated by `scripts/pediatric_epilepsy_census.py`. Do not hand-edit; "
        "regenerate with `uv run python scripts/pediatric_epilepsy_census.py "
        "--out research/pediatric_epilepsy_census.md`."
    )
    out.append("")
    tiers = Counter(e.tier for e in entries)
    verdicts = Counter(e.pediatric for e in entries if e.tier == 1)
    out.append("## Summary")
    out.append("")
    out.append("| Measure | Count |")
    out.append("| --- | --- |")
    out.append(f"| Tier 1: MONDO epilepsy closure (`MONDO:0005027`) | {tiers[1]} |")
    out.append(f"| Tier 2: epilepsy-named, outside the closure | {tiers[2]} |")
    out.append(
        f"| Tier 3: seizures OBLIGATE/VERY_FREQUENT, outside tiers 1-2 | {tiers[3]} |"
    )
    out.append(f"| Tier 1 pediatric verdict YES | {verdicts['YES']} |")
    out.append(
        f"| Tier 1 pediatric verdict VARIABLE (ILAE variable-age syndromes) | {verdicts['VARIABLE']} |"
    )
    out.append(f"| Tier 1 umbrella/index entries | {verdicts['UMBRELLA']} |")
    out.append(
        f"| Tier 1 verdict UNKNOWN (no onset data, not in the ILAE map) | {verdicts['UNKNOWN']} |"
    )
    out.append("")

    out.append("## AAP pediatric epilepsy types: coverage")
    out.append("")
    out.append("| AAP type | KB entries | Status | Note |")
    out.append("| --- | --- | --- | --- |")
    known = {e.stem for e in entries}
    covered = 0
    for label, stems, note in AAP_TYPES:
        present = [s for s in stems if s in known]
        status = (
            "PARTIAL"
            if note.startswith("PARTIAL")
            else ("COVERED" if present else "MISSING")
        )
        if status == "COVERED":
            covered += 1
        note_text = note.removeprefix("PARTIAL: ")
        out.append(
            f"| {label} | {', '.join(_link(s) for s in present) or '(none)'} | {status} | {note_text} |"
        )
    out.append("")
    out.append(
        f"{covered} of {len(AAP_TYPES)} AAP types fully covered; the rest are partial."
    )
    out.append("")

    group_order = [
        "NEONATAL_INFANTILE",
        "CHILDHOOD",
        "IGE",
        "ETIOLOGY_PEDIATRIC",
        "DEE",
        "OTHER_CLOSURE",
        "VARIABLE",
        "UMBRELLA",
    ]
    group_titles = {
        "NEONATAL_INFANTILE": "Onset in neonates and infants (ILAE 2022, PMID:35503712)",
        "CHILDHOOD": "Onset in childhood (ILAE 2022, PMID:35503717)",
        "IGE": "Idiopathic generalized epilepsies with adolescent onset (ILAE 2022, PMID:35503716)",
        "ETIOLOGY_PEDIATRIC": "Etiology-specific pediatric epilepsies",
        "DEE": "Gene-defined developmental and epileptic encephalopathies (onset in infancy or early childhood by definition)",
        "OTHER_CLOSURE": "Other entries in the MONDO epilepsy closure (verdict from the entry's own onset annotations)",
        "VARIABLE": "Variable age at onset (ILAE 2022, PMID:35503725): not pediatric-specific",
        "UMBRELLA": "Umbrella and index entries",
    }
    out.append("## Tier 1: entries in the MONDO epilepsy closure")
    out.append("")
    for group in group_order:
        rows = [e for e in entries if e.tier == 1 and e.ilae_group == group]
        if not rows:
            continue
        out.append(f"### {group_titles[group]} ({len(rows)})")
        out.append("")
        out.append(
            "| Entry | MONDO | Pediatric | Onset annotations | Modules | Epilepsy groupings |"
        )
        out.append("| --- | --- | --- | --- | --- | --- |")
        for e in sorted(rows, key=lambda x: x.stem.casefold()):
            out.append(
                f"| {_link(e.stem)} | `{e.mondo_id or ''}` {e.mondo_label or ''} | {e.pediatric} | "
                f"{', '.join(e.onset_categories)} | {', '.join(f'`{m}`' for m in e.conforms_to)} | "
                f"{', '.join(e.in_grouping)} |"
            )
        out.append("")

    out.append("## Tier 2: epilepsy-named entries MONDO does not place under epilepsy")
    out.append("")
    out.append(
        "| Entry | MONDO | Verdict | Onset annotations | Modules | Epilepsy groupings |"
    )
    out.append("| --- | --- | --- | --- | --- | --- |")
    for e in sorted(
        (x for x in entries if x.tier == 2), key=lambda x: x.stem.casefold()
    ):
        out.append(
            f"| {_link(e.stem)} | `{e.mondo_id or ''}` {e.mondo_label or ''} | {e.pediatric} | "
            f"{', '.join(e.onset_categories)} | {', '.join(f'`{m}`' for m in e.conforms_to)} | "
            f"{', '.join(e.in_grouping)} |"
        )
    out.append("")

    out.append("## Tier 3: seizures are an obligate or very frequent phenotype")
    out.append("")
    out.append("| Entry | MONDO | Verdict | Onset annotations | Modules |")
    out.append("| --- | --- | --- | --- | --- |")
    for e in sorted(
        (x for x in entries if x.tier == 3), key=lambda x: x.stem.casefold()
    ):
        out.append(
            f"| {_link(e.stem)} | `{e.mondo_id or ''}` {e.mondo_label or ''} | {e.pediatric} | "
            f"{', '.join(e.onset_categories)} | {', '.join(f'`{m}`' for m in e.conforms_to)} |"
        )
    out.append("")

    out.append("## Module conformance across all three tiers")
    out.append("")
    counts: Counter[str] = Counter()
    by_tier: dict[str, Counter[int]] = defaultdict(Counter)
    for e in entries:
        for module in e.conforms_to:
            counts[module] += 1
            by_tier[module][e.tier] += 1
    total = len(entries)
    none = sum(1 for e in entries if not e.conforms_to)
    out.append(
        f"{total - none} of {total} entries declare at least one `conforms_to`; {none} declare none."
    )
    out.append("")
    out.append("| Module | Conformers | Tier 1 | Tier 2 | Tier 3 |")
    out.append("| --- | --- | --- | --- | --- |")
    for module, count in counts.most_common():
        out.append(
            f"| `{module}` | {count} | {by_tier[module][1]} | {by_tier[module][2]} | {by_tier[module][3]} |"
        )
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", help="write markdown here instead of stdout")
    parser.add_argument(
        "--json", action="store_true", help="emit JSON records instead of markdown"
    )
    args = parser.parse_args(argv)

    adapter = get_adapter("sqlite:obo:mondo")
    entries = collect(adapter)
    if args.json:
        payload = json.dumps([asdict(e) for e in entries], indent=2)
    else:
        payload = render_markdown(entries)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(payload + "\n")
        print(f"wrote {args.out} ({len(entries)} entries)", file=sys.stderr)
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
