"""Tests for rendering disease-level ``external_assertions`` (issue #8044).

``ExternalAssertion`` is bound to both ``Variant`` and ``Disease``, but only the
variant card rendered it, so the registry records (Orphanet / OMIM / ClinGen /
CIViC) that 151 disorder files carry at the disease level reached no page at
all. Both placements now go through one shared macro.
"""

import re
from collections import Counter
from pathlib import Path

import yaml

from dismech.graph import build_causal_graph
from dismech.render import render_disorder

DISORDER = {
    "name": "Example Disease",
    "pathophysiology": [
        {"name": "CFTR Dysfunction", "downstream": [{"target": "Bronchiectasis"}]}
    ],
    "phenotypes": [{"name": "Bronchiectasis"}],
    "external_assertions": [
        {
            "name": "Orphanet example disease record",
            "source": "Orphanet",
            "assertion_type": "structured_disease_record",
            "external_id": "ORPHA:558",
            "url": "https://www.orpha.net/en/disease/detail/558",
            "description": "Orphanet structured record for the example disease.",
            "evidence": [
                {
                    "reference": "ORPHA:558",
                    "supports": "SUPPORT",
                    "evidence_source": "OTHER",
                    "snippet": "MONDO:0007947 | Exact",
                    "explanation": "The cross-reference table maps ORPHA:558.",
                }
            ],
        },
        {
            "name": "OMIM example disease record",
            "source": "OMIM",
            "assertion_type": "disease_record",
            "external_id": "OMIM:154700",
            "description": "OMIM entry for the example disease.",
            "notes": (
                "This external assertion is broader than the present entry, "
                "which isolates one branch."
            ),
        },
        {
            "name": "ClinGen validity assertion",
            "source": "ClinGen",
            "assertion_type": "gene_disease_validity",
            "external_id": "assertion_7f53d03d-2022-09-15T160000.000Z",
        },
    ],
}


def _render(tmp_path: Path, disorder: dict) -> str:
    disorder_path = tmp_path / "Example_Disease.yaml"
    disorder_path.write_text(yaml.safe_dump(disorder, sort_keys=False))
    output_path = tmp_path / "pages" / "disorders" / "Example_Disease.html"
    render_disorder(disorder_path, output_path=output_path)
    return output_path.read_text()


def test_disease_level_assertions_render_their_own_section(tmp_path: Path) -> None:
    """The gap this issue reports: disease-level assertions reach the page."""
    html = _render(tmp_path, DISORDER)
    assert '<div class="card" id="external-assertions">' in html
    assert "External Assertions" in html
    assert "Orphanet example disease record" in html
    assert "OMIM example disease record" in html
    assert "structured disease record" in html  # underscores are humanized
    assert "Orphanet structured record for the example disease." in html


def test_disease_level_assertion_evidence_renders(tmp_path: Path) -> None:
    """Assertion evidence goes through the standard evidence disclosure."""
    html = _render(tmp_path, DISORDER)
    assert "MONDO:0007947 | Exact" in html
    assert "The cross-reference table maps ORPHA:558." in html


def test_assertion_notes_render(tmp_path: Path) -> None:
    """`notes` is where a record's scope caveat lives, so it cannot be dropped.

    24 of the 212 disease-level records carry one, and on entries like
    `Aortic_Valve_Disease_2` it records that the external record is *broader*
    than the dismech entry -- without it the card contradicts the entry it
    sits on. No variant-level record carries `notes`, so rendering it here
    leaves variant output unchanged in practice as well as in intent.
    """
    html = _render(tmp_path, DISORDER)
    assert (
        "This external assertion is broader than the present entry, "
        "which isolates one branch." in html
    )


def test_assertion_identifier_linking(tmp_path: Path) -> None:
    """http(s) URLs link out; a bare CURIE falls back to the resolver chip."""
    html = _render(tmp_path, DISORDER)
    assert 'href="https://www.orpha.net/en/disease/detail/558"' in html
    # No URL curated, but OMIM:154700 is CURIE-shaped, so it still resolves
    # through the same prefix map every other identifier chip on the page uses.
    assert re.search(r'<a[^>]*class="curie-chip[^"]*"[^>]*>\s*OMIM:154700\s*</a>', html)
    # An opaque ClinGen assertion id is not CURIE-shaped and stays plain text.
    assert "assertion_7f53d03d-2022-09-15T160000.000Z" in html
    assert not re.search(
        r"<a[^>]*>\s*assertion_7f53d03d-2022-09-15T160000\.000Z\s*</a>", html
    )


def test_assertion_urls_are_scheme_guarded(tmp_path: Path) -> None:
    """A curated non-http URL must not become a clickable link."""
    disorder = dict(DISORDER)
    disorder["external_assertions"] = [
        {"name": "Bad link", "external_id": "XX1", "url": "javascript:alert(1)"}
    ]
    html = _render(tmp_path, disorder)
    assert "Bad link" in html
    assert "XX1" in html
    # The raw-YAML footer echoes the source, so assert on rendered links only.
    assert 'href="javascript:' not in html


def test_assertion_anchor_ids_are_unique(tmp_path: Path) -> None:
    """Two registry records that slugify alike still get distinct anchors."""
    disorder = dict(DISORDER)
    disorder["external_assertions"] = [
        {"name": "Registry record", "external_id": "ORPHA:1"},
        {"name": "Registry record", "external_id": "ORPHA:2"},
    ]
    html = _render(tmp_path, disorder)
    assertion_ids = re.findall(r'id="(external-assertion-[^"]*)"', html)
    assert len(assertion_ids) == 2
    assert len(set(assertion_ids)) == 2
    duplicates = [
        i for i, c in Counter(re.findall(r'\sid="([^"]+)"', html)).items() if c > 1
    ]
    assert not duplicates, f"duplicate element IDs on the page: {duplicates}"


def test_section_is_absent_without_assertions(tmp_path: Path) -> None:
    """No empty card when a disorder carries no disease-level assertions."""
    disorder = {k: v for k, v in DISORDER.items() if k != "external_assertions"}
    html = _render(tmp_path, disorder)
    assert '<div class="card" id="external-assertions">' not in html


def test_assertions_are_not_pathograph_nodes(tmp_path: Path) -> None:
    """Documents why the cards carry no data-dismech-node pair.

    ``dismech.graph`` emits no node for an external assertion, so there is no
    jump-to-card wiring to do (issue #8032/#8036); adding a name-keyed
    ``data-dismech-node`` would only give ``findCardForNode`` a wrong fallback
    target when an assertion happens to share a name with a real node.
    """
    graph = build_causal_graph(DISORDER)
    assert "Orphanet example disease record" not in graph.nodes
