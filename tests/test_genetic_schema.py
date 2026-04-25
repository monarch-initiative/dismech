"""Tests for the structured genetics slots/enums added for issue #126.

These tests pin down the data-model improvements that constrain the
previously free-text `association` slot in the `Genetic` class to a
controlled vocabulary, and add a `variant_origin` slot bound to GENO
allele origin terms.
"""

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
def validator() -> Validator:
    # Use closed=True so unknown enum values are flagged as errors. This is
    # required to demonstrate that the new enum constraints actually bite.
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_gene_disease_relationship_enum_defined(schema_view):
    """The new GeneDiseaseRelationshipEnum exists with the expected values."""
    enum = schema_view.get_enum("GeneDiseaseRelationshipEnum")
    assert enum is not None
    expected = {
        "CAUSATIVE",
        "RISK_FACTOR",
        "PROTECTIVE",
        "MODIFIER",
        "SUSCEPTIBILITY",
        "SOMATIC_DRIVER",
        "COOPERATING",
        "BIOMARKER",
        "DISPUTED",
        "UNKNOWN",
    }
    actual = set(enum.permissible_values.keys())
    missing = expected - actual
    assert not missing, f"Missing enum values: {missing}"


def test_variant_origin_enum_bound_to_geno(schema_view):
    """VariantOriginEnum exists and binds GERMLINE/SOMATIC to GENO terms."""
    enum = schema_view.get_enum("VariantOriginEnum")
    assert enum is not None
    pvs = enum.permissible_values
    assert "GERMLINE" in pvs and "SOMATIC" in pvs
    # GENO bindings verified via OAK against sqlite:obo:geno
    assert pvs["GERMLINE"].meaning == "GENO:0000888"
    assert pvs["SOMATIC"].meaning == "GENO:0000882"
    assert pvs["DE_NOVO"].meaning == "GENO:0000880"
    assert pvs["UNKNOWN"].meaning == "GENO:0000881"


def test_genetic_class_has_new_slots(schema_view):
    """The Genetic class includes the new structured slots."""
    cls = schema_view.get_class("Genetic")
    assert cls is not None
    induced = schema_view.class_induced_slots("Genetic")
    slot_names = {s.name for s in induced}
    assert "relationship_type" in slot_names
    assert "variant_origin" in slot_names
    # Free-text association slot is preserved for backward compatibility
    assert "association" in slot_names


def test_genetic_record_validates_with_structured_fields(validator):
    """A minimal Disease using the new structured fields validates."""
    disease = {
        "name": "Test Disease For Issue 126",
        "genetic": [
            {
                "name": "BRCA1",
                "association": "Germline pathogenic loss-of-function variants",
                "relationship_type": "CAUSATIVE",
                "variant_origin": "GERMLINE",
            },
            {
                "name": "TP53",
                "relationship_type": "SOMATIC_DRIVER",
                "variant_origin": "SOMATIC",
            },
            {
                "name": "HLA-B51",
                "relationship_type": "RISK_FACTOR",
            },
        ],
    }
    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_invalid_relationship_type_rejected(validator):
    """An out-of-vocabulary relationship_type fails validation."""
    disease = {
        "name": "Test Disease Invalid",
        "genetic": [
            {
                "name": "FOO",
                "relationship_type": "TOTALLY_MADE_UP_VALUE",
            }
        ],
    }
    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for invalid relationship_type"
