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
    evidence_source: HUMAN_CLINICAL  # or MODEL_ORGANISM, IN_VITRO, COMPUTATIONAL
    snippet: "Quoted text from the paper"
    explanation: "Why this evidence supports/refutes the claim"
```

Set `evidence_source` to clarify provenance:
- HUMAN_CLINICAL for direct human observations (default when not specified)
- MODEL_ORGANISM when citing animal model recapitulation
- IN_VITRO for cell-based experiments
- COMPUTATIONAL for in silico predictions
- OTHER for evidence types that do not fit the above categories
Model organism evidence should not be the only support for human phenotypes; keep it distinct via `evidence_source`.

Quick classification rules (use these before tagging):
- HUMAN_CLINICAL: human patients, cohorts, case reports, clinical trials (NCT), epidemiology.
- MODEL_ORGANISM: any in vivo animal data (mouse, zebrafish, dog/cat/horse veterinary case series, primate, or other non-human animals), even if observational and not interventional.
- IN_VITRO: cultured cells or tissue explants (human or animal), organoids, ex vivo slices, biochemical assays outside an organism.
- COMPUTATIONAL: in silico modeling, docking, simulations, ML predictions, network/pathway inference without wet-lab confirmation.
- OTHER: anything that does not cleanly fit above (e.g., expert consensus without data, pathology image atlases without linked cohort context).

Edge cases:
- Veterinary observations are MODEL_ORGANISM (non-human mammals are still animal models for this purpose).
- In silico “modeling studies” belong to COMPUTATIONAL, even if they use clinical datasets as input.
- If a paper mixes sources, split evidence items so each item gets a single `evidence_source`.

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

### Clinical Trials

Clinical trials can be added to disease entries with evidence validated against ClinicalTrials.gov:

```yaml
clinical_trials:
- name: NCT05813288
  phase: Phase III
  status: Completed
  description: Brief description of the trial's objective and approach
  target_phenotypes:
    - preferred_term: Wheezing
      term:
        id: HP:0030828
        label: Wheezing
    - preferred_term: Breathlessness
      term:
        id: HP:0002094
        label: Dyspnea
  evidence:
    - reference: clinicaltrials:NCT05813288
      supports: SUPPORT
      snippet: "Exact quote from the trial summary"
      explanation: "Why this trial is relevant to the disease"
```

**Fetching trial data:**
```bash
just fetch-reference NCT05813288  # Caches trial data from ClinicalTrials.gov API
```

**Key fields:**
- `name`: NCT identifier (e.g., NCT05813288)
- `phase`: Trial phase (Phase I, II, III, IV)
- `status`: Recruitment status (Recruiting, Completed, Terminated, Active not recruiting)
- `target_phenotypes`: Phenotypes addressed by the trial (with HP ontology terms)
- `evidence`: Evidence items validated against ClinicalTrials.gov

## Testing

Tests are in `tests/test_data.py`:
- Schema validation for all 56 disorder files
- Required field checks
- Evidence reference validation
- Unique name verification

## Standard Operating Procedure: Adding/Editing Evidence

When adding or editing evidence items in disorder files, follow this SOP to prevent hallucinations:

### 1. Never Fabricate Snippets

Evidence snippets MUST be exact quotes from the cited paper's abstract. Do not paraphrase.

**Wrong:**
```yaml
evidence:
  - reference: PMID:12345678
    snippet: The study showed that X causes Y through Z mechanism.  # Paraphrase - will fail validation
```

**Correct:**
```yaml
evidence:
  - reference: PMID:12345678
    snippet: "X causes Y through the Z mechanism, as demonstrated by..."  # Exact quote from abstract
```

### 2. Verify PMIDs Before Use

Always check that a PMID actually corresponds to the paper you think it does:

```bash
# Check cached abstract (if previously fetched)
cat references_cache/pmid_12345678.md

# Or fetch fresh and validate
just validate-references kb/disorders/MyDisease.yaml
```

### 3. Validation Workflow

Before committing changes to any disorder file:

```bash
# 1. Schema validation (structure correct)
just validate kb/disorders/MyDisease.yaml

# 2. Reference validation (snippets match abstracts)
just validate-references kb/disorders/MyDisease.yaml

# 3. Term validation (ontology IDs/labels correct)
just validate-terms-file kb/disorders/MyDisease.yaml
```

### 4. When Evidence Cannot Be Verified

If a claim is well-established but you cannot find a quotable snippet:

- **Option A**: Move the claim to the `notes` field (no evidence required)
- **Option B**: Find a different paper with a quotable abstract
- **Option C**: Remove the evidence block entirely, keep the description

**Do NOT** fabricate quotes or use incorrect PMIDs.

### 5. Common Validation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Text part not found as substring" | Snippet is paraphrased | Use exact quote from abstract |
| "Reference not found" | PMID doesn't exist | Verify PMID on PubMed |
| Low similarity score | Wrong PMID for the paper | Check abstract matches topic |

### 6. Running Full QC

```bash
# All validation checks
just qc

# Compliance analysis (recommended field coverage)
just compliance-all

# With weighted scoring and threshold checks
just compliance-weighted

# Generate visual dashboard (dashboard/index.html)
just gen-dashboard
```

The dashboard shows priority curation targets - the 10 files with lowest compliance scores.
