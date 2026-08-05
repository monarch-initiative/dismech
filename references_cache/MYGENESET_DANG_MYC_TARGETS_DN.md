---
reference_id: "MYGENESET:DANG_MYC_TARGETS_DN"
title: "DANG_MYC_TARGETS_DN"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:DANG_MYC_TARGETS_DN  DANG_MYC_TARGETS_DN

**MYGENESET:DANG_MYC_TARGETS_DN** — DANG_MYC_TARGETS_DN (msigdb, C2:CGP)

## Description

MSigDB C2:CGP genetic-perturbation signature of genes DOWN-regulated by the MYC oncogene (Zeller/Dang, PMID:14519204). This 31-gene set represents the DOWN component of the MYC transcriptional program — genes whose promoters are bound by MYC and whose expression is repressed upon MYC activation. The set is enriched for cell-adhesion molecules (integrins, thrombospondin-1/THBS1), growth-arrest mediators (CDKN1A/p21), extracellular matrix proteins, and differentiation-associated genes, reflecting MYC's oncogenic function of silencing growth-restraint and differentiation programs. Unlike the MYC-UP set, the DN set does not enrich for translation or ribosomal biogenesis; spurious translation enrichment is not expected and is excluded here.

## Context

| Type | Term | Label |
|---|---|---|
| genetic_perturbation | PR:P01106 | Myc proto-oncogene protein (human) |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0007155 | cell adhesion | biological_process | core_process | high |
| GO:0008285 | negative regulation of cell population proliferation | biological_process | core_process | high |
| GO:0031012 | extracellular matrix | cellular_component | core_component | medium |
| GO:0030154 | cell differentiation | biological_process | supporting_process | medium |
| GO:0030198 | extracellular matrix organization | biological_process | supporting_process | medium |
| GO:0071559 | response to transforming growth factor beta | biological_process | supporting_process | low |

## Members (32 genes)

| Symbol | Gene ID |
|---|---|
| ACP5 | hgnc:124 |
| ALDH9A1 | hgnc:412 |
| APP | hgnc:620 |
| ARPC4 | hgnc:707 |
| CDKN1B | hgnc:1785 |
| CDKN2B | hgnc:1788 |
| CEBPA | hgnc:1833 |
| CSDE1 | hgnc:29905 |
| DLEU2 | hgnc:13748 |
| DNTT | hgnc:2983 |
| ERBB2 | hgnc:3430 |
| GTF2H2 | hgnc:4656 |
| HMOX1 | hgnc:5013 |
| ID3 | hgnc:5362 |
| ILK | hgnc:6040 |
| ITGB1 | hgnc:6153 |
| LAMC1 | hgnc:6492 |
| LAMP1 | hgnc:6499 |
| MSN | hgnc:7373 |
| MYC | hgnc:7553 |
| NDRG1 | hgnc:7679 |
| PDGFB | hgnc:8800 |
| PTPA | hgnc:9308 |
| PTPN1 | hgnc:9642 |
| PTPRA | hgnc:9664 |
| RARA | hgnc:9864 |
| SERPINE1 | hgnc:8583 |
| SFXN3 | hgnc:16087 |
| TGFB1 | hgnc:11766 |
| TMEM126A | hgnc:25382 |
| VHL | hgnc:12687 |
| ZFP36L1 | hgnc:1107 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/DANG_MYC_TARGETS_DN.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/DANG_MYC_TARGETS_DN) (source: msigdb).

Upstream identifier: `MSIGDB:DANG_MYC_TARGETS_DN`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
