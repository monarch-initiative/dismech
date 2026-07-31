"""Tests for disease-level clinical burden schema support."""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def strict_validator() -> Validator:
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_clinical_burden_enum_defined(schema_view):
    enum = schema_view.get_enum("ClinicalBurdenLevelEnum")
    assert enum is not None
    assert set(enum.permissible_values) == {
        "LOW",
        "MODERATE",
        "HIGH",
        "VARIABLE",
        "UNKNOWN",
    }


def test_disease_has_clinical_burden_object(schema_view):
    slot_names = {slot.name for slot in schema_view.class_induced_slots("Disease")}
    assert "clinical_burden" in slot_names
    assert (
        schema_view.induced_slot("clinical_burden", "Disease").range == "ClinicalBurden"
    )
    assert (
        schema_view.induced_slot("burden_level", "ClinicalBurden").range
        == "ClinicalBurdenLevelEnum"
    )
    assert schema_view.induced_slot("burden_level", "ClinicalBurden").required is True


def test_disease_validates_with_clinical_burden(strict_validator):
    disease = {
        "name": "Test Jet Lag",
        "clinical_burden": {
            "burden_level": "LOW",
            "rationale": (
                "Typically transient and self-limited after circadian re-entrainment."
            ),
        },
    }

    report = strict_validator.validate(disease, target_class="Disease")
    errors = [result for result in report.results if result.severity.name == "ERROR"]
    assert not errors, (
        f"Unexpected validation errors: {[str(error) for error in errors]}"
    )


def test_clinical_burden_rejects_invalid_level(strict_validator):
    disease = {
        "name": "Test Jet Lag",
        "clinical_burden": {
            "burden_level": "TRIVIAL",
            "rationale": "Invalid burden level should fail strict validation.",
        },
    }

    report = strict_validator.validate(disease, target_class="Disease")
    errors = [result for result in report.results if result.severity.name == "ERROR"]
    assert errors
