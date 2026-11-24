---
reference_id: "HDRUK:PH152"
title: "Diabetes"
database: "HDR UK Phenotype Library"
source_snapshot: "PH152 version 304"
content_type: "structured_record"
---

# HDRUK:PH152  Diabetes

**PH152** version 304 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH152 |
| Version | 304 |
| Name | Diabetes |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A |
| Collections | CALIBER; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; Med codes |
| Data sources | CPRD GOLD; HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/96hk-f518 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/Diabetes---a1f20850-1779-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/Diabetes.cwl |
| Ontology | MONDO:0005015 diabetes mellitus |

## Definition

Use MODIFIED CALIBER 'Diabetes' phenotyping algorithm for

1. T1DM,

2. T2DM,

3. 'Diabetes' other or uncertain type:

IF there is at least one record for code for type 2 'Diabetes' (diabdiag_gprd = 4)

and no record for type 1 'Diabetes' (no record with diabdiag_gprd = 3)

then classify the patient as type 2 'Diabetes'

ELSE if there is at least one record for code for type I 'Diabetes' (diabdiag_gprd = 3)

and no record for type 2 'Diabetes' (no record with diabdiag_gprd = 4)

then classify the patient as type 1 'Diabetes'

ELSE if there is at least one record of type 1 'Diabetes' (diabdiag_gprd = 3)

and type 2 'Diabetes' (diabdiag_gprd = 4)

then classify as 'Diabetes' other or uncertain type

ELSE if there are no diabdiag_gprd records for this patient:

If there is at least one record for Non-insulin-dependent 'Diabetes' mellitus (NIDDM) (dm_gprd = 4 or dm_hes = 4)

and no record for IDDM (no record with dm_gprd = 3 or dm_hes = 3)

then classify the patient as type 2 'Diabetes'

ELSE if there is at least one record for Insulin-dependent 'Diabetes' mellitus (IDDM) (dm_gprd = 3 or dm_hes = 3)

and no record for NIDDM (no record with dm_gprd = 4 or dm_hes = 4)

then classify the patient as type 1 'Diabetes'

ELSE if there is at least one record of 'Diabetes' (dm_gprd or dm_hes category 3, 4, 5 or 6)

then classify as 'Diabetes' other or uncertain type

ELSE classify as no 'Diabetes'

## Publications

- Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI 10.1016/S2589-7500(19)30012-3

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:C108.12 | Type 1 diabetes mellitus | Diabetes - Primary care |
| READ2:C108.13 | Type I diabetes mellitus | Diabetes - Primary care |
| READ2:C108011 | Type I diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C108012 | Type 1 diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C108211 | Type I diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C108212 | Type 1 diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C108411 | Unstable type I diabetes mellitus | Diabetes - Primary care |
| READ2:C108412 | Unstable type 1 diabetes mellitus | Diabetes - Primary care |
| READ2:C108511 | Type I diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C108512 | Type 1 diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C108711 | Type I diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C108712 | Type 1 diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C108811 | Type I diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C108812 | Type 1 diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C108911 | Type I diabetes mellitus maturity onset | Diabetes - Primary care |
| READ2:C108912 | Type 1 diabetes mellitus maturity onset | Diabetes - Primary care |
| READ2:C108A11 | Type I diabetes mellitus without complication | Diabetes - Primary care |
| READ2:C108D11 | Type I diabetes mellitus with nephropathy | Diabetes - Primary care |
| READ2:C108E11 | Type I diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C108E12 | Type 1 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C108F11 | Type I diabetes mellitus with diabetic cataract | Diabetes - Primary care |
| READ2:C108H11 | Type I diabetes mellitus with arthropathy | Diabetes - Primary care |
| READ2:C108J11 | Type I diabetes mellitus with neuropathic arthropathy | Diabetes - Primary care |
| READ2:C108J12 | Type 1 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary care |
| READ2:C109.12 | Type 2 diabetes mellitus | Diabetes - Primary care |
| READ2:C109.13 | Type II diabetes mellitus | Diabetes - Primary care |
| READ2:C109011 | Type II diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C109012 | Type 2 diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C109111 | Type II diabetes mellitus with ophthalmic complications | Diabetes - Primary care |
| READ2:C109112 | Type 2 diabetes mellitus with ophthalmic complications | Diabetes - Primary care |
| READ2:C109211 | Type II diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C109212 | Type 2 diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C109411 | Type II diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C109412 | Type 2 diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C109511 | Type II diabetes mellitus with gangrene | Diabetes - Primary care |
| READ2:C109512 | Type 2 diabetes mellitus with gangrene | Diabetes - Primary care |
| READ2:C109611 | Type II diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C109612 | Type 2 diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C109711 | Type II diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C109712 | Type 2 diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C109A11 | Type II diabetes mellitus with mononeuropathy | Diabetes - Primary care |
| READ2:C109B11 | Type II diabetes mellitus with polyneuropathy | Diabetes - Primary care |
| READ2:C109C11 | Type II diabetes mellitus with nephropathy | Diabetes - Primary care |
| READ2:C109C12 | Type 2 diabetes mellitus with nephropathy | Diabetes - Primary care |
| READ2:C109D11 | Type II diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C109D12 | Type 2 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C109E11 | Type II diabetes mellitus with diabetic cataract | Diabetes - Primary care |
| READ2:C109E12 | Type 2 diabetes mellitus with diabetic cataract | Diabetes - Primary care |
| READ2:C109F11 | Type II diabetes mellitus with peripheral angiopathy | Diabetes - Primary care |
| READ2:C109F12 | Type 2 diabetes mellitus with peripheral angiopathy | Diabetes - Primary care |
| READ2:C109G11 | Type II diabetes mellitus with arthropathy | Diabetes - Primary care |
| READ2:C109G12 | Type 2 diabetes mellitus with arthropathy | Diabetes - Primary care |
| READ2:C109H11 | Type II diabetes mellitus with neuropathic arthropathy | Diabetes - Primary care |
| READ2:C109H12 | Type 2 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary care |
| READ2:C109J00 | Insulin treated Type 2 diabetes mellitus | Diabetes - Primary care |
| READ2:C109J12 | Insulin treated Type II diabetes mellitus | Diabetes - Primary care |
| READ2:C109K00 | Hyperosmolar non-ketotic state in type 2 diabetes mellitus | Diabetes - Primary care |
| READ2:C10E.00 | Type 1 diabetes mellitus | Diabetes - Primary care |
| READ2:C10E.11 | Type I diabetes mellitus | Diabetes - Primary care |
| READ2:C10E000 | Type 1 diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C10E100 | Type 1 diabetes mellitus with ophthalmic complications | Diabetes - Primary care |
| READ2:C10E200 | Type 1 diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C10E300 | Type 1 diabetes mellitus with multiple complications | Diabetes - Primary care |
| READ2:C10E311 | Type I diabetes mellitus with multiple complications | Diabetes - Primary care |
| READ2:C10E400 | Unstable type 1 diabetes mellitus | Diabetes - Primary care |
| READ2:C10E411 | Unstable type I diabetes mellitus | Diabetes - Primary care |
| READ2:C10E500 | Type 1 diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C10E511 | Type I diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C10E600 | Type 1 diabetes mellitus with gangrene | Diabetes - Primary care |
| READ2:C10E700 | Type 1 diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C10E711 | Type I diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C10E800 | Type 1 diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C10E900 | Type 1 diabetes mellitus maturity onset | Diabetes - Primary care |
| READ2:C10E911 | Type I diabetes mellitus maturity onset | Diabetes - Primary care |
| READ2:C10EA00 | Type 1 diabetes mellitus without complication | Diabetes - Primary care |
| READ2:C10EA11 | Type I diabetes mellitus without complication | Diabetes - Primary care |
| READ2:C10EB00 | Type 1 diabetes mellitus with mononeuropathy | Diabetes - Primary care |
| READ2:C10EC00 | Type 1 diabetes mellitus with polyneuropathy | Diabetes - Primary care |
| READ2:C10EC11 | Type I diabetes mellitus with polyneuropathy | Diabetes - Primary care |
| READ2:C10ED00 | Type 1 diabetes mellitus with nephropathy | Diabetes - Primary care |
| READ2:C10EE00 | Type 1 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C10EF00 | Type 1 diabetes mellitus with diabetic cataract | Diabetes - Primary care |
| READ2:C10EG00 | Type 1 diabetes mellitus with peripheral angiopathy | Diabetes - Primary care |
| READ2:C10EH00 | Type 1 diabetes mellitus with arthropathy | Diabetes - Primary care |
| READ2:C10EJ00 | Type 1 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary care |
| READ2:C10EK00 | Type 1 diabetes mellitus with persistent proteinuria | Diabetes - Primary care |
| READ2:C10EL00 | Type 1 diabetes mellitus with persistent microalbuminuria | Diabetes - Primary care |
| READ2:C10EM00 | Type 1 diabetes mellitus with ketoacidosis | Diabetes - Primary care |
| READ2:C10EM11 | Type I diabetes mellitus with ketoacidosis | Diabetes - Primary care |
| READ2:C10EN00 | Type 1 diabetes mellitus with ketoacidotic coma | Diabetes - Primary care |
| READ2:C10EN11 | Type I diabetes mellitus with ketoacidotic coma | Diabetes - Primary care |
| READ2:C10EP00 | Type 1 diabetes mellitus with exudative maculopathy | Diabetes - Primary care |
| READ2:C10EP11 | Type I diabetes mellitus with exudative maculopathy | Diabetes - Primary care |
| READ2:C10EQ00 | Type 1 diabetes mellitus with gastroparesis | Diabetes - Primary care |
| READ2:C10F.00 | Type 2 diabetes mellitus | Diabetes - Primary care |
| READ2:C10F.11 | Type II diabetes mellitus | Diabetes - Primary care |
| READ2:C10F000 | Type 2 diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C10F011 | Type II diabetes mellitus with renal complications | Diabetes - Primary care |
| READ2:C10F100 | Type 2 diabetes mellitus with ophthalmic complications | Diabetes - Primary care |
| READ2:C10F200 | Type 2 diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C10F211 | Type II diabetes mellitus with neurological complications | Diabetes - Primary care |
| READ2:C10F300 | Type 2 diabetes mellitus with multiple complications | Diabetes - Primary care |
| READ2:C10F311 | Type II diabetes mellitus with multiple complications | Diabetes - Primary care |
| READ2:C10F400 | Type 2 diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C10F411 | Type II diabetes mellitus with ulcer | Diabetes - Primary care |
| READ2:C10F500 | Type 2 diabetes mellitus with gangrene | Diabetes - Primary care |
| READ2:C10F600 | Type 2 diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C10F611 | Type II diabetes mellitus with retinopathy | Diabetes - Primary care |
| READ2:C10F700 | Type 2 diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C10F711 | Type II diabetes mellitus - poor control | Diabetes - Primary care |
| READ2:C10F900 | Type 2 diabetes mellitus without complication | Diabetes - Primary care |
| READ2:C10F911 | Type II diabetes mellitus without complication | Diabetes - Primary care |
| READ2:C10FA00 | Type 2 diabetes mellitus with mononeuropathy | Diabetes - Primary care |
| READ2:C10FA11 | Type II diabetes mellitus with mononeuropathy | Diabetes - Primary care |
| READ2:C10FB00 | Type 2 diabetes mellitus with polyneuropathy | Diabetes - Primary care |
| READ2:C10FB11 | Type II diabetes mellitus with polyneuropathy | Diabetes - Primary care |
| READ2:C10FC00 | Type 2 diabetes mellitus with nephropathy | Diabetes - Primary care |
| READ2:C10FD00 | Type 2 diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C10FD11 | Type II diabetes mellitus with hypoglycaemic coma | Diabetes - Primary care |
| READ2:C10FE00 | Type 2 diabetes mellitus with diabetic cataract | Diabetes - Primary care |
| READ2:C10FE11 | Type II diabetes mellitus with diabetic cataract | Diabetes - Primary care |
| READ2:C10FF00 | Type 2 diabetes mellitus with peripheral angiopathy | Diabetes - Primary care |
| READ2:C10FG00 | Type 2 diabetes mellitus with arthropathy | Diabetes - Primary care |
| READ2:C10FH00 | Type 2 diabetes mellitus with neuropathic arthropathy | Diabetes - Primary care |
| READ2:C10FJ00 | Insulin treated Type 2 diabetes mellitus | Diabetes - Primary care |
| READ2:C10FJ11 | Insulin treated Type II diabetes mellitus | Diabetes - Primary care |
| READ2:C10FK00 | Hyperosmolar non-ketotic state in type 2 diabetes mellitus | Diabetes - Primary care |
| READ2:C10FL00 | Type 2 diabetes mellitus with persistent proteinuria | Diabetes - Primary care |
| READ2:C10FL11 | Type II diabetes mellitus with persistent proteinuria | Diabetes - Primary care |
| READ2:C10FM00 | Type 2 diabetes mellitus with persistent microalbuminuria | Diabetes - Primary care |
| READ2:C10FM11 | Type II diabetes mellitus with persistent microalbuminuria | Diabetes - Primary care |
| READ2:C10FN00 | Type 2 diabetes mellitus with ketoacidosis | Diabetes - Primary care |
| READ2:C10FP00 | Type 2 diabetes mellitus with ketoacidotic coma | Diabetes - Primary care |
| READ2:C10FQ00 | Type 2 diabetes mellitus with exudative maculopathy | Diabetes - Primary care |
| READ2:C10FR00 | Type 2 diabetes mellitus with gastroparesis | Diabetes - Primary care |
| 10418 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 10692 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 12455 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 12640 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 12736 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 1407 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 1549 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 17545 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 17858 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 17859 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18143 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18209 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18219 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18230 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 18264 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18278 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18387 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 18390 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18425 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18496 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 18642 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 18683 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 18777 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 21983 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 22871 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 22884 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 24423 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 24458 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 24836 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 25591 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 25627 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 26054 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 30294 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 30323 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 32627 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 34268 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 34450 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 35288 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 35385 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 36633 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 37806 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 38161 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 39070 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 40682 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 40837 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 41049 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 42729 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 42762 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 42831 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 43227 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 43921 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 44779 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 44982 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 45913 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 45914 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 45919 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 46150 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 46301 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 46850 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 46917 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 47315 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 47321 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 47409 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 47582 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 47649 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 47650 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 47816 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 47954 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 48192 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 49074 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 49146 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 49554 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 49655 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 49869 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 49949 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 50225 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 50527 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 50813 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 51756 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 51957 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 53392 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 54008 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 54899 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 55075 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 55239 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 56268 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 57278 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 58604 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 59253 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 59725 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 60107 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 60208 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 60699 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 60796 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 61071 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 61344 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 61829 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 62107 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 62209 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 62352 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 62613 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 62674 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 63017 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 63690 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 64571 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 64668 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 65267 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 65704 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 66145 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 66872 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 66965 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 67905 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 68105 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 68390 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 69676 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 69993 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 70316 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 70766 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 758 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 85991 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 91646 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 91942 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 91943 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 93468 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 93727 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 93878 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 95343 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 95351 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 95992 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 96235 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 97446 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 97474 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 97894 (Med codes) | Type I diabetes mellitus (3) | Diabetes - Primary care |
| 98616 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| 98723 (Med codes) | Type II diabetes mellitus (4) | Diabetes - Primary care |
| ICD10:E10 | Insulin-dependent diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:E11 | Non-insulin-dependent diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:E12 | Malnutrition-related diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:E13 | Other specified diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:E14 | Unspecified diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:G590 | Diabetic mononeuropathy | Diabetes - Secondary care - Diagnoses |
| ICD10:G632 | Diabetic polyneuropathy | Diabetes - Secondary care - Diagnoses |
| ICD10:H280 | Diabetic cataract | Diabetes - Secondary care - Diagnoses |
| ICD10:H360 | Diabetic retinopathy | Diabetes - Secondary care - Diagnoses |
| ICD10:M142 | Diabetic arthropathy | Diabetes - Secondary care - Diagnoses |
| ICD10:N083 | Glomerular disorders in diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:O240 | Diabetes mellitus in pregnancy: Pre-existing diabetes mellitus, insulin-dependent | Diabetes - Secondary care - Diagnoses |
| ICD10:O241 | Diabetes mellitus in pregnancy: Pre-existing diabetes mellitus, non-insulin-dependent | Diabetes - Secondary care - Diagnoses |
| ICD10:O242 | Diabetes mellitus in pregnancy: Pre-existing malnutrition-related diabetes mellitus | Diabetes - Secondary care - Diagnoses |
| ICD10:O243 | Diabetes mellitus in pregnancy: Pre-existing diabetes mellitus, unspecified | Diabetes - Secondary care - Diagnoses |

## Source

HDR UK Phenotype Library record PH152 version 304, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH152/version/304/detail/)
