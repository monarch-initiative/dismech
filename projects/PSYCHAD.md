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
  - Corticobasal_Syndrome
  - Schizophrenia
  - Bipolar_Disorder
modules:
  - inflammaging
  - cellular_senescence
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

| PsychAD diagnosis | dismech entry |
|---|---|
| Alzheimer disease | `Alzheimer_Disease` |
| Diffuse Lewy body disease | `Dementia_with_Lewy_Bodies` |
| Parkinson disease | `Parkinsons_Disease` |
| Frontotemporal dementia | `Frontotemporal_Dementia` |
| Tauopathy | no single entry; candidates `Progressive_Supranuclear_Palsy`, `Corticobasal_Syndrome` |
| Schizophrenia | `Schizophrenia` |
| Bipolar disorder | `Bipolar_Disorder` |
| Vascular dementia | none, and no stub in `stubs/` |

## Tasks

- [x] Cache all nine papers
- [ ] Review each paper for evidence and candidate hypotheses
- [ ] Inventory datasets and access tiers
- [ ] Run OpenScientist re-analyses of the open data
- [ ] Curate verified evidence into the disorder entries
