"""Tests for the node-class logical-definition language."""

from __future__ import annotations

import pytest

from dismech.node_class_definitions import (
    DefinitionError,
    check_labels,
    curie_labels,
    evaluate,
    no_closure,
    parse_definition,
)

DEATH = "biological_processes some GO:0008219 'cell death'"


def bp(term, modifier=None):
    item = {"term": {"id": term}}
    if modifier:
        item["modifier"] = modifier
    return item


def test_parses_a_single_atom_with_label():
    d = parse_definition(DEATH)
    assert len(d.disjuncts) == 1 and len(d.disjuncts[0]) == 1
    atom = d.disjuncts[0][0]
    assert atom.slot == "biological_processes"
    assert atom.term == "GO:0008219"
    assert atom.label == "cell death"
    assert not atom.negated and atom.modifiers == ()
    assert d.render() == DEATH


def test_and_binds_tighter_than_or_and_modifiers_pin_a_value_set():
    d = parse_definition(
        "molecular_functions some GO:0005215 'transporter activity' "
        "and not molecular_functions some GO:0015267 'channel activity' "
        "or chemical_entities some CHEBI modifier INCREASED|DECREASED"
    )
    assert [len(c) for c in d.disjuncts] == [2, 1]
    assert d.disjuncts[0][1].negated
    prefix_atom = d.disjuncts[1][0]
    assert prefix_atom.is_prefix and prefix_atom.modifiers == ("INCREASED", "DECREASED")
    assert d.render() == d.raw


@pytest.mark.parametrize(
    "text, fragment",
    [
        ("", "empty"),
        ("nowhere some GO:1", "unknown slot"),
        ("cell_types GO:0000540", "expected 'some'"),
        ("cell_types some", "unexpected end"),
        ("cell_types some not-a-term!", "bad term"),
        ("cell_types some CL 'a label'", "takes no label"),
        ("cell_types some CL modifier HUGE", "unknown modifier"),
        ("cell_types some CL xor cell_types some CL", "expected 'and' or 'or'"),
    ],
)
def test_grammar_errors_name_the_problem(text, fragment):
    with pytest.raises(DefinitionError) as excinfo:
        parse_definition(text)
    assert fragment in str(excinfo.value)


def test_evaluate_exact_match_and_closure():
    d = parse_definition(DEATH)
    apoptosis = {"biological_processes": [bp("GO:0006915")]}
    assert not evaluate(d, apoptosis, no_closure)
    assert evaluate(d, apoptosis, lambda t: {"GO:0008219"} if t == "GO:0006915" else set())
    assert evaluate(d, {"biological_processes": [bp("GO:0008219")]}, no_closure)
    assert not evaluate(d, {"cell_types": [{"term": {"id": "CL:1"}}]}, no_closure)


def test_modifier_restricts_the_same_descriptor():
    d = parse_definition("biological_processes some GO:0007165 modifier INCREASED")
    assert evaluate(d, {"biological_processes": [bp("GO:0007165", "INCREASED")]}, no_closure)
    assert not evaluate(d, {"biological_processes": [bp("GO:0007165", "DECREASED")]}, no_closure)
    # a matching term without the modifier plus an unrelated increased term is not enough
    node = {"biological_processes": [bp("GO:0007165"), bp("GO:0000001", "INCREASED")]}
    assert not evaluate(d, node, no_closure)


def test_prefix_atoms_and_negation():
    d = parse_definition("locations some UBERON and not cell_types some CL")
    assert evaluate(d, {"locations": [{"term": {"id": "UBERON:0002107"}}]}, no_closure)
    both = {
        "locations": [{"term": {"id": "UBERON:0002107"}}],
        "cell_types": [{"term": {"id": "CL:0000182"}}],
    }
    assert not evaluate(d, both, no_closure)
    assert not evaluate(d, {"locations": [{"term": {"id": "GO:0005739"}}]}, no_closure)


def test_disjunction_holds_when_any_branch_holds():
    d = parse_definition("cell_types some CL or locations some UBERON")
    assert evaluate(d, {"locations": [{"term": {"id": "UBERON:1"}}]}, no_closure)
    assert not evaluate(d, {"genes": [{"term": {"id": "hgnc:1"}}]}, no_closure)


def test_label_check_reports_wrong_and_unresolved_labels():
    claimed = curie_labels([parse_definition(DEATH), parse_definition("cell_types some CL:0000232 'erythrocyte'")])
    assert claimed == {"GO:0008219": "cell death", "CL:0000232": "erythrocyte"}
    lookup = {"GO:0008219": "cell death", "CL:0000232": "red blood cell"}.get
    problems = check_labels(claimed, lookup)
    assert problems == ["CL:0000232: label 'erythrocyte' but ontology says 'red blood cell'"]
    assert check_labels({"GO:0000001": None}, lambda _: None) == ["GO:0000001: unresolved (not in cache)"]
