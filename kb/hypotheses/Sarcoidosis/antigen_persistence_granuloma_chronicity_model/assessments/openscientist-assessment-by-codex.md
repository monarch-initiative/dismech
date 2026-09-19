# Antigen persistence / Th17.1 / mTORC1 report assessment

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `WEAKLY_SUPPORTED_UNRESOLVED`

## Executive judgment

The report is a useful causal map and gets its most important conclusion right:
the distinctive Th17.1-to-macrophage-mTORC1 edge remains unresolved. Its
`PARTIALLY_SUPPORTED` label is nevertheless too generous. The report joins
three different evidence classes:

1. observational Th17.1/Treg immunophenotyping in patients;
2. granuloma formation after engineered chronic mTORC1 activation in mice; and
3. clinical improvement after broad JAK inhibition.

Each makes a component of the model plausible. Together they still do not show
that persistent antigen drives Th17.1-derived cytokines, that those cytokines
activate macrophage-intrinsic mTORC1, or that this edge is necessary for human
granuloma persistence.

A 2026 mouse study is the closest partial bridge: anti-CXCR6 treatment reduced
Th17/Th17.1 abundance, was associated with lower downstream mTORC1 signaling,
and reduced granuloma and collagen deposition
([PMID:42143504](https://pubmed.ncbi.nlm.nih.gov/42143504/)). That result makes
the report's “nowhere directly demonstrated” wording too categorical, but it
does not close the gap. CXCR6 blockade alters cell recruitment and inflammatory
composition; the study does not establish
Th17.1-derived-IFN-gamma-to-macrophage-mTORC1 mediation.

The better overall classification is therefore **weakly supported and
unresolved**, with the hypothesis retained as `EMERGING`.

## What the report gets right

### It separates nodes from the defining edge

The report correctly observes that evidence for Th17.1 and evidence for mTORC1
largely arise from separate systems. That is the central causal-inference issue,
and it should remain an explicit knowledge gap rather than be hidden by a
module-level evidence count.

### It recognizes antigen identity as unresolved

Microbial and self-antigen candidates do not establish causal necessity for
chronicity. The statement that no single antigen has been shown necessary is
appropriately conservative.

### It does not force fibrosis into one pathway

The report treats fibrosis as only partly coupled to the proposed
Th17.1/mTORC1 circuit and considers parallel macrophage–fibroblast programs.
That avoids claiming that improvement in granulomatous inflammation must
prevent established fibrosis.

### Its highest-priority experiment targets the missing edge

Patient-derived Th17.1/macrophage co-culture with IFN-gamma neutralization and
mTORC1 readouts is directionally the right experiment. A decisive version
should include purified cell populations, cell-specific phospho-S6 and
phospho-4E-BP1 readouts, cytokine add-back, and orthogonal necessity and
sufficiency perturbations.

## Major qualifications

### 1. The report overlooks a partial bridge in a paper it cites

The report cites the CXCR6 study as evidence that Th17 blockade affects
granuloma and fibrosis, but its categorical literature-absence claim does not
account for the same study's reported association with downstream mTORC1
inhibition. The accurate synthesis is:

> A Th17/Th17.1 perturbation has been associated with lower mTORC1 signaling in
> a sarcoidosis-like mouse model, but macrophage-specific signaling and causal
> mediation have not been demonstrated.

That is stronger than “no bridge exists” and much weaker than validation of the
seed edge.

### 2. Engineered mTORC1 sufficiency is narrower than the report implies

TSC2 loss in macrophages or CD11c-positive cells produces granulomatous disease,
and mTOR inhibitors reverse disease in those models
([PMID:28092373](https://pubmed.ncbi.nlm.nih.gov/28092373/),
[PMID:37750561](https://pubmed.ncbi.nlm.nih.gov/37750561/)). Fsp1-Cre deletion
of `Tsc1` or `Tsc2` similarly supports an mTORC1–CCL24–CCR3 mechanism
([PMID:42246493](https://pubmed.ncbi.nlm.nih.gov/42246493/)).

These are strong sufficiency experiments for an engineered mouse state. They do
not establish the physiological upstream cause in sarcoidosis, and Fsp1-Cre is
not a macrophage-only perturbation. Human evidence is also heterogeneous:
phospho-S6 was found in 43% of one sarcoidosis cohort, in 31% of patients with
other granulomatous lung diseases, and had no detected association with
clinical phenotype
([PMID:34944053](https://pubmed.ncbi.nlm.nih.gov/34944053/)).

The source report also cites the preprint record
[PMID:40791394](https://pubmed.ncbi.nlm.nih.gov/40791394/) even though the
peer-reviewed article, PMID:42246493, was available before the report date.

### 3. Th17.1 is supported as an activity/endotype correlate

Treatment-naive lymph-node and BAL data associate higher Th17.1 proportions
with chronic rather than resolving disease
([PMID:29449421](https://pubmed.ncbi.nlm.nih.gov/29449421/)). A later
exploratory study found activated Th17.1 enrichment, lower lung Treg
proportions, corticosteroid-associated decline, and an association with
progression in corticosteroid-responsive pulmonary disease
([PMID:42286635](https://pubmed.ncbi.nlm.nih.gov/42286635/)).

This supports a biomarker or endotype claim. It does not by itself establish
that Th17.1 is the causal driver of chronicity or the upstream activator of
macrophage mTORC1.

### 4. Tofacitinib response does not prove causal necessity

The report states:

> “This proves the effector cytokine circuit is causally required to sustain
> granulomas.”

The cited primary human evidence is an uncontrolled series of eight refractory
cardiac-sarcoidosis patients; seven improved by repeat PET/CT
([PMID:41916671](https://pubmed.ncbi.nlm.nih.gov/41916671/)). This is an
important clinical signal, but tofacitinib affects multiple JAK-dependent
cytokine pathways, the series lacks a randomized counterfactual, and the result
does not isolate Th17.1, IFN-gamma, or mTORC1. The paper itself calls for larger
prospective cohorts.

The defensible statement is that JAK inhibition is a promising perturbation of
the inflammatory network, not proof that the report's proposed circuit is
causally necessary.

### 5. HLA association is converted into deterministic clearance

HLA-DRB1 alleles associate with susceptibility and disease course, and peptide
binding analyses provide biologically plausible leads
([PMID:19382529](https://pubmed.ncbi.nlm.nih.gov/19382529/),
[PMID:25506722](https://pubmed.ncbi.nlm.nih.gov/25506722/)). They do not
identify the causal antigen, measure antigen clearance, or establish that HLA
determines whether the antigen persists. The report's deterministic
“recognized/cleared versus persists” language should be replaced by an
association-plus-mechanistic-hypothesis formulation.

### 6. Cardiac scope is less supported than pulmonary scope

The direct longitudinal Th17.1 evidence is pulmonary. The cardiac case rests
mainly on an engineered mouse model, descriptive tissue work, and the
eight-patient tofacitinib series. Those data justify testing the mechanism in
cardiac disease, but not yet defining a single chronic pulmonary-and-cardiac
mechanistic subtype.

## Claim-level disposition

| Claim | Disposition | Reason |
| --- | --- | --- |
| The Th17.1-to-macrophage-mTORC1 edge is nowhere demonstrated | **Qualified** | PMID:42143504 is a partial, non-cell-specific bridge; direct mediation remains absent. |
| Mouse knockout plus rescue proves mTORC1 sufficiency | **Qualified** | Strong for engineered mouse granulomas, not the physiological human upstream mechanism. |
| Activated Th17.1 reflects activity/progression | **Qualified** | Supported as an observational pulmonary biomarker/endotype. |
| JAK response proves effector-circuit necessity | **Rejected** | Small uncontrolled series and broad pathway inhibition cannot identify the necessary edge. |
| HLA determines antigen recognition/clearance and chronicity | **Rejected** | Association and in-silico binding do not establish deterministic clearance. |
| No antigen is proven necessary for chronicity | **Retained** | Candidate detection and sensitization have not established necessity. |
| Best fit includes chronic pulmonary and cardiac disease | **Qualified** | Pulmonary evidence is stronger; cardiac generalization remains a lead. |

## Curation implications

- Keep the hypothesis `EMERGING`.
- Do not curate `Th17.1/IFN-gamma → macrophage mTORC1` as a supported causal
  edge.
- Curate Th17.1 enrichment and mTORC1 activation as separately supported,
  scope-bounded modules when exact primary evidence is available.
- Treat mTORC1 as heterogeneous in human granulomatous disease, not as a
  universal sarcoidosis state.
- Treat JAK-inhibitor response as therapeutic evidence and a mechanistic lead,
  not as identification of the report's causal mediator.
- Keep the persistent antigen and direct Th17.1-to-mTORC1 mediation as explicit
  knowledge gaps.

## Most discriminating next evidence

A useful bridge experiment would combine patient-derived antigen-responsive
Th17.1 cells with sorted sarcoidosis alveolar macrophages and test:

1. whether Th17.1 contact or conditioned medium increases
   macrophage-specific phospho-S6, phospho-4E-BP1, and mTORC1 transcriptional
   targets;
2. whether IFN-gamma neutralization or receptor disruption prevents that
   response;
3. whether cytokine add-back is sufficient;
4. whether macrophage-selective mTORC1 inhibition interrupts granuloma-like
   organization without simply depleting the T-cell population; and
5. whether the same directional coupling appears in spatially resolved human
   tissue and predicts longitudinal persistence.

That design would test the defining edge rather than add another correlation
between two active inflammatory modules.
