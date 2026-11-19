"""dismech's cache lookups agree with the validator's cache filenames.

From linkml-reference-validator 0.5.0 a cache filename over 200 bytes is cut
and ends in a hash of the reference id (linkml/linkml-reference-validator#132),
so the old local rule of replacing ``:/?=`` with ``_`` no longer finds it.
"""

from pathlib import Path

from linkml_reference_validator.cache import cache_filename

from dismech.reference_cache_frontmatter import resolve_cache_file
from dismech.reference_cache_names import cache_filenames
from dismech.reference_snippet_audit import CachedReferenceIndex

LONG_URL = (
    "url:https://www.cureus.com/articles/106741-homozygous-unc13a-variant-in-an-"
    "infant-with-congenital-encephalopathy-and-severe-neuromuscular-phenotype-a-"
    "case-report-with-detailed-central-nervous-system-neuropathologic-findings"
)


def _write(cache_dir: Path, reference_id: str) -> Path:
    path = cache_dir / cache_filename(reference_id)
    path.write_text(
        f"---\nreference_id: {reference_id}\ncontent_type: abstract_only\n---\n\n"
        "## Content\n\nSome cached text.\n",
        encoding="utf-8",
    )
    return path


def test_long_url_filename_is_capped_and_hashed():
    name = cache_filenames(LONG_URL)[0]
    assert len(name.encode("utf-8")) <= 200
    assert name.endswith("_70c868fd5a31a7c6.md")


def test_frontmatter_lookup_finds_a_capped_filename(tmp_path):
    path = _write(tmp_path, LONG_URL)
    assert resolve_cache_file(tmp_path, LONG_URL) == path


def test_snippet_audit_finds_a_capped_filename(tmp_path):
    path = _write(tmp_path, LONG_URL)
    assert CachedReferenceIndex(tmp_path).resolve_cache_path(LONG_URL) == path


def test_committed_long_url_cache_files_use_the_validators_names():
    """No committed cache file still carries an uncapped name over 200 bytes."""
    too_long = [
        p.name
        for p in Path("references_cache").glob("*.md")
        if len(p.name.encode("utf-8")) > 200
    ]
    assert too_long == []
