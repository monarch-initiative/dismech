---
reference_id: "HDRUK:PH618"
title: "Diabetes"
database: "HDR UK Phenotype Library"
source_snapshot: "PH618 version 1236"
content_type: "structured_record"
---

# HDRUK:PH618  Diabetes

**PH618** version 1236 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH618 |
| Version | 1236 |
| Name | Diabetes |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | David Reeves, David A Springate, Darren M Ashcroft, Ronan Ryan, Tim Doran, Richard Morris, Ivan Olier, Evangelos Kontopantelis |
| Collections | ClinicalCodes Repository; Phenotype Library |
| Coding systems | Read codes v2 |
| Data sources | CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1996 - 17/12/20003 |
| DOI | https://doi.org/10.48533/39gs-zf52 |
| Ontology | MONDO:0005015 diabetes mellitus |

## Definition

Data:

CPRD and THIN obtain their data from practices using the Vision electronic record system, while QResearch obtains data from practices using EMIS software. We felt that comparisons would be most informative between databases drawing data from different capture systems. Across the time-period studied, two versions of EMIS were in use, the more common being the text-based EMIS LV system with navigation and data entry mainly via the keyboard; EMIS PCS, which is Windows-based with mouse control and drop-down menus, was introduced from 1999. Vision was Windows-based throughout the study period. A small-scale direct comparison of EMIS LV and Vision indicated that coded data entry, excepting prescribing information, was faster with Vision and that more items were likely to be coded. Practices running Vision have slightly higher achievement rates for most Quality and Outcomes Framework (QOF) indicators than practices running either version of EMIS, even after controlling for differences in practice and area characteristics. We had access to CPRD, and therefore chose to replicate a study previously conducted using QResearch. CPRD and QResearch both draw data from general practices spread throughout the UK—currently more than 600 practices each—and comparisons to the national age-gender structure and prevalence rates for common conditions mostly show good correspondence for both datasets. For practical reasons, we focused on studies of the effectiveness of medicinal interventions and, after assessing the available studies, chose to replicate an investigation into the effects of statins on the mortality of patients with ischaemic heart disease (IHD) by Hippisley-Cox and Coupland (H-C&C). The methodological details provided in the published paper were insufficient on their own to allow a close replication to be conducted, and we therefore obtained additional details from the authors. We requested purely factual information about the methods used and did not share any of our analyses or results. We replicated the methods of H-C&C as closely as possible, given the differences between the two databases. All of the methods described below, including the study period, variable specifications and analytical procedures, are exact replications of those used in the original study, unless indicated otherwise. We selected all practices in CPRD that provided up to standard (UTS) data (UTS is CPRD’s designation for data meeting their internal quality standards) for the whole of the period from 1 January 1996 to 17 December 2003. We next identified all patients with a first diagnosis of IHD within this period, based on the QOF business rules for 2004. We excluded patients whose IHD diagnosis fell within the first 3 months of registration with their general practice or was on or subsequent to their recorded date of death, or who were prescribed statins prior to first diagnosis. We extracted data for these patients from the date of IHD diagnosis up until 17 December 2003, or until the date of death or exit from the practice, or the last recorded date for practices that stopped providing data before 17 December 2003, giving a maximum possible length of follow-up postdiagnosis of just under 8 years.

Analysis:

The main outcome was all-cause mortality, identified through a record of death in the CPRD. Following H-C&C, we conducted two main analyses: (1) a cohort analysis and (2) a case-control analysis nested within the full cohort. All analyses were conducted using R. Following H-C&C, statistical significance was assessed using p<0.01 (two tailed), but 95% CIs are reported in tables and figures. We made an a priori decision not to attempt to ‘improve’ on the analysis conducted by H-C&C, as our specific aim was to determine whether the same results and conclusions would emerge from using identical methods on a different underlying dataset targeting the same population.

Cohort analysis:

The cohort analysis used a Cox proportional hazards model to examine the effect of statin use on patient survival, with survival time determined by the time (in days) between the date of first diagnosis and date of death. Patients who transferred out of their practice before death or who were still alive at the end of the study period were treated as censored observations. Statin exposure was used as a time-varying covariate, with the period of exposure from the date of first prescription to when the statin was stopped (estimated as the date of last prescription plus 90 days; intervening breaks in the use of statins were ignored), or if not stopped until the end of the study period, date of death or date of transfer out of practice. Covariates adjusted for in the analysis were year of diagnosis, gender, comorbidities (diabetes, hypertension, myocardial infarction, congestive cardiac failure and cancer), and age (coded as 0–44, 45–54, 55–64, 65–74, 75–84, 85–94 or ≥95), smoking (ever smoked, never smoked, not recorded) and body mass index (BMI; coded as <25, 25–30, >30 kg/m2) all at the date of diagnosis. The presence of each comorbidity was indicated by a diagnosis in the patient record (using the 2004 QOF business rules) and coded as present/not present at the date of IHD diagnosis. If smoking status or BMI was not recorded within 4 years prior to diagnosis of IHD, we coded it as missing. The analysis was undertaken using the R survival analysis package accounting for the clustering of patients by practice and using the Huber-White robust estimate of SE. The proportional hazards assumption was checked graphically and with a test for proportional hazards.

Nested case-control study:

The nested case-control analysis compared all patients from the cohort who died during the follow-up period (the cases) with a group of matched control patients (also with IHD) who did not die. For each case, we defined an ‘index date’ as the date of death. We then used an incidence density sampling procedure (as per the original study; personal correspondence) to randomly select four control patients for each case matched on gender, year of IHD diagnosis and age (coded in 5-year age-bands). General practice was not used as a matching variable. Controls were patients with IHD alive at the time their matched case died (including patients who themselves became cases at a later time-point). The incidence sampling procedure allowed the same patient to be selected as a control for more than one case, thus providing a full set of four controls for each case, while still producing unbiased estimates of risk. Statin exposure was based on the first and last prescription dates prior to the index date and coded into: (1) currently taking statins (last prescription was within 90 days of the index date); (2) previously took statins (last prescription more than 90 days prior to the index date) and (3) has never taken statins. We did this for all statins as a group and also separately for five different types of statin (atorvastatin, cerivastatin, fluvastatin, pravastatin and simvastatin). For ‘all statins’, the last prescription could be for a different statin type than the first; for individual statins, it had to be the same type. One further formulation, rosuvastatin, was in use that did not appear in the QResearch study. We included this in the ‘all statins’ group but did not analyse it individually as only 22 patients had received the statin. Analysis of the case-control study used conditional logistic regression accounting for the matching of cases with controls, to obtain ORs for the risk of death in relation to use of statins. We allowed for clustering by general practice and used a robust estimate of SE, in line with the cohort analysis. Covariates in the analysis were smoking status, BMI and comorbidities, specified as in the Cohort analysis but based on the index date rather than the date of diagnosis. Additional covariates in this analysis were the Townsend deprivation score for the practice postcode (in national quintiles; H-C&C used quintiles of patient-level Townsend scores) and use of β-blockers, aspirin, ACE inhibitors and calcium channel blockers, identified through the British National Formulary chapter codes in the patient record. Each medication was coded as either used or not used prior to the index date but after the date of IHD diagnosis. Interactions between use of statins and each of gender, age (less than 75 vs 75 and over) and diabetes were tested by adding interaction terms into the model.

## Publications

- David Reeves, David A Springate, Darren M Ashcroft, Ronan Ryan, Tim Doran, Richard Morris, Ivan Olier, Evangelos Kontopantelis, Can analyses of electronic patient records be independently and externally validated? The effect of statins on the mortality of patients with ischaemic heart disease: a cohort study with nested case–control analysis. BMJ Open, 4:e004952 2014.

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:2126300 | Diabetes resolved | Diabetes - Primary Care |
| READ2:C10..00 | Diabetes mellitus | Diabetes - Primary Care |
| READ2:C100.00 | Diabetes mellitus with no mention of complication | Diabetes - Primary Care |
| READ2:C100000 | Diabetes mellitus; juvenile type; no mention of complication | Diabetes - Primary Care |
| READ2:C100011 | Insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C100100 | Diabetes mellitus; adult onset; no mention of complication | Diabetes - Primary Care |
| READ2:C100111 | Maturity onset diabetes | Diabetes - Primary Care |
| READ2:C100112 | Non-insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C100z00 | Diabetes mellitus NOS with no mention of complication | Diabetes - Primary Care |
| READ2:C101.00 | Diabetes mellitus with ketoacidosis | Diabetes - Primary Care |
| READ2:C101000 | Diabetes mellitus; juvenile type; with ketoacidosis | Diabetes - Primary Care |
| READ2:C101100 | Diabetes mellitus; adult onset; with ketoacidosis | Diabetes - Primary Care |
| READ2:C101y00 | Other specified diabetes mellitus with ketoacidosis | Diabetes - Primary Care |
| READ2:C101z00 | Diabetes mellitus NOS with ketoacidosis | Diabetes - Primary Care |
| READ2:C102.00 | Diabetes mellitus with hyperosmolar coma | Diabetes - Primary Care |
| READ2:C102000 | Diabetes mellitus; juvenile type; with hyperosmolar coma | Diabetes - Primary Care |
| READ2:C102100 | Diabetes mellitus; adult onset; with hyperosmolar coma | Diabetes - Primary Care |
| READ2:C102z00 | Diabetes mellitus NOS with hyperosmolar coma | Diabetes - Primary Care |
| READ2:C103.00 | Diabetes mellitus with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C103000 | Diabetes mellitus; juvenile type; with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C103100 | Diabetes mellitus; adult onset; with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C103y00 | Other specified diabetes mellitus with coma | Diabetes - Primary Care |
| READ2:C103z00 | Diabetes mellitus NOS with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C104.00 | Diabetes mellitus with renal manifestation | Diabetes - Primary Care |
| READ2:C104.11 | Diabetic nephropathy | Diabetes - Primary Care |
| READ2:C104000 | Diabetes mellitus; juvenile type; with renal manifestation | Diabetes - Primary Care |
| READ2:C104100 | Diabetes mellitus; adult onset; with renal manifestation | Diabetes - Primary Care |
| READ2:C104y00 | Other specified diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C104z00 | Diabetes mellitus with nephropathy NOS | Diabetes - Primary Care |
| READ2:C105.00 | Diabetes mellitus with ophthalmic manifestation | Diabetes - Primary Care |
| READ2:C105000 | Diabetes mellitus; juvenile type; + ophthalmic manifestation | Diabetes - Primary Care |
| READ2:C105100 | Diabetes mellitus; adult onset; + ophthalmic manifestation | Diabetes - Primary Care |
| READ2:C105y00 | Other specified diabetes mellitus with ophthalmic complicatn | Diabetes - Primary Care |
| READ2:C105z00 | Diabetes mellitus NOS with ophthalmic manifestation | Diabetes - Primary Care |
| READ2:C106.00 | Diabetes mellitus with neurological manifestation | Diabetes - Primary Care |
| READ2:C106.11 | Diabetic amyotrophy | Diabetes - Primary Care |
| READ2:C106.12 | Diabetes mellitus with neuropathy | Diabetes - Primary Care |
| READ2:C106.13 | Diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C106000 | Diabetes mellitus; juvenile; + neurological manifestation | Diabetes - Primary Care |
| READ2:C106100 | Diabetes mellitus; adult onset; + neurological manifestation | Diabetes - Primary Care |
| READ2:C106y00 | Other specified diabetes mellitus with neurological comps | Diabetes - Primary Care |
| READ2:C106z00 | Diabetes mellitus NOS with neurological manifestation | Diabetes - Primary Care |
| READ2:C107.00 | Diabetes mellitus with peripheral circulatory disorder | Diabetes - Primary Care |
| READ2:C107.11 | Diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C107.12 | Diabetes with gangrene | Diabetes - Primary Care |
| READ2:C107000 | Diabetes mellitus; juvenile +peripheral circulatory disorder | Diabetes - Primary Care |
| READ2:C107100 | Diabetes mellitus; adult; + peripheral circulatory disorder | Diabetes - Primary Care |
| READ2:C107200 | Diabetes mellitus; adult with gangrene | Diabetes - Primary Care |
| READ2:C107300 | IDDM with peripheral circulatory disorder | Diabetes - Primary Care |
| READ2:C107400 | NIDDM with peripheral circulatory disorder | Diabetes - Primary Care |
| READ2:C107z00 | Diabetes mellitus NOS with peripheral circulatory disorder | Diabetes - Primary Care |
| READ2:C108.00 | Insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C108.11 | IDDM-Insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C108.12 | Type 1 diabetes mellitus | Diabetes - Primary Care |
| READ2:C108.13 | Type I diabetes mellitus | Diabetes - Primary Care |
| READ2:C108000 | Insulin-dependent diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C108011 | Type I diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C108012 | Type 1 diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C108100 | Insulin-dependent diabetes mellitus with ophthalmic comps | Diabetes - Primary Care |
| READ2:C108112 | Type 1 diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C108200 | Insulin-dependent diabetes mellitus with neurological comps | Diabetes - Primary Care |
| READ2:C108211 | Type I diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C108212 | Type 1 diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C108300 | Insulin dependent diabetes mellitus with multiple complicatn | Diabetes - Primary Care |
| READ2:C108400 | Unstable insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C108411 | Unstable type I diabetes mellitus | Diabetes - Primary Care |
| READ2:C108412 | Unstable type 1 diabetes mellitus | Diabetes - Primary Care |
| READ2:C108500 | Insulin dependent diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C108511 | Type I diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C108512 | Type 1 diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C108600 | Insulin dependent diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C108700 | Insulin dependent diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C108711 | Type I diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C108712 | Type 1 diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C108800 | Insulin dependent diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C108811 | Type I diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C108812 | Type 1 diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C108900 | Insulin dependent diabetes maturity onset | Diabetes - Primary Care |
| READ2:C108911 | Type I diabetes mellitus maturity onset | Diabetes - Primary Care |
| READ2:C108912 | Type 1 diabetes mellitus maturity onset | Diabetes - Primary Care |
| READ2:C108A00 | Insulin-dependent diabetes without complication | Diabetes - Primary Care |
| READ2:C108A11 | Type I diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C108B00 | Insulin dependent diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C108B11 | Type I diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C108C00 | Insulin dependent diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C108D00 | Insulin dependent diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C108D11 | Type I diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C108E00 | Insulin dependent diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C108E11 | Type I diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C108E12 | Type 1 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C108F00 | Insulin dependent diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C108F11 | Type I diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C108G00 | Insulin dependent diab mell with peripheral angiopathy | Diabetes - Primary Care |
| READ2:C108H00 | Insulin dependent diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C108H11 | Type I diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C108J00 | Insulin dependent diab mell with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C108J11 | Type I diabetes mellitus with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C108J12 | Type 1 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C108y00 | Other specified diabetes mellitus with multiple comps | Diabetes - Primary Care |
| READ2:C108z00 | Unspecified diabetes mellitus with multiple complications | Diabetes - Primary Care |
| READ2:C109.00 | Non-insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C109.11 | NIDDM - Non-insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C109.12 | Type 2 diabetes mellitus | Diabetes - Primary Care |
| READ2:C109.13 | Type II diabetes mellitus | Diabetes - Primary Care |
| READ2:C109000 | Non-insulin-dependent diabetes mellitus with renal comps | Diabetes - Primary Care |
| READ2:C109011 | Type II diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C109012 | Type 2 diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C109100 | Non-insulin-dependent diabetes mellitus with ophthalm comps | Diabetes - Primary Care |
| READ2:C109111 | Type II diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C109112 | Type 2 diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C109200 | Non-insulin-dependent diabetes mellitus with neuro comps | Diabetes - Primary Care |
| READ2:C109211 | Type II diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C109212 | Type 2 diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C109300 | Non-insulin-dependent diabetes mellitus with multiple comps | Diabetes - Primary Care |
| READ2:C109400 | Non-insulin dependent diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C109411 | Type II diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C109412 | Type 2 diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C109500 | Non-insulin dependent diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C109511 | Type II diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C109512 | Type 2 diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C109600 | Non-insulin-dependent diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C109611 | Type II diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C109612 | Type 2 diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C109700 | Non-insulin dependent diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C109711 | Type II diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C109712 | Type 2 diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C109800 | Reaven's syndrome | Diabetes - Primary Care |
| READ2:C109900 | Non-insulin-dependent diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C109A00 | Non-insulin dependent diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C109A11 | Type II diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C109B00 | Non-insulin dependent diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C109B11 | Type II diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C109C00 | Non-insulin dependent diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C109C11 | Type II diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C109C12 | Type 2 diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C109D00 | Non-insulin dependent diabetes mellitus with hypoglyca coma | Diabetes - Primary Care |
| READ2:C109D11 | Type II diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C109D12 | Type 2 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C109E00 | Non-insulin depend diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C109E11 | Type II diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C109E12 | Type 2 diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C109F00 | Non-insulin-dependent d m with peripheral angiopath | Diabetes - Primary Care |
| READ2:C109F11 | Type II diabetes mellitus with peripheral angiopathy | Diabetes - Primary Care |
| READ2:C109F12 | Type 2 diabetes mellitus with peripheral angiopathy | Diabetes - Primary Care |
| READ2:C109G00 | Non-insulin dependent diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C109G11 | Type II diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C109G12 | Type 2 diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C109H00 | Non-insulin dependent d m with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C109H11 | Type II diabetes mellitus with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C109H12 | Type 2 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C109J00 | Insulin treated Type 2 diabetes mellitus | Diabetes - Primary Care |
| READ2:C109J11 | Insulin treated non-insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C109J12 | Insulin treated Type II diabetes mellitus | Diabetes - Primary Care |
| READ2:C109K00 | Hyperosmolar non-ketotic state in type 2 diabetes mellitus | Diabetes - Primary Care |
| READ2:C10A.00 | Malnutrition-related diabetes mellitus | Diabetes - Primary Care |
| READ2:C10A000 | Malnutrition-related diabetes mellitus with coma | Diabetes - Primary Care |
| READ2:C10A100 | Malnutrition-related diabetes mellitus with ketoacidosis | Diabetes - Primary Care |
| READ2:C10A500 | Malnutritn-relat diabetes melitus wth periph circul complctn | Diabetes - Primary Care |
| READ2:C10B.00 | Diabetes mellitus induced by steroids | Diabetes - Primary Care |
| READ2:C10B000 | Steroid induced diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10C.00 | Diabetes mellitus autosomal dominant | Diabetes - Primary Care |
| READ2:C10C.11 | Maturity onset diabetes in youth | Diabetes - Primary Care |
| READ2:C10C.12 | Maturity onset diabetes in youth type 1 | Diabetes - Primary Care |
| READ2:C10D.00 | Diabetes mellitus autosomal dominant type 2 | Diabetes - Primary Care |
| READ2:C10D.11 | Maturity onset diabetes in youth type 2 | Diabetes - Primary Care |
| READ2:C10E.00 | Type 1 diabetes mellitus | Diabetes - Primary Care |
| READ2:C10E.11 | Type I diabetes mellitus | Diabetes - Primary Care |
| READ2:C10E.12 | Insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C10E000 | Type 1 diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C10E012 | Insulin-dependent diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C10E100 | Type 1 diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C10E111 | Type I diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C10E112 | Insulin-dependent diabetes mellitus with ophthalmic comps | Diabetes - Primary Care |
| READ2:C10E200 | Type 1 diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C10E212 | Insulin-dependent diabetes mellitus with neurological comps | Diabetes - Primary Care |
| READ2:C10E300 | Type 1 diabetes mellitus with multiple complications | Diabetes - Primary Care |
| READ2:C10E311 | Type I diabetes mellitus with multiple complications | Diabetes - Primary Care |
| READ2:C10E312 | Insulin dependent diabetes mellitus with multiple complicat | Diabetes - Primary Care |
| READ2:C10E400 | Unstable type 1 diabetes mellitus | Diabetes - Primary Care |
| READ2:C10E411 | Unstable type I diabetes mellitus | Diabetes - Primary Care |
| READ2:C10E412 | Unstable insulin dependent diabetes mellitus | Diabetes - Primary Care |
| READ2:C10E500 | Type 1 diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C10E511 | Type I diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C10E512 | Insulin dependent diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C10E600 | Type 1 diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C10E611 | Type I diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C10E700 | Type 1 diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C10E711 | Type I diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C10E712 | Insulin dependent diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C10E800 | Type 1 diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C10E812 | Insulin dependent diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C10E900 | Type 1 diabetes mellitus maturity onset | Diabetes - Primary Care |
| READ2:C10E911 | Type I diabetes mellitus maturity onset | Diabetes - Primary Care |
| READ2:C10E912 | Insulin dependent diabetes maturity onset | Diabetes - Primary Care |
| READ2:C10EA00 | Type 1 diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10EA11 | Type I diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10EA12 | Insulin-dependent diabetes without complication | Diabetes - Primary Care |
| READ2:C10EB00 | Type 1 diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C10EC00 | Type 1 diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C10EC11 | Type I diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C10EC12 | Insulin dependent diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C10ED00 | Type 1 diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C10ED12 | Insulin dependent diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C10EE00 | Type 1 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C10EE12 | Insulin dependent diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C10EF00 | Type 1 diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C10EF12 | Insulin dependent diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C10EG00 | Type 1 diabetes mellitus with peripheral angiopathy | Diabetes - Primary Care |
| READ2:C10EH00 | Type 1 diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C10EJ00 | Type 1 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C10EK00 | Type 1 diabetes mellitus with persistent proteinuria | Diabetes - Primary Care |
| READ2:C10EL00 | Type 1 diabetes mellitus with persistent microalbuminuria | Diabetes - Primary Care |
| READ2:C10EL11 | Type I diabetes mellitus with persistent microalbuminuria | Diabetes - Primary Care |
| READ2:C10EM00 | Type 1 diabetes mellitus with ketoacidosis | Diabetes - Primary Care |
| READ2:C10EM11 | Type I diabetes mellitus with ketoacidosis | Diabetes - Primary Care |
| READ2:C10EN00 | Type 1 diabetes mellitus with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C10EN11 | Type I diabetes mellitus with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C10EP00 | Type 1 diabetes mellitus with exudative maculopathy | Diabetes - Primary Care |
| READ2:C10EP11 | Type I diabetes mellitus with exudative maculopathy | Diabetes - Primary Care |
| READ2:C10EQ00 | Type 1 diabetes mellitus with gastroparesis | Diabetes - Primary Care |
| READ2:C10ER00 | Latent autoimmune diabetes mellitus in adult | Diabetes - Primary Care |
| READ2:C10F.00 | Type 2 diabetes mellitus | Diabetes - Primary Care |
| READ2:C10F.11 | Type II diabetes mellitus | Diabetes - Primary Care |
| READ2:C10F000 | Type 2 diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C10F011 | Type II diabetes mellitus with renal complications | Diabetes - Primary Care |
| READ2:C10F100 | Type 2 diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C10F111 | Type II diabetes mellitus with ophthalmic complications | Diabetes - Primary Care |
| READ2:C10F200 | Type 2 diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C10F211 | Type II diabetes mellitus with neurological complications | Diabetes - Primary Care |
| READ2:C10F300 | Type 2 diabetes mellitus with multiple complications | Diabetes - Primary Care |
| READ2:C10F311 | Type II diabetes mellitus with multiple complications | Diabetes - Primary Care |
| READ2:C10F400 | Type 2 diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C10F411 | Type II diabetes mellitus with ulcer | Diabetes - Primary Care |
| READ2:C10F500 | Type 2 diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C10F511 | Type II diabetes mellitus with gangrene | Diabetes - Primary Care |
| READ2:C10F600 | Type 2 diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C10F611 | Type II diabetes mellitus with retinopathy | Diabetes - Primary Care |
| READ2:C10F700 | Type 2 diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C10F711 | Type II diabetes mellitus - poor control | Diabetes - Primary Care |
| READ2:C10F800 | Reaven's syndrome | Diabetes - Primary Care |
| READ2:C10F811 | Metabolic syndrome X | Diabetes - Primary Care |
| READ2:C10F900 | Type 2 diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10F911 | Type II diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10FA00 | Type 2 diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C10FA11 | Type II diabetes mellitus with mononeuropathy | Diabetes - Primary Care |
| READ2:C10FB00 | Type 2 diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C10FB11 | Type II diabetes mellitus with polyneuropathy | Diabetes - Primary Care |
| READ2:C10FC00 | Type 2 diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C10FC11 | Type II diabetes mellitus with nephropathy | Diabetes - Primary Care |
| READ2:C10FD00 | Type 2 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C10FD11 | Type II diabetes mellitus with hypoglycaemic coma | Diabetes - Primary Care |
| READ2:C10FE00 | Type 2 diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C10FE11 | Type II diabetes mellitus with diabetic cataract | Diabetes - Primary Care |
| READ2:C10FF00 | Type 2 diabetes mellitus with peripheral angiopathy | Diabetes - Primary Care |
| READ2:C10FG00 | Type 2 diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C10FG11 | Type II diabetes mellitus with arthropathy | Diabetes - Primary Care |
| READ2:C10FH00 | Type 2 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary Care |
| READ2:C10FJ00 | Insulin treated Type 2 diabetes mellitus | Diabetes - Primary Care |
| READ2:C10FJ11 | Insulin treated Type II diabetes mellitus | Diabetes - Primary Care |
| READ2:C10FK00 | Hyperosmolar non-ketotic state in type 2 diabetes mellitus | Diabetes - Primary Care |
| READ2:C10FL00 | Type 2 diabetes mellitus with persistent proteinuria | Diabetes - Primary Care |
| READ2:C10FL11 | Type II diabetes mellitus with persistent proteinuria | Diabetes - Primary Care |
| READ2:C10FM00 | Type 2 diabetes mellitus with persistent microalbuminuria | Diabetes - Primary Care |
| READ2:C10FM11 | Type II diabetes mellitus with persistent microalbuminuria | Diabetes - Primary Care |
| READ2:C10FN00 | Type 2 diabetes mellitus with ketoacidosis | Diabetes - Primary Care |
| READ2:C10FP00 | Type 2 diabetes mellitus with ketoacidotic coma | Diabetes - Primary Care |
| READ2:C10FQ00 | Type 2 diabetes mellitus with exudative maculopathy | Diabetes - Primary Care |
| READ2:C10FR00 | Type 2 diabetes mellitus with gastroparesis | Diabetes - Primary Care |
| READ2:C10FS00 | Maternally inherited diabetes mellitus | Diabetes - Primary Care |
| READ2:C10G.00 | Secondary pancreatic diabetes mellitus | Diabetes - Primary Care |
| READ2:C10G000 | Secondary pancreatic diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10H.00 | Diabetes mellitus induced by non-steroid drugs | Diabetes - Primary Care |
| READ2:C10H000 | DM induced by non-steroid drugs without complication | Diabetes - Primary Care |
| READ2:C10J.00 | Insulin autoimmune syndrome | Diabetes - Primary Care |
| READ2:C10K.00 | Type A insulin resistance | Diabetes - Primary Care |
| READ2:C10K000 | Type A insulin resistance without complication | Diabetes - Primary Care |
| READ2:C10M.00 | Lipoatrophic diabetes mellitus | Diabetes - Primary Care |
| READ2:C10N.00 | Secondary diabetes mellitus | Diabetes - Primary Care |
| READ2:C10N000 | Secondary diabetes mellitus without complication | Diabetes - Primary Care |
| READ2:C10N100 | Cystic fibrosis related diabetes mellitus | Diabetes - Primary Care |
| READ2:C10y.00 | Diabetes mellitus with other specified manifestation | Diabetes - Primary Care |
| READ2:C10y100 | Diabetes mellitus; adult; + other specified manifestation | Diabetes - Primary Care |
| READ2:C10yy00 | Other specified diabetes mellitus with other spec comps | Diabetes - Primary Care |
| READ2:C10yz00 | Diabetes mellitus NOS with other specified manifestation | Diabetes - Primary Care |
| READ2:C10z.00 | Diabetes mellitus with unspecified complication | Diabetes - Primary Care |
| READ2:C10z000 | Diabetes mellitus; juvenile type; + unspecified complication | Diabetes - Primary Care |
| READ2:C10z100 | Diabetes mellitus; adult onset; + unspecified complication | Diabetes - Primary Care |
| READ2:C10zy00 | Other specified diabetes mellitus with unspecified comps | Diabetes - Primary Care |
| READ2:C10zz00 | Diabetes mellitus NOS with unspecified complication | Diabetes - Primary Care |

## Source

HDR UK Phenotype Library record PH618 version 1236, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH618/version/1236/detail/)
