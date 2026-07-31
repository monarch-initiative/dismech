"""Helpers for cross-provider research-synthesis artifacts.

Two things the LinkML schema cannot express on its own:

1. ``derive_consensus`` computes a finding's consensus from its provider
   stances, so consensus is never hand-authored (it is a pure function of the
   ``provider_support`` stances).
2. ``iter_quote_problems`` enforces that every ``best_matching_text`` is a
   verbatim (whitespace-normalized) substring of the provider report it claims
   to quote — the anti-fabrication guarantee, analogous to
   ``validate-references`` checking evidence snippets against abstracts.

Run as a module to check one or more synthesis files::

    uv run python -m dismech.research_synthesis research/*-research-synthesis.yaml
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable
from functools import cache
from pathlib import Path

import yaml

_WS = re.compile(r"\s+")


def _norm(text: str) -> str:
    """Collapse all whitespace runs to a single space and strip."""
    return _WS.sub(" ", text).strip()


def derive_consensus(finding: dict) -> str:
    """Derive the consensus label for a finding from its provider stances.

    Rules (in order):
    - any CONTRADICTORY stance -> CONFLICT
    - at most one asserting provider (CONCORDANT/PARTIAL) -> SINGLE
    - more than one asserting provider, all CONCORDANT -> UNANIMOUS
    - otherwise -> MAJORITY
    """
    stances = [
        ps.get("stance") for ps in (finding.get("provider_support") or [])
    ]
    if "CONTRADICTORY" in stances:
        return "CONFLICT"
    asserting = [s for s in stances if s in ("CONCORDANT", "PARTIAL")]
    if len(asserting) <= 1:
        return "SINGLE"
    if all(s == "CONCORDANT" for s in asserting):
        return "UNANIMOUS"
    return "MAJORITY"


@cache
def _normalized_report(path: str) -> str:
    return _norm(Path(path).read_text(encoding="utf-8"))


def iter_quote_problems(synthesis_path: str | Path) -> Iterable[str]:
    """Yield a message for each best_matching_text that fails to verify.

    A problem is raised when a ``provider_support`` block has a
    ``best_matching_text`` but (a) no resolvable ``source_report``, or (b) the
    quote is not a whitespace-normalized substring of that report.
    """
    synthesis_path = Path(synthesis_path)
    data = yaml.safe_load(synthesis_path.read_text(encoding="utf-8")) or {}
    for i, finding in enumerate(data.get("harmonized_findings") or []):
        for support in finding.get("provider_support") or []:
            quote = support.get("best_matching_text")
            if not quote:
                continue
            provider = support.get("provider")
            report = support.get("source_report")
            if not report:
                yield (
                    f"harmonized_findings[{i}] provider={provider!r}: "
                    f"best_matching_text present but no source_report to verify against"
                )
                continue
            if not Path(report).is_file():
                yield (
                    f"harmonized_findings[{i}] provider={provider!r}: "
                    f"source_report {report!r} does not exist"
                )
                continue
            if _norm(quote) not in _normalized_report(report):
                yield (
                    f"harmonized_findings[{i}] provider={provider!r}: "
                    f"best_matching_text is not a verbatim substring of {report!r}: "
                    f"{_norm(quote)[:120]!r}"
                )


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print("usage: python -m dismech.research_synthesis <synthesis.yaml> ...")
        return 2
    problems = 0
    for path in argv:
        for msg in iter_quote_problems(path):
            print(f"{path}: {msg}")
            problems += 1
    if problems:
        print(f"\n✗ {problems} best_matching_text verification problem(s).")
        return 1
    print(f"✓ All best_matching_text quotes verified across {len(argv)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
