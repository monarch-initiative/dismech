---
name: initiate-new-disorder-creation
description: >
  Skill for initiating new disorder YAML files in the dismech knowledge base.
  Use this skill when the user asks to create a new disorder entry. Also useful
  for enhancing existing entries.
---

# Initiate New Disorder Creation Skill

## Overview

Guide the creation of new disorder YAML files in the dismech knowledge base. This skill
emphasizes a **research-first approach** to ensure scientific accuracy and prevent
AI hallucinations by requiring deep research queries before file creation.

## When to Use

- User asks to create a new disorder/disease entry
- User names a disorder that doesn't exist in `kb/disorders/`

This skill can also be consulted for ongoing curation of existing disorders.

## Workflow

### Step 1: Select Disorder Name and Verify Disorder Doesn't Exist

Choose the clinically preferred name for the disorder, use title case (e.g. `Foo Bar Syndrome`).
For file names, spaces will. be replaced by underscores, and characters such as apostrophes removed.

```bash
ls kb/disorders/*yaml
```
If it exists, edit the existing file instead of creating a new one.

### Step 2: Create initial YAML file

Create an initial yaml file using the underscore form of the disease, e.g.

kb/disorders/Foo_Bar.yaml:
```yaml
name: Foo Bar
category: Complex
disease_term:
  term:
    id: MONDO:nnnnnnn
    label: foo bar  ## mondo name will follow OBO case conventions
parents:
  <yaml list of strings>
has_subtypes:
  <optional yaml list of Subtype objects>
pathophysiology:
  <yaml list of Pathophysiology objects>
phenotypes:
  <yaml list of Phenotype objects>
biochemical:
  <optional yaml list of Biochemical objects>
genetic:
  <optional yaml list of Genetic objects>
environmental:
  <optional yaml list of Environmental objects>
treatments:
  <optional yaml list of Treatment objects>
datasets:
```

The objects must follow the LinkML schema in src/dismech/schema.

It can be validated with `just validate kb/disorders/Foo_Bar.yaml`

This first pass should use textbook knowledge about the disease: you will later refine this.

### Step 3: Perform Deep Research (REQUIRED)

Execute at least one deep research query. Always do this via the `just` command, do
not perform your own deep research.

Depending on user preference, use one or more of the following commands

- `just research-disorder perplexity DISORDER_NAME`
- `just research-disorder falcon DISORDER_NAME`
- `just research-disorder openai DISORDER_NAME`
- `just research-disorder cyberian DISORDER_NAME`

Use the filesystem-friendly name here.

On completion (may be several minutes, be patient), this will create a file here:

`./research/DISORDER_NAME.md`

You MUST read this before progressing.

### Step 4: Enhance YAML file with evidence for assestions

Use the results of deep research to enhance the yaml file, providing evidence for as many assertions as possible.

Find the pubmed IDs or DOIs for the papers in the deep research and retrieve these:

- `just fetch-reference PMID:nnnnnnn`
- `just fetch-reference DOI:...`

You can also find additional references relevant to individual assertions, on top of what is in the deep research.

Then use this to provide snippets/excerpts and explanations for assertions. For example, for a phenotype assertion:

```
phenotypes:
- name: <Phenotype Name>
  description: <Description from research>
  evidence:
  - reference: PMID:XXXXXXXX
    supports: <SUPPORT | REFUTE | PARTIAL>
    snippet: "<Exact quote from abstract>"
    explanation: "<Why this supports the phenotype>"
```

The same generic `evidence` list schema is used for most types.

### Step 5: Add term objects

Add term objects using ontology term IDs; for example, for a `pathophsyiology` object, it might look like this:

```
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
```      

Consult the LinkML schema to see what terms are appropriate for any given object type. These will be validated.

You can use OAK commands to find relevant terms.

General term search (use mondo for diseases)

```bash
uv run runoak -i sqlite:obo:mondo info "l~<disease name>"
```

starts-with queries (use hp for phenotypes)

```bash
uv run runoak -i sqlite:obo:hp info "l^<phenotype>"
```

exact:

```
uv run runoak -i sqlite:obo:cl info CL:nnnnnnn
```

relationships (up and down):

```
uv run runoak -i sqlite:obo:go relationships --direction both GO:nnnnnnn
```


### Step 6: Final review and validation

Strict validation check (adherence to schema, term and reference checks):

```bash
just validate kb/disorders/<Disease_Name>.yaml
```

Compliance report (completeness, term and evidence coverage):

```bash
just compliance kb/disorders/<Disease_Name>.yaml
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

Use all loaded skills, including:

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
