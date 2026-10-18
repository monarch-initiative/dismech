# OpenScientist review: canonical MECP2 loss model for Rett syndrome

Assessor: claude-opus-5. Report: `../openscientist.md` (671 lines, 55 citations,
run 2026-05-23). Verdict: **SUPPORTED**.

## What I checked

I fetched 25 of the 55 cited identifiers into `references_cache/` and compared
every quotation the report acts on against the cached source. That included the
five 2026 identifiers whose high numbers made them the obvious fabrication
candidates — PMID:41182667, PMID:41296873, PMID:41455590, PMID:41975033,
PMID:42159339. All five are real, all five are on the stated topic, and the
sentences the report quotes from them are verbatim.

That is worth saying plainly because it is not what this sweep usually finds.
Across 25 spot-checked citations there was no fabricated identifier, no
wrong-paper attribution, and no invented quotation.

## What the report actually contributes

The central thesis came from the KB, so re-deriving it earns no credit. The
value is in the four things it found that the curated entry did not have.

**Human evidence for the E/I shift.** The curated hypothesis description
asserted excitatory/inhibitory imbalance. The entry had no node for it and no
human evidence. PMID:32129908 is paired-pulse TMS in 14 typical Rett patients:
excitation index up (p = 0.003), short- and long-interval intracortical
inhibition both reduced, LTP-like plasticity in M1 abolished (p = 0.008) and
scaling with motor disability. This is in vivo human neurophysiology, not a
mouse inference, and it was the single biggest gap in the pathograph.

**Reversibility.** The hypothesis description names adult Mecp2 reactivation as
one of three pillars of the model and cited nothing for it. PMID:24009314 is
that experiment.

**Non-cell-autonomous glia.** The pathograph was strictly neuron-intrinsic.
PMID:20392956 shows Mecp2-null microglia releasing fivefold more glutamate and
damaging dendrites and postsynaptic components in 24 hours, with causality
established four different ways. PMID:24285883 shows that restoring MeCP2 to
oligodendrocyte lineage cells alone — every neuron still mutant — improves
locomotion and clasping.

**A specific site for the respiratory lesion.** The brainstem node cited a review
naming "ventrolateral medulla and pons". PMID:26507912 localises it to the
Kölliker-Fuse area, names GABA as the transmitter, and closes the loop in both
directions: boosting GABA there reduces irregularity in mutant mice, blocking
GABA-A receptors there reproduces the phenotype in healthy rats.

## Where the report overstates

Three places, all recorded as `QUALIFIED` in the sidecar.

It calls PMID:30929312 evidence from "large-scale studies" and grades it "Human
clinical" in the evidence matrix. It is a narrative review.

It reports both LAVENDER communication endpoints as statistically significant.
The source calls the RTT-COMC result nominally significant, and PMID:38232652 is
a secondary endpoint analysis, not the trial's primary report — which is already
curated here as PMID:37291210.

Its bidirectional-dosage citation, PMID:39838601, compared 11 MECP2-duplication
individuals against 6 *male RTT-like* individuals. That is not classic female
Rett, and the conversion-risk sentence the report leans on is the paper's stated
rationale rather than one of its results.

Separately, several of the report's proposed curation snippets are unusable as
written. The one offered for the Super Elongation Complex finding is
`"Loss-of-function mutations in methyl-CpG binding protein 2 (..."` — a truncated
title fragment ending mid-parenthesis, stating no finding. Every snippet I
curated was re-derived from the cached abstract. The same finding is also
double-counted: PMID:39005382 and PMID:41296873, offered as "Sonn et al.
(2024/2025)", are the bioRxiv preprint and the published version of one study.
Only the published version is cited in the entry.

## Provenance

No artifact bundle is committed. The directory holds `openscientist.md` and its
citations sidecar and nothing else, so the four embedded figure placeholders
(`final_synthesis.png`, `evidence_matrix.png`, `evidence_landscape.png`,
`knowledge_gaps_table.png`) resolve to nothing and render as literal template
syntax. The "5 iterations, 136 papers, 21 findings confirmed" counts cannot be
audited.

The template asked explicitly for source-level absences — "no relevant GenCC,
ClinGen, trial, omics, or cohort evidence found as of the search date". The run
checked none of them. All eight of its knowledge gaps are literature-derived.

## Integration into the disease YAML

Target: `kb/disorders/Rett_Syndrome.yaml`.

**Added to `mechanistic_hypotheses`** (the existing CANONICAL entry, whose
`notes` already summarised this report):
- PMID:24009314, `SUPPORT` / `MODEL_ORGANISM` — adult reactivation rescues
  established deficits.
- PMID:25870282, `SUPPORT` / `MODEL_ORGANISM` — mCH accumulates postnatally and
  the genes acquiring it are the ones that misregulate, which is the timing
  mechanism the description asserted without support.
- PMID:20188665, `REFUTE` / `MODEL_ORGANISM` — recorded as a refutation rather
  than softened into support, because "predominantly repressor of long,
  methylated genes" is what Skene's near-histone-octamer abundance result argues
  against. The description's separate chromatin-modifier claim stands, so only
  the repressor framing is refuted.

**Expanded `pathophysiology#Loss of MeCP2 Epigenetic Regulation`**: description
now records genome-wide chromatin dampening, splicing regulation, and SEC-
mediated elongation; added `GO:0006325` and `GO:0008380`; added evidence
PMID:20188665 (global chromatin change), PMID:28211484 (most MeCP2 partners are
splicing factors), PMID:41296873 (MeCP2 loads AFF4 on synaptic-plasticity genes).

**New node `Cortical Excitation/Inhibition Imbalance`**, downstream of
`Dysregulated Neuronal Gene Expression`, feeding `Seizures` and `Gait
Abnormalities`, grounded on two PMID:32129908 evidence items. The paper's own
hedge — "likely due to GABAergic dysfunction" — is preserved in the node
description rather than upgraded to an assertion.

**New node `Non-Cell-Autonomous Glial Injury of Neurons`**, downstream of `Loss
of MeCP2 Epigenetic Regulation`, feeding `Reduced Synapse and Dendritic Spine
Density`, with PMID:20392956 (two items) and PMID:24285883.

**Expanded `pathophysiology#Brainstem Respiratory Circuit Dysregulation`** with
the Kölliker-Fuse localisation and both directions of the PMID:26507912
perturbation.

**Three `discussions` entries**, which is where the unresolved material went
rather than into nodes:
- `rett_mecp2_phase_separation_species_mismatch` (`HUMAN_MODEL_MISMATCH`) — the
  LLPS dispute, curated as translational rather than merely contested because
  PMID:38719804 shows the focal MeCP2 distribution behind the model is a mouse
  trait and human MeCP2 is diffuse.
- `rett_prenatal_versus_postnatal_contribution` (`KNOWLEDGE_GAP`) — the organoid
  result, with a timed conditional deletion experiment proposed.
- `rett_peripheral_tissue_autonomous_pathology` (`KNOWLEDGE_GAP`) — hepatic and
  innate-immune tissue-autonomous pathology, which has no phenotype in this
  entry to attach to.

### Deliberately not integrated

- **PMID:30929312 detection rates.** Review-level, and the entry already carries
  the causal MECP2 claim from the primary discovery paper and from ClinGen.
- **PMID:38232652 trofinetide endpoints.** Restates curated content and would
  import the report's significance error.
- **PMID:39838601 dosage sensitivity.** The comparison group is male RTT-like,
  not classic Rett. The narrow-therapeutic-window point already sits in the
  hypothesis notes, and three AAV-MECP2 trials are already curated.
- **PMID:41182667 as a pathophysiology node.** One organoid line, one variant,
  no human in vivo measurement — a knowledge gap, not a mechanism node.
- **PMID:27288453 / PMID:35085773 as pathophysiology nodes.** Real findings, but
  the entry curates no peripheral phenotype for them to reach, and a node with
  no downstream would dangle.
- **Hypothesis `status`.** Retained CANONICAL. The report's own recommendation
  was to annotate rather than change it, and the annotation was already there.
- **PMID:23077217 (catecholaminergic rescue), PMID:31629059, PMID:22412847,
  PMID:22815516, PMID:17046689, PMID:26842955, PMID:21085180, PMID:28927958,
  PMID:18032561, PMID:21307341, PMID:41455590, PMID:42159339.** Verified where
  fetched, but each restates a mechanism the entry already models or extends it
  into territory (PTM cascade, mitochondrial and OxInflammatory biology, L1
  retrotransposition) that would need its own curation pass rather than a
  bolt-on evidence item.
