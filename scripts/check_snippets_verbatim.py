#!/usr/bin/env python3
"""Mechanically verify that every evidence snippet is a verbatim substring of its cached reference.

This is an independent, deliberately dumb cross-check of the anti-hallucination
invariant stated in CLAUDE.md ("snippets MUST be exact quotes"). It does not
call any model, does not fuzzy-match, and does not repair anything — it walks
the YAML, finds every `snippet` that sits next to a `reference`, and asserts the
snippet text appears in `references_cache/<REF>.md`.

Unlike `just validate-references`, this reports a per-file PASS/FAIL and an
explicit count of what it checked, so an empty result can never be mistaken for
a clean one.

Usage:
    uv run python scripts/check_snippets_verbatim.py kb/disorders/Foo.yaml [...]
    uv run python scripts/check_snippets_verbatim.py --all

Exit code is non-zero if any snippet fails to verify.
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
import unicodedata
from pathlib import Path

import yaml

CACHE_DIR = Path("references_cache")

# References whose bodies are not fetched abstracts. Snippets against these are
# reported separately rather than counted as failures.
SKIP_PREFIXES = ("clinicaltrials:", "NCT")


def cache_path_for(ref: str) -> Path | None:
    """Map a reference CURIE to its cache file, mirroring the validator's naming."""
    stem = ref.replace(":", "_").replace("/", "_")
    candidate = CACHE_DIR / f"{stem}.md"
    if candidate.exists():
        return candidate
    # Fall back to a case-insensitive scan; the cache has both PMID_ and pmid_ historically.
    matches = [p for p in CACHE_DIR.glob("*.md") if p.stem.lower() == stem.lower()]
    return matches[0] if matches else None


def normalize(text: str) -> str:
    """Collapse the differences that are typographic rather than substantive.

    Unicode dashes/quotes and line-wrapping whitespace differ routinely between a
    YAML block scalar and the cached abstract without the quote being any less
    verbatim. Anything beyond that is a real mismatch.
    """
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("‐", "-").replace("‑", "-").replace("‒", "-")
    text = text.replace("–", "-").replace("—", "-").replace("−", "-")
    text = text.replace("‘", "'").replace("’", "'").replace("ʼ", "'")
    text = text.replace("“", '"').replace("”", '"')
    # Lancet/BMJ house style uses a middle dot as the decimal separator ("61·4%").
    # Only convert when it sits between digits, so it never mangles real prose.
    text = re.sub(r"(?<=\d)[·•](?=\d)", ".", text)
    # Greek letters routinely survive as ASCII transliterations in one text and as
    # the real codepoint in the other ("μg/dL" vs "mug/dL", "α" vs "alpha").
    for ch, ascii_ in (("μ", "mu"), ("µ", "mu"), ("α", "alpha"), ("β", "beta"), ("γ", "gamma"), ("κ", "kappa")):
        text = text.replace(ch, ascii_)
    text = text.replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip().lower()


def deartifact(text: str) -> str:
    """Strip PDF-extraction artifacts that are not the curator's doing.

    Many cache bodies are extracted from PDFs (GeneReviews chapters, guideline
    papers) rather than clean PubMed abstracts. Two artifacts routinely break a
    byte-exact match on a snippet that is, in substance, an accurate quote:

      * inline numeric citation markers   "...lymphopenia (TCL) [13]. Stud-"
      * hyphenation across a line break   "Stud- ies"  ->  "Studies"

    Stripping these is NOT fuzzy matching: what remains is still an exact-substring
    test, so a paraphrase or an invented sentence still fails. What it buys is that
    a reported FAIL is worth a human's attention instead of being extraction noise.
    """
    text = re.sub(r"\s*\[\d+(?:\s*[,\-]\s*\d+)*\]", "", text)  # [13], [4,5], [7-9]
    text = re.sub(r"(\w)-\s+(\w)", r"\1\2", text)  # de-hyphenate across line breaks
    return text


def contains(snippet: str, body: str) -> bool:
    """Exact-substring test, tolerant of two conventional quoting moves.

    Both are things a careful human curator does and neither weakens the quote:

    * **Elision.** ``"A... B"`` means A and B were quoted from the same source with
      material dropped between them. Each segment must still appear exactly, and
      must appear *in order* — so an elision cannot be used to smuggle in text that
      isn't there, or to reverse the source's meaning by reordering.
    * **Early truncation.** Ending a quote mid-sentence and closing it with a period
      where the source continues with a comma or semicolon.

    Everything else is still a byte-exact comparison. A paraphrase fails.
    """
    segments = [s.strip() for s in re.split(r"\.{3,}|…", snippet) if s.strip()]

    pos = 0
    for i, seg in enumerate(segments):
        idx = body.find(seg, pos)
        if idx < 0:
            # Last segment may have been truncated early and closed with a period.
            if i == len(segments) - 1 and seg.endswith("."):
                idx = body.find(seg[:-1].rstrip(), pos)
            if idx < 0:
                return False
        pos = idx + len(seg)
    return True


def diagnose(snippet: str, body: str) -> str:
    """Explain *where* a snippet stops matching, not just that it does.

    Reporting a truncated snippet is useless for triage — it hides whether the
    quote is wholly absent (likely fabricated / wrong paper) or diverges at one
    token (a typographic or transcription slip). Binary-search the longest
    matching prefix and show the two texts at the divergence point.
    """
    if not snippet:
        return "empty snippet"
    if snippet[:40] not in body:
        return f"text absent from this reference entirely: {snippet[:120]!r}"

    lo, hi = 40, len(snippet)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if snippet[:mid] in body:
            lo = mid
        else:
            hi = mid - 1

    idx = body.find(snippet[:lo])
    return (
        f"diverges after {lo}/{len(snippet)} chars | "
        f"SNIPPET ...{snippet[max(0, lo - 30):lo + 40]!r} | "
        f"CACHE ...{body[max(0, idx + lo - 30):idx + lo + 40]!r}"
    )


def walk(node, ref_ctx=None):
    """Yield (reference, snippet) pairs from anywhere in the document tree."""
    if isinstance(node, dict):
        ref = node.get("reference", ref_ctx)
        snippet = node.get("snippet")
        if snippet and ref:
            yield str(ref), str(snippet)
        for value in node.values():
            yield from walk(value, ref)
    elif isinstance(node, list):
        for item in node:
            yield from walk(item, ref_ctx)


def check_file(path: Path) -> tuple[int, list[str], list[str]]:
    """Return (verified_count, failures, skipped)."""
    data = yaml.safe_load(path.read_text())
    verified = 0
    failures: list[str] = []
    skipped: list[str] = []

    bodies: dict[str, str] = {}
    for ref, snippet in walk(data):
        if ref.startswith(SKIP_PREFIXES):
            skipped.append(f"{ref} (non-abstract source)")
            continue

        if ref not in bodies:
            cache = cache_path_for(ref)
            if cache is None:
                failures.append(f"NO CACHE FILE for {ref} — snippet: {snippet[:90]!r}")
                bodies[ref] = ""
                continue
            bodies[ref] = deartifact(normalize(cache.read_text()))

        body = bodies[ref]
        if not body:
            continue
        norm_snippet = deartifact(normalize(snippet))
        if contains(norm_snippet, body):
            verified += 1
        else:
            failures.append(f"NOT VERBATIM in {ref}: {diagnose(norm_snippet, body)}")

    return verified, failures, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", help="disorder YAML files to check")
    parser.add_argument("--all", action="store_true", help="check every kb/disorders/*.yaml")
    args = parser.parse_args()

    targets = [Path(p) for p in args.files]
    if args.all:
        targets = sorted(Path(p) for p in glob.glob("kb/disorders/*.yaml"))
    if not targets:
        parser.error("pass one or more files, or --all")

    total_verified = 0
    total_failed = 0
    for path in targets:
        verified, failures, skipped = check_file(path)
        total_verified += verified
        total_failed += len(failures)
        status = "FAIL" if failures else "PASS"
        note = f", {len(skipped)} skipped" if skipped else ""
        print(f"[{status}] {path}: {verified} snippets verified verbatim{note}")
        for f in failures:
            print(f"         {f}")

    print(f"\nTotal: {total_verified} verified, {total_failed} failed across {len(targets)} file(s)")
    return 1 if total_failed else 0


if __name__ == "__main__":
    sys.exit(main())
