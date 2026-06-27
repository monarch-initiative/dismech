"""Tests for the Genomics England PanelApp structured-database source.

The source is exercised against the JSON-Lines snapshot built into
``data/panelapp/`` (gitignored, produced by ``just panelapp-refresh``). Tests
that need the snapshot are skipped automatically when it is absent. The
snapshot-free tests cover pure projection/serialization logic against a small
synthetic snapshot written to a tmp dir. The committed
``references_cache/PANELAPP_*.md`` files are additionally covered by the
deterministic frontmatter contract check in ``test_data.py``.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.panelapp import (
    PanelAppSource,
    _record_from_gene,
)

REPO_ROOT = Path(__file__).parent.parent
PANELAPP_DIR = REPO_ROOT / "data" / "panelapp"
MANIFEST = PANELAPP_DIR / "MANIFEST.yaml"
SNAPSHOT = PANELAPP_DIR / "panelapp_snapshot.jsonl"


# A minimal PanelApp /genes/ API entry (HMBS on the acute intermittent
# porphyria panel) used by the snapshot-free tests.
_SAMPLE_GENE = {
    "entity_name": "HMBS",
    "entity_type": "gene",
    "confidence_level": "3",
    "mode_of_inheritance": "BOTH monoallelic and biallelic",
    "phenotypes": [
        "Porphyria, acute intermittent, OMIM:176000",
        "acute intermittent porphyria, MONDO:0008294",
    ],
    "evidence": ["NHS GMS", "Expert Review Green"],
    "publications": ["27539938", "1577472"],
    "gene_data": {
        "hgnc_id": "HGNC:4982",
        "gene_symbol": "HMBS",
        "omim_gene": ["609806"],
    },
    "panel": {
        "id": 1207,
        "name": "Acute intermittent porphyria",
        "version": "2.2",
        "disease_group": "Gastrohepatology",
        "disease_sub_group": "",
        "relevant_disorders": ["R169", "GT220"],
    },
}


@pytest.fixture
def synthetic_source(tmp_path: Path) -> PanelAppSource:
    """A source backed by a one-record synthetic snapshot in a tmp dir."""
    record = _record_from_gene(_SAMPLE_GENE)
    (tmp_path / "panelapp_snapshot.jsonl").write_text(
        json.dumps(record, sort_keys=True) + "\n", encoding="utf-8"
    )
    PanelAppSource._manifest_snapshot_date = "2026-06-27"
    return PanelAppSource(tmp_path)


def test_record_from_gene_projects_key_fields():
    record = _record_from_gene(_SAMPLE_GENE)
    assert record["panel_id"] == 1207
    assert record["gene_symbol"] == "HMBS"
    assert record["hgnc_id"] == "HGNC:4982"
    assert record["confidence_level"] == "3"
    assert "acute intermittent porphyria, MONDO:0008294" in record["phenotypes"]


def test_record_from_gene_skips_incomplete_entries():
    assert _record_from_gene({"panel": {"id": 1}}) is None  # no gene symbol
    assert _record_from_gene({"entity_name": "X", "panel": {}}) is None  # no panel id


def test_identifier_and_serialize(synthetic_source: PanelAppSource):
    ids = list(synthetic_source.identifiers())
    assert ids == ["PANELAPP:1207_HMBS"]

    entry = synthetic_source.serialize("PANELAPP:1207_HMBS")
    text = entry.render()
    assert entry.reference_id == "PANELAPP:1207_HMBS"
    assert 'database: "PanelApp"' in text
    assert 'content_type: "structured_record"' in text
    # The gene-panel row is the quotable d2g evidence snippet.
    assert (
        "| HMBS | HGNC:4982 | Acute intermittent porphyria | 1207 | 2.2 "
        "| Green (3) | BOTH monoallelic and biallelic |"
    ) in text
    # Phenotype rows (with embedded MONDO) are also quotable substrings.
    assert "| acute intermittent porphyria, MONDO:0008294 |" in text
    assert "PMID:27539938" in text
    # The overlap caveat is always present.
    assert "complementary panel-level signal" in text


def test_serialize_accepts_bare_identifier(synthetic_source: PanelAppSource):
    a = synthetic_source.serialize("PANELAPP:1207_HMBS").render()
    b = synthetic_source.serialize("1207_HMBS").render()
    assert a == b


def test_unknown_identifier_raises(synthetic_source: PanelAppSource):
    with pytest.raises(KeyError):
        synthetic_source.serialize("PANELAPP:9999_NOPE")


def test_cache_entry_matches_frontmatter_contract(
    synthetic_source: PanelAppSource, tmp_path: Path
):
    out_dir = tmp_path / "cache"
    path = synthetic_source.write_cache_file("PANELAPP:1207_HMBS", out_dir)
    finding = check_cache_file(path)
    assert finding is None, f"frontmatter contract violation: {finding}"


@pytest.mark.skipif(
    not (SNAPSHOT.exists() and MANIFEST.exists()),
    reason="PanelApp snapshot missing — run `just panelapp-refresh`",
)
def test_real_snapshot_identifiers_are_well_formed():
    PanelAppSource.load_manifest(MANIFEST)
    src = PanelAppSource(PANELAPP_DIR)
    ids = list(src.identifiers())
    assert ids, "expected at least one gene-panel association"
    assert len(ids) == len(set(ids))
    for ref_id in ids[:50]:
        assert src.id_pattern.match(ref_id)
