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
  neither field populated), *except* genuine NCBI Bookshelf records
  (LiverTox, GeneReviews, StatPearls, …) which efetch renders as a book
  citation carrying neither field

The heavier last line of defence remains the existing
``linkml-reference-validator`` run inside ``just qc``.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError
from ruamel.yaml import YAML

from dismech.frontmatter import naive_frontmatter_text, split_frontmatter

_YAML = YAML(typ="safe")
_YAML.allow_duplicate_keys = False
# NCBI Bookshelf records (LiverTox, GeneReviews, StatPearls, …) are real
# PubMed-indexed references that legitimately carry neither ``authors:`` nor
# ``journal:``: efetch renders them as a book citation, not a journal article.
# The "[Internet]." token is the distinctive Bookshelf citation marker and
# does not appear in journal abstracts, so we use it to exempt these records
# from the #1737 fabrication-fingerprint check. Re-fetching such a record
# reproduces the same file byte-for-byte, the ground-truth signal that it is
# not a hand-crafted fabrication.
_NCBI_BOOKSHELF_RE = re.compile(r"\[Internet\]\.")
# Agency / society clinical-practice-guideline monographs are PubMed-indexed
# references that, like NCBI Bookshelf books, legitimately carry neither
# ``authors:`` nor ``journal:``: efetch renders them as an agency
# monograph/report citation, not a journal article. This pattern matches the
# NICE-style NCBI collection line ``<Issuing body>: Guidelines.`` (e.g.
# "National Institute for Health and Care Excellence: Guidelines."); that marker
# does not appear in journal abstracts and reproduces byte-for-byte on re-fetch,
# the same ground-truth signal used for the Bookshelf exemption. It intentionally
# does NOT match other agency collection formats yet (e.g. WHO's "... Guidelines
# Review Committee.") — a false negative only *tightens* the check (the record
# still needs authors/journal), so those can be added if/when such a record
# trips the contract. See issue #6607 (PMID:31909928, a NICE guideline, was a
# false-positive fabrication flag).
_AGENCY_GUIDELINE_RE = re.compile(r"(?m)^.{2,120}:[ \t]*Guidelines\.[ \t]*$")


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
    # Preprint / full-text fields written by linkml-reference-validator
    # >=0.2.1rc2 (preprint support + Europe PMC full-text route). Present on
    # records the fetcher attempted full text for; absent on older cache files.
    is_preprint: bool | None = None
    peer_review_status: str | None = None
    full_text_attempted: bool | None = None
    full_text_provider: str | None = None
    full_text_url: str | None = None
    oa_status: str | None = None
    license: str | None = None
    local_pdf_path: str | None = None
    # PubMed publication types, written by linkml-reference-validator >=0.2.1
    # (the final release; the 0.2.1rc2 this repo previously pinned did not emit
    # it). Absent on every cache file fetched before that bump, so it stays
    # optional rather than becoming a required contract field.
    publication_types: list[Any] | str | None = None
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
    split = split_frontmatter(path.read_text(encoding="utf-8"))
    if split is None:
        return None
    return split.frontmatter


def _load_frontmatter(path: Path) -> dict[str, Any]:
    frontmatter = _extract_frontmatter_text(path)
    if frontmatter is None:
        raise ValueError("missing markdown frontmatter")

    data = _YAML.load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data


def _looks_like_ncbi_bookshelf(text: str) -> bool:
    """True if the cache body is an NCBI Bookshelf book citation."""
    return _NCBI_BOOKSHELF_RE.search(text) is not None


def _looks_like_agency_guideline(text: str) -> bool:
    """True if the cache body is an agency/society clinical-guideline monograph."""
    return _AGENCY_GUIDELINE_RE.search(text) is not None


def _validate_contract(
    path: Path, data: dict[str, Any], *, is_monograph: bool = False
) -> list[str]:
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
    # PubMed records. Genuine NCBI Bookshelf records and agency/society
    # clinical-guideline monographs (``is_monograph``) are legitimate
    # exceptions and are exempted (see #1737, #6607).
    if (
        frontmatter.reference_id.startswith("PMID:")
        and not is_monograph
        and not (frontmatter.authors or frontmatter.journal)
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

    try:
        body = path.read_text(encoding="utf-8")
        is_monograph = _looks_like_ncbi_bookshelf(body) or _looks_like_agency_guideline(
            body
        )
    except OSError:
        is_monograph = False
    reasons = _validate_contract(path, data, is_monograph=is_monograph)
    if not reasons:
        return None

    return Finding(
        path=path,
        reference_id=str(data.get("reference_id", path.stem)),
        reasons=tuple(reasons),
    )


def check_consumer_compatibility(path: Path) -> Finding | None:
    """Advisory: does a delimiter-unaware consumer read this file differently?

    This is deliberately *not* part of the gating contract. The contract above is
    correct — a ``---`` inside a title does not close the frontmatter, and
    ``test_check_cache_file_allows_inline_triple_hyphen_sequence`` asserts exactly
    that on purpose. The problem is that consumers which split on the ``---``
    *substring* rather than the ``---`` *line* disagree, and the pinned
    ``linkml-reference-validator`` is one of them (issue #7697): depending on
    whether the emitter quoted the title, such a file either crashes the
    validation run or silently loses its title and every field after it.

    ``dismech.patch_reference_validator`` repairs the read side for anything
    routed through ``scripts/run_reference_validator.sh``, so these files are
    readable *here*. They remain a hazard for a bare ``linkml-reference-validator``
    invocation, and the emitter's quoting is not stable across versions (#7393,
    #7523) — a file that is silently degraded today can crash tomorrow. Hence:
    report, do not gate.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:  # pragma: no cover - unreadable cache file
        return None

    split = split_frontmatter(text)
    if split is None:
        return None

    # A block with no literal '---' inside it is read identically by a
    # delimiter-unaware consumer *by construction*: the second occurrence of
    # '---' in the file then is the closing delimiter, so both readings select
    # the same text. Skipping the two YAML parses here takes the scan over the
    # 33k-file corpus from ~68s to ~1.5s with identical output, which matters
    # because this is the first dependency of `just qc`. Mirrors the guard in
    # patch_reference_validator._wrap_load_markdown_format.
    if "---" not in split.frontmatter:
        return None

    naive = naive_frontmatter_text(text)
    if naive is None:
        return None

    try:
        strict_data = _YAML.load(split.frontmatter)
    except Exception:  # pragma: no cover - the gating check reports this already
        return None

    # Compare what each consumer actually *sees*, not the raw slices: the naive
    # split keeps the newlines around the block, which is not a disagreement.
    naive_crashes = False
    try:
        naive_data = _YAML.load(naive)
    except Exception:
        naive_crashes = True
        naive_data = None

    if not naive_crashes and naive_data == strict_data:
        return None

    reference_id = path.stem
    if isinstance(strict_data, dict):
        reference_id = str(strict_data.get("reference_id", path.stem))

    return Finding(
        path=path,
        reference_id=reference_id,
        reasons=(
            (
                "frontmatter contains a literal '---' inside a value, so a "
                "delimiter-unaware consumer reads this file differently (issue "
                "#7697); valid here because dismech.patch_reference_validator "
                "repairs the read side, but a bare linkml-reference-validator "
                "run will truncate or crash on it"
            ),
        ),
    )


def scan_cache_dir_consumer_compatibility(cache_dir: Path) -> list[Finding]:
    """Advisory scan for files a delimiter-unaware consumer misreads."""
    findings: list[Finding] = []
    for path in sorted(cache_dir.glob("*.md")):
        finding = check_consumer_compatibility(path)
        if finding is not None:
            findings.append(finding)
    return findings


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
    advisories = scan_cache_dir_consumer_compatibility(cache_dir)

    for advisory in advisories:
        print(f"ADVISORY: {advisory.format()}", file=sys.stderr)
    if advisories:
        # Printed regardless of the gating outcome -- an advisory is no less
        # true when the contract check also found something.
        print(
            f"note: {len(advisories)} file(s) are readable only because of the "
            "local delimiter-aware patch (issue #7697)",
            file=sys.stderr,
        )

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
