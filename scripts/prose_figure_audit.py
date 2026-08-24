#!/usr/bin/env python3
"""Audit quantitative figures written into ``description:`` / ``notes:`` prose.

Issue #7791 named a failure mode the rest of the validation stack is structurally
blind to. Every anti-hallucination check dismech runs — ``validate-references``,
``check_snippets_verbatim.py``, ``count-verified-snippets`` — operates on
``evidence[].snippet``. A claim that never becomes a snippet is never checked by
anything. So a deep-research report's *"LAM occurs in 30-40% of adult females with
TSC"*, copied into a ``description:`` and attributed to a real, topically plausible
PMID that does not contain the figure, passes the entire suite.

The reported evidence is that this is not rare. @jmcmurry ran a batch of 10 new
entries in which every curating agent was explicitly warned about this exact risk
and every entry was adversarially reviewed for it. Snippets came back 992/992
clean; unverified or source-contradicted prose claims turned up in **10 of 10**
entries. The channel CI checks was perfect and the channel it does not check
failed everywhere, under warning.

This script is the "targeted audit rather than a sweep" the issue asks for. It
does not attempt to judge prose. It asks one narrow, mechanical question per
figure, and the scope of that question is what makes it useful:

    This ``description:`` states a figure. Does that figure appear in the
    references cited by the **nearest enclosing evidence block**?

Scope has to be local, and that is not a stylistic preference. Checking against
everything the entry cites is worthless: ``Tuberous_Sclerosis_Complex.yaml``
cites 33 prose references whose bodies between them contain **all 90** two-digit
integers, so a whole-entry corpus "confirms" any percentage you care to invent.
Adjacency is what carries information, and adjacency is also exactly what the
issue asks for — *"quantitative claims that are not backed by an adjacent
evidence item"*.

Three verdicts, in descending order of how much they should worry you:

``NOT_IN_ADJACENT``
    The prose sits next to an ``evidence:`` block, and the figure appears in
    none of that block's cached references. This is the #7791 shape: a real,
    topically plausible citation attached to a number it does not contain.
``UNCITED``
    The figure sits in prose with no adjacent evidence item anywhere up its
    ancestor chain. Not evidence of falsification — a coverage gap, and the
    surface on which the falsifications land.
``OK``
    Found adjacently. Says the number is present, nothing more (see below).

Each finding also records ``in_entry_corpus``: whether the figure turns up
anywhere else in the entry's cited literature. A ``NOT_IN_ADJACENT`` finding that
is also absent entry-wide is the strongest signal the tool produces.

What it deliberately does NOT do
--------------------------------

It is **advisory and heuristic**, and is not wired into ``just qc`` or CI. Three
reasons it must not gate:

* **Derived figures are legitimate.** A curator may write "roughly a third" from
  a cached "34/103", or convert 1-in-25,000 to 4 per 100,000. Common conversions
  are handled (see :func:`equivalent_figures`), but arithmetic in general is not.
* **Not every source is cached prose.** Textbook knowledge, GeneReviews chapters
  behind a PDF-extraction failure, and figures a curator knows from the field are
  all legitimate and all unmatched here.
* **A match is not a verification.** Finding "40" in an adjacent abstract says
  nothing about whether it was 40% of *that*. This tool can raise suspicion; only
  reading the source resolves it. ``OK`` is not a clean bill of health, and the
  #7791 cases where the wrong figure is *also* a real figure in the cited paper
  would pass.

The asymmetry is intentional: the matcher is generous, so it under-reports rather
than over-reports.

Scope of what counts as a "figure"
----------------------------------

Only number forms carrying a quantitative unit — percentages, ``1 in N``, rates
per 100,000/million, and ``N-fold``. Bare integers are excluded, because
"exon 51", "type 2" and "chromosome 15" are names, not measurements.

Usage::

    uv run python scripts/prose_figure_audit.py
    uv run python scripts/prose_figure_audit.py --dr-only --format tsv --out /tmp/prose.tsv
    uv run python scripts/prose_figure_audit.py kb/disorders/Tuberous_Sclerosis_Complex.yaml --format list
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so it resolves from src/.
from dismech.yaml_io import safe_load_path  # noqa: E402

CACHE_DIR = _REPO_ROOT / "references_cache"
RESEARCH_DIR = _REPO_ROOT / "research"

#: KB subtrees walked by default, relative to the repo root.
_KB_GLOBS = (
    "kb/disorders/*.yaml",
    "kb/modules/*.yaml",
    "kb/comorbidities/*.yaml",
    "kb/groupings/*.yaml",
)

#: Prose slots audited by default. These are the two the issue names: free text
#: that renders on the disorder page but is attached to no snippet.
_DEFAULT_KEYS = ("description", "notes")

#: Reference prefixes whose cache bodies are accessions, registrations or tables
#: rather than prose. A figure "missing" from a GEO accession record means
#: nothing, so these are not counted as searchable sources.
_NON_PROSE_PREFIXES = (
    "clinicaltrials:", "nct", "ictrp:",
    "url:", "http:", "https:",
    "geo:", "sra:", "bioproject:", "dbgap:", "gtex:",
    "metabolights:", "mtbls", "mgnify:", "mgys",
    "morphic:", "cellxgene:", "pride:", "massive:",
    "proteomexchange:", "osdr:", "nasa_osdr:", "genelab:",
)


# --------------------------------------------------------------------------
# Figure extraction
# --------------------------------------------------------------------------

#: A percentage, including the leading number of a range ("30-40%" -> 30 and 40).
_PCT = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(?:%|per\s?cent\b|percent\b)",
    re.IGNORECASE,
)
#: The unattached leading term of a percentage range: the "30" in "30-40%".
_PCT_RANGE_HEAD = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(?:-|–|—|\bto\b)\s*\d+(?:[.,]\d+)?\s*(?:%|per\s?cent\b|percent\b)",
    re.IGNORECASE,
)
_ONE_IN_N = re.compile(r"\b1\s*(?:in|:|/)\s*([\d][\d,\s]{2,})", re.IGNORECASE)
_PER_RATE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:per|/)\s*([\d][\d,\s]*(?:million|000))",
    re.IGNORECASE,
)
_FOLD = re.compile(r"(\d+(?:\.\d+)?)[\s-]*fold\b", re.IGNORECASE)


def _clean_number(raw: str) -> str:
    """Normalise a captured number to a bare comparable token.

    Thousands separators (comma, space, non-breaking space) are removed, a comma
    used as a decimal separator is converted to a point, and a trailing ``.0`` is
    dropped so ``40.0`` and ``40`` compare equal.
    """
    token = raw.replace(" ", "").replace("\xa0", "").replace(" ", "")
    # A comma with exactly one or two digits after it is a decimal separator
    # (European style); anything else is a thousands separator.
    if re.fullmatch(r"\d+,\d{1,2}", token):
        token = token.replace(",", ".")
    else:
        token = token.replace(",", "")
    if "." in token:
        token = token.rstrip("0").rstrip(".")
    return token or "0"


def _fmt(value: float) -> str:
    """Render a derived number the way the corpus is most likely to write it."""
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def equivalent_figures(token: str, kind: str) -> set[str]:
    """Return forms a source might legitimately use for the same quantity.

    A curator converting Orphanet's ``1 / 25 000`` into "4 per 100,000" has not
    invented anything, and flagging that would bury the real findings. Only the
    standard epidemiological conversions are covered; general arithmetic is not.
    """
    out = {token}
    try:
        value = float(token)
    except ValueError:
        return out
    if value == 0:
        return out
    if kind == "percent":
        out.add(_fmt(value / 100))          # 40%      -> 0.4
        out.add(_fmt(value * 1000))         # 40%      -> 40000 per 100,000
        # Deliberately NOT the "1 in N" reciprocal: 100/50 = 2, and a token that
        # small matches something in almost any abstract. It silently cleared a
        # real finding ("40-50% of TSC patients") during development.
    elif kind == "one_in_n":
        out.add(_fmt(100 / value))          # 1 in 25000 -> 0.004%
        out.add(_fmt(100_000 / value))      # 1 in 25000 -> 4 per 100,000
        out.add(_fmt(1_000_000 / value))    # 1 in 25000 -> 40 per million
    elif kind == "rate":
        # The denominator is not carried on the Figure, so cover both readings
        # ("per 100,000" and "per 1 million"). A superset is the safe direction:
        # it can only suppress a finding, never manufacture one.
        out.add(_fmt(value / 1000))         # 4 per 100,000  -> 0.004%
        out.add(_fmt(value / 10_000))       # 4 per 1,000,000 -> 0.0004%
        out.add(_fmt(100_000 / value))      # 4 per 100,000  -> 1 in 25,000
        out.add(_fmt(1_000_000 / value))    # 4 per 1,000,000 -> 1 in 250,000
    return {t for t in out if t}


@dataclass(frozen=True)
class Figure:
    """One quantity asserted in prose, with the forms that would satisfy it."""

    token: str
    kind: str
    context: str

    @property
    def candidates(self) -> set[str]:
        return equivalent_figures(self.token, self.kind)


#: A ``FrequencyEnum`` band definition quoted to justify a `frequency:` value, as
#: `docs/frequency-evidence-guidelines.md` asks curators to do. The numbers in
#: "falls in the FREQUENT band (30-79%)" are dismech's own enum boundaries, not
#: claims about the literature, and no cited paper will ever contain them.
_BAND_DEFINITION = re.compile(
    r"(?:OBLIGATE|VERY[_ ]FREQUENT|FREQUENT|OCCASIONAL|VERY[_ ]RARE|EXCLUDED)"
    r"[^.()]{0,30}\(\s*\d+\s*(?:-|–|—)\s*\d+\s*%\s*\)"
    r"|band\s*\(\s*\d+\s*(?:-|–|—)\s*\d+\s*%\s*\)",
    re.IGNORECASE,
)
#: A fraction the curator has shown their working for: "16/29 (55%)", "16 of 29".
_FRACTION = re.compile(r"\b(\d{1,5})\s*(?:/|\s+of\s+)\s*(\d{1,6})\b")


#: Slack, in percentage points, between a stated fraction and a stated percentage
#: before the percentage stops counting as derived from it. Deliberately looser
#: than pure rounding (13/29 is 44.8%, and curators write it as 45% or 46%):
#: a percentage the prose derives from a fraction it also states is *sourced* if
#: the fraction is, and whether the division was done exactly right is a
#: different and much smaller defect that this tool is not for.
_DERIVATION_TOLERANCE = 2.0


def _derived_percentages(text: str) -> list[float]:
    """Percentages the prose itself derives from a fraction it also states.

    "ID in 16 of 29 patients with available data (55%)" is not an unsourced
    figure — it is arithmetic on a number that *is* sourced, with the working
    shown. Flagging it punishes exactly the curation practice
    `docs/frequency-evidence-guidelines.md` asks for, and it is the dominant
    false positive without this.
    """
    out: list[float] = []
    for numerator, denominator in _FRACTION.findall(text):
        try:
            n, d = int(numerator), int(denominator)
        except ValueError:
            continue
        if d == 0 or n > d:
            continue
        out.append(100 * n / d)
    return out


def _context(text: str, start: int, end: int, width: int = 60) -> str:
    left = max(0, start - width)
    right = min(len(text), end + width)
    return re.sub(r"\s+", " ", text[left:right]).strip()


def extract_figures(text: str) -> list[Figure]:
    """Pull every unit-bearing quantity out of a block of prose.

    Two classes are excluded because they are not claims *about the literature*
    and so can never be found in it: ``FrequencyEnum`` band boundaries quoted to
    justify a `frequency:` value, and a percentage the prose derives from a
    fraction it also states.
    """
    band_spans = [m.span() for m in _BAND_DEFINITION.finditer(text)]
    derived = _derived_percentages(text)
    found: dict[tuple[str, str], Figure] = {}

    def add(token: str, kind: str, match: re.Match[str]) -> None:
        cleaned = _clean_number(token)
        if kind == "percent" and derived:
            try:
                value = float(cleaned)
            except ValueError:
                value = None
            if value is not None and any(
                abs(value - pct) <= _DERIVATION_TOLERANCE for pct in derived
            ):
                return
        if any(start <= match.start() < end for start, end in band_spans):
            return
        key = (cleaned, kind)
        if key not in found:
            found[key] = Figure(cleaned, kind, _context(text, match.start(), match.end()))

    for pattern, kind, group in (
        (_PCT, "percent", 1),
        (_PCT_RANGE_HEAD, "percent", 1),
        (_ONE_IN_N, "one_in_n", 1),
        (_FOLD, "fold", 1),
    ):
        for match in pattern.finditer(text):
            add(match.group(group), kind, match)
    for match in _PER_RATE.finditer(text):
        add(match.group(1), "rate", match)
    return list(found.values())


# --------------------------------------------------------------------------
# Reference cache
# --------------------------------------------------------------------------

_number_cache: dict[str, set[str] | None] = {}


def _cache_path_for(ref: str) -> Path | None:
    """Map a reference CURIE to its cache file, mirroring the validator's naming."""
    stem = ref.replace(":", "_").replace("/", "_")
    candidate = CACHE_DIR / f"{stem}.md"
    if candidate.exists():
        return candidate
    lower = CACHE_DIR / f"{stem.lower()}.md"
    return lower if lower.exists() else None


def strip_frontmatter(text: str) -> str:
    """Reduce a cache file to its quotable body, as ``check_snippets_verbatim`` does.

    Two headers have to go, not one. The YAML block and the restated
    title/authors/journal preamble before ``## Content`` are dense with numbers
    that are not findings: DOIs, the PMID itself, publication years, volume and
    page ranges, even postal codes in an affiliation. Left in, they clear real
    claims by coincidence — during development ``50`` in "40-50% of TSC patients"
    verified against ``PMID:38991206`` purely on the ``2`` inside its DOI.

    Structured-source caches (``ORPHA_*``, ``CGGV_*``, ``ICEES_*``) have no
    ``## Content`` marker and their tables *are* the quotable content, so
    everything after the YAML block is kept.
    """
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    marker = text.find("## Content")
    if marker != -1:
        text = _strip_bibliographic_noise(text[marker + len("## Content"):])
    return text


#: Lines inside a fetched ``## Content`` block that are bibliographic apparatus
#: rather than findings. Each is a measured coincidence generator: the NLM
#: citation line contributes the year, volume and page range; the affiliation
#: block contributed "15" (Francis Street) and "02115" (a Boston postal code) to
#: PMID:27226234; the byline contributes small integers 1-9 as author markers,
#: which are exactly the tokens a low single-digit percentage collides with.
_NOISE_LINE = re.compile(
    r"""^(?:
          \s*\d+\.\s.*\bdoi:\s                # 1. Nat Rev Dis Primers. 2016 ... doi: ...
        | \s*Author\s+information:\s*$
        | \s*\(\d+\).*                        # (1)Pulmonary and Critical Care ...
        | \s*(?:DOI|PMID|PMCID):\s
        | \s*(?:Conflict\s+of\s+interest|Copyright|Comment\s+in|Erratum\s+in)\b
      )""",
    re.IGNORECASE | re.VERBOSE,
)
#: An author byline carries three or more parenthesised affiliation markers.
_AFFIL_MARKER = re.compile(r"\(\d+\)")


def _strip_bibliographic_noise(body: str) -> str:
    """Drop citation, byline and affiliation lines from a fetched abstract body.

    Both the leading NLM citation and the affiliation list are *blocks* that wrap
    across lines, so each is consumed to its terminating blank line rather than
    line by line: PMID:38991206's citation continues onto a second line holding
    only ``10.1590/2175-8239-JBN-2024-0013en. eCollection 2024.``
    """
    kept: list[str] = []
    in_affiliations = False
    in_citation = False
    seen_content = False
    for line in body.splitlines():
        if not seen_content and line.strip():
            seen_content = True
            if re.match(r"\s*\d+\.\s\S", line):
                in_citation = True
        if in_citation:
            if line.strip():
                continue
            in_citation = False
        if re.match(r"\s*Author\s+information:", line, re.IGNORECASE):
            in_affiliations = True
            continue
        if in_affiliations:
            # Affiliations wrap across lines, so a continuation does not start
            # with "(N)". The run ends at the blank line before the abstract.
            if line.strip():
                continue
            in_affiliations = False
        if _NOISE_LINE.match(line) or len(_AFFIL_MARKER.findall(line)) >= 3:
            continue
        kept.append(line)
    return "\n".join(kept)


def reference_numbers(ref: str) -> set[str] | None:
    """Every numeric token in a cached reference body, or ``None`` if not cached."""
    if ref in _number_cache:
        return _number_cache[ref]
    path = _cache_path_for(ref)
    if path is None:
        _number_cache[ref] = None
        return None
    try:
        text = strip_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        _number_cache[ref] = None
        return None
    # Lancet/BMJ house style writes decimals with a middle dot ("61·4%").
    text = re.sub(r"(?<=\d)[·•](?=\d)", ".", text)
    text = re.sub(r"(?<=\d)[, \xa0 ](?=\d{3}\b)", "", text)
    numbers = {_clean_number(tok) for tok in re.findall(r"\d+(?:\.\d+)?", text)}
    _number_cache[ref] = numbers
    return numbers


def _is_prose_reference(ref: str) -> bool:
    lowered = ref.lower()
    return not any(lowered.startswith(p) for p in _NON_PROSE_PREFIXES)


# --------------------------------------------------------------------------
# YAML walking
# --------------------------------------------------------------------------

def collect_references(node: object, out: set[str]) -> None:
    """Gather every ``reference:`` value anywhere in the document."""
    if isinstance(node, dict):
        ref = node.get("reference")
        if isinstance(ref, str) and ref.strip():
            out.add(ref.strip())
        for value in node.values():
            collect_references(value, out)
    elif isinstance(node, list):
        for item in node:
            collect_references(item, out)


def _own_evidence_refs(node: dict) -> set[str]:
    """References cited by this mapping's *own* ``evidence:`` list, if any."""
    refs: set[str] = set()
    evidence = node.get("evidence")
    if isinstance(evidence, list):
        for item in evidence:
            if isinstance(item, dict):
                ref = item.get("reference")
                if isinstance(ref, str) and ref.strip():
                    refs.add(ref.strip())
    return refs


def iter_prose(
    node: object,
    keys: tuple[str, ...],
    path: str = "",
    scope: frozenset[str] = frozenset(),
) -> list[tuple[str, str, frozenset[str]]]:
    """Yield ``(dotted-path, text, adjacent-references)`` for every prose slot.

    ``scope`` is the reference set of the nearest ancestor-or-self mapping that
    carries an ``evidence:`` list. A phenotype's ``description`` and its
    ``evidence`` are siblings, so the common case resolves to exactly the
    citations a reader would take that description to rest on.
    """
    hits: list[tuple[str, str, frozenset[str]]] = []
    if isinstance(node, dict):
        own = _own_evidence_refs(node)
        here_scope = frozenset(own) if own else scope
        for key, value in node.items():
            here = f"{path}.{key}" if path else str(key)
            if key == "evidence":
                # Evidence items carry their own prose (``explanation``), which is
                # snippet-adjacent by construction and out of scope for #7791.
                continue
            if key in keys and isinstance(value, str):
                hits.append((here, value, here_scope))
            elif key in keys and isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, str):
                        hits.append((f"{here}[{i}]", item, here_scope))
            else:
                hits.extend(iter_prose(value, keys, here, here_scope))
    elif isinstance(node, list):
        for i, item in enumerate(node):
            hits.extend(iter_prose(item, keys, f"{path}[{i}]", scope))
    return hits


@dataclass
class Finding:
    file: str
    slot: str
    figure: str
    kind: str
    context: str
    verdict: str          # NOT_IN_ADJACENT | UNCITED
    adjacent_cached: int  # cached references in the adjacent evidence block
    in_entry_corpus: bool


@dataclass
class FileReport:
    path: Path
    name: str
    has_dr_artifact: bool
    cited: int = 0
    cached: int = 0
    figures: int = 0
    findings: list[Finding] = field(default_factory=list)

    @property
    def misattributions(self) -> list[Finding]:
        """Figures contradicted by their own adjacent citation — the #7791 shape."""
        return [f for f in self.findings if f.verdict == "NOT_IN_ADJACENT"]

    @property
    def uncited(self) -> list[Finding]:
        return [f for f in self.findings if f.verdict == "UNCITED"]

    @property
    def status(self) -> str:
        if self.figures == 0:
            return "NO_FIGURES"
        if self.misattributions:
            return "NOT_IN_ADJACENT"
        if self.uncited:
            return "UNCITED"
        return "OK"


def _dr_artifact_stems() -> set[str]:
    """Entry stems that have at least one deep-research report in ``research/``."""
    stems: set[str] = set()
    if not RESEARCH_DIR.is_dir():
        return stems
    for path in RESEARCH_DIR.glob("*-deep-research-*.md"):
        stems.add(path.name.split("-deep-research-")[0])
    return stems


def audit_file(path: Path, keys: tuple[str, ...], dr_stems: set[str]) -> FileReport:
    doc = safe_load_path(path)
    report = FileReport(
        path=path,
        name=str(doc.get("name") or path.stem) if isinstance(doc, dict) else path.stem,
        has_dr_artifact=path.stem in dr_stems,
    )
    if not isinstance(doc, dict):
        return report

    refs: set[str] = set()
    collect_references(doc, refs)
    prose_refs = {r for r in refs if _is_prose_reference(r)}
    report.cited = len(prose_refs)

    entry_corpus: set[str] = set()
    for ref in sorted(prose_refs):
        numbers = reference_numbers(ref)
        if numbers is None:
            continue
        report.cached += 1
        entry_corpus |= numbers

    scope_cache: dict[frozenset[str], tuple[set[str], int]] = {}

    def resolve(scope: frozenset[str]) -> tuple[set[str], int]:
        """Numeric tokens reachable from an adjacent evidence block, and its size."""
        if scope not in scope_cache:
            numbers: set[str] = set()
            cached = 0
            for ref in scope:
                if not _is_prose_reference(ref):
                    continue
                found = reference_numbers(ref)
                if found is None:
                    continue
                cached += 1
                numbers |= found
            scope_cache[scope] = (numbers, cached)
        return scope_cache[scope]

    for slot, text, scope in iter_prose(doc, keys):
        adjacent, adjacent_cached = resolve(scope)
        for figure in extract_figures(text):
            report.figures += 1
            if figure.candidates & adjacent:
                continue
            # No adjacent *cached prose* source at all: the claim is uncited
            # rather than contradicted, so say so instead of overstating it.
            verdict = "NOT_IN_ADJACENT" if adjacent_cached else "UNCITED"
            report.findings.append(
                Finding(
                    file=str(path.relative_to(_REPO_ROOT)),
                    slot=slot,
                    figure=figure.token,
                    kind=figure.kind,
                    context=figure.context,
                    verdict=verdict,
                    adjacent_cached=adjacent_cached,
                    in_entry_corpus=bool(figure.candidates & entry_corpus),
                )
            )
    return report


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def _iter_targets(explicit: list[str]) -> list[Path]:
    if explicit:
        return [Path(p).resolve() for p in explicit]
    paths: list[Path] = []
    for pattern in _KB_GLOBS:
        paths.extend(sorted(_REPO_ROOT.glob(pattern)))
    return paths


def render_summary(reports: list[FileReport], out) -> None:
    counts = Counter(r.status for r in reports)
    misattr = [f for r in reports for f in r.misattributions]
    uncited = [f for r in reports for f in r.uncited]
    hard = [f for f in misattr if not f.in_entry_corpus]
    flagged = [r for r in reports if r.misattributions]
    dr_flagged = [r for r in flagged if r.has_dr_artifact]
    total_figures = sum(r.figures for r in reports)

    print("Prose figure audit (advisory; see issue #7791)", file=out)
    print("=" * 66, file=out)
    print(f"  entries scanned                       : {len(reports)}", file=out)
    print(f"  quantitative figures in prose         : {total_figures}", file=out)
    print("", file=out)
    print(f"  NOT_IN_ADJACENT (cited, not supported): {len(misattr)}", file=out)
    print(f"    ...and absent entry-wide too        : {len(hard)}", file=out)
    print(f"  UNCITED (no adjacent evidence at all) : {len(uncited)}", file=out)
    print("", file=out)
    print(f"  entries with >=1 NOT_IN_ADJACENT      : {len(flagged)}", file=out)
    print(f"    ...with a DR report in research/    : {len(dr_flagged)}", file=out)
    print("", file=out)
    for status in ("OK", "NOT_IN_ADJACENT", "UNCITED", "NO_FIGURES"):
        print(f"  {status:<20} {counts.get(status, 0)}", file=out)

    if not flagged:
        return
    print("", file=out)
    print("Highest NOT_IN_ADJACENT counts (DR-backed entries first):", file=out)
    ranked = sorted(
        flagged, key=lambda r: (not r.has_dr_artifact, -len(r.misattributions), r.name)
    )
    for report in ranked[:25]:
        marker = "DR" if report.has_dr_artifact else "  "
        print(
            f"  [{marker}] {len(report.misattributions):>3}  "
            f"{report.path.relative_to(_REPO_ROOT)}",
            file=out,
        )
    by_kind = Counter(f.kind for f in misattr)
    print("", file=out)
    print("By figure kind: " + ", ".join(f"{k}={v}" for k, v in by_kind.most_common()), file=out)


def render_list(reports: list[FileReport], out) -> None:
    """Print the actionable findings only — NOT_IN_ADJACENT, strongest first."""
    ranked = sorted(
        (r for r in reports if r.misattributions),
        key=lambda r: (not r.has_dr_artifact, r.name),
    )
    for report in ranked:
        for finding in sorted(report.misattributions, key=lambda f: f.in_entry_corpus):
            tag = "" if finding.in_entry_corpus else "  [absent entry-wide]"
            print(
                f"{finding.file}\t{finding.slot}\t{finding.kind}\t{finding.figure}{tag}",
                file=out,
            )
            print(f"    ...{finding.context}...", file=out)


def render_tsv(reports: list[FileReport], out) -> None:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "file", "entry", "has_dr_report", "verdict", "in_entry_corpus",
        "adjacent_cached_refs", "slot", "kind", "figure", "context",
    ])
    for report in reports:
        for finding in report.findings:
            writer.writerow([
                finding.file, report.name, "yes" if report.has_dr_artifact else "no",
                finding.verdict, "yes" if finding.in_entry_corpus else "no",
                finding.adjacent_cached, finding.slot, finding.kind,
                finding.figure, finding.context,
            ])


def render_json(reports: list[FileReport], out) -> None:
    payload = [
        {
            "file": str(r.path.relative_to(_REPO_ROOT)),
            "entry": r.name,
            "has_dr_report": r.has_dr_artifact,
            "status": r.status,
            "cited_prose_references": r.cited,
            "cached_references": r.cached,
            "prose_figures": r.figures,
            "findings": [
                {
                    "slot": f.slot, "kind": f.kind, "figure": f.figure,
                    "verdict": f.verdict, "in_entry_corpus": f.in_entry_corpus,
                    "adjacent_cached_refs": f.adjacent_cached, "context": f.context,
                }
                for f in r.findings
            ],
        }
        for r in reports
        if r.findings
    ]
    json.dump(payload, out, indent=2)
    out.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("paths", nargs="*", help="Specific YAML files (default: the whole KB).")
    parser.add_argument(
        "--format", choices=("summary", "list", "tsv", "json"), default="summary",
    )
    parser.add_argument("--out", help="Write to this file instead of stdout.")
    parser.add_argument(
        "--dr-only", action="store_true",
        help="Only entries with a deep-research report in research/ — the #7791 blast radius.",
    )
    parser.add_argument(
        "--keys", default=",".join(_DEFAULT_KEYS),
        help=f"Comma-separated prose slots to audit (default: {','.join(_DEFAULT_KEYS)}).",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 on any NOT_IN_ADJACENT finding. Off by default: this is advisory.",
    )
    args = parser.parse_args(argv)

    keys = tuple(k.strip() for k in args.keys.split(",") if k.strip())
    dr_stems = _dr_artifact_stems()
    targets = _iter_targets(args.paths)
    if args.dr_only:
        targets = [p for p in targets if p.stem in dr_stems]

    reports = [audit_file(path, keys, dr_stems) for path in targets]

    stream = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    try:
        {"summary": render_summary, "list": render_list,
         "tsv": render_tsv, "json": render_json}[args.format](reports, stream)
    finally:
        if args.out:
            stream.close()
            print(f"Wrote {args.out}", file=sys.stderr)

    if args.strict and any(r.misattributions for r in reports):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
