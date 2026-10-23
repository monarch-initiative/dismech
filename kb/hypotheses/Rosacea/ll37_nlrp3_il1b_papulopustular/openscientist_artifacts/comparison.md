# Comparison — observed results vs biological inference

Hypothesis: **LL-37 drives papulopustular lesions through NLRP3 inflammasome
activation and IL-1β maturation.** Dataset: GSE155141 (n = 5 paired subjects).
All values are from `gene_results.csv` (paired t-test on log2(CPM+1), BH-FDR over
the 8 genes within each contrast). Fold change > 1 = higher in the test group.

## Observed results

### Contrast 1 — lesional vs paired non-lesional (untreated)
| Gene | FC (les/non) | log2 diff | Cohen's d | p | q(BH) |
|------|-------------|-----------|-----------|------|-------|
| NLRP3  | 1.05 | +0.065 | +0.20 | 0.685 | 0.882 |
| CASP1  | 0.69 | −0.533 | −0.58 | 0.263 | 0.846 |
| PYCARD | 0.99 | −0.021 | −0.03 | 0.955 | 0.955 |
| IL1B   | 1.48 | +0.564 | +0.54 | 0.290 | 0.846 |
| IL18   | 1.12 | +0.165 | +0.14 | 0.772 | 0.882 |
| IL1RN  | 0.88 | −0.180 | −0.16 | 0.738 | 0.882 |
| CAMP   | 0.95 | −0.073 | −0.51 | 0.317 | 0.846 |
| KLK5   | 0.84 | −0.244 | −0.17 | 0.726 | 0.882 |

No gene reaches significance (all q ≈ 0.85–0.96). IL1B shows the largest positive
lesional effect (FC 1.48, d 0.54) but is not significant at n = 5; CASP1 and CAMP
trend downward.

### Contrast 2 — non-lesional IL-1β-treated vs untreated
| Gene | FC (IL1/unt) | log2 diff | Cohen's d | p | q(BH) |
|------|-------------|-----------|-----------|------|-------|
| **NLRP3** | 1.19 | +0.245 | +1.57 | **0.025** | 0.196 |
| CASP1  | 1.12 | +0.163 | +0.32 | 0.508 | 0.812 |
| PYCARD | 0.98 | −0.032 | −0.04 | 0.936 | 0.936 |
| IL1B   | 2.01 | +1.010 | +0.80 | 0.147 | 0.519 |
| IL18   | 0.95 | −0.079 | −0.12 | 0.805 | 0.920 |
| IL1RN  | 1.59 | +0.671 | +0.60 | 0.250 | 0.519 |
| CAMP   | 1.13 | +0.170 | +0.59 | 0.260 | 0.519 |
| KLK5   | 0.91 | −0.129 | −0.25 | 0.611 | 0.814 |

NLRP3 is significantly up-regulated by IL-1β (raw p = 0.025, large paired
d = 1.57; q = 0.196 after BH over 8 genes). IL1B (FC 2.01, d 0.80) and IL1RN
(FC 1.59) show sizeable positive effects that do not reach significance at n = 5.
IL18 and PYCARD are essentially unchanged.

## Biological inference (separated from the observed numbers)
- The clearest observed signal is **IL-1β priming of NLRP3 transcription** in
  non-lesional explants, consistent with a feed-forward loop in which IL-1β
  up-regulates the sensor (NLRP3) and its own transcript (IL1B trend) plus the
  antagonist IL1RN (a counter-regulatory response). This is *consistent with* the
  inflammasome arm of the hypothesis at the transcript level.
- The **lesional-vs-non-lesional** comparison does **not** confirm transcriptional
  up-regulation of the NLRP3 module in lesions: NLRP3/PYCARD are flat and CASP1
  trends down. IL1B is the only inflammasome-output gene trending up in lesions,
  and CAMP/KLK5 (the cathelicidin/LL-37 processing axis) are not elevated at the
  mRNA level.
- **Caveat:** inflammasome activation is chiefly post-translational (CASP1
  cleavage, pro-IL-1β maturation, LL-37 peptide generation from CAMP by KLK5),
  which mRNA abundance cannot capture. Absence of transcriptional change does not
  refute protein-level inflammasome activity. These are targeted replication
  metrics at n = 5, not a powered genome-wide DE analysis.

## Bottom line
Observed: IL-1β significantly induces NLRP3 mRNA (only gene passing raw p < 0.05),
with supportive but non-significant IL1B/IL1RN increases; no target gene is
significantly changed between lesional and non-lesional skin after FDR. The data
partially support the inflammasome-priming component of the hypothesis and neither
confirm nor refute the LL-37 (CAMP/KLK5) transcriptional axis.
