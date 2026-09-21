"""Rendering of the evidence `directness` badge (issue #7439).

`supports` says which way the evidence cuts; `directness` says how directly the
quoted text bears on the claim. They are separate axes, so the page has to show
them as separate things -- and specifically must not style an INDIRECT badge as
though it were a weaker or worse kind of support, which is the misreading the
retired PARTIAL value invited.

Most of the knowledge base has no directness assessment, so the common case is
the badge being absent entirely.
"""

from pathlib import Path

import yaml

from dismech.render import render_disorder


def _disorder(evidence: list[dict]) -> dict:
    return {
        "name": "Directness Test Disorder",
        "pathophysiology": [
            {
                "name": "A Mechanism",
                "description": "A node carrying the evidence under test.",
                "evidence": evidence,
            }
        ],
    }


def _render(tmp_path: Path, evidence: list[dict]) -> str:
    disorder_path = tmp_path / "Directness_Test_Disorder.yaml"
    output_path = tmp_path / "pages" / "disorders" / "Directness_Test_Disorder.html"
    disorder_path.write_text(yaml.safe_dump(_disorder(evidence), sort_keys=False))
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


_BASE = {
    "reference": "PMID:1",
    "supports": "SUPPORT",
    "snippet": "a quoted sentence",
    "explanation": "why it bears on the claim",
}


def test_directness_renders_as_its_own_badge(tmp_path: Path) -> None:
    html = _render(tmp_path, [{**_BASE, "directness": "INDIRECT"}])

    assert '<span class="evidence-directness"' in html
    assert ">INDIRECT</span>" in html
    # The direction badge is still there and unchanged: the two are additive.
    assert 'class="evidence-support support-SUPPORT"' in html


def test_directness_is_absent_when_unassessed(tmp_path: Path) -> None:
    """No badge at all rather than a default -- absent means nobody assessed it."""
    html = _render(tmp_path, [_BASE])

    assert '<span class="evidence-directness"' not in html
    assert 'class="evidence-support support-SUPPORT"' in html


def test_directness_badge_is_not_styled_as_a_support_grade(tmp_path: Path) -> None:
    """It must not reuse the coloured support-* pills.

    An INDIRECT quote can come from a large, well-controlled study. Colouring it
    like a downgraded SUPPORT would reassert exactly the strength reading that
    splitting the enum was meant to remove.
    """
    html = _render(tmp_path, [{**_BASE, "directness": "INDIRECT"}])

    assert 'class="evidence-directness"' in html
    assert 'class="evidence-support support-INDIRECT"' not in html
    assert ".support-INDIRECT" not in html


def test_retired_support_values_have_no_styling_left(tmp_path: Path) -> None:
    """PARTIAL and WRONG_STATEMENT are gone; their CSS must not linger."""
    html = _render(tmp_path, [_BASE])

    assert ".support-PARTIAL" not in html
    assert ".support-WRONG_STATEMENT" not in html
