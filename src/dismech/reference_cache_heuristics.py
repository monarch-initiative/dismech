"""Heuristic detection of fabricated/hallucinated reference cache metadata.

Background
----------
Issue #871: An AI-generated reference cache for PMID:36919950 contained entirely
fabricated metadata that passed snippet validation because the snippet was
written to match the fake cache. The author list was a classic LLM
placeholder pattern: ``Smith AB, Johnson CD, Williams EF, Brown GH, Davis IJ,
Miller KL`` -- six common English surnames where each is followed by a unique
two-letter initial pair and the initials together progress through the
alphabet (AB, CD, EF, GH, IJ, KL). The surnames themselves are *not* in
alphabetical order; that is a separate LLM placeholder shape called out in
the issue body and detected by ``detect_alphabetical_common_surnames``.

This module implements lightweight heuristics that flag such patterns. It is
intentionally conservative: real PubMed entries occasionally contain a few
common English surnames, so we require multiple corroborating signals before
flagging. Heuristics are a *defence in depth* layer; they are not a substitute
for fetching the canonical metadata from PubMed.

Usage
-----
As a library::

    from dismech.reference_cache_heuristics import scan_cache_dir
    findings = scan_cache_dir(Path("references_cache"))

As a CLI::

    uv run python -m dismech.reference_cache_heuristics references_cache
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml

# Top common English surnames (US Census top ~30 + a few additions). Kept small
# and high-confidence so that genuine papers with one or two common surnames
# don't trip the alphabetical-sequence signal.
COMMON_ENGLISH_SURNAMES: frozenset[str] = frozenset(
    {
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Garcia",
        "Miller",
        "Davis",
        "Rodriguez",
        "Martinez",
        "Hernandez",
        "Lopez",
        "Gonzalez",
        "Wilson",
        "Anderson",
        "Thomas",
        "Taylor",
        "Moore",
        "Jackson",
        "Martin",
        "Lee",
        "Perez",
        "Thompson",
        "White",
        "Harris",
        "Sanchez",
        "Clark",
        "Ramirez",
        "Lewis",
        "Robinson",
        "Walker",
        "Young",
        "Allen",
        "King",
        "Wright",
        "Scott",
        "Torres",
        "Nguyen",
        "Hill",
        "Flores",
        "Green",
        "Adams",
        "Nelson",
        "Baker",
        "Hall",
        "Rivera",
        "Campbell",
        "Mitchell",
        "Carter",
        "Roberts",
    }
)

# Vancouver-style PubMed author: "LastName Initials" e.g. "Smith AB", "Möhring C".
# We allow the surname to contain unicode letters, hyphens, apostrophes, and
# spaces (e.g. "van der Berg J").
_AUTHOR_RE = re.compile(r"^(?P<surname>[^\d]+?)\s+(?P<initials>[A-Z]{1,4})$")


@dataclass(frozen=True)
class Finding:
    """A single suspicious cache file."""

    path: Path
    reference_id: str
    reasons: tuple[str, ...]
    authors: tuple[str, ...]

    def format(self) -> str:
        bullet = "\n  - "
        return (
            f"{self.path}  ({self.reference_id})\n"
            f"  reasons:{bullet}{bullet.join(self.reasons)}\n"
            f"  authors: {', '.join(self.authors)}"
        )


def _parse_author(author: str) -> tuple[str, str] | None:
    """Split a Vancouver-style author into ``(surname, initials)``.

    Returns ``None`` for shapes we don't recognise (full first names, ORCIDs,
    consortium credits, etc.) -- those are *not* the LLM placeholder shape we
    are looking for, so they should not contribute to a false flag.
    """
    match = _AUTHOR_RE.match(author.strip())
    if not match:
        return None
    return match.group("surname").strip(), match.group("initials")


def detect_alphabetical_common_surnames(authors: Iterable[str]) -> str | None:
    """Flag when ≥3 authors all use common English surnames in alphabetical order.

    Real papers occasionally have one or two such authors; an entire author
    list of nothing but alphabetised top-50 English surnames is exceptionally
    unlikely outside of LLM placeholder text.
    """
    parsed = [_parse_author(a) for a in authors]
    surnames = [p[0] for p in parsed if p is not None]
    if len(surnames) < 3:
        return None
    if not all(s in COMMON_ENGLISH_SURNAMES for s in surnames):
        return None
    if surnames != sorted(surnames):
        return None
    return (
        f"all {len(surnames)} authors have common English surnames in "
        f"alphabetical order ({', '.join(surnames)})"
    )


def detect_sequential_initials(authors: Iterable[str]) -> str | None:
    """Flag when authors' initials form an alphabetical sequence with no repeats.

    The reference incident's author list was ``Smith AB, Johnson CD, Williams
    EF, Brown GH, Davis IJ, Miller KL``: every initial letter is unique and
    they progress alphabetically. A real paper would contain duplicates and
    out-of-order initials almost immediately.
    """
    parsed = [_parse_author(a) for a in authors]
    if len(parsed) < 3 or any(p is None for p in parsed):
        return None
    # After the guard above every element is a (surname, initials) tuple.
    initials_strings = [p[1] for p in parsed if p is not None]
    # Multi-letter initials only -- real papers use single-letter initials
    # constantly, so requiring ≥2 letters per author makes this signal much
    # more specific.
    if not all(len(i) >= 2 for i in initials_strings):
        return None
    letters = [c for s in initials_strings for c in s]
    if len(set(letters)) != len(letters):
        return None
    if letters != sorted(letters):
        return None
    return (
        f"all {len(parsed)} authors have unique initials forming an "
        f"alphabetical sequence ({' '.join(initials_strings)})"
    )


# All registered detectors. Adding a new heuristic = adding it here.
DETECTORS = (
    detect_alphabetical_common_surnames,
    detect_sequential_initials,
)


def check_authors(authors: Iterable[str]) -> list[str]:
    """Run every detector against an author list and return the reasons that fired."""
    author_list = list(authors)
    return [
        reason
        for detector in DETECTORS
        if (reason := detector(author_list)) is not None
    ]


class _TolerantLoader(yaml.SafeLoader):
    """SafeLoader that ignores unknown tags (e.g. legacy ``!!python/object/new``).

    A tiny number of historic cache files were written by an older code path
    that pickled ``Bio.Entrez.Parser.StringElement`` objects into the YAML
    frontmatter. We only need plain string fields like ``authors``, so we map
    every unknown tag to its underlying scalar/sequence/mapping value.
    """


def _ignore_unknown_tag(loader, tag_suffix, node):  # type: ignore[no-untyped-def]
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node, deep=True)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node, deep=True)
    return None


# Narrow prefixes: only intercept python-object-style tags. SafeLoader's
# built-in constructors for ``tag:yaml.org,2002:int`` etc. must continue to
# fire so that typed scalars (years, booleans) round-trip correctly.
_TolerantLoader.add_multi_constructor("!python/", _ignore_unknown_tag)
_TolerantLoader.add_multi_constructor("tag:yaml.org,2002:python/", _ignore_unknown_tag)


def _extract_frontmatter_text(path: Path) -> str | None:
    """Return the YAML frontmatter slice of a markdown file, or ``None``."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return text[3:end]


def check_cache_file(path: Path) -> Finding | None:
    """Check a single reference cache file for suspicious metadata.

    Returns a ``Finding`` if the file is structurally broken (malformed YAML
    frontmatter) or if its author list trips any heuristic. Returns ``None``
    for files that parse cleanly and pass every check.
    """
    frontmatter = _extract_frontmatter_text(path)
    if frontmatter is None:
        return None
    try:
        data = yaml.load(frontmatter, Loader=_TolerantLoader)  # noqa: S506
    except yaml.YAMLError as exc:
        # A future cache file with malformed YAML should surface as a finding,
        # not crash the whole sweep. Reporting it lets curators regenerate it
        # via ``just fetch-reference``.
        return Finding(
            path=path,
            reference_id=path.stem,
            reasons=(f"malformed YAML frontmatter: {exc.__class__.__name__}",),
            authors=(),
        )
    if not isinstance(data, dict):
        return None
    raw_authors = data.get("authors") or []
    if not isinstance(raw_authors, list):
        return None
    authors = tuple(str(a) for a in raw_authors)
    reasons = check_authors(authors)
    if not reasons:
        return None
    return Finding(
        path=path,
        reference_id=str(data.get("reference_id", path.stem)),
        reasons=tuple(reasons),
        authors=authors,
    )


def scan_cache_dir(cache_dir: Path) -> list[Finding]:
    """Scan a directory of reference cache markdown files."""
    findings: list[Finding] = []
    for path in sorted(cache_dir.glob("*.md")):
        finding = check_cache_file(path)
        if finding is not None:
            findings.append(finding)
    return findings


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    cache_dir = Path(args[0]) if args else Path("references_cache")
    if not cache_dir.is_dir():
        print(f"error: {cache_dir} is not a directory", file=sys.stderr)
        return 2
    findings = scan_cache_dir(cache_dir)
    if not findings:
        print(f"OK: no suspicious reference caches found in {cache_dir}")
        return 0
    print(
        f"FAIL: {len(findings)} suspicious reference cache(s) in {cache_dir}",
        file=sys.stderr,
    )
    for finding in findings:
        print(finding.format(), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
