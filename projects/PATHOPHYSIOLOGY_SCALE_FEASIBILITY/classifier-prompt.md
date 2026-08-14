# Pathophysiology Node Kind Classifier — Prompt Spec

Shared specification for the feasibility analysis described in
[../../docs/superpowers/specs/2026-06-26-pathophysiology-scale-feasibility-design.md](../../docs/superpowers/specs/2026-06-26-pathophysiology-scale-feasibility-design.md).

Any classifier (inline, subagent, future API script) should follow this prompt
and emit this exact JSON schema, so passes are comparable.

## Task

You are classifying nodes from `pathophysiology[]` lists in dismech disorder
YAML files. Each node is one assertion the curator chose to write as a single
pathology step. Your job is to assign exactly one `kind` to each node from a
small enum, capture how well it fits, and flag bundled or unclassifiable nodes.

## The starting enum (pass 1)

| Kind | Definition | Substrate |
|---|---|---|
| `MOLECULAR_ACTIVITY` | A specific molecular function of a gene product, complex, or chemical — kinase activity, phosphatase activity, transcription factor binding, ion transport. Includes pathway-level signaling activity when it lives at the protein-interaction scale. | molecules, complexes |
| `CELLULAR_PROCESS` | A process happening at the level of one cell or cell type — differentiation, apoptosis, autophagy, intracellular transport, cell-intrinsic signaling, cell division, polarity. | cells |
| `TISSUE_PROCESS` | A process at the level of a tissue, organ, or anatomical structure — inflammation in a tissue, fibrosis, granuloma formation, vascular remodeling, organ damage, edema, neoplastic growth. | tissues, organs, anatomical sites |
| `ORGANISM_PROCESS` | A systemic / multi-organ / whole-body process — coagulopathy (system-wide), cytokine storm, multi-system developmental syndrome, metabolic acidosis as a systemic state, fever, cachexia. | organism |

If none of these fit, do **not** force one — set `confidence: 1` or `2` and use
`proposes_new_kind` to describe what's missing.

## Output schema (per node, JSON)

```json
{
  "primary_kind": "MOLECULAR_ACTIVITY",
  "confidence": 4,
  "second_choice_kind": null,
  "proposes_new_kind": null,
  "split_suggestion": null,
  "reasoning": "one sentence"
}
```

Field definitions — read these carefully, the prior pass conflated some:

- **`primary_kind`** — single value from the enum. Forced choice even when fit is poor; the model of `proposes_new_kind` carries the dissent.
- **`confidence`** — 1-5 integer. **Asks one thing only: how well does this node fit a *single* kind?** It does NOT measure how confident you are that the node is well-designed, nor does it measure split-ness. A bundled node may still fit a single kind cleanly (high confidence) if the bundle is at one scale.
  - 5: unambiguous, the node is clearly one kind
  - 4: clear primary kind, minor scale-axis ambiguity
  - 3: real tie between two kinds, but the primary is defensible
  - 2: poor fit to any kind in the enum; primary is the least-bad option
  - 1: no kind fits at all (must also set `proposes_new_kind`)
- **`second_choice_kind`** — required when `confidence ≤ 3`; otherwise null. The runner-up.
- **`proposes_new_kind`** — free text, only when the enum is genuinely missing a category. Format: `"NEW_KIND_NAME — one-sentence justification"`. Null when the existing 4 cover the node.
- **`split_suggestion`** — **independent of `confidence`.** Asks: does this node bundle two or more distinct claims that should be separate pathophysiology entries? If yes, describe the proposed split. Null if the node is atomic. A high-confidence single-kind node can still be a split candidate (if the bundle is two claims at the *same* scale).
- **`reasoning`** — one sentence, focused on the *primary_kind* call (not on splits or new kinds — those have their own fields).

## Input you'll receive per node

The node's `name`, `description`, and these descriptor slots when present:
`cell_types`, `biological_processes`, `molecular_functions`, `locations`,
`chemical_entities`, `cellular_components`, `protein_complexes`, `gene_products`.

Each descriptor may carry a `modifier` (INCREASED / DECREASED / etc.) and an
ontology `term` — these are diagnostic signals: lots of `molecular_functions`
suggests molecular scale, `locations` (anatomy) suggests tissue, etc. But don't
mechanically infer from slot presence alone — the `name` and `description` are
authoritative.

## Calibration guidance

- **Don't penalize bundles in confidence.** "PML-RARA Fusion Oncogene Formation"
  bundles a translocation event and a fusion protein's activity, but if you
  decide the *primary* claim is molecular-scale, score confidence on how well
  that primary fits — then flag the bundle in `split_suggestion`.
- **Watch for states vs processes.** Several nodes describe entity *states*
  (a fusion protein exists, an organelle is disrupted, a cell population has
  accumulated, an organ is malformed) rather than ongoing processes. The
  starting enum is process-centric — these are exactly the cases where
  `proposes_new_kind` should fire.
- **"Multi-organ" disambiguation.** Three patterns to distinguish:
  - *Same tissue-level process in multiple tissues independently* (granulomas
    in lung + liver + kidney; fibrosis in multiple organs; granulomatous
    vasculitis affecting multiple beds): stay with `TISSUE_PROCESS` and add
    `split_suggestion` to separate by organ. The mechanism is the same; the
    multi-organ-ness is just curator-bundling.
  - *Truly coordinated systemic phenomenon* (DIC, cytokine storm, fever,
    cachexia, metabolic acidosis as a system state, anaphylaxis): use
    `ORGANISM_PROCESS`. The whole organism is the unit.
  - *Multi-organ developmental defect bundle* (cataract + hearing loss +
    cranial dysmorphism + growth restriction co-occurring as a syndromic
    pattern): use `ORGANISM_PROCESS` only if the curator framed it as one
    syndromic outcome; prefer `split_suggestion` if the pieces are
    mechanistically independent.

## Split-piece classification mode

When asked to classify hypothetical split pieces of a bundled node, propose 2-N
atomic node names + descriptions, then run the same schema on each piece.
Report whether each piece cleanly fits a single kind (this validates both the
split *and* the taxonomy).
