"""Validation tests for the phenotype matching LinkML schema."""

from pathlib import Path

from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from dismech.yaml_io import safe_load

ROOT_DIR = Path(__file__).resolve().parents[2]
MATCHING_SCHEMA_PATH = ROOT_DIR / "src" / "phenoagent" / "schema" / "matching.yaml"
VALID_MATCHING_FILE = ROOT_DIR / "tests" / "phenoagent" / "data" / "valid" / "MatchingRun-001.yaml"


def _matching_validator() -> Validator:
    # An explicit plugin is required: a plugin-less Validator returns an empty
    # report for any instance, making every assertion vacuous (dismech#11011).
    return Validator(
        MATCHING_SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_matching_schema_loads():
    """Ensure the matching schema compiles to JSON Schema.

    Constructing a Validator compiles nothing, so this generates the schema
    explicitly; an undeclared slot used to pass here unnoticed.
    """
    assert JsonSchemaGenerator(str(MATCHING_SCHEMA_PATH)).serialize()


def test_matching_validator_rejects_an_invalid_run():
    """Guard: the validator these tests use must actually report errors."""
    report = _matching_validator().validate(
        {"run_id": "x", "matches": [{"exact": "not a boolean", "bogus": 1}]},
        target_class="MatchingRun",
    )
    assert [r for r in report.results if r.severity.name == "ERROR"]


def test_valid_matching_run_example():
    """Ensure the matching example validates as a MatchingRun."""
    with open(VALID_MATCHING_FILE) as stream:
        data = safe_load(stream)

    report = _matching_validator().validate(data, target_class="MatchingRun")
    errors = [result for result in report.results if result.severity.name == "ERROR"]
    assert not errors, f"Validation errors in {VALID_MATCHING_FILE}: {[str(e) for e in errors]}"


def test_matching_explanation_ids_reference_shared_entries():
    """Matches should reference reusable explanation entries when pointers are present."""
    with open(VALID_MATCHING_FILE) as stream:
        data = safe_load(stream)

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
        data = safe_load(stream)

    model_only_rows = [
        row
        for row in data.get("matches", [])
        if isinstance(row, dict) and row.get("model_term_id") and not row.get("case_term_id")
    ]
    assert model_only_rows, "Expected at least one model-only row in example"
