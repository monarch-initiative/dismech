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
def test_cache_path_naming(ref, expected, tmp_path, monkeypatch):
    """cache_path_for maps a CURIE onto its cache filename."""
    monkeypatch.setattr(csv_mod, "CACHE_DIR", tmp_path)
    (tmp_path / expected).write_text("body")
    got = csv_mod.cache_path_for(ref)
    assert got is not None and got.name == expected


# --- second-round calibration: the residual noise a reviewer triaged by hand ---
# Every case below was an observed false positive in the first full-KB run.


def test_hyphen_with_spaces_on_both_sides_is_tolerated():
    # PDF extraction: "emo - tional"
    assert check("emotional lability", "showed emo - tional lability in childhood")


def test_hyphenated_compound_broken_at_line_break_still_matches():
    # "T-\ncell" must match a snippet written "T-cell"
    assert check("T-cell lymphopenia", "showed T-\ncell lymphopenia in most patients")


def test_hyphenated_compound_matches_unhyphenated_line_break():
    assert check("T-cell counts", "reduced T- cell counts were seen")


def test_space_before_punctuation_is_tolerated():
    assert check("ACVR1(R206H), the recurrent variant",
                 "ACVR1(R206H) , the recurrent variant was found")


@pytest.mark.parametrize("snip,cache", [
    ("a mean of 12 +/- 3 years", "a mean of 12 ± 3 years"),
    ("in patients <= 18 years", "in patients ⩽ 18 years"),
    ("a 3 x 4 cm lesion", "a 3 × 4 cm lesion"),
    ("the 5' untranslated region", "the 5′ untranslated region"),
])
def test_symbol_transliterations_are_tolerated(snip, cache):
    assert check(snip, cache)


def test_early_divergence_is_not_called_absent():
    """A quote that is present but wrong near its start is a divergence, not a fabrication.

    Gating "absent entirely" on a fixed 40-char prefix put these in the
    fabrication bucket and defeated the two-class triage.
    """
    cache = _body("Patients with the variant showed marked improvement over twelve weeks of therapy in this cohort")
    snippet = _snippet("Subjects with the variant showed marked improvement over twelve weeks of therapy in this cohort")
    msg = csv_mod.diagnose(snippet, cache)
    assert "absent from this reference entirely" not in msg
    assert "diverges after" in msg


def test_non_literature_prefixes_are_skipped_not_failed(tmp_path, monkeypatch):
    """url:/GEO:/metabolights: refs are dataset accessions, not prose to quote."""
    monkeypatch.setattr(csv_mod, "CACHE_DIR", tmp_path)
    doc = tmp_path / "d.yaml"
    doc.write_text(
        "evidence:\n"
        "- reference: url:https://example.org/dataset\n"
        "  snippet: anything at all\n"
        "- reference: GEO:GSE12345\n"
        "  snippet: also anything\n"
    )
    verified, failures, skipped = csv_mod.check_file(doc)
    assert failures == []
    assert len(skipped) == 2
    assert verified == 0


def test_every_snippet_on_an_uncached_reference_is_reported(tmp_path, monkeypatch):
    """A cache miss must not silently swallow the 2nd..Nth snippet on that ref."""
    monkeypatch.setattr(csv_mod, "CACHE_DIR", tmp_path)
    doc = tmp_path / "d.yaml"
    doc.write_text(
        "evidence:\n"
        "- reference: PMID:99999999\n"
        "  snippet: first quote\n"
        "- reference: PMID:99999999\n"
        "  snippet: second quote\n"
        "- reference: PMID:99999999\n"
        "  snippet: third quote\n"
    )
    verified, failures, _skipped = csv_mod.check_file(doc)
    assert verified == 0
    assert len(failures) == 3, "each snippet on the uncached ref must be reported"
    assert all("NO CACHE FILE" in f for f in failures)


def test_hyphen_rendered_as_space_is_tolerated():
    """A source hyphen quoted as a space must still match, and vice versa.

    Real case: L1_Syndrome quotes "spastic paraplegia shuffling gait adducted
    thumbs syndrome" where GeneReviews hyphenates the compound. Collapsing
    hyphens to nothing fixes "emo - tional" but breaks this; the squash fallback
    covers both.
    """
    assert check("spastic paraplegia shuffling gait adducted thumbs syndrome",
                 "the spastic paraplegia-shuffling gait-adducted thumbs syndrome phenotype")
    assert check("spastic paraplegia-shuffling gait syndrome",
                 "the spastic paraplegia shuffling gait syndrome phenotype")


def test_squash_fallback_still_rejects_a_paraphrase():
    """The looser fallback must not open a hole for real fabrication."""
    assert not check("roughly two thirds of patients had lymphopenia",
                     "An estimated 67-80% of individuals have some degree of T cell lymphopenia.")
    assert not check("the treatment was effective", "the treatment was not effective")
    assert not check("showed marked improvement", "showed marked deterioration")


def test_short_snippet_mostly_matching_is_a_divergence_not_an_absence():
    """A short quote that nearly matches is a slip, not a fabrication.

    Real case: the source reads "AMH) levels below detection sensitivity" and the
    curator quoted "AMH levels below detection sensitivity", dropping the paren.
    Too short for the 40-char window, so it was misfiled as "absent entirely".
    """
    msg = csv_mod.diagnose(
        _snippet("amh levels below detection sensitivity."),
        _body("Mullerian hormone (AMH) levels below detection sensitivity. In this cohort"),
    )
    assert "absent from this reference entirely" not in msg


def test_short_snippet_genuinely_absent_is_still_absent():
    msg = csv_mod.diagnose(_snippet("hypertelorism"),
                           _body("APC7 mediates ubiquitin signaling in heterochromatin."))
    assert "absent from this reference entirely" in msg


# --- third-round calibration: holes the reviewer found in the fixes themselves ---


def test_numeric_range_is_not_collapsed_into_a_point_value():
    """"1-2 months" must NOT match a snippet claiming "12 months".

    The hyphen collapse that fixes "emo - tional" also erased ranges, because \\w
    includes digits. A range quoted as a point value is exactly the class of
    misquote this tool exists to catch, so it must survive every normalization.
    """
    assert not check("12 months of therapy", "treated for 1-2 months of therapy")
    assert not check("510 mg daily", "dosed at 5-10 mg daily")
    assert not check("in 25 patients", "in 2-5 patients")


def test_real_ranges_still_match_themselves():
    assert check("1-2 months of therapy", "treated for 1-2 months of therapy")
    assert check("5-10 mg daily", "dosed at 5-10 mg daily")


def test_list_marker_hyphen_still_tolerated():
    """ORPHA rows begin with a list marker; letter-only stripping broke these."""
    assert check("- Autosomal recessive", "Inheritance\n- Autosomal recessive\n")


def test_frontmatter_is_not_searchable():
    """A snippet echoing the paper title must not 'verify' against the header."""
    cache = (
        "---\n"
        "reference_id: \"PMID:123\"\n"
        "title: Excess EEG beta-band oscillations in Dup15q syndrome\n"
        "authors:\n- Hipp JF\n"
        "---\n\n"
        "The abstract proper says something entirely different about mice.\n"
    )
    body = _body(csv_mod.strip_frontmatter(cache))
    assert not contains(_snippet("Excess EEG beta-band oscillations in Dup15q syndrome"), body)
    assert not contains(_snippet("Hipp JF"), body)
    assert contains(_snippet("something entirely different about mice"), body)


def test_skip_is_decided_by_missing_cache_not_by_prefix(tmp_path, monkeypatch):
    """A clinicaltrials ref WITH a cache body must be checked, not waved through."""
    monkeypatch.setattr(csv_mod, "CACHE_DIR", tmp_path)
    (tmp_path / "clinicaltrials_NCT01.md").write_text(
        "---\nreference_id: clinicaltrials:NCT01\n---\n\nA study of widgets in adults.\n"
    )
    doc = tmp_path / "d.yaml"
    doc.write_text(
        "evidence:\n"
        "- reference: clinicaltrials:NCT01\n"
        "  snippet: A study of widgets in adults.\n"
        "- reference: clinicaltrials:NCT01\n"
        "  snippet: A study of gizmos in children.\n"
    )
    verified, failures, skipped = csv_mod.check_file(doc)
    assert verified == 1, "the cached trial snippet should be verified, not skipped"
    assert len(failures) == 1, "the non-matching trial snippet should fail"
    assert skipped == []


# --- fourth-round: two one-liners the reviewer measured ---


def test_squash_digit_guard_strips_unless_both_neighbours_are_digits():
    """The guard must not be inverted.

    (?<!\\d)-(?!\\d) stripped only when NEITHER neighbour was a digit, which made
    a quote truncated on a trailing digit-hyphen unmatchable. Real case:
    ER_Positive_Breast_Cancer / PMID:32954927, diverging after 139/140 chars.
    """
    # stripped: at least one neighbour is not a digit
    assert csv_mod._squash("her2-negative") == "her2negative"
    assert csv_mod._squash("t-cell") == "tcell"
    assert csv_mod._squash("grade 3- ") == "grade3"
    # kept: both neighbours are digits, so this is a range
    assert csv_mod._squash("5-10") == "5-10"
    assert csv_mod._squash("1-2 months") == "1-2months"


def test_squash_still_shields_true_ranges():
    assert not check("510 mg daily", "dosed at 5-10 mg daily")
    assert not check("12 months", "over 1-2 months")
    assert not check("in 25 patients", "in 2-5 patients")


def test_markdown_header_after_frontmatter_is_not_searchable():
    """Dropping only the YAML block leaves a restated title/author header."""
    cache = (
        "---\n"
        "reference_id: \"PMID:123\"\n"
        "---\n\n"
        "# Excess EEG beta-band oscillations in Dup15q syndrome\n\n"
        "**Authors:** Hipp JF, Chamberlain S\n\n"
        "**Journal:** Neuron\n\n"
        "## Content\n\n"
        "The abstract proper concerns mice and lactate.\n"
    )
    body = _body(csv_mod.strip_frontmatter(cache))
    assert not contains(_snippet("Excess EEG beta-band oscillations in Dup15q syndrome"), body)
    assert not contains(_snippet("Hipp JF"), body)
    assert contains(_snippet("concerns mice and lactate"), body)


def test_structured_source_caches_are_left_whole():
    """ORPHA/CGGV tables have no '## Content' marker and ARE the quotable body."""
    cache = (
        "---\nreference_id: ORPHA:558\n---\n\n"
        "## Phenotypes\n\n"
        "| HP:0002616 | Aortic root aneurysm | Very frequent (99-80%) |\n"
    )
    body = _body(csv_mod.strip_frontmatter(cache))
    assert contains(_snippet("HP:0002616 | Aortic root aneurysm | Very frequent (99-80%)"), body)
