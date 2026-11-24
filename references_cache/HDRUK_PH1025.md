---
reference_id: "HDRUK:PH1025"
title: "Atrial Fibrillation"
database: "HDR UK Phenotype Library"
source_snapshot: "PH1025 version 2259"
content_type: "structured_record"
---

# HDRUK:PH1025  Atrial Fibrillation

**PH1025** version 2259 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH1025 |
| Version | 2259 |
| Name | Atrial Fibrillation |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Katherine I. Morley, Joshua Wallace , Spiros C. Denaxas, Ross J. Hunter, Riyaz S. Patel, Pablo Perel, Anoop D. Shah, Adam D. Timmis, Richard J. Schilling, Harry Hemingway |
| Collections | CALIBER |
| Coding systems | ICD10 codes; Read codes v2; OPCS4 codes; GPRD product codes |
| Data sources | HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/jwpp-y848 |
| Ontology | MONDO:0004981 atrial fibrillation |

## Definition

# Combining evidence across sources to define and date phenotypes The case definition for AF has three categories: * Historical: first recorded AF code indicates monitoring of an existing condition, or reference to a previous AF diagnosis. * Diagnosed: first record is a diagnosis code for AF; preference given to the earliest dated record rather than diagnosis source (i.e. no preference for primary versus secondary care). * Inferred: no diagnosis code is present, but the patient record includes a warfarin prescription in the absence of prior DVT or PE, or a digoxin prescription in the absence of HF. The phenotype algorithm incorporates these definitions in a hierarchical, mutually exclusive manner (see FIGURE). If the earliest recorded AF codes relate to a historical diagnosis or monitoring, the patient is in category 1 which precludes inclusion in other categories. If these codes are absent, then the presence of a coded diagnosis from primary or secondary care places a patient in category 2. Finally, in the absence of a coded diagnosis, a patient may be allocated to category 3, depending on the combination of prescriptions and diagnoses in their record. Otherwise a participant is treated as undiagnosed. ![Flow chart diagram illustrating the CALIBER phenotype algorithm for atrial fibrillation][images/af_flowchart.jpeg]

## Validation

EHR sources, aetiologic, prognostic

## Publications

- Steele AJ et al. Machine learning models in electronic health records can outperform conventional survival models for predicting patient mortality in coronary artery disease. PLoS One. 2018 Aug 31;13(8):e0202344. doi: 10.1371/journal.pone.0202344. eCollection 2018. PMID: 30169498
- Archangelidi O et al. Clinically recorded heart rate and incidence of 12 coronary, cardiac, cerebrovascular and peripheral arterial diseases in 233,970 men and women: A linked electronic health record study. Eur J Prev Cardiol. 2018 Sep;25(14):1485-1495. doi: 10.1177/2047487318785228. Epub 2018 Jul 2. PMID: 29966429
- Koudstaal S et al. Prognostic burden of heart failure recorded in primary care, acute hospital admissions, or both: a population-based linked electronic health record cohort study in 2.1 million people. Eur J Heart Fail. 2017 Sep;19(9):1119-1127. doi: 10.1002/ejhf.709. Epub 2016 Dec 23. PMID: 28008698
- Chung SC et al. Time spent at blood pressure target and the risk of death and cardiovascular diseases. PLoS One. 2018 Sep 5;13(9):e0202359. doi: 10.1371/journal.pone.0202359. eCollection 2018. PMID: 30183734
- Bell S et al. Association between clinically recorded alcohol consumption and initial presentation of 12 cardiovascular diseases: population based cohort study using linked health records. BMJ. 2017 Mar 22;356:j909. PMID: 28331015
- Pasea L et al. Personalising the decision for prolonged dual antiplatelet therapy: development, validation and potential impact of prognostic models for cardiovascular events and bleeding in myocardial infarction survivors. Eur Heart J. 2017 Apr 7;38(14):1048-1055. doi: 10.1093/eurheartj/ehw683. PMID: 28329300
- Shah AD et al. Neutrophil Counts and Initial Presentation of 12 Cardiovascular Diseases: A CALIBER Cohort Study. J Am Coll Cardiol. 2017 Mar 7;69(9):1160-1169. doi: 10.1016/j.jacc.2016.12.022. PMID: 28254179
- Asaria M et al. Using electronic health records to predict costs and outcomes in stable coronary artery disease. Heart. 2016 May 15;102(10):755-62. doi: 10.1136/heartjnl-2015-308850. Epub 2016 Feb 10. PMID: 26864674
- Daskalopoulou M et al. Depression as a Risk Factor for the Initial Presentation of Twelve Cardiac, Cerebrovascular, and Peripheral Arterial Diseases: Data Linkage Study of 1.9 Million Women and Men. PLoS One. 2016 Apr 22;11(4):e0153838. doi: 10.1371/journal.pone.0153838. eCollection 2016. PMID: 27105076
- Pujades-Rodriguez M et al. Associations between polymyalgia rheumatica and giant cell arteritis and 12 cardiovascular diseases. Heart. 2016 Mar;102(5):383-9. doi: 10.1136/heartjnl-2015-308514. Epub 2016 Jan 19. PMID: 26786818
- Pujades-Rodriguez M et al. Rheumatoid Arthritis and Incidence of Twelve Initial Presentations of Cardiovascular Disease: A Population Record-Linkage Cohort Study in England. PLoS One. 2016 Mar 15;11(3):e0151245. doi: 10.1371/journal.pone.0151245. eCollection 2016. PMID: 26978266
- Shah AD et al. Low eosinophil and low lymphocyte counts and the incidence of 12 cardiovascular diseases: a CALIBER cohort study. Open Heart. 2016 Sep 5;3(2):e000477. doi: 10.1136/openhrt-2016-000477. eCollection 2016. PMID: 27621833
- Timmis A et al. Prolonged dual antiplatelet therapy in stable coronary disease: comparative observational study of benefits and harms in unselected versus trial populations. BMJ. 2016 Jun 22;353:i3163. PMID: 27334486
- Walker S et al. Long-term healthcare use and costs in patients with stable coronary artery disease: a population-based cohort using linked health records (CALIBER). Eur Heart J Qual Care Clin Outcomes. 2016 Jan 20;2(2):125-140. doi: 10.1093/ehjqcco/qcw003. PMID: 27042338
- George J et al. How Does Cardiovascular Disease First Present in Women and Men? Incidence of 12 Cardiovascular Diseases in a Contemporary Cohort of 1,937,360 People. Circulation. 2015 Oct 6;132(14):1320-8. doi: 10.1161/CIRCULATIONAHA.114.013797. Epub 2015 Sep 1. PMID: 26330414
- Morley KI et al. Defining disease phenotypes using national linked electronic health records: a case study of atrial fibrillation. PLoS One. 2014 Nov 4;9(11):e110900. doi: 10.1371/journal.pone.0110900. eCollection 2014. PMID: 25369203
- Pujades-Rodriguez M et al. Heterogeneous associations between smoking and a wide range of initial presentations of cardiovascular disease in 1937360 people in England: lifetime risks and implications for risk prediction. Int J Epidemiol. 2015 Feb;44(1):129-41. doi: 10.1093/ije/dyu218. Epub 2014 Nov 20. PMID: 25416721
- Pujades-Rodriguez M et al. Socioeconomic deprivation and the incidence of 12 cardiovascular diseases in 1.9 million women and men: implications for risk prediction and prevention. PLoS One. 2014 Aug 21;9(8):e104671. doi: 10.1371/journal.pone.0104671. eCollection 2014. PMID: 25144739
- Rapsomaniki E et al. Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1.25 million people. Lancet. 2014 May 31;383(9932):1899-911. doi: 10.1016/S0140-6736(14)60685-1. PMID: 24881994
- Shah AD et al. Type 2 diabetes and incidence of cardiovascular diseases: a cohort study in 1.9 million people. Lancet Diabetes Endocrinol. 2015 Feb;3(2):105-13. doi: 10.1016/S2213-8587(14)70219-0. Epub 2014 Nov 11. PMID: 25466521
- Rapsomaniki E et al. Prognostic models for stable coronary artery disease based on electronic health record cohort of 102 023 patients. Eur Heart J. 2014 Apr;35(13):844-52. doi: 10.1093/eurheartj/eht533. Epub 2013 Dec 17. PMID: 24353280

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:3272 | ECG: atrial fibrillation | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:3273 | ECG: atrial flutter | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:793M100 | Perc transluminal ablation of atrial wall for atrial flutter | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:793M300 | Perc translum ablat conduct sys heart for atrial flutter NEC | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573.00 | Atrial fibrillation and flutter | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573000 | Atrial fibrillation | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573100 | Atrial flutter | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573200 | Paroxysmal atrial fibrillation | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573300 | Non-rheumatic atrial fibrillation | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573400 | Permanent atrial fibrillation | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573500 | Persistent atrial fibrillation | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:G573z00 | Atrial fibrillation and flutter NOS | File - Atrial Fibrillation - Primary Care - Diagnosis |
| READ2:14S4.00 | H/O: heart valve recipient | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:14T3.00 | H/O: artificial heart valve | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914.11 | Replacement of unspecified valve of heart | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914000 | Allograft replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914100 | Xenograft replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914200 | Prosthetic replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914211 | Edwards prosthetic replacement of valve of heart | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914212 | Starr prosthetic replacement of valve of heart | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:7914300 | Replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:SP00200 | Mechanical complication of heart valve prosthesis | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:SyuK611 | [X] Embolism from prosthetic heart valve | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:TB01200 | Implant of heart valve prosthesis + complication, no blame | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:ZV42200 | [V]Heart valve transplanted | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:ZV43300 | [V]Has artificial heart valve | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:ZV45H00 | [V]Presence of prosthetic heart valve | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:ZVu6e00 | [X]Presence of other heart valve replacement | File - Atrial Fibrillation - Primary Care - Heart Valve Procedure |
| READ2:14A8100 | H/O: Deep Vein Thrombosis | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:1JH..00 | Suspected deep vein thrombosis | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:8HTm.00 | Referral to deep vein thrombosis clinic | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801.00 | Deep vein phlebitis and thrombophlebitis of the leg | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801.12 | Deep vein thrombosis, leg | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801600 | Thrombophlebitis of the femoral vein | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801700 | Thrombophlebitis of the popliteal vein | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801B00 | Deep vein thrombophlebitis of the leg unspecified | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801C00 | Deep vein thrombosis of leg related to air travel | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801E00 | Deep vein thrombosis of leg related to intravenous drug use | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801F00 | Deep vein thrombosis of peroneal vein | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:G801z00 | Deep vein phlebitis and thrombophlebitis of the leg NOS | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:ZV12800 | [V] Personal history deep vein thrombosis | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:ZV12811 | [V] Personal history DVT- deep vein thrombosis | File - Atrial Fibrillation - Primary Care - Deep Vein Thrombosis |
| READ2:14AC.00 | H/O: pulmonary embolus | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:1JC..00 | Suspected pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:7A09300 | Open embolectomy of pulmonary artery | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:7A09311 | Trendelenburg pulmonary embolectomy | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:7A0A100 | Percutaneous transluminal embolectomy of pulmonary artery | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:G401.00 | Pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:G401.12 | Pulmonary embolus | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:G401000 | Post operative pulmonary embolus | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:G401100 | Recurrent pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L096400 | Pulmonary embolism following abortive pregnancy | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L43..00 | Obstetric pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L43..11 | Obstetric pulmonary embolus | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L430.00 | Obstetric air pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L431.00 | Amniotic fluid pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L431100 | Amniotic fluid pulmonary embolism - delivered | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L432.00 | Obstetric blood-clot pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L43z.00 | Obstetric pulmonary embolism NOS | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L43z100 | Obstetric pulmonary embolism NOS - delivered | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L43z400 | Obstetric pulmonary embolism NOS with postnatal complication | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:L43zz00 | Obstetric pulmonary embolism NOS | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| READ2:ZV12900 | [V] Personal history of pulmonary embolism | File - Atrial Fibrillation - Primary Care - Pulmonary Embolism |
| 13348 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 16366 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 1781 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 17965 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 20844 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 20944 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 2302 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 23078 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 2511 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 25238 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 27523 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 29282 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 30202 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 30203 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 31511 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 3181 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 31937 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 3286 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 33080 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 33274 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 33612 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 33675 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 33711 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34017 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34019 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34023 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34024 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34086 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34087 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34088 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34095 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34299 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34327 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34328 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34416 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34417 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34418 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34517 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34519 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34526 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34576 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34691 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34758 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34864 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34918 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 34948 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 36 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 36099 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 3705 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 38041 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 38044 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 39866 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 40143 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 40245 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 45 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 61 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 6262 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 792 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 833 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 8466 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 8467 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 94 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| 9522 (GPRD product codes) |  | File - Atrial Fibrillation - Primary Care - Medication |
| READ2:14N6.00 | H/O: cardiac surgery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:14S4.00 | H/O: heart valve recipient | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:14T3.00 | H/O: artificial heart valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7.90E+02 | Creation of conduit between heart atrium and ventricle NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7.90E+102 | Creation of conduit between right atrium and pulm artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7.90E+113 | Creation of Fontan conduit between right atrium & pulmon art | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7.90E+202 | Creation conduit between right ventricle and pulm artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7.90E+213 | Rastelli creation conduit between right ventricle/pulmon art | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7.93E+02 | Cardiotachygraphy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:79...00 | Heart operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:79...11 | Cardiac operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790..00 | Heart wall, septum and chamber operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7900 | Transplantation of heart and lung | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7900000 | Allotransplantation of heart and lung | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7900z00 | Transplantation of heart and lung NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901 | Other transplantation of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901000 | Allotransplantation of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901100 | Xenotransplantation of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901200 | Implantation of prosthetic heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901400 | Revision of implantation of prosthetic heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901500 | Revision of transplantation of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901y00 | Other specified other transplantation of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7901z00 | Other transplantation of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902 | Correction of tetralogy of Fallot | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902.11 | Repair of tetralogy of Fallot | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902000 | Correct Fallot tetralogy- valved right ventr outflow conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902100 | Correct Fallot tetralogy- right ventric outflow conduit NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902300 | Revision of correction of tetralogy of Fallot | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902400 | Repair of tetralogy of Fallot using transannular patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902500 | Repair of tetralogy of Fallot with absent pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902y00 | Other specified correction of tetralogy of Fallot | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7902z00 | Correction of tetralogy of Fallot NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903 | Atrial inversion ops for transposition of great vessels | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903.11 | Mustard interatrial tr venous return | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903.12 | Senning correction for transposition of great vessels | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903.13 | Atrial inversion operations for transposition of great art | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903000 | Atrium reconstruction atrial patch for transpos great vessel | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903100 | Atrium reconstruction atrial wall for transpos great vessels | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903y00 | Atrial inversion op for transposition of great vessels OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7903z00 | Atrial inversion op for transposition of great vessels NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7904 | Other correction of transposition of great vessels | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7904000 | Repositioning of transposed great vessels | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7904y00 | Other correction of transposition of great vessels OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7904z00 | Other correction of transposition of great vessels NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7905 | Correction of total anomalous pulmonary venous connection | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7905000 | Correct total anomal pulm venous connect to supracard vessel | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7905100 | Correct total anomal pulm venous connect to coronary sinus | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7905z00 | Correction total anomalous pulmonary venous connection NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906 | Closure of defect of atrioventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906.11 | Repair of defect of the atrioventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906000 | Close defect atrioventric septum using dual prosthetic patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906100 | Close defect atrioventric septum using prosthetic patch NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906111 | Repair defect atrioventricular septum prosthetic patch NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906200 | Closure defect atrioventricular septum using tissue graft | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906300 | Closure of persistent ostium primum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906400 | Primary closure of defect of atrioventricular septum NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906500 | Revision of closure of defect of atrioventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906y00 | Other specified closure of defect of atrioventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7906z00 | Closure of defect of atrioventricular septum NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907 | Closure of defect of interatrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907.11 | Repair of defect of interatrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907000 | Closure defect of interatrial septum using prosthetic patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907011 | Repair defect of interatrial septum using prosthetic patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907100 | Closure defect of interatrial septum using pericardial patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907200 | Closure defect of interatrial septum using tissue graft NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907300 | Primary closure of defect of interatrial septum NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907400 | Revision of closure of defect of interatrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907y00 | Other specified closure of defect of interatrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7907z00 | Closure of defect of interatrial septum NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908 | Closure of defect of interventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908.11 | Repair of defect of interventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908000 | Close defect interventricular septum using prosthetic patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908100 | Close defect interventricular septum using pericardial patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908111 | Repair defect interventricular septum us pericardial patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908200 | Close defect interventricular septum using tissue graft NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908300 | Primary closure of defect of interventricular septum NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908311 | Primary repair of defect of interventricular septum NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908511 | Repair of multiple interventricular septal defects | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908y00 | Other specified closure of defect of interventricular septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7908z00 | Closure of defect of interventricular septum NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909 | Closure of defect of unspecified septum of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909.11 | Repair of defect of unspecified septum of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909000 | Closure of defect of heart septum using prosthetic patch NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909100 | Closure defect of heart septum using pericardial patch NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909300 | Primary closure of defect of septum of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909y00 | Other specified closure of defect unspecified heart septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7909z00 | Closure of defect of unspecified septum of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790A.00 | Other open operations on septum of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790A000 | Open enlargement of defect of atrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790A100 | Open atrial septostomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790A111 | Atrial septostomy NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790A300 | Atrial septectomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790A600 | Surgical atrial septation | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Ay00 | Other specified other open operation on septum of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Az00 | Other open operation on septum of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790B.00 | Closed operations on septum of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790B000 | Closed enlargement of defect of atrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790B011 | Blalock creation of defect in atrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790B012 | Hanlon creation of defect in atrial septum | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790B100 | Closed atrial septostomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790By00 | Other specified closed operation on septum of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Bz00 | Closed operation on septum of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790D.00 | Creation of valved cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790D200 | Creation of valved conduit between right ventr +pulm artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790D400 | Revision of valved cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790D700 | Replacement of valved cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790E.00 | Creation of other cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790E500 | Revision of cardiac conduit NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Ey00 | Other specified creation of other cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Ez00 | Creation of other cardiac conduit NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790F.00 | Refashioning of atrium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790F000 | Correction of persistent sinus venosus | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790F100 | Correction of partial anomalous pulmonary venous drainage | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790G.00 | Other operations on wall of atrium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790G000 | Excision of lesion of atrium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790G100 | Repair of atrium NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Gy00 | Other specified operation on wall of atrium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790H000 | Excision of lesion of wall of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790H100 | Biopsy of lesion of wall of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790H200 | Repair of wall of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790H300 | Revascularisation of wall of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790H400 | Partial left ventriculectomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790H500 | Cardiomyoplasty | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Hy00 | Other specified operation on wall of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Hz00 | Operation on wall of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790J.00 | Other repair of transposition of great arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790J000 | Repositioning of transposed great arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790K.00 | Repair of double outlet ventricle | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790K200 | Repair of double outlet right ventricle | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790M.00 | Repair of univentricular heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790M100 | Total cavopulmonary connection with lateral atrial tunnel | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790M400 | Biventricular repair of hypoplastic left heart syndrome | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790M500 | Takedown of total cavopulmonary connection | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790My00 | Other specified repair of univentricular heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790N.00 | Other operations on ventricles of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790N000 | Relief of right ventricular outflow tract obstruction | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790N200 | Repair of right ventricular aneurysm | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790N300 | Repair of left ventricular aneurysm | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790N400 | Relief of left ventricular outflow tract obstruction | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790N500 | Myectomy of left ventricular outflow tract | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:790Ny00 | Other specified other operations on ventricles of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791..00 | Valves of heart and adjacent structures operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910 | Plastic repair of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910.11 | Mitral valvuloplasty | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910.12 | Replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910000 | Allograft replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910100 | Xenograft replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910200 | Prosthetic replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910211 | Bjork-Shiley prosthetic replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910212 | Bjork-Shiley prosthetic replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910213 | Carpentier prosthetic replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910214 | Edwards prosthetic replacement of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910300 | Replacement of mitral valve NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910400 | Mitral valvuloplasty NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910411 | Mitral valve repair NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910y00 | Other specified plastic repair of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7910z00 | Plastic repair of mitral valve NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911 | Plastic repair of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911.11 | Aortic valvuloplasty | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911.12 | Replacement of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911000 | Allograft replacement of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911100 | Xenograft replacement of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911200 | Prosthetic replacement of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911300 | Replacement of aortic valve NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911400 | Aortic valvuloplasty NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911411 | Aortic valve repair NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911y00 | Other specified plastic repair of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7911z00 | Plastic repair of aortic valve NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912 | Plastic repair of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912.11 | Replacement of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912.12 | Tricuspid valvuloplasty | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912000 | Allograft replacement of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912100 | Xenograft replacement of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912200 | Prosthetic replacement of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912300 | Replacement of tricuspid valve NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912511 | Tricuspid valve repair NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912y00 | Other specified plastic repair of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7912z00 | Plastic repair of tricuspid valve NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913 | Plastic repair of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913.11 | Pulmonary valvuloplasty | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913.12 | Replacement of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913000 | Allograft replacement of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913100 | Xenograft replacement of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913200 | Prosthetic replacement of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913300 | Replacement of pulmonary valve NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913400 | Pulmonary valvuloplasty NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913411 | Pulmonary valve repair NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913y00 | Other specified plastic repair of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7913z00 | Plastic repair of pulmonary valve NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914 | Plastic repair of unspecified valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914.11 | Replacement of unspecified valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914000 | Allograft replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914100 | Xenograft replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914200 | Prosthetic replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914211 | Edwards prosthetic replacement of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914212 | Starr prosthetic replacement of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914300 | Replacement of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914400 | Valvuloplasty of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914500 | Truncal valve repair | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914y00 | Other specified plastic repair of unspecified valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7914z00 | Plastic repair of unspecified valve of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7915 | Revision of plastic repair of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7915000 | Revision of plastic repair of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7915100 | Revision of plastic repair of aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7915200 | Revision of plastic repair of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7915300 | Revision of plastic repair of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7915y00 | Other specified revision of plastic repair of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916 | Open incision of heart valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916.11 | Open heart valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916000 | Open mitral valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916100 | Open aortic valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916200 | Open tricuspid valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916300 | Open pulmonary valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916y00 | Other specified open specified incision of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916z00 | Open incision of valve of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7916z11 | Heart valvotomy NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917 | Closed incision of heart valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917.11 | Closed heart valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917000 | Closed mitral valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917100 | Closed aortic valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917300 | Closed pulmonary valvotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917311 | Brock pulmonary valvulotomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7917z00 | Closed incision of valve of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918 | Other open operations on valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918000 | Annuloplasty of mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918100 | Annuloplasty of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918111 | De Vega tricuspid annuloplasty | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918200 | Annuloplasty of valve of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918300 | Excision of vegetations of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918400 | Closure of tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918500 | Closure of pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918y00 | Other specified other open operation on valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7918z00 | Other open operation on valve of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791A.00 | Remove obstruction from structure adjacent to valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791A000 | Infundibulectomy of heart using patch | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791A100 | Infundibulectomy of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791A200 | Repair of subaortic stenosis | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791A300 | Repair of supraaortic stenosis | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791B.00 | Other operations on structure adjacent to valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791B000 | Operation on papillary muscle | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791B100 | Operation on chordae tendineae | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791B200 | Operations on mitral subvalvar apparatus | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791B400 | Closure of aortic sinus of Valsalva fistula | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791B500 | Repair of aortic sinus of Valsalva aneurysm | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791By00 | Operation on structure adjacent to heart valve OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791Bz00 | Operation on structure adjacent to valve of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791C.00 | Operations on aortic root | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791C200 | Aortic root replacement using homograft | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791C300 | Aortic root replacement using mechanical prosthesis | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791C400 | Aortic root replacement | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791C500 | Aortoventriculoplasty with pulmonary valve autograft | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791Cy00 | Other specified operations on aortic root | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791D.00 | Excision of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791D000 | Tricuspid valvectomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791D100 | Pulmonary valvectomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791y.00 | Heart valve or adjacent structures operations OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:791z.00 | Heart valve and adjacent structures operations NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792..00 | Coronary artery operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792..11 | Coronary artery bypass graft operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920 | Saphenous vein graft replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920.11 | Saphenous vein graft bypass of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920000 | Saphenous vein graft replacement of one coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920100 | Saphenous vein graft replacement of two coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920200 | Saphenous vein graft replacement of three coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920300 | Saphenous vein graft replacement of four+ coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920y00 | Saphenous vein graft replacement of coronary artery OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7920z00 | Saphenous vein graft replacement coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921 | Other autograft replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921.11 | Other autograft bypass of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921000 | Autograft replacement of one coronary artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921100 | Autograft replacement of two coronary arteries NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921200 | Autograft replacement of three coronary arteries NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921300 | Autograft replacement of four of more coronary arteries NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921y00 | Other autograft replacement of coronary artery OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7921z00 | Other autograft replacement of coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922 | Allograft replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922.11 | Allograft bypass of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922000 | Allograft replacement of one coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922100 | Allograft replacement of two coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922200 | Allograft replacement of three coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922300 | Allograft replacement of four or more coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922y00 | Other specified allograft replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7922z00 | Allograft replacement of coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923 | Prosthetic replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923.11 | Prosthetic bypass of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923000 | Prosthetic replacement of one coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923100 | Prosthetic replacement of two coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923200 | Prosthetic replacement of three coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923300 | Prosthetic replacement of four or more coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7923z00 | Prosthetic replacement of coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924 | Revision of bypass for coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924000 | Revision of bypass for one coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924100 | Revision of bypass for two coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924200 | Revision of bypass for three coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924500 | Revision of implantation of thoracic artery into heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924y00 | Other specified revision of bypass for coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7924z00 | Revision of bypass for coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925 | Connection of mammary artery to coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925.11 | Creation of bypass from mammary artery to coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925000 | Double anastomosis of mammary arteries to coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925011 | LIMA sequential anastomosis | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925012 | RIMA sequential anastomosis | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925100 | Double implant of mammary arteries into coronary arteries | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925200 | Single anast mammary art to left ant descend coronary art | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925400 | Single implantation of mammary artery into coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925y00 | Connection of mammary artery to coronary artery OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7925z00 | Connection of mammary artery to coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7926 | Connection of other thoracic artery to coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7926000 | Double anastom thoracic arteries to coronary arteries NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7926200 | Single anastomosis of thoracic artery to coronary artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7926300 | Single implantation thoracic artery into coronary artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7926z00 | Connection of other thoracic artery to coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927 | Other open operations on coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927000 | Repair of arteriovenous fistula of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927100 | Repair of aneurysm of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927200 | Transection of muscle bridge of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927300 | Transposition of coronary artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927400 | Exploration of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927500 | Open angioplasty of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927y00 | Other specified other open operation on coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7927z00 | Other open operation on coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792B.00 | Repair of coronary artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792B000 | Endarterectomy of coronary artery NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792B100 | Repair of rupture of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792B200 | Repair of arteriovenous malformation of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792By00 | Other specified repair of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792Bz00 | Repair of coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792C.00 | Other replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792C000 | Replacement of coronary arteries using multiple methods | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792Cy00 | Other specified replacement of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792Cz00 | Replacement of coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792D.00 | Other bypass of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792Dy00 | Other specified other bypass of coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792Dz00 | Other bypass of coronary artery NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792y.00 | Other specified operations on coronary artery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:792z.00 | Coronary artery operations NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930 | Open operations on conducting system of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930000 | Open ablation of atrioventricular node | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930100 | Epicardial excision of rhythmogenic focus | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930200 | Endocardial excision of rhythmogenic focus | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930300 | Open division of accessory pathway within heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930400 | Open division of conducting system of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930y00 | Other specified open operation on conducting system of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7930z00 | Open operation on conducting system of heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7931 | Other incision of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7931000 | Inspection of valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7931100 | Exploration of heart NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7931200 | Cardiotomy NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932 | Other open operations on heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932000 | Ligation of sinus of Valsalva | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932100 | Open chest massage of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932111 | Cardiac massage - open | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932200 | Open removal of cardiac thrombus | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932400 | Resection of heart tumour | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932500 | Repair of traumatic injury of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7932z00 | Open operation on heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7933 | Transluminal heart assist operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7933000 | Transluminal insertion of pulsation balloon into aorta | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7933300 | Transluminal removal of heart assist system | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7933z00 | Transluminal heart assist operation NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934 | Other therapeutic transluminal operations on heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934000 | Percutaneous transluminal ablation of atrioventricular node | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934100 | Percut transluminal ablation of heart conducting system NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934200 | Transluminal radiofreq ablation heart conducting system NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934400 | Percutaneous transluminal ablation of accessory pathway | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934500 | Percutaneous transluminal ablation of atrial wall | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934600 | Percutaneous transluminal ablation of ventricular wall | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934800 | Percutaneous transluminal ablation of atrial wall NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934y00 | Other therapeutic transluminal operation on heart OS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7934z00 | Other therapeutic transluminal operation on heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7936900 | Implantation of intravenous atrial overdrive pacemaker | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7936A00 | Implant intravenous pacemaker for atrial fibrillation | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793A.00 | Excision of pericardium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793A.11 | Pericardiectomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793A000 | Excision of lesion of pericardium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793A100 | Delorme pericardiectomy | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793Az00 | Excision of pericardium NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793E.00 | Other operations on heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793Ey00 | Other specified other operation on heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793Ez00 | Other operation on heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793H.00 | Transluminal operations on cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793Hy00 | Other specified transluminal operations on cardiac conduit | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793L.00 | Open heart assist operations | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793L000 | Open implantation of ventricular assist device | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793L100 | Open removal of ventricular assist device | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793M.00 | Therapeutic transluminal operations on heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793M000 | Perc translum ablat pulmon vein to lft atrium conduct system | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793M100 | Perc transluminal ablation of atrial wall for atrial flutter | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793M200 | Percutaneous transluminal internal cardioversion NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793M300 | Perc translum ablat conduct sys heart for atrial flutter NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:793Mz00 | Therapeutic transluminal operations on heart NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:79y..00 | Other specified operations on heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:79z..00 | Heart operations NOS | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H.11 | Cardioversion and stimulation | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H.12 | Direct current cardiac shock | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H.13 | Defibrillation | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H000 | Direct current cardioversion | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H100 | External cardioversion NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H111 | External electrode cardioversion | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H200 | Internal electrode cardioversion | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H300 | Electrical sinus rhythm conversion | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H400 | Electrical operative cardiac stimulation | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7L1H800 | Chemical cardioversion | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7M36000 | Cardiopulmonary bypass | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N4..00 | [SO]Heart, arteries and veins | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N40.00 | [SO]Valve of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N40000 | [SO]Mitral valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N40100 | [SO]Aortic valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N40200 | [SO]Tricuspid valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N40300 | [SO]Pulmonary valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N41400 | [SO]Pericardium | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N41500 | [SO]Atrium of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:7N41600 | [SO]Ventricle of heart | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:8735 | Operative resuscitation NEC | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:8H2O.00 | Admit cardiothoracic emergency | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:9b8B.00 | Cardiothoracic surgery | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:P512.00 | Corrected great vessel transposition | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV15100 | [V]Personal history of heart or great vessel operation | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV42100 | [V]Heart transplanted | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV42200 | [V]Heart valve transplanted | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV43300 | [V]Has artificial heart valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV45800 | [V]Presence of coronary angioplasty implant and graft | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV45H00 | [V]Presence of prosthetic heart valve | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV45K00 | [V]Presence of coronary artery bypass graft | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV45K11 | [V]Presence of coronary artery bypass graft - CABG | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:ZV59600 | [V]Heart and lungs transplant status | File - Atrial Fibrillation - Primary Care - Procedure |
| READ2:14AN.00 | H/O: atrial fibrillation | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:14AR.00 | History of atrial flutter | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:212R.00 | Atrial fibrillation resolved | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:662S.00 | Atrial fibrillation monitoring | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:6A9..00 | Atrial fibrillation annual review | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9Os..00 | Atrial fibrillation monitoring administration | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9Os0.00 | Atrial fibrillation monitoring first letter | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9Os1.00 | Atrial fibrillation monitoring second letter | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9Os2.00 | Atrial fibrillation monitoring third letter | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9Os3.00 | Atrial fibrillation monitoring verbal invite | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9Os4.00 | Atrial fibrillation monitoring telephone invite | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9hF..00 | Exception reporting: atrial fibrillation quality indicators | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| READ2:9hF1.00 | Excepted from atrial fibrillation qual indic: Inform dissent | File - Atrial Fibrillation - Primary Care - Prevalent Diagnoses or Possible Diagnoses |
| ICD10:I48 | Atrial fibrillation and flutter | File - Atrial Fibrillation - Secondary Care - Diagnosis |
| ICD10:I801 | Phlebitis and thrombophlebitis of femoral vein | File - Atrial Fibrillation - Secondary Care - Deep Vein Thrombosis |
| ICD10:I802 | Phlebitis and thrombophlebitis of other deep vessels of lower extremities | File - Atrial Fibrillation - Secondary Care - Deep Vein Thrombosis |
| ICD10:I803 | Phlebitis and thrombophlebitis of lower extremities, unspecified | File - Atrial Fibrillation - Secondary Care - Deep Vein Thrombosis |
| ICD10:I26 | Pulmonary embolism | File - Atrial Fibrillation - Secondary Care - Pulmonary Embolism |
| READ2:14S4.00 | H/O: heart valve recipient | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:14T3.00 | H/O: artificial heart valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914.11 | Replacement of unspecified valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914000 | Allograft replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914100 | Xenograft replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914200 | Prosthetic replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914211 | Edwards prosthetic replacement of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914212 | Starr prosthetic replacement of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:7914300 | Replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:SP00200 | Mechanical complication of heart valve prosthesis | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:SyuK611 | [X] Embolism from prosthetic heart valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:TB01200 | Implant of heart valve prosthesis + complication, no blame | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:ZV42200 | [V]Heart valve transplanted | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:ZV43300 | [V]Has artificial heart valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:ZV45H00 | [V]Presence of prosthetic heart valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| READ2:ZVu6e00 | [X]Presence of other heart valve replacement | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K01 | Transplantation of heart and lung | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K011 | Allotransplantation of heart and lung | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K012 | Revision of transplantation of heart and lung | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K018 | Other specified transplantation of heart and lung | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K019 | Unspecified transplantation of heart and lung | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K02 | Other transplantation of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K021 | Allotransplantation of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K022 | Xenotransplantation of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K023 | Implantation of prosthetic heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K024 | Piggyback transplantation of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K025 | Revision of implantation of prosthetic heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K026 | Revision of transplantation of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K028 | Other specified other transplantation of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K029 | Unspecified other transplantation of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K04 | Repair of tetralogy of Fallot | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K041 | Repair of tetralogy of Fallot using valved right ventricular outflow conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K042 | Repair of tetralogy of Fallot using right ventricular outflow conduit NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K043 | Repair of tetralogy of Fallot using transannular patch | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K044 | Revision of repair of tetralogy of Fallot | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K045 | Repair of tetralogy of Fallot with absent pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K046 | Repair of Fallot-type pulmonary atresia with aortopulmonary collaterals | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K048 | Other specified repair of tetralogy of Fallot | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K049 | Unspecified repair of tetralogy of Fallot | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K05 | Atrial inversion operations for transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K051 | Reconstruction of atrium using atrial patch for transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K052 | Reconstruction of atrium using atrial wall for transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K058 | Other specified atrial inversion operations for transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K059 | Unspecified atrial inversion operations for transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K06 | Other repair of transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K061 | Repositioning of transposed great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K062 | Left ventricle to aorta tunnel with right ventricle to pulmonary trunk direct anastomosis | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K063 | Left ventricle to aorta tunnel with right ventricle to pulmonary artery valved conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K064 | Atrial inversion and repositioning of transposed great artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K068 | Other specified other repair of transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K069 | Unspecified other repair of transposition of great arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K07 | Correction of total anomalous pulmonary venous connection | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K071 | Correction of total anomalous pulmonary venous connection to supracardiac vessel | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K072 | Correction of total anomalous pulmonary venous connection to coronary sinus | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K073 | Correction of total anomalous pulmonary venous connection to infradiaphragmatic vessel | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K078 | Other specified correction of total anomalous pulmonary venous connection | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K079 | Unspecified correction of total anomalous pulmonary venous connection | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K08 | Repair of double outlet ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K081 | Repair of double outlet right ventricle with intraventricular tunnel | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K082 | Repair of Fallot-type double outlet right ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K083 | Repair of double outlet right ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K084 | Repair of double outlet left ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K088 | Other specified repair of double outlet ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K089 | Unspecified repair of double outlet ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K09 | Repair of defect of atrioventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K091 | Repair of defect of atrioventricular septum using dual prosthetic patches | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K092 | Repair of defect of atrioventricular septum using prosthetic patch NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K093 | Repair of defect of atrioventricular septum using tissue graft | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K094 | Repair of persistent ostium primum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K095 | Primary repair of defect of atrioventricular septum NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K096 | Revision of repair of defect of atrioventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K098 | Other specified repair of defect of atrioventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K099 | Unspecified repair of defect of atrioventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K10 | Repair of defect of interatrial septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K101 | Repair of defect of interatrial septum using prosthetic patch | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K102 | Repair of defect of interatrial septum using pericardial patch | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K103 | Repair of defect of interatrial septum using tissue graft NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K104 | Primary repair of defect of interatrial septum NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K105 | Revision of repair of defect of interatrial septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K108 | Other specified repair of defect of interatrial septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K109 | Unspecified repair of defect of interatrial septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K11 | Repair of defect of interventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K111 | Repair of defect of interventricular septum using prosthetic patch | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K112 | Repair of defect of interventricular septum using pericardial patch | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K113 | Repair of defect of interventricular septum using tissue graft NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K114 | Primary repair of defect of interventricular septum NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K115 | Revision of repair of defect of interventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K116 | Repair of multiple interventricular septal defects | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K117 | Repair of interventricular septal defect using intraoperative transluminal prosthesis | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K118 | Other specified repair of defect of interventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K119 | Unspecified repair of defect of interventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K12 | Repair of defect of unspecified septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K121 | Repair of defect of septum of heart using prosthetic patch NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K122 | Repair of defect of septum of heart using pericardial patch NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K123 | Repair of defect of septum of heart using tissue graft NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K124 | Primary repair of defect of septum of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K125 | Revision of repair of septum of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K128 | Other specified repair of defect of unspecified septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K129 | Unspecified repair of defect of unspecified septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K14 | Other open operations on septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K141 | Open enlargement of defect of atrial septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K142 | Open atrial septostomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K143 | Atrial septectomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K144 | Surgical atrial septation | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K145 | Open enlargement of defect of interventricular septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K148 | Other specified other open operations on septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K149 | Unspecified other open operations on septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K15 | Closed operations on septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K151 | Closed enlargement of defect of atrial septum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K152 | Closed atrial septostomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K158 | Other specified closed operations on septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K159 | Unspecified closed operations on septum of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K17 | Repair of univentricular heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K171 | Total cavopulmonary connection with extracardiac inferior caval vein to pulmonary artery conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K172 | Total cavopulmonary connection with lateral atrial tunnel | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K173 | Aortopulmonary reconstruction with systemic to pulmonary arterial shunt | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K174 | Aortopulmonary reconstruction with right ventricle to pulmonary arterial valveless conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K175 | Biventricular repair of hypoplastic left heart syndrome | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K176 | Takedown of total cavopulmonary connection | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K177 | Conversion of atrial pulmonary anastomosis to total pulmonary connection | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K178 | Other specified repair of univentricular heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K179 | Unspecified repair of univentricular heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K18 | Creation of valved cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K181 | Creation of valved conduit between atrium and ventricle of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K182 | Creation of valved conduit between right atrium and pulmonary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K183 | Creation of valved conduit between right ventricle of heart and pulmonary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K184 | Creation of valved conduit between left ventricle of heart and aorta | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K185 | Revision of valved cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K186 | Creation of valved conduit between left ventricle of heart and pulmonary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K187 | Replacement of valved cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K188 | Other specified creation of valved cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K189 | Unspecified creation of valved cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K19 | Creation of other cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K191 | Creation of conduit between atrium and ventricle of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K192 | Creation of conduit between right atrium and pulmonary artery NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K193 | Creation of conduit between right ventricle of heart and pulmonary artery NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K194 | Creation of conduit between right ventricle of heart and vena cava | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K195 | Creation of conduit between left ventricle of heart and aorta NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K196 | Revision of cardiac conduit NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K198 | Other specified creation of other cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K199 | Unspecified creation of other cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K20 | Refashioning of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K201 | Correction of persistent sinus venosus | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K202 | Correction of partial anomalous pulmonary venous drainage | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K203 | Repair of cor triatriatum | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K204 | Repair of coronary sinus abnormality | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K208 | Other specified refashioning of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K209 | Unspecified refashioning of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K22 | Other operations on wall of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K221 | Excision of lesion of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K222 | Repair of atrium NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K228 | Other specified other operations on wall of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K229 | Unspecified other operations on wall of atrium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K23 | Other operations of wall of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K231 | Excision of lesion of wall of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K232 | Biopsy of lesion of wall of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K233 | Repair of wall of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K234 | Revascularisation of wall of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K235 | Partial left ventriculectomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K236 | Cardiomyoplasty | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K238 | Other specified other operations of wall of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K239 | Unspecified other operations of wall of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K24 | Other operations on ventricles of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K241 | Relief of right ventricular outflow tract obstruction | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K242 | Repair of double chambered right ventricle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K243 | Repair of right ventricular aneurysm | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K244 | Repair of left ventricular aneurysm | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K245 | Relief of left ventricular outflow tract obstruction | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K246 | Myectomy of left ventricular outflow tract | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K247 | Myotomy of left ventricular outflow tract | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K248 | Other specified other operations on ventricles of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K249 | Unspecified other operations on ventricles of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K25 | Plastic repair of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K251 | Allograft replacement of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K252 | Xenograft replacement of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K253 | Prosthetic replacement of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K254 | Replacement of mitral valve NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K255 | Mitral valve repair NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K258 | Other specified plastic repair of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K259 | Unspecified plastic repair of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K26 | Plastic repair of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K261 | Allograft replacement of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K262 | Xenograft replacement of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K263 | Prosthetic replacement of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K264 | Replacement of aortic valve NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K265 | Aortic valve repair NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K268 | Other specified plastic repair of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K269 | Unspecified plastic repair of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K27 | Plastic repair of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K271 | Allograft replacement of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K272 | Xenograft replacement of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K273 | Prosthetic replacement of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K274 | Replacement of tricuspid valve NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K275 | Repositioning of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K276 | Tricuspid valve repair NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K278 | Other specified plastic repair of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K279 | Unspecified plastic repair of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K28 | Plastic repair of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K281 | Allograft replacement of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K282 | Xenograft replacement of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K283 | Prosthetic replacement of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K284 | Replacement of pulmonary valve NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K285 | Pulmonary valve repair NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K288 | Other specified plastic repair of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K289 | Unspecified plastic repair of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K29 | Plastic repair of unspecified valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K291 | Allograft replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K292 | Xenograft replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K293 | Prosthetic replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K294 | Replacement of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K295 | Repair of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K296 | Truncal valve repair | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K297 | Replacement of truncal valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K298 | Other specified plastic repair of unspecified valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K299 | Unspecified plastic repair of unspecified valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K30 | Revision of plastic repair of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K301 | Revision of plastic repair of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K302 | Revision of plastic repair of aortic valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K303 | Revision of plastic repair of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K304 | Revision of plastic repair of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K305 | Revision of plastic repair of truncal valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K308 | Other specified revision of plastic repair of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K309 | Unspecified revision of plastic repair of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K31 | Open incision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K311 | Open mitral valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K312 | Open aortic valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K313 | Open tricuspid valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K314 | Open pulmonary valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K315 | Open truncal valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K318 | Other specified open incision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K319 | Unspecified open incision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K32 | Closed incision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K321 | Closed mitral valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K322 | Closed aortic valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K323 | Closed tricuspid valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K324 | Closed pulmonary valvotomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K328 | Other specified closed incision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K329 | Unspecified closed incision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K33 | Operations on aortic root | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K331 | Aortic root replacement using pulmonary valve autograft with right ventricle to pulmonary artery valved conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K332 | Aortic root replacement using pulmonary valve autograft with right ventricle to pulmonary artery valved conduit and aortoventriculoplasty | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K333 | Aortic root replacement using homograft | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K334 | Aortic root replacement using mechanical prosthesis | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K335 | Aortic root replacement NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K336 | Aortoventriculoplasty with pulmonary valve autograft | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K338 | Other specified operations on aortic root | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K339 | Unspecified operations on aortic root | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K34 | Other open operations on valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K341 | Annuloplasty of mitral valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K342 | Annuloplasty of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K343 | Annuloplasty of valve of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K344 | Excision of vegetations of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K345 | Closure of tricuspid valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K346 | Closure of pulmonary valve | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K348 | Other specified other open operations on valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K349 | Unspecified other open operations on valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K36 | Excision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K361 | Tricuspid valvectomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K362 | Pulmonary valvectomy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K368 | Other specified excision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K369 | Unspecified excision of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K37 | Removal of obstruction from structure adjacent to valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K371 | Infundibulectomy of heart using patch | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K372 | Infundibulectomy of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K373 | Repair of subaortic stenosis | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K374 | Repair of supra-aortic stenosis | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K375 | Excision of supramitral ring | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K376 | Aortoventriculoplasty | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K378 | Other specified removal of obstruction from structure adjacent to valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K379 | Unspecified removal of obstruction from structure adjacent to valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K38 | Other operations on structure adjacent to valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K381 | Operations on papillary muscle | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K382 | Operations on chordae tendineae | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K383 | Operations on mitral subvalvar apparatus | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K384 | Closure of aorto-left ventricular tunnel | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K385 | Closure of aortic sinus of Valsalva fistula | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K386 | Repair of aortic sinus of Valsalva aneurysm | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K388 | Other specified other operations on structure adjacent to valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K389 | Unspecified other operations on structure adjacent to valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K40 | Saphenous vein graft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K401 | Saphenous vein graft replacement of one coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K402 | Saphenous vein graft replacement of two coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K403 | Saphenous vein graft replacement of three coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K404 | Saphenous vein graft replacement of four or more coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K408 | Other specified saphenous vein graft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K409 | Unspecified saphenous vein graft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K41 | Other autograft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K411 | Autograft replacement of one coronary artery NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K412 | Autograft replacement of two coronary arteries NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K413 | Autograft replacement of three coronary arteries NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K414 | Autograft replacement of four or more coronary arteries NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K418 | Other specified other autograft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K419 | Unspecified other autograft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K42 | Allograft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K421 | Allograft replacement of one coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K422 | Allograft replacement of two coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K423 | Allograft replacement of three coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K424 | Allograft replacement of four or more coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K428 | Other specified allograft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K429 | Unspecified allograft replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K43 | Prosthetic replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K431 | Prosthetic replacement of one coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K432 | Prosthetic replacement of two coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K433 | Prosthetic replacement of three coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K434 | Prosthetic replacement of four or more coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K438 | Other specified prosthetic replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K439 | Unspecified prosthetic replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K44 | Other replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K441 | Replacement of coronary arteries using multiple methods | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K442 | Revision of replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K448 | Other specified other replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K449 | Unspecified other replacement of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K45 | Connection of thoracic artery to coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K451 | Double anastomosis of mammary arteries to coronary arteries | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K452 | Double anastomosis of thoracic arteries to coronary arteries NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K453 | Anastomosis of mammary artery to left anterior descending coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K454 | Anastomosis of mammary artery to coronary artery NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K455 | Anastomosis of thoracic artery to coronary artery NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K456 | Revision of connection of thoracic artery to coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K458 | Other specified connection of thoracic artery to coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K459 | Unspecified connection of thoracic artery to coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K46 | Other bypass of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K461 | Double implantation of mammary arteries into heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K462 | Double implantation of thoracic arteries into heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K463 | Implantation of mammary artery into heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K464 | Implantation of thoracic artery into heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K465 | Revision of implantation of thoracic artery into heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K468 | Other specified other bypass of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K469 | Unspecified other bypass of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K47 | Repair of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K471 | Endarterectomy of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K472 | Repair of arteriovenous fistula of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K473 | Repair of aneurysm of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K474 | Repair of rupture of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K475 | Repair of arteriovenous malformation of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K478 | Other specified repair of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K479 | Unspecified repair of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K48 | Other open operations on coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K481 | Transection of muscle bridge of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K482 | Transposition of coronary artery NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K483 | Open angioplasty of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K484 | Exploration of coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K488 | Other specified other open operations on coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K489 | Unspecified other open operations on coronary artery | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K52 | Open operations on conducting system of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K521 | Open ablation of atrioventricular node | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K522 | Epicardial excision of rhythmogenic focus | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K523 | Endocardial excision of rhythmogenic focus | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K524 | Open division of accessory pathway within heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K525 | Open division of conducting system of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K526 | Incision of tissue in atria | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K528 | Other specified open operations on conducting system of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K529 | Unspecified open operations on conducting system of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K53 | Other incision of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K531 | Inspection of valve of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K532 | Exploration of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K538 | Other specified other incision of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K539 | Unspecified other incision of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K54 | Open heart assist operations | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K541 | Open implantation of ventricular assist device | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K542 | Open removal of ventricular assist device | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K548 | Other specified open heart assist operations | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K549 | Unspecified open heart assist operations | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K55 | Other open operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K551 | Ligation of sinus of Valsalva | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K552 | Open chest massage of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K553 | Open removal of cardiac thrombus | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K554 | Open removal of cardiac vegetations NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K555 | Resection of heart tumour | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K556 | Repair of traumatic injury of heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K558 | Other specified other open operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K559 | Unspecified other open operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K56 | Transluminal heart assist operations | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K561 | Transluminal insertion of pulsation balloon into aorta | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K562 | Transluminal insertion of heart assist system NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K563 | Transluminal maintenance of heart assist system | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K564 | Transluminal removal of heart assist system | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K568 | Other specified transluminal heart assist operations | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K569 | Unspecified transluminal heart assist operations | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K57 | Other therapeutic transluminal operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K571 | Percutaneous transluminal ablation of atrioventricular node | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K572 | Percutaneous transluminal ablation of conducting system of heart NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K573 | Percutaneous transluminal removal of foreign body from heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K574 | Percutaneous transluminal ablation of accessory pathway | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K575 | Percutaneous transluminal ablation of atrial wall NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K576 | Percutaneous transluminal ablation of ventricular wall | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K577 | Percutaneous transluminal ablation for congenital heart malformation | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K578 | Other specified other therapeutic transluminal operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K579 | Unspecified other therapeutic transluminal operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K62 | Therapeutic transluminal operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K621 | Percutaneous transluminal ablation of pulmonary vein to left atrium conducting system | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K622 | Percutaneous transluminal ablation of atrial wall for atrial flutter | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K623 | Percutaneous transluminal ablation of conducting system of heart for atrial flutter NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K624 | Percutaneous transluminal internal cardioversion NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K66 | Other operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K661 | Cardiotachygraphy | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K668 | Other specified other operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K669 | Unspecified other operations on heart | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K67 | Excision of pericardium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K671 | Excision of lesion of pericardium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K678 | Other specified excision of pericardium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K679 | Unspecified excision of pericardium | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K76 | Transluminal operations on cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K761 | Percutaneous transluminal balloon dilation of cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K768 | Other specified transluminal operations on cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:K769 | Unspecified transluminal operations on cardiac conduit | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:X501 | Direct current cardioversion | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:X502 | External cardioversion NEC | File - Atrial Fibrillation - Secondary Care - Procedure |
| OPCS4:X504 | External ventricular defibrillation | File - Atrial Fibrillation - Secondary Care - Procedure |

## Source

HDR UK Phenotype Library record PH1025 version 2259, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH1025/version/2259/detail/)
