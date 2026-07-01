---
reference_id: "MYGENESET:KEGG_VIRAL_MYOCARDITIS"
title: "KEGG_VIRAL_MYOCARDITIS"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_VIRAL_MYOCARDITIS  KEGG_VIRAL_MYOCARDITIS

**MYGENESET:KEGG_VIRAL_MYOCARDITIS** — KEGG_VIRAL_MYOCARDITIS (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy viral myocarditis pathway gene set (MSigDB C2 curated gene set). This is an infection-driven inflammatory heart disease pathway gene set, not a cell-type signature. The member genes are drawn from three mechanistic arms: (1) MHC-mediated antigen presentation and adaptive immune activation, in which virus-infected cardiomyocytes display viral peptides via upregulated MHC class I molecules (HLA-A/B/C, B2M, TAP1/TAP2, TAPBP) and professional antigen-presenting cells engage MHC class II (HLA-DR); (2) immune-mediated cardiomyocyte killing by CD8 cytotoxic T cells and NK cells using the perforin/granzyme (PRF1, GZMA, GZMB) and Fas/FasL (FAS, FASLG) cytotoxic programs, amplified by inflammatory cytokines (TNF, IFNG, IL1B, IL6, IL10); and (3) direct cytoskeletal disruption via enteroviral protease 2A cleavage of dystrophin (DMD), uncoupling the sarcomere from the sarcolemma through the dystrophin-associated glycoprotein complex (DMD, SGCA/B/G/D, DAG1, SNTA1) — a mechanism shared with the KEGG dilated cardiomyopathy pathway. As a KEGG legacy pathway it captures established mechanistic arms known at the time of curation.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0023161 | viral myocarditis |
| anatomical_structure | UBERON:0000948 | heart |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0019882 | antigen processing and presentation | biological_process | core_process | high |
| GO:0001913 | T cell mediated cytotoxicity | biological_process | core_process | high |
| GO:0042612 | MHC class I protein complex | cellular_component | core_component | high |
| GO:0006954 | inflammatory response | biological_process | supporting_process | medium |
| GO:0016010 | dystrophin-associated glycoprotein complex | cellular_component | core_component | high |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0051607 | defense response to virus | biological_process | supporting_process | medium |

## Members (74 genes)

| Symbol | Gene ID |
|---|---|
| ABL1 | hgnc:76 |
| ABL2 | hgnc:77 |
| ACTB | hgnc:132 |
| ACTG1 | hgnc:144 |
| BID | hgnc:1050 |
| CASP3 | hgnc:1504 |
| CASP8 | hgnc:1509 |
| CASP9 | hgnc:1511 |
| CAV1 | hgnc:1527 |
| CCND1 | hgnc:1582 |
| CD28 | hgnc:1653 |
| CD40 | hgnc:11919 |
| CD40LG | hgnc:11935 |
| CD55 | hgnc:2665 |
| CD80 | hgnc:1700 |
| CD86 | hgnc:1705 |
| CXADR | hgnc:2559 |
| CYCS | hgnc:19986 |
| DAG1 | hgnc:2666 |
| DMD | hgnc:2928 |
| EIF4G1 | hgnc:3296 |
| EIF4G2 | hgnc:3297 |
| EIF4G3 | hgnc:3298 |
| FYN | hgnc:4037 |
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
| ICAM1 | hgnc:5344 |
| ITGAL | hgnc:6148 |
| ITGB2 | hgnc:6155 |
| LAMA2 | hgnc:6482 |
| MYH1 | hgnc:7567 |
| MYH10 | hgnc:7568 |
| MYH11 | hgnc:7569 |
| MYH13 | hgnc:7571 |
| MYH14 | hgnc:23212 |
| MYH15 | hgnc:31073 |
| MYH2 | hgnc:7572 |
| MYH3 | hgnc:7573 |
| MYH4 | hgnc:7574 |
| MYH6 | hgnc:7576 |
| MYH7 | hgnc:7577 |
| MYH7B | hgnc:15906 |
| MYH8 | hgnc:7578 |
| MYH9 | hgnc:7579 |
| NCOA3 | hgnc:7670 |
| PRF1 | hgnc:9360 |
| RAC1 | hgnc:9801 |
| RAC2 | hgnc:9802 |
| RAC3 | hgnc:9803 |
| RNASE1 | hgnc:10044 |
| SGCA | hgnc:10805 |
| SGCB | hgnc:10806 |
| SGCD | hgnc:10807 |
| SGCG | hgnc:10809 |
| ZNF395 | hgnc:18737 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_VIRAL_MYOCARDITIS.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_VIRAL_MYOCARDITIS) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_VIRAL_MYOCARDITIS`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
