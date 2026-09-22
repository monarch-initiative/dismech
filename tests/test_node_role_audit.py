"""Tests for auditing the free-text pathophysiology ``role`` slot against edges."""

from __future__ import annotations

from dismech.node_role_audit import (
    CONTRADICTED,
    CURATED,
    DERIVED,
    FACETS,
    INTERIOR,
    ISOLATED,
    ROLE_FACETS,
    SINK,
    SOURCE,
    UNMAPPED,
    audit,
    casing_variants,
    compute_positions,
    crosstab,
    facet_table,
    judge,
    normalize_role,
    summarize,
)


def test_normalize_role_collapses_case_and_spacing():
    assert normalize_role("TRIGGER") == "trigger"
    assert normalize_role(" Trigger ") == "trigger"
    assert normalize_role("central effector") == "central_effector"


def test_positions_follow_in_and_out_degree_within_the_file():
    nodes = [
        {"name": "A", "downstream": [{"target": "B"}]},
        {"name": "B", "downstream": [{"target": "C"}, {"target": "Pain"}]},
        {"name": "C"},
        {"name": "D", "downstream": [{"target": "D"}, {"target": "Nowhere"}]},
    ]
    pos = compute_positions(nodes, phenotype_names={"Pain"})
    assert pos["A"] == (SOURCE, 0, 1, 0)
    assert pos["B"] == (INTERIOR, 1, 1, 1)
    assert pos["C"] == (SINK, 1, 0, 0)
    # a self-loop and a dangling target are not graph edges
    assert pos["D"] == (ISOLATED, 0, 0, 0)


def test_a_phenotype_exit_makes_a_source_not_an_isolate():
    nodes = [{"name": "Lesion", "downstream": [{"target": "Pain"}]}]
    assert compute_positions(nodes, {"Pain"})["Lesion"] == (SOURCE, 0, 0, 1)
    assert compute_positions(nodes)["Lesion"] == (ISOLATED, 0, 0, 0)


def test_position_role_is_checked_against_the_computed_position():
    assert judge("trigger", SOURCE, {}) == ("POSITION", DERIVED, SOURCE)
    facet, verdict, detail = judge("trigger", INTERIOR, {})
    assert (facet, verdict) == ("POSITION", CONTRADICTED)
    assert "INTERIOR" in detail and "SOURCE" in detail


def test_downstream_roles_accept_interior_as_well_as_sink():
    """'consequence' claims 'caused by something upstream', not 'a strict sink'."""
    assert judge("consequence", SINK, {})[1] == DERIVED
    assert judge("consequence", INTERIOR, {})[1] == DERIVED
    assert judge("consequence", SOURCE, {})[1] == CONTRADICTED
    assert judge("outcome", ISOLATED, {})[1] == CONTRADICTED


def test_interface_role_needs_the_edge_it_implies():
    assert judge("therapeutic_vulnerability", ISOLATED, {"targeted": True})[1] == DERIVED
    assert judge("therapeutic_vulnerability", ISOLATED, {"targeted": False})[1] == CONTRADICTED
    assert judge("biomarker", SINK, {"read_out": True})[1] == DERIVED
    assert judge("biomarker", SINK, {})[1] == CONTRADICTED


def test_kind_of_thing_roles_are_curated_not_checked():
    for role in ("susceptibility", "protective", "immune_evasion", "mechanism"):
        facet, verdict, _ = judge(role, SOURCE, {})
        assert verdict == CURATED, role
        assert facet in FACETS and facet not in ("POSITION", "INTERFACE", "UNMAPPED")


def test_epistemic_role_reports_whether_mechanism_confidence_is_set():
    assert judge("disputed_branch", SINK, {}, "PROVISIONAL") == (
        "EPISTEMIC", CURATED, "mechanism_confidence=PROVISIONAL"
    )
    assert judge("disputed_branch", SINK, {})[2] == "no mechanism_confidence"


def test_unknown_role_is_unmapped_rather_than_an_error():
    assert judge("something_new", SOURCE, {}) == ("UNMAPPED", UNMAPPED, "")


def test_role_table_is_well_formed():
    assert set(ROLE_FACETS) == {normalize_role(k) for k in ROLE_FACETS}
    for role, (facet, expected) in ROLE_FACETS.items():
        assert facet in FACETS and facet != "UNMAPPED", role
        if facet == "POSITION":
            assert isinstance(expected, frozenset) and expected, role
        elif facet == "INTERFACE":
            assert expected in ("targeted", "modeled", "read_out", "influenced"), role
        else:
            assert expected is None, role


def _demo_kb(tmp_path):
    kb = tmp_path / "disorders"
    kb.mkdir()
    (kb / "Demo.yaml").write_text(
        "pathophysiology:\n"
        "- name: Upstream\n"
        "  role: TRIGGER\n"
        "  downstream:\n"
        "  - target: Middle\n"
        "- name: Middle\n"
        "  role: central effector\n"
        "  downstream:\n"
        "  - target: End\n"
        "- name: End\n"
        "  role: consequence\n"
        "- name: Lone Target\n"
        "  role: therapeutic_vulnerability\n"
        "- name: Lone Claim\n"
        "  role: therapeutic_vulnerability\n"
        "- name: Untagged\n"
        "treatments:\n"
        "- name: Drug\n"
        "  target_mechanisms:\n"
        "  - target: Lone Target\n",
        encoding="utf-8",
    )
    return kb


def test_audit_reads_a_kb_directory(tmp_path):
    result = audit([_demo_kb(tmp_path)])
    assert result.total_nodes == 6
    by_name = {n.node: n for n in result.nodes}
    assert set(by_name) == {"Upstream", "Middle", "End", "Lone Target", "Lone Claim"}
    assert (by_name["Upstream"].role, by_name["Upstream"].verdict) == ("trigger", DERIVED)
    assert by_name["Middle"].role == "central_effector"
    assert by_name["Middle"].position == INTERIOR
    assert by_name["End"].verdict == DERIVED and by_name["End"].position == SINK
    assert by_name["Lone Target"].targeted and by_name["Lone Target"].verdict == DERIVED
    assert not by_name["Lone Claim"].targeted
    assert by_name["Lone Claim"].verdict == CONTRADICTED
    assert result.raw_spellings["TRIGGER"] == 1


def test_reports_over_the_demo_kb(tmp_path):
    result = audit([_demo_kb(tmp_path)])
    s = summarize(result)
    assert s["tagged"] == 5 and s["raw_spellings"] == 4 and s["normalized_values"] == 4
    assert s["verdicts"][DERIVED] == 4 and s["verdicts"][CONTRADICTED] == 1
    assert s["residue"] == 1 and s["residue_by_facet"] == {"INTERFACE": 1}
    assert s["causal_function_residue"] == 1
    assert casing_variants(result) == {}
    assert crosstab(result)["therapeutic_vulnerability"][ISOLATED] == 2
    rows = {row[0]: row for row in facet_table(result)}
    assert rows["POSITION"][2:] == (3, 3, 0, 0)
    assert rows["INTERFACE"][2:] == (2, 1, 1, 0)


def test_casing_variants_group_raw_spellings(tmp_path):
    kb = tmp_path / "disorders"
    kb.mkdir()
    (kb / "Demo.yaml").write_text(
        "pathophysiology:\n"
        "- name: A\n  role: Trigger\n"
        "- name: B\n  role: trigger\n"
        "- name: C\n  role: trigger\n"
        "- name: D\n  role: mediator\n",
        encoding="utf-8",
    )
    variants = casing_variants(audit([kb]))
    assert variants == {"trigger": [("trigger", 2), ("Trigger", 1)]}
