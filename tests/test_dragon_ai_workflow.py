"""Wiring guards for the mention-driven agent workflow (dragon-ai.yml).

The summon handles live in one place, ``.github/scripts/agent-mention.js``,
and both the workflow's mention check and the comment trust gate read them from
there. A handle spelled out again inside the workflow is how the ``@ai4c-agent``
alias was missed the first time: PR #6979 switched the responder's identity to
the ai4c-agent App but left the trigger regex on the retired handle, so
``@ai4c-agent please ...`` was silently ignored.
"""

import json
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
    comment: {body: "@ai4c-agent please fix it", user: {login: 'cmungall'}},
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


def _run_check_script(tmp_path, mode: str) -> dict:
    """Execute the workflow's inline mention-check script under node."""
    check = _step(_workflow()["jobs"]["check-mention"], "Check for qualifying mention")
    script = tmp_path / "check.js"
    script.write_text(check["with"]["script"], encoding="utf-8")
    driver = tmp_path / "driver.js"
    driver.write_text(NODE_DRIVER, encoding="utf-8")

    proc = subprocess.run(
        ["node", str(driver), str(script), mode],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=True,
    )
    return json.loads(proc.stdout)


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
