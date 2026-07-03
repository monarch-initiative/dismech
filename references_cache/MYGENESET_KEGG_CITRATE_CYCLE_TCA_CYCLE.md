---
reference_id: "MYGENESET:KEGG_CITRATE_CYCLE_TCA_CYCLE"
title: "KEGG_CITRATE_CYCLE_TCA_CYCLE"
database: "mygeneset.info"
content_type: "structured_record"
---

# MYGENESET:KEGG_CITRATE_CYCLE_TCA_CYCLE  KEGG_CITRATE_CYCLE_TCA_CYCLE

**MYGENESET:KEGG_CITRATE_CYCLE_TCA_CYCLE** — KEGG_CITRATE_CYCLE_TCA_CYCLE (msigdb, C2:CP:KEGG_LEGACY)

## Description

MSigDB C2 KEGG legacy gene set representing the enzymes of the tricarboxylic acid (TCA) cycle, also known as the citric acid cycle or Krebs cycle. This is a pure metabolic-pathway signature, not a cell-type or disease signature. Member genes encode the eight enzymatic complexes that catalyse the sequential oxidation of acetyl-CoA in the mitochondrial matrix: citrate synthase (CS), aconitase (ACO2), isocitrate dehydrogenase (IDH2/IDH3A/IDH3B/IDH3G), 2-oxoglutarate dehydrogenase complex (OGDH/DLST/DLD), succinyl-CoA synthetase (SUCLG1/SUCLG2/SUCLA2), succinate dehydrogenase (SDHA/SDHB/SDHC/SDHD), fumarase (FH), and malate dehydrogenase (MDH2). The cycle oxidises acetyl-CoA to CO2, reduces NAD+ and FAD to NADH and FADH2, and generates GTP, providing reducing equivalents for the electron transport chain and biosynthetic precursors for amino acids, nucleotides, and porphyrins.

## Context

| Type | Term | Label |
|---|---|---|
| experimental_condition | GO:0006099 | tricarboxylic acid cycle |

## Curated GO interpretation

| GO ID | Label | Aspect | Role | Confidence |
|---|---|---|---|---|
| GO:0006099 | tricarboxylic acid cycle | biological_process | core_process | high |
| GO:0005739 | mitochondrion | cellular_component | core_component | high |
| GO:0005759 | mitochondrial matrix | cellular_component | core_component | high |
| GO:0006091 | generation of precursor metabolites and energy | biological_process | supporting_process | high |
| GO:0009060 | aerobic respiration | biological_process | supporting_process | high |
| GO:0016491 | oxidoreductase activity | molecular_function | supporting_process | high |
| GO:0006412 | translation | biological_process | nonspecific | high |

## Members (39 genes)

| Symbol | Gene ID |
|---|---|
| ACLY | hgnc:115 |
| ACO1 | hgnc:117 |
| ACO2 | hgnc:118 |
| CFH | hgnc:4883 |
| CS | hgnc:2422 |
| DLAT | hgnc:2896 |
| DLD | hgnc:2898 |
| DLST | hgnc:2911 |
| FAM3A | hgnc:13749 |
| FH | hgnc:3700 |
| IDH1 | hgnc:5382 |
| IDH2 | hgnc:5383 |
| IDH3A | hgnc:5384 |
| IDH3B | hgnc:5385 |
| IDH3G | hgnc:5386 |
| LDLR | hgnc:6547 |
| MDH1 | hgnc:6970 |
| MDH2 | hgnc:6971 |
| OGDH | hgnc:8124 |
| OGDHL | hgnc:25590 |
| PC | hgnc:8636 |
| PCK1 | hgnc:8724 |
| PCK2 | hgnc:8725 |
| PDHA1 | hgnc:8806 |
| PDHA2 | hgnc:8807 |
| PDHB | hgnc:8808 |
| PODXL | hgnc:9171 |
| PROC | hgnc:9451 |
| SDHA | hgnc:10680 |
| SDHB | hgnc:10681 |
| SDHC | hgnc:10682 |
| SDHCP5 | - |
| SDHCP5 | hgnc:57039 |
| SDHD | hgnc:10683 |
| SUCLA2 | hgnc:11448 |
| SUCLG1 | hgnc:11449 |
| SUCLG2 | hgnc:11450 |
| SUCLG2P2 | - |
| SUCLG2P2 | hgnc:43997 |

## Source

Curated GO interpretation from [`monarch-initiative/genesets`](https://github.com/monarch-initiative/genesets) (`curation/genesets/KEGG_CITRATE_CYCLE_TCA_CYCLE.yaml` @ `08115aa072e2`).

Gene membership from [mygeneset.info](https://mygeneset.info/geneset/KEGG_CITRATE_CYCLE_TCA_CYCLE) (source: msigdb).

Upstream identifier: `MSIGDB:KEGG_CITRATE_CYCLE_TCA_CYCLE`.

Licence: see monarch-initiative/genesets and mygeneset.info source terms.
