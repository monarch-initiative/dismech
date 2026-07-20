# Pathophysiology `biological_scale:` slot — Feasibility Analysis Design

**Date:** 2026-06-26
**Status:** Executed — see [`projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md`](../../../projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md) for the final report
**Related:** [v2.5 incremental proposals discussion](./2026-05-01-phenocam-data-model-redesign.md)

> **Naming note.** This spec was written under the working name `kind:`. The completed analysis showed the four enum values encode biological scale only, and the slot was renamed to `biological_scale:` on completion. The body below is preserved with the working name to reflect what we designed at the time; only the enum name (`BiologicalScaleEnum`) has been updated to match what actually shipped.

## Purpose

Inform two design decisions for the proposed `kind:` slot on `Pathophysiology`:

1. **Taxonomy design** — what enum values belong in `BiologicalScaleEnum`? Do the starting four (MOLECULAR_ACTIVITY, CELLULAR_PROCESS, TISSUE_PROCESS, ORGANISM_PROCESS) cover the real corpus, or are additional kinds (e.g., BIOCHEMICAL_STATE, STRUCTURAL_ABNORMALITY) needed?
2. **Curator burden estimate** — how often do curators hit ambiguous nodes, and how often does forcing single-class assignment surface nodes that should be split?

This analysis is for *our own* design judgment. It does not need to be defensible to a skeptical team — the artifacts produced should be inspectable, but we are not pursuing formal ground-truthing or reproducibility guarantees.

## Approach

Stratified sample of ~10 disorders (with allowance for 1-2 thin-node disorders), classified node-by-node by an LLM, run in **small batches** so we catch concerning signal early without committing to a large run that turns out to need rework.

### Sample selection

- Pull most recently `updated_date`-touched disorders from `kb/disorders/`
- Prune greedily to maintain category diversity (no more than 2 per category from: metabolic, cancer, neuro, congenital, immune, autoimmune, infectious, vascular, dermatologic, dev/syndromic, cardiovascular)
- Prefer disorders with ≥5 pathophysiology nodes for signal density
- Allow up to 2 disorders with <5 nodes — thin pathographs are informative cases too (kind ambiguity may look different when the curator hasn't yet teased apart sub-mechanisms)
- Target: ~10 disorders, ~150-200 total nodes

### Classification

One LLM call per node. **Sonnet 4.6** (not Haiku — Haiku tends to over-pick MOLECULAR_ACTIVITY when a node merely mentions a gene; the scale-judgment calls genuinely benefit from stronger reasoning, and at this volume Sonnet cost is pennies).

**Input per node:** `name`, `description`, and structured descriptor slots (`cell_types`, `biological_processes`, `molecular_functions`, `locations`, `chemical_entities`, `cellular_components`, `protein_complexes`, `gene_products`).

**Output (structured JSON):**

| Field | Type | Notes |
|---|---|---|
| `primary_kind` | enum value | Single choice from current enum |
| `confidence` | int 1-5 | 5 = unambiguous, 1 = forced guess |
| `second_choice_kind` | optional enum | Required when `confidence ≤ 3` |
| `proposes_new_kind` | optional string | Free text when no kind fits ("this is really a BIOCHEMICAL_STATE") |
| `split_suggestion` | optional string | "yes if bundles two kinds; describe the two" |
| `reasoning` | string | One sentence justification |

### Two-pass iteration

1. **Pass 1** — starting enum: {MOLECULAR_ACTIVITY, CELLULAR_PROCESS, TISSUE_PROCESS, ORGANISM_PROCESS}. Read `proposes_new_kind` outputs; cluster them.
2. **Pass 2** — expanded enum incorporating ≤2 new kinds from pass-1 clusters (likely candidates: BIOCHEMICAL_STATE, STRUCTURAL_ABNORMALITY). Re-classify the same nodes.

If pass-2 ambiguity rate drops markedly and "doesn't fit" calls collapse, the expanded enum is the finding. If not, the original 4 hold up.

### Batching strategy

Run the disorders in small batches (3 disorders ≈ 30-60 nodes per batch) rather than all 10 at once. After each batch:

- Eyeball the results for obvious classifier failures
- Flag any unexpected `proposes_new_kind` cluster early
- Adjust the prompt if confidence is systematically too high/low
- Decide whether to continue, change the prompt, or stop

This avoids burning a full run on a prompt that turns out to be miscalibrated.

## Deliverables

- `projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass1-results.csv` — every classified node, all fields, raw
- `projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass2-results.csv` — same, after enum expansion (if pass-2 runs)
- `projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md` — synthesis (project narrative with frontmatter):
  - Histogram of `primary_kind` per pass
  - `proposes_new_kind` cluster summary (frequency + representative examples)
  - Top-10 ambiguous nodes with worked examples
  - Top-10 split candidates with worked examples
  - Recommended final enum
  - Per-disorder summary table (kind distribution per disorder)
  - Confidence distribution

## Explicitly out of scope (defer)

- **Combine candidates** — needs different signal (A→B chain analysis with shared cell_types/BP). Run as a separate pass *only if* pass-1 ambiguity results look encouraging.
- **Manual ground-truthing** — eyeball spot-check the 10 highest- and 10 lowest-confidence calls per pass, but no formal labeled set.
- **Scaling to all 958 disorders** — let pass-2 results decide.
- **Visualization / interactive browser** of results — markdown + CSV is enough for design judgment.

## Decision criteria

Coming out of the analysis:

| Outcome | Action |
|---|---|
| 4-kind enum: <15% ambiguity, <5% "doesn't fit" | Ship Proposal B with original 4 kinds |
| 4-kind enum: 15-30% ambiguity, clear "doesn't fit" cluster | Run pass 2 with 1-2 added kinds; ship the expanded enum if ambiguity drops |
| Even pass-2: >30% ambiguity | Reconsider — `kind:` may be the wrong abstraction (perhaps separate `scale:` and `nature:` tags) |
| Split-candidate count high (>20% of nodes) | Document as a curation-quality finding; consider a separate "node hygiene" pass before pushing `kind:` |

## Implementation outline

1. Selection script — pulls candidate disorders by recency + diversity, prints proposed sample
2. Classification script — takes a disorder file, loops nodes, calls Sonnet, emits JSON rows
3. Batch driver — runs N disorders, appends rows to CSV, prints quick summary
4. Reporting script — generates `report.md` from the CSV

Runs in `projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY/` (following the `projects/*.md` + `projects/*/` convention documented in `docs/projects.md`) to keep this exploratory work out of the main `scripts/` tree until/unless it earns a permanent place.

## Out-of-scope alternates considered

- **Whole-population census** (Approach 1 in brainstorm): cheap but produces a 10k-row CSV nobody reads. Deferred.
- **Haiku classifier**: marginally cheaper, materially worse on scale judgments where node language is biological-rich. Not used.
- **Multi-label classification**: would let curators paper over conflated nodes. Single-class friction is the *point*.
