"""Tests for the node-class logical-definition language."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from dismech.node_class_definitions import (
    UNRESOLVED,
    WRONG_LABEL,
    DefinitionError,
    check_labels,
    curie_labels,
    evaluate,
    evaluate_tree,
    modifier_values,
    no_closure,
    obo_ancestors,
    parse_definition,
    triage_label_problems,
)

SCHEMA = Path(__file__).parent.parent / "src" / "dismech" / "schema" / "dismech.yaml"

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
    assert [(p.curie, p.kind) for p in problems] == [("CL:0000232", WRONG_LABEL)]
    assert problems[0].render("the ontology") == (
        "CL:0000232: label 'erythrocyte' but the ontology says 'red blood cell'"
    )
    missing = check_labels({"GO:9999999": None}, lambda _: None)
    assert [(p.curie, p.kind) for p in missing] == [("GO:9999999", UNRESOLVED)]
    assert missing[0].render("the term cache") == "GO:9999999: unresolved (not in the term cache)"


def test_unresolved_curie_fails_only_against_an_authoritative_lookup():
    """A fabricated CURIE must not pass the online check (review of #11132)."""
    wrong, missing = check_labels(
        {"CL:0000232": "erythrocyte", "GO:9999999": "made up"},
        {"CL:0000232": "red blood cell"}.get,
    )
    assert (wrong.kind, missing.kind) == (WRONG_LABEL, UNRESOLVED)
    offline_fail, offline_unchecked = triage_label_problems([wrong, missing], authoritative=False)
    assert offline_fail == [wrong] and offline_unchecked == [missing]
    online_fail, online_unchecked = triage_label_problems([wrong, missing], authoritative=True)
    assert online_fail == [wrong, missing] and online_unchecked == []


def test_modifier_values_are_read_from_the_schema():
    """The definition language's modifier vocabulary is the schema's, not a copy."""
    with SCHEMA.open(encoding="utf-8") as fh:
        schema = yaml.safe_load(fh)
    expected = set(schema["enums"]["ModifierEnum"]["permissible_values"])
    assert modifier_values() == expected
    assert {"GAIN_OF_FUNCTION", "LOSS_OF_FUNCTION"} <= modifier_values()
    d = parse_definition("biological_processes some GO:0007165 modifier GAIN_OF_FUNCTION")
    assert d.disjuncts[0][0].modifiers == ("GAIN_OF_FUNCTION",)


def test_obo_ancestors_closes_over_is_a(tmp_path):
    obo = tmp_path / "mini.obo"
    obo.write_text(
        "format-version: 1.2\n\n"
        "[Term]\nid: GO:3\nname: leaf\nis_a: GO:2 ! middle\n\n"
        "[Term]\nid: GO:2\nname: middle\nis_a: GO:1 ! root\n\n"
        "[Term]\nid: GO:1\nname: root\n\n"
        "[Typedef]\nid: part_of\nis_a: GO:9\n",
        encoding="utf-8",
    )
    ancestors = obo_ancestors(obo)
    assert ancestors("GO:3") == {"GO:2", "GO:1"}
    assert ancestors("GO:1") == set()
    assert ancestors("CL:0000000") == set()
    assert ancestors("part_of") == set(), "a [Typedef] stanza is not a term"


def test_a_tier_definition_is_scored_over_the_examples_beneath_it(tmp_path):
    """A tier's examples sit on its leaves, so its own-example recall is 0/0."""
    from dismech.node_classes import parse_text

    kb = tmp_path / "disorders"
    kb.mkdir()
    (kb / "D.yaml").write_text(
        "pathophysiology:\n"
        "- name: Dying\n  biological_processes:\n  - term: {id: GO:0008219}\n"
        "- name: Bare\n",
        encoding="utf-8",
    )
    roots = parse_text(
        "CELLULAR EFFECT\n"
        "  = biological_processes some GO:0008219\n"
        "  cell death\n"
        "    [D] Dying\n"
        "    [D] Bare\n"
    )
    (report,) = evaluate_tree(roots, [kb], no_closure)
    assert (report.examples, report.examples_matched) == (0, 0)
    assert (report.subtree_examples, report.subtree_matched) == (2, 1)
    assert report.subtree_recall == 0.5


def test_evaluate_refuses_to_download_the_go_build(monkeypatch, capsys):
    import dismech.oak_db
    from dismech import node_classes

    monkeypatch.setattr(dismech.oak_db, "local_build_present", lambda spec: False)
    tree = Path(__file__).parent.parent / "kb" / "node_classes" / "pathograph_node_classes.txt"
    assert node_classes.main([str(tree), "--evaluate"]) == 2
    assert "just fetch-ontology-dbs go" in capsys.readouterr().err
