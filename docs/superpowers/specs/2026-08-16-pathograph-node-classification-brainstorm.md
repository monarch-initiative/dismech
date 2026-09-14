---
title: A Simple Tree for Pathograph Node Classification
status: BRAINSTORM
description: >-
  Proposes a `node_class` vocabulary for pathophysiology nodes ordered as a
  causal cascade: genomic -> environmental -> molecular activity -> molecular
  substance -> pathway -> cellular -> tissue/organ -> systemic -> outcome, plus
  a DISPOSITION tier and cross-cutting classes (compensation, intervention
  point). Validated against every pathophysiology node in the KB; replaces the
  improvised 55-value free-text `role` vocabulary.
tags: [SCHEMA_EVOLUTION, PATHOGRAPH, PATHOPHYSIOLOGY, BRAINSTORM]
---

# A Simple Tree for Pathograph Node Classification

**Status: brainstorm.** One slot, one flat enum, values ordered as a cascade.

## The tree

The authoritative tree is
[`pathograph_node_classes.txt`](../pathograph_node_classes.txt), which carries
the glosses and ~1,600 worked `<node name> [Disease]` examples. Reproduced here
is only its top level, which is what the proposal actually is; do not treat this
copy as the tree, and regenerate it rather than editing it:

```bash
just node-classes --format summary
```

```
 1. GENOMIC EFFECT             genome instability; pathogenic sequence variant; dosage;
                               structural variant; epigenetic; transcript-level
 2. ENVIRONMENTAL EFFECT       infectious agent; chemical / drug / toxin; physical exposure;
                               hormonal / physiological exposure; physiological stressor;
                               microbiome state
 3. MOLECULAR ACTIVITY EFFECT  catalytic activity; channel conductance; transport activity;
                               receptor / adaptor activity; structural-protein activity
 4. MOLECULAR SUBSTANCE EFFECT metabolite accumulation; metabolite depletion;
                               protein misfolding / aggregation; protein abundance loss;
                               post-translational modification state
 5. PATHWAY EFFECT             signalling reduced / failed; signalling increased;
                               metabolic flux block
 6. CELLULAR EFFECT            cell death; differentiation / identity; metaplasia; haemolysis;
                               proliferation / expansion; senescence; cell activation;
                               organelle dysfunction; morphogenesis, migration and positioning;
                               protein trafficking and localization
 7. TISSUE / ORGAN EFFECT      inflammation; fibrosis / remodelling; pathological structure
                               formed; degeneration / atrophy; developmental malformation;
                               barrier failure; injury; circulatory disturbance; mechanical
                               obstruction and stenosis; abnormal communication; vascular
                               malformation; material deposition; ischemia and infarction;
                               inflammatory infiltration; functional disturbance; neoplastic
                               invasion and metastasis; pathogen spread and tissue invasion;
                               immune evasion and immunosuppressive microenvironment;
                               impaired repair; neural circuit and network dysfunction;
                               pathological angiogenesis; compression and mass effect
 8. SYSTEMIC EFFECT            metabolic crisis; organ failure; endocrine / homeostatic
                               derangement; systemic inflammatory state; haematological
                               deficit; autoimmune response; immune deficiency; behavioural
                               and cognitive mechanism; nutritional deficit
 9. OUTCOME                    clinical endpoint; progression and transformation

--- not cascade tiers; these cut across all of the above ---

10. DISPOSITION               genetic predisposition; trigger-specific susceptibility;
                              tissue vulnerability; outcome risk; penetrance and
                              expressivity modifier
11. ALSO CLASSES              COMPENSATION; INTERVENTION POINT
12. DEBUNDLE TARGETS          found by name; found by GO term; found by conflicting GO terms;
                              not a bundle, do not split
13. STILL UNPLACED            not an effect at all; normal biology, not pathology;
                              aetiology unresolved
```

The original sketch was 9 cascade tiers plus 2 cross-cutting classes. Tiers 10
and 12-13 were all forced by the corpus rather than designed: DISPOSITION was
promoted out of STILL UNPLACED once it held four distinct shapes, and DEBUNDLE
TARGETS is the payoff rather than a residue -- a node needing two classes is
making two claims.

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

## The GO seed table

[`pathograph_node_class_go_seed.tsv`](../pathograph_node_class_go_seed.tsv)
hand-classifies **640 GO BP terms** into the nine classes, with a `confidence`
column so genuinely ambiguous terms (`inflammatory response`, `nervous system
development`) are marked `LOW` and suggest rather than seed.

It was built in three tranches, and the third one is the interesting result.

| tranche | terms | how chosen |
|---|---:|---|
| 1 | 200 | most frequent GO BP terms in the KB |
| 2 | +300 | next most frequent (to rank 500) |
| 3 | +140 | **every GO BP term used in `kb/modules/` that the first two missed** |

### Coverage

Over all 12,290 pathophysiology nodes:

| | 200 terms | 500 terms | 640 terms |
|---|---:|---:|---:|
| single unambiguous class (seeded) | 34.5% | 43.6% | **45.0%** |
| conflicting classes (debundle candidate) | 3.6% | 5.8% | **6.2%** |
| combined, with the `MF or gene` rule | 49.8% | 58.7% | **60.1%** |

Class mix of the seeded nodes: CELLULAR 42%, TISSUE 18%, PATHWAY 11%,
SUBSTANCE 10%, GENOMIC 8%, SYSTEMIC 6%, ACTIVITY 5%.

**Diminishing returns are steep on frequency alone.** The first 200 terms
seeded ~21 nodes each; terms 201–500 seeded ~3.7 each. Chasing the frequency
tail further is not worth it — 1,184 GO BP terms are used twice or less and
together account for only 12.6% of all annotations.

### Frequency ranking has a systematic blind spot

Tranche 3 exists because of a wrong prediction. Four bacterial drug-mechanism
modules would not classify, and the earlier guess was that their GO terms fell
below the frequency cutoff. Two of the four terms they depend on were in fact
**already in the table, marked `LOW`** — a confidence gap, not a coverage gap.
The rest were genuinely absent, and inspecting them revealed the real pattern:
whole specialist vocabularies were missing — viral lifecycle (`virion assembly`,
`viral genome integration into host DNA`, `establishment of viral latency`),
meiosis, fungal and bacterial cell wall, cortical migration — because each term
is rare KB-wide while being *central to the module that uses it*.

Adding those 140 terms moves the needle barely at all corpus-wide (43.6% →
45.0%) and enormously where it matters:

| | all nodes | module nodes |
|---|---:|---:|
| seeded single class | 45.0% | **63.8%** |
| conflicts | 6.2% | 11.2% |
| combined with MF/gene rule | 60.1% | **76.4%** |

The lesson generalizes past this table: **frequency-ranked seeding
under-serves exactly the conserved-mechanism content the KB most wants
classified.** Any future extension should be target-driven, not rank-driven.

### Self-check against an independent label

Mapping each seed class onto the coarser `biological_scale` enum
(ACTIVITY/SUBSTANCE/GENOMIC → MOLECULAR, PATHWAY → no equivalent) and comparing
against the curator's own tag on the 1,252 nodes that carry both:
**65% agree.** That number held steady across all three tranches, which is at
least evidence the labelling is internally consistent rather than drifting.

It should not be read as 35% error. The largest disagreement classes are
CELLULAR-seed→TISSUE-curated (98) and CELLULAR-seed→MOLECULAR-curated (71) —
which is precisely the debundle signal: the GO term describes the *process*
while the curator tagged the *node's* substrate, and when those differ the node
is often carrying both. Separating "my label is wrong" from "the node is
bundled" needs manual review of a sample, and has not been done.

### The conflicts are a second debundling detector

762 nodes (6.2%) carry GO terms that span two classes. Unlike the earlier
detector this needs no curated class at all — a node whose *own* annotations
disagree is making two claims:

- *Impaired Oligodendrocyte Precursor Proliferation and …* — CELLULAR + TISSUE
- *Neutrophil Oxidative and Proteolytic Injury* [ARDS] — CELLULAR + SUBSTANCE
- *Cortical Excitation-Inhibition Imbalance* — CELLULAR + PATHWAY
- *Failure of Poly(ADP-Ribose) Turnover under Stress* — CELLULAR + GENOMIC

Note how many say "and" in the name.

## The classification now runs over the KB

`src/dismech/node_class_scan.py` applies the seed table plus a documented rule
cascade to every pathophysiology node, so the numbers above are reproducible
rather than reported:

```bash
just node-class-scan                        # coverage summary
just node-class-scan --format tsv           # per-node assignments
just node-class-scan --format debundle      # nodes whose own GO terms conflict
just node-class-scan --format conformance   # class check across conforms_to edges
```

Rules fire in order, and each carries its own confidence because they are not
equally trustworthy:

| # | rule | class | confidence | fires on |
|---|---|---|---|---:|
| 1 | one HIGH seeded GO BP class | that class | HIGH | 51.2% |
| 2 | >1 HIGH seeded GO BP class | `CONFLICT` | — | 6.2% |
| 3 | GO MF present | ACTIVITY | HIGH | 3.2% |
| 4 | CHEBI present | SUBSTANCE | MEDIUM | 1.8% |
| 5 | gene present | GENOMIC | **LOW** | 5.5% |
| 6 | UBERON without CL | TISSUE | **LOW** | 5.0% |
| 7 | CL present | CELLULAR | **LOW** | 16.5% |
| — | nothing | unclassified | — | 16.7% |

Rule 5 is deliberately LOW: a gene annotation does not distinguish a genomic
lesion from a broken molecular activity, and those are now different tiers.

**76.2% of the 13,821 nodes get a class, 6.0% are flagged as debundle
candidates, 17.8% stay unclassified.** Class mix: CELLULAR 45.7%, TISSUE 16.8%,
GENOMIC 12.2%, ACTIVITY 8.0%, SUBSTANCE 7.7%, PATHWAY 6.5%, SYSTEMIC 3.1%.

These move as the KB grows -- they were 77.1% of 12,290 nodes when first
measured. Read them as the shape of the result, not as constants, and re-run
`just node-class-scan` rather than quoting this paragraph.

### One tempting "fix" that makes things worse

Rule 1 outranks rule 3, so a node carrying both a seeded GO BP term and a GO MF
term is classified from the BP term. That looks like an ordering bug when you
see a case like `ACADSB molecular function deficiency`, which carries
`GO:0006550 L-isoleucine catabolic process` (seeded SUBSTANCE) alongside
`GO:0003995 acyl-CoA dehydrogenase activity` — and whose own name says it is an
activity claim. MF is also the better-measured signal in isolation (91%).

Promoting MF above BP was tried and is worse. 252 nodes carry both, and the swap
moves conformance agreement from **90.0% down to 87.3%**, because MF is often a
secondary annotation on a node that genuinely is about the process
(*Glycosaminoglycan-Assisted Fibril Nucleation and Extracellular Deposition*
carries an MF term and is not an activity node).

So the current order is empirically right and the individual case is still
wrong. Discriminating "this node is about the enzyme" from "this node is about
the pathway the enzyme sits in" needs more than which slots are populated, and
is unsolved. The limitation is recorded in the module docstring so the ordering
does not get "corrected" later.

### A second seed row that looks wrong and tests the same way

`GO:0006457 protein folding -> ACTIVITY HIGH` reads as a mistake: the tree files
`protein misfolding / aggregation` under MOLECULAR SUBSTANCE, and the 49 entries
carrying this term name nodes like *ADan Misfolding and Beta-Sheet
Oligomerization* and *Mutant Huntingtin Protein Aggregation* -- substance claims
by any reading.

Reseeding it to SUBSTANCE was tried. Conformance agreement gets **worse**, 9.3%
mismatch to 10.0%, and the debundle count does not move (823 either way). The
new disagreements are pairs where the module side becomes SUBSTANCE while the
disorder side stays CELLULAR or ACTIVITY from a different GO term -- so the
metric is penalising a change that makes one side of the pair more defensible
while the other side stays wrong.

That is the honest reading, and it is why the row is left alone rather than
"fixed": the conformance number is an **agreement** measure, not an accuracy
measure, and it cannot adjudicate a case where both sides may be wrong. Anyone
revisiting this row should change the CELLULAR-seeded aggregation terms in the
same pass, and expect the number to get worse before it gets better.

### Two gaps in the seed table worth knowing about

- **`OUTCOME` has no seed rows at all**, so rule 1 can never assign it. That is
  a consequence of note 3e in the tree file -- patient-level outcomes are
  curated in `phenotypes:`, not `pathophysiology:` -- but it is invisible from
  the rule table, which reads as though every class is reachable. `ENVIRONMENTAL`
  and `DISPOSITION` are unseeded for the same reason.
- **`MEDIUM` never appears in the seed table** (574 HIGH, 66 LOW), even though
  the CHEBI rule emits it. The three-level confidence scale is really two levels
  in the seeded path, and the gate that matters is HIGH vs not-HIGH.

## Conformance edges are an independent check on the classes

This is the test the earlier module section predicted, and it is worth more
than the coverage number. A `conforms_to` edge asserts that a disorder node and
a module node are the same *kind* of thing — curated by a process with no
knowledge of this classification. So the agreement rate is evidence about the
classes, not a restatement of them.

Over 871 conformance pairs where both sides classify at HIGH confidence:
**they agree 90.7% of the time.** For a nine-class scheme applied by an
independent route, that is a real result.

**But the gate matters, and this is the finding:**

| pairs | mismatch |
|---|---:|
| both sides HIGH (seeded GO BP or GO MF) | **9.3%** (81/871) |
| both sides from seeded GO BP alone | 7.5% (62/832) |
| either side from a LOW fallback rule | **40.4%** (112/277) |
| all pairs | 16.8% (193/1148) |

Regenerate the whole table rather than quoting it — it moves as the KB grows,
and every row is derived from the pair list `--format conformance` prints:

```bash
just node-class-scan --format conformance-gates
```

The gene/CL/UBERON fallbacks more than quadruple the disagreement rate. They are
useful for coverage and useless for adjudication, so `--format conformance`
gates on both-sides-HIGH by default and `--include-low` opts back in.

Per-module agreement varies in an interpretable way:
`complex_iv_assembly_deficiency` 37/37, `amyloidogenesis` 22/25,
`epilepsy_excitation_inhibition_imbalance` 84/117, and
`metabolic_intoxication_decompensation` 14/30 — the worst, and plausibly a real
finding about that module rather than about the classifier, since its conformers
substitute enzyme-level lesions under substance- and systemic-level module
nodes.

**What a mismatch means is not yet settled.** Two readings compete and the data
does not separate them: either the mapping is wrong, or a conforming node is
legitimately allowed to sit one tier off its module target because the disorder
substitutes a disease-specific *cause* for a generic *state*. *Reduced FGF14
Expression in Cerebellar Neurons* conforming to `cerebellar_purkinje_degeneration#Cerebellar Neuron Insult`
(GENOMIC vs CELLULAR) reads as the second. Resolving this needs a curator to
review a sample; until then the check is a worklist, not a verdict.

## Rules should target leaves, not tiers — and `modifier` is the missing axis

The scanner assigns a **tier** (CELLULAR, TISSUE, …). That is the wrong target
for rule-writing, for a simple reason: once nodes are classified manually
against the taxonomy, the tier falls out of the leaf for free. A node assigned
`CELLULAR > cell death` has already said it is CELLULAR. Rules that predict only
the tier are redundant with the manual pass they are meant to bootstrap.

What survives the redirect, and what does not:

| | status |
|---|---|
| tier prediction | superseded by manual leaf assignment |
| `CONFLICT` / debundle detection | **survives** — it needs terms to *disagree*, not to be right |
| conformance class check | **survives** — same reason |
| the confidence gate | **survives** — it is what made the conformance number honest |

### Leaves come in two shapes, and only one is in the seed table

Looking at the taxonomy's actual leaves, they split cleanly:

**Intrinsic leaves** — the GO term alone names the leaf. `GO:0006915 apoptotic
process` → `CELLULAR > cell death`; `GO:0090398 cellular senescence` →
`CELLULAR > senescence`; `GO:0030198 extracellular matrix organization` →
`TISSUE > fibrosis / remodelling`; `GO:0071805 potassium ion transmembrane
transport` → `ACTIVITY > channel conductance`. These need nothing more than a
`leaf` column added to the existing seed table.

**Polar leaves** — the GO term names a *family* and the leaf depends on
direction. `GO:0016055 Wnt signaling pathway` is `PATHWAY > signalling
increased` or `PATHWAY > signalling reduced` depending on which way it runs; a
metabolic process term is `SUBSTANCE > accumulation` or `SUBSTANCE > depletion`.
**The GO term cannot resolve these and the seed table structurally cannot
either.**

### The polarity is already curated, and the scanner ignores it

`Descriptor.modifier` carries it, and coverage is much better than expected:

| slot | descriptors carrying a modifier |
|---|---:|
| `biological_processes` | 9,682 / 12,166 (**79.6%**) |
| `chemical_entities` | 678 / 813 (83.4%) |
| `molecular_functions` | 599 / 727 (82.4%) |
| `cell_types` | 66 / 8,343 (0.8%) |
| `locations` | 14 / 3,509 (0.4%) |

Values on GO BP: INCREASED 3,441, DECREASED 3,163, ABNORMAL 2,342,
DYSREGULATED 713.

Tested against an independent signal — the polarity word in the node's own name
— `modifier` resolves the polar leaves well: **81% agreement on SUBSTANCE**
(accumulation vs depletion, n=176) and **88% on PATHWAY** (increased vs reduced,
n=309). Several disagreements are the name-regex misfiring rather than the
modifier being wrong (*"Impaired Surfactant Catabolism and Macrophage
Cholesterol Overload"* is an accumulation node whose name contains "Impaired"),
so those are floors.

So the leaf rule has the shape **GO term (which family) × modifier (which
direction)**, and the current scanner uses only the first half. The
`ABNORMAL`/`DYSREGULATED` third of the modifiers names no direction and leaves
those nodes at family level — which is the honest answer for them.

The CL and UBERON slots carry essentially no modifiers, so leaves under CELLULAR
and TISSUE must come from intrinsic GO terms; the LOW-confidence CL/UBERON
fallbacks cannot reach leaf granularity at all.

### Why this is not being implemented yet

Hand-assigning leaves to 640 GO terms is a large, hard-to-revise commitment, and
**the leaf vocabulary is still moving** — the last expansion of the
representatives file added five subclasses (physical exposure,
structural-protein activity, migration/positioning, barrier failure, exhausted
compensation) that a 108-example sample had hidden. Freezing leaves into the
seed table before the leaf set stabilises would bake in a vocabulary that is
still being discovered. Stabilise the leaves against more worked examples first,
then add the `leaf` column and the modifier axis together.

## How this ties in with module classification

Modules (`kb/modules/`) validate against the same `Disease` class, so their
pathophysiology nodes get node classes exactly like disorder nodes do. The open
question is whether a *module* then gets a class, and whether it is derived.

Three options were on the table: (1) module class is entirely a function of the
nodes it contains, (2) something bespoke, (3) neither. **The corpus says (3):
two orthogonal things, one bespoke and one derived.**

### Deriving it from nodes does not work

Profiling all 123 modules (580 nodes, 71% classifiable — better grounded than
disorder nodes at ~50%) and reducing each to an *entry→exit* signature, using
the informal groups CLAUDE.md already names:

| group | modules | distinct signatures |
|---|---:|---:|
| treatment toxicity | 4 | **1** |
| Xogenesis | 5 | 3 |
| disease-like phenotype | 10 | 4 |
| drug mechanism | 8 | 4 |
| hallmark of cancer | 10 | **7** |

The failure is a collision, not a precision problem. `CELLULAR→CELLULAR` is the
signature of **all four** toxicity modules, **seven of ten** disease-like
phenotype modules, two of the five Xogenesis modules, and three hallmark
modules. One signature spans four curator-authored groups. In the other
direction, "hallmark of cancer" has seven signatures across ten modules — the
group is internally heterogeneous by shape.

That is the expected result on reflection: the existing groups encode **why the
module exists in the KB** — is this a cancer hallmark, a drug-toxicity pattern,
a drug-mechanism target pattern, a phenotype final-common-pathway, a
structure-formation pattern — and that is a curation-provenance fact, not a
property of the node cascade.

### But the derived shape is not noise either

It separates things the bespoke groups do not:

- **Drug-mechanism modules are ACTIVITY-anchored** (`viral_protease_inhibition`,
  `bacterial_protein_synthesis_inhibition`, `fungal_cell_wall_…`). That is
  exactly right — the drug target *is* a molecular activity, which is the tier
  added in the previous section.
- **Xogenesis splits cleanly by what gets built**: `amyloidogenesis` is
  ACTIVITY→SUBSTANCE (a deposit), while `thrombogenesis` and `atherogenesis` are
  CELLULAR→TISSUE (a cellular structure). That distinction is real and is not
  currently recorded anywhere.
- `genome_instability_mutation` is the only GENOMIC→GENOMIC hallmark, and
  `deregulated_cellular_energetics` the only SUBSTANCE one — both correct.

### So: two slots, and the derived one audits the bespoke one

Same relationship node class already has with ontology grounding — evidence
*for* a curated claim, not a parallel axis:

| | what it is | who sets it |
|---|---|---|
| **module kind** | hallmark / toxicity / drug-mechanism / disease-like phenotype / Xogenesis / serial-homology / … | curator (already exists, in CLAUDE.md prose, with no slot) |
| **module shape** | entry→exit signature over node classes, plus the class histogram | computed |

The bespoke half is not new work — it is formalizing a taxonomy that already
exists as prose. The derived half becomes a consistency check: a module filed as
a drug-mechanism pattern whose nodes are not ACTIVITY-anchored is worth a look,
as is a new Xogenesis module that ends CELLULAR rather than TISSUE or SUBSTANCE.

### The one place node class serves modules directly

Every module has a **key conformance target** — the node other entries point at
with `conforms_to`. That is a node, so it carries a node class, and that gives
the conformance check real teeth: **a disorder node conforming to a module node
of a different class is a probable mis-mapping.** This is the sharpest concrete
use of node classification found so far, and it needs no module-level slot at
all.

### Caveat on these numbers

Module signatures rest on few nodes (most modules have 2–6), so an individual
signature is fragile; the collision result is robust because it is about
overlap, not precision. And four drug-mechanism modules came back unclassifiable
— not because their nodes lack grounding (all five nodes of
`bacterial_cell_wall_synthesis_inhibition` carry GO BP terms) but because
bacterial GO terms fall outside the top-200 seed table. That is a seed-coverage
gap, and an argument for extending the table to 500 terms before leaning on
module shape.

## Comparison with MPATH and NCI Thesaurus

Both are prior art for "kinds of pathology" and both were checked against the
tree (via OLS, 2026-08).

### MPATH — a process/structure mirror over lesion type

```
MPATH:0 pathological entity
├── MPATH:596 pathological process          ├── MPATH:603 pathological anatomical entity
│   ├── 597 cell and tissue damage process  │   ├── 1   cell and tissue damage
│   ├── 188 immunopathological process      │   ├── 105 circulatory disorder
│   ├── 604 defective growth/differentiation│   ├── 126 growth and differentiation defect
│   ├── 606 neoplasia                       │   ├── 218 neoplasm
│   ├── 599 developmental abnormalities     │   ├── 55  developmental/structural abnormality
│   └── 175 healing and repair process      │   └── 607 healing and repair structure
```

Two structural facts. MPATH's **primary** split is occurrent vs continuant, and
then a near-perfect 6-way mirror across it. Its classifying axis is **lesion
type as a pathologist sees it** — damage, immune, growth, development,
neoplasia, repair.

**It is orthogonal to ours, not competing.** We classify by *position in the
causal chain*; MPATH classifies by *what kind of lesion resulted*. A single
dismech node has both properties.

Where they touch, our TISSUE leaves map onto MPATH cleanly: `injury` →
MPATH:597/1, `inflammatory infiltration` + `immune evasion` → MPATH:188,
`developmental malformation` → MPATH:599/55, `neoplastic invasion` →
MPATH:606/218, `impaired repair` → MPATH:175/607.

Two asymmetries matter:

- **MPATH stops at the cell.** It has no counterpart to our GENOMIC, ACTIVITY,
  SUBSTANCE or PATHWAY tiers — the entire upper half of our cascade. That is the
  part of dismech's pathograph MPATH cannot express, and it is most of what
  makes a mechanism graph a mechanism graph rather than a lesion list.
- **We have no systematic process/structure mirror.** The Xogenesis convention
  already borrowed the idea for five modules, but the taxonomy at large has one
  `pathological structure formed` leaf rather than a pairing rule. Worth
  deciding deliberately rather than by omission.

### MPATH found a real gap: circulatory disorder

MPATH gives `circulatory disorder` **top-level** billing. We had scattered it —
thrombus under `structure formed`, ischemia in its own leaf — and had no home at
all for roughly **70 haemorrhage, oedema/effusion and dilatation/ectasia nodes**.
`TISSUE > circulatory disturbance` was added as a direct result.

### NCIT:C16956 Pathologic Process — a flat term list, not a taxonomy

41 direct children, no intermediate structure, and radically mixed granularity:
`Pathogenesis` (the entire concept of disease mechanism) sits as a sibling of
`Karyomegaly` (a nucleus is enlarged). It also mixes kinds freely — processes
(`Amyloidogenesis`, `Necrotic Process`), states (`Impaired Cytoskeletal
Integrity`), relations (`Host-Parasite Relationship`), outcomes (`Disease
Progression`), and even a therapeutic effect (`Graft-Versus-Tumor Induction`).

So NCIT offers **no structural competition** — there is nothing here to adopt as
an organising axis. What it does offer is **leaf-level grounding**: a
ready-made, coded term for many of our leaves — `Amyloidogenesis` C44955,
`Neovascularization` C16900, `Invasion` C75004, `Intravasation` C48197 /
`Extravasation` C48198, `Degeneration` C61557, `Necrotic Process` C16897,
`Cell Stress Process` C21065, `Mitochondrial Damage` C45524, `Lithiasis` C97086,
`Ectasia` C120877, `Fibroplasia` C120881, `Microgliosis` C120898.

That is the practical use: if leaves ever need CURIEs, NCIT supplies many of
them without inventing anything.

Checked against the KB, NCIT's classic gross-pathology terms are mostly *not*
worth leaves for us — `Ulceration` matches 2 nodes, `Hyalinization` 1. Their
absence from our tree is correct, not an oversight.

### What neither has

- **Causal ordering.** Neither encodes upstream/downstream at all.
- **DISPOSITION.** NCIT's `Permissiveness` (C19311) is the nearest thing and is
  about infection susceptibility only; MPATH has nothing. Our four disposition
  shapes have no prior art here.
- **COMPENSATION.** Neither ontology has any notion of the body pushing back.
  This is arguably the most distinctive class in the tree and the one with the
  least external support — which cuts both ways.
- **INTERVENTION POINT.** Neither, unsurprisingly, since neither is modelling
  drug action.

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
Its `STILL UNPLACED` section is where the design is already failing and is the
most useful part to argue with.

Then, in order:

1. **Migrate `role` mechanically where it is derivable** — normalise casing
   (3 variants of `trigger` today), compute cascade position and C2 from the
   edges, and see how much of the 2,322 tagged nodes is left over. That number
   sizes the real curation job.
2. ~~Classify ~100 nodes against the 9+2 tree~~ — **done, and then some.** The
   tree now carries ~1,600 worked examples across ~1,275 entries, placed in five
   random draws plus a sweep of MPATH/MeSH/SNOMED/NCIT. The build notes at the
   foot of the tree file record what each draw forced, including the leaves that
   reversed earlier decisions.

## Appendix — reproducing the numbers

All figures read `kb/disorders/*.yaml` and `kb/modules/*.yaml` via
`dismech.yaml_io.safe_load`. `role` values normalised with
`.strip().lower().replace(' ', '_')`. Degree and depth computed over
`downstream[].target` edges restricted to targets resolving to a
pathophysiology node in the same file; depth is longest path from a source,
iterated to fixpoint with a 12-round cap.
