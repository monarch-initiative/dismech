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

import os
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
    # Cache-staleness stamps and full-text access outcome, written by
    # linkml-reference-validator once it could tell a cache entry written by an
    # older extractor from a current one (upstream #62, #85). The version
    # integers are the fetcher's own cache-format counters -- dismech never
    # interprets them, it only has to accept them, and a refresh rewrites the
    # file rather than bumping a stamp in place. ``full_text_declined`` names
    # the policy that stopped a full-text fetch (for example
    # ``landing_page_only``), and ``full_text_access_type`` records whether the
    # located file was openly licensed. All five are absent on cache files
    # written before the upgrade, so they stay optional: the repository holds
    # both generations at once and `just check-reference-cache-frontmatter`
    # must pass over both.
    extractor_version: int | None = None
    xml_extraction_version: int | None = None
    html_full_text_version: int | None = None
    absent_content_version: int | None = None
    full_text_declined: str | None = None
    full_text_access_type: str | None = None
    full_text_source_item_id: str | None = None
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

    Upstream now splits on the ``---`` *line*
    (linkml/linkml-reference-validator#71), so a current validator reads these
    files correctly. They remain a hazard for any other delimiter-unaware
    consumer, and the emitter's quoting is not stable across versions (#7393,
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
    # because this is the first dependency of `just qc`.
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
                "#7697); valid for a current linkml-reference-validator, which "
                "splits on the delimiter line, but an older one or another "
                "naive reader will truncate or crash on it"
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


# ---------------------------------------------------------------------------
# Empty caches: records fetched with no quotable text (issue #9825)
# ---------------------------------------------------------------------------
#
# The fetcher writes ``content_type: unavailable`` when it found a record but
# retrieved no text a snippet could quote -- no abstract, no full text. That
# field, not body length, is the signal: a structured ORPHA/ClinGen cache or a
# guideline monograph without a ``## Content`` heading has a short or oddly
# shaped body and is perfectly quotable.
#
# "Unavailable" describes one fetch, not the paper. PMID:33054089 cached as
# ``unavailable`` and an hour later re-fetched as ``full_text_xml`` from PMC, so
# every message below says what happened on this fetch and that a retry may
# succeed, never that the record cannot be quoted.

EMPTY_CONTENT_TYPE = "unavailable"

_CONTENT_TYPE_RE = re.compile(r"""(?m)^content_type:[ \t]*['"]?([A-Za-z0-9_\-]+)""")
_FULL_TEXT_ATTEMPTED_RE = re.compile(
    r"""(?m)^full_text_attempted:[ \t]*['"]?(true|True|TRUE|yes)\b"""
)
_REFERENCE_ID_RE = re.compile(
    r"""(?m)^reference_id:[ \t]*['"]?([^'"\n]+?)['"]?[ \t]*$"""
)


@dataclass(frozen=True)
class EmptyCache:
    """A cache file whose fetch retrieved no quotable text."""

    path: Path
    reference_id: str
    full_text_attempted: bool

    @property
    def prefix(self) -> str:
        head, sep, _ = self.reference_id.partition(":")
        return head if sep else "(none)"


def read_empty_cache(path: Path) -> EmptyCache | None:
    """Return an :class:`EmptyCache` if ``path`` is ``content_type: unavailable``.

    Reads only the frontmatter, with line-anchored regexes rather than a full
    YAML parse, so a sweep over the ~33k-file corpus stays at a few seconds. A
    file with no frontmatter or no ``content_type`` is not reported: the
    contract check above is what reports malformed files.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    split = split_frontmatter(text)
    if split is None:
        return None
    match = _CONTENT_TYPE_RE.search(split.frontmatter)
    if match is None or match.group(1) != EMPTY_CONTENT_TYPE:
        return None
    id_match = _REFERENCE_ID_RE.search(split.frontmatter)
    reference_id = id_match.group(1).strip() if id_match else path.stem
    return EmptyCache(
        path=path,
        reference_id=reference_id,
        full_text_attempted=_FULL_TEXT_ATTEMPTED_RE.search(split.frontmatter)
        is not None,
    )


def _cache_stem(reference_id: str) -> str:
    return (
        reference_id.replace(":", "_")
        .replace("/", "_")
        .replace("?", "_")
        .replace("=", "_")
    )


def resolve_cache_file(cache_dir: Path, reference_id: str) -> Path | None:
    """Locate the cache file the fetcher wrote for ``reference_id``.

    Tries the filename exactly as the fetcher derives it, then a
    case-insensitive match (DOIs are cached in mixed case, and a curator may
    type ``pmid:`` for ``PMID:``). Returns ``None`` when nothing matches, in
    which case the caller stays silent rather than guessing.
    """
    reference_id = reference_id.strip()
    if not reference_id:
        return None
    direct = cache_dir / f"{_cache_stem(reference_id)}.md"
    if direct.is_file():
        return direct
    wanted = f"{_cache_stem(reference_id)}.md".casefold()
    try:
        names = os.listdir(cache_dir)
    except OSError:
        return None
    for name in names:
        if name.casefold() == wanted:
            return cache_dir / name
    return None


def empty_cache_warning(reference_id: str, cache_dir: Path) -> str | None:
    """Return the fetch-time warning for ``reference_id``, or ``None``.

    ``None`` means the cache file is missing (the fetch failed, which the
    fetcher reports itself) or holds quotable text.
    """
    path = resolve_cache_file(cache_dir, reference_id)
    if path is None:
        return None
    empty = read_empty_cache(path)
    if empty is None:
        return None
    return (
        f"WARNING: {empty.reference_id} was cached with no quotable text "
        f"(content_type: {EMPTY_CONTENT_TYPE} in {path}).\n"
        "  No abstract or full text was retrieved on this fetch, so nothing in "
        "this cache file can be\n"
        "  used as an evidence snippet as it stands. This is often a property "
        "of the fetch rather than\n"
        "  of the paper: a retry may succeed, for example once an open-access "
        "full text is reachable.\n"
        "  Retry with:  scripts/run_reference_validator.sh cache reference "
        f"{empty.reference_id} --force\n"
        "  If it stays empty, say in `notes` why the paper is not cited (a "
        "top-level `references:`\n"
        "  entry is optional); never write a snippet paraphrased from the "
        "title or from memory.\n"
        "  (Advisory only: the cache file is kept and the exit code is unchanged. "
        "See issue #9825.)"
    )


def scan_empty_caches(paths: list[Path]) -> list[EmptyCache]:
    """Return every ``content_type: unavailable`` record under ``paths``.

    Each path may be a cache directory (its ``*.md`` files are read) or a
    single cache file.
    """
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.glob("*.md")))
        elif path.is_file():
            files.append(path)
    results: list[EmptyCache] = []
    for file in files:
        empty = read_empty_cache(file)
        if empty is not None:
            results.append(empty)
    return results


@dataclass
class KbCitations:
    """Where a set of reference ids is cited in ``kb/``."""

    files: dict[str, set[Path]]
    snippet_citations: dict[str, list[Path]]


def _walk_citations(
    node: Any,
    path: Path,
    wanted: dict[str, str],
    citations: KbCitations,
    parent_key: str | None = None,
) -> None:
    if isinstance(node, dict):
        ref = node.get("reference")
        if ref is None and parent_key == "references":
            ref = node.get("id")
        if isinstance(ref, str):
            key = wanted.get(ref.strip().casefold())
            if key is not None:
                citations.files.setdefault(key, set()).add(path)
                snippet = node.get("snippet")
                if isinstance(snippet, str) and snippet.strip():
                    citations.snippet_citations.setdefault(key, []).append(path)
        for child_key, value in node.items():
            _walk_citations(value, path, wanted, citations, str(child_key))
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, str) and parent_key == "references":
                key = wanted.get(item.strip().casefold())
                if key is not None:
                    citations.files.setdefault(key, set()).add(path)
            else:
                _walk_citations(item, path, wanted, citations, parent_key)


def find_kb_citations(kb_dir: Path, reference_ids: list[str]) -> KbCitations:
    """Find where each of ``reference_ids`` is cited in ``kb_dir/**/*.yaml``.

    A citation is a ``reference:`` value anywhere in a document (evidence items
    and top-level ``references:`` entries both use that key), or an ``id`` /
    bare string inside a ``references:`` list. Matching is case-insensitive so
    a DOI cited in a different case still counts.
    """
    from dismech import kb_cache

    wanted = {rid.casefold(): rid for rid in reference_ids}
    citations = KbCitations(files={}, snippet_citations={})
    for path, document in kb_cache.iter_documents(kb_dir, "**/*.yaml"):
        _walk_citations(document, path, wanted, citations)
    return citations


def format_empty_cache_summary(
    empties: list[EmptyCache],
    total_files: int,
    citations: KbCitations | None,
) -> str:
    """Human-readable summary of the empty-cache sweep."""
    lines = [
        (
            f"Reference caches with no quotable text (content_type: "
            f"{EMPTY_CONTENT_TYPE}): {len(empties)} of {total_files} cache files"
        ),
        "",
        (
            "  'tried full text' = full_text_attempted: true; the full-text "
            "route was tried and found nothing."
        ),
        (
            "  'not retried'     = no such marker; fetched before or outside "
            "the full-text route, so a"
        ),
        "                      --force refetch may recover text.",
        "",
    ]
    by_prefix: dict[str, list[EmptyCache]] = {}
    for empty in empties:
        by_prefix.setdefault(empty.prefix, []).append(empty)

    header = (
        f"  {'prefix':<24} {'total':>6} {'tried full text':>16} {'not retried':>12}"
    )
    if citations is not None:
        header += f" {'cited in kb':>12}"
    lines.append(header)
    for prefix in sorted(by_prefix, key=lambda p: (-len(by_prefix[p]), p)):
        group = by_prefix[prefix]
        attempted = sum(1 for e in group if e.full_text_attempted)
        row = f"  {prefix:<24} {len(group):>6} {attempted:>16} {len(group) - attempted:>12}"
        if citations is not None:
            cited = sum(1 for e in group if e.reference_id in citations.files)
            row += f" {cited:>12}"
        lines.append(row)

    if citations is not None:
        cited_ids = [e for e in empties if e.reference_id in citations.files]
        cited_files = (
            set().union(*citations.files.values()) if citations.files else set()
        )
        lines += [
            "",
            (
                f"Cited anywhere in kb/: {len(cited_ids)} record(s), across "
                f"{len(cited_files)} file(s)."
            ),
        ]
        snippet_ids = sorted(citations.snippet_citations)
        lines.append(
            "Cited by an evidence item carrying a snippet: "
            f"{len(snippet_ids)} record(s)"
            + (
                " (expected 0: an empty cache has nothing to quote)"
                if not snippet_ids
                else ":"
            )
        )
        for rid in snippet_ids:
            files = sorted({str(p) for p in citations.snippet_citations[rid]})
            lines.append(f"  - {rid}: {', '.join(files)}")
    lines += [
        "",
        (
            "Report-only (exit 0). A --force refetch may recover text; if the "
            "record stays empty,"
        ),
        (
            "say in `notes` why the paper is not cited (a `references:` entry "
            "is optional), never write a snippet."
        ),
        "See issue #9825.",
    ]
    return "\n".join(lines)


def format_empty_cache_tsv(
    empties: list[EmptyCache], citations: KbCitations | None
) -> str:
    """One row per empty cache record."""
    rows = [
        (
            "reference_id\tprefix\tfull_text_attempted\tkb_files_citing\t"
            "snippet_citations\tpath"
        )
    ]
    for empty in empties:
        if citations is None:
            cited, snippets = "", ""
        else:
            cited = str(len(citations.files.get(empty.reference_id, ())))
            snippets = str(len(citations.snippet_citations.get(empty.reference_id, ())))
        rows.append(
            f"{empty.reference_id}\t{empty.prefix}\t"
            f"{str(empty.full_text_attempted).lower()}\t{cited}\t{snippets}\t{empty.path}"
        )
    return "\n".join(rows)


def main_list_empty(argv: list[str]) -> int:
    """CLI for ``just list-empty-reference-caches``. Always exits 0."""
    import argparse

    from dismech import kb_cache

    parser = argparse.ArgumentParser(
        prog="list-empty-reference-caches",
        description=(
            "List reference caches fetched with no quotable text "
            "(content_type: unavailable). Read-only and offline."
        ),
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="cache directories or files to sweep (default: references_cache)",
    )
    parser.add_argument("--format", choices=("summary", "tsv"), default="summary")
    parser.add_argument("--kb-dir", type=Path, default=Path("kb"))
    parser.add_argument(
        "--no-kb",
        action="store_true",
        help="skip the kb/ citation lookup (it parses every KB file)",
    )
    args = parser.parse_args(argv)

    paths = args.paths or [Path("references_cache")]
    total_files = 0
    for path in paths:
        if path.is_dir():
            total_files += sum(1 for _ in path.glob("*.md"))
        elif path.is_file():
            total_files += 1
    empties = scan_empty_caches(paths)

    citations = None
    if not args.no_kb and args.kb_dir.is_dir():
        kb_cache.default_off()
        citations = find_kb_citations(
            args.kb_dir, [empty.reference_id for empty in empties]
        )

    if args.format == "tsv":
        print(format_empty_cache_tsv(empties, citations))
    else:
        print(format_empty_cache_summary(empties, total_files, citations))
    return 0


def main_fetch_warning(argv: list[str]) -> int:
    """CLI used by ``scripts/run_reference_validator.sh`` after ``cache reference``.

    Prints the empty-cache warning to stderr for each id whose cache file is
    ``content_type: unavailable``. Always exits 0: the warning is advisory.
    """
    import argparse

    parser = argparse.ArgumentParser(prog="empty-cache-warning")
    parser.add_argument("reference_ids", nargs="+")
    parser.add_argument("--cache-dir", type=Path, default=Path("references_cache"))
    args = parser.parse_args(argv)
    for reference_id in args.reference_ids:
        try:
            warning = empty_cache_warning(reference_id, args.cache_dir)
        except Exception:  # pragma: no cover - advisory path must never fail
            warning = None
        if warning:
            print(warning, file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    if args and args[0] == "list-empty":
        return main_list_empty(args[1:])
    if args and args[0] == "fetch-warning":
        return main_fetch_warning(args[1:])
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
            f"note: {len(advisories)} file(s) carry a frontmatter value that "
            "only a delimiter-aware reader survives; the current validator is "
            "one (linkml/linkml-reference-validator#71), but other consumers "
            "are not (issue #7697)",
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
