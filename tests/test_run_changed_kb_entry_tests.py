"""Tests for scripts/run_changed_kb_entry_tests.py (issue #18313)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "run_changed_kb_entry_tests.py"

spec = importlib.util.spec_from_file_location("run_changed_kb_entry_tests", SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


@pytest.fixture
def fake_repo(tmp_path):
    for rel in (
        "kb/disorders/Asthma.yaml",
        "kb/disorders/Asthma_Severe.yaml",
        "kb/disorders/Fructose-1,6-Bisphosphatase_Deficiency.yaml",
        "kb/modules/fibrotic_response.yaml",
        "kb/comorbidities/A_B.yaml",
        "kb/groupings/G.yaml",
    ):
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("name: x\n")
    return tmp_path


def test_maps_each_kind_to_its_parametrized_test(fake_repo):
    ids, skipped = runner.node_ids(
        [
            "kb/disorders/Asthma.yaml",
            "kb/modules/fibrotic_response.yaml",
            "kb/comorbidities/A_B.yaml",
        ],
        fake_repo,
    )
    assert ids == [
        "tests/test_data.py::test_disorder_file[kb/disorders/Asthma.yaml]",
        "tests/test_data.py::test_module_file[kb/modules/fibrotic_response.yaml]",
        "tests/test_data.py::test_comorbidity_file[kb/comorbidities/A_B.yaml]",
    ]
    assert skipped == []


def test_selects_only_the_named_file_not_a_prefix_match(fake_repo):
    ids, _ = runner.node_ids(["kb/disorders/Asthma.yaml"], fake_repo)
    assert len(ids) == 1
    assert "Asthma_Severe" not in ids[0]


def test_comma_in_filename_survives(fake_repo):
    ids, _ = runner.node_ids(
        ["kb/disorders/Fructose-1,6-Bisphosphatase_Deficiency.yaml"], fake_repo
    )
    expected = (
        "tests/test_data.py::test_disorder_file"
        "[kb/disorders/Fructose-1,6-Bisphosphatase_Deficiency.yaml]"
    )
    assert ids == [expected]


def test_skips_deleted_other_kinds_and_history(fake_repo):
    ids, skipped = runner.node_ids(
        [
            "kb/disorders/Deleted.yaml",
            "kb/groupings/G.yaml",
            "kb/disorders/Asthma.history.yaml",
            "README.md",
        ],
        fake_repo,
    )
    assert ids == []
    assert len(skipped) == 4
    assert any("deleted" in s for s in skipped)


def test_duplicates_collapse(fake_repo):
    ids, _ = runner.node_ids(
        ["kb/disorders/Asthma.yaml", str(fake_repo / "kb/disorders/Asthma.yaml")],
        fake_repo,
    )
    assert len(ids) == 1


def test_no_files_exits_zero_without_running_pytest(fake_repo, monkeypatch):
    monkeypatch.setattr(runner, "_repo_root", lambda: fake_repo)

    def boom(*_a, **_k):
        raise AssertionError("pytest must not run with nothing to test")

    monkeypatch.setattr(runner.subprocess, "call", boom)
    assert runner.main(["kb/groupings/G.yaml"]) == 0


def test_kind_table_matches_the_per_file_tests_in_test_data():
    """Every mapped test exists in tests/test_data.py and is parametrized over
    files from the directory the table maps to, so a rename there breaks this
    rather than silently testing nothing."""
    source = (ROOT / "tests" / "test_data.py").read_text()
    dir_constants = {
        "kb/disorders": "DISORDER_FILES",
        "kb/modules": "MODULE_FILES",
        "kb/comorbidities": "COMORBIDITY_FILES",
    }
    assert set(runner.KIND_TESTS) == set(dir_constants)
    for directory, test_name in runner.KIND_TESTS.items():
        expected = (
            f'@pytest.mark.parametrize("filepath", {dir_constants[directory]}, '
            f"ids=_file_id)\ndef {test_name}("
        )
        assert expected in source, (
            f"{test_name} is no longer parametrized over "
            f"{dir_constants[directory]} in tests/test_data.py"
        )


def test_large_batches_run_under_xdist(fake_repo, monkeypatch):
    calls = []
    monkeypatch.setattr(runner, "_repo_root", lambda: fake_repo)
    monkeypatch.setattr(
        runner, "node_ids", lambda paths, root: ([f"id{i}" for i in range(50)], [])
    )
    monkeypatch.setattr(
        runner.subprocess, "call", lambda cmd, cwd: calls.append(cmd) or 0
    )
    runner.main([])
    assert "-n" in calls[0]


def test_small_batches_run_serially(fake_repo, monkeypatch):
    calls = []
    monkeypatch.setattr(runner, "_repo_root", lambda: fake_repo)
    monkeypatch.setattr(
        runner.subprocess, "call", lambda cmd, cwd: calls.append(cmd) or 0
    )
    runner.main(["kb/disorders/Asthma.yaml"])
    assert "-n" not in calls[0]
    assert (
        calls[0][-1]
        == "tests/test_data.py::test_disorder_file[kb/disorders/Asthma.yaml]"
    )
