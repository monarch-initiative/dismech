---
reference_id: DOI:10.1186/s12885-024-13129-1
title: "Efficacy and safety of PD-1/PD-L1 inhibitors in patients with Merkel Cell Carcinoma: a systematic review and Meta-analysis"
authors:
- Francisco Cezar Aquino de Moraes
- Michele Kreuz
- Isabella Christina Amaral de Lara
- Artur de Oliveira Macena Lôbo
- Rommel Mario Rodríguez Burbano
journal: BMC Cancer
year: '2024'
doi: 10.1186/s12885-024-13129-1
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://bmccancer.biomedcentral.com/counter/pdf/10.1186/s12885-024-13129-1"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1186_s12885-024-13129-1.pdf
---

# Efficacy and safety of PD-1/PD-L1 inhibitors in patients with Merkel Cell Carcinoma: a systematic review and Meta-analysis
**Authors:** Francisco Cezar Aquino de Moraes, Michele Kreuz, Isabella Christina Amaral de Lara, Artur de Oliveira Macena Lôbo, Rommel Mario Rodríguez Burbano
**Journal:** BMC Cancer (2024)
**DOI:** [10.1186/s12885-024-13129-1](https://doi.org/10.1186/s12885-024-13129-1)

## Content

de Moraes et al. BMC Cancer         (2024) 24:1357  
https://doi.org/10.1186/s12885-024-13129-1
SYSTEMATIC REVIEW Open Access
© The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if 
you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or 
parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To 
view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
BMC Cancer
Efficacy and safety of PD-1/PD-L1 inhibitors 
in patients with Merkel Cell Carcinoma: 
a systematic review and Meta-analysis
Francisco Cezar Aquino de Moraes1*, Michele Kreuz2, Isabella Christina Amaral de Lara3, Artur de Oliveira 
Macena Lôbo4 and Rommel Mario Rodríguez Burbano1,5 
Abstract 
Background Merkel cell carcinoma (MCC) is a rare and aggressive neuroendocrine skin cancer characterized by high 
rates of metastasis. Emerging evidence suggests that PD-L1/PD1 blockade holds promise as a therapeutic option 
for MCC. However, the efficacy and safety of this approach in treating MCC remain incompletely understood. This 
systematic review and meta-analysis aims to analyze the efficacy and safety of PD-1/PD-L1 blockade for patients 
with MCC.
Methods PubMed, Cochrane, and Embase were searched for studies evaluating patients with MCC undergoing 
PD-1/PD-L1 treatment. The estimated outcomes were overall response rate (ORR), disease control rate (DCR), progres-
sion-free survival (PFS), overall survival (OS), and treatment-related adverse events (TRAEs). We performed the meta-
analysis using RStudio v4.4.2 software.
Results A total of 14 reports of 13 different studies encompassing 615 patients were included. The median age 
ranged from 64 to 77 years. Median follow-up ranged from 7.9 months to 59.3 months. Pooled OS rates at 24 and 36 
months were 65.05% (95% CI 44.04–81.49) and 59.58% (95% CI 39.62–76.81), respectively, while pooled PFS rates at 6, 
12, and 36 months were 51.78% (95% CI 37.83–65.45), 46.12% (95% CI 29.44–63.72), and 28.73% (95% CI 16.57–45.02), 
in the same order. DCR proportion was 61.65% (95% CI 54.85–68.03) and ORR was 53.79% (95% CI 47.80-59.68). The 
frequency of TRAEs of any grade was 61.72% (95% CI 45.75–75.51) and for TRAEs of grade ≥ 3 was 17.60% (95% CI 
12.28 to 24.57).
Conclusions This systematic review and meta-analysis revealed that patients with MCC undergoing treatment 
with PD-1/PDL-1 showed durable responses with continuous and clinically meaningful survival outcomes.
Keywords Merkel cell carcinoma, Skin cancer, PD-1/PD-L1 inhibitors, Meta-analysis
*Correspondence:
Francisco Cezar Aquino de Moraes
francisco.cezar2205@gmail.com
Full list of author information is available at the end of the article

Page 2 of 13de Moraes et al. BMC Cancer         (2024) 24:1357 
Graphical Abstract
Background
The aggressive skin cancer known as Merkel cell carci -
noma (MCC) is rare and is linked to immunosuppres -
sion, ultraviolet radiation exposure, and the presence 
of the clonally integrated Merkel cell polyomavirus 
(MCPyV) [1, 2]. Individuals diagnosed with metastatic 
MCC (mMCC) have an unfavorable prognosis, with a 
historical 5-year overall survival rate of ≤ 18% [1–3].
Treatment options have mostly been restricted to 
chemotherapy or experimental strategies, with therapy 
selection depending on disease stage, location of the 
tumor and comorbid conditions. MCC is known to be 
sensitive to chemotherapy, but existing literature on its 
use remains unclear. Commonly prescribed regimens 
include a platinum agent with or without etoposide 
phosphate, cyclophosphamide, doxorubicin, epirubicin, 
vincristine, and topotecan. Current evidence does not 
provide definitive evaluation regarding efficacy of exist -
ing regimens, and many often come with considerable 
toxicity. Although chemotherapy produces compara -
tively high objective response rates, patients usually 
have significant toxicity, short survival times, and tem -
porary responses [1 , 4–6]. MCC is also closely associ -
ated with immunosuppression, since it was shown to 
arise more frequently and have a worse prognosis in 
immunocompromised people [7 , 8].
Approximately 50% of Merkel-cell carcinomas 
express PD-1 (Programmed Cell Death 1) on tumor-
infiltrating lymphocytes and PD-L1 (Programmed Cell 
Death Ligand 1) on tumor cells or infiltrating mac -
rophages in a “adaptive resistance” pattern, indicating 
an endogenous tumor-reactive immune response that 
may be triggered by anti-PD-1 or anti-PD-L1 drugs [7 , 
9–11]. Emerging evidence suggests that PD-L1/PD1 
blockade holds promise as a therapeutic option for 
MCC. However, the efficacy and safety of this approach 
in treating MCC remains incompletely understood.
This systematic review and single-arm meta-anal -
ysis aims to analyze the Overall Survival (OS) and 

Page 3 of 13
de Moraes et al. BMC Cancer         (2024) 24:1357 
 
Progression Free Survival (PFS) of patients with MCC 
undergoing treatment with PD-1/PD-L1 blockade.
Methods
Protocol and registration
This systematic review aims to provide a comprehensive 
analysis and synthesis of the existing literature. To ensure 
transparency and adherence to best practices, this review 
followed the Preferred Reporting Items for Systematic 
Reviews and Meta-Analysis guidelines (PRISMA Check -
list, Supplementary Tables S1 and S2) [12]. The protocol 
for this review was registered in the International Pro -
spective Register of Systematic Reviews (PROSPERO), 
National Institute for Health and Care Research with reg-
istration number CRD42024577303.
Eligibility criteria and search strategy
This systematic review and meta-analysis searched for 
studies that assessed the efficacy of immunotherapy 
based on PD-1/PD-L1 inhibitors for adults with MCC 
and had disease within stages II to IV. We excluded stud -
ies with overlapping populations, those that were case 
reports, case series, reviews and opinion pieces. No 
restriction was set with respect to previous lines of ther -
apy or use of combinations of drugs. Also, there were no 
restrictions regarding language, geographical region or 
publication date of the included articles.
PubMed, Cochrane, and Embase databases were sys -
tematically searched from July 13 to July 15, 2024, using a 
sensitive search strategy that can be found in Supplemen-
tary Table  3. We combined Medical Subject Headings 
(MeSH) terms and input terms with boolean connectors 
(OR, AND) for the search query elaboration. The results 
were incorporated into the reference management soft -
ware Rayyan and duplicate records were automatically 
and manually removed [13].
Two reviewers (M.K. and A.O.M.L.) independently 
analyzed the titles and abstracts of the articles found in 
the databases and screened them according to prespeci -
fied criteria. A third reviewer (F.C.A.M.) determined 
the study eligibility in cases where a consensus was not 
reached.
Data extraction
Data extraction was performed by two authors (I.C.A.L. 
and F.C.A.M.) and conflicts were resolved through con -
sensus between both authors. We collected the following 
baseline characteristics: (1) age; (2) male/female ratio; (3) 
Eastern Cooperative Oncology Group (ECOG) perfor -
mance status; and (4) disease stage.
The following outcomes of interest were extracted: 
(1) overall response rate (ORR); (2) disease control rate 
(DCR); (3) overall survival (OS); (4) progression-free 
survival (PFS); (5) treatment-related adverse events 
(TRAEs) of any grade; (6) treatment-related adverse 
events of grade ≥ 3; (7) immune-related adverse events; 
(8) treatment discontinuation due to TRAEs; and (9) 
deaths related to TRAEs.
Quality assessment and sensitivity analysis
The risk of bias assessment was made using the Newcas -
tle-Ottawa Quality Assessment Scale for observational 
studies [14]. All included articles were assigned a score 
ranging from 0 to 9, according to predetermined criteria. 
Studies with scores of ≤ 4, 5 to 7 and ≥ 8 were labeled as 
low quality, moderate quality and high quality, respec -
tively. Two authors (M.K. and F.C.A.M.) were respon -
sible for independently assessing the methodological 
quality of all articles included in this review. Any disa -
greements were resolved by the intervention of a third 
reviewer (A.O.M.L.), who made the final decision. As a 
way to evaluate the presence and influence of publica -
tion bias and small-study effects, the reviewers employed 
Doi plots along with the LFK index for outcomes with at 
least 10 observations. A LFK index beyond the interval 
between ± 1 was considered to indicate significant asym -
metry [15].
Statistical analysis
We conducted a single-arm meta-analysis using the 
‘meta’ package in the R Project for Statistical Comput -
ing software (version 4.3.2) [16]. The reported proportion 
from the studies for each of the prespecified endpoints 
were subjected to a logit transformation and the weights 
for each study were calculated according to the inverse 
variance method. The degree of heterogeneity was 
assessed by the Tau² statistic, which quantifies the vari -
ation in true effects, and the I² statistic, which measures 
the percentage of variation due to heterogeneity [17]. The 
evidence of heterogeneity was considered significant for 
p-values less than 0.10 or I² greater than 25%. To inves -
tigate how much each study influenced the overall result 
and heterogeneity, a leave-one-one sensitivity analysis 
was conducted. For presentation, the logit-transformed 
prevalences were back-transformed, along with their 
respectives 95% confidence and prediction intervals. Fur -
thermore, a subgroup analysis according to drug mecha -
nism, whether PD-1 or PD-L1 blockade, was performed. 
A random-effects model was used for all endpoints.
Results
Study selection and baseline characteristics
Our initial systematic search yielded 849 results. After 
the removal of duplicate records, and the exclusion of 
references based on title and abstract, 28 studies were 
eligible and remained for thorough full-text review. 

Page 4 of 13de Moraes et al. BMC Cancer         (2024) 24:1357 
Of these, based on prespecified eligibility criteria, 14 
reports of 13 different studies were included [1 , 18–30], 
comprising 615 patients with MCC. Details of study 
selection can be found on Fig. 1 .
Among the included studies, median follow-up 
ranged from 7.9 months to 59.3 months, while median 
patient age varied from 64 to 77 years. Out of the 613 
patients that had information on disease stage, 525 
(85.6%) had stage IV MCC, 77 (12.6%) had stage III 
MCC, and the remaining 11 (1.8%) had stage II MMC. 
With respect to the PD-1/PD-L1 inhibitor of choice, 
339 (55.1%) patients received avelumab, 103 (16.7%) 
received nivolumab, 101 (16.4%) received retifanli -
mab, 50 (8.1%) received pembrolizumab, and 22 (3.6%) 
received atezolizumab. A detailed description of each 
study’s design and sample characteristics is shown in 
detail in Table 1 .
Pooled analysis of the outcomes
Overall Survival (OS)
In a pooled analysis of four studies, selected based on 
available data, including 202 patients, the overall survival 
rate at 24 months was 65.05% (95% CI 44.04 to 81.49; 
 I2 = 85%; Fig.  2A) in patients undergoing PD-1/PD-L1 
treatment. At 36 months, the OS proportion was 59.58% 
(95% CI 39.62 to 76.81;  I2 = 84%; Fig. 2B).
Progression‑Free Survival (PFS)
According to the patient data available from four stud -
ies, comprising 163 patients, the PFS rate at 6 months 
was 51.78% (95% CI 37.83 to 65.45;  I2 = 58%; Fig.  3A). 
Similarly, the PFS proportion at 12 months was 46.12% 
(95% CI 29.44 to 63.72;  I2 = 73%; Fig. 3B). Three reports 
brought data at 36 months, comprising 149 patients, and 
Fig. 1 Flow diagram of the study selection

Page 5 of 13
de Moraes et al. BMC Cancer         (2024) 24:1357 
 
the pooled PFS ratio was 28.73% (95% CI 16.57 to 45.02; 
 I2 = 66%; Fig. 3C).
Overall Response Rate (ORR)
Thirteen studies, comprising 563 patients, provided data 
on this outcome. The treatment with PD-1/PD-L1 inhibi-
tors was associated with an ORR of 53.79% (95% CI 47.80 
to 59.68;  I2 = 43%; Fig. 4A).
Disease Control Rate (DCR)
Our analysis based on available data of 552 patients from 
twelve studies revealed a pooled DCR of 61.65% (95% CI 
54.85 to 68.03;  I2 = 54%; Fig.  4B) concerning treatment 
with PD-1/PD-L1 blockade.
Treatment‑Related Adverse Events (TRAEs)
In our pooled analysis of ten studies, selected accord -
ing to provided data, the pooled proportion of TRAEs of 
any grade was 61.72% (95% CI 45.75 to 75.51;  I2 = 90%; 
Fig.  5A), and 17.60% (95% CI 12.28 to 24.57;  I2 = 68%; 
Fig.  5B) for TRAEs of grade ≥ 3. Regarding immune-
related adverse events, we found the pooled propor -
tion to be 22.76% of patients (95% CI 12.93 to 36.90; 
 I2 = 63%; Fig. 5C). The pooled frequency of patients that 
Table 1 Design and sample characteristics of the included studies
PD-1 Programmed cell death protein 1, PD-L1 Programmed death ligand 1, ECOG Eastern Cooperative Oncology Group; a: median (range)
Study (year) Study design PD-1/PD-L1 
inhibitor
Follow-upa Number 
of 
patients
Age (years)a Sex 
(male/
female)
ECOG status -
n (%)
Disease stage -
n (%)
Averbuch
2023[18]
Retrospective 
cohort
Avelumab 12.75 months 62 74.5 (37–95) 34/28 0: 26 (42%)
1: 12 (19%)
2: 8 (13%)
3: 3 (5%)
4: 1 (2%)
Unknown: 12 
(19%)
III: 8 (13%)
IV: 52 (84%)
Unknown:
2 (3%)
D’Angelo
2020[1]
Single-arm clini-
cal trial
Avelumab 40.8 months 88 N.R. N.R. N.R. IV: 88 (100%)
Ferrarotto
2019[19]
Single-arm clini-
cal trial
Atezolizumab 9.7 months 11 70 (57–84) 7/4 N.R. IV: 11 (100%)
Glutsch
2022[20]
Retrospective 
cohort
Nivolumab 18.85 months 14 64 (53–83) 9/14 0: 7 (50%)
1: 4 (29%)
2: 3 (21%)
III: 3 (21%)
IV: 11 (79%)
Grignani
2023[21]
Single-arm clini-
cal trial
Retifanlimab 17.6 months 101 71.0 (38–90) 68/33 0: 74 (73.3%)
1: 27 (26.7%)
III: 10 (9.9%)
IV: 91 (90.1%)
Kim
2022[22]
Randomized clini-
cal trial
Nivolumab 14.6 months 50 73 (67–81) 39/11 0: 23 (46%)
1: 27 (54%)
IIIB: 12 (24%)
IV: 38 (76%)
Levy
2020[23]
Retrospective 
cohort
Avelumab 8.9 months 54 73 (53–88) 34/20 0: 17 (32%)
1: 32 (59%)
2: 5 (9%)
III: 8 (15%)
IV: 46 (85%)
Munhoz
2021[24]
Single-arm clini-
cal trial
Avelumab 7.9 months 46 71.6 (44–94) 28/18 0: 14 (34%)
1: 21 (46%)
2: 7 (15%)
3:1 (2%)
Unknown: 3 (3%)
IV: 46 (100%)
Nghiem
2021[25]
Single-arm clini-
cal trial
Pembrolizumab 31.8 months 50 70.5 (46–91) N.R. N.R. IIIB: 7 (14%)
IV: 43 (86%)
Ríos-Viñuela 
2024[26]
Retrospective 
cohort
Avelumab 9.5 months 14 70 (54–84)) 13/1 N.R. IV : 14 (100%)
Sousa
2024[27]
Single-arm clini-
cal trial
Atezolizumab 59.3 months 11 71 (57–84) 7/4 N.R. III: 3 (27%)
IV: 8 (73%)
Topalian
2020[28, 29]
Single-arm clini-
cal trial
Nivolumab 54.1 weeks 39 68 (22–88) 25/14 0: 30 (76.9%)
1: 9 (23.1%)
II: 11 (28.2%)
III: 26 (66.7%)
IV: 2 (5.1%)
Uhara
2024[30]
Single-arm clini-
cal trial
Avelumab 51 weeks 75 77 (42–95) 36/39 0: 36 (48%)
1: 25 (33%)
2: 7 (9%)
3: 6 (8%)
Unknown: 1 (1%)
IV: 75 (100%)

Page 6 of 13de Moraes et al. BMC Cancer         (2024) 24:1357 
discontinued treatment due to TRAEs was 12.74% (95% 
CI 7.74 to 20.27  I2 = 45%; Supplementary Fig. 1A) and the 
rate of death related to TRAEs was 3.45% (95% CI 1.44 to 
8.03;  I2 = 0%; Supplementary Fig. 1B).
Subgroup analysis
In our subgroup analysis according to drug mechanism, 
no difference was identified between PD-1 and PD-L1 
inhibitors for OS at 24 months (70.45%; 95% CI 60.04 to 
79.09; I² = 10% versus 65.05%; 95% CI 44.04 to 81.49; I² = 
84%; p = 0.61), OS at 36 months (65.66%; 95% CI 55.85 to 
74.29; I² = 0% versus 49.82%; 95% CI 15.45 to 84.37; I² = 
83%; p = 0.46), PFS at 6 months (55.21%; 95% CI 40.06 to 
69.45; I² = 22% versus 53.84%; 95% CI 24.36 to 80.87; I² = 
72%; p = 0.94), PFS at 12 months (50.02%; 95% CI 37.98 
to 62.06; I² = 0% versus 48.67%; 95% CI 13.55 to 85.16; 
I² = 85%; p = 0.95), ORR (56.87%; 95% CI 50.46 to 63.06; 
I² = 0% versus 50.13%; 95% CI 41.90 to 58.35; I² = 48%; 
p = 0.21), DCR (60.88%; 95% CI 454.17 to 67.19; I² = 0% 
versus 58.53%; 95% CI 46.16 to 69.25; I² = 64%; p = 0.69), 
and treatment discontinuation (14.79%; 95% CI 7.28 to 
27.74; I² = 60% versus 9.09%; 95% CI 4.96 to 16.08; I² = 
0%; p = 0.29).
The same applied to TRAEs of any grade (75.33%; 95% 
CI 54.04 to 88.80; I² = 86% versus 48.00%; 95% CI 26.46 
to 70.29; I² = 92%; p = 0.08), although marginally. For PFS 
at 36 months (40.00%; 95% CI 26.41 to 54.82; I² = N/A 
versus 21.28%; 95% CI 14.30 to 30.46; I² = 0%; p = 0.02), 
TRAEs of grade 3 or more (23.07%; 95% CI 14.35 to 
34.93; I² = 68% versus 12.71%; 95% CI 9.26 to 17.19; I² 
= 0%; p = 0.04), and immune-related adverse events 
(34.65%; 95% CI 25.46 to 44.77; I² = N/A versus 18.41%; 
95% CI 10.85 to 29.49; I² = 8%; p = 0.02), significant dif -
ferences were verified between the subgroups. All sub -
group analyses can be found in Supplementary Fig. 2.
Sensitivity analysis
We performed leave-one-out sensitivity analyses for 
all outcomes to assess the potential influences of each 
study on our findings (Supplementary Fig.  3). For 
TRAEs of any grade and grade ≥ 3, there was no signifi -
cant change in heterogeneity with the omission of any 
of the studies. Omitting the study by D’Angelo et  al. 
Fig. 2 PD-1/PD-L1 blockade treatment was associated with an OS ratio of (A) 65.05% at 24 months and (B) 59.58% at 36 months

Page 7 of 13
de Moraes et al. BMC Cancer         (2024) 24:1357 
 
significantly reduced the I² statistic for OS at 24 months 
(85–0%), OS at 36 months (84–0%), PFS at 6 months 
(58–13%), PFS at 12 months (73–9%), PFS at 36 months 
(66–0%), ORR (43–0%), and DCR (54–19%). Similarly, 
omitting the study by Grignani et al. reduced the I² sta -
tistic from 63 to 8% for immune-related adverse events 
and from 45 to 0% for treatment discontinuation due to 
TRAEs.
Quality assessment
Doi plots for ORR (LFK = 0.74) and TRAEs (LFK = 0.81) 
of any grade did not show significant asymmetry. How -
ever, a LFK index of 2.36 was assessed for DCR. All Doi 
plots can be seen in Supplementary Fig. 4.
The Newcastle–Ottawa Scale (NOS) was used to 
assess the risk of bias of each included study. Nine 
studies were judged to be of good quality, scoring 8 or 
Fig. 3 PD-1/PD-L1 blockade treatment was associated with a PFS rate of (A) 51.78% at 6 months, (B) 46.12% at 12 months, and (C) 28.73% at 36 
months

Page 8 of 13de Moraes et al. BMC Cancer         (2024) 24:1357 
9 points, while the remaining studies received a fair 
quality assessment, scoring between 5 and 7 points, 
due to not fulfilling the minimal criteria for selection 
and comparability factors. The evaluation of study 
quality assessment using the NOS tool can be found in 
Supplementary Fig. 5 .
Discussion
In this systematic review and meta-analysis, we evaluated 
the effectiveness and safety of PD-1/PD-L1 inhibition 
in patients with MCC. In a pooled study, the DCR was 
61.65% (95% CI 54.85 to 68.03) and the ORR was 53.79% 
(95% CI 47.80 to 59.68). These findings underscore the 
Fig. 4 PD-1/PD-L1 blockade treatment was associated with an (A) ORR of 53.79% and an (B) DCR of 61.65%

Page 9 of 13
de Moraes et al. BMC Cancer         (2024) 24:1357 
 
Fig. 5 Treatment with PD-1/PD-L1 blockade was associated with the occurrence rate of (A) 61.72% of adverse events of any grade, (B) 17.60% 
of grade ≥ 3 TRAEs, and (C) 22.76% of immune-related adverse events

Page 10 of 13de Moraes et al. BMC Cancer         (2024) 24:1357 
potential for PD-1/PD-L1 blockade to exert a more pro -
nounced therapeutic effect in patients with merkel cell 
carcinoma.
MCC highlights the intersection of multiple explora -
tory biomarker categories: it is frequently related with 
PD-L1 expression and CD8 infiltrates, and it can have a 
high mutational burden (caused by a carcinogen [ultra -
violet light]) or be virus-associated. The presence of 
oncogenic viruses in virus-associated malignancies, 
where viral antigens function as tumor-specific antigens, 
has recently been postulated as a potential mechanistic 
marker for anti-PD-1 therapeutic response. More than 
20% of all cancers globally are virus-associated, and their 
mutational loads may be low or modest as a result of car -
cinogenesis driven by viral oncogenes. Viral antigens are 
foreign and thus potentially potent immune stimulants, 
and many virus-associated malignancies have substantial 
immunological infiltrates and PD-L1 expression [7, 31, 
32].
Treatment resistance, a notion relevant to MCC, refers 
to genetic changes in tumor cells that might result in the 
loss or modification of tumor antigens, making them less 
recognized by the immune system, even in the presence 
of PD-1 inhibitors, or PD-L1 [33]. Joyce et al. 2015 [34] 
referred to alterations in the tumor microenvironment 
that can produce an immunosuppressive environment, 
preventing PD-1 and PD-L1 inhibitors from working 
effectively and contributing to immunotherapy resistance 
[34]. However, our meta-analysis revealed long-term and 
significant results in Merkel cancer patients treated with 
PD-1 and PD-L1 blockers.
The advent of PD-1/PD-L1 inhibitors has revolu -
tionized the natural history of several cancer types, 
particularly small cell lung cancer, melanoma, and 
gynecological malignancies [35–40]. Regarding MCC, 
recent trials studying anti-PD1/PD-L1 drugs, such as 
avelumab, pembrolizumab, retifanlimab and nivolumab, 
have shown promising results in treating this type of 
malignancy [41–46]. The US Food and Drug Adminis -
tration have approved pembrolizumab and retifanlimab, 
two PD-1 blockers, and avelumab, one PD-L1 inhibitor 
for metastatic MCC [7, 43, 44, 47, 48].
Adverse events associated with cancer treatment, espe -
cially those of grade 3 or higher, significantly impact the 
quality of life in cancer patients, particularly those with 
MCC, which often develops in the older population, 
affecting both their physical and emotional well-being 
[38, 49–52]. The main adverse effects associated with 
PD-1/PD-L1 blockade therapy are immune-mediated 
events, especially pneumonitis, rash, pruritus, colitis 
and hepatitis [51, 52]. However, our analysis revealed 
that only 61.72% of patients experienced any grade 
TRAEs, with the proportion of patients that had TRAEs 
of grade ≥ 3 being 17.60%. Additionally, only 22.76% of 
patients reported immune-related adverse events.
PD-1 and PD-L1 inhibitors work by blocking the 
immunosuppressive communication between tumor cells 
and T cells. However, both immune checkpoint inhibitors 
operate in different manners, targeting different parts of 
the immune response. PD-1 inhibitors block the interac -
tion between PD-1 and its ligands (PD-L1 and PD-L2), 
while anti-PD-L1 antibodies inhibit the binding of PD-L1 
to PD-1. By targeting the PD-1-PD-L1 interaction, both 
types of inhibitors aim to restore immune activity, but 
may differ in epitope binding, affinity, molecular targets, 
and pharmacokinetic properties. These differences can 
result in variations in efficacy and safety profiles, includ -
ing immune-related adverse events [53, 54]. Our results 
show that TRAEs of grade ≥ 3 and immune-related 
adverse events were more frequent with anti-PD-1 drugs 
compared to anti-PD-L1.
The findings of this meta-analysis highlight the clini -
cal relevance of PD-1/PD-L1 inhibitors as a promising 
therapeutic option for patients with Merkel cell carci -
noma (MCC), a cancer known for its aggressive nature 
and high rates of metastasis. By demonstrating durable 
responses, with combined overall survival (OS) rates of 
65.05% at 24 months and 59.58% at 36 months, the analy-
sis underscores the potential for long-term benefits in a 
population with limited treatment options. Addition -
ally, the disease control rate (DCR) of 61.65% and overall 
response rate (ORR) of 53.79% confirm that PD-1/PD-L1 
blockade is effective in achieving significant antitumor 
responses.
Our study adds value to the existing body of knowledge 
by consolidating survival and safety data from various 
studies, offering a comprehensive evaluation of the effi -
cacy and tolerability of immune checkpoint inhibitors 
in MCC. The pooled data on progression-free survival 
(PFS) and treatment-related adverse events (TRAEs) fur -
ther reinforce the favorable and manageable safety pro -
file of these therapies, with a manageable rate of grade ≥ 3 
TRAEs (17.60%). These results help clarify the risk-ben -
efit ratio of PD-1/PD-L1 inhibitors in MCC, an area that 
has been relatively underexplored due to the rarity of the 
disease. As such, this study provides crucial evidence 
that could inform clinical decisions and the develop -
ment of more personalized treatment strategies for MCC 
patients.This meta-analysis has some limitations. First of 
all, as a single-arm meta-analysis, the absence of a con -
trol group limits the articulation of important insights. 
In second place, the high heterogeneity observed in most 
outcomes may reflect significant differences between 
studies and their varying designs.
In third place, as MCC is a rare tumor type, small sin -
gle arm studies were included in the analyses, which can 

Page 11 of 13
de Moraes et al. BMC Cancer         (2024) 24:1357 
 
limit the robustness of our findings. Despite this, these 
factors did not prevent the formulation of robust con -
clusions from the performed pooled analyses. Our study 
provides valuable insights for the development of clini -
cal protocols, as well as clarifies the efficacy and safety 
of anti-PD-1/anti-PD-L1 treatment for MCC, which may 
assist physicians in making more informed decisions 
based on expected efficacy and toxicity profiles.
Conclusions
The results of this meta-analysis reinforce the clini -
cal importance of PD-1/PD-L1 inhibitors as an effective 
therapeutic option for patients with Merkel cell carci -
noma (MCC), offering significant antitumor responses 
and durable survival benefits in a population with few 
treatment alternatives. The favorable safety profile, with a 
low incidence of severe treatment-related adverse events, 
supports the feasibility of these therapies in clinical prac -
tice among these patients. Clinically, these findings sug -
gest that PD-1/PD-L1 inhibitors should be considered 
early in the treatment of advanced MCC. However, future 
studies should focus on identifying response biomarkers 
to better predict which patients will benefit the most, as 
well as monitoring the long-term durability of responses 
and potential late-onset adverse effects.
Abbreviations
MCC  Merkel cell carcinoma
MCPyV  Merkel cell polyomavirus
mMCC  Metastatic MCC
PD-1  Programmed Cell Death 1
PDL1  Programmed death-ligand 1
OS  Overall Survival
PFS  Progression Free Survival
ECOG  Eastern Cooperative Oncology Group
ORR  Overall response rate
DCR  Disease control rate
PFS  Progression-free survival
TRAE  Treatment-related adverse events
AE  Adverse events
NOS  Newcastle–Ottawa Scale
Supplementary Information
The online version contains supplementary material available at https:// doi. 
org/ 10. 1186/ s12885- 024- 13129-1.
Supplementary Material 1.
Acknowledgements
We thank the Federal University of Pará (UFPA); the Center for Research Oncol-
ogy (NPO/UFPA), and thanks to the Pró-Reitoria de Pesquisa e Pós-Graduação 
da UFPA (PROPESP) for paying for the article’s publication fee. This support had 
no role in study design, data collection and analysis, decision to publish, or 
preparation of the manuscript.
Authors’ contributions
All authors contributed to the study conception and design. [F.C.A.M.] 
conceived the project; material preparation was performed by [F.C.A.M., 
M.K., I.C.A.L., A.O.M.L.]. Data collection and analysis were performed by [M.K., 
A.O.M.L., F.C.A.M., R.M.R.B.]. The figures and tables were created by [F.C.A.M., 
I.C.A.L., A.O.M.L.]. The first draft of the manuscript was written by [F.C.A.M., M.K., 
I.C.A.L., A.O.M.L., R.M.R.B.] and all authors commented on previous versions of 
the manuscript. All authors read and approved the final manuscript.
Funding
None.
Data availability
All data generated or analysed during this study are included in this published 
article [and its supplementary information files].
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Competing interests
The authors declare no competing interests.
Author details
1 Federal University of Pará, R. Augusto Corrêa, 01, PA, Belém 66075-110, Brazil. 
2 Lutheran University of Brazil, Canoas, Rio Grande Do Sul 92425-020, Brazil. 
3 Cesumar University, Maringá, Paraná 87050-900, Brazil. 4 Federal University Of 
Pernambuco, Recife, Pernambuco 50670-901, Brazil. 5 Ophir Loyola Hospital, 
Belém, Pará 66063-240, Brazil. 
Received: 20 August 2024   Accepted: 29 October 2024
References
 1. D’Angelo SP , Bhatia S, Brohl AS, Hamid O, Mehnert JM, Terheyden P , et al. 
Avelumab in patients with previously treated metastatic Merkel cell 
carcinoma: long-term data and biomarker analyses from the single-arm 
phase 2 JAVELIN Merkel 200 trial. J Immunother Cancer. 2020;8:e000674.
 2. Schadendorf D, Lebbé C, Zur Hausen A, Avril M-F, Hariharan S, Bharmal M, 
et al. Merkel cell carcinoma: pidemiology, prognosis, therapy and unmet 
medical needs. Eur J Cancer. 2017;71:53–69.
 3. Lebbe C, Becker JC, Grob J-J, Malvehy J, Del Marmol V, Pehamberger H, 
et al. Diagnosis and treatment of Merkel Cell Carcinoma. European con-
sensus-based interdisciplinary guideline. Eur J Cancer. 2015;51:2396–403.
 4. Nghiem P , Kaufman HL, Bharmal M, Mahnke L, Phatak H, Becker JC. 
Systematic literature review of efficacy, safety and tolerability outcomes 
of chemotherapy regimens in patients with metastatic Merkel cell carci-
noma. Future Oncol. 2017;13:1263–79.
 5. Cowey CL, Mahnke L, Espirito J, Helwig C, Oksen D, Bharmal M. Real-world 
treatment outcomes in patients with metastatic Merkel cell carcinoma 
treated with chemotherapy in the USA. Future Oncol. 2017;13:1699–710.
 6. Becker JC, Lorenz E, Ugurel S, Eigentler TK, Kiecker F, Pföhler C, et al. 
Evaluation of real-world treatment outcomes in patients with distant 
metastatic Merkel cell carcinoma following second-line chemotherapy in 
Europe. Oncotarget. 2017;8:79731–41.
 7. Nghiem PT, Bhatia S, Lipson EJ, Kudchadkar RR, Miller NJ, Annamalai 
L, et al. PD-1 blockade with pembrolizumab in advanced Merkel-Cell 
Carcinoma. N Engl J Med. 2016;374:2542–52.
 8. Paulson KG, Iyer JG, Blom A, Warton EM, Sokil M, Yelistratova L, et al. Sys-
temic immune suppression predicts diminished Merkel cell carcinoma-
specific survival independent of stage. J Invest Dermatol. 2013;133:642–6.
 9. Afanasiev OK, Yelistratova L, Miller N, Nagase K, Paulson K, Iyer JG, et al. 
Merkel polyomavirus-specific T cells fluctuate with merkel cell carcinoma 
burden and express therapeutically targetable PD-1 and Tim-3 exhaus-
tion markers. Clin Cancer Res. 2013;19:5351–60.
 10. Taube JM, Anders RA, Young GD, Xu H, Sharma R, McMiller TL, et al. 
Colocalization of inflammatory response with B7-h1 expression in human 
melanocytic lesions supports an adaptive resistance mechanism of 
immune escape. Sci Transl Med. 2012;4:127ra37.

Page 12 of 13de Moraes et al. BMC Cancer         (2024) 24:1357 
 11. Dowlatshahi M, Huang V, Gehad AE, Jiang Y, Calarese A, Teague JE, et al. 
Tumor-specific T cells in human Merkel cell carcinomas: a possible role for 
Tregs and T-cell exhaustion in reducing T-cell responses. J Invest Derma-
tol. 2013;133:1879–89.
 12. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, 
et al. The PRISMA 2020 statement: an updated guideline for reporting 
systematic reviews. BMJ. 2021;372:n71.
 13. Ouzzani M, Hammady H, Fedorowicz Z, Elmagarmid A. Rayyan-a web and 
mobile app for systematic reviews. Syst Rev. 2016;5:210.
 14. Peterson J, et al. The Newcastle-Ottawa scale (NOS) for assessing the 
quality of nonrandomised studies in meta-analyses. Ottawa: Ott Hosp Res 
Inst. 2011;2(1):1–12.
 15. Furuya-Kanamori L, Barendregt JJ, Doi SAR. A new improved graphical 
and quantitative method for detecting bias in meta-analysis. Int J Evid 
Based Healthc. 2018;16:195–203.
 16. Balduzzi S, Rücker G, Schwarzer G. How to perform a meta-analysis with 
R: a practical tutorial. Evid Based Ment Health. 2019;22:153–60.
 17. Higgins JPT, Thompson SG, Deeks JJ, Altman DG. Measuring inconsist-
ency in meta-analyses. BMJ. 2003;327:557–60.
 18. Averbuch I, Stoff R, Miodovnik M, Fennig S, Bar-Sela G, Yakobson A, et al. 
Avelumab for the treatment of locally advanced or metastatic Merkel cell 
carcinoma-A multicenter real-world experience in Israel. Cancer Med. 
2023;12:12065–70.
 19. Ferrarotto R, Mata J, Mott F, Bhosale P , Rubin ML, Altan M, et al. Safety 
and interim results from a phase II, single-arm study of atezolizumab 
and bevacizumab in Merkel cell carcinoma (MCC). JCO. 2019;37 
15suppl:e21006-21006.
 20. Glutsch V, Schummer P , Kneitz H, Gesierich A, Goebeler M, Klein D, 
et al. Ipilimumab plus Nivolumab in avelumab-refractory Merkel cell 
carcinoma: a multicenter study of the prospective skin cancer registry 
ADOREG. J Immunother Cancer. 2022;10: e005930.
 21. Grignani G, Rutkowski P , Lebbe C, Guida M, Marqueste CG, Braud FGMD, 
et al. 1146P updated results from POD1UM-201: a phase II study of reti-
fanlimab in patients with advanced or metastatic Merkel cell carcinoma 
(MCC). Ann Oncol. 2023;34:S686.
 22. Kim S, Wuthrick E, Blakaj D, Eroglu Z, Verschraegen C, Thapa R, et al. 
Combined nivolumab and ipilimumab with or without stereotactic body 
radiation therapy for advanced Merkel cell carcinoma: a randomised, 
open label, phase 2 trial. Lancet. 2022;400:1008–19.
 23. Levy S, Aarts MJB, Eskens FALM, Keymeulen KBMI, Been LB, Grünhagen D, 
et al. Avelumab for advanced Merkel cell carcinoma in the Netherlands: a 
real-world cohort. J Immunother Cancer. 2020;8:e001076.
 24. Munhoz RR, Cayol F, Corrales L, Gerson R, Tilli M, Barreto EO, et al. Merkel 
cell carcinoma in Latin America: a contribution from an expanded access 
program for avelumab to address issues from experts’ recommendations. 
Cancer Immunol Immunother. 2021;70:1031–6.
 25. Nghiem P , Bhatia S, Lipson EJ, Sharfman WH, Kudchadkar RR, Brohl AS, 
et al. Three-year survival, correlates and salvage therapies in patients 
receiving first-line pembrolizumab for advanced Merkel cell carcinoma. J 
Immunother Cancer. 2021;9:e002478.
 26. Ríos-Viñuela E, García-Vázquez M, Juan MJ, Nagore E, Requena C, 
Sanmartín O, et al. Avelumab to treat Merkel cell carcinoma: real-life 
experience in a dedicated oncology center. Actas Dermosifiliogr. 
2024;S0001–7310(24):00059.
 27. de Sousa LG, Liu S, Bhosale P , Altan M, Darbonne W, Schulze K, et al. 
Atezolizumab plus Bevacizumab in advanced Merkel cell carcinoma: a 
prospective study. Oral Oncol. 2024;151: 106747.
 28. Topalian SL, Bhatia S, Amin A, Kudchadkar RR, Sharfman WH, Lebbé C, 
et al. Neoadjuvant Nivolumab for patients with Resectable Merkel Cell 
Carcinoma in the CheckMate 358 Trial. J Clin Oncol. 2020;38:2476–87.
 29. Topalian SL, Bhatia S, Hollebecque A, Awada A, Boer JPD, Kudchadkar 
RR, et al. Abstract CT074: Non-comparative, open-label, multiple cohort, 
phase 1/2 study to evaluate nivolumab (NIVO) in patients with virus-
associated tumors (CheckMate 358): Efficacy and safety in Merkel cell 
carcinoma (MCC). Cancer Res. 2017;77(13_Supplement):CT074.
 30. Uhara H, Kiyohara Y, Isei T, Nagase K, Kambe A, Sato M, et al. Safety and 
effectiveness of avelumab in patients with Merkel cell carcinoma in gen-
eral clinical practice in Japan: post-marketing surveillance. J Dermatol. 
2024;51:475–83.
 31. Lipson EJ, Vincent JG, Loyo M, Kagohara LT, Luber BS, Wang H, et al. 
PD-L1 expression in the Merkel cell carcinoma microenvironment: 
association with inflammation, Merkel cell polyomavirus and overall 
survival. Cancer Immunol Res. 2013;1:54–63.
 32. Lyford-Pike S, Peng S, Young GD, Taube JM, Westra WH, Akpeng B, et al. 
Evidence for a role of the PD-1:PD-L1 pathway in immune resistance of 
HPV-associated head and neck squamous cell carcinoma. Cancer Res. 
2013;73:1733–41.
 33. Zaretsky JM, Garcia-Diaz A, Shin DS, Escuin-Ordinas H, Hugo W, Hu-
Lieskovan S, et al. Mutations Associated with Acquired Resistance to 
PD-1 blockade in Melanoma. N Engl J Med. 2016;375:819–29.
 34. Joyce JA, Fearon DT. T cell exclusion, immune privilege, and the tumor 
microenvironment. Science. 2015;348:74–80.
 35. Cancers. | Free Full-Text | Efficacy and Safety of Rechallenge with BRAF/
MEK Inhibitors in Advanced Melanoma Patients: A Systematic Review 
and Meta-Analysis. https:// www. mdpi. com/ 2072- 6694/ 15/ 15/ 3754. 
Accessed 18 Aug 2024.
 36. Pasqualotto E, de Moraes FCA, Chavez MP , Souza MEC, Rodrigues 
ALS, de Ferreira O. PD-1/PD-L1 inhibitors plus Chemotherapy Versus 
Chemotherapy alone for Resectable Non-small Cell Lung Cancer: a 
systematic review and Meta-analysis of Randomized controlled trials. 
Cancers (Basel). 2023;15:5143.
 37. de Moraes FCA, Pasqualotto E, Lopes LM, Cavalcanti Souza ME, de 
Oliveira Rodrigues ALS, de Almeida AM, et al. PD-1/PD-L1 inhibi-
tors plus carboplatin and paclitaxel compared with carboplatin and 
paclitaxel in primary advanced or recurrent endometrial cancer: a 
systematic review and meta-analysis of randomized clinical trials. BMC 
Cancer. 2023;23:1166.
 38. de Moraes FCA, Lôbo A, de OM, Sano VKT, Kelly FA, Burbano RMR. 
Treatment-related adverse events, including fatal toxicities, in patients 
with extensive-stage small-cell Lung Cancer receiving adjuvant 
programmed cell death 1/Programmed cell death Ligand 1 inhibitors: 
a Meta-analysis and Trial Sequential Analysis of Randomized controlled 
trials. Clin Oncol. 2024;23:1167.
 39. Vilbert M, Priantti JN, Madeira T, Moraes FCA, Tojjari A, Sahin IH, et al. 
Updated pooled analyses of first-line anti-PD1/PD-L1 inhibitors plus 
chemotherapy in advanced esophageal squamous cell carcinoma. JCO. 
2024;42 3suppl:366–366.
 40. Madeira TM, Moraes FCA, Priantti JN, Santiago EM, de Ribeiro L, Vilbert 
MF. 1098P Anti-PD1-based neoadjuvant therapy in resectable stage III 
or IV melanoma patients: a systematic review and meta-analysis. Ann 
Oncol. 2023;34:S661.
 41. Topalian SL, Bhatia S, Amin A, Kudchadkar RR, Sharfman WH, Lebbé C, 
et al. Neoadjuvant Nivolumab for patients with Resectable Merkel Cell 
Carcinoma in the CheckMate 358 Trial. JCO. 2020;38:2476–87.
 42. Sol S, Boncimino F, Todorova K, Waszyn SE, Mandinova A. Therapeutic 
approaches for Non-melanoma skin Cancer: Standard of Care and 
Emerging modalities. Int J Mol Sci. 2024;25: 7056.
 43. D’Angelo SP , Lebbé C, Mortier L, Brohl AS, Fazio N, Grob J-J, et al. First-
line avelumab in a cohort of 116 patients with metastatic Merkel cell 
carcinoma (JAVELIN Merkel 200): primary and biomarker analyses of a 
phase II study. J Immunother Cancer. 2021;9:e002646.
 44. Nghiem P , Bhatia S, Lipson EJ, Sharfman WH, Kudchadkar RR, Brohl AS, 
et al. Durable Tumor regression and overall survival in patients with 
Advanced Merkel Cell Carcinoma receiving Pembrolizumab as First-
Line Therapy. J Clin Oncol. 2019;37:693–702.
 45. Khaddour K, Rosman IS, Dehdashti F, Ansstas G. Durable remission after 
rechallenge with ipilimumab and nivolumab in metastatic Merkel cell 
carcinoma refractory to avelumab: any role for sequential immuno -
therapy? J Dermatol. 2021;48:e80-81.
 46. Glutsch V, Kneitz H, Gesierich A, Goebeler M, Haferkamp S, Becker JC, 
et al. Activity of ipilimumab plus nivolumab in avelumab-refractory 
Merkel cell carcinoma. Cancer Immunol Immunother. 2021;70:2087–93.
 47. Mortier L, Blom A, van Hille B, Samimi M, Luciani L, Cahuzac C, et al. 
Avelumab as second-line or later treatment in patients with metastatic 
Merkel cell carcinoma: analysis of real-world outcomes in France using 
the CARADERM database linked to the French national healthcare 
database. Eur J Cancer. 2024;209: 114261.
 48. 545 A phase 2 study of retifanlimab in patients with advanced or meta-
static merkel cell carcinoma (MCC) (POD1UM-201) | J ImmunoTher 
Cancer. https:// jitc. bmj. com/ conte nt/9/ Suppl_2/ A574. Accessed 16 
Aug 2024.

Page 13 of 13
de Moraes et al. BMC Cancer         (2024) 24:1357 
 
 49. Pichardo R, Abu Omar Y, Wani K, Shango K, Wang D. Uncovering the 
Burden of Immune-related adverse events in Immunotherapy: insights 
from a nationally Representative Sample. Target Oncol. 2023;18:451–61.
 50. Joseph A, Simonaggio A, Stoclin A, Vieillard-Baron A, Geri G, Oudard S, 
et al. Immune-related adverse events: a retrospective look into the future 
of oncology in the intensive care unit. Ann Intensive Care. 2020;10:143.
 51. Management of immune-related adverse events in patients treated with 
immune checkpoint inhibitor therapy. ASCO Guideline Update | J Clin 
Oncol. https:// doi. org/ 10. 1200/ JCO. 21. 01440. Accessed 16 Aug 2024.
 52. Raschi E, Gatti M, Gelsomino F, Ardizzoni A, Poluzzi E, De Ponti F. Lessons 
to be Learnt from Real-World studies on Immune-related adverse events 
with checkpoint inhibitors: a clinical perspective from Pharmacovigilance. 
Target Oncol. 2020;15:449–66.
 53. Bian J, Shao R, Li J, Zhu JF, Shao AZ, Liu C, et al. Mechanism research of 
non-coding RNA in immune checkpoint inhibitors therapy. Cancer Sci. 
2024;115:114261.
 54. Sonpavde GP , Grivas P , Lin Y, Hennessy D, Hunt JD. Immune-related 
adverse events with PD-1 versus PD-L1 inhibitors: a Meta-analysis of 8730 
patients from clinical trials. Future Oncol. 2021;17:2545–58.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.