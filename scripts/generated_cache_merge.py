"""Lossless, additive reconciliation of conflicted term and enum CSV blobs.

This module never fetches, reads, or writes a cache file. Its caller supplies
Git blobs and remains responsible for validating Git paths, modes, merge state,
and the final tree before publishing anything. Generated files outside the two
documented CSV shapes are deliberately unsupported.

Every surviving row comes from an input, unchanged as parsed CSV fields.
Deletions, edits (including timestamp edits), malformed input, and competing
rows for one CURIE require the shepherd's judgement; none are auto-resolved.
"""

from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path

# Reuse the repository's structural contract without installing the project or
# its ontology dependencies. This module and term_cache_integrity are stdlib-only.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from dismech.term_cache_integrity import (
    EXPECTED_ENUM_HEADER,
    EXPECTED_HEADER,
    _check_enum_row,
    _check_row,
)

_TERM_PATH = re.compile(r"cache/([A-Za-z][A-Za-z0-9._]*)/terms\.csv")
_ENUM_PATH = re.compile(r"cache/enums/[A-Za-z0-9][A-Za-z0-9_.-]*\.csv")


class UnsafeMerge(ValueError):
    """The input cannot be reconciled without choosing or discarding data."""


def is_supported_cache_path(path: str) -> bool:
    """Whether an exact repository-relative path has a supported CSV shape.

    This is a lexical allowlist, not a filesystem or Git-mode safety check.
    No normalization is performed: traversal, absolute paths, and backslashes
    must never become a supported path through normalization.
    """
    return bool(_ENUM_PATH.fullmatch(path) or _TERM_PATH.fullmatch(path))


def _check_quoting(text: str) -> None:
    """Reject bare quotes that even csv.reader(strict=True) accepts.

    Keep valid escaped quotes and quoted multiline labels; CSV reserialization
    must never turn an ambiguously malformed input into a clean-looking row.
    """
    state = "start"
    for character in text:
        if state == "quoted":
            if character == '"':
                state = "closed"
        elif state == "closed":
            if character == '"':
                state = "quoted"
            elif character in ",\r\n":
                state = "start"
            else:
                raise UnsafeMerge("unexpected character after closing CSV quote")
        elif character == '"':
            if state != "start":
                raise UnsafeMerge("bare quote in an unquoted CSV field")
            state = "quoted"
        elif character in ",\r\n":
            state = "start"
        else:
            state = "unquoted"
    if state == "quoted":
        raise UnsafeMerge("unterminated quoted CSV field")


def _parse(path: str, blob: bytes, side: str) -> dict[str, tuple[str, ...]]:
    """Validate an entire blob before permitting any reconciliation."""
    enum = path.startswith("cache/enums/")
    expected_header = EXPECTED_ENUM_HEADER if enum else EXPECTED_HEADER
    try:
        text = blob.decode("utf-8", errors="strict")
        if "\x00" in text:
            raise UnsafeMerge("NUL byte in CSV")
        _check_quoting(text)
        reader = csv.reader(io.StringIO(text, newline=""), strict=True)
        header = next(reader, None)
        if header != expected_header:
            raise UnsafeMerge(f"expected header {expected_header!r}, got {header!r}")
        rows: dict[str, tuple[str, ...]] = {}
        for row in reader:
            problems = (
                _check_enum_row(row) if enum else _check_row(row, path.split("/")[1])
            )
            # The shared check uses a regex ending in $, which also matches
            # before a final newline. Identifiers themselves must have no
            # whitespace, even inside an otherwise legal quoted CSV field.
            if row and any(character.isspace() for character in row[0]):
                problems.append("whitespace in CURIE")
            if problems:
                raise UnsafeMerge(f"line {reader.line_num}: {'; '.join(problems)}")
            key = row[0].casefold()
            if key in rows:
                raise UnsafeMerge(f"line {reader.line_num}: duplicate CURIE {row[0]!r}")
            rows[key] = tuple(row)
        return rows
    except (UnicodeDecodeError, csv.Error, UnsafeMerge) as error:
        raise UnsafeMerge(f"{path} ({side}): {error}") from error


def _serialize(header: list[str], rows: list[tuple[str, ...]]) -> bytes:
    """Write canonical LF record endings without changing quoted label text."""
    record = io.StringIO(newline="")
    # CRLF makes csv.writer quote labels containing either CR or LF. Strip
    # only each record's terminator; global newline replacement would alter a
    # multiline label, and a bare-LF writer need not quote embedded CRs.
    # All output records intentionally use LF, even for CRLF input, matching
    # the cache CSV invariant in .gitattributes; quoted field values stay intact.
    writer = csv.writer(record, lineterminator="\r\n")
    output: list[str] = []
    for row in [header, *rows]:
        record.seek(0)
        record.truncate(0)
        writer.writerow(row)
        output.append(record.getvalue()[:-2] + "\n")
    return "".join(output).encode("utf-8")


def merge_cache_csv(path: str, base: bytes | None, ours: bytes, theirs: bytes) -> bytes:
    """Return an additive union, or raise UnsafeMerge without side effects.

    ``base=None`` is allowed only for an add/add conflict whose ancestor has
    no file. Both tips must supply complete blobs. All ancestor rows must occur
    unchanged on both tips, and shared CURIEs must have identical fields,
    including their original timestamp. Case variants of one CURIE collide.

    Output uses the repository's codepoint CURIE sort and LF record endings;
    CSV quoting may be normalized, while every field value is preserved.
    """
    if not is_supported_cache_path(path):
        raise UnsafeMerge(f"unsupported cache path: {path!r}")
    ancestor = {} if base is None else _parse(path, base, "base")
    left = _parse(path, ours, "ours")
    right = _parse(path, theirs, "theirs")

    for side, rows in (("ours", left), ("theirs", right)):
        for key, row in ancestor.items():
            if key not in rows:
                raise UnsafeMerge(f"{path} ({side}): deleted ancestor CURIE {row[0]!r}")
            if rows[key] != row:
                raise UnsafeMerge(f"{path} ({side}): changed ancestor CURIE {row[0]!r}")

    merged = left.copy()
    for key, row in right.items():
        if key in merged and merged[key] != row:
            raise UnsafeMerge(f"{path}: competing rows for CURIE {row[0]!r}")
        merged[key] = row

    header = (
        EXPECTED_ENUM_HEADER if path.startswith("cache/enums/") else EXPECTED_HEADER
    )
    output = _serialize(header, sorted(merged.values(), key=lambda row: row[0]))
    # Guard the serialization boundary as well as the union: no source field
    # may disappear or change even for unusual but valid CSV quoting.
    if _parse(path, output, "result") != merged:
        raise UnsafeMerge(f"{path}: CSV round trip changed a source row")
    return output
