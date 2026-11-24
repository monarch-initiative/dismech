---
reference_id: "HDRUK:PH1028"
title: "Heart Failure (fatal/non-fatal)"
database: "HDR UK Phenotype Library"
source_snapshot: "PH1028 version 2265"
content_type: "structured_record"
---

# HDRUK:PH1028  Heart Failure (fatal/non-fatal)

**PH1028** version 2265 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH1028 |
| Version | 2265 |
| Name | Heart Failure (fatal/non-fatal) |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Koudstaal, S; Pujades-Rodriguez, M; Denaxas, S; Gho, JM; Shah, AD; Yu, N; Patel, RS; Gale, CP; Hoes, AW; Cleland, JG; Asselbergs, FW; Hemingway, H |
| Collections | CALIBER |
| Coding systems | ICD10 codes; Read codes v2; ICD9 codes |
| Data sources | HES Admitted Patient Care data for CPRD GOLD; mortality data (ONS) |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/hmf7-em52 |
| Ontology | MONDO:0005252 heart failure |

## Definition

# Combining evidence across sources to define and date phenotypes We took the first occurring diagnosis code in primary, secondary care or the death registry to define the date, and clinical setting, of diagnosis. A prevalent case was defined as existing at or before the date of baseline; and incident case was defined as the new occurrence of a heart failure diagnosis code among people who, at baseline, did not have any previous diagnosis codes. ![Flow chart diagram illustrating the CALIBER phenotype algorithm for heart failure.][images/hf_flowchart.png] For identifying prevalent cases in primary care, we used a broader list of Read terms in addition to the case definition. While these terms alone did not provide sufficient certainty to identify incident cases, using them to exclude prevalent cases ensured that we removed any patient that had a historic or suspected HF diagnosis from the analysis.

## Validation

EHR sources, Clinical, prognostic, Risk factors, casenote review, genetic, cross-country, prognostic, aetiologic

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
| READ2:1O1..00 | Heart failure confirmed | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:662W.00 | Heart failure annual review | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:662p.00 | Heart failure 6 month review | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:8B29.00 | Cardiac failure therapy | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:8H2S.00 | Admit heart failure emergency | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:9Or0.00 | Heart failure review completed | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G1yz100 | Rheumatic left ventricular failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G210.00 | Malignant hypertensive heart disease | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G210000 | Malignant hypertensive heart disease without CCF | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G210100 | Malignant hypertensive heart disease with CCF | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G211100 | Benign hypertensive heart disease with CCF | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G21z100 | Hypertensive heart disease NOS with CCF | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G230.00 | Malignant hypertensive heart and renal disease | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G232.00 | Hypertensive heart&renal dis wth (congestive) heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G234.00 | Hyperten heart&renal dis+both(congestv)heart and renal fail | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G400.00 | Acute cor pulmonale | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G41z.11 | Chronic cor pulmonale | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G554000 | Congestive cardiomyopathy | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G554011 | Congestive obstructive cardiomyopathy | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G58..00 | Heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G58..11 | Cardiac failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580.00 | Congestive heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580.11 | Congestive cardiac failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580.12 | Right heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580.13 | Right ventricular failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580.14 | Biventricular failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580000 | Acute congestive heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580100 | Chronic congestive heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580200 | Decompensated cardiac failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580300 | Compensated cardiac failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G580400 | Congestive heart failure due to valvular disease | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G581.00 | Left ventricular failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G581.11 | Asthma - cardiac | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G581.13 | Impaired left ventricular function | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G581000 | Acute left ventricular failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G582.00 | Acute heart failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G58z.00 | Heart failure Not Otherwise Specified | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G58z.12 | Cardiac failure Not Otherwise Specified | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G5yy900 | Left ventricular systolic dysfunction | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:G5yyA00 | Left ventricular diastolic dysfunction | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:R2y1000 | [D]Cardiorespiratory failure | File - Heart Failure - Primary Care - Incident - Diagnosis |
| READ2:585f.00 | Echocardiogram shows left ventricular systolic dysfunction | File - Heart Failure - Primary Care - Incident - Abnormal Echocardiogram Findings |
| READ2:585g.00 | Echocardiogram shows left ventricular diastolic dysfunction | File - Heart Failure - Primary Care - Incident - Abnormal Echocardiogram Findings |
| READ2:14A6.00 | H/O: heart failure | File - Heart Failure - Primary Care - Prevalent |
| READ2:14AM.00 | H/O: Heart failure in last year | File - Heart Failure - Primary Care - Prevalent |
| READ2:1736 | Paroxysmal nocturnal dyspnoea | File - Heart Failure - Primary Care - Prevalent |
| READ2:1J60.00 | Suspected heart failure | File - Heart Failure - Primary Care - Prevalent |
| READ2:23E1.00 | O/E - pulmonary oedema | File - Heart Failure - Primary Care - Prevalent |
| READ2:388D.00 | New York Heart Assoc classification heart failure symptoms | File - Heart Failure - Primary Care - Prevalent |
| READ2:662T.00 | Congestive heart failure monitoring | File - Heart Failure - Primary Care - Prevalent |
| READ2:662f.00 | New York Heart Association classification - class I | File - Heart Failure - Primary Care - Prevalent |
| READ2:662g.00 | New York Heart Association classification - class II | File - Heart Failure - Primary Care - Prevalent |
| READ2:662h.00 | New York Heart Association classification - class III | File - Heart Failure - Primary Care - Prevalent |
| READ2:662i.00 | New York Heart Association classification - class IV | File - Heart Failure - Primary Care - Prevalent |
| READ2:679X.00 | Heart failure education | File - Heart Failure - Primary Care - Prevalent |
| READ2:8CL3.00 | Heart failure care plan discussed with patient | File - Heart Failure - Primary Care - Prevalent |
| READ2:8HBE.00 | Heart failure follow-up | File - Heart Failure - Primary Care - Prevalent |
| READ2:8HHz.00 | Referral to heart failure exercise programme | File - Heart Failure - Primary Care - Prevalent |
| READ2:8Hg8.00 | Discharge from practice nurse heart failure clinic | File - Heart Failure - Primary Care - Prevalent |
| READ2:8Hk0.00 | Referred to heart failure education group | File - Heart Failure - Primary Care - Prevalent |
| READ2:9N0k.00 | Seen in heart failure clinic | File - Heart Failure - Primary Care - Prevalent |
| READ2:9N2p.00 | Seen by community heart failure nurse | File - Heart Failure - Primary Care - Prevalent |
| READ2:9N4s.00 | Did not attend practice nurse heart failure clinic | File - Heart Failure - Primary Care - Prevalent |
| READ2:9N4w.00 | Did not attend heart failure clinic | File - Heart Failure - Primary Care - Prevalent |
| READ2:9N6T.00 | Referred by heart failure nurse specialist | File - Heart Failure - Primary Care - Prevalent |
| READ2:9On..00 | Left ventricular dysfunction monitoring administration | File - Heart Failure - Primary Care - Prevalent |
| READ2:9On0.00 | Left ventricular dysfunction monitoring first letter | File - Heart Failure - Primary Care - Prevalent |
| READ2:9On1.00 | Left ventricular dysfunction monitoring second letter | File - Heart Failure - Primary Care - Prevalent |
| READ2:9On2.00 | Left ventricular dysfunction monitoring third letter | File - Heart Failure - Primary Care - Prevalent |
| READ2:9On3.00 | Left ventricular dysfunction monitoring verbal invite | File - Heart Failure - Primary Care - Prevalent |
| READ2:9On4.00 | Left ventricular dysfunction monitoring telephone invite | File - Heart Failure - Primary Care - Prevalent |
| READ2:9Or..00 | Heart failure monitoring administration | File - Heart Failure - Primary Care - Prevalent |
| READ2:9Or1.00 | Heart failure monitoring telephone invite | File - Heart Failure - Primary Care - Prevalent |
| READ2:9Or2.00 | Heart failure monitoring verbal invite | File - Heart Failure - Primary Care - Prevalent |
| READ2:9Or3.00 | Heart failure monitoring first letter | File - Heart Failure - Primary Care - Prevalent |
| READ2:9Or4.00 | Heart failure monitoring second letter | File - Heart Failure - Primary Care - Prevalent |
| READ2:9Or5.00 | Heart failure monitoring third letter | File - Heart Failure - Primary Care - Prevalent |
| READ2:9h1..00 | Exception reporting: LVD quality indicators | File - Heart Failure - Primary Care - Prevalent |
| READ2:9h11.00 | Excepted from LVD quality indicators: Patient unsuitable | File - Heart Failure - Primary Care - Prevalent |
| READ2:9h12.00 | Excepted from LVD quality indicators: Informed dissent | File - Heart Failure - Primary Care - Prevalent |
| READ2:9hH..00 | Exception reporting: heart failure quality indicators | File - Heart Failure - Primary Care - Prevalent |
| READ2:9hH0.00 | Excepted heart failure quality indicators: Patient unsuitabl | File - Heart Failure - Primary Care - Prevalent |
| READ2:9hH1.00 | Excepted heart failure quality indicators: Informed dissent | File - Heart Failure - Primary Care - Prevalent |
| READ2:G581.12 | Pulmonary oedema - acute | File - Heart Failure - Primary Care - Prevalent |
| READ2:G58z.11 | Weak heart | File - Heart Failure - Primary Care - Prevalent |
| READ2:H54..00 | Pulmonary congestion and hypostasis | File - Heart Failure - Primary Care - Prevalent |
| READ2:H541.00 | Pulmonary congestion | File - Heart Failure - Primary Care - Prevalent |
| READ2:H541000 | Chronic pulmonary oedema | File - Heart Failure - Primary Care - Prevalent |
| READ2:H541z00 | Pulmonary oedema NOS | File - Heart Failure - Primary Care - Prevalent |
| READ2:H54z.00 | Pulmonary congestion and hypostasis NOS | File - Heart Failure - Primary Care - Prevalent |
| READ2:H584.00 | Acute pulmonary oedema unspecified | File - Heart Failure - Primary Care - Prevalent |
| READ2:H584z00 | Acute pulmonary oedema NOS | File - Heart Failure - Primary Care - Prevalent |
| READ2:ZRad.00 | New York Heart Assoc classification heart failure symptoms | File - Heart Failure - Primary Care - Prevalent |
| ICD10:I11.0 | Hypertensive heart disease with (congestive) heart failure | File - Coronary Heart Disease - Secondary Care |
| ICD10:I13.0 | Hypertensive heart and renal disease with (congestive) heart failure | File - Coronary Heart Disease - Secondary Care |
| ICD10:I32.2 | Hypertensive heart and renal disease with both (congestive) heart failure and renal failure | File - Coronary Heart Disease - Secondary Care |
| ICD10:I50.0 | Congestive heart failure | File - Coronary Heart Disease - Secondary Care |
| ICD10:I50.1 | Left ventricular heart failure | File - Coronary Heart Disease - Secondary Care |
| ICD10:I50.9 | Heart failure, unspecified | File - Coronary Heart Disease - Secondary Care |
| ICD10:I11.0 | Hypertensive heart disease with (congestive) heart failure | File - Coronary Heart Disease - Death |
| ICD10:I13.0 | Hypertensive heart and renal disease with (congestive) heart failure | File - Coronary Heart Disease - Death |
| ICD10:I32.2 | Hypertensive heart and renal disease with both (congestive) heart failure and renal failure | File - Coronary Heart Disease - Death |
| ICD10:I50.0 | Congestive heart failure | File - Coronary Heart Disease - Death |
| ICD10:I50.1 | Left ventricular heart failure | File - Coronary Heart Disease - Death |
| ICD10:I50.9 | Heart failure, unspecified | File - Coronary Heart Disease - Death |
| ICD9CM:428 | Congestive heart failure, unspecified | File - Coronary Heart Disease - Death |
| ICD9CM:428.1 | Left heart failure | File - Coronary Heart Disease - Death |
| ICD9CM:428.9 | Heart failure, unspecified | File - Coronary Heart Disease - Death |

## Source

HDR UK Phenotype Library record PH1028 version 2265, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH1028/version/2265/detail/)
