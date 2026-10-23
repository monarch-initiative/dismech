# Comparison / interpretation — GSE65914 rosacea GWAS loci

*Observed results are stated first; biological inference is clearly separated.*

## Observed results (from `gene_results.csv`, log2 RMA; positive = higher in lesional)

**Immune loci — up in lesional skin (pooled rosacea vs control):**
| Gene | log2 diff | fold change | Welch p | BH q | Cohen's d |
|------|-----------|-------------|---------|------|-----------|
| HLA-DRA  | +1.454 | 2.74 | ~0     | ~0     | +2.76 |
| TLR2     | +1.908 | 3.75 | ~0     | ~0     | +4.02 |
| IRF1     | +1.413 | 2.66 | ~0     | ~0     | +2.03 |
| HLA-DRB1 | +1.097 | 2.14 | 2e-10  | 1.9e-9 | +1.96 |
| HLA-DQB1 | +1.156 | 2.23 | 5.8e-7 | 2.5e-6 | +1.74 |
| TLR1     | +1.003 | 2.00 | 1.8e-9 | 1.3e-8 | +1.61 |
| HLA-DQA1 | +1.249 | 2.38 | 2.2e-4 | 4.5e-4 | +1.04 |
| BTNL2    | +0.187 | 1.14 | 7.9e-3 | 1.2e-2 | +0.91 |

- **IL13**: no change (pooled log2 diff −0.033, p = 0.50, q = 0.54).
- **IRF4**: down only in ETR (log2 diff −0.139, q = 4.3e-3); pooled n.s. (p = 0.073).

**Pigmentation loci — down in lesional skin (pooled rosacea vs control):**
| Gene | log2 diff | fold change | Welch p | BH q | Cohen's d |
|------|-----------|-------------|---------|------|-----------|
| HERC2   | −0.205 | 0.87 | 8.2e-6 | 2.7e-5 | −1.61 |
| OCA2    | −0.563 | 0.68 | 4.9e-3 | 7.8e-3 | −1.00 |
| SLC45A2 | −0.108 | 0.93 | 7.5e-2 | 9.1e-2 | −0.60 |

All three subtypes (ETR, PPR, PhR) show the same directions; magnitudes are broadly
comparable, with the strongest immune upregulation often in PPR (e.g. HLA-DRA, IRF1, TLR1).

## TLR1–TLR2 correlation (from `tlr_correlation.csv`)
- **All samples (n = 58):** Spearman ρ = **0.690**, p = 2.1e-9.
- Within rosacea (n = 38): ρ = 0.350 (p = 0.031); within control (n = 20): ρ = 0.522 (p = 0.018).
- **Rosacea vs control difference:** Fisher r-to-z z = −0.72, **p = 0.47 → not significantly different**.

## Which loci are immune vs pigmentation
- **Immune:** HLA-DRA, BTNL2, HLA-DRB1, HLA-DQB1, HLA-DQA1, IL13, IRF1, TLR1, TLR2, IRF4.
- **Pigmentation:** HERC2, OCA2, SLC45A2.

## Biological inference (separate from the observed numbers above)
- The data are **consistent** with the hypothesis that rosacea GWAS immune-locus genes act
  through **altered lesional expression**: HLA class II (DRA/DRB1/DQA1/DQB1), IRF1, BTNL2 and
  both TLR1 and TLR2 are significantly upregulated in lesional skin across subtypes, with large
  effect sizes — compatible with antigen-presentation / Th1–Th17 activation.
- The **TLR1–TLR2 heterodimer axis** is supported at the co-expression level: TLR1 and TLR2 are
  positively correlated overall and both are strongly induced in lesions. However, the strength of
  the TLR1–TLR2 correlation is **not** statistically different between rosacea and control
  (p = 0.47); the axis is co-induced rather than showing rewired coupling.
- **Pigmentation** GWAS loci (HERC2, OCA2, SLC45A2) are, if anything, **modestly down** in lesional
  skin — the opposite direction from the immune loci — so an eQTL-in-lesion mechanism is not
  supported for them by this transcriptomic contrast (their GWAS signal more plausibly reflects
  pigmentation/UV-sensitivity confounding rather than lesional expression change).
- These are cross-sectional microarray associations, not causal or eQTL evidence; genotypes are
  not available in this dataset.
