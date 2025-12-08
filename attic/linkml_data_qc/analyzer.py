"""Core compliance analysis logic."""

from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

from .config import QCConfig
from .introspector import SchemaIntrospector
from .models import (
    AggregatedPathScore,
    ComplianceReport,
    PathCompliance,
    SlotCompliance,
    ThresholdViolation,
)


class ComplianceAnalyzer:
    """Analyze data files for recommended field compliance."""

    def __init__(self, schema_path: str, config: QCConfig | None = None):
        """Initialize the analyzer.

        Args:
            schema_path: Path to LinkML schema YAML file
            config: Optional QC configuration for weights and thresholds.
                    If not provided, uses default config (all weights = 1.0).
        """
        self.introspector = SchemaIntrospector(schema_path)
        self.schema_path = schema_path
        self.config = config or QCConfig.default()
        self._config_path: str | None = None

    @classmethod
    def with_config_file(cls, schema_path: str, config_path: str) -> "ComplianceAnalyzer":
        """Create analyzer with configuration from a YAML file."""
        config = QCConfig.from_yaml(config_path)
        analyzer = cls(schema_path, config)
        analyzer._config_path = config_path
        return analyzer

    def analyze_file(self, data_path: str, target_class: str) -> ComplianceReport:
        """Analyze a single data file for compliance."""
        with open(data_path) as f:
            data = yaml.safe_load(f)

        path_scores: list[PathCompliance] = []
        self._analyze_object(data, target_class, "", path_scores)

        # Calculate unweighted summaries
        global_compliance, total_checks, total_populated = self._calculate_global(path_scores)
        summary_by_slot = self._summarize_by_slot(path_scores)

        # Calculate aggregated scores with weights from config
        aggregated_scores = self._aggregate_by_list_path(path_scores)

        # Calculate weighted compliance
        weighted_compliance = self._calculate_weighted_compliance(aggregated_scores)

        # Check thresholds
        threshold_violations = self._check_thresholds(aggregated_scores)

        return ComplianceReport(
            file_path=str(data_path),
            target_class=target_class,
            schema_path=self.schema_path,
            global_compliance=global_compliance,
            weighted_compliance=weighted_compliance,
            total_checks=total_checks,
            total_populated=total_populated,
            path_scores=path_scores,
            aggregated_scores=aggregated_scores,
            threshold_violations=threshold_violations,
            summary_by_slot=summary_by_slot,
            recommended_slots=list(self.introspector.recommended_slots),
            config_path=self._config_path,
        )

    def _analyze_object(
        self,
        obj: Any,
        class_name: str,
        path: str,
        results: list[PathCompliance],
    ) -> None:
        """Recursively analyze an object for compliance."""
        if obj is None:
            return

        if not isinstance(obj, dict):
            return

        class_info = self.introspector.get_class_slots(class_name)
        slot_scores: list[SlotCompliance] = []

        # Check recommended slots at this level
        for slot_name in class_info.recommended_slots:
            value = obj.get(slot_name)
            populated = 1 if self._is_populated(value) else 0
            slot_scores.append(
                SlotCompliance(
                    path=path or "(root)",
                    slot_name=slot_name,
                    populated=populated,
                    total=1,
                    percentage=100.0 if populated else 0.0,
                )
            )

        if slot_scores:
            overall = sum(s.percentage for s in slot_scores) / len(slot_scores)
            results.append(
                PathCompliance(
                    path=path or "(root)",
                    parent_class=class_name,
                    item_count=1,
                    slot_scores=slot_scores,
                    overall_percentage=overall,
                )
            )

        # Recurse into nested objects
        for slot_info in self.introspector.get_traversable_slots(class_name):
            child_data = obj.get(slot_info.name)
            if child_data is None:
                continue

            child_path = f"{path}.{slot_info.name}" if path else slot_info.name

            if slot_info.multivalued and isinstance(child_data, list):
                for i, item in enumerate(child_data):
                    self._analyze_object(item, slot_info.range, f"{child_path}[{i}]", results)
            else:
                self._analyze_object(child_data, slot_info.range, child_path, results)

    def _is_populated(self, value: Any) -> bool:
        """Check if a value counts as populated."""
        if value is None:
            return False
        if isinstance(value, str) and value.strip() == "":
            return False
        if isinstance(value, list) and len(value) == 0:
            return False
        if isinstance(value, dict) and len(value) == 0:
            return False
        return True

    def _calculate_global(
        self, path_scores: list[PathCompliance]
    ) -> tuple[float, int, int]:
        """Calculate global compliance percentage.

        Returns: (percentage, total_checks, total_populated)
        """
        if not path_scores:
            return 100.0, 0, 0

        total_checks = 0
        total_populated = 0
        for ps in path_scores:
            for ss in ps.slot_scores:
                total_checks += ss.total
                total_populated += ss.populated

        if total_checks == 0:
            return 100.0, 0, 0

        return (total_populated / total_checks) * 100, total_checks, total_populated

    def _summarize_by_slot(self, path_scores: list[PathCompliance]) -> dict[str, float]:
        """Summarize compliance by slot name."""
        slot_totals: dict[str, tuple[int, int]] = defaultdict(lambda: (0, 0))

        for ps in path_scores:
            for ss in ps.slot_scores:
                pop, tot = slot_totals[ss.slot_name]
                slot_totals[ss.slot_name] = (pop + ss.populated, tot + ss.total)

        return {
            slot: (pop / tot * 100 if tot > 0 else 100.0)
            for slot, (pop, tot) in slot_totals.items()
        }

    def _aggregate_by_list_path(
        self, path_scores: list[PathCompliance]
    ) -> list[AggregatedPathScore]:
        """Aggregate compliance scores by normalized list paths.

        Converts paths like 'pathophysiology[0].cell_types[2]' to
        'pathophysiology[].cell_types[]' and sums populated/total across
        all items matching the same normalized path.

        Only includes paths that contain list indices (i.e., have [] in normalized form).
        """
        import re

        # Key: (normalized_path, slot_name, parent_class) -> (populated, total)
        aggregates: dict[tuple[str, str, str], tuple[int, int]] = defaultdict(lambda: (0, 0))

        for ps in path_scores:
            # Normalize path: replace [N] with []
            normalized_path = re.sub(r"\[\d+\]", "[]", ps.path)

            # Only aggregate paths that actually have list indices
            if "[]" not in normalized_path:
                continue

            for ss in ps.slot_scores:
                key = (normalized_path, ss.slot_name, ps.parent_class)
                pop, tot = aggregates[key]
                aggregates[key] = (pop + ss.populated, tot + ss.total)

        # Convert to AggregatedPathScore objects with weights from config
        results = []
        for (norm_path, slot_name, parent_class), (pop, tot) in sorted(aggregates.items()):
            weight = self.config.get_weight(norm_path, slot_name)
            min_compliance = self.config.get_min_compliance(norm_path, slot_name)
            results.append(
                AggregatedPathScore(
                    path=norm_path,
                    slot_name=slot_name,
                    parent_class=parent_class,
                    populated=pop,
                    total=tot,
                    percentage=(pop / tot * 100) if tot > 0 else 100.0,
                    weight=weight,
                    min_compliance=min_compliance,
                )
            )

        return results

    def _calculate_weighted_compliance(
        self, aggregated_scores: list[AggregatedPathScore]
    ) -> float:
        """Calculate weighted compliance from aggregated scores.

        Weighted compliance = sum(populated * weight) / sum(total * weight) * 100

        This gives higher importance to paths/slots with higher weights.
        """
        if not aggregated_scores:
            return 100.0

        weighted_populated = 0.0
        weighted_total = 0.0

        for agg in aggregated_scores:
            weighted_populated += agg.populated * agg.weight
            weighted_total += agg.total * agg.weight

        if weighted_total == 0:
            return 100.0

        return (weighted_populated / weighted_total) * 100

    def _check_thresholds(
        self, aggregated_scores: list[AggregatedPathScore]
    ) -> list[ThresholdViolation]:
        """Check aggregated scores against configured minimum thresholds.

        Returns list of violations (paths that fell below their minimum).
        """
        violations = []

        for agg in aggregated_scores:
            if agg.min_compliance is not None and agg.percentage < agg.min_compliance:
                violations.append(
                    ThresholdViolation(
                        path=f"{agg.path}.{agg.slot_name}",
                        slot_name=agg.slot_name,
                        actual_compliance=agg.percentage,
                        min_required=agg.min_compliance,
                        shortfall=agg.min_compliance - agg.percentage,
                    )
                )

        return violations


def analyze_directory(
    schema_path: str,
    data_dir: str,
    target_class: str,
    pattern: str = "*.yaml",
    config: QCConfig | None = None,
    config_path: str | None = None,
) -> list[ComplianceReport]:
    """Analyze all YAML files in a directory.

    Args:
        schema_path: Path to LinkML schema
        data_dir: Directory containing data files
        target_class: Root class for validation
        pattern: Glob pattern for files (default: *.yaml)
        config: Optional QCConfig object
        config_path: Optional path to config YAML file (alternative to config)
    """
    if config_path:
        analyzer = ComplianceAnalyzer.with_config_file(schema_path, config_path)
    else:
        analyzer = ComplianceAnalyzer(schema_path, config)

    data_path = Path(data_dir)
    reports = []

    for yaml_file in sorted(data_path.glob(pattern)):
        reports.append(analyzer.analyze_file(str(yaml_file), target_class))

    return reports
