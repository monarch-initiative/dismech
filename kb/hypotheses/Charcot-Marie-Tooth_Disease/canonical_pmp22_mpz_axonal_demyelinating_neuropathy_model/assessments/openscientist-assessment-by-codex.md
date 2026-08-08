# Assessment of the OpenScientist canonical CMT report

## Overall assessment

**Verdict on the scoped canonical framework: supported.**

The report is right about the broad architecture. Charcot-Marie-Tooth disease is
genetically and mechanistically heterogeneous; PMP22 duplication is the leading
resolved cause; major subtypes begin in either the Schwann-cell/myelin or
neuronal/axonal compartment; and distal axonal dysfunction or loss is a major
determinant of disability. The 1,515-person specialist cohort directly supports
the genetic hierarchy
([PMID:38481354](https://pubmed.ncbi.nlm.nih.gov/38481354/)), and the cited human
and model studies make the canonical framework much more than a speculative
hypothesis.

That overall verdict should not be read as an endorsement of the report's finer
claims. Several of its seven advertised “qualifications” are useful model-level
leads, but the report repeatedly turns them into disease-wide or human
conclusions. It also contains a directionality error in its cholesterol trial
proposal, a species error in its clinical-trial summary, two incorrect ontology
mappings, and unreconstructable corpus and figure claims.

## What should be retained

### The genetic and compartment-level framework is strong

The report correctly ranks PMP22 duplication as the commonest genetic diagnosis.
The exact proportion needs denominator discipline: it was 505 of 1,165 solved
cases (43.3%) but 505 of all 1,515 clinically diagnosed participants (33.3%) in
the cited specialist cohort. The “approximately 60%” number comes from a
background statement about pathogenic variations in
[PMID:31852984](https://pubmed.ncbi.nlm.nih.gov/31852984/), not from that paper's
200-person PMP22-duplication-negative analysis. These numbers should not be
rendered as a single 43–60% range of diagnosed-case fractions.

The common-path concept is also useful if it is not made universal. Distal
axonal loss is strongly associated with severity, but the report itself cites
pronounced impairment in CMT1A model mice without overt axonal loss
([PMID:41400104](https://pubmed.ncbi.nlm.nih.gov/41400104/)). Developmental
myelin dysfunction, primary axonal injury, and subtype-specific additional
phenotypes remain biologically meaningful before and alongside late axonal
convergence.

### Direct PMP22 lowering has strong preclinical support

[PMID:29202483](https://pubmed.ncbi.nlm.nih.gov/29202483/) reports post-onset
rescue with PMP22 antisense oligonucleotides in two rodent models and a rat-skin
target-engagement readout.
[PMID:41948127](https://pubmed.ncbi.nlm.nih.gov/41948127/) reports durable
miR871-mediated lowering and phenotypic improvement in a humanized CMT1A mouse,
plus dose, safety, target-engagement, and biodistribution work in mice and
non-human primates. These are important preclinical validations, not human
clinical efficacy.

The report's PXT3003 numbers are also accurate. The high-dose arm showed a
statistically significant but small ONLS difference in
[PMID:34656144](https://pubmed.ncbi.nlm.nih.gov/34656144/). The high-dose
formulation crystallized, the arm was stopped early, extensive missing data led
to a modified analysis set, and PXT3003 is not direct PMP22 silencing. The
report appropriately calls the effect modest and qualified.

### KIF1B should be represented as limited

The original KIF1B association came from one pedigree
([PMID:11389829](https://pubmed.ncbi.nlm.nih.gov/11389829/)); later studies found
MFN2 in most families linked to the historical CMT2A locus
([PMID:16043786](https://pubmed.ncbi.nlm.nih.gov/16043786/)). Additional KIF1B
variants have functional support, but the human pedigrees remain few
([PMID:30126838](https://pubmed.ncbi.nlm.nih.gov/30126838/)). Consistent with the
report's proposed downgrade, the
[ClinGen Charcot-Marie-Tooth GCEP](https://search.clinicalgenome.org/kb/gene-validity/CGGV%3Aassertion_ae6ffeae-9609-47bf-89a9-4863cf6ef05c-2026-06-12T160000.000Z)
classified KIF1B–CMT2A1 as **Limited** in June 2026. That expert-panel result
postdates the provider report but supports the assessment.

## Material scientific corrections

### “Dysmyelinating, not demyelinating” is too absolute

The skin-biopsy study found uniformly shortened internodes and no segmental
demyelination in the sampled dermal fibers of 32 CMT1A patients
([PMID:19923170](https://pubmed.ncbi.nlm.nih.gov/19923170/)). Its conclusion says
that this **suggests** a potential developmental defect. The long-term mouse
study similarly found delayed, incomplete, then stable myelination
([PMID:21487305](https://pubmed.ncbi.nlm.nih.gov/21487305/)).

Those results support a major developmental dysmyelination component; they do
not establish that CMT1A is never demyelinating across every nerve compartment
and stage. The first paper itself describes inherited versus acquired
“demyelinating neuropathies,” and another cited translational study explicitly
calls CMT1A “dysmyelinating and demyelinating”
([PMID:22189569](https://pubmed.ncbi.nlm.nih.gov/22189569/)). The conventional
electrophysiologic demyelinating class and a developmental dysmyelination
mechanism are compatible. The disease YAML should not copy the report's
all-caps absolute reclassification.

There is also an internal timing tension: the report infers that treatment may
need to target a developmental window, then cites ASO rescue after disease
onset. Developmental timing is worth testing; it is not an established reason
to deprioritize adult intervention.

### Structural PMP22 evidence is compelling but remains model-level

[PMID:41400104](https://pubmed.ncbi.nlm.nih.gov/41400104/) directly shows
junctional and nodal disorganization in CMT1A and HNPP model mice and proposes
PMP22 as a structural organizer. The same abstract calls impaired metabolic
support and axonal excitability predictions. This is a strong new mechanistic
lead, not yet a quantified human causal branch or a demonstrated actionable
target.

### The cholesterol trial proposal reverses the tested dosage context

[PMID:32511821](https://pubmed.ncbi.nlm.nih.gov/32511821/) supports altered
cholesterol handling across PMP22 gain-, loss-, and point-mutation systems. The
critical intervention detail is lost in the report: cholesterol supplementation
improved myelination in explants from **heterozygous PMP22-deficient mice**, a
loss-of-function/HNPP context. In the overexpression model, cholesterol was
sequestered in lysosomes and efflux fell.

The proposed pilot of cholesterol supplementation or an LXR agonist in
PMP22-duplication CMT1A therefore does not follow from the rescue experiment.
Direction, dose, tissue delivery, and safety must first be resolved in an
appropriate duplication model. A newer patient-derived Schwann-cell-precursor
study supports lipid-homeostasis disruption in CMT1A and rescue through
autophagy/lipolysis, not simple cholesterol add-back
([PMID:38743588](https://pubmed.ncbi.nlm.nih.gov/38743588/)).

### SARM1 is causal in one CMT2A rat model, not yet universal

Deleting Sarm1 rescued much of the pathology in Mfn2-H361Y rats and revealed a
mitochondrial feedback loop
([PMID:36287202](https://pubmed.ncbi.nlm.nih.gov/36287202/)). This is high-value
genetic perturbation evidence. The source says “much of the neuropathology in
this model”; it does not show that SARM1 is rate-limiting in human CMT2A, every
MFN2 genotype, or unrelated axonal CMT subtypes. “Therapeutic candidate” is the
appropriate translational status.

### UPR convergence is preclinical

[PMID:35501630](https://pubmed.ncbi.nlm.nih.gov/35501630/) shows IFB-088 benefit
and movement of UPR markers toward wild type in C3-PMP22 and Mpz-R98C mice. This
supports a cross-model proteostasis lead. It does not yet validate UPR as a
human disease-modifying target, and overexpressed PMP22 and a misfolded MPZ
mutant need not engage the pathway in identical ways.

### The immune evidence is model- and subtype-specific

The evidence matrix labels PMID:16775375 “model organism,” but PubMed classifies
it as a review. Its abstract reports RAG1 crosses in P0-deficient CMT1B and
Cx32-deficient CMT1X models. CMT1A is described as having increased immune cells,
not as receiving the same RAG1 perturbation. The cited CSF1 isoform paper
directly tests a CMT1X mouse
([PMID:26865613](https://pubmed.ncbi.nlm.nih.gov/26865613/)). Immune amplification
is credible in several models but is not uniform: the review also reports a
neuroprotective immune effect in a severe P0-null model.

Most importantly, complement inhibition was **not** a failed human CMT1A
intervention. [PMID:36926597](https://pubmed.ncbi.nlm.nih.gov/36926597/) used C6
antisense oligonucleotides in two PMP22-overexpressing mouse models. It reduced
neuroinflammatory pathway signals without improving motor function. The
executive judgment's placement of this experiment among failed human trials is
a material species and evidence-level error. The mechanistic review later
describes the same experiment correctly as systemic complement inhibition in
CMT1A mice, so the problem is confined to the executive judgment.

### Ascorbic-acid failure has not been mechanistically explained

The negative trial conclusion is robust: five trials failed, including the
277-person, two-year randomized study
([PMID:21393063](https://pubmed.ncbi.nlm.nih.gov/21393063/)). The claim that tight
absorption control “likely explains” the failures comes from a pharmacokinetic
perspective that proposes this explanation
([PMID:23525455](https://pubmed.ncbi.nlm.nih.gov/23525455/)). It was not tested as
the causal reason. Target biology, nerve exposure, outcome sensitivity, and
model fidelity remain alternatives.

### Human experimental support is narrower than clinical proof, but not absent

No cited study demonstrates clinical benefit from direct PMP22 lowering in
people. That is the correct translational gap. Calling the **entire** dosage axis
devoid of human validation is too broad:

- Patient-derived CMT1A PNS organoids showed myelin abnormalities improved by
  PMP22 downregulation
  ([PMID:36511878](https://pubmed.ncbi.nlm.nih.gov/36511878/)).

- Editing the duplicated region rescued phenotypes in patient-derived iPSC
  Schwann cells
  ([PMID:38017287](https://pubmed.ncbi.nlm.nih.gov/38017287/)).

These are human-cell proof-of-concept, not human clinical proof.

The “complete absence” of human single-cell evidence likewise needs a narrower
scope. On 2026-07-31, a PubMed search for `("Charcot-Marie-Tooth"[Title/Abstract]
OR CMT1A[Title/Abstract] OR CMT1B[Title/Abstract] OR CMT2A[Title/Abstract] OR
CMTX1[Title/Abstract]) AND ("single cell"[Title/Abstract] OR
"single-cell"[Title/Abstract] OR "single nucleus"[Title/Abstract] OR
"single-nucleus"[Title/Abstract] OR scRNA-seq[Title/Abstract] OR
snRNA-seq[Title/Abstract] OR "spatial transcriptomics"[Title/Abstract] OR
"spatial omics"[Title/Abstract])` returned 13 records. Manual screening found
no single-cell or spatial profiling of ex vivo CMT nerve. However, PMID:36511878
used single-cell analysis in patient-derived CMT1A PNS organoids. The useful gap
is therefore ex vivo patient-nerve single-cell/spatial profiling, not complete
absence of CMT-derived human single-cell work.

### Metabolic support and oligogenic inheritance remain leads

Schwann-cell MCT1 deletion disrupted long-term motor-endplate innervation while
leaving peripheral myelin intact
([PMID:32686211](https://pubmed.ncbi.nlm.nih.gov/32686211/)). A separate culture
study supports a role for lactate homeostasis in myelination-related gene
expression ([PMID:25762662](https://pubmed.ncbi.nlm.nih.gov/25762662/)). Neither
tested CMT, so lactate shuttling is external plausibility for the missing
Schwann-cell-to-axon link, not an established intermediate CMT mechanism.

The non-Mendelian evidence also needs restraint.
[PMID:32741968](https://pubmed.ncbi.nlm.nih.gov/32741968/) reports a preliminary
risk allele and explores multilocus inheritance.
[PMID:35153971](https://pubmed.ncbi.nlm.nih.gov/35153971/) found variants in two
genes in 4 of 189 families. Coexisting variants and severity modification do
not demonstrate that both loci are required for disease. Modifier architecture
is plausible; a defined oligogenic CMT class is not established by these two
studies.

### Biomarkers are promising, not validated surrogates

The MRI studies are encouraging but small: 20 CMT1A participants in the
four-year analysis
([PMID:39957630](https://pubmed.ncbi.nlm.nih.gov/39957630/)) and 20 participants
plus 7 controls in the automated-segmentation study
([PMID:37979968](https://pubmed.ncbi.nlm.nih.gov/37979968/)). The plasma study
included 44 cases and 44 controls and found moderate severity correlations for
NfL and GFAP ([PMID:39882365](https://pubmed.ncbi.nlm.nih.gov/39882365/)). These
data support candidate biomarkers. They do not prove a field-wide “most
responsive” ranking, causal dual pathology, treatment responsiveness, or
surrogate-endpoint validity. The report's later biomarker gap correctly admits
the last limitation.

## Ontology corrections

The curation-lead list is not ontology-ready:

- `CL:0000218` correctly labels **myelinating Schwann cell**.
- `CL:0000333` labels **migratory neural crest cell**, not generic neural crest
  cell; the latter is `CL:0011012`.
- `GO:0031175` labels **neuron projection development**, not axon degeneration.
- `GO:0006986` has the canonical label **response to unfolded protein**, not
  “unfolded protein response,” although it is the relevant UPR process.
- The non-myelinating Schwann-cell and endoneurial-macrophage suggestions lack
  identifiers.

The myelination, cholesterol-transport, and Schwann-cell-differentiation
identifiers are valid. The presence of valid terms does not make the full list
safe to copy. The labels above were checked on 2026-07-31 with:

```shell
uv run runoak -i sqlite:obo:cl info CL:0000333 CL:0011012 CL:0000218
uv run runoak -i sqlite:obo:go info GO:0031175 GO:0006986
```

## Corpus and artifact provenance

The frontmatter records 42 citations, and the citation manifest contains 42
PMIDs. The evidence matrix contains 29 rows. The report nevertheless claims “36
primary findings across 128 papers reviewed over 5 investigation iterations.”
No search strategies, screening log, excluded-result record, or complete
128-paper corpus is deposited. The larger review may have occurred, but its
count and claimed systematic coverage are not reproducible.

The report also references five figures:

- `evidence_strength_heatmap.png`
- `final_summary_visualization.png`
- `mechanistic_causal_chain.png`
- `biomarker_landscape_and_gaps.png`
- `evidence_strength_assessment.png`

None is present in the hypothesis directory. The reported UniProt SPARQL check
is similarly missing an endpoint, query, retrieval date, result table, and
accession list. These omissions do not negate the source-backed prose, but they
prevent audit of the claimed corpus, figures, and database count.

## Curation consequence

Retain the hypothesis as `CANONICAL`, but do not preserve the provider's seven
qualifications verbatim in the disease YAML. In particular:

1. Keep conventional CMT1A demyelinating classification while noting strong
   developmental dysmyelination evidence.
2. Scope structural PMP22, UPR, SARM1, inflammation, metabolic support, and
   lipid branches to the tested model and subtype.
3. Correct the executive-summary claim that complement inhibition failed in
   humans; retain its later, accurate description as a CMT1A mouse experiment.
4. Do not promote cholesterol supplementation for PMP22-duplication CMT1A.
5. Separate clinical absence of direct PMP22-lowering efficacy from existing
   patient-derived cell and organoid proof-of-concept.
6. Represent KIF1B–CMT2A1 as limited, not equivalent to MFN2–CMT2A.
7. Correct ontology identifiers before adding new nodes or edges.

Each promoted paper-derived statement still needs the normal DisMech reference
cache, exact-snippet, evidence-source, and ontology validation workflow.
