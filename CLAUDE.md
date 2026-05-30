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

### Structured-Database Sources (`src/dismech/structured_sources/`)
- Framework for ingesting structured knowledge bases (Orphanet, ClinGen; OMIM /
  MONDO / HGNC pluggable) into `references_cache/` as line-oriented markdown
- Flagship: `OrphanetSource` — pre-caches all 8,823 leaf disorders from
  Orphadata XML so curators can cite `ORPHA:<code>` and quote individual rows
  (definition, prevalence, HPO phenotypes, gene-disease, xrefs)
- `ClinGenSource` — pre-caches ClinGen Gene-Disease Validity assertions from
  the public CSV so curators can cite `CGGV:<assertion_id>` and quote the
  gene-disease validity row
- See "Structured-Database Reference Sources" below

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
- `dna_repair_synthetic_lethality` — Conserved HRR/FA-BRCA deficiency pattern: HRR or FA/BRCA repair deficiency → replication-associated DNA damage accumulation → PARP/platinum synthetic lethality → POLQ/error-prone repair escape → restored HRR and acquired resistance. Key conformance target: `dna_repair_synthetic_lethality#PARP and Platinum Synthetic Lethality`
- `rtk_grb2_signaling_adaptation` — Conserved RTK/GRB2 adaptor pattern: activated RTK phosphotyrosine docking → GRB2 adaptor hub → RAS-MAPK/PI3K-AKT proliferation output, with an emerging GRB2-RAD51 replication-fork protection branch. Key conformance target: `rtk_grb2_signaling_adaptation#GRB2 Adaptor Hub`
- `parp_parg_macrodomain_viral_evasion` — Conserved antiviral ADP-ribosylation pattern: viral/interferon PARP induction → NAD-dependent antiviral ADP-ribosylation → PARG/host reset → viral macrodomain de-ADP-ribosylation countermeasure → enhanced viral replication/pathogenesis. Key conformance target: `parp_parg_macrodomain_viral_evasion#Viral Macrodomain De-ADP-Ribosylation Countermeasure`
- `lysosomal_substrate_accumulation` — Conserved lysosomal storage disease pattern: lysosomal hydrolase/cofactor deficiency → undegraded substrate accumulation in the lysosome → autophagic-lysosomal dysfunction and secondary cascade → storage-cell cytotoxicity and neuroinflammation → progressive multisystem/neurodegenerative disease. Conforming disorder nodes substitute the disorder-specific deficient enzyme, stored substrate, and storage cell type (e.g., glucocerebrosidase/glucocerebroside/Gaucher cell; hexosaminidase/GM2 ganglioside/neuron; alpha-galactosidase A/Gb3/endothelium). Key conformance target: `lysosomal_substrate_accumulation#Lysosomal Substrate Accumulation`
- `aortopathy_tgfbeta_dysregulation` — Conserved heritable thoracic aortic aneurysm/dissection (TAAD) pattern: aortic-wall ECM or smooth-muscle contractile-apparatus defect → paradoxically increased TGF-beta signaling dysregulation → medial degeneration (smooth muscle cell depletion + elastic fiber fragmentation) and wall weakening → progressive aortic dilation/aneurysm → aortic dissection and rupture. Conforming disorder nodes substitute the disorder-specific primary lesion (FBN1 microfibril deficiency in Marfan/Shprintzen-Goldberg; TGFBR1/2, SMAD3, TGFB2/3 in Loeys-Dietz; COL3A1 in vascular Ehlers-Danlos; SLC2A10 in arterial tortuosity; ACTA2/MYH11/MYLK/PRKG1 in nonsyndromic familial TAAD). Key conformance target: `aortopathy_tgfbeta_dysregulation#TGF-beta Signaling Dysregulation`

**Module-level hypotheses and gaps:**
- Modules may define `mechanistic_hypotheses` just like disease entries. Use stable `hypothesis_group_id` values for canonical, alternative, or emerging mechanism groupings.
- Causal edges opt into those groups with `downstream[].hypothesis_groups`. In conforming disorder entries, copy and specialize the same grouping only when the disease-specific causal edge belongs to that model.
- Knowledge gaps should currently use `discussions` with `kind: KNOWLEDGE_GAP`, `attaches_to`, and optional `proposed_experiments`. A separate structural `knowledge_gaps:` slot is still a schema follow-up; do not invent it in YAML entries yet.

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

Each `Disease` entry should include a creation timestamp:

```yaml
creation_date: "2025-06-12T20:16:27Z"
```

Rules:
- Use ISO 8601 / RFC 3339 datetime strings.
- Keep `creation_date` stable after first creation.
- Prefer UTC (`Z` suffix) for consistency.
- **Do not add `updated_date` to new entries.** The field is deprecated — git history is the authoritative change log. Existing entries that still carry `updated_date` may retain it until a future bulk cleanup.

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

### Descriptor Qualifier Slots

Common clinical qualifiers on ontology-bound descriptors should use explicit slots on
the descriptor object rather than the deprecated generic `qualifiers` list:

- `temporality`: `ACUTE`, `TRANSIENT`, `SUBACUTE`, `CHRONIC`, `RECURRENT`,
  `DIURNAL`, `NOCTURNAL`, `PROLONGED`
- `clinical_course`: `PROGRESSIVE`, `STABLE`
- `severity`: prefer enum-backed values (`MILD`, `MODERATE`, `SEVERE`) when the qualifier
  is part of the ontology post-composition; free text is still tolerated for legacy
  phenotype/context summaries
- `onset`: structured `OnsetDescriptor` with `onset_category` and optional age fields

Pattern:
```yaml
phenotype_term:
  preferred_term: Diarrhea
  term:
    id: HP:0002014
    label: Diarrhea
  temporality: CHRONIC

phenotype_term:
  preferred_term: Muscle weakness
  term:
    id: HP:0001324
    label: Muscle weakness
  clinical_course: PROGRESSIVE
```

Use these first-class slots for common post-composition. Reserve `qualifiers` for
more complex predicate-value patterns that are not covered by dedicated slots.

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

### Treatment Terms (MAXO or NCIT)
Treatments can be annotated with Medical Action Ontology (MAXO) terms or NCI Thesaurus (NCIT)
clinical intervention terms. NCIT often provides more specific procedure and therapy terms
than MAXO. Use whichever ontology has the most specific and accurate term for the treatment.

```yaml
# MAXO example
treatments:
- name: Physical Therapy
  description: Rehabilitation exercises to improve mobility.
  treatment_term:
    preferred_term: physical therapy
    term:
      id: MAXO:0000011
      label: physical therapy

# NCIT example
treatments:
- name: Orthopedic Surgery
  description: Corrective surgery for skeletal deformities.
  treatment_term:
    preferred_term: orthopedic surgical procedure
    term:
      id: NCIT:C16186
      label: Orthopedic Surgical Procedure
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

Common NCIT clinical intervention terms:
- `NCIT:C49236` - Therapeutic Procedure
- `NCIT:C15329` - Surgical Procedure
- `NCIT:C16186` - Orthopedic Surgical Procedure
- `NCIT:C15302` - Physical Therapy
- `NCIT:C15315` - Rehabilitation
- `NCIT:C15747` - Supportive Care

Use OAK to search for terms:
```bash
uv run runoak -i sqlite:obo:maxo search "physical therapy"
uv run runoak -i sqlite:obo:ncit info "l^Physical Therap"
```

#### Therapeutic Agent Pattern (drug + drug class on pharmacotherapy)

MAXO treatment terms describe the **medical action** (e.g., pharmacotherapy, chemotherapy,
vaccination) but not the specific agent involved. When the action is generic but a
specific drug or drug class is involved, combine the MAXO action term with the
`therapeutic_agent` slot, which is multivalued and bindable to CHEBI (for specific drugs)
or NCIT (for drug classes).

**When to use `therapeutic_agent`:**
- `treatment_term` is a generic MAXO action like `MAXO:0000058` (pharmacotherapy),
  `MAXO:0000647` (chemotherapy), `MAXO:0001017` (vaccination), or `MAXO:0000014` (radiation therapy)
- A specific drug, chemical, or drug class is referenced in the `name` / `description`
- You want the treatment to be machine-queryable by drug identity

**Ontology selection:**
- **CHEBI**: preferred for specific small-molecule drugs (`CHEBI:36796` duloxetine, `CHEBI:46345` 5-fluorouracil)
- **NCIT**: use for drug classes, or for biologics/newer drugs that lack a CHEBI term
  (`NCIT:C20401` Monoclonal Antibody, `NCIT:C2322` Corticosteroid, `NCIT:C65216` Adalimumab)
- Leave `therapeutic_agent` absent when the treatment is non-pharmacological
  (surgery, physical therapy, counseling, dietary intervention — use `dietary_modifications` for the latter)

**Example — single specific drug (CHEBI):**
```yaml
treatments:
- name: Duloxetine
  description: SNRI, FDA-approved for fibromyalgia chronic pain management.
  treatment_term:
    preferred_term: pharmacotherapy
    term:
      id: MAXO:0000058
      label: pharmacotherapy
    therapeutic_agent:
    - preferred_term: duloxetine
      term:
        id: CHEBI:36796
        label: duloxetine
```

**Example — drug class (NCIT) when CHEBI is too specific:**
```yaml
treatments:
- name: Anti-TNF Biologic Therapy
  description: TNF inhibitors such as adalimumab or infliximab.
  treatment_term:
    preferred_term: anti-TNF biologic therapy
    term:
      id: MAXO:0000058
      label: pharmacotherapy
    therapeutic_agent:
    - preferred_term: monoclonal antibody
      term:
        id: NCIT:C20401
        label: Monoclonal Antibody
```

**Example — combination therapy (multivalued):**
```yaml
treatments:
- name: FOLFIRINOX
  description: Combination chemotherapy regimen for pancreatic adenocarcinoma.
  treatment_term:
    preferred_term: chemotherapy
    term:
      id: MAXO:0000647
      label: chemotherapy
    therapeutic_agent:
    - preferred_term: fluorouracil
      term:
        id: CHEBI:46345
        label: 5-fluorouracil
    - preferred_term: irinotecan
      term:
        id: CHEBI:80630
        label: irinotecan
    - preferred_term: oxaliplatin
      term:
        id: CHEBI:31941
        label: oxaliplatin
```

**Guidelines:**
- `therapeutic_agent` is optional at the schema level but **recommended whenever `treatment_term` is MAXO:0000058** or another generic action term where a specific drug is involved.
- Use OAK to verify CHEBI terms: `uv run runoak -i sqlite:obo:chebi search "duloxetine"`
- For NCIT drug-class terms, the local `ncit` adapter is configured in `conf/oak_config.yaml`.
- A dedicated `treatment.name` (e.g., "Duloxetine") should still match common clinical usage; `therapeutic_agent` carries the machine-readable identifier.
- Do NOT put the drug name in `preferred_term` on `treatment_term` — `preferred_term` describes the action (pharmacotherapy), `therapeutic_agent.preferred_term` describes the agent.

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

### 2a. Deep-Research (Falcon/DR) Tool Outputs — Extra Verification Needed

Deep-research tools (Falcon, DGO, etc.) synthesize information across many sources but are **known to fabricate or misattribute citations, misquote snippets, and invent ontology identifiers**. When using DR outputs for curation:

**Treat DR outputs as *leads*, not ground truth.** Every PMID, snippet, and ontology term from a DR summary must be independently verified before committing.

**Three categories of hallucination risk:**
1. **Fabricated PMIDs** — The cited paper does not exist, or the PMID belongs to an unrelated paper
2. **Misquoted snippets** — The snippet is paraphrased or invented rather than an exact quote from the real abstract
3. **Invented ontology terms** — HP, GO, CL, MAXO, CHEBI, or NCIT identifiers that don't exist or whose canonical label doesn't match `term.label`

**Mandatory verification workflow for any curation step sourced from DR:**
1. For **each new PMID** cited: run `just fetch-reference PMID:XXXX` to fetch the real abstract
2. For **each snippet**: manually verify it is an exact substring of the abstract by comparing against the cached file in `references_cache/PMID_XXXX.md`
3. For **each ontology term** (HP, GO, CL, MAXO, CHEBI, NCIT): verify the term exists and its canonical label matches `term.label` by running `just validate-terms-file kb/disorders/YourDisease.yaml`
4. Run the full validation suite before committing (see Validation Workflow below)

If a DR-suggested citation cannot be verified against the real abstract, do not use it. Find an alternative source or remove the claim entirely.

**Historical note:** Issue #1737 audited DR-sourced entries and found ~1% hallucination rate in the cache layer — the dismech validation stack catches these errors, but only *after* the curator runs the checks. Treating DR outputs as leads rather than ground truth is the most reliable protection.

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

### 6. Frequency Qualifiers Need Their Own Evidence

Phenotype `frequency:` values (FREQUENT, OCCASIONAL, etc.) make a *separate*
quantitative claim from the disease–phenotype association itself. Most snippets
support only the association, not the band. See
[`docs/frequency-evidence-guidelines.md`](docs/frequency-evidence-guidelines.md)
for the curator SOP: acceptable evidence patterns (direct quantitative,
derived counts, qualitative-term mapping, clinical estimate), the literature-term
→ enum mapping table, and worked examples. **When in doubt, omit `frequency:`
rather than fabricate justification.**

### 7. Running Full QC

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

**Deterministic cache contract check (dismech#871):**
`just check-reference-cache-frontmatter` validates that every
`references_cache/*.md` file has parseable YAML frontmatter matching the local
`linkml-reference-validator` cache contract and filename/reference_id mapping.
It runs as part of `just qc` before the heavier validators. This is still only
a structural check — `validate-references` remains the last defence against a
snippet matching the wrong cached paper.

**Agent guardrail:** Claude Code and Codex must never create or hand-edit
`references_cache/*.md`. If a cache file is wrong or malformed, regenerate it
with `just fetch-reference <ID>` instead of patching the frontmatter manually.

## Structured-Database Reference Sources

In addition to fetched literature references (PMID, DOI, NCT), dismech ingests
structured knowledge bases — currently **Orphanet** and **ClinGen** — into
`references_cache/` as deterministic line-oriented markdown files. Each file
holds one entity (one ORPHA disorder) and curators can quote individual rows
as evidence `snippet:` values.

**Available structured prefixes:**

| Prefix | Source | Coverage | License |
|--------|--------|----------|---------|
| `ORPHA:` | Orphadata bulk XML | 8,823 leaf disorders + subtypes | CC-BY 4.0 |
| `CGGV:` | ClinGen Gene-Disease Validity CSV | One record per gene-disease validity assertion | ClinGen terms |
| `CGDS:` | ClinGen Dosage Sensitivity downloads | One record per dosage-sensitive gene | ClinGen terms |
| `CIVIC_ASSERTION:`, `CIVIC_EID:` | CIViC accepted assertion and clinical evidence TSVs | One record per accepted CIViC assertion or evidence item | CIViC |

**Citing an Orphanet entry:**

```yaml
evidence:
  - reference: ORPHA:558
    supports: SUPPORT
    snippet: "Marfan syndrome is a systemic disease of connective tissue"
    explanation: Orphadata definition supports this characterization.
```

Snippets must be exact substrings of the cache file's body. The body uses
markdown section headings (`## Definition`, `## Inheritance`, `## Phenotypes`,
`## Genes`, `## Epidemiology`, `## Cross-references`, `## Source`) with
markdown tables for tabular data. Each table row is a stable quotable
substring across refreshes:

```
| HP:0002616 | Aortic root aneurysm | Very frequent (99-80%) |
| FBN1 | fibrillin-1 | hgnc:3603 | Disease-causing germline mutation(s) in |
| MONDO:0007947 | Exact |
```

A curator-quoted snippet may include or omit the leading and trailing
pipes — both substring-match against the cached body. Prefer the
unbracketed form for cleaner YAML:

```yaml
snippet: "HP:0002616 | Aortic root aneurysm | Very frequent (99-80%)"
```

**Citing a ClinGen gene-disease validity assertion:**

```yaml
evidence:
  - reference: CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z
    supports: SUPPORT
    snippet: "HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | Definitive"
    explanation: ClinGen classifies the HEXB-Sandhoff disease relationship as definitive.
```

ClinGen cache bodies contain a `## Evidence summary` section when the
assertion report page has ClinGen narrative text, plus a `## Gene-disease
validity` markdown table:

```
## Evidence summary

In summary, HEXB is definitively associated with Sandhoff disease.

## Gene-disease validity

| Gene | HGNC | Disease | MONDO | MOI | Classification | SOP | GCEP | Classification date |
| HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | Definitive | SOP9 | Lysosomal Diseases Gene Curation Expert Panel | 2022-09-15T16:00:00.000Z |
```

**Citing a ClinGen dosage sensitivity assertion:**

```yaml
evidence:
  - reference: CGDS:HGNC_9585
    supports: SUPPORT
    snippet: "PTCH1 | HGNC:9585 | 5727 | 9q22.32 | chr9:95442980-95516971 | 3 - Sufficient Evidence for Haploinsufficiency | 0 - No Evidence for Triplosensitivity | 2020-07-01"
    explanation: ClinGen dosage sensitivity supports PTCH1 haploinsufficiency as a disease mechanism.
```

ClinGen dosage cache bodies contain a `## Gene dosage sensitivity` table and,
when available, report-page narrative for haploinsufficiency and
triplosensitivity evidence.

**How the cache is built:**

```bash
# 1. Refresh the bulk XML pinned in data/orphadata/MANIFEST.yaml
just refresh-orphadata

# 2. Rebuild every references_cache/ORPHA_*.md
just structured-rebuild-orphanet

# Or rebuild a single ID
just structured-rebuild-orphanet --id 558

# ClinGen Gene-Disease Validity CSV
just clingen-refresh
just clingen-list
just clingen-rebuild
just clingen-rebuild --id CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z

# Use --csv-only to skip fetching report-page narrative during a fast rebuild
just clingen-rebuild --csv-only --id CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z

# ClinGen Dosage Sensitivity CSV/TSV
just clingen-dosage-refresh
just clingen-dosage-list
just clingen-dosage-rebuild
just clingen-dosage-rebuild --id CGDS:HGNC_9585
```

`data/orphadata/*.xml` is gitignored; `data/orphadata/MANIFEST.yaml` is
committed and pins the snapshot date + sha256 of each bulk file. To verify
no drift has occurred, run `just structured-rebuild-orphanet` locally and
check `git diff references_cache/ORPHA_*.md`. (A CI workflow that does this
automatically is a worthwhile follow-up but does not yet exist.)

**Adding a new structured source:**

The framework is in `src/dismech/structured_sources/`. To add a new source
(OMIM, MONDO, HGNC, …):

1. Subclass `StructuredSource` (`base.py`) and implement `build_index`,
   `identifiers`, `serialize`.
2. Pin bulk-data files in `data/<source>/MANIFEST.yaml`.
3. Register a CLI entry in `src/dismech/structured_sources/cli.py`.
4. Use the same UniProt-flat-file-style line layout — fixed column widths,
   sorted within each tag block — so curator-quoted snippets remain valid
   across refreshes.

**Agent guardrail:** Like literature cache files, `references_cache/ORPHA_*.md`
must NEVER be hand-edited. Regenerate via `just structured-rebuild-orphanet`.

## Git/GitHub Best Practices

### Open PRs from origin, not forks

Do not open PRs from forks. GitHub does not expose repository secrets to
fork-triggered workflows, so fork PRs will not receive automated AI review. Push
branches directly to `origin`; new contributors should first open an issue
requesting repository access.

### Use worktrees

Use worktrees for parallel feature work. The **primary checkout** (wherever you cloned the repo) must always stay on `main`. Feature branches go in worktrees only.

- Never check out `main` in a worktree — `main` belongs to the primary checkout.
- Never leave the primary checkout on a feature branch.
- If `git checkout main` fails with "already checked out at …", find which worktree holds `main` (`git worktree list | grep '\[main\]'`), switch that worktree to a feature branch, then retry.

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

### Refresh your own branch safely
Refreshing a PR branch with `main` is a content-changing operation, not bookkeeping.
For branches you own:
1. Prefer `git fetch origin && git rebase origin/main`
2. If the branch is stale or conflict-heavy, create a fresh branch from `origin/main` and cherry-pick only the intended commits
3. Avoid routine `git merge origin/main` into PR branches
4. After any refresh, review:
```bash
git diff --name-status origin/main...HEAD
git diff --stat origin/main...HEAD
```
5. If you see unrelated deletions, stale reversions, or protected-path churn, stop and fix that before commit/push
6. If merge/rebase/cherry-pick reports conflicts or index errors, do not commit or push until the operation is clean and the post-refresh diff has been reviewed

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

### Reviews

Your PR will always be removed by an automated Claude reviewer. This usually happens within a few minutes.
The reviewer will mark your PR as being ready to merge or requiring changes. Be sure to address all changes.
Try and address even "optional" changes if they improve overall quality and completion.

If you disagree you can say so, but provide clearly articulated arguments in the PR comments. Never get
into back and forth. If something cannot be resolved, stop, and assign a human like @cmungall to the PR, and ask
them to facilitate.

Note that sometimes it will appear that a review has stalled, but in fact this is usually because
the PR is in conflict. Actively try and manage this, resolve conflicts carefully.
