"""Validation helpers for hypothesis-exploration report assessment sidecars."""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable, Mapping
from functools import cache
from pathlib import Path

from dismech.yaml_io import safe_load

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
    data = safe_load(assessment_path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, Mapping):
        yield "assessment document root must be a mapping"
        return

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
    report_path = assessment_path.parent / str(source) if source else None
    if not source:
        yield "source_report is required to verify report_quote values"
    elif not report_path.is_file():
        yield f"source_report {source!r} does not exist"

    claims = data.get("claims") or []
    if not isinstance(claims, list):
        yield "claims must be a list"
        claims = []
    seen_claim_ids: set[str] = set()
    for i, claim in enumerate(claims):
        if not isinstance(claim, Mapping):
            yield f"claims[{i}] must be a mapping"
            continue
        claim_id = claim.get("claim_id")
        if claim_id:
            claim_id = str(claim_id)
            if claim_id in seen_claim_ids:
                yield f"claims[{i}] duplicates claim_id {claim_id!r}"
            seen_claim_ids.add(claim_id)
        quote = claim.get("report_quote")
        quote_norm = _norm(str(quote)) if quote is not None else ""
        if quote is not None and not quote_norm:
            yield f"claims[{i}] report_quote must contain non-whitespace text"
        if (
            quote_norm
            and report_path
            and report_path.is_file()
            and quote_norm not in _normalized_text(str(report_path))
        ):
            yield (
                f"claims[{i}] report_quote is not a verbatim substring of "
                f"{source!r}: {quote_norm[:120]!r}"
            )

    artifacts = data.get("artifacts") or []
    if not isinstance(artifacts, list):
        yield "artifacts must be a list"
        artifacts = []
    for artifact in artifacts:
        if not (assessment_path.parent / str(artifact)).is_file():
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
