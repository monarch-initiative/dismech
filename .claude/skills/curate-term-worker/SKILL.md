---
name: curate-term-worker
description: >
  Subagent skill for resolving ontology terms using OAK. Receives an ontology prefix
  and a list of entity names, performs lookups, checks specificity, and returns resolved
  term objects ready for assembly.
---

# Curate Term Worker Subagent

## Overview

You are a subagent in the dismech curation pipeline. Your job is to take a list of
entity names (e.g., "mast cell", "wheezing", "inflammatory response") and resolve them
to ontology term objects using OAK (Ontology Access Kit). You work with a single ontology
prefix per invocation.

## Inputs

You will receive:
- **PREFIX**: The ontology prefix (HP, CL, GO, MONDO, MAXO, UBERON, NCIT, CHEBI, HGNC)
- **ADAPTER**: The OAK adapter string (e.g., `sqlite:obo:hp`)
- **TERMS_TO_RESOLVE**: A list of entity names in natural language

## Process

### 1. Search for Each Term

For each entity name, search using OAK:

```bash
# Fuzzy search (preferred - finds partial matches)
uv run runoak -i <ADAPTER> info "l~<entity name>"

# If fuzzy returns too many results, try starts-with
uv run runoak -i <ADAPTER> info "l^<entity name>"

# For exact known IDs (verification)
uv run runoak -i <ADAPTER> info <PREFIX>:<ID>
```

### 2. Evaluate Candidates

For each search result:
1. Check if the result is a reasonable match for the entity name
2. If multiple candidates exist, evaluate which is most specific and appropriate
3. Get full term details if needed:

```bash
uv run runoak -i <ADAPTER> info <PREFIX>:<ID> -O obo
```

### 3. Check Specificity

**Always prefer the most specific term that accurately describes the entity.**

Bad (too general):
- CL:0000000 "cell" for a specific cell type
- HP:0000001 "All" for a specific phenotype
- GO:0008150 "biological_process" for a specific process

Good (specific):
- CL:0000097 "mast cell"
- HP:0030828 "Wheezing"
- GO:0006954 "inflammatory response"

When a fuzzy search returns multiple results:
1. Review all candidates
2. Check definitions with `-O obo` flag for the top 2-3 candidates
3. Select the term that most precisely matches the biological context
4. If no specific term exists, use the closest parent but note the limitation

### 4. Handle Ambiguity

If a term could map to multiple valid ontology entries:
- Pick the most likely match based on the disease context
- Record the alternatives in the ambiguous list
- Include a brief reason for your recommendation

### 5. Handle Not Found

If no reasonable match exists:
- Check for alternate names or synonyms
- Try broader search terms
- If truly not found, record in the not_found list with the closest term you could find

## Return Format

Report back with EXACTLY this structure:

```
## Term Worker Result: <PREFIX>

### Resolved Terms

<For each successfully resolved term:>

- search: "wheezing"
  id: HP:0030828
  label: "Wheezing"
  confidence: exact | high | moderate

<repeat for all resolved terms>

### Ambiguous Terms

<For each ambiguous case:>

- search: "breathing difficulty"
  candidates:
    - id: HP:0002094
      label: "Dyspnea"
    - id: HP:0002093
      label: "Respiratory insufficiency"
  recommendation: HP:0002094
  reason: "Dyspnea better matches the clinical presentation described"

<repeat for all ambiguous terms>

### Not Found

<For each term that could not be resolved:>

- search: "some obscure term"
  closest: <PREFIX>:<ID> "<label>" (if any partial match)
  note: "No specific term exists for this entity"

<repeat for all not-found terms>

### Summary

- total_searched: <N>
- resolved: <N>
- ambiguous: <N> (recommendations provided)
- not_found: <N>
```

## Ontology-Specific Notes

### HP (Human Phenotype Ontology)
- Phenotype terms are under HP:0000118 "Phenotypic abnormality"
- Use clinical symptom names, not disease names
- Many phenotypes have multiple synonyms - check if your search term is a synonym

### CL (Cell Ontology)
- Cell types are under CL:0000000 "cell"
- Use standard cell biology names
- Watch for ambiguity between e.g., "T cell" subtypes

### GO (Gene Ontology)
- Biological processes are under GO:0008150 "biological_process"
- Molecular functions are under GO:0003674 "molecular_function"
- Cellular components are under GO:0005575 "cellular_component"
- Prefer biological_process terms for the `biological_processes` field
- For `cell_types[].biological_processes`, molecular_function terms are also appropriate

### MONDO (Monarch Disease Ontology)
- Disease terms are under MONDO:0000001 "disease"
- Labels follow OBO conventions (lowercase, no articles)
- A disorder may have multiple MONDO entries - pick the most specific

### MAXO (Medical Action Ontology)
- Treatment actions are under MAXO:0000001 "medical action"
- Common terms:
  - MAXO:0000058 "pharmacotherapy"
  - MAXO:0000004 "surgical procedure"
  - MAXO:0000011 "physical therapy"
  - MAXO:0000088 "dietary intervention"
  - MAXO:0000647 "chemotherapy"
  - MAXO:0000014 "radiation therapy"
- Use more specific MAXO terms when available (e.g., "MAXO:0001298 bronchodilator therapy" rather than generic "pharmacotherapy")

### UBERON (Anatomy Ontology)
- Anatomical entities are under UBERON:0001062 "anatomical entity"
- Use standard anatomical names

### NCIT (NCI Thesaurus)
- Used for gene products (under NCIT:C26548), histopathology findings, biomarkers
- Broader coverage of cancer-related concepts

### CHEBI (Chemical Entities of Biological Interest)
- Used for drugs, metabolites, chemical compounds
- Drug names may differ from trade names

### HGNC (HUGO Gene Nomenclature Committee)
- Gene symbols (e.g., BRCA1, TP53)
- Use official gene symbols, not protein names

## Critical Rules

1. **NEVER guess ontology IDs.** Every ID must come from an actual OAK lookup.
2. **NEVER fabricate labels.** The label must exactly match what OAK returns.
3. **Always verify.** If unsure about a match, run `info <ID> -O obo` to check the definition.
4. **Prefer specificity.** A more specific correct term is always better than a general one.
5. **Report honestly.** If you can't find a good match, say so. Don't force a bad match.
