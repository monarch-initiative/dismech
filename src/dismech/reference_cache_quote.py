"""Idempotent YAML-quoting normalization for reference-cache frontmatter.

``just fix-references-cache`` runs this as a whole-cache sweep (tens of thousands
of files) before most reference-validation recipes, so it MUST be a no-op on a
well-formed cache. If it rewrites files that do not need it, every validation run
fills the working tree with quoting-only churn a curator then has to notice and
avoid staging. That is exactly what happened before issue-level fix in PR #8203:
the old predicate quoted any value containing a colon, so it re-quoted every
``reference_id: PREFIX:LOCALID`` line (and the handful of ``doi:`` values with an
embedded colon) on every run — ~9.9k of ~35.6k files — without ever fixing a real
problem, because the reference fetcher deliberately writes those two fields as
valid unquoted plain scalars.

:func:`needs_quoting` therefore quotes a value only when YAML genuinely requires
it. Critically, an embedded colon forces quoting ONLY when it is followed by
whitespace or ends the value (the ``key: value`` mapping ambiguity); a bare
``PMID:11390973`` / ``10.1023/a:1022935115323`` colon is a legal plain scalar and
is left alone. The ``[ { * & ! @ #`` indicator characters force quoting only when
they are the *leading* character — YAML excludes them from ``ns-plain-first`` but
permits them mid-scalar in block context.

The committed cache is intentionally left in a *mixed* state: values quoted by
past sweeps stay quoted (:func:`needs_quoting` short-circuits on an already-quoted
value), and the fetcher's native unquoted form stays unquoted. Both parse
identically; normalizing either way would mean a 10k–26k-file diff, which is the
churn this module exists to avoid. Do NOT "clean up" that split, and do NOT
restore the naive ``c in value`` colon test.

This deliberately keeps the historical ``str.split("---", 2)`` reconstruction so
its output is byte-for-byte what the recipe produced; the no-op property is what
protects the rare ``---``-in-title records (issue #7697) from that naive split,
since a file that needs no rewrite is never reconstructed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

__all__ = [
    "files_needing_requote",
    "main",
    "needs_quoting",
    "normalize_reference_cache",
    "requote_frontmatter",
]

# YAML indicator characters that force quoting when they are the first character
# of a plain scalar. Only ``-`` gets the "indicates only before whitespace"
# special-case below (``-5`` is a legal plain scalar, ``- x`` is a block-sequence
# item). ``?`` and ``:`` are kept in this set and so are quoted unconditionally
# when leading: in YAML 1.2 a leading ``?``/``:`` not followed by whitespace is
# actually legal plain-scalar content, so quoting it is never *wrong*, merely
# unnecessary -- a deliberately conservative choice, since no cache value begins
# with one and the churn-relevant fields (reference_id/doi) never do.
_LEADING_INDICATORS = frozenset("!&*[]{}#,>|%@`\"'?:")

_FRONTMATTER_KEY_RE = re.compile(r"^(\s*)([a-z_]+):\s+(.+)$", re.IGNORECASE)


def needs_quoting(value: str) -> bool:
    """Return True when ``value`` cannot be written as a bare YAML plain scalar.

    Examples:
        >>> needs_quoting("PMID:11390973")          # colon not before whitespace
        False
        >>> needs_quoting("10.1023/a:1022935115323")
        False
        >>> needs_quoting("Structural basis of X.")
        False
        >>> needs_quoting("Title: a subtitle")      # ": " mapping ambiguity
        True
        >>> needs_quoting("ends with colon:")
        True
        >>> needs_quoting("[Cholera].")             # leading flow indicator
        True
        >>> needs_quoting("- dashspace")            # block-sequence marker
        True
        >>> needs_quoting("word #comment")          # inline comment start
        True
        >>> needs_quoting("-5 degrees")             # '-' not before whitespace
        False
    """
    if not value:
        return False
    if value != value.strip():  # leading/trailing whitespace
        return True
    if value[0] in _LEADING_INDICATORS:  # value starts with an indicator
        return True
    if value[0] == "-" and (len(value) == 1 or value[1] == " "):
        return True  # "- " block-sequence indicator
    if ": " in value or value.endswith(":"):
        return True  # colon that YAML reads as a mapping
    return " #" in value  # start of an inline comment


def requote_frontmatter(frontmatter: str) -> tuple[str, bool]:
    """Return ``(new_frontmatter, modified)`` after quoting values that need it."""
    new_lines: list[str] = []
    modified = False
    for line in frontmatter.split("\n"):
        if not line.strip() or line.strip().startswith("-"):
            new_lines.append(line)
            continue
        match = _FRONTMATTER_KEY_RE.match(line)
        if match:
            indent, key, value = match.groups()
            is_quoted = value.startswith(('"', "'"))
            if needs_quoting(value) and not is_quoted:
                escaped = value.replace('"', '\\"')
                new_lines.append(f'{indent}{key}: "{escaped}"')
                modified = True
                continue
        new_lines.append(line)
    return "\n".join(new_lines), modified


def _iter_cache_files(cache_dir: Path):
    for md_file in sorted(cache_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            continue
        parts = content.split("---", 2)
        if len(parts) < 3:
            continue
        yield md_file, parts[1], parts[2]


def files_needing_requote(cache_dir: str | Path) -> list[str]:
    """Read-only: names of cache files the sweep would rewrite (no writes)."""
    cache_dir = Path(cache_dir)
    if not cache_dir.exists():
        return []
    return [
        md_file.name
        for md_file, frontmatter, _body in _iter_cache_files(cache_dir)
        if requote_frontmatter(frontmatter)[1]
    ]


def normalize_reference_cache(cache_dir: str | Path) -> list[str]:
    """Quote frontmatter values that need it; return the names of rewritten files."""
    cache_dir = Path(cache_dir)
    rewritten: list[str] = []
    if not cache_dir.exists():
        return rewritten
    for md_file, frontmatter, body in _iter_cache_files(cache_dir):
        new_frontmatter, modified = requote_frontmatter(frontmatter)
        if modified:
            md_file.write_text(f"---{new_frontmatter}---{body}", encoding="utf-8")
            rewritten.append(md_file.name)
    return rewritten


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    cache_dir = Path(args[0]) if args else Path("references_cache")
    rewritten = normalize_reference_cache(cache_dir)
    if rewritten:
        print(f"fix-references-cache: re-quoted {len(rewritten)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
