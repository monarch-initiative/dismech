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

| Symbol | NCBI Gene |
|---|---|
| CCL11 | NCBIGene:6356 |
| CD40 | NCBIGene:958 |
| CD40LG | NCBIGene:959 |
| EPX | NCBIGene:8288 |
| FCER1A | NCBIGene:2205 |
| FCER1G | NCBIGene:2207 |
| HLA-DMA | NCBIGene:3108 |
| HLA-DMB | NCBIGene:3109 |
| HLA-DOA | NCBIGene:3111 |
| HLA-DOB | NCBIGene:3112 |
| HLA-DPA1 | NCBIGene:3113 |
| HLA-DPB1 | NCBIGene:3115 |
| HLA-DQA1 | NCBIGene:3117 |
| HLA-DQA2 | NCBIGene:3118 |
| HLA-DQB1 | NCBIGene:3119 |
| HLA-DQB2 | NCBIGene:3120 |
| HLA-DRA | NCBIGene:3122 |
| HLA-DRB1 | NCBIGene:3123 |
| HLA-DRB3 | NCBIGene:3125 |
| HLA-DRB4 | NCBIGene:3126 |
| HLA-DRB5 | NCBIGene:3127 |
| IL10 | NCBIGene:3586 |
| IL13 | NCBIGene:3596 |
| IL3 | NCBIGene:3562 |
| IL4 | NCBIGene:3565 |
| IL5 | NCBIGene:3567 |
| IL9 | NCBIGene:3578 |
| MS4A2 | NCBIGene:2206 |
| PLPPR3 | NCBIGene:79948 |
| PRG2 | NCBIGene:5553 |
| PXDN | NCBIGene:7837 |
| RNASE3 | NCBIGene:6037 |
| TNF | NCBIGene:7124 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_ASTHMA.yaml` @ `c9af95e92cdd`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_ASTHMA) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_ASTHMA`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
