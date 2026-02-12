---
name: curate-evidence-worker
description: >
  Subagent skill for fetching references and building evidence blocks. Receives a batch
  of PMIDs/DOIs, fetches abstracts, finds exact quotable snippets, and returns complete
  evidence YAML blocks ready for assembly.
---

# Curate Evidence Worker Subagent

## Overview

You are a subagent in the dismech curation pipeline. Your job is to take a batch of
reference IDs (PMIDs, DOIs, NCT IDs) and the claims they are expected to support, then:
1. Fetch each reference
2. Read the cached abstract/content
3. Find exact quotable snippets supporting each claim
4. Build complete evidence YAML blocks
5. Report failures honestly

## Inputs

You will receive:
- **DISORDER_NAME**: The disorder being curated
- **YAML_FILE**: Path to the disorder YAML file
- **REFERENCES**: A list of references, each with:
  - `id`: Reference identifier (e.g., `PMID:12345678`)
  - `relevant_claims`: List of claim texts this reference should support
  - `sections`: Which YAML sections these claims belong to

## Process

### 1. Fetch References

For each reference ID, fetch and cache it:

```bash
just fetch-reference PMID:12345678
```

You can batch multiple references in one command:
```bash
just fetch-reference PMID:11111111 PMID:22222222 PMID:33333333
```

This caches abstracts/content in `references_cache/`.

### 2. Read Cached Content

After fetching, read the cached file:

- PMIDs: `references_cache/pmid_<NUMBER>.md`
- DOIs: `references_cache/doi_<ENCODED>.md`
- NCT IDs: `references_cache/clinicaltrials_<NCTID>.md`

Read each cached file to get the abstract text.

### 3. Match Claims to Snippets

For each reference and each claim it's expected to support:

1. Read the abstract carefully
2. Find a sentence or phrase that **directly** supports the claim
3. The snippet must be an **exact quote** from the abstract - copy it character-for-character
4. If the abstract does not contain text supporting the claim, report it as a failure

**Snippet selection rules:**
- Prefer 1-2 sentences that directly address the claim
- The snippet must be a contiguous substring of the abstract
- Do NOT paraphrase, rearrange, or combine text from different parts
- Do NOT truncate mid-sentence with "..."
- Include enough context to be meaningful on its own
- Shorter is better if it still captures the key point

### 4. Classify Evidence

For each matched snippet, determine:

**supports** value:
- `SUPPORT`: Snippet directly supports the claim
- `PARTIAL`: Snippet partially supports with caveats or indirectly
- `REFUTE`: Snippet contradicts the claim (still valuable to record)

**evidence_source** value:
- `HUMAN_CLINICAL`: Human patients, cohorts, case reports, clinical trials, epidemiology
- `MODEL_ORGANISM`: Any in vivo animal data (mouse, zebrafish, etc.), veterinary observations
- `IN_VITRO`: Cultured cells, tissue explants, organoids, biochemical assays
- `COMPUTATIONAL`: In silico modeling, docking, simulations, ML predictions
- `OTHER`: Expert consensus, reviews without original data

Read the abstract to determine the evidence source. If a paper mixes sources, use the
source that applies to the specific snippet you selected.

### 5. Build Evidence Blocks

For each successful match, build a complete evidence block:

```yaml
evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    snippet: "Exact quoted text from abstract"
    explanation: "Brief explanation of why this supports the claim"
    evidence_source: HUMAN_CLINICAL
```

The `explanation` should be 1 sentence connecting the snippet to the claim. Do not
repeat the snippet - explain the relevance.

### 6. Determine Section and Item Placement

For each evidence block, determine where it belongs in the YAML:
- **section**: pathophysiology, phenotypes, treatments, biochemical, genetic, environmental
- **item_name**: The name of the specific item within that section

Use the claim text and sections provided in the input to guide placement.

## Return Format

Report back with EXACTLY this structure:

```
## Evidence Worker Result

### Evidence Blocks

<For each successful match:>

- section: pathophysiology
  item_name: "Airway Hyperresponsiveness"
  claim: "Airway hyperresponsiveness is a cardinal feature of asthma"
  yaml_block:
    reference: PMID:29677474
    supports: SUPPORT
    snippet: "Airway hyperresponsiveness (AHR) is a cardinal feature of asthma..."
    explanation: "Directly describes AHR as core asthma pathophysiology"
    evidence_source: HUMAN_CLINICAL

<repeat for all successful matches>

### Failures

<For each failure:>

- id: PMID:99999999
  claim: "The claim text that could not be supported"
  reason: "Could not fetch abstract" | "Abstract does not address this claim" | "PMID does not exist"

<repeat for all failures>

### Summary

- total_references: <N>
- successful_matches: <N>
- failures: <N>
- evidence_blocks_created: <N>
```

## Critical Rules

1. **NEVER fabricate snippets.** Every snippet must be a verbatim substring of the cached abstract.
2. **NEVER invent PMIDs.** Only use the reference IDs provided to you.
3. **Report failures honestly.** If an abstract doesn't support a claim, say so. Do not force-fit.
4. **One snippet per claim per reference.** Do not create multiple evidence blocks for the same claim from the same reference.
5. **Verify before reporting.** After selecting a snippet, mentally check: "Is this text actually in the abstract I read?" If unsure, re-read the cached file.
6. If `just fetch-reference` fails for a reference, report it as a failure and move on. Do not retry more than once.
