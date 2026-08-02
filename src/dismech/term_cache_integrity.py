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
- ``retrieved_at`` is non-empty and a parseable ISO-8601 timestamp

A correctly *quoted* label containing a comma is legitimate and must pass —
there are hundreds of them in the committed caches (MONDO's ``, dominant`` /
``, recessive`` / ``, type N`` naming conventions are the bulk of it), and they
are precisely the rows the concatenation bug can damage.

The heavier last line of defence remains the ``linkml-term-validator`` run
inside ``just validate-terms`` / ``just qc``.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

EXPECTED_HEADER = ["curie", "label", "retrieved_at"]

# Deliberately permissive: the repo's caches carry both uppercase OBO-style
# prefixes (``HP:0001250``) and the lowercase ``hgnc:746`` form documented in
# CLAUDE.md. This checks the *shape* of a CURIE, not its prefix registration.
_CURIE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._]*:[A-Za-z0-9_][A-Za-z0-9_.\-]*$")


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
            f"row parses to {len(row)} fields, expected 3 "
            "(unquoted comma in the label truncates it — see #7682); "
            f"fields: {row!r}"
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

    return reasons


def check_cache_file(path: Path, expected_prefix: str | None = None) -> list[Finding]:
    """Check one ``terms.csv`` against the deterministic structural contract.

    ``expected_prefix`` defaults to the name of the cache subdirectory holding
    the file, which is the convention every committed cache follows.
    """
    if expected_prefix is None:
        expected_prefix = path.parent.name
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        return [Finding(path=path, line=0, curie="", reasons=(f"unreadable: {exc}",))]

    if not rows:
        return [Finding(path=path, line=0, curie="", reasons=("file is empty",))]

    findings: list[Finding] = []
    if rows[0] != EXPECTED_HEADER:
        findings.append(
            Finding(
                path=path,
                line=1,
                curie="",
                reasons=(
                    f"header must be {','.join(EXPECTED_HEADER)}, got {rows[0]!r}",
                ),
            )
        )

    for offset, row in enumerate(rows[1:], start=2):
        if not row:
            # csv.reader yields [] only for a genuinely blank line; a trailing
            # newline at end of file does not produce one.
            findings.append(
                Finding(path=path, line=offset, curie="", reasons=("blank row",))
            )
            continue
        reasons = _check_row(row, expected_prefix)
        if reasons:
            findings.append(
                Finding(
                    path=path,
                    line=offset,
                    curie=row[0],
                    reasons=tuple(reasons),
                )
            )

    return findings


def scan_cache_dir(cache_dir: Path) -> list[Finding]:
    """Scan every ``cache/<ontology>/terms.csv`` under ``cache_dir``."""
    findings: list[Finding] = []
    for path in sorted(cache_dir.glob("*/terms.csv")):
        findings.extend(check_cache_file(path))
    return findings


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    cache_dir = Path(args[0]) if args else Path("cache")
    if not cache_dir.is_dir():
        print(f"error: {cache_dir} is not a directory", file=sys.stderr)
        return 2

    paths = sorted(cache_dir.glob("*/terms.csv"))
    findings = scan_cache_dir(cache_dir)
    if not findings:
        print(
            f"OK: {len(paths)} term cache file(s) in {cache_dir} match the "
            "structural contract"
        )
        return 0

    print(
        f"FAIL: {len(findings)} term cache row(s) failed deterministic checks",
        file=sys.stderr,
    )
    for finding in findings:
        print(finding.format(), file=sys.stderr)
    print(
        "\nDo NOT hand-edit cache/*/terms.csv. Delete the offending row and "
        "regenerate it with `just validate-terms <file>` (see #7682).",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
