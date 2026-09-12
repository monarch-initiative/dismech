"""Phenotype cards must not repeat their own title as an ontology label (#8402).

A phenotype card's title is curator free text and its bound term carries its
own label, so the two very often say the same thing -- ``name: Severe global
developmental delay`` against ``HP:0001263 Global developmental delay``. The
grouped renderer used to print both, at the same size and colour, with nothing
between them, so the card read "Severe global developmental delay Global
developmental delay".

The rule these tests pin down: drop the label when the title already contains
it, and when it does add something, mark it up as its own pill so it can never
be mistaken for a continuation of the title.
"""

import html as html_lib
import re
from pathlib import Path

import yaml

from dismech.render import render_disorder

# The grouped renderer -- the one the bug was reported against -- only kicks in
# when a disorder has more than one phenotype category, hence two categories.
DISORDER = {
    "name": "Example Disease",
    "phenotypes": [
        {
            "name": "Severe global developmental delay",
            "category": "Neurologic",
            "phenotype_term": {
                "preferred_term": "Global developmental delay",
                "term": {"id": "HP:0001263", "label": "Global developmental delay"},
            },
        },
        {
            "name": "Infantile seizures",
            "category": "Neurologic",
            "phenotype_term": {"term": {"id": "HP:0001250", "label": "Seizure"}},
        },
        {
            "name": "Spastic tetraplegia",
            "category": "Neurologic",
            "phenotype_term": {
                "term": {"id": "HP:0002510", "label": "Spastic tetraplegia"}
            },
        },
        {
            "name": "Ventricular pre-excitation",
            "category": "Neurologic",
            "phenotype_term": {
                "term": {"id": "HP:0004309", "label": "Ventricular preexcitation"}
            },
        },
        {
            "name": "Congenital microcephaly",
            "category": "Craniofacial",
            "phenotype_term": {
                "term": {"id": "HP:0011451", "label": "Primary microcephaly"}
            },
        },
        {
            "name": "Unbound finding",
            "category": "Craniofacial",
        },
    ],
}

CARD_RE = re.compile(
    r'<div class="item-box phenotype-box[^>]*data-dismech-node="([^"]*)"'
    r'[^>]*>\s*<div class="item-name">(.*?)</div>',
    re.DOTALL,
)


def _render(tmp_path: Path, disorder: dict) -> str:
    disorder_path = tmp_path / "Example_Disease.yaml"
    disorder_path.write_text(yaml.safe_dump(disorder, sort_keys=False))
    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


def _card_titles(html: str) -> dict[str, str]:
    """Map each card's phenotype name to its whole heading, flattened to text.

    Tooltips are stripped first: they legitimately restate the term label, and
    they are not part of what the reader sees before hovering.
    """
    titles = {}
    for node, block in CARD_RE.findall(html):
        block = re.sub(r'<span class="pill-tip".*?</span>', "", block, flags=re.DOTALL)
        text = html_lib.unescape(re.sub(r"<[^>]+>", " ", block))
        titles[html_lib.unescape(node)] = " ".join(text.split())
    return titles


def test_label_contained_in_the_title_is_not_repeated(tmp_path: Path) -> None:
    titles = _card_titles(_render(tmp_path, DISORDER))

    # The two cards from the issue report, plus the exact-match case.
    assert titles["Severe global developmental delay"] == (
        "Severe global developmental delay HP:0001263"
    )
    # "Seizure" is a substring of "Infantile seizures" once cased down, so the
    # plural does not smuggle the repetition back in.
    assert titles["Infantile seizures"] == "Infantile seizures HP:0001250"
    assert titles["Spastic tetraplegia"] == "Spastic tetraplegia HP:0002510"
    # Hyphenation is not a difference worth printing the label over.
    assert titles["Ventricular pre-excitation"] == (
        "Ventricular pre-excitation HP:0004309"
    )


def test_label_that_adds_meaning_survives_as_its_own_pill(tmp_path: Path) -> None:
    html = _render(tmp_path, DISORDER)
    titles = _card_titles(html)

    # "Primary microcephaly" is a genuinely different claim from "Congenital
    # microcephaly", so suppressing it would lose the binding the curator made.
    assert titles["Congenital microcephaly"] == (
        "Congenital microcephaly Primary microcephaly HP:0011451"
    )
    assert '<span class="phenotype-term-label">Primary microcephaly</span>' in html, (
        "a surviving label must carry the class that styles it apart from the title"
    )


def test_curie_is_never_printed_twice(tmp_path: Path) -> None:
    """A term with no label used to fall back to its own ID, next to the chip."""
    disorder = {
        "name": "Example Disease",
        "phenotypes": [
            {
                "name": "Labelless finding",
                "category": "Neurologic",
                "phenotype_term": {"term": {"id": "HP:0001250"}},
            },
            {"name": "Other finding", "category": "Craniofacial"},
        ],
    }
    titles = _card_titles(_render(tmp_path, disorder))
    assert titles["Labelless finding"] == "Labelless finding HP:0001250"


def test_unbound_phenotype_renders_its_title_alone(tmp_path: Path) -> None:
    titles = _card_titles(_render(tmp_path, DISORDER))
    assert titles["Unbound finding"] == "Unbound finding"
