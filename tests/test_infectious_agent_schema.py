"""Tests for the agent-stratum binding on `InfectiousAgent.has_subtypes`.

`InfectiousAgent.has_subtypes` originally reused the disease-level `Subtype`
class, whose `subtype_term` binds `DiseaseOrSubtypeTerm` - an enum rooted at
`MONDO:0000001` and the NCIT disease classes. A serovar, serotype, subspecies
or biotype nested under an infectious agent is an *organism*, not a disease, so
that binding admitted no honest term and every such stratum in the KB was
forced to remain name-only free text (`Cholera` O1/O139, `Shigellosis`,
`Paratyphoid_Fever`).

These tests pin the narrower classes that fix it: `AgentSubtype` overrides
`subtype_term` to `AgentSubtypeDescriptor`, which inherits the NCBITaxon
`OrganismTerm` binding from `OrganismDescriptor`. The disease-level binding is
deliberately left untouched, and the last test guards that.
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


def _binding_ranges(schema_view: SchemaView, slot_name: str, class_name: str):
    slot = schema_view.induced_slot(slot_name, class_name)
    return {b.range for b in (slot.bindings or [])}


def test_infectious_agent_subtypes_use_agent_subtype(schema_view):
    """`InfectiousAgent.has_subtypes` ranges over `AgentSubtype`, not `Subtype`."""
    slot = schema_view.induced_slot("has_subtypes", "InfectiousAgent")
    assert slot.range == "AgentSubtype"


def test_agent_subtype_term_binds_ncbitaxon(schema_view):
    """An agent stratum grounds to NCBITaxon via `OrganismTerm`."""
    subtype_term = schema_view.induced_slot("subtype_term", "AgentSubtype")
    assert subtype_term.range == "AgentSubtypeDescriptor"

    ranges = _binding_ranges(schema_view, "term", "AgentSubtypeDescriptor")
    assert ranges == {"OrganismTerm"}, (
        f"AgentSubtypeDescriptor.term should bind OrganismTerm only, got {ranges}"
    )


def test_agent_subtype_does_not_admit_disease_terms(schema_view):
    """The disease enum is not reachable from an agent stratum.

    This is the defect the split exists to close: before it, the only legal
    grounding for a serovar was a MONDO/NCIT *disease* class.
    """
    ranges = _binding_ranges(schema_view, "term", "AgentSubtypeDescriptor")
    assert "DiseaseOrSubtypeTerm" not in ranges


def test_agent_subtype_inherits_subtype_slots(schema_view):
    """`AgentSubtype` keeps the `Subtype` shape so existing entries stay valid.

    `Cholera`, `Shigellosis` and `Paratyphoid_Fever` already carry agent strata
    using `name`, `description` and `evidence`; narrowing the class must not
    invalidate them.
    """
    slots = set(schema_view.class_slots("AgentSubtype"))
    assert {"name", "description", "evidence", "subtype_term"} <= slots


def test_bound_agent_stratum_validates(validator):
    """A serovar stratum carrying an NCBITaxon term passes schema validation."""
    data = {
        "name": "Test Disease",
        "infectious_agent": [
            {
                "name": "Salmonella enterica serovar Paratyphi",
                "has_subtypes": [
                    {
                        "name": "Paratyphi A",
                        "description": (
                            "Predominant paratyphoid serovar in South and "
                            "Southeast Asia."
                        ),
                        "subtype_term": {
                            "preferred_term": "Salmonella enterica serovar Paratyphi A",
                            "term": {
                                "id": "NCBITaxon:54388",
                                "label": (
                                    "Salmonella enterica subsp. enterica "
                                    "serovar Paratyphi A"
                                ),
                            },
                        },
                    }
                ],
            }
        ],
    }
    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_unbound_agent_stratum_still_validates(validator):
    """`subtype_term` stays optional.

    Pathotypes (ETEC, MRSA) and serogroups have no NCBITaxon node at their own
    rank. Omitting the term is the correct curation, so it must not be an error.
    """
    data = {
        "name": "Test Disease",
        "infectious_agent": [
            {
                "name": "Vibrio cholerae",
                "has_subtypes": [{"name": "O1"}, {"name": "O139"}],
            }
        ],
    }
    report = validator.validate(data, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_disease_level_subtype_binding_unchanged(schema_view):
    """Regression guard: disease subtypes still bind MONDO/NCIT, not NCBITaxon.

    The split must not leak the organism enum into the disease axis.
    """
    subtype_term = schema_view.induced_slot("subtype_term", "Subtype")
    assert subtype_term.range == "SubtypeDescriptor"

    ranges = _binding_ranges(schema_view, "term", "SubtypeDescriptor")
    assert ranges == {"DiseaseOrSubtypeTerm"}
