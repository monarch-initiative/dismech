# Environmental exposure × host susceptibility report assessment

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `WEAKLY_SUPPORTED_UNRESOLVED`

## Executive judgment

The report's causal decomposition is stronger than its headline verdict. It
correctly distinguishes:

1. established host-genetic associations;
2. modest environmental and occupational associations;
3. exploratory statistical gene–environment interactions; and
4. the unproven exposure-specific sensor/antigen-presentation mechanism.

That separation leads to a sound curation guardrail: no exposure-specific
causal trigger edge should be promoted. The report nevertheless labels the
whole model `PARTIALLY_SUPPORTED`, even though the defining idiopathic chain—

> exposure-specific trigger × genotype → innate sensing or antigen presentation
> → CD4 polarization → sarcoidosis

—has not been directly demonstrated.

The report also misses two relevant human gene–environment analyses, converts a
single beryllium study's main-effect findings into an invalid general
“interaction-only” rule, overinterprets post-diagnosis antigen sensitization,
and proposes the immunologically incorrect term “type II hypersensitivity to
metals.”

The distinctive mechanism is best classified as **weakly supported and
unresolved**, while the hypothesis remains a useful `EMERGING` framework.

## What the report gets right

### It preserves the association/causation boundary

The report does not treat the ACCESS odds ratios as identified antigens or
causal exposures. ACCESS found modest associations with agricultural
employment, occupational insecticide exposure, and mold/mildew work
environments, while explicitly finding no single predominant cause
([PMID:15347561](https://pubmed.ncbi.nlm.nih.gov/15347561/)).

### It separates host susceptibility from the missing trigger mechanism

Multi-ancestry GWAS evidence supports HLA-region, BTNL2, ANXA11, NOTCH4, and
other susceptibility loci
([PMID:22952805](https://pubmed.ncbi.nlm.nih.gov/22952805/)). Those associations
make genetically modified responses plausible but do not identify the relevant
exposure or establish a gene–environment mechanism. The report generally keeps
that distinction visible.

### It uses chronic beryllium disease as an analogue, not as idiopathic
sarcoidosis

The report explicitly notes that CBD has a known exposure and a specific HLA
restriction and therefore validates a template, not its generalization. That is
the right starting caveat.

### Its final curation recommendation is appropriate

“Do not curate any exposure-specific trigger edge as causal yet” is the
assessment's most important retained conclusion.

## Major qualifications

### 1. The gene–environment literature search is incomplete

The report describes ACCESS as “the one direct human gene-environment
interaction analysis.” At least two relevant primary studies published in 2019
were missed:

- A Swedish population-based case-control study of 3,713 individuals reported
  smoking interactions with multiple loci, with leading signals in `FCRL1` for
  Löfgren syndrome and `IL23R` for non-Löfgren disease
  ([PMID:31819081](https://pubmed.ncbi.nlm.nih.gov/31819081/)).
- A gene-environment-wide analysis of 1,877 African Americans identified
  suggestive insecticide interactions using methods that account for ancestry
  and relatedness
  ([PMID:30793815](https://pubmed.ncbi.nlm.nih.gov/30793815/)).

These studies do **not** replicate the exact ACCESS
HLA-DRB1*11–insecticide/mold result, prove that the statistical interactions are
biological, or identify an exposure-specific sensor. The report's central
mechanistic uncertainty remains. But “one direct analysis” and a broadly
“unreplicated G×E literature” are inaccurate descriptions of the evidence base.

A corrected synthesis would distinguish:

- exact replication of the ACCESS exposure–HLA pairs: **not established**;
- other sarcoidosis G×E findings: **present but exploratory**; and
- a mechanistic exposure–sensor–presentation–CD4 chain: **not established**.

### 2. CBD demonstrates plausibility, not support for an idiopathic edge

CBD offers an unusually complete example: beryllium exposure, HLA-DP
susceptibility, beryllium-modified self peptides, beryllium-specific CD4 T
cells, and granulomatous inflammation
([PMID:24912188](https://pubmed.ncbi.nlm.nih.gov/24912188/),
[PMID:33630763](https://pubmed.ncbi.nlm.nih.gov/33630763/)).

That validates the biological possibility of the **model class**. It does not
raise support for a particular idiopathic sarcoidosis trigger above
plausibility. CBD is etiologically distinct and can be distinguished by
beryllium-specific lymphocyte responses even though histopathology and clinical
presentation can overlap.

The CBD evidence should therefore be labeled **analogue/paradigm evidence**, not
partial evidence for the unidentified idiopathic edge.

### 3. The “model only survives as an interaction” inference is invalid

The report reasons from null beryllium and HLA-DPB1 Glu69 main effects to the
claim that the model only survives as a genuine interaction. The primary paper
does not support that generalization
([PMID:25305207](https://pubmed.ncbi.nlm.nih.gov/25305207/)):

- it addresses one exposure and one susceptibility marker, not the broader
  environmental model;
- it reports a significant exposure-duration-by-Glu69 interaction in a subgroup;
  and
- it interprets the result as evidence that some community diagnoses may
  actually represent occupational beryllium disease.

The paper is primarily a differential-diagnosis, exposure-history, and
misclassification constraint. Null main effects neither prove an interaction
mechanism nor imply that all other versions of the seed model are
interaction-only.

### 4. Inorganic sensitization does not establish a modifier edge

In one cohort, 27.6% of the tested sarcoidosis subgroup versus 4.2% of controls
had an ELISPOT response to metals or silica, and sensitized patients were more
likely to have radiographic fibrosis five years after diagnosis
([PMID:32941653](https://pubmed.ncbi.nlm.nih.gov/32941653/)).

This is a useful phenotype-stratification lead. It does not establish verified
past exposure, show that sensitization preceded disease, identify a genotype
interaction, or demonstrate that the response caused fibrosis. The report's
arrow notation—

> inorganic sensitization → fibrotic phenotype

—should be replaced by an association symbol or explicit observational wording.

### 5. “Type II hypersensitivity to metals” encodes the wrong mechanism

Type II hypersensitivity is antibody-mediated cytotoxicity. The beryllium
mechanism cited by the report is MHC class II-restricted, beryllium-specific CD4
T-cell immunity: a delayed cell-mediated response conventionally classified as
type IV hypersensitivity. The candidate ontology term should not be curated.

### 6. The controlled-human-exposure heading should be removed

The experiment body largely describes an ex-vivo challenge of BAL cells or lung
organoids from HLA- and exposure-stratified patients. That is potentially
informative. The heading also says “controlled human exposure,” which is not an
acceptable design for silica, pesticides, mold mixtures, or an unresolved
suspected trigger.

The proposed work should be split into:

1. prospective observation with independently measured naturally occurring
   exposures; and
2. matched-versus-mismatched **ex-vivo** challenge under controlled laboratory
   conditions.

## Claim-level disposition

| Claim | Disposition | Reason |
| --- | --- | --- |
| Host genetics predisposes to disease and shapes phenotype | **Retained** | Strong association evidence; does not identify a trigger. |
| Inhaled exposure classes associate with pulmonary risk | **Qualified** | Modest observational associations, not causal antigens or pathways. |
| ACCESS is the one direct human G×E analysis | **Rejected** | PMID:31819081 and PMID:30793815 were missed. |
| CBD proves the model class is biologically real | **Qualified** | Strong analogue for a distinct exposure-defined disease, not direct idiopathic evidence. |
| The model survives only as a genuine interaction | **Rejected** | Overgeneralizes one CBD-focused study and misreads its role. |
| The defining idiopathic sensor × genotype edge is unproven | **Retained** | Statistical interactions do not establish the biological chain. |
| Inorganic sensitization leads to fibrosis | **Qualified** | Post-diagnosis association without temporality or causal perturbation. |
| Type II hypersensitivity to metals | **Rejected** | The cited T-cell mechanism is type IV, not antibody-mediated type II. |
| Controlled human exposure / ex-vivo challenge | **Qualified** | Retain ex-vivo work; remove deliberate hazardous exposure. |
| Do not curate a causal exposure-specific trigger edge | **Retained** | Correct guardrail for the present evidence. |

## Curation implications

- Keep the hypothesis `EMERGING`.
- Preserve exposure findings as observational risk associations with explicit
  confounding and measurement caveats.
- Record sarcoidosis G×E findings as exploratory, and distinguish non-replication
  of a specific pair from absence of all other G×E analyses.
- Use CBD only as an exposure-defined mechanistic analogue and diagnostic
  comparator.
- Do not encode post-diagnosis sensitization as a directional
  exposure-to-fibrosis edge.
- Do not add a shared exposure sensor or causal antigen-presentation edge until
  a specific exposure, genotype, molecular presentation event, and CD4 response
  are connected in idiopathic disease.
- Replace the type-II-hypersensitivity candidate with an accurately scoped
  cell-mediated process only if the ontology term is verified.

## Most discriminating next evidence

A credible test needs exposure measurement, replication, and mechanism in that
order:

1. preregister an exposure–genotype pair and replicate it in independent,
   phenotype-stratified cohorts using objective exposure measures where
   possible;
2. show that the matched exposure produces a genotype-dependent response in
   patient-derived antigen-presenting cells or organoids, with mismatched
   exposure and allele pairs as negative controls;
3. identify the presented ligand or sensor-dependent intermediate;
4. demonstrate exposure-specific CD4 clonotype expansion or polarization; and
5. perturb the sensor, presentation molecule, or candidate ligand to abolish
   the response.

Without that sequence, additional associations will refine exposure
prioritization but will not establish the report's distinctive mechanism.
