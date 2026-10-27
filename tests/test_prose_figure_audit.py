"""Tests for the prose quantitative-figure audit (issue #7791).

The audit's value rests entirely on its *scope* being adjacent rather than
entry-wide, and on the cache side being stripped of bibliographic apparatus.
Both were bugs during development that silently cleared a real finding, so both
are pinned here.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "prose_figure_audit.py"
SPEC = importlib.util.spec_from_file_location("prose_figure_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


CACHE_TEMPLATE = """---
reference_id: "{ref}"
title: A paper about something.
year: '2016'
doi: 10.1038/nrdp.2016.35
---

# A paper about something.
**DOI:** [10.1038/nrdp.2016.35](https://doi.org/10.1038/nrdp.2016.35)

## Content

1. Nat Rev Dis Primers. 2016 May 26;2:16035. doi: 10.1038/nrdp.2016.35.

A paper about something.

Smith AB(1), Jones CD(2)(3), Brown EF(4).

Author information:
(1)Department of Medicine, Some Hospital, 15 Francis Street, Boston,
Massachusetts 02115, USA.
(2)Another Department, Elsewhere.

{body}
"""


@pytest.fixture()
def cache(tmp_path, monkeypatch):
    """Redirect the audit at a temporary reference cache."""
    cache_dir = tmp_path / "references_cache"
    cache_dir.mkdir()
    monkeypatch.setattr(audit, "CACHE_DIR", cache_dir)
    audit._number_cache.clear()

    def write(ref: str, body: str) -> None:
        stem = ref.replace(":", "_")
        (cache_dir / f"{stem}.md").write_text(
            CACHE_TEMPLATE.format(ref=ref, body=body), encoding="utf-8"
        )

    yield write
    audit._number_cache.clear()


def _audit(tmp_path, yaml_text: str):
    path = tmp_path / "Some_Disease.yaml"
    path.write_text(yaml_text, encoding="utf-8")
    monkey_root = audit._REPO_ROOT
    # ``Finding.file`` is reported relative to the repo root; point it at tmp_path
    # so the dataclass can be built for a fixture file outside the repo.
    audit._REPO_ROOT = tmp_path
    try:
        return audit.audit_file(path, ("description", "notes"), set())
    finally:
        audit._REPO_ROOT = monkey_root


# ---------------------------------------------------------------------------
# Figure extraction
# ---------------------------------------------------------------------------

def test_extracts_both_ends_of_a_percentage_range():
    figures = {(f.token, f.kind) for f in audit.extract_figures("occurs in 30-40% of adults")}
    assert ("30", "percent") in figures
    assert ("40", "percent") in figures


@pytest.mark.parametrize(
    "text,token,kind",
    [
        ("affects up to 90% of patients", "90", "percent"),
        ("a birth prevalence of 1 in 25,000", "25000", "one_in_n"),
        ("4 per 100,000 person-years", "4", "rate"),
        ("a 2.5-fold increased risk", "2.5", "fold"),
        ("reported in 12 per cent of cases", "12", "percent"),
    ],
)
def test_extracts_unit_bearing_quantities(text, token, kind):
    assert (token, kind) in {(f.token, f.kind) for f in audit.extract_figures(text)}


@pytest.mark.parametrize(
    "text",
    [
        "skipping of exon 51 restores the reading frame",
        "a variant on chromosome 15",
        "Sanfilippo syndrome type 3",
        "the 2 patients described",
    ],
)
def test_bare_integers_are_not_figures(text):
    """Names and counts are not measurements; flagging them would bury the signal."""
    assert audit.extract_figures(text) == []


# ---------------------------------------------------------------------------
# Suppressions: prose that is not a claim about the literature
# ---------------------------------------------------------------------------

def test_frequency_band_boundaries_are_not_claims():
    """"falls in the FREQUENT band (30-79%)" quotes dismech's own enum, not a paper.

    `docs/frequency-evidence-guidelines.md` asks curators to justify a
    `frequency:` value exactly this way, and no cited paper will ever contain the
    boundary numbers. Left in, this one pattern produced 68 of the 79 findings on
    BRPF1-Related_Intellectual_Disability.yaml.
    """
    text = "16/29 (55%). 55% falls in the FREQUENT band (30-79%), so FREQUENT."
    tokens = {f.token for f in audit.extract_figures(text)}
    assert "30" not in tokens
    assert "79" not in tokens


def test_percentage_derived_from_a_stated_fraction_is_not_flagged():
    """Showing your working is good curation; flagging it punishes the practice."""
    assert audit.extract_figures("ID in 16 of 29 patients with data (55%)") == []
    assert audit.extract_figures("language disorder in 11/12 assessed (92%)") == []


def test_derivation_tolerance_absorbs_loose_rounding():
    """13/29 is 44.8%; curators write that as 45% or 46% and both are derived."""
    assert audit.extract_figures("recorded in 13/29 (45%)") == []
    assert audit.extract_figures("recorded in 13/29 (46%)") == []


def test_a_figure_unrelated_to_the_stated_fraction_still_flags():
    """The tolerance is slack on a derivation, not a licence for any nearby number."""
    assert {f.token for f in audit.extract_figures("hypotonia in 13/29 (72%)")} == {"72"}


def test_an_unrelated_percentage_survives_a_nearby_fraction():
    """Suppression is per-figure, not per-block."""
    tokens = {f.token for f in audit.extract_figures("ID in 16 of 29 (55%); LAM in 90%")}
    assert tokens == {"90"}


def test_thousands_separators_and_decimal_commas_normalise():
    assert audit._clean_number("25,000") == "25000"
    assert audit._clean_number("61,4") == "61.4"
    assert audit._clean_number("40.0") == "40"


# ---------------------------------------------------------------------------
# Equivalent forms
# ---------------------------------------------------------------------------

def test_one_in_n_accepts_the_standard_rate_conversions():
    """A curator converting Orphanet's 1/25,000 to 4 per 100,000 invented nothing."""
    candidates = audit.equivalent_figures("25000", "one_in_n")
    assert "4" in candidates          # per 100,000
    assert "40" in candidates         # per million


def test_percent_does_not_generate_the_reciprocal():
    """100/50 = 2 matches something in almost any abstract (regression guard)."""
    assert "2" not in audit.equivalent_figures("50", "percent")


# ---------------------------------------------------------------------------
# Cache reading
# ---------------------------------------------------------------------------

def test_bibliographic_apparatus_is_not_searchable_evidence(cache):
    """Years, DOIs, page ranges and postal codes must not clear a real claim."""
    cache("PMID:1", "The condition affects 73% of the cohort.")
    numbers = audit.reference_numbers("PMID:1")
    assert "73" in numbers
    for noise in ("2016", "16035", "02115", "15", "26"):
        assert noise not in numbers, f"{noise} leaked from the bibliographic header"


def test_uncached_reference_reports_none(cache):
    assert audit.reference_numbers("PMID:404") is None


# ---------------------------------------------------------------------------
# Scope: the whole point of the tool
# ---------------------------------------------------------------------------

ENTRY = """name: Some Disease
phenotypes:
- name: Thing
  description: >-
    The thing affects {claim}% of patients.
  evidence:
  - reference: PMID:1
    snippet: irrelevant
genetic:
- name: GENE
  notes: unrelated
  evidence:
  - reference: PMID:2
    snippet: irrelevant
"""


def test_figure_supported_by_the_adjacent_reference_is_clean(tmp_path, cache):
    cache("PMID:1", "The thing affects 73% of patients.")
    cache("PMID:2", "Something else entirely.")
    report = _audit(tmp_path, ENTRY.format(claim=73))
    assert report.findings == []
    assert report.status == "OK"


def test_figure_absent_from_its_own_citation_is_flagged(tmp_path, cache):
    """The #7791 shape: a real, topical citation attached to a number it lacks."""
    cache("PMID:1", "The thing is common in this population.")
    cache("PMID:2", "Something else entirely.")
    report = _audit(tmp_path, ENTRY.format(claim=73))
    assert [f.verdict for f in report.findings] == ["NOT_IN_ADJACENT"]
    assert report.findings[0].figure == "73"
    assert report.findings[0].in_entry_corpus is False


def test_scope_is_adjacent_not_entry_wide(tmp_path, cache):
    """A figure elsewhere in the entry's literature does not vouch for this claim.

    Whole-entry scope is not merely looser, it is useless: the 33 references cited
    by Tuberous_Sclerosis_Complex.yaml contain all 90 two-digit integers between
    them, so any percentage would 'verify'.
    """
    cache("PMID:1", "The thing is common in this population.")
    cache("PMID:2", "An unrelated finding in 73% of a different cohort.")
    report = _audit(tmp_path, ENTRY.format(claim=73))
    assert [f.verdict for f in report.findings] == ["NOT_IN_ADJACENT"]
    # Still reported, but marked as present elsewhere so a curator can weigh it.
    assert report.findings[0].in_entry_corpus is True


def test_prose_with_no_adjacent_evidence_is_uncited_not_contradicted(tmp_path, cache):
    cache("PMID:2", "Something else entirely.")
    report = _audit(
        tmp_path,
        "name: Some Disease\ndescription: Affects 73% of patients.\n"
        "genetic:\n- name: GENE\n  evidence:\n  - reference: PMID:2\n    snippet: x\n",
    )
    assert [f.verdict for f in report.findings] == ["UNCITED"]
    assert report.status == "UNCITED"


def test_evidence_explanations_are_out_of_scope(tmp_path, cache):
    """``explanation`` sits beside a checked snippet; #7791 is about unchecked prose."""
    cache("PMID:1", "No numbers here.")
    report = _audit(
        tmp_path,
        "name: Some Disease\nphenotypes:\n- name: Thing\n  evidence:\n"
        "  - reference: PMID:1\n    snippet: x\n"
        "    description: Seen in 73% of cases.\n",
    )
    assert report.findings == []


def test_uncached_adjacent_reference_does_not_manufacture_a_contradiction(tmp_path, cache):
    """Nothing to compare against is 'uncited', never 'not supported'."""
    report = _audit(tmp_path, ENTRY.format(claim=73))
    assert {f.verdict for f in report.findings} == {"UNCITED"}
