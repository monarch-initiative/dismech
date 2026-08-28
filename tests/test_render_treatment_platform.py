"""Tests for rendering the treatment platform rows on a disorder page.

`therapeutic_modality` and the oligonucleotide detail block were curated for a
long time without ever reaching the HTML: the treatment card renders an explicit
field list, and neither slot was on it. These tests pin the rows down so the
data stays visible.

The case that matters most is patisiran versus vutrisiran. They silence the same
transcript by the same mechanism and differ only in how the duplex is carried, so
`conjugation` and `delivery_platform` have to render as separate chips —
collapsing them would show "no targeting" versus "GalNAc" when the real
distinction is nanoparticle versus conjugate.
"""

import re
from pathlib import Path

import yaml

from dismech.render import render_disorder, render_module


def _strip_yaml_preview(html: str) -> str:
    """Drop the raw-YAML preview block the page embeds.

    It reproduces the source entry verbatim, so it contains the raw enum keys and
    duplicates every string these tests look for. Assertions about *rendered*
    markup have to exclude it.
    """
    return re.sub(
        r'<pre class="yaml-preview">.*?</pre>', "", html, flags=re.DOTALL
    )


def _render(tmp_path: Path, treatments: list[dict]) -> str:
    disorder_path = tmp_path / "Example_Disease.yaml"
    disorder_path.write_text(
        yaml.safe_dump(
            {
                "name": "Example Disease",
                "pathophysiology": [{"name": "Pathogenic Protein Accumulation"}],
                "treatments": treatments,
            },
            sort_keys=False,
        )
    )
    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)
    return _strip_yaml_preview(output_path.read_text())


def _sirna(name: str, conjugation: str, delivery_platform: str) -> dict:
    return {
        "name": name,
        "therapeutic_modality": "SIRNA",
        "oligonucleotide_details": {
            "oligonucleotide_mechanism": "RNAI_KNOCKDOWN",
            "target_gene": {
                "preferred_term": "TTR",
                "term": {"id": "hgnc:12405", "label": "TTR"},
            },
            "target_transcript": "TTR mRNA",
            "conjugation": conjugation,
            "delivery_platform": delivery_platform,
        },
    }


def test_lnp_and_galnac_sirnas_are_distinguishable(tmp_path: Path) -> None:
    html = _render(
        tmp_path,
        [
            _sirna("Patisiran", "UNCONJUGATED", "LIPID_NANOPARTICLE"),
            _sirna("Vutrisiran", "GALNAC", "CONJUGATE"),
        ],
    )

    assert "Delivery: Lipid nanoparticle" in html
    assert "Conjugate: Unconjugated" in html
    assert "Delivery: Ligand conjugate" in html
    assert "Conjugate: GalNAc" in html

    # Shared mechanism and target render for both.
    assert html.count("RNAi knockdown") == 2
    assert html.count("TTR mRNA") == 2
    assert "hgnc:12405" in html


def test_enum_values_get_readable_labels(tmp_path: Path) -> None:
    """Raw enum keys must not leak, and `| title` alone would give 'Sirna'."""
    html = _render(tmp_path, [_sirna("Patisiran", "UNCONJUGATED", "LIPID_NANOPARTICLE")])

    assert "siRNA" in html
    assert "SIRNA" not in html
    assert "RNAI_KNOCKDOWN" not in html
    assert "LIPID_NANOPARTICLE" not in html
    assert "UNCONJUGATED" not in html


def test_deprecated_aso_details_still_renders(tmp_path: Path) -> None:
    """Entries authored before the slot was generalized must keep rendering."""
    html = _render(
        tmp_path,
        [
            {
                "name": "Legacy ASO",
                "therapeutic_modality": "ANTISENSE_OLIGONUCLEOTIDE",
                "aso_details": {
                    "aso_mechanism": "RNASE_H_KNOCKDOWN",
                    "aso_chemistry": "TWO_PRIME_O_METHOXYETHYL",
                    "target_transcript": "APOB mRNA",
                },
            }
        ],
    )

    assert "RNase H knockdown" in html
    assert "APOB mRNA" in html
    assert "Chemistry: 2′-MOE" in html


def test_dosing_interval_renders_verbatim_and_normalized(tmp_path: Path) -> None:
    html = _render(
        tmp_path,
        [
            {
                "name": "Inclisiran",
                "therapeutic_modality": "SIRNA",
                "dosing_interval": "once every 6 months after loading",
                "dosing_interval_days": 182.5,
            }
        ],
    )

    assert "once every 6 months after loading" in html
    # A non-integer interval keeps its fraction rather than being truncated.
    assert "every 182.5 days" in html


def test_treatment_without_platform_data_renders_no_platform_row(tmp_path: Path) -> None:
    """A surgical or supportive treatment must be untouched by this change."""
    html = _render(
        tmp_path,
        [{"name": "Orthotopic liver transplantation", "description": "Definitive."}],
    )

    assert "Platform:" not in html
    assert "RNA target:" not in html
    assert "Dosing:" not in html
    assert "Orthotopic liver transplantation" in html


def _render_module(tmp_path: Path, treatments: list[dict]) -> str:
    """Render a module page, which until recently showed no treatments at all."""
    module_path = tmp_path / "example_module.yaml"
    module_path.write_text(
        yaml.safe_dump(
            {
                "name": "Example Module",
                "category": "Module",
                "description": "A module.",
                "pathophysiology": [{"name": "Target Node", "role": "effector"}],
                "treatments": treatments,
            },
            sort_keys=False,
        )
    )
    disorders_dir = tmp_path / "kb" / "disorders"
    disorders_dir.mkdir(parents=True)
    output_path = tmp_path / "pages" / "modules" / "example_module.html"
    render_module(module_path, output_path=output_path, disorders_dir=disorders_dir)
    return _strip_yaml_preview(output_path.read_text())


def test_module_page_renders_its_treatments(tmp_path: Path) -> None:
    html = _render_module(
        tmp_path,
        [
            {
                "name": "Vutrisiran",
                "therapeutic_modality": "SIRNA",
                "oligonucleotide_details": {
                    "oligonucleotide_mechanism": "RNAI_KNOCKDOWN",
                    "target_gene": {
                        "preferred_term": "TTR",
                        "term": {"id": "hgnc:12405", "label": "TTR"},
                    },
                    "conjugation": "GALNAC",
                    "delivery_platform": "CONJUGATE",
                },
                "dosing_interval": "once every 3 months",
                "dosing_interval_days": 90,
                "target_mechanisms": [
                    {"target": "Target Node", "treatment_effect": "ACTIVATES"}
                ],
            }
        ],
    )

    assert 'id="treatments"' in html
    assert "Vutrisiran" in html
    assert "Conjugate: GalNAc" in html
    assert "Delivery: Ligand conjugate" in html
    assert "hgnc:12405" in html
    assert "once every 3 months" in html


def test_module_treatment_links_to_its_target_node(tmp_path: Path) -> None:
    """The mechanism target should reach the node's card, not sit as dead text."""
    html = _render_module(
        tmp_path,
        [
            {
                "name": "Some Drug",
                "target_mechanisms": [
                    {"target": "Target Node", "treatment_effect": "INHIBITS"}
                ],
            }
        ],
    )

    anchor = re.search(r'id="([^"]+)"[^>]*data-dismech-type="pathophysiology"', html)
    assert anchor, "pathophysiology node should carry an anchor id"
    assert f'href="#{anchor.group(1)}"' in html


def test_module_treatment_without_platform_data_renders_no_platform_row(
    tmp_path: Path,
) -> None:
    html = _render_module(tmp_path, [{"name": "Supportive care", "description": "X."}])

    assert 'id="treatments"' in html
    assert "Platform:" not in html
    assert "RNA target:" not in html
    assert "Dosing:" not in html


def test_every_platform_enum_value_has_a_curated_label() -> None:
    """A new enum member should get a real label, not the generic fallback.

    The fallback in `treatment_platform_label` exists so an unlabeled value still
    shows on the page rather than vanishing. It is a safety net, not the intended
    outcome: it would render TWO_PRIME_FLUORO as "Two prime fluoro". This test is
    what tells whoever adds an enum member to write the label.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    from dismech.treatment_platform import TREATMENT_PLATFORM_LABELS

    view = SchemaView("src/dismech/schema/dismech.yaml")
    enums = [
        "TherapeuticModalityEnum",
        "OligonucleotideMechanismEnum",
        "OligonucleotideChemistryEnum",
        "OligonucleotideConjugationEnum",
        "OligonucleotideDeliveryPlatformEnum",
    ]

    missing = {
        f"{enum}.{value}"
        for enum in enums
        for value in view.get_enum(enum).permissible_values
        if value not in TREATMENT_PLATFORM_LABELS
    }
    assert not missing, f"add display labels for: {sorted(missing)}"


def test_platform_label_falls_back_rather_than_vanishing() -> None:
    from dismech.treatment_platform import treatment_platform_label

    assert treatment_platform_label("SIRNA") == "siRNA"
    assert treatment_platform_label("A_BRAND_NEW_VALUE") == "A brand new value"
    assert treatment_platform_label(None) == ""
    assert treatment_platform_label("") == ""
