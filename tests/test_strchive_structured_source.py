"""Tests for the STRchive structured-database source.

The source is exercised against the bulk ``STRchive-loci.json`` committed to
``data/strchive/`` (gitignored, fetched via ``just strchive-refresh``). Tests
are skipped automatically when the bulk data is absent. The committed
``references_cache/STRCHIVE_*.md`` files are additionally covered by the
deterministic frontmatter contract check in ``test_data.py``.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.strchive import StrchiveSource

REPO_ROOT = Path(__file__).parent.parent
STRCHIVE_DIR = REPO_ROOT / "data" / "strchive"
MANIFEST = STRCHIVE_DIR / "MANIFEST.yaml"
LOCI = STRCHIVE_DIR / "STRchive-loci.json"


def _strchive_available() -> bool:
    return LOCI.exists() and MANIFEST.exists()


pytestmark = pytest.mark.skipif(
    not _strchive_available(),
    reason="bulk STRchive-loci.json missing — run `just strchive-refresh`",
)


@pytest.fixture(scope="module")
def strchive_source() -> StrchiveSource:
    StrchiveSource.load_manifest(MANIFEST)
    src = StrchiveSource(STRCHIVE_DIR)
    src.index()
    return src


def test_identifiers_are_prefixed_and_unique(strchive_source: StrchiveSource):
    ids = list(strchive_source.identifiers())
    assert ids, "expected at least one emitted locus"
    for ref_id in ids:
        assert ref_id.startswith("STRCHIVE:")
    assert len(ids) == len(set(ids))
    assert ids == sorted(ids)


def test_serialize_sca3_locus(strchive_source: StrchiveSource):
    entry = strchive_source.serialize("STRCHIVE:SCA3_ATXN3")
    text = entry.render()
    assert entry.reference_id == "STRCHIVE:SCA3_ATXN3"
    assert 'database: "STRchive"' in text
    assert 'content_type: "structured_record"' in text
    # The mechanistically critical rows are quotable evidence substrings.
    assert "## Repeat-count thresholds" in text
    assert "| Pathogenic | 60 | 87 |" in text
    assert "| Reference motif (reference orientation) | CTG |" in text
    # Cross-reference rows are quotable per-row.
    assert "| MONDO | MONDO:0007182 |" in text
    # CC BY 4.0 attribution is present.
    assert "CC BY 4.0" in text


def test_bare_locus_id_accepted(strchive_source: StrchiveSource):
    # The serializer accepts an id with or without the STRCHIVE: prefix.
    a = strchive_source.serialize("SCA3_ATXN3").render()
    b = strchive_source.serialize("STRCHIVE:SCA3_ATXN3").render()
    assert a == b


def test_additional_literature_excluded(strchive_source: StrchiveSource):
    # The high-volume tracking bibliography is not dumped into the body; the
    # curated reference list is. SCA3 has hundreds of additional_literature
    # PMIDs but only a short curated references list.
    text = strchive_source.serialize("STRCHIVE:SCA3_ATXN3").render()
    rec = strchive_source.index()["SCA3_ATXN3"].data
    extra = rec.get("additional_literature") or []
    assert len(extra) > 50  # sanity: SCA3 really does carry a long bibliography
    # The bibliography list is not dumped. A few of its PMIDs may still appear
    # because they are cited inline in the mechanism/details prose (e.g. a
    # disease-modifier reference), but the overwhelming majority must be absent.
    curated = set(rec.get("references") or [])
    extra_only = [p for p in extra if p not in curated]
    present = [p for p in extra_only if p in text]
    assert len(present) < 0.05 * len(extra_only), (
        f"too much of additional_literature appears in the body: "
        f"{len(present)}/{len(extra_only)}"
    )


def test_cache_entry_matches_frontmatter_contract(
    strchive_source: StrchiveSource, tmp_path: Path
):
    path = strchive_source.write_cache_file("STRCHIVE:SCA3_ATXN3", tmp_path)
    finding = check_cache_file(path)
    assert finding is None, f"frontmatter contract violation: {finding}"


def test_unknown_locus_raises(strchive_source: StrchiveSource):
    with pytest.raises(KeyError):
        strchive_source.serialize("STRCHIVE:NOT_A_REAL_LOCUS")
