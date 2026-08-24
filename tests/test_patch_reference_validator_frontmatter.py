"""Regression tests for the delimiter-aware cache loader patch (issue #7697).

Before the patch, ``ReferenceFetcher._load_markdown_format`` split frontmatter on
the ``---`` *substring*. These tests use the two real titles that break it and
assert that every frontmatter field survives the round trip.
"""

from __future__ import annotations

import pytest

import dismech.patch_reference_validator  # noqa: F401  (applies the patch on import)

pytest.importorskip("linkml_reference_validator")

from linkml_reference_validator.etl.reference_fetcher import (
    ReferenceFetcher,
)
from linkml_reference_validator.models import (
    ReferenceValidationConfig,
)

from tests.test_frontmatter import MMWR_CACHE, NLM_ARROW_CACHE


@pytest.fixture
def fetcher(tmp_path):
    config = ReferenceValidationConfig(cache_dir=tmp_path)
    return ReferenceFetcher(config)


def test_patch_is_applied():
    assert getattr(ReferenceFetcher, "_frontmatter_split_patch_applied", False)


def test_quoted_triple_hyphen_title_no_longer_crashes(fetcher):
    """PMID:20881935 shape: previously an unhandled ScannerError killed the run."""
    content = fetcher._load_markdown_format(MMWR_CACHE, "PMID:20881935")

    assert content is not None
    assert content.title == "Human rabies---Virginia, 2009."
    assert content.reference_id == "PMID:20881935"
    assert content.journal == "MMWR Morb Mortal Wkly Rep"
    assert content.year == "2010"
    assert content.content_type == "abstract_only"
    assert content.authors == ["Centers for Disease Control and Prevention (CDC)"]
    assert "The patient died on November 20." in content.content


def test_unquoted_triple_hyphen_title_no_longer_truncates(fetcher):
    """PMID:1899320 shape: previously parsed silently, losing title and metadata."""
    content = fetcher._load_markdown_format(NLM_ARROW_CACHE, "PMID:1899320")

    assert content is not None
    # The whole title, not "Rapid detection of the A".
    assert content.title == "Rapid detection of the A----G(8344) mutation of mtDNA."
    # Every field that used to fall past the naive split point.
    assert content.authors == ["Zeviani M"]
    assert content.journal == "Am J Hum Genet"
    assert content.year == "1991"
    assert content.keywords == ["Humans"]
    assert content.content_type == "abstract_only"
    assert "widespread" in content.content


def test_ordinary_cache_file_is_unaffected(fetcher):
    """Files without '---' in frontmatter take the early return, byte-identical."""
    ordinary = (
        "---\n"
        'reference_id: "PMID:12345678"\n'
        'title: "An ordinary paper"\n'
        "authors:\n"
        "- Doe J\n"
        "journal: Example Journal\n"
        "year: '2024'\n"
        "content_type: abstract_only\n"
        "---\n"
        "\n"
        "## Content\n"
        "\n"
        "Body text.\n"
    )
    content = fetcher._load_markdown_format(ordinary, "PMID:12345678")

    assert content is not None
    assert content.title == "An ordinary paper"
    assert content.journal == "Example Journal"
    assert "Body text." in content.content


def test_restored_scalar_authors_are_list_wrapped_like_upstream(fetcher):
    """A held-back field must come back shaped the way upstream would shape it.

    Upstream wraps a scalar ``authors``/``keywords`` into a list and stringifies
    ``year``. Restoring the raw parsed value would hand callers a bare ``str``
    where the rest of the codebase is promised ``list[str]``.
    """
    text = (
        "---\n"
        'reference_id: "PMID:1899320"\n'
        "title: A----G(8344) arrow title.\n"
        "authors: Zeviani M---Amati P\n"
        "keywords: 5'----3'\n"
        "journal: Am J Hum Genet\n"
        "---\n"
        "\n"
        "## Content\n"
        "\n"
        "Body text.\n"
    )
    content = fetcher._load_markdown_format(text, "PMID:1899320")

    assert content is not None
    assert content.authors == ["Zeviani M---Amati P"]
    assert content.keywords == ["5'----3'"]
    assert content.title == "A----G(8344) arrow title."


def test_committed_cache_record_round_trips(fetcher):
    """The real file on main loads with its full title and metadata."""
    from pathlib import Path

    path = Path(__file__).parent.parent / "references_cache" / "PMID_1899320.md"
    if not path.exists():  # pragma: no cover - corpus may be pruned
        pytest.skip("PMID_1899320.md not present in this checkout")

    content = fetcher._load_markdown_format(
        path.read_text(encoding="utf-8"), "PMID:1899320"
    )

    assert content is not None
    assert content.title is not None
    assert content.title.startswith("Rapid detection of the A----G(8344)")
    # These are exactly the fields the naive split used to discard.
    assert content.authors
    assert content.journal
    assert content.content_type == "abstract_only"
