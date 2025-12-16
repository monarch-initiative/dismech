---
name: dismech-compliance
description: >
  Skill for analyzing and improving compliance in the dismech knowledge base.
  Use this skill when checking disorder file completeness, identifying missing
  fields (ontology terms, evidence, descriptions), understanding weighted
  priority scoring, and systematically improving knowledge base coverage.
---

# Dismech Compliance Analysis Skill

## Overview

Analyze and improve the completeness of disorder YAML files in the dismech knowledge base.
The compliance system checks for recommended fields (ontology terms, evidence items,
descriptions) and generates scores to identify priority curation targets.

## When to Use

- Running compliance checks on disorder files
- Identifying missing recommended fields
- Understanding which files need the most curation work
- Improving overall knowledge base quality
- Generating compliance dashboards and reports
- Understanding field priority (weighted scoring)

## Key Commands

### Analyze Single File
```bash
just compliance kb/disorders/Asthma.yaml
```

Output includes:
- **Global Compliance**: Percentage of recommended fields populated
- **Weighted Compliance**: Score adjusted by field importance
- **Summary by Slot**: Compliance grouped by field type (term, evidence, description)
- **Aggregated Scores by List Path**: Breakdown for nested structures
- **Detailed Path Scores**: Individual field status (OK/MISSING)

### Analyze All Files
```bash
just compliance-all
```

Multi-file report showing:
- Overall knowledge base compliance
- Per-path compliance across all files
- Quick identification of systematically missing fields

### Weighted Analysis with Thresholds
```bash
just compliance-weighted
```

Uses `conf/qc_config.yaml` to:
- Apply importance weights to different fields
- Flag violations where compliance falls below minimum thresholds
- Prioritize critical fields (phenotype terms, cell types, disease terms)

### Generate Reports
```bash
# CSV format for spreadsheet analysis
just compliance-csv

# JSON format for programmatic processing
just compliance-report
```

### Generate Visual Dashboard
```bash
just gen-dashboard
```

Creates `dashboard/index.html` with:
- Interactive charts showing compliance distribution
- Priority curation targets (10 lowest-scoring files)
- Trend analysis across the knowledge base

## Understanding Compliance Scores

### Global vs Weighted Compliance

| Metric | Description |
|--------|-------------|
| Global Compliance | Simple percentage: populated fields / total recommended fields |
| Weighted Compliance | Adjusted by field importance from `conf/qc_config.yaml` |

### Field Weights (from qc_config.yaml)

| Field | Weight | Min Threshold | Why |
|-------|--------|---------------|-----|
| `disease_term.term` | 5.0 | 95% | Root disease identity - always required |
| `phenotypes[].phenotype_term.term` | 3.0 | 90% | Core clinical data |
| `pathophysiology[].cell_types[].term` | 3.0 | 85% | Mechanistic understanding |
| `treatments[].treatment_term.term` | 2.5 | 80% | Clinical relevance |
| `term` (general) | 2.0 | 80% | All ontology bindings |
| `pathophysiology[].evidence` | 2.0 | 80% | Scientific backing |
| `evidence` (general) | 1.5 | - | Valuable but not always required |
| `description` | 0.5 | - | Nice-to-have context |

### Compliance Status Values

| Status | Meaning |
|--------|---------|
| OK | Field is populated |
| MISSING | Recommended field is empty/absent |

## Improving Compliance

### Priority Order

Address fields in this priority order based on weights:

1. **disease_term.term** (weight 5.0) - Add MONDO term for the disease
2. **phenotypes[].phenotype_term.term** (weight 3.0) - Add HPO terms to phenotypes
3. **pathophysiology[].cell_types[].term** (weight 3.0) - Add CL terms to cell types
4. **treatments[].treatment_term.term** (weight 2.5) - Add MAXO terms to treatments
5. **pathophysiology[].evidence** (weight 2.0) - Add PMID-backed evidence
6. **General descriptions** (weight 0.5) - Add explanatory text

### Common Fixes

#### Missing disease_term.term
```yaml
disease_term:
  preferred_term: Asthma
  term:
    id: MONDO:0004979
    label: asthma
```

Look up: `uv run runoak -i sqlite:obo:mondo info "asthma"`

#### Missing phenotype_term.term
```yaml
phenotypes:
- name: Wheezing
  phenotype_term:
    preferred_term: Wheezing
    term:
      id: HP:0030828
      label: Wheezing
```

Look up: `uv run runoak -i sqlite:obo:hp info "l~wheezing"`

#### Missing cell_types[].term
```yaml
cell_types:
- preferred_term: Mast cells
  term:
    id: CL:0000097
    label: mast cell
```

Look up: `uv run runoak -i sqlite:obo:cl info "l~mast cell"`

#### Missing treatment_term.term
```yaml
treatments:
- name: Inhaled corticosteroids
  treatment_term:
    preferred_term: corticosteroid therapy
    term:
      id: MAXO:0000653
      label: corticosteroid therapy
```

Look up: `uv run runoak -i sqlite:obo:maxo search "corticosteroid"`

#### Missing evidence
```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    snippet: "Exact quote from abstract"
    explanation: "Why this supports the claim"
```

## Batch Improvement Workflow

### 1. Identify Lowest-Scoring Files
```bash
just gen-dashboard
# Check dashboard/index.html for "Priority Curation Targets"
```

Or use compliance-all and sort:
```bash
just compliance-report | jq -r '.files | sort_by(.weighted_compliance) | .[:10] | .[].file'
```

### 2. Check Threshold Violations
```bash
just compliance-weighted 2>&1 | grep "VIOLATION"
```

### 3. Systematic Field Addition

For systematically missing fields across many files:

```python
import yaml
import glob

# Example: Find files missing disease_term.term
for f in glob.glob("kb/disorders/*.yaml"):
    with open(f) as file:
        data = yaml.safe_load(file)
    dt = data.get('disease_term', {})
    if not dt.get('term'):
        print(f"{f}: missing disease_term.term")
```

### 4. Validate After Changes
```bash
# Schema validation
just validate kb/disorders/MyDisease.yaml

# Term validation (labels match ontology)
just validate-terms-file kb/disorders/MyDisease.yaml

# Re-check compliance
just compliance kb/disorders/MyDisease.yaml
```

## Configuration

### qc_config.yaml Structure

```yaml
# Default for unconfigured fields
default_weight: 1.0
default_min_compliance: null

# Per-slot config (applies everywhere that slot appears)
slots:
  term:
    weight: 2.0
    min_compliance: 80.0

# Per-path config (overrides slot config for specific locations)
paths:
  "phenotypes[].phenotype_term.term":
    weight: 3.0
    min_compliance: 90.0
```

### Customizing Weights

Edit `conf/qc_config.yaml` to:
- Increase weight for critical fields in your workflow
- Set min_compliance thresholds to enforce standards
- Add new paths for specific validation requirements

## Integration with Other Skills

- Use **dismech-terms** skill when adding ontology term bindings
- Use **dismech-references** skill when adding evidence items
- Run `just qc` after improvements for full validation

## Troubleshooting

### "Weighted Compliance" differs significantly from "Global Compliance"
This indicates your important fields (high weight) have different coverage than low-priority fields. Focus on improving high-weight fields first.

### Many MISSING descriptions
Descriptions have low weight (0.5) and no minimum threshold. Address these last, or not at all if not needed.

### Threshold violations blocking CI
Check `conf/qc_config.yaml` for `min_compliance` settings. Either:
1. Improve the field coverage to meet the threshold
2. Lower the threshold if it's too aggressive

### Dashboard not generating
Ensure the dashboard directory exists and you have write permissions:
```bash
mkdir -p dashboard
just gen-dashboard
```
