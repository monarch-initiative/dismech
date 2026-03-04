"""Tests that build matching runs from example phenopackets."""

from pathlib import Path

import pytest
from linkml.validator import Validator

from phenoagent.matching import (
    build_matching_run_from_phenopacket,
    extract_case_phenotypes_from_phenopacket,
    load_phenopacket,
)

ROOT_DIR = Path(__file__).resolve().parents[2]
MATCHING_SCHEMA_PATH = ROOT_DIR / "src" / "phenoagent" / "schema" / "matching.yaml"
PHENOPACKET_DIR = ROOT_DIR / "tests" / "phenoagent" / "data" / "phenopackets"
LOCAL_PHENOPACKET_STORE = ROOT_DIR / "projects" / "PHENOPACKETS" / "files" / "phenopacket-store"


@pytest.mark.parametrize(
    ("fixture_name", "disease_slug"),
    [
        ("PMID_25681079_proband_FKT118.min.json", "Galactosemia"),
        ("PMID_35451551_proband.min.json", "Fanconi_Anemia"),
    ],
)
def test_build_matching_run_from_phenopacket_validates(fixture_name: str, disease_slug: str):
    """Ensure phenopacket-derived runs validate against MatchingRun schema."""
    phenopacket = load_phenopacket(PHENOPACKET_DIR / fixture_name)
    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug=disease_slug,
        run_id=f"test-{phenopacket['id']}",
    )

    assert run["matches"], "Expected at least one match row"
    validator = Validator(MATCHING_SCHEMA_PATH)
    report = validator.validate(run, target_class="MatchingRun")
    errors = [result for result in report.results if result.severity.name == "ERROR"]
    assert not errors, f"Validation errors for {fixture_name}: {[str(e) for e in errors]}"


def test_excluded_features_become_case_present_false():
    """Phenopacket excluded features should map to negative case phenotypes."""
    phenopacket = load_phenopacket(PHENOPACKET_DIR / "PMID_35451551_proband.min.json")
    rows = extract_case_phenotypes_from_phenopacket(phenopacket)

    assert any(row["case_present"] for row in rows)
    assert any(not row["case_present"] for row in rows)


@pytest.mark.parametrize(
    ("relative_path", "disease_slug"),
    [
        (
            "notebooks/GALT/phenopackets/PMID_25681079_proband_FKT118.json",
            "Galactosemia",
        ),
        (
            "notebooks/RAP1B/phenopackets/PMID_35451551_proband.json",
            "Fanconi_Anemia",
        ),
    ],
)
def test_local_phenopacket_store_examples_if_present(relative_path: str, disease_slug: str):
    """Use local phenopacket-store examples directly when available."""
    phenopacket_path = LOCAL_PHENOPACKET_STORE / relative_path
    if not phenopacket_path.exists():
        pytest.skip(f"Phenopacket store example missing: {phenopacket_path}")

    phenopacket = load_phenopacket(phenopacket_path)
    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug=disease_slug,
        run_id=f"test-{phenopacket.get('id', 'unknown')}",
    )

    validator = Validator(MATCHING_SCHEMA_PATH)
    report = validator.validate(run, target_class="MatchingRun")
    errors = [result for result in report.results if result.severity.name == "ERROR"]
    assert not errors, f"Validation errors for {phenopacket_path}: {[str(e) for e in errors]}"


def test_fanconi_matching_has_exact_hits_for_known_terms():
    """Terms shared between case and Fanconi model should resolve as exact."""
    phenopacket = load_phenopacket(PHENOPACKET_DIR / "PMID_35451551_proband.min.json")
    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug="Fanconi_Anemia",
        run_id="test-fanconi-exact",
    )

    by_case_id = {row["case_term_id"]: row for row in run["matches"] if row.get("case_term_id")}
    assert by_case_id["HP:0001873"]["model_term_id"] == "HP:0001873"
    assert by_case_id["HP:0001873"]["exact"] is True
    assert by_case_id["HP:0001903"]["model_term_id"] == "HP:0001903"
    assert by_case_id["HP:0001903"]["exact"] is True


def test_fanconi_unmatched_model_terms_are_emitted_as_model_only_rows():
    """Model terms with no case match should appear as model-only rows."""
    phenopacket = load_phenopacket(PHENOPACKET_DIR / "PMID_35451551_proband.min.json")
    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug="Fanconi_Anemia",
        run_id="test-fanconi-model-only",
    )

    model_only_rows = [row for row in run["matches"] if row.get("model_term_id") and not row.get("case_term_id")]
    assert model_only_rows, "Expected at least one model-only row"

    ventriculomegaly_rows = [row for row in model_only_rows if row.get("model_term_id") == "HP:0002119"]
    assert ventriculomegaly_rows, "Expected model-only row for Ventriculomegaly"

    vent = ventriculomegaly_rows[0]
    assert vent.get("model_label") == "Ventriculomegaly"
    assert "case_term_id" not in vent
    assert "case_present" not in vent
    assert vent["exact"] is False
    assert vent["case_is_broader"] is False
    assert vent["case_is_narrower"] is False
    assert vent["case_is_close"] is False
    assert vent["explanation_for_no_match"] == "NO_EXPLANATION"
    assert "similarity_percent" not in vent

    case_only_rows = [row for row in run["matches"] if row.get("case_term_id") and not row.get("model_term_id")]
    assert case_only_rows, "Expected at least one case-only row"
    assert case_only_rows[0]["explanation_for_no_match"] == "NO_EXPLANATION"
    assert "similarity_percent" not in case_only_rows[0]
    assert run["pr_is_diagnosis"] == 0.0


def test_all_non_exact_rows_have_default_explanation_pointer():
    """All exact=false rows should carry an explanation pointer from initialization."""
    phenopacket = load_phenopacket(PHENOPACKET_DIR / "PMID_35451551_proband.min.json")
    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug="Fanconi_Anemia",
        run_id="test-fanconi-non-exact-explanation-pointer",
    )

    non_exact_rows = [row for row in run["matches"] if row.get("exact") is False]
    assert non_exact_rows, "Expected at least one non-exact row"
    assert all(row.get("explanation_for_no_match") == "NO_EXPLANATION" for row in non_exact_rows)
