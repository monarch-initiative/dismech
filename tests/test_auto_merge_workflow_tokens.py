"""Credential guards for the separately managed ``auto/`` PR lanes."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"
APPROVAL_ACTION = ROOT / ".github" / "actions" / "approve-regen-pr" / "action.yml"
REVIEW_WORKFLOW = WORKFLOW_DIR / "claude-code-review.yml"
AUTO_MERGE_WORKFLOWS = {
    "generate-grouping-pages.yaml",
    "generate-pages.yaml",
    "generate-project-pages.yaml",
    "reference-title-baseline.yaml",
    "title-snippet-baseline.yaml",
    "warm-reference-cache.yaml",
}
STALE_CLEANUP_WORKFLOWS = {
    "generate-grouping-pages.yaml",
    "generate-pages.yaml",
    "generate-project-pages.yaml",
}
APP_TOKEN_ACTION = (
    "actions/create-github-app-token@d72941d797fd3113feb6b93fd0dec494b13a2547"
)


def _workflow(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _steps(data: dict) -> list[dict]:
    return [step for job in data["jobs"].values() for step in job["steps"]]


def test_all_server_side_auto_merge_lanes_use_the_ai4c_agent_token():
    discovered = {
        path.name
        for path in WORKFLOW_DIR.glob("*.y*ml")
        if "gh pr merge" in (text := path.read_text(encoding="utf-8"))
        and "--auto" in text
    }
    assert discovered == AUTO_MERGE_WORKFLOWS

    for name in sorted(AUTO_MERGE_WORKFLOWS):
        data = _workflow(WORKFLOW_DIR / name)
        job = next(iter(data["jobs"].values()))
        assert job["permissions"] == {
            "contents": "read",
            "pull-requests": "write" if name in STALE_CLEANUP_WORKFLOWS else "read",
        }
        steps = _steps(data)
        checkout = next(
            step for step in steps if step.get("name") == "Checkout repository"
        )
        assert checkout["with"]["persist-credentials"] is False

        token = next(step for step in steps if step.get("id") == "auto-merge-token")
        assert token["uses"] == APP_TOKEN_ACTION
        assert token["with"] == {
            "app-id": "${{ secrets.AI4C_AGENT_APP_ID }}",
            "private-key": "${{ secrets.AI4C_AGENT_PRIVATE_KEY }}",
            "permission-contents": "write",
            "permission-pull-requests": "write",
        }

        arming_step = next(
            step
            for step in steps
            if "gh pr merge" in step.get("run", "") and "--auto" in step.get("run", "")
        )
        assert arming_step["env"] == {
            "GH_TOKEN": "${{ steps.auto-merge-token.outputs.token }}"
        }
        run = arming_step["run"]
        assert "secrets.GITHUB_TOKEN" not in run
        assert "AUTO_MERGE_TOKEN" not in run
        assert run.count("gh pr merge") == 2
        assert run.count("gh pr view") == 1
        assert run.count("gh pr create") == 1
        assert run.count("git push") == 1
        assert run.count('enable_auto_merge "$') == 2
        assert "app/github-actions" in run
        assert "app/ai4c-agent" in run
        assert run.index("gh auth setup-git") < run.index("git push")
        assert run.index("git push") < run.index("gh pr create")
        assert run.count("--disable-auto") == 1
        assert run.index("autoMergeRequest") < run.index("--disable-auto")
        assert run.index("--disable-auto") < run.rindex("--auto")
        assert steps.index(checkout) < steps.index(token)
        assert steps.index(token) < steps.index(arming_step)


def test_approval_and_review_guards_accept_only_the_two_regen_bot_identities():
    approval = yaml.safe_load(APPROVAL_ACTION.read_text(encoding="utf-8"))
    approval_run = next(
        step["run"] for step in approval["runs"]["steps"] if "run" in step
    )
    assert "--json number,headRefOid,author" in approval_run
    assert "app/github-actions" in approval_run
    assert "app/ai4c-agent" in approval_run
    assert '--author "app/github-actions"' not in approval_run
    assert 'if [ "$pr_head" != "$head_sha" ]' in approval_run
    assert "pulls/$pr_number/reviews" in approval_run
    assert "--field event=APPROVE" in approval_run
    assert '--field commit_id="$head_sha"' in approval_run
    assert "gh pr review" not in approval_run

    review = _workflow(REVIEW_WORKFLOW)
    dispatch_run = review["jobs"]["dispatch-guard"]["steps"][0]["run"]
    for login in (
        "app/github-actions",
        "github-actions[bot]",
        "app/ai4c-agent",
        "ai4c-agent[bot]",
    ):
        assert login.replace("[", r"\[").replace("]", r"\]") in dispatch_run

    review_condition = review["jobs"]["claude-review"]["if"]
    assert "startsWith(github.event.pull_request.head.ref, 'auto/generate-')" in (
        review_condition
    )
    assert "github-actions[bot]" in review_condition
    assert "ai4c-agent[bot]" in review_condition


def test_auto_merge_workflow_edits_run_the_credential_guard():
    main_workflow = (WORKFLOW_DIR / "main.yaml").read_text(encoding="utf-8")
    guarded_paths = {
        *(f".github/workflows/{name}" for name in AUTO_MERGE_WORKFLOWS),
        ".github/actions/approve-regen-pr/action.yml",
        ".github/workflows/claude-code-review.yml",
    }
    for path in guarded_paths:
        assert f"- '{path}'" in main_workflow
