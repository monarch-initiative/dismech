"""Tests for the ICEES KG structured-database source.

The source is exercised against the bulk KGX files committed to
``data/icees-kg/`` (gitignored, fetched via ``just icees-refresh``). Tests are
skipped automatically when the bulk data is absent. The committed
``references_cache/ICEES_*.md`` files are additionally covered by the
deterministic frontmatter contract check in ``test_data.py``.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.icees import ICEESSource

REPO_ROOT = Path(__file__).parent.parent
ICEES_DIR = REPO_ROOT / "data" / "icees-kg"
MANIFEST = ICEES_DIR / "MANIFEST.yaml"
NODES = ICEES_DIR / "nodes.jsonl.gz"
EDGES = ICEES_DIR / "edges.jsonl.gz"


def _icees_available() -> bool:
    return NODES.exists() and EDGES.exists() and MANIFEST.exists()


pytestmark = pytest.mark.skipif(
    not _icees_available(),
    reason="bulk ICEES KG JSON-Lines missing — run `just icees-refresh`",
)


@pytest.fixture(scope="module")
def icees_source() -> ICEESSource:
    ICEESSource.load_manifest(MANIFEST)
    src = ICEESSource(ICEES_DIR)
    src.index()
    return src


def test_identifiers_are_mondo_hp_pairs(icees_source: ICEESSource):
    ids = list(icees_source.identifiers())
    assert ids, "expected at least one emitted pair"
    # Every emitted identifier is a sorted MONDO/HP disease/phenotype pair.
    for ref_id in ids:
        assert ref_id.startswith("ICEES:")
        a, b = ref_id.removeprefix("ICEES:").split("__")
        assert a.startswith(("MONDO_", "HP_"))
        assert b.startswith(("MONDO_", "HP_"))
        assert a <= b  # sorted, so the record is order-independent
    assert len(ids) == len(set(ids))


def test_serialize_asthma_copd_pair(icees_source: ICEESSource):
    # A "CURIE,CURIE" disease pair resolves to the canonical sorted id.
    entry = icees_source.serialize("MONDO:0005002,MONDO:0004979")
    text = entry.render()
    assert entry.reference_id == "ICEES:MONDO_0004979__MONDO_0005002"
    assert 'database: "ICEES KG"' in text
    assert 'content_type: "structured_record"' in text
    assert "## Cohort statistics" in text
    # Cohort rows are quotable substrings (the curator's evidence snippet).
    assert "| PCD_UNC_patient_2016_v6_binned_deidentified |" in text
    assert "infores:automat-icees-kg" in text


def test_pair_order_is_symmetric(icees_source: ICEESSource):
    a = icees_source.serialize("MONDO:0004979,MONDO:0005002").render()
    b = icees_source.serialize("MONDO:0005002,MONDO:0004979").render()
    assert a == b


def test_cache_entry_matches_frontmatter_contract(
    icees_source: ICEESSource, tmp_path: Path
):
    path = icees_source.write_cache_file(
        "ICEES:MONDO_0004979__MONDO_0005002", tmp_path
    )
    finding = check_cache_file(path)
    assert finding is None, f"frontmatter contract violation: {finding}"


def test_unknown_pair_raises(icees_source: ICEESSource):
    with pytest.raises(KeyError):
        icees_source.serialize("MONDO:9999999,MONDO:8888888")
