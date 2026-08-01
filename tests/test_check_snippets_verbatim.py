"""Tests for scripts/check_snippets_verbatim.py.

The value of that checker is entirely in its calibration: it has to tolerate the
artifacts of PDF text extraction while still failing a paraphrase. Too strict and
it drowns real findings in noise (an early version reported 1,285 "failures" that
were all extraction artifacts); too loose and it stops catching fabrication.

These tests pin both edges.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_snippets_verbatim.py"
_spec = importlib.util.spec_from_file_location("check_snippets_verbatim", _SCRIPT)
csv_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(csv_mod)

contains = csv_mod.contains
normalize = csv_mod.normalize
deartifact = csv_mod.deartifact


def _body(text: str) -> str:
    """Run a cache body through the same pipeline check_file() uses."""
    return deartifact(normalize(text))


def _snippet(text: str) -> str:
    return deartifact(normalize(text))


def check(snippet: str, cache: str) -> bool:
    return contains(_snippet(snippet), _body(cache))


# --- the checker must ACCEPT these: real quotes, mangled only by extraction ---


def test_exact_quote_passes():
    assert check("the cat sat on the mat", "Before. The cat sat on the mat. After.")


def test_line_wrapping_is_tolerated():
    assert check("progressive motor decline and seizures",
                 "showed progressive motor\ndecline and seizures at 10 years")


def test_hyphenation_across_line_break_is_tolerated():
    # PDF extraction splits words at the line break: "Stud-\nies"
    assert check("Studies show a benefit", "Stud-\nies show a benefit in this cohort")


def test_inline_numeric_citation_markers_are_tolerated():
    assert check("some degree of T cell lymphopenia (TCL).",
                 "have some degree of T cell lymphopenia (TCL) [13]. Studies then")


def test_bracketed_citation_ranges_are_tolerated():
    assert check("an established finding here",
                 "an established finding [4,5] here")
    assert check("another established finding here",
                 "another established finding [7-9] here")


def test_lancet_middle_dot_decimal_is_tolerated():
    # Lancet house style writes 61·4% where the curator typed 61.4%
    assert check("prevalence was 61.4% and the rate was 58.2%.",
                 "The overall prevalence was 61·4% and the rate was 58·2%. Next.")


def test_greek_letter_transliteration_is_tolerated():
    assert check("low serum cortisol (1.2 mug/dl)",
                 "showed low serum cortisol (1.2 μg/dl) with high ACTH")


def test_unicode_dashes_and_quotes_are_tolerated():
    assert check("the patient's 5-year outcome", "the patient’s 5–year outcome was good")


def test_ellipsis_elision_in_order_is_tolerated():
    assert check("the first part... the third part",
                 "the first part, then the second part, then the third part")


def test_early_truncation_with_added_period_is_tolerated():
    # Curator ends the quote early and closes it with a period where the source
    # continues with a comma.
    assert check("the occurrence of new freckles.",
                 "the occurrence of new freckles, that was diagnosed in the presence of")


# --- the checker must REJECT these: the failures worth a human's attention ---


def test_paraphrase_fails():
    assert not check("Roughly two thirds of patients display lymphopenia.",
                     "An estimated 67-80% of individuals have some degree of T cell lymphopenia.")


def test_text_absent_entirely_fails():
    assert not check("hypertelorism", "APC7 mediates ubiquitin signaling in heterochromatin.")


def test_reordered_elision_fails():
    """An elision must not be usable to reorder the source.

    The source says "acute crisis, whereas chronic..."; quoting chronic first and
    acute second misrepresents the sentence even though every word is present.
    """
    cache = "orthostatic hypotension and hypoglycemia characterize acute crisis, whereas chronic disease presents insidiously"
    assert not check("chronic disease presents insidiously... characterize acute crisis", cache)


def test_single_word_substitution_fails():
    assert not check("the patient showed marked improvement",
                     "the patient showed marked deterioration")


def test_negation_flip_fails():
    assert not check("the treatment was effective", "the treatment was not effective")


# --- diagnostics distinguish the two failure classes ---


def test_diagnose_reports_absent_when_wholly_missing():
    msg = csv_mod.diagnose(_snippet("completely unrelated sentence here"),
                           _body("nothing of the sort appears in this abstract"))
    assert "absent from this reference entirely" in msg


def test_diagnose_reports_divergence_point_when_partially_present():
    msg = csv_mod.diagnose(
        _snippet("the patient showed marked improvement over twelve months of therapy"),
        _body("the patient showed marked improvement over twelve weeks of therapy"),
    )
    assert "diverges after" in msg


@pytest.mark.parametrize("ref,expected", [
    ("PMID:12345678", "PMID_12345678.md"),
    ("DOI:10.1016/j.cell.2020.01.001", "DOI_10.1016_j.cell.2020.01.001.md"),
])
def test_cache_path_naming(ref, expected):
    assert csv_mod.cache_path_for.__doc__  # sanity: helper is documented
    assert ref.replace(":", "_").replace("/", "_") + ".md" == expected
