"""Offline, affirmative count of the reference/snippet pairs in KB YAML files.

Issue #7252: ``linkml-reference-validator`` prints ``Total checks: 0`` on every
clean run because the counter it echoes (``total_results``) holds the number of
*issues found*, not the number of checks *performed* -- the plugin only yields a
result when something fails. A passing run is therefore indistinguishable from a
silent no-op, which has already caused at least one misdiagnosis (#7246).

This module is the downstream mitigation: it walks the same evidence pairs the
validator walks and reports an affirmative ``Snippets checked: N/N verified``
line. It is deliberately **advisory and read-only**:

- it never touches the network -- a snippet is checked only against the body
  already cached in ``references_cache/`` (the same bytes the validator used)
- it never changes exit codes; ``linkml-reference-validator`` stays the sole
  authority on pass/fail (``--strict`` exists for direct CLI use only)

Matching semantics are borrowed from the validator itself
(``SupportingTextValidator``: editorial ``[...]`` stripped, ``...`` splitting
into independently-matched parts, Greek letters spelled out, punctuation and
case folded, whitespace collapsed) so the two agree on what "verified" means.
"""

from __future__ import annotations

import argparse
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

try:  # pragma: no cover - exercised implicitly wherever YAML is loaded
    from yaml import CSafeLoader as _FastYamlLoader
except ImportError:  # pragma: no cover - only when libyaml is not built
    from yaml import SafeLoader as _FastYamlLoader

DEFAULT_SCHEMA = Path("src/dismech/schema/dismech.yaml")
DEFAULT_CONFIG = Path("conf/reference_validator_config.yaml")
DEFAULT_CACHE_DIR = Path("references_cache")

# Fallbacks used when the schema cannot be read. These are the dismech slots
# carrying ``implements: [linkml:excerpt]`` / ``[linkml:authoritative_reference]``.
FALLBACK_EXCERPT_FIELDS = frozenset({"snippet"})
FALLBACK_REFERENCE_FIELDS = frozenset({"reference"})

_EXCERPT_IMPLEMENTS = "linkml:excerpt"
_REFERENCE_IMPLEMENTS = "linkml:authoritative_reference"


@dataclass(frozen=True)
class SnippetPair:
    """One ``reference``/``snippet`` pair found in a data file."""

    path: Path
    location: str
    reference_id: str
    snippet: str


@dataclass(frozen=True)
class Unverified:
    """A pair that could not be affirmatively verified against the cache."""

    pair: SnippetPair
    reason: str

    def format(self) -> str:
        return (
            f"    {self.pair.path}:{self.pair.location}\n"
            f"      Reference: {self.pair.reference_id}\n"
            f"      {self.reason}"
        )


@dataclass
class AuditReport:
    """Aggregate counts across every file audited."""

    files: int = 0
    total: int = 0
    verified: int = 0
    skipped_prefix: int = 0
    not_cached: int = 0
    mismatched: list[Unverified] = field(default_factory=list)
    unreadable: list[str] = field(default_factory=list)

    def summary_line(self) -> str:
        """One-line affirmative summary, the counterpart of ``Total checks:``."""
        if self.total == 0:
            return "  Snippets checked: 0 (no reference/snippet pairs in input)"

        line = f"  Snippets checked: {self.verified}/{self.total} verified against cached references"
        notes: list[str] = []
        if self.mismatched:
            notes.append(f"{len(self.mismatched)} not found in cached text")
        if self.skipped_prefix:
            notes.append(f"{self.skipped_prefix} skipped by prefix")
        if self.not_cached:
            notes.append(f"{self.not_cached} not cached locally")
        if notes:
            line += f" ({', '.join(notes)})"
        return line

    def format(self) -> str:
        """Full advisory report: the summary line plus any unverified detail."""
        lines = [self.summary_line()]
        if self.mismatched:
            lines.append(
                f"  Snippets not found in the cached reference text ({len(self.mismatched)}):"
            )
            lines.extend(item.format() for item in self.mismatched)
        for problem in self.unreadable:
            lines.append(f"  Skipped (unreadable): {problem}")
        return "\n".join(lines)


def _load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.load(handle, Loader=_FastYamlLoader)


def _implements(definition: Any) -> list[str]:
    if not isinstance(definition, dict):
        return []
    implements = definition.get("implements")
    if isinstance(implements, str):
        return [implements]
    if isinstance(implements, list):
        return [item for item in implements if isinstance(item, str)]
    return []


def discover_field_names(schema_path: Path) -> tuple[frozenset[str], frozenset[str]]:
    """Return ``(excerpt_fields, reference_fields)`` declared by a LinkML schema.

    Fields are discovered from the same ``implements:`` annotations the upstream
    plugin uses, so the audit stays in step with the schema instead of hardcoding
    ``snippet``/``reference``. Falls back to those names if the schema cannot be
    read.
    """
    try:
        schema = _load_yaml(schema_path)
    except (OSError, yaml.YAMLError):
        return FALLBACK_EXCERPT_FIELDS, FALLBACK_REFERENCE_FIELDS

    if not isinstance(schema, dict):
        return FALLBACK_EXCERPT_FIELDS, FALLBACK_REFERENCE_FIELDS

    excerpts: set[str] = set()
    references: set[str] = set()

    def scan(definitions: Any) -> None:
        if not isinstance(definitions, dict):
            return
        for name, definition in definitions.items():
            implements = _implements(definition)
            if _EXCERPT_IMPLEMENTS in implements:
                excerpts.add(name)
            if _REFERENCE_IMPLEMENTS in implements:
                references.add(name)

    scan(schema.get("slots"))
    classes = schema.get("classes")
    if isinstance(classes, dict):
        for class_definition in classes.values():
            if isinstance(class_definition, dict):
                scan(class_definition.get("attributes"))

    return (
        frozenset(excerpts) or FALLBACK_EXCERPT_FIELDS,
        frozenset(references) or FALLBACK_REFERENCE_FIELDS,
    )


def _load_config(config_path: Path) -> dict[str, Any]:
    try:
        config = _load_yaml(config_path)
    except (OSError, yaml.YAMLError):
        return {}
    return config if isinstance(config, dict) else {}


def load_skip_prefixes(config_path: Path) -> frozenset[str]:
    """Read ``skip_prefixes`` from the reference-validator config (uppercased)."""
    prefixes = _load_config(config_path).get("skip_prefixes")
    if not isinstance(prefixes, list):
        return frozenset()
    return frozenset(str(prefix).upper() for prefix in prefixes)


def load_cache_dir(config_path: Path, default: Path = DEFAULT_CACHE_DIR) -> Path:
    """Read ``cache_dir`` from the reference-validator config, else ``default``."""
    cache_dir = _load_config(config_path).get("cache_dir")
    if isinstance(cache_dir, str) and cache_dir.strip():
        return Path(cache_dir)
    return default


def iter_snippet_pairs(
    path: Path,
    data: Any,
    excerpt_fields: Iterable[str],
    reference_fields: Iterable[str],
) -> Iterator[SnippetPair]:
    """Yield every reference/snippet pair in a loaded YAML document."""
    # Sorted so a node carrying more than one candidate field is handled
    # deterministically rather than at frozenset-iteration order.
    excerpts = tuple(sorted(excerpt_fields))
    references = tuple(sorted(reference_fields))

    def walk(node: Any, location: str) -> Iterator[SnippetPair]:
        if isinstance(node, dict):
            reference_id = next(
                (
                    node[name]
                    for name in references
                    if isinstance(node.get(name), str) and node[name].strip()
                ),
                None,
            )
            if reference_id is not None:
                for name in excerpts:
                    snippet = node.get(name)
                    if isinstance(snippet, str) and snippet.strip():
                        child = f"{location}.{name}" if location else name
                        yield SnippetPair(
                            path=path,
                            location=child,
                            reference_id=reference_id.strip(),
                            snippet=snippet,
                        )
            for key, value in node.items():
                child = f"{location}.{key}" if location else str(key)
                yield from walk(value, child)
        elif isinstance(node, list):
            for index, value in enumerate(node):
                yield from walk(value, f"{location}[{index}]")

    yield from walk(data, "")


class CachedReferenceIndex:
    """Read-only, memoized view over ``references_cache/`` bodies.

    Reuses ``linkml-reference-validator``'s own cache loader and text
    normalization so "verified" here means exactly what it means there. If the
    upstream private API ever moves, the local fallbacks below keep the audit
    working (it is advisory, so degrading is preferable to crashing).
    """

    def __init__(self, cache_dir: Path, skip_prefixes: Iterable[str] = ()) -> None:
        self.cache_dir = cache_dir
        self.skip_prefixes = frozenset(prefix.upper() for prefix in skip_prefixes)
        self._normalized: dict[str, str | None] = {}
        self._fetcher = self._build_fetcher(cache_dir)
        self._by_stem: dict[str, Path] | None = None
        self._by_bare_id: dict[str, Path | None] | None = None

    @staticmethod
    def _build_fetcher(cache_dir: Path) -> Any:
        try:
            from linkml_reference_validator.etl.reference_fetcher import (
                ReferenceFetcher,
            )
            from linkml_reference_validator.models import ReferenceValidationConfig
        except ImportError:  # pragma: no cover - validator always installed here
            return None
        return ReferenceFetcher(ReferenceValidationConfig(cache_dir=cache_dir))

    @staticmethod
    def normalize(text: str) -> str:
        """Normalize text exactly as the validator does before substring matching."""
        try:
            from linkml_reference_validator.validation.supporting_text_validator import (
                SupportingTextValidator,
            )
        except ImportError:  # pragma: no cover - validator always installed here
            return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", text.lower())).strip()
        return SupportingTextValidator.normalize_text(text)

    @staticmethod
    def split_snippet(snippet: str) -> list[str]:
        """Split a snippet into the parts the validator matches independently."""
        without_brackets = re.sub(r"\[.*?\]", " ", snippet)
        parts = re.split(r"\s*\.{2,}\s*", without_brackets)
        return [re.sub(r"\s+", " ", part).strip() for part in parts if part.strip()]

    def is_skipped(self, reference_id: str) -> bool:
        prefix = reference_id.split(":", 1)[0].upper() if ":" in reference_id else ""
        return bool(prefix) and prefix in self.skip_prefixes

    @staticmethod
    def _safe_id(reference_id: str) -> str:
        return (
            reference_id.replace(":", "_")
            .replace("/", "_")
            .replace("?", "_")
            .replace("=", "_")
        )

    def _build_filename_index(self) -> None:
        by_stem: dict[str, Path] = {}
        # A bare identifier (one the fetcher could not prefix, e.g. ``NCT06087757``)
        # is cached under the *source's* canonical id (``clinicaltrials_NCT…``).
        # Map the unprefixed tail back to its file, leaving ``None`` where two
        # prefixes claim the same tail so an ambiguous id is never resolved.
        by_bare: dict[str, Path | None] = {}
        try:
            entries = list(self.cache_dir.glob("*.md"))
        except OSError:  # pragma: no cover - unreadable cache directory
            entries = []
        for entry in entries:
            stem = entry.stem.casefold()
            by_stem.setdefault(stem, entry)
            prefix, _, tail = entry.stem.partition("_")
            if prefix and tail:
                tail_key = tail.casefold()
                by_bare[tail_key] = None if tail_key in by_bare else entry
        self._by_stem = by_stem
        self._by_bare_id = by_bare

    def resolve_cache_path(self, reference_id: str) -> Path | None:
        """Locate the cache file for a reference id, or ``None`` if uncached."""
        direct = self.cache_dir / f"{self._safe_id(reference_id)}.md"
        if direct.is_file():
            return direct

        if self._by_stem is None or self._by_bare_id is None:
            self._build_filename_index()
        assert self._by_stem is not None and self._by_bare_id is not None

        key = self._safe_id(reference_id).casefold()
        # DOI identifiers are case-insensitive in practice and the tracked cache
        # corpus carries mixed-case DOI filenames.
        match = self._by_stem.get(key)
        if match is not None:
            return match
        return self._by_bare_id.get(key)

    @staticmethod
    def _extract_body(text: str) -> str:
        """Strip YAML frontmatter and pre-content headers, as the fetcher does."""
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                text = parts[2]
        body = text.strip()
        lines = body.split("\n")
        for index, line in enumerate(lines):
            if line.strip().startswith("## Content"):
                return "\n".join(lines[index + 1 :]).strip()
        return body

    def _read_body(self, reference_id: str) -> str | None:
        if self._fetcher is not None:
            try:
                cached = self._fetcher._load_from_disk(
                    self._fetcher.normalize_reference_id(reference_id)
                )
            except Exception:  # pragma: no cover - upstream API drift
                cached = None
            if cached is not None and cached.content:
                return cached.content

        path = self.resolve_cache_path(reference_id)
        if path is None:
            return None
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:  # pragma: no cover - unreadable cache file
            return None
        return self._extract_body(text) or None

    def normalized_content(self, reference_id: str) -> str | None:
        """Normalized cached body for a reference, or ``None`` if not cached."""
        if reference_id not in self._normalized:
            body = self._read_body(reference_id)
            self._normalized[reference_id] = (
                None if body is None else self.normalize(body)
            )
        return self._normalized[reference_id]


def check_pair(index: CachedReferenceIndex, pair: SnippetPair) -> str | Unverified:
    """Classify one pair: ``"verified"``/``"skipped"``/``"not_cached"`` or a mismatch."""
    if index.is_skipped(pair.reference_id):
        return "skipped"

    content = index.normalized_content(pair.reference_id)
    if content is None:
        return "not_cached"

    parts = index.split_snippet(pair.snippet)
    if not parts:
        return Unverified(
            pair=pair,
            reason="Snippet is empty after removing bracketed editorial notes",
        )

    for part in parts:
        if index.normalize(part) not in content:
            return Unverified(
                pair=pair, reason=f"Text part not found as substring: {part!r}"
            )
    return "verified"


def audit_files(
    paths: Iterable[Path],
    *,
    schema_path: Path = DEFAULT_SCHEMA,
    config_path: Path = DEFAULT_CONFIG,
    cache_dir: Path | None = None,
) -> AuditReport:
    """Count and re-verify every reference/snippet pair in ``paths``."""
    excerpt_fields, reference_fields = discover_field_names(schema_path)
    if cache_dir is None:
        cache_dir = load_cache_dir(config_path)
    index = CachedReferenceIndex(cache_dir, load_skip_prefixes(config_path))

    report = AuditReport()
    for path in paths:
        try:
            data = _load_yaml(path)
        except (OSError, yaml.YAMLError) as exc:
            report.unreadable.append(f"{path}: {exc.__class__.__name__}")
            continue

        report.files += 1
        for pair in iter_snippet_pairs(path, data, excerpt_fields, reference_fields):
            report.total += 1
            outcome = check_pair(index, pair)
            if outcome == "verified":
                report.verified += 1
            elif outcome == "skipped":
                report.skipped_prefix += 1
            elif outcome == "not_cached":
                report.not_cached += 1
            else:
                report.mismatched.append(outcome)  # type: ignore[arg-type]

    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m dismech.reference_snippet_audit",
        description=(
            "Count reference/snippet pairs and re-verify each against the local "
            "reference cache. Advisory: linkml-reference-validator remains "
            "authoritative for pass/fail (issue #7252)."
        ),
    )
    parser.add_argument("files", nargs="+", type=Path, help="YAML data files to audit")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="Reference cache directory (default: the config's cache_dir, else references_cache)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any snippet is not found in its cached reference text",
    )
    args = parser.parse_args(argv)

    report = audit_files(
        args.files,
        schema_path=args.schema,
        config_path=args.config,
        cache_dir=args.cache_dir,
    )
    print(report.format())

    if args.strict and report.mismatched:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
