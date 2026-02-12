---
name: curate
description: >
  Orchestrator skill for curating disorder entries in the dismech knowledge base.
  Dispatches subagents for scaffold creation, research extraction, evidence building,
  term resolution, and validation. Keeps main context lean by delegating heavy work.
---

# Curate Disorder Orchestrator

## Overview

You are the orchestrator for a multi-phase curation pipeline. Your job is to dispatch
subagents that do the heavy lifting (reading research files, fetching references, running
OAK lookups) and assemble their results into a validated disorder YAML file.

**Your context stays lean.** You never read research files, PubMed abstracts, or raw OAK
output directly. Subagents consume that and return compact structured results.

## Inputs

Parse from `$ARGUMENTS`:
- **DISORDER_NAME**: Required. The disorder to curate (e.g., "Asthma", "Marfan Syndrome").
- **RESEARCH_PROVIDER**: Optional. Deep research provider (default: `falcon`). Options: `falcon`, `perplexity`, `openai`, `cyberian`.

## File Naming

Convert disorder name to file-safe format:
- Replace spaces with underscores
- Remove apostrophes
- Keep hyphens and numbers
- Use title case

Examples: "Type 2 Diabetes" -> `Type_2_Diabetes.yaml`, "Alzheimer's Disease" -> `Alzheimers_Disease.yaml`

## Pipeline

### Phase 0: Scaffold Creation (subagent)

Check if the disorder file already exists:
```bash
ls kb/disorders/DISORDER_FILE.yaml
```

Dispatch a scaffold subagent using the Task tool:

1. Read the skill file: `.claude/skills/curate-scaffold/SKILL.md`
2. Dispatch with `subagent_type="general-purpose"`:

```
Task prompt:
  <include full content of curate-scaffold/SKILL.md>

  ## Your Assignment

  Create a scaffold YAML file for: <DISORDER_NAME>
  File path: kb/disorders/<DISORDER_FILE>.yaml
  Existing file: <yes/no, and if yes, the file path>

  When done, report:
  - file_path
  - sections_created (list of section names)
  - section_summary (dict of section name -> item count)
```

Capture the returned summary. Do NOT read the YAML file yourself.

### Phase 1: Deep Research (main agent)

Run the deep research command and wait for it to complete:

```bash
just research-disorder <PROVIDER> <DISORDER_FILE_NAME>
```

This creates `research/<DISORDER_FILE_NAME>-deep-research-<PROVIDER>.md`. It may take several minutes.

Do NOT read the research file. Phase 2 handles that.

### Phase 2: Research Extraction (subagent)

Dispatch a research extraction subagent:

1. Read the skill file: `.claude/skills/curate-research-extraction/SKILL.md`
2. Dispatch with `subagent_type="general-purpose"`:

```
Task prompt:
  <include full content of curate-research-extraction/SKILL.md>

  ## Your Assignment

  Extract structured data from deep research for: <DISORDER_NAME>
  Research file: research/<DISORDER_FILE_NAME>-deep-research-<PROVIDER>.md
  Scaffold YAML: kb/disorders/<DISORDER_FILE>.yaml
  Sections in scaffold: <sections_created from Phase 0>

  Return the structured extraction as described in the skill.
```

Capture the returned structured data:
- `references`: list of {id, relevant_claims}
- `terms_needed`: dict of ontology prefix -> list of entity names
- `enhancements`: list of {section, item, new_content, supporting_refs}
- `new_items`: list of {section, name, description, supporting_refs}

### Phase 3: Evidence + Term Workers (parallel subagents)

This is the most parallel phase. Launch ALL of these in a **single message** with multiple Task tool calls.

#### 3a: Evidence Workers (batched by ~8 PMIDs each)

Split the `references` list into batches of ~8 references each. For each batch:

1. Read the skill file once: `.claude/skills/curate-evidence-worker/SKILL.md`
2. Dispatch with `subagent_type="general-purpose"`:

```
Task prompt:
  <include full content of curate-evidence-worker/SKILL.md>

  ## Your Assignment

  Build evidence blocks for the following references and their claims:

  <list of {id, relevant_claims} for this batch>

  Target disorder: <DISORDER_NAME>
  YAML file: kb/disorders/<DISORDER_FILE>.yaml

  Return evidence_blocks and failures as described in the skill.
```

#### 3b: Term Workers (one per ontology prefix)

For each ontology prefix in `terms_needed` that has entries, dispatch a term worker:

1. Read the skill file once: `.claude/skills/curate-term-worker/SKILL.md`
2. Dispatch with `subagent_type="general-purpose"`:

```
Task prompt:
  <include full content of curate-term-worker/SKILL.md>

  ## Your Assignment

  Resolve ontology terms for prefix: <PREFIX> (e.g., HP, CL, GO, MONDO, MAXO, UBERON)
  Adapter: <adapter from table below>

  Terms to resolve:
  <list of entity names>

  Return terms, ambiguous, and not_found as described in the skill.
```

**Ontology adapters:**
| Prefix | Adapter | Use For |
|--------|---------|---------|
| HP | sqlite:obo:hp | Phenotypes |
| CL | sqlite:obo:cl | Cell types |
| GO | sqlite:obo:go | Biological processes |
| MONDO | sqlite:obo:mondo | Disease terms |
| MAXO | sqlite:obo:maxo | Treatments |
| UBERON | sqlite:obo:uberon | Anatomical entities |
| NCIT | sqlite:obo:ncit | Cancer/gene products/histopathology |
| CHEBI | sqlite:obo:chebi | Chemical entities |
| HGNC | sqlite:obo:hgnc | Gene symbols |

Wait for ALL Phase 3 subagents to complete before proceeding.

### Phase 4: Assembly (main agent)

Now you assemble the final YAML. This is the one phase where you work directly with the file.

1. Read the scaffold YAML file (kb/disorders/<DISORDER_FILE>.yaml)
2. Apply enhancements from Phase 2 (update descriptions, add new content)
3. Add new items from Phase 2 (new phenotypes, mechanisms, etc.)
4. Insert evidence blocks from Phase 3a into their corresponding sections/items
   - Match each evidence block to its section and item by name
   - Skip failures (report them at the end)
5. Insert term objects from Phase 3b into their corresponding entries
   - For ambiguous terms, use the subagent's recommendation
   - For not_found terms, omit the term object (the item keeps its name/description)
6. Write the complete YAML file

**Assembly rules:**
- Match evidence blocks to items by section name + item name
- If an evidence block can't be matched to an item, place it on the most relevant item
- Use the `preferred_term` / `term` structure for all ontology bindings
- For ambiguous terms, use the subagent's recommended term

### Phase 5: Validation (subagent)

Dispatch a validation subagent:

1. Read the skill file: `.claude/skills/curate-validator/SKILL.md`
2. Dispatch with `subagent_type="general-purpose"`:

```
Task prompt:
  <include full content of curate-validator/SKILL.md>

  ## Your Assignment

  Validate the disorder file: kb/disorders/<DISORDER_FILE>.yaml

  Run all validation checks and attempt auto-repair for minor reference mismatches.
  Return structured results as described in the skill.
```

### Completion

After Phase 5, print a brief summary:

```
## Curation Complete: <DISORDER_NAME>

**File**: kb/disorders/<DISORDER_FILE>.yaml
**Sections**: <list sections with item counts>
**Evidence**: <N evidence items added, M failures>
**Terms**: <N terms resolved, M ambiguous (used recommendations), K not found>
**Compliance**: Global XX% | Weighted XX%
**Validation issues**: <count, or "None">

<if there are unresolved issues, list them briefly>

Run `/review-disorder kb/disorders/<DISORDER_FILE>.yaml` to interactively review.
```

Do NOT present the full structured review inline. The review-disorder skill handles that.

## Error Handling

- **Subagent fails entirely**: Report the failure, proceed with available data, note gaps in summary
- **Evidence batch fails**: Other batches continue. Report which references couldn't be processed
- **Term worker fails**: Items are created without term objects. Flag them in summary
- **Validation fails**: Report all issues. Do NOT claim success if validation finds errors
- **Research command fails**: Stop and inform the user. Cannot proceed without research

## Important

- NEVER read research files, PubMed abstracts, or raw OAK output in the main context
- ALWAYS dispatch subagents for heavy operations
- Launch Phase 3 subagents in a SINGLE message (parallel dispatch)
- The pipeline is fire-and-forget: produce the file, print summary, done
- For cancer/neoplastic disorders, the scaffold subagent will apply cancer-specific patterns
