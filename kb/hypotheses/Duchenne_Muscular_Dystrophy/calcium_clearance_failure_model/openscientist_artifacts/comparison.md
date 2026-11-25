# Comparison: DMD versus healthy human myoblasts (GSE299627)

One comparison, computed once: DMD (AB1071; GSM9042258, GSM9042259, GSM9042260) relative to
healthy (AB1190; GSM9042255, GSM9042256, GSM9042257). PyDESeq2 0.6.0, median-of-ratios
normalization, negative-binomial Wald test, Benjamini-Hochberg adjustment over 17,977 tested genes.
Negative log2 fold change means lower in the DMD line.

## Genome-wide result

6,265 genes reach BH q < 0.05: **3,143 up in DMD** and **3,122 down in DMD**. That is 35 % of all
tested genes, which is what two different immortalized cell lines look like when compared to each
other, and it is the context in which every gene-level number below should be read.

## Positive control: DMD

| gene | mean norm. healthy | mean norm. DMD | log2FC | p | BH q |
|---|---|---|---|---|---|
| DMD | 218.43 | 161.67 | **-0.431** | 0.0201 | 0.0563 |

Dystrophin transcript is lower in the dystrophic line, by about 26 % (fold change 0.74), but the
change does not reach BH q < 0.05. **Stated prominently as required:** the positive control is weak.
A 0.43 log2 reduction in whole-gene counts is not the near-absence of transcript one might expect,
so the gene-level count does not by itself confirm the group labels. This is consistent with a
dystrophic line carrying an out-of-frame deletion or point mutation that removes protein without
abolishing the transcript, but gene-level counts cannot distinguish that from a mislabelled
comparison. Exon-level or transcript-level evidence would be needed, and this analysis did not
generate it.

## Replication check against the published values

| gene | published log2FC | published p | observed log2FC | observed p | observed BH q | agrees? |
|---|---|---|---|---|---|---|
| FBN1 | -1.2 | p < 0.0001 | **-1.200** | 1.88e-13 | 3.36e-12 | yes, on sign, magnitude and significance |
| FBN2 | -0.9 | p < 0.0001 | **-0.358** | 0.0465 | 0.111 | no |

FBN1 reproduces to three significant figures. FBN2 does not: the sign matches, but the magnitude is
2.5-fold smaller than reported and the gene is not significant after multiple-testing correction
(and only marginally significant before it). This discrepancy is reported as found. The pipeline was
not adjusted to recover -0.9, and no reconciling explanation is offered.

## Target genes

Full numbers, including unadjusted p and BH q for every gene, are in `target_gene_results.csv`.
Summary by group:

**Fibrillins.** FBN1 down (-1.200, q = 3.4e-12). FBN2 down but not significant (-0.358, q = 0.111).
FBN3 was removed by the low-expression filter (mean raw counts 2.3 healthy, 1.0 DMD) and is reported
as filtered, not omitted.

**LTBPs.** LTBP3 down (-1.317, q = 3.9e-34, the strongest target result), LTBP2 down (-0.739,
q = 2.2e-06), LTBP4 down (-0.702, q = 4.7e-04). LTBP1 moves the other way, **up** (+0.528,
q = 5.9e-04). So the fibrillin-binding partners are not coordinately lower: three of four fall,
one rises.

**ZNF277.** Up (+0.406, q = 0.038), a small increase, opposite in direction to the ECM genes it was
proposed to regulate downward.

**SERCA paralogs.** ATP2A1 down (-0.817, q = 5.9e-05) and ATP2A3 down (-1.429, q = 5.5e-04), both
from low absolute levels (normalized means 221 and 54 in healthy myoblasts). ATP2A2, which carries
essentially all the SERCA signal in these undifferentiated myoblasts (normalized mean ~15,800), is
**unchanged** (-0.151, q = 0.360). The dominant SERCA transcript in this cell type does not differ
between the lines.

**SR calcium handling and release.** RYR1 (-7.585, q = 7.6e-12) and CASQ2 (-5.301, q = 2.4e-03) are
near-absent in the DMD line, but both start from very low counts in myoblasts (RYR1 normalized mean
137, CASQ2 15), so these are changes between "barely expressed" and "not detected" in
undifferentiated cells. ITPR1 is down (-0.965, q = 1.4e-06) from a moderate level. SLN, PLN and
CASQ1 were removed by the low-expression filter (mean raw counts < 8 in both groups), as expected in
undifferentiated myoblasts. Calmodulins split: CALM1 (+0.284, q = 0.014) and CALM2 (+0.368,
q = 0.0057) up, CALM3 (-0.227, q = 0.071) not significant.

**Sarcolemmal calcium entry, the competing model.** ORAI1 (+0.161, q = 0.371), STIM1 (-0.088,
q = 0.605) and PIEZO1 (-0.257, q = 0.168) show no significant change. TRPC1 is up (+0.629,
q = 9.96e-04) and TRPC3 is down (-2.205, q = 3.3e-06) from a low level (normalized mean 48 healthy).
TRPC6 was filtered out. The store-operated entry genes central to the competing entry-based model do
not move in this comparison; two TRPC channels move in opposite directions.

## What was observed, separated from what it would mean

Observed, and nothing beyond this is established by these data:

1. In these two cell lines, FBN1, LTBP2, LTBP3, LTBP4, ATP2A1, ATP2A3, ATP2A2 (no change), ITPR1,
   RYR1, CASQ2 and TRPC3 transcripts are lower in AB1071 than in AB1190; LTBP1, ZNF277, CALM1,
   CALM2 and TRPC1 are higher; FBN2, ATP2A2, CALM3, ORAI1, STIM1 and PIEZO1 do not reach q < 0.05.
2. FBN1 matches the published log2 fold change of -1.2; FBN2 does not match the published -0.9.
3. The dystrophin transcript is 26 % lower in the dystrophic line and does not reach significance.
4. 6,265 of 17,977 genes are differentially expressed at q < 0.05, nearly symmetric in direction.

Inference, which this dataset cannot test:

- Whether any of these transcript differences change SERCA pump activity, SR calcium load, cytosolic
  calcium transients, or calcium clearance kinetics. Transcript abundance is not pump activity and
  not calcium flux. Functional calcium measurements in the same lines would be required, and none
  exist here.
- Whether the pattern reflects dystrophin deficiency at all. See the design limitation below.

## Design limitation (mandatory, applies to every result above)

Each group is a single immortalized cell line, so the three samples per group are replicates of one
donor background rather than independent donors. Every differential-expression result from this
design is confounded with cell-line identity, and the analysis cannot attribute any difference to
dystrophin deficiency as opposed to donor genotype, immortalization history, or passage. This is a
limitation of the design, not a caveat on individual genes. The comparison is not n = 6 independent
samples. With 35 % of the transcriptome differential, the base rate for any prespecified gene to
differ "significantly" in this comparison is high, so individual significant target genes carry
little evidential weight about DMD biology.

## Verdict on the hypothesis as stated

The dataset does not support a coordinated downregulation of fibrillin-related ECM genes together
with SR calcium-handling genes as a specific signature. FBN1 falls and LTBP2/3/4 fall, but LTBP1
rises, FBN2 does not replicate, and the dominant SERCA transcript ATP2A2 is unchanged. The competing
sarcolemmal-entry genes are largely flat rather than moving in the same direction. Whatever the
direction of individual genes, no causal or mechanistic claim about calcium clearance can be drawn
from this design.
