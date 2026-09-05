#!/usr/bin/env python3
"""Audit the publications that Orphanet *recites* on prevalence/epidemiology rows.

A ``prevalence:`` or ``epidemiology:`` record sourced from Orphanet carries an
``ORPHA:`` evidence item. That item is direct evidence for the *imported database
assertion*. Orphanet, in turn, names the publication its own estimate came from —
and today that relationship survives only as display text inside ``snippet``:

.. code-block:: yaml

    - reference: ORPHA:271861
      snippet: "1-9 / 1 000 000 | Worldwide | Point prevalence | PMID:29211930"

``PMID:29211930`` cannot be queried, resolved, or told apart from the rest of the
row without parsing the sentence again. Issue #7518 asks for a structured slot to
hold it. This audit is the prerequisite step the maintainer green-lit ahead of
that schema decision: it enumerates every recited token, classifies it, and says
whether the record already cites it as direct evidence — so the slot is designed
against measured data, and so acceptance criterion 3 ("malformed tokens are
reported rather than silently promoted") has a standing guard.

Why classification is needed at all
-----------------------------------

Not every recited token is a publication. ``_clean_source()`` in
``src/dismech/structured_sources/orphanet.py`` captures the Orphadata source tag
and then discards it, so it stamps ``PMID:`` onto **any** digit run preceding
**any** bracketed tag. Orphadata's tag vocabulary is ``PMID``, ``OTHER``,
``EXPERT``, ``DOI`` and ``ORPHANET``; everything mislabelled in the cache today
is a digit run that preceded ``[OTHER]`` or ``[DOI]``. Worked examples, each
traced from the committed cache back to the upstream ``<Source>`` string:

===============================  ==========================================
Cache token                      Upstream ``<Source>``
===============================  ==========================================
``PMID:2012``                    ``European Medicines Agency 2012[OTHER]``
``PMID:0870684507``              ``ISBN:0870684507[OTHER]``
``PMID:9780313387135``           ``ISBN:9780313387135[OTHER]_ORPHANET``
``PMID:008``                     ``DOI:10.1016/j.jfma.2013.01.008[OTHER]``
``PMID:11``                      ``10.1007/978-3-642-05080-0_11[DOI]``
===============================  ==========================================

so a year, an ISBN, and the tail of a DOI all reach the KB wearing a ``PMID:``
prefix. Honouring the captured tag fixes every one of them — that is the parser
half of the issue, and it is deliberately **not** done here (it rewrites
``references_cache/ORPHA_*.md``, which four KB snippets currently quote verbatim).

This audit therefore reads the *committed cache*, which has already lost the tag,
and classifies heuristically. Every class below is a flag for a human, never a
verdict, and in particular:

* **No length gate.** 5- and 6-digit PMIDs are valid and already cited in this KB
  (``references_cache/PMID_68190.md`` is Lancet 1977). Short tokens are reported
  as ``SHORT_SUSPECT``, not rejected — the distinction matters because
  ``PMID:11`` is *syntactically* a real PubMed identifier and only the upstream
  tag reveals it as a DOI fragment.
* **A year is never promoted.** A bare four-digit token in 1900-2030 is
  ``YEAR_SUSPECT``. ``2012`` is also a valid PubMed identifier, so no
  resolvability check can separate "the year 2012" from "PMID 2012"; only a
  human can.

Output is deterministic (no timestamps, stable ordering) so the committed report
under ``research/`` regenerates byte-identically from an unchanged KB and cache.

Usage::

    uv run python scripts/orphanet_prevalence_source_audit.py
    uv run python scripts/orphanet_prevalence_source_audit.py --format tsv
    uv run python scripts/orphanet_prevalence_source_audit.py --out research/orphanet_prevalence_source_audit.md
    uv run python scripts/orphanet_prevalence_source_audit.py --strict
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so it resolves from src/.
from dismech.yaml_io import safe_load_path

#: KB subtrees that may carry ``prevalence:`` / ``epidemiology:`` records.
_KB_GLOBS = ("kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/comorbidities/*.yaml")

#: The two record sections in scope. Both use the same ``EvidenceItem`` shape.
_SECTIONS = ("prevalence", "epidemiology")

#: Orphadata source-type tags that reach a Source cell on their own, with no
#: identifier attached. Censused from the committed caches rather than assumed:
#: ``ORPHANET`` (152), ``EXPERT`` (111), ``PMID`` (7), ``OTHER`` (6), ``REG`` (5),
#: ``INST`` (5). A bare ``PMID`` is its own small loss — Orphanet tagged the row
#: as a publication citation and the identifier did not survive the parse.
_MARKERS = frozenset({"EXPERT", "ORPHANET", "PMID", "OTHER", "REG", "INST"})

#: Default location of the committed report (a script-generated artifact, which
#: ``CLAUDE.md`` explicitly permits under ``research/``).
_DEFAULT_OUT = "research/orphanet_prevalence_source_audit.md"

# --- token classification -------------------------------------------------

#: A recited token that looks like a real, promotable PubMed identifier.
PMID_CANDIDATE = "PMID_CANDIDATE"
#: Four digits in 1900-2030. Never promote: ``2012`` is both a year and a PMID.
YEAR_SUSPECT = "YEAR_SUSPECT"
#: ISBN-13 (``978``/``979`` + 13 digits) or ISBN-10 shaped. Orphanet cites books.
ISBN_SUSPECT = "ISBN_SUSPECT"
#: Fewer than four digits, or leading zeros. Syntactically a PMID, but in the
#: caches these are DOI fragments; needs the upstream tag to settle.
SHORT_SUSPECT = "SHORT_SUSPECT"
#: A bare Orphadata source-type tag (``EXPERT``, ``ORPHANET``, ...) — not a
#: publication.
MARKER = "MARKER"
#: An unterminated ``[PMID`` bracket upstream defeated the regex entirely, so
#: ``_clean_source()`` fell through to its raw-passthrough branch and a real,
#: recoverable identifier is sitting in the cache unparsed.
STRANDED_PMID = "STRANDED_PMID"
#: The raw-passthrough branch again, but with no identifier in it — a URL or an
#: organisation name Orphanet gave as free text.
FREE_TEXT = "FREE_TEXT"

#: Classes that must never be auto-promoted to a publication reference.
NON_PUBLICATION = frozenset({YEAR_SUSPECT, ISBN_SUSPECT, MARKER, FREE_TEXT})

#: Every class, in report order.
ALL_CLASSES = (
    PMID_CANDIDATE,
    YEAR_SUSPECT,
    ISBN_SUSPECT,
    SHORT_SUSPECT,
    STRANDED_PMID,
    FREE_TEXT,
    MARKER,
)


def classify_token(token: str) -> str:
    """Classify one token from an Orphanet Epidemiology ``Source`` cell.

    The cache has already lost Orphadata's ``[PMID]``/``[OTHER]``/``[DOI]`` tag,
    so this is shape-based triage, not adjudication. Ordering matters: ISBN
    shapes are checked before the leading-zero rule, because ``0870684507`` is a
    ten-digit ISBN-10 rather than a malformed PMID.
    """
    token = token.strip()
    if not token or token == "-":
        return FREE_TEXT
    if token in _MARKERS:
        return MARKER
    if re.search(r"\d+\[\w+$", token):
        return STRANDED_PMID
    m = re.fullmatch(r"PMID:(\d+)", token)
    if not m:
        return FREE_TEXT
    digits = m.group(1)
    if len(digits) == 13 and digits[:3] in ("978", "979"):
        return ISBN_SUSPECT
    if len(digits) in (9, 10):
        # No assigned PubMed identifier is anywhere near nine digits, and every
        # such token in the caches traces to an ``ISBN:...[OTHER]`` source.
        return ISBN_SUSPECT
    if len(digits) == 4 and 1900 <= int(digits) <= 2030:
        return YEAR_SUSPECT
    if len(digits) < 4 or digits.startswith("0"):
        return SHORT_SUSPECT
    return PMID_CANDIDATE


# --- cache parsing --------------------------------------------------------


def _normalize_row(text: str) -> str:
    """Normalize a table row (or a curator snippet) for substring matching.

    Curators may quote a row with or without its leading/trailing pipes, and may
    stop short of the final column — both forms must match the same row.
    """
    return re.sub(r"\s+", " ", text.strip().strip("|").strip())


@dataclass(frozen=True)
class EpiRow:
    """One parsed row of an ORPHA cache ``## Epidemiology`` table."""

    pclass: str
    region: str
    ptype: str
    source: str

    @property
    def normalized(self) -> str:
        return _normalize_row(
            f"{self.pclass} | {self.region} | {self.ptype} | {self.source}"
        )

    def tokens(self) -> list[str]:
        """The Source cell split into individual recited tokens."""
        if self.source in ("", "-"):
            return []
        return [t for t in (p.strip() for p in self.source.split(",")) if t]


def parse_epidemiology_rows(cache_text: str) -> list[EpiRow]:
    """Extract the ``## Epidemiology`` table rows from an ORPHA cache body."""
    rows: list[EpiRow] = []
    in_table = False
    for line in cache_text.splitlines():
        if line.startswith("## "):
            in_table = line.strip() == "## Epidemiology"
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            continue
        if cells[0] in ("Class", "---") or set(cells[0]) == {"-"}:
            continue
        rows.append(EpiRow(*cells))
    return rows


# --- KB walk --------------------------------------------------------------


@dataclass
class Finding:
    """One recited token, resolved back to the KB record that imported it."""

    kb_file: str
    section: str
    record_index: int
    orpha_id: str
    token: str
    classification: str
    match_status: str
    duplicates_direct_evidence: bool
    cached_locally: bool

    def as_row(self) -> list[str]:
        return [
            self.kb_file,
            self.section,
            str(self.record_index),
            self.orpha_id,
            self.token,
            self.classification,
            self.match_status,
            "yes" if self.duplicates_direct_evidence else "no",
            "yes" if self.cached_locally else "no",
        ]


TSV_HEADER = [
    "kb_file",
    "section",
    "record_index",
    "orpha_id",
    "token",
    "classification",
    "row_match",
    "duplicates_direct_evidence",
    "cached_locally",
]


@dataclass
class AuditResult:
    findings: list[Finding]
    orpha_evidence_items: int
    records_with_orpha_evidence: int
    #: ``(kb_file, orpha_id, status)`` for evidence items whose snippet did not
    #: resolve to an Epidemiology row. ``NON_EPI_QUOTE`` entries are expected;
    #: ``UNMATCHED`` / ``AMBIGUOUS`` are the ones a human should look at.
    unresolved_snippets: list[tuple[str, str, str]]
    missing_cache_files: list[tuple[str, str]]
    #: ``classification -> (occurrences, distinct tokens)`` across *every*
    #: ``references_cache/ORPHA_*.md``, not just the KB-cited rows. This is the
    #: blast radius of a parser fix.
    cache_census: dict[str, tuple[int, int]]
    #: ``(kb_file, reference, token)`` for KB snippets that quote a token a
    #: parser fix would rewrite — i.e. the snippets that would stop validating.
    at_risk_snippets: list[tuple[str, str, str]]

    @property
    def needs_review(self) -> list[tuple[str, str, str]]:
        return [u for u in self.unresolved_snippets if u[2] != "NON_EPI_QUOTE"]


#: Classes whose rendered text a tag-honouring parser would necessarily change.
#: A KB snippet quoting one of these stops matching its cache the moment
#: ``_clean_source()`` is fixed — the collision between step 1 of #7518 and its
#: own acceptance criterion that existing snippets stay unchanged.
VOLATILE = frozenset({YEAR_SUSPECT, ISBN_SUSPECT, SHORT_SUSPECT, STRANDED_PMID})


def _cache_path(root: Path, orpha_id: str) -> Path:
    return root / "references_cache" / f"ORPHA_{orpha_id.split(':', 1)[1]}.md"


def _match_row(rows: list[EpiRow], snippet: str, cache_text: str) -> tuple[EpiRow | None, str]:
    """Find the cache row a curator's snippet was quoted from.

    Statuses:

    ``MATCHED``
        The snippet is a substring of exactly one Epidemiology row (or of
        several that recite the same sources).
    ``NON_EPI_QUOTE``
        The snippet is in the cache body but not in the Epidemiology table —
        typically a prevalence record citing Orphanet's ``## Definition`` prose
        ("NON RARE IN EUROPE: Celiac disease"). Legitimate, and it means there
        is no recited publication on that record to preserve.
    ``AMBIGUOUS``
        Several rows contain the snippet and they recite different sources, so
        the recitation cannot be attributed.
    ``UNMATCHED``
        Not found anywhere in the cache body. That is a real problem — the
        reference validator permits full-text matches this audit cannot see, so
        report it rather than treating it as an error here.
    """
    if not snippet:
        return None, "UNMATCHED"
    needle = _normalize_row(snippet)
    hits = [r for r in rows if needle in r.normalized]
    if hits:
        if len(hits) > 1 and len({r.source for r in hits}) > 1:
            return None, "AMBIGUOUS"
        return hits[0], "MATCHED"
    body = re.sub(r"\s+", " ", cache_text)
    return None, "NON_EPI_QUOTE" if needle in body else "UNMATCHED"


def census_all_caches(root: Path) -> tuple[dict[str, tuple[int, int]], set[str]]:
    """Classify every Source token in every ORPHA cache, not just KB-cited rows.

    Returns the per-class ``(occurrences, distinct)`` census and the set of
    token strings a tag-honouring parser would rewrite.
    """
    occurrences: Counter[str] = Counter()
    distinct: dict[str, set[str]] = {}
    volatile: set[str] = set()
    for path in sorted((root / "references_cache").glob("ORPHA_*.md")):
        for row in parse_epidemiology_rows(path.read_text(encoding="utf-8")):
            for token in row.tokens():
                cls = classify_token(token)
                occurrences[cls] += 1
                distinct.setdefault(cls, set()).add(token)
                if cls in VOLATILE:
                    volatile.add(token)
    return {c: (n, len(distinct[c])) for c, n in occurrences.items()}, volatile


def find_at_risk_snippets(root: Path, volatile: set[str]) -> list[tuple[str, str, str]]:
    """Find KB evidence snippets that quote a token a parser fix would rewrite.

    Scans every ``evidence`` item anywhere in the KB — not only prevalence and
    epidemiology — because the volatile text is cache content and any section
    may quote it.
    """
    if not volatile:
        return []
    hits: list[tuple[str, str, str]] = []
    # Anchor on a non-digit (or end of string) so the short token ``PMID:11``
    # does not match inside the perfectly good ``PMID:11235813``.
    patterns = [(t, re.compile(re.escape(t) + r"(?!\d)")) for t in sorted(volatile)]

    def walk(node, rel: str) -> None:
        if isinstance(node, dict):
            snippet = node.get("snippet")
            ref = node.get("reference")
            if isinstance(snippet, str) and isinstance(ref, str):
                for token, pattern in patterns:
                    if pattern.search(snippet):
                        hits.append((rel, ref, token))
            for value in node.values():
                walk(value, rel)
        elif isinstance(node, list):
            for value in node:
                walk(value, rel)

    for path in sorted(p for glob in _KB_GLOBS for p in root.glob(glob)):
        try:
            doc = safe_load_path(path)
        except Exception:
            continue
        walk(doc, path.relative_to(root).as_posix())
    return sorted(set(hits))


def audit(root: Path) -> AuditResult:
    """Walk the KB and resolve every ORPHA-sourced prevalence/epidemiology row."""
    findings: list[Finding] = []
    unresolved: list[tuple[str, str, str]] = []
    missing_cache: list[tuple[str, str]] = []
    evidence_items = 0
    records = 0
    cache_cache: dict[str, tuple[list[EpiRow], str] | None] = {}

    paths = sorted(p for glob in _KB_GLOBS for p in root.glob(glob))
    for path in paths:
        try:
            doc = safe_load_path(path)
        except Exception:  # a malformed entry is check-duplicate-keys' problem
            continue
        if not isinstance(doc, dict):
            continue
        rel = path.relative_to(root).as_posix()
        for section in _SECTIONS:
            recs = doc.get(section)
            if not isinstance(recs, list):
                continue
            for idx, rec in enumerate(recs):
                if not isinstance(rec, dict):
                    continue
                evidence = [e for e in (rec.get("evidence") or []) if isinstance(e, dict)]
                orpha_items = [
                    e for e in evidence if str(e.get("reference", "")).startswith("ORPHA:")
                ]
                if not orpha_items:
                    continue
                records += 1
                sibling_refs = {str(e.get("reference", "")) for e in evidence}
                for item in orpha_items:
                    evidence_items += 1
                    orpha_id = str(item["reference"])
                    if orpha_id not in cache_cache:
                        cpath = _cache_path(root, orpha_id)
                        if cpath.exists():
                            text = cpath.read_text(encoding="utf-8")
                            cache_cache[orpha_id] = (parse_epidemiology_rows(text), text)
                        else:
                            cache_cache[orpha_id] = None
                    parsed = cache_cache[orpha_id]
                    if parsed is None:
                        missing_cache.append((rel, orpha_id))
                        continue
                    rows, cache_text = parsed
                    row, status = _match_row(rows, str(item.get("snippet") or ""), cache_text)
                    if row is None:
                        unresolved.append((rel, orpha_id, status))
                        continue
                    for token in row.tokens():
                        cls = classify_token(token)
                        # Computed for every PMID-shaped token, not just the
                        # plausible ones: a year or ISBN that already has a
                        # cache file would mean something was fetched as if it
                        # were the recited paper, which is the failure this
                        # audit exists to make visible.
                        digits = re.fullmatch(r"PMID:(\d+)", token)
                        cached = bool(digits) and (
                            root / "references_cache" / f"PMID_{digits.group(1)}.md"
                        ).exists()
                        findings.append(
                            Finding(
                                kb_file=rel,
                                section=section,
                                record_index=idx,
                                orpha_id=orpha_id,
                                token=token,
                                classification=cls,
                                match_status=status,
                                duplicates_direct_evidence=token in sibling_refs,
                                cached_locally=cached,
                            )
                        )

    findings.sort(key=lambda f: (f.kb_file, f.section, f.record_index, f.token))
    unresolved.sort()
    missing_cache.sort()
    cache_census, volatile = census_all_caches(root)
    return AuditResult(
        findings,
        evidence_items,
        records,
        unresolved,
        missing_cache,
        cache_census,
        find_at_risk_snippets(root, volatile),
    )


# --- reporting ------------------------------------------------------------

_PREAMBLE = """<!-- Generated by scripts/orphanet_prevalence_source_audit.py -- do not hand-edit.
     Regenerate with `just orphanet-prevalence-source-audit`. -->

# Orphanet prevalence/epidemiology recited-publication audit

Every `prevalence:` / `epidemiology:` record whose evidence cites an `ORPHA:` id,
resolved back to the `## Epidemiology` row it was quoted from, with each
publication token that Orphanet **recites** on that row classified.

This is the measurement step for [#7518](https://github.com/monarch-initiative/dismech/issues/7518),
which asks for a structured slot holding "publication named by this source" as
distinct from "publication DisMech reviewed". It is deliberately read-only: no
schema slot, no `kb/**` change, and no cache rewrite.

## How to read a classification

The committed caches have already lost Orphadata's `[PMID]` / `[OTHER]` / `[DOI]`
tag — `_clean_source()` captures it and discards it, stamping `PMID:` onto any
digit run before any tag. So the classes below are **shape-based triage of a lossy
string, flags for a human, never verdicts**:

| Class | Meaning |
|---|---|
| `PMID_CANDIDATE` | Plausible PubMed identifier. `cached_locally` says whether `references_cache/PMID_<n>.md` already exists — not whether PubMed resolves it. |
| `YEAR_SUSPECT` | Bare four-digit token in 1900-2030. Never promote: `2012` is simultaneously a year and a valid PubMed identifier, so no resolvability check can separate them. |
| `ISBN_SUSPECT` | ISBN-13 (`978`/`979`) or ISBN-10 shaped. Orphanet cites books. |
| `SHORT_SUSPECT` | Under four digits, or leading zeros. Reported, *not* rejected — short PMIDs are genuinely valid (`references_cache/PMID_68190.md` is Lancet 1977), so there is no length gate here. In the current caches these trace to DOI fragments. |
| `STRANDED_PMID` | An unterminated `[PMID` bracket upstream defeated the regex, so `_clean_source()` fell through to raw passthrough and left a real, recoverable identifier unparsed in the cache. |
| `FREE_TEXT` | The same passthrough branch with no identifier in it — a URL or an organisation name. |
| `MARKER` | A bare Orphadata source-type tag (`EXPERT`, `ORPHANET`, `REG`, `INST`, `OTHER`, and a bare `PMID` whose identifier did not survive the parse). Not a citation. |

`duplicates_direct_evidence` is true when the same identifier already appears as a
sibling `reference` on that record, i.e. DisMech has independently cited it and a
provenance slot would be redundant there.

## Records whose snippet is not an epidemiology row

Some prevalence records cite Orphanet prose rather than a table row (`NON_EPI_QUOTE`).
Those are legitimate and recite nothing, so they contribute no tokens — but they do
bound the backfill, so they are counted. `UNMATCHED` and `AMBIGUOUS` are the
statuses that want a human.

"""


def render_markdown(result: AuditResult) -> str:
    out = io.StringIO()
    out.write(_PREAMBLE)

    by_class = Counter(f.classification for f in result.findings)
    promotable = [
        f
        for f in result.findings
        if f.classification == PMID_CANDIDATE and not f.duplicates_direct_evidence
    ]
    distinct_promotable = sorted({f.token for f in promotable})

    out.write("## Totals\n\n")
    out.write("| | Count |\n|---|---:|\n")
    out.write(f"| Records carrying `ORPHA:` evidence | {result.records_with_orpha_evidence} |\n")
    out.write(f"| `ORPHA:` evidence items on those records | {result.orpha_evidence_items} |\n")
    out.write(f"| Recited tokens resolved from cache rows | {len(result.findings)} |\n")
    out.write(
        "| Distinct publications a backfill would introduce | "
        f"{len(distinct_promotable)} |\n"
    )
    out.write(
        "| Tokens that must never be promoted | "
        f"{sum(by_class[c] for c in NON_PUBLICATION)} |\n"
    )
    non_epi = sum(1 for u in result.unresolved_snippets if u[2] == "NON_EPI_QUOTE")
    out.write(f"| Evidence items citing Orphanet prose, not a row | {non_epi} |\n")
    out.write(f"| Snippets needing review (`UNMATCHED`/`AMBIGUOUS`) | {len(result.needs_review)} |\n")
    out.write(f"| `ORPHA:` ids with no cache file | {len(result.missing_cache_files)} |\n\n")

    out.write("## Tokens by classification\n\n")
    out.write("| Class | Tokens | Distinct | Already direct evidence |\n|---|---:|---:|---:|\n")
    for cls in ALL_CLASSES:
        rows = [f for f in result.findings if f.classification == cls]
        if not rows:
            continue
        out.write(
            f"| `{cls}` | {len(rows)} | {len({r.token for r in rows})} | "
            f"{sum(1 for r in rows if r.duplicates_direct_evidence)} |\n"
        )
    out.write("\n")

    flagged = [
        f
        for f in result.findings
        if f.classification not in (PMID_CANDIDATE, MARKER)
    ]
    out.write("## Flagged tokens (never auto-promote)\n\n")
    if flagged:
        out.write("| KB file | Section | ORPHA | Token | Class |\n|---|---|---|---|---|\n")
        for f in flagged:
            out.write(
                f"| `{f.kb_file}` | {f.section} | {f.orpha_id} | `{f.token}` | `{f.classification}` |\n"
            )
    else:
        out.write("None.\n")
    out.write("\n")

    out.write("## Cache-wide census (blast radius of a parser fix)\n\n")
    out.write(
        "The table above counts only rows a KB record cites. This one classifies "
        "every Source token in every `references_cache/ORPHA_*.md`, which is what "
        "a `_clean_source()` fix would rewrite.\n\n"
    )
    out.write("| Class | Tokens | Distinct |\n|---|---:|---:|\n")
    for cls in ALL_CLASSES:
        if cls in result.cache_census:
            n, d = result.cache_census[cls]
            out.write(f"| `{cls}` | {n} | {d} |\n")
    out.write("\n")

    out.write("## KB snippets a parser fix would break\n\n")
    if result.at_risk_snippets:
        out.write(
            "Each snippet below quotes a cache token that a tag-honouring parser "
            "necessarily rewrites, so fixing `_clean_source()` and rebuilding the "
            "caches would stop these snippets matching. #7518 asks for both the fix "
            "*and* for existing snippets to stay byte-identical; these rows are where "
            "those two requirements collide, and the collision needs a maintainer "
            "decision rather than a unilateral edit.\n\n"
        )
        out.write("| KB file | Reference | Token |\n|---|---|---|\n")
        for rel, ref, token in result.at_risk_snippets:
            out.write(f"| `{rel}` | {ref} | `{token}` |\n")
    else:
        out.write("None.\n")
    out.write("\n")

    if result.unresolved_snippets:
        out.write("## Snippets not matched to an epidemiology row\n\n")
        out.write("| KB file | ORPHA | Status |\n|---|---|---|\n")
        for rel, orpha_id, status in result.unresolved_snippets:
            out.write(f"| `{rel}` | {orpha_id} | `{status}` |\n")
        out.write("\n")

    if result.missing_cache_files:
        out.write("## `ORPHA:` ids with no cache file\n\n")
        for rel, orpha_id in result.missing_cache_files:
            out.write(f"- `{rel}` -> {orpha_id}\n")
        out.write("\n")

    out.write("## Every recited token\n\n")
    out.write(
        "| KB file | Section | Rec | ORPHA | Token | Class | Dup | Cached |\n"
        "|---|---|---:|---|---|---|---|---|\n"
    )
    for f in result.findings:
        out.write(
            f"| `{f.kb_file}` | {f.section} | {f.record_index} | {f.orpha_id} | "
            f"`{f.token}` | `{f.classification}` | "
            f"{'yes' if f.duplicates_direct_evidence else '-'} | "
            f"{'yes' if f.cached_locally else '-'} |\n"
        )
    return out.getvalue()


def render_tsv(result: AuditResult) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf, delimiter="\t", lineterminator="\n")
    writer.writerow(TSV_HEADER)
    for f in result.findings:
        writer.writerow(f.as_row())
    return buf.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--format",
        choices=("markdown", "tsv", "summary"),
        default="markdown",
        help="Output format (default: markdown report).",
    )
    parser.add_argument(
        "--out",
        help=f"Write to this path instead of stdout (markdown default: {_DEFAULT_OUT}).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any token is flagged as a non-publication or is unresolved.",
    )
    parser.add_argument("--root", default=str(_REPO_ROOT), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    result = audit(Path(args.root))

    if args.format == "tsv":
        text = render_tsv(result)
    elif args.format == "summary":
        counts = Counter(f.classification for f in result.findings)
        lines = [
            f"records with ORPHA evidence: {result.records_with_orpha_evidence}",
            f"ORPHA evidence items:        {result.orpha_evidence_items}",
            f"recited tokens:              {len(result.findings)}",
        ]
        lines += [f"  {cls:<16} {n}" for cls, n in sorted(counts.items())]
        lines.append(f"snippets needing review:     {len(result.needs_review)}")
        text = "\n".join(lines) + "\n"
    else:
        text = render_markdown(result)

    out_path = args.out or (_DEFAULT_OUT if args.format == "markdown" else None)
    if out_path:
        target = Path(out_path)
        if not target.is_absolute():
            target = Path(args.root) / target
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target}")
    else:
        sys.stdout.write(text)

    if args.strict:
        bad = [f for f in result.findings if f.classification in NON_PUBLICATION]
        if bad or result.needs_review:
            print(
                f"FAIL: {len(bad)} non-publication token(s), "
                f"{len(result.needs_review)} snippet(s) needing review",
                file=sys.stderr,
            )
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
