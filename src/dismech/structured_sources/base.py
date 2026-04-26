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
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Iterable, Optional

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
        self._index_cache: Optional[dict[str, object]] = None

    # ----- bulk data -----

    def refresh(self, *, force: bool = False) -> None:
        """Download bulk files into ``data_dir``, verifying sha256.

        Existing files with matching checksum are kept; mismatches re-download.
        """
        self.data_dir.mkdir(parents=True, exist_ok=True)
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
                raise RuntimeError(
                    f"checksum mismatch for {bf.name} after download: "
                    f"got {actual}, expected {bf.sha256}"
                )

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
