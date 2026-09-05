"""The frontmatter readers fixed in issue #7697, end to end.

Each of these used ``text.split("---", 2)`` and therefore mis-read any cache file
whose frontmatter contains a literal ``---``. The committed
``references_cache/PMID_1899320.md`` is the real instance.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import (
    check_cache_file,
    check_consumer_compatibility,
    scan_cache_dir_consumer_compatibility,
)
from dismech.reference_snippet_audit import CachedReferenceIndex
from tests.test_frontmatter import MMWR_CACHE, NLM_ARROW_CACHE

ROOT = Path(__file__).resolve().parents[1]
_SCRIPT = ROOT / "scripts" / "warm_reference_cache.py"
_spec = importlib.util.spec_from_file_location("warm_reference_cache", _SCRIPT)
warm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(warm)


def _write(tmp_path: Path, name: str, text: str) -> Path:
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


# --- scripts/warm_reference_cache.py ------------------------------------------


def test_warm_cache_sees_content_type_behind_triple_hyphen_title(tmp_path: Path):
    """Previously the truncated frontmatter hid content_type, and the skip was silent."""
    _write(tmp_path, "PMID_1899320.md", NLM_ARROW_CACHE)

    targets = warm.find_targets(tmp_path, {"abstract_only"})

    assert [reference_id for _, reference_id in targets] == ["PMID:1899320"]


def test_warm_cache_sees_content_type_in_committed_record():
    path = ROOT / "references_cache" / "PMID_1899320.md"
    if not path.exists():  # pragma: no cover - corpus may be pruned
        pytest.skip("PMID_1899320.md not present in this checkout")

    frontmatter = warm._frontmatter(path)

    assert frontmatter is not None
    assert "content_type:" in frontmatter
    # The fields that used to fall past the naive split point.
    assert "authors:" in frontmatter
    assert "journal:" in frontmatter


# --- src/dismech/reference_snippet_audit.py -----------------------------------


def test_snippet_audit_body_excludes_frontmatter():
    """Leaked frontmatter would let a snippet quoting the *title* verify."""
    body = CachedReferenceIndex.extract_body(MMWR_CACHE)

    assert "reference_id:" not in body
    assert "content_type:" not in body
    assert body.strip() == "The patient died on November 20."


# --- src/dismech/reference_cache_frontmatter.py -------------------------------


def test_contract_still_accepts_triple_hyphen_titles(tmp_path: Path):
    """The gating contract is correct and must not start rejecting these."""
    for name, text in (
        ("PMID_1899320.md", NLM_ARROW_CACHE),
        ("PMID_20881935.md", MMWR_CACHE),
    ):
        assert check_cache_file(_write(tmp_path, name, text)) is None


def test_consumer_compatibility_advisory_flags_triple_hyphen(tmp_path: Path):
    path = _write(tmp_path, "PMID_1899320.md", NLM_ARROW_CACHE)

    finding = check_consumer_compatibility(path)

    assert finding is not None
    assert finding.reference_id == "PMID:1899320"
    assert "#7697" in finding.reasons[0]


def test_consumer_compatibility_advisory_is_quiet_on_ordinary_files(tmp_path: Path):
    ordinary = (
        "---\n"
        'reference_id: "PMID:12345678"\n'
        'title: "An ordinary paper"\n'
        "journal: Example Journal\n"
        "content_type: abstract_only\n"
        "---\n\n# An ordinary paper\n"
    )
    path = _write(tmp_path, "PMID_12345678.md", ordinary)

    assert check_consumer_compatibility(path) is None
    assert scan_cache_dir_consumer_compatibility(tmp_path) == []


def test_consumer_compatibility_scan_finds_the_one_file(tmp_path: Path):
    _write(tmp_path, "PMID_1899320.md", NLM_ARROW_CACHE)
    _write(
        tmp_path,
        "PMID_12345678.md",
        "---\n"
        'reference_id: "PMID:12345678"\n'
        "journal: Example Journal\n"
        "content_type: abstract_only\n"
        "---\n\nbody\n",
    )

    findings = scan_cache_dir_consumer_compatibility(tmp_path)

    assert [f.reference_id for f in findings] == ["PMID:1899320"]
