---
title: 'Toxicology NAMs Special Issue: Screened Methods and Where dismech Can Hold Them'
status: IN_PROGRESS
description: >-
  Paper-by-paper screen of the 2024 Toxicology New Approach Methodologies special
  issue, recording for each method what it measures, whether any dismech
  pathophysiology node its measurement bears on exists, and what is owed to the
  separate nams-registry. A method can be registry-worthy with no dismech home,
  so the two dispositions are recorded separately.
tags: [NAM, FRAMEWORK_ALIGNMENT, ENVIRONMENTAL_EXPOSURE, EVIDENCE, CROSSWALK]
---

# Toxicology NAMs Special Issue: Screened Methods and Where dismech Can Hold Them

The 2024 *Toxicology* special issue on New Approach Methodologies was screened
paper by paper. Seventeen papers were kept and each carries its own
`NAM mining:` issue; five were set aside and are listed in
[#16882](https://github.com/monarch-initiative/dismech/issues/16882).

## Two destinations, two sets of criteria

A screened paper has up to two dispositions, and they are independent:

- **The registry.** [`monarch-initiative/nams-registry`](https://github.com/monarch-initiative/nams-registry)
  holds one record per method, in `nams/<id>.yaml`, wrapping the method as a
  [NAMO](https://github.com/monarch-initiative/namo) model. Its criterion is
  that the thing is a New Approach Methodology.
- **dismech.** A dismech record is a `ModelMechanismLink` from a model to a
  *pathophysiology node*. Its criterion is therefore stricter: a mechanism node
  the method's measurement bears on has to exist in `kb/`.

The second criterion is the narrower one, so screening against dismech's needs
systematically under-nominates for the registry — the problem
[#16882](https://github.com/monarch-initiative/dismech/issues/16882) raises.
**A method with no dismech anchor is still a complete registry entry.** Record
the registry disposition either way, and record the absence of an anchor rather
than reaching for the nearest module.

## Assessed

### BPA analogues in 2D versus 3D SH-SY5Y — PMID:38211720

Sendra, Cavia-Saiz and Múñiz, *Toxicology* 502:153715. Issue
[#16868](https://github.com/monarch-initiative/dismech/issues/16868).

Hybrid open access under CC BY-NC-ND. The cached reference
(`references_cache/PMID_38211720.md`) is `abstract_only`: the paper is not in
PMC, and the publisher's open-access copy that Unpaywall reports for this DOI is
the graphical-abstract image, not the article. The full text is at
<https://riubu.ubu.es/bitstream/10259/9295/1/Sendra-toxicology_2024.pdf>. Any
`kb/` snippet citing this PMID can therefore only quote the abstract; the
statements below are read off the full text and quoted here, not in `kb/`.

**The two formats.** One cell line, ATCC HTB-11 SH-SY5Y human neuroblastoma,
differentiated identically in both formats — retinoic acid 5 µM for two days,
then PMA 80 nM for two days, with differentiation confirmed by anti-β-III-tubulin
immunofluorescence.

| | 2D monolayer | 3D spheroid |
|---|---|---|
| Format | flat-bottom 96-well, 30,000 cells/well | forced flotation, 9,000 cells/spheroid, 4% Methocel A4M, low-adhesion U-bottom |
| Role | comparator | the candidate method |
| Viability | MTT | MTT (spheroids disaggregated first) |
| ROS | DCFH-DA, **flow cytometry**, % of population positive | DCFH-DA, **fluorescence microscopy**, mean intensity over spheroid area |
| Cell cycle | DAPI flow cytometry, 1 µM only | DAPI flow cytometry after collagenase/TrypLE disaggregation, 1 µM only |
| Morphology | — | projected area by planimetry, plus a 96 h recovery arm |
| Scale observed | `CELLULAR` | `CELLULAR` |

Exposures were 24 h and 96 h across 2.5–160 µM, DMSO solvent control, etoposide
17 µM positive control, medium replaced every 48 h. The recovery arm exists only
in the 3D format: 96 h in medium without bisphenol.

`CELLULAR` is right for the endpoints the two formats share. Spheroid
morphology is the exception — projected area observes a multicellular structure,
and a link grounded on that readout alone would be `TISSUE`. The paper reads it
that way too, noting that a spheroid losing its shape would "lose the
representativeness of spheroids as an organ or tissue".

**What the comparison found.** The 2D format was the more sensitive one on
viability, and the two formats moved in *opposite directions* on ROS at the same
concentrations and times:

> The spheroids exposed to BPs tended to decrease in ROS levels, while the 2D
> model demonstrated significant increases in ROS levels (p < 0.05).

> different strategies to respond to the exposure to BPs was observed as there
> was an increase in ROS in the 2D model and a decrease in ROS in the 3D model
> at the same concentrations and sampling times

That direction split is the whole of the paper's "different mechanisms of ROS
production". **No pathway is identified.** The words Nrf2, Keap1 and
antioxidant do not appear in the paper; mitochondrial dysfunction and
epigenetic change appear only as properties of the SH-SY5Y line in the
discussion and in cited work by others. The ROS comparison is also measured by
two different instruments reporting two different quantities — per-cell
positivity by flow cytometry in 2D against mean field intensity by microscopy in
3D — so some of the direction difference is attributable to the readout rather
than to the cells.

**Recovery is dissociated between endpoints, and that matters more than the
dose range.** The abstract compresses the recovery arm to spheroids at 2.5–40 µM
recovering "cell viability and the morphology". The results and discussion do
not support the second half for most analogues:

> Although cell viability was recovered in most cases, the spheroids could not
> maintain their morphology.

> the recovery of the area only occurred for doses from 2.5–40 µM for BPs such
> as BPFL, BPAP and BPAF. However, at higher doses the structure was lost.

Only BPA and BPC recovered area relative to controls; for the others, recovery
is an increase relative to their own 96 h exposed state, and spheroids exposed
to the highest concentrations of BPAP, BPAF and BPFL disintegrated. The paper's
own reading is that "replication and proliferation were recovered, while the
mechanisms responsible for maintaining the morphology of the spheroids could be
negatively affected by previous chronic exposure".

So this is not one reversible injury but a partly reversible one, reversible on
the proliferation endpoint and not on the structural endpoint. Whatever
[#16886](https://github.com/monarch-initiative/dismech/issues/16886) settles on
has to be able to say that; a single flag on the model or the node cannot, and a
`direction: RESTORED` readout would be true of viability and false of
morphology in the same arm.

**Potency.** The conclusions state that BPFL, BPAF, BPAP and BPC were more toxic
than BPS and BPA, and that BPS was the only analogue less potent than BPA
itself. The ordering within that group is given as BPFL > BPAF > BPAP > BPC for
the 2D format at 96 h but as BPFL > BPAF > BPAP < BPC for the 3D format, so it
is not one ranking that holds across formats.

**Genotoxicity.** The title claims genotoxic effects; no genotoxicity assay was
run. Cell cycle is the sole proxy — "Exposure to these BPs not only provoked
cytotoxicity but also genotoxicity, which was studied by analysing the cell
cycle" — and it was measured at 1 µM only, because 2.5 µM already moved the
other endpoints. The cell-cycle data therefore cannot be read alongside the
viability and ROS dose-responses.

**dismech disposition: no anchor, no record.** Nothing in `kb/` covers
bisphenol neurotoxicity. Bisphenol A appears only as a `Gestational bisphenol A
exposure` environmental entry on `Preeclampsia` and
`Gestational_Diabetes_Mellitus`, neither of which is this mechanism.
`keap1_nrf2_are_signaling` is excluded by the paper never reporting pathway
involvement, and `mitochondrial_dysfunction` and `epigenetic_alterations` by the
same test. `xenobiotic_oxidative_phosphorylation_blockade` is scoped to acute
poisoning of ATP synthesis and measures none of these endpoints. The paper
supplies no mechanism chain of its own: its causal content is a dose, a
direction and a viability loss.

**Registry disposition: both formats qualify**, and the record's value is the
paired comparison — same line, same differentiation protocol, opposite ROS
direction — together with the two limitations above, the readout-modality
confound and the endpoint-dissociated recovery.

## Not yet assessed

Read as a queue, not as findings: each row is its issue's subject line, and
nothing in it has been checked against the paper.

| Issue | PMID | Subject |
|---|---|---|
| [#16858](https://github.com/monarch-initiative/dismech/issues/16858) | 37863466 | 1,3-dichloropropene nasal epithelium, repeated exposure |
| [#16859](https://github.com/monarch-initiative/dismech/issues/16859) | 38013136 | Calu-3 air-liquid-interface 3D lung model, aerosol exposure |
| [#16861](https://github.com/monarch-initiative/dismech/issues/16861) | 38740170 | 3D quadruple co-culture liver spheroid for DILI prediction |
| [#16863](https://github.com/monarch-initiative/dismech/issues/16863) | 38341018 | 3D Nrf2 reporter epidermis for skin sensitization |
| [#16864](https://github.com/monarch-initiative/dismech/issues/16864) | 38040083 | AOP-based combined pesticide neurotoxicity, with synergy |
| [#16865](https://github.com/monarch-initiative/dismech/issues/16865) | 38360295 | respiratory sensitizer biomarkers in non-immune airway cells |
| [#16866](https://github.com/monarch-initiative/dismech/issues/16866) | 38369009 | 3D tetraculture bronchial model for respiratory sensitization |
| [#16867](https://github.com/monarch-initiative/dismech/issues/16867) | 38428665 | carboxylic acid hepatotoxicity, lipid accumulation patterns |
| [#16869](https://github.com/monarch-initiative/dismech/issues/16869) | 38788893 | microelectrode array neural network assays |
| [#16870](https://github.com/monarch-initiative/dismech/issues/16870) | 38580097 | PFOS endocrine disruption via AOP network and NAMs |
| [#16871](https://github.com/monarch-initiative/dismech/issues/16871) | 38029956 | ReproTracker hiPSC developmental toxicity with PBPK extrapolation |
| [#16872](https://github.com/monarch-initiative/dismech/issues/16872) | 38029955 | particulate matter on skin, ocular and lung co-culture systems |
| [#16873](https://github.com/monarch-initiative/dismech/issues/16873) | 38614204 | heated tobacco product in vitro toxicology, EpiAirway tissues |
| [#16874](https://github.com/monarch-initiative/dismech/issues/16874) | 38036094 | zearalenone estrogenicity and aromatase genetic variability |
| [#16875](https://github.com/monarch-initiative/dismech/issues/16875) | 38432407 | ochratoxin A molecular targets, OGFOD1 |
| [#16876](https://github.com/monarch-initiative/dismech/issues/16876) | 38272384 | P-glycoprotein (ABCB1) dynamics by molecular dynamics simulation |

Three of these are also 3D-versus-conventional comparisons (#16859, #16861,
#16866), so the readout-modality confound recorded above is worth checking in
each: a format comparison is only as good as the endpoint being measured the
same way in both arms.

## Set aside, and why that is itself a finding

Per [#16882](https://github.com/monarch-initiative/dismech/issues/16882), five
papers were screened out as having nothing a dismech pathograph node can attach
to — PMID:37993082 (read-across mutagenicity), PMID:38043774 (high-throughput
transcriptomic points of departure), PMID:38056590 (nanoparticle toxicity by
machine learning), PMID:38705560 (q-RASAR subchronic oral NOAEL) and
PMID:38719068 (in vitro true-dose workflow). Each predicts or conditions an
apical endpoint or a dose metric without asserting a mechanism.

They are not marginal methods. High-throughput transcriptomics is an
EPA-authored flagship regulatory approach. They were set aside by dismech's
criterion alone, which is the case for screening against the registry's broader
criterion first.

## Cross-cutting gaps

| Gap | Status |
|---|---|
| Nothing records that an injury resolves once exposure stops | [#16886](https://github.com/monarch-initiative/dismech/issues/16886). PMID:38211720 sharpens it: recovery was endpoint-dissociated, so the slot has to be per-endpoint |
| A method can belong in the registry with no dismech home | [#16882](https://github.com/monarch-initiative/dismech/issues/16882) |
| No module or entry covers bisphenol, or endocrine-disruptor, neurotoxicity | Not filed. Blocks every dismech record for PMID:38211720, and a module would need a mechanism chain that this paper does not supply |
| An immortalised tumour line standing in for a neuron | Not filed. `ModelDivergenceTypeEnum` has no value for a cell-identity substitution; `PROXY_QUANTITY` describes a stand-in quantity and `POPULATION_MISMATCH` a human population, and neither is a cell type standing in for another cell type. The paper states the problem itself: the line "derives from a tumour and therefore contains genetic peculiarities that can, potentially, alter the expected response of the cells" |
