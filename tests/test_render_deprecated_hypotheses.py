"""Rendering of superseded (DEPRECATED) mechanistic hypotheses.

A deprecated hypothesis is deliberately retained in the entry rather than
deleted (design decision 6a), so the rendered page has to say plainly that the
model is not the mechanism DisMech asserts. It also has to defuse the citation
count: a superseded hypothesis often carries more supporting than refuting
citations simply because the supporting literature accumulated first.
"""

from pathlib import Path

import yaml

from dismech.render import render_disorder

_DISORDER = {
    "name": "Retired Model Disorder",
    "mechanistic_hypotheses": [
        {
            "hypothesis_group_id": "live_model",
            "hypothesis_label": "The currently accepted model",
            "status": "CANONICAL",
            "description": "The model DisMech asserts.",
            "evidence": [
                {
                    "reference": "PMID:1",
                    "supports": "SUPPORT",
                    "snippet": "s",
                    "explanation": "e",
                }
            ],
        },
        {
            "hypothesis_group_id": "retired_model",
            "hypothesis_label": "The overturned model",
            "status": "DEPRECATED",
            "description": "Historical model, refuted.",
            # Deliberately support-heavy: the point of the balance row is that a
            # majority of SUPPORT citations does not confer standing.
            "evidence": [
                {
                    "reference": f"PMID:{n}",
                    "supports": "SUPPORT",
                    "snippet": "s",
                    "explanation": "e",
                }
                for n in (2, 3, 4)
            ]
            + [
                {
                    "reference": "PMID:5",
                    "supports": "REFUTE",
                    "snippet": "s",
                    "explanation": "e",
                }
            ],
        },
    ],
    "pathophysiology": [
        {
            "name": "Disputed Step",
            "mechanism_confidence": "HYPOTHETICAL",
            "description": "A node that exists only to carry the retired model.",
            "downstream": [
                {
                    "target": "Endpoint",
                    "causal_link_type": "INDIRECT_UNKNOWN_INTERMEDIATES",
                    "hypothesis_groups": ["retired_model"],
                }
            ],
        },
        {"name": "Endpoint", "description": "Downstream endpoint."},
    ],
}


def _render(tmp_path: Path) -> str:
    disorder_path = tmp_path / "Retired_Model_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Retired_Model_Disorder.html"
    disorder_path.write_text(yaml.safe_dump(_DISORDER, sort_keys=False))
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


def test_deprecated_hypothesis_renders_overturned_callout(tmp_path: Path) -> None:
    """The box must state that the model is not asserted as current mechanism."""
    html = _render(tmp_path)

    assert "hypothesis-deprecated" in html
    assert "Overturned model" in html
    assert "not as current mechanism" in html
    # The editorial stance on citation weight has to be stated, not implied.
    assert "Citation volume does not decide standing" in html


def test_live_hypothesis_has_no_overturned_callout(tmp_path: Path) -> None:
    """The callout must be scoped to DEPRECATED, not shown on every hypothesis."""
    html = _render(tmp_path)

    # One occurrence is the CSS rule; the callout itself adds exactly one more.
    assert html.count("hypothesis-overturned-title") == 2


def test_hypothesis_evidence_balance_is_rendered(tmp_path: Path) -> None:
    """Support/refute split is shown so citation asymmetry is visible."""
    html = _render(tmp_path)

    assert "Evidence balance" in html
    assert ">3 support<" in html
    assert ">1 refute<" in html


def test_deprecated_status_marks_hypothesis_chips(tmp_path: Path) -> None:
    """Nodes and edges in a retired group must not read as current mechanism."""
    html = _render(tmp_path)

    assert "tag-hypothesis-link-DEPRECATED" in html
    assert "retained for reference, not asserted as current mechanism" in html
