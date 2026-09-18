"""Wiring guards for merge-queue (`merge_group`) support in the CI workflow.

A merge queue tests each PR on a temporary branch and waits for the required
``test (3.13)`` check there (#10168). The guarded invariants:

1. ``main.yaml`` declares the ``merge_group`` trigger — without it the check is
   never reported and every queued PR times out.
2. The dorny/paths-filter step runs on merge-group refs (supported since
   v4.0.1, where ``base``/``ref`` default to the event's commit hashes), so
   its ``*_files`` lists feed the changed-file KB validations in the merged
   context.
3. No ``steps.changes.outputs.*`` gate may suppress a step on ``merge_group``
   unless the step is one of the pinned file-scoped validations that consume a
   filter file list. Everything else runs the full suite in a queue build —
   path filtering is why the #9538 cross-file enum break was invisible until
   the branch was updated.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / ".github" / "workflows" / "main.yaml"

MERGE_GROUP_FIRES = "github.event_name == 'merge_group'"

# Steps allowed to stay purely filter-gated (no merge_group forcing): each
# consumes a `*_files` output, so its gate is meaningful on merge_group only
# because the filter itself runs there and populates the list. Every entry
# must actually interpolate a file list — asserted below — so this set cannot
# silently grow into a way of skipping suite steps on queue builds.
FILE_SCOPED_STEPS = {
    "Validate changed disorder KB files",
    "Validate changed comorbidity KB files",
}


def load_workflow() -> dict:
    return yaml.safe_load(MAIN.read_text(encoding="utf-8"))


def workflow_steps() -> list[dict]:
    return load_workflow()["jobs"]["test"]["steps"]


def paths_filter_step() -> dict:
    return next(step for step in workflow_steps() if step.get("id") == "changes")


def test_main_workflow_declares_merge_group_trigger():
    # `on:` parses as the YAML 1.1 boolean True under safe_load.
    triggers = load_workflow()[True]
    assert "merge_group" in triggers


def test_paths_filter_runs_on_merge_group():
    # The filter must not be event-gated: on merge_group it supplies the
    # changed-file lists the KB validations consume. Merge-queue support
    # requires dorny/paths-filter v4.0.1+, so pin the major version too.
    step = paths_filter_step()
    assert "if" not in step, (
        "the paths-filter step must run on every event; merge-group refs are "
        "supported since dorny/paths-filter v4.0.1"
    )
    action, _, version = str(step["uses"]).partition("@")
    assert action == "dorny/paths-filter"
    # Merge-group support landed in v4.0.1 exactly; v4.0.0 predates it, so a
    # bare major check is not a floor. Accept the moving major tags (v4, v5,
    # ...) or a full version >= 4.0.1; anything else (v4.0.0, a SHA pin, a
    # pre-v4 tag) must be re-vetted by hand.
    parts = version.lstrip("v").split(".")
    assert all(p.isdigit() for p in parts), (
        f"unrecognized paths-filter pin {version!r}; if pinning a SHA, "
        "confirm it postdates v4.0.1 (merge-group support) and update this "
        "guard"
    )
    numeric = tuple(int(p) for p in parts)
    is_moving_major_tag = len(numeric) == 1 and numeric[0] >= 4
    assert is_moving_major_tag or numeric >= (4, 0, 1), (
        "dorny/paths-filter below v4.0.1 has no merge_group case and diffs "
        "against the default branch instead, an over-broad result that can "
        "blame other PRs' changes on the queued PR"
    )


def test_no_paths_filter_gate_can_suppress_a_step_on_merge_group():
    for step in workflow_steps():
        condition = str(step.get("if", ""))
        if "steps.changes.outputs." not in condition:
            continue
        name = step.get("name", "<unnamed>")
        if name in FILE_SCOPED_STEPS:
            run = str(step.get("run", ""))
            assert "_files }}" in run, (
                f"{name!r} is pinned as file-scoped but no longer consumes a "
                "paths-filter file list; force it on merge_group and drop it "
                "from FILE_SCOPED_STEPS"
            )
            # The inverse guard: forcing a file-scoped step on merge_group
            # would run it with an empty argument list whenever the queue
            # build has no matching changes -- validating nothing while
            # reporting success.
            assert MERGE_GROUP_FIRES not in condition, (
                f"{name!r} consumes a paths-filter file list and must stay "
                "purely filter-gated, never forced on merge_group"
            )
            continue
        assert MERGE_GROUP_FIRES in condition, (
            f"step {name!r} is gated on paths-filter outputs without firing "
            "on merge_group; a queue build must run the full suite, so add "
            f"`{MERGE_GROUP_FIRES} ||` to its condition"
        )


def test_file_list_consumers_are_gated_on_their_output():
    # A step interpolating a `*_files` list without gating on the matching
    # output would run with an empty argument list whenever the filter finds
    # no changes — including validating nothing while reporting success.
    for step in workflow_steps():
        run = str(step.get("run", ""))
        if "steps.changes.outputs." not in run:
            continue
        name = step.get("name", "<unnamed>")
        condition = str(step.get("if", ""))
        outputs = {
            fragment.split("_files")[0]
            for fragment in run.split("steps.changes.outputs.")[1:]
            if "_files" in fragment.split("}}")[0]
        }
        for output in outputs:
            assert f"steps.changes.outputs.{output} == 'true'" in condition, (
                f"step {name!r} consumes steps.changes.outputs.{output}_files "
                f"but is not gated on steps.changes.outputs.{output}"
            )


def test_pr_only_steps_stay_guarded_by_event_name():
    # Steps that read github.event.pull_request.number would fail (or worse,
    # act on nothing) on merge_group/push events; they must pin the event.
    for step in workflow_steps():
        if "github.event.pull_request.number" not in str(step.get("run", "")):
            continue
        assert step.get("if") == "github.event_name == 'pull_request'", (
            f"step {step.get('name', '<unnamed>')!r} reads the PR number but "
            "is not guarded with github.event_name == 'pull_request'"
        )


def test_schema_term_validation_is_offline_on_merge_group():
    """The one forced step that reaches a third-party service must not make
    every queue build depend on it.

    Resolving the schema's dynamic-enum terms against EBI OLS is the point on
    a PR that touched the schema or the OAK config. On a merge group the step
    is forced on regardless of paths, which turned EBI availability into a
    merge dependency and ejected two queue builds in four hours on read
    timeouts the validator itself calls "not a data error" (#10677, #10700).
    """
    step = next(
        s for s in workflow_steps()
        if s.get("name") == "Validate schema term references"
    )
    run = str(step.get("run", ""))
    assert "--offline" in run, (
        "merge-group runs must validate schema terms against the committed "
        "cache, not a remote ontology service"
    )
    assert MERGE_GROUP_FIRES in str(step.get("if", "")), (
        "the step must still run on merge_group; only its network dependency "
        "is dropped"
    )
    # The PR path must keep the online check, which is where it can differ.
    online = [
        line for line in run.splitlines()
        if "validate-terms-schema" in line and "--offline" not in line
    ]
    assert online, "non-merge-group events must still validate online"
