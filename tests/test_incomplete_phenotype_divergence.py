"""`INCOMPLETE_PHENOTYPE` is a value, distinct from `SPECIES_MISMATCH` (#11743).

`ModelDivergenceTypeEnum` had no value for "the model shows some of the disease
phenotype and not the rest". The nearest value, `SPECIES_MISMATCH`, asserts
something stronger and different: that the divergence follows from the organism
being a different species. Sometimes it does; often it does not, and using it
then puts a cause in a typed field that is not in evidence, with the real issue
left in `description`, the one field no query can read.
"""

from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
GALNT2 = ROOT_DIR / "kb" / "disorders" / "GALNT2-Congenital_Disorder_of_Glycosylation.yaml"


@pytest.fixture(scope="module")
def divergence_values() -> dict:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    return schema["enums"]["ModelDivergenceTypeEnum"]["permissible_values"]


@pytest.fixture(scope="module")
def strict_validator() -> Validator:
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_incomplete_phenotype_is_a_permissible_value(divergence_values):
    assert "INCOMPLETE_PHENOTYPE" in divergence_values


def test_the_two_values_point_at_each_other(divergence_values):
    """Neither description is usable without the contrast; that is the whole value."""
    incomplete = divergence_values["INCOMPLETE_PHENOTYPE"]["description"]
    species = divergence_values["SPECIES_MISMATCH"]["description"]
    assert "SPECIES_MISMATCH" in incomplete or "species" in incomplete.lower()
    assert "INCOMPLETE_PHENOTYPE" in species


def test_species_mismatch_was_not_removed(divergence_values):
    """Retiring a value would invalidate every in-flight PR using it."""
    assert "SPECIES_MISMATCH" in divergence_values


def test_a_link_can_carry_both_values(strict_validator):
    """One model is often species-mismatched for one feature and incomplete for another."""
    disease = {
        "name": "Both Divergences",
        "pathophysiology": [{"name": "Neurodevelopmental Dysfunction"}],
        "animal_models": [
            {
                "name": "Knockout mouse",
                "species": "Mouse",
                "modeled_mechanisms": [
                    {
                        "target": "Neurodevelopmental Dysfunction",
                        "relationship": "PARTIALLY_RECAPITULATES",
                        "divergences": [
                            {
                                "divergence_type": "SPECIES_MISMATCH",
                                "materiality": "QUALIFYING",
                                "description": (
                                    "Language has no murine counterpart at all, so "
                                    "the model structurally cannot address it."
                                ),
                            },
                            {
                                "divergence_type": "INCOMPLETE_PHENOTYPE",
                                "materiality": "QUALIFYING",
                                "description": (
                                    "Epilepsy is unreported in the model, and a "
                                    "mouse can have seizures, so this is not a "
                                    "species-structural gap."
                                ),
                            },
                        ],
                    }
                ],
            }
        ],
    }
    report = strict_validator.validate(disease, target_class="Disease")
    assert [r for r in report.results if r.severity.name == "ERROR"] == []


def test_the_worked_example_carries_both_and_explains_each():
    """GALNT2-CDG is the motivating case; its own prose named the missing value."""
    data = yaml.safe_load(GALNT2.read_text(encoding="utf-8"))
    divergences = [
        div
        for model in data["animal_models"]
        for link in model.get("modeled_mechanisms") or []
        for div in link.get("divergences") or []
    ]
    kinds = {div["divergence_type"] for div in divergences}
    assert {"SPECIES_MISMATCH", "INCOMPLETE_PHENOTYPE"} <= kinds

    # The old text said "what is meant is an incomplete phenotype, for which
    # ModelDivergenceTypeEnum currently has no term". With the term, the
    # workaround note must be gone rather than left contradicting the value.
    for div in divergences:
        assert "currently has no term" not in div["description"]
