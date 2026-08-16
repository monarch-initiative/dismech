---
title: A Simple Tree for Pathograph Node Classification
status: BRAINSTORM
description: >-
  Proposes a single flat `node_class` enum for pathophysiology nodes, ordered
  as a causal cascade: genomic -> environmental -> molecular -> pathway ->
  cellular -> tissue/organ -> systemic -> outcome, plus two cross-cutting
  classes (compensation, intervention point). Validated against all 12,290
  pathophysiology nodes; replaces the improvised 55-value free-text `role`
  vocabulary.
tags: [SCHEMA_EVOLUTION, PATHOGRAPH, PATHOPHYSIOLOGY, BRAINSTORM]
---

# A Simple Tree for Pathograph Node Classification

**Status: brainstorm.** One slot, one flat enum, values ordered as a cascade.

## The tree

```
1. GENOMIC_PERTURBATION      the lesion in the genome
     variant / allele              "Biallelic HMGCL loss of function"
     dosage                        "Recurrent LCR22-mediated multigene deletion"
     structural / fusion           PML-RARA, BCR-ABL1
     epigenetic                    "Maternal 15q11-q13 dosage increase"

2. ENVIRONMENTAL_PERTURBATION  the insult from outside
     chemical / drug / toxin       "Supratherapeutic Acetaminophen Exposure"
     infectious agent              "Persistent HIV Infection and Replication"
     physical                      radiation, trauma, mechanical load
     nutritional                   deficiency or excess
     physiological stressor        fasting, fever, catabolic stress

3. MOLECULAR_EFFECT           what the lesion does to a molecule
     protein function change       "HMGCS2 Catalytic Loss"
     misfolding / aggregation      amyloid oligomers, tau tangles
     metabolite accumulation       "Reactive valine-derived intermediate accumulation"
     metabolite depletion          "Low L-Serine and Downstream Metabolites"
     transport / channel defect    "Sodium channel dysfunction"

4. PATHWAY_EFFECT             signalling and flux
     signalling up / down          "FSHR Signaling Resistance"
     metabolic flux block          "Impaired leucine degradation"
     transcriptional program       HIF stabilisation, NF-kB activation

5. CELLULAR_EFFECT
     cell death                    apoptosis, necrosis, pyroptosis
     proliferation / growth
     differentiation / identity    "Testis differentiation in 46,XX gonads"
     organelle dysfunction         mitochondrial, lysosomal, ER stress
     stress response / senescence

6. TISSUE_ORGAN_EFFECT
     inflammation
     fibrosis / remodelling
     structure formed              thrombus, granuloma, atheroma, cyst, amyloid deposit
     degeneration / atrophy
     barrier failure

7. SYSTEMIC_EFFECT            whole-body physiology
     organ failure
     metabolic crisis              "Acute hypoketotic metabolic decompensation"
     systemic derangement          hyperammonaemia, cytokine storm

8. OUTCOME                    what happens to the patient
     clinical manifestation, disability, death

--- not tiers; these cut across all of the above ---

C1. COMPENSATION              the body pushing back
     host defence, adaptive escape, protective response

C2. INTERVENTION_POINT        where a drug acts
     the node a treatment targets or a resistance mechanism defeats
```

## Why this ordering, not just a vibe

Mean topological depth (longest path from a graph source, computed over
`downstream` edges) for the 3,704 nodes that carry a curated
`biological_scale`:

| tier | n | mean depth | median |
|---|---:|---:|---:|
| MOLECULAR | 1,066 | 1.71 | 1.0 |
| CELLULAR | 963 | 3.25 | 2.0 |
| TISSUE | 920 | 4.57 | 3.0 |
| ORGANISM | 755 | 4.74 | 4.0 |

Monotonic. Curators are already drawing the cascade in this order without
being asked to — the tier ordering is a description of the KB, not an
imposition on it.

The one soft join is TISSUE (4.57) vs ORGANISM (4.74), which barely separate.
That is the argument for splitting tier 7 (SYSTEMIC) from tier 8 (OUTCOME):
"organ failure" and "the patient decompensates" are currently collapsed into
one `ORGANISM` bucket doing two jobs.

## What this replaces

`role` is a free-text `string` slot with `examples: [Primary]` and no enum.
2,322 nodes use it, with **55 distinct values** after normalising case and
spacing (72 before — `trigger`, `TRIGGER`, and `Trigger` all occur). Top eight
cover 90%; the 41-value tail is where it fell apart:

| value | n | | value | n |
|---|---:|---|---|---:|
| trigger | 472 | | therapeutic_vulnerability | 91 |
| consequence | 384 | | intermediate | 34 |
| central_effector | 362 | | mechanism | 31 |
| effector | 327 | | driver | 30 |
| amplifier | 213 | | adaptive_escape | 30 |
| mediator | 122 | | modifier | 29 |
| outcome | 94 | | *(41 more, <=13 each)* | 227 |

The tail conflates four different questions in one slot: cascade position
(`upstream`, `root`, `endpoint`), confidence (`provisional_effector`,
`emerging_mechanism`, `disputed_branch`), direction (`protective`,
`host_defense`), and drug interface (`therapeutic_vulnerability`,
`intrinsic_resistance`). The tree absorbs the last two as C1/C2, and the first
two are handled below.

## Two things the tree should *not* try to do

**Don't encode where the node sits in the graph — the graph already knows.**
Cross-tabbing curated `role` against topology:

| role | n | source | internal | sink | isolated |
|---|---:|---:|---:|---:|---:|
| trigger | 352 | **89%** | 11% | 0% | 0% |
| mediator | 122 | 1% | **99%** | 0% | 0% |
| central_effector | 257 | 4% | **96%** | 0% | 0% |
| amplifier | 140 | 4% | **95%** | 1% | 0% |
| consequence | 270 | 0% | 55% | **44%** | 1% |
| outcome | 86 | 0% | 56% | **44%** | 0% |

`trigger` is just "graph source". `consequence` and `outcome` are
indistinguishable from each other and from "graph sink". Compute those; don't
ask a curator to retype them. `therapeutic_vulnerability` is 55% *isolated* —
those nodes have no pathophysiology edges at all and exist only as targets of
`treatments.target_mechanisms`, which is exactly C2 and exactly derivable.

**Don't encode confidence.** `mechanism_confidence` already exists
(`ESTABLISHED` 373 / `PROVISIONAL` 348 / `HYPOTHETICAL` 89). A node is
`PATHWAY_EFFECT` whether or not the pathway claim is solid.

## Overlap with existing sections — worth deciding early

Tiers 1 and 2 duplicate the `genetic:` and `environmental:` sections, which are
already separate node types in the pathograph. But curators *do* write genomic
lesions as pathophysiology nodes — roughly 7% of node names carry variant /
dosage / fusion language, and "Biallelic HMGCL loss of function" is a
pathophysiology node, not a `genetic:` entry.

Two options, and this needs a decision rather than a default:

- **Keep tiers 1-2 in the enum.** Accepts that the same claim can be written
  two ways, but classifies what curators actually wrote.
- **Drop tiers 1-2**, start the enum at MOLECULAR, and treat a genomic
  pathophysiology node as a curation smell that belongs in `genetic:`.

Leaning toward the first for now — reclassifying ~900 existing nodes into
another section is a much bigger change than adding two enum values, and the
overlap can be surfaced as a QC warning instead.

## What it buys

- **Cross-disease queries that don't work today:** every pathological structure
  formed across the KB (tier 6, structure-formed); every metabolic crisis node
  (tier 7); every drug intervention point (C2).
- **Layout.** Colour or column by tier and the pathograph reads as a cascade
  left to right instead of a uniform blue field. Today all 12,290
  pathophysiology nodes render identically.
- **QC with teeth.** A tier-6 node upstream of a tier-3 node is a probable
  mis-drawn edge. A tier-8 OUTCOME node with outgoing `causes` edges is
  probably a phenotype in the wrong section.
- **Bundle detection.** Same trick the `biological_scale` survey used: forcing
  one value per node surfaces nodes doing two jobs (~41% of that survey's
  sample were split candidates). *"Amyloid Fibril Formation and Extracellular
  Deposition"* is tier 3 and tier 6 in one name.

## Open questions

- **8 tiers or 6?** Tiers 3/4 (molecular vs pathway) and 7/8 (systemic vs
  outcome) are the two joins most likely to be argued about. Cheap to test.
- **Does this replace `biological_scale` or sit beside it?** Tiers 3-7 are
  close to a refinement of MOLECULAR/CELLULAR/TISSUE/ORGANISM. Two slots saying
  nearly the same thing would be worse than either alone — most likely
  `node_class` supersedes `biological_scale` and the 3,704 existing values
  migrate mechanically.
- **Adoption.** `biological_scale` sits at 30.1% after being added. Plan for a
  similar ceiling, and seed from existing values rather than from zero.

## Next step

Two things, in order:

1. **Migrate `role` mechanically where it is derivable** — normalise casing
   (3 variants of `trigger` today), compute cascade position and C2 from the
   edges, and see how much of the 2,322 tagged nodes is left over. That number
   sizes the real curation job.
2. **Classify ~100 nodes against the 8+2 tree** to find the contested joins,
   reusing the three-pass structure from
   [the `biological_scale` survey](../../../projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md).

## Appendix — reproducing the numbers

All figures read `kb/disorders/*.yaml` and `kb/modules/*.yaml` via
`dismech.yaml_io.safe_load`. `role` values normalised with
`.strip().lower().replace(' ', '_')`. Degree and depth computed over
`downstream[].target` edges restricted to targets resolving to a
pathophysiology node in the same file; depth is longest path from a source,
iterated to fixpoint with a 12-round cap.
