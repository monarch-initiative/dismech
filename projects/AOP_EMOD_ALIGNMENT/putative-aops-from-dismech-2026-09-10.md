# Two putative AOPs derived from dismech pathographs

**Date:** 2026-09-10
**Entries:** [`Left_Ventricular_Noncompaction_8`](../../kb/disorders/Left_Ventricular_Noncompaction_8.yaml) (MONDO:0014152), [`Skeletal_Fluorosis`](../../kb/disorders/Skeletal_Fluorosis.yaml) (MONDO:0400003)
**Selection:** [`docs/reports/aop-derivable-measurable-chains-2026-09-10.md`](../../docs/reports/aop-derivable-measurable-chains-2026-09-10.md)
**AOP-Wiki snapshot:** 2026-09-03 bulk XML export (1,598 Events, 2,369 KERs)
**Illustrated summary:** [Pathographs to Pathways](https://claude.ai/code/artifact/7325e46d-c794-4ac4-a9a7-3cd077f4f784) — a web page carrying the two
chain diagrams, which this file does not reproduce. It was written by hand rather than
generated from this document, and nothing keeps the two in sync. This file holds the
detail — the full Event and KER tables — and is the authority where they disagree.

## What this is

Two **derivation exercises**: dismech pathographs re-expressed in AOP-Wiki v2.8
vocabulary, to see what a dismech-derived AOP contains and where it comes up empty. The
second entry was chosen specifically to test whether the first entry's results were
properties of dismech or properties of that entry's curation. Three of five were the
latter.

Working material for the AOP EMOD alignment project. **Not** a schema proposal — no
`aop*:` CURIE is written into `kb/`, and whether a pathophysiology node should carry a
Key Event cross-reference is
[open schema question 1](../AOP_EMOD_ALIGNMENT.md#1-should-a-pathophysiology-node-be-able-to-carry-a-key-event-cross-reference)
on the project page. **Not** an AOP-Wiki submission; Event and KER numbering below is
local to this document.

Both are **putative** on the Villeneuve et al. 2014 scale
([PMID:25466378](https://pubmed.ncbi.nlm.nih.gov/25466378/), Table 3) — hypothesized sets
of KEs and KERs supported by biological plausibility and empirical evidence, with no
weight-of-evidence evaluation and no quantitative understanding on any relationship.

---

## Derivation A — `Left_Ventricular_Noncompaction_8`

Selected as the only entry in the KB whose 5-node chain carries two or more independent
models on every node. Nine linked models: 2 NAM, 7 animal.

### Events

| # | Event | LoBO | How measured (from readouts) | AOP-Wiki counterpart |
|---|---|---|---|---|
| A1 | PRDM16 loss of function | Molecular | *(no readout)* | none |
| A2 | Loss of compact myocardium transcriptional identity | Cellular | scRNA-seq with spatial transcriptomics of LV compact myocardium, scored compact vs trabecular (`ALTERED`) | **none** — proposed |
| A3 | Increased TGF-beta signalling in cardiomyocytes | Molecular | ChIP-PCR of PRDM16 occupancy at the *Tgfb3* promoter with H3K4me1/me3 state (`INCREASED`); ligand transcripts and phospho-Smad2 (`INCREASED`); myocardial TGF-beta expression (`DECREASED`, conflicting) | **KE 1271** *Increase, TGF-beta signaling* (Molecular; 7 AOPs) |
| A4 | Decreased cardiomyocyte proliferation | Cellular | Proliferative and apoptotic indices in genotype-matched hiPSC-CMs (`DECREASED`) | **none** — all 31 proliferation KEs are increases, none cardiac |
| A5 | Failed ventricular compaction | Tissue | *(no readout)* | **none** — no `compaction` Event exists |
| A6 | Decreased left ventricular function with dilation | Organ | Chamber dimensions, systolic performance, sex-stratified contractile dysfunction (all `DECREASED`) | **KE 2215** *Decrease Left Ventricular function* (Organ; 2 AOPs) |
| A7 | Occurrence of cardiac arrhythmia *(AO)* | Organ | Postnatal electrophysiology (`ALTERED`); QRS and QTc (`INCREASED`); ion-channel transcripts (`ALTERED`) | **KE 1106** *Occurrence, cardiac arrhythmia* (Organ; 8 AOPs) |

Three reused, three proposed. `Congestive Heart Failure` sits downstream of A6 and would
map to **KE 1535** *Heart failure*, but no model links to it, so it is not measurable in
this entry and is left out.

### The finding: no MIE, and none obtainable

An MIE is a molecular interaction between a **stressor** and a biomolecule. A1 is a
germline heterozygous `PRDM16` loss-of-function lesion — molecular in scale, genuinely
the head of the chain, and not an interaction with anything. No stressor, no dose, no
exposure.

This is a limitation of the selection: the census ranked on measurability, model
multiplicity and AOP-Wiki novelty, and never asked whether a chain has a chemical entry
point. A monogenic disease does not have one.

What survives is the **network** use. Villeneuve's founding principles make Events the
reusable unit and networks of shared Events the functional unit of prediction, so an AOP
with no MIE of its own still contributes Events a chemically initiated AOP can converge
onto — and KE 1271 is already carried by seven.

### KERs

| # | KER | Empirical support | Evidence type |
|---|---|---|---|
| A-KER1 | A1 → A2 | [PMID:34915728](https://pubmed.ncbi.nlm.nih.gov/34915728/) — *Prdm16cKO* LV compact cardiomyocytes shift to a trabecular-like signature | Model organism |
| A-KER2 | A2 → A3 | [PMID:38113297](https://pubmed.ncbi.nlm.nih.gov/38113297/) — PRDM16 binds the *TGFB3* promoter and represses transcription | In vitro |
| A-KER3 | A3 → A4 | [PMID:27642787](https://pubmed.ncbi.nlm.nih.gov/27642787/) — "LVNC iPSC-CMs have decreased proliferative capacity due to abnormal activation of TGF-β signalling" | In vitro, human |
| A-KER4 | A4 → A5 | [PMID:38113297](https://pubmed.ncbi.nlm.nih.gov/38113297/) — homozygous *Prdm16Q187X* mice show an underdeveloped compact myocardium | Model organism, `INDIRECT` |
| A-KER5 | A5 → A6 | [PMID:34915728](https://pubmed.ncbi.nlm.nih.gov/34915728/) — cardiomyocyte-specific ablation causes LV-specific dilation and dysfunction with biventricular noncompaction | Model organism, `INDIRECT` |
| A-KER6 | A6 → A7 | [PMID:25443708](https://pubmed.ncbi.nlm.nih.gov/25443708/), [PMID:31959004](https://pubmed.ncbi.nlm.nih.gov/31959004/) — tachyarrhythmias in up to 47% of symptomatic patients; ejection fraction, not trabeculation extent, drives incidence | Human clinical, `INDIRECT` |

**A-KER2 carries a real `uncertainties-or-inconsistencies` payload**, from the entry's
existing `gap_lvnc8_tgfbeta_direction_conflict` discussion (`kind: HUMAN_MODEL_MISMATCH`).
Three systems disagree on the **direction** of A3:

| System | Direction | Curated link |
|---|---|---|
| Cardiac-specific *Prdm16* conditional knockout mouse | transcripts and phospho-Smad2 **up** | `RECAPITULATES`, `MODERATE` |
| *Prdm16Q187X* heterozygous knock-in — genotype-matched | expression **down** with age | `FAILS_TO_RECAPITULATE`, `LOW` |
| Proband hiPSC-cardiomyocytes | activation | `RECAPITULATES`, `HIGH` |

Reusing **KE 1271**, whose title asserts an *increase*, is therefore provisional: the
genotype-matched mammalian model moves the other way.

---

## Derivation B — `Skeletal_Fluorosis`

Selected as the chemically initiated counterpart: a real environmental exposure, four
linked animal models, no NAM, no computational model. State as submitted in PR
[#11617](https://github.com/monarch-initiative/dismech/pull/11617).

**This was first derived along the wrong chain.** The census picked the entry's
*measurable* spine — fluorapatite substitution → impaired collagen → turnover → mixed
lesion — and that spine has 2 of 5 relationships supported. The entry's *evidenced*
backbone is a different, longer path through the gut-microbiome arm, and it is the one a
putative AOP should be built on. See
[Why the first derivation of B was wrong](#why-the-first-derivation-of-b-was-wrong).

### Events

All eight relationships below carry validated-quote evidence. `LoBO` is read off
`biological_scale`; *measured* marks the Events with a `readouts` entry.

| # | Event | LoBO | Measured | AOP-Wiki counterpart |
|---|---|---|---|---|
| B0 | Chronic excess fluoride intake | Organism | no | **toxicokinetic** — outside an AOP by design |
| B1 | Gut microbial tryptophan metabolism disruption | Organism | no (model linked, no readout) | **KE 1954** *Gut microbiota, alteration* (Organ; 1 AOP) |
| B2 | AhR under-activation with Wnt hyperactivation | Molecular | **yes** — Wnt/β-catenin signalling and bone damage after 3-IAA restoration (`RESTORED`) | **KE 18** *Activation, AhR* (Molecular; **22 AOPs**) — polarity inverted, see below; plus **KE 1755** *beta-catenin activation* (Cellular) |
| B3 | Osteoblast proliferation and activation | Cellular | no | **KE 2089** *Altered Bone Cell Homeostasis* (Cellular; 2 AOPs) |
| B4 | Accelerated and disordered bone turnover | Tissue | **yes** — turnover, mineral content and biomechanics (`INCREASED`); trabecular separation and porosity (`INCREASED`) | **KE 2090** *Increase, Bone Remodeling* (Tissue) |
| B5 | Mixed osteosclerosis, osteomalacia and osteoporosis | Tissue | **yes** — DEXA density (`UNCHANGED`); mechanical quality (`DECREASED`) | **KE 2091** *Occurrence, Bone Loss* (Organ) — partial |
| B6 | Ligament and interosseous membrane ossification | Tissue | no | **none** |
| B7 | Spinal canal and foraminal narrowing | Tissue | no | **none** — no spinal or compression Event exists in the export |
| B8 | Compressive myelopathy and radiculopathy *(AO)* | Organism | no | **none** |

Three of nine Events instrumented, five with an AOP-Wiki counterpart, and a terminal
three-Event mechanical/neurological arm with no counterpart at all. That arm is the
clearest novel contribution in either derivation: AOP-Wiki has no Event matching
`spinal`, `myelopath`, `radiculopath` or `compress` anywhere in 1,598 records.

### KERs

| # | KER | Support | Grading |
|---|---|---|---|
| B-KER1 | B0 → B1 | [PMID:41380608](https://pubmed.ncbi.nlm.nih.gov/41380608/) — fluoride disrupted gut microbial tryptophan metabolism, lowering serum 3-IAA in model rats and human patients | `DIRECT` |
| B-KER2 | B1 → B2 | [PMID:41380608](https://pubmed.ncbi.nlm.nih.gov/41380608/) — the 3-IAA deficiency impaired AHR activation, leading to Wnt/β-catenin hyperactivation | `DIRECT` |
| B-KER3 | B2 → B3 | [PMID:24300170](https://pubmed.ncbi.nlm.nih.gov/24300170/) — the osteoblastic response is abolished by the Wnt blocker DKK-1; [PMID:41380608](https://pubmed.ncbi.nlm.nih.gov/41380608/) | `DIRECT` ×2 |
| B-KER4 | B3 → B4 | [PMID:34769367](https://pubmed.ncbi.nlm.nih.gov/34769367/) — excessive osteoblast proliferation accelerating bone turnover | `DIRECT` |
| B-KER5 | B4 → B5 | [PMID:34769367](https://pubmed.ncbi.nlm.nih.gov/34769367/) — osteosclerosis from osteogenic activity, osteoporosis from resorption | `DIRECT` |
| B-KER6 | B5 → B6 | [PMID:30415519](https://pubmed.ncbi.nlm.nih.gov/30415519/) — osteosclerosis and ligamentous ossification in the same radiographic criteria | `INDIRECT` |
| B-KER7 | B6 → B7 | [PMID:2172892](https://pubmed.ncbi.nlm.nih.gov/2172892/) — sclerosis and osteophytosis reducing foraminal and canal diameter | `DIRECT` |
| B-KER8 | B7 → B8 | [PMID:2172892](https://pubmed.ncbi.nlm.nih.gov/2172892/) ×2 — the deficits as a consequence of the skeletal changes | `DIRECT` + `INDIRECT` |

Eight of eight supported, against six of six for derivation A and two of five for the
chain first derived here.

### The MIE is still two toxicokinetic hops away, and it moved

B0 is where all five `environmental:` entries land with `environmental_effect: TRIGGERS`
— fluoride-rich groundwater, brick tea, indoor coal combustion, occupational inhalation,
propellant inhalation. On this chain the first molecular Event is **B2**, still two hops
downstream, but the intervening node is now the gut arm rather than skeletal deposition.

**This reproduces the `Lead_Poisoning` result on a second entry and by two independent
routes.** The alignment page records it as a single-entry observation — ten of ten
`TRIGGERS` edges landing on `Lead absorption`, initiating-event-shaped nodes two hops
downstream. Here it is five of five, with the same two-hop offset along either the mineral
spine or the gut backbone. It is a pattern in how exposure is modelled, and neither the
edge type nor `biological_scale` marks the boundary.

The scale sequence still opens non-monotonically —
`ORGANISM → ORGANISM → MOLECULAR → CELLULAR → TISSUE → … → ORGANISM` — and it still
descends exactly across the toxicokinetic prefix. That signature survives the change of
chain, which strengthens it as a marker.

### KE 18 would invert the claim

**KE 18 *Activation, AhR* is carried by 22 AOPs** — the most reused Event either
derivation touches, and by a wide margin. B2 cannot use it as written. dismech asserts AhR
**under**-activation: the microbial metabolite is lost, so the receptor is *less* active,
and Wnt hyperactivates in consequence. Reusing an Event titled "Activation" would assert
the opposite of what the entry says.

This is exactly the gap EMOD's `phenotype` property is introduced to close. The alignment
page records it: paired with Experimental Effect, phenotype "separates a chemical that
induces an outcome from one that treats it — the difference between an Observation mapping
to a Seizure Event and one mapping to a Decreased Seizure Event." Here it would separate
AhR activation from AhR under-activation, and without it a correct Event reuse is not
expressible.

**B2 also bundles two claims at two levels.** AhR under-activation is molecular; Wnt
hyperactivation maps to KE 1755 *beta-catenin activation* at Cellular. The node carries a
single `biological_scale: MOLECULAR`, and CLAUDE.md reads a node that would naturally take
two values as a signal it should be split. The AOP mapping surfaces the same thing the
scale slot would have — which is how the `Liver_Cirrhosis` Kupffer-cell split was found
(#10314).

### The downstream half joins an endorsed AOP with a different stressor

**AOP 482, *Deposition of energy leading to occurrence of bone loss*** — OECD WPHA/WNT
Endorsed, 7 Events, 11 KERs, method text on all seven. Its MIE is ionizing radiation. B3,
B4 and B5 are its KE 2089 → KE 2090 → KE 2091 terminus. So a fluorosis derivation supplies
a **second, chemical entry into a radiation AOP's downstream Events**, and then continues
past them into three Events AOP-Wiki does not have.

Meanwhile **fluoride appears in none of AOP-Wiki's 756 stressor records and none of its
439 chemicals** — the one "fluoride" hit is CAS 96-64-0, soman, an organophosphate. The
Events exist; the stressor does not.

**The AO mapping is partial and the mismatch matters.** KE 2091 is *bone loss*. B5 is a
mixed lesion — osteosclerosis, osteomalacia and osteoporosis at once, with exostosis on
top — and the entry deliberately refuses to collapse it. Mapping it to "bone loss" would
discard what distinguishes fluorotic bone from radiation-induced bone loss: it is denser
and weaker at once. The inbred-strain model measures precisely that and is curated
`FAILS_TO_RECAPITULATE`, DEXA density `UNCHANGED` against mechanical quality `DECREASED`.

### Why the first derivation of B was wrong

The census ranked chains by whether every node carries a model readout, reasoning that an
AOP Event is defined partly by how it is measured. That is a fact about Events and says
nothing about KERs — and in this entry the two run opposite ways.

| Chain | Nodes measured | KERs supported |
|---|---|---|
| Measurable spine (fluorapatite → collagen → turnover → mixed lesion) | 4 of 4 | **2 of 5** |
| Evidenced backbone (B0–B8, through the gut arm) | **3 of 9** | 8 of 8 |

The measurable nodes are the ones models instrument — bone fluoride content, collagen
markers, turnover and porosity, density and mechanics. Models measure *states*. The
transitions between states are what a paper asserts in prose, and across the mineral
segment they mostly do not: two of the three empty links there touch the fluorapatite node,
one entering and one leaving, and the entry's own curator had already marked them
`INDIRECT_UNKNOWN_INTERMEDIATES`.

Re-running the census with both requirements settles which constraint actually binds, and
it is not the one this document originally claimed:

| Longest chain | Every node measured | Every edge cited | Both |
|---|---|---|---|
| ≥3 nodes | 97 | 1,041 | 38 |
| ≥4 nodes | 21 | 725 | 6 |
| ≥5 nodes | 5 | 434 | 1 |

Counted with `just aop-chain-census` on 2026-09-15; the figures move with every curation PR.
36,793 causal edges KB-wide, 15,722 carrying evidence (43%). Fully-cited chains reach **12
nodes** (`Familial_Hypercholesterolemia`, `Lupus_Nephritis`,
`Autosomal_Dominant_Hypercholesterolemia_3`); fully-measured ones stop at 5. **Edge evidence
is about thirty-five times more available than node measurability**, so the scarce input to
an AOP derivation is `modeled_mechanisms` coverage, not literature.

`Left_Ventricular_Noncompaction_8` is the only entry in the knowledge base clearing both
requirements at five nodes, so derivation A survives the tightened screen — by luck rather
than by the reasoning that selected it.

## What the pair settles

The five verdicts drawn from LVNC8 alone, retested against fluorosis.

| Verdict from A | Holds? | What B showed |
|---|---|---|
| The Event layer transfers almost for free | **yes** | LoBO from `biological_scale`, measurement from `readouts`, terms from the CL/GO/UBERON bindings, in both entries |
| The relationship layer transfers with its evidence attached | **yes, and it is the abundant half** | A: 14/14 edges evidenced. B: 2/20 before PR #11617, 16/20 after, with 7 of 8 direct quotes coming from papers already in `references_cache/` and merely attached to the wrong object. KB-wide, 725 entries carry a 4-node fully-cited chain against 21 with a fully-measured one. The transfer is real; what is scarce is the readouts, not the citations |
| The initiating end does not transfer | **entry-dependent** | A has no MIE and can have none. B has two MIE candidates. What both share is that the exposure edges land on toxicokinetic nodes, so the MIE is never where an AOP would look for it |
| Model disagreement is an asset | **yes, differently** | A: three systems disagreeing on TGF-beta direction. B: a `FAILS_TO_RECAPITULATE` split between an `UNCHANGED` density readout and a `DECREASED` quality readout, which is the mixed-lesion claim in measurement form |
| Nothing needed a schema change | **yes** | Still true. `Pathophysiology.assays` remains the one slot that would most improve the output and remains unused in both |

One result reverses outright. On the method axis the alignment page records harvestable
free text on the AOP side and an empty slot on dismech's; A inverted that, because
`measured_or_detected` is empty on all four cardiac Events it reuses while dismech had an
instrumented readout for five of seven. **B inverts it back**: all seven Events of AOP 482
carry method text, and every readout `description` in `Skeletal_Fluorosis` is empty. The
corpus-wide figure is 601 of 1,598 Events (38%), so neither entry is representative —
which is the point. Method coverage is per-Event on one side and per-curator on the other.

One further correction the pair forces: **the census screen was measuring the wrong
thing, and in the opposite direction from the one first supposed.** It ranked chains by
whether every node carries a readout — a fact about Events that says nothing about KERs.
Adding the edge requirement turns 97 candidate entries into 38 at three nodes and 21 into
6 at four, and leaves exactly one at five. But the reason is not that edge evidence is
scarce. It is about 35× more available than node measurability. **The binding constraint on
deriving an AOP from any one dismech entry is `modeled_mechanisms` coverage.** A curation push that
linked models to more nodes and readouts to more links would move this number; more
literature work would not.

**Two derivations are enough to separate the framework from the file, and not enough to
generalize.** Every verdict above that changed, changed because the second entry was
curated by different hands to different conventions. A third would most usefully be an
entry with computational models linked, since neither of these has one and
`ModelMechanismLink.divergences` — the typed caveat vocabulary — is populated on
computational models only. The 38 entries clearing the joint screen at three nodes are the
place to look for it — `just aop-chain-census --list-joint 3`.
