---
name: dismech-terms
description: >
  Skill for adding and validating ontology term references in the dismech knowledge base.
  This skill should be used when working with disorder YAML files that need ontology term
  annotations (HPO for phenotypes, CL for cell types, GO for biological processes, MONDO
  for diseases, UBERON for anatomical entities). Use this skill when adding phenotype_term,
  cell_types term, biological_processes term, or other ontology-bound fields to disorder files.
---

# Dismech Ontology Terms Skill

## Overview

Add and validate ontology term references in the dismech disorder knowledge base. This ensures
phenotypes, cell types, biological processes, and other entities are properly linked to
authoritative ontology terms with correct IDs and labels.

## When to Use

- Adding `phenotype_term` to phenotype entries (uses HP - Human Phenotype Ontology)
- Adding `term` to `cell_types` entries (uses CL - Cell Ontology)
- Adding `term` to `biological_processes` entries (uses GO - Gene Ontology)
- Adding `disease_term` to disease entries (uses MONDO)
- Validating existing ontology term references
- Fixing label mismatches between preferred_term and ontology labels

## Term Object Structure

All term references follow this YAML structure:

```yaml
# For phenotypes:
phenotype_term:
  preferred_term: <Human readable name>
  term:
    id: HP:XXXXXXX
    label: <Exact HP label from ontology>

# For cell types:
cell_types:
- preferred_term: <Human readable name>
  term:
    id: CL:XXXXXXX
    label: <Exact CL label from ontology>

# For biological processes:
biological_processes:
- preferred_term: <Human readable name>
  term:
    id: GO:XXXXXXX
    label: <Exact GO label from ontology>
```

## Ontology Lookup with OAK

Use the Ontology Access Kit (OAK) to look up terms:

### Exact Match
```bash
uv run runoak -i sqlite:obo:hp info "seizure"
# Returns: HP:0001250 ! Seizure
```

### Fuzzy Search
```bash
uv run runoak -i sqlite:obo:hp info "l~cognitive impairment"
# Returns multiple matches - select the most appropriate
```

### Get Full Term Details
```bash
uv run runoak -i sqlite:obo:cl info CL:0000540 -O obo
# Returns complete term information including definition
```

### Common Ontology Prefixes
| Ontology | Prefix | Adapter | Use For |
|----------|--------|---------|---------|
| Human Phenotype | HP | sqlite:obo:hp | phenotype_term |
| Cell Ontology | CL | sqlite:obo:cl | cell_types |
| Gene Ontology | GO | sqlite:obo:go | biological_processes |
| MONDO Disease | MONDO | sqlite:obo:mondo | disease_term |
| Uberon Anatomy | UBERON | sqlite:obo:uberon | anatomical locations |

## Specificity Guidelines

**Critical**: Always use the most specific term that accurately describes the entity:

| Incorrect (too general) | Correct (specific) |
|------------------------|-------------------|
| CL:0000066 epithelial cell | CL:0002202 epithelial cell of tracheobronchial tree |
| HP:0000001 All | HP:0001250 Seizure |
| CL:0000000 cell | CL:0000540 neuron |

When a fuzzy search returns multiple results:
1. Review all candidates
2. Check term definitions with `-O obo` flag
3. Select the term that most precisely matches the biological context
4. If no specific term exists, use the closest parent but note the limitation

## Validation

After adding terms, validate with:

```bash
just validate-terms
```

This checks:
- Term IDs exist in the ontology
- Labels match the canonical ontology labels exactly
- Required fields are present

### Fixing Label Mismatches

If validation reports a label mismatch:
```
LABEL MISMATCH: Cholera.yaml
  Term: HP:0003394
  Expected: Muscle cramps
  Actual: Muscle spasm
```

Update the `label` field to match the ontology's canonical label exactly.

## Batch Processing

To find entries missing term annotations:

```python
import yaml
import glob

for f in glob.glob("kb/disorders/*.yaml"):
    with open(f) as file:
        data = yaml.safe_load(file)
    for pheno in data.get('phenotypes', []):
        if 'phenotype_term' not in pheno:
            print(f"{f}: {pheno.get('name')} - missing phenotype_term")
```

## Common Patterns

### Adding HPO to a Phenotype
1. Look up term: `uv run runoak -i sqlite:obo:hp info "l~<phenotype name>"`
2. Verify specificity: `uv run runoak -i sqlite:obo:hp info <HP:ID> -O obo`
3. Add to YAML:
   ```yaml
   phenotype_term:
     preferred_term: <Original Name>
     term:
       id: <HP:ID>
       label: <Exact label from OAK>
   ```
4. Validate: `just validate-terms`

### Descriptor Qualifiers for Common Clinical Modifiers

When a base ontology term needs common clinical qualification, prefer the explicit
descriptor slots instead of the deprecated generic `qualifiers` list:

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

phenotype_term:
  preferred_term: Meningitis
  term:
    id: HP:0001287
    label: Meningitis
  severity: SEVERE
  onset:
    onset_category: NEONATAL
```

Enum values with ontology `meaning` mappings:
- `temporality`: `ACUTE` = `HP:0011009`, `TRANSIENT` = `HP:0025153`,
  `SUBACUTE` = `HP:0011011`, `CHRONIC` = `HP:0011010`, `RECURRENT` = `HP:0031796`,
  `DIURNAL` = `HP:0025302`, `NOCTURNAL` = `HP:0025301`, `PROLONGED` = `HP:0025297`
- `clinical_course`: `PROGRESSIVE` = `HP:0003676`, `STABLE` = `HP:0031915`
- `severity`: `MILD` = `HP:0012825`, `MODERATE` = `HP:0012826`, `SEVERE` = `HP:0012828`

Prefer a precoordinated ontology term when one already exists; otherwise add the
qualifier in these dedicated slots.

### Adding CL to Cell Types
1. Look up term: `uv run runoak -i sqlite:obo:cl info "l~<cell type>"`
2. Verify specificity
3. Add `term:` block under the cell_type entry
4. Validate
