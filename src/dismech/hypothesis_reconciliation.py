"""Validation helpers for cross-provider hypothesis reconciliations."""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable, Mapping
from functools import cache
from pathlib import Path

from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

from dismech.hypothesis_assessment import iter_assessment_problems
from dismech.yaml_io import safe_load

_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_CLAIM_ID = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
_WS = re.compile(r"\s+")
_ASSESSMENT_SCHEMA = Path(__file__).parent / "schema" / "hypothesis_assessment.yaml"


def _load_mapping(path: Path) -> Mapping:
    data = safe_load(path.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, Mapping) else {}


def _claims_by_id(assessment: Mapping) -> dict[str, Mapping]:
    claims = assessment.get("claims") or []
    if not isinstance(claims, list):
        return {}
    return {
        str(claim["claim_id"]): claim
        for claim in claims
        if isinstance(claim, Mapping) and claim.get("claim_id")
    }


def _analyses_by_id(assessment: Mapping) -> dict[str, Mapping]:
    analyses = assessment.get("analyses") or []
    if not isinstance(analyses, list):
        return {}
    return {
        str(analysis["analysis_id"]): analysis
        for analysis in analyses
        if isinstance(analysis, Mapping) and analysis.get("analysis_id")
    }


def _norm(text: str) -> str:
    return _WS.sub(" ", text).strip()


@cache
def _normalized_report(path: str) -> str:
    return _norm(Path(path).read_text(encoding="utf-8"))


@cache
def _assessment_validator() -> Validator:
    """Return a strict validator for source-assessment sidecars."""
    return Validator(
        _ASSESSMENT_SCHEMA,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _resolve_relative_within(base: Path, root: Path, ref: object) -> Path | None:
    if not ref or Path(str(ref)).is_absolute():
        return None
    path = (base / str(ref)).resolve()
    return path if path.is_relative_to(root.resolve()) else None


def _resolve_within(root: Path, ref: object) -> Path | None:
    return _resolve_relative_within(root, root, ref)


def _lineage_cycles(edges: Mapping[str, str]) -> Iterable[list[str]]:
    """Yield cycles in a provider-to-source-provider lineage graph."""
    processed: set[str] = set()
    for start in edges:
        if start in processed:
            continue
        path: list[str] = []
        indices: dict[str, int] = {}
        current = start
        while current in edges and current not in processed:
            if current in indices:
                yield [*path[indices[current] :], current]
                break
            indices[current] = len(path)
            path.append(current)
            current = edges[current]
        processed.update(path)


def iter_reconciliation_problems(
    reconciliation_path: str | Path,
) -> Iterable[str]:
    """Yield layout, foreign-key, and source-anchoring problems."""
    reconciliation_path = Path(reconciliation_path)
    data = _load_mapping(reconciliation_path)

    if reconciliation_path.name != "reconciliation.yaml":
        yield "filename must be reconciliation.yaml"
    hypothesis_root = reconciliation_path.parent
    resolved_root = hypothesis_root.resolve()
    if (
        resolved_root.parent.parent.name != "hypotheses"
        or resolved_root.parent.parent.parent.name != "kb"
    ):
        yield (
            "reconciliation YAML must live at "
            "kb/hypotheses/<Disease>/<hypothesis_id>/reconciliation.yaml"
        )
    expected_hypothesis = hypothesis_root.name
    if data.get("hypothesis_id") != expected_hypothesis:
        yield (
            f"hypothesis_id={data.get('hypothesis_id')!r} does not match "
            f"directory {expected_hypothesis!r}"
        )
    assessor = data.get("assessor")
    if not isinstance(assessor, str) or not _SLUG.fullmatch(assessor):
        yield "assessor must be a lowercase, hyphenated slug"

    sources: dict[str, tuple[Path, Mapping, Path]] = {}
    declared: set[str] = set()
    assessment_paths: dict[Path, str] = {}
    report_paths: dict[Path, str] = {}
    raw_sources_value = data.get("providers") or []
    if not isinstance(raw_sources_value, list):
        yield "providers must be a list"
        raw_sources: list = []
    else:
        raw_sources = raw_sources_value
    if len(raw_sources) < 2:
        yield "providers must declare at least two separately assessed providers"
    for i, source in enumerate(raw_sources):
        label = f"providers[{i}]"
        if not isinstance(source, Mapping):
            yield f"{label} must be a mapping"
            continue
        provider = source.get("provider")
        assessment_ref = source.get("source_assessment")
        report_ref = source.get("source_report")
        if not isinstance(provider, str) or not _SLUG.fullmatch(provider):
            yield f"{label} provider must be a lowercase, hyphenated slug"
            continue
        if provider in declared:
            yield f"{label} duplicates provider {provider!r}"
            continue
        declared.add(provider)
        if not assessment_ref:
            yield f"{label} source_assessment is required"
        if not report_ref:
            yield f"{label} source_report is required"
        if not assessment_ref or not report_ref:
            continue
        assessment_path = _resolve_within(hypothesis_root, assessment_ref)
        report_path = _resolve_within(hypothesis_root, report_ref)
        if assessment_path is None:
            yield (
                f"{label} source_assessment {assessment_ref!r} escapes "
                "the hypothesis directory"
            )
            continue
        if assessment_path.parent != (hypothesis_root / "assessments").resolve():
            yield f"{label} source_assessment must live in assessments/"
        if not assessment_path.is_file():
            yield f"{label} source_assessment {assessment_ref!r} does not exist"
            continue
        previous_provider = assessment_paths.get(assessment_path)
        if previous_provider:
            yield (
                f"{label} reuses source_assessment {assessment_ref!r} already "
                f"selected for provider {previous_provider!r}"
            )
        else:
            assessment_paths[assessment_path] = provider
        if report_path is None:
            yield (
                f"{label} source_report {report_ref!r} escapes the hypothesis directory"
            )
            continue
        if not report_path.is_file():
            yield f"{label} source_report {report_ref!r} does not exist"
            continue
        if (
            report_path.parent != resolved_root
            or report_path.suffix.lower() != ".md"
            or report_path.name.lower().endswith(".citations.md")
        ):
            yield (
                f"{label} source_report must be a raw .md report directly in "
                "the hypothesis directory"
            )
        previous_provider = report_paths.get(report_path)
        if previous_provider:
            yield (
                f"{label} reuses source_report {report_ref!r} already selected "
                f"for provider {previous_provider!r}"
            )
        else:
            report_paths[report_path] = provider
        assessment = _load_mapping(assessment_path)
        assessment_report = _assessment_validator().validate(
            assessment,
            target_class="HypothesisAssessment",
        )
        for result in assessment_report.results:
            if result.severity.name == "ERROR":
                yield f"{label} source assessment schema invalid: {result.message}"
        if assessment.get("provider") != provider:
            yield (
                f"{label} provider={provider!r} does not match "
                f"assessment provider={assessment.get('provider')!r}"
            )
        if assessment.get("hypothesis_id") != data.get("hypothesis_id"):
            yield (
                f"{label} assessment hypothesis_id="
                f"{assessment.get('hypothesis_id')!r} does not match reconciliation "
                f"hypothesis_id={data.get('hypothesis_id')!r}"
            )
        assessed_report = _resolve_relative_within(
            assessment_path.parent,
            hypothesis_root,
            assessment.get("source_report"),
        )
        if assessed_report != report_path:
            yield (
                f"{label} source_report {report_ref!r} is not the report "
                f"selected assessment {assessment_ref!r} reviews"
            )
        for problem in iter_assessment_problems(assessment_path):
            yield f"{label} source assessment invalid: {problem}"
        sources[provider] = (assessment_path, assessment, report_path)

    if len(declared) < 2:
        yield "providers must declare at least two unique provider slugs"

    seen_claim_ids: set[str] = set()
    raw_claims = data.get("reconciled_claims") or []
    if not isinstance(raw_claims, list):
        yield "reconciled_claims must be a list"
        raw_claims = []
    for i, claim in enumerate(raw_claims):
        if not isinstance(claim, Mapping):
            continue
        claim_id = claim.get("claim_id")
        if not isinstance(claim_id, str) or not _CLAIM_ID.fullmatch(claim_id):
            yield (
                f"reconciled_claims[{i}].claim_id must be a lowercase local identifier"
            )
        elif claim_id in seen_claim_ids:
            yield f"reconciled_claims[{i}] duplicates claim_id {claim_id!r}"
        else:
            seen_claim_ids.add(claim_id)
        positions_value = claim.get("provider_support") or []
        if not isinstance(positions_value, list):
            yield f"reconciled_claims[{i}].provider_support must be a list"
            positions: list = []
        else:
            positions = positions_value
        seen: set[str] = set()
        non_silent = 0
        positions_by_provider: dict[str, Mapping] = {}
        lineage_edges: dict[str, str] = {}
        for j, position in enumerate(positions):
            if not isinstance(position, Mapping):
                continue
            provider_value = position.get("provider")
            provider = provider_value if isinstance(provider_value, str) else ""
            label = f"reconciled_claims[{i}].provider_support[{j}]"
            if provider in seen:
                yield f"{label} duplicates provider {provider!r}"
                continue
            seen.add(provider)
            positions_by_provider[provider] = position
            if provider not in declared:
                yield f"{label} references undeclared provider {provider!r}"
                continue

            stance = position.get("stance")
            assessment_claim_ids_value = position.get("assessment_claim_ids") or []
            if not isinstance(assessment_claim_ids_value, list):
                yield f"{label} assessment_claim_ids must be a list"
                assessment_claim_ids: list = []
            else:
                assessment_claim_ids = assessment_claim_ids_value
            analysis_ids_value = position.get("analysis_ids") or []
            if not isinstance(analysis_ids_value, list):
                yield f"{label} analysis_ids must be a list"
                analysis_ids: list = []
            else:
                analysis_ids = analysis_ids_value
            report_quote = position.get("report_quote")
            report_quote_norm = (
                _norm(str(report_quote)) if report_quote is not None else ""
            )
            claim_origin = position.get("claim_origin")
            derived_from = position.get("derived_from_provider")
            if stance == "SILENT":
                if assessment_claim_ids or analysis_ids or report_quote:
                    yield f"{label} is SILENT but declares source anchors"
                if claim_origin or derived_from:
                    yield f"{label} is SILENT but declares claim lineage"
                continue
            non_silent += 1
            if not assessment_claim_ids:
                yield f"{label} requires assessment_claim_ids when stance is {stance!r}"
            if not report_quote_norm:
                yield f"{label} requires report_quote when stance is {stance!r}"
            if not claim_origin:
                yield f"{label} requires claim_origin when stance is {stance!r}"
            if claim_origin == "PROVIDER_ANALYSIS" and not analysis_ids:
                yield (
                    f"{label} requires analysis_ids when claim_origin is "
                    "PROVIDER_ANALYSIS"
                )
            elif analysis_ids and claim_origin != "PROVIDER_ANALYSIS":
                yield (f"{label} has analysis_ids but claim_origin is {claim_origin!r}")
            if claim_origin == "PRIOR_PROVIDER_DERIVED":
                if not derived_from:
                    yield (
                        f"{label} requires derived_from_provider when claim_origin "
                        "is PRIOR_PROVIDER_DERIVED"
                    )
                elif derived_from not in declared:
                    yield (
                        f"{label} derived_from_provider={derived_from!r} is not a "
                        "declared provider"
                    )
                elif derived_from == provider:
                    yield f"{label} cannot derive a claim from the same provider"
                else:
                    lineage_edges[provider] = str(derived_from)
            elif derived_from:
                yield (
                    f"{label} has derived_from_provider but claim_origin is "
                    f"{claim_origin!r}"
                )

            source = sources.get(provider)
            if source is None:
                yield f"{label} cannot verify anchors because its source is invalid"
                continue
            assessment_path, assessment, report_path = source
            claims_by_id = _claims_by_id(assessment)
            analyses_by_id = _analyses_by_id(assessment)
            anchored_analysis_ids: set[str] = set()
            seen_assessment_claim_ids: set[str] = set()
            for assessment_claim_id in assessment_claim_ids:
                assessment_claim_id = str(assessment_claim_id)
                if assessment_claim_id in seen_assessment_claim_ids:
                    yield (
                        f"{label} duplicates assessment_claim_id "
                        f"{assessment_claim_id!r}"
                    )
                seen_assessment_claim_ids.add(assessment_claim_id)
                source_claim = claims_by_id.get(str(assessment_claim_id))
                if source_claim is None:
                    yield (
                        f"{label} assessment_claim_id={assessment_claim_id!r} does "
                        f"not resolve in {assessment_path.name!r}"
                    )
                elif not _norm(str(source_claim.get("report_quote") or "")):
                    yield (
                        f"{label} assessment claim {assessment_claim_id!r} has no "
                        "report_quote anchor"
                    )
                else:
                    source_analysis_ids = source_claim.get("analysis_ids") or []
                    if isinstance(source_analysis_ids, list):
                        anchored_analysis_ids.update(map(str, source_analysis_ids))
            seen_analysis_ids: set[str] = set()
            for analysis_id in analysis_ids:
                analysis_id = str(analysis_id)
                if analysis_id in seen_analysis_ids:
                    yield f"{label} duplicates analysis_id {analysis_id!r}"
                seen_analysis_ids.add(analysis_id)
                analysis = analyses_by_id.get(analysis_id)
                if analysis is None:
                    yield (
                        f"{label} analysis_id={analysis_id!r} does not resolve in "
                        f"{assessment_path.name!r}"
                    )
                elif analysis.get("status") in {"FAILED", "SKIPPED"}:
                    yield (
                        f"{label} PROVIDER_ANALYSIS cannot derive a position from "
                        f"analysis {analysis_id!r} with status="
                        f"{analysis.get('status')!r}"
                    )
                if analysis_id not in anchored_analysis_ids:
                    yield (
                        f"{label} analysis_id={analysis_id!r} is not linked from "
                        "an anchored assessment claim"
                    )
            if report_quote_norm and report_quote_norm not in _normalized_report(
                str(report_path)
            ):
                yield (
                    f"{label} report_quote is not a verbatim substring of "
                    f"{report_path.name!r}: {report_quote_norm[:120]!r}"
                )

        for provider, derived_from in lineage_edges.items():
            source_position = positions_by_provider.get(derived_from)
            if (
                source_position is not None
                and source_position.get("stance") == "SILENT"
            ):
                yield (
                    f"reconciled_claims[{i}] provider {provider!r} derives from "
                    f"SILENT provider {derived_from!r}"
                )
        for cycle in _lineage_cycles(lineage_edges):
            yield (
                f"reconciled_claims[{i}] has cyclic provider lineage: "
                f"{' -> '.join(cycle)}"
            )
        if not non_silent:
            yield f"reconciled_claims[{i}] has no non-SILENT provider position"
        missing = declared - seen
        if missing:
            yield (
                f"reconciled_claims[{i}] omits declared provider(s): "
                f"{', '.join(sorted(missing))}"
            )

    artifacts = data.get("artifacts") or []
    if not isinstance(artifacts, list):
        yield "artifacts must be a list"
        artifacts = []
    for artifact in artifacts:
        artifact_path = _resolve_within(hypothesis_root, artifact)
        if artifact_path is None:
            yield f"artifact {artifact!r} escapes the hypothesis directory"
        elif not artifact_path.is_file():
            yield f"artifact {artifact!r} does not exist"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print("usage: python -m dismech.hypothesis_reconciliation <file.yaml> ...")
        return 2
    problems = 0
    for path in argv:
        for message in iter_reconciliation_problems(path):
            print(f"{path}: {message}")
            problems += 1
    if problems:
        print(f"\n✗ {problems} hypothesis-reconciliation validation problem(s).")
        return 1
    print(f"✓ All hypothesis-reconciliation links verified across {len(argv)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
