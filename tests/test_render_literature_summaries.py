"""Tests for literature summary rendering on disorder pages."""

from pathlib import Path

import yaml

from dismech.render import collect_literature_summaries, render_disorder


def _write_disorder(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_collect_literature_summaries_extracts_report_body_and_metadata(
    tmp_path: Path,
) -> None:
    research_dir = tmp_path / "research"
    research_dir.mkdir()
    (research_dir / "Test_Disorder-deep-research-falcon.md").write_text(
        """---
provider: falcon
model: Edison Scientific Literature
citation_count: 12
end_time: '2026-04-07T10:00:00Z'
---
## Question

Prompt scaffold.

## Output

# Disease Pathophysiology Research Template

Prompt scaffold that should not render.

Disease Pathophysiology Research Report

## Pathophysiology description
Actual summary with **signal**.

| Marker | Effect |
|---|---|
| HIF | up |
"""
    )
    (research_dir / "Test_Disorder-deep-research-falcon.md.citations.md").write_text(
        "# citations\n"
    )

    results = collect_literature_summaries(
        "Test_Disorder",
        research_root=research_dir,
    )

    assert len(results) == 1
    assert results[0]["title"] == "Falcon"
    assert results[0]["citation_count"] == 12
    assert results[0]["end_time"] == "2026-04-07T10:00:00Z"
    assert "Actual summary with <strong>signal</strong>." in results[0]["html"]
    assert "<table>" in results[0]["html"]
    assert "Prompt scaffold that should not render." not in results[0]["html"]


def test_render_disorder_inlines_nearby_literature_summaries(
    tmp_path: Path,
) -> None:
    disorder_path = tmp_path / "Test_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Test_Disorder.html"
    research_dir = tmp_path / "research"
    research_dir.mkdir()
    _write_disorder(disorder_path, {"name": "Test Disorder"})
    (research_dir / "Test_Disorder-deep-research-cyberian-codex.md").write_text(
        """---
provider: cyberian-codex
model: codex-local-synthesis
citation_count: 7
---
## Question

        Codex secondary synthesis.

        ## Output

        ### Disorder
        - Name: Test Disorder

        ### Key Pathophysiology Nodes
        - Calcium signaling
- Epithelial stress
"""
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert 'id="references-deep-research"' in html
    assert 'id="literature-summaries"' in html
    assert "References &amp; Deep Research" in html
    assert "Deep Research" in html
    assert "Cyberian Codex" in html
    assert "codex-local-synthesis" in html
    assert "Calcium signaling" in html
    assert "Codex secondary synthesis." not in html


def test_render_disorder_places_references_and_deep_research_last(
    tmp_path: Path,
) -> None:
    disorder_path = tmp_path / "Test_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Test_Disorder.html"
    research_dir = tmp_path / "research"
    reports_dir = tmp_path / "reports" / "Test_Disorder"
    research_dir.mkdir()
    reports_dir.mkdir(parents=True)
    _write_disorder(
        disorder_path,
        {
            "name": "Test Disorder",
            "references": [
                {
                    "reference": "PMID:12345678",
                    "title": "Reference title",
                    "findings": [],
                }
            ],
        },
    )
    (research_dir / "Test_Disorder-deep-research-openai.md").write_text(
        """---
provider: openai
---
## Output

## Pathophysiology description
Deep research body.
"""
    )
    (reports_dir / "01-report.md").write_text("# Report\n\nReport body.\n")

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert html.index('stat-label">Reports') < html.index('stat-label">References')
    assert html.index('stat-label">References') < html.index(
        'stat-label">Deep Research'
    )
    assert html.index('id="reports"') < html.index('id="yamlContent"')
    assert html.index('id="yamlContent"') < html.index('id="references-deep-research"')
    assert html.index('id="references"') < html.index('id="literature-summaries"')
    assert html.index('id="references-deep-research"') < html.index(
        '<footer class="page-footer">'
    )
