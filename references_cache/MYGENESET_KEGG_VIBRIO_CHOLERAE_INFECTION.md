---
reference_id: "MYGENESET:KEGG_VIBRIO_CHOLERAE_INFECTION"
title: "KEGG_VIBRIO_CHOLERAE_INFECTION"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_VIBRIO_CHOLERAE_INFECTION  KEGG_VIBRIO_CHOLERAE_INFECTION

**MYGENESET:KEGG_VIBRIO_CHOLERAE_INFECTION** — KEGG_VIBRIO_CHOLERAE_INFECTION (msigdb, C2:CP:KEGG_LEGACY)

## Description

KEGG legacy Vibrio cholerae infection pathway gene set (MSigDB C2 curated gene set). This is a disease/infection pathway gene set, not a cell-type signature. The member genes encode the host molecular machinery subverted or engaged during cholera: cholera toxin ADP-ribosylates the Gsα subunit (GNAS), locking it in the active GTP-bound state and constitutively stimulating adenylate cyclases (ADCY) to overproduce cyclic AMP. Elevated cAMP activates protein kinase A (PKA; PRKAR* and PRKAC* subunits), which phosphorylates the cystic fibrosis transmembrane conductance regulator (CFTR), driving massive luminal chloride secretion in intestinal epithelial cells. Osmotic water follows, producing the profuse secretory diarrhea of cholera. Additional gene set members include vacuolar-type H+-ATPase (V-ATPase; ATP6V* subunits) involved in endosomal and lysosomal processing of the toxin and cell maintenance, cytoskeletal components (actin), and secondary ion transporters (SLC26A3/DRA, KCNQ1). As a legacy KEGG pathway it captures the established Gs/cAMP/PKA/CFTR axis and omits more recently characterised host innate-immune and tight-junction responses.

## Context

| Type | Term | Label |
|---|---|---|
| disease | MONDO:0015766 | cholera |
| anatomical_structure | UBERON:0002108 | small intestine |
| infection | NCBITaxon:666 | Vibrio cholerae |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:1902476 | chloride transmembrane transport | biological_process | core_process | high |
| GO:0007189 | adenylate cyclase-activating G protein-coupled receptor signaling pathway | biological_process | core_process | high |
| GO:0009636 | response to toxic substance | biological_process | supporting_process | medium |
| GO:0033176 | proton-transporting V-type ATPase complex | cellular_component | core_component | medium |
| GO:0009617 | response to bacterium | biological_process | supporting_process | medium |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (55 genes)

| Symbol | Gene ID |
|---|---|
| ACTB | hgnc:132 |
| ACTG1 | hgnc:144 |
| ADCY3 | hgnc:234 |
| ADCY8 | hgnc:239 |
| ADCY9 | hgnc:240 |
| ARF1 | hgnc:652 |
| ATP6AP1 | hgnc:868 |
| ATP6V0A1 | hgnc:865 |
| ATP6V0A2 | hgnc:18481 |
| ATP6V0A4 | hgnc:866 |
| ATP6V0B | hgnc:861 |
| ATP6V0C | hgnc:855 |
| ATP6V0D1 | hgnc:13724 |
| ATP6V0D2 | hgnc:18266 |
| ATP6V0E1 | hgnc:863 |
| ATP6V0E2 | hgnc:21723 |
| ATP6V1A | hgnc:851 |
| ATP6V1B1 | hgnc:853 |
| ATP6V1B2 | hgnc:854 |
| ATP6V1C1 | hgnc:856 |
| ATP6V1C2 | hgnc:18264 |
| ATP6V1D | hgnc:13527 |
| ATP6V1E1 | hgnc:857 |
| ATP6V1E2 | hgnc:18125 |
| ATP6V1F | hgnc:16832 |
| ATP6V1G1 | hgnc:864 |
| ATP6V1G2 | hgnc:862 |
| ATP6V1G3 | hgnc:18265 |
| ATP6V1H | hgnc:18303 |
| CFTR | hgnc:1884 |
| ERO1A | hgnc:13280 |
| GNAS | hgnc:4392 |
| KCNQ1 | hgnc:6294 |
| KDELR1 | hgnc:6304 |
| KDELR2 | hgnc:6305 |
| KDELR3 | hgnc:6306 |
| MUC2 | hgnc:7512 |
| PDIA4 | hgnc:30167 |
| PLCG1 | hgnc:9065 |
| PLCG2 | hgnc:9066 |
| PRKACA | hgnc:9380 |
| PRKACB | hgnc:9381 |
| PRKACG | hgnc:9382 |
| PRKCA | hgnc:9393 |
| PRKCB | hgnc:9395 |
| PRKCG | hgnc:9402 |
| PRKX | hgnc:9441 |
| SEC61A1 | hgnc:18276 |
| SEC61A2 | hgnc:17702 |
| SEC61B | hgnc:16993 |
| SEC61G | hgnc:18277 |
| SLC12A2 | hgnc:10911 |
| TCIRG1 | hgnc:11647 |
| TJP1 | hgnc:11827 |
| TJP2 | hgnc:11828 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_VIBRIO_CHOLERAE_INFECTION.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_VIBRIO_CHOLERAE_INFECTION) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_VIBRIO_CHOLERAE_INFECTION`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
