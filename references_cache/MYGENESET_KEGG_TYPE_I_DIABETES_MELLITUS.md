---
reference_id: "MYGENESET:KEGG_TYPE_I_DIABETES_MELLITUS"
title: "KEGG_TYPE_I_DIABETES_MELLITUS"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_TYPE_I_DIABETES_MELLITUS  KEGG_TYPE_I_DIABETES_MELLITUS

**MYGENESET:KEGG_TYPE_I_DIABETES_MELLITUS** — KEGG_TYPE_I_DIABETES_MELLITUS (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy type 1 diabetes mellitus pathway gene set (MSigDB C2 curated gene set). This is a disease pathway gene set representing autoimmune destruction of pancreatic beta cells. Member genes are heavily enriched for antigen presentation machinery (MHC class I and II), cytotoxic T-cell effectors (granzymes, perforin), apoptosis regulators (CASP3, CASP8, BAD, BCL2-family), and cytokine signaling components, reflecting the major mechanistic arms of the KEGG type 1 diabetes pathway: immune recognition, T-cell-mediated beta-cell killing, and beta-cell apoptosis. Insulin and related beta-cell function genes are also represented as the targeted tissue.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0005147 | type 1 diabetes mellitus |
| anatomical_structure | UBERON:0000006 | islet of Langerhans |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0019882 | antigen processing and presentation | biological_process | core_process | high |
| GO:0001913 | T cell mediated cytotoxicity | biological_process | core_process | high |
| GO:0042613 | MHC class II protein complex | cellular_component | core_component | medium |
| GO:0006915 | apoptotic process | biological_process | supporting_process | medium |
| GO:0006955 | immune response | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0030073 | insulin secretion | biological_process | marker_driven_plausible | medium |

## Members (46 genes)

| Symbol | Gene ID |
|---|---|
| CD28 | hgnc:1653 |
| CD80 | hgnc:1700 |
| CD86 | hgnc:1705 |
| CPE | hgnc:2303 |
| FAS | hgnc:11920 |
| FASLG | hgnc:11936 |
| FASN | hgnc:3594 |
| GAD1 | hgnc:4092 |
| GAD2 | hgnc:4093 |
| GZMB | hgnc:4709 |
| HLA-A | hgnc:4931 |
| HLA-B | hgnc:4932 |
| HLA-C | hgnc:4933 |
| HLA-DMA | hgnc:4934 |
| HLA-DMB | hgnc:4935 |
| HLA-DOA | hgnc:4936 |
| HLA-DOB | hgnc:4937 |
| HLA-DPA1 | hgnc:4938 |
| HLA-DPB1 | hgnc:4940 |
| HLA-DQA1 | hgnc:4942 |
| HLA-DQA2 | hgnc:4943 |
| HLA-DQB1 | hgnc:4944 |
| HLA-DQB2 | hgnc:4945 |
| HLA-DRA | hgnc:4947 |
| HLA-DRB1 | hgnc:4948 |
| HLA-DRB3 | hgnc:4951 |
| HLA-DRB4 | hgnc:4952 |
| HLA-DRB5 | hgnc:4953 |
| HLA-E | hgnc:4962 |
| HLA-F | hgnc:4963 |
| HLA-G | hgnc:4964 |
| HSPD1 | hgnc:5261 |
| ICA1 | hgnc:5343 |
| IFNG | hgnc:5438 |
| IL12A | hgnc:5969 |
| IL12B | hgnc:5970 |
| IL1A | hgnc:5991 |
| IL1B | hgnc:5992 |
| IL2 | hgnc:6001 |
| INS | hgnc:6081 |
| LTA | hgnc:6709 |
| PRF1 | hgnc:9360 |
| PTPRN | hgnc:9676 |
| PTPRN2 | hgnc:9677 |
| TNF | hgnc:11892 |
| ZNF395 | hgnc:18737 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_TYPE_I_DIABETES_MELLITUS.yaml` @ `c9af95e92cdd`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_TYPE_I_DIABETES_MELLITUS) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_TYPE_I_DIABETES_MELLITUS`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
