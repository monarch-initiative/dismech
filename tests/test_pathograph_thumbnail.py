"""Tests for the label-free pathograph thumbnail and the disorder-page header."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from dismech.cli import app
from dismech.graph import build_causal_graph
from dismech.pathograph_thumbnail import render_thumbnail
from dismech.render import render_disorder

DISORDER = {
    "name": "Thumbnail Disorder",
    "genetic": [{"name": "GENE1", "association": "causative"}],
    "pathophysiology": [
        {"name": "Enzyme deficiency", "downstream": [{"target": "Substrate storage"}]},
        {
            "name": "Substrate storage",
            "downstream": [{"target": "Pain"}, {"target": "Plasma marker"}],
        },
    ],
    "phenotypes": [{"name": "Pain"}, {"name": "Rash"}],
    "biochemical": [{"name": "Plasma marker", "presence": "Increased"}],
    "treatments": [
        {
            "name": "Enzyme replacement",
            "target_mechanisms": [{"target": "Enzyme deficiency"}],
        }
    ],
}


@pytest.fixture
def thumbnail():
    return render_thumbnail(build_causal_graph(DISORDER))


def test_thumbnail_is_well_formed_svg(thumbnail) -> None:
    root = ET.fromstring(thumbnail.svg)
    assert root.tag.endswith("svg")
    width, height = map(float, root.attrib["viewBox"].split()[2:])
    assert width == 300
    assert 0 < height < 200


def test_thumbnail_counts(thumbnail) -> None:
    assert thumbnail.phenotypes == 2
    assert thumbnail.phenotypes_connected == 1
    assert thumbnail.unconnected == 1  # Rash has no edge


def test_connected_count_matches_the_causal_inlink_metric() -> None:
    """A readout-only phenotype is drawn but not counted as connected (#11935)."""
    from dismech.qc_plugins import causal_inlink_coverage

    disorder = {
        "name": "Readout Disorder",
        "pathophysiology": [
            {"name": "Mechanism", "downstream": [{"target": "Pain"}]},
        ],
        "phenotypes": [
            {"name": "Pain"},
            {"name": "Lab finding", "reports_on": [{"target": "Mechanism"}]},
        ],
    }
    thumb = render_thumbnail(build_causal_graph(disorder))
    connected, total, _ = causal_inlink_coverage(disorder)
    assert (thumb.phenotypes_connected, thumb.phenotypes) == (connected, total)
    assert thumb.phenotypes_connected == 1


def test_thumbnail_has_no_visible_text(thumbnail) -> None:
    """Names appear only as hover titles, never as drawn labels."""
    assert "<text" not in thumbnail.svg
    titles = re.findall(r"<title>([^<]*)</title>", thumbnail.svg)
    assert {"Enzyme deficiency", "Pain", "Enzyme replacement"} <= set(titles)
    assert "Rash (no causal edge)" in titles


def test_thumbnail_places_outcomes_right_of_mechanisms(thumbnail) -> None:
    x = {
        title: float(cx)
        for cx, title in re.findall(
            r'<circle cx="([\d.]+)"[^>]*><title>([^<]*)</title>', thumbnail.svg
        )
    }
    assert x["Enzyme deficiency"] < x["Substrate storage"] < x["Pain"]


def test_tall_columns_wrap_and_bound_the_height() -> None:
    disorder = {
        "pathophysiology": [
            {
                "name": "Root",
                "downstream": [{"target": f"Phenotype {i}"} for i in range(60)],
            }
        ],
        "phenotypes": [{"name": f"Phenotype {i}"} for i in range(60)],
    }
    thumb = render_thumbnail(build_causal_graph(disorder), max_rows=18)
    height = float(ET.fromstring(thumb.svg).attrib["viewBox"].split()[3])
    assert height <= 16 + 17 * 8 + 1
    assert thumb.phenotypes_connected == 60


def test_rendered_page_has_section_index_and_thumbnail(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Thumbnail_Disorder.yaml"
    disorder_path.write_text(yaml.safe_dump(DISORDER, sort_keys=False))
    output_path = tmp_path / "pages" / "Thumbnail_Disorder.html"
    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert 'class="stats-bar"' not in html
    assert '<nav class="page-index has-thumbnail"' in html
    assert '<a class="page-index-thumbnail" href="#pathograph"' in html
    assert '<svg class="pathograph-thumbnail"' in html
    assert "<b>1/2</b> phenotypes connected" in html
    # Biomarkers now have a pill and a card to jump to.
    assert '<a class="page-index-pill" href="#biochemical-markers">' in html
    assert '<div class="card" id="biochemical-markers">' in html
    # Pills follow page order.
    assert (
        html.index("<span>Pathophysiology</span>")
        < html.index("<span>Phenotypes</span>")
        < html.index("<span>Biomarkers</span>")
    )


def test_page_without_edges_has_no_thumbnail(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Bare.yaml"
    disorder_path.write_text(
        yaml.safe_dump({"name": "Bare", "phenotypes": [{"name": "Pain"}]})
    )
    output_path = tmp_path / "pages" / "Bare.html"
    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()
    assert '<nav class="page-index"' in html
    assert (
        "pathograph-thumbnail"
        not in html.split("<!-- Classifications -->")[0].split(
            '<nav class="page-index"'
        )[1]
    )


def test_cli_writes_svg(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Thumbnail_Disorder.yaml"
    disorder_path.write_text(yaml.safe_dump(DISORDER, sort_keys=False))
    out = tmp_path / "thumb.svg"
    result = CliRunner().invoke(
        app, ["pathograph-thumbnail", str(disorder_path), "-o", str(out)]
    )
    assert result.exit_code == 0, result.output
    assert out.read_text().startswith('<svg class="pathograph-thumbnail"')
    assert "1/2 phenotypes connected" in result.output


def test_cli_prints_svg_to_stdout(tmp_path: Path) -> None:
    disorder_path = tmp_path / "Thumbnail_Disorder.yaml"
    disorder_path.write_text(yaml.safe_dump(DISORDER, sort_keys=False))
    result = CliRunner().invoke(app, ["pathograph-thumbnail", str(disorder_path)])
    assert result.exit_code == 0, result.output
    assert '<svg class="pathograph-thumbnail"' in result.output
