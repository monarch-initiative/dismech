"""Every NAM-mining spec must fill every placeholder its template has.

`just nam-mining` renders templates/nam_mining_research.md from a hand-written
spec in templates/nam_mining/<slug>.yaml. None of its variables are generated:
which biological systems a paper contains and which mechanism nodes are worth
testing against are the screener's judgement, read off the paper. So the spec
file is the whole input, and a field missing from it is a hole in the prompt
rather than a stale value.

That hole is cheap to create and expensive to find. deep-research-client
substitutes the variables it is handed and leaves any other `{placeholder}` in
place, so a spec missing `candidate_nodes` sends a provider a template with the
literal text `{candidate_nodes}` where the nodes should be. The run still costs
a provider call and real minutes, and the report it returns looks like a report.
These tests make a missing field fail offline in milliseconds instead.

They also pin the two refusals the script already performs, so neither becomes
a silent pass: an unknown slug names the available ones rather than rendering an
empty prompt, and a spec missing a field is refused rather than partially
rendered.

This mirrors tests/test_claim_confirmation_specs.py, which guards its sibling
template the same way.
"""

from __future__ import annotations

import importlib.util
import pathlib
import re

import pytest

from dismech.yaml_io import safe_load_path

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "templates" / "nam_mining_research.md"
USE_CASES = REPO / "templates" / "nam_mining"
SCRIPT = REPO / "scripts" / "nam_mining_vars.py"

# The template is plain text with {name} placeholders, not a Jinja template.
PLACEHOLDER = re.compile(r"\{([a-z_]+)\}")


def template_placeholders() -> set[str]:
    return set(PLACEHOLDER.findall(TEMPLATE.read_text(encoding="utf-8")))


def spec_paths() -> list[pathlib.Path]:
    return sorted(USE_CASES.glob("*.yaml"))


def load_module(monkeypatch: pytest.MonkeyPatch):
    """Import the script with cwd at the repo root, which its paths assume."""
    monkeypatch.chdir(REPO)
    spec = importlib.util.spec_from_file_location("nam_mining_vars", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_the_template_and_the_script_agree_on_every_variable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """HAND_WRITTEN plus GENERATED must be exactly the template's placeholders.

    If the template gains a placeholder the script does not collect, every run
    goes out with that placeholder unsubstituted.
    """
    module = load_module(monkeypatch)
    assert set(module.HAND_WRITTEN) | set(module.GENERATED) == template_placeholders()


def test_hand_written_and_generated_do_not_overlap(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A spec must not be able to override a schema-derived definition.

    The generated definitions are authoritative precisely because no use case
    can restate them; a name in both tuples would let one quietly do so.
    """
    module = load_module(monkeypatch)
    assert not set(module.HAND_WRITTEN) & set(module.GENERATED)


def test_generated_definitions_cover_every_link_slot(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Each slot the prompt asks a run to fill must arrive with its definition."""
    module = load_module(monkeypatch)
    rendered = module.link_slot_definitions()
    missing = [slot for slot in module.LINK_SLOTS if f"`{slot}`" not in rendered]
    assert not missing, f"no definition emitted for: {', '.join(missing)}"


def test_generated_definitions_carry_enum_values_from_the_schema(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Every permitted value of the link's enums must appear.

    This is the drift the generator exists to prevent: the template used to
    list these verbs by hand, so a new enum value would have left the prompt
    describing a vocabulary the schema no longer had.
    """
    module = load_module(monkeypatch)
    schema = module._schema()
    rendered = module.link_slot_definitions(schema)
    for enum in ("ModelMechanismRelationshipEnum", "ModelDivergenceTypeEnum"):
        for value in schema["enums"][enum]["permissible_values"]:
            assert f"`{value}`" in rendered, f"{enum}.{value} missing from the prompt"


def test_slot_usage_description_wins_over_the_top_level_slot(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """`relationship` must be described as the model's verb, not a biomarker's.

    The top-level `relationship` slot in the schema is written for biomarkers
    ("between a biomarker and the pathograph node it reports on"), and
    ModelMechanismLink overrides it in `slot_usage`. Quoting the wrong one
    would hand a model-mining run a definition of a different object, which is
    worse than no definition at all.
    """
    module = load_module(monkeypatch)
    rendered = module.link_slot_definitions()
    assert "biomarker and the pathograph node" not in rendered
    assert "What this model does to the linked mechanism" in rendered


def test_at_least_one_spec_is_committed() -> None:
    """A passing sweep over zero specs would prove nothing."""
    assert spec_paths(), f"no specs found in {USE_CASES}"


@pytest.mark.parametrize("path", spec_paths(), ids=lambda p: p.stem)
def test_spec_supplies_every_placeholder(
    path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    module = load_module(monkeypatch)
    spec = safe_load_path(path)
    required = (template_placeholders() - set(module.GENERATED)) | {"entry"}
    missing = sorted(k for k in required if not spec.get(k))
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


@pytest.mark.parametrize("path", spec_paths(), ids=lambda p: p.stem)
def test_spec_names_a_source_identifier(path: pathlib.Path) -> None:
    """`reference` must carry a PMID or a DOI.

    The template tells the run to confine itself to one paper and to quote it.
    A spec whose reference names no resolvable identifier cannot support that,
    and the resulting report has nothing to validate its citations against.
    """
    reference = str(safe_load_path(path).get("reference", ""))
    assert re.search(r"PMID:\s*\d+", reference) or re.search(
        r"\b10\.\d{4,9}/", reference
    ), f"{path.name}: `reference` names no PMID or DOI"


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
        "reference": "PMID:1",
        "access": "x",
        "paper_summary": "x",
        "systems": "x",
    }
    path = tmp_path / "incomplete.yaml"
    path.write_text(
        "\n".join(f"{k}: {v}" for k, v in incomplete.items()) + "\n", encoding="utf-8"
    )
    monkeypatch.setattr(module, "USE_CASES", tmp_path)
    with pytest.raises(SystemExit) as excinfo:
        module.use_case("incomplete")
    assert "candidate_nodes" in str(excinfo.value)
