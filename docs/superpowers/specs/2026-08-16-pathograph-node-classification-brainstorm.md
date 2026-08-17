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

3. MOLECULAR_ACTIVITY_EFFECT  what the gene product can no longer do
     catalytic activity            "HMGCS2 Catalytic Loss"
     channel conductance           "SCN5A Sodium-Channel Loss of Function"
     transport activity            "Loss of GLUT2 Transporter Function"
     receptor / adaptor activity   "STAT3 dominant-negative dysfunction"

4. MOLECULAR_SUBSTANCE_EFFECT which molecules are now in the wrong amount or form
     metabolite accumulation       "Reactive valine-derived intermediate accumulation"
     metabolite depletion          "Low L-Serine and Downstream Metabolites"
     misfolding / aggregation      "ADan Misfolding and Beta-Sheet Oligomerization"

5. PATHWAY_EFFECT             signalling and flux
     signalling up / down          "FSHR Signaling Resistance"
     metabolic flux block          "Impaired leucine degradation"
     transcriptional program       HIF stabilisation, NF-kB activation

6. CELLULAR_EFFECT
     cell death                    apoptosis, necrosis, pyroptosis
     proliferation / growth
     differentiation / identity    "Testis differentiation in 46,XX gonads"
     organelle dysfunction         mitochondrial, lysosomal, ER stress
     stress response / senescence

7. TISSUE_ORGAN_EFFECT
     inflammation
     fibrosis / remodelling
     structure formed              thrombus, granuloma, atheroma, cyst, amyloid deposit
     degeneration / atrophy
     barrier failure

8. SYSTEMIC_EFFECT            whole-body physiology
     organ failure
     metabolic crisis              "Acute hypoketotic metabolic decompensation"
     systemic derangement          hyperammonaemia, cytokine storm

9. OUTCOME                    what happens to the patient
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

## Splitting MOLECULAR into ACTIVITY and SUBSTANCE

The original sketch had one `MOLECULAR_EFFECT` tier. The corpus says it is two,
and GO's own structure names the missing level: **gene → molecular function →
biological process**. The middle term — *what the gene product can no longer do*
— had no class.

Mean topological depth by grounding, over all 12,290 nodes:

| grounding | n | mean depth | median |
|---|---:|---:|---:|
| gene present (genomic lesion) | 1,985 | 0.94 | 0.0 |
| **GO MF present (activity)** | 647 | **0.81** | 0.0 |
| **CHEBI present (substance)** | 496 | **1.78** | 1.0 |
| CL only (cellular) | 4,567 | 2.25 | 1.0 |
| UBERON present (tissue) | 2,819 | 2.43 | 2.0 |
| no grounding at all | 1,713 | 2.94 | 2.0 |

A full causal step separates activity from substance. And restricting to nodes
curators themselves tagged `biological_scale: MOLECULAR`, MF nodes sit at
**0.87** and CHEBI nodes at **1.90** — that one tag was already covering two
tiers.

Curators had also improvised the class without a slot to put it in: **31 nodes
are literally named `<GENE> molecular function deficiency`**, and 394 node names
(3.4%) are activity-shaped overall (`catalytic loss`, `channel dysfunction`,
`transporter deficiency`, `loss/gain of function`).

**But the new tier does not go between GENOMIC and SUBSTANCE.** Gene-grounded
nodes sit at 0.94 and MF-grounded at 0.81 — statistically the same place.
GENOMIC and ACTIVITY are **alternative entry points**, not sequential steps: an
entry opens either on the lesion or on the broken activity, rarely both. Same
pattern as the SHH/holoprosencephaly case, where the entry opens at pathway
level and the allele stays in `genetic:`.

This relocates part of the earlier tree. `HMGCS2 Catalytic Loss` and `SRD5A2
Loss of Function` were filed under GENOMIC; they are activity claims. GENOMIC
keeps only genome-level content — dosage, structural variants, imprinting,
silencing, transcriptional regulation.

## The GO seed table works

[`pathograph_node_class_go_seed.tsv`](../pathograph_node_class_go_seed.tsv)
hand-classifies the **top 200 GO BP terms** (55.6% of all BP annotations) into
the nine classes, with a `confidence` column so genuinely ambiguous terms
(`inflammatory response`, `nervous system development`) are marked `LOW` and
suggest rather than seed.

Result over all 12,290 pathophysiology nodes:

| | nodes | share |
|---|---:|---:|
| carry ≥1 seeded GO BP term | 5,382 | 43.8% |
| carry ≥1 HIGH-confidence term | 4,675 | 38.0% |
| **→ single unambiguous class (seeded)** | **4,235** | **34.5%** |
| **→ conflicting classes (debundle candidate)** | **440** | **3.6%** |
| + `has GO MF or gene` rule | +1,448 | → 49.8% combined |

**200 decisions classified or flagged ~5,700 nodes.** Seeded distribution:
CELLULAR 43.4%, TISSUE 19.7%, PATHWAY 13.9%, GENOMIC 8.5%, SUBSTANCE 6.2%,
ACTIVITY 4.5%, SYSTEMIC 3.9%.

The 440 conflicts are a second debundling detector, and unlike the earlier one
it needs no curated class at all — a node whose *own* GO annotations span two
classes is making two claims:

- *Impaired Oligodendrocyte Precursor Proliferation and …* — CELLULAR + TISSUE
- *Neutrophil Oxidative and Proteolytic Injury* [ARDS] — CELLULAR + SUBSTANCE
- *Cortical Excitation-Inhibition Imbalance* — CELLULAR + PATHWAY
- *Failure of Poly(ADP-Ribose) Turnover under Stress* — CELLULAR + GENOMIC

Note how many say "and" in the name. Extending the table from 200 to 500 terms
would reach 75.6% of BP annotations for roughly 300 more decisions.

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

## Ontology grounding: evidence for the class, not a second axis

GO / CL / UBERON / CHEBI should **not** become a parallel classification. One
slot stays authoritative; the terms do three jobs *for* it — **seed** it,
**check** it, and **find bundles** in it.

Measured against the 3,704 nodes that already carry a curated
`biological_scale` (using it as a stand-in class label):

| grounding present | n | MOL | CEL | TIS | ORG |
|---|---:|---:|---:|---:|---:|
| GO MF | 313 | **91%** | 8% | 0% | 1% |
| gene | 582 | **81%** | 14% | 3% | 2% |
| GO MF + gene | 59 | **98%** | 2% | 0% | 0% |
| CL + UBERON | 131 | 3% | 18% | **70%** | 8% |
| UBERON alone | 250 | 2% | 2% | **63%** | 34% |
| GO BP + CL | 666 | 13% | **61%** | 20% | 6% |
| **GO BP alone** | 501 | 40% | 24% | 13% | 23% |
| nothing at all | 629 | 12% | 5% | 20% | **62%** |

Two results matter.

**GO MF is near-definitional for MOLECULAR** (91%, and 98% with a gene), and
UBERON pulls hard toward TISSUE. Those are *slot-level* signals — you only need
to know which slot is filled.

**GO BP presence carries no signal at all** (40/24/13/23 — barely different from
the corpus baseline). That is not a defect; GO BP legitimately spans every tier,
from `protein ubiquitination` to `blood coagulation`. It means BP is a
*term-level* signal: you need the identity of the term, not its presence.

**And GO BP term identity does separate — for about half the vocabulary.** Of
the 58 GO BP terms used ≥8× on labelled nodes, 29 are ≥70% one scale:

| clean | | genuinely ambiguous | |
|---|---|---|---|
| `GO:0006914` autophagy | 92% CELLULAR | `GO:0006954` inflammatory response | 47% |
| `GO:0016567` protein ubiquitination | 92% MOLECULAR | `GO:0007399` nervous system development | 37% |
| `GO:0001913` T cell mediated cytotoxicity | 92% CELLULAR | `GO:0007596` blood coagulation | 43% |
| `GO:0030182` neuron differentiation | 88% CELLULAR | `GO:0007224` smoothened signaling pathway | 47% |
| `GO:0006325` chromatin organization | 84% MOLECULAR | `GO:0006487` protein N-linked glycosylation | 44% |

The ambiguous column is ambiguous for a real reason — inflammation genuinely
happens at cellular, tissue, and organism scale. Don't force those; they are
exactly where the class has to come from the curator.

### Seeding is far cheaper than classifying nodes

The KB uses **2,073 distinct GO BP terms** across 12,158 BP annotations, but the
head is short: the top 200 terms cover **55.6%** of all annotations and the top
500 cover **75.6%**. Add 398 MF, 476 CL, 542 UBERON, 338 CHEBI terms.

So the tractable job is *classify a few hundred ontology terms once and
propagate*, not *classify 12,290 nodes*. That also makes the seed auditable in
one file rather than spread across 2,000 YAML entries.

### The same signal is the debundling instrument

This is what the classification is *for*. Take the GO BP terms that are
scale-pure, and flag any node whose own class disagrees with its term's usual
class. **55 of the 333 labelled nodes carrying a confident GO term disagree —
17%**, and they read as genuine bundles:

- *SCN5A Sodium-Channel Loss of Function* [Atrial_Standstill] — curated
  MOLECULAR, annotated `GO:0061337 cardiac conduction` (usually TISSUE).
  Splits into the channel lesion and the conduction failure.
- *Loss of Cardiomyocyte KATP Conductance* — curated CELLULAR, annotated
  `potassium ion transmembrane transport` (usually MOLECULAR).
- *White-Matter Oxidative Stress* [Alexander_Disease] — curated TISSUE,
  annotated `response to oxidative stress` (usually CELLULAR).

A node needing two classes is a node making two claims. The value of the
classification is that it *names which two*, so the split is obvious rather than
a judgement call.

### One detector that does NOT work

"Node carries a molecular-tier term **and** a UBERON term" looks like a
cross-tier bundle detector. It fires on 368 nodes (3.0%) and is mostly wrong:
*"PRRX1/OTX2 Loss of Function in First-Arch Neural Crest"* and *"ANK2
Haploinsufficiency in Neurons"* are single molecular claims with a site
qualifier. **UBERON is usually doing location duty, not tier duty.** Rejected.

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
- **Debundling — the primary payoff.** Forcing one class per node surfaces
  nodes doing two jobs (~41% of the `biological_scale` survey's sample were
  split candidates), and the GO-disagreement detector above finds them
  mechanically rather than by eye. Bundling is a curation state, not a flaw in
  the classification: a node that resists a single class is the tool working.

## Open questions

- **8 tiers or 6?** Tiers 3/4 (molecular vs pathway) and 7/8 (systemic vs
  outcome) are the two joins most likely to be argued about. Cheap to test.
- **Does this replace `biological_scale` or sit beside it?** Tiers 3-7 are
  close to a refinement of MOLECULAR/CELLULAR/TISSUE/ORGANISM. Two slots saying
  nearly the same thing would be worse than either alone — most likely
  `node_class` supersedes `biological_scale` and the 3,704 existing values
  migrate mechanically.
- **Adoption.** `biological_scale` sits at 30.1% after being added. But the
  ontology-seeding result above changes the arithmetic: seed from the term
  vocabulary (a few hundred terms) rather than from the 30% of nodes already
  hand-tagged, and coverage is bounded by grounding coverage (69% carry a GO BP
  term) instead of by curator throughput.

## Next step

Started: [`docs/superpowers/pathograph_node_classes.txt`](../pathograph_node_classes.txt) — the tree as a plain text file, leaves being real `<node name> [Disease]`
pairs, representatives only. No schema, no enum, nothing in `kb/` depends on it.
Its `DOESN'T FIT` section is where the design is already failing and is the most
useful part to argue with.

Then, in order:

1. **Migrate `role` mechanically where it is derivable** — normalise casing
   (3 variants of `trigger` today), compute cascade position and C2 from the
   edges, and see how much of the 2,322 tagged nodes is left over. That number
   sizes the real curation job.
2. **Classify ~100 nodes against the 9+2 tree** to find the contested joins,
   reusing the three-pass structure from
   [the `biological_scale` survey](../../../projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md).

## Appendix — reproducing the numbers

All figures read `kb/disorders/*.yaml` and `kb/modules/*.yaml` via
`dismech.yaml_io.safe_load`. `role` values normalised with
`.strip().lower().replace(' ', '_')`. Degree and depth computed over
`downstream[].target` edges restricted to targets resolving to a
pathophysiology node in the same file; depth is longest path from a source,
iterated to fixpoint with a 12-round cap.
