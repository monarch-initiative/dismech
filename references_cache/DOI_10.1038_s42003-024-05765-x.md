---
reference_id: "DOI:10.1038/s42003-024-05765-x"
title: Single-cell transcriptomic analyses of tumor microenvironment and molecular reprograming landscape of metastatic laryngeal squamous cell carcinoma
authors:
- Yuanyuan Sun
- Sheng Chen
- Yongping Lu
- Zhenming Xu
- Weineng Fu
- Wei Yan
journal: Communications Biology
year: '2024'
doi: 10.1038/s42003-024-05765-x
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s42003-024-05765-x.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s42003-024-05765-x.pdf
---

# Single-cell transcriptomic analyses of tumor microenvironment and molecular reprograming landscape of metastatic laryngeal squamous cell carcinoma
**Authors:** Yuanyuan Sun, Sheng Chen, Yongping Lu, Zhenming Xu, Weineng Fu, Wei Yan
**Journal:** Communications Biology (2024)
**DOI:** [10.1038/s42003-024-05765-x](https://doi.org/10.1038/s42003-024-05765-x)

## Content

AbstractLaryngeal squamous cell carcinoma (LSCC) is a malignant tumor with a high probability of metastasis. The tumor microenvironment (TME) plays a critical role in cancer metastasis. To gain insights into the TME of LSCC, we conducted single-cell RNA-seq (scRNA-seq) on samples collected from LSCC patients with or without lymphatic metastasis. The stem and immune cell signatures in LSCC suggest their roles in tumor invasion and metastasis. Infiltration of a large number of regulatory T cells, dysplastic plasma cells, and macrophages that are at the early development stage in the cancerous tissue indicates an immunosuppressive state. Abundant neutrophils detected at the cancer margins reflect the inflammatory microenvironment. In addition to dynamic ligand-receptor interactions between the stromal and myeloid cells, the enhanced autophagy in endothelial cells and fibroblasts implies a role in nutrient supply. Taken together, the comprehensive atlas of LSCC obtained allowed us to identify a complex yet unique TME of LSCC, which may help identify potential diagnostic biomarkers and therapeutic targets for LSCC.

ARTICLE
Single-cell transcriptomic analyses of tumor
microenvironment and molecular reprograming
landscape of metastatic laryngeal squamous cell
carcinoma
Yuanyuan Sun 1, Sheng Chen 2, Yongping Lu 3, Zhenming Xu 4 ✉, Weineng Fu 1 ✉ & Wei Yan 5,6 ✉
Laryngeal squamous cell carcinoma (LSCC) is a malignant tumor with a high probability of
metastasis. The tumor microenvironment (TME) plays a critical role in cancer metastasis. To
gain insights into the TME of LSCC, we conducted single-cell RNA-seq (scRNA-seq) on
samples collected from LSCC patients with or without lymphatic metastasis. The stem and
immune cell signatures in LSCC suggest their roles in tumor invasion and metastasis. In ﬁl-
tration of a large number of regulatory T cells, dysplastic plasma cells, and macrophages that
are at the early development stage in the cancerous tissue indicates an immunosuppressive
state. Abundant neutrophils detected at the cancer margins re ﬂect the in ﬂammatory
microenvironment. In addition to dynamic ligand-receptor interactions between the stromal
and myeloid cells, the enhanced autophagy in endothelial cells and ﬁbroblasts implies a role
in nutrient supply. Taken together, the comprehensive atlas of LSCC obtained allowed us to
identify a complex yet unique TME of LSCC, which may help identify potential diagnostic
biomarkers and therapeutic targets for LSCC.
https://doi.org/10.1038/s42003-024-05765-x OPEN
1 Department of Medical Genetics, China Medical University, Shenyang 110122, China. 2 Department of Laboratory Animal Science, China Medical
University, Shenyang 110122, China. 3 NHC Key Laboratory of Reproductive Health and Medical Genetics, Shenyang 110122, China. 4 Department of
Otolaryngology, the Fourth People ’s Hospital of Shenyang City, Shenyang 110031, China. 5 The Lundquist Institute for Biomedical Innovation at Harbor-
UCLA Medical Center, Torrance, CA 90502, USA. 6 Department of Medicine, David Geffen School of Medicine at UCLA, Los Angeles, CA 90095, USA.
✉email: zhenmingxu@cmu.edu.cn; wnfu@cmu.edu.cn; wei.yan@lundquist.org
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 1
1234567890():,;

L
aryngeal squamous cell carcinoma (LSCC) is one of the
common malignant tumors of the head and neck. The early
symptoms of LSCC are not obvious and consequently, more
than half of the patients, upon diagnosis, are already at the mid or
late stage of tumor progression with in ﬁltration and lymphatic
metastasis
1. Recurrence and metastasis are two important factors
affecting the ﬁve-year survival rate in LSCC patients 2,3. Therefore,
early diagnosis and prevention of metastasis are key to the
treatment of LSCC. Since the concept of the tumor micro-
environment (TME) emerged, it has been widely acknowledged
that TME plays a critical role in tumor progression. The TME
refers to a complex, heterogeneous composition of in ﬁltrating
immune and resident host cells, secreted factors, and extracellular
matrix. Dynamic and reciprocal interactions between cancer cells
and components of the TME lead to conditions that favor cancer
cell survival, local invasion, and metastatic dissemination. For
example, the TME can promote angiogenesis to overcome the
hypoxic and acidic microenvironment; diverse adaptive and
innate immune cells in ﬁltrate the tumor to exert either pro- or
anti-tumorigenic functions. Therefore, it is of great signi ﬁcance to
study tumor-speci ﬁc TME as it helps us not only understand
tumor progression but also identify novel targets for diagnostics
and therapeutics. Indeed, TME-based precision medicine has
drawn great attention over the last decade. In particular, perso-
nalized immunotherapies for lung cancer, ovarian cancer, and
pancreatic cancer have widely been used in clinical practice, and
consequently, the quality of life and ﬁve-year survival rate of
cancer patients have improved greatly 4–6. However, highly vari-
able outcomes among patients with various tumor types suggest
an incomplete understanding of the TME. The TME of LSCC
with lymphatic metastasis remains unclear at present, and so is
the role of TME in tumorigenesis and metastasis of LSCC.
To elucidate the TME of LSCC, we carried out the present
study with the following goals: (1) Obtain a single-cell atlas of
LSCC with lymphatic metastasis using scRNA-seq to determine
the cellular heterogeneity in LSCC. (2) Identify speci ﬁc cell sub-
clusters associated with LSCC metastasis and determine the gene
signatures that may serve as potential biomarkers for early
diagnosis and treatment. (3) Analyze copy number variations
(CNVs), transcription factors (TFs), and signaling pathways
regulating each subcluster of the epithelial cells to explore the
mechanisms of tumorigenesis. (4) Analyze the heterogeneity,
function, developmental trajectories, and key TFs of immune cells
to reveal the mechanism underlying the immune escape of LSCC.
(5) De ﬁne the cell-cell interaction networks to gain insights into
the complex cell-cell communications in the LSCC TME. To
accomplish these goals, we performed scRNA-seq analyses on
samples from LSCC patients with lymphatic metastasis using the
10X Genomics single-cell platform followed by in-depth bioin-
formatic analyses. The comprehensive atlas of LSCC obtained
allowed us to identify a complex yet unique tumor micro-
environment of laryngeal squamous cell carcinoma (LSCC) with
lymphatic metastasis.
Results
Single-cell atlas and cellular heterogeneity in metastatic LSCC .
Four types of samples were collected from six LSCC patients
undergoing surgery (Supplementary Table S1), including tumor
in situ (T), normal laryngeal mucosal epithelia adjacent to the
tumor (N), margins of cancer (R), and lymph nodes with
metastasized cancer cells (L). Histology of all of the samples was
examined using HE-staining of paraf ﬁn sections (Supplementary
Fig. S1). Single-cell suspensions were prepared immediately after
sample collection during surgery followed by scRNA-seq and in-
depth bioinformatic analyses (Fig. 1a). Quality control of the
scRNA-seq data was performed by analyzing unique molecular
identiﬁer (UMI) numbers, gene numbers, and the percentage of
mitochondrial genes per cell (Supplementary Fig. S2a –c), and
cell-cycle-related genes appeared to have no effects on cell cluster
analyses (Supplementary Fig. S2d –e). A total of 89,406 single cells
from all of the ten samples, including T, R, N, and L, were cap-
tured and sequenced (Supplementary Table S2). A total of
25 subclusters were identi ﬁed and 7 cell types were annotated,
including epithelial-derived cells (EpCs), myeloid cells, T cells, B
cells, NK cells, endothelial cells, and cancer-associated ﬁbroblasts
(CAFs) (Fig. 1b). The cell identity was further veri ﬁed by t-SNE
plots (Fig. 1c) using known marker genes, including EPCAM for
epithelial-derived cells, CD3 for T cells, CD19 for B cells, CD33
for myeloid cells, CD56 for NK cells, VEGFC for endothelial cells,
and a-SMA for ﬁbroblasts, as well as immuno ﬂuorescent staining
of these marker proteins
7 (Fig. 1d).
To reveal the cellular heterogeneity of LSCC with lymph node
metastasis, we re-clustered four major cell types, including EpCs,
T cells, B cells, and myeloid cells. We further divided T samples
into T1 and T2, representing LSCC with and without lymph node
metastasis, respectively. Eleven subclusters in epithelial-derived
cells, ten subclusters in T cells, nine subclusters in B cells, and ten
subclusters in myeloid cells were identi ﬁed (Fig. 1e). Signi ﬁcant
differences in cell numbers and cell types were observed among
all of the ﬁve types of samples (T1, T2, R, N, and L), especially in
T cells and myeloid cells (Fig. 1e, f). These data reveal a highly
complex TME that is constantly changing with the progression of
LSCC, thus validating the notion that the “tumor microenviron-
ment is not just a silent bystander, but rather an active promotor
of cancer progression ”8.
Correlations of stem and immune cell features in LSCC with
invasion and metastasis . Numerous copy number variations
(CNVs), including deletions (3q, 5p, 5q, 13p, and 13q) and copy
number gains (3p, 6q, 7q, 11q, and 12q), were detected in EpCs
(Fig. 2a). The CNV patterns allowed for classi ﬁcation of the EpCs
into malignant and non-malignant groups (Fig. 2a). Further
clustering analyses revealed 11 subclusters in the ﬁve types of
tissues (L, T1, T2, N, and R) (Fig. 2b). Clusters C0, C5, C6 and
C10 mainly existed in normal laryngeal mucosal epithelia (N);
clusters C4 and C8 in lymph nodes with metastasized LSCC (L);
clusters C1, C2, C7 and C9 in tumor in situ (T); cluster C4 in
both T and L; clusters C3, C4, C5, C6 and C10 in tumor margins
(R); clusters C1 and C2 in tumor with and without metastasis (T1
and T2). Based on differentially expressed genes (DEGs), the
functions of each subcluster were further investigated using Gene
Set Enrichment Analysis (GSEA) 9. The upregulated genes in
clusters C3, C4, C5 and C10 were mostly those that promote
proliferation (with GO terms of “mitotic sister chromosome
segregation, DNA replication, and DNA strand elongation ”) and
energy production (with GO terms of “NADH dehydrogenase,
respiratory electron transport chain, etc. ”) (Fig. 2c, d; Supple-
mentary Table S3), whereas the upregulated genes in clusters C7
(Fig. 2c, d; Supplementary Table S3) contained those usually
expressed in early embryos ( “embryonic skeletal system mor-
phogenesis and development ”). Both L and T samples displayed
downregulated genes that control the extracellular matrix, as
compared to the N and R samples (Fig. 2c, d; Supplementary
Table S3). These results suggest that the malignant cells in both L
and T samples have higher proliferative activity, lower differ-
entiation and immune chemotaxis, which may account for their
enhanced capability of invasion and metastasis.
Developmental trajectory analyses revealed that subclusters C2,
C7 and C8, which displayed stem cell features, were the initial cell
types correlated with a higher degree of malignancy and
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
2 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

metastatic potential and lower keratinization (Fig. 3a). Consis-
tently, SCENIC analyses 10 identiﬁed several key transcriptional
factors (e.g., SOX2, TWIST1, HOXC10, etc.) in subclusters C7 and
C8, which are known to be related to stem cell activities (Fig. 3b;
Supplementary Fig. S3). To identify the potential biomarkers of
LSCC invasion and metastasis, we performed Ingenuity Pathway
Analyses (IPA). The most relevant functions identi ﬁed included
cancer, organismal injury or abnormalities, endocrine disorders,
Fig. 1 A single-cell atlas and transcriptional heterogeneity of LSCC with lymphatic metastasis. a Diagram showing the work ﬂow of the present study.
b t-SNE plots showing the seven major cell types identi ﬁed in four types of tissue samples analyzed in this study. c t-SNE plots showing marker gene
expression in each of the seven cell types identi ﬁed in the four types of tissue samples analyzed in this study. Marker genes for epithelial-derived cells:
KRT15, KRT18, KRT19 and EPCAM; Marker genes for T cells: CD2, CD3D, CD3E and CD3G; Markers for B cells: CD19, CD79A, CD79B; Marker genes for
myeloid cells: CD33, CD68, CD1E, LYZ and LAMP3; marker genes for NK cells: CD56, CD16, NKP46 and NKP30; Marker genes for endothelial cells: VEGFR, TEK
and CD54; marker genes for ﬁbroblasts: alpha-SMA, FAP, and S100A4. d Immunoﬂuorescent detection of the seven marker proteins in LSCC tissue cross-
sections. Scale bars = 100 μm. e Cellular composition, and the numbers of cells, genes, and unique molecular identi ﬁers (UMIs) of all cell types in the
different types of samples examined in the present study. f t-SNE plots showing the subclusters identi ﬁed in epithelial/malignant cells, myeloid cells,
T cells, and B cells.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 3

Fig. 2 Epithelial-derived cell transcriptional heterogeneity of LSCC with lymphatic metastasis. a Chromosomal landscape of inferred CNVs
distinguishing malignant epithelial-derived cells and non-malignant epithelial-derived cells from different types of samples based on the scRNA -seq data.
The references are T cells and B cells; chromosomal ampli ﬁcations are shown in red and deletions in blue. b t-SNE plots and heat map showing the
distribution of the eleven epithelia-derived cell subclusters in the four tissue types. c Heatmap showing the top differentially expressed genes (DEGs) in
eleven epithelial-derived cell subclusters. d GSEA results showing the activated and suppressed pathways in the eleven epithelial-derived cell subclusters.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
4 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

dermatological conditions, metabolic disease, cell death and
survival, infectious disease, cellular movement, etc. (Fig. 3c).
Moreover, oxidative phosphorylation, estrogen receptor signaling,
hepatic ﬁbrosis signaling, IL-8 signaling were found to be
activated in tumors, whereas PD-L1 cancer immunotherapy
pathway, the antioxidant action of vitamin C, PTEN signaling
and PPAR signaling were inhibited (Fig. 3d). Several factors, e.g.,
ATF4, JUNB, PPRC1 and NFKBIZ, were found to promote or
Fig. 3 The stem and immune cell features in the malignant epithelial cells in LSCC. a Developmental trajectory of epithelial-derived cells, as revealed by
pseudotime analyses (Top two panels). Developmental stages (proliferation, keratinization and migration) of the 11 subclusters in the EpCs are als o shown
(Lower 11 panels). b Heatmap showing the activity of transcriptional factors (TFs) in each of the twelve subclusters of EpCs. c Diseases and functions
enrichment of DEGs. d Pathway enrichment analyses of DEGs between malignant and non-malignant epithelial cells. e Predicted activated and inhibited
upstream TFs in malignant epithelial cells in LSCC. f Graphical summary of ingenuity pathway analyses showing the most affected regulator and effectors
in malignant epithelial cells in LSCC.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 5

inhibit a large number of in ﬂammation-related genes, genes
involved in cell proliferation, invasion, cell movement and lipid
metabolism (Fig. 3e). Analyses of upstream TFs revealed
numerous TFs, e.g., GATA3, TWIST1, STAT1 and STAT2, were
signiﬁcantly activated. In contrast, some TFs, e.g., SOX7, NFIX,
and LMO2, were drastically inhibited (Fig. 3e). Overall, the most
affected regulators and effectors appeared to be related to STAT
genes and participate in the regulation of autophagy, antimicro-
bial and interferon responses (Fig. 3f; Supplementary Fig. S4a). As
the key regulators in metastasis-related EpC clusters (C7, C8)
(Supplementary Fig. S4b), STAT1 and STAT2 belong to the
STAT family and play essential roles in interferon (IFN)-signaling
in response to stimulation by cytokines, growth factors, and
hormones11–13. Of interest, the expression patterns of STAT1 and
STAT2 were variable in various cancer types (Supplementary
Fig. S4c). In head-neck squamous cell carcinoma (HNSCC),
STAT1, and STAT2 expression levels were signi ﬁcantly upregu-
lated in tumors compared to normal tissues and positively
correlated with individual cancer stage, grade, and nodal
metastasis (Supplementary Fig. S4d). STAT1 and STAT2 levels
were particularly high in tumors with in ﬁltration of immune cells,
including CD4 +T, macrophage, neutrophil, and dendritic cells
(DCs) (Supplementary Fig. S4e –g). These results suggest that
transcriptomic features of malignant cells are indicative of
invasion and metastasis of LSCC, and STAT1 and STAT2 in the
TME may participate in tumorigenesis and immune cell
inﬁltration.
T cell subcluster reprograming landscape in metastatic LSCC .
T cells are the major immune cells that ﬁght cancerous cells and
represent the dominant moderator for tumor immunity. As the
second most abundant cell type in LSCC, the T cells, may play an
important role in tumor immunity. To this end, we further
analyzed the T/NK cells by re-clustering them into 10 subclusters,
including CD8+ T cells (C0, C2 and C5), CD4 + memory T cells
(C1, C4, C6 and C7), CD4 + Tregs cells (C3) and γδ T cells (C8
and C9) 14 (Fig. 4a, b). The high degree of heterogeneity of the T
cell populations in LSCC supports the notion that LSCC has a
highly complex TME (Fig. 4c). Indeed, the four types of samples
displayed distinct cell cluster compositions, whereas the samples
without metastasis displayed similar cell cluster compositions
(Fig. 4c). The fact that tumor tissues are in ﬁltrated with a greater
number of T cells than normal tissues indicates that T cells play
an important role in tumorigenesis and development.
To discover the effects of the T cells, we performed GSEA using
the top DEGs among all of the T subclusters. GSEA data showed
that CD8 + T cells and γδ T cells displayed higher cytotoxicity
and antigen-binding activity, but CD8 + T cells showed lower
metabolism and proliferation than γδ T cells (Supplementary
Fig. S5a, b). Moreover, cluster C5 CD8 + T cells mainly existed in
the T samples, cluster C0 and C2 CD8 + T cells and C8 γδ T cells
were mostly present in the N samples, and cluster C9 γδ T cells
were mostly present in the T samples with metastasis (Fig. 4c).
Together, these data suggest that γδ T cells and CD8 + T cells
may play a key role of anti-in ﬂammation and anti-tumor, and the
CD8+ T cells appear to have been reprogrammed by the LSCC
TME, enabling malignant cells to escape immune attacks.
Of interest, a large number of Tregs (C3) were detected in the
tumor tissues, further supporting the immunosuppressive state of
the LSCC TME (Fig. 4a–c, Supplementary Fig. S5b). Consistently,
SCENIC analyses identi ﬁed several key TFs (e.g., FOXP3, NFKB
complex, SOX4, PRDM1, etc.), which are known critical regulators
of Treg characteristics (Fig. 4d; Supplementary Fig. S5c). The
GSEA results identi ﬁed increased activities of the death receptor,
tumor necrosis factor −activated receptor, and regulation of
autophagy, suggesting a high level of apoptosis (Fig. 4e;
Supplementary Fig. S5d). Therefore, the drastically increased
number of Tregs in LSCC re ﬂects a highly immune-suppressive
TME. Additionally, high levels of BATF, an important regulator
of T cells differentiated into Th17 cells 15, were observed in LSCC
(Supplementary Fig. S5e). Th17 cells are known to play different
roles in different diseases. For example, Th17 cells increase tumor
progression by activating angiogenesis and immunosuppressive
activities; Th17 cells also drive anti-tumor immune responses by
producing IFN- γ16. The balance between Th17 cells and Tregs is
believed to be critical for regulating cancer autoimmunity 16.
Aberrant developmental state of B cells in metastatic LSCC .B
cells are responsible for the humoral immunity component of
adaptive immunity. Our scRNA-seq detected abundant B cells
among the LSCC tissue samples. Re-clustering of the B cells
identiﬁed 9 subclusters, including memory B cell (cluster C2),
naive B cell (clusters C0 and C1), germinal center (GC) B cell
(clusters C3) and plasma cell (clusters C4, C8) 14 (Fig. 5a, b).
These subclusters showed different distribution patterns among
the ﬁve types of tissues analyzed (Fig. 5c). The developmental
trajectory analyses of B cells revealed that the plasma cells
represented the early development stage (Fig. 5d). GSEA detected
increased activities in complement activation, protein exit from
the endoplasmic reticulum, and SRP −dependent co-translational
protein targeting to the membrane in both clusters C4, C8, and
upregulated endoplasmic reticulum unfolded protein response in
cluster C8, suggesting compromised functions of the plasma cells
(Fig. 5e; Supplementary Fig. S6a, b). All the results implied that
the B cells in ﬁltrated failed to play the anti-tumor humoral
immunity role, which may partially explain the immune escape of
LSCC.
To identify key regulators for B cell development in LSCC, we
performed GSEA and SCENIC analyses. The pathway enrichment
results showed that glutathione metabolism, mRNA surveillance
pathway and oxidative phosphorylation were inhibited in plasma
cells (Supplementary Fig. S6b). Consistent with their function,
this ﬁnding indicates that hypoxia and oxidative free radicals
(ROS) in the TME might lead to endoplasmic reticulum stress in
plasma cells so the function of staphylococcus aureus infection
and RIG-I-like receptor signaling pathway remained suppressed
(Supplementary Fig. S6b). TF analyses identi ﬁed that XBP1 was
signiﬁcantly upregulated in plasma cells, which had been reported
to promote the accumulation of unfolded proteins in the
endoplasmic reticulum (ER) 17. TFs regulating cell proliferation,
differentiation, and apoptosis were also identi ﬁed to be
differentially expressed, e.g., KLF10, IRF4, REL, NFKB2 , etc.
(Supplementary Fig. S6c). These results suggest that B cells in the
LSCC TME display weaker anti-tumor effects due to its
endoplasmic reticulum stress and poor development and that
TFs, e.g., STAT1, XBP1, and CREB3L2, may play an important
role in regulating B cell vitality in LSCC.
Myeloid cell subcluster enrichment and reprograming land-
scape in metastatic LSCC . Myeloid cells were re-clustered into
ten subclusters and the cells were identi ﬁed as macrophages,
neutrophils, monocytes and dendritic cells (DCs) (Fig. 6a).
Clusters C0 and C1 represent neutrophils, as these cells showed
high levels of CEACAM1 and CXCR214 (Fig. 6b). Clusters C2, C4,
and C6 cells displayed abundant expression of CD14, CD163, and
APOE, thus representing macrophages (Fig. 6b). Clusters C3, C5
and C7 are monocytes based on their higher expression levels of
VCAM, FCN1 and S100A12 (Fig. 6b). Cluster C4 highly expressed
CCR7, FSCN1, and LAMP3, thus representing DCs, the most
powerful antigen-presenting cells 14 (Fig. 6b). Also, we found a
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
6 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

Fig. 4 T cell heterogeneity in LSCC with lymphatic metastasis. a t-SNE plots showing the eleven subclusters identi ﬁed in T cells of LSCC. b Marker gene
expression in the eleven T cell subclusters. c t-SNE plots and heatmap showing the distribution of the eleven T cell subclusters in the four tissue types
analyzed in the present study. d Heatmap showing the activity of TFs in the eleven T cell subclusters. e GSEA results showing pathway activation
differences among the 10 T/NK cell subclusters.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 7

Fig. 5 B cell heterogeneity in LSCC with lymphatic metastasis. a t-SNE plot showing the nine subclusters identi ﬁed in the B cells of LSCC. b Marker gene
expression in the four major B cell subtypes. c Heatmap and t-SNE plots showing the distribution of the nine B cell subclusters in the four tissue types
analyzed in the present study. d Pseudotime analyses of the developmental trajectory of the B cells detected in LSCC. e GSEA results showing pathway
activation differences among the nine B cell subclusters.
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
8 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

Fig. 6 Myeloid cell heterogeneity in LSCC with lymphatic metastasis. a t-SNE plots showing the seven subclusters detected in myeloid cells in LSCC
tissues. b Marker gene expression in the four major myeloid cell subtypes. c Heatmap and t-SNE plots showing the distribution of the ten myeloid cell
subclusters in the four tissue types analyzed in the present study. d Pseudotime analyses of the developmental trajectory of the myeloid cells detected in
LSCC. e Heatmap showing the activity of TFs in the seven myeloid cell subclusters. f GSEA results showing pathway activation differences among the
seven myeloid cell subclusters.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 9

large number of neutrophils enriched in the marginal cancer
tissues (R) and tumors with metastasis (T1), re ﬂecting an
inﬂammatory microenvironment along the cancer edges and its
importance in tumor in ﬁltration (Fig. 6b, c). In the T2 samples
(LSCC in situ without metastasis), macrophages and monocytes,
although heterogeneous, are dominant (Fig. 6c).
The developmental trajectory an alyses of myeloid cell clusters
revealed that the macrophages are at the early developmental stage
(Fig. 6d), implying that the in ﬁltrated macrophages fail to play the
anti-tumor humoral immunity role, which may partially explain the
immune escape of LSCC. The GSEA and SCENIC analyses revealed a
number of differentially activated transcription factors and pathways
related to interferon-dependent immune responses, differentiation or
activation of macrophages, cell cycle, and p53-dependent/indepen-
dent apoptosis. For example, in neutrophils, NFKB1, CREM, and
ETS1, important TFs for cell proliferation, were upregulated
signiﬁcantly (Fig. 6e). These results suggest that neutrophils tend to
undergo apoptosis. Meanwhile, levels of SPI1, MAF, and STAT1,
which are important TFs involved in the differentiation or activation
of macrophages or B cells and interferon-dependent immune
responses18, were increased signiﬁcantly in C2 and C6 macrophages
(Fig. 6e). To reveal the function of myeloid cell clusters, we
performed GSEA based on the GO database. The GO terms of
“mitochondrial inner membrane respiratory chain, rRNA processing,
and tRNA processing ” were enriched in macrophages (Fig. 6f),
indicating activation (Fig. 6f), suggesting that macrophages in the
LSCC TME display signiﬁcant activation.
Stromal cell autophagy may promote invasion and metastasis
of LSCC. In the TME of LSCC, stromal cell heterogeneity was less
prominent than immune cells, as evidenced by only two cell
clusters (one endothelial and one ﬁbroblast) identi ﬁed (Supple-
mentary Fig. S7a, b). Normal tissue also contained ﬁbroblasts and
endothelial cells and ﬁbroblasts were present in marginal LSCC
tissue (R) (Supplementary Fig. S7c). GSEA based on DEGs
between T and R uncovered enhanced autophagy (Supplementary
Fig. S7d, e), suggesting that ﬁbroblasts and endothelial cells in
LSCC have an impact on the tumor microenvironment by pro-
viding the tumor cells with nutrients, thus promoting invasion
and metastasis of LSCC.
Complex cell-cell communication networks in LSCC . Interac-
tions among EpCs, ﬁbroblasts, myeloid and endothelial cells were
investigated based on the ligand-receptor pairs in the four types
analyzed in this study using Cellchat
19. A complex intercellular
communication network appeared to exist among all major cell
types in the LSCC TME (Fig. 7a). Many ligand-receptor pairs
were detected in the epithelial cells, ﬁbroblast, endothelial cells,
and B cells in the TME of LSCC, suggesting potential interactions
between any two of these different cell types (Fig. 7b). The tumor
cells appeared to interact with most of the cell types in the TME
(Fig. 7c). For example, strong interactions existed between the
tumor cells and B cells, CD4 + T cells, CD8 + T cells or Tregs
through the lymphotoxin and lymphotoxin beta receptor (LTB-
LTBR) (Fig. 7c). Moreover, the functions of those ligand-receptor
pairs enriched among the four major cell types were analyzed,
and the enriched functions included cytokine regulation, immune
response and suppression (Fig. 7c, Supplementary Figs. S8 –11).
The complex cell-cell communication networks in the LSCC
TME suggest that the tumor cells have the ability to remodel
TME to facilitate tumor immune escape and tumor progression.
Discussion
Human Cell Atlas (HCA) and Human Tumor Atlas Network
(HTAN) projects had been launched, aiming to collect
transcriptomic data using scRNA-seq to de ﬁne key processes and
events in the development of human cancers, e.g., the transition
from precancerous lesions to malignant tumors 20,21. scRNA-seq
analyses have been used to analyze cell heterogeneity, immune
microenvironment, and drug resistance mechanisms of various
types of malignancies, including breast cancer, lymphocytes,
kidney cancer, renal cell cancers and melanoma
22–25. One
scRNA-seq study on LSCC in situ has been reported 26, but the
transcriptomic atlas of LSCC with lymphatic metastasis remains
to be determined. In the present study, we analyzed samples from
3 LSCC patients with lymphatic metastasis and 3 LSCC patients
without lymphatic metastasis to obtain the single-cell tran-
scriptomic pro ﬁles related closely to metastasis via scRNA-seq.
Our analyses identi ﬁed seven major cell types in LSCC, including
epithelial-derived cells, T lymphocytes, B lymphocytes, myeloid
cells, NK cells, endothelial cells, and cancer-associated ﬁbroblasts,
suggesting that immune cells played important roles in the TME
of LSCC. The degree of cancer heterogeneity has been correlated
with malignant features, including tumor invasion, metastasis,
drug resistance, and prognosis 27–29. The high degree of cellular
heterogeneity in LSCC suggests a complex TME of LSCC. Two of
the three cell subclusters in LSCC are potentially cancer stem cells
(CSCs) because they express higher levels of SOX2 and SOX4.
CSCs have been shown to play a critical role in tumor survival,
proliferation, metastasis, and recurrence by promoting tumor cell
survival through self-renewal and immortal proliferation 30–32.I n
addition, the identi ﬁcation of stem cell-like subclusters in lym-
phatic tissues may account for tumor immune escape in LSCC.
Our data also show that the cell subclusters associated with
invasion and metastasis display gene signatures of immune che-
motaxis and epithelial-to-mesenchymal transition (EMT), e.g.,
STAT1 and STAT2. The STAT family members have seven
conservative structural features: the N-terminal domain (ND),
coiled-coil domain (coiled-coil), DNA-binding domains (DBD),
linker domain (Linker), Src homology 2 domain (SH2) and the
C-terminal transcriptional activation domains (TAD) 11. Before
being activated, non-phosphorylated STATs bind to each other
through the ND domain to form antiparallel dimers, which
constantly shuttle between the cytoplasm and nucleus. However,
after the receptor is activated by cytokines, the phosphorylation of
the STAT proteins by JAK leads to the spatial reorganization of
the STAT dimer complex, forming active parallel dimers, which
are then separated from the receptor and transferred to the
nucleus
33. STAT1/ STAT2 has a large number of target genes,
including NO, BCL-2, p21 , and CCND1, which all participate in
pro-apoptotic and cell-cycle regulation, and act as tumor sup-
pressors in various cancers 33. Consistently, STAT1 knockout
mice display increased susceptibility to experimentally-induced
tumors and spontaneously develop mammary adenocarcinomas
and ovarian teratomas 34. Moreover, STAT1 expression and
activation are abnormal in malignant pleural mesothelioma,
pancreatic cancer, and breast cancer 35–37.P D ‑L1 and p ‑STAT1
have been found co ‑expressed in breast cancer cells, and high
p-STAT1 expression or STAT1 mRNA levels are associated with
poor outcomes and advanced clinical stages in breast cancer,
suggesting p ‑STAT1 was related to tumor immune escape 38.I n
the present study, both STAT1 and STAT2 are highly expressed
and activated in LSCC, and associated with immune cell in ﬁl-
tration, suggesting their pro-cancer function and potential
immune microenvironment remodeling functions.
Tumor progression depends on not only the degree of malig-
nant transformation but also the microenvironment in which the
tumor is located. A well-accepted hypothesis regards tumor cells
as “seeds”, and the microenvironment as “soil”, and that they
interact with each other and evolve together to promote cancer
development39. Recently, cancer immunotherapy based on the
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
10 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

immune microenvironment has developed rapidly, especially
the immune checkpoint inhibitor therapy 40,41, e.g., CTLA-4,
PD-1, etc. Although this therapeutic method has been proven
promising, the effects seem very uneven among different
patients or different cancer types. Factors such as the cell-type
composition, developmental stage, and metabolic states in the
tumor immune microenvironment all affect the effectiveness
of immunotherapy 42. The presence of a large number of T cells,
especially Tregs, abnormal plasma cells, neutrophils and M2
polarized macrophage cells in LSCC, indicates an immunosup-
pressive and pro-in ﬂammatory microenvironment.
Tregs function to regulate or suppress other cells in the
immune system by controlling the immune response to self and
foreign antigens and helping prevent autoimmune diseases. In
malignant tissues, the immunosuppressive effect of Tregs is one
of the key factors for tumor immune escape. Treg-meditated
immune tolerance is also closely related to tumor metastasis and
may serve as a potential target for immunotherapy 43. In LSCC,
the homeostasis of T cells is inhibited, whereas the apoptosis and
autophagy pathways are activated, suggesting that Tregs tend to
undergo apoptosis and autophagy. Traditionally the decrease of
Tregs would lead to the relief of anti-tumor immunosuppression.
Fig. 7 Complex intercellular communication networks in the LSCC TME. a Schematic illustration of the cell-cell interaction networks among all major cell
types identi ﬁed in the LSCC TME. b Plots showing the dominant ligand-receptor pairs expressed between eight cell-cell pairs in the LSCC TME. c Plots
showing selected interactions between the tumor cells and other major immune cell types in the LSCC TME. The interactions are mediated through ligand -
receptor pairs known to have immune functions.
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 11

However, it has been reported that the apoptotic Tregs are more
suppressive because apoptotic Tregs eliminate PD-L1 blockade-
mediated anti-tumor T cell immunity 44. In addition, the apop-
totic Tregs could quickly convert ATP into adenosine targeting
T cells and bind the receptors on the surface of T cells to affect
the T cell functions. Several reports have proposed that the role of
Tregs in cancers might be associated with in ﬂammation
45,46.
Given that Tregs appear to cause immunosuppression and pro-
mote tumor progression in LSCC, immune therapy might work
on LSCC as well.
B cells are derived from bone marrow and can differentiate into
plasma cells after antigen stimulation, followed by synthesis and
secretion of antibodies to achieve humoral immunity. In can-
cerous tissues, B cells can in ﬁltrate and form tertiary lymphoid
structures (TLSs) or germinal centers (GC), but the effect of
tumor-inﬁltrating B cells has not been fully understood. A study
on lung cancer found the adoptive transfer of B cells to tumor-
draining lymph nodes can cause tumor regression in a mouse
model of breast cancer with lung metastasis 47. Another study also
found that B cells in the tumor-draining lymph node can be
recruited to tumors, lungs, and secondary lymphoid organs
in vivo and can directly kill tumor cells through the Fas/FasL
pathway48. Analyses of the composition of immune cells in tumor
tissues from metastatic melanoma and renal cell carcinoma
cohorts have found that B cells and TLSs are positively correlated
with patients ’ responses to immunotherapy 49. In LSCC, more B
cells are present in cancerous tissues than in normal tissues.
However, effector B cells (i.e., plasma cells) in ﬁltrated LSCC tis-
sues are at the early stage of development and display enhanced
endoplasmic reticulum unfolded protein response and ubiquitin-
dependent protein catabolic process, which may explain the
compromised humoral immunity. Although the exact function of
B cells in LSCC metastasis remains unknown, these B cells may
represent a good target for developing laryngeal cancer
immunotherapy.
Derived from common myeloid progenitor cells, myeloid
lineage cells include neutrophils, basophils, eosinophils, ery-
throcytes, macrophages, monocytes, dendritic cells, granulocytes,
and megakaryocytes (platelets), which are the main component of
the natural immune system and serve as the ﬁrst line of defense
against infection
50. In addition to lymphocytes, myeloid lineage
cells are also one of the important components of tumor-
inﬁltrating immune cells, and play an important role in regulating
tumor in ﬂammation, angiogenesis, and immune cell
activation51,52. Among monocytes, neutrophils, macrophages and
DCs, macrophages and monocytes are enriched in tumor tissues,
whereas neutrophils are dominant in marginal cancer tissues, and
most of the in ﬁltrating macrophages in LSCC are abnormal
developing states. In addition to macrophages, a large number of
inﬁltrated neutrophils are present in tumor tissues, consistent
with their roles in the activation of tumor cell in ﬂammation and
chemokine-related pathways. In ﬂammation in TME is a “double-
edged sword”. On the one hand, in ﬂammatory factors, in general,
can kill pathogens, promote tissue repair, and prevent tumor
growth. On the other hand, in ﬂammation can promote tumor
growth and progression by promoting angiogenesis and metas-
tasis, subverting the anti-tumor immune response, and changing
the sensitivity of tumor cells to chemotherapeutic drugs 53.
Although the neutrophil-mediated antibacterial humoral
response is activated in LSCC TME, proper regulation of T and B
cell differentiation seems inhibited. Consequently, the role of
neutrophils in LSCC TME tends to promote tumor progression.
Stromal cells in the TME of LSCC include ﬁbroblasts and
endothelial cells. While their number is smaller than immune
cells, they appear to have more interactions with tumor cells.
Stromal cells in the tumor microenvironment regulate tumor
growth, metastasis and proliferation, and this has been veri ﬁed by
numerous studies on various cancers, including hepatocellular
carcinoma, pancreatic carcinoma, head and neck carcinoma,
colorectal carcinoma and lung carcinoma 54–59. Indeed, compared
to the center of LSCC, the stromal cells in marginal tissues display
enhanced autophagy, suggesting a potential role in promoting
tumor invasion and in ﬁltration.
In summary, the present study not only provided a compre-
hensive atlas of LSCC but also revealed the complex TME of
LSCC. Data reported here will inspire future studies on the
molecular mechanism underlying LSCC invasion and metastasis
and also facilitate the efforts in developing early diagnostics and
effective therapeutics for LSCC.
Methods
Sample collection . Laryngeal squamous cell carcinoma (LSCC)
in situ (T), normal laryngeal mucosal epithelial tissue adjacent to
LSCC (N), marginal tissue of LSCC (R), lymph nodes with
metastatic LSCC (L) from 3 LSCC patients with lymphatic
metastasis and LSCC in situ (T) from 3 LSCC patients without
lymphatic metastasis were collected from the Department of
Otolaryngology, the Fourth People ’s Hospital of Shenyang City.
All the patients gave their informed consent, and the study was
approved by the Institutional Review Board of China Medical
University in accordance with the Declaration of Helsinki. All
ethical regulations relevant to human research participants were
followed. The pathological type of each tissue was con ﬁrmed by at
least two well-trained pathologists, and the clinical characteristics
are shown in Supplementary Table S1. Immediately after surgical
removal, the tissue samples were dissected into two segments: one
was digested into a single-cell suspension for scRNA-seq; the
other one was immediately transferred into 4% paraformaldehyde
for ﬁxation and paraf ﬁn embedding for immunohistochemistry.
Preparation of single-cell suspensions . A tissue sample sub-
merged in a digestion solution containing Type II and Type IV
collagenase (Type II and Type IV from Gibco, Cat#17101015,
17104019) was cut into smaller pieces (3 mm × 3 mm) which were
then transferred to a 50 ml centrifuge tube containing 5 ml of the
digestion solution followed by incubation in a 37 °C water bath
for 30 min. After digestion, the digestion solution was passed
through a pre-wet cell sieve (70 μM, BD, cat# 431751), and the
ﬁltrate was collected into a new 50 ml centrifuge tube for cen-
trifugation at 900 × g. An aliquot of 3 ml precooled erythrocyte
lysate was added to the cell pellet to resuspend the cells followed
by incubation at room temperature for 3 min. After centrifuga-
tion (300 × g at room temperature for 10 min), an appropriate
volume of DPBS containing 2% FBS (20 μl/ml) was added to
resuspend the cells to make the ﬁnal concentration at >10,000
cells per ml. To qualify for downstream scRNA-seq analyses, a
single-cell suspension was con ﬁrmed to contain neither small cell
clusters with more than two cells adhered to each other, nor cell
debris and other particulate matters, and the cell viability was
>80%.
scRNA-seq library preparation and sequencing . The 10X
Genomics Chromium Single Cell Platform was used for scRNA-
seq. scRNA-seq libraries were generated using the Chromium
Single Cell 30 Library and Gel Bead Kit v2 (10X Genomics, PN-
120237) and the Chromium TM Single Cell A Chip Kit (10X
Genomics, PN-120236) following the manufacturer ’s protocols.
The cDNA concentration was measured using a Qubit 4 Fluo-
rometer (Thermo Fisher, Cat#Q33238) and the fragment sizes
were determined by an Agilent 2100 Bioanalyzer (Agilent, Santa
Clara, CA, USA). All samples were sequenced at multiplex
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
12 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

paired-end 150 bp on an Illumina NovaSeq 6000 sequencer with
100 G high quality of sequence reads.
scRNA-seq data processing . The sequencing data were converted
to cell expression matrix using cell Ranger software, and quality
control and statistics of the raw data were carried out for exon
ratio, second-generation sequencing Q30, barcode and UMI
numbers. Single-cell sequencing results of different samples were
combined, and the batch differences due to experiments or
sequencing and the differences in sequencing depth, UMI
expression, gene expression and the proportion of mitochondrial
ribosomes were removed. The following cells were also ﬁltered
out: (1) those with a total gene number of >6000 or <200;
(2) those with a mitochondrial gene ratio of >20%, and (3) those
with a hemoglobin gene ratio of >1%.
To evaluate cell-cycle effects, the cell-cycle score of each cell
was calculated based on the expression of cell-cycle genes
followed by principal clustering analysis (PCA). If the cell-cycle
effect was too large, it was then removed by linear regression. For
PCA dimensionality reduction and clustering, the “scaledata”
function in the Seurat package was used to normalize the data of
hypervariable genes. Louvain algorithm was used to cluster the
cells through t-SNE function in the Seurat package.
Annotation of major cell types and their subclusters . Wilcoxon
algorithm was used to analyze the marker genes for all clusters by
scoring the marker genes with one vs rest algorithm, as described
previously
14. The genes with highly speci ﬁc expression in each
cluster, logFC >0.25 and expressed in at least 20% of the cells
were selected as the signi ﬁcant marker gene of the cluster. The
cell type was annotated using single R on the basis of marker
genes, with the normal immune cell expression pro ﬁle as the
reference database. The expression status of speci ﬁc genes or gene
sets in each cell was analyzed through LOUPE software to further
identify cell subsets. Speci ﬁcally, CD8A, NKG7, GZMB, GZMH
and GNLY labeled CD8 + T cells; CD4, IL7R and CCR7 labeled
CD4+ T cells; FOXP3, KLRB1, IKZF2 and TNFRSF4 labeled
Tregs; KLRF1, XCL1 and XCL2 labeled NK cells; CD19, MS4A1,
CD79a, and CD49b labeled B cells; CD27 and CCR7 labeled
memory B cells; AICDA, RGS13, and GCSAM labeled GC B cells;
CD38, SDC1 , and MZB1 labeled plasma cells; CEACAM1 and
CXCR2 labeled neutrophils; CCR7, FSCN1 , and LAMP3 labeled
DC cells, CD14, CD163 , and APOE labeled macrophages; VCAN,
FCN1, and S 100A12 labeled monocytes. The cell differentiation
trajectories pseudotime analyses were performed using Monocle
in R package ( https://cole-trapnell-lab.github.io/monocle3).
Gene set enrichment analysis (GSEA) . Human GO and KEGG
datasets as the target gene sets were downloaded from the GESA
websites to prepare the three ﬁles that the GSEA software
9 needed
(.gct ﬁle - Gene expression scale; .cls ﬁle - information table of
each subgroup; .rnk ﬁle - gene sequencing list). The enrichment
fraction of each subgroup in different functions/pathways in
GSEA was imported, and the functional and activated signaling
pathways of the subgroup were analyzed. As the output images of
GSEA software were of poor quality and not intuitive enough, we
imported the results into R Studio to replot the heatmaps.
Single-cell regulatory network inference and clustering (SCE-
NIC) analysis . SCENIC, a computational method for simulta-
neous gene regulatory network reconstruction and cell-state
identiﬁcation from scRNA-seq data 10, was adopted in the present
study. The data from SCENIC analyses were imported into the R
Studio (pheatmap) to generate the heatmaps.
Cell-cell communication analysis . CellChat 19 was used for
analyzing intercellular communication networks based on the
receptor-ligand interactions from multiple databases. The
scRNA-seq input data for CellChat included quantitative count
data and cell-type annotation information. In brief, the percen-
tage and the average of gene expressing for each gene in the cells
were calculated. The ligand-receptor pairs were ﬁltered to obtain
receptor and ligand genes exceeding a speci ﬁed threshold (the
default is 10%). A pair-to-pair comparison was then performed
between all cell types in the dataset, and the actual mean value of
the ligand-receptor pairs between two cell types was calculated to
speculate p-value of the receptor-ligand pair in 2 cell types.
Finally, the highly speci ﬁc interactions between cell types were
arranged through the enrichment results of signi ﬁcant ligand-
receptor pairs.
Immunoﬂuorescence. Parafﬁn sections (4 μm in thickness) of the
four types of tissues (T, L, R, and N) were used for immuno-
ﬂuorescent staining. Antigen retrieval was performed by boiling
the slides with sections in Citrate Antigen Retrieval Solution (pH
6.0) for 5 min in a microwave, followed by blocking with the goat
serum for 15 min at room temperature. The ﬁrst antibodies used
included EPCAM (for epithelial-derived cells at a dilution of
100X, Abcam, Cat#ab223582), CD3 (T cells at a dilution of 50×,
Abcam, Cat#ab135372), CD19 (for B cells at a dilution of 50×,
Abcam, Cat#ab245235), CD33 (myeloid cells at a dilution of 50×,
Abcam, Cat#ab269456), CD56 (NK cells at a dilution of 50×,
Abcam, Cat#ab220360), VEGFC (for endothelial cells at a dilu-
tion of 50×, Abcam, Cat#ab83905), a-SMA (cancer-associated
ﬁbroblasts at a dilution of 200×, Cell Signaling Technology,
Cat#19245), STAT1 (diluted at 100×, Abcam, Cat#ab239360),
STAT2 (diluted at 100×, Abcam, Cat#ab32367), OCT4 (stem cells
at a dilution of 100×, Abcam, Cat#ab181557), SOX2 (stem cells at
a dilution of 100×, Abcam, Cat#ab97959). CoraLite488 or Cor-
aLite594 Conjugated Antibodies were used as secondary anti-
bodies, and DAPI was used to counter-stain the nucleus.
Immunoﬂuorescent images were taken using a microscope
(Nikon, A1R) equipped with imaging software (NIS-Elements
Viewer, 5.21.00_b1483, Nikon).
Copy number variation (CNV) and benign/malignant analysis
of epithelial-derived cells . The CNV analyses were carried out via
importing the data, including the original matrix of scRNA-seq, the
reference, and gene or chromosome location information into the
inferred CNV software to analyze the CNV information by com-
paring the gene expression value in each of cell types with the
reference cell (i.e., normal immune cells). The benign/malignant
analysis of each cell was also based on the CNV value compared to
the reference value by scCancer software, and the cells are scored
based on the changes in overall gene copy number (i.e., malign score).
Ingenuity pathway analysis . From the differentially expressed
genes in the epithelial-derived cells between groups T and N,
3,000 genes with the largest difference were selected and uploaded
to IPA (Qiagen, https://www.qiagenbioinformatics.com/products/
ingenuity-pathway-analysis/). The canonical pathway, interaction
network, disease, functions, and upstream regulatory factors were
analyzed.
Statistics and reproducibility . R and R Studio software (version
4.0.2, R Foundation for Statistical Computing, Vienna, Austria;
http://www.r-project.org) ware used for statistical analysis and
data visualization including Louvain algorithm, SCENIC, CNV
analyses, CellChat. Z-score and P-value were used to judge sta-
tistically signi ﬁcant. |z-score|>2 is considered meaningful. The
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 13

positive and negative Z-scores indicate activated and suppressed
molecular interactions, respectively. P-values < 0.05 were con-
sidered statistically signi ﬁcant.
Reporting summary . Further information on research design is
available in the Nature Portfolio Reporting Summary linked to
this article.
Data availability
The scRNA-seq data have been deposited into the National Center for Biotechnology
Information Sequence Read Achieve database (accession no. GES206332). All source data
behind graphs in Figs. 1–7 can be found in Supplementary Data 1. Any other data are
available from the corresponding author upon reasonable request.
Received: 15 December 2022; Accepted: 2 January 2024;
References
1. Nocini, R., Molteni, G., Mattiuzzi, C. & Lippi, G. Updates on larynx cancer
epidemiology. Chin. J. Cancer Res. 32,1 8 –25 (2020).
2. Steuer, C. E., El-Deiry, M., Parks, J. R., Higgins, K. A. & Saba, N. F. An update
on larynx cancer. CA Cancer J. Clin. 67,3 1 –50 (2017).
3. Bollig, C., Ahmad, J. & Dooley, L. Effect of medical comorbidities on
treatment regimen and survival in T3/T4 laryngeal cancer. Laryngoscope 130,
1459–1464 (2020).
4. Ruiz-Cordero, R. & Devine, W. P. Targeted therapy and checkpoint
immunotherapy in lung cancer. Surg. Pathol. Clin. 13,1 7 –33 (2020).
5. Yang, C. et al. Immunotherapy for ovarian cancer: adjuvant, combination, and
neoadjuvant. Front. Immunol. 11, 577869 (2020).
6. Morrison, A. H., Byrne, K. T. & Vonderheide, R. H. Immunotherapy and
prevention of pancreatic cancer. Trends Cancer 4, 418 –428 (2018).
7. Jin, S. et al. Single-cell transcriptomic analysis de ﬁnes the interplay between
tumor cells, viral infection, and the microenvironment in nasopharyngeal
carcinoma. Cell Res. 30, 950 –965 (2020).
8. Hinshaw, D. C. & Shevde, L. A. The tumor microenvironment innately
modulates cancer progression. Cancer Res. 79, 4557 –4566 (2019).
9. Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based
approach for interpreting genome-wide expression pro ﬁles. Proc. Natl Acad.
Sci. USA 102, 15545 –15550 (2005).
10. Aibar, S. et al. SCENIC: single-cell regulatory network inference and
clustering. Nat. Methods 14, 1083 –1086 (2017).
11. Verhoeven, Y. et al. The potential and controversy of targeting STAT family
members in cancer. Semin. Cancer Biol. 60,4 1 –56 (2020).
12. Ivashkiv, L. B. & Donlin, L. T. Regulation of type I interferon responses. Nat.
Rev. Immunol. 14,3 6 –49 (2014).
13. O ’Shea, J. J. et al. The JAK-STAT pathway: impact on human disease and
therapeutic intervention. Annu. Rev. Med. 66, 311 –328 (2015).
14. Hu, C. et al. CellMarker 2.0: an updated database of manually curated cell
markers in human/mouse and web tools based on scRNA-seq data. Nucleic
Acids Res.
51, D870 –D876 (2023).
15. Shetty, A. et al. A systematic comparison of FOSL1, FOSL2, and BATF-
mediated transcriptional regulation during early human Th17 differentiation.
Nucleic Acids Res. 50, 4938 –4958 (2022).
16. Knochelmann, H. M. et al. When worlds collide: Th17 and Treg cells in cancer
and autoimmunity. Cell Mol. Immunol. 15, 458 –469 (2018).
17. Chopra, S. et al. IRE1-XBP1 signaling in leukocytes controls prostaglandin
biosynthesis and pain. Science 365, eaau6499 (2019).
18. Liu, M. et al. Transcription factor c-Maf is a checkpoint that programs
macrophages in lung cancer. J. Clin. Invest. 130, 2081 –2096 (2020).
19. Jin, S. et al. Inference and analysis of cell-cell communication using CellChat.
Nat. Commun. 12, 1088 (2021).
20. Weber, G. M., Ju, Y. & Börner, K. Considerations for using the vasculature as a
coordinate system to map all the cells in the human body. Front. Cardiovasc.
Med. 7, 29 (2020).
21. Rozenblatt-Rosen, O. et al. The human tumor atlas network: charting tumor
transitions across space and time at single-cell resolution.Cell 181,2 3 6–249 (2020).
22. Ding, S., Chen, X. & Shen, K. Single-cell RNA sequencing in breast cancer:
understanding tumor heterogeneity and paving roads to individualized
therapy. Cancer Commun. 40, 329 –344 (2020).
23. Ren, X. & Zhang, Z. Understanding tumor-in ﬁltrating lymphocytes by single
cell RNA sequencing. Adv. Immunol. 144, 217 –245 (2019).
24. Zhang, Y. et al. Single-cell analyses of renal cell cancers reveal insights into
tumor microenvironment, cell of origin, and therapy response. Proc. Natl
Acad. Sci. USA 118, e2103240118 (2021).
25. Durante, M. A. et al. Single-cell analysis reveals new evolutionary complexity
in uveal melanoma. Nat. Commun. 11, 496 (2020).
26. Song, L. et al. Cellular heterogeneity landscape in laryngeal squamous cell
carcinoma. Int J. Cancer 147, 2879 –2890 (2020).
27. Jiang, H. et al. Revealing the transcriptional heterogeneity of organ-speci ﬁc
metastasis in human gastric cancer using single-cell RNA Sequencing. Clin.
Transl. Med. 12, e730 (2022).
28. Zhang, A., Miao, K., Sun, H. & Deng, C. X. Tumor heterogeneity reshapes the
tumor microenvironment to in ﬂuence drug resistance. Int. J. Biol. Sci. 18,
3019–3033 (2022).
29. Vitale, I., Shema, E., Loi, S. & Galluzzi, L. Intratumoral heterogeneity in cancer
progression and response to immunotherapy.
Nat. Med. 27, 212 –224 (2021).
30. Ku şoğlu, A. & Biray Avc ı, Ç. Cancer stem cells: a brief review of the current
status. Gene 681,8 0 –85 (2019).
31. Babaei, G., Aziz, S. G. & Jaghi, N. Z. Z. EMT, cancer stem cells and autophagy;
The three main axes of metastasis. Biomed. Pharmacother. 133, 110909 (2021).
32. Chang, J. C. Cancer stem cells: Role in tumor growth, recurrence, metastasis,
and treatment resistance. Medicine 95, S20 –S25 (2016).
3 3 . Z h a n g ,Y .&L i u ,Z .S T A T 1i nc a n c e r :f r i e n do rf o e ?Discov. Med.24,1 9–29 (2017).
34. Chan, S. R. et al. STAT1-de ﬁcient mice spontaneously develop estrogen
receptor alpha-positive luminal mammary carcinomas. Breast Cancer Res. 14,
R16 (2012).
35. Arzt, L., Halbwedl, I., Gogg-Kamerer, M. & Popper, H. H. Signal transducer
and activator of transcription 1 (STAT1) acts like an oncogene in malignant
pleural mesothelioma. Virchows Arch. 465,7 9 –88 (2014).
36. Sun, Y., Yang, S., Sun, N. & Chen, J. Differential expression of STAT1 and p21
proteins predicts pancreatic cancer progression and prognosis. Pancreas 43,
619–623 (2014).
37. Koromilas, A. E. & Sexl, V. The tumor suppressor function of STAT1 in breast
cancer. JAKSTAT 2, e23353 (2013).
38. Suzuki, Y., Nakazawa, T., Ichikawa, D. & Kono, K. Phospho-STAT1
expression as a potential biomarker for anti-PD-1/anti-PD-L1
immunotherapy for breast cancer. Int J. Oncol. 54, 2030 –2038 (2019).
39. Langley, R. R. & Fidler, I. J. The seed and soil hypothesis revisited-the role of
tumor-stroma interactions in metastasis to different organs. Int J. Cancer 128,
2527–2535 (2011).
40. Alsaab, H. O. et al. PD-1 and PD-L1 checkpoint signaling inhibition for
cancer immunotherapy: mechanism, combinations, and clinical outcome.
Front Pharmacol. 8, 561 (2017).
41. Rotte, A. Combination of CTLA-4 and PD-1 blockers for treatment of cancer.
J. Exp. Clin. Cancer Res. 38, 255 (2019).
42. Wu, T. & Dai, Y. Tumor microenvironment and therapeutic response. Cancer
Lett. 387,6 1 –68 (2017).
43. Yan, S., Zhang, Y. & Sun, B. The function and potential drug targets of
tumour-associated Tregs for cancer immunotherapy. Sci. China Life Sci. 62,
179–186 (2019).
44. Maj, T. et al. Oxidative stress controls regulatory T cell apoptosis and
suppressor activity and PD-L1-blockade resistance in tumor. Nat. Immunol.
18, 1332 –1341 (2017).
45. Sharma, A. et al. Anti-CTLA-4 immunotherapy does not deplete FOXP3( +)
regulatory T Cells (Tregs) in human cancers. Clin. Cancer Res. 25, 1233–1238
(2019).
46. Wang, H., Franco, F. & Ho, P. C. Metabolic regulation of tregs in cancer:
opportunities for immunotherapy. Trends Cancer 3, 583 –592 (2017).
47. Li, Q. et al. Adoptive transfer of tumor reactive B cells confers host T-cell
immunity and tumor regression. Clin. Cancer Res. 17, 4987 –4995 (2011).
48. Tao, H. et al. Antitumor effector B cells directly kill tumor cells via the Fas/FasL
pathway and are regulated by IL-10. Eur. J. Immunol. 45,9 9 9–1009 (2015).
49. Helmink, B. A. et al. B cells and tertiary lymphoid structures promote
immunotherapy response. Nature 577, 549 –555 (2020).
50. Geissmann, F. et al. Development of monocytes, macrophages, and dendritic
cells. Science 327, 656 –661 (2010).
51. Mantovani, A., Sozzani, S., Locati, M., Allavena, P. & Sica, A. Macrophage
polarization: tumor-associated macrophages as a paradigm for polarized M2
mononuclear phagocytes. Trends Immunol. 23, 549 –555 (2002).
52. Wang, S. et al. Metabolic reprogramming of macrophages during infections
and cancer. Cancer Lett. 452,1 4 –22 (2019).
53. Xia, Y. et al. Engineering macrophages for cancer immunotherapy and drug
delivery. Adv. Mater. 32, e2002054 (2020).
54. Ai, J. et al. Mesenchymal stromal cells induce inhibitory effects on
hepatocellular carcinoma through various signaling pathways. Cancer Cell Int.
19, 329 (2019).
55. Tian, C. et al. Proteomic analyses of ECM during pancreatic ductal
adenocarcinoma progression reveal different contributions by tumor and
stromal cells. Proc. Natl Acad. Sci. USA 116, 19609 –19618 (2019).
ARTICLE COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x
14 COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio

56. Puram, S. V. et al. Single-cell transcriptomic analysis of primary and
metastatic tumor ecosystems in head and neck cancer. Cell 171,
1611–1624.e24 (2017).
57. Zhou, Y. et al. Single-cell multiomics sequencing reveals prevalent genomic
alterations in tumor stromal cells of human colorectal cancer. Cancer Cell 38,
818–828 (2020).
58. Kim, N. et al. Single-cell RNA sequencing demonstrates the molecular and
cellular reprogramming of metastatic lung adenocarcinoma. Nat. Commun.
11, 2285 (2020).
59. Bertero, T. et al. Tumor-stroma mechanics coordinate amino acid availability
to sustain tumor growth and malignancy. Cell Metab. 29, 124 –140 (2019).
Acknowledgements
This work was supported by the National Natural Science Foundation of China
(81372876 to WF), Liaoning Science and Technology Project (2021JH6/10500157 and
LQNK201726 to WF and YS). Shanghai Biotechnology Corporation is acknowledged for
its help with sequencing and bioinformatic analyses of the data.
Author contributions
W.Y. and W.F. designed the research. Y.S. performed the experiments. Y.S., W.F., and
W.Y. analyzed the data. S.C., Y.L., and Z.X. helped collect samples and provided the
clinical data. Y.S. and W.Y. wrote the manuscript. All authors have read and approved
the ﬁnal submitted manuscript.
Competing interests
The authors declare no competing interests.
Ethical approval
All patients gave their informed consent, and the study was approved by the Institutional
Review Board of China Medical University in accordance with the Declaration of
Helsinki.
Additional information
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1038/s42003-024-05765-x.
Correspondence and requests for materials should be addressed to Zhenming Xu,
Weineng Fu or Wei Yan.
Peer review information Communications Biology thanks Takahiro Tsujikawa and the
other, anonymous, reviewer(s) for their contribution to the peer review of this work.
Primary Handling Editor: Christina Karlsson-Rosenthal. A peer review ﬁle is available.
Reprints and permission information is available at http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional af ﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if changes were made. The images or other third party
material in this article are included in the article ’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder. To view a copy of this licence, visit http://creativecommons.org/
licenses/by/4.0/.
© The Author(s) 2024
COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-024-05765-x ARTICLE
COMMUNICATIONS BIOLOGY |            (2024) 7:63 | https://doi.org/10.1038/s42003-024-05765-x | www.nature.com/commsbio 15