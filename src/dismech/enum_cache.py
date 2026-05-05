"""Integrity checks for cached dynamic enum membership CSVs.

``linkml-term-validator`` uses ``cache/enums/*.csv`` as a positive-hit cache
for dynamic enum membership. That makes corrupted rows dangerous: a bad CURIE
present in an enum cache can be accepted before the validator asks OAK whether
the CURIE is actually reachable from the enum's current roots.

This module verifies that every tracked enum cache row still belongs to the
current schema enum, with enum cache reads disabled during the check.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path

from linkml_runtime.linkml_model import EnumDefinition
from linkml_runtime.utils.schemaview import SchemaView
from linkml_term_validator.plugins import BindingValidationPlugin


@dataclass(frozen=True)
class EnumCacheFinding:
    """A single enum cache integrity problem."""

    path: Path
    enum_name: str
    reason: str
    curie: str | None = None

    def format(self) -> str:
        detail = f": {self.curie}" if self.curie else ""
        return f"{self.path} ({self.enum_name}) {self.reason}{detail}"


@dataclass(frozen=True)
class CurrentEnumCache:
    """Current schema enum plus its expected cache path."""

    enum_name: str
    enum_def: EnumDefinition
    path: Path


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
        cache_key = plugin._get_enum_cache_key(enum_def)  # noqa: SLF001
        path = plugin._get_enum_cache_file(enum_name, cache_key)  # noqa: SLF001
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
) -> list[EnumCacheFinding]:
    """Scan enum cache files for stale files, duplicate rows, and invalid rows."""

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
    checker = _checking_plugin(cache_dir, oak_config)
    findings: list[EnumCacheFinding] = []

    for path in sorted(enum_dir.glob("*.csv")):
        current = expected.get(path.name)
        if current is None:
            findings.append(
                EnumCacheFinding(
                    path=path, enum_name="unknown", reason="stale enum cache file"
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

            if not checker.is_value_in_enum(curie, current.enum_def, schema_view):
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
            for curie in sorted(valid_rows):
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
        "--max-findings",
        type=int,
        default=50,
        help="Maximum findings to print before truncating output",
    )
    args = parser.parse_args(argv)

    oak_config = args.oak_config if args.oak_config.exists() else None
    findings = (
        repair_enum_cache_dir(args.schema, args.cache_dir, oak_config)
        if args.fix
        else scan_enum_cache_dir(args.schema, args.cache_dir, oak_config)
    )

    if not findings:
        print(
            f"OK: enum cache rows match current dynamic enum definitions in {args.cache_dir}"
        )
        return 0

    action = "repaired" if args.fix else "failed"
    print(
        f"Enum cache integrity {action}: {len(findings)} finding(s)",
        file=sys.stderr,
    )
    for finding in findings[: args.max_findings]:
        print(f"  - {finding.format()}", file=sys.stderr)
    if len(findings) > args.max_findings:
        print(f"  ... {len(findings) - args.max_findings} more", file=sys.stderr)

    return 0 if args.fix else 1


if __name__ == "__main__":
    raise SystemExit(main())
