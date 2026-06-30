"""Phenopacket match-quality evaluation harness.

This is a *deterministic match-quality* evaluator (the "1=A" scope): for each
phenopacket carrying a ground-truth diagnosis, it resolves that diagnosis to a
dismech disorder, runs the deterministic phenotype matcher against *only that
true disease*, and reports how well the case phenotypes line up with the
modelled phenotypes. It does **not** rank candidate diseases.

Why a surrogate score (and not ``pr_is_diagnosis``):
``calculate_pr_is_diagnosis`` multiplies the probabilities of every referenced
explanation, and at deterministic init every non-exact / model-only row points
to ``NO_EXPLANATION`` (probability 0.0). Because a real run almost always has at
least one such row, the deterministic ``pr_is_diagnosis`` is ~0.0 for every
packet -- it only becomes meaningful after the agentic cyberian+Claude
explanation loop assigns real probabilities. This harness therefore ranks/grades
on a deterministic match-quality surrogate and reports ``pr_is_diagnosis``
alongside purely so a zero column is not mistaken for a broken matcher.

Coverage: a phenopacket whose ground-truth disease cannot be resolved to a
dismech disorder is recorded as a coverage miss (``KB_MISS``), which feeds the
KB-coverage statistic the PHENOPACKETS project asks for.

This v1 runs against bundled fixtures (the "2=C" scope). Pointing it at a full
phenopacket-store checkout (``--store-dir``) already works -- the deferred
follow-up is the pinned-release fetch, not this runner.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from phenoagent.matching import (
    _default_kb_dir,
    _disease_term_id,
    _iter_disease_files,
    _normalize_for_lookup,
    build_matching_run_from_phenopacket,
    calculate_pr_is_diagnosis,
    load_disease_model,
    load_phenopacket,
    resolve_disease_reference,
)

# Frequency weights for weighted model coverage. Mirrors matching._FREQUENCY_PRIORITY
# but floors unknown/missing frequencies at 1 so untyped model terms still count.
_FREQUENCY_WEIGHT = {
    "OBLIGATE": 5,
    "VERY_FREQUENT": 4,
    "FREQUENT": 3,
    "OCCASIONAL": 2,
    "VERY_RARE": 1,
}
_DEFAULT_FREQUENCY_WEIGHT = 1


def extract_ground_truth_disease(phenopacket: dict[str, Any]) -> dict[str, str] | None:
    """Return the ground-truth diagnosis ``{"id", "label"}`` from a phenopacket.

    Reads GA4GH ``interpretations[].diagnosis.disease`` first, then falls back to
    a top-level ``diseases[].term``. Returns ``None`` when neither is present.
    """
    interpretations = phenopacket.get("interpretations")
    if isinstance(interpretations, list):
        for interpretation in interpretations:
            if not isinstance(interpretation, dict):
                continue
            diagnosis = interpretation.get("diagnosis")
            if not isinstance(diagnosis, dict):
                continue
            disease = diagnosis.get("disease")
            if isinstance(disease, dict) and disease.get("id"):
                return {
                    "id": str(disease["id"]),
                    "label": str(disease.get("label") or ""),
                }

    diseases = phenopacket.get("diseases")
    if isinstance(diseases, list):
        for disease_entry in diseases:
            if not isinstance(disease_entry, dict):
                continue
            term = disease_entry.get("term")
            if isinstance(term, dict) and term.get("id"):
                return {
                    "id": str(term["id"]),
                    "label": str(term.get("label") or ""),
                }

    return None


@dataclass
class DiseaseIndex:
    """One-pass lookup index from disease id / name / slug to dismech slug.

    ``resolve_disease_reference`` re-parses every disorder YAML on each call,
    which is fine for one-off resolution but O(packets x KB) for a corpus run.
    Building this index once lets a full phenopacket-store sweep stay practical.
    """

    by_id: dict[str, str] = field(default_factory=dict)
    by_name: dict[str, str] = field(default_factory=dict)

    def resolve(self, disease_id: str | None, disease_label: str | None) -> str | None:
        """Resolve a ground-truth disease to a slug (id first, then label)."""
        if disease_id:
            slug = self.by_id.get(disease_id.strip().upper())
            if slug:
                return slug
        if disease_label:
            slug = self.by_name.get(_normalize_for_lookup(disease_label))
            if slug:
                return slug
        return None


def build_disease_index(kb_dir: Path | None = None) -> DiseaseIndex:
    """Scan the disorder directory once and build a resolution index."""
    disorder_dir = kb_dir or _default_kb_dir()
    index = DiseaseIndex()
    for path in _iter_disease_files(disorder_dir):
        slug = path.stem
        try:
            model = load_disease_model(slug, kb_dir=disorder_dir)
        except (ValueError, OSError):
            continue
        term_id = _disease_term_id(model)
        if term_id:
            index.by_id.setdefault(term_id.upper(), slug)
        name = model.get("name")
        if isinstance(name, str) and name.strip():
            index.by_name.setdefault(_normalize_for_lookup(name), slug)
        index.by_name.setdefault(_normalize_for_lookup(slug), slug)
    return index


@dataclass
class PacketResult:
    """Outcome of evaluating a single phenopacket."""

    packet_path: str
    case_id: str
    status: str  # SCORED | KB_MISS | NO_GROUND_TRUTH
    ground_truth_id: str | None = None
    ground_truth_label: str | None = None
    resolved_slug: str | None = None
    metrics: dict[str, Any] = field(default_factory=dict)


def _classify_rows(matches: list[dict[str, Any]]) -> dict[str, Any]:
    """Bucket matching rows into case/model overlap counts.

    Case-side metrics are per-row (each phenotypic observation is one row, which
    is what recall should measure). Model-side coverage is over *distinct* model
    terms -- a single model phenotype can be hit by several case rows (e.g. an
    exact term plus a broader parent term), and must not be counted twice.
    """
    case_total = case_exact = case_related = case_unmatched = 0
    matched_model: dict[str, int] = {}  # term id -> frequency weight
    model_only: dict[str, int] = {}

    for row in matches:
        if not isinstance(row, dict):
            continue
        has_case = bool(row.get("case_term_id"))
        model_term_id = row.get("model_term_id")

        if model_term_id:
            weight = _FREQUENCY_WEIGHT.get(
                str(row.get("model_frequency") or ""), _DEFAULT_FREQUENCY_WEIGHT
            )
            if has_case:
                matched_model.setdefault(str(model_term_id), weight)
            else:
                model_only.setdefault(str(model_term_id), weight)

        if has_case:
            case_total += 1
            if model_term_id:
                if row.get("exact") is True:
                    case_exact += 1
                elif row.get("case_is_broader") or row.get("case_is_narrower"):
                    case_related += 1
            else:
                case_unmatched += 1

    # A matched model term must never also count as model-only.
    for term_id in list(model_only):
        if term_id in matched_model:
            del model_only[term_id]

    model_matched = len(matched_model)
    model_only_count = len(model_only)
    model_total = model_matched + model_only_count
    matched_weight = sum(matched_model.values())
    total_weight = matched_weight + sum(model_only.values())

    def _ratio(numerator: int, denominator: int) -> float:
        return round(numerator / denominator, 4) if denominator else 0.0

    return {
        "case_total": case_total,
        "case_exact": case_exact,
        "case_related": case_related,
        "case_unmatched": case_unmatched,
        "model_total": model_total,
        "model_matched": model_matched,
        "model_only": model_only_count,
        "exact_recall": _ratio(case_exact, case_total),
        "related_recall": _ratio(case_exact + case_related, case_total),
        "model_coverage": _ratio(model_matched, model_total),
        "weighted_model_coverage": _ratio(matched_weight, total_weight),
    }


def score_matching_run(run: dict[str, Any]) -> dict[str, Any]:
    """Compute deterministic match-quality metrics for one MatchingRun."""
    matches = run.get("matches", [])
    metrics = _classify_rows(matches if isinstance(matches, list) else [])
    # Reported for transparency only; ~0.0 before the agentic explanation loop.
    metrics["pr_is_diagnosis"] = calculate_pr_is_diagnosis(run)
    return metrics


def evaluate_phenopacket(
    packet_path: str | Path,
    *,
    kb_dir: Path | None = None,
    disease_index: DiseaseIndex | None = None,
) -> PacketResult:
    """Evaluate a single phenopacket against its ground-truth disease.

    Pass ``disease_index`` (from :func:`build_disease_index`) to avoid re-scanning
    the disorder directory on every call; without it, resolution falls back to
    :func:`resolve_disease_reference`.
    """
    packet_path = Path(packet_path)
    phenopacket = load_phenopacket(packet_path)
    case_id = str(phenopacket.get("id") or packet_path.stem)

    ground_truth = extract_ground_truth_disease(phenopacket)
    if ground_truth is None:
        return PacketResult(
            packet_path=str(packet_path),
            case_id=case_id,
            status="NO_GROUND_TRUTH",
        )

    # Resolve the ground-truth disease (id first, then label) to a dismech slug.
    slug: str | None = None
    if disease_index is not None:
        slug = disease_index.resolve(ground_truth["id"], ground_truth["label"])
    else:
        for reference in (ground_truth["id"], ground_truth["label"]):
            if not reference:
                continue
            try:
                slug, _ = resolve_disease_reference(reference, kb_dir=kb_dir)
                break
            except (FileNotFoundError, ValueError):
                continue

    if slug is None:
        return PacketResult(
            packet_path=str(packet_path),
            case_id=case_id,
            status="KB_MISS",
            ground_truth_id=ground_truth["id"],
            ground_truth_label=ground_truth["label"] or None,
        )

    run = build_matching_run_from_phenopacket(
        phenopacket,
        disease_slug=slug,
        run_id=f"eval-{case_id}",
        kb_dir=kb_dir,
    )
    return PacketResult(
        packet_path=str(packet_path),
        case_id=case_id,
        status="SCORED",
        ground_truth_id=ground_truth["id"],
        ground_truth_label=ground_truth["label"] or None,
        resolved_slug=slug,
        metrics=score_matching_run(run),
    )


def _discover_phenopackets(paths: list[Path]) -> list[Path]:
    """Expand a mix of files and directories into phenopacket JSON paths.

    Directories are searched recursively for ``*.json`` files; only documents
    with a ``phenotypicFeatures`` list are kept (so unrelated JSON is skipped).
    """
    discovered: list[Path] = []
    for path in paths:
        if path.is_dir():
            candidates = sorted(path.rglob("*.json"))
        else:
            candidates = [path]
        for candidate in candidates:
            try:
                doc = load_phenopacket(candidate)
            except (ValueError, json.JSONDecodeError, OSError):
                continue
            if isinstance(doc.get("phenotypicFeatures"), list):
                discovered.append(candidate)
    # De-duplicate while preserving order.
    seen: set[Path] = set()
    unique: list[Path] = []
    for path in discovered:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique


def _mean(values: list[float]) -> float:
    return round(sum(values) / len(values), 4) if values else 0.0


def aggregate_results(results: list[PacketResult]) -> dict[str, Any]:
    """Aggregate per-packet results into summary coverage + quality stats."""
    scored = [r for r in results if r.status == "SCORED"]
    kb_miss = [r for r in results if r.status == "KB_MISS"]
    no_gt = [r for r in results if r.status == "NO_GROUND_TRUTH"]
    with_gt = len(scored) + len(kb_miss)

    summary: dict[str, Any] = {
        "n_packets": len(results),
        "n_with_ground_truth": with_gt,
        "n_no_ground_truth": len(no_gt),
        "n_scored": len(scored),
        "n_kb_miss": len(kb_miss),
        "kb_coverage_rate": round(len(scored) / with_gt, 4) if with_gt else 0.0,
        "kb_miss_diseases": sorted(
            {
                f"{r.ground_truth_id} ({r.ground_truth_label})"
                if r.ground_truth_label
                else str(r.ground_truth_id)
                for r in kb_miss
            }
        ),
    }
    if scored:
        summary["mean_exact_recall"] = _mean([r.metrics["exact_recall"] for r in scored])
        summary["mean_related_recall"] = _mean([r.metrics["related_recall"] for r in scored])
        summary["mean_model_coverage"] = _mean([r.metrics["model_coverage"] for r in scored])
        summary["mean_weighted_model_coverage"] = _mean(
            [r.metrics["weighted_model_coverage"] for r in scored]
        )
        summary["mean_pr_is_diagnosis"] = _mean(
            [float(r.metrics.get("pr_is_diagnosis", 0.0)) for r in scored]
        )
    return summary


def run_eval(
    paths: list[Path],
    *,
    kb_dir: Path | None = None,
    disease_index: DiseaseIndex | None = None,
) -> dict[str, Any]:
    """Evaluate all phenopackets reachable from ``paths`` and return a report.

    Builds a :class:`DiseaseIndex` once (a full KB scan) unless one is supplied.
    """
    packet_paths = _discover_phenopackets(paths)
    if disease_index is None:
        disease_index = build_disease_index(kb_dir=kb_dir)
    results = [
        evaluate_phenopacket(path, kb_dir=kb_dir, disease_index=disease_index)
        for path in packet_paths
    ]
    return {
        "summary": aggregate_results(results),
        "results": [asdict(result) for result in results],
    }


def render_markdown(report: dict[str, Any]) -> str:
    """Render a human-readable markdown summary of an eval report."""
    summary = report["summary"]
    lines = [
        "# Phenopacket Match-Quality Eval",
        "",
        "_Deterministic match-quality surrogate. `pr_is_diagnosis` is ~0.0 by",
        "design before the agentic explanation loop runs and is shown for",
        "transparency only -- a zero column is expected, not a broken matcher._",
        "",
        "## Coverage",
        "",
        f"- Phenopackets evaluated: **{summary['n_packets']}**",
        f"- With ground-truth diagnosis: **{summary['n_with_ground_truth']}** "
        f"(no ground truth: {summary['n_no_ground_truth']})",
        f"- Resolved to a dismech disorder (scored): **{summary['n_scored']}**",
        f"- Ground-truth disease not in KB (KB miss): **{summary['n_kb_miss']}**",
        f"- KB coverage rate: **{summary.get('kb_coverage_rate', 0.0):.2%}**",
    ]
    if summary.get("kb_miss_diseases"):
        lines.append("")
        lines.append("### Diseases missing from the KB")
        lines.append("")
        lines.extend(f"- {disease}" for disease in summary["kb_miss_diseases"])
    if summary.get("n_scored"):
        lines.extend(
            [
                "",
                "## Mean match quality (scored packets)",
                "",
                f"- Exact recall: **{summary['mean_exact_recall']:.2%}**",
                f"- Related recall (exact + broader/narrower): **{summary['mean_related_recall']:.2%}**",
                f"- Model coverage: **{summary['mean_model_coverage']:.2%}**",
                f"- Weighted model coverage: **{summary['mean_weighted_model_coverage']:.2%}**",
                f"- Mean pr_is_diagnosis (deterministic): {summary['mean_pr_is_diagnosis']}",
                "",
                "## Per-packet results",
                "",
                "| case_id | disease | slug | exact_recall | related_recall | model_coverage |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for result in report["results"]:
            if result["status"] != "SCORED":
                continue
            metrics = result["metrics"]
            lines.append(
                f"| {result['case_id']} | {result['ground_truth_label'] or result['ground_truth_id']} "
                f"| {result['resolved_slug']} | {metrics['exact_recall']:.2%} "
                f"| {metrics['related_recall']:.2%} | {metrics['model_coverage']:.2%} |"
            )
    return "\n".join(lines) + "\n"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m phenoagent.eval",
        description="Deterministic phenopacket match-quality evaluation against dismech.",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Phenopacket JSON files and/or directories (searched recursively).",
    )
    parser.add_argument(
        "--store-dir",
        type=Path,
        default=None,
        help="Convenience alias for a phenopacket-store checkout to include.",
    )
    parser.add_argument(
        "--kb-dir",
        type=Path,
        default=None,
        help="Override the dismech disorder directory (defaults to kb/disorders).",
    )
    parser.add_argument(
        "--json",
        dest="json_out",
        type=Path,
        default=None,
        help="Write the full JSON report to this path.",
    )
    parser.add_argument(
        "--markdown",
        dest="markdown_out",
        type=Path,
        default=None,
        help="Write the markdown summary to this path (also printed to stdout).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for the phenopacket eval."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    paths = list(args.paths)
    if args.store_dir is not None:
        paths.append(args.store_dir)

    report = run_eval(paths, kb_dir=args.kb_dir)

    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2) + "\n")

    markdown = render_markdown(report)
    if args.markdown_out is not None:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(markdown)

    sys.stdout.write(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
