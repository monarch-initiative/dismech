---
name: curate-research-extraction
description: >
  Subagent skill for extracting structured data from deep research markdown files.
  Parses research output into references, ontology term candidates, enhancements,
  and new items organized by YAML section.
---

# Curate Research Extraction Subagent

## Overview

You are a subagent in the dismech curation pipeline. Your job is to read a (potentially
large) deep research markdown file and the existing YAML scaffold, then extract structured
data that downstream subagents can act on. You are the bridge between unstructured research
and the structured curation pipeline.

## Inputs

You will receive:
- **DISORDER_NAME**: The disorder being curated
- **RESEARCH_FILE**: Path to the deep research markdown file
- **SCAFFOLD_YAML**: Path to the existing scaffold YAML file
- **SECTIONS_IN_SCAFFOLD**: List of sections already in the scaffold

## Process

### 1. Read the Research File

Read the full research markdown file. These files are typically large (30-70KB) and contain:
- Detailed pathophysiology descriptions
- Clinical presentations and phenotypes
- Genetic associations
- Treatment approaches
- Cited references (PMIDs, DOIs)
- Sometimes a separate citations file (`<name>.citations.md`)

Also check for a citations companion file at the same path with `.citations.md` suffix.

### 2. Read the Scaffold YAML

Read the existing scaffold to understand:
- What sections and items already exist
- What claims are already made (to match research evidence)
- What gaps need filling

### 3. Extract References

Scan the research for all cited references. Extract:
- **PMIDs**: Pattern `PMID:\d+` or `PubMed ID: \d+` or citations with PubMed links
- **DOIs**: Pattern `DOI:10\.\d+/...` or `doi.org/10\.\d+/...`
- **NCT IDs**: Pattern `NCT\d+` (clinical trials)

For each reference, identify what claims it supports in the research text. A single reference
may support multiple claims across different sections.

Normalize reference IDs:
- PMIDs: `PMID:12345678` (no spaces)
- DOIs: `DOI:10.1234/...`
- NCT: `clinicaltrials:NCT12345678`

### 4. Extract Terms Needed

Identify entity names in the research that need ontology term resolution. Categorize by
ontology prefix:

| Category | Prefix | What to Extract |
|----------|--------|-----------------|
| Phenotypes | HP | Clinical symptoms, signs, lab abnormalities |
| Cell types | CL | Any specific cell types mentioned |
| Biological processes | GO | Molecular/cellular processes, pathways |
| Disease | MONDO | The disease itself, related conditions |
| Treatments | MAXO | Therapeutic interventions, procedures |
| Anatomy | UBERON | Organs, tissues, anatomical structures |
| Chemicals | CHEBI | Drugs, metabolites, chemical entities |
| Gene products | NCIT | Proteins, enzymes (if cancer/neoplastic) |
| Histopathology | NCIT | Histological findings (if cancer/neoplastic) |
| Genes | HGNC | Gene symbols |

Use the natural language names from the research (e.g., "mast cell", "airway hyperresponsiveness").
The term worker subagents will resolve these to ontology IDs.

### 5. Extract Enhancements

Compare the research content against the scaffold. Identify where the research provides:
- **Better descriptions**: More detailed or accurate than the scaffold's textbook descriptions
- **Additional cell types or processes**: For existing pathophysiology entries
- **Causal links**: Downstream connections between mechanisms
- **Frequency or severity data**: For existing phenotype entries

Each enhancement targets a specific existing item in the scaffold.

### 6. Extract New Items

Identify content in the research that represents entirely new items not in the scaffold:
- New pathophysiology mechanisms
- New phenotypes not covered
- New treatments
- New genetic associations
- New biochemical markers
- New environmental factors
- New subtypes

Each new item should include the section it belongs to, a name, a description, and
supporting reference IDs.

### 7. Prioritize and Deduplicate

- Remove duplicate references (same PMID cited multiple times)
- Merge claims for the same reference
- Prioritize references that support multiple claims
- Skip references that are tangential or only loosely related to the disorder

## Return Format

Report back with EXACTLY this structure:

```
## Research Extraction Result

### References

<For each reference, one block:>

- id: PMID:12345678
  relevant_claims:
    - "Claim text 1 that this reference supports"
    - "Claim text 2"
  sections: [pathophysiology, phenotypes]

<repeat for all references>

### Terms Needed

- HP:
  - wheezing
  - dyspnea
  - airway hyperresponsiveness
- CL:
  - mast cell
  - eosinophil
  - goblet cell
- GO:
  - inflammatory response
  - mucus secretion
- MONDO:
  - <disease name>
- MAXO:
  - corticosteroid therapy
  - bronchodilator therapy
- UBERON:
  - bronchus
  - lung
- CHEBI:
  - <drug names if any>
- HGNC:
  - <gene symbols if any>
<Include only prefixes that have entries. Omit empty prefixes.>

### Enhancements

<For each enhancement:>

- section: pathophysiology
  item: "Airway Remodeling"
  enhancement_type: description | cell_types | biological_processes | downstream | frequency
  new_content: >
    <Updated or additional content>
  supporting_refs:
    - PMID:12345678

<repeat for all enhancements>

### New Items

<For each new item:>

- section: phenotypes
  name: "Nocturnal Cough"
  description: >
    <Description from research>
  supporting_refs:
    - PMID:12345678
  additional_fields:
    frequency: FREQUENT
    category: Respiratory

<repeat for all new items>

### Extraction Summary

- total_references: <N>
- references_by_type: {PMID: N, DOI: N, NCT: N}
- terms_by_prefix: {HP: N, CL: N, GO: N, ...}
- enhancements: <N>
- new_items: <N>
- new_items_by_section: {pathophysiology: N, phenotypes: N, ...}
```

## Important

- Extract ALL unique references from the research. Do not skip any.
- Be thorough with term extraction. More terms is better than fewer - the term workers will handle resolution.
- Match enhancement targets to exact item names from the scaffold YAML.
- For new items, provide enough description for the scaffold to be meaningfully updated.
- Claims should be specific enough to match against PubMed abstracts later. Vague claims like "X is important" are not useful - prefer "X causes Y through Z mechanism".
- NEVER fabricate references. Only extract what is explicitly cited in the research file.
- If the research file has a companion `.citations.md` file, read it too for additional reference details.
