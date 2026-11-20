"""A progression phase can describe itself (#14450).

`ProgressionInfo` had no `description`, so the only place for "what happens in
this phase" was `notes` -- which CLAUDE.md reserves for the caveats a claim
needs, not for the claim. Nearly every neighbouring class an entry fills in
takes `description`, so writing one on a phase is the natural thing to do, and
before this the validator stopped the curator (PR #14448).

The renderer half is pinned here too: a slot whose content no page shows is not
a home for the text.
"""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
TEMPLATE_PATH = ROOT_DIR / "src" / "dismech" / "templates" / "disorder.html.j2"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def strict_validator() -> Validator:
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_progression_info_has_a_description_slot(schema_view):
    slot_names = {slot.name for slot in schema_view.class_induced_slots("ProgressionInfo")}
    assert "description" in slot_names


def test_progression_info_description_says_what_belongs_there(schema_view):
    """The slot's own text has to draw the line against `notes`, or it drifts back."""
    induced = schema_view.induced_slot("description", "ProgressionInfo")
    assert induced.description and "notes" in induced.description


def test_the_class_itself_is_described(schema_view):
    assert schema_view.get_class("ProgressionInfo").description


def test_a_phase_carrying_a_description_validates(strict_validator):
    report = strict_validator.validate(
        {
            "name": "Progression Description Probe",
            "progression": [
                {
                    "phase": "Antenatal",
                    "description": (
                        "Fetal thrombocytopenia can begin in the second trimester."
                    ),
                    "notes": "Detection depends on cordocentesis being indicated.",
                }
            ],
        },
        target_class="Disease",
    )
    assert list(report.results) == []


def test_a_phase_without_a_description_still_validates(strict_validator):
    """Additive only: no existing entry has to gain the slot."""
    report = strict_validator.validate(
        {"name": "No Description", "progression": [{"phase": "Antenatal"}]},
        target_class="Disease",
    )
    assert list(report.results) == []


def test_the_progression_card_renders_the_description():
    """Guards against the slot existing while no page shows it."""
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    card = template.split('<div class="card" id="progression">', 1)[1]
    card = card.split('id="stages"', 1)[0]
    assert "phase.description" in card
