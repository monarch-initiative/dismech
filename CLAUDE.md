# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Disorder Mechanisms Knowledge Base (dismech)** - a LinkML-based knowledge base storing disease pathophysiology information. It combines:
1. A LinkML schema defining the data model (`src/dismech/schema/dismech.yaml`)
2. A knowledge base of disorder YAML files (`kb/disorders/*.yaml`)
3. HTML rendering for browsable disorder pages (`pages/disorders/*.html`)

## Skills

Claude Code skills are available in `.claude/skills/`:

- **dismech-terms**: Use when adding ontology term annotations (HPO phenotypes, CL cell types, GO processes, MAXO treatments). Covers term lookup with OAK, specificity guidelines, and validation.
- **dismech-references**: Use when validating/repairing evidence references. Ensures snippets match PubMed abstracts and catches AI hallucinations.

## Key Commands

```bash
# Install dependencies
just install

# Run all QC checks (validation + term validation)
just qc

# Validate all disorder YAML files against schema
just validate-all

# Validate a single disorder file
just validate kb/disorders/Asthma.yaml

# Validate ontology term references in schema (anti-hallucination check)
just validate-terms

# Run pytest tests
just pytest-all

# Run a single test
uv run pytest tests/test_data.py -k "test_name" -v

# Generate HTML pages for all disorders
uv run python -m dismech.render --all

# Generate HTML for a single disorder
uv run python -m dismech.render kb/disorders/Asthma.yaml

# List all available commands
just --list
```

## Architecture

### Schema (`src/dismech/schema/dismech.yaml`)
- LinkML schema defining Disease, Pathophysiology, Phenotype, EvidenceItem, etc.
- Uses ontology term bindings (HP, GO, GENO, MONDO, MAXO, etc.) with `meaning` fields
- Dynamic enums with `reachable_from` constraints for ontology validation
- Descriptor classes (PhenotypeDescriptor, CellTypeDescriptor, TreatmentDescriptor) bind entities to ontology terms

### Knowledge Base (`kb/disorders/`)
- One YAML file per disorder (55 total)
- Each file validates against the `Disease` class in the schema
- Evidence items require PMID references
- Ontology term bindings for phenotypes, cell types, biological processes, and treatments

### Ontology Configuration (`conf/oak_config.yaml`)
Maps ontology prefixes to OAK adapters for term validation:
- HP, CL, GO, MONDO, UBERON, CHEBI, GENO, HGNC → `sqlite:obo:<name>`
- MAXO (Medical Action Ontology) for treatment terms
- NCIT (NCI Thesaurus) for cancer/treatment concepts

### HTML Rendering (`src/dismech/render.py`)
- Jinja2 templates in `src/dismech/templates/`
- Generates browsable HTML pages in `pages/disorders/`
- Links ontology terms to external browsers (HPO JAX, MONDO Monarch, OLS, etc.)

### Scripts (`scripts/`)
- `add_maxo_terms.py`: Batch-add MAXO treatment terms to disorder files

### Validation Stack
- **linkml-validate**: Schema conformance checking
- **linkml-term-validator**: Validates ontology term references against authoritative sources (critical for catching AI hallucinations)
- **linkml-reference-validator**: Validates that quoted text appears in cited references

## Important Patterns

### Evidence Items
All evidence must have PMID references and support classification:
```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT  # or REFUTE, PARTIAL, NO_EVIDENCE, WRONG_STATEMENT
    snippet: "Quoted text from the paper"
    explanation: "Why this evidence supports/refutes the claim"
```

### Ontology Term Mappings
When adding enum values with `meaning` fields, the description MUST exactly match the ontology term's canonical label. Use OAK to verify:
```bash
uv run runoak -i sqlite:obo:hp info HP:0040282 -O obo
```

This prevents AI hallucination of fake or mismatched ontology terms.

### Treatment Terms (MAXO)
Treatments can be annotated with Medical Action Ontology (MAXO) terms:
```yaml
treatments:
- name: Physical Therapy
  description: Rehabilitation exercises to improve mobility.
  treatment_term:
    preferred_term: physical therapy
    term:
      id: MAXO:0000011
      label: physical therapy
```

Common MAXO terms:
- `MAXO:0000058` - pharmacotherapy (drug treatments)
- `MAXO:0000004` - surgical procedure
- `MAXO:0000011` - physical therapy
- `MAXO:0000079` - genetic counseling
- `MAXO:0000088` - dietary intervention
- `MAXO:0000647` - chemotherapy
- `MAXO:0000014` - radiation therapy
- `MAXO:0001017` - vaccination
- `MAXO:0010039` - organ transplantation
- `MAXO:0000950` - supportive care

Use OAK to search for MAXO terms:
```bash
uv run runoak -i sqlite:obo:maxo search "physical therapy"
```

## Testing

Tests are in `tests/test_data.py`:
- Schema validation for all 55 disorder files
- Required field checks
- Evidence reference validation
- Unique name verification
