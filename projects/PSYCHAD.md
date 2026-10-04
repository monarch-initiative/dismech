---
title: PsychAD Consortium Collection
status: IN_PROGRESS
description: >-
  Mine the PsychAD Consortium papers (Nature Portfolio collection, 23 September
  2026) and their released datasets for evidence and mechanistic hypotheses
  across Alzheimer disease, related dementias, schizophrenia and bipolar disorder.
tags: [NEURODEGENERATION, PSYCHIATRY, SINGLE_CELL, DATASETS, HYPOTHESES]
diseases:
  - Alzheimer_Disease
  - Dementia_with_Lewy_Bodies
  - Parkinsons_Disease
  - Frontotemporal_Dementia
  - Progressive_Supranuclear_Palsy
  - Schizophrenia
  - Bipolar_Disorder
  - Major_Depressive_Disorder
modules:
  - inflammaging
  - neuroinflammation_glial_activation
  - loss_of_proteostasis
  - genomic_instability_aging
  - disabled_macroautophagy
---

# PsychAD Consortium Collection

## Overview

The PsychAD Consortium generated a single-nucleus RNA-seq atlas of the human
dorsolateral prefrontal cortex: more than 6.3 million nuclei from 1,494 donors.
The cohort covers neurotypical controls and eight disorders: Alzheimer disease,
diffuse Lewy body disease, vascular dementia, Parkinson disease, tauopathy,
frontotemporal dementia, schizophrenia and bipolar disorder. The papers were
published together as a Nature Portfolio collection on 23 September 2026
(<https://www.nature.com/collections/jfibicjjjg>; consortium site
<https://psych-ad.org>).

This project tracks which findings from those papers and datasets are curated
into dismech, which candidate mechanistic hypotheses they motivate, and which
re-analyses of the open data have been run.

## Papers

All papers are cached in `references_cache/`. Content type is noted because
snippets from an abstract-only cache can quote only the abstract.

| PMID | First author | Title | Journal | Cache |
|---|---|---|---|---|
| PMID:42778699 | Lee | Single-cell atlas of transcriptomic vulnerability across brain disorders | Nature | full text |
| PMID:42778698 | Yang | Lifespan single-cell transcriptomic atlas of the human prefrontal cortex | Nature | full text |
| PMID:42778697 | Venkatesh | Single-nucleus transcriptome-wide association study of human brain disorders | Nature | full text |
| PMID:42778763 | He | AI-based characterization of Alzheimer's disease phenotypes from population-scale single-cell data (PASCode) | Nature Medicine | abstract only |
| PMID:42778721 | Zeng | Single-nucleus atlas of cell-type specific genetic regulation in the human brain | Nature Genetics | full text (PDF) |
| PMID:42778537 | Chandrashekar | Personalized single-cell transcriptomics reveals molecular diversity in Alzheimer's disease | Nature Communications | full text |
| PMID:42778538 | Hoffman | Fast, flexible analysis of differences in cellular composition with crumblr | Nature Communications | full text |
| PMID:42778542 | Hoffman | Efficient differential expression analysis of large-scale single-cell transcriptomics data using Dreamlet | Nature Communications | full text |
| PMID:40480991 | Fullard | Population-scale cross-disorder atlas of the human prefrontal cortex at single-cell resolution | Scientific Data | full text |

## Disorder coverage

Donor counts are from Table 1 of the data descriptor (PMID:40480991). All
tissue is dorsolateral prefrontal cortex (DLPFC), so for diseases whose primary
lesion lies elsewhere (Parkinson disease, PSP) the data describe cortical
involvement only. About a fifth of donors carry two or more major diagnoses
("21% of donors had comorbid diagnoses of two or more major brain disorders",
PMID:40480991), and AD co-pathology is permitted in the DLBD, vascular, PD and
FTD groups, which confounds every non-AD claim.

| PsychAD diagnosis | Donors | dismech entry | Notes |
|---|---|---|---|
| Alzheimer disease | 519 | `Alzheimer_Disease` | Already lists `synapse:syn60084804` and cites PASCode |
| Diffuse Lewy body disease | 112 | `Dementia_with_Lewy_Bodies` | Neuropathological diagnosis; frequent AD co-pathology |
| Parkinson disease | 40 (48 in the descriptor's text) | `Parkinsons_Disease` | Cortex only; the two counts in PMID:40480991 disagree |
| Frontotemporal dementia | 16 | `Frontotemporal_Dementia` | FTLD-tau and FTLD-TDP are not distinguished |
| Tauopathy | 45 | none | Defined by pathology, not clinical diagnosis (see below) |
| Vascular dementia | 85 | none | Generic brain-bank "vascular" diagnosis; no entry or stub |
| Schizophrenia | 177 | `Schizophrenia` | Mostly the MSSM cohort |
| Bipolar disorder | 72 | `Bipolar_Disorder` | All from the HBCC cohort, so cohort is partly confounded with diagnosis |
| PSP | 5 | `Progressive_Supranuclear_Palsy` | Not one of the eight analysed disorders; too few donors for a dataset record |

**"Tauopathy" here is not PSP or corticobasal degeneration.** The flagship
defines it as "any individual with CERAD = {1}, Braak = {4,5,6} and secondary
diagnosis allowed" (PMID:42778699): high tangle stage without neuritic plaques,
which is closest to primary age-related tauopathy. The paper never mentions
PSP, CBD or 4R tau, so its tauopathy results should not be cited on the PSP or
corticobasal entries. dismech has no PART entry.

## Datasets

| Accession | Contents | Access |
|---|---|---|
| `synapse:syn60084804` (PsychAD_NPS) | Hub project linking the raw FASTQ, joint h5ad and metadata for all 1,494 donors | Hub page public; the data it links to (under `syn52160016`, MSSM_PsychAD) is controlled through the AD Knowledge Portal |
| `cellxgene:84ce6837-548d-4a1f-919f-0bc0d9a3952f` | Four h5ad datasets with MONDO disease labels per cell: MSSM (1,042 donors), HBCC (300), RADC (152), Aging (291) | Open, direct download. The Aging dataset duplicates MSSM and HBCC donors (`is_primary_data=False`) and must be dropped when pooling |
| `synapse:syn61929918` (PsychAD_eQTL_release) | Zeng et al. cis/trans/dynamic eQTL and colocalization results | Open with a free Synapse login |
| `synapse:syn63181047` (PsychAD_snTWAS) | Venkatesh et al. imputation models and supplementary data; also on Zenodo (10.5281/zenodo.17435917) | Open |
| `synapse:syn52396927` (DLPFC Lifespan Atlas) | Yang et al. h5ad, pseudobulk, trajectories, circadian results | No access requirement on the Synapse entity, but the paper describes the data as controlled-use; confirm before relying on it |
| `synapse:syn51188606` (PsychAD - public) | Earlier 299-donor AD/control release used by Dreamlet | Open |
| Zenodo 10.5281/zenodo.14606776 | Xenium spatial data, 11 DLPFC sections | Open; 3-18 GB per section |

The Nature supplementary files for every paper are downloadable from
`media.springernature.com`. The tables most relevant to curation:

- Flagship: Supplementary Table 3 (cross-disorder composition), Table 4
  (shared vs disease-specific differential expression), Table 5 (composition
  vs AD pathology and ageing), Table 6 (AD-severity DEGs), Tables 7-9
  (trajectory modules), Table 13 (mediation), and Supplementary Data 1
  (per-cell Braak and dementia predictions).
- Lifespan: Supplementary Data 1-21 and Tables 1-4.
- TWAS: Supplementary Tables 1-42.
- eQTL: Supplementary Tables 1-4 (multi-gene coloc loci, trans-eGenes).
- Chandrashekar: Supplementary Data 1-5.

`just verify-datasets` cannot resolve `synapse:` or `cellxgene:` accessions,
so dataset records for these carry `notes` rather than a cached record.

## Reading the results

Two methods papers in the collection set how the main results should be read.

- **Composition changes are relative.** crumblr uses a centred log-ratio
  transform: "The CLR transform is widely used in compositional data analysis
  and normalizes each cell component with the same denominator using the
  geometric mean of cell frequencies" (PMID:42778538). A cell type reported as
  increased may only be spared while others are lost. Curate these as changes
  in proportion, never as proliferation or absolute loss.
- **Absent differential expression is not absent effect.** Dreamlet reports
  that "The effect of AD status is modest, with only 101 genes explaining more
  than 5% of the variance, underscoring the need for large sample sizes to
  characterize expression changes associated with the disease"
  (PMID:42778542), and DEG counts scale with nuclei per donor. A rare cell type
  or a small diagnosis group (FTD, PSP) without DEGs says little.

**`evidence_source` grading.** Descriptive composition, differential
expression and RNAscope or spatial validation on postmortem tissue are
`HUMAN_CLINICAL`. TWAS, eQTL colocalization, fine-mapping, mediation models
and the graph-neural-network results of PASCode and Chandrashekar et al. are
`COMPUTATIONAL`. Use one grade per quoted sentence across files, as
`just check-snippet-grading` requires.

## Candidate evidence by entry

Every quote below is an exact substring of the cached paper after the
validator's normalization. None has been added to the KB yet.

### Alzheimer_Disease

| Finding | Quote | Target node | Effect |
|---|---|---|---|
| Neocortical L2-3 IT neuron loss | "Moreover, the loss of L2–3 IT neurons in AD (based on case–control and CERAD comparisons), which is not evident in normal ageing, suggests a specific vulnerability for this neuronal subtype to AD." (PMID:42778699) | Selective Vulnerability of RORB+ Entorhinal Excitatory Neurons, or a new DLPFC node | Extends the vulnerability claim to neocortex |
| RNAscope validation | "confirming the decline in L2–3 IT excitatory and SST+ inhibitory neurons and the prevalence of VLMCs in AD" (PMID:42778699) | Same; Interneuron Dysfunction and Network Hypersynchrony | Support |
| AD-specific smooth muscle increase | "we identified an AD-specific increase in smooth muscle cells (SMCs), a vascular cell type that normally declines with age, suggesting an AD-specific vulnerability in these cells." (PMID:42778699) | Vascular Dysfunction | Support |
| Early loss of homeostatic microglia | "Several markers for homeostatic microglia57, including CX3CR1, NAV2 and P2RY12, were among the top 5 early decreasing genes with increasing disease pseudotime" (PMID:42778699) | Neuroinflammation | Support; adds timing |
| Immune response tracks resilience | "On the other hand, the immune response appears to be generally protective, whereby an early innate immune activation85 followed by an adaptive immune response64,75,76 was associated with resilience to dementia." (PMID:42778699) | Adaptive Immune T Cell Response to Tau Pathology | **Qualifies.** That node treats T cells as damaging |
| IL-17 response is the exception | "The one exception was the response of immune, mural and endothelial cell classes to IL-17, which was damaging in the early stages of AD." (PMID:42778699) | Vascular Dysfunction, or a new node | Support |
| Cell-type-dependent chaperone effect | "Our results suggest that chaperones can have opposing roles depending on the cellular context—damaging for glia, immune and endothelial cells but possibly protective for neurons." (PMID:42778699) | Autophagy-Lysosomal Dysfunction / proteostasis | Qualifies the sign by cell type |
| No APOE expression footprint | "First, performing differential expression analysis on the basis of the APOE genotype did not identify any genes as differentially expressed at a study-wide FDR of 5%." (PMID:42778699) | `apoe_risk_modulation_model` | Qualifies |
| Mediation: microglia and VLMCs | "Tau progression results in more VLMCs mediated by an increase in microglia" (PMID:42778699) | Neuroinflammation → Vascular Dysfunction edge | Statistical mediation, not experiment |
| Mediation: SST interneurons and plaque | "Furthermore, plaque accumulation is mitigated by SST+ inhibitory neurons" (PMID:42778699) | Interneuron Dysfunction (currently PV-centred) | Support; adds SST |
| Deep-layer neurons and NPS | "we found that patients with AD experiencing weight loss and PMA have an increased ratio of excitatory neurons, especially deep-layer neurons in L5–6" (PMID:42778699) | Behavioral Changes phenotype; contrasts with `glial_depression_in_ad_model` | Support |
| Microglial ZYX at the EPHA1 locus | "Together, these findings prioritize ZYX as a putative coding effector at this locus and link its downregulation to impaired MG stress responses to β-amyloid" (PMID:42778697) | Neuroinflammation; ZYX has no `genetic:` record | Support (computational) |
| Astrocyte-specific EGFR risk | "The lead variant for the astrocyte signal is rs74504435, which has a composite posterior probability of 0.946 that it is associated only with EGFR expression in astrocytes" (PMID:42778721) | New astrocyte node; EGFR has no `genetic:` record | Support (computational) |
| Ageing microglial programs carry AD risk | "Moreover, microglial trajectories 3 (chromatin modification) and 6 (autophagy), characterized by age-related decline, also showed AD risk enrichment, suggesting that these programs contribute to AD vulnerability independent of late-life differential expression" (PMID:42778698) | Autophagy-Lysosomal Dysfunction | Support, indirect |
| Mature oligodendrocytes and AD risk | "OPCs showed significant associations with psychiatric traits and obesity, while mature oligodendrocytes exhibited enrichment for AD" (PMID:42778698) | Oligodendrocyte and Myelin Dysfunction | Support, indirect |
| Regulatory staging | "For BRAAK phenotype, we identified several TFs from IN CTs with higher scores in early BRAAK stages and TFs from astrocytes and microglia for late BRAAK stages" (PMID:42778537) | Interneuron Dysfunction; Neuroinflammation | Support (computational) |
| Microglial signalling lost in AD | "Notably, interactions originating from microglia were higher in control donors, whereas those involving IN_SST neurons as the source CT were higher in AD donors" (PMID:42778537) | Neuroinflammation | Qualifies the amplification framing |
| "Subtypes" track severity | "For example, c1-c2 were enriched for early BRAAK stages (0-2), controls in CDRscore, and 'No AD' based on CERAD; while c4-c5 were enriched for late BRAAK stages (5-6), Dementia (CDRscore), and presence of AD (CERAD)." (PMID:42778537) | None | The c1-c5 clusters are stages, not subtypes; do not add them as `has_subtypes` |

### Dementia_with_Lewy_Bodies and Parkinsons_Disease

| Finding | Quote | Effect |
|---|---|---|
| Concordance among four dementias | "After discounting these cross-disease signatures, we show stronger genetic and transcriptomic concordance among AD, DLBD, Vas and PD." (PMID:42778699) | Shared mechanism with AD; relevant to both entries and to a comorbidity record |
| Microglial heritability | "The neurodegenerative traits Alzheimer’s disease (AD) and Parkinson’s disease show enrichment in microglia but not in neuronal subclasses." (PMID:42778721) | Supports a microglial node in `Parkinsons_Disease` (computational) |

The flagship reports DLBD and PD mostly as members of the neurodegenerative
group. Disease-specific results are in its Supplementary Tables 3 and 4 and
have not been extracted.

### Schizophrenia and Bipolar_Disorder

| Finding | Quote | Target | Effect |
|---|---|---|---|
| Psychiatric disorders are neuronal | "neurological diseases, including NDDs such as AD and neuroimmune diseases such as MS, largely involve immune and glial cell types, whereas psychiatric diseases are predominantly associated with neurons" (PMID:42778699) | Both | Support |
| Deep-layer excitatory neurons | "By contrast, NPDs were predominantly associated with an increase in neuronal cells, particularly deep-layer ENs in L5–6." (PMID:42778699) | New node in both; a proportion, not proliferation | Support |
| Chandelier cells and shared heritability | "Among all cell types, Chandelier cells (IN_PVALB_CHC), a subset of GABAergic interneurons, had the highest concordance with the pairwise trait heritability." (PMID:42778699) | `Schizophrenia` Abnormality of GABAergic Signaling | Support, cross-disorder |
| CACNA1C in inhibitory neurons | "Among the top hits, CACNA1C showed highly specific effects in class-inhibitory neurons for schizophrenia" (PMID:42778697) | `Schizophrenia` GABAergic node; CACNA1C has no Schizophrenia `genetic:` record | Support (computational) |
| CNTN4 in layer 6 neurons | "CNTN4 coding for the contactin 4 protein involved in cell adhesion only colocalized with SCZ risk in layer 6" (PMID:42778721) | `Schizophrenia` Abnormality of Glutamergic Signaling | Support (computational) |
| Astrocytic RERE/AUTS2 | "the cis regulation of RERE and the trans regulation of AUTS2 colocalize, albeit weakly, with the genetic risk for SCZ" (PMID:42778721) | `Schizophrenia`, no astrocyte node yet | Weak; the authors say so |
| Developmental risk genes | "Psychiatric risk genes for schizophrenia and major depressive disorder were enriched among downregulated aDEGs but not upregulated aDEGs" (PMID:42778698) | `Schizophrenia` neurodevelopmental hypothesis | Support, indirect |
| RHOBTB2 in bipolar disorder | "prioritizing RHOBTB2 as the probable causal BD gene at this locus." (PMID:42778697) | `Bipolar_Disorder`; RHOBTB2 has no record | Support (computational) |
| Ancestry caveat | "yet only 8.3% of significant AFR GTAs (4 of 48) were also significant in EUR, even when aggregating across all cell types." (PMID:42778697) | Any snTWAS gene claim | Qualifies |

### Ageing modules

| Finding | Quote | Module | Effect |
|---|---|---|---|
| Midlife stability | "The second phase, encompassing young and middle adulthood, showed transcriptomic stability with only 27 and 1 aDEGs, respectively." (PMID:42778698) | `inflammaging` | Qualifies timing: cortical change is non-linear |
| Late-life glial reactivation | "By contrast, the third phase during late adulthood showed renewed remodelling, primarily affecting glia (426 out of 735 aDEGs) versus neurons (246 out of 735)" (PMID:42778698) | `neuroinflammation_glial_activation` | Support |
| Interferon signalling | "Trajectory 10 specifically highlighted glial immune activation and interferon signalling in late-life neuroinflammation" (PMID:42778698) | `neuroinflammation_glial_activation`, `inflammaging` | Support |
| SST decline is normal ageing | "These assays revealed a progressive decline in SST+ interneurons and a marked increase in GPR37+ oligodendrocytes with age" (PMID:42778698) | Baseline for AD and SCZ interneuron claims | Confounder |
| Loss of neuronal clock rhythms | "In late adulthood, these rhythms were largely lost, and peak times became inconsistent across subclasses" (PMID:42778698) | `Bipolar_Disorder` Circadian Rhythm Disruption (ageing context) | Qualifies |

The lifespan atlas reports no senescence markers, so it should not be cited
on `cellular_senescence`. Its upregulated unfolded-protein-response and
DNA-repair transcripts in aged cells read as responses to stress, which
qualifies rather than supports the "decline" framing of `loss_of_proteostasis`
and `genomic_instability_aging`.

## Candidate mechanistic hypotheses

Each is a statistical association in one cohort and would enter at most as
`EMERGING`. The "test" column names the published or open data a re-analysis
would use. Several reuse the same donors as the paper that motivated them, so a
re-analysis checks robustness, not independent replication.

| Entry | `hypothesis_group_id` | Statement | Test data |
|---|---|---|---|
| Alzheimer_Disease | `microglia_vlmc_meningeal_expansion_model` | Tau-associated microglial expansion drives an increase in meningeal VLMC fibroblasts (VLMC_DCDC2) that mediates cognitive decline | Flagship Supp. Tables 3, 5, 6, 13 |
| Alzheimer_Disease | `sst_interneuron_amyloid_restraint_model` | SST interneuron loss, driven by microglial expansion and tau, permits plaque accumulation; interneuron loss is upstream of amyloid burden as well as downstream | Flagship Supp. Tables 5, 6, 13 |
| Alzheimer_Disease | `early_il17_neurovascular_injury_model` | An early IL-17 response in immune, mural and endothelial cells injures the neurovascular unit, against an otherwise protective immune trajectory | Flagship Supp. Tables 7, 9; Supp. Data 1 |
| Alzheimer_Disease | `monocyte_adaptive_immune_resilience_model` | Innate-then-adaptive and monocyte immune programs confer resilience to dementia at a given Braak stage; competes with `adaptive_immune_tcell_model` | Flagship Supp. Tables 7-9; Supp. Data 1 |
| Alzheimer_Disease | `neuronal_regulatory_reserve_resilience_model` | Resilience reflects preserved upper-layer excitatory regulatory programs (CUX2, DLGAP1, TENM4) rather than a protective astrocyte state; competes with `reactive_astrocyte_resilience_model` | Chandrashekar Supp. Data 2; PASCode Supp. Data 1-7 |
| Alzheimer_Disease | `microglial_homeostatic_regulon_loss_model` | Progression involves early loss of homeostatic microglial control (CX3CR1, P2RY12, IRF8 targets) before late microglial and astrocytic programs take over | Flagship Supp. Tables 7-9; Chandrashekar Supp. Data 1-2 |
| Alzheimer_Disease | `ad_microglial_zyx_downregulation` | Genetically reduced microglial ZYX at the EPHA1 locus impairs the microglial response to amyloid | TWAS Supp. Tables 18, 23, 24; eQTL Supp. Table 2 |
| Alzheimer_Disease | `ad_astrocytic_egfr_risk` | AD risk at EGFR acts through astrocyte-specific cis-regulation | `syn61929918` coloc tables |
| Alzheimer_Disease, Schizophrenia, Bipolar_Disorder | `deep_layer_excitatory_nps_model` | A relative excess of L5-6 excitatory neurons is a shared cortical substrate of neuropsychiatric symptoms in AD and of SCZ and BD | Flagship Supp. Tables 1, 3, 5 |
| Schizophrenia | `scz_inhibitory_cacna1c_grex` | SCZ risk acts through genetically regulated CACNA1C and GPM6A expression in ADARB2 inhibitory interneurons | TWAS Supp. Tables 18, 20 |
| Bipolar_Disorder | `bd_excitatory_rhobtb2` | RHOBTB2 in excitatory neurons is the causal BD gene at its locus | TWAS Supp. Table 30 |
| `inflammaging` | `late_onset_glial_inflammaging` | Cortical inflammaging stays near baseline through midlife and rises after about 60, in glia rather than neurons | Lifespan Supp. Data 4, 7 |
| `loss_of_proteostasis` | `compensatory_glial_upr_with_age` | Aged microglia and oligodendrocytes raise UPR transcripts as compensation, not as evidence of proteostasis collapse | Lifespan Supp. Data 7, 17, 21 |

## Re-analyses (OpenScientist)

Planned runs on open data only. The existing PASCode runs
(`kb/hypotheses/Alzheimer_Disease/glial_depression_in_ad_model/` and
`reactive_astrocyte_resilience_model/`) show the pattern: download published
supplementary tables, record checksums, and assess with the
`review-hypothesis-exploration` skill.

`just research-hypothesis openscientist <Disorder> <hypothesis_group_id>` needs
the hypothesis to exist in the entry's `mechanistic_hypotheses`, so a hypothesis
from the table above has to be curated before it can be run. Dataset discovery
runs need only the entry (`just research-datasets openscientist <Disorder>`).

| Run | Input | Question | Informs |
|---|---|---|---|
| Cross-disorder composition | Flagship Supp. Table 3 | Which subclasses shift in DLBD, PD, FTD, SCZ and BD, and which shifts are shared | Cell-type nodes in the non-AD entries |
| Shared vs specific expression | Flagship Supp. Table 4 | Are DLBD and PD glial programs shared with AD or specific to Lewy body disease | `Dementia_with_Lewy_Bodies`, `Parkinsons_Disease` |
| Comorbidity-free recount | CELLxGENE MSSM, HBCC, RADC `obs` tables | Donors per diagnosis after excluding comorbid cases and applying the age floors (60 for neurodegenerative, 17 for psychiatric) | Whether FTD and BD dataset records are warranted |
| Gene placement check | `syn61929918` coloc tables | For each `genetic:` gene in SCZ, BD, AD and PD, which cell type carries the colocalization, and does it match the node the gene is wired to | Gene-to-mechanism wiring |
| snTWAS gene census | TWAS Supp. Tables, `syn63181047` | Cell-type TWAS genes absent from the entries | `genetic:` additions (`SUSCEPTIBILITY`) |
| Per-cell Braak and dementia signal | Flagship Supp. Data 1 | Which subclasses carry the strongest Braak and dementia signal | AD vulnerability nodes |
| Hypothesis runs | As in the hypothesis table | One run per curated hypothesis | The hypothesis itself |

## Tasks

- [x] Cache all nine papers
- [x] Review each paper for candidate evidence and hypotheses
- [x] Inventory datasets and access tiers
- [ ] Add `datasets:` records to `Dementia_with_Lewy_Bodies`, `Parkinsons_Disease`, `Frontotemporal_Dementia`, `Schizophrenia`, `Bipolar_Disorder`
- [ ] Curate the evidence above into the entries
- [ ] Curate the candidate hypotheses that survive review into `mechanistic_hypotheses`
- [ ] Run the OpenScientist re-analyses and assess them
- [ ] Decide whether vascular dementia and primary age-related tauopathy need stubs
