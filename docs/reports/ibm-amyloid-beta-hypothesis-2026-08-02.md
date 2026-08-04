# Hypothesis exploration: are amyloid-beta and its precursors abnormally and specifically present in inclusion body myositis?

**Date:** 2026-08-02
**Target entry:** `kb/disorders/Inclusion_Body_Myositis.yaml` (sporadic IBM, `MONDO:0007827`)
**Hypothesis id curated:** `amyloid_beta_proteotoxicity`
**Verdict:** the *specificity* claim is refuted; the *abnormal presence* claim is unresolved but poorly supported. Curated as `status: DEPRECATED` with an OPEN `CONTROVERSY` discussion.

## Why this was worth exploring

The dismech IBM entry carried two mechanistic hypotheses — `autoimmune_primary` (CANONICAL)
and `degeneration_primary` (ALTERNATIVE) — and mentioned amyloid-beta only in passing, as one
constituent listed in the description of the `Autophagy-Lysosome Failure and Rimmed Vacuole
Formation` node. The single most famous mechanistic claim ever made about IBM was therefore
absent from a knowledge base whose purpose is to record disease mechanism. A curator meeting
amyloid claims in the IBM literature — and they are everywhere, including in older diagnostic
criteria — had nothing in the entry to check them against.

## The claim, as originally made

Askanas and Engel, from the early 1990s, cast sporadic IBM as a muscle analogue of Alzheimer
disease. Vacuolated myofibres were reported to transcribe APP at increased levels
([PMID:8394158](https://pubmed.ncbi.nlm.nih.gov/8394158/)); APP and its cleavage product
amyloid-beta, preferentially the aggregation-prone Abeta42, were reported to accumulate
intracellularly and to be the "key upstream pathogenic events"
([PMID:16432144](https://pubmed.ncbi.nlm.nih.gov/16432144/)); and soluble Abeta oligomers
(ADDLs) were later reported by immunoblot in every sIBM sample studied and in no control
([PMID:20711838](https://pubmed.ncbi.nlm.nih.gov/20711838/)).

It is worth separating the two assertions bundled in the phrase "abnormally and specifically
present", because they resolve differently.

## Specificity: refuted

Amyloid-positive, ubiquitinated, tubulofilamentous rimmed vacuoles that are
morphologically and immunologically indistinguishable from those of IBM occur in:

| Setting | Source |
|---|---|
| Long-standing denervation (postpoliomyelitis muscular atrophy) — vacuoles in 31% of biopsies, Congo-red positive in 27.8% | [PMID:9781653](https://pubmed.ncbi.nlm.nih.gov/9781653/) |
| Congenital myopathy of children — "the full morphological phenotype of IBM including beta-amyloid and tau protein deposits" | [PMID:16788822](https://pubmed.ncbi.nlm.nih.gov/16788822/) |

**Oculopharyngeal muscular dystrophy is *not* on that list**, and it is worth saying why,
because it is the obvious third candidate. OPMD shares the ubiquitinated filamentous
inclusions, but the one study here that applied a beta-amyloid antibody to it reports the
opposite of what the non-specificity argument would need: *"Labelling with
anti-beta-amyloid-protein antibody was seen in a few fibres in IBM but not in the other two
conditions"* ([PMID:8268725](https://pubmed.ncbi.nlm.nih.gov/8268725/) — the other two being
familial IBM-like disorder and OPMD). That item is curated `PARTIAL`, and OPMD appears in
this entry only as an experimental control arm, never as evidence. Denervation and
congenital myopathy carry the specificity argument on their own.

The postpolio authors draw the general conclusion the specificity claim cannot survive:
*"The chronicity of the underlying disease, rather than the cause, may lead to vacuolar
formation, amyloid deposition, and accumulation of ubiquitinated filaments."*

The quantitative comparison is more damaging still. Scoring markers head to head in the same
biopsies ([PMID:19533646](https://pubmed.ncbi.nlm.nih.gov/19533646/)):

| Marker | % of IBM myofibres |
|---|---|
| Sarcoplasmic TDP-43 | 23% |
| Rimmed vacuoles | 2.8% |
| SMI-31 | 0.83% |
| Fluorescent Congo red material | 0.57% |
| **Focal R1282 beta-amyloid immunoreactivity** | **0.00%** |

and sarcoplasmic TDP-43 at >1% of fibres was 91% sensitive and 100% specific for IBM across
50 inflammatory myopathy samples. TDP-43 mislocalization, not amyloid, is the specific
molecular signature of IBM. This is consistent with the entry's existing framing that
aggregate-bearing fibres number fewer than 1% and are a marker rather than the dominant
injury mechanism.

## Abnormal presence: unresolved, and weakly supported

This half does not resolve as cleanly, and it would be overreach to call it refuted.

**Against.** Unbiased laser-capture mass spectrometry of the rimmed vacuole itself recovered
213 proteins enriched >1.5-fold, dominated by protein-folding and autophagy machinery, and
did not report amyloid-beta or APP among them
([PMID:28009083](https://pubmed.ncbi.nlm.nih.gov/28009083/)) — which is not what the
hypothesis predicts of its own signature lesion. Cultured IBM myotubes, from the originating
laboratory, do not accumulate betaAPP at all, so whatever drives accumulation in biopsy tissue
is not cell-autonomous ([PMID:10599804](https://pubmed.ncbi.nlm.nih.gov/10599804/)). And the
companion phospho-tau limb of the Alzheimer analogy was shown to rest on antibodies that
stain normal myonuclei and recognize proteins other than tau
([PMID:19626672](https://pubmed.ncbi.nlm.nih.gov/19626672/)) — a direct demonstration that the
reagent class the histological arm depended on can report protein accumulation that is not
there.

**For.** The Abeta-dimer/trimer/tetramer immunoblots and anti-ADDL dot-blots
([PMID:20711838](https://pubmed.ncbi.nlm.nih.gov/20711838/)) are antibody-based but are not
immunohistochemistry, they were positive in every sIBM sample and negative in every control,
and they have not been retracted or directly rebutted. They issue almost entirely from the
laboratory that proposed the hypothesis and have not been widely replicated independently,
but "not independently replicated" is not "refuted". The negative from proteomics is an
*absence* of detection, and spectral-count proteomics is weak at small, poorly soluble,
aggregation-prone peptides.

Note also what the controls were: normal and general disease controls, not the
chronic-denervation and OPMD muscle that the specificity literature identifies as the
comparison that actually matters.

## The meta-scientific finding

The belief that beta amyloid is produced by and injures IBM muscle is the literal subject of
Greenberg's citation-network analysis ([PMID:19622839](https://pubmed.ncbi.nlm.nih.gov/19622839/)).
Across 242 papers and 675 citations addressing the belief, the study found authority
established by *"citation bias against papers that refuted or weakened the belief;
amplification, the marked expansion of the belief system by papers presenting no data
addressing it; and forms of invention such as the conversion of hypothesis into fact through
citation alone."*

This measures citations, not muscle, and it cannot settle a biological question. What it does
settle is that the apparent weight of literature behind the hypothesis substantially overstates
the underlying data — which is why the hypothesis is curated `DEPRECATED` rather than merely
`ALTERNATIVE`, and why the proposed resolving experiments below are all antibody-independent
or replication-in-another-lab designs.

## Direction of causation, if any amyloid is real

Even granting some genuine amyloid-beta, its position in the causal chain is contested in the
opposite direction from the original model. Benveniste and colleagues
([PMID:25579751](https://pubmed.ncbi.nlm.nih.gov/25579751/)) argue that inflammation comes
first and that *"if the protein degradation systems are overloaded ... amyloid and other
protein deposits may appear within muscle fibres, reinforcing the myopathic process in a
vicious circle"* — amyloid as consequence and amplifier, not initiator. This is recorded as
`REFUTE` evidence on the edge from the amyloid node into the autophagy-lysosome node.

## What was changed in the knowledge base

1. **New `mechanistic_hypotheses` entry** `amyloid_beta_proteotoxicity`, `status: DEPRECATED`,
   with 11 evidence items spanning SUPPORT (3), REFUTE (6) and PARTIAL (2), so both sides of
   the assessment are anchored in verified snippets rather than in the description prose.
2. **New pathophysiology node** `Amyloid-beta and APP Accumulation in Myofibres`,
   `mechanism_confidence: HYPOTHETICAL`, `biological_scale: MOLECULAR`, bound to `hgnc:620`
   (APP), `GO:0042982` and `GO:0034205`, carrying both the founding positive evidence and the
   quantitative and in-vitro refutations. Its two `downstream` edges opt into the
   `amyloid_beta_proteotoxicity` hypothesis group, so the disputed chain is queryable as a
   group and is not confused with the two live models.
3. **New discussion** `ibm_amyloid_beta_specificity`, `kind: CONTROVERSY`, `status: OPEN`,
   attached to the new node and to the autophagy-lysosome node, with three proposed
   experiments: blinded multi-laboratory targeted mass spectrometry (PRM / IP-MS with
   isotope-labelled Abeta40/42 standards) against chronic-injury disease controls;
   independent pre-registered replication of the oligomer immunoblots; and a test of whether
   amyloid burden predicts functional decline independently of T cell infiltrate and TDP-43
   cryptic exon burden.

4. **Rendering.** A DEPRECATED hypothesis now renders an explicit "Overturned model —
   shown for reference, not as current mechanism" callout stating that DisMech does not
   assert the model and that citation volume does not decide standing; an evidence-balance
   row shows the SUPPORT / PARTIAL / REFUTE split (here 3 / 2 / 6); and hypothesis chips on
   pathophysiology nodes and causal edges carry the deprecated status so a node in a retired
   group is not read as current. The policy is recorded as design decision
   [§6a](../explanation/design-decisions.md).

Deliberately **not** done: no `conforms_to` edge to the `amyloidogenesis` module was added.
That module models genuine amyloid-deposit formation (AL, ATTR, AA, Alzheimer), and declaring
conformance would assert as curated fact precisely the claim this exploration finds
unsupported. If the targeted mass-spectrometry experiment above ever returns positive, that
edge is the natural next change.

## Validation

```
linkml-validate -C Disease                    → No issues found
run_reference_validator.sh validate data      → Snippets checked: 131/131 verified
run_term_validator.sh validate-data --labels  → Validation passed
```

All 13 newly cited references were fetched with the reference validator's cache command; no
cache file was hand-written.
