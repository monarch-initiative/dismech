# LinkML Data QC

A generic compliance analysis tool for LinkML data files. This module calculates compliance percentages for `recommended: true` slots defined in LinkML schemas.

## Features

- **Hierarchical scoring**: Calculate compliance at multiple levels (global, path-level, per-item)
- **Aggregated list scoring**: Roll up scores across list elements using jq-style `[]` notation
- **Configurable weights**: Assign importance weights to paths and slots
- **Threshold violations**: Set minimum compliance requirements and detect violations
- **Multiple output formats**: JSON, CSV, and human-readable text
- **Multi-file reports**: Aggregate compliance across an entire knowledge base

## Quick Start

### Python API

```python
from dismech.linkml_data_qc import ComplianceAnalyzer

# Basic usage
analyzer = ComplianceAnalyzer("path/to/schema.yaml")
report = analyzer.analyze_file("path/to/data.yaml", "Disease")

print(f"Global compliance: {report.global_compliance:.1f}%")
print(f"Weighted compliance: {report.weighted_compliance:.1f}%")

# With configuration file
analyzer = ComplianceAnalyzer.with_config_file(
    "path/to/schema.yaml",
    "path/to/qc_config.yaml"
)
report = analyzer.analyze_file("path/to/data.yaml", "Disease")

if report.threshold_violations:
    print(f"Found {len(report.threshold_violations)} violations!")
```

### Command Line

```bash
# Single file analysis
uv run python -m dismech.linkml_data_qc.cli kb/disorders/Asthma.yaml \
    -s src/dismech/schema/dismech.yaml \
    -t Disease \
    -f text

# Analyze all files in a directory
uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
    -s src/dismech/schema/dismech.yaml \
    -t Disease \
    -f json

# With configuration and threshold enforcement
uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
    -s src/dismech/schema/dismech.yaml \
    -t Disease \
    -c conf/qc_config.yaml \
    --fail-on-violations
```

## CLI Options

| Option | Description |
|--------|-------------|
| `data_path` | Data file(s) or directory to analyze (positional, can be multiple) |
| `-s, --schema` | Path to LinkML schema YAML (required) |
| `-t, --target-class` | Target class name for validation (required) |
| `-c, --config` | Path to QC configuration YAML file |
| `-f, --format` | Output format: `json`, `csv`, `text` (default: text) |
| `-o, --output` | Output file path (default: stdout) |
| `--min-compliance` | Minimum global compliance percentage (exit 1 if below) |
| `--fail-on-violations` | Exit with error code if any threshold violations occur |
| `--pattern` | Glob pattern for directory search (default: `*.yaml`) |

## How It Works

### Schema Introspection

The module uses LinkML's `SchemaView` to identify slots marked with `recommended: true`:

```yaml
# In your LinkML schema
slots:
  description:
    description: Human-readable description
    recommended: true  # This slot will be tracked

  term:
    description: Ontology term binding
    recommended: true  # This slot will be tracked
```

### Recursive Analysis

The analyzer recursively traverses your data, tracking:
- Which recommended slots are present at each location
- The path to each object (e.g., `pathophysiology[0].cell_types[2]`)
- The LinkML class of each object

### Aggregation Levels

Results are computed at multiple levels:

1. **Per-item scores**: Each object gets compliance scores for its recommended slots
   ```
   pathophysiology[0]: description=100%, term=0%
   pathophysiology[1]: description=100%, term=100%
   ```

2. **Aggregated list scores**: Rolled up by normalized path with `[]` notation
   ```
   pathophysiology[].description: 100% (2/2)
   pathophysiology[].term: 50% (1/2)
   ```

3. **Nested aggregation**: Lists within lists are also aggregated
   ```
   pathophysiology[].cell_types[].term: 80% (8/10)
   ```

4. **Global scores**: Overall compliance across all paths

## Configuration

Create a YAML configuration file to customize weights and thresholds:

```yaml
# qc_config.yaml

# Default weight for all paths/slots not otherwise configured
default_weight: 1.0

# Default minimum compliance (null = no minimum required)
default_min_compliance: null

# Per-slot configuration (applies to all occurrences of a slot)
slots:
  term:
    weight: 2.0  # Ontology term bindings are important
    min_compliance: 80.0  # Require at least 80% term coverage
  evidence:
    weight: 1.5  # Evidence is valuable but not always required
    min_compliance: null
  description:
    weight: 0.5  # Descriptions are nice-to-have

# Per-path configuration (overrides slot config for specific paths)
# Use jq-style [] notation for list paths
paths:
  # Phenotype terms are critical
  "phenotypes[].phenotype_term.term":
    weight: 3.0
    min_compliance: 90.0

  # Cell type terms in pathophysiology are very important
  "pathophysiology[].cell_types[].term":
    weight: 3.0
    min_compliance: 85.0

  # Disease term at root should always be present
  "disease_term.term":
    weight: 5.0
    min_compliance: 95.0
```

### Configuration Precedence

When looking up weight or threshold for a path+slot combination:

1. **Path-specific config** (highest priority): Exact match on `path.slot_name`
2. **Slot-specific config**: Applies to all occurrences of that slot
3. **Default values**: Falls back to `default_weight` or `default_min_compliance`

### Weighted Compliance

When weights are configured, the `weighted_compliance` score is calculated as:

```
weighted_compliance = sum(populated_i * weight_i) / sum(total_i * weight_i) * 100
```

This allows you to emphasize important paths (like ontology term bindings) over less critical ones (like descriptions).

## Output Formats

### Text Output

Human-readable format with hierarchical display:

```
Compliance Report: kb/disorders/Asthma.yaml
Target Class: Disease
Global Compliance: 65.3% (125/191)
Weighted Compliance: 71.2%
Config: conf/qc_config.yaml

Summary by Slot:
  description: 78.4%
  evidence: 45.2%
  term: 72.1%

Threshold Violations (2):
  pathophysiology[].evidence: 45.2% < 80.0% (shortfall: 34.8%)
  treatments[].treatment_term.term: 70.0% < 80.0% (shortfall: 10.0%)

Aggregated Scores by List Path:
  pathophysiology[].description: 100.0% (5/5)
  pathophysiology[].term: 80.0% (4/5)
  pathophysiology[].cell_types[].term: 85.7% (12/14)
  phenotypes[].phenotype_term.term: 95.0% (19/20)
```

### JSON Output

Structured output for programmatic processing:

```json
{
  "file_path": "kb/disorders/Asthma.yaml",
  "target_class": "Disease",
  "global_compliance": 65.3,
  "weighted_compliance": 71.2,
  "total_checks": 191,
  "total_populated": 125,
  "summary_by_slot": {
    "description": 78.4,
    "evidence": 45.2,
    "term": 72.1
  },
  "aggregated_scores": [
    {
      "path": "pathophysiology[]",
      "slot_name": "description",
      "parent_class": "Pathophysiology",
      "populated": 5,
      "total": 5,
      "percentage": 100.0,
      "weight": 1.5,
      "min_compliance": 70.0
    }
  ],
  "threshold_violations": [
    {
      "path": "pathophysiology[].evidence",
      "slot_name": "evidence",
      "actual_compliance": 45.2,
      "min_required": 80.0,
      "shortfall": 34.8
    }
  ]
}
```

### CSV Output

Flat format for spreadsheet analysis:

```csv
file,path,class,slot,populated,total,percentage
kb/disorders/Asthma.yaml,pathophysiology[0],Pathophysiology,description,1,1,100.0
kb/disorders/Asthma.yaml,pathophysiology[0],Pathophysiology,term,1,1,100.0
kb/disorders/Asthma.yaml,pathophysiology[0].cell_types[0],CellTypeDescriptor,term,1,1,100.0
```

## Data Models

All results are Pydantic models for type safety and serialization:

### SlotCompliance

Compliance score for a single slot at a specific path:

```python
class SlotCompliance(BaseModel):
    slot_name: str      # e.g., "term"
    populated: int      # Number of items with field populated
    total: int          # Total items checked
    percentage: float   # 0-100
```

### PathCompliance

Compliance scores for all recommended slots at a specific path:

```python
class PathCompliance(BaseModel):
    path: str                    # e.g., "pathophysiology[0].cell_types[2]"
    parent_class: str            # e.g., "CellTypeDescriptor"
    item_count: int              # Number of items at this path
    slot_scores: list[SlotCompliance]
    overall_percentage: float    # Average across slots
```

### AggregatedPathScore

Aggregated score across list elements:

```python
class AggregatedPathScore(BaseModel):
    path: str           # e.g., "pathophysiology[].cell_types[]"
    slot_name: str      # e.g., "term"
    parent_class: str
    populated: int
    total: int
    percentage: float
    weight: float       # From configuration
    min_compliance: float | None
```

### ThresholdViolation

A compliance threshold violation:

```python
class ThresholdViolation(BaseModel):
    path: str                  # e.g., "phenotypes[].term"
    slot_name: str
    actual_compliance: float
    min_required: float
    shortfall: float           # min_required - actual
```

### ComplianceReport

Complete report for a single file:

```python
class ComplianceReport(BaseModel):
    file_path: str
    target_class: str
    schema_path: str
    global_compliance: float
    weighted_compliance: float
    total_checks: int
    total_populated: int
    path_scores: list[PathCompliance]
    aggregated_scores: list[AggregatedPathScore]
    summary_by_slot: dict[str, float]
    threshold_violations: list[ThresholdViolation]
    recommended_slots: list[str]
    config_path: str | None
    timestamp: datetime
```

### MultiFileReport

Aggregated report across multiple files:

```python
class MultiFileReport(BaseModel):
    files_analyzed: int
    reports: list[ComplianceReport]
    global_compliance: float
    weighted_compliance: float
    summary_by_slot: dict[str, float]
    summary_by_path: dict[str, float]
    threshold_violations: list[ThresholdViolation]
```

## Integration with CI/CD

Use the CLI with exit codes for CI integration:

```bash
# Fail if global compliance is below 70%
uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
    -s src/dismech/schema/dismech.yaml \
    -t Disease \
    --min-compliance 70

# Fail if any configured threshold is violated
uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
    -s src/dismech/schema/dismech.yaml \
    -t Disease \
    -c conf/qc_config.yaml \
    --fail-on-violations
```

Exit codes:
- `0`: All checks passed
- `1`: Compliance below threshold or violations detected

## Just Recipes

If using `just`, add these recipes:

```just
# Run compliance analysis on all disorders
compliance-all:
    uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
        -s src/dismech/schema/dismech.yaml -t Disease -f text

# Analyze a single file
compliance file:
    uv run python -m dismech.linkml_data_qc.cli {{file}} \
        -s src/dismech/schema/dismech.yaml -t Disease -f text

# Generate JSON report
compliance-report:
    uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
        -s src/dismech/schema/dismech.yaml -t Disease -f json \
        -o reports/compliance.json

# Check thresholds (CI mode)
compliance-check:
    uv run python -m dismech.linkml_data_qc.cli kb/disorders/ \
        -s src/dismech/schema/dismech.yaml -t Disease \
        -c conf/qc_config.yaml --fail-on-violations
```

## API Reference

### ComplianceAnalyzer

Main analyzer class:

```python
class ComplianceAnalyzer:
    def __init__(self, schema_path: str, config: QCConfig | None = None):
        """Create analyzer with schema and optional configuration."""

    @classmethod
    def with_config_file(cls, schema_path: str, config_path: str) -> "ComplianceAnalyzer":
        """Create analyzer loading configuration from YAML file."""

    def analyze_file(self, data_path: str, target_class: str) -> ComplianceReport:
        """Analyze a single data file for compliance."""
```

### QCConfig

Configuration class:

```python
class QCConfig(BaseModel):
    default_weight: float = 1.0
    default_min_compliance: float | None = None
    slots: dict[str, SlotQCConfig] = {}
    paths: dict[str, PathQCConfig] = {}

    @classmethod
    def from_yaml(cls, path: str) -> "QCConfig":
        """Load configuration from YAML file."""

    @classmethod
    def default(cls) -> "QCConfig":
        """Create default configuration with no weights or thresholds."""

    def get_weight(self, path: str, slot_name: str) -> float:
        """Get weight for path+slot, respecting precedence rules."""

    def get_min_compliance(self, path: str, slot_name: str) -> float | None:
        """Get minimum threshold for path+slot, respecting precedence rules."""
```

### Formatters

Output formatters:

```python
class JSONFormatter:
    @staticmethod
    def format(report: ComplianceReport) -> str
    @staticmethod
    def format_multi(report: MultiFileReport) -> str

class CSVFormatter:
    @staticmethod
    def format(report: ComplianceReport) -> str
    @staticmethod
    def format_multi(report: MultiFileReport) -> str

class TextFormatter:
    @staticmethod
    def format(report: ComplianceReport, show_details: bool = True) -> str
    @staticmethod
    def format_multi(report: MultiFileReport) -> str
```

### Helper Functions

```python
def create_multi_file_report(reports: list[ComplianceReport]) -> MultiFileReport:
    """Aggregate multiple single-file reports into a multi-file report."""

def analyze_directory(
    schema_path: str,
    directory: str,
    target_class: str,
    pattern: str = "*.yaml",
    config: QCConfig | None = None
) -> MultiFileReport:
    """Convenience function to analyze all files in a directory."""
```

## Module Structure

```
src/dismech/linkml_data_qc/
├── __init__.py       # Public API exports
├── analyzer.py       # ComplianceAnalyzer class
├── cli.py           # Command-line interface
├── config.py        # QCConfig and related models
├── formatters.py    # JSON, CSV, Text formatters
├── introspector.py  # Schema introspection utilities
├── models.py        # Pydantic data models
└── README.md        # This documentation
```

## Future Improvements

- Schema annotations for per-slot configuration (alternative to config file)
- Historical trend tracking with timestamp comparison
- HTML report generation
- Integration with linkml-validate for combined reporting
- Support for custom metadata beyond `recommended`
