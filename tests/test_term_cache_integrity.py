"""Tests for deterministic term cache structural checks (issue #7682)."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.term_cache_integrity import (
    Finding,
    check_cache_file,
    check_enum_cache_file,
    discover_cache_files,
    scan_cache_dir,
)

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "cache"

HEADER = "curie,label,retrieved_at\n"
ENUM_HEADER = "curie\n"


def _write_cache(tmp_path: Path, ontology: str, body: str) -> Path:
    """Write a ``cache/<ontology>/terms.csv`` fixture and return its path."""
    path = tmp_path / ontology / "terms.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(HEADER + body, encoding="utf-8")
    return path


def _write_enum_cache(tmp_path: Path, name: str, body: str) -> Path:
    """Write a ``cache/enums/<name>.csv`` fixture and return its path."""
    path = tmp_path / "enums" / f"{name}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENUM_HEADER + body, encoding="utf-8")
    return path


def _reasons(findings: list[Finding]) -> str:
    return "\n".join(f.format() for f in findings)


def test_valid_cache_file_passes(tmp_path: Path):
    good = _write_cache(
        tmp_path,
        "hp",
        "HP:0001250,Seizure,2026-03-18T01:50:00.134167\n"
        "HP:0002014,Diarrhea,2026-07-31T17:35:40.810696\n",
    )
    assert check_cache_file(good) == []


def test_quoted_comma_containing_label_passes(tmp_path: Path):
    """Correctly-quoted commas in labels are legitimate and common.

    MONDO's ``, dominant`` / ``, recessive`` / ``, type N`` naming conventions
    account for hundreds of committed rows. These are exactly the labels the
    concatenation bug in #7682 damages, so the check must accept the *correct*
    form or it would fail on most of the MONDO cache.
    """
    good = _write_cache(
        tmp_path,
        "mondo",
        'MONDO:0012013,"Weill-Marchesani syndrome 2, dominant",'
        "2026-08-01T04:30:00.000000\n"
        'MONDO:0000914,"cerebral arteriopathy, autosomal dominant, with '
        'subcortical infarcts and leukoencephalopathy, type 1",'
        "2026-03-17T19:32:49.026708\n",
    )
    assert check_cache_file(good) == []


def test_unquoted_comma_label_four_field_row_is_rejected(tmp_path: Path):
    """The stage-one signature from #7682: string-concatenated row.

    ``MONDO:0012013,Weill-Marchesani syndrome 2, dominant,<ts>`` parses to four
    fields; the label is truncated at the comma and ``retrieved_at`` becomes
    ``" dominant"``.
    """
    bad = _write_cache(
        tmp_path,
        "mondo",
        "MONDO:0012013,Weill-Marchesani syndrome 2, dominant,"
        "2026-08-01T04:30:00.000000\n",
    )
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert findings[0].line == 2
    assert any("4 fields" in reason for reason in findings[0].reasons)


def test_two_field_row_is_rejected(tmp_path: Path):
    """A row missing its trailing timestamp entirely (no trailing comma).

    The mirror image of the four-field case, and a plausible hand-edit artifact.
    """
    bad = _write_cache(tmp_path, "hp", "HP:0001250,Seizure\n")
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("2 fields" in reason for reason in findings[0].reasons)


def test_empty_retrieved_at_is_rejected(tmp_path: Path):
    """Regression fixture for the ``GO:0016887`` row that was on ``main``."""
    bad = _write_cache(tmp_path, "go", "GO:0016887,ATP hydrolysis activity,\n")
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("retrieved_at is empty" in reason for reason in findings[0].reasons)


def test_malformed_retrieved_at_is_rejected(tmp_path: Path):
    """Regression fixture for the ``HP:0001520`` row that was on ``main``.

    ``2026-03-18T:50:00.134167`` is missing the hour component.
    """
    bad = _write_cache(
        tmp_path,
        "hp",
        "HP:0001520,Large for gestational age,2026-03-18T:50:00.134167\n",
    )
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("ISO-8601" in reason for reason in findings[0].reasons)


def test_date_only_retrieved_at_is_rejected(tmp_path: Path):
    """``datetime.fromisoformat`` accepts a bare date, but the cache writer
    always emits date *and* time — a date-only value is a truncation."""
    bad = _write_cache(tmp_path, "hp", "HP:0001250,Seizure,2026-08-02\n")
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("missing its time component" in r for r in findings[0].reasons)


def test_retrieved_at_with_curie_tail_is_rejected(tmp_path: Path):
    """Regression fixture for the ``MONDO:0018019`` row that was on ``main``."""
    bad = _write_cache(
        tmp_path,
        "mondo",
        "MONDO:0018019,lead poisoning,2026-03-18T02:23:27.3MONDO:0018076\n",
    )
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("ISO-8601" in reason for reason in findings[0].reasons)


def test_malformed_curie_is_rejected(tmp_path: Path):
    """Regression fixtures for the clobbered CURIEs that were on ``main``."""
    bad = _write_cache(
        tmp_path,
        "mondo",
        "MONDO:0MONDO:0008661,vitiligo,2026-03-18T01:49:51.180817\n"
        "MONDO:MONDO:0018088,familial Mediterranean fever,"
        "2026-03-18T01:49:51.180721\n",
    )
    findings = check_cache_file(bad)
    assert len(findings) == 2
    assert all(
        any("not a PREFIX:LOCALID CURIE" in reason for reason in f.reasons)
        for f in findings
    ), _reasons(findings)


def test_curie_without_prefix_is_rejected(tmp_path: Path):
    """Regression fixture for the ``887`` row (a clobbered ``GO:0016887``)."""
    bad = _write_cache(
        tmp_path, "go", "887,ATP hydrolysis activity,2026-03-17T19:39:29.616328\n"
    )
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("not a PREFIX:LOCALID CURIE" in r for r in findings[0].reasons)


def test_curie_prefix_must_match_cache_directory(tmp_path: Path):
    """Regression fixture for ``BI:24996`` (a clobbered ``CHEBI:24996``).

    The clobbered CURIE still has a valid ``PREFIX:LOCALID`` shape, so only the
    directory/prefix invariant catches it.
    """
    bad = _write_cache(
        tmp_path, "chebi", "BI:24996,lactate,2026-03-08T15:17:40.512904\n"
    )
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("match the cache directory" in r for r in findings[0].reasons)


def test_prefix_match_is_case_insensitive(tmp_path: Path):
    """``cache/ncbitaxon`` holds ``NCBITaxon:`` rows and ``cache/hgnc`` holds
    lowercase ``hgnc:`` rows; both are legitimate."""
    assert (
        check_cache_file(
            _write_cache(
                tmp_path,
                "ncbitaxon",
                "NCBITaxon:9606,Homo sapiens,2026-03-08T15:17:40.512904\n",
            )
        )
        == []
    )
    assert (
        check_cache_file(
            _write_cache(
                tmp_path, "hgnc", "hgnc:746,ABCA4,2026-03-08T15:17:40.512904\n"
            )
        )
        == []
    )


def test_empty_label_is_rejected(tmp_path: Path):
    bad = _write_cache(tmp_path, "hp", "HP:0001250,,2026-03-18T01:50:00.134167\n")
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert any("label is empty" in reason for reason in findings[0].reasons)


def test_wrong_header_is_rejected(tmp_path: Path):
    path = tmp_path / "hp" / "terms.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "curie,label\nHP:0001250,Seizure,2026-03-18T01:50:00.134167\n",
        encoding="utf-8",
    )
    findings = check_cache_file(path)
    assert any(
        any("header must be" in reason for reason in f.reasons) for f in findings
    ), _reasons(findings)


def test_header_only_file_passes(tmp_path: Path):
    """A freshly-created, still-empty cache is structurally fine."""
    assert check_cache_file(_write_cache(tmp_path, "hp", "")) == []


def test_duplicate_curie_is_rejected(tmp_path: Path):
    """Four of the eight corruptions found on ``main`` were duplicates in
    disguise. A clobber producing a valid-looking CURIE already present in the
    file passes every other check, so duplicates are flagged on their own."""
    bad = _write_cache(
        tmp_path,
        "hp",
        "HP:0001250,Seizure,2026-03-18T01:50:00.134167\n"
        "HP:0002014,Diarrhea,2026-03-18T01:50:00.134167\n"
        "HP:0001250,Seizures,2026-07-31T17:35:40.810696\n",
    )
    findings = check_cache_file(bad)
    assert len(findings) == 1
    assert findings[0].line == 4
    assert any("duplicate curie" in r and "line 2" in r for r in findings[0].reasons)


def test_duplicate_curie_detection_is_case_insensitive(tmp_path: Path):
    bad = _write_cache(
        tmp_path,
        "hgnc",
        "hgnc:746,ABCA4,2026-03-18T01:50:00.134167\n"
        "HGNC:746,ABCA4,2026-03-18T01:50:00.134167\n",
    )
    findings = check_cache_file(bad)
    assert any(any("duplicate curie" in r for r in f.reasons) for f in findings), (
        _reasons(findings)
    )


def test_headerless_file_still_checks_its_first_row(tmp_path: Path):
    """A file with no header must not have its first *data* row silently
    consumed as the header and skipped."""
    path = tmp_path / "hp" / "terms.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "HP:0001250,Seizure,not-a-timestamp\n"
        "HP:0002014,Diarrhea,2026-03-18T01:50:00.134167\n",
        encoding="utf-8",
    )
    findings = check_cache_file(path)
    lines = {f.line for f in findings}
    # line 1: the missing header, *and* the malformed timestamp on that row.
    assert lines == {1}, _reasons(findings)
    reasons = [r for f in findings for r in f.reasons]
    assert any("header must be" in r for r in reasons), _reasons(findings)
    assert any("ISO-8601" in r for r in reasons), _reasons(findings)


def test_valid_enum_cache_passes(tmp_path: Path):
    """Enum membership caches are single-column and mixed-prefix by design."""
    good = _write_enum_cache(
        tmp_path, "phenotypeterm_abc123", "HP:0001250\nMONDO:0018019\nhgnc:746\n"
    )
    assert check_enum_cache_file(good) == []


def test_enum_cache_rejects_malformed_curie(tmp_path: Path):
    bad = _write_enum_cache(tmp_path, "phenotypeterm_abc123", "HP:0001250\n887\n")
    findings = check_enum_cache_file(bad)
    assert len(findings) == 1
    assert findings[0].line == 3
    assert any("not a PREFIX:LOCALID CURIE" in r for r in findings[0].reasons)


def test_enum_cache_rejects_extra_column(tmp_path: Path):
    """The concatenation vector applied to an enum cache: a label glued on."""
    bad = _write_enum_cache(
        tmp_path, "diseaseterm_abc123", "MONDO:0012013,Weill-Marchesani syndrome 2\n"
    )
    findings = check_enum_cache_file(bad)
    assert len(findings) == 1
    assert any("expected 1" in r for r in findings[0].reasons)


def test_enum_cache_rejects_duplicate_curie(tmp_path: Path):
    bad = _write_enum_cache(
        tmp_path, "phenotypeterm_abc123", "HP:0001250\nHP:0001250\n"
    )
    findings = check_enum_cache_file(bad)
    assert len(findings) == 1
    assert any("duplicate curie" in r for r in findings[0].reasons)


def test_enum_cache_rejects_wrong_header(tmp_path: Path):
    path = tmp_path / "enums" / "phenotypeterm_abc123.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("id\nHP:0001250\n", encoding="utf-8")
    findings = check_enum_cache_file(path)
    assert any(any("header must be curie" in r for r in f.reasons) for f in findings), (
        _reasons(findings)
    )


def test_scan_cache_dir_covers_enum_caches(tmp_path: Path):
    _write_cache(tmp_path, "hp", "HP:0001250,Seizure,2026-03-18T01:50:00.134167\n")
    _write_enum_cache(tmp_path, "phenotypeterm_abc123", "HP:0001250\n887\n")
    findings = scan_cache_dir(tmp_path)
    assert len(findings) == 1, _reasons(findings)
    assert findings[0].path.parent.name == "enums"


def test_enums_dir_is_never_scanned_as_a_term_cache(tmp_path: Path):
    """A ``cache/enums/terms.csv`` would match both globs and be scanned twice
    under two contradictory contracts. No such file should exist, but the
    discovery split must make it impossible rather than merely unlikely."""
    _write_enum_cache(tmp_path, "terms", "HP:0001250\n")
    term_caches, enum_caches = discover_cache_files(tmp_path)
    assert term_caches == []
    assert [p.name for p in enum_caches] == ["terms.csv"]
    # Scanned once, under the single-column enum contract, so it passes.
    assert scan_cache_dir(tmp_path) == []


def test_scan_cache_dir_reports_every_ontology(tmp_path: Path):
    _write_cache(tmp_path, "go", "GO:0016887,ATP hydrolysis activity,\n")
    _write_cache(tmp_path, "hp", "HP:0001250,Seizure,2026-03-18T01:50:00.134167\n")
    _write_cache(tmp_path, "mondo", "MONDO:0018019,lead poisoning,not-a-timestamp\n")
    findings = scan_cache_dir(tmp_path)
    assert len(findings) == 2, _reasons(findings)
    assert {f.path.parent.name for f in findings} == {"go", "mondo"}


@pytest.mark.skipif(not CACHE_DIR.is_dir(), reason="cache/ not present")
def test_committed_term_caches_match_structural_contract():
    findings = scan_cache_dir(CACHE_DIR)
    assert findings == [], _reasons(findings)
