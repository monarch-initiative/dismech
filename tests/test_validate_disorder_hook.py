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


def test_hook_marker_matches_the_recipe_warning():
    """The hook recognizes an outage by the text the recipe prints (#12634)."""
    assert hook.TERMS_NOT_CHECKED_MARKER in _recipe_body("validate-pre-edit")


def test_terms_not_checked_notice_reaches_the_model_without_approving():
    import json

    assert hook.terms_not_checked_notice("✓ Pre-edit validation passed") is None

    notice = hook.terms_not_checked_notice(
        "⚠ TERMS NOT CHECKED: ontology service unavailable."
    )
    payload = json.loads(notice)["hookSpecificOutput"]
    assert payload["hookEventName"] == "PreToolUse"
    assert "NOT checked" in payload["additionalContext"]
    # Adding context must never double as an approval of the tool call.
    assert "permissionDecision" not in payload


def test_terms_not_checked_notice_lists_the_unchecked_terms():
    """The model is told which terms to recheck, not just that some were skipped."""
    import json

    output = (
        "⚠ TERMS NOT CHECKED: ontology service unavailable.\n"
        "Offline recheck: no errors in what the local cache could check. Not checked:\n"
        "  not checked: HP:9999998 at phenotypes[1].phenotype_term.term "
        "(not in the local term cache)\n"
    )
    context = json.loads(hook.terms_not_checked_notice(output))["hookSpecificOutput"][
        "additionalContext"
    ]
    assert "not checked: HP:9999998 at phenotypes[1].phenotype_term.term" in context


def test_terms_not_checked_notice_caps_a_long_list():
    import json

    many = "\n".join(f"  not checked: HP:{i:07d}" for i in range(30))
    context = json.loads(
        hook.terms_not_checked_notice("TERMS NOT CHECKED\n" + many)
    )["hookSpecificOutput"]["additionalContext"]
    assert context.count("not checked: HP:") == hook.MAX_NOT_CHECKED_LINES
    assert "... and 10 more" in context


# --- Shared uv environment across worktrees (dismech#13119) -------------------


def _git(cwd: Path, *args: str) -> None:
    import subprocess

    subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.org", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
    )


@pytest.fixture
def primary_and_worktree(tmp_path):
    """A primary checkout with a `.venv`, plus a fresh worktree without one."""
    primary = _make_checkout(tmp_path / "dismech")
    (primary / "pyproject.toml").write_text("[project]\nname = 'x'\n")
    (primary / "uv.lock").write_text("version = 1\n")
    _git(primary, "init", "-q", "-b", "main")
    _git(primary, "add", "-A")
    _git(primary, "commit", "-q", "-m", "init")
    (primary / ".venv").mkdir()
    worktree = tmp_path / "wt" / "dismech-asthma"
    _git(primary, "worktree", "add", "-q", "-b", "asthma", str(worktree))
    return primary, worktree


def test_worktree_reuses_the_primary_environment_without_syncing(primary_and_worktree):
    primary, worktree = primary_and_worktree

    env = hook.validation_env(worktree, environ={})

    assert Path(env["UV_PROJECT_ENVIRONMENT"]).resolve() == (primary / ".venv").resolve()
    assert env["UV_NO_SYNC"] == "1", (
        "A worktree must not re-sync the shared environment, or it repoints the "
        "primary's editable install at itself."
    )


def test_explicit_uv_project_environment_wins(primary_and_worktree):
    _, worktree = primary_and_worktree

    env = hook.validation_env(worktree, environ={"UV_PROJECT_ENVIRONMENT": "/elsewhere"})

    assert env["UV_PROJECT_ENVIRONMENT"] == "/elsewhere"
    assert "UV_NO_SYNC" not in env


def test_primary_checkout_keeps_its_own_environment(primary_and_worktree):
    primary, _ = primary_and_worktree

    assert "UV_PROJECT_ENVIRONMENT" not in hook.validation_env(primary, environ={})


def test_worktree_with_its_own_venv_keeps_it(primary_and_worktree):
    _, worktree = primary_and_worktree
    (worktree / ".venv").mkdir()

    assert "UV_PROJECT_ENVIRONMENT" not in hook.validation_env(worktree, environ={})


@pytest.mark.parametrize("changed", ["pyproject.toml", "uv.lock"])
def test_worktree_with_different_dependencies_gets_its_own_environment(
    primary_and_worktree, changed
):
    _, worktree = primary_and_worktree
    (worktree / changed).write_text("# a dependency change on this branch\n")

    assert "UV_PROJECT_ENVIRONMENT" not in hook.validation_env(worktree, environ={})


def test_no_shared_environment_when_the_primary_has_none(primary_and_worktree):
    primary, worktree = primary_and_worktree
    (primary / ".venv").rmdir()

    assert "UV_PROJECT_ENVIRONMENT" not in hook.validation_env(worktree, environ={})


def test_outside_git_the_environment_is_unchanged(tmp_path):
    checkout = _make_checkout(tmp_path / "dismech")

    assert hook.validation_env(checkout, environ={"PATH": "/bin"}) == {"PATH": "/bin"}


# --- Rejected Write content is kept (dismech#16164) ---------------------------


def _run_main(monkeypatch, payload: dict, passes: bool) -> int:
    """Run the hook's main() on `payload` with validation stubbed out."""
    import io
    import json

    monkeypatch.setattr(hook, "recipe_available", lambda root, recipe: True)
    monkeypatch.setattr(
        hook,
        "validate_content",
        lambda content, path, root: (passes, "" if passes else "ERROR: bad slot"),
    )
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps(payload)))
    with pytest.raises(SystemExit) as exc:
        hook.main()
    return exc.value.code


PROPOSED = "name: Asthma\nnot_a_slot: true\ndescription: \"naïve — unicode\"\n"


def test_blocked_write_saves_the_proposed_content(tmp_path, monkeypatch, capsys):
    checkout = _make_checkout(tmp_path / "dismech-asthma")
    target = checkout / "kb" / "disorders" / "Asthma.yaml"

    code = _run_main(
        monkeypatch,
        {"tool_name": "Write", "tool_input": {"file_path": str(target), "content": PROPOSED}},
        passes=False,
    )

    saved = checkout / "tmp" / "rejected_edits" / "Asthma.yaml"
    assert code == 2
    assert saved.read_bytes() == PROPOSED.encode("utf-8")
    assert not target.exists(), "the blocked Write must still not reach kb/"
    err = capsys.readouterr().err
    assert str(saved) in err
    assert f"just {hook.VALIDATE_RECIPE} {saved}" in err


def test_a_second_rejection_overwrites_the_first(tmp_path, monkeypatch):
    checkout = _make_checkout(tmp_path / "dismech-asthma")
    target = checkout / "kb" / "disorders" / "Asthma.yaml"
    for content in ("name: first\n", "name: second\n"):
        _run_main(
            monkeypatch,
            {"tool_name": "Write", "tool_input": {"file_path": str(target), "content": content}},
            passes=False,
        )

    saved_dir = checkout / "tmp" / "rejected_edits"
    assert [p.name for p in saved_dir.iterdir()] == ["Asthma.yaml"]
    assert (saved_dir / "Asthma.yaml").read_text() == "name: second\n"


def test_a_passing_write_removes_a_stale_rejection(tmp_path, monkeypatch):
    checkout = _make_checkout(tmp_path / "dismech-asthma")
    target = checkout / "kb" / "disorders" / "Asthma.yaml"
    saved = checkout / "tmp" / "rejected_edits" / "Asthma.yaml"
    saved.parent.mkdir(parents=True)
    saved.write_text("name: old rejection\n")

    code = _run_main(
        monkeypatch,
        {"tool_name": "Write", "tool_input": {"file_path": str(target), "content": "name: Asthma\n"}},
        passes=True,
    )

    assert code == 0
    assert not saved.exists()


@pytest.mark.parametrize("tool_name", ["Edit", "MultiEdit"])
def test_blocked_edit_saves_nothing(tmp_path, monkeypatch, tool_name):
    checkout = _make_checkout(tmp_path / "dismech-asthma")
    target = checkout / "kb" / "disorders" / "Asthma.yaml"
    target.write_text("name: Asthma\n")
    edit = {"old_string": "name: Asthma\n", "new_string": PROPOSED}
    tool_input = {"file_path": str(target), **edit}
    if tool_name == "MultiEdit":
        tool_input = {"file_path": str(target), "edits": [edit]}

    code = _run_main(monkeypatch, {"tool_name": tool_name, "tool_input": tool_input}, passes=False)

    assert code == 2
    assert not (checkout / "tmp" / "rejected_edits").exists()
    assert target.read_text() == "name: Asthma\n"


def test_a_failed_save_still_blocks_without_crashing(tmp_path, monkeypatch, capsys):
    """A full disk (#13119) must not turn an ordinary block into a traceback."""
    checkout = _make_checkout(tmp_path / "dismech-asthma")
    target = checkout / "kb" / "disorders" / "Asthma.yaml"
    # A regular file where the directory should be makes mkdir raise OSError.
    (checkout / "tmp").write_text("not a directory\n")

    code = _run_main(
        monkeypatch,
        {"tool_name": "Write", "tool_input": {"file_path": str(target), "content": PROPOSED}},
        passes=False,
    )

    assert code == 2
    err = capsys.readouterr().err
    assert "BLOCKING EDIT" in err
    assert "Could not save the rejected content" in err
