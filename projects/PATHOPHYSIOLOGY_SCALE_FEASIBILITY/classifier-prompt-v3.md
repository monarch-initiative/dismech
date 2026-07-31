# Pathophysiology Node Kind Classifier — Prompt Spec v3

Successor to [classifier-prompt-v2.md](./classifier-prompt-v2.md). The enum is unchanged from v2 (scale-only: MOLECULAR / CELLULAR / TISSUE / ORGANISM, each covering both processes and states). The only substantive change is **explicit split-detection emphasis**: pass 2 saw split-flag rate drop from 41% (pass 1) to 4%, almost certainly because the v2 prompt narrated kind-classification so heavily that agents anchored on "this is clean now" and stopped looking for bundles.

In v3, split detection is treated as a **co-equal task** with kind classification, not a side note.

## The enum (unchanged from v2)

| Kind | Scale | Covers — both processes and states |
|---|---|---|
| `MOLECULAR` | molecules, complexes, genetic elements, small molecules | molecular activities (kinase activity, TF binding, transport); molecular states (a fusion protein exists, a chemical accumulates, a gene has a variant burden) |
| `CELLULAR` | one cell or cell type | cellular processes (differentiation, apoptosis, signaling within a cell); cellular states (a cell population is in a maintained aberrant condition; an organelle structure is disrupted) |
| `TISSUE` | tissue, organ, anatomical structure | tissue processes (inflammation, fibrosis, granuloma formation); tissue states (an ectopic tissue persists, an organ is malformed, a lesion exists) |
| `ORGANISM` | systemic / multi-organ / whole-body | systemic processes (DIC, cytokine storm); systemic states (chronic metabolite elevation, dysbiotic microbiome, syndromic developmental phenotype) |

Re-read the v2 spec for full guidance on scale assignment, "states are not a gap," and substrate-of-the-node thinking. The output schema is unchanged.

## Two co-equal tasks per node

For each node, ask **both** questions independently:

### Task A — Kind assignment
Pick the single best scale from the enum. Output `primary_kind`, `confidence` (1-5 = "how well does this fit a *single* kind"), `second_choice_kind` when confidence ≤ 3.

### Task B — Bundle / split detection
Independently ask: **does this node bundle two or more distinct mechanistic claims that should be separate pathophysiology entries?** Output `split_suggestion` (a description of the proposed split, or empty if atomic). This is **fully orthogonal** to Task A — a node can be high-confidence single-kind AND a split candidate at the same time.

**Critical anchoring warning:** If you just classified the kind cleanly, do NOT skip Task B. The v3 dataset includes nodes where the kind is unambiguous (high confidence) but the node bundles multiple atomic claims at that scale. Examples seen in v1: "Hepatic / Renal / Pulmonary Visceral Involvement" (cleanly TISSUE; clearly 3+ separate per-organ claims), "Stabilized MAF Protein and Dysregulated Transcriptional Programs" (cleanly MOLECULAR; clearly 2 claims). Clean kind ≠ atomic node.

## Bundle patterns to watch for

Treat these as triggers to actively consider `split_suggestion`. Match the *pattern*, not just the wording:

1. **Conjunctions in the node name** — "and", "&", commas listing multiple things, slashes. Examples: "Stabilization and Dysregulation," "Visceral and Vascular Involvement," "Cataract / Hearing Loss / Developmental Delay."
2. **Multi-organ enumeration** — node name or description lists ≥2 anatomical sites without explicit shared mechanism (e.g., "involves lung, liver, and kidney"). Distinct sites with the same underlying mechanism → split into per-site nodes. (Truly coordinated systemic = ORGANISM, single node.)
3. **Etiology bundled with consequence** — node name combines a cause (variant, translocation, fusion) with its downstream effect (activity, dysregulation, deficiency). Example: "PML-RARA Fusion Oncogene Formation" bundles the translocation event with the fusion protein's aberrant activity.
4. **Mechanism bundled with outcome** — node describes a mechanism (e.g., "Stabilization via Ubiquitination Failure") and its downstream effect (e.g., "Dysregulated Transcriptional Programs") in one breath. Each is a separate causal node.
5. **Multi-step pathway compressed** — description reads like a chain ("A leads to B leads to C"), all under one node name. Each step may deserve its own node.
6. **"Multiple X" or "X, Y, and Z phenotypes"** — node lists several phenotypes or sub-mechanisms in plural ("Multisystem developmental defects," "Multiple endocrine abnormalities").
7. **Long heterogeneous descriptions** — description that touches multiple cell types, multiple processes, or multiple anatomical structures without an obvious unifying mechanism is likely two or more claims fused.

When you flag a split, describe the proposed atomic pieces in `split_suggestion`. Format: `"Split into: (1) <piece 1>; (2) <piece 2>; ..."`. One sentence is fine — you don't need to fully re-describe each piece.

## What does NOT warrant a split

- A node with one mechanism realised in one cell type at one location (even if the description is long) — fine.
- A node citing multiple evidence sources for one claim — fine.
- A node naming multiple gene names that all act through the same activity (e.g., "SOS1, SOS2, NRAS Activation" if all converge on the same RAS-GTP loading step) — judgment call; lean atomic if mechanism is shared.
- A pure description of one substance's elevated state across the body (e.g., "Hyperphenylalaninemia") — single ORGANISM-scale state, not a bundle.

## Output schema (unchanged from v1/v2)

```json
{
  "primary_kind": "MOLECULAR",
  "confidence": 4,
  "second_choice_kind": null,
  "proposes_new_kind": null,
  "split_suggestion": "Split into: (1) ...; (2) ...",
  "reasoning": "one sentence on the primary_kind call (not on the split)"
}
```

`split_suggestion` should be populated whenever the bundle-patterns above match. Empty `split_suggestion` is an active assertion that the node is atomic — don't leave it empty by default.

## Hypothesis being tested in v3

If pass-3 split rate returns to ~30-45% (matching pass-1's 41%), then pass-2's 4% was a prompt-attention artifact and the node-hygiene argument for Proposal B is intact. If pass-3 split rate stays low (<15%), state-shaped bundles may genuinely have been the dominant source of pass-1 splits, and the scale-only renaming silently solved more than just the taxonomy gap.
