"""Publish real repair commits to disposable remotes, including branch races."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import repair_generated_cache_conflicts as repair

BOT_AUTHOR = {"login": "ai4c-agent[bot]", "is_bot": True}
HUMAN_AUTHOR = {"login": "contributor", "is_bot": False}
ACTIVE_AUTHORS = [
    pytest.param(BOT_AUTHOR, id="known-bot"),
    pytest.param(HUMAN_AUTHOR, id="human"),
]


def git(path, *args):
    return subprocess.run(
        ["git", "-C", str(path), *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def eligible(head, **overrides):
    return {
        "number": 12,
        "state": "OPEN",
        "baseRefName": "main",
        "headRefName": "repair-me",
        "headRefOid": head,
        "author": BOT_AUTHOR,
        "assignees": [],
        "isCrossRepository": False,
        "mergeable": "CONFLICTING",
        "statusCheckRollup": [],
    } | overrides


@pytest.fixture
def publication(tmp_path, monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "test-discovery")
    monkeypatch.setenv("GH_CACHE_REPAIR_TOKEN", "test-writer")
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", os.devnull)
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")
    local, remote = tmp_path / "local", tmp_path / "remote.git"
    local.mkdir()
    git(local, "init", "-q", "-b", "main")
    git(local, "config", "user.name", "Test")
    git(local, "config", "user.email", "test@example.invalid")
    git(local, "config", "commit.gpgSign", "false")
    git(local, "config", "core.hooksPath", "/dev/null")
    for name in ("ancestor", "head", "base", "concurrent"):
        (local / "example.txt").write_text(name)
        git(local, "add", "example.txt")
        git(local, "commit", "-qm", name)
    concurrent = git(local, "rev-parse", "HEAD")
    base = git(local, "rev-parse", "HEAD~1")
    head = git(local, "rev-parse", "HEAD~2")
    ancestor = git(local, "rev-parse", "HEAD~3")
    git(local, "clone", "--bare", str(local), str(remote))
    git(remote, "update-ref", "refs/heads/repair-me", head)
    tree = git(local, "rev-parse", f"{base}^{{tree}}")
    monkeypatch.setattr(
        repair,
        "build_merge",
        lambda *_: repair.MergePlan(tree, head, base, ("cache/hp/terms.csv",)),
    )
    monkeypatch.setattr(repair, "current_pr", lambda *_: eligible(head))
    monkeypatch.setattr(repair, "main_sha", lambda _: base)

    class RemoteRepo(repair.GitRepo):
        race = None
        pushes = 0

        def git(self, *args, **kwargs):
            args = list(args)
            if "https://github.com/owner/repo.git" in args:
                args[args.index("https://github.com/owner/repo.git")] = str(remote)
            if "push" in args:
                self.pushes += 1
                assert kwargs["env"]["GH_TOKEN"] == "test-writer"
                assert "GH_CACHE_REPAIR_TOKEN" not in kwargs["env"]
                if self.race == "advance":
                    git(remote, "update-ref", "refs/heads/repair-me", concurrent)
                elif self.race == "rewind":
                    git(remote, "update-ref", "refs/heads/repair-me", ancestor)
                elif self.race == "delete":
                    git(remote, "update-ref", "-d", "refs/heads/repair-me")
            return super().git(*args, **kwargs)

    return RemoteRepo(local), remote, head, base, ancestor, concurrent


@pytest.mark.parametrize(
    "author",
    ACTIVE_AUTHORS
    + [
        pytest.param({"login": "other-tool[bot]", "is_bot": True}, id="unknown-bot"),
        pytest.param(None, id="deleted-author"),
        pytest.param({}, id="unknown-author"),
    ],
)
def test_publication_keeps_both_parents_and_does_not_change_local_branch(
    publication, monkeypatch, author
):
    repo, remote, head, base, _, _ = publication
    monkeypatch.setattr(repair, "current_pr", lambda *_: eligible(head, author=author))
    before = git(repo.path, "rev-parse", "HEAD")
    local_branch = git(repo.path, "symbolic-ref", "HEAD")
    remote_branches = git(remote, "for-each-ref", "--format=%(refname)", "refs/heads")
    remote_main = git(remote, "rev-parse", "refs/heads/main")
    outcome = repair.repair_one(repo, "owner/repo", 12, dry_run=False)
    tip = git(remote, "rev-parse", "refs/heads/repair-me")
    assert git(remote, "rev-list", "--parents", "-n", "1", tip).split() == [
        tip,
        head,
        base,
    ]
    git(remote, "merge-base", "--is-ancestor", head, tip)
    git(remote, "merge-base", "--is-ancestor", base, tip)
    assert git(repo.path, "rev-parse", "HEAD") == before
    assert git(repo.path, "symbolic-ref", "HEAD") == local_branch
    assert (
        git(remote, "for-each-ref", "--format=%(refname)", "refs/heads")
        == remote_branches
    )
    assert git(remote, "rev-parse", "refs/heads/main") == remote_main
    assert outcome.startswith("REPAIRED")


@pytest.mark.parametrize("race", ["advance", "rewind", "delete"])
@pytest.mark.parametrize("author", ACTIVE_AUTHORS)
def test_racing_remote_ref_cannot_be_overwritten(
    publication, monkeypatch, race, author
):
    repo, remote, head, _, ancestor, concurrent = publication
    monkeypatch.setattr(repair, "current_pr", lambda *_: eligible(head, author=author))
    repo.race = race
    with pytest.raises(subprocess.CalledProcessError):
        repair.repair_one(repo, "owner/repo", 12, dry_run=False)
    if race == "delete":
        result = subprocess.run(
            ["git", "-C", str(remote), "show-ref", "--verify", "refs/heads/repair-me"],
            capture_output=True,
            check=False,
        )
        assert result.returncode != 0
    else:
        assert git(remote, "rev-parse", "refs/heads/repair-me") == (
            concurrent if race == "advance" else ancestor
        )


@pytest.mark.parametrize(
    "change", ["head", "assignment", "base", "branch", "closed", "fork", "checks"]
)
@pytest.mark.parametrize("author", ACTIVE_AUTHORS)
def test_rechecks_mutation_guards_before_publishing(
    publication, monkeypatch, change, author
):
    repo, remote, head, base, _, concurrent = publication
    calls = 0

    def current(*_):
        nonlocal calls
        calls += 1
        pr = eligible(head, author=author)
        if calls > 1:
            if change == "head":
                pr["headRefOid"] = concurrent
            elif change == "assignment":
                pr["assignees"] = [{"login": "maintainer"}]
            elif change == "branch":
                pr["headRefName"] = "other-branch"
            elif change == "closed":
                pr["state"] = "CLOSED"
            elif change == "fork":
                pr["isCrossRepository"] = True
            elif change == "checks":
                pr["statusCheckRollup"] = [{"status": "IN_PROGRESS"}]
        return pr

    monkeypatch.setattr(repair, "current_pr", current)
    monkeypatch.setattr(
        repair,
        "main_sha",
        lambda _: concurrent if calls > 1 and change == "base" else base,
    )
    with pytest.raises(repair.UnsafeMerge):
        repair.repair_one(repo, "owner/repo", 12, dry_run=False)
    assert calls == 2, "repair must reach the final guard before refusing the update"
    assert repo.pushes == 0
    assert git(remote, "rev-parse", "refs/heads/repair-me") == head


@pytest.mark.parametrize("author", ACTIVE_AUTHORS)
def test_dry_run_never_needs_writer_or_publishes(publication, monkeypatch, author):
    repo, remote, head, *_ = publication
    monkeypatch.setattr(repair, "current_pr", lambda *_: eligible(head, author=author))
    monkeypatch.delenv("GH_CACHE_REPAIR_TOKEN")
    assert repair.repair_one(repo, "owner/repo", 12, dry_run=True).startswith(
        "WOULD REPAIR"
    )
    assert repo.pushes == 0
    assert git(remote, "rev-parse", "refs/heads/repair-me") == head


def test_omitted_author_does_not_block_cache_repair():
    pr = eligible("a" * 40)
    pr.pop("author")
    repair.repair_guard(pr)


def test_cache_discovery_excludes_fork_and_unknown_heads(monkeypatch):
    same_repo = eligible("a" * 40)
    prs = [same_repo]
    for number, value in enumerate((True, None, "false", 0), start=20):
        prs.append(eligible("b" * 40, number=number, isCrossRepository=value))
    missing = eligible("c" * 40, number=24)
    del missing["isCrossRepository"]
    prs.append(missing)

    def discover(*args):
        assert args[:2] == ("pr", "list")
        assert "isCrossRepository" in args[args.index("--json") + 1].split(",")
        return prs

    repaired = []

    def repair_one(_local, _repo, number, **_kwargs):
        repaired.append(number)
        return "WOULD REPAIR"

    monkeypatch.setattr(repair, "gh", discover)
    monkeypatch.setattr(repair, "repair_one", repair_one)
    assert repair.main(["--repo", "owner/repo", "--dry-run"]) == 0
    assert repaired == [same_repo["number"]]


def test_discovery_env_strips_writer_and_git_overrides(monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "reader")
    monkeypatch.setenv("GH_CACHE_REPAIR_TOKEN", "writer")
    monkeypatch.setenv("GIT_INDEX_FILE", "/untrusted/index")
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    env = repair.process_env()
    assert env["GH_TOKEN"] == "reader"
    assert "GH_CACHE_REPAIR_TOKEN" not in env
    assert "GIT_INDEX_FILE" not in env and "GIT_CONFIG_COUNT" not in env


def test_zero_limit_needs_no_token_or_network(monkeypatch):
    monkeypatch.delenv("GH_CACHE_REPAIR_TOKEN", raising=False)
    monkeypatch.setattr(repair, "gh", lambda *_: pytest.fail("network call"))
    assert repair.main(["--repo", "owner/repo", "--max-repairs", "0"]) == 0


@pytest.mark.parametrize(
    "checks",
    [None, {}, [{}], [None], [{"status": "COMPLETED"}], [{"state": "UNKNOWN"}]],
)
def test_incomplete_check_metadata_cannot_authorize_a_push(checks):
    pr = eligible("a" * 40)
    pr["statusCheckRollup"] = checks
    with pytest.raises(repair.UnsafeMerge):
        repair.repair_guard(pr)


def test_controller_errors_are_not_reported_as_a_successful_sweep(monkeypatch):
    def fail(*args, **kwargs):
        raise subprocess.CalledProcessError(128, ["git"])

    monkeypatch.setattr(repair, "repair_one", fail)
    assert (
        repair.main(["--repo", "owner/repo", "--specific-pr", "12", "--dry-run"]) == 1
    )


def test_cache_job_runs_trusted_code_before_agent_and_without_project_install():
    root = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((root / ".github/workflows/pr-shepherd.yml").read_text())
    job = workflow["jobs"]["repair-caches"]
    steps = {step["name"]: step for step in job["steps"]}
    assert set(job["permissions"].values()) == {"read"}
    checkout = steps["Checkout trusted default branch"]["with"]
    assert checkout["ref"] == "${{ github.event.repository.default_branch }}"
    assert checkout["persist-credentials"] is False
    token = steps["Generate scoped cache repair token"]["with"]
    assert {k: v for k, v in token.items() if k.startswith("permission-")} == {
        "permission-contents": "write"
    }
    run = steps["Repair additive cache conflicts (deterministic)"]
    assert "python scripts/repair_generated_cache_conflicts.py" in run["run"]
    assert "uv " not in str(job) and "claude-code-action" not in str(job)
    assert workflow["jobs"]["shepherd"]["needs"] == "repair-caches"
    assert "!cancelled()" in workflow["jobs"]["shepherd"]["if"]
    ci = (root / ".github/workflows/main.yaml").read_text()
    assert "'scripts/generated_cache_merge.py'" in ci
    assert "'scripts/repair_generated_cache_conflicts.py'" in ci
