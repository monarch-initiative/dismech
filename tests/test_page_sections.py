"""The disorder-page section index must follow the order the template renders."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from dismech.page_sections import SECTIONS, section_index

TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "src" / "dismech" / "templates"


def _anchor_positions(template: str) -> dict[str, int]:
    """Position of each section anchor; included partials count at their include."""
    positions: dict[str, int] = {}
    for section in SECTIONS:
        match = re.search(rf'id="{re.escape(section.anchor)}"', template)
        if match:
            positions[section.anchor] = match.start()
    include = template.find('{% include "_model_cards.html.j2" %}')
    partial = (TEMPLATE_DIR / "_model_cards.html.j2").read_text()
    if include >= 0 and 'id="models"' in partial:
        positions["models"] = include
    return positions


def test_every_section_has_an_anchor_in_the_template() -> None:
    template = (TEMPLATE_DIR / "disorder.html.j2").read_text()
    positions = _anchor_positions(template)
    missing = [s.anchor for s in SECTIONS if s.anchor not in positions]
    assert not missing, f"no id=... for these sections in disorder.html.j2: {missing}"


def test_sections_are_listed_in_page_order() -> None:
    template = (TEMPLATE_DIR / "disorder.html.j2").read_text()
    positions = _anchor_positions(template)
    page_order = sorted(positions, key=positions.get)
    assert [s.anchor for s in SECTIONS] == page_order


def test_groups_are_contiguous() -> None:
    """A group heading appears once, so its sections must be adjacent."""
    seen: list[str] = []
    for section in SECTIONS:
        if not seen or seen[-1] != section.group:
            assert section.group not in seen, f"group {section.group!r} is split"
            seen.append(section.group)


@pytest.mark.parametrize(
    ("disorder", "extra", "expected"),
    [
        ({}, {}, []),
        (
            {
                "biochemical": [{"name": "Lyso-Gb3"}],
                "diagnosis": [{"name": "Enzyme assay"}],
            },
            {},
            [("Diagnosis", [("Biomarkers", 1), ("Diagnosis", 1)])],
        ),
        (
            {"epidemiology": {"incidence": "rare"}},
            {"comorbidities": 2},
            [
                ("Overview", [("Comorbidities", 2)]),
                ("Course & epidemiology", [("Epidemiology", 1)]),
            ],
        ),
    ],
)
def test_section_index_counts(disorder, extra, expected) -> None:
    groups = section_index(disorder, extra)
    assert [
        (g["group"], [(i["label"], i["count"]) for i in g["items"]]) for g in groups
    ] == expected
