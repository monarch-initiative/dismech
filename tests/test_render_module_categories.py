"""Tests for module study-area category pills (module index + module pages)."""

from itertools import pairwise
from pathlib import Path

import yaml

from dismech.render import (
    _module_category_display,
    _resolve_module_categories,
    render_all_modules,
    render_module_index,
)
from dismech.yaml_io import safe_load_path


def _write_module(path: Path, name: str, categories: list[str] | None) -> None:
    data: dict = {
        "name": name,
        "description": f"{name} test module.",
        "category": "Module",
        "pathophysiology": [{"name": f"{name} Node"}],
    }
    if categories is not None:
        data["module_categories"] = categories
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_display_records_come_from_the_schema_enum() -> None:
    display = _module_category_display()
    schema = safe_load_path(Path("src/dismech/schema/dismech.yaml"))
    permissible_values = schema["enums"]["ModuleCategoryEnum"]["permissible_values"]

    assert set(display) == set(permissible_values)
    for key, record in display.items():
        assert record["label"] == permissible_values[key]["title"]
        assert record["description"], f"{key} needs descriptive text in the schema"


def test_every_category_gets_a_visually_distinct_hue() -> None:
    hues = sorted(int(record["hue"]) for record in _module_category_display().values())
    gaps = [b - a for a, b in pairwise(hues)] + [360 - hues[-1] + hues[0]]
    assert min(gaps) >= 20, f"hues crowd together: {hues}"


def test_resolved_categories_follow_enum_order_and_drop_duplicates() -> None:
    resolved = _resolve_module_categories(
        {"module_categories": ["NEUROSCIENCE", "TOXICOLOGY", "NEUROSCIENCE"]}
    )

    # TOXICOLOGY is declared before NEUROSCIENCE in the enum, so it leads
    # regardless of the order the curator typed.
    assert [record["key"] for record in resolved] == ["TOXICOLOGY", "NEUROSCIENCE"]


def test_unknown_category_is_shown_rather_than_silently_dropped() -> None:
    (record,) = _resolve_module_categories({"module_categories": ["NOT_A_CATEGORY"]})

    assert record["label"] == "Not A Category"
    assert record["description"] == ""
    # Neutral grey, so a curation error does not masquerade as a real category.
    assert "hsl(" not in record["background"]


def test_module_pages_render_pills_and_the_index_renders_a_legend(
    tmp_path: Path,
) -> None:
    modules_dir = tmp_path / "kb" / "modules"
    _write_module(modules_dir / "tagged.yaml", "Tagged Module", ["TOXICOLOGY"])
    _write_module(modules_dir / "untagged.yaml", "Untagged Module", None)

    output_dir = tmp_path / "pages" / "modules"
    render_all_modules(
        input_dir=modules_dir,
        output_dir=output_dir,
        disorders_dir=tmp_path / "kb" / "disorders",
    )

    # Match the rendered element, not the class name: the stylesheet defining
    # .badge-study-area is inlined on every module page, tagged or not.
    pill = 'class="badge badge-study-area"'

    detail = (output_dir / "tagged.html").read_text()
    assert pill in detail
    assert ">Toxicology<" in detail

    untagged = (output_dir / "untagged.html").read_text()
    assert pill not in untagged

    index = (output_dir / "index.html").read_text()
    assert index.count('class="category-pill"') == 2  # one card pill, one legend pill
    assert "What do the category labels mean?" in index
    # The legend carries the schema's own blurb, not a label repeated twice.
    assert _module_category_display()["TOXICOLOGY"]["description"] in index


def test_index_legend_omits_categories_no_module_uses(tmp_path: Path) -> None:
    modules_dir = tmp_path / "kb" / "modules"
    _write_module(modules_dir / "tagged.yaml", "Tagged Module", ["TOXICOLOGY"])
    output_path = tmp_path / "index.html"

    render_module_index(
        [{"name": "Tagged Module", "href": "tagged.html", "categories": []}],
        output_path,
    )

    assert "What do the category labels mean?" not in output_path.read_text()


def test_module_categories_stays_off_disorder_entries() -> None:
    """`module_categories` is schema-legal on any Disease, but is for modules.

    The slot hangs off the Disease class because modules validate against it, so
    nothing in the schema stops it appearing in kb/disorders/ — where it would
    render nowhere and quietly compete with the unrelated free-text `categories`
    slot disorders actually use. This keeps that from starting.
    """
    offenders = [
        path.name
        for path in sorted(Path("kb/disorders").glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
        and (safe_load_path(path) or {}).get("module_categories")
    ]

    assert not offenders, (
        "module_categories belongs on kb/modules/ entries; disorder entries use "
        f"the free-text `categories` slot: {offenders}"
    )


def test_committed_modules_use_only_schema_defined_categories() -> None:
    allowed = set(_module_category_display())
    offenders: dict[str, list[str]] = {}

    for path in sorted(Path("kb/modules").glob("*.yaml")):
        values = safe_load_path(path).get("module_categories") or []
        unknown = [value for value in values if value not in allowed]
        if unknown:
            offenders[path.name] = unknown

    assert not offenders, f"module_categories outside ModuleCategoryEnum: {offenders}"
