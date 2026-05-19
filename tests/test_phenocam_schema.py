"""Schema validation tests for PhenoCAM V2."""

import glob
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "phenocam" / "phenocam.yaml"
MODULES_DIR = ROOT_DIR / "causal_models" / "modules"
DISEASES_DIR = ROOT_DIR / "causal_models" / "diseases"


@pytest.fixture(scope="module")
def validator():
    return Validator(SCHEMA_PATH)


def test_schema_exists():
    assert SCHEMA_PATH.exists(), f"Schema not found at {SCHEMA_PATH}"


def test_schema_loadable(validator):
    assert validator is not None


def test_module_validator_accepts_minimal_module(validator):
    data = {"id": "test_module", "name": "Test Module"}
    report = validator.validate(data, target_class="Module")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected errors: {[str(e) for e in errors]}"
