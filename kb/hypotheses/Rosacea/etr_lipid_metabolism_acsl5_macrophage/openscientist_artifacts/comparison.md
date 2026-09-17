# Comparison — observed results vs biological inference

Contrast: **ETR (n=14) vs healthy control (n=20)** in GSE65914 (GPL570), gene-level
log2 expression, Welch's t-test, BH-FDR over 7 genes. Fold change = 2^(log2 mean diff),
oriented ETR/control.

## Observed results (from `gene_results.csv`)

| Gene   | Class            | log2 diff | Fold change | t      | p        | q (BH)   | Cohen's d |
|--------|------------------|-----------|-------------|--------|----------|----------|-----------|
| ACSL5  | lipid metabolism | +2.490    | 5.62        | 12.76  | 4.73e-14 | 3.31e-13 | 4.23      |
| ACADVL | lipid metabolism | +1.018    | 2.03        | 10.37  | 1.73e-09 | 4.04e-09 | 3.92      |
| PPARG  | PPAR/fatty-acid  | +2.164    | 4.48        | 9.08   | 2.39e-10 | 8.37e-10 | 2.93      |
| CPT1A  | PPAR/fatty-acid  | -0.003    | 1.00        | -0.04  | 9.66e-01 | 9.66e-01 | -0.01     |
| CD68   | macrophage       | +0.679    | 1.60        | 4.70   | 1.53e-04 | 2.14e-04 | 1.79      |
| CD163  | macrophage       | +0.819    | 1.76        | 4.38   | 2.86e-04 | 3.33e-04 | 1.65      |
| CD86   | macrophage       | +0.485    | 1.40        | 5.63   | 2.88e-05 | 5.05e-05 | 2.20      |

Within-ETR Spearman correlation of ACSL5 with macrophage markers (n=14, from
`spearman_acsl5_macrophage.csv`):

| Pair            | Spearman rho | p      | q (BH) |
|-----------------|--------------|--------|--------|
| ACSL5 vs CD68   | 0.297        | 0.303  | 0.454  |
| ACSL5 vs CD163  | 0.037        | 0.899  | 0.899  |
| ACSL5 vs CD86   | 0.310        | 0.281  | 0.454  |

## What was observed (results only)
- **6 of 7 genes are significantly higher in ETR than control** after BH-FDR
  (q < 0.001 for all six), with large-to-very-large effect sizes (Cohen's d 1.65–4.23).
- The lipid-metabolism hub gene **ACSL5** shows the strongest signal of any tested
  gene (fold change 5.6, d = 4.23). **ACADVL** (2.0×) and the PPAR regulator
  **PPARG** (4.5×) are also strongly up-regulated.
- **CPT1A is essentially unchanged** (fold change 1.00, q = 0.97).
- All three **macrophage markers (CD68, CD163, CD86) are up-regulated** in ETR,
  consistent with increased macrophage abundance.
- **Within ETR**, ACSL5 does **not** correlate significantly with any macrophage
  marker (all q > 0.45; weak positive rho for CD68/CD86, near-zero for CD163).

## Biological inference (interpretation, not measurement)
- The coordinated up-regulation of ACSL5, ACADVL and PPARG in ETR is consistent
  with **lipid-metabolic reprogramming** in early (erythematotelangiectatic)
  rosacea, alongside a concurrent **increase in macrophage markers** — matching
  the hypothesis's two pillars at the group-comparison level.
- The lack of a significant CPT1A change suggests that if fatty-acid handling is
  altered, it is **not driven by classical mitochondrial β-oxidation import (CPT1A)**
  in this cohort; ACADVL (very-long-chain acyl-CoA dehydrogenase) and ACSL5
  (acyl-CoA synthesis) dominate the observed lipid signal.
- The **non-significant within-ETR ACSL5↔macrophage correlations do not support a
  direct co-regulatory / causal link** between ACSL5 level and macrophage-marker
  level among ETR samples. Both are elevated versus control, but their variation
  within ETR is not coupled. This is a genuinely negative sub-result; note it is
  based on only 14 arrays (7 subjects × 2), so it is **underpowered** for
  correlation and cannot exclude a modest association. It also cannot establish
  causal direction ("ACSL5 drives M1 infiltration").

## Bottom line
The prespecified contrast **supports lipid-metabolic reprogramming centred on
ACSL5 (plus ACADVL and PPARG) co-occurring with elevated macrophage markers in
ETR**, but the **causal/co-regulatory coupling of ACSL5 to macrophage markers
within ETR is not demonstrated** by the within-group Spearman analysis.
