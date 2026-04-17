"""Tests for protected-path merge auditing."""

from __future__ import annotations

import subprocess
from pathlib import Path

from dismech.git_audit import classify_deleted_paths
from dismech.git_audit import inspect_merge_commit
from dismech.git_audit import load_allow_patterns
from dismech.git_audit import scan_merge_history
from dismech.git_audit import stale_resolutions_for_merge_commit


def test_load_allow_patterns_ignores_blank_lines_and_comments(tmp_path: Path) -> None:
    allowlist = tmp_path / "allowlist.txt"
    allowlist.write_text(
        """
# comment
.claude/**

CLAUDE.md  # inline comment
""".strip(),
        encoding="utf-8",
    )

    assert load_allow_patterns(allowlist) == (".claude/**", "CLAUDE.md")


def test_classify_deleted_paths_respects_allowlist_and_derived_paths() -> None:
    classified = classify_deleted_paths(
        (
            ".claude/skills/boss/SKILL.md",
            "cache/enums/example.csv",
            "pages/disorders/Foo.html",
            "notes/todo.md",
            "CLAUDE.md",
        ),
        allow_patterns=("CLAUDE.md",),
    )

    assert classified.protected == (".claude/skills/boss/SKILL.md",)
    assert classified.allowed == ("CLAUDE.md",)
    assert classified.ignored == ("pages/disorders/Foo.html",)
    assert classified.other == ("cache/enums/example.csv", "notes/todo.md")


def test_inspect_merge_commit_detects_first_parent_deletion(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    _commit_file(repo, "CLAUDE.md", "one\n", "add claude")
    _git(repo, "checkout", "-b", "feature/delete-claude")
    _git(repo, "rm", "CLAUDE.md")
    _git(repo, "commit", "-m", "delete claude")
    _git(repo, "checkout", "main")
    _git(repo, "merge", "--no-ff", "-m", "merge delete claude", "feature/delete-claude")

    record = inspect_merge_commit(repo, "HEAD")
    assert record.deleted.protected == ("CLAUDE.md",)
    assert record.stale.protected == ()


def test_stale_resolutions_for_merge_commit_detects_second_parent_win(
    tmp_path: Path,
) -> None:
    repo = _init_repo(tmp_path)
    _commit_file(repo, "CLAUDE.md", "old\n", "seed claude")
    _git(repo, "checkout", "-b", "feature/stale")
    feature_tip = _git_output(repo, "rev-parse", "HEAD").strip()
    _git(repo, "checkout", "main")
    _commit_file(repo, "CLAUDE.md", "new\n", "update claude on main")
    main_tip = _git_output(repo, "rev-parse", "HEAD").strip()

    bad_merge = _git_output(
        repo,
        "commit-tree",
        f"{feature_tip}^{{tree}}",
        "-p",
        main_tip,
        "-p",
        feature_tip,
        "-m",
        "bad stale-side merge",
    ).strip()

    resolutions = stale_resolutions_for_merge_commit(repo, bad_merge)

    assert len(resolutions) == 1
    assert resolutions[0].path == "CLAUDE.md"
    assert resolutions[0].result_blob == resolutions[0].second_parent_blob
    assert resolutions[0].result_blob != resolutions[0].first_parent_blob


def test_scan_merge_history_reports_protected_findings(tmp_path: Path) -> None:
    repo = _init_repo(tmp_path)
    _commit_file(repo, "CLAUDE.md", "old\n", "seed claude")
    _git(repo, "checkout", "-b", "feature/stale")
    feature_tip = _git_output(repo, "rev-parse", "HEAD").strip()
    _git(repo, "checkout", "main")
    _commit_file(repo, "CLAUDE.md", "new\n", "update claude on main")
    main_tip = _git_output(repo, "rev-parse", "HEAD").strip()

    bad_merge = _git_output(
        repo,
        "commit-tree",
        f"{feature_tip}^{{tree}}",
        "-p",
        main_tip,
        "-p",
        feature_tip,
        "-m",
        "bad stale-side merge",
    ).strip()
    _git(repo, "update-ref", "refs/heads/main", bad_merge)

    records = scan_merge_history(repo)
    assert len(records) == 1
    assert records[0].stale.protected == ("CLAUDE.md",)
    assert records[0].deleted.protected == ()


def _init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    _git(repo, "config", "user.name", "Test User")
    _git(repo, "config", "user.email", "test@example.org")
    return repo


def _commit_file(repo: Path, relpath: str, contents: str, message: str) -> None:
    path = repo / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(contents, encoding="utf-8")
    _git(repo, "add", relpath)
    _git(repo, "commit", "-m", message)


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True)


def _git_output(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout
