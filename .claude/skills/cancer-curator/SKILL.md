---
name: cancer-curator
description: >
  Skill for curating cancer and neoplastic disease entries in the dismech knowledge base.
  Use this skill when creating or enhancing cancer entries, adding oncogene/tumor suppressor
  pathophysiology, curating histopathology findings, adding targeted therapy information,
  and linking genetic drivers to treatment responses. Covers fusion genes, two-hit hypothesis,
  oncogene addiction, and precision oncology concepts.
---

# Cancer Curation Skill

## Overview

Curate cancer and neoplastic disease entries in the dismech knowledge base with a focus on:
- Genetic drivers (oncogenes, tumor suppressors, fusion genes)
- Pathophysiology with causal chains
- Histopathology findings
- Targeted therapies and their molecular targets
- NCIT terms for biomarkers, gene products, and histologic findings

## When to Use

- Creating new cancer/neoplasm entries
- Adding genetic driver information (BCR-ABL, KIT, RET, RB1, etc.)
- Structuring pathophysiology as atomic processes with causal links
- Adding histopathology findings (grades, patterns, rosettes)
- Linking treatments to their molecular targets
- Adding CHEBI terms for chemotherapy drugs
- Adding NCIT terms for biomarkers and fusion proteins

## Cancer-Specific Schema Features

### Disease Stages (not Subtypes)

For cancers with disease phases (chronic → accelerated → blast crisis), use `stages` not `has_subtypes`:

```yaml
stages:
- name: Chronic Phase
  description: >-
    Initial indolent phase with <10% blasts. Most patients diagnosed here.
- name: Accelerated Phase
  description: >-
    Transitional phase with 10-19% blasts, additional cytogenetic abnormalities.
- name: Blast Crisis
  description: >-
    Terminal phase resembling acute leukemia with ≥20% blasts.
```

Use `has_subtypes` for true molecular/histologic subtypes (KIT-mutant vs PDGFRA-mutant GIST).

### Pathophysiology: Atomic Processes with Causal Chains

Split bundled pathway descriptions into atomic processes linked by `downstream` edges:

```yaml
pathophysiology:
- name: BCR-ABL1 Fusion Oncogene Formation
  description: >-
    The t(9;22) translocation creates the Philadelphia chromosome with
    constitutively active BCR-ABL1 tyrosine kinase.
  cell_types:
  - preferred_term: hematopoietic stem cell
    term:
      id: CL:0000037
      label: hematopoietic stem cell
  gene_products:
  - preferred_term: BCR-ABL1 fusion protein
    term:
      id: NCIT:C16325
      label: BCR/ABL1 Fusion Protein
  downstream:
  - target: Constitutive Tyrosine Kinase Activation
    description: BCR-ABL1 exhibits ligand-independent kinase activity

- name: Constitutive Tyrosine Kinase Activation
  description: >-
    BCR-ABL1 activates RAS-MAPK, PI3K-AKT, and JAK-STAT pathways.
  biological_processes:
  - preferred_term: protein tyrosine kinase activity
    modifier: INCREASED
    term:
      id: GO:0004713
      label: protein tyrosine kinase activity
  downstream:
  - target: Uncontrolled Myeloid Proliferation
    description: Activated signaling drives excessive myeloid expansion
```

**Key principles:**
1. One mechanism per entry (not "Oncogenic Signaling" combining MAPK + PI3K)
2. Use `downstream` to connect cause → effect
3. Include `cell_types`, `biological_processes`, `locations` as appropriate
4. Add `gene_products` for fusion proteins/oncoproteins (NCIT terms)

### Histopathology Section

Use the dedicated `histopathology` section for microscopic findings:

```yaml
histopathology:
- name: Flexner-Wintersteiner Rosettes
  finding_term:
    preferred_term: Flexner-Wintersteiner rosette
    term:
      id: HP:0031927
      label: Flexner-Wintersteiner rosette
  frequency: FREQUENT
  diagnostic: true
  description: >-
    Characteristic rosettes with central lumen surrounded by tumor cells
    showing photoreceptor differentiation. Pathognomonic for retinoblastoma.

- name: Spindle Cell Morphology
  finding_term:
    preferred_term: Spindle Cell Pattern
    term:
      id: NCIT:C53643
      label: Spindle Cell Pattern
  frequency: VERY_FREQUENT
  description: >-
    Elongated cells arranged in fascicles. Typical of KIT-mutant GIST.
```

**Histopathology term sources:**
- NCIT:C35867 (Morphologic Finding) - patterns, dysplasia, necrosis
- NCIT:C18000 (Histologic Grade) - Fuhrman, Nottingham, GIST grades
- HP:0025461 (Abnormal cell morphology) - rosettes, inclusion bodies

### Biomarkers (NCIT)

Add `biomarker_term` to biochemical entries:

```yaml
biochemical:
- name: BCR-ABL1 Fusion Transcript
  biomarker_term:
    preferred_term: BCR-ABL1 fusion protein
    term:
      id: NCIT:C36715
      label: BCR-ABL1 Fusion Protein Expression
  notes: >-
    RT-PCR or FISH detection is diagnostic and used for molecular monitoring.
```

### Gene Products (NCIT)

Add `gene_products` to pathophysiology for fusion proteins and oncoproteins:

```yaml
gene_products:
- preferred_term: BCR-ABL1 fusion protein
  term:
    id: NCIT:C16325
    label: BCR/ABL1 Fusion Protein
```

Look up NCIT gene product terms:
```bash
uv run runoak -i sqlite:obo:ncit descendants NCIT:C26548 --predicates rdfs:subClassOf | grep -i "fusion\|kinase"
```

### Therapeutic Agents (CHEBI)

Add `therapeutic_agent` to treatments with CHEBI terms:

```yaml
treatments:
- name: Imatinib
  description: First-generation TKI targeting BCR-ABL1.
  treatment_term:
    preferred_term: pharmacotherapy
    term:
      id: MAXO:0000058
      label: pharmacotherapy
    therapeutic_agent:
    - preferred_term: imatinib
      term:
        id: CHEBI:45783
        label: imatinib
```

## Ontology Lookups

### NCIT Gene Products
```bash
# Search for fusion proteins
uv run runoak -i sqlite:obo:ncit search "fusion protein"

# Check specific term
uv run runoak -i sqlite:obo:ncit info NCIT:C16325

# Get descendants of Gene Product
uv run runoak -i sqlite:obo:ncit descendants NCIT:C26548 --predicates rdfs:subClassOf | head -50
```

### NCIT Histopathology
```bash
# Morphologic findings
uv run runoak -i sqlite:obo:ncit descendants NCIT:C35867 --predicates rdfs:subClassOf | head -50

# Histologic grades
uv run runoak -i sqlite:obo:ncit descendants NCIT:C18000 --predicates rdfs:subClassOf | head -50
```

### CHEBI Drugs
```bash
uv run runoak -i sqlite:obo:chebi search "imatinib"
uv run runoak -i sqlite:obo:chebi info CHEBI:45783
```

### HP Rosettes and Cell Morphology
```bash
uv run runoak -i sqlite:obo:hp descendants HP:0025461 --predicates rdfs:subClassOf | grep -i rosette
```

## Common NCIT Terms

### Fusion Proteins
| Term | ID | Cancer |
|------|-----|--------|
| BCR/ABL1 Fusion Protein | NCIT:C16325 | CML |
| Mast/Stem Cell Growth Factor Receptor Kit | NCIT:C17328 | GIST |
| Proto-Oncogene Tyrosine-Protein Kinase Receptor Ret | NCIT:C18539 | MTC |

### Biomarkers
| Term | ID | Use |
|------|-----|-----|
| BCR-ABL1 Fusion Protein Expression | NCIT:C36715 | CML monitoring |
| Calcitonin | NCIT:C2281 | MTC tumor marker |
| Carcinoembryonic Antigen | NCIT:C16384 | MTC, colorectal |

### Histologic Grades
| Term | ID | Cancer |
|------|-----|--------|
| Fuhrman Nuclear Grade | NCIT:C62411 | Renal cell carcinoma |
| GIST Histologic Grade | NCIT:C160731 | GIST |
| Nottingham Grade | NCIT:C138986 | Breast cancer |

### Morphologic Findings
| Term | ID | Finding |
|------|-----|---------|
| Spindle Cell Pattern | NCIT:C53643 | Elongated cell morphology |
| Low Mitotic Activity | NCIT:C35961 | <5 mitoses/50 HPF |
| Fleurette Formation | NCIT:C35950 | Retinoblastoma differentiation |

## Common CHEBI Drug Terms

### TKIs
| Drug | CHEBI ID |
|------|----------|
| imatinib | CHEBI:45783 |
| dasatinib | CHEBI:49375 |
| nilotinib | CHEBI:52172 |
| ponatinib | CHEBI:78543 |
| sunitinib | CHEBI:38940 |

### Chemotherapy
| Drug | CHEBI ID |
|------|----------|
| carboplatin | CHEBI:31355 |
| vincristine | CHEBI:27375 |
| etoposide | CHEBI:4911 |
| doxorubicin | CHEBI:28748 |
| cyclophosphamide | CHEBI:4026 |

## Cancer Tiers (from CANCER.md project)

### Tier 1: Paradigmatic Single-Gene Drivers
Clear driver mutations with targeted therapies:
- CML (BCR-ABL1) → imatinib
- GIST (KIT/PDGFRA) → imatinib/avapritinib
- MTC (RET) → selpercatinib
- ccRCC (VHL) → belzutifan
- Retinoblastoma (RB1) → two-hit paradigm
- Ewing Sarcoma (EWS-FLI1) → fusion transcription factor

### Tier 2: Hereditary Cancer Syndromes
Germline mutations with defined progression:
- Li-Fraumeni (TP53)
- FAP (APC)
- VHL disease
- MEN2 (RET)
- HBOC (BRCA1/2)
- NF1

### Tier 3: Molecular Subtype Cancers
- AML (FLT3, NPM1, IDH1/2)
- Colorectal (CMS subtypes)
- Breast (HER2+)
- Melanoma (BRAF)
- Glioblastoma (IDH-mutant vs wildtype)

## Validation Workflow

```bash
# 1. Schema validation
just validate kb/disorders/MyCancer.yaml

# 2. Term validation (NCIT, CHEBI, HP, CL, GO)
just validate-terms kb/disorders/MyCancer.yaml

# 3. Reference validation (if evidence added)
just validate-references kb/disorders/MyCancer.yaml

# 4. Full QC
just qc
```

## Example: Creating a New Cancer Entry

1. **Start with deep research** (if available):
   ```bash
   # Check for existing research
   ls research/*MyCancer*.md
   ```

2. **Create YAML structure**:
   - name, description, categories, parents
   - disease_term (MONDO)
   - has_subtypes or stages (as appropriate)
   - pathophysiology (atomic, with causal chains)
   - histopathology (if relevant)
   - phenotypes
   - biochemical (with biomarker_term)
   - genetic
   - treatments (with treatment_term + therapeutic_agent)

3. **Add evidence** for key claims (PMID references)

4. **Validate** all term bindings

## Integration with Other Skills

- **dismech-terms**: For general ontology term lookups (HP, CL, GO, MONDO)
- **dismech-references**: For evidence validation and PMID snippet checking
- **dismech-compliance**: For checking field coverage

## Project Tracking

Cancer curation is tracked in `projects/CANCER.md`. Update status after completing entries.
