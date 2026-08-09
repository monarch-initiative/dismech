# Autoimmune receptor-antibody report assessment

- **Provider:** OpenScientist
- **Assessor:** Codex
- **Source:** `../openscientist.md`
- **Overall verdict:** `PARTIALLY_SUPPORTED`

## Executive judgment

The report finds a genuine but unconfirmed mechanism class. Three kinds of
evidence matter:

1. selected receptor peptides can induce functionally active antibodies and a
   POTS-like tilt phenotype in rabbits;
2. POTS IgG can modulate adrenergic, muscarinic, or AT1R signaling in
   receptor-transfected cells; and
3. clinical cohorts contain autoimmune context and occasional assay-specific
   receptor signals.

That is enough for **partial support of biological plausibility**. It is not
enough to establish a receptor-antibody-defined human POTS subtype or to show
that naturally occurring patient antibodies cause orthostatic tachycardia.

The report appropriately identifies the largest negative ELISA study, the
single-group concentration of functional-assay evidence, absent patient-IgG
passive transfer, and the negative small iSTAND IVIG trial. Its headline is
therefore defensible only with a much narrower interpretation than the report
sometimes gives it.

## What the report gets right

### The standard-ELISA result is a serious constraint

[PMID:35766055](https://pubmed.ncbi.nlm.nih.gov/35766055/) tested 116 patients
and 81 controls across 11 adrenergic, muscarinic, angiotensin-II, and endothelin
targets. No concentration or manufacturer-threshold comparison separated the
groups, and ROC performance was poor. The report correctly does not treat the
commercial ELISA as a clinical diagnostic.

### Human functional activity is a lead, not settled replication

The alpha-1/beta-1 study
([PMID:32743496](https://pubmed.ncbi.nlm.nih.gov/32743496/)), the ten-patient
M2R study ([PMID:34409582](https://pubmed.ncbi.nlm.nih.gov/34409582/)), and the
17-patient AT1R study
([PMID:29618472](https://pubmed.ncbi.nlm.nih.gov/29618472/)) report
receptor-specific in-vitro effects. They also share the Yu/Kem assay lineage.
The report is right that an independent, blinded, multi-platform replication is
still missing.

### The causal experiment gap is correctly prioritized

Active peptide immunization is not passive transfer of patient IgG. The report
correctly asks for patient-IgG transfer, antigen-specific depletion and add-back,
and longitudinal antibody measurements.

## Major corrections

### 1. The rabbit studies are not independent replications

The report says the mechanism is supported by “three independent rabbit
immunization studies.” The alpha/beta, repeat alpha/beta, and M2R experiments
([PMID:31547749](https://pubmed.ncbi.nlm.nih.gov/31547749/),
[PMID:36873318](https://pubmed.ncbi.nlm.nih.gov/36873318/), and
[PMID:35118574](https://pubmed.ncbi.nlm.nih.gov/35118574/)) come from the same
University of Oklahoma program, have heavily overlapping authors, and use only
8, 6, and 5 rabbits. The second study explicitly says it confirms the group's
previous report.

These studies show that deliberately induced antibodies can perturb the chosen
receptors in this model. They are neither independent-laboratory replication
nor evidence that naturally arising POTS antibodies reproduce the effect.

### 2. AT1R is promising, not consistently elevated

A small functional study found AT1R activity in 12 of 17 patients, and a later
ELISA cohort of 19 patients and 22 controls found higher mean AT1R levels
([PMID:29618472](https://pubmed.ncbi.nlm.nih.gov/29618472/),
[PMID:40432440](https://pubmed.ncbi.nlm.nih.gov/40432440/)). The larger
116-patient ELISA study included angiotensin-II receptors and found no
difference. “Most consistently elevated across assay platforms” is therefore
not supported.

The systemic-sclerosis comparison does not repair this inconsistency.
[PMID:34956217](https://pubmed.ncbi.nlm.nih.gov/34956217/) shows that
functional and ELISA assays can disagree in another disease, but its functional
AT1R activity was nonspecific and did not correlate with manifestations. It is
a methodological warning, not independent validation of the POTS assay.

### 3. The RAAS edge remains inferred

The renin-aldosterone study
([PMID:15781744](https://pubmed.ncbi.nlm.nih.gov/15781744/)) and AT1R
cell-assay study are in different cohorts. Together they motivate a testable
model—an inhibitory antibody could impair a compensatory Ang-II response—but no
study has shown antibody-linked aldosterone suppression in vivo. “Compelling
mechanistic bridge” should be replaced by “plausible untested bridge.”

### 4. The EBV study does not supply the missing POTS trigger

[PMID:41050647](https://pubmed.ncbi.nlm.nih.gov/41050647/) is an exploratory
study in post-COVID syndrome and ME/CFS, not a POTS cohort. It reports
autoantibody reactivity and symptom correlations; it does not demonstrate that
EBV initiated POTS or that cross-reactive receptor clones caused orthostatic
physiology. It is external plausibility only.

### 5. The randomized evidence needs balanced framing

iSTAND found no benefit of IVIG over albumin in 30 treated participants
([PMID:38311655](https://pubmed.ncbi.nlm.nih.gov/38311655/)). That is important
negative treatment evidence, but the cohort was selected by clinical autoimmune
features rather than a validated receptor-antibody assay, and albumin controlled
for volume expansion. It does not directly test one antibody target.

The report also omits a relevant 2024 sham-controlled tVNS trial
([PMID:37999672](https://pubmed.ncbi.nlm.nih.gov/37999672/)). In 26 women, active
tVNS reduced the postural heart-rate increment and antiadrenergic activity
relative to sham. The trial is small, comes from the same receptor-antibody
research program, and does not establish mediation, but it belongs in the
therapeutic evidence balance.

### 6. A 30–50% antibody subtype has not been measured

Assay-specific positivity rates cannot be combined into one prevalence:
receptors overlap, thresholds differ, and the largest ELISA study showed no
discrimination. The report's 30–50% estimate is unsupported.

### 7. Two ontology leads are wrong

- `MONDO:0017360` is vitamin B12-unresponsive methylmalonic acidemia type mut0,
  not POTS. This repository uses `MONDO:0011479`.
- `CL:0000003` is obsolete native cell, not a dorsal-root-ganglion neuron.

Neither candidate may be promoted.

## Curation implication

Keep `autoimmune_receptor_model` as an alternative mechanism and keep causal
status open. The disease entry may represent:

- negative standard-ELISA discrimination;
- small, single-network functional-assay signals;
- an inferred AT1R–RAAS connection; and
- the need for patient-IgG transfer and independent assay replication.

Do not encode a 30–50% antibody-defined subtype, an EBV-to-POTS causal edge, or
the report's invalid ontology mappings. No disease YAML or reference cache was
changed in this assessment-only PR.

## Most discriminating next evidence

The highest-value design is a blinded, preregistered multi-center study that
tests the same incident POTS and control samples on at least two independent
functional platforms, followed by affinity depletion/add-back and passive
transfer of assay-positive patient IgG. Clinical association should be tested
prospectively against orthostatic hemodynamics and treatment response rather
than inferred from cross-sectional positivity.
