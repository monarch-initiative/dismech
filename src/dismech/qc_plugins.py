"""Graph-derived QC metric plugins for dismech compliance scoring.

``linkml-data-qc`` scores *recommended-slot population* per object: for each
recommended slot it asks "is this slot filled on this instance?". Some quality
dimensions are not slot-population facts at all -- they are cross-object graph
properties that no ``recommended:`` flag can express. The motivating example is
**phenotype connectivity**: whether a phenotype is actually wired into the
causal pathograph (i.e. some pathophysiology node lists it as a ``downstream``
target). A phenotype can carry a perfect HPO ``term``, evidence, and
description -- full compliance credit -- yet still float as a disconnected node
in the rendered pathograph, because the edge that would connect it lives on a
*different* object's ``downstream`` list.

This module computes such properties from :func:`dismech.graph.build_causal_graph`
and emits them as :class:`linkml_data_qc.models.AggregatedPathScore` records, so
they compose with the existing weighted-compliance machinery. The score is
**graded coverage, not a binary gate**: a file with 9 of 12 phenotypes wired in
scores 75% on the ``phenotypes[].causal_inlink`` path, and that rolls into
``weighted_compliance`` and ``ThresholdViolation`` using the same
``conf/qc_config.yaml`` weight / ``min_compliance`` knobs as every other field.

The :class:`QCMetricPlugin` protocol is the generic seam: any plugin takes the
parsed disorder dict plus the active :class:`QCConfig` and returns extra
``AggregatedPathScore`` records. Connectivity is the first plugin; the same hook
generically covers other graph-derived coverage metrics (orphan-target rate,
gene-to-mechanism wiring, dead-end pathophysiology nodes, ...).
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from linkml_data_qc.config import QCConfig
from linkml_data_qc.models import AggregatedPathScore, ComplianceReport, ThresholdViolation

from dismech.graph import build_causal_graph

# Predicates that mechanistically *explain* a downstream node. A phenotype is
# considered "wired in" only when something causes it via one of these. A
# ``treats`` edge (treatment -> phenotype) or a ``models`` edge does not
# mechanistically explain the phenotype, so those are intentionally excluded.
CAUSAL_PREDICATES: frozenset[str] = frozenset({"causes", "leads_to"})


@runtime_checkable
class QCMetricPlugin(Protocol):
    """A computed QC metric that emits ``AggregatedPathScore`` records.

    Implementations derive graded coverage percentages from the parsed disorder
    data (typically via the causal graph) and return them in the same shape the
    ``linkml-data-qc`` analyzer uses for recommended-slot scores, so they slot
    straight into weighted compliance and threshold checking.
    """

    def evaluate(
        self, data: dict[str, Any], config: QCConfig
    ) -> list[AggregatedPathScore]:  # pragma: no cover - structural
        ...


def causal_inlink_coverage(
    data: dict[str, Any],
    predicates: frozenset[str] = CAUSAL_PREDICATES,
) -> tuple[int, int, list[str]]:
    """Return ``(connected, total, unconnected_names)`` for phenotype nodes.

    A phenotype node counts as connected when at least one causal edge
    (predicate in ``predicates``) targets it. Self-loops are ignored. Phenotype
    nodes are taken from the built causal graph, so they reflect exactly what the
    rendered pathograph shows.
    """
    graph = build_causal_graph(data)

    phenotype_nodes = [
        name for name, info in graph.nodes.items() if info.node_type == "phenotype"
    ]
    total = len(phenotype_nodes)
    if total == 0:
        return 0, 0, []

    inbound: set[str] = set()
    for edge in graph.edges:
        if edge.predicate in predicates and edge.target != edge.source:
            inbound.add(edge.target)

    unconnected = [name for name in phenotype_nodes if name not in inbound]
    connected = total - len(unconnected)
    return connected, total, unconnected


class PhenotypeConnectivityPlugin:
    """Coverage of phenotype nodes reached by at least one causal edge.

    Emits a single ``phenotypes[].causal_inlink`` score whose ``populated`` /
    ``total`` are the connected / total phenotype-node counts.
    """

    path = "phenotypes[]"
    slot_name = "causal_inlink"
    parent_class = "Phenotype"

    def __init__(self, predicates: frozenset[str] = CAUSAL_PREDICATES) -> None:
        self.predicates = predicates

    def evaluate(
        self, data: dict[str, Any], config: QCConfig
    ) -> list[AggregatedPathScore]:
        connected, total, _ = causal_inlink_coverage(data, self.predicates)
        if total == 0:
            return []
        return [
            AggregatedPathScore(
                path=self.path,
                slot_name=self.slot_name,
                parent_class=self.parent_class,
                populated=connected,
                total=total,
                percentage=connected / total * 100,
                weight=config.get_weight(self.path, self.slot_name),
                min_compliance=config.get_min_compliance(self.path, self.slot_name),
            )
        ]


DEFAULT_PLUGINS: tuple[QCMetricPlugin, ...] = (PhenotypeConnectivityPlugin(),)


def _weighted_compliance(scores: list[AggregatedPathScore]) -> float:
    """Recompute weighted compliance over a score list (mirrors the analyzer)."""
    if not scores:
        return 100.0
    weighted_populated = sum(s.populated * s.weight for s in scores)
    weighted_total = sum(s.total * s.weight for s in scores)
    if weighted_total == 0:
        return 100.0
    return weighted_populated / weighted_total * 100


def _violations(scores: list[AggregatedPathScore]) -> list[ThresholdViolation]:
    violations: list[ThresholdViolation] = []
    for score in scores:
        if score.min_compliance is not None and score.percentage < score.min_compliance:
            violations.append(
                ThresholdViolation(
                    path=f"{score.path}.{score.slot_name}",
                    slot_name=score.slot_name,
                    actual_compliance=score.percentage,
                    min_required=score.min_compliance,
                    shortfall=score.min_compliance - score.percentage,
                )
            )
    return violations


def augment_report(
    report: ComplianceReport,
    data: dict[str, Any],
    config: QCConfig,
    plugins: tuple[QCMetricPlugin, ...] = DEFAULT_PLUGINS,
) -> ComplianceReport:
    """Fold plugin-derived scores into a ``linkml-data-qc`` ComplianceReport.

    The extra ``AggregatedPathScore`` records are appended to
    ``report.aggregated_scores``; ``weighted_compliance`` is recomputed over the
    union, and any new threshold violations are appended. Base recommended-slot
    scores and their violations are preserved unchanged. The report is mutated in
    place and also returned for convenience.
    """
    extra: list[AggregatedPathScore] = []
    for plugin in plugins:
        extra.extend(plugin.evaluate(data, config))
    if not extra:
        return report

    report.aggregated_scores = list(report.aggregated_scores) + extra
    report.weighted_compliance = _weighted_compliance(report.aggregated_scores)
    report.threshold_violations = list(report.threshold_violations) + _violations(extra)
    return report


def _main() -> None:
    import argparse
    from pathlib import Path

    import yaml

    parser = argparse.ArgumentParser(
        description=(
            "Report phenotype causal-connectivity coverage (graph-derived QC "
            "metric) across dismech disorder files."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Disorder YAML files or directories to scan.",
    )
    parser.add_argument(
        "-c",
        "--config",
        default="conf/qc_config.yaml",
        help="QC config YAML (for weight / min_compliance on the metric).",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=None,
        help="Exit non-zero if aggregate connectivity coverage falls below this percent.",
    )
    parser.add_argument(
        "--list-unconnected",
        action="store_true",
        help="List the disconnected phenotype node names per file.",
    )
    args = parser.parse_args()

    config = (
        QCConfig.from_yaml(args.config)
        if Path(args.config).exists()
        else QCConfig.default()
    )
    # Effective threshold: explicit --fail-under wins, otherwise fall back to the
    # min_compliance configured for the metric in qc_config.yaml (may be None).
    plugin = PhenotypeConnectivityPlugin()
    fail_under = args.fail_under
    if fail_under is None:
        fail_under = config.get_min_compliance(plugin.path, plugin.slot_name)

    files: list[Path] = []
    for raw in args.paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(
                f
                for f in sorted(p.glob("*.yaml"))
                if not f.name.endswith(".history.yaml")
            )
        else:
            files.append(p)

    total_connected = 0
    total_phenotypes = 0
    files_with_gaps = 0

    for path in files:
        with open(path) as fh:
            data = yaml.safe_load(fh)
        if not isinstance(data, dict):
            continue
        connected, total, unconnected = causal_inlink_coverage(data)
        if total == 0:
            continue
        total_connected += connected
        total_phenotypes += total
        pct = connected / total * 100
        if unconnected:
            files_with_gaps += 1
            print(f"{path.name}: {connected}/{total} phenotypes connected ({pct:.0f}%)")
            if args.list_unconnected:
                for name in unconnected:
                    print(f"    - {name}")

    if total_phenotypes:
        agg = total_connected / total_phenotypes * 100
        print(
            f"\nAggregate: {total_connected}/{total_phenotypes} phenotype nodes "
            f"causally connected ({agg:.1f}%); {files_with_gaps} file(s) with gaps."
        )
        if fail_under is not None and agg < fail_under:
            print(f"FAIL: below threshold {fail_under:.1f}%")
            raise SystemExit(1)
    else:
        print("No phenotype nodes found.")


if __name__ == "__main__":
    _main()
