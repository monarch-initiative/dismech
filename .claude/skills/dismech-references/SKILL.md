---
name: dismech-references
description: >
  Skill for validating and repairing evidence references in the dismech knowledge base.
  Use this skill when working with evidence items in disorder YAML files, validating
  that snippet text matches PubMed abstracts, and repairing misquoted or fabricated
  evidence. Critical for ensuring scientific accuracy and preventing AI hallucinations.
---

# DisMech Reference Validation Skill

## Overview

Validate and repair evidence references in the dismech disorder knowledge base. This ensures
that quoted snippets actually appear in the cited sources, preventing fabricated or misquoted
evidence from entering the knowledge base. The tool supports both PubMed references (PMID)
and ClinicalTrials.gov data (NCT identifiers).

## When to Use

- Validating evidence items after adding new disorder content
- Checking that snippets match their cited PMID abstracts
- Repairing evidence items with minor text mismatches
- Removing fabricated evidence (AI hallucinations)
- QC checks before committing changes

## Evidence Item Structure

All evidence items follow this YAML structure:

```yaml
evidence:
  - reference: PMID:12345678  # or clinicaltrials:NCT05813288
    supports: SUPPORT  # SUPPORT, REFUTE, PARTIAL, NO_EVIDENCE, WRONG_STATEMENT
    snippet: "Exact quoted text from the abstract or trial summary"
    explanation: "Why this evidence supports/refutes the claim"
```

### Reference Types

- **PMID**: PubMed references (e.g., `PMID:12345678`) - validated against PubMed abstracts
- **clinicaltrials**: ClinicalTrials.gov references (e.g., `clinicaltrials:NCT05813288`) - validated against ClinicalTrials.gov API via linkml-reference-validator

### Support Classifications

| Value | Meaning |
|-------|---------|
| SUPPORT | Evidence directly supports the statement |
| REFUTE | Evidence contradicts the statement |
| PARTIAL | Evidence partially supports with caveats |
| NO_EVIDENCE | Citation exists but doesn't address the claim |
| WRONG_STATEMENT | The statement itself is incorrect |

## Validation Commands

### Validate a Single File
```bash
uv run linkml-reference-validator validate data kb/disorders/Asthma.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease
```

### Validate All Disorder Files
```bash
just validate-all
```

Or manually:
```bash
for f in kb/disorders/*.yaml; do
  echo "=== $f ==="
  uv run linkml-reference-validator validate data "$f" \
    --schema src/dismech/schema/dismech.yaml \
    --target-class Disease
done
```

### Using the Just Target
```bash
just qc  # Runs all QC including reference validation
```

## Repair Commands

### Dry Run (Preview Changes)
```bash
uv run linkml-reference-validator repair data kb/disorders/Cholera.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease
```

### Auto-Repair with Threshold
```bash
uv run linkml-reference-validator repair data kb/disorders/Cholera.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease \
  --no-dry-run \
  --fix-threshold 0.80
```

The `--fix-threshold 0.80` means snippets with 80%+ similarity to the actual abstract
text will be automatically corrected.

## Fetching Clinical Trial References

Use the `just fetch-reference` command to cache trial data from ClinicalTrials.gov:

```bash
just fetch-reference NCT05813288
```

This will:
1. Fetch the trial data from ClinicalTrials.gov API
2. Cache it as markdown in `references_cache/clinicaltrials_NCT05813288.md`
3. Make the snippet text available for validation

The cached file contains the trial title, status, and summary that you can quote from.

## Common Error Patterns

### 1. Snippet Not Found in Abstract/Trial Data
```
ERROR: Snippet not found in reference PMID:12345678
  Snippet: "The patient showed symptoms..."
  Abstract: [actual abstract text]
```

**Solutions:**
- Check if snippet is from full text (not abstract) - may need to remove
- Check for minor typos - use repair with threshold
- If fabricated, remove the evidence item entirely

### 2. Reference Cannot Be Fetched
```
ERROR: Could not fetch reference PMID:99999999
```

**Solutions:**
- Verify PMID exists on PubMed
- Check for typos in PMID
- If PMID is invalid, remove the evidence item

### 3. Fabricated Evidence Patterns

Watch for these red flags indicating AI-generated fake evidence:
- Snippet says "N/A" or "No abstract available"
- Snippet is suspiciously perfect match to the claim
- PMID doesn't exist or is for unrelated topic
- Generic statements without specific data

**Solution:** Remove the entire evidence item.

## Cache Management

Reference validator caches PubMed abstracts in `.refval_cache/`. If you encounter
stale cache issues:

```bash
rm -rf .refval_cache/
```

### Cache File Format Issues

If you see YAML parsing errors in cache files, check for unquoted colons in titles:
```yaml
# Bad - will cause parse error
title: COVID-19: A New Challenge

# Good - properly quoted
title: "COVID-19: A New Challenge"
```

## Batch Processing Workflow

### 1. Get Error Count
```bash
uv run linkml-reference-validator validate data kb/disorders/*.yaml \
  --schema src/dismech/schema/dismech.yaml \
  --target-class Disease 2>&1 | grep -c "ERROR"
```

### 2. Process Files with Errors
```bash
for f in kb/disorders/*.yaml; do
  errors=$(uv run linkml-reference-validator validate data "$f" \
    --schema src/dismech/schema/dismech.yaml \
    --target-class Disease 2>&1 | grep -c "ERROR" || echo 0)
  if [ "$errors" -gt 0 ]; then
    echo "=== $f has $errors errors ==="
  fi
done
```

### 3. Auto-Repair All
```bash
for f in kb/disorders/*.yaml; do
  uv run linkml-reference-validator repair data "$f" \
    --schema src/dismech/schema/dismech.yaml \
    --target-class Disease \
    --no-dry-run \
    --fix-threshold 0.80
done
```

## Best Practices

### Adding New Evidence

1. **Use real PMIDs**: Always verify the PMID exists on PubMed
2. **Quote exactly**: Copy snippet text directly from the abstract
3. **Keep snippets short**: 1-2 sentences that directly support the claim
4. **Validate immediately**: Run validation after adding evidence

### Reviewing AI-Generated Content

When reviewing disorder files that may contain AI-generated evidence:

1. Run validation first to catch obvious fabrications
2. Spot-check PMIDs on PubMed
3. Look for suspiciously perfect or generic snippets
4. Remove any evidence that cannot be verified

### Handling Unfetchable References

If a reference cannot be fetched:
1. Manually check PubMed for the PMID
2. If it exists but is restricted, note in explanation
3. If it doesn't exist, remove the evidence item
4. Consider replacing with a valid alternative reference

## Reference Validation on Deep-Research Reports

There are **two** reference-validation layers now, checking two different things.
Do not report one as if it were the other.

| | DR report validation | KB evidence validation |
|---|---|---|
| What it checks | the identifiers and quotes in `research/*-deep-research-*.md` | the `snippet:` on each evidence item in `kb/**/*.yaml` |
| When it runs | while the report is generated (`just research-disorder` etc.) | in the curation loop and before the PR |
| Command | built in; retro-fit with `just validate-research-reference` | `just count-verified-snippets`, `just validate-disorders` |
| Where results live | in the report — frontmatter + `## Reference Validation` | validator stdout |

Since `deep-research-client` 0.2.9, every `just research-*` recipe resolves the
report's PMIDs/DOIs and checks its quoted claims as it generates the report, and
writes the outcome into the report itself:

- a `reference_validation:` block in the YAML frontmatter (`total_references`,
  `verified`, `not_found`, `unverifiable`, `confabulation_rate`,
  `quotes_checked`, `quotes_valid`, `unresolved_references`)
- a `## Reference Validation` section at the end of the body, with a counts table
  and an `### Unresolved references` list

Since 0.2.10 the same pass adds a third check — **topical relevance**. Each
resolved reference's already-fetched record (title, journal, MeSH terms,
abstract) is scored against the report's own most characteristic vocabulary;
`>= 0.35` is on topic, `<= 0.08` is off topic. It costs no extra lookups and is
on by default. It adds `relevance_assessed` / `on_topic` (and `off_topic` +
`off_topic_references` when something is flagged) to the frontmatter, a
`### References that may not be about this subject` section to the body, and sets
`needs_review: true`.

**Read that before citing anything from the report.** An identifier listed under
`unresolved_references` should not be curated into an evidence item — find
another source or drop the claim. `needs_review: true` is the single key worth
grepping for: it is set by an unresolved identifier, an unsupported quote, *or*
an off-topic reference, whereas `confabulation_rate` only measures identifier
resolution.

An **off-topic flag is evidence, not a verdict.** The reference resolved, so it
is not a fabrication — it just shares little vocabulary with the report, and a
paper can be relevant in ways its title and abstract do not spell out. Read it
before dropping the claim. Off-topic references deliberately do not count as
confabulations and do not trip `--fail-on-unresolved`.

For a report generated before 0.2.9 (most of `research/`):

```bash
just validate-research-reference research/Marfan_Syndrome-deep-research-falcon.md
```

This appends the section in place and is safe to re-run. It does **not** add a
frontmatter summary — upstream only refreshes one that is already present — so on
a retro-fitted report, read the section at the bottom of the file.

**Three things this deliberately does not do:**

1. It does not validate KB snippets. A green report is not evidence that your
   `kb/` entry is correctly quoted — the snippet you paste is a different quote
   in a different file.
2. It cannot catch Named Entity Confusion (a report about the wrong disease
   cites real papers correctly). Run `just preflight-dr` as usual. The relevance
   check does not help here: it scores references against the report's *own*
   vocabulary, so a wrong-disease report and its wrong-disease citations agree
   with each other and everything reads as on topic.
3. It cannot catch a real paper cited for a claim it does not make, where the
   report paraphrases rather than quotes (issue #7791).

Full detail: [`docs/deep-research-reference-validation.md`](../../../docs/deep-research-reference-validation.md).

## Integration with Schema

The evidence structure is defined in `src/dismech/schema/dismech.yaml`:

```yaml
EvidenceItem:
  attributes:
    reference:
      description: PMID, DOI, or ClinicalTrials.gov reference
      pattern: "^PMID:\\d+$|^DOI:.*$|^clinicaltrials:NCT\\d+$"
    supports:
      range: SupportType
    snippet:
      description: Quoted text from the reference
    explanation:
      description: Why this evidence supports/refutes the claim
```

### Clinical Trials Integration

The `ClinicalTrial` class in the schema supports:
- **name**: NCT identifier or trial name
- **phase** (`ClinicalTrialPhaseEnum`): `PHASE_I`, `PHASE_II`, `PHASE_III`, `PHASE_IV`, or
  `NOT_APPLICABLE` (observational or device studies that do not follow the standard FDA
  phase classification)
- **status** (`ClinicalTrialStatusEnum`): `RECRUITING`, `NOT_RECRUITING`, `ACTIVE_NOT_RECRUITING`,
  `COMPLETED`, `ENROLLING_BY_INVITATION`, `SUSPENDED`, `TERMINATED`, `WITHDRAWN`, or `UNKNOWN`.
  Both slots are enum-bound — the free-text spellings (`Phase III`, `Completed`) fail `just validate`.
- **description**: Summary of the trial
- **target_phenotypes**: Phenotypes the trial addresses (as PhenotypeDescriptor objects with HP ontology terms)
- **evidence**: Evidence items validated against ClinicalTrials.gov

Example clinical trial entry with ontology-linked phenotypes:
```yaml
clinical_trials:
- name: NCT05813288
  phase: PHASE_III
  status: COMPLETED
  description: Study of dexpramipexole in severe eosinophilic asthma
  target_phenotypes:
    - preferred_term: Wheezing
      term:
        id: HP:0030828
        label: Wheezing
    - preferred_term: Breathlessness
      term:
        id: HP:0002094
        label: Dyspnea
  evidence:
  - reference: clinicaltrials:NCT05813288
    supports: SUPPORT
    snippet: "The objective of this clinical study is to investigate the safety, tolerability, and efficacy of dexpramipexole in participants with inadequately controlled severe eosinophilic asthma."
    explanation: "This trial directly evaluates a therapeutic approach for severe eosinophilic asthma"
```
