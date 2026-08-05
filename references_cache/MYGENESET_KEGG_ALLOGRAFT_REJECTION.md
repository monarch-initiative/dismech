---
reference_id: "MYGENESET:KEGG_ALLOGRAFT_REJECTION"
title: "KEGG_ALLOGRAFT_REJECTION"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_ALLOGRAFT_REJECTION  KEGG_ALLOGRAFT_REJECTION

**MYGENESET:KEGG_ALLOGRAFT_REJECTION** — KEGG_ALLOGRAFT_REJECTION (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy allograft rejection pathway gene set (MSigDB C2 curated gene set). This is a disease pathway gene set representing alloimmune-mediated tissue destruction following solid organ or tissue transplantation. Host (recipient) T cells recognise donor MHC alloantigens presented on transplanted tissue, then clonally expand and differentiate into effector cells that destroy graft tissue through direct cytotoxicity (perforin-granzyme and Fas-FasL pathways) and pro-inflammatory cytokine release (TNF, IL-1alpha/beta, IFN-gamma, IL-2). NK cells contribute additional cytotoxic killing via shared perforin-granzyme machinery. Member genes are enriched for MHC class I (HLA-A, HLA-B, HLA-C, B2M) and class II (HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1, HLA-DPA1, HLA-DPB1) molecules, cytotoxic effectors (PRF1, GZMB, FASLG), cytokine and cytokine-receptor signalling components (IL2, IL1A, IL1B, TNF, IFNG, IL6, IL10), and co-stimulatory molecules (CD80, CD86, CD28). This pathway represents host-versus-graft directionality — recipient immune cells attacking the donor organ — and should be distinguished from graft-versus-host disease (GVHD), where the reverse polarity applies: donor T cells attacking host tissue. As a legacy KEGG pathway representation, the set captures the established alloimmune effector phase and omits some regulatory and upstream priming events.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:1010185 | transplant rejection |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0019882 | antigen processing and presentation | biological_process | core_process | high |
| GO:0001913 | T cell mediated cytotoxicity | biological_process | core_process | high |
| GO:0042267 | natural killer cell mediated cytotoxicity | biological_process | supporting_process | medium |
| GO:0042612 | MHC class I protein complex | cellular_component | core_component | high |
| GO:0006955 | immune response | biological_process | supporting_process | medium |
| GO:0006954 | inflammatory response | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |
| GO:0002250 | adaptive immune response | biological_process | supporting_process | medium |

## Members (40 genes)

| Symbol | Gene ID |
|---|---|
| CD28 | hgnc:1653 |
| CD40 | hgnc:11919 |
| CD40LG | hgnc:11935 |
| CD80 | hgnc:1700 |
| CD86 | hgnc:1705 |
| FAS | hgnc:11920 |
| FASLG | hgnc:11936 |
| FASN | hgnc:3594 |
| GZMB | hgnc:4709 |
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
| IFNG | hgnc:5438 |
| IL10 | hgnc:5962 |
| IL12A | hgnc:5969 |
| IL12B | hgnc:5970 |
| IL2 | hgnc:6001 |
| IL4 | hgnc:6014 |
| IL5 | hgnc:6016 |
| PRF1 | hgnc:9360 |
| TNF | hgnc:11892 |
| ZNF395 | hgnc:18737 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_ALLOGRAFT_REJECTION.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_ALLOGRAFT_REJECTION) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_ALLOGRAFT_REJECTION`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
