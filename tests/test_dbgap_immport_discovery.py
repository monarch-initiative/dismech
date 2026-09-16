"""Regression tests for dbGaP/ImmPort discovery and accession verification.

All offline: every test exercises pure functions, so nothing here hits dbGaP,
ImmPort, or NCBI.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from disease_title_match import (
    ADJECTIVAL_FORMS,
    compile_phrases,
    entry_phrases,
    fold_diacritics,
    inflected_variants,
    match_title,
    query_phrases,
)

from discover_dbgap_immport import (  # isort: skip
    ASSAY_TO_ENUM,
    BLOCKED_STUDIES,
    BLOCKED_TITLE_RE,
    DATA_DICT_RE,
    MAX_FHIR_PAGES,
    OUTCOME_CUES,
    _fhir_studies,
    _immport_total,
    _truncate,
    affection_signal,
    decode_body,
    infer_data_type,
    tier,
    to_record,
)
import discover_dbgap_immport  # isort: skip
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


# --------------------------------------------------------------------------- #
# Review round 1 (PR #10567) regressions
#
# Every test below reproduces a defect the reviewer found in the first round of
# this work. They are grouped here so a future change that reintroduces one is
# named rather than merely red.
# --------------------------------------------------------------------------- #


def test_every_adjectival_forms_key_is_reachable():
    """`head.lower().strip("'s")` strips a character *set*, not a suffix, so it
    ate the head noun's own trailing s: diabetes -> diabete, stenosis -> tenosi.
    Seven of the fourteen hand-verified pairs were unreachable, and the tests
    only exercised Asthma, one of the survivors."""
    unreachable = [key for key in ADJECTIVAL_FORMS if not inflected_variants(key)]
    assert unreachable == []


def test_inflected_variants_for_the_keys_that_used_to_be_unreachable():
    assert inflected_variants("Rheumatoid Arthritis") == ["Rheumatoid Arthritic"]
    assert inflected_variants("Psoriasis") == ["Psoriatic"]
    assert inflected_variants("Type 2 Diabetes") == ["Type 2 Diabetic", "Type 2 Diabetics"]


def test_a_possessive_head_still_reaches_the_table():
    """Dropping the possessive is what the strip was *for*; keep that working."""
    assert inflected_variants("Asthma's") == ["Asthmatic", "Asthmatics"]
    assert inflected_variants("Asthma\u2019s") == ["Asthmatic", "Asthmatics"]


def test_all_caps_titles_do_not_defeat_the_camelcase_relaxation():
    """Accepting any following uppercase letter admitted exactly the matches the
    module docstring says are blocked -- repository titles are full of ALL-CAPS
    fragments, and a phrase followed by more capitals is not a CamelCase seam."""
    for phrase, title in (
        ("Adenoma", "FAMILIAL ADENOMATOUS POLYPOSIS"),
        ("Adenoma", "Familial ADENOMATOUS Polyposis"),
        ("Lymphoma", "LYMPHOMATOID PAPULOSIS COHORT"),
    ):
        assert match_title(title, compile_phrases([phrase]), [])[0] == "", (phrase, title)


def test_camelcase_still_matches_after_the_all_caps_fix():
    patterns = compile_phrases(["Asthma"])
    assert match_title("AsthmaNet -APRIL and Oral Corticosteroids", patterns, [])[0] == "Asthma"
    assert match_title("The AsthmaNet Network", patterns, [])[0] == "Asthma"


def test_an_incidental_cue_in_the_same_variable_vetoes_the_outcome_reading():
    """A self-reported-diagnosis checkbox is what a mega-cohort records. Reading
    it as an outcome promoted the study to VARIABLE_MATCH, which is
    auto-approved -- the GTEx class of hit the tier exists to reject."""
    signal, _ = affection_signal(
        [("MHASTHMA", "Self-reported physician diagnosis of asthma (medical history)")],
        _ASTHMA,
    )
    assert signal == "INCIDENTAL"


def test_bare_diagnosis_of_is_no_longer_an_outcome_cue():
    assert affection_signal([("AST_DX", "Age at diagnosis of asthma")], _ASTHMA) == ("", "")
    assert not OUTCOME_CUES.search("Age at diagnosis of asthma")


def test_outcome_across_variables_still_wins_over_incidental():
    """The veto is per variable. A study carrying a history checkbox *and* a
    separate affection-status variable is still an outcome study."""
    signal, quoted = affection_signal(
        [
            ("MHASTHMA", "Self-reported asthma (medical history)"),
            ("Affection_Status", "Case or Control for asthma"),
        ],
        _ASTHMA,
    )
    assert signal == "OUTCOME"
    assert "Affection_Status" in quoted


def test_inflected_variants_are_not_issued_as_repository_queries():
    """dbGaP `condition:text=` searches MeSH entry terms and ImmPort
    `conditionOrDisease=` a curated disease field; neither holds "Asthmatic",
    so querying the variants is a wasted request per variant per entry."""
    phrases, _ = entry_phrases({"name": "Asthma"}, "Asthma")
    assert "Asthmatic" in phrases
    assert "Asthmatic" not in query_phrases(phrases)
    assert "Asthma" in query_phrases(phrases)


def test_fhir_search_follows_every_page(monkeypatch):
    """Reading only the first bundle silently truncated the coded pass, which is
    the pass the "same coverage as the catalog" argument rests on."""
    pages = {
        "https://x/?q=1": {
            "entry": [{"resource": {"id": "a"}}],
            "link": [{"relation": "next", "url": "https://x/?q=2"}],
        },
        "https://x/?q=2": {
            "entry": [{"resource": {"id": "b"}}, {"resource": {"id": "c"}}],
            "link": [{"relation": "self", "url": "https://x/?q=2"}],
        },
    }
    monkeypatch.setattr(discover_dbgap_immport, "DBGAP_FHIR", "https://x/")
    monkeypatch.setattr(discover_dbgap_immport, "http_json", lambda url, **kw: pages.get(url))
    monkeypatch.setitem(pages, "https://x/?q=1&_count=50&_format=json", pages["https://x/?q=1"])
    assert [s["id"] for s in _fhir_studies("q=1")] == ["a", "b", "c"]


def test_fhir_page_walk_is_capped_and_says_so(monkeypatch, capsys):
    """A server that always offers a next link must not loop forever, and the
    cap is reported when it bites -- the convention MAX_DICT_TABLES already set."""
    monkeypatch.setattr(discover_dbgap_immport, "DBGAP_FHIR", "https://x/")
    calls = {"n": 0}

    def endless(url, **kw):
        calls["n"] += 1
        return {
            "entry": [{"resource": {"id": str(calls["n"])}}],
            "link": [{"relation": "next", "url": f"https://x/?page={calls['n'] + 1}"}],
        }

    monkeypatch.setattr(discover_dbgap_immport, "http_json", endless)
    studies = _fhir_studies("condition=D001249")
    assert len(studies) == MAX_FHIR_PAGES
    assert "page cap" in capsys.readouterr().err


def test_fhir_page_walk_stops_on_a_self_referential_next_link(monkeypatch):
    monkeypatch.setattr(discover_dbgap_immport, "DBGAP_FHIR", "https://x/")
    same = "https://x/?condition=D1&_count=50&_format=json"
    monkeypatch.setattr(
        discover_dbgap_immport,
        "http_json",
        lambda url, **kw: {
            "entry": [{"resource": {"id": "a"}}],
            "link": [{"relation": "next", "url": same}],
        },
    )
    assert len(_fhir_studies("condition=D1")) == 1


def test_immport_total_is_read_from_either_response_shape():
    assert _immport_total({"hits": {"total": 12}}) == 12
    assert _immport_total({"hits": {"total": {"value": 12}}}) == 12
    assert _immport_total({"hits": {}}) is None
    assert _immport_total(None) is None


def test_immport_truncation_is_reported_not_silent(capsys):
    discover_dbgap_immport._report_immport_truncation("Asthma", {"hits": {"total": 56}}, 10)
    assert "truncated" in capsys.readouterr().err


def test_immport_reports_nothing_when_the_page_held_everything(capsys):
    discover_dbgap_immport._report_immport_truncation("Asthma", {"hits": {"total": 10}}, 10)
    assert capsys.readouterr().err == ""


def test_truncation_never_appends_a_period_to_a_mid_word_cut():
    """`desc[:700].rsplit(". ", 1)[0] + "."` returned the raw slice plus a full
    stop whenever the slice held no sentence break, punctuating a cut word as
    though the sentence ended there."""
    long_clause = "supercalifragilistic " * 60
    out = _truncate(long_clause, limit=700)
    # An ellipsis reads as truncated; a bare full stop reads as a finished
    # sentence, which is what the old expression produced.
    assert out.endswith("...")
    assert not out[:-3].endswith(".")
    # ...and the cut lands on a word boundary, so no half word is quoted.
    assert out[:-3].split()[-1] == "supercalifragilistic"
    assert len(out) <= 700 + 3


def test_truncation_prefers_a_whole_sentence_when_there_is_one():
    text = "First sentence here. " + "filler word " * 100
    out = _truncate(text, limit=700)
    assert out == "First sentence here."


def test_short_descriptions_are_left_alone():
    assert _truncate("Short enough.", limit=700) == "Short enough."


def test_dbgap_resolver_reports_a_study_with_no_phs_identifier(monkeypatch):
    """The identity guard was skipped entirely when the FHIR resource carried no
    phs identifier, so an unconfirmable response fell through to OK. "We could
    not confirm this is the study you asked for" is a different answer from
    "it is"."""
    import verify_dataset_accessions as vda

    monkeypatch.setattr(
        vda,
        "http_json",
        lambda url, **kw: {"entry": [{"resource": {"title": "Some Study", "identifier": []}}]},
    )
    status, title, note, extra = vda.resolve_dbgap("phs001289.v1.p1", None, None)
    assert status == vda.ERROR
    assert "no phs identifier" in note


def test_dbgap_resolver_reports_the_canonical_versioned_accession(monkeypatch):
    import verify_dataset_accessions as vda

    monkeypatch.setattr(
        vda,
        "http_json",
        lambda url, **kw: {
            "entry": [
                {
                    "resource": {
                        "title": "Asthma Study",
                        "identifier": [{"value": "phs001289.v2.p1"}],
                        "condition": [{"text": "Asthma"}],
                    }
                }
            ]
        },
    )
    status, title, _, extra = vda.resolve_dbgap("phs001289.v1.p1", None, None)
    assert status == vda.OK
    assert extra["canonical_accession"] == "phs001289.v2.p1"
    assert "dbGaP current is phs001289.v2.p1" in extra["version_note"]


def test_immport_resolver_reports_organism_as_a_scalar(monkeypatch):
    """`extra["organism"]` is a scalar in every other resolver; ImmPort returns
    a list, and letting one key change shape by prefix is a trap downstream."""
    import verify_dataset_accessions as vda

    monkeypatch.setattr(
        vda,
        "http_json",
        lambda url, **kw: {
            "hits": {
                "hits": [
                    {
                        "_source": {
                            "study_accession": "SDY1679",
                            "brief_title": "A study",
                            "species": ["Homo sapiens"],
                        }
                    }
                ]
            }
        },
    )
    status, title, _, extra = vda.resolve_immport("SDY1679", None, None)
    assert status == vda.OK
    assert extra["organism"] == "Homo sapiens"
