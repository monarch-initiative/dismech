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
Which brackets count as editorial is read from the same config both tools use
(``literal_bracket_patterns``), and a mismatch that bracket stripping alone
explains says so in its reason rather than reporting a bare "not found" that
reads as a misquote (#8597).

Issue #7450 added a second, deliberately narrow matching pass on top of that,
because a mismatch against the cache is not the same claim as a misquote in the
KB. Two defects live in *our cached text* rather than in the curation:

- **PDF ligatures.** PDF extraction emits ``ﬁ`` (U+FB01) and friends, so the
  cache reads ``amyloid ﬁbrils`` where the snippet reads ``amyloid fibrils``.
  The upstream ``normalize_text`` does not fold these.
- **Stripped inline markup joining words.** Full-text HTML extraction removes
  ``<i>``/``<em>`` without inserting a space, so "within the *ANAPC7* locus"
  caches as ``within theANAPC7locus``.

Both are cache defects that no amount of re-quoting can fix, so a snippet that
matches only after ligature folding and ignoring word boundaries is reported as
verified under :data:`PairOutcome.VERIFIED_RELAXED` -- counted as verified, but
tallied separately so the cache-defect backlog stays visible.

Separately, a snippet quoted from full text that was never cached (the cache
holds only the abstract) is neither a misquote nor a mangled cache but an
*incomplete* one, and is reported as :data:`PairOutcome.ABSTRACT_ONLY` rather
than as a mismatch -- mirroring the note the upstream validator already emits on
the PMID path.

That split is diagnostic, not an exemption. An abstract-only pair is still
**unverified**: nothing was proved about it either way, and roughly 23,000 of the
cached references are abstract-only, so treating the state as automatically
benign would hide far more than the ``skip_prefixes`` gap that prompted #7450.
``--strict`` therefore still fails on it unless ``--allow-abstract-only`` is
passed. Upstream agrees on the substance -- ``SupportingTextValidator`` appends
its "only abstract available" note to a result whose severity stays ``ERROR``.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from collections import OrderedDict
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

import yaml

from dismech.frontmatter import split_frontmatter
from dismech.yaml_io import safe_load

DEFAULT_SCHEMA = Path("src/dismech/schema/dismech.yaml")
DEFAULT_CONFIG = Path("conf/reference_validator_config.yaml")
DEFAULT_CACHE_DIR = Path("references_cache")

# Fallbacks used when the schema cannot be read. These are the dismech slots
# carrying ``implements: [linkml:excerpt]`` / ``[linkml:authoritative_reference]``.
FALLBACK_EXCERPT_FIELDS = frozenset({"snippet"})
FALLBACK_REFERENCE_FIELDS = frozenset({"reference"})

_EXCERPT_IMPLEMENTS = "linkml:excerpt"
_REFERENCE_IMPLEMENTS = "linkml:authoritative_reference"

# Normalized reference bodies are large (~18 KB each), and a whole-KB run touches
# thousands of them, so the memo is an LRU rather than an unbounded dict. Pairs
# citing one reference cluster within a file, so a modest window keeps the hit
# rate high while capping peak RSS.
NORMALIZED_CACHE_SIZE = 512

# Mismatch detail is printed for triage, but a misconfigured run (e.g. a
# --cache-dir pointing somewhere unrelated) can produce thousands; cap the
# detail so a CI log stays readable. The summary line always reports the
# full count.
MAX_REPORTED_MISMATCHES = 20

# Multi-letter forms that must be expanded before matching. Two different kinds
# live here, and the table is NOT redundant with the NFKC pass that follows it:
#
# - The first block are true *compatibility* ligatures, the ones PDF text
#   extraction emits as single codepoints. NFKC does decompose these, so listing
#   them is a fast path rather than a necessity.
# - ``Æ æ Œ œ`` are encoded as distinct letters, not compatibility characters,
#   and NFKC leaves them exactly as they are. For those four this table is the
#   only thing doing the folding. They are also genuine orthography (archaic
#   ``anæmia``, ``fœtal``) rather than an extractor artifact -- folding them
#   symmetrically costs nothing for matching and lets a modern transcription
#   match an old-spelling source.
LIGATURES = {
    # Compatibility ligatures (NFKC would also handle these).
    "ﬀ": "ff",
    "ﬁ": "fi",
    "ﬂ": "fl",
    "ﬃ": "ffi",
    "ﬄ": "ffl",
    "ﬅ": "st",
    "ﬆ": "st",
    "Ĳ": "IJ",
    "ĳ": "ij",
    # Distinct letters: NFKC does NOT touch these, so the table is required.
    "Œ": "OE",
    "œ": "oe",
    "Æ": "AE",
    "æ": "ae",
}

# ``content_type`` values in the reference-cache frontmatter that mean "no full
# text was ever cached". A snippet quoted from the body of such a paper cannot
# be found locally however faithfully it was transcribed.
ABSTRACT_ONLY_CONTENT_TYPES = frozenset(
    {"abstract_only", "summary", "unavailable", "url"}
)

_CONTENT_TYPE_RE = re.compile(
    r"^content_type:\s*[\"']?([\w_]+)[\"']?\s*$", re.MULTILINE
)


class PairOutcome(Enum):
    """Classification of a reference/snippet pair that produced no mismatch."""

    VERIFIED = "verified"
    VERIFIED_RELAXED = "verified_relaxed"
    ABSTRACT_ONLY = "abstract_only"
    SKIPPED_PREFIX = "skipped"
    NOT_CACHED = "not_cached"


@dataclass(frozen=True)
class SnippetPair:
    """One ``reference``/``snippet`` pair found in a data file."""

    path: Path
    location: str
    reference_id: str
    snippet: str


@dataclass(frozen=True)
class Unverified:
    """A pair that could not be affirmatively verified against the cache.

    ``outcome`` separates a genuine mismatch (the default) from the advisory
    abstract-only state, which carries the same detail but is not a finding.
    """

    pair: SnippetPair
    reason: str
    outcome: PairOutcome | None = None

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
    verified_relaxed: int = 0
    abstract_only: int = 0
    skipped_prefix: int = 0
    not_cached: int = 0
    mismatched: list[Unverified] = field(default_factory=list)
    abstract_only_pairs: list[Unverified] = field(default_factory=list)
    boundary_suspect: list[Unverified] = field(default_factory=list)
    unreadable: list[str] = field(default_factory=list)

    def summary_line(self) -> str:
        """One-line affirmative summary, the counterpart of ``Total checks:``."""
        if self.total == 0:
            return "  Snippets checked: 0 (no reference/snippet pairs in input)"

        verified = self.verified + self.verified_relaxed
        line = f"  Snippets checked: {verified}/{self.total} verified against cached references"
        notes: list[str] = []
        if self.verified_relaxed:
            notes.append(
                f"{self.verified_relaxed} only after cache-defect normalization"
            )
        if self.mismatched:
            notes.append(f"{len(self.mismatched)} not found in cached text")
        if self.abstract_only:
            notes.append(f"{self.abstract_only} quoted beyond an abstract-only cache")
        if self.skipped_prefix:
            notes.append(f"{self.skipped_prefix} skipped by prefix")
        if self.not_cached:
            notes.append(f"{self.not_cached} not cached locally")
        if self.boundary_suspect:
            notes.append(f"{len(self.boundary_suspect)} starting or ending mid-word")
        if notes:
            line += f" ({', '.join(notes)})"
        return line

    def format(self, max_mismatches: int = MAX_REPORTED_MISMATCHES) -> str:
        """Full advisory report: the summary line plus any unverified detail."""
        lines = [self.summary_line()]
        if self.abstract_only_pairs:
            lines.append(
                f"  Unverified: {len(self.abstract_only_pairs)} snippet(s) were not "
                "found, but only an abstract is cached for them -- the full text may "
                "contain the excerpt. Reported apart from mismatches because nothing "
                "was established either way:"
            )
            lines.extend(
                item.format() for item in self.abstract_only_pairs[:max_mismatches]
            )
            remaining = len(self.abstract_only_pairs) - max_mismatches
            if remaining > 0:
                lines.append(f"    ... and {remaining} more")
        if self.boundary_suspect:
            lines.append(
                f"  Snippets verified only as a mid-word fragment ({len(self.boundary_suspect)}). "
                "The quote IS in the cached text, so every other check passes -- "
                "which is exactly what made dismech#9207 invisible for two fix "
                "rounds. A fragment cut inside a word carries no propositional "
                "content and invites the truncation being read back as a fact "
                "about the source:"
            )
            lines.extend(
                item.format() for item in self.boundary_suspect[:max_mismatches]
            )
            remaining = len(self.boundary_suspect) - max_mismatches
            if remaining > 0:
                lines.append(f"    ... and {remaining} more")
        if self.mismatched:
            lines.append(
                f"  Snippets not found in the cached reference text ({len(self.mismatched)}):"
            )
            lines.extend(item.format() for item in self.mismatched[:max_mismatches])
            remaining = len(self.mismatched) - max_mismatches
            if remaining > 0:
                lines.append(f"    ... and {remaining} more")
        for problem in self.unreadable:
            lines.append(f"  Skipped (unreadable): {problem}")
        return "\n".join(lines)


def _load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return safe_load(handle)


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


def load_literal_bracket_patterns(config_path: Path) -> tuple[str, ...]:
    """Read ``literal_bracket_patterns`` from the reference-validator config.

    These mark bracketed text the validator treats as *source* text rather than
    an editorial note, so the audit must apply the same rule to stay in parity.
    """
    patterns = _load_config(config_path).get("literal_bracket_patterns")
    if not isinstance(patterns, list):
        return ()
    return tuple(str(pattern) for pattern in patterns)


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

    def __init__(
        self,
        cache_dir: Path,
        skip_prefixes: Iterable[str] = (),
        literal_bracket_patterns: Iterable[str] = (),
        cache_size: int = NORMALIZED_CACHE_SIZE,
    ) -> None:
        self.cache_dir = cache_dir
        self.skip_prefixes = frozenset(prefix.upper() for prefix in skip_prefixes)
        self._literal_bracket_regexes = [
            re.compile(pattern) for pattern in literal_bracket_patterns
        ]
        self._cache_size = max(1, cache_size)
        self._normalized: OrderedDict[str, str | None] = OrderedDict()
        self._relaxed: OrderedDict[str, str | None] = OrderedDict()
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

    @classmethod
    def fold_ligatures(cls, text: str) -> str:
        """Expand typographic ligatures a PDF extractor leaves in cached text.

        ``normalize_text`` treats ``ﬁ`` (U+FB01) as a single word character, so
        cached ``amyloid ﬁbrils`` never matches a snippet reading ``amyloid
        fibrils`` however faithful the transcription. Folding is applied to both
        sides, so it can only ever bring a correct quote and its mangled cache
        back into agreement -- it cannot make two genuinely different strings
        match.
        """
        for ligature, expansion in LIGATURES.items():
            text = text.replace(ligature, expansion)
        return unicodedata.normalize("NFKC", text)

    @classmethod
    def normalize_relaxed(cls, text: str) -> str:
        """Normalize for the cache-defect pass: folded ligatures, no word gaps.

        Dropping whitespace entirely is what tolerates markup-stripped joins
        (``theANAPC7locus``). It is a real loosening, but a narrow one: the
        snippet's characters must still appear contiguously and in order, so it
        merges word boundaries rather than admitting arbitrary text. Only pairs
        that already failed the strict check are ever tested this way.
        """
        return cls.normalize(cls.fold_ligatures(text)).replace(" ", "")

    def split_snippet(self, snippet: str) -> list[str]:
        """Split a snippet into the parts the validator matches independently.

        Mirrors ``SupportingTextValidator._split_query``, including its
        ``literal_bracket_patterns`` branch: bracketed content matching a
        configured pattern is source text the validator keeps, so the audit must
        keep it too. Under this repo's config that means an all-caps
        abbreviation (``[APTT]``) or a percent-bearing span (``[28, 62%]``).
        Without configured patterns both sides strip every ``[...]`` as an
        editorial note.
        """

        def replace_bracket(match: re.Match[str]) -> str:
            if self.is_literal_bracket(match.group(1)):
                return match.group(0)
            return " "

        without_brackets = re.sub(r"\[(.*?)\]", replace_bracket, snippet)
        return self._split_parts(without_brackets)

    def is_literal_bracket(self, content: str) -> bool:
        """True when bracketed ``content`` is source text rather than a gloss.

        Content matching a configured ``literal_bracket_pattern`` is kept; with
        no patterns configured nothing is literal, which is upstream's default.
        """
        return any(regex.search(content) for regex in self._literal_bracket_regexes)

    def stripped_brackets(self, snippet: str) -> tuple[str, ...]:
        """Bracketed spans this snippet loses before matching, in order."""
        return tuple(
            match.group(0)
            for match in re.finditer(r"\[(.*?)\]", snippet)
            if not self.is_literal_bracket(match.group(1))
        )

    def brackets_explaining_mismatch(
        self, snippet: str, content: str
    ) -> tuple[str, ...]:
        """Stripped spans whose removal is what broke the match, else empty.

        Used only to explain a failure (#8597): when a quote matches the cached
        text with these spans restored, nothing is wrong with the quote -- the
        bracket-stripping step is what broke it, and the error should say so
        rather than leave the curator hunting for a paraphrase they never wrote.

        A snippet can carry both kinds of bracket at once -- a genuine curator
        gloss (absent from the source, and correctly stripped) alongside source
        text the config does not yet keep. Restoring only the spans that are
        actually present in the cached text separates the two, so the hint names
        the culprit instead of going silent on the mixed case.
        """
        candidates = tuple(
            span
            for span in self.stripped_brackets(snippet)
            if self.normalize(span[1:-1]).strip()
            and self.normalize(span[1:-1]) in content
        )
        if not candidates:
            return ()

        def restore(match: re.Match[str]) -> str:
            keep = (
                self.is_literal_bracket(match.group(1)) or match.group(0) in candidates
            )
            return match.group(0) if keep else " "

        restored = re.sub(r"\[(.*?)\]", restore, snippet)
        if all(self.normalize(part) in content for part in self._split_parts(restored)):
            return candidates
        return ()

    @staticmethod
    def _split_parts(text: str) -> list[str]:
        parts = re.split(r"\s*\.{2,}\s*", text)
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
    def extract_body(text: str) -> str:
        """Strip YAML frontmatter and pre-content headers, as the fetcher does.

        The frontmatter split is delimiter-aware (issue #7697): a ``---`` inside a
        title must not be mistaken for the closing delimiter, or the leftover
        frontmatter leaks into the body and a snippet quoting the *title* can
        spuriously verify.
        """
        split = split_frontmatter(text)
        if split is not None:
            text = split.body
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
        return self.extract_body(text) or None

    def _memoized_content(
        self,
        memo: OrderedDict[str, str | None],
        reference_id: str,
        normalizer: Callable[[str], str],
    ) -> str | None:
        if reference_id in memo:
            memo.move_to_end(reference_id)
            return memo[reference_id]

        body = self._read_body(reference_id)
        content = None if body is None else normalizer(body)
        memo[reference_id] = content
        while len(memo) > self._cache_size:
            memo.popitem(last=False)
        return content

    def normalized_content(self, reference_id: str) -> str | None:
        """Normalized cached body for a reference, or ``None`` if not cached."""
        return self._memoized_content(self._normalized, reference_id, self.normalize)

    def relaxed_content(self, reference_id: str) -> str | None:
        """Cached body under :meth:`normalize_relaxed`, or ``None`` if not cached."""
        return self._memoized_content(
            self._relaxed, reference_id, self.normalize_relaxed
        )

    def content_type(self, reference_id: str) -> str | None:
        """``content_type`` from the cache file's frontmatter, if it has one.

        Used to tell an *incomplete* cache (abstract only, full text never
        fetched) apart from a genuinely absent quote. Read straight from the
        file rather than via the fetcher, which surfaces only the body.
        """
        path = self.resolve_cache_path(reference_id)
        if path is None:
            return None
        try:
            with path.open(encoding="utf-8") as handle:
                head = handle.read(4096)
        except OSError:  # pragma: no cover - unreadable cache file
            return None
        if not head.startswith("---"):
            return None
        # ``head`` is a bounded read, so the closing delimiter may fall outside it;
        # fall back to scanning what we have rather than losing the field.
        split = split_frontmatter(head)
        frontmatter = split.frontmatter if split is not None else head
        match = _CONTENT_TYPE_RE.search(frontmatter)
        return match.group(1) if match else None

    def is_abstract_only(self, reference_id: str) -> bool:
        """True when the cache holds no full text for this reference."""
        content_type = self.content_type(reference_id)
        return content_type is not None and content_type in ABSTRACT_ONLY_CONTENT_TYPES


def boundary_defect(index: CachedReferenceIndex, pair: SnippetPair) -> str | None:
    """Reason a strictly-verified snippet begins or ends inside a word, else ``None``.

    A snippet cut mid-word is a substring of the cached text, so it verifies --
    which is precisely the property that hid dismech#9207 through two fix
    rounds. Four snippets there stopped at ``movement d``; the truncation was
    then read back as a *fact about the source* ("the cached abstract is
    truncated mid-word") and restated in a node description and an evidence
    explanation, all of it validating cleanly the whole time.

    Because ``normalize`` reduces text to word characters and single spaces, the
    test is just whether the match is flanked by a non-space character. A quote
    is reported only when **every** occurrence in the cached text is flanked --
    a fragment that lands cleanly somewhere is a real quote that also happens to
    appear inside a longer word elsewhere.

    Deliberately restricted to strict matches. ``normalize_relaxed`` ends in
    ``.replace(" ", "")``, so under relaxed matching *every* match is flanked by
    word characters by construction and this would fire on 100% of relaxed
    verifications -- which are exactly the #8048 ligature/hyphenation cases that
    the legitimate "begins mid-word" curator notes are about.
    """
    content = index.normalized_content(pair.reference_id)
    if content is None:
        return None
    for part in index.split_snippet(pair.snippet):
        needle = index.normalize(part)
        if not needle:
            continue
        clean = False
        flanks: list[str] = []
        start = content.find(needle)
        while start != -1:
            end = start + len(needle)
            before = content[start - 1] if start > 0 else " "
            after = content[end] if end < len(content) else " "
            # Only an ALPHABETIC flank means a word was cut in half. A digit
            # flank is a superscript citation marker or footnote fused into the
            # cached text by extraction ("...hearing loss and microcephaly20-26"
            # in PMID:40760247) -- a cache defect of the #8048 family that the
            # curator cannot fix by re-quoting, and not the #9207 shape at all.
            if not before.isalpha() and not after.isalpha():
                clean = True
                break
            side = []
            if before.isalpha():
                side.append("start")
            if after.isalpha():
                side.append("end")
            flanks.append("/".join(side))
            start = content.find(needle, start + 1)
        if clean or not flanks:
            continue
        where = " and ".join(sorted(set(flanks[0].split("/"))))
        return (
            f"Snippet part {part!r} appears in the cached text only as a "
            f"mid-word fragment (cut at the {where}). Re-quote from a word "
            "boundary; do not record the cut as a property of the source."
        )
    return None


def check_pair(
    index: CachedReferenceIndex, pair: SnippetPair
) -> PairOutcome | Unverified:
    """Classify one pair: a :class:`PairOutcome`, or an :class:`Unverified` mismatch."""
    if index.is_skipped(pair.reference_id):
        return PairOutcome.SKIPPED_PREFIX

    content = index.normalized_content(pair.reference_id)
    if content is None:
        return PairOutcome.NOT_CACHED

    parts = index.split_snippet(pair.snippet)
    if not parts:
        return Unverified(
            pair=pair,
            reason="Snippet is empty after removing bracketed editorial notes",
        )

    missing = [part for part in parts if index.normalize(part) not in content]
    if not missing:
        return PairOutcome.VERIFIED

    # Second pass: the cache, not the quote, may be at fault (#7450). Ligatures
    # and markup-stripped word joins are cache-extraction defects the curator
    # cannot fix by re-quoting.
    relaxed = index.relaxed_content(pair.reference_id)
    if relaxed is not None and all(
        index.normalize_relaxed(part) in relaxed for part in parts
    ):
        return PairOutcome.VERIFIED_RELAXED

    # Third pass: name bracket stripping when that is what broke the match
    # (#8597). The quote is then present in the cache verbatim, so this is
    # neither a misquote nor an incomplete cache, and saying "not found as
    # substring" and stopping sends the curator looking for a paraphrase that
    # does not exist. The fix is a `literal_bracket_patterns` entry in
    # conf/reference_validator_config.yaml, not a re-quote.
    culprits = index.brackets_explaining_mismatch(pair.snippet, content)
    if culprits:
        spans = (
            culprits[0]
            if len(culprits) == 1
            else f"{', '.join(culprits[:-1])} and {culprits[-1]}"
        )
        verb = "is" if len(culprits) == 1 else "are"
        return Unverified(
            pair=pair,
            reason=(
                f"Text part not found as substring: {missing[0]!r} "
                f"(note: the snippet matches the cached text exactly once {spans} "
                f"{verb} kept; bracketed spans are stripped before matching "
                "unless conf/reference_validator_config.yaml lists a matching "
                "literal_bracket_patterns entry)"
            ),
        )

    # Fourth pass: an abstract-only cache cannot contain a quote taken from the
    # full text. That is an incomplete cache, not a misquote, so it is reported
    # as its own advisory state rather than as a mismatch.
    if index.is_abstract_only(pair.reference_id):
        return Unverified(
            pair=pair,
            reason=(
                f"Text part not found as substring: {missing[0]!r} "
                "(note: only abstract available in cache; full text may contain "
                "this excerpt)"
            ),
            outcome=PairOutcome.ABSTRACT_ONLY,
        )

    return Unverified(
        pair=pair, reason=f"Text part not found as substring: {missing[0]!r}"
    )


def audit_files(
    paths: Iterable[Path],
    *,
    schema_path: Path = DEFAULT_SCHEMA,
    config_path: Path = DEFAULT_CONFIG,
    cache_dir: Path | None = None,
    unskip_prefixes: Iterable[str] = (),
    check_boundaries: bool = False,
) -> AuditReport:
    """Count and re-verify every reference/snippet pair in ``paths``.

    ``unskip_prefixes`` drops prefixes from the config's ``skip_prefixes`` for
    this run only, so the coverage the skip currently hides can be measured
    without changing what the gating validator does (#7450).
    """
    excerpt_fields, reference_fields = discover_field_names(schema_path)
    if cache_dir is None:
        cache_dir = load_cache_dir(config_path)
    skip_prefixes = set(load_skip_prefixes(config_path)) - {
        prefix.upper() for prefix in unskip_prefixes
    }
    index = CachedReferenceIndex(
        cache_dir,
        skip_prefixes,
        load_literal_bracket_patterns(config_path),
    )

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
            if isinstance(outcome, Unverified):
                if outcome.outcome is PairOutcome.ABSTRACT_ONLY:
                    report.abstract_only += 1
                    report.abstract_only_pairs.append(outcome)
                else:
                    report.mismatched.append(outcome)
            elif outcome is PairOutcome.VERIFIED:
                report.verified += 1
                if check_boundaries:
                    reason = boundary_defect(index, pair)
                    if reason is not None:
                        report.boundary_suspect.append(
                            Unverified(pair=pair, reason=reason)
                        )
            elif outcome is PairOutcome.VERIFIED_RELAXED:
                report.verified_relaxed += 1
            elif outcome is PairOutcome.SKIPPED_PREFIX:
                report.skipped_prefix += 1
            else:
                report.not_cached += 1

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
    parser.add_argument(
        "--allow-abstract-only",
        action="store_true",
        help=(
            "With --strict, do not fail on snippets that were not found in a cache "
            "holding only an abstract (the full text may contain them). Off by "
            "default: such a pair is unverified, not verified."
        ),
    )
    parser.add_argument(
        "--check-boundaries",
        action="store_true",
        help=(
            "Also report snippets that verify only as a mid-word fragment of the "
            "cached text (issue #9226). Off by default so the affirmative count "
            "stays cheap; strict matches only, never relaxed ones."
        ),
    )
    parser.add_argument(
        "--unskip-prefix",
        action="append",
        default=[],
        metavar="PREFIX",
        help=(
            "Audit references with this prefix even though the config lists it in "
            "skip_prefixes (repeatable, e.g. --unskip-prefix DOI). Affects this "
            "advisory run only; the gating validator is unchanged. See issue #7450."
        ),
    )
    args = parser.parse_args(argv)

    report = audit_files(
        args.files,
        schema_path=args.schema,
        config_path=args.config,
        cache_dir=args.cache_dir,
        unskip_prefixes=args.unskip_prefix,
        check_boundaries=args.check_boundaries,
    )
    print(report.format())

    if args.strict:
        # boundary_suspect is populated only when --check-boundaries was passed,
        # so an existing --strict caller that does not opt in sees an empty list
        # and its exit code is unchanged. Opting in makes boundary findings
        # gating, which is the point of asking for them.
        unverified = list(report.mismatched) + report.boundary_suspect
        if not args.allow_abstract_only:
            unverified += report.abstract_only_pairs
        if unverified:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
