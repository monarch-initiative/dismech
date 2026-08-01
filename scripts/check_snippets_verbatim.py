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

# Reference prefixes whose bodies are not fetched prose abstracts — dataset
# accessions, trial registrations and bare URLs. Snippets against these are
# reported as skipped rather than counted as failures, mirroring the intent of
# skip_prefixes in conf/reference_validator_config.yaml. Note DOI is
# deliberately ABSENT here: DOI is a literature identifier and checking it is
# the whole point of this script (see #7514).
SKIP_PREFIXES = (
    "clinicaltrials:", "NCT",
    "url:", "http:", "https:",
    "GEO:", "geo:", "SRA:", "sra:", "BIOPROJECT:", "bioproject:",
    "dbGaP:", "dbgap:", "DBGAP:", "GTEX:", "gtex:",
    "metabolights:", "METABOLIGHTS:", "MTBLS",
    "mgnify:", "MGNIFY:", "MGYS",
    "morphic:", "MORPHIC:", "cellxgene:", "CELLXGENE:",
    "pride:", "PRIDE:", "massive:", "MASSIVE:",
    "proteomexchange:", "osdr:", "OSDR:", "nasa_osdr:", "genelab:", "GENELAB:",
)


def cache_path_for(ref: str) -> Path | None:
    """Map a reference CURIE to its cache file, mirroring the validator's naming."""
    stem = ref.replace(":", "_").replace("/", "_")
    candidate = CACHE_DIR / f"{stem}.md"
    if candidate.exists():
        return candidate
    # Fall back to a case-insensitive scan; the cache has both PMID_ and pmid_ historically.
    matches = [p for p in CACHE_DIR.glob("*.md") if p.stem.lower() == stem.lower()]
    return matches[0] if matches else None


def strip_frontmatter(text: str) -> str:
    """Reduce a cache file to its quotable body before searching it.

    Two headers have to go, not one. Dropping only the ``---`` YAML block is
    insufficient: 29,656 of 32,969 cache files then *restate* the title, authors
    and journal as markdown before a ``## Content`` marker, so a snippet echoing
    the paper's title still "verifies" — the opposite of what this tool is for.
    Seven live KB snippets did exactly that.

    So: drop the YAML block, then advance past ``## Content`` when present.
    Structured-source caches (``ORPHA_*``, ``CGGV_*``, ``CGDS_*``) have no such
    marker and their tables ARE the quotable content, so they are left whole.
    """
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    marker = text.find("## Content")
    if marker != -1:
        text = text[marker + len("## Content"):]
    return text


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
    for ch, ascii_ in (
        ("μ", "mu"), ("µ", "mu"), ("α", "alpha"), ("β", "beta"), ("γ", "gamma"),
        ("δ", "delta"), ("κ", "kappa"), ("λ", "lambda"), ("σ", "sigma"), ("ω", "omega"),
    ):
        text = text.replace(ch, ascii_)
    # Other symbols that differ purely by encoding between extracted PDF text and
    # a hand-typed YAML snippet.
    for ch, ascii_ in (
        ("±", "+/-"), ("≤", "<="), ("⩽", "<="), ("≥", ">="), ("⩾", ">="),
        ("×", "x"), ("→", "->"), ("′", "'"), ("″", '"'),
    ):
        text = text.replace(ch, ascii_)
    text = text.replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip().lower()


def deartifact(text: str) -> str:
    """Strip PDF-extraction artifacts that are not the curator's doing.

    Many cache bodies are extracted from PDFs (GeneReviews chapters, guideline
    papers) rather than clean PubMed abstracts. These artifacts routinely break a
    byte-exact match on a snippet that is, in substance, an accurate quote:

      * inline numeric citation markers   "...lymphopenia (TCL) [13]. Stud-"
      * hyphenation across a line break   "Stud- ies"      -> "studies"
      * spaces on BOTH sides of the break "emo - tional"   -> "emotional"
      * a break with no hyphen at all     "con firmed"     -> handled below
      * space before punctuation          "acvr1(r206h) ,"

    The hyphen cases are the dominant residual noise source. Note the deliberate
    asymmetry: a real hyphenated compound ("T-cell") must survive, but the same
    compound broken at a line break ("T-\ncell") must also match a snippet that
    writes it as "T-cell". Both are therefore reduced to the SAME form by removing
    intra-word hyphens entirely once whitespace has been collapsed - so "t-cell",
    "t- cell" and "t - cell" all become "tcell" on both sides of the comparison.

    Stripping these is NOT fuzzy matching: what remains is still an exact-substring
    test, so a paraphrase or an invented sentence still fails. What it buys is that
    a reported FAIL is worth a human's attention instead of being extraction noise.
    """
    text = re.sub(r"\s*\[\d+(?:\s*[,\-]\s*\d+)*\]", "", text)  # [13], [4,5], [7-9]
    # Collapse every intra-word hyphen (with or without surrounding spaces) so that
    # line-broken and unbroken spellings of the same compound converge.
    # NB the digit guards: "1-2 months" is a RANGE, and collapsing it would make a
    # snippet saying "12 months" match — a range quoted as a point value is exactly
    # the kind of misquote this tool exists to catch. Letter-only stripping is too
    # narrow though (it breaks ORPHA list-marker snippets like "- Autosomal
    # recessive"), so the rule is: strip hyphens EXCEPT between two digits.
    text = _collapse_hyphens(text)
    # Drop whitespace sitting before punctuation ("acvr1(r206h) ," -> "acvr1(r206h),").
    text = re.sub(r"\s+([,.;:)\]])", r"\1", text)
    return text


# Sentinel used to shield digit-hyphen-digit while other hyphens are collapsed.
_RANGE = "\x00"


def _collapse_hyphens(text: str) -> str:
    """Collapse intra-word hyphens, but never one sitting between two digits."""
    text = re.sub(r"(?<=\d)\s*-\s*(?=\d)", _RANGE, text)
    text = re.sub(r"(?<=\w)\s*-\s*(?=\w)", "", text)
    return text.replace(_RANGE, "-")


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
    if _contains_strict(snippet, body):
        return True
    # Fallback: a hyphen in the source may be rendered as a space in the quote, or
    # vice versa ("spastic paraplegia-shuffling gait" quoted as "spastic paraplegia
    # shuffling gait"). Hyphen-as-nothing and hyphen-as-space are different
    # normalizations and no single rule satisfies both, so retry with hyphens AND
    # spaces removed from both sides. Still an exact contiguous character match, so
    # a paraphrase, substitution or negation flip continues to fail.
    return _contains_strict(_squash(snippet), _squash(body))


def _squash(text: str) -> str:
    """Strip whitespace and hyphens, but never a hyphen between two digits.

    Same reasoning as deartifact(): squashing "5-10 mg" to "510mg" would let a
    snippet claiming "510 mg" verify against a source that says "5-10 mg".

    The guard must strip a hyphen unless BOTH neighbours are digits. An earlier
    form, ``(?<!\\d)-(?!\\d)``, inverted that — it stripped only when *neither*
    neighbour was a digit, so a quote truncated on a trailing digit-hyphen
    became unmatchable. That inversion was the entire cost of the numeric
    shield across the KB.
    """
    text = re.sub(r"-(?!\d)|(?<!\d)-", "", text)
    return re.sub(r"\s+", "", text)


def _contains_strict(snippet: str, body: str) -> bool:
    segments = [s.strip() for s in re.split(r"\.{3,}|…", snippet) if s.strip()]
    if not segments:
        return False

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

    The "absent entirely" verdict is the fabrication signal, so it must not be
    reachable by a quote that is merely *wrong near its start*. It is therefore
    gated on finding no substantial run of the snippet anywhere in the body — not
    on a fixed-length prefix. An earlier version tested only ``snippet[:40]``,
    which dumped any early divergence into the fabrication bucket and defeated
    the two-class triage this function exists to provide.
    """
    if not snippet:
        return "empty snippet"

    # Longest matching prefix (0 if even the first characters differ).
    lo, hi = 0, len(snippet)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if snippet[:mid] in body:
            lo = mid
        else:
            hi = mid - 1

    # Does any substantial contiguous run of the snippet appear at all? If some
    # window does, the source text is present and this is a divergence, not an
    # absence — regardless of where the mismatch falls.
    # Does any substantial contiguous run of the snippet appear ANYWHERE in the
    # body? Prefix length alone is not enough: a quote can diverge at character 4
    # (the source reads "AMH) levels below detection sensitivity", the quote
    # dropped the paren) while the remaining 35 characters match perfectly. That
    # is a transcription slip, not a fabrication, and must not land in the
    # fabrication bucket. Slide a window sized to the snippet instead.
    window = min(40, max(12, int(0.6 * len(snippet))))
    if len(snippet) >= window:
        anywhere = any(
            snippet[i:i + window] in body
            for i in range(len(snippet) - window + 1)
        )
    else:
        anywhere = snippet in body

    if not anywhere:
        return f"text absent from this reference entirely: {snippet[:120]!r}"

    idx = body.find(snippet[:lo]) if lo else 0
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
        if ref not in bodies:
            cache = cache_path_for(ref)
            bodies[ref] = deartifact(normalize(strip_frontmatter(cache.read_text()))) if cache else None

        body = bodies[ref]
        if body is None:
            # Nothing to check against. For dataset accessions and bare URLs that is
            # expected, so report it as skipped; for a literature reference it is a
            # real gap. Either way the decision is made on whether a cache body
            # EXISTS, not on the prefix — an earlier version skipped by prefix and
            # thereby declined to check 1,525 snippets that did have cache bodies.
            if ref.startswith(SKIP_PREFIXES):
                skipped.append(f"{ref} (no cache body; non-literature source)")
            else:
                failures.append(f"NO CACHE FILE for {ref} — snippet: {snippet[:90]!r}")
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
    parser.add_argument(
        "--all", action="store_true",
        help="check every YAML under kb/disorders, kb/modules and kb/comorbidities",
    )
    args = parser.parse_args()

    targets = [Path(p) for p in args.files]
    if args.all:
        # kb/modules and kb/comorbidities carry evidence too (~1,300 snippets) and
        # were missed by an earlier disorders-only glob.
        targets = sorted(
            Path(p)
            for d in ("kb/disorders", "kb/modules", "kb/comorbidities")
            for p in glob.glob(f"{d}/*.yaml")
        )
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
