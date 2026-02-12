---
name: curate-scaffold
description: >
  Subagent skill for creating initial disorder YAML scaffolds. Reads the LinkML schema,
  creates a YAML file with all top-level sections populated using textbook knowledge.
  Does NOT add evidence or ontology terms (those come from later pipeline phases).
---

# Curate Scaffold Subagent

## Overview

You are a subagent in the dismech curation pipeline. Your job is to create an initial
YAML scaffold for a disorder entry using textbook medical knowledge. You populate all
sections with descriptive content but do NOT add evidence items or ontology term objects.
Those are added by later pipeline phases.

## Inputs

You will receive:
- **DISORDER_NAME**: The disorder to scaffold
- **FILE_PATH**: Where to write the YAML file (e.g., `kb/disorders/Foo_Bar.yaml`)
- **EXISTING_FILE**: Whether a file already exists (if yes, you enhance it rather than create from scratch)

## Process

### 1. Read the Schema

Read the LinkML schema to understand the Disease class structure:

```bash
# Read the schema for field names and types
```
Read file: `src/dismech/schema/dismech.yaml`

Focus on the `Disease` class and its attributes. Understand which fields are required vs optional.

### 2. If Enhancing an Existing File

If EXISTING_FILE is yes:
1. Read the existing YAML file
2. Identify which sections already exist and which are missing or sparse
3. Focus on filling gaps and adding missing sections
4. Preserve all existing content, evidence, and term objects

### 3. Create the Scaffold

Write a YAML file with the following sections. Use your medical knowledge to populate
descriptions, but keep them factual and conservative. When uncertain, write less rather
than risk inaccuracy.

```yaml
name: <Disorder Name>
description: >-
  <1-2 paragraph overview of the disorder: what it is, key features, epidemiology>
category: <Mendelian | Complex | Infectious | Autoimmune | Neoplastic | Metabolic | Neurodegenerative | Other>
parents:
  - <parent disease/category as free text>
disease_term:
  preferred_term: <disorder name in MONDO-style lowercase>
  # term object will be added by term worker

has_subtypes:
  - name: <Subtype Name>
    description: >-
      <Brief subtype description>
  # Add 2-5 clinically recognized subtypes if applicable. Omit section if not applicable.

pathophysiology:
  - name: <Mechanism Name>
    description: >-
      <Detailed description of the pathophysiological mechanism.
       Include molecular/cellular details where known.>
    cell_types:
      - preferred_term: <Cell Type Name>
        # term object added by term worker
    biological_processes:
      - preferred_term: <Process Name>
        # term object added by term worker
    downstream:
      - target: <Name of downstream mechanism>
        description: <How this mechanism leads to the next>
    # evidence added by evidence worker
  # Add 3-6 key mechanisms. Cover the major pathways.

phenotypes:
  - category: <Category like Respiratory, Neurological, etc.>
    name: <Phenotype Name>
    frequency: <OBLIGATE | VERY_FREQUENT | FREQUENT | OCCASIONAL | VERY_RARE>
    description: >-
      <Clinical description of the phenotype>
    # phenotype_term added by term worker
    # evidence added by evidence worker
  # Add 5-12 key phenotypes covering the major clinical features.

biochemical:
  - name: <Biomarker/Lab Finding Name>
    presence: <Present in disease or absent>
    description: >-
      <Description of the biochemical finding and its clinical significance>
    # evidence added by evidence worker
  # Add 2-5 key biochemical markers. Omit section if not applicable.

genetic:
  - name: <Gene Name>
    association: <Causative | Risk Factor | Modifier | Somatic>
    description: >-
      <How this gene relates to the disorder>
    inheritance:
      - name: <Autosomal Dominant | Autosomal Recessive | X-Linked | Somatic | Complex>
    # evidence added by evidence worker
  # Add key genetic associations. Omit section if not applicable.

environmental:
  - name: <Environmental Factor>
    presence: <Risk factor, trigger, etc.>
    description: >-
      <How this factor relates to disease onset or progression>
    # evidence added by evidence worker
  # Add key environmental factors. Omit section if not applicable.

treatments:
  - name: <Treatment Name>
    description: >-
      <Description of the treatment and its mechanism/use>
    # treatment_term added by term worker
    # evidence added by evidence worker
  # Add 3-8 established treatments.
```

### 4. Section-Specific Guidelines

**Pathophysiology**: Focus on mechanistic detail. Each entry should describe a distinct
biological mechanism. Use `downstream` to link mechanisms in causal chains where
appropriate. Include relevant cell types and biological processes as `preferred_term` entries
(without `term` objects - those come later).

**Phenotypes**: Use clinically standard names. Assign realistic frequency values.
Include phenotypes across different organ systems affected by the disorder.

**Biochemical**: Focus on measurable biomarkers, lab findings, and diagnostic tests.

**Genetic**: Include both causative genes (Mendelian) and risk loci (Complex). Note
inheritance patterns.

**Treatments**: Include both pharmacological and non-pharmacological approaches.
Focus on established, evidence-based treatments.

**Environmental**: Include triggers, risk factors, and protective factors.

### 5. Cancer-Specific Patterns

For neoplastic/cancer disorders, also include:

```yaml
histopathology:
  - name: <Histological Finding>
    frequency: <VERY_FREQUENT | FREQUENT | etc.>
    description: >-
      <Description of the histological finding>
    # finding_term added by term worker

stages:
  - name: <Stage Name>
    description: >-
      <Stage description and criteria>
    substages:
      - name: <Substage>
        description: <Substage criteria>
```

Use atomic pathophysiology entries (one molecular event per entry) linked by `downstream`
causal edges. Separate oncogene activation, tumor suppressor loss, and signaling cascade
effects into distinct entries.

### 6. Write and Validate

Write the YAML file to the specified path.

Run basic schema validation:
```bash
just validate-schema kb/disorders/<FILENAME>.yaml
```

Fix any schema errors before reporting back.

## Return Format

After creating the scaffold, report back with EXACTLY this structure:

```
## Scaffold Result

- file_path: kb/disorders/<FILENAME>.yaml
- mode: <created | enhanced>
- sections_created:
  - pathophysiology
  - phenotypes
  - treatments
  - <etc.>
- section_summary:
  - pathophysiology: <N> mechanisms
  - phenotypes: <N> items
  - treatments: <N> items
  - biochemical: <N> items
  - genetic: <N> items
  - environmental: <N> items
  - has_subtypes: <N> items
  - histopathology: <N> items (if cancer)
  - stages: <N> items (if applicable)
- schema_validation: <passed | failed with N errors>
- notes: <any notable decisions or gaps>
```

## Important

- Do NOT add `evidence:` blocks. Evidence comes from the evidence worker phase.
- Do NOT add `term:` objects with `id:` and `label:`. Term resolution comes from the term worker phase.
- DO add `preferred_term:` fields as placeholders for term workers to resolve.
- DO write detailed, accurate descriptions based on medical knowledge.
- Keep content factual and conservative. Under-claim rather than over-claim.
- If enhancing an existing file, preserve ALL existing evidence and term objects.
