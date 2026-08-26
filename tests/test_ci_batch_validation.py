from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent


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
    workflow = (ROOT / ".github" / "workflows" / "main.yaml").read_text()
    assert "- name: Check entity references resolve" in workflow
    step = workflow.split("- name: Check entity references resolve", 1)[1]
    step = step.split("- name:", 1)[0]
    assert "scripts/check_entity_refs.py" in step
    assert "if:" not in step, "the entity-ref check must stay ungated"
    # No file arguments: the sweep is whole-KB, not changed-files.
    assert "steps.changes.outputs" not in step


def test_nightly_sweep_runs_both_pytest_lanes() -> None:
    """The nightly backstop must run the unmarked lane too (#5155, #9473).

    `just test-kb` is `pytest -m kb_data`, and five whole-KB checks in
    `tests/test_data.py` carry no such marker -- the three entity-ref/FK tests
    and the two unique-name tests. A backstop that ran only `test-kb` would
    leave exactly the checks that have gone stale before uncovered.
    """
    workflow = (ROOT / ".github" / "workflows" / "nightly-kb-sweep.yaml").read_text()
    assert "just test-kb" in workflow
    assert "just test-python-code" in workflow
    assert "schedule:" in workflow
