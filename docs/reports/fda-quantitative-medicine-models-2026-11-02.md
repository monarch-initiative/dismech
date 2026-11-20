# FDA quantitative medicine models

FDA defines quantitative medicine as follows
([Federal Register 2026-15887](https://public-inspection.federalregister.gov/2026-15887.pdf)):

> Quantitative medicine approaches integrate mathematical and computational models with
> biological, clinical, and statistical data to inform drug development, regulatory, and clinical
> decisions.

FDA does not publish a catalog of the quantitative medicine models it has accepted or relied on.
The closest list is CDER's
[Fit-for-Purpose table](https://www.fda.gov/drugs/development-approval-process-drugs/drug-development-tools-fit-purpose-initiative)
(current as of 10 January 2025), which holds four tools, three of them statistical methods. The
CDER Quantitative Medicine Center of Excellence's
[Progress and Priorities Update](https://www.fda.gov/media/188999/download) (October 2025) says
the Center "aims to develop knowledge management resources to catalog past and current QM related
regulatory interactions", and that commenters on an earlier FDA request asked for "improved
understanding of regulatory precedence with examples".

This report records nine models in two groups:

- **Models FDA has acted on in a specific decision**, plus one academic benchmark without FDA
  standing (five models).
- **The four Fit-for-Purpose tools.**

For each model it records what DisMech holds and where the model belongs. It also records the
validation and regulatory properties that the DisMech schema has no slot for today. Curation of
the models into `kb/` is tracked in
[dismech#16321](https://github.com/monarch-initiative/dismech/issues/16321).

## How to read the ratings

**Validation ladder.** Each level presumes the ones before it. The scores are this report's
reading of the published record, not an FDA qualification.

| Level | Meaning |
|---|---|
| 0 | Context of use stated: question, decision, population, acceptable performance |
| 1 | Reproducible: code and parameters available, result can be regenerated |
| 2 | Biologically valid: outputs match independent human data for the step it represents |
| 3 | Intervention response: drug or genetic perturbations move outputs as seen clinically |
| 4 | Prospective prediction: an outcome was predicted before it was observed and acted on |

**FDA-side strength** rates only the FDA-side record, not the model:

| Rating | Meaning |
|---|---|
| Strong | FDA's own published words |
| Moderate | An FDA-hosted document written by the sponsor |
| Developer-reported | No FDA document found; acceptance is reported by the developers |
| None | FDA has not acted on the model |

Ladder marks: ● met, ◐ partly met, ○ not met, ? not determined.

Where level 1 is `?` (code or parameters not public, or reproducibility not checked), the marks
for levels 2–4 record this report's reading of the published evidence for each level on its own.
They are not met in the cumulative sense until level 1 is determined.

## Summary

| Model | Type | Ladder 0·1·2·3·4 | FDA status | FDA-side strength | DisMech target | In DisMech |
|---|---|---|---|---|---|---|
| Pembrolizumab every-6-weeks PK and exposure–response | Population PK, exposure–response | ●?●●● | Basis of 2020 dosing approval | Strong | `Cutaneous_Melanoma` | No |
| CiPA in silico torsade model | Cardiac electrophysiology (modified O'Hara-Rudy) | ●●●●◐ | Developed largely in FDA labs; advisory committee endorsed the approach in 2017 | Strong | `Long_QT_Syndrome` | Yes, partly |
| Ibrutinib PBPK | Physiologically based pharmacokinetic | ●?●●◐ | Informed drug–drug interaction labeling | Moderate | `Chronic_Lymphocytic_Leukemia` | No |
| UVA/Padova type 1 diabetes simulator | Glucose–insulin physiology, virtual population | ●?●●◐ | Reported accepted in place of animal studies (2008) | Developer-reported | `Type_I_Diabetes` | No |
| Populations of human cardiac models | Cardiac electrophysiology, model population | ●?●●◐ | None | None | `Long_QT_Syndrome` | No |
| CAMD Alzheimer's disease progression model | Disease progression (placebo, drop-out) | not scored | Fit-for-Purpose, 12 Jun 2013 | Strong | `Alzheimer_Disease` | No |
| MCP-Mod | Dose-finding statistical method | not scored | Fit-for-Purpose, 26 May 2016 | Strong | None | Not applicable |
| BOIN design | Dose-finding statistical method | not scored | Fit-for-Purpose, 10 Dec 2021 | Strong | None | Not applicable |
| Empirically based Bayesian Emax models | Dose-finding statistical method | not scored | Fit-for-Purpose, 5 Aug 2022 | Strong | None | Not applicable |

The four Fit-for-Purpose tools are rated Strong because FDA lists them on its own page. Their
ladder levels were not scored for this report.

## Models FDA has acted on

### Pembrolizumab every-6-weeks dosing

- **Type:** Population pharmacokinetic and exposure–response models.
- **Developer:** Merck.
- **Context of use:** Whether 400 mg every 6 weeks gives exposures comparable to the approved
  regimens, across all adult indications.
- **Data integrated:** The model predicted exposures for 400 mg every 6 weeks. These were compared
  with observed exposures under 2 mg/kg every 3 weeks, 200 mg every 3 weeks and 10 mg/kg every
  2 weeks, supported by exposure–response analyses across the development program. Interim
  pharmacokinetics and response came from KEYNOTE-555 cohort B, in melanoma.
- **Validation:** ●?●●●. Interim KEYNOTE-555 data checked the predicted exposures; FDA reported an
  overall response rate of 39% (95% CI 24–55) in the first 44 patients.
- **Reproducibility:** Not checked.
- **FDA status:** Accelerated approval of the new schedule on 28 April 2020. Continued approval may
  depend on a confirmatory trial.
- **FDA-side document:**
  [FDA approves new dosing regimen for pembrolizumab](https://www.fda.gov/drugs/drug-approvals-and-databases/fda-approves-new-dosing-regimen-pembrolizumab).
  Strength: Strong.
- **DisMech:** Not present. Pembrolizumab is mentioned in 66 entries; `Cutaneous_Melanoma` is the
  proposed home because the confirming cohort was melanoma. This is a model of a drug, not a
  disease mechanism; see the open question in dismech#16321.
- **References:** Lala et al., Eur J Cancer 2020,
  [PMID:32305010](https://pubmed.ncbi.nlm.nih.gov/32305010/); KEYNOTE-555 cohort B, PLoS One 2024,
  [PMID:39531423](https://pubmed.ncbi.nlm.nih.gov/39531423/).

### CiPA in silico torsade model

- **Type:** Human ventricular cardiomyocyte electrophysiology model, a modified O'Hara-Rudy model
  with dynamic hERG (IKr) drug binding.
- **Developer:** FDA, within the Comprehensive in vitro Proarrhythmia Assay (CiPA) initiative.
- **Context of use:** Classify a drug's torsade de pointes risk from in vitro ion-channel data.
- **Data integrated:** In vitro block data for several cardiac ion channels are the model input.
  Outputs are compared with reference drugs of known clinical risk. FDA's page also describes
  checks against human stem-cell cardiomyocyte assays and phase 1 ECG biomarkers.
- **Validation:** ●●●●◐. Trained on 12 reference drugs and assessed on further drugs of known
  risk. As with the populations-of-models benchmark below, that assessment is retrospective on
  compounds whose clinical risk was already known, so level 4 is partly met.
- **Reproducibility:** Code at [github.com/FDA/CiPA](https://github.com/FDA/CiPA).
- **FDA status:** An FDA advisory committee endorsed the approach in March 2017, pending ongoing
  validation studies.
- **FDA-side document:**
  [Developing a mechanistic model-based approach to assess cardiac safety of new drugs](https://www.fda.gov/science-research/about-science-research-fda/developing-mechanistic-model-based-approach-assess-cardiac-safety-new-drugs).
  Strength: Strong. The page dates from 2017, so the current regulatory status should be checked
  against the ICH E14/S7B Q&A.
- **DisMech:** On `Long_QT_Syndrome` as three models: the original O'Hara-Rudy model
  (PMID:21637795, CellML), the "CiPA IKr-Dynamic ORd Proarrhythmia Model" (PMID:28878692) and
  ToR-ORd (PMID:31868580). None of their mechanism links records relationship, fidelity,
  limitations or model scale, and neither validation paper is cited.
- **References:** Dutta et al., Front Physiol 2017,
  [PMID:28878692](https://pubmed.ncbi.nlm.nih.gov/28878692/); Li et al., Clin Pharmacol Ther 2019,
  [PMID:30151907](https://pubmed.ncbi.nlm.nih.gov/30151907/); Li et al., Clin Pharmacol Ther 2020,
  [PMID:31709525](https://pubmed.ncbi.nlm.nih.gov/31709525/).

### Ibrutinib PBPK

- **Type:** Physiologically based pharmacokinetic model.
- **Developer:** Janssen, built in the Simcyp simulator.
- **Context of use:** Predict ibrutinib exposure with CYP3A4 inhibitors and inducers, to set dose
  adjustments for co-medications.
- **Data integrated:** Built from in vitro data. Verified against clinical studies of a strong
  CYP3A4 inhibitor and a strong inducer.
- **Validation:** ●?●●◐. Predictions for unstudied interactions were used on the label, but those
  were not then confirmed by observation. The hepatic-impairment prediction overestimated exposure
  against interim clinical data, and a clinical hepatic-impairment study was still required.
- **Reproducibility:** Not checked; Simcyp is commercial software.
- **FDA status:** Secondary sources report that 24 drug–drug interaction and dosing claims on the
  2013 label came from model predictions without clinical studies. The FDA review on Drugs@FDA has
  not been checked against that figure.
- **FDA-side document:**
  [FDA-hosted sponsor slides on post-approval MIDD for ibrutinib](https://fda.gov/media/112937/download).
  Strength: Moderate.
- **DisMech:** Not present. Ibrutinib is mentioned in 6 entries; `Chronic_Lymphocytic_Leukemia` is
  the proposed home. This is a model of a drug, not a disease mechanism.
- **References:** de Zwart et al., Clin Pharmacol Ther 2016,
  [PMID:27367453](https://pubmed.ncbi.nlm.nih.gov/27367453/); survey of PBPK in NDA reviews,
  [PMC5414891](https://pmc.ncbi.nlm.nih.gov/articles/PMC5414891).

### UVA/Padova type 1 diabetes simulator

- **Type:** Glucose–insulin physiology model with a population of virtual subjects.
- **Developer:** University of Virginia and University of Padova.
- **Context of use:** Preclinical testing of insulin-dosing strategies and closed-loop
  (artificial pancreas) control algorithms.
- **Data integrated:** Meal-test data from people with and without diabetes calibrate the model.
  Later versions added hypoglycemia counter-regulation (S2013) and single-day scenarios (S2017).
- **Validation:** ●?●●◐. Used to screen control algorithms before human trials; prospective
  agreement with trial outcomes is reported by the developers but not assessed here.
- **Reproducibility:** Distributed commercially as T1DMS by The Epsilon Group; source not public.
- **FDA status:** The developers report that FDA accepted the simulator in January 2008 as a
  substitute for animal trials in preclinical testing, through a master file that is not public.
  A 2020 preprint reports that FDA evaluated 140 candidate algorithms with it, leading to 16
  investigational device exemptions.
- **FDA-side document:** None found. Strength: Developer-reported.
- **DisMech:** Not present. `Type_I_Diabetes` (MONDO:0005147, type 1 diabetes mellitus) exists and
  has no `computational_models` block, so it is the proposed home. Type 1 diabetes also appears as
  a subtype inside `Diabetes_Mellitus`, and stubs exist for monogenic and susceptibility subtypes
  such as `Type_1_Diabetes_Mellitus_2`.
- **References:** Dalla Man et al., IEEE Trans Biomed Eng 2007,
  [PMID:17926672](https://pubmed.ncbi.nlm.nih.gov/17926672/); Dalla Man et al., J Diabetes Sci
  Technol 2014, [PMID:24876534](https://pubmed.ncbi.nlm.nih.gov/24876534/); Visentin et al., J
  Diabetes Sci Technol 2023, [PMID:37743740](https://pubmed.ncbi.nlm.nih.gov/37743740/).

### Populations of human cardiac models (academic benchmark)

- **Type:** Population of 1,213 human ventricular action-potential models.
- **Developer:** University of Oxford.
- **Context of use:** Predict clinical pro-arrhythmic risk of drugs.
- **Data integrated:** Models calibrated to human recordings; in silico trials of 62 reference
  compounds at several concentrations, compared with known clinical risk.
- **Validation:** ●?●●◐. 89% accuracy against clinical risk; the NC3Rs reports up to 75% for animal
  studies on similar data sets. The benchmark is retrospective on known compounds.
- **Reproducibility:** Not checked.
- **FDA status:** None. Recognized by the UK NC3Rs with the 2017 International 3Rs Prize.
- **FDA-side document:** None. Strength: None.
- **DisMech:** Not present. Proposed home `Long_QT_Syndrome`, next to the CiPA models.
- **References:** Passini et al., Front Physiol 2017,
  [PMID:28955244](https://pubmed.ncbi.nlm.nih.gov/28955244/);
  [NC3Rs announcement](https://nc3rs.org.uk/news/international-3rs-prize-awarded-computer-modelling-predicts-human-cardiac-safety-better-animal).

## Fit-for-Purpose tools

FDA designates a tool fit-for-purpose when formal qualification is not available, "based on the
acceptance of the proposed tool following a thorough evaluation". Each row on FDA's table links a
determination letter.

### CAMD Alzheimer's disease placebo/disease progression model

- **Type:** Disease progression model of cognitive decline (ADAS-cog) with placebo, demographic and
  drop-out components, for clinical trial simulation.
- **Submitter:** Coalition Against Major Diseases (CAMD), Critical Path Institute.
- **Context of use:** Simulating mild-to-moderate Alzheimer's disease trials for design decisions.
- **Data integrated:** Patient-level data from trials and the Alzheimer's Disease Neuroimaging
  Initiative, combined with summary-level literature data in a beta-regression meta-analysis.
- **Validation:** Not scored for this report.
- **Reproducibility:** Not checked.
- **FDA status:** Fit-for-Purpose, issued 12 June 2013. The EMA later qualified the same tool.
- **FDA-side document:** FDA Fit-for-Purpose table. Strength: Strong.
- **DisMech:** Not present. `Alzheimer_Disease` carries only the DADD digital twin.
- **References:** Rogers et al., J Pharmacokinet Pharmacodyn 2012,
  [PMID:22821139](https://pubmed.ncbi.nlm.nih.gov/22821139/); Romero et al., Clin Pharmacol Ther
  2015, [PMID:25669145](https://pubmed.ncbi.nlm.nih.gov/25669145/).

### MCP-Mod

- **Type:** Statistical method for phase II dose finding under model uncertainty. It tests for a
  dose–response signal, then fits candidate models to estimate target doses.
- **Submitter:** Janssen and Novartis.
- **FDA status:** Fit-for-Purpose, issued 26 May 2016. Strength: Strong.
- **DisMech:** No disease home; recorded here only.
- **References:** Bretz et al., Biometrics 2005,
  [PMID:16135025](https://pubmed.ncbi.nlm.nih.gov/16135025/).

### Bayesian optimal interval (BOIN) design

- **Type:** Statistical design for phase I dose escalation.
- **Submitter:** Ying Yuan, MD Anderson Cancer Center.
- **FDA status:** Fit-for-Purpose, issued 10 December 2021. Strength: Strong.
- **DisMech:** No disease home; recorded here only.
- **References:** Yuan et al., Clin Cancer Res 2016,
  [PMID:27407096](https://pubmed.ncbi.nlm.nih.gov/27407096/).

### Empirically based Bayesian Emax models

- **Type:** Statistical method for dose–response estimation using Emax models with priors derived
  from historical dose–response data.
- **Submitter:** Pfizer.
- **FDA status:** Fit-for-Purpose, issued 5 August 2022. Strength: Strong.
- **DisMech:** No disease home; recorded here only.
- **References:** Primary publication not identified for this report.

## What the DisMech schema cannot hold today

`computational_models` records a model's type, repository, publication, and its links to
mechanism nodes with relationship, fidelity, limitations, model scale and typed divergences. It
has no slot for:

- the model's stated context of use;
- the validation level reached against that context of use;
- the regulatory status and the agency document behind it;
- models of a drug rather than a disease, such as PBPK and exposure–response models. The one
  precedent is "PBPK Model for GLP-1 Receptor Agonists" on `Type_2_Diabetes_Mellitus`.

Until the schema has these, this report is where they are kept.
