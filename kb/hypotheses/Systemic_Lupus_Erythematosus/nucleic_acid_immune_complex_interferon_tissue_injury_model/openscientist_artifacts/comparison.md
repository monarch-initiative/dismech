# Comparison / interpretation — GSE65391 interferon & plasmablast replication

Hypothesis: *Nucleic-Acid Immune Complex, Interferon, and Tissue-Injury Model*
(`nucleic_acid_immune_complex_interferon_tissue_injury_model`). Prespecified test:
does the blood type I interferon signature track disease **activity** and
**nephritis**, or only disease **presence**?

All numbers below are read directly from the locked primary outputs
(`gene_results.csv`, `correlations.csv`) produced by `analysis.py`. This is a
single-provider computational replication; no external provider results informed
any method, sample, feature, probe, model, threshold, or parameter choice.

## Observed results

### Contrast 1 — SLE (n=158) vs Healthy (n=46), first visit
- Every interferon gene is strongly elevated in SLE (BH q ≪ 1e-9):
  IFI27 (log2 diff +5.58, d=2.44), IFI44L (+3.78, d=2.37), RSAD2 (+3.71, d=2.22),
  IFIT1 (+2.85, d=2.21), ISG15 (+2.77, d=1.89), SIGLEC1 (+0.59, d=0.76).
- Composite **IFN6_SCORE**: +2.41 z-units, d=2.18, q≈1.9e-27.
- Plasmablast genes: MZB1 modestly up (+0.51, d=0.35, q=4.8e-3);
  JCHAIN and TNFRSF17 not significant.

### Contrast 2 — within SLE, SLEDAI ≥6 (n=94) vs <6 (n=64), first visit
- All interferon genes higher with active disease (BH q ≤ 3e-4):
  ISG15, RSAD2, SIGLEC1, IFI44L, IFIT1, IFI27 (d 0.59–0.81).
- **IFN6_SCORE**: +0.95 z-units, d=0.89, q≈9.9e-6.
- Plasmablast genes also elevated: MZB1 (d=0.57, q=4.9e-4),
  TNFRSF17 (d=0.39, q=0.017), JCHAIN (d=0.34, q=0.037).

### Contrast 3 — within SLE, biopsy-proven nephritis (n=33) vs none (n=125), first visit
- **No gene reaches significance** (all BH q ≥ 0.57).
- IFN6_SCORE difference +0.25 z-units, d=0.22, q=0.57.
- Plasmablast genes essentially flat (|d| ≤ 0.06).

### Correlations — within SLE first visit (Spearman)
- IFN6_SCORE vs SLEDAI: ρ=+0.44 (q≈1.1e-7); vs C3: ρ=−0.34; vs C4: ρ=−0.35
  (both q<1e-4); vs neutrophil count: ρ=−0.12 (ns); vs anti-dsDNA: ρ=+0.26,
  n=90 (q=0.018).
- Plasmablast genes track the same axis: MZB1 vs C4 ρ=−0.47 (q≈3.4e-8),
  vs SLEDAI ρ=+0.37; TNFRSF17 and JCHAIN show concordant patterns.
- Anti-dsDNA correlations rest on only n=90 numeric values because most `ds_dna`
  entries are titers/qualitative strings treated as missing (see methods.md).

## Biological inference (separated from the observations above)
The observed pattern is consistent with the interferon-centric model: the type I
IFN signature is a near-universal marker of SLE **presence** (huge effect vs
healthy) and additionally scales with **global disease activity** (SLEDAI, low
complement), i.e. it is an activity biomarker, not merely a disease switch.
However, at a cross-sectional first visit it does **not** discriminate
biopsy-proven lupus **nephritis** from non-nephritis SLE, suggesting renal
tissue injury is not captured by the circulating blood IFN score alone. The
plasmablast signature (MZB1, TNFRSF17, JCHAIN) tracks activity and complement
consumption in parallel with IFN, but likewise does not mark nephritis
cross-sectionally. These are inferences; the replication only establishes the
statistical associations reported above.

## Limitations
- Cross-sectional first-visit design; no longitudinal/within-subject modelling.
- Nephritis contrast is modestly powered (33 vs 125) and depends on the
  documented parsing of `nephritis_class` (NoLN + "Data Not Available" = no
  nephritis).
- `ds_dna` is largely non-numeric (titers), sharply reducing its effective n.
- Uses authors' processed log2 intensities as distributed in the series matrix;
  no re-normalization from raw IDAT files.
