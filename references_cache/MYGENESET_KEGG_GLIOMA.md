---
reference_id: "MYGENESET:KEGG_GLIOMA"
title: "KEGG_GLIOMA"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_GLIOMA  KEGG_GLIOMA

**MYGENESET:KEGG_GLIOMA** — KEGG_GLIOMA (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy glioma pathway gene set (MSigDB C2 curated gene set). This is a cancer disease pathway gene set, not a cell-type signature. The member genes are heavily enriched for growth-factor receptor signaling components (EGFR, PDGFRA/B and their downstream effectors), RAS/MAPK pathway members (HRAS, KRAS, NRAS, RAF1, MAP2K1, MAPK1/3), PI3K/AKT effectors (PIK3CA, PIK3R1, PTEN, AKT1), cell-cycle regulators driving G1/S transition (CDKN2A, CDK4, CDK6, CCND1, RB1, E2F family), and the TP53 tumor-suppressor axis, reflecting the major mechanistic arms of the KEGG glioma pathway: receptor tyrosine kinase-driven initiation, RAS/MAPK-mediated proliferation, PI3K/AKT survival signaling, cell-cycle checkpoint bypass, and TP53-mediated apoptosis deregulation.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0005499 | brain glioma |
| anatomical_structure | UBERON:0000955 | brain |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0007173 | epidermal growth factor receptor signaling pathway | biological_process | core_process | high |
| GO:0042127 | regulation of cell population proliferation | biological_process | core_process | high |
| GO:0000165 | MAPK cascade | biological_process | supporting_process | medium |
| GO:0043491 | phosphatidylinositol 3-kinase/protein kinase B signal transduction | biological_process | supporting_process | medium |
| GO:0000082 | G1/S transition of mitotic cell cycle | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (67 genes)

| Symbol | Gene ID |
|---|---|
| AKT1 | hgnc:391 |
| AKT2 | hgnc:392 |
| AKT3 | hgnc:393 |
| ARAF | hgnc:646 |
| BRAF | hgnc:1097 |
| CALM1 | hgnc:1442 |
| CALM2 | hgnc:1445 |
| CALM3 | hgnc:1449 |
| CALML3 | hgnc:1452 |
| CALML5 | hgnc:18180 |
| CALML6 | hgnc:24193 |
| CAMK2A | hgnc:1460 |
| CAMK2B | hgnc:1461 |
| CAMK2D | hgnc:1462 |
| CAMK2G | hgnc:1463 |
| CCND1 | hgnc:1582 |
| CDK4 | hgnc:1773 |
| CDK6 | hgnc:1777 |
| CDKN1A | hgnc:1784 |
| CDKN2A | hgnc:1787 |
| CDPF1 | hgnc:33710 |
| E2F1 | hgnc:3113 |
| E2F2 | hgnc:3114 |
| E2F3 | hgnc:3115 |
| EGF | hgnc:3229 |
| EGFR | hgnc:3236 |
| GRB2 | hgnc:4566 |
| HRAS | hgnc:5173 |
| IGF1 | hgnc:5464 |
| IGF1R | hgnc:5465 |
| KRAS | hgnc:6407 |
| MAP2K1 | hgnc:6840 |
| MAP2K2 | hgnc:6842 |
| MAPK1 | hgnc:6871 |
| MAPK3 | hgnc:6877 |
| MDM2 | hgnc:6973 |
| MTOR | hgnc:3942 |
| NRAS | hgnc:7989 |
| PDGFA | hgnc:8799 |
| PDGFB | hgnc:8800 |
| PDGFRA | hgnc:8803 |
| PDGFRB | hgnc:8804 |
| PIK3CA | hgnc:8975 |
| PIK3CB | hgnc:8976 |
| PIK3CD | hgnc:8977 |
| PIK3CG | hgnc:8978 |
| PIK3R1 | hgnc:8979 |
| PIK3R2 | hgnc:8980 |
| PIK3R3 | hgnc:8981 |
| PIK3R5 | hgnc:30035 |
| PLCG1 | hgnc:9065 |
| PLCG2 | hgnc:9066 |
| PRKCA | hgnc:9393 |
| PRKCB | hgnc:9395 |
| PRKCG | hgnc:9402 |
| PTEN | hgnc:9588 |
| RAF1 | hgnc:9829 |
| RB1 | hgnc:9884 |
| RNASE3 | hgnc:10046 |
| SHC1 | hgnc:10840 |
| SHC2 | hgnc:29869 |
| SHC3 | hgnc:18181 |
| SHC4 | hgnc:16743 |
| SOS1 | hgnc:11187 |
| SOS2 | hgnc:11188 |
| TGFA | hgnc:11765 |
| TP53 | hgnc:11998 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_GLIOMA.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_GLIOMA) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_GLIOMA`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
