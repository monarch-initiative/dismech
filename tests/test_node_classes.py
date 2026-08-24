"""Tests for the compact pathograph node-class tree parser."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.node_classes import (
    ClassNode,
    ParseError,
    iter_classes,
    iter_examples,
    parse_file,
    parse_text,
    render_text,
    to_dict,
    verify_examples,
)

ROOT = Path(__file__).parent.parent
TREE = ROOT / "docs" / "superpowers" / "pathograph_node_classes.txt"

SAMPLE = """\
# a comment, ignored
GENOMIC EFFECT  -- the lesion at the level of DNA/chromatin
  dosage
    JAG1 haploinsufficiency  [Alagille_syndrome]

CELLULAR EFFECT
  cell death
    Some Node  [Some_Disease]
      :note attached to the example
"""


def test_parses_classes_glosses_and_examples():
    roots = parse_text(SAMPLE)
    assert [r.name for r in roots] == ["GENOMIC EFFECT", "CELLULAR EFFECT"]
    assert roots[0].gloss == "the lesion at the level of DNA/chromatin"
    assert roots[1].gloss is None
    dosage = roots[0].children[0]
    assert dosage.name == "dosage"
    assert dosage.examples[0].node == "JAG1 haploinsufficiency"
    assert dosage.examples[0].disease == "Alagille_syndrome"


def test_class_id_is_upper_snake():
    assert parse_text(SAMPLE)[0].id == "GENOMIC_EFFECT"
    assert ClassNode(name="not a bundle, do not split", line=1).id == (
        "NOT_A_BUNDLE_DO_NOT_SPLIT"
    )


def test_attribute_attaches_to_the_example_not_the_class():
    roots = parse_text(SAMPLE)
    example = roots[1].children[0].examples[0]
    assert example.attributes == {"note": ["attached to the example"]}
    assert roots[1].children[0].attributes == {}


def test_repeated_attribute_keys_accumulate_in_order():
    roots = parse_text(
        "DEBUNDLE\n"
        "  A Node  [A_Disease]\n"
        "    :split ACTIVITY = first\n"
        "    :split TISSUE = second\n"
    )
    assert roots[0].examples[0].attributes["split"] == [
        "ACTIVITY = first",
        "TISSUE = second",
    ]


def test_class_may_carry_its_own_attributes():
    roots = parse_text("TOP\n  :source issue #1234\n  child\n")
    assert roots[0].attributes == {"source": ["issue #1234"]}
    assert [c.name for c in roots[0].children] == ["child"]


def test_example_name_may_contain_single_spaces_and_brackets_elsewhere():
    roots = parse_text("TOP\n  Bacterial Cross-Linking (Beta-Lactam Target)  [Meningitis]\n")
    example = roots[0].examples[0]
    assert example.node == "Bacterial Cross-Linking (Beta-Lactam Target)"
    assert example.disease == "Meningitis"


@pytest.mark.parametrize(
    "text, fragment",
    [
        ("TOP\n   bad indent\n", "not a multiple of 2"),
        ("TOP\n\tbad tab\n", "tab in indentation"),
        ("TOP\n      too deep\n", "indent jumps"),
        ("  Orphan Node  [D]\n", "example outside any class"),
        ("TOP\n  a\n  a\n", "duplicate sibling class name"),
        ("  :key value\n", "attribute line has no enclosing node"),
        (
            "TOP\n  first\n    A Node  [D]\n  second\n      :key value\n",
            "attribute line has no enclosing node",
        ),
    ],
)
def test_grammar_violations_raise_with_a_line_number(text, fragment):
    with pytest.raises(ParseError) as excinfo:
        parse_text(text, source="sample.txt")
    assert fragment in str(excinfo.value)
    assert excinfo.value.line >= 1


def test_an_example_opens_no_scope_for_a_following_class():
    # A class line at the example's own depth is a sibling of the example's
    # parent class, not a child of the example.
    roots = parse_text("TOP\n  first\n    A Node  [D]\n  second\n")
    assert [c.name for c in roots[0].children] == ["first", "second"]



def test_an_attribute_cannot_attach_into_a_closed_subtree():
    # Regression: the owner lookup used to keep entries from subtrees the
    # current line had already closed, so this attribute -- misindented under
    # `second`, which has no example -- silently became an attribute of
    # `A Node` two branches away instead of failing.
    text = "TOP\n  first\n    A Node  [D]\n  second\n      :key value\n"
    with pytest.raises(ParseError) as excinfo:
        parse_text(text, source="sample.txt")
    assert excinfo.value.line == 5

    # The same indentation IS valid while that subtree is still open.
    roots = parse_text("TOP\n  first\n    A Node  [D]\n      :key value\n")
    assert roots[0].children[0].examples[0].attributes == {"key": ["value"]}


def test_round_trip_is_stable():
    roots = parse_text(SAMPLE)
    once = render_text(roots)
    assert to_dict(parse_text(once)) == to_dict(roots)
    assert render_text(parse_text(once)) == once


def test_verify_examples_reports_missing_entry_and_missing_node(tmp_path):
    kb = tmp_path / "disorders"
    kb.mkdir()
    (kb / "Real_Disease.yaml").write_text(
        "name: Real Disease\npathophysiology:\n- name: Real Node\n", encoding="utf-8"
    )
    roots = parse_text(
        "TOP\n"
        "  Real Node  [Real_Disease]\n"
        "  Ghost Node  [Real_Disease]\n"
        "  Real Node  [No_Such_Disease]\n"
    )
    problems = verify_examples(roots, [kb])
    assert len(problems) == 2
    assert any("no such entry 'No_Such_Disease'" in p for p in problems)
    assert any("has no pathophysiology node named 'Ghost Node'" in p for p in problems)


# --- the committed tree itself -------------------------------------------------


def test_committed_tree_parses():
    roots = parse_file(TREE)
    assert roots, "node-class tree parsed to nothing"
    names = {r.name for r in roots}
    assert "GENOMIC EFFECT" in names
    assert "MOLECULAR ACTIVITY EFFECT" in names


def test_committed_tree_class_ids_are_unique_and_slug_safe():
    ids = [node.id for _, node in iter_classes(parse_file(TREE))]
    assert len(ids) == len(set(ids)), "duplicate class ids in the tree"
    assert all(id_ and id_.replace("_", "").isalnum() for id_ in ids)


def test_committed_tree_examples_resolve_in_kb():
    """Every cited leaf must be a real pathophysiology node.

    A class tree whose leaves have drifted from the KB is worse than no tree,
    because it still looks grounded.
    """
    roots = parse_file(TREE)
    kb_dirs = [ROOT / "kb" / "disorders", ROOT / "kb" / "modules"]
    problems = verify_examples(roots, kb_dirs)
    assert not problems, "unresolved examples:\n" + "\n".join(problems)


def test_committed_tree_every_class_has_a_gloss_or_examples():
    for trail, node in iter_classes(parse_file(TREE)):
        assert node.gloss or node.examples or node.children, (
            f"class {' > '.join(trail)} is empty"
        )


def test_committed_tree_has_examples_for_every_top_level_class():
    roots = parse_file(TREE)
    for root in roots:
        cited = [ex for trail, ex in iter_examples([root])]
        assert cited, f"top-level class {root.name} cites no examples"
