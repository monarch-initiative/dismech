# Comparison / interpretation

All numbers below are a RE-ANALYSIS of published derived scores (He et al. 2026,
Nat Med; PMID:42778763). This bundle shares data lineage with the paper and is not an
independent replication. Observed results and biological inference are separated below.

## OBSERVED RESULTS

### (1) Astrocyte resilience signal (Supp Data 2 'Fig. 3f')
- Astro: adjusted P = 0.00149687; (AD-strict - AD-resilient) median PAC
  difference = 0.38617
  (strict median 0.430957 vs resilient
  0.0447871).
- Astro rank by adjusted P = 16 of 27 subclasses
  present in the sheet. The strongest separators are neuronal (EN_L3_5_IT_3, IN_PVALB_CHC,
  EN_L2_3_IT, IN_SST); astrocytes are significant but mid-ranked.

### (2) Reactive-astrocyte marker classification (primary: Supp7 AD PAC DEGs, 1,171 genes)
- EMP1 (A2/neuroprotective): log2FC = -0.990 -> DOWN in AD-PAC (inferred
  higher-in-resilient direction). Matches the neuroprotective prediction.
- FKBP5 (A1/neurotoxic): log2FC = +0.959 -> UP in AD-PAC (impaired/strict-like
  direction). Matches the neurotoxic prediction.
- Directional A2-vs-A1 Fisher (A2 enriched in resilient direction): OR =
  1, p = 0.833, BH q =
  0.893. Counts: A2 down/up = 1/
  1; A1 down/up = 1/
  1. NOT significant: only 4 canonical A1/A2 markers survive
  as significant astrocyte DEGs, and the counter-examples HLA-E (A1, down) and CD109
  (A2, up) cancel the EMP1/FKBP5 signal.
- Pooled directional test (Supp7 + Fig.2f PAC-level astrocyte DEGs, 8
  markers): OR = 0.5, p = 0.893,
  BH q = 0.893. Still not significant: most A1 markers are also
  DOWN in AD-PAC (higher in resilient-like), so A2 is not preferentially resilient-directed.
- Overlap enrichment vs 11,145-gene background: see enrichment_results.csv (BH-corrected);
  no marker set is significantly over-represented among astrocyte DEGs after correction.

### (3) Astro-vs-neuronal PAC co-variation (Supp Data 6 'AD progression', n=581)
- All 17/17 excitatory+inhibitory subclasses correlate POSITIVELY with Astro
  PAC (Spearman rho 0.168-0.570; 17/17 BH-q < 0.05).
- Strongest: EN_L3_5_IT_2, EN_L2_3_IT, EN_L3_5_IT_1 (rho ~0.52-0.57).

## BIOLOGICAL INFERENCE (clearly separated from the observations above)
- The two named marker genes behave as the neuroprotective-vs-neurotoxic model predicts
  (EMP1 up in resilient-like, FKBP5 up in impaired-like), but the marker AXIS as a whole
  is NOT statistically supported in these published astrocyte DEGs: the A2-vs-A1 directional
  enrichment is null (OR~1, p~0.83) and rests on only 4 overlapping markers.
- Positive Astro-neuronal PAC co-variation is consistent with a shared donor-level
  disease-burden component rather than an astrocyte-specific resilience axis; because both
  are derived phenotype-association scores, part of this correlation may restate the
  construction of the scores.
- Objective 1 and the EMP1/FKBP5 directions largely RESTATE quantities the paper already
  computed (same derived tables). The only genuinely new derived statistic here is the
  donor-level Astro-vs-neuronal Spearman structure and the (null) directional marker test.

## LIMITATIONS
- Re-analysis of published derived scores; shared lineage with the source paper.
- Donor PAC matrices carry no diagnosis/Braak/resilience labels -> no direct
  resilient-vs-strict astrocyte DE; the resilient direction is inferred via Fig.3f.
- Astrocyte DEG tables are significant-only, limiting background choice; overlap
  background is the union of genes reported across subclass blocks, not the full
  transcriptome.
- Group means / Cohen's d not recoverable from summary statistics.
