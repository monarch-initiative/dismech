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
_LOCAL_ID = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
_CHECKSUM = re.compile(r"^sha256:[0-9a-fA-F]{64}$")


def _norm(text: str) -> str:
    """Collapse whitespace so Markdown line wrapping does not affect quoting."""
    return _WS.sub(" ", text).strip()


@cache
def _normalized_text(path: str) -> str:
    return _norm(Path(path).read_text(encoding="utf-8"))


def _resolve_relative_within(base: Path, root: Path, ref: object) -> Path | None:
    """Resolve a relative path only when its target remains below ``root``."""
    if not ref or Path(str(ref)).is_absolute():
        return None
    path = (base / str(ref)).resolve()
    return path if path.is_relative_to(root.resolve()) else None


def _iter_artifact_problems(
    value: object,
    *,
    label: str,
    base: Path,
    root: Path,
    single: bool = False,
    structured_assessment_path: Path | None = None,
    structured_report_path: Path | None = None,
    structured_artifact_root: Path | None = None,
) -> Iterable[str]:
    """Validate committed, non-empty, hypothesis-local artifact files."""
    if value is None:
        return
    if single:
        artifacts = [value]
    elif not isinstance(value, list):
        yield f"{label} must be a list"
        return
    else:
        artifacts = value
    for i, artifact in enumerate(artifacts):
        artifact_label = label if single else f"{label}[{i}]"
        if not isinstance(artifact, str) or not artifact.strip():
            yield f"{artifact_label} must be a non-empty relative path"
            continue
        artifact_path = _resolve_relative_within(base, root, artifact)
        if artifact_path is None:
            yield f"{artifact_label}={artifact!r} escapes the hypothesis directory"
            continue
        if structured_assessment_path is not None:
            assessments_dir = structured_assessment_path.parent.resolve()
            if artifact_path.is_relative_to(assessments_dir):
                yield (
                    f"{artifact_label}={artifact!r} must not point inside assessments/"
                )
                continue
            if artifact_path.name.lower().endswith(".citations.md"):
                yield (
                    f"{artifact_label}={artifact!r} must not point to a citation "
                    "sidecar"
                )
                continue
            if (
                structured_report_path is not None
                and artifact_path == structured_report_path.resolve()
            ) or (
                artifact_path.parent == root.resolve()
                and artifact_path.suffix.lower() == ".md"
            ):
                yield f"{artifact_label}={artifact!r} must not point to a raw report"
                continue
            if (
                structured_artifact_root is not None
                and not artifact_path.is_relative_to(structured_artifact_root.resolve())
            ):
                yield (f"{artifact_label}={artifact!r} must be beneath artifact_root")
                continue
        if not artifact_path.exists():
            yield f"{artifact_label}={artifact!r} does not exist"
        elif not artifact_path.is_file():
            yield f"{artifact_label}={artifact!r} is not a regular file"
        elif artifact_path.stat().st_size == 0:
            yield f"{artifact_label}={artifact!r} is empty"


def _resolved_artifact_paths(
    value: object,
    *,
    base: Path,
    root: Path,
    single: bool = False,
) -> set[Path]:
    """Return canonical paths for set-overlap checks; validation is separate."""
    if value is None:
        return set()
    values = [value] if single else value if isinstance(value, list) else []
    resolved: set[Path] = set()
    for artifact in values:
        if not isinstance(artifact, str) or not artifact.strip():
            continue
        artifact_path = _resolve_relative_within(base, root, artifact)
        if artifact_path is not None:
            resolved.add(artifact_path)
    return resolved


def _lineage_cycles(edges: Mapping[str, str]) -> Iterable[list[str]]:
    """Yield cycles in an analysis-to-predecessor fallback graph."""
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


def iter_assessment_problems(assessment_path: str | Path) -> Iterable[str]:
    """Yield layout, quote, dataset, analysis, and artifact problems."""
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
    hypothesis_root = assessment_path.parent.parent
    resolved_root = hypothesis_root.resolve()
    if assessment_path.parent.name != "assessments":
        yield "assessment YAML must live in an assessments/ directory"
    if (
        resolved_root.parent.parent.name != "hypotheses"
        or resolved_root.parent.parent.parent.name != "kb"
    ):
        yield (
            "assessment YAML must live at "
            "kb/hypotheses/<Disease>/<hypothesis_id>/assessments/<file>.yaml"
        )
    expected_hypothesis = hypothesis_root.name
    if data.get("hypothesis_id") != expected_hypothesis:
        yield (
            f"hypothesis_id={data.get('hypothesis_id')!r} does not match "
            f"directory {expected_hypothesis!r}"
        )

    source = data.get("source_report")
    report_path = (
        _resolve_relative_within(assessment_path.parent, hypothesis_root, source)
        if source
        else None
    )
    if not source:
        yield "source_report is required to verify report_quote values"
    elif report_path is None:
        yield f"source_report {source!r} escapes the hypothesis directory"
    elif not report_path.is_file():
        yield f"source_report {source!r} does not exist"
    elif (
        report_path.parent != resolved_root
        or report_path.suffix.lower() != ".md"
        or report_path.name.lower().endswith(".citations.md")
    ):
        yield "source_report must be a raw .md report in the hypothesis directory"

    artifact_root_ref = data.get("artifact_root")
    artifact_root_path: Path | None = None
    if artifact_root_ref is not None:
        if not isinstance(artifact_root_ref, str) or not artifact_root_ref.strip():
            yield "artifact_root must be a non-empty relative path"
        else:
            artifact_root_path = _resolve_relative_within(
                assessment_path.parent, hypothesis_root, artifact_root_ref
            )
            if artifact_root_path is None:
                yield "artifact_root must remain inside the hypothesis directory"
            else:
                provider = data.get("provider")
                if isinstance(provider, str):
                    expected_artifact_root = (
                        hypothesis_root / f"{provider}_artifacts"
                    ).resolve()
                    if artifact_root_path != expected_artifact_root:
                        yield (
                            "artifact_root must resolve to the provider-specific "
                            f"directory ../{provider}_artifacts/"
                        )
                if not artifact_root_path.is_dir():
                    yield f"artifact_root {artifact_root_ref!r} is not a directory"

    structured_artifacts_declared = False

    data_sources_value = data.get("data_sources")
    if data_sources_value is None:
        data_sources: list = []
    elif not isinstance(data_sources_value, list):
        yield "data_sources must be a list"
        data_sources = []
    else:
        data_sources = data_sources_value
    data_sources_by_id: dict[str, Mapping] = {}
    for i, source_record in enumerate(data_sources):
        label = f"data_sources[{i}]"
        if not isinstance(source_record, Mapping):
            yield f"{label} must be a mapping"
            continue
        data_source_id = source_record.get("data_source_id")
        if not isinstance(data_source_id, str) or not _LOCAL_ID.fullmatch(
            data_source_id
        ):
            yield f"{label}.data_source_id must be a lowercase local identifier"
        elif data_source_id in data_sources_by_id:
            yield f"{label} duplicates data_source_id {data_source_id!r}"
        else:
            data_sources_by_id[data_source_id] = source_record

        source_artifacts_value = source_record.get("source_artifacts")
        structured_artifacts_declared = structured_artifacts_declared or bool(
            source_artifacts_value
        )
        yield from _iter_artifact_problems(
            source_artifacts_value,
            label=f"{label}.source_artifacts",
            base=assessment_path.parent,
            root=hypothesis_root,
            structured_assessment_path=assessment_path,
            structured_report_path=report_path,
            structured_artifact_root=artifact_root_path,
        )
        source_artifacts = (
            source_artifacts_value if isinstance(source_artifacts_value, list) else []
        )
        access_status = source_record.get("access_status")
        retrieved_at = source_record.get("retrieved_at")
        query = _norm(str(source_record.get("query") or ""))
        identifier = _norm(str(source_record.get("identifier") or ""))
        uri = _norm(str(source_record.get("uri") or ""))
        notes = _norm(str(source_record.get("notes") or ""))
        source_type = source_record.get("source_type")
        checksum = source_record.get("checksum")

        if source_type == "PUBLIC_DATASET" and not identifier:
            yield f"{label} PUBLIC_DATASET requires identifier"
        if checksum is not None and (
            not isinstance(checksum, str) or not _CHECKSUM.fullmatch(checksum)
        ):
            yield (f"{label}.checksum must use sha256:<64 hexadecimal characters>")
        if access_status in {"ACCESSED", "SEARCHED_NO_RESULT"}:
            if not retrieved_at:
                yield f"{label} {access_status} requires retrieved_at"
            if not source_artifacts:
                yield f"{label} {access_status} requires source_artifacts"
        if access_status == "ACCESSED":
            if not (identifier or uri or source_type == "LOCAL_FILE"):
                yield f"{label} ACCESSED requires identifier, uri, or LOCAL_FILE"
            if source_type in {"DATABASE", "API"} and not query:
                yield f"{label} ACCESSED {source_type} requires query"
        elif access_status == "SEARCHED_NO_RESULT":
            if not query:
                yield f"{label} SEARCHED_NO_RESULT requires query"
        elif access_status == "CITED_NOT_ACCESSED":
            if not (identifier or uri):
                yield f"{label} CITED_NOT_ACCESSED requires identifier or uri"
            if retrieved_at:
                yield f"{label} CITED_NOT_ACCESSED cannot declare retrieved_at"
            if source_artifacts:
                yield f"{label} CITED_NOT_ACCESSED cannot declare source_artifacts"
        elif access_status == "UNVERIFIABLE" and not notes:
            yield f"{label} UNVERIFIABLE requires notes"

    analyses_value = data.get("analyses")
    if analyses_value is None:
        analyses: list = []
    elif not isinstance(analyses_value, list):
        yield "analyses must be a list"
        analyses = []
    else:
        analyses = analyses_value
    analyses_by_id: dict[str, Mapping] = {}
    fallback_edges: dict[str, str] = {}
    for i, analysis in enumerate(analyses):
        label = f"analyses[{i}]"
        if not isinstance(analysis, Mapping):
            yield f"{label} must be a mapping"
            continue
        analysis_id = analysis.get("analysis_id")
        if not isinstance(analysis_id, str) or not _LOCAL_ID.fullmatch(analysis_id):
            yield f"{label}.analysis_id must be a lowercase local identifier"
        elif analysis_id in analyses_by_id:
            yield f"{label} duplicates analysis_id {analysis_id!r}"
        else:
            analyses_by_id[analysis_id] = analysis

        input_ids_value = analysis.get("input_data_source_ids")
        if input_ids_value is None:
            input_ids: list = []
        elif not isinstance(input_ids_value, list):
            yield f"{label}.input_data_source_ids must be a list"
            input_ids = []
        else:
            input_ids = input_ids_value
        seen_input_ids: set[str] = set()
        for input_id in input_ids:
            input_id = str(input_id)
            if input_id in seen_input_ids:
                yield f"{label} duplicates input_data_source_id {input_id!r}"
            seen_input_ids.add(input_id)
            source_record = data_sources_by_id.get(input_id)
            if source_record is None:
                yield f"{label} input_data_source_id={input_id!r} does not resolve"
            elif analysis.get("status") == "SUCCEEDED" and source_record.get(
                "access_status"
            ) not in {"ACCESSED", "SEARCHED_NO_RESULT"}:
                yield (
                    f"{label} SUCCEEDED analysis cannot use {input_id!r} with "
                    f"access_status={source_record.get('access_status')!r}"
                )

        software_value = analysis.get("software")
        if software_value is None:
            software: list = []
        elif not isinstance(software_value, list):
            yield f"{label}.software must be a list"
            software = []
        else:
            software = software_value
        for j, dependency in enumerate(software):
            dependency_label = f"{label}.software[{j}]"
            if not isinstance(dependency, Mapping):
                yield f"{dependency_label} must be a mapping"
                continue
            if not _norm(str(dependency.get("software_name") or "")):
                yield f"{dependency_label}.software_name is required"
            if analysis.get("auditability") == "REPRODUCIBLE" and not _norm(
                str(dependency.get("software_version") or "")
            ):
                yield (
                    f"{dependency_label}.software_version is required for "
                    "REPRODUCIBLE analysis"
                )

        code_artifacts_value = analysis.get("code_artifacts")
        output_artifacts_value = analysis.get("output_artifacts")
        structured_artifacts_declared = structured_artifacts_declared or bool(
            code_artifacts_value or output_artifacts_value
        )
        yield from _iter_artifact_problems(
            code_artifacts_value,
            label=f"{label}.code_artifacts",
            base=assessment_path.parent,
            root=hypothesis_root,
            structured_assessment_path=assessment_path,
            structured_report_path=report_path,
            structured_artifact_root=artifact_root_path,
        )
        yield from _iter_artifact_problems(
            output_artifacts_value,
            label=f"{label}.output_artifacts",
            base=assessment_path.parent,
            root=hypothesis_root,
            structured_assessment_path=assessment_path,
            structured_report_path=report_path,
            structured_artifact_root=artifact_root_path,
        )
        code_artifacts = (
            code_artifacts_value if isinstance(code_artifacts_value, list) else []
        )
        output_artifacts = (
            output_artifacts_value if isinstance(output_artifacts_value, list) else []
        )
        environment_ref = analysis.get("environment_artifact")
        structured_artifacts_declared = structured_artifacts_declared or bool(
            environment_ref
        )
        yield from _iter_artifact_problems(
            environment_ref,
            label=f"{label}.environment_artifact",
            base=assessment_path.parent,
            root=hypothesis_root,
            single=True,
            structured_assessment_path=assessment_path,
            structured_report_path=report_path,
            structured_artifact_root=artifact_root_path,
        )

        artifact_groups = {
            "code_artifacts": _resolved_artifact_paths(
                code_artifacts_value,
                base=assessment_path.parent,
                root=hypothesis_root,
            ),
            "environment_artifact": _resolved_artifact_paths(
                environment_ref,
                base=assessment_path.parent,
                root=hypothesis_root,
                single=True,
            ),
            "output_artifacts": _resolved_artifact_paths(
                output_artifacts_value,
                base=assessment_path.parent,
                root=hypothesis_root,
            ),
        }

        status = analysis.get("status")
        auditability = analysis.get("auditability")
        method = _norm(str(analysis.get("method") or ""))
        status_reason = _norm(str(analysis.get("status_reason") or ""))
        has_execution_artifacts = bool(
            code_artifacts or output_artifacts or environment_ref
        )
        if status == "SUCCEEDED" and auditability != "REPRODUCIBLE":
            yield f"{label} SUCCEEDED analysis must be REPRODUCIBLE"
        if status == "PARTIAL" and auditability not in {
            "REPRODUCIBLE",
            "PARTIALLY_AUDITABLE",
        }:
            yield (
                f"{label} PARTIAL analysis must be REPRODUCIBLE or PARTIALLY_AUDITABLE"
            )
        if status == "FAILED" and auditability not in {
            "REPRODUCIBLE",
            "PARTIALLY_AUDITABLE",
            "UNVERIFIABLE",
        }:
            yield (
                f"{label} FAILED analysis must be REPRODUCIBLE, "
                "PARTIALLY_AUDITABLE, or UNVERIFIABLE"
            )
        if status == "SKIPPED" and auditability != "UNVERIFIABLE":
            yield f"{label} SKIPPED analysis must be UNVERIFIABLE"
        if status in {"PARTIAL", "FAILED", "SKIPPED", "REPORTED_ONLY"} and not (
            status_reason
        ):
            yield f"{label} {status} requires status_reason"
        if status == "REPORTED_ONLY" and auditability not in {
            "PARTIALLY_AUDITABLE",
            "UNVERIFIABLE",
        }:
            yield (
                f"{label} REPORTED_ONLY analysis must be PARTIALLY_AUDITABLE "
                "or UNVERIFIABLE"
            )
        if status == "SKIPPED" and output_artifacts:
            yield f"{label} SKIPPED analysis cannot declare output_artifacts"

        if auditability == "REPRODUCIBLE":
            if not input_ids:
                yield f"{label} REPRODUCIBLE analysis requires input_data_source_ids"
            if not method:
                yield f"{label} REPRODUCIBLE analysis requires method"
            if not software:
                yield f"{label} REPRODUCIBLE analysis requires software"
            if not code_artifacts:
                yield f"{label} REPRODUCIBLE analysis requires code_artifacts"
            if not environment_ref:
                yield f"{label} REPRODUCIBLE analysis requires environment_artifact"
            if not output_artifacts:
                yield f"{label} REPRODUCIBLE analysis requires output_artifacts"
            group_names = tuple(artifact_groups)
            for left_index, left_name in enumerate(group_names):
                for right_name in group_names[left_index + 1 :]:
                    for reused_path in sorted(
                        artifact_groups[left_name] & artifact_groups[right_name]
                    ):
                        yield (
                            f"{label} REPRODUCIBLE artifact {reused_path.name!r} "
                            f"is reused across {left_name} and {right_name}"
                        )
        elif auditability == "PARTIALLY_AUDITABLE":
            if not method:
                yield f"{label} PARTIALLY_AUDITABLE analysis requires method"
            if not has_execution_artifacts:
                yield (
                    f"{label} PARTIALLY_AUDITABLE analysis requires at least one "
                    "execution artifact"
                )
        elif auditability == "UNVERIFIABLE" and has_execution_artifacts:
            yield f"{label} UNVERIFIABLE analysis cannot declare execution artifacts"

        fallback_declared = "fallback_from_analysis_id" in analysis
        fallback_from = _norm(str(analysis.get("fallback_from_analysis_id") or ""))
        if fallback_declared and not fallback_from:
            yield f"{label}.fallback_from_analysis_id must contain non-whitespace text"
        if fallback_declared and not status_reason:
            yield f"{label} fallback_from_analysis_id requires status_reason"
        if fallback_from and isinstance(analysis_id, str):
            fallback_edges[analysis_id] = fallback_from

    for analysis_id, fallback_from in fallback_edges.items():
        source_analysis = analyses_by_id.get(fallback_from)
        if source_analysis is None:
            yield (
                f"analysis {analysis_id!r} fallback_from_analysis_id="
                f"{fallback_from!r} does not resolve"
            )
        elif analysis_id == fallback_from:
            yield f"analysis {analysis_id!r} cannot fall back from itself"
        elif source_analysis.get("status") not in {"PARTIAL", "FAILED", "SKIPPED"}:
            yield (
                f"analysis {analysis_id!r} fallback source {fallback_from!r} must "
                "have status PARTIAL, FAILED, or SKIPPED"
            )
    for cycle in _lineage_cycles(fallback_edges):
        yield f"analyses have cyclic fallback lineage: {' -> '.join(cycle)}"

    if structured_artifacts_declared and not artifact_root_ref:
        yield "artifact_root is required when structured artifacts are declared"

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

        analysis_ids_value = claim.get("analysis_ids")
        if analysis_ids_value is None:
            analysis_ids: list = []
        elif not isinstance(analysis_ids_value, list):
            yield f"claims[{i}].analysis_ids must be a list"
            analysis_ids = []
        else:
            analysis_ids = analysis_ids_value
        seen_analysis_ids: set[str] = set()
        linked_analyses: list[Mapping] = []
        for analysis_id in analysis_ids:
            analysis_id = str(analysis_id)
            if analysis_id in seen_analysis_ids:
                yield f"claims[{i}] duplicates analysis_id {analysis_id!r}"
            seen_analysis_ids.add(analysis_id)
            analysis = analyses_by_id.get(analysis_id)
            if analysis is None:
                yield f"claims[{i}] analysis_id={analysis_id!r} does not resolve"
            else:
                linked_analyses.append(analysis)
                if claim.get("disposition") == "RETAINED" and (
                    analysis.get("status") != "SUCCEEDED"
                    or analysis.get("auditability") != "REPRODUCIBLE"
                ):
                    yield (
                        f"claims[{i}] RETAINED claim cannot rely on analysis "
                        f"{analysis_id!r} with status={analysis.get('status')!r}, "
                        f"auditability={analysis.get('auditability')!r}"
                    )
        if (
            claim.get("disposition") == "QUALIFIED"
            and analysis_ids
            and not any(
                analysis.get("status") in {"SUCCEEDED", "PARTIAL"}
                for analysis in linked_analyses
            )
        ):
            yield (
                f"claims[{i}] QUALIFIED claim with analysis_ids requires at least "
                "one SUCCEEDED or PARTIAL analysis"
            )

    yield from _iter_artifact_problems(
        data.get("artifacts"),
        label="artifacts",
        base=assessment_path.parent,
        root=hypothesis_root,
    )


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
