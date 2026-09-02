"""Wiring guards for the mention-driven agent workflow (dragon-ai.yml).

The summon handles live in one place, ``.github/scripts/agent-mention.js``,
and both the workflow's mention check and the comment trust gate read them from
there. A handle spelled out again inside the workflow is how the ``@ai4c-agent``
alias was missed the first time: PR #6979 switched the responder's identity to
the ai4c-agent App but left the trigger regex on the retired handle, so
``@ai4c-agent please ...`` was silently ignored.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "dragon-ai.yml"
MENTION_MODULE = ROOT / ".github" / "scripts" / "agent-mention.js"


def _step(job: dict, name: str) -> dict:
    return next(item for item in job["steps"] if item.get("name") == name)


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def test_mention_check_loads_the_shared_handle_module():
    check = _step(_workflow()["jobs"]["check-mention"], "Check for qualifying mention")
    script = check["with"]["script"]

    assert MENTION_MODULE.exists()
    assert "./.github/scripts/agent-mention.js" in script
    # No second copy of a handle: the module is the single source of truth.
    assert "@dragon-ai-agent" not in script
    assert "@ai4c-agent" not in script


def test_mention_check_still_reads_the_allowlist_from_the_default_branch():
    checkout = _step(
        _workflow()["jobs"]["check-mention"],
        "Checkout allowlist from the default branch",
    )

    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"


def test_respond_job_does_not_hardcode_the_agent_handle():
    prompt = _step(
        _workflow()["jobs"]["respond-to-mention"], "Create structured Claude prompt"
    )

    assert "You are @dragon-ai-agent" not in prompt["run"]
    assert "You are @ai4c-agent" not in prompt["run"]
