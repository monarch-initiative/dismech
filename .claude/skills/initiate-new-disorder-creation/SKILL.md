---
name: initiate-new-disorder-creation
description: >
  Skill for initiating new disorder YAML files in the dismech knowledge base.
  Use this skill when the user asks to create a new disorder entry. CRITICAL:
  Before creating any new disorder file, at least one deep research query must
  be performed using tools like falcon, cyberian, perplexity, or openai to gather
  accurate pathophysiology information and prevent hallucination.
---

# Initiate New Disorder Creation Skill

## Overview

Guide the creation of new disorder YAML files in the dismech knowledge base. This skill
emphasizes a **research-first approach** to ensure scientific accuracy and prevent
AI hallucinations by requiring deep research queries before file creation.

## When to Use

- User asks to create a new disorder/disease entry
- User wants to add a condition to the knowledge base
- User names a disorder that doesn't exist in `kb/disorders/`

## CRITICAL: Research-First Requirement

**NEVER create a new disorder file without first performing at least one deep research query.**

### Why Research First?

1. **Prevents hallucination** of pathophysiology mechanisms
2. **Ensures evidence-backed content** with real PMIDs
3. **Captures accurate disease terminology** (MONDO terms, phenotypes)
4. **Identifies correct cell types and biological processes**

### Deep Research Tools

Use at least ONE of these tools before creating any disorder file:

| Tool | Best For | How to Use |
|------|----------|------------|
| **Falcon** | Comprehensive disease research | MCP tool: query disease pathophysiology |
| **Cyberian** | Literature-focused research | MCP tool: search biomedical literature |
| **Perplexity** | General research with citations | MCP tool or web search with citations |
| **OpenAI** | Deep research mode | MCP tool: structured research query |

### Recommended Research Queries

Structure your research query to gather:

```
"Provide a comprehensive overview of [DISEASE NAME] pathophysiology including:
1. Primary disease mechanisms
2. Key cell types involved
3. Biological processes affected
4. Associated phenotypes/symptoms
5. Known genetic factors
6. Standard treatments
7. Relevant PMID references from PubMed"
```

## Workflow

### Step 1: Verify Disorder Doesn't Exist

```bash
ls kb/disorders/ | grep -i "<disease_name>"
```

If it exists, edit the existing file instead of creating a new one.

### Step 2: Perform Deep Research (REQUIRED)

Execute at least one deep research query. Document what tool was used:

```
[RESEARCH LOG]
Tool: <falcon/cyberian/perplexity/openai>
Query: "<your research query>"
Key findings:
- Pathophysiology mechanisms: ...
- Cell types: ...
- Phenotypes: ...
- PMIDs gathered: ...
```

### Step 3: Look Up Ontology Terms

Before creating the file, look up required ontology terms using OAK:

```bash
# Disease term (MONDO)
uv run runoak -i sqlite:obo:mondo info "l~<disease name>"

# Phenotype terms (HPO)
uv run runoak -i sqlite:obo:hp info "l~<phenotype>"

# Cell types (CL)
uv run runoak -i sqlite:obo:cl info "l~<cell type>"

# Biological processes (GO)
uv run runoak -i sqlite:obo:go info "l~<process>"

# Treatment terms (MAXO)
uv run runoak -i sqlite:obo:maxo search "<treatment>"
```

### Step 4: Create the File

Create `kb/disorders/<Disease_Name>.yaml` with this template:

```yaml
name: <Disease Name>
category: <Mendelian|Complex|Infectious|Other>
parents:
- <Parent Category>

disease_term:
  preferred_term: <Disease Name>
  term:
    id: MONDO:XXXXXXX
    label: <exact MONDO label>

description: >
  <Brief disease description from research>

phenotypes:
- name: <Phenotype Name>
  description: <Description from research>
  frequency: <Common|Variable|Rare>
  phenotype_term:
    preferred_term: <Phenotype Name>
    term:
      id: HP:XXXXXXX
      label: <exact HPO label>
  evidence:
  - reference: PMID:XXXXXXXX
    supports: SUPPORT
    snippet: "<Exact quote from abstract>"
    explanation: "<Why this supports the phenotype>"

pathophysiology:
- name: <Mechanism Name>
  description: >
    <Detailed mechanism description from research>
  cell_types:
  - preferred_term: <Cell Type>
    term:
      id: CL:XXXXXXX
      label: <exact CL label>
  biological_processes:
  - preferred_term: <Process Name>
    term:
      id: GO:XXXXXXX
      label: <exact GO label>
  evidence:
  - reference: PMID:XXXXXXXX
    supports: SUPPORT
    snippet: "<Exact quote from abstract>"
    explanation: "<Why this supports the mechanism>"

treatments:
- name: <Treatment Name>
  description: <Treatment description>
  treatment_term:
    preferred_term: <Treatment>
    term:
      id: MAXO:XXXXXXX
      label: <exact MAXO label>
```

### Step 5: Validate the New File

```bash
# Schema validation
just validate kb/disorders/<Disease_Name>.yaml

# Term validation (ontology IDs/labels)
just validate-terms-file kb/disorders/<Disease_Name>.yaml

# Reference validation (snippets match PMIDs)
just validate-references kb/disorders/<Disease_Name>.yaml

# Full QC
just qc
```

### Step 6: Generate HTML Page

```bash
uv run python -m dismech.render kb/disorders/<Disease_Name>.yaml
```

## File Naming Convention

Convert the disease name to a file-safe format:
- Replace spaces with underscores
- Remove special characters
- Use title case

Examples:
- "Type 2 Diabetes" → `Type_2_Diabetes.yaml`
- "Alzheimer's Disease" → `Alzheimers_Disease.yaml`
- "COVID-19" → `COVID-19.yaml`

## Minimum Required Fields

A new disorder file MUST include at minimum:

| Field | Source | Notes |
|-------|--------|-------|
| `name` | - | Human-readable disease name |
| `category` | Research | Mendelian, Complex, Infectious, etc. |
| `disease_term` | OAK lookup | MONDO term binding |
| `phenotypes` (1+) | Research | At least one phenotype with HPO term |
| `pathophysiology` (1+) | Research | At least one mechanism |
| `evidence` (1+) | Research | At least one PMID reference |

## Evidence Requirements

All evidence items MUST:
1. Use real PMIDs from the research query results
2. Have snippets that are exact quotes from abstracts
3. Include explanations linking evidence to claims

**NEVER fabricate PMIDs or paraphrase snippets.**

## Validation Errors and Fixes

### "Term not found in ontology"
- Re-run OAK lookup with fuzzy search: `info "l~<term>"`
- Use the exact label from the ontology

### "Snippet not found in reference"
- The quoted text must be from the PMID's abstract
- Fetch and verify: `just validate-references <file>`
- Use `--fix-threshold 0.80` to auto-repair minor mismatches

### "Required field missing"
- Check the schema for required fields
- Ensure `name`, `category`, and at least one `pathophysiology` entry

## Integration with Other Skills

After creating the disorder file:
- Use **dismech-terms** to add additional ontology term bindings
- Use **dismech-references** to validate/repair evidence items
- Use **dismech-compliance** to check completeness and identify gaps

## Anti-Hallucination Checklist

Before finalizing a new disorder file, verify:

- [ ] Deep research query was performed (document which tool)
- [ ] All PMIDs exist and are for relevant papers
- [ ] All snippets are exact quotes from abstracts
- [ ] MONDO term exists and label matches exactly
- [ ] HPO terms exist and labels match exactly
- [ ] CL terms exist and labels match exactly
- [ ] GO terms exist and labels match exactly
- [ ] MAXO terms (if used) exist and labels match exactly
- [ ] `just validate` passes
- [ ] `just validate-terms-file` passes
- [ ] `just validate-references` passes
