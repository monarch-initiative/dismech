#!/usr/bin/env python3
"""Report deep-research reports that name a MONDO CURIE for a different disease.

A report's own ``## Term Validation`` section compares a CURIE with a label only
when the report prints a label next to it. The disease's own MONDO term is most
often printed bare, in a "Key identifiers:" list, so a wrong one passes with
``confabulation_rate: 0.0`` (#9949). The ADH1 report named ``MONDO:0008833``,
which is renal-hepatic-pancreatic dysplasia 1, and nothing flagged it.

For each ``research/<Slug>-deep-research-<provider>.md`` this script works out
the MONDO term the report should be about, from ``kb/disorders/<Slug>.yaml``
``disease_term.term.id`` or else ``stubs/<Slug>.yaml`` ``mondo_id``, and compares
every MONDO CURIE the report names against it:

``OK``
    Every cited CURIE is the expected term, or its cached label shares a content
    word with the expected label. A grouping report citing its own subtypes
    lands here, because the subtype labels repeat the group's name.
``MISMATCH``
    At least one cited CURIE has a cached label sharing no content word with the
    expected label. This is a lead, not a verdict: a report can legitimately
    name a differential diagnosis or a comorbidity.
``UNCACHED``
    No mismatch, but the expected term or a cited CURIE has no row in
    ``cache/mondo/terms.csv``, so the comparison is incomplete.
``SKIPPED``
    No expected term could be resolved for the slug, or the report names no
    MONDO CURIE at all.

Labels come from ``cache/mondo/terms.csv`` only. Nothing is fetched, nothing is
written under ``research/``, and the exit status is 0 whatever is found.

Usage:
    scripts/dr_mondo_audit.py
    scripts/dr_mondo_audit.py research/Autosomal_Dominant_Hypocalcemia_1-deep-research-openscientist.md
    scripts/dr_mondo_audit.py --format tsv --out /tmp/dr_mondo.tsv
    scripts/dr_mondo_audit.py --format json
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path

from dismech import kb_cache
from dismech.yaml_io import safe_load_path

REPORT_MARKER = "-deep-research-"
MONDO_RE = re.compile(r"\bMONDO[:_](\d{7})\b", re.IGNORECASE)
_TOKEN_RE = re.compile(r"[a-z0-9]+")

# Words that say what kind of disease a label names rather than which one.
# Two unrelated labels routinely share these ("bone Paget disease" and "Cushing
# disease due to pituitary adenoma"), so counting them would hide every mismatch.
GENERIC_WORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "associated",
        "autosomal",
        "by",
        "caused",
        "congenital",
        "deficiency",
        "disease",
        "disorder",
        "dominant",
        "due",
        "familial",
        "for",
        "form",
        "from",
        "hereditary",
        "in",
        "inherited",
        "linked",
        "obsolete",
        "of",
        "or",
        "primary",
        "recessive",
        "related",
        "syndrome",
        "the",
        "to",
        "type",
        "with",
        "without",
        "x",
    }
)

STATUSES = ("OK", "MISMATCH", "UNCACHED", "SKIPPED")


@dataclass
class CitedTerm:
    curie: str
    label: str | None
    lines: list[int]
    verdict: str  # EXPECTED, RELATED, MISMATCH, UNCACHED


@dataclass
class ReportResult:
    report: str
    slug: str
    expected_id: str | None
    expected_source: str | None
    expected_label: str | None
    status: str
    reason: str
    cited: list[CitedTerm] = field(default_factory=list)

    @property
    def mismatches(self) -> list[CitedTerm]:
        return [term for term in self.cited if term.verdict == "MISMATCH"]


def content_tokens(label: str) -> set[str]:
    """Return the words of a label that identify the disease.

    Digits are dropped as well as generic words: "1" is shared by every first
    numbered subtype and says nothing about which disease is meant.
    """
    return {
        token
        for token in _TOKEN_RE.findall(label.lower())
        if token not in GENERIC_WORDS and not token.isdigit() and len(token) > 1
    }


def load_labels(cache_path: Path) -> dict[str, str]:
    labels: dict[str, str] = {}
    if not cache_path.exists():
        return labels
    with cache_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            curie = (row.get("curie") or "").strip().upper()
            label = (row.get("label") or "").strip()
            if curie and label:
                labels[curie] = label
    return labels


def report_slug(path: Path) -> str | None:
    name = path.name
    if REPORT_MARKER not in name:
        return None
    return name.split(REPORT_MARKER, 1)[0]


def iter_reports(research_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in research_dir.glob(f"*{REPORT_MARKER}*.md")
        if path.is_file() and not path.name.endswith(".citations.md")
    )


def extract_mondo_curies(text: str) -> dict[str, list[int]]:
    """Map each MONDO CURIE in ``text`` to the 1-based lines it appears on."""
    found: dict[str, list[int]] = {}
    for lineno, line in enumerate(text.splitlines(), start=1):
        for match in MONDO_RE.finditer(line):
            curie = f"MONDO:{match.group(1)}"
            lines = found.setdefault(curie, [])
            if not lines or lines[-1] != lineno:
                lines.append(lineno)
    return found


def _kb_disease_term(path: Path) -> str | None:
    try:
        document = safe_load_path(path)
    except Exception:  # an unparsable entry is some other gate's finding
        return None
    if not isinstance(document, dict):
        return None
    term = (document.get("disease_term") or {}).get("term") or {}
    curie = term.get("id") if isinstance(term, dict) else None
    return str(curie).strip().upper() if curie else None


def _stub_mondo_id(path: Path) -> str | None:
    try:
        document = safe_load_path(path)
    except Exception:
        return None
    if not isinstance(document, dict) or not document.get("mondo_id"):
        return None
    return str(document["mondo_id"]).strip().upper()


class ExpectedResolver:
    """Resolve a slug to the MONDO term its entry or stub records, once per slug."""

    def __init__(self, kb_dir: Path, stubs_dir: Path) -> None:
        self.kb_dir = kb_dir
        self.stubs_dir = stubs_dir
        self._memo: dict[str, tuple[str | None, str | None]] = {}

    def resolve(self, slug: str) -> tuple[str | None, str | None]:
        if slug not in self._memo:
            self._memo[slug] = self._resolve(slug)
        return self._memo[slug]

    def _resolve(self, slug: str) -> tuple[str | None, str | None]:
        entry = self.kb_dir / f"{slug}.yaml"
        if entry.exists():
            curie = _kb_disease_term(entry)
            if curie and curie.startswith("MONDO:"):
                return curie, str(entry)
        stub = self.stubs_dir / f"{slug}.yaml"
        if stub.exists():
            curie = _stub_mondo_id(stub)
            if curie and curie.startswith("MONDO:"):
                return curie, str(stub)
        return None, None


def assess_report(
    path: Path,
    resolver: ExpectedResolver,
    labels: dict[str, str],
    display_root: Path | None = None,
) -> ReportResult:
    slug = report_slug(path) or path.stem
    shown = str(path)
    if display_root is not None:
        try:
            shown = str(path.resolve().relative_to(display_root.resolve()))
        except ValueError:
            pass
    expected_id, expected_source = resolver.resolve(slug)
    if display_root is not None and expected_source:
        try:
            expected_source = str(
                Path(expected_source).resolve().relative_to(display_root.resolve())
            )
        except ValueError:
            pass
    result = ReportResult(
        report=shown,
        slug=slug,
        expected_id=expected_id,
        expected_source=expected_source,
        expected_label=labels.get(expected_id) if expected_id else None,
        status="SKIPPED",
        reason="",
    )
    if expected_id is None:
        result.reason = (
            "no kb/disorders or stubs/ file records a MONDO term for this slug"
        )
        return result

    found = extract_mondo_curies(path.read_text(encoding="utf-8", errors="replace"))
    if not found:
        result.reason = "the report names no MONDO CURIE"
        return result

    expected_tokens = (
        content_tokens(result.expected_label) if result.expected_label else None
    )
    for curie, lines in sorted(found.items()):
        label = labels.get(curie)
        if curie == expected_id:
            verdict = "EXPECTED"
        elif label is None or expected_tokens is None:
            verdict = "UNCACHED"
        elif content_tokens(label) & expected_tokens:
            verdict = "RELATED"
        else:
            verdict = "MISMATCH"
        result.cited.append(
            CitedTerm(curie=curie, label=label, lines=lines, verdict=verdict)
        )

    if result.mismatches:
        result.status = "MISMATCH"
        result.reason = (
            "a cited MONDO label shares no content word with the expected label"
        )
    elif result.expected_label is None:
        result.status = "UNCACHED"
        result.reason = (
            f"expected term {expected_id} has no row in cache/mondo/terms.csv"
        )
    elif any(term.verdict == "UNCACHED" for term in result.cited):
        result.status = "UNCACHED"
        result.reason = "a cited MONDO CURIE has no row in cache/mondo/terms.csv"
    else:
        result.status = "OK"
    return result


def audit(
    reports: list[Path],
    kb_dir: Path,
    stubs_dir: Path,
    cache_path: Path,
    display_root: Path | None = None,
) -> list[ReportResult]:
    labels = load_labels(cache_path)
    resolver = ExpectedResolver(kb_dir, stubs_dir)
    return [assess_report(path, resolver, labels, display_root) for path in reports]


def summarize(results: list[ReportResult]) -> dict[str, int]:
    counts = Counter(result.status for result in results)
    return {status: counts.get(status, 0) for status in STATUSES}


def format_text(results: list[ReportResult]) -> str:
    summary = summarize(results)
    out = [f"dr-mondo-audit: {len(results)} deep-research reports"]
    out.extend(f"  {status:<9} {summary[status]}" for status in STATUSES)
    skipped = Counter(result.reason for result in results if result.status == "SKIPPED")
    out.extend(f"    {count:>6}  {reason}" for reason, count in sorted(skipped.items()))
    mismatched = [result for result in results if result.status == "MISMATCH"]
    if mismatched:
        out.append("")
        out.append(
            "MISMATCH rows (a lead to read, not a verdict: a report may name a "
            "differential diagnosis or a comorbidity):"
        )
        for result in mismatched:
            out.append(
                f"{result.report}\n  expected {result.expected_id} "
                f"{result.expected_label!r} (from {result.expected_source})"
            )
            for term in result.mismatches:
                lines = ",".join(str(line) for line in term.lines)
                out.append(f"  cited    {term.curie} {term.label!r} (line {lines})")
    return "\n".join(out) + "\n"


def format_tsv(results: list[ReportResult]) -> str:
    header = (
        "report",
        "slug",
        "status",
        "expected_id",
        "expected_label",
        "expected_source",
        "cited_count",
        "mismatched",
        "uncached",
        "reason",
    )
    rows = ["\t".join(header)]
    for result in results:
        mismatched = "; ".join(
            f"{term.curie}={term.label}" for term in result.mismatches
        )
        uncached = "; ".join(
            term.curie for term in result.cited if term.verdict == "UNCACHED"
        )
        rows.append(
            "\t".join(
                (
                    result.report,
                    result.slug,
                    result.status,
                    result.expected_id or "",
                    result.expected_label or "",
                    result.expected_source or "",
                    str(len(result.cited)),
                    mismatched,
                    uncached,
                    result.reason,
                )
            )
        )
    return "\n".join(rows) + "\n"


def format_json(results: list[ReportResult]) -> str:
    payload = {
        "summary": summarize(results),
        "reports": [asdict(result) for result in results],
    }
    return json.dumps(payload, indent=2) + "\n"


def main(argv: list[str] | None = None) -> int:
    # One pass over the entries the reports name; nothing is read twice, so the
    # parsed-KB cache would be pure cost (CLAUDE.md, "Parsed-KB Cache").
    kb_cache.default_off()
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "reports",
        nargs="*",
        type=Path,
        help="specific reports to audit (default: every research/*-deep-research-*.md)",
    )
    parser.add_argument("--root", type=Path, default=Path("."), help="repository root")
    parser.add_argument("--format", choices=("text", "tsv", "json"), default="text")
    parser.add_argument(
        "--out", type=Path, help="write the report here instead of stdout"
    )
    args = parser.parse_args(argv)

    root = args.root
    reports = args.reports or iter_reports(root / "research")
    results = audit(
        reports,
        kb_dir=root / "kb" / "disorders",
        stubs_dir=root / "stubs",
        cache_path=root / "cache" / "mondo" / "terms.csv",
        display_root=root,
    )
    formatter = {"text": format_text, "tsv": format_tsv, "json": format_json}[
        args.format
    ]
    rendered = formatter(results)
    if args.out:
        args.out.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
