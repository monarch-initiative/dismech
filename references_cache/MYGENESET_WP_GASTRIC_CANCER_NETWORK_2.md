---
reference_id: "MYGENESET:WP_GASTRIC_CANCER_NETWORK_2"
title: "WP_GASTRIC_CANCER_NETWORK_2"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:WP_GASTRIC_CANCER_NETWORK_2  WP_GASTRIC_CANCER_NETWORK_2

**MYGENESET:WP_GASTRIC_CANCER_NETWORK_2** — WP_GASTRIC_CANCER_NETWORK_2 (msigdb, C2:CP:WIKIPATHWAYS)

## Description

WikiPathways gastric cancer network 2 gene set (MSigDB C2:CP:WIKIPATHWAYS, 32 genes). This cancer disease pathway gene set captures the receptor tyrosine kinase / RAS-MAPK and PI3K/AKT signalling axes that drive gastric (stomach) carcinoma proliferation and survival, together with cell-cycle deregulation and apoptosis dysregulation. In contrast to the first gastric cancer network (WP_GASTRIC_CANCER_NETWORK_1), this set emphasises RTK-initiated oncogenic cascades: EGFR, HER2/ERBB2, FGFR2, and MET are among the receptor tyrosine kinases frequently amplified or mutated in gastric cancer that initiate downstream RAS-RAF-MEK-ERK (MAPK cascade) and PI3K-AKT survival signalling. Oncogenic KRAS mutations and HER2 amplification are the best-characterised drivers in this gene set. Downstream cell-cycle entry is mediated by cyclin D1 (CCND1) in complex with CDK4/CDK6 driving G1/S transition, while apoptosis evasion involves BCL2-family members and TP53 inactivation. The set thus represents the mitogenic signalling hierarchy from cell-surface RTK through MAPK and PI3K second-messenger cascades to proliferative and anti-apoptotic transcriptional outputs.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0004950 | gastric carcinoma |
| anatomical_structure | UBERON:0000945 | stomach |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0000165 | MAPK cascade | biological_process | core_process | high |
| GO:0042127 | regulation of cell population proliferation | biological_process | core_process | high |
| GO:0043491 | phosphatidylinositol 3-kinase/protein kinase B signal transduction | biological_process | supporting_process | medium |
| GO:2000045 | regulation of G1/S transition of mitotic cell cycle | biological_process | supporting_process | medium |
| GO:0006915 | apoptotic process | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (35 genes)

| Symbol | Gene ID |
|---|---|
| AHCTF1 | hgnc:24618 |
| ATAD2 | hgnc:30123 |
| BRIX1 | hgnc:24170 |
| CACYBP | hgnc:30423 |
| CD48 | hgnc:1683 |
| CEBPZ | hgnc:24218 |
| CHTF18 | hgnc:18435 |
| CHTF8 | hgnc:24353 |
| COL9A1 | hgnc:2217 |
| COL9A3 | hgnc:2219 |
| CTNNB1 | hgnc:2514 |
| DDIT3 | hgnc:2726 |
| DSCC1 | hgnc:24453 |
| EGFR | hgnc:3236 |
| FAM91A1 | hgnc:26306 |
| FANCI | hgnc:25568 |
| LBR | hgnc:6518 |
| LGALS13 | hgnc:15449 |
| LMNB2 | hgnc:6638 |
| MIRLET7E | hgnc:31482 |
| MTDH | hgnc:29608 |
| MYC | hgnc:7553 |
| OTUD5 | hgnc:25402 |
| PLAC8 | hgnc:19254 |
| RAD17 | hgnc:9807 |
| RFC3 | hgnc:9971 |
| RFC4 | hgnc:9972 |
| RNF144B | hgnc:21578 |
| RNF4 | hgnc:10067 |
| S100A6 | hgnc:10496 |
| SNURF | hgnc:11171 |
| TOP2A | hgnc:11989 |
| TP53 | hgnc:11998 |
| UBE2C | hgnc:15937 |
| UBE2T | hgnc:25009 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/WP_GASTRIC_CANCER_NETWORK_2.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/WP_GASTRIC_CANCER_NETWORK_2) (source: msigdb).

Upstream identifier: `MSIGDB:WP_GASTRIC_CANCER_NETWORK_2`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
