---
title: Drugs With Unknown or Contested Mechanisms of Action
status: IN_PROGRESS
description: >-
  Audit of KB treatments that use a drug whose therapeutic mechanism is unknown
  or disputed, to check that their target_mechanisms edges do not state a
  settled mechanism the literature does not support.
tags: [AUDIT, TREATMENTS, PHARMACOLOGY]
diseases:
- Bipolar_Disorder
- Major_Depressive_Disorder
- Post-Traumatic_Stress_Disorder
- Type_2_Diabetes_Mellitus
- Idiopathic_Hypersomnia
- pseudotumor_cerebri
- BRPF1-Related_Intellectual_Disability
- Li-Ghorbani-Weisz-Hubshman_Syndrome
- Immunodeficiency_64
- Lafora_Disease
- Maple_Syrup_Urine_Disease
- Dravet_syndrome
modules:
- deregulated_nutrient_sensing
- disabled_macroautophagy
- gut_dysbiosis
- inflammaging
- mitochondrial_dysfunction
- stem_cell_exhaustion
---

# Drugs With Unknown or Contested Mechanisms of Action

## Why this matters for dismech

A `treatments[].target_mechanisms` edge says *this drug acts on this node of the
causal graph*. For most drugs that is a well-characterized claim. For a set of
widely used drugs (valproate, lamotrigine, topiramate, metformin, lithium,
ketamine, cannabidiol, paracetamol, modafinil, riluzole) the mechanism that
produces the therapeutic effect is still unknown or disputed, even though the
clinical effect is not. On those, a `target_mechanisms` edge can state a
mechanism more confidently than its source does, and the schema has no way to
record that the mechanism is open.

## Source list

Wikipedia's
[Category:Drugs with unknown mechanisms of action](https://en.wikipedia.org/wiki/Category:Drugs_with_unknown_mechanisms_of_action)
(154 pages and a *General anesthetics* subcategory, read 2026-10-12) is the
seed list. It is a **lead, not a ruling**:

- Membership is editor-assigned and goes stale. Lenalidomide is listed, although
  cereblon-dependent degradation of IKZF1/IKZF3 is now the accepted mechanism.
  Clavulanic acid is listed, although it is a beta-lactamase inhibitor.
- "Unknown" refers to the drug's best-known use. Ethanol is listed for its
  psychoactive effects. As a toxic-alcohol antidote, competitive saturation of
  alcohol dehydrogenase is well understood.
- Most of the 154 pages are research compounds, racetams, and modafinil
  analogues that the KB does not use.

## Overlap with the KB

String matching on treatment `name` and `treatment_term` (agents included)
across `kb/disorders`, `kb/modules` and `kb/comorbidities` found **25 of the
listed drugs in 248 treatment records across 193 entries**. 113 of those
records carry `target_mechanisms` (in 93 entries). The full table is
[`DRUGS_UNKNOWN_MECHANISM/kb_treatment_overlap.tsv`](DRUGS_UNKNOWN_MECHANISM/kb_treatment_overlap.tsv);
the discussions already attached to each record are in
[`kb_treatment_discussions.tsv`](DRUGS_UNKNOWN_MECHANISM/kb_treatment_discussions.tsv).
Matching is lexical, so a multi-drug treatment ("Valproate with lamotrigine")
is counted once per drug.

| Drug | Treatment records | With `target_mechanisms` |
|---|---:|---:|
| Valproate | 81 | 33 |
| Lamotrigine | 29 | 10 |
| Topiramate | 28 | 13 |
| Metformin | 25 | 18 |
| Cannabidiol | 12 | 6 |
| Ketamine | 10 | 6 |
| Memantine | 9 | 5 |
| Riluzole | 8 | 3 |
| Lenalidomide | 7 | 2 |
| Paracetamol | 6 | 2 |
| Lithium | 5 | 3 |
| Ethanol | 4 | 4 |
| Modafinil | 4 | 1 |
| Amantadine | 4 | 0 |
| Mesalazine | 3 | 1 |
| Selegiline | 2 | 2 |
| Edaravone | 2 | 1 |
| Anagrelide | 2 | 0 |
| Rasagiline, Piracetam, Medroxyprogesterone acetate, Hydralazine, Clavulanic acid, Armodafinil, Acamprosate | 1 each | 4 total |

## Triage

The 113 linked records fall into three groups. Only the third needs review.

1. **Symptomatic targets make no mechanism claim.** An antiseizure medication
   targeting `Seizures` or `Cortical Network Hyperexcitability` says the drug
   suppresses the phenotype, which is the documented clinical effect. The
   schema explicitly allows this. Most valproate, lamotrigine, topiramate and
   cannabidiol records are here. No action needed.
2. **The mechanism in this use is known, despite the Wikipedia listing.**
   Ethanol as an ADH-competing antidote (`Ethylene_Glycol_Poisoning`,
   `Methanol_Poisoning`, `Diethylene_Glycol_Poisoning`,
   `toxic_alcohol_adh_bioactivation`); selegiline and rasagiline as MAO-B
   inhibitors in `Parkinsons_Disease`; memantine as an NMDA channel blocker on
   GRIN gain-of-function nodes; clavulanic acid in `Pasteurellosis`. No action
   needed beyond checking the evidence.
3. **A specific molecular mechanism is asserted for a drug whose therapeutic
   mechanism is contested.** These are the worklist:
   - **Metformin, six aging modules.** Each module asserts a different
     mechanism: AMPK/mTORC1 (`deregulated_nutrient_sensing`), autophagic flux
     (`disabled_macroautophagy`), microbiome (`gut_dysbiosis`),
     anti-inflammatory (`inflammaging`), mitochondrial
     (`mitochondrial_dysfunction`), stem-cell (`stem_cell_exhaustion`).
     These may all be true, but read together they show that no single
     mechanism has been established. Also check `Type_2_Diabetes_Mellitus`
     (hepatic glucose output, where the molecular route is contested),
     `Lafora_Disease`, `Maple_Syrup_Urine_Disease`, `Li-Fraumeni_Syndrome`
     (already covered by a gap, see below),
     `Classic_Familial_Adenomatous_Polyposis`,
     `Oral_Cavity_Squamous_Cell_Carcinoma`.
   - **Lithium in `Bipolar_Disorder`.** Four parallel targets (GSK-3β,
     phosphoinositide, circadian, neuroplasticity). These are the competing
     hypotheses, not an established mechanism. They are a candidate for
     `mechanistic_hypotheses` groups.
   - **Valproate as an HDAC inhibitor** (`BRPF1-Related_Intellectual_Disability`,
     and `Li-Ghorbani-Weisz-Hubshman_Syndrome`, which is already covered by a
     gap) and on mitochondrial nodes
     (`Autosomal_Recessive_Spinocerebellar_Ataxia_20`). HDAC inhibition is a
     real property of valproate, so check that the evidence shows it acting
     through that route *in this disease*.
   - **Ketamine** in `Major_Depressive_Disorder` and
     `Post-Traumatic_Stress_Disorder` (the antidepressant mechanism beyond NMDA
     block is disputed), **modafinil** in `Idiopathic_Hypersomnia`,
     **topiramate** in `pseudotumor_cerebri` (CSF hypersecretion),
     **lenalidomide** in `Immunodeficiency_64` (already covered by a gap),
     **paracetamol** in
     `Patent_Ductus_Arteriosus`, **riluzole** in `Friedreich_Ataxia` and
     `Spinocerebellar_Ataxia_Type_1`, **edaravone** in
     `Amyotrophic_Lateral_Sclerosis`.

For each record in group 3, the review is:

- Read the `target_mechanisms[].evidence`. If the quote shows a clinical
  response and the mechanism is inferred from it, mark the item
  `directness: INDIRECT`. That is what `INDIRECT` means: a therapeutic
  response cited as validation of the mechanism it targets.
- If the entry carries competing mechanisms for one drug, consider expressing
  them as `mechanistic_hypotheses` with `hypothesis_groups` on the edges
  rather than as parallel settled edges.
- If no evidence supports the specific node, retarget the edge to the
  phenotype the drug treats, or remove it. Do not add evidence in order to
  keep the edge.
- Record the open mechanism as a `KNOWLEDGE_GAP` discussion (next section).

## Recording an unknown mechanism: a knowledge gap on the treatment

No new slot is needed. A `discussions` entry with `kind: KNOWLEDGE_GAP` whose
`attaches_to` names both the treatment and the node its edge targets says
exactly this: the drug works, and how it works here is not established. The
`prompt` states the question, the `rationale` says which candidate mechanisms
the evidence cannot tell apart, and `proposed_experiments` can say how they
could be.

Three entries already do this and are the pattern to copy:

| Entry | Discussion | Drug |
|---|---|---|
| `Li-Fraumeni_Syndrome` | `lfs_metformin_mechanism_unresolved` | Metformin. The MILI trial protocol itself calls the mechanism unclear. |
| `Li-Ghorbani-Weisz-Hubshman_Syndrome` | `kat8_valproate_mechanism_untested` | Valproate. HDAC inhibition vs. generic anticonvulsant effect; histone acetylation has not been measured in a treated patient. |
| `Immunodeficiency_64` | `rasgrp1_lenalidomide_translational_gap` | Lenalidomide |

`HNRNPU-Related_Developmental_and_Epileptic_Encephalopathy` asks a similar
question about valproate (`gap_valproate_efficacy_mechanism`) but is not the
pattern: it is an `OPEN_QUESTION` attached only to
`pathophysiology#Recurrent Seizures`, not to a treatment.

### Coverage

Of the 113 linked records, 47 have some discussion attached to the treatment
or to a node it targets. Almost all of those discussions are about the node,
for example whether a biomarker tracks aging. They are not about the drug.
**Apart from the three pattern entries above (`Li-Fraumeni_Syndrome`,
`Li-Ghorbani-Weisz-Hubshman_Syndrome`, `Immunodeficiency_64`), none of the
group 3 records had a gap about the drug's own mechanism** when this page was
written. That included the metformin module edges, lithium in
`Bipolar_Disorder` and both ketamine psychiatric entries. Adding one per
record, attached to the treatment and its target, is the main deliverable of
this project.

Rules for writing them:

- One discussion per entry and drug, attached to every node the drug targets
  there. Do not create one per edge.
- The `rationale` names the candidate mechanisms and says why the cited
  evidence does not discriminate between them. It needs its own evidence, and
  ideally a source that says the mechanism is unclear in so many words, as the
  MILI protocol does for Li-Fraumeni. A Wikipedia category listing does not
  count.
- A gap does not replace fixing an edge that overstates its evidence. Do both:
  set `directness: INDIRECT` where the mechanism is inferred from a clinical
  response, and record the gap.
- Where the literature argues for two or more specific models (lithium), a
  `CONTROVERSY` discussion or `mechanistic_hypotheses` groups may fit better
  than `KNOWLEDGE_GAP`. Use `KNOWLEDGE_GAP` when the honest answer is that
  nobody has tested it.

### Progress

**Everything listed as done below is in PR #14110 and is not on `main` until
that PR merges.**

Done (one `KNOWLEDGE_GAP` each, attached to the treatment and its targets):
`deregulated_nutrient_sensing`, `disabled_macroautophagy`, `gut_dysbiosis`,
`inflammaging`, `mitochondrial_dysfunction` (metformin) and `Bipolar_Disorder`
(lithium, `gap_bipolar_lithium_therapeutic_mechanism`).

**Not done, on purpose: `stem_cell_exhaustion`.** The study behind that
metformin edge (`PMID:33524231`) tested the mechanism: siRNA knockdown of AMPKα
abolished metformin's effect on NF-κB activation and the senescence-associated
secretory phenotype in cultured CKD mesenchymal stem cells. The mechanism in
that system is therefore supported, and an "unknown mechanism" gap would be
false. What remains open is whether ex vivo preconditioning says anything about
systemic metformin and resident stem cells in aging tissue. That is a
translational question, not this project's.

Done with an OpenScientist report behind each (`just research-drug-mechanism`,
reports in `research/drug_mechanism/`). Every quote used was re-checked against
`references_cache/`:

| Entry | Drug | Report verdict | Gap |
|---|---|---|---|
| `Major_Depressive_Disorder` | ketamine | several competing candidates | `gap_mdd_ketamine_therapeutic_mechanism` |
| `Type_2_Diabetes_Mellitus` | metformin | physiological effect established, molecular route unknown | `gap_t2d_metformin_molecular_mechanism` |
| `pseudotumor_cerebri` | topiramate | not established | `gap_iih_topiramate_mechanism` |
| `Idiopathic_Hypersomnia` | modafinil | unknown | `gap_ih_modafinil_mechanism` |

The reports are leads, not evidence. Two of their claims did not survive
checking against the cited source and were left out (see the history records).
OpenScientist jobs can exceed the client's default one-hour timeout; pass
`--param timeout=7000`.

Still pending for all ten records: the `directness: INDIRECT` check on the
existing edge evidence. The gaps were added without changing any edge, and
several edges carry no evidence of their own, including every metformin
module edge and the lithium circadian edge.

The knowledge gaps and research reports themselves are in PR #14110; this
page, the recipe and the template are kept separate because the curation
scope check does not allow tooling in a KB PR.

Remaining: the other group 3 records above.

A schema change, such as a treatment-level "mechanism unknown" flag, would
duplicate this and is not proposed.

## Reproducing the overlap

The table was built by matching drug names (with common synonyms:
acetaminophen, mesalamine, valproic, dipyrone) against each treatment's `name`
and `treatment_term`, excluding evidence text. It is not a gate and should not
become one. Membership in the Wikipedia category is not a property of a KB
treatment.
