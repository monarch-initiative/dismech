"""Wiring guards for the PR-shepherd workflow policy boundary."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SHEPHERD = ROOT / ".github" / "workflows" / "pr-shepherd.yml"
COMPLIANCE = ROOT / ".github" / "workflows" / "auto-merge-compliance.yml"
CRON_PROFILES = ROOT / ".github" / "cron-profiles.yaml"
CONTROLLER_ONLY_CRON = "37 1-3,5-7,9-11,13-15,17-19,21-23 * * *"


def workflow(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def step(job: dict, name: str) -> dict:
    return next(item for item in job["steps"] if item.get("name") == name)


def action_uses(job: dict) -> set[str]:
    return {str(item["uses"]) for item in job["steps"] if "uses" in item}


def test_merge_controller_has_a_fresh_trusted_runner_and_scoped_writer():
    data = workflow(SHEPHERD)
    jobs = data["jobs"]
    assert {"shepherd", "merge-ready"} <= jobs.keys()
    agent_job = jobs["shepherd"]
    merge_job = jobs["merge-ready"]

    assert any(
        value.startswith("anthropics/claude-code-action@")
        for value in action_uses(agent_job)
    )
    assert not any(
        value.startswith("anthropics/claude-code-action@")
        for value in action_uses(merge_job)
    )

    checkout = step(merge_job, "Checkout trusted default branch")
    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert checkout["with"]["token"] == "${{ github.token }}"
    assert checkout["with"]["persist-credentials"] is False

    token = step(merge_job, "Generate scoped merge token")
    assert token["with"]["permission-contents"] == "write"
    assert token["with"]["permission-pull-requests"] == "write"
    controller = step(merge_job, "Merge at most one ready PR (deterministic)")
    assert controller["env"]["GH_TOKEN"] == "${{ github.token }}"
    assert controller["env"]["GH_MERGE_TOKEN"] == (
        "${{ steps.ai4c-token-merge.outputs.token }}"
    )
    assert "scripts/auto_merge_ready_prs.py" in controller["run"]
    assert '--base-health-check "test (3.13)"' in controller["run"]
    assert '--base-health-app-id "15368"' in controller["run"]
    assert 'args+=(--specific-pr "$SPECIFIC_PR")' in controller["run"]
    assert merge_job["env"]["SPECIFIC_PR"] == "${{ inputs.pr_number || '' }}"
    assert "python scripts/auto_merge_ready_prs.py" in controller["run"]
    assert "uv run" not in controller["run"]
    setup_python = step(merge_job, "Set up Python")
    assert setup_python["with"]["python-version"] == "3.12"
    assert merge_job["steps"].index(setup_python) < merge_job["steps"].index(token)
    assert agent_job["concurrency"]["group"] != merge_job["concurrency"]["group"]


def test_agent_token_is_scoped_and_cannot_outlive_the_job():
    job = workflow(SHEPHERD)["jobs"]["shepherd"]
    assert job["timeout-minutes"] == 55
    assert set(job["permissions"].values()) == {"read"}
    token = step(job, "Generate ai4c-agent token")
    assert {
        key: token["with"][key]
        for key in token["with"]
        if str(key).startswith("permission-")
    } == {
        "permission-actions": "write",
        "permission-checks": "read",
        "permission-contents": "write",
        "permission-issues": "write",
        "permission-pull-requests": "write",
    }


def test_active_cron_profile_matches_workflow_and_preserves_the_lane_split():
    data = workflow(SHEPHERD)
    schedules = {item["cron"] for item in data[True]["schedule"]}
    profiles = workflow(CRON_PROFILES)
    active = profiles["active"]
    configured = {
        item["cron"]
        for item in profiles["profiles"][active]["workflows"]["pr-shepherd"]
    }
    assert schedules == configured
    assert "37 */4 * * *" in schedules
    assert CONTROLLER_ONLY_CRON in schedules
    agent_condition = data["jobs"]["shepherd"]["if"]
    assert CONTROLLER_ONLY_CRON in agent_condition
    assert "!=" in agent_condition

    for name, profile in profiles["profiles"].items():
        crons = {item["cron"] for item in profile["workflows"]["pr-shepherd"]}
        if name == "off":
            assert crons == set()
        elif name == "slow":
            assert crons == {"37 */4 * * *", CONTROLLER_ONLY_CRON}
        else:
            assert crons == {"37 * * * *"}


def test_agent_lane_uses_a_bounded_deterministic_shortlist():
    job = workflow(SHEPHERD)["jobs"]["shepherd"]
    selection = step(job, "Select agent-tendable PRs (deterministic)")
    assert "scripts/pr_shepherd_policy.py" in selection["run"]
    assert '--limit "$((MAX_PRS * 3))"' in selection["run"]
    agent = step(job, "Run PR Shepherd")
    prompt = agent["with"]["prompt"]
    assert "CANDIDATE_PRS: ${{ steps.pr-candidates.outputs.pr_numbers }}" in prompt
    assert "merge_base_commit.sha == $MAIN_SHA" in prompt
    assert "baseRefOid" in prompt and "NOT an ancestry signal" in prompt
    assert "APPROVED + ALIGNED + RED/BLOCKED" in prompt
    assert "Update at most ONE behind branch per run" in prompt
    assert "Never merge a PR, enable auto-merge" in prompt
    assert "Squash merge it directly" not in prompt


def test_compliance_lane_only_classifies_for_the_common_controller():
    data = workflow(COMPLIANCE)
    # PyYAML 1.1 parses the unquoted workflow key `on` as boolean true.
    triggers = data[True]["pull_request_target"]["types"]
    assert "ready_for_review" not in triggers
    assert data["permissions"]["pull-requests"] == "read"
    job = data["jobs"]["prepare-pr"]
    eligibility = step(job, "Check PR eligibility")
    assert "scripts/pr_shepherd_policy.py compliance" in eligibility["run"]
    serialized = COMPLIANCE.read_text(encoding="utf-8")
    assert "gh pr ready" not in serialized
    assert "gh pr merge" not in serialized


def test_scanner_no_longer_uses_draft_as_a_lifecycle_signal():
    text = (ROOT / ".github/workflows/curation-scanner.yml").read_text(encoding="utf-8")
    assert "Prefer draft PRs" not in text
    assert "Draft status is not a lifecycle signal" in text


def test_workflow_policy_changes_run_the_python_test_job():
    text = (ROOT / ".github/workflows/main.yaml").read_text(encoding="utf-8")
    for path in (
        ".github/cron-profiles.yaml",
        ".github/workflows/auto-merge-compliance.yml",
        ".github/workflows/curation-scanner.yml",
        ".github/workflows/main.yaml",
        ".github/workflows/pr-shepherd.yml",
        "scripts/auto_merge_ready_prs.py",
        "scripts/pr_shepherd_policy.py",
    ):
        assert f"- '{path}'" in text
