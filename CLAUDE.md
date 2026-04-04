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

# Fetch and cache a reference (PMID, DOI, NCT) — NEVER create cache files manually
just fetch-reference PMID:12345678

# Validate references for a single file
just validate-references kb/disorders/Asthma.yaml

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

### CURIE Prefix Casing

HGNC gene CURIEs use **lowercase** `hgnc:` prefix in this repo (e.g., `hgnc:746`, not `HGNC:746`). This is the canonical form that passes term validation. Do not flag lowercase `hgnc:` as an error in reviews.

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

### Mechanism Modules

Mechanism modules (`kb/modules/`) define conserved pathological processes that recur across
multiple disorders (e.g., the fibrotic response). A module uses the **same schema** as a
regular dismech Disease entry — it has `pathophysiology` nodes with cell types, biological
processes, evidence, and causal edges (`downstream`).

**How conformance works:**

Individual disorder entries declare that a pathophysiology node conforms to a module node
using the `conforms_to` slot:

```yaml
# In kb/disorders/Liver_Cirrhosis.yaml
pathophysiology:
- name: Hepatic Stellate Cell Activation
  conforms_to: "fibrotic_response#Mesenchymal Cell Activation"
  cell_types:
  - preferred_term: Hepatic Stellate Cell
    term:
      id: CL:0000632
      label: hepatic stellate cell
  biological_processes:
  - preferred_term: TGF-beta Receptor Signaling
    term:
      id: GO:0007179
      label: transforming growth factor beta receptor signaling pathway
    modifier: INCREASED
```

**Key principles:**
- **Same schema**: Modules validate against the `Disease` class, just like disorder files
- **Not DRY**: Disorder entries fully duplicate content; conformance is for consistency checking, not inheritance
- **Organ-specific substitution**: Module nodes define generic cell types (e.g., `fibroblast`); conforming disorder nodes substitute organ-specific types (e.g., `hepatic stellate cell`)
- **Consistency checking**: If a node declares `conforms_to`, it should include the expected biological processes and causal edges from the module
- **Reference format**: `"module_name#Node Name"` — module name matches the filename in `kb/modules/` (without `.yaml`), node name matches a pathophysiology `name` in that module

**Available modules:**
- `fibrotic_response` — Conserved fibrotic response: tissue injury → inflammation → mesenchymal cell activation → myofibroblast → excessive ECM → organ dysfunction
- `immune_checkpoint_blockade` — Conserved tumor-immune evasion pattern: neoantigen generation → anti-tumor T cell response → adaptive immune resistance (PD-L1 upregulation) → T cell exhaustion and immune escape. Drug mechanism design pattern: checkpoint inhibitor treatments use `target_mechanisms` to link back to the "Adaptive Immune Resistance" node they inhibit. Key conformance target: `immune_checkpoint_blockade#Adaptive Immune Resistance`

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

**IMPORTANT**: The `evidence_source` field classifies **the type of evidence presented in the cited publication**, NOT how the curation was performed. Even if an AI agent is curating the entry, `evidence_source` describes what kind of study the paper reports (human clinical trial, animal model, cell culture, computational simulation, etc.).

Set `evidence_source` to clarify the publication's evidence type:
- HUMAN_CLINICAL for direct human observations (default when not specified)
- MODEL_ORGANISM when citing animal model recapitulation
- IN_VITRO for cell-based experiments
- COMPUTATIONAL for in silico predictions/simulations reported in the paper
- OTHER for evidence types that do not fit the above categories
Model organism evidence should not be the only support for human phenotypes; keep it distinct via `evidence_source`.

### Entry Metadata Dates

Each `Disease` entry should include lifecycle timestamps:

```yaml
creation_date: "2025-06-12T20:16:27Z"
updated_date: "2025-07-03T11:05:10Z"
```

Rules:
- Use ISO 8601 / RFC 3339 datetime strings.
- Keep `creation_date` stable after first creation.
- Update `updated_date` whenever curated content changes.
- Prefer UTC (`Z` suffix) for consistency.

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

### `preferred_term` vs Ontology Term Labels

Each descriptor (phenotype, cell type, treatment, etc.) has two distinct label fields with different rules:

- **`term.label`**: MUST exactly match the canonical ontology term label. Verified with OAK. Never deviate from the official label.
- **`preferred_term`**: The human-readable name used in display. **This CAN be more specific or nuanced than the ontology term** when the ontology does not fully capture the desired clinical or biological granularity.

When the ontology provides only a broad parent term but you want to convey greater specificity, use a more descriptive `preferred_term` while still linking to the best-fit ontology term:

```yaml
# Example: cell type with preferred clinical name
cell_types:
- preferred_term: CD4+ regulatory T cell
  term:
    id: CL:0000815
    label: regulatory T cell

# Example: treatment more specific than generic MAXO term
treatments:
- name: Anti-TNF Biologic Therapy
  description: Treatment with TNF inhibitors such as adalimumab or infliximab.
  treatment_term:
    preferred_term: anti-TNF biologic therapy
    term:
      id: MAXO:0000058
      label: pharmacotherapy
```

**Guidelines:**
- Always link to the most specific available ontology term, even if `preferred_term` is more granular.
- If the ontology has a term that closely matches, prefer using its label as `preferred_term` for clarity.
- Use a more nuanced `preferred_term` only when the ontology term is genuinely too broad to convey the intended meaning.
- A `modifier` may be used to capture the semantics of some preferred terms.

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

### Subtype Naming Conventions

The `name` field on `Subtype` (in `has_subtypes`) serves as the **foreign key target** — other sections
(phenotypes, biochemical, genetic, prevalence, progression, histopathology) reference it via their
`subtype` field. A validation test (`test_subtype_foreign_keys`) enforces that all `subtype` values
match a defined `has_subtypes[].name`.

**Naming rules for `name`:**
- Keep names short and slug-friendly: `Type 1`, `MEN2A`, `Vascular EDS`, `FA-A`
- Avoid parenthetical qualifiers, long descriptions, or special characters
- Use `display_name` (optional) for verbose/human-readable labels when the `name` is too terse

**Example:**
```yaml
has_subtypes:
- name: Type 1
  display_name: Type 1 (Non-neuronopathic)
  description: Most common form, no CNS involvement...

phenotypes:
- name: Seizures
  subtype: Type 1    # references the short name
```

**When `display_name` is set**, renderers show it instead of `name`. When absent, `name` is displayed directly.

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

### MorPhiC Cellular Phenotypes

The MorPhiC Consortium (Molecular Phenotypes of Null Alleles in Cells) creates null alleles of human genes in iPSC-derived multicellular systems and measures their molecular and cellular phenotypes. MorPhiC data can enrich dismech entries with `category: Cellular` phenotypes.

**When to add MorPhiC-derived phenotypes:**
- The disorder involves a gene targeted by MorPhiC (check morphic.bio for gene lists)
- iPSC-derived cellular models recapitulate disease-relevant phenotypes
- Evidence source should be `IN_VITRO` for all MorPhiC-derived evidence

**Pattern for cellular phenotypes:**
```yaml
phenotypes:
- category: Cellular
  name: Impaired Cardiomyocyte Differentiation
  description: >
    Gene-null iPSC-derived cardiomyocytes show impaired differentiation...
  phenotype_term:
    preferred_term: Impaired cardiomyocyte differentiation
    term:
      id: HP:0001637
      label: Abnormal myocardium morphology
  evidence:
  - reference: PMID:39939790
    supports: SUPPORT
    evidence_source: IN_VITRO
    snippet: "exact quote from paper"
    explanation: "How MorPhiC data supports this phenotype"
```

**MorPhiC dataset references:**
```yaml
datasets:
- accession: morphic:GENE_SYMBOL
  title: MorPhiC null allele phenotyping of GENE in iPSC-derived cells
  data_type: MULTI_OMICS_PERTURBATION
  organism:
    preferred_term: human
    term:
      id: NCBITaxon:9606
      label: Homo sapiens
  publication: PMID:39939790
```

Key MorPhiC anchor genes: ISL1, EOMES, GCM1, NKX2-1. Data available under CC BY 4.0.

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



## CRITICAL: Reference Cache Files — NEVER Create Manually

Reference cache files in `references_cache/` are created EXCLUSIVELY by `linkml-reference-validator`.
**NEVER write these files by hand.** This is the #1 source of agent errors in dismech.

**Correct workflow:**
```bash
# 1. Fetch and cache the reference (creates references_cache/PMID_12345678.md)
just fetch-reference PMID:12345678

# 2. Validate that your snippet matches the cached abstract
just validate-references kb/disorders/MyDisease.yaml

# 3. If validation fails, fix the snippet or find a different PMID
just validate kb/disorders/MyDisease.yaml
```

**Why this matters:**
- `just fetch-reference` fetches the REAL abstract from PubMed and creates the cache file with the correct filename format (`PMID_` uppercase prefix), correct YAML frontmatter, and correct content
- Hand-created cache files have wrong filenames (lowercase `pmid_`), fabricated content, and wrong format
- CI validates snippets against these cached files — if the cache is fabricated, validation is meaningless

**What agents MUST do:**
1. Add YAML with `reference: PMID:XXXX` and a snippet
2. Run `just fetch-reference PMID:XXXX` for each new PMID cited
3. Run `just validate-references kb/disorders/YourFile.yaml`
4. If snippet doesn't match, fix it to be an exact quote or find a different PMID

## Git Best Practices

### What to commit

| Path | Commit? | Reason |
|------|---------|--------|
| `kb/disorders/*.yaml`, `kb/modules/*.yaml` | YES | Core content |
| `references_cache/*.md` | YES | Required for deterministic `validate-references` CI |
| `cache/**/*.csv` | YES | Required for deterministic term validation CI |
| `research/*.md` | YES | Useful provenance |
| `src/`, `scripts/`, `tests/`, `conf/` | YES | Source code |

### What NOT to commit

| Path | Commit? | Reason |
|------|---------|--------|
| `pages/disorders/*.html` | NO | Derived — regenerated by downstream CI after merge |
| `dashboard/*.html` | NO | Derived — generated by `just gen-dashboard` |
| `docs/` HTML output | NO | Derived — regenerated by CI |

### Never force-push someone else's branch
If a PR was authored by another contributor, **do not** force-push, rebase, or reset their branch. Instead:
1. Ask the original author to rebase/fix conflicts themselves
2. Or create a separate fix commit on top of their work (no force-push)
3. Only force-push branches that you (or your orchestrator) created

### Always use targeted git add
Never use `git add -A` or `git add .` in worktrees. Only stage files relevant to the task:
```bash
git add kb/disorders/ references_cache/ research/
```
This prevents committing generated files (HTML, schema docs, cache CSVs) that cause merge conflicts.

### Commit and push as final step
Every task should end with: validate → targeted git add → commit → push. Don't leave uncommitted work for someone else to discover.

### Post PR comments explaining your changes
After pushing fixes, comment on the PR summarizing:
- What you changed and why
- What you intentionally did NOT change, with reasoning
- Validation results
