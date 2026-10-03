"""Tests for Treatment.effect_modifiers (heterogeneity of treatment effect).

A treatment's effect can differ between patient subgroups (age, sex, baseline
severity, genotype ...). ``effect_modifiers`` records each such difference as a
``TreatmentEffectModifier``: the stratum, its comparator, the outcome, the
direction of the difference, and how it was established.
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
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _disease_with_modifier(modifier: dict) -> dict:
    return {
        "name": "Example",
        "treatments": [
            {
                "name": "Resistance training",
                "effect_modifiers": [modifier],
            }
        ],
    }


VALID_MODIFIER = {
    "effect_modifier_type": "SEX",
    "stratum": "women over 65",
    "comparator_stratum": "men over 65",
    "modified_outcome": "knee extensor maximal torque",
    "effect_in_stratum": "SMALLER_EFFECT",
    "modification_analysis": "CROSS_STRATUM_COMPARISON",
    "interaction_tested": True,
}


def _errors(validator, data):
    report = validator.validate(data, target_class="Disease")
    return [r for r in report.results if r.severity.name == "ERROR"]


def test_treatment_carries_effect_modifiers(schema_view):
    slots = {s.name for s in schema_view.class_induced_slots("Treatment")}
    assert "effect_modifiers" in slots
    assert schema_view.get_slot("effect_modifiers").range == "TreatmentEffectModifier"


def test_valid_effect_modifier_validates(validator):
    errors = _errors(validator, _disease_with_modifier(VALID_MODIFIER))
    assert not errors, [str(e) for e in errors]


@pytest.mark.parametrize(
    "missing",
    ["effect_modifier_type", "stratum", "modified_outcome", "effect_in_stratum"],
)
def test_core_fields_are_required(validator, missing):
    modifier = {k: v for k, v in VALID_MODIFIER.items() if k != missing}
    assert _errors(validator, _disease_with_modifier(modifier))


def test_direction_is_enum_bound(validator):
    modifier = dict(VALID_MODIFIER, effect_in_stratum="WORSE")
    assert _errors(validator, _disease_with_modifier(modifier))


def test_tested_null_is_a_recordable_direction(schema_view):
    """A subgroup comparison that found no difference must be expressible."""
    enum = schema_view.get_enum("EffectModificationDirectionEnum")
    assert "NO_DIFFERENCE" in enum.permissible_values
    assert "NO_EFFECT" in enum.permissible_values


def test_reproductive_status_is_separate_from_sex(schema_view):
    """Menopausal status varies within one sex, so it is not folded into SEX."""
    enum = schema_view.get_enum("EffectModifierTypeEnum")
    assert {"SEX", "REPRODUCTIVE_STATUS"} <= set(enum.permissible_values)
