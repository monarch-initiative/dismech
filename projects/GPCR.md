---
title: 'GPCRs: Drug Mechanisms and Disease Modules'
status: IN_PROGRESS
description: >-
  Mechanism modules anchored on G protein-coupled receptors: drug-mechanism
  modules for the major GPCR-targeting drug classes, and disease modules for
  receptor loss-of-function, gain-of-function and transducer defects.
tags: [PHARMACOLOGY, MODULES, GPCR]
diseases:
- Heart_Failure
- Essential_Hypertension
- Atrial_Fibrillation
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
- Migraine_with_Aura
- pseudotumor_cerebri
- Restless_Legs_Syndrome
- Peripartum_Cardiomyopathy
- Asthma
- Thunderstorm_Asthma
- Formaldehyde_Poisoning
- Chronic_Obstructive_Pulmonary_Disease
- Urticaria
- Alpha-gal_Syndrome
- Gastroesophageal_Reflux_Disease
- Multiple_Sclerosis
- Glaucoma
- Familial_Hypocalciuric_Hypercalcemia_1
- Autosomal_Dominant_Hypocalcemia_1
- X-Linked_Nephrogenic_Diabetes_Insipidus
- Pseudohypoparathyroidism
- Familial_Glucocorticoid_Deficiency
- Kallmann_Syndrome
- Bipolar_Disorder
- Cannabis_Hyperemesis_Syndrome
- Subacute_Delirium
- IgA_Nephropathy
modules:
- cardiac_camp_pka_calcium_handling
- somatotroph_camp_pka_overactivation
- spinal_hsp90_opioid_enhancement
- addiction_cycle
- parkinsonism_dopaminergic_degeneration
- photoreceptor_degeneration
- mu_opioid_receptor_agonism
- mu_opioid_receptor_antagonism
- beta_adrenergic_receptor_blockade
- d2_receptor_antagonism
- at1_receptor_blockade
- glp1_receptor_agonism
- dopamine_receptor_agonism
- serotonin_1b_1d_receptor_agonism
- cgrp_receptor_antagonism
- h1_receptor_antagonism
- h2_receptor_antagonism
- beta2_adrenergic_receptor_agonism
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
| beta-adrenergic receptor blockade | ADRB1, ADRB2 | beta-blockers | Heart_Failure, Essential_Hypertension, Atrial_Fibrillation (Glaucoma and Migraine were assessed and rejected; see the module's scope notes) |
| AT1 receptor blockade | AGTR1 | sartans, ARNI, sparsentan | Essential_Hypertension, Heart_Failure, IgA_Nephropathy (diabetic kidney disease has no entry yet; the module's renal evidence is the RENAAL trial in type 2 diabetic nephropathy) |
| mu-opioid receptor agonism | OPRM1 | opioid analgesics; antagonists/partial agonists for OUD | Opioid_Use_Disorder, Acute_Opioid_Poisoning |
| D2 receptor antagonism | DRD2 | antipsychotics, antiemetics | Schizophrenia, Bipolar_Disorder, Cannabis_Hyperemesis_Syndrome, Subacute_Delirium. The extrapyramidal arm is modelled inside the module rather than as a drug-induced parkinsonism conformer; tardive dyskinesia is deliberately out of scope — see the module's scope notes |
| dopamine receptor agonism | DRD2, DRD3 | dopamine agonists | Parkinsons_Disease, hyperprolactinemia |
| GLP-1 / GIP receptor agonism | GLP1R, GIPR | incretin mimetics | Type_2_Diabetes_Mellitus, Obesity |
| 5-HT1B/1D agonism | HTR1B, HTR1D | triptans | Migraine, Migraine_with_Aura. `Familial_Hemiplegic_Migraine` was assessed and rejected: its management is avoidance of vasoconstricting agents, and a disease that withholds a drug class is not an instance of that class's mechanism |
| CGRP receptor antagonism | CALCRL, RAMP1 | gepants, erenumab | Migraine, pseudotumor_cerebri. Scoped to receptor antagonism, so the peptide-directed antibodies are out; `Migraine_with_Aura` was assessed and rejected because its only CGRP treatment names no agent |
| H1 receptor antagonism | HRH1 | antihistamines | Urticaria, Alpha-gal_Syndrome. Two modules rather than one: see the Decisions below. `allergic rhinitis` was listed here as a candidate and has no dismech entry, so `Alpha-gal_Syndrome` was wired instead, which also keeps the module indication-independent |
| H2 receptor antagonism | HRH2 | H2 blockers | Gastroesophageal_Reflux_Disease. Scoped to H2 blockade, so the proton-pump inhibitors are out: they block the same terminal pump non-competitively and the H2RA mechanism is upstream of it |
| beta2 adrenergic receptor agonism | ADRB2 | SABA, LABA | Asthma, Thunderstorm_Asthma, Formaldehyde_Poisoning. Airway-scoped: the receptor's neuromuscular-transmission and potassium-shift effector chains are a separate question, below. `Chronic_Obstructive_Pulmonary_Disease` and `Cough_Variant_Asthma` were assessed and could not be wired -- each binds the generic `Bronchodilator` agent in one treatment covering both drug classes |
| muscarinic receptor antagonism (airway) | CHRM3 | SAMA, LAMA | Chronic_Obstructive_Pulmonary_Disease, Asthma -- but both candidate conformers are blocked by the same bundling as above: COPD's and `Cough_Variant_Asthma`'s single `Bronchodilators` treatment covers beta2 agonists and muscarinic antagonists together, so splitting those treatments is this module's prerequisite |
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
- [x] mu-opioid receptor agonism (first module; see above) — `mu_opioid_receptor_agonism` (#14453)
- [x] mu-opioid receptor antagonism — `mu_opioid_receptor_antagonism` (#14456)
- [x] beta-adrenergic receptor blockade — `beta_adrenergic_receptor_blockade` (#15087)
- [ ] GLP-1 receptor agonism — `glp1_receptor_agonism` (#15252, in review)
- [ ] GPCR loss-of-function hormone resistance
- [ ] GPCR constitutive activation

### Phase 2 — conformers and remaining modules
- [ ] Add `conforms_to` on the treatment-linked pathophysiology nodes of the
      candidate conformers above
  - [x] The four opioid-treated entries, in #14973: `Opioid_Use_Disorder` and
        `Acute_Opioid_Poisoning` against both mu-opioid modules, `Acute_Post-Surgical_Pain`
        against agonism, `Alcohol_Use_Disorder` against antagonism
  - [x] Three beta-blocker-treated entries, in #15087: `Heart_Failure`,
        `Essential_Hypertension` and `Atrial_Fibrillation` against
        `beta_adrenergic_receptor_blockade`. `Migraine` and `Glaucoma` are deliberately
        not wired — see that module's scope notes
  - [x] Four antipsychotic-treated entries, in #15299: `Schizophrenia`, `Bipolar_Disorder`,
        `Cannabis_Hyperemesis_Syndrome` and `Subacute_Delirium` against
        `d2_receptor_antagonism`. The four span three indications — psychosis/mania, antiemesis
        and agitation — which is the point: one receptor action, three reasons to prescribe.
        `Schizophrenia` keeps its dopamine-dysregulation target alongside the receptor node,
        because D2 blockade acts downstream of that presynaptic abnormality
  - [x] Three angiotensin-blocker-treated entries, in #15271: `Essential_Hypertension`,
        `Heart_Failure` and `IgA_Nephropathy` against `at1_receptor_blockade`.
        `Essential_Hypertension`'s ACE inhibitor is pointed at its own
        renin-angiotensin-aldosterone node instead, because an ACE inhibitor never
        occupies the receptor — see that module's scope notes
  - [x] Two incretin-treated entries, in #15252: `Type_2_Diabetes_Mellitus`
        and `Obesity` against `glp1_receptor_agonism`, both at the receptor step. The
        module names no dominant weight-loss arm, so conforming `Obesity` against one
        would assert more than the evidence carries
  - [x] Three dopamine-agonist-treated entries, in #15350: `Parkinsons_Disease`,
        `Restless_Legs_Syndrome` and `Peripartum_Cardiomyopathy` against
        `dopamine_receptor_agonism`. All three anchor without a `downstream` edge; the
        first two at the trigger, and `Peripartum_Cardiomyopathy` at the module's
        lactotroph node instead, because bromocriptine is given there for prolactin
        suppression rather than for striatal signalling
  - [x] Two triptan-treated entries, in #15470: `Migraine` and `Migraine_with_Aura`
        against `serotonin_1b_1d_receptor_agonism`, both at the trigger.
        `Familial_Hemiplegic_Migraine` is deliberately not wired — see that module's
        scope notes
  - [x] Two CGRP-antagonist-treated entries, in #15624: `Migraine`, through its named
        gepant treatment, and `pseudotumor_cerebri`, through its erenumab treatment.
        The second is not a migraine entry on purpose, so the module is
        indication-independent and both the small-molecule and the antibody route are
        exercised. `Migraine`'s anti-CGRP antibody treatment is left unwired because it
        bundles a receptor-directed agent with two peptide-directed ones
  - [x] Two antihistamine-treated entries, in #15686: `Urticaria` and
        `Alpha-gal_Syndrome` against `h1_receptor_antagonism`, both at the trigger.
        The second is not an urticaria entry on purpose, so the module is
        indication-independent. Four entries that bundle an H1 and an H2 agent into one
        treatment (`Mast_Cell_Activation_Syndrome`, `Maculopapular_Cutaneous_Mastocytosis`,
        `Systemic_Mastocytosis` and `Monoclonal_Mast_Cell_Activation_Syndrome`) are
        deliberately not wired: neither module can take them without asserting one
        receptor's action for the other receptor's drug, so splitting those treatments is
        the prerequisite
  - [x] One H2-blocker-treated entry, in #15689: `Gastroesophageal_Reflux_Disease`
        against `h2_receptor_antagonism`, at the trigger. Its existing H2 antagonist
        treatment was wired rather than a new one added
  - [x] Three beta2-agonist-treated entries, in #15706: `Asthma` (both its pre-existing
        short- and long-acting treatments wired to one node, since the receptor is the
        same and only the route and duration differ), `Thunderstorm_Asthma` and
        `Formaldehyde_Poisoning` against `beta2_adrenergic_receptor_agonism`, all at the
        trigger. The third is a toxicological entry rather than an airway disease, so the
        module is not tied to asthma; its link carries receptor-level evidence only,
        because that treatment's own notes record that no formaldehyde-specific efficacy
        publication exists. `Chronic_Obstructive_Pulmonary_Disease` and
        `Cough_Variant_Asthma` are deliberately not wired, and `Sulfur_Mustard_Poisoning`
        likewise: the first two bind the generic `Bronchodilator` agent in a treatment
        covering both airway drug classes, and the third's salmeterol sits in a bundled
        supportive-care treatment with no agent-level binding
- [ ] Remaining Workstream A modules
  - [x] D2 receptor antagonism — `d2_receptor_antagonism` (#15299)
  - [x] AT1 receptor blockade — `at1_receptor_blockade` (#15271)
  - [x] dopamine receptor agonism — `dopamine_receptor_agonism` (#15350)
  - [x] 5-HT1B/1D agonism — `serotonin_1b_1d_receptor_agonism` (#15470)
  - [x] CGRP receptor antagonism — `cgrp_receptor_antagonism` (#15624)
  - [x] H1 receptor antagonism — `h1_receptor_antagonism` (#15686)
  - [x] H2 receptor antagonism — `h2_receptor_antagonism` (#15689)
  - [x] beta2 adrenergic receptor agonism — `beta2_adrenergic_receptor_agonism` (#15706)
  - [ ] muscarinic receptor antagonism (airway)
  - [ ] CaSR positive allosteric modulation
  - [ ] S1P receptor modulation
  - [ ] P2Y12 receptor antagonism
  - [ ] V2 receptor antagonism
  - [ ] MC4R agonism
  - [ ] migraine neurovascular mechanism — a *disease* module, not a drug one, factoring
        the cortical spreading depolarization → trigeminovascular activation → central
        sensitization chain out of `Migraine`, `Migraine_with_Aura` and
        `Familial_Hemiplegic_Migraine`, which currently each re-derive it. Added from the
        resolution of the CGRP open question below
- [ ] Gs alpha defect module

## Decisions

- **Agonism and antagonism of the same receptor are separate modules** (decided
  2026-10-15), because their downstream consequence chains differ.
- **One receptor family plus one direction of pharmacological action makes one
  module** (decided 2026-10-25, generalizing the rule above). A module is never
  defined by an indication: conformers come from whatever diseases happen to be
  treated that way, not the reverse.
- **5-HT1B/1D agonism and CGRP receptor antagonism are two modules, not one**
  (decided 2026-10-25, resolving the open question below). Three reasons, in
  increasing order of weight. By the rule above, they are different receptors in
  opposite directions, so bundling them would bundle on shared indication. The
  triptan arm carries a vasoconstriction profile that the gepant arm exists
  specifically to avoid, so one module could not hold both adverse chains without
  contradicting itself. And the pharmacology review the CGRP module is grounded on
  ([PMID:34076887](https://pubmed.ncbi.nlm.nih.gov/34076887/), Garelja, Walker and Hay,
  *Br J Pharmacol* 2022) draws the line itself: it separates the drugs that bind the CGRP peptide from the
  receptor antagonists, and subdivides the latter into small molecules and one
  antibody antagonist. That third reason also settles where erenumab goes, which
  the first two left open, and it scopes `cgrp_receptor_antagonism` to receptor
  antagonism with the peptide-directed antibodies out.

  The question's premise was a false choice, and the answer is *both*: a migraine
  neurovascular **mechanism** module is a genuinely distinct third module, not a
  substitute for either drug module, and is now in the Workstream A queue above.
- **H1 and H2 antagonism are two modules, and so are airway beta2 agonism and
  muscarinic antagonism** (decided 2026-10-26). Both were single rows in the
  Workstream A table above, and both are now split, by the rule two entries up.
  H1 and H2 are different receptors on different cells with disjoint effector
  chains -- cutaneous vasodilatation, extravasation and itch against
  parietal-cell acid secretion -- and disjoint conformers; they share only the
  word *antihistamine*. The airway pair are different receptors in opposite
  directions, Gs-coupled relaxation against Gq blockade, sharing only that the
  two drug classes are often inhaled together.

  The queue table bundled on shared indication twice, which is the failure the
  rule above names, so a bundled row there should be read as a candidate for
  splitting rather than as a decision already taken.

## Deferred follow-ups

Items raised in review and deliberately not done at the time, recorded here so
they are not lost. None blocks anything.

- **Join the H1 anticholinergic node to the pathograph.** `Anticholinergic
  Effects of First-Generation Antihistamines` in `h1_receptor_antagonism` has no
  edges at all, which is deliberate: its effects are conventionally muscarinic,
  no cited abstract says so, and an edge from H1 occupancy would assert that
  blocking H1 causes thirst and tachycardia. The #15686 reviewer suggested a
  `target_mechanisms` link from the first-generation treatment instead, which
  asserts only that the agents cause them and rests on the sentence already
  cited. Not pushed because it would have reset an approval for a rendering
  improvement.
- **Drop ranitidine from `Gastroesophageal_Reflux_Disease`'s H2 treatment, or
  decide to keep it.** That treatment binds ranitidine while conforming to a
  module that leaves it unbound, because NDMA contamination led to recalls and
  registration suspensions
  ([PMID:35696227](https://pubmed.ncbi.nlm.nih.gov/35696227/)). The entry records
  the caveat and cites that source, but the roster is unchanged: removing an
  agent is a clinical-content decision and was another curator's call. Whoever
  takes it should also delete the trailing clause "Whether to drop it from the
  roster is a clinical-content decision and has not been made here", which
  describes a pull request rather than the treatment.
- **Split the four entries that bundle an H1 and an H2 antihistamine into one
  treatment.** Neither histamine module can take them without asserting one
  receptor's action for the other receptor's drug, so this is the prerequisite
  for conforming them. They do not all need the same work, because they bundle
  to different degrees:
    - `Mast_Cell_Activation_Syndrome` — `H1/H2 Antihistamines`, binding
      cetirizine and famotidine. Both agents are bound, so splitting the
      treatment in two is mechanical.
    - `Systemic_Mastocytosis` — `Anti-Mediator Symptomatic Therapy`, binding an
      H1 and an H2 receptor-antagonist class term plus cromoglicate and
      adrenaline. Four modalities in one treatment, not two.
    - `Maculopapular_Cutaneous_Mastocytosis` — `H1 and H2 Antihistamines`, whose
      name and description cover both but which binds only the H1 class term, so
      the H2 half is asserted in prose and nowhere else.
    - `Monoclonal_Mast_Cell_Activation_Syndrome` — `Anti-mediator Therapy`, which
      names H1 and H2 antagonists, anti-leukotrienes and stabilisers in its
      description and binds **no** agent at all. The hardest of the four, and the
      one a conformance pass would silently skip.
- **Correct the same count in both histamine modules' `notes`.** Both say three
  and both leave `Monoclonal_Mast_Cell_Activation_Syndrome` unnamed, but they
  word it differently, so a single search will not find both:
    - `h2_receptor_antagonism`: "Three entries bundle an H1 and an H2
      antihistamine into a single treatment (… and the related systemic
      mastocytosis entries)".
    - `h1_receptor_antagonism`: "Three further entries treat with H1 and H2
      antihistamines bundled into a single treatment (… and
      `Systemic_Mastocytosis`' relatives)" — vaguer still, since it names one
      entry and then gestures at unnamed relatives.

  There are four, listed in the bullet above. A `kb/` change, so it could not
  ride the `projects/`-only pull request that fixed this page.

## Open questions

- How should biased agonism (G protein vs arrestin, e.g. oliceridine) be
  represented — a node within the agonism module, or a hypothesis group?
- Should the peptide-directed anti-CGRP antibodies (fremanezumab, galcanezumab,
  eptinezumab) get a ligand-sequestration module of their own? They reduce
  signalling through the same receptor one step upstream, so such a module would
  share `cgrp_receptor_antagonism`'s effector chain — which is a reason to decide
  it deliberately rather than fold them in. `Migraine`'s anti-CGRP antibody
  treatment bundles one receptor-directed and two peptide-directed agents and
  wants splitting either way.
- **Is tissue a third scoping axis?** The rule above is one receptor family plus
  one direction of action. Beta2 agonism does not fit it: the corpus uses the
  class for three mechanistically disjoint purposes that share one trigger and
  one transducer and diverge only at the effector — airway smooth muscle
  relaxation (`Asthma`, `Thunderstorm_Asthma`, `Cough_Variant_Asthma`,
  `Formaldehyde_Poisoning`, `Sulfur_Mustard_Poisoning`); enhancing neuromuscular
  transmission (`Congenital_Myasthenic_Syndrome` and its `_6` and `_7` entries,
  `ALG2-Congenital_Disorder_of_Glycosylation`,
  `Combined_Oxidative_Phosphorylation_Deficiency_58`, `RYR1-Related_Myopathy`);
  and driving potassium intracellularly (`Hyperkalemic_Periodic_Paralysis`).
  `beta2_adrenergic_receptor_agonism` is scoped to the airway on this table's own
  wording plus the tissue-scoped precedent of
  `cardiac_camp_pka_calcium_handling` and `spinal_hsp90_opioid_enhancement`, and
  that scope does not settle the question. Either the other two chains become
  their own modules, or they become further effector arms off a shared trigger —
  in which case one module would serve about ten conformers instead of three.
  **MC4R and V2 have the same shape**, so this is worth deciding before either.
- **May a module PR split another entry's bundled treatment?** Three modules have
  now been blocked by one treatment covering two drug classes: the muscarinic
  module cannot take `Chronic_Obstructive_Pulmonary_Disease` or
  `Cough_Variant_Asthma` until their single `Bronchodilators` treatment is split,
  and both histamine modules are blocked the same way by the four bundled H1+H2
  antihistamine treatments listed under Deferred follow-ups. Splitting a bundled
  treatment is arguably a modelling fix rather than a clinical one — it separates
  two mechanisms without changing which agents are listed — but it is adjacent to
  changing an agent roster, which this project has treated as belonging to
  whoever curated the entry (see the ranitidine item under Deferred follow-ups).
  Deciding this unblocks the muscarinic module and several conformers.
