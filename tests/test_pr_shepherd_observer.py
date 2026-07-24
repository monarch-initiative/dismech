from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "pr-shepherd.yml"
OBSERVER_PATH = ROOT / ".github" / "scripts" / "pr_shepherd_observer.py"
ACTION_SHA = "44423bdec74b97d67543eb16c110546762c110b2"

spec = importlib.util.spec_from_file_location("pr_shepherd_observer", OBSERVER_PATH)
assert spec and spec.loader
observer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(observer)


def _pull(
    number: int,
    *,
    repo: str = "monarch-initiative/dismech",
    ref: str = "bot/work",
    sha: str = "a" * 40,
    author: str = "dragon-ai-agent[bot]",
    association: str = "NONE",
) -> dict:
    return {
        "number": number,
        "head": {
            "repo": {"full_name": repo},
            "ref": ref,
            "sha": sha,
        },
        "user": {"login": author},
        "author_association": association,
    }


def _workflow() -> tuple[dict, str]:
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    return yaml.safe_load(text), text


def _observation(number: int, head: str, rollup: list[dict] | None = None) -> dict:
    return {
        "number": number,
        "title": "title",
        "body": "body",
        "url": f"https://example.test/pull/{number}",
        "isDraft": False,
        "createdAt": "2026-01-01T00:00:00Z",
        "updatedAt": "2026-01-01T00:00:00Z",
        "baseRefName": "main",
        "baseRefOid": "f" * 40,
        "headRefName": "bot/work",
        "headRefOid": head,
        "isCrossRepository": False,
        "mergeStateStatus": "CLEAN",
        "mergeable": "MERGEABLE",
        "reviewDecision": "APPROVED",
        "statusCheckRollup": rollup or [],
        "labels": [],
        "reviews": [],
        "latestReviews": [],
        "comments": [],
    }


def _runtime_initialization() -> dict:
    return {
        "type": "system",
        "subtype": "init",
        "tools": ["Glob", "Grep", "Read"],
        "permissionMode": "dontAsk",
        "mcp_servers": [],
        "slash_commands": [],
    }


def test_candidate_gate_accepts_only_same_repo_trusted_sources():
    pulls = [
        _pull(1),
        _pull(
            2,
            ref="claude/fix-review",
            author="trusted-human",
            association="MEMBER",
        ),
        _pull(3, repo="outsider/fork"),
        _pull(4, author="outsider"),
        _pull(5, ref="claude/injection", author="outsider"),
    ]

    candidates = observer.resolve_candidates(
        pulls,
        "monarch-initiative/dismech",
        None,
    )

    assert [candidate["number"] for candidate in candidates] == [1, 2]
    assert candidates[0]["trust_basis"] == "trusted_bot"
    assert candidates[1]["trust_basis"] == "trusted_collaborator_claude_branch"
    assert set(candidates[0]) == {
        "number",
        "head_sha",
        "head_repo",
        "head_ref",
        "author",
        "author_association",
        "trust_basis",
    }


def test_specific_candidate_fails_closed_when_not_trusted():
    with pytest.raises(observer.ObserverError, match="not an open trusted candidate"):
        observer.resolve_candidates(
            [_pull(8, author="outsider")],
            "monarch-initiative/dismech",
            8,
        )


def test_rollup_shape_and_exact_head_are_enforced():
    head = "b" * 40
    observer.validate_rollup(
        _observation(
            1,
            head,
            [
                {
                    "__typename": "CheckRun",
                    "name": "test",
                    "status": "COMPLETED",
                    "conclusion": "SUCCESS",
                },
                {
                    "__typename": "StatusContext",
                    "context": "legacy-ci",
                    "state": "SUCCESS",
                },
            ],
        ),
        head,
    )

    with pytest.raises(observer.ObserverError, match="head changed"):
        observer.validate_rollup(_observation(1, "c" * 40), head)
    with pytest.raises(observer.ObserverError, match="invalid shape"):
        observer.validate_rollup(
            _observation(
                1,
                head,
                [
                    {
                        "__typename": "CheckRun",
                        "name": "test",
                        "status": "COMPLETED",
                        "conclusion": None,
                    }
                ],
            ),
            head,
        )


def test_probe_enriches_snapshot_only_after_double_head_check(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
):
    repo = "monarch-initiative/dismech"
    pull = _pull(42)
    candidate = observer.candidate_from_pull(pull, repo)
    assert candidate is not None
    snapshot = tmp_path / "candidate-snapshot.json"
    snapshot.write_text(
        json.dumps({"repository": repo, "candidates": [candidate]}),
        encoding="utf-8",
    )
    observation = _observation(42, candidate["head_sha"])
    responses = iter(
        [
            pull,
            observation,
            {"total_count": 0, "check_runs": []},
            pull,
        ]
    )
    monkeypatch.setattr(observer, "_run_json", lambda _args: next(responses))

    observer.probe(repo, snapshot)

    document = json.loads(snapshot.read_text(encoding="utf-8"))
    assert document["candidates"][0]["observation"] == observation


def test_probe_rejects_a_head_race(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
):
    repo = "monarch-initiative/dismech"
    pull = _pull(42)
    candidate = observer.candidate_from_pull(pull, repo)
    assert candidate is not None
    snapshot = tmp_path / "candidate-snapshot.json"
    snapshot.write_text(
        json.dumps({"repository": repo, "candidates": [candidate]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        observer,
        "_run_json",
        lambda _args: _pull(42, sha="d" * 40),
    )

    with pytest.raises(observer.ObserverError, match="changed before"):
        observer.probe(repo, snapshot)


def test_runtime_boundary_accepts_exact_pinned_action_initialization(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
):
    execution_file = tmp_path / "claude-execution-output.json"
    execution_file.write_text(
        json.dumps(
            [
                _runtime_initialization(),
                {"type": "result", "subtype": "success", "is_error": False},
            ]
        ),
        encoding="utf-8",
    )

    observer.verify_runtime_boundary(execution_file, tmp_path)

    assert "tools=Glob,Grep,Read" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("tools", ["Bash", "Glob", "Grep", "Read"], "unexpected tool set"),
        ("tools", ["Glob", "Grep"], "unexpected tool set"),
        ("permissionMode", "bypassPermissions", "unexpected permission mode"),
        (
            "mcp_servers",
            [{"name": "github", "status": "connected"}],
            "exposed an MCP server",
        ),
        ("slash_commands", ["review"], "exposed a slash command"),
    ],
)
def test_runtime_boundary_fails_closed_on_capability_drift(
    tmp_path: Path,
    field: str,
    value: object,
    message: str,
):
    initialization = _runtime_initialization()
    initialization[field] = value
    execution_file = tmp_path / "claude-execution-output.json"
    execution_file.write_text(json.dumps([initialization]), encoding="utf-8")

    with pytest.raises(observer.ObserverError, match=message):
        observer.verify_runtime_boundary(execution_file, tmp_path)


def test_runtime_boundary_rejects_execution_file_outside_runner_temp(
    tmp_path: Path,
):
    runner_temp = tmp_path / "runner"
    runner_temp.mkdir()
    execution_file = tmp_path / "claude-execution-output.json"
    execution_file.write_text(
        json.dumps([_runtime_initialization()]),
        encoding="utf-8",
    )

    with pytest.raises(observer.ObserverError, match="outside RUNNER_TEMP"):
        observer.verify_runtime_boundary(execution_file, runner_temp)


def test_workflow_has_read_only_permissions_and_no_write_secret():
    workflow, text = _workflow()

    assert workflow["permissions"] == {
        "actions": "read",
        "checks": "read",
        "contents": "read",
        "issues": "read",
        "pull-requests": "read",
    }
    assert "create-github-app-token" not in text
    assert "AI4C_AGENT" not in text
    assert "PAT_FOR_PR" not in text
    assert "gh auth setup-git" not in text
    assert set(re.findall(r"secrets\.([A-Z0-9_]+)", text)) == {
        "CLAUDE_CODE_OAUTH_TOKEN",
        "GITHUB_TOKEN",
    }


def test_model_step_is_pinned_and_observer_only():
    workflow, _text = _workflow()
    steps = workflow["jobs"]["shepherd"]["steps"]
    model_step = next(step for step in steps if step["name"] == "Run PR Shepherd")

    assert model_step["uses"] == f"anthropics/claude-code-action@{ACTION_SHA}"
    assert model_step["with"]["github_token"] == "${{ secrets.GITHUB_TOKEN }}"
    assert "env" not in model_step

    args = model_step["with"]["claude_args"]
    assert "--permission-mode dontAsk" in args
    assert '--allowedTools "Read,Glob,Grep"' in args
    assert '--tools "Read,Glob,Grep"' in args
    assert "--setting-sources user" in args
    assert "--disable-slash-commands" in args
    assert "dangerously-skip-permissions" not in args
    for forbidden in ("Bash", "Edit", "Write", "WebFetch", "WebSearch", "mcp"):
        assert forbidden not in args

    prompt = model_step["with"]["prompt"]
    assert "observer-only" in prompt
    assert "Never claim\nan action was performed" in prompt
    assert "CANDIDATE_SNAPSHOT" in prompt


def test_candidate_snapshot_and_probe_precede_model():
    workflow, text = _workflow()
    steps = workflow["jobs"]["shepherd"]["steps"]
    names = [step["name"] for step in steps]

    assert (
        names.index("Resolve trusted candidate PRs")
        < names.index("Probe exact-head check rollups")
        < names.index("Run PR Shepherd")
    )
    assert "pr-shepherd-input" in text
    assert "candidate-snapshot.json" in text
    assert "statusCheckRollup" in OBSERVER_PATH.read_text(encoding="utf-8")
    assert "check-runs?per_page=1" in OBSERVER_PATH.read_text(encoding="utf-8")


def test_runtime_boundary_verification_runs_after_model_even_on_failure():
    workflow, _text = _workflow()
    steps = workflow["jobs"]["shepherd"]["steps"]
    names = [step["name"] for step in steps]
    boundary = next(
        step for step in steps if step["name"] == "Verify observer runtime boundary"
    )

    assert (
        names.index("Run PR Shepherd")
        < names.index("Verify observer runtime boundary")
        < names.index("Write step summary")
    )
    assert "always()" in boundary["if"]
    assert boundary["env"]["EXECUTION_FILE"] == (
        "${{ steps.pr-shepherd.outputs.execution_file }}"
    )
    assert "verify-runtime" in boundary["run"]


def test_summary_escapes_execution_file_result():
    workflow, _text = _workflow()
    steps = workflow["jobs"]["shepherd"]["steps"]
    summary = next(step for step in steps if step["name"] == "Write step summary")
    script = summary["run"]

    assert "EXECUTION_FILE" in summary["env"]
    assert "resolved.relative_to(runner_temp)" in script
    assert "escape(str(result), quote=True)" in script
    assert "<pre>" in script
