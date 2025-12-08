"""Configuration models for LinkML data QC compliance analysis.

Supports configurable weights and minimum thresholds for compliance scoring.
Configuration can be loaded from YAML files.

Example config.yaml:

    default_weight: 1.0
    default_min_compliance: null

    # Per-slot defaults (apply to all occurrences of a slot)
    slots:
      term:
        weight: 2.0  # term fields are twice as important
        min_compliance: 80.0  # require at least 80% compliance
      evidence:
        weight: 1.5
      description:
        weight: 0.5  # descriptions are nice-to-have

    # Per-path overrides (more specific, takes precedence over slot config)
    paths:
      "pathophysiology[].cell_types[].term":
        weight: 3.0  # cell type terms are critical
        min_compliance: 90.0
      "phenotypes[].phenotype_term.term":
        weight: 3.0
        min_compliance: 95.0
"""

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class SlotQCConfig(BaseModel):
    """Configuration for a specific slot across all paths."""

    weight: float = Field(default=1.0, ge=0.0, description="Weight for scoring (higher = more important)")
    min_compliance: float | None = Field(
        default=None,
        ge=0.0,
        le=100.0,
        description="Minimum required compliance percentage (null = no minimum)",
    )


class PathQCConfig(BaseModel):
    """Configuration for a specific path pattern."""

    weight: float = Field(default=1.0, ge=0.0, description="Weight for scoring")
    min_compliance: float | None = Field(
        default=None,
        ge=0.0,
        le=100.0,
        description="Minimum required compliance percentage",
    )


class QCConfig(BaseModel):
    """Root configuration for QC compliance analysis.

    Precedence (highest to lowest):
    1. Path-specific config (exact match on normalized path + slot)
    2. Slot-specific config
    3. Default values
    """

    default_weight: float = Field(default=1.0, ge=0.0, description="Default weight for unspecified paths/slots")
    default_min_compliance: float | None = Field(
        default=None,
        description="Default minimum compliance (null = no minimum)",
    )

    slots: dict[str, SlotQCConfig] = Field(
        default_factory=dict,
        description="Per-slot configuration (applies to all occurrences)",
    )

    paths: dict[str, PathQCConfig] = Field(
        default_factory=dict,
        description="Per-path configuration (overrides slot config)",
    )

    def get_weight(self, path: str, slot_name: str) -> float:
        """Get the weight for a specific path+slot combination.

        Args:
            path: Normalized path (e.g., 'pathophysiology[].cell_types[]')
            slot_name: Name of the slot (e.g., 'term')

        Returns:
            Weight value, checking path config first, then slot config, then default.
        """
        # Full path includes slot name
        full_path = f"{path}.{slot_name}"

        # Check path-specific config first (highest precedence)
        if full_path in self.paths:
            return self.paths[full_path].weight

        # Check slot-specific config
        if slot_name in self.slots:
            return self.slots[slot_name].weight

        # Fall back to default
        return self.default_weight

    def get_min_compliance(self, path: str, slot_name: str) -> float | None:
        """Get the minimum compliance threshold for a specific path+slot.

        Args:
            path: Normalized path
            slot_name: Name of the slot

        Returns:
            Minimum compliance percentage, or None if no minimum set.
        """
        full_path = f"{path}.{slot_name}"

        # Check path-specific config first
        if full_path in self.paths:
            return self.paths[full_path].min_compliance

        # Check slot-specific config
        if slot_name in self.slots:
            return self.slots[slot_name].min_compliance

        # Fall back to default
        return self.default_min_compliance

    @classmethod
    def from_yaml(cls, path: str | Path) -> "QCConfig":
        """Load configuration from a YAML file."""
        with open(path) as f:
            data = yaml.safe_load(f)
        return cls.model_validate(data or {})

    @classmethod
    def default(cls) -> "QCConfig":
        """Create a default configuration with no weights or thresholds."""
        return cls()

    def to_yaml(self, path: str | Path) -> None:
        """Save configuration to a YAML file."""
        with open(path, "w") as f:
            yaml.dump(self.model_dump(exclude_none=True), f, default_flow_style=False, sort_keys=False)


class ThresholdViolation(BaseModel):
    """A compliance threshold violation."""

    path: str = Field(..., description="Full path including slot (e.g., 'phenotypes[].term')")
    slot_name: str
    actual_compliance: float = Field(..., ge=0.0, le=100.0)
    min_required: float = Field(..., ge=0.0, le=100.0)
    shortfall: float = Field(..., description="How far below threshold (min_required - actual)")


def check_thresholds(
    aggregated_scores: list[Any],  # list[AggregatedPathScore]
    config: QCConfig,
) -> list[ThresholdViolation]:
    """Check aggregated scores against configured thresholds.

    Args:
        aggregated_scores: List of AggregatedPathScore from analysis
        config: QC configuration with thresholds

    Returns:
        List of threshold violations (empty if all thresholds met)
    """
    violations = []

    for agg in aggregated_scores:
        min_compliance = config.get_min_compliance(agg.path, agg.slot_name)
        if min_compliance is not None and agg.percentage < min_compliance:
            violations.append(
                ThresholdViolation(
                    path=f"{agg.path}.{agg.slot_name}",
                    slot_name=agg.slot_name,
                    actual_compliance=agg.percentage,
                    min_required=min_compliance,
                    shortfall=min_compliance - agg.percentage,
                )
            )

    return violations
