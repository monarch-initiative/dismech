"""Check extracted Test Guideline facts against the paragraph they cite.

Every fact extracted from a Test Guideline carries three things: the value, the
guideline's own sentence, and the paragraph that sentence came from. This script checks
the third against the second: that each recorded quote really is a substring of the
cited paragraph in the committed index.

That is the whole point of recording a quote and a paragraph number rather than a
paraphrase. A field saying `"key_event": 2` cannot be checked by anything. The same
field with its sentence and `442D/IA/1` can be checked by a script, which is this one,
and by a person reading the PDF.

What it cannot check is whether the quoted sentence *supports* the value. A quote may be
verbatim, correctly located, and cited for a claim it does not make -- which is the
error this whole exercise exists to catch, and it needs a reader. See
`docs/oecd-tg-extraction.md`.

Comparison follows the repository's evidence convention: both sides are normalised
before matching, so publisher typography does not decide whether a quote verifies.
Whitespace runs collapse and the non-ASCII characters the guideline uses for its own
nomenclature fold to ASCII, so a quote typed as "KeratinoSens(TM)" matches a source
reading "KeratinoSens™". Mid-word gaps are not closed: that is a broken extraction
rather than a typographic variant, and it should fail.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# Characters the guideline uses that a curator cannot reasonably be expected to type,
# mapped to what they would type instead.
FOLD = {
    # The guideline writes the same method three ways -- "KeratinoSens™" in body text,
    # "KeratinoSensTM" in title blocks -- so the marker is dropped rather than folded to
    # a spelling, and a quote typed "KeratinoSens" or "KeratinoSens(TM)" matches either.
    "™": "",  # ™
    "®": "",  # ®
    "°": " degrees ",  # °
    "α": "alpha",
    "β": "beta",
    "μ": "u",  # micro sign vs mu
    "µ": "u",
    "–": "-",
    "—": "-",
    "−": "-",
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
    "≤": "<=",
    "≥": ">=",
    " ": " ",
    " ": " ",
    " ": " ",
}


# A quote shorter than this cannot locate anything: a three-word fragment matches in
# many paragraphs, which makes both the match and the "appears in <other paragraph>"
# diagnosis meaningless. Same floor, and the same reason, as MIN_SNIPPET_WORDS in
# scripts/check_snippet_length.py.
MIN_QUOTE_WORDS = 5

# The ASCII renderings a curator types for a trademark marker, dropped to match FOLD.
TRADEMARK_ASCII_RE = re.compile(r"\(\s*(?:tm|r)\s*\)", re.IGNORECASE)


def normalise(text: str) -> str:
    """Fold typography, then collapse whitespace. Case-insensitive.

    FOLD is applied before NFKC on purpose. NFKC expands "™" to "TM", which would turn
    "KeratinoSens™" into "KeratinoSensTM" and stop it matching a quote typed either
    "KeratinoSens" or "KeratinoSens(TM)".
    """
    for source, target in FOLD.items():
        text = text.replace(source, target)
    text = unicodedata.normalize("NFKC", text)
    text = TRADEMARK_ASCII_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip().casefold()


def iter_quotes(records: list[dict]) -> list[tuple[str, str, str, str]]:
    """Return (method, field, citation_key, quote) for every field of every record.

    A record's fields each carry `value`, `quote` and `paragraph`. Every field is
    returned, including one that carries no quote and one written as a bare value
    (`"key_event": 2`) rather than as an object. Those are the shapes this tool exists
    to reject, so they are reported as unsourced rather than skipped.
    """
    found: list[tuple[str, str, str, str]] = []
    for record in records:
        method = str(record.get("method", "<unnamed>"))
        for name, field in sorted(record.get("fields", {}).items()):
            if not isinstance(field, dict):
                found.append((method, name, "", ""))
                continue
            found.append(
                (
                    method,
                    name,
                    str(field.get("paragraph") or ""),
                    str(field.get("quote") or ""),
                )
            )
    return found


def check(index: dict, records: list[dict]) -> list[str]:
    """Return one message per problem found. An empty list means every quote verified."""
    paragraphs = {
        str(p["citation_key"]): normalise(str(p["text"]))
        for p in index["paragraphs"]
    }
    problems: list[str] = []

    for method, field, key, quote in iter_quotes(records):
        where = f"{method} / {field}"
        if not quote:
            problems.append(f"{where}: value carries no quote")
            continue
        if not key:
            problems.append(f"{where}: quote carries no paragraph reference")
            continue
        # The citation is checked before the quote's own usability: "cites a paragraph
        # that is not in the index" names a concrete fix, and holds whatever the quote
        # turns out to look like.
        if key not in paragraphs:
            problems.append(
                f"{where}: cites {key}, which is not in the index "
                f"(out of scope, or a wrong appendix)"
            )
            continue
        needle = normalise(quote)
        if not needle:
            # "(TM)" or whitespace alone normalises to nothing, and "" is a substring
            # of every paragraph, so this would otherwise verify against anything.
            problems.append(f"{where}: quote is empty once normalised")
            continue
        words = len(needle.split())
        if words < MIN_QUOTE_WORDS:
            problems.append(
                f"{where}: quote is {words} word(s), below the {MIN_QUOTE_WORDS}-word "
                f"floor -- a fragment matches in too many places to locate anything"
            )
            continue
        if needle in paragraphs[key]:
            continue
        elsewhere = sorted(k for k, text in paragraphs.items() if needle in text)
        if elsewhere:
            problems.append(
                f"{where}: quote cites {key} but appears in {', '.join(elsewhere)}"
            )
        else:
            problems.append(
                f"{where}: quote does not appear in {key} or anywhere in scope"
            )
    return problems


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("data/oecd_tg/tg442d-paragraphs.json"),
        help="The committed paragraph index.",
    )
    parser.add_argument(
        "--records",
        type=Path,
        help="Extracted method records to check. Omit to report on the index alone.",
    )
    args = parser.parse_args()

    index = json.loads(args.index.read_text())
    count = len(index["paragraphs"])

    if args.records is None:
        print(f"{args.index}: {count} paragraphs, no records to check")
        return

    payload = json.loads(args.records.read_text())
    records = payload["methods"] if isinstance(payload, dict) else payload
    problems = check(index, records)
    quotes = len(iter_quotes(records))

    if problems:
        print(f"{len(problems)} problem(s) across {quotes} quoted fact(s):")
        for problem in problems:
            print(f"  {problem}")
        sys.exit(1)
    print(f"{quotes} quoted fact(s) verified against {count} paragraphs")


if __name__ == "__main__":
    main()
