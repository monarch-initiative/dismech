"""Integrity checks for cached dynamic enum membership CSVs.

``linkml-term-validator`` uses ``cache/enums/*.csv`` as a positive-hit cache
for dynamic enum membership. That makes corrupted rows dangerous: a bad CURIE
present in an enum cache can be accepted before the validator asks OAK whether
the CURIE is actually reachable from the enum's current roots.

This module verifies that every tracked enum cache row still belongs to the
current schema enum, with enum cache reads disabled during the check.  It also
provides a read-only ordering audit for both enum membership and ontology term
caches.

Sibling module: ``dismech.term_cache_integrity`` owns the *structural* half of
``cache/**`` — CSV field counts, CURIE shape, label/timestamp well-formedness,
duplicate CURIEs — for both ``cache/<ontology>/terms.csv`` and
``cache/enums/*.csv``. This module owns the *semantic* half (membership,
reachability) plus ordering. Keep new cache checks in whichever of the two
fits rather than adding a third scanner.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from linkml_runtime.linkml_model import EnumDefinition
from linkml_runtime.utils.schemaview import SchemaView
from linkml_term_validator.plugins import BindingValidationPlugin


@dataclass(frozen=True)
class EnumCacheFinding:
    """A single enum cache integrity problem.

    ``is_warning`` is True for findings that are advisory during the current
    migration: stale filenames and non-canonical row order.  Warnings do **not**
    fail CI.  All other findings (malformed headers, duplicate rows, invalid
    CURIEs) are errors and do fail CI.
    """

    path: Path
    enum_name: str
    reason: str
    curie: str | None = None
    is_warning: bool = False

    def format(self) -> str:
        detail = f": {self.curie}" if self.curie else ""
        level = "WARNING" if self.is_warning else "ERROR"
        return f"[{level}] {self.path} ({self.enum_name}) {self.reason}{detail}"


@dataclass(frozen=True)
class CurrentEnumCache:
    """Current schema enum plus its expected cache path."""

    enum_name: str
    enum_def: EnumDefinition
    path: Path


@dataclass(frozen=True)
class CacheOrderFinding:
    """The first descending CURIE pair in a cache CSV."""

    path: Path
    row_count: int
    sorted_through: int
    first_bad_curie: str
    previous_curie: str

    @property
    def tail_size(self) -> int:
        """Count every row after the first inversion, not only misplaced rows."""

        return self.row_count - self.sorted_through

    def format(self) -> str:
        return (
            f"{self.path}: sorted through row {self.sorted_through} of "
            f"{self.row_count}; out-of-order tail {self.tail_size}; first bad "
            f"CURIE {self.first_bad_curie!r} follows {self.previous_curie!r}"
        )


@dataclass(frozen=True)
class CacheOrderReadFinding:
    """A cache CSV that could not be inspected for canonical ordering."""

    path: Path
    reason: str

    def format(self) -> str:
        return f"{self.path}: {self.reason}"


def canonical_curie_rows(rows: Iterable[str]) -> list[str]:
    """Return the canonical enum-cache body (C/codepoint order, deduplicated)."""

    return sorted(set(rows))


def _cache_order_finding(path: Path, rows: list[str]) -> CacheOrderFinding | None:
    """Return the first ordering inversion, or ``None`` when rows are sorted."""

    for index in range(1, len(rows)):
        if rows[index] < rows[index - 1]:
            return CacheOrderFinding(
                path=path,
                row_count=len(rows),
                sorted_through=index,
                first_bad_curie=rows[index],
                previous_curie=rows[index - 1],
            )
    return None


def _read_first_column(path: Path) -> list[str]:
    """Read non-empty CURIE values from the first column of a cache CSV."""

    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.reader(stream)
        header = next(reader, None)
        if not header or header[0] != "curie":
            raise ValueError(
                f"expected first CSV column to be 'curie', found {header!r}"
            )
        return [row[0] for row in reader if row and row[0]]


def scan_cache_order(
    cache_dir: Path,
) -> list[CacheOrderFinding | CacheOrderReadFinding]:
    """Audit canonical CURIE order without modifying caches or consulting OAK."""

    paths = sorted((cache_dir / "enums").glob("*.csv"))
    paths.extend(sorted(cache_dir.glob("*/terms.csv")))
    findings: list[CacheOrderFinding | CacheOrderReadFinding] = []
    for path in paths:
        try:
            rows = _read_first_column(path)
        except (OSError, csv.Error, UnicodeError, ValueError) as error:
            findings.append(CacheOrderReadFinding(path=path, reason=str(error)))
            continue
        finding = _cache_order_finding(path, rows)
        if finding is not None:
            findings.append(finding)
    return findings


def _naming_plugin(cache_dir: Path, oak_config: Path | None) -> BindingValidationPlugin:
    return BindingValidationPlugin(cache_dir=cache_dir, oak_config_path=oak_config)


def _checking_plugin(
    cache_dir: Path, oak_config: Path | None
) -> BindingValidationPlugin:
    return BindingValidationPlugin(
        cache_labels=False,
        cache_enum_expansions=False,
        cache_dir=cache_dir,
        oak_config_path=oak_config,
    )


def current_enum_caches(
    schema_path: Path,
    cache_dir: Path,
    oak_config: Path | None,
) -> dict[str, CurrentEnumCache]:
    """Return expected dynamic enum cache files for the current schema."""

    schema_view = SchemaView(str(schema_path))
    plugin = _naming_plugin(cache_dir, oak_config)
    expected: dict[str, CurrentEnumCache] = {}

    for enum_name, enum_def in schema_view.all_enums().items():
        if not plugin.is_dynamic_enum(enum_def):
            continue
        cache_key = plugin._get_enum_cache_key(enum_def)
        path = plugin._get_enum_cache_file(enum_name, cache_key)
        expected[path.name] = CurrentEnumCache(enum_name, enum_def, path)

    return expected


def _read_curie_rows(path: Path) -> tuple[list[str], list[EnumCacheFinding]]:
    findings: list[EnumCacheFinding] = []
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["curie"]:
            return [], [
                EnumCacheFinding(
                    path=path,
                    enum_name="unknown",
                    reason=f"expected CSV header ['curie'], found {reader.fieldnames!r}",
                )
            ]
        return [row["curie"] for row in reader if row.get("curie")], findings


def scan_enum_cache_dir(
    schema_path: Path,
    cache_dir: Path,
    oak_config: Path | None,
    offline: bool = False,
    strict_order: bool = False,
) -> list[EnumCacheFinding]:
    """Scan enum caches for stale files, ordering, duplicates, and invalid rows.

    When ``offline`` is true the per-CURIE membership re-derivation
    (``is_value_in_enum``, which asks OAK to expand the enum and can trigger
    multi-GB ``sqlite:obo:*`` downloads) is skipped. The structural checks that
    need no ontology access — stale-file detection, malformed headers,
    duplicate rows, and canonical ordering — still run. Use this in network-
    or disk-constrained environments where the committed ``cache/*.csv`` is
    trusted. Ordering is warning-only unless ``strict_order`` is true; that
    switch is the Phase 2 hook for promoting the invariant to a hard gate.
    """

    enum_dir = cache_dir / "enums"
    if not enum_dir.is_dir():
        return [
            EnumCacheFinding(
                path=enum_dir,
                enum_name="unknown",
                reason="enum cache directory does not exist",
            )
        ]

    schema_view = SchemaView(str(schema_path))
    expected = current_enum_caches(schema_path, cache_dir, oak_config)
    checker = None if offline else _checking_plugin(cache_dir, oak_config)
    findings: list[EnumCacheFinding] = []

    for path in sorted(enum_dir.glob("*.csv")):
        current = expected.get(path.name)
        if current is None:
            findings.append(
                EnumCacheFinding(
                    path=path,
                    enum_name="unknown",
                    reason="stale enum cache file",
                    is_warning=True,
                )
            )
            continue

        rows, row_findings = _read_curie_rows(path)
        if row_findings:
            findings.extend(
                EnumCacheFinding(
                    path=f.path, enum_name=current.enum_name, reason=f.reason
                )
                for f in row_findings
            )
            continue

        order_finding = _cache_order_finding(path, rows)
        if order_finding is not None:
            findings.append(
                EnumCacheFinding(
                    path=path,
                    enum_name=current.enum_name,
                    reason=(
                        "rows are not in canonical order "
                        f"(sorted through row {order_finding.sorted_through}; "
                        f"out-of-order tail {order_finding.tail_size}; "
                        f"previous CURIE {order_finding.previous_curie!r})"
                    ),
                    curie=order_finding.first_bad_curie,
                    is_warning=not strict_order,
                )
            )

        seen: set[str] = set()
        for curie in rows:
            if curie in seen:
                findings.append(
                    EnumCacheFinding(
                        path=path,
                        enum_name=current.enum_name,
                        reason="duplicate cached CURIE",
                        curie=curie,
                    )
                )
                continue
            seen.add(curie)

            if checker is not None and not checker.is_value_in_enum(
                curie, current.enum_def, schema_view
            ):
                findings.append(
                    EnumCacheFinding(
                        path=path,
                        enum_name=current.enum_name,
                        reason="cached CURIE is not valid for current enum",
                        curie=curie,
                    )
                )

    return findings


def repair_enum_cache_dir(
    schema_path: Path,
    cache_dir: Path,
    oak_config: Path | None,
) -> list[EnumCacheFinding]:
    """Remove stale enum cache files and invalid/duplicate rows from current files."""

    enum_dir = cache_dir / "enums"
    enum_dir.mkdir(parents=True, exist_ok=True)

    schema_view = SchemaView(str(schema_path))
    expected = current_enum_caches(schema_path, cache_dir, oak_config)
    checker = _checking_plugin(cache_dir, oak_config)
    findings: list[EnumCacheFinding] = []

    for path in sorted(enum_dir.glob("*.csv")):
        current = expected.get(path.name)
        if current is None:
            findings.append(
                EnumCacheFinding(
                    path=path,
                    enum_name="unknown",
                    reason="removed stale enum cache file",
                )
            )
            path.unlink()
            continue

        rows, row_findings = _read_curie_rows(path)
        if row_findings:
            findings.extend(
                EnumCacheFinding(
                    path=f.path,
                    enum_name=current.enum_name,
                    reason=f"rewrote malformed enum cache file: {f.reason}",
                )
                for f in row_findings
            )
            with path.open("w", newline="", encoding="utf-8") as stream:
                writer = csv.DictWriter(
                    stream, fieldnames=["curie"], lineterminator="\n"
                )
                writer.writeheader()
            continue

        valid_rows: set[str] = set()
        for curie in rows:
            if curie in valid_rows:
                findings.append(
                    EnumCacheFinding(
                        path=path,
                        enum_name=current.enum_name,
                        reason="removed duplicate cached CURIE",
                        curie=curie,
                    )
                )
                continue

            if checker.is_value_in_enum(curie, current.enum_def, schema_view):
                valid_rows.add(curie)
            else:
                findings.append(
                    EnumCacheFinding(
                        path=path,
                        enum_name=current.enum_name,
                        reason="removed invalid cached CURIE",
                        curie=curie,
                    )
                )

        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=["curie"], lineterminator="\n")
            writer.writeheader()
            for curie in canonical_curie_rows(valid_rows):
                writer.writerow({"curie": curie})

    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--schema", type=Path, default=Path("src/dismech/schema/dismech.yaml")
    )
    parser.add_argument("--cache-dir", type=Path, default=Path("cache"))
    parser.add_argument("--oak-config", type=Path, default=Path("conf/oak_config.yaml"))
    parser.add_argument(
        "--fix", action="store_true", help="Repair cache files in place"
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help=(
            "Skip the OAK-backed membership re-derivation (which can trigger "
            "multi-GB sqlite:obo:* downloads) and run only the structural checks "
            "(stale files, malformed headers, duplicate rows, ordering) that "
            "trust the committed cache. Incompatible with --fix."
        ),
    )
    parser.add_argument(
        "--check-order",
        action="store_true",
        help=(
            "Read-only ordering audit for cache/enums/*.csv and "
            "cache/*/terms.csv; does not load the schema or consult OAK"
        ),
    )
    parser.add_argument(
        "--strict-order",
        action="store_true",
        help=(
            "Promote out-of-order rows from warnings to errors. Reserved for "
            "the coordinated cache-order cutover."
        ),
    )
    parser.add_argument(
        "--max-findings",
        type=int,
        default=50,
        help="Maximum findings to print before truncating output",
    )
    args = parser.parse_args(argv)

    if args.offline and args.fix:
        parser.error("--offline cannot be combined with --fix (repair needs OAK)")
    if args.check_order and args.fix:
        parser.error("--check-order cannot be combined with --fix")

    if args.check_order:
        order_findings = scan_cache_order(args.cache_dir)
        if not order_findings:
            print(f"OK: cache CSV rows are in canonical order in {args.cache_dir}")
            return 0
        print(
            f"Cache order: {len(order_findings)} file(s) have non-canonical ordering:",
            file=sys.stderr,
        )
        for finding in order_findings[: args.max_findings]:
            level = (
                "ERROR"
                if args.strict_order and isinstance(finding, CacheOrderFinding)
                else "WARNING"
            )
            print(f"  - [{level}] {finding.format()}", file=sys.stderr)
        if len(order_findings) > args.max_findings:
            print(
                f"  ... {len(order_findings) - args.max_findings} more",
                file=sys.stderr,
            )
        print(
            "  Advisory only; run 'just normalize-cache' during the coordinated "
            "cache-order cutover.",
            file=sys.stderr,
        )
        has_order_error = any(
            isinstance(finding, CacheOrderFinding) for finding in order_findings
        )
        return 1 if args.strict_order and has_order_error else 0

    oak_config = args.oak_config if args.oak_config.exists() else None
    findings = (
        repair_enum_cache_dir(args.schema, args.cache_dir, oak_config)
        if args.fix
        else scan_enum_cache_dir(
            args.schema,
            args.cache_dir,
            oak_config,
            offline=args.offline,
            strict_order=args.strict_order,
        )
    )

    if not findings:
        note = " (offline: membership re-derivation skipped)" if args.offline else ""
        print(
            f"OK: enum cache rows match current dynamic enum definitions in "
            f"{args.cache_dir}{note}"
        )
        return 0

    if args.fix:
        print(
            f"Enum cache integrity repaired: {len(findings)} finding(s)",
            file=sys.stderr,
        )
        for finding in findings[: args.max_findings]:
            print(f"  - {finding.format()}", file=sys.stderr)
        if len(findings) > args.max_findings:
            print(f"  ... {len(findings) - args.max_findings} more", file=sys.stderr)
        return 0

    warnings = [f for f in findings if f.is_warning]
    errors = [f for f in findings if not f.is_warning]

    if warnings:
        print(
            f"Enum cache: {len(warnings)} warning(s) found:",
            file=sys.stderr,
        )
        for finding in warnings[: args.max_findings]:
            print(f"  - {finding.format()}", file=sys.stderr)
        if len(warnings) > args.max_findings:
            print(f"  ... {len(warnings) - args.max_findings} more", file=sys.stderr)
        print(
            "  Remediation: use 'just check-enum-cache --fix' for stale files; "
            "use 'just normalize-cache' for ordering during the coordinated cutover.",
            file=sys.stderr,
        )

    if errors:
        print(
            f"Enum cache integrity failed: {len(errors)} error(s)",
            file=sys.stderr,
        )
        for finding in errors[: args.max_findings]:
            print(f"  - {finding.format()}", file=sys.stderr)
        if len(errors) > args.max_findings:
            print(f"  ... {len(errors) - args.max_findings} more", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
