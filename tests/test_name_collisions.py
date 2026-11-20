"""Tests for pathograph name-collision detection (issue #15443).

Rows sharing a ``name`` collapse into one node in ``dismech.graph``. These
tests pin the classification, that :func:`collect_graph_nodes` is unchanged by
the shared iterator, the gate's baseline behaviour, and its wiring.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from dismech.graph import (
    build_causal_graph,
    collect_graph_nodes,
    find_name_collisions,
    iter_graph_node_rows,
)

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_name_collisions.py"
BASELINE = ROOT / "tests" / "name_collision_baseline.txt"
sys.path.insert(0, str(ROOT / "scripts"))


def _kinds(disorder):
    return {c.name: c.kind for c in find_name_collisions(disorder)}


def test_unstratified_same_section_rows_collide():
    d = {"phenotypes": [{"name": "Dehydration"}, {"name": "Dehydration"}]}
    assert _kinds(d) == {"Dehydration": "UNSTRATIFIED"}


def test_rows_with_distinct_subtypes_are_stratified():
    d = {
        "phenotypes": [
            {"name": "Primary amenorrhea", "subtype": "CAIS"},
            {"name": "Primary amenorrhea", "subtype": "PAIS"},
        ]
    }
    assert _kinds(d) == {"Primary amenorrhea": "STRATIFIED"}


@pytest.mark.parametrize(
    "subtypes",
    [
        ("Vascular EDS", "Vascular EDS"),  # same subtype twice
        ("SGCG", None),  # one row unstratified
        ("Type 1", "Type 2", None),  # Gaucher GBA1 shape
    ],
)
def test_partial_or_repeated_subtypes_are_unstratified(subtypes):
    rows = [{"name": "X", **({"subtype": s} if s else {})} for s in subtypes]
    assert _kinds({"genetic": rows}) == {"X": "UNSTRATIFIED"}


def test_cross_section_match_does_not_hide_an_unstratified_pair():
    """Review of #16431: classifying the whole name let CROSS_SECTION win."""
    d = {
        "pathophysiology": [{"name": "Fatigue"}],
        "phenotypes": [{"name": "Fatigue"}, {"name": "Fatigue"}],
    }
    kinds = sorted(c.kind for c in find_name_collisions(d))
    assert kinds == ["CROSS_SECTION", "UNSTRATIFIED"]
    (pair,) = [c for c in find_name_collisions(d) if c.kind == "UNSTRATIFIED"]
    assert {r.source for r in pair.rows} == {"phenotypes"}


def test_cross_section_includes_variants_and_animal_models():
    d = {
        "pathophysiology": [{"name": "Nephrocalcinosis"}],
        "phenotypes": [{"name": "Nephrocalcinosis"}],
        "genetic": [{"name": "ASPA", "variants": [{"name": "SVA insertion"}]}],
        "animal_models": [{"name": "SVA insertion"}],
    }
    assert _kinds(d) == {
        "Nephrocalcinosis": "CROSS_SECTION",
        "SVA insertion": "CROSS_SECTION",
    }


def test_unique_names_report_nothing_and_lost_rows_counts_merges():
    assert find_name_collisions({"phenotypes": [{"name": "A"}, {"name": "B"}]}) == []
    d = {"phenotypes": [{"name": "A"}, {"name": "A"}, {"name": "A"}]}
    (collision,) = find_name_collisions(d)
    assert collision.lost_rows == 2


def test_collect_graph_nodes_still_lets_the_last_row_win():
    d = {
        "phenotypes": [
            {"name": "Bone Pain", "description": "first"},
            {"name": "Bone Pain", "description": "second"},
        ]
    }
    nodes = collect_graph_nodes(d)
    assert list(nodes) == ["Bone Pain"]
    assert nodes["Bone Pain"].description == "second"
    assert len(list(iter_graph_node_rows(d))) == 2


def test_graph_node_count_matches_the_issue_reproducer():
    """54 rows, 44 names, 44 nodes on main when #15443 was filed."""
    from dismech import yaml_io

    d = yaml_io.safe_load_path(
        ROOT / "kb/disorders/Androgen_Insensitivity_Syndrome.yaml"
    )
    rows = [r for r in iter_graph_node_rows(d) if r.source == "phenotypes"]
    names = {r.name for r in rows}
    nodes = [
        n for n, i in build_causal_graph(d).nodes.items() if i.node_type == "phenotype"
    ]
    lost = sum(
        c.lost_rows for c in find_name_collisions(d) if c.rows[0].source == "phenotypes"
    )
    assert len(rows) - len(names) == lost
    assert len(nodes) == len(names)


@pytest.mark.ci_step_twin("uv run python scripts/check_name_collisions.py")
def test_committed_kb_has_no_new_unstratified_collisions():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_new_unstratified_collision_fails_the_gate(tmp_path, capsys):
    import check_name_collisions as mod

    entry = tmp_path / "Example.yaml"
    entry.write_text(
        "name: Example\nphenotypes:\n- name: Fatigue\n- name: Fatigue\n",
        encoding="utf-8",
    )
    assert mod.main([str(entry)]) == 1
    assert "'Fatigue'" in capsys.readouterr().out


def test_stratified_and_cross_section_do_not_fail_the_gate(tmp_path):
    import check_name_collisions as mod

    entry = tmp_path / "Example.yaml"
    entry.write_text(
        "name: Example\n"
        "pathophysiology:\n- name: Fibrosis\n"
        "phenotypes:\n- name: Fibrosis\n"
        "- name: Amenorrhea\n  subtype: CAIS\n- name: Amenorrhea\n  subtype: PAIS\n",
        encoding="utf-8",
    )
    assert mod.main([str(entry)]) == 0


def test_extra_copy_of_a_grandfathered_name_fails(tmp_path, monkeypatch, capsys):
    """Review of #16431: the baseline grandfathers a row count, not just a name."""
    import check_name_collisions as mod

    entry = tmp_path / "Example.yaml"
    entry.write_text(
        "name: Example\nphenotypes:\n- name: Fatigue\n- name: Fatigue\n- name: Fatigue\n",
        encoding="utf-8",
    )
    key = f"{mod._display(entry)}\tphenotypes\tFatigue"
    monkeypatch.setattr(mod, "load_baseline", lambda: {key: 2})
    assert mod.main([str(entry)]) == 1
    monkeypatch.setattr(mod, "load_baseline", lambda: {key: 3})
    assert mod.main([str(entry)]) == 0
    capsys.readouterr()


def test_missing_path_is_a_usage_error(tmp_path, capsys):
    import check_name_collisions as mod

    assert mod.main([str(tmp_path / "Nope.yaml")]) == 2
    assert "OK:" not in capsys.readouterr().out


def test_update_baseline_refuses_paths_and_never_adds(tmp_path):
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--update-baseline", "kb/disorders/Cholera.yaml"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode != 0
    assert "whole-KB only" in result.stderr


def test_baseline_is_well_formed_and_sorted():
    rows = [
        line
        for line in BASELINE.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    ]
    assert rows == sorted(rows)
    for row in rows:
        fields = row.split("\t")
        assert len(fields) == 4, row
        assert int(fields[3]) >= 2, row


def test_gate_is_wired_into_qc_and_ci():
    justfile = (ROOT / "project.justfile").read_text()
    qc = next(line for line in justfile.splitlines() if line.startswith("qc:"))
    assert "check-name-collisions" in qc.split()
    workflow = (ROOT / ".github" / "workflows" / "main.yaml").read_text()
    assert ":: uv run python scripts/check_name_collisions.py\n" in workflow
