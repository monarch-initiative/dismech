---
reference_id: DOI:10.1186/s13075-025-03707-4
title: Transcriptome analysis unveils Th1 cell cycle signature as a distinctive feature of mixed connective tissue disease
authors:
- Yuichi Suwa
- Yasuo Nagafuchi
- Saeko Yamada
- Junko Maeda
- Mineto Ota
- Yumi Tsuchida
- Hirofumi Shoda
- Tomohisa Okamura
- Keishi Fujio
journal: "Arthritis Research &amp; Therapy"
year: '2025'
doi: 10.1186/s13075-025-03707-4
content_type: full_text_html
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://doi.org/10.1186/s13075-025-03707-4"
oa_status: gold
license: cc-by-nc-nd
---

# Transcriptome analysis unveils Th1 cell cycle signature as a distinctive feature of mixed connective tissue disease
**Authors:** Yuichi Suwa, Yasuo Nagafuchi, Saeko Yamada, Junko Maeda, Mineto Ota, Yumi Tsuchida, Hirofumi Shoda, Tomohisa Okamura, Keishi Fujio
**Journal:** Arthritis Research &amp; Therapy (2025)
**DOI:** [10.1186/s13075-025-03707-4](https://doi.org/10.1186/s13075-025-03707-4)

## Content

You have full access to thisopen accessarticle

1136Accesses

Explore all metrics

Mixed connective tissue disease (MCTD) is characterized by positivity for anti-U1-RNP antibodies and a combination of symptoms of systemic lupus erythematosus (SLE), systemic sclerosis (SSc), and inflammatory myositis (IIM). The aim of this study was to elucidate the similarities and differences in gene expression profiles of peripheral blood immune cells between MCTD and its related diseases, as well as their association with clinical parameters.

Transcriptome analysis was performed in peripheral blood immune cells from 19 MCTD patients, 58 SLE patients, 63 SSc patients, 64 IIM patients, and 79 healthy controls (HC), comprising a total of 283 individuals across 27 immune cell subsets. Differential gene expression and enrichment analyses were conducted to compare MCTD with related diseases and HC. The association between dysregulated pathways in MCTD and clinical parameters was assessed. Gene modular and machine learning analyses were employed to identify related gene signatures in other immune cells.

MCTD exhibited a higher number of differentially expressed genes (DEGs) in Th1 cells compared to other related diseases and HC. Although the DEGs between MCTD and SLE were limited, Th1 cells in MCTD shared common DEGs with each disease, and enrichment analysis revealed upregulation of cell cycle pathways in MCTD Th1 cells. This gene signature showed upregulation in high disease activity and in anti-U1-RNP antibody positive patients in related diseases, and it was associated with severity of Raynaud’s phenomenon. Furthermore, the Th1 cell cycle signature correlated with interferon signature in other immune cells.

Transcriptome analysis of peripheral blood immune cells revealed that MCTD Th1 cells share many transcriptional features with those in SLE, yet display distinctive cell cycle signature. Particularly, upregulation of cell cycle pathways was associated with characteristic clinical features of MCTD, such as positivity for anti-U1-RNP antibodies and Raynaud’s phenomenon. This Th1 cell cycle signature holds promise for shedding light on the underlying pathophysiology of MCTD.

Mixed connective tissue disease (MCTD) is a rare autoimmune disease. First proposed by Sharp in 1972, it is defined as a disease with positive anti-U1-ribonucleoprotein (U1-RNP) antibody and a mixture of clinical features of systemic lupus erythematosus (SLE), systemic sclerosis (SSc), and idiopathic inflammatory myositis (IIM) [1]. Characteristic features of MCTD include aseptic meningitis and trigeminal neuropathy [2]. However, the clinical presentation of MCTD patients is heterogenous, and MCTD is sometimes considered a clinical subtype of SLE, SSc, or IIM. Previous cohort studies have shown that MCTD has a high prevalence of Raynaud’s phenomenon and skin sclerosis, and the occurrence of pulmonary hypertension is related to prognosis, which are symptoms commonly associated with SSc [3]. While both MCTD and SSc are linked to a high prevalence of pulmonary hypertension, the rate of response to immunosuppressive treatment is higher in MCTD compared to SSc [4]. On the other hand, photosensitivity and malar rash, which are typical for SLE symptoms, are also observed in nearly 30% of MCTD cases [5]. According to a study of long-term follow-up of anti-U1-RNP antibody-positive cases, there were more cases finally diagnosed as SLE than SSc [6]. There is an ongoing discussion regarding whether MCTD should be regarded as a distinct disease subtype or as a clinical subtype of SLE, SSc, or IIM.

The pathophysiology of MCTD remains largely unknown. Recent reports, including ours, suggest that the peripheral blood immunophenotype of MCTD bears similarities to that of SLE [7,8]. Nevertheless, several pathophysiological studies suggest that MCTD has independent characteristics. A genetic association with MCTD was found in HLA-DR4, which is not known of having the association with SLE nor SSc [9]. Anti- survival motor neuron complex antibody was detected in 36% of MCTD patients, which was significantly higher than that in SLE (8%) or SSc (12%) [10].

Comprehensive immune cell gene expression profiling provides a deeper understanding of the pathophysiological characteristics of autoimmune diseases compared to immunophenotypic studies, which analyze a limited number of protein expressions on immune cell surfaces. Previously, in a whole blood transcriptome analysis, MCTD was classified into an interferon (IFN) cluster along with SLE and Sjogren syndrome [11]. Recently, we compiled an extensive immune cell gene expression catalog, ImmuNexUT (Immune Cell Gene Expression Atlas from the University of Tokyo) [12]. In this report, we confirmed that both MCTD and SLE exhibit similarities characterized by high IFN signatures in the transcriptome. However, the specific differences between MCTD and SLE were not explored. In this study, we utilized the large transcriptome data from ImmuNexUT to compare the RNA-seq data of 27 immune cell subsets from 19 MCTD patients with those from 59 SLE patients, 63 SSc patients, 64 IIM patients, and 79 healthy controls (HC). Our aim was to investigate unique immune cell-specific transcriptome signatures specific to MCTD. Additionally, we examined the clinical relevance and its association with other immune-cell subset signatures of the identified signature.

In this study, we first utilized the public bulk RNA-seq data E-GEAD-397 from ImmuNexUT project flagship paper (https://humandbs.biosciencedbc.jp/en/hum0214-v3) [12]. Patients and HC were recruited according to the following criteria: Patients with MCTD who fulfilled the 1996 revised version of Kasukawa’s criteria [13] were recruited. Patients clinically diagnosed as overlap syndrome were excluded. SLE cohort comprised of patients who met the 1997 revised version of ACR SLE criteria [14]. SSc cohort comprised of patients who met the 2013 American College of Rheumatology (ACR)/European League Against Rheumatism (EULAR) classification criteria for Systemic Sclerosis [15]. IIM cohort comprised of patients who met either one of following criteria: Bohan and Peter criteria [16,17], the European Neuromuscular Center criteria (Hoogendijk et al., 2004), Sontheimer criteria [18] or Griggs criteria [19]. The inclusion criteria for HC were people with no apparent co-morbidities, no direct family history of autoimmune diseases, and no use of prescription drugs or supplements. Samples were collected from the University of Tokyo, the Jikei University School of Medicine, St. Luke’s International Hospital, National Center for Global Health and Medicine and Tokyo Metropolitan Komagome Hospital with approval by the Graduate School of Medicine and Faculty of Medicine, The University of Tokyo Human Genome, Gene Analysis Research Ethics Committee (G10095) and the Ethics Committees at each site. This study was conducted in accordance with the principles of the Declaration of Helsinki. All participants gave written informed consent to study enrolment. The clinical information and treatment details of both patients and HC at the time of sample collection were compiled at the University of Tokyo and were utilized in this study.

The procedures for sample collection, processing, and sorting strategy for immune cell subsets were previously described in Ota et al., 2021 [12]. In brief, peripheral blood mononuclear cells were isolated by density gradient separation with Ficoll-Paque (GE Healthcare). Flow cytometry was used to purify 26 immune cell subsets, while neutrophils were purified using magnetic cell sorting. Flow cytometric data analyses were performed using the FlowJo software (TreeStar Inc). RNA-seq libraries were prepared using SMART-seq v4 Ultra Low Input RNA Kits (Takara Bio) and were sequenced on HiSeq2500 sequencers (Illumina). Raw reads were first processed to remove adaptor sequences using Cutadapt [20]. Reads containing too many low-quality bases (Phred quality score < 20 in more than 20% of bases) were removed. Cleaned Reads were aligned against the GRCh38 reference sequence using STAR [21] and gene expression was quantified with HTSeq [22]. We also excluded samples with low uniquely mapped read rates or unique read counts less than 6 × 106. For the quality control of RNA-seq analysis data, we calculated the correlation coefficient of the expression data between two samples belonging to the same cell subset then determined the average of the correlation coefficient (Di). Samples with a Di less than 0.9 were removed.

Linear principal component analysis (PCA) and non-linear t-distributed stochastic neighbor embedding (t-SNE) were conducted to ensure the accuracy of immune subset sorting. The t-SNE analysis was performed using the R package RtSNE (https://cran.r-project.org/web/packages/Rtsne/index.html). For PCA, genes with more than ten counts in all samples were included. The count data were normalized between samples using TMM method, converted to count per million (CPM) with edgeR package [23], log transformed and batch effects (MACS reagent in Neutrophil, study phase in other subsets) removed using the ComBat() function in the sva package [24]. The top 500 variable genes among all immune cell subsets were utilized for PCA. Additionally, t-SNE was independently performed for each subset, using the count data processed similarly to PCA.

The variance decomposition of the normalized count data was conducted using the variancePartition package [25]. The following linear mixed model was employed to calculate the fixed effect of age, daily corticosteroid intake converted to prednisolone equivalent (PSL), and random effects of sex, disease on gene expression in each immune cell subset.

MCTD was compared to three other autoimmune diseases and HC. Differentially expressed genes (DEGs) were identified for each subset using edgeR. Genes with more than ten counts in all samples were used for DEGs analysis. Raw count data were normalized by TMM approach, with age, sex, and daily corticosteroid intake as covariates. In the treatment-adjusted DEG analysis, the presence or absence of each immunosuppressant was included as an individual covariate. DEGs were detected with function glmTreat(), with the log2-fold-change threshold of ≥ 1.1 and the adjustedp-value (Benjamini-Hochberg method) < 0.25. Additionally, for each subset, a pathway enrichment analysis was performed for MSigdb gene sets C2 (curated gene sets) using with package, ReactomePA [26] and clusterProfiler [27], with adjustedp-values calculated by the Benjamini–Hochberg method.

Power analysis for DEG detection was conducted using the R package PROPER [28]. PROPER performs repeated DEG analysis simulations to evaluate the statistical power to detect genes with biologically meaningful effect sizes under varying sample size conditions. In this study, bulk RNA-seq data from the entire ImmunexUT cohort, including HC and other autoimmune diseases other than MCTD, SLE, SSc, and IIM, were randomly sampled to perform a total of 20 DEG analysis simulations. DEG analyses were performed under the same analytical conditions as described in the previous section.

A gene set variation analysis (GSVA) [29] was performed to quantify the cell cycle signature in Th1 cells. In this analysis, we evaluated expression of genes associated with the cell cycle mitotic pathway (https://www.reactome.org/content/detail/R-HSA-69278), which showed the lowest adjustedp-value in the enrichment analysis of DEGs commonly observed in Th1 cells across pairwise comparisons of MCTD versus SLE, SSc, IIM, and HC. Transcriptomic data pre-processed in the same manners as for the PCA were used for GSVA. The GSVA score for each sample was calculated and presented as the “cell cycle signature” in Fig.3.

A linear regression model was employed to assess the significance of the association between Th1 cell cycle signature and clinical factors. We analyzed samples from only SLE patients to estimate the associations of disease activity and anti-U1-RNP antibody positivity (U1-RNP) with Th1 cell cycle signature. The formula of linear regression model as follows:

All factors used in each formula were scaled for analysis.

In this study, patients with active disease were defined as either newly diagnosed untreated cases or cases experiencing a disease flare. For disease flares in MCTD, SLE and IIM, they were defined as cases requiring escalation of immunosuppressive therapy and increased glucocorticoid doses due to worsening organ involvement. In SSc, flares were defined as cases requiring modification or addition of immunosuppressive treatment due to progression of organ damage. In patients with MCTD and anti-U1-RNP antibody-positive SLE, we evaluated the severity of commonly observed symptoms at four levels (none, mild, moderate, severe) at the sampling time. Patients without symptoms were categorized as the symptom (-) group, while those with moderate or severe symptoms were classified as the symptom (+) group. The correlation coefficient with positivity for anti-U1-RNP antibody was computed for each group across each symptom.

We utilized modules generated thorough a weighted gene co-expression network analysis (WGCNA) [30] from all ImmuNexUT samples for this study. Each module was annotated based on the results of a pathway enrichment analysis of its constituent genes. The intra-modular gene network in the Th1 cell cycle module was visualized using the igraph package (https://cran.r-project.org/web/packages/igraph/index.html). Nodes with a Pearson’s correlation coefficient exceeding a threshold of 0.6 were connected by an edge. Correlations of the Th1 cell cycle modules with other modules of immune cell subsets were depicted using the qgraph package (https://cran.r-project.org/web/packages/qgraph/index.html). Modules with a correlation coefficient greater than 0.5 were plotted and connected.

The random forest algorithm was employed to identify genes that discriminate the presence of the anti-U1-RNP antibody. This analysis was conducted using the randomForest package (https://cran.r-project.org/web/packages/randomForest/index.html). RNA-seq data from patients with MCTD and stable SLE were pre-processed with the same way as PCA. Due to the limited number of samples, CM CD8, EM CD8, Fr I nTreg, Fr III T, Int Mono, NC Mono, TEMRA CD8 were omitted from this analysis. Top 500 variable genes were used for machine learning. 75% of samples were randomly selected and then used for training for prediction of anti-U1-RNP antibody positivity. The results of the training set analysis were validated on the remaining 25% of samples.

Statistical analysis was conducted using R v4.1.0. Categorical data were evaluated using Fisher’s exact probability test. For intergroup testing of quantitative variables, the Shapiro-Wilk test was performed to assess normality. The Mann-WhitneyUtest was applied if the distribution was non-normal. In cases of a normal distribution, Student’st-test was performed if there was homogeneity of variance according to anF-test, and Welch’st-test was performed if there was heterogeneity of variance. One-way ANOVA was performed to compare means across multiple groups when the data followed a normal distribution and met the assumptions of homogeneity of variances. Spearman’s rank correlation coefficient was utilized for the correlation analysis in non-normally distributed data, while Pearson’s correlation coefficient was employed for normally distributed data.

In this study, a total of 19 MCTD patients, 59 SLE patients, 63 SSc patients, 64 IIM patients, and 79 HC were analyzed (Fig.1). Table1provides a summary of clinical information for patients and HC at the time of sampling. Disease-specific clinical characteristics of patients with each autoimmune disease are shown in Supplementary Table 1. Considering variations in age, gender, and daily corticosteroid intake among MCTD patients and controls, these variables were included as covariates in the subsequent analyses. Anti-U1-RNP antibodies were detected in all MCTD cases, 39% of SLE cases, 12.7% of SSc cases, and 3.1% of IIM cases.

Overview of the study. The peripheral blood transcriptome from 19 MCTD, 59 SLE, 63 SSc, 64 IIM patients and 79 HC were utilized from ImmuNexUT data. RNA-sequencing was performed on sorted 27 immune cell subsets.HCHealthy control,MCTDMixed connective tissue disease,SLESystemic lupus erythematosus,SScSystemic sclerosis,IIMIdiopathic inflammatory myositis,Naïve CD4Naïve CD4+T cells,Mem CD4Memory CD4+T cells,Th1T helper 1 cells,Th2T helper 2 cells,Th17T helper 17 cells,TfhT follicular helper cells,Fr. I n TregFraction I naïve regulatory Tcells,Fr. II e TregFraction II effector regulatory T cells,Fr. III TFraction III non-regulatory Tcells,Naïve CD8Naïve CD8+T cells,CM CD8Central Memory CD8+T cells,EM CD8Effector Memory CD8+T cells,TEMRA CD8CD8+T effector memory CD45RA+cells,Naïve BNaïve B cells,USM BUnswitched memory B cells,SM BSwitched memory B cells,DN BDouble Negative B cells,NKNatural Killer cells,CD16p MonoCD16 positive monocytes,NC MonoNon-classical monocytes,Int MonoIntermediate monocytes,CL MonoClassical monocytes,mDCMyeloid dendritic cells,pDCPlasmacytoid dendritic cells,NeuNeutrophils,LDGLow-Density Granuocytes,DEGDifferentially Expressed Gene,GSVAGene Set Variation Analysis,WGCNAWeighted Gene Correlation Network Analysis

Initially, we conducted unsupervised dimension reduction of the data to obtain an overview and validate the transcriptome data. In PCA, samples from all cases were grouped into individual immune cell subsets, maintaining appropriate relationships along immune cell lineages (Fig.2A). Subsequently, variance partitioning was employed to assess the impact of clinical differences on gene expression within immune cell subsets (Fig.2B). Reassuringly, disease differences exhibited larger variance compared to age, gender, and corticosteroid dose. Notably, the variance of disease difference was particularly pronounced in Th1, effector memory (EM) CD8, double negative (DN) B, and two granulocytes; low density granulocyte (LDG) and neutrophils (Neu). Furthermore, we applied another dimension reduction technique to each of these immune cell subsets to confirm significant differences in the transcriptome reflecting disease differences. T-SNE showed a clear difference between HC and autoimmune diseases in every subset (Fig.2C). When we compared the distribution of MCTD patients and 3 other autoimmune disease patients, MCTD patients formed a unique cluster alongside some of SLE and IIM samples, suggesting the existence of shared MCTD-specific features in Th1 cells. In contrast, we observed scattered distribution of MCTD patients among patients with each autoimmune disease in other subsets, indicating the heterogeneity between patients.

Overview of the transcriptome.APCA of all RNA-seq samples from this study.BGene expression variance decomposition using a linear mixed model in each of immune cell subset.CtSNE of the top 5 subsets with the most pronounced variations of gene expression by the disease difference. The blue circle indicates the cluster including MCTD in Th1.PCAPrincipal Component Analysis,PSLPrednisolone,tSNEt-distributed Stochastic Neighbor Embedding

To identify gene signatures specific to MCTD, a DEG analysis was conducted in each immune cell subset. Since the number of MCTD samples was limited in this study (n= 19), a power analysis was performed to assess the reliability of DEG detection. The peak gene expression counts across immune cell subsets ranged from 320 to 640 in our ImmuNexUT dataset (Supplementary Fig. 1), and the power analysis indicated that a sample size of 10 or more provides sufficient power for DEG detection (Supplementary Fig. 2). Initially, we assessed DEGs between MCTD and each of the other autoimmune diseases (SLE, SSc, IIM) as well as HC (Fig.3A, Supplementary Table 2). Although MCTD exhibited a large number of DEGs in comparison to HC, SSc, and IIM, the number of DEGs between MCTD and SLE was limited, indicating transcriptomic similarity of MCTD and SLE. However, specific subsets, particularly Th1 cells, showed DEGs between MCTD and SLE. To account for potential effects of medication on gene expression, DEG analysis was restricted to MCTD and SLE samples with known treatment information, including treatment as a covariate. Even after this adjustment, Th1 cells exhibited the highest number of DEGs, with 99.8% of these DEGs overlapped (Supplement Fig. 3, Supplementary Table 3). Th1 cells had the highest number of common DEGs shared in the comparison of MCTD to each of other diseases and HC (Fig.3B and C, Supplementary Table 4). Pathway enrichment analysis revealed an upregulation of the cell cycle pathway in these Th1-shared DEGs (Fig.3D). Of note, all the other enriched pathways, such as the DNA replication pathway, were biologically linked to the cell cycle pathway and used overlapping signature gene sets. These results imply that Th1 cell harbors a unique cell cycle transcriptome signature of MCTD.

DEGs are most apparent in Th1 cells between MCTD and other diseases.ANumber of DEGs in each immune cell subset comparing MCTD with HC, SLE, SSc, and IIM.BNumbers of DEGs shared between MCTD and each disease/control.CVolcano plot of Th1 cell DEGs between MCTD and SLE; red, up in MCTD; blue, down in SLE; shared DEGs, pink (up) and light blue (down).DPathway enrichment of DEGs commonly detected in Th1 cells. p.adjust, adjustedp-value (Benjamini-Hochberg method)

Next, we quantified the expression of signature gene sets using GSVA to investigate the correlation of Th1 cell cycle signature with clinical features (Fig.4A). Considering that disease activity has the potential to change the gene expression of immune cells [31,32], we categorized the cases based on their disease activity. Additionally, we compared differences in signatures between cases with and without the presence of the specific antibody for MCTD, the anti-U1-RNP antibody. In SLE and IIM the Th1 cell cycle signature was upregulated in cases with high disease activity. Furthermore, in both SLE and MCTD, cases with anti-U1-RNP antibody had also showed the upregulated signature score despite their stable disease state. Although not statistically significant, cases with an active disease state of IIM and SSc and anti-U1-RNP antibody positivity tended to express higher Th1 cell cycle signatures (Fig.4B). We then evaluated whether Th1 cell expansion occurred in cases where Th1 cell cycle signature was upregulated. In HC and IIM, Th1 proportion and cell cycle signature demonstrated a negative correlation, while in MCTD, the correlation was heterogenous among cases, and there was no statistically significant correlation observed (Fig.4C).

Cell cycle signature in Th1 cells is upregulated in anti-U1-RNP positive patients.AGSVA score of cell cycle mitotic pathway in Th1 cells across diseases and HC.BCorrelation coefficients for the Th1 cell proportion per whole CD4+T cells with GSVA cell cycle signature score.CCorrelation of Th1-Cell cycle signature and flow-cytometric Th1 proportion.DCorrelation heatmap of Th1 cell cycle signature and clinical symptoms in MCTD and anti-U1-RNP antibody-positive SLE patients. *p< 0.05. by (A,B) Mann-Whitney’sUtest or Student’st-test, (C,D) Spearman’s correlation coefficient

We next evaluated the influence of disease activity and the anti-U1-RNP antibody on Th1 cell cycle signature. Since all cases of MCTD were stable and the transcriptomic features of SLE were similar to MCTD, we performed this analysis using SLE samples (Table2). The results confirm that both disease activity and the presence of anti-U1-RNP antibody play a key role in upregulation of Th1 cell cycle pathway.

We further characterized the association of the Th1 cell cycle signature with clinical symptoms in MCTD and anti-U1-RNP antibody-positive SLE patients (Fig.4D). There was a significant correlation observed between this signature score and the severity of certain symptoms such as arthritis and Raynaud’s phenomenon, which have been reported to be associated with anti-U1-RNP antibody [33]. These results suggest that the Th1 cell cycle signature is closely related to disease activity, clinical symptoms including Raynaud’s phenomenon, and the anti-U1-RNP antibody, all of which have the central roles in the pathophysiology of MCTD.

Lastly, we performed a modular analysis to explore co-expression gene networks relevant to the Th1-cell cycle pathway in other immune cell subsets. A total of 629 modules in all immune subsets were constructed. Of the nine modules in Th1, the Th1-1 module exhibited a strong correlation with the Th1 cell cycle signature (R= 0.89, Fig.5A). The hub genes in the Th1-1 module included many genes related to proteasome and ubiquitin pathways, implying the importance of these genes in the regulation of the Th1 cell cycle (Supplementary Table 5). Of note,HMGB2, whose protein has been reported to have a crucial role in activating type 1 IFN via Toll-like receptor 7 (TLR7), was included in this module. Antibodies to HMGB2 have been identified in autoimmune diseases such as SLE, Sjogren syndrome, and ANCA-associated vasculitis (Fig.5B) [34,35].

Th1 gene module of cell cycle pathway correlates with IFN signature in various immune cell subsets.AA heatmap reflecting the correlation coefficients of the Th1 gene modules, cell cycle signatures, and clinical parameters.BNetwork visualization of gene expression correlation for the top 50 hub genes of the Th1-1 cCell cycle module eigengenes.CNetwork figure of Th1-1 cell cycle module and other modules. Modules with Pearson’s correlation coefficient >0.5 correlation analysis to Th1-1 module are displayed. The strength of the correlation with other modules are indicated with the thickness of each edge. Modules composed of genes related to cell cycle pathway are depicted with yellow, modules related to IFN signaling are depicted with purple.DThe top 50 genes that are important in the machine learning prediction of anti-U1-RNP antibody-positive MCTD/SLE patients.IFNInterferon

We further investigated the correlation of this Th1-1 module to modules of various immune cell subsets. Th1-1 module showed strong correlation to modules of other immune cell subsets associated with type 1 IFN signaling (Fig.5C). Finally, we performed unbiased machine learning to investigate genes important for predicting anti-U1-RNP antibody positivity in patients with SLE or MCTD. The cell cycle pathway in Th1 and IFN related genes in subsets including myeloid cell lineage were selected as highly important genes, such asIFI44in plasmacytoid dendritic cells (pDC) andIFITM1in classical monocytes (CL Mono) (Fig.5D). These results suggest that IFN signature has a role in the induction of Th1 cell cycle signature that characterizes MCTD disease.

In this study, we investigated the transcriptomic features of MCTD using RNA-seq data from 19 MCTD cases, 186 related 3 disease controls (SLE, SSc, IIM) to MCTD, and 79 HC. Variance decomposition analysis revealed high variation in Th1 cells among disease groups (Fig.2). Additionally, differential gene expression analysis and enrichment analysis demonstrated upregulation of the cell cycle signature in Th1 cells (Fig.3). Interestingly, Th1-cell cycle signature was associated with anti-U1-RNP antibody positivity and disease activity, and it was associated with the severity of arthritis, neuralgia, and Raynaud’s phenomenon (Fig.4). While the presence of anti-U1-RNP antibodies has been clinically associated with the development of arthritis, Raynaud’s phenomenon, neuropathy, and pulmonary hypertension, their pathophysiological relationship to these clinical features remains unclear. The enhanced cell cycle signature of Th1 identified in our study may provide a potential link between these antibodies and these clinical manifestations.

A previous report stratified MCTD and SLE as similar clusters with enriched activated Th1 cells [7]. Anti-U1-RNP antibody is a specific antibody found in MCTD, and it can be also positive in some cases of SLE [36]. MCTD and SLE exhibit similarities in the transcriptome, consistent with a previous study where stratification of autoimmune diseases based on transcriptome revealed a type I IFN-enriched cluster comprising most of SLE and MCTD patients [11]. U1-RNA, a target of the anti-U1-RNP antibody, has been reported to promote type 1 IFN production by pDC through TLR7 activation, thereby supporting the survival of effector T cells [37]. In our study, Th1 proportion had negative correlations to cell cycle signature in HC, while there was no statistically significant correlation in MCTD and SLE. These results suggest that in MCTD, Th1 cells continuously upregulate cell cycle signaling and circulate systemically, whereas in healthy individuals, expanded Th1 cells migrate locally in response to limited cell cycle signaling. Although reports of Th1 enrichment in localized inflammation in MCTD are lacking, histopathological studies of cutaneous lupus have shown a correlation between type I IFN-related proteins and the number of Th1 cells in the skin [38]. While Th1 cells are generally associated with type II IFN, an in vitro study has suggested they can be induced by type I IFN under certain conditions [39]. Therefore, anti-U1-RNP antibody positivity may be involved in Th1 activation and enrichment through type I IFN. In our analysis, the Th1 cell cycle module strongly correlated with the type I IFN pathway in other cell subsets, suggesting a relationship between Th1 cell cycle signaling and type I IFN (Fig.5C). Machine learning analysis confirmed that some IFN genes strongly contribute to the prediction of anti-U1-RNP antibody-positive MCTD/SLE (Fig.5D). These anti-RNP antibody associated genes included IFN-related genes from non-Th1 subsets, as well as activation markers of Th1 cells such asCD38andHLA-DR, suggesting the pathophysiology of anti-U1-RNP antibody-positive MCTD/SLE is characterized by Th1 activation state and IFN genes. Moreover, the Th1 cell cycle signature was correlated with characteristic clinical manifestations of MCTD, such as joint swelling, neuralgia, and Raynaud’s phenomenon, in anti-U1-RNP antibody–positive cases (Fig. 4DD). Taken together, these results suggest that anti-U1-RNP antibodies may induce typical clinical features of MCTD through a characteristic interaction between Th1 cells and type I IFN (Fig.6).

Summary of this study. In MCTD, the Th1 cell cycle signature is upregulated in parallel with the type I IFN signaling and correlates with clinical manifestations associated with the disease

MCTD has a high prevalence of Raynaud’s phenomenon and skin sclerosis. In the affected skin of systemic sclerosis, a high frequency of cytotoxic CD4+T cells is reported and proposed to have a role in the vasculopathy [40]. While Th1 cells themselves are generally considered to anti-fibrotic [41], several reports suggest a plasticity of Th1 cells to cytotoxic CD4+T cells [42,43,44]. The Th1 cells with cell cycle signature could potentially contribute to the fibrotic manifestations of MCTD through differentiation to cytotoxic CD4+T cells.

Various immunosuppressive agents are available for the treatment of autoimmune diseases; however, their effects on immune cell functions and organ manifestations differ among therapeutic agents. We reported that mycophenolate mofetil (MMF) strongly influences the variance of Th1 gene expression in the transcriptome of SLE [31]. In systemic sclerosis, MMF has also been reported to improve skin fibrosis and nail fold vasculopathy [45,46]. In MCTD, it would be of great interest to evaluate the therapeutic response to MMF according to the Th1 cell cycle signature and clinical manifestations, suggesting the potential application of Th1-focused precision medicine.

This study has several limitations. Firstly, the number of MCTD cases is limited, leading to sample bias. Although machine learning methods were applied to explore potential patterns, the small sample size restricts the robustness of these analyses. Secondly, our dataset included very few patients presenting with clinical features characteristic of MCTD such as pulmonary hypertension, trigeminal neuralgia, and aseptic meningitis, and cases of MCTD with severe phenotypes were not represented. In addition, untreated MCTD cases were not available, so the potential influence of treatment on the transcriptome cannot be fully excluded, and it is challenging to distinguish the effects of disease activity from those of disease state. Furthermore, publicly available transcriptomic data of MCTD are extremely limited, making validation with independent datasets difficult. Despite the overall transcriptomic similarity between MCTD and SLE, the Th1 cell cycle signature appears to be specifically associated with clinical features characteristic of MCTD. This finding suggests that a unique proliferative program within the Th1 subset may underlie certain pathophysiological aspects of MCTD, providing new insights into its distinct disease mechanisms.

The peripheral blood cell subsets RNA-seq data are deposited in National Bioscience Database Center (NBDC) Human Database (http://humandbs.biosciencedbc.jp/en) with the accession number of E-GEAD-397. We used publicly available software for the analyses.

Sharp GC, Irvin WS, Tan EM, Gould RG, Holman HR. Mixed connective tissue disease–an apparently distinct rheumatic disease syndrome associated with a specific antibody to an extractable nuclear antigen (ENA). Am J Med. 1972;52(2):148–59.

ArticlePubMedGoogle Scholar

Tanaka Y, Kuwana M, Fujii T, Kameda H, Muro Y, Fujio K, Itoh Y, Yasuoka H, Fukaya S, Ashihara K, et al. 2019 diagnostic criteria for mixed connective tissue disease (MCTD): from the Japan research committee of the ministry of health, labor, and welfare for systemic autoimmune diseases. Mod Rheumatol. 2021;31(1):29–33.

ArticlePubMedGoogle Scholar

Pope JE. Other manifestations of mixed connective tissue disease. Rheum Dis Clin North Am. 2005;31(3):519–33. vii.

ArticlePubMedGoogle Scholar

Sanchez O, Sitbon O, Jaïs X, Simonneau G, Humbert M. Immunosuppressive therapy in connective tissue diseases-associated pulmonary arterial hypertension. Chest. 2006;130(1):182–9.

ArticlePubMedGoogle Scholar

Mosca M, Tani C, Vagnani S, Carli L, Bombardieri S. The diagnosis and classification of undifferentiated connective tissue diseases. J Autoimmun. 2014;48–49:50–2.

ArticlePubMedGoogle Scholar

Frandsen PB, Kriegbaum NJ, Ullman S, Høier-Madsen M, Wiik A, Halberg P. Follow-up of 151 patients with high-titer U1RNP antibodies. Clin Rheumatol. 1996;15(3):254–60.

ArticlePubMedGoogle Scholar

Tanaka H, Okada Y, Nakayamada S, Miyazaki Y, Sonehara K, Namba S, Honda S, Shirai Y, Yamamoto K, Kubo S, et al. Extracting immunological and clinical heterogeneity across autoimmune rheumatic diseases by cohort-wide immunophenotyping. Ann Rheum Dis. 2024;83(2):242–52.

ArticlePubMedGoogle Scholar

Izuka S, Komai T, Itamiya T, Ota M, Nagafuchi Y, Shoda H, Matsuki K, Yamamoto K, Okamura T, Fujio K. Machine learning-driven immunophenotypic stratification of mixed connective tissue disease corroborating the clinical heterogeneity. Rheumatology (Oxford) 2024.

Genth E, Zarnowski H, Mierau R, Wohltmann D, Hartl PW. HLA-DR4 and Gm(1,3;5,21) are associated with U1-nRNP antibody positive connective tissue disease. Ann Rheum Dis. 1987;46(3):189–96.

ArticlePubMedPubMed CentralGoogle Scholar

Todoroki Y, Satoh M, Kubo S, Kosaka S, Fukuyo S, Nakatsuka K, Saito K, Tanaka S, Nakayamada S, Tanaka Y. Anti-survival motor neuron complex antibodies as a novel biomarker for pulmonary arterial hypertension and interstitial lung disease in mixed connective tissue disease. Rheumatology (Oxford). 2024;63(4):1068–75.

ArticlePubMedGoogle Scholar

Barturen G, Babaei S, Català-Moll F, Martínez-Bueno M, Makowska Z, Martorell-Marugán J, Carmona-Sáez P, Toro-Domínguez D, Carnero-Montoro E, Teruel M, et al. Integrative analysis reveals a molecular stratification of systemic autoimmune diseases. Arthritis Rheumatol. 2021;73(6):1073–85.

ArticlePubMedGoogle Scholar

Ota M, Nagafuchi Y, Hatano H, Ishigaki K, Terao C, Takeshima Y, Yanaoka H, Kobayashi S, Okubo M, Shirai H, et al. Dynamic landscape of immune cell-specific gene regulation in immune-mediated diseases. Cell. 2021;184(11):3006–e30213017.

ArticlePubMedGoogle Scholar

Kasukawa R. Mixed connective tissue disease. Intern Med. 1999;38(5):386–93.

ArticlePubMedGoogle Scholar

Hochberg MC. Updating the American college of rheumatology revised criteria for the classification of systemic lupus erythematosus. Arthritis Rheum. 1997;40(9):1725.

ArticlePubMedGoogle Scholar

van den Hoogen F, Khanna D, Fransen J, Johnson SR, Baron M, Tyndall A, Matucci-Cerinic M, Naden RP, Medsger TA, Carreira PE, et al. 2013 classification criteria for systemic sclerosis: an American college of Rheumatology/European league against rheumatism collaborative initiative. Arthritis Rheum. 2013;65(11):2737–47.

ArticlePubMedPubMed CentralGoogle Scholar

Bohan A, Peter JB. Polymyositis and dermatomyositis (first of two parts). N Engl J Med. 1975;292(7):344–7.

ArticlePubMedGoogle Scholar

Bohan A, Peter JB. Polymyositis and dermatomyositis (second of two parts). N Engl J Med. 1975;292(8):403–7.

ArticlePubMedGoogle Scholar

Sontheimer RD. Would a new name hasten the acceptance of amyopathic dermatomyositis (dermatomyositis siné myositis) as a distinctive subset within the idiopathic inflammatory dermatomyopathies spectrum of clinical illness? J Am Acad Dermatol. 2002;46(4):626–36.

ArticlePubMedGoogle Scholar

Griggs RC, Askanas V, DiMauro S, Engel A, Karpati G, Mendell JR, Rowland LP. Inclusion body myositis and myopathies. Ann Neurol. 1995;38(5):705–13.

ArticlePubMedGoogle Scholar

Marcel M. Cutadapt removes adapter sequences from high-throughput sequencing reads. EMBnet J. 2011;17:5–7.

Google Scholar

Dobin A, Davis CA, Schlesinger F, Drenkow J, Zaleski C, Jha S, Batut P, Chaisson M, Gingeras TR. STAR: ultrafast universal RNA-seq aligner. Bioinformatics. 2013;29(1):15–21.

ArticlePubMedGoogle Scholar

Anders S, Pyl PT, Huber W. HTSeq–a python framework to work with high-throughput sequencing data. Bioinformatics. 2015;31(2):166–9.

ArticlePubMedGoogle Scholar

Robinson MD, McCarthy DJ, Smyth GK. EdgeR: a bioconductor package for differential expression analysis of digital gene expression data. Bioinformatics. 2010;26(1):139–40.

ArticlePubMedGoogle Scholar

Leek JT, Johnson WE, Parker HS, Jaffe AE, Storey JD. The Sva package for removing batch effects and other unwanted variation in high-throughput experiments. Bioinformatics. 2012;28(6):882–3.

ArticlePubMedPubMed CentralGoogle Scholar

Hoffman GE, Schadt EE. VariancePartition: interpreting drivers of variation in complex gene expression studies. BMC Bioinformatics. 2016;17(1):483.

ArticlePubMedPubMed CentralGoogle Scholar

Yu G, He QY. ReactomePA: an R/Bioconductor package for reactome pathway analysis and visualization. Mol Biosyst. 2016;12(2):477–9.

ArticlePubMedGoogle Scholar

Yu G, Wang LG, Han Y, He QY. ClusterProfiler: an R package for comparing biological themes among gene clusters. OMICS. 2012;16(5):284–7.

ArticlePubMedPubMed CentralGoogle Scholar

Wu H, Wang C, Wu Z. PROPER: comprehensive power evaluation for differential expression using RNA-seq. Bioinformatics. 2015;31(2):233–41.

ArticlePubMedGoogle Scholar

Hänzelmann S, Castelo R, Guinney J. GSVA: gene set variation analysis for microarray and RNA-seq data. BMC Bioinformatics. 2013;14:7.

ArticlePubMedPubMed CentralGoogle Scholar

Langfelder P, Horvath S. WGCNA: an R package for weighted correlation network analysis. BMC Bioinformatics. 2008;9:559.

ArticlePubMedPubMed CentralGoogle Scholar

Nakano M, Ota M, Takeshima Y, Iwasaki Y, Hatano H, Nagafuchi Y, Itamiya T, Maeda J, Yoshida R, Yamada S, et al. Distinct transcriptome architectures underlying lupus establishment and exacerbation. Cell. 2022;185(18):3375–e33893321.

ArticlePubMedGoogle Scholar

Takeshima Y, Iwasaki Y, Nakano M, Narushima Y, Ota M, Nagafuchi Y, Sumitomo S, Okamura T, Elkon K, Ishigaki K, et al. Immune cell multiomics analysis reveals contribution of oxidative phosphorylation to B-cell functions and organ damage of lupus. Ann Rheum Dis. 2022;81(6):845–53.

ArticlePubMedGoogle Scholar

Alves MR, Isenberg DA. Mixed connective tissue disease: a condition in search of an identity. Clin Exp Med. 2020;20(2):159–66.

ArticlePubMedPubMed CentralGoogle Scholar

Yanai H, Ban T, Wang Z, Choi MK, Kawamura T, Negishi H, Nakasato M, Lu Y, Hangai S, Koshiba R, et al. HMGB proteins function as universal sentinels for nucleic-acid-mediated innate immune responses. Nature. 2009;462(7269):99–103.

ArticlePubMedGoogle Scholar

Lewis MJ, McAndrew MB, Wheeler C, Workman N, Agashe P, Koopmann J, Uddin E, Morris DL, Zou L, Stark R, et al. Autoantibodies targeting TLR and SMAD pathways define new subgroups in systemic lupus erythematosus. J Autoimmun. 2018;91:1–12.

ArticlePubMedGoogle Scholar

Dima A, Jurcut C, Baicus C. The impact of anti-U1-RNP positivity: systemic lupus erythematosus versus mixed connective tissue disease. Rheumatol Int. 2018;38(7):1169–78.

ArticlePubMedGoogle Scholar

Paradowska-Gorycka A. U1-RNP and Toll-like receptors in the pathogenesis of mixed connective tissue diseasepart II. Endosomal TLRs and their biological significance in the pathogenesis of mixed connective tissue disease. Reumatologia. 2015;53(3):143–51.

ArticlePubMedPubMed CentralGoogle Scholar

Mathian A, Felten R, Alarcon-Riquelme ME, Psarras A, Mertz P, Chasset F, Vital EM, Arnaud L. Type 1 interferons: A target for immune-mediated inflammatory diseases (IMIDs). Joint Bone Spine. 2024;91(2):105627.

ArticlePubMedGoogle Scholar

Wenzel J, Wörenkämper E, Freutel S, Henze S, Haller O, Bieber T, Tüting T. Enhanced type I interferon signalling promotes Th1-biased inflammation in cutaneous lupus erythematosus. J Pathol. 2005;205(4):435–42.

ArticlePubMedGoogle Scholar

Maehara T, Kaneko N, Perugino CA, Mattoo H, Kers J, Allard-Chamard H, Mahajan VS, Liu H, Murphy SJ, Ghebremichael M, et al. Cytotoxic CD4 + T lymphocytes May induce endothelial cell apoptosis in systemic sclerosis. J Clin Invest. 2020;130(5):2451–64.

ArticlePubMedPubMed CentralGoogle Scholar

Truchetet ME, Brembilla NC, Chizzolini C. Current concepts on the pathogenesis of systemic sclerosis. Clin Rev Allergy Immunol. 2023;64(3):262–83.

ArticlePubMedGoogle Scholar

Elyahu Y, Hekselman I, Eizenberg-Magar I, Berner O, Strominger I, Schiller M, Mittal K, Nemirovsky A, Eremenko E, Vital A, et al. Aging promotes reorganization of the CD4 T cell landscape toward extreme regulatory and effector phenotypes. Sci Adv. 2019;5(8):eaaw8330.

ArticlePubMedPubMed CentralGoogle Scholar

Goto M, Takahashi H, Yoshida R, Itamiya T, Nakano M, Nagafuchi Y, Harada H, Shimizu T, Maeda M, Kubota A, et al. Age-associated CD4. Sci Immunol. 2024;9(93):eadk1643.

ArticlePubMedGoogle Scholar

van Leeuwen EM, Remmerswaal EB, Vossen MT, Rowshani AT, Wertheim-van Dillen PM, van Lier RA, ten, Berge IJ. Emergence of a CD4 + CD28- granzyme B+, cytomegalovirus-specific T cell subset after recovery of primary cytomegalovirus infection.J Immunol2004, 173(3):1834–1841.

Wildt M, Andréasson K, Hamberg V, Hesselstrand R, Wuttge DM. Treatment with mycophenolate mofetil is associated with improved nailfold vasculature in systemic sclerosis. Rheumatology (Oxford). 2024;63(2):385–91.

ArticlePubMedGoogle Scholar

Ohta R, Horinishi Y, Sano C, Ichinose K. Efficacy of mycophenolate mofetil in treating skin fibrosis in systemic sclerosis: A systematic review and Meta-Analysis. J Clin Med 2025; 14(12):4187.

Download references

We thank all the study participants and all the members of the recruitment sites for the collection of clinical data. The supercomputing resource SHIROKANE was provided by the Human Genome Center at The University of Tokyo.

This research was performed in collaboration with Chugai Pharmaceutical Co., Ltd.

Department of Allergy and Rheumatology, Graduate School of Medicine, the University of Tokyo, Tokyo, Japan

Yuichi Suwa, Yasuo Nagafuchi, Saeko Yamada, Junko  Maeda, Mineto Ota, Yumi Tsuchida, Hirofumi Shoda, Tomohisa Okamura & Keishi Fujio

Department of Functional Genomics and Immunological Diseases, Graduate School of Medicine, the University of Tokyo, Tokyo, Japan

Yasuo Nagafuchi, Mineto Ota & Tomohisa Okamura

Division of Rheumatology and Clinical Immunology, Department of Medicine, Jichi Medical University, Tochigi, Japan

Yasuo Nagafuchi

Department of Rheumatology, Tokyo Medical University Hospital, Tokyo, Japan

Hirofumi Shoda

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

Search author on:PubMedGoogle Scholar

YN and KF designed the study. YS analyzed the data with the help of YN, SY, and MO. YS wrote the initial manuscript with critical input from YN, SY and KF. YN, SY, JM, and MO contributed to data acquisition. YT contributed to critical reading and revision of the manuscript. HS, TO, and KF supervised the study. All authors contributed to the final version of the manuscript and approved it.

Correspondence toYasuo NagafuchiorKeishi Fujio.

This study received approval from the Ethics Committee of the University of Tokyo (approval number: G10095), and written informed consent was obtained from all participants.

Consent to Publish declaration: not applicable.

YN, MO and TO belonged to the Social Cooperation Program of the Department of Functional Genomics and Immunological Diseases, supported by Chugai Pharmaceutical.

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open AccessThis article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visithttp://creativecommons.org/licenses/by-nc-nd/4.0/.

Reprints and permissions

Suwa, Y., Nagafuchi, Y., Yamada, S.et al.Transcriptome analysis unveils Th1 cell cycle signature as a distinctive feature of mixed connective tissue disease.Arthritis Res Ther28, 5 (2026). https://doi.org/10.1186/s13075-025-03707-4

Download citation

Received:24 September 2025

Accepted:26 November 2025

Published:04 December 2025

Version of record:07 January 2026

DOI:https://doi.org/10.1186/s13075-025-03707-4

Anyone you share the following link with will be able to read this content:

Sorry, a shareable link is not currently available for this article.

Provided by the Springer Nature SharedIt content-sharing initiative

Advertisement