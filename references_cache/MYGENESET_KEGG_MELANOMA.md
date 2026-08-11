---
reference_id: "MYGENESET:KEGG_MELANOMA"
title: "KEGG_MELANOMA"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_MELANOMA  KEGG_MELANOMA

**MYGENESET:KEGG_MELANOMA** — KEGG_MELANOMA (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy melanoma pathway gene set (MSigDB C2 curated gene set). This is a cancer disease pathway gene set, not a cell-type signature. The member genes are heavily enriched for RAS/RAF/MAPK pathway components (BRAF, NRAS, RAF1, MAP2K1/2, MAPK1/3), PI3K/AKT survival signaling effectors (PIK3CA, PTEN, AKT1), cell-cycle regulators controlling the G1/S transition (CDKN2A, CDK4, RB1, E2F family), apoptosis modulators (TP53, MDM2, BCL2-family, CASP3), and growth-factor receptor inputs (EGFR, MET, FGFR1), reflecting the major mechanistic arms of the KEGG melanoma pathway: BRAF-driven MAPK proliferative signaling, PI3K/AKT cell-survival signaling, CDKN2A/RB-mediated cell-cycle control, and TP53-dependent apoptosis evasion, all operating in the melanocyte cell-of-origin context.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0005105 | melanoma |
| anatomical_structure | UBERON:0002097 | skin of body |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0000165 | MAPK cascade | biological_process | core_process | high |
| GO:0042127 | regulation of cell population proliferation | biological_process | core_process | high |
| GO:0043491 | phosphatidylinositol 3-kinase/protein kinase B signal transduction | biological_process | supporting_process | medium |
| GO:0000082 | G1/S transition of mitotic cell cycle | biological_process | supporting_process | medium |
| GO:0006915 | apoptotic process | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0030318 | melanocyte differentiation | biological_process | supporting_process | medium |

## Members (78 genes)

| Symbol | Gene ID |
|---|---|
| AKT1 | hgnc:391 |
| AKT2 | hgnc:392 |
| AKT3 | hgnc:393 |
| ARAF | hgnc:646 |
| BAD | hgnc:936 |
| BRAF | hgnc:1097 |
| CCND1 | hgnc:1582 |
| CDH1 | hgnc:1748 |
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
| FGF1 | hgnc:3665 |
| FGF10 | hgnc:3666 |
| FGF11 | hgnc:3667 |
| FGF12 | hgnc:3668 |
| FGF13 | hgnc:3670 |
| FGF14 | hgnc:3671 |
| FGF16 | hgnc:3672 |
| FGF17 | hgnc:3673 |
| FGF18 | hgnc:3674 |
| FGF19 | hgnc:3675 |
| FGF2 | hgnc:3676 |
| FGF20 | hgnc:3677 |
| FGF21 | hgnc:3678 |
| FGF22 | hgnc:3679 |
| FGF23 | hgnc:3680 |
| FGF3 | hgnc:3681 |
| FGF4 | hgnc:3682 |
| FGF5 | hgnc:3683 |
| FGF6 | hgnc:3684 |
| FGF7 | hgnc:3685 |
| FGF8 | hgnc:3686 |
| FGF9 | hgnc:3687 |
| FGFR1 | hgnc:3688 |
| FZR1 | hgnc:24824 |
| HGF | hgnc:4893 |
| HRAS | hgnc:5173 |
| IGF1 | hgnc:5464 |
| IGF1R | hgnc:5465 |
| IL6 | hgnc:6018 |
| KRAS | hgnc:6407 |
| MAP2K1 | hgnc:6840 |
| MAP2K2 | hgnc:6842 |
| MAPK1 | hgnc:6871 |
| MAPK3 | hgnc:6877 |
| MDM2 | hgnc:6973 |
| MET | hgnc:7029 |
| MITF | hgnc:7105 |
| NRAS | hgnc:7989 |
| PDGFA | hgnc:8799 |
| PDGFB | hgnc:8800 |
| PDGFC | hgnc:8801 |
| PDGFD | hgnc:30620 |
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
| PTEN | hgnc:9588 |
| RAF1 | hgnc:9829 |
| RB1 | hgnc:9884 |
| RNASE3 | hgnc:10046 |
| RNMT | hgnc:10075 |
| SLTM | hgnc:20709 |
| SOS1 | hgnc:11187 |
| TP53 | hgnc:11998 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_MELANOMA.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_MELANOMA) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_MELANOMA`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
