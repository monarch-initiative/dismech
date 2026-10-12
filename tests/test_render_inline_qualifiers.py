"""Qualifiers render inside the pill of the term they qualify (issue #13550).

As separate sibling pills, a modifier such as INCREASED wrapped onto its own
line in the narrow single-column module cards, so a reader could not tell
which process it belonged to.
"""

import re
from pathlib import Path

import yaml

from dismech.render import render_disorder, render_module

PROCESS = {
    "preferred_term": "apoptotic process",
    "term": {"id": "GO:0006915", "label": "apoptotic process"},
    "modifier": "INCREASED",
}
CELL = {
    "preferred_term": "hepatocyte",
    "term": {"id": "CL:0000182", "label": "hepatocyte"},
    "modifier": "DECREASED",
}


def _pills(html: str, tag_class: str, label: str) -> list[str]:
    """Return each `<span class="tag <tag_class>">` pill whose text has `label`.

    Pills nest only tag-qual / curie-chip / pill-tip spans, so matching to the
    first `</span>` that closes the pill itself is done by counting depth.
    """
    pills = []
    for m in re.finditer(rf'<span class="tag {tag_class}"[^>]*>', html):
        depth, i = 1, m.end()
        while depth:
            nxt = re.search(r"<span\b|</span>", html[i:])
            depth += 1 if nxt.group(0) == "<span" else -1
            i += nxt.end()
        pill = html[m.start() : i]
        if label in pill:
            pills.append(pill)
    return pills


def _assert_inline(
    html: str, tag_class: str, label: str, modifier: str, direction: str
) -> None:
    pills = _pills(html, tag_class, label)
    assert pills, f"no {tag_class} pill for {label}"
    for pill in pills:
        assert f'class="tag-qual tag-qual-{direction}"' in pill, pill
        assert modifier in pill, pill


def test_module_cards_put_the_modifier_inside_the_pill(tmp_path: Path) -> None:
    src = tmp_path / "modules" / "inline_qualifier_test.yaml"
    src.parent.mkdir(parents=True)
    src.write_text(
        yaml.safe_dump(
            {
                "name": "Inline Qualifier Test Module",
                "description": "Test module.",
                "category": "Module",
                "pathophysiology": [
                    {
                        "name": "Test Node",
                        "cell_types": [CELL],
                        "biological_processes": [PROCESS],
                    }
                ],
            },
            sort_keys=False,
        )
    )
    out = tmp_path / "module.html"
    render_module(src, output_path=out, usage_index={}, collections=[])
    html = out.read_text()

    _assert_inline(html, "tag-bio", "apoptotic process", "INCREASED", "up")
    _assert_inline(html, "tag-cell", "hepatocyte", "DECREASED", "down")
    # No free-standing modifier pill left beside the term.
    assert 'class="tag tag-modifier"' not in html


def test_disorder_pathophysiology_puts_the_modifier_inside_the_pill(
    tmp_path: Path,
) -> None:
    src = tmp_path / "Inline_Qualifier_Test.yaml"
    src.write_text(
        yaml.safe_dump(
            {
                "name": "Inline Qualifier Test",
                "pathophysiology": [
                    {
                        "name": "Test Node",
                        "cell_types": [CELL],
                        "biological_processes": [PROCESS],
                    }
                ],
            },
            sort_keys=False,
        )
    )
    out = tmp_path / "disorder.html"
    render_disorder(src, output_path=out)
    html = out.read_text()

    _assert_inline(html, "tag-bio", "apoptotic process", "INCREASED", "up")
    _assert_inline(html, "tag-cell", "hepatocyte", "DECREASED", "down")
