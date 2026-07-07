---
reference_id: DOI:10.1038/s41467-024-53163-y
title: Integrative ensemble modelling of cetuximab sensitivity in colorectal cancer patient-derived xenografts
authors:
- Umberto Perron
- Elena Grassi
- Aikaterini Chatzipli
- Marco Viviani
- Emre Karakoc
- Lucia Trastulla
- Lorenzo M. Brochier
- Claudio Isella
- Eugenia R. Zanella
- Hagen Klett
- Ivan Molineris
- Julia Schueler
- Manel Esteller
- Enzo Medico
- Nathalie Conte
- Ultan McDermott
- Livio Trusolino
- Andrea Bertotti
- Francesco Iorio
journal: Nature Communications
year: '2024'
doi: 10.1038/s41467-024-53163-y
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-024-53163-y.pdf"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1038_s41467-024-53163-y.pdf
---

# Integrative ensemble modelling of cetuximab sensitivity in colorectal cancer patient-derived xenografts
**Authors:** Umberto Perron, Elena Grassi, Aikaterini Chatzipli, Marco Viviani, Emre Karakoc, Lucia Trastulla, Lorenzo M. Brochier, Claudio Isella, Eugenia R. Zanella, Hagen Klett, Ivan Molineris, Julia Schueler, Manel Esteller, Enzo Medico, Nathalie Conte, Ultan McDermott, Livio Trusolino, Andrea Bertotti, Francesco Iorio
**Journal:** Nature Communications (2024)
**DOI:** [10.1038/s41467-024-53163-y](https://doi.org/10.1038/s41467-024-53163-y)

## Content

Article https://doi.org/10.1038/s41467-024-53163-y
Integrative ensemble modelling of
cetuximab sensitivity in colorectal cancer
patient-derived xenografts
Umberto Perron1,15,17,E l e n aG r a s s i2,3,17, Aikaterini Chatzipli4,5,17,
Marco Viviani 2,3,E m r eK a r a k o c4,L u c i aT r a s t u l l a1,6, Lorenzo M. Brochier 1,7,
Claudio Isella 2,3, Eugenia R. Zanella2, Hagen Klett8, Ivan Molineris 9,
Julia Schueler 8, Manel Esteller 10,11,12,13,E n z oM e d i c o2,3, Nathalie Conte14,
Ultan McDermott 4,16, Livio Trusolino 2,3,18 , Andrea Bertotti 2,3,18 &
Francesco Iorio 1,4,18
Patient-derived xenografts (PDXs) are tumour fragments engrafted into mice
for preclinical studies. PDXs offer clearadvantages over simpler in vitro cancer
models - such as cancer cell lines (CCLs) and organoids - in terms of structural
complexity, heterogeneity, and stromal in t e r a c t i o n s .H e r e ,w ec h a r a c t e r i s e2 3 1
colorectal cancer PDXs at the genomic, transcriptomic, and epigenetic levels,
along with their response to cetuximab, an EGFR inhibitor used clinically for
metastatic colorectal cancer. After evaluating the PDXs’quality, stability, and
molecular concordance with publicly available patient cohorts, we present
results from training, interpreting, and validating the integrative ensemble
classiﬁer CeSta. This model takes in input the PDXs’multi-omic characterisa-
tion and predicts their sensitivity to cetuximab treatment, achieving an area
under the receiver operating characteristics curve > 0.88. Our study demon-
strates that large PDX collections can be leveraged to train accurate, inter-
pretable drug sensitivity models that:(1) better capture patient-derived
therapeutic biomarkers compared to models trained on CCL data, (2) can be
robustly validated across independentPDX cohorts, and (3) could contribute
to the development of future therapeutic biomarkers.
Colorectal cancer (CRC) is a heterogeneous disease with distinctly
variable molecular features and responses to therapy. It is among the
most prevalent causes of cancer mortality worldwide, with more than
1.85 million cases and 850,000 annual deaths globally
1. Around 20% of
newly diagnosed CRC patients have metastatic disease (mCRC) at
presentation, with 25% later developing metastases
2– 4.
In recent years, several clinical trials 5– 7 have suggested that
genome-based treatment selection leads to therapeutic bene ﬁts for
patients, reduced exposure to ineffective therapies, and median sur-
vival for mCRC patients exceeding 30 months 8.S p e c iﬁcally, ~50% of
mCRC patients have KRAS-NRAS-BRAF wild-type (triple negative)
tumours and are routinely treated with cetuximab and panitumumab,
monoclonal antibody inhibitors of the epithelial growth factor recep-
tor EGFR in combination with chemotherapy as an alternative to sur-
gery. This protocol extends median survival by 2 to 4 months,
compared with chemotherapy alone
1. Unfortunately, the overall mCRC
clinical trial success rate remains low: 32% of combined phase II and III
clinical trials failed between 2013 and 2015, up from 23% in 2010
9.T h i s
highlights the need for more robustly predictive markers of drug
response for CRC patients.
Biomarkers of response to cetuximab and cetuximab plus che-
motherapy, such as the triple negative signature mentioned above,
Received: 10 January 2023
Accepted: 3 October 2024
Check for updates
A full list of af ﬁliations appears at the end of the paper. e-mail: livio.trusolino@ircc.it; andrea.bertotti@ircc.it; francesco.iorio@fht.org
Nature Communications|         (2024) 15:9139 1
1234567890():,;
1234567890():,;

have been derived from clinical and molecular analysis of patients and
patient-derived experimental models of CRC, including immortalised
cancer cell lines, organoids, and patient-derived xenografts (PDX)
2,10– 13.
However, several other systematic therapeutic biomarkers discovery
efforts conducted using in vitro models have conﬁrmed limited clinical
translatability9,14,15. This is primarily due to the intrinsic limitations of
such models, encompassing genetic, epigenetic, and transcriptomic
changes resulting from their selective adaptation to arti ﬁcial culture
conditions
16,17. Furthermore, cancer cell lines do not maintain the
complex heterogeneity of the tumour of derivation; they often lose or
gain speciﬁc subclones and might miss relevant components of the
human tumour stromal microenvironment
18,19.
Unlike cancer cell lines, PDXs have been shown to offer good
retention of tumour complexity, mimicking (at least to a certain
extent) stromal interactions. They are relatively easy to screen and
characterise. Further, histopathological characterisation has con-
ﬁrmed a high degree of concordance between PDXs and correspond-
ing parental tumours in terms of differentiation, mucus secretion, and
stromal composition, as well as maintenance of primary intratumoral
clonal heterogeneity
2,3,20– 22.
These factors have contributed to PDXs playing a pivotal role in
translational cancer research, furthering our understanding of
tumour biology and drug response mechanisms in CRC
23,24.A sa
result, extensive multi-institutional efforts (such as EuroPDX 25) are
now ongoing, aiming to establish and characterise extensive col-
lections of PDX models at the molecular and histopathological level
to ensure that they recapitulate the broadest possible diversity of
clinical cases
26.
Using data derived from the multi-omics characterisation of CRC
PDXs paired with their pharmacological/phenotypic features is a
proﬁtable strategy for training supervised machine learning models to
predict drug response in CRC patients. In this case, the extent of
training data availability is a critical determinant of the accuracy of a
model, especially when considering high-dimensional multi-omics
datasets. Machine learning models of drug response trained on large
pooled pan-cancer cell line datasets ( N = 329) outperform models
which only used cell lines ( N =2 8−68) from a speci ﬁc tissue
27.T h i s
suggests that, in some cases, data quantity can outweigh data speci-
ﬁcity. Kurilov and colleagues have also noted that predicting PDX drug
response using models trained on cell line data results in poor per-
formance across three out of four examined cohorts, except for the
erlotinib lung cancer cohort
27.
In summary, most of the pre-clinical studies of cetuximab
response in CRC cohorts performed to date have been characterised
by (1) relatively small sample sizes, (2) single platform proﬁling often
aimed at characterising the status of few known CRC driver genes, (3)
reliance on biological models which have proved to be suboptimal for
translational purposes, or a combination of these factors. These
aspects negatively inﬂuenced the studies’ability to capture the tumour
ecosystem’s complexity and inter-tumour heterogeneity’s impact on
drug response, ultimately contributing to the increasingly low success
rate of early-stage CRC clinical trials.
Here, we present one of the largest thoroughly characterised CRC
PDX collections to date ( N = 231), which closely recapitulates gold-
standard CRC patient cohorts across three ‘omics (genomics, tran-
scriptomics, and methylomics) and results from training an ensemble
classiﬁer predicting the response of these models to cetuximab
treatment, based on an integrative stacked architecture.
Our model outperforms other state-of-the-art (SOTA) predictive
methods and the biomarker of cetuximab response currently used in
the clinic, i.e., the KRAS-NRAS-BRAF mutational status, internally and
when tested on an independent cohort of CRC PDXs.
Finally, we show that our model’s predictions provide an extent of
interpretability, highlighting potential biomarkers of cetuximab
sensitivity.
Results
We selected 231 ﬁrst-pass CRC PDXs (the IRCC-PDX collection), which
were fully characterised across multiple omics (encompassing geno-
mics, transcriptomics, methylomics), clinical metadata, and were
screened with cetuximab, from a larger cohort of >600 xenografts
(Fig. 1a). These tumour models were uniquely derived from surgical
resections of CRC liver metastases performed at the Candiolo Cancer
Institute (Candiolo, Torino, IT), the Mauriziano Umberto I Hospital
(Torino, IT), the San Giovanni Battista Hospital (Torino, IT) and the
Niguarda Hospital (Milano, IT) between 2008 and 2015.
The initial ‘raw’ multi-omics characterisation of IRCC-PDX con-
sisted of the methylation status of 700,298 Illumina probes, 33,670
gene transcription levels from RNAseq, 1272 copy number (CN)
alteration and driver variant features, and 45 clinical features covering
patient demographics, primary tumour characteristics, and previous
patient treatment for a total of 735,285 features (Fig.1a). In line with the
clinical deﬁnition of ‘disease control’, which denotes clinical bene ﬁt,
we categorised as ‘responders’ those PDXs in which cetuximab
induced tumour shrinkage objective response (OR), more than 50%
tumour volume reduction compared with baseline tumour volumes or
stable disease (SD), less than 50% tumour shrinkage and less than 35%
increase in tumour volume
2.
We performed several omic-speci ﬁc feature engineering steps
(Methods, Fig. 1a) before using this data with our integrative classiﬁer
(Fig. 1a, b). These aggregated some of the dimensions of the original
‘raw’ IRCC-PDX dataset (e.g., non-negative matrix factorisation
clustering28 of methylation features), introduced feature curation via
prior knowledge of gene regulatory pathways, e.g., PROGENy 29 (11
features) and MSigDB30 gene set analysis scores (50 features), gener-
ated potentially more informative collective feature-sets, e.g.,
CELLector
31 genomic signatures (17 features), and retained 25 suf ﬁ-
ciently curated clinical features for aﬁnal total number of 113 features
across 231 PDXs (Supplementary Data 1).
Multi-omic characterisation of the IRCC-PDX collection
Previous comprehensive genetic characterisations of CRC models
have shown that the frequency of common genetic mutations
observed in PDXs is similar to that observed in primary
tumours
2,3,20,21,32,33. Targeted sequencing of 116 genes in our PDX cohort
identiﬁed 6426 driver mutations (Methods), with APC (observed in
90% of the IRCC-PDXs),TP53 (85%),KRAS (29%),PIK3CA(19%), andATM
(16%) being the most frequently affected genes (Fig. 1c and Supple-
mentary Fig. 1). In our PDX collection, mutational frequencies forKRAS
and BRAF were lower than those reported for large CRC patient
c o h o r t ss u c ha sT C G AC O A D / R E A D(https://www.cancer.gov/tcga)a n d
MSK IMPACT 34 (https://www.mskcc.org/msk-impact). KRAS’s case is
due to a pre-hoc enrichment ofKRAS wild-type models for subsequent
treatment with cetuximab (as KRAS mutant models were assumed to
be cetuximab resistant a priori). In the case of BRAF, the lower fre-
quency is ascribable to our PDXs being derived from metastatic sam-
ples. BRAF mutant tumours are frequently characterised by
microsatellite instability (MSI). Because MSI CRCs have a better prog-
nosis and rarely progress to metastasis
35, they are under-represented
in our dataset. Indeed, after removing MSI samples, the frequency of
BRAF mutated tumours in TCGA is reduced to 5.3%, which is compar-
able to that detected in our collection.
Aside from these exceptions, the mutational landscape of the
IRCC-PDXs closely matched that of the previous CRC patient cohorts
(Supplementary Fig. 2) and recapitulated known top frequently
mutated CRC driver genes
36,37.
T of u r t h e rc o n t r o lo u rP D Xm o d e l s’ ability to recapitulate char-
acteristics of their tumour sample of origin, we investigated PDX
mutational proﬁle stability for a subset of more extended PDX lineages
(i.e., those where targeted sequencing data was available beyond the
ﬁrst-passage; Supplementary Fig. 3). We observed a signi ﬁcant
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 2

agreement between all models belonging to a given lineage, regardless
of their distance from their sample of origin in terms of passages, with
few exceptions attributable to sequencing errors or clonal expansion
(Supplementary Fig. 4).
CN alterations, derived from the same 116 genes in the targeted
sequencing panel (Methods), affected some known CRC drivers,
including EGFR and SMAD4, and showed a positive correlation
(Spearman r = 0.87 and 0.93, respectively, for CN losses and gains)
with CN alteration frequencies observed in TCGA COAD/READ samples
(Supplementary Fig. 5 and Supplementary Fig. 6).
As described above, we also assessed CN pro ﬁle stability along
PDX lineages which extend beyond the ﬁrst passage. We observed
c
d
b
a
42.9
42.9
38.5
48.9
25.5
38.1
23.8
24.2
22.1
18.6
17.7
16.8
12.6
15.1
13.9
14.7
9.1
11.2
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 3

solid intra-lineage CN consistency overall (median log2R Pearson
coefﬁcient 0.927, Supplementary Fig. 7) and at the gene level (94% of
driver genes are CN-stable within lineages, Supplementary Fig. 8), in
line with previous reports
38.
We characterised our PDX collection’s transcriptional landscape
using two approaches to classify samples into subtypes: CMS39,40 and
CRIS4. Results from these analyses were broadly consistent with TCGA
COAD/READ and other CRC datasets where expression data is available
(Fig. 1d and Supplementary Fig. 9).
To concisely represent our PDXs ’ epigenomics pro ﬁles, we
grouped samples into ﬁve clusters obtained through non-negative
matrix factorisation
28 (Methods). We observed that the samples
belonging to one of these groups (cluster 1) were remarkably more
hypermethylated over all measured CpG islands (median beta
methylation level = 0.81, Kruskal-Wallis test, chi-squared = 289.47,
df = 4, p value < 2.2 × 10
−16, effect size = 0.59, Supplementary Fig. 10).
Consistent with our cluster de ﬁnition, we also found cluster 1 to be
highly enriched for the CpG island methylator phenotype (CIMP41)i n
130 out of 146 PDXs (Supplementary Fig. 10). This heterogeneity of
PDX methylation pro ﬁles resembled that observed in CRC patients,
even though the percentage of IRCC-PDX samples classi ﬁed as CIMP
was slightly lower than that reported in TCGA COAD/READ (44% vs
58%, Supplementary Fig. 11). This is expected considering the low
prevalence of MSI tumours — which are typically enriched for CIMP
cases— within metastatic CRC cohorts such as ours
34.
Overall, our multi-omic overview of the PDX collection indicates
that IRCC-PDX closely recapitulates the genomics, transcriptomics,
and methylomics landscape of gold-standard human CRC cohorts,
such as TCGA COAD/READ and MSK-IMPACT.
Exploratory single-omic analysis of the IRCC-PDX collection
To further investigate the molecular proﬁles of the PDXs in an unsu-
pervised manner we conducted UMAP dimensionality reduction 42
across individual omics and a density-based cluster analysis (via
HDBSCAN)
43. This was followed by an enrichment analysis of covari-
ates in the resulting clusters, as well as of differential drug response
across them (Methods) to identify, respectively, speci ﬁcm o l e c u l a r
features and drug responses that discriminate between different sub-
groups (Supplementary Data 2).
By applying this approach to IRCC-PDX binary gene mutation
features, we identify two clusters (Supplementary Fig. 12). The ﬁrst
cluster (id = 0) was almost entirely made up of TP53 mutated (95%),
and KRAS and PIK3CA wild-type PDXs (96% and 89%). The majority of
models in this cluster belonged to CRIS type C (51%, chi-square statistic
(chi2) = 8.53, chi-square adjustedp value (cap) = 0.15) and were sensi-
tive to cetuximab treatment (SD, OR, 65%, chi2 = 10.34, cap = 0.06).
Almost all PDXs in the second cluster (id = 1) were also TP53 mutant
(67%) but also KRAS mutant, differently from cluster 0 (98%, chi2 =
122.43, cap = 2.85 × 10
−26). This cluster was also enriched for CRIS type
A( 4 3 % ,c h i 2=2 6 . 0 6 ,c a p=1 . 4 9×1 0−5)a n dn o n - r e s p o n d e r( P D )m o d e l s
(75%, chi2 = 11.66, cap = 0.03) (Supplementary Data 2).
When applied to binary CNV features, the same approach
identiﬁed four clusters (Supplementary Fig. 13 and Supplementary
Data 2). One cluster (id = 3) exhibited a high CNV burden and CN gain
count, with 19 out of 21 associated CNV (at a cap <0.1) being a CN
gain and present in 82% of the samples, among which top signi ﬁcant
genes are NFX1, ESRRA and MARK2. Moreover, this cluster was pre-
dominantly composed of strong cetuximab responders (OR: 44%,
chi2 = 10.17, cap = 0.1). Another cluster (id = 0) displayed instead a
low count of CN events, and it was composed mainly of CRIS type A
PDXs (67%, chi2 = 29.93, cap = 7.49 × 10
−5). Finally, cluster 2 was
characterised by losses in FGD5, RAF1, XPC and SATB1 genes (all
present in 79% of the samples, at a cap <0.1), while cluster 1 showed
mild enrichment of losses in BCL2, SMAD4 and MALT1 (30%, at a chi-
square p Value < 0.01).
In addition, we identi ﬁed 3 UMAP/HDBSCAN clusters from con-
tinuous gene-level RNAseq features (Supplementary Fig. 14). Among
these, one cluster (id = 1) was almost exclusively composed of cetux-
imab non-responders (PD, 88%, chi2 = 8.99, chi-squarep value = 0.002,
cap = 0.16), as well as it was enriched for hypermethylated (NMF
cluster 1, 76%, chi2 = 50.91, cap = 5.81 × 10
−11)a n dC R I St y p eAP D X s
(96%, chi2 = 89.22, cap = 2.11 ×10−19). Finally, we projected the methy-
lation NMF cluster labels (Methods) onto 2D UMAP embeddings
computed from probe-level methylation features and analysed their
distribution across 5 obtained clusters (Supplementary Fig. 15). The
ﬁrst one (id = 0, exactly matching NMF cluster 1, chi2 = 189,
cap = 3.94 × 10
−41) was the most hypermethylated overall and largely
made up of cetuximab non-responders (83%, chi2 = 12.49, cap = 0.03).
Another one (id = 3, mostly matching NMF cluster 4, 96%, chi2 = 154.43,
cap = 1.4 ×10 −33) was enriched for CRIS type C (72%, chi2 = 22.87,
cap = 0.0001) and OR PDXs (32%, chi2 = 22.41, cap = 0.0001).
Conﬁrmation of established biomarkers of cetuximab
sensitivity
Around half of the tumours in mCRC patients are wild-type for the
KRAS-NRAS-BRAF genes (triple negative). These patients routinely
receive anti-EGFR treatment with cetuximab or panitumumab in
combination with chemotherapy as an alternative to surgery resulting
in a median survival extension of 2 to 4 months, compared with che-
motherapy alone
1. Retrospective analysis of triple-negative CRC
patients from the CRYSTAL and FIRE3 trials has also highlighted that
patients with left-sided tumours treated with anti-EGFR antibodies had
better survival and treatment response than patients with right-sided
tumours
44.
Fig. 1 | Multi-omic Overview of the Colorectal Cancer PDX Cohort and Cetux-
imab Response Modelling Approach. a The left panel presents the IRCC patient
derive xenografs (PDX) collection, from 231 unique colorectal cancer (CRC) liver
metastasis (LMX) resections. This collection was characterised at a multi-omic level
and assessed for cetuximab response. A schematic of the omic-speciﬁc feature
engineering is also provided. The right panel outlines the CeSta classiﬁer pipeline.
Input features selected from the training set (Methods) using univariate tests
(Fisher’s exact, Mann-Withney U-test) and multivariate linear models feed into
three independent level 1 classiﬁer pipelines: forward feature selection plus elastic
net, ANOVA feature selection plus extra trees, and ANOVA feature selection plus
support vector classiﬁers. A fourth classiﬁer, a catBoost model, is pre-trained on
pan-cancer data from the Cell Model Passport repository and ﬁne-tuned using
IRCC-PDX data. The predictions from these level 1 classiﬁers are stacked and
inputted into a meta-classiﬁer, which produces the ﬁnal binary classiﬁcation
(cetuximab-responder/non-responder) using argmax-based soft voting.b CeSta
nested cross-validation approach: 50 train/test splits are generated via stratiﬁed
sampling of the IRCC-PDX collection. CeSta is trained and tuned independently
across these 50 splits. In each iteration, the training set is divided into three folds.
Two folds are used in three rounds as the ‘training fold’, while the remaining fold
serves as the ‘validation fold’. Predictions from level-1 classiﬁers for the validation
fold are stacked and input into the meta-classiﬁer. After validation, ﬁrst-level clas-
siﬁers are ﬁtted to the entire training set, and CeSta’s performance is evaluated on
the test set (pink rectangle, N = 81). CeSta is then trained on the entire IRCC-PDx
dataset and tested on an independent CR-PDX dataset (grey rectangle,N = 50) for
external validation.c Top frequently mutated genes in the IRCC-PDX cohort.
d Selection of multi-omic and clinical features across the IRCC-PDX collection,
including CRIS expression cluster labels, methylation NMF cluster labels, primary
sample anatomical location, and treatment backbone. Source data are provided as
a Source Data ﬁle. Fig. 1AB has been Created in BioRender [Iorio, F. (2024) BioR-
ender.com/q01w468] and released under a Creative Commons Attribution-
NonCommercial-NoDerivs 4.0 International license (https://creativecommons.org/
licenses/by-nc-nd/4.0/deed.en).
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 4

Treatment intervention in our PDXs (Methods) closely matched
that of cetuximab human trials such as PEAK 7,45 and FIRE35 as well as
current clinical best practices46,47.
Across our IRCC-PDX collection ( N = 231), KRAS mutations were
much more frequently observed in PDXs with a cetuximab non-
responder phenotype (Fisher’se x a c tt e s t’s odds ratio (FETo) = 0.12, p
value (FETp) = 1.2 × 10
−10, 95% conﬁdence interval (FETci) = [0.06,0.26],
standardised residuals (FETsres) = 6.37) Fig. 2a and (Supplementary
Data 1). NRAS (FETo = 0.06, FETp = 8.49 × 10 −4,F E T c i = [ 0 . 0 0 2 , 0 . 4 7 ] ,
FETsres = 3.35) and BRAF (FETo = 0.27, FETp = 0.035, FETci =
[0.06,0.95], FETsres = 2.31) mutations were noticeably more likely to
occur in non-responder PDXs, though only 13 and 16 mutant PDXs
were observed across IRCC-PDXs, respectively. However, overall
mutational and CN alteration burden, deﬁned as the total number of
e v e n t sp e rP D Xa n di n t e n d e da sc o a r s e - g r a i n e dp r o x i e sf o rt u m o u r
progression and genomic stability, did not appear to correlate with
cetuximab sensitivity (Fig.2b, c and Supplementary Data 1).
Finally, a right-sided localisation of the original tumour showed a
moderate association with a non-responder phenotype (FETo = 0.42,
FETp = 0.01, FETci = [0.20,0.84], FETsres = 2.66).
As previously mentioned, the KRAS-NRAS-BRAF triple negative
signature is widely recognised as the best-established biomarker of
cetuximab sensitivity. This association is being used both as a clinical
discriminant for treatment and as an entry criterion for anti-EGFR
trials, and it is clearly visible in our IRCC-PDX collection (FETo = 11.38,
FETp = 4.91 × 10
−16, FETci = [5.80,23.40], FETsres = 7.99). These obser-
vations thus indicate that our IRCC-PDX collection recapitulates the
best available marker of cetuximab sensitivity in patients.
To further explore how molecular characteristics of the IRCC-
PDXs distribute with respect to t heir response to cetuximab, we
performed a differential expression analysis, comparing cetuximab
responder versus non-responder PDXs. This yielded 230 upregulated
and 1534 downregulated genes (at a negative binomial generalised lin-
ear model adjustedp value < 0.05 and | log fold change (logFC) | > 0.58,
Supplementary Data 3). A functional enrichment analysis via preranked
GSEA using the Hallmark gene-signature collections from the Molecular
Signature Database (MsigDB)
48, unveiled, as expected, many sig-
niﬁcantly down-regulated gene sets (Supplementary Data 3). Among
these, HALLMARK_EPITHELIAL_ MESENCHYMAL_TRANSITION and
HALLMARK_INFLAMMATORY_RESPONSE were the most signi ﬁcantly
enriched (NES = −1.92 and −1.82, respectively, with an adjusted p
value = 0.001 for both, Supplementary Data 4 and Supplemen-
tary Fig. 16).
A single sample GSEA extended to Reactome pathways
49 con-
ﬁrmed Inﬂammatory processes as among those upregulated in non-
responder samples (positive scorein 63 out of 121 non-responder PDXs
for REACTOME_INTERFERON_GAMMA_SIGNALING, Supplementary
Data 5 and Supplementary Fig. 17). The other consistent signal for
upregulated genes in resistant PDXs (positive score in 77 out of 121 non
responder PDXs for REACTOME_KERATINIZATION) was related to
keratinisation, which has been previously found associated with a set
of more aggressive tumours in this same cohort
50. The only Reactome
pathway signiﬁcantly upregulated in cetuximab responder PDXs was,
unsurprisingly, REACTOME_SIGNALING_BY_EGFR_IN_CANCER (posi-
tive score in 42 out of 121 non-responder PDXs).
Consistently, a transcription factor binding site enrichment ana-
lyses yielded signi ﬁcant results only for promoters of the genes
downregulated in cetuximab-sensitive PDXs, and involved transcrip-
tion factors with known roles in in ﬂammation, such as STAT1/2 and
KLF15 (Supplementary Fig. 18).
Fig. 2 | Overview of cetuximab response and biomarker candidates. aMutation
patterns of CRC driver genes and mutational signature features among those with
the most signiﬁcant impact on CeSta predictions (Fig. 4a) b cetuximab non-
responders (‘PD’, volume growth > 35%, in orange) and responders (‘SD-OR’,
volume growth ≤35%, in blue). c Selection of continuous features which best dif-
ferentiate between PD and SD-OR PDX models. Source data are provided as a
Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 5

A stacked classiﬁer modelling cetuximab sensitivity
Results from the single-omic and differential analyses highlighted the
need for a more elaborate integrative modelling approach. To predict
whether a CRC PDX responds to cetuximab treatment in terms of
tumour volume shrinkage
2, we considered its multi-omic character-
isation and reduced the task to a binary classi ﬁcation problem. We
selected and integrated multi-omic features into a stacked classi ﬁer
pipeline51: the cetuximab Stacked classiﬁer (CeSta, Fig.1a). Stacking is a
supervised ensemble learning technique which combines multiple
weak classi ﬁcation models (level 1 classi ﬁers, lvl1) using a meta-
classiﬁer. This architecture improves upon individual classi ﬁers’ per-
formance. It is well suited for a classiﬁcation task such as ours, which is
based on tabular data with relatively few examples (231) and a much
larger number of features (35,053, Supplementary Data 1): a scenario
where more complex models and deep neural networks fare poorly
52,53.
A similar architecture has been successfully used to predict drug
response in breast cancer patients from the multi-omic characterisa-
tion of their tumours
54.
Our CeSta pipeline implements a late integration approach to
prevent high-dimensional‘omics (transcriptomics, methylomics) from
overwhelming those with fewer features (typically genomics) by
dominating the feature selection phase (Fig. 1a). We used a nested
cross-validation approach for model tuning, training, and validation,
based on generating 50 train/test split replicates of our IRCC-PDX
dataset (with 150 and 81 PDXs, respectively, for the training set and test
set) assembled via strati ﬁed sampling (Fig. 1b). On each of these 50
training sets, our classiﬁer pipeline performed a custom single omic
feature selection step which reduced the initial input of 113 engineered
and clinical features plus 34,940 raw transcriptomics and genomics
features (Fig. 1a and Supplementary Data 1) to a smaller subset, with
the size of the latter being amongst the hyperparameters tuned inde-
pendently, across data splits (Fig. 1a and Supplementary Fig. 19,
Methods). We used these pre-selected IRCC-PDX features as the input
to 4 different lvl1 classiﬁer pipelines: (1) model-based forward feature
selection, followed by elastic net logistic regression, (2) ANOVA-based
feature selection, followed by either support vector classiﬁer (SVC) or
(3) extraTrees classiﬁers, and (4) a catBoost classiﬁer pre-trained on a
set of 55 multi-omic features from a collection of 860 pan-cancer cell
lines from the Cell Model Passports (panCMP
55), then re ﬁned on the
same set of 55 features from the IRCC-PDX (continual learning,
Methods). The lvl1 predicted probabilities were then stacked and
combined using a soft voting classiﬁer which outputs a binary classi-
ﬁcation of cetuximab sensitivity (Fig.1a, b, Methods).
Candidate biomarkers of cetuximab sensitivity
Our CeSta pipeline selects the most informative biomarkers of
cetuximab sensitivity across training examples sampled from the
IRCC-PDX collection by combining univariate statistical tests (Fish-
er’s exact, Mann-Whitney U test), percent lift, and logit (statsmodels
v0.13.2 logit
56) models (Fig. 1a, b and Supplementary Data 6, and
Methods). Here and in Fig. 2a, we provide an overview of some of
CeSta’s top features (i.e., as ranked by their impact on CeSta ’s pre-
dictions) and their relationship with cetuximab sensitivity. The latter
represents our binary target variable, with ‘responder’PDXs deﬁned
as those that grew in volume by 35% or less at three weeks after
treatment (a proxy of disease control, as mentioned above) (Fig. 2b,
Methods).
Among the considered genomics features, beyond the KRAS-
NRAS-BRAF triple negative signature, CLSPN (percent lift: −0.675),
PTEN (percent lift:−0.594), andPIK3CA(percent lift:−0.654) mutations
were also more frequently observed in non-responder PDXs. Addi-
tionally, a few other driver gene mutations (e.g., EGFR (percent lift:
−0.721) and MET (percent lift:−0.702)) were noticeably more likely to
occur in non-responder PDXs, although they were rare overall (21 and 8
observations in IRCC-PDX, respectively). Only mutations inKRAS (logit
p-value (logit p)=0 . 0 0 2 ) , B R A F ( l o g i tp = 0.037), PTEN (logit
p = 0.049), and NRAS (logitp =0 . 0 3 )w e r ef o u n dt ob ea s s o c i a t e dw i t h
cetuximab resistance via single-omic multivariate logit regression. Our
CeSta approach combines these metrics (univariate and multivariatep
values, percent lift) into an aggregated feature selection score (Meth-
ods) which allows us to detect both well-supported and rare candidate
markers. CELLector subgroups 7 (APC, TP53, KRAS, PIK3CA mutated),
16 ( TP53 wild-type; APC, KRAS, PIK3CA mutated), and 5 ( APC, TP53,
KRAS mutated; PIK3CA wild-type) were signiﬁcantly associated with a
non-responder phenotype (FETo = 13.46, 9.51, 4.12, FETp = 0.002,
0.014, 0.001, FETci = [1.89,587.67], [1.24,427.84], [1.61,11.98],
FETsres = 3.17, 2.55, respectively).
In contrast, subgroup 12 (APC, TCF7L2,a n d TP53 mutated; KRAS,
BRCA2
, ATM, TPTE, EP400 wild-type) was more likely to contain
responder PDXs (FETo = 9.57, FETp = 0.011, FETci = [1.32, 421.45],
FETsres = 2.59). However, this is a rare occurence, with only 8 PDXs
presenting this signature across IRCC-PDX. Subgroups 7,16 and 5 were
also signi ﬁcantly associated with cetuximab resistance after multi-
variate logit regression (logit p =2×1 0
−6,3 × 1 0 −6 and 3 × 10 −4,
respectively).
Finally, FGFR1 CN gains (FETo = 3.19, FETp = 5.98 × 10 −5, FETci =
[1.74, 5.98], FETsres = 4.04) were more frequently observed in
responder PDXs. AlthoughERBB2 and MET ampliﬁcation events (i.e., >2
copies gained) were rare (5 and 3 examples in IRCC-PDX, respectively),
they were more frequent in non-responders (percent lift:−1 for both).
These genomic signatures agree with previous surveys of CRC poor-
prognosis driver alterations
36,57, suggesting at least a partial overlap
between markers of CRC progression and those of cetuximab resis-
tance in PDX.
As transcriptomics features (Fig. 2c), while EGFR (Mann-Whitney
U-test pv a l u e(MWU p) = 4) and EGF (MWU p = 17) were not differen-
tially expressed in cetuximab responders versus non-responders PDXs,
REG4 (MWU p =0 . 0 0 1 ) a n dEREG (MWU p =7×1 0
−5)w e r ei n s t e a ds i g -
niﬁcantly upregulated in resistant and sensitive cases, respectively.
REG4 (Regenerating Islet-Derived Protein 4) is a C-type lectin-like
mitogenic protein known to stimulate EGFR signalling and promote
migration and invasion in CRC
58.H i g hREG4 expression is associated
with poor prognosis and low recurrence-free survival in CRC patients59
and, more speciﬁcally, with cetuximab resistance12 in CRC organoids
and PDX models. A suggested mechanistic explanation points to FZD
and LRP5/6, both upstream components of the Wnt/ β-catenin path-
way, which are involved in the REG4-mediated promotion of stemness
induced by KRAS mutation in CRC with APC loss
60. EREG (epiregulin) is
a member of the EGF family and an EGFR ligand; it is thus involved in
inﬂammation, cell proliferation, and cancer progression.EREG activity
has been associated with cetuximab sensitivity in preclinical models
and patients
61,62, and it has been suggested that, in an in ﬂammatory
environment, EREG can promote stemness and cancer cell prolifera-
tion by stimulating ERK signalling throughEGFR activation in a variety
of cancer types63– 65.
We also observed high PROGENy 29 EGFR pathway expression
scores associated with a non-responder phenotype (MWU p = 0.002,
percent lift:−1.879), whereas, as mentioned above, EGFR expression as
an individual feature was not. We observed a similar pattern for KRAS:
It was not differentially expressed across responders versus non-
responders PDXs (MWU p = 0.23) but high MSigDB
48,66 HALLMARK_K-
RAS_SIGNALING_UP gene set ssGSEA scores were associated with non-
responder PDXs (MWU p = 0.001, percent lift: −10.688). These obser-
vations suggest that engineering aggregated expression features using
ssGSEA and PROGENy scores might be more informative than indivi-
dual gene expression features for cetuximab sensitivity prediction.
However, it is also important to note that feature aggregation might
introduce additional complexity. PROGENy signals for EGFR could be
partly driven by downstream ERK-mediated signals, which are hard to
disentangle from KRAS-triggered inputs. This may explain why both
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 6

EGFR and KRAS signatures are associated with resistance to EGFR
blockage.
Finally, we observed that higher MSigDB gene set ssGSEA scores
for angiogenesis (percent lift:−2.168), inﬂammatory response (percent
lift: −3.7), UV and DNA damage response (percent lift: −6.63), and
Hedgehog (Hh) signalling (percent lift:−5.44), were all associated with
non-responder PDXs (MWUp ≪ 0.01 for all). The Hh hallmark score is
fascinating as it might corroborate the evidence that Hh pathway
activity correlates with reduced response to cetuximab
67.
When considering methylation features (Fig. 2c), NMF cluster 1,
the most hypermethylated, was enriched for non-responders and MSI-
like PDXs (FETp = 2 × 10
−4, percent lift: −0.796). Cluster 4, the second-
most hypo methylated, was enriched for responder PDXs
(FETp = 3 × 10
−4, percent lift: 2.299).
Across all omics, both categorical (Fig. 2a) and continuous fea-
tures (Fig. 2b) were either too sparse or too noisy to be adequate
predictors of cetuximab response when considered individually. This
highlights the effectiveness of an integrative model which combines
the most informative features across‘omic boundaries.
Validation of the CeSta classiﬁer
We set out to internally assess CeSta’s performance on our IRCC-PDX
collection using a holdout shuf ﬂe approach, followed by testing the
null hypothesis that results generated by different classi ﬁers are
equivalent68.
We started by generating 50 train/test set split (150 and 81
PDXs, respectively) replicates from our IRCC-PDX dataset. We used a
nested cross-validation approach to tune and train 50 independent
CeSta replicates (Fig. 1b, ‘internal validation’). To provide a realistic
and stringent benchmark, we evaluated many baseline cetuximab
sensitivity classi ﬁers of varying complexity (Fig. 3a, b and Supple-
mentary Fig. 20). Here, we present results from a performance
comparison of our CeSta classi ﬁer against three of the best-
performing baseline classi ﬁers. These build on the SOTA clinical
predictor of cetuximab sensitivity: the KRAS-NRAS-BRAF triple
negative marker
46,47 and whether the original tumour is located in
the left portion of the patient ’s colon 44. These features were com-
bined into a cetuximab sensitivity classi ﬁer using either (1) a rule-
based approach entirely analogous to the clinical criterion for
cetuximab treatment (i.e., PDXs with the triple negative marker were
predicted as responders to cetuximab, Fig. 3a, ‘tripleNegRule’ and
‘tripleNegRightRule’) or (2) an elastic net penalised logistic regres-
sion model (Fig. 3a, elNet baseline’) taking in input the four features
above as possible regressors (Methods). As for CeSta, we tuned and
trained 50 independent replicates of this latter baseline classi ﬁer
over the 50 split replicates we previously generated.
CeSta outperformed all baseline models (mean F1: 0.941, Mann-
Whitney post-hoc testp value: «0.001) on this internal validation setup
(Fig. 3). Interestingly, the elNet baseline performance, measured via F1
score (i.e., the harmonic mean of precision and recall), fully matched
the triple negative rule-based classiﬁer, indicating that the elNet model
can recapitulate the clinical decision criterion. Figure 3bs h o w st h a t
CeSta outperforms this same elNet baseline classi ﬁer for the vast
majority of replicate splits (mean AUROC = 0.821 versus 0.780, Mann-
Whitney post-hoc test p value: «0.001), with an average of 0.04
increase in ROC AUC, computed using the ROC AUC variance formula
ﬁrst proposed by Delong and colleagues
69– 71.
Based on our ﬁnding, we evaluated whether our CeSta classi ﬁer
would outperform the clinical SOTA baseline classi ﬁer on an inde-
pendent cohort of CRC PDX models (Fig.1b, ‘external validation’). This
external validation cohort (from now on CR-PDX), consisting of 50
CRC xenografts, was collected and characterised at the genomic,
transcriptomic and clinical levels at Charles River Discovery Research
Services and included samples from European patients (Supplemen-
tary Data 7, Methods).
We tuned and trained a single instance of our CeSta pipeline as
well as a single instance of the baseline model over the entire IRCC-
PDX collection ( N = 231). We then compared their predictive per-
formance on the never-before-seen CR-PDX set ( N = 50) using the
same set of multi-omic engineered features we described previously
for IRCC-PDX (Supplementary Data 7, Methods). Similar to what we
observed in the internal validation phase, our CeSta classi ﬁer out-
performed the clinical baseline classi ﬁer (AUROC = 0.88 and 0.78,
respectively), with an improvement of 0.1 ROC AUC (Fig. 3ca n d
Supplementary Data 8). More speci ﬁcally, our CeSta pipeline cor-
rectly predicted three additional KRAS-NRAS-BRAF triple-negative
PDXs as cetuximab non-responders and one additional non-triple-
negative as a responder; on top of matching biomarkers correctly
predicted by the baseline classi ﬁer (Fig. 3d, e and Supplementary
Data 8). The three triple-negative non-responders (relative tumour
volumes at 3 weeks: 125%, 485% and 1380%) have a lower than
average (VST 7.4 vs 9.9) EREG one and higher than average (VST 13.9
vs 9.4) REG4 expression, highlighting how the transcriptional fea-
tures identi ﬁed by CeSta help its correct predictions, despite the
genetic features, for those samples. Interestingly they are two CRIS-
A and one CRIS-B, subtypes generally refractory to anti-EGFR ther-
apy. The non triple-negative sample has a canonical BRAF mutation
(V600E) that usually determines resistance to cetuximab, but CeSta
correctly identiﬁed it as a responder (−18.4% relative tumour volume
at 3 weeks), in this case the relevant feature that steered its pre-
diction in the right direction most probably is the FGFR1 ampliﬁca-
tion (log2 0.18).
Further external validations of CeSta on patients ’ data are cur-
rently unfeasible, due to the lack of datasets from the characterisation
of cohorts that are unselected forKRAS mutational status, treated with
cetuximab monotherapy and with multi-omics data available. How-
ever, we tested whether any of the predictive transcriptional features
identiﬁed by CeSta differentiate between cetuximab responder and
non-responder patients. This analysis was conducted using gene
expression data obtained from a limited single-omic CRC patient
dataset, accompanied by cetuximab response data and encompassing
43 non-responder patients and 25 responders patients
62. When com-
paring ssGSEA scores (Supplementary Data 4) computed across the
two groups for the three Hallmark pathways identiﬁed as predictive by
CeSta and with the highest percent-lift (as previously discussed), the
one related to in ﬂammatory processes showed a statistically sig-
niﬁcant difference (Wilcoxon test p value = 0.02, Supplementary
Fig. 21). While these results con ﬁrm the association between higher
inﬂammation marker expression and lack of sensitivity to cetuximab in
patients, a larger, multimodal dataset would be ideal for performing a
more rigorous validation of the CeSta predictive features in human
patients in the future.
Explanation of the CeSta classiﬁer
Post hoc explanations approximate the behaviour of a classi ﬁer by
modelling relationships between feature values and the classi ﬁer’s
predictions. Here, we relied on SHapley Additive exPlanations (SHAP72)
to de ﬁne local feature importance and their impact on the CeSta
classiﬁer’s predictions. SHAP is a game theoretic approach through
which values representing a feature’s average marginal contributions
over all possible feature coalitions are computed.
Our CeSta classi ﬁer leverages additional informative genomic
(e.g., FGFR1 ampliﬁcation) and transcriptomics (e.g., EREG and REG4
expression; angiogenesis, in ﬂammation, and Hh signalling ssGSEA
scores) features (Fig. 4a) to improve upon the clinical baseline classi-
ﬁer (Fig. 3b,c) while retaining the latter ’s top predictive features,
namely the KRAS-NRAS-BRAF signature. As shown in the CeSta SHAP
waterfall plot in Fig. 4b, we observed high Hh signalling, high angio-
genesis ssGSEA scores, and the KRAS, APC, TP53 mutation signatures
being predictive of cetuximab resistance. In the same panel, highEREG
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 7

expression and, more noisily, low REG4 expression and FGFR1 ampli-
ﬁcation appeared to in ﬂuence the model towards a ‘responsive’ pre-
diction. Further, stacking our four lvl1 classi ﬁers resulted in a slight
performance increase over the best-performing lvl 1 classiﬁer (i.e., the
ANOVA SVC pipeline) taken on its own, albeit with substantial AUROC
conﬁdence interval overlap (Fig. 4e).
To further characterise the outstanding CeSta features, we con-
sidered the 275 genes from the engineered transcriptomic features
with the highest SHAP values and characterised their coded proteins in
terms of physical interaction. To this aim, we performed a protein-
protein interaction network analysis, through String-db
73, observing a
larger number of interactions than expected by chance (135 vs 23, p
Fig. 3 | CeSta outperforms the state-of-the-art baseline classiﬁer on IRCC-PDX
and CR-PDX. aClassiﬁcation performances quantiﬁed through F1 scores (harmonic
mean of precision and recall) across 50 train/test IRCC-PDX split replicates (x-axis)
for the stacked classiﬁer (‘CeSta’, in blue), an elastic net penalised logistic model
(‘elNet baseline’, in tan) which uses state-of-the-art clinical features for cetuximab
sensitivity in CRC (KRAS, NRAS, BRAF mutational status, right colon tumour loca-
tion), a rule-based classiﬁer using the KRAS-BRAF-NRAS triple negative clinical
signature (tripleNegRule, in orange) as a binary predictor, and another rule-based
classiﬁer which uses both the aforementioned triple-negative signature and the
‘right colon’feature (tripleNegRightRule, in green).b Area under the receiver-
operating-characteristic curve (AUROC) values and error bars, obtained via
DeLong’s method, indicating 95% conﬁdence intervals
69,70 across 50 IRCC-PDX of
n = 150 and 81 train/test split replicates replicates (x-axis), for CeSta (in blue) and
the elastic net penalised logistic model (‘elNet baseline’, in tan) described in (a).
c AUROC (DeLong’s method) computed over the external validation CR-PDX
dataset for CeSta (in blue) and the elNet baseline classiﬁer (‘elNet baseline’, in tan)
after a single instance of both models is trained and tuned over the entire IRCC-PDX
dataset. The shaded area between the CeSta and elNet baseline ROC curves
represents the improvement in AUROC. Decision point coordinates correspond to
the false-positive and true positive rates obtained from the corresponding classi-
ﬁer’s predictions. Here, rule-based classiﬁer decision points overlap with the elNet
baseline’s. d Confusion matrix from a comparison of CeSta classiﬁer outcomes
(same validation setup asc) and PDXs actual cetuximab response over the external
validation CR-PDX dataset. Correct predictions are on the diagonal highlighted in
blue, incorrect predictions off the diagonal are highlighted in purple.e CeSta
correct prediction counts (same validation setup asc) over the CR-PDX external
validation set grouped by PDX cetuximab sensitivity (x-axis) and PDX KRAS-NRAS-
BRAF triple-negative status (y-axis). CeSta correctly predicts additional triple-
negative non-responders (3) and triple-positive responders (1), which all baseline
classiﬁers miss. Source data are provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 8

value < 10−16) and conﬁrmed the relevance of subnetworks involved in
the transcriptional control (RELA, NFKB1-2, IRF1) and execution
(CXCL9-11-10 chemokines) of the in ﬂammatory response (Supple-
mentary Fig. S22). This analysis also underscored interactions invol-
ving the MAPK pathway (i.e., between RAF1 and NRAS), transcriptional
regulators of WNT signalling (TCF7L2 and TLE1/3) and adhesion-
dependent growth control (L1CAM, and FGFR1).
We also detected very low collinearity among the top CeSta fea-
tures’values, with the largest anticorrelation between the Hh signalling
ssGSEA score and EREG expression (Pearson ’s r = −0.2). In contrast,
high EREG expression was associated with both increased angiogen-
esis (Pearson ’s r = 0.4) and high in ﬂammatory response (Pearson ’s
r = 0.3) ssGSEA scores (Supplementary Fig. S23).
Comparison of cetuximab response in cell lines and PDX models
PDX models are thought to recapitulate inter and intra-tumour het-
erogeneity observed in patients more faithfully than immortalised cell
lines. They provide at least some stromal microenvironment interac-
tions and are more likely to follow pathways of drug sensitivity or
resistance found in primary human tumours
74. However, 2d cell line
Fig. 4 | CeSta leverages informative features and combines weaker classiﬁers.
a Feature importance as determined by CeSta, represented by the mean absolute
SHAP value (x-axis) for the top signiﬁcant features (y-axis). b Top signiﬁcant fea-
tures’impact on CeSta output using SHAP values (x-axis) across all 50 PDXs in the
CR-PDX validation set (scatter dots). The most important features in (a)h a v et h e
greatest impact on model outcomes, with a clear separation between positive and
negative effects. c Performance of CeSta’s top features on IRCC PDXs and the
external cohort. The relationship between a feature’s SHAP values and cetuximab
sensitivity on the train set (full IRCC PDX set, x-axis) and test set (CR PDX set), after
removing other features’effects (partial correlation, parSHAP). Dot size and colour
indicate a feature’s mean absolute SHAP value on the training set. Dots closer to the
diagonal indicate consistent performance across train and test sets. Key features
like KRAS mutation and EREG expression align closely with the diagonal, indicating
ag o o dﬁto rs l i g h tu n d e rﬁtting. d Underperformance of CMP-trained features on
the external cohort. The relationship between CatBoostCMP feature SHAP values
and cetuximab sensitivity on the train (panCMP set) and test (CR-PDX) sets, after
removing other features’effects. Dot size and colour represent a feature’si m p a c t
on model prediction. Many top features of this model fall in the lower right
quadrant, indicating overﬁtting. e AUROC conﬁdence intervals (CI, 95%) for CeSta
(blue), three level 1 classiﬁers (orange), the catBoost model trained on the panCMP
dataset (green), and the same catBoost model retrained on the IRCC-PDX dataset.
CeSta shows a slight performance improvement over the best level 1 classiﬁer, with
overlapping CIs. The cell-line-trained CatBoost classiﬁer poorly predicts cetuximab
sensitivity in PDXs, but retraining improves its performance. Source data are pro-
vided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 9

models are undeniably cheaper as well as simpler to screen and char-
acterise, an advantage that has enabled the generation of large multi-
omics cell line datasets
55,75,76 and aided systematic drug and functional
genetic screening efforts14,75.
Several methods have been proposed to align gene-expression
and other omics datasets from different model collections and
patients. These methods include anchoring on common genes
77 or
employing batch correction methods originally developed for single-
cell data, thus harmonising all the features into a shared space across
datasets/model-collections (such asCelligner
78). To avoid information
leakage we opted instead for a supervised continual learning
approach.
Particularly, we investigated whether a cetuximab sensitivity
classiﬁer trained (1) on a large pan-cancer multi-omic dataset (panCMP,
N = 860) of 2d cell line models derived from the CMP dataset
55,o r( 2 )
on a small CRC-speci ﬁc subset of the same panCMP cell-line dataset
(CRC-CMP, N = 44) would compare favourably against (1) the classiﬁer
itself, retrained on the IRCC-PDX dataset (N = 231) or (2) the classiﬁer
itself, retrained on a randomly selected subsample of IRCC-PDX, with
the same size as the colorectal 2d cell-line dataset (subIRCC-
PDX, N = 44).
We observed that a panCMP-trained boosting classiﬁer catBoost
79
performed very poorly in predicting PDX sensitivity to cetuximab
(Fig. 4). This poor performance persisted even when considering the
inclusion of the cell line tissue of origin as a categorical covariate
(Fig. S24). When this catBoost model was further trained on the IRCC-
PDX dataset (continual learning, Methods), its performance on the CR-
PDX validation set became comparable to that of the other IRCC-PDX
trained lvl1 classiﬁers. We observed a similar result when we traded
several examples for tissue speci ﬁcity in the cell-line dataset and
compared a CRC-CMP-trained classiﬁer against itself after retraining
on subIRCC-PDX (Supplementary Fig. 25).
We evaluated the partial correlation between a feature ’sS H A P
values and the target variable (parSHAP) to investigate further these
differences in model performance across different training datasets. In
this case, a positive parSHAP suggests that the classiﬁer has identiﬁed
and successfully exploited an informative feature for its current clas-
siﬁcation task. Given that our CeSta classiﬁer performed just as well on
the internal and external validations, it was not surprising to see
matching parSHAP across CeSta SHAP values and cetuximab response
in IRCC-PDX and CR-PDX (Fig.4c and Supplementary Data 9) for most
features, and particularly for those with the most signiﬁcant impact on
model prediction (Fig.4a, b and Supplementary Data 9). On the other
hand, several of the panCMP catBoost classi ﬁer’st o pf e a t u r e s
(VEGFBC, PTEN, MET, PIK3CA and LYZ expression,TCF7L2 loss) did not
perform as well on CR-PDX, compared to the cell lines training dataset
(Fig. 4d, e), that is: their SHAP values’partial correlation with the target
variable was lower across CR-PDX. This suggests that cell-line-trained
m o d e l so fc e t u x i m a br e s p o n s es t r u g g l et op r e d i c tP D Xc e t u x i m a b
sensitivity, primarily due to differences in the relationship between
expression features and the target variable. These transcriptional dif-
ferences between cell lines and PDXs might be due to the intense
selection pressure imposed during cell line establishment, which
makes available 2d models only partially representative of the general
patient population
19.
Discussion
We have described and made available multi-omic characterisation
and drug screening data for one of the largest CRC PDX collections to
date. This dataset recapitulates typical CRC alteration patterns
observed in patient trials and gold-standard primary cohorts across all
examined ‘omics, and offers a combination of complete cetuximab
response labels as well as dense multi-omic features. The cohort pro-
vides a realistic, stable platform for cetuximab sensitivity biomarker
discovery and drug response modelling.
Building on this PDX collection, we developed CeSta, a multi-omic
ensemble classi ﬁer of cetuximab sensitivity based on a stacked
ensemble architecture. CeSta identiﬁes and leverages transcriptional
markers and predicts cetuximab responses (in an internal holdout
shufﬂev a l i d a t i o na sw e l la sw h e nt e s t e do na ne x t e r n a li n d e p e n d e n t
dataset) more accurately than other state-of-the-art classi ﬁers and
outperforms the criteria currently used in the clinic to address CRC
patients to cetuximab treatment, speci ﬁcally the KRAS-NRAS-BRAF
triple negative genotype. Among the predictive transcriptional mar-
kers identi ﬁed by CeSta are EREG expression (which is higher in
responsive models) and REG4,H hs i g n a l l i n g ,a n g i o g e n e s i s ,a n d
inﬂammation gene set cumulative expression scores (all more repre-
sented in resistant models). Some of these response predictors con-
ﬁrm previous ﬁndings in independent datasets. EREG has been
documented to positively correlate with response to cetuximab in
mCRC patients
62; EREG is an EGFR ligand, so it is conceivable that high
EREG abundance leads to sustained EGFR signalling and sensitisation
to EGFR inhibition. REG4 is a poor-prognosis biomarker in CRC, pos-
sibly due to its ability to promote cancer cell stemness 80,a n di t s
expression was found to correlate with resistance to cetuximab and
other ERBB family inhibitors in CRC PDX models
12. Interestingly, some
elements of the Hh pathway proved to be upregulated in a CRC cell line
in which resistance to cetuximab was attained by prolonged drug
treatment
67. Our results provide translational signi ﬁcance for this
observation by extending its reach to patient tumours on a population
scale. We report that the expression of genes associated with hallmarks
of angiogenesis and in ﬂammation correlate with poor response to
cetuximab and, in the case of inﬂammation, this applies also to clinical
samples from patients. These transcriptional biomarkers might
therefore be viable candidates for inclusion into an improved com-
panion diagnostic for cetuximab sensitivity using clinical-grade gene
expression technologies, such as Nanostring.
The identiﬁed features show a weaker association with cetuximab
response in 2d CRC models than PDXs, corroborating our observation
of poorer predictive performance for models trained on cancer cell
line datasets. While this evidence supports the accuracy of PDX models
for biomarker discovery, it is fair to acknowledge that PDXs only partly
recapitulate the complexity of human tumours. In particular, the
human stroma is rapidly substituted by murine counterparts during
PDX serial passaging, and human immune components are not sub-
stituted by host populations owing to the severe immunodeﬁciency of
mouse recipients
81. Accordingly, all molecular data that contributed to
CeSta development and application were limited to the exploration of
cancer cell-intrinsic traits. However, the fact that CeSta predictive
ability was maintained when analysing bulk transcriptomic datasets
from patients’samples
62 indicates that CeSta, although unﬁtt oc a p t u r e
stromal and immune characteristics, has clinical applicability.
Collectively, our results highlight the value of extensive, cancer
type-speciﬁc, and well-characterised PDX collections for drug screen-
ing, drug sensitivity modelling and mechanism of action discovery,
and motivate future efforts to increase resource dimensions and
improve analytical approaches as a means to further enhance the
informative power and translational potential of PDX-based research.
Methods
Ethics statement
Tumour samples were obtained from 570 patients with CRC who
underwent surgical resection of liver metastases at the Candiolo
Cancer Institute (Candiolo, Torino, Italy), Ospedale Mauriziano
Umberto I (Torino), Città della Salute e della Scienza di Torino — Pre-
sidio Molinette (Torino), and Grande Ospedale Metropolitano
Niguarda (Milano, Italy) during the period 2008– 2015. Informed con-
sent for research use, including for the collection of sex and age
information, was obtained in written form from all patients at the
enrolling institution before tissue banking. Donor patient sex was
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 10

determined by self-report. Study approval was obtained from the
Review Board of the Fondazione del Piemonte per l ’Oncologia FPO—
IRCCS (PROFILING protocol No. 001-IRCC-00IIS-10, version 11.0,
updated July 13, 2022). Tumour tissue (hepatic metastasis) not
required for diagnosis was used to generate PDXs. Animal procedures
were approved by the Candiolo Cancer Institute Institutional Animal
Care and Use Committee (IACUC) and by the Italian Ministry of Health
(authorization 816/2016-PR) and were compliant with all relevant
ethical regulations.
Genomic data collection
Illumina PairEnd pre-capture libraries were synthesised from double-
stranded DNA according to Illumina’s protocol (Illumina Inc.). Geno-
mic DNA quality was validated and for each sample, 200 ng were used
for library preparation. DNA was sheared into 300 base-pair fragments
(1ug DNA in 100 μl volume) using the E210 Covaris plate system
(Covaris, Inc. Woburn, MA). The fragmentation settings used are
Intensity of 4200 Cycles per Burst, for 120 s. Sequencing libraries were
ampliﬁed using the ‘bridge-ampliﬁcation’ process by Illumina HiSeq
pair read cluster generation kits (TruSeq PE Cluster Kit v2.5, Illumina)
and were hybridised to custom RNA baits for the Agilent SureSelect®
protocol. Paired-end, 75 bp sequence reads were generated using
Illumina HiSeq 2000®. The sample mean sequencing coverage was
~700X if the lost coverage because of duplicated and off-target
reads is considered. Reads were aligned to the reference human gen-
ome (NCBI build37) using BWA-aln 0.5.9
82, and sequencing data were
archived in bam ﬁles stored at the European Genome-Phenome
Archive (https://www.ebi.ac.uk/ega/at the EBI) with accession num-
ber EGAD00001003334 (cram ﬁles are in EGAD00001003334, the
study accession number is EGAS00001001171).
555 samples were sequenced using a custom-designed targeted
colon cancer panel (SureSelect, Agilent, UK) consisting of all coding
exons of 116 genes, 22 genes recurrently ampli ﬁed/deleted, 51 CN
regions, 121 MSI regions and 2 gene fusions (RSPO2 and 3). Samples
were fragmented to an average insert size of 150 bp and subjected to
Illumina DNA sequencing library preparation using Bravo automated
liquid handling platform.
Sequencing was performed on an Illumina HiSeq2000 machine
using the 75-bp paired-end protocol targeting 1 Gb sequence per
sample. Data quality was checked for 95% target coverage at 100x and
mutation analysis was performed using an in-house algorithm.
S e q u e n c i n gr e a d sw e r ea l i g n e dt ot h eN C B I3 7h u m a ng e n o m eb u i l d
using the BWA algorithm
82 with Smith-Waterman correction and PCR
duplicates were removed. Base substitutions, small insertions or
deletions, and breakpoints were identiﬁed by comparison against an
unmatched control using established bioinformatic algorithms:
CaVEMan ( https://github.com/cancerit/CaVEMan/) for mutations,
Pindel ( https://github.com/genome/pindel)t od e t e c ti n s e r t i o n sa n d
deletions, and CNVKit ( https://github.com/etal/cnvkit)f o rC N
detection.
We used an unmatched blood sample sequenced to an equivalent
depth as control. To account for the absence of matched control, a
bespoke variant selection pipeline was developed. To enrich for high-
conﬁdence somatic variants, we performed further ﬁltering by
removing known somatic polymorphisms using human variation
databases— Ensembl GRCh37, 1000 genomes release 2.2.2 and
ESP6500— and whether the same polymorphism was observed recur-
rently in 93 normal DNA samples sequenced using the same protocol
and depth.
Cancer genes (CGs) are genes for which we can observe evidence
of positive selection. Several statistical approaches have been devel-
oped to categorise the likelihood of a given gene in a speciﬁct u m o u r
type to undergo a mutation at a high enough frequency for this to be
indicative of a positive selection process. The majority of these
methods rely on a comparison of non-synonymous (dN) and
synonymous (dS) mutations in each gene and factor in additional
covariates. We have elected to use as the foundation of our set of
colorectal CGs two recent statistical approaches developed using large
TCGA datasets
83,84.
6426 driver variants across 113 genes were identi ﬁed using the
statistically signiﬁcant single-codon hotspots from Chang et al. 36 and
the intOGen85 framework. These variants were combined to generate a
reference set of driver variants, annotated based on their origin
(Intogen driver only, Chang driver only, or common to both), their
hotspot status, and whether they were known drivers for CRC. Theﬁnal
set of driver variants was used for annotating the PDX variants.
To assign segment log2R to individual genes we used coordinates
overlap (BEDtools v2.29.2
86, https://github.com/arq5x/bedtools2)
between them and gene coordinates (TSS-TES) obtained from GEN-
CODE (version 34, https://www.gencodegenes.org) for a set of 568
intOGen driver genes.
TCGA COAD/READ copy number calling
Segmented CN variation (CNV) data from TCGA-COAD and TCGA-
READ (~1200 samples) on 02/09/2020 was downloaded via the
Genomic Data Commons Data Portal (GDC, https://portal.gdc.cancer.
gov/repository) using the TCGAbiolinks R package (v2.20.0
87).
The GDC CNV pipeline uses Affymetrix SNP 6.0 array data (har-
monised to GRCh38) to identify genomic regions that are repeated and
infer the CN of these repeats. This pipeline uses the DNAcopy
R-package
88 to perform a circular binary segmentation (CBS) analysis.
CBS translates noisy intensity measurements into chromosomal
regions of equal CN. Theﬁnal outputﬁles are segmented into genomic
regions with the estimated CN for each region. The GDC further
transforms these CN values into segment mean values, which are equal
to log2(copy-number/2). Diploid regions will have a segment mean of
zero, ampliﬁed regions will have positive values, and deletions will
have negative values
89. Masked CN segments are generated using the
same method except that a ﬁltering step is performed that removes
the Y chromosome and probe sets that were previously indicated to be
associated with frequent germline copy-number variation.
Robust CNV events across our patient cohort were identi ﬁed by
searching for matches in the combined TCGA COAD/READ data, using
GISTIC2.0
90 (ftp.broadinstitute.org/pub/GISTIC2.0) and ADMIRE v1.291
(https://ccb.nki.nl/software/admire/)
GISTIC2.0 was applied using the recommended ‘GISTIC2 Com-
mand Line Parameters ’ listed in the GDC CN segmentation doc-
umentation at https://docs.gdc.cancer.gov/Data/Bioinformatics_
Pipelines/CNV_Pipeline/#copy-number-segmentation.H e r et h e ‘seg-
mentation ﬁle’ corresponds to the masked segmented CN variation
downloaded from TCGA COAD/READ, the ‘marker ﬁle’ contains the
aforementioned probe coordinates ﬁltered for ‘freqcnv == FALSE’ as
per the GDC reference ﬁles ( https://gdc.cancer.gov/about-data/gdc-
data-processing/gdc-reference-ﬁles), and the‘reference geneﬁle’is the
GRCh38 reference provided alongside GISTIC2.0.
ADMIRE1.2 was applied using the same parameter con ﬁguration
shown in the example use case provided athttps://ccb.nki.nl/software/
admire/readme.txtwith the ‘segmented CNA’ﬁle again corresponding
to the combined COAD/READ data, and the‘marker ﬁle’containing the
ﬁltered probe coordinates.
The output of these two analyses identiﬁes CNV events spanning
multiple segments from different samples across the patient cohort. We
then merged these results by computing the union of all (fully or par-
tially) overlapping ADMIRE or GISTIC segments, and included all non-
overlapping segments from either tool resulting in a set of 2382 events.
From this combined output, we extracted event and segment coordi-
nates and mapped both to 552 known cancer driver genes in the intO-
Gen catalogue
85 (02/02/2020 release, https://www.intogen.org/
download?ﬁle=IntOGen-Cohorts-20191112.zip) using BEDtools v2.29.286
(https://github.com/arq5x/bedtools2) (Supplementary Fig. 27).
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 11

CNV event frequencies are denoted as the number of equivalent
CNV events in TCGA samples divided by the number of COAD/READ
samples.
Comparing driver gene SNPs in TCGA COAD/READ and PDXs
Frequencies of somatic alteration for TCGA samples was obtained
from cBioPortal, selecting the Colorectal Adenocarcinoma TCGA,
PanCancer atlas ( https://www.cbioportal.org/study/summary?id=
coadread_tcga_pan_can_atlas_2018) dataset.
Comparing copy number variation events in TCGA COAD/READ
and PDXs
We ﬁrst binned PDX segment log2R values into three categories (‘Loss’,
‘Neutral’, ‘Gain’), using the same GISTIC log2R thresholds we applied to
the TCGA COAD/READ data ( −0 . 2 ,1 )[ u s i n gt h es a m et h r e s h o l da si n
TCGA data here might be too strict for PDx sequencing data where
there’s less non-tumour tissue contamination as murine cells/DNA are
ﬁltered out]. We then computed gene-speciﬁc CNV event frequencies
by counting the number of PDX samples with CN altered segments
mapping to each gene, divided by the number of PDX samples.
We then computed the Spearman correlation coefﬁcient for the
TCGA and PDX genewise CNV event (here only ‘Loss’, ‘Gain’)
frequencies.
Assessing PDX copy number stability within lineages
We grouped 91 PDX samples, according to their genealogy, into 13
multi-passage lineages and retrieved gene-speciﬁcl o g 2 Rd a t af o r5 6 9
genes from the analysis described in the previous sections. We then
computed the Pearson correlation across all gene log2Rs for each pair
of PDX samples and labelled each Pearson coef ﬁcient according to
whether the two samples belonged to the same lineage or to
different ones.
Assessing PDX mutational stability within lineages
We analysed somatic mutations along multi-passage PDX lineages
using the same set of 91 PDX samples grouped into 13 lineages as
described above. To rule out false positive calls for putative WT sam-
ples in lineages with apparent inconsistencies (Fig. S4), we further
checked the coverage and absolute number of reads supporting each
individual SNVs and only found single mutated reads in three WT
samples with coverages ~400X.
Gene expression data collection and differential expression
analysis
RNA was extracted using miRNeasy Mini Kit (Qiagen), according to the
manufacturer’s protocol. The quanti ﬁcation and quality analysis of
RNA was performed on a Bioanalyzer 2100 (Agilent), using RNA 6000
Nano Kit (Agilent). Total RNA was processed for RNA-seq analysis with
the TruSeq RNA Library Prep Kit v2 (Illumina) following manufacturer’s
instructions. Sequencing was then performed on Illumina Nextseq 500
at Biodiversa SRL, obtaining single end 151 bp reads, aiming at
20 M reads.
Read counts were obtained using an automated pipeline (https://
github.com/molinerisLab/StromaDistiller), that uses a hybrid genome
composed of both human and mouse sequences to exploit the aligner
ability to distinguish between human derived reads, representing the
tumour component, and mouse ones, representing the murine host
contaminating RNA material.
Reads were aligned using STAR
92 (version 2.7.1a, parameters--
outSAMunmapped Within--outFilterMultimapNmax 10--out-
FilterMultimapScoreRange 3--outFilterMismatchNmax 999--out-
FilterMismatchNoverLmax 0.04) versus this hybrid genome
(GRCh38.p10 plus GRCm38.p5hg38 with GENCODE version 27 and
mouse GRCm38 with GENCODE version 16, indexed with standard
parameters and including annotation information from the GENCODE
27 plus m16 comprehensive annotation).
Aligned reads were sorted using sambamba
93 (version 0.6.6) and
only non-ribosomal reads were retained using split_bam.py94 (version
2.6.4) and rRNA coordinates obtained from the GENCODE annotation
and repeatmasker track downloaded from UCSC genome browser
hg38 and mm9.
featureCounts ( https://rdrr.io/bioc/Rsubread/man/featureCounts.
html, version 1.6.3) was run with the a ppropriate strandness para-
meter (-s 2) to count the non-multi-mapping reads falling on exons and
reporting gene level information (-t exon -g gene_name) using combined
GENCODE basic gene annotation (27 plus m16).
Sequencing data was available for 480 samples, but different ﬁl-
tering criteria lead to 470 QC passing samples. These criteria include:
(1) ≥ 15 M total reads, (2) ≥60% reads assigned to genes by feature
counts, (3) ≥30% reads assigned to human genes over the total of
assigned reads.
These ﬁlters let us retain only samples with at least 5 M
human reads.
To remove samples with lymphomatous characteristics
4, 2 cri-
teria were applied: (i) Principal Component analysis of expression
data (samples with PC2 ≥ 30 were discarded): (ii) computation of a
sample-level score for a leucocyte expression signature
95, averaging
FPKM values for all the signature genes (samples with an average
leucocyte signature ≥ 48 were discarded). Positivity for either cri-
terion ﬂagged samples as lymphomatous and excluded them from
analysis.
Gene-level variance stabilised expression (VST) and robust fpkm
values for 33,670 genes were obtained using DESeq2
96 (version 1.26.0),
tmm using edgeR 97 (version 3.28.1) using only read counts from
human genes.
CRIS and CMS subtyping was obtained for each individual tumour
averaging the VST values for replicates, when available, using the R
package CMScaller
39 (v2.0.1, FDR = 0.05 and RNAseq = TRUE) and the
Rp a c k a g eC R I S c l a s s iﬁer4 (v1.0.0, FDR < 0.2).
Differential expression analysis to compare responders and non
responders was run with DEseq2 96 with the formula ‘~batch +
response’, where batch indicates which one of the ﬁve different
sequencing batches the sample belongs to ssGSEA scores were calcu-
lated using GSVA
98 (version 1.34.0) on tmm values with kcdf = ‘
Gaussian’and method = ‘gsva’.
The obtained DEGs were used to perform GSEA enrichment ana-
lysis with R libraries ClusterPro ﬁler99,100 (v3.14.3), DOSE101 (v3.12.0),
msigdbr30 (v7.4.1) and enrichplot ( https://yulab-smu.top/biomedical-
knowledge-mining-book/)(v1.6.1). Protein-protein interactions net-
work analysis was performed with STRING (string-db.org), the 20th
April 2023 (https://version-11-5.string-db.org/cgi/network?networkId=
bJPsEA2nP3WX).
Promoter sequences of the differentially expressed genes were
deﬁned as regions 1500 bp upstream and 500 bp downstream the TSS,
using the same annotations for transcripts that were used with fea-
tureCounts. Motifs enrichments were obtained with HOMER
(version 4.8).
Microarray data from Khambata-Ford
62 (GSE5851) was obtained
using Gene Expression Omnibus (GEO) query 102 (version 2.54.1),
applying a log transformation and selecting the most variable probe
when multiple ones were available for the same gene, then ssGSEA
scores were obtained as previously described.
Github repositories: https://github.com/molinerisLab/
StromaDistiller, https://github.com/vodkatad/RNASeq_biod_metadata
and https://github.com/vodkatad/biodiversa_DE.
The fastq ﬁles for all sequenced samples are stored at the Eur-
opean Genome-Phenome Archive ( https://www.ebi.ac.uk/ega/at the
EBI) with accession number EGAS00001006492.
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 12

Methylation data collection
Methylation proﬁles for 568 CRC samples were obtained using Illumina
MethylationEPIC bead chip, which measures methylation status at
about 850,000 sites using hybridisation on two different probes after
bisulﬁte treatment on DNA. These samples comprise tissue from the
original patient, either primary tumours or metastases, or both in
some cases, and the corresponding engrafted tumours in mice (PDXs).
Raw data have been processed using the min ﬁ package (https://
bioconductor.org/packages/release/bioc/html/minﬁ.html, version 1.32.0).
Data preprocessing was performed following the best practices outlined
by Bioconductor minﬁ vignette and documentation, and Hinoue et al.
41.
(https://www.bioconductor.org/packages/devel/workﬂows/vignettes/
methylationArrayAnalysis/inst/doc/methylationArrayAnalysis.html).
Background noise was removed using the min ﬁ function pre-
processNoob(), which implements the noob background subtraction
method with dye-bias normalisation. Samples and probes that did not
pass the quality control were then excluded from further analyses.
For samples, min ﬁ provides a simple quality control plot that
represents the log median intensity in both the methylated (M) and
unmethylated (U) channels. By adopting the default median intensity
cutoff of 10.5, six samples with lower values were removed from the
dataset.
We then ﬁltered the probes, based on their detectionp value (det-
Pval), which is indicative of the quality of the signal. Byﬁltering out all
those probes of which det-Pval was higher than 0.01 in at least one
sample, we removed 64,361 probes. We also removed all the probes
mapping on X and Y chromosomes (19,627), to remove gender bias,
and those probes that are known to bind to common SNPs (30,435).
Moreover, using the list originally published by Chen et al.
103,w e
r e m o v e d4 3 , 1 7 7p r o b e st h a th a v eb e e nd e m o n s t r a t e dt om a pt om u l -
tiple places in the genome.
To work with a coherent set of probes for all the samples, in
particular xenografts, we decided to apply one last probes ﬁlter,
removing all those probes known to speciﬁcally map on murine gen-
ome as well, in order to remove possible methylation signal coming
f r o mt h em u r i n ei nﬁltrate, with the same rationale followed for
microarray data
95.T od ot h i s ,w ec o m b i n e dt w ol i s t so fm u r i n e - s p e c iﬁc
probes, obtained from Needhamsen et al.104 and Gujar et al. 105,w h i c h
resulted in removal of other 22,537 probes.
We combined the hg19 annotation package (IlluminaHu-
manMethylationEPICanno.ilm10b2.hg19 version 0.6.0), with the lift-
Over()function from the rtracklayer package106 (version 1.46.0) and the
importedﬁle hg19ToHg38.over.chain.gz (http://hgdownload.soe.ucsc.
edu/goldenPath/hg19/liftOver/) in order to convert the remaining
700,298 probes’coordinates from hg19 to hg38.
Moreover, as done for expression data (See Gene expression data
collection), we removed samples with clear lymphomatous char-
acteristics. Speciﬁcally for methylation, samples with PC2 ≥ 500 were
almost alwaysﬂagged by H&E analysis when it was available, therefore
we considered all of them to be lymphomatous.
To identify groups of samples sharing similar methylation proﬁles,
Beta values were used to run non-neg ative matrix factorisation algo-
rithms in R ( https://www.rdocumentation.org/packages/NMF/,v e r s i o n
0.22.0). k =5 w a s i d e n t iﬁed as the best parameter by the cophenetic
correlation coefﬁcient (bootstrapping arguments:rank= 2:6, nrun= 100,
seed= 42,.options= ‘p70’). We therefore selected 5 as the number of
classes used to characterise the methylation landscape of our samples.
We ﬁnally converted the ﬁve groups ﬁve engineered features from
methylation data via one-hot encoding (Supplementary Data 1).
The idat ﬁles for all samples are available at the GEO with acces-
sion number GSE208713.
Clinical data collection
Since the patients whose tumours are included in our biobank were
not enroled in a speci ﬁc clinical trial and underwent surgery in
different hospitals, our clinical data collection is based on personal
communications with the Surgery Departments. This is the main rea-
son behind the sparseness of the data.
Measuring cetuximab response in PDX models
After surgical removal from patients, each metastatic CRC specimen
was fragmented; some fragments were frozen for molecular analyses,
and two fragments were implanted in two 5-week-old female NOD-
SCID mice. After engraftment and tumour mass formation, the
tumours were passaged and expanded for two generations until pro-
duction of 2 cohorts, each consisting of six 5-week-old male or female
NOD-SCID mice. When tumours reached an average volume of
400 mm 3, mice were randomised for treatment: 6 mice were treated
with placebo and 6 mice were treated with cetuximab (20 mg/kg/
twice-weekly i.p.).
Tumour size was evaluated once-weekly by calliper measure-
ments and the approximate volume of the mass was calculated using
the formula 4/3π·(d/2)
2·D/2, where d is the minor tumour axis and D is
the major tumour axis. The maximum tumour diameter allowed by the
IACUC and the Italian Ministry of Health (20 mm) was not exceeded.
Sex was not factored into the study design because large-scale studies
on cetuximab have demonstrated no signi ﬁcant differences in
response between male and female mice
2,20.F o ra s s e s s i n gP D Xm o d e l s
response to therapy, we used averaged volume measurements at
3 weeks after treatment normalised to the tumorgraft volume at the
time of cetuximab treatment initiation. 231 tumour grafts were clas-
siﬁed as follows: (1) ‘OR’ models with a decrease of at least 50% in
tumour volume (2)‘progressive disease’(PD) models with at least a 35%
increase in tumour volume, and (3) ‘SD’for the ones in between
2.
Finally, to obtain a balanced dataset, we elected to combine the
‘SD’ and ‘OR’ classes into a single ‘SD-OR’ (i.e., treatment responder)
class, turning our cetuximab response modelling task into a binary
classiﬁcation problem.
All animal procedures were approved by the Ethical Commission
of the Candiolo Cancer Institute and by the Italian Ministry of Health
(authorization 806/2016-PR). All animal procedures for the CR PDX
data set were executed in an AAALAC-accredited animal facility and
approved by the Committee on the Ethics of Animal Experiments of
the regional council (Permit Numbers: G-13/13 & G18/12).
No statistical methods were employed to predetermine sample
size. Sample sizes were guided by our prior experience with various
PDX models
2,20 and aligned with PDX minimal information
standards107. Tumour-bearing mice were randomised prior to treat-
ment using the Laboratory Assistant Suite 108 by alternately assigning
them to different treatment groups.Investigators were not blinded to
group allocation during the experiments or outcome assessment.
Genomic feature engineering
To reduce data sparsity, we reshaped our mutational annotations into
a binary matrix -- with columns (110 in total) corresponding to genes
and rows (231 in total) corresponding to PDX models, where a value of
1 indicates that one or more SNVs mapping to a given gene have been
observed in a given PDX model. We also generated additional muta-
tional features: a‘mutational burden’feature containing the sum of all
mutated genes for each PDX, and a set of‘multiple mutations’features,
i n d i c a t i n gt h en u m b e ro fu n i q u eS N P sh o s t e db yag i v e ng e n ei naP D X
model. Finally, we ﬁltered out any binary feature which was observed
in fewer than 5 PDXs across our IRCC-PDX collection. To obtain a
compact representation of relevant co-occurent or mutually exclusive
mutations, we developed an extended version of the CELLector
methodology
31 that partitioned the PDx mutation landscape recur-
sively ﬁnding subgroups deﬁned by the most recurrent combinations
of genomic events (mutations or CN alterations). Brieﬂy, the original
version of CELLector (from now on referred to as hierarchical),
recursively applies the Eclat algorithm
109 on a population described by
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 13

a binary event matrix (BEM), with each column representing a genomic
feature and 0/1 possible entries indicating the absence/presence of
that feature in a sample. In the hierarchical version of CELLector, the
genomic background of a population is represented as a binary tree
whose topology is de ﬁned by the most frequently observed combi-
nation of genomic features (referred as signature) together with the
fraction of samples for which those mutations occur and hence satisfy
the signature rule (sequence of presence/absence of speciﬁc features).
In particular, CELLectorﬁrst identiﬁes the root as the genomic feature
with largest support, i.e., number of patients in which that feature is
observed, and then de ﬁnes two sibling nodes. The left child corre-
sponds to the subset of samples satisfying the parent feature and the
feature with greatest support among the samples in the parent node.
The right child corresponds to the complementary population of the
parent node, composed of samples not satisfying that feature, and
among those the feature with greatest support. This algorithm is
applied recursively until no sub-population satisfying a certain sig-
nature rule of at least a minGlobSupp percentage of samples is iden-
tiﬁed, with minGlobSuppbeing a hyperparameter deﬁned apriori. This
hierarchical structure outputsK recursive signature rules that can be
converted into a partition of K + 1 groups as follows.
Starting from CELLector hierarchical binary tree,
1. For each node starting from the root, we de ﬁne with U the set of
samples satisfying that node rule de ﬁned as the corresponding
signature S.
2. If the considered node has a left child ( U
l /C26 U) associated to
feature Fl ,w ed e ﬁned with Urm : = Ul the set of samples to be
removed from U.
3. If Ul has additionally a right childUr deﬁned by feature Fr , Urm is
updated with Urm : = Urm
S Ur
4. If Ur has another right child Ur, r deﬁned by signature Fr, r ,t h e
update is repeated as Urm : = Urm
S Ur, r a n dt h i ss t e pi sp e r -
formed recursively until the considered node has no right child.
5. The new set of samples is de ﬁned as Un = UnUrm and corre-
sponding signature rule representing the group is de ﬁned
as S, /C24 Fl , /C24 Fr , /C24 Fr, r , ::
If the condition in step 2. is not satis ﬁed, the group is directly
deﬁned as samples in node U and satisfying signature S rule. Once
every node in the hierarchical binary tree was considered, the last
group was deﬁned as the remaining samples that did not satisfying any
hierarchical signature rule. The signature deﬁning this group is created
as the negation of the root node and all the recursive right childers, as
described before. Note that the newly created groups could be com-
posed of a fraction of patients lower than the minGlobSupp.
We applied the partitioned version of CELLector (V2.0.0) to the
somatic mutation PDx space in BEM format with minGlobSupp
ﬁxed at 0.02.
Similarly to what we describe for above for mutation features, we
discretise each of our 1162 gene-level log2 features into four categories
(‘Loss’, ‘Neutral’, ‘Gain’, ‘High Gain’), using, in addition to the GISTIC
log2R thresholds for‘Loss’and ‘Gain’(−0.2, 1), an additional threshold
at 2, above which a gene is considered to be involved in a ‘High Gain’
event in which more than 1 additional copy is gained.
This ‘High Gain’category is added to help capture any association
between driver gene high-order CN gain and cetuximab sensitivity.
We then reshape these categorical CN annotations into a binary
matrix with columns corresponding to individual CNV events involving
a given gene (e.g., ‘CD12_Gain’) and rows corresponding to PDX mod-
els. We then remove features which have the same value in 85% or
more of our training PDX models.
Transcriptomic feature engineering
To reduce RNAseq data dimensionality from an initial input of 33,668
gene-level expression features, as well as to include state-of-the-art
knowledge of cancer signalling pathways and transcription factor
activity, we computed (1) GSVA scores 98 (http://www.biomedcentral.
com/1471-2105/14/7) using the GSVA R package (version 1.34.0, R 3.6.3,
kcdf = ‘gaussian’) on tmm expression levels and the MSigDB Hallmark
gene sets30 as well as (2) PROGENy scores computed using the progeny
Rp a c k a g e29. Both sets of scores were computed separately for each
train/test replicate (see following sections) to avoid any information
leakage. This step yelds to a total of 66 aggregated transcriptomic
features (Supplementary Data 1). Finally, we considered that many
PROGENy and Hallmarks gene set are partially overlapping: for
example PROGENy ’s ‘NFkB’ set corresponds to Reactome ’s ‘TAK1
activates NFkB by phosphorylation and activation of IKKs complex ’
and ‘RIP-mediated NFkB activation via ZBP1’, and thus it shares 8 of its
48 genes with PROGENy’s ‘TNFa’set (Reactome’s ‘TNF signalling’). To
avoid excessive collinearity between scores based on overlapping gene
sets, weﬁrst computed the Pearson correlation coefﬁcient (PCC) for all
pairs of engineered transcriptomic features over all instances in the
training set, and considered as ‘collinear’ all pairs with a PCC larger
than 7. Here, for each pair of collinear features, we discard the one with
the higher Mann-Whitney U test p value between responder and non-
responder PDXs in each training split.
Clinical feature engineering
We consolidated our clinical data by: (1) dropping any features with
more than 40% missing values, (2) dropping redundant or inconsistent
features (‘OXALIPLATIN-based treatments’, ‘N’, ‘T’, ‘N of other meta-
static resections before collected metastasis’, ‘M’, ‘Site M’, ‘Site of pri-
mary’, ‘Site of primary DICOT’), (3) converting‘Stage at ﬁrst diagnosis’
annotations to an integer score and retaining only the highest score for
a given PDX model where multiple annotations are present, (4) con-
verting the ‘ Lymph node density’ annotations to a numerical score
corresponding to the ratio of positive lymph nodes over the total
lymph node count, (5) encoding all treatment backbone annotations as
categorical features, (6) one-hot-encoding all sample anatomical
location annotations. This yielded 25 features covering patient, pre-
vious treatment, and tumour metadata (Supplementary Data 1).
Single-omic exploration of IRCC-PDX data
We conducted UMAP dimensionality reduction 42 across individual
omics using umap-learn (v 0.5.2, https://github.com/lmcinnes/umap)
followed by density-based HDBSCAN43 (v0.8.29-1,https://github.com/
scikit-learn-contrib/hdbscanclustering) of the resulting 2d UMAP
embeddings. We then assessed omic feature distribution across clus-
ters for each omic and highlighted (Supplementary Fig. 12-15) those
which differentiate best between clusters using a Kruskal-Wallis test
(W. H. Kruskal & W. W. Wallis, ‘Use of Ranks in One-Criterion Variance
Analysis’, Journal of the American Statistical Association, Vol. 47, Issue
260, pp. 583-621, 1952) as implemented in scipy v1.11.1 (Supplementary
Data 2). Further, we computed a‘one vs all’X2 test of independence for
each categorical feature and each cluster or a Mann-Whitney U test for
each continuous feature and each cluster (Supplementary Data 2),
using scikit-learn v1.02 or scipy v1.11.1. This procedure was replicated
to compute enrichment analysis of covariates -- that is sample anno-
tations that were not included in the UMAP input, including NMF
methylation cluster labels, CRIS classes -- in the the above mentioned
UMAP + HDBSCAN clusters, as well as of differential drug response
across them (Supplementary Data 2). P values were corrected via
Bonferroni across all feature and clusters, divided per omic.
Model architecture
For our cetuximab response model we selected a stacking classi ﬁer
architecture. Stacking is an ensemble learning technique which com-
bines the individual contributions of multiple classi ﬁcation models
(level-1-classiﬁers) via a meta-classi ﬁer. Here, we use a soft voting
classiﬁer which outputs the ﬁnal binary class labels (cetuximab non-
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 14

responder; cetuximab responder) based on the argmax of the sums of
the predicted probabilities from the level-1-classi ﬁers (scikit-learn
VotingClassﬁer110,111,v 1 . 0 2 ) .
Our CeSta classiﬁer pipeline uses a late integration approach to
prevent high-dimensional‘omics (transcriptomics, methylomics) from
overwhelming smaller omics by dominating the selected feature set.
We perform an initial round of single-omic supervised feature selec-
tion whose output is then piped into each of the four lvl 1 classi ﬁers
described below (Fig. 1a).
This selection step ranks features according to the product of (1) a
feature rank based on the Fisher ’s exact statistic (scipy v1.9
110,111)f o r
binary features or Mann-Whitney U-test statistic (scipy v1.9) for con-
tinuous features, (2) a feature rank based on percent lift, and (3) a
feature rank based on logit model (statsmodels v0.13.2 logit) coef ﬁ-
cients. A set of topK features is then selected from this ranked list, with
K being one of CeSta ’s hyperparameters. This selection process is
applied exclusively to the training set in each train, test split replicate
during the internal validation (Fig. 1b and below) to avoid any infor-
mation leakage. Model explanation in Fig.4 shows feature importance
and corresponding statistics and metrics obtained when training CeSta
over the entire IRCC-PDX set as per the CeSta instance used for
external validation on CR-PDX sample (Fig.1b)
We used four distinct level-1-classi ﬁer pipelines (Fig. 1a): (1) a
model-based (scikit-learn KNeighborsClassi ﬁer) forward feature
selection, followed by elastic net penalised logistic regression (scikit-
learn LogisticRegression with ‘penalty’ set to ‘elasticnet’), (2) ANOVA
feature selection (scikit-learn f_classif), followed either by a support
vector classiﬁer (scikit-learn SVC) or (3) an extra trees classiﬁer (scikit-
learn ExtraTreesClassiﬁer), and (4) a CatBoost classi ﬁer (catBoost
1.0.5
79) trained on a common subset of features from CMP, then on
IRCC PDX (continual learning).
Each level-1-classiﬁer was trained (or re-trained in the case of
CatBoost, see following sections) on a dataset of features selected (see
above) from our 5 ‘omic data sources (mutation, CNV, expression,
methylation, clinical). Finally, level-1-classiﬁer prediction probabilities
were stacked and taken as input by our meta-classi ﬁer (see above)
which, in turn, gave in output a ﬁnal binary prediction.
Model training, tuning, and validation
We generated 50 train, test split (150/81 PDXs) holdout shuf ﬂe repli-
cates by performing stratiﬁed sampling from our IRCC-PDX dataset.
The latter consisted of 231 fully characterised (targeted sequencing,
RNAseq, methylation assay, clinical metadata) PDX models which were
labelled as cetuximab responders or non-responders according to
tumour volume variation after treatment, as described above.
For the internal validation analysis, we used a nested cross-
validation approach (inspired by mlextend’s StackingCVClassiﬁer
112)t o
tune and train 50 independent CeSta replicates, one per each train, test
split. Each training set replicate was further split into 3 folds, and in
3 successive rounds, 2 folds were used (in turn) to ﬁtt h el e v e l - 1 -
classiﬁers. In each round, the level-1-classiﬁers were then applied to the
remaining 1 subset not used for model ﬁtting in each iteration. The
resulting predictions were then stacked and provided -- as input data --
to the meta-classiﬁer. After comparing the meta-classiﬁer’s prediction
on the validation fold to the corresponding true labels, the ﬁrst-level
classiﬁers were ﬁt to the entire training set replicate (Fig. 1a, b).
This model training process was performed using a hyperpara-
meter combination suggested by Optuna
113 across 200 trials, while
maximising the average of the area under the ROC curve (ROC AUC)
computed over 3 training folds. Tuned parameter include: the number
of top features selected during the ﬁrst selection step, ‘colsample_-
bylevel’, ‘depth’, ‘boosting_type’, ‘boosting_type’, ‘bootstrap_type’ for
the CatBoost classi ﬁer; number of sequentially-selected features,
elastic net ‘C’, ‘l1_ratio’ for the Logistic elastic net classi ﬁer pipeline;
number of ANOVA-selected features, ‘C’ and ‘kernel’ for the SVC
classiﬁer pipeline; number of ANOVA-selected features,‘n_estimators’
for the ExtraTrees classi ﬁer pipeline. This hyperparameter space
search was performed, independently, for each model replicate.
Finally, we validated each of our 50 CeSta pipelines by predicting
each PDX model in their respective test set as a cetuximab‘responder’
or ‘non-responder’, and computing the resulting ROC AUC and ROC
AUC 95 con ﬁdence interval (using DeLong ’s method) by comparing
predicted and true labels.
For the external validation analysis, the same tuning, training, and
validation process was repeated using the entire IRCC-PDX dataset as a
training set ( N = 231), and the CR-PDX dataset as a test set ( N =5 0 )
(Fig. 1b, c).
Performance baselines
To provide a realistic benchmark for CeSta performance, we de ﬁne
and train a number of alternative, multi-omic cetuximab sensitivity
predictors. The latter are all trained, tuned, and validated using a set of
30 holdout shufﬂe replicates, analogous to the setup we use for CeSta
internal validation in Fig. 1b.
‘tripleNegRule’is a rule-based classiﬁer based on the KRAS-NRAS-
BRAF mutational signature: it will output a‘non-responder’prediction
if any of these three genes is mutated in the current PDX example.
‘tripleNegRightRule’is a rule-based classiﬁer based on the KRAS-
NRAS-BRAF mutational signature and the ‘right colon’ marker (i.e.,
whether the original tumour was located in the right portion of the
patient’s colon). This decision strategy originates from a retrospective
analysis of triple negative patients from the CRYSTAL and FIRE-3 trials
where right-sided tumours had signi ﬁcantly poorer prognosis and
lower response to cetuximab treatment(Tejpar et al.
44).
tripleNegRightRule will output a ‘non-responder’ prediction if
either (1) any of KRAS, NRAS, BRAF is mutated or (2) the original
tumour was right-sided.
‘elNet_baseline’ is an Elastic-Net net penalised logistic regression
classiﬁer (scikit-learn LogisticRegression with penalty set to ‘elas-
ticnet’) based on four binary features encoding the mutational status
of KRAS, BRAF, NRAS (i.e., the ‘triple negative’ CRC signature), and
whether the primary tumour is located in the Right Colon. This cor-
responds to the state-of-the-art clinical signature for cetuximab sen-
sitivity in CRC, as we discuss in Introduction and Results.
‘rawL1elasticnet’is an Elastic-Net net penalised logistic regression
classiﬁer which uses our full set of raw (non aggregated) features, that
is: 110 binary gene mutational status features, 33,668 variance-
normalised gene-level RNAseq data, and 1162 binary CNV events.
‘MixOmics sPLS-DA ’ uses mixOmic ’s
114 multivariate integration
approach, based on Partial Least Squares (PLS) regression and dis-
criminant analysis, in which the most informative features (i.e., those
that best discriminate between c etuximab responsive and non-
responsive PDXs) from different ‘omics are selected with the con-
straint of correlation between their ﬁrst PLS components. More speci-
ﬁcally, here we follow the multi-omic classiﬁcation case study illustrated
in http://mixomics.org/methods/spls/.W e( 1 )p e r f o r mL A S S Of e a t u r e
selection (glmnet v4.2, https://www.rdocumentation.org/packages/
glmnet) for methylation (700,298 probe-level features) and expression
(33,668 gene level features), (2) use a sparse partial least-squares dis-
criminant analysis model (sPLS DA) for single-omic dimensionality
reduction, (3) followed by a DIABLO model for horizontal multiple
‘omics integration. We optimise both the number of PLS components
and the number of selected features for each omic and each component
via 3-fold cross-validation on each training set replicate.
Finally, we validate these benchmark classi ﬁe r so ne a c ht e s ts e t
replicate, as described for our CeSta classi ﬁer in Fig. 3bb yl a b e l l i n g
each PDX model as a cetuximab ‘responder’ or ‘non-responder’,a n d
computing the resulting ROC AUC by comparing predicted and true
labels, again using DeLong’s method for computing the ROC AUC 0.95
conﬁdence interval where possible.
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 15

Cell line multiomic data source
The Cell Model Passport portal 55 (https://cellmodelpassports.sanger.
ac.uk/) catalogues and curates multi-omic data for cancer cell line and
organoid models. When combined with the Genomics of Drug Sensi-
tivity in Cancer dataset ( https://www.sanger.ac.uk/tool/gdsc-
genomics-drug-sensitivity-cancer/), it provides genomics, tran-
scriptomics, and cetuximab response data for 860 unique cancer cell
line models (panCMP dataset). Here, we repeat the same data pre-
processing and feature engineering steps we performed for the IRCC-
PDX dataset, with the exception of the NMF-based clustering of
methylation probes as this omic is missing from the CMP collection.
Further, as cell line cetuximab response is quanti ﬁed as IC50 values,
rather than tumour volume change, here we dichotomise our target
variable using the median IC50 for all cell lines in the panCMP dataset
with lines falling below this threshold being labelled as ‘responders’.
For the purpose of comparing the predictive performance of a
model trained on cell line data against one trained on PDX data, we
generate a panCMP training set which includes a subset of 860
examples and their multi omic characterisation (Data and Code
Availability). These features correspond to the subset available in both
the aforementioned panCMP dataset, our IRCC-PDX dataset, and the
CR-PDX dataset. We then train and tune a catBoost classiﬁer pipeline
(see above for pipeline architecture, hyperparameters) over this
panCMP training set using an 8-fold cross-validation approach across
50 Optuna trials. This cell-line trained‘base model’is then provided, as
a starting point for continual learning, to a second round of training
(using the ‘init_model’ﬂag) over either an IRCC PDX train set split for
internal validation, or the entire IRCC-PDX dataset for external vali-
dation on the CR-PDX dataset (Fig. 1b).
From the panCMP dataset, we can further subset 44 colorectal cell
lines (CRC-CMP), which are characterised with the same subset of
features as in the panCMP dataset. This context-speci ﬁc dataset can
also be used to train a catBoost‘base model’w h i c hw et h e nf e e di n t oa
second catBoost classiﬁer trained on IRCC-PDX.
External validation: Charles River dataset
An independent CRC PDX cohort 115 (https://www.cancermodels.org/
search?ﬁlters=data_source%3ACRL+AND+dataset_available%3Acopy
+number+alteration%2Cexpression%2Cmutation+AND+model_type%
3APDX+AND+primary_site%3Acolon) has been assembled and char-
acterised by our collaborators at Charles River Discovery Research
Services (CR). We use 50 CRC LMX, ﬁrst-pass PDX models corre-
sponding to 50 unique patient samples characterised using a partially
overlapping set of multi-omics features as in the IRCC PDX cohort. For
missing features (e.g., methylation NMF cluster labels, some clinical
annotations, some CNV events) we impute their values for this CR-PDX
cohort using the mode for categorical features and the median for
continuous features. We then use this CR-PDX dataset as a fully inde-
pendent validation cohort to compare our stacked classiﬁer’sp e r f o r -
mance against that of baseline models after training on the entire
IRCC-PDX dataset.
Post-hoc model explanation
As a cross-model proxy for feature importance, for each feature, we
calculate the mean of the absolute SHAP values ( https://github.com/
slundberg/shapv0.4) across all instances in the test set. We consider
the absolute values as we do not want positive and negative values to
offset each other. Features that have large mean absolute SHAP values
are those that more signiﬁcantly impact model predictions.
We are also interested in assessing, for a given classi ﬁer, which
features perform equally well across different datasets (i.e., panCMP,
IRCC-PDX, CR-PDX). To do so, we start by evaluating the relationship
between a feature ’s SHAP values and the target variable. A positive
correlation here indicates that the model has identiﬁed and it is suc-
cessfully exploiting an informative feature for its current classiﬁcation
task. Given that SHAP values are additive, with the model’s prediction
being the sum of all feature SHAPs, it makes sense to remove the effect
of other features ’ contribution by computing the partial correlation
between each feature and the target after removing the effect of all
other features (i.e., controlling variables). Speci ﬁcally, here we use
pingouin
116 (v0.5.1) and its partial_corr function specifying, in turn, all
features but one as x-covariates.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
The raw sequencing data generated in this study have been deposited in
the European Genome-Phenome Archive (EGA) database under the
accession numbersEGAS00001001171(targeted DNA sequencing) and
EGAS00001006492(RNAseq), and are accessible upon request via the
EGA portal, as required for personally identiﬁable data. In compliance
with legal requirements to safeguard patient privacy, access to the raw
data stored in the EGA is managed by a Data Access Committee (DAC)
overseen by E.G., L.T. and the Data Sharing ofﬁce at Sanger. Researchers
can request access by reaching out to the EGA, which will inform the
DAC of the request. The DAC will approve access within roughly two
weeks and decide the duration for which access will be granted. The raw
methylation data generated in this study have been deposited in the GEO
database under the accession numbersGSE208713(methylation data).
The Khambata-Ford dataset is available on GEO under the accession
numberGSE5851. Intermediate data needed to fully replicate the results
in Figs. 1, 2 is available at https://bitbucket.org/uperron/ircc-pdx_
exploration. Intermediate data, models and code needed to fully repli-
cate CeSta and the results in Figs. 3, 4 is available at https://bitbucket.
org/uperron/cesta_pdx. The CR-PDX data is available on CancerMo-
dels.org. The sample list can be retrieved, matching sample identiﬁers as
detailed in Supplementary Data 1, at: https://www.cancermodels.org/
search?ﬁlters=data_source%3ACRL + AND+dataset_available%3Acopy
+number+alteration%2Cexpression%2Cmutation+AND+model_type%
3APDX + AND+primary_site%3Acolon. The associated multi-omic data
can be obtained on request by registering a free account on criver.com
at https://compendium.criver.com/search?m%5Bids%5D%5B0%5D=
10715&m%5Bs%5D=1&f%5Bg%5D%5Bht%5D%5Bs%5D=&f%5Bg%5D%5Bmu
%5D%5Ba%5D=&f%5Bg%5D%5Bmu%5D%5Be%5D=&f%5Bg%5D%5Bcn%5D
%5Bmi%5D=0&f%5Bg%5D%5Bcn%5D%5Bmx%5D=0&f%5Bp%5D%5Bage%
5D%5Bmin%5D=&f%5Bp%5D%5Bag e%5D%5Bmax%5D=&f%5Bp%5D%
5BoriginTypes%5D=&f%5Bp%5D%5Bgenders%5D=&f%5Bp%5D%
5Bspecies_population_ids%5D=&f%5Bp%5D%5Bdifferentiations%5D=&g%
5Baccessions%5D=all, after registering a free user-account. Processed
RNAseq data for the IRCC-PDX and the CR-PDX collections is available on
ﬁgShare at https://ﬁgshare.com/s/35d13c7e7cf8f4759334
117. The cell-line
multi-omic and drug response data used in this study can be accessed on
the CellModelPassports55 and the Genomics of Drug Sensitivity in
Cancer118 data portals, respectively at:https://cellmodelpassports.sanger.
ac.uk/downloads and https://www.cancerrxgene.org/downloads/drug_
data. Source data are provided with this paper.
Code availability
The StromaDistiller Code119 and the RNASeq_biod_metadata code 120
implementing a computational pipeline tracking counts and metadata
across different sequencing batches for xenografts/organoids RNAseq is
available athttps://github.com/molinerisLab/StromaDistillerand https://
github.com/vodkatad/RNASeq_biod_metadata. The biodiversa_DE
Code
121 performing differential expression analysis with DESeq2 and
various enrichment analyses on the results is available athttps://github.
com/vodkatad/biodiversa_DE. CELLector v2.0.0122 is available at https://
github.com/francescojm/CELLector. Additional code performing multi-
omic data preprocessing, normalisation, and integration and
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 16

reproducing the results depicted in Figs.1,2, 3, 4 is available at https://
bitbucket.org/uperron/pdx_multiomics_integration_preprocand https://
bitbucket.org/uperron/ircc-pdx_explorationand https://bitbucket.org/
uperron/cesta_pdx, respectively.
References
1. Biller, L. H. & Schrag, D. Diagnosis and treatment of metastatic
colorectal cancer: a review.JAMA 325, 669–685 (2021).
2. Bertotti, A. et al. A molecularly annotated platform of patient-
derived xenografts (‘xenopatients’)i d e n t iﬁes HER2 as an effective
therapeutic target in cetuximab-resistant colorectal cancer.Can-
cer Discov. 1,5 0 8–523 (2011).
3. Burgenske, D. M. et al. Establishment of genetically diverse
patient-derived xenografts of colorectal cancer.Am. J. Cancer
Res. 4,8 2 4–837 (2014).
4. Isella, C. et al. Selective analysis of cancer-cell intrinsic tran-
scriptional traits deﬁnes novel clinically relevant subtypes of
colorectal cancer.Nat. Commun. 8, 15107 (2017).
5. Stintzing, S. et al. FOLFIRI plus cetuximab versus FOLFIRI plus
bevacizumab for metastatic colorectal cancer (FIRE-3): a post-hoc
analysis of tumour dynamics in the ﬁnal RAS wild-type subgroup
of this randomised open-label phase 3 trial.Lancet Oncol. 17,
1426–1434 (2016).
6. Heinemann, V. et al. FOLFIRI plus cetuximab or bevacizumab for
advanced colorectal cancer:ﬁnal survival and per-protocol ana-
lysis of FIRE-3, a randomised clinical trial.B r .J .C a n c e r124,
587–594 (2021).
7 . S c h w a r t z b e r g ,L .S .e ta l .P E A K :ar a n d o m i z e d ,m u l t i c e n t e rp h a s eI I
study of panitumumab plus modiﬁed ﬂuorouracil, leucovorin, and
oxaliplatin (mFOLFOX6) or bevacizumab plus mFOLFOX6 in
patients with previously untreated, unresectable, wild-type KRAS
exon 2 metastatic colorectal cancer.J. Clin. Oncol.32, 2240–2247
(2014).
8. Van Cutsem, E. et al. ESMO consensus guidelines for the man-
agement of patients with metastatic colorectal cancer.Ann.
Oncol. 27,1 3 8 6–1422 (2016).
9. Harrison, R. K. Phase II and phase III failures: 2013-2015. Nat. Rev.
Drug Discov. 15,8 1 7–818 (2016).
10. Yonesaka, K. et al. Activation of ERBB2 signaling causes resistance
to the EGFR-directed therapeutic antibody cetuximab.Sci. Transl.
Med. 3, 99ra86 (2011).
1 1 . v a nd eW e t e r i n g ,M .e ta l .P r o s p e c tive derivation of a living organoid
biobank of colorectal cancer patients.Cell 161
,9 3 3–945 (2015).
12. Schütte, M. et al. Molecular dissection of colorectal cancer in pre-
clinical models identiﬁes biomarkers predicting sensitivity to
EGFR inhibitors.Nat. Commun. 8, 14262 (2017).
13. Lupo, B. et al. Colorectal cancer residual disease at maximal
response to EGFR blockade displays a druggable Paneth cell-like
phenotype.Sci. Transl. Med. 12, eaax8313 (2020).
14. Iorio, F. et al. A landscape of pharmacogenomic interactions in
cancer. Cell 166,7 4 0–754 (2016).
1 5 . T s h e r n i a k ,A . ,V a z q u e z ,F . ,M o n t g o m e r y ,P .G .&W e i r ,B .A .D eﬁning
a cancer dependency map. Cell 170,5 6 4–576.e16 (2017).
16. Ledford, H. US cancer institute ov erhauls cell lines: veteran cells
to be replaced by human tumours grown in mice. Nature 530,
391 (2016).
17. Santaballa, A. et al. SEOM clinical guideline in ovarian cancer
(2016). Clin. Transl. Oncol. 18,1 2 0 6–1212 (2016).
18. Ben-David, U. et al. Genetic and transcriptional evolution alters
cancer cell line drug response. Nature 560,3 2 5–330 (2018).
19. Trastulla, L., Noorbakhsh, J., Va zquez, F., McFarland, J. & Iorio, F.
Computational estimation of quality and clinical relevance of
cancer cell lines. Mol. Syst. Biol. 18, e11017 (2022).
20. Bertotti, A. et al. The genomic landscape of response to EGFR
blockade in colorectal cancer.Nature 526,2 6 3–267 (2015).
21. Ziemke, E. K. et al. Sensitivity of KRAS-mutant colorectal cancers
to combination therapy that cotargets MEK and CDK4/6.Clin.
Cancer Res. 22,4 0 5–414 (2016).
22. Julien, S. et al. Characterization of a large panel of patient-derived
tumor xenografts representing the clinical heterogeneity of
human colorectal cancer.Clin. Cancer Res.18,5 3 1 4–5328 (2012).
23. Cho, Y. B. et al. Colorectal cancer patient-derived xenografted
tumors maintain characteristic features of the original tumors.J.
Surg. Res. 187,5 0 2–509 (2014).
24. Cayrefourcq, L. et al. Establishment and characterization of a cell
line from human circulating colon cancer cells. Cancer Res. 75,
892–901 (2015).
25. Dudová, Z. et al. The EurOPDX data portal: an open platform for
patient-derived cancer xenograft data sharing and visualization.
BMC Genom. 23, 156 (2022).
26. Byrne, A. T. et al. Interrogating open issues in cancer precision
medicine with patient-derived xenografts.Nat. Rev. Cancer 17,
254–268 (2017).
27. Kurilov, R., Haibe-Kains, B. & Brors, B. Assessment of modelling
strategies for drug response prediction in cell lines and xeno-
grafts. Sci. Rep. 10,2 8 4 9( 2 0 2 0 ) .
28. Gaujoux, R. & Seoighe, C. A ﬂexible R package for nonnegative
matrix factorization.BMC Bioinforma. 11, 367 (2010).
29. Schubert, M. et al. Perturbation-response genes reveal signaling
footprints in cancer gene expression.Nat. Commun. 9,2 0( 2 0 1 8 ) .
30. Liberzon, A. et al. The molecular signatures database (MSigDB)
hallmark gene set collection.Cell Syst. 1,4 1 7–425 (2015).
31. Najgebauer, H. et al. CELLector : genomics-guided selection of
cancer in vitro models. Cell Syst. 10,4 2 4–432.e6 (2020).
32. Tignanelli, C. J., Herrera Loeza, S. G. & Yeh, J. J. KRAS and PIK3CA
mutation frequencies in patient-derived xenograft models of
pancreatic and colorectal cancer are reﬂective of patient tumors
and stable across passages.Am. Surg. 80,8 7 3–877 (2014).
33. Julien, S., Merino-Trigo, A., Lacr oix, L., Pocard, M. Characterization
of a large panel of patient-derived tumor xenografts representing
the clinical heterogeneity of human colorectal cancercolorectal
patient. Clin. Cancer Drugs.18,5 3 1 4–5328 (2012).
34. Cheng, D. T. et al. Memorial Sloan kettering-integrated mutation
proﬁling of actionable cancer targets(MSK-IMPACT): a hybridization
capture-based next-generation sequencing clinical assay for solid
tumor molecular oncology.J. Mol. Diagn.17,2 5 1–264 (2015).
3 5 . B a t t a g l i n ,F . ,N a s e e m ,M . ,L e n z ,H . - J .&S a l e m ,M .E .M i c r o s a t e l l i t e
instability in colorectal cancer: overview of its clinical signiﬁcance
and novel perspectives.C l i n .A d v .H e m a t o l .O n c o l .16,
735–745 (2018).
36. Chang, M. T. et al. Accelerating discovery of functional mutant
alleles in cancer. Cancer Discov. 8,1 7 4–183 (2018).
37. Normanno, N. et al. Implications for KRAS status and EGFR-
targeted therapies in metastatic CRC.
Nat. Rev. Clin. Oncol. 6,
519–527 (2009).
38. Woo, X. Y. et al. Conservation of copy number pro ﬁles during
engraftment and passaging of patient-derived cancer xenografts.
Nat. Genet. 53,8 6–99 (2021).
39. Eide, P. W., Bruun, J., Lothe, R. A. & Sveen, A. CMScaller: an R
package for consensus molecularsubtyping of colorectal cancer
pre-clinical models.Sci. Rep. 7, 16618 (2017).
40. Guinney, J. et al. The consensus m olecular subtypes of colorectal
cancer. Nat. Med. 21,1 3 5 0–1356 (2015).
41. Hinoue, T. et al. Genome-scale analysis of aberrant DNA methy-
lation in colorectal cancer.Genome Res. 22,2 7 1–282 (2012).
42. Becht, E. et al. Dimensionality reduction for visualizing single-cell
data using UMAP. Nat. Biotechnol. https://doi.org/10.1038/nbt.
4314 (2018).
43. Campello, R. J. G. B., Moulavi, D. & Sander, J. Density-based
clustering based on hierarchical density estimates. InProc.
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 17

Advances In Knowledge Discovery And Data Mining (eds. Pei, J.,
T s e n g ,V . S . ,C a o ,L . ,M o t o d a ,H . ,X u ,G . )1 6 0–172 (Springer Berlin
Heidelberg, 2013).
44. Tejpar, S. et al. Prognostic and predictive relevance of primary
tumor location in patients with RAS wild-type metastatic color-
ectal cancer: retrospective analyses of the CRYSTAL and FIRE-3
trials. JAMA Oncol. 3,1 9 4–201 (2017).
45. Vogel, C. L. et al. First and subsequent cycle use of peg ﬁlgrastim
prevents febrile neutropenia in patients with breast cancer: a
multicenter, double-blind, placebo-controlled phase III study.J.
Clin. Oncol. 23, 1178–1184 (2005).
46. Yoshino, T. et al. Pan-Asian adapted ESMO consensus guidelines
for the management of patients with metastatic colorectal cancer:
a JSMO-ESMO initiative endorsed by CSCO, KACO, MOS, SSO and
TOS. Ann. Oncol. 29,4 4–70 (2018).
47. Benson, A. B. et al. Colon cancer, version 2.2021, NCCN clinical
practice guidelines in oncology.J. Natl Compr. Cancer Netw. 19,
329–359 (2021).
48. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-
based approach for interpreting genome-wide expression pro-
ﬁles. Proc. Natl Acad. Sci. USA 102,1 5 5 4 5–15550 (2005).
49. Jassal, B. et al. The reactome pathway knowledgebase. Nucleic
Acids Res. 48,D 4 9 8–D503 (2020).
50. Pernice, S. et al. CONNECTOR, ﬁtting and clustering of long-
itudinal data to reveal a new risk stratiﬁcation system. Bioinfor-
matics 39, btad201 (2023).
51. Wolpert, D. H. Stacked generalization. Neural Netw. 5,2 4 1–259
(1992).
52. Shwartz-Ziv, R. & Armon, A. Tabular data: deep learning is not all
you need. Inf. Fusion 81,8 4–90 (2022).
53. Grinsztajn, L., Oyallon, E. & Varoquaux, G. Why do tree-based
models still outperform deep learning on typical tabular data? In
NIPS’22 Conference Proceedings.5 0 7–520 (NIPS, 2022).
54. Sammut, S.-J. et al. Multi-omic machine learning predictor of
breast cancer therapy response.Nature 601,6 2 3–629 (2022).
55. van der Meer, D. et al. Cell model passports-a hub for clinical,
genetic and functional datasets of preclinical cancer models.
Nucleic Acids Res. 47,D 9 2 3–D929 (2019).
56. Seabold, S. & Perktold, J. Statsmo dels: econometric and statistical
modeling with python. In Proc. Python in Science Conference.
https://doi.org/10.25080/majora-92bf1922-011(2010).
57. Ried, T. et al. The landscape of genomic copy number alterations
in colorectal cancer and their consequences on gene expression
levels and disease outcome.Mol. Asp. Med. 69,4 8–61 (2019).
58. Rafa, L. et al. REG4 acts as a mitogenic, motility and pro-invasive
factor for colon cancer cells. Int. J. Oncol. 36,6 8 9–698 (2010).
5 9 . K a n g ,G . ,O h ,I . ,P y o ,J . ,K a n g ,D .&S o n ,B .C l i n i c o p a t h o l o g i c a l
signiﬁcance and prognostic implications of REG4 immunohisto-
chemical expression in colorectal cancer.Medicina57,9 3 8( 2 0 2 1 ) .
60. Hwang, J.-H. et al. A mutant KRAS-induced factor REG4 promotes
cancer stem cell properties via Wnt/β-catenin signaling.Int. J.
Cancer 146,2 8 7 7–2890 (2020).
61. Jonker, D. J. et al. Epiregulin gene expression as a biomarker of
beneﬁt from cetuximab in the treatment of advanced colorectal
cancer. Br. J. Cancer 110,6 4 8–655 (2014).
62. Khambata-Ford, S. et al. Expression of epiregulin and amphir-
egulin and K-ras mutation status predict disease control in meta-
static colorectal cancer patients treated with cetuximab.J. Clin.
Oncol. 25,3 2 3 0–3237 (2007).
63. Kumbrink, J. et al. p130Cas Is cor related with EREG expression and a
prognostic factor depending on colorectal cancer stage and loca-
lization reducing FOLFIRI efﬁcacy. I n t .J .M o l .S c i. 22,12364 (2021).
64. Liu, S. et al. EREG-driven oncogenesis of head and neck squamous
cell carcinoma exhibits higher sensitivity to Erlotinib therapy.
Theranostics10,1 0 5 8 9–10605 (2020).
65. Zhang, Y. et al. Epiregulin incr eases stemness-associated genes
expression and promotes chemoresistance of non-small cell lung
cancer via ERK signaling. Stem Cell Res. Ther. 13, 197 (2022).
66. Liberzon, A. et al. Molecular signatures database (MSigDB) 3.0.
Bioinformatics27,1 7 3 9–1740 (2011).
67. Park, S. H. et al. Sonic hedgehog pathway activation is associated
with cetuximab resistance and EPHB3 receptor induction in col-
orectal cancer. Theranostics9, 2235–2251 (2019).
68. Nicholls, A. Con ﬁdence limits, error bars and method comparison
in molecular modeling. Part 2: comparing methods.J. Comput.
Aided Mol. Des.
30,1 0 3–126 (2016).
69. DeLong, E. R., DeLong, D. M. & Clarke-Pearson, D. L. Comparing
the areas under two or more correlated receiver operating char-
acteristic curves: a nonparametric approach.Biometrics 44,
837–845 (1988).
7 0 . S u n ,X .&X u ,W .F a s ti m p l e m e n t a t i o no fD e L o n g’s algorithm for
comparing the areas under correlated receiver operating char-
acteristic curves.IEEE Signal. Process. Lett.21,1 3 8 9–1393 (2014).
71. Nicholls, A. Con ﬁdence limits, error bars and method comparison
in molecular modeling. Part 1: the calculation of conﬁdence
intervals.J. Comput. Aided Mol. Des. 28, 887–918 (2014).
72. Lundberg, S. M. & Lee, S.-I. A uni ﬁed approach to interpreting
model predictions. InNIPS’17 Conference Proceedings.4 7 6 8–4777
(NIPS, 2017).
73. Szklarczyk, D. et al. The STRING database in 2023: protein-protein
association networks and functional enrichment analyses for any
sequenced genome of interest.Nucleic Acids Res.51,D 6 3 8–D646
(2023).
74. Rivera, M. et al. Patient-derived xenograft (PDX) models of color-
ectal carcinoma (CRC) as a platform for chemosensitivity and
biomarker analysis in personalized medicine.Neoplasia23,2 1–35
(2021).
75. Behan, F. M. et al. Prioritization of cancer therapeutic targets using
CRISPR–Cas9 screens. Nature 568,5 1 1–516 (2019).
76. Ghandi, M. et al. Next-generati on characterization of the cancer
cell line encyclopedia.Nature 569,5 0 3–508 (2019).
7 7 . A r g e l a g u e t ,R . ,C u o m o ,A .S .E . ,S t e g l e ,O .&M a r i o n i ,J .C .C o m -
putational principles and challenges in single-cell data integra-
tion. Nat. Biotechnol.39,1 2 0 2–1215 (2021).
78. Warren, A. et al. Global computational alignment of tumor and cell
line transcriptional proﬁles. Nat. Commun. 12, 22 (2021).
79. Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V. & Gulin,
A. CatBoost: unbiased boostingwith categorical features. In
NIPS’18 Conference Proceedings. 6639
–6649 (NIPS, 2017).
80. Bishnupuri, K. S., Sainathan, S. K., Ciorba, M. A., Houchen, C. W. &
Dieckgraefe, B. K. Reg4 interacts with CD44 to regulate pro-
liferation and stemness of colorectal and pancreatic cancer cells.
Mol. Cancer Res. 20,3 8 7–399 (2022).
81. Zanella, E. R., Grassi, E. & Trusolino, L. Towards precision oncology
with patient-derived xenografts.Nat. Rev. Clin. Oncol.19,7 1 9–732
(2022).
82. Li, H. & Durbin, R. Fast and accurate short read alignment with
Burrows-Wheeler transform.Bioinformatics25,1 7 5 4–1760 (2009).
83. Bailey, M. H. et al. Comprehensive characterization of cancer
driver genes and mutations.Cell 174,1 0 3 4–1035 (2018).
84. Martincorena, I. et al. Universal patterns of selection in cancer and
somatic tissues.Cell 171,1 0 2 9–1041.e21 (2017).
85. Martínez-Jiménez, F. et al. A compendium of mutational cancer
driver genes. Nat. Rev. Cancer 20, 555–572 (2020).
8 6 . Q u i n l a n ,A .R .&H a l l ,I .M .B E D T o o l s :aﬂexible suite of utilities for
comparing genomic features.Bioinformatics26,8 4 1–842 (2010).
87. Colaprico, A. et al. TCGAbiolinks: an R/Bioconductor package for
integrative analysis of TCGA data.Nucleic Acids Res.44,e 7 1( 2 0 1 6 ) .
88. Seshan, V. E. & Olshen, A. B. DNAcopy: a package for analyzing
DNA copy data. Bioconductor Vignette(2014).
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 18

89. Beroukhim, R. et al. The landscape of somatic copy-number
alteration acrosshuman cancers. Nature 463,8 9 9–905 (2010).
90. Mermel, C. H. et al. GISTIC2.0 facilitates sensitive and con ﬁdent
localization of the targets of focal somatic copy-number alteration
in human cancers. Genome Biol. 12, R41 (2011).
91. van Dyk, E., Reinders, M. J. T. & Wessels, L. F. A. A scale-space
method for detecting recurrentDNA copy number changes with
analytical false discovery rate control.Nucleic Acids Res. 41,
e100 (2013).
92. Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner. Bioin-
formatics 29,1 5–21 (2013).
93. Tarasov, A., Vilella, A. J., Cuppen, E., Nijman, I. J. & Prins, P. Sam-
bamba: fast processing of NGS alignment formats.Bioinformatics
31,2 0 3 2–2034 (2015).
94. Wang, L., Wang, S. & Li, W. RSeQC: quality control of RNA-seq
experiments.Bioinformatics28,2 1 8 4–2185 (2012).
95. Isella, C. et al. Stromal contribution to the colorectal cancer
transcriptome.Nat. Genet. 47,3 1 2–319 (2015).
9 6 . L o v e ,M .I . ,H u b e r ,W .&A n d e r s ,S .M o d e r a t e de s t i m a t i o no ff o l d
change and dispersion for RNA-seq data with DESeq2.Genome
Biol. 15, 550 (2014).
97. Robinson, M. D., McCarthy, D. J. & Smyth, G. K. edgeR: a Bio-
conductor package for differential expression analysis of digital
gene expression data.Bioinformatics26,1 3 9–140 (2010).
98. Hänzelmann, S., Castelo, R. & Guinney, J. GSVA: gene set variation
analysis for microarray and RNA-seq data.BMC Bioinforma. 14,
7 (2013).
99. Wu, T. et al. clusterPro ﬁler 4.0: a universal enrichment tool for
interpreting omics data.Innovation2,1 0 0 1 4 1( 2 0 2 1 ) .
1 0 0 . Y u ,G . ,W a n g ,L . - G . ,H a n ,Y .&H e ,Q . - Y .c l u s t e r P r oﬁler: an R
package for comparing biological themes among gene clusters.
OMICS 16,2 8 4–287 (2012).
1 0 1 . Y u ,G . ,W a n g ,L . - G . ,Y a n ,G . - R .&H e ,Q . - Y .D O S E :a nR / B i o -
conductor package for disease ontology semantic and enrich-
ment analysis. Bioinformatics31,6 0 8–609 (2015).
102. Davis, S. & Meltzer, P. S. GEOquery: a bridge between the gene
expression omnibus (GEO) and BioConductor.Bioinformatics23
,
1846–1847 (2007).
103. Chen, Y.-A. et al. Discovery of cross-reactive probes and poly-
morphic CpGs in the Illumina Inﬁnium HumanMethylation450
microarray.Epigenetics8,2 0 3–209 (2013).
104. Needhamsen, M. et al. Usability of human In ﬁnium Methylatio-
nEPIC BeadChip for mouse DNA methylation studies.BMC Bioin-
form. 18, 486 (2017).
1 0 5 . G u j a r ,H . ,L i a n g ,J .W . ,W o n g ,N .C .&M o z h u i ,K .P r oﬁling DNA
methylation differences between inbred mouse strains on the
Illumina Human Inﬁnium MethylationEPIC microarray.PLoS ONE
13, e0193496 (2018).
106. Lawrence, M., Gentleman, R. & Carey, V. rtracklayer: an R package
for interfacing with genome browsers.Bioinformatics25,
1841–1842 (2009).
1 0 7 . M e e h a n ,T .F .e ta l .P D X - M I :m i n i m a li n f o r m a t i o nf o rp a t i e n t -
derived tumor xenograft models.Cancer Res. 77,e 6 2–e66 (2017).
108. Baralis, E., Bertotti, A., Fiori, A. & Grand, A. LAS: a software platform
to support oncological data management.J. Med. Syst. 36,
S81–S90 (2012).
109. Kaur, M. & Grag, U. ECLAT algorithm for frequent itemsets
generation. Int. J. Comput. Syst. Softw. Eng . 10, 23263–23279
(2015).
110. Buitinck, L. et al. API design for machine learning software:
experiences from the scikit-learn project. InEuropean Conference
on Machine Learning and Principles and Practices of Knowledge
Discovery in Databases(2013).
111. Virtanen, P. et al. SciPy 1.0: fundamental algorithms for scienti ﬁc
computing in Python. Nat. Methods 17,2 6 1–272 (2020).
112. Raschka, S. MLxtend: providing machine learning and data sci-
ence utilities and extensions to Python’ss c i e n t iﬁc computing
stack. J. Open Source Softw. 3,6 3 8( 2 0 1 8 ) .
113. Akiba, T., Sano, S., Yanase, T., Ohta, T. & Koyama, M. Optuna: A
Next-generation Hyperparameter Optimization Framework. In
Proc. 25th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining 2623–2631 (Association for Computing
Machinery, 2019).
1 1 4 . R o h a r t ,F . ,G a u t i e r ,B . ,S i n g h ,A .&L êC a o ,K . - A .m i x O m i c s :a nR
package for
’omics feature selection and multiple data integration.
PLoS Comput. Biol. 13, e1005752 (2017).
115. Conte, N. et al. PDX Finder: a po rtal for patient-derived tumor
xenograft model discovery.Nucleic Acids Res.47,D 1 0 7 3–D1079
(2019).
116. Vallat, R. Pingouin: statistics in Python. J. Open Source Softw. 3,
1026 (2018).
117. Perron, U. et al. Data Package for Perron et al. (Nature Commu-
nications, 2024).ﬁgshare https://doi.org/10.6084/M9.FIGSHARE.
27103786 (2024).
118. Yang, W. et al. Genomics of Drug Sensitivity in Cancer (GDSC): a
resource for therapeutic biomarker discovery in cancer cells.
Nucleic Acids Res. 41,D 9 5 5–D961 (2013).
119. Molineris, I. molinerisLab/StromaDistiller: v1.0.0.( Z e n o d o ,2 0 2 4 ) .
https://doi.org/10.5281/ZENODO.13682494.
120. Grassi, E. vodkatad/RNASeq_biod_metadata: CeSta Paper First Revi-
sion. (Zenodo, 2024).https://doi.org/10.5281/ZENODO.13682838.
121. Grassi, E. vodkatad/biodiversa_DE: CeSta Paper First Revision.
(Zenodo, 2024). https://doi.org/10.5281/ZENODO.13640241.
122. Trastulla, L. & Iorio, F. francescojm/CELLector: v2.0.0. (Zenodo,
2024). https://doi.org/10.5281/ZENODO.13629554.
Acknowledgements
This work was conducted with funding from AIRC, Associazione Itali-
ana per la Ricerca sul Cancro, Investigator Grants 20697 (to AB),
22802 (to LT) and 28772 (to FI); AIRC 5×1000 grant 21091 (to AB, EM,
and LT); AIRC/CRUK/FC AECC Accelerator Award 22795 (to LT). This
work has been partially funded by European Union (European
Research Council Consolidator - ERC) Consolidator Grants 724748
BEAT (to AB) and 101125051 DepSHOCK (to FI), H2020 grant agree-
ment no. 754923 COLOSSUS (to LT); H2020 INFRAIA grant agreement
no. 731105 EDIReX (to AB and EM). Views and opinions expressed are
however those of the author(s) only and do not necessarily re ﬂect
those of the European Union or the European Research Council. Nei-
ther the European Union nor the granting authority can be held
responsible for them. In addition, this work has been partially funded
by Fondazione Piemontese per la Ricerca sul Cancro-ONLUS, 5 × 1000
Ministero della Salute 2016 (to LT) and 2022 (to EM and LT); Italian
Ministry of Health, GR-2016 –02362726 (to CI); Italian Ministry of Uni-
versity and Research, National Recovery and Resilience Plan, project
PNC0000001 (to LT) and Ricerca Finalizzata 2021 Giovani Ricercatori,
ID. GR-2021-12375316 (to EG). AB and LT are members of the EurOPDX
Consortium. LMB PhD fellowship is funded by Nerviano Medical
Sciences.
Author contributions
U.P., E.G., A.C., N.C., U.M., L.Tru., A.B. and F.I. conceived the project and
scope. E.R.Z. derived and characterised the IRCC-PDX collection, col-
lected metadata from the original patients, coordinated by E.M., M.E.,
L.Tru. and A.B., U.P., E.G., A.C., M.V., E.K., L.M.B., L.Tra., C.I. and I.M.
processed and analysed the IRCC-PDX data. U.M., L.Tru., A.B. and F.I.
supervised IRCC-PDX data processing and analysis. H.K. and J.S.
derived, characterised, and analysed the CR-PDX collection. U.P.
designed and implemented the CeSta pipeline. U.P., E.G. and A.C.
drafted the manuscript and designed theﬁgures. U.P., E.G., A.C., L.Tru.,
A.B. and F.I. edited and revised manuscript andﬁgures. L.Tru., A.B. and
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 19

F.I. supervised the study. All authors discussed the results and con-
tributed to the ﬁnal manuscript.
Competing interests
FI receives funding from Open Targets, a public-private initiative invol-
ving academia and industry, and from Nerviano Medical Sciences and
performs consultancy for the joint Cancer Research Horizon— AstraZe-
neca Functional Genomics Centre andfor Mosaic T.X., L.T. has received
research grants from Menarini, Merck KGaA, Merus, Pﬁzer, Servier and
Symphogen. U.P. is a consultant for Omniscope Inc. H.K. and J.S. are
employee of Charles River. U.M. is an employee and holder of company
stock of AstraZeneca. All the other authors declare no competing
interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-024-53163-y.
Correspondenceand requests for materials should be addressed to
Livio Trusolino, Andrea Bertotti or Francesco Iorio.
Peer review informationNature Communicationsthanks the anon-
ymous, reviewers for their contribution to the peer review of this work. A
peer review ﬁle is available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.
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
1Human Technopole, Milano, Italy.2Candiolo Cancer Institute FPO IRCCS, Candiolo, Torino, Italy.3Department of Oncology, University of Torino, Candiolo,
Torino, Italy.4Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, UK.5Boston Children’s Hospital, Harvard Medical School, Boston, MA, USA.
6Open Targets, Wellcome Genome Campus, Hinxton, UK.7Nerviano Medical Sciences, Milan, Nerviano, Italy.8Charles River Germany GmbH,
Freiburg, Germany.9Department of Life Sciences and Systems Biology, University of Torino, Torino, Italy.10Josep Carreras Leukemia Research Institute (IJC),
Badalona, Barcelona, Catalonia, Spain.11Centro de Investigacion Biomedica en Red Cancer (CIBERONC), Madrid, Spain.12Institucio Catalana de Recerca i
Estudis Avançats (ICREA), Barcelona, Catalonia, Spain.13Physiological Sciences Department, School of Medicine and Health Sciences, University of Barcelona
(UB), Barcelona, Catalonia, Spain.14European Molecular Biology Laboratory European Bioinformatics Institute, Cambridge, UK.15Present address: Omniscope
España, Barcelona, Spain.16Present address: AstraZeneca Oncology R&D, Cambridge, UK.17These authors contributed equally: Umberto Perron, Elena Grassi,
Aikaterini Chatzipli.18These authors jointly supervised this work: Livio Trusolino, Andrea Bertotti, Francesco Iorio. e-mail: livio.trusolino@ircc.it;
andrea.bertotti@ircc.it; francesco.iorio@fht.org
Article https://doi.org/10.1038/s41467-024-53163-y
Nature Communications|         (2024) 15:9139 20