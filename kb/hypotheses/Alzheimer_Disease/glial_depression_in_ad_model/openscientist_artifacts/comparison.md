# Comparison / interpretation

Separation of OBSERVED results from biological inference. All numbers are a re-analysis
of He et al. 2026 published derived scores (shared lineage; not independent replication).

## Observed results
### (1) Depression vs AD-progression PAC correlation (208 common donors, Spearman, BH)
- Astro: rho = -0.015, p = 0.825, q = 0.825 (no significant correlation).
- Oligo: rho = -0.182, p = 0.0085, q = 0.0099 (weak, though nominally significant).
- Neuronal subclasses show strong NEGATIVE correlations (e.g. IN_VIP rho = -0.80,
  IN_SST -0.77, IN_ADARB2 -0.78, EN_L5_ET -0.75; all q < 1e-40).
- SHAP importance for DepressionMood: Astro rank 1 (0.099), Oligo rank 2 (0.050),
  OPC rank 3 - glia dominate the random-forest importance.

### (2) Gene-set enrichment in Supp Data 3 astrocyte gene sets (Fisher, BH)
- AD-Depression Astro_WIF1 up-cluster vs UPR/ER-stress: 3/15 overlap
  (CALR, DNAJB9, HSPA5); genomic-background OR = 17.5, p = 0.00115, q = 0.0092
  (significant); DEG-restricted background OR = 2.07, p = 0.22, q = 0.57 (not sig).
- AD-Depression Astro_WIF1 up-cluster vs inflammatory: 1/11 (NFKBIA), not significant.
- Depression-PAC astrocyte DEGs vs UPR/ER-stress: 0/15 overlap (q = 1.0).
- Depression-PAC astrocyte DEGs vs inflammatory: 1/11 (CHI3L1), not significant.

### (3) Overlap depression-astro DEGs (568) vs AD-astro DEGs (1171)
- intersection = 265, union = 1474, Jaccard = 0.180.
- ER-stress genes: NONE in depression-PAC astrocyte DEGs; CALR and HSPA5 present in
  AD-PAC astrocyte DEGs. ER-stress genes are therefore NOT specific to the depression set.

## Interpretation (inference)
- The astrocyte depression PAC signal is statistically INDEPENDENT of the AD-progression
  PAC signal (rho ~ 0), and the oligodendrocyte signal is only weakly related, whereas
  neuronal subclasses track AD progression strongly. Under the constraint that donor
  labels are unavailable, this cross-phenotype independence is consistent with the
  hypothesis that the depression-within-AD GLIAL signal is distinct from the general AD
  signal. Glia (Astro, Oligo) being the top SHAP predictors of DepressionMood reinforces
  a glial locus for the depression phenotype.
- ER-stress/UPR enrichment is detectable in the AD-Depression Astro_WIF1 cluster
  (HSPA5, CALR, DNAJB9) but NOT in the broader depression-PAC astrocyte DEG list, and the
  same ER-stress genes appear in the general AD astrocyte DEGs. Thus ER-stress is an
  AD-context astrocyte feature rather than a depression-specific one; the "ER-stress model
  of depression in AD" is supported only at the level of the combined AD-Depression
  Astro_WIF1 cluster, and depends on the choice of gene universe (significant against a
  genomic background, not against a DEG-restricted background).
- Several prespecified target genes (ATF4, DDIT3, XBP1, MANF, SERPINA3, IL1B, IL6, TNF)
  are absent from all four loaded astrocyte gene lists.

## What merely restates the paper
The PAC scores, SHAP values, and DEG tables are the paper's own outputs; the SHAP ranking
(Astro/Oligo dominance) and the presence of the Astro_WIF1 cluster ER-stress genes simply
re-expose published quantities. The cross-phenotype Spearman correlation, the BH-corrected
enrichment tests with an explicit universe, and the Jaccard overlap are new derived
statistics computed here, but they operate on the same derived data and cannot constitute
independent validation.
