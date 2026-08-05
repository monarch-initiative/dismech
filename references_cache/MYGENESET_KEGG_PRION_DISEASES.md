---
reference_id: "MYGENESET:KEGG_PRION_DISEASES"
title: "KEGG_PRION_DISEASES"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_PRION_DISEASES  KEGG_PRION_DISEASES

**MYGENESET:KEGG_PRION_DISEASES** — KEGG_PRION_DISEASES (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy Prion Diseases pathway gene set (MSigDB C2 curated gene set). This is a disease pathway gene set, not a cell-type signature. The member genes reflect the major mechanistic arms of the KEGG prion diseases pathway (hsa05020): conversion of the cellular prion protein (PrPC) to its pathogenic misfolded isoform (PrPSc) with amyloid fibril formation; complement-mediated early prion propagation; neuroinflammatory activation of astrocytes and microglia; caspase-dependent neuronal apoptosis; and endoplasmic-reticulum stress and unfolded protein response signalling. Ribosomal protein subunits present in the gene set drive non-specific translation enrichment signals.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0005429 | prion disease |
| anatomical_structure | UBERON:0000955 | brain |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:1990000 | amyloid fibril formation | biological_process | core_process | high |
| GO:0006956 | complement activation | biological_process | supporting_process | medium |
| GO:0006915 | apoptotic process | biological_process | supporting_process | medium |
| GO:0051402 | neuron apoptotic process | biological_process | core_process | medium |
| GO:0005886 | plasma membrane | cellular_component | core_component | high |
| GO:0048143 | astrocyte activation | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (40 genes)

| Symbol | Gene ID |
|---|---|
| BAX | hgnc:959 |
| C1QA | hgnc:1241 |
| C1QB | hgnc:1242 |
| C1QC | hgnc:1245 |
| C5 | hgnc:1331 |
| C6 | hgnc:1339 |
| C7 | hgnc:1346 |
| C8A | hgnc:1352 |
| C8B | hgnc:1353 |
| C8G | hgnc:1354 |
| C9 | hgnc:1358 |
| CCL5 | hgnc:10632 |
| CXCL10 | hgnc:10637 |
| EGR1 | hgnc:3238 |
| ELK1 | hgnc:3321 |
| FYN | hgnc:4037 |
| HSPA1A | hgnc:5232 |
| HSPA5 | hgnc:5238 |
| IL1A | hgnc:5991 |
| IL1B | hgnc:5992 |
| IL6 | hgnc:6018 |
| KCNH4 | hgnc:6253 |
| KCNH8 | hgnc:18864 |
| LAMC1 | hgnc:6492 |
| MAP2K1 | hgnc:6840 |
| MAP2K2 | hgnc:6842 |
| MAPK1 | hgnc:6871 |
| MAPK3 | hgnc:6877 |
| NCAM1 | hgnc:7656 |
| NCAM2 | hgnc:7657 |
| NOTCH1 | hgnc:7881 |
| PHOX2A | hgnc:691 |
| PRKACA | hgnc:9380 |
| PRKACB | hgnc:9381 |
| PRKACG | hgnc:9382 |
| PRKX | hgnc:9441 |
| PRNP | hgnc:9449 |
| PSMA7 | hgnc:9536 |
| SOD1 | hgnc:11179 |
| STIP1 | hgnc:11387 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_PRION_DISEASES.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_PRION_DISEASES) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_PRION_DISEASES`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
