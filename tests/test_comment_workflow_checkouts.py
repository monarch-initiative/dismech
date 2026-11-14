"""The per-comment workflow jobs check out only ``.github/`` (#17150).

``check-mention`` (dragon-ai.yml) and ``guard-comment``
(untrusted-comment-guard.yml) start on every issue, PR, comment and review
comment. Each reads a few files under ``.github/`` and decides in under a
second. Before these checkouts were made sparse, each job did a full checkout
of this repository that took about 3.7 minutes, which at ~1,500 runs a day
held org-wide runner slots for ~98 hours a day.

A sparse checkout is only safe while everything those jobs read lives under
``.github/``. These tests pin both halves: the checkout stays sparse, and the
inline scripts and the modules they load reach for nothing outside it. The
agent job's own checkout is the working tree it edits, so it must stay full.
"""

import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SCRIPTS = ROOT / ".github" / "scripts"

# (workflow file, job id) for every job that runs on every comment event.
PER_COMMENT_JOBS = [
    ("dragon-ai.yml", "check-mention"),
    ("untrusted-comment-guard.yml", "guard-comment"),
]

# Repository-relative paths a script opens: require('./x'), readFileSync('x'),
# existsSync('x'), and string constants naming a ./ or .github/ path.
_PATH_LITERAL = re.compile(r"""['"](\./[^'"]+|\.github/[^'"]+)['"]""")


def _job(workflow: str, job_id: str) -> dict:
    data = yaml.safe_load((WORKFLOWS / workflow).read_text(encoding="utf-8"))
    return data["jobs"][job_id]


def _checkout_steps(job: dict) -> list[dict]:
    return [
        step
        for step in job["steps"]
        if str(step.get("uses", "")).startswith("actions/checkout@")
    ]


@pytest.mark.parametrize(("workflow", "job_id"), PER_COMMENT_JOBS)
def test_per_comment_job_checks_out_only_dot_github(workflow, job_id):
    checkouts = _checkout_steps(_job(workflow, job_id))

    assert checkouts, f"{workflow}:{job_id} has no checkout step"
    for step in checkouts:
        assert step.get("with", {}).get("sparse-checkout") == ".github", (
            f"{workflow}:{job_id} checks out the whole repository on every "
            "comment; keep `sparse-checkout: .github` (#17150)"
        )


def test_mention_check_keeps_its_trusted_ref_and_no_credentials():
    (checkout,) = _checkout_steps(_job("dragon-ai.yml", "check-mention"))

    assert checkout["with"]["ref"] == "${{ github.event.repository.default_branch }}"
    assert checkout["with"]["persist-credentials"] is False


def test_agent_job_checkout_stays_full():
    for step in _checkout_steps(_job("dragon-ai.yml", "respond-to-mention")):
        assert "sparse-checkout" not in step.get("with", {}), (
            "the agent edits the working tree, so its checkout must be complete"
        )


def _paths_read_by(text: str) -> set[str]:
    return set(_PATH_LITERAL.findall(text))


@pytest.mark.parametrize(("workflow", "job_id"), PER_COMMENT_JOBS)
def test_per_comment_job_reads_nothing_outside_dot_github(workflow, job_id):
    job = _job(workflow, job_id)
    scripts = [
        step["with"]["script"]
        for step in job["steps"]
        if str(step.get("uses", "")).startswith("actions/github-script@")
    ]
    assert scripts, f"{workflow}:{job_id} has no github-script step"

    # Walk the inline scripts, then every local module they (transitively) load.
    seen: set[Path] = set()
    pending = [(text, ROOT) for text in scripts]
    while pending:
        text, base = pending.pop()
        for literal in _paths_read_by(text):
            # A ./ path is module-relative for require(); a .github/ path is
            # opened relative to the job's working directory, the repo root.
            anchor = ROOT if literal.startswith(".github/") else base
            target = (anchor / literal).resolve()
            assert target.is_relative_to(ROOT / ".github"), (
                f"{workflow}:{job_id} reads {literal}, outside .github/, which the "
                "sparse checkout does not contain"
            )
            if target.suffix == ".js" and target.is_file() and target not in seen:
                seen.add(target)
                pending.append((target.read_text(encoding="utf-8"), target.parent))


# --- Job-level pre-filters (#17150, follow-ups to #17312) ------------------
#
# A job-level `if:` is evaluated before GitHub assigns a runner, so a skipped
# job never waits in the shared org-wide queue. Each filter must only ever skip
# events the job's own script would have declined; these tests pin that.

MENTION_MODULE = SCRIPTS / "agent-mention.js"
TRUST_GATE = SCRIPTS / "github-trust-gate.js"


def _module_handles() -> set[str]:
    source = MENTION_MODULE.read_text(encoding="utf-8")
    canonical = re.search(r'AGENT_MENTION = "([^"]+)"', source).group(1)
    legacy = re.findall(
        r'"([^"]+)"',
        re.search(r"LEGACY_AGENT_MENTIONS = \[([^\]]*)\]", source).group(1),
    )
    return {canonical, *legacy}


def test_mention_prefilter_names_exactly_the_module_handles():
    """The `if:` repeats the handles, so it must track agent-mention.js.

    A handle added to the module but not to the `if:` would be silently
    skipped before the parser ever saw it -- the same failure as the
    retired-handle bug the module exists to prevent.
    """
    condition = _job("dragon-ai.yml", "check-mention")["if"]
    in_filter = set(re.findall(r"'@([^']+)'", condition))

    assert in_filter == _module_handles()


def test_mention_prefilter_reads_every_event_body():
    condition = _job("dragon-ai.yml", "check-mention")["if"]
    # The comment body must come first: a comment event's payload also
    # carries the parent issue or PR, whose body is not what was just posted.
    expected = (
        "github.event.comment.body || github.event.issue.body"
        " || github.event.pull_request.body"
    )
    for handle in _module_handles():
        assert f"contains({expected}, '@{handle}')" in condition


def test_agent_job_still_depends_on_the_mention_check():
    """If check-mention is skipped, respond-to-mention must be skipped too."""
    job = _job("dragon-ai.yml", "respond-to-mention")
    assert job["needs"] == "check-mention"
    assert "always()" not in job["if"]


def test_guard_skips_only_logins_the_trust_gate_already_trusts():
    condition = _job("untrusted-comment-guard.yml", "guard-comment")["if"]
    assert condition == "${{ !endsWith(github.event.comment.user.login, '[bot]') }}"
    assert "author_association" not in condition

    # The skip is only safe while the gate trusts every `[bot]` login.
    gate = TRUST_GATE.read_text(encoding="utf-8")
    assert 'normalized.endsWith("[bot]")' in gate
