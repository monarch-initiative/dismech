---
reference_id: "MYGENESET:KEGG_ASTHMA"
title: "KEGG_ASTHMA"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_ASTHMA  KEGG_ASTHMA

**MYGENESET:KEGG_ASTHMA** — KEGG_ASTHMA (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy asthma pathway gene set (MSigDB C2 curated gene set). This is a disease pathway gene set representing the allergic inflammatory cascade in asthma. Member genes are dominated by Th2/type-2 immune effectors: immunoglobulin E (IgE) pathway components, MHC class II antigen-presenting molecules (HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1), Th2-polarising cytokines and their receptors (IL4, IL5, IL13, IL4R), mast cell and eosinophil effectors (FCER1A, FCER1G, MS4A2), and airway smooth muscle regulators. Antigen processing and presentation, IgE-mediated mast cell degranulation, eosinophil recruitment, and airway remodelling are the major mechanistic arms of the KEGG asthma pathway representation.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0004979 | asthma |
| anatomical_structure | UBERON:0002048 | lung |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0006954 | inflammatory response | biological_process | core_process | high |
| GO:0045064 | T-helper 2 cell differentiation | biological_process | core_process | high |
| GO:0019882 | antigen processing and presentation | biological_process | supporting_process | medium |
| GO:0042613 | MHC class II protein complex | cellular_component | core_component | medium |
| GO:0006955 | immune response | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (33 genes)

| Symbol | Gene ID |
|---|---|
| CCL11 | hgnc:10610 |
| CD40 | hgnc:11919 |
| CD40LG | hgnc:11935 |
| EPX | hgnc:3423 |
| FCER1A | hgnc:3609 |
| FCER1G | hgnc:3611 |
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
| IL10 | hgnc:5962 |
| IL13 | hgnc:5973 |
| IL3 | hgnc:6011 |
| IL4 | hgnc:6014 |
| IL5 | hgnc:6016 |
| IL9 | hgnc:6029 |
| MS4A2 | hgnc:7316 |
| PLPPR3 | hgnc:23497 |
| PRG2 | hgnc:9362 |
| PXDN | hgnc:14966 |
| RNASE3 | hgnc:10046 |
| TNF | hgnc:11892 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_ASTHMA.yaml` @ `c9af95e92cdd`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_ASTHMA) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_ASTHMA`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
