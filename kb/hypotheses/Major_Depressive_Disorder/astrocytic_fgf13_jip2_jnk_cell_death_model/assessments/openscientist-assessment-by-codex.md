# Assessment of the OpenScientist FGF13–JIP2–JNK report

## Overall assessment

The report's core judgment is sound: **PARTIALLY_SUPPORTED, with the support
restricted to the tested mouse and primary-astrocyte systems**. One new study
reports bidirectional astrocyte-specific FGF13 perturbations, depression-like
behavior, apoptosis and inflammation in male stress-model mice, plus
FGF13/JIP2/JNK-associated results in primary astrocytes
([PMID:42421017](https://pubmed.ncbi.nlm.nih.gov/42421017/)). That is meaningful
direct evidence within the model. It is not adult human MDD evidence, and the
report correctly recommends keeping the hypothesis `EMERGING`.

The report is strongest when it separates the narrow, load-bearing FGF13/JIP2
claims from nonspecific downstream findings such as JNK activation, Bax/Bcl-2
change, inflammation and behavioral endpoints. Its proposed kinase-comparison,
region-matched human, sex-stratified and causal-mediation experiments are also
well chosen.

Several ancillary conclusions are too strong, however. The older p38delta
biochemistry is a serious unresolved conflict rather than a direct refutation;
the sex-transcriptomic paper does not predict a female-null FGF13 mechanism;
FGF2 and FGF9 are not as directly competing as the report implies; and selected
paper searches do not establish a resource-level genetic absence. Separately,
older human cortical FGF-system data supply background but do not, at the
abstract level, establish a negative FGF13 result either way.

| Dimension | Assessment |
| --- | --- |
| Direct source identification | Strong |
| Model-versus-human calibration | Strong |
| Causal-chain decomposition | Strong |
| Treatment of kinase conflict | Overstated |
| Sex-specific inference | Unsupported |
| Alternative-model classification | Mixed |
| Negative-search discipline | Weak |
| Curation recommendation | Appropriate |

## What the report gets right

### It identifies the only direct evidence

The direct evidence is one 2026 paper. Its abstract reports both
astrocyte-specific loss and overexpression experiments in mice, while the
supplement describes behavioral groups of 8–12 mice and primary-astrocyte
pathway immunoblots with `n=4` per group. The report appropriately treats this
as causal model-organism evidence and does not silently convert the secondary
human analysis into proof of the same hippocampal pathway.

The human component is a reanalysis of the all-male GSE144136 dlPFC cohort
originally reported in
[PMID:32341540](https://pubmed.ncbi.nlm.nih.gov/32341540/). It is cross-sectional,
cortical rather than hippocampal, and does not measure JIP2/JNK activity or
apoptosis. The report is right to call it limited association evidence.

### It correctly limits the positive human FGF13 evidence

The report describes the GSE144136 reanalysis as the only human component.
That remains the only positive, cell-type-specific human component of the seed
study. An earlier primary study of FGF-system transcripts
([PMID:15483108](https://pubmed.ncbi.nlm.nih.gov/15483108/)) reported
dysregulation of several transcripts in frontal cortical tissue but did not
identify FGF13 among the significant findings in its abstract. The abstract
says profiles of other detected growth factors and receptors were made
available; it does not establish that FGF13 was measured or nonsignificant in
either region.

The older study is therefore broad human FGF-system context, not direct
negative FGF13 evidence. It neither supports nor refutes the newer
astrocyte-specific association, because bulk tissue and older arrays cannot
adjudicate a cell-restricted signal from the abstract alone.

### It correctly keeps shared endpoints nonspecific

Astrocyte loss, inflammation, synaptic changes, JNK activity and
depression-like behaviors can arise through many routes. Independent examples
make those endpoints biologically plausible but do not validate the distinctive
FGF13→JIP2→JNK chain. The report's insistence on epistasis, pathway-specific
inhibitors and region-matched validation is therefore useful.

### Its curation disposition is conservative

Keeping `EMERGING`, preserving a human-model mismatch, and withholding a
FGF13/JIP2-directed treatment are the correct implications. The report provides
research leads, not grounds for a standalone human causal edge.

## Where the reasoning needs correction

### The p38delta study does not directly refute the astrocyte result

The report says:

> The JIP2→JNK edge is directly contradicted by prior biochemistry.

[PMID:12244047](https://pubmed.ncbi.nlm.nih.gov/12244047/) did show that
FHF2/FGF13 promoted IB2/JIP2 recruitment and activation of p38delta rather than
JNK in its native-brain-complex and heterologous biochemical experiments. That
is a real, load-bearing conflict. But it did not repeat the 2026 manipulation
in primary astrocytes or stress-exposed hippocampus. Cell type, state, isoform,
complex composition and assay differ.

The defensible classification is:

- `JIP2→JNK` in the new astrocyte system: directly reported once, unreplicated.
- `FHF2/FGF13→IB2/JIP2→p38delta`: independently supported in an older
  biochemical context.
- Kinase specificity across those contexts: unresolved and requiring a
  head-to-head p38delta/JNK experiment.

Calling this “directly contradicted” turns a valuable conflict into a stronger
refutation claim than the evidence warrants.

### The female-null prediction is not supported

The report moves from a sex-stratified dlPFC result to the prediction that the
FGF13 finding:

> is not expected to generalize to female MDD

[PMID:37217515](https://pubmed.ncbi.nlm.nih.gov/37217515/) found that the cell
types contributing the largest numbers of significant DEGs differed by sex.
It also found similar threshold-free MDD-associated expression patterns across
sexes and concordant astrocyte patterns. It did not analyze the
FGF13–JIP2–JNK chain, kinase activity or astrocyte death.

That paper supports including both sexes and testing interaction effects. It
does not establish a male subtype and does not justify an expected null result
in females.

### FGF2 is parallel, not a more parsimonious replacement

The report calls astrocytic FGF2:

> a more parsimonious, better-human-anchored FGF-family alternative

The primary study
([PMID:41545369](https://pubmed.ncbi.nlm.nih.gov/41545369/)) manipulated Fgf2 in
male mouse nucleus-accumbens astrocytes and implicated a blood-brain-barrier
stress-resilience route. Its human result is an association between circulating
FGF2 and symptom measures, not causal engagement of human astrocytes. This
differs from the hippocampal intracellular FGF13/JIP2/apoptosis proposal in
protein, region, target cell and intermediate mechanism.

FGF2 is a useful parallel comparator because it shows that an astrocytic FGF
manipulation can change a shared behavioral endpoint without validating
FGF13/JIP2. It is not evidence that the FGF13 model is less parsimonious.

### The FGF9 row combines evidence from different studies

The matrix says that
[PMID:37705188](https://pubmed.ncbi.nlm.nih.gov/37705188/) shows FGF9 is
“selectively upregulated in MDD” and suppresses synaptic/neuronal function. The
paper's experiments concern FGF9-treated cultures and cortical overexpression
in a progressive-multiple-sclerosis context. Its MDD expression statement is
background drawn from prior literature.

The directly relevant primary MDD paper is
[PMID:26351673](https://pubmed.ncbi.nlm.nih.gov/26351673/), which reported
increased hippocampal FGF9 across postmortem MDD datasets and affect-related
rodent perturbations. Even that evidence supports a parallel FGF9 model; it does
not test astrocytic FGF13, JIP2 or JNK. The report should not let the
MS-oriented experiment carry a composite MDD claim.

### “Search-verified genetic absence” is not earned

The report states:

> Search-verified source-level absence: FGF13 and MAPK8IP2/JIP2 are absent from
> prioritized human MDD GWAS/functional-genomics loci

It then lists a direct PGC-MDD GWAS/exome/GenCC/ClinGen lookup as an experiment
still needed to resolve the gap. Those two statements cannot both hold.
Checking whether several recent papers mention the genes is not equivalent to a
systematic locus, gene-burden and assertion-resource query.

The supported wording is:

> No human genetic support was identified in the papers inspected; a systematic
> resource-level search was not completed.

Also, the index paper appeared only 18 days before the report. Independent
replication was absent as of the assessment date, but that short interval makes
the absence expected rather than negative evidence.

## Revised evidential classification

| Claim | Assessment |
| --- | --- |
| Astrocyte-specific Fgf13 manipulation changes apoptosis, inflammation and behavior in male stress-model mice | Directly supported by one study |
| FGF13/JIP2/JNK-associated changes occur in primary mouse astrocytes | Directly reported once; small and unreplicated |
| FGF13–JIP2 physical association | Supported in new and older biochemical contexts |
| JIP2 uses JNK rather than p38delta in the relevant astrocyte state | Unresolved conflict, not directly refuted |
| Adult human hippocampal astrocytes execute this pathway in MDD | Unsupported |
| The mechanism is male-only or expected to be absent in females | Unsupported |
| FGF2 is a direct alternative to the FGF13 chain | Parallel comparator only |
| FGF9 neurotoxicity directly competes with astrocytic FGF13 | Parallel and incompletely sourced |
| FGF13/MAPK8IP2 human genetic support is absent | Not identified, but not systematically verified |
| FGF13/JIP2 is ready for therapeutic targeting | Unsupported |

## Curation implications

No change to the current conservative disease-level disposition is warranted:

- Keep the hypothesis `EMERGING`.
- Keep the scope explicit: male mouse hippocampus and primary mouse astrocytes.
- Retain the `HUMAN_MODEL_MISMATCH` discussion.
- Describe p38delta as conflicting pathway-specificity evidence, not a
  definitive refutation.
- Do not infer a male human subtype or a female-null result.
- Treat FGF2 and FGF9 as parallel comparators.
- Do not assert a human causal edge, genetic absence or FGF13/JIP2-directed
  treatment.

The highest-value next experiment remains a preregistered epistasis design in
adult astrocytes that directly compares JNK and p38delta readouts after FGF13
and JIP2 perturbation, followed by independent in-vivo replication in both
sexes and region-matched human hippocampal validation.
