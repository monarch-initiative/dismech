---
title: 'NAMs Special Issue: Model-to-Mechanism Mining'
status: IN_PROGRESS
description: >-
  Screening the Toxicology special issue "New approach methodologies: from conceptual
  development to regulatory application" for papers that pair a named measurement model
  with a mechanism in a human-relevant biological system, so each one can be mined by
  deep research into nams-registry report rows and dismech pathograph model links.
tags: [MODELS, NAM, EXTERNAL_COLLABORATION, ENVIRONMENTAL_EXPOSURE, EVIDENCE]
modules:
  - chemical_respiratory_allergy
  - inhaled_irritant_airway_injury
  - keap1_nrf2_are_signaling
  - drug_induced_liver_injury
  - hepatic_steatosis_lipotoxicity
  - cholestatic_liver_injury
  - fibrotic_response
  - mitochondrial_dysfunction
  - disabled_macroautophagy
  - epithelial_barrier_dysfunction
  - hypothyroidism_thyroid_hormone_deficiency
  - sex_steroid_driven_proliferation
---

# NAMs Special Issue: Model-to-Mechanism Mining

## Goal

The *Toxicology* special issue "New approach methodologies: from conceptual development
to regulatory application" collects New Approach Methodology papers across in vitro,
in silico, and AOP-based approaches. Each paper that reports both a measurement or
simulation model and a mechanism it bears on is a candidate for two destinations at
once:

1. a report row in [nams-registry](https://github.com/monarch-initiative/nams-registry),
   describing the method; and
2. a `ModelMechanismLink` on a dismech pathograph node, describing what the method
   measures and how faithfully.

Extraction is done by deep research (OpenScientist) per paper, driven from a GitHub
issue that states what to look for. This page tracks which papers were screened in,
which were screened out, and why.

## Screening rule

A paper is screened in when its abstract indicates **both** a named model and a
mechanism in a human-relevant biological system. Model organisms count — zebrafish and
*C. elegans* are in scope. Papers whose endpoint is purely ecotoxicological are out.
Papers whose only output is a statistical or structure-based prediction of a toxicity
label, with no mechanism and no biological system, are also out: there is nothing for a
pathograph node to attach to, however useful the method is as a method. Several
borderline calls are recorded in
[open-questions.md](NAMS_SPECIAL_ISSUE/open-questions.md) rather than settled here.

Screening is from abstracts only. A screened-in paper's listed mechanisms and models are
expectations to be verified against the full text during extraction, not curated content.

## Screened in

| Paper | PMID | System | Issue |
|---|---|---|---|
| 1,3-dichloropropene, 5-day repeated nasal exposure | 37863466 | MucilAir nasal ALI | [#16858](https://github.com/monarch-initiative/dismech/issues/16858) |
| Calu-3 ALI 3D lung model, aerosol exposure | 38013136 | Calu-3 ALI | [#16859](https://github.com/monarch-initiative/dismech/issues/16859) |
| ReproTracker developmental toxicity with PBPK | 38029956 | hiPSC | [#16871](https://github.com/monarch-initiative/dismech/issues/16871) |
| Particulate matter on skin, ocular, lung systems | 38029955 | multi-tissue co-culture | [#16872](https://github.com/monarch-initiative/dismech/issues/16872) |
| Zearalenone estrogenicity and aromatase variants | 38036094 | in silico, human CYP19A1 | [#16874](https://github.com/monarch-initiative/dismech/issues/16874) |
| AOP-based pesticide combined neurotoxicity | 38040083 | mammalian neuronal cells | [#16864](https://github.com/monarch-initiative/dismech/issues/16864) |
| BPA analogues, 2D vs 3D neuron model | 38211720 | SH-SY5Y 2D and spheroid | [#16868](https://github.com/monarch-initiative/dismech/issues/16868) |
| P-glycoprotein dynamics, molecular dynamics | 38272384 | in silico, human ABCB1 | [#16876](https://github.com/monarch-initiative/dismech/issues/16876) |
| 3D Nrf2 reporter epidermis, skin sensitization | 38341018 | Ker-CT 3D epidermis | [#16863](https://github.com/monarch-initiative/dismech/issues/16863) |
| Respiratory sensitizer biomarkers, airway cells | 38360295 | BEAS-2B, MRC-5, EA.hy926 | [#16865](https://github.com/monarch-initiative/dismech/issues/16865) |
| 3D tetraculture bronchial model | 38369009 | 4-cell bronchial | [#16866](https://github.com/monarch-initiative/dismech/issues/16866) |
| Carboxylic acid hepatotoxicity | 38428665 | hepatocytes, HCS | [#16867](https://github.com/monarch-initiative/dismech/issues/16867) |
| Ochratoxin A molecular targets | 38432407 | in silico | [#16875](https://github.com/monarch-initiative/dismech/issues/16875) |
| PFOS endocrine disruption via AOP and NAMs | 38580097 | AOP network | [#16870](https://github.com/monarch-initiative/dismech/issues/16870) |
| Heated tobacco product in vitro evaluation | 38614204 | EpiAirway 3D | [#16873](https://github.com/monarch-initiative/dismech/issues/16873) |
| 3D quadruple co-culture liver spheroid | 38740170 | 4-cell liver spheroid | [#16861](https://github.com/monarch-initiative/dismech/issues/16861) |
| Neural network activity, microelectrode arrays | 38788893 | rat cortical networks | [#16869](https://github.com/monarch-initiative/dismech/issues/16869) |

## Screened out

| Paper | PMID | Reason |
|---|---|---|
| QSAR for mercury | 37924932 | Aquatic ecotoxicology; reports a data gap rather than a working model |
| Read-across mutagenicity classification | 37993082 | Cheminformatics over an Ames dataset; no biological system, no mechanism |
| Nanoparticle toxicity by machine learning | 38056590 | Learns cell death from physicochemical properties and exposure conditions |
| Deep learning for prospective chemical hazards | 38104655 | Generates candidate hazardous structures; no mechanism in a system |
| In vitro transcriptomic points of departure (HTTr) | 38043774 | Endpoint is a dose metric, not a mechanism; flagship NAM, so a strong registry candidate |
| q-RASAR for subchronic oral NOAEL | 38705560 | Structure-based prediction of a rat apical endpoint |
| True-dose workflow for in vitro testing | 38719068 | In vitro dosimetry workflow; no mechanism |
| NGRA for occupational safety, sodium isethionate | 38857863 | Exposure and bioactivity-ratio workflow across a NAM battery |

Five of the eight are recorded in the open-questions register: they are strong
registry candidates with no dismech home, which is a different thing from being out of
scope for the registry too.

## Where extraction output goes

- **Registry report** — one row per model-to-mechanism pairing, with the paper's own
  wording behind each row.
- **dismech** — a `ModelMechanismLink` under `experimental_models:`, `animal_models:`,
  or `computational_models:` on the entry or module whose node the mechanism matches,
  carrying `relationship`, `fidelity`, `model_scale`, `readouts`, and a typed
  `divergences` entry where the model cannot observe what it is cited for.
- **Unmapped inventory** — a pairing with no matching dismech node is recorded in
  [open-questions.md](NAMS_SPECIAL_ISSUE/open-questions.md) with the kind of node it
  would need. The two largest gaps the abstracts revealed are now closed: the
  modules `inhaled_irritant_airway_injury` and `chemical_respiratory_allergy` were
  built for dismech#16877 and dismech#16878, so the seven papers that needed them
  have a conformance target.
