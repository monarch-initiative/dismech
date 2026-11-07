"""Build a citable paragraph index from an OECD Test Guideline PDF.

The guideline is the authority for what each test method measures, but its text is
unstructured, so a claim sourced from it cannot be checked without re-reading the PDF.
This script turns the PDF into a paragraph index: every numbered paragraph of the
in-scope sections, with the division and paragraph number that cite it.

It extracts text and nothing else. Which paragraph supports which fact about a method is
a judgement, made against this index rather than against the PDF. The records carrying
those judgements are checked by `scripts/check_tg_extraction.py`; the skill that writes
them is still to come (see `docs/oecd-tg-extraction.md` and issue #16338).

Paragraph numbering restarts in every division, so a bare paragraph number is ambiguous
across the five methods TG 442D describes. The citation key therefore carries both:
`442D/IA/3` is paragraph 3 of Appendix IA, not paragraph 3 of the guideline.

Text is extracted in pypdf's ``layout`` mode. The default ``plain`` mode inserts spaces
inside words on this document -- "asses sing", "Ker atinoSens" -- which would make every
quote unusable as a verbatim quote, since whitespace normalisation collapses runs of
spaces but does not close a gap inside a word.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import re
import sys
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path

from pypdf import PdfReader

# A division is a top-level part of the guideline, rendered as an indented title block.
# Paragraph numbering restarts in each one.
DIVISION_TITLES = {
    "GENERAL INTRODUCTION": ("general-introduction", None),
}
APPENDIX_TITLE_RE = re.compile(r"^Appendix\s+(I[A-D])\s*:", re.IGNORECASE)

# Section headings inside a division are flush-left and upper-case.
SECTION_HEADING_RE = re.compile(r"^[A-Z][A-Z0-9 ,\-:()/&'–—’.]{5,}$")

# A numbered paragraph starts flush-left: "3." then the wide gap the guideline uses
# before the body text.
PARAGRAPH_START_RE = re.compile(r"^(\d{1,3})\.\s\s+(\S.*)$")

# Running header and footer, dropped before anything is classified. Blank lines are not
# noise: they mark the boundary between a paragraph and the heading that follows it, and
# are the only reliable way to tell a mixed-case subheading from a wrapped line of body
# text, since both are flush-left.
NOISE_RE = re.compile(
    r"^\s*(?:OECD/OCDE\s|©\s*OECD\s*\(\d{4}\)|\d{1,3}\s*$)",
)

# The sections worth extracting. `PROCEDURE`, `DATA AND REPORTING`, the prediction model
# and the annexes are out of scope by decision, so a heading that matches none of these
# closes the current in-scope run.
IN_SCOPE_SECTION_PATTERNS = (
    re.compile(r"^INITIAL CONSIDERATIONS\b"),
    re.compile(r"^PRINCIPLE OF THE TEST\b"),
)

# The guideline's own front matter repeats its title and citation; paragraph numbering
# has not started yet, so nothing before the first division title is of interest.


@dataclass
class Paragraph:
    """One numbered paragraph, with what is needed to cite and verify it."""

    division_id: str
    appendix: str | None
    section: str | None
    number: int
    text: str
    subheading: str | None = None
    pdf_pages: list[int] = field(default_factory=list)

    @property
    def citation_key(self) -> str:
        scope = self.appendix or "GI"
        return f"442D/{scope}/{self.number}"

    def to_dict(self) -> dict[str, object]:
        return {
            "citation_key": self.citation_key,
            "division_id": self.division_id,
            "appendix": self.appendix,
            "section": self.section,
            "subheading": self.subheading,
            "paragraph_number": self.number,
            "pdf_pages": self.pdf_pages,
            "text": self.text,
        }


def page_lines(reader: PdfReader, index: int) -> list[str]:
    """Layout-mode lines for one page, with the running header and footer removed.

    pypdf logs "Rotated text discovered" to stderr for some pages; it is captured so a
    run's output stays machine-readable, and reported by the caller instead.
    """
    captured = io.StringIO()
    with contextlib.redirect_stderr(captured):
        text = reader.pages[index].extract_text(extraction_mode="layout")
    lines = [ln for ln in text.splitlines() if not NOISE_RE.match(ln)]
    return lines


def classify_division(line: str) -> tuple[str, str | None] | None:
    """Return (division_id, appendix) when this line is a division title."""
    stripped = line.strip()
    if not line.startswith(" "):
        # Division titles are indented title blocks. A flush-left line of the same text
        # is a table-of-contents entry or a running head.
        return None
    if stripped in DIVISION_TITLES:
        return DIVISION_TITLES[stripped]
    match = APPENDIX_TITLE_RE.match(stripped)
    if match:
        appendix = match.group(1).upper()
        return f"appendix-{appendix.lower()}", appendix
    return None


def is_in_scope_section(heading: str) -> bool:
    return any(pattern.match(heading) for pattern in IN_SCOPE_SECTION_PATTERNS)


def normalise(text: str) -> str:
    """Collapse the whitespace that justified typesetting leaves inside a line."""
    return close_hyphen_gaps(re.sub(r"\s+", " ", text).strip())


# A hyphenated compound can arrive split in two ways, and both make the word
# unquotable. Across a line break, the join inserts the space ("non-" +
# "sensitisers"); within one line, pypdf's `layout` mode preserves the horizontal
# position of justified text and a wide gap after the hyphen comes through as a
# space ("Reverse Transcription- quantitative PCR"). Both are the mid-word gap
# defect pypdf's `plain` mode produces ("con sidered"); they survived because the
# gap sits at a hyphen, where it reads as ordinary punctuation.
#
# The hyphen itself is kept. Every such break in TG 442D is a lexical compound --
# "up-regulated", "Kelch-like", "IL-8", "Reverse Transcription-quantitative" -- and
# keeping a character the source printed fails conservatively if a guideline ever
# breaks a word at a soft hyphen: that quote will not verify, rather than the
# paragraph text being silently altered.
#
# The exception is a suspended hyphen -- "5- and 10-fold" -- where the space is
# correct. Same shape, and the same guard, as COORD_RE in
# scripts/check_folded_hyphens.py, so the two detectors agree by construction.
COORD_RE = re.compile(r"^(and|or|to|vs|nor|&)\b", re.IGNORECASE)

# A word character, a hyphen, one space, then a word character. Requiring a word
# character *before* the hyphen is what keeps a spaced dash used as punctuation
# (" - ") out of this.
HYPHEN_GAP_RE = re.compile(r"(?<=\w)- (?=\w)")


def close_hyphen_gaps(text: str) -> str:
    """Close a spurious space after a hyphen inside a single line."""

    def repair(match: re.Match[str]) -> str:
        return "- " if COORD_RE.match(text[match.end() :]) else "-"

    return HYPHEN_GAP_RE.sub(repair, text)


def join_lines(left: str, right: str) -> str:
    """Join two lines of one paragraph, closing a hyphenated line break."""
    if not left or not right:
        return left or right
    if left.endswith("-") and right[0].isalnum() and not COORD_RE.match(right):
        return f"{left}{right}"
    return f"{left} {right}"


def parse_pages(pages: Sequence[Sequence[str]]) -> tuple[list[Paragraph], list[str]]:
    """Parse already-extracted page lines into paragraphs and the headings seen.

    Takes lines rather than a PDF so the classification rules can be tested against
    short synthetic pages. The guideline PDF is 98 pages and is not committed.
    """
    paragraphs: list[Paragraph] = []
    division_id: str | None = None
    appendix: str | None = None
    section: str | None = None
    # A division's text before its first upper-case heading belongs to the division
    # itself; that is where the General Introduction's ten paragraphs live.
    in_scope = False
    current: Paragraph | None = None
    seen_sections: list[str] = []

    subheading: str | None = None
    for page_number, lines in enumerate(pages, start=1):
        # A page opens with the running header, then blank lines. Those blanks are an
        # artifact of stripping the header, not a paragraph boundary -- a paragraph that
        # continues across a page break would otherwise look like it ended.
        at_page_start = True
        pending_break = False

        for line in lines:
            if not line.strip():
                if not at_page_start:
                    pending_break = True
                continue

            division = classify_division(line)
            if division is not None:
                division_id, appendix = division
                section, subheading, in_scope, current = None, None, True, None
                at_page_start, pending_break = False, False
                continue

            if division_id is None:
                at_page_start = False
                continue  # front matter and table of contents

            stripped = line.strip()
            if not line.startswith(" ") and SECTION_HEADING_RE.match(stripped):
                section = normalise(stripped)
                seen_sections.append(f"{division_id}:{section}")
                in_scope = is_in_scope_section(section)
                subheading, current = None, None
                at_page_start, pending_break = False, False
                continue

            was_at_page_start, at_page_start = at_page_start, False
            start = PARAGRAPH_START_RE.match(line)

            if not in_scope:
                pending_break = False
                continue

            if start:
                current = Paragraph(
                    division_id=division_id,
                    appendix=appendix,
                    section=section,
                    number=int(start.group(1)),
                    text=normalise(start.group(2)),
                    subheading=subheading,
                    pdf_pages=[page_number],
                )
                paragraphs.append(current)
                pending_break = False
                continue

            # A flush-left line after a blank, inside a division, is the mixed-case
            # subheading that groups the paragraphs below it -- not body text. Appending
            # it would put heading words inside a paragraph, and so inside any quote
            # taken from the end of that paragraph.
            if not line.startswith(" ") and pending_break and not was_at_page_start:
                subheading = normalise(stripped)
                current, pending_break = None, False
                continue

            if current is None:
                # A subheading wraps onto a second line, or a stray line precedes the
                # division's first paragraph.
                if subheading is not None and not pending_break:
                    subheading = join_lines(subheading, normalise(stripped))
                continue

            addition = normalise(line)
            if addition:
                current.text = join_lines(current.text, addition)
                if page_number not in current.pdf_pages:
                    current.pdf_pages.append(page_number)
            pending_break = False

    return paragraphs, seen_sections


def extract(pdf_path: Path) -> dict[str, object]:
    """Extract the in-scope numbered paragraphs of a Test Guideline PDF."""
    reader = PdfReader(str(pdf_path))
    pages = [page_lines(reader, i) for i in range(len(reader.pages))]
    paragraphs, seen_sections = parse_pages(pages)

    return {
        "source": {
            "path": pdf_path.name,
            "sha256": hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
            "pages": len(pages),
        },
        "extraction": {
            "tool": "pypdf",
            "mode": "layout",
            "scope": [pattern.pattern for pattern in IN_SCOPE_SECTION_PATTERNS],
            "note": (
                "Numbered paragraphs of the General Introduction and of each "
                "appendix's Initial Considerations and Principle of the Test "
                "sections. PROCEDURE, DATA AND REPORTING, the prediction model and "
                "the annexes are out of scope."
            ),
        },
        "sections_seen": seen_sections,
        "paragraphs": [p.to_dict() for p in paragraphs],
    }


def summarise(index: dict[str, object]) -> str:
    paragraphs = index["paragraphs"]
    assert isinstance(paragraphs, list)
    by_scope: dict[str, list[int]] = {}
    for item in paragraphs:
        assert isinstance(item, dict)
        scope = str(item["appendix"] or "General Introduction")
        by_scope.setdefault(scope, []).append(int(item["paragraph_number"]))
    lines = [f"{len(paragraphs)} in-scope paragraphs"]
    for scope, numbers in by_scope.items():
        gaps = [
            n
            for n in range(min(numbers), max(numbers) + 1)
            if n not in set(numbers)
        ]
        detail = f"{len(numbers)} paragraphs, {min(numbers)}-{max(numbers)}"
        if gaps:
            detail += f", MISSING {gaps}"
        lines.append(f"  {scope}: {detail}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="The Test Guideline PDF.")
    parser.add_argument(
        "--out",
        type=Path,
        help="Where to write the paragraph index. Omit to print the summary only.",
    )
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"not a file: {args.pdf}")

    index = extract(args.pdf)
    print(summarise(index), file=sys.stderr)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
        print(f"wrote {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
