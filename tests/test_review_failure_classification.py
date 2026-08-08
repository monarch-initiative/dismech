"""Tests for the review workflow's agent-failure classifier (dismech#7731).

`claude-code-review.yml` ends with a "Verify the review agent actually ran"
step that reads the execution log and sorts a failed run into one of four
classes: max-turns, API-account billing, subscription usage limit, or generic.
Each class prints a different remedy, so a misclassification actively sends
debugging the wrong way.

That is not hypothetical. The live message ``You've hit your limit - resets
8pm (UTC)`` did not match the original ``"usage limit"``/``"weekly limit"``
markers, so a plain subscription cap was reported as "Common causes: an
invalid/retired --model, a bad token" and cost hours. Because the failure mode
IS wording drift, these tests extract the marker tuples from the workflow YAML
itself rather than restating them — a copy here would drift in exactly the way
the tests exist to catch.
"""

import ast
import re
from pathlib import Path

import pytest

from dismech.yaml_io import safe_load_path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = REPO_ROOT / ".github" / "workflows" / "claude-code-review.yml"


def _verify_step_source() -> str:
    """Return the embedded Python of the verify step, straight from the YAML."""
    workflow = safe_load_path(WORKFLOW)
    steps = workflow["jobs"]["claude-review"]["steps"]
    step = next(s for s in steps if s.get("name", "").startswith("Verify"))
    return step["run"].split("<<'PY'", 1)[1].rsplit("PY", 1)[0]


def _marker_tuple(name: str) -> tuple[str, ...]:
    """Evaluate a literal marker tuple defined in the verify step."""
    source = _verify_step_source()
    match = re.search(rf"^\s*{name} = (\(.*?\))", source, re.S | re.M)
    assert match, f"{name} not found in the verify step"
    return ast.literal_eval(match.group(1))


@pytest.fixture(scope="module")
def limit_markers() -> tuple[str, ...]:
    return _marker_tuple("LIMIT_MARKERS")


@pytest.fixture(scope="module")
def billing_markers() -> tuple[str, ...]:
    return _marker_tuple("BILLING_MARKERS")


def test_verify_step_python_is_valid():
    compile(_verify_step_source(), "verify-step", "exec")


@pytest.mark.parametrize(
    "message",
    [
        "You've hit your limit · resets 8pm (UTC)",  # the real dismech#7655 failure
        "Claude AI usage limit reached",
        "weekly limit exceeded for your account",
        "rate_limit",
        "rate_limit_error",
    ],
)
def test_subscription_cap_wordings_are_detected(message, limit_markers):
    assert any(m in message.lower() for m in limit_markers), (
        f"{message!r} would be reported as a generic agent error"
    )


@pytest.mark.parametrize(
    "message",
    [
        "model: claude-opus-4-6 does not exist",
        "aborted by user",
        "tool execution failed",
    ],
)
def test_unrelated_errors_are_not_misread_as_quota(
    message, limit_markers, billing_markers
):
    lowered = message.lower()
    assert not any(m in lowered for m in limit_markers + billing_markers)


@pytest.mark.parametrize(
    "message",
    [
        "Your credit balance is too low to run this request",
        "insufficient quota for this organization",
    ],
)
def test_billing_failures_are_classified_separately(
    message, billing_markers, limit_markers
):
    """Billing errors come from the API-key path and must not be reported as a
    subscription cap — the remedies are opposites (top up the account vs. set
    the API key / unstale the base branch)."""
    lowered = message.lower()
    assert any(m in lowered for m in billing_markers)
    assert not any(m in lowered for m in limit_markers)


def _branch_positions() -> dict[str, int]:
    """Offsets of the three guard statements, ignoring prose in comments.

    Keyed on code syntax (the assignment / the condition) rather than a bare
    name, since all three names are also discussed in the surrounding comments
    and a substring search would report a comment's position instead.
    """
    source = "\n".join(
        line
        for line in _verify_step_source().splitlines()
        if not line.lstrip().startswith("#")
    )
    positions = {
        "max_turns": source.find('subtype") == "error_max_turns"'),
        "billing": source.find("BILLING_MARKERS = ("),
        "limit": source.find("LIMIT_MARKERS = ("),
    }
    assert all(v >= 0 for v in positions.values()), positions
    return positions


def test_billing_branch_precedes_the_usage_limit_branch():
    """Order matters: the billing check must run first, or a message matching
    both tuples would emit the subscription-cap remedy."""
    pos = _branch_positions()
    assert pos["billing"] < pos["limit"]


def test_max_turns_is_checked_before_quota_markers():
    """`error_max_turns` is a workflow-budget bug, not a quota problem; a
    phrasing like "turn limit reached" would otherwise match LIMIT_MARKERS."""
    pos = _branch_positions()
    assert pos["max_turns"] < pos["limit"]
