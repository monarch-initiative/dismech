"""A DOI fetched in a different capitalization must reuse its existing cache file.

DOIs resolve case-insensitively, but the reference fetcher derived the cache
filename from the DOI exactly as written, so on a case-sensitive filesystem the
second spelling wrote a second copy of the same paper (#9112). Seventeen such
pairs had accumulated in ``references_cache/`` before #11977 removed them.

The assertions compare directory listings and returned filenames rather than
``Path.exists()``, because on macOS ``exists()`` is true for any capitalization
of an existing file and would pass without the fix. The lookup tests fail without
the fix on every filesystem. The two save tests can only fail on a case-sensitive
one -- on macOS a second spelling overwrites the same file -- which is why they
sit beside the lookup tests rather than replacing them; CI runs on Linux.
"""

from pathlib import Path

import pytest
from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
from linkml_reference_validator.models import (
    ReferenceContent,
    ReferenceValidationConfig,
)

import dismech.patch_reference_validator  # noqa: F401  # side-effect: applies the patch
from dismech import doi_cache_case

MIXED = "DOI_10.1172_JCI89626.md"
CACHED_RECORD = """---
reference_id: DOI:10.1172/JCI89626
title: Mutations in sphingosine-1-phosphate lyase cause nephrosis with ichthyosis and adrenal insufficiency
journal: Journal of Clinical Investigation
year: '2017'
doi: 10.1172/JCI89626
content_type: abstract_only
full_text_attempted: true
---

# Mutations in sphingosine-1-phosphate lyase cause nephrosis

## Content

Abstract text.
"""


@pytest.fixture(autouse=True)
def _fresh_indexes():
    doi_cache_case.reset_indexes()
    yield
    doi_cache_case.reset_indexes()


def _fetcher(cache_dir: Path) -> ReferenceFetcher:
    return ReferenceFetcher(ReferenceValidationConfig(cache_dir=cache_dir, fetch_full_text=False))


def _doi_files(cache_dir: Path) -> list[str]:
    return sorted(p.name for p in cache_dir.iterdir() if p.name.upper().startswith("DOI_"))


def test_lowercase_lookup_finds_the_mixed_case_file(tmp_path):
    (tmp_path / MIXED).write_text(CACHED_RECORD, encoding="utf-8")

    path = _fetcher(tmp_path).get_cache_path("DOI:10.1172/jci89626")

    assert path.name == MIXED


def test_mixed_case_lookup_finds_the_lowercase_file(tmp_path):
    (tmp_path / "DOI_10.1172_jci89626.md").write_text(CACHED_RECORD, encoding="utf-8")

    path = _fetcher(tmp_path).get_cache_path("DOI:10.1172/JCI89626")

    assert path.name == "DOI_10.1172_jci89626.md"


def test_an_uncached_doi_keeps_the_capitalization_it_was_written_in(tmp_path):
    fetcher = _fetcher(tmp_path)

    assert fetcher.get_cache_path("DOI:10.7554/eLife.74270").name == "DOI_10.7554_eLife.74270.md"
    assert fetcher.get_cache_path("DOI:10.1056/nejmoa055262").name == "DOI_10.1056_nejmoa055262.md"


def test_non_doi_references_are_unaffected(tmp_path):
    (tmp_path / "PMID_12345678.md").write_text("---\nreference_id: PMID:12345678\n---\n")

    assert _fetcher(tmp_path).get_cache_path("PMID:12345678").name == "PMID_12345678.md"


def test_the_cached_record_loads_under_another_capitalization(tmp_path):
    """The read path: a lowercase citation is served from the mixed-case file."""
    (tmp_path / MIXED).write_text(CACHED_RECORD, encoding="utf-8")

    loaded = _fetcher(tmp_path)._load_from_disk("DOI:10.1172/jci89626")

    assert loaded is not None
    assert loaded.reference_id == "DOI:10.1172/JCI89626"


def test_saving_another_capitalization_does_not_write_a_second_file(tmp_path):
    """The write path, which calls ``_cache_path`` directly and skips ``get_cache_path``."""
    (tmp_path / MIXED).write_text(CACHED_RECORD, encoding="utf-8")

    _fetcher(tmp_path)._save_to_disk(
        ReferenceContent(
            reference_id="DOI:10.1172/jci89626",
            title="Mutations in sphingosine-1-phosphate lyase",
            content="Abstract text.",
            content_type="abstract_only",
        )
    )

    assert _doi_files(tmp_path) == [MIXED]


def test_a_doi_saved_in_this_process_is_reused_by_a_later_spelling(tmp_path):
    fetcher = _fetcher(tmp_path)
    fetcher._save_to_disk(
        ReferenceContent(reference_id="DOI:10.1172/JCI89626", title="t", content="c")
    )
    fetcher._save_to_disk(
        ReferenceContent(reference_id="DOI:10.1172/jci89626", title="t", content="c")
    )

    assert _doi_files(tmp_path) == [MIXED]


def test_the_cache_directory_is_listed_once_per_process(tmp_path, monkeypatch):
    (tmp_path / MIXED).write_text(CACHED_RECORD, encoding="utf-8")
    calls = []
    real_scandir = doi_cache_case.os.scandir

    def counting_scandir(path):
        calls.append(path)
        return real_scandir(path)

    monkeypatch.setattr(doi_cache_case.os, "scandir", counting_scandir)
    fetcher = _fetcher(tmp_path)
    for reference_id in ("DOI:10.1172/jci89626", "DOI:10.1172/JCI89626", "DOI:10.1/other"):
        fetcher.get_cache_path(reference_id)

    assert len(calls) == 1
