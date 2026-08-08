"""Normalize YAML frontmatter only for reference caches in scope.

The historical ``fix-references-cache`` recipe swept every markdown file in
``references_cache/`` before even a single-file validation.  This module keeps
the explicit whole-cache maintenance mode, while allowing validation recipes
to pass their data files and touch only the cache records those files cite.
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

import yaml

from dismech.yaml_io import safe_load_path

DEFAULT_CACHE_DIR = Path("references_cache")
_FRONTMATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(?P<frontmatter>.*?)(?:\r?\n)---[ \t]*(?:\r?\n|\Z)",
    re.DOTALL,
)
_SCALAR_RE = re.compile(r"^(\s*)([a-z_]+):\s+(.+)$", re.IGNORECASE)
_PLAIN_SCALAR_INDICATORS = (
    "[",
    "{",
    "*",
    "&",
    "!",
    "@",
    "#",
    ">",
    "|",
    "%",
    "`",
    "?",
    "-",
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
    """Resolve cache files cited by ``data_files``, ignoring uncached references."""
    by_stem, by_bare_id = _cache_index(cache_dir)
    resolved: set[Path] = set()
    for data_file in data_files:
        try:
            data = safe_load_path(data_file)
        except (OSError, yaml.YAMLError):
            # This is a best-effort normalization pre-pass. The schema/data
            # validator that follows owns diagnostics for missing or malformed
            # inputs and should not be preempted by a traceback here.
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


def _quote_scalar(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def normalize_cache_file(path: Path) -> bool:
    """Quote unsafe plain frontmatter scalars, returning whether ``path`` changed."""
    content = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(content)
    if match is None:
        return False

    frontmatter = match.group("frontmatter")
    lines: list[str] = []
    modified = False
    for line in frontmatter.split("\n"):
        scalar = _SCALAR_RE.match(line)
        if scalar is None or not line.strip() or line.strip().startswith("-"):
            lines.append(line)
            continue

        indent, key, value = scalar.groups()
        is_quoted = value.startswith(('"', "'"))
        needs_quoting = (
            ": " in value
            or value.endswith(":")
            or value.startswith(_PLAIN_SCALAR_INDICATORS)
        )
        if needs_quoting and not is_quoted:
            lines.append(f"{indent}{key}: {_quote_scalar(value)}")
            modified = True
        else:
            lines.append(line)

    if not modified:
        return False

    normalized = (
        content[: match.start("frontmatter")]
        + "\n".join(lines)
        + content[match.end("frontmatter") :]
    )
    path.write_text(normalized, encoding="utf-8")
    return True


def normalize_cache(cache_dir: Path, data_files: Iterable[Path] = ()) -> list[Path]:
    """Normalize the cited cache subset, or the whole cache when no files are given."""
    inputs = list(data_files)
    targets = (
        resolve_cache_paths(cache_dir, inputs)
        if inputs
        else sorted(cache_dir.glob("*.md"))
    )
    return [path for path in targets if normalize_cache_file(path)]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Normalize reference-cache frontmatter without unrelated churn."
    )
    parser.add_argument(
        "data_files",
        nargs="*",
        type=Path,
        help="data YAML files whose cited caches should be normalized; omit for all",
    )
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.cache_dir.is_dir():
        return 0
    changed = normalize_cache(args.cache_dir, args.data_files)
    scope = "cited" if args.data_files else "total"
    print(f"Normalized {len(changed)} reference cache file(s) ({scope} scope).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
