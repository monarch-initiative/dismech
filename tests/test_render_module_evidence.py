"""Evidence on module pathophysiology nodes (issue #10329).

A module abstracts a mechanism across diseases, often from model-system
evidence, so whether a node rests on a human cohort or a dish is the thing a
reader needs. Module pages showed only a count. Pathophysiology nodes now render
the same evidence expander as disorder pages, from the shared
``_evidence.html.j2`` partial; the model, readout and treatment sections keep
their count summary, which is a separate decision.
"""

import re
from pathlib import Path

import yaml

from dismech.render import render_module

NODE = "Reduced Calcium Influx"

_EVIDENCE = {
    "reference": "PMID:20427647",
    "supports": "SUPPORT",
    "evidence_source": "IN_VITRO",
    "snippet": "a quoted patch-clamp sentence",
    "explanation": "why it bears on the node",
}


def _render(tmp_path: Path, **extra) -> str:
    module = {
        "name": "Example Module",
        "category": "Module",
        "pathophysiology": [
            {
                "name": NODE,
                "description": "A node carrying the evidence under test.",
                "evidence": [_EVIDENCE],
            }
        ],
        **extra,
    }
    path = tmp_path / "example_module.yaml"
    path.write_text(yaml.safe_dump(module, sort_keys=False))
    disorders_dir = tmp_path / "kb" / "disorders"
    disorders_dir.mkdir(parents=True)
    out = tmp_path / "pages" / "modules" / "example_module.html"
    render_module(path, output_path=out, disorders_dir=disorders_dir)
    html = out.read_text()
    # The raw YAML preview repeats every snippet; assert on the rendered page.
    return re.sub(r'<pre class="yaml-preview">.*?</pre>', "", html, flags=re.DOTALL)


def test_pathophysiology_evidence_renders_with_source_badge(tmp_path: Path) -> None:
    html = _render(tmp_path)

    assert '<details class="evidence-details">' in html
    assert ">PMID:20427647</a>" in html
    assert 'class="evidence-source source-IN_VITRO"' in html
    assert 'class="evidence-support support-SUPPORT"' in html
    assert "a quoted patch-clamp sentence" in html


def test_module_page_carries_the_shared_evidence_styles(tmp_path: Path) -> None:
    html = _render(tmp_path)

    assert ".source-IN_VITRO" in html
    assert ".evidence-snippet" in html


def test_hypothesis_tally_styles_are_scoped(tmp_path: Path) -> None:
    """The tally reuses the evidence-support class names; unscoped, its pill
    rules would restyle the evidence-list badges (or the reverse)."""
    html = _render(tmp_path)

    assert ".hypothesis-evidence-balance .evidence-support {" in html
    assert (
        re.search(r"^\s*\.support-SUPPORT \{ background: #d1fae5", html, re.MULTILINE)
        is None
    )


def test_model_link_evidence_stays_a_count(tmp_path: Path) -> None:
    """Only pathophysiology nodes get the expander on module pages."""
    html = _render(
        tmp_path,
        animal_models=[
            {
                "name": "Example mouse",
                "species": "Mouse",
                "modeled_mechanisms": [
                    {
                        "target": NODE,
                        "relationship": "RECAPITULATES",
                        "evidence": [{**_EVIDENCE, "reference": "PMID:999"}],
                    }
                ],
            }
        ],
    )

    assert html.count('<details class="evidence-details">') == 1
    assert ">PMID:999</a>" not in html


def test_evidence_images_resolve_against_research(tmp_path: Path) -> None:
    """An artifact image src is relative to research/, as on disorder pages,
    not root-relative."""
    (tmp_path / "research").mkdir()
    image = {**_EVIDENCE, "images": ["Example_artifacts/fig1.png"]}
    html = _render(tmp_path, pathophysiology=[{"name": NODE, "evidence": [image]}])

    assert 'src="../../research/Example_artifacts/fig1.png"' in html
