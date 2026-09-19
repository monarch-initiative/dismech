# Canonical motor-neuron proteostatic-failure report assessment

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `PARTIALLY_SUPPORTED`

## Executive judgment

The report identifies real, important ALS biology. Diverse genetic causes and
sporadic disease converge on motor-neuron dysfunction through TDP-43 pathology,
mutant-protein toxicity, RNA dysregulation, impaired clearance, mitochondrial
stress, axonal transport defects, and non-cell-autonomous injury. The report is
also right to retract the seed hypothesis's claim that a C9orf72 antisense
program provided clinical validation.

The evidence does not establish one universal “proteostatic failure” sequence.
The model is a useful umbrella over mechanistically different ALS subtypes, and
the report itself finds competing upstream orders. Its strongest language
frequently converts cellular sufficiency, postmortem association, model
timing, or an exploratory clinical analysis into human causal ordering.

The largest corrections are:

1. VALOR showed SOD1 and neurofilament target engagement but missed its
   prespecified randomized clinical endpoint.
2. BIIB078 failure does not identify which C9orf72 mechanism dominates.
3. The report assigns the approximately 2% all-ALS SOD1 fraction to familial
   ALS.
4. A TDP-43 mutant-mouse result does not establish aggregation as a late-stage
   human marker.
5. The proposed Betz-cell, alpha-motor-neuron, and protein-folding ontology
   mappings contain two swapped/wrong cell identifiers and one obsolete GO
   term.

## What is supported

### ALS has genuine molecular convergence

The large ALS GWAS in
[PMID:34873335](https://pubmed.ncbi.nlm.nih.gov/34873335/) supports
heterogeneous genetic architecture with neuron-specific and trafficking or
autophagy biology. TDP-43 pathology is broadly characteristic of ALS outside
important SOD1- and FUS-associated exceptions. SOD1, C9orf72, TARDBP, FUS, and
other genotypes provide distinct upstream routes that can meet at shared
cellular stresses.

This makes the canonical model useful as a convergence framework. It does not
make “proteostatic failure” a single demonstrated initiator or establish that
every listed mechanism occurs in every subtype.

### BIIB078 did not validate C9orf72 RNA targeting

The randomized phase 1 BIIB078 study
([PMID:39059407](https://pubmed.ncbi.nlm.nih.gov/39059407/)) found no
neurofilament reduction or clinical benefit relative to placebo, and
development was discontinued. The report correctly rejects the seed's claim
that a C9orf72 ASO had therapeutically validated that genetic axis.

The negative study cannot determine why the program failed. Exposure, timing,
sense versus antisense transcripts, dipeptide repeats, haploinsufficiency,
TDP-43 pathology, and other mechanisms remain competing explanations. It does
not prove that combined targeting is necessary or that DPR toxicity dominates.

### Aggregation is not required in one TDP-43 mouse model

[PMID:23382207](https://pubmed.ncbi.nlm.nih.gov/23382207/) directly showed
motor axon degeneration and motor-neuron death in TDP-43 Q331K and M337V mice
without nuclear TDP-43 loss, aggregate accumulation, or insoluble TDP-43. This
is strong evidence against aggregation being necessary in that model.

It does not determine whether aggregates are early, late, toxic, protective,
or incidental in sporadic human ALS. The report's general “late-stage marker”
conclusion should therefore remain a model-derived hypothesis.

## Major qualifications

### 1. Tofersen is meaningful but not an unqualified efficacy validation

The pivotal randomized VALOR study
([PMID:36129998](https://pubmed.ncbi.nlm.nih.gov/36129998/)) lowered CSF SOD1
and plasma neurofilament. At 28 weeks, however, the ALSFRS-R primary endpoint
and secondary clinical endpoints did not differ significantly from placebo.

Long-term follow-up
([PMID:41661214](https://pubmed.ncbi.nlm.nih.gov/41661214/)) reported numerical
advantages for earlier versus delayed initiation and survival relative to
expected natural history. After crossover, that comparison was no longer a
blinded randomized efficacy test, and only 46 of 95 open-label entrants
completed the extension. Together, these data support target engagement and an
encouraging SOD1-specific treatment. They should not be used as simple proof of
the complete proteostatic model.

The four-person Icelandic series
([PMID:41670738](https://pubmed.ncbi.nlm.nih.gov/41670738/)) is notable but
uncontrolled and variant-specific. It cannot independently supply “compelling
causal evidence.”

### 2. The SOD1 denominator is wrong

The report's causal diagram says “SOD1 mutations (~2% fALS).” Approximately 2%
is an estimate for all ALS attributable to SOD1, as the report itself states
elsewhere and the long-term tofersen paper reiterates. Familial-ALS estimates
are commonly around 10–20%, with population variation; a prospective Polish
cohort found SOD1 variants in 21.1% of familial and 2.3% of sporadic cases
([PMID:34996976](https://pubmed.ncbi.nlm.nih.gov/34996976/)).

### 3. NPC perturbation is causal in cells, not temporally proven in patients

[PMID:40819564](https://pubmed.ncbi.nlm.nih.gov/40819564/) found NPC component
loss in ALS postmortem tissue and models. CRISPR depletion of NUP107 in human
cells produced TDP-43 mislocalization, phosphorylation, and autophagy
dysfunction, which is direct cellular sufficiency evidence. TDP-43 knockdown
also changed NPC composition, suggesting reciprocity.

The study does not show NPC loss preceding TDP-43 pathology in living patients
or establish one universal upstream edge across ALS.

### 4. Axonal-transport primacy is a proposed synthesis

[PMID:41890591](https://pubmed.ncbi.nlm.nih.gov/41890591/) explicitly says “we
propose” axonal transport as an early convergent upstream vulnerability. It
synthesizes heterogeneous model, iPSC, and imaging evidence. The report's
matrix correctly calls this review-level; other sections should not present the
proposal as direct temporal proof.

### 5. Postmortem somatic variants do not establish initiation

[PMID:41378777](https://pubmed.ncbi.nlm.nih.gov/41378777/) found enriched
low-allele-frequency variants in sporadic-ALS motor cortex and accumulation in
excitatory neurons. Its conclusion is appropriately cautious: somatic variants
*may contribute*. Autopsy data cannot establish that they initiated disease,
so the proposed `somatic_mutations → sporadic_ALS_initiation` edge should not be
promoted.

## Ontology corrections

The proposed mappings are not safe to curate:

- `CL:0002071` is an enterocyte of the large-intestine epithelium, not Betz
  cell.
- `CL:0008049` is Betz cell, not alpha motor neuron.
- `CL:0008038` is the current alpha-motor-neuron term.
- `GO:0061077` is obsolete; it points to `GO:0006457` protein folding.

The other candidate identifiers still need normal term validation before use.

## Search-provenance limitation

The report says it reviewed 103 publications and confirmed eight findings, but
its delivered citation sidecar lists 35 PMIDs. It provides no complete corpus,
executable queries, screening decisions, or paper-to-finding audit trail.
These counts should be treated as provider metadata rather than reproducible
systematic-review coverage.

## Claim-level disposition

| Claim | Disposition | Reason |
| --- | --- | --- |
| Diverse ALS routes converge on proteostatic and cellular stress | **Qualified** | Component biology is supported; one universal causal sequence is not. |
| Tofersen validates the SOD1 axis | **Qualified** | Strong target engagement and encouraging follow-up; randomized 28-week clinical endpoints were negative. |
| Four Icelandic cases give compelling causal proof | **Qualified** | Notable but uncontrolled, small, and variant-specific. |
| C9orf72 ASO therapy has not achieved clinical validation | **Retained** | BIIB078 showed no NfL or clinical benefit and was discontinued. |
| BIIB078 proves one mechanism cannot be targeted alone | **Qualified** | The failed program does not discriminate among mechanisms or technical explanations. |
| SOD1 causes about 2% of familial ALS | **Rejected** | The denominator is all ALS; familial proportions are much higher. |
| Aggregation is generally a late-stage marker | **Qualified** | One mutant-mouse model shows it is unnecessary, not its timing in humans. |
| NPC dysfunction is upstream in human ALS | **Qualified** | Cellular sufficiency and postmortem association do not establish human temporal primacy. |
| Axonal transport is proven upstream | **Qualified** | The cited source proposes a cross-study framework. |
| Somatic mutations initiate sporadic ALS | **Rejected** | Cross-sectional postmortem enrichment cannot establish initiation. |
| Proposed CL/GO mappings match their labels | **Rejected** | Two cell mappings are wrong and one GO term is obsolete. |
| 103 papers were systematically reviewed | **Needs verification** | Only 35 citations and no reproducible screening trail are delivered. |

## Curation implications

- Retain the canonical hypothesis as a heterogeneous convergence model.
- Preserve the negative BIIB078 result without inferring DPR dominance.
- Describe tofersen with both biomarker and randomized clinical-endpoint
  results.
- Keep NPC, axonal-transport, somatic-mutation, HK1, and related findings
  explicitly scoped to their experimental systems.
- Do not promote the incorrect or obsolete ontology identifiers.
- Assessment citations are context only and are not automatically disease-YAML
  evidence.

## Existing disease-YAML implications

The current ALS disorder YAML already incorporates provider-derived
overstatements. It says BIIB078 failure indicates DPR-mediated toxicity likely
dominates the C9orf72 axis, presents NPC dysfunction as upstream of TDP-43
proteinopathy without a human temporal qualifier, and creates a directional
somatic-initiation lead elsewhere in the report. This assessment PR
deliberately does not edit the disorder YAML. Those promoted claims should be
reviewed in a separate curation change with evidence scope and provenance
checked independently.
