"""Tests for the DepMap structured-database source.

Unlike the ICEES/CIViC sources (whose bulk data is gitignored and fetched on
demand, so their tests skip when absent), this suite runs against a small
committed fixture TSV under ``tests/data/depmap/`` so the serialize path always
has CI coverage. The fixture rows are illustrative literature-established
relationships, not real DepMap statistics, and are never written into the
committed ``references_cache/`` — they only drive these unit tests.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.depmap import DepMapSource

REPO_ROOT = Path(__file__).parent.parent
FIXTURE_DIR = REPO_ROOT / "tests" / "data" / "depmap"
MANIFEST = REPO_ROOT / "data" / "depmap" / "MANIFEST.yaml"


@pytest.fixture(scope="module")
def depmap_source() -> DepMapSource:
    if MANIFEST.exists():
        DepMapSource.load_manifest(MANIFEST)
    src = DepMapSource(FIXTURE_DIR)
    src.index()
    return src


def test_identifiers_cover_single_and_pair(depmap_source: DepMapSource):
    ids = set(depmap_source.identifiers())
    # Single-gene selective dependencies
    assert "DEPMAP:PARP1" in ids
    assert "DEPMAP:WRN" in ids
    # Gene-pair synthetic lethality, symbols sorted
    assert "DEPMAP:MTAP__PRMT5" in ids
    assert "DEPMAP:SMARCA2__SMARCA4" in ids
    assert "DEPMAP:ARID1A__ARID1B" in ids
    # No unsorted duplicate of a pair leaks through
    assert "DEPMAP:PRMT5__MTAP" not in ids
    assert "DEPMAP:SMARCA4__SMARCA2" not in ids


def test_selective_dependency_aggregates_contexts(depmap_source: DepMapSource):
    entry = depmap_source.serialize("DEPMAP:PARP1")
    text = entry.render()
    assert entry.reference_id == "DEPMAP:PARP1"
    assert 'database: "DepMap"' in text
    assert 'content_type: "structured_record"' in text
    assert "## Selective dependency statistics" in text
    # Both PARP1 contexts aggregate into one cache file as quotable rows.
    assert "| BRCA1/BRCA2-mutant |" in text
    assert "| HRD-high |" in text
    # HGNC CURIE carried for machine linkage.
    assert "(hgnc:270)" in text


def test_pair_identity_is_order_independent(depmap_source: DepMapSource):
    a = depmap_source.serialize("MTAP,PRMT5").render()
    b = depmap_source.serialize("PRMT5,MTAP").render()
    c = depmap_source.serialize("DEPMAP:MTAP__PRMT5").render()
    assert a == b == c
    assert "Gene A: MTAP (hgnc:7154)" in a
    assert "Gene B: PRMT5 (hgnc:9265)" in a
    assert "COLLATERAL_LETHAL" in a


def test_bare_symbol_resolves(depmap_source: DepMapSource):
    entry = depmap_source.serialize("WRN")
    assert entry.reference_id == "DEPMAP:WRN"
    assert "MSI-high" in entry.render()


def test_cache_entry_matches_frontmatter_contract(
    depmap_source: DepMapSource, tmp_path: Path
):
    for ident in ("DEPMAP:PARP1", "DEPMAP:MTAP__PRMT5"):
        path = depmap_source.write_cache_file(ident, tmp_path)
        finding = check_cache_file(path)
        assert finding is None, f"frontmatter contract violation: {finding}"


def test_unknown_identifier_raises(depmap_source: DepMapSource):
    with pytest.raises(KeyError):
        depmap_source.serialize("DEPMAP:NOTAGENE")
