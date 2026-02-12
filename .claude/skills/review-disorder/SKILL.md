---
name: review-disorder
description: >
  Standalone skill for interactive review and Q&A of any disorder YAML file. Presents
  a structured review summary, then enters an interactive loop for human questions,
  change requests, and re-validation. Not tied to the curation pipeline.
---

# Review Disorder Skill

## Overview

You are an interactive reviewer for dismech disorder YAML files. Your job is to present
a structured review of a disorder entry and then help the human explore, question, and
refine it through conversation.

This skill is standalone - it works on any disorder file, whether freshly curated,
manually edited, or pre-existing. It is NOT part of the curation pipeline (that's the
curate skill). Use this skill when:

- Reviewing output from `/curate`
- Revisiting an existing disorder entry
- Preparing a PR review for disorder file changes
- Interrogating evidence quality or identifying gaps

## Inputs

Parse from `$ARGUMENTS`:
- **FILE_PATH**: Path to the disorder YAML file (e.g., `kb/disorders/Asthma.yaml`)

If no path given, ask the user which disorder to review.

## Process

### Step 1: Load and Validate

1. Read the disorder YAML file
2. Dispatch a validation subagent to get current status:

Read the skill file `.claude/skills/curate-validator/SKILL.md`, then dispatch:

```
Task tool with subagent_type="general-purpose":

  <include full content of curate-validator/SKILL.md>

  ## Your Assignment

  Validate the disorder file: <FILE_PATH>

  Run all validation checks and attempt auto-repair for minor reference mismatches.
  Return structured results as described in the skill.
```

3. While waiting for validation, read the YAML file yourself (it's small enough)

### Step 2: Generate Structured Review

Present the review in this format:

```markdown
## Review: [Disorder Name]

**File**: [file path]
**Category**: [category]
**Disease Term**: [MONDO ID and label, or "missing"]
**Compliance**: Global XX% | Weighted XX%

---

### Pathophysiology ([N] mechanisms)

#### 1. [Mechanism Name]
> **Description**: [first 1-2 sentences of description]
> **Cell types**: [list of preferred_terms with term IDs, or "none"]
> **Processes**: [list of preferred_terms with term IDs, or "none"]
> **Downstream**: [list of targets, or "none"]
> **Evidence**: [N items - list each as "PMID:xxx (SUPPORT/PARTIAL/REFUTE)"]
> [icon] [any warnings: missing evidence, missing terms, validation errors]

#### 2. [Next Mechanism]
> ...

---

### Phenotypes ([N] items)

#### 1. [Phenotype Name]
> **Term**: [HP ID and label, or "missing"]
> **Frequency**: [frequency value, or "not set"]
> **Evidence**: [N items]
> [icon] [warnings]

#### 2. ...

---

### Treatments ([N] items)

#### 1. [Treatment Name]
> **Term**: [MAXO ID and label, or "missing"]
> **Evidence**: [N items]
> [icon] [warnings]

---

### Biochemical ([N] items)
[Same pattern - name, key fields, evidence count, warnings]

### Genetic ([N] items)
[Same pattern]

### Environmental ([N] items)
[Same pattern]

---

### Validation Summary
- Schema: [passed/failed with N errors]
- Terms: [N errors - list briefly]
- References: [N errors - list briefly]
- Auto-repairs: [N applied]

### Gaps and Recommendations
- [List items missing evidence]
- [List items missing ontology terms]
- [List sections that are empty or sparse]
- [Suggest specific improvements]
```

**Formatting rules:**
- Keep it scannable. Use the structured format above, not prose paragraphs.
- For each item, show the most important fields inline. Don't dump raw YAML.
- Flag problems visually (use "WARNING:" prefix for issues needing attention).
- If a section is empty, say "[Section] is empty" and suggest what to add.

### Step 3: Interactive Loop

After presenting the review, say:

```
What would you like to explore or change? You can:
- Ask about evidence ("Why this PMID for airway remodeling?")
- Request changes ("Remove the second phenotype", "Add nocturnal cough")
- Drill into terms ("Find a more specific CL term for this")
- Re-validate ("Run validation again")
- Compare with research ("What did deep research say about this?")
```

Then respond to the human's questions and requests.

### Handling Interactive Requests

**Evidence questions** ("Why this PMID?", "Is there stronger evidence?"):
- Read the specific cached reference: `references_cache/pmid_<NUMBER>.md`
- Show the relevant abstract excerpt
- Explain why it was chosen (from the `explanation` field)
- If asked for alternatives, suggest searching PubMed (do not fabricate PMIDs)

**Change requests** ("Remove X", "Add Y", "Change Z"):
- Read the current YAML file
- Make the requested edit using the Edit tool
- After editing, run quick validation:
  ```bash
  just validate-schema kb/disorders/<FILENAME>.yaml
  ```
- Report what changed

**Term questions** ("Why HP:xxx?", "Find a more specific term"):
- Run OAK lookup to show alternatives:
  ```bash
  uv run runoak -i sqlite:obo:<ontology> info "l~<search term>"
  ```
- Show candidates with definitions
- If the human picks a new term, update the YAML

**Re-validation** ("Run validation again", "Check compliance"):
- Dispatch a new validation subagent (same as Step 1)
- Present updated results

**Research comparison** ("What did deep research say?"):
- Check for research files: `research/<DISORDER_FILE>-deep-research-*.md`
- If found, read the relevant section (do NOT load the entire file - search for the
  specific topic the human asked about using Grep)
- Summarize what the research says vs. what's in the YAML

**Adding new evidence**:
- Fetch the reference: `just fetch-reference PMID:xxx`
- Read the cached abstract
- Find an exact snippet supporting the claim
- Add the evidence block to the YAML
- Run reference validation on the file

## Context Efficiency

This skill is designed to be lightweight:
- The YAML file is small (typically < 300 lines) - reading it is fine
- Validation runs in a subagent (results returned as compact summary)
- References are only fetched on demand (when the human asks)
- Research files are only searched on demand (never loaded fully)
- OAK lookups only run when the human asks about terms

This leaves maximum context room for extended back-and-forth conversation.

## Critical Rules

1. **Read the YAML file.** Don't guess about its contents.
2. **Use the structured review format.** Don't present raw YAML dumps.
3. **Validate via subagent.** Don't run validation commands in the main context unless it's a quick schema check after an edit.
4. **Fetch on demand only.** Don't preload abstracts, research files, or OAK results.
5. **Edit carefully.** When making changes, use the Edit tool for precision. Don't rewrite the entire file.
6. **Anti-hallucination.** When adding evidence, the snippet MUST be a verbatim quote from the cached abstract. Never fabricate.
