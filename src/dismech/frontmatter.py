"""Delimiter-aware YAML frontmatter splitting for markdown files.

Issue #7697. Several readers in this repository — and the pinned
``linkml-reference-validator`` — split markdown frontmatter with
``text.split("---", 2)``. That split is delimiter-*unaware*: it looks for the
substring ``---`` anywhere, so a ``---`` occurring inside a frontmatter *value*
terminates the block early.

This is not hypothetical. ``---`` reaches us verbatim from the source records:

- MMWR's ``Disease---Location, Year`` title convention, e.g. PMID:20881935
  ``title: "Human rabies---Virginia, 2009."``
- Pre-1996 NLM ASCII renderings of arrows and superscripts in the classic
  molecular-genetics literature this project cites for mechanism, e.g.
  PMID:1899320 ``title: Rapid detection of the A----G(8344) mutation of mtDNA.``
  and the ``5'----3'`` / ``X---->Y`` forms.

The failure has two modes, decided only by whether the emitter happened to quote
the title:

- **quoted** (``title: "Human rabies---Virginia, 2009."``) — the naive split cuts
  inside the quoted scalar, leaving it unterminated, and the YAML parser raises.
  For the reference validator this is an unhandled ``ScannerError`` that kills
  the whole run rather than reporting one bad file.
- **unquoted** (``title: Rapid detection of the A----G(8344) …``) — the truncated
  text is *still valid YAML*, so it parses silently. The title is cut mid-word
  and every field after it (``authors``, ``journal``, ``year``, ``keywords``,
  ``content_type``) is discarded into the body. Nothing errors; the reader just
  gets less than it asked for.

The second mode is the dangerous one, and because the cache emitter's quoting is
known to be unstable (#7393, #7523) a silently-degraded file is one dependency
bump away from becoming a crashing one.

``split_frontmatter`` matches the ``---`` delimiter only when it stands alone on
its own line, which is what the YAML frontmatter convention actually means.
Prefer it over any hand-rolled split.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

__all__ = [
    "FRONTMATTER_RE",
    "SplitDocument",
    "contains_frontmatter_delimiter",
    "naive_frontmatter_text",
    "split_frontmatter",
]

# A leading ``---`` line, the frontmatter, then a closing ``---`` line. Both
# delimiters must own their line (trailing spaces/tabs and CRLF tolerated); the
# closing one may end the file without a trailing newline.
#
# The frontmatter and the newline ending it are optional *as a unit*, so an empty
# block (``---\n---\n``) matches. Note they have to be optional together: making
# only the newline optional would let the closing delimiter match a ``---`` that
# merely *ends* a value line, reintroducing exactly the bug this module exists to
# fix (``title: a---\nmore: b\n---``).
FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?:(?P<frontmatter>.*?)(?:\r?\n))?---[ \t]*(?:\r?\n|\Z)",
    re.DOTALL,
)


@dataclass(frozen=True)
class SplitDocument:
    """A markdown file separated into its frontmatter and body."""

    frontmatter: str
    body: str


def split_frontmatter(text: str) -> SplitDocument | None:
    """Split leading YAML frontmatter from a markdown body.

    Returns ``None`` when the text has no well-formed frontmatter block, which
    callers should treat the same way they treat a file that does not start with
    ``---`` at all.

    Unlike ``text.split("---", 2)`` this only accepts a ``---`` that stands alone
    on its own line, so ``---`` inside a value (a title, a keyword) does not end
    the block.
    """
    match = FRONTMATTER_RE.match(text)
    if match is None:
        return None
    return SplitDocument(
        # ``None`` when the block is empty (``---\n---``), which is an empty
        # block rather than a missing one.
        frontmatter=match.group("frontmatter") or "",
        body=text[match.end() :],
    )


def naive_frontmatter_text(text: str) -> str | None:
    """Reproduce the delimiter-unaware ``split("---", 2)`` reading.

    This exists so callers can *detect* the discrepancy — comparing this against
    :func:`split_frontmatter` tells you whether a file reads differently to a
    consumer that still splits naively. Do not use it to actually read a file.
    """
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def contains_frontmatter_delimiter(value: object) -> bool:
    """True when a value would serialize with a literal ``---`` inside it.

    Used to decide which frontmatter entries have to be held back from a
    delimiter-unaware consumer and restored afterwards.
    """
    if isinstance(value, str):
        return "---" in value
    if isinstance(value, dict):
        return any(
            contains_frontmatter_delimiter(key) or contains_frontmatter_delimiter(item)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple, set)):
        return any(contains_frontmatter_delimiter(item) for item in value)
    return False
