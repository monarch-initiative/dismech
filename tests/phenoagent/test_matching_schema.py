"""Validation tests for the phenotype matching LinkML schema."""

from pathlib import Path

import yaml
from linkml.validator import Validator

ROOT_DIR = Path(__file__).resolve().parents[2]
MATCHING_SCHEMA_PATH = ROOT_DIR / "src" / "phenoagent" / "schema" / "matching.yaml"
VALID_MATCHING_FILE = ROOT_DIR / "tests" / "phenoagent" / "data" / "valid" / "MatchingRun-001.yaml"


def test_matching_schema_loads():
    """Ensure the matching schema is valid LinkML."""
    validator = Validator(MATCHING_SCHEMA_PATH)
    assert validator is not None


def test_valid_matching_run_example():
    """Ensure the matching example validates as a MatchingRun."""
    with open(VALID_MATCHING_FILE) as stream:
        data = yaml.safe_load(stream)

    validator = Validator(MATCHING_SCHEMA_PATH)
    report = validator.validate(data, target_class="MatchingRun")
    errors = [result for result in report.results if result.severity.name == "ERROR"]
    assert not errors, f"Validation errors in {VALID_MATCHING_FILE}: {[str(e) for e in errors]}"


def test_matching_explanation_ids_reference_shared_entries():
    """Matches should reference reusable explanation entries when pointers are present."""
    with open(VALID_MATCHING_FILE) as stream:
        data = yaml.safe_load(stream)

    explanations = data.get("explanations", [])
    explanation_ids = {
        explanation["explanation_id"]
        for explanation in explanations
        if isinstance(explanation, dict) and explanation.get("explanation_id")
    }
    match_explanation_ids = [
        match["explanation_for_no_match"]
        for match in data.get("matches", [])
        if isinstance(match, dict) and match.get("explanation_for_no_match")
    ]

    assert "NO_EXPLANATION" in explanation_ids
    assert match_explanation_ids, "Expected at least one match-level explanation pointer"
    assert set(match_explanation_ids).issubset(explanation_ids)


def test_matching_example_includes_model_only_row():
    """Example should permit rows with model fields present and case fields omitted."""
    with open(VALID_MATCHING_FILE) as stream:
        data = yaml.safe_load(stream)

    model_only_rows = [
        row
        for row in data.get("matches", [])
        if isinstance(row, dict) and row.get("model_term_id") and not row.get("case_term_id")
    ]
    assert model_only_rows, "Expected at least one model-only row in example"
