"""Enum values reach pages through their schema labels, never through `title`.

Jinja's `title` filter lowercases everything after a word's first letter, so the
imaging modality `MRI` rendered as `Mri` (#16531).
"""

import re
from pathlib import Path

import pytest
import yaml

from dismech.render import (
    _ENUM_LABEL_OVERRIDES,
    _get_shared_env,
    enum_label,
    enum_tooltip,
    render_disorder,
)

SRC = Path(__file__).resolve().parents[1] / "src" / "dismech"
TEMPLATES = sorted((SRC / "templates").glob("*.j2"))
SCHEMA_ENUMS = yaml.safe_load((SRC / "schema" / "dismech.yaml").read_text())["enums"]


def _imaging_page(tmp_path: Path, finding: dict) -> str:
    disorder = {"name": "Example imaging disorder", "imaging_findings": [finding]}
    source = tmp_path / "Example.yaml"
    source.write_text(yaml.safe_dump(disorder))
    output = tmp_path / "page.html"
    render_disorder(source, output)
    html = output.read_text()
    start = html.index('class="card" id="imaging-findings"')
    end = html.find('class="card"', start + 1)
    return html[start:end] if end != -1 else html[start:]


def _term(curie: str, label: str) -> dict:
    return {"preferred_term": label, "term": {"id": curie, "label": label}}


@pytest.mark.parametrize("template", TEMPLATES, ids=lambda path: path.name)
def test_templates_do_not_title_case(template: Path) -> None:
    source = template.read_text()
    assert not re.search(r"\|\s*title\b", source), (
        f"{template.name} uses the `title` filter, which lowercases acronyms. "
        "Use `| enum_label('<EnumName>')` for an enum value."
    )


def test_shared_environment_provides_the_helpers() -> None:
    """Every page renderer uses this environment, and a missing filter fails at compile."""
    env = _get_shared_env(str(SRC / "templates"))
    assert env.filters["enum_label"] is enum_label
    assert env.globals["enum_tooltip"] is enum_tooltip


def test_every_enum_named_by_a_template_is_in_the_schema() -> None:
    """A misspelled enum name would silently fall back to the tidied key."""
    named = {
        name
        for template in TEMPLATES
        for name in re.findall(
            r"(?:enum_label\(|render_enum_tag\([^,]+,\s*)'(\w+)'", template.read_text()
        )
    }
    assert "ImagingModalityEnum" in named
    assert named <= set(SCHEMA_ENUMS)


@pytest.mark.parametrize("enum_name", sorted(_ENUM_LABEL_OVERRIDES))
def test_overrides_name_real_values(enum_name: str) -> None:
    values = set(SCHEMA_ENUMS[enum_name]["permissible_values"])
    assert set(_ENUM_LABEL_OVERRIDES[enum_name]) <= values


@pytest.mark.parametrize(
    ("value", "enum_name", "expected"),
    [
        ("MRI", "ImagingModalityEnum", "MRI"),
        ("FUNCTIONAL_MRI", "ImagingModalityEnum", "Functional MRI"),
        ("XRAY", "ImagingModalityEnum", "X-ray"),
        ("MAMMOGRAPHY", "ImagingModalityEnum", "Mammography"),
        ("COUNSELING_INFORMATIONAL", "MedicalActionCategoryEnum", "Counseling / Informational"),
        ("LIKELY_PATHOGENIC", "ClinicalSignificanceEnum", "Likely pathogenic"),
        ("IN_VITRO", "EvidenceSourceEnum", "In vitro / ex vivo"),
        ("ULTRA_RARE", "PrevalenceClassEnum", "Ultra-rare"),
        ("PRESENT_ABSENT", "BiomarkerReadoutDirectionEnum", "Present/absent"),
    ],
)
def test_enum_label(value: str, enum_name: str, expected: str) -> None:
    assert enum_label(value, enum_name) == expected


def test_unrecognized_value_still_renders_without_title_casing() -> None:
    assert enum_label("NOT_A_VALUE", "ImagingModalityEnum") == "Not a value"
    assert enum_label("mixed_Case", "ImagingModalityEnum") == "mixed Case"
    assert enum_label(None, "ImagingModalityEnum") == ""


@pytest.mark.parametrize(
    ("value", "enum_name", "label", "tooltip"),
    [
        ("MRI", "ImagingModalityEnum", "MRI", "Magnetic Resonance Imaging"),
        ("PET", "ImagingModalityEnum", "PET", "Positron Emission Tomography"),
        ("mLOE", "RegulatoryVariantCategoryEnum", "mLOE", "Modular loss of expression"),
    ],
)
def test_acronym_pill_spells_out_its_title(
    value: str, enum_name: str, label: str, tooltip: str
) -> None:
    assert enum_label(value, enum_name) == label
    assert enum_tooltip(value, enum_name) == tooltip


def test_tooltip_comes_from_the_schema() -> None:
    assert enum_tooltip("EXTENSIVE", "SpatialExtentEnum").startswith("Large extent")
    assert enum_tooltip("MAMMOGRAPHY", "ImagingModalityEnum") == "X-ray imaging of the breast"
    assert enum_tooltip("NOT_A_VALUE", "SpatialExtentEnum") == ""


def test_imaging_pills_name_their_slot(tmp_path: Path) -> None:
    card = _imaging_page(
        tmp_path,
        {
            "name": "White matter change",
            "modality": "MRI",
            "spatial_extent": "EXTENSIVE",
            "laterality": "BILATERAL",
            "diagnostic": True,
        },
    )
    assert "Modality: MRI" in card
    assert "Mri" not in card
    assert "Extent: Extensive" in card
    assert "Laterality: Bilateral" in card
    assert re.search(
        r'role="tooltip" id="pill-tip-\d+">Magnetic Resonance Imaging</span>', card
    )
    assert re.search(r'role="tooltip" id="pill-tip-\d+">Large extent', card)
    assert re.search(r'role="tooltip" id="pill-tip-\d+">This finding is pathognomonic', card)
    tip_ids = re.findall(r'id="(pill-tip-\d+)"', card)
    assert len(tip_ids) == len(set(tip_ids))


def test_imaging_context_is_a_note_not_a_pill(tmp_path: Path) -> None:
    context = "Reported adult-onset cases; association remains unproven."
    card = _imaging_page(tmp_path, {"name": "Finding", "context": context})
    assert f'<div class="item-desc">Context: {context}</div>' in card
    assert f'<span class="tag">{context}</span>' not in card


def test_identical_phenotype_term_is_not_repeated(tmp_path: Path) -> None:
    term = _term("HP:0002352", "Leukoencephalopathy")
    card = _imaging_page(
        tmp_path,
        {"name": "Finding", "imaging_finding_term": term, "phenotype_term": term},
    )
    assert "tag-bio" in card
    assert "tag-phenotype" not in card


def test_different_phenotype_term_is_kept_and_labelled(tmp_path: Path) -> None:
    card = _imaging_page(
        tmp_path,
        {
            "name": "Finding",
            "imaging_finding_term": _term("HP:0002352", "Leukoencephalopathy"),
            "phenotype_term": _term("HP:0002500", "Abnormality of the cerebral white matter"),
        },
    )
    assert "Finding:" in card
    assert "Phenotype:" in card
    assert "tag-phenotype" in card


def test_regulatory_category_pill_spells_out_its_acronym(tmp_path: Path) -> None:
    source = tmp_path / "Example.yaml"
    source.write_text(
        yaml.safe_dump(
            {
                "name": "Example regulatory disorder",
                "pathophysiology": [
                    {
                        "name": "Enhancer loss",
                        "regulatory_category": "mLOE",
                        "mechanism_confidence": "ESTABLISHED",
                    }
                ],
            }
        )
    )
    output = tmp_path / "page.html"
    render_disorder(source, output)
    html = output.read_text()
    assert "Regulatory category: mLOE (Established)" in html
    assert re.search(r'id="pill-tip-\d+">Modular loss of expression</span>', html)
