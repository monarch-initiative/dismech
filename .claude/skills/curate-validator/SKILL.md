---
name: curate-validator
description: >
  Subagent skill for running the full validation suite on a disorder YAML file.
  Runs schema validation, term validation, reference validation, and compliance checks.
  Attempts auto-repair for minor reference mismatches.
---

# Curate Validator Subagent

## Overview

You are a subagent in the dismech curation pipeline. Your job is to run all validation
checks on a disorder YAML file and return a structured report of results. You also
attempt auto-repair for minor reference snippet mismatches.

## Inputs

You will receive:
- **YAML_FILE**: Path to the disorder YAML file (e.g., `kb/disorders/Asthma.yaml`)

## Process

### 1. Schema Validation

Run schema validation to check structural conformance:

```bash
just validate-schema kb/disorders/<FILENAME>.yaml
```

This checks:
- Required fields are present
- Field types are correct
- Enum values are valid
- Nested object structure is correct

Capture all errors. Schema errors are the most critical - they mean the file won't load.

### 2. Term Validation

Run ontology term validation:

```bash
just validate-terms-file kb/disorders/<FILENAME>.yaml
```

This checks:
- Term IDs exist in the referenced ontology
- Labels match the canonical ontology labels exactly
- Terms are within the expected ontology namespace

Capture all term errors. Common issues:
- Label mismatch (wrong case, outdated label)
- ID not found (typo or obsolete term)
- Wrong namespace (e.g., GO ID used where HP expected)

### 3. Reference Validation

Run reference/evidence validation:

```bash
just validate-references kb/disorders/<FILENAME>.yaml
```

This checks:
- PMIDs exist and are fetchable
- Snippet text appears as a substring of the cited abstract
- Reference format is correct (PMID:\d+, DOI:..., clinicaltrials:NCT\d+)

Capture all reference errors.

### 4. Auto-Repair Reference Mismatches

For files with reference errors, attempt auto-repair:

```bash
uv run linkml-reference-validator repair data kb/disorders/<FILENAME>.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease \
  --no-dry-run \
  --fix-threshold 0.80
```

The `--fix-threshold 0.80` means snippets with 80%+ similarity to the actual abstract
will be automatically corrected. This fixes minor typos, whitespace issues, and small
transcription errors.

After repair, re-run reference validation to confirm fixes:

```bash
just validate-references kb/disorders/<FILENAME>.yaml
```

Record what was auto-repaired.

### 5. Compliance Check

Run the compliance analysis:

```bash
just compliance kb/disorders/<FILENAME>.yaml
```

This checks field completeness and coverage. Capture:
- Global compliance percentage
- Weighted compliance percentage
- Missing or incomplete fields

### 6. Compile Results

Gather all results into a structured report.

## Return Format

Report back with EXACTLY this structure:

```
## Validation Result: <FILENAME>

### Schema Validation
- status: passed | failed
- errors:
  <list each error, or "None">

### Term Validation
- status: passed | N errors
- errors:
  <For each error:>
  - term: <PREFIX>:<ID>
    field_path: <where in the YAML>
    issue: "label mismatch" | "term not found" | "wrong namespace"
    expected: "<expected value>"
    actual: "<actual value>"

### Reference Validation
- status: passed | N errors
- errors:
  <For each error:>
  - reference: PMID:<ID>
    field_path: <where in the YAML>
    issue: "snippet not found" | "reference not fetchable" | "format error"
    details: "<additional detail>"

### Auto-Repairs
- attempted: <N>
- successful: <N>
- repairs:
  <For each repair:>
  - reference: PMID:<ID>
    what: "snippet corrected"
    similarity: <0.XX>
    old_snippet: "<first 50 chars>..."
    new_snippet: "<first 50 chars>..."

### Compliance
- global: <XX>%
- weighted: <XX>%
- missing_fields:
  <list of fields with 0% coverage>
- low_coverage_fields:
  <list of fields below threshold>

### Summary
- schema_valid: true | false
- total_term_errors: <N>
- total_reference_errors: <N> (after auto-repair)
- compliance_global: <XX>%
- compliance_weighted: <XX>%
- overall_status: clean | has_issues
- critical_issues: <list any blocking problems>
```

## Error Handling

- If a validation command fails to run (not validation errors, but the command itself fails),
  report the command failure and continue with other checks.
- If auto-repair makes things worse (more errors after repair), revert by noting the issue
  but do NOT re-run repair.
- Always run all 4 validation steps even if earlier ones find errors.

## Critical Rules

1. **Run ALL validation checks.** Do not skip any, even if early checks find errors.
2. **Report everything.** Include all errors, not just the first few.
3. **Auto-repair conservatively.** Only use the 0.80 threshold. Do not lower it.
4. **Do not manually edit the file.** Your job is to validate and report, not fix issues.
   The only exception is auto-repair via the repair command.
5. **Include the full compliance output.** The orchestrator needs these numbers for the summary.
