"""Tests for the PreToolUse disorder-validation hook (.claude/hooks/).

Regression cover for dismech#8542: the hook derived its validation cwd from its
own location (`Path(__file__).parent.parent.parent`), but Claude Code invokes it
as "$CLAUDE_PROJECT_DIR"/.claude/hooks/..., and CLAUDE_PROJECT_DIR is always the
primary checkout. Every edit made in a `git worktree` therefore ran its
validation — and that validation's working-tree side effects — against the
primary checkout instead of the worktree the agent was editing.
"""

import importlib.util
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK_PATH = REPO_ROOT / ".claude" / "hooks" / "validate_disorder_hook.py"
PROJECT_JUSTFILE = REPO_ROOT / "project.justfile"


def _load_hook():
    spec = importlib.util.spec_from_file_location("validate_disorder_hook", HOOK_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hook = _load_hook()


def _make_checkout(root: Path) -> Path:
    """Create the minimal marker layout of a dismech checkout."""
    (root / "kb" / "disorders").mkdir(parents=True)
    (root / "justfile").write_text("# marker\n")
    return root


def test_find_project_root_resolves_to_the_edited_files_own_checkout(tmp_path):
    primary = _make_checkout(tmp_path / "dismech")
    worktree = _make_checkout(tmp_path / "dismech-ffi")
    edited = worktree / "kb" / "disorders" / "Fatal_Familial_Insomnia.yaml"
    edited.write_text("name: Fatal Familial Insomnia\n")

    assert hook.find_project_root(edited) == worktree
    assert hook.find_project_root(edited) != primary


def test_find_project_root_picks_the_nearest_enclosing_checkout(tmp_path):
    """A worktree nested inside another checkout still routes to itself."""
    outer = _make_checkout(tmp_path / "dismech")
    inner = _make_checkout(outer / "worktrees" / "dismech-ibm")
    edited = inner / "kb" / "disorders" / "Inclusion_Body_Myositis.yaml"
    edited.write_text("name: Inclusion Body Myositis\n")

    assert hook.find_project_root(edited) == inner
    assert hook.find_project_root(edited) != outer


def test_find_project_root_returns_none_outside_any_checkout(tmp_path):
    stray = tmp_path / "kb" / "disorders" / "Asthma.yaml"
    stray.parent.mkdir(parents=True)
    stray.write_text("name: Asthma\n")

    assert hook.find_project_root(stray) is None


def test_find_project_root_ignores_the_hooks_own_checkout(tmp_path):
    """The hook script lives in the real repo; that must not leak into routing."""
    worktree = _make_checkout(tmp_path / "dismech-elsewhere")
    edited = worktree / "kb" / "disorders" / "Asthma.yaml"
    edited.write_text("name: Asthma\n")

    assert hook.find_project_root(edited) == worktree
    assert hook.find_project_root(edited) != REPO_ROOT


def test_recipe_available_detects_a_present_recipe():
    assert hook.recipe_available(REPO_ROOT, hook.VALIDATE_RECIPE) is True


def test_recipe_available_detects_a_checkout_predating_the_recipe(tmp_path):
    """An older worktree must be skipped, not have every disorder edit blocked."""
    old_checkout = _make_checkout(tmp_path / "dismech-old")
    (old_checkout / "justfile").write_text("validate file:\n    @echo {{file}}\n")

    assert hook.recipe_available(old_checkout, hook.VALIDATE_RECIPE) is False


def test_hook_does_not_derive_its_root_from_its_own_location():
    source = HOOK_PATH.read_text()
    assert "Path(__file__).parent.parent.parent" not in source, (
        "The hook must derive its validation cwd from the edited file's checkout, "
        "not from where the hook script itself lives (dismech#8542)."
    )


def test_hook_runs_the_side_effect_free_recipe():
    source = HOOK_PATH.read_text()
    assert hook.VALIDATE_RECIPE == "validate-pre-edit", (
        "The pre-edit hook must call `just validate-pre-edit`, not `just validate` "
        "— the latter rewrites the reference and term caches on every edit."
    )
    assert '"just", "validate"' not in source


def _recipe_body(name: str) -> str:
    text = PROJECT_JUSTFILE.read_text()
    match = re.search(rf"^{re.escape(name)} .*?:\n((?:[ \t]+.*\n|\n)*)", text, re.MULTILINE)
    assert match, f"recipe {name!r} not found in project.justfile"
    return match.group(1)


def test_validate_pre_edit_recipe_exists_and_has_no_working_tree_side_effects():
    body = _recipe_body("validate-pre-edit")

    for mutating in ("fix-references-cache", "normalize-cache"):
        assert mutating not in body, (
            f"`validate-pre-edit` runs on every disorder edit, so it must not call "
            f"`{mutating}` — that leaves cache churn in the agent's worktree (dismech#8542)."
        )
    assert "--no-full-text" in body, (
        "Reference validation in the pre-edit hook must stay cache-bound so it does "
        "not download PDFs or write full-text state back into references_cache/."
    )


def test_validate_pre_edit_keeps_reference_validation_advisory():
    """Snippet verification depends on cache state, so it must not block an edit."""
    body = _recipe_body("validate-pre-edit")
    ref_line = next(line for line in body.splitlines() if "validate data" in line)

    assert ref_line.lstrip().startswith("if ! "), (
        "Reference validation must be guarded so it warns instead of failing the "
        "recipe — a quote from a paywalled paper's body reads as unverified, not "
        "wrong, and blocking on it strands an in-progress edit (dismech#8542)."
    )


@pytest.mark.parametrize("validator", ["linkml-validate", "validate-data", "validate data"])
def test_validate_pre_edit_keeps_all_three_validators(validator):
    assert validator in _recipe_body("validate-pre-edit")
