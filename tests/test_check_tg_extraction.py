"""Quote verification for facts extracted from an OECD Test Guideline.

The contract is that every extracted fact carries a value, the guideline's own sentence,
and the paragraph it came from. These tests pin what the checker can and cannot catch,
because the difference matters: a verbatim quote attached to the wrong claim passes every
check here and is exactly the error the extraction exists to prevent.
"""

from __future__ import annotations

from scripts.check_tg_extraction import check, normalise

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
