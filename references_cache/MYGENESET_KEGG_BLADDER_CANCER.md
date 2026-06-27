---
reference_id: "MYGENESET:KEGG_BLADDER_CANCER"
title: "KEGG_BLADDER_CANCER"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_BLADDER_CANCER  KEGG_BLADDER_CANCER

**MYGENESET:KEGG_BLADDER_CANCER** — KEGG_BLADDER_CANCER (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy bladder cancer pathway gene set (MSigDB C2 curated gene set). This is a cancer disease pathway gene set, not a cell-type signature. The member genes are heavily enriched for RAS/RAF/MAPK pathway components (HRAS, NRAS, RAF1, MAP2K1/2, MAPK1/3), cell-cycle regulators and tumour suppressors from the RB/TP53 axis (RB1, TP53, CDKN2A, CDK4, MDM2, E2F family), PI3K/AKT survival effectors (PIK3CA, PTEN, AKT1), VEGF-driven angiogenesis components (VEGFA, FLT1, KDR), and ECM/invasion machinery (MMP family, integrin subunits), reflecting the major mechanistic arms of the KEGG urinary bladder cancer pathway: RAS-MAPK-driven proliferative signalling, RB/TP53-mediated cell-cycle control, VEGF-stimulated tumour angiogenesis, ECM remodelling for local invasion, and apoptosis evasion.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0004986 | urinary bladder carcinoma |
| anatomical_structure | UBERON:0001255 | urinary bladder |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0000165 | MAPK cascade | biological_process | core_process | high |
| GO:0042127 | regulation of cell population proliferation | biological_process | core_process | high |
| GO:0001525 | angiogenesis | biological_process | supporting_process | medium |
| GO:0006915 | apoptotic process | biological_process | supporting_process | medium |
| GO:0007155 | cell adhesion | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0031012 | extracellular matrix | cellular_component | core_component | medium |

## Members (45 genes)

| Symbol | Gene ID |
|---|---|
| ARAF | hgnc:646 |
| BRAF | hgnc:1097 |
| CCND1 | hgnc:1582 |
| CDH1 | hgnc:1748 |
| CDK4 | hgnc:1773 |
| CDKN1A | hgnc:1784 |
| CDKN2A | hgnc:1787 |
| CDPF1 | hgnc:33710 |
| CXCL8 | hgnc:6025 |
| DAPK1 | hgnc:2674 |
| DAPK2 | hgnc:2675 |
| DAPK3 | hgnc:2676 |
| E2F1 | hgnc:3113 |
| E2F2 | hgnc:3114 |
| E2F3 | hgnc:3115 |
| EGF | hgnc:3229 |
| EGFR | hgnc:3236 |
| ERBB2 | hgnc:3430 |
| FGFR3 | hgnc:3690 |
| FZR1 | hgnc:24824 |
| HRAS | hgnc:5173 |
| KRAS | hgnc:6407 |
| MAP2K1 | hgnc:6840 |
| MAP2K2 | hgnc:6842 |
| MAPK1 | hgnc:6871 |
| MAPK3 | hgnc:6877 |
| MDM2 | hgnc:6973 |
| MMP1 | hgnc:7155 |
| MMP2 | hgnc:7166 |
| MMP9 | hgnc:7176 |
| MYC | hgnc:7553 |
| NRAS | hgnc:7989 |
| PGF | hgnc:8893 |
| RAF1 | hgnc:9829 |
| RASSF1 | hgnc:9882 |
| RB1 | hgnc:9884 |
| RNASE3 | hgnc:10046 |
| RPS6KA5 | hgnc:10434 |
| THBS1 | hgnc:11785 |
| TP53 | hgnc:11998 |
| TYMP | hgnc:3148 |
| VEGFA | hgnc:12680 |
| VEGFB | hgnc:12681 |
| VEGFC | hgnc:12682 |
| VEGFD | hgnc:3708 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_BLADDER_CANCER.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_BLADDER_CANCER) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_BLADDER_CANCER`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
