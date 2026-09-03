"""Regression tests for dbGaP/ImmPort discovery and accession verification.

All offline: every test exercises pure functions, so nothing here hits dbGaP,
ImmPort, or NCBI.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from disease_title_match import (
    compile_phrases,
    entry_phrases,
    fold_diacritics,
    inflected_variants,
    match_title,
)

from discover_dbgap_immport import (  # isort: skip
    ASSAY_TO_ENUM,
    BLOCKED_STUDIES,
    BLOCKED_TITLE_RE,
    DATA_DICT_RE,
    affection_signal,
    decode_body,
    infer_data_type,
    tier,
    to_record,
)
from verify_dataset_accessions import RESOLVERS, SHAPE  # isort: skip


# --------------------------------------------------------------------------- #
# Diacritic folding
#
# dbGaP writes "Sjögren's Syndrome"; the KB entry is Sjogrens_Syndrome. Before
# folding, two on-target studies were scored SUBJECT_ONLY as though the disease
# were absent from the title.
# --------------------------------------------------------------------------- #


def test_diacritic_title_matches_ascii_entry_name():
    patterns = compile_phrases(["Sjogren's Syndrome"])
    matched, conflict = match_title(
        "RNAseq of Sjögren's Syndrome and Healthy Volunteers' Salivary Glands",
        patterns,
        [],
    )
    assert matched == "Sjogren's Syndrome"
    assert conflict == ""


def test_matched_phrase_reported_is_the_entry_spelling_not_the_folded_one():
    """Curators and provenance notes see the phrase the entry actually uses."""
    patterns = compile_phrases(["Behçet disease"])
    matched, _ = match_title("Genomics of Behcet disease", patterns, [])
    assert matched == "Behçet disease"


def test_folding_does_not_dissolve_word_boundaries():
    """Folding must not weaken the guard that keeps Pick out of Niemann-Pick."""
    patterns = compile_phrases(["Pick disease"])
    matched, _ = match_title("Niemann-Pick disease type C fibroblasts", patterns, [])
    assert matched == ""


def test_fold_diacritics_leaves_ascii_untouched():
    assert fold_diacritics("Sjogren's Syndrome") == "Sjogren's Syndrome"


# --------------------------------------------------------------------------- #
# Relevance tiering
# --------------------------------------------------------------------------- #


def _hit(title, **kw):
    base = {
        "title": title,
        "description": "",
        "conditions": ["Bronchiectasis"],
        "design": "",
        "pubmed_ids": [],
        "sample_count": None,
        "organism": "Homo sapiens",
        "route": "MeSH D001987",
        "repository": "dbGaP",
        "accession": "dbgap:phs000518.v1.p1",
    }
    base.update(kw)
    return base


def test_disease_named_in_title_is_title_match():
    patterns = compile_phrases(["Bronchiectasis"])
    assert tier(_hit("NHLBI GO-ESP Family Studies: Idiopathic Bronchiectasis"), patterns, [])[0] == (
        "TITLE_MATCH"
    )


def test_coded_but_unnamed_study_is_subject_only_not_title_match():
    """The incidental-mega-cohort class: coded to the disease, not about it."""
    patterns = compile_phrases(["Asthma"])
    assert tier(_hit("Bogalusa Heart Study (BHS-BioLINCC)"), patterns, [])[0] == "SUBJECT_ONLY"


def test_subject_only_records_are_not_auto_approved():
    rec = to_record(_hit("Yale Center for Mendelian Genomics"), "SUBJECT_ONLY", "", "2026-08-07")
    assert "NOT named" in rec["notes"]


# --------------------------------------------------------------------------- #
# Record construction
# --------------------------------------------------------------------------- #


def test_study_design_is_never_inferred_as_a_data_type():
    """`category` is the study design, not the assay.

    Mapping dbGaP's "Case-Control" to GWAS labelled an RNAseq study of salivary
    glands as a genome-wide association study.
    """
    assert infer_data_type(_hit("x", design="Case-Control")) == ""
    assert infer_data_type(_hit("x", design="Cross-Sectional")) == ""


def test_immport_assay_method_maps_to_data_type():
    hit = _hit("x", repository="ImmPort", assay_methods=["RNA sequencing"])
    assert infer_data_type(hit) == ASSAY_TO_ENUM["rna sequencing"]


def test_unrecognised_assay_leaves_data_type_unset():
    hit = _hit("x", repository="ImmPort", assay_methods=["ELISA"])
    assert infer_data_type(hit) == ""


def test_immport_pmid_and_enrollment_reach_the_record():
    """The fields the NIH Dataset Catalog could not supply for any repository."""
    hit = _hit(
        "Asthma cohort",
        repository="ImmPort",
        accession="immport:SDY1027",
        pubmed_ids=["25769910"],
        sample_count=200,
    )
    rec = to_record(hit, "TITLE_MATCH", "Asthma", "2026-08-07")
    assert rec["publication"] == "PMID:25769910"
    assert rec["sample_count"] == 200
    assert rec["organism"]["term"]["id"] == "NCBITaxon:9606"


def test_non_human_organism_is_not_reported_as_human():
    hit = _hit("Mouse model", repository="ImmPort", organism="Mus musculus")
    rec = to_record(hit, "TITLE_MATCH", "x", "2026-08-07")
    assert rec["organism"]["term"]["id"] == "NCBITaxon:10090"


def test_unknown_organism_is_omitted_rather_than_guessed():
    rec = to_record(_hit("x", organism=""), "TITLE_MATCH", "x", "2026-08-07")
    assert "organism" not in rec


# --------------------------------------------------------------------------- #
# Mixed-encoding decode
#
# dbGaP FHIR declares charset=iso-8859-1 but serves mostly-UTF-8 text with the
# occasional raw latin-1 byte. errors="replace" planted U+FFFD into curated
# description text.
# --------------------------------------------------------------------------- #


def test_raw_latin1_byte_inside_utf8_body_decodes_without_replacement_char():
    raw = "molecular mechanisms of Sj".encode() + b"\xf6" + "gren's syndrome".encode()
    decoded = decode_body(raw)
    assert decoded == "molecular mechanisms of Sjögren's syndrome"
    assert "�" not in decoded


def test_well_formed_utf8_is_unaffected():
    raw = "Sjögren's Syndrome".encode()
    assert decode_body(raw) == "Sjögren's Syndrome"


# --------------------------------------------------------------------------- #
# Verifier registration
# --------------------------------------------------------------------------- #


def test_immport_prefix_is_resolvable_and_shape_checked():
    assert "immport" in RESOLVERS
    assert SHAPE["immport"].match("SDY1679")
    assert not SHAPE["immport"].match("SDY")
    assert not SHAPE["immport"].match("phs001289")


def test_dbgap_resolver_does_not_use_the_withdrawn_eutils_gap_db():
    """NCBI removed db=gap; using it reported NOT_FOUND for every real study,
    which the curation SOP reads as "treat as fabricated"."""
    source = Path(__file__).resolve().parents[1] / "scripts" / "verify_dataset_accessions.py"
    body = source.read_text()
    start = body.index("def resolve_dbgap")
    end = body.index("def resolve_immport")
    assert '_eutils_lookup("gap"' not in body[start:end]
    assert "DBGAP_FHIR" in body[start:end]


def test_immport_prefix_is_declared_in_the_schema():
    schema = Path(__file__).resolve().parents[1] / "src" / "dismech" / "schema" / "dismech.yaml"
    assert "immport: https://www.immport.org/shared/study/" in schema.read_text()


# --------------------------------------------------------------------------- #
# CamelCase compound boundary
#
# dbGaP names a trial network "AsthmaNet". Only an uppercase next character
# relaxes the trailing boundary, so this cannot also admit "Lymphomatoid".
# --------------------------------------------------------------------------- #


def test_camelcase_compound_counts_as_naming_the_disease():
    patterns = compile_phrases(["Asthma"])
    matched, _ = match_title("AsthmaNet -APRIL and Oral Corticosteroids", patterns, [])
    assert matched == "Asthma"


def test_lowercase_suffix_is_still_not_a_match():
    """The compound rule must not become a blanket prefix match."""
    patterns = compile_phrases(["Lymphoma"])
    assert match_title("Lymphomatoid papulosis cohort", patterns, [])[0] == ""
    patterns = compile_phrases(["Adenoma"])
    assert match_title("Familial adenomatous polyposis", patterns, [])[0] == ""


# --------------------------------------------------------------------------- #
# Inflected forms
# --------------------------------------------------------------------------- #


def test_inflected_variant_is_derived_for_a_known_head_noun():
    assert inflected_variants("Asthma") == ["Asthmatic", "Asthmatics"]
    assert inflected_variants("Severe Asthma") == ["Severe Asthmatic", "Severe Asthmatics"]


def test_inflected_variants_are_not_invented_for_unlisted_heads():
    """The table is hand-verified, not productive -- an unknown head yields none."""
    assert inflected_variants("Lymphoma") == []
    assert inflected_variants("Bronchiectasis") == []


def test_entry_phrases_include_the_inflected_form():
    phrases, _ = entry_phrases({"name": "Asthma"}, "Asthma")
    assert "Asthmatic" in phrases
    patterns = compile_phrases(phrases)
    assert match_title("Sputum RNA-Seq from Asthmatic Patients", patterns, [])[0]


# --------------------------------------------------------------------------- #
# Data-dictionary affection signal
#
# The variable's role decides, not its presence. Both examples below mention
# asthma; only the first is an asthma study.
# --------------------------------------------------------------------------- #

_ASTHMA = compile_phrases(["Asthma"])


def test_affection_status_variable_marks_the_study_as_an_outcome_study():
    signal, quoted = affection_signal(
        [("Affection_Status", "Childhood asthma case or control")], _ASTHMA
    )
    assert signal == "OUTCOME"
    assert "Affection_Status" in quoted


def test_medical_history_variable_is_incidental_not_an_outcome():
    """GTEx is MeSH-coded for asthma and is not an asthma study."""
    signal, quoted = affection_signal(
        [("MHASTHMA", "Asthma (General Medical History)")], _ASTHMA
    )
    assert signal == "INCIDENTAL"
    assert "MHASTHMA" in quoted


def test_variable_not_mentioning_the_disease_gives_no_signal():
    assert affection_signal([("BMI", "Body mass index")], _ASTHMA) == ("", "")


def test_outcome_beats_incidental_when_a_study_has_both():
    signal, _ = affection_signal(
        [
            ("MHASTHMA", "Asthma (General Medical History)"),
            ("Affection_Status", "Case or Control for asthma"),
        ],
        _ASTHMA,
    )
    assert signal == "OUTCOME"


def test_var_report_files_are_never_read():
    """var_report holds cohort distributions, not clinical reference intervals;
    curating one into reference_ranges would record a misleading number."""
    source = Path(__file__).resolve().parents[1] / "scripts" / "discover_dbgap_immport.py"
    body = source.read_text()
    assert "var_report" not in DATA_DICT_RE.pattern
    assert "var_report.xml" not in body.replace("*.var_report.xml", "")


# --------------------------------------------------------------------------- #
# Test-fixture studies
# --------------------------------------------------------------------------- #


def test_fhir_test_study_is_blocked():
    """NCBI's FHIR service carries fixtures coded like real studies."""
    assert "phs002409" in BLOCKED_STUDIES
    assert BLOCKED_TITLE_RE.search("FHIR Test Study's ALPHA")
    assert not BLOCKED_TITLE_RE.search("Genome Wide Association Study of Asthma")
