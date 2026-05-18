"""Tests for literature summary rendering on disorder pages."""

from pathlib import Path

import yaml

from dismech.render import (
    collect_hypothesis_research_links,
    collect_literature_summaries,
    render_disorder,
)


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


def test_collect_literature_summaries_rebases_artifact_image_paths(
    tmp_path: Path,
) -> None:
    research_dir = tmp_path / "research"
    output_dir = tmp_path / "pages" / "disorders"
    research_dir.mkdir()
    output_dir.mkdir(parents=True)
    (research_dir / "Test_Disorder-deep-research-falcon.md").write_text(
        """---
provider: falcon
---
## Output

Summary.

## Artifacts

![Figure](Test_Disorder-deep-research-falcon_artifacts/image-1.png)
"""
    )

    results = collect_literature_summaries(
        "Test_Disorder",
        research_root=research_dir,
        output_dir=output_dir,
    )

    assert (
        "../../research/Test_Disorder-deep-research-falcon_artifacts/image-1.png"
        in results[0]["html"]
    )


def test_render_disorder_includes_rebased_literature_artifact_images(
    tmp_path: Path,
) -> None:
    disorder_path = tmp_path / "Test_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Test_Disorder.html"
    research_dir = tmp_path / "research"
    research_dir.mkdir()
    _write_disorder(disorder_path, {"name": "Test Disorder"})
    (research_dir / "Test_Disorder-deep-research-falcon.md").write_text(
        """---
provider: falcon
model: Edison Scientific Literature
citation_count: 1
---
## Output

# Disease Pathophysiology Research Report

Summary.

## Artifacts

![Figure](Test_Disorder-deep-research-falcon_artifacts/image-1.png)
"""
    )

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert (
        "../../research/Test_Disorder-deep-research-falcon_artifacts/image-1.png"
        in html
    )
    assert "<img" in html


def test_render_disorder_links_hypothesis_research_without_inlining(
    tmp_path: Path,
) -> None:
    disorder_dir = tmp_path / "kb" / "disorders"
    hypothesis_dir = (
        tmp_path / "kb" / "hypotheses" / "Wilsons_Disease" / "cuproptosis_model"
    )
    disorder_dir.mkdir(parents=True)
    hypothesis_dir.mkdir(parents=True)
    disorder_path = disorder_dir / "Wilsons_Disease.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Wilsons_Disease.html"
    _write_disorder(
        disorder_path,
        {
            "name": "Wilson Disease",
            "mechanistic_hypotheses": [
                {
                    "hypothesis_group_id": "cuproptosis_model",
                    "hypothesis_label": "Copper-Dependent Cuproptosis Model",
                    "status": "EMERGING",
                    "description": "Copper-dependent cell death may amplify injury.",
                    "evidence": [
                        {
                            "reference": "PMID:12345678",
                            "supports": "SUPPORT",
                            "snippet": "Cuproptosis can injure hepatocytes.",
                        }
                    ],
                }
            ],
            "pathophysiology": [
                {
                    "name": "Hepatic copper overload",
                    "description": "Copper accumulates in hepatocytes.",
                    "downstream": [
                        {
                            "target": "Mitochondrial cell injury",
                            "description": "Copper overload injures mitochondria.",
                            "hypothesis_groups": ["cuproptosis_model"],
                            "causal_link_type": "INDIRECT_UNKNOWN_INTERMEDIATES",
                        }
                    ],
                },
                {"name": "Mitochondrial cell injury"},
            ],
        },
    )
    (hypothesis_dir / "openscientist.md").write_text(
        """---
provider: openscientist
citation_count: 20
end_time: '2026-05-17T22:33:39Z'
---
# Hypothesis report

This full report body should stay out of the rendered disorder page.
"""
    )
    (hypothesis_dir / "openscientist.md.citations.md").write_text("# citations\n")

    render_disorder(disorder_path, output_path=output_path)
    html = output_path.read_text()

    assert 'id="mechanistic-hypotheses"' in html
    assert 'id="hypothesis-cuproptosis-model"' in html
    assert 'id="hypothesis-research"' not in html
    assert "Copper-Dependent Cuproptosis Model" in html
    assert "Pathograph links" in html
    assert 'href="#pathophysiology-hepatic-copper-overload"' in html
    assert 'href="#hypothesis-cuproptosis-model"' in html
    assert "OpenScientist" in html
    assert (
        "https://github.com/monarch-initiative/dismech/blob/main/"
        "kb/hypotheses/Wilsons_Disease/cuproptosis_model/openscientist.md"
    ) in html
    assert (
        "https://github.com/monarch-initiative/dismech/blob/main/"
        "kb/hypotheses/Wilsons_Disease/cuproptosis_model/"
        "openscientist.md.citations.md"
    ) in html
    assert "This full report body should stay out" not in html


def test_collect_hypothesis_research_links_uses_metadata_and_citations(
    tmp_path: Path,
) -> None:
    hypothesis_dir = (
        tmp_path / "kb" / "hypotheses" / "Test_Disorder" / "canonical_model"
    )
    hypothesis_dir.mkdir(parents=True)
    (hypothesis_dir / "falcon.md").write_text(
        """---
provider: falcon
citation_count: 3
---
Report body.
"""
    )
    (hypothesis_dir / "falcon.md.citations.md").write_text("# citations\n")

    links = collect_hypothesis_research_links(
        "Test_Disorder",
        [
            {
                "hypothesis_group_id": "canonical_model",
                "hypothesis_label": "Canonical Model",
                "status": "CANONICAL",
            }
        ],
        hypotheses_root=tmp_path / "kb" / "hypotheses",
    )

    assert len(links) == 1
    assert links[0]["hypothesis_label"] == "Canonical Model"
    assert links[0]["status"] == "CANONICAL"
    assert links[0]["reports"][0]["provider_label"] == "Falcon"
    assert links[0]["reports"][0]["citation_count"] == 3
    assert links[0]["reports"][0]["citations_href"].endswith(
        "kb/hypotheses/Test_Disorder/canonical_model/falcon.md.citations.md"
    )
