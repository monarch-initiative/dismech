"""Audit non-ClinicalTrials.gov trial registry identifiers in the knowledge base.

``clinical_trials`` grew up around ClinicalTrials.gov: ``name`` holds an
``NCT…`` identifier and evidence resolves against the ClinicalTrials.gov API.
A trial registered anywhere else had nowhere to go, so its identifier ended up
in one of three unvalidated shapes:

``STRANDED``
    the identifier appears only in prose (a ``description:``, ``notes:``, or
    evidence ``snippet:``) — invisible to any query over trials
``TRIAL_NAME``
    the identifier is the trial's ``name`` (bare, or embedded in free text like
    ``ML-DS 2006 (EudraCT 2007-006219-2)``) — queryable but unverified, which
    is how a nonexistent ``ChiCTR-2100045397`` survived in the KB
``CITED``
    the trial is cited as ``ICTRP:<TrialID>`` with a cache file backing it —
    snippet-validated like any other reference

This reports which is which. It is advisory: an identifier quoted inside an
evidence ``snippet:`` is often a faithful transcription of what the cited paper
printed (errors included) and must not be "corrected" in place — the fix is to
add an ``ICTRP:`` evidence item alongside it.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_KB = _REPO_ROOT / "kb"
_DEFAULT_CACHE = _REPO_ROOT / "references_cache"

# Registry identifier shapes seen in the wild. EudraCT is included even though
# ICTRP keys those records as ``EUCTR<number>-<country>``: curators write the
# EudraCT form, and knowing it is present is the point of the audit.
_PATTERNS: tuple[tuple[str, re.Pattern], ...] = (
    ("ChiCTR", re.compile(r"\bChiCTR[- ]?[A-Za-z]{0,3}-?\d{6,}\b")),
    ("ISRCTN", re.compile(r"\bISRCTN\s?\d{6,}\b")),
    (
        "EudraCT",
        re.compile(r"\b(?:EudraCT|EUCTR)\s?\d{4}-\d{6}-\d{1,2}(?:-[A-Z]{2})?\b"),
    ),
    ("UMIN", re.compile(r"\b(?:JPRN-)?UMIN\s?\d{6,}\b")),
    ("jRCT", re.compile(r"\b(?:JPRN-)?jRCTs?\d{6,}\b")),
    ("CTRI", re.compile(r"\bCTRI/\d{4}/\d{2}/\d{4,}\b")),
    ("ANZCTR", re.compile(r"\bACTRN\d{10,}\b")),
    ("IRCT", re.compile(r"\bIRCT\d{6,}[A-Za-z0-9]*\b")),
    ("DRKS", re.compile(r"\bDRKS\d{6,}\b")),
    ("PACTR", re.compile(r"\bPACTR\d{10,}\b")),
    ("TCTR", re.compile(r"\bTCTR\d{8,}\b")),
    ("KCT", re.compile(r"\bKCT\d{7,}\b")),
    ("RBR", re.compile(r"\bRBR-[A-Za-z0-9]{6,}\b")),
    ("NTR", re.compile(r"\bNTR\d{4,}\b")),
    ("SLCTR", re.compile(r"\bSLCTR/\d{4}/\d{3,}\b")),
    # A bare EudraCT number, for prose that names the registry a few words
    # earlier ("Registered on EudraCT as 2018-004611-50"). Kept last so a
    # prefixed match above wins the same span.
    ("EudraCT", re.compile(r"\b\d{4}-\d{6}-\d{2}\b")),
)

_ICTRP_REFERENCE = re.compile(r"reference:\s*ICTRP:(\S+)")
_TRIAL_NAME_LINE = re.compile(r"^-\s+name:\s*(.+?)\s*$")


@dataclass(frozen=True)
class Hit:
    """One registry identifier occurrence."""

    path: Path
    line_number: int
    registry: str
    identifier: str
    placement: str  # STRANDED | TRIAL_NAME | CITED

    @property
    def relative_path(self) -> str:
        try:
            return str(self.path.relative_to(_REPO_ROOT))
        except ValueError:
            return str(self.path)


def _cached_ictrp_ids(cache_dir: Path) -> set[str]:
    """Trial identifiers with an ``ICTRP_*.md`` cache file."""
    if not cache_dir.is_dir():
        return set()
    return {path.stem[len("ICTRP_") :] for path in cache_dir.glob("ICTRP_*.md")}


def _in_clinical_trials_block(lines: list[str], index: int) -> bool:
    """True when ``lines[index]`` sits under a top-level ``clinical_trials:``.

    Scans backwards for the nearest top-level (column-zero) key; the block is
    ``clinical_trials`` if that key is the one we find.
    """
    for line in reversed(lines[: index + 1]):
        if line and not line[0].isspace() and line.rstrip().endswith(":"):
            return line.startswith("clinical_trials:")
    return False


def scan_file(path: Path, cited: set[str]) -> list[Hit]:
    """Find registry identifiers in one YAML file."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    file_citations = {
        identifier.strip("\"'") for identifier in _ICTRP_REFERENCE.findall(text)
    }
    hits: list[Hit] = []
    for index, line in enumerate(lines):
        # Spans already claimed on this line, so a bare-number pattern cannot
        # re-report the tail of an identifier a prefixed pattern already matched.
        claimed: list[tuple[int, int]] = []
        for registry, pattern in _PATTERNS:
            for match in pattern.finditer(line):
                start, end = match.span()
                if any(start >= c_start and end <= c_end for c_start, c_end in claimed):
                    continue
                claimed.append((start, end))
                identifier = " ".join(match.group(0).split())
                name_match = _TRIAL_NAME_LINE.match(line.strip())
                if identifier in file_citations and identifier in cited:
                    placement = "CITED"
                elif name_match and _in_clinical_trials_block(lines, index):
                    placement = "TRIAL_NAME"
                else:
                    placement = "STRANDED"
                hits.append(
                    Hit(
                        path=path,
                        line_number=index + 1,
                        registry=registry,
                        identifier=identifier,
                        placement=placement,
                    )
                )
    return hits


def scan(kb_dir: Path, cache_dir: Path) -> list[Hit]:
    """Scan every KB YAML file for registry identifiers."""
    cited = _cached_ictrp_ids(cache_dir)
    hits: list[Hit] = []
    for path in sorted(kb_dir.rglob("*.yaml")):
        hits.extend(scan_file(path, cited))
    return hits


def format_summary(hits: list[Hit]) -> str:
    """Human-readable census grouped by placement."""
    if not hits:
        return "No non-ClinicalTrials.gov registry identifiers found."
    by_placement: dict[str, list[Hit]] = defaultdict(list)
    for hit in hits:
        by_placement[hit.placement].append(hit)
    by_registry: dict[str, int] = defaultdict(int)
    for hit in hits:
        by_registry[hit.registry] += 1

    distinct = {hit.identifier for hit in hits}
    out: list[str] = []
    out.append(
        f"{len(hits)} non-ClinicalTrials.gov registry identifier occurrence(s), "
        f"{len(distinct)} distinct"
    )
    out.append("")
    out.append("By registry:")
    for registry, count in sorted(by_registry.items(), key=lambda kv: (-kv[1], kv[0])):
        out.append(f"  {registry:<10} {count}")
    out.append("")
    for placement in ("TRIAL_NAME", "STRANDED", "CITED"):
        group = by_placement.get(placement, [])
        out.append(f"{placement} ({len(group)})")
        for hit in group:
            out.append(f"  {hit.relative_path}:{hit.line_number}  {hit.identifier}")
        out.append("")
    out.append(
        "Fix: `just ictrp-fetch <TrialID>` then cite `ICTRP:<TrialID>` in the "
        "trial's evidence. Do NOT rewrite an identifier inside an evidence "
        "snippet - that quote belongs to the cited paper."
    )
    return "\n".join(out)


def format_tsv(hits: list[Hit]) -> str:
    """Tab-delimited output for downstream processing."""
    rows = ["file\tline\tregistry\tidentifier\tplacement"]
    rows.extend(
        f"{hit.relative_path}\t{hit.line_number}\t{hit.registry}\t"
        f"{hit.identifier}\t{hit.placement}"
        for hit in hits
    )
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--kb-dir", type=Path, default=_DEFAULT_KB, help="KB root to scan"
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=_DEFAULT_CACHE,
        help="references_cache directory",
    )
    parser.add_argument(
        "--format", choices=("summary", "tsv"), default="summary", help="output format"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 if any identifier is not cited as ICTRP:<TrialID>",
    )
    args = parser.parse_args(argv)

    hits = scan(args.kb_dir, args.cache_dir)
    print(format_tsv(hits) if args.format == "tsv" else format_summary(hits))
    if args.strict and any(hit.placement != "CITED" for hit in hits):
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
