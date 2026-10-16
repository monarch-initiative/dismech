---
title: 'GPCRs: Drug Mechanisms and Disease Modules'
status: PLANNED
description: >-
  Mechanism modules anchored on G protein-coupled receptors: drug-mechanism
  modules for the major GPCR-targeting drug classes, and disease modules for
  receptor loss-of-function, gain-of-function and transducer defects.
tags: [PHARMACOLOGY, MODULES, GPCR]
diseases:
- Heart_Failure
- Essential_Hypertension
- Type_2_Diabetes_Mellitus
- Obesity
- Obesity_Due_to_MC4R_Pathway_Disruption
- Opioid_Use_Disorder
- Acute_Opioid_Poisoning
- Acute_Post-Surgical_Pain
- Alcohol_Use_Disorder
- Schizophrenia
- Parkinsons_Disease
- Migraine
- Asthma
- Chronic_Obstructive_Pulmonary_Disease
- Urticaria
- Gastroesophageal_Reflux_Disease
- Multiple_Sclerosis
- Glaucoma
- Familial_Hypocalciuric_Hypercalcemia_1
- Autosomal_Dominant_Hypocalcemia_1
- X-Linked_Nephrogenic_Diabetes_Insipidus
- Pseudohypoparathyroidism
- Familial_Glucocorticoid_Deficiency
- Kallmann_Syndrome
modules:
- cardiac_camp_pka_calcium_handling
- somatotroph_camp_pka_overactivation
- spinal_hsp90_opioid_enhancement
- addiction_cycle
- parkinsonism_dopaminergic_degeneration
- photoreceptor_degeneration
---

# GPCRs: Drug Mechanisms and Disease Modules

## Overview

G protein-coupled receptors are the molecular target of a large share of
approved drugs and the site of a well-defined set of Mendelian
endocrinopathies. This project builds dismech **mechanism modules** around
them, on two axes:

1. **Drug-mechanism modules** — one per major GPCR-targeting drug class, so a
   disease entry's treatment can `conforms_to` a shared receptor → transducer →
   effector chain instead of re-deriving it, following the pattern the
   antimicrobial set established (`projects/ANTIMICROBIAL.md`).
2. **Disease modules** — the recurring ways a GPCR or its transducer breaks:
   loss of function (hormone resistance), constitutive activation, and
   transducer defects.

The gene side is curated in parallel in ai-gene-review
([projects/GPCR.md](https://github.com/ai4curation/ai-gene-review/blob/main/projects/GPCR.md)):
receptor and transducer gene reviews, PANTHER family reviews, and GO
pathway modules (Gs-cAMP-PKA, Gq-PLC-Ca2+, planned Gi/o, G12/13, arrestin).
The receptor reviewed there is the molecular anchor for the module here.

## Scope (what this is and is not)

- **In scope:** the pharmacological mechanism by which a GPCR drug changes a
  disease's pathophysiology, including on-target adverse effects that are
  themselves mechanisms (opioid respiratory depression, antipsychotic
  parkinsonism, 5-HT2B valvulopathy).
- **Not in scope:** a drug–indication database, dosing, or pharmacokinetics
  except where it gates mechanism. NCIT P302 already supplies indications
  (`projects/NCIT_TREATMENT_INDICATIONS.md`).
- **Granularity:** one module per receptor-and-direction (agonism vs
  antagonism), not per drug. Drugs sit on the conforming disease entries'
  `treatments` with `therapeutic_agent` bindings.

## Existing modules that touch GPCRs

| Module | GPCR content |
|---|---|
| `cardiac_camp_pka_calcium_handling` | beta-adrenergic → cAMP → PKA → Ca2+ handling in cardiomyocytes |
| `somatotroph_camp_pka_overactivation` | GPR101 / GNAS / AIP convergence on cAMP in somatotrophs |
| `spinal_hsp90_opioid_enhancement` | mu-opioid receptor signaling amplification |
| `addiction_cycle` | dopamine and opioid receptor circuitry |
| `parkinsonism_dopaminergic_degeneration` | nigrostriatal dopaminergic degeneration → striatal dopamine deficiency (presynaptic; no receptor content, so not a target for D2-blockade parkinsonism, which involves no neuron loss) |
| `photoreceptor_degeneration` | rhodopsin-related retinopathy |

Read each before creating a neighbour, and extend rather than duplicate where
the scope already fits.

## Workstream A — Drug-mechanism modules

Candidate modules, ordered by how many existing disease entries would
conform:

| Proposed module | Receptor (gene) | Drug classes | Candidate conformers |
|---|---|---|---|
| beta-adrenergic receptor blockade | ADRB1, ADRB2 | beta-blockers | Heart_Failure, Essential_Hypertension, Atrial_Fibrillation, Glaucoma, Migraine |
| AT1 receptor blockade | AGTR1 | sartans | Essential_Hypertension, Heart_Failure, diabetic kidney disease |
| mu-opioid receptor agonism | OPRM1 | opioid analgesics; antagonists/partial agonists for OUD | Opioid_Use_Disorder, Acute_Opioid_Poisoning |
| D2 receptor antagonism | DRD2 | antipsychotics, antiemetics | Schizophrenia; toxicity arm to drug-induced parkinsonism |
| dopamine receptor agonism | DRD2, DRD3 | dopamine agonists | Parkinsons_Disease, hyperprolactinemia |
| GLP-1 / GIP receptor agonism | GLP1R, GIPR | incretin mimetics | Type_2_Diabetes_Mellitus, Obesity |
| 5-HT1B/1D agonism and CGRP receptor antagonism | HTR1B, HTR1D, CALCRL/RAMP1 | triptans, gepants | Migraine, Migraine_with_Aura |
| H1 / H2 receptor antagonism | HRH1, HRH2 | antihistamines, H2 blockers | Urticaria, allergic rhinitis, Gastroesophageal_Reflux_Disease |
| beta2 agonism / muscarinic antagonism (airway) | ADRB2, CHRM3 | SABA/LABA, LAMA | Asthma, Chronic_Obstructive_Pulmonary_Disease |
| CaSR positive allosteric modulation | CASR | calcimimetics | secondary hyperparathyroidism in CKD |
| S1P receptor modulation | S1PR1 | fingolimod, siponimod | Multiple_Sclerosis |
| P2Y12 receptor antagonism | P2RY12 | clopidogrel, ticagrelor | Coronary_Artery_Disease |
| V2 receptor antagonism | AVPR2 | vaptans | SIADH, ADPKD |
| MC4R agonism | MC4R | setmelanotide | Obesity_Due_to_MC4R_Pathway_Disruption |

Each module follows the `create-module` skill: a trigger → receptor
engagement → transducer → effector → tissue consequence chain, with the
treatment `target_mechanisms` drug pattern, `module_categories:
[PHARMACOLOGY]` (plus `TOXICOLOGY` where an adverse-effect arm is modelled),
and receptor genes bound to HGNC.

Adverse-effect arms to model explicitly, because they are mechanisms in
their own right: opioid respiratory depression (brainstem MOR), D2-blockade
extrapyramidal effects and hyperprolactinemia, beta-blocker bronchospasm
(beta2 off-selectivity), 5-HT2B agonist valvulopathy.

### First pairing: mu-opioid receptor (OPRM1)

Chosen first (2026-10-15): opioid drugs appear in about 18 entries
(`Opioid_Use_Disorder`, `Acute_Opioid_Poisoning`, `Acute_Post-Surgical_Pain`,
`Alcohol_Use_Disorder`, ...) and in `addiction_cycle` and
`spinal_hsp90_opioid_enhancement`, each describing the mechanism on its own.

- **Mu-opioid receptor agonism** (morphine, fentanyl, oxycodone; methadone
  and buprenorphine for OUD). Branches: analgesia (spinal and supraspinal),
  respiratory depression (brainstem; the overdose mechanism), constipation
  (enteric), reward/tolerance/dependence (link to `addiction_cycle`).
  Buprenorphine, a partial agonist, belongs here with its respiratory
  ceiling recorded on that branch rather than in a third module.
- **Mu-opioid receptor antagonism** (naloxone reversal, naltrexone relapse
  prevention, peripheral antagonists for opioid-induced constipation).
- Biased agonism (oliceridine) remains the open question below; this module
  pair is where it will need an answer.
- Kappa-opioid modules (nalfurafine; mixed agonist-antagonists) come later.

## Workstream B — Disease modules

| Proposed module | Mechanism | Example conformers |
|---|---|---|
| GPCR loss-of-function hormone resistance | receptor misfolding / ER retention or loss of coupling → end-organ resistance despite high ligand | X-Linked_Nephrogenic_Diabetes_Insipidus (AVPR2), Familial_Hypocalciuric_Hypercalcemia_1 (CASR), Familial_Glucocorticoid_Deficiency (MC2R/MRAP), Obesity_Due_to_MC4R_Pathway_Disruption, Kallmann_Syndrome / GNRHR / KISS1R hypogonadism |
| GPCR constitutive activation | ligand-independent receptor signaling → hormone excess or tissue overgrowth | Autosomal_Dominant_Hypocalcemia_1 (CASR gain), Jansen metaphyseal chondrodysplasia (PTH1R), familial male-limited precocious puberty (LHCGR), non-autoimmune hyperthyroidism (TSHR) |
| Gs alpha defect | GNAS loss (with imprinting) → multi-hormone resistance; GNAS gain → cAMP excess | Pseudohypoparathyroidism, McCune-Albright syndrome (no dismech entry yet; a curation target); relate to `somatotroph_camp_pka_overactivation` |

The loss/gain pair is deliberately symmetric: the same receptor (CASR, TSHR,
LHCGR) appears on both sides, which is the test that the modules are
mechanism-level rather than disease-level.

## Plan

### Phase 0 — scoping
- [ ] Census: which `kb/disorders` entries already name a GPCR drug in
      `treatments` (`therapeutic_agent`) and which GPCR genes appear in
      `genetic:`
- [ ] Agree tranche-1 receptor list with the ai-gene-review side
- [ ] Decide whether the drug-mechanism set becomes a `kb/module_collections/`
      entry (GPCR drug mechanisms)

### Phase 1 — first modules
- [ ] mu-opioid receptor agonism (first module; see above) — `mu_opioid_receptor_agonism`, in review in #14453
- [ ] mu-opioid receptor antagonism — `mu_opioid_receptor_antagonism`, in review in #14456
- [ ] beta-adrenergic receptor blockade
- [ ] GLP-1 receptor agonism
- [ ] GPCR loss-of-function hormone resistance
- [ ] GPCR constitutive activation

### Phase 2 — conformers and remaining modules
- [ ] Add `conforms_to` on the treatment-linked pathophysiology nodes of the
      candidate conformers above
- [ ] Remaining Workstream A modules
- [ ] Gs alpha defect module

## Decisions

- **Agonism and antagonism of the same receptor are separate modules** (decided
  2026-10-15), because their downstream consequence chains differ.

## Open questions

- How should biased agonism (G protein vs arrestin, e.g. oliceridine) be
  represented — a node within the agonism module, or a hypothesis group?
- Is a CGRP-receptor module better placed with migraine neurovascular
  mechanism than with the 5-HT1B/1D triptan module?
