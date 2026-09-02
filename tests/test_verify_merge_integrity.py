"""Tests for the post-push merge-integrity verifier.

The interesting cases run against a real throwaway git repository so the tree
identity being relied on -- ``merge-tree --write-tree parent head ==
commit^{tree}`` for a clean squash -- is exercised with actual git, not a
mock of it. PR metadata lookups are stubbed; everything else is live plumbing.
"""

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import verify_merge_integrity as vmi


def test_pr_number_from_subject():
    assert vmi.pr_number_from_subject("Fix the thing (#123)") == 123
    assert vmi.pr_number_from_subject("Fix the thing (#123)  ") == 123
    assert vmi.pr_number_from_subject("Fix issue #123") is None
    assert vmi.pr_number_from_subject("(#12) leading not trailing") is None
    assert vmi.pr_number_from_subject("Ordinary direct push") is None


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def _commit_file(repo: Path, name: str, content: str, message: str) -> str:
    (repo / name).write_text(content)
    _git(repo, "add", name)
    _git(repo, "commit", "-q", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


@pytest.fixture()
def squash_repo(tmp_path, monkeypatch):
    """A repo where PR head H (from base A) was squashed onto a moved main M2.

    Returns (H, M2, expected_tree): the ingredients for building both a
    correct squash commit and a corrupted one that silently drops M2's change
    -- the #2034 incident signature.
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "test@example.org")
    _git(repo, "config", "user.name", "Test")
    base = _commit_file(repo, "a.txt", "base\n", "base")
    # PR branch from base edits b.txt only.
    _git(repo, "checkout", "-q", "-b", "feature", base)
    head = _commit_file(repo, "b.txt", "feature\n", "feature work")
    # main moves on independently (edits c.txt).
    _git(repo, "checkout", "-q", "-", )
    m2 = _commit_file(repo, "c.txt", "other pr\n", "Other change (#6)")
    expected_tree = _git(repo, "merge-tree", "--write-tree", m2, head)
    monkeypatch.chdir(repo)
    return repo, head, m2, expected_tree


def _squash_commit(repo: Path, tree: str, parent: str, subject: str) -> str:
    sha = _git(repo, "commit-tree", tree, "-p", parent, "-m", subject)
    _git(repo, "update-ref", "HEAD", sha)
    return sha


def test_correct_squash_verifies(squash_repo, monkeypatch):
    repo, head, m2, expected_tree = squash_repo
    commit = _squash_commit(repo, expected_tree, m2, "Feature work (#7)")
    monkeypatch.setattr(
        vmi, "gh_pr",
        lambda repo_, n: {"head_sha": head, "merge_commit_sha": commit},
    )
    result = vmi.verify_commit("owner/name", commit)
    assert result.status == vmi.VERIFIED
    assert result.pr_number == 7


def test_squash_that_drops_prior_changes_is_a_mismatch(squash_repo, monkeypatch):
    # The corrupted commit carries the PR head's tree verbatim: b.txt is
    # there, but M2's c.txt has vanished -- a silent revert of another PR.
    repo, head, m2, _ = squash_repo
    head_tree = _git(repo, "rev-parse", f"{head}^{{tree}}")
    commit = _squash_commit(repo, head_tree, m2, "Feature work (#7)")
    monkeypatch.setattr(
        vmi, "gh_pr",
        lambda repo_, n: {"head_sha": head, "merge_commit_sha": commit},
    )
    result = vmi.verify_commit("owner/name", commit)
    assert result.status == vmi.MISMATCH
    assert "does not contain" in result.detail


def test_merge_commits_are_skipped_not_judged(squash_repo):
    repo, head, _m2, _ = squash_repo
    _git(repo, "merge", "-q", "--no-ff", "-m", "Merge feature (#7)", head)
    merge_sha = _git(repo, "rev-parse", "HEAD")
    result = vmi.verify_commit("owner/name", merge_sha)
    assert result.status == vmi.SKIPPED_MERGE_COMMIT


def test_direct_push_without_pr_number_is_skipped(squash_repo):
    repo, *_ = squash_repo
    sha = _commit_file(repo, "d.txt", "direct\n", "hotfix pushed directly")
    result = vmi.verify_commit("owner/name", sha)
    assert result.status == vmi.SKIPPED_NO_PR_NUMBER


def test_stale_pr_mapping_is_skipped_not_guessed(squash_repo, monkeypatch):
    repo, head, m2, expected_tree = squash_repo
    commit = _squash_commit(repo, expected_tree, m2, "Feature work (#7)")
    monkeypatch.setattr(
        vmi, "gh_pr",
        lambda repo_, n: {"head_sha": head, "merge_commit_sha": "f" * 40},
    )
    result = vmi.verify_commit("owner/name", commit)
    assert result.status == vmi.SKIPPED_PR_MAPPING
