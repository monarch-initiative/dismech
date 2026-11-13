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

Three further papers were set aside for reasons other than a missing dismech
anchor, and are listed here so the screen accounts for all twenty-five:
PMID:37924932 (a QSAR case study for mercury) is aquatic ecotoxicology and
reports a data gap rather than a working model; PMID:38104655 (a deep-learning
framework that generates candidate hazardous structures) asserts no mechanism in
a biological system; and PMID:38857863 (next generation risk assessment for
occupational safety, sodium isethionate) is an exposure and
bioactivity-ratio workflow across a NAM battery. The first is out of scope for
both destinations. The other two raise the same registry question as the five
above.

The gaps and open questions this screen produced, including the ones that are
not about any single paper, are kept in
[open-questions.md](NAMS_SPECIAL_ISSUE/open-questions.md).

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

### PMID:38740170 — the quadruple co-culture liver spheroid links into four dismech modules

Sun et al. 2024, *Toxicology* 505:153829 ([#16861](https://github.com/monarch-initiative/dismech/issues/16861), merged in [#16923](https://github.com/monarch-initiative/dismech/pull/16923)).
A self-assembled 3D liver spheroid of four human cell types (HepG2, PUMC-HUVEC-T1
endothelial, THP-1-derived macrophages, human hepatic stellate cells) for DILI
prediction. The contrast with the MEA case above is the point of keeping both:
this paper names the pathology each readout stands for, so each proof-of-concept
arm has a mechanism node to attach to.

The model is added as one `experimental_models` entry on each of four modules,
with a `modeled_mechanisms` link scoped to that module's relevant node:

| Module | Node | relationship | Readout |
|---|---|---|---|
| `drug_induced_liver_injury` | Sterile and Immune-Mediated Inflammatory Amplification | `PARTIALLY_RECAPITULATES` | isoniazid cytotoxicity `INCREASED` by non-parenchymal cells |
| `cholestatic_liver_injury` | Impaired Bile Formation and Secretion | `RECAPITULATES` | bile acid efflux `DECREASED` |
| `hepatic_steatosis_lipotoxicity` | Hepatocyte Lipid Overload | `RECAPITULATES` | lipid accumulation `INCREASED` |
| `fibrotic_response` | Mesenchymal Cell Activation | `RECAPITULATES` | α-SMA `INCREASED` |

Three decisions carried through the links:

- The **immune arm is `PARTIALLY_RECAPITULATES`, not `RECAPITULATES`.** The paper
  shows the non-parenchymal cells amplify isoniazid toxicity, but reads a
  mediating role in immune-mediated toxicity off that cytotoxicity difference
  rather than measuring an immune effector. The link carries a `PROXY_QUANTITY`
  divergence saying so.
- The **cholestasis link carries a `BOUNDARY_OMISSION` divergence** for the
  absent biliary tree, canalicular network and bile flow: the spheroid captures
  transporter-level efflux inhibition, not downstream bile stasis.
- The **lipid link carries a `PROXY_QUANTITY` divergence** because the bulk
  lipid-dysregulation readout spans steatosis and phospholipidosis, which are
  distinct. Drug-induced phospholipidosis as a node gap is tracked at
  [#16881](https://github.com/monarch-initiative/dismech/issues/16881).

The predictive-performance panel (22 DILI-positive, 5 DILI-negative compounds) is
recorded as a `findings` entry on each model, not as a mechanism link — it is
model validation, not a per-compound mechanism.

The record is **abstract-only**; the full text was not retrievable in the curation
environment, so every snippet is quoted from the abstract's summary statement and
the links are not yet backed by per-compound or quantitative readout data. A `notes`
line on each entry records that limit, and strengthening the links from the full
text is tracked at
[#16977](https://github.com/monarch-initiative/dismech/issues/16977).
`references_cache/PMID_38740170.md` is committed with the modules.

### PMID:38211720 — BPA analogues in 2D versus 3D SH-SY5Y: registry only, no dismech anchor

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

`references_cache/PMID_38211720.md` is committed and is cited only from this page,
not from any `kb/` entry. It is kept deliberately, so the abstract stays
checkable — do not read its absence from `kb/` as uncited and prune it.

### PMID:38580097 — the PFOS thyroid–DNT AOP network: registry only, no dismech edges

Wiklund, Pípal, Weiss and Beronius 2024, *Toxicology* 504:153794
([#16870](https://github.com/monarch-initiative/dismech/issues/16870)). An AOP
network for the thyroid modality, with the sub-paths leading to developmental
neurotoxicity (DNT) identified within it; an AOPN-driven systematic-review and
Weight-of-Evidence (WoE) assessment mapping existing in vitro and in vivo PFOS
data back onto that network; and a comparison of this mechanism-based endocrine-
disruptor (ED) identification against a standard guidance-based ED assessment.

This is the one paper in the batch whose *product* is a mechanism map rather than
an assay readout, which is why the issue hoped for two `mechanistic_hypotheses`
groups — a thyroid-mediated path and a directly-neurotoxic alternative path — out
of it. It yields neither, and the two reasons are worth keeping separate because
they fail the link at different ends.

**1. The paper is a negative result for the mechanism-based approach.** Its
conclusion, from the abstract, is that PFOS *"fulfils the criteria for ED
classification in the standard ED assessment, but not in the mechanism-based
assessment"*, and that the gap is quantitative information — the mechanism-based
route needs quantitative AOPs, which do not exist. That is a finding about the
method, not about PFOS. A dismech causal edge asserting a PFOS thyroid→DNT
mechanism, cited to this paper, would assert exactly what the paper declined to
conclude. The directly-neurotoxic alternative mode of action is weaker still —
the authors raise it *"based on available in vitro data"* as an explicit
alternative, not a confirmed path. So even with an anchor, the strongest honest
dismech content this paper supports is a `KNOWLEDGE_GAP` discussion, not a graded
causal edge. **If any future dismech content cites this PMID, it must not be cited
as establishing that PFOS is an endocrine disruptor or that the thyroid→DNT link
is operative for PFOS.**

**2. There is no anchor to attach to, in either arm.** Verified against `main`:

- **No PFOS entry.** There is no perfluorooctane-sulfonate disease or exposure
  entry anywhere in `kb/`. (The `perfluoro*` hits are `perfluorocarbon`, an
  unrelated oxygen carrier in `High_Altitude_Pulmonary_Edema`; a PFAS→GDM exposure
  *association* snippet in `Gestational_Diabetes_Mellitus`, which is not this
  mechanism; and `pFAS` = partial fetal alcohol syndrome in
  `Fetal_Alcohol_Spectrum_Disorder`, an acronym collision.) A `modeled_mechanisms`
  or `influences_mechanisms` target is a bare name resolved inside the entry that
  declares it, so there is no entry for either hypothesis group to live in.
- **No DNT outcome module.** `kb/modules/` has no developmental-neurotoxicity
  module; `epigenetic_machinery_neurodevelopmental_dysregulation` is a different
  concept. The gap is tracked at
  [#16880](https://github.com/monarch-initiative/dismech/issues/16880), and this
  paper's thyroid arm is one of its consumers — the other being the MEA network
  formation assay in [#16869](https://github.com/monarch-initiative/dismech/issues/16869).
  Those two should agree on one DNT node name and scale before either builds it.
- **The thyroid module stops short of the brain.**
  `hypothyroidism_thyroid_hormone_deficiency` runs Impaired Thyroid Hormone
  Synthesis → Thyroid Hormone Insufficiency → Reduced Thyroid Hormone Action at
  Peripheral Sites → Decreased Metabolic Rate → Systemic Hypometabolic State. Its
  terminal node is systemic hypometabolism; nothing in it reaches thyroid-hormone
  action in the developing brain. The thyroid arm of this AOP network would need a
  new downstream node (most naturally in a DNT module, not in the hypometabolism
  module whose scope is adult peripheral hypothyroidism).

A DNT module should be built from the broad, independently-established thyroid→
brain-development AOP literature under #16880, not sourced from this single
negative-result PFOS paper — building it here, citing this paper, is precisely the
misuse reason 1 warns against. So the thyroid→DNT AOP network is left unmapped,
and no thyroid→DNT AOP content exists elsewhere in the repo today
(`AOP_EMOD_ALIGNMENT`, `TDAR_AOP` and the parkinsonism crosswalk cover lead,
immunotoxicology and parkinsonism respectively; none touches the thyroid modality,
so the issue's suggestion that this network may already be partly mapped is not
borne out).

**The record is abstract-only.** The full text carries the per-KER WoE grades the
issue's deliverable 1 asked for, but it was not retrievable in the curation
environment: the paper is Elsevier/ScienceDirect, is **not** in PMC and is marked
non-open-access by Europe PMC, and `doi.org`/`sciencedirect.com` are outside the
session's allowed network. So no path could have been graded here even if there
were an anchor. A companion open-access methods paper from the same group
(*Front. Toxicol.* 5:1183824, 2023, which describes the thyroid AOP-network generation
and ships an R script) and the first author's doctoral thesis are the reachable
sources for the network structure, should a DNT module under #16880 want them;
they are not this PMID and do not carry its PFOS-specific WoE.

**The method goes to the registry, but its shape is undecided.** The AOPN-driven
systematic-review-plus-WoE assessment is a regulatory ED-identification
*methodology*, not an assay or a model system, so it does not slot cleanly into a
NAMO model class the way the MEA and ReproTracker records above do — this is the
"registry shape still undecided" flagged in the issue's repo-check comment. It is
proposed as a registry entry rather than drafted as a validated `NAMRecord`:

| Proposed registry subject | Kind | Status |
|---|---|---|
| AOP-network-driven systematic review + WoE for mechanism-based ED identification | assessment methodology (not an assay/model) | proposal — shape undecided, see below |

Opening the nams-registry PR is out of this screen's scope (that repository is not
in this session's GitHub access, and the record needs validation against NAMO,
which has no obvious class for an assessment workflow). It raises the same
`source_resources` blocker the MEA and ReproTracker drafts hit — the method was
found in a primary research paper — and additionally the prior question of whether
a WoE assessment methodology is a NAM the registry catalogues at all. Both are
registry questions, not screen questions.

**Quantitative AOPs, as an inventory-level limitation.** The paper's actual
conclusion — mechanism-based ED identification needs quantitative AOPs and they do
not exist — is recorded as a general caveat on AOP-derived dismech content in
[open-questions.md §10](NAMS_SPECIAL_ISSUE/open-questions.md), next to the qAOP
thread already open in [`AOP_EMOD_ALIGNMENT`](AOP_EMOD_ALIGNMENT.md). It is not
specific to this paper.

`references_cache/PMID_38580097.md` is committed and is cited only from this page,
not from any `kb/` entry. It is kept deliberately, so the abstract stays
checkable — do not read its absence from `kb/` as uncited and prune it.

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
| Schema gap | Reversibility of a toxic injury; PMID:38211720 shows recovery can be endpoint-dissociated, so it has to be per-endpoint | [#16886](https://github.com/monarch-initiative/dismech/issues/16886) |
| Convention | AOP-derived edges are qualitative; a mechanism-based call needs quantitative AOPs, which do not exist (raised by PMID:38580097) — [open-questions §10](NAMS_SPECIAL_ISSUE/open-questions.md) | Not filed |
| Module gap | Bisphenol, or endocrine-disruptor, neurotoxicity (blocks every dismech record for PMID:38211720; a module would need a mechanism chain that paper does not supply) | Not filed |
| Schema gap | An immortalised tumour line standing in for a primary cell type: `ModelDivergenceTypeEnum` has no value for a cell-identity substitution (raised by PMID:38211720) | Not filed |
