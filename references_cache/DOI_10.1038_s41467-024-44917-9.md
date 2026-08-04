---
reference_id: "DOI:10.1038/s41467-024-44917-9"
title: Applying a genetic risk score model to enhance prediction of future multiple sclerosis diagnosis at first presentation with optic neuritis
authors:
- Pavel Loginovic
- Feiyi Wang
- Jiang Li
- Lauric Ferrat
- Uyenlinh L. Mirshahi
- H. Shanker Rao
- Axel Petzold
- Jessica Tyrrell
- Harry D. Green
- Michael N. Weedon
- Andrea Ganna
- Tiinamaija Tuomi
- David J. Carey
- Richard A. Oram
- Tasanee Braithwaite
journal: Nature Communications
year: '2024'
doi: 10.1038/s41467-024-44917-9
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-024-44917-9.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41467-024-44917-9.pdf
---

# Applying a genetic risk score model to enhance prediction of future multiple sclerosis diagnosis at first presentation with optic neuritis
**Authors:** Pavel Loginovic, Feiyi Wang, Jiang Li, Lauric Ferrat, Uyenlinh L. Mirshahi, H. Shanker Rao, Axel Petzold, Jessica Tyrrell, Harry D. Green, Michael N. Weedon, Andrea Ganna, Tiinamaija Tuomi, David J. Carey, Richard A. Oram, Tasanee Braithwaite
**Journal:** Nature Communications (2024)
**DOI:** [10.1038/s41467-024-44917-9](https://doi.org/10.1038/s41467-024-44917-9)

## Content

Abstract

                    Optic neuritis (ON) is associated with numerous immune-mediated inflammatory diseases, but 50% patients are ultimately diagnosed with multiple sclerosis (MS). Differentiating MS-ON from non-MS-ON acutely is challenging but important; non-MS ON often requires urgent immunosuppression to preserve vision. Using data from the United Kingdom Biobank we showed that combining an MS-genetic risk score (GRS) with demographic risk factors (age, sex) significantly improved MS prediction in undifferentiated ON; one standard deviation of MS-GRS increased the Hazard of MS 1.3-fold (95% confidence interval 1.07–1.55,
                    P
                     < 0.01). Participants stratified into quartiles of predicted risk developed incident MS at rates varying from 4% (95%CI 0.5–7%, lowest risk quartile) to 41% (95%CI 33–49%, highest risk quartile). The model replicated across two cohorts (Geisinger, USA, and FinnGen, Finland). This study indicates that a combined model might enhance individual MS risk stratification, paving the way for precision-based ON treatment and earlier MS disease-modifying therapy.

Article https://doi.org/10.1038/s41467-024-44917-9
Applying a genetic risk score model to
enhance prediction of future multiple
sclerosis diagnosis atﬁrst presentation
with optic neuritis
Pavel Loginovic 1,17,F e i y iW a n g2,17,J i a n gL i 3,17,L a u r i cF e r r a t4,
Uyenlinh L. Mirshahi 3,H .S h a n k e rR a o3,A x e lP e t z o l d5,6,7,
Jessica Tyrrell 8, Harry D. Green 9, Michael N. Weedon4, Andrea Ganna2,10,
Tiinamaija Tuomi 2,11,12,13,D a v i dJ .C a r e y3, UKBB Eye & Vision Consortium*,
FinnGen*, Geisinger-Regeneron DiscovEHR Collaboration*,
Richard A. Oram
4,14,18 & Tasanee Braithwaite 15,16,18
Optic neuritis (ON) is associated with numerous immune-mediated inﬂam-
matory diseases, but 50% patients are ultimately diagnosed with multiple
sclerosis (MS). Differentiating MS-ONfrom non-MS-ON acutely is challenging
but important; non-MS ON often requires urgent immunosuppression to
preserve vision. Using data from the United Kingdom Biobank we showed that
combining an MS-genetic risk score (GRS) with demographic risk factors (age,
sex) signiﬁcantly improved MS prediction in undifferentiated ON; one stan-
d a r dd e v i a t i o no fM S - G R Si n c r e a s e dt h eH a z a r do fM S1 . 3 - f o l d( 9 5 %c o nﬁdence
interval 1.07– 1.55, P < 0.01). Participants stratiﬁed into quartiles of predicted
risk developed incident MS at rates varying from 4% (95%CI 0.5– 7%, lowest risk
quartile) to 41% (95%CI 33– 49%, highest risk quartile). The model replicated
across two cohorts (Geisinger, USA, and FinnGen, Finland). This study indi-
cates that a combined model might enhance individual MS risk stratiﬁcation,
paving the way for precision-based ON treatment and earlier MS disease-
modifying therapy.
Optic neuritis (ON) presents most frequently in young adults with
subacute uni- or bilateral vision loss1. It is a rare but treatable cause of
blindness. The incidence of ON has been stable over decades, and
varies by latitude, with a population-based incidence of 3.7 to 5.1 per
100k person-years in the United Kingdom (UK) and United States of
America (USA), respectively
2,3. Approximately two-thirds are undiffer-
entiated at presentation with the remainder having either a prior
diagnosis of Multiple Sclerosis (MS) or preceding infectious or
immune-mediated inﬂammatory disease (I-IMID)
2.B y ﬁve years of
follow-up, approximately 20% of undifferentiated ON cases are
diagnosed with MS, compared to 0.1% controls (adjusted Hazard Ratio
[aHR] 285,P < 0.001)2. By 15 years, up to 50% of all ON cases, excluding
those with bilateral presentation, are diagnosed with MS4,5.
Importantly, ON ultimately associated with diagnosis of MS (MS-
ON)6, including Clinically Isolated Syndrome (CIS, consisting of ON
plus magnetic resonance imaging features of demyelination at
presentation)
1, has different management and prognosis to non-MS-
associated ON. In MS-ON, vision usually recovers spontaneously to
near-baseline over 3 months
7. Trial evidence indicates an equivocal
role for corticosteroid therapy8– 10, although there may be a role for
Received: 16 October 2023
Accepted: 9 January 2024
Check for updates
A full list of afﬁliations appears at the end of the paper. *Lists of authors and their afﬁliations appear at the end of the paper. e-mail: R.Oram@exeter.ac.uk
Nature Communications|         (2024) 15:1415 1
1234567890():,;
1234567890():,;

hyperacute corticosteroid therapy11. Non-MS ON may be associated
with subsequent diagnosis of corticosteroid-responsive diseases
including sarcoidosis, neuromyelitis optica spectrum disorder
(NMOSD), and vasculitides
12. In marked contrast to MS-ON, axonal
injury can be swift and vision loss irreversible, with signiﬁcant impacts
on patients’lives13. Clinicians managing acute undifferentiated ON face
a challenging and time-critical decision while awaiting diagnostic
investigations
14: whether or not to initiate potentially sight-saving
corticosteroid therapy which risks serious adverse effects15. There is an
unmet clinical need for a tool to improve acute risk stratiﬁcation, dif-
ferentiating those at low future MS risk, who may beneﬁt from urgent
corticosteroids, from those at high future MS risk, who may bene ﬁt
from earlier disease-modifying therapy to reduce long-term neurolo-
gical disability
16,17.
Many autoimmune and autoinﬂammatory diseases, including MS,
are heritable. Almost 20% of MS risk heritability can be attributed to
common genetic variants16,18, and the latest genome-wide association
studies (GWAS) from the International Multiple Sclerosis Genetics
Consortium (IMSGC)
19 study of 47,429 MS patients and 68,374 control
subjects identiﬁed over 200 associated loci 20.T h ei d e n t iﬁcation of
strong, complex, human leukocyte antigen (HLA) class II associations,
combined with non-HLA associations, offers the opportunity to aggre-
gate MS genetic risk as a continuous MS genetic risk score (GRS).
Additional risk factors for MS include female sex, age at onset
21,l a t i t u d e
of country of residence, low serum 25-hydroxyvitamin22– 24,i n c r e a s e d
body mass index 22,24– 26, Epstein-Barr virus seropositivity 27,a n d
smoking28,29.I nt h e ﬁrst MS-GRS model, De Jager et al. (2009) studied
2215 individuals with MS and 2189 controls, and in independent samples
conﬁrmed that 16 MS susceptibility alleles (2 MHC alleles and 14 non-
MHC alleles) had modest discriminatory ability, which was enhanced by
integrating of non-genetic risk factors (sex (ROC AUC 0.74), smoking
and anti-EBV antibody titers (ROC AUC 0.68) in the model
30.T h e i rs t u d y
included subjects with MS-ON, including CIS, and showed that they
share a similar genetic architecture as those with MS. To our knowledge,
genetic data has not previously been used in combination with other
risk factors to aid MS risk strati ﬁcation in undifferentiated ON which
includes, but is not limited to, CIS. This UK Biobank (UKBB) study had
two aims: Firstly, to determine w hether an MS-GRS, created using
published GWAS summary statistics, aids prediction of future MS in
people presenting with undifferentiated ON; secondly, whether com-
bining MS-GRS with demographic and clinical variables enhances MS
diagnosis risk stratiﬁcation at ﬁrst ON presentation.
Results
MS, ON and MS-ON cases and demographic characteristics
From 483,506 unrelated individuals with available genetic and pheno-
type data, of whom 83.9% were of European ancestry, we identiﬁed 2369
MS cases (prevalence 0.49%, or 490 per 100,000 participants) and 687
ON cases (prevalence 0.14% or 142 per 100,000 participants) (Fig.1). ON
cases included 545 (545 out of 687, 79.3%) who were not known to have
MS at ﬁrst ON presentation and 142 (20.7%) with prior or simultaneous
diagnosis of MS (MS-ON). During cumulative follow-up from ﬁrst ON
presentation to latest data extraction in 2019 or death (median 18.4 years,
IQR 9.9– 30.2) a further 124 out of 545 (22.8%) were diagnosed with MS.
Demographic and clinical characteristics are summarised in
Table 1 and Supplementary Table 5 for the cases presenting with MS-
ON and undifferentiated ON, in comparison to the group with MS
without ON, and the control population. At ON presentation, the
Fig. 1 | Flow diagram of participants, illustrating exclusions and quality
control steps.The ﬁgure describes the exclusion and inclusion criteria used in the
UK Biobank (UKBB) population. The boxes in the last row show the number of
participants within each group: healthy controls (yellow), MS without ON (MS only,
blue), MS-associated ON (MS-ON, purple), and ON without MS (ON only, red). An
extended version is available in the supplement, which describes sources of diag-
noses in more detail (Supplementary Fig. 1). UKBB UK Biobank, QC quality control,
ON optic neuritis, MS multiple sclerosis.
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 2

female to male ratio was 1.8 in the initially undifferentiated ON group
(n = 545) and 2.9 in the MS-ON group (n = 142), in comparison to 2.5 in
the group with MS alone ( n = 2103), and 1.2 in the control population
(n = 480,690) (χ², 9 degrees of freedom,P < 0.00001). The mean age at
onset of undifferentiated ON was 44.7 (SD 15.0, range 1 to 80) years
compared to 47.3 (12.2, range 20 to 73) years in the group presenting
with MS-ON. The percentage of European ancestry cases was 84.8%
(n = 462) in undifferentiated ON and 85.2% ( n =1 2 1 ) i n M S - O N a t p r e -
sentation, compared to 87.7% (n = 1845) in the MS without ON group,
and 83.9% ( n = 403,051) in the control population. Supplementary
Tables 6 and 7 present the data for all ON and all MS by end of
cumulative follow-up.
MS-GRS was discriminative of MS
W ea s s e s s e dt h eM S - G R Si nM Sc a s e sa n dt h er e s to ft h eU K B B
(including ON without MS) (Fig.2a). Both the HLA and non-HLA mean
scores were higher in people with MS (mean 0.74 (SD 0.78) vs 0.29 (SD
0.71), P < 0.0001 for HLA, 2.88 (SD 0.92) vs 2.37 (0.92), P <0 . 0 0 0 1f o r
non-HLA) and were discriminative of MS (ROC-AUC (95% CI) 0.666
(0.663– 0.669) and 0.656 (0.653 – 0.659) respectively, Fig. 2 and Sup-
plementary Fig. 2). The full MS-GRS had a ROC AUC of 0.721
(0.718– 0.723), and 0.752 (0.750– 0.755) when combined with a subset
of risk factors associated with MS (sex, age at UKBB entry, Townsend
deprivation index) and the ﬁrst four genetic principal components
(Fig. 2a, d).
Genetic overlap of MS, ON and MS-associated ON
We assessed the distribution of MS-GRS in healthy controls, ON only
(undifferentiated ON at the end of follow-up), MS-ON and MS only
(Fig. 2a– c), with groups deﬁned by diagnosis at the end of cumulative
follow-up. We found that the MS-GRS distribution of the non-MS-ON
group (mean 3.02 (SD 1.29) lay between that of healthy controls 2.66
(1.15) and MS-ON cases 3.71 (1.17) (P < 0.0001 for both, Fig.2a). The MS-
GRS signiﬁcantly differentiated MS cases from cases with non-MS-ON
Table 1 | Demographic characteristics of participants presenting with MS-ON versusu n d i f f e r e n t i a t e dO N ,a n dc o m p a r i s o nw i t h
healthy control population, and group with MS without ON (MS Only) between three datasets
MS-ON at
presentation
MS Only Controls Undifferentiated ON at
presentation
Hazard ratio of MS diagnosis in
undifferentiated ON
Study participants (n) UKBB 142 2103 480,690 545
Geisinger 280 1901 113,751 835
FinnGen 262 1544 369,633 977
Of which European
ancestry (%)
UKBB 121 (85.2) 1845 (87.7) 403,051 (83.9) 462 (84.8) 0.77 (0.48 –1.24), P = 0.28
Geisinger 247 (88.2) 1656 (87.1) 96,569 (84.9) 751 (89.9)
FinnGen NA NA NA NA
Median age at cohort
enrolment (IQR,
range), years
UKBB 54.5 (48 –59,
40 to 69)
56 (49–62,
40 to 70)
58 (50–63,
37 to 73)
57 (50–62, 40–70) 0.94 (0.92 –0.97), P < 0.0001**
Geisinger 52.4 (45 –62,
23 to 84)
56 (49–62,
40 to 70)
58 (50–63,
37 to 73)
59.8 (48–73, 14–89)
FinnGen 46.6 (37 –55, 9 to 82) 50.3 (40 –60,
10 to 90)
56.2 (41–67,
0.0 to 105)
49 (37–62, 6–95)
n Females (F:M) UKBB 106 (2.9) 1504 (2.5) 260,093 (1.2) 352 (1.8) 2.20 (1.41– 3.45), P = 0.0005*
Geisinger 220 (3.7) 1440 (3.1) 68,175 (2.4) 546 (1.9)
FinnGen 216 (4.7) 1133 (2.8) 206,268 (1.3) 711 (2.7)
ON diagnosed between
18 and 50 years of age
UKBB 89 (62.3) NA NA 336 (62.0) 2.43 (1.43– 4.17), P = 0.0014*
Geisinger 125 (44.6) NA NA 259 (31.0)
FinnGen 220 (84.0) NA NA 705 (72.2)
Mean MS-GRS (SD) UKBB 3.74 (1.15) 3.71 (1.17) 2.66 (1.15) 3.17 (1.30) 1.29 (1.07– 1.55), P =
0.0067*
Geisinger 3.80 (1.28) 3.35 (1.31) 2.74 (1.14) 2.92 (1.23)
FinnGen 3.96 (1.24) 3.73 (1.25) 2.74 (1.13) 3.41 (1.30)
Variables not included in Cox regression
Mean age at onset ON
(SD, range), years
UKBB 47.3 (12.2, 20 to 73) NA NA 44.7 (15.0, 1 to 80)
Geisinger 40.8 (11.5, 15.7
to 69.6)
NA NA 52.2 (17.1, 11 to 89)
FinnGen 38.7 (11.3, 10.5
to 72.9)
NA NA 38.8 (15.4, 7 to 89)
Mean age at onset MS
(SD, range), years
UKBB 38.7 (9.6, 18 to 58) 44.9 (12.5, 15 to 80) NA 45.5 (11.2, 20 to 73)
Geisinger 45.0 (12.1, 16 to 77) 47.1 (13.0, 4 to 88) NA 40.4 (11.9, 15 to 80)
FinnGen 33.5 (9.7, 11 to 68) 41.3 (12.6, 13 to 87) NA 36.3 (11.3, 15 to 76)
Mean Non-HLA-
GRS (SD)
UKBB 2.86 (0.86) 2.89 (0.93) 2.37 (0.92) 2.63 (0.98)
Geisinger 3.12 (0.90) 2.85 (0.98) 2.50 (0.91) 2.62 (0.95)
FinnGen 3.11 (0.86) 3.01 (0.93) 2.44 (0.90) 2.86 (0.99)
Mean HLA-GRS (SD) UKBB 0.88 (0.74) 0.73 (0.795) 0.29 (0.71) 0.53 (0.77)
Geisinger 0.68 (0.82) 0.50(0.78) 0.25 (0.69) 0.30 (0.75)
FinnGen 0.85 (0.85) 0.72 (0.78) 0.30 (0.69) 0.55 (0.77)
P-values in the rightmost column are derived from a univariate MS-free Cox proportional hazard model in the undifferentiated ON UKBB population, unless speciﬁed otherwise with an asterisk: *P-
values from multivariate Cox MS-free survival model with binary age at ON diagnosis, sex, and MS-GRS; **P-values from a model with binary age at ON diagnosis, sex, MS-GRS and age at UK Biobank
(UKBB) enrolment.
Variables included in the ﬁnal MS-free survival model are highlighted in bold.
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 3

P < 0.0001
P < 0.0001
P < 0.0001
P = 0.2499
P = 0.7249
P < 0.0001
P < 0.0001
P < 0.0001
P < 0.0001
P < 0.0001
P < 0.0001
P = 0.0003
a
b
c
d
e
f
Fig. 2 | MS-GRS distribution and ROC-AUC analysis across three cohorts.
a– c MS-GRS distribution violin plots: comparative distribution of MS-GRS (multiple
sclerosis genetic risk score) among different participant groups in three datasets:
UK Biobank (a), Geisinger (b), and FinnGen (c). Groups are deﬁned on the x-axis:
healthy controls (Controls), individuals with optic neuritis without MS (ON only),
MS-associated optic neuritis (MS-ON), and individuals with MS without optic
neuritis (MS only). The mean is represented as a white circle, interquartile range as a
black box, and the outside line shows the kernel density estimate of the underlying
distribution. Each colour corresponds to a speciﬁc group: healthy controls (yellow),
ON without MS (red), MS without ON (blue), and MS-ON (purple). The statistical
analysis utilized two-sided Welch’s t-test with Bonferroni correction term to
account for multiple comparisons.d– f ROC-AUC analysis: receiver operating
characteristic area under the curve (ROC-AUC) analysis for differentiation between
any form of MS (including MS only and MS-ON) versus healthy controls in three
distinct datasets: UK Biobank (d), Geisinger (e), and FinnGen (f). The null model
(grey line) encompassed the same covariates as the MS-GRS+covariates model (red
line) but excluded the MS-GRS. MS-GRS without covariates is shown as a blue line.
Covariates included in the models were: sex, TDI (Townsend Deprivation Index),
age at cohort entry, and the ﬁrst four principal components for UK Biobank;
reported sex, index age, and theﬁrst four principal components for Geisinger; and
sex, age at DNA sample collection, and the ﬁrst four principal components for
FinnGen. The ROC-AUC analysis provides insight into the discriminatory power of
the models in distinguishing between MS cases and healthy controls.
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 4

at the end of study follow-up (3.62 (1.22), P < 0.0001), but not from
cases with MS-ON (Table 1 and Fig. 2a, Supplementary Table 6). Fig-
ure 2 further demonstrates the distribution of MS-GRS in external
validation datasets, with in-detail description provided in Supple-
mentary Results. In individuals with MS-ON, MS-GRS did not differ
signiﬁcantly whether MS diagnosis preceded or followed ﬁrst ON
presentation in UKBB, although deviations from this were observed in
one of the external datasets (Supplementary Fig. 9). There was a weak
association between MS-GRS and age at onset of MS (R
2 = 0.011,
P < 0.0001); higher MS-GRS was associated with younger age at MS
diagnosis (Supplementary Fig. 10).
MS-GRS predictive of future MS after ﬁrst diagnosis of ON
For the MS-free survival analysis, we limited our primary analysis of
MS-GRS to undifferentiated ON cases (n = 545) after excluding people
with MS diagnosed before ON (n = 122), and cases with ﬁrst presenta-
tion of MS including ON (n = 20). This group had a median cumulative
f o l l o w - u pp e r i o do f1 8 . 4( I Q R1 0– 30) years. We included both prevalent
ON (435/545 diagnosed before UKBB entry) and incident ON (110/545,
diagnosed after UKBB entry). The outcome event, MS diagnosis, was
documented in 22.9% (n = 124) cases, at a median interval of 3.8 years
(IQR 0.8– 12.2) years from ON to MS diagnosis.
Signiﬁcant variables in Cox proportional hazard model single
variable analysis included sex, binary age at ON diagnosis and MS-GRS
only (Table 1 and Supplementary Table 5). These variables all remained
signiﬁcant in multivariable analysis. Ancestry-associated principal
components, and interaction between age at ON onset and sex were
not signiﬁcant in the multivariable model and were excluded (Sup-
plementary Results 2.6). Proportional hazard assumptions were met in
the ﬁnal model at P < 0.05 in UKBB (Scaled Schoenfeld ’sr e s i d u a l s
Supplementary Fig. 14). The model containing MS-GRS, sex and binary
age at diagnosis calibrated well at 5, 10, and 20 years of follow-up
(Fig. 3b– d) and the distribution of predicted cumulative MS risk
(expressed as predicted partial hazard) is shown in Fig.3a. MS-GRS was
signiﬁcantly associated with future development of MS, with adjusted
Hazard Ratio (95% CI) of 1.29 (1.07 – 1.55), P < 0.01) per one standard
deviation increase in MS-GRS. Stratiﬁcation by quartiles of predicted
risk (Fig. 4,S u p p l e m e n t a r yF i g .1 5 )i d e n t iﬁed individuals who, at dif-
ferent durations of follow-up, were at relatively low risk of MS (Percent
diagnosed with MS at the end of the follow-up, 3.6%, 95% CI 0.5– 6.8%),
intermediate risk (14.7%, 8.8 – 20.7%), higher risk (31.6%, 23.8 – 39.4%)
and highest MS risk (41.2%, 32.9 – 49.4%) (Fig. 5a). The median pre-
dicted partial hazard for each quartile is displayed in Supplementary
Fig. 15. The sex-difference by quartile of predicted risk is illustrated in
Fig. 5d and Supplementary Fig. 16. Lastly, we evaluated whether a full
model (MS-GRS, binary age at onset, sex) performed better than cov-
ariates alone using time-dependant ROC-AUC up to 35 years (Supple-
mentary Fig. 4), and found the average time-ROC-AUC for the full
model was 0.627 vs 0.609 for the null model. It is worth mentioning
that both absolute values and the difference between AUCs were
a
bc d
Fig. 3 | Predicted risk of MS by Sex and model calibration plots for 5-, 10-, and
20-year horizons.Panel (a) shows boxen plots of predicted partial hazard based on
participants’MS-GRS, sex and age at ON diagnosis for undifferentiated ON that did
not develop MS (ON only, red) and those who did (MS-ON, blue) by the end of
cumulative follow-up. Grey centerline shows the median, with the darkest shade
around showing second and third quartiles. Each successive level outward contains
half of the remaining data and is shaded in lighter colour. Outliers are shown as
diamonds. Panels (b– d) illustrate calibration plots of the Cox model at three points
in time (5, 10, and 20 years, respectively). The smoothed calibration curve is shown
in red, and ideal calibration as a black dotted line. X-axis is the predicted probability
of developing MS up to 5, 10, and 20 years post ON diagnosis for ( b– d),
respectively.
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 5

lowest in UKBB compared to other datasets, which could be explained
by the lack of standardised follow-up in UKBB and over ﬁtting of
covariates.
External validation
The MS prevalence was 1285 per 100,000 people in Geisinger and 556
per 100,000 people in FinnGen. In the FinnGen database, there were
977 cases of undifferentiated ON, of whom 369 (37.8%) developed MS
with median of 1.02 years (IQR 0.24 to 5.46 years). In the Geisinger
database, there were 835 cases of undifferentiated ON, of whom 140
(16.8%) developed MS with median latency of 0.32 years (IQR
0.06– 1.68). MS-GRS was higher in both MS-ON and MS alone than
either healthy controls or non-MS-ON in both validation cohorts
(Fig. 2). It is worth mentioning that in both Geisinger and FinnGen MS-
ON cases had higher MS-GRS than MS cases without ON— this was not
observed in UKBB, and to our knowledge, has not been previously
reported (Fig.2b, c). MS-GRS was discriminative of MS cases vs healthy
controls in both Geisinger (0.744 for MS-GRS with sex, index age,ﬁrst
four principal components, 0.650 for MS-GRS alone) and FinnGen
(0.764 for MS-GRS with sex, age at DNA sample collection, and theﬁrst
four principal components, 0.737 for MS-GRS alone) (Fig. 2e, f), and
both HLA- and non-HLA were independently discriminative of MS
(Supplementary Fig. 2). Amongst people with undifferentiated ON, the
median risk of developing MS was 16.8% in the Geisinger population
and 37.8% in FinnGen population. We used the multivariable Cox MS-
free survival model trained on UKBB data in the Geisinger and FinnGen
datasets and found that it calibrated well after adjusting for differing
prevalence of MS in these different population cohorts (Supplemen-
tary Fig. 3). Using the model to split the data into quartiles of predicted
MS risk, we observed differing proportions of incident MS over
cumulative follow-up of 5.8 years (IQR 1.6– 10.8) in Geisinger, and 8.6
years (IQR 1.6– 18.4) in FinnGen. Speciﬁcally, in the lowest quartile of
MS-GRS predicted risk, 6.7% (95% CI 3.7– 10.1%) in Geisinger, and 10.2%
(95% CI 6.4– 14.0%) in FinnGen developed MS. Whereas in the highest
quartile of MS-GRS predicted risk, 30.6% (95% CI 24.4 – 36.9%) in Gei-
singer, and 60.7% (95% CI 54.5 – 66.8%) in FinnGen developed MS
(Supplementary Fig. 3). Lastly, in Both Geisinger and FinnGen, full Cox
survival model in undifferentiated ON (MS-GRS, sex, and binary ON
diagnosis between 18 and 50) had better time-ROC-AUC for MS pre-
diction than models containing covariates only (sex and binary age):
0.711 vs 0.692 in Geisinger, and 0.692 vs 0.647 in FinnGen (Supple-
mentary Fig. 4).
Sensitivity analyses
In subgroup analysis of European ancestry British individuals (84%
participants),ﬁndings were similar to the main analysis (Supplemen-
tary Results Section 3). Speciﬁcally, the MS-GRS had a very similar ROC
AUC of 0.750 (95% CI 0.746– 0 . 7 5 3 ) ,w h e nc o m b i n e dw i t hr i s kf a c t o r s
associated with MS (sex, age at UKBB entry, Townsend deprivation
index) and ﬁrst four genetic principal components. Similarly, in the
Cox proportional hazard model, the Hazard Ratio (95% CI) of future MS
diagnosis amongst participants presenting with undifferentiated ON
was 1.29 (1.05 – 1.58, P < 0.05) per standard deviation increase in
MS-GRS.
In subgroup analysis of non-European ancestry British individuals
(16% participants), ﬁndings were also similar to the main analysis
(Supplementary Table 12), but without statistical signi ﬁcance, on
account of the small number of participants. Speciﬁcally, the MS-GRS
had a very similar ROC AUC of 0.753 (95% CI 0.746 – 0.760) when
combined with risk factors associated with MS (sex, age at UKBB entry,
Townsend deprivation index) and ﬁrst four genetic principal compo-
nents. Similarly, in the Cox proportional hazard model, the Hazard
Ratio (HR) (95% CI) of future MS diagnosis amongst participants pre-
senting with undifferentiated ON was 1.40 (0.89 – 2.22, P = 0.15) per
standard deviation increase in MS-GRS versus 1.29 (1.07– 1.55, P <0 . 0 1 )
in the whole of UKBB. The HR for female sex was 1.81 (0.53 – 6.24,
P = 0.35) versus 2.20 (1.41– 3.45), P < 0.001), and the HR for age 18 – 50
years at ON diagnosis was 2.47 (0.69 – 8.77, P = 0.16) versus 2.43
(1.41– 4.17, P < 0.001), as compared to the whole of UKBB, respectively.
Additional subgroup analyses restricted to either cases diagnosed
after 20 years of age or diagnoses based on either hospital episode
statistics (HES) or primary care records (GP records) revealed nearly
identical results both for ROC-AUC MS-GRS performance and Cox
models of future MS risk in undifferentiated ON. A summary of these
subgroups and comparisons is provided in Supplementary Table 12.
Pilot application
Here will illustrate how the combined model could be integrated into
an application for use in clinical practice to estimate individual risk:
https://mspredictor.com.
Discussion
This pioneering investigation establishes a link between an individual’s
combined genetic susceptibility, as measured by the MS-GRS encom-
passing numerous MS-associated loci with common alleles, and the
subsequent risk of MS development in those experiencing an initial
episode of undifferentiated ON. Moreover, we unveil a strati ﬁcation
paradigm for individuals with undifferentiated ON, integrating the MS-
GRS, age at ON onset, and sex, which delineates cohorts characterised
by varying future MS risks: low (3.6%), intermediate (14.7%), higher
(31.6%), and highest (41.2%). Signi ﬁcantly, our study demonstrates
robustness through the successful replication and validation of the
composite MS-GRS model across two distinct datasets from the USA
and Finland, populations also predominantly of European ancestry.
Fig. 4 | Kaplan–Meier analysis of MS-free survival. Kaplan– Meier analysis
demonstrating MS-free survival trends based on quartiles of predicted MS risk.
Quartile divisions were determined by the forecasted partial hazard of Multiple
Sclerosis (MS), derived from individual characteristics utilizing the UK Biobank
(UKBB)-trained Cox model. The time span to the event is calculated from the onset
of optic neuritis (ON) diagnosis to the identiﬁcation of MS, or the conclusion of
follow-up for cases subjected to censoring. MS-free survival curves depicting
quartiles of predicted risk for the validation cohort are provided in Supplementary
Fig. 3 for further reference.
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 6

Fig. 5 | Incidence of multiple sclerosis development in undifferentiated optic
neuritis. a– c Cumulative incidence graphs: Illustration of the percentage of par-
ticipants experiencing undifferentiated optic neuritis (ON) within three distinct
datasets: UK Biobank (a), Geisinger (b), and FinnGen (c). The analysis is stratiﬁed by
quartile of predicted Multiple Sclerosis (MS) risk, with colours representing quar-
tiles: orange— ﬁrst, red— second, purple— third, and blue— fourth. The time points
represent four horizons of cumulative follow-up, with squares representing 5 years,
circles— 10 years, triangles— 20 years, and crosses— end of follow-up. Vertical lines
denote 95% conﬁdence intervals (95% CI) for the reported percentages estimated
using normal approximation. Numbers adjacent to each marker indicate the
cumulative number of people who developed MS in each quartile by time horizon.
The total number of participants within each quartile are shown below the x-axis.
d– f Sex-speciﬁc MS diagnosis rates: Graph depicting the percentage of each sex
who were subsequently diagnosed with MS by the end of follow-up, by quartile of
predicted MS risk. Percentage calculated as number of females (circles) or males
(triangles) with MS-ON divided by the total number of that sex within a quartile. The
size ratio of markers within a quartile corresponds to the participant sex ratio.
Numbers adjacent to each plot indicate the sex-speciﬁc number of participants with
MS-ON versus the total number of either males or females in that group. Vertical
lines indicate 95% CI for the sex-speciﬁc percentages estimated using normal
approximation. Paneld is UK Biobank (UKBB),e is Geisinger,f is FinnGen cohort.“*”
indicates a range, rather than exact value due to FinnGen’s data protection policy
on presenting potentially identiﬁable data. Remaining males (less than ﬁve parti-
cipants), 100% of who developed MS, are not presented for this reason. It is
important to note the differing y-axis scales in panels (c)a n d(f).
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 7

While it has been long-established that ON may be the ﬁrst pre-
sentation of MS, the additional risk stratiﬁcation outlined in this study
could valuably aid management of ON, and greater international
consensus on this
1, in the time-critical window before neuroimaging
and serum and cerebrospinalﬂuid investigations are available. In usual
clinical practice, European ancestry British women aged 18 to 50
years, who present with mild-moderate vision impairment, would not
typically be offered corticosteroid therapy
8,a n dt h eM S - G R Sw o u l d
identify most of these individuals to be at enhanced MS genetic risk.
Whereas, urgent corticosteroid therapy may be better targeted to the
smaller number of individuals at low MS genetic risk, who are more
likely to have an alternative, and potentially corticosteroid-responsive,
cause for ON, averting irreversible vision loss. A low-risk MS-GRS could
also reduce inadvertent initiation of interferon therapy in patients
whose ON is later determined to be associated with NMOSD. Similarly,
there may be value in avoidance of urgent corticosteroid therapy for a
s m a l ln u m b e ro fp a t i e n t sa g e dl e s st h a n1 8o ro v e r5 0y e a r s ,w h o s e
presentation is ‘atypical’f o rM S( e . g . ,v i s i o nw o r s et h a n6 / 6 0 ,n op a i n
on eye movements or no improvement) but whose MS-GRS reveals
high MS risk
15. The availability of an MS-GRS combined model, in the
context of undifferentiated ON, may help advance understanding of a
clinically isolated syndrome, the forme fruste of ON in MS. Indeed,
there is increasing recognition of MS clinical phenotypes falling on a
continuum of disease severity and progression over time
16, and further
research is needed to determine whether individuals at high MS risk
should be directed to MS services more rapidly, for consideration of
disease-modifying therapy.
Limitations
The primary analysis was performed on individuals of all ancestries,
with subgroup analyses on European and non-European ancestry
British individuals. Ancestry was not a signi ﬁcant predictor of future
MS diagnosis in patients presenting with undifferentiated ON, but non-
European populations are underrepresented in UKBB. A recent study
indicates that MS-GRS derived from predominantly white European
ancestry populations do not translate well to South Asian ancestry
populations
31. It will be important to continue to develop large, diverse
ancestry population biobanks and research studies to address this
deﬁciency and avoid perpetuating health inequalities.
MS-free survival may have been affected by cohort intrinsic con-
founding, such as age at UKBB enrolment (Supplementary Fig. 18) and
lack of standardised follow-up across the UKBB. Our Cox proportional
hazard model included hazard ratios derived from the UKBB data.
There is a risk of over ﬁtting associations with sex and age at onset of
ON because of the known selection biases in the UKBB data
32, including
healthy volunteer bias. Our use of known risk factors from previous
epidemiology and genome-wide association studies reduces the risk of
a false result. However, we will in future test and calibrate our model
using prospective diagnostic and implementation studies before a
combined model can be integrated into clinical care. Additionally,
UKBB data did not permit the use of the most recent and more precise
HLA data
20 for HLA-GRS. Other general and important limitations of
the UKBB study have been outlined elsewhere33.
Classiﬁcation of ON could be enhanced by using segmented
optical coherence tomography (OCT) imaging data in the ON case
deﬁnition
1.S p e c iﬁcally, a 4%/4 μm inter-eye difference in the macula
ganglion cell inner plexiform layer could enhance case de ﬁnition,
indicating prior unilateral optic nerve damage, as part of new diag-
nostic criteria for ON
34,35. Unfortunately, OCT images are currently
available for less than one-ﬁfth of UKBB participants, and output from
automated retinal image segmentation is not yet available in the public
UKBB data repository to permit sensitivity analysis 36. We anticipate
that potential misclassiﬁcation bias resulting from noise in case de ﬁ-
nitions, with likely overdiagnosis of optic neuritis based on diagnostic
codes alone, would lead ourﬁndings to underestimate the value of MS-
GRS in MS risk stratiﬁcation, as compared to veriﬁcation of ON cases
with greater precision using OCT. Reassuringly, even though the UKBB
is not population-representative and recruited adults aged over 40
years, we found comparable ON and MS prevalence to population-
representative national studies
2,37.
Furthermore, while Epstein-Barr virus seropositivity was not
available in the UKBB dataset, we explored diagnostic codes for prior
clinical diagnosis of EBV infection or glandular fever, which have been
identiﬁed as causal predictors of MS risk, but these diagnoses are
scarcely available in UKBB
27. Furthermore, seropositivity for EBV (data-
ﬁeld 23005) was available for less than ten thousand individuals.
Finally, we would have liked to explore the additional contribution to
future MS risk prediction of the presence or absence of brain lesions
on unenhanced MRI imaging. However, this imaging was only per-
formed in a subset of UKBB participants, and not at the time of ON
diagnosis, and a variable relating to the presence or absence of
demyelinating lesions suggestive of MS was not available for analysis.
Rigorous quality control of phenotype data
Our study highlights that rigorous case de ﬁnition QC in population
biobanks is important and may reduce noise and increase power of
analyses like ours. We manually checked all the diagnostic codes in
each data source and performed a subgroup analysis which conﬁrmed
that similar results were found when cases were limited to those with a
‘stricter’deﬁnition of MS and ON diagnosis. We also identiﬁed that two
common Read3 codes for optic neuritis (F4H3 or F4H32) were omitted
from the central UKBB de ﬁnition of optic neuritis. This resulted in
capture of an additional 194 cases of ON in this study. We also
enhanced speciﬁcity for the diagnosis of ON by excluding a few codes
used in the UKBB central ON de ﬁnition, for example, ‘optic neuro-
pathy’, which has many causes (e.g., genetic, nutritional, toxic, com-
pressive) that are clinically distinct from ON. However, for 34
participants with undifferentiated ON who had only an ICD9 or ICD10
code, we were unable to further review which diagnostic codes made
up the UKBB ON case de ﬁnition.
Comparison to existing literature
Our study leverages retrospective and prospective healthcare data to
build on existing knowledge of the association between ON presenting
as a clinically isolated syndrome (CIS) and future MS risk. The 1992
Optic Neuritis Treatment trial, which recruited 389 adults with acute
unilateral, undifferentiated ON, reported a 5-year cumulative prob-
ability of MS of 29% rising to 38% at 10 years
7,a n d5 0 %b y1 5y e a r s ,w i t h
risk signiﬁcantly associated with the presence of 1 or more lesions on
baseline non-contrast-enhanced magnetic resonance imaging (MRI) of
the brain
4, and also with female sex in participants without baseline
MRI lesions (HR 3.6). This study found that the risk of developing MS
was highest in the ﬁrst 5 years following ON, and then decreased. A
United States Armed Forces cohort study, including 1427 adults with
ON, reported that 136 (9.5%) people developed MS by 10 years,
including 19% of women and 14% of men with ON, and 68% were
diagnosed within a year of ON
38.
In patients with undifferentiated ON, we found female sex to be a
signiﬁcant independent predictor of MS risk (aHR 2.20, P < 0.005,
Fig. 3a), an association well-established in the literature but not fully
understood, reﬂecting a complex interplay between genetic, epige-
netic, immunological, hormonal and environmental factors39,40. Binary
age at onset of ON (between 18 and 50 years) was also signi ﬁcantly
associated with MS risk (aHR 2.43,P < 0.005). We found a weak inverse
association between MS-GRS and age at MS onset (R 2 = 0.011,
P < 0.0001, Supplementary Fig. 10), aligning with a recent study by
Misicka et al. (2022) reporting higher MS-GRS risk burden and younger
age at MS diagnosis
41.W ed i dn o t ﬁnd signiﬁcant associations with
additional clinical risk factors including BMI, smoking, or vitamin D
insufﬁciency at UKBB study entry, which have been highlighted in
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 8

other studies22– 25,28,29.I ti sp o s s i b l et h a tt h i si sb e c a u s eo u rs t u d yo n l y
measures these variables at a single time point (UK Biobank study
entry) unrelated to diagnosis of ON and/or MS. Additionally, risk fac-
tors that are signiﬁcantly associated with disease in large observational
epidemiology studies sometimes do not explain enough variation in
disease development to be useful for clinical prediction.
Future research
Further research is needed to test the hypothesis that an MS-GRS
combined with existing diagnostic
6, demographic, and other deep
phenotypic variables, can usefully stratify patients with undiffer-
entiated ON into high/medium/low genetic MS risk in a prospective
diagnostic predictive clinical setting. Patient and public involvement
around the acceptability of integrating genetic risk stratiﬁcation into
frontline care will be vital. Our study hints at the possibility of clinical
translation, with use of a genetic test atﬁrst ON presentation to deliver
better acute clinical care. With up to 5 million adults in the UK soon to
be recruited into the UK ’s largest ever health research programme,
including genomic medicine, ‘Our Future Health’, use of GRSs could
soon become part of an enhanced approach to personalised
medicine
42.
In summary, our study unveils the potential of a composite model
that integrates MS-GRS with age at ON onset and sex, offering a means
to stratify patients based on their likelihood of a future MS diagnosis,
thus providing valuable insights for clinical management decisions.
Future research endeavours should delve into the practical application
of the MS-GRS model within clinical settings. We hypothesize that the
knowledge of high MS-GRS, especially in individuals with suspected
clinically isolated syndrome, would facilitate MS follow-up manage-
ment and guide decisions around performing lumbar puncture to seek
earlier MS diagnosis and potentially earlier disease-modifying treat-
ment to reduce relapse rate. Additionally, we posit that a swift MS-GRS
model panel test to identify low MS-GRS could facilitate hyperacute
corticosteroid treatment, especially of subsequent vision-threatening
ON relapses, potentially mitigating visual morbidity in those with non-
MS-ON, while also yielding substantial economic and quality-adjusted
life year beneﬁts.
Methods
Data source and population
We studied participant data in the UKBB, a longitudinal population-
based cohort study, described in detail elsewhere43.I nb r i e f ,t h eU K B B
comprises extensive genetic and phenotypic data from ~500,000
individuals (n = 229,134 men, n =2 7 3 , 4 0 2 w o m e n ) a g e d 4 0– 69 years.
Participants were recruited from 22 assessment centres in the UK
between 2006 and 2010, with data linkage to hospital episode statis-
tics (HES), the death register, and primary care data. UKBB participants
gave informed consent to participate, and ethics committee approval
was granted by the Northwest Multi-Centre Research Ethics Commit-
tee (ref 06/MRE08/65).
Identifying cases and controls
Our case identi ﬁcation process is detailed in Supplementary Meth-
ods 1.1 and Supplementary Fig. 1, with a summary in Fig. 1.W ed e ﬁne
the included diagnostic codes in Supplementary Tables 1 – 3a n d
excluded 24 cases who had Read codes indicating a diagnosis distinct
from ON, or to be insufﬁciently speciﬁc for ON diagnosis. We excluded
cases with MS diagnosis before the age of 15.0 years, but retained cases
with ON before the age of 15.0 years.
We deﬁned four groups: MS without ON, MS with ON, ON without
MS, and controls who had neither ON nor MS. All groups contained
both prevalent and incident cases. We analysed the order of diagnoses
using the earliest available date of diagnosis from all data sources
(Hospital Episode Statistics (HES), GP records, self-report). We limited
our MS-free survival analysis to undifferentiated ON cases, after
excluding those with MS diagnosis preceding ON diagnosis, and
compared those who were subsequently diagnosed with MS to those
who were not.
Genetic data
We used imputed genetic data downloaded from the UK Biobank44.W e
limited our analysis to 11,977,111 genetic variants imputed using the
Haplotype Reference Consortium imputation reference panel with a
minimum minor allele frequency (MAF) > 0.1% and imputation quality
score (INFO) > 0.3. We used eight HLA alleles imputed to four-digit
resolution centrally by UKBB using HLA*IMP:02
45.
The primary analysis was based on unrelated individuals of all
ancestries. We excluded one of each pair of related individuals at
random based on the genetic relatedness coef ﬁcient (>=0.084) to
exclude third-degree relatives or closer, and to reduce the risk of bias
from cryptic relatedness ( n =3 4 0 0 i n t o t a l ,n =2 1 w i t h M S a n dn =4
with ON)
46. We performed a secondary analysis of individuals identi-
ﬁed as European ancestry British by principle component analysis
(Data-Field 22006), and then separately those of non-white-European
ancestry.
Generating the MS genetic risk score (MS-GRS)
We used external sources of risk alleles and odds ratios for non-HLA
and HLA alleles (Supplementary Methods 1.2). Speciﬁcally, we gener-
ated a non-HLA genetic risk score using 317 autosomal single nucleo-
tide polymorphisms (SNPs) with a genome-wide signi ﬁcance of P
value < 10
−5, including 200 SNPs with genome-wide signi ﬁcance
P <5×1 0 −8 and a further 117 strongly suggestive SNPs with genome-
wide signi ﬁcance between P <1 0−5 and P >5×1 0 −8 20. All SNPs were
outside the extended HLA region (i.e. excluding the chromosome 6
region from 24 to 35 Mbps, hg19). We ensured that no SNPs were in
linkage disequilibrium (r
2 > 0.2) using LDlink ( n =8 )47, and excluded
ambiguous ( n = 1), missing ( n = 1), or duplicated ( n =1 ) v a r i a n t s ,
resulting in 307 SNPs (Supplementary Data 1). We calculated a log-
additive sum of the risk alleles in PLINK2, using a natural log of odds
ratios (log OR) as weights.
Recent work has revealed that accounting for HLA interaction
improves the discriminative performance of autoimmune disease
GRS
48,49. A recent GWAS by IMSGC described HLA and nearby non-HLA
genes in-detail, including independent effects within some loci 20.
However, we used a 10-allele HLA interaction model developed by
Moutsianas et al. (2015) on 17,456 MS cases and 30,385 controls from
across 11 cohorts to account for non-additive interaction between the
HLA alleles derived externally from UKBB
50.T h i si n c l u d e d8i m p u t e d
HLA alleles and 2 SNPs from the HLA region (29.9 to 33.6 Mbps on chr6
hg19). We captured interactions between the alleles by calculating the
interactive model; scoring imputed HLA alleles while employing both
additive effects, homozygote correction terms, and conditional scor-
ing of some HLA alleles (Supplementary Table 4). We performed this
scoring using the Python 3 libraries Pandas and NumPy
51,52.W et h e n
scored the two SNPs from the HLA region by multiplying the natural
log odds ratios (OR) by risk allele dosage using PLINK2. Lastly, we
combined the scores calculated from HLA alleles and the two SNPs to
produce the HLA-GRS. The ﬁnal MS-GRS was a sum of non-HLA- and
HLA-GRS.
Statistical analysis
We analysed the distribution of MS-GRS in the four groups: healthy
controls, MS only cases, ON only cases, and cases with both MS and
ON, using Welch ’s t-test. We tested the ability of MS-GRS to dis-
criminate between MS cases and healthy controls using the area under
the curve (AUC) of the receiver operating characteristic (ROC). We
compared the discriminative power of covariates only, MS-GRS only,
and MS-GRS plus covariates. To avoid overﬁtting, we calculated each
ROC-AUC using three-fold cross-validation with ten repetitions,
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 9

reporting means with 95% con ﬁdence intervals. Covariates selected
from the published literature included sex, age at UKBB entry, Town-
send deprivation index (TDI) and the ﬁrst four genetic principal
components, as they were previously scrutinised in the context of an
MS genetic risk score
53.
Finally, to assess the ability of MS-GRS to predict MS-free sur-
vival time in cases presenting with undifferentiated ON (i.e., without
prior MS diagnosis), we explored Cox proportional hazards survival
regression, by multiple potential predictor variables speci ﬁed a
priori from literature review. Here, we tested potential predictor
variables more extensively, including those putatively associated
with MS. Binary variables included sex, age group (18 – 50 years
versus younger and older), and ethnicity (European ancestry British
versus not/unknown, Data-Field 22006)
22. Continuous variables
included age, MS-GRS (standardised for 545 individuals with
undifferentiated ON), and Body Mass Index (kg/m 2, UK Biobank
Data-Field 21001) 22,24– 26. Categorical variables included smoking
status (ever vs never vs missing, Data-Field 20160) 28,29,54, country of
birth (England, Scotland, Northern Ireland, Republic of Ireland,
Wales and Other/Unknown, Data-Field 1647), Townsend deprivation
index quintiles (1 to 5 or missing, Data-Field 189), and serum 25-OH
vitamin D level at UKBB baseline assessment (suf ﬁcient [>50 nmol/
L], insuf ﬁcient [25 – 50 nmol/L], de ﬁcient [<25 nmol/L] or missing,
Data-Fields 30890 – 30896)
22– 24. We assumed the age of diagnosis
was the earliest record of diagnosis across all sources. For the
outcome variable, we estimated the time from diagnosis of ON to
diagnosis of MS using the earliest records of diagnoses available for
both diseases. Censoring was estimated using the latest HES or GP
episode record available for each individual, and where it was
deemed unsuitable or was not available (e.g., last record preceded
enrolment date, or neither HES nor GP records were available for an
individual ( n = 26 people with non-MS-ON) we used the last date of
global HES update. Variables reaching statistical signi ﬁcance
P < 0.05 in the single variable analysis were included in the full
multivariable regression model and were removed through back-
ward elimination to identify the most parsimonious model with the
lowest partial AIC (Akaike information criterion). We considered the
interaction term between sex and age at ON diagnosis.
We explored the impact of genetic stratiﬁcation on our results in
all UKBB participants by performing an analysis of the European
ancestry population only, as deﬁned by UKBB self-reported ethnicity
and genetic principal components (Data-Field 22006) (Supplementary
Results Section 3). While anticipating the analysis to be underpowered,
we also performed a sensitivity analysis comparing non-European and
European ancestry British participants. Two additional subgroup ana-
lyses included one on ‘strict’diagnoses from either GP records or HES
only, and one excluding cases diagnosed before 20 years of age
(Supplementary Table 12).
Statistical analyses and visualisations were performed using
Python 3 and NumPy
52, Scikit-learn 55, Matplotlib 56 and Lifelines
libraries57. All codes for the completed analyses are available athttps://
github.com/ploginovic/MS-ON-ukb-code.
External validation
We sought to validate our ﬁndings in two large genetic and health
datasets, Geisinger, USA 58,59 and FinnGen, Finland 60,61.W ea s s e s s e d
discrimination and calibration of the UKBB combined model in these
datasets. See Supplementary Methods and Results (Sections 1.3 – 2.1)
for additional detail.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
The Genetic risk score will be deposited in the Polygenic Score Catalog
(PGS Catalog: https://www.pgscatalog.org/)u p o nr e c e i v i n gaD O Io f
this study. Individual-level genotype data described in this study are
available to bona ﬁde researchers as per the UK Biobank data-access
protocol ( https://www.ukbiobank.ac.uk/enable-your-research/apply-
for-access). Further details and instructions about registration for
access to the data are available at http://www.ukbiobank.ac.uk/
register-apply/. UK Biobank accession codes of this study were 9055
and 9072. For FinnGen data, access to individual-level sensitive health
data must be approved by national authorities for speci ﬁcr e s e a r c h
projects and for speci ﬁcally listed and approved researchers in
accordance with the National and European regulations (GDPR).
Researchers can apply for the health register data from the Finnish
Data Authority Findata ( https://ﬁndata.ﬁ/en/permits/)a n df o r
individual-level genotype data from Finnish biobanks via the Finge-
nious portal (https://site.ﬁngenious.ﬁ/en/)h o s t e db yt h eF i n n i s hB i o -
bank Cooperative FINBB (https://ﬁnbb.ﬁ/en/). For Geisinger, the data
was generated as described in Carey et al.
58. Further details regarding
phenotype and genotyping data for Geisinger can be found here:
https://www.geisinger.org/precision-health/mycode/discovehr-
project. Institutional Review Board determined this study to be“Non-
human subject research” using de-identiﬁed information (IRB #: 2023-
1075). The HLA genotyping data and MS-GRS from the MyCode par-
ticipants in this study may be shared with a third party bona ﬁde
researchers upon execution of the data-sharing agreement.
Code availability
The code used for phenotype, genotype, and statistical analysis is
available through the following GitHub repository:https://github.com/
ploginovic/MS-ON-ukb-code. Statistical analyses were performed in
Python v3.10 ( https://docs.python.org/release/3.10.11/), with adapta-
tions the LifeLines Python package, covered by the MIT license
(https://github.com/CamDavidsonPilon/lifelines). Genetic analyses
were performed in PLINK v1.9 (https://www.cog-genomics.org/plink/)
and PLINK v2.0.a ( https://www.cog-genomics.org/plink/2.0/). Pheno-
type analyses were performed in STATA v17 ( https://www.stata.com)
and R v3.6 (https://www.r-project.org).
References
1. Petzold, A. et al. Diagnosis and classi ﬁcation of optic neuritis.Lancet
Neurol. 21, 1120–1134 (2022).
2. Braithwaite, T. et al. Trends in optic neuritis incidence and pre-
valence in the UK and association with systemic and neurologic
disease. JAMA Neurol. 77,1 5 1 4–1523 (2020).
3. Rodriguez, M., Siva, A., Cross, S. A., O ’Brien, P. C. & Kurland, L. T.
Optic neuritis: a population-based study in Olmsted County, Min-
nesota. Neurology 45,2 4 4–250 (1995).
4. Optic Neuritis Study. G. Multiple sclerosis risk after optic neuritis:
ﬁnal optic neuritis treatment trial follow-up.Arch. Neurol. 65,
727–732 (2008).
5. Beck, R. W. et al. Visual function more than 10 years after optic
neuritis: experience of the optic neuritis treatment trial.Am. J.
Ophthalmol.137,7 7–83 (2004).
6. Thompson, A. J. et al. Diagnosis of multiple sclerosis: 2017 revisions
of the McDonald criteria. Lancet Neurol. 17,1 6 2–173 (2018).
7 . B e c k ,R .W .e ta l .H i g h -a n dl o w - r i s kp r oﬁles for the development of
multiple sclerosis within 10 years after optic neuritis: experience of
the optic neuritis treatment trial.Arch. Ophthalmol.121,
944–949 (2003).
8. Optic Neuritis Study Group. Visual function 5 years after optic
neuritis: experience of the Optic Neuritis Treatment Trial.Arch.
Ophthalmol.115,1 5 4 5–1552 (1997).
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 10

9. Wakakura, M. et al. Multicenter clinical trial for evaluating methyl-
prednisolone pulse treatment of idiopathic optic neuritis in Japan.
Optic Neuritis Treatment Trial Multicenter Cooperative Research
Group (ONMRG). Jpn J. Ophthalmol. 43,1 3 3–138 (1999).
10. Wakakura, M. et al. Baseline features of idiopathic optic neuritis as
determined by a multicenter treatment trial in Japan. Optic Neuritis
Treatment Trial Multicenter Cooperative Research Group (ONMRG).
Jpn J. Ophthalmol. 43,1 2 7–132 (1999).
11. Petzold, A. et al. Case for a new corticosteroid treatment trial in
optic neuritis: review of updated evidence.J. Neurol. Neurosurg.
Psychiatry91,9 –14 (2020).
12. Petzold, A. et al. The investigation of acute optic neuritis: a review
and proposed protocol.Nat. Rev. Neurol. 10, 447–458 (2014).
13. Braithwaite, T., Wiegerinck, N., Petzold, A. & Denniston, A. Vision
loss from atypical optic neuritis: patient and physician perspectives.
Ophthalmol. Ther.9,2 1 5–220 (2020).
14. Osinga, E., van Oosten, B., de Vries-Knoppert, W. & Petzold, A. Time
is vision in recurrent optic neuritis.Brain Res. 1673,9 5–101
(2017).
15. Chan, K. L. & Mok, C. C. Glucocorticoid-induced avascular bone
necrosis: diagnosis and management.Open Orthop. J. 6,
449–457 (2012).
16. Kuhlmann, T. et al. Multiple scl erosis progression: time for a new
mechanism-driven framework.Lancet Neurol. 22,7 8–88 (2023).
1 7 . L e b r u n - F r e n a y ,C .e ta l .T e r iﬂunomide and time to clinical multiple
sclerosis in patients with radiologically isolated syndrome: the
TERIS randomized clinical trial.JAMA Neurol. 80,
1080–1088 (2023).
18. International Multiple Sclerosis Genetics Consortium. Electronic
address, c.c.y.e. & International Multiple Sclerosis Genetics, C.
Low-frequency and rare-coding variation contributes to multiple
sclerosis risk. Cell 175,1 6 7 9–1687.e1677 (2018).
19. International Multiple Sclerosis Genetics, C. Risk alleles for multiple
sclerosis identiﬁed by a genomewide study. N .E n g l .J .M e d357,
851–862 (2007).
20. International Multiple Sclerosis Genetics, C. Multiple sclerosis
genomic map implicates peripheral immune cells and microglia in
susceptibility.Science 365, eaav7188 (2019).
21. Scalfari, A. et al. The relationshi p of age with the clinical phenotype
in multiple sclerosis.Mult. Scler. 22,1 7 5 0–1758 (2016).
22. Gianfrancesco, M. A. et al. Evidence for a causal relationship
between low vitamin D, high BMI, and pediatric-onset MS.Neurol-
ogy 88,1 6 2 3–1629 (2017).
23. Rhead, B. et al. Mendelian randomization shows a causal effect of
low vitamin D on multiple sclerosis risk. Neurol. Genet. 2,e 9 7
(2016).
24. Jacobs, B. M., Noyce, A. J., Giovannoni, G. & Dobson, R. BMI and low
vitamin D are causal factors for multiple sclerosis: a Mendelian
Randomization study.Neurol. Neuroimmunol. Neuroinﬂamm 7,
e662 (2020).
2 5 . G i a n f r a n c e s c o ,M .A .e ta l .C a u sal effect of genetic variants asso-
ciated with body mass index on multiple sclerosis susceptibility.
Am. J. Epidemiol. 185,1 6 2–171 (2017).
2 6 . M o k r y ,L .E .e ta l .O b e s i t ya n dmultiple sclerosis: a Mendelian
Randomization study.PLoS Med. 13, e1002053 (2016).
27. Bjornevik, K. et al. Longitudinal analysis reveals high prevalence of
Epstein-Barr virus associated with multiple sclerosis.Science 375,
296–301 (2022).
28. Hedstrom, A. K. et al. The interaction between smoking and HLA
genes in multiple sclerosis: replication and reﬁnement. Eur. J. Epi-
demiol. 32,9 0 9–919 (2017).
29. Kleerekooper, I. et al. Associations of alcohol consumption and
smoking with disease risk and neurodegeneration in individuals
with multiple sclerosis in the United Kingdom.JAMA Netw. Open5,
e220902 (2022).
30. De Jager, P. L. et al. Integration of genetic risk factors into a clinical
algorithm for multiple sclerosis susceptibility: a weighted genetic
risk score. Lancet Neurol. 8, 1111–1119 (2009).
31. Breedon, J. R. et al. Polygenic risk score prediction of multiple
sclerosis in individuals of South Asian ancestry.Brain Commun. 5,
fcad041 (2023).
32. Swanson, J. M. The UK Biobank and selection bias. Lancet 380,
110 (2012).
3 3 . M u n a f o ,M .R . ,T i l l i n g ,K . ,T a y l o r ,A .E . ,E v a n s ,D .M .&D a v e yS m i t h ,G .
Collider scope: when selection bias can substantially inﬂuence
observed associations.Int J. Epidemiol. 47, 226–235 (2018).
34. Bsteh, G. et al. Diagnostic performance of adding the optic nerve
region assessed by optical coherence tomography to the diag-
nostic criteria for multiple sclerosis.Neurology 101,
e784
–e793 (2023).
35. Petzold, A. et al. Retinal asymmetry in multiple sclerosis. Brain 144,
224–235 (2021).
36. Keane, P. A. et al. Optical coherence tomography in the UK Biobank
study— rapid automated analysis of retinal thickness for large
population-based studies.PLoS ONE 11, e0164095 (2016).
37. Mackenzie, I. S., Morant, S. V., Bloomﬁe l d ,G .A . ,M a c D o n a l d ,T .M .&
O’Riordan, J. Incidence and prevalence of multiple sclerosis in the
UK 1990-2010: a descriptive study in the General Practice Research
Database. J. Neurol. Neurosurg. Psychiatry85,7 6–84 (2014).
38. Gu, W. et al. Incidence of optic neuritis and the associated risk of
multiple sclerosis for service members of U.S. Armed Forces.Mil.
Med. 188,e 6 9 7–e702 (2023).
39. Ysrraelit, M. C. & Correale, J. Impact of sex hormones on immune
function and multiple sclerosis development.Immunology156,
9–22 (2019).
40. Lef ﬂer, J., Trend, S., Gorman, S. & Hart, P. H. Sex-speciﬁc environ-
mental impacts on initiation and progression of multiple sclerosis.
Front Neurol. 13, 835162 (2022).
41. Misicka, E. et al. A higher burden of multiple sclerosis genetic risk
confers an earlier onset. Mult. Scler. 28, 1189–1197 (2022).
42. Our Future Health Research Programme. https://ourfuturehealth.
org.uk/ (2023).
43. Sudlow, C. et al. UK biobank: an open access resource for identi-
fying the causes of a wide range of complex diseases of middle and
old age. PLoS Med. 12, e1001779 (2015).
44. Bycroft, C. et al. The UK Biobank resource with deep phenotyping
and genomic data. Nature 562,2 0 3–209 (2018).
45. Dilthey, A. et al. Multi-population classical HLA type imputation.
PLoS Comput. Biol. 9, e1002877 (2013).
46. Green, H. D. et al. Applying a genetic risk score for prostate cancer
to men with lower urinary tract symptoms in primary care to predict
prostate cancer diagnosis: a cohort study in the UK Biobank.Br. J.
Cancer 127,1 5 3 4–1539 (2022).
47. Machiela, M. J. & Chanock, S. J. LDlink: a web-based application for
exploring population-speciﬁc haplotype structure and linking cor-
related alleles of possible functional variants.Bioinformatics31,
3555–3557 (2015).
48. Sharp, S. A. et al. A single nucleotide polymorphism genetic risk
score to aid diagnosis of coeliac disease: a pilot study in clinical
care. Aliment Pharm. Ther. 52, 1165–1173 (2020).
4 9 . S h a r p ,S .A .e ta l .D e v e l o p m e n tand standardization of an improved
type 1 diabetes genetic risk score for use in newborn screening and
incident diagnosis.Diabetes Care 42,2 0 0–207 (2019).
50. Moutsianas, L. et al. Class II HLA interactions modulate genetic risk
for multiple sclerosis.Nat. Genet. 47, 1107–1113 (2015).
51. McKinney, W. A. O. Data structures for statistical computing in
Python. InProceedings of the 9th Python in Science Conference,V o l .
445, 51–56 (2010).
52. Harris, C. R. et al. Array programming with NumPy. Nature 585,
357–362 (2020).
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 11

53. Jacobs, B. M. et al. Gene-envi ronment interactions in multiple
sclerosis: a UK Biobank study. Neurol. Neuroimmunol. Neuroin-
ﬂamm 8, e1007 (2021).
54. Vandebergh, M. & Goris, A. Smoki ng and multiple sclerosis risk: a
Mendelian randomization study.J. Neurol. 267,3 0 8 3–3091
(2020).
55. Pedregosa, F. et al. Scikit-learn: machine learning in Python. J.
Mach. Learn. Res. 12, 2825–2830 (2011).
56. Hunter, J. D. Matplotlib: a 2D graphics environment. Comput. Sci.
Eng. 9,9 0–95 (2007).
57. Davidson-Pilon, C. Lifelines: survival analysis in Python. J. Open
Source Softw. 4,1 3 1 7( 2 0 1 9 ) .
58. Carey, D. J. et al. The Geisinger MyCode community health initia-
tive: an electronic health record-linked biobank for precision
medicine research.Genet Med. 18,9 0 6–913 (2016).
59. Dewey, F. E. et al. Distribution and clinical impact of functional
variants in 50,726 whole-exome sequences from the DiscovEHR
study. Science 354, aaf6814 (2016).
60. FinnGen, I.f.M.M.F.F., University of Helsinki. FinnGen Research
Project. Vol. 2023 (2023).
61. Kurki, M. I. et al. FinnGen provides genetic insights from a well-
phenotyped isolated population.Nature 613,5 0 8–518
(2023).
Acknowledgements
T.B. was supported by the Royal College of Ophthalmologists and Fight
for Sight Zakarian Award 2022 (RCOZAK2022). P.L. was supported by the
INSPIRE Studentship by the University of Exeter. RAO had a UK MRC
conﬁdence in concept award to develop a type 1 diabetes GRS biochip
with Randox R&D and has ongoing research funding from Randox; and
has research funding from a Diabetes UK Harry Keen Fellowship (16/
0005529), National Institute of Diabetes and Digestive and Kidney Dis-
e a s e sg r a n t s( N I HR 0 1D K 1 2 1 8 4 3–01 and U01DK127382–01), JDRF (3-SRA-
2019–827-S-B, 2-SRA-2022–1261-S-B, 2-SRA-2002–1259-S-B, 3-SRA-
2022–1241-S-B, and 2-SRA-2022–1258-M-B), and The Larry M and Leona B
Helmsley Charitable Trust. This study was supported by the National
Institute for Health and Care Research Exeter Biomedical Research
Centre. The views expressed are those of the author(s) and not neces-
sarily those of the NIHR or the Department of Health and Social
Care. This research has been conducted using data from UK Biobank
(https://www.ukbiobank.ac.uk/), a major biomedical database, and the
authors are grateful to the participants. The authors are grateful to the
participants of the Geisinger MyCode Community Health Initiative for
the use of their genomic and electronic health information, without
whom this study would not be possible. The patient enrolment and
exome sequencing for the DiscovEHR study were funded by the
Regeneron Genetics Center. We would like to acknowledge the
Geisinger-Regeneron DiscovEHR Collaboration for making the genotype
data and phenotype available for this project. We want to acknowledge
the participants and investigators of FinnGen study. The FinnGen project
is funded by two grants from Business Finland (HUS 4685/31/2016 and
UH 4386/31/2016) and the following industry partners: AbbVie Inc.,
AstraZeneca UK Ltd, Biogen MA Inc., Bristol Myers Squibb (and Celgene
Corporation & Celgene International II Sàrl), Genentech Inc., Merck
Sharp & Dohme LCC, Pﬁzer Inc., GlaxoSmithKline Intellectual Property
Development Ltd., Sanoﬁ US Services Inc., Maze Therapeutics Inc.,
Janssen Biotech Inc, Novartis AG, and Boehringer Ingelheim Interna-
tional GmbH. The following biobanks are acknowledged for delivering
biobank samples to FinnGen: Auria Biobank (www.auria.ﬁ/biopankki),
THL Biobank (www.thl.ﬁ/biobank), Helsinki Biobank (www.
helsinginbiopankki.ﬁ), Biobank Borealis of Northern Finland (https://
www.ppshp.ﬁ/Tutkimus-ja-opetus/Biopankki/Pages/Biobank-Borealis-
brieﬂy-in-English.aspx), Finnish Clinical Biobank Tampere (www.tays.ﬁ/
en-US/Research_and_development/Finnish_Clinical_Biobank_Tampere),
Biobank of Eastern Finland (www.ita-suomenbiopankki.ﬁ/en), Central
Finland Biobank (www.ksshp.ﬁ/ﬁ-FI/Potilaalle/Biopankki), Finnish Red
Cross Blood Service Biobank (www.veripalvelu.ﬁ/verenluovutus/
biopankkitoiminta), Terveystalo Biobank (www.terveystalo.com/ﬁ/
Yritystietoa/Terveystalo-Biopankki/Biopankki/)a n dA r c t i cB i o b a n k
(https://www.oulu.ﬁ/en/university/faculties-and-units/faculty-
medicine/northern-ﬁ
nland-birth-cohorts-and-arctic-biobank). All Fin-
nish Biobanks are members of BBMRI.ﬁ infrastructure (www.bbmri.ﬁ).
Finnish Biobank Cooperative -FINBB (https://ﬁnbb.ﬁ/) is the coordinator
of BBMRI-ERIC operations in Finland. The Finnish biobank data can be
accessed through the Fingenious® services (https://site.ﬁngenious.ﬁ/
en/) managed by FINBB.
Author contributions
Conceptualization: R.A.O., T.B., L.F. and P.L. Genetic analysis: P.L., F.W.,
J.L., L.F., M.N.W., H.S.R. and R.A.O. Phenotype preparation, harmoniza-
tion, and analysis: P.L., F.W., J.L., T.B., L.F., M.N.W., J.T., H.D.G., U.L.M.,
H.S.R., D.J.C. and R.A.O. Statistical analysis and modelling: P.L., F.W.,
J.L., L.F., T.B., R.A.O., H.D.G., M.N.W. and U.L.M. Project administration:
R.A.O., T.B., M.N.W., T.T., A. G. and D.J.C. Supervision: T.B., R.A.O., T.T.,
D.J.C. and A.G. Writing— original draft: T.B., R.A.O., P.L, L.F., A.P., M.N.W.
and J.T. Data curation: M.N.W., U.L.M., D.J.C., T.T. and A.G. All authors
contributed to data interpretation, manuscript revisions, and approval of
the ﬁnal version of the manuscript.
Competing interests
R.A.O. is a co-investigator on a Randox Laboratories R&D research grant
and received translational industry academic funding from Randox
Laboratories R&D relating to autoimmune GRS for prediction and clas-
siﬁcation of disease. There are no established patents, loyalties, or
licensing agreements relating to this grant. It is a 3-year grant (February
2022–2025). The approximate value is a £2.2 million program grant on
GRS across autoimmune disease. A.P. reports personal fees from
Novartis, Heidelberg Engineering, Zeiss, grants from Novartis, outside
the submitted work; and is part of the steering committee of the OCTiMS
study which is sponsored by Novartis and the Angio-OCT steering
committee which is sponsored by Zeiss. He does not receive compen-
sation for these activities. Other authors have no competing interests to
declare.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-024-44917-9.
Correspondenceand requests for materials should be addressed to
Richard A. Oram.
Peer review informationNature Communicationsthanks Farren Briggs
and the other, anonymous, reviewer(s)for their contribution to the peer
review of this work. A peer review ﬁle is available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 12

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons license, and indicate if
changes were made. The images or other third party material in this
article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons license and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this license, visithttp://creativecommons.org/
licenses/by/4.0/.
© The Author(s) 2024
1University of Exeter Medical School, College of Medicine and Health, University of Exeter, Heavitree Road, Exeter EX1 2HZ, UK. 2Institute for Molecular
Medicine Finland (FIMM), HiLIFE, University of Helsinki, Helsinki, Finland. 3Weis Center for Research, Geisinger, Danville, PA, USA. 4Institute of Biomedical
and Clinical Science, University of Exeter Medical School, St Luke ’s Campus, University of Exeter, Heavitree Road, Exeter, Devon EX1 2LU, UK. 5Neuro-
ophthalmology Expert Center, Amsterdam UMC, Amsterdam, The Netherlands. 6Department of Neuro-ophthalmology, The National Hospital for Neu-
rology and Neurosurgery, Queen Square, UCL Institute of Neurology, London, UK. 7Neuro-ophthalmology service, Moorﬁelds Eye Hospital, London, UK.
8Genetics of Complex Traits, University of Exeter Medical School, University of Exeter, Exeter EX2 5DW, UK. 9Exeter Centre of Excellence for Diabetes
Research (EXCEED), University of Exeter Medical School, St Luke’s Campus, University of Exeter, Heavitree Road, Exeter, Devon EX1 2LU, UK.10Analytic and
Translational Genetics Unit, Department of Medicine, Massachusetts General Hospital, Boston, MA, USA.11Abdominal Center, Endocrinology, University of
Helsinki and Helsinki University Hospital, Helsinki, Finland. 12Folkhälsan Institute of Genetics, Folkhälsan Research Center, Biomedicum, Helsinki, Finland.
13Lund University Diabetes Centre, Department of Clinical Sciences, Lund University, Malmö, Sweden. 14Academic Kidney Unit, Royal Devon University
Healthcare NHS Foundation Trust, Exeter, UK. 15King’s College London, School of Immunology & Microbial Sciences and School of Life Course and
Population Sciences, London, UK. 16Medical Eye Unit, St Thomas ’Hospital, Guy’s and St Thomas ’NHS Foundation Trust, Westminster Bridge Road,
London, UK. 17These authors contributed equally: Pavel Loginovic, Feiyi Wang, Jiang Li. 18These authors jointly supervised this work: Richard A. Oram,
Tasanee Braithwaite. e-mail: R.Oram@exeter.ac.uk
UKBB Eye & Vision Consortium
Tasanee Braithwaite 15,16,18,R i c h a r dA .O r a m4,14,18 ,A x e lP e t z o l d5,6,7 & Michael N. Weedon4
FinnGen
Tiinamaija Tuomi 2,11,12,13 & Andrea Ganna2,10
Geisinger-Regeneron DiscovEHR Collaboration
David J. Carey3
Article https://doi.org/10.1038/s41467-024-44917-9
Nature Communications|         (2024) 15:1415 13