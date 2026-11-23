"""How criteria sets combine, and which phenotype a criterion is.

Covers `Definition.criteria_set_logic`, `CriteriaItem.attaches_to`, the rules
in `dismech.definition_criteria`, and the `scripts/criteria_item_refs.py`
backfill.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from dismech.definition_criteria import (
    attaches_to_candidates,
    criteria_errors,
    iter_criteria_items,
)
from dismech.entity_refs import entity_ref_errors

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


@pytest.fixture(scope="module")
def backfill():
    spec = importlib.util.spec_from_file_location(
        "criteria_item_refs", ROOT_DIR / "scripts" / "criteria_item_refs.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _phenotype(name, curie, label, preferred=None):
    return {
        "name": name,
        "phenotype_term": {
            "preferred_term": preferred or label,
            "term": {"id": curie, "label": label},
        },
    }


def _entry(definition, phenotypes=()):
    return {
        "name": "Test Disorder",
        "phenotypes": list(phenotypes),
        "definitions": [definition],
    }


def _two_set_definition(logic="ANY_SUFFICIENT", items=None):
    items = items or [{"preferred_term": "Depressed mood"}]
    return {
        "name": "Test rule",
        "definition_type": "DIAGNOSTIC_CRITERIA",
        "criteria_set_logic": logic,
        "criteria_sets": [
            {"name": "A", "core_clinical_characteristics": items},
            {"name": "B", "minimum_required": 1},
        ],
    }


def _errors(report):
    return [r for r in report.results if r.severity.name == "ERROR"]


# --- schema -----------------------------------------------------------------


def test_criteria_set_logic_enum_values(schema_view):
    enum = schema_view.get_enum("CriteriaSetLogicEnum")
    assert set(enum.permissible_values) == {
        "ALL_REQUIRED",
        "ANY_SUFFICIENT",
        "GRADED",
        "WEIGHTED_SCORE",
    }
    assert schema_view.induced_slot("criteria_set_logic", "Definition").range == (
        "CriteriaSetLogicEnum"
    )


def test_criteria_item_has_attaches_to(schema_view):
    slot = schema_view.induced_slot("attaches_to", "CriteriaItem")
    assert slot.multivalued


def test_definition_with_both_slots_validates(strict_validator):
    entry = _entry(
        _two_set_definition(
            items=[
                {
                    "preferred_term": "Depressed mood",
                    "term": {"id": "HP:0000716", "label": "Depressed mood"},
                    "attaches_to": ["phenotypes#Depressed mood"],
                }
            ]
        ),
        [_phenotype("Depressed mood", "HP:0000716", "Depressed mood")],
    )
    assert not _errors(strict_validator.validate(entry, target_class="Disease"))


def test_unknown_logic_value_is_rejected(strict_validator):
    entry = _entry(_two_set_definition(logic="SOME_OF_THEM"))
    assert _errors(strict_validator.validate(entry, target_class="Disease"))


# --- rules --------------------------------------------------------------------


def test_logic_on_a_single_set_definition_is_an_error():
    definition = _two_set_definition()
    definition["criteria_sets"] = definition["criteria_sets"][:1]
    errors = criteria_errors(_entry(definition))
    assert len(errors) == 1 and "1 criteria set" in errors[0]


def test_logic_on_two_sets_is_fine():
    assert criteria_errors(_entry(_two_set_definition())) == []


def test_attached_term_must_be_the_phenotypes_binding():
    item = {
        "preferred_term": "Depressed mood",
        "term": {"id": "HP:0012154", "label": "Anhedonia"},
        "attaches_to": ["phenotypes#Depressed mood"],
    }
    entry = _entry(
        _two_set_definition(items=[item]),
        [_phenotype("Depressed mood", "HP:0000716", "Depressed mood")],
    )
    errors = criteria_errors(entry)
    assert len(errors) == 1 and "HP:0012154" in errors[0]


def test_attached_term_label_must_match_too():
    # The id agrees and the label is invented: the shape #10197 found inside
    # `qualifiers`, where nothing compared the label with the ontology's.
    item = {
        "preferred_term": "Depressed mood",
        "term": {"id": "HP:0000716", "label": "Low mood of any kind"},
        "attaches_to": ["phenotypes#Depressed mood"],
    }
    entry = _entry(
        _two_set_definition(items=[item]),
        [_phenotype("Depressed mood", "HP:0000716", "Depressed mood")],
    )
    assert len(criteria_errors(entry)) == 1


def test_criterion_spanning_two_phenotypes_may_carry_either_term():
    item = {
        "preferred_term": "Mood symptom",
        "term": {"id": "HP:0012154", "label": "Anhedonia"},
        "attaches_to": ["phenotypes#Depressed mood", "phenotypes#Anhedonia"],
    }
    entry = _entry(
        _two_set_definition(items=[item]),
        [
            _phenotype("Depressed mood", "HP:0000716", "Depressed mood"),
            _phenotype("Anhedonia", "HP:0012154", "Anhedonia"),
        ],
    )
    assert criteria_errors(entry) == []


def test_attached_criterion_without_its_own_term_is_fine():
    item = {
        "preferred_term": "Depressed mood",
        "attaches_to": ["phenotypes#Depressed mood"],
    }
    entry = _entry(
        _two_set_definition(items=[item]),
        [_phenotype("Depressed mood", "HP:0000716", "Depressed mood")],
    )
    assert criteria_errors(entry) == []


def test_dangling_criterion_ref_is_left_to_the_entity_ref_check():
    item = {
        "preferred_term": "Depressed mood",
        "term": {"id": "HP:0000716", "label": "Depressed mood"},
        "attaches_to": ["phenotypes#No Such Phenotype"],
    }
    entry = _entry(_two_set_definition(items=[item]))
    assert criteria_errors(entry) == []
    assert any("No Such Phenotype" in e for e in entity_ref_errors(entry))


def test_items_are_found_on_definitions_and_sets():
    definition = _two_set_definition()
    definition["exclusion_criteria"] = [{"preferred_term": "Mania"}]
    paths = [site.path for site in iter_criteria_items(_entry(definition))]
    assert paths == [
        "definitions[0].exclusion_criteria[0]",
        "definitions[0].criteria_sets[0].core_clinical_characteristics[0]",
    ]


# --- backfill worklist ----------------------------------------------------------


def _statuses(entry):
    return [(c.status, c.ref) for c in attaches_to_candidates(entry)]


def test_same_term_and_wording_is_exact():
    item = {
        "preferred_term": "optic neuritis",
        "term": {"id": "HP:0100653", "label": "Optic neuritis"},
    }
    entry = _entry(
        _two_set_definition(items=[item]),
        [_phenotype("Optic Neuritis", "HP:0100653", "Optic neuritis")],
    )
    assert _statuses(entry) == [("EXACT", "phenotypes#Optic Neuritis")]


def test_same_term_different_wording_is_not_written():
    # The NMOSD case: one CURIE, and a phenotype row narrower than the criterion.
    item = {
        "preferred_term": "Acute myelitis",
        "term": {"id": "HP:0012486", "label": "Myelitis"},
    }
    entry = _entry(
        _two_set_definition(items=[item]),
        [
            _phenotype(
                "Longitudinally Extensive Transverse Myelitis", "HP:0012486", "Myelitis"
            )
        ],
    )
    assert _statuses(entry) == [
        ("TERM_ONLY", "phenotypes#Longitudinally Extensive Transverse Myelitis")
    ]


def test_other_statuses():
    items = [
        {
            "preferred_term": "Seizures",
            "term": {"id": "HP:0001250", "label": "Seizure"},
        },
        {"preferred_term": "Fever", "term": {"id": "HP:0001945", "label": "Fever"}},
        {"preferred_term": "Social or occupational impairment"},
        {"preferred_term": "Linked", "attaches_to": ["phenotypes#Fever A"]},
    ]
    entry = _entry(
        _two_set_definition(items=items),
        [
            _phenotype("Fever A", "HP:0001945", "Fever"),
            _phenotype("Fever B", "HP:0001945", "Fever"),
        ],
    )
    assert [s for s, _ in _statuses(entry)] == ["NO_MATCH", "AMBIGUOUS", "NO_TERM"]


SAMPLE = """\
name: Test Disorder
phenotypes:
- name: Optic Neuritis
  phenotype_term:
    preferred_term: Optic neuritis
    term:
      id: HP:0100653
      label: Optic neuritis
definitions:
- name: Test rule
  definition_type: DIAGNOSTIC_CRITERIA
  criteria_set_logic: ANY_SUFFICIENT
  criteria_sets:
  - name: Seropositive
    core_clinical_characteristics:
    - preferred_term: Optic neuritis
      description: >-
        Folded text that the insertion must not disturb.
      term:
        id: HP:0100653
        label: Optic neuritis
    - preferred_term: Acute myelitis
  - name: Seronegative
    core_clinical_characteristics:
    - preferred_term: Optic neuritis
      term:
        id: HP:0100653
        label: Optic neuritis
notes: Trailing top-level key.
"""


def test_apply_writes_only_the_new_slot(backfill, tmp_path):
    path = tmp_path / "Test_Disorder.yaml"
    path.write_text(SAMPLE)
    before = yaml.safe_load(SAMPLE)
    ready = [c for c in attaches_to_candidates(before) if c.status == "EXACT"]
    assert len(ready) == 2

    assert backfill.apply_file(path, ready) == 2

    after = yaml.safe_load(path.read_text())
    sets = after["definitions"][0]["criteria_sets"]
    for cset in sets:
        item = cset["core_clinical_characteristics"][0]
        assert item.pop("attaches_to") == ["phenotypes#Optic Neuritis"]
    assert after == before
    assert criteria_errors(after) == []
    assert entity_ref_errors(yaml.safe_load(path.read_text())) == []


def test_apply_skips_when_the_text_does_not_match_the_worklist(
    backfill, tmp_path, capsys
):
    path = tmp_path / "Test_Disorder.yaml"
    path.write_text(SAMPLE)
    data = yaml.safe_load(SAMPLE)
    ready = [c for c in attaches_to_candidates(data) if c.status == "EXACT"][:1]
    # One candidate for a (preferred_term, id) pair the text holds twice: the
    # script cannot tell which occurrence is meant, so it writes neither.
    assert backfill.apply_file(path, ready) == 0
    assert path.read_text() == SAMPLE
    assert "expected 1" in capsys.readouterr().err
