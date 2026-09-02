"""Wiring guards for the mention-driven agent workflow (dragon-ai.yml).

The summon handles live in one place, ``.github/scripts/agent-mention.js``,
and both the workflow's mention check and the comment trust gate read them from
there. A handle spelled out again inside the workflow is how the ``@ai4c-agent``
alias was missed the first time: PR #6979 switched the responder's identity to
the ai4c-agent App but left the trigger regex on the retired handle, so
``@ai4c-agent please ...`` was silently ignored.
"""

import json
import re
import subprocess
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


NODE_DRIVER = """
const fs = require('fs');
const path = require('path');
const body = fs.readFileSync(process.argv[2], 'utf8');
const missing = process.argv[3] === 'missing';

// Stand in for github-script's `require`: relative ids resolve against the
// workspace. Simulate the parser being absent from the trusted checkout the
// way Node does, with MODULE_NOT_FOUND.
const fakeRequire = (id) => {
  if (id.includes('agent-mention')) {
    if (missing) {
      const err = new Error(`Cannot find module '${id}'`);
      err.code = 'MODULE_NOT_FOUND';
      throw err;
    }
    return require(path.join(process.cwd(), '.github/scripts/agent-mention.js'));
  }
  if (id === 'fs') {
    return missing
      ? {...fs, existsSync: (p) => (String(p).includes('agent-mention') ? false : fs.existsSync(p))}
      : fs;
  }
  return require(id);
};

const context = {
  eventName: 'issue_comment',
  payload: {
    comment: {body: process.argv[4], user: {login: 'cmungall'}},
    issue: {number: 10556},
  },
};
const core = {warning: (m) => process.stderr.write('WARNING: ' + m + '\\n')};
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const run = new AsyncFunction('require', 'context', 'core', 'console', body);

run(fakeRequire, context, core, {log: () => {}}).then(
  (result) => process.stdout.write(JSON.stringify(result)),
  (err) => {
    process.stdout.write(JSON.stringify({threw: String(err && err.message)}));
  },
);
"""


def _run_check_script(
    tmp_path, mode: str, body: str = "@ai4c-agent please fix it"
) -> dict:
    """Execute the workflow's inline mention-check script under node."""
    check = _step(_workflow()["jobs"]["check-mention"], "Check for qualifying mention")
    script = tmp_path / "check.js"
    script.write_text(check["with"]["script"], encoding="utf-8")
    driver = tmp_path / "driver.js"
    driver.write_text(NODE_DRIVER, encoding="utf-8")

    proc = subprocess.run(
        ["node", str(driver), str(script), mode, body],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    result = json.loads(proc.stdout)
    result["_warnings"] = proc.stderr
    return result


def test_check_script_dispatches_on_the_canonical_handle(tmp_path):
    result = _run_check_script(tmp_path, "present")

    assert result["qualifiedMention"] is True
    assert result["prompt"] == "fix it"
    assert result["handle"] == "ai4c-agent"


def test_check_script_declines_when_trusted_ref_predates_the_parser(tmp_path):
    """The allowlist, and so the parser beside it, is read from the default
    branch on purpose: reading either from the PR ref would let a proposer's
    branch rewrite who counts as authorized, or rewrite an authorized user's
    comment into an attacker-chosen prompt. The cost is that a default branch
    predating the parser has no parser to load. Decline that event loudly
    instead of crashing the job on every comment in the repository.
    """
    result = _run_check_script(tmp_path, "missing")

    assert "threw" not in result, f"check script crashed: {result.get('threw')}"
    assert result["qualifiedMention"] is False


def test_request_is_delimited_by_a_marker_the_request_cannot_predict():
    """The request is controller-supplied text that may legitimately contain a
    code fence, now that the parser keeps fenced blocks in the prompt. A fixed
    ``` wrapper can be closed from inside such a request, letting its tail read
    as instructions rather than as quoted request text. Delimit with a value
    generated at run time instead.
    """
    prompt = _step(
        _workflow()["jobs"]["respond-to-mention"], "Create structured Claude prompt"
    )
    run = prompt["run"]

    assert "openssl rand" in run, "delimiter must be generated at run time"

    # Check the emitted prompt, not the surrounding script: a comment explaining
    # this rule may legitimately mention a backtick fence.
    body = run.split("<< EOL\n", 1)[1].split("\nEOL", 1)[0]
    # Fences are backslash-escaped inside the heredoc, so compare unescaped.
    assert "```" not in body.replace("\\", ""), (
        "request must not be wrapped in a fixed backtick fence"
    )
    lines = [line.strip() for line in body.splitlines()]
    request = lines.index("$(cat /tmp/claude-input/prompt.txt)")
    assert lines[request - 1] == "${DELIM}", "no opening marker before the request"
    assert lines[request + 1] == "${DELIM}", "no closing marker after the request"


# Sites that legitimately document every handle, current and retired: the module
# that defines them, and the workflow whose trigger comment explains both.
LEGACY_HANDLE_ALLOWED = {
    ".github/scripts/agent-mention.js",
    ".github/workflows/dragon-ai.yml",
}


def _handles() -> tuple[str, list[str]]:
    """Read the canonical and legacy handles out of the shared module."""
    source = MENTION_MODULE.read_text(encoding="utf-8")
    canonical = re.search(r'AGENT_MENTION = "([^"]+)"', source).group(1)
    legacy = re.findall(
        r'"([^"]+)"',
        re.search(r"LEGACY_AGENT_MENTIONS = \[([^\]]*)\]", source).group(1),
    )
    return canonical, legacy


def test_no_workflow_emits_a_retired_handle():
    """A summon phrase written into a prompt must name the current handle.

    The prompt in claude-issue-summarize-action is the only place in the repo
    that *generates* a summon rather than documenting one, and it still named
    the retired handle. It could not be caught by a dragon-ai.yml-scoped check,
    so this one is repo-wide. Spelling the canonical handle out in a prompt is
    unavoidable and allowed; spelling out a retired one is the bug.
    """
    canonical, legacy = _handles()
    assert legacy, "expected at least one retired handle to guard against"

    offenders = []
    for directory in ("workflows", "actions"):
        for path in (ROOT / ".github" / directory).rglob("*.y*ml"):
            rel = path.relative_to(ROOT).as_posix()
            if rel in LEGACY_HANDLE_ALLOWED:
                continue
            for number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                # Prose telling an agent *not* to use a phrase is the opposite
                # of the defect, and must keep naming the alias it forbids.
                if any(w in line.lower() for w in ("do not", "don't", "never")):
                    continue
                for handle in legacy:
                    if f"@{handle} please" in line:
                        offenders.append(f"{rel}:{number}")

    assert not offenders, (
        f"retired handle used to summon the agent; use @{canonical}: "
        + ", ".join(offenders)
    )


def test_check_script_warns_when_an_authorized_mention_did_not_parse(tmp_path):
    """Naming the agent and getting nothing is the failure this PR fixes.

    A mention with no `please`, or one masked by a stray backtick, is a correct
    refusal. Doing it silently is not: that is how the retired handle survived
    for weeks. The job should leave a visible annotation.
    """
    result = _run_check_script(tmp_path, "present", "cc @ai4c-agent for visibility")

    assert result["qualifiedMention"] is False
    assert "no request was parsed" in result["_warnings"]


def test_check_script_stays_quiet_when_nobody_named_the_agent(tmp_path):
    result = _run_check_script(tmp_path, "present", "just an ordinary comment")

    assert result["qualifiedMention"] is False
    assert result["_warnings"].strip() == ""
