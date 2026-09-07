---
reference_id: DOI:10.1038/s41598-023-50722-z
title: Development and validation of a prognostic nomogram for predicting in-hospital mortality of patients with acute paraquat poisoning
authors:
- Guo Tang
- Zhen Jiang
- Lingjie Xu
- Ying Yang
- Sha Yang
- Rong Yao
journal: Scientific Reports
year: '2024'
doi: 10.1038/s41598-023-50722-z
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41598-023-50722-z.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41598-023-50722-z.pdf
---

# Development and validation of a prognostic nomogram for predicting in-hospital mortality of patients with acute paraquat poisoning
**Authors:** Guo Tang, Zhen Jiang, Lingjie Xu, Ying Yang, Sha Yang, Rong Yao
**Journal:** Scientific Reports (2024)
**DOI:** [10.1038/s41598-023-50722-z](https://doi.org/10.1038/s41598-023-50722-z)

## Content

AbstractThis study aimed to develop and validate a predictive model to determine the risk of in-hospital mortality in patients with acute paraquat poisoning. This retrospective observational cohort study included 724 patients with acute paraquat poisoning whose clinical data were collected within 24 h of admission. The primary outcome was in-hospital mortality. Patients were randomly divided into training and validation cohorts (7/3 ratio). In the training cohort, the least absolute shrinkage and selection operator regression models were used for data dimension reduction and feature selection. Multivariate logistic regression was used to generate a predictive nomogram for in-hospital mortality. The prediction model was assessed for both the training and validation cohorts. In the training cohort, decreased level of consciousness (Glasgow Coma Scale score < 15), neutrophil-to-lymphocyte ratio, alanine aminotransferase, creatinine, carbon dioxide combining power, and paraquat plasma concentrations at admission were identified as independent predictors of in-hospital mortality in patients with acute paraquat poisoning. The calibration curves, decision curve analysis, and clinical impact curves indicated that the model had a good predictive performance. It can be used on admission to the emergency department to predict mortality and facilitate early risk stratification and actionable measures in clinical practice after further external validation.

1
Vol.:(0123456789)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports
Development and validation 
of a prognostic nomogram 
for predicting in‑hospital mortality 
of patients with acute paraquat 
poisoning
Guo Tang 1,2, Zhen Jiang 1,2, Lingjie Xu 1, Ying Yang 1, Sha Yang 1 & Rong Yao 1*
This study aimed to develop and validate a predictive model to determine the risk of in‑hospital 
mortality in patients with acute paraquat poisoning. This retrospective observational cohort study 
included 724 patients with acute paraquat poisoning whose clinical data were collected within 24 h 
of admission. The primary outcome was in‑hospital mortality. Patients were randomly divided into 
training and validation cohorts (7/3 ratio). In the training cohort, the least absolute shrinkage and 
selection operator regression models were used for data dimension reduction and feature selection. 
Multivariate logistic regression was used to generate a predictive nomogram for in‑hospital mortality. 
The prediction model was assessed for both the training and validation cohorts. In the training 
cohort, decreased level of consciousness (Glasgow Coma Scale score < 15), neutrophil‑to‑lymphocyte 
ratio, alanine aminotransferase, creatinine, carbon dioxide combining power, and paraquat plasma 
concentrations at admission were identified as independent predictors of in‑hospital mortality in 
patients with acute paraquat poisoning. The calibration curves, decision curve analysis, and clinical 
impact curves indicated that the model had a good predictive performance. It can be used on 
admission to the emergency department to predict mortality and facilitate early risk stratification and 
actionable measures in clinical practice after further external validation.
Paraquat (1,1′-dimethyl-4,4′-bipyridinium dichloride [PQ]) is a non-selective contact herbicide widely used in 
many countries since the  1960s1. Acute PQ poisoning (APP) has been associated with suicides and accidents, 
with PQ causing sequential organ damage/failure through oxidative stress and systemic inflammatory responses. 
The most prominent manifestations include acute lung and kidney  injuries2. The mortality rate of patients with 
APP remains tremendously high (50–90%)3–6. Consequently, PQ has been banned in most countries, including 
China. However, PQ is still legally used in some  areas7,8.
Early assessment of the severity and prognosis of patients with APP is crucial to guide treatment (hemodilu-
tion, immunosuppressive therapy)9,10. Currently, no standardized method exists for predicting the prognosis of 
APP . Previous studies have demonstrated the utility of the Severity Index of PQ Poisoning (SIPP) as a specific 
scoring system for prognosticating  APP11. However, calculating the SIPP score necessitates the measurement of 
serum PQ concentration, which demands costly equipment. Consequently, its usage is limited in most countries, 
particularly in developing  nations12,13. Furthermore, research indicates that the SIPP score might overestimate the 
survival rate of patients with  APP14, especially those admitted to the hospital more than 24 h after  poisoning15. 
Prior research has identified complete blood cell  count16, liver and kidney function  indicators17, serum anion 
 gap18,19, and chest computed  tomography20 as independent prognostic indicators for APP . Nevertheless, these 
indicators are relatively individualistic and demonstrate limited predictive power. The currently available scor-
ing systems for predicting patient prognosis, including the Acute Physiology and Chronic Health Evaluation II 
(APACHE II)  score21, Sequential Organ Failure Assessment (SOFA)  score22, and Poisoning Severity Score (PSS)23, 
are designed for critically ill patients rather than individuals with low exposure or mild symptoms.
OPEN
1Emergency Medicine Laboratory and the Department of Emergency, West China Hospital, Sichuan University, No. 
37 Guoxue Alley, Chengdu 610041, Sichuan, China. 2These authors contributed equally: Guo Tang and Zhen Jiang. 
*email: yaorong@wchscu.cn

2
Vol:.(1234567890)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
Furthermore, due to the intricate calculation process, these scoring systems are incapable of promptly predict-
ing the mortality rate or conducting risk assessments for PQ poisoning  patients24. Accordingly, it is imperative to 
develop an efficient, straightforward, and universally applicable predictive model based on commonly employed 
laboratory indicators. A nomogram is a simple multivariate prediction model that incorporates multiple vari -
ables affecting prognosis to calculate an individual’s survival  probability25. Therefore, this study aims to develop 
a nomogram model based on clinical data collected within 24 h of admission that can identify, at an early stage, 
patients who are at high risk of in-hospital mortality due to APP .
Methods
Setting
We performed a retrospective, observational cohort study in an emergency department (ED) with more than 
3000 beds in an extensive tertiary care teaching hospital in Chengdu City, Sichuan Province, China, per the 
amended Declaration of Helsinki. The West China Hospital approved the study of the Sichuan University Bio-
medical Research Ethics Committee (No. 2022-1591). Due to the retrospective nature of the study, the need of 
informed consent was waived by the Sichuan University Biomedical Research Ethics Committee. All analyses 
were performed following the Transparent Reporting of a multivariate prediction model for Individual Prognosis 
or Diagnosis  statement26.
Patients
We conducted a study involving patients diagnosed with APP who were admitted to the ED of West China 
Hospital, Sichuan University, between September 1, 2010, and January 31, 2022. Inclusion criteria comprised of 
patients aged ≥ 14 years, those with poisoning via gastrointestinal intake, and individuals with PQ plasma con -
centrations ≥ 0.01 mg/L by high-performance liquid chromatography. Exclusion criteria encompassed patients 
whose PQ concentrations were not detected in the plasma, those with incomplete clinical data, those with other 
concomitant poisoning (such as alcohol poisoning), and pregnant women.
For patients who developed symptoms within 6 h of onset, gastric lavage was recommended. Those who 
developed symtoms within 12 h of onset were administered activated charcoal via oral or nasogastric route. 
Patients with positive concentrations of PQ in blood tests were advised to undergo blood purification treatment, 
including blood perfusion, hemodialysis, or continuous venovenous hemofiltration. After excluding contraindi-
cations such as gastrointestinal bleeding, all patients should be given methylprednisolone sodium succinate at a 
dosage of 80 mg/day for anti-inflammatory treatment through intravenous  infusion27.
Predictors
We collected anonymous clinical data within 24 h of admission to the Emergency Department (ED) from elec-
tronic medical records. The collected data comprised the following variables: time from poisoning to treatment 
at the study site, sex, age, level of consciousness (LOC), heart rate (HR), respiration rate (RR), systolic blood 
pressure (SBP), diastolic blood pressure (DBP), white blood cell (WBC) count, neutrophil-to-lymphocyte ratio 
(NLR), monocyte-to-lymphocyte ratio (MLR), platelet count (PLT), total bilirubin, alanine aminotransferase 
(ALT), aspartate aminotransferase (AST), alkaline phosphatase (ALP), blood urea nitrogen (BUN), creatinine, 
cystatin C, carbon dioxide combining power (CO2CP), blood potassium, plasma PQ concentrations, and SIPP . 
Carbon dioxide combining power (CO2CP) measures a substance or solution’s ability to react with and bind 
carbon dioxide  (CO2) molecules. It quantifies the substance’s capacity to combine with  CO2 chemically. The 
normal range of CO2CP typically falls between 22 and 30 milliequivalents per liter (mEq/L) 28. Decreased LOC 
is defined as a Glasgow Coma Scale (GCS) score below  1529. The severity of PQ poisoning was estimated quanti-
tatively by using the SIPP , which was calculated by multiplying the elapsed time (hours) from ingestion to arrival 
by the serum PQ level(μg/ml) 11. All patient data were anonymized and de-identified. Variables were treated as 
continuous variables, except for sex and disturbance of consciousness, which were binary variables. Finally, the 
continuous variables used to construct the nomogram were transformed into categorical variables based on 
the actual data. This was achieved by categorizing them based on the normal upper and lower bounds, median, 
tertiles, and quartiles.
Clinical outcome
The patients were divided into two groups: survivor and non-survivor group, according to the occurrence of 
in-hospital death. The in-hospital mortality discussed in this study refers to all-cause mortality of APP patients, 
including deaths in the ED.
Statistical analysis
Data were analyzed using R version 4.2.1 (R Foundation for Statistical Computing, Vienna, Austria). A two-
sided P value < 0.05 indicated statistical significance. Data are presented as medians (interquartile ranges) for 
continuous variables and as numbers (percentages) for categorical variables, as appropriate. The non-parametric 
Mann–Whitney U test, chi-square analysis, and Fisher’s exact test were used to test for differences between 
groups, as appropriate. In this study, grouping was achieved through simple random non-relaxation sampling 
using the simple_ra() function in the R software. All the baseline characteristics were comparable between the 
training and validation cohorts.
In the training cohort, the least absolute shrinkage and selection operator (LASSO) regression was used to 
decrease the potential collinearity of variables assessed from the same patient and the overfitting of variables. The 
latent variables in the LASSO regression analysis were included in the multivariate analysis of stepwise forward 
selection to determine independent risk factors affecting in-hospital mortality. The results are reported as odds 

3
Vol.:(0123456789)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
ratios (ORs) and 95% confidence intervals (95% CI). A simple nomogram based on the independent risk factors 
was developed to predict the probability of mortality. The prediction model was assessed using the concordance 
index (C-index), area under the receiver operating characteristic (ROC) curve (AUC), calibration curves, deci-
sion curve analysis (DCA), and clinical impact curves for both the training and validation  cohorts30–32.
Results
Patients
A total of 1708 patients with APP presented to our ED, of whom 984 were excluded. Finally, 724 patients who 
met the inclusion criteria in this study were randomly divided into two groups: training and validation cohorts 
group using a 7:3 ratio (Fig.  1); among them, 360/724 patients (49.7%) died. In terms of demographics, there 
were 325/724 (44.9%) males, with a median age of 33 (23–42) years. Among 506/724 patients in the training 
group, 44.1% were male, with a median age of 29 (22–42) years, and 253/506 (50%) patients died. Of the 218/724 
patients in the validation group, 46.8% were male, with a median age of 31 (23–42) years, and 107/218 (49.1%) 
patients died. No statistical significant differences were observed between the two groups ( P > 0.05) (Table 1).
Model development
In the demographic and clinical characteristics analysis of 506 patients, 22 features were reduced to nine potential 
predictive features. These features had non-zero coefficients in the LASSO regression model, which included age, 
LOC, WBC count, NLR, MLR, ALT, creatinine,  CO2CP , and plasma PQ concentrations (Fig. 2a,b).
Construction of nomogram
Multivariate analysis revealed several independent risk factors for in-hospital mortality upon admission, includ-
ing decreased LOC, NLR, ALT, creatinine,  CO2CP , and plasma PQ concentrations. The detailed ORs and 95% 
CI of the multivariate analysis are summarized in Table 2.
Therefore, these six factors were used to construct the prediction model, as shown in Table 2. A simple nomo-
gram was developed to predict the probability of death based on the independent risk factors (Fig. 3a). The NLR 
values were categorized into quartiles as follows: category 1 for NLR < 6.2, category 2 for NLR 6.2–10.94, category 
3 for NLR 10.94–18.02, and category 4 for NLR > 18.02. ALT values were categorized based on the upper limit of 
normal as category 1 for ALT 0–39 IU/L and category 2 for ALT ≥ 40 IU/L. Additionally, categorical variables were 
created based on the median value of creatinine, resulting in category 1 for creatinine ≤ 110 μmol/L and category 
2 for creatinine > 110 μmol/L. Finally, PQ values were categorized into quartiles: category 1 for PQ ≤ 0.33 g/mL, 
category 2 for PQ 0.33–1.66 g/mL, category 3 for PQ 1.66–11.15 g/mL, and category 4 for PQ  > 11.15 g/mL. As 
shown in the nomogram, each factor was assigned a point, and the total nomogram points were calculated by 
summing the individual points of all predictors. The relationship between the total points and the probability 
of death is presented at the bottom of the nomogram. As an example, CO2CP was considered as a continuous 
variable. Where a decrease of 5 units corresponded to an approximate 35 points increase in the risk score. The 
nomogram depicts the predicted probability of in-hospital death resulting from APP , measured on a scale of 0 
to 300. Draw a vertical line upward and assign labels to signify the respective points for each covariate. Repeated 
this procedure for each covariate to ascertain the cumulative.
Assessment of nomogram
The calibration curve in Fig. 3b,c suggests high consistency, demonstrating that the model’s predicted probabili-
ties are close to the observed actual probabilities. The bias-corrected C-indices for the training and validation 
cohorts were 0.933 and 0.947, respectively.
Figure 1.  Flowchart of the study.

4
Vol:.(1234567890)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
In the training and validation cohorts, the C-indices were 0.953 (95% CI 0.936–0.970) and 0.947 (95% CI 
0.920–0.974), respectively, indicating excellent accuracy. The ROC curves and AUC for the training and valida-
tion cohorts are shown in Fig. 4a,b. The DCA demonstrated that the nomogram had a superior overall net benefit 
across a wide range of practical threshold probabilities (Fig. 5a,b). In addition, we plotted clinical impact curves 
to predict improved probability stratification for a population size of 1000. The predicted probability coincided 
with the actual probability in the training and validation cohorts (Fig. 5c,d).
Construction and comparison of other predictive models
Since plasma PQ concentrations accounted for much of the model and some primary hospitals could not detect 
them, we used LASSO and multivariate logistic regression to construct another model without PQ plasma con-
centrations. Finally, we determined the following independent risk factors: LOC, age, WBC count, MLR, ALT 
Plasma PQ concentrations, and  CO2CP . Concurrently, we included the SIPP to compare the effectiveness of the 
three prediction models and construct the ROC curve (Fig.  6).
Discussion
Timely identification of the severity of patients with PQ poisoning is of utmost importance in clinical practice. It 
assists in formulating targeted treatment plans, allocating medical resources efficiently, and potentially enhancing 
patient prognosis. Nevertheless, currently, no universally accepted method exists to comprehensively evaluate 
the correlation between clinical indicators and the survival outcomes of patients with APP . This study bridges 
this gap by developing a prediction model that evaluates the risk of in-hospital mortality using clinical data col-
lected during admission. The created nomogram exhibited exceptional performance in both the training and 
validation cohorts, with an AUC exceeding 0.9. The included indicators can be readily acquired upon admission, 
and the nomogram score can be calculated with ease. These characteristics render the model appropriate for 
swift and uncomplicated clinical implementation, facilitating early-stage evaluation and prognosis prediction. 
Its convenience further encourages widespread adoption. Additionally, based on our comprehension, the sample 
size employed in this study is one of the largest worldwide, and the constructed model has achieved near-perfect 
prediction performance. Moreover, after comparing the nomogram to SIPP , we have ascertained the superiority 
of our prediction model.
Prior nomogram models developed to predict the prognosis of APP patients primarily originated from the 
research conducted by Lu Shan. They retrospectively included a total of 80 cases of patients with APP , utilizing 
serological markers and imaging examinations to construct their nomogram. The AUC in their training set and 
validation set were 0.953 (95% CI 0.936–0.970) and 0.947 (95% CI 0.920–0.974), respectively. In comparison to 
Table 1.  Comparison of baseline characteristics between the training and validation cohorts. Values are 
presented as medians [interquartile ranges] or n (%). LOC level of consciousness, GCS glasgow coma scale, 
CO2CP carbon dioxide combining power, PQ paraquat.
Risk factors Training cohort (n = 506) Validation cohort (n = 218) P
Time from poisoning to treatment at the study site (h) 6.00 [3.00, 18.0] 7.00 [3.00, 18.2] 0.760
Sex (male) 223 (44.1) 102 (46.8) 0.500
Age (years) 29 [22,42] 31 [23,42] 0.398
Decreased LOC(GCS < 15) 47 (9.29) 16 (7.34) 0.394
Heart rate (times/min) 84 [74.2, 93] 84 [73, 94] 0.664
Respiration rate (times/min) 20 [20,22] 20 [20,22] 0.941
Systolic blood pressure (mmHg) 120 [111, 132] 118 [109, 128] 0.143
Diastolic blood pressure (mmHg) 75.0 [68.0, 81.8] 74.5 [66.2, 82.0] 0.675
White blood cells (×  109/L) 13.6 [9.67, 20.4] 13.1 [8.67, 19.2] 0.373
Neutrophil-to-lymphocyte ratio 11.0 [6.30, 18.2] 9.66 [5.26, 17.1] 0.142
Monocyte-to-lymphocyte ratio 0.42 [0.25, 0.72] 0.39 [0.23, 0.63] 0.129
Platelets (×  1012/L) 176 [135, 223] 168 [134, 219] 0.540
Total bilirubin (μmol/L) 13.3 [10.0, 18.9] 13.4 [9.50, 20.8] 0.838
Alanine aminotransferase (IU/L) 21.0 [15.0, 34.0] 22.0 [16.0, 38.0] 0.136
Aspartate aminotransferase (IU/L) 27.0 [21.0, 39.0] 28.0 [22.0, 43.8] 0.246
Alkaline phosphatase (IU/L) 77.0 [61.2, 97.0] 77.0 [62.0, 99.8] 0.889
Blood urea nitrogen (mmol/L) 5.96 [4.51, 7.81] 5.97 [4.51, 7.77] 0.832
Creatinine (μmol/L) 99.0 [71.0, 176] 93.0 [70.0, 190] 0.747
Cystatin C (mg/L) 0.76 [0.65, 0.96] 0.80 [0.66, 1.01] 0.146
CO2CP (mmol/L) 18.5 [14.4, 21.5] 18.6 [14.5, 21.1] 0.977
Blood potassium (mmol/L) 3.20 [2.77, 3.56] 3.28 [2.79, 3.68] 0.204
Plasma PQ concentrations (mg/L) 1.63 [0.34, 11.6] 1.64 [0.35, 12.9] 0.870
Mortality 253 (50.0) 107 (49.1) 0.821

5
Vol.:(0123456789)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
Figure 2.  Demographic and clinical feature selection using the LASSO binary logistic regression model. (a) 
Optimal parameter (λ) selection in the LASSO model used 10-fold cross-validation via the minimum criteria. A 
partial likelihood deviance (binomial deviance) curve was plotted against log(λ). Dotted vertical lines are drawn 
at the optimal values using the minimum criteria and 1SE of the minimum criteria (1-SE criteria). (b) LASSO 
coefficient profiles of nine features. A coefficient profile plot was constructed against log(λ) sequence. A vertical 
line was drawn at the value selected using 10-fold cross-validation, where the optimal lambda resulted in eight 
features with non-zero coefficients. LASSO least absolute shrinkage and selection operator, SE standard error.
Table 2.  Risk factors for in-hospital mortality in patients with acute paraquat poisoning. OR odds ratio, CI 
confidence interval, LOC level of consciousness, GCS glasgow coma scale, LR likelihood ratio.
Variable Crude OR (95% CI) Adjusted OR (95% CI) P (Wald’s test) P (LR test)
Decreased LOC(GCS < 15) 9.87 (3.84–25.41) 4.69 (1.3–16.85) 0.018 0.016
White blood cell (×  109/L) 1.2 (1.16–1.25) 1.06 (0.99–1.13) 0.095 0.093
Neutrophil-to-lymphocyte ratio 1.07 (1.05–1.1) 1.05 (1.01–1.09) 0.014 0.011
Alanine amino transferase (IU/L) 1.0029 (1.0006–1.0052) 1.0024 (0.9998–1.0049) 0.07 0.037
Creatinine (μmol/L) 1.0038 (1.0023–1.0053) 1.002 (1.0004–1.0037) 0.017 0.016
Carbon dioxide combining power 0.74 (0.7–0.78) 0.91 (0.84–0.98) 0.013 0.012
Plasma paraquat concentrations (mg/L) 1.68 (1.49–1.9) 1.55 (1.36–1.76) < 0.001 < 0.001

6
Vol:.(1234567890)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
their study, our current study encompasses an expanded sample size, a wider array of accessible indicators and 
demonstrates exceptional predictive capacity.
Our study revealed a high mortality rate in patients with decreased LOC due to APP , possibly related to toxic 
encephalopathy or hyperemia. Previous research has reported that PQ can stimulate glutamate efflux, leading 
to  excitotoxicity33. Animal studies have demonstrated PQ’s ability to induce α-synuclein upregulation, promote 
aggregate formation, and activate  microglial34.
The NLR is a readily detectable inflammation marker using routine blood tests. It has been used to assess 
inflammatory-related lesions such as tumors, ischemic stroke, and coronary artery  disease35–37. Neutrophils are 
important members of the human immune system that have gradually gained attention for their role in APP . 
Studies have shown that PQ can induce rapid expression of neutrophil chemoattractant proteins in bone marrow 
mesenchymal stem cells. Consequently, neutrophils rapidly increase in the blood and accumulate in the lungs, 
promoting the production of chemokines and pro-inflammatory factors (such as tumor necrosis factor α and 
interleukin 8) and activating the inflammatory response. Simultaneously, alveolar macrophages generated by 
neutrophils initiate immune responses and generate reactive oxygen species, leading to cellular nicotinamide 
adenine dinucleotide phosphate (reduced coenzyme II) depletion and cell membrane lipid peroxidation, thereby 
promoting the expression of pro-fibrotic genes in fibroblasts and resulting in pulmonary  fibrosis38,39. Lymphocytes 
play a central role in regulating inflammatory responses in the human body. However, the specific mechanism 
through which PQ induces lymphocyte degradation remains unclear. Whether PQ inhibits the cellular immune 
function requires further investigation.
Figure 3.  (a) Nomogram for in-hospital mortality in patients with acute paraquat poisoning. Decreased 
LOC (GCS score < 15) (0, no; 1, yes), NLR (1, < 6.2; 2, 6.2–10.94; 3, 10.94–18.02; 4, > 18.02), ALT (1, 0–39; 
2, ≥ 40 IU/L), CREA (1, ≤ 110; 2, > 110 µmol/L), PQ (1, ≤ 0.33; 2, 0.33–1.66; 3, 1.66–11.15; 4, ≥ 11.15 g/mL). (b) 
Calibration curve of the nomogram in the training set. (c) Calibration curve in the validation set. LOC level of 
consciousness, GCS glasgow coma scale, NLR neutrophil-to-lymphocyte ratio, ALT alanine aminotransferase, 
CREA creatinine, CO2CP carbon dioxide combining power, PQ paraquat.

7
Vol.:(0123456789)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
Our study showed that liver injury was an independent risk factor for death in patients with APP , which 
contradicts the findings of previous studies showing that toxic hepatitis is common after PQ exposure. Toxic 
hepatitis appears mild and transient in scope but is associated with higher complication rates, including respira-
tory and renal  failure40.
PQ penetration into tissues and organs can cause a series of oxidative stress reactions, generating a large 
amount of reactive oxygen species and leading to organ damage or  failure41. The kidney is the main excretory 
organ for PQ, eliminating 90% of PQ within 12–24 h. Consequently, patients with APP often present with acute 
Figure 4.  ROC curve of the nomogram for the training (a) and validation (b) cohorts. ROC receiver operating 
characteristic, AUC  area under the ROC curve.
Figure 5.  Nomogram decision curve analysis for the training (a) and validation (b) cohorts, and clinical impact 
curves for the training (c) and validation (d) cohorts.

8
Vol:.(1234567890)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
kidney injury characterized by elevated  creatinine42. In addition, renal dysfunction can significantly reduce the 
PQ excretion rate and increase its accumulation in the body, forming a vicious  circle43,44. Further studies are 
needed to confirm whether correcting kidney injury improves prognosis.
CO2CP refers to the plasma  CO2 content measured after isolating plasma from venous blood samples at room 
temperature and balancing it with the alveolar air of healthy  people45. Two major acid–base disturbances, res -
piratory acidosis and metabolic alkalosis, both of which can result in increased  CO2CP , are common in patients 
with respiratory diseases. If respiratory diseases such as chronic obstructive pulmonary diseases are excluded, 
the impact of the respiratory acid–base balance on  CO2CP can be  minimized46. In contrast, reduced  CO2CP 
concentrations suggest metabolic  acidosis47 or respiratory  alkalosis48, both of which are indicators of poor out-
comes. Most often, decreased  CO2CP indicates the presence of metabolic acidosis; however, it could also reflect 
a decline in bicarbonate concentration as compensation for respiratory alkalosis. Therefore, it is considered a 
broad indicator of lung and kidney damage. In this study, the  CO2CP of the mortality group was significantly 
lower than that of the survival group (P  < 0.05). As the lungs and kidneys are important target organs of APP , 
this index can be regarded as a comprehensive evaluation index.
Considering that some primary hospitals cannot detect plasma PQ concentrations, we constructed a predic-
tive model for plasma concentrations without PQ and compared it with SIPP . The second model showed the 
AUC of 0.882 (95% CI 0.853–0.911). Although the performance of the second model is not as good as that of 
the first, it is still worth promoting.
The current study has some limitations. First, it was a single-center retrospective study with selection bias; 
furthermore, only 724 patients were included because of missing data, which may limit the scalability of the 
model. Second, this study only included the clinical data of patients with APP at the time of enrollment and did 
not combine the clinical data after treatment to evaluate patient survival after discharge, which may have affected 
the results. Owing to limitations in clinical data, the GCS classification in this study was restricted to < 15/15. 
However, in future studies, we aim to collect more comprehensive data to improve nomogram precision. Moreo-
ver, because of the severe lack of clinical data and absence of indicators of lung injury, this study was performed 
retrospectively. The model must be updated when more multicenter data become available.
Conclusion
We developed a predictive model for in-hospital mortality in patients with APP . The nomogram, which includes 
six risk factors with favorable predictive accuracy, discrimination, and clinical utility, allows for simple and rapid 
individual patient risk estimates. It can be used on admission to the ED to predict mortality and facilitate early 
risk stratification and actionable measures in clinical practice after further external validation.
Data availability
The datasets generated during and/or analyzed during the current study are not publicly available due to data 
confidentiality. However, they can be obtained from the corresponding author upon reasonable request.
Received: 16 July 2023; Accepted: 23 December 2023
Figure 6.  Comparison of other predictive models. m1, nomogram of predictive models, AUC: 0.953 (95% CI 
0.936–0.970); m2, predictive model excluding plasma PQ concentrations, AUC: 0.882 (95% CI 0.853–0.911); 
m3, SIPP , AUC: 0.909 (95% CI 0.883–0.934); AUC  area under the receiver operating characteristic curve, SIPP 
severity index of paraquat.

9
Vol.:(0123456789)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
References
 1. Wilks, M. F . et al. Improvement in survival after paraquat ingestion following introduction of a new formulation in Sri Lanka. 
PLoS Med. 5, e49 (2008).
 2. Gawarammana, I. B. & Buckley, N. A. Medical management of paraquat ingestion. Br. J. Clin. Pharmacol. 72, 745–757 (2011).
 3. Wu, W .-P . et al. Addition of immunosuppressive treatment to hemoperfusion is associated with improved survival after paraquat 
poisoning: A nationwide study. PLoS One 9, e87568 (2014).
 4. Gao, J. et al. Prolonged methylprednisolone therapy after the pulse treatment for patients with moderate-to-severe paraquat 
poisoning: A retrospective analysis. Medicine (Baltimore) 96, e7244 (2017).
 5. Tan, J. T. et al. Paraquat poisoning: Experience in hospital taiping (year 2008–October 2011). Med. J. Malaysia 68, 384–388 (2013).
 6. Wang, W . J. et al. Sequential organ failure assessment in predicting mortality after paraquat poisoning: A meta-analysis. PLoS One 
13, e0207725 (2018).
 7. Gheshlaghi, F . et al. Prediction of mortality and morbidity following paraquat poisoning based on trend of liver and kidney injury. 
BMC Pharmacol. Toxicol. 23, 67 (2022).
 8. Li, C. et al. Treatment outcome of combined continuous venovenous hemofiltration and hemoperfusion in acute paraquat poison-
ing: A prospective controlled trial. Crit. Care Med. 46, 100–107 (2018).
 9. Wang, Y . et al. Clinical effect of haemoperfusion combined with continuous veno-veno haemofiltration in treatment of paraquat 
poisoning: A meta-analysis. Zhonghua Wei Zhong Bing Ji Jiu Yi Xue 31, 214–220 (2019).
 10. Hsu, C.-W . et al. Early hemoperfusion may improve survival of severely paraquat-poisoned patients. PLoS One 7, e48397 (2012).
 11. Sawada, Y . et al. Severity index of paraquat poisoning. Lancet (London, England) 1(8598), 1333 (1988).
 12. Proudfoot, A. T. et al. Paraquat poisoning: Significance of plasma-paraquat concentrations. Lancet (London, England) 2(8138), 
330–332 (1979).
 13. Senarathna, L. et al. Prediction of outcome after paraquat poisoning by measurement of the plasma paraquat concentration. QJM 
Mon. J. Assoc. Phys. 102(4), 251–259 (2009).
 14. Xu, S. et al. APACHE score, severity index of paraquat poisoning, and serum lactic acid concentration in the prognosis of paraquat 
poisoning of Chinese patients. Pediatr Emerg Care 31(2), 117–121 (2015).
 15. Suzuki, K. et al. Evaluation of severity indexes of patients with paraquat poisoning. Hum. Exp. Toxicol. 10(1), 21–23 (1991).
 16. Chen, H. et al. An effective machine learning approach for prognosis of paraquat poisoning patients using blood routine indexes. 
Basic Clin. Pharmacol. Toxicol. 120(1), 86–96 (2017).
 17. Gheshlaghi, F . et al. Prediction of mortality and morbidity following paraquat poisoning based on trend of liver and kidney injury. 
BMC Pharmacol. Toxicol. 23(1), 67 (2022).
 18. Hu, L. et al. A new machine-learning method to prognosticate paraquat poisoned patients by combining coagulation, liver, and 
kidney indices. PloS One 12(10), e0186427 (2017).
 19. Zhao, Y . et al. Serum anion gap at admission as a predictor of the survival of patients with paraquat poisoning: A retrospective 
analysis. Medicine 99(31), e21351 (2020).
 20. Lu, S. et al. Development and validation of a radiomics nomogram for prognosis prediction of patients with acute paraquat poison-
ing: A retrospective cohort study. BioMed Res. Int. 2021, 6621894 (2021).
 21. Huang, J. et al. The value of APACHE II in predicting mortality after paraquat poisoning in Chinese and Korean population: A 
systematic review and meta-analysis. Medicine 96(30), e6838 (2017).
 22. Wang, W . J. et al. Sequential organ failure assessment in predicting mortality after paraquat poisoning: A meta-analysis. PloS One 
13(11), e0207725 (2018).
 23. Persson, H. E. et al. Poisoning severity score grading of acute poisoning. J. Toxicol. Clin. Toxicol. 36(3), 205–213 (1998).
 24. Wang, J. et al. Identify the early predictor of mortality in patients with acute paraquat poisoning. BioMed Res. Int. 2020, 8894180 
(2020).
 25. Iasonos, A. et al. How to build and interpret a nomogram for cancer prognosis. J. Clin. Oncol. 26, 1364–1370 (2008).
 26. Lu, S. et al. Development and validation of a radiomics nomogram for prognosis prediction of patients with acute paraquat poison-
ing: A retrospective cohort study. Biomed. Res. Int. 2021, 6621894 (2021).
 27. Li, C. et al. Treatment outcome of combined continuous venovenous hemofiltration and hemoperfusion in acute paraquat poison-
ing: A prospective controlled trial. Crit. Care Med. 46(1), 100–107 (2018).
 28. Huang, P .-F . et al. Predictive value of admission  CO2 combining power combined with serum sodium for the prognosis in acute 
Stanford type A aortic dissection patients. Sci. Rep. 13(1), 1048 (2023).
 29. Savonius, O. et al. PCR-confirmed malaria among children presenting with a decreased level of consciousness in Angola: A pro -
spective, observational study. Malar. J. 22(1), 130 (2023).
 30. Caetano, S. J., Sonpavde, G. & Pond, G. R. C-statistic: A brief explanation of its construction, interpretation and limitations. Eur. 
J. Cancer 90, 130–132 (2018).
 31. Alba, A. C. et al. Discrimination and calibration of clinical prediction models: Users’ guides to the medical literature. JAMA 318, 
1377–1384 (2017).
 32. Vickers, A. J. & Elkin, E. B. Decision curve analysis: A novel method for evaluating prediction models. Med. Decis. Mak. 26, 565–574 
(2006).
 33. Shi, C. et al. Bone marrow mesenchymal stem and progenitor cells induce monocyte emigration in response to circulating toll-like 
receptor ligands. Immunity 34, 590–601 (2011).
 34. Y ang, C.-J. et al. Spectrum of toxic hepatitis following intentional paraquat ingestion: Analysis of 187 cases. Liver Int. 32, 1400–1406 
(2012).
 35. Nouri, A., Heibati, F . & Heidarian, E. Gallic acid exerts anti-inflammatory, anti-oxidative stress, and nephroprotective effects 
against paraquat-induced renal injury in male rats. Naunyn Schmiedebergs Arch. Pharmacol. 394, 1–9 (2021).
 36. Sun, B. & He, Y . Paraquat poisoning mechanism and its clinical treatment progress. Zhonghua Wei Zhong Bing Ji Jiu Yi Xue 29, 
1043–1046 (2017).
 37. Mohamed, F. et al. Mechanisms underlying early rapid increases in creatinine in paraquat poisoning. PLoS One 10, e0122357 
(2015).
 38. Kim, S.-J. et al. The clinical features of acute kidney injury in patients with acute paraquat intoxication. Nephrol. Dial. Transpl. 24, 
1226–1232 (2009).
 39. Proudfoot, A. T. et al. Paraquat poisoning: Significance of plasma-paraquat concentrations. Lancet 2, 330–332 (1979).
 40. Hart, T. B., Nevitt, A. & Whitehead, A. A new statistical approach to the prognostic significance of plasma paraquat concentrations. 
Lancet 2, 1222–1223 (1984).
 41. Scherrmann, J. M. et al. Prognostic value of plasma and urine paraquat concentration. Hum. Toxicol. 6, 91–93 (1987).
 42. Jones, A. L., Elton, R. & Flanagan, R. Multiple logistic regression analysis of plasma paraquat concentrations as a predictor of 
outcome in 375 cases of paraquat poisoning. QJM 92, 573–578 (1999).
 43. Y amamoto, I. et al. Correlating the severity of paraquat poisoning with specific hemodynamic and oxygen metabolism variables. 
Crit. Care Med. 28, 1877–1883 (2000).
 44. Li, Y ., Zhang, H. & Zhang, G. Early white blood cell count in predicting mortality after acute paraquat poisoning: A meta-analysis. 
Zhonghua Wei Zhong Bing Ji Jiu Yi Xue 31, 1013–1017 (2019).

10
Vol:.(1234567890)Scientific Reports |         (2024) 14:1622  | https://doi.org/10.1038/s41598-023-50722-z
www.nature.com/scientificreports/
 45. Li, S. et al. The significance of  CO2 combining power in predicting prognosis of patients with stage II and III colorectal cancer. 
Biomark. Med. 13, 1071–1080 (2019).
 46. Hu, J. et al. Metabolic acidosis as a risk factor for the development of acute kidney injury and hospital mortality. Exp. Ther. Med. 
13, 2362–2374 (2017).
 47. Gunnerson, K. J. et al. Lactate versus non-lactate metabolic acidosis: A retrospective outcome evaluation of critically ill patients. 
Crit. Care 10, R22 (2006).
 48. Shirakabe, A. et al. Clinical significance of acid-base balance in an emergency setting in patients with acute heart failure. J. Cardiol. 
60, 288–294 (2012).
Acknowledgements
This work was supported by the National Natural Science Foundation of China (Grant No. 82072156) and the 
Science and Technology Department of Sichuan Province (Grant No. 2022YFS0273).
Author contributions
G.T. performed all data analysis. G.T. and J.Z. wrote the main manuscript text. J.X., Y .Y . and S.Y . prepared all 
figures and table. RY conducted the design and review of the article. All authors reviewed the manuscript.
Competing interests 
The authors declare no competing interests.
Additional information
Correspondence and requests for materials should be addressed to R.Y .
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International 
License, which permits use, sharing, adaptation, distribution and reproduction in any medium or 
format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the 
Creative Commons licence, and indicate if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the 
material. If material is not included in the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from 
the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.
© The Author(s) 2024