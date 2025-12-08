"""Pydantic models for LinkML data compliance analysis results."""

from datetime import datetime
from pydantic import BaseModel, Field


class SlotCompliance(BaseModel):
    """Compliance measurement for a single recommended slot at a path."""

    path: str = Field(..., description="Data path, e.g., 'pathophysiology.cell_types'")
    slot_name: str = Field(..., description="Name of recommended slot")
    populated: int = Field(..., ge=0, description="Count of items with slot populated")
    total: int = Field(..., ge=0, description="Total items at this path")
    percentage: float = Field(..., ge=0, le=100, description="Compliance percentage")


class PathCompliance(BaseModel):
    """Aggregated compliance for all recommended slots at a specific data path."""

    path: str = Field(..., description="Data path in the tree")
    parent_class: str = Field(..., description="LinkML class at this path")
    item_count: int = Field(..., ge=0, description="Number of items at this path")
    slot_scores: list[SlotCompliance] = Field(default_factory=list)
    overall_percentage: float = Field(..., ge=0, le=100)


class AggregatedPathScore(BaseModel):
    """Aggregated compliance across all items at a list path.

    Uses jq-style [] notation to indicate aggregation over list members.
    E.g., 'pathophysiology[].description' aggregates across all pathophysiology items.
    E.g., 'pathophysiology[].cell_types[].term' aggregates across all nested items.
    """

    path: str = Field(
        ...,
        description="Aggregated path using [] notation, e.g., 'pathophysiology[].cell_types[]'",
    )
    slot_name: str = Field(..., description="Name of the recommended slot")
    parent_class: str = Field(..., description="LinkML class at this path")
    populated: int = Field(..., ge=0, description="Sum of populated across all items")
    total: int = Field(..., ge=0, description="Sum of total across all items")
    percentage: float = Field(..., ge=0, le=100, description="Compliance percentage")
    weight: float = Field(default=1.0, ge=0.0, description="Configured weight for this path+slot")
    min_compliance: float | None = Field(
        default=None,
        description="Configured minimum compliance threshold (if any)",
    )


class ThresholdViolation(BaseModel):
    """A compliance threshold violation."""

    path: str = Field(..., description="Full path including slot (e.g., 'phenotypes[].term')")
    slot_name: str
    actual_compliance: float = Field(..., ge=0.0, le=100.0)
    min_required: float = Field(..., ge=0.0, le=100.0)
    shortfall: float = Field(..., description="How far below threshold (min_required - actual)")


class ComplianceReport(BaseModel):
    """Complete compliance analysis report for a data file."""

    file_path: str = Field(..., description="Path to analyzed data file")
    target_class: str = Field(..., description="Root LinkML class for validation")
    schema_path: str = Field(..., description="Path to LinkML schema")
    global_compliance: float = Field(..., ge=0, le=100, description="Overall compliance percentage (unweighted)")
    weighted_compliance: float = Field(
        ...,
        ge=0,
        le=100,
        description="Weighted compliance percentage (using configured weights)",
    )
    total_checks: int = Field(..., ge=0, description="Total compliance checks performed")
    total_populated: int = Field(..., ge=0, description="Total fields that were populated")
    path_scores: list[PathCompliance] = Field(
        default_factory=list,
        description="Detailed per-item scores (e.g., pathophysiology[0], pathophysiology[1])",
    )
    aggregated_scores: list[AggregatedPathScore] = Field(
        default_factory=list,
        description="Aggregated scores at list level (e.g., pathophysiology[].description)",
    )
    threshold_violations: list[ThresholdViolation] = Field(
        default_factory=list,
        description="List of paths that fell below their minimum compliance threshold",
    )
    summary_by_slot: dict[str, float] = Field(
        default_factory=dict,
        description="Slot name -> overall compliance percentage",
    )
    recommended_slots: list[str] = Field(
        default_factory=list,
        description="List of recommended slots found in schema",
    )
    config_path: str | None = Field(
        default=None,
        description="Path to QC config file used (if any)",
    )
    timestamp: datetime = Field(default_factory=datetime.now)


class MultiFileReport(BaseModel):
    """Aggregated report across multiple data files."""

    files_analyzed: int = Field(..., ge=0)
    reports: list[ComplianceReport] = Field(default_factory=list)
    global_compliance: float = Field(..., ge=0, le=100, description="Unweighted compliance")
    weighted_compliance: float = Field(..., ge=0, le=100, description="Weighted compliance")
    summary_by_slot: dict[str, float] = Field(
        default_factory=dict,
        description="Slot name -> overall compliance percentage across all files",
    )
    summary_by_path: dict[str, float] = Field(
        default_factory=dict,
        description="Path -> overall compliance percentage across all files",
    )
    threshold_violations: list[ThresholdViolation] = Field(
        default_factory=list,
        description="Aggregated threshold violations across all files",
    )
