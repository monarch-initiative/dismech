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
  - drug_induced_phospholipidosis
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

The paper yields **two** `NAMRecord`s, because the two assays are
different model systems rather than one system run two ways — the acute assay
records a matured network at DIV13 or 15, the network formation assay records one
as it is being built:

| Record id | Assay |
|---|---|
| `cortex-mea-acute-network-primary-cell-rat` | AcN |
| `cortex-mea-network-formation-primary-cell-rat` | NFA |

Both are typed `TwoDCellCulture`, `biological_organization_level:
CELLULAR_NEIGHBORHOOD`, `species: NCBITaxon:10116`, with each assay's applications
and limitations carrying the paper's own sentences. They live under `nams/` in
[monarch-initiative/nams-registry](https://github.com/monarch-initiative/nams-registry),
and each carries a `dismech_status` with `present_in_dismech: false` — the registry's
way of recording that a NAM came through dismech curation and deliberately got no
`kb/` entry.

Drafting them raised a question that was general rather than specific to this
paper, and it has since been settled. `source_resources` is required and is defined
as "A registry resource a NAM was found in", but a NAM found in a primary research
paper had nothing to name: the registry's own `ResourceTypeEnum.Report` says "A
primary research paper is not a report", while `test_nam_source_resources_exist`
requires every value in that slot to name a file in `resources/`.
[nams-registry#63](https://github.com/monarch-initiative/nams-registry/issues/63)
answered it with a `scientific-literature` resource that carries the paper's DOI in
`source_urls`; the same round added `compared_with` for NAMs a study compared head
to head, which is how these two assays name each other.

`references_cache/PMID_38788893.md` is committed and is cited only from this page,
not from any `kb/` entry. It is kept deliberately, so the quoted sentences above
and in the registry records stay checkable — do not read its absence from `kb/` as
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
  distinct. That node gap ([#16881](https://github.com/monarch-initiative/dismech/issues/16881))
  is now closed by the `drug_induced_phospholipidosis` module, created from
  [#16867](https://github.com/monarch-initiative/dismech/issues/16867), which
  homes phospholipidosis as a lysosomal lipid-storage lesion separate from the
  triglyceride lipotoxicity of `hepatic_steatosis_lipotoxicity`.

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

### PMID:38614204 — glo heated-tobacco battery: registry only, and the Nrf2 anchor is deferred to full text

Keyser et al. 2024, *Toxicology* 504:153801 ([#16873](https://github.com/monarch-initiative/dismech/issues/16873)).
An in vitro battery applied to three menthol and one non-menthol variant of the glo
heated tobacco product (HTP), with market cigarette and HTP comparators: MTT in 3D
EpiAirway™ tissue, neutral red uptake (NRU) in monolayer, an in vitro micronucleus
assay, a bacterial reverse mutation (Ames) assay, an oxidative-stress readout in
EpiAirway, and limited aerosol chemistry (acetaldehyde, acrolein, crotonaldehyde,
formaldehyde).

**Funding and conflict of interest, recorded here because the registry rows must carry
it.** All authors are employees of RAI Services Company (Reynolds American, a British
American Tobacco subsidiary) and the work was commissioned by RAI — per #16873 and the
paper's own Declaration of Competing Interest; the committed cache holds only the
abstract, where this does not appear (its indexed publication type is "Research Support,
Non-U.S. Gov't"), so the affiliation and sponsorship are recorded from those sources
rather than quoted from a cached file. The paper's headline is
a comparative risk claim about the sponsor's own products ("substantially lower
toxicity compared to cigarettes"). **That comparative claim appears in no dismech or
registry content** — the assay-to-mechanism pairings are extracted independently of it.

**The oxidative-stress arm is almost certainly an NRF2/ARE pathway readout, not a
generic ROS or GSH marker — this was the issue's central open question.** The RAI
group's standard EpiAirway oxidative-stress method is the MatTek **EpiAirway Nrf2
ARE-luciferase bioreporter**: 3D airway tissue stably transfected so that NRF2/ARE
transcriptional activity drives luciferase. That this specific readout is the one used
in PMID:38614204 is an **inference from the group's standard platform, not a statement
quoted from PMID:38614204** — which is abstract-only here (see below) and reports only
an "oxidative stress response in the EpiAirway tissues". The platform itself is
confirmed from the same group's open-access companion paper on the identical model
(Keyser et al. 2024, *Toxics* 12:129, PMID:38393224):

> Briefly, EpiAirway™ tissues are stably transfected with a lentiviral vector
> consisting of the antioxidant responsive element of the Nrf2 gene fused with the
> luciferase gene as a bioreporter. The EpiAirway™ Nrf2 tissue model was developed by
> MatTek corporation and was described previously.

> EpiAirway™ tissues transfected with the Nrf2 luciferase reporter responded robustly
> to exposure to cigarette whole smoke at sub-cytotoxic doses, indicating the induction
> of the oxidative stress response.

On that reading the mechanistically correct anchor is `keap1_nrf2_are_signaling`,
specifically the `NRF2 Transcriptional Activation of ARE Genes` node — an ARE-luciferase
readout reports exactly that transactivation — at `model_scale: TISSUE`. Acrolein and
formaldehyde,
both measured in the aerosol, are electrophiles of the kind the upstream `KEAP1 Sensor
Cysteine Modification` node describes, which is why this is the right module rather than
a generic oxidative-stress label.

**The dismech link is nonetheless deferred, and the reason is grounding, not the
anchor.** PMID:38614204 is abstract-only: despite #16873's "open access" note, Europe
PMC reports the paper as subscription-only (Elsevier *Toxicology*; not in PMC/EPMC), and
doi.org / ScienceDirect are outside the session's allowed network. The abstract supports
"oxidative stress responses ... in the EpiAirway tissues" but does **not** itself contain
*Nrf2* or *ARE*. A model→mechanism link on `keap1_nrf2_are_signaling` has to be grounded
in a snippet from the cited reference that names the Nrf2 reporter; binding the pathway
node on the companion paper's wording alone would assert more than this reference's own
available text says, which is the named-entity discipline the evidence rules impose.
Adding the link once the full text is reachable is tracked at
[#17314](https://github.com/monarch-initiative/dismech/issues/17314).

**The other endpoints are registry assays, not dismech anchors.** The in vitro
micronucleus result is an abstract-level genotoxicity hazard call ("the whole aerosol
exposures of glo HTPs were classified as genotoxic in the in vitro micronucleus assay"),
and the abstract names no cell system for it, so neither a `genome_instability_mutation`
nor a `dna_damage_checkpoint_arrest` link can be grounded or correctly scaled yet —
that too waits on the full text. Cytotoxicity (NRU, MTT) is apical. The negative Ames
result ("The glo HTPs were non-mutagenic in the bacterial reverse mutagenesis assay") is
a recordable negative: in the registry it is a method with a negative outcome, and if it
ever reaches a model link the CLAUDE.md convention is a readout with `direction:
UNCHANGED` rather than `supports: NO_EVIDENCE`, which records evidence *direction* on a
claim rather than a measured null. There is no dismech entry for heated-tobacco or
cigarette-aerosol exposure for any of these to attach to in the first place; EpiAirway
here is the model this issue notes as the fourth pointing at the missing inhaled-irritant
airway-injury module ([#16877](https://github.com/monarch-initiative/dismech/issues/16877)).

Registry records proposed, one per model system, with the funding recorded on each and
no comparative claim. **This typing has not been validated against the registry's
schema** — no nams-registry pull request has been opened — so the table is a proposal,
as for PMID:38029956:

| Proposed record id | Assay / model | NAMO class | model_scale |
|---|---|---|---|
| `airway-epiairway-mtt-three-d-tissue-human` | MTT cytotoxicity, EpiAirway | `ThreeDTissueModel` | TISSUE |
| `airway-epiairway-nrf2-are-luciferase-three-d-tissue-human` | Nrf2/ARE luciferase oxidative-stress reporter, EpiAirway | `ThreeDTissueModel` | TISSUE |
| `airway-nru-two-d-culture-human` | NRU cytotoxicity, monolayer | `TwoDCellCulture` | CELLULAR |
| `in-vitro-micronucleus-system-tbd` | in vitro micronucleus (cell system not stated in abstract) | TBD | TBD (`CELLULAR` if a monolayer line) |
| `bacterial-reverse-mutation-ames` | Ames (negative) | `BacterialAssay` | — |

`source_resources` hits the same blocker the MEA and ReproTracker drafts did: the NAM
was found in a primary research paper, which the registry's own `ResourceTypeEnum.Report`
excludes.

`references_cache/PMID_38614204.md` (the glo abstract) and
`references_cache/PMID_38393224.md` (the companion full text, from which the Nrf2-reporter
sentences above are quoted) are committed and are cited only from this page, not from any
`kb/` entry. Both are kept deliberately so the quoted sentences stay checkable — do not
read their absence from `kb/` as uncited and prune them.

## Gaps and questions the screen raised

Mined out of the batch and filed separately, so they are not lost inside a
per-paper issue:

| Kind | Subject | Issue |
|---|---|---|
| Module gap | Inhaled-irritant injury of the conducting airway | [#16877](https://github.com/monarch-initiative/dismech/issues/16877) |
| Module gap | Chemical respiratory allergy (low molecular weight sensitizers) | [#16878](https://github.com/monarch-initiative/dismech/issues/16878) |
| Module gap | Efflux-mediated multidrug resistance | [#16879](https://github.com/monarch-initiative/dismech/issues/16879) |
| Module gap | Developmental neurotoxicity as an outcome | [#16880](https://github.com/monarch-initiative/dismech/issues/16880) |
| Node gap | Drug-induced phospholipidosis as distinct from steatosis — **closed** by the `drug_induced_phospholipidosis` module | [#16881](https://github.com/monarch-initiative/dismech/issues/16881) |
| Scope | A NAM can belong in the registry with no dismech home | [#16882](https://github.com/monarch-initiative/dismech/issues/16882) |
| Convention | When is a molecular simulation a model of a mechanism? | [#16883](https://github.com/monarch-initiative/dismech/issues/16883) |
| Convention | Where a PBPK or IVIVE dosimetry bridge belongs | [#16887](https://github.com/monarch-initiative/dismech/issues/16887) |
| Schema gap | Toxicant susceptibility varying by host genotype | [#16884](https://github.com/monarch-initiative/dismech/issues/16884) |
| Schema gap | Synergy between two exposures | [#16885](https://github.com/monarch-initiative/dismech/issues/16885) |
| Schema gap | Reversibility of a toxic injury; PMID:38211720 shows recovery can be endpoint-dissociated, so it has to be per-endpoint | [#16886](https://github.com/monarch-initiative/dismech/issues/16886) |
| Module gap | Bisphenol, or endocrine-disruptor, neurotoxicity (blocks every dismech record for PMID:38211720; a module would need a mechanism chain that paper does not supply) | Not filed |
| Schema gap | An immortalised tumour line standing in for a primary cell type: `ModelDivergenceTypeEnum` has no value for a cell-identity substitution (raised by PMID:38211720) | Not filed |
