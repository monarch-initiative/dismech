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
diseases:
  - Fetal_Valproate_Syndrome
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
dismech link. Both decisions recorded below went that way, for different reasons —
one because the endpoint asserts no mechanism, the other because the mechanism it
does assert has no disease entry to attach to.

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

### PMID:38029956 — the ReproTracker assay and its PBPK bridge go to the registry only

Moreau et al. 2023, *Toxicology* 500:153684 ([#16871](https://github.com/monarch-initiative/dismech/issues/16871)).
A commercial human iPSC biomarker assay for teratogenic potential (ReproTracker,
Toxys), coupled to a pregnancy PBPK model that converts the assay's in vitro
effect concentrations into human equivalent doses, run on two known human
teratogens.

| | ReproTracker hiPSC biomarker assay | Pregnancy PBPK model plus IVIVE |
|---|---|---|
| Measures | biomarker expression during directed differentiation | plasma and uterus concentration for an oral dose |
| Output | a teratogen / non-teratogen classification | a human equivalent dose for an in vitro effect concentration |
| Scope | "The ReproTracker assay focuses on the gastrulation phase." | five-week pregnancy, uterus compartment, no placenta or fetus |

The assay runs three directed differentiations from one hiPSC line — "The assay is
based on the differentiation of hiPSCs into functional cardiomyocytes, hepatocytes,
and neural rosettes." — and reads a germ-layer and a cell-specific biomarker in each:

| Differentiation | Germ-layer marker | Cell-specific marker |
|---|---|---|
| Cardiomyocyte | BMP4 (mesoderm) | MYH6 |
| Hepatocyte | FOXA2 (endoderm) | AFP |
| Neural rosette | PAX6 (neural ectoderm) | Nestin |

OCT4 is carried as a pluripotency control. Classification is by loss of signal:
"compound classification was primarily based on a significant reduction in the
selected biomarker expression following exposure to the test substances", and a
concentration-dependent drop below threshold across at least two consecutive
non-cytotoxic concentrations "indicated disruption of the developmental program and, therefore,
the compound was classified as a teratogen". Morphology and cardiomyocyte
contraction are secondary: "a compound affecting only morphology/functionality of
the differentiated cells without having any effect on the selected biomarker genes,
was a non-developmental toxicant in ReproTracker".

Both compounds were called teratogenic, by different profiles:

| | Thalidomide | Carbamazepine |
|---|---|---|
| Cardiomyocyte | MYH6 down "in a dose-dependent manner starting at 0.4 μM"; contraction abolished at 2 μM | beating stopped from 15.6 μM; MYH6 down |
| Hepatocyte | AFP and morphology disrupted "starting at 2 μM" | morphology at 31.2 μM; FOXA2 and AFP down |
| Neural rosette | spared — "no effect on the morphology of neural rosettes, nor on expression pattern of the neural rosette-specific biomarker gene, NESTIN"; PAX6 *increased* | morphology at 15.6 μM; PAX6 down |

**Both methods belong in the registry. Neither is being added to a dismech entry.**
The reason is not the one that applies to the MEA assays above, and the difference
is worth keeping.

The paper names no mechanism at all. In the cached full text the words "mechanism"
and "pathway" do not occur, and there is no cereblon, ubiquitin-ligase, SALL4,
anti-angiogenesis, histone-deacetylase or folate claim anywhere in it. The
cereblon-substrate-degradation anchor that
[#16871](https://github.com/monarch-initiative/dismech/issues/16871) floated from
the abstract has no
support in this paper; thalidomide's mechanism would have to come from other
literature.

But the readout is **not** mechanism-agnostic in the way an activity screen is. It
is lineage-resolved, directional and compound-specific, and thalidomide's profile
is selective in a way that would be informative if it had anywhere to attach:
cardiac and hepatic differentiation impaired, neural rosettes spared, and PAX6
moving *up* rather than down. That is the shape of a cellular-scale mechanism
claim, not an apical label.

The obstacle is at the anchor end instead. Neither test compound has a disease
entry whose pathograph could host the node:

- There is no thalidomide embryopathy entry.
- Fetal carbamazepine syndrome is in the knowledge base only as a term-bound
  `differential_diagnoses` row inside Fetal_Valproate_Syndrome.

A `modeled_mechanisms` target is a bare name resolved inside the entry that
declares it, so there is nothing for either method to point at. Pointing the
carbamazepine arm at Fetal_Valproate_Syndrome's `Altered Neural Progenitor
Proliferation and Differentiation` would assert a valproate mechanism from
carbamazepine data, which is the named-entity confusion the evidence rules forbid.
That entry gap is [#16910](https://github.com/monarch-initiative/dismech/issues/16910).

Two registry records are proposed, the assay and the dosimetry bridge separately,
because they have different outputs and either could be reused without the other:

| Proposed record id | Method | NAMO class |
|---|---|---|
| `multilineage-differentiation-two-d-culture-induced-pluripotent-stem-cell` | ReproTracker | `TwoDCellCulture` |
| `pregnancy-thalidomide-carbamazepine-pbpk` | PBPK plus IVIVE | `PBPKModel` |

Both are human (`NCBITaxon:9606`), which for thalidomide is the whole point:
"Thalidomide is a strong human teratogenic agent where its developmental toxicity
cannot be detected in mouse models or in murine-based in vitro assays."

**Unlike the MEA records above, this typing has not been validated against the
registry's schema** — no registry pull request has been opened for it, and the
class names here were read off NAMO and `nam_records.yaml` rather than checked by a
LinkML run. Treat the table as a proposal.

Three things would need deciding in the registry, and none of them is a question
for this screen:

- **One record or three.** NAMO's `model` slot asks an id to name "the organ, the
  format if it is not an organoid, and the cell source", which assumes one organ
  per record. ReproTracker spans cardiac, hepatic and neural lineages. One record
  matches how the assay is sold and how it classifies — a compound is a teratogen
  if *any* lineage drops, so the three protocols are coupled by the decision rule —
  while three records would match the id convention and let the lineage-specific
  results above be recorded against the lineage they belong to.
- **`source_resources`.** The same blocker the MEA draft hit, for the same reason:
  the NAM was found in a primary research paper. Toxys is the vendor and would be
  the plausible resource, with ReproTracker as its product.
- **Whether a PBPK model is a NAM record here at all.** NAMO does type it —
  `PBPKModel` sits under `InSilicoModel` under `NAMModel`, with compartment and
  drug-property slots — so in the registry the bridge has a home. This does not
  settle [#16887](https://github.com/monarch-initiative/dismech/issues/16887),
  which asks where the bridge belongs in **dismech**: a model of the
  exposure-to-concentration relationship still has no mechanism node to attach to,
  and the dismech answer for this paper is the same whether or not the registry
  takes the model.

`references_cache/PMID_38029956.md` is committed and is cited only from this page,
not from any `kb/` entry. It is kept deliberately, so the quoted sentences above
stay checkable — do not read its absence from `kb/` as uncited and prune it.

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
| Convention | Where a PBPK or IVIVE dosimetry bridge belongs | [#16887](https://github.com/monarch-initiative/dismech/issues/16887) |
| Schema gap | Toxicant susceptibility varying by host genotype | [#16884](https://github.com/monarch-initiative/dismech/issues/16884) |
| Schema gap | Synergy between two exposures | [#16885](https://github.com/monarch-initiative/dismech/issues/16885) |
| Schema gap | Reversibility of a toxic injury | [#16886](https://github.com/monarch-initiative/dismech/issues/16886) |
