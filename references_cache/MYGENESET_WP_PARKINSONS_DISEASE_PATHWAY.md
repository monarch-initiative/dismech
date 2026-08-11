---
reference_id: "MYGENESET:WP_PARKINSONS_DISEASE_PATHWAY"
title: "WP_PARKINSONS_DISEASE_PATHWAY"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:WP_PARKINSONS_DISEASE_PATHWAY  WP_PARKINSONS_DISEASE_PATHWAY

**MYGENESET:WP_PARKINSONS_DISEASE_PATHWAY** — WP_PARKINSONS_DISEASE_PATHWAY (msigdb, C2:CP:WIKIPATHWAYS)

## Description

WikiPathways Parkinson's disease pathway gene set (MSigDB C2 curated gene set, collection C2:CP:WIKIPATHWAYS). This is a disease pathway gene set, not a cell-type signature. At 71 member genes, this set is substantially smaller than the KEGG legacy Parkinson's disease pathway and represents the mechanistic architecture of PD centred on its established causal genetic determinants: alpha-synuclein (SNCA) misfolding and Lewy body formation, the PINK1/Parkin axis mediating mitophagy of damaged mitochondria, ubiquitin-proteasome system (UPS) dysfunction (PRKN/parkin E3 ligase, UCHL1, proteasome subunits), dopaminergic neuron biology (TH, DDC, MAOB, SLC6A3), mitochondrial complex I dysfunction, and apoptotic dopaminergic neuron death. Unlike the KEGG PD legacy pathway — which is dominated by electron-transport-chain subunits — the WikiPathways PD set emphasises established PD causal gene products (SNCA, PRKN, PINK1, PARK7/DJ-1, LRRK2) and their molecular interactions. The PINK1/Parkin mitophagy pathway and alpha-synuclein aggregation biology are distinctive features relative to the KEGG version and are curated independently.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0005180 | Parkinson disease |
| anatomical_structure | UBERON:0000955 | brain |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0006511 | ubiquitin-dependent protein catabolic process | biological_process | core_process | high |
| GO:0000422 | autophagy of mitochondrion | biological_process | core_process | high |
| GO:0005739 | mitochondrion | cellular_component | core_component | high |
| GO:0042416 | dopamine biosynthetic process | biological_process | core_process | high |
| GO:1990000 | amyloid fibril formation | biological_process | core_process | medium |
| GO:0006915 | apoptotic process | biological_process | supporting_process | medium |
| GO:0051402 | neuron apoptotic process | biological_process | core_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (71 genes)

| Symbol | Gene ID |
|---|---|
| APAF1 | hgnc:576 |
| ATXN2 | hgnc:10555 |
| CASP2 | hgnc:1503 |
| CASP3 | hgnc:1504 |
| CASP6 | hgnc:1507 |
| CASP7 | hgnc:1508 |
| CASP9 | hgnc:1511 |
| CCNE1 | hgnc:1589 |
| CCNE2 | hgnc:1590 |
| CYCS | hgnc:19986 |
| DDC | hgnc:2719 |
| EPRS1 | hgnc:3418 |
| GPR37 | hgnc:4494 |
| HTRA2 | hgnc:14348 |
| LRRK2 | hgnc:18618 |
| MAPK11 | hgnc:6873 |
| MAPK12 | hgnc:6874 |
| MAPK13 | hgnc:6875 |
| MAPK14 | hgnc:6876 |
| MIR10A | hgnc:31497 |
| MIR1224 | hgnc:33923 |
| MIR127 | hgnc:31509 |
| MIR128-1 | hgnc:31510 |
| MIR128-2 | hgnc:31511 |
| MIR1294 | hgnc:35287 |
| MIR132 | hgnc:31516 |
| MIR136 | hgnc:31522 |
| MIR16-2 | hgnc:31546 |
| MIR18A | hgnc:31548 |
| MIR195 | hgnc:31566 |
| MIR19A | hgnc:31574 |
| MIR19B1 | hgnc:31575 |
| MIR19B2 | hgnc:31576 |
| MIR212 | hgnc:31589 |
| MIR26A1 | hgnc:31610 |
| MIR26A2 | hgnc:31611 |
| MIR26B | hgnc:31612 |
| MIR30A | hgnc:31624 |
| MIR30E | hgnc:31629 |
| MIR338 | hgnc:31775 |
| MIR34B | hgnc:31636 |
| MIR34C | hgnc:31637 |
| MIR370 | hgnc:31784 |
| MIR375 | hgnc:31868 |
| MIR409 | hgnc:32055 |
| MIR431 | hgnc:32027 |
| MIR433 | hgnc:32026 |
| MIR4448 | hgnc:41604 |
| MIR485 | hgnc:32067 |
| MIR503 | hgnc:32138 |
| MIR873 | hgnc:33663 |
| MIRLET7G | hgnc:31485 |
| PARK7 | hgnc:16369 |
| PINK1 | hgnc:14581 |
| PRKN | hgnc:8607 |
| SEPTIN5 | hgnc:9164 |
| SLC6A3 | hgnc:11049 |
| SNCA | hgnc:11138 |
| SNCAIP | hgnc:11139 |
| SYT11 | hgnc:19239 |
| TH | hgnc:11782 |
| UBA1 | hgnc:12469 |
| UBA7 | hgnc:12471 |
| UBB | hgnc:12463 |
| UBE2G1 | hgnc:12482 |
| UBE2G2 | hgnc:12483 |
| UBE2J1 | hgnc:17598 |
| UBE2J2 | hgnc:19268 |
| UBE2L3 | hgnc:12488 |
| UBE2L6 | hgnc:12490 |
| UCHL1 | hgnc:12513 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/WP_PARKINSONS_DISEASE_PATHWAY.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/WP_PARKINSONS_DISEASE_PATHWAY) (source: msigdb).

Upstream identifier: `MSIGDB:WP_PARKINSONS_DISEASE_PATHWAY`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
