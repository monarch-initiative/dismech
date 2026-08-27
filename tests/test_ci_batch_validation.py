from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from dismech.yaml_io import safe_load


def _recipe_body(justfile: str, recipe: str) -> str:
    match = re.search(rf"(?m)^{re.escape(recipe)}:\n", justfile)
    assert match is not None, f"recipe {recipe!r} not found"
    body = justfile[match.end() :]
    return body.split("\n# ", 1)[0]


def test_validate_comorbidities_batches_expensive_validators() -> None:
    """Changed-file comorbidity validation safely reuses processes."""
    body = _recipe_body(
        (ROOT / "project.justfile").read_text(),
        "validate-comorbidity-batch *files",
    )

    assert 'for f in "$@"; do' in body
    assert '"$f" == {{comorbidity_dir}}/*.yaml' in body
    assert (
        "uv run linkml-validate --schema {{schema_path}} "
        '--target-class ComorbidityAssociation "${existing[@]}"' in body
    )
    assert (
        '{{term_validator}} validate-data "${existing[@]}" -s {{schema_path}} '
        "-t ComorbidityAssociation" in body
    )
    assert (
        '{{ref_validator}} validate data "${existing[@]}" '
        "--schema {{schema_path}} --target-class ComorbidityAssociation" in body
    )
    assert "just check-enum-cache" not in body
    assert "--no-full-text" in body
    assert body.count("|| exit_code=1") == 4


def test_ci_changed_comorbidity_validation_uses_batched_recipe() -> None:
    workflow = (ROOT / ".github" / "workflows" / "main.yaml").read_text()
    changed_step = workflow.split("- name: Validate changed comorbidity KB files", 1)[
        1
    ].split("- name: Validate history records", 1)[0]

    assert "just validate-comorbidity-batch" in changed_step
    assert "for f in" not in changed_step
    assert 'just validate-comorbidity "$f"' not in changed_step


def _workflow_steps(filename: str) -> list[dict]:
    """Every step of every job in a workflow, parsed rather than string-sliced.

    Reviewed on #9504: an earlier version of this test sliced the file between
    `- name:` markers, so its assertions were also scanning the *next* step's
    comment block -- an edit to unrelated prose could fail it, and an `if:` on
    a neighbouring step would have looked like a finding here.
    """
    workflow = safe_load((ROOT / ".github" / "workflows" / filename).read_text())
    return [
        step
        for job in workflow["jobs"].values()
        for step in job.get("steps", [])
        if isinstance(step, dict)
    ]


def _step_named(filename: str, name: str) -> dict:
    matches = [s for s in _workflow_steps(filename) if s.get("name") == name]
    assert len(matches) == 1, f"expected exactly one {name!r} step in {filename}"
    return matches[0]


def test_entity_ref_check_runs_ungated_over_the_whole_kb() -> None:
    """The entity-ref lane must not acquire a path filter (#9473).

    Its entire reason for existing is that the pytest sweep covering the same
    rules is selected by the `python`/`schema` filters, so it never runs on a
    curation PR -- the only kind of PR that can break a reference. A well-meant
    `if: steps.changes.outputs.kb_disorders == 'true'` here would restore the
    hole in a subtler form: `kb/modules/**` and `kb/groupings/**` have no filter
    at all, and a PR deleting a referenced node need not touch the file that
    references it.
    """
    step = _step_named("main.yaml", "Check entity references resolve")
    assert "if" not in step, "the entity-ref check must stay ungated"
    run = step["run"].strip()
    assert run.endswith("scripts/check_entity_refs.py"), (
        f"the sweep must take no file arguments; got {run!r}"
    )


def test_nightly_sweep_runs_both_pytest_lanes() -> None:
    """The nightly backstop must run the unmarked lane too (#5155, #9473).

    `just test-kb` is `pytest -m kb_data`, and five whole-KB checks in
    `tests/test_data.py` carry no such marker -- the three entity-ref/FK tests
    and the two unique-name tests. A backstop that ran only `test-kb` would
    leave exactly the checks that have gone stale before uncovered.
    """
    steps = _workflow_steps("nightly-kb-sweep.yaml")
    runs = " ".join(step.get("run", "") for step in steps)
    assert "just test-kb" in runs
    assert "just test-python-code" in runs
    workflow = safe_load(
        (ROOT / ".github" / "workflows" / "nightly-kb-sweep.yaml").read_text()
    )
    # PyYAML resolves the bare key `on` to the boolean True (YAML 1.1).
    triggers = workflow.get("on") or workflow[True]
    assert "schedule" in triggers


def test_nightly_sweep_reuses_the_oak_cache_action() -> None:
    """The nightly must `uses:` the composite action, not re-inline half of it.

    Reviewed on #9504, where this step pinned `PYSTOW_HOME` but dropped the
    `actions/cache` half it exists to serve -- so it was named "Cache ..." and
    cached nothing, and every nightly would re-download whole ontology
    databases for the four OAK-touching tests that carry no `kb_data` marker.
    """
    step = _step_named("nightly-kb-sweep.yaml", "Cache OAK ontology databases")
    assert step.get("uses") == "./.github/actions/oak-cache"


def test_entity_ref_sweep_covers_every_kb_subtree() -> None:
    """A new `kb/<something>/` must be listed as checked or as excluded (#9504).

    A tree nobody checks is the bug `check_entity_refs.py` exists to fix, so
    silence is not an acceptable default for one. This fails on a new subtree
    until somebody decides which list it belongs in.
    """
    from scripts.check_entity_refs import DEFAULT_ROOTS, EXCLUDED_ROOTS

    accounted = {*DEFAULT_ROOTS, *EXCLUDED_ROOTS}
    present = {f"kb/{d.name}" for d in (ROOT / "kb").iterdir() if d.is_dir()}
    assert present <= accounted, (
        f"unaccounted kb/ subtree(s): {sorted(present - accounted)}. Add each to "
        f"DEFAULT_ROOTS (checked) or EXCLUDED_ROOTS (with a reason) in "
        f"scripts/check_entity_refs.py."
    )
