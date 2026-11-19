"""Every claim-confirmation spec must fill every placeholder its template has.

`just claim-confirmation` renders templates/claim_confirmation_research.md from
a hand-written spec in templates/claim_confirmation/<slug>.yaml. Unlike its
siblings, none of its variables are generated: nothing in the repository can
derive a claim list, because deciding which assertions of a source are worth
checking is the curator's judgement. So the spec file is the whole input, and a
field missing from it is a hole in the prompt rather than a stale value.

That hole is cheap to create and expensive to find. deep-research-client
substitutes the variables it is handed and leaves any other `{placeholder}` in
place, so a spec missing `claims` sends a provider a template with the literal
text `{claims}` where the claims should be. The run still costs a provider call
and real minutes, and the report it returns looks like a report. These tests
make a missing field fail offline in milliseconds instead.

They also pin the two refusals the script already performs, so neither becomes
a silent pass: an unknown slug names the available ones rather than rendering
an empty prompt, and a spec missing a field is refused rather than partially
rendered.
"""

from __future__ import annotations

import importlib.util
import pathlib
import re

import pytest

from dismech.yaml_io import safe_load_path

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "templates" / "claim_confirmation_research.md"
USE_CASES = REPO / "templates" / "claim_confirmation"
SCRIPT = REPO / "scripts" / "claim_confirmation_vars.py"

# The template is plain text with {name} placeholders, not a Jinja template.
PLACEHOLDER = re.compile(r"\{([a-z_]+)\}")


def template_placeholders() -> set[str]:
    return set(PLACEHOLDER.findall(TEMPLATE.read_text(encoding="utf-8")))


def spec_paths() -> list[pathlib.Path]:
    return sorted(USE_CASES.glob("*.yaml"))


def load_module(monkeypatch: pytest.MonkeyPatch):
    """Import the script with cwd at the repo root, which its paths assume."""
    monkeypatch.chdir(REPO)
    spec = importlib.util.spec_from_file_location("claim_confirmation_vars", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_the_template_and_the_script_agree_on_which_fields_are_hand_written(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """HAND_WRITTEN must be exactly the template's placeholders.

    If the template gains a placeholder the script does not collect, every run
    goes out with that placeholder unsubstituted.
    """
    module = load_module(monkeypatch)
    assert set(module.HAND_WRITTEN) == template_placeholders()


def test_at_least_one_spec_is_committed() -> None:
    """A passing sweep over zero specs would prove nothing."""
    assert spec_paths(), f"no specs found in {USE_CASES}"


@pytest.mark.parametrize("path", spec_paths(), ids=lambda p: p.stem)
def test_spec_supplies_every_placeholder(path: pathlib.Path) -> None:
    spec = safe_load_path(path)
    missing = sorted(k for k in template_placeholders() | {"entry"} if not spec.get(k))
    assert not missing, f"{path.name} is missing: {', '.join(missing)}"


@pytest.mark.parametrize("path", spec_paths(), ids=lambda p: p.stem)
def test_spec_renders_with_no_placeholder_left(
    path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Substituting the spec's values must consume every placeholder.

    Checked without the client's TemplateProcessor so the test stays offline
    and dependency-free; the contract under test is the template's, not the
    renderer's.
    """
    module = load_module(monkeypatch)
    values = module.variables(safe_load_path(path))
    rendered = TEMPLATE.read_text(encoding="utf-8")
    for name, value in values.items():
        rendered = rendered.replace("{" + name + "}", value)
    leftover = sorted(set(PLACEHOLDER.findall(rendered)))
    assert not leftover, f"{path.name} leaves unsubstituted: {', '.join(leftover)}"


def test_unknown_slug_is_refused_and_names_the_available_ones(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = load_module(monkeypatch)
    with pytest.raises(SystemExit) as excinfo:
        module.use_case("no_such_slug")
    message = str(excinfo.value)
    assert "no_such_slug" in message
    for path in spec_paths():
        assert path.stem in message


def test_spec_missing_a_field_is_refused(
    monkeypatch: pytest.MonkeyPatch, tmp_path: pathlib.Path
) -> None:
    """A partially filled spec must fail rather than render a holed prompt."""
    module = load_module(monkeypatch)
    incomplete = {
        "entry": "Some_Disease",
        "source_citation": "Someone et al.",
        "context": "x",
    }
    path = tmp_path / "incomplete.yaml"
    path.write_text(
        "\n".join(f"{k}: {v}" for k, v in incomplete.items()) + "\n", encoding="utf-8"
    )
    monkeypatch.setattr(module, "USE_CASES", tmp_path)
    with pytest.raises(SystemExit) as excinfo:
        module.use_case("incomplete")
    assert "claims" in str(excinfo.value)
