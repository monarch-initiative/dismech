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

from dismech.render import render_disorder


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
