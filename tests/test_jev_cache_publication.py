"""Exercise the workflow's publication shell against disposable local Git repos."""

import os
import subprocess
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
CACHE = "analysis/classification/jev"


def git(repo, *args):
    return subprocess.run(
        ["git", *args], cwd=repo, text=True, capture_output=True, check=True
    ).stdout.strip()


def prepare(tmp_path):
    remote = tmp_path / "remote.git"
    git(tmp_path, "init", "--bare", str(remote))
    repo = tmp_path / "checkout"
    git(tmp_path, "init", "-b", "base", str(repo))
    git(repo, "config", "user.name", "Test")
    git(repo, "config", "user.email", "test@example.org")
    git(repo, "remote", "add", "origin", str(remote))
    directory = repo / CACHE
    directory.mkdir(parents=True)
    (directory / "README.md").write_text("History\n")
    (repo / "code.txt").write_text("original code\n")
    git(repo, "add", "--", "code.txt", f"{CACHE}/README.md")
    git(repo, "commit", "-m", "base")
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    gh = fake_bin / "gh"
    gh.write_text("""#!/bin/sh
case "$*" in
  *"--jq .state"*) printf '%s\\n' "$PR_STATE" ;;
  *"--jq .headRefOid"*) printf '%s\\n' "$PR_HEAD" ;;
  *) exit 0 ;;
esac
""")
    gh.chmod(0o755)
    env = {
        **os.environ,
        "PATH": str(fake_bin) + os.pathsep + os.environ["PATH"],
        "RUNNER_TEMP": str(tmp_path),
        "PENDING_HEAD": "",
        "PR_NUMBER": "",
        "CACHE_BRANCH": "auto/jev-assessments-test",
        "GITHUB_REPOSITORY": "test/repo",
        "GITHUB_RUN_ID": "123",
        "GITHUB_RUN_ATTEMPT": "1",
    }
    workflow = yaml.safe_load(
        (ROOT / ".github/workflows/jev-evidence-audit.yaml").read_text()
    )
    script = next(
        step["run"]
        for step in workflow["jobs"]["persist"]["steps"]
        if step.get("name") == "Propose assessment history updates"
    )
    return repo, env, script


def publish(repo, env, script):
    return subprocess.run(
        ["bash", "-e", "-o", "pipefail", "-c", script],
        cwd=repo,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def change_cache(repo, text):
    directory = repo / CACHE / "Example"
    directory.mkdir(exist_ok=True)
    (directory / "evidence_claim_match.yaml").write_text(text)


def test_publication_changes_only_cache_on_pending_head(tmp_path):
    repo, env, script = prepare(tmp_path)
    base = git(repo, "rev-parse", "HEAD")
    change_cache(repo, "assessments: {first: retained}\n")
    result = publish(repo, env, script)
    assert result.returncode == 0, result.stderr
    pending = git(repo, "rev-parse", "refs/remotes/origin/" + env["CACHE_BRANCH"])
    assert git(repo, "show", pending + ":code.txt") == "original code"
    # Advance main independently, without putting its code changes in the data PR.
    (repo / "code.txt").write_text("new code on main\n")
    git(repo, "add", "--", "code.txt")
    git(repo, "commit", "-m", "main advances")
    main_head = git(repo, "rev-parse", "HEAD")
    assert main_head != base
    change_cache(repo, "assessments: {first: retained, second: added}\n")
    env.update(PENDING_HEAD=pending, PR_NUMBER="7", PR_STATE="OPEN", PR_HEAD=pending)
    result = publish(repo, env, script)
    assert result.returncode == 0, result.stderr
    updated = git(repo, "rev-parse", "refs/remotes/origin/" + env["CACHE_BRANCH"])
    assert git(repo, "rev-parse", updated + "^") == pending
    assert (
        git(repo, "diff", "--name-only", pending, updated)
        == f"{CACHE}/Example/evidence_claim_match.yaml"
    )
    assert git(repo, "show", updated + ":code.txt") == "original code"
    assert git(repo, "rev-parse", "HEAD") == main_head
    assert git(repo, "diff", "--cached", "--name-only") == ""
    # Repeating an unchanged publication does not create another commit.
    env.update(PENDING_HEAD=updated, PR_HEAD=updated)
    assert publish(repo, env, script).returncode == 0
    assert (
        git(repo, "rev-parse", "refs/remotes/origin/" + env["CACHE_BRANCH"]) == updated
    )


@pytest.mark.parametrize("state,moved", [("CLOSED", False), ("OPEN", True)])
def test_publication_stops_when_review_branch_changes(tmp_path, state, moved):
    repo, env, script = prepare(tmp_path)
    change_cache(repo, "assessments: {first: retained}\n")
    assert publish(repo, env, script).returncode == 0
    pending = git(repo, "rev-parse", "refs/remotes/origin/" + env["CACHE_BRANCH"])
    env.update(
        PENDING_HEAD=pending,
        PR_NUMBER="7",
        PR_STATE=state,
        PR_HEAD="changed" if moved else pending,
    )
    change_cache(repo, "assessments: {first: retained, second: added}\n")
    result = publish(repo, env, script)
    assert result.returncode != 0
    assert (
        git(repo, "rev-parse", "refs/remotes/origin/" + env["CACHE_BRANCH"]) == pending
    )
