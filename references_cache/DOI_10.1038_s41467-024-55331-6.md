---
reference_id: DOI:10.1038/s41467-024-55331-6
title: AI allows pre-screening of FGFR3 mutational status using routine histology slides of muscle-invasive bladder cancer
authors:
- Pierre-Antoine Bannier
- Charlie Saillard
- Philipp Mann
- Maxime Touzot
- Charles Maussion
- Christian Matek
- Niklas Klümper
- Johannes Breyer
- Ralph Wirtz
- Danijel Sikic
- Bernd Schmitz-Dräger
- Bernd Wullich
- Arndt Hartmann
- Sebastian Försch
- Markus Eckstein
journal: Nature Communications
year: '2024'
doi: 10.1038/s41467-024-55331-6
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-024-55331-6.pdf"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1038_s41467-024-55331-6.pdf
---

# AI allows pre-screening of FGFR3 mutational status using routine histology slides of muscle-invasive bladder cancer
**Authors:** Pierre-Antoine Bannier, Charlie Saillard, Philipp Mann, Maxime Touzot, Charles Maussion, Christian Matek, Niklas Klümper, Johannes Breyer, Ralph Wirtz, Danijel Sikic, Bernd Schmitz-Dräger, Bernd Wullich, Arndt Hartmann, Sebastian Försch, Markus Eckstein
**Journal:** Nature Communications (2024)
**DOI:** [10.1038/s41467-024-55331-6](https://doi.org/10.1038/s41467-024-55331-6)

## Content

Article https://doi.org/10.1038/s41467-024-55331-6
AI allows pre-screening of FGFR3 mutational
status using routine histology slides of
muscle-invasive bladder cancer
Pierre-Antoine Bannier 1 ,C h a r l i eS a i l l a r d1, Philipp Mann 1,
Maxime Touzot1, Charles Maussion1,C h r i s t i a nM a t e k2,3,4, Niklas Klümper5,6,7,
Johannes Breyer8,R a l p hW i r t z9, Danijel Sikic3,4,10, Bernd Schmitz-Dräger11,
Bernd Wullich3,4,10, Arndt Hartmann2,3,4, Sebastian Försch 12 &
Markus Eckstein 2,3,4
Pathogenic activating mutations in theﬁbroblast growth factor receptor 3
(FGFR3) drive disease maintenance and progression in urothelial cancer.
10–15% of muscle-invasive and metastatic urothelial cancer (MIBC/mUC) are
FGFR3-mutant. Selective targeting ofFGFR3 hotspot mutations with tyrosine
kinase inhibitors (e.g., erdaﬁtinib) is approved for mUC and requires FGFR3
mutational testing. However, current testing assays (polymerase chain reac-
tion or next-generation sequencing) necessitate high tissue quality, have long
turnover time, and are expensive. To overcome these limitations, we develop a
deep-learning model that detectsFGFR3 mutations using routine hematoxylin-
eosin slides. Encompassing 1222 cases, our study is a large-scale validation of a
model prescreeningFGFR3 mutations for MIBC and mUC patients. In this work,
we demonstrate that our model achieves high sensitivity (>93%) on advanced
and metastatic cases while reducing molecular testing by 40% on average,
thereby offering a cost-effective and rapid pre-screening tool for identifying
patients eligible for FGFR3 targeted therapies.
Urothelial carcinoma (UC), mainly localized in the bladder, is a common
malignancy in women and is the fourth most common malignancy in
men1. At diagnosis, over 75% of patien ts show a non-muscle-invasive
bladder cancer (NMIBC) that can be successfully managed with local
bladder preserving surgical treatment, instillation therapy in selected
risk groups, and surveillance. The remaining 25% of patients exhibit a
muscle-invasive disease (MIBC), which usually requires aggressive
treatment (cystectomy, radiotherapy, or palliative treatment). Despite
progress in understanding the disease and therapeutic strategies, sur-
vival rates of locally advanced and metastatic bladder cancer are still
poor
2. However, very recent major therapeutic improvements such as
enfortumab vedotin plus pembrolizumab for the treatment of metastatic
urothelial carcinoma raise the hope that the outcome rates of urothelial
carcinoma patients can be signiﬁcantly improved in the near future
3.
One of the central biological pathways driving NMIBC involves the
ﬁbroblast growth factor receptor 3 ( FGFR3). FGFR3 encodes a cell
Received: 17 April 2024
Accepted: 9 December 2024
Check for updates
1Owkin, Paris, France. 2Institute of Pathology, Universitätsklinikum Erlangen, Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, Germany.
3Comprehensive Cancer Center Erlangen-EMN (CCC ER-EMN) and Comprehensive Cancer Center Alliance WERA (CCC WERA), Erlangen, Germany.4Bavarian
Cancer Research Center (BZKF), Erlangen, Germany.5Department of Urology and Pediatric Urology, University Hospital Bonn, Bonn, Germany.6Institute of
Experimental Oncology, University Medical Center Bonn (UKB), Bonn, Germany.7Center for Integrated Oncology Aachen/Bonn/Cologne/Düsseldorf (CIO-
ABCD), Bonn, Germany.8Department of Urology, St. Caritas Hospital Regensburg, University of Regensburg, Regensburg, Germany.9STRATIFYER Molecular
Pathology, Cologne, Germany.10Department of Urology and Pediatric Urology, Universitätsklinikum Erlangen, Friedrich-Alexander-Universität Erlangen-
Nürnberg, Erlangen, Germany.11Urologie 24, St. Theresienkrankenhaus, Nürnberg, Germany.12Institute of Pathology, University Medical Center Mainz,
Johannes Gutenberg-Universität Mainz, Mainz, Germany. e-mail: pierre-antoine.bannier@owkin.com; markus.eckstein@uk-erlangen.de
Nature Communications|        (2024) 15:10914 1
1234567890():,;
1234567890():,;

surface receptor that plays a pivotal role in cell proliferation, differ-
entiation, and survival. Pathogenic activating mutations, fusions, and
ampliﬁcations of the FGFR3 gene (fusions are rare) have been exten-
sively linked to the development and maintenance of NMIBC, where
alteration frequencies range between up to 50% (in stroma-invasive
pT1 carcinomas) and up to 80% in non-invasive papillary low-grade
urothelial carcinoma, while FGFR3 alterations are less observed in
advanced stage MIBC (non-metastatic and metastatic) or urothelial
carcinoma in situ (alteration frequency ranging from 0 to up to 15%;
average distribution in nmMIBC and mMIBC around 10 to 15%)
4–7.T h e
differences in mutation frequencies can be explained by the fact that
bladder cancer is a highly heterogeneous disease on molecular and
pathological levels
8. While papillary non-invasive UC and a relevant
subset of stroma-invasive UC mainly arise via a hyperplasia sequence
driven by activatingFGFR3 alterations (particularly mutations, but also
ampliﬁcations and activating gene fusions), the majority of muscle-
invasive and relevant subset of aggressive stroma-invasive metastatic
UCs arise via the ﬂat carcinoma in situ sequence that is mainly driven
by chromosomal aberrations and inactivating TP53 mutations
8.T h i s
explains the low frequency of FGFR3 alterations in MIBC and mUC,
where FGFR3 mutant tumors can often be backtracked to long-lasting
high-grade non-invasive or stroma-invasive carcinomas progressing to
muscle-invasive and subsequently metastatic disease
8. This illustrates
that bladder cancer is a heterogeneous disease, where selective tar-
geting of tumor-driving FGFR3 alterations— mainly activating hotspot
mutations and gene fusions - repres ents an attractive therapeutic
strategy.
Based on these observations, several pharmaceutical companies
developed more or less speci ﬁc FGFR-inhibiting small molecules,
where erdaﬁtinib is the only FDA and EMA approved for the treatment
of FGFR3 mutant or fused (activating hotspot mutations or/and acti-
vating gene fusions) metastatic urothelial cancer after progression on
ﬁrst-line chemotherapy (FDA) or monotherapy with immune check-
point inhibitors (EMA)
9.T e s t i n gf o rFGFR3 mutations and fusions is
currently prescribed to identify suitable patients for erdaﬁtinib treat-
ment. It can be performed either with simple hotspot targeting poly-
merase chain reaction protocols, next-generation sequencing (NGS)
o nD N Aa n dR N Al e v e l ,o rb ys p e c iﬁc RT-qPCR assays coveringFGFR2/3
mutations and fusions in a one-shot assay requiring tumor RNA
(Therascreen Assay, Quiagen; companion diagnostic assay for
erdaﬁtinib)
9. However, these assays are dependent on high tissue
quality (especially those based on RNA), are accompanied by long
turnover times (e.g., NGS-based assays), and are relatively expensive if
only one candidate gene has to be tested. Thus, the development of
pre-screening tools that can be easily and quickly applied in routine
diagnostic material, such as hematoxylin and eosin (H&E) glass slides
of tumor tissue utilized for routine pathological diagnostics, are of
signiﬁcant interest. This is all the more critical as recently published
data from the THOR trials conﬁrmed the clinical efﬁcacy and beneﬁto f
erdaﬁtinib in FGFR3 mutant or fused metastatic urothelial cancer
patients
10. In particular, the rapid administration of a further therapy
regimen is crucial to increase the likelihood of disease control or
therapy response in patient subsets that have already progressed to
multiple prior therapy regimens. Thus, pre-screening tools could
identify patients with a high probability of having a vulnerable altera-
tion in a fast and cost-effective manner. In contrast, patients with a very
low probability could be referred directly to another potentially
effective therapy without wasting valuable time on extensive testing.
In this work, we propose a deep-learning model designed to
detect FGFR3-mutant tumors using routine histology slides (H&E
staining) from bladder carcinoma patients. Weﬁnd that using our pre-
screening tool can save on average 40% of molecular tests by ruling out
wild-type cases. We address key questions for use in clinical routine by
studying our model’sc o nﬁdence in its predictions, inter-block varia-
bility, and its performance on histological subtypes.
Results
The model saves on average 40% of molecular tests
The model was trained and validated using a total of 1222 cases across
multiple cohorts (Fig. 1a, b). The model ’s training phase utilized a
discovery cohort of 391 cases, achieving a cross-validation area under
the receiver operating characteristic (AUC) of 0.82 [0.74 –0.90].
External validation was conducted on three independent cohorts of
MIBC cases: TCGA MIBC (n = 307), MIBC II (n =1 8 3 )a n dm U C(n = 96).
The model was successfully validated with AUCs of 0.82 [0.75 –0.88],
0.89 [0.82–0.93], and 0.82 [0.68–0.94] on TCGA MIBC, MIBC II, and
mUC, respectively (Fig.2a–c).
Using an operating threshold calibrated to minimize false nega-
tives, our model demonstrated excellent performance as a pre-
s c r e e n i n gt e s ta c r o s st h eT C G A ,M I B CI I ,a n dm U Cc o h o r t s .T h e
model achieved near-perfect negative predictive values (NPV) of 0.99
[0.98–1.00] for TCGA, 0.99 [0.98–1.00] for MIBC II and 1.00 [0.97–1.00]
for mUC. This high NPV allowed us to reliably identify patients who do
not require further molecular testing, potentially saving 144 (47.2%), 72
(37.9%), and 35 (36.5%) molecular analyses in the TCGA, MIBC II, and
mUC cohorts, respectively (Table1). The model’s performance across
cohorts was as follows (Sensitivity/Speci ﬁcity/PPV): TCGA = 0.96
[0.92–1.00]/0.47 [0.30 –0.72]/0.14 [0.09 –0.23], MIBC II = 0.96
[0.92–1.00] / 0.47 [0.36 –0.85]/0.21 [0.13 –0.45], mUC = 1.00
[0.92–1.00]/0.32 [0.12–0.70]/0.17 [0.10–0.34]. The detailed results can
be found in Supplementary Table 2. When evaluated on the identical
TCGA cases provided by Loefﬂer et al.
11,o u rm o d e la c h i e v e da nA U Co f
0.83 [0.76–0.88] in external validation. This represents a substantial
improvement of their reported AUC of 0.70 in cross-validation.
Interestingly, we found that using a model trained at a resolution
of 1.0 micrometer per pixel (MPP) yielded a performance improve-
ment over models trained at 0.5 MPP (see Supplementary Table 4 for a
detailed comparison).
Since our cohorts featured various hotspot mutations (Supple-
mentary Table 7), we investigated whether some hotspots were easier
to detect than others. We looked at all the hotspots with more thanﬁve
occurrences in our dataset and found six: Y373C, S249C, R248C,
G380R, G370C, and S371C. S249C was the easiest to detect across the
TCGA, mUC, and MIBC II cohorts (Fig. 3a–c).
In our analysis, we evaluated the prevalence of FGFR3 mutations
and the model ’s prediction accuracy based on sex. No statistically
signiﬁcant differences in FGFR3 mutation prevalence were observed
between males and females across training and validation cohorts
(Supplementary Table 15). When stratifying according to sex, the small
sample sizes preclude deﬁnitive conclusions.
Training on NMIBC cases improves the model performance
NMIBC and MIBC are biologically and pathologically different disease
entities with different rates ofFGFR3 alterations. Interestingly, despite
known morphological and molecular differences, we observed that a
model trained on additional NMIBC cases (MIBC and NMIBC) out-
performed a model trained on MIBC cases only (see Supplementary
Table 3). The model trained on both MIBC and NMIBC demonstrated
superior performance across all external validation cohorts compared
to the model trained exclusively on MIBC. Notably, incorporating
NMIBC cases in the training set led to signi ﬁcant improvements not
only for TCGA NMIBC but also for TCGA MIBC. The model trained
jointly on NMIBC and MIBC cases achieved AUCs of 0.87 [0.83 –0.91]
for TCGA NMIBC and 0.82 [0.75–0.88] for TCGA MIBC, both marking
substantial enhancements over the baseline model trained solely on
MIBC cases.
Since the TCGA database contained both MIBC ( n =3 0 7 ) a n d
NMIBC ( n = 65) cases, we also validated our model on the pooled
cohort MIBC and NMIBC cases (n = 372). Our model performed better
with an AUC of 0.87 [0.83 –0.91]. To further investigate the model ’s
transferability from MIBC to NMIBC, we conducted an external
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 2

Surgical Collec/g415on
1
FFPE Prepara/g415on
2
DNA & RNA 
Sequencing
3
Model Training
4
a
b
TCGA
n = 307 (8%)
Excluded (n = 43)
- Blurry (n=43)
Erlangen hospital
MIBC I
n = 236 (11%)
mUC
n = 96 (13%)
NMIBC I
n = 155 (42%)
MIBC II
n = 183 (11%)
Excluded (n = 105)
- No FFPE slide (n=25)
- No RNAseq / mutation status (n=7)
- No MIBC tumor slide (n=73)
Public
Validation
n = 586 (11% FGFR3-mutant)
Training
n = 391 (23% FGFR3-mutant)
n=810 resected 
patients
DNA sequencing
FGFR3 MUT or WT
(ground truth)
pTa pT1 ≥ pT2
TCGA
n = 412
DNAseq available RNAseq available
FGFR3MUT
Predic/g415on
5
MUTWT
32%
n=812 slides 
collected
n=391 slides used 
for training
n=421 slides used 
for validation
MIBC I
n = 239
NMIBC I
n = 155
MIBC II
n = 201
NMIBC II
n = 109
mUC
n = 106
NMIBC II
n = 97 (65%)
Transferability
Experiment
Fig. 1 | Clinical workﬂow and cohorts presentation. a Multiple cohorts encom-
passing 810 cases were selected from the Erlangen hospital, where patients had
undergone surgical bladder tissue extraction (Step 1). These tissue specimens
were then preserved using formalin ﬁxation and parafﬁn embedding (FFPE) and
subsequently stained with hematoxylin and eosin (H&E) for histological exam-
ination (Step 2). Following this, consecutive cuts of the tissue were subjected to
DNA sequencing utilizing the TSO 500 assay. The DNA sequences were aligned on
a reference genome to detect the mutation hotspots across samples. This map-
ping process enabled the determination of the FGFR3 mutation status among the
patients (Step 3). Subsequently, the H&E slides and the FGFR3 mutation status
were used as input to train and validate a deep-learning model.b FFPE slides from
all cohorts were visually inspected to detect artifacts. Slides that did not pass the
visual inspection were excluded from the training and validation cohorts. The
model was trained on 391 cases and validated on 586 cases, spanning locally
advanced and metastatic muscle-invasive bladder cancer (MIBC) cases. The per-
centages in italic correspond to theﬁnal proportion of FGFR3-mutant cases in the
cohorts. We made sure that the training and validation cohorts were enriched in
MIBC cases (MIBC I for training and MIBC II for validation). A detailed ﬂow
chart to select MIBC cases from the TCGA cohort is available in Supplementary
Fig. 2. Besides, to explore the model ’s potential applicability to non-muscle-
invasive bladder cancer (NMIBC), we included an additional cohort of 109
NMIBC cases (NMIBC II). While not part of our formal external validation, this
cohort served as an exploratory dataset to test the model ’s transferability. A
succinct description of the stages of our cohorts is presented in the bottom right
pie chart.
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 3

validation on the cohort NMIBC II (n = 97). The model performed
worse in this external NMIBC cohort than on external MIBC cohorts,
scoring an AUC of 0.70 [0.61 –0.80], with sensitivity of 0.93
[0.92–0.97], Speciﬁcity of 0.34 [0.13 –0.57], positive predictive value
(PPV) of 0.73 [0.63–0.82] and NPV of 0.73 [0.50–0.86]. It’si m p o r t a n t
to note that this transferability experiment from MIBC to NMIBC was
conducted primarily to explore the model’s generalization capabilities.
The observed decrease in performance on the NMIBC cohort is not
entirely unexpected, as the model was speci ﬁcally trained and opti-
mized for MIBC cases.
The model performed consistently across histological subtypes
We examined the model ’s performance across various histological
subtypes, categorizing the 3 validation cohorts into conventional
urothelial, divergent subtype, and neuroendocrine groups. The dis-
tribution of these cases is presented in Supplementary Table 9. Our
analysis revealed consistent model performance across these sub-
types (Supplementary Table 12). Additionally, we assessed the
model’s performance in relation to different growth patterns, clas-
sifying cases as either solid or papillary (Supplementary Table 10).
The results demonstrated stable performance for both patterns
(Supplementary Table 13), with AUC values ranging from 0.84 to 1.00
on MIBC II, 0.81 to 1.00 on mUC, and 0.79 on TCGA MIBC. Lastly, we
investigated whether the presence of carcinoma in situ (CIS) affected
the model’s performance (Supplementary Table 11). This analysis also
showed consistent results (Supplementary Table 14), with an AUC of
0.90 [0.79–0.97], 0.89 [0.73 - 0.99] for cases presenting CIS and an
AUC of 0.88 [0.78 –0.96], 0.83 [0.61 –1.00] with no CIS, respectively
on MIBC II and mUC. In all three analyses, the model maintained
robust performance across the various categories examined.
Besides, we investigated whether FGFR3-mutant low-grade or high-
grade carcinomas were particularly harder to predict. We found that
our model performed better on low-grade cases with an AUC of 0.89
[0.75–1.00] compared to an AUC of 0.82 [0.74 –0.88] for high-grade
cases on TCGA MIBC.
The model demonstrates high conﬁdence in its predictions
To test the model’s robustness, we investigated the variability in pre-
diction scores between slides from the same case (Fig. 4a, b). The
intraclass correlation coefﬁcient between the prediction scores from
multiple slides on the mUC cohort was 0.66 [0.42 –0.90] and 0.89
[0.76–0.96] on the TCGA MIBC cohort. Additionally, given the model’s
aSensitivity
Specificity
bc
0.0
0.2
0.4
0.6
0.8
1.0
1.0 0.8 0.6 0.4 0.2 0.0
d
 f
Predicted FGFR3-mutant
e
5mm
112μm
TCGA (n=307)
AUC=0.82
mUC (n=96)
AUC=0.82AUC=0.89
MIBC II (n=183)
1.0 0.8 0.6 0.4 0.2 0.0 1.0 0.8 0.6 0.4 0.2 0.0
Wild-type FGFR3-mutant
NPV=0.99
PPV=0.14
NPV=0.99
PPV=0.21 NPV=1.00
PPV=0.17
5mm
5mm 5mm
Fig. 2 | FGFR3 mutation prediction. a–c Receiver operating curves (ROC) of the
FGFR3MUT model on TCGA MIBC (left), MIBC II (middle), and mUC (right). The
area under the ROC curve (AUC) is displayed in the upper-left corner.d Thumbnail
of a FGFR3-mutant case (top) and wild-type case (bottom).e The FGFR3 mutation
prediction heatmaps showing a probability of each 112 × 112μmt i l eh a r b o r i n g
FGFR3-mutated features, for a FGFR3-mutant case (top), and wild-type case (bot-
tom). f Corresponding most predictive regions of the FGFR3 mutation status (top)
and wild-type status (bottom) across the mUC cohort. We inspected the 100 most
predictive tiles of the slide and sampled 9 representative tiles. Regions predictive of
FGFR3 mutations revealed monomorphous conventional urothelial tumor mor-
phology and low desmoplastic tumor stroma content. Conversely, regions pre-
dictive of the wild-type status contained pleomorphic tumor morphology and
desmoplastic tumor content. Source data are provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 4

notably strong performance on the mUC cohort, we sought to explore
the differences in FGFR3 mutation score produced by the model for
primary versus metastatic sites. Of the 96 metastatic cases, 4 had at
least one tissue sample from the primary tumor site and one from the
metastasis. For these 4 cases, we found that none of the slides, whether
from the primary or metastatic sites, would lead to a different diag-
nosis since all scores were signi ﬁcantly higher than the operating
decision threshold. Furthermore, to qualitatively assess the difference
between primary and metastatic slides, we looked at the top predictive
tiles from primary and metastatic sites (Fig. 5b). After careful inspec-
tion by a pathologist, no signiﬁcant differences in histomorphological
patterns were found between both sites.
To evaluate the model’sc o nﬁdence in its predictions, we analyzed
the variance in predicted class probabilities across the 125 multiple-
instance models comprising the ﬁn a le n s e m b l e( s e eU n c e r t a i n t y
quantiﬁcation and conformal prediction in the Methods section). We
sampled 30 cases each from TCGA (Fig.4c), MIBC II (Fig.4d), and mUC
(Fig. 4e) cohorts, examining average predictions and their associated
variances. Notably, for all observed FGFR3-mutant cases across the
three external validation cohorts, the prediction variance near the
calibrated classiﬁcation thresholds (Table 1) is low, indicating high
agreement among the models in the ensemble in assigning prob-
abilities for these cases. This demonstrates the model ’s high con-
ﬁdence in identifyingFGFR3-mutant cases, effectively minimizing false
negatives. We further derived conformalized predictions
12 and pre-
diction sets from the model. These 95% con ﬁdence prediction sets
contain either a single class (wild-type or FGFR3-mutant) or both
classes when the model lacks conﬁdence. The expected cardinality of
prediction sets was 1.42 [1.00–1.71] for TCGA, 1.12 [1.05–1.29] for MIBC
II and 1.19 [1.05–1.28] for mUC, showing that for the majority of cases
the model is conﬁdent enough to only include one class in its predic-
tion sets.
Histopathology shows patterns linked to FGFR3 mutations
To ensure our model accurately identiﬁed FGFR3 mutations in patho-
logically relevant regions, we presented the highest and lowest-scoring
predictive tiles to a pathologist for veri ﬁcation (Fig. 2d, e; see Inter-
pretability analysis in the Methods section). The regions most asso-
ciated with FGFR3 mutations revealed monomorphous conventional
urothelial tumor morphology and low desmoplastic tumor stroma
content (Fig. 2f). In contrast, the least associated regions contained
pleomorphic tumor morphology and high amounts of desmoplastic
tumor stroma (content). These ﬁndings align with those reported by
Loefﬂer et al.
11., speciﬁcally in relation to the predictive accuracy of
papillary tumor growth and the presence of homogeneous, regularly
shaped nuclei in the most predictive regions of the FGFR3-mutation
status.
To accurately quantify which histology patterns were linked to
FGFR3 mutations, we selected 400 tiles from TCGA MIBC associated
with the FGFR3-mutant status ( n =2 0 0 ) a n d t h e w i l d - t y p e s t a t u s
(n = 200). A pathologist (M.E.) annotated the regions (tiles), assigning
one or multiple histology patterns to every tile (more details can be
found in the Supplementary Methods section). We found that most
tiles predictive of wild-type andFGFR3 statuses contained tumor cells,
with 99% of mutant tiles and 57% of wild-type tiles containing tumor
cells. Tiles predictive of theFGFR3-mutant status had a monomorphic
appearance, which was observed in 18% of mutant tiles compared to
only 4% of wild-type tiles (p < 0.001). Tiles predictive of the wild-type
status were associated with desmoplastic stroma in the tumor, present
in 12% of wild-type tiles but only 1% of mutant tiles ( p < 0.001). Addi-
tionally, in ﬂammation lymphocytes in the microenvironment were
observed in 12% of wild-type tiles compared to just 1% of mutant tiles
(p <0 . 0 0 1 ) ( F i g .5a). The detailed ﬁndings are presented in Supple-
mentary Table 8.
We also examined the histology patterns associated with the
mutation hotspots. We found that the top predictive tiles for FGFR3
mutations, except for those for G380R, predominantly reﬂected tumor
morphologies with low or absent stroma content and monomorphic
and bland-appearing tumor cell nuclei (Supplementary Fig. 1).
Low-expressorFGFR3 mutants mimic wild-type morphology
Given the prevalent association between FGFR3 mutations and ele-
vated FGFR3 expression levels13, we carried out a validation excluding
atypical FGFR3-mutant cases characterized by low FGFR3 RNAseq
expression. We analyzed FGFR3 RNAseq TPM-normalized expression
Table 1 | Performance of the FGFR3MUT prediction model
across three external validation cohorts
Cohorts Predicted FGFR3-
mutant
patients (%)
Potentially saved
molecular tests(%)
Operating thresh-
old (between 0
and 1)
TCGA MIBC 161 (53) 144 (47) 0.059
MIBC II 118 (63) 72 (37) 0.051
mUC 61 (64) 35 (36) 0.063
Predicted FGFR3-mutant patients indicate the number of patients the model predicted to have
an FGFR3 mutation. Potentially saved molecular tests represent the number and percentage of
patients in each cohort for whom molecular testing could potentially be avoided based on the
model’s predictions. Operating threshold denotes the classiﬁcation threshold (between 0 and 1)
used for the model in each cohort to achieve these results.ab
Predic/g415on
0.1
0.3
0.5
0.7
c
WT S249C Y373C WT S249C Y373C
IICBIMCUmAGCT
0.0
0.2
0.4
0.8
0.6
0.2
0.0
0.4
0.6
0.8
Fig. 3 | Model performance across mutation hotspots. a–c Distribution of model
prediction scores for the most prevalent FGFR3 mutation hotspots in TCGA
(n =3 0 0 ) ,m U C(n =9 4 )a n dM I B CI I(n = 186). The wild-type (WT) category is uti-
lized as a reference point for comparison. The exact number of hotspot mutations
in each cohort is given in Supplementary Table 7. Center corresponds to the
median, lower and upper hingers indicate theﬁrst and third quartiles, and whiskers
to the high/lowest value no further than 1.5× inter-quartile range. Source data are
provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 5

across the TCGA cohort, identifying the ﬁrst and third quartiles of
expression. Our initial step involved excluding FGFR3-mutant cases
that were within the lowest quartile of FGFR3 expression ( n =1 4 ) ,
resulting in an improved AUC of 0.86 [0.79–0.92]. Next, we excluded
wild-type cases (n = 82) that exhibited high FGFR3 expression, falling
into the highest expression quartile, leading to an AUC of 0.85
[0.78–0.91]. By eliminating both atypical groups from our analysis, the
model’s performance on the TCGA cohort was notably enhanced,
achieving an AUC of 0.89 [0.83–0.94] (Supplementary Tables 5 and 6).
Our results suggest that mutants with low FGFR3 (respectively, wild
types with highFGFR3) expression have a morphology similar to that of
wild types (respectively mutants), while FGFR3 mutant tumors with
activating mutations and high FGFR3 expression are morphologically
different. In the TCGA MIBC cohort, we evaluated the meanFGFR3 log
TPM-normalized RNAseq expression between wild-type tumors cor-
rectly classiﬁed by the model (true negatives;n =1 3 8 )a n dm i s c l a s s iﬁed
wild-type tumors (false positives; n =1 4 4 ) . T h e a v e r a g eFGFR3
expression in true negative tumors was 3.26, compared to 4.28 in false
positive tumors, with the difference being statistically signi ﬁcant
(Mann–Whitney test, p = 7.9e-8).
Discussion
The recent approval of erdaﬁtinib, a tyrosine kinase inhibitor targeting
the FGFR signaling pathway, represents the ﬁrst targeted therapy for
metastatic urothelial cancer (mUC) with FGFR alterations 10.O t h e r
molecules are currently tested in clinical trials and may represent new
alternatives in the coming years in MIBC and NMIBC, with intravesical
erdaﬁtinib delivery using the TAR-210 system (NCT05316155). Acti-
vating FGFR3 mutations are recurrent oncogenic mutations in UC.
Their frequency is notably high (50 –80%) in non-muscle-invasive
bladder cancer (NMIBC) but decreases to 10–15% in locally advanced
and metastatic UC, with gene fusions being exceedingly rare (~1%)
4–8.
Both the FDA and EMA approval are bound to proven activatingFGFR3
mutations or gene fusions10, which can be assessed by the companion
diagnostic Therascreen assay or by DNA and RNA-based conventional
sequencing or NGS approaches
14. However, all these methods are
either expensive or bound to mRNA (Therascreen, RNA-seq), whose
quality can be severely altered in FFPE tissues. Given the low frequency
in metastatic urothelial cancer, the question arises whether pre-
screening tools utilizing existing H&E tumor slides might help identify
tumors with a high likelihood of harboring targetable activatingFGFR3
0.1 0.2 0.3 0.40.1 0.2 0.3 0.4 0.5 0.20.1 0.4
a
mUC / ICC=0.66
0.1
0.2
0.3
0.4
0.5
0.6
b
Predic/g415on
Cases
TCGA / ICC=0.89
Cases
cde
Cases
TCGA MIBC II mUC
Predic/g415on
Wild-type FGFR3-mutant
Primary
 Metastasis
0.3
Fig. 4 | Prediction robustness and uncertainty quantiﬁcation. a–b Variability in
model predictions across multiple slides from the same patient in the mUC (left)
and TCGA (right) cohorts. The intraclass correlation coefﬁcient (ICC) was 0.66
[0.42–0.90] for mUC and 0.89 [0.76–0.96] for TCGA. Metastatic slides are repre-
sented by crosses, while primary slides are shown as circles. c–e The ensemble
model’s prediction variability for the FGFR3 mutation status was evaluated by
randomly selecting 30 samples from each validation cohort: TCGA MIBC (c), MIBC
II (d), and mUC (e). The data is represented as mean values ± variance of the
predictions, with blue representing true wild-type cases and red indicating true
FGFR3-mutant cases. The variances were quantiﬁed using deep ensemble uncer-
tainty quantiﬁcation, and the statistics for each sample were obtained from 150
data points (models) per sample. Source data are provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 6

alterations in order to reduce testing costs and turnaround times. In
case of poor RNA and DNA quality, such tools could further predict
whether rebiopsy of metastasis or obtaining a liquid biopsy might be
indicated.
Therefore, in the present study, we outlined the development and
validation of a deep learning model trained for assessing the FGFR3
mutation status of locally advanced and metastatic urothelial cancer
patients by utilizing digitized H&E images of patient tumors. While we
decided to develop an algorithm directly trained to predict the pre-
sence or absence of activatingFGFR3 mutations in H&E histopathology
slides, other studies have demon strated, that the presence of FGFR
gene alterations can be predicted based on surrogate parameters such
as low in ﬁltration with tumor-inﬁltrating lymphocytes, which is sup-
posed to be a common feature of FGFR3 mutant urothelial
carcinomas
15,16, but not a predictor for decreased responsivity to
immunotherapy17. Validating these interestingﬁndings from Velhamos
et al.15, we also observed that top predictive tiles for the presence of
FGFR3 mutations were lymphocyte depleted15. Our results showed that
the model identiﬁed at least 93% (up to 100%) ofFGFR3-mutant cases in
three independent validation cohorts. The model showcased
commendable AUCs (at least 82%) across three cohorts, reinforcing its
robustness and clinical applicability. A paramount strength of our
study lies in its extensive validation, covering a large spectrum of
disease stages, from pT2 cases to metastatic patients, that were col-
lected consecutively at multiple centers without speciﬁci n c l u s i o no r
exclusion criteria. Notably, our sensitivity of 100% on the mUC cohort
with a negative predictive value (NPV) of at least 98% underlines the
clinical relevance of this assay to pre-screen patients who could beneﬁt
from an FGFR3-targeted therapy, like erdaﬁtinib.
One notable aspect of our approach was including NMIBC cases in
the training phase. Our strategy proved beneﬁcial despite NMIBC and
MIBC being distinct entities with different pathological and clinical
pathways and morphology
8. Although mixing NMIBC with MIBC/mUC
is considered the “original sin” in bladder cancer research, integrating
NMIBC cases likely introduced a broader spectrum of histological
features associated with FGFR3 mutations regardless of tumor stage,
including monomorphic tumor cell appearance, low desmoplastic
stroma content, and low or absent immune inﬁltration, enhancing the
model’s generalizability. Although unconventional, this cross-disease
training approach contributed signiﬁcantly to the model’s impressive
aFrequency0.1
0.2
0.3
Predic/g415vity: FGFR3MUT WT
b
112 μm
Arteries
(NT)
Atypia
(T)
Inflammation
Lymphocytes
(NT)
Mitosis
(T)
Monomorphic
Appearance
(T)
***
Desmoplastic
Stroma
(NT)
***
***
***
***
112 μm
112 μm
Fig. 5 | Histopathological features associated with FGFR3 mutations.
a Proportion of histology patterns associated with FGFR3 mutation status. A
pathologist (M.E.) independently examined 400 representative tiles from TCGA
MIBC, equally divided between FGFR3-mutant (n = 200) and wild-type (n =2 0 0 ) ,t o
identify patterns indicative of each status. Tumor-associated patterns are denoted
by (T), whereas patterns identiﬁed in non-tumorous regions are represented by
(NT). The detailed ﬁndings are presented in Supplementary Tables 8 and 9. Key
observations include a monomorphic appearance (FGFR3MUT: 18%, WT: 1%,
P = 4.3e-13) and atypia (FGFR3MUT: 27%, WT: 12%, P = 5.0e-3) in FGFR3-mutant
tumors, while wild-type tumors typically elicit an immune response (FGFR3MUT:
0%, WT: 12%, P = 2.9e-8) and are characterized by the presence of desmoplastic
stroma (FGFR3MUT: 1%, WT: 14%, P = 9.8e-13). Statistical signiﬁcance was assessed
using a two-sided z-test for proportions, with Bonferroni adjustment for multiple
comparisons. Statistically signiﬁcant differences were marked with the *** symbol.
b Comparison of top predictive tiles for the same metastatic FGFR3-mutant patient
from the mUC cohort. The left slide shows the top predictive tiles on the primary
site, while the right slide shows the top predictive tiles on the metastasis. For each
group, we inspected the 50 most predictive tiles of the slide and sampled 6
representative tiles. Source data are provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 7

performance in external validation. It underscores the potential of
leveraging histopathological similarities across different stages of the
disease to enhance an artiﬁcial intelligence model’s performance. This
ﬁnding also opens avenues for future research in developing more
comprehensive models that span various cancer stages and types,
potentially leading to more robust and universally applicable diag-
nostic tools. Furthermore, it underlines that features related toFGFR3
mutations can be partially bound to speci ﬁc morphological features
maintained throughout progression and metastatic dissemination.
While our model performed well in detecting targetable FGFR3
mutations, it is worth noting that in the early phase of the study, we
also tried includingFGFR3 fusions in the MIBC I and TCGA cohort. Yet,
our model could not learn to detect those alterations, most likely due
to the rarity of these alterations (a total of 10 cases across n =5 4 3
tumors of MIBC I and TCGA cohort). The scarcity of such cases in our
dataset might have limited the model’s ability to learn and recognize
associated histological patterns. Furthermore, we hypothesized that
associated patterns might be very different from tumors with acti-
vating FGFR3 point mutations that cannot be sufﬁciently captured due
to the very low number of cases. This remains speculation and has to
be further elucidated in datasets with larger numbers of tumors with
FGFR3 fusions, which is important since patients with FGFR3 fusions
also beneﬁt from erdaﬁtinib treatment in metastatic stage (HR = 0.49,
95%-CI 0.23–1.03)
10.
In conclusion, we demonstrated that H&E slides contain sufﬁcient
information to predict FGFR3 mutations in muscle-invasive and
metastatic urothelial cancer. These results pave the way for developing
a diagnostic tool for detectingFGFR3 mutations. While our results are
promising, they must be con ﬁrmed through a large-scale, blind vali-
dation study to ensure the tool ’s reliability in a clinical setting. Cru-
cially, our study calls for a subsequent calibration study to investigate
how different operating thresholds might impact the predictive values
of the model— ideally in patient cohorts treated withFGFR3 inhibitors,
that allow correlations with therapy outcomes. This calibration pro-
cess is essential to adapt a potential diagnostic tool to the speci ﬁc
variations and conditions encountered in diverse clinical environ-
ments. In addition, further studies are required to study whether
FGFR3 fusions, that indicate FGFR3 inhibition susceptibility, can be
predicted from H&E histopathology slides.
Methods
Ethics approval
The present study was approved by the Institutional Ethical Review
Board of Friedrich-Alexander-University Erlangen-Nuremberg FAU
(protocol code 4607, 2015; protocol code 97_18Bc, 2018; protocol
code 22-343-B, 2022; and protocol code 217_18C, 2018), and patients
gave written informed consent. All experiments were carried out under
the Declaration of Helsinki.
Datasets description
In total, we included n = 1222 patients with non-invasive or stroma-
invasive (papillary) urothelial carcinomas (NMIBC: n = 264), muscle-
invasive urothelial carcinomas (MIBC: n =4 4 0 ; T C G A B L C A c o h o r t :
n = 412) and metastatic urothelial carcinomas (mUC, n =1 0 6 ) o f t h e
bladder (Supplementary Table 1). Patients from all utilized cohorts
were included consecutively in the sequence of treatment mentioned
below to account for expected sex distribution for urothelial bladder
cancer. As outlined in Supplementary Table 1 this strategy led to a
balanced biological sex distribution (sex assigned at birth) as expected
for urothelial (bladder) cancer. No self-reported gender data are
available for the present cohorts. No inclusion or selection criteria
were applied except the availability of FFPE tissue material for nucleic
acid isolation and H&E stained tumor tissue carrying slides for digiti-
zation. Per sample a FFPE block with at least 30% tumor content
(related to all tissue covered on the block) and at least an area of vital
non-necrotic 0.5 × 0.5 cm tumor tissue area with surrounding tumor
stroma was selected by an experienced board-certi ﬁed uropatholo-
gist (M.E.).
The MIBC cohort consists of n = 546 patients diagnosed with
muscle-invasive urothelial carcinoma of the bladder who have been
treated in curative intent by radical cystectomy plus lymphade-
nectomy and perioperative platinum-based chemotherapy according
to applying EAU guidelines between 2008 and 2022 (Fig.1a). Digitized
H&E slides in conjunction with molecular data on FGFR3 mutations
were available inn = 440 patients of this cohort (split into two cohorts
for training [MIBC I] and validation [MIBC II]). The NMIBC I cohort
comprises n = 155 pTa and pT1 carcinoma patients treated by local
surgical (transurethral resection) ± instillation therapy adapted to EAU
risk classes between 2010 and 2020. The NMIBC II cohort consisted of
n = 109 independent pTa carcinomas that were treated by transure-
thral resection followed by surveillance adapted to EAU risk classes
between 2020-2023. The mUC cohort consists of 106 patients with
metastatic urothelial cancer treated with standard regimes such as
platinum-based chemotherapy and immunotherapy. All digitized H&E
slides used in the present study were of intrinsic cancer tissues
retrieved from the initial cancer diagnosis made on tissue material of
the ﬁrst transurethral resection or cystectomy without prior neoad-
juvant chemotherapy treatment or instillation therapy. The FGFR3
alteration status in these tumors was assessed by SNaPshot PCR as
described in detail in the following sections. All cohorts were then
scanned on the same slide scanner with identical settings. Thus, the
present study cohort contains digitized H&E images that have been
stained with a variety of H&E staining protocols in- and outside of
Erlangen University Hospital, thus covering a signi ﬁcant variance in
staining.
TCGA-BLCA is a multicentric cohort of 412 cases from the public
TCGA database
18. TCGA slides were used in digital format (downloaded
from TCGA slide archive) and were H&E stained outside of our insti-
tution. Cases without a formalin-ﬁxed parafﬁn-embedded tissue slide,
FGFR3 mutation status, and RNA sequencing were ﬁrst ﬁltered out.
Slides of the remaining cases were then reviewed by an expert
pathologist (M.E.), and cases without a slide containing tumor tissue
covering MIBC were excluded. Ultimately, this led to the inclusion of
307 cases from the TCGA-BLCA repository (Fig.1b and Supplementary
Fig. 2). In our study, we denote this cohort TCGA. TheFGFR3 mutation
status was obtained via the CBioPortal in the TCGA BLCA PanCan Atlas
2018 collection
18. The cases harboring non-activating or inactivating
FGFR3 mutations/alterations (H349D, S344Y, P358L, V306I, L88Wfs*10,
Q674*, E216K, D222N, G235D, and H791Tfs*29) were considered“wild-
type” tumors as those mutations are not leading to a FGFR inhibitor
targetable phenotype. The RNA sequencing was obtained fromhttps://
portal.gdc.cancer.gov/.O ft h e s e3 9 7c a s e s ,2 4w e r eFGFR3 mutants,
corresponding to 8% of the cohort. Supplementary Table 7 provides a
detailed breakdown of the most frequent mutations in all the cohorts.
Supplementary Table 1 provides a detailed summary of the main
clinical variables for all the cohorts included in the study.
Mutational detection via SNaPshot PCR and mRNA expression
DNA for mutational testing in NMIBC, MIBC, and mUC cohorts and
RNA for gene expression pro ﬁling was isolated from FFPE using an
automated procedure (Promega Maxwell, Promega, Wisconsin, USA).
Five 10 µmF F P Es e c t i o n sw i t ha tl e a s t5 0 %t u m o rc o n t e n tw e r eu s e d
per patient tumor and microdissected to maximize tumor purity.
Sections were deparafﬁnized, tissues microdissected and suspended
in 300 µl incubation buffer (Promega), and digested with Proteinase K
(Promega) at 56 °C overnight (550 rpm). DNA or RNA was then isolated
from lysates using the Promega DNA FFPE puri ﬁcation Kit (Promega,
Wisconsin, USA) according to the manufacturer’s instructions. After-
ward, DNA or RNA samples were puri ﬁed, quanti ﬁed, and quality-
controlled using the Qubit Fluorometer (Thermoﬁsher).
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 8

FGFR3 mutation analysis was performed by a modiﬁed SNaPshot
PCR protocol19–21.T h r e er e g i o n so ft h eFGFR3 gene on Exons 7, 10, and
15 are ampliﬁed in a multiplex PCR followed by extension of mutation-
speciﬁc primers with labeled dideoxynucleotides. After removing
excess primers and dNTPs, eight SNaPshot primers detecting nine
FGFR3 mutations were annealed to the PCR products and extended
with a labeled dideoxynucleotide. These extended primers were ana-
lyzed on an automatic sequencer, with the label on the incorporated
nucleotide indicating the presence or absence of a mutation. A second
and independent SNaPshot analysis veriﬁed all mutations. This allows
sensitive detection of a total of eleven known activating FGFR3 muta-
tions that account for over 99% of known activating FGFR3 mutations
(p.R248C, p.S249C, p.G372C, p.G38 2R, p.S373C, p.Y375C, p.A393E,
p.K652E, p.K652Q, p.K652M and p.K652T) and all known activating
FGFR3 mutations found in urothelial bladder cancer.
mRNA sequencing for FGFR3 mRNA expression quantiﬁcation in
the MIBC I cohort was performed from 500 ng puri ﬁed input RNA
using the QuantSeq FWD Kit (Lexogen), which generates Illumina-
compatible libraries from poly-adenylated mRNA
22,23.S e q u e n c i n gw a s
performed on an Illumina NovaSeq 6000 platform (single end;
1 × 75 bp), yielding at least 20 M clusters per sample. Preprocessing of
demultiplexed raw data (FASTQ ﬁles) was performed via the nf-core
RNA-seq pipeline v.3.3
22,23. TPM normalized expression data was log2
transformed for further analyses.
Preprocessing of whole-slide images
Whole slide images (WSI) are typically 100,000 × 100,000 pixels in
dimension, making it computationally intractable to feed them
directly to a deep learning model. We used a preprocessing pipeline to
reduce the dimensionality of the data, which can be decomposed into
three steps: 1) matter detection, 2) t iling, and 3) feature extraction.
First, the tissue is detected on the WSI: a U-Net neural network seg-
m e n t sp a r to ft h ei m a g et h a tc o n t a i n sm a t t e ra n dd i s c a r d sr e g i o n sw i t h
folded tissue, with artifacts (e.g. pen markers) or blurriness. This U-Net
was trained on 460 H&E and IHC slides from an internal dataset where
the tissue was manually annotated and validated on 115 slides with a
Dice score of 0.96. Second, the regions detected as matter are tiled
into smaller images (the“tiles”) of size 224 × 224 pixels, corresponding
to an effective area of 224 × 224 μm (1.0 MPP). To be selected, a tile
from an H&E slide must have at least 60% of the matter detected by the
U-Net
24. Eventually, 1539 features are extracted from each selected tile
using Bioptimus ’ H0 (a Vision Transformer Giant) 25. The feature
extractor for H&E slides is trained in a self-supervised fashion using
DINOv2
26 without using any labels. For training and inference, the
feature extractor weights were frozen. At the end of this preprocessing
pipeline, each slide is represented by a matrix of size (n_tiles, 1539).
FGFR3 mutation prediction
The model detecting FGFR3 mutations was trained on a discovery set
comprising two cohorts (MIBC I, n = 239; NMIBC I, n = 155) and vali-
dated on three independent MIBC validation cohorts (TCGA, n =3 7 3 ;
MIBC II,n = 183; mUC,n =9 6 ) .T h eFGFR3 mutation status was obtained
by DNA sequencing using the SNaPshot method, described in detail in
the “Datasets description” and “Mutational detection via SNaPshot
PCR and mRNA expression sections” above
21. The slides were split into
small tiles of 224 × 224 pixels, corresponding to a tissue size of
224 × 224μm at 1.0 MPP. The features were extracted with a pre-
trained model from these tiles (more details in the Preprocessing of
whole-slide images section).
The ﬁnal model is an ensemble of 125 multiple-instance learning
(MIL) models. The predictions of each model were aggregated by
averaging all the output logits. Each MIL model uses the WSI pre-
processing pipeline described in the section“Preprocessing of whole-
slide images.” For training, a maximum of 5000 tiles are uniformly
sampled from each slide for speed and memory considerations. All
models have an identical structure, as proposed by Courtiol et al.
27.
First, each tile’s score corresponding to the FGFR3 mutation status is
computed. These scores are obtained from a multi-layer perceptron
(MLP) with 128 hidden neurons followed by one neuron and a ReLU
activation. We select the 100 top and bottom scores. Finally, these
extreme scores are passed to a linear activation to obtain aﬁnal output
logit. The logit is passed in a sigmoid layer to obtain a probability of
whether the case isFGFR3-mutant or wild-type. The model was trained
with the binary cross-entropy loss, using the labels obtained from the
DNA sequencing described in the “DNA sequencing and FGFR3 muta-
tion status” section.
Performance assessment and statistical methods
The area under the receiver operating characteristic was used to
quantify the model’s capability to distinguish between wild-type and
FGFR3-mutant tumors. The sensitivity, speci ﬁc i t y ,P P V ,a n dn e g a t i v e
predictive value (NPV) to FGFR3 mutations were used to assess the
ability of the model to identify FGFR3-mutant cases. Con ﬁdence
intervals at 95% con ﬁdence level were obtained by bootstrapping
experiment results with 1000 repeats. All tests were two-tailed, and P-
values < 0.05 were considered statistically signi ﬁcant. The intraclass
correlation coefﬁcient used to assess the model’s agreement between
different slide predictions correspond to Pingouin’s ICC2k metric (a
random sample of k judges rate each target).
Interpretability analysis
An expert pathologist (M.E.) reviewed 400 tiles predictive of FGFR3
mutant status ( n = 200) and wild-type status ( n =2 0 0 ) o f T C G A . T o
analyze the morphological differences of the predictive tiles depend-
ing on the FGFR3 expression level, the 200 predictive tiles of each
status were selected to include 100 tiles with high expression and 100
tiles with low expression. The pathologist assessed twenty histological
criteria (see Supplementary Methods) blinded to their model scores.
Uncertainty quantiﬁcation and conformal prediction
To assess the reliability of our model ’s predictions, we leveraged the
ensemble nature of our prediction model by using a Deep Ensemble
uncertainty quanti ﬁcation technique 28.T h em o d e lc o m p r i s e s1 2 5
individual multiple-instance learning models. For each patient, we
calculated the variance of the predicted probabilities of the predicted
class across these 125 models. This variance serves as a measure of
uncertainty in the model ’s predictions, providing insight into the
conﬁdence level of each classiﬁcation.
To generate conformalized predictions
29,30, we split our external
validation cohort into two equal groups: a calibration set and a test set.
First, we calculated non-conformity scores for the calibration set,
deﬁning them as 1 — the predicted probability of the true class (either
wild-type or FGFR3-mutant). Next, we determined a con ﬁdence
threshold by taking the 95th perc entile of these non-conformity
s c o r e s .T h i sa l l o w e du st od e r i v et h ep r e d i c t i o ns e t so nt h et e s ts e t
31.T o
assess our model con ﬁdence in its predictions, we monitored the
expected cardinality of the prediction sets on the test set.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
All images and the associated FGFR3 mutational status for the TCGA
cohort used in this study are publicly available at https://portal.gdc.
cancer.gov/and cBioPortal (https://www.cbioportal.org/). The cohorts
MIBC I, MIBC II, NMIBC I, NMIBC II, and mUC are the property of
University Hospital Erlangen & Friedrich-Alexander-Universität
Erlangen-Nürnberg. Image data, patient data and molecular data of
patient cohorts of the University Hospital Erlangen (UKER) fall under
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 9

the European general data protection regulation (GDPR) and are
available under restricted access given their potential sensitive nature.
Access can be obtained for academic non-commercial research pro-
jects by contacting the corresponding authors. The processing time
for data access requests may take up to one calendar month. Access to
the sensitive data is restricted to the project duration speciﬁed by the
requesting academic non-commercial researcher/research group.
Source data are provided as a Source Data ﬁle. Source data are pro-
vided with this paper.
Code availability
An implementation of the U-Net is available at https://github.com/
milesial/Pytorch-UNet. An implementation of Bioptimus H0 is avail-
able at https://huggingface.co/bioptimus/H-optimus-0. The packaged
models can be found here: https://github.com/PABannier/fgfr3mut
(https://doi.org/10.5281/zenodo.13959977)32, under a Creative Com-
mons Attribution 4.0 International (CC-BY-4.0) License. The reposi-
tories referenced above contain license ﬁl e sa n dd e t a i l so fu s a g e
permissions. Any reuse of third-party software, including the U-Net
implementation and Bioptimus H0, complies with their respective
licenses.
References
1 . L e n i s ,A .T . ,L e c ,P .M . ,C h a m i e ,K .&M s h s ,M .D .B l a d d e rc a n c e r :a
review. JAMA 324,1 9 8 0–1991 (2020).
2. Saginala, K. et al. Epidemiology of bladder cancer. Med. Sci. 8,
15 (2020).
3. Powles, T. et al. Enfortumab vedotin and pembrolizumab in
untreated advanced urothelial cancer.N. Engl. J. Med. 390,
875–888 (2024).
4. Billerey, C. et al. Frequent FG FR3 mutations in papillary non-
invasive bladder (pTa) tumors.A m .J .P a t h o l .158,1 9 5 5–1959 (2001).
5. Ascione, C. M. et al. Role of FGFR3 in bladder cancer: treatment
landscape and future challenges.Cancer Treat. Rev. 115,
102530 (2023).
6. Gust, K. M. et al. Fibroblast growth factor receptor 3 is a rational
therapeutic target in bladder cancer.Mol. Cancer Ther. 12,
1245–1254 (2013).
7. Tomlinson, D., Baldo, O., Harnden, P. & Knowles, M. FGFR3 protein
expression and its relationship to mutation status and prognostic
variables in bladder cancer.J. Pathol. 213,9 1–98 (2007).
8. Knowles, M. A. & Hurst, C. D. Molecular biology of bladder cancer:
new insights into pathogenesis and clinical diversity. Nat. Rev.
Cancer 15,2 5–41 (2015).
9. Loriot, Y. et al. Erda ﬁtinib in locally advanced or metastatic uro-
thelial carcinoma.N. Engl. J. Med. 381,3 3 8–348 (2019).
10. Loriot, Y. et al. Erda ﬁtinib or chemotherapy in advanced or meta-
static urothelial carcinoma.N. Engl. J. Med. 389, 1961–1971 (2023).
11. Loef ﬂe r ,C .M .L .e ta l .A r t iﬁcial intelligence–based detection of
FGFR3 mutational status directly from routine histology in bladder
cancer: a possible preselection for molecular testing?Eur. Urol.
Focus 8,4 7 2–479 (2022).
12. Banerji, C. R. S., Chakraborti, T., Harbron, C. & MacArthur, B. D.
Clinical AI tools must convey predictive uncertainty for each indi-
vidual patient. Nat. Med. 29, 2996–2998 (2023).
13. van Rhijn, B. W. G. et al. FGFR3 mutation status and FGFR3
expression in a large bladder cancer cohort treated by radical
cystectomy: implications for anti-FGFR3 treatment?†.
Eur. Urol. 78,
682–687 (2020).
1 4 . B a h l i n g e r ,V . ,E c k s t e i n ,M . ,H a r t m a n n ,A .&S t ö h r ,R .E v a l u a t i o no f
FGFR alteration status in urothelial tumors.Methods Mol. Biol.
2684,2 8 3–291 (2023).
15. Velmahos, C. S., Badgeley, M. & Lo, Y.-C. Using deep learning to
identify bladder cancers with FGFR-activating mutations from his-
tology images. Cancer Med. 10,4 8 0 5–4813 (2021).
16. Komura, K. et al. The Impact of FGFR3 alterations on the tumor
microenvironment and the efﬁcacy of immune checkpoint inhibi-
tors in bladder cancer. Mol. Cancer 22,1 8 5( 2 0 2 3 ) .
17. Wang, L. et al. Fibroblast growth factor receptor 3 alterations and
response to PD-1/PD-L1 blockade in patients with metastatic uro-
thelial cancer. Eur. Urol. 76,5 9 9–603 (2019).
18. Tomczak, K., Czerwi ńska, P. & Wiznerowicz, M. The Cancer Genome
Atlas (TCGA): an immeasurable source of knowledge.Contemp.
Oncol. 19,A 6 8–A77 (2015).
19. Koufou, S. et al. Mutational activation of FGFR3 is not involved in the
development of prostate cancer.Pathobiol. J. Immunopathol. Mol.
Cell. Biol. 77,2 4 9–252 (2010).
20. Hafner, C. et al. Mosaicism of activating FGFR3 mutations in human
skin causes epidermal nevi.J. Clin. Investig.116, 2201–2207 (2006).
21. van Oers, J. M. M. et al. A simple and fast method for the simulta-
neous detection of nine ﬁbroblast growth factor receptor 3 muta-
tions in bladder cancer and voided urine. Clin. Cancer Res. 11,
7743–7748 (2005).
22. Wullweber, A. et al. Bladder tumor subtype commitment occurs in
c a r c i n o m ai ns i t ud r i v e nb yk e ys i g n a l i n gp a t h w a y si n c l u d i n gE C M
remodeling.Cancer Res. 81,1 5 5 2–1566 (2021).
23. Köhler, S. A. et al. Improved bladder tumor RNA isolation from
archived tissues using methylene blue for normalization, multiplex
RNA hybridization, sequencing and subtyping.Int. J. Mol. Sci. 23,
10267 (2022).
24. Ronneberger, O. et al. U-Net: convolutional networks for biomedi-
cal image segmentation.Medical Image Computing and Computer-
Assisted Intervention– MICCAI 2015. Lecture Notes in Computer
Science, vol 9351. https://doi.org/10.1007/978-3-319-24574-4_28
(Springer, Cham, 2015).
25. Saillard, C. et al. H-optimus-0. GitHub https://github.com/
bioptimus/releases/tree/main/models/h-optimus/v0(2024).
26. Oquab, M. et al. DINOv2: learning robust visual features without
supervision. Preprint athttps://doi.org/10.48550/arXiv.2304.
07193 (2024).
27. Courtiol, P., Tramel, E. W., Sanselme, M. & Wainrib, G. Classiﬁcation
and disease localization in histopathology using only global
labels: a weakly-supervised approach.ArXiv180202212 Cs
Stat (2020).
2 8 . L a k s h m i n a r a y a n a n ,B . ,P r i t z e l ,A .&B l u n d e l l ,C .S i m p l ea n ds c a l a b l e
predictive uncertainty estimation using deep ensembles. InProc.
the 31st International Conference on Neural Information Processing
Systems, 6405–6416 (2017).
29. Lei J. & Wasserman, L. Distribution-free prediction bands for non-
parametric regression.J. R. Stat. Soc. Ser. BS t a t. Methodol. https://
academic.oup.com/jrsssb/article/76/1/71/7075937(2013).
30. Papadopoulos, H., Proedrou, K., Vovk, V. & Gammerman, A.
Inductive conﬁdence machines for regression. InProc. 13th Eur-
opean Conference on Machine Learning(eds. Elomaa, T., Mannila,
H. & Toivonen, H.) 345–356. https://doi.org/10.1007/3-540-36755-
1_29 (Springer, 2002).
31. Angelopoulos A.N. & Bates, S. Conformal prediction: a gentle
introduction.Found. Trends Mach. Learn.16, 494–591. (2023).
32. Bannier, P.-A. & Saillard, C. FGFR3MUT: AI allows pre-screening of
FGFR3 mutational status using routine histology slides of muscle-
invasive bladder cancer. Zenodohttps://doi.org/10.5281/zenodo.
13959978 (2024).
Acknowledgements
We are grateful to all patients who contributed their tissues for the
present study. The present study was funded by Owkin and partly sup-
ported by the Else Kröner-Fresenius Foundation/EKFS (2020_EKEA.129;
2023_EKES.07 to M.E.), the Clinician Scientist program of the Inter-
disciplinary Center for Clinical Research (IZKF) of the FAU to M.E., the
TOPeCS funding line of the IZKF (T04) of the FAU (to M.E.), an advanced
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 10

research grant of the IZKF of the FAU Erlangen-Nürnberg (IZKF-FAU D41
to M.E.), a Young Clinical Scientist Fellowship of the Bavarian Center for
Cancer Research (BZKF; YSF-TP01; to M.E.) and the German Cancer Aid
(DKH 70116726 to M.E. and C.M.).
Author contributions
Study conception and design: M.E., C.S., C.Maussion., and P.-A.B.; data
collection: P.M., C.Matek., N.K., J.B., R.W., D.S., B.S.-D., B.W., A.H., S.F.,
M.E.; software: P.-A.B., C.S.; analysis and interpretation of results: P.-A.B.,
C.S., M.E., M.T.; Draft manuscript preparation: P.-A.B., C.S., M.E. All
authors reviewed the results and approved theﬁnal version of the
manuscript.
Competing interests
Owkin employees own the company ’s stocks (P.-A.B., C.S., M.T., P.M.,
C.M.). B.S-D: consultant for Arquer Ltd, UK, Cepheid, CA, USA, Concile
GmbH, Germany, and Nucleix Inc., Israel. B.W.: received speaker ’s
honoraria from MSD and Janssen ‐Cilag. N.K.: Personal fees, travel
costs, and speaker’s honoraria from Astellas, Novartis, Ipsen, Photo-
cure, MSD, BicycleTX; advisory role for BicycleTX; research funding
from BicycleTX. A.H.: Honoraria for lectures for Abbvie, AstraZeneca,
Biontech, BMS, Boehringer Ingelheim, Cepheid, Diaceutics, Ipsen,
Janssen, Lilly, MSD, Nanostring, Novartis, Roche, 3DHistotech; Con-
sulting/advisory role for Abbvie, AstraZeneca, Biontech, BMS, Boeh-
ringer Ingelheim, Cepheid, Diaceutics, Gilead, Illumina, Ipsen, Janssen,
Lilly, MSD, Nanostring, Novartis, Qiagen, QUIP GmbH, Roche, 3DHis-
totech; research support from AstraZeneca, Biontech, Cepheid,
Gilead, Illumina, Janssen, Nanostring, Qiagen, QUIP GmbH, Roche.
M.E.: Personal fees, travel costs, and speaker ’s honoraria from Eisai,
MSD, AstraZeneca, Janssen-Cilag, Cepheid, Roche, Astellas, Diaceu-
tics, Owkin, BMS, BicycleTX; research funding from AstraZeneca,
Janssen-Cilag, STRATIFYER, Cepheid, Roche, Gilead, Owkin, QUIP
GmbH, BicycleTX; advisory roles for Ferring, Diaceutics, MSD, Astra-
Zeneca, Janssen-Cilag, GenomicHealth, Owkin, BMS, BicycleTX.
R.M.W. is the CEO of STRATIFYER. All other authors declare no conﬂict
of interest regarding the present work.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-024-55331-6.
Correspondenceand requests for materials should be addressed to
Pierre-Antoine Bannier or Markus Eckstein.
Peer review informationNature Communicationsthanks Bernhard Eigl
who co-reviewed with David Müller and Tapabrata Chakraborty for their
contribution to the peer review of this work. A peer review ﬁle is
available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional afﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the
Creative Commons licence, and indicate if you modiﬁed the licensed
material. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other third
party material in this article are included in the article’s Creative
Commons licence, unless indicatedotherwise in a credit line to the
material. If material is not included in the article’s Creative Commons
licence and your intended use is not permitted by statutory regulation or
exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
© The Author(s) 2024
Article https://doi.org/10.1038/s41467-024-55331-6
Nature Communications|        (2024) 15:10914 11