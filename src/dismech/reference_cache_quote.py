"""Idempotent YAML-quoting normalization for reference-cache frontmatter.

``just fix-references-cache`` normally scopes this operation to the caches cited
by the data files being validated; omitting data-file arguments retains an
explicit whole-cache maintenance mode. Either mode MUST be a no-op on already
well-formed cache records. If it rewrites files that do not need it, validation
fills the working tree with quoting-only churn a curator then has to notice and
avoid staging. That is exactly what happened before the issue-level fixes:
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

Frontmatter replacement uses match offsets into the original text so a literal
``---`` in the body is never mistaken for the closing delimiter. Double-quoted
rewrites escape backslashes before quotes so values such as ``C:\\study`` remain
valid YAML and round-trip unchanged.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

import yaml

from dismech.yaml_io import safe_load_path

__all__ = [
    "files_needing_requote",
    "main",
    "needs_quoting",
    "normalize_reference_cache",
    "requote_frontmatter",
    "resolve_cache_paths",
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
_FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?P<frontmatter>.*?)(?:\r?\n)---[ \t]*(?:\r?\n|\Z)",
    re.DOTALL,
)


def iter_reference_ids(value: Any) -> Iterator[str]:
    """Yield values from slots implementing ``linkml:authoritative_reference``."""
    if isinstance(value, dict):
        for slot_name in ("reference", "accession"):
            reference = value.get(slot_name)
            if isinstance(reference, str) and reference.strip():
                yield reference.strip()
        for child in value.values():
            yield from iter_reference_ids(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_reference_ids(child)


def _safe_cache_stem(reference_id: str) -> str:
    return (
        reference_id.replace(":", "_")
        .replace("/", "_")
        .replace("?", "_")
        .replace("=", "_")
    )


def _cache_index(cache_dir: Path) -> tuple[dict[str, Path], dict[str, Path | None]]:
    by_stem: dict[str, Path] = {}
    by_bare_id: dict[str, Path | None] = {}
    for path in cache_dir.glob("*.md"):
        by_stem.setdefault(path.stem.casefold(), path)
        prefix, separator, tail = path.stem.partition("_")
        if prefix and separator and tail:
            key = tail.casefold()
            by_bare_id[key] = None if key in by_bare_id else path
    return by_stem, by_bare_id


def resolve_cache_paths(cache_dir: Path, data_files: Iterable[Path]) -> list[Path]:
    """Resolve caches cited by data files, leaving input diagnostics to validators."""
    by_stem, by_bare_id = _cache_index(cache_dir)
    resolved: set[Path] = set()
    for data_file in data_files:
        try:
            data = safe_load_path(data_file)
        except (OSError, yaml.YAMLError):
            continue
        for reference_id in iter_reference_ids(data):
            key = _safe_cache_stem(reference_id).casefold()
            path = by_stem.get(key)
            if path is None:
                # Bare identifiers such as NCT06087757 are cached under the
                # source's canonical prefix (clinicaltrials_NCT06087757.md).
                path = by_bare_id.get(key)
            if path is not None:
                resolved.add(path)
    return sorted(resolved)


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
    # Split only on actual YAML line endings. ``str.splitlines`` also treats
    # U+2028/U+2029 in publication titles as separators and would corrupt them.
    for raw_line in frontmatter.split("\n"):
        line = raw_line.removesuffix("\r")
        carriage_return = "\r" if raw_line.endswith("\r") else ""
        if not line.strip() or line.strip().startswith("-"):
            new_lines.append(raw_line)
            continue
        match = _FRONTMATTER_KEY_RE.match(line)
        if match:
            indent, key, value = match.groups()
            is_quoted = value.startswith(('"', "'"))
            if needs_quoting(value) and not is_quoted:
                escaped = value.replace("\\", "\\\\").replace('"', '\\"')
                new_lines.append(f'{indent}{key}: "{escaped}"{carriage_return}')
                modified = True
                continue
        new_lines.append(raw_line)
    return "\n".join(new_lines), modified


def _iter_cache_files(cache_dir: Path, data_files: Iterable[Path] = ()):
    inputs = list(data_files)
    targets = (
        resolve_cache_paths(cache_dir, inputs)
        if inputs
        else sorted(cache_dir.glob("*.md"))
    )
    for md_file in targets:
        content = md_file.read_text(encoding="utf-8")
        match = _FRONTMATTER_RE.match(content)
        if match is None:
            continue
        yield md_file, content, match


def files_needing_requote(
    cache_dir: str | Path, data_files: Iterable[Path] = ()
) -> list[str]:
    """Read-only: names of cache files the sweep would rewrite (no writes)."""
    cache_dir = Path(cache_dir)
    if not cache_dir.exists():
        return []
    return [
        md_file.name
        for md_file, _content, match in _iter_cache_files(cache_dir, data_files)
        if requote_frontmatter(match.group("frontmatter"))[1]
    ]


def normalize_reference_cache(
    cache_dir: str | Path, data_files: Iterable[Path] = ()
) -> list[str]:
    """Quote frontmatter values that need it; return the names of rewritten files."""
    cache_dir = Path(cache_dir)
    rewritten: list[str] = []
    if not cache_dir.exists():
        return rewritten
    for md_file, content, match in _iter_cache_files(cache_dir, data_files):
        new_frontmatter, modified = requote_frontmatter(match.group("frontmatter"))
        if modified:
            normalized = (
                content[: match.start("frontmatter")]
                + new_frontmatter
                + content[match.end("frontmatter") :]
            )
            md_file.write_text(normalized, encoding="utf-8")
            rewritten.append(md_file.name)
    return rewritten


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    cache_dir = Path(args[0]) if args else Path("references_cache")
    data_files = [Path(value) for value in args[1:]]
    rewritten = normalize_reference_cache(cache_dir, data_files)
    if rewritten:
        print(f"fix-references-cache: re-quoted {len(rewritten)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
