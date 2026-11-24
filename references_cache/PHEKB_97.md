---
reference_id: "PHEKB:97"
title: "Abdominal Aortic Aneurysm ( AAA )"
database: "PheKB"
content_type: "structured_record"
---

# PHEKB:97  Abdominal Aortic Aneurysm ( AAA )

**Abdominal Aortic Aneurysm ( AAA )** — phenotype algorithm page from PheKB (node 97).

## Record

| Field | Value |
|---|---|
| Phenotype ID | 97 |
| Date Created | Tuesday, June 5, 2012 |
| Status | Final |
| Authors | Kenneth Borthwick |
| Institution | Geisinger |
| Network Associations | eMERGE |
| Owner Phenotyping Groups | eMERGE Geisinger Group |
| Structured data | ICD9; CPT |
| Data Source/clinical domain | observations |
| Phenotype Attributes | CPT Codes; ICD 9 Codes; Vital Signs |
| Type of Phenotype | Disease or Syndrome |
| Gender | Female; Male |
| Age | Adult; Geriatric |

## Description

The algorithm uses Structured Query Language to identify AAA cases, controls, and excludes from the Electronic Medical Record. AAA cases were defined as meeting at least one of three criteria: had a AAA repair procedure (Case Type 1), had at least one vascular clinic encounter with a diagnosis of ruptured AAA (Case Type 2), or had at least two vascular clinic encounters with a diagnosis of unruptured AAA (Case Type 3). AAA controls must be neither excludes nor cases, had an encounter within the past 5 years, and never had a diagnosis of ICD9 code 441.3, 441.4, or 441.9 from any department. Patients were excluded if any exclusion diagnosis existed in the medical record, were younger than 40 or older than 89, were neither a Case Type 1 nor Case Type 2 and haven’t had an encounter within the past 5 years, or were not a case and had an ICD9 code diagnosis of 441.* at some point in the medical history.

## Files

- AAA_Flowchart_v20120815.pdf
- Geisinger_AAA_Algorithm_Pseudocode_Final20120815.pdf
- Geisinger_AAA_Medications_v20120815.xlsx
- Geisinger_AAA_ClinicalVariablesForGWAS_V20120920.xlsx

## Attachment: AAA_Flowchart_v20120815.pdf

Yes
GeM cohort: consented, not
withdrawn, with blood
Exclusion
diagnosis
40 ≤ Age* < 90
*at encounter
No
Yes
Exclude
Control
Case: Type 3
Case: Type 1
Case: Type 2
AAA repair code Yes AAA Repair Code
Last encounter < 5 y
No
Yes
No No
≥ 2 unruptured
AAA Dx by
Vasc. Dept.
ICD-9 code: 441.*
Yes
No
No
Yes
AAA rupture
Dx by
Vasc. Dept.
Yes
No
Exclude
Type 1
Exclude
Type 2
Exclude
Type 3a
Exclude
Type 3b

## Attachment: Geisinger_AAA_Algorithm_Pseudocode_Final20120815.pdf

Geisinger Health System
Last Updated: 08/15/2012 Page 1

GEISINGER ALGORITHM FOR IDENTIFYING PATIENTS WITH AN
ABDOMINAL AORTIC ANEURYSM

CASE TYPE 1:
Subject
 is not an Exclude Type 1
 is not an Exclude Type 2
AND
 has undergone one or more AAA repair procedures based on the following CPT codes:
 34800 (Endovascular repair of infrarenal abdominal aortic aneurysm or dissection; using aorto‐
aortic tube prosthesis)
 34802 (Endovascular repair of infrarenal abdominal aortic aneurysm or dissection; using modular
bifurcated prosthesis (1 docking limb))
 34803 (Endovascular repair of infrarenal abdominal aortic aneurysm or dissection; using modular
bifurcated prosthesis (2 docking limbs))
 34804 (Endovascular repair of infrarenal abdominal aortic aneurysm or dissection; using unibody
bifurcated prosthesis)
 34805 (Endovascular repair of infrarenal abdominal aortic aneurysm or dissection; using aorto‐
uniiliac or aorto‐unifemoral prosthesis)
 34830 (Open repair of infrarenal aortic aneurysm or dissection, plus repair of associated arterial
trauma, following unsuccessful endovascular repair; tube prosthesis)
 34831 (Open repair of infrarenal aortic aneurysm or dissection, plus repair of associated arterial
trauma, following unsuccessful endovascular repair; aorto‐bi‐iliac prosthesis)
 34832 (Open repair of infrarenal aortic aneurysm or dissection, plus repair of associated arterial
trauma, following unsuccessful endovascular repair; aorto‐bifemoral prosthesis)
 35081 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for aneurysm, pseudoaneurysm, and associated occlusive
disease, abdominal aorta)
 35082 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for ruptured aneurysm, abdominal aorta)
 35091 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for aneurysm, pseudoaneurysm, and associated occlusive
disease, abdominal aorta involving visceral vessels (mesenteric, celiac, renal))
 35092 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for ruptured aneurysm, abdominal aorta involving visceral
vessels (mesenteric, celiac, renal))
 35102 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for aneurysm, pseudoaneurysm, and associated occlusive
disease, abdominal aorta involving iliac vessels (common, hypogastric, external))
Geisinger Health System
Last Updated: 08/15/2012 Page 2

 35103 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for ruptured aneurysm, abdominal aorta involving iliac
vessels (common, hypogastric, external))
 35131 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for aneurysm, pseudoaneurysm, and associated occlusive
disease, iliac artery (common, hypogastric, external))
 35132 (Direct repair of aneurysm, pseudoaneurysm, or excision (partial or total) and graft
insertion, with or without patch graft; for ruptured aneurysm, iliac artery (common, hypogastric,
external))
*Note that for Case Type 1, the patient’s most recent encounter does not need to be within the past 5 years.

CASE TYPE 2:
Subject
 is not a Case Type 1
 is not an Exclude Type 1
 is not an Exclude Type 2
AND
 has had one or more visits to the vascular clinic/lab/department that resulted in the following
diagnosis:
 441.3 (Abdominal aortic aneurysm, ruptured)
*Note that for Case Type 2, the patient’s most recent encounter does not need to be within the past 5 years.

CASE TYPE 3:
Subject
 is not a Case Type 1
 is not a Case Type 2
 is not an Exclude Type 1
 is not an Exclude Type 2
AND
 has had two or more visits to the vascular clinic/lab/department that resulted in a diagnosis of:
 441.4 (Abdominal aortic aneurysm, without mention of rupture)
AND
 Subject’s most recent encounter was within the past 5 years.

Geisinger Health System
Last Updated: 08/15/2012 Page 3

CONTROLS:
Subject
 does not qualify for exclusion
AND
 does not qualify for as a Case
AND
 most recent encounter was within the past 5 years.
AND

 has never had any of the following ICD9 Code diagnoses*:
 441.3 (Abdominal aortic aneurysm, ruptured)
 441.4 (Abdominal aortic aneurysm, without mention of rupture)
 441.9 (Aortic aneurysm of unspecified site without mention of rupture)
*This condition applies to all departments within the system and at any point in the patient’s medical
history.

EXCLUDES:
EXLUDE TYPE 1:
Exclude if subject has any of the following ICD9 Code diagnoses:

 759.82 (Marfan Syndrome)
 756.83 (Ehlers‐Danlos Syndrome)
 441.1 (Thoracic Aneurysm, ruptured)
 441.2 (Thoracic Aneurysm without mention of rupture)
 441.7 (Thoracoabdominal aneurysm without mention of rupture)
 443.2 (Other arterial dissection)
 437.5 (Moyamoya Disease)
 447.8 (Fibromuscular Dysplasia)

EXLUDE TYPE 2:
Exclude if subject was younger than 40 or older than 89 years of age at the time of encounter.

Geisinger Health System
Last Updated: 08/15/2012 Page 4

EXLUDE TYPE 3:
Exclude if subject
TYPE 3a
 Is not a Case Type 1
OR
 Is not a Case Type 2
AND
 Has not had an encounter in the last 5 years.
OR
TYPE 3b
 Is not a Case 1, 2 or 3
AND
 Has ICD9 code 441.[x]

## Suggested citation

Kenneth Borthwick. Geisinger. Abdominal Aortic Aneurysm ( AAA ). PheKB; 2012 Available from: https://phekb.org/phenotype/97 Log in to post comments Gerard Tromp Updates 2012-08-15 Wed, 2012-08-15 18:24 The Pseudocode and Flowchart files were updated today (2012-08-15). No substantive changes -- Content did not change . Added notations on the excludes. Indicated where they occur on the flow chart. Excludes have the following functions Type 1: Remove known confounders, i.e., diagnoses that lead to generalize aorta/artery problems that can include AAA. Type 2: Remove very old (HIPAA) and very young who will not be informative since the age-at -onset is 65 +/- 13 years. Type 3a: Remove individuals who might be cases, but who have insufficient data to vaildate Type 3b: Remove individuals who have had the suspicion of aortic aneurysm at any time so that they cannot contaminate the controls. Log in to post comments Jim Linneman Questions Thu, 2012-09-13 11:51 1. Missing ICD9 codes for coronary stenosis and unintentional weight loss. Can you please add these to the data dictionary? 2. At what timepoint do you want INRs (within how many ? days prior to an anticoagulaent or antiplatelet medication mention)? Log in to post comments Gerard Tromp Update 2012-09-24 Mon, 2012-09-24 16:40 1. Missing codes in revised data dictionary. 2. Removed the condition. Simply collect INR regardless. Log in to post comments Gerard Tromp Update 2012-09-24 Mon, 2012-09-24 16:40 1. Missing codes in revised data dictionary. 2. Removed the condition. Simply collect INR regardless. Log in to post comments Gerard Tromp Updated Data dictionary Mon, 2012-09-24 16:43 1. Reordered the ICD-9 codes to match the order of static variables 2. Removed duplicate (HIV) 3. Added missing ICD-9 codes (see response to Jim Linneman above) 4. Removed pretreatment clause for INR in repeating lab values Log in to post comments Gerard Tromp Updated Data dictionary Mon, 2012-09-24 16:43 1. Reordered the ICD-9 codes to match the order of static variables 2. Removed duplicate (HIV) 3. Added missing ICD-9 codes (see response to Jim Linneman above) 4. Removed pretreatment clause for INR in repeating lab values Log in to post comments Gerard Tromp Vascular Surgery in pseudocode and flowchart Mon, 2012-09-24 19:36 It should be noted that vascular surgery can be replaced by whatever specialty treats some or all of the abdominal aortic aneurysm cases. At some sites that might be Interventional Radiology, at othe sites both. The Vascular Surgery should be treated as a placeholder for the collection of specialty clinics/service lines that treat AAA at the site. Log in to post comments

## Source

PheKB phenotype page 97. PDF algorithm documents are transcribed by text extraction; journal articles and non-PDF attachments are listed only. PheKB states no licence for its content.

[PheKB record](https://phekb.org/node/97)
