---
reference_id: "HDRUK:PH11"
title: "COPD"
database: "HDR UK Phenotype Library"
source_snapshot: "PH11 version 22"
content_type: "structured_record"
---

# HDRUK:PH11  COPD

**PH11** version 22 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH11 |
| Version | 22 |
| Name | COPD |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Eleanor L Axson, Jennifer K Quint |
| Collections | BREATHE; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; SNOMED CT codes; UKBioBank codes; ICD11 codes |
| Data sources | CPRD GOLD; CPRD Aurum; HES Admitted Patient Care data for CPRD GOLD; HES Admitted Patient Care data for CPRD Aurum; Death Registration data for CPRD GOLD; CPRD Aurum Civil Registrations of Death; UK Biobank |
| Sex | Both |
| Event date range | 01/01/2001 - 31/12/2019 |
| DOI | https://doi.org/10.48533/zwdk-jf93 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/COPD---6bb80220-16f3-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/COPD.cwl |
| Ontology | MONDO:0005002 chronic obstructive pulmonary disease |

## Definition

These codes are not intended to be mandatory, but are to be used as a starting point for the identification of COPD in routine EHR. Each study may differ in the sensitivity and specificity of the coding required.

According to the National Institute for Health and Care Excellence (NICE) guidelines for the diagnosis of COPD, COPD should be suspected in patients over 35 years old who have a risk factor (typically smoking) and at least one symptom. It is therefore recommended that these codes are only utilised in an adult population at least 35 years old with a history of smoking.

https://www.nice.org.uk/guidance/ng115/chapter/Recommendations#diagnosing-copd

Validation of Read Codes for the Identification of COPD in CPRD

"Quint et al. validated a set of Read codes for the identification of COPD in CPRD in 2014. Using diagnostic codes alone, the positive predictive value (PPV) was 86.5% (77.5?92.3%). Requiring a diagnostic code, spirometry measures, and specific medication increased PPV to 89.4% (80.7?94.5%) but reduced case numbers by 10%."

## Publications

- Publications in 2019 using validated Read codes from Quint et al. 2014
- D. Stolz, Kostikas, K., Loefroth, E., Fogel, R., Gutzwiller, F. S., Conti, V., Cao, H., and Clemens, A., ?Differences in COPD exacerbation risk between women and men: analysis from the UK Clinical Practice Research Datalink data?, Chest, 2019."
- M. Pikoula, Quint, J. K., Nissen, F., Hemingway, H., Smeeth, L., and Denaxas, S., ?Identifying clinically important COPD sub-types using data-driven approaches in primary care population based electronic health records?, BMC Med Inform Decis Mak, vol. 19, p. 86, 2019."
- H. R. Whittaker, Mullerova, H., Jarvis, D., Barnes, N. C., Jones, P. W., Compton, C. H., Kiddle, S. J., and Quint, J. K., ?Inhaled corticosteroids, blood eosinophils, and FEV1 decline in patients with COPD in a large UK primary health care setting?, Int J Chron Obstruct Pulmon Dis, vol. 14, pp. 1063-1073, 2019."
- C. I. Bloom, Ricciardi, F., Smeeth, L., Stone, P., and Quint, J. K., ?Predicting COPD 1-year mortality using prognostic predictors routinely measured in primary care?, BMC Med, vol. 17, p. 73, 2019."
- D. Dedman, Coton, S. J., Ghosh, R. E., Meeraus, W., Crim, C., Harvey, C., Amelio, J., and Landis, S. H., ?Treatment Patterns of New Users of Fluticasone Furoate/Vilanterol in Asthma and COPD in UK Primary Care: Retrospective Cohort Study?, Pulmonary Therapy, vol. 5, pp. 81-95, 2019."
- J. D. Chalmers, Poole, C., Webster, S., Tebboth, A., Dickinson, S., and Gayle, A., ?Assessing the healthcare resource use associated with inappropriate prescribing of inhaled corticosteroids for people with chronic obstructive pulmonary disease (COPD) in GOLD groups A or B: an observational study using the Clinical Practice Research Data?, Respir Res, vol. 19, p. 63, 2018."
- Publications in 2019 using Read codes from QOF
- P. Rockenschaub, Jhass, A., Freemantle, N., Aryee, A., Rafiq, M., Hayward, A., and Shallcross, L., ?Opportunities to reduce antibiotic prescribing for patients with COPD in primary care: a cohort study using electronic health records from the Clinical Practice Research Datalink (CPRD)?, J Antimicrob Chemother, 2019."

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:14B3.12 | History of chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:14OX.00 | At risk of chronic obstructive pulmonary diseas exacerbation | COPD - Primary care |
| READ2:663K.00 | Airways obstructn irreversible | COPD - Primary care |
| READ2:66YB.00 | Chronic obstructive pulmonary disease monitoring | COPD - Primary care |
| READ2:66YB000 | Chronic obstructive pulmonary disease 3 monthly review | COPD - Primary care |
| READ2:66YB100 | Chronic obstructive pulmonary disease 6 monthly review | COPD - Primary care |
| READ2:66YB200 | Telehealth chronic obstructive pulmonary disease monitoring | COPD - Primary care |
| READ2:66YD.00 | Chronic obstructive pulmonary disease monitoring due | COPD - Primary care |
| READ2:66YI.00 | Chronic obstructive pulmonary disease self-management plan given | COPD - Primary care |
| READ2:66YL.00 | Chronic obstructive pulmonary disease follow-up | COPD - Primary care |
| READ2:66YL.11 | COPD follow-up | COPD - Primary care |
| READ2:66YM.00 | Chronic obstructive pulmonary disease annual review | COPD - Primary care |
| READ2:66YS.00 | Chronic obstructive pulmonary disease monitoring by nurse | COPD - Primary care |
| READ2:66YT.00 | Chronic obstructive pulmonary disease monitoring by doctor | COPD - Primary care |
| READ2:66Yd.00 | Chronic obstructive pulmonary disease accident and emergency attendance since last visit | COPD - Primary care |
| READ2:66Ye.00 | Emergency chronic obstructive pulmonary disease admission since last appointment | COPD - Primary care |
| READ2:66Yf.00 | Number of chronic obstructive pulmonary disease exacerbations in past year | COPD - Primary care |
| READ2:66Yh.00 | Chronic obstructive pulmonary disease does not disturb sleep | COPD - Primary care |
| READ2:66Yi.00 | Multiple chronic obstructive pulmonary disease emergency hospital admissions | COPD - Primary care |
| READ2:679V.00 | Health education ? chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:6Yg.00 | Chronic obstructive pulmonary disease disturbs sleep | COPD - Primary care |
| READ2:8CMW500 | Chronic obstructive pulmonary disease care pathway | COPD - Primary care |
| READ2:8CR1.00 | Chronic obstructive pulmonary disease clini management plan | COPD - Primary care |
| READ2:9NgP.00 | On chronic obstructive pulmonary disease supportv cre pathway | COPD - Primary care |
| READ2:9NgP.11 | On COPD (chr obstruc pulmonary disease) supportv cre pathway | COPD - Primary care |
| READ2:9Nk7000 | Seen in chronic obstructive pulmonary disease clinic | COPD - Primary care |
| READ2:9Oi..00 | Chronic obstructive pulmonary disease monitoring admin | COPD - Primary care |
| READ2:9Oi0.00 | Chronic obstructive pulmonary disease monitoring 1st letter | COPD - Primary care |
| READ2:9Oi1.00 | Chronic obstructive pulmonary disease monitoring 2nd letter | COPD - Primary care |
| READ2:9Oi2.00 | Chronic obstructive pulmonary disease monitoring 3rd letter | COPD - Primary care |
| READ2:9Oi3.00 | Chronic obstructive pulmonary disease monitoring verb invite | COPD - Primary care |
| READ2:9Oi4.00 | Chronic obstructive pulmonary disease monitor phone invite | COPD - Primary care |
| READ2:H31..00 | Chronic bronchitis | COPD - Primary care |
| READ2:H310.00 | Simple chronic bronchitis | COPD - Primary care |
| READ2:H310000 | Chronic catarrhal bronchitis | COPD - Primary care |
| READ2:H310z00 | Simple chronic bronchitis NOS | COPD - Primary care |
| READ2:H311.00 | Mucopurulent chronic bronchitis | COPD - Primary care |
| READ2:H311000 | Purulent chronic bronchitis | COPD - Primary care |
| READ2:H311100 | Fetid chronic bronchitis | COPD - Primary care |
| READ2:H311z00 | Mucopurulent chronic bronchitis NOS | COPD - Primary care |
| READ2:H312.00 | Obstructive chronic bronchitis | COPD - Primary care |
| READ2:H312000 | Chronic asthmatic bronchitis | COPD - Primary care |
| READ2:H312011 | Chronic wheezy bronchitis | COPD - Primary care |
| READ2:H312100 | Emphysematous bronchitis | COPD - Primary care |
| READ2:H312200 | Acute exacerbation of chronic obstructive airways disease | COPD - Primary care |
| READ2:H312300 | Bronchiolitis obliterans | COPD - Primary care |
| READ2:H312z00 | Obstructive chronic bronchitis NOS | COPD - Primary care |
| READ2:H313.00 | Mixed simple and mucopurulent chronic bronchitis | COPD - Primary care |
| READ2:H31y.00 | Other chronic bronchitis | COPD - Primary care |
| READ2:H31y100 | Chronic tracheobronchitis | COPD - Primary care |
| READ2:H31yz00 | Other chronic bronchitis NOS | COPD - Primary care |
| READ2:H31z.00 | Chronic bronchitis NOS | COPD - Primary care |
| READ2:H32..00 | Emphysema | COPD - Primary care |
| READ2:H320.00 | Chronic bullous emphysema | COPD - Primary care |
| READ2:H320000 | Segmental bullous emphysema | COPD - Primary care |
| READ2:H320100 | Zonal bullous emphysema | COPD - Primary care |
| READ2:H320200 | Giant bullous emphysema | COPD - Primary care |
| READ2:H320300 | Bullous emphysema with collapse | COPD - Primary care |
| READ2:H320z00 | Chronic bullous emphysema NOS | COPD - Primary care |
| READ2:H321.00 | Panlobular emphysema | COPD - Primary care |
| READ2:H322.00 | Centrilobular emphysema | COPD - Primary care |
| READ2:H32y.00 | Other emphysema | COPD - Primary care |
| READ2:H32y000 | Acute vesicular emphysema | COPD - Primary care |
| READ2:H32y100 | Atrophic (senile) emphysema | COPD - Primary care |
| READ2:H32y111 | Acute interstitial emphysema | COPD - Primary care |
| READ2:H32y200 | MacLeod's unilateral emphysema | COPD - Primary care |
| READ2:H32yz00 | Other emphysema NOS | COPD - Primary care |
| READ2:H32yz11 | Sawyer-Jones syndrome | COPD - Primary care |
| READ2:H32z.00 | Emphysema NOS | COPD - Primary care |
| READ2:H36..00 | Mild chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:H37..00 | Moderate chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:H38..00 | Severe chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:H39..00 | Very severe chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:H3?00 | Chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:H3?11 | Chronic obstructive airways disease | COPD - Primary care |
| READ2:H3A..00 | End stage chronic obstructive airways disease | COPD - Primary care |
| READ2:H3B..00 | Asthma-chronic obstructive pulmonary disease overlap syndrome | COPD - Primary care |
| READ2:H3y..00 | Other specified chronic obstructive airways disease | COPD - Primary care |
| READ2:H3y..11 | Other specified chronic obstructive pulmonary disease | COPD - Primary care |
| READ2:H3y0.00 | Chronic obstruct pulmonary dis with acute lower resp infectn | COPD - Primary care |
| READ2:H3y1.00 | Chron obstruct pulmonary dis wth acute exacerbation, unspec | COPD - Primary care |
| READ2:H3z..00 | Chronic obstructive airways disease NOS | COPD - Primary care |
| READ2:H3z..11 | Chronic obstructive pulmonary disease NOS | COPD - Primary care |
| READ2:H464000 | Chronic emphysema due to chemical fumes | COPD - Primary care |
| READ2:H464100 | Obliterative bronchiolitis due to chemical fumes | COPD - Primary care |
| READ2:H583200 | Eosinophilic bronchitis | COPD - Primary care |
| READ2:Hyu3000 | [X]Other emphysema | COPD - Primary care |
| READ2:Hyu3100 | [X]Other specified chronic obstructive pulmonary disease | COPD - Primary care |
| 1112 (UKBioBank codes) | Chronic obstructive airways disease/COPD | COPD - UK Biobank |
| 1113 (UKBioBank codes) | Emphysema/chronic bronchitis | COPD - UK Biobank |
| 1472 (UKBioBank codes) | Emphysema | COPD - UK Biobank |
| ICD10:J43 | Emphysema | COPD - Mortality |
| ICD10:J44 | Other chronic obstructive pulmonary disease | COPD - Mortality |
| ICD10:J43 | Emphysema | COPD - Secondary care - Diagnoses |
| ICD10:J44 | Other chronic obstructive pulmonary disease | COPD - Secondary care - Diagnoses |
| CA22 (ICD11 codes) | Chronic obstructive pulmonary disease | COPD - Secondary care - Diagnoses |

Not cached: 65 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH11 version 22, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH11/version/22/detail/)
