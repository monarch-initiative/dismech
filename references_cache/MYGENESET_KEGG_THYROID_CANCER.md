---
reference_id: "MYGENESET:KEGG_THYROID_CANCER"
title: "KEGG_THYROID_CANCER"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_THYROID_CANCER  KEGG_THYROID_CANCER

**MYGENESET:KEGG_THYROID_CANCER** — KEGG_THYROID_CANCER (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy thyroid cancer pathway gene set (MSigDB C2 curated gene set). This is a cancer disease pathway gene set, not a cell-type signature. The member genes are enriched for components of the RET/PTC–RAS–BRAF–MAPK signaling axis (the dominant oncogenic driver in papillary thyroid carcinoma), the PAX8–PPARG fusion and PAX8/NKX2-1 transcription factor network, CTNNB1/Wnt signaling components, and regulators of cell proliferation. A defining biological feature captured in this gene set is dedifferentiation: constitutive MAPK activation leads to loss of thyroid-specific differentiation markers (NIS/SLC5A5, thyroglobulin, TSH receptor), a clinically significant hallmark of radioactive-iodine–refractory thyroid cancer. The PAX8-PPARG fusion, recurring in follicular thyroid carcinomas, and activating CTNNB1 mutations, enriched in anaplastic/poorly-differentiated carcinomas, provide additional mechanistic arms in this gene set.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0002108 | thyroid cancer |
| anatomical_structure | UBERON:0002046 | thyroid gland |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0000165 | MAPK cascade | biological_process | core_process | high |
| GO:0042127 | regulation of cell population proliferation | biological_process | core_process | high |
| GO:0006357 | regulation of transcription by RNA polymerase II | biological_process | supporting_process | medium |
| GO:0016055 | Wnt signaling pathway | biological_process | supporting_process | medium |
| GO:0030154 | cell differentiation | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0030878 | thyroid gland development | biological_process | supporting_process | medium |

## Members (30 genes)

| Symbol | Gene ID |
|---|---|
| BRAF | hgnc:1097 |
| CCDC6 | hgnc:18782 |
| CCND1 | hgnc:1582 |
| CDH1 | hgnc:1748 |
| CTNNB1 | hgnc:2514 |
| FZR1 | hgnc:24824 |
| HRAS | hgnc:5173 |
| KRAS | hgnc:6407 |
| LEF1 | hgnc:6551 |
| MAP2K1 | hgnc:6840 |
| MAP2K2 | hgnc:6842 |
| MAPK1 | hgnc:6871 |
| MAPK3 | hgnc:6877 |
| MYC | hgnc:7553 |
| NCOA4 | hgnc:7671 |
| NRAS | hgnc:7989 |
| NTRK1 | hgnc:8031 |
| PAX8 | hgnc:8622 |
| PPARG | hgnc:9236 |
| RET | hgnc:9967 |
| RXRA | hgnc:10477 |
| RXRB | hgnc:10478 |
| RXRG | hgnc:10479 |
| TCF7 | hgnc:11639 |
| TCF7L1 | hgnc:11640 |
| TCF7L2 | hgnc:11641 |
| TFG | hgnc:11758 |
| TP53 | hgnc:11998 |
| TPM3 | hgnc:12012 |
| TPR | hgnc:12017 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_THYROID_CANCER.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_THYROID_CANCER) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_THYROID_CANCER`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
