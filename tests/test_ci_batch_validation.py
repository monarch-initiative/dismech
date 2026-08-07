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
