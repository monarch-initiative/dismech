---
reference_id: "HDRUK:PH1928"
title: "Epilepsy (all) (and incident epilepsy with incidence date)"
database: "HDR UK Phenotype Library"
source_snapshot: "PH1928 version 4530"
content_type: "structured_record"
---

# HDRUK:PH1928  Epilepsy (all) (and incident epilepsy with incidence date)

**PH1928** version 4530 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH1928 |
| Version | 4530 |
| Name | Epilepsy (all) (and incident epilepsy with incidence date) |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kathryn J. Bush, Beata Fonferko-Shadrach, Huw A. Strafford, Arron S. Lacey, Andrew Kingston, Rhys H. Thomas, Sheena E. Ramsay, William O Pickrell |
| Coding systems | ICD10 codes; Read codes v2; Med codes; SNOMED CT codes; PROD codes; BNF codes; ICD9 codes; dm+d codes |
| Data sources | Hospital Episode Statistics Admitted Patient Care; CPRD GOLD; CPRD Aurum; Welsh Longitudinal General Practice Dataset (WLGP) - Welsh Primary Care; Patient Episode Dataset for Wales (PEDW) |
| Sex | Both |
| DOI | https://doi.org/10.48533/4qbk-3b07 |
| Ontology | MONDO:0005027 epilepsy |

## Definition

This algorithm combines primary care and secondary care data in the UK to acurately identify cohorts with epilepsy.

The algorithm may be applied in primary care or hospital data alone, but the highest sensitivity algorithms include both data sets.

Epilepsy incidence dates should be calculated as a further step, once the case has been established.

Note that we have also included lists of codes that we have identified and excluded from our lists.

**References:**

This work builds on that previously done by:

Fonferko-Shadrach B, Lacey AS, White CP, Powell HWR, Sawhney IMS, Lyons RA, Smith PEM, Kerr MP, Rees MI, Pickrell WO. Validating epilepsy diagnoses in routinely collected data. Seizure. 2017 Nov;52:195-198. doi: 10.1016/j.seizure.2017.10.008. Epub 2017 Oct 13. PMID: 29059611; PMCID: PMC5703030.

## Implementation

**Assertaining cohorts with epilepsy**

In order to best assertain adult (\>\\\\\=16yrs) cohorts of individuals with epilepsy we would reccomend that the algorithm is applied using the following methods.

This method combines prescribing data with epilepsy codes. Note that there are different types of codes used to define epilepsy contained here. Note also that genetic syndromes with associated epilepsy are included as 'epilepsy diagnostic codes', due to their high sensitivity for epilepsy when used in combination with anti-seizure medications. These code lists should be re-visited if you intend to use the diagnostic codes without anti-seizure medications.

Note that the linked validation paper also includes multiple alternative methods and code combinations.

**Recommended algorithm for adults \>\\\=16 years:** 2 anti-seizure medication prescriptions in 6 months from the attached lists ***AND*** an epilepsy code (any type) in ***EITHER*** primary care or hospital data, within +/- 12 months

**Reccomended algorithm for children \\\<16 years:** an epilepsy code (diagnostic only) in ***EITHER*** primary care or hospital data

**Assertaining epilepsy incidence date**

Electronic prescribing in the UK was introduced from 1985 onwards. Therefore, by definition no individual can meet the algorithm until after 1985. The majority of practices did not introduce electronic prescribing until 1990 onwards.

Therefore we would recommend that in cases identified by the algorithm, the earliest dates is taken of: First diagnostic epilepsy code in primary care, first diagnostic epilepsy code date in hospital data, first prescription of 2 anti-seizure medications in 6 months.

Note that if you do not do this, and use only the date at which the algorithm is first met, you risk misclassification of onset - this risk should be considered even if you are only using more recent data - as a failure to identify the original onset date can lead to later misclassification.

## Validation

This work has been validated in Welsh SAIL data (Read codes and ICD 10) against clinical data from hospital records. Publication pending.

The study cohort comprised of 6875 adults (3009 with epilepsy and 3866 with alternative neurological diagnosis) with linkage to SAIL primary-care and hospital data. The optimal algorithm for ascertaining epilepsy cohorts combined primary-care and hospital data and included: \>2 anti-seizure medication codes in 6-months, and an epilepsy or seizure code within +/-12 months. This ascertained 2687 epilepsy cases with a sensitivity of 89.3%, specificity 98.8%, positive predictive value (PPV) 98.3% and F1 score 0.94. The code types used had a statistically significant impact upon algorithm outcome metrics.

All other code lists are generated from the equivalent codes in other data sets. CPRD codes were extracted from the browser in in July 2024.

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:1473. | H/O: epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:1B1W. | Transient epileptic amnesia | Epilepsy diagnosis codes: primary care |
| READ2:1O30. | Epilepsy confirmed | Epilepsy diagnosis codes: primary care |
| READ2:667B. | Nocturnal epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:94F1. | SUDEP - sudden unexpected death in epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:C3151 | MELAS | Epilepsy diagnosis codes: primary care |
| READ2:C3272 | Niemann-Pick disease | Epilepsy diagnosis codes: primary care |
| READ2:EMISNQGL2 | GLUT1 deficiency syndrome | Epilepsy diagnosis codes: primary care |
| READ2:EMISR4QPA1 | Partial epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:Eu052-2 | [X]Schizophrenia-like psychosis in epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:Eu05212 | [X]Schizophrenia-like psychosis in epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:Eu05y-1 | [X]Epileptic psychosis NOS | Epilepsy diagnosis codes: primary care |
| READ2:Eu05y11 | [X]Epileptic psychosis NOS | Epilepsy diagnosis codes: primary care |
| READ2:Eu06013 | [X]Limbic epilepsy personality | Epilepsy diagnosis codes: primary care |
| READ2:Eu803 | Acquired epileptic aphasia | Epilepsy diagnosis codes: primary care |
| READ2:Eu80300 | [X]Acquired aphasia with epilepsy [Landau - Kleffner] | Epilepsy diagnosis codes: primary care |
| READ2:Eu842 | Rett syndrome | Epilepsy diagnosis codes: primary care |
| READ2:Eu84200 | Rett syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F0352 | Rasmussen syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F035200 | Rasmussen syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F1010 | Janksy-Bielschowsky disease (CLN2) | Epilepsy diagnosis codes: primary care |
| READ2:F1011 | Kufs Disease | Epilepsy diagnosis codes: primary care |
| READ2:F1012 | Batten's disease | Epilepsy diagnosis codes: primary care |
| READ2:F1021 | Cerebral degeneration in Niemann-Pick disease | Epilepsy diagnosis codes: primary care |
| READ2:F10y0 | Alper's disease | Epilepsy diagnosis codes: primary care |
| READ2:F1306 | Aicardi Goutieres syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F130600 | Aicardi Goutieres syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F1321 | Progressive myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F132100 | Progressive myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F132111 | Unverricht - Lundborg disease | Epilepsy diagnosis codes: primary care |
| READ2:F1322 | Myoclonic encepahlopathy | Epilepsy diagnosis codes: primary care |
| READ2:F132200 | Myoclonic encephalopathy | Epilepsy diagnosis codes: primary care |
| READ2:F1422 | Dyssynergia cerebellaris myoclonica | Epilepsy diagnosis codes: primary care |
| READ2:F142200 | Dyssynergia cerebellaris myoclonica | Epilepsy diagnosis codes: primary care |
| READ2:F25.. | Epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250. | Generalised nonconvulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2500 | Petit mal (minor) epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250000 | Petit mal (minor) epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250011 | Epileptic absences | Epilepsy diagnosis codes: primary care |
| READ2:F2501 | Pykno-epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250100 | Pykno-epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2502 | Epileptic seizures - atonic | Epilepsy diagnosis codes: primary care |
| READ2:F250200 | Epileptic seizures - atonic | Epilepsy diagnosis codes: primary care |
| READ2:F2503 | Epileptic seizures - akinetic | Epilepsy diagnosis codes: primary care |
| READ2:F250300 | Epileptic seizures - akinetic | Epilepsy diagnosis codes: primary care |
| READ2:F2504 | Juvenile absence epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250400 | Juvenile absence epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2505 | Lennox-Gastaut syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F250500 | Lennox-Gastaut syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F250y | Other specified generalised nonconvulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250y00 | Other specified generalised nonconvulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F250z | Generalised nonconvulsive epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F250z00 | Generalised nonconvulsive epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F251. | Generalised convulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251.00 | Generalised convulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2510 | Grand mal (major) epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251000 | Grand mal (major) epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251011 | Tonic-clonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2511 | Neonatal myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251100 | Neonatal myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251111 | Otohara syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F2512 | Epileptic seizures - clonic | Epilepsy diagnosis codes: primary care |
| READ2:F251200 | Epileptic seizures - clonic | Epilepsy diagnosis codes: primary care |
| READ2:F2513 | Epileptic seizures - myoclonic | Epilepsy diagnosis codes: primary care |
| READ2:F251300 | Epileptic seizures - myoclonic | Epilepsy diagnosis codes: primary care |
| READ2:F2514 | Epileptic seizures - tonic | Epilepsy diagnosis codes: primary care |
| READ2:F251400 | Epileptic seizures - tonic | Epilepsy diagnosis codes: primary care |
| READ2:F2515 | Tonic-clonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251500 | Tonic-clonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2516 | Grand mal seizure | Epilepsy diagnosis codes: primary care |
| READ2:F251600 | Grand mal seizure | Epilepsy diagnosis codes: primary care |
| READ2:F251y | Other specified generalised convulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251y00 | Other specified generalised convulsive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F251z | Generalised convulsive epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F251z00 | Generalised convulsive epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F252. | Petit mal status | Epilepsy diagnosis codes: primary care |
| READ2:F252.00 | Petit mal status | Epilepsy diagnosis codes: primary care |
| READ2:F253. | Grand mal status | Epilepsy diagnosis codes: primary care |
| READ2:F253.00 | Grand mal status | Epilepsy diagnosis codes: primary care |
| READ2:F253.11 | Status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:F254. | Partial epilepsy with impairment of consciousness | Epilepsy diagnosis codes: primary care |
| READ2:F254.00 | Partial epilepsy with impairment of consciousness | Epilepsy diagnosis codes: primary care |
| READ2:F2540 | Temporal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F254000 | Temporal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2541 | Psychomotor epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F254100 | Psychomotor epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2542 | Psychosensory epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F254200 | Psychosensory epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2543 | Limbic system epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F254300 | Limbic system epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2544 | Epileptic automatism | Epilepsy diagnosis codes: primary care |
| READ2:F254400 | Epileptic automatism | Epilepsy diagnosis codes: primary care |
| READ2:F2545 | Complex partial epileptic seizure | Epilepsy diagnosis codes: primary care |
| READ2:F254500 | Complex partial epileptic seizure | Epilepsy diagnosis codes: primary care |
| READ2:F254z | Partial epilepsy with impairment of consciousness NOS | Epilepsy diagnosis codes: primary care |
| READ2:F254z00 | Partial epilepsy with impairment of consciousness NOS | Epilepsy diagnosis codes: primary care |
| READ2:F255. | Partial epilepsy without impairment of consciousness | Epilepsy diagnosis codes: primary care |
| READ2:F255.00 | Partial epilepsy without impairment of consciousness | Epilepsy diagnosis codes: primary care |
| READ2:F2550 | Jacksonian, focal or motor epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255000 | Jacksonian, focal or motor epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255011 | Focal epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255012 | Motor epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2551 | Sensory induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255100 | Sensory induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2552 | Somatosensory epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255200 | Somatosensory epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2553 | Visceral reflex epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255300 | Visceral reflex epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255311 | Partial epilepsy with autonomic symptoms | Epilepsy diagnosis codes: primary care |
| READ2:F2554 | Visual reflex epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255400 | Visual reflex epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2555 | Unilateral epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F255500 | Unilateral epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F2556 | Simple partial epileptic seizure | Epilepsy diagnosis codes: primary care |
| READ2:F255600 | Simple partial epileptic seizure | Epilepsy diagnosis codes: primary care |
| READ2:F255y | Partial epilepsy without impairment of consciousness OS | Epilepsy diagnosis codes: primary care |
| READ2:F255y00 | Partial epilepsy without impairment of consciousness OS | Epilepsy diagnosis codes: primary care |
| READ2:F255z | Partial epilepsy without impairment of consciousness NOS | Epilepsy diagnosis codes: primary care |
| READ2:F255z00 | Partial epilepsy without impairment of consciousness NOS | Epilepsy diagnosis codes: primary care |
| READ2:F256. | Infantile spasms | Epilepsy diagnosis codes: primary care |
| READ2:F256.00 | Infantile spasms | Epilepsy diagnosis codes: primary care |
| READ2:F256.12 | West syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F2560 | Hypsarrhythmia | Epilepsy diagnosis codes: primary care |
| READ2:F256000 | Hypsarrhythmia | Epilepsy diagnosis codes: primary care |
| READ2:F2561 | Salaam attacks | Epilepsy diagnosis codes: primary care |
| READ2:F256100 | Salaam attacks | Epilepsy diagnosis codes: primary care |
| READ2:F256z. | Infantile spasms NOS | Epilepsy diagnosis codes: primary care |
| READ2:F256z00 | Infantile spasms NOS | Epilepsy diagnosis codes: primary care |
| READ2:F257. | Kojevnikov's epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F257.00 | Kojevnikov's epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F258. | Post-ictal state | Epilepsy diagnosis codes: primary care |
| READ2:F258.00 | Post-ictal state | Epilepsy diagnosis codes: primary care |
| READ2:F259. | Early infant epileptic encephalopathy wth suppression bursts | Epilepsy diagnosis codes: primary care |
| READ2:F259.00 | Early infant epileptic encephalopathy wth suppression bursts | Epilepsy diagnosis codes: primary care |
| READ2:F259.11 | Ohtahara syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F25A. | Juvenile myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25A.00 | Juvenile myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25B. | Alcohol-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25B.00 | Alcohol-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25C. | Drug-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25C.00 | Drug-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25D. | Menstrual epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25D.00 | Menstrual epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25E. | Stress-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25E.00 | Stress-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25F. | Photosensitive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25F.00 | Photosensitive epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25G. | Severe myoclonic epilepsy in infancy | Epilepsy diagnosis codes: primary care |
| READ2:F25G.00 | Severe myoclonic epilepsy in infancy | Epilepsy diagnosis codes: primary care |
| READ2:F25G.11 | Dravet syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F25H. | Generalised seizure | Epilepsy diagnosis codes: primary care |
| READ2:F25H.00 | Generalised seizure | Epilepsy diagnosis codes: primary care |
| READ2:F25X. | Status epilepticus, unspecified | Epilepsy diagnosis codes: primary care |
| READ2:F25X.00 | Status epilepticus, unspecified | Epilepsy diagnosis codes: primary care |
| READ2:F25y. | Other forms of epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y.00 | Other forms of epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y0 | Cursive (running) epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y000 | Cursive (running) epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y1 | Gelastic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y100 | Gelastic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y2 | Locl-rlt(foc)(part)idiop epilep&amp;epilptic syn seiz locl onset | Epilepsy diagnosis codes: primary care |
| READ2:F25y200 | Locl-rlt(foc)(part)idiop epilep&amp;epilptic syn seiz locl onset | Epilepsy diagnosis codes: primary care |
| READ2:F25y3 | Complex partial status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:F25y300 | Complex partial status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:F25y4 | Benign Rolandic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y400 | Benign Rolandic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:F25y5 | Panayiotopoulos syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F25y500 | Panayiotopoulos syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F25yz | Other forms of epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F25yz00 | Other forms of epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F25z. | Epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F25z.00 | Epilepsy NOS | Epilepsy diagnosis codes: primary care |
| READ2:F25z.11 | Fit (in known epileptic) NOS | Epilepsy diagnosis codes: primary care |
| READ2:F28y4-1 | Glucose transporter protein type 1 deficiency syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F28y400 | GLUT1 deficiency syndrome | Epilepsy diagnosis codes: primary care |
| READ2:F28y411 | Glucose transporter protein type 1 deficiency syndrome | Epilepsy diagnosis codes: primary care |
| READ2:Fyu50 | [X]Other generalized epilepsy and epileptic syndromes | Epilepsy diagnosis codes: primary care |
| READ2:Fyu51 | [X]Other epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:Fyu52 | [X]Other status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:Fyu59 | [X]Status epilepticus, unspecified | Epilepsy diagnosis codes: primary care |
| READ2:HNG0067 | [RFC] Epilepsy/convulsion | Epilepsy diagnosis codes: primary care |
| READ2:P2283 | Aicardi syndrome | Epilepsy diagnosis codes: primary care |
| READ2:P228300 | Aicardi syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PC0682 | Nocturnal epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:PK5.. | Tuberous sclerosis | Epilepsy diagnosis codes: primary care |
| READ2:PK61.00 | Sturge-Weber syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PKy93 | Prader-Willi syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PKyz5-1 | Angelman syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PKyz511 | Angelman syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PKyz7-1 | Angelman syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PKyz700 | Angelman's syndrome | Epilepsy diagnosis codes: primary care |
| READ2:PKyz711 | Angelman syndrome | Epilepsy diagnosis codes: primary care |
| READ2:SC200 | Traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:SC200-99 | Post traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:SC2000 | Traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:SC20000 | Traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:SC20099 | Post traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:ZS82.00 | Acquired epileptic aphasia | Epilepsy diagnosis codes: primary care |
| READ2:ZS82.11 | Landau-Kleffner syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1170594 | Recurrent complex partial epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1170675 | Intractable idiopathic partial epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1177804 | Dravet Syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1183138 | Infantile-onset symptomatic epilepsy syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1204977 | Hypothalamic hamartoma with gelastic seizure | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1205388 | Recurrent benign focal seizures of childhood | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1207699 | STXBP1 encephalopathy with epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349122 | Benign familial mesial temporal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349309 | Benign occipital lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349311 | Benign partial epilepsy of infancy with complex partial seizures | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349343 | Mesial temporal lobe epilepsy with hippocampal sclerosis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349497 | Intellectual disability, seizures, hypotonia, ophthalmologic, skeletal anomalies syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349504 | New-onset refractory status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1349947 | Cortical dysplasia with focal epilepsy syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1350026 | Infantile epileptic dyskinetic encephalopathy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1350306 | Early-onset spastic ataxia, myoclonic epilepsy, neuropathy syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1357219 | KCNQ2-related epileptic encephalopathy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1357293 | Myoclonic epilepsy in non-progressive encephalopathy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1357314 | Cryptogenic late-onset epileptic spasms | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1362207 | Diffuse cerebral and cerebellar atrophy, intractable seizures, progressive microcephaly syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1362256 | Congenital muscular dystrophy with intellectual disability and severe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1362418 | Infantile spasms, psychomotor retardation, progressive brain atrophy, basal ganglia disease syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1363280 | Familial temporal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1363726 | Familial infantile myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1363784 | Familial mesial temporal lobe epilepsy with febrile seizures | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1364672 | Multiple congenital anomalies, hypotonia, seizures syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1368624 | Benign childhood epilepsy with centrotemporal spikes, refractory | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1368627 | Benign childhood epilepsy with centrotemporal spikes, non-refractory | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1379158 | Myoclonic epilepsy with ragged red fibres | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1391198 | Primary hyperaldosteronism, seizures, neurological abnormalities syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1395088 | Epilepsy due to infectious encephalitis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1395092 | Epilepsy due to infectious meningitis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCT1405504 | Scar epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTAN375005 | Angelman syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTAN500729 | Anterior frontopolar epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTAT805326 | Atypical absence epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTBE274612 | Benign focal epilepsy of childhood | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTBE476954 | Benign myoclonic epilepsy in infancy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTBE500710 | Benign frontal epilepsy of childhood | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTBE500712 | Benign atypical partial epilepsy in childhood | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTBE500717 | Benign occipital epilepsy of childhood - early onset variant | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTBI530037 | Bilateral periodic epileptiform discharges | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTCE321095 | Centrotemporal epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTCH332385 | Childhood absence epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTCH500714 | Childhood epilepsy with occipital paroxysms | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTCR500755 | Cryptogenic generalised epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTCR500777 | Cryptogenic myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTDE781180 | Developmental delay, epilepsy, neonatal diabetes syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEA500810 | Eating epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP361845 | Epileptic vertigo | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP387848 | Epileptic disorder | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP387849 | Epileptic | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP387850 | EP - Epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP500713 | Epilepsy with recurrent unilateral seizures in children | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP500754 | Epilepsy with grand mal seizures on awakening | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP500787 | Epilepsy undetermined whether focal or generalised | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP500794 | Epilepsy with continuous spike wave during slow-wave sleep | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP502353 | Epileptic psychosis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP784067 | Epileptic encephalopathy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP786134 | Epilepsy due to stroke | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP786364 | Epilepsy with mesial temporal sclerosis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP786368 | Epilepsy co-occurrent and due to dementia | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP795276 | Epilepsy telangiectasia syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP795518 | Epilepsy of infancy with migrating focal seizures | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP802469 | Epileptic dementia with behavioural disturbance | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTEP803161 | Epilepsy in pregnancy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTFR500726 | Frontal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTGE281108 | Generalized epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTHI454014 | History of epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTID309315 | Idiopathic generalised epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTID309316 | Idiopathic generalized epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTID500778 | Idiopathic myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTIN730683 | Intractable epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTIN802507 | Intractable partial temporal lobe epilepsy with impairment of consciousness | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTIN808972 | Infantile spasms co-occurrent with status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTIN808973 | Infantile spasms with status epilepticus | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTJE774510 | Jeavons syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTJM259887 | JME - Juvenile myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTKU350778 | Kufs type neuronal ceroid lipofuscinosis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTLA500792 | Landau-Kleffner syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTLO500721 | Localisation-related symptomatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTLO500744 | Localisation-related cryptogenic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTLO561416 | Localisation-related idiopathic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTME476964 | Mesiobasal limbic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTMY500762 | Myoclonic astatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTMY500766 | Myoclonic absence epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTOC500736 | Occipital lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTOP500732 | Opercular epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTOS782746 | Osteogenesis imperfecta, retinopathy, seizures, intellectual disability syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPA500735 | Parietal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPE819168 | Petit-mal epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPH405292 | Photogenic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPO371965 | Post-traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPR309317 | Primary generalised epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPR500720 | Primary inherited reading epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTPT371966 | PTE - Post-traumatic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTRA500472 | Rasmussen encephalitis | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTRE379689 | Reflex epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTRE699745 | Refractory epilepsia partialis continua | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTRE730682 | Refractory epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTRE751247 | Refractory juvenile myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSE366834 | Secondary generalized epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSE379690 | Sensory-induced epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSE500797 | Secondary reading epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSL500803 | Sleep-related epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTST281552 | Sturge-Weber disease | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSY366832 | Symptomatic generalised epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSY366833 | Symptomatic generalized epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTSY500781 | Symptomatic myoclonic epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTTE321094 | Temporal-central focal epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTTL476961 | TLE - Temporal lobe epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTTR506771 | Triple X syndrome, epilepsy, and hypogammaglobulinaemia | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTUN500768 | Unverricht-Lundborg syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^ESCTXL775809 | X-linked epilepsy with learning disability and behaviour disorder syndrome | Epilepsy diagnosis codes: primary care |
| READ2:^^ESCT1164424 | Pyridoxine-dependent epilepsy | Epilepsy diagnosis codes: primary care |
| READ2:14On.00 | At risk of sudden unexpected death in epilepsy | Epilepsy administration codes: primary care |
| READ2:1B26.00 | Trigger factor for seizure | Epilepsy administration codes: primary care |
| READ2:38VX | Neurological Disorders Depression Inventory in Epilepsy | Epilepsy administration codes: primary care |
| READ2:6110 | Contraceptive advice for patients with epilepsy | Epilepsy administration codes: primary care |
| READ2:667..00 | Epilepsy monitoring | Epilepsy administration codes: primary care |
| READ2:6671 | Initial epilepsy assessment | Epilepsy administration codes: primary care |
| READ2:6672 | Follow-up epilepsy assessment | Epilepsy administration codes: primary care |
| READ2:6674 | Epilepsy associated problems | Epilepsy administration codes: primary care |
| READ2:6675 | Fit frequency | Epilepsy administration codes: primary care |
| READ2:6677 | Epilepsy drug side effects | Epilepsy administration codes: primary care |
| READ2:6678 | Epilepsy treatment changed | Epilepsy administration codes: primary care |
| READ2:6679 | Epilepsy treatment started | Epilepsy administration codes: primary care |
| READ2:667C. | Epilepsy control good | Epilepsy administration codes: primary care |
| READ2:667D. | Epilepsy control poor | Epilepsy administration codes: primary care |
| READ2:667E.00 | Epilepsy care arrangement | Epilepsy administration codes: primary care |
| READ2:667G. | Epilepsy restricts employment | Epilepsy administration codes: primary care |
| READ2:667H. | Epilepsy prevents employment | Epilepsy administration codes: primary care |
| READ2:667J. | Epilepsy impairs education | Epilepsy administration codes: primary care |
| READ2:667K. | Epilepsy limits activities | Epilepsy administration codes: primary care |
| READ2:667L. | Epilepsy does not limit activities | Epilepsy administration codes: primary care |
| READ2:667M.00 | Epilepsy management plan given | Epilepsy administration codes: primary care |
| READ2:667N. | Epilepsy severity | Epilepsy administration codes: primary care |
| READ2:667W. | Emergency epilepsy treatment since last appointment | Epilepsy administration codes: primary care |
| READ2:667X.00 | No epilepsy drug side effects | Epilepsy administration codes: primary care |
| READ2:667Z.00 | Epilepsy monitoring NOS | Epilepsy administration codes: primary care |
| READ2:67AF.00 | Pregnancy advice for patients with epilepsy | Epilepsy administration codes: primary care |
| READ2:67IJ000 | Pre-conception advice for patients with epilepsy | Epilepsy administration codes: primary care |
| READ2:8BIF.00 | Epilepsy medication review | Epilepsy administration codes: primary care |
| READ2:8BL3.00 | Patient on maximal tolerated anticonvulsant therapy | Epilepsy administration codes: primary care |
| READ2:8IAg.00 | Contraceptive advice for patients with epilepsy declined | Epilepsy administration codes: primary care |
| READ2:8IAh.00 | Pre-conception advice for patients with epilepsy declined | Epilepsy administration codes: primary care |
| READ2:8IAi.00 | Pregnancy advice for patients with epilepsy declined | Epilepsy administration codes: primary care |
| READ2:8IB2.00 | Contraceptiv advice for patients with epilepsy not indicated** | Epilepsy administration codes: primary care |
| READ2:8IB3.00 | Pre-conception advic fr patients with epilepsy not indicated** | Epilepsy administration codes: primary care |
| READ2:8IB4.00 | Pregnancy advice for patients with epilepsy not indicated** | Epilepsy administration codes: primary care |
| READ2:9Of..00 | Epilepsy screen administration | Epilepsy administration codes: primary care |
| READ2:9Of0.00 | Epilepsy screen invite 1 | Epilepsy administration codes: primary care |
| READ2:9Of1.00 | Epilepsy screen invite 2 | Epilepsy administration codes: primary care |
| READ2:9Of2.00 | Epilepsy screen invite 3 | Epilepsy administration codes: primary care |
| READ2:9Of3.00 | Epilepsy monitoring verbal invite | Epilepsy administration codes: primary care |
| READ2:9Of4.00 | Epilepsy monitoring telephone invite | Epilepsy administration codes: primary care |
| READ2:9Of5.00 | Epilepsy monitoring call first letter | Epilepsy administration codes: primary care |
| READ2:9Of6.00 | Epilepsy monitoring call second letter | Epilepsy administration codes: primary care |
| READ2:9Of7.00 | Epilepsy monitoring call third letter | Epilepsy administration codes: primary care |
| READ2:9h6..00 | Exception reporting: epilepsy quality indicators | Epilepsy administration codes: primary care |
| READ2:9h62.00 | Excepted from epilepsy quality indicators: Informed dissent** | Epilepsy administration codes: primary care |
| READ2:EMISNQCO292 | Contraceptive advice for patients on valproate for epilepsy | Epilepsy administration codes: primary care |
| READ2:EMISNQEP19 | Epilepsy monitoring administration | Epilepsy administration codes: primary care |
| READ2:EMISNQEP20 | Epilepsy monitoring in primary care | Epilepsy administration codes: primary care |
| READ2:EMISNQEP21 | Epilepsy monitoring in secondary care | Epilepsy administration codes: primary care |
| READ2:EMISNQEP22 | Epilepsy treatment compliance | Epilepsy administration codes: primary care |
| READ2:EMISNQEP23 | Epilepsy treatment compliance good | Epilepsy administration codes: primary care |
| READ2:EMISNQEP24 | Epilepsy treatment compliance poor | Epilepsy administration codes: primary care |
| READ2:EMISNQEP25 | Epilepsy monitoring default | Epilepsy administration codes: primary care |
| READ2:EMISNQEP4 | Epilepsy treatment continued | Epilepsy administration codes: primary care |
| READ2:EMISNQEP5 | Epilepsy monitoring call first letter | Epilepsy administration codes: primary care |
| READ2:EMISNQEP7 | Epilepsy monitoring call third letter | Epilepsy administration codes: primary care |
| READ2:PC0037 | Epilepsy monitoring | Epilepsy administration codes: primary care |
| READ2:PC0678 | Epilepsy associated problems | Epilepsy administration codes: primary care |
| READ2:PC0681 | Epilepsy drug side effects | Epilepsy administration codes: primary care |
| READ2:^ESCT1167752 | Seizure disorder clinical management plan | Epilepsy administration codes: primary care |
| READ2:^ESCT1171158 | Paediatric epilepsy care plan | Epilepsy administration codes: primary care |
| READ2:^ESCTEP519238 | Epilepsy monitoring status | Epilepsy administration codes: primary care |
| READ2:^ESCTEP690875 | Epilepsy monitoring call | Epilepsy administration codes: primary care |
| READ2:^ESCTEP807979 | Epilepsy monitoring telephone invitation | Epilepsy administration codes: primary care |
| READ2:^ESCTEP828973 | Epilepsy annual review | Epilepsy administration codes: primary care |
| READ2:^ESCTEP828983 | Epilepsy care management | Epilepsy administration codes: primary care |
| READ2:^ESCTEP828988 | Epilepsy self-management plan review | Epilepsy administration codes: primary care |
| READ2:^ESCTUN826098 | Under care of epilepsy specialist nurse | Epilepsy administration codes: primary care |
| READ2:13ZD | Witnessed epileptic seizure | Epilepsy seizure codes: primary care |
| READ2:13ZD.00 | Witnessed epileptic seizure | Epilepsy seizure codes: primary care |
| READ2:1B63. | Had a fit | Epilepsy seizure codes: primary care |
| READ2:1B63.00 | Had a fit | Epilepsy seizure codes: primary care |
| READ2:1B63.11 | Fit - had one, symptom | Epilepsy seizure codes: primary care |
| READ2:282-2 | O/E - a fit | Epilepsy seizure codes: primary care |
| READ2:282-3 | O/E - a seizure | Epilepsy seizure codes: primary care |
| READ2:282..00 | O/E - fit/convulsion | Epilepsy seizure codes: primary care |
| READ2:282..12 | O/E - a fit | Epilepsy seizure codes: primary care |
| READ2:282..13 | O/E - a seizure | Epilepsy seizure codes: primary care |
| READ2:2822 | O/E - grand mal fit | Epilepsy seizure codes: primary care |
| READ2:2823 | O/E - petit mal fit | Epilepsy seizure codes: primary care |
| READ2:2824 | O/E - focal (Jacksonian) fit | Epilepsy seizure codes: primary care |
| READ2:2824.11 | O/E - Jacksonian fit | Epilepsy seizure codes: primary care |
| READ2:2824.12 | O/E - focal fit | Epilepsy seizure codes: primary care |
| READ2:2825 | O/E - psychomotor fit | Epilepsy seizure codes: primary care |
| READ2:2826. | O/E - salaam attack | Epilepsy seizure codes: primary care |
| READ2:2828. | Absence seizure | Epilepsy seizure codes: primary care |
| READ2:282Z. | O/E - fit/convulsion NOS | Epilepsy seizure codes: primary care |
| READ2:282Z.00 | O/E - fit/convulsion NOS | Epilepsy seizure codes: primary care |
| READ2:667Q. | 1 to 12 seizures a year | Epilepsy seizure codes: primary care |
| READ2:667Q.00 | 1 to 12 seizures a year | Epilepsy seizure codes: primary care |
| READ2:667R. | 2 to 4 seizures a month | Epilepsy seizure codes: primary care |
| READ2:667R.00 | 2 to 4 seizures a month | Epilepsy seizure codes: primary care |
| READ2:667S. | 1 to 7 seizures a week | Epilepsy seizure codes: primary care |
| READ2:667S.00 | 1 to 7 seizures a week | Epilepsy seizure codes: primary care |
| READ2:667T. | Daily seizures | Epilepsy seizure codes: primary care |
| READ2:667T.00 | Daily seizures | Epilepsy seizure codes: primary care |
| READ2:667V. | Many seizures a day | Epilepsy seizure codes: primary care |
| READ2:667V.00 | Many seizures a day | Epilepsy seizure codes: primary care |
| READ2:667Y. | Observations of measures of seizures | Epilepsy seizure codes: primary care |
| READ2:667Y.00 | Observations of measures of seizures | Epilepsy seizure codes: primary care |
| READ2:F132z-2 | Myoclonic seizure | Epilepsy seizure codes: primary care |
| READ2:F132z12 | Myoclonic seizure | Epilepsy seizure codes: primary care |
| READ2:JHCHO1 | H/O: seizures | Epilepsy seizure codes: primary care |
| READ2:R0034 | Night seizure | Epilepsy seizure codes: primary care |
| READ2:R003400 | [D]Nocturnal seizure | Epilepsy seizure codes: primary care |
| READ2:R003z-1 | Convulsion NOS* | Epilepsy seizure codes: primary care |
| READ2:R003z11 | [D]Seizure NOS* | Epilepsy seizure codes: primary care |
| READ2:^ESCT1445378 | Non-convulsive seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCT1463640 | Generalised onset seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTAB386273 | Abdominal seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTAB523187 | Absence seizure with impairment of consciousness only | Epilepsy seizure codes: primary care |
| READ2:^ESCTAB523190 | Absence seizure with atonic components | Epilepsy seizure codes: primary care |
| READ2:^ESCTAB523191 | Absence seizure with tonic components | Epilepsy seizure codes: primary care |
| READ2:^ESCTAF728992 | Afebrile seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTAL622145 | Alcohol-related fit | Epilepsy seizure codes: primary care |
| READ2:^ESCTAT287277 | Atypical absence seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTAT318292 | Atonic seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTAT318293 | Atonic seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTCH727709 | Childhood seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTCL259897 | Clonic seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO256432 | Complex partial seizure with impairment of consciousness | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO256435 | Complex partial seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO272147 | Convulsive status epilepticus | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO476969 | Complex partial seizures with automatisms | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO802498 | Complex partial seizure of frontal lobe | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO802502 | Complex partial epileptic seizure of occipital lobe | Epilepsy seizure codes: primary care |
| READ2:^ESCTCO802504 | Complex partial seizure of temporal lobe | Epilepsy seizure codes: primary care |
| READ2:^ESCTDY298235 | Dysmnesic seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTEE319923 | EEG abnormality with seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTEP250235 | Epilepsia partialis continua | Epilepsy seizure codes: primary care |
| READ2:^ESCTEP261211 | Epileptic absence status | Epilepsy seizure codes: primary care |
| READ2:^ESCTEP475577 | Epileptic drop attack | Epilepsy seizure codes: primary care |
| READ2:^ESCTEP602864 | Epileptic fit | Epilepsy seizure codes: primary care |
| READ2:^ESCTFI801842 | First generalised onset seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTFI801843 | First generalized onset seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTFO250239 | Focal status epilepticus | Epilepsy seizure codes: primary care |
| READ2:^ESCTFO297900 | Focal seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTFO441188 | Focal motor seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTFO736636 | Focal seizure with experiential sensory symptoms | Epilepsy seizure codes: primary care |
| READ2:^ESCTGE257261 | Generalised-onset seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTGE257262 | Generalized-onset seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTGE395515 | Gelastic seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTGE523183 | Generalized seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTGE530025 | Generalised epileptiform discharges | Epilepsy seizure codes: primary care |
| READ2:^ESCTGE530026 | Generalized epileptiform discharges | Epilepsy seizure codes: primary care |
| READ2:^ESCTIN802144 | Intractable absence seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTIS500784 | Isolated seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTMY310191 | Myoclonic seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTNE392196 | Neonatal seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTNO261212 | Non-convulsive status epilepticus with impaired consciousness | Epilepsy seizure codes: primary care |
| READ2:^ESCTNO500821 | Non-convulsive status epilepticus without three per second spike wave | Epilepsy seizure codes: primary care |
| READ2:^ESCTNO500823 | Non-convulsive simple partial status epilepticus | Epilepsy seizure codes: primary care |
| READ2:^ESCTNO726538 | Nonconvulsive status epilepticus | Epilepsy seizure codes: primary care |
| READ2:^ESCTPA297898 | Partial seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTPA297899 | Partial seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTPA523179 | Partial seizure evolving to secondary generalised seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTPA523180 | Partial seizure evolving to secondary generalized seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTPE261210 | Petit mal status | Epilepsy seizure codes: primary care |
| READ2:^ESCTPE379509 | Petit-mal seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTPH523168 | Phonatory seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTPO271113 | Postseizure headache | Epilepsy seizure codes: primary care |
| READ2:^ESCTPO301162 | Post-seizure state | Epilepsy seizure codes: primary care |
| READ2:^ESCTPO523167 | Postural seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTSE282653 | Secondarily generalised seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTSE441189 | Seizure disorder | Epilepsy seizure codes: primary care |
| READ2:^ESCTSE500786 | Seizure with provoking factor | Epilepsy seizure codes: primary care |
| READ2:^ESCTSE559501 | Seizure undetermined whether focal or generalised | Epilepsy seizure codes: primary care |
| READ2:^ESCTSE781369 | Seizure, sensorineural deafness, ataxia, intellectual disability, electrolyte imbalance syndrome | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI330348 | Simple partial onset seizure followed by impaired consciousness | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI349888 | Simple partial seizure evolving to generalised seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI379031 | Simple partial seizure, consciousness not impaired | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI384042 | Simple partial seizure with motor dysfunction | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI384043 | Simple partial seizures with motor signs | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI500782 | Situation-related seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI523162 | Simple partial seizure with focal motor signs without march | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI523163 | Simple partial seizure with focal motor signs with march | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI523176 | Simple partial onset of seizure with automatisms | Epilepsy seizure codes: primary care |
| READ2:^ESCTSI803702 | Simple partial seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTST336737 | Startle partial seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTST808958 | Status epilepticus due to refractory complex partial seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTTO334109 | Tonic seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTTO337924 | Tonic-clonic seizure | Epilepsy seizure codes: primary care |
| READ2:^ESCTTO337925 | Tonic-clonic seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTUN375993 | Unclassified epileptic seizures | Epilepsy seizure codes: primary care |
| READ2:^ESCTVI273002 | Visual seizure | Epilepsy seizure codes: primary care |
| ICD10:E75.4 | Neuronal ceroid lipofuscinosis | Epilepsy diagnosis codes: secondary care |
| ICD10:F80.3 | Landau-Kleffner syndrome | Epilepsy diagnosis codes: secondary care |
| ICD10:F84.2 | Rett Syndrome | Epilepsy diagnosis codes: secondary care |
| ICD10:G40 | Epilepsy | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.0 | Localization-related (focal)(partial) idiopathic epilepsy and epileptic syndromes with seizures of localized onset | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.1 | Localization-related (focal)(partial) symptomatic epilepsy and epileptic syndromes with simple partial seizures | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.2 | Localization-related (focal)(partial) symptomatic epilepsy and epileptic syndromes with complex partial seizures | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.3 | Generalized idiopathic epilepsy and epileptic syndromes: Benign: myoclonic epilepsy in infancy, neonatal convulsions (familial), Childhood absence epilepsy [pyknolepsy], Epilepsy with grand mal seizures on awakening, Juvenile: absence epilepsy, myoclonic epilepsy [impulsive petit mal], Nonspecific epileptic seizures: atonic, clonic, myoclonic, tonic, tonic-clonic. | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.4 | Other generalized epilepsy and epileptic syndromes: This term includes Epilepsy with myoclonic absenses, myoclonic-astatic seizures, Infantile spasms, Lennox-Gastaut syndrome, Salaam attacks, Symptomatic early myoclonic encephalopathy, West syndrome | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.5 | Special epileptic syndromes: Includes: Epilepsia partialis continua [Kozhevnikof], and Epileptic seizures related to: alcohol, drugs, hormonal change, sleep deprivation and stress.** | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.8 | Other epilepsy | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.9 | Epilepsy, unspecified | Epilepsy diagnosis codes: secondary care |
| ICD10:G41 | Status epilepticus | Epilepsy diagnosis codes: secondary care |
| ICD10:G41.0 | Grand mal status epilepticus | Epilepsy diagnosis codes: secondary care |
| ICD10:G41.1 | Petit mal status epilepticus | Epilepsy diagnosis codes: secondary care |
| ICD10:G41.2 | Complex partial status epilepticus | Epilepsy diagnosis codes: secondary care |
| ICD10:G41.8 | Other status epilepticus | Epilepsy diagnosis codes: secondary care |
| ICD10:G41.9 | Status epilepticus, unspecified | Epilepsy diagnosis codes: secondary care |
| ICD10:Q85.1 | Tuberous Sclerosis | Epilepsy diagnosis codes: secondary care |
| ICD10:G40.6 | Grand mal seizures, unspecified (with or without petit mal) | Epilepsy seizure codes: secondary care |
| ICD10:G40.7 | Petit mal, unspecified, without grand mal seizures | Epilepsy seizure codes: secondary care |
| ICD10:R56 | Convulsions, not elsewhere classified* | Epilepsy seizure codes: secondary care |
| ICD10:R56.8 | Other and unspecified convulsions* | Epilepsy seizure codes: secondary care |
| ICD9CM:345 | Epilepsy and recurrent seizures | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.0 | Generalized nonconvulsive epilepsy | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.1 | Generalized convulsive epilepsy | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.2 | Petit mal status | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.3 | Grand mal status | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.4 | Localization-related (focal) (partial) epilepsy and epileptic syndromes with complex partial seizures | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.5 | Localization-related (focal) (partial) epilepsy and epileptic syndromes with simple partial seizures | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.6 | Infantile spasms | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.7 | Epilepsia partialis continua | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.8 | Other forms of epilepsy and recurrent seizures (e.g. gelastic epilepsy) | Epilepsy diagnosis codes: secondary care |
| ICD9CM:345.9 | Epilepsy, unspecified | Epilepsy diagnosis codes: secondary care |
| ICD9CM:780.3 | Convulsions | Epilepsy seizure codes: secondary care |
| READ2:115Q. | No history of epilepsy | Excluded codes - codes not indicating epilepsy |
| READ2:13Y9. | Epilepsy society member | Excluded codes - codes not indicating epilepsy |
| READ2:13ZD. | Eye witness to an epileptic seizure | Excluded codes - codes not indicating epilepsy |
| READ2:1AJ0. | Suspected epilepsy | Excluded codes - codes not indicating epilepsy |
| READ2:1B27. | Seizures in response to an acute event | Excluded codes - codes not indicating epilepsy |
| READ2:21260 | Epilepsy resolved | Excluded codes - codes not indicating epilepsy |
| READ2:2126000 | Epilepsy resolved | Excluded codes - codes not indicating epilepsy |
| READ2:300 | Anxiety, dissociative and somatoform disorders | Excluded codes - codes not indicating epilepsy |
| READ2:300.1 | Dissociative, conversion and factitious disorders | Excluded codes - codes not indicating epilepsy |
| READ2:300.11 | Conversion disorder | Excluded codes - codes not indicating epilepsy |
| READ2:667A.00 | Epilepsy treatment stopped | Excluded codes - codes not indicating epilepsy |
| READ2:667F.00 | Seizure free &gt;12 months | Excluded codes - codes not indicating epilepsy |
| READ2:667P.00 | No seizures on treatment | Excluded codes - codes not indicating epilepsy |
| READ2:779.0 | Convulsions in newborn | Excluded codes - codes not indicating epilepsy |
| READ2:8CE7. | Epilepsy leaflet given | Excluded codes - codes not indicating epilepsy |
| READ2:8Hlp. | Refferal to epilepsy clinic | Excluded codes - codes not indicating epilepsy |
| READ2:8T0L. | Refferal to epilepsy services | Excluded codes - codes not indicating epilepsy |
| READ2:9N0r. | Seen in epilepsy clinic | Excluded codes - codes not indicating epilepsy |
| READ2:9N4V. | Did not attend epilepsy clinic | Excluded codes - codes not indicating epilepsy |
| READ2:E2015 | Hysterical seizures | Excluded codes - codes not indicating epilepsy |
| READ2:Eu108. | Alcohol withdrawel induced seizures | Excluded codes - codes not indicating epilepsy |
| READ2:F44.5 | Dissociative convulsions | Excluded codes - codes not indicating epilepsy |
| READ2:R0033 | Reflex anoxic seizure | Excluded codes - codes not indicating epilepsy |
| READ2:R56.0 | Febrile convulsions (code here if simple) | Excluded codes - codes not indicating epilepsy |
| READ2:ZV172 | Family history of epilepsy | Excluded codes - codes not indicating epilepsy |
| READ2:bc6.. | PHENYTOIN SODIUM [ANTIARRHYTHMIC] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:bc61. | EPANUTIN READY MIXED PARENTERAL 250mg/5mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:bc62. | PHENYTOIN 250mg/5mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21G. | VALCLAIR 10mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21d. | DIAZEMULS 10mg/2mL ampoules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21i. | *STESOLID 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21j. | *STESOLID 20mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21k. | STESOLID 5mg rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21l. | STESOLID 10mg rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21v. | VALIUM [ANXIOL] 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21w. | *VALIUM DUP DEL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21x. | *VALIUM 5mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21y. | *VALIUM 10mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21z. | DIAZEPAM 10mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d26.. | CLOBAZAM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d261. | *CLOBAZAM 10mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d262. | *FRISIUM 10mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d263. | CLOBAZAM 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d264. | FRISIUM 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d265. | TAPCLOB 5mg/5mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d266. | CLOBAZAM 5mg/5mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d267. | TAPCLOB 10mg/5mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d268. | CLOBAZAM 10mg/5mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d269. | PERIZAM 1mg/mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d26A. | PERIZAM 2mg/mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:df2.. | FENFLURAMINE HYDROCHLORIDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:df2z. | FENFLURAMINE HYDROCHLORIDE 60mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn1.. | ACETAZOLAMIDE [EPILEPSY] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn11. | DIAMOX [EP] 500mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn12. | DIAMOX [EP] 250mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn13. | DIAMOX [EP] 500mg injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn1x. | ACETAZOLAMIDE [EP] 500mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn1y. | ACETAZOLAMIDE [EP] 250mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn1z. | ACETAZOLAMIDE [EP] 500mg injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn2.. | *BECLAMIDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn21. | *NYDRANE 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn2z. | *BECLAMIDE 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3.. | CARBAMAZEPINE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn31. | CARBAMAZEPINE 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn32. | CARBAMAZEPINE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn33. | CARBAMAZEPINE 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn34. | TEGRETOL 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn35. | TEGRETOL 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn36. | TEGRETOL 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn37. | TEGRETOL 100mg/5mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn38. | TEGRETOL RETARD 200mg m/r tabs | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn39. | TEGRETOL RETARD 400mg m/r tabs | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3A. | *EPIMAZ 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3B. | *EPIMAZ 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3C. | *EPIMAZ 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3D. | TEGRETOL 125mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3E. | TEGRETOL 250mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3F. | TIMONIL RETARD 200mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3G. | TIMONIL RETARD 400mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3H. | TERIL CR 200mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3I. | TERIL CR 400mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3J. | CARBAGEN SR 200mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3K. | CARBAGEN SR 400mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3a. | CARBAMAZEPINE 200mg m/r tabs | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3b. | CARBAMAZEPINE 400mg m/r tabs | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3c. | TEGRETOL 100mg chewable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3d. | TEGRETOL 200mg chewable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3e. | ARBIL MR 200mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3f. | ARBIL MR 400mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3v. | CARBAMAZEPINE 125mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3w. | CARBAMAZEPINE 250mg suppositories | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3x. | CARBAMAZEPINE 200mg chewable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3y. | CARBAMAZEPINE 100mg chewable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn3z. | CARBAMAZEPINE 100mg/5mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn4.. | CLONAZEPAM [EPILEPSY CONTROL] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn41. | RIVOTRIL 500micrograms tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn42. | RIVOTRIL 2mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn4w. | CLONAZEPAM 0.5mg/5mL sugar free oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn4x. | CLONAZEPAM 2mg/5mL sugar free oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn4y. | CLONAZEPAM 500microgram tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn4z. | CLONAZEPAM 2mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn5.. | ETHOSUXIMIDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn51. | *ETHOSUXIMIDE 250mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn52. | *ETHOSUXIMIDE 250mg/5mL elixir | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn53. | *EMESIDE 250mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn54. | EMESIDE 250mg/5mL syrup | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn55. | *ZARONTIN 250mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn56. | ZARONTIN 250mg/5mL syrup | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn5x. | ETHOSUXIMIDE 250mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn5y. | *ETHOSUXIMIDE 250mg/5mL elixir | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn5z. | ETHOSUXIMIDE 250mg/5mL syrup | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn6.. | METHYLPHENOBARBITAL | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn61. | *PROMINAL 30mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn62. | *PROMINAL 60mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn63. | *PROMINAL 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn6x. | METHYLPHENOBARBITONE 30mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn6y. | METHYLPHENOBARBITONE 60mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn6z. | METHYLPHENOBARBITONE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn7.. | PHENOBARBITAL | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn71. | PHENOBARBITAL 15mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn72. | PHENOBARBITAL 30mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn73. | PHENOBARBITAL 60mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn74. | PHENOBARBITAL 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn75. | PHENOBARBITONE SODIUM 30mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn76. | PHENOBARBITONE SODIUM 60mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn77. | PHENOBARBITONE 15mg/10mL elixir | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn78. | PHENOBARBITAL 200mg/1mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn79. | *GARDENAL 200mg/1mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn7a. | *LUMINAL 15mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn7b. | *LUMINAL 30mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn7c. | *LUMINAL 60mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn7d. | PHENOBARBITAL 15mg/5mL elixir | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn8.. | PHENYTOIN | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn81. | EPANUTIN 30mg/5mL suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn82. | EPANUTIN 50mg Infatabs | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn83. | PHENYTOIN 50mg chewable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn8y. | PHENYTOIN 30mg/5mL suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn8z. | PHENYTOIN 90mg/5mL sugar free suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn9.. | PHENYTOIN SODIUM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn91. | PHENYTOIN 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn92. | PHENYTOIN 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn93. | EPANUTIN 25mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn94. | EPANUTIN 50mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn95. | EPANUTIN 100mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn96. | EPANUTIN 300mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn97. | *PENTRAN 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn98. | *PENTRAN 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn9w. | PHENYTOIN SODIUM 300mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn9x. | PHENYTOIN SODIUM 25mg caps | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn9y. | PHENYTOIN SODIUM 50mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dn9z. | PHENYTOIN SODIUM 100mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dna.. | PRIMIDONE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dna1. | MYSOLINE 250mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dna2. | MYSOLINE 250mg/5mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dna3. | MYSOLINE 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnax. | PRIMIDONE 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnay. | PRIMIDONE 250mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnaz. | PRIMIDONE 250mg/5mL oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb.. | SODIUM VALPROATE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb1. | EPILIM 100mg crushable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb2. | EPILIM 200mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb3. | EPILIM 500mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb4. | EPILIM 200mg/5mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb5. | EPILIM 200mg/5mL syrup | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb6. | EPILIM IV 400mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb7. | SODIUM VALPROATE 200mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb8. | SODIUM VALPROATE 500mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnb9. | ORLEPT STARTER PACK 200mg e/c tablets x10 | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbA. | ORLEPT 200mg/5mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbB. | EPIVAL CR 300mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbC. | EPIVAL CR 500mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbD. | EPISENTA 300mg/3mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbE. | SODIUM VALPROATE 300mg/3mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbF. | EPISENTA 150mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbG. | EPISENTA 300mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbH. | EPISENTA 500mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbI. | EPISENTA 1g/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbJ. | SODIUM VALPROATE 150mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbK. | SODIUM VALPROATE 300mg m/r capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbL. | SODIUM VALPROATE 500mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbM. | SODIUM VALPROATE 1g/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbN. | SODIUM VALPROATE 1g/10mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbO. | EPISENTA 1g/10mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbP. | EPILIM CHRONOSPHERE 50mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbQ. | EPILIM CHRONOSPHERE 100mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbR. | EPILIM CHRONOSPHERE 250mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbS. | EPILIM CHRONOSPHERE 500mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbT. | EPILIM CHRONOSPHERE 750mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbU. | EPILIM CHRONOSPHERE 1g/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnba. | *ORLEPT 200mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbb. | *ORLEPT 500mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbc. | EPILIM CHRONO 200 m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbd. | EPILIM CHRONO 300 m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbe. | EPILIM CHRONO 500 m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbn. | SODIUM VALPROATE 50mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbo. | SODIUM VALPROATE 100mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbp. | SODIUM VALPROATE 250mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbq. | SODIUM VALPROATE 750mg/sachet m/r granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbr. | SODIUM VALPROATE 200mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbs. | SODIUM VALPROATE 300mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbt. | SODIUM VALPROATE 500mg m/r tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbu. | SODIUM VALPROATE 400mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbv. | SODIUM VALPROATE 100mg crushable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbw. | SODIUM VALPROATE 200mg crushable tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbx. | SODIUM VALPROATE 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnby. | SODIUM VALPROATE 200mg/5mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnbz. | SODIUM VALPROATE 200mg/5mL syrup | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnc.. | CLOBAZAM [EPILEPSY ONLY] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnc1. | *CLOBAZAM SLS 10mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dne.. | VIGABATRIN | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dne1. | VIGABATRIN 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dne2. | SABRIL 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dne3. | VIGABATRIN 500mg powder sachets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dne4. | SABRIL 500mg powder sachets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf.. | LAMOTRIGINE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf1. | LAMOTRIGINE 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf2. | LAMOTRIGINE 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf3. | LAMICTAL 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf4. | LAMICTAL 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf5. | LAMOTRIGINE 25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf6. | LAMICTAL 25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf7. | LAMICTAL 5mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf8. | LAMICTAL 25mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnf9. | LAMICTAL 100mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfA. | LAMOTRIGINE 5mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfB. | LAMOTRIGINE 25mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfC. | LAMOTRIGINE 100mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfD. | LAMICTAL 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfE. | LAMOTRIGINE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfF. | LAMICTAL MONOTHERAPY 25mg starter pack | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfG. | LAMICTAL VALPROATE ADD-ON 25mg starter pack | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfH. | LAMICTAL NON-VALPROATE ADD-ON 50mg starter pack | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfJ. | LAMICTAL 2mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnfz. | LAMOTRIGINE 2mg dispersible tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng.. | PIRACETAM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng1. | NOOTROPIL 800mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng2. | NOOTROPIL 1.2g tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng3. | NOOTROPIL 33% oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng4. | PIRACETAM 800mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng5. | PIRACETAM 1.2g tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dng6. | PIRACETAM 333.3mg/mL oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh.. | VALPROIC ACID | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh1. | CONVULEX 150mg e/c capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh2. | CONVULEX 300mg e/c capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh3. | CONVULEX 500mg e/c capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh4. | VALPROIC ACID 150mg e/c capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh5. | VALPROIC ACID 300mg e/c capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh6. | VALPROIC ACID 500mg e/c capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh7. | DEPAKOTE 250mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnh8. | DEPAKOTE 500mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnhy. | VALPROIC ACID 500mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnhz. | VALPROIC ACID 250mg e/c tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dni.. | FOSPHENYTOIN SODIUM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dni1. | FOSPHENYTOIN SODIUM 750mg/10mL injection concentrate | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dni2. | PRO-EPANUTIN 750mg/10mL injection concentrate | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk.. | TOPIRAMATE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk1. | TOPIRAMATE 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk2. | TOPIRAMATE 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk3. | TOPIRAMATE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk4. | TOPAMAX 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk5. | TOPAMAX 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk6. | TOPAMAX 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk7. | TOPIRAMATE 25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk8. | TOPAMAX 25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnk9. | TOPIRAMATE 15mg beads in capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnkA. | TOPIRAMATE 25mg beads in capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnkB. | TOPAMAX SPRINKLE 15mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnkC. | TOPAMAX SPRINKLE 25mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnkD. | TOPIRAMATE 50mg beads in capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnkE. | TOPAMAX SPRINKLE 50mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl.. | TIAGABINE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl1. | TIAGABINE 5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl2. | TIAGABINE 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl3. | TIAGABINE 15mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl4. | GABITRIL 5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl5. | GABITRIL 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnl6. | GABITRIL 15mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnm.. | OXCARBAZEPINE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnm1. | TRILEPTAL 150 tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnm2. | TRILEPTAL 300 tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnm3. | TRILEPTAL 600 tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnm4. | TRILEPTAL 60mg/mL sugar free oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnmw. | OXCARBAZEPINE 60mg/mL sugar free oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnmx. | OXCARBAZEPINE 150mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnmy. | OXCARBAZEPINE 300mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnmz. | OXCARBAZEPINE 600mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno.. | LEVETIRACETAM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno1. | KEPPRA 250mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno2. | KEPPRA 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno3. | KEPPRA 1g tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno4. | KEPPRA 750mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno5. | KEPPRA 100mg/mL s/f oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno6. | KEPPRA 500mg/5mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno7. | DESITREND 250mg/sachet granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dno8. | DESITREND 500mg/sachet granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnoA. | DESITREND 100mg/mL oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnor. | LEVETIRACETAM 1g/sachet granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnos. | LEVETIRACETAM 500mg/sachet granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnot. | LEVETIRACETAM 250mg/sachet granules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnou. | LEVETIRACETAM 500mg/5mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnov. | LEVETIRACETAM 100mg/mL s/f oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnow. | LEVETIRACETAM 750mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnox. | LEVETIRACETAM 1g tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnoy. | LEVETIRACETAM 500mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnoz. | LEVETIRACETAM 250mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq.. | ZONISAMIDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq1. | ZONISAMIDE 25mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq2. | ZONISAMIDE 50mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq3. | ZONISAMIDE 100mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq4. | ZONEGRAN 25mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq5. | ZONEGRAN 50mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnq6. | ZONEGRAN 100mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnr.. | RUFINAMIDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnr1. | INOVELON 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnr2. | INOVELON 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnr3. | INOVELON 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnrx. | RUFINAMIDE 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnry. | RUFINAMIDE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnrz. | RUFINAMIDE 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dns.. | STIRIPENTOL | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dns1. | DIACOMIT 250mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dns2. | DIACOMIT 500mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dns3. | DIACOMIT 250mg/sachet powder for oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dns4. | DIACOMIT 500mg/sachet powder for oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnsx. | STIRIPENTOL 250mg/sachet powder for oral suspension | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnsy. | STIRIPENTOL 500mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnsz. | STIRIPENTOL 250mg capsules | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt.. | LACOSAMIDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt1. | VIMPAT 200mg/20mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt2. | VIMPAT 15mg/1mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt3. | VIMPAT 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt4. | VIMPAT 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt5. | VIMPAT 150mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt6. | VIMPAT 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt7. | LACOSAMIDE 200mg/20mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt8. | LACOSAMIDE 15mg/1mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnt9. | LACOSAMIDE 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dntA. | LACOSAMIDE 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dntB. | LACOSAMIDE 150mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dntC. | LACOSAMIDE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dntE. | LACOSAMIDE 10mg/1mL sugar free liquid | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnu.. | ESLICARBAZEPINE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnu1. | ZEBINIX 800mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnu2. | ESLICARBAZEPINE ACETATE 800mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv.. | RETIGABINE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv1. | TROBALT 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv2. | TROBALT 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv3. | TROBALT 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv4. | TROBALT 300mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv5. | TROBALT 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv6. | TROBALT tablets initiation pack | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv7. | RETIGABINE 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv8. | RETIGABINE 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnv9. | RETIGABINE 200mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnvA. | RETIGABINE 300mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnvB. | RETIGABINE 400mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnvC. | RETIGABINE 50mg+100mg tablets initiation pack | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnw.. | PERAMPANEL | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnw1. | FYCOMPA 2mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnw2. | FYCOMPA 4mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnw3. | FYCOMPA 6mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnw4. | FYCOMPA 8mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnw5. | FYCOMPA 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnwu. | PERAMPANEL 12mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnwv. | PERAMPANEL 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnww. | PERAMPANEL 8mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnwx. | PERAMPANEL 6mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnwy. | PERAMPANEL 4mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnwz. | PERAMPANEL 2mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx. | BRIVARACETAM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx1. | BRIVIACT 10mg/mL oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx2. | BRIVARACETAM 10mg/mL oral solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx3. | BRIVIACT 50mg/mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx4. | BRIVARACETAM 50mg/mL solution for injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx5. | BRIVIACT 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx6. | BRIVARACETAM 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx7. | BRIVIACT 25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx8. | BRIVARACETAM 25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnx9. | BRIVIACT 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnxA. | BRIVARACETAM 50mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnxB. | BRIVIACT 75mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnxC. | BRIVARACETAM 75mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnxD. | BRIVIACT 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:dnxE. | BRIVARACETAM 100mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1.. | DIAZEPAM [EPILEPSY USE] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do11. | DIAZEMULS [EP] 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do12. | STESOLID [EP] 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do13. | *STESOLID 20mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do14. | STESOLID 5mg/2.5mL rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do15. | STESOLID 10mg/2.5mL rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do16. | VALIUM [EP] 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do17. | VALIUM [EP] 20mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do18. | DIAZEPAM 5mg/2.5mL RecTubes | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do19. | DIAZEPAM 10mg/2.5mL RecTubes | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1A. | DIAZEPAM 2.5mg/1.25mL RecTubes | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1B. | *DIAZEPAM 20mg/5mL RecTubes | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1t. | DIAZEPAM 2.5mg/1.25mL rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1u. | DIAZEPAM 20mg/5mL rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1v. | DIAZEPAM 10mg/2mL emulsion injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1w. | DIAZEPAM 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1x. | DIAZEPAM 5mg/2.5mL rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1y. | DIAZEPAM 10mg/2.5mL rectal solution | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do1z. | *DIAZEPAM 20mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do2.. | CLONAZEPAM [STATUS EPILEPSY] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do21. | RIVOTRIL 1mg/1mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do2z. | CLONAZEPAM 1mg/1mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do3.. | CLOMETHIAZOLE EDISYLATE [CENTRAL NERVOUS SYSTEM USE] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do31. | HEMINEVRIN [CNS] 8mg/mL intravenous infusion | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do3z. | CLOMETHIAZOLE EDISYLATE 8mg/mL intravenous infusion | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do5.. | PARALDEHYDE | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do51. | *PARALDEHYDE injection 5mL | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do52. | *PARALDEHYDE injection 10mL | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do6.. | PHENYTOIN SODIUM [STATUS EPILEPSY] | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do61. | EPANUTIN [EP] 250mg/5mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:do6z. | PHENYTOIN SODIUM 250mg/5mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ.. | EVEROLIMUS | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ1. | AFINITOR 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ2. | AFINITOR 5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ3. | VOTUBIA 2.5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ4. | VOTUBIA 5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ5. | VOTUBIA 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ7. | CERTICAN 0.25mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ8. | EVEROLIMUS 250micrograms tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQ9. | CERTICAN 0.5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQA. | EVEROLIMUS 500micrograms tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQB. | CERTICAN 0.75mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQC. | EVEROLIMUS 750micrograms tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQx. | EVEROLIMUS 2.5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQy. | EVEROLIMUS 5mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:hhQz. | EVEROLIMUS 10mg tablets | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o531. | DIAZEMULS 10mg injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o532. | *STESOLID 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o533. | *STESOLID 20mg/4mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o534. | *VALIUM 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57.. | MIDAZOLAM | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o571. | *HYPNOVEL 10mg/5mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o572. | HYPNOVEL 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o573. | BUCCOLAM 2.5mg/0.5mL oromucosal soln pre-filled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o574. | BUCCOLAM 7.5mg/1.5mL oromucosal soln pre-filled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o575. | BUCCOLAM 5mg/1mL oromucosal solution pre-filled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o576. | BUCCOLAM 10mg/2mL oromucosal solution prefilled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57r. | MIDAZOLAM 10mg/2mL oromucosal soln pre-filled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57s. | MIDAZOLAM 5mg/1mL oromucosal soln pre-filled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57t. | MIDAZOLAM 7.5mg/1.5mL oromucosal soln prefilled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57u. | MIDAZOLAM 2.5mg/0.5mL oromucosal soln prefilled oral syringe | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57v. | MIDAZOLAM 100mg/50mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57w. | MIDAZOLAM 50mg/50mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57y. | MIDAZOLAM 10mg/5mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:o57z. | MIDAZOLAM 10mg/2mL injection | Anti-seizure medication codes (excluding gabapentin, pregabalin and IV benzodiazepines) |
| READ2:d21.. | DIAZEPAM [ANXIOLYTIC] | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d211. | *DIAZEPAM 2mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d212. | *DIAZEPAM 5mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d213. | DIAZEPAM 2mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d214. | DIAZEPAM 5mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d215. | DIAZEPAM 10mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d216. | DIAZEPAM 2mg/5mL elixir | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21A. | DIAZEPAM 5mg/5mL oral solution | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21J. | DIAZEPAM 10mg/5mL suspension | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21p. | *VALIUM 2mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21q. | *VALIUM 5mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21r. | *VALIUM 2mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21s. | *VALIUM 5mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21t. | *VALIUM 10mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d21u. | *VALIUM 2mg/5mL syrup | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d2a7. | ATIVAN 4mg/mL injection | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d2ax. | LORAZEPAM 4MG/1mL injection | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:d2az. | LORAZEPAM 4MG/1mL injection | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj.. | GABAPENTIN | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj1. | GABAPENTIN 100mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj2. | GABAPENTIN 300mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj3. | GABAPENTIN 400mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj4. | NEURONTIN 100mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj5. | NEURONTIN 300mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj6. | NEURONTIN 400mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj7. | NEURONTIN 600mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj8. | NEURONTIN 800mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnj9. | NEURONTIN 300mg capsules/600mg tablets titration pack | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnjx. | GABAPENTIN 300mg capsules/600mg tablets titration pack | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnjy. | GABAPENTIN 600mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnjz. | GABAPENTIN 800mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp.. | PREGABALIN | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp1. | LYRICA 25mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp2. | LYRICA 50mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp3. | LYRICA 75mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp4. | LYRICA 100mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp5. | LYRICA 150mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp6. | LYRICA 200mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp7. | LYRICA 300mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnp8. | LYRICA 225mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpA. | LECAENT 25mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpB. | LECAENT 50mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpC. | LECAENT 75mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpD. | LECAENT 100mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpE. | LECAENT 150mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpF. | LECAENT 200mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpG. | LECAENT 225mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpH. | LECAENT 300mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpI. | REWISCA 25mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpJ. | REWISCA 50mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpK. | REWISCA 75mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpL. | REWISCA 100mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpM. | REWISCA 150mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpN. | REWISCA 200mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpO. | REWISCA 225mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpP. | REWISCA 300mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpr. | PREGABALIN 20mg/1mL oral solution | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnps. | PREGABALIN 225mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpt. | PREGABALIN 300mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpu. | PREGABALIN 200mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpv. | PREGABALIN 100mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpw. | PREGABALIN 150mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpx. | PREGABALIN 75mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpy. | PREGABALIN 50mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:dnpz. | PREGABALIN 25mg capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:do4.. | LORAZEPAM [EPILEPSY] | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:do41. | ATIVAN [EP] 4mg/mL injection | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:j81.. | DIAZEPAM [SKELETAL MUSCLE RELAXANT] | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k81.. | ACETAZOLAMIDE [GLAUCOMA] | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k811. | DIAMOX SUSTETS 500mg m/r capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k812. | DIAMOX 250mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k813. | *DIAMOX powder | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k814. | DIAMOX PARENTERAL 500mg injection | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k815. | DIAMOX SR 250mg m/r capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k81v. | *ACETAZOLAMIDE powder | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k81w. | ACETAZOLAMIDE 250mg m/r capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k81x. | ACETAZOLAMIDE 500mg m/r capsules | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k81y. | ACETAZOLAMIDE 250mg tablets | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:k81z. | ACETAZOLAMIDE 500mg injection | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:o53.. | DIAZEPAM [ANAESTHESIA] | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| READ2:o535. | *VALIUM | Excluded codes - codes excluded from anti-seizure medication (ASM) lists |
| 100011000001108 (dm+d codes) | Epilim 200mg/5ml liquid (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 101045001000027109 (dm+d codes) | Heminevrin 8mg/ml Intravenous infusion (AstraZeneca UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 101295001000027107 (dm+d codes) | Carbamazepine 100mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 101305001000027100 (dm+d codes) | Carbamazepine 200mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10225811000001107 (dm+d codes) | Lamotrigine 50mg dispersible tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 102785001000027101 (dm+d codes) | Clobazam 10mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 10287011000001104 (dm+d codes) | Lamotrigine 25mg tablets (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10287511000001107 (dm+d codes) | Lamotrigine 50mg tablets (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10308711000001109 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10356611000001109 (dm+d codes) | Clobazam 10mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10415611000001103 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Arrow Generics Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10446811000001102 (dm+d codes) | Keppra 500mg/5ml concentrate for solution for infusion vials (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10450811000001101 (dm+d codes) | Lamotrigine 25mg tablets (Arrow Generics Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10451811000001109 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Arrow Generics Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10501411000001107 (dm+d codes) | Keppra 250mg tablets (Dowelhurst Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 10503911000001103 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10543411000001100 (dm+d codes) | Lyrica 75mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10547411000001107 (dm+d codes) | Keppra 250mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10548011000001102 (dm+d codes) | Keppra 500mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 107835001000027109 (dm+d codes) | TEGRETOL liq 100 MG/5ML LIQ | Anti-seizure medications CPRD gold (all) primary care |
| 10854011000001105 (dm+d codes) | Epilim Chrono 200 tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10854211000001100 (dm+d codes) | Epilim Chrono 300 tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10854411000001101 (dm+d codes) | Epilim Chrono 500 tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10854611000001103 (dm+d codes) | Epilim 500 gastro-resistant tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 10854811000001104 (dm+d codes) | Epilim 200mg/5ml liquid (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 108855001000027104 (dm+d codes) | Carbamazepine 200mg Modified-release tablet (Generics (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 108865001000027108 (dm+d codes) | Carbamazepine 400mg Modified-release tablet (Generics (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 109855001000027101 (dm+d codes) | Diazepam 5mg suppository | Anti-seizure medications CPRD gold (all) primary care |
| 11089411000001104 (dm+d codes) | Sodium valproate 300mg/3ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 11141611000001101 (dm+d codes) | Depakote 125mg sprinkle gastro-resistant capsules (Imported (United States)) | Anti-seizure medications CPRD gold (all) primary care |
| 11146711000001104 (dm+d codes) | Valproic acid 125mg gastro-resistant capsules | Anti-seizure medications CPRD gold (all) primary care |
| 11383911000001108 (dm+d codes) | Primidone 125mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 11475111000001108 (dm+d codes) | Sodium valproate 150mg modified-release capsules | Anti-seizure medications CPRD gold (all) primary care |
| 11475211000001102 (dm+d codes) | Sodium valproate 300mg modified-release capsules | Anti-seizure medications CPRD gold (all) primary care |
| 11475311000001105 (dm+d codes) | Sodium valproate 500mg modified-release granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 11475411000001103 (dm+d codes) | Sodium valproate 1g modified-release granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 11475611000001100 (dm+d codes) | Episenta 150mg modified-release capsules (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11475911000001106 (dm+d codes) | Episenta 300mg modified-release capsules (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11476211000001108 (dm+d codes) | Episenta 500mg modified-release granules sachets (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11476511000001106 (dm+d codes) | Episenta 1000mg modified-release granules sachets (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 114811000001105 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11485111000001102 (dm+d codes) | Primidone 250mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 11500511000001106 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11500711000001101 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11500911000001104 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11532011000001106 (dm+d codes) | Gabapentin 100mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11652711000001100 (dm+d codes) | Acetazolamide 40mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 11654611000001101 (dm+d codes) | Acetazolamide 50mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 117311000001105 (dm+d codes) | Emeside 250mg capsules (Fontus Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 118005001000027107 (dm+d codes) | Carbamazepine sr 200mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 118025001000027100 (dm+d codes) | Carbamazepine sr 400mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 119011000001103 (dm+d codes) | Sodium valproate 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 11944611000001102 (dm+d codes) | Clonazepam 125micrograms/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 11944711000001106 (dm+d codes) | Clonazepam 125micrograms/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 11955111000001107 (dm+d codes) | Clonazepam 25micrograms/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 11955611000001104 (dm+d codes) | Clonazepam 312.5micrograms/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 11956511000001105 (dm+d codes) | Clonazepam 50micrograms/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12022011000001107 (dm+d codes) | Clobazam 1.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12022211000001102 (dm+d codes) | Clobazam 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12024011000001101 (dm+d codes) | Clobazam 7.5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12024111000001100 (dm+d codes) | Clobazam 7.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12089111000001105 (dm+d codes) | Gabapentin 150mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12089311000001107 (dm+d codes) | Gabapentin 200mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12089511000001101 (dm+d codes) | Gabapentin 500mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12095001000027109 (dm+d codes) | Frisium 10mg Capsule (Aventis Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 12152911000001100 (dm+d codes) | Phenobarbital 10mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 12178011000001104 (dm+d codes) | Phenobarbital 45mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 12186711000001109 (dm+d codes) | Phenobarbital 10mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12187211000001100 (dm+d codes) | Phenobarbital 150mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12188111000001107 (dm+d codes) | Phenobarbital 20mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12189011000001101 (dm+d codes) | Phenobarbital 250mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12189511000001109 (dm+d codes) | Phenobarbital 30mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12189811000001107 (dm+d codes) | Phenobarbital 34mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12191711000001104 (dm+d codes) | Phenobarbital 60mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12205211000001109 (dm+d codes) | Phenobarbital 15mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 12212911000001106 (dm+d codes) | Phenobarbital 15mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12213011000001103 (dm+d codes) | Phenobarbital 15mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12213111000001102 (dm+d codes) | Phenobarbital 25mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12213211000001108 (dm+d codes) | Phenobarbital 25mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12213511000001106 (dm+d codes) | Phenobarbital 5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12214011000001101 (dm+d codes) | Phenobarbital 75mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12214111000001100 (dm+d codes) | Phenobarbital 75mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 122211000001108 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 12249711000001107 (dm+d codes) | Phenobarbital 100mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 12299311000001101 (dm+d codes) | Phenobarbital 100mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 12299411000001108 (dm+d codes) | Phenobarbital 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 12299611000001106 (dm+d codes) | Phenobarbital 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12311000001104 (dm+d codes) | Teril Retard 200mg tablets (Taro Pharmaceuticals (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 12323011000001102 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 12326711000001107 (dm+d codes) | Carbamazepine 200mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 12387511000001107 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12387711000001102 (dm+d codes) | Carbamazepine 10mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12425011000001109 (dm+d codes) | Phenobarbital 10mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 12425511000001101 (dm+d codes) | Phenobarbital 60mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 125145001000027104 (dm+d codes) | Methylphenobarbital 30mg Tablet | Anti-seizure medications CPRD gold (all) primary care |
| 125155001000027101 (dm+d codes) | Methylphenobarbital 60mg Tablet | Anti-seizure medications CPRD gold (all) primary care |
| 125165001000027105 (dm+d codes) | Methylphenobarbital 200mg Tablet | Anti-seizure medications CPRD gold (all) primary care |
| 12644511000001103 (dm+d codes) | Lamotrigine 15mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12644711000001108 (dm+d codes) | Lamotrigine 200mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12645211000001100 (dm+d codes) | Lamotrigine 5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12645411000001101 (dm+d codes) | Levetiracetam 250mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 12645511000001102 (dm+d codes) | Levetiracetam 250mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 12645611000001103 (dm+d codes) | Levetiracetam 400mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 126655001000027104 (dm+d codes) | Sodium valproate 200mg/5ml Oral solution (Hillcross Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 12862111000001104 (dm+d codes) | Inovelon 100mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 12865211000001100 (dm+d codes) | Rufinamide 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 12948611000001108 (dm+d codes) | Gabapentin 100mg capsules (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 12949111000001107 (dm+d codes) | Gabapentin 300mg capsules (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13016311000001107 (dm+d codes) | Vigabatrin 350mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13016411000001100 (dm+d codes) | Vigabatrin 500mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13041211000001104 (dm+d codes) | Phenytoin sodium 84mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13076011000001103 (dm+d codes) | Lyrica 225mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13117911000001104 (dm+d codes) | Sodium valproate 1g/10ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 13123911000001104 (dm+d codes) | Inovelon 200mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13124211000001106 (dm+d codes) | Inovelon 400mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13162911000001100 (dm+d codes) | Epanutin 100mg capsules (Dowelhurst Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13301111000001104 (dm+d codes) | Sodium valproate 500mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13301211000001105 (dm+d codes) | Sodium valproate 600mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13301311000001102 (dm+d codes) | Sodium valproate 60mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13324511000001102 (dm+d codes) | Topiramate 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13324711000001107 (dm+d codes) | Topiramate 12.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13324811000001104 (dm+d codes) | Topiramate 125mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13355211000001100 (dm+d codes) | Topiramate 100mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13355411000001101 (dm+d codes) | Topiramate 10mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13355511000001102 (dm+d codes) | Topiramate 12.5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13355711000001107 (dm+d codes) | Topiramate 12mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13355911000001109 (dm+d codes) | Topiramate 12mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13356411000001105 (dm+d codes) | Topiramate 20mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13356611000001108 (dm+d codes) | Topiramate 20mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13356711000001104 (dm+d codes) | Topiramate 30mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13356811000001107 (dm+d codes) | Topiramate 30mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13356911000001102 (dm+d codes) | Topiramate 5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13387511000001103 (dm+d codes) | Gabapentin 300mg capsules (Arrow Generics Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13403211000001101 (dm+d codes) | Diacomit 250mg oral powder sachets (Alan Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13411111000001108 (dm+d codes) | Stiripentol 250mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 13411211000001102 (dm+d codes) | Stiripentol 250mg oral powder sachets | Anti-seizure medications CPRD gold (all) primary care |
| 13411311000001105 (dm+d codes) | Stiripentol 500mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 13411411000001103 (dm+d codes) | Stiripentol 500mg oral powder sachets | Anti-seizure medications CPRD gold (all) primary care |
| 13436711000001105 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13436911000001107 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 134565001000027108 (dm+d codes) | Phenytoin 25mg capsule | Anti-seizure medications CPRD gold (all) primary care |
| 134575001000027101 (dm+d codes) | Phenytoin 50mg capsule | Anti-seizure medications CPRD gold (all) primary care |
| 134595001000027105 (dm+d codes) | Phenytoin 100mg capsule | Anti-seizure medications CPRD gold (all) primary care |
| 134605001000027102 (dm+d codes) | Phenytoin 300mg capsule | Anti-seizure medications CPRD gold (all) primary care |
| 13565811000001105 (dm+d codes) | Gabapentin 600mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13566011000001108 (dm+d codes) | Gabapentin 600mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 13567111000001107 (dm+d codes) | Lyrica 50mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 13649111000001102 (dm+d codes) | Phenytoin sodium 250mg/5ml solution for injection ampoules (Alliance Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13653211000001108 (dm+d codes) | Clonazepam 500microgram tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13665411000001101 (dm+d codes) | Epilim Chronosphere MR 100mg granules sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 13665711000001107 (dm+d codes) | Epilim Chronosphere MR 250mg granules sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 13665911000001109 (dm+d codes) | Epilim Chronosphere MR 500mg granules sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 13666311000001103 (dm+d codes) | Epilim Chronosphere MR 750mg granules sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 13666611000001108 (dm+d codes) | Epilim Chronosphere MR 50mg granules sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 13718611000001103 (dm+d codes) | Sodium valproate 100mg modified-release granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 13718711000001107 (dm+d codes) | Sodium valproate 250mg modified-release granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 13718811000001104 (dm+d codes) | Sodium valproate 50mg modified-release granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 13718911000001109 (dm+d codes) | Sodium valproate 750mg modified-release granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 13722811000001106 (dm+d codes) | Gabapentin 300mg capsules (Ranbaxy (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13753511000001102 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Tillomed Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 138611000001109 (dm+d codes) | Topamax 50mg tablets (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 13891811000001106 (dm+d codes) | Phenytoin 90mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 13893911000001100 (dm+d codes) | Phenytoin 90mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 13917811000001106 (dm+d codes) | Lamictal 25mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13918011000001104 (dm+d codes) | Lamictal 50mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13928311000001105 (dm+d codes) | Lyrica 50mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13928511000001104 (dm+d codes) | Lyrica 75mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13985811000001103 (dm+d codes) | Tegretol 100mg/5ml liquid (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13986611000001107 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 13987711000001100 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 14010811000001103 (dm+d codes) | Gabapentin 400mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 14014011000001102 (dm+d codes) | Gabapentin 400mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 14016711000001109 (dm+d codes) | Pregabalin 75mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 14016811000001101 (dm+d codes) | Pregabalin 75mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 14055611000001100 (dm+d codes) | Lamotrigine 25mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 14194411000001101 (dm+d codes) | Vimpat 200mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14194911000001109 (dm+d codes) | Vimpat 50mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14196211000001105 (dm+d codes) | Vimpat 200mg/20ml solution for infusion vials (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14196911000001101 (dm+d codes) | Vimpat 150mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14199511000001103 (dm+d codes) | Vimpat 100mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14203611000001101 (dm+d codes) | Lacosamide 200mg/20ml solution for infusion vials | Anti-seizure medications CPRD gold (all) primary care |
| 14220911000001108 (dm+d codes) | Epilim Chrono 200 tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14252711000001109 (dm+d codes) | Gabapentin 800mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 142605001000027105 (dm+d codes) | Sodium valproate CR 300mg Tablet (Hillcross Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 142611000001108 (dm+d codes) | Stesolid 10mg rectal tube (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14262811000001106 (dm+d codes) | Keppra 100mg/ml oral solution (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14263111000001105 (dm+d codes) | Keppra 250mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14263511000001101 (dm+d codes) | Keppra 500mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 142645001000027100 (dm+d codes) | Sodium valproate CR 500mg Tablet (Hillcross Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14316311000001106 (dm+d codes) | Vimpat 15mg/ml syrup (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 14376511000001105 (dm+d codes) | Lyrica 100mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14377511000001107 (dm+d codes) | Lyrica 150mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14410411000001105 (dm+d codes) | Lacosamide 15mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 14593611000001108 (dm+d codes) | Zonegran 100mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14624511000001108 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14624811000001106 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14664211000001104 (dm+d codes) | Rivotril 2mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14685311000001109 (dm+d codes) | Trileptal 300mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14738811000001108 (dm+d codes) | Lamictal 25mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 14770211000001106 (dm+d codes) | Phenytoin sodium 100mg tablets (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15047811000001103 (dm+d codes) | Mysoline 250mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15056411000001104 (dm+d codes) | Lamotrigine 100mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15075911000001102 (dm+d codes) | Carbamazepine 400mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15076411000001101 (dm+d codes) | Carbamazepine 200mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15076811000001104 (dm+d codes) | Carbamazepine 200mg modified-release tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15077211000001103 (dm+d codes) | Clonazepam 2mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15105511000001108 (dm+d codes) | Lamotrigine 50mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15125311000001109 (dm+d codes) | Pregabalin 150mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 15125411000001102 (dm+d codes) | Pregabalin 150mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 15165011000001104 (dm+d codes) | Gabapentin 600mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15166711000001105 (dm+d codes) | Oxcarbazepine 300mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15175811000001104 (dm+d codes) | Sodium valproate 300mg modified-release tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 15243311000001108 (dm+d codes) | Pregabalin 200mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 15243411000001101 (dm+d codes) | Pregabalin 200mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 15356811000001101 (dm+d codes) | Gabapentin 600mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15439411000001102 (dm+d codes) | Epilim Chronosphere MR 1000mg granules sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 15451911000001105 (dm+d codes) | Primidone 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 15535811000001106 (dm+d codes) | Valproic acid 250mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 15536811000001103 (dm+d codes) | Valproic acid 250mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 15621611000001101 (dm+d codes) | Phenytoin 300mg/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 15621911000001107 (dm+d codes) | Phenytoin 300mg/5ml oral suspension (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 15627711000001101 (dm+d codes) | Clonazepam 500microgram tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15628011000001102 (dm+d codes) | Clobazam 10mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15632911000001103 (dm+d codes) | Phenytoin 300mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 156945001000027109 (dm+d codes) | Diazepam 5mg Rectal tubes (Hillcross Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 157005001000027109 (dm+d codes) | Diazepam 10mg Rectal tubes (Hillcross Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15849411000001105 (dm+d codes) | Oxcarbazepine 150mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15849611000001108 (dm+d codes) | Oxcarbazepine 300mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 15915211000001106 (dm+d codes) | Pregabalin 25mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 159611000001104 (dm+d codes) | Neurontin 800mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16056111000001107 (dm+d codes) | Afinitor 10mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16058511000001102 (dm+d codes) | Lamotrigine 25mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16059011000001100 (dm+d codes) | Lamotrigine 50mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16059211000001105 (dm+d codes) | Lamotrigine 100mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16085211000001103 (dm+d codes) | Topiramate 25mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16086111000001103 (dm+d codes) | Topiramate 200mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16091111000001106 (dm+d codes) | Topiramate 15mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 16091211000001100 (dm+d codes) | Topiramate 15mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 16102311000001106 (dm+d codes) | Valproic acid 500mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 16102411000001104 (dm+d codes) | Valproic acid 500mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 16168411000001101 (dm+d codes) | Topiramate 25mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16172011000001103 (dm+d codes) | Epilim Chrono 200 tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16172211000001108 (dm+d codes) | Epilim Chrono 300 tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16172411000001107 (dm+d codes) | Epilim Chrono 500 tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16172611000001105 (dm+d codes) | Epilim 200mg/5ml syrup (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16177011000001101 (dm+d codes) | Topiramate 25mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16177211000001106 (dm+d codes) | Topiramate 50mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16177411000001105 (dm+d codes) | Topiramate 25mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16177611000001108 (dm+d codes) | Topiramate 50mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16177911000001102 (dm+d codes) | Topiramate 100mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16178611000001107 (dm+d codes) | Zebinix 800mg tablets (BIAL Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16185611000001106 (dm+d codes) | Topiramate 15mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16185811000001105 (dm+d codes) | Topiramate 25mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16186011000001108 (dm+d codes) | Topiramate 50mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16186411000001104 (dm+d codes) | Topiramate 50mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16186611000001101 (dm+d codes) | Topiramate 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16193811000001107 (dm+d codes) | Keppra 100mg/ml oral solution (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16194611000001106 (dm+d codes) | Lamictal 25mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16195311000001102 (dm+d codes) | Lamictal 200mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16195611000001107 (dm+d codes) | Lamictal 25mg dispersible tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16197411000001103 (dm+d codes) | Eslicarbazepine 800mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 16204211000001109 (dm+d codes) | Lyrica 25mg capsules (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16204811000001105 (dm+d codes) | Lyrica 50mg capsules (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16205111000001104 (dm+d codes) | Lyrica 75mg capsules (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16205511000001108 (dm+d codes) | Lyrica 150mg capsules (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16208711000001105 (dm+d codes) | Mysoline 250mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16263711000001103 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16264811000001109 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16266611000001101 (dm+d codes) | Tegretol 200mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16267311000001109 (dm+d codes) | Tegretol 400mg tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16267611000001104 (dm+d codes) | Tegretol 100mg/5ml liquid (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 162715001000027106 (dm+d codes) | Epilim ec 200mg Gastro-resistant tablet (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 162725001000027102 (dm+d codes) | Epilim ec 500mg Gastro-resistant tablet (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 16516411000001108 (dm+d codes) | Lyrica 50mg capsules (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16534511000001105 (dm+d codes) | Lamictal 25mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16534711000001100 (dm+d codes) | Lamictal 50mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16583311000001107 (dm+d codes) | Lyrica 75mg capsules (Stephar (U.K.) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 16632811000001106 (dm+d codes) | Paraldehyde 50% in Olive oil rectal solution (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 16634911000001105 (dm+d codes) | Paraldehyde 50% in Olive oil rectal solution | Anti-seizure medications CPRD gold (all) primary care |
| 16677911000001101 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Stephar (U.K.) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17020811000001104 (dm+d codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 17020911000001109 (dm+d codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 17021011000001101 (dm+d codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 17021111000001100 (dm+d codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 17111000001104 (dm+d codes) | Phenytoin sodium 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17298211000001101 (dm+d codes) | Rivotril 500microgram tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 17459311000001107 (dm+d codes) | Tegretol 400mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17459711000001106 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 174985001000027109 (dm+d codes) | Clonazepam 500microgram/5ml Oral solution (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17511811000001101 (dm+d codes) | Keppra 250mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17512011000001104 (dm+d codes) | Keppra 750mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17569111000001106 (dm+d codes) | Lyrica 300mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 17575611000001109 (dm+d codes) | Topiramate 25mg capsules (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 176211000001108 (dm+d codes) | Phenobarbital 60mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 177785001000027109 (dm+d codes) | Vigabatrin 125mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 17822611000001103 (dm+d codes) | Topiramate 25mg capsules (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17822911000001109 (dm+d codes) | Topiramate 50mg capsules (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17824311000001101 (dm+d codes) | Carbamazepine 200mg modified-release tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17824511000001107 (dm+d codes) | Carbamazepine 400mg modified-release tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17824711000001102 (dm+d codes) | Carbamazepine 100mg tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17824911000001100 (dm+d codes) | Carbamazepine 200mg tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 178425001000027101 (dm+d codes) | Gabapentin 250mg/5ml Oral solution (Boots Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17845001000027104 (dm+d codes) | Phenobarbital 15mg Tablet (Celltech Pharma Europe Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17855001000027101 (dm+d codes) | Phenobarbital 30mg Tablet (Celltech Pharma Europe Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17861111000001106 (dm+d codes) | Clonazepam 500microgram tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17865001000027105 (dm+d codes) | Phenobarbital 60mg Tablet (Celltech Pharma Europe Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17870411000001103 (dm+d codes) | Clonazepam 500microgram orodispersible tablets | Anti-seizure medications CPRD gold (all) primary care |
| 17895001000027107 (dm+d codes) | Phenobarbital 15mg/5ml Oral solution (William Ransom) | Anti-seizure medications CPRD gold (all) primary care |
| 17913811000001107 (dm+d codes) | Gabapentin 300mg capsules (Phoenix Healthcare Distribution Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17945001000027109 (dm+d codes) | Phenytoin 50mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17955001000027107 (dm+d codes) | Phenytoin 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17964111000001104 (dm+d codes) | Phenobarbital 30mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17966511000001102 (dm+d codes) | Clonazepam 500microgram tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17971011000001105 (dm+d codes) | Gabapentin 100mg capsules (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17971411000001101 (dm+d codes) | Gabapentin 300mg capsules (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17971811000001104 (dm+d codes) | Gabapentin 400mg capsules (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17985001000027100 (dm+d codes) | Phenytoin 100mg Capsule (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 17999911000001103 (dm+d codes) | Clonazepam 500microgram oral lyophilisates sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 18047011000001103 (dm+d codes) | Ammonium bromide 400mg/5ml / Potassium bromide 400mg/5ml / Sodium bromide 400mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 18047111000001102 (dm+d codes) | Triple Bromide 1.2g/5ml oral solution (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 18061611000001109 (dm+d codes) | Keppra 1g tablets (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18078411000001107 (dm+d codes) | Lamotrigine 25mg tablets (Fannin (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18084111000001100 (dm+d codes) | Zonisamide 50mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 18084211000001106 (dm+d codes) | Zonisamide 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 18155711000001103 (dm+d codes) | Topamax 25mg sprinkle capsules (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18195711000001107 (dm+d codes) | Tegretol 100mg/5ml liquid (Necessity Supplies Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18195911000001109 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Necessity Supplies Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18196211000001106 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Necessity Supplies Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18196611000001108 (dm+d codes) | Tegretol 200mg tablets (Necessity Supplies Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18196811000001107 (dm+d codes) | Tegretol 400mg tablets (Necessity Supplies Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18270711000001108 (dm+d codes) | Keppra 250mg tablets (Necessity Supplies Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18389711000001104 (dm+d codes) | Clobazam 10mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 184311000001104 (dm+d codes) | Sabril 500mg tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 18455311000001101 (dm+d codes) | Mysoline 50mg tablets (SERB) | Anti-seizure medications CPRD gold (all) primary care |
| 18469511000001101 (dm+d codes) | Topiramate 25mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18469711000001106 (dm+d codes) | Topiramate 50mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18520211000001109 (dm+d codes) | Paraldehyde 50% in Arachis oil rectal solution | Anti-seizure medications CPRD gold (all) primary care |
| 185711000001101 (dm+d codes) | Epanutin 30mg/5ml oral suspension (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18576511000001108 (dm+d codes) | Epilim Chrono 200 tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 18576711000001103 (dm+d codes) | Epilim Chrono 300 tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 18576911000001101 (dm+d codes) | Epilim Chrono 500 tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 18577111000001101 (dm+d codes) | Epilim 200mg/5ml syrup (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 18606911000001100 (dm+d codes) | Primidone 250mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 18610411000001108 (dm+d codes) | Rivotril 500microgram tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 186311000001105 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 187111000001106 (dm+d codes) | Phenobarbital 30mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18742911000001103 (dm+d codes) | Topiramate 25mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 18769311000001102 (dm+d codes) | Trobalt 50mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18769811000001106 (dm+d codes) | Trobalt 400mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18770111000001101 (dm+d codes) | Trobalt 300mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18770411000001106 (dm+d codes) | Trobalt 200mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18770811000001108 (dm+d codes) | Trobalt 100mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 18772111000001102 (dm+d codes) | Retigabine 50mg tablets and Retigabine 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 18781211000001106 (dm+d codes) | Phenytoin sodium 100mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19174011000001104 (dm+d codes) | Topamax 15mg sprinkle capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 191911000001102 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 194275001000027103 (dm+d codes) | Carbamazepine 500mg/5ml Oral suspension (Martindale Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19472111000001105 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19472511000001101 (dm+d codes) | Levetiracetam 250mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19472711000001106 (dm+d codes) | Levetiracetam 500mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19472911000001108 (dm+d codes) | Levetiracetam 750mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19484711000001106 (dm+d codes) | Levetiracetam 250mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19484911000001108 (dm+d codes) | Levetiracetam 500mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19490111000001100 (dm+d codes) | Levetiracetam 250mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19490311000001103 (dm+d codes) | Levetiracetam 500mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19491711000001107 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19530211000001109 (dm+d codes) | Buccolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19530511000001107 (dm+d codes) | Buccolam 5mg/1ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19530811000001105 (dm+d codes) | Buccolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19531111000001109 (dm+d codes) | Buccolam 10mg/2ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 195385001000027109 (dm+d codes) | Sodium valproate with valproic acid 200mg modified release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 195395001000027108 (dm+d codes) | Sodium valproate with valproic acid 300mg modified release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 195405001000027100 (dm+d codes) | Sodium valproate with valproic acid 500mg modified release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 19570411000001105 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19617711000001104 (dm+d codes) | Mysoline 250mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 196211000001103 (dm+d codes) | Carbamazepine 200mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19632511000001100 (dm+d codes) | Levetiracetam 500mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19632711000001105 (dm+d codes) | Levetiracetam 750mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19633111000001103 (dm+d codes) | Levetiracetam 250mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19657311000001109 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19664811000001102 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19665211000001102 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 196675001000027107 (dm+d codes) | Phenytoin 90mg/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 19744011000001106 (dm+d codes) | Everolimus 2.5mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 19817511000001100 (dm+d codes) | Carbamazepine 100mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19817711000001105 (dm+d codes) | Carbamazepine 200mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19817911000001107 (dm+d codes) | Carbamazepine 400mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19821611000001100 (dm+d codes) | Lacosamide 10mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 19843411000001102 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19861211000001109 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19868011000001105 (dm+d codes) | Matever 750mg tablets (Aspire Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19868411000001101 (dm+d codes) | Matever 500mg tablets (Aspire Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19868711000001107 (dm+d codes) | Matever 250mg tablets (Aspire Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 198711000001109 (dm+d codes) | Epanutin 300mg capsules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 19976511000001103 (dm+d codes) | Paraldehyde 50% in Sunflower oil rectal solution | Anti-seizure medications CPRD gold (all) primary care |
| 19977911000001108 (dm+d codes) | Sodium valproate 500mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 199911000001103 (dm+d codes) | Epanutin 25mg capsules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 200005001000027106 (dm+d codes) | Diazepam 20mg rectal tubes | Anti-seizure medications CPRD gold (all) primary care |
| 20018711000001105 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20019211000001108 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20028611000001107 (dm+d codes) | Topamax 50mg sprinkle capsules (Lexon (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20065611000001108 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 20128211000001100 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 20167011000001102 (dm+d codes) | Lamotrigine 25mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20167211000001107 (dm+d codes) | Lamotrigine 50mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20167411000001106 (dm+d codes) | Lamotrigine 100mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20167611000001109 (dm+d codes) | Lamotrigine 200mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20168111000001100 (dm+d codes) | Levetiracetam 250mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20168311000001103 (dm+d codes) | Levetiracetam 500mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20168511000001109 (dm+d codes) | Levetiracetam 750mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20168711000001104 (dm+d codes) | Levetiracetam 1g tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20343811000001100 (dm+d codes) | Inovelon 40mg/ml oral suspension (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20353211000001104 (dm+d codes) | Rufinamide 40mg/ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 20353711000001106 (dm+d codes) | Vimpat 10mg/ml syrup (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20359311000001105 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20385001000027101 (dm+d codes) | Mysoline 250mg Tablet (AstraZeneca UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20395001000027102 (dm+d codes) | Mysoline 250mg/5ml Oral suspension (AstraZeneca UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 204111000001102 (dm+d codes) | Gardenal Sodium 200mg/1ml solution for injection ampoules (Concord Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20451011000001102 (dm+d codes) | Vimpat 50mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 205311000001101 (dm+d codes) | Carbamazepine 400mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20536511000001107 (dm+d codes) | Acetazolamide 250mg tablets (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 205411000001108 (dm+d codes) | Phenobarbital 60mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20545811000001103 (dm+d codes) | Lyrica 20mg/ml oral solution (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20556411000001107 (dm+d codes) | Pregabalin 20mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 20560511000001102 (dm+d codes) | Epilim Chronosphere MR 100mg granules sachets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 206611000001101 (dm+d codes) | Carbamazepine 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 208611000001100 (dm+d codes) | Epanutin 50mg capsules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20901711000001105 (dm+d codes) | Topiramate 25mg tablets (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20910411000001105 (dm+d codes) | Topiramate 15mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20910611000001108 (dm+d codes) | Topiramate 25mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20910811000001107 (dm+d codes) | Topiramate 50mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20914811000001102 (dm+d codes) | Levetiracetam 250mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20915011000001107 (dm+d codes) | Levetiracetam 500mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20915211000001102 (dm+d codes) | Levetiracetam 750mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 20915411000001103 (dm+d codes) | Levetiracetam 1g tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21025111000001104 (dm+d codes) | Phenytoin sodium 100mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21028311000001106 (dm+d codes) | Levetiracetam 250mg tablets (Arrow Generics Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21032911000001107 (dm+d codes) | Gabapentin 100mg capsules (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21033111000001103 (dm+d codes) | Gabapentin 300mg capsules (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21033311000001101 (dm+d codes) | Gabapentin 400mg capsules (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21039111000001100 (dm+d codes) | Phenobarbital 15mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21039311000001103 (dm+d codes) | Phenobarbital 30mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21039511000001109 (dm+d codes) | Phenobarbital 60mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 210755001000027102 (dm+d codes) | Diazepam rectubes 20mg Rectal tubes (C P Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21200511000001100 (dm+d codes) | Phenytoin sodium 25mg capsules (Flynn Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21200711000001105 (dm+d codes) | Phenytoin sodium 50mg capsules (Flynn Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21200911000001107 (dm+d codes) | Phenytoin sodium 100mg capsules (Flynn Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21201111000001103 (dm+d codes) | Phenytoin sodium 300mg capsules (Flynn Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21212111000001106 (dm+d codes) | Fycompa 2mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21212611000001103 (dm+d codes) | Fycompa 4mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21213011000001101 (dm+d codes) | Fycompa 6mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21213311000001103 (dm+d codes) | Fycompa 8mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21213611000001108 (dm+d codes) | Fycompa 10mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21213911000001102 (dm+d codes) | Fycompa 12mg tablets (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21282711000001105 (dm+d codes) | Gabapentin 600mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21290611000001103 (dm+d codes) | Midazolam 2.5mg/0.25ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 21348611000001102 (dm+d codes) | Phenytoin sodium 25mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21349211000001109 (dm+d codes) | Phenytoin sodium 50mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21349411000001108 (dm+d codes) | Phenytoin sodium 100mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21349711000001102 (dm+d codes) | Phenytoin sodium 300mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21374911000001100 (dm+d codes) | Phenytoin sodium 25mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21375111000001104 (dm+d codes) | Phenytoin sodium 50mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21375311000001102 (dm+d codes) | Phenytoin sodium 100mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21375511000001108 (dm+d codes) | Phenytoin sodium 300mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21658711000001101 (dm+d codes) | Gabapentin 50mg/ml oral solution sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21660111000001105 (dm+d codes) | Gabapentin 50mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 21696311000001108 (dm+d codes) | Gabapentin 50mg/ml oral solution sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 217211000001104 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21730711000001109 (dm+d codes) | Desitrend 250mg granules sachets (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21731111000001102 (dm+d codes) | Desitrend 500mg granules sachets (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21731611000001105 (dm+d codes) | Desitrend 1000mg granules sachets (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21733211000001107 (dm+d codes) | Levetiracetam 1g granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 21733311000001104 (dm+d codes) | Levetiracetam 250mg granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 21733411000001106 (dm+d codes) | Levetiracetam 500mg granules sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 21802811000001108 (dm+d codes) | Tapclob 5mg/5ml oral suspension (Martindale Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21803611000001104 (dm+d codes) | Tapclob 10mg/5ml oral suspension (Martindale Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 21816611000001107 (dm+d codes) | Carbamazepine 100mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 21817311000001104 (dm+d codes) | Carbamazepine 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 21846411000001103 (dm+d codes) | Phenobarbital 30mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 21846811000001101 (dm+d codes) | Phenytoin sodium 100mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 21856411000001100 (dm+d codes) | Clobazam 10mg/5ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 21856511000001101 (dm+d codes) | Clobazam 5mg/5ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 21885111000001107 (dm+d codes) | Topiramate 50mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 21900611000001102 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 220011000001104 (dm+d codes) | Orlept 500mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 22019411000001102 (dm+d codes) | Gabapentin 300mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 22019611000001104 (dm+d codes) | Gabapentin 400mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 22057311000001105 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 22058811000001102 (dm+d codes) | Lamotrigine 25mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 22060711000001100 (dm+d codes) | Lamotrigine 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 22082011000001101 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 22195001000027100 (dm+d codes) | Nydrane 500mg Tablet (Lipha Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 223295001000027101 (dm+d codes) | Stesolid 10mg Rectal tubes (Dumex Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 22349411000001109 (dm+d codes) | Gabapentin 600mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 224395001000027108 (dm+d codes) | Gabitril 5mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 224405001000027100 (dm+d codes) | Gabitril 10mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 224415001000027103 (dm+d codes) | Gabitril 15mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 22629711000001105 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 22629911000001107 (dm+d codes) | Carbamazepine 100mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 22630111000001101 (dm+d codes) | Carbamazepine 200mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 22630311000001104 (dm+d codes) | Carbamazepine 400mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 22663911000001101 (dm+d codes) | Sodium valproate 400mg/4ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 23167411000001105 (dm+d codes) | Desitrend 100mg/ml oral solution (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23180311000001102 (dm+d codes) | Primidone 50mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23180511000001108 (dm+d codes) | Primidone 250mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23223411000001109 (dm+d codes) | Sodium valproate 500mg modified-release tablets (J M McGill Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23305711000001100 (dm+d codes) | Primidone 250mg tablets (SERB) | Anti-seizure medications CPRD gold (all) primary care |
| 23305911000001103 (dm+d codes) | Primidone 50mg tablets (SERB) | Anti-seizure medications CPRD gold (all) primary care |
| 233611000001104 (dm+d codes) | Rivotril 500microgram tablets (Roche Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23407511000001107 (dm+d codes) | Gabapentin 300mg capsules (Medreich Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 234145001000027105 (dm+d codes) | Timonil retard 400mg Modified-release tablet (C P Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23466511000001106 (dm+d codes) | Clonazepam 2.5mg/ml drops | Anti-seizure medications CPRD gold (all) primary care |
| 23480211000001109 (dm+d codes) | Primidone 250mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 235111000001108 (dm+d codes) | Topamax 200mg tablets (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23587811000001101 (dm+d codes) | Levetiracetam 250mg tablets (Bristol Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23595311000001103 (dm+d codes) | Phenytoin sodium 100mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23600711000001100 (dm+d codes) | Primidone 250mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 23614511000001103 (dm+d codes) | Gabapentin 300mg capsules (Creo Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23640811000001104 (dm+d codes) | Primidone 50mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 236505001000027100 (dm+d codes) | Epistatus 10mg/ml Oromucosal solution (Special Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 23675911000001104 (dm+d codes) | Lorazepam 2mg/1ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 240511000001105 (dm+d codes) | Phenobarbital 30mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 240965001000027100 (dm+d codes) | Ospolot fc 50mg Tablet (IDIS World Medicines) | Anti-seizure medications CPRD gold (all) primary care |
| 240985001000027102 (dm+d codes) | Ospolot fc 200mg Tablet (IDIS World Medicines) | Anti-seizure medications CPRD gold (all) primary care |
| 24104211000001101 (dm+d codes) | Afinitor 2.5mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 24104911000001105 (dm+d codes) | Gabapentin 300mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 24105111000001106 (dm+d codes) | Gabapentin 400mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 24105511000001102 (dm+d codes) | Gabapentin 600mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 24108311000001104 (dm+d codes) | Carbagen 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 24108811000001108 (dm+d codes) | Carbagen 200mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 24109211000001102 (dm+d codes) | Carbagen 400mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 241345001000027106 (dm+d codes) | Clonazepam 500micrograms/5ml solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 24354811000001102 (dm+d codes) | Lamotrigine 25mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 24355011000001107 (dm+d codes) | Lamotrigine 50mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 24365411000001108 (dm+d codes) | Levetiracetam 250mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 245125001000027101 (dm+d codes) | Phenobarbital oral liquid | Anti-seizure medications CPRD gold (all) primary care |
| 245615001000027106 (dm+d codes) | Carbamazepine oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 24595411000001108 (dm+d codes) | Zonisamide 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 24595511000001107 (dm+d codes) | Zonisamide 25mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 246675001000027100 (dm+d codes) | Levetiracetam Oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 248115001000027103 (dm+d codes) | Midazolam Oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 250015001000027101 (dm+d codes) | Phenobarbital capsule | Anti-seizure medications CPRD gold (all) primary care |
| 250155001000027102 (dm+d codes) | Primidone 100mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 250805001000027102 (dm+d codes) | Mesuximide 300mg Capsule | Anti-seizure medications CPRD gold (all) primary care |
| 251405001000027102 (dm+d codes) | Phenytoin sodium oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 251415001000027100 (dm+d codes) | Phenobarbital sodium oral liquid | Anti-seizure medications CPRD gold (all) primary care |
| 251711000001106 (dm+d codes) | Epanutin Infatabs 50mg chewable tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 251925001000027106 (dm+d codes) | Sodium valproate with valproic acid 100mg modified release granules | Anti-seizure medications CPRD gold (all) primary care |
| 251945001000027109 (dm+d codes) | Sodium valproate with valproic acid 250mg modified release granules | Anti-seizure medications CPRD gold (all) primary care |
| 251965001000027103 (dm+d codes) | Sodium valproate with valproic acid 500mg modified release granules | Anti-seizure medications CPRD gold (all) primary care |
| 251975001000027105 (dm+d codes) | Sodium valproate with valproic acid 750mg modified release granules | Anti-seizure medications CPRD gold (all) primary care |
| 251985001000027100 (dm+d codes) | Sodium valproate with valproic acid 1000mg modified release granules | Anti-seizure medications CPRD gold (all) primary care |
| 252205001000027104 (dm+d codes) | Sodium valproate oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 252695001000027103 (dm+d codes) | Sodium valproate with valproic acid 50mg modified release granules | Anti-seizure medications CPRD gold (all) primary care |
| 253111000001106 (dm+d codes) | Carbamazepine 400mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 25442311000001101 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 260011000001109 (dm+d codes) | Epimaz 100mg tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 261545001000027104 (dm+d codes) | Midazolam buccal solution | Anti-seizure medications CPRD gold (all) primary care |
| 261911000001101 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 262575001000027104 (dm+d codes) | Lamotrigine 50mg Suppository | Anti-seizure medications CPRD gold (all) primary care |
| 26811000001102 (dm+d codes) | Diazepam 10mg RecTubes (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 27989111000001104 (dm+d codes) | Levetiracetam 500mg tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 27989511000001108 (dm+d codes) | Levetiracetam 1g tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28036611000001106 (dm+d codes) | Sodium valproate 200mg modified-release tablets (Ennogen Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28037011000001101 (dm+d codes) | Sodium valproate 300mg modified-release tablets (Ennogen Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28050211000001106 (dm+d codes) | Sodium valproate 500mg modified-release tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 28267611000001105 (dm+d codes) | Sodium valproate 300mg modified-release tablets (Colorama Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 283311000001103 (dm+d codes) | Diazepam 2.5mg RecTubes (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28694511000001103 (dm+d codes) | Gabapentin 100mg capsules (Rivopharm (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28696911000001102 (dm+d codes) | Levetiracetam 1g tablets (Rivopharm (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28736211000001106 (dm+d codes) | Rewisca 100mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28736711000001104 (dm+d codes) | Rewisca 25mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28737611000001105 (dm+d codes) | Rewisca 50mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28738211000001107 (dm+d codes) | Rewisca 75mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28738711000001100 (dm+d codes) | Rewisca 150mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28739111000001108 (dm+d codes) | Rewisca 200mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28740211000001105 (dm+d codes) | Rewisca 225mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28742111000001100 (dm+d codes) | Rewisca 300mg capsules (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28909711000001107 (dm+d codes) | Lecaent 25mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28910011000001104 (dm+d codes) | Lecaent 50mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28910211000001109 (dm+d codes) | Lecaent 75mg capsules (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28910411000001108 (dm+d codes) | Lecaent 100mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28910611000001106 (dm+d codes) | Lecaent 150mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28910811000001105 (dm+d codes) | Lecaent 200mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28911211000001103 (dm+d codes) | Lecaent 300mg capsules (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28947311000001109 (dm+d codes) | Levetiracetam 500mg/5ml solution for infusion ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 28964511000001102 (dm+d codes) | Pregabalin 50mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28964811000001104 (dm+d codes) | Pregabalin 75mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28965011000001109 (dm+d codes) | Pregabalin 100mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28965811000001103 (dm+d codes) | Pregabalin 300mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28995001000027109 (dm+d codes) | Phenobarbital 30mg Tablet (C P Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28996411000001106 (dm+d codes) | Alzain 25mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28996611000001109 (dm+d codes) | Alzain 50mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28996911000001103 (dm+d codes) | Alzain 75mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28997111000001103 (dm+d codes) | Alzain 100mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28997311000001101 (dm+d codes) | Alzain 150mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28997511000001107 (dm+d codes) | Alzain 200mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28997711000001102 (dm+d codes) | Alzain 225mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 28997911000001100 (dm+d codes) | Alzain 300mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 290011000001107 (dm+d codes) | Topamax 25mg tablets (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29065001000027104 (dm+d codes) | Phenytoin 50mg Tablet (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 291011000001103 (dm+d codes) | Rivotril 2mg tablets (Roche Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29105001000027107 (dm+d codes) | Phenytoin 50mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 292411000001102 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 2925811000001101 (dm+d codes) | Lamictal 25mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 2927711000001103 (dm+d codes) | Lamictal 50mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 2928811000001105 (dm+d codes) | Lamictal 100mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 296811000001104 (dm+d codes) | Epimaz 200mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29794011000001101 (dm+d codes) | Perizam 1mg/ml oral suspension (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29794211000001106 (dm+d codes) | Perizam 2mg/ml oral suspension (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29933411000001108 (dm+d codes) | Clobazam 5mg/5ml oral suspension sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29935311000001100 (dm+d codes) | Pregabalin 75mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29936111000001108 (dm+d codes) | Pregabalin 50mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29936811000001101 (dm+d codes) | Pregabalin 150mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29938111000001107 (dm+d codes) | Pregabalin 300mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29938311000001109 (dm+d codes) | Pregabalin 25mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 29984311000001109 (dm+d codes) | Phenobarbital 15mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 29984911000001105 (dm+d codes) | Phenytoin sodium 100mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 30028711000001102 (dm+d codes) | Carbamazepine 200mg modified-release tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30076311000001104 (dm+d codes) | Phenobarbital 15mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30076511000001105 (dm+d codes) | Phenobarbital 30mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30101411000001101 (dm+d codes) | Topiramate 15mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30101611000001103 (dm+d codes) | Topiramate 25mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30102011000001102 (dm+d codes) | Topiramate 50mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30115211000001104 (dm+d codes) | Pregabalin 25mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30115811000001103 (dm+d codes) | Pregabalin 75mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30208011000001102 (dm+d codes) | Epanutin 50mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 30218211000001109 (dm+d codes) | Lamotrigine 25mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30224311000001100 (dm+d codes) | Pregabalin 300mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30224511000001106 (dm+d codes) | Pregabalin 50mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30224911000001104 (dm+d codes) | Pregabalin 75mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30225511000001107 (dm+d codes) | Pregabalin 150mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 302911000001103 (dm+d codes) | Neurontin 400mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 304111000001109 (dm+d codes) | Phenobarbital 60mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 305385001000027103 (dm+d codes) | Tegretol retard 200mg Modified-release tablet (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 305395001000027104 (dm+d codes) | Tegretol retard 400mg Modified-release tablet (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 305485001000027106 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 305505001000027104 (dm+d codes) | Midazolam 10mg/ml buccal solution | Anti-seizure medications CPRD gold (all) primary care |
| 305635001000027100 (dm+d codes) | Midazolam maleate buccal solution | Anti-seizure medications CPRD gold (all) primary care |
| 30764211000001106 (dm+d codes) | Phenytoin sodium 100mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30782211000001104 (dm+d codes) | Pregabalin 200mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30782611000001102 (dm+d codes) | Pregabalin 300mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30782811000001103 (dm+d codes) | Pregabalin 50mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30783011000001100 (dm+d codes) | Pregabalin 75mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30786811000001102 (dm+d codes) | Pregabalin 25mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30787011000001106 (dm+d codes) | Pregabalin 50mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30787311000001109 (dm+d codes) | Pregabalin 75mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30811000001102 (dm+d codes) | Phenobarbital 30mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30845411000001100 (dm+d codes) | Phenytoin sodium 100mg capsules (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 30854111000001109 (dm+d codes) | Primidone 50mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30854311000001106 (dm+d codes) | Primidone 250mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 30951511000001107 (dm+d codes) | Sodium valproate 200mg modified-release tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 3145211000001105 (dm+d codes) | Lamictal 200mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3145811000001106 (dm+d codes) | Lamictal 5mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3146411000001100 (dm+d codes) | Lamictal 25mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3147211000001102 (dm+d codes) | Lamictal 100mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31499611000001107 (dm+d codes) | Briviact 10mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31500511000001109 (dm+d codes) | Briviact 25mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31501311000001108 (dm+d codes) | Briviact 50mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31502211000001107 (dm+d codes) | Briviact 75mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31502611000001109 (dm+d codes) | Briviact 100mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31505811000001101 (dm+d codes) | Briviact 50mg/5ml solution for injection vials (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31507311000001102 (dm+d codes) | Briviact 10mg/ml oral solution (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31533711000001103 (dm+d codes) | Brivaracetam 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 31533811000001106 (dm+d codes) | Brivaracetam 10mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 31534011000001103 (dm+d codes) | Brivaracetam 25mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 31534111000001102 (dm+d codes) | Brivaracetam 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 31534211000001108 (dm+d codes) | Brivaracetam 50mg/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 31534411000001107 (dm+d codes) | Brivaracetam 50mg/5ml solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 31534511000001106 (dm+d codes) | Brivaracetam 75mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 3160011000001104 (dm+d codes) | Tegretol 100mg Chewtabs (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3160911000001100 (dm+d codes) | Tegretol 200mg Chewtabs (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31898611000001108 (dm+d codes) | Pregabalin 25mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31899611000001104 (dm+d codes) | Pregabalin 50mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31901111000001103 (dm+d codes) | Pregabalin 75mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31901711000001102 (dm+d codes) | Pregabalin 100mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31902411000001103 (dm+d codes) | Pregabalin 150mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31902911000001106 (dm+d codes) | Pregabalin 200mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31904411000001105 (dm+d codes) | Pregabalin 300mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 31953611000001101 (dm+d codes) | Clobazam 5mg/5ml oral suspension sugar free (Thame Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 321238008 (dm+d codes) | Diazepam 10mg suppositories | Anti-seizure medications CPRD gold (all) primary care |
| 321272000 (dm+d codes) | Clobazam 10mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 32164811000001109 (dm+d codes) | Pregabalin 50mg capsules (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32167211000001101 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 322863001 (dm+d codes) | Carbamazepine 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322864007 (dm+d codes) | Carbamazepine 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322865008 (dm+d codes) | Carbamazepine 400mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322887004 (dm+d codes) | Carbamazepine 125mg suppositories | Anti-seizure medications CPRD gold (all) primary care |
| 322888009 (dm+d codes) | Carbamazepine 250mg suppositories | Anti-seizure medications CPRD gold (all) primary care |
| 322889001 (dm+d codes) | Carbamazepine 200mg chewable tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 322890005 (dm+d codes) | Carbamazepine 100mg chewable tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 322891009 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 322897008 (dm+d codes) | Clonazepam 500microgram tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322898003 (dm+d codes) | Clonazepam 2mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322906007 (dm+d codes) | Ethosuximide 250mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 322908008 (dm+d codes) | Ethosuximide 250mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 322915000 (dm+d codes) | Phenobarbital 15mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322916004 (dm+d codes) | Phenobarbital 30mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322917008 (dm+d codes) | Phenobarbital 60mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322927002 (dm+d codes) | Phenobarbital 15mg/5ml elixir | Anti-seizure medications CPRD gold (all) primary care |
| 322930009 (dm+d codes) | Phenytoin 50mg chewable tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322931008 (dm+d codes) | Phenytoin 30mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 322933006 (dm+d codes) | Phenytoin sodium 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322934000 (dm+d codes) | Phenytoin sodium 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322942004 (dm+d codes) | Phenytoin sodium 300mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 322943009 (dm+d codes) | Phenytoin sodium 25mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 322944003 (dm+d codes) | Phenytoin sodium 50mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 322948000 (dm+d codes) | Primidone 250mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322956002 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322957006 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322977004 (dm+d codes) | Vigabatrin 500mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322979001 (dm+d codes) | Vigabatrin 500mg oral powder sachets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 322981004 (dm+d codes) | Lamotrigine 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322982006 (dm+d codes) | Lamotrigine 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322985008 (dm+d codes) | Lamotrigine 25mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 322991005 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 322992003 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 322994002 (dm+d codes) | Lamotrigine 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323002000 (dm+d codes) | Piracetam 800mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323003005 (dm+d codes) | Piracetam 1.2g tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323004004 (dm+d codes) | Piracetam 333.3mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 323008001 (dm+d codes) | Valproic acid 150mg gastro-resistant capsules | Anti-seizure medications CPRD gold (all) primary care |
| 323009009 (dm+d codes) | Valproic acid 300mg gastro-resistant capsules | Anti-seizure medications CPRD gold (all) primary care |
| 323010004 (dm+d codes) | Valproic acid 500mg gastro-resistant capsules | Anti-seizure medications CPRD gold (all) primary care |
| 323013002 (dm+d codes) | Gabapentin 100mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 323014008 (dm+d codes) | Gabapentin 300mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 323015009 (dm+d codes) | Gabapentin 400mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 323021008 (dm+d codes) | Gabapentin 600mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323022001 (dm+d codes) | Gabapentin 800mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323023006 (dm+d codes) | Topiramate 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323024000 (dm+d codes) | Topiramate 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323025004 (dm+d codes) | Topiramate 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323029005 (dm+d codes) | Topiramate 25mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323046008 (dm+d codes) | Oxcarbazepine 150mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323047004 (dm+d codes) | Oxcarbazepine 300mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323048009 (dm+d codes) | Oxcarbazepine 600mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323053004 (dm+d codes) | Levetiracetam 1g tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323054005 (dm+d codes) | Levetiracetam 500mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323055006 (dm+d codes) | Levetiracetam 250mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 323069006 (dm+d codes) | Diazepam 2.5mg/1.25ml rectal solution tube | Anti-seizure medications CPRD gold (all) primary care |
| 323074003 (dm+d codes) | Diazepam 10mg/2.5ml rectal solution tube | Anti-seizure medications CPRD gold (all) primary care |
| 32398011000001100 (dm+d codes) | Clonazepam 500microgram tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32490011000001109 (dm+d codes) | Gabapentin 300mg capsules (Brown &amp; Burk UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32498111000001107 (dm+d codes) | Phenobarbital 15mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32518811000001108 (dm+d codes) | Buccolam 10mg/2ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32519111000001108 (dm+d codes) | Buccolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32519411000001103 (dm+d codes) | Buccolam 5mg/1ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32519711000001109 (dm+d codes) | Buccolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32636411000001107 (dm+d codes) | Rivotril 1mg/1ml concentrate for solution for injection ampoules and diluent (Imported (France)) | Anti-seizure medications CPRD gold (all) primary care |
| 32655111000001107 (dm+d codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 32655211000001101 (dm+d codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 32655311000001109 (dm+d codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 32655411000001102 (dm+d codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 32711911000001108 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 32879411000001109 (dm+d codes) | Pregabalin 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 32880411000001109 (dm+d codes) | Topiramate 25mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 33038311000001102 (dm+d codes) | Sultiame 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 330601002 (dm+d codes) | Acetazolamide 250mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 33185001000027108 (dm+d codes) | Valium 5mg/ml Injection (Roche Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 332111000001105 (dm+d codes) | Carbamazepine 100mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33355001000027106 (dm+d codes) | Valium 5mg Suppository (Roche Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33365001000027102 (dm+d codes) | Valium 10mg Suppository (Roche Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33382211000001102 (dm+d codes) | Acetazolamide 250mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 333834003 (dm+d codes) | Thiopental 500mg powder for solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 33493711000001109 (dm+d codes) | Ethosuximide 250mg/5ml syrup (Essential Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33607411000001109 (dm+d codes) | Pregabalin 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33608411000001108 (dm+d codes) | Pregabalin 75mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33608611000001106 (dm+d codes) | Pregabalin 50mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33608811000001105 (dm+d codes) | Pregabalin 25mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33709111000001104 (dm+d codes) | Axalid 25mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33709711000001103 (dm+d codes) | Axalid 50mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33710311000001109 (dm+d codes) | Axalid 75mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33710511000001103 (dm+d codes) | Axalid 100mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33712111000001106 (dm+d codes) | Axalid 150mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33712511000001102 (dm+d codes) | Axalid 200mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33715511000001108 (dm+d codes) | Axalid 225mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 33715911000001101 (dm+d codes) | Axalid 300mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34165411000001101 (dm+d codes) | Votubia 5mg dispersible tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34195511000001104 (dm+d codes) | Ethosuximide 250mg/5ml syrup (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34211000001106 (dm+d codes) | Carbamazepine 200mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34246711000001109 (dm+d codes) | Zacco 5mg/5ml oral suspension (Thame Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34327611000001105 (dm+d codes) | Ethosuximide 250mg/5ml syrup (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34378611000001108 (dm+d codes) | Perampanel 4mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 34466511000001108 (dm+d codes) | Epistatus 10mg/1ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34466711000001103 (dm+d codes) | Midazolam 10mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 34581711000001102 (dm+d codes) | Zebinix 200mg tablets (BIAL Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34606611000001108 (dm+d codes) | Eslicarbazepine 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 34683911000001107 (dm+d codes) | Pregabalin 300mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 34754411000001104 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Bowmed Ibisqus Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 34933411000001108 (dm+d codes) | Gabapentin 300mg capsules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35163411000001107 (dm+d codes) | Lamotrigine 25mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35163611000001105 (dm+d codes) | Lamotrigine 50mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35164011000001101 (dm+d codes) | Lamotrigine 200mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35164211000001106 (dm+d codes) | Levetiracetam 250mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35176711000001102 (dm+d codes) | Pregabalin 50mg capsules (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35178511000001108 (dm+d codes) | Pregabalin 300mg capsules (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35186611000001101 (dm+d codes) | Topiramate 25mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35187011000001106 (dm+d codes) | Topiramate 100mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35187211000001101 (dm+d codes) | Topiramate 200mg tablets (Milpharm Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 352911000001109 (dm+d codes) | Epimaz Retard 200mg tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35721611000001105 (dm+d codes) | Gabapentin 300mg capsules (Tillomed Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35832511000001104 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 35919911000001103 (dm+d codes) | Topiramate 15mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 35920011000001101 (dm+d codes) | Topiramate 25mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 35920111000001100 (dm+d codes) | Topiramate 50mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 35928211000001109 (dm+d codes) | Sodium valproate 200mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 35928311000001101 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 35928511000001107 (dm+d codes) | Sodium valproate 400mg powder and solvent for solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 36015611000001102 (dm+d codes) | Phenytoin sodium 250mg/5ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 36037711000001108 (dm+d codes) | Lamotrigine 2mg dispersible tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 36038411000001103 (dm+d codes) | Levetiracetam 500mg/5ml solution for infusion vials | Anti-seizure medications CPRD gold (all) primary care |
| 36040511000001101 (dm+d codes) | Lorazepam 4mg/1ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 36061111000001107 (dm+d codes) | Fosphenytoin 750mg/10ml solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 36097511000001106 (dm+d codes) | Diazepam 10mg/2ml emulsion for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 36097611000001105 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules | Anti-seizure medications CPRD gold (all) primary care |
| 36107311000001106 (dm+d codes) | Ethosuximide 250mg/5ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 3637411000001100 (dm+d codes) | Keppra 1g tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 364611000001102 (dm+d codes) | Emeside 250mg/5ml syrup (Fontus Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36508311000001103 (dm+d codes) | Cannabidiol 100mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 36510411000001109 (dm+d codes) | Zebinix 50mg/1ml oral suspension (BIAL Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36511211000001104 (dm+d codes) | Eslicarbazepine 50mg/1ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 36561911000001107 (dm+d codes) | Levetiracetam 500mg/100ml infusion bags | Anti-seizure medications CPRD gold (all) primary care |
| 36566611000001108 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 36567811000001109 (dm+d codes) | Topiramate 100mg/5ml oral suspension sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3672511000001102 (dm+d codes) | Trileptal 300mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36753111000001103 (dm+d codes) | Topiramate 100mg/5ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 36753211000001109 (dm+d codes) | Topiramate 50mg/5ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 36776811000001103 (dm+d codes) | Fycompa 0.5mg/ml oral suspension (Eisai Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36784011000001105 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Esteve Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36813311000001107 (dm+d codes) | Lamotrigine 50mg tablets (Torrent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36830311000001109 (dm+d codes) | Levetiracetam 250mg tablets (Torrent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 36915111000001101 (dm+d codes) | Perampanel 500micrograms/ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 369911000001109 (dm+d codes) | Carbagen SR 200mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37082411000001106 (dm+d codes) | Carbamazepine 200mg modified-release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 37082511000001105 (dm+d codes) | Carbamazepine 400mg modified-release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 37093211000001100 (dm+d codes) | Levetiracetam 250mg tablets (Relonchem Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3711611000001107 (dm+d codes) | Sabril 500mg oral powder sachets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 371194003 (dm+d codes) | Primidone 250mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 37293211000001107 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Sciecure Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37322611000001104 (dm+d codes) | Dilantin Infatabs 50mg chewable tablets (Imported (Canada)) | Anti-seizure medications CPRD gold (all) primary care |
| 37327811000001102 (dm+d codes) | Pregabalin 25mg capsules (Creo Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37329411000001108 (dm+d codes) | Pregabalin 75mg capsules (Creo Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 374700006 (dm+d codes) | Felbamate 600mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 37480211000001100 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (Crescent Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 375136008 (dm+d codes) | Primidone 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 37515211000001102 (dm+d codes) | Keppra 250mg tablets (CST Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 375396003 (dm+d codes) | Levetiracetam 750mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 375522007 (dm+d codes) | Clonazepam 1mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 37573711000001104 (dm+d codes) | Belvo 250mg gastro-resistant tablets (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37574111000001103 (dm+d codes) | Belvo 500mg gastro-resistant tablets (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37613111000001104 (dm+d codes) | Levetiracetam 250mg tablets (Crescent Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37669211000001108 (dm+d codes) | Keppra 100mg/ml oral solution (Ethigen Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3784111000001104 (dm+d codes) | Trileptal 600mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37982211000001101 (dm+d codes) | Syonell 500mg gastro-resistant tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 37982411000001102 (dm+d codes) | Syonell 250mg gastro-resistant tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 38019511000001108 (dm+d codes) | Pregabalin 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38019611000001107 (dm+d codes) | Pregabalin 150mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38019711000001103 (dm+d codes) | Pregabalin 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38019811000001106 (dm+d codes) | Pregabalin 225mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38019911000001101 (dm+d codes) | Pregabalin 25mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38020011000001104 (dm+d codes) | Pregabalin 300mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38020111000001103 (dm+d codes) | Pregabalin 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38020211000001109 (dm+d codes) | Pregabalin 75mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 38029811000001101 (dm+d codes) | Epidyolex 100mg/ml oral solution (GW Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 380311000001102 (dm+d codes) | Carbamazepine 200mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 38109311000001105 (dm+d codes) | Kigabeq 100mg soluble tablets (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 38161111000001105 (dm+d codes) | Carbamazepine 100mg tablets (Medreich Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 3824311000001107 (dm+d codes) | Valclair 10mg suppositories (Durbin Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 38286011000001103 (dm+d codes) | Vigabatrin 100mg soluble tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 38286111000001102 (dm+d codes) | Vigabatrin 500mg soluble tablets sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 3839911000001106 (dm+d codes) | Trileptal 150mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3846411000001106 (dm+d codes) | Depakote 250mg gastro-resistant tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 3847111000001103 (dm+d codes) | Depakote 500mg gastro-resistant tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 38752611000001105 (dm+d codes) | Oxcarbazepine 60mg/ml oral suspension sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 38819911000001100 (dm+d codes) | Carbamazepine 200mg tablets (Medihealth (Northern) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3893111000001104 (dm+d codes) | Nootropil 800mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3894111000001102 (dm+d codes) | Nootropil 1200mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 38998111000001101 (dm+d codes) | Dyzantil 200mg modified-release tablets (Aspire Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 38999111000001108 (dm+d codes) | Dyzantil 500mg modified-release tablets (Aspire Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3901811000001103 (dm+d codes) | Gabitril 5mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3902111000001100 (dm+d codes) | Gabitril 10mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 39025611000001101 (dm+d codes) | Phenytoin sodium 100mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 39107811000001107 (dm+d codes) | Sodium valproate 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39108211000001105 (dm+d codes) | Sodium valproate 200mg modified-release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39108311000001102 (dm+d codes) | Sodium valproate 300mg modified-release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39108411000001109 (dm+d codes) | Sodium valproate 500mg modified-release tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39205511000001103 (dm+d codes) | Desizon 20mg/ml oral suspension (Desitin Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3920911000001105 (dm+d codes) | Convulex 150mg gastro-resistant capsules (Gerot Lannach UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3921311000001104 (dm+d codes) | Convulex 300mg gastro-resistant capsules (Gerot Lannach UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3921711000001100 (dm+d codes) | Convulex 500mg gastro-resistant capsules (Gerot Lannach UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3923811000001107 (dm+d codes) | Tegretol 125mg suppositories (Essential Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3924111000001103 (dm+d codes) | Tegretol 250mg suppositories (Essential Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 3925811000001106 (dm+d codes) | Ativan 4mg/1ml solution for injection ampoules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 39334711000001109 (dm+d codes) | Ethosuximide 250mg/5ml syrup (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 39704911000001104 (dm+d codes) | Tiagabine 10mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39705011000001104 (dm+d codes) | Tiagabine 15mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39705111000001103 (dm+d codes) | Tiagabine 5mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 39709411000001106 (dm+d codes) | Diazepam 5mg/2.5ml rectal solution tube | Anti-seizure medications CPRD gold (all) primary care |
| 3971111000001102 (dm+d codes) | Diazemuls 10mg/2ml emulsion for injection ampoules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 39803911000001103 (dm+d codes) | Fenfluramine 2.2mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 39845311000001108 (dm+d codes) | Carbamazepine 100mg tablets (Medihealth (Northern) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 39878911000001104 (dm+d codes) | Midazolam 5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 39879011000001108 (dm+d codes) | Midazolam 7.5mg/0.75ml oromucosal solution pre-filled oral syringes | Anti-seizure medications CPRD gold (all) primary care |
| 399711000001109 (dm+d codes) | Phenytoin sodium 100mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 40020211000001105 (dm+d codes) | Epesri 250mg capsules (Strides Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 401511000001108 (dm+d codes) | Neurontin 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 40199011000001106 (dm+d codes) | Ontozry 50mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medications CPRD gold (all) primary care |
| 40202111000001103 (dm+d codes) | Ontozry 100mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medications CPRD gold (all) primary care |
| 40202911000001100 (dm+d codes) | Ontozry 150mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medications CPRD gold (all) primary care |
| 40203711000001105 (dm+d codes) | Ontozry 200mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medications CPRD gold (all) primary care |
| 40206011000001100 (dm+d codes) | Ontozry 12.5mg/25mg tablets treatment initiation pack (Angelini Pharma UK-I Limited) | Anti-seizure medications CPRD gold (all) primary care |
| 40206211000001105 (dm+d codes) | Cenobamate 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 40206411000001109 (dm+d codes) | Cenobamate 12.5mg tablets and Cenobamate 25mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 40206511000001108 (dm+d codes) | Cenobamate 150mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 40206611000001107 (dm+d codes) | Cenobamate 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 40207211000001107 (dm+d codes) | Cenobamate 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 4021611000001103 (dm+d codes) | Lamictal 2mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 40217911000001100 (dm+d codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes sugar free (Xiromed) | Anti-seizure medications CPRD gold (all) primary care |
| 40218211000001108 (dm+d codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes sugar free (Xiromed) | Anti-seizure medications CPRD gold (all) primary care |
| 405811000001109 (dm+d codes) | Carbamazepine 400mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 40829211000001102 (dm+d codes) | Sodium valproate 300mg/3ml solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 40922211000001102 (dm+d codes) | Curatil Prolonged Release 200mg tablets (Tillomed Laboratories Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4092411000001104 (dm+d codes) | Nootropil 33% oral solution (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 409467001 (dm+d codes) | Gabapentin 250mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 410930002 (dm+d codes) | Zonisamide 100mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 4130011000001105 (dm+d codes) | Gabitril 15mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 41305001000027106 (dm+d codes) | Clomethiazole 8mg/ml IV infusion | Anti-seizure medications CPRD gold (all) primary care |
| 415161007 (dm+d codes) | Pregabalin 100mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 415162000 (dm+d codes) | Pregabalin 150mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 415163005 (dm+d codes) | Pregabalin 200mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 415164004 (dm+d codes) | Pregabalin 25mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 415165003 (dm+d codes) | Pregabalin 300mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 415166002 (dm+d codes) | Pregabalin 50mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 415167006 (dm+d codes) | Pregabalin 75mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 417050003 (dm+d codes) | Zonisamide 25mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 417678003 (dm+d codes) | Zonisamide 50mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 4196611000001108 (dm+d codes) | Phenobarbital 15mg/5ml elixir (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4196911000001102 (dm+d codes) | Phenobarbital 15mg/5ml elixir (Thornton &amp; Ross Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4197311000001100 (dm+d codes) | Phenobarbital 15mg/5ml elixir (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4205011000001105 (dm+d codes) | Topamax 15mg sprinkle capsules (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4206011000001101 (dm+d codes) | Topamax 25mg sprinkle capsules (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4206411000001105 (dm+d codes) | Topamax 50mg sprinkle capsules (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 421070002 (dm+d codes) | Pregabalin 225mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 4215911000001106 (dm+d codes) | Rivotril 1mg/1ml concentrate for solution for injection ampoules (Roche Products Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4217711000001103 (dm+d codes) | Clonazepam 1mg/1ml solution for injection ampoules and diluent | Anti-seizure medications CPRD gold (all) primary care |
| 4249911000001100 (dm+d codes) | Sodium valproate 500mg modified-release tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 425011000001109 (dm+d codes) | Carbamazepine 400mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 434211000001102 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 43505001000027104 (dm+d codes) | Diazepam 10mg Suppository (Sinclair IS Pharma Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 4351111000001108 (dm+d codes) | Epilim Intravenous 400mg powder and solvent for solution for injection vials (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 4358911000001102 (dm+d codes) | Epanutin Ready-Mixed Parenteral 250mg/5ml solution for injection ampoules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4370711000001104 (dm+d codes) | Diamox Sodium Parenteral 500mg powder for solution for injection vials (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 4377611000001107 (dm+d codes) | Acetazolamide 500mg powder for solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 4390811000001104 (dm+d codes) | Pro-Epanutin 750mg/10ml concentrate for solution for injection vials (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 441464008 (dm+d codes) | Lacosamide 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 441572007 (dm+d codes) | Rufinamide 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 441726005 (dm+d codes) | Everolimus 5mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 441822003 (dm+d codes) | Rufinamide 400mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 441836008 (dm+d codes) | Lacosamide 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 441947000 (dm+d codes) | Lacosamide 150mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 441953000 (dm+d codes) | Everolimus 10mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 442041004 (dm+d codes) | Lacosamide 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 443711000001108 (dm+d codes) | Tegretol 200mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 446482007 (dm+d codes) | Everolimus 500microgram tablets | Anti-seizure medications CPRD gold (all) primary care |
| 447132004 (dm+d codes) | Everolimus 250microgram tablets | Anti-seizure medications CPRD gold (all) primary care |
| 448711000001102 (dm+d codes) | Epilim 500 gastro-resistant tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 451611000001101 (dm+d codes) | Phenobarbital 15mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4571411000001103 (dm+d codes) | Carbamazepine 200mg modified-release tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4571611000001100 (dm+d codes) | Carbamazepine 400mg modified-release tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 459211000001102 (dm+d codes) | Neurontin 100mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 462911000001106 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4765911000001103 (dm+d codes) | Epival CR 300mg tablets (Gerot Lannach UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 4766111000001107 (dm+d codes) | Epival CR 500mg tablets (Gerot Lannach UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 48865001000027103 (dm+d codes) | Luminal 30mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 48875001000027105 (dm+d codes) | Luminal 60mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 48885001000027100 (dm+d codes) | Luminal 15mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 489711000001100 (dm+d codes) | Epilim Chrono 200 tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 49325001000027106 (dm+d codes) | Prominal 30mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 49335001000027108 (dm+d codes) | Prominal 60mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 49345001000027109 (dm+d codes) | Prominal 200mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 502645001000027104 (dm+d codes) | Epistatus 10mg/1ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 502685001000027108 (dm+d codes) | Epistatus 2.5mg/0.25ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 502705001000027103 (dm+d codes) | Midazolam 5mg/0.5ml oromucosal solution pre-filled syringes | Anti-seizure medications CPRD gold (all) primary care |
| 502725001000027105 (dm+d codes) | Epistatus 5mg/0.5ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 502765001000027102 (dm+d codes) | Epistatus 7.5mg/0.75ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 502795001000027100 (dm+d codes) | Epistatus 50mg/5ml oromucosal solution bottle (Veriton Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 504111000001107 (dm+d codes) | Carbamazepine 100mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 504711000001108 (dm+d codes) | Orlept 200mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 506411000001105 (dm+d codes) | Carbamazepine 100mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5083111000001106 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules (hameln pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 511611000001103 (dm+d codes) | Neurontin 600mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 514411000001104 (dm+d codes) | Carbamazepine 100mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 51755001000027109 (dm+d codes) | Valproate sodium 200mg Gastro-resistant tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 51765001000027100 (dm+d codes) | Valproate sodium 500mg Gastro-resistant tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 520611000001103 (dm+d codes) | Carbamazepine 200mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5240511000001109 (dm+d codes) | Potassium bromide mixture | Anti-seizure medications CPRD gold (all) primary care |
| 53485001000027100 (dm+d codes) | Diamox 250mg Tablet (Wyeth Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 53495001000027101 (dm+d codes) | Diamox 500mg/vial Sodium injection (Wyeth Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 5367711000001103 (dm+d codes) | Frisium 10mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 5379611000001106 (dm+d codes) | Lamictal 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 5381611000001101 (dm+d codes) | Lamictal 25mg dispersible tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 5398011000001101 (dm+d codes) | Neurontin 100mg capsules (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 5418811000001102 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Waymade Healthcare Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 5471411000001101 (dm+d codes) | Gabapentin 100mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5472411000001106 (dm+d codes) | Gabapentin 300mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5473811000001100 (dm+d codes) | Gabapentin 400mg capsules (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5474211000001103 (dm+d codes) | Gabapentin 600mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5475211000001102 (dm+d codes) | Gabapentin 800mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 548211000001104 (dm+d codes) | Phenobarbital 15mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 552511000001100 (dm+d codes) | Epilim 100mg crushable tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 5547911000001106 (dm+d codes) | Neurontin 300mg capsules (Dowelhurst Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 55611000001105 (dm+d codes) | Phenytoin sodium 100mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5568111000001101 (dm+d codes) | Gabapentin 100mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5569411000001103 (dm+d codes) | Gabapentin 300mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5569611000001100 (dm+d codes) | Gabapentin 400mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5570311000001108 (dm+d codes) | Gabapentin 600mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5586611000001106 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Dowelhurst Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 5629911000001107 (dm+d codes) | Gabapentin 600mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 563311000001108 (dm+d codes) | Phenobarbital 60mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 566911000001103 (dm+d codes) | Phenobarbital 60mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 56811000001101 (dm+d codes) | Phenobarbital 15mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 569811000001102 (dm+d codes) | Phenobarbital 15mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 591311000001109 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 603811000001108 (dm+d codes) | Diazepam 5mg RecTubes (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 60435001000027108 (dm+d codes) | Paraldehyde intravenous injection | Anti-seizure medications CPRD gold (all) primary care |
| 60445001000027109 (dm+d codes) | Paraldehyde rectal solution | Anti-seizure medications CPRD gold (all) primary care |
| 60595001000027105 (dm+d codes) | Phenobarbital 50mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 60705001000027108 (dm+d codes) | Sodium valproate 500mg Gastro-resistant tablet (C P Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 61035001000027109 (dm+d codes) | Phenytoin 90mg/5ml Oral suspension sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 612111000001105 (dm+d codes) | Carbamazepine 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 624411000001104 (dm+d codes) | Phenytoin sodium 100mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 636111000001104 (dm+d codes) | Diazepam 5mg/2.5ml rectal solution tube (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 640811000001105 (dm+d codes) | Carbagen SR 400mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 658111000001104 (dm+d codes) | Teril Retard 400mg tablets (Taro Pharmaceuticals (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 66045001000027108 (dm+d codes) | Sodium valproate 200mg/5ml Oral solution (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 662611000001103 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 680511000001100 (dm+d codes) | Tegretol 100mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 687511000001101 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 702711000001104 (dm+d codes) | Tegretol 400mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 703729002 (dm+d codes) | Perampanel 2mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 703730007 (dm+d codes) | Perampanel 4mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 703732004 (dm+d codes) | Perampanel 6mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 703733009 (dm+d codes) | Perampanel 8mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 703734003 (dm+d codes) | Perampanel 10mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 703735002 (dm+d codes) | Perampanel 12mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 704477007 (dm+d codes) | Retigabine 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 704478002 (dm+d codes) | Retigabine 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 704479005 (dm+d codes) | Retigabine 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 704480008 (dm+d codes) | Retigabine 300mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 704481007 (dm+d codes) | Retigabine 400mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 707111000001103 (dm+d codes) | Diazepam 5mg/2.5ml rectal solution tube (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 71005001000027101 (dm+d codes) | Pentran 50mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 71015001000027104 (dm+d codes) | Pentran 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 725911000001101 (dm+d codes) | Epanutin 100mg capsules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 731411000001109 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7315411000001103 (dm+d codes) | Trileptal 60mg/ml oral suspension (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 739111000001100 (dm+d codes) | Epilim Chrono 500 tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 755011000001104 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 75811000001106 (dm+d codes) | Diazepam 10mg/2.5ml rectal solution tube (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7585001000027105 (dm+d codes) | Diamox sustets 500 500mg Sustets (Wyeth Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 760111000001100 (dm+d codes) | Tegretol 100mg/5ml liquid (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 760511000001109 (dm+d codes) | Epimaz 400mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7655011000001106 (dm+d codes) | Rivotril 2.5mg/1ml drops (Imported (Switzerland)) | Anti-seizure medications CPRD gold (all) primary care |
| 7662511000001100 (dm+d codes) | Clonazepam 2.5mg/ml drops sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 767111000001104 (dm+d codes) | Zarontin 250mg capsules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 77085001000027104 (dm+d codes) | Stesolid 5mg/ml Injection (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7716411000001106 (dm+d codes) | Ospolot 50mg tablets (Imported (Germany)) | Anti-seizure medications CPRD gold (all) primary care |
| 7721511000001108 (dm+d codes) | Sultiame 200mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 7721611000001107 (dm+d codes) | Sultiame 50mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 781611000001101 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 782711000001103 (dm+d codes) | Zarontin 250mg/5ml syrup (Essential Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7843411000001108 (dm+d codes) | Acetazolamide 250mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7847211000001100 (dm+d codes) | Gabapentin 100mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7847411000001101 (dm+d codes) | Gabapentin 300mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7847611000001103 (dm+d codes) | Gabapentin 400mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7865001000027106 (dm+d codes) | Carbamazepine 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7875001000027104 (dm+d codes) | Carbamazepine 200mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7889411000001104 (dm+d codes) | Lyrica 25mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7890211000001109 (dm+d codes) | Lyrica 50mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7890511000001107 (dm+d codes) | Lyrica 75mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7890811000001105 (dm+d codes) | Lyrica 100mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7891211000001103 (dm+d codes) | Lyrica 150mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7891611000001101 (dm+d codes) | Lyrica 200mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 7892111000001104 (dm+d codes) | Lyrica 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 789911000001106 (dm+d codes) | Epilim Chrono 300 tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 801011000001107 (dm+d codes) | Diamox 250mg tablets (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 8171111000001104 (dm+d codes) | Keppra 750mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8176611000001100 (dm+d codes) | Keppra 100mg/ml oral solution (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 82011000001104 (dm+d codes) | Stesolid 5mg rectal tube (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 823811000001105 (dm+d codes) | Topamax 100mg tablets (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8269211000001104 (dm+d codes) | Acetazolamide 100mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8269311000001107 (dm+d codes) | Acetazolamide 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8269411000001100 (dm+d codes) | Acetazolamide 125mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8269511000001101 (dm+d codes) | Acetazolamide 125mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8270711000001109 (dm+d codes) | Acetazolamide 250mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8270911000001106 (dm+d codes) | Acetazolamide 250mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8271511000001106 (dm+d codes) | Acetazolamide 500mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8271611000001105 (dm+d codes) | Acetazolamide 62.5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8285511000001102 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free | Anti-seizure medications CPRD gold (all) primary care |
| 8354711000001108 (dm+d codes) | Carbamazepine 40mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8354911000001105 (dm+d codes) | Carbamazepine 500mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8360711000001105 (dm+d codes) | Clobazam 10mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8360811000001102 (dm+d codes) | Clobazam 10mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8361111000001103 (dm+d codes) | Clobazam 1mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8361211000001109 (dm+d codes) | Clobazam 2.5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8361311000001101 (dm+d codes) | Clobazam 2.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8366311000001109 (dm+d codes) | Clobazam 20mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8366411000001102 (dm+d codes) | Clobazam 25mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8366611000001104 (dm+d codes) | Clobazam 25mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8366811000001100 (dm+d codes) | Clobazam 2mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8367111000001105 (dm+d codes) | Clobazam 3.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8367211000001104 (dm+d codes) | Clobazam 4mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8367411000001100 (dm+d codes) | Clobazam 4mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8368611000001103 (dm+d codes) | Clobazam 5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8368711000001107 (dm+d codes) | Clobazam 5mg/5ml oral suspension (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8368811000001104 (dm+d codes) | Clobazam 5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8382911000001108 (dm+d codes) | Clonazepam 10mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 839211000001109 (dm+d codes) | Keppra 500mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8395211000001105 (dm+d codes) | Clonazepam 1mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8395311000001102 (dm+d codes) | Clonazepam 2.5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8395711000001103 (dm+d codes) | Clonazepam 250micrograms/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8395811000001106 (dm+d codes) | Clonazepam 250micrograms/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8395911000001101 (dm+d codes) | Clonazepam 2mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8396011000001109 (dm+d codes) | Clonazepam 2mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8397111000001108 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8397211000001102 (dm+d codes) | Clonazepam 500micrograms/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8397311000001105 (dm+d codes) | Clonazepam 5mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8397411000001103 (dm+d codes) | Clonazepam 5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 84011000001105 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8520111000001104 (dm+d codes) | Gabapentin 100mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8520211000001105 (dm+d codes) | Gabapentin 100mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8520411000001109 (dm+d codes) | Gabapentin 250mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8520511000001108 (dm+d codes) | Gabapentin 300mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8523111000001106 (dm+d codes) | Gabapentin 300mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8523211000001100 (dm+d codes) | Gabapentin 450mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8523311000001108 (dm+d codes) | Gabapentin 450mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8523411000001101 (dm+d codes) | Gabapentin 50mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 8523511000001102 (dm+d codes) | Gabapentin 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8582611000001104 (dm+d codes) | Lamotrigine 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8611000001108 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 87155001000027103 (dm+d codes) | Phenobarbital 100mg tablet | Anti-seizure medications CPRD gold (all) primary care |
| 872211000001104 (dm+d codes) | Orlept SF 200mg/5ml liquid (Wockhardt UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8723811000001103 (dm+d codes) | Topiramate 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8723911000001108 (dm+d codes) | Topiramate 25mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8768411000001102 (dm+d codes) | Primidone 50mg capsules (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 87711000001100 (dm+d codes) | Mysoline 250mg tablets (SERB) | Anti-seizure medications CPRD gold (all) primary care |
| 87855001000027106 (dm+d codes) | Acetazolamide 40mg/ml Oral solution (Martindale Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8789511000001106 (dm+d codes) | Phenobarbital 50mg/5ml oral solution (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8790011000001107 (dm+d codes) | Phenobarbital 50mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8792211000001101 (dm+d codes) | Clobazam 2.5mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 8800311000001105 (dm+d codes) | Primidone 50mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 8800811000001101 (dm+d codes) | Phenobarbital 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8800911000001106 (dm+d codes) | Phenobarbital 50mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 880211000001107 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8808311000001107 (dm+d codes) | Primidone 25mg/5ml oral suspension (Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8808911000001108 (dm+d codes) | Primidone 50mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8809511000001107 (dm+d codes) | Primidone 62.5mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8814411000001107 (dm+d codes) | Phenytoin 90mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medications CPRD gold (all) primary care |
| 8817911000001105 (dm+d codes) | Phenytoin 90mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8818111000001108 (dm+d codes) | Primidone 25mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8818211000001102 (dm+d codes) | Primidone 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8818311000001105 (dm+d codes) | Primidone 62.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 8818511000001104 (dm+d codes) | Sodium valproate 300mg suppositories | Anti-seizure medications CPRD gold (all) primary care |
| 889311000001108 (dm+d codes) | Epilim 200 gastro-resistant tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 89011000001106 (dm+d codes) | Carbamazepine 400mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8916811000001109 (dm+d codes) | Gabapentin 100mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 8917211000001105 (dm+d codes) | Gabapentin 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 892411000001106 (dm+d codes) | Epilim 200mg/5ml syrup (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 89505001000027108 (dm+d codes) | Carbamazepine 200mg Modified-release tablet (Lagap) | Anti-seizure medications CPRD gold (all) primary care |
| 89515001000027105 (dm+d codes) | Carbamazepine 400mg Modified-release tablet (Lagap) | Anti-seizure medications CPRD gold (all) primary care |
| 896911000001104 (dm+d codes) | Phenobarbital 30mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 91175001000027104 (dm+d codes) | Paraldehyde intramuscular injection | Anti-seizure medications CPRD gold (all) primary care |
| 91195001000027108 (dm+d codes) | Phenobarbital sodium 30mg tablet | Anti-seizure medications CPRD gold (all) primary care |
| 91205001000027108 (dm+d codes) | Phenobarbital sodium 60mg tablet | Anti-seizure medications CPRD gold (all) primary care |
| 91511000001103 (dm+d codes) | Carbamazepine 200mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 918411000001102 (dm+d codes) | Phenobarbital 30mg tablets (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 926511000001105 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 929411000001104 (dm+d codes) | Keppra 250mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9298111000001103 (dm+d codes) | Gabapentin 100mg capsules (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9298311000001101 (dm+d codes) | Gabapentin 300mg capsules (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 929911000001107 (dm+d codes) | Frisium 10mg tablets (Sanofi) | Anti-seizure medications CPRD gold (all) primary care |
| 9303511000001105 (dm+d codes) | Zonegran 25mg capsules (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 9303911000001103 (dm+d codes) | Zonegran 50mg capsules (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 9304111000001104 (dm+d codes) | Zonegran 100mg capsules (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 9308411000001100 (dm+d codes) | Gabapentin 300mg capsules (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9326611000001105 (dm+d codes) | Lamotrigine 25mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9326811000001109 (dm+d codes) | Lamotrigine 50mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9327011000001100 (dm+d codes) | Lamotrigine 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9327411000001109 (dm+d codes) | Lamotrigine 25mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9327611000001107 (dm+d codes) | Lamotrigine 50mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9327811000001106 (dm+d codes) | Lamotrigine 100mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9328011000001104 (dm+d codes) | Lamotrigine 200mg tablets (Actavis UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9329311000001107 (dm+d codes) | Lamotrigine 25mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9329511000001101 (dm+d codes) | Lamotrigine 50mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9329711000001106 (dm+d codes) | Lamotrigine 100mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9360611000001104 (dm+d codes) | Lamotrigine 50mg tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 93775001000027101 (dm+d codes) | Acetazolamide powder | Anti-seizure medications CPRD gold (all) primary care |
| 9378311000001100 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (PLIVA Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 93785001000027106 (dm+d codes) | Acetazolamide 40mg/ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 9378511000001106 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (PLIVA Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9378711000001101 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (PLIVA Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 93865001000027106 (dm+d codes) | Sodium valproate 200mg Tablet (Sterwin Medicines) | Anti-seizure medications CPRD gold (all) primary care |
| 93875001000027104 (dm+d codes) | Sodium valproate 200mg/5ml Oral solution (Sterwin Medicines) | Anti-seizure medications CPRD gold (all) primary care |
| 93885001000027109 (dm+d codes) | Sodium valproate 500mg Tablet (Sterwin Medicines) | Anti-seizure medications CPRD gold (all) primary care |
| 93895001000027108 (dm+d codes) | Diamox Powder (Wyeth Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 9450711000001106 (dm+d codes) | Lamotrigine 25mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9450911000001108 (dm+d codes) | Lamotrigine 50mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9451211000001105 (dm+d codes) | Lamotrigine 100mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9451411000001109 (dm+d codes) | Lamotrigine 200mg tablets (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9451811000001106 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9452011000001108 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (Teva UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9454111000001101 (dm+d codes) | Lamotrigine 25mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9454511000001105 (dm+d codes) | Lamotrigine 50mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9454711000001100 (dm+d codes) | Lamotrigine 100mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9455711000001101 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9456011000001107 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9458411000001102 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9458611000001104 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9458811000001100 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9459011000001101 (dm+d codes) | Lamotrigine 25mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9459411000001105 (dm+d codes) | Lamotrigine 50mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9460011000001100 (dm+d codes) | Lamotrigine 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9460211000001105 (dm+d codes) | Lamotrigine 200mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 95445001000027100 (dm+d codes) | Beclamide 500mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 9557711000001101 (dm+d codes) | Gabapentin 100mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9557911000001104 (dm+d codes) | Gabapentin 300mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9703811000001109 (dm+d codes) | Acetazolamide 250mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9735001000027108 (dm+d codes) | Emeside 250mg Capsule (Laboratories For Applied Biology Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 9745001000027109 (dm+d codes) | Emeside 250mg/5ml Oral solution (Laboratories For Applied Biology Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 00000000 (BNF codes) | TIAGABINE | Anti-seizure medications CPRD gold (all) primary care |
| 02020700 (BNF codes) | Diamox 250mg tablets (Advanz Pharma) | Anti-seizure medications CPRD gold (all) primary care |
| 02020700/04080101/11065300 (BNF codes) | Acetazolamide 100mg/5ml oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 02020700/11065300 (BNF codes) | Diamox 500mg/vial Sodium injection (Wyeth Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 04010200/04080100 (BNF codes) | Clobazam 10mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 04010200/04080200 (BNF codes) | Diazepam 10mg Rectal tubes (Hillcross Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04010201/04080100 (BNF codes) | Clobazam 1.5mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 04010201/04080200/04080300/10020200/15010401 (BNF codes) | Diazepam 10mg/2ml solution for injection ampoules (A A H Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04010201/04080200/04080300/10020200/15010401/54140000 (BNF codes) | Diazemuls 10mg/2ml emulsion for injection ampoules (Accord Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04010201/04080200/10020200/15010401/54140000 (BNF codes) | Diazepam 10mg/2.5ml rectal solution tube (Sandoz Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04010201/04080200/15010401 (BNF codes) | Ativan 4mg/1ml solution for injection ampoules (Pfizer Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04010300/04080200/15010100 (BNF codes) | Thiopental 500mg powder for solution for injection vials | Anti-seizure medications CPRD gold (all) primary care |
| 04020000/04080100 (BNF codes) | Lamictal 100mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04020300/04070402 (BNF codes) | Belvo 250mg gastro-resistant tablets (Consilient Health Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04020300/04080100 (BNF codes) | Carbamazepine 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04030000/04070300/04080100 (BNF codes) | Alzain 100mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04030000/04070300/04080100/06010500 (BNF codes) | Lyrica 100mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medications CPRD gold (all) primary care |
| 04030000/04080100 (BNF codes) | Pregabalin 150mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04070300/04080100 (BNF codes) | Gabapentin 100mg capsules | Anti-seizure medications CPRD gold (all) primary care |
| 04070402/04080100 (BNF codes) | Topamax 100mg tablets (Janssen-Cilag Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04080100 (BNF codes) | Carbamazepine 100mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 04080100/04080200 (BNF codes) | Epanutin 100mg capsules (Dowelhurst Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04080100/04090300 (BNF codes) | Mysoline 250mg Tablet (AstraZeneca UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04080100/04105000/06010500 (BNF codes) | Carbagen 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 04080101 (BNF codes) | Ospolot 50mg tablets (Imported (Germany)) | Anti-seizure medications CPRD gold (all) primary care |
| 04080102 (BNF codes) | Phenobarbital 50mg/5ml oral suspension | Anti-seizure medications CPRD gold (all) primary care |
| 04080102/04090300 (BNF codes) | Mysoline 250mg tablets (DE Pharmaceuticals) | Anti-seizure medications CPRD gold (all) primary care |
| 04080200 (BNF codes) | Clonazepam 1mg/1ml solution for injection ampoules and diluent | Anti-seizure medications CPRD gold (all) primary care |
| 04080200/04105000 (BNF codes) | Clomethiazole 8mg/ml IV infusion | Anti-seizure medications CPRD gold (all) primary care |
| 04080200/15010401 (BNF codes) | Midazolam Oral solution | Anti-seizure medications CPRD gold (all) primary care |
| 04080400 (BNF codes) | Cenobamate 12.5mg tablets and Cenobamate 25mg tablets | Anti-seizure medications CPRD gold (all) primary care |
| 04090300 (BNF codes) | Nootropil 1200mg tablets (UCB Pharma Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 08010000/08020100 (BNF codes) | Everolimus 250microgram tablets | Anti-seizure medications CPRD gold (all) primary care |
| 08010551 (BNF codes) | Afinitor 10mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medications CPRD gold (all) primary care |
| 50000000 (BNF codes) | Acetazolamide powder | Anti-seizure medications CPRD gold (all) primary care |
| 100011000001108 (dm+d codes) | Epilim 200mg/5ml liquid (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 101045001000027109 (dm+d codes) | Heminevrin 8mg/ml Intravenous infusion (AstraZeneca UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 101295001000027107 (dm+d codes) | Carbamazepine 100mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 101305001000027100 (dm+d codes) | Carbamazepine 200mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10225811000001107 (dm+d codes) | Lamotrigine 50mg dispersible tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 102785001000027101 (dm+d codes) | Clobazam 10mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 10287011000001104 (dm+d codes) | Lamotrigine 25mg tablets (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10287511000001107 (dm+d codes) | Lamotrigine 50mg tablets (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10308711000001109 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10356611000001109 (dm+d codes) | Clobazam 10mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10415611000001103 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Arrow Generics Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10446811000001102 (dm+d codes) | Keppra 500mg/5ml concentrate for solution for infusion vials (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10450811000001101 (dm+d codes) | Lamotrigine 25mg tablets (Arrow Generics Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10451811000001109 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Arrow Generics Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10501411000001107 (dm+d codes) | Keppra 250mg tablets (Dowelhurst Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10503911000001103 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10543411000001100 (dm+d codes) | Lyrica 75mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10547411000001107 (dm+d codes) | Keppra 250mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10548011000001102 (dm+d codes) | Keppra 500mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 107835001000027109 (dm+d codes) | TEGRETOL liq 100 MG/5ML LIQ | Anti-seizure medication CPRD gold (all) primary care |
| 10854011000001105 (dm+d codes) | Epilim Chrono 200 tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10854211000001100 (dm+d codes) | Epilim Chrono 300 tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10854411000001101 (dm+d codes) | Epilim Chrono 500 tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10854611000001103 (dm+d codes) | Epilim 500 gastro-resistant tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 10854811000001104 (dm+d codes) | Epilim 200mg/5ml liquid (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 108855001000027104 (dm+d codes) | Carbamazepine 200mg Modified-release tablet (Generics (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 108865001000027108 (dm+d codes) | Carbamazepine 400mg Modified-release tablet (Generics (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 109855001000027101 (dm+d codes) | Diazepam 5mg suppository | Anti-seizure medication CPRD gold (all) primary care |
| 11089411000001104 (dm+d codes) | Sodium valproate 300mg/3ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 11141611000001101 (dm+d codes) | Depakote 125mg sprinkle gastro-resistant capsules (Imported (United States)) | Anti-seizure medication CPRD gold (all) primary care |
| 11146711000001104 (dm+d codes) | Valproic acid 125mg gastro-resistant capsules | Anti-seizure medication CPRD gold (all) primary care |
| 11383911000001108 (dm+d codes) | Primidone 125mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 11475111000001108 (dm+d codes) | Sodium valproate 150mg modified-release capsules | Anti-seizure medication CPRD gold (all) primary care |
| 11475211000001102 (dm+d codes) | Sodium valproate 300mg modified-release capsules | Anti-seizure medication CPRD gold (all) primary care |
| 11475311000001105 (dm+d codes) | Sodium valproate 500mg modified-release granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 11475411000001103 (dm+d codes) | Sodium valproate 1g modified-release granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 11475611000001100 (dm+d codes) | Episenta 150mg modified-release capsules (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11475911000001106 (dm+d codes) | Episenta 300mg modified-release capsules (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11476211000001108 (dm+d codes) | Episenta 500mg modified-release granules sachets (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11476511000001106 (dm+d codes) | Episenta 1000mg modified-release granules sachets (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 114811000001105 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11485111000001102 (dm+d codes) | Primidone 250mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 11500511000001106 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11500711000001101 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11500911000001104 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11532011000001106 (dm+d codes) | Gabapentin 100mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11652711000001100 (dm+d codes) | Acetazolamide 40mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 11654611000001101 (dm+d codes) | Acetazolamide 50mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 117311000001105 (dm+d codes) | Emeside 250mg capsules (Fontus Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 118005001000027107 (dm+d codes) | Carbamazepine sr 200mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 118025001000027100 (dm+d codes) | Carbamazepine sr 400mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 119011000001103 (dm+d codes) | Sodium valproate 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 11944611000001102 (dm+d codes) | Clonazepam 125micrograms/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 11944711000001106 (dm+d codes) | Clonazepam 125micrograms/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 11955111000001107 (dm+d codes) | Clonazepam 25micrograms/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 11955611000001104 (dm+d codes) | Clonazepam 312.5micrograms/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 11956511000001105 (dm+d codes) | Clonazepam 50micrograms/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12022011000001107 (dm+d codes) | Clobazam 1.5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12022211000001102 (dm+d codes) | Clobazam 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12024011000001101 (dm+d codes) | Clobazam 7.5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12024111000001100 (dm+d codes) | Clobazam 7.5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12089111000001105 (dm+d codes) | Gabapentin 150mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12089311000001107 (dm+d codes) | Gabapentin 200mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12089511000001101 (dm+d codes) | Gabapentin 500mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12095001000027109 (dm+d codes) | Frisium 10mg Capsule (Aventis Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 12152911000001100 (dm+d codes) | Phenobarbital 10mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 12178011000001104 (dm+d codes) | Phenobarbital 45mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 12186711000001109 (dm+d codes) | Phenobarbital 10mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12187211000001100 (dm+d codes) | Phenobarbital 150mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12188111000001107 (dm+d codes) | Phenobarbital 20mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12189011000001101 (dm+d codes) | Phenobarbital 250mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12189511000001109 (dm+d codes) | Phenobarbital 30mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12189811000001107 (dm+d codes) | Phenobarbital 34mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12191711000001104 (dm+d codes) | Phenobarbital 60mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12205211000001109 (dm+d codes) | Phenobarbital 15mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 12212911000001106 (dm+d codes) | Phenobarbital 15mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12213011000001103 (dm+d codes) | Phenobarbital 15mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12213111000001102 (dm+d codes) | Phenobarbital 25mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12213211000001108 (dm+d codes) | Phenobarbital 25mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12213511000001106 (dm+d codes) | Phenobarbital 5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12214011000001101 (dm+d codes) | Phenobarbital 75mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12214111000001100 (dm+d codes) | Phenobarbital 75mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 122211000001108 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 12249711000001107 (dm+d codes) | Phenobarbital 100mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 12299311000001101 (dm+d codes) | Phenobarbital 100mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 12299411000001108 (dm+d codes) | Phenobarbital 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 12299611000001106 (dm+d codes) | Phenobarbital 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12311000001104 (dm+d codes) | Teril Retard 200mg tablets (Taro Pharmaceuticals (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 12323011000001102 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 12326711000001107 (dm+d codes) | Carbamazepine 200mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 12387511000001107 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12387711000001102 (dm+d codes) | Carbamazepine 10mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12425011000001109 (dm+d codes) | Phenobarbital 10mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 12425511000001101 (dm+d codes) | Phenobarbital 60mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 125145001000027104 (dm+d codes) | Methylphenobarbital 30mg Tablet | Anti-seizure medication CPRD gold (all) primary care |
| 125155001000027101 (dm+d codes) | Methylphenobarbital 60mg Tablet | Anti-seizure medication CPRD gold (all) primary care |
| 125165001000027105 (dm+d codes) | Methylphenobarbital 200mg Tablet | Anti-seizure medication CPRD gold (all) primary care |
| 12644511000001103 (dm+d codes) | Lamotrigine 15mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12644711000001108 (dm+d codes) | Lamotrigine 200mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12645211000001100 (dm+d codes) | Lamotrigine 5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12645411000001101 (dm+d codes) | Levetiracetam 250mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 12645511000001102 (dm+d codes) | Levetiracetam 250mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 12645611000001103 (dm+d codes) | Levetiracetam 400mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 126655001000027104 (dm+d codes) | Sodium valproate 200mg/5ml Oral solution (Hillcross Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 12862111000001104 (dm+d codes) | Inovelon 100mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 12865211000001100 (dm+d codes) | Rufinamide 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 12948611000001108 (dm+d codes) | Gabapentin 100mg capsules (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 12949111000001107 (dm+d codes) | Gabapentin 300mg capsules (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13016311000001107 (dm+d codes) | Vigabatrin 350mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13016411000001100 (dm+d codes) | Vigabatrin 500mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13041211000001104 (dm+d codes) | Phenytoin sodium 84mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13076011000001103 (dm+d codes) | Lyrica 225mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13117911000001104 (dm+d codes) | Sodium valproate 1g/10ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 13123911000001104 (dm+d codes) | Inovelon 200mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13124211000001106 (dm+d codes) | Inovelon 400mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13162911000001100 (dm+d codes) | Epanutin 100mg capsules (Dowelhurst Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13301111000001104 (dm+d codes) | Sodium valproate 500mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13301211000001105 (dm+d codes) | Sodium valproate 600mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13301311000001102 (dm+d codes) | Sodium valproate 60mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13324511000001102 (dm+d codes) | Topiramate 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13324711000001107 (dm+d codes) | Topiramate 12.5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13324811000001104 (dm+d codes) | Topiramate 125mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13355211000001100 (dm+d codes) | Topiramate 100mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13355411000001101 (dm+d codes) | Topiramate 10mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13355511000001102 (dm+d codes) | Topiramate 12.5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13355711000001107 (dm+d codes) | Topiramate 12mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13355911000001109 (dm+d codes) | Topiramate 12mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13356411000001105 (dm+d codes) | Topiramate 20mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13356611000001108 (dm+d codes) | Topiramate 20mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13356711000001104 (dm+d codes) | Topiramate 30mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13356811000001107 (dm+d codes) | Topiramate 30mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13356911000001102 (dm+d codes) | Topiramate 5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13387511000001103 (dm+d codes) | Gabapentin 300mg capsules (Arrow Generics Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13403211000001101 (dm+d codes) | Diacomit 250mg oral powder sachets (Alan Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13411111000001108 (dm+d codes) | Stiripentol 250mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 13411211000001102 (dm+d codes) | Stiripentol 250mg oral powder sachets | Anti-seizure medication CPRD gold (all) primary care |
| 13411311000001105 (dm+d codes) | Stiripentol 500mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 13411411000001103 (dm+d codes) | Stiripentol 500mg oral powder sachets | Anti-seizure medication CPRD gold (all) primary care |
| 13436711000001105 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13436911000001107 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 134565001000027108 (dm+d codes) | Phenytoin 25mg capsule | Anti-seizure medication CPRD gold (all) primary care |
| 134575001000027101 (dm+d codes) | Phenytoin 50mg capsule | Anti-seizure medication CPRD gold (all) primary care |
| 134595001000027105 (dm+d codes) | Phenytoin 100mg capsule | Anti-seizure medication CPRD gold (all) primary care |
| 134605001000027102 (dm+d codes) | Phenytoin 300mg capsule | Anti-seizure medication CPRD gold (all) primary care |
| 13565811000001105 (dm+d codes) | Gabapentin 600mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13566011000001108 (dm+d codes) | Gabapentin 600mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 13567111000001107 (dm+d codes) | Lyrica 50mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 13649111000001102 (dm+d codes) | Phenytoin sodium 250mg/5ml solution for injection ampoules (Alliance Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13653211000001108 (dm+d codes) | Clonazepam 500microgram tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13665411000001101 (dm+d codes) | Epilim Chronosphere MR 100mg granules sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 13665711000001107 (dm+d codes) | Epilim Chronosphere MR 250mg granules sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 13665911000001109 (dm+d codes) | Epilim Chronosphere MR 500mg granules sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 13666311000001103 (dm+d codes) | Epilim Chronosphere MR 750mg granules sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 13666611000001108 (dm+d codes) | Epilim Chronosphere MR 50mg granules sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 13718611000001103 (dm+d codes) | Sodium valproate 100mg modified-release granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 13718711000001107 (dm+d codes) | Sodium valproate 250mg modified-release granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 13718811000001104 (dm+d codes) | Sodium valproate 50mg modified-release granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 13718911000001109 (dm+d codes) | Sodium valproate 750mg modified-release granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 13722811000001106 (dm+d codes) | Gabapentin 300mg capsules (Ranbaxy (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13753511000001102 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Tillomed Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 138611000001109 (dm+d codes) | Topamax 50mg tablets (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 13891811000001106 (dm+d codes) | Phenytoin 90mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 13893911000001100 (dm+d codes) | Phenytoin 90mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 13917811000001106 (dm+d codes) | Lamictal 25mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13918011000001104 (dm+d codes) | Lamictal 50mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13928311000001105 (dm+d codes) | Lyrica 50mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13928511000001104 (dm+d codes) | Lyrica 75mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13985811000001103 (dm+d codes) | Tegretol 100mg/5ml liquid (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13986611000001107 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 13987711000001100 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 14010811000001103 (dm+d codes) | Gabapentin 400mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 14014011000001102 (dm+d codes) | Gabapentin 400mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 14016711000001109 (dm+d codes) | Pregabalin 75mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 14016811000001101 (dm+d codes) | Pregabalin 75mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 14055611000001100 (dm+d codes) | Lamotrigine 25mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 14194411000001101 (dm+d codes) | Vimpat 200mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14194911000001109 (dm+d codes) | Vimpat 50mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14196211000001105 (dm+d codes) | Vimpat 200mg/20ml solution for infusion vials (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14196911000001101 (dm+d codes) | Vimpat 150mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14199511000001103 (dm+d codes) | Vimpat 100mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14203611000001101 (dm+d codes) | Lacosamide 200mg/20ml solution for infusion vials | Anti-seizure medication CPRD gold (all) primary care |
| 14220911000001108 (dm+d codes) | Epilim Chrono 200 tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14252711000001109 (dm+d codes) | Gabapentin 800mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 142605001000027105 (dm+d codes) | Sodium valproate CR 300mg Tablet (Hillcross Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 142611000001108 (dm+d codes) | Stesolid 10mg rectal tube (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14262811000001106 (dm+d codes) | Keppra 100mg/ml oral solution (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14263111000001105 (dm+d codes) | Keppra 250mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14263511000001101 (dm+d codes) | Keppra 500mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 142645001000027100 (dm+d codes) | Sodium valproate CR 500mg Tablet (Hillcross Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14316311000001106 (dm+d codes) | Vimpat 15mg/ml syrup (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 14376511000001105 (dm+d codes) | Lyrica 100mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14377511000001107 (dm+d codes) | Lyrica 150mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14410411000001105 (dm+d codes) | Lacosamide 15mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 14593611000001108 (dm+d codes) | Zonegran 100mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14624511000001108 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14624811000001106 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14664211000001104 (dm+d codes) | Rivotril 2mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14685311000001109 (dm+d codes) | Trileptal 300mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14738811000001108 (dm+d codes) | Lamictal 25mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 14770211000001106 (dm+d codes) | Phenytoin sodium 100mg tablets (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15047811000001103 (dm+d codes) | Mysoline 250mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15056411000001104 (dm+d codes) | Lamotrigine 100mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15075911000001102 (dm+d codes) | Carbamazepine 400mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15076411000001101 (dm+d codes) | Carbamazepine 200mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15076811000001104 (dm+d codes) | Carbamazepine 200mg modified-release tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15077211000001103 (dm+d codes) | Clonazepam 2mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15105511000001108 (dm+d codes) | Lamotrigine 50mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15125311000001109 (dm+d codes) | Pregabalin 150mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 15125411000001102 (dm+d codes) | Pregabalin 150mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 15165011000001104 (dm+d codes) | Gabapentin 600mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15166711000001105 (dm+d codes) | Oxcarbazepine 300mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15175811000001104 (dm+d codes) | Sodium valproate 300mg modified-release tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 15243311000001108 (dm+d codes) | Pregabalin 200mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 15243411000001101 (dm+d codes) | Pregabalin 200mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 15356811000001101 (dm+d codes) | Gabapentin 600mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15439411000001102 (dm+d codes) | Epilim Chronosphere MR 1000mg granules sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 15451911000001105 (dm+d codes) | Primidone 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 15535811000001106 (dm+d codes) | Valproic acid 250mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 15536811000001103 (dm+d codes) | Valproic acid 250mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 15621611000001101 (dm+d codes) | Phenytoin 300mg/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 15621911000001107 (dm+d codes) | Phenytoin 300mg/5ml oral suspension (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 15627711000001101 (dm+d codes) | Clonazepam 500microgram tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15628011000001102 (dm+d codes) | Clobazam 10mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15632911000001103 (dm+d codes) | Phenytoin 300mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 156945001000027109 (dm+d codes) | Diazepam 5mg Rectal tubes (Hillcross Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 157005001000027109 (dm+d codes) | Diazepam 10mg Rectal tubes (Hillcross Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15849411000001105 (dm+d codes) | Oxcarbazepine 150mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15849611000001108 (dm+d codes) | Oxcarbazepine 300mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 15915211000001106 (dm+d codes) | Pregabalin 25mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 159611000001104 (dm+d codes) | Neurontin 800mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16056111000001107 (dm+d codes) | Afinitor 10mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16058511000001102 (dm+d codes) | Lamotrigine 25mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16059011000001100 (dm+d codes) | Lamotrigine 50mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16059211000001105 (dm+d codes) | Lamotrigine 100mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16085211000001103 (dm+d codes) | Topiramate 25mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16086111000001103 (dm+d codes) | Topiramate 200mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16091111000001106 (dm+d codes) | Topiramate 15mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 16091211000001100 (dm+d codes) | Topiramate 15mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 16102311000001106 (dm+d codes) | Valproic acid 500mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 16102411000001104 (dm+d codes) | Valproic acid 500mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 16168411000001101 (dm+d codes) | Topiramate 25mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16172011000001103 (dm+d codes) | Epilim Chrono 200 tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16172211000001108 (dm+d codes) | Epilim Chrono 300 tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16172411000001107 (dm+d codes) | Epilim Chrono 500 tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16172611000001105 (dm+d codes) | Epilim 200mg/5ml syrup (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16177011000001101 (dm+d codes) | Topiramate 25mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16177211000001106 (dm+d codes) | Topiramate 50mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16177411000001105 (dm+d codes) | Topiramate 25mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16177611000001108 (dm+d codes) | Topiramate 50mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16177911000001102 (dm+d codes) | Topiramate 100mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16178611000001107 (dm+d codes) | Zebinix 800mg tablets (BIAL Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16185611000001106 (dm+d codes) | Topiramate 15mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16185811000001105 (dm+d codes) | Topiramate 25mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16186011000001108 (dm+d codes) | Topiramate 50mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16186411000001104 (dm+d codes) | Topiramate 50mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16186611000001101 (dm+d codes) | Topiramate 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16193811000001107 (dm+d codes) | Keppra 100mg/ml oral solution (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16194611000001106 (dm+d codes) | Lamictal 25mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16195311000001102 (dm+d codes) | Lamictal 200mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16195611000001107 (dm+d codes) | Lamictal 25mg dispersible tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16197411000001103 (dm+d codes) | Eslicarbazepine 800mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 16204211000001109 (dm+d codes) | Lyrica 25mg capsules (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16204811000001105 (dm+d codes) | Lyrica 50mg capsules (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16205111000001104 (dm+d codes) | Lyrica 75mg capsules (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16205511000001108 (dm+d codes) | Lyrica 150mg capsules (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16208711000001105 (dm+d codes) | Mysoline 250mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16263711000001103 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16264811000001109 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16266611000001101 (dm+d codes) | Tegretol 200mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16267311000001109 (dm+d codes) | Tegretol 400mg tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16267611000001104 (dm+d codes) | Tegretol 100mg/5ml liquid (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 162715001000027106 (dm+d codes) | Epilim ec 200mg Gastro-resistant tablet (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 162725001000027102 (dm+d codes) | Epilim ec 500mg Gastro-resistant tablet (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 16516411000001108 (dm+d codes) | Lyrica 50mg capsules (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16534511000001105 (dm+d codes) | Lamictal 25mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16534711000001100 (dm+d codes) | Lamictal 50mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16583311000001107 (dm+d codes) | Lyrica 75mg capsules (Stephar (U.K.) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 16632811000001106 (dm+d codes) | Paraldehyde 50% in Olive oil rectal solution (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 16634911000001105 (dm+d codes) | Paraldehyde 50% in Olive oil rectal solution | Anti-seizure medication CPRD gold (all) primary care |
| 16677911000001101 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Stephar (U.K.) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17020811000001104 (dm+d codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 17020911000001109 (dm+d codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 17021011000001101 (dm+d codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 17021111000001100 (dm+d codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 17111000001104 (dm+d codes) | Phenytoin sodium 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17298211000001101 (dm+d codes) | Rivotril 500microgram tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 17459311000001107 (dm+d codes) | Tegretol 400mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17459711000001106 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 174985001000027109 (dm+d codes) | Clonazepam 500microgram/5ml Oral solution (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17511811000001101 (dm+d codes) | Keppra 250mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17512011000001104 (dm+d codes) | Keppra 750mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17569111000001106 (dm+d codes) | Lyrica 300mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 17575611000001109 (dm+d codes) | Topiramate 25mg capsules (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 176211000001108 (dm+d codes) | Phenobarbital 60mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 177785001000027109 (dm+d codes) | Vigabatrin 125mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 17822611000001103 (dm+d codes) | Topiramate 25mg capsules (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17822911000001109 (dm+d codes) | Topiramate 50mg capsules (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17824311000001101 (dm+d codes) | Carbamazepine 200mg modified-release tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17824511000001107 (dm+d codes) | Carbamazepine 400mg modified-release tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17824711000001102 (dm+d codes) | Carbamazepine 100mg tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17824911000001100 (dm+d codes) | Carbamazepine 200mg tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 178425001000027101 (dm+d codes) | Gabapentin 250mg/5ml Oral solution (Boots Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17845001000027104 (dm+d codes) | Phenobarbital 15mg Tablet (Celltech Pharma Europe Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17855001000027101 (dm+d codes) | Phenobarbital 30mg Tablet (Celltech Pharma Europe Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17861111000001106 (dm+d codes) | Clonazepam 500microgram tablets (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17865001000027105 (dm+d codes) | Phenobarbital 60mg Tablet (Celltech Pharma Europe Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17870411000001103 (dm+d codes) | Clonazepam 500microgram orodispersible tablets | Anti-seizure medication CPRD gold (all) primary care |
| 17895001000027107 (dm+d codes) | Phenobarbital 15mg/5ml Oral solution (William Ransom) | Anti-seizure medication CPRD gold (all) primary care |
| 17913811000001107 (dm+d codes) | Gabapentin 300mg capsules (Phoenix Healthcare Distribution Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17945001000027109 (dm+d codes) | Phenytoin 50mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17955001000027107 (dm+d codes) | Phenytoin 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17964111000001104 (dm+d codes) | Phenobarbital 30mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17966511000001102 (dm+d codes) | Clonazepam 500microgram tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17971011000001105 (dm+d codes) | Gabapentin 100mg capsules (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17971411000001101 (dm+d codes) | Gabapentin 300mg capsules (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17971811000001104 (dm+d codes) | Gabapentin 400mg capsules (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17985001000027100 (dm+d codes) | Phenytoin 100mg Capsule (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 17999911000001103 (dm+d codes) | Clonazepam 500microgram oral lyophilisates sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 18047011000001103 (dm+d codes) | Ammonium bromide 400mg/5ml / Potassium bromide 400mg/5ml / Sodium bromide 400mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 18047111000001102 (dm+d codes) | Triple Bromide 1.2g/5ml oral solution (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 18061611000001109 (dm+d codes) | Keppra 1g tablets (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18078411000001107 (dm+d codes) | Lamotrigine 25mg tablets (Fannin (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18084111000001100 (dm+d codes) | Zonisamide 50mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 18084211000001106 (dm+d codes) | Zonisamide 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 18155711000001103 (dm+d codes) | Topamax 25mg sprinkle capsules (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18195711000001107 (dm+d codes) | Tegretol 100mg/5ml liquid (Necessity Supplies Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18195911000001109 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Necessity Supplies Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18196211000001106 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Necessity Supplies Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18196611000001108 (dm+d codes) | Tegretol 200mg tablets (Necessity Supplies Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18196811000001107 (dm+d codes) | Tegretol 400mg tablets (Necessity Supplies Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18270711000001108 (dm+d codes) | Keppra 250mg tablets (Necessity Supplies Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18389711000001104 (dm+d codes) | Clobazam 10mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 184311000001104 (dm+d codes) | Sabril 500mg tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 18455311000001101 (dm+d codes) | Mysoline 50mg tablets (SERB) | Anti-seizure medication CPRD gold (all) primary care |
| 18469511000001101 (dm+d codes) | Topiramate 25mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18469711000001106 (dm+d codes) | Topiramate 50mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18520211000001109 (dm+d codes) | Paraldehyde 50% in Arachis oil rectal solution | Anti-seizure medication CPRD gold (all) primary care |
| 185711000001101 (dm+d codes) | Epanutin 30mg/5ml oral suspension (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18576511000001108 (dm+d codes) | Epilim Chrono 200 tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 18576711000001103 (dm+d codes) | Epilim Chrono 300 tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 18576911000001101 (dm+d codes) | Epilim Chrono 500 tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 18577111000001101 (dm+d codes) | Epilim 200mg/5ml syrup (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 18606911000001100 (dm+d codes) | Primidone 250mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 18610411000001108 (dm+d codes) | Rivotril 500microgram tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 186311000001105 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 187111000001106 (dm+d codes) | Phenobarbital 30mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18742911000001103 (dm+d codes) | Topiramate 25mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 18769311000001102 (dm+d codes) | Trobalt 50mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18769811000001106 (dm+d codes) | Trobalt 400mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18770111000001101 (dm+d codes) | Trobalt 300mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18770411000001106 (dm+d codes) | Trobalt 200mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18770811000001108 (dm+d codes) | Trobalt 100mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 18772111000001102 (dm+d codes) | Retigabine 50mg tablets and Retigabine 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 18781211000001106 (dm+d codes) | Phenytoin sodium 100mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19174011000001104 (dm+d codes) | Topamax 15mg sprinkle capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 191911000001102 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 194275001000027103 (dm+d codes) | Carbamazepine 500mg/5ml Oral suspension (Martindale Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19472111000001105 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19472511000001101 (dm+d codes) | Levetiracetam 250mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19472711000001106 (dm+d codes) | Levetiracetam 500mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19472911000001108 (dm+d codes) | Levetiracetam 750mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19484711000001106 (dm+d codes) | Levetiracetam 250mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19484911000001108 (dm+d codes) | Levetiracetam 500mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19490111000001100 (dm+d codes) | Levetiracetam 250mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19490311000001103 (dm+d codes) | Levetiracetam 500mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19491711000001107 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19530211000001109 (dm+d codes) | Buccolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19530511000001107 (dm+d codes) | Buccolam 5mg/1ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19530811000001105 (dm+d codes) | Buccolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19531111000001109 (dm+d codes) | Buccolam 10mg/2ml oromucosal solution pre-filled oral syringes (Shire Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 195385001000027109 (dm+d codes) | Sodium valproate with valproic acid 200mg modified release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 195395001000027108 (dm+d codes) | Sodium valproate with valproic acid 300mg modified release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 195405001000027100 (dm+d codes) | Sodium valproate with valproic acid 500mg modified release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 19570411000001105 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19617711000001104 (dm+d codes) | Mysoline 250mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 196211000001103 (dm+d codes) | Carbamazepine 200mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19632511000001100 (dm+d codes) | Levetiracetam 500mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19632711000001105 (dm+d codes) | Levetiracetam 750mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19633111000001103 (dm+d codes) | Levetiracetam 250mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19657311000001109 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19664811000001102 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19665211000001102 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 196675001000027107 (dm+d codes) | Phenytoin 90mg/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 19744011000001106 (dm+d codes) | Everolimus 2.5mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 19817511000001100 (dm+d codes) | Carbamazepine 100mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19817711000001105 (dm+d codes) | Carbamazepine 200mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19817911000001107 (dm+d codes) | Carbamazepine 400mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19821611000001100 (dm+d codes) | Lacosamide 10mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 19843411000001102 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19861211000001109 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19868011000001105 (dm+d codes) | Matever 750mg tablets (Aspire Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19868411000001101 (dm+d codes) | Matever 500mg tablets (Aspire Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19868711000001107 (dm+d codes) | Matever 250mg tablets (Aspire Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 198711000001109 (dm+d codes) | Epanutin 300mg capsules (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 19976511000001103 (dm+d codes) | Paraldehyde 50% in Sunflower oil rectal solution | Anti-seizure medication CPRD gold (all) primary care |
| 19977911000001108 (dm+d codes) | Sodium valproate 500mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 199911000001103 (dm+d codes) | Epanutin 25mg capsules (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 200005001000027106 (dm+d codes) | Diazepam 20mg rectal tubes | Anti-seizure medication CPRD gold (all) primary care |
| 20018711000001105 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20019211000001108 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20028611000001107 (dm+d codes) | Topamax 50mg sprinkle capsules (Lexon (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20065611000001108 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 20128211000001100 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 20167011000001102 (dm+d codes) | Lamotrigine 25mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20167211000001107 (dm+d codes) | Lamotrigine 50mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20167411000001106 (dm+d codes) | Lamotrigine 100mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20167611000001109 (dm+d codes) | Lamotrigine 200mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20168111000001100 (dm+d codes) | Levetiracetam 250mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20168311000001103 (dm+d codes) | Levetiracetam 500mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20168511000001109 (dm+d codes) | Levetiracetam 750mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20168711000001104 (dm+d codes) | Levetiracetam 1g tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20343811000001100 (dm+d codes) | Inovelon 40mg/ml oral suspension (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20353211000001104 (dm+d codes) | Rufinamide 40mg/ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 20353711000001106 (dm+d codes) | Vimpat 10mg/ml syrup (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20359311000001105 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20385001000027101 (dm+d codes) | Mysoline 250mg Tablet (AstraZeneca UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20395001000027102 (dm+d codes) | Mysoline 250mg/5ml Oral suspension (AstraZeneca UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 204111000001102 (dm+d codes) | Gardenal Sodium 200mg/1ml solution for injection ampoules (Concord Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20451011000001102 (dm+d codes) | Vimpat 50mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 205311000001101 (dm+d codes) | Carbamazepine 400mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20536511000001107 (dm+d codes) | Acetazolamide 250mg tablets (Advanz Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 205411000001108 (dm+d codes) | Phenobarbital 60mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20545811000001103 (dm+d codes) | Lyrica 20mg/ml oral solution (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20556411000001107 (dm+d codes) | Pregabalin 20mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 20560511000001102 (dm+d codes) | Epilim Chronosphere MR 100mg granules sachets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 206611000001101 (dm+d codes) | Carbamazepine 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 208611000001100 (dm+d codes) | Epanutin 50mg capsules (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20901711000001105 (dm+d codes) | Topiramate 25mg tablets (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20910411000001105 (dm+d codes) | Topiramate 15mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20910611000001108 (dm+d codes) | Topiramate 25mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20910811000001107 (dm+d codes) | Topiramate 50mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20914811000001102 (dm+d codes) | Levetiracetam 250mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20915011000001107 (dm+d codes) | Levetiracetam 500mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20915211000001102 (dm+d codes) | Levetiracetam 750mg tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 20915411000001103 (dm+d codes) | Levetiracetam 1g tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21025111000001104 (dm+d codes) | Phenytoin sodium 100mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21028311000001106 (dm+d codes) | Levetiracetam 250mg tablets (Arrow Generics Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21032911000001107 (dm+d codes) | Gabapentin 100mg capsules (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21033111000001103 (dm+d codes) | Gabapentin 300mg capsules (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21033311000001101 (dm+d codes) | Gabapentin 400mg capsules (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21039111000001100 (dm+d codes) | Phenobarbital 15mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21039311000001103 (dm+d codes) | Phenobarbital 30mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21039511000001109 (dm+d codes) | Phenobarbital 60mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 210755001000027102 (dm+d codes) | Diazepam rectubes 20mg Rectal tubes (C P Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21200511000001100 (dm+d codes) | Phenytoin sodium 25mg capsules (Flynn Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21200711000001105 (dm+d codes) | Phenytoin sodium 50mg capsules (Flynn Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21200911000001107 (dm+d codes) | Phenytoin sodium 100mg capsules (Flynn Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21201111000001103 (dm+d codes) | Phenytoin sodium 300mg capsules (Flynn Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21212111000001106 (dm+d codes) | Fycompa 2mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21212611000001103 (dm+d codes) | Fycompa 4mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21213011000001101 (dm+d codes) | Fycompa 6mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21213311000001103 (dm+d codes) | Fycompa 8mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21213611000001108 (dm+d codes) | Fycompa 10mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21213911000001102 (dm+d codes) | Fycompa 12mg tablets (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21282711000001105 (dm+d codes) | Gabapentin 600mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21290611000001103 (dm+d codes) | Midazolam 2.5mg/0.25ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 21348611000001102 (dm+d codes) | Phenytoin sodium 25mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21349211000001109 (dm+d codes) | Phenytoin sodium 50mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21349411000001108 (dm+d codes) | Phenytoin sodium 100mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21349711000001102 (dm+d codes) | Phenytoin sodium 300mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21374911000001100 (dm+d codes) | Phenytoin sodium 25mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21375111000001104 (dm+d codes) | Phenytoin sodium 50mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21375311000001102 (dm+d codes) | Phenytoin sodium 100mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21375511000001108 (dm+d codes) | Phenytoin sodium 300mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21658711000001101 (dm+d codes) | Gabapentin 50mg/ml oral solution sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21660111000001105 (dm+d codes) | Gabapentin 50mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 21696311000001108 (dm+d codes) | Gabapentin 50mg/ml oral solution sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 217211000001104 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21730711000001109 (dm+d codes) | Desitrend 250mg granules sachets (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21731111000001102 (dm+d codes) | Desitrend 500mg granules sachets (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21731611000001105 (dm+d codes) | Desitrend 1000mg granules sachets (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21733211000001107 (dm+d codes) | Levetiracetam 1g granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 21733311000001104 (dm+d codes) | Levetiracetam 250mg granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 21733411000001106 (dm+d codes) | Levetiracetam 500mg granules sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 21802811000001108 (dm+d codes) | Tapclob 5mg/5ml oral suspension (Martindale Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21803611000001104 (dm+d codes) | Tapclob 10mg/5ml oral suspension (Martindale Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 21816611000001107 (dm+d codes) | Carbamazepine 100mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 21817311000001104 (dm+d codes) | Carbamazepine 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 21846411000001103 (dm+d codes) | Phenobarbital 30mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 21846811000001101 (dm+d codes) | Phenytoin sodium 100mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 21856411000001100 (dm+d codes) | Clobazam 10mg/5ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 21856511000001101 (dm+d codes) | Clobazam 5mg/5ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 21885111000001107 (dm+d codes) | Topiramate 50mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 21900611000001102 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 220011000001104 (dm+d codes) | Orlept 500mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 22019411000001102 (dm+d codes) | Gabapentin 300mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 22019611000001104 (dm+d codes) | Gabapentin 400mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 22057311000001105 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 22058811000001102 (dm+d codes) | Lamotrigine 25mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 22060711000001100 (dm+d codes) | Lamotrigine 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 22082011000001101 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 22195001000027100 (dm+d codes) | Nydrane 500mg Tablet (Lipha Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 223295001000027101 (dm+d codes) | Stesolid 10mg Rectal tubes (Dumex Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 22349411000001109 (dm+d codes) | Gabapentin 600mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 224395001000027108 (dm+d codes) | Gabitril 5mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 224405001000027100 (dm+d codes) | Gabitril 10mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 224415001000027103 (dm+d codes) | Gabitril 15mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 22629711000001105 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 22629911000001107 (dm+d codes) | Carbamazepine 100mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 22630111000001101 (dm+d codes) | Carbamazepine 200mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 22630311000001104 (dm+d codes) | Carbamazepine 400mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 22663911000001101 (dm+d codes) | Sodium valproate 400mg/4ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 23167411000001105 (dm+d codes) | Desitrend 100mg/ml oral solution (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23180311000001102 (dm+d codes) | Primidone 50mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23180511000001108 (dm+d codes) | Primidone 250mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23223411000001109 (dm+d codes) | Sodium valproate 500mg modified-release tablets (J M McGill Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23305711000001100 (dm+d codes) | Primidone 250mg tablets (SERB) | Anti-seizure medication CPRD gold (all) primary care |
| 23305911000001103 (dm+d codes) | Primidone 50mg tablets (SERB) | Anti-seizure medication CPRD gold (all) primary care |
| 233611000001104 (dm+d codes) | Rivotril 500microgram tablets (Roche Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23407511000001107 (dm+d codes) | Gabapentin 300mg capsules (Medreich Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 234145001000027105 (dm+d codes) | Timonil retard 400mg Modified-release tablet (C P Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23466511000001106 (dm+d codes) | Clonazepam 2.5mg/ml drops | Anti-seizure medication CPRD gold (all) primary care |
| 23480211000001109 (dm+d codes) | Primidone 250mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 235111000001108 (dm+d codes) | Topamax 200mg tablets (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23587811000001101 (dm+d codes) | Levetiracetam 250mg tablets (Bristol Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23595311000001103 (dm+d codes) | Phenytoin sodium 100mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23600711000001100 (dm+d codes) | Primidone 250mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 23614511000001103 (dm+d codes) | Gabapentin 300mg capsules (Creo Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23640811000001104 (dm+d codes) | Primidone 50mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 236505001000027100 (dm+d codes) | Epistatus 10mg/ml Oromucosal solution (Special Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 23675911000001104 (dm+d codes) | Lorazepam 2mg/1ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 240511000001105 (dm+d codes) | Phenobarbital 30mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 240965001000027100 (dm+d codes) | Ospolot fc 50mg Tablet (IDIS World Medicines) | Anti-seizure medication CPRD gold (all) primary care |
| 240985001000027102 (dm+d codes) | Ospolot fc 200mg Tablet (IDIS World Medicines) | Anti-seizure medication CPRD gold (all) primary care |
| 24104211000001101 (dm+d codes) | Afinitor 2.5mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 24104911000001105 (dm+d codes) | Gabapentin 300mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 24105111000001106 (dm+d codes) | Gabapentin 400mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 24105511000001102 (dm+d codes) | Gabapentin 600mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 24108311000001104 (dm+d codes) | Carbagen 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 24108811000001108 (dm+d codes) | Carbagen 200mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 24109211000001102 (dm+d codes) | Carbagen 400mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 241345001000027106 (dm+d codes) | Clonazepam 500micrograms/5ml solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 24354811000001102 (dm+d codes) | Lamotrigine 25mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 24355011000001107 (dm+d codes) | Lamotrigine 50mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 24365411000001108 (dm+d codes) | Levetiracetam 250mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 245125001000027101 (dm+d codes) | Phenobarbital oral liquid | Anti-seizure medication CPRD gold (all) primary care |
| 245615001000027106 (dm+d codes) | Carbamazepine oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 24595411000001108 (dm+d codes) | Zonisamide 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 24595511000001107 (dm+d codes) | Zonisamide 25mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 246675001000027100 (dm+d codes) | Levetiracetam Oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 248115001000027103 (dm+d codes) | Midazolam Oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 250015001000027101 (dm+d codes) | Phenobarbital capsule | Anti-seizure medication CPRD gold (all) primary care |
| 250155001000027102 (dm+d codes) | Primidone 100mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 250805001000027102 (dm+d codes) | Mesuximide 300mg Capsule | Anti-seizure medication CPRD gold (all) primary care |
| 251405001000027102 (dm+d codes) | Phenytoin sodium oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 251415001000027100 (dm+d codes) | Phenobarbital sodium oral liquid | Anti-seizure medication CPRD gold (all) primary care |
| 251711000001106 (dm+d codes) | Epanutin Infatabs 50mg chewable tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 251925001000027106 (dm+d codes) | Sodium valproate with valproic acid 100mg modified release granules | Anti-seizure medication CPRD gold (all) primary care |
| 251945001000027109 (dm+d codes) | Sodium valproate with valproic acid 250mg modified release granules | Anti-seizure medication CPRD gold (all) primary care |
| 251965001000027103 (dm+d codes) | Sodium valproate with valproic acid 500mg modified release granules | Anti-seizure medication CPRD gold (all) primary care |
| 251975001000027105 (dm+d codes) | Sodium valproate with valproic acid 750mg modified release granules | Anti-seizure medication CPRD gold (all) primary care |
| 251985001000027100 (dm+d codes) | Sodium valproate with valproic acid 1000mg modified release granules | Anti-seizure medication CPRD gold (all) primary care |
| 252205001000027104 (dm+d codes) | Sodium valproate oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 252695001000027103 (dm+d codes) | Sodium valproate with valproic acid 50mg modified release granules | Anti-seizure medication CPRD gold (all) primary care |
| 253111000001106 (dm+d codes) | Carbamazepine 400mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 25442311000001101 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 260011000001109 (dm+d codes) | Epimaz 100mg tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 261545001000027104 (dm+d codes) | Midazolam buccal solution | Anti-seizure medication CPRD gold (all) primary care |
| 261911000001101 (dm+d codes) | Tegretol Prolonged Release 200mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 262575001000027104 (dm+d codes) | Lamotrigine 50mg Suppository | Anti-seizure medication CPRD gold (all) primary care |
| 26811000001102 (dm+d codes) | Diazepam 10mg RecTubes (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 27989111000001104 (dm+d codes) | Levetiracetam 500mg tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 27989511000001108 (dm+d codes) | Levetiracetam 1g tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28036611000001106 (dm+d codes) | Sodium valproate 200mg modified-release tablets (Ennogen Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28037011000001101 (dm+d codes) | Sodium valproate 300mg modified-release tablets (Ennogen Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28050211000001106 (dm+d codes) | Sodium valproate 500mg modified-release tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 28267611000001105 (dm+d codes) | Sodium valproate 300mg modified-release tablets (Colorama Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 283311000001103 (dm+d codes) | Diazepam 2.5mg RecTubes (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28694511000001103 (dm+d codes) | Gabapentin 100mg capsules (Rivopharm (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28696911000001102 (dm+d codes) | Levetiracetam 1g tablets (Rivopharm (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28736211000001106 (dm+d codes) | Rewisca 100mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28736711000001104 (dm+d codes) | Rewisca 25mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28737611000001105 (dm+d codes) | Rewisca 50mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28738211000001107 (dm+d codes) | Rewisca 75mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28738711000001100 (dm+d codes) | Rewisca 150mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28739111000001108 (dm+d codes) | Rewisca 200mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28740211000001105 (dm+d codes) | Rewisca 225mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28742111000001100 (dm+d codes) | Rewisca 300mg capsules (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28909711000001107 (dm+d codes) | Lecaent 25mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28910011000001104 (dm+d codes) | Lecaent 50mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28910211000001109 (dm+d codes) | Lecaent 75mg capsules (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28910411000001108 (dm+d codes) | Lecaent 100mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28910611000001106 (dm+d codes) | Lecaent 150mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28910811000001105 (dm+d codes) | Lecaent 200mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28911211000001103 (dm+d codes) | Lecaent 300mg capsules (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28947311000001109 (dm+d codes) | Levetiracetam 500mg/5ml solution for infusion ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 28964511000001102 (dm+d codes) | Pregabalin 50mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28964811000001104 (dm+d codes) | Pregabalin 75mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28965011000001109 (dm+d codes) | Pregabalin 100mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28965811000001103 (dm+d codes) | Pregabalin 300mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28995001000027109 (dm+d codes) | Phenobarbital 30mg Tablet (C P Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28996411000001106 (dm+d codes) | Alzain 25mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28996611000001109 (dm+d codes) | Alzain 50mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28996911000001103 (dm+d codes) | Alzain 75mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28997111000001103 (dm+d codes) | Alzain 100mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28997311000001101 (dm+d codes) | Alzain 150mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28997511000001107 (dm+d codes) | Alzain 200mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28997711000001102 (dm+d codes) | Alzain 225mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 28997911000001100 (dm+d codes) | Alzain 300mg capsules (Dr Reddy's Laboratories (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 290011000001107 (dm+d codes) | Topamax 25mg tablets (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29065001000027104 (dm+d codes) | Phenytoin 50mg Tablet (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 291011000001103 (dm+d codes) | Rivotril 2mg tablets (Roche Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29105001000027107 (dm+d codes) | Phenytoin 50mg Tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 292411000001102 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 2925811000001101 (dm+d codes) | Lamictal 25mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 2927711000001103 (dm+d codes) | Lamictal 50mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 2928811000001105 (dm+d codes) | Lamictal 100mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 296811000001104 (dm+d codes) | Epimaz 200mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29794011000001101 (dm+d codes) | Perizam 1mg/ml oral suspension (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29794211000001106 (dm+d codes) | Perizam 2mg/ml oral suspension (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29933411000001108 (dm+d codes) | Clobazam 5mg/5ml oral suspension sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29935311000001100 (dm+d codes) | Pregabalin 75mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29936111000001108 (dm+d codes) | Pregabalin 50mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29936811000001101 (dm+d codes) | Pregabalin 150mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29938111000001107 (dm+d codes) | Pregabalin 300mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29938311000001109 (dm+d codes) | Pregabalin 25mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 29984311000001109 (dm+d codes) | Phenobarbital 15mg tablets (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 29984911000001105 (dm+d codes) | Phenytoin sodium 100mg capsules (Sigma Pharmaceuticals Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 30028711000001102 (dm+d codes) | Carbamazepine 200mg modified-release tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30076311000001104 (dm+d codes) | Phenobarbital 15mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30076511000001105 (dm+d codes) | Phenobarbital 30mg tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30101411000001101 (dm+d codes) | Topiramate 15mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30101611000001103 (dm+d codes) | Topiramate 25mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30102011000001102 (dm+d codes) | Topiramate 50mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30115211000001104 (dm+d codes) | Pregabalin 25mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30115811000001103 (dm+d codes) | Pregabalin 75mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30208011000001102 (dm+d codes) | Epanutin 50mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 30218211000001109 (dm+d codes) | Lamotrigine 25mg tablets (Mawdsley-Brooks &amp; Company Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30224311000001100 (dm+d codes) | Pregabalin 300mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30224511000001106 (dm+d codes) | Pregabalin 50mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30224911000001104 (dm+d codes) | Pregabalin 75mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30225511000001107 (dm+d codes) | Pregabalin 150mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 302911000001103 (dm+d codes) | Neurontin 400mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 304111000001109 (dm+d codes) | Phenobarbital 60mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 305385001000027103 (dm+d codes) | Tegretol retard 200mg Modified-release tablet (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 305395001000027104 (dm+d codes) | Tegretol retard 400mg Modified-release tablet (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 305485001000027106 (dm+d codes) | Clonazepam 2mg/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 305505001000027104 (dm+d codes) | Midazolam 10mg/ml buccal solution | Anti-seizure medication CPRD gold (all) primary care |
| 305635001000027100 (dm+d codes) | Midazolam maleate buccal solution | Anti-seizure medication CPRD gold (all) primary care |
| 30764211000001106 (dm+d codes) | Phenytoin sodium 100mg tablets (Almus Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30782211000001104 (dm+d codes) | Pregabalin 200mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30782611000001102 (dm+d codes) | Pregabalin 300mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30782811000001103 (dm+d codes) | Pregabalin 50mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30783011000001100 (dm+d codes) | Pregabalin 75mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30786811000001102 (dm+d codes) | Pregabalin 25mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30787011000001106 (dm+d codes) | Pregabalin 50mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30787311000001109 (dm+d codes) | Pregabalin 75mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30811000001102 (dm+d codes) | Phenobarbital 30mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30845411000001100 (dm+d codes) | Phenytoin sodium 100mg capsules (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 30854111000001109 (dm+d codes) | Primidone 50mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30854311000001106 (dm+d codes) | Primidone 250mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 30951511000001107 (dm+d codes) | Sodium valproate 200mg modified-release tablets (DE Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 3145211000001105 (dm+d codes) | Lamictal 200mg tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3145811000001106 (dm+d codes) | Lamictal 5mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3146411000001100 (dm+d codes) | Lamictal 25mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3147211000001102 (dm+d codes) | Lamictal 100mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31499611000001107 (dm+d codes) | Briviact 10mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31500511000001109 (dm+d codes) | Briviact 25mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31501311000001108 (dm+d codes) | Briviact 50mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31502211000001107 (dm+d codes) | Briviact 75mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31502611000001109 (dm+d codes) | Briviact 100mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31505811000001101 (dm+d codes) | Briviact 50mg/5ml solution for injection vials (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31507311000001102 (dm+d codes) | Briviact 10mg/ml oral solution (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31533711000001103 (dm+d codes) | Brivaracetam 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 31533811000001106 (dm+d codes) | Brivaracetam 10mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 31534011000001103 (dm+d codes) | Brivaracetam 25mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 31534111000001102 (dm+d codes) | Brivaracetam 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 31534211000001108 (dm+d codes) | Brivaracetam 50mg/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 31534411000001107 (dm+d codes) | Brivaracetam 50mg/5ml solution for injection vials | Anti-seizure medication CPRD gold (all) primary care |
| 31534511000001106 (dm+d codes) | Brivaracetam 75mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 3160011000001104 (dm+d codes) | Tegretol 100mg Chewtabs (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3160911000001100 (dm+d codes) | Tegretol 200mg Chewtabs (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31898611000001108 (dm+d codes) | Pregabalin 25mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31899611000001104 (dm+d codes) | Pregabalin 50mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31901111000001103 (dm+d codes) | Pregabalin 75mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31901711000001102 (dm+d codes) | Pregabalin 100mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31902411000001103 (dm+d codes) | Pregabalin 150mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31902911000001106 (dm+d codes) | Pregabalin 200mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31904411000001105 (dm+d codes) | Pregabalin 300mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 31953611000001101 (dm+d codes) | Clobazam 5mg/5ml oral suspension sugar free (Thame Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 321238008 (dm+d codes) | Diazepam 10mg suppositories | Anti-seizure medication CPRD gold (all) primary care |
| 321272000 (dm+d codes) | Clobazam 10mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 32164811000001109 (dm+d codes) | Pregabalin 50mg capsules (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32167211000001101 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 322863001 (dm+d codes) | Carbamazepine 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322864007 (dm+d codes) | Carbamazepine 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322865008 (dm+d codes) | Carbamazepine 400mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322887004 (dm+d codes) | Carbamazepine 125mg suppositories | Anti-seizure medication CPRD gold (all) primary care |
| 322888009 (dm+d codes) | Carbamazepine 250mg suppositories | Anti-seizure medication CPRD gold (all) primary care |
| 322889001 (dm+d codes) | Carbamazepine 200mg chewable tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 322890005 (dm+d codes) | Carbamazepine 100mg chewable tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 322891009 (dm+d codes) | Carbamazepine 100mg/5ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 322897008 (dm+d codes) | Clonazepam 500microgram tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322898003 (dm+d codes) | Clonazepam 2mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322906007 (dm+d codes) | Ethosuximide 250mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 322908008 (dm+d codes) | Ethosuximide 250mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 322915000 (dm+d codes) | Phenobarbital 15mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322916004 (dm+d codes) | Phenobarbital 30mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322917008 (dm+d codes) | Phenobarbital 60mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322927002 (dm+d codes) | Phenobarbital 15mg/5ml elixir | Anti-seizure medication CPRD gold (all) primary care |
| 322930009 (dm+d codes) | Phenytoin 50mg chewable tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322931008 (dm+d codes) | Phenytoin 30mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 322933006 (dm+d codes) | Phenytoin sodium 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322934000 (dm+d codes) | Phenytoin sodium 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322942004 (dm+d codes) | Phenytoin sodium 300mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 322943009 (dm+d codes) | Phenytoin sodium 25mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 322944003 (dm+d codes) | Phenytoin sodium 50mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 322948000 (dm+d codes) | Primidone 250mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322956002 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322957006 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322977004 (dm+d codes) | Vigabatrin 500mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322979001 (dm+d codes) | Vigabatrin 500mg oral powder sachets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 322981004 (dm+d codes) | Lamotrigine 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322982006 (dm+d codes) | Lamotrigine 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322985008 (dm+d codes) | Lamotrigine 25mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 322991005 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 322992003 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 322994002 (dm+d codes) | Lamotrigine 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323002000 (dm+d codes) | Piracetam 800mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323003005 (dm+d codes) | Piracetam 1.2g tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323004004 (dm+d codes) | Piracetam 333.3mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 323008001 (dm+d codes) | Valproic acid 150mg gastro-resistant capsules | Anti-seizure medication CPRD gold (all) primary care |
| 323009009 (dm+d codes) | Valproic acid 300mg gastro-resistant capsules | Anti-seizure medication CPRD gold (all) primary care |
| 323010004 (dm+d codes) | Valproic acid 500mg gastro-resistant capsules | Anti-seizure medication CPRD gold (all) primary care |
| 323013002 (dm+d codes) | Gabapentin 100mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 323014008 (dm+d codes) | Gabapentin 300mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 323015009 (dm+d codes) | Gabapentin 400mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 323021008 (dm+d codes) | Gabapentin 600mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323022001 (dm+d codes) | Gabapentin 800mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323023006 (dm+d codes) | Topiramate 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323024000 (dm+d codes) | Topiramate 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323025004 (dm+d codes) | Topiramate 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323029005 (dm+d codes) | Topiramate 25mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323046008 (dm+d codes) | Oxcarbazepine 150mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323047004 (dm+d codes) | Oxcarbazepine 300mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323048009 (dm+d codes) | Oxcarbazepine 600mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323053004 (dm+d codes) | Levetiracetam 1g tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323054005 (dm+d codes) | Levetiracetam 500mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323055006 (dm+d codes) | Levetiracetam 250mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 323069006 (dm+d codes) | Diazepam 2.5mg/1.25ml rectal solution tube | Anti-seizure medication CPRD gold (all) primary care |
| 323074003 (dm+d codes) | Diazepam 10mg/2.5ml rectal solution tube | Anti-seizure medication CPRD gold (all) primary care |
| 32398011000001100 (dm+d codes) | Clonazepam 500microgram tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32490011000001109 (dm+d codes) | Gabapentin 300mg capsules (Brown &amp; Burk UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32498111000001107 (dm+d codes) | Phenobarbital 15mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32518811000001108 (dm+d codes) | Buccolam 10mg/2ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32519111000001108 (dm+d codes) | Buccolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32519411000001103 (dm+d codes) | Buccolam 5mg/1ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32519711000001109 (dm+d codes) | Buccolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes (Neuraxpharm UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32636411000001107 (dm+d codes) | Rivotril 1mg/1ml concentrate for solution for injection ampoules and diluent (Imported (France)) | Anti-seizure medication CPRD gold (all) primary care |
| 32655111000001107 (dm+d codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 32655211000001101 (dm+d codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 32655311000001109 (dm+d codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 32655411000001102 (dm+d codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 32711911000001108 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 32879411000001109 (dm+d codes) | Pregabalin 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 32880411000001109 (dm+d codes) | Topiramate 25mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 33038311000001102 (dm+d codes) | Sultiame 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 330601002 (dm+d codes) | Acetazolamide 250mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 33185001000027108 (dm+d codes) | Valium 5mg/ml Injection (Roche Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 332111000001105 (dm+d codes) | Carbamazepine 100mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33355001000027106 (dm+d codes) | Valium 5mg Suppository (Roche Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33365001000027102 (dm+d codes) | Valium 10mg Suppository (Roche Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33382211000001102 (dm+d codes) | Acetazolamide 250mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 333834003 (dm+d codes) | Thiopental 500mg powder for solution for injection vials | Anti-seizure medication CPRD gold (all) primary care |
| 33493711000001109 (dm+d codes) | Ethosuximide 250mg/5ml syrup (Essential Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33607411000001109 (dm+d codes) | Pregabalin 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33608411000001108 (dm+d codes) | Pregabalin 75mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33608611000001106 (dm+d codes) | Pregabalin 50mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33608811000001105 (dm+d codes) | Pregabalin 25mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33709111000001104 (dm+d codes) | Axalid 25mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33709711000001103 (dm+d codes) | Axalid 50mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33710311000001109 (dm+d codes) | Axalid 75mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33710511000001103 (dm+d codes) | Axalid 100mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33712111000001106 (dm+d codes) | Axalid 150mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33712511000001102 (dm+d codes) | Axalid 200mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33715511000001108 (dm+d codes) | Axalid 225mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 33715911000001101 (dm+d codes) | Axalid 300mg capsules (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34165411000001101 (dm+d codes) | Votubia 5mg dispersible tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34195511000001104 (dm+d codes) | Ethosuximide 250mg/5ml syrup (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34211000001106 (dm+d codes) | Carbamazepine 200mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34246711000001109 (dm+d codes) | Zacco 5mg/5ml oral suspension (Thame Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34327611000001105 (dm+d codes) | Ethosuximide 250mg/5ml syrup (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34378611000001108 (dm+d codes) | Perampanel 4mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 34466511000001108 (dm+d codes) | Epistatus 10mg/1ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34466711000001103 (dm+d codes) | Midazolam 10mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 34581711000001102 (dm+d codes) | Zebinix 200mg tablets (BIAL Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34606611000001108 (dm+d codes) | Eslicarbazepine 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 34683911000001107 (dm+d codes) | Pregabalin 300mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 34754411000001104 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Bowmed Ibisqus Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 34933411000001108 (dm+d codes) | Gabapentin 300mg capsules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35163411000001107 (dm+d codes) | Lamotrigine 25mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35163611000001105 (dm+d codes) | Lamotrigine 50mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35164011000001101 (dm+d codes) | Lamotrigine 200mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35164211000001106 (dm+d codes) | Levetiracetam 250mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35176711000001102 (dm+d codes) | Pregabalin 50mg capsules (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35178511000001108 (dm+d codes) | Pregabalin 300mg capsules (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35186611000001101 (dm+d codes) | Topiramate 25mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35187011000001106 (dm+d codes) | Topiramate 100mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35187211000001101 (dm+d codes) | Topiramate 200mg tablets (Milpharm Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 352911000001109 (dm+d codes) | Epimaz Retard 200mg tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35721611000001105 (dm+d codes) | Gabapentin 300mg capsules (Tillomed Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35832511000001104 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 35919911000001103 (dm+d codes) | Topiramate 15mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 35920011000001101 (dm+d codes) | Topiramate 25mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 35920111000001100 (dm+d codes) | Topiramate 50mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 35928211000001109 (dm+d codes) | Sodium valproate 200mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 35928311000001101 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 35928511000001107 (dm+d codes) | Sodium valproate 400mg powder and solvent for solution for injection vials | Anti-seizure medication CPRD gold (all) primary care |
| 36015611000001102 (dm+d codes) | Phenytoin sodium 250mg/5ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 36037711000001108 (dm+d codes) | Lamotrigine 2mg dispersible tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 36038411000001103 (dm+d codes) | Levetiracetam 500mg/5ml solution for infusion vials | Anti-seizure medication CPRD gold (all) primary care |
| 36040511000001101 (dm+d codes) | Lorazepam 4mg/1ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 36061111000001107 (dm+d codes) | Fosphenytoin 750mg/10ml solution for injection vials | Anti-seizure medication CPRD gold (all) primary care |
| 36097511000001106 (dm+d codes) | Diazepam 10mg/2ml emulsion for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 36097611000001105 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD gold (all) primary care |
| 36107311000001106 (dm+d codes) | Ethosuximide 250mg/5ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 3637411000001100 (dm+d codes) | Keppra 1g tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 364611000001102 (dm+d codes) | Emeside 250mg/5ml syrup (Fontus Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36508311000001103 (dm+d codes) | Cannabidiol 100mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 36510411000001109 (dm+d codes) | Zebinix 50mg/1ml oral suspension (BIAL Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36511211000001104 (dm+d codes) | Eslicarbazepine 50mg/1ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 36561911000001107 (dm+d codes) | Levetiracetam 500mg/100ml infusion bags | Anti-seizure medication CPRD gold (all) primary care |
| 36566611000001108 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 36567811000001109 (dm+d codes) | Topiramate 100mg/5ml oral suspension sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3672511000001102 (dm+d codes) | Trileptal 300mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36753111000001103 (dm+d codes) | Topiramate 100mg/5ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 36753211000001109 (dm+d codes) | Topiramate 50mg/5ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 36776811000001103 (dm+d codes) | Fycompa 0.5mg/ml oral suspension (Eisai Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36784011000001105 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Esteve Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36813311000001107 (dm+d codes) | Lamotrigine 50mg tablets (Torrent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36830311000001109 (dm+d codes) | Levetiracetam 250mg tablets (Torrent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 36915111000001101 (dm+d codes) | Perampanel 500micrograms/ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 369911000001109 (dm+d codes) | Carbagen SR 200mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37082411000001106 (dm+d codes) | Carbamazepine 200mg modified-release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 37082511000001105 (dm+d codes) | Carbamazepine 400mg modified-release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 37093211000001100 (dm+d codes) | Levetiracetam 250mg tablets (Relonchem Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3711611000001107 (dm+d codes) | Sabril 500mg oral powder sachets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 371194003 (dm+d codes) | Primidone 250mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 37293211000001107 (dm+d codes) | Levetiracetam 500mg/5ml concentrate for solution for infusion vials (Sciecure Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37322611000001104 (dm+d codes) | Dilantin Infatabs 50mg chewable tablets (Imported (Canada)) | Anti-seizure medication CPRD gold (all) primary care |
| 37327811000001102 (dm+d codes) | Pregabalin 25mg capsules (Creo Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37329411000001108 (dm+d codes) | Pregabalin 75mg capsules (Creo Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 374700006 (dm+d codes) | Felbamate 600mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 37480211000001100 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free (Crescent Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 375136008 (dm+d codes) | Primidone 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 37515211000001102 (dm+d codes) | Keppra 250mg tablets (CST Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 375396003 (dm+d codes) | Levetiracetam 750mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 375522007 (dm+d codes) | Clonazepam 1mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 37573711000001104 (dm+d codes) | Belvo 250mg gastro-resistant tablets (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37574111000001103 (dm+d codes) | Belvo 500mg gastro-resistant tablets (Consilient Health Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37613111000001104 (dm+d codes) | Levetiracetam 250mg tablets (Crescent Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37669211000001108 (dm+d codes) | Keppra 100mg/ml oral solution (Ethigen Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3784111000001104 (dm+d codes) | Trileptal 600mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37982211000001101 (dm+d codes) | Syonell 500mg gastro-resistant tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 37982411000001102 (dm+d codes) | Syonell 250mg gastro-resistant tablets (Lupin Healthcare (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 38019511000001108 (dm+d codes) | Pregabalin 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38019611000001107 (dm+d codes) | Pregabalin 150mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38019711000001103 (dm+d codes) | Pregabalin 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38019811000001106 (dm+d codes) | Pregabalin 225mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38019911000001101 (dm+d codes) | Pregabalin 25mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38020011000001104 (dm+d codes) | Pregabalin 300mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38020111000001103 (dm+d codes) | Pregabalin 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38020211000001109 (dm+d codes) | Pregabalin 75mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 38029811000001101 (dm+d codes) | Epidyolex 100mg/ml oral solution (GW Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 380311000001102 (dm+d codes) | Carbamazepine 200mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 38109311000001105 (dm+d codes) | Kigabeq 100mg soluble tablets (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 38161111000001105 (dm+d codes) | Carbamazepine 100mg tablets (Medreich Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 3824311000001107 (dm+d codes) | Valclair 10mg suppositories (Durbin Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 38286011000001103 (dm+d codes) | Vigabatrin 100mg soluble tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 38286111000001102 (dm+d codes) | Vigabatrin 500mg soluble tablets sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 3839911000001106 (dm+d codes) | Trileptal 150mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3846411000001106 (dm+d codes) | Depakote 250mg gastro-resistant tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 3847111000001103 (dm+d codes) | Depakote 500mg gastro-resistant tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 38752611000001105 (dm+d codes) | Oxcarbazepine 60mg/ml oral suspension sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 38819911000001100 (dm+d codes) | Carbamazepine 200mg tablets (Medihealth (Northern) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3893111000001104 (dm+d codes) | Nootropil 800mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3894111000001102 (dm+d codes) | Nootropil 1200mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 38998111000001101 (dm+d codes) | Dyzantil 200mg modified-release tablets (Aspire Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 38999111000001108 (dm+d codes) | Dyzantil 500mg modified-release tablets (Aspire Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3901811000001103 (dm+d codes) | Gabitril 5mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3902111000001100 (dm+d codes) | Gabitril 10mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 39025611000001101 (dm+d codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 39107811000001107 (dm+d codes) | Sodium valproate 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39108211000001105 (dm+d codes) | Sodium valproate 200mg modified-release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39108311000001102 (dm+d codes) | Sodium valproate 300mg modified-release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39108411000001109 (dm+d codes) | Sodium valproate 500mg modified-release tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39205511000001103 (dm+d codes) | Desizon 20mg/ml oral suspension (Desitin Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3920911000001105 (dm+d codes) | Convulex 150mg gastro-resistant capsules (Gerot Lannach UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3921311000001104 (dm+d codes) | Convulex 300mg gastro-resistant capsules (Gerot Lannach UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3921711000001100 (dm+d codes) | Convulex 500mg gastro-resistant capsules (Gerot Lannach UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3923811000001107 (dm+d codes) | Tegretol 125mg suppositories (Essential Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3924111000001103 (dm+d codes) | Tegretol 250mg suppositories (Essential Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 3925811000001106 (dm+d codes) | Ativan 4mg/1ml solution for injection ampoules (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 39334711000001109 (dm+d codes) | Ethosuximide 250mg/5ml syrup (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 39704911000001104 (dm+d codes) | Tiagabine 10mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39705011000001104 (dm+d codes) | Tiagabine 15mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39705111000001103 (dm+d codes) | Tiagabine 5mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 39709411000001106 (dm+d codes) | Diazepam 5mg/2.5ml rectal solution tube | Anti-seizure medication CPRD gold (all) primary care |
| 3971111000001102 (dm+d codes) | Diazemuls 10mg/2ml emulsion for injection ampoules (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 39803911000001103 (dm+d codes) | Fenfluramine 2.2mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 39845311000001108 (dm+d codes) | Carbamazepine 100mg tablets (Medihealth (Northern) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 39878911000001104 (dm+d codes) | Midazolam 5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 39879011000001108 (dm+d codes) | Midazolam 7.5mg/0.75ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD gold (all) primary care |
| 399711000001109 (dm+d codes) | Phenytoin sodium 100mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 40020211000001105 (dm+d codes) | Epesri 250mg capsules (Strides Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 401511000001108 (dm+d codes) | Neurontin 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 40199011000001106 (dm+d codes) | Ontozry 50mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medication CPRD gold (all) primary care |
| 40202111000001103 (dm+d codes) | Ontozry 100mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medication CPRD gold (all) primary care |
| 40202911000001100 (dm+d codes) | Ontozry 150mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medication CPRD gold (all) primary care |
| 40203711000001105 (dm+d codes) | Ontozry 200mg tablets (Angelini Pharma UK-I Limited) | Anti-seizure medication CPRD gold (all) primary care |
| 40206011000001100 (dm+d codes) | Ontozry 12.5mg/25mg tablets treatment initiation pack (Angelini Pharma UK-I Limited) | Anti-seizure medication CPRD gold (all) primary care |
| 40206211000001105 (dm+d codes) | Cenobamate 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 40206411000001109 (dm+d codes) | Cenobamate 12.5mg tablets and Cenobamate 25mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 40206511000001108 (dm+d codes) | Cenobamate 150mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 40206611000001107 (dm+d codes) | Cenobamate 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 40207211000001107 (dm+d codes) | Cenobamate 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 4021611000001103 (dm+d codes) | Lamictal 2mg dispersible tablets (GlaxoSmithKline UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 40217911000001100 (dm+d codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes sugar free (Xiromed) | Anti-seizure medication CPRD gold (all) primary care |
| 40218211000001108 (dm+d codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes sugar free (Xiromed) | Anti-seizure medication CPRD gold (all) primary care |
| 405811000001109 (dm+d codes) | Carbamazepine 400mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 40829211000001102 (dm+d codes) | Sodium valproate 300mg/3ml solution for injection vials | Anti-seizure medication CPRD gold (all) primary care |
| 40922211000001102 (dm+d codes) | Curatil Prolonged Release 200mg tablets (Tillomed Laboratories Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4092411000001104 (dm+d codes) | Nootropil 33% oral solution (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 409467001 (dm+d codes) | Gabapentin 250mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 410930002 (dm+d codes) | Zonisamide 100mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 4130011000001105 (dm+d codes) | Gabitril 15mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 41305001000027106 (dm+d codes) | Clomethiazole 8mg/ml IV infusion | Anti-seizure medication CPRD gold (all) primary care |
| 415161007 (dm+d codes) | Pregabalin 100mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 415162000 (dm+d codes) | Pregabalin 150mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 415163005 (dm+d codes) | Pregabalin 200mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 415164004 (dm+d codes) | Pregabalin 25mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 415165003 (dm+d codes) | Pregabalin 300mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 415166002 (dm+d codes) | Pregabalin 50mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 415167006 (dm+d codes) | Pregabalin 75mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 417050003 (dm+d codes) | Zonisamide 25mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 417678003 (dm+d codes) | Zonisamide 50mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 4196611000001108 (dm+d codes) | Phenobarbital 15mg/5ml elixir (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4196911000001102 (dm+d codes) | Phenobarbital 15mg/5ml elixir (Thornton &amp; Ross Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4197311000001100 (dm+d codes) | Phenobarbital 15mg/5ml elixir (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4205011000001105 (dm+d codes) | Topamax 15mg sprinkle capsules (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4206011000001101 (dm+d codes) | Topamax 25mg sprinkle capsules (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4206411000001105 (dm+d codes) | Topamax 50mg sprinkle capsules (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 421070002 (dm+d codes) | Pregabalin 225mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 4215911000001106 (dm+d codes) | Rivotril 1mg/1ml concentrate for solution for injection ampoules (Roche Products Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4217711000001103 (dm+d codes) | Clonazepam 1mg/1ml solution for injection ampoules and diluent | Anti-seizure medication CPRD gold (all) primary care |
| 4249911000001100 (dm+d codes) | Sodium valproate 500mg modified-release tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 425011000001109 (dm+d codes) | Carbamazepine 400mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 434211000001102 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 43505001000027104 (dm+d codes) | Diazepam 10mg Suppository (Sinclair IS Pharma Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 4351111000001108 (dm+d codes) | Epilim Intravenous 400mg powder and solvent for solution for injection vials (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 4358911000001102 (dm+d codes) | Epanutin Ready-Mixed Parenteral 250mg/5ml solution for injection ampoules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4370711000001104 (dm+d codes) | Diamox Sodium Parenteral 500mg powder for solution for injection vials (Advanz Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 4377611000001107 (dm+d codes) | Acetazolamide 500mg powder for solution for injection vials | Anti-seizure medication CPRD gold (all) primary care |
| 4390811000001104 (dm+d codes) | Pro-Epanutin 750mg/10ml concentrate for solution for injection vials (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 441464008 (dm+d codes) | Lacosamide 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 441572007 (dm+d codes) | Rufinamide 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 441726005 (dm+d codes) | Everolimus 5mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 441822003 (dm+d codes) | Rufinamide 400mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 441836008 (dm+d codes) | Lacosamide 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 441947000 (dm+d codes) | Lacosamide 150mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 441953000 (dm+d codes) | Everolimus 10mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 442041004 (dm+d codes) | Lacosamide 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 443711000001108 (dm+d codes) | Tegretol 200mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 446482007 (dm+d codes) | Everolimus 500microgram tablets | Anti-seizure medication CPRD gold (all) primary care |
| 447132004 (dm+d codes) | Everolimus 250microgram tablets | Anti-seizure medication CPRD gold (all) primary care |
| 448711000001102 (dm+d codes) | Epilim 500 gastro-resistant tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 451611000001101 (dm+d codes) | Phenobarbital 15mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4571411000001103 (dm+d codes) | Carbamazepine 200mg modified-release tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4571611000001100 (dm+d codes) | Carbamazepine 400mg modified-release tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 459211000001102 (dm+d codes) | Neurontin 100mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 462911000001106 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4765911000001103 (dm+d codes) | Epival CR 300mg tablets (Gerot Lannach UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 4766111000001107 (dm+d codes) | Epival CR 500mg tablets (Gerot Lannach UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 48865001000027103 (dm+d codes) | Luminal 30mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 48875001000027105 (dm+d codes) | Luminal 60mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 48885001000027100 (dm+d codes) | Luminal 15mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 489711000001100 (dm+d codes) | Epilim Chrono 200 tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 49325001000027106 (dm+d codes) | Prominal 30mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 49335001000027108 (dm+d codes) | Prominal 60mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 49345001000027109 (dm+d codes) | Prominal 200mg Tablet (Sanofi-Synthelabo Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 502645001000027104 (dm+d codes) | Epistatus 10mg/1ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 502685001000027108 (dm+d codes) | Epistatus 2.5mg/0.25ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 502705001000027103 (dm+d codes) | Midazolam 5mg/0.5ml oromucosal solution pre-filled syringes | Anti-seizure medication CPRD gold (all) primary care |
| 502725001000027105 (dm+d codes) | Epistatus 5mg/0.5ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 502765001000027102 (dm+d codes) | Epistatus 7.5mg/0.75ml oromucosal solution pre-filled oral syringes (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 502795001000027100 (dm+d codes) | Epistatus 50mg/5ml oromucosal solution bottle (Veriton Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 504111000001107 (dm+d codes) | Carbamazepine 100mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 504711000001108 (dm+d codes) | Orlept 200mg gastro-resistant tablets (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 506411000001105 (dm+d codes) | Carbamazepine 100mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5083111000001106 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules (hameln pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 511611000001103 (dm+d codes) | Neurontin 600mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 514411000001104 (dm+d codes) | Carbamazepine 100mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 51755001000027109 (dm+d codes) | Valproate sodium 200mg Gastro-resistant tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 51765001000027100 (dm+d codes) | Valproate sodium 500mg Gastro-resistant tablet (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 520611000001103 (dm+d codes) | Carbamazepine 200mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5240511000001109 (dm+d codes) | Potassium bromide mixture | Anti-seizure medication CPRD gold (all) primary care |
| 53485001000027100 (dm+d codes) | Diamox 250mg Tablet (Wyeth Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 53495001000027101 (dm+d codes) | Diamox 500mg/vial Sodium injection (Wyeth Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 5367711000001103 (dm+d codes) | Frisium 10mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 5379611000001106 (dm+d codes) | Lamictal 200mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 5381611000001101 (dm+d codes) | Lamictal 25mg dispersible tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 5398011000001101 (dm+d codes) | Neurontin 100mg capsules (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 5418811000001102 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Waymade Healthcare Plc) | Anti-seizure medication CPRD gold (all) primary care |
| 5471411000001101 (dm+d codes) | Gabapentin 100mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5472411000001106 (dm+d codes) | Gabapentin 300mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5473811000001100 (dm+d codes) | Gabapentin 400mg capsules (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5474211000001103 (dm+d codes) | Gabapentin 600mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5475211000001102 (dm+d codes) | Gabapentin 800mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 548211000001104 (dm+d codes) | Phenobarbital 15mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 552511000001100 (dm+d codes) | Epilim 100mg crushable tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 5547911000001106 (dm+d codes) | Neurontin 300mg capsules (Dowelhurst Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 55611000001105 (dm+d codes) | Phenytoin sodium 100mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5568111000001101 (dm+d codes) | Gabapentin 100mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5569411000001103 (dm+d codes) | Gabapentin 300mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5569611000001100 (dm+d codes) | Gabapentin 400mg capsules (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5570311000001108 (dm+d codes) | Gabapentin 600mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5586611000001106 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Dowelhurst Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 5629911000001107 (dm+d codes) | Gabapentin 600mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 563311000001108 (dm+d codes) | Phenobarbital 60mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 566911000001103 (dm+d codes) | Phenobarbital 60mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 56811000001101 (dm+d codes) | Phenobarbital 15mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 569811000001102 (dm+d codes) | Phenobarbital 15mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 591311000001109 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 603811000001108 (dm+d codes) | Diazepam 5mg RecTubes (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 60435001000027108 (dm+d codes) | Paraldehyde intravenous injection | Anti-seizure medication CPRD gold (all) primary care |
| 60445001000027109 (dm+d codes) | Paraldehyde rectal solution | Anti-seizure medication CPRD gold (all) primary care |
| 60595001000027105 (dm+d codes) | Phenobarbital 50mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 60705001000027108 (dm+d codes) | Sodium valproate 500mg Gastro-resistant tablet (C P Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 61035001000027109 (dm+d codes) | Phenytoin 90mg/5ml Oral suspension sugar free (Rosemont Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 612111000001105 (dm+d codes) | Carbamazepine 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 624411000001104 (dm+d codes) | Phenytoin sodium 100mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 636111000001104 (dm+d codes) | Diazepam 5mg/2.5ml rectal solution tube (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 640811000001105 (dm+d codes) | Carbagen SR 400mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 658111000001104 (dm+d codes) | Teril Retard 400mg tablets (Taro Pharmaceuticals (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 66045001000027108 (dm+d codes) | Sodium valproate 200mg/5ml Oral solution (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 662611000001103 (dm+d codes) | Tegretol Prolonged Release 400mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 680511000001100 (dm+d codes) | Tegretol 100mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 687511000001101 (dm+d codes) | Diazepam 10mg/2ml solution for injection ampoules (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 702711000001104 (dm+d codes) | Tegretol 400mg tablets (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 703729002 (dm+d codes) | Perampanel 2mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 703730007 (dm+d codes) | Perampanel 4mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 703732004 (dm+d codes) | Perampanel 6mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 703733009 (dm+d codes) | Perampanel 8mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 703734003 (dm+d codes) | Perampanel 10mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 703735002 (dm+d codes) | Perampanel 12mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 704477007 (dm+d codes) | Retigabine 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 704478002 (dm+d codes) | Retigabine 100mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 704479005 (dm+d codes) | Retigabine 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 704480008 (dm+d codes) | Retigabine 300mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 704481007 (dm+d codes) | Retigabine 400mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 707111000001103 (dm+d codes) | Diazepam 5mg/2.5ml rectal solution tube (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 71005001000027101 (dm+d codes) | Pentran 50mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 71015001000027104 (dm+d codes) | Pentran 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 725911000001101 (dm+d codes) | Epanutin 100mg capsules (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 731411000001109 (dm+d codes) | Sodium valproate 200mg/5ml oral solution sugar free (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7315411000001103 (dm+d codes) | Trileptal 60mg/ml oral suspension (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 739111000001100 (dm+d codes) | Epilim Chrono 500 tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 755011000001104 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 75811000001106 (dm+d codes) | Diazepam 10mg/2.5ml rectal solution tube (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7585001000027105 (dm+d codes) | Diamox sustets 500 500mg Sustets (Wyeth Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 760111000001100 (dm+d codes) | Tegretol 100mg/5ml liquid (Novartis Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 760511000001109 (dm+d codes) | Epimaz 400mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7655011000001106 (dm+d codes) | Rivotril 2.5mg/1ml drops (Imported (Switzerland)) | Anti-seizure medication CPRD gold (all) primary care |
| 7662511000001100 (dm+d codes) | Clonazepam 2.5mg/ml drops sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 767111000001104 (dm+d codes) | Zarontin 250mg capsules (Pfizer Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 77085001000027104 (dm+d codes) | Stesolid 5mg/ml Injection (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7716411000001106 (dm+d codes) | Ospolot 50mg tablets (Imported (Germany)) | Anti-seizure medication CPRD gold (all) primary care |
| 7721511000001108 (dm+d codes) | Sultiame 200mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 7721611000001107 (dm+d codes) | Sultiame 50mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 781611000001101 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 782711000001103 (dm+d codes) | Zarontin 250mg/5ml syrup (Essential Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7843411000001108 (dm+d codes) | Acetazolamide 250mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7847211000001100 (dm+d codes) | Gabapentin 100mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7847411000001101 (dm+d codes) | Gabapentin 300mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7847611000001103 (dm+d codes) | Gabapentin 400mg capsules (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7865001000027106 (dm+d codes) | Carbamazepine 100mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7875001000027104 (dm+d codes) | Carbamazepine 200mg Tablet (Berk Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7889411000001104 (dm+d codes) | Lyrica 25mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7890211000001109 (dm+d codes) | Lyrica 50mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7890511000001107 (dm+d codes) | Lyrica 75mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7890811000001105 (dm+d codes) | Lyrica 100mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7891211000001103 (dm+d codes) | Lyrica 150mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7891611000001101 (dm+d codes) | Lyrica 200mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 7892111000001104 (dm+d codes) | Lyrica 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 789911000001106 (dm+d codes) | Epilim Chrono 300 tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 801011000001107 (dm+d codes) | Diamox 250mg tablets (Advanz Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 8171111000001104 (dm+d codes) | Keppra 750mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8176611000001100 (dm+d codes) | Keppra 100mg/ml oral solution (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 82011000001104 (dm+d codes) | Stesolid 5mg rectal tube (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 823811000001105 (dm+d codes) | Topamax 100mg tablets (Janssen-Cilag Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8269211000001104 (dm+d codes) | Acetazolamide 100mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8269311000001107 (dm+d codes) | Acetazolamide 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8269411000001100 (dm+d codes) | Acetazolamide 125mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8269511000001101 (dm+d codes) | Acetazolamide 125mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8270711000001109 (dm+d codes) | Acetazolamide 250mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8270911000001106 (dm+d codes) | Acetazolamide 250mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8271511000001106 (dm+d codes) | Acetazolamide 500mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8271611000001105 (dm+d codes) | Acetazolamide 62.5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8285511000001102 (dm+d codes) | Levetiracetam 100mg/ml oral solution sugar free | Anti-seizure medication CPRD gold (all) primary care |
| 8354711000001108 (dm+d codes) | Carbamazepine 40mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8354911000001105 (dm+d codes) | Carbamazepine 500mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8360711000001105 (dm+d codes) | Clobazam 10mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8360811000001102 (dm+d codes) | Clobazam 10mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8361111000001103 (dm+d codes) | Clobazam 1mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8361211000001109 (dm+d codes) | Clobazam 2.5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8361311000001101 (dm+d codes) | Clobazam 2.5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8366311000001109 (dm+d codes) | Clobazam 20mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8366411000001102 (dm+d codes) | Clobazam 25mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8366611000001104 (dm+d codes) | Clobazam 25mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8366811000001100 (dm+d codes) | Clobazam 2mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8367111000001105 (dm+d codes) | Clobazam 3.5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8367211000001104 (dm+d codes) | Clobazam 4mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8367411000001100 (dm+d codes) | Clobazam 4mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8368611000001103 (dm+d codes) | Clobazam 5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8368711000001107 (dm+d codes) | Clobazam 5mg/5ml oral suspension (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8368811000001104 (dm+d codes) | Clobazam 5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8382911000001108 (dm+d codes) | Clonazepam 10mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 839211000001109 (dm+d codes) | Keppra 500mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8395211000001105 (dm+d codes) | Clonazepam 1mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8395311000001102 (dm+d codes) | Clonazepam 2.5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8395711000001103 (dm+d codes) | Clonazepam 250micrograms/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8395811000001106 (dm+d codes) | Clonazepam 250micrograms/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8395911000001101 (dm+d codes) | Clonazepam 2mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8396011000001109 (dm+d codes) | Clonazepam 2mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8397111000001108 (dm+d codes) | Clonazepam 500micrograms/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8397211000001102 (dm+d codes) | Clonazepam 500micrograms/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8397311000001105 (dm+d codes) | Clonazepam 5mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8397411000001103 (dm+d codes) | Clonazepam 5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 84011000001105 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8520111000001104 (dm+d codes) | Gabapentin 100mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8520211000001105 (dm+d codes) | Gabapentin 100mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8520411000001109 (dm+d codes) | Gabapentin 250mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8520511000001108 (dm+d codes) | Gabapentin 300mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8523111000001106 (dm+d codes) | Gabapentin 300mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8523211000001100 (dm+d codes) | Gabapentin 450mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8523311000001108 (dm+d codes) | Gabapentin 450mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8523411000001101 (dm+d codes) | Gabapentin 50mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 8523511000001102 (dm+d codes) | Gabapentin 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8582611000001104 (dm+d codes) | Lamotrigine 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8611000001108 (dm+d codes) | Sodium valproate 500mg gastro-resistant tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 87155001000027103 (dm+d codes) | Phenobarbital 100mg tablet | Anti-seizure medication CPRD gold (all) primary care |
| 872211000001104 (dm+d codes) | Orlept SF 200mg/5ml liquid (Wockhardt UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8723811000001103 (dm+d codes) | Topiramate 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8723911000001108 (dm+d codes) | Topiramate 25mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8768411000001102 (dm+d codes) | Primidone 50mg capsules (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 87711000001100 (dm+d codes) | Mysoline 250mg tablets (SERB) | Anti-seizure medication CPRD gold (all) primary care |
| 87855001000027106 (dm+d codes) | Acetazolamide 40mg/ml Oral solution (Martindale Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8789511000001106 (dm+d codes) | Phenobarbital 50mg/5ml oral solution (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8790011000001107 (dm+d codes) | Phenobarbital 50mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8792211000001101 (dm+d codes) | Clobazam 2.5mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 8800311000001105 (dm+d codes) | Primidone 50mg capsules | Anti-seizure medication CPRD gold (all) primary care |
| 8800811000001101 (dm+d codes) | Phenobarbital 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8800911000001106 (dm+d codes) | Phenobarbital 50mg/5ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 880211000001107 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8808311000001107 (dm+d codes) | Primidone 25mg/5ml oral suspension (Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8808911000001108 (dm+d codes) | Primidone 50mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8809511000001107 (dm+d codes) | Primidone 62.5mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8814411000001107 (dm+d codes) | Phenytoin 90mg/5ml oral suspension (Drug Tariff Special Order) | Anti-seizure medication CPRD gold (all) primary care |
| 8817911000001105 (dm+d codes) | Phenytoin 90mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8818111000001108 (dm+d codes) | Primidone 25mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8818211000001102 (dm+d codes) | Primidone 50mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8818311000001105 (dm+d codes) | Primidone 62.5mg/5ml oral suspension | Anti-seizure medication CPRD gold (all) primary care |
| 8818511000001104 (dm+d codes) | Sodium valproate 300mg suppositories | Anti-seizure medication CPRD gold (all) primary care |
| 889311000001108 (dm+d codes) | Epilim 200 gastro-resistant tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 89011000001106 (dm+d codes) | Carbamazepine 400mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8916811000001109 (dm+d codes) | Gabapentin 100mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 8917211000001105 (dm+d codes) | Gabapentin 300mg capsules (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 892411000001106 (dm+d codes) | Epilim 200mg/5ml syrup (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 89505001000027108 (dm+d codes) | Carbamazepine 200mg Modified-release tablet (Lagap) | Anti-seizure medication CPRD gold (all) primary care |
| 89515001000027105 (dm+d codes) | Carbamazepine 400mg Modified-release tablet (Lagap) | Anti-seizure medication CPRD gold (all) primary care |
| 896911000001104 (dm+d codes) | Phenobarbital 30mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 91175001000027104 (dm+d codes) | Paraldehyde intramuscular injection | Anti-seizure medication CPRD gold (all) primary care |
| 91195001000027108 (dm+d codes) | Phenobarbital sodium 30mg tablet | Anti-seizure medication CPRD gold (all) primary care |
| 91205001000027108 (dm+d codes) | Phenobarbital sodium 60mg tablet | Anti-seizure medication CPRD gold (all) primary care |
| 91511000001103 (dm+d codes) | Carbamazepine 200mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 918411000001102 (dm+d codes) | Phenobarbital 30mg tablets (Accord Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 926511000001105 (dm+d codes) | Sodium valproate 200mg gastro-resistant tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 929411000001104 (dm+d codes) | Keppra 250mg tablets (UCB Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9298111000001103 (dm+d codes) | Gabapentin 100mg capsules (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9298311000001101 (dm+d codes) | Gabapentin 300mg capsules (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 929911000001107 (dm+d codes) | Frisium 10mg tablets (Sanofi) | Anti-seizure medication CPRD gold (all) primary care |
| 9303511000001105 (dm+d codes) | Zonegran 25mg capsules (Advanz Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 9303911000001103 (dm+d codes) | Zonegran 50mg capsules (Advanz Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 9304111000001104 (dm+d codes) | Zonegran 100mg capsules (Advanz Pharma) | Anti-seizure medication CPRD gold (all) primary care |
| 9308411000001100 (dm+d codes) | Gabapentin 300mg capsules (Sandoz Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9326611000001105 (dm+d codes) | Lamotrigine 25mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9326811000001109 (dm+d codes) | Lamotrigine 50mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9327011000001100 (dm+d codes) | Lamotrigine 100mg tablets (Viatris UK Healthcare Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9327411000001109 (dm+d codes) | Lamotrigine 25mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9327611000001107 (dm+d codes) | Lamotrigine 50mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9327811000001106 (dm+d codes) | Lamotrigine 100mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9328011000001104 (dm+d codes) | Lamotrigine 200mg tablets (Actavis UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9329311000001107 (dm+d codes) | Lamotrigine 25mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9329511000001101 (dm+d codes) | Lamotrigine 50mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9329711000001106 (dm+d codes) | Lamotrigine 100mg tablets (Kent Pharma (UK) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9360611000001104 (dm+d codes) | Lamotrigine 50mg tablets (IVAX Pharmaceuticals UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 93775001000027101 (dm+d codes) | Acetazolamide powder | Anti-seizure medication CPRD gold (all) primary care |
| 9378311000001100 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (PLIVA Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 93785001000027106 (dm+d codes) | Acetazolamide 40mg/ml oral solution | Anti-seizure medication CPRD gold (all) primary care |
| 9378511000001106 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (PLIVA Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9378711000001101 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (PLIVA Pharma Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 93865001000027106 (dm+d codes) | Sodium valproate 200mg Tablet (Sterwin Medicines) | Anti-seizure medication CPRD gold (all) primary care |
| 93875001000027104 (dm+d codes) | Sodium valproate 200mg/5ml Oral solution (Sterwin Medicines) | Anti-seizure medication CPRD gold (all) primary care |
| 93885001000027109 (dm+d codes) | Sodium valproate 500mg Tablet (Sterwin Medicines) | Anti-seizure medication CPRD gold (all) primary care |
| 93895001000027108 (dm+d codes) | Diamox Powder (Wyeth Pharmaceuticals) | Anti-seizure medication CPRD gold (all) primary care |
| 9450711000001106 (dm+d codes) | Lamotrigine 25mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9450911000001108 (dm+d codes) | Lamotrigine 50mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9451211000001105 (dm+d codes) | Lamotrigine 100mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9451411000001109 (dm+d codes) | Lamotrigine 200mg tablets (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9451811000001106 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9452011000001108 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (Teva UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9454111000001101 (dm+d codes) | Lamotrigine 25mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9454511000001105 (dm+d codes) | Lamotrigine 50mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9454711000001100 (dm+d codes) | Lamotrigine 100mg tablets (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9455711000001101 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9456011000001107 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (Alliance Healthcare (Distribution) Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9458411000001102 (dm+d codes) | Lamotrigine 5mg dispersible tablets sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9458611000001104 (dm+d codes) | Lamotrigine 25mg dispersible tablets sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9458811000001100 (dm+d codes) | Lamotrigine 100mg dispersible tablets sugar free (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9459011000001101 (dm+d codes) | Lamotrigine 25mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9459411000001105 (dm+d codes) | Lamotrigine 50mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9460011000001100 (dm+d codes) | Lamotrigine 100mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9460211000001105 (dm+d codes) | Lamotrigine 200mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 95445001000027100 (dm+d codes) | Beclamide 500mg tablets | Anti-seizure medication CPRD gold (all) primary care |
| 9557711000001101 (dm+d codes) | Gabapentin 100mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9557911000001104 (dm+d codes) | Gabapentin 300mg capsules (Zentiva Pharma UK Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9703811000001109 (dm+d codes) | Acetazolamide 250mg tablets (A A H Pharmaceuticals Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9735001000027108 (dm+d codes) | Emeside 250mg Capsule (Laboratories For Applied Biology Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 9745001000027109 (dm+d codes) | Emeside 250mg/5ml Oral solution (Laboratories For Applied Biology Ltd) | Anti-seizure medication CPRD gold (all) primary care |
| 10205841000033114 (PROD codes) | Rewisca 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10205941000033118 (PROD codes) | Rewisca 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10206041000033111 (PROD codes) | Rewisca 75mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10206141000033110 (PROD codes) | Rewisca 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10206241000033115 (PROD codes) | Rewisca 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10206341000033113 (PROD codes) | Rewisca 200mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10206441000033119 (PROD codes) | Rewisca 225mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10206541000033118 (PROD codes) | Rewisca 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220341000033117 (PROD codes) | Lecaent 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220441000033111 (PROD codes) | Lecaent 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220541000033112 (PROD codes) | Lecaent 75mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220641000033113 (PROD codes) | Lecaent 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220741000033116 (PROD codes) | Lecaent 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220841000033114 (PROD codes) | Lecaent 200mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10220941000033118 (PROD codes) | Lecaent 225mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10221041000033111 (PROD codes) | Lecaent 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10229041000033112 (PROD codes) | Levetiracetam 500mg/5ml solution for infusion ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 10229241000033116 (PROD codes) | Desitrend 500mg/5ml concentrate for solution for infusion ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 10253941000033110 (PROD codes) | Alzain 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254041000033112 (PROD codes) | Alzain 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254141000033111 (PROD codes) | Alzain 75mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254241000033116 (PROD codes) | Alzain 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254341000033114 (PROD codes) | Alzain 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254441000033115 (PROD codes) | Alzain 200mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254541000033119 (PROD codes) | Alzain 225mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10254641000033118 (PROD codes) | Alzain 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10334241000033111 (PROD codes) | Everolimus 500microgram tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 10334441000033112 (PROD codes) | Everolimus 250microgram tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 10334541000033113 (PROD codes) | Everolimus 750microgram tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 10334641000033114 (PROD codes) | Certican 0.25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 10334741000033117 (PROD codes) | Certican 0.5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 10334841000033110 (PROD codes) | Certican 0.75mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1034941000033113 (PROD codes) | Paraldehyde 100% solution for injection 5ml ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 10388041000033115 (PROD codes) | Perizam 1mg/ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 10388141000033116 (PROD codes) | Perizam 2mg/ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 1068641000033115 (PROD codes) | Phenytoin sodium 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1068841000033119 (PROD codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1068941000033110 (PROD codes) | Phenytoin sodium 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1069041000033118 (PROD codes) | Phenytoin sodium 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 10702041000033117 (PROD codes) | Phenobarbital 30mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 10702141000033118 (PROD codes) | Phenobarbital 60mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 1074441000033118 (PROD codes) | Phenytoin sodium 250mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 1074641000033116 (PROD codes) | Phenytoin 50mg chewable tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1082141000033114 (PROD codes) | Phenytoin sodium 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1082541000033117 (PROD codes) | Phenytoin sodium 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1089441000033113 (PROD codes) | Piracetam 333.3mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 1092041000033114 (PROD codes) | Piracetam 1.2g tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1092141000033113 (PROD codes) | Piracetam 800mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11026841000033112 (PROD codes) | Brivaracetam 50mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 11027241000033111 (PROD codes) | Briviact 10mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 11028241000033112 (PROD codes) | Brivaracetam 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11028441000033113 (PROD codes) | Brivaracetam 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11028541000033114 (PROD codes) | Brivaracetam 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11028641000033110 (PROD codes) | Brivaracetam 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11028741000033118 (PROD codes) | Brivaracetam 75mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11028841000033111 (PROD codes) | Briviact 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11028941000033115 (PROD codes) | Briviact 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11029041000033112 (PROD codes) | Briviact 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11029141000033111 (PROD codes) | Briviact 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11029241000033116 (PROD codes) | Briviact 75mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11141000033118 (PROD codes) | Acetazolamide 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1129241000033113 (PROD codes) | Primidone 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 1139341000033117 (PROD codes) | Primidone 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11559841000033118 (PROD codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 11559941000033114 (PROD codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 11560041000033112 (PROD codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 11560141000033111 (PROD codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 11616241000033110 (PROD codes) | Clonazepam 1mg/1ml solution for injection ampoules and diluent | Anti-seizure medication CPRD aurum (all) primary care |
| 11616341000033117 (PROD codes) | Rivotril 1mg/1ml concentrate for solution for injection ampoules and diluent | Anti-seizure medication CPRD aurum (all) primary care |
| 11717841000033118 (PROD codes) | Phenytoin sodium 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11724841000033116 (PROD codes) | Valproic acid 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 1177241000033117 (PROD codes) | Rivotril 500microgram tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1177341000033110 (PROD codes) | Rivotril 2mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 11821741000033110 (PROD codes) | Axalid 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11821841000033117 (PROD codes) | Axalid 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11821941000033113 (PROD codes) | Axalid 75mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11822041000033119 (PROD codes) | Axalid 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11822141000033115 (PROD codes) | Axalid 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11822241000033110 (PROD codes) | Axalid 200mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11822341000033117 (PROD codes) | Axalid 225mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 11822441000033111 (PROD codes) | Axalid 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 12188741000033115 (PROD codes) | Everolimus 2mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12188941000033117 (PROD codes) | Everolimus 3mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12189141000033113 (PROD codes) | Everolimus 5mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12202541000033114 (PROD codes) | Zacco 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 12202641000033110 (PROD codes) | Zacco 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 12315241000033112 (PROD codes) | Midazolam 10mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12341141000033112 (PROD codes) | Eslicarbazepine 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 12341241000033117 (PROD codes) | Zebinix 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1252741000033112 (PROD codes) | Sabril 500mg oral powder sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 12578741000033117 (PROD codes) | Depakin 200mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 1258841000033116 (PROD codes) | Sabril 500mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 12602641000033112 (PROD codes) | Phenobarbital 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 12684541000033116 (PROD codes) | Ethosuximide 250mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12881541000033111 (PROD codes) | Eslicarbazepine 50mg/1ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12881641000033112 (PROD codes) | Zebinix 50mg/1ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 12903541000033116 (PROD codes) | Mesuximide 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 12910641000033110 (PROD codes) | Topiramate 50mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12910741000033118 (PROD codes) | Topiramate 100mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12999441000033116 (PROD codes) | Perampanel 500micrograms/ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 12999541000033115 (PROD codes) | Fycompa 0.5mg/ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 13091441000033117 (PROD codes) | Dilantin Infatabs 50mg chewable tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13149541000033117 (PROD codes) | Belvo 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13149641000033116 (PROD codes) | Belvo 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13149741000033113 (PROD codes) | Midazolam 10mg/5ml oral solution unit dose ampoules sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 13344341000033118 (PROD codes) | Pregabalin 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13344541000033113 (PROD codes) | Pregabalin 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13344641000033114 (PROD codes) | Pregabalin 75mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13344741000033117 (PROD codes) | Pregabalin 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13344841000033110 (PROD codes) | Pregabalin 150mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13344941000033119 (PROD codes) | Pregabalin 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13345041000033119 (PROD codes) | Pregabalin 225mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13345141000033115 (PROD codes) | Pregabalin 300mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13348941000033113 (PROD codes) | Syonell 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13349541000033114 (PROD codes) | Syonell 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13352641000033119 (PROD codes) | Phenobarbital 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13352741000033111 (PROD codes) | Cannabidiol 100mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 13352941000033114 (PROD codes) | Epidyolex 100mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 13420041000033119 (PROD codes) | Midazolam 50mg/50ml solution for infusion pre-filled syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 13446741000033116 (PROD codes) | Vigabatrin 100mg soluble tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 13446841000033114 (PROD codes) | Vigabatrin 500mg soluble tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 1358241000033111 (PROD codes) | Sodium valproate 400mg powder and solvent for solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 1359341000033113 (PROD codes) | Sodium valproate 200mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1359441000033119 (PROD codes) | Sodium valproate 300mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1359541000033118 (PROD codes) | Sodium valproate 500mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1361241000033114 (PROD codes) | Sodium valproate 200mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 1363641000033113 (PROD codes) | Sodium valproate 200mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 1364941000033115 (PROD codes) | Sodium valproate 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1365041000033115 (PROD codes) | Sodium valproate 200mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1365141000033116 (PROD codes) | Sodium valproate 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13722141000033112 (PROD codes) | Dyzantil 200mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13722241000033117 (PROD codes) | Dyzantil 300mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13722341000033110 (PROD codes) | Dyzantil 500mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13752941000033110 (PROD codes) | Zonisamide 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 13753041000033117 (PROD codes) | Desizon 20mg/ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 13764841000033115 (PROD codes) | Phenobarbital 30mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 13765041000033111 (PROD codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 13830041000033111 (PROD codes) | Midazolam 5mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 1383241000033113 (PROD codes) | Stesolid 10mg rectal tube | Anti-seizure medication CPRD aurum (all) primary care |
| 1383341000033115 (PROD codes) | Stesolid 5mg rectal tube | Anti-seizure medication CPRD aurum (all) primary care |
| 13910341000033111 (PROD codes) | Fenfluramine 2.2mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 13914541000033113 (PROD codes) | Epesri 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 13934341000033111 (PROD codes) | Cenobamate 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13934441000033117 (PROD codes) | Cenobamate 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13934541000033116 (PROD codes) | Cenobamate 150mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13934641000033115 (PROD codes) | Cenobamate 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13934741000033112 (PROD codes) | Ontozry 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13934841000033119 (PROD codes) | Ontozry 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 13935041000033110 (PROD codes) | Ontozry 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 14032541000033118 (PROD codes) | Clonazepam 1mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1415041000033114 (PROD codes) | Tegretol 100mg Chewtabs | Anti-seizure medication CPRD aurum (all) primary care |
| 1415141000033113 (PROD codes) | Tegretol 200mg Chewtabs | Anti-seizure medication CPRD aurum (all) primary care |
| 1423941000033119 (PROD codes) | Tegretol 125mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 1424041000033117 (PROD codes) | Tegretol 250mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 1424241000033113 (PROD codes) | Tegretol 100mg/5ml liquid | Anti-seizure medication CPRD aurum (all) primary care |
| 1425841000033111 (PROD codes) | Tegretol 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1425941000033115 (PROD codes) | Tegretol 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1426041000033113 (PROD codes) | Tegretol 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1428841000033119 (PROD codes) | Tegretol Prolonged Release 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1428941000033110 (PROD codes) | Tegretol Prolonged Release 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1450441000033115 (PROD codes) | Topamax 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1450541000033119 (PROD codes) | Topamax 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1450641000033118 (PROD codes) | Topamax 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1451441000033112 (PROD codes) | Topamax 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1451541000033113 (PROD codes) | Topiramate 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1451641000033114 (PROD codes) | Topiramate 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1451741000033117 (PROD codes) | Topiramate 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1451841000033110 (PROD codes) | Topiramate 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1500041000033112 (PROD codes) | Valproic acid 150mg gastro-resistant capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1500141000033111 (PROD codes) | Valproic acid 300mg gastro-resistant capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1500241000033116 (PROD codes) | Valproic acid 500mg gastro-resistant capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1502941000033114 (PROD codes) | Valclair 10mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 1521941000033110 (PROD codes) | Vigabatrin 500mg oral powder sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 1522741000033118 (PROD codes) | Vigabatrin 500mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1548241000033112 (PROD codes) | Zarontin 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1550041000033116 (PROD codes) | Zarontin 250mg/5ml syrup | Anti-seizure medication CPRD aurum (all) primary care |
| 1611841000033119 (PROD codes) | Gabitril 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1611941000033110 (PROD codes) | Gabitril 15mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1612041000033116 (PROD codes) | Gabitril 5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1701341000033119 (PROD codes) | Tiagabine 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1701441000033113 (PROD codes) | Tiagabine 15mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1701541000033114 (PROD codes) | Tiagabine 5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1729541000033118 (PROD codes) | Epimaz 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1729641000033117 (PROD codes) | Epimaz 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1729741000033114 (PROD codes) | Epimaz 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1747541000033114 (PROD codes) | Orlept SF 200mg/5ml liquid | Anti-seizure medication CPRD aurum (all) primary care |
| 1747641000033110 (PROD codes) | Orlept 200mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1747741000033118 (PROD codes) | Orlept 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 1767341000033110 (PROD codes) | Fosphenytoin 750mg/10ml solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 1767441000033116 (PROD codes) | Pro-Epanutin 750mg/10ml concentrate for solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 178741000033110 (PROD codes) | Carbamazepine 100mg chewable tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 178841000033117 (PROD codes) | Carbamazepine 200mg chewable tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 1847941000033118 (PROD codes) | Topamax 15mg sprinkle capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1848041000033115 (PROD codes) | Topamax 25mg sprinkle capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 1870841000033112 (PROD codes) | Phenytoin 30mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 198141000033115 (PROD codes) | Carbamazepine 100mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 2033041000033110 (PROD codes) | Oxcarbazepine 150mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2033141000033114 (PROD codes) | Oxcarbazepine 300mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2033241000033119 (PROD codes) | Oxcarbazepine 600mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2033341000033112 (PROD codes) | Trileptal 150mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2033441000033118 (PROD codes) | Trileptal 300mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2033541000033117 (PROD codes) | Trileptal 600mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2056341000033116 (PROD codes) | Midazolam 50mg/50ml solution for infusion vials | Anti-seizure medication CPRD aurum (all) primary care |
| 207541000033111 (PROD codes) | Carbamazepine 125mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 207641000033112 (PROD codes) | Carbamazepine 250mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 2093841000033113 (PROD codes) | Potassium bromide powder | Anti-seizure medication CPRD aurum (all) primary care |
| 212541000033112 (PROD codes) | Carbamazepine 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 212641000033113 (PROD codes) | Carbamazepine 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 212741000033116 (PROD codes) | Carbamazepine 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2145941000033118 (PROD codes) | Gabapentin 600mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2146041000033111 (PROD codes) | Gabapentin 800mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2146141000033110 (PROD codes) | Neurontin 600mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2146241000033115 (PROD codes) | Neurontin 800mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2212941000033119 (PROD codes) | Levetiracetam 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2213041000033112 (PROD codes) | Levetiracetam 500mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2213141000033111 (PROD codes) | Levetiracetam 1g tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2213241000033116 (PROD codes) | Keppra 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2213341000033114 (PROD codes) | Keppra 500mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2213441000033115 (PROD codes) | Keppra 1g tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2217641000033111 (PROD codes) | Topamax 50mg sprinkle capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 2266041000033115 (PROD codes) | Carbamazepine 200mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2266141000033116 (PROD codes) | Carbamazepine 400mg modified-release tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2271441000033112 (PROD codes) | Depakote 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2271541000033113 (PROD codes) | Depakote 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2584441000033110 (PROD codes) | Lamotrigine 2mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 2584541000033111 (PROD codes) | Lamictal 2mg dispersible tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2601041000033112 (PROD codes) | Clonazepam 2.5mg/ml drops sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 2601141000033111 (PROD codes) | Rivotril 2.5mg/1ml drops | Anti-seizure medication CPRD aurum (all) primary care |
| 262841000033110 (PROD codes) | Clobazam 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2640041000033113 (PROD codes) | Clonazepam 125micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 2667941000033119 (PROD codes) | Clonazepam 625micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 2668041000033116 (PROD codes) | Teril Retard 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2668141000033117 (PROD codes) | Teril Retard 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2711041000033119 (PROD codes) | Clobazam 5mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 2711241000033110 (PROD codes) | Valproic acid 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2711341000033117 (PROD codes) | Valproic acid 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2719441000033110 (PROD codes) | Clonazepam 500micrograms/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 2722341000033116 (PROD codes) | Clonazepam 500micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 2730441000033114 (PROD codes) | Arbil MR 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2730541000033110 (PROD codes) | Arbil MR 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2752741000033119 (PROD codes) | Clonazepam 2mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 2758641000033114 (PROD codes) | Primidone 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 2796241000033118 (PROD codes) | Gabapentin 250mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 2796341000033111 (PROD codes) | Neurontin 250mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 2799141000033115 (PROD codes) | Epival CR 500mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2799241000033110 (PROD codes) | Epival CR 300mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2839041000033113 (PROD codes) | Oxcarbazepine 60mg/ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 2839141000033112 (PROD codes) | Trileptal 60mg/ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 286741000033118 (PROD codes) | Clonazepam 500microgram tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 286841000033111 (PROD codes) | Clonazepam 2mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2928641000033118 (PROD codes) | Epimaz Retard 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2928741000033110 (PROD codes) | Epimaz Retard 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2929341000033119 (PROD codes) | Carbagen SR 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2929441000033113 (PROD codes) | Carbagen SR 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 2973141000033118 (PROD codes) | Topiramate 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 3033041000033117 (PROD codes) | Diazepam 10mg/2ml emulsion for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 3033141000033118 (PROD codes) | Diazepam 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 3076141000033111 (PROD codes) | Topiramate 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 3085341000033114 (PROD codes) | Clomethiazole 192mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3096941000033115 (PROD codes) | Mesuximide 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3102641000033118 (PROD codes) | Phenobarbital 15mg/5ml elixir | Anti-seizure medication CPRD aurum (all) primary care |
| 3102741000033110 (PROD codes) | Phenobarbital 200mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 3103141000033116 (PROD codes) | Phenobarbital 15mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 3103241000033111 (PROD codes) | Phenobarbital 30mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 3103341000033118 (PROD codes) | Phenobarbital 60mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 3135541000033116 (PROD codes) | Clonazepam 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 3152941000033118 (PROD codes) | Sodium valproate 300mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 3153041000033111 (PROD codes) | Sodium valproate 100mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 3153341000033113 (PROD codes) | Pregabalin 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3153441000033119 (PROD codes) | Pregabalin 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3153541000033118 (PROD codes) | Pregabalin 75mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3153641000033117 (PROD codes) | Pregabalin 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3153741000033114 (PROD codes) | Pregabalin 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3153841000033116 (PROD codes) | Pregabalin 200mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3153941000033112 (PROD codes) | Pregabalin 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154041000033114 (PROD codes) | Lyrica 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154141000033113 (PROD codes) | Lyrica 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154241000033118 (PROD codes) | Lyrica 75mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154341000033111 (PROD codes) | Lyrica 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154441000033117 (PROD codes) | Lyrica 150mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154541000033116 (PROD codes) | Lyrica 200mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3154641000033115 (PROD codes) | Lyrica 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3157541000033114 (PROD codes) | Clobazam 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 3189041000033117 (PROD codes) | Topiramate 15mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3189141000033118 (PROD codes) | Topiramate 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3189241000033113 (PROD codes) | Topiramate 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3200941000033110 (PROD codes) | Levetiracetam 750mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 3201041000033117 (PROD codes) | Levetiracetam 100mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 3201141000033118 (PROD codes) | Keppra 750mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 3201241000033113 (PROD codes) | Keppra 100mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 3246441000033111 (PROD codes) | Klonopin 0.5mg oral lyophilisates | Anti-seizure medication CPRD aurum (all) primary care |
| 325841000033119 (PROD codes) | Convulex 150mg gastro-resistant capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 325941000033110 (PROD codes) | Convulex 300mg gastro-resistant capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 326041000033117 (PROD codes) | Convulex 500mg gastro-resistant capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3291841000033110 (PROD codes) | Zonisamide 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3291941000033119 (PROD codes) | Zonisamide 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3292041000033113 (PROD codes) | Zonisamide 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3292141000033112 (PROD codes) | Zonegran 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3292241000033117 (PROD codes) | Zonegran 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3292341000033110 (PROD codes) | Zonegran 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 3889841000033119 (PROD codes) | Felbamate 600mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 3923941000033110 (PROD codes) | Sodium valproate 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 3928541000033113 (PROD codes) | Levetiracetam 500mg/5ml solution for infusion vials | Anti-seizure medication CPRD aurum (all) primary care |
| 3928641000033114 (PROD codes) | Keppra 500mg/5ml concentrate for solution for infusion vials | Anti-seizure medication CPRD aurum (all) primary care |
| 3929241000033115 (PROD codes) | Midazolam 100mg/50ml solution for infusion vials | Anti-seizure medication CPRD aurum (all) primary care |
| 3956041000033115 (PROD codes) | Midazolam 5mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 3979441000033115 (PROD codes) | Carbamazepine 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 3993541000033113 (PROD codes) | Pregabalin 75mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 4021241000033113 (PROD codes) | Sodium valproate 300mg/3ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 4021341000033115 (PROD codes) | Episenta 300mg/3ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 4150241000033114 (PROD codes) | Sodium valproate 150mg modified-release capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4150341000033116 (PROD codes) | Sodium valproate 300mg modified-release capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4150441000033110 (PROD codes) | Episenta 150mg modified-release capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4150641000033112 (PROD codes) | Episenta 300mg modified-release capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4150941000033117 (PROD codes) | Sodium valproate 500mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4151041000033110 (PROD codes) | Sodium valproate 1g modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4151141000033114 (PROD codes) | Episenta 500mg modified-release granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4151241000033119 (PROD codes) | Episenta 1000mg modified-release granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4151341000033112 (PROD codes) | Midazolam 50mg/10ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 4171741000033110 (PROD codes) | Acetazolamide 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 4268341000033113 (PROD codes) | Rufinamide 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4268441000033119 (PROD codes) | Rufinamide 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4268541000033118 (PROD codes) | Rufinamide 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4268641000033117 (PROD codes) | Inovelon 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4268741000033114 (PROD codes) | Inovelon 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4268841000033116 (PROD codes) | Inovelon 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4387641000033111 (PROD codes) | Pregabalin 225mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4387741000033119 (PROD codes) | Lyrica 225mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4434741000033113 (PROD codes) | Sodium valproate 1g/10ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 4457141000033119 (PROD codes) | Stiripentol 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4457241000033114 (PROD codes) | Stiripentol 500mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4457341000033116 (PROD codes) | Stiripentol 250mg oral powder sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4457441000033110 (PROD codes) | Stiripentol 500mg oral powder sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4457541000033111 (PROD codes) | Diacomit 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4457641000033112 (PROD codes) | Diacomit 500mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4457741000033115 (PROD codes) | Diacomit 250mg oral powder sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4457841000033113 (PROD codes) | Diacomit 500mg oral powder sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 446441000033119 (PROD codes) | Diazemuls 10mg/2ml emulsion for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 448341000033114 (PROD codes) | Diamox Sodium Parenteral 500mg powder for solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 451641000033114 (PROD codes) | Diamox SR 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4549841000033112 (PROD codes) | Sodium valproate 100mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4549941000033116 (PROD codes) | Sodium valproate 250mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4550041000033113 (PROD codes) | Sodium valproate 50mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4550141000033112 (PROD codes) | Sodium valproate 750mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4550241000033117 (PROD codes) | Epilim Chronosphere MR 50mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4550341000033110 (PROD codes) | Epilim Chronosphere MR 100mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4550441000033116 (PROD codes) | Epilim Chronosphere MR 250mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4550541000033115 (PROD codes) | Epilim Chronosphere MR 500mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 4550641000033119 (PROD codes) | Epilim Chronosphere MR 750mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 457941000033112 (PROD codes) | Diazepam 10mg RecTubes | Anti-seizure medication CPRD aurum (all) primary care |
| 458041000033110 (PROD codes) | Diazepam 2.5mg RecTubes | Anti-seizure medication CPRD aurum (all) primary care |
| 458241000033119 (PROD codes) | Diazepam 5mg RecTubes | Anti-seizure medication CPRD aurum (all) primary care |
| 458341000033112 (PROD codes) | Diazepam 2.5mg/1.25ml rectal solution tube | Anti-seizure medication CPRD aurum (all) primary care |
| 458541000033117 (PROD codes) | Diazepam 10mg/2.5ml rectal solution tube | Anti-seizure medication CPRD aurum (all) primary care |
| 458641000033116 (PROD codes) | Diazepam 5mg/2.5ml rectal solution tube | Anti-seizure medication CPRD aurum (all) primary care |
| 460041000033115 (PROD codes) | Diazepam 10mg suppositories | Anti-seizure medication CPRD aurum (all) primary care |
| 4606641000033118 (PROD codes) | Lacosamide 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4606741000033110 (PROD codes) | Lacosamide 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4606841000033117 (PROD codes) | Lacosamide 150mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4606941000033113 (PROD codes) | Lacosamide 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4607041000033114 (PROD codes) | Lacosamide 15mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4607141000033113 (PROD codes) | Lacosamide 200mg/20ml solution for infusion vials | Anti-seizure medication CPRD aurum (all) primary care |
| 4607241000033118 (PROD codes) | Vimpat 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4607341000033111 (PROD codes) | Vimpat 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4607441000033117 (PROD codes) | Vimpat 150mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4607541000033116 (PROD codes) | Vimpat 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4607641000033115 (PROD codes) | Vimpat 15mg/ml syrup | Anti-seizure medication CPRD aurum (all) primary care |
| 4655041000033114 (PROD codes) | Acetazolamide 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 466341000033116 (PROD codes) | Diamox 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4957341000033119 (PROD codes) | Pregabalin 150mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5008741000033110 (PROD codes) | Sultiame 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 5009441000033113 (PROD codes) | Sultiame 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 5055041000033113 (PROD codes) | Epilim Chronosphere MR 1000mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 5090541000033119 (PROD codes) | Midazolam 2mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 5100341000033117 (PROD codes) | Gabapentin 400mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 511341000033115 (PROD codes) | Emeside 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 513841000033113 (PROD codes) | Emeside 250mg/5ml syrup | Anti-seizure medication CPRD aurum (all) primary care |
| 524741000033114 (PROD codes) | Epanutin 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 524841000033116 (PROD codes) | Epanutin 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 524941000033112 (PROD codes) | Epanutin 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 525041000033112 (PROD codes) | Epanutin 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 526941000033119 (PROD codes) | Epanutin Ready-Mixed Parenteral 250mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 5292541000033110 (PROD codes) | Everolimus 5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 5292641000033111 (PROD codes) | Everolimus 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 5292841000033112 (PROD codes) | Afinitor 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 529441000033118 (PROD codes) | Epanutin Infatabs 50mg chewable tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 529541000033117 (PROD codes) | Epilim Intravenous 400mg powder and solvent for solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 529641000033116 (PROD codes) | Epilim 200mg/5ml liquid | Anti-seizure medication CPRD aurum (all) primary care |
| 529841000033115 (PROD codes) | Epilim Chrono 200 tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 529941000033111 (PROD codes) | Epilim Chrono 300 tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 530041000033115 (PROD codes) | Epilim Chrono 500 tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 531941000033113 (PROD codes) | Epanutin 30mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 532141000033115 (PROD codes) | Epilim 200mg/5ml syrup | Anti-seizure medication CPRD aurum (all) primary care |
| 5323841000033119 (PROD codes) | Zebinix 800mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 5323941000033110 (PROD codes) | Eslicarbazepine 800mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 532541000033112 (PROD codes) | Epilim 100mg crushable tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 532641000033113 (PROD codes) | Epilim 200 gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 532741000033116 (PROD codes) | Epilim 500 gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 5377241000033111 (PROD codes) | Topiramate 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5404041000033114 (PROD codes) | Paraldehyde 50% in Olive oil rectal solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5426341000033114 (PROD codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5426441000033115 (PROD codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5426541000033119 (PROD codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5426641000033118 (PROD codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5426741000033110 (PROD codes) | Buccolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5426841000033117 (PROD codes) | Buccolam 5mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5426941000033113 (PROD codes) | Buccolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5427041000033114 (PROD codes) | Buccolam 10mg/2ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 5452741000033110 (PROD codes) | Primidone 62.5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 547141000033116 (PROD codes) | Ethosuximide 250mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 549441000033115 (PROD codes) | Ethosuximide 250mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5575641000033118 (PROD codes) | Zonisamide 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5887341000033110 (PROD codes) | Phenytoin 90mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5887441000033116 (PROD codes) | Phenytoin 90mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5890841000033118 (PROD codes) | Gabapentin 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5892141000033113 (PROD codes) | Clobazam 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5892241000033118 (PROD codes) | Clobazam 10mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5899541000033113 (PROD codes) | Clobazam 1mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5899641000033114 (PROD codes) | Clobazam 1mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5899741000033117 (PROD codes) | Clobazam 2.5mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5899841000033110 (PROD codes) | Clobazam 2.5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5899941000033119 (PROD codes) | Clobazam 25mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5900041000033117 (PROD codes) | Clobazam 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5901041000033114 (PROD codes) | Clonazepam 12.5mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5901241000033118 (PROD codes) | Clonazepam 250micrograms/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5901341000033111 (PROD codes) | Clonazepam 250micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5968141000033119 (PROD codes) | Gabapentin 100mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5968241000033114 (PROD codes) | Gabapentin 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5968341000033116 (PROD codes) | Gabapentin 200mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5968441000033110 (PROD codes) | Gabapentin 200mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5968541000033111 (PROD codes) | Gabapentin 300mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5968641000033112 (PROD codes) | Gabapentin 300mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5973041000033115 (PROD codes) | Midazolam 10mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5973141000033116 (PROD codes) | Midazolam 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5973241000033111 (PROD codes) | Midazolam 12.5mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5973341000033118 (PROD codes) | Midazolam 12.5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5973441000033112 (PROD codes) | Midazolam 5mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5973541000033113 (PROD codes) | Midazolam 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5974041000033117 (PROD codes) | Phenobarbital 90mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5974141000033118 (PROD codes) | Phenobarbital 90mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5978341000033111 (PROD codes) | Phenobarbital 10mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5978441000033117 (PROD codes) | Phenobarbital 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5991341000033113 (PROD codes) | Clonazepam 2mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5993441000033118 (PROD codes) | Gabapentin 400mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5997641000033114 (PROD codes) | Phenobarbital 50mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5997741000033117 (PROD codes) | Phenobarbital 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5997941000033119 (PROD codes) | Pregabalin 75mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 5998441000033113 (PROD codes) | Zonisamide 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 5998641000033110 (PROD codes) | Zonisamide 50mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 6001641000033114 (PROD codes) | Midazolam 10mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 6013841000033113 (PROD codes) | Pregabalin 75mg oral powder sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 6067741000033110 (PROD codes) | Primidone 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6067841000033117 (PROD codes) | Mysoline 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 609541000033119 (PROD codes) | Frisium 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6165641000033117 (PROD codes) | Retigabine 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6165741000033114 (PROD codes) | Retigabine 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6165841000033116 (PROD codes) | Retigabine 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6165941000033112 (PROD codes) | Retigabine 300mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6166041000033119 (PROD codes) | Retigabine 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6166141000033115 (PROD codes) | Trobalt 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6166241000033110 (PROD codes) | Trobalt 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6166341000033117 (PROD codes) | Trobalt 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6166441000033111 (PROD codes) | Trobalt 300mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 620641000033115 (PROD codes) | Gabapentin 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 620741000033112 (PROD codes) | Gabapentin 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 620841000033119 (PROD codes) | Gabapentin 400mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 6360941000033113 (PROD codes) | Clobazam 2mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 6361041000033115 (PROD codes) | Clobazam 2mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 6470841000033117 (PROD codes) | Everolimus 2.5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6471741000033117 (PROD codes) | Votubia 5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6475241000033113 (PROD codes) | Lacosamide 10mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 6475341000033115 (PROD codes) | Vimpat 10mg/ml syrup | Anti-seizure medication CPRD aurum (all) primary care |
| 6475441000033114 (PROD codes) | Midazolam 10mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 6512441000033115 (PROD codes) | Matever 750mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6512541000033119 (PROD codes) | Matever 500mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6512641000033118 (PROD codes) | Matever 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 6529041000033112 (PROD codes) | Clonazepam 2mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 6529741000033110 (PROD codes) | Clonazepam 500micrograms/5ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 664141000033111 (PROD codes) | Heminevrin 192mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 736941000033118 (PROD codes) | Hypnovel 10mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 737041000033117 (PROD codes) | Hypnovel 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 7678541000033116 (PROD codes) | Epistatus 10mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum (all) primary care |
| 7687641000033113 (PROD codes) | Rufinamide 40mg/ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 7687741000033116 (PROD codes) | Inovelon 40mg/ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 7859541000033118 (PROD codes) | Phenobarbital 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 7871541000033119 (PROD codes) | Pregabalin 20mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 7871641000033118 (PROD codes) | Lyrica 20mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 809341000033116 (PROD codes) | Lamictal 100mg dispersible tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 809441000033110 (PROD codes) | Lamictal 25mg dispersible tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 809541000033111 (PROD codes) | Lamictal 5mg dispersible tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 809641000033112 (PROD codes) | Lamotrigine 100mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 809741000033115 (PROD codes) | Lamotrigine 25mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 809841000033113 (PROD codes) | Lamotrigine 5mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8114241000033114 (PROD codes) | Perampanel 2mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114341000033116 (PROD codes) | Perampanel 4mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114441000033110 (PROD codes) | Perampanel 6mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114541000033111 (PROD codes) | Perampanel 8mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114641000033112 (PROD codes) | Perampanel 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114741000033115 (PROD codes) | Perampanel 12mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114841000033113 (PROD codes) | Fycompa 2mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8114941000033117 (PROD codes) | Fycompa 4mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8115041000033117 (PROD codes) | Fycompa 6mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8115141000033118 (PROD codes) | Fycompa 8mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8115241000033113 (PROD codes) | Fycompa 10mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8115341000033115 (PROD codes) | Fycompa 12mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8124641000033115 (PROD codes) | Phenytoin sodium 25mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 8124741000033112 (PROD codes) | Phenytoin sodium 50mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 8124841000033119 (PROD codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 8124941000033110 (PROD codes) | Phenytoin sodium 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 8125341000033112 (PROD codes) | Gabapentin 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 816841000033115 (PROD codes) | Lamictal 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 816941000033111 (PROD codes) | Lamictal 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 817041000033112 (PROD codes) | Lamotrigine 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 817141000033111 (PROD codes) | Lamotrigine 50mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 817341000033114 (PROD codes) | Lamictal 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 817441000033115 (PROD codes) | Lamotrigine 25mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 817741000033110 (PROD codes) | Lamictal 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 817841000033117 (PROD codes) | Lamotrigine 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 8237041000033117 (PROD codes) | Gabapentin 50mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8241000033118 (PROD codes) | Acetazolamide 500mg powder for solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 8246741000033115 (PROD codes) | Levetiracetam 1g granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8246841000033113 (PROD codes) | Levetiracetam 250mg granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8246941000033117 (PROD codes) | Levetiracetam 500mg granules sachets sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8247041000033116 (PROD codes) | Desitrend 1000mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 8247141000033117 (PROD codes) | Desitrend 250mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 8247241000033112 (PROD codes) | Desitrend 500mg granules sachets | Anti-seizure medication CPRD aurum (all) primary care |
| 8262841000033115 (PROD codes) | Clobazam 5mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8262941000033111 (PROD codes) | Clobazam 10mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8263041000033118 (PROD codes) | Tapclob 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 8263141000033119 (PROD codes) | Tapclob 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 844141000033111 (PROD codes) | Lorazepam 4mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 8535841000033110 (PROD codes) | Sodium valproate 400mg/4ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 8536541000033119 (PROD codes) | Lamotrigine 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 8841000033119 (PROD codes) | Acetazolamide 250mg modified-release capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 8870741000033111 (PROD codes) | Clonazepam 2.5mg/ml drops | Anti-seizure medication CPRD aurum (all) primary care |
| 8885341000033112 (PROD codes) | Desitrend 100mg/ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 88941000033110 (PROD codes) | Ativan 4mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 9118141000033112 (PROD codes) | Afinitor 2.5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 9119841000033112 (PROD codes) | Carbagen 100mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 9119941000033116 (PROD codes) | Carbagen 200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 9120041000033118 (PROD codes) | Carbagen 400mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 914741000033113 (PROD codes) | Midazolam 10mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 914841000033115 (PROD codes) | Midazolam 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 9158441000033111 (PROD codes) | Eytazox 250mg modified-release capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 946441000033116 (PROD codes) | Mysoline 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum (all) primary care |
| 948141000033113 (PROD codes) | Mysoline 250mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 958041000033112 (PROD codes) | Neurontin 100mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 958141000033111 (PROD codes) | Neurontin 300mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 958241000033116 (PROD codes) | Neurontin 400mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 9703341000033113 (PROD codes) | Gabapentin 6% gel | Anti-seizure medication CPRD aurum (all) primary care |
| 9776741000033114 (PROD codes) | Topiramate 100mg/5ml oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 984241000033117 (PROD codes) | Nootropil 33% oral solution | Anti-seizure medication CPRD aurum (all) primary care |
| 987841000033110 (PROD codes) | Nootropil 1200mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 987941000033119 (PROD codes) | Nootropil 800mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 10205841000033114 (PROD codes) | Rewisca 25mg capsules | Anti-seizure medication CPRD aurum |
| 10205941000033118 (PROD codes) | Rewisca 50mg capsules | Anti-seizure medication CPRD aurum |
| 10206041000033111 (PROD codes) | Rewisca 75mg capsules | Anti-seizure medication CPRD aurum |
| 10206141000033110 (PROD codes) | Rewisca 100mg capsules | Anti-seizure medication CPRD aurum |
| 10206241000033115 (PROD codes) | Rewisca 150mg capsules | Anti-seizure medication CPRD aurum |
| 10206341000033113 (PROD codes) | Rewisca 200mg capsules | Anti-seizure medication CPRD aurum |
| 10206441000033119 (PROD codes) | Rewisca 225mg capsules | Anti-seizure medication CPRD aurum |
| 10206541000033118 (PROD codes) | Rewisca 300mg capsules | Anti-seizure medication CPRD aurum |
| 10220341000033117 (PROD codes) | Lecaent 25mg capsules | Anti-seizure medication CPRD aurum |
| 10220441000033111 (PROD codes) | Lecaent 50mg capsules | Anti-seizure medication CPRD aurum |
| 10220541000033112 (PROD codes) | Lecaent 75mg capsules | Anti-seizure medication CPRD aurum |
| 10220641000033113 (PROD codes) | Lecaent 100mg capsules | Anti-seizure medication CPRD aurum |
| 10220741000033116 (PROD codes) | Lecaent 150mg capsules | Anti-seizure medication CPRD aurum |
| 10220841000033114 (PROD codes) | Lecaent 200mg capsules | Anti-seizure medication CPRD aurum |
| 10220941000033118 (PROD codes) | Lecaent 225mg capsules | Anti-seizure medication CPRD aurum |
| 10221041000033111 (PROD codes) | Lecaent 300mg capsules | Anti-seizure medication CPRD aurum |
| 10229041000033112 (PROD codes) | Levetiracetam 500mg/5ml solution for infusion ampoules | Anti-seizure medication CPRD aurum |
| 10229241000033116 (PROD codes) | Desitrend 500mg/5ml concentrate for solution for infusion ampoules | Anti-seizure medication CPRD aurum |
| 10253941000033110 (PROD codes) | Alzain 25mg capsules | Anti-seizure medication CPRD aurum |
| 10254041000033112 (PROD codes) | Alzain 50mg capsules | Anti-seizure medication CPRD aurum |
| 10254141000033111 (PROD codes) | Alzain 75mg capsules | Anti-seizure medication CPRD aurum |
| 10254241000033116 (PROD codes) | Alzain 100mg capsules | Anti-seizure medication CPRD aurum |
| 10254341000033114 (PROD codes) | Alzain 150mg capsules | Anti-seizure medication CPRD aurum |
| 10254441000033115 (PROD codes) | Alzain 200mg capsules | Anti-seizure medication CPRD aurum |
| 10254541000033119 (PROD codes) | Alzain 225mg capsules | Anti-seizure medication CPRD aurum |
| 10254641000033118 (PROD codes) | Alzain 300mg capsules | Anti-seizure medication CPRD aurum |
| 10334241000033111 (PROD codes) | Everolimus 500microgram tablets | Anti-seizure medication CPRD aurum |
| 10334441000033112 (PROD codes) | Everolimus 250microgram tablets | Anti-seizure medication CPRD aurum |
| 10334541000033113 (PROD codes) | Everolimus 750microgram tablets | Anti-seizure medication CPRD aurum |
| 10334641000033114 (PROD codes) | Certican 0.25mg tablets | Anti-seizure medication CPRD aurum |
| 10334741000033117 (PROD codes) | Certican 0.5mg tablets | Anti-seizure medication CPRD aurum |
| 10334841000033110 (PROD codes) | Certican 0.75mg tablets | Anti-seizure medication CPRD aurum |
| 1034941000033113 (PROD codes) | Paraldehyde 100% solution for injection 5ml ampoules | Anti-seizure medication CPRD aurum |
| 10388041000033115 (PROD codes) | Perizam 1mg/ml oral suspension | Anti-seizure medication CPRD aurum |
| 10388141000033116 (PROD codes) | Perizam 2mg/ml oral suspension | Anti-seizure medication CPRD aurum |
| 1068641000033115 (PROD codes) | Phenytoin sodium 300mg capsules | Anti-seizure medication CPRD aurum |
| 1068841000033119 (PROD codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD aurum |
| 1068941000033110 (PROD codes) | Phenytoin sodium 25mg capsules | Anti-seizure medication CPRD aurum |
| 1069041000033118 (PROD codes) | Phenytoin sodium 50mg capsules | Anti-seizure medication CPRD aurum |
| 10702041000033117 (PROD codes) | Phenobarbital 30mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 10702141000033118 (PROD codes) | Phenobarbital 60mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 1074441000033118 (PROD codes) | Phenytoin sodium 250mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 1074641000033116 (PROD codes) | Phenytoin 50mg chewable tablets | Anti-seizure medication CPRD aurum |
| 1082141000033114 (PROD codes) | Phenytoin sodium 100mg tablets | Anti-seizure medication CPRD aurum |
| 1082541000033117 (PROD codes) | Phenytoin sodium 50mg tablets | Anti-seizure medication CPRD aurum |
| 1089441000033113 (PROD codes) | Piracetam 333.3mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 1092041000033114 (PROD codes) | Piracetam 1.2g tablets | Anti-seizure medication CPRD aurum |
| 1092141000033113 (PROD codes) | Piracetam 800mg tablets | Anti-seizure medication CPRD aurum |
| 11026841000033112 (PROD codes) | Brivaracetam 50mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 11027241000033111 (PROD codes) | Briviact 10mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 11028241000033112 (PROD codes) | Brivaracetam 100mg tablets | Anti-seizure medication CPRD aurum |
| 11028441000033113 (PROD codes) | Brivaracetam 10mg tablets | Anti-seizure medication CPRD aurum |
| 11028541000033114 (PROD codes) | Brivaracetam 25mg tablets | Anti-seizure medication CPRD aurum |
| 11028641000033110 (PROD codes) | Brivaracetam 50mg tablets | Anti-seizure medication CPRD aurum |
| 11028741000033118 (PROD codes) | Brivaracetam 75mg tablets | Anti-seizure medication CPRD aurum |
| 11028841000033111 (PROD codes) | Briviact 100mg tablets | Anti-seizure medication CPRD aurum |
| 11028941000033115 (PROD codes) | Briviact 10mg tablets | Anti-seizure medication CPRD aurum |
| 11029041000033112 (PROD codes) | Briviact 25mg tablets | Anti-seizure medication CPRD aurum |
| 11029141000033111 (PROD codes) | Briviact 50mg tablets | Anti-seizure medication CPRD aurum |
| 11029241000033116 (PROD codes) | Briviact 75mg tablets | Anti-seizure medication CPRD aurum |
| 11141000033118 (PROD codes) | Acetazolamide 250mg tablets | Anti-seizure medication CPRD aurum |
| 1129241000033113 (PROD codes) | Primidone 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 1139341000033117 (PROD codes) | Primidone 250mg tablets | Anti-seizure medication CPRD aurum |
| 11559841000033118 (PROD codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum |
| 11559941000033114 (PROD codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum |
| 11560041000033112 (PROD codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum |
| 11560141000033111 (PROD codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum |
| 11616241000033110 (PROD codes) | Clonazepam 1mg/1ml solution for injection ampoules and diluent | Anti-seizure medication CPRD aurum |
| 11616341000033117 (PROD codes) | Rivotril 1mg/1ml concentrate for solution for injection ampoules and diluent | Anti-seizure medication CPRD aurum |
| 11717841000033118 (PROD codes) | Phenytoin sodium 100mg tablets | Anti-seizure medication CPRD aurum |
| 11724841000033116 (PROD codes) | Valproic acid 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 1177241000033117 (PROD codes) | Rivotril 500microgram tablets | Anti-seizure medication CPRD aurum |
| 1177341000033110 (PROD codes) | Rivotril 2mg tablets | Anti-seizure medication CPRD aurum |
| 11821741000033110 (PROD codes) | Axalid 25mg capsules | Anti-seizure medication CPRD aurum |
| 11821841000033117 (PROD codes) | Axalid 50mg capsules | Anti-seizure medication CPRD aurum |
| 11821941000033113 (PROD codes) | Axalid 75mg capsules | Anti-seizure medication CPRD aurum |
| 11822041000033119 (PROD codes) | Axalid 100mg capsules | Anti-seizure medication CPRD aurum |
| 11822141000033115 (PROD codes) | Axalid 150mg capsules | Anti-seizure medication CPRD aurum |
| 11822241000033110 (PROD codes) | Axalid 200mg capsules | Anti-seizure medication CPRD aurum |
| 11822341000033117 (PROD codes) | Axalid 225mg capsules | Anti-seizure medication CPRD aurum |
| 11822441000033111 (PROD codes) | Axalid 300mg capsules | Anti-seizure medication CPRD aurum |
| 12188741000033115 (PROD codes) | Everolimus 2mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 12188941000033117 (PROD codes) | Everolimus 3mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 12189141000033113 (PROD codes) | Everolimus 5mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 12202541000033114 (PROD codes) | Zacco 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 12202641000033110 (PROD codes) | Zacco 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 12315241000033112 (PROD codes) | Midazolam 10mg/1ml oromucosal solution pre-filled oral syringes sugar free | Anti-seizure medication CPRD aurum |
| 12341141000033112 (PROD codes) | Eslicarbazepine 200mg tablets | Anti-seizure medication CPRD aurum |
| 12341241000033117 (PROD codes) | Zebinix 200mg tablets | Anti-seizure medication CPRD aurum |
| 1252741000033112 (PROD codes) | Sabril 500mg oral powder sachets | Anti-seizure medication CPRD aurum |
| 12578741000033117 (PROD codes) | Depakin 200mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 1258841000033116 (PROD codes) | Sabril 500mg tablets | Anti-seizure medication CPRD aurum |
| 12602641000033112 (PROD codes) | Phenobarbital 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 12684541000033116 (PROD codes) | Ethosuximide 250mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 12881541000033111 (PROD codes) | Eslicarbazepine 50mg/1ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 12881641000033112 (PROD codes) | Zebinix 50mg/1ml oral suspension | Anti-seizure medication CPRD aurum |
| 12903541000033116 (PROD codes) | Mesuximide 150mg capsules | Anti-seizure medication CPRD aurum |
| 12910641000033110 (PROD codes) | Topiramate 50mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 12910741000033118 (PROD codes) | Topiramate 100mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 12999441000033116 (PROD codes) | Perampanel 500micrograms/ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 12999541000033115 (PROD codes) | Fycompa 0.5mg/ml oral suspension | Anti-seizure medication CPRD aurum |
| 13091441000033117 (PROD codes) | Dilantin Infatabs 50mg chewable tablets | Anti-seizure medication CPRD aurum |
| 13149541000033117 (PROD codes) | Belvo 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 13149641000033116 (PROD codes) | Belvo 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 13149741000033113 (PROD codes) | Midazolam 10mg/5ml oral solution unit dose ampoules sugar free | Anti-seizure medication CPRD aurum |
| 13344341000033118 (PROD codes) | Pregabalin 25mg tablets | Anti-seizure medication CPRD aurum |
| 13344541000033113 (PROD codes) | Pregabalin 50mg tablets | Anti-seizure medication CPRD aurum |
| 13344641000033114 (PROD codes) | Pregabalin 75mg tablets | Anti-seizure medication CPRD aurum |
| 13344741000033117 (PROD codes) | Pregabalin 100mg tablets | Anti-seizure medication CPRD aurum |
| 13344841000033110 (PROD codes) | Pregabalin 150mg tablets | Anti-seizure medication CPRD aurum |
| 13344941000033119 (PROD codes) | Pregabalin 200mg tablets | Anti-seizure medication CPRD aurum |
| 13345041000033119 (PROD codes) | Pregabalin 225mg tablets | Anti-seizure medication CPRD aurum |
| 13345141000033115 (PROD codes) | Pregabalin 300mg tablets | Anti-seizure medication CPRD aurum |
| 13348941000033113 (PROD codes) | Syonell 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 13349541000033114 (PROD codes) | Syonell 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 13352641000033119 (PROD codes) | Phenobarbital 100mg tablets | Anti-seizure medication CPRD aurum |
| 13352741000033111 (PROD codes) | Cannabidiol 100mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 13352941000033114 (PROD codes) | Epidyolex 100mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 13420041000033119 (PROD codes) | Midazolam 50mg/50ml solution for infusion pre-filled syringes | Anti-seizure medication CPRD aurum |
| 13446741000033116 (PROD codes) | Vigabatrin 100mg soluble tablets sugar free | Anti-seizure medication CPRD aurum |
| 13446841000033114 (PROD codes) | Vigabatrin 500mg soluble tablets sugar free | Anti-seizure medication CPRD aurum |
| 1358241000033111 (PROD codes) | Sodium valproate 400mg powder and solvent for solution for injection vials | Anti-seizure medication CPRD aurum |
| 1359341000033113 (PROD codes) | Sodium valproate 200mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 1359441000033119 (PROD codes) | Sodium valproate 300mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 1359541000033118 (PROD codes) | Sodium valproate 500mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 1361241000033114 (PROD codes) | Sodium valproate 200mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 1363641000033113 (PROD codes) | Sodium valproate 200mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 1364941000033115 (PROD codes) | Sodium valproate 100mg tablets | Anti-seizure medication CPRD aurum |
| 1365041000033115 (PROD codes) | Sodium valproate 200mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 1365141000033116 (PROD codes) | Sodium valproate 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 13722141000033112 (PROD codes) | Dyzantil 200mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 13722241000033117 (PROD codes) | Dyzantil 300mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 13722341000033110 (PROD codes) | Dyzantil 500mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 13752941000033110 (PROD codes) | Zonisamide 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 13753041000033117 (PROD codes) | Desizon 20mg/ml oral suspension | Anti-seizure medication CPRD aurum |
| 13764841000033115 (PROD codes) | Phenobarbital 30mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 13765041000033111 (PROD codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD aurum |
| 13830041000033111 (PROD codes) | Midazolam 5mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 1383241000033113 (PROD codes) | Stesolid 10mg rectal tube | Anti-seizure medication CPRD aurum |
| 1383341000033115 (PROD codes) | Stesolid 5mg rectal tube | Anti-seizure medication CPRD aurum |
| 13910341000033111 (PROD codes) | Fenfluramine 2.2mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 13914541000033113 (PROD codes) | Epesri 250mg capsules | Anti-seizure medication CPRD aurum |
| 13934341000033111 (PROD codes) | Cenobamate 50mg tablets | Anti-seizure medication CPRD aurum |
| 13934441000033117 (PROD codes) | Cenobamate 100mg tablets | Anti-seizure medication CPRD aurum |
| 13934541000033116 (PROD codes) | Cenobamate 150mg tablets | Anti-seizure medication CPRD aurum |
| 13934641000033115 (PROD codes) | Cenobamate 200mg tablets | Anti-seizure medication CPRD aurum |
| 13934741000033112 (PROD codes) | Ontozry 50mg tablets | Anti-seizure medication CPRD aurum |
| 13934841000033119 (PROD codes) | Ontozry 100mg tablets | Anti-seizure medication CPRD aurum |
| 13935041000033110 (PROD codes) | Ontozry 200mg tablets | Anti-seizure medication CPRD aurum |
| 14032541000033118 (PROD codes) | Clonazepam 1mg tablets | Anti-seizure medication CPRD aurum |
| 1415041000033114 (PROD codes) | Tegretol 100mg Chewtabs | Anti-seizure medication CPRD aurum |
| 1415141000033113 (PROD codes) | Tegretol 200mg Chewtabs | Anti-seizure medication CPRD aurum |
| 1423941000033119 (PROD codes) | Tegretol 125mg suppositories | Anti-seizure medication CPRD aurum |
| 1424041000033117 (PROD codes) | Tegretol 250mg suppositories | Anti-seizure medication CPRD aurum |
| 1424241000033113 (PROD codes) | Tegretol 100mg/5ml liquid | Anti-seizure medication CPRD aurum |
| 1425841000033111 (PROD codes) | Tegretol 100mg tablets | Anti-seizure medication CPRD aurum |
| 1425941000033115 (PROD codes) | Tegretol 200mg tablets | Anti-seizure medication CPRD aurum |
| 1426041000033113 (PROD codes) | Tegretol 400mg tablets | Anti-seizure medication CPRD aurum |
| 1428841000033119 (PROD codes) | Tegretol Prolonged Release 200mg tablets | Anti-seizure medication CPRD aurum |
| 1428941000033110 (PROD codes) | Tegretol Prolonged Release 400mg tablets | Anti-seizure medication CPRD aurum |
| 1450441000033115 (PROD codes) | Topamax 100mg tablets | Anti-seizure medication CPRD aurum |
| 1450541000033119 (PROD codes) | Topamax 200mg tablets | Anti-seizure medication CPRD aurum |
| 1450641000033118 (PROD codes) | Topamax 50mg tablets | Anti-seizure medication CPRD aurum |
| 1451441000033112 (PROD codes) | Topamax 25mg tablets | Anti-seizure medication CPRD aurum |
| 1451541000033113 (PROD codes) | Topiramate 100mg tablets | Anti-seizure medication CPRD aurum |
| 1451641000033114 (PROD codes) | Topiramate 200mg tablets | Anti-seizure medication CPRD aurum |
| 1451741000033117 (PROD codes) | Topiramate 25mg tablets | Anti-seizure medication CPRD aurum |
| 1451841000033110 (PROD codes) | Topiramate 50mg tablets | Anti-seizure medication CPRD aurum |
| 1500041000033112 (PROD codes) | Valproic acid 150mg gastro-resistant capsules | Anti-seizure medication CPRD aurum |
| 1500141000033111 (PROD codes) | Valproic acid 300mg gastro-resistant capsules | Anti-seizure medication CPRD aurum |
| 1500241000033116 (PROD codes) | Valproic acid 500mg gastro-resistant capsules | Anti-seizure medication CPRD aurum |
| 1502941000033114 (PROD codes) | Valclair 10mg suppositories | Anti-seizure medication CPRD aurum |
| 1521941000033110 (PROD codes) | Vigabatrin 500mg oral powder sachets sugar free | Anti-seizure medication CPRD aurum |
| 1522741000033118 (PROD codes) | Vigabatrin 500mg tablets | Anti-seizure medication CPRD aurum |
| 1548241000033112 (PROD codes) | Zarontin 250mg capsules | Anti-seizure medication CPRD aurum |
| 1550041000033116 (PROD codes) | Zarontin 250mg/5ml syrup | Anti-seizure medication CPRD aurum |
| 1611841000033119 (PROD codes) | Gabitril 10mg tablets | Anti-seizure medication CPRD aurum |
| 1611941000033110 (PROD codes) | Gabitril 15mg tablets | Anti-seizure medication CPRD aurum |
| 1612041000033116 (PROD codes) | Gabitril 5mg tablets | Anti-seizure medication CPRD aurum |
| 1701341000033119 (PROD codes) | Tiagabine 10mg tablets | Anti-seizure medication CPRD aurum |
| 1701441000033113 (PROD codes) | Tiagabine 15mg tablets | Anti-seizure medication CPRD aurum |
| 1701541000033114 (PROD codes) | Tiagabine 5mg tablets | Anti-seizure medication CPRD aurum |
| 1729541000033118 (PROD codes) | Epimaz 100mg tablets | Anti-seizure medication CPRD aurum |
| 1729641000033117 (PROD codes) | Epimaz 200mg tablets | Anti-seizure medication CPRD aurum |
| 1729741000033114 (PROD codes) | Epimaz 400mg tablets | Anti-seizure medication CPRD aurum |
| 1747541000033114 (PROD codes) | Orlept SF 200mg/5ml liquid | Anti-seizure medication CPRD aurum |
| 1747641000033110 (PROD codes) | Orlept 200mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 1747741000033118 (PROD codes) | Orlept 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 1767341000033110 (PROD codes) | Fosphenytoin 750mg/10ml solution for injection vials | Anti-seizure medication CPRD aurum |
| 1767441000033116 (PROD codes) | Pro-Epanutin 750mg/10ml concentrate for solution for injection vials | Anti-seizure medication CPRD aurum |
| 178741000033110 (PROD codes) | Carbamazepine 100mg chewable tablets sugar free | Anti-seizure medication CPRD aurum |
| 178841000033117 (PROD codes) | Carbamazepine 200mg chewable tablets sugar free | Anti-seizure medication CPRD aurum |
| 1847941000033118 (PROD codes) | Topamax 15mg sprinkle capsules | Anti-seizure medication CPRD aurum |
| 1848041000033115 (PROD codes) | Topamax 25mg sprinkle capsules | Anti-seizure medication CPRD aurum |
| 1870841000033112 (PROD codes) | Phenytoin 30mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 198141000033115 (PROD codes) | Carbamazepine 100mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 2033041000033110 (PROD codes) | Oxcarbazepine 150mg tablets | Anti-seizure medication CPRD aurum |
| 2033141000033114 (PROD codes) | Oxcarbazepine 300mg tablets | Anti-seizure medication CPRD aurum |
| 2033241000033119 (PROD codes) | Oxcarbazepine 600mg tablets | Anti-seizure medication CPRD aurum |
| 2033341000033112 (PROD codes) | Trileptal 150mg tablets | Anti-seizure medication CPRD aurum |
| 2033441000033118 (PROD codes) | Trileptal 300mg tablets | Anti-seizure medication CPRD aurum |
| 2033541000033117 (PROD codes) | Trileptal 600mg tablets | Anti-seizure medication CPRD aurum |
| 2056341000033116 (PROD codes) | Midazolam 50mg/50ml solution for infusion vials | Anti-seizure medication CPRD aurum |
| 207541000033111 (PROD codes) | Carbamazepine 125mg suppositories | Anti-seizure medication CPRD aurum |
| 207641000033112 (PROD codes) | Carbamazepine 250mg suppositories | Anti-seizure medication CPRD aurum |
| 2093841000033113 (PROD codes) | Potassium bromide powder | Anti-seizure medication CPRD aurum |
| 212541000033112 (PROD codes) | Carbamazepine 100mg tablets | Anti-seizure medication CPRD aurum |
| 212641000033113 (PROD codes) | Carbamazepine 200mg tablets | Anti-seizure medication CPRD aurum |
| 212741000033116 (PROD codes) | Carbamazepine 400mg tablets | Anti-seizure medication CPRD aurum |
| 2145941000033118 (PROD codes) | Gabapentin 600mg tablets | Anti-seizure medication CPRD aurum |
| 2146041000033111 (PROD codes) | Gabapentin 800mg tablets | Anti-seizure medication CPRD aurum |
| 2146141000033110 (PROD codes) | Neurontin 600mg tablets | Anti-seizure medication CPRD aurum |
| 2146241000033115 (PROD codes) | Neurontin 800mg tablets | Anti-seizure medication CPRD aurum |
| 2212941000033119 (PROD codes) | Levetiracetam 250mg tablets | Anti-seizure medication CPRD aurum |
| 2213041000033112 (PROD codes) | Levetiracetam 500mg tablets | Anti-seizure medication CPRD aurum |
| 2213141000033111 (PROD codes) | Levetiracetam 1g tablets | Anti-seizure medication CPRD aurum |
| 2213241000033116 (PROD codes) | Keppra 250mg tablets | Anti-seizure medication CPRD aurum |
| 2213341000033114 (PROD codes) | Keppra 500mg tablets | Anti-seizure medication CPRD aurum |
| 2213441000033115 (PROD codes) | Keppra 1g tablets | Anti-seizure medication CPRD aurum |
| 2217641000033111 (PROD codes) | Topamax 50mg sprinkle capsules | Anti-seizure medication CPRD aurum |
| 2266041000033115 (PROD codes) | Carbamazepine 200mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 2266141000033116 (PROD codes) | Carbamazepine 400mg modified-release tablets | Anti-seizure medication CPRD aurum |
| 2271441000033112 (PROD codes) | Depakote 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 2271541000033113 (PROD codes) | Depakote 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 2584441000033110 (PROD codes) | Lamotrigine 2mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 2584541000033111 (PROD codes) | Lamictal 2mg dispersible tablets | Anti-seizure medication CPRD aurum |
| 2601041000033112 (PROD codes) | Clonazepam 2.5mg/ml drops sugar free | Anti-seizure medication CPRD aurum |
| 2601141000033111 (PROD codes) | Rivotril 2.5mg/1ml drops | Anti-seizure medication CPRD aurum |
| 262841000033110 (PROD codes) | Clobazam 10mg tablets | Anti-seizure medication CPRD aurum |
| 2640041000033113 (PROD codes) | Clonazepam 125micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 2667941000033119 (PROD codes) | Clonazepam 625micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 2668041000033116 (PROD codes) | Teril Retard 200mg tablets | Anti-seizure medication CPRD aurum |
| 2668141000033117 (PROD codes) | Teril Retard 400mg tablets | Anti-seizure medication CPRD aurum |
| 2711041000033119 (PROD codes) | Clobazam 5mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 2711241000033110 (PROD codes) | Valproic acid 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 2711341000033117 (PROD codes) | Valproic acid 500mg gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 2719441000033110 (PROD codes) | Clonazepam 500micrograms/5ml oral solution | Anti-seizure medication CPRD aurum |
| 2722341000033116 (PROD codes) | Clonazepam 500micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 2730441000033114 (PROD codes) | Arbil MR 200mg tablets | Anti-seizure medication CPRD aurum |
| 2730541000033110 (PROD codes) | Arbil MR 400mg tablets | Anti-seizure medication CPRD aurum |
| 2752741000033119 (PROD codes) | Clonazepam 2mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 2758641000033114 (PROD codes) | Primidone 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 2796241000033118 (PROD codes) | Gabapentin 250mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 2796341000033111 (PROD codes) | Neurontin 250mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 2799141000033115 (PROD codes) | Epival CR 500mg tablets | Anti-seizure medication CPRD aurum |
| 2799241000033110 (PROD codes) | Epival CR 300mg tablets | Anti-seizure medication CPRD aurum |
| 2839041000033113 (PROD codes) | Oxcarbazepine 60mg/ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 2839141000033112 (PROD codes) | Trileptal 60mg/ml oral suspension | Anti-seizure medication CPRD aurum |
| 286741000033118 (PROD codes) | Clonazepam 500microgram tablets | Anti-seizure medication CPRD aurum |
| 286841000033111 (PROD codes) | Clonazepam 2mg tablets | Anti-seizure medication CPRD aurum |
| 2928641000033118 (PROD codes) | Epimaz Retard 200mg tablets | Anti-seizure medication CPRD aurum |
| 2928741000033110 (PROD codes) | Epimaz Retard 400mg tablets | Anti-seizure medication CPRD aurum |
| 2929341000033119 (PROD codes) | Carbagen SR 200mg tablets | Anti-seizure medication CPRD aurum |
| 2929441000033113 (PROD codes) | Carbagen SR 400mg tablets | Anti-seizure medication CPRD aurum |
| 2973141000033118 (PROD codes) | Topiramate 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 3033041000033117 (PROD codes) | Diazepam 10mg/2ml emulsion for injection ampoules | Anti-seizure medication CPRD aurum |
| 3033141000033118 (PROD codes) | Diazepam 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 3076141000033111 (PROD codes) | Topiramate 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 3085341000033114 (PROD codes) | Clomethiazole 192mg capsules | Anti-seizure medication CPRD aurum |
| 3096941000033115 (PROD codes) | Mesuximide 300mg capsules | Anti-seizure medication CPRD aurum |
| 3102641000033118 (PROD codes) | Phenobarbital 15mg/5ml elixir | Anti-seizure medication CPRD aurum |
| 3102741000033110 (PROD codes) | Phenobarbital 200mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 3103141000033116 (PROD codes) | Phenobarbital 15mg tablets | Anti-seizure medication CPRD aurum |
| 3103241000033111 (PROD codes) | Phenobarbital 30mg tablets | Anti-seizure medication CPRD aurum |
| 3103341000033118 (PROD codes) | Phenobarbital 60mg tablets | Anti-seizure medication CPRD aurum |
| 3135541000033116 (PROD codes) | Clonazepam 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 3152941000033118 (PROD codes) | Sodium valproate 300mg suppositories | Anti-seizure medication CPRD aurum |
| 3153041000033111 (PROD codes) | Sodium valproate 100mg suppositories | Anti-seizure medication CPRD aurum |
| 3153341000033113 (PROD codes) | Pregabalin 25mg capsules | Anti-seizure medication CPRD aurum |
| 3153441000033119 (PROD codes) | Pregabalin 50mg capsules | Anti-seizure medication CPRD aurum |
| 3153541000033118 (PROD codes) | Pregabalin 75mg capsules | Anti-seizure medication CPRD aurum |
| 3153641000033117 (PROD codes) | Pregabalin 100mg capsules | Anti-seizure medication CPRD aurum |
| 3153741000033114 (PROD codes) | Pregabalin 150mg capsules | Anti-seizure medication CPRD aurum |
| 3153841000033116 (PROD codes) | Pregabalin 200mg capsules | Anti-seizure medication CPRD aurum |
| 3153941000033112 (PROD codes) | Pregabalin 300mg capsules | Anti-seizure medication CPRD aurum |
| 3154041000033114 (PROD codes) | Lyrica 25mg capsules | Anti-seizure medication CPRD aurum |
| 3154141000033113 (PROD codes) | Lyrica 50mg capsules | Anti-seizure medication CPRD aurum |
| 3154241000033118 (PROD codes) | Lyrica 75mg capsules | Anti-seizure medication CPRD aurum |
| 3154341000033111 (PROD codes) | Lyrica 100mg capsules | Anti-seizure medication CPRD aurum |
| 3154441000033117 (PROD codes) | Lyrica 150mg capsules | Anti-seizure medication CPRD aurum |
| 3154541000033116 (PROD codes) | Lyrica 200mg capsules | Anti-seizure medication CPRD aurum |
| 3154641000033115 (PROD codes) | Lyrica 300mg capsules | Anti-seizure medication CPRD aurum |
| 3157541000033114 (PROD codes) | Clobazam 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 3189041000033117 (PROD codes) | Topiramate 15mg capsules | Anti-seizure medication CPRD aurum |
| 3189141000033118 (PROD codes) | Topiramate 25mg capsules | Anti-seizure medication CPRD aurum |
| 3189241000033113 (PROD codes) | Topiramate 50mg capsules | Anti-seizure medication CPRD aurum |
| 3200941000033110 (PROD codes) | Levetiracetam 750mg tablets | Anti-seizure medication CPRD aurum |
| 3201041000033117 (PROD codes) | Levetiracetam 100mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 3201141000033118 (PROD codes) | Keppra 750mg tablets | Anti-seizure medication CPRD aurum |
| 3201241000033113 (PROD codes) | Keppra 100mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 3246441000033111 (PROD codes) | Klonopin 0.5mg oral lyophilisates | Anti-seizure medication CPRD aurum |
| 325841000033119 (PROD codes) | Convulex 150mg gastro-resistant capsules | Anti-seizure medication CPRD aurum |
| 325941000033110 (PROD codes) | Convulex 300mg gastro-resistant capsules | Anti-seizure medication CPRD aurum |
| 326041000033117 (PROD codes) | Convulex 500mg gastro-resistant capsules | Anti-seizure medication CPRD aurum |
| 3291841000033110 (PROD codes) | Zonisamide 25mg capsules | Anti-seizure medication CPRD aurum |
| 3291941000033119 (PROD codes) | Zonisamide 50mg capsules | Anti-seizure medication CPRD aurum |
| 3292041000033113 (PROD codes) | Zonisamide 100mg capsules | Anti-seizure medication CPRD aurum |
| 3292141000033112 (PROD codes) | Zonegran 25mg capsules | Anti-seizure medication CPRD aurum |
| 3292241000033117 (PROD codes) | Zonegran 50mg capsules | Anti-seizure medication CPRD aurum |
| 3292341000033110 (PROD codes) | Zonegran 100mg capsules | Anti-seizure medication CPRD aurum |
| 3889841000033119 (PROD codes) | Felbamate 600mg tablets | Anti-seizure medication CPRD aurum |
| 3923941000033110 (PROD codes) | Sodium valproate 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 3928541000033113 (PROD codes) | Levetiracetam 500mg/5ml solution for infusion vials | Anti-seizure medication CPRD aurum |
| 3928641000033114 (PROD codes) | Keppra 500mg/5ml concentrate for solution for infusion vials | Anti-seizure medication CPRD aurum |
| 3929241000033115 (PROD codes) | Midazolam 100mg/50ml solution for infusion vials | Anti-seizure medication CPRD aurum |
| 3956041000033115 (PROD codes) | Midazolam 5mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 3979441000033115 (PROD codes) | Carbamazepine 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 3993541000033113 (PROD codes) | Pregabalin 75mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 4021241000033113 (PROD codes) | Sodium valproate 300mg/3ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 4021341000033115 (PROD codes) | Episenta 300mg/3ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 4150241000033114 (PROD codes) | Sodium valproate 150mg modified-release capsules | Anti-seizure medication CPRD aurum |
| 4150341000033116 (PROD codes) | Sodium valproate 300mg modified-release capsules | Anti-seizure medication CPRD aurum |
| 4150441000033110 (PROD codes) | Episenta 150mg modified-release capsules | Anti-seizure medication CPRD aurum |
| 4150641000033112 (PROD codes) | Episenta 300mg modified-release capsules | Anti-seizure medication CPRD aurum |
| 4150941000033117 (PROD codes) | Sodium valproate 500mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 4151041000033110 (PROD codes) | Sodium valproate 1g modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 4151141000033114 (PROD codes) | Episenta 500mg modified-release granules sachets | Anti-seizure medication CPRD aurum |
| 4151241000033119 (PROD codes) | Episenta 1000mg modified-release granules sachets | Anti-seizure medication CPRD aurum |
| 4151341000033112 (PROD codes) | Midazolam 50mg/10ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 4171741000033110 (PROD codes) | Acetazolamide 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 4268341000033113 (PROD codes) | Rufinamide 100mg tablets | Anti-seizure medication CPRD aurum |
| 4268441000033119 (PROD codes) | Rufinamide 200mg tablets | Anti-seizure medication CPRD aurum |
| 4268541000033118 (PROD codes) | Rufinamide 400mg tablets | Anti-seizure medication CPRD aurum |
| 4268641000033117 (PROD codes) | Inovelon 100mg tablets | Anti-seizure medication CPRD aurum |
| 4268741000033114 (PROD codes) | Inovelon 200mg tablets | Anti-seizure medication CPRD aurum |
| 4268841000033116 (PROD codes) | Inovelon 400mg tablets | Anti-seizure medication CPRD aurum |
| 4387641000033111 (PROD codes) | Pregabalin 225mg capsules | Anti-seizure medication CPRD aurum |
| 4387741000033119 (PROD codes) | Lyrica 225mg capsules | Anti-seizure medication CPRD aurum |
| 4434741000033113 (PROD codes) | Sodium valproate 1g/10ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 4457141000033119 (PROD codes) | Stiripentol 250mg capsules | Anti-seizure medication CPRD aurum |
| 4457241000033114 (PROD codes) | Stiripentol 500mg capsules | Anti-seizure medication CPRD aurum |
| 4457341000033116 (PROD codes) | Stiripentol 250mg oral powder sachets | Anti-seizure medication CPRD aurum |
| 4457441000033110 (PROD codes) | Stiripentol 500mg oral powder sachets | Anti-seizure medication CPRD aurum |
| 4457541000033111 (PROD codes) | Diacomit 250mg capsules | Anti-seizure medication CPRD aurum |
| 4457641000033112 (PROD codes) | Diacomit 500mg capsules | Anti-seizure medication CPRD aurum |
| 4457741000033115 (PROD codes) | Diacomit 250mg oral powder sachets | Anti-seizure medication CPRD aurum |
| 4457841000033113 (PROD codes) | Diacomit 500mg oral powder sachets | Anti-seizure medication CPRD aurum |
| 446441000033119 (PROD codes) | Diazemuls 10mg/2ml emulsion for injection ampoules | Anti-seizure medication CPRD aurum |
| 448341000033114 (PROD codes) | Diamox Sodium Parenteral 500mg powder for solution for injection vials | Anti-seizure medication CPRD aurum |
| 451641000033114 (PROD codes) | Diamox SR 250mg capsules | Anti-seizure medication CPRD aurum |
| 4549841000033112 (PROD codes) | Sodium valproate 100mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 4549941000033116 (PROD codes) | Sodium valproate 250mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 4550041000033113 (PROD codes) | Sodium valproate 50mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 4550141000033112 (PROD codes) | Sodium valproate 750mg modified-release granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 4550241000033117 (PROD codes) | Epilim Chronosphere MR 50mg granules sachets | Anti-seizure medication CPRD aurum |
| 4550341000033110 (PROD codes) | Epilim Chronosphere MR 100mg granules sachets | Anti-seizure medication CPRD aurum |
| 4550441000033116 (PROD codes) | Epilim Chronosphere MR 250mg granules sachets | Anti-seizure medication CPRD aurum |
| 4550541000033115 (PROD codes) | Epilim Chronosphere MR 500mg granules sachets | Anti-seizure medication CPRD aurum |
| 4550641000033119 (PROD codes) | Epilim Chronosphere MR 750mg granules sachets | Anti-seizure medication CPRD aurum |
| 457941000033112 (PROD codes) | Diazepam 10mg RecTubes | Anti-seizure medication CPRD aurum |
| 458041000033110 (PROD codes) | Diazepam 2.5mg RecTubes | Anti-seizure medication CPRD aurum |
| 458241000033119 (PROD codes) | Diazepam 5mg RecTubes | Anti-seizure medication CPRD aurum |
| 458341000033112 (PROD codes) | Diazepam 2.5mg/1.25ml rectal solution tube | Anti-seizure medication CPRD aurum |
| 458541000033117 (PROD codes) | Diazepam 10mg/2.5ml rectal solution tube | Anti-seizure medication CPRD aurum |
| 458641000033116 (PROD codes) | Diazepam 5mg/2.5ml rectal solution tube | Anti-seizure medication CPRD aurum |
| 460041000033115 (PROD codes) | Diazepam 10mg suppositories | Anti-seizure medication CPRD aurum |
| 4606641000033118 (PROD codes) | Lacosamide 50mg tablets | Anti-seizure medication CPRD aurum |
| 4606741000033110 (PROD codes) | Lacosamide 100mg tablets | Anti-seizure medication CPRD aurum |
| 4606841000033117 (PROD codes) | Lacosamide 150mg tablets | Anti-seizure medication CPRD aurum |
| 4606941000033113 (PROD codes) | Lacosamide 200mg tablets | Anti-seizure medication CPRD aurum |
| 4607041000033114 (PROD codes) | Lacosamide 15mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 4607141000033113 (PROD codes) | Lacosamide 200mg/20ml solution for infusion vials | Anti-seizure medication CPRD aurum |
| 4607241000033118 (PROD codes) | Vimpat 50mg tablets | Anti-seizure medication CPRD aurum |
| 4607341000033111 (PROD codes) | Vimpat 100mg tablets | Anti-seizure medication CPRD aurum |
| 4607441000033117 (PROD codes) | Vimpat 150mg tablets | Anti-seizure medication CPRD aurum |
| 4607541000033116 (PROD codes) | Vimpat 200mg tablets | Anti-seizure medication CPRD aurum |
| 4607641000033115 (PROD codes) | Vimpat 15mg/ml syrup | Anti-seizure medication CPRD aurum |
| 4655041000033114 (PROD codes) | Acetazolamide 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 466341000033116 (PROD codes) | Diamox 250mg tablets | Anti-seizure medication CPRD aurum |
| 4957341000033119 (PROD codes) | Pregabalin 150mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5008741000033110 (PROD codes) | Sultiame 200mg tablets | Anti-seizure medication CPRD aurum |
| 5009441000033113 (PROD codes) | Sultiame 50mg tablets | Anti-seizure medication CPRD aurum |
| 5055041000033113 (PROD codes) | Epilim Chronosphere MR 1000mg granules sachets | Anti-seizure medication CPRD aurum |
| 5090541000033119 (PROD codes) | Midazolam 2mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 5100341000033117 (PROD codes) | Gabapentin 400mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 511341000033115 (PROD codes) | Emeside 250mg capsules | Anti-seizure medication CPRD aurum |
| 513841000033113 (PROD codes) | Emeside 250mg/5ml syrup | Anti-seizure medication CPRD aurum |
| 524741000033114 (PROD codes) | Epanutin 100mg capsules | Anti-seizure medication CPRD aurum |
| 524841000033116 (PROD codes) | Epanutin 25mg capsules | Anti-seizure medication CPRD aurum |
| 524941000033112 (PROD codes) | Epanutin 50mg capsules | Anti-seizure medication CPRD aurum |
| 525041000033112 (PROD codes) | Epanutin 300mg capsules | Anti-seizure medication CPRD aurum |
| 526941000033119 (PROD codes) | Epanutin Ready-Mixed Parenteral 250mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 5292541000033110 (PROD codes) | Everolimus 5mg tablets | Anti-seizure medication CPRD aurum |
| 5292641000033111 (PROD codes) | Everolimus 10mg tablets | Anti-seizure medication CPRD aurum |
| 5292841000033112 (PROD codes) | Afinitor 10mg tablets | Anti-seizure medication CPRD aurum |
| 529441000033118 (PROD codes) | Epanutin Infatabs 50mg chewable tablets | Anti-seizure medication CPRD aurum |
| 529541000033117 (PROD codes) | Epilim Intravenous 400mg powder and solvent for solution for injection vials | Anti-seizure medication CPRD aurum |
| 529641000033116 (PROD codes) | Epilim 200mg/5ml liquid | Anti-seizure medication CPRD aurum |
| 529841000033115 (PROD codes) | Epilim Chrono 200 tablets | Anti-seizure medication CPRD aurum |
| 529941000033111 (PROD codes) | Epilim Chrono 300 tablets | Anti-seizure medication CPRD aurum |
| 530041000033115 (PROD codes) | Epilim Chrono 500 tablets | Anti-seizure medication CPRD aurum |
| 531941000033113 (PROD codes) | Epanutin 30mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 532141000033115 (PROD codes) | Epilim 200mg/5ml syrup | Anti-seizure medication CPRD aurum |
| 5323841000033119 (PROD codes) | Zebinix 800mg tablets | Anti-seizure medication CPRD aurum |
| 5323941000033110 (PROD codes) | Eslicarbazepine 800mg tablets | Anti-seizure medication CPRD aurum |
| 532541000033112 (PROD codes) | Epilim 100mg crushable tablets | Anti-seizure medication CPRD aurum |
| 532641000033113 (PROD codes) | Epilim 200 gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 532741000033116 (PROD codes) | Epilim 500 gastro-resistant tablets | Anti-seizure medication CPRD aurum |
| 5377241000033111 (PROD codes) | Topiramate 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5404041000033114 (PROD codes) | Paraldehyde 50% in Olive oil rectal solution | Anti-seizure medication CPRD aurum |
| 5426341000033114 (PROD codes) | Midazolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5426441000033115 (PROD codes) | Midazolam 5mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5426541000033119 (PROD codes) | Midazolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5426641000033118 (PROD codes) | Midazolam 10mg/2ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5426741000033110 (PROD codes) | Buccolam 2.5mg/0.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5426841000033117 (PROD codes) | Buccolam 5mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5426941000033113 (PROD codes) | Buccolam 7.5mg/1.5ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5427041000033114 (PROD codes) | Buccolam 10mg/2ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 5452741000033110 (PROD codes) | Primidone 62.5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 547141000033116 (PROD codes) | Ethosuximide 250mg capsules | Anti-seizure medication CPRD aurum |
| 549441000033115 (PROD codes) | Ethosuximide 250mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5575641000033118 (PROD codes) | Zonisamide 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5887341000033110 (PROD codes) | Phenytoin 90mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5887441000033116 (PROD codes) | Phenytoin 90mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5890841000033118 (PROD codes) | Gabapentin 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5892141000033113 (PROD codes) | Clobazam 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5892241000033118 (PROD codes) | Clobazam 10mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5899541000033113 (PROD codes) | Clobazam 1mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5899641000033114 (PROD codes) | Clobazam 1mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5899741000033117 (PROD codes) | Clobazam 2.5mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5899841000033110 (PROD codes) | Clobazam 2.5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5899941000033119 (PROD codes) | Clobazam 25mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5900041000033117 (PROD codes) | Clobazam 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5901041000033114 (PROD codes) | Clonazepam 12.5mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5901241000033118 (PROD codes) | Clonazepam 250micrograms/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5901341000033111 (PROD codes) | Clonazepam 250micrograms/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5968141000033119 (PROD codes) | Gabapentin 100mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5968241000033114 (PROD codes) | Gabapentin 100mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5968341000033116 (PROD codes) | Gabapentin 200mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5968441000033110 (PROD codes) | Gabapentin 200mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5968541000033111 (PROD codes) | Gabapentin 300mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5968641000033112 (PROD codes) | Gabapentin 300mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5973041000033115 (PROD codes) | Midazolam 10mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5973141000033116 (PROD codes) | Midazolam 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5973241000033111 (PROD codes) | Midazolam 12.5mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5973341000033118 (PROD codes) | Midazolam 12.5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5973441000033112 (PROD codes) | Midazolam 5mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5973541000033113 (PROD codes) | Midazolam 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5974041000033117 (PROD codes) | Phenobarbital 90mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5974141000033118 (PROD codes) | Phenobarbital 90mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5978341000033111 (PROD codes) | Phenobarbital 10mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5978441000033117 (PROD codes) | Phenobarbital 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5991341000033113 (PROD codes) | Clonazepam 2mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5993441000033118 (PROD codes) | Gabapentin 400mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5997641000033114 (PROD codes) | Phenobarbital 50mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5997741000033117 (PROD codes) | Phenobarbital 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5997941000033119 (PROD codes) | Pregabalin 75mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 5998441000033113 (PROD codes) | Zonisamide 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 5998641000033110 (PROD codes) | Zonisamide 50mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 6001641000033114 (PROD codes) | Midazolam 10mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 6013841000033113 (PROD codes) | Pregabalin 75mg oral powder sachets | Anti-seizure medication CPRD aurum |
| 6067741000033110 (PROD codes) | Primidone 50mg tablets | Anti-seizure medication CPRD aurum |
| 6067841000033117 (PROD codes) | Mysoline 50mg tablets | Anti-seizure medication CPRD aurum |
| 609541000033119 (PROD codes) | Frisium 10mg tablets | Anti-seizure medication CPRD aurum |
| 6165641000033117 (PROD codes) | Retigabine 50mg tablets | Anti-seizure medication CPRD aurum |
| 6165741000033114 (PROD codes) | Retigabine 100mg tablets | Anti-seizure medication CPRD aurum |
| 6165841000033116 (PROD codes) | Retigabine 200mg tablets | Anti-seizure medication CPRD aurum |
| 6165941000033112 (PROD codes) | Retigabine 300mg tablets | Anti-seizure medication CPRD aurum |
| 6166041000033119 (PROD codes) | Retigabine 400mg tablets | Anti-seizure medication CPRD aurum |
| 6166141000033115 (PROD codes) | Trobalt 50mg tablets | Anti-seizure medication CPRD aurum |
| 6166241000033110 (PROD codes) | Trobalt 100mg tablets | Anti-seizure medication CPRD aurum |
| 6166341000033117 (PROD codes) | Trobalt 200mg tablets | Anti-seizure medication CPRD aurum |
| 6166441000033111 (PROD codes) | Trobalt 300mg tablets | Anti-seizure medication CPRD aurum |
| 620641000033115 (PROD codes) | Gabapentin 100mg capsules | Anti-seizure medication CPRD aurum |
| 620741000033112 (PROD codes) | Gabapentin 300mg capsules | Anti-seizure medication CPRD aurum |
| 620841000033119 (PROD codes) | Gabapentin 400mg capsules | Anti-seizure medication CPRD aurum |
| 6360941000033113 (PROD codes) | Clobazam 2mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 6361041000033115 (PROD codes) | Clobazam 2mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 6470841000033117 (PROD codes) | Everolimus 2.5mg tablets | Anti-seizure medication CPRD aurum |
| 6471741000033117 (PROD codes) | Votubia 5mg tablets | Anti-seizure medication CPRD aurum |
| 6475241000033113 (PROD codes) | Lacosamide 10mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 6475341000033115 (PROD codes) | Vimpat 10mg/ml syrup | Anti-seizure medication CPRD aurum |
| 6475441000033114 (PROD codes) | Midazolam 10mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 6512441000033115 (PROD codes) | Matever 750mg tablets | Anti-seizure medication CPRD aurum |
| 6512541000033119 (PROD codes) | Matever 500mg tablets | Anti-seizure medication CPRD aurum |
| 6512641000033118 (PROD codes) | Matever 250mg tablets | Anti-seizure medication CPRD aurum |
| 6529041000033112 (PROD codes) | Clonazepam 2mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 6529741000033110 (PROD codes) | Clonazepam 500micrograms/5ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 664141000033111 (PROD codes) | Heminevrin 192mg capsules | Anti-seizure medication CPRD aurum |
| 736941000033118 (PROD codes) | Hypnovel 10mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 737041000033117 (PROD codes) | Hypnovel 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 7678541000033116 (PROD codes) | Epistatus 10mg/1ml oromucosal solution pre-filled oral syringes | Anti-seizure medication CPRD aurum |
| 7687641000033113 (PROD codes) | Rufinamide 40mg/ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 7687741000033116 (PROD codes) | Inovelon 40mg/ml oral suspension | Anti-seizure medication CPRD aurum |
| 7859541000033118 (PROD codes) | Phenobarbital 25mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 7871541000033119 (PROD codes) | Pregabalin 20mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 7871641000033118 (PROD codes) | Lyrica 20mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 809341000033116 (PROD codes) | Lamictal 100mg dispersible tablets | Anti-seizure medication CPRD aurum |
| 809441000033110 (PROD codes) | Lamictal 25mg dispersible tablets | Anti-seizure medication CPRD aurum |
| 809541000033111 (PROD codes) | Lamictal 5mg dispersible tablets | Anti-seizure medication CPRD aurum |
| 809641000033112 (PROD codes) | Lamotrigine 100mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 809741000033115 (PROD codes) | Lamotrigine 25mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 809841000033113 (PROD codes) | Lamotrigine 5mg dispersible tablets sugar free | Anti-seizure medication CPRD aurum |
| 8114241000033114 (PROD codes) | Perampanel 2mg tablets | Anti-seizure medication CPRD aurum |
| 8114341000033116 (PROD codes) | Perampanel 4mg tablets | Anti-seizure medication CPRD aurum |
| 8114441000033110 (PROD codes) | Perampanel 6mg tablets | Anti-seizure medication CPRD aurum |
| 8114541000033111 (PROD codes) | Perampanel 8mg tablets | Anti-seizure medication CPRD aurum |
| 8114641000033112 (PROD codes) | Perampanel 10mg tablets | Anti-seizure medication CPRD aurum |
| 8114741000033115 (PROD codes) | Perampanel 12mg tablets | Anti-seizure medication CPRD aurum |
| 8114841000033113 (PROD codes) | Fycompa 2mg tablets | Anti-seizure medication CPRD aurum |
| 8114941000033117 (PROD codes) | Fycompa 4mg tablets | Anti-seizure medication CPRD aurum |
| 8115041000033117 (PROD codes) | Fycompa 6mg tablets | Anti-seizure medication CPRD aurum |
| 8115141000033118 (PROD codes) | Fycompa 8mg tablets | Anti-seizure medication CPRD aurum |
| 8115241000033113 (PROD codes) | Fycompa 10mg tablets | Anti-seizure medication CPRD aurum |
| 8115341000033115 (PROD codes) | Fycompa 12mg tablets | Anti-seizure medication CPRD aurum |
| 8124641000033115 (PROD codes) | Phenytoin sodium 25mg capsules | Anti-seizure medication CPRD aurum |
| 8124741000033112 (PROD codes) | Phenytoin sodium 50mg capsules | Anti-seizure medication CPRD aurum |
| 8124841000033119 (PROD codes) | Phenytoin sodium 100mg capsules | Anti-seizure medication CPRD aurum |
| 8124941000033110 (PROD codes) | Phenytoin sodium 300mg capsules | Anti-seizure medication CPRD aurum |
| 8125341000033112 (PROD codes) | Gabapentin 500mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 816841000033115 (PROD codes) | Lamictal 100mg tablets | Anti-seizure medication CPRD aurum |
| 816941000033111 (PROD codes) | Lamictal 50mg tablets | Anti-seizure medication CPRD aurum |
| 817041000033112 (PROD codes) | Lamotrigine 100mg tablets | Anti-seizure medication CPRD aurum |
| 817141000033111 (PROD codes) | Lamotrigine 50mg tablets | Anti-seizure medication CPRD aurum |
| 817341000033114 (PROD codes) | Lamictal 25mg tablets | Anti-seizure medication CPRD aurum |
| 817441000033115 (PROD codes) | Lamotrigine 25mg tablets | Anti-seizure medication CPRD aurum |
| 817741000033110 (PROD codes) | Lamictal 200mg tablets | Anti-seizure medication CPRD aurum |
| 817841000033117 (PROD codes) | Lamotrigine 200mg tablets | Anti-seizure medication CPRD aurum |
| 8237041000033117 (PROD codes) | Gabapentin 50mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum |
| 8241000033118 (PROD codes) | Acetazolamide 500mg powder for solution for injection vials | Anti-seizure medication CPRD aurum |
| 8246741000033115 (PROD codes) | Levetiracetam 1g granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 8246841000033113 (PROD codes) | Levetiracetam 250mg granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 8246941000033117 (PROD codes) | Levetiracetam 500mg granules sachets sugar free | Anti-seizure medication CPRD aurum |
| 8247041000033116 (PROD codes) | Desitrend 1000mg granules sachets | Anti-seizure medication CPRD aurum |
| 8247141000033117 (PROD codes) | Desitrend 250mg granules sachets | Anti-seizure medication CPRD aurum |
| 8247241000033112 (PROD codes) | Desitrend 500mg granules sachets | Anti-seizure medication CPRD aurum |
| 8262841000033115 (PROD codes) | Clobazam 5mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 8262941000033111 (PROD codes) | Clobazam 10mg/5ml oral suspension sugar free | Anti-seizure medication CPRD aurum |
| 8263041000033118 (PROD codes) | Tapclob 5mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 8263141000033119 (PROD codes) | Tapclob 10mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 844141000033111 (PROD codes) | Lorazepam 4mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 8535841000033110 (PROD codes) | Sodium valproate 400mg/4ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 8536541000033119 (PROD codes) | Lamotrigine 50mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 8841000033119 (PROD codes) | Acetazolamide 250mg modified-release capsules | Anti-seizure medication CPRD aurum |
| 8870741000033111 (PROD codes) | Clonazepam 2.5mg/ml drops | Anti-seizure medication CPRD aurum |
| 8885341000033112 (PROD codes) | Desitrend 100mg/ml oral solution | Anti-seizure medication CPRD aurum |
| 88941000033110 (PROD codes) | Ativan 4mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 9118141000033112 (PROD codes) | Afinitor 2.5mg tablets | Anti-seizure medication CPRD aurum |
| 9119841000033112 (PROD codes) | Carbagen 100mg tablets | Anti-seizure medication CPRD aurum |
| 9119941000033116 (PROD codes) | Carbagen 200mg tablets | Anti-seizure medication CPRD aurum |
| 9120041000033118 (PROD codes) | Carbagen 400mg tablets | Anti-seizure medication CPRD aurum |
| 914741000033113 (PROD codes) | Midazolam 10mg/5ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 914841000033115 (PROD codes) | Midazolam 10mg/2ml solution for injection ampoules | Anti-seizure medication CPRD aurum |
| 9158441000033111 (PROD codes) | Eytazox 250mg modified-release capsules | Anti-seizure medication CPRD aurum |
| 946441000033116 (PROD codes) | Mysoline 250mg/5ml oral suspension | Anti-seizure medication CPRD aurum |
| 948141000033113 (PROD codes) | Mysoline 250mg tablets | Anti-seizure medication CPRD aurum |
| 958041000033112 (PROD codes) | Neurontin 100mg capsules | Anti-seizure medication CPRD aurum |
| 958141000033111 (PROD codes) | Neurontin 300mg capsules | Anti-seizure medication CPRD aurum |
| 958241000033116 (PROD codes) | Neurontin 400mg capsules | Anti-seizure medication CPRD aurum |
| 9703341000033113 (PROD codes) | Gabapentin 6% gel | Anti-seizure medication CPRD aurum |
| 9776741000033114 (PROD codes) | Topiramate 100mg/5ml oral solution | Anti-seizure medication CPRD aurum |
| 984241000033117 (PROD codes) | Nootropil 33% oral solution | Anti-seizure medication CPRD aurum |
| 987841000033110 (PROD codes) | Nootropil 1200mg tablets | Anti-seizure medication CPRD aurum |
| 987941000033119 (PROD codes) | Nootropil 800mg tablets | Anti-seizure medication CPRD aurum |
| 11060000 (BNF codes) | Acetazolamide 500mg powder for solution for injection vials | Anti-seizure medication CPRD aurum (all) primary care |
| 15010401 (BNF codes) | Midazolam 5mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 19040000 (BNF codes) | Potassium bromide powder | Anti-seizure medication CPRD aurum (all) primary care |
| 4010100 (BNF codes) | Clomethiazole 192mg capsules | Anti-seizure medication CPRD aurum (all) primary care |
| 4010200 (BNF codes) | Lorazepam 4mg/1ml solution for injection ampoules | Anti-seizure medication CPRD aurum (all) primary care |
| 4020300 (BNF codes) | Valproic acid 250mg gastro-resistant tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 4080100 (BNF codes) | Brivaracetam 50mg/5ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 4080200 (BNF codes) | Clonazepam 1mg/1ml solution for injection ampoules and diluent | Anti-seizure medication CPRD aurum (all) primary care |
| 4090300 (BNF codes) | Piracetam 333.3mg/ml oral solution sugar free | Anti-seizure medication CPRD aurum (all) primary care |
| 8010500 (BNF codes) | Everolimus 5mg tablets | Anti-seizure medication CPRD aurum (all) primary care |
| 100652 (Med codes) | Contraceptive advice for patients with epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 100920 (Med codes) | Pre-conception advice for patients with epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 101143 (Med codes) | Contraceptiv advice for patients with epilepsy not indicated | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 101224 (Med codes) | GLUT1 deficiency syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 102190 (Med codes) | Contraceptive advice for patients with epilepsy declined | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 102191 (Med codes) | Pregnancy advice for patients with epilepsy declined | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 102264 (Med codes) | Pre-conception advic fr patients with epilepsy not indicated | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 102265 (Med codes) | Pre-conception advice for patients with epilepsy declined | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 102359 (Med codes) | Pregnancy advice for patients with epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 102375 (Med codes) | Pregnancy advice for patients with epilepsy not indicated | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 105679 (Med codes) | Dravet syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 105926 (Med codes) | Glucose transporter protein type 1 deficiency syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 106571 (Med codes) | Generalised seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 108409 (Med codes) | Severe myoclonic epilepsy in infancy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 110497 (Med codes) | Observations of measures of seizures | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 11186 (Med codes) | Generalised nonconvulsive epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 11394 (Med codes) | Complex partial epileptic seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 12098 (Med codes) | O/E - focal fit | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 1306 (Med codes) | [D]Seizure NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 13220 (Med codes) | Epilepsy control poor | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 13221 (Med codes) | 2 to 4 seizures a month | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 17136 (Med codes) | O/E - a fit | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 1715 (Med codes) | Epileptic absences | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 17399 (Med codes) | Juvenile absence epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 18471 (Med codes) | Epileptic seizures - clonic | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 18899 (Med codes) | Daily seizures | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 1902 (Med codes) | Had a fit | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 19170 (Med codes) | Benign Rolandic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 19363 (Med codes) | Juvenile myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 19549 (Med codes) | 1 to 7 seizures a week | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 19550 (Med codes) | Epilepsy control good | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 19551 (Med codes) | Epilepsy care arrangement | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 19552 (Med codes) | Epilepsy does not limit activities | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 20566 (Med codes) | Epilepsy treatment stopped | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 21885 (Med codes) | Post-ictal state | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 22341 (Med codes) | Epilepsy confirmed | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 22804 (Med codes) | Tonic-clonic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 22991 (Med codes) | Epilepsy severity | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 23415 (Med codes) | Salaam attacks | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 23634 (Med codes) | Psychomotor epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 24309 (Med codes) | Epileptic seizures - atonic | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 25306 (Med codes) | Angelman syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 25330 (Med codes) | Complex partial status epilepticus | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26015 (Med codes) | Partial epilepsy without impairment of consciousness | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26144 (Med codes) | Generalised convulsive epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26512 (Med codes) | Epilepsy treatment changed | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26618 (Med codes) | 1 to 12 seizures a year | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26619 (Med codes) | Epilepsy limits activities | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26620 (Med codes) | Epilepsy restricts employment | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 26733 (Med codes) | Partial epilepsy without impairment of consciousness OS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 27280 (Med codes) | Prader-Willi syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 27526 (Med codes) | Partial epilepsy without impairment of consciousness NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 2907 (Med codes) | Petit mal (minor) epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 30604 (Med codes) | Alcohol-induced epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 30635 (Med codes) | Photosensitive epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 30816 (Med codes) | Drug-induced epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 31042 (Med codes) | [X]Rett's syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 31663 (Med codes) | O/E - salaam attack | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 3175 (Med codes) | Temporal lobe epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 31830 (Med codes) | Epileptic seizures - akinetic | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 31877 (Med codes) | [X]Schizophrenia-like psychosis in epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 31920 (Med codes) | Partial epilepsy with impairment of consciousness NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 32288 (Med codes) | Partial epilepsy with impairment of consciousness | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 32662 (Med codes) | O/E - fit/convulsion | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 34079 (Med codes) | Epileptic automatism | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 34473 (Med codes) | Epilepsy treatment started | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 34792 (Med codes) | Lennox-Gastaut syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 3607 (Med codes) | Fit (in known epileptic) NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 36203 (Med codes) | Psychosensory epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 3652 (Med codes) | Fit - had one, symptom | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 36696 (Med codes) | Epilepsy monitoring NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 37592 (Med codes) | Somatosensory epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 37644 (Med codes) | Progressive myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 37782 (Med codes) | Neonatal myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 3783 (Med codes) | H/O: epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 37906 (Med codes) | Early infant epileptic encephalopathy wth suppression bursts | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 38307 (Med codes) | Other forms of epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 38457 (Med codes) | O/E - fit/convulsion NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 38919 (Med codes) | Transient epileptic amnesia | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 39023 (Med codes) | West syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 39160 (Med codes) | Many seizures a day | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 39530 (Med codes) | O/E - Jacksonian fit | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 40105 (Med codes) | Simple partial epileptic seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 40806 (Med codes) | Generalised convulsive epilepsy NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 40863 (Med codes) | Epilepsy impairs education | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4093 (Med codes) | Status epilepticus | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4109 (Med codes) | Traumatic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 41461 (Med codes) | Prader-Willi Syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 42606 (Med codes) | Epilepsy screen invite 3 | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 43679 (Med codes) | [X]Acquired aphasia with epilepsy [Landau - Kleffner] | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 44252 (Med codes) | Generalised nonconvulsive epilepsy NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4478 (Med codes) | Infantile spasms | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4479 (Med codes) | Tuberous sclerosis | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 45602 (Med codes) | Myoclonic encephalopathy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 45757 (Med codes) | Epilepsy monitoring verbal invite | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 45927 (Med codes) | Other specified generalised convulsive epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4602 (Med codes) | Nocturnal epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 46516 (Med codes) | Niemann-Pick disease | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 46603 (Med codes) | Emergency epilepsy treatment since last appointment | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4749 (Med codes) | Sturge-Weber syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 47974 (Med codes) | Aicardi Goutieres syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 4801 (Med codes) | Epileptic seizures - myoclonic | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 48134 (Med codes) | Sensory induced epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 48211 (Med codes) | Alper's disease | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 48462 (Med codes) | [X]Limbic epilepsy personality | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 49322 (Med codes) | Infantile spasms NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 49340 (Med codes) | Otohara syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 49737 (Med codes) | Dyssynergia cerebellaris myoclonica | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 49889 (Med codes) | Acquired epileptic aphasia | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 50012 (Med codes) | Epilepsy associated problems | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 50702 (Med codes) | Epilepsy prevents employment | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 5117 (Med codes) | Grand mal status | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 5152 (Med codes) | Epileptic seizures - tonic | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 51998 (Med codes) | Ohtahara syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 53483 (Med codes) | Gelastic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 54002 (Med codes) | Rasmussen syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 5525 (Med codes) | Focal epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 55260 (Med codes) | Cursive (running) epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 55665 (Med codes) | Limbic system epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 55706 (Med codes) | Epilepsy management plan given | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 55739 (Med codes) | Visual reflex epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 56359 (Med codes) | Menstrual epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 5668 (Med codes) | Grand mal seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 56951 (Med codes) | Spielmeyer-Vogt (Batten) disease | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 57183 (Med codes) | Mitochond encephalopathy, lact acidosis &amp; strokelike episode | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 57277 (Med codes) | O/E - focal (Jacksonian) fit | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 573 (Med codes) | Epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 59120 (Med codes) | [X]Other status epilepticus | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 59185 (Med codes) | Other specified generalised nonconvulsive epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 59806 (Med codes) | Landau-Kleffner syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 6271 (Med codes) | Status epilepticus, unspecified | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 63826 (Med codes) | Unverricht - Lundborg disease | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 65343 (Med codes) | Cerebral degeneration in Niemann-Pick disease | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 65673 (Med codes) | Stress-induced epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 65699 (Med codes) | Motor epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 6709 (Med codes) | [X]Epileptic psychosis NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 68486 (Med codes) | Lightning spasms | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 68946 (Med codes) | Unilateral epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 6983 (Med codes) | Epilepsy monitoring | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 69831 (Med codes) | [X]Other epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 71719 (Med codes) | Kojevnikov's epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 71801 (Med codes) | [X]Status epilepticus, unspecified | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 72384 (Med codes) | Epilepsy monitoring telephone invite | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 7275 (Med codes) | O/E - a seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 7295 (Med codes) | FH: Epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 73542 (Med codes) | Visceral reflex epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 7945 (Med codes) | Hypsarrhythmia | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 8097 (Med codes) | Absence seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 8187 (Med codes) | Tonic-clonic epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 8487 (Med codes) | Myoclonic seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 9569 (Med codes) | Jacksonian, focal or motor epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 96641 (Med codes) | Panayiotopoulos syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 97059 (Med codes) | Angelman's syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 9747 (Med codes) | Epilepsy NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 98442 (Med codes) | Epilepsy monitoring call first letter | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 98536 (Med codes) | Epilepsy monitoring call second letter | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 98617 (Med codes) | Angelman syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 98753 (Med codes) | Aicardi syndrome | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 988 (Med codes) | Grand mal (major) epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 9886 (Med codes) | Petit mal status | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 9887 (Med codes) | Locl-rlt(foc)(part)idiop epilep&amp;epilptic syn seiz locl onset | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 98870 (Med codes) | Partial epilepsy with autonomic symptoms | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 98977 (Med codes) | Epilepsy monitoring call third letter | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 99548 (Med codes) | Pykno-epilepsy | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 99731 (Med codes) | [X]Other generalized epilepsy and epileptic syndromes | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 9979 (Med codes) | Other forms of epilepsy NOS | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 99834 (Med codes) | [D]Nocturnal seizure | Epilepsy, seizure and administration codes CPRD gold (all) primary care |
| 103531000006110 (Med codes) | Tonic-clonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 10791000006116 (Med codes) | Other specified generalised nonconvulsive epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 11300012 (Med codes) | Juvenile myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1172511000000110 (Med codes) | Glucose transporter protein type 1 deficiency syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1173961000000112 (Med codes) | Night seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1175991000000119 (Med codes) | Contraceptive advice for patients with epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1176031000000114 (Med codes) | Pre-conception advice for patients with epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1176071000000111 (Med codes) | Pregnancy advice for patients with epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1176241000000114 (Med codes) | Pregnancy advice for patients with epilepsy not indicated | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1176301000000117 (Med codes) | Contraceptive advice for patients with epilepsy declined | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1176341000000119 (Med codes) | Pre-conception advice for patients with epilepsy declined | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1176381000000110 (Med codes) | Pregnancy advice for patients with epilepsy declined | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 11778041000006119 (Med codes) | Dravet Syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 11831381000006119 (Med codes) | Infantile-onset symptomatic epilepsy syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 12049771000006118 (Med codes) | Hypothalamic hamartoma with gelastic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 12053881000006113 (Med codes) | Recurrent benign focal seizures of childhood | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 12076991000006114 (Med codes) | STXBP1 encephalopathy with epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1222437010 (Med codes) | Alper's disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1222472013 (Med codes) | Seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1227482018 (Med codes) | Observations of measures of seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1234038018 (Med codes) | Angelman's syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1234503010 (Med codes) | Aicardi syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 125721000006111 (Med codes) | Status epilepticus, unspecified | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 12602012 (Med codes) | Petit-mal status | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 127638013 (Med codes) | Angelman syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 12877016 (Med codes) | Tuberous sclerosis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13491221000006117 (Med codes) | Benign familial mesial temporal lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13493091000006112 (Med codes) | Benign occipital lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13493111000006115 (Med codes) | Benign partial epilepsy of infancy with complex partial seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13493431000006116 (Med codes) | Mesial temporal lobe epilepsy with hippocampal sclerosis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13494971000006112 (Med codes) | Intellectual disability, seizures, hypotonia, ophthalmologic, skeletal anomalies syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13495041000006116 (Med codes) | New-onset refractory status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13499471000006116 (Med codes) | Cortical dysplasia with focal epilepsy syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13500261000006114 (Med codes) | Infantile epileptic dyskinetic encephalopathy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13503061000006114 (Med codes) | Early-onset spastic ataxia, myoclonic epilepsy, neuropathy syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13572191000006116 (Med codes) | KCNQ2-related epileptic encephalopathy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13572931000006117 (Med codes) | Myoclonic epilepsy in non-progressive encephalopathy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13573141000006116 (Med codes) | Cryptogenic late-onset epileptic spasms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13622071000006110 (Med codes) | Diffuse cerebral and cerebellar atrophy, intractable seizures, progressive microcephaly syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13622561000006113 (Med codes) | Congenital muscular dystrophy with intellectual disability and severe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13624181000006116 (Med codes) | Infantile spasms, psychomotor retardation, progressive brain atrophy, basal ganglia disease syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13632801000006112 (Med codes) | Familial temporal lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13637261000006111 (Med codes) | Familial infantile myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13637841000006111 (Med codes) | Familial mesial temporal lobe epilepsy with febrile seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13646721000006112 (Med codes) | Multiple congenital anomalies, hypotonia, seizures syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13686241000006115 (Med codes) | Benign childhood epilepsy with centrotemporal spikes, refractory | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13686271000006111 (Med codes) | Benign childhood epilepsy with centrotemporal spikes, non-refractory | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 137801000000112 (Med codes) | Epilepsy limits activities | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13791581000006111 (Med codes) | Myoclonic epilepsy with ragged red fibres | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 138671000000116 (Med codes) | Epilepsy screening administration | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 138681000000119 (Med codes) | Epilepsy screening first invitation | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 138691000000117 (Med codes) | Epilepsy screening second invitation | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 138701000000117 (Med codes) | Epilepsy screening third invitation | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 139021000000118 (Med codes) | Exception reporting - epilepsy quality indicators | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13911981000006114 (Med codes) | Primary hyperaldosteronism, seizures, neurological abnormalities syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 139161000000110 (Med codes) | Excepted from epilepsy quality indicators - informed dissent | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13950881000006118 (Med codes) | Epilepsy due to infectious encephalitis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 13950921000006114 (Med codes) | Epilepsy due to infectious meningitis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 14055041000006118 (Med codes) | Scar epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 141981000000118 (Med codes) | Epilepsy restricts employment | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 141991000000116 (Med codes) | Epilepsy prevents employment | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 142041000000115 (Med codes) | Epilepsy does not limit activities | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 142051000000117 (Med codes) | Epilepsy management plan given | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 14453781000006117 (Med codes) | Non-convulsive seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 14636401000006111 (Med codes) | Generalised onset seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 148214012 (Med codes) | Prader-Willi syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 148427014 (Med codes) | Gelastic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 148591000006114 (Med codes) | Sensory induced epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1489345013 (Med codes) | Transient epileptic amnesia | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 154851000000115 (Med codes) | Epilepsy impairs education | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1550581000000111 (Med codes) | GLUT1 deficiency syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1673671000006116 (Med codes) | Epilepsy treatment continued | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1699591000006112 (Med codes) | Epilepsy monitoring call first letter | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1699611000006118 (Med codes) | Epilepsy monitoring call third letter | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1705901000006118 (Med codes) | Angelman syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1724341000006110 (Med codes) | GLUT1 deficiency syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1741271000006111 (Med codes) | Contraceptive advice for patients with epilepsy not indicated | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1741281000006114 (Med codes) | Pre-conception advice for patients with epilepsy not indicated | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1759441000006117 (Med codes) | HoNOS-LD item 13 - seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1780225016 (Med codes) | Trigger factor for seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1780267013 (Med codes) | Epilepsy medication review | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1780375016 (Med codes) | Epilepsy care arrangement | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 178739011 (Med codes) | Epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1855731000006116 (Med codes) | Epilepsy monitoring administration | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1855741000006114 (Med codes) | Epilepsy monitoring in primary care | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1855761000006113 (Med codes) | Epilepsy monitoring in secondary care | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1856761000006115 (Med codes) | Epilepsy treatment compliance | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1856771000006110 (Med codes) | Epilepsy treatment compliance good | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1856781000006113 (Med codes) | Epilepsy treatment compliance poor | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1856791000006111 (Med codes) | Epilepsy monitoring default | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 1879221000006113 (Med codes) | H/O: seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 199568011 (Med codes) | Grand mal seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2014871000006119 (Med codes) | Contraceptive advice for patients on valproate for epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 212911000006116 (Med codes) | Prader-Willi syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 212921000006112 (Med codes) | Prader-Willi Syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159216019 (Med codes) | Epilepsy severity | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159218018 (Med codes) | 1 to 12 seizures a year | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159219014 (Med codes) | 2 to 4 seizures a month | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159220015 (Med codes) | 1 to 7 seizures a week | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159221016 (Med codes) | Daily seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159222011 (Med codes) | Many seizures a day | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159223018 (Med codes) | Emergency epilepsy treatment since last appointment | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159227017 (Med codes) | Epilepsy confirmed | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2159274014 (Med codes) | Complex partial epileptic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2193821000000118 (Med codes) | Dravet syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 223781000000116 (Med codes) | Unverricht - Lundborg disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 223811000000118 (Med codes) | Generalised epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 230321000006117 (Med codes) | Petit mal (minor) epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 23819016 (Med codes) | Grand mal status | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 23820010 (Med codes) | Status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2444841000000117 (Med codes) | Paediatric epilepsy care plan | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 245341000006117 (Med codes) | Localisation-related epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 245351000006115 (Med codes) | Partial epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 245361000006118 (Med codes) | Partial epilepsy without impairment of consciousness OS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2466801000000118 (Med codes) | At risk of sudden unexpected death in epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2474650018 (Med codes) | Stress-induced epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2478828012 (Med codes) | Traumatic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2502351000006114 (Med codes) | Epilepsia partialis continua | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2502391000006115 (Med codes) | Focal status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 251269010 (Med codes) | Witnessed epileptic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 251644018 (Med codes) | H/O: epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 253231000006116 (Med codes) | Otohara syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 254809018 (Med codes) | O/E - a seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 254811010 (Med codes) | O/E - a fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 254813013 (Med codes) | O/E - grand mal fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 254814019 (Med codes) | O/E - petit mal fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 254819012 (Med codes) | O/E - psychomotor fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2548491016 (Med codes) | Epilepsy monitoring verbal invite | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2550890017 (Med codes) | Generalised non-convulsive epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2564321000006112 (Med codes) | Complex partial seizure with impairment of consciousness | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2564351000006115 (Med codes) | Complex partial seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2572611000006114 (Med codes) | Generalised-onset seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2572621000006118 (Med codes) | Generalized-onset seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2589101000000111 (Med codes) | SUDEP - sudden unexpected death in epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2598871000006114 (Med codes) | JME - Juvenile myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2598971000006115 (Med codes) | Clonic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2612101000006119 (Med codes) | Petit mal status | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2612111000006116 (Med codes) | Epileptic absence status | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2612121000006112 (Med codes) | Non-convulsive status epilepticus with impaired consciousness | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264629018 (Med codes) | Epilepsy monitoring | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264630011 (Med codes) | Initial epilepsy assessment | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264631010 (Med codes) | Follow-up epilepsy assessment | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264634019 (Med codes) | Epilepsy associated problems | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264637014 (Med codes) | Epilepsy drug side effect | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264638016 (Med codes) | Epilepsy treatment changed | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264639012 (Med codes) | Epilepsy treatment started | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264640014 (Med codes) | Epilepsy treatment stopped | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 264645016 (Med codes) | Epilepsy monitoring NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2692343011 (Med codes) | Seen in epilepsy clinic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2711131000006112 (Med codes) | Postseizure headache | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2721471000006114 (Med codes) | Convulsive status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2730021000006111 (Med codes) | Visual seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2746121000006114 (Med codes) | Benign focal epilepsy of childhood | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2811081000006110 (Med codes) | Generalized epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2815521000006118 (Med codes) | Sturge-Weber disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2826531000006116 (Med codes) | Secondarily generalised seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2872771000006114 (Med codes) | Atypical absence seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 296991018 (Med codes) | Cerebral degeneration in Niemann-Pick disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297060016 (Med codes) | Myoclonic encephalopathy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297107018 (Med codes) | Dyssynergia cerebellaris myoclonica | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297266016 (Med codes) | Epileptic seizures - atonic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297267013 (Med codes) | Epileptic seizures - akinetic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297281010 (Med codes) | Neonatal myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297282015 (Med codes) | Epileptic seizures - clonic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297283013 (Med codes) | Epileptic seizures - myoclonic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297284019 (Med codes) | Epileptic seizures - tonic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297289012 (Med codes) | Other specified generalised convulsive epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297290015 (Med codes) | Generalised convulsive epilepsy NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297295013 (Med codes) | Partial epilepsy with impairment of consciousness | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297296014 (Med codes) | Temporal lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297300010 (Med codes) | Psychosensory epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297302019 (Med codes) | Epileptic automatism | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297303012 (Med codes) | Partial epilepsy with impairment of consciousness NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297311019 (Med codes) | Somatosensory epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297312014 (Med codes) | Partial epilepsy with autonomic symptoms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297313016 (Med codes) | Visceral reflex epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297314010 (Med codes) | Visual reflex epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297315011 (Med codes) | Unilateral epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297320011 (Med codes) | Infantile spasms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297321010 (Med codes) | Kojevnikov's epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297324019 (Med codes) | Other forms of epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297325018 (Med codes) | Cursive (running) epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 297330019 (Med codes) | Other forms of epilepsy NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2978981000006119 (Med codes) | Partial seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2978991000006116 (Med codes) | Partial seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2979001000006116 (Med codes) | Focal seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 2982351000006119 (Med codes) | Dysmnesic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 299334015 (Med codes) | [X]Other generalized epilepsy and epileptic syndromes | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 299336018 (Med codes) | [X]Other epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 299337010 (Med codes) | [X]Other status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 299345017 (Med codes) | [X]Status epilepticus, unspecified | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3011621000006111 (Med codes) | Post-seizure state | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 301541000000116 (Med codes) | Simple partial epileptic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 307861000000113 (Med codes) | Epilepsy monitoring call first letter | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 307881000000116 (Med codes) | Epilepsy monitoring call second letter | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 307901000000118 (Med codes) | Epilepsy monitoring call third letter | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3093151000006111 (Med codes) | Idiopathic generalised epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3093161000006113 (Med codes) | Idiopathic generalized epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3093171000006118 (Med codes) | Primary generalised epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3101911000006116 (Med codes) | Myoclonic seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3168891000006111 (Med codes) | Anoxic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 317021010 (Med codes) | Reflex anoxic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3182921000006118 (Med codes) | Atonic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3182931000006115 (Med codes) | Atonic seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3199231000006115 (Med codes) | EEG abnormality with seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3210941000006113 (Med codes) | Temporal-central focal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3210951000006110 (Med codes) | Centrotemporal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3303481000006114 (Med codes) | Simple partial onset seizure followed by impaired consciousness | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3323851000006114 (Med codes) | Childhood absence epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3341091000006114 (Med codes) | Tonic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 33473011 (Med codes) | Sturge-Weber syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3367371000006110 (Med codes) | Startle partial seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3379241000006110 (Med codes) | Tonic-clonic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3379251000006112 (Med codes) | Tonic-clonic seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 344986017 (Med codes) | Rasmussen syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345138018 (Med codes) | Aicardi Goutieres syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345225017 (Med codes) | Focal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345275015 (Med codes) | Juvenile absence epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345281011 (Med codes) | Lennox-Gastaut syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345293019 (Med codes) | Lafora disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345302015 (Med codes) | Ohtahara syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345307014 (Med codes) | Seizures in response to acute event | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345311015 (Med codes) | Severe myoclonic epilepsy in infancy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345318014 (Med codes) | Drug-induced epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345321011 (Med codes) | Menstrual epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345323014 (Med codes) | Nocturnal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 345345010 (Med codes) | Complex partial status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3498881000006114 (Med codes) | Simple partial seizure evolving to generalised seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3506708010 (Med codes) | Pyridoxine-dependent epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3507781000006110 (Med codes) | Kufs type neuronal ceroid lipofuscinosis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3510617017 (Med codes) | Intractable idiopathic partial epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3511291019 (Med codes) | Recurrent complex partial epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3527840015 (Med codes) | Seizure disorder clinical management plan | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3618451000006117 (Med codes) | Epileptic vertigo | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 362161000006110 (Med codes) | Acquired epileptic aphasia | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3668321000006119 (Med codes) | Symptomatic generalised epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3668331000006116 (Med codes) | Symptomatic generalized epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3668341000006114 (Med codes) | Secondary generalized epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 368296019 (Med codes) | Generalised seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3719651000006117 (Med codes) | Post-traumatic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3719661000006115 (Med codes) | PTE - Post-traumatic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3750051000006112 (Med codes) | Angelman syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3759931000006112 (Med codes) | Unclassified epileptic seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3790311000006116 (Med codes) | Simple partial seizure, consciousness not impaired | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3795091000006119 (Med codes) | Petit-mal seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3796891000006117 (Med codes) | Reflex epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3796901000006118 (Med codes) | Sensory-induced epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 379901000006113 (Med codes) | [X]Epileptic psychosis NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3840421000006110 (Med codes) | Simple partial seizure with motor dysfunction | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3840431000006113 (Med codes) | Simple partial seizures with motor signs | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3862731000006112 (Med codes) | Abdominal seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3878481000006113 (Med codes) | Epileptic disorder | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3878491000006111 (Med codes) | Epileptic | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3878501000006115 (Med codes) | EP - Epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3921961000006111 (Med codes) | Neonatal seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 395221000006119 (Med codes) | [X]Limbic epilepsy personality | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 3955151000006114 (Med codes) | Gelastic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 399395015 (Med codes) | Progressive myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 399408014 (Med codes) | Epilepsy NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 402500015 (Med codes) | O/E - focal (Jacksonian) fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 402501016 (Med codes) | O/E - focal fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 402502011 (Med codes) | O/E - Jacksonian fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4052921000006118 (Med codes) | Photogenic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 406781000000119 (Med codes) | Epilepsy monitoring telephone invite | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 424971000006111 (Med codes) | Rett syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 425631000006118 (Med codes) | [X]Schizophrenia-like psychosis in epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4411881000006115 (Med codes) | Focal motor seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4411891000006117 (Med codes) | Seizure disorder | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 450602015 (Med codes) | Motor epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 450603013 (Med codes) | Jacksonian, focal or motor epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 453344019 (Med codes) | Epileptic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4540141000006110 (Med codes) | History of epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 459233015 (Med codes) | Epilepsy control good | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 459234014 (Med codes) | Epilepsy control poor | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 46968015 (Med codes) | West syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 46969011 (Med codes) | Infantile spasms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 46970012 (Med codes) | Hypsarrhythmia | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 46971011 (Med codes) | Salaam attacks | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 46972016 (Med codes) | Lightning spasms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 472410017 (Med codes) | Tonic-clonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 472411018 (Med codes) | Grand mal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4755771000006114 (Med codes) | Epileptic drop attack | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4769541000006119 (Med codes) | Benign myoclonic epilepsy in infancy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4769611000006117 (Med codes) | TLE - Temporal lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4769641000006118 (Med codes) | Mesiobasal limbic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 4769691000006110 (Med codes) | Complex partial seizures with automatisms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 477355017 (Med codes) | Psychomotor epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 478024019 (Med codes) | Alcohol-induced epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 485041012 (Med codes) | Post-ictal state | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 486701019 (Med codes) | Myoclonic seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 495804010 (Med codes) | Pykno-epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 500033015 (Med codes) | Generalised convulsive epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5004721000006111 (Med codes) | Rasmussen encephalitis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007101000006111 (Med codes) | Benign frontal epilepsy of childhood | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007121000006118 (Med codes) | Benign atypical partial epilepsy in childhood | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007131000006115 (Med codes) | Epilepsy with recurrent unilateral seizures in children | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007141000006113 (Med codes) | Childhood epilepsy with occipital paroxysms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007171000006117 (Med codes) | Benign occipital epilepsy of childhood - early onset variant | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007201000006118 (Med codes) | Primary inherited reading epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007211000006115 (Med codes) | Localisation-related symptomatic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007261000006117 (Med codes) | Frontal lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007291000006113 (Med codes) | Anterior frontopolar epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007321000006116 (Med codes) | Opercular epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007351000006113 (Med codes) | Parietal lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007361000006110 (Med codes) | Occipital lobe epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007441000006115 (Med codes) | Localisation-related cryptogenic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007541000006119 (Med codes) | Epilepsy with grand mal seizures on awakening | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007551000006117 (Med codes) | Cryptogenic generalised epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007621000006113 (Med codes) | Myoclonic astatic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007661000006119 (Med codes) | Myoclonic absence epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007681000006112 (Med codes) | Unverricht-Lundborg syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007771000006116 (Med codes) | Cryptogenic myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007781000006118 (Med codes) | Idiopathic myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007811000006116 (Med codes) | Symptomatic myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007821000006112 (Med codes) | Situation-related seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007841000006117 (Med codes) | Isolated seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007861000006118 (Med codes) | Seizure with provoking factor | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007871000006113 (Med codes) | Epilepsy undetermined whether focal or generalised | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007921000006115 (Med codes) | Landau-Kleffner syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007941000006110 (Med codes) | Epilepsy with continuous spike wave during slow-wave sleep | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5007971000006119 (Med codes) | Secondary reading epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5008031000006115 (Med codes) | Sleep-related epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5008101000006110 (Med codes) | Eating epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5008211000006119 (Med codes) | Non-convulsive status epilepticus without three per second spike wave | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5008231000006113 (Med codes) | Non-convulsive simple partial status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5023531000006114 (Med codes) | Epileptic psychosis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 504081000006111 (Med codes) | Batten's disease of retina | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 504161016 (Med codes) | Absence seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5067711000006114 (Med codes) | Triple X syndrome, epilepsy, and hypogammaglobulinaemia | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 512000013 (Med codes) | Photosensitive epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5192381000006111 (Med codes) | Epilepsy monitoring status | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231621000006116 (Med codes) | Simple partial seizure with focal motor signs without march | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231631000006118 (Med codes) | Simple partial seizure with focal motor signs with march | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231671000006115 (Med codes) | Postural seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231681000006117 (Med codes) | Phonatory seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231721000006112 (Med codes) | Affective seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231761000006118 (Med codes) | Simple partial onset of seizure with automatisms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231791000006114 (Med codes) | Partial seizure evolving to secondary generalised seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231801000006110 (Med codes) | Partial seizure evolving to secondary generalized seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231831000006119 (Med codes) | Generalized seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231871000006116 (Med codes) | Absence seizure with impairment of consciousness only | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231901000006116 (Med codes) | Absence seizure with atonic components | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5231911000006118 (Med codes) | Absence seizure with tonic components | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5300251000006119 (Med codes) | Generalised epileptiform discharges | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5300261000006117 (Med codes) | Generalized epileptiform discharges | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5300371000006115 (Med codes) | Bilateral periodic epileptiform discharges | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5595011000006117 (Med codes) | Seizure undetermined whether focal or generalised | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 5614161000006114 (Med codes) | Localisation-related idiopathic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 6028641000006114 (Med codes) | Epileptic fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 6221451000006112 (Med codes) | Alcohol-related fit | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 632721000000111 (Med codes) | Panayiotopoulos syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 647301000006112 (Med codes) | Epileptic absences | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 6908751000006116 (Med codes) | Epilepsy monitoring call | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 6997451000006113 (Med codes) | Refractory epilepsia partialis continua | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7069151000006119 (Med codes) | Non-epileptic myoclonus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7237211000006118 (Med codes) | Reflex anoxic seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7265381000006118 (Med codes) | Nonconvulsive status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 72751000006116 (Med codes) | Unverricht - Lundborg disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7277091000006117 (Med codes) | Childhood seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7289921000006116 (Med codes) | Afebrile seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7306821000006113 (Med codes) | Refractory epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7306831000006111 (Med codes) | Intractable epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 73622018 (Med codes) | Benign Rolandic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 736371000006112 (Med codes) | Localization-related(focal)(partial)idiopathic epilepsy and epileptic syndromes with seizures of localised onset | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7366361000006112 (Med codes) | Focal seizure with experiential sensory symptoms | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 743461000006119 (Med codes) | Limbic system epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7512471000006111 (Med codes) | Refractory juvenile myoclonic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 753441000006115 (Med codes) | Kuf's disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 758291000006119 (Med codes) | Jansky-Bielschowsky disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7745101000006111 (Med codes) | Jeavons syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7758091000006113 (Med codes) | X-linked epilepsy with learning disability and behaviour disorder syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7811801000006113 (Med codes) | Developmental delay, epilepsy, neonatal diabetes syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7813691000006118 (Med codes) | Seizure, sensorineural deafness, ataxia, intellectual disability, electrolyte imbalance syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7827461000006112 (Med codes) | Osteogenesis imperfecta, retinopathy, seizures, intellectual disability syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7840671000006115 (Med codes) | Epileptic encephalopathy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7861341000006115 (Med codes) | Epilepsy due to stroke | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7863641000006114 (Med codes) | Epilepsy with mesial temporal sclerosis | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7863681000006115 (Med codes) | Epilepsy co-occurrent and due to dementia | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7952761000006111 (Med codes) | Epilepsy telangiectasia syndrome | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 7955181000006111 (Med codes) | Epilepsy of infancy with migrating focal seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 800721000006115 (Med codes) | Generalised nonconvulsive epilepsy NOS | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8021441000006111 (Med codes) | Intractable absence seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8024691000006119 (Med codes) | Epileptic dementia with behavioural disturbance | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8024981000006113 (Med codes) | Complex partial seizure of frontal lobe | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8025021000006114 (Med codes) | Complex partial epileptic seizure of occipital lobe | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8025041000006119 (Med codes) | Complex partial seizure of temporal lobe | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8025071000006110 (Med codes) | Intractable partial temporal lobe epilepsy with impairment of consciousness | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8031611000006111 (Med codes) | Epilepsy in pregnancy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8037021000006117 (Med codes) | Simple partial seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8053261000006111 (Med codes) | Atypical absence epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8079791000006114 (Med codes) | Epilepsy monitoring telephone invitation | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8089581000006114 (Med codes) | Status epilepticus due to refractory complex partial seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8089721000006118 (Med codes) | Infantile spasms co-occurrent with status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8089731000006115 (Med codes) | Infantile spasms with status epilepticus | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8191681000006117 (Med codes) | Petit-mal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8259581000006110 (Med codes) | Referral for epilepsy review | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8260981000006117 (Med codes) | Under care of epilepsy specialist nurse | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8289731000006113 (Med codes) | Epilepsy annual review | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8289831000006117 (Med codes) | Epilepsy care management | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 8289881000006116 (Med codes) | Epilepsy self-management plan review | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 851121000006117 (Med codes) | Partial epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 883041000006118 (Med codes) | Petit mal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 883061000006119 (Med codes) | Infantile spasms -hysarrythmia | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 897431000006113 (Med codes) | Post traumatic epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 905881000006111 (Med codes) | [RFC] Epilepsy/convulsion | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 916571000006117 (Med codes) | Epilepsy monitoring | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 918561000006111 (Med codes) | Epilepsy associated problems | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 918591000006115 (Med codes) | Epilepsy drug side effects | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 918601000006111 (Med codes) | Nocturnal epilepsy | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 928621000006111 (Med codes) | MELAS - Mitochondrial encephalopathy, lactic acidosis and stroke-like episodes | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 930341000006113 (Med codes) | Seizure free &gt; 12 months | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 931711000006118 (Med codes) | Early infantile epileptic encephalopathy with suppression bursts | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 932141000006111 (Med codes) | Partial complex seizure | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 961751000006110 (Med codes) | Tremors/seizures | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |
| 97154016 (Med codes) | Niemann-Pick disease | Epilepsy, seizure and administration codes CPRD aurum (all) primary care |

Not cached: 700 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH1928 version 4530, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH1928/version/4530/detail/)
