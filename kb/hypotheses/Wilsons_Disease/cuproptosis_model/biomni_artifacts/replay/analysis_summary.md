# Analysis summary

Datasets: GSE197406 (GPL570) and GSE125637 (GPL1261)

Group assignment checks:
- GSE197406: Wilson cirrhotic n_case=7 vs normal-control n_ctrl=8; gate enforced (7 vs 8).
- GSE125637: WT=4, untreated Atp7b-null=4, zinc-treated Atp7b-null=4; gate enforced (4/4/4) and zinc arm excluded from contrast.

Transform decisions:
- GSE197406: Distributions within log2-like range; no additional log transform.
- GSE125637: Distributions within log2-like range; no additional log transform.

Probe mapping:
- GSE197406 probes: 54675 rows; platform annotations merged.
- GSE125637 probes: 45101 rows; platform annotations merged.

Gene-level selection:
- For each gene and dataset, selected the probe with the highest global mean expression across all samples before group labels.
- All-probe sensitivity retained via 'n_probes' and 'all_probes' columns in gene_level_results.tsv.

Statistics:
- Case-minus-control log2 mean difference, ordinary fold-change, Welch p-value, BH q-value across the full platform, and pooled-SD Cohen's d computed.

Cuproptosis genes included: FDX1/Fdx1, LIAS/Lias, LIPT1/Lipt1, DLD/Dld, DLAT/Dlat, DLST/Dlst, PDHA1/Pdha1, PDHB/Pdhb, MTF1/Mtf1, GLS/Gls, and CDKN2A/Cdkn2a.

No temporal trajectory inferred from cross-sectional datasets.
## Target genes (pre-specified)

| dataset | gene_symbol | log2_mean_diff | p_value_welch | q_value_bh |
| --- | --- | --- | --- | --- |
| GSE125637 | Cdkn2a | -0.2632 | 0.1726 | 0.3594 |
| GSE125637 | Dlat | -0.1126 | 0.1217 | 0.2996 |
| GSE125637 | Dld | 0.00313 | 0.9786 | 0.988 |
| GSE125637 | Dlst | 0.5607 | 2.449e-05 | 0.00601 |
| GSE125637 | Fdx1 | -0.1855 | 0.04257 | 0.1793 |
| GSE125637 | Gls | -0.1713 | 0.3557 | 0.5406 |
| GSE125637 | Lias | 0.4389 | 0.001114 | 0.03327 |
| GSE125637 | Lipt1 | 0.2742 | 0.03983 | 0.1739 |
| GSE125637 | Mtf1 | -0.0996 | 0.3715 | 0.5544 |
| GSE125637 | Pdha1 | -0.1225 | 0.03827 | 0.1706 |
| GSE125637 | Pdhb | -0.05933 | 0.3668 | 0.5504 |
| GSE197406 | CDKN2A | 0.3181 | 0.04603 | 0.2628 |
| GSE197406 | DLAT | 0.5144 | 0.03081 | 0.2173 |
| GSE197406 | DLD | -0.0549 | 0.6369 | 0.8622 |
| GSE197406 | DLST | 0.4474 | 0.1132 | 0.4101 |
| GSE197406 | FDX1 | -0.6315 | 0.002701 | 0.0569 |
| GSE197406 | GLS | 1.395 | 0.0002916 | 0.01565 |
| GSE197406 | LIAS | -0.1909 | 0.0533 | 0.2831 |
| GSE197406 | LIPT1 | -0.03595 | 0.8291 | 0.9453 |
| GSE197406 | MTF1 | 0.246 | 0.09283 | 0.3731 |
| GSE197406 | PDHA1 | -0.4463 | 0.02726 | 0.2049 |
| GSE197406 | PDHB | -0.2656 | 0.3214 | 0.6594 |

Note: These cross-sectional expression contrasts do not, by themselves, establish cuproptosis, causal mechanism, or temporal disease stages.