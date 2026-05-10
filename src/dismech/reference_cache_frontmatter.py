"""Deterministic validation for reference cache markdown frontmatter.

Issue #871 showed that a fabricated cache can defeat snippet validation when both
the cache file and the snippet are hallucinated together. The deterministic
local check we can enforce in this repository is narrower: every
``references_cache/*.md`` file must parse cleanly and match the cache contract
used by ``linkml-reference-validator``.

This module intentionally does *not* try to infer whether metadata "looks real".
It validates only structural facts:

- the YAML frontmatter is parseable and has no duplicate keys
- required cache fields are present and have the expected types
- optional fields match the shapes written by the upstream cache writer
- the filename matches the normalized ``reference_id``
- ``PMID:`` caches carry at least one of ``authors`` / ``journal`` (issue
  #1737 defense-in-depth — the documented fabrication fingerprint had
  neither field populated)

The heavier last line of defence remains the existing
``linkml-reference-validator`` run inside ``just qc``.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError
from ruamel.yaml import YAML

_YAML = YAML(typ="safe")
_YAML.allow_duplicate_keys = False


class SupplementaryFileFrontmatter(BaseModel):
    """Shape written for supplementary files in cache frontmatter."""

    model_config = ConfigDict(extra="forbid")

    filename: str
    download_url: str | None = None
    content_type: str | None = None
    size_bytes: int | None = None
    checksum: str | None = None
    description: str | None = None
    local_path: str | None = None


class ReferenceCacheFrontmatter(BaseModel):
    """Frontmatter fields written by ``ReferenceFetcher._save_to_disk``."""

    model_config = ConfigDict(extra="forbid")

    reference_id: str
    content_type: str
    title: str | None = None
    authors: list[Any] | str | None = None
    journal: str | None = None
    year: str | int | None = None
    doi: str | None = None
    keywords: list[Any] | str | None = None
    extra_fields_captured: list[Any] | str | None = None
    supplementary_files: list[SupplementaryFileFrontmatter] | None = None
    # Local extension (dismech): identifies the source database for cache
    # files derived from a structured knowledge base (Orphanet, OMIM, MONDO,
    # …) rather than from a literature reference. The upstream
    # ``linkml-reference-validator`` loader silently ignores this field at
    # read time; an upstream FR is tracked to mirror it on
    # ``ReferenceContent``.
    database: str | None = None


@dataclass(frozen=True)
class Finding:
    """A single cache file that fails deterministic validation."""

    path: Path
    reference_id: str
    reasons: tuple[str, ...]

    def format(self) -> str:
        bullet = "\n  - "
        return (
            f"{self.path}  ({self.reference_id})\n"
            f"  reasons:{bullet}{bullet.join(self.reasons)}"
        )


def _extract_frontmatter_text(path: Path) -> str | None:
    """Return the YAML frontmatter slice of a markdown file, or ``None``."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def _load_frontmatter(path: Path) -> dict[str, Any]:
    frontmatter = _extract_frontmatter_text(path)
    if frontmatter is None:
        raise ValueError("missing markdown frontmatter")

    data = _YAML.load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data


def _validate_contract(path: Path, data: dict[str, Any]) -> list[str]:
    try:
        frontmatter = ReferenceCacheFrontmatter.model_validate(data)
    except ValidationError as exc:
        return [
            f"{'.'.join(str(part) for part in err['loc'])}: {err['msg']}"
            for err in exc.errors()
        ]

    reasons: list[str] = []
    expected_name = (
        frontmatter.reference_id.replace(":", "_")
        .replace("/", "_")
        .replace("?", "_")
        .replace("=", "_")
        + ".md"
    )
    matches_filename = path.name == expected_name
    # DOI identifiers are case-insensitive in practice, and the tracked cache
    # corpus contains mixed-case DOI filenames. Match those names
    # case-insensitively so Linux CI agrees with the repo's existing files.
    if frontmatter.reference_id.startswith("DOI:"):
        matches_filename = path.name.casefold() == expected_name.casefold()
    if not matches_filename:
        reasons.append(f"filename must match reference_id ({expected_name})")

    # Defense-in-depth check for the fabrication fingerprint documented in
    # issue #1737: hand-crafted PMID cache files lacking real bibliographic
    # metadata (no authors, no journal) where the body content was just the
    # YAML snippet copy-pasted back, defeating the snippet-substring check
    # in linkml-reference-validator. All legitimate PMID caches in the
    # current corpus carry at least one of authors / journal — including
    # pre-abstract-era papers, foreign-language abstracts, and minimal
    # PubMed records.
    if frontmatter.reference_id.startswith("PMID:") and not (
        frontmatter.authors or frontmatter.journal
    ):
        reasons.append(
            "PMID cache files must carry at least one of `authors:` or "
            "`journal:` (fabrication fingerprint per #1737)"
        )

    return reasons


def check_cache_file(path: Path) -> Finding | None:
    """Check a single cache file against the deterministic frontmatter contract."""
    try:
        data = _load_frontmatter(path)
    except Exception as exc:
        return Finding(
            path=path,
            reference_id=path.stem,
            reasons=(f"invalid YAML frontmatter: {exc}",),
        )

    reasons = _validate_contract(path, data)
    if not reasons:
        return None

    return Finding(
        path=path,
        reference_id=str(data.get("reference_id", path.stem)),
        reasons=tuple(reasons),
    )


def scan_cache_dir(cache_dir: Path) -> list[Finding]:
    """Scan a directory of reference cache markdown files."""
    findings: list[Finding] = []
    for path in sorted(cache_dir.glob("*.md")):
        finding = check_cache_file(path)
        if finding is not None:
            findings.append(finding)
    return findings


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    cache_dir = Path(args[0]) if args else Path("references_cache")
    if not cache_dir.is_dir():
        print(f"error: {cache_dir} is not a directory", file=sys.stderr)
        return 2

    findings = scan_cache_dir(cache_dir)
    if not findings:
        print(f"OK: reference cache frontmatter matches the contract in {cache_dir}")
        return 0

    print(
        f"FAIL: {len(findings)} reference cache file(s) failed deterministic checks",
        file=sys.stderr,
    )
    for finding in findings:
        print(finding.format(), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
