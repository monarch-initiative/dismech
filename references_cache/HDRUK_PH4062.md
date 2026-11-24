---
reference_id: "HDRUK:PH4062"
title: "Diabetes"
database: "HDR UK Phenotype Library"
source_snapshot: "PH4062 version 9273"
content_type: "structured_record"
---

# HDRUK:PH4062  Diabetes

**PH4062** version 9273 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH4062 |
| Version | 9273 |
| Name | Diabetes |
| Type | Disease or syndrome |
| Template | BHF Data Science Centre Phenotype |
| Author | Chalmers, F, Young K, Walker E, Chilala C, Coombe A, Shields B, Preiss D, Cezard G, MacArthur J, Dennis J, Valabhji J, Kaptoge S, Khunti K, Mafham M, Rutter MK, Lessels S, Shi W, Wild S, Eastwood S, Denaxas S, Bolton T, Thomas N, Pearson E |
| Collections | BHF Data Science Centre |
| Coding systems | SNOMED CT codes; BNF codes; ICD10 codes |
| Data sources | GPES Data for Pandemic Planning and Research (COVID-19); Hospital Episode Statistics Admitted Patient Care; Medicines dispensed in Primary Care (NHSBSA data) |
| Sex | Both |
| DOI | https://doi.org/10.48533/61w4-w911 |
| Ontology | MONDO:0005015 diabetes mellitus |

## Definition

This phenotype is a rule-based diabetes phenotyping algorithm designed for use in electronic health records (EHR) to **identify people with diabetes, define diabetes type, and determine date of diagnosis** from routinely collected health data. It is intended to improve the quality, consistency, transparency, and comparability of diabetes research using EHRs. The algorithm has been developed iteratively, and multiple versions are available to reflect updates and refinements over time.

The algorithm was developed by the Diabetes Data Science Catalyst (DDSC) (https://bhfdatasciencecentre.org/areas/diabetes-data-science-catalyst/?utm_source=chatgpt.com), a collaboration between the BHF Data Science Centre, Diabetes UK, and HDR UK.

Further details of the algorithm are available through the public DDSC diabetes phenotype app (https://bhf-dsc-hds.shinyapps.io/hds_phenotypes_diabetes/).

## Implementation

This phenotype is implemented as a rule-based algorithm for application to electronic health records, using structured logic applied to diagnosis, prescribing, and laboratory data to identify diabetes status, define diabetes type, and derive date of diagnosis. The implementation is coded in PySpark and R and is publicly available through the BHF Data Science Centre GitHub (https://github.com/BHFDSC/hds_phenotypes_diabetes), with supporting methodological documentation provided through the associated public application (https://bhf-dsc-hds.shinyapps.io/hds_phenotypes_diabetes/).

!DDSC algorithm flow chart (https://raw.githubusercontent.com/BHFDSC/hds_phenotypes_diabetes/main/flowchart/DDSC_Algorithm.png)

## Validation

The phenotype underwent validation using UK Biobank data, with a particular focus on assessing the classification of diabetes type. Validation results were used to refine the algorithm and improve performance, including changes aimed at increasing the specificity of type 1 diabetes identification. The phenotype has been validated by the authors of the algorithm and by researchers applying it within the CVD-COVID-UK consortium. The current version therefore reflects both rule-based clinical logic and empirical validation.

## Codes

| Code | Description | Concept |
|---|---|---|
| ICD10:E10 | Type 1 diabetes mellitus | Diabetes Type 1 |
| ICD10:E100 | Type 1 diabetes mellitus With coma | Diabetes Type 1 |
| ICD10:E101 | Type 1 diabetes mellitus With ketoacidosis | Diabetes Type 1 |
| ICD10:E102 | Type 1 diabetes mellitus With renal complications | Diabetes Type 1 |
| ICD10:E103 | Type 1 diabetes mellitus With ophthalmic complications | Diabetes Type 1 |
| ICD10:E104 | Type 1 diabetes mellitus With neurological complications | Diabetes Type 1 |
| ICD10:E105 | Type 1 diabetes mellitus With peripheral circulatory complications | Diabetes Type 1 |
| ICD10:E106 | Type 1 diabetes mellitus With other specified complications | Diabetes Type 1 |
| ICD10:E107 | Type 1 diabetes mellitus With multiple complications | Diabetes Type 1 |
| ICD10:E108 | Type 1 diabetes mellitus With unspecified complications | Diabetes Type 1 |
| ICD10:E109 | Type 1 diabetes mellitus Without complications | Diabetes Type 1 |
| ICD10:O240 | Diabetes mellitus in pregnancy: Pre-existing type 1 diabetes mellitus | Diabetes Type 1 |
| ICD10:E11 | Type 2 diabetes mellitus | Diabetes Type 2 |
| ICD10:E110 | Type 2 diabetes mellitus With coma | Diabetes Type 2 |
| ICD10:E111 | Type 2 diabetes mellitus With ketoacidosis | Diabetes Type 2 |
| ICD10:E112 | Type 2 diabetes mellitus With renal complications | Diabetes Type 2 |
| ICD10:E113 | Type 2 diabetes mellitus With ophthalmic complications | Diabetes Type 2 |
| ICD10:E114 | Type 2 diabetes mellitus With neurological complications | Diabetes Type 2 |
| ICD10:E115 | Type 2 diabetes mellitus With peripheral circulatory complications | Diabetes Type 2 |
| ICD10:E116 | Type 2 diabetes mellitus With other specified complications | Diabetes Type 2 |
| ICD10:E117 | Type 2 diabetes mellitus With multiple complications | Diabetes Type 2 |
| ICD10:E118 | Type 2 diabetes mellitus With unspecified complications | Diabetes Type 2 |
| ICD10:E119 | Type 2 diabetes mellitus Without complications | Diabetes Type 2 |
| ICD10:O241 | Diabetes mellitus in pregnancy: Pre-existing type 2 diabetes mellitus | Diabetes Type 2 |
| ICD10:E13 | Other specified diabetes mellitus | Diabetes Not Otherwise Specified |
| ICD10:E130 | Other specified diabetes mellitus with coma | Diabetes Not Otherwise Specified |
| ICD10:E131 | Other specified diabetes mellitus with ketoacidosis | Diabetes Not Otherwise Specified |
| ICD10:E132 | Other specified diabetes mellitus with renal complications | Diabetes Not Otherwise Specified |
| ICD10:E133 | Other specified diabetes mellitus with ophthalmic complications | Diabetes Not Otherwise Specified |
| ICD10:E134 | Other specified diabetes mellitus with neurological complications | Diabetes Not Otherwise Specified |
| ICD10:E135 | Other specified diabetes mellitus with peripheral circulatory complications | Diabetes Not Otherwise Specified |
| ICD10:E136 | Other specified diabetes mellitus with other specified complications | Diabetes Not Otherwise Specified |
| ICD10:E137 | Other specified diabetes mellitus with multiple complications | Diabetes Not Otherwise Specified |
| ICD10:E138 | Other specified diabetes mellitus with unspecified complications | Diabetes Not Otherwise Specified |
| ICD10:E139 | Other specified diabetes mellitus without complications | Diabetes Not Otherwise Specified |
| ICD10:E14 | Unspecified diabetes mellitus | Diabetes Not Otherwise Specified |
| ICD10:E140 | Unspecified diabetes mellitus with coma | Diabetes Not Otherwise Specified |
| ICD10:E141 | Unspecified diabetes mellitus with ketoacidosis | Diabetes Not Otherwise Specified |
| ICD10:E142 | Unspecified diabetes mellitus with renal complications | Diabetes Not Otherwise Specified |
| ICD10:E143 | Unspecified diabetes mellitus with ophthalmic complications | Diabetes Not Otherwise Specified |
| ICD10:E144 | Unspecified diabetes mellitus with neurological complications | Diabetes Not Otherwise Specified |
| ICD10:E145 | Unspecified diabetes mellitus with peripheral circulatory complications | Diabetes Not Otherwise Specified |
| ICD10:E146 | Unspecified diabetes mellitus with other specified complications | Diabetes Not Otherwise Specified |
| ICD10:E147 | Unspecified diabetes mellitus with multiple complications | Diabetes Not Otherwise Specified |
| ICD10:E148 | Unspecified diabetes mellitus with unspecified complications | Diabetes Not Otherwise Specified |
| ICD10:E149 | Unspecified diabetes mellitus without complications | Diabetes Not Otherwise Specified |
| ICD10:G590 | Diabetic mononeuropathy | Diabetes Not Otherwise Specified |
| ICD10:G632 | Diabetic polyneuropathy | Diabetes Not Otherwise Specified |
| ICD10:H280 | Diabetic cataract | Diabetes Not Otherwise Specified |
| ICD10:H360 | Diabetic retinopathy | Diabetes Not Otherwise Specified |
| ICD10:M142 | Diabetic arthropathy | Diabetes Not Otherwise Specified |
| ICD10:N083 | Glomerular disorders in diabetes mellitus | Diabetes Not Otherwise Specified |
| ICD10:O243 | Diabetes mellitus in pregnancy: Pre-existing diabetes mellitus, unspecified | Diabetes Not Otherwise Specified |
| ICD10:Y423 | Insulin and oral hypoglycaemic [antidiabetic] drugs | Diabetes Not Otherwise Specified |
| 0601011A0 (BNF codes) | Insulin aspart | Insulin |
| 0601011L0 (BNF codes) | Insulin Lispro | Insulin |
| 0601011N0 (BNF codes) | Soluble insulin (Neutral insulin) | Insulin |
| 0601011P0 (BNF codes) | Insulin glulisine | Insulin |
| 0601011Q0 (BNF codes) |  | Insulin |
| 0601011R0 (BNF codes) | Insulin human | Insulin |
| 0601012AB (BNF codes) | Insulin glargine/lixisenatide | Insulin |
| 0601012D0 (BNF codes) | Biphasic isophane insulin | Insulin |
| 0601012F0 (BNF codes) | Biphasic insulin lispro | Insulin |
| 0601012G0 (BNF codes) | Insulin zinc suspension | Insulin |
| 0601012N0 (BNF codes) |  | Insulin |
| 0601012S0 (BNF codes) | Isophane insulin | Insulin |
| 0601012U0 (BNF codes) | Protamine zinc insulin | Insulin |
| 0601012V0 (BNF codes) | Insulin glargine | Insulin |
| 0601012W0 (BNF codes) | Biphasic insulin aspart | Insulin |
| 0601012X0 (BNF codes) | Insulin detemir | Insulin |
| 0601012Z0 (BNF codes) | Insulin degludec | Insulin |
| 0601022B0 (BNF codes) | Metformin hydrochloride | Metformin |
| 0601021A0 (BNF codes) | Glimepiride | Glucose Lowering Therapies |
| 0601021E0 (BNF codes) | Chlorpropamide | Glucose Lowering Therapies |
| 0601021H0 (BNF codes) | Glibenclamide | Glucose Lowering Therapies |
| 0601021M0 (BNF codes) | Gliclazide | Glucose Lowering Therapies |
| 0601021P0 (BNF codes) | Glipizide | Glucose Lowering Therapies |
| 0601021R0 (BNF codes) |  | Glucose Lowering Therapies |
| 0601021X0 (BNF codes) | Tolbutamide | Glucose Lowering Therapies |
| 0601023A0 (BNF codes) | Acarbose | Glucose Lowering Therapies |
| 0601023AA (BNF codes) | Vildagliptin | Glucose Lowering Therapies |
| 0601023AB (BNF codes) | Liraglutide | Glucose Lowering Therapies |
| 0601023AC (BNF codes) | Saxagliptin | Glucose Lowering Therapies |
| 0601023AD (BNF codes) | Metformin hydrochloride/sitagliptin | Glucose Lowering Therapies |
| 0601023AE (BNF codes) | Linagliptin | Glucose Lowering Therapies |
| 0601023AF (BNF codes) | Linagliptin/metformin | Glucose Lowering Therapies |
| 0601023AG (BNF codes) | Dapagliflozin | Glucose Lowering Therapies |
| 0601023AH (BNF codes) | Saxagliptin/metformin | Glucose Lowering Therapies |
| 0601023AI (BNF codes) | Lixisenatide | Glucose Lowering Therapies |
| 0601023AJ (BNF codes) | Alogliptin/metformin | Glucose Lowering Therapies |
| 0601023AK (BNF codes) | Alogliptin | Glucose Lowering Therapies |
| 0601023AL (BNF codes) | Dapagliflozin/metformin | Glucose Lowering Therapies |
| 0601023AM (BNF codes) | Canagliflozin | Glucose Lowering Therapies |
| 0601023AN (BNF codes) | Empagliflozin | Glucose Lowering Therapies |
| 0601023AP (BNF codes) | Canagliflozin/metformin | Glucose Lowering Therapies |
| 0601023AQ (BNF codes) | Dulaglutide | Glucose Lowering Therapies |
| 0601023AR (BNF codes) | Empagliflozin/metformin | Glucose Lowering Therapies |
| 0601023AS (BNF codes) | Albiglutide | Glucose Lowering Therapies |
| 0601023AU (BNF codes) | Ins degludec/liraglutide | Glucose Lowering Therapies |
| 0601023AV (BNF codes) | Saxagliptin/dapagliflozin | Glucose Lowering Therapies |
| 0601023AW (BNF codes) | Semaglutide | Glucose Lowering Therapies |
| 0601023AX (BNF codes) | Ertugliflozin | Glucose Lowering Therapies |
| 0601023AY (BNF codes) | Empagliflozin/linagliptin | Glucose Lowering Therapies |
| 0601023AZ (BNF codes) | Tirzepatide | Glucose Lowering Therapies |
| 0601023B0 (BNF codes) | Pioglitazone hydrochloride | Glucose Lowering Therapies |
| 0601023I0 (BNF codes) | Guar gum | Glucose Lowering Therapies |
| 0601023R0 (BNF codes) | Repaglinide | Glucose Lowering Therapies |
| 0601023S0 (BNF codes) | Rosiglitazone | Glucose Lowering Therapies |
| 0601023U0 (BNF codes) | Nateglinide | Glucose Lowering Therapies |
| 0601023V0 (BNF codes) | Metformin hydrochloride/rosiglitazone | Glucose Lowering Therapies |
| 0601023W0 (BNF codes) | Metformin hydrochloride/pioglitazone | Glucose Lowering Therapies |
| 0601023X0 (BNF codes) | Sitagliptin | Glucose Lowering Therapies |
| 0601023Y0 (BNF codes) | Exenatide | Glucose Lowering Therapies |
| 0601023Z0 (BNF codes) | Metformin hydrochloride/vildagliptin | Glucose Lowering Therapies |

Not cached: 628 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH4062 version 9273, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH4062/version/9273/detail/)
