"""Abstract base for structured-database reference sources.

A :class:`StructuredSource` ingests a structured knowledge base (typically
bulk XML/JSON/TSV) and emits one markdown file per entity into
``references_cache/``. Each file uses the same UniProt-flat-file-inspired
line format so curators can quote individual rows as evidence ``snippet:``
values that validate as exact substrings of the cached body.

Subclasses implement three things:

1. ``bulk_files`` — the URLs / sha256s / local paths of bulk data files
2. ``index()`` — parse bulk data into ``{id: record}`` (lazy, lru-cached)
3. ``serialize_body(record)`` — emit deterministic line-oriented text

The base class handles cache-file IO, frontmatter, manifest pinning, and
registration with :mod:`linkml_reference_validator`.
"""

from __future__ import annotations

import hashlib
import logging
import re
from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import ClassVar

import requests

logger = logging.getLogger(__name__)


def _yaml_quote(s: str) -> str:
    """Double-quote a YAML string with minimal escaping.

    Matches the style produced by ``linkml-reference-validator``'s cache
    writer (which double-quotes ``reference_id`` and titles containing
    special characters).
    """
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


@dataclass(frozen=True)
class BulkFile:
    """One bulk-data file pinned in a source's manifest."""

    name: str
    url: str
    sha256: str
    description: str = ""


class ChecksumMismatchError(RuntimeError):
    """A freshly downloaded bulk file does not match its pinned sha256.

    Carries the remedy in its message. Nearly every occurrence of this in
    practice is upstream having published a new release behind an unversioned
    URL (issues #9687, #9897, #10150 for Orphadata; #10081 for ClinGen), which
    is fixed by repinning the manifest rather than by investigating a download.
    """

    def __init__(self, *, name: str, url: str, expected: str, actual: str) -> None:
        self.name = name
        self.url = url
        self.expected = expected
        self.actual = actual
        super().__init__(
            f"checksum mismatch for {name} after download:\n"
            f"  expected (manifest pin): {expected}\n"
            f"  actual   (upstream now): {actual}\n"
            f"  url: {url}\n"
            "\nThis usually means upstream published a new release behind the same\n"
            "URL, not that the download is corrupt. To accept the new release and\n"
            "record it in the manifest (leaving a reviewable diff), re-run with\n"
            "--repin, e.g.:\n"
            "    just refresh-orphadata --repin\n"
            "then rebuild the cache and review the diff before committing."
        )


@dataclass(frozen=True)
class ChecksumChange:
    """An observed difference between a manifest's pin and what upstream now serves.

    Recorded (rather than raised) when :meth:`StructuredSource.refresh` is called
    with ``repin=True``, so the caller can write the new values back to the
    manifest and leave a reviewable diff.
    """

    name: str
    old_sha256: str
    new_sha256: str
    size_bytes: int


@dataclass
class ReferenceCacheEntry:
    """One serialized cache entry.

    The ``body`` is a deterministic line-oriented text rendering. The
    frontmatter fields match
    :class:`dismech.reference_cache_frontmatter.ReferenceCacheFrontmatter`
    so the deterministic cache contract check accepts the file.
    """

    reference_id: str
    title: str
    body: str
    content_type: str = "structured_record"
    extra_frontmatter: dict = field(default_factory=dict)

    def filename(self) -> str:
        """Filename derived from ``reference_id`` (matches cache contract)."""
        return (
            self.reference_id.replace(":", "_")
            .replace("/", "_")
            .replace("?", "_")
            .replace("=", "_")
            + ".md"
        )

    def render(self) -> str:
        """Render the full markdown file (frontmatter + body).

        Frontmatter is emitted in insertion order (matching the upstream
        ``linkml-reference-validator`` cache writer): ``reference_id``,
        ``title``, then any extra fields, then ``content_type``.
        """
        from io import StringIO

        fm: list[tuple[str, object]] = [
            ("reference_id", self.reference_id),
            ("title", self.title),
        ]
        for k, v in self.extra_frontmatter.items():
            if k in {"reference_id", "title", "content_type"}:
                continue
            fm.append((k, v))
        fm.append(("content_type", self.content_type))

        buf = StringIO()
        buf.write("---\n")
        for k, v in fm:
            if v is None or v == "":
                continue
            if isinstance(v, str):
                buf.write(f"{k}: {_yaml_quote(v)}\n")
            elif isinstance(v, (int, float)):
                buf.write(f"{k}: {v}\n")
            elif isinstance(v, bool):
                buf.write(f"{k}: {'true' if v else 'false'}\n")
            else:
                # Unsupported types — coerce to string
                buf.write(f"{k}: {_yaml_quote(str(v))}\n")
        buf.write("---\n\n")
        buf.write(self.body)
        if not self.body.endswith("\n"):
            buf.write("\n")
        return buf.getvalue()


class StructuredSource(ABC):
    """Base class for a structured-database reference source.

    Subclasses are organized around three responsibilities:

    - **Bulk data acquisition**: ``refresh()`` downloads and verifies
      the files in ``bulk_files`` against pinned sha256s.
    - **Indexing**: ``index()`` parses bulk data into a mapping of
      ``identifier -> record``. Cached for the process lifetime.
    - **Serialization**: ``serialize(id_)`` returns a
      :class:`ReferenceCacheEntry` whose body is the deterministic text.
    """

    prefix: ClassVar[str] = ""
    id_pattern: ClassVar[re.Pattern] = re.compile(r".+")
    bulk_files: ClassVar[tuple[BulkFile, ...]] = ()
    snapshot_date: ClassVar[str] = ""
    schema_tag: ClassVar[str] = ""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        self._index_cache: dict[str, object] | None = None

    # ----- bulk data -----

    def refresh(
        self, *, force: bool = False, repin: bool = False
    ) -> list[ChecksumChange]:
        """Download bulk files into ``data_dir``, verifying sha256.

        Existing files with matching checksum are kept; mismatches re-download.

        **On a post-download checksum mismatch there are two possibilities, and
        they need different handling.** Most of these manifests pin a sha256
        against a *rolling* upstream URL — ``en_product1.xml`` is always the
        current Orphanet release, not a versioned artifact — so the pin is
        guaranteed to go stale the next time upstream publishes. That is
        ordinary release drift, not a problem with the download. The other
        possibility, a truncated or substituted file, is a real fault.

        The default (``repin=False``) refuses to proceed, because a source
        silently changing under a curator is exactly what the pin exists to
        catch. Passing ``repin=True`` instead *records* the new checksum and
        returns it, so the caller can write it back to the manifest and leave a
        diff a human reviews. Nothing is ever repinned implicitly.

        Returns the checksum changes observed (always empty unless ``repin``).
        """
        self.data_dir.mkdir(parents=True, exist_ok=True)
        changes: list[ChecksumChange] = []
        for bf in self.bulk_files:
            target = self.data_dir / bf.name
            if not force and target.exists():
                actual = _sha256_of(target)
                if actual == bf.sha256:
                    logger.info("OK  %s (%s)", bf.name, bf.sha256[:12])
                    continue
                logger.warning(
                    "checksum mismatch for %s (got %s, expected %s); refetching",
                    bf.name,
                    actual[:12],
                    bf.sha256[:12],
                )
            logger.info("downloading %s ...", bf.url)
            self._download(bf.url, target)
            actual = _sha256_of(target)
            if bf.sha256 and actual != bf.sha256:
                if not repin:
                    raise ChecksumMismatchError(
                        name=bf.name,
                        url=bf.url,
                        expected=bf.sha256,
                        actual=actual,
                    )
                logger.warning(
                    "repinning %s: %s -> %s", bf.name, bf.sha256[:12], actual[:12]
                )
                changes.append(
                    ChecksumChange(
                        name=bf.name,
                        old_sha256=bf.sha256,
                        new_sha256=actual,
                        size_bytes=target.stat().st_size,
                    )
                )
        return changes

    @staticmethod
    def _download(url: str, target: Path) -> None:
        with requests.get(url, stream=True, timeout=120) as r:
            r.raise_for_status()
            tmp = target.with_suffix(target.suffix + ".tmp")
            with tmp.open("wb") as fh:
                for chunk in r.iter_content(chunk_size=1 << 16):
                    if chunk:
                        fh.write(chunk)
            tmp.replace(target)

    # ----- indexing & serialization -----

    @abstractmethod
    def build_index(self) -> dict[str, object]:
        """Parse bulk files into ``{identifier: record}``."""

    def index(self) -> dict[str, object]:
        """Lazy, memoized accessor for the parsed index."""
        if self._index_cache is None:
            self._index_cache = self.build_index()
        return self._index_cache

    @abstractmethod
    def identifiers(self) -> Iterable[str]:
        """Yield every identifier this source can serialize."""

    @abstractmethod
    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        """Build the cache entry for one identifier."""

    # ----- cache file IO -----

    def write_cache_file(
        self,
        identifier: str,
        cache_dir: Path,
    ) -> Path:
        """Serialize ``identifier`` and write its cache file. Returns the path."""
        entry = self.serialize(identifier)
        cache_dir.mkdir(parents=True, exist_ok=True)
        path = cache_dir / entry.filename()
        text = entry.render()
        # Atomic write so partial files never appear under cache_dir
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(text, encoding="utf-8")
        tmp.replace(path)
        return path


def repin_manifest(
    manifest_path: Path,
    changes: Iterable[ChecksumChange],
    *,
    snapshot_date: str | None = None,
) -> list[str]:
    """Write accepted checksums back into a source manifest.

    Uses a ruamel round-trip load so the manifest's comments — which carry the
    licence, the provenance notes, and the bump procedure — survive the edit,
    and so the resulting git diff shows only the lines that actually changed.

    ``snapshot_date`` defaults to today (UTC): a new checksum means a new
    upstream release, so leaving the old date in place would misdescribe what
    the manifest now pins.

    Returns a human-readable description of each edit.
    """
    from ruamel.yaml import YAML

    by_name = {c.name: c for c in changes}
    if not by_name:
        return []

    yaml = YAML()
    yaml.preserve_quotes = True
    # Match the manifests' committed layout (two-space block sequences indented
    # under their key) so the diff shows only the checksum lines that changed.
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.width = 4096
    data = yaml.load(manifest_path)

    notes: list[str] = []
    for entry in data.get("bulk_files", []):
        change = by_name.get(entry.get("name"))
        if change is None:
            continue
        entry["sha256"] = change.new_sha256
        if "size_bytes" in entry or change.size_bytes:
            entry["size_bytes"] = change.size_bytes
        notes.append(
            f"{change.name}: {change.old_sha256[:12] or '(unpinned)'}"
            f" -> {change.new_sha256[:12]} ({change.size_bytes} bytes)"
        )

    if notes:
        new_date = snapshot_date or datetime.now(UTC).strftime("%Y-%m-%d")
        if data.get("snapshot_date") != new_date:
            notes.append(f"snapshot_date: {data.get('snapshot_date')} -> {new_date}")
            data["snapshot_date"] = new_date
        yaml.dump(data, manifest_path)

    return notes


def _sha256_of(path: Path, chunk_size: int = 1 << 16) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            chunk = fh.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def format_columns(
    rows: Iterable[Iterable[str]],
    widths: Iterable[int],
    sep: str = "  ",
) -> list[str]:
    """Format rows into fixed-width left-aligned columns.

    Used by serializers to keep the flat-file layout stable across refreshes
    so curator-quoted snippets keep matching.
    """
    widths = list(widths)
    out: list[str] = []
    for row in rows:
        cells = list(row)
        # Pad each but the last to its column width; last column unpadded.
        formatted = []
        for i, cell in enumerate(cells):
            if i < len(cells) - 1 and i < len(widths):
                formatted.append(cell.ljust(widths[i]))
            else:
                formatted.append(cell)
        out.append(sep.join(formatted).rstrip())
    return out
