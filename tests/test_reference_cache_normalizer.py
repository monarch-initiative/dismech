"""Regression tests for scoped reference-cache normalization (issue #7844)."""

from __future__ import annotations

from pathlib import Path

from dismech.reference_cache_normalizer import (
    normalize_cache,
    normalize_cache_file,
)


def _write_cache(path: Path, reference_id: str, *, title: str = "A paper") -> str:
    content = (
        "---\n"
        f"reference_id: {reference_id}\n"
        f"title: {title}\n"
        "content_type: abstract_only\n"
        "---\n\n"
        "## Content\n\n"
        "Body with an inline --- sequence that must remain unchanged.\n"
    )
    path.write_text(content, encoding="utf-8")
    return content


def test_normalize_cache_file_quotes_unsafe_scalars_without_touching_body(
    tmp_path: Path,
):
    cache = tmp_path / "PMID_123.md"
    _write_cache(cache, "PMID:123", title=r"Study: C:\study")

    assert normalize_cache_file(cache)
    normalized = cache.read_text(encoding="utf-8")
    assert "reference_id: PMID:123" in normalized
    assert 'title: "Study: C:\\\\study"' in normalized
    assert "Body with an inline --- sequence that must remain unchanged." in normalized
    assert not normalize_cache_file(cache)


def test_data_file_scope_does_not_modify_unrelated_cache(tmp_path: Path):
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    cited = cache_dir / "PMID_123.md"
    unrelated = cache_dir / "PMID_456.md"
    _write_cache(cited, "PMID:123", title="Cited: paper")
    unrelated_before = _write_cache(unrelated, "PMID:456", title="Other: paper")

    data_file = tmp_path / "Disease.yaml"
    data_file.write_text(
        "name: Example\nevidence:\n- reference: PMID:123\n  snippet: Exact quote\n",
        encoding="utf-8",
    )

    assert normalize_cache(cache_dir, [data_file]) == [cited]
    assert 'title: "Cited: paper"' in cited.read_text(encoding="utf-8")
    assert "reference_id: PMID:123" in cited.read_text(encoding="utf-8")
    assert unrelated.read_text(encoding="utf-8") == unrelated_before


def test_scope_resolves_case_insensitive_doi_and_bare_nct(tmp_path: Path):
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    doi = cache_dir / "DOI_10.1000_MixedCase.md"
    trial = cache_dir / "clinicaltrials_NCT06087757.md"
    _write_cache(doi, "DOI:10.1000/MixedCase", title="DOI: paper")
    _write_cache(trial, "clinicaltrials:NCT06087757", title="Trial: paper")
    data_file = tmp_path / "Disease.yaml"
    data_file.write_text(
        "references:\n- reference: doi:10.1000/mixedcase\n- reference: NCT06087757\n",
        encoding="utf-8",
    )

    assert normalize_cache(cache_dir, [data_file]) == [doi, trial]


def test_scope_includes_authoritative_reference_accession(tmp_path: Path):
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    trial = cache_dir / "clinicaltrials_NCT01238250.md"
    _write_cache(trial, "clinicaltrials:NCT01238250", title="Trial: record")
    data_file = tmp_path / "Disease.yaml"
    data_file.write_text(
        "datasets:\n- accession: clinicaltrials:NCT01238250\n",
        encoding="utf-8",
    )

    assert normalize_cache(cache_dir, [data_file]) == [trial]


def test_missing_and_malformed_data_files_are_skipped(tmp_path: Path):
    cache_dir = tmp_path / "cache"
    cache_dir.mkdir()
    cited = cache_dir / "PMID_123.md"
    before = _write_cache(cited, "PMID:123", title="Cited: paper")
    malformed = tmp_path / "Malformed.yaml"
    malformed.write_text("evidence: [\n", encoding="utf-8")

    changed = normalize_cache(
        cache_dir,
        [tmp_path / "Missing.yaml", malformed],
    )

    assert changed == []
    assert cited.read_text(encoding="utf-8") == before


def test_plain_scalar_colon_and_indicator_rules(tmp_path: Path):
    cache = tmp_path / "PMID_123.md"
    _write_cache(cache, "PMID:123", title="Unsafe: title")

    assert normalize_cache_file(cache)
    normalized = cache.read_text(encoding="utf-8")
    assert "reference_id: PMID:123" in normalized
    assert 'title: "Unsafe: title"' in normalized
