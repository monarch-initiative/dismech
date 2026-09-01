"""Wiring guards for merge-queue (`merge_group`) support in the CI workflow.

A merge queue tests each PR on a temporary branch and waits for the required
``test (3.13)`` check there (#10168). Two silent failure modes are guarded:

1. The workflow not declaring the ``merge_group`` trigger at all — the check is
   never reported and every queued PR times out.
2. The dorny/paths-filter gates suppressing steps on a merge-group ref — the
   filter cannot auto-detect its comparison point for that event, so an
   ungated filter would return no matches and ``test (3.13)`` would report
   green having run almost nothing. Merge-group runs must run the full suite;
   path filtering is why the #9538 cross-file enum break was invisible until
   the branch was updated.

Two steps are deliberately exempt from the full-suite rule because they consume
the filter's changed-file *lists*, which do not exist when the filter is
skipped. They are content-local (the PR's own files, already validated by the
PR's required run), and the exemption is pinned here so it cannot silently
grow.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / ".github" / "workflows" / "main.yaml"

MERGE_GROUP_FIRES = "github.event_name == 'merge_group'"

# Steps allowed to stay skipped on merge_group despite a paths-filter gate.
# Every entry must consume a `*_files` output — that dependency is what makes
# forcing the gate impossible (empty argument list) and the skip sound (the
# check is content-local to files the PR itself carries).
FILE_LIST_EXEMPT_STEPS = {
    "Validate changed disorder KB files",
    "Validate changed comorbidity KB files",
}


def load_workflow() -> dict:
    return yaml.safe_load(MAIN.read_text(encoding="utf-8"))


def test_steps() -> list[dict]:
    return load_workflow()["jobs"]["test"]["steps"]


def test_main_workflow_declares_merge_group_trigger():
    # `on:` parses as the YAML 1.1 boolean True under safe_load.
    triggers = load_workflow()[True]
    assert "merge_group" in triggers


def test_paths_filter_is_skipped_on_merge_group():
    filter_step = next(
        step for step in test_steps() if step.get("id") == "changes"
    )
    assert filter_step["if"] == "github.event_name != 'merge_group'"


def test_no_paths_filter_gate_can_suppress_a_step_on_merge_group():
    for step in test_steps():
        condition = str(step.get("if", ""))
        if "steps.changes.outputs." not in condition:
            continue
        name = step.get("name", "<unnamed>")
        if name in FILE_LIST_EXEMPT_STEPS:
            run = str(step.get("run", ""))
            assert "_files }}" in run, (
                f"{name!r} is exempt from the merge-group full-suite rule but "
                "no longer consumes a paths-filter file list; wire it to "
                f"fire on merge_group and drop it from FILE_LIST_EXEMPT_STEPS"
            )
            continue
        assert MERGE_GROUP_FIRES in condition, (
            f"step {name!r} is gated on paths-filter outputs but would skip "
            "on a merge_group event, silently weakening the merge queue's "
            f"required check; add `{MERGE_GROUP_FIRES} ||` to its condition"
        )


def test_pr_only_steps_stay_guarded_by_event_name():
    # Steps that read github.event.pull_request.number would fail (or worse,
    # act on nothing) on merge_group/push events; they must pin the event.
    for step in test_steps():
        uses_pr_number = "github.event.pull_request.number" in str(
            step.get("run", "")
        )
        if not uses_pr_number:
            continue
        assert step.get("if") == "github.event_name == 'pull_request'", (
            f"step {step.get('name', '<unnamed>')!r} reads the PR number but "
            "is not guarded with github.event_name == 'pull_request'"
        )
