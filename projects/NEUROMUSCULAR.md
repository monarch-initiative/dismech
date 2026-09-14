---
title: Neuromuscular Disease Curation Project
status: PLANNED
description: >-
  Build out the neuromuscular branch of dismech along the four compartments of
  the motor unit. The knowledge base already holds ~69 neuromuscular entries but
  has no muscle-side mechanism module at all, so most myopathies, dystrophies,
  channelopathies, and neuromuscular junction disorders are curated as isolated
  pathographs with nothing shared between them.
tags: [DISEASE_DOMAIN, NEUROMUSCULAR, MODULE_BUILDOUT, MONDO_ALIGNMENT]
diseases:
- Amyotrophic_Lateral_Sclerosis
- Botulism
- Central_Core_Myopathy
- Congenital_Myasthenic_Syndrome
- Dermatomyositis
- Duchenne_Muscular_Dystrophy
- Dystroglycanopathy
- Emery_Dreifuss_Muscular_Dystrophy
- Facioscapulohumeral_Muscular_Dystrophy
- Hypokalemic_Periodic_Paralysis
- Inclusion_Body_Myositis
- Malignant_Hyperthermia_of_Anesthesia
- Multiminicore_Disease
- Myasthenia_Gravis
- Myotonic_Dystrophy_Type_1
- Nemaline_Myopathy
- Pompe_Disease
- Postpoliomyelitis_Syndrome
- Spinal_Muscular_Atrophy
- Thomsen_and_Becker_disease
modules:
- peripheral_axonal_degeneration
- synaptic_vesicle_cycle
- glutamate_excitotoxicity
- tdp43_proteinopathy
- antisense_oligonucleotide_therapy
- fibrotic_response
groupings:
- Motor_Neuron_Disorders
- Charcot-Marie-Tooth_Diseases
---

# Neuromuscular Disease Curation Project

Tracking epic: [monarch-initiative/dismech#9005](https://github.com/monarch-initiative/dismech/issues/9005)

## Overview

Neuromuscular disease is organized around the **motor unit**: lower motor neuron
→ peripheral nerve → neuromuscular junction (NMJ) → muscle fiber. Each
compartment fails in its own characteristic way, and the classification that the
Mondo neuromuscular workshop is converging on — classify by *affected structure*
rather than by etiology, because the causes (genetic, autoimmune, toxic,
infectious, metabolic, paraneoplastic, degenerative) are too varied to
partition cleanly — is exactly the classification dismech should mirror in its
mechanism modules.

This project has two aims:

1. **Fill the module layer.** Give each motor-unit compartment at least one
   conserved mechanism module, so that entries that currently share nothing can
   declare `conforms_to` against a common trunk.
2. **Record what is genuinely unresolved.** Several of the most-cited mechanisms
   in this field are contested or rest on model systems that do not reproduce the
   human phenotype. Those belong in `mechanistic_hypotheses` and
   `HUMAN_MODEL_MISMATCH` discussions rather than being flattened into a single
   confident causal chain.

## Current state of the knowledge base

Counted over `kb/disorders/` (69 entries matching neuromuscular naming patterns,
excluding retinal/corneal dystrophies, leukodystrophies, cardiomyopathies, and
rhabdomyosarcomas):

| | count |
|---|---|
| Neuromuscular disorder entries | 69 |
| Declaring **any** `conforms_to` | 19 |
| Declaring **no** module conformance | **50** |

The 19 that do conform reach the module layer almost entirely through the
**nerve** and **motor neuron** compartments — `peripheral_axonal_degeneration`
(the Charcot-Marie-Tooth and inflammatory neuropathy entries),
`tdp43_proteinopathy` / `glutamate_excitotoxicity` / `disabled_macroautophagy`
(ALS), plus a handful reached incidentally
(`lysosomal_substrate_accumulation` for Pompe,
`molecular_mimicry_autoimmunity` for Guillain-Barré,
`antisense_oligonucleotide_therapy` for Duchenne).

**There is no muscle-side mechanism module in the repository.** Of the 123
modules in `kb/modules/`, none models sarcolemmal integrity, excitation-contraction
coupling, sarcomere assembly, skeletal-muscle excitability, myofiber necrosis, or
endplate transmission. The consequence is visible in the orphan list:
`Spinal_Muscular_Atrophy`, `Myasthenia_Gravis`, `Congenital_Myasthenic_Syndrome`,
`Myotonic_Dystrophy_Type_1`, `Nemaline_Myopathy`, `Central_Core_Myopathy`,
`Malignant_Hyperthermia_of_Anesthesia`, `Dermatomyositis`,
`Facioscapulohumeral_Muscular_Dystrophy`, and
`Emery_Dreifuss_Muscular_Dystrophy` all carry zero module conformance.

The one partial exception is presynaptic transmission: `synaptic_vesicle_cycle`
already names presynaptic congenital myasthenic syndrome in scope and covers
UNC13A, SNAP25, SYT2, and VAMP1. It is explicitly and deliberately presynaptic,
so the postsynaptic and synaptic-basal-lamina arms of the NMJ have no home.

## Proposed modules

Tier 1 gives each motor-unit compartment a trunk and mirrors the four-way Mondo
split (motor neuron disorder / peripheral neuropathy / NMJ disease / myopathy).
Tier 2 covers well-bounded mechanisms with several ready conformers each.

### Tier 1

#### 1. `sarcolemmal_mechanical_fragility` — the muscular dystrophy trunk

Loss of a dystrophin-glycoprotein complex (DGC), membrane-repair, or
sarcolemma-ECM linkage component → loss of mechanical coupling between the
cortical cytoskeleton and the basal lamina → contraction-induced (particularly
eccentric) sarcolemmal injury with Ca²⁺ influx → calpain activation,
mitochondrial Ca²⁺ overload, and myofiber necrosis → regenerative exhaustion of
the satellite cell pool → fibro-fatty replacement and progressive weakness. The
terminal step feeds the existing `fibrotic_response` module.

Ready conformers: `Duchenne_Muscular_Dystrophy` (which currently reaches the
module layer only through its exon-skipping treatment),
`Autosomal_Recessive_Limb-Girdle_Muscular_Dystrophy`,
`Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant`,
`Ullrich_Congenital_Muscular_Dystrophy` and `Bethlem_Myopathy` (the COL6
extracellular arm), `Dystroglycanopathy` (whose muscle arm is unmodeled — the
entry currently conforms only to the brain-side
`pial_basement_membrane_radial_glial_endfoot_failure`).

This is the highest-value single module in the project. It should carry the
mechanical-fragility vs mechanotransduction controversy as competing
`mechanistic_hypotheses` (see below) rather than asserting either.

#### 2. `neuromuscular_transmission_failure` — the NMJ trunk

An endplate lesion (postsynaptic AChR subunit or clustering-pathway defect,
synaptic basal lamina / acetylcholinesterase anchoring defect, or presynaptic
release failure) → reduction in the **safety factor of neuromuscular
transmission** → intermittent failure of endplate potentials to reach threshold
→ transmission block at a growing fraction of endplates → fatigable weakness.

The safety factor is the organizing quantity: normally 3–5 in adult mammals, and
the thing that every CMS mechanism erodes, whether by reducing quantal content,
reducing AChR number, altering endplate geometry, or desensitizing AChR through
ACh overexposure ([Engel et al., PMC6032286](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6032286/)).
Postsynaptic and endplate-development/maintenance defects account for roughly
77% of CMS cases, and ~40 CMS genes are now reported.

Three etiologic entry arms, matching the workshop deck's proposed NMJ split:

- **genetic** — congenital myasthenic syndromes
- **autoimmune** — myasthenia gravis (AChR / MuSK / LRP4), Lambert-Eaton
- **toxin** — botulinum toxin, α-neurotoxin envenomation, tick paralysis

Ready conformers: `Myasthenia_Gravis`, `Congenital_Myasthenic_Syndrome`,
`Congenital_Myasthenic_Syndrome_6`, `Botulism`. Carries the
acetylcholinesterase-inhibitor drug pattern (pyridostigmine `target_mechanisms`
on the transmission node) and the 3,4-diaminopyridine presynaptic pattern.

Deliberately complementary to `synaptic_vesicle_cycle`, which stays the home for
the presynaptic release machinery itself; this module models the endplate and the
safety-factor consequence.

#### 3. `sarcolemmal_excitability_channelopathy` — the muscle channelopathy trunk

The skeletal-muscle counterpart of the existing (and explicitly cardiac)
`cardiac_ion_channel_repolarization`. Skeletal muscle ion channel variant (CLCN1
/ ClC-1, SCN4A / NaV1.4, CACNA1S / CaV1.1, KCNJ2 / Kir2.1) → altered sarcolemmal
and t-tubular resting potential or action-potential behavior → two mutually
exclusive branches:

- **hyperexcitable** — reduced chloride conductance or impaired Na⁺ channel
  inactivation → repetitive after-discharges → **myotonia** (delayed relaxation)
- **inexcitable** — sustained depolarization → NaV1.4 inactivation → loss of
  action potential generation → **flaccid periodic paralysis**

Ready conformers: `Thomsen_and_Becker_disease` (CLCN1),
`Hypokalemic_Periodic_Paralysis`, `Andersen-Tawil_Syndrome` (which currently sits
on the cardiac side only).

This module is the direct dismech counterpart of the deck's proposal to give
`muscular channelopathy` (MONDO:0019119) a real definition and reclassify it
under `myopathy`.

#### 4. `denervation_reinnervation_remodeling` — the motor unit trunk

Distinct from `peripheral_axonal_degeneration`, which models *length-dependent
sensory-and-motor* distal axonopathy. This one models the motor unit as a unit:
motor neuron or motor axon loss → NMJ denervation → collateral sprouting from
surviving axons and reinnervation of orphaned fibers → motor unit enlargement
with fiber-type grouping → eventual exhaustion of sprouting capacity →
neurogenic atrophy and weakness.

Ready conformers: `Postpoliomyelitis_Syndrome` (the paradigm case — decades of
compensated reinnervation followed by late failure), `Progressive_Muscular_Atrophy`,
`Monomelic_Amyotrophy`, `Spinal_Muscular_Atrophy`, `Kennedy_Disease`,
`Amyotrophic_Lateral_Sclerosis`, `Madras_Motor_Neuron_Disease`.

Fills the Mondo deck's motor-neuron section, which is currently a stub
("Add content from discussion on 2026-08-13").

### Tier 2

#### 5. `excitation_contraction_coupling_calcium_release`

RYR1 / CACNA1S / STAC3 defect at the triad → dysregulated sarcoplasmic reticulum
Ca²⁺ release, with two branches: **reduced or uncoupled release** producing
core formation and congenital weakness, and **hypersensitive release** under
volatile anaesthetic or succinylcholine producing uncontrolled Ca²⁺ efflux,
hypermetabolic crisis, and rhabdomyolysis.

Ready conformers: `Central_Core_Myopathy`, `Multiminicore_Disease`,
`Malignant_Hyperthermia_of_Anesthesia` — three entries that today share the same
gene and none of the same graph. Carries the dantrolene `target_mechanisms`
(`INHIBITS`) pattern on the Ca²⁺-release node.

#### 6. `rna_repeat_spliceopathy`

Expanded CUG (DM1) or CCUG (DM2) repeat transcribed but retained → nuclear
ribonuclear foci → MBNL protein sequestration with reciprocal CELF1 stabilization
→ reversion of alternative splicing to fetal patterns across dozens of
transcripts → the multisystem DM phenotype, with individual features traceable to
individual mis-splicing events (CLCN1 → myotonia, which links this module to
module 3; INSR → insulin resistance; BIN1 → t-tubule disorganization).

Ready conformers: `Myotonic_Dystrophy_Type_1`; DM2 is not yet in the KB.

Distinct from `fame_pentanucleotide_repeat_rna_toxicity`, which is deliberately
conservative about intronic TTTCA repeat RNA and makes no spliceopathy claim, and
from `polyglutamine_expansion_proteotoxicity`, which acts at the protein level.

#### 7. `sarcomere_thin_filament_assembly`

Sarcomeric or Z-disk protein defect (ACTA1, NEB, TPM2/TPM3, TNNT1; DES, CRYAB;
TTN) → impaired thin-filament or Z-disk assembly and stability → pathological
protein aggregation (nemaline rods, myofibrillar inclusions) → reduced specific
force → congenital hypotonia and weakness. A candidate **Xogenesis** module —
nemaline rod bodies are a formed pathological structure with an MPATH/OGMS anchor.

Ready conformers: `Nemaline_Myopathy`, `Myofibrillar_Myopathy`,
`TTN_Related_Myopathy_Dominant_Negative_TTNsv`,
`Distal_Myopathy_6_Adult-Onset_Autosomal_Dominant`.

#### 8. `immune_mediated_myofiber_injury`

Three mechanistically distinct arms under one autoimmune-myopathy trunk, which is
why the current lumping into "myositis" loses information:

- **dermatomyositis** — type I interferon signature plus complement membrane-attack
  complex on endomysial capillaries → capillary dropout → perifascicular atrophy
  (a microangiopathy, not primarily a myofiber-directed attack)
- **polymyositis / inclusion body myositis** — myofiber MHC class I upregulation →
  CD8⁺ cytotoxic T cell invasion of non-necrotic fibers
- **immune-mediated necrotizing myopathy** — anti-HMGCR or anti-SRP autoantibodies
  → myofiber necrosis with sparse cellular infiltrate (includes statin-associated
  autoimmune myopathy, which also makes this a treatment-toxicity module)

Ready conformers: `Dermatomyositis`, `Polymyositis`, `Inclusion_Body_Myositis`
(which already carries the degenerative arm via `cellular_senescence`).

#### 9. `muscle_energy_failure_rhabdomyolysis`

Block in glycogenolysis/glycolysis, fatty acid oxidation, or oxidative
phosphorylation → ATP deficit under a **workload pattern specific to the block**
(brief high-intensity for the glycogenoses; prolonged exertion, fasting, or
illness for FAO defects) → failure of SERCA and Na⁺/K⁺-ATPase to maintain ionic
gradients → Ca²⁺ dysregulation and myofiber necrosis → rhabdomyolysis,
myoglobinuria, and pigment nephropathy.

Ready conformers: `Glycogen_Storage_Disease_Type_V`,
`Glycogen_Storage_Disease_Type_VII`,
`Carnitine_Palmitoyltransferase_II_Deficiency`,
`Neutral_Lipid_Storage_Myopathy`, `MSTO1-Related_Mitochondrial_Myopathy`.

The workload-specificity is the mechanistically interesting part and is what
distinguishes the two exercise-intolerance phenotypes clinically.

### Tier 3 — proposed, decision needed

- **`nuclear_envelope_mechanotransduction`** (LMNA/EMD). Real cross-system reach
  (`Emery_Dreifuss_Muscular_Dystrophy`, `Familial_Partial_Lipodystrophy`,
  `Dilated_Cardiomyopathy`), but the unifying mechanism across those tissues is
  genuinely contested, which may make it premature.
- **`dux4_reactivation`** (FSHD). D4Z4 contraction or SMCHD1 loss → chromatin
  derepression → DUX4 expression in skeletal muscle → activation of an embryonic
  transcriptional program → myotoxicity. Mechanistically clean and a paradigm of
  epigenetic derepression, but currently one conformer
  (`Facioscapulohumeral_Muscular_Dystrophy`); may be better as disease-level
  curation until a second conformer exists.
- **`alpha_dystroglycan_matriglycan_glycosylation`**. Probably *not* a separate
  module: the muscle consequence is loss of laminin binding, i.e. exactly the
  linkage failure that module 1 models, and the enzymology is already partly
  served by `congenital_disorder_of_glycosylation`. Recommend modeling it as a
  substitution branch inside `sarcolemmal_mechanical_fragility`.
- **SMN / snRNP assembly**. Recommend *against* a module. A module should recur
  across disorders; SMN deficiency is essentially one disease. Curate at the
  `Spinal_Muscular_Atrophy` entry and route its muscle consequence through
  module 4.

## Knowledge gaps

These are the places where the field does not have a settled answer, and where
dismech's `mechanistic_hypotheses`, `KNOWLEDGE_GAP`, and `HUMAN_MODEL_MISMATCH`
machinery is the right way to record the state of knowledge instead of picking a
side.

### 1. Dystrophin: mechanical fragility or mechanotransduction?

The textbook account is that dystrophin is a shock absorber and its loss makes
the sarcolemma tear under eccentric contraction. The competing account is that
the DGC is primarily a **mechanotransduction and signaling hub**, and that much
of the pathology follows from disrupted signaling — notably nNOS mislocalization
producing functional ischemia during exercise — rather than from frank membrane
rupture ([Comms Biol 2022](https://www.nature.com/articles/s42003-022-03980-y)).
The distinction matters therapeutically: micro-dystrophin constructs that restore
mechanical linkage but omit the nNOS-binding domain test the two accounts
directly.

→ Curate as competing `mechanistic_hypotheses` on
`sarcolemmal_mechanical_fragility` (`mechanical_fragility_model` CANONICAL vs
`mechanotransduction_signaling_model` ALTERNATIVE), with disease-level edges
opting into groups.

### 2. ALS: dying-back or dying-forward?

NMJ denervation is among the earliest detectable events in ALS, and 2025 work
frames skeletal muscle as an **active participant** in degeneration rather than a
passive target, with NMJ regenerative capacity as a therapeutic axis
([bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.07.13.664600v1.full);
[State of the Art 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12266013/)).
Whether the primary lesion is in the motor neuron soma with distal consequence,
or at the periphery with retrograde consequence, is unresolved.

→ `mechanistic_hypotheses` on `Amyotrophic_Lateral_Sclerosis` and on
`denervation_reinnervation_remodeling`.

### 3. DM1: MBNL sequestration does not account for the whole phenotype

Mouse models reproduce substantially **less** splicing mis-regulation than is seen
in DM1 patient brain, and additional mechanisms — mRNA translation, localization,
and stability, repeat-associated non-AUG translation, CELF1 hyperphosphorylation
— are implicated but not quantified.

→ `HUMAN_MODEL_MISMATCH` discussion on `rna_repeat_spliceopathy`: evidence exists
in the model, translational validity to the human CNS phenotype is the open
question. This is precisely the distinction from a plain `KNOWLEDGE_GAP`.

### 4. Selective vulnerability is unexplained across the whole domain

Extraocular muscles are spared in Duchenne but preferentially targeted in
myasthenia gravis and mitochondrial myopathy. Cranial motor units differ in
vulnerability in ALS and SMA. There is a measurement trap here worth recording:
in the most vulnerable muscles there is underlying **loss of endplates**, which
can mask denervation on standard assays.

→ `KNOWLEDGE_GAP` discussions with `proposed_experiments`; the endplate-loss
caveat belongs in `limitations` on any model link that uses endplate occupancy as
a readout.

### 5. The safety factor is a model-system quantity

Neuromuscular transmission safety factor is the organizing concept for the whole
NMJ module, and it is measured in mouse and in intercostal biopsy — almost never
in a living patient, where the surrogate is repetitive nerve stimulation decrement.
The surrogate has not been validated against the underlying quantity across CMS
subtypes.

→ `KNOWLEDGE_GAP` on `neuromuscular_transmission_failure`, in the same spirit as
the DTI-ALPS imaging-surrogate caveat in `glymphatic_dysfunction`.

### 6. Post-therapy natural history is a new and unmodeled phenotype

Nusinersen- and onasemnogene-treated SMA, and exon-skipping-treated Duchenne, are
producing disease courses that no pre-therapy natural history describes. What
residual deficit remains, and which compartment it lives in, is open.

→ Worth an explicit `KNOWLEDGE_GAP` rather than silently curating pre-therapy
natural history as if it still applied.

### 7. NMJ aging and neuromuscular disease converge

The NMJ is a shared vulnerability of aging and disease, and biomarkers are
crossing over — neurofilament light is elevated in severe sarcopenia as well as in
motor neuron disease. This is a candidate link between this project and the
existing aging modules (`inflammaging`, `stem_cell_exhaustion`,
`cellular_senescence`).

### 8. Entry-level gaps in the knowledge base

Missing entries that would each unlock a module conformer:

| Missing entry | Would conform to |
|---|---|
| Lambert-Eaton myasthenic syndrome | `neuromuscular_transmission_failure` (presynaptic autoimmune arm) |
| Myotonic dystrophy type 2 | `rna_repeat_spliceopathy` (CCUG arm) |
| Immune-mediated necrotizing myopathy / statin-associated | `immune_mediated_myofiber_injury` |
| Paramyotonia congenita, hyperkalemic periodic paralysis | `sarcolemmal_excitability_channelopathy` |
| Sarcoglycanopathies, dysferlinopathy (LGMD R subtypes) | `sarcolemmal_mechanical_fragility` |
| Critical illness myopathy | `denervation_reinnervation_remodeling` + acquired arm |

### 9. Ontology-side gaps carried over from the Mondo workshop

Recorded here because they constrain what dismech can bind to, not because this
project owns them:

- No Mondo term for **toxin-induced neuromuscular junction disease** (proposed in
  the workshop deck to cover botulism, tetanus, tick paralysis, and envenomation).
- No Mondo terms for CMS associated with **UNC13A, RPH3A, LAMA5, MACF1, GMPPB**.
- No **`acquired neuromuscular disease`** counterpart to
  `hereditary neuromuscular disease` (MONDO:0100546); the workshop flags that
  there is no semantic basis on which to maintain such a class.
- `atrophic muscular disease` (MONDO:0004714) and `muscular channelopathy`
  (MONDO:0019119) are proposed to move under `myopathy`, and `myopathy`
  (MONDO:0005336) to become a direct child of `neuromuscular disease`.

## Proposed groupings

`kb/groupings/` currently holds `Motor_Neuron_Disorders` and
`Charcot-Marie-Tooth_Diseases` for this domain. Candidates to add, each with a
`CONFORMS_TO_MODULE` necessary criterion once the corresponding module exists:

- `Muscular_Dystrophies` → `sarcolemmal_mechanical_fragility`
- `Congenital_Myopathies` → `sarcomere_thin_filament_assembly` /
  `excitation_contraction_coupling_calcium_release`
- `Skeletal_Muscle_Channelopathies` → `sarcolemmal_excitability_channelopathy`
- `Neuromuscular_Junction_Disorders` → `neuromuscular_transmission_failure`
- `Idiopathic_Inflammatory_Myopathies` → `immune_mediated_myofiber_injury`

## Worklist

- [ ] Create `sarcolemmal_mechanical_fragility` module with competing mechanical /
      mechanotransduction hypotheses
- [ ] Create `neuromuscular_transmission_failure` module with the three etiologic
      arms and the safety-factor knowledge gap
- [ ] Create `sarcolemmal_excitability_channelopathy` module
- [ ] Create `denervation_reinnervation_remodeling` module
- [ ] Wire `Duchenne_Muscular_Dystrophy`, `Myasthenia_Gravis`,
      `Congenital_Myasthenic_Syndrome`, `Thomsen_and_Becker_disease`, and
      `Postpoliomyelitis_Syndrome` as the first conformers, one per Tier 1 module
- [ ] Create `excitation_contraction_coupling_calcium_release` and wire the three
      RYR1 entries
- [ ] Create `rna_repeat_spliceopathy` with the DM1 `HUMAN_MODEL_MISMATCH`
- [ ] Create `sarcomere_thin_filament_assembly` (evaluate Xogenesis anchor for
      nemaline rods)
- [ ] Create `immune_mediated_myofiber_injury` with the three-arm split
- [ ] Create `muscle_energy_failure_rhabdomyolysis`
- [ ] Decide Tier 3: laminopathy, DUX4, matriglycan-as-branch
- [ ] Add the six missing disorder entries listed under knowledge gap 8
- [ ] Add the five proposed groupings
