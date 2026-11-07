"""Classification rules behind the OECD Test Guideline paragraph index.

The guideline PDF is 98 pages and is not committed, so these tests exercise
`parse_pages` against short synthetic pages laid out the way pypdf's ``layout`` mode
renders the real document: an indented division title, flush-left upper-case section
headings, flush-left ``N.`` paragraph starts with a wide gap, indented bullets, and a
running header that `page_lines` has already removed.

Each test below pins a failure that happened while the parser was written.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from scripts.extract_oecd_tg import (
    classify_division,
    close_hyphen_gaps,
    is_in_scope_section,
    join_lines,
    parse_pages,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

# "GENERAL INTRODUCTION" and "Appendix IA:" are rendered as indented title blocks.
DIVISION = "        GENERAL INTRODUCTION"
APPENDIX_IA = "        Appendix IA: In Vitro Skin Sensitisation:"


def body(text: str) -> str:
    """A numbered paragraph's first line, with the guideline's wide gap after "N."."""
    return text


def test_paragraph_is_keyed_by_division_because_numbering_restarts() -> None:
    """A bare paragraph number is ambiguous: every appendix starts again at 1."""
    pages = [
        [
            DIVISION,
            "",
            "1.                     The first paragraph of the introduction.",
            "",
            APPENDIX_IA,
            "",
            "INITIAL CONSIDERATIONS, APPLICABILITY AND LIMITATIONS",
            "",
            "1.                     The first paragraph of Appendix IA.",
        ]
    ]
    paragraphs, _ = parse_pages(pages)
    assert [p.citation_key for p in paragraphs] == ["442D/GI/1", "442D/IA/1"]
    assert [p.appendix for p in paragraphs] == [None, "IA"]


def test_subheading_is_not_absorbed_into_the_paragraph_above_it() -> None:
    """A mixed-case subheading is flush-left, exactly like a wrapped body line.

    Treating it as body text put heading words inside the paragraph, and so inside any
    quote taken from the end of that paragraph.
    """
    pages = [
        [
            DIVISION,
            "",
            "3.                     These test methods have all been considered valid.",
            "It was reviewed by an independent peer review panel (17).",
            "",
            "",
            "Background and principles of the test methods",
            "",
            "4.                     The assessment has historically involved animals.",
        ]
    ]
    paragraphs, _ = parse_pages(pages)
    assert paragraphs[0].text.endswith("peer review panel (17).")
    assert "Background" not in paragraphs[0].text
    assert paragraphs[1].subheading == "Background and principles of the test methods"


def test_a_subheading_that_wraps_is_joined_rather_than_overwritten() -> None:
    pages = [
        [
            DIVISION,
            "",
            "3.                     A paragraph.",
            "",
            "",
            "Background and principles of the test methods included in the Key Event based Test",
            "Guidelines",
            "",
            "4.                     Another paragraph.",
        ]
    ]
    paragraphs, _ = parse_pages(pages)
    assert paragraphs[1].subheading == (
        "Background and principles of the test methods included in the Key Event "
        "based Test Guidelines"
    )


def test_paragraph_continues_across_a_page_break() -> None:
    """The blanks left by stripping a page's running header are not a boundary."""
    pages = [
        [
            DIVISION,
            "",
            "3.                     These test methods have all been considered",
            "scientifically valid. The KeratinoSens test method",
        ],
        [
            "",
            "",
            "underwent a validation study followed by peer review (8).",
        ],
    ]
    paragraphs, _ = parse_pages(pages)
    assert len(paragraphs) == 1
    assert paragraphs[0].text.endswith("followed by peer review (8).")
    assert paragraphs[0].pdf_pages == [1, 2]


def test_out_of_scope_sections_are_seen_but_not_extracted() -> None:
    pages = [
        [
            APPENDIX_IA,
            "",
            "PRINCIPLE OF THE TEST",
            "",
            "8.                     The test method uses a luciferase reporter gene.",
            "",
            "PROCEDURE",
            "",
            "12.                    A DB-ALM protocol is available.",
            "",
            "DATA AND REPORTING",
            "",
            "26.                    Calculations are performed as follows.",
        ]
    ]
    paragraphs, seen = parse_pages(pages)
    assert [p.citation_key for p in paragraphs] == ["442D/IA/8"]
    assert "appendix-ia:PROCEDURE" in seen
    assert "appendix-ia:DATA AND REPORTING" in seen


def test_bullets_stay_with_the_paragraph_that_introduces_them() -> None:
    pages = [
        [
            DIVISION,
            "",
            "2.                     The test methods currently described include:",
            "        •   The ARE-Nrf2 luciferase KeratinoSens™ test method (Appendix IA),",
            "        •   The ARE-Nrf2 luciferase LuSens test method (Appendix IB).",
        ]
    ]
    paragraphs, _ = parse_pages(pages)
    assert len(paragraphs) == 1
    assert "KeratinoSens™ test method (Appendix IA)" in paragraphs[0].text
    assert "LuSens test method (Appendix IB)" in paragraphs[0].text


def test_justified_whitespace_runs_are_collapsed() -> None:
    """Justified lines carry multi-space runs that would break an exact-quote match."""
    pages = [
        [
            DIVISION,
            "",
            "2.                     The  in  vitro  ARE-Nrf2  luciferase  test  method.",
        ]
    ]
    paragraphs, _ = parse_pages(pages)
    assert paragraphs[0].text == "The in vitro ARE-Nrf2 luciferase test method."


def test_a_table_of_contents_line_is_not_a_division_title() -> None:
    """Division titles are indented; the same words flush-left are a contents entry."""
    assert classify_division(DIVISION) == ("general-introduction", None)
    assert classify_division("GENERAL INTRODUCTION                       5") is None
    assert classify_division(APPENDIX_IA) == ("appendix-ia", "IA")


def test_appendix_ic_heading_variant_is_in_scope() -> None:
    """Appendix IC drops "APPLICABILITY" from the heading the other three use."""
    assert is_in_scope_section("INITIAL CONSIDERATIONS, APPLICABILITY AND LIMITATIONS")
    assert is_in_scope_section("INITIAL CONSIDERATIONS AND LIMITATIONS")
    assert is_in_scope_section("PRINCIPLE OF THE TEST")
    assert not is_in_scope_section("PROCEDURE")
    assert not is_in_scope_section("DATA AND REPORTING")
    assert not is_in_scope_section("APPENDIX IA - ANNEX 1: PROFICIENCY SUBSTANCES")


def test_committed_index_numbering_is_contiguous_in_every_division() -> None:
    """Guards the heading regex against silently truncating an in-scope section.

    `SECTION_HEADING_RE` matches any flush-left upper-case line, which includes table
    rows such as "C EGDMA EGDMA EGDMA". Today every such row falls inside a section that
    is already out of scope, so nothing is lost. One inside an in-scope section would
    close the in-scope run early and drop the paragraphs after it -- with no error, and
    no sign in the output except a gap in the numbering. So the numbering is the guard.
    """
    index = json.loads(
        (REPO_ROOT / "data" / "oecd_tg" / "tg442d-paragraphs.json").read_text()
    )
    by_division: dict[str, list[int]] = {}
    for paragraph in index["paragraphs"]:
        key = paragraph["appendix"] or "GI"
        by_division.setdefault(key, []).append(paragraph["paragraph_number"])

    assert set(by_division) == {"GI", "IA", "IB", "IC", "ID"}
    for division, numbers in sorted(by_division.items()):
        assert numbers == sorted(numbers), f"{division} is out of order: {numbers}"
        assert numbers == list(range(1, len(numbers) + 1)), (
            f"{division} numbering is not 1..N: {numbers}"
        )


def test_a_word_hyphenated_across_a_line_break_is_rejoined() -> None:
    """Joining the lines with a space made "non-sensitisers" unquotable.

    The word is split at the hyphen, so a curator typing "non-sensitisers" matches
    nothing: the checker folds typography but deliberately does not close a gap
    inside a word.
    """
    pages = [
        [
            DIVISION,
            "",
            "2.                     It supports the discrimination between sensitisers and non-",
            "sensitisers for hazard identification.",
        ]
    ]
    paragraphs, _ = parse_pages(pages)
    assert "non-sensitisers for hazard" in paragraphs[0].text
    assert "non- sensitisers" not in paragraphs[0].text


def test_a_suspended_hyphen_keeps_its_space() -> None:
    """"5- and 10-fold" is correct as written, and must not be joined."""
    assert join_lines("induction was 5-", "and 10-fold") == "induction was 5- and 10-fold"
    assert close_hyphen_gaps("pre- and post-exposure") == "pre- and post-exposure"


def test_a_hyphen_gap_inside_one_line_is_closed() -> None:
    """Justified text in `layout` mode renders a wide gap after a hyphen as a space.

    Same broken word as the line-break case, a different cause: it arrives inside
    a single extracted line, so rejoining lines never sees it.
    """
    assert close_hyphen_gaps("Reverse Transcription- quantitative PCR") == (
        "Reverse Transcription-quantitative PCR"
    )
    assert close_hyphen_gaps("a three- dimensional model") == "a three-dimensional model"


def test_a_spaced_dash_used_as_punctuation_is_left_alone() -> None:
    """Requiring a word character before the hyphen is what excludes this."""
    assert close_hyphen_gaps("the method - which is validated") == (
        "the method - which is validated"
    )


def test_committed_index_has_no_word_split_at_a_hyphen() -> None:
    """A split word cannot be quoted, and nothing downstream would report it.

    The checker compares a curator's quote against this text, so a paragraph
    carrying "IL- 8" silently makes the marker-gene list unquotable. Seventeen such
    spots were committed before `join_lines` and `close_hyphen_gaps` existed.
    """
    index = json.loads(
        (REPO_ROOT / "data" / "oecd_tg" / "tg442d-paragraphs.json").read_text()
    )
    split = [
        (p["citation_key"], m.group(0))
        for p in index["paragraphs"]
        for m in re.finditer(r"\w- (?=\w)", p["text"])
        if not re.match(r"^(and|or|to|vs|nor|&)\b", p["text"][m.end() :], re.IGNORECASE)
    ]
    assert split == []


def test_committed_index_paragraphs_are_whole_sentences() -> None:
    """A paragraph cut mid-sentence means a quote taken from its end cannot verify."""
    index = json.loads(
        (REPO_ROOT / "data" / "oecd_tg" / "tg442d-paragraphs.json").read_text()
    )
    truncated = [
        p["citation_key"]
        for p in index["paragraphs"]
        if not p["text"].rstrip().endswith((".", ".)", ".”"))
    ]
    assert truncated == []
