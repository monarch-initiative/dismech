---
title: 'NAMs Special Issue: Open Questions and Unmapped Models'
status: IN_PROGRESS
description: >-
  Edge cases raised by screening the Toxicology NAMs special issue: methods that belong
  in the NAMs registry but have no dismech home, mechanisms with no pathograph node to
  attach a model to, and scope questions the existing conventions do not settle.
tags: [MODELS, NAM, SCHEMA, EVIDENCE]
---

# NAMs Special Issue: Open Questions and Unmapped Models

Questions raised while screening the papers tracked in
[NAMS_SPECIAL_ISSUE](../NAMS_SPECIAL_ISSUE.md). Each one is a decision that has to be
made before or during extraction, with the state of play rather than an answer.

Anything here that turns into a settled convention belongs in
[`docs/explanation/design-decisions.md`](../../docs/explanation/design-decisions.md),
which is the decision register. This page is the staging area: open questions, not
recorded decisions.

## 1. A method can belong in the registry and have no dismech home

Tracked as dismech#16882.

Four screened-out papers are legitimate NAMs and would plausibly earn a registry entry,
but offer nothing a pathograph node can attach to:

- read-across mutagenicity classification (PMID:37993082)
- nanoparticle toxicity by machine learning (PMID:38056590)
- q-RASAR for subchronic oral NOAEL (PMID:38705560)
- the true-dose in vitro dosimetry workflow (PMID:38719068)

Each predicts or conditions a toxicity endpoint without asserting a mechanism. dismech
links a model to a *mechanism node*, so a method whose output is an apical label has no
anchor by construction.

**Question:** does the registry take these, with dismech simply not citing them? If so,
the registry's inclusion criteria are strictly broader than dismech's, and a screening
pass driven from dismech's needs will systematically under-nominate for the registry.
That argues for screening against the registry's criteria first and dismech's second,
rather than the single pass used here.

## 2. Is a simulation of a human protein a model of a mechanism?

Tracked as dismech#16883.

Three papers are purely computational but target a specific human protein and make a
mechanistic claim about it:

- zearalenone inhibition of aromatase (CYP19A1) across 434 human sequence variants
  (PMID:38036094)
- P-glycoprotein (ABCB1) conformational dynamics with ATP and substrates
  (PMID:38272384)
- ochratoxin A predicted to inhibit OGFOD1, a translation factor (PMID:38432407)

These were screened in. They have no biological system, which the screening rule asks
for, but they do name a mechanism at molecular scale and a model that bears on it, and
`computational_models:` with `model_scale: MOLECULAR` is exactly the shape for that.

**Question:** where is the floor? A docking run that proposes a novel target
(the OGFOD1 case) is a hypothesis, not a measurement. Recording it as a model link
asserts the model informs the node; recording it as evidence asserts something weaker.
The `divergences` taxonomy may cover this with `PROXY_QUANTITY` — binding affinity
standing in for inhibition in a cell — but a predicted interaction with no wet
confirmation might warrant a `KNOWLEDGE_GAP` discussion instead of a model link.

## 3. Human sequence variation as a modifier of toxicant susceptibility

Tracked as dismech#16884.

The aromatase paper's finding is that specific human variants differ in how strongly
zearalenone inhibits the enzyme — T310S more susceptible, D309G and S478F possibly
inactive. dismech has `population_effects` for a variant behaving differently across
human populations, and `effect_modifiers` with `GENOTYPE` for a treatment working
differently by genotype. Neither covers a *toxicant* whose effect depends on host
genotype.

**Question:** is toxicant susceptibility by host variant a gap, or should the exposure
be modelled as a treatment-like perturbation so `effect_modifiers` applies? Note the
paper's variant effects are computationally predicted, so whichever slot is chosen, the
source is a simulation and not an observed cohort difference.

## 4. No module for inhaled-irritant injury to the conducting airway

Tracked as dismech#16877. **Closed** — the module `inhaled_irritant_airway_injury` now exists.

Repeatedly needed and absent. Papers affected: 1,3-dichloropropene nasal exposure
(PMID:37863466), Calu-3 aerosol exposure (PMID:38013136), heated tobacco products
(PMID:38614204), and the particulate matter lung arm (PMID:38029955).

The closest existing modules do not fit. `alveolar_capillary_barrier_failure` is distal
lung. `emphysema_protease_antiprotease_imbalance` is a different mechanism.
`epithelial_barrier_dysfunction` is scoped to the allergic and type 2 epithelial barrier
hypothesis, so conforming a chemical irritant to it overstates what the module claims.

**Question:** one module for inhaled-irritant airway epithelial injury, or is this
several — oxidative and electrophilic injury, barrier loss, and loss of mucociliary
differentiation are distinguishable mechanisms that these papers measure separately.

## 5. No module for chemical respiratory allergy

Tracked as dismech#16878. **Closed** — the module `chemical_respiratory_allergy` now exists.

Three papers in this issue address it directly: the airway sensitizer biomarker study
(PMID:38360295), the 3D tetraculture bronchial model (PMID:38369009), and, on the skin
side of the same AOP family, the Nrf2 reporter epidermis (PMID:38341018). Occupational
asthma from low molecular weight sensitizers has a recognised AOP, and the papers name
its key events: danger signal production, dendritic cell activation, epithelial mucin
disruption, endothelial adhesion molecule expression.

dismech has `cdc1_tolerogenic_maturation` and `nlrp3_inflammasome_activation`, which
cover fragments, and [AOP_40_SKIN_SENSITIZATION](../AOP_40_SKIN_SENSITIZATION.md)
already maps the skin sensitization AOP's assays to key events.

**Question:** does chemical respiratory allergy become a module, and if so does it sit
beside the skin sensitization work as a sibling? The two AOPs share the covalent
protein binding molecular initiating event and diverge downstream, which is the shape
`conforms_to` handles well.

## 6. Where does an IVIVE or PBPK bridge live?

Tracked as dismech#16887.

The ReproTracker paper (PMID:38029956) pairs an hiPSC assay with a PBPK model to turn an
in vitro concentration into a human equivalent dose, and the 1,3-dichloropropene paper
does the same with IVIVE. This dosimetry step is what carries the regulatory weight, and
it is not a mechanism.

**Question:** dismech has `computational_models:` and the models directory, but an IVIVE
bridge does not model a pathograph node — it models the relationship between an exposure
and an internal concentration. Recording it as a model link to the mechanism the assay
reads out would misstate what it computes. It may belong only in the registry.

## 7. A validated model with no pathology to attach it to

Tracked as dismech#16888.

The Calu-3 paper (PMID:38013136) and the bronchial tetraculture paper (PMID:38369009)
both spend half their length establishing that the model reproduces normal mucociliary
differentiation — rising barrier resistance, mucous and ciliated cell markers up, basal
markers down. That is the model's credibility claim, and it is a normal developmental
trajectory, not a disease mechanism.

**Question:** dismech models pathology, so there is no node for normal differentiation
and arguably should not be. But the registry report should carry it, since it is the
evidence the model is fit for purpose. This may simply be a case where the registry row
is richer than the dismech link, which is worth stating explicitly if so.

## 8. Species scale in a multi-tissue co-culture

Tracked as dismech#16889.

The particulate matter paper (PMID:38029955) builds co-cultures from a mix of human
cell lines (A549, HEK001), a rabbit corneal line (SIRC), and a mouse fibroblast feeder
layer (BALB/3T3). The ocular arm is therefore not a human model, and the feeder layer
is non-human in all three arms.

**Question:** `SPECIES_MISMATCH` exists in the divergence taxonomy, but a single
`model_scale` and one `fidelity` tier describe a construct whose layers differ in
species. Recording one divergence for the construct loses which layer is affected.

## 9. Synergy between two exposures

Tracked as dismech#16885.

The pesticide AOP paper (PMID:38040083) finds that pairs of pesticides from different
classes act synergistically on shared key events, with combination indexes below 1.
dismech's `environmental[].influences_mechanisms` links one exposure to one node.

**Question:** nothing expresses "these two exposures together produce an effect greater
than either alone". Two separate `TRIGGERS` links state that both act on the node and
lose the interaction, which is the paper's actual finding.

## 10. AOP-derived content inherits the qualitative/quantitative gap

Raised by the PFOS paper (PMID:38580097, dismech#16870), but not specific to it.

That paper's result is a negative one for the mechanism-based route: PFOS meets the ED
criteria under the standard guidance-based assessment but **not** under the AOP/NAM
mechanism-based assessment, and the authors discuss the need for *quantitative* AOPs —
key-event relationships described quantitatively enough to carry a hazard call — for that
route. Whether the qualitative thyroid→DNT KERs the paper used actually lack quantitative
understanding is a checkable claim, not an asserted one: the AOP-Wiki KER
`quantitative-understanding` fields answer it (the `aop-wiki` skill), and the full text
that would name the exact AOP set the paper assembled was not reachable in this
environment, so it is left unchecked here rather than stated. A qualitative AOP says A
leads to B; it does not say how much of A produces how much of B, or whether a given
exposure reaches the threshold.

dismech's causal edges are qualitative by construction: a `downstream` or
`influences_mechanisms` link asserts direction and, through `hypothesis_groups` and
evidence grading, strength of belief — but not a dose-response. So any dismech content
derived from an AOP inherits exactly the limitation this paper raises. An edge mapped from
a qualitative AOP is a statement that the path is *plausible and supported*, never that a
particular exposure *does* traverse it at a relevant dose.

This matters most for exposure-initiated chains (the `environmental[].influences_mechanisms`
edges), where the regulatory question is quantitative by definition. It is the same
observation already open in [`AOP_EMOD_ALIGNMENT`](../AOP_EMOD_ALIGNMENT.md)'s
quantitative-AOP-development thread, recorded here so the screen's own instance of it is
not lost.

**Question:** should AOP-derived edges carry an explicit marker that they are qualitative
— distinguishing "this path is established in the AOP framework" from "this exposure
traverses it at a relevant internal dose" — or is that distinction already adequately
carried by evidence grading plus the absence of a dose slot? Either way, AOP-derived
dismech content should not be read as a quantitative hazard statement, and a note to that
effect belongs wherever such content is first added.
