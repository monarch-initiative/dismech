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
``AggregatedPathScore`` records. Phenotype connectivity was the first plugin;
gene-to-mechanism wiring (:class:`GeneMechanismWiringPlugin`) is the source-side
complement, rewarding a causal gene being wired into the pathograph rather than
floating as an isolated genetic node.

Those two ask *whether* a gene reaches the mechanism graph.
:class:`GeneActivityGroundingPlugin` asks where it lands: GO puts a molecular
function between a gene and a biological process, and an edge from a gene
straight to a process-only node skips it. The two gene metrics are deliberately
independent -- the grounding denominator is the *wired* genes, so an unwired
gene is charged once, against wiring, rather than twice.

The same hook generically covers further graph-derived coverage metrics
(orphan-target rate, dead-end pathophysiology nodes, ...).
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from linkml_data_qc.config import QCConfig
from linkml_data_qc.models import (
    AggregatedPathScore,
    ComplianceReport,
    ThresholdViolation,
)

from dismech.graph import _genetic_item_infers_mechanism_edges, build_causal_graph
from dismech.yaml_io import safe_load

# Predicates that mechanistically *explain* a downstream node. A phenotype is
# considered "wired in" only when something causes it via one of these. A
# ``treats`` edge (treatment -> phenotype) or a ``models`` edge does not
# mechanistically explain the phenotype, so those are intentionally excluded.
#
# Environmental edges are included selectively. ``triggers`` and ``exacerbates``
# are genuine causal claims -- an exposure that initiates or amplifies a
# manifestation does explain it -- so an exposure curated directly onto a
# phenotype counts as wiring that phenotype in. The rest are deliberately left
# out: ``predisposes_to`` raises susceptibility without explaining the
# phenotype, ``protects_against`` runs the other way, and
# ``modulates``/``influences`` are non-committal by construction.
CAUSAL_PREDICATES: frozenset[str] = frozenset(
    {"causes", "leads_to", "triggers", "exacerbates"}
)

# Predicates that wire a genetic node *into* the mechanism pathograph. A genetic
# node reaches the mechanism graph when it ``contributes_to`` a pathophysiology
# node -- the gene->mechanism edge graph.py infers when a shared gene key on the
# ``genetic[].gene_term`` (or the genetic node's bare-symbol ``name``) matches a
# ``gene``/``genes`` descriptor on a ``pathophysiology`` node.
GENE_WIRING_PREDICATES: frozenset[str] = frozenset({"contributes_to"})


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


def gene_mechanism_wiring_coverage(
    data: dict[str, Any],
    predicates: frozenset[str] = GENE_WIRING_PREDICATES,
) -> tuple[int, int, list[str]]:
    """Return ``(wired, total, unwired_names)`` for causal genetic nodes.

    Measures whether a Mendelian/causal gene is actually *wired into the
    pathograph*: a top-level ``genetic`` node counts as wired when it is the
    source of at least one mechanism edge (predicate in ``predicates``) that
    reaches a pathophysiology node -- i.e. graph.py matched its gene key to a
    pathophysiology node carrying the same ``gene``/``genes`` descriptor.

    Only *mechanism-relevant* genetic items are counted in the denominator:
    items whose relationship/association marks them as BIOMARKER, PROTECTIVE,
    MODIFIER, DISPUTED, or UNKNOWN are intentionally not expected to explain a
    mechanism (see :func:`dismech.graph._genetic_item_infers_mechanism_edges`),
    so they neither help nor hurt coverage. Variant-level nodes are excluded;
    this scores the gene-level assertion, the parallel of the phenotype
    ``causal_inlink`` metric on the source side of the graph.
    """
    genetic_items = data.get("genetic", []) or []
    candidates = [
        item["name"]
        for item in genetic_items
        if isinstance(item, dict)
        and item.get("name")
        and _genetic_item_infers_mechanism_edges(item)
    ]
    total = len(candidates)
    if total == 0:
        return 0, 0, []

    graph = build_causal_graph(data)
    candidate_set = set(candidates)

    wired_sources: set[str] = set()
    for edge in graph.edges:
        if edge.predicate not in predicates:
            continue
        if edge.source == edge.target:
            continue
        if edge.source not in candidate_set:
            continue
        target = graph.nodes.get(edge.target)
        if target is not None and target.node_type == "pathophysiology":
            wired_sources.add(edge.source)

    unwired = [name for name in candidates if name not in wired_sources]
    wired = total - len(unwired)
    return wired, total, unwired


def gene_activity_grounding_coverage(
    data: dict[str, Any],
    predicates: frozenset[str] = GENE_WIRING_PREDICATES,
) -> tuple[int, int, list[str]]:
    """Return ``(grounded, total, ungrounded_names)`` for wired genetic nodes.

    GO puts a level between a gene and a process -- **gene -> molecular function
    -> biological process** -- and a pathograph edge that runs from a genetic
    node straight to a node annotated only with ``biological_processes:`` skips
    it: the graph states what the *cell* can no longer do without ever stating
    what the *protein* can no longer do.

    A wired gene counts as activity-grounded when at least one pathophysiology
    node it reaches carries ``molecular_functions:``. Every such edge is direct,
    so "the first node it links into" is any node it links into; one grounded
    landing is enough, because a gene commonly reaches both the activity node
    and its downstream consequences.

    **The denominator is the wired genes, not all of them.** An unwired gene is
    already counted against :func:`gene_mechanism_wiring_coverage`, and charging
    it here as well would penalise one defect twice while making neither number
    readable on its own. The two metrics compose: wiring asks whether the gene
    reaches the mechanism graph at all, grounding asks whether where it lands
    names a molecular function.

    A landing node carrying many genes is the case to watch. When one node
    collects twenty gene products with unrelated activities, no single MF term
    is true of it, and the fix is to split the node rather than to annotate it.
    This metric reports the gap; it does not say which of the two repairs the
    node needs.
    """
    genetic_items = data.get("genetic", []) or []
    candidates = [
        item["name"]
        for item in genetic_items
        if isinstance(item, dict)
        and item.get("name")
        and _genetic_item_infers_mechanism_edges(item)
    ]
    if not candidates:
        return 0, 0, []

    graph = build_causal_graph(data)
    candidate_set = set(candidates)
    activity_nodes = {
        item["name"]
        for item in data.get("pathophysiology", []) or []
        if isinstance(item, dict)
        and item.get("name")
        and item.get("molecular_functions")
    }

    wired: set[str] = set()
    grounded: set[str] = set()
    for edge in graph.edges:
        if edge.predicate not in predicates:
            continue
        if edge.source == edge.target or edge.source not in candidate_set:
            continue
        target = graph.nodes.get(edge.target)
        if target is None or target.node_type != "pathophysiology":
            continue
        wired.add(edge.source)
        if edge.target in activity_nodes:
            grounded.add(edge.source)

    # Count candidate *entries*, not distinct names, so this denominator is
    # exactly gene_mechanism_wiring_coverage's numerator even when an entry name
    # repeats within one file.
    wired_candidates = [name for name in candidates if name in wired]
    total = len(wired_candidates)
    if total == 0:
        return 0, 0, []
    ungrounded = [name for name in wired_candidates if name not in grounded]
    return total - len(ungrounded), total, ungrounded


class GeneMechanismWiringPlugin:
    """Coverage of causal genetic nodes wired into the mechanism pathograph.

    Emits a single ``genetic[].mechanism_outlink`` score whose ``populated`` /
    ``total`` are the wired / mechanism-relevant genetic-node counts. This is the
    source-side complement of :class:`PhenotypeConnectivityPlugin`: it rewards a
    gene being connected to a pathophysiology node (via a shared ``gene``/
    ``genes`` descriptor) rather than floating as an isolated genetic node.
    """

    path = "genetic[]"
    slot_name = "mechanism_outlink"
    parent_class = "Genetic"

    def __init__(self, predicates: frozenset[str] = GENE_WIRING_PREDICATES) -> None:
        self.predicates = predicates

    def evaluate(
        self, data: dict[str, Any], config: QCConfig
    ) -> list[AggregatedPathScore]:
        wired, total, _ = gene_mechanism_wiring_coverage(data, self.predicates)
        if total == 0:
            return []
        return [
            AggregatedPathScore(
                path=self.path,
                slot_name=self.slot_name,
                parent_class=self.parent_class,
                populated=wired,
                total=total,
                percentage=wired / total * 100,
                weight=config.get_weight(self.path, self.slot_name),
                min_compliance=config.get_min_compliance(self.path, self.slot_name),
            )
        ]


class GeneActivityGroundingPlugin:
    """Coverage of wired genes landing on a node that names a molecular function.

    Emits a single ``genetic[].mechanism_activity_grounding`` score. Paired with
    :class:`GeneMechanismWiringPlugin`, which scores the prior question: the
    wiring metric asks whether the gene reaches the mechanism graph, this one
    asks whether where it lands names the activity the gene product lost.
    """

    path = "genetic[]"
    slot_name = "mechanism_activity_grounding"
    parent_class = "Genetic"

    def __init__(self, predicates: frozenset[str] = GENE_WIRING_PREDICATES) -> None:
        self.predicates = predicates

    def evaluate(
        self, data: dict[str, Any], config: QCConfig
    ) -> list[AggregatedPathScore]:
        grounded, total, _ = gene_activity_grounding_coverage(data, self.predicates)
        if total == 0:
            return []
        return [
            AggregatedPathScore(
                path=self.path,
                slot_name=self.slot_name,
                parent_class=self.parent_class,
                populated=grounded,
                total=total,
                percentage=grounded / total * 100,
                weight=config.get_weight(self.path, self.slot_name),
                min_compliance=config.get_min_compliance(self.path, self.slot_name),
            )
        ]


DEFAULT_PLUGINS: tuple[QCMetricPlugin, ...] = (
    PhenotypeConnectivityPlugin(),
    GeneMechanismWiringPlugin(),
    GeneActivityGroundingPlugin(),
)


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

    parser = argparse.ArgumentParser(
        description=(
            "Report graph-derived pathograph-wiring coverage across dismech "
            "disorder files: phenotype causal-connectivity (inbound), "
            "gene-to-mechanism wiring (outbound), and whether a wired gene "
            "lands on a node naming a molecular function."
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
        help="QC config YAML (for weight / min_compliance on the metrics).",
    )
    parser.add_argument(
        "--fail-under",
        type=float,
        default=None,
        help="Exit non-zero if aggregate phenotype connectivity falls below this percent.",
    )
    parser.add_argument(
        "--genes-fail-under",
        type=float,
        default=None,
        help="Exit non-zero if aggregate gene-to-mechanism wiring falls below this percent.",
    )
    parser.add_argument(
        "--activity-fail-under",
        type=float,
        default=None,
        help=(
            "Exit non-zero if aggregate gene activity grounding (a wired gene "
            "landing on a node with molecular_functions) falls below this percent."
        ),
    )
    parser.add_argument(
        "--list-unconnected",
        action="store_true",
        help=(
            "List the disconnected phenotype, unwired genetic, and "
            "activity-ungrounded genetic node names per file."
        ),
    )
    args = parser.parse_args()

    config = (
        QCConfig.from_yaml(args.config)
        if Path(args.config).exists()
        else QCConfig.default()
    )
    # Effective thresholds: explicit CLI flags win, otherwise fall back to the
    # min_compliance configured for each metric in qc_config.yaml (may be None).
    pheno_plugin = PhenotypeConnectivityPlugin()
    gene_plugin = GeneMechanismWiringPlugin()
    fail_under = args.fail_under
    if fail_under is None:
        fail_under = config.get_min_compliance(
            pheno_plugin.path, pheno_plugin.slot_name
        )
    activity_plugin = GeneActivityGroundingPlugin()
    genes_fail_under = args.genes_fail_under
    if genes_fail_under is None:
        genes_fail_under = config.get_min_compliance(
            gene_plugin.path, gene_plugin.slot_name
        )
    activity_fail_under = args.activity_fail_under
    if activity_fail_under is None:
        activity_fail_under = config.get_min_compliance(
            activity_plugin.path, activity_plugin.slot_name
        )

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
    pheno_files_with_gaps = 0
    total_wired = 0
    total_genes = 0
    gene_files_with_gaps = 0
    total_grounded = 0
    total_wired_genes = 0
    activity_files_with_gaps = 0

    for path in files:
        with open(path) as fh:
            data = safe_load(fh)
        if not isinstance(data, dict):
            continue

        connected, total, unconnected = causal_inlink_coverage(data)
        if total:
            total_connected += connected
            total_phenotypes += total
            if unconnected:
                pheno_files_with_gaps += 1
                pct = connected / total * 100
                print(
                    f"{path.name}: {connected}/{total} phenotypes connected ({pct:.0f}%)"
                )
                if args.list_unconnected:
                    for name in unconnected:
                        print(f"    - phenotype: {name}")

        wired, gtotal, unwired = gene_mechanism_wiring_coverage(data)
        if gtotal:
            total_wired += wired
            total_genes += gtotal
            if unwired:
                gene_files_with_gaps += 1
                gpct = wired / gtotal * 100
                print(
                    f"{path.name}: {wired}/{gtotal} causal genes wired to mechanism "
                    f"({gpct:.0f}%)"
                )
                if args.list_unconnected:
                    for name in unwired:
                        print(f"    - gene: {name}")

        grounded, wtotal, ungrounded = gene_activity_grounding_coverage(data)
        if wtotal:
            total_grounded += grounded
            total_wired_genes += wtotal
            if ungrounded:
                activity_files_with_gaps += 1
                apct = grounded / wtotal * 100
                print(
                    f"{path.name}: {grounded}/{wtotal} wired genes land on a "
                    f"molecular function ({apct:.0f}%)"
                )
                if args.list_unconnected:
                    for name in ungrounded:
                        print(f"    - gene without an activity landing: {name}")

    failed = False

    if total_phenotypes:
        agg = total_connected / total_phenotypes * 100
        print(
            f"\nPhenotype connectivity: {total_connected}/{total_phenotypes} nodes "
            f"causally connected ({agg:.1f}%); {pheno_files_with_gaps} file(s) with gaps."
        )
        if fail_under is not None and agg < fail_under:
            print(f"FAIL: phenotype connectivity below threshold {fail_under:.1f}%")
            failed = True
    else:
        print("\nNo phenotype nodes found.")

    if total_genes:
        gagg = total_wired / total_genes * 100
        print(
            f"Gene-to-mechanism wiring: {total_wired}/{total_genes} causal genes "
            f"wired to a mechanism ({gagg:.1f}%); {gene_files_with_gaps} file(s) with gaps."
        )
        if genes_fail_under is not None and gagg < genes_fail_under:
            print(
                f"FAIL: gene-to-mechanism wiring below threshold {genes_fail_under:.1f}%"
            )
            failed = True
    else:
        print("No mechanism-relevant genetic nodes found.")

    if total_wired_genes:
        aagg = total_grounded / total_wired_genes * 100
        print(
            f"Gene activity grounding: {total_grounded}/{total_wired_genes} wired "
            f"genes land on a node naming a molecular function ({aagg:.1f}%); "
            f"{activity_files_with_gaps} file(s) with gaps."
        )
        if activity_fail_under is not None and aagg < activity_fail_under:
            print(
                f"FAIL: gene activity grounding below threshold "
                f"{activity_fail_under:.1f}%"
            )
            failed = True
    else:
        print("No wired genetic nodes found.")

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    _main()
