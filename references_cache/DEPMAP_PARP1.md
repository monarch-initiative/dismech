---
reference_id: "DEPMAP:PARP1"
title: "PARP1 selective dependency (DepMap)"
database: "DepMap"
content_type: "structured_record"
---

# DEPMAP:PARP1  PARP1 selective dependency

**DEPMAP:PARP1** - DepMap CRISPR selective dependency of PARP1.

## Dependency

- Gene A: PARP1 (hgnc:270)
- Relationship: SELECTIVE_DEPENDENCY

## Selective dependency statistics

Per-context DepMap CRISPR gene-effect statistics. A more negative gene-effect (Chronos) score means stronger dependency; a differential-dependency metric compares the context-positive and context-negative model groups. Values are from pooled cancer cell-line screens (IN_VITRO), are not corrected for the number of genes/contexts tested, and require orthogonal validation before clinical inference.

| Context | Metric | Value | Effect size | N models |
|---|---|---|---|---|
| BRCA1/BRCA2 loss-of-function (mutant) | MEAN_GENE_EFFECT | -0.2503 | - | 55 |
| BRCA1/BRCA2 loss-of-function vs wild-type | DIFFERENTIAL_DEPENDENCY_WELCH_T | -2.9740 | -0.4958 | 55 |
| BRCA1/BRCA2 loss-of-function wild-type | MEAN_GENE_EFFECT | -0.1801 | - | 1123 |

## Source

Cancer Dependency Map (DepMap), Broad Institute, release **DepMap Public 24Q4** (observations from DepMap Public 24Q4). Genome-scale CRISPR knockout dependency screens across cancer cell lines; selective dependencies and gene-pair synthetic lethality are derived by differential dependency analysis. License: CC BY 4.0.

DOI: 10.25452/figshare.plus.27993248.v1

[DepMap portal](https://depmap.org/portal/)
