---
reference_id: "MYGENESET:KEGG_RHEUMATOID_ARTHRITIS"
title: "KEGG_RHEUMATOID_ARTHRITIS"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_RHEUMATOID_ARTHRITIS  KEGG_RHEUMATOID_ARTHRITIS

**MYGENESET:KEGG_RHEUMATOID_ARTHRITIS** — KEGG_RHEUMATOID_ARTHRITIS (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy rheumatoid arthritis pathway gene set (MSigDB C2 curated gene set). This is a disease pathway gene set representing the autoimmune inflammatory joint disease rheumatoid arthritis. Member genes are heavily enriched for pro-inflammatory cytokines and their receptors (TNF, IL1A/B, IL6, IL17), MHC class II antigen presentation machinery (HLA-DRA, HLA-DRB1, HLA-DQA1, HLA-DQB1), osteoclast differentiation and bone-erosion regulators (TNFSF11/RANKL, TNFRSF11A/RANK, TNFRSF11B/OPG), chemokines driving synovial leukocyte recruitment (CXCL1, CCL2), and angiogenesis factors (VEGF/PGF) in the inflamed synovium. The gene set reflects the major mechanistic arms of the KEGG RA pathway: synovial inflammation, adaptive immune activation, pannus-mediated cartilage invasion, and osteoclast-driven bone erosion.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0008383 | rheumatoid arthritis |
| anatomical_structure | UBERON:0002018 | synovial membrane of synovial joint |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0006954 | inflammatory response | biological_process | core_process | high |
| GO:0001816 | cytokine production | biological_process | core_process | high |
| GO:0019882 | antigen processing and presentation | biological_process | supporting_process | high |
| GO:0030316 | osteoclast differentiation | biological_process | supporting_process | high |
| GO:0030595 | leukocyte chemotaxis | biological_process | supporting_process | medium |
| GO:0042613 | MHC class II protein complex | cellular_component | core_component | high |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_RHEUMATOID_ARTHRITIS.yaml` @ `08115aa072e2`).

Upstream identifier: `MSIGDB:KEGG_RHEUMATOID_ARTHRITIS`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
