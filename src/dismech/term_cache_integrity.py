"""Deterministic structural validation for the ontology term caches.

Issue #7682 showed that ``cache/<ontology>/terms.csv`` can be corrupted in a way
that is invisible to every other check in the repository, because the term cache
is treated as ontology truth by ``linkml-term-validator``. An ad-hoc seeding
script that builds a CSV row by string concatenation writes::

    MONDO:0012013,Weill-Marchesani syndrome 2, dominant,2026-08-01T04:30:00.000000

which is a *four*-field row: ``csv.reader`` reads the label as
``"Weill-Marchesani syndrome 2"`` and ``retrieved_at`` as ``" dominant"``. The
label has been silently truncated at the comma. The dangerous second stage is a
later "repair" pass that rewrites the malformed row as a well-formed three-field
row, cementing the truncated label as clean-looking data — from that point
``just validate-terms`` reports the truncation as ontology truth and validation
becomes circular. This check catches stage one, before the repair can hide it.

This module intentionally does *not* try to infer whether a cached label is the
*correct* label for its CURIE. That requires re-deriving from OAK/OLS and is
deliberately out of scope here (see #7682's proposed ``audit-term-cache-labels``
and #712). It validates only structural facts:

- the header row is exactly ``curie,label,retrieved_at``
- every data row parses to exactly three fields via ``csv.reader``
  (more than three is the stage-one truncation signature above)
- ``curie`` has a ``PREFIX:LOCALID`` shape, and its prefix matches the cache
  subdirectory it lives in (``cache/chebi/terms.csv`` holds only ``CHEBI:``
  rows) — an invariant every committed cache already satisfies, and the only
  thing that catches a row whose *prefix* was clobbered into another
  valid-looking shape (``BI:24996`` for ``CHEBI:24996``)
- ``label`` is non-empty
- ``retrieved_at`` is non-empty and an ISO-8601 date *and* time, matching what
  the validator's cache writer actually emits (a bare ``2026-08-02`` parses
  fine for :func:`datetime.fromisoformat` but is a truncation, not a write)
- no CURIE appears twice in one file — four of the eight corruptions found on
  ``main`` were duplicates in disguise, and a clobber that produced a
  valid-looking CURIE already present in the file would otherwise pass

The same treatment is applied to ``cache/enums/*.csv``, the dynamic-enum
membership caches, which stand in for an authority in exactly the same way:
``linkml-term-validator`` uses them as the positive-hit set for
``reachable_from``, so a clobbered CURIE there silently changes what passes
enum validation. They are single-column (``curie`` header, one CURIE per line)
and mixed-prefix by design, so they get the shape, duplicate, and field-count
checks but not the per-directory prefix invariant.

A correctly *quoted* label containing a comma is legitimate and must pass —
there are hundreds of them in the committed caches (MONDO's ``, dominant`` /
``, recessive`` / ``, type N`` naming conventions are the bulk of it), and they
are precisely the rows the concatenation bug can damage.

Sibling module: ``dismech.enum_cache`` owns the *semantic* half of ``cache/**``
— whether an enum cache row is still reachable from its enum's roots — plus the
canonical-ordering audit. This module owns the *structural* half. Keep new
cache checks in whichever of the two fits rather than adding a third scanner.

The heavier last line of defence remains the ``linkml-term-validator`` run
inside ``just validate-terms`` / ``just qc``.
"""

from __future__ import annotations

import csv
import re
import sys
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

EXPECTED_HEADER = ["curie", "label", "retrieved_at"]
EXPECTED_ENUM_HEADER = ["curie"]

# Deliberately permissive: the repo's caches carry both uppercase OBO-style
# prefixes (``HP:0001250``) and the lowercase ``hgnc:746`` form documented in
# CLAUDE.md. This checks the *shape* of a CURIE, not its prefix registration.
_CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._]*:[A-Za-z0-9_][A-Za-z0-9_.\-]*$")
# The cache writer emits a full date+time (``2026-08-02T02:08:16.455296``).
# ``datetime.fromisoformat`` alone would also accept a bare date, so require
# the time component explicitly — a lopped-off time is a truncation, not a
# legitimate write.
_TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}")


@dataclass(frozen=True)
class Finding:
    """A single term cache row (or header) that fails structural validation."""

    path: Path
    line: int
    curie: str
    reasons: tuple[str, ...]

    def format(self) -> str:
        bullet = "\n  - "
        return (
            f"{self.path}:{self.line}  ({self.curie})\n"
            f"  reasons:{bullet}{bullet.join(self.reasons)}"
        )


def _check_row(row: list[str], expected_prefix: str) -> list[str]:
    """Return structural problems with a single parsed data row."""
    if len(row) > len(EXPECTED_HEADER):
        # The signature described in #7682: a label containing a comma was
        # written without CSV quoting, so the label is truncated at the comma
        # and its tail has been shifted into `retrieved_at` (and beyond).
        return [
            (
                f"row parses to {len(row)} fields, expected 3 "
                "(unquoted comma in the label truncates it — see #7682); "
                f"fields: {row!r}"
            )
        ]
    if len(row) < len(EXPECTED_HEADER):
        return [f"row parses to {len(row)} fields, expected 3; fields: {row!r}"]

    curie, label, retrieved_at = row
    reasons: list[str] = []

    if not _CURIE_RE.match(curie):
        reasons.append(f"curie {curie!r} is not a PREFIX:LOCALID CURIE")
    elif curie.split(":", 1)[0].casefold() != expected_prefix.casefold():
        reasons.append(
            f"curie {curie!r} has prefix "
            f"{curie.split(':', 1)[0]!r}, expected {expected_prefix!r} "
            "to match the cache directory"
        )
    if not label.strip():
        reasons.append("label is empty")
    if not retrieved_at.strip():
        reasons.append("retrieved_at is empty")
    else:
        try:
            datetime.fromisoformat(retrieved_at)
        except ValueError:
            reasons.append(
                f"retrieved_at {retrieved_at!r} is not a parseable ISO-8601 timestamp"
            )
        else:
            if not _TIMESTAMP_RE.match(retrieved_at):
                reasons.append(
                    f"retrieved_at {retrieved_at!r} is missing its time component "
                    "(the cache writer always emits an ISO-8601 date and time)"
                )

    return reasons


def _check_enum_row(row: list[str]) -> list[str]:
    """Return structural problems with a single ``cache/enums/*.csv`` row."""
    if len(row) != len(EXPECTED_ENUM_HEADER):
        return [
            (
                f"row parses to {len(row)} fields, expected 1 "
                f"(enum membership caches are single-column); fields: {row!r}"
            )
        ]
    curie = row[0]
    if not _CURIE_RE.match(curie):
        return [f"curie {curie!r} is not a PREFIX:LOCALID CURIE"]
    return []


def _read_rows(path: Path) -> list[list[str]] | Finding:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.reader(handle))
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        return Finding(path=path, line=0, curie="", reasons=(f"unreadable: {exc}",))


def _scan_rows(
    path: Path,
    rows: list[list[str]],
    expected_header: list[str],
    row_checker: Callable[[list[str]], list[str]],
) -> list[Finding]:
    """Shared header / per-row / duplicate-CURIE scan for both cache shapes."""
    findings: list[Finding] = []

    if rows[0] != expected_header:
        findings.append(
            Finding(
                path=path,
                line=1,
                curie="",
                reasons=(
                    f"header must be {','.join(expected_header)}, got {rows[0]!r}",
                ),
            )
        )

    # Only skip the first line when it really is a header. A file whose header
    # is missing entirely would otherwise have its first *data* row silently
    # consumed as the header and never structurally checked.
    looks_like_header = bool(rows[0]) and rows[0][0].strip().casefold() == "curie"
    data_rows = rows[1:] if looks_like_header else rows
    first_line = 2 if looks_like_header else 1

    seen: dict[str, int] = {}
    for offset, row in enumerate(data_rows, start=first_line):
        if not row:
            # csv.reader yields [] only for a genuinely blank line; a trailing
            # newline at end of file does not produce one.
            findings.append(
                Finding(path=path, line=offset, curie="", reasons=("blank row",))
            )
            continue

        reasons = list(row_checker(row))

        key = row[0].casefold()
        if key in seen:
            reasons.append(
                f"duplicate curie {row[0]!r} (first seen on line {seen[key]})"
            )
        else:
            seen[key] = offset

        if reasons:
            findings.append(
                Finding(path=path, line=offset, curie=row[0], reasons=tuple(reasons))
            )

    return findings


def check_cache_file(path: Path, expected_prefix: str | None = None) -> list[Finding]:
    """Check one ``terms.csv`` against the deterministic structural contract.

    ``expected_prefix`` defaults to the name of the cache subdirectory holding
    the file, which is the convention every committed cache follows.
    """
    if expected_prefix is None:
        expected_prefix = path.parent.name

    rows = _read_rows(path)
    if isinstance(rows, Finding):
        return [rows]
    if not rows:
        return [Finding(path=path, line=0, curie="", reasons=("file is empty",))]

    return _scan_rows(
        path,
        rows,
        EXPECTED_HEADER,
        lambda row: _check_row(row, expected_prefix),
    )


def check_enum_cache_file(path: Path) -> list[Finding]:
    """Check one ``cache/enums/*.csv`` dynamic-enum membership cache.

    These are single-column and mixed-prefix by design, so they get the CURIE
    shape, field-count, and duplicate checks but not the per-directory prefix
    invariant that ``cache/<ontology>/terms.csv`` carries.
    """
    rows = _read_rows(path)
    if isinstance(rows, Finding):
        return [rows]
    if not rows:
        return [Finding(path=path, line=0, curie="", reasons=("file is empty",))]

    return _scan_rows(path, rows, EXPECTED_ENUM_HEADER, _check_enum_row)


def discover_cache_files(cache_dir: Path) -> tuple[list[Path], list[Path]]:
    """Return the (term cache, enum cache) files under ``cache_dir``.

    Single source of truth for what gets scanned, so the ``OK:`` coverage line
    can never disagree with what was actually checked. The ``enums`` exclusion
    keeps a hypothetical ``cache/enums/terms.csv`` from matching both globs and
    being scanned twice under two contradictory contracts.
    """
    term_caches = sorted(
        path for path in cache_dir.glob("*/terms.csv") if path.parent.name != "enums"
    )
    enum_caches = sorted((cache_dir / "enums").glob("*.csv"))
    return term_caches, enum_caches


def scan_cache_dir(cache_dir: Path) -> list[Finding]:
    """Scan every ontology term cache and dynamic-enum membership cache."""
    term_caches, enum_caches = discover_cache_files(cache_dir)
    findings: list[Finding] = []
    for path in term_caches:
        findings.extend(check_cache_file(path))
    for path in enum_caches:
        findings.extend(check_enum_cache_file(path))
    return findings


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    cache_dir = Path(args[0]) if args else Path("cache")
    if not cache_dir.is_dir():
        print(f"error: {cache_dir} is not a directory", file=sys.stderr)
        return 2

    term_caches, enum_caches = discover_cache_files(cache_dir)
    findings = scan_cache_dir(cache_dir)
    if not findings:
        print(
            f"OK: {len(term_caches)} term cache file(s) and {len(enum_caches)} "
            f"enum cache file(s) in {cache_dir} match the structural contract"
        )
        return 0

    print(
        f"FAIL: {len(findings)} cache integrity issue(s) found",
        file=sys.stderr,
    )
    for finding in findings:
        print(finding.format(), file=sys.stderr)
    print(
        "\nDo NOT hand-edit these caches. Delete the offending row and "
        "regenerate it with `just validate-terms <file>` (see #7682).",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
