"""Structured-source commands write into the tree they are run in (#15051).

Before the fix, ``dismech.structured_sources.cli`` derived its output
directories from its own ``__file__``. With one virtualenv shared across git
worktrees that is the primary checkout, so ``just fetch-reference ORPHA:...``
run in a worktree wrote its cache file into the primary checkout and reported
success.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from dismech import repo_root as rr
from dismech.structured_sources import cli
from dismech.structured_sources.clingen import ClinGenSource
from tests.test_clingen_structured_source import CSV_TEXT, HEXB_ASSERTION

MODULE_TREE = Path(cli.__file__).resolve().parents[3]
CACHE_NAME = (
    "CGGV_assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z.md"
)


def _make_tree(root: Path) -> Path:
    """A minimal dismech-shaped tree: justfile, kb/, references_cache/, a CSV."""
    root.mkdir(parents=True)
    (root / "justfile").write_text("", encoding="utf-8")
    (root / "kb" / "disorders").mkdir(parents=True)
    (root / "references_cache").mkdir()
    clingen = root / "data" / "clingen"
    clingen.mkdir(parents=True)
    (clingen / "gene_validity.csv").write_text(CSV_TEXT, encoding="utf-8")
    return root


def _stat(path: Path) -> tuple[int, int] | None:
    return (path.stat().st_mtime_ns, path.stat().st_size) if path.exists() else None


@pytest.fixture()
def no_manifest(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep a manifest another test loaded from changing the pin checks."""
    monkeypatch.delenv(rr.ENV_VAR, raising=False)
    for attr in ("bulk_files", "_manifest_snapshot_date", "_manifest_schema_tag"):
        monkeypatch.setattr(
            ClinGenSource, attr, getattr(ClinGenSource, attr, None), raising=False
        )


def test_find_repo_root_walks_up_from_a_subdirectory(tmp_path: Path):
    tree = _make_tree(tmp_path / "wt")
    assert rr.find_repo_root(tree / "kb" / "disorders") == tree.resolve()
    assert rr.find_repo_root(tmp_path) is None


def test_env_override_wins_over_the_working_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    tree = _make_tree(tmp_path / "wt")
    other = tmp_path / "elsewhere"
    other.mkdir()
    monkeypatch.chdir(tree)
    monkeypatch.setenv(rr.ENV_VAR, str(other))
    assert rr.repo_root() == other.resolve()
    assert not rr.is_in_working_tree(other)


def test_outside_any_checkout_falls_back_to_the_module_tree_with_a_warning(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
):
    monkeypatch.delenv(rr.ENV_VAR, raising=False)
    monkeypatch.chdir(tmp_path)
    rr._warn_fallback.cache_clear()
    with caplog.at_level("WARNING", logger="dismech.repo_root"):
        assert rr.repo_root() == MODULE_TREE
    assert any(rr.ENV_VAR in r.getMessage() for r in caplog.records)


def test_rebuild_writes_under_the_working_tree_not_the_module_tree(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, no_manifest: None
):
    tree = _make_tree(tmp_path / "wt")
    module_copy = MODULE_TREE / "references_cache" / CACHE_NAME
    before = _stat(module_copy)
    monkeypatch.chdir(tree)

    result = CliRunner().invoke(
        cli.app, ["rebuild", "clingen", "--csv-only", "--id", HEXB_ASSERTION]
    )

    assert result.exit_code == 0, result.output
    assert (tree / "references_cache" / CACHE_NAME).exists()
    # Read from the tree's own data/clingen/, not the module tree's.
    assert "CSV snapshot **2026-01-24**" in (
        tree / "references_cache" / CACHE_NAME
    ).read_text(encoding="utf-8")
    assert _stat(module_copy) == before
    assert "outside the tree" not in result.output


def test_rebuild_from_a_subdirectory_still_writes_at_the_tree_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, no_manifest: None
):
    tree = _make_tree(tmp_path / "wt")
    monkeypatch.chdir(tree / "kb" / "disorders")

    result = CliRunner().invoke(
        cli.app, ["rebuild", "clingen", "--csv-only", "--id", HEXB_ASSERTION]
    )

    assert result.exit_code == 0, result.output
    assert (tree / "references_cache" / CACHE_NAME).exists()
    assert not (tree / "kb" / "disorders" / "references_cache").exists()


def test_rebuild_honours_the_env_override_and_says_where_it_wrote(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, no_manifest: None
):
    tree = _make_tree(tmp_path / "wt")
    target = _make_tree(tmp_path / "target")
    monkeypatch.chdir(tree)
    monkeypatch.setenv(rr.ENV_VAR, str(target))

    result = CliRunner().invoke(
        cli.app, ["rebuild", "clingen", "--csv-only", "--id", HEXB_ASSERTION]
    )

    assert result.exit_code == 0, result.output
    assert (target / "references_cache" / CACHE_NAME).exists()
    assert not (tree / "references_cache" / CACHE_NAME).exists()
    # A default destination outside the tree the command ran in is named.
    assert "outside the tree" in result.output


def test_clingen_committed_fallback_comes_from_the_working_tree(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    tree = _make_tree(tmp_path / "wt")
    committed = tree / "cache" / "clingen" / "gene_validity.csv"
    committed.parent.mkdir(parents=True)
    committed.write_text(CSV_TEXT, encoding="utf-8")
    monkeypatch.delenv(rr.ENV_VAR, raising=False)
    monkeypatch.chdir(tree)

    src = ClinGenSource(tree / "data" / "empty", include_report_text=False)
    assert src._csv_path() == committed.resolve()
