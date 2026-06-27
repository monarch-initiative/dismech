---
reference_id: "MYGENESET:SANA_RESPONSE_TO_IFNG_UP"
title: "SANA_RESPONSE_TO_IFNG_UP"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:SANA_RESPONSE_TO_IFNG_UP  SANA_RESPONSE_TO_IFNG_UP

**MYGENESET:SANA_RESPONSE_TO_IFNG_UP** — SANA_RESPONSE_TO_IFNG_UP (msigdb, C2:CGP)

## Description

MSigDB C2:CGP signature of genes up-regulated by interferon-gamma (IFN-γ) stimulation across five primary human endothelial cell types (iliac artery, aortic, lung, colon, and dermal), as reported by Sana et al. (2005, PMID:15749026). A cytokine-perturbation UP signature: member genes are induced by IFN-γ in endothelium and encompass MHC class I antigen presentation machinery, CXCL chemokines (CXCL9/10/11), adhesion molecules (ICAM1), and interferon-stimulated genes. This is an independent endothelial dataset distinct from the Hallmark IFN-γ Response set (which is cell-type agnostic); both share the PR:000000017 interferon-gamma chemical_perturbagen context.

## Context

| Type | Term | Label |
|---|---|---|
| chemical_perturbagen | PR:000000017 | interferon gamma |
| cell_type | CL:0000115 | endothelial cell |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0071346 | cellular response to type II interferon | biological_process | core_process | high |
| GO:0019882 | antigen processing and presentation | biological_process | core_process | high |
| GO:0042612 | MHC class I protein complex | cellular_component | core_component | high |
| GO:0051607 | defense response to virus | biological_process | supporting_process | high |
| GO:0070098 | chemokine-mediated signaling pathway | biological_process | supporting_process | medium |
| GO:0050900 | leukocyte migration | biological_process | core_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (80 genes)

| Symbol | Gene ID |
|---|---|
| APOL1 | hgnc:618 |
| APOL2 | hgnc:619 |
| APOL3 | hgnc:14868 |
| APOL4 | hgnc:14867 |
| ATL1 | hgnc:11231 |
| ATP6V0A4 | hgnc:866 |
| BATF2 | hgnc:25163 |
| BST2 | hgnc:1119 |
| C1S | hgnc:1247 |
| CASP1 | hgnc:1499 |
| CD274 | hgnc:17635 |
| CD74 | hgnc:1697 |
| CEACAM1 | hgnc:1814 |
| CFH | hgnc:4883 |
| CX3CL1 | hgnc:10647 |
| CXCL10 | hgnc:10637 |
| CXCL11 | hgnc:10638 |
| CXCL9 | hgnc:7098 |
| DDX60 | hgnc:25942 |
| DTX3L | hgnc:30323 |
| ETV7 | hgnc:18160 |
| GBP1 | hgnc:4182 |
| GBP3 | hgnc:4184 |
| GIMAP7 | hgnc:22404 |
| GOLM1 | hgnc:15451 |
| HLA-A | hgnc:4931 |
| HLA-B | hgnc:4932 |
| HLA-C | hgnc:4933 |
| HLA-DMA | hgnc:4934 |
| HLA-DPA1 | hgnc:4938 |
| HLA-DQA1 | hgnc:4942 |
| HLA-DQB1 | hgnc:4944 |
| HLA-DQB2 | hgnc:4945 |
| HLA-DRB1 | hgnc:4948 |
| HLA-DRB3 | hgnc:4951 |
| HLA-DRB4 | hgnc:4952 |
| HLA-DRB5 | hgnc:4953 |
| HLA-E | hgnc:4962 |
| HSD17B11 | hgnc:22960 |
| IDO1 | hgnc:6059 |
| IFI35 | hgnc:5399 |
| IFI44L | hgnc:17817 |
| IFIH1 | hgnc:18873 |
| IL18BP | hgnc:5987 |
| IL23A | hgnc:15488 |
| LAP3 | hgnc:18449 |
| LGALS3BP | hgnc:6564 |
| LGALS9 | hgnc:6570 |
| LIPG | hgnc:6623 |
| MLKL | hgnc:26617 |
| MMP24 | hgnc:7172 |
| MMP25 | hgnc:14246 |
| MMP28 | hgnc:14366 |
| MX1 | hgnc:7532 |
| NCOA3 | hgnc:7670 |
| NLRC5 | hgnc:29933 |
| OAS1 | hgnc:8086 |
| OAS2 | hgnc:8087 |
| PARP14 | hgnc:29232 |
| PARP9 | hgnc:24118 |
| PLA1A | hgnc:17661 |
| PLAAT4 | hgnc:9869 |
| PPP3CA | hgnc:9314 |
| RABL3 | hgnc:18072 |
| RAC3 | hgnc:9803 |
| RNF213 | hgnc:14539 |
| SAMD9L | hgnc:1349 |
| SAMHD1 | hgnc:15925 |
| SEPTIN4 | hgnc:9165 |
| SERPING1 | hgnc:1228 |
| SLC25A28 | hgnc:23472 |
| SSPN | hgnc:11322 |
| ST8SIA4 | hgnc:10871 |
| STAT1 | hgnc:11362 |
| TNFSF10 | hgnc:11925 |
| TRIM22 | hgnc:16379 |
| UBD | hgnc:18795 |
| UBE2L6 | hgnc:12490 |
| VAMP5 | hgnc:12646 |
| WARS1 | hgnc:12729 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/SANA_RESPONSE_TO_IFNG_UP.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/SANA_RESPONSE_TO_IFNG_UP) (source: msigdb).

Upstream identifier: `MSIGDB:SANA_RESPONSE_TO_IFNG_UP`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
