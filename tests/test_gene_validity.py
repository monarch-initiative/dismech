"""Tests for ``Genetic.gene_disease_validity`` and its audit (#10179).

A gene-disease validity tier is only meaningful under the framework that
assigned it, so the schema requires every recorded tier to say who assigned it.
When the assigner is ClinGen, the tier is already written down in the cached
``CGGV:`` assertion, so ``scripts/check_gene_validity.py`` can compare the two
without judgement. These tests pin both halves: the schema contract, and the
rules that keep the comparison honest (a tier belongs to a gene-disease *pair*,
so an assertion for another disease must never fill the slot).
"""

import sys
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

# Inline the path rather than assigning ROOT first, for ruff's E402 allowance
# (same preamble as tests/test_causal_targets.py, #9964).
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_gene_validity as mod
from check_gene_validity import assess, parse_assertion

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"

ALS22 = "CGGV:assertion_aaaa-2025-03-27T160000.000Z"
MACRO = "CGGV:assertion_bbbb-2023-11-06T170000.000Z"
ALS22_AR = "CGGV:assertion_cccc-2024-01-01T000000.000Z"


# --- schema ------------------------------------------------------------------


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        SCHEMA_PATH, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


def _disease(*assertions):
    return {
        "name": "Probe",
        "genetic": [
            {
                "name": "HGD",
                "relationship_type": "CAUSATIVE",
                "gene_disease_validity": list(assertions),
            }
        ],
    }


def _errors(validator, data):
    report = validator.validate(data, target_class="Disease")
    return [str(r.message) for r in report.results if r.severity.name == "ERROR"]


def test_attributed_classification_validates(validator):
    data = _disease(
        {
            "validity_classification": "DEFINITIVE",
            "classified_by": "CLINGEN",
            "external_id": ALS22,
        }
    )
    assert _errors(validator, data) == []


def test_a_tier_without_its_source_is_rejected(validator):
    """The point of #10179: dismech must not record a tier nobody assigned."""
    data = _disease({"validity_classification": "MODERATE"})
    assert any("classified_by" in e for e in _errors(validator, data))


def test_a_source_without_a_tier_is_rejected(validator):
    data = _disease({"classified_by": "CLINGEN"})
    assert any("validity_classification" in e for e in _errors(validator, data))


def test_there_is_no_curator_or_dismech_source(schema_view):
    sources = set(
        schema_view.get_enum("GeneDiseaseValiditySourceEnum").permissible_values
    )
    assert not {s for s in sources if "CURATOR" in s or "DISMECH" in s}


def test_classification_values_are_the_gencc_tiers_in_use(schema_view):
    """Pinned to the GenCC submissions export read on 2026-09-23.

    GENCC:100007 had no submissions, so there is deliberately no
    ANIMAL_MODEL_ONLY value.
    """
    enum = schema_view.get_enum("GeneDiseaseValidityClassificationEnum")
    curies = {
        name: pv.annotations["gencc_classification"].value
        for name, pv in enum.permissible_values.items()
    }
    assert curies == {
        "DEFINITIVE": "GENCC:100001",
        "STRONG": "GENCC:100002",
        "MODERATE": "GENCC:100003",
        "LIMITED": "GENCC:100004",
        "DISPUTED": "GENCC:100005",
        "REFUTED": "GENCC:100006",
        "NO_KNOWN_DISEASE_RELATIONSHIP": "GENCC:100008",
        "SUPPORTIVE": "GENCC:100009",
    }


def test_every_clingen_label_maps_onto_the_enum(schema_view):
    values = set(
        schema_view.get_enum("GeneDiseaseValidityClassificationEnum").permissible_values
    )
    assert set(mod.CLINGEN_TO_ENUM.values()) <= values


def test_relationship_type_is_unchanged(schema_view):
    """Validity is a separate axis; the relationship enum keeps its values."""
    values = set(schema_view.get_enum("GeneDiseaseRelationshipEnum").permissible_values)
    assert {"CAUSATIVE", "DISPUTED", "UNKNOWN"} <= values
    assert not values & {"MODERATE", "LIMITED"}


# --- audit fixtures ----------------------------------------------------------


def _cache_file(gene, hgnc, disease, mondo, moi, classification):
    return (
        "---\n"
        'database: "ClinGen"\n'
        "---\n\n"
        "## Evidence summary\n\n"
        "Narrative | with | pipes that must not parse as a row.\n\n"
        "## Gene-disease validity\n\n"
        "| Gene | HGNC | Disease | MONDO | MOI | Classification | SOP | GCEP "
        "| Classification date |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        f"| {gene} | {hgnc} | {disease} | {mondo} | {moi} | {classification} "
        "| SOP10 | Some GCEP | 2025-03-27T16:00:00.000Z |\n\n"
        "## Online report\n\n- Curation ID: CCID:000001\n"
    )


@pytest.fixture
def cache(tmp_path):
    rows = {
        ALS22: ("TUBA4A", "HGNC:12407", "ALS 22", "MONDO:0014531", "AD", "Moderate"),
        MACRO: ("TUBA4A", "HGNC:12407", "macro", "MONDO:0000001", "AD", "Limited"),
        ALS22_AR: (
            "TUBA4A",
            "HGNC:12407",
            "ALS 22",
            "MONDO:0014531",
            "AR",
            "Definitive",
        ),
    }
    for curie, row in rows.items():
        mod.cache_path(curie, tmp_path).write_text(_cache_file(*row), encoding="utf-8")
    return tmp_path


def _entry(
    *cited, recorded=(), relationship="CAUSATIVE", mondo="MONDO:0014531", **extra
):
    record = {
        "name": "TUBA4A",
        "relationship_type": relationship,
        "gene_term": {"term": {"id": "hgnc:12407", "label": "TUBA4A"}},
        "evidence": [{"reference": c} for c in cited],
    }
    if recorded:
        record["gene_disease_validity"] = list(recorded)
    data = {
        "name": "Probe",
        "disease_term": {"term": {"id": mondo}},
        "genetic": [record],
    }
    data.update(extra)
    return data


def _clingen(curie, tier):
    return {
        "validity_classification": tier,
        "classified_by": "CLINGEN",
        "external_id": curie,
    }


def _kinds(findings):
    return sorted((f.kind, f.clingen) for f in findings)


# --- parsing -----------------------------------------------------------------


def test_parses_the_validity_row_and_ignores_narrative_pipes():
    text = _cache_file(
        "SOX10", "HGNC:11190", "WS4C", "MONDO:0013202", "AD", "Definitive"
    )
    a = parse_assertion("CGGV:x", text)
    assert (a.gene, a.hgnc, a.mondo, a.moi, a.classification) == (
        "SOX10",
        "hgnc:11190",
        "MONDO:0013202",
        "AD",
        "DEFINITIVE",
    )


def test_every_committed_cggv_cache_file_parses():
    """The parser must read the real cache, not only the fixture's shape."""
    files = sorted((ROOT / "references_cache").glob("CGGV_*.md"))
    assert files, "expected committed CGGV cache files"
    unparsed = [
        f.name
        for f in files
        if parse_assertion(f.stem.replace("_", ":", 1), f.read_text(encoding="utf-8"))
        is None
    ]
    assert unparsed == []


# --- audit -------------------------------------------------------------------


def test_cited_same_disease_assertion_is_a_backfill_candidate(cache):
    findings = assess(_entry(ALS22, relationship="RISK_FACTOR"), "x.yaml", cache)
    assert _kinds(findings) == [("backfill", "MODERATE")]


def test_matching_recorded_assertion_is_clean(cache):
    data = _entry(
        ALS22, recorded=[_clingen(ALS22, "MODERATE")], relationship="RISK_FACTOR"
    )
    assert assess(data, "x.yaml", cache) == []


def test_recorded_tier_that_disagrees_with_its_record_is_a_conflict(cache):
    data = _entry(ALS22, recorded=[_clingen(ALS22, "DEFINITIVE")])
    assert ("conflict", "MODERATE") in _kinds(assess(data, "x.yaml", cache))


def test_recorded_id_for_another_gene_is_a_conflict(cache):
    data = _entry(ALS22, recorded=[_clingen(ALS22, "MODERATE")])
    data["genetic"][0]["gene_term"]["term"] = {"id": "hgnc:1", "label": "OTHER"}
    kinds = {f.kind for f in assess(data, "x.yaml", cache)}
    assert "conflict" in kinds


def test_clingen_tier_without_a_cggv_id_is_unsourced(cache):
    data = _entry(
        recorded=[{"validity_classification": "MODERATE", "classified_by": "CLINGEN"}]
    )
    assert _kinds(assess(data, "x.yaml", cache)) == [("unsourced", "")]


def test_non_clingen_sources_are_not_checked(cache):
    data = _entry(
        recorded=[{"validity_classification": "LIMITED", "classified_by": "G2P"}],
        relationship="RISK_FACTOR",
    )
    assert assess(data, "x.yaml", cache) == []


def test_two_same_disease_assertions_are_two_backfill_rows(cache):
    """Two modes of inheritance: each assertion is recorded separately."""
    findings = assess(
        _entry(ALS22, ALS22_AR, relationship="RISK_FACTOR"), "x.yaml", cache
    )
    assert _kinds(findings) == [("backfill", "DEFINITIVE"), ("backfill", "MODERATE")]
    details = " ".join(f.detail for f in findings)
    assert " AD (" in details and " AR (" in details


def test_recording_one_assertion_leaves_the_other_as_backfill(cache):
    data = _entry(
        ALS22,
        ALS22_AR,
        recorded=[_clingen(ALS22_AR, "DEFINITIVE")],
        relationship="RISK_FACTOR",
    )
    assert _kinds(assess(data, "x.yaml", cache)) == [("backfill", "MODERATE")]


def test_assertion_for_another_disease_is_never_backfill(cache):
    """The gene's second disease is not this entry's tier."""
    findings = assess(_entry(MACRO), "x.yaml", cache)
    assert _kinds(findings) == [("other_disease", "LIMITED")]


def test_exact_match_mapping_counts_as_the_entry_disease(cache):
    mappings = {
        "mondo_mappings": [
            {"term": {"id": "MONDO:0000001"}, "mapping_predicate": "skos:exactMatch"}
        ]
    }
    findings = assess(
        _entry(MACRO, mondo="MONDO:9", mappings=mappings), "x.yaml", cache
    )
    assert ("backfill", "LIMITED") in _kinds(findings)


def test_broad_match_mapping_does_not(cache):
    mappings = {
        "mondo_mappings": [
            {"term": {"id": "MONDO:0000001"}, "mapping_predicate": "skos:broadMatch"}
        ]
    }
    findings = assess(
        _entry(MACRO, mondo="MONDO:9", mappings=mappings), "x.yaml", cache
    )
    assert _kinds(findings) == [("other_disease", "LIMITED")]


def test_subtype_term_counts_as_the_entry_disease(cache):
    subtypes = [{"name": "Macro", "subtype_term": {"term": {"id": "MONDO:0000001"}}}]
    findings = assess(
        _entry(MACRO, mondo="MONDO:9", has_subtypes=subtypes), "x.yaml", cache
    )
    assert ("backfill", "LIMITED") in _kinds(findings)


def test_causative_below_strong_is_overstated(cache):
    findings = assess(_entry(ALS22), "x.yaml", cache)
    assert ("overstated", "MODERATE") in _kinds(findings)


def test_causative_is_not_overstated_by_another_disease(cache):
    findings = assess(_entry(MACRO), "x.yaml", cache)
    assert "overstated" not in {f.kind for f in findings}


def test_uncached_citation_is_reported(cache):
    findings = assess(_entry("CGGV:assertion_zzzz-2020"), "x.yaml", cache)
    assert _kinds(findings) == [("uncached", "")]


def test_gene_match_prefers_hgnc_over_symbol(cache):
    """A record bound to another HGNC id must not match on a shared name."""
    data = _entry(ALS22)
    data["genetic"][0]["gene_term"]["term"] = {"id": "hgnc:1", "label": "TUBA4A"}
    assert assess(data, "x.yaml", cache) == []


def test_symbol_match_when_no_hgnc_is_bound(cache):
    data = _entry(ALS22)
    del data["genetic"][0]["gene_term"]
    assert ("backfill", "MODERATE") in _kinds(assess(data, "x.yaml", cache))


# --- attribution to the record that cites the assertion ----------------------


def _two_records(cited_in_causative=True, entry_level=False):
    """A causative row and a susceptibility row for the same gene (review #1)."""
    causative = {
        "name": "TUBA4A causative",
        "relationship_type": "CAUSATIVE",
        "gene_term": {"term": {"id": "hgnc:12407", "label": "TUBA4A"}},
        "evidence": [{"reference": ALS22}] if cited_in_causative else [],
    }
    susceptibility = {
        "name": "TUBA4A susceptibility",
        "relationship_type": "SUSCEPTIBILITY",
        "gene_term": {"term": {"id": "hgnc:12407", "label": "TUBA4A"}},
    }
    data = {
        "name": "Probe",
        "disease_term": {"term": {"id": "MONDO:0014531"}},
        "genetic": [causative, susceptibility],
    }
    if entry_level:
        data["external_assertions"] = [{"source": "ClinGen", "external_id": ALS22}]
    return data


def test_assertion_is_attributed_only_to_the_record_that_cites_it(cache):
    """A ClinGen tier must not be offered for a susceptibility row it never classified."""
    findings = assess(_two_records(), "x.yaml", cache)
    backfill = [f for f in findings if f.kind == "backfill"]
    assert [f.record for f in backfill] == ["TUBA4A causative"]


def test_overstated_follows_the_same_attribution(cache):
    findings = assess(_two_records(), "x.yaml", cache)
    assert [f.record for f in findings if f.kind == "overstated"] == [
        "TUBA4A causative"
    ]


def test_entry_level_citation_with_several_records_is_unplaced_once(cache):
    data = _two_records(cited_in_causative=False, entry_level=True)
    findings = assess(data, "x.yaml", cache)
    assert _kinds(findings) == [("unplaced", "MODERATE")]
    assert "TUBA4A causative" in findings[0].detail
    assert "TUBA4A susceptibility" in findings[0].detail


def test_entry_level_citation_with_one_record_is_attributed_to_it(cache):
    data = _entry(relationship="RISK_FACTOR")
    data["external_assertions"] = [{"source": "ClinGen", "external_id": ALS22}]
    findings = assess(data, "x.yaml", cache)
    assert [(f.kind, f.record) for f in findings] == [("backfill", "TUBA4A")]


def test_committed_kb_reports_no_duplicate_rows():
    """Each (record, assertion) pair appears at most once in the worklist."""
    findings, errors = mod.collect([])
    assert errors == []
    keys = [(f.path, f.kind, f.record, f.detail) for f in findings]
    assert len(keys) == len(set(keys))


# --- CLI ---------------------------------------------------------------------


def test_conflict_fails_the_run_and_report_mode_does_not(
    cache, tmp_path, monkeypatch, capsys
):
    monkeypatch.setattr(mod, "CACHE_DIR", cache)
    path = tmp_path / "Probe.yaml"
    path.write_text(
        yaml.safe_dump(_entry(ALS22, recorded=[_clingen(ALS22, "DEFINITIVE")])),
        encoding="utf-8",
    )
    assert mod.main([str(path)]) == 1
    assert "contradict" in capsys.readouterr().err
    assert mod.main([str(path), "--report"]) == 0


def test_missing_path_is_a_usage_error(tmp_path, capsys):
    assert mod.main([str(tmp_path / "Nope.yaml")]) == 2
    assert "Nope.yaml" in capsys.readouterr().err


def test_committed_kb_has_no_conflicts():
    """The gate itself, over the real KB."""
    assert mod.main(["--kind", "conflict"]) == 0
