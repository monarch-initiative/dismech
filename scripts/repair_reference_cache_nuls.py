#!/usr/bin/env python3
"""Replace NUL bytes in ``references_cache/*.md`` with the text they stand for.

Why the NULs are there
----------------------
The reference fetcher extracts PDF text with ``pypdf`` (inside
linkml-reference-validator). When a PDF font has no ToUnicode entry for a glyph,
the glyph comes out as U+0000. Usually that glyph is a ligature -- ``in\\0ammation``
is "inflammation", ``signi\\0cant`` is "significant" -- but in some PDFs the same
unmapped glyph is a digit (``1\\0. Zaidi SH``, a reference number) or a minus sign
(``1 \\0 P``). One NUL therefore does not have one meaning, even within one file.

A NUL also makes ``grep`` classify the whole file as binary and drop it from its
output, so every grep-based count over ``references_cache/`` silently skipped
these files (#12543).

What this does
--------------
For each NUL run that sits inside a word, try each ligature expansion
(``fi``, ``fl``, ``ff``, ``ffi``, ``ffl``). Use an expansion when the word it
produces occurs elsewhere in the cache corpus at least ``DOMINANCE`` (10) times as
often as the word any other expansion produces. For words the PDF ran together
("withsigni\\0cant"), fall back to the letters on each side of the NUL, which must
be well attested inside some ordinary word; this needs at least two letters on
each side. Anything else -- a NUL between digits, a standalone NUL, a lost
separator, or a word no expansion clearly explains -- becomes U+FFFD REPLACEMENT
CHARACTER, which says "a character was lost here" without guessing which one.

This is a deterministic transform of the existing cache, not a re-fetch: a
re-fetch would run the same extractor and write the same NULs back. Snippet
matching normalizes every non-word character to a space, so a NUL and U+FFFD are
equivalent to the validator, and a ligature restored to letters can only make a
quote that spans it match where it previously could not.

Usage
-----
    python scripts/repair_reference_cache_nuls.py            # report only
    python scripts/repair_reference_cache_nuls.py --apply    # rewrite the files
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "references_cache"

NUL = "\x00"
REPLACEMENT = "�"
LIGATURES = ("fi", "fl", "ff", "ffi", "ffl")

# A word with NUL runs inside it: letters, then one or more (NUL-run + letters)
# segments. Hyphens and digits end the word, so a NUL between digits is never
# offered a ligature.
_WORD_WITH_NUL = re.compile(r"[A-Za-z]*(?:\x00+[A-Za-z]*)+")
_WORD = re.compile(r"[a-z]+")
# Minimum corpus occurrences for an expansion to count as an attested word.
MIN_ATTESTATIONS = 2
# The winning expansion must be this many times more frequent than the runner-up.
# "Exactly one attested reading" is too strict: the corpus is itself PDF-extracted,
# so OCR junk such as "infiammatory" is attested too, a few times against
# "inflammatory"'s tens of thousands.
DOMINANCE = 10
# Letters needed around a NUL before any reading is offered. With one letter,
# "\0n diameter" (a lost "i") would be read as "fin".
MIN_WORD_LETTERS = 2
# Letters needed on the two sides of one NUL for the substring fallback, which
# handles words the PDF ran together ("withsigni\0cant"). Each side also needs
# two letters of its own: in "Smoking history\0n (%)" the NUL is a lost column
# separator, and "tory" + "fi" + "n" is otherwise a plausible window.
MIN_WINDOW_LETTERS = 4
WINDOW = 4


def build_vocabulary(paths: list[Path]) -> Counter[str]:
    """Count lowercase alphabetic tokens across the cache, NUL-split."""
    vocab: Counter[str] = Counter()
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace").lower()
        vocab.update(_WORD.findall(text))
    return vocab


def _dominant(scores: dict[str, int]) -> str | None:
    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    best, best_count = ranked[0]
    runner_up = ranked[1][1] if len(ranked) > 1 else 0
    if best_count >= MIN_ATTESTATIONS and best_count >= DOMINANCE * runner_up:
        return best
    return None


class _WindowScorer:
    """Corpus frequency of a short letter window, as a substring of any word."""

    def __init__(self, vocab: Counter[str]):
        self._words = [(word, count) for word, count in vocab.items() if "f" in word]
        self._memo: dict[str, int] = {}

    def __call__(self, window: str) -> int:
        if window not in self._memo:
            self._memo[window] = sum(c for w, c in self._words if window in w)
        return self._memo[window]


def _resolve_word(word: str, vocab: Counter[str], scorer: _WindowScorer) -> str | None:
    """Return ``word`` with its NULs expanded, or None if no reading is clear."""
    parts = re.split(r"\x00+", word)
    runs = re.findall(r"\x00+", word)
    if any(len(run) != 1 for run in runs):
        return None
    if sum(len(part) for part in parts) < MIN_WORD_LETTERS:
        return None

    # Whole word first. Every NUL takes the same expansion: one unmapped glyph
    # per word is the overwhelming case.
    whole = {lig: vocab[lig.join(parts).lower()] for lig in LIGATURES}
    choice = _dominant(whole)
    if choice is not None:
        return choice.join(parts)

    # Fallback for run-together words: decide each NUL from the letters next to
    # it, which must be well attested inside some ordinary word.
    out = [parts[0]]
    for left, right in pairwise(parts):
        left_w, right_w = left[-WINDOW:].lower(), right[:WINDOW].lower()
        if len(left_w) + len(right_w) < MIN_WINDOW_LETTERS or min(len(left_w), len(right_w)) < 2:
            return None
        choice = _dominant({lig: scorer(left_w + lig + right_w) for lig in LIGATURES})
        if choice is None:
            return None
        out += [choice, right]
    return "".join(out)


def repair_text(
    text: str, vocab: Counter[str], scorer: _WindowScorer | None = None
) -> tuple[str, int, int]:
    """Return (repaired text, ligatures restored, replacement characters used)."""
    scorer = scorer or _WindowScorer(vocab)
    restored = 0

    def _sub(match: re.Match[str]) -> str:
        nonlocal restored
        word = match.group(0)
        resolved = _resolve_word(word, vocab, scorer)
        if resolved is None:
            return word  # left for the blanket replacement below
        restored += word.count(NUL)
        return resolved

    text = _WORD_WITH_NUL.sub(_sub, text)
    replaced = text.count(NUL)
    return text.replace(NUL, REPLACEMENT), restored, replaced


def files_with_nul(cache_dir: Path = CACHE_DIR) -> list[Path]:
    return sorted(p for p in cache_dir.glob("*.md") if b"\x00" in p.read_bytes())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--apply", action="store_true", help="rewrite the affected files")
    args = parser.parse_args(argv)

    targets = files_with_nul()
    if not targets:
        print("OK: no NUL bytes under references_cache/.")
        return 0

    vocab = build_vocabulary(sorted(CACHE_DIR.glob("*.md")))
    scorer = _WindowScorer(vocab)
    total_restored = total_replaced = 0
    for path in targets:
        text = path.read_bytes().decode("utf-8")
        repaired, restored, replaced = repair_text(text, vocab, scorer)
        total_restored += restored
        total_replaced += replaced
        print(f"{path.relative_to(ROOT)}: {restored} ligature(s) restored, {replaced} replaced with U+FFFD")
        if args.apply:
            path.write_bytes(repaired.encode("utf-8"))

    verb = "Repaired" if args.apply else "Would repair"
    print(
        f"\n{verb} {len(targets)} file(s): {total_restored} NUL(s) restored as "
        f"ligatures, {total_replaced} replaced with U+FFFD."
    )
    if not args.apply:
        print("Re-run with --apply to rewrite them.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
