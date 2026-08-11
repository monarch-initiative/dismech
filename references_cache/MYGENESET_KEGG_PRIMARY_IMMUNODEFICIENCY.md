---
reference_id: "MYGENESET:KEGG_PRIMARY_IMMUNODEFICIENCY"
title: "KEGG_PRIMARY_IMMUNODEFICIENCY"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_PRIMARY_IMMUNODEFICIENCY  KEGG_PRIMARY_IMMUNODEFICIENCY

**MYGENESET:KEGG_PRIMARY_IMMUNODEFICIENCY** — KEGG_PRIMARY_IMMUNODEFICIENCY (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy primary immunodeficiency pathway gene set (MSigDB C2 curated gene set). This is a disease pathway gene set whose members are genes whose loss-of-function mutations cause inherited primary immunodeficiency disorders. The member genes span the major mechanistic arms of lymphocyte development and function: B cell development (BTK, RAG1/RAG2, ADA, CD40, CD40LG, AICDA), T cell development and signalling (IL2RG, JAK3, RAG1/RAG2, ZAP70, CD3D/CD3E/CD3G, CD8A/CD8B1), thymic central tolerance (AIRE), and cytoskeletal regulation (WAS). Because these genes encode processes essential for lymphocyte development and adaptive immunity, the represented biology is the NORMAL function that is lost in disease: T cell differentiation, B cell differentiation, V(D)J recombination, cytokine-receptor signalling, and thymic selection. The gene set is dominated by combined immunodeficiency (SCID) and B cell immunodeficiency (XLA, hyper-IgM) genes, reflecting the major disease categories of the KEGG primary immunodeficiency pathway. Unlike expression-based gene sets, the causal disease direction (loss of function) is not captured by GO annotations, so associations describe the underlying normal biology rather than a disease-elevated gene signature.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0003778 | inborn error of immunity |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0030217 | T cell differentiation | biological_process | core_process | high |
| GO:0030183 | B cell differentiation | biological_process | core_process | high |
| GO:0042101 | T cell receptor complex | cellular_component | core_component | high |
| GO:0030098 | lymphocyte differentiation | biological_process | supporting_process | medium |
| GO:0016447 | somatic recombination of immunoglobulin gene segments | biological_process | supporting_process | medium |
| GO:0002250 | adaptive immune response | biological_process | supporting_process | medium |
| GO:0006955 | immune response | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0045060 | negative thymic T cell selection | biological_process | core_process | medium |

## Members (37 genes)

| Symbol | Gene ID |
|---|---|
| ADA | hgnc:186 |
| AICDA | hgnc:13203 |
| AIRE | hgnc:360 |
| BLNK | hgnc:14211 |
| BTK | hgnc:1133 |
| CD19 | hgnc:1633 |
| CD3D | hgnc:1673 |
| CD3E | hgnc:1674 |
| CD4 | hgnc:1678 |
| CD40 | hgnc:11919 |
| CD40LG | hgnc:11935 |
| CD79A | hgnc:1698 |
| CD8A | hgnc:1706 |
| CD8B | hgnc:1707 |
| CIITA | hgnc:7067 |
| DCLRE1C | hgnc:17642 |
| ICOS | hgnc:5351 |
| IGLL1 | hgnc:5870 |
| IKBKG | hgnc:5961 |
| IL2RG | hgnc:6010 |
| IL7R | hgnc:6024 |
| JAK3 | hgnc:6193 |
| LCK | hgnc:6524 |
| PTPRC | hgnc:9666 |
| RAG1 | hgnc:9831 |
| RAG2 | hgnc:9832 |
| RFX5 | hgnc:9986 |
| RFXANK | hgnc:9987 |
| RFXAP | hgnc:9988 |
| SEC14L2 | hgnc:10699 |
| SEC14L3 | hgnc:18655 |
| TAP1 | hgnc:43 |
| TAP2 | hgnc:44 |
| TNFRSF13B | hgnc:18153 |
| TNFRSF13C | hgnc:17755 |
| UNG | hgnc:12572 |
| ZAP70 | hgnc:12858 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_PRIMARY_IMMUNODEFICIENCY.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_PRIMARY_IMMUNODEFICIENCY) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_PRIMARY_IMMUNODEFICIENCY`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
