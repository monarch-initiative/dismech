"""Tests for MRO (MHC Restriction Ontology) integration in the dismech schema."""

from pathlib import Path

import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from dismech.term_tooltips import ONTOLOGY_NAMES, TERM_ROLES, term_tooltip

SCHEMA_PATH = (
    Path(__file__).resolve().parent.parent
    / "src"
    / "dismech"
    / "schema"
    / "dismech.yaml"
)
OAK_CONFIG_PATH = Path(__file__).resolve().parent.parent / "conf" / "oak_config.yaml"


def _validate_disease_doc(data: dict) -> list[str]:
    validator = Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )
    report = validator.validate(data, target_class="Disease")
    return [r.message for r in report.results if r.severity.name == "ERROR"]


def test_mro_configured_in_oak_and_schema() -> None:
    oak_cfg = yaml.safe_load(OAK_CONFIG_PATH.read_text(encoding="utf-8"))
    assert oak_cfg["ontology_adapters"].get("MRO") == "ols:mro"

    sv = SchemaView(str(SCHEMA_PATH))
    assert "MRO" in sv.schema.prefixes
    assert (
        sv.schema.prefixes["MRO"].prefix_reference
        == "http://purl.obolibrary.org/obo/MRO_"
    )

    mhc_enum = sv.get_enum("MHCTerm")
    assert mhc_enum is not None
    assert set(mhc_enum.reachable_from.source_nodes) == {
        "GO:0042611",
        "MRO:0000775",
        "MRO:0000776",
        "MRO:0000007",
        "MRO:0000005",
    }

    mhc_desc = sv.get_class("MHCDescriptor")
    assert mhc_desc is not None
    assert mhc_desc.is_a == "Descriptor"

    genetic_slots = {slot.name for slot in sv.class_induced_slots("Genetic")}
    assert "mhc_term" in genetic_slots

    em_slots = {slot.name for slot in sv.class_induced_slots("TreatmentEffectModifier")}
    assert "mhc_term" in em_slots


def test_disease_accepts_mro_bindings_across_genetic_treatment_and_pathophysiology() -> (
    None
):
    doc = {
        "name": "Hepatitis B",
        "pathophysiology": [
            {
                "name": "HBsAg Peptide Presentation by MHC Class II",
                "protein_complexes": [
                    {
                        "preferred_term": "HLA-DRB1*03:01 protein complex",
                        "term": {
                            "id": "MRO:0001284",
                            "label": "HLA-DRB1*03:01 protein complex",
                        },
                    }
                ],
            }
        ],
        "genetic": [
            {
                "name": "HLA-DQ2",
                "gene_term": {
                    "preferred_term": "HLA-DQA1",
                    "term": {
                        "id": "hgnc:4942",
                        "label": "HLA-DQA1",
                    },
                },
                "mhc_term": {
                    "preferred_term": "HLA-DQ2 serotype",
                    "term": {
                        "id": "MRO:0000283",
                        "label": "HLA-DQ2 serotype",
                    },
                },
                "relationship_type": "RISK_FACTOR",
            }
        ],
        "treatments": [
            {
                "name": "Hepatitis B Vaccination",
                "effect_modifiers": [
                    {
                        "effect_modifier_type": "GENOTYPE",
                        "stratum": "HLA-DRB1*03:01 carriers",
                        "mhc_term": {
                            "preferred_term": "HLA-DRB1*03:01 protein complex",
                            "term": {
                                "id": "MRO:0001284",
                                "label": "HLA-DRB1*03:01 protein complex",
                            },
                        },
                        "comparator_stratum": "non-carriers",
                        "modified_outcome": "anti-HBs seroprotection rate",
                        "effect_in_stratum": "SMALLER_EFFECT",
                    }
                ],
            }
        ],
    }

    assert _validate_disease_doc(doc) == []


def test_mro_term_tooltips() -> None:
    assert "MRO" in ONTOLOGY_NAMES
    assert "gene.mhc_term" in TERM_ROLES
    assert "effect_modifier.mhc_term" in TERM_ROLES

    descriptor = {
        "preferred_term": "HLA-DQ2 serotype",
        "term": {"id": "MRO:0000283", "label": "HLA-DQ2 serotype"},
    }
    tip = term_tooltip(descriptor, "gene.mhc_term")
    assert "MHC Restriction Ontology (MRO)" in tip
    assert (
        "MRO:0000283 is a major histocompatibility complex restriction "
        "from the MHC Restriction Ontology."
    ) in tip
