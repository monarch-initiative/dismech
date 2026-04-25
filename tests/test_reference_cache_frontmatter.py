"""Tests for deterministic reference cache frontmatter checks (issue #871)."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import (
    Finding,
    check_cache_file,
    scan_cache_dir,
)

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "references_cache"


def test_check_cache_file_accepts_valid_cache(tmp_path: Path):
    good = tmp_path / "PMID_12345678.md"
    good.write_text(
        "---\n"
        'reference_id: "PMID:12345678"\n'
        'title: "A real paper"\n'
        "authors:\n"
        "- Doe J\n"
        "- Roe K\n"
        "journal: Example Journal\n"
        "year: '2024'\n"
        "doi: 10.1234/example\n"
        "content_type: abstract_only\n"
        "---\n\n"
        "# A real paper\n",
        encoding="utf-8",
    )
    assert check_cache_file(good) is None


def test_check_cache_file_reports_malformed_yaml(tmp_path: Path):
    broken = tmp_path / "PMID_88888888.md"
    broken.write_text(
        "---\n"
        "authors:\n"
        "- A\n"
        'doi: "!!python/object/new:Bio.Entrez.Parser.StringElement"\n'
        "  args:\n"
        "  - 10.1/foo\n"
        "---\n",
        encoding="utf-8",
    )
    finding = check_cache_file(broken)
    assert isinstance(finding, Finding)
    assert any("invalid YAML frontmatter" in reason for reason in finding.reasons)


def test_check_cache_file_requires_reference_id_and_content_type(tmp_path: Path):
    bad = tmp_path / "PMID_12345678.md"
    bad.write_text(
        '---\nreference_id: "PMID:12345678"\n---\n',
        encoding="utf-8",
    )
    finding = check_cache_file(bad)
    assert isinstance(finding, Finding)
    assert any("content_type" in reason for reason in finding.reasons)


def test_check_cache_file_rejects_unknown_fields(tmp_path: Path):
    bad = tmp_path / "PMID_12345678.md"
    bad.write_text(
        "---\n"
        'reference_id: "PMID:12345678"\n'
        "content_type: abstract_only\n"
        "mystery_field: nope\n"
        "---\n",
        encoding="utf-8",
    )
    finding = check_cache_file(bad)
    assert isinstance(finding, Finding)
    assert any("mystery_field" in reason for reason in finding.reasons)


def test_check_cache_file_requires_filename_to_match_reference_id(tmp_path: Path):
    bad = tmp_path / "PMID_00000000.md"
    bad.write_text(
        '---\nreference_id: "PMID:12345678"\ncontent_type: abstract_only\n---\n',
        encoding="utf-8",
    )
    finding = check_cache_file(bad)
    assert isinstance(finding, Finding)
    assert any("filename must match" in reason for reason in finding.reasons)


def test_check_cache_file_allows_mixed_case_doi_filename(tmp_path: Path):
    doi = tmp_path / "DOI_10.1272_jnms.JNMS.2023_90-104.md"
    doi.write_text(
        "---\n"
        'reference_id: "DOI:10.1272/jnms.jnms.2023_90-104"\n'
        "content_type: unavailable\n"
        "---\n",
        encoding="utf-8",
    )
    assert check_cache_file(doi) is None


@pytest.mark.skipif(not CACHE_DIR.is_dir(), reason="references_cache/ not present")
def test_existing_repo_caches_match_frontmatter_contract():
    findings = scan_cache_dir(CACHE_DIR)
    assert findings == [], "\n".join(f.format() for f in findings)
