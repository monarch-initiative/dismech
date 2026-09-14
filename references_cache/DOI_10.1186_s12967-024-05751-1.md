---
reference_id: DOI:10.1186/s12967-024-05751-1
title: "Efficacy and safety of immunosuppressants and monoclonal antibodies in adults with myasthenia gravis: a systematic review and network meta-analysis"
authors:
- Jian Gu
- Yue Qiao
- Rui Huang
- Shuyan Cong
journal: Journal of Translational Medicine
year: '2024'
doi: 10.1186/s12967-024-05751-1
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://link.springer.com/content/pdf/10.1186/s12967-024-05751-1.pdf"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1186_s12967-024-05751-1.pdf
---

# Efficacy and safety of immunosuppressants and monoclonal antibodies in adults with myasthenia gravis: a systematic review and network meta-analysis
**Authors:** Jian Gu, Yue Qiao, Rui Huang, Shuyan Cong
**Journal:** Journal of Translational Medicine (2024)
**DOI:** [10.1186/s12967-024-05751-1](https://doi.org/10.1186/s12967-024-05751-1)

## Content

REVIEW Open Access
© The Author(s) 2024. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you 
give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the 
licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the 
material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation 
or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
Gu et al. Journal of Translational Medicine          (2024) 22:955 
https://doi.org/10.1186/s12967-024-05751-1
Journal of Translational 
Medicine
*Correspondence:
Jian Gu
jackgu0801@126.com
Shuyan Cong
congshuyan@hotmail.com
1Department of Neurology, Shengjing Hospital of China Medical 
University, Shenyang, Liaoning 110000, China
Abstract
Numerous clinical trials for myasthenia gravis (MG) treatment have been conducted recently, with satisfactory 
cognitive and clinical results. However, due to the limited evidence for direct comparison of the safety and 
effectiveness of various drugs, there is a need for further exploration of the advantages and disadvantages of 
different monoclonal antibodies and immunosuppressants. Thus, in the present network meta-analysis (NMA), we 
aimed to compare the efficacy and safety of immunosuppressants and monoclonal antibodies in treating MG. We 
systematically searched for randomized controlled trials published in PubMed, Embase, Web of Science, and the 
Cochrane Library between January 1, 2000 and March 6, 2024. Statistical analyses were performed using R software 
(version 4.2.3), JAGS, and STATA (version 15.0). The surface under the cumulative ranking curve (SUCRA) value was 
calculated to assess the potential efficacy of each drug and the likelihood of adverse events (AEs), with higher 
SUCRA values indicating better efficacy or a lower likelihood of AEs. This NMA included 21 randomized controlled 
trials involving 13 drugs and 1,657 patients. Based on changes in Quantitative MG and MG Composite scores, 
batoclimab was most likely to exert the best therapeutic effects, with SUCRA values of 99% and 92%, respectively. 
Rozanolixzumab performed better than the other drugs in terms of the MG Activities of Daily Living score (85%). 
Eculizumab exhibited the highest potential in reducing the 15-item revised version of the MG Quality of Life score 
(96%). Regarding safety, belimumab had the highest SUCRA value (85%), demonstrating the lowest likelihood of 
AEs. In conclusion, all immunosuppressants and monoclonal antibodies analyzed in this study were more effective 
than the placebo in treating MG, with rozanolixzumab and batoclimab potentially being the most effective. 
Regarding safety, rozanolixzumab exhibited a higher likelihood of AEs than did placebo. The conclusions guide the 
clinical selection of effective drugs and offer insights for future drug experiments.
Keywords Generalized myasthenia gravis, Monoclonal antibody, Immunosuppressants, FcRn inhibitor, Complement 
inhibitor, Meta-analysis
Efficacy and safety of immunosuppressants 
and monoclonal antibodies in adults 
with myasthenia gravis: a systematic review 
and network meta-analysis
Jian Gu1*, Yue Qiao1, Rui Huang1 and Shuyan Cong1*

Page 2 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
Introduction
Myasthenia gravis (MG) is a relatively rare autoimmune 
disease of the nervous system that is mainly mediated 
by B cells and damages the prominent posterior mem -
brane of the neuromuscular junction [ 1]. As an autoim -
mune disease, its primary pathogenic antibodies include 
antibodies against the nicotinic acetylcholine receptor 
(AChR; detected in 80% of patients) and muscle-specific 
kinase (MuSK) (detected in approximately 6% of patients) 
and anti-lipoprotein receptor-related protein 4 (occurs 
more rarely) [2–4]. The primary clinical symptoms of MG 
include fluctuating fatigue and weakness of the extraocu -
lar, pharyngeal, laryngeal, trunk, and limb muscles, and 
the respiratory muscles can be seriously involved. The 
incidence of GM is approximately 0.15–61.33 per million 
person-years; however, in recent years, the incidence of 
MG has increased significantly [5, 6].
Currently, treatment for MG mainly includes cholines -
terase inhibitors and conventional immunosuppressants 
(glucocorticoids and nonsteroidal immunosuppressive 
agents) [ 7, 8]. The condition of many patients has been 
controlled using these drugs; however, poor curative 
effects are still observed in some patients, and approxi -
mately 20% of patients with MG do not respond to con -
ventional immunosuppressive treatment [ 9]. In addition, 
hormones and immunosuppressive agents have signifi -
cant side effects, such as diabetes, osteoporosis, hyper -
tension, obesity, and skin lesions, making some patients 
unable to adhere to immunosuppressive treatments [ 10, 
11]. Therefore, new drugs with stronger targeting, higher 
safety, and better efficacy, particularly monoclonal anti -
body drugs, have been developed recently.
According to their mechanism of action, new immune 
drugs for MG can be divided into the following three cat-
egories: neonatal Fc receptor inhibitors (FcRn), complex 
inhibitors, and B-cell therapies [ 12, 13]. After 2017, the 
US Food and Drug Administration (FDA) successively 
approved eculizumab, ravulizumab, efgartigimod, and 
rozanolixizumab as treatments for patients with MG 
[14–17]. In October 2023, the FDA approved zilucoplan 
as a treatment for adult generalized MG. However, owing 
to the limited evidence for the direct comparison of the 
safety and effectiveness of various drugs, the advantages 
and disadvantages of different monoclonal antibodies 
and immunosuppressants need to be further explored. 
Through a Bayesian network meta-analysis (NMA), the 
effectiveness and safety of different drugs can be com -
pared, and their effects can be ranked by collecting direct 
or indirect comparison evidence [ 18]. Therefore, in the 
present study, we conducted an NMA of all relevant 
immunotherapy methods and comprehensively com -
pared and ranked the strategies for MG treatment.
Methods
Search strategy
The study protocol was prospectively registered in 
the International Prospective Register for Systematic 
Reviews (CRD42024519160). This NMA complies with 
the Preferred Reporting Items for Systematic Reviews 
and Meta-Analyses statement [19].
Two reviewers independently performed a compre -
hensive literature search of PubMed, Embase, Cochrane 
Library, and Web of Science. The search covered all 
studies published between January 1, 2000 and March 
6, 2024. Discrepancies between the two reviewers were 
resolved through discussion or arbitration by a third 
reviewer (Shu-Yan Cong).
All studies were double-blind, randomized, placebo-
controlled trials on the efficacy of MG treatment and 
were published in English. To accurately search for the 
required studies, we searched for a combination of terms 
in Medical Subject Headings and general terms.
The included studies were those related to immunosup-
pressants and monoclonal antibodies and reported infor -
mation about the treatment effects. Details of the search 
strategy and extraction of specific literature are presented 
in Supplementary Table S1.
Inclusion criteria
We included all MG-related immunosuppressants and 
monoclonal antibodies that underwent randomized 
controlled trials (RCTs) after 2000. Participants in the 
included studies were adult patients diagnosed with gen -
eralized MG who met the Myasthenia Gravis Founda -
tion of America (MGFA) class II–V clinical classification 
at the time of screening. The patients were treated with 
immunosuppressants or monoclonal antibodies, and dif -
ferent doses of the same drug were administered to the 
same intervention group. The control group included in 
the experiment received a placebo treatment. At least 
one of the following four scores was the most important 
outcome in the included studies: MG Activities of Daily 
Living (MG-ADL), Quantitative MG (QMG), MG Com -
posite (MGC), and 15-item revised version of the MG 
Quality of Life (MG-QoL 15r) scores. The included stud -
ies reported adverse events (AEs) and severe AEs (SAEs) 
as adverse reactions.
Data extraction and outcome measures
We collected the following data: [ 1] the last name of the 
first author and the year of publication; [ 2] study phase, 
sample size, patient sex, patient age, intervention mea -
sures, disease duration, history of thymectomy, duration 
and dose of medication, serotype (AB AChR-positive 
and anti-MuSK antibody-positive and seronegative), and 
MGFA category; [3] outcome data for efficacy: MG-ADL, 
QMG, MGC, and MG-QOL 15r scores (mean, standard 

Page 3 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
deviation [SD]); and [ 4] outcome data for safety: drug-
related AEs and SAEs during the follow-up period. Data 
were extracted by two reviewers (Yue Qiao and Jian Gu) 
using a standardized data extraction table, and another 
reviewer (Shu-Yan Cong) checked the data. Any conflict -
ing observations were discussed, and a consensus was 
reached.
Quality assessment and risk of bias
In this NMA, we strictly adhered to the predefined inclu -
sion and exclusion criteria and only incorporated RCTs. 
To assess the risk of bias in the included studies, we used 
the Cochrane Collaboration’s risk of bias assessment tool 
[20], which covers six key domains: random sequence 
generation (selection bias), allocation concealment 
(selection bias), blinding of participants and person -
nel (performance bias), blinding of outcome assessment 
(detection bias), incomplete outcome data (attrition 
bias), and selective reporting (reporting bias) and other 
biases. The risk of bias in each study was evaluated by 
two independent reviewers (Yue Qiao and Jian Gu), who 
rated each domain as having “low risk, ” “high risk, ” or 
“unclear risk” according to the guidelines provided by the 
Cochrane tool. Any disagreements during the assessment 
were resolved through discussion or consultation with a 
third reviewer (Shu-Yan Cong).
Statistical analysis
The Bayesian NMA was performed using R statistical 
software (Version 4.2.3) [ 21] and STATA software (ver -
sion 15.0). The primary measures of effect were the odds 
ratio (OR) and mean difference (MD) for dichotomous 
and continuous outcomes, respectively, both with corre -
sponding 95% credible intervals (CrIs). If there were no 
raw data (for example, no SDs, only P-values or ranges 
were reported), the SDs and 95% CIs indicated in the 
publication were calculated using established methods 
for estimation [ 22]. When significant heterogeneity is 
detected (I² ≥ 50%), a random-effects model is applied to 
account for variability across studies. In contrast, when 
heterogeneity is low (I² < 50%) indicating greater con -
sistency among studies, a fixed-effects model is used.
Network comparisons of various interventions are illus -
trated in network maps, where each node represents an 
intervention, and the thickness of the connecting lines 
indicates the number of trials comparing the two inter -
ventions. The size of each node indicates the number 
of cases to which the intervention was applied. Global 
inconsistency was evaluated by comparing the Deviance 
Information Criterion (DIC) between the random- and 
fixed-effects models. A DIC difference of < 11 suggests 
superior global consistency [ 23]. Given that all compari -
sons involved monoclonal antibodies or immunosup -
pressive agents versus placebo or varying drug dosages, 
without direct comparisons between different monoclo -
nal antibodies or immunosuppressive agents, and closed 
loops were absent in the network plots, consistency was 
not assessed using the node-splitting method [ 24]. The 
surface under the cumulative ranking curve (SUCRA) 
value was calculated to rank the interventions accord -
ing to their efficacy and safety, with larger SUCRA values 
indicating superior performance [ 25]. For the outcomes 
of each trial, potential publication bias was assessed by 
visually inspecting the symmetry of the funnel plot.
Results
Study characteristics
After searching various databases, 1395 studies were 
identified. Two reviewers read the titles and abstracts 
and excluded duplicate studies, animal experiments, 
non-RCTs, and studies with outcome times and designs 
that did not match those of the required studies. Finally, 
20 studies were included in the present NMA [ 26–46]. 
Three trials included three intervention groups, whereas 
the remaining included two. A flowchart of the search 
process is shown in Fig.  1. In total, 1657 patients diag -
nosed with generalized MG were enrolled. Thirteen types 
of immunosuppressants or monoclonal antibodies were 
summarized: batoclimab, efgartigimod, nipocalimab, 
rozanolixizumab, ravulizumab, eculizumab, zilucoplan, 
iscalimab, belimumab, rituximab, tacrolimus, metho -
trexate, and mycophenolate mofetil. Treatment groups 
with different doses of the same drug were summarized. 
Patients’ baseline characteristics are shown in Table  1. 
The study duration ranged between 29 and 52 weeks. The 
number of participants ranged from 14 to 200. A total of 
1216 patients provided a serum AChR antibody status, 
among which 1137 provided positive serum samples.
NMA
Figure  2 shows a network map of various immunosup -
pressants and monoclonal antibodies, focusing on their 
efficacy and safety outcomes. Each node represents a dif -
ferent intervention, with the node size indicating the par-
ticipant count. The thickness of the connecting lines or 
edges between nodes indicates the number of trials com -
paring the two strategies.
MG-ADL score network
The NMA of MG-ADL included 20 studies involving 13 
drugs, in which different dosages of the same drug were 
not considered as separate treatment methods. Bato -
climab (MD: -2, 95% CrI: -2.7 to -1.3), eculizumab (MD: 
-1.8, 95% CrI: -3.2 to -0.42), methotrexate (MD: -1.5, 95% 
CrI: -2.9 to -0.029), ravulizumab (MD: -1.7, 95% CrI: -2.7 
to -0.66), rozanolixzumab (MD: -2.2, 95% CrI: -3 to -1.4), 
tacrolimus (MD: -1.1, 95% CrI: -1.8 to -0.41), and zilu -
coplan (MD: -2.1, 95% CrI − 3.2 to -1.1) demonstrated 

Page 4 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
superiority to the placebo. Notably, rozanolixzumab was 
superior to belimumab, efgartigimod, and mycophenolate 
mofetil (MDs ranging between 1.52 and 1.89). Zilucoplan 
demonstrated superiority to efgartigimod and mycophe -
nolate mofetil (MDs ranging between 1.46 and 1.57). 
Batoclimab was superior to efgartigimod and mycophe -
nolate mofetil (MDs ranging between − 1.43 and − 1.32). 
According to the SUCRA values, rozanolixzumab ranked 
first (85%), followed by zilucoplan (82%) and batoclimab 
(78%) (Table  2). Belimumab (21%), efgartigimod (25%), 
and placebo (7%) were the least effective therapies. The 
detailed results are presented in Supplementary Table S2. 
Cumulative probability analysis showed that rozanolixi -
zumab was associated with the greatest benefit in terms 
of MG-ADL, as shown in Fig. 3A.
QMG score network
The NMA of QMG included 21 studies involving 13 
drugs, in which different dosages of the same drug were 
not considered as separate treatment methods.
Batoclimab (MD: -5.3, 95% CrI: -6.5 to -4.1), eculi -
zumab (MD: -2.9, 95% CrI: -4.6 to -1.2), efgartigimod 
(MD: -1.8, 95% CrI: -2.9 to -0.69), ravulizumab (MD: -2, 
95% CrI: -3.3 to -0.74), rozanolixzumab (MD: -3, 95% 
CrI: -3.9 to -2.1), tacrolimus (MD: -1.4, 95% CrI: -2.8 to 
-0.066), and zilucoplan (MD: -2.8, 95% CrI: -4.1 to -1.5) 
demonstrated superiority to the placebo. Notably, bato -
climab demonstrated significant superiority to all the 
other treatments. Batoclimab had the highest SUCRA 
value (99%), followed by rozanolixzumab (79%) and 
eculizumab (75%) (Table  2). Rozanolixzumab demon -
strated significant superiority to nipocalimab and myco -
phenolate mofetil. Zilucoplan demonstrated significant 
Fig. 1 PRISMA flow diagram of the present network meta-analysis. PRISMA, Preferred Reporting Items for Systematic review and Meta-analysis
 

Page 5 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
Study phase Sample size Gender(M/F) Mean age(years) intervention Time since onset (y) Thymectomy Intervention periods AChR+ Outcome
Yan 2022(26)
NCT04346888
2 BAT680mg: 11
BAT340mg: 10
PLA:9
BAT680mg: 2/9
BAT340mg: 2/8
PLA:2/7
BAT680mg: 40.6 ± 16.8
BAT340mg: 36.4 ± 9.8
PLA:40.2 ± 9.3
BAT BAT680mg: 6.4 ± 5.7
BAT340mg: 9.8 ± 10.8
PLA:6.0 ± 6.8
BAT680mg: 3
BAT340mg: 3
PLA:2
43 days BAT680mg: 11
BAT340mg: 9
PLA:8
a.b.c.d.e.f.
Yan 2024(45)
NCT05039190
3 BAT:67
PLA:64
BAT:27/40
PLA:16/48
BAT:43.8 ± 13.9
PLA:43.7 ± 13.5
BAT NA BAT:23
PLA:14
6 weeks BAT:65
PLA:59
a.b.c.d.e.
Hewett 2018(27)
NCT01480596
2 BEL: 18
PLA: 21
BEL: 8/10
PLA: 7/14
BEL: 52.7 ± 17.32
PLA: 59 ± 13.88
BEL BEL: 6.95 ± 9.03
PLA: 8.30 ± 8.06
BEL: 6
PLA: 7
24 weeks BEL: 18
PLA: 20
a.b.c.e.f.
Howard 2017(28)
NCT01997229
3 ECU:62
PLA:63
ECU:21/41
PLA:22/41
ECU:47.5 ± 15.7
PLA:46.9 ± 18
ECU ECU:9.9 ± 8.1
PLA:9.2 ± 8.4
ECU:37
PLA:31
26 weeks NA a.b.c.d.f.
Howard 2019(29)
NCT02965573
2 EFG:12
PLA:12
EFG:5/7
PLA:4/8
EFG:55.3 ± 13.6
PLA:43.5 ± 19.3
EFG EFG:8.2 ± 9
PLA:13.3 ± 11.2
NA 78 days NA a.b.c.d.e.f.
Howard 2021(30)
NCT03669588
3 EFG:84
PLA:83
EFG:21/63
PLA:28/55
EFG:45.9 ± 14.4
PLA:48.2 ± 15
EFG EFG:10.1 ± 9
PLA:8.8 ± 7.6
EFG:59
PLA:36
8 weeks EFG:65
PLA:64
a.b.c.d.e.f.
GomezMancilla 2024(31)
NCT02565576
2 ISC:22
PLA:22
ISC:10/12
PLA:6/16
ISC:44.7 ± 13.5
PLA:43.3 ± 13.9
ISC ISC:8.2 ± 6.96
PLA:8.4 ± 8.47
NA 25 weeks ISC:22
PLA:22
a.b.c.d.e.f.
Antozzi 2024(32)
NCT03772587
2 NIP:54
PLA:14
NIP:25/29
PLA:6/8
NIP:57.5 ± 14.8
PLA:60.5 ± 14.5
NIP NIP:7.3 ± 7.31
PLA:13.2 ± 9.81
NA 57 days NIP:51
PLA:3
a.b.d.e.f.
Tuan 2022(33)
NCT03920293
3 RAV:86
PLA:89
RAV:42/44
PLA:44/45
RAV:58.0 ± 13.8
PLA:53.3 ± 16.1
RAV RAV:9.8 ± 9.7
PLA:10.0 ± 8.9
NA 26 weeks RAV:86
PLA:89
a.b.d.e.f.
Bril 2021(34)
NCT03971422
2 ROZ:21
PLA:22
ROZ:8/13
PLA:8/14
ROZ:50.5 ± 14.7
PLA:53 ± 15.7
ROZ NA ROZ:11
PLA:10
29 days ROZ:19
PLA:21
a.b.c.e.f.
Bril 2023(35)
NCT03971422
3 ROZ 7 mg:66
ROZ 10 mg:67
PLA:67
ROZ 7 mg:27/39
ROZ 10 mg:32/35
PLA:20/47
ROZ 7 mg:53.2 ± 14.7
ROZ 10 mg:51.9 ± 16.5
PLA:50.4 ± 17.7
ROZ NA ROZ 7 mg:32
ROZ 10 mg:20
PLA:31
43 days ROZ 7 mg:60
ROZ 10 mg:60
PLA:59
a.b.c.e.f.
Howard 2020(36)
NCT03315130
2 ZIL0.1 mg:15
ZIL0.3 mg: 14
PLA:15
ZIL:7/8
ZIL0.3 mg: 10/4
PLA:4/11
ZIL0.1 mg:45.5 ± 15.7
ZIL0.3 mg: 54.6 ± 15.5
PLA:48.4 ± 15.7
ZIL ZIL0.1 mg:6.5 ± 5.63
ZIL0.3 mg: 5.3 ± 6.38
PLA:6.3 ± 5.2
ZIL0.1 mg:8
ZIL0.3 mg: 7
PLA:5
12 weeks ZIL0.1 mg:15
ZIL0.3 mg: 14
PLA:15
a.b.c.d.e.f.
Howard 2023(37)
NCT04115293
3 ZIL:86
PLA:88
ZIL:34/52
PLA:41/47
ZIL:52.6 ± 14.6
PLA:53.3 ± 15.7
ZIL ZIL:9.3 ± 9.5
PLA:9 ± 10.4
ZIL:45
PLA:37
12 weeks ZIL:86
PLA:88
a.b.c.d.e.f.
Piehl 2022(38)
NCT02950155
3 RIT:25
PLA:22
RIT:18/7
PLA:15/7
RIT:67.4 ± 13.4
PLA:58 ± 18.6
RIT NA NA 16 weeks RIT:23
PLA:22
a.b.d.e.f.
Nowak 2022(39)
NCT02110706
2 RIT:25
PLA:27
RIT:14/11
PLA:15/12
RIT:53.2 ± 17.5
PLA:56.8 ± 17
RIT RIT:6.7 ± 6.5
PLA:4.4 ± 5.3
RIT:8
PLA:14
52 weeks RIT:25
PLA:27
a.b.c.d.e.f.
Zhou 2017(41)
NCT01325571
3 TAC:44
PLA:38
TAC:16/28
PLA:20/18
TAC:41 ± 12.8
PLA:44 ± 12.1
TAC TAC:27.9 ± 37.8 M
PLA:63.5 ± 90.2 M
NA 24 weeks NA a.b.e.f.
Yoshikawa 2011(40)
NCT00309088
3 TAC:40
PLA:40
TAC:17/23
PLA:13/27
TAC:45.9 ± 11.5
PLA:44.4 ± 12.36
TAC TAC:7.41 ± 9
PLA:7.94 ± 9.54
TAC:28
PLA:30
28 weeks NA a.b.e.f.
Pasnoor 2016(42)
NCT00814138
3 MTX:25
PLA:25
MTX:19/6
PLA:16/9
MTX:66.5 ± 13.85
PLA:68.6 ± 15.15
MTX NA NA 52 weeks NA a.b.c.d.e.
Meriggioli 2003(44) 2 MMF:7
PLA:7
MMF:2/5
PLA:2/5
MMF:57.7 ± 8.75
PLA:51.3 ± 12.75
MMF MMF:8.99
PLA:9.91
MMF:3
PLA:5
21 weeks MMF:5
PLA:6
b.
Table 1 Trial features and baseline characteristics of participants for 21 trials included in the network meta-analysis

Page 6 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
superiority to nipocalimab and mycophenolate mofetil. 
Eculizumab demonstrated significant superiority to nipo-
calimab. Nipocalimab was the least effective treatment 
according to the SUCRA value (13%), except for the pla -
cebo. The detailed results are presented in Supplemen -
tary Table S3. The cumulative probability analysis showed 
that batoclimab was associated with the greatest benefit 
in terms of QMG score, as shown in Fig. 3B.
MGC score network
The NMA of MGC included 13 studies involving nine 
drugs, in which different dosages of the same drug were 
not considered as separate treatment methods.
Batoclimab (MD: -5.1, 95% CrI: -6.8 to -3.4), eculi -
zumab (MD: -3.3, 95% CrI: -6.1 to -0.52), methotrexate 
(MD: -3.3, 95% CrI: -6.2 to -0.41), rozanolixzumab (MD: 
-4.5, 95% CrI: -5.3 to -3.8), and zilucoplan (MD: -3.1, 95% 
CrI: -4.9 to -1.3) demonstrated superiority to the placebo. 
Rozanolixzumab demonstrated significant superiority to 
belimumab and efgartigimod. Batoclimab had the highest 
SUCRA value (92%), followed by rozanolixzumab (85%), 
eculizumab (64%), and methotrexate (64%). Batoclimab 
demonstrated significant superiority to efgartigimod and 
belimumab. Belimumab was the least effective treatment 
according to the SUCRA value (15%), except for the pla -
cebo (Table 2). The detailed results are presented in Sup -
plementary Table S4. The cumulative probability analysis 
showed that batoclimab was associated with the greatest 
benefit in terms of MGC score, as shown in Fig. 3C.
MG-QoL 15r score network
The NMA of MG-QoL 15r included 13 studies involving 
nine drugs, in which different dosages of the same drug 
were not considered as separate treatment methods.
Batoclimab (MD: -3.4, 95% CrI: -4.9 to -1.8), eculi -
zumab (MD: -7.1, 95% CrI: -12 to -2.7), efgartigimod 
(MD: -2.1, 95% CrI: -3.8 to -0.53), and zilucoplan (MD: 
-3.1, 95% CrI: -4.9 to -1.3) demonstrated superiority to 
the placebo. Eculizumab demonstrated significant supe -
riority to efgartigimod, nipocalimab, rituximab, and 
ravulizumab. Eculizumab had the highest SUCRA value 
(96%), followed by batoclimab (72%) and zilucoplan 
(67%). Methotrexate was the least effective treatment 
according to the SUCRA value (35%), except for the pla -
cebo (Table 2). The detailed results are presented in Sup -
plementary Table S5. The cumulative probability analysis 
showed that eculizumab was associated with the great -
est benefit in terms of MG-QoL 15r score, as shown in 
Fig. 3D.
AE and SAE network
The NMA of AEs included 19 studies involving 12 drugs.
Rozanolixzumab was associated with a higher risk 
of AEs than did efgartigimod, mycophenolate mofetil, 
Study phase Sample size Gender(M/F) Mean age(years) intervention Time since onset (y) Thymectomy Intervention periods AChR+ Outcome
Sanders 2008a(43) 3 MMF:88
PLA:88
MMF:42/46
PLA:40/48
MMF:49 ± 18
PLA:49.7 ± 18.4
MMF MMF:35.1 ± 30.8
PLA:41.1 ± 39.2 M
MMF:23
PLA:25
36 weeks NA a.b.e.f.
Sanders 2008b(46) 3 MMF:41
PLA:39
MMF:24/17
PLA:23/16
MMF:57.1 ± 18.8
PLA:55.3 ± 17.7
MMF MMF:2 ± 4.1
PLA:2 ± 4.4
NA 12 weeks NA a.b.e.
a. Myasthenia Gravis Activities of Daily Living (MG-ADL) score
b. Quantitative Myasthenia Gravis (QMG) score
c. Myasthenia Gravis Composite (MGC) score
d. 15-item revised version of the Myasthenia Gravis Quality of Life (MG-QoL 15r) score
e. adverse effects (AEs)
f. several adverse effects (SAEs)
ROZ, rozanolixzumab; BAT, batoclimab; EFG, efgartigimod; NIP, nipocalimab; ECU, eculizumab; ZIL, zilucoplan; RAV, ravulizumab; BEL, belimumab; RIT, rituximab; ISC, iscalimab; PLA, placebo; MMF, mycophenolate mofetil; 
TAC, Tacrolimus; MTX, Methotrexate; NA, not applicable; AChR, nicotinic acetylcholine receptor
Table 1 (continued)
 

Page 7 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
and the placebo. The results of the ranking according to 
SUCRA values showed that belimumab (85%) exhibited 
the highest safety, followed by iscalimab (75%), efgartigi -
mod (73%), mycophenolate mofetil (66%), placebo (55%), 
methotrexate (51%), batoclimab (50%), nipocalimab 
(43%), tacrolimus (39%), rituximab (35%), ravulizumab 
(32%), zilucoplan (29%), and rozanolixzumab (17%) 
(Table 2).
The NMA of SAEs included 18 studies involving 12 
drugs. Rozanolixzumab was associated with a higher risk 
of SAEs than did belimumab, eculizumab, batoclimab, 
nipocalimab, and the placebo. Additionally, ravulizumab 
was associated with a higher risk of SAEs than did beli -
mumab, eculizumab, and nipocalimab. Mycophenolate 
mofetil was associated with a higher risk of SAEs than did 
belimumab, eculizumab, and nipocalimab. Nipocalimab 
had the highest SUCRA value (89%), whereas rozanolix -
zumab had the lowest SUCRA value (7%) (Table  2). The 
detailed results are presented in Supplementary Tables 
S6 and S7. The cumulative probability analysis showed 
that belimumab was associated with AEs, as shown in 
Fig. 3E, and that nipocalimab was associated with SAEs, 
as shown in Fig. 3F.
Risk of bias and heterogeneity
The outcomes of risk of bias are shown in Fig. 4, revealing 
that most included studies had a low risk of bias. Eight 
studies had one uncertain risk of bias, three had two, and 
one had four. These uncertainties in the risk levels were 
predominantly found in the category of other biases. In 
addition, one study had a high risk of bias in the category 
of other biases. Funnel plots were used to assess publica -
tion bias for the outcomes, as shown in Fig.  5. The fun -
nel plot appeared visually symmetrical, indicating no 
potential publication bias, thereby further supporting 
the robustness of the study results. Global inconsistency 
was evaluated through the development of consistency 
and inconsistency models. The negligible discrepancies 
observed in the DIC and additional parameters between 
the fixed- and random-effects models suggested minimal 
inconsistency, underscoring the reliability and stability 
of our results (Supplementary Table S8). Furthermore, 
a heterogeneity analysis of multiple outcomes was per -
formed. The findings showed that most comparisons 
exhibited low heterogeneity, except those in the studies 
of Bril et al. (Supplementary Figures S1–S6).
Fig. 2 Risk of bias graph and summary
 

Page 8 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
Discussion
In total, 1657 participants from 21 studies were included 
in the present NMA to investigate the efficacy and safety 
of immunosuppressants and monoclonal antibodies as 
treatments for MG. The results of the pairwise meta-
analyses showed that, compared with other interven -
tions, batoclimab had a better effect on improving the 
QMG and MGC scores, with SUCRA values of 99% and 
92%, respectively. According to the MG-ADL assessment, 
rozanolixzumab demonstrated the best performance in 
improving the MG symptoms. Eculizumab had a SUCRA 
value of 96% and performed better than the other drugs 
in improving the MG-QoL 15r score. Batoclimab, ecu -
lizumab, and zilucoplan were superior to the placebo in 
terms of all four efficacy scores. The risk of AEs due to 
immunosuppressants and monoclonal antibodies for 
treating MG was also investigated. Compared with the 
placebo, none of the drugs significantly increased the risk 
of AEs, except for rozanolixzumab.
To assess the efficacy of the drugs, we used the MG-
ADL, QMG, MGC, and MG-QoL 15r scores. Notably, 
the MG-ADL and QMG scores were used in almost all 
studies, with the MG-ADL score frequently designated 
as the primary outcome measure. When the MG-ADL 
score was prioritized as the primary evaluation criterion, 
rozanolixizumab emerged as the top candidate based 
on the ranking probability, followed by zilucoplan and 
batoclimab. When drug efficacy was assessed using the 
QMG and MGC scores, batoclimab ranked first, with the 
highest probability ranking, whereas rozanolixizumab 
ranked second. An NMA published in 2023 on the effi -
cacy and safety of monoclonal antibodies for treating MG 
suggested that rozanolixzumab had the highest prob -
ability ranking, followed by batoclimab and zilucoplan 
[47]. A recent meta-analysis [ 48] suggested that roza -
nolixizumab was more effective than the placebo when 
efficacy was assessed using the MG-ADL score, whereas 
batoclimab was more effective than the placebo when 
efficacy was evaluated using the QMG score. This find -
ing was largely consistent with that of the present study; 
however, the ranking of batoclimab slightly decreased 
in the present study when efficacy was assessed using 
the MG-ADL score, possibly due to the inclusion of the 
most recent research findings related to batoclimab in 
our analysis [45]. The most recent Phase 3 study of bato -
climab included more patients, thus reducing bias and 
making the results more credible. Rozanolixizumab is a 
humanized monoclonal antibody designed to treat MG 
[34]. Its therapeutic mechanism is based on the target -
ing and inhibition of FcRn. Rozanolixizumab blocks FcRn 
to induce the degradation of immunoglobulins (IgGs) 
[49], including the pathogenic autoantibodies respon -
sible for MG. This degradation can decrease the immune 
system’s attack on the neuromuscular junction, thereby 
Table 2 The SUCRA values for each treatment
Treatment AEs Rank SAEs Rank MG-ADL Rank QMG Rank MGC Rank MG-QoL 15r Rank
Batoclimab 49.86% 7 72.27% 3 78.02% 3 99.66% 1 92.48% 1 72.04% 2
Efgartigimod 73.25% 3 61.25% 5 25.49% 12 48.68% 7 24.96% 8 49.45% 5
Nipocalimab 42.62% 8 89.08% 1 47.03% 8 13.18% 13 - - 35.30% 8
Rozanolixizumab 19.99% 13 6.52% 13 84.53% 1 79.34% 2 85.40% 2 - -
Ravulizumab 32.32% 11 16.91% 12 66.43% 5 54.43% 5 - - 41.25% 6
Eculizumab - - 70.93% 4 68.95% 4 74.84% 3 64.02% 3 96.66% 1
Zilucoplan 28.97% 12 42.62% 9 81.61% 2 74.55% 4 61.40% 5 66.98% 3
Iscalimab 74.64% 2 54.99% 6 50.87% 7 34.89% 11 41.33% 6 56.20% 4
Belimumab 84.85% 1 85.30% 2 21.03% 13 49.84% 6 15.34% 9 - -
Rituximab 35.30% 10 49.32% 7 38.86% 10 48.60% 8 39.57% 7 36.49% 7
Tacrolimus 39.49% 9 42.86% 8 44.60% 9 39.53% 10 - - - -
Placebo 55.23% 5 37.05% 10 6.65% 14 7.41% 14 11.53% 10 11.78% 10
Methotrexate 50.75% 6 - - 57.11% 6 46.96% 9 63.96% 4 34.86% 9
Mycophenolate Mofetil 65.74% 4 20.92% 11 28.82% 11 28.09% 12 - - - -
AEs, adverse events; SAEs, severe adverse events; MG-ADL, Myasthenia Gravis Activities of Daily Living; QMG, Quantitative Myasthenia Gravis; MGC, Myasthenia Gravis
Composite; MG-QoL 15r,15-item revised version of the Myasthenia Gravis Quality of Life

Page 9 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
alleviating MG symptoms. Additionally, rozanolixzumab 
was the first and only drug approved by the FDA to treat 
adult patients with anti-AChR and anti-MuSK antibody-
positive generalized MG. Recent clinical trials indicate 
that rozanolixizumab has therapeutic benefits that are 
not inferior to those of plasma exchange and intravenous 
immunoglobulin and that its administration through 
subcutaneous injection facilitates its dissemination. 
Fig. 4 Ranking of the cumulative probabilities for basic parameters and adverse events: (A) MG-ADL, (B) QMG, (C) MGC, (D) MG-QoL 15r, (E) AEs, and (F) 
SAEs. MG-ADL, Myasthenia Gravis Activities of Daily Living; QMG, Quantitative Myasthenia Gravis; MGC, Myasthenia Gravis Composite; MG-QoL 15r, 15-
item revised version of the Myasthenia Gravis Quality of Life; AEs, adverse events; SAEs, severe adverse events
 
Fig. 3 Network graphs of randomized controlled trials comparing the efficacy and safety of mAbs and immunosuppressants for treating myasthenia 
gravis: (A) MG-ADL, (B) QMG, (C) MGC, (D) MG-QoL 15r, (E) AEs, and (F) SAEs. mAbs, monoclonal antibodies; MG-ADL, Myasthenia Gravis Activities of Daily 
Living; QMG, Quantitative Myasthenia Gravis; MGC, Myasthenia Gravis Composite; MG-QoL 15r, 15-item revised version of the Myasthenia Gravis Quality 
of Life; AEs, adverse events; SAEs, severe adverse events
 

Page 10 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
However, its safety and efficacy require further evalua -
tion after its market launch. If the effectiveness of roza -
nolixizumab is validated in the real world, it may become 
the preferred medication for the treatment of MG in the 
future [50]. Previous NMAs have primarily confirmed the 
efficacy of rozanolixizumab [ 47], with fewer analyses of 
its safety, indicating that its AEs are not superior to those 
of other monoclonal antibodies. Recent meta-analyses 
have shown that rozanolixizumab has superior efficacy; 
however, the incidence of AEs was higher in the rozano -
lixizumab group than in the placebo group [ 48, 51]. The 
AEs associated with rozanolixizumab were mostly mild 
to moderate in severity. The most commonly reported 
AEs included headache, diarrhea, pyrexia, and nausea 
[34, 35]. The increased incidence of rozanolixizumab-
related AEs was likely due to rozanolixizumab-induced 
mild to moderate headaches, which required no addi -
tional treatment [ 35]. Regarding safety, rozanolixizumab 
ranked last regarding the likelihood of AEs and SAEs in 
the present study. The forest plot showed that the safety 
of rozanolixizumab was significantly worse than that of 
the placebo, which is consistent with the findings of pre -
vious studies. A recent meta-analysis [ 48] has suggested 
that batoclimab is superior to the placebo in terms of 
QMG, MGC, and MG-QoL 15r scores. The present study 
indicated that batoclimab ranked first in the likelihood of 
improving the QMG and MGC scores, which is consis -
tent with the findings of recent meta-analyses. However, 
an NMA by Chen et al. [ 47] suggested that batoclimab 
did not rank first in the likelihood of improving the QMG 
and MGC scores, which is inconsistent with the findings 
of the present study. The present NMA, which incor -
porated the results of the most recent clinical trials of 
batoclimab, had higher credibility. Based on the ranking 
for the likelihood of AEs, batoclimab was in the middle 
range, whereas it was ranked third based on the ranking 
for the likelihood of SAEs. This suggests that batoclimab 
has a relatively good safety profile, particularly regarding 
severe adverse reactions. Batoclimab treatment was asso -
ciated with hypercholesterolemia. However, after admin -
istering batoclimab to patients, a rapid recovery and no 
related complications are observed [26]. An RCT of bato-
climab showed that serum cholesterol levels increased 
and then decreased after discontinuing the drug [ 52]. 
Previous studies did not directly compare the safety of 
batoclimab with that of other FcRn inhibitors [ 53]. The 
present NMA validated the efficacy and safety of bato -
climab. Although batoclimab can be recommended as 
an option to reduce the risk of adverse events associated 
with rozanolizumab, the final treatment decision should 
be based on the patient’s individual needs and specific 
clinical requirements. Eculizumab inhibits the cleav -
age of complement protein C5 into C5a and C5b, which 
are key components in the formation of the membrane 
attack complex that damages cells [ 54]. In cases of MG, 
the activation of the complement system contributes to 
damage at the neuromuscular junction, leading to muscle 
weakness [ 55]. By preventing the formation of C5a and 
C5b, eculizumab reduces complement-mediated dam -
age at the neuromuscular junction, thereby improving 
Fig. 5 Funnel plots for efficacy and safety outcomes: (A) MG-ADL, (B) QMG, (C) MGC, (D) MG-QoL 15r, (E) AEs, and (F) SAEs. MG-ADL, Myasthenia Gravis 
Activities of Daily Living; QMG, Quantitative Myasthenia Gravis; MGC, Myasthenia Gravis Composite; MG-QoL 15r, 15-item revised version of the Myasthe-
nia Gravis Quality of Life; AEs, adverse events; SAEs, severe adverse events
 

Page 11 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
muscle strength and reducing MG symptoms. Eculi -
zumab was first approved for the treatment of MG by 
the United States FDA in 2017 [14], followed by approval 
in other regions, including the European Union. In the 
present NMA, eculizumab ranked high in terms of the 
likelihood of improving the MG-QoL 15r, MGC, and 
QMG scores, ranking first in terms of the MG-QoL 15r 
score. Studies on patients with generalized anti-AChR 
antibody-positive MG treated with eculizumab indicated 
that eculizumab demonstrated higher efficacy than that 
of rituximab [56]. However, owing to its specific targeting 
of the complement system and associated costs, its use 
may be reserved for specific patient populations or those 
with severe diseases not adequately controlled by other 
therapies.
In the present study, three immunosuppressants were 
included: methotrexate, mycophenolate mofetil, and 
tacrolimus. Among these, methotrexate ranked higher 
than the other two drugs in terms of both the MG-ADL 
and QMG scores. The other two immunosuppressants 
were not included in the comparison regarding the MGC 
and MG-QoL 15r scores. Methotrexate has been used 
to treat MG in some patients, particularly those who are 
not sensitive enough to other treatments or develop an 
adverse reaction [ 57]. The present study indicates that 
methotrexate has better efficacy than that of other immu-
nosuppressants; however, its effectiveness is moderate 
compared with that of some monoclonal antibodies. A 
systematic review of the use of methotrexate for gener -
alized MG showed that it is a potentially safe and effec -
tive alternative to azathioprine as a steroid-sparing agent, 
especially in developing countries where the high cost 
of azathioprine limits compliance [ 58]. This finding sup -
ports those of the present study.
In the present study, drug safety was assessed using 
two indicators: AEs and SAEs. When evaluated based on 
AEs, the top three drugs were belimumab, iscalimab, and 
efgartigimod, respectively, with rozanolixizumab ranking 
last. When assessed based on SAEs, the top three drugs 
in the probability ranking were nipocalimab, belimumab, 
and batoclimab, respectively. Belimumab targets and 
inhibits B lymphocyte stimulation, which plays a role in 
reducing abnormal B-cell activity in autoimmune condi -
tions. A study evaluated the effectiveness of belimumab 
in treating MG and revealed no significant difference in 
improvement between belimumab and the placebo based 
on the primary endpoint, which was the change in the 
QMG score; however, it did not increase the risk of AEs 
[27]. This is consistent with the findings in the present 
study.
The present study is the most recent NMA to com -
prehensively compare common monoclonal antibod -
ies and immunosuppressants for treating MG. This 
NMA included a wide range of drugs, incorporated 
high-quality RCTs, and included the most recent drug 
trial results [ 45]. Clinically, individualized treatment 
plans that balance efficacy and safety are essential for 
optimizing patient outcomes in the management of 
myasthenia gravis. However, the present study has some 
limitations. First, the number of included studies was 
limited, with few direct comparisons; therefore, indirect 
estimates were relied on rather than direct estimates. 
Second, we compared the overall drug outcomes without 
considering different doses, with significant variations in 
the follow-up period. Third, we included only published 
studies and excluded unpublished studies. Finally, some 
studies lacked data on the percentage of antibody-nega -
tive patients, changes in serum IgG levels, and antibody 
levels compared to the baseline values. Future research 
should focus on evaluating the long-term safety profiles 
and real-world effectiveness of these treatments.
Conclusion
The results of this study indicated that the included 
immunosuppressants and monoclonal antibodies were 
more effective than the placebo. Rozanolixizumab and 
batoclimab may be the most effective treatments for gen -
eralized MG. However, rozanolixizumab was associated 
with a higher likelihood of AEs and SAEs. Methotrexate 
may be superior to other immunosuppressants in terms 
of efficacy.The conclusions provide a strong reference for 
the clinical selection of more effective therapeutic drugs 
and also offer insights for the further development of 
related drug experiments. Owing to the lack of trials with 
direct comparisons and statistical uncertainty in SUCRA 
rankings, specific case analyses of clinical medications 
are needed to determine treatment plans.
Supplementary Information
The online version contains supplementary material available at https://doi.
org/10.1186/s12967-024-05751-1.
Supplementary Material 1: Table S1. Detailed search strategy for the four 
databases. Table S2. League table for MG-ADL. Table S3. League table for 
QMG. Table S4. League table for MGC. Table S5. League table for MG-QoL 
15r. Table S6. League table for AEs. Table S7. League table for SAEs. Table 
S8. The results of consistency and inconsistency tests. Figure S1. Sensitivity 
analysis of MG-ADL. Figure S2. Sensitivity analysis of QMG. Figure S3. Sensi-
tivity analysis of MGC. Figure S4. Sensitivity analysis of MG-QoL 15r. Figure 
S5. Sensitivity analysis of AEs. Figure S6. Sensitivity analysis of SAEs
Author contributions
All authors contributed to the conception and design of this study. JG: subject 
design and writing—original draft. YQ: investigation. SC: conceptualization, 
supervision, reviewing, and editing. RH: conceptualization, supervision, 
reviewing, and editing. All the authors contributed to the manuscript and 
approved the submitted version.
Funding
None.

Page 12 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
Data availability
The original contributions presented in this study are included in the 
article/supplementary material. Further inquiries can be directed to the 
corresponding author.
Declarations
Conflict of interest
The authors declare no conflict of interest.
Received: 13 July 2024 / Accepted: 8 October 2024
References
1. Gilhus NE, Tzartos S, Evoli A, Palace J, Burns TM, Verschuuren J. Myasthenia 
gravis. Nat Rev Dis Primers. 2019;5(1):30.
2. Gilhus NE, Verschuuren JJ. Myasthenia gravis: subgroup classification and 
therapeutic strategies. Lancet Neurol. 2015;14(10):1023–36.
3. Lazaridis K, Tzartos SJ. Autoantibody specificities in Myasthenia gravis; 
implications for Improved Diagnostics and therapeutics. Front Immunol. 
2020;11:212.
4. Verschuuren JJ, Huijbers MG, Plomp JJ, Niks EH, Molenaar PC, Martinez-
Martinez P , et al. Pathophysiology of myasthenia gravis with antibodies to the 
acetylcholine receptor, muscle-specific kinase and low-density lipoprotein 
receptor-related protein 4. Autoimmun Rev. 2013;12(9):918–23.
5. Bubuioc AM, Kudebayeva A, Turuspekova S, Lisnic V, Leone MA. The epidemi-
ology of myasthenia gravis. J Med Life. 2021;14(1):7–16.
6. Joensen P . Myasthenia gravis incidence in a general North Atlantic isolated 
population. Acta Neurol Scand. 2014;130(4):222–8.
7. Sanders DB, Wolfe GI, Benatar M, Evoli A, Gilhus NE, Illa I, et al. International 
consensus guidance for management of myasthenia gravis: executive sum-
mary. Neurology. 2016;87(4):419–25.
8. Narayanaswami P , Sanders DB, Wolfe G, Benatar M, Cea G, Evoli A, et al. Inter-
national Consensus Guidance for Management of Myasthenia gravis: 2020 
update. Neurology. 2021;96(3):114–22.
9. Zhang Q, Ge H, Gui M, Yang M, Bi Z, Ma X, et al. Polymorphisms in drug 
metabolism genes predict the risk of refractory myasthenia gravis. Ann Transl 
Med. 2022;10(21):1155.
10. Suh J, Goldstein JM, Nowak RJ. Clinical characteristics of refractory myasthe-
nia gravis patients. Yale J Biol Med. 2013;86(2):255–60.
11. Silvestri NJ, Wolfe GI. Treatment-refractory myasthenia gravis. J Clin Neuro-
muscul Dis. 2014;15(4):167–78.
12. Menon D, Bril V. Pharmacotherapy of generalized myasthenia gravis with 
special emphasis on newer biologicals. Drugs. 2022;82(8):865–87.
13. Zeng R, Glaubitz S, Schmidt J. Antibody therapies in Autoimmune Inflam-
matory myopathies: Promising Treatment options. Neurotherapeutics. 
2022;19(3):911–21.
14. ALEXION. Fda Approves Soliris® (Eculizumab) for the Treatment of Patients 
with Generalized Myasthenia Gravis (Gmg) 2017 [ https://myasthenia.org/
Portals/0/Press%20Release%20Soliris%20FDA%20Approval.pdf
15. AstraZeneca. Ultomiris Approved in the Us for Adults with Generalised 
Myasthenia Gravis 2022 [ https://www.astrazeneca.com/media-centre/press-
releases/2022/ultomiris-approved-in-the-us-for-adults-with-generalisedmy-
asthenia-gravis.html
16. U N, UCB Announces US. FDA Approval of Rystiggo[®] (Rozanolixizumab-
Noli) for the Treatment of Adults with Generalized Myasthenia Gravis 2023 [ 
https://www.ucb.com/stories-media/Press-Releases/article/UCB-announces-
USFDA-approval-of-RYSTIGGOR-rozanolixizumab-noli-for-the-treatment-of-
adultswith-generalized-myasthenia-gravis
17. Argenx. Argenx Announces US. Food and Drug Administration Approval of 
Vyvgart Hytrulo (Efgartigimod Alfa and Hyaluronidase-Qvfc) Injection for 
Subcutaneous Use in Generalized Myasthenia Gravis 2023 [ https://www.
globenewswire.com/news-release/2023/06/20/2691658/0/en/argenx-
AnnouncesU-S-Food-and-Drug-Administration-Approval-of-VYVGART-
Hytrulo-efgartigimodalfa-and-hyaluronidase-qvfc-Injection-for-Subcutane-
ous-Use-in-GeneralizedMyasthenia-Grav.html
18. Rouse B, Chaimani A, Li T. Network meta-analysis: an introduction for clini-
cians. Intern Emerg Med. 2017;12(1):103–11.
19. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. 
The PRISMA 2020 statement: an updated guideline for reporting systematic 
reviews. BMJ. 2021;372:n71.
20. Higgins JP , Altman DG, Gøtzsche PC, Jüni P , Moher D, Oxman AD, et al. The 
Cochrane collaboration’s tool for assessing risk of bias in randomised trials. 
BMJ. 2011;343:d5928.
21. van Valkenhoef G, Lu G, de Brock B, Hillege H, Ades AE, Welton NJ. Automat-
ing network meta-analysis. Res Synth Methods. 2012;3(4):285–99.
22. Wan X, Wang W, Liu J, Tong T. Estimating the sample mean and standard 
deviation from the sample size, median, range and/or interquartile range. 
BMC Med Res Methodol. 2014;14:135.
23. Spiegelhalter DJ, Best NG, Carlin BP , Van Der Linde A. Bayesian measures 
of Model Complexity and Fit. J Royal Stat Soc Ser B: Stat Methodol. 
2002;64(4):583–639.
24. Chen K, Li H, Yang L, Jiang Y, Wang Q, Zhang J, et al. Comparative efficacy and 
safety of antidepressant therapy for the agitation of dementia: a systematic 
review and network meta-analysis. Front Aging Neurosci. 2023;15:1103039.
25. Shim S, Yoon BH, Shin IS, Bae JM. Network meta-analysis: application and 
practice using Stata. Epidemiol Health. 2017;39:e2017047.
26. Yan C, Duan RS, Yang H, Li HF, Zou Z, Zhang H, et al. Therapeutic effects 
of Batoclimab in Chinese patients with generalized Myasthenia gravis: a 
Double-Blinded, randomized, placebo-controlled phase II study. Neurol Ther. 
2022;11(2):815–34.
27. Hewett K, Sanders DB, Grove RA, Broderick CL, Rudo TJ, Bassiri A, et al. 
Randomized study of adjunctive belimumab in participants with generalized 
myasthenia gravis. Neurology. 2018;90(16):e1425–34.
28. Howard JF Jr., Utsugisawa K, Benatar M, Murai H, Barohn RJ, Illa I, et al. Safety 
and efficacy of eculizumab in anti-acetylcholine receptor antibody-positive 
refractory generalised myasthenia gravis (REGAIN): a phase 3, randomised, 
double-blind, placebo-controlled, multicentre study. Lancet Neurol. 
2017;16(12):976–86.
29. Howard JF Jr., Bril V, Burns TM, Mantegazza R, Bilinska M, Szczudlik A, et al. 
Randomized phase 2 study of FcRn antagonist efgartigimod in generalized 
myasthenia gravis. Neurology. 2019;92(23):e2661–73.
30. Howard JF Jr., Bril V, Vu T, Karam C, Peric S, Margania T, et al. Safety, efficacy, 
and tolerability of efgartigimod in patients with generalised myasthenia 
gravis (ADAPT): a multicentre, randomised, placebo-controlled, phase 3 trial. 
Lancet Neurol. 2021;20(7):526–36.
31. GomezMancilla B, Meriggioli MN, Genge A, Roubenoff R, Espié P , Dupuy C, et 
al. Efficacy and safety of iscalimab, a novel anti-CD40 monoclonal antibody, 
in moderate-to-severe myasthenia gravis: a phase 2 randomized study. J Clin 
Neurosci. 2024;119:76–84.
32. Antozzi C, Guptill J, Bril V, Gamez J, Meuth SG, Nowak RJ, et al. Safety and 
Efficacy of Nipocalimab in patients with generalized Myasthenia Gravis. 
Neurology. 2024;102(2):e207937.
33. Vu T, Meisel A, Mantegazza R, Annane D, Katsuno M, Aguzzi R, et al. Terminal 
complement inhibitor ravulizumab in generalized Myasthenia Gravis. NEJM 
Evid. 2022;1(5):EVIDoa2100066.
34. Bril V, Benatar M, Andersen H, Vissing J, Brock M, Greve B, et al. Efficacy and 
safety of Rozanolixizumab in moderate to severe generalized Myasthenia 
gravis: a phase 2 Randomized Control Trial. Neurology. 2021;96(6):e853–65.
35. Bril V, Drużdż A, Grosskreutz J, Habib AA, Mantegazza R, Sacconi S, et al. Safety 
and efficacy of rozanolixizumab in patients with generalised myasthenia 
gravis (MycarinG): a randomised, double-blind, placebo-controlled, adaptive 
phase 3 study. Lancet Neurol. 2023;22(5):383–94.
36. Howard JF Jr., Nowak RJ, Wolfe GI, Freimer ML, Vu TH, Hinton JL, et al. Clini-
cal effects of the self-administered subcutaneous complement inhibitor 
zilucoplan in patients with moderate to severe generalized Myasthenia 
gravis: results of a phase 2 Randomized, Double-Blind, Placebo-Controlled, 
Multicenter Clinical Trial. JAMA Neurol. 2020;77(5):582–92.
37. Howard JF Jr., Bresch S, Genge A, Hewamadduma C, Hinton J, Hussain Y, et 
al. Safety and efficacy of zilucoplan in patients with generalised myasthenia 
gravis (RAISE): a randomised, double-blind, placebo-controlled, phase 3 
study. Lancet Neurol. 2023;22(5):395–406.
38. Piehl F, Eriksson-Dufva A, Budzianowska A, Feresiadou A, Hansson W, Hietala 
MA, et al. Efficacy and safety of Rituximab for New-Onset generalized 
Myasthenia gravis: the RINOMAX Randomized Clinical Trial. JAMA Neurol. 
2022;79(11):1105–12.
39. Nowak RJ, Coffey CS, Goldstein JM, Dimachkie MM, Benatar M, Kissel JT, et al. 
Phase 2 trial of Rituximab in Acetylcholine receptor antibody-positive gener-
alized Myasthenia gravis: the BeatMG Study. Neurology. 2022;98(4):e376–89.

Page 13 of 13
Gu et al. Journal of Translational Medicine          (2024) 22:955 
40. Yoshikawa H, Kiuchi T, Saida T, Takamori M. Randomised, double-blind, 
placebo-controlled study of tacrolimus in myasthenia gravis. J Neurol Neuro-
surg Psychiatry. 2011;82(9):970–7.
41. Zhou L, Liu W, Li W, Li H, Zhang X, Shang H, et al. Tacrolimus in the treatment 
of myasthenia gravis in patients with an inadequate response to gluco-
corticoid therapy: randomized, double-blind, placebo-controlled study 
conducted in China. Ther Adv Neurol Disord. 2017;10(9):315–25.
42. Pasnoor M, He J, Herbelin L, Burns TM, Nations S, Bril V, et al. A randomized 
controlled trial of methotrexate for patients with generalized myasthenia 
gravis. Neurology. 2016;87(1):57–64.
43. Sanders DB, Hart IK, Mantegazza R, Shukla SS, Siddiqi ZA, De Baets MH, et 
al. An international, Phase III, randomized trial of mycophenolate mofetil in 
myasthenia gravis. Neurology. 2008;71(6):400–6.
44. Meriggioli MN, Rowin J, Richman JG, Leurgans S. Mycophenolate mofetil for 
myasthenia gravis: a double-blind, placebo-controlled pilot study. Ann N Y 
Acad Sci. 2003;998:494–9.
45. Yan C, Yue Y, Guan Y, Bu B, Ke Q, Duan R et al. Batoclimab vs Placebo for 
generalized Myasthenia gravis: a Randomized Clinical Trial. JAMA Neurol. 
2024;81(4):336-345.
46. A trial of. Mycophenolate mofetil with prednisone as initial immunotherapy 
in myasthenia gravis. Neurology. 2008;71(6):394–9.
47. Chen H, Qiu Y, Yin Z, Wang Z, Tang Y, Ni H, et al. Efficacy and safety of the 
innovative monoclonal antibodies in adults with generalized myasthenia 
gravis: a bayesian network analysis. Front Immunol. 2023;14:1280226.
48. Li J, Wu X, Chu T, Tan X, Wang S, Qu R et al. The efficacy and safety of FcRn 
inhibitors in patients with myasthenia gravis: a systematic review and meta-
analysis. J Neurol. 2024;271(5):2298-2308.
49. Flammer J, Neziraj T, Rüegg S, Pröbstel AK. Immune mechanisms in Epilep-
togenesis: update on diagnosis and treatment of Autoimmune Epilepsy 
syndromes. Drugs. 2023;83(2):135–58.
50. Matic A, Alfaidi N, Bril V. An evaluation of rozanolixizumab-noli for the treat-
ment of anti-AChR and anti-MuSK antibody-positive generalized myasthenia 
gravis. Expert Opin Biol Ther. 2023;23(12):1163–71.
51. Rissardo JP , Caprara ALF, Durante Í, Rauber A. Lithium-associated movement 
disorder: a literature review. Brain Circ. 2022;8(2):76–86.
52. Kahaly GJ, Dolman PJ, Wolf J, Giers BC, Elflein HM, Jain AP , et al. Proof-
of-concept and Randomized, Placebo-controlled trials of an FcRn 
inhibitor, Batoclimab, for thyroid Eye Disease. J Clin Endocrinol Metab. 
2023;108(12):3122–34.
53. Zhu LN, Hou HM, Wang S, Zhang S, Wang GG, Guo ZY, et al. FcRn inhibitors: 
a novel option for the treatment of myasthenia gravis. Neural Regen Res. 
2023;18(8):1637–44.
54. Patriquin CJ, Kuo KHM. Eculizumab and Beyond: the past, Present, and future 
of complement therapeutics. Transfus Med Rev. 2019;33(4):256–65.
55. Conti-Fine BM, Milani M, Kaminski HJ. Myasthenia gravis: past, present, and 
future. J Clin Invest. 2006;116(11):2843–54.
56. Nelke C, Schroeter CB, Stascheit F, Pawlitzki M, Regner-Nelke L, Huntemann N, 
et al. Eculizumab versus Rituximab in generalised myasthenia gravis. J Neurol 
Neurosurg Psychiatry. 2022;93(5):548–54.
57. Rodolico C, Bonanno C, Brizzi T, Nicocia G, Trimarchi G, Lupica A, et al. 
Methotrexate as a steroid-sparing Agent in Myasthenia gravis: a preliminary 
retrospective study. J Clin Neuromuscul Dis. 2021;23(2):61–5.
58. Prado MB Jr., Adiao KJB. Methotrexate in generalized myasthenia gravis: a 
systematic review. Acta Neurol Belg. 2023;123(5):1679–91.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations. 