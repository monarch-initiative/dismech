"""Tests for the structured-database reference-source framework.

The Orphanet flagship is exercised against the bulk XML files committed to
``data/orphadata/`` (gitignored, fetched via ``just refresh-orphadata``).
Tests are skipped automatically when the bulk data is absent.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.orphanet import OrphanetSource

REPO_ROOT = Path(__file__).parent.parent
ORPHADATA_DIR = REPO_ROOT / "data" / "orphadata"
MANIFEST = ORPHADATA_DIR / "MANIFEST.yaml"
PRODUCT1 = ORPHADATA_DIR / "en_product1.xml"


def _orphadata_available() -> bool:
    return PRODUCT1.exists() and MANIFEST.exists()


pytestmark = pytest.mark.skipif(
    not _orphadata_available(),
    reason="bulk Orphadata XML missing — run `just refresh-orphadata`",
)


@pytest.fixture(scope="module")
def orphanet_source() -> OrphanetSource:
    OrphanetSource.load_manifest(MANIFEST)
    src = OrphanetSource(ORPHADATA_DIR)
    # Force the index to populate so subsequent tests are fast.
    src.index()
    return src


def test_index_filters_to_leaf_disorders(orphanet_source: OrphanetSource):
    idx = orphanet_source.index()
    # We only emit Disorder + Subtype-of-disorder entries.
    groups = {rec.disorder_group for rec in idx.values()}
    assert groups <= {"Disorder", "Subtype of disorder"}
    # And we drop the pure-Category scaffolding nodes.
    types = {rec.disorder_type for rec in idx.values()}
    assert "Category" not in types
    # Sanity check: ~8.8k leaves.
    assert 8000 <= len(idx) <= 10000


def test_serialize_marfan_has_expected_blocks(orphanet_source: OrphanetSource):
    text = orphanet_source.serialize("558").render()
    # Frontmatter
    assert 'reference_id: "ORPHA:558"' in text
    assert 'title: "Marfan syndrome"' in text
    assert 'content_type: "structured_record"' in text
    # Body sections
    for header in [
        "## Identification",
        "## Definition",
        "## Inheritance",
        "## Phenotypes (HPO)",
        "## Cross-references",
        "## Source",
    ]:
        assert header in text, f"missing section {header!r}"
    # Tag-prefixed lines must be present so curators can quote them.
    assert "ID    ORPHA:558  Marfan syndrome" in text
    assert "INH   Autosomal dominant" in text
    # MONDO xref roundtrip
    assert "XREF   MONDO:0007947" in text


def test_serialize_is_byte_deterministic(orphanet_source: OrphanetSource):
    """Two consecutive serializations of the same ID must be byte-identical.

    Snippet validation depends on stable line content; nondeterminism (e.g.
    dict iteration order) would silently break curator-quoted snippets on
    the next refresh.
    """
    for code in ["558", "79318", "550", "63"]:
        a = orphanet_source.serialize(code).render()
        b = orphanet_source.serialize(code).render()
        assert a == b, f"non-deterministic serialization for ORPHA:{code}"


def test_cache_file_passes_frontmatter_contract(
    orphanet_source: OrphanetSource, tmp_path: Path
):
    """Generated cache files conform to dismech's deterministic cache contract."""
    path = orphanet_source.write_cache_file("558", tmp_path)
    assert check_cache_file(path) is None


def test_filename_matches_reference_id(orphanet_source: OrphanetSource):
    entry = orphanet_source.serialize("558")
    assert entry.filename() == "ORPHA_558.md"


def test_subtype_disorders_are_emitted(orphanet_source: OrphanetSource):
    """At least some subtype-of-disorder entries should be in the index."""
    idx = orphanet_source.index()
    subtypes = [r for r in idx.values() if r.disorder_group == "Subtype of disorder"]
    assert len(subtypes) > 100
