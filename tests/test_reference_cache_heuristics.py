"""Tests for reference cache hallucination heuristics (issue #871)."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_heuristics import (
    Finding,
    check_authors,
    check_cache_file,
    detect_alphabetical_common_surnames,
    detect_sequential_initials,
    scan_cache_dir,
)

ROOT = Path(__file__).parent.parent
CACHE_DIR = ROOT / "references_cache"


# The exact author list from the PR #714 / issue #871 incident. Surnames are
# *not* alphabetical here -- only the initials are sequential -- so the
# sequential-initials detector is what flags this real-world case.
ISSUE_871_AUTHORS = [
    "Smith AB",
    "Johnson CD",
    "Williams EF",
    "Brown GH",
    "Davis IJ",
    "Miller KL",
]

# A second LLM placeholder shape -- alphabetised top-50 English surnames --
# described in the issue body and the github-actions analysis comment.
PLACEHOLDER_ALPHABETICAL_AUTHORS = [
    "Brown A",
    "Davis B",
    "Johnson C",
    "Miller D",
    "Smith E",
    "Williams F",
]


# ---- Detector unit tests ---------------------------------------------------


def test_detects_issue_871_incident_via_sequential_initials():
    reasons = check_authors(ISSUE_871_AUTHORS)
    assert any("alphabetical sequence" in r for r in reasons), reasons


def test_detects_alphabetised_common_surname_placeholder():
    reasons = check_authors(PLACEHOLDER_ALPHABETICAL_AUTHORS)
    assert any("alphabetical order" in r for r in reasons), reasons


def test_alphabetical_surnames_requires_three_authors():
    # Two common surnames in order = not enough signal.
    assert detect_alphabetical_common_surnames(["Brown A", "Davis B"]) is None


def test_alphabetical_surnames_requires_alphabetical_order():
    assert (
        detect_alphabetical_common_surnames(["Smith A", "Brown B", "Davis C"]) is None
    )


def test_alphabetical_surnames_ignores_uncommon_names():
    # Real-world: short author list of common-but-not-listed surnames.
    assert (
        detect_alphabetical_common_surnames(["Möhring C", "Mańczak A", "Timotheou A"])
        is None
    )


def test_sequential_initials_requires_multi_letter_initials():
    # Single-letter initials are the PubMed norm; never a signal on their own.
    assert detect_sequential_initials(["Aaron A", "Bose B", "Choi C"]) is None


def test_sequential_initials_requires_alphabetical_order():
    assert detect_sequential_initials(["Foo CD", "Bar AB", "Baz EF"]) is None


def test_sequential_initials_requires_unique_letters():
    assert detect_sequential_initials(["Foo AB", "Bar BC", "Baz CD"]) is None


def test_real_pubmed_authors_pass_clean():
    # Sample drawn from references_cache/PMID_31558676.md (Israeli FA cohort).
    real = [
        "Steinberg-Shemer O",
        "Goldberg TA",
        "Yacobovich J",
        "Levin C",
        "Koren A",
        "Revel-Vilk S",
    ]
    assert check_authors(real) == []


def test_single_author_never_flags():
    assert check_authors(["Smith AB"]) == []


# ---- File / directory level tests -----------------------------------------


def test_check_cache_file_flags_synthetic_bad_cache(tmp_path: Path):
    bad = tmp_path / "PMID_99999999.md"
    bad.write_text(
        "---\n"
        'reference_id: "PMID:99999999"\n'
        "title: A fabricated study\n"
        "authors:\n" + "".join(f"- {a}\n" for a in ISSUE_871_AUTHORS) + "---\n\n"
        "fake content\n",
        encoding="utf-8",
    )
    finding = check_cache_file(bad)
    assert isinstance(finding, Finding)
    assert finding.reference_id == "PMID:99999999"
    assert any("alphabetical sequence" in r for r in finding.reasons)


def test_check_cache_file_passes_real_cache(tmp_path: Path):
    good = tmp_path / "PMID_12345678.md"
    good.write_text(
        "---\n"
        'reference_id: "PMID:12345678"\n'
        "title: A real-looking study\n"
        "authors:\n"
        "- Möhring C\n"
        "- Mańczak A\n"
        "- Timotheou A\n"
        "---\n\nabstract text\n",
        encoding="utf-8",
    )
    assert check_cache_file(good) is None


@pytest.mark.skipif(not CACHE_DIR.is_dir(), reason="references_cache/ not present")
def test_existing_repo_caches_have_no_findings():
    """Sweep the live cache: every existing entry should pass.

    If this fails, either we have a real hallucinated cache to investigate, or
    the heuristic is too aggressive and needs tightening.
    """
    findings = scan_cache_dir(CACHE_DIR)
    assert findings == [], "\n".join(f.format() for f in findings)
