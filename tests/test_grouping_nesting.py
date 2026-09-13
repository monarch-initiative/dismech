"""Grouping-of-grouping nesting: expansion, evaluation, and the nesting report.

The grouping index looked flat because nesting is declared only by
``member_type: GROUPING`` members and most groupings declare none; worse, a
disease held through a nested grouping was invisible to the parent's
evaluator and rendered as ``not listed`` on the parent's page. These tests pin
the nesting-aware behaviour.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from dismech.groupings import (
    DiseaseFacts,
    Satisfaction,
    compute_nesting_report,
    declared_nestings,
    evaluate_grouping,
    iter_disease_targets,
    nested_disease_members,
)
from dismech.render import render_all_groupings


def _grouping(name: str, members: list[tuple[str, str]], criteria=None) -> dict:
    return {
        "name": name,
        "members": [{"member": m, "member_type": t} for m, t in members],
        "membership_criteria": criteria or [],
    }


PARENT = _grouping(
    "Parent",
    [("A", "DISEASE"), ("Child", "GROUPING"), ("Loop", "GROUPING")],
    criteria=[
        {
            "description": "Every member conforms to the test module.",
            "criteria_semantics": "NECESSARY",
            "logic": {"criterion_predicate": "CONFORMS_TO_MODULE", "module": "m"},
        }
    ],
)
CHILD = _grouping("Child", [("B", "DISEASE"), ("C", "SUBTYPE"), ("A", "DISEASE")])
LOOP = _grouping("Loop", [("D", "DISEASE"), ("Parent", "GROUPING")])
CONTAINED = _grouping("Contained", [("A", "DISEASE"), ("B", "DISEASE")])
TWIN = _grouping("Twin", [("A", "DISEASE"), ("B", "DISEASE")])
PARTIAL = _grouping("Partial", [("A", "DISEASE"), ("Z", "DISEASE")])
ALONE = _grouping("Alone", [("Q", "DISEASE")])
GROUPINGS = {
    g["name"]: g for g in (PARENT, CHILD, LOOP, CONTAINED, TWIN, PARTIAL, ALONE)
}


def test_iter_disease_targets_expands_nested_groupings_with_via() -> None:
    targets = list(iter_disease_targets(PARENT, GROUPINGS))
    assert ("A", "DISEASE", None) in targets  # direct membership wins
    assert ("B", "DISEASE", "Child") in targets
    assert ("C", "SUBTYPE", "Child") in targets
    assert ("D", "DISEASE", "Loop") in targets  # reached despite the cycle
    assert len({t[0] for t in targets}) == len(targets)  # each disease once
    assert nested_disease_members(PARENT, GROUPINGS) == {
        "B": "Child",
        "C": "Child",
        "D": "Loop",
    }


def test_evaluate_grouping_covers_nested_members() -> None:
    index = {
        name: DiseaseFacts(name=name, module_stems={"m"} if name != "D" else set())
        for name in "ABCD"
    }
    evaluations = evaluate_grouping(PARENT, index, GROUPINGS)
    by_member = {ev.member: ev for ev in evaluations}
    assert by_member["A"].via is None
    assert by_member["B"].via == "Child"
    assert by_member["B"].result is Satisfaction.SATISFIED
    # "Every member of G satisfies C" binds nested members too.
    assert by_member["D"].via == "Loop"
    assert by_member["D"].result is Satisfaction.NOT_SATISFIED


def test_nesting_report_separates_declared_from_undeclared_containment() -> None:
    report = compute_nesting_report(GROUPINGS, threshold=0.5)

    assert report.children_by_parent == {
        "Loop": ("Parent",),
        "Parent": ("Child", "Loop"),
    }
    assert report.parents_by_child == {
        "Child": ("Parent",),
        "Loop": ("Parent",),
        "Parent": ("Loop",),
    }
    assert report.standalone == ("Alone", "Contained", "Partial", "Twin")

    contained = {(c.child, c.parent): c for c in report.containments}
    # Contained ⊆ Parent (expanded: A, B, C, D) and ⊆ Child (A, B, C).
    assert ("Contained", "Parent") in contained
    assert ("Contained", "Child") in contained
    # A declared edge is never re-reported as a containment.
    assert ("Child", "Parent") not in contained
    # Identical member sets are reported once, in name order, and flagged.
    twins = [c for c in report.containments if c.equal_sets]
    assert [(c.child, c.parent) for c in twins] == [("Twin", "Contained")]
    # A grouping cannot be contained by a smaller one.
    assert all(c.parent_count >= c.child_count for c in report.containments)

    near = {(c.child, c.parent): c for c in report.near_containments}
    assert ("Partial", "Parent") in near
    assert near[("Partial", "Parent")].missing_members == ("Z",)
    assert near[("Partial", "Parent")].fraction == 0.5


def test_declared_nestings_reports_dangling_refs() -> None:
    dangling = _grouping("Dangling", [("Nowhere", "GROUPING")])
    children, unresolved = declared_nestings({"Dangling": dangling})
    assert children == {}
    assert unresolved == (("Dangling", "Nowhere"),)


def _write(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_rendered_pages_expose_nesting(tmp_path: Path) -> None:
    input_dir = tmp_path / "kb" / "groupings"
    disorders_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "groupings"
    disorders_dir.mkdir(parents=True)

    _write(
        input_dir / "Outer.yaml",
        {
            "name": "Outer Grouping",
            "description": "Holds Inner.",
            "members": [
                {"member": "Direct Disease", "member_type": "DISEASE"},
                {
                    "member": "Inner Grouping",
                    "member_type": "GROUPING",
                    "differentiating_mechanisms": [{"description": "Nested."}],
                },
            ],
        },
    )
    _write(
        input_dir / "Inner.yaml",
        {
            "name": "Inner Grouping",
            "description": "Nested in Outer.",
            "members": [{"member": "Nested Disease", "member_type": "DISEASE"}],
        },
    )
    _write(
        input_dir / "Shadow.yaml",
        {
            "name": "Shadow Grouping",
            "description": "Same diseases as Inner, undeclared.",
            "members": [{"member": "Nested Disease", "member_type": "DISEASE"}],
        },
    )
    _write(
        input_dir / "Lone.yaml",
        {
            "name": "Lone Grouping",
            "description": "Nests in nothing.",
            "members": [{"member": "Other Disease", "member_type": "DISEASE"}],
        },
    )

    render_all_groupings(input_dir, output_dir, disorders_dir=disorders_dir)

    index = (output_dir / "index.html").read_text()
    assert "1 nested tree" in index
    assert "1 nested relation" in index
    assert "2 standalone" in index
    # The nested tree is drawn; standalone groupings are folded, not tree rows.
    tree_start = index.index('class="tree-root-list"')
    tree_end = index.index('class="standalone"')
    assert "Outer Grouping" in index[tree_start:tree_end]
    assert "Inner Grouping" in index[tree_start:tree_end]
    assert "Lone Grouping" not in index[tree_start:tree_end]
    assert "Standalone groupings (2)" in index
    # Undeclared containment advisory: Shadow = Inner (equal sets, once).
    assert "Undeclared containment" in index
    advisory = index[index.index("Undeclared containment") :]
    # Shadow = Inner (identical sets, reported once) and Shadow ⊆ Outer, whose
    # expanded members include the one Inner holds. Inner ⊆ Outer is declared
    # and therefore not an advisory.
    assert "Shadow Grouping" in advisory and "Inner Grouping" in advisory
    assert advisory.count("containment-rel") == 2
    assert advisory.count(">=<") == 1
    assert "Nested in Outer Grouping" in index  # card stat on Inner

    outer = (output_dir / "Outer_Grouping.html").read_text()
    assert "Where this grouping sits" in outer
    assert "Nested groupings" in outer
    assert 'href="Inner_Grouping.html"' in outer
    assert 'nested via <a href="Inner_Grouping.html">Inner Grouping</a>' in outer
    assert "1 via nested grouping" in outer

    inner = (output_dir / "Inner_Grouping.html").read_text()
    assert "Nested in" in inner
    assert 'href="Outer_Grouping.html"' in inner

    lone = (output_dir / "Lone_Grouping.html").read_text()
    assert "Where this grouping sits" not in lone
