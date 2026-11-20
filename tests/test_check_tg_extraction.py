"""Quote verification for facts extracted from an OECD Test Guideline.

The contract is that every extracted fact carries a value, the guideline's own sentence,
and the paragraph it came from. These tests pin what the checker can and cannot catch,
because the difference matters: a verbatim quote attached to the wrong claim passes every
check here and is exactly the error the extraction exists to prevent.
"""

from __future__ import annotations

from scripts.check_snippet_length import MIN_SNIPPET_WORDS
from scripts.check_tg_extraction import (
    ABSENCE_MARKERS,
    MIN_QUOTE_WORDS,
    check,
    normalise,
)

INDEX = {
    "paragraphs": [
        {
            "citation_key": "442D/GI/3",
            "text": (
                "These test methods have all been considered scientifically valid. "
                "The KeratinoSens™ test method first underwent a validation study."
            ),
        },
        {
            "citation_key": "442D/IA/1",
            "text": (
                "The test method described in this Appendix to Test Guideline 442D "
                "addresses the second key event of the skin sensitisation AOP (1), "
                "namely keratinocytes activation."
            ),
        },
        {
            "citation_key": "442D/IC/3",
            "text": (
                "The EpiSensA is considered a VRM with regards to test methods "
                "quantifying changes in the expression of marker genes associated "
                "with keratinocyte activation (ATF3, IL-8, GCLM, and DNAJB4)."
            ),
        },
    ]
}


def record(field: str, **kwargs: object) -> list[dict]:
    return [{"method": "KeratinoSens", "fields": {field: kwargs}}]


def test_a_verbatim_quote_in_the_cited_paragraph_verifies() -> None:
    problems = check(
        INDEX,
        record(
            "key_event",
            value=2,
            paragraph="442D/IA/1",
            quote="addresses the second key event of the skin sensitisation AOP",
        ),
    )
    assert problems == []


def test_a_real_quote_cited_to_the_wrong_paragraph_is_located() -> None:
    """The message names where the sentence actually is, so the fix is obvious."""
    problems = check(
        INDEX,
        record(
            "validation_route",
            value="VRM",
            paragraph="442D/IA/1",
            quote="These test methods have all been considered scientifically valid",
        ),
    )
    assert len(problems) == 1
    assert "cites 442D/IA/1 but appears in 442D/GI/3" in problems[0]


def test_a_fabricated_quote_is_rejected() -> None:
    problems = check(
        INDEX,
        record(
            "reporter",
            value="luciferase",
            paragraph="442D/IA/1",
            quote="the reporter construct is driven by the ARE of the human NQO1 gene",
        ),
    )
    assert len(problems) == 1
    assert "does not appear in 442D/IA/1 or anywhere in scope" in problems[0]


def test_a_value_without_a_quote_is_reported_not_skipped() -> None:
    problems = check(INDEX, record("cell_line", value="HaCaT-derived"))
    assert problems == ["KeratinoSens / cell_line: value carries no quote"]


def test_an_out_of_scope_paragraph_reference_is_reported() -> None:
    """Paragraph 16 of Appendix IA is in PROCEDURE, which is not extracted."""
    problems = check(
        INDEX,
        record(
            "dosing",
            value="12 concentrations",
            paragraph="442D/IA/16",
            quote="12 master concentrations",
        ),
    )
    assert len(problems) == 1
    assert "not in the index" in problems[0]


def test_the_trademark_marker_does_not_decide_whether_a_quote_verifies() -> None:
    """The guideline writes "KeratinoSens™" in body text and "KeratinoSensTM" in titles."""
    for typed in ("KeratinoSens™", "KeratinoSens(TM)", "KeratinoSens"):
        problems = check(
            INDEX,
            record(
                "name",
                value="KeratinoSens",
                paragraph="442D/GI/3",
                quote=f"The {typed} test method first underwent a validation study",
            ),
        )
        assert problems == [], f"{typed} should verify, got {problems}"


def test_a_mid_word_gap_still_fails() -> None:
    """pypdf's default mode emits "con sidered". That is a broken extraction, not
    typography, so it must not be normalised away."""
    problems = check(
        INDEX,
        record(
            "status",
            value="valid",
            paragraph="442D/GI/3",
            quote="These test methods have all been con sidered scientifically valid",
        ),
    )
    assert len(problems) == 1


def test_whitespace_and_case_do_not_decide_a_match() -> None:
    assert normalise("The  in  vitro   method") == "the in vitro method"
    assert normalise("ATF3, IL-8") == normalise("atf3, il-8")
    assert normalise("α-Sens®") == "alpha-sens"


def test_both_alpha_characters_the_guideline_uses_fold_together() -> None:
    """TG 442D paragraph ID/3 writes the method name once with U+237A.

    Every other mention uses U+03B1, so without folding both the same name
    compares two ways and a quote copied from one sentence fails against the
    other.
    """
    assert normalise("⍺-Sens®") == normalise("α-Sens®") == "alpha-sens"


def test_the_checker_cannot_tell_whether_a_quote_supports_its_value() -> None:
    """The error this whole exercise exists to catch needs a reader, not a script.

    IL-8 is a marker gene in a keratinocyte-activation assay, which is Key Event 2. The
    quote below is verbatim and correctly located, and the value it is attached to is
    wrong. Nothing here objects.
    """
    problems = check(
        INDEX,
        record(
            "key_event",
            value=3,
            paragraph="442D/IC/3",
            quote="marker genes associated with keratinocyte activation (ATF3, IL-8",
        ),
    )
    assert problems == []


def test_a_bare_value_is_reported_rather_than_skipped() -> None:
    """`"key_event": 2` is the exact shape this tool exists to reject.

    It is not an object, so it carries neither a quote nor a paragraph. Skipping a
    non-object field meant this record came back clean, with an exit code of 0.
    """
    problems = check(INDEX, [{"method": "KeratinoSens", "fields": {"key_event": 2}}])
    assert problems == ["KeratinoSens / key_event: value carries no quote"]


def test_a_quote_that_normalises_to_nothing_does_not_verify() -> None:
    """"" is a substring of every paragraph, so this would verify against anything."""
    for quote in ("(TM)", "™", "   "):
        problems = check(
            INDEX, record("name", value="x", paragraph="442D/GI/3", quote=quote)
        )
        assert len(problems) == 1, f"{quote!r} should not verify"
        assert "empty once normalised" in problems[0]


def test_a_quote_below_the_word_floor_does_not_verify() -> None:
    """A fragment matches in too many places for the match to locate anything."""
    problems = check(
        INDEX, record("name", value="x", paragraph="442D/IA/1", quote="the test method")
    )
    assert len(problems) == 1
    assert f"below the {MIN_QUOTE_WORDS}-word floor" in problems[0]


def test_the_word_floor_matches_the_evidence_snippet_floor() -> None:
    """Same floor, and the same reason, as the repository's snippet-length gate."""
    assert MIN_QUOTE_WORDS == MIN_SNIPPET_WORDS


# ---------------------------------------------------------------------------
# Recording an absence
#
# An omitted key means "nobody extracted this". The two markers below are
# different claims, and the checker holds each to its own burden of proof so
# that neither can be used to wave a field away.
# ---------------------------------------------------------------------------

MARKER_GENES = (
    "quantifying changes in the expression of marker genes associated "
    "with keratinocyte activation"
)


def test_not_applicable_needs_a_quote_like_any_other_claim() -> None:
    """"This method has none" is a claim about the guideline, so it is sourced."""
    assert check(
        INDEX,
        record(
            "source_gene",
            absent="NOT_APPLICABLE",
            quote=MARKER_GENES,
            paragraph="442D/IC/3",
        ),
    ) == []


def test_not_applicable_without_a_quote_is_rejected() -> None:
    problems = check(INDEX, record("source_gene", absent="NOT_APPLICABLE"))
    assert problems
    assert "carries no quote" in problems[0]


def test_not_applicable_with_a_fabricated_quote_is_still_rejected() -> None:
    """The absence marker buys no exemption from quote verification."""
    problems = check(
        INDEX,
        record(
            "source_gene",
            absent="NOT_APPLICABLE",
            quote="this method carries no reporter construct of any kind",
            paragraph="442D/IC/3",
        ),
    )
    assert problems
    assert "does not appear" in problems[0]


def test_not_in_indexed_scope_needs_a_note_and_takes_no_quote() -> None:
    assert check(
        INDEX,
        record(
            "exposure_schedule",
            absent="NOT_IN_INDEXED_SCOPE",
            note="No in-scope paragraph states the exposure duration for this method.",
        ),
    ) == []


def test_not_in_indexed_scope_without_a_note_is_rejected() -> None:
    problems = check(INDEX, record("exposure_schedule", absent="NOT_IN_INDEXED_SCOPE"))
    assert problems
    assert "carries no note" in problems[0]


def test_not_in_indexed_scope_carrying_a_quote_is_rejected() -> None:
    """A quote contradicts the claim: the claim is that there is nothing to quote."""
    problems = check(
        INDEX,
        record(
            "exposure_schedule",
            absent="NOT_IN_INDEXED_SCOPE",
            note="Stated nowhere in scope.",
            quote=MARKER_GENES,
            paragraph="442D/IC/3",
        ),
    )
    assert any("carries a quote" in m for m in problems)


def test_a_field_cannot_be_both_present_and_absent() -> None:
    problems = check(
        INDEX,
        record(
            "source_species",
            value="rat",
            absent="NOT_APPLICABLE",
            quote=MARKER_GENES,
            paragraph="442D/IC/3",
        ),
    )
    assert any("both a value and absent" in m for m in problems)


def test_an_invented_absence_marker_is_rejected() -> None:
    """The vocabulary is closed, so `absent: UNKNOWN` cannot be smuggled in."""
    problems = check(INDEX, record("source_gene", absent="UNKNOWN"))
    assert problems
    assert "not one of" in problems[0]
    for marker in ABSENCE_MARKERS:
        assert marker in problems[0]
