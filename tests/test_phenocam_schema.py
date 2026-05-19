"""Schema validation tests for PhenoCAM V2."""

import glob
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "phenocam" / "phenocam.yaml"
# Used in Tasks 7-8 when example module/disease files are added
MODULES_DIR = ROOT_DIR / "causal_models" / "modules"
DISEASES_DIR = ROOT_DIR / "causal_models" / "diseases"


@pytest.fixture(scope="module")
def validator():
    return Validator(SCHEMA_PATH)


def test_schema_exists():
    assert SCHEMA_PATH.exists(), f"Schema not found at {SCHEMA_PATH}"


def test_schema_loadable(validator):
    """Schema loads and contains the Module class."""
    schema_view = validator._schema
    assert "Module" in schema_view.classes, "Expected Module class in schema"


def test_module_validator_accepts_minimal_module(validator):
    data = {"id": "test_module", "name": "Test Module"}
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected errors: {[str(e) for e in errors]}"


def test_invalid_perturbation_quality_rejected(validator):
    """Schema rejects unknown perturbation quality values."""
    data = {
        "id": "test_module",
        "name": "Test",
        "molecular_activities": [
            {
                "id": "act1",
                "gene": {"symbol": "SMO", "hgnc_id": "hgnc:11119"},
                "quality": "NOT_A_VALID_QUALITY",
            }
        ],
    }
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for invalid quality value"
