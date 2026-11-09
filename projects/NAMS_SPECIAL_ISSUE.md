---
title: 'Toxicology NAMs Special Issue: Screening Log'
status: IN_PROGRESS
description: >-
  The screening log for the Toxicology New Approach Methodologies special issue —
  which papers were kept, which issue carries each one, and which of the two
  destinations (the nams-registry or a dismech entry) each paper's methods belong in.
tags: [NAM, FRAMEWORK_ALIGNMENT, ENVIRONMENTAL_EXPOSURE, EXTERNAL_COLLABORATION]
modules:
  - epilepsy_excitation_inhibition_imbalance
---

# Toxicology NAMs Special Issue: Screening Log

The *Toxicology* special issue on New Approach Methodologies was screened paper by
paper for methods, mechanisms and gaps. Each paper kept by the screen has its own
issue; this page is the index over them, and the place where a per-paper
destination decision is recorded once it is made.

## Two destinations, and they are not the same screen

A paper from this issue can land in either of two places, and most land in only one:

- the [nams-registry](https://github.com/monarch-initiative/nams-registry), which
  catalogues a method as a method; or
- a dismech entry, which needs the method to attach to a **mechanism node**.

dismech links a model to a mechanism, so a method whose output is an apical
toxicity label, a dose metric, or an undifferentiated activity call has no dismech
anchor by construction — however well established the method is. Five papers were
set aside on exactly that ground, and whether the registry takes them is
[#16882](https://github.com/monarch-initiative/dismech/issues/16882), which also
records that screening both destinations through one filter under-nominates for the
registry.

That question is live for papers kept by the screen too, not only for the five
rejected ones: a kept paper can still turn out to support a registry entry and no
dismech link. The first such decision is recorded below.

## Screened in

Seventeen papers, one issue each. **The method and mechanism descriptions in these
issues were read off abstracts and are expectations, not verified content** — each
issue says so. Treat a row here as a pointer to the issue, not as a finding.

| PMID | Subject | Issue |
|---|---|---|
| 37863466 | 1,3-dichloropropene nasal epithelium, repeated exposure | [#16858](https://github.com/monarch-initiative/dismech/issues/16858) |
| 38013136 | Calu-3 air-liquid-interface 3D lung model, aerosol exposure | [#16859](https://github.com/monarch-initiative/dismech/issues/16859) |
| 38740170 | 3D quadruple co-culture liver spheroid for DILI prediction | [#16861](https://github.com/monarch-initiative/dismech/issues/16861) |
| 38341018 | 3D Nrf2 reporter epidermis for skin sensitization | [#16863](https://github.com/monarch-initiative/dismech/issues/16863) |
| 38040083 | AOP-based combined pesticide neurotoxicity, with synergy | [#16864](https://github.com/monarch-initiative/dismech/issues/16864) |
| 38360295 | Respiratory sensitizer biomarkers in non-immune airway cells | [#16865](https://github.com/monarch-initiative/dismech/issues/16865) |
| 38369009 | 3D tetraculture bronchial model for respiratory sensitization | [#16866](https://github.com/monarch-initiative/dismech/issues/16866) |
| 38428665 | Carboxylic acid hepatotoxicity, lipid accumulation patterns | [#16867](https://github.com/monarch-initiative/dismech/issues/16867) |
| 38211720 | BPA analogues in 2D vs 3D neuron models | [#16868](https://github.com/monarch-initiative/dismech/issues/16868) |
| 38788893 | Microelectrode array neural network assays, acute vs network formation | [#16869](https://github.com/monarch-initiative/dismech/issues/16869) |
| 38580097 | PFOS endocrine disruption via AOP network and NAMs | [#16870](https://github.com/monarch-initiative/dismech/issues/16870) |
| 38029956 | ReproTracker hiPSC developmental toxicity with PBPK extrapolation | [#16871](https://github.com/monarch-initiative/dismech/issues/16871) |
| 38029955 | Particulate matter on skin, ocular and lung co-culture systems | [#16872](https://github.com/monarch-initiative/dismech/issues/16872) |
| 38614204 | Heated tobacco product in vitro toxicology, EpiAirway tissues | [#16873](https://github.com/monarch-initiative/dismech/issues/16873) |
| 38036094 | Zearalenone estrogenicity and aromatase genetic variability | [#16874](https://github.com/monarch-initiative/dismech/issues/16874) |
| 38432407 | Ochratoxin A molecular targets, OGFOD1 | [#16875](https://github.com/monarch-initiative/dismech/issues/16875) |
| 38272384 | P-glycoprotein (ABCB1) dynamics by molecular dynamics simulation | [#16876](https://github.com/monarch-initiative/dismech/issues/16876) |

## Screened out as having no dismech anchor

PMID:37993082 (read-across mutagenicity classification), PMID:38043774 (in vitro
transcriptomic points of departure), PMID:38056590 (nanoparticle toxicity by
machine learning), PMID:38705560 (q-RASAR subchronic oral NOAEL) and
PMID:38719068 (an in vitro true-dose workflow). Each predicts or conditions a
toxicity endpoint without asserting a mechanism. Whether the registry takes them
is [#16882](https://github.com/monarch-initiative/dismech/issues/16882).

## Destination decisions

### PMID:38788893 — the two MEA neural network assays go to the registry only

Martin et al. 2024, *Toxicology* 505:153842 ([#16869](https://github.com/monarch-initiative/dismech/issues/16869)).
Two US EPA microelectrode-array assays in dissociated rat cortical cultures,
compared head to head across 243 chemicals.

| | MEA acute network function assay (AcN) | MEA network formation assay (NFA) |
|---|---|---|
| Exposure | "a 40-minute chemical exposure on day in vitro (DIV)13 or 15" | "a developmental exposure paradigm spanning DIV0 through DIV12" |
| Sampling | network activity during the exposure | "Measures of network activity over time at DIV5, 7, 9, and 12 in the NFA are reduced to an estimated area under the curve" |
| Informative for | "identifying chemicals with a shared mode of action" | "information relevant to developmental exposure" |

Across the 243 chemicals screened in both, the paper reports "70.3% concordance
between the AcN and NFA after eliminating activity inferred to be cytotoxic
(selective activity), with the majority of discordance explained by chemicals that
altered selective activity in the AcN but not NFA." The NFA "detected more active
chemicals when evaluating activity associated with cytotoxicity", and its median
potencies were lower, "but within-chemical potency values were not uniformly lower
in the NFA than the AcN." The authors' conclusion is that both are worth using
depending on the context of use.

**Both assays belong in the registry. Neither is being added to a dismech entry.**
The reason is not that the assays are weak — a functional, emergent endpoint
measured across a 243-chemical screen is the strongest kind of NAM this issue
produced. It is that the paper supplies no mechanism for a model link to attach
to:

- The record is **abstract-only**; the full text was not retrievable, so the
  chemical-level detail that would name a mode of action is not available to quote.
- The abstract **names no chemical**, so no link to a chemical-specific entry
  (`Organophosphate_Poisoning` and the other exposure entries included) could cite
  any text.
- The endpoint is **mechanism-agnostic and non-directional** by design. It records
  that something perturbed network function, in either direction, without saying
  what or why. `epilepsy_excitation_inhibition_imbalance` is the closest anchor,
  and neither end of it fits. Its trigger node, `Ion Channel and Synaptic
  Dysfunction`, *is* non-directional — it binds `GO:0042391 regulation of
  membrane potential` and `GO:0007268 chemical synaptic transmission` with
  `modifier: ABNORMAL`, which is the one annotation shape a bidirectional screen
  readout could attach to — but it describes channel and synaptic transmission in
  a neuron, where the MEA readout is emergent network function across a well, so
  it is at the wrong level. The nodes that *are* at network level
  (excitation-inhibition imbalance, then hyperexcitability and hypersynchrony) are
  directional, and a screen hit that may be a decrease in activity is not evidence
  for a node asserting an increase.

This is the sharpest instance of the general problem #16882 raises, and the first
case in this batch where a paper kept by the screen yields a registry entry and no
dismech link.

The registry record is drafted as **two** `NAMRecord`s, because the two assays are
different model systems rather than one system run two ways — the acute assay
records a matured network at DIV13 or 15, the network formation assay records one
as it is being built:

| Proposed record id | Assay |
|---|---|
| `cortex-mea-acute-network-primary-cell-rat` | AcN |
| `cortex-mea-network-formation-primary-cell-rat` | NFA |

Both are typed `TwoDCellCulture`, `biological_organization_level:
CELLULAR_NEIGHBORHOOD`, `species: NCBITaxon:10116`, with each assay's applications
and limitations carrying the paper's own sentences. They are open as a draft in
[nams-registry#57](https://github.com/monarch-initiative/nams-registry/pull/57),
where both were validated as `NAMRecord`, and their models as `TwoDCellCulture`,
against that repository's own `nam_records.yaml` and the NAMO commit it pins.

One thing holds that PR as a draft, and it is a question for the registry rather
than for this screen. `source_resources` is required and is defined as "A registry
resource a NAM was found in", but this NAM was found in a primary research paper, and a
primary research paper cannot be a registry resource: the registry's own
`ResourceTypeEnum.Report` says "A primary research paper is not a report."
Something still has to go in that slot, because the registry's
`test_nam_source_resources_exist` requires every value there to name a file in its
`resources/`. The draft carries ToxCast as a marked placeholder — the plausible
home for the EPA MEA endpoints, which could not be confirmed against invitrodb —
and records the paper and this special issue in free text instead. A separate
nams-registry issue covers the general case.

`references_cache/PMID_38788893.md` is committed and is cited only from this page,
not from any `kb/` entry. It is kept deliberately, so the quoted sentences above
and in the registry draft stay checkable — do not read its absence from `kb/` as
uncited and prune it.

The NFA's own gap — developmental neurotoxicity as an outcome, which dismech has
no module for — is tracked separately as
[#16880](https://github.com/monarch-initiative/dismech/issues/16880).

## Gaps and questions the screen raised

Mined out of the batch and filed separately, so they are not lost inside a
per-paper issue:

| Kind | Subject | Issue |
|---|---|---|
| Module gap | Inhaled-irritant injury of the conducting airway | [#16877](https://github.com/monarch-initiative/dismech/issues/16877) |
| Module gap | Chemical respiratory allergy (low molecular weight sensitizers) | [#16878](https://github.com/monarch-initiative/dismech/issues/16878) |
| Module gap | Efflux-mediated multidrug resistance | [#16879](https://github.com/monarch-initiative/dismech/issues/16879) |
| Module gap | Developmental neurotoxicity as an outcome | [#16880](https://github.com/monarch-initiative/dismech/issues/16880) |
| Node gap | Drug-induced phospholipidosis as distinct from steatosis | [#16881](https://github.com/monarch-initiative/dismech/issues/16881) |
| Scope | A NAM can belong in the registry with no dismech home | [#16882](https://github.com/monarch-initiative/dismech/issues/16882) |
| Convention | When is a molecular simulation a model of a mechanism? | [#16883](https://github.com/monarch-initiative/dismech/issues/16883) |
| Schema gap | Toxicant susceptibility varying by host genotype | [#16884](https://github.com/monarch-initiative/dismech/issues/16884) |
| Schema gap | Synergy between two exposures | [#16885](https://github.com/monarch-initiative/dismech/issues/16885) |
| Schema gap | Reversibility of a toxic injury | [#16886](https://github.com/monarch-initiative/dismech/issues/16886) |
