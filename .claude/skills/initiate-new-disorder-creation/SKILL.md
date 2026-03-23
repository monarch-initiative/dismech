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

### Step 2a: Setup git worktree

The preferred mode of working is to use git worktrees, unless the user has expressed
a preference not to do this in advance.

### Step 2b: Create initial YAML file

Create an initial yaml file using the underscore form of the disease, e.g.

kb/disorders/Foo_Bar.yaml:
```yaml
name: Foo Bar
creation_date: "2025-06-12T20:16:27Z"
updated_date: "2025-06-12T20:16:27Z"
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

`creation_date` and `updated_date` must be ISO 8601/RFC 3339 datetime strings.
When editing an existing file, preserve `creation_date` and bump `updated_date`.

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

The `just fetch-reference` command can accept multiple identifiers of different types, such as:

- `just fetch-reference PMID:nnnnnnn DOI:nn.nnnn`

You can also find additional references relevant to individual assertions, on top of what is in the deep research.

Then use this to provide snippets/excerpts and explanations for assertions. For example, for a phenotype assertion:

```
phenotypes:
- name: <Phenotype Name>
  description: <Description from research>
  evidence:
  - reference: PMID:XXXXXXXX
    supports: <SUPPORT | REFUTE | PARTIAL>
    evidence_source: <HUMAN_CLINICAL | MODEL_ORGANISM | IN_VITRO | COMPUTATIONAL>
    snippet: "<Exact quote from abstract>"
    explanation: "<Why this supports the phenotype>"
```

**IMPORTANT**: The `evidence_source` field classifies **the type of evidence in the cited publication** (human study, animal model, cell culture, computational simulation), NOT whether the curation was performed by an AI agent. Always classify based on what the paper reports, regardless of who or what is doing the curation.

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


### Step 6: Validation

Strict validation check (adherence to schema, term and reference checks):

```bash
just validate kb/disorders/<Disease_Name>.yaml
```

Compliance report (completeness, term and evidence coverage):

```bash
just compliance kb/disorders/<Disease_Name>.yaml
```

### Step 7: Review

Use the `dismech-pr-review/` to do an initial round of review. Use a subagent for fresh context
(note that we haven't made the PR yet, but we want to do our own "red team" before making the actual PR

### Step 8: Make a PR

IF THE USER asks, then go ahead and make a PR on behalf of the user

### Step 9: Check reviews on the PR

Some time (~5 mins) after making the PR, a review will appear. You should prioritize in order:

1. reviews from a human/curator -- always take precedence
2. reviews from claude -- high quality but sometimes focuses on wrong thing
3. copilot -- useful for targeted line-level edits but in general lower quality

Follow these priorities but use judgment. If something doesn't sit right, ask for clarification on the PR.
Be proactive. If the review says "moderate" go ahead and fix it as you are fixing things anyway.
Ignore things that seem super-minor but if there is no cost in making a fix and you agree, do it.

Once you have made the changes:

1. **Stage ONLY disorder-relevant files** — never use `git add -A` or `git add .`:
   ```bash
   git add kb/disorders/ references_cache/ research/
   ```
   This prevents committing unrelated generated files (HTML, schema docs, cache CSVs) that cause merge conflicts.

2. **Commit and push**:
   ```bash
   git commit --no-verify -m "feat: Add <Disease Name> (<gene>) with deep research and validated evidence"
   git push
   ```

3. **Post a PR comment** summarizing what you did:
   - What was created/changed
   - Key PMIDs used
   - Validation results
   - Any issues you found but intentionally did NOT fix (with reasoning)





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
4. Set `evidence_source` based on the **publication's evidence type** (human clinical, animal model, in vitro, computational), NOT based on whether an AI agent performed the curation

**NEVER fabricate PMIDs or paraphrase snippets.**

**Evidence Source Classification**: When adding `evidence_source`, ask "What kind of study does this paper report?" not "How was this entry curated?" A computational fluid dynamics study gets `COMPUTATIONAL`, a mouse model study gets `MODEL_ORGANISM`, a human clinical trial gets `HUMAN_CLINICAL` - regardless of whether the curation was done by a human or an AI agent.

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

## Responding to PR Review Comments

When asked to address review comments on an existing PR:

1. **Read the full review carefully** — understand each issue before making changes
2. **Address ALL 🔴 CRITICAL and 🟡 IMPORTANT issues** — don't skip any
3. **For issues you disagree with**, don't silently ignore them. Post a PR comment explaining why:
   - e.g. "The reviewer flagged X as a typo, but this matches the canonical MONDO label (verified with OAK). Filed upstream issue."
4. **After pushing fixes, post a PR comment** with a table summarizing:
   - Each reviewer issue and how you addressed it
   - Any issues you intentionally did NOT fix, with reasoning
   - Validation results after fixes
5. **Use `supports: PARTIAL`** when evidence is indirect — don't overstate evidence strength
6. **If evidence doesn't support a claim, find better evidence** rather than arguing about evidence_source classification
7. **Verify ontology terms with OAK** when the reviewer questions them — don't assume

### Git discipline for review fixes

```bash
# ONLY stage disorder-relevant files
git add kb/disorders/ references_cache/ research/

# NEVER do this — picks up generated files from other disorders
# git add -A
# git add .

git commit --no-verify -m "fix: Address PR review comments"
git push
```

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
