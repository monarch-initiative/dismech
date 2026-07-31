# Paternal GNAS loss-of-function report assessment

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `PARTIALLY_SUPPORTED`

## Executive judgment

The report is right about the central mechanism. Paternal coding loss of
`GNAS` usually leaves sufficient Gs-alpha signaling in the renal proximal
tubule to avoid classic PTH resistance, while reducing Gs-alpha dosage in
biallelic tissues and producing AHO skeletal and soft-tissue features. Mouse
parent-of-origin experiments and human genetics make this a canonical model.

The report is not reliable as an exception-free causal graph. It omits a
directly relevant paternal-variant case with biochemical hormone resistance,
puts an STX16/PHP1B experiment inside the PPHP causal chain, overstates
complete-knockout skeletal models, and recommends invalid ontology mappings.
The right synthesis is strong support for the core model with explicit
exceptions and tissue/model qualifiers.

## What is supported

### The renal parent-of-origin effect is well established

Maternal, but not paternal, `Gnas` disruption caused PTH resistance and reduced
renal-cortical Gs-alpha in the foundational mouse model
([PMID:9671744](https://pubmed.ncbi.nlm.nih.gov/9671744/)). An exon-1-specific
model likewise found PTH and TSH resistance after maternal inheritance and
normal hormone responsiveness after paternal inheritance
([PMID:16099856](https://pubmed.ncbi.nlm.nih.gov/16099856/)). These experiments
avoid conflating Gs-alpha with all other transcripts at the complex locus.

Human segregation and mutation cohorts support the same group-level
distinction. They do not justify an absolute claim that a paternal variant can
never coexist with hormone resistance.

### Biallelic skeletal expression and a PTHrP/Gs-alpha axis are credible

Chimeric growth plates showed approximately half-normal Gs-alpha RNA and
modestly premature hypertrophy in heterozygous chondrocytes
([PMID:15459318](https://pubmed.ncbi.nlm.nih.gov/15459318/)). This is good
dosage-relevant support. It does not directly reproduce digit-selective human
brachydactyly, and it should not be conflated with complete conditional
deletion.

### XL-alpha-s is a plausible modifier

An engineered mouse allele supports effects of XL-alpha-s loss on growth, fat,
leptin, and bone
([PMID:22215617](https://pubmed.ncbi.nlm.nih.gov/22215617/)). Lower birth
weight reported with human exon 2–13 variants is compatible with that model
([PMID:25952723](https://pubmed.ncbi.nlm.nih.gov/25952723/)). The human
contribution has not been isolated from mutation-class and broader
locus-transcript effects, so “double hit” is a mechanistic lead rather than a
quantified explanation.

## Major corrections

### 1. “No hormone resistance” is too absolute

The report repeatedly turns the classical distinction into “NO hormone
resistance” and proposes a negative curation edge. A patient with a proven
paternal `GNAS` p.A109P variant had repeatedly elevated PTH and a blunted
growth-hormone stimulation response
([PMID:25464124](https://pubmed.ncbi.nlm.nih.gov/25464124/)). A separate
POH-overlap case developed mild PTH and TSH resistance during adolescence
([PMID:34254228](https://pubmed.ncbi.nlm.nih.gov/34254228/)).

These are rare exceptions and do not overturn the parent-of-origin model. They
do require “usually spares classic renal PTH resistance” and longitudinal
screening rather than a hard negative edge.

### 2. STX16-ICR is not a PPHP-specific upstream cause

The cited human-embryonic-stem-cell experiment studied why STX16-ICR
microdeletions have allele-specific effects on GNAS imprinting
([PMID:39910084](https://pubmed.ncbi.nlm.nih.gov/39910084/)). Those deletions
cause PHP1B when maternally inherited. A person with a paternal coding
loss-of-function variant does not acquire PPHP through an STX16 deletion.

This is valuable locus-level context, but calling it a filled causal-chain gap
and proposing it as an upstream PPHP node mixes two distinct etiologies.

### 3. The chondrocyte evidence is overstated

The report uses a chondrocyte-specific knockout as a direct link from
haploinsufficiency to brachydactyly. That experiment used complete
chondrocyte-specific deficiency, and its heterozygotes explicitly exhibited no
phenotype
([PMID:15765186](https://pubmed.ncbi.nlm.nih.gov/15765186/)). The separate
chimera study provides the better heterozygous evidence, but its effect was
modest and it did not explain fourth/fifth-digit selectivity.

### 4. Mixed GOF/LOF variants are outside the seed hypothesis

The report correctly describes receptor-specific variants with both
ligand-independent gain and ligand-dependent loss of signaling
([PMID:30312418](https://pubmed.ncbi.nlm.nih.gov/30312418/),
[PMID:40172207](https://pubmed.ncbi.nlm.nih.gov/40172207/),
[PMID:41530545](https://pubmed.ncbi.nlm.nih.gov/41530545/)). Those variants
broaden GNAS-associated disease and complicate variant interpretation. They do
not qualify a seed hypothesis explicitly restricted to coding
loss-of-function variants; they are a neighboring mechanism.

### 5. Obesity sparing is typical, not invariant

Parent-specific deletion in the mouse DMH strongly supports a mechanism for
maternal-variant obesity
([PMID:27991864](https://pubmed.ncbi.nlm.nih.gov/27991864/)). A 67-person AHO
cohort described PPHP as lacking **marked** obesity, not as proving universal
leanness
([PMID:29059381](https://pubmed.ncbi.nlm.nih.gov/29059381/)). The report’s
“typically not PPHP” wording is reasonable; its diagrammatic “NO obesity” is
not.

### 6. Several ontology leads are not usable

- `CL:1000838` is **kidney proximal convoluted tubule epithelial cell**, not a
  generic renal-proximal-tubule class.
- `CL:0000743` is **hypertrophic chondrocyte**, not “growth plate
  chondrocyte.”
- `GO:0019933` is obsolete **cAMP-mediated signaling**; the current specific
  term is `GO:0141156` **cAMP/PKA signal transduction**.
- `GO:0007224` currently labels **smoothened signaling pathway**, so the
  report should not present “Hedgehog signaling pathway” as its verbatim label.

### 7. The iPPSD subtype numbers are shifted

The report attributes PRKAR1A to iPPSD5 and PDE4D to iPPSD6. The cited
classification instead assigns PRKAR1A-related acrodysostosis type 1 to
**iPPSD4**, PDE4D-related acrodysostosis type 2 to **iPPSD5**, and
PDE3A-related hypertension with brachydactyly to **iPPSD6**
([PMID:29280743](https://pubmed.ncbi.nlm.nih.gov/29280743/)). The two
acrodysostosis genes remain relevant differential diagnoses, but the shifted
subtype labels should not be curated.

## Claim-level disposition

| Claim | Disposition | Reason |
| --- | --- | --- |
| Canonical paternal loss-of-function model | **Qualified** | Strongly supported, but the report needs exceptions and model qualifiers. |
| Renal parent-of-origin mouse evidence | **Retained** | Direct and well matched to the core renal mechanism. |
| PPHP means absolutely no hormone resistance | **Qualified** | Rare proven paternal-variant exceptions exist. |
| STX16-ICR fills the PPHP causal chain | **Rejected** | The experiment explains STX16-deletion PHP1B, not coding-variant PPHP. |
| Chondrocyte deletion directly proves heterozygous brachydactyly | **Qualified** | Complete knockout was severe; heterozygotes in that study had no phenotype. |
| PRKAR1A is iPPSD5 and PDE4D is iPPSD6 | **Rejected** | The cited classification assigns PRKAR1A = iPPSD4 and PDE4D = iPPSD5. |
| XL-alpha-s produces a human “double hit” | **Qualified** | Plausible mouse-supported modifier, not isolated in humans. |
| Mixed-function GNAS variants qualify a loss-of-function model | **Qualified** | Important neighboring mechanism but outside the seed’s stated scope. |
| PPHP has no obesity | **Qualified** | Marked obesity is typically spared; universal leanness is not established. |
| Candidate CL/GO mappings are ready for curation | **Rejected** | One CL label is too narrow, another is wrong, and the cAMP term is obsolete. |
| 54 papers were reproducibly reviewed | **Needs verification** | Only 30 PMIDs are exposed and a directly relevant case was missed. |

## Curation implications

- Retain the parent-of-origin model as canonical, with “usually spares classic
  renal PTH resistance.”
- Do not create invariant negative edges for hormone resistance or obesity.
- Keep STX16-ICR/PHP1B imprinting-establishment biology separate from the
  coding-variant PPHP causal path.
- Represent complete knockout, heterozygous chimera, mouse DMH, and human
  clinical evidence as distinct evidence levels.
- Treat XL-alpha-s and mixed-function variants as scoped modifier/neighboring
  mechanisms.
- Correct the ontology mappings before promotion.
- Assessment citations are review context only; they are not automatically
  disease-YAML evidence.

## Most discriminating next evidence

A prospective, molecularly confirmed paternal-`GNAS` cohort should combine
serial PTH/TSH/GHRH phenotyping with variant phase, exon class, body
composition, and allele-specific expression in patient-derived renal and
chondrocyte models. That design would test the frequency and timing of
exceptions while separating Gs-alpha haploinsufficiency from XL-alpha-s effects.
