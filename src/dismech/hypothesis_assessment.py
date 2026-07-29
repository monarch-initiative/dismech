"""Validation helpers for hypothesis-exploration report assessment sidecars."""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable
from functools import cache
from pathlib import Path

import yaml

_WS = re.compile(r"\s+")
_FILENAME = re.compile(
    r"^(?P<provider>[a-z0-9][a-z0-9-]*)-assessment-by-"
    r"(?P<assessor>[a-z0-9][a-z0-9-]*)\.yaml$"
)


def _norm(text: str) -> str:
    """Collapse whitespace so Markdown line wrapping does not affect quoting."""
    return _WS.sub(" ", text).strip()


@cache
def _normalized_text(path: str) -> str:
    return _norm(Path(path).read_text(encoding="utf-8"))


def iter_assessment_problems(assessment_path: str | Path) -> Iterable[str]:
    """Yield filename, link, and verbatim-quote problems for one sidecar."""
    assessment_path = Path(assessment_path)
    data = yaml.safe_load(assessment_path.read_text(encoding="utf-8")) or {}

    filename = _FILENAME.fullmatch(assessment_path.name)
    if not filename:
        yield "filename must be <provider>-assessment-by-<assessor>.yaml"
    else:
        for field in ("provider", "assessor"):
            if data.get(field) != filename.group(field):
                yield (
                    f"{field}={data.get(field)!r} does not match filename "
                    f"{filename.group(field)!r}"
                )
    if assessment_path.parent.name != "assessments":
        yield "assessment YAML must live in an assessments/ directory"

    source = data.get("source_report")
    report_path = assessment_path.parent / source if source else None
    if not source:
        yield "source_report is required to verify report_quote values"
    elif not report_path.is_file():
        yield f"source_report {source!r} does not exist"

    for i, claim in enumerate(data.get("claims") or []):
        quote = claim.get("report_quote")
        if quote and report_path and report_path.is_file():
            if _norm(quote) not in _normalized_text(str(report_path)):
                yield (
                    f"claims[{i}] report_quote is not a verbatim substring of "
                    f"{source!r}: {_norm(quote)[:120]!r}"
                )

    for artifact in data.get("artifacts") or []:
        if not (assessment_path.parent / artifact).is_file():
            yield f"artifact {artifact!r} does not exist"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print("usage: python -m dismech.hypothesis_assessment <assessment.yaml> ...")
        return 2
    problems = 0
    for path in argv:
        for message in iter_assessment_problems(path):
            print(f"{path}: {message}")
            problems += 1
    if problems:
        print(f"\n✗ {problems} hypothesis-assessment validation problem(s).")
        return 1
    print(
        f"✓ All hypothesis-assessment links and quotes verified across {len(argv)} file(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
