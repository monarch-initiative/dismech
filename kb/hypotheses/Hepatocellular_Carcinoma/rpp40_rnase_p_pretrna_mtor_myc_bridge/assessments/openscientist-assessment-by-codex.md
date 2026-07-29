# OpenScientist assessment: RPP40 RNase-P/pre-tRNA–mTOR/MYC bridge

## Overall assessment

The report reaches a defensible bottom line: the distinctive
RNase-P/pre-tRNA-to-mTOR/MYC bridge remains **weakly supported and unresolved**.
The HCC studies establish useful flanking observations, but no study establishes
the proposed temporal middle:

```text
RPP40 loss
  → RNase-P-specific pre-tRNA defect
  → reduced translational capacity
  → mTOR/MYC decline
  → reduced HCC proliferation
```

The report is nevertheless not reliable as a literature adjudication without
substantial correction. It missed two primary papers that materially change the
analysis, made a false checked-absence claim, conflated cleavage of a pre-tRNA
leader with degradation of that leader after excision, and overinterpreted
pan-cancer essentiality and canonical directionality.

| Dimension | Assessment |
| --- | --- |
| Overall hypothesis verdict | **Retain: weakly supported / unresolved** |
| Causal decomposition | Strong |
| Primary-literature completeness | Poor; two decisive papers omitted |
| Treatment of competing models | Useful but sometimes overstated |
| Discriminating experiments | Useful after correcting branch-specific handles |
| Ready for blind promotion into disease YAML | **No** |

## What the report gets right

### The central bridge is still untested in HCC

[PMID:42424930](https://pubmed.ncbi.nlm.nih.gov/42424930/) supports RPP40
upregulation, adverse outcome association, perturbation-dependent malignant
phenotypes, and an mTOR/MYC association in HCC. It does not establish
RNase-P-specific pre-tRNA maturation as the intervening mechanism or show that
the RNA-processing defect precedes signaling decline.

A separate HCC paper,
[PMID:40517827](https://pubmed.ncbi.nlm.nih.gov/40517827/), supports an
rRNA/ribosomal-gene route. That strengthens the competing explanation; it does
not settle whether RNase MRP catalysis, broader ribosome biogenesis, RNase P, or
some combination is responsible.

Keeping the hypothesis `EMERGING` and leaving it unwired as a causal pathograph
edge is therefore appropriate.

### Shared-subunit confounding is real

RPP40 belongs to RNase P and RNase MRP. The report is right that an RPP40
perturbation is not an RNase-P-specific experiment. The strongest evidence is
not merely old co-sedimentation data, however. A rapid-degron study,
[PMID:40533478](https://pubmed.ncbi.nlm.nih.gov/40533478/), directly showed that
RPP40 degradation in human cells:

- reduced the catalytic RNAs of RNase P and RNase MRP;
- accumulated 5-prime-leader-containing pre-tRNAs and pre-rRNA intermediates;
- caused a much earlier, stronger proliferative arrest than
  RNase-P-specific RPP21 degradation; and
- attributed the early translational/proliferative effect primarily to disrupted
  rRNA biogenesis, while not excluding a smaller RNase P contribution.

This is highly relevant non-HCC evidence. It strengthens the RNase MRP
competitor while also showing that RPP40 loss really can produce the pre-tRNA
defect predicted at the first step of the seed model.

### Time-resolved branch discrimination is the right experimental strategy

The report appropriately recommends measuring pre-tRNA, pre-rRNA, translation,
and mTOR/MYC before generalized arrest or loss of viability. That strategy
directly addresses causal order. A matched dual-complex perturbation is also
needed: a phenotype unique to shared-subunit RPP40 is not evidence for a
noncanonical role unless combined RNase P and RNase MRP loss reproduces the two
processing defects without reproducing the signaling phenotype.

## Major problems

### 1. It missed the separate primary HCC RPP40–ribosome study

The report says that the primary evidence base consists of one 2026 paper and
that an `RPP40+rRNA+HCC` search returned no hits. Both statements are false.

[PMID:40517827](https://pubmed.ncbi.nlm.nih.gov/40517827/) was published in
2025. Its title and abstract explicitly concern RPP40, pre-rRNA/ribosomal genes,
and HCC. The authors report that RPP40 coordinates ribosomal-RNA transcription
and ribosomal-gene expression while promoting HCC-cell malignancy.

The paper does not prove RNase MRP mediation or temporal ordering upstream of
mTOR/MYC, so it should be curated as **partial support for a concrete competing
rRNA/ribosome-biogenesis route**. It cannot be represented as a checked absence.

### 2. It omitted the strongest direct RPP40-versus-RNase-P experiment

[PMID:40533478](https://pubmed.ncbi.nlm.nih.gov/40533478/) is more diagnostic
than several reviews and indirect cancer studies in the evidence matrix. It
uses rapid degradation of shared RPP40 and RNase-P-specific RPP21, direct
precursor assays, and a time course. Its results sharply refine the hypothesis:

| Observation | Implication |
| --- | --- |
| RPP40 loss disrupts both pre-tRNA and pre-rRNA processing | RPP40 perturbation cannot assign the phenotype to one complex |
| RPP21 loss disrupts pre-tRNA but not pre-rRNA processing | RPP21 is a clean RNase-P-specific control |
| RNase P-only loss slows growth relatively late | RNase P can contribute, but is not the dominant acute proliferative effect in that model |
| Joint P/MRP loss causes rapid translation decline and arrest | RNase MRP/rRNA biogenesis is the stronger default competitor |

These data are from HEK293T and HCT116 cells, not HCC, and do not measure
mTOR/MYC. They qualify the seed model rather than directly refuting it.

### 3. The Rpp14 argument confuses two different reactions

The report argues that Rpp14, rather than RPP40, performs
5-prime-leader-degradation catalysis and concludes that an RPP40 perturbation
cannot isolate RNase-P pre-tRNA maturation “even in principle.”

[PMID:37831743](https://pubmed.ncbi.nlm.nih.gov/37831743/) distinguishes:

1. RNase P endonucleolytic cleavage of the precursor, which produces the mature
   tRNA 5-prime terminus; and
2. Rpp14 exonucleolytic degradation of the leader **after it has been excised**.

RPP40 need not itself be the nuclease to be required for holoenzyme integrity
and precursor cleavage. Consistent with that distinction, the RPP40-degron
experiment in PMID:40533478 directly produced accumulation of
5-prime-leader-containing pre-tRNAs. The valid limitation is that RPP40 is
shared with RNase MRP—not that Rpp14’s downstream exonuclease activity refutes
RPP40 participation in RNase P.

### 4. Canonical directionality is a competitor, not a refutation

Primary HCC evidence places mTORC1 upstream of the ribosome-biogenesis factor
HEATR1 ([PMID:37247644](https://pubmed.ncbi.nlm.nih.gov/37247644/)). This makes
the reverse-direction model important:

```text
mTOR/MYC activity → increased RNA/ribosome-biogenesis demand → increased RPP40
```

It does not rule out feedback in the other direction:

```text
loss of RNA-processing capacity → translational stress → reduced mTOR/MYC output
```

Both can operate in one feedback system. Only reciprocal perturbation,
time-resolved readouts, and epistasis can determine the operative ordering in
HCC.

### 5. Pan-essentiality is overinterpreted

[PMID:41933259](https://pubmed.ncbi.nlm.nih.gov/41933259/) supports broad
DepMap CRISPR essentiality and pan-cancer overexpression. That argues against
assuming an HCC-selective dependency. It does not establish that RPP40
upregulation is merely a passenger or that the HCC phenotype cannot use a
specific RNA-processing branch.

The report also omits a directly relevant limitation from that paper: the
CancerSEA expression-to-cell-cycle correlation was significant across the
examined cancers **except LIHC**. The paper’s cell-cycle mechanism is itself a
qualified multi-omics inference, not a branch-resolved RPP40 perturbation study.

### 6. One proposed “RNase-P-specific” handle is not clean

The report proposes `POP4/RPP21` versus `RPP24/RPP64`. Current primary studies
support:

- **RNase P:** RPP21 (and the catalytic RNA RPPH1/H1 RNA);
- **RNase MRP:** C18orf21/RMP24 and NEPRO/RMP64 (and RMRP RNA).

RPP21 is the unique protein subunit used for a clean RNase-P-specific
perturbation. POP4/RPP29 has been described as shared or preferentially
RNase-P-associated, so it should not be bundled into the unique-control label.
The current MRP-specific names are RMP24 and RMP64, not RPP24 and RPP64.
Relevant primary sources are
[PMID:40413743](https://pubmed.ncbi.nlm.nih.gov/40413743/) and
[PMID:41136609](https://pubmed.ncbi.nlm.nih.gov/41136609/).

## Revised evidence classification

| Claim | Assessment |
| --- | --- |
| RPP40 is upregulated and functionally associated with malignant HCC phenotypes | Supported by two HCC studies |
| RPP40 is linked to mTOR/MYC in HCC | Supported by one study; intervening mechanism unresolved |
| RPP40 affects pre-tRNA processing when acutely depleted | Directly supported outside HCC |
| RPP40 loss is RNase-P-specific | Refuted; RPP40 loss can destabilize both P and MRP |
| RNase P-only loss can affect proliferation | Supported outside HCC, but delayed/milder than joint P/MRP loss |
| RNase MRP/rRNA biogenesis is a strong competitor | Supported outside HCC and by an independent HCC RPP40–ribosome association |
| Rpp14 leader degradation refutes RPP40 holoenzyme contribution | Incorrect |
| RPP40 is a selective HCC dependency | Unsupported; broad essentiality argues against selectivity |
| RPP40 is merely a generic proliferation passenger in HCC | Unsupported; plausible alternative, not established |
| RNase-P/pre-tRNA loss precedes and causes mTOR/MYC decline in HCC | Unresolved |

## Curation implications

- Keep the hypothesis **EMERGING**, explicitly unwired, and framed as a
  falsifiable branch-ordering question.
- Retain PMID:40517827 as a competing rRNA/ribosome-biogenesis lead; do not
  record a source absence.
- Use PMID:40533478 to justify early processing readouts and to establish why
  RPP40 loss requires both single-complex and matched dual-complex controls.
- Use RPP21 for RNase P and C18orf21/RMP24 or NEPRO/RMP64 for RNase MRP.
- Treat the pan-cancer study as evidence of broad dependency and as motivation
  to test selectivity—not as proof that the HCC association is downstream or
  noncausal.
- Do not promote the report’s Rpp14 conclusion, source-absence claim, or
  branch-specific terminology into disease YAML.

The current PR’s conservative treatment—retaining the narrow hypothesis as
unresolved, representing the rRNA route as a competitor, and requiring
complex-specific early perturbation—is the appropriate curation outcome.
