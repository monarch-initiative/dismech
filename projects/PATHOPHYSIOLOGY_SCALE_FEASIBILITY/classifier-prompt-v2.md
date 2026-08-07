# Pathophysiology Node Kind Classifier — Prompt Spec v2

Companion to [classifier-prompt.md](./classifier-prompt.md) (v1, process-named enum). The only substantive change in v2 is that the enum is renamed to **scale-only**: each kind explicitly covers both processes AND states at that biological scale. This tests the hypothesis that the v1 ambiguity (29%) and all `proposes_new_kind` calls (all variations on `*_STATE`) reflect the v1 names misrepresenting what they were classifying.

## The pass-2 enum (scale-only)

| Kind | Scale | Covers — both processes and states |
|---|---|---|
| `MOLECULAR` | molecules, complexes, genetic elements, small molecules | molecular activities (kinase activity, TF binding, ion transport); molecular states (a fusion protein exists, a chemical accumulates, a gene has a variant burden, an enzyme is functionally deficient). Substrate is a molecule, complex, or genetic element. |
| `CELLULAR` | one cell or cell type | cellular processes (differentiation, apoptosis, autophagy, signaling within a cell); cellular states (a cell population is in a maintained aberrant condition; an organelle structure is disrupted; a cell-type has accumulated). Substrate is a cell. |
| `TISSUE` | tissue, organ, anatomical structure | tissue processes (inflammation in a tissue, fibrosis, granuloma formation, neoplastic outgrowth); tissue states (an ectopic tissue persists, an organ is malformed, a structural lesion exists). Substrate is a tissue, organ, or anatomical site. |
| `ORGANISM` | systemic / multi-organ / whole-body | systemic processes (DIC, cytokine storm, fever); systemic states (a metabolite is chronically elevated, the microbiome is in a dysbiotic configuration, a developmental syndrome bundles multi-organ phenotypes). Substrate is the whole organism. |

**Key point: scale is the noun, process vs. state is just the verb.** "Activity" / "process" suffixes are removed from the v1 names because they pre-judged the verb. A node may describe an ongoing process *or* a persistent state at any of these scales — both are first-class citizens of the same kind.

## Output schema (unchanged from v1)

```json
{
  "primary_kind": "MOLECULAR",
  "confidence": 4,
  "second_choice_kind": null,
  "proposes_new_kind": null,
  "split_suggestion": null,
  "reasoning": "one sentence"
}
```

All field semantics are identical to v1 — re-read the "Field definitions" section of [classifier-prompt.md](./classifier-prompt.md) for those. The only change is the values that `primary_kind` and `second_choice_kind` accept: `MOLECULAR`, `CELLULAR`, `TISSUE`, `ORGANISM` (not the v1 `_ACTIVITY` / `_PROCESS` variants).

## Calibration guidance for v2

Most v1 guidance still applies. The important shifts:

- **States are not a gap, they're in-scope.** If a node describes a persistent state ("Ectopic Endometrial Tissue", "Hyperphenylalaninemia", "Persistent Blastemal Progenitor State"), classify it at the substrate's scale: TISSUE, ORGANISM, CELLULAR respectively. **Do not fire `proposes_new_kind: *_STATE`** — that gap was a v1 artifact.
- **`proposes_new_kind` should fire only if the substrate doesn't fit any biological scale** — e.g., something genuinely outside molecules/cells/tissues/organism (an environmental factor, a treatment, a behavioral phenomenon that isn't body-scale). If you fire it, name the missing category clearly.
- **Confidence and split_suggestion remain independent axes** — same as v1.
- **Multi-organ disambiguation** is unchanged: same coordinated systemic phenomenon → ORGANISM; same tissue process happening in multiple tissues → TISSUE + split_suggestion.
- **Subcellular structural disruption** (PML nuclear body disruption, mitochondrial dysfunction) is CELLULAR — the substrate is the cell whose organelles are disrupted.
- **"Pathway-level signaling"** (Wnt hyperactivation, NF-kB activation) — judgment call between MOLECULAR (the protein-interaction cascade) and CELLULAR (the cell-intrinsic signaling state). If the node names a specific protein-protein interaction or post-translational modification, lean MOLECULAR. If the node describes "a cell is in a Wnt-hyperactivated state," lean CELLULAR. Use second_choice_kind when it's a real tie.

## Hypothesis being tested

If v2 ambiguity drops below 15% and `proposes_new_kind` near-zero, the v1 names were the problem and 4 scale-only kinds are sufficient. If v2 ambiguity stays ≥15% or new kinds keep firing on non-state grounds, residual categorical strain is real and STATE additions (or a deeper rethink) would be warranted.
