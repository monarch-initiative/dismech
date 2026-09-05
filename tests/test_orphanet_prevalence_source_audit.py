"""Tests for the Orphanet recited-publication audit (issue #7518).

Every fixture token below is a *real* string taken from the committed
``references_cache/ORPHA_*.md`` files, and each one is traceable to the upstream
Orphadata ``<Source>`` string that produced it. That matters: the whole point of
the audit is that the shapes it triages are the shapes the data actually has, so
inventing plausible-looking fixtures would test the wrong thing.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SCRIPT = _REPO_ROOT / "scripts" / "orphanet_prevalence_source_audit.py"

_spec = importlib.util.spec_from_file_location("orphanet_prevalence_source_audit", _SCRIPT)
assert _spec and _spec.loader
audit_mod = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = audit_mod
_spec.loader.exec_module(audit_mod)


# --- classification -------------------------------------------------------


@pytest.mark.parametrize(
    "token,expected,upstream_source",
    [
        # Ordinary, well-formed citation: the tag really was [PMID].
        ("PMID:29211930", audit_mod.PMID_CANDIDATE, "29211930[PMID]"),
        # A five-digit PMID is valid and must not be rejected by any length
        # gate -- references_cache/PMID_68190.md is Jokipii, Lancet 1977.
        ("PMID:68190", audit_mod.PMID_CANDIDATE, "68190[PMID]"),
        # Organisation-plus-year citations tagged [OTHER]; the year gets the
        # PMID: prefix stamped on it. 2012 is also a real PubMed identifier,
        # which is exactly why it can never be auto-promoted.
        ("PMID:2012", audit_mod.YEAR_SUSPECT, "European Medicines Agency 2012[OTHER]"),
        ("PMID:2019", audit_mod.YEAR_SUSPECT, "European Medicines Agency 2019[OTHER]"),
        # Books. ISBN-13 keeps its 978/979 prefix; ISBN-10 may lead with a zero,
        # so the ISBN check has to run before any leading-zero rule.
        ("PMID:9780313387135", audit_mod.ISBN_SUSPECT, "ISBN:9780313387135[OTHER]_ORPHANET"),
        ("PMID:9789350901885", audit_mod.ISBN_SUSPECT, "ISBN 13:9789350901885[OTHER]_[EXPERT]"),
        ("PMID:9630566311", audit_mod.ISBN_SUSPECT, "ISBN:9630566311[OTHER]"),
        ("PMID:0870684507", audit_mod.ISBN_SUSPECT, "ISBN:0870684507[OTHER]"),
        ("PMID:702021520", audit_mod.ISBN_SUSPECT, "ISBN:702021520[OTHER]_21364698[PMID]"),
        # DOI fragments. Both are syntactically valid PubMed identifiers, so
        # they are flagged for a human rather than rejected outright.
        ("PMID:008", audit_mod.SHORT_SUSPECT, "DOI:10.1016/j.jfma.2013.01.008[OTHER]"),
        ("PMID:11", audit_mod.SHORT_SUSPECT, "10.1007/978-3-642-05080-0_11[DOI]"),
        # Bare source-type tags, all present in the committed caches.
        ("EXPERT", audit_mod.MARKER, "[EXPERT]"),
        ("ORPHANET", audit_mod.MARKER, "ORPHANET"),
        ("REG", audit_mod.MARKER, "[REG]"),
        ("INST", audit_mod.MARKER, "[INST]"),
        ("OTHER", audit_mod.MARKER, "[OTHER]"),
        # A [PMID] tag whose identifier did not survive the parse.
        ("PMID", audit_mod.MARKER, "[PMID]"),
        # An unterminated bracket upstream defeats the regex entirely, so the
        # raw string is passed through and a real PMID is stranded in it.
        ("ORPHANET_16928994[PMID", audit_mod.STRANDED_PMID, "ORPHANET_16928994[PMID"),
        ("30260188[PMID", audit_mod.STRANDED_PMID, "30260188[PMID"),
        # Same passthrough branch, but nothing citable in it.
        (
            "https://www.ncbi.nlm.nih.gov/books/NBK1212/",
            audit_mod.FREE_TEXT,
            "https://www.ncbi.nlm.nih.gov/books/NBK1212/",
        ),
        ("ECFSNeonatalScreeningWorkingGroup", audit_mod.FREE_TEXT, "..."),
        ("-", audit_mod.FREE_TEXT, "(empty Source cell)"),
    ],
)
def test_classify_token(token: str, expected: str, upstream_source: str) -> None:
    assert audit_mod.classify_token(token) == expected, upstream_source


def test_no_length_gate_on_plausible_pmids() -> None:
    """Digit count alone must never reject a PMID (the #7518 review finding)."""
    for digits in ("68190", "397771", "480028", "623097", "12345678"):
        assert audit_mod.classify_token(f"PMID:{digits}") == audit_mod.PMID_CANDIDATE


def test_years_outside_the_plausible_range_are_not_year_suspect() -> None:
    """A four-digit token is only a year if it could plausibly *be* one."""
    assert audit_mod.classify_token("PMID:1899") == audit_mod.PMID_CANDIDATE
    assert audit_mod.classify_token("PMID:2031") == audit_mod.PMID_CANDIDATE
    assert audit_mod.classify_token("PMID:1900") == audit_mod.YEAR_SUSPECT
    assert audit_mod.classify_token("PMID:2030") == audit_mod.YEAR_SUSPECT


def test_non_publication_classes_exclude_pmid_candidates() -> None:
    assert audit_mod.PMID_CANDIDATE not in audit_mod.NON_PUBLICATION
    assert audit_mod.SHORT_SUSPECT not in audit_mod.NON_PUBLICATION


# --- cache table parsing --------------------------------------------------

_CACHE_FIXTURE = """# ORPHA:52  Alagille syndrome

## Definition

A rare disorder.

## Epidemiology

| Class | Region | Type | Source |
|---|---|---|---|
| 1-9 / 1 000 000 | Europe | Prevalence at birth | PMID:2012 |
| <1 / 1 000 000 | Worldwide | Point prevalence | PMID:29211930,EXPERT |
| Unknown | France | Annual incidence | - |

## Genes

| Gene | Name |
|---|---|
| JAG1 | jagged 1 |
"""


def test_parse_epidemiology_rows_only_reads_that_table() -> None:
    rows = audit_mod.parse_epidemiology_rows(_CACHE_FIXTURE)
    assert [r.region for r in rows] == ["Europe", "Worldwide", "France"]
    # The Genes table that follows must not leak in.
    assert all(r.pclass != "JAG1" for r in rows)


def test_row_tokens_split_the_source_cell() -> None:
    rows = audit_mod.parse_epidemiology_rows(_CACHE_FIXTURE)
    assert rows[0].tokens() == ["PMID:2012"]
    assert rows[1].tokens() == ["PMID:29211930", "EXPERT"]
    assert rows[2].tokens() == []


@pytest.mark.parametrize(
    "snippet,expected_status",
    [
        # Quoted with and without the surrounding pipes -- both are documented
        # curator forms and must resolve to the same row.
        ("1-9 / 1 000 000 | Europe | Prevalence at birth | PMID:2012", "MATCHED"),
        ("| 1-9 / 1 000 000 | Europe | Prevalence at birth | PMID:2012 |", "MATCHED"),
        # Curators routinely stop before the Source column.
        ("<1 / 1 000 000 | Worldwide | Point prevalence", "MATCHED"),
        # Prose quoted from elsewhere in the same cache recites nothing.
        ("A rare disorder.", "NON_EPI_QUOTE"),
        ("text that is nowhere in this cache", "UNMATCHED"),
    ],
)
def test_match_row(snippet: str, expected_status: str) -> None:
    rows = audit_mod.parse_epidemiology_rows(_CACHE_FIXTURE)
    _, status = audit_mod._match_row(rows, snippet, _CACHE_FIXTURE)
    assert status == expected_status


def test_match_row_resolves_the_right_source_cell() -> None:
    rows = audit_mod.parse_epidemiology_rows(_CACHE_FIXTURE)
    row, _ = audit_mod._match_row(
        rows, "<1 / 1 000 000 | Worldwide | Point prevalence", _CACHE_FIXTURE
    )
    assert row is not None
    assert row.tokens() == ["PMID:29211930", "EXPERT"]


# --- at-risk snippet detection --------------------------------------------


def test_at_risk_detection_does_not_fire_on_a_longer_pmid(tmp_path: Path) -> None:
    """``PMID:11`` must not match inside ``PMID:11344308``.

    Fanconi_Anemia genuinely quotes ``PMID:11344308``; a naive substring test
    reported it as collateral damage of a parser fix, which it is not.
    """
    (tmp_path / "kb" / "disorders").mkdir(parents=True)
    (tmp_path / "references_cache").mkdir()
    (tmp_path / "kb" / "disorders" / "Example.yaml").write_text(
        "name: Example\n"
        "prevalence:\n"
        "- population: Specific population\n"
        "  evidence:\n"
        "  - reference: ORPHA:84\n"
        '    snippet: "1-9 / 100 000 | Specific population | Point prevalence | PMID:11344308"\n',
        encoding="utf-8",
    )
    hits = audit_mod.find_at_risk_snippets(tmp_path, {"PMID:11"})
    assert hits == []

    # ...but the exact token, at a real boundary, is caught.
    hits = audit_mod.find_at_risk_snippets(tmp_path, {"PMID:11344308"})
    assert [h[2] for h in hits] == ["PMID:11344308"]


# --- end-to-end over the real repository ----------------------------------


@pytest.fixture(scope="module")
def real_audit():
    return audit_mod.audit(_REPO_ROOT)


def test_audit_resolves_every_orpha_snippet(real_audit) -> None:
    """No ORPHA-sourced prevalence snippet should be unresolvable.

    An ``UNMATCHED`` snippet means the quoted text is nowhere in the cache it
    cites, which the fast snippet check would also flag; ``AMBIGUOUS`` means a
    recitation cannot be attributed to one row. Both want a human, so this test
    guards the audit's own coverage rather than the KB's correctness.
    """
    assert real_audit.needs_review == []
    assert real_audit.missing_cache_files == []


def test_audit_finds_the_known_bad_tokens(real_audit) -> None:
    """The tokens #7518 was filed about are still present and still flagged."""
    by_token = {f.token: f.classification for f in real_audit.findings}
    assert by_token.get("PMID:2012") == audit_mod.YEAR_SUSPECT
    assert by_token.get("PMID:0870684507") == audit_mod.ISBN_SUSPECT
    assert by_token.get("ORPHANET_16928994[PMID") == audit_mod.STRANDED_PMID


def test_no_flagged_token_is_ever_cached_as_a_reference(real_audit) -> None:
    """A year or ISBN must never have been fetched as if it were a paper."""
    for finding in real_audit.findings:
        if finding.classification in audit_mod.NON_PUBLICATION:
            assert not finding.cached_locally, finding


def test_report_is_deterministic(real_audit) -> None:
    """The committed report must regenerate byte-identically."""
    first = audit_mod.render_markdown(real_audit)
    second = audit_mod.render_markdown(audit_mod.audit(_REPO_ROOT))
    assert first == second


def test_committed_report_is_current(real_audit) -> None:
    """`just orphanet-prevalence-source-audit` output is committed and fresh."""
    report = _REPO_ROOT / "research" / "orphanet_prevalence_source_audit.md"
    assert report.exists(), "run `just orphanet-prevalence-source-audit`"
    assert report.read_text(encoding="utf-8") == audit_mod.render_markdown(real_audit), (
        "research/orphanet_prevalence_source_audit.md is stale -- regenerate it "
        "with `just orphanet-prevalence-source-audit`"
    )
