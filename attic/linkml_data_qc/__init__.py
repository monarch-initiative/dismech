"""LinkML Data QC - Compliance analysis for recommended fields.

This module provides tools to analyze LinkML data files for compliance with
recommended field requirements. It calculates compliance percentages at various
levels of the data tree, allowing you to identify areas where recommended
ontology term bindings or other recommended fields are missing.

Example usage:

    >>> from dismech.linkml_data_qc import ComplianceAnalyzer
    >>> analyzer = ComplianceAnalyzer("src/dismech/schema/dismech.yaml")
    >>> report = analyzer.analyze_file("kb/disorders/Asthma.yaml", "Disease")
    >>> print(f"Global compliance: {report.global_compliance:.1f}%")

With configuration for weights and thresholds:

    >>> from dismech.linkml_data_qc import ComplianceAnalyzer, QCConfig
    >>> config = QCConfig.from_yaml("qc_config.yaml")
    >>> analyzer = ComplianceAnalyzer("schema.yaml", config)
    >>> report = analyzer.analyze_file("data.yaml", "Disease")
    >>> print(f"Weighted compliance: {report.weighted_compliance:.1f}%")

CLI usage:

    uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \\
        -s src/dismech/schema/dismech.yaml -t Disease -f text

    # With config file
    uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \\
        -s src/dismech/schema/dismech.yaml -t Disease \\
        -c conf/qc_config.yaml --fail-on-violations
"""

from .analyzer import ComplianceAnalyzer, analyze_directory
from .config import PathQCConfig, QCConfig, SlotQCConfig
from .formatters import (
    CSVFormatter,
    JSONFormatter,
    TextFormatter,
    create_multi_file_report,
)
from .introspector import ClassSlotMap, SchemaIntrospector, SlotInfo
from .models import (
    AggregatedPathScore,
    ComplianceReport,
    MultiFileReport,
    PathCompliance,
    SlotCompliance,
    ThresholdViolation,
)

__all__ = [
    # Main analyzer
    "ComplianceAnalyzer",
    "analyze_directory",
    # Configuration
    "QCConfig",
    "SlotQCConfig",
    "PathQCConfig",
    # Schema introspection
    "SchemaIntrospector",
    "SlotInfo",
    "ClassSlotMap",
    # Data models
    "SlotCompliance",
    "PathCompliance",
    "AggregatedPathScore",
    "ThresholdViolation",
    "ComplianceReport",
    "MultiFileReport",
    # Formatters
    "JSONFormatter",
    "CSVFormatter",
    "TextFormatter",
    "create_multi_file_report",
]
