---
reference_id: DOI:10.1038/s41413-022-00237-6
title: Characterizing the tumor microenvironment at the single-cell level reveals a novel immune evasion mechanism in osteosarcoma
authors:
- Weijian Liu
- Hongzhi Hu
- Zengwu Shao
- Xiao Lv
- Zhicai Zhang
- Xiangtian Deng
- Qingcheng Song
- Yong Han
- Tao Guo
- Liming Xiong
- Baichuan Wang
- Yingze Zhang
journal: Bone Research
year: '2023'
doi: 10.1038/s41413-022-00237-6
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41413-022-00237-6.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41413-022-00237-6.pdf
---

# Characterizing the tumor microenvironment at the single-cell level reveals a novel immune evasion mechanism in osteosarcoma
**Authors:** Weijian Liu, Hongzhi Hu, Zengwu Shao, Xiao Lv, Zhicai Zhang, Xiangtian Deng, Qingcheng Song, Yong Han, Tao Guo, Liming Xiong, Baichuan Wang, Yingze Zhang
**Journal:** Bone Research (2023)
**DOI:** [10.1038/s41413-022-00237-6](https://doi.org/10.1038/s41413-022-00237-6)

## Content

AbstractThe immune microenvironment extensively participates in tumorigenesis as well as progression in osteosarcoma (OS). However, the landscape and dynamics of immune cells in OS are poorly characterized. By analyzing single-cell RNA sequencing (scRNA-seq) data, which characterize the transcription state at single-cell resolution, we produced an atlas of the immune microenvironment in OS. The results suggested that a cluster of regulatory dendritic cells (DCs) might shape the immunosuppressive microenvironment in OS by recruiting regulatory T cells. We also found that major histocompatibility complex class I (MHC-I) molecules were downregulated in cancer cells. The findings indicated a reduction in tumor immunogenicity in OS, which can be a potential mechanism of tumor immune escape. Of note, CD24 was identified as a novel “don’t eat me” signal that contributed to the immune evasion of OS cells. Altogether, our findings provide insights into the immune landscape of OS, suggesting that myeloid-targeted immunotherapy could be a promising approach to treat OS.

ARTICLE OPEN
Characterizing the tumor microenvironment at the single-cell
level reveals a novel immune evasion mechanism in
osteosarcoma
Weijian Liu 1,2, Hongzhi Hu 1,2, Zengwu Shao 1, Xiao Lv 1, Zhicai Zhang 1, Xiangtian Deng 3, Qingcheng Song 3,4,5, Yong Han 6, Tao Guo 7,
Liming Xiong 1 ✉, Baichuan Wang 1 ✉ and Yingze Zhang 1,2,3,4 ✉
The immune microenvironment extensively participates in tumorigenesis as well as progression in osteosarcoma (OS). However, the
landscape and dynamics of immune cells in OS are poorly characterized. By analyzing single-cell RNA sequencing (scRNA-seq) data,
which characterize the transcription state at single-cell resolution, we produced an atlas of the immune microenvironment in OS.
The results suggested that a cluster of regulatory dendritic cells (DCs) might shape the immunosuppressive microenvironment in
OS by recruiting regulatory T cells. We also found that major histocompatibility complex class I (MHC-I) molecules were
downregulated in cancer cells. The ﬁndings indicated a reduction in tumor immunogenicity in OS, which can be a potential
mechanism of tumor immune escape. Of note, CD24 was identi ﬁed as a novel “don’t eat me” signal that contributed to the immune
evasion of OS cells. Altogether, our ﬁndings provide insights into the immune landscape of OS, suggesting that myeloid-targeted
immunotherapy could be a promising approach to treat OS.
Bone Research            (2023) 11:4 ; https://doi.org/10.1038/s41413-022-00237-6
INTRODUCTION
Osteosarcoma (OS), a common primary malignant bone tumor,
mainly occurs in children and teenagers.
1 Advances in surgical
technology and neoadjuvant chemotherapy have signi ﬁcantly
increased the overall survival rate of OS. Nevertheless, improving
the survival rate of recurrent and metastatic diseases still remains a
challenge (less than 30% within two years).
2 Immune checkpoint
blockade (ICB) is regarded as a promising therapy for numerous solid
tumors, including melanoma, non-small cell lung cancer and kidney
cancer.
3 Recently, immune checkpoint inhibitors that target PD-1 or
CTLA-4 have also been tested in OS. 4– 6 However, only a limited
number of patients have demonstrated a response to anti-PD-1
immunotherapy in recent clinical trials. Moreover, the impact of anti-
CTLA-4 immunotherapy in clinical application for OS remains unclear.
7
In OS, cancer cells interact with both immune cells and stromal
cells to form an immunosuppressive tumor microenvironment
(TME), thus enhancing cancer cell immune evasion. The inter-
tumoral heterogeneity is also an important feature of OS, leading
to treatment resistance and divergent therapeutic outcomes
among patients.
8 Understanding cancer cell heterogeneity as well
as the dynamic tumor immune microenvironment could provide
new therapeutic targets to treat OS.
The advent of deep sequencing technology has revolutionized
the diagnosis and treatment of diseases. The accumulation of
genomic and transcriptomic datasets from large cohorts of clinical
samples in TCGA, ICGC and NCBI GEO databases enables
researchers to characterize novel therapeutic targets. Conven-
tional bulk RNA sequencing (RNA-seq) is normally performed to
determine the mixed gene features of all cellular populations in
one sample. Therefore, this method is less likely to detect
transcriptional and immunogenic heterogeneity among cell.
The emergence of single-cell RNA-sequencing (scRNA-seq)
technology has fundamentally changed the ﬁeld of tumor biology
and provided a strategy to demonstrate TME heterogeneity as
well as intercellular communication at the single-cell level.
9,10
Zhou et al. performed scRNA-seq of 11 patients with OS, and their
results revealed the transdifferentiation of malignant cells along
with the heterogeneity of tumor-in ﬁltrating T lymphocytes (TILs).
11
However, the immunoregulatory characteristics of myeloid cells,
which might account for most of the tumor-in ﬁltrating immune
cells in OS, have not yet been fully investigated. 12 Myeloid cells,
including macrophages, dendritic cells (DCs) and monocytes, play
a vital role in tumor immune surveillance through phagocytosis,
antigen processing and presentation. Tumor-associated macro-
phages (TAMs) may also play a critical role in regulating tumor
inﬂammation and angiogenesis to accelerate tumor progression.
Given that these myeloid cells can be polarized toward a
protumor/antitumor response,
13 we hypothesize that regulating
myeloid cells in the TME can be a promising strategy for OS
immunotherapy.
Received: 20 July 2021 Revised: 8 July 2022 Accepted: 4 September 2022
1Department of Orthopaedics, Union Hospital, Tongji Medical College, Huazhong University of Science and Technology, Wuhan 430022, China; 2Department of Orthopaedic
Surgery, The Third Hospital of Hebei Medical University, Shijiazhuang 050051, China; 3Orthopaedic Institute of Hebei Province, Shijiazhuang 050051, China; 4Key Laboratory of
Biomechanics of Hebei Province, Shijiazhuang 050051, China; 5Animal Center of Hebei Ex & In vivo Biotechnology, Shijiazhuang 050051, China; 6Department of Pharmacy, Union
Hospital, Tongji Medical College, Huazhong University of Science and Technology, Wuhan, China and 7Department of Pathology, Union Hospital, Tongji Medical College,
Huazhong University of Science and Technology, Wuhan, China
Correspondence: Liming Xiong (xiongliming@hust.edu.cn) or Baichuan Wang (wangbaichuan-112@163.com) or Yingze Zhang (yzling_liu@163.com)
These authors contributed equally: Weijian Liu, Hongzhi Hu, Zengwu Shao
www.nature.com/boneresBone Research
© The Author(s) 2023
1234567890();,:

To identify the pro ﬁle of tumor-in ﬁltrating myeloid cells and the
immune heterogeneity of OS, we analyzed published scRNA-seq
datasets from the GEO database and bulk RNA-seq data from the
Therapeutically Applicable Research to Generate Effective Treat-
ments (TARGET, https://ocg.cancer.gov/programs/target) database
to explore the diverse phenotypes and functions of subtypes
within the TME. In this study, we identi ﬁed a tumor-educated
“betrayer” DC that suppressed the immune response, deciphered
heterogeneous myeloid cells in OS, and predicted the cell ‒cell
interaction network. Through systematic analyses, our work helps
to elucidate the biology of the TME in OS and contributes to the
development of immunotherapy in clinical applications.
RESULTS
Overview of the osteosarcoma tumor microenvironment at a
single-cell resolution
In the published single-cell dataset (GSE152048), there are seven
primary tumor lesions, two recurrent tumor lesions and two lung
metastases. The scRNA-seq data were included in this study and
were combined with bulk RNA-seq data of tumor tissue from
eighty-ﬁve patients (Fig. 1a). After the quality control process (Fig.
S1a; b) and removal of the batch effects between patients (Fig.
S1c) (see “Materials and Methods ”), we identi ﬁed eight clusters of
cells. Brie ﬂy, myeloid cells (LYZ
+), lymphocytes (CD3D +), osteo-
clasts (ACP5 +), endothelial cells (CLDN5 +), perivascular-like cells
(PVL) (RGS5 +TAGLNhigh), cancer-associated ﬁbroblasts (CAFs)
(TAGLNlowACTA2+) and proliferative cells (MKI67 +) were identi ﬁed
in the study (Figs. 1b; c; S2). Among the myeloid cell population,
macrophages (APOE+CD68+), monocytes (S100A8 +S100A9+), and
DCs (HLA-DQA1 highCD14-) were annotated. For lymphocytes, we
classiﬁed CD4 T cells (IL7R +), CD8 T cells (CD8A +), regulatory
T cells (Tregs) (TNFRSF4 +), natural killer cells (NK) (GNLY +GZMB+),
and B cells (CD79A +JCHAIN+). Furthermore, PDGFRA +CXCL12+
CAFs were annotated as in ﬂammatory CAFs (iCAFs) as described
by Öhlund D et al., 14 while myo ﬁbroblast-like CAFs were
characterized by high expression of ACTA2 but negative expres-
sion of PDGFRA - (Figs. 1d; S2). 15
Tumor-associated DCs promote tumor immune tolerance by
recruiting Tregs
Three DC subsets were characterized in OS, including conven-
tional class 1 DCs (cDC1s) (XCR1
+CLEC9A+) and conventional class
2 DCs (cDC2s) (CD1C +CLEC10A+) (Figs. 2a, b; S3a). In addition, a
cluster of CD83 +CCR7+LAMP3+ DCs was found in OS and can be
referred to as mature regulatory DCs (mregDCs) (Fig. 2a– c).16 To
investigate whether these mregDCs are tumor speci ﬁc, we
aggregated the DCs from normal peripheral blood mononuclear
cells (PBMCs) (GSE94820) and two OS cohorts (GSE152048 and
GSE162454) through Harmony packages (Fig. 2d).
17 We found that
mregDCs preferentially existed in the two independent OS cohorts
but were nearly absent in normal PBMCs, indicating that mregDCs
may be a tumor-associated DC population (Fig. 2d, e). In addition,
the number of CD83 +CCR7+LAMP3+ DCs was higher in OS than in
normal bone marrow, as shown in Fig. 2f, g. These results together
suggest the existence of a group of tumor-speci ﬁc DCs in OS.
After reclustering of DCs, we used the function TransferData
from the Seurat v3 package to calculate the similarity of cells from
PBMCs to different subsets identi ﬁed in the OS dataset. This result
suggests similarity between mregDCs and cDC1 subsets (Fig. 3a).
To examine the lineage relationship of mregDCs with other DC
populations, we performed Monocle2 analysis of DC clusters in OS.
The results suggest that mregDCs in OS may originate from cDC1,
consistent with previous ﬁndings of Cheng et al. and Zhang et al.
(Fig. 3b).
18,19 In addition, the coinhibitors CD274, LAG3, LGALS9,
SIRPA, TIGIT, and PDCD1LG2 were upregulated along the
pseudotime trajectory (Fig. 3b). Compared with cDC1s and cDC2s,
mregDCs exhibited an “activated” phenotype with a higher
capacity of migratory ability as well as immune-regulatory ability,
indicating that this variable DC subset is mature regulatory DCs
(Fig. 3c). More importantly, mregDCs speci ﬁcally expressed CCR7,
CCL17, CCL19 and CCL22, which can recruit multiple types of
inﬁltrating T cells (Fig. 3d).
20,21 Because the current single-cell
RNA-Seq dataset includes only 11 patients, we calculated the
correlation between the mregDC signature and T-cell signatures in
85 OS patients from the TARGET website to expand the sample
size. The results showed a strong correlation between mregDCs
and Tregs (Fig. 3e). Interestingly, staining of tumor sections further
conﬁrmed the existence of mregDCs and revealed the physical
juxtaposition of mregDCs and Tregs (Fig. 5f). Moreover, the
number of Tregs within 100 μm was signi ﬁcantly higher than that
in the distant areas (Fig. 3g). To investigate the clinical role of the
variable DC subset identi ﬁed in the present study, we estimated
the fraction of every cell type in samples from the TAGET
osteosarcoma cohort with CIBERSORTx (Fig. S4a, b).
22 The score of
mregDCs was found to be related to a poorer overall survival rate,
and the accumulation of Tregs was correlated with the event-free
survival rate (Fig. S3b). In addition, the cell fraction evaluated by
CIBERSORTx suggested a positive correlation between mregDCs
and Tregs (Fig. S3c). These results suggest the possibility that
mregDCs promote tumor immune tolerance through recruitment
of Tregs in the OS TME.
The heterogeneity of cancer cell immunogenicity
Copy number variations (CNVs) have been shown to be an effective
strategy to identify more aggressive clones of cancer cells. Zhou
et al. revealed that more canonical CNVs accumulated in
chondroblastic OS lesions, suggesting that chondroblastic cancer
cells are a less differentiated OS type.
11 However, whether high CNV
leads to immune escape remains unclear. Thus, we examined the
r e l a t i o n s h i pb e t w e e nC N Va n dt h ei m m u n er e s p o n s ei nO Si nt h e
current study. We integrated the stromal cells (Fig. S5a) and
estimated the CNV of each cell by the inferCNV package (Figs. 4a, b;
S5b). The results revealed that cancer cells accumulated a larger
number of CNVs than ﬁbroblast cells. Interestingly, we observed a
cluster of low CNV cancer cells in the stromal cells. PySCENIC
23 was
applied to perform transcription factor and motif analysis.
Transcription factor (TF) motifs, including CEBPB ( +), FOSB ( +),
SAP30 (+)a n dA T F 4(+), were signiﬁcantly upregulated in CNV high
cancer cells, while IRF3 ( +), ETV7 ( +), STAT1 ( +) and IRF7 ( +)w e r e
downregulated (Fig. S5c), indicating promising new regulatory
networks driven by TFs in OS cells. In addition, both Gene Ontology
(GO) enrichment analysis
24 and gene set variation analysis (GSVA)25
of MSigDB hallmark gene sets revealed that the interferon-gamma
response was relatively enriched in CNV low cancer cells (Fig. 4c, d).
As transcriptional downregulation of MHC-I is one of the most
important factors that impairs the antitumor effect of IFN- γ
signaling,
26 we subsequently examined the expression of MHC-I
molecules at the mRNA level. We found that cancer cells with higher
levels of CNV displayed lower levels of MHC-I genes (HLA-A, HLA-B
and HLA-E) and the B2M gene, suggesting that these cancer cells
were less immunogenic (Fig. 4e). To further examine whether the
downregulation of MHC-I can be generalized across osteosarcoma,
we evaluated the expression of MHC-I and B2M through
immunohistochemistry (IHC) staining in sections from OS patients.
The results showed that high-grade OS downregulated the
expression of MHC-I and B2M (Fig. 4f, g). Based on these ﬁndings,
we believe that the downregulation of the interferon signaling
pathway and MHC class I molecules in high-grade OS may lead to
immune evasion.
CD24 signaling regulates the macrophage-mediated immune
response to OS
Accumulating evidence suggests that the TME polarizes macro-
phages toward a protumor phenotype in multiple types of
cancers.
27 In the current study, the results of the analysis of
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
2
Bone Research            (2023) 11:4 

Single-cell RNA-seq analysis
a
b
d
c
Bulk RNA-seq analysis
Myeloid cell LYZ
Endothelial CLDN5
Osteoblastic cell
COL1A1
tSNE_1
tSNE_2
Endothelial
Proliferative cancer cell
PVL
Osteoclast
Cancer cell
Myeloid cell
Lymphocytes
CAF
Endothelial
B
NK
Treg
CD4 T
CD8 T
DC
Osteoclast
Monocyte
TAM
PVL
CAF
Cancer
COL11A1
HAPLN1
FGFBP2
COL2A1
IBSP
SFRP2
PLA2G2A
CXCL14
COMP
COL3A1
ACTA2
RGS5
IGFBP7
TAGLN
THY1
C1QA
C1QB
APOC1
APOE
C1QC
S100A8
S100A9
LYZ
G0S2
CXCL8
ACP5
MMP9
CTSK
CKB
CST3
FCER1A
HLA-DPB1
HLA-DRA
AREG
HLA-DQA2
CCL5
CD69
GZMA
GZMK
CD52
LTB
KLRB1
CD3D
IL32
TNFRSF4
TNFRSF18
GNLY
NKG7
GZMB
XCL2
CD79A
CD79B
RAMP2
GNG11
SPARCL1
PLVAP
CLDN5
Chondroblastic cell
COL2A1
Proliferative cell
MKI67
Max
Min
Average expression
02 0 7 5
Percent expressed
PVL RGS5 CAF TAGLN
Lymphocyte CD3D Osteoclast ACP5(TRAP)
Digital cytometry
Survival analysis
Annotation
Crosstalk analysis
M1 like TAM
Trag
SPP1+ TAM
Endothelial
NKT
cDC2
cDC1
CD8 T CD4 T
C1QC+ TAM
regDC
1.00
0.75
0.50
0.25
0.00
0
1 000
2 000
3 000
4 000
5 000
6 000
Fig. 1 Overview of the osteosarcoma tumor microenvironment at a single-cell resolution. a Overall design for investigating the tumor
microenvironment in osteosarcoma. b T-distributed stochastic neighbor embedding (tSNE) plot of the identi ﬁed main cell clusters in OS
lesions. c tSNE plots showing the expression of marker genes of the maj or cell types detected in this study. Red represents high
expression; gray represents low expression. d D o tp l o ts h o w i n gt h es p e c iﬁcally expressed genes of the major cell types. Red represents
high expression; gray represents low expression. The size of th ec i r c l er e p r e s e n t st h ep e r c e ntage of cells that expressed the
indicated genes
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
3
Bone Research            (2023) 11:4 

cDC1
cDC2
mregDC
LAMP3CCR7CD83
tSNE_2
tSNE_1
tSNE_2
tSNE_1
Cancer cell
CAF PVL
Macrophage
Monocyte
cDC1 cDC2
mregDCOsteoclastLymphocyteEndothelial
ac
bd
CLEC9A
2
THBD
XCR1
IFNG
CD1C
FCGR2B
CD209
CLEC10A
LAMP3
FSCN1
CD274
IL7R
cDC1
1
0
–1
–2
cDC2 mregDC
Integrated DC PBMC GSE94820
OS GSE152048 OS GSE162454
cDC1
cDC2
mregDC
pDC
AS DC
100%
50%
0
AS DC
mregDC
cDC1
cDC2
pDC
OS GSE162454
OS GSE152048
PBMC GSE94820
CCR7 CD83 LAMP3
Bone marrow
Number of mregDCs per mm2
Tumor
ef g
80
60
40
20
0
***
Bone marrow
Tumor
Fig. 2 Manifesting mature regulatory dendritic cells (mregDCs) as a tumor-associated DC population. a T-distributed stochastic neighbor
embedding (tSNE) plot of DCs colored by subgroup clusters. b Heatmaps revealing the average gene expression levels of marker genes in
each DC cluster. c Violin plot showing the speci ﬁc expression of LAMP3, CD83 and CCR7 in mregDCs. d tSNE plots showing the integrated
clustering of DCs from OS cohorts and normal peripheral blood mononuclear cells (PBMCs). e Cell fractions in the OS cohorts and normal
PBMCs. f Immunoﬂuorescence staining of mregDC markers in osteosarcoma (OS) primary tumors. The scale bar represents 20 μm.
g Quantitative analysis of the density of CD83 +LAMP3+CCR7+ DCs in the regenerative area from bone marrow and OS tissue sections. Data
are the means ± SEMs. *** P < 0.001
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
4
Bone Research            (2023) 11:4 

Smiliarity
CD1C+ DCs
CLEC9A+ DCs
CD141-CD1C- DCs
AS DCs
pDCs
cDC2 cDC1 mregDC
cDC1 cDC2 mregDC
cDC2cDC1 mregDCcDC2cDC1 mregDC
cDC2cDC1 mregDC
cDC2
cDC1
mregDC
Max
Min
Max
Min
Pseudotime
0 15
TNFRSF8
HAVCR2
CD44
TNFRSF14
PDCD1LG2
CD40
LAG3
LGALS9
CD27
CD274
TNFSF18
TIGIT
TNFRSF18
SIRPA
3
2
1
0
–1
–2
–3
ab
c dMaturation Migration Regulatory
CD40
CD80
CD86
RELB
CD83
CCR7
MYO1G
CXCL16
ADAM8
ICAM1
FSCN1
MARCKS
CD274
PDCD1LG2
CD200
FAS
ALDH1A2
SOCS1
SOCS2
CCR7
CCL17
CCL19
CCL22
ef g Signature genes
R = 0.27 P = 0.012
R = 0.36 P = 0.000 72
R = 0.5 P = 1.5e-6
0.3
0.2
0.1
0
0.20
0.15
0.10
0.05
0.02
0
0.01
0
0 0.005 0.010 0.015
mregDC
CD4
LAMP3
FOXP3
Merge
400
300
200
100
0
***
***
Treg CD8 T CD4 T
Number of CD4+FOXP3+ cells per mm2
Distance to LAMP3+ cell
<100 
μm
100-200 
μm
>200 
μm
Fig. 3 Mature regulatory dendritic cells (mregDCs) promote tumor immune tolerance. a Heatmap showing the similarity of dendritic cells
from the OS scRNA dataset projected onto different dendritic cells identi ﬁed from the normal PBMC dataset. Red represents high similarity;
blue represents low similarity. b Developmental trajectory for DCs inferred by Monocle2 and the heatmap showing the expression changes of
coinhibitors and costimulators along the pseudotime trajectory. c Heatmaps revealing the average gene expression levels of maturation
genes, regulatory markers, and migration genes in dendritic cells. Red represents high expression; blue represents low expression. d Violin
plots showing the expression of CCR7, CCL17, CCL19 and CCL22 in dendritic cells. e Correlation between the mregDC signature and T-cell
signatures in the TARGET OS cohort. f Representative image of mregDCs and regulatory T cells (Tregs) that colocalized in OS tissues stained by
multicolored immunoﬂuorescence staining. White arrows depict mregDCs, while gray arrows indicate Tregs. The scale bar represents 10 μm. g
Distribution of CD4 +FOXP3+ cells adjacent or nonadjacent to CD42 mregDCs. Data are the means ± SEMs. * P < 0.05; ** P < 0.01; *** P < 0.001
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
5
Bone Research            (2023) 11:4 

RNA catabolic process
Low CNV cancer High CNV cancer
mRNA catabolic process
Protein localization to membrane
RNA splicing
mRNA splicing, via spliceosome
Ribosome biogenesis
Protein targeting to membrane
Nuclear-transcribed mRNA catabolic
Response to interferon-gamma
Regulation of multi-organism process
Regulation of actin filament-based
Leukocyte migration
Regulation of peptidase activity
Actin filament organization
Cell-substrate adhesion
Ossification
Neutrophil mediated immunity
MTORC1 SIGNALING
MYC TARGETS V1
G2M CHECKPOINT
MYC TARGETS V2
E2F TARGETS
INTERFERON ALPHA RESPONSE
INTERFERON GAMMA RESPONSE
SPERMATOGENESIS
EPITHELIAL MESENCHYMAL TRANSITION
UV RESPONSE DN
IL2 STAT5 SIGNALING
IL6 JAK STAT3 SIGNALING
COAGULATION
NOTCH SIGNALING
COMPLEMENT
KRAS SIGNALING UP
TGF BETA SIGNALING
ANDROGEN RESPONSE
ANGIOGENESIS
APICAL JUNCTION
INFLAMMATORY RESPONSE
ALLOGRAFT REJECTION
PROTEIN SECRETION
TNFA SIGNALING VIA NFKB
APOPTOSIS
FATTY ACID METABOLISM
PEROXISOME
HEME METABOLISM
HYPOXIA
UV RESPONSE UP
GLYCOLYSIS
UNFOLDED PROTEIN RESPONSE
KRAS SIGNALING DN
MITOTIC SPINDLE
PI3K AKT MTOR SIGNALING
PANCREAS BETA CELLS
WNT BETA CATENIN SIGNALING
BILE ACID METABOLISM
ESTROGEN RESPONSE EARLY
CHOLESTEROL HOMEOSTASIS
XENOBIOTIC METABOLISM
P53 PATHWAY
ADIPOGENESIS
MYOGENESIS
APICAL SURFACE
OXIDATIVE PHOSPHORYLATION
REACTIVE OXYGEN SPECIES PATHWAY
DNA REPAIR
ESTROGEN RESPONSE LATE
HEDGEHOG SIGNALING
High CNV cancerLow CNV cancer
2
1
0
–1
–2
CNV
ab d
CNV
MKI67 RGS5
TAGLN
High CNV cancer
Proliferative cancer
Low CNV cancer
CAF
PVL
50 0 50
Gene counts
HLA-A HLA-B HLA-E B2M
HLA-AHLA-BHLA-EB2M
Max
Min
Max
Min
tSNE_2
tSNE_1
tSNE_2
tSNE_1
**
**
0.4
0.2
0Low grade High grade IgG control
c
e
High CNV cancer
Proliferative cancer
Low CNV cancer
CAF
PVL
g
H&EMHC-IB2M
f
0.6
0.4
0.2
0
Low grade High grade
Density mean of
B2M
Density mean of
MHC-I
Fig. 4 The heterogeneity of cancer cell immunogenicity. a tSNE plot representing the single-cell copy number variations (CNVs) of cancer
cells. Red represents high levels of CNV, and gray represents low levels of CNV. b tSNE plots of stromal cells colored by cluster (top); violin plots
of CNV score and marker gene expression levels (bottom). c Bar plot showing the enriched Gene Ontology enrichment of differentially
expressed genes between CNV high and low cancer cells. d Heatmap revealing the differentially regulated pathways between CNV high and
low cancer cells scored by GSVA. Red represents high scores; blue represents low scores. e tSNE plots and violin plots showing the expression
of HLA-A, HLA-B, HLA-E and B2M in stromal cells. f and g Representative immunohistochemistry and mean density of MHC-I and B2M
expression in low-grade and high-grade OS tissue. Scale bar, 100 μm. Data are the means ± SEMs. * P < 0.05; ** P < 0.01
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
6
Bone Research            (2023) 11:4 

macrophage subsets revealed robust expression of MRC1 (encod-
ing CD206) and CD163 (Fig. S6a – c). In addition, MHC-II genes were
downregulated in C1QC + TAMs and SPP1 + TAMs (Fig. S6d). These
results indicate the existence of an M2-like phenotype in most
macrophages in OS. However, the underlying mechanisms that
drive immune tolerance are not yet fully understood.
Cancer cells were reported to evade clearance by immune cells
through the overexpression of an tiphagocytic surface proteins,
including CD47 and programmed cell death ligand 1 (encoded by
CD274). CD24 is a novel “don’te a tm e” signal that inhibits Toll-like-
receptor-mediated inﬂammation and cellular engulfment by macro-
phages.
28 The expression of CD24 and CD47 was stronger than that
of CD274, indicating a role of macrophage-mediated immune escape
rather than T-cell-mediated immune evasion in OS (Fig.5a, b). At the
single-cell resolution, we found that CD47 was highly expressed by
almost all cell types, while CD24 was preferentially expressed by OS
cells (Fig. 5a). CD24 exhibited higher mRNA expression in OS tissues
than in normal bone marrow from the same patients, as shown by
ﬂuorescence in situ hybridization (FISH) (Fig.5c). Moreover, high CNV
cancer cells were found to express higher CD24 than low CNV cancer
cells and ﬁbroblasts (Fig. 5d). IHC staining also demonstrated
stronger expression of CD24 in high-grade OS (Fig. 5e, f). These
results together illustrate that CD 24 is a potential immunotherapy
target in OS.
To investigate the role of CD24 in regulating the macrophage-
mediated immune response in OS, we treated bone marrow-
derived macrophages (BMDMs) with IL-4 to generate M2-like
macrophages and cocultured these less phagocytic macrophages
with the GFP
+ K7M2 osteosarcoma cell line for 36 h. We found
that interference with Cd24a in the K7M2 cell line potentiates
phagocytosis as measured by live-cell microscopy (Fig. 5g, h).
Similarly, ﬂuorescence-activated cell sorting (FACS)-based mea-
surements revealed a signi ﬁcant increase in phagocytosis upon
transfection with Cd24a siRNA compared to the scramble siRNA
(Fig. 5i, j). In addition, the BMDMs cocultured with Cd24a
knockdown cancer cells had a more in ﬂammatory phenotype
(Fig. 5i, k). To investigate whether the protection of phagocytosis
conferred by downregulating CD24 could be recapitulated in vivo,
we treated mice bearing periosteal osteosarcoma with
cholesterol-modiﬁed Cd24a siRNA or scramble siRNA at a dose
of 1 OD every two days through intratumor injection. Three weeks
after engraftment, we observed signi ﬁcantly reduced tumor
tumorigenicity in the Cd24a siRNA group compared to the
scramble siRNA group as measured by micro-CT scanning (Fig.
6a, b). Moreover, robustly increased MHC-II
+ cells and in ﬁltrating
CD4 T cells were observed in the Cd24a siRNA group, as shown by
IHC staining (Fig. 6c– e). FACS analysis also revealed increases in
phagocytosis as well as antigen presentation phenotype (Fig.
6f– h). In summary, our results revealed that OS cells evade the
macrophage-mediated immune response through CD24 signaling.
Cell‒cell interactions within OS
Given that exploring the cell ‒cell interaction LR pairs can provide
new information about the OS TME, we calculated the attraction
strengths of ligand ‒receptor pairs in the scRNA-seq dataset. The
cell‒cell interactions in OS were also interrogated by CellPho-
neDB.
29 The enrichment of the CD24-SIGLEC10 LR pair between
cancer cells and multiple macrophage subsets revealed the
immunoregulatory role of CD24 in OS, as we described above.
In addition, the robust expression of SPP1 and ITGAV in SPP1 +
TAMs and CAFs suggested that SPP1 + TAMs may promote
directional cancer cell migration by aligning ﬁbronectin in CAFs
(Fig. 7a).30,31 Next, we focused on the heterogenetic cell ‒cell
interactions of DC subsets. We found that cDC1 had a strong
ability to induce multiple T-cell in ﬁltration through CXCL10-CXCR3,
whereas mregDCs showed the highest immunosuppression
potency through CD274-PDCD1 and PVR-TIGHT interactions with
Tregs (Fig. 7a). In addition, we found that CAFs and SPP1
+ TAMs
interacted with endothelial cells through the ACKR3-CXCL12 and
CCL2/CXCL1-ACKR1 axes (Fig. 7b). Our analyses suggested a role
for the ACKR family in angiogenesis in OS. Other ligand ‒receptor
pairs involved interactions between cancer cells and SPP1 + TAMs
through PGRMC2-CCL4L2 and interactions between CAFs and
TAMs through CXCL12-CXCR4. Of note, the OS samples were
composed of osteoblastic osteosarcoma and chondroblastic
osteosarcoma from primary, recurrent, and metastatic lesions. In
these cases, cells cannot communicate with each other, as they do
not reside in the same TME. Thus, we separately predicted cell ‒cell
interactions in different lesions. These results revealed distinct
cell‒cell interaction modes in various OS types, which may require
precise personalized treatments. Overall, our analysis of scRNA-seq
data suggests a role of myeloid cells in the TME through
interacting with immune and stromal cells in OS (Fig. S8).
DISCUSSION
Currently, the treatment of advanced OS is still very challenging. In
the present study, we leveraged the advantages of scRNA-seq
technology and bulk RNA-seq to explore the immune hetero-
geneity of cancer cells as well as the atlas of myeloid cells within
OS patients. An immunoregulatory subset of DCs was identi ﬁed in
OS tissue. The classi ﬁcation of the malignant cells into CNV high or
low groups revealed diverse immunogenicity in OS. In addition,
CD24 was characterized as a novel “don’t eat me ” signal that
mediated the immune escape of OS cells.
Dendritic cells, the most ef ﬁcient professional antigen presenta-
tion cells (APCs), are critical in T-cell priming, activation, and
differentiation. Based on their cell surface markers, human
dendritic cells can be classi ﬁed into conventional class 1 DCs
(cDC1s), conventional class 2 DCs (cDC2s), and plasmacytoid DCs.
Recently, the existence of a new type of dendritic cell (cDC3) in
mice and humans has been proven by single-cell sequencing.
32
cDC1 is essential for CD8 T-cell priming and activation, which is
important for antitumor and antiviral immunity, while cDC2 is
involved in CD4 T-cell responses.
33,34 Moreover, recent studies
found that cDC1s were not only essential for priming CD8 T cells
but were also required for the licensing of CD4 T cells in tumors.
35
In the current study, CXCL10-CXCR3 was enriched between cDC1
and multiple T cells (Fig. 7a), indicating the role of cDC1 in the
recruitment or activation of T cells. In addition, cDC1s were the
only tumor-in ﬁltrating immune cells that were associated with
better prognosis in the current study (Fig. S3b). These results
suggest the core role of cDC1s in immune priming as well as the
necessity to develop cDC1 recruitment strategies.
36
Although mature immunoregulatory DCs have been identi ﬁed in
various cancers, the presence of this subgroup in osteosarcoma has
not yet been conﬁrmed.16,19 The mregDCs (CCR7+LAMP3+CD83+)i n
the current study can be referred to as CCR7 + DCs that were found
by Zhou et al. 11 As they mainly focused on the heterogeneity of
cancer cells and T cells, the role and function of this DC subset were
not fully annotated. In this study, the interaction between mregDCs
and Tregs was identi ﬁed through CD274-PDCD1 and PVR-TIGIT
signaling, as well as their physical juxtaposition. Given that mregDCs
were enriched in OS but were absent in PBMCs, we speculate that
mregDCs are tumor-associated DCs that negate antitumor immunity
in OS.
19,37 Further studies are still needed to better understand the
regulation and differentiation of mregDCs. The marker genes of the
DC populations identi ﬁed in this study can also be used to
characterize this DC subset for further studies.
Many cancers evade immune surveillance by suppressing the
expression of major histocompatibility class I (MHC-I). 38 Loss of
MHC-I expression enables tumor cells to escape killing by
cytotoxic T lymphocytes.
39 Moreover, transcriptional repression
of MHC I has been reported to be associated with resistance to
cancer immunotherapy. 40 In our study, the transcription of MHC I
and the interferon-gamma response were repressed in high CNV
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
7
Bone Research            (2023) 11:4 

a
CD24 CD47 CD274
SIGLEC10 SIRPA PDCD1
CD24
CD47
CD274
Expression
02
Bone marrow Tumor tissue
P6
BC21
P3
P2
BC3
BC20
BC16
BC5
BC17
BC10
BC11
P5
BC22
BC6
P1
P4
BC2
Max
Min
CD24
tSNE_2
tSNE_1
d
CD24
High CNV cancerLow CNV cancer
CAF PVL
siNC
siCd24a #1siCd24a #2
siNC
siCd24a #1siCd24a #2
siNC
siCd24a #1siCd24a #2
Proliferative cancer
Average expression
Percent expressed
b
c
1.0
0.5
0.0
-0.5
-1.0
5
10
20
30
e
Low grade High grade
CD24
f 0.32
0.30
0.28
0.26
Low grade High grade
***
Density mean of
CD24
100%
Relative mRNA expression
of Cd24a (ΔΔCT)
Percent of GFP+ macrophagesPercent of MHC-II+ macrophages
10%
0
**
**
**
**
**
*
siNC siCd24a #1 siCd24a #2
siNC siCd24a #1 siCd24a #2
siNC siCd24a #1 siCd24a #2
gh j 60
40
20
0
i
Co-cultured cell
SSC-A
SSC-A
FSC-AFSC-A
F4/80
GFP
MHC-II
FSC-A
90
80
70
60
50
40
F4/80
+ Macrophage
F4/80+ Macrophage
k
Fig. 5 CD24 protects OS cells from macrophage attack. a Expression of the immune checkpoints CD24, CD47, and CD274 and their receptors
overlaid onto tSNE plots. Red represents high expression; gray represents low expression.b Heatmap showing the normalized expression of CD24,
CD47, and CD274 in each patient. Red represents hig h expression; blue represents low expression. c Fluorescence in situ hybridization (FISH)
imaging of CD24 in tumor tissues and bone marrow f rom the patients. The scale bar represents 100 μm. d Dot plots showing the expression of
CD24 in stromal cells. Red represents high expression; gray represents lowexpression. The size of the circle represents the percentage of cells that
e x p r e s s e dt h ei n d i c a t e dg e n e s .e and f Representative immunohistochemistry and mean density of CD24 expression in low-grade and high-grade
OS tissue. Scale bar, 100μm. g Relative expression of Cd24a in K7M2 cell lines that were transfected with Cd24a siRNA or scramble siRNA. Scale bar,
100 μm. Data are the means ± SEMs. * P < 0.05; **P <0 . 0 1 .h Representative liveﬂuorescence microscopy images of in vitro phagocytosis of K7M2
cells (GFP+ green) by BMDMs in the presence of Cd24a siRNA or scramble siRNA. i-k Representative images of the gating strategy and statistical
analysis for the in vitro phagocytosis assay and the M 1-like macrophage assay. Data are the means ± SEMs. *P < 0.05; **P <0 . 0 1
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
8
Bone Research            (2023) 11:4 

cancer cells (Fig. 2b). The results suggested that downregulating
MHC-I on tumor cells may be a driving mechanism of immune
evasion in OS. Moreover, emerging evidence suggests a role for
antiphagocytic signals in immune evasion. Through the expres-
sion of “don’t eat me ” signals, tumors are capable of escaping
macrophage-mediated phagocytosis. CD47 is a classical “don’t eat
me” signal that binds to its receptor SIPR α on macrophages to
protect cells from phagocytosis.
41 Mohanty et al. reported an
additive therapeutic effect of CD47 mAb in animal models of
OS.
42,43 However, CD47 is also expressed in normal immune cells
and erythrocytes. As a result, anemia and neutrophil count
decreases were frequently observed in patients who underwent
CD47 blockade therapy.
44 To address this issue, we tried to
explore novel macrophage-targeted immune therapies. CD24 is a
cancer stem cell marker that is critical for the maintenance, self-
renewal, and differentiation of OS. 45– 47 Recently, CD24 was
identiﬁed as a novel “don’t eat me ” signal through the CD24-
Siglec10 interaction in cancers. 48 However, scant attention has
been given to the role of CD24 in innate immune evasion in OS.
Our results showed that CD24 was a tumor-speci ﬁc “don’t eat me ”
signal in OS. We also found that high-grade OS cells exhibited
robust expression of CD24. More importantly, interference with
the expression of CD24 potentiated phagocytosis and activation
of macrophages in OS. These results could serve as evidence in
support of the therapeutic potential of CD24 blockade in OS
immunotherapy.
In summary, we constructed a singl e-cell atlas of osteosarcoma
cells and myeloid cells across scRNA-seq data and bulk RNA-seq data,
with the aim of verifying the role of mregDCs in OS. Our study also
revealed CD24 as a novel“don’te a tm e” signal in OS, suggesting new
avenues for potential therapeutic treatments of OS.
MATERIALS AND METHODS
Data acquisition
The scRNA-seq of OS has been described by Zhou et al. and Liu
et al.
11,49 The processed count matrix was directly obtained from
GSE152048 and GSE162454, and the clinical data of these patients
were obtained from their supplementary data. The clinical sample
bulk RNA-seq data were acquired from Therapeutically Applicable
Research to Generate Effective Treatments (TARGET, https://
ocg.cancer.gov/programs/target). The reference scRNA-seq data
of the DC population were obtained from GSE94820.
Analysis of scRNA-seq data
Data processing of scRNA-seq data was mainly performed by Seurat
(version 3.0.1).
50 Brieﬂy, low-quality single cells were eliminated
through a set threshold with the number of UMIs, features and
mitochondrion-derived genes. The intergradation of data from the
patients was performed by the IntegrateData function in Seurat to
remove the batch effects among patients, and the top 3 000 variable
genes were used to calculate intergradation anchors in this process.
Subsequently, the NormalizeData function in Seurat was used to
normalize the data matrix. The uns upervised clustering of the main
cell subtypes was performed by the F indClusters function in Seurat
and visualized with 2D UMAP or t-distributed stochastic neighbor
embedding (tSNE). Then, the markers of each cell cluster were
identiﬁed by the FindAllMarkers function in Seurat for annotation.
Monocle2 was used to decipher the transcriptional trajectories of
macrophages.
Patients and tumor samples
All clinical samples were obtained from the Department of
Orthopedics, Union Hospital of Tongji Medical College, Huazhong
University of Science and Technology, Wuhan, China. The murine
osteosarcoma K7M2 cell line was purchased from Zhongqiaox-
inzhou Biotechnology Co., Ltd. (Shanghai, China). A tumor-bearing
mouse model was established by inoculating 2 × 10
6 K7M2 cells
with Matrigel matrix (Sigma-Aldrich E1270) into the right ﬂank of
6-week-old female Balb/c mice. Then, these subcutaneous tumors
were cut into 1 × 1 × 1 mm 3 lumps and transplanted onto the
periosteum of the distal femur in 6-week-old female Balb/c mice.
All experimental processes were approved by the Institutional
Review Board of Union Hospital, Tongji Medical College,
Huazhong University of Science and Technology and Ethics
Committee of Hebei Ex & In Vivo Animal Center.
Cell culturing and in vitro phagocytosis assay
The GFP-K7M2 cell line was obtained from Qijing Biological
Technology Co., Ltd. (Wuhan, China). Bone marrow-derived
macrophages (BMDMs) were obtained by culturing bone marrow
from 6-week-old Balb/c mice with DMEM containing 10% FBS and
20 ng·mL
−1 m-CSF (R&D, 416-M-050). On Day 5 of culture, the
medium was refreshed again, and 20 ng·mL −1 IL-4 was added for
4 days to induce M2-like BMDMs. BMDMs were cocultured with
GFP-K7M2 cells in phagocytosis assay wells to observe the
phagocytosis rate. All phagocytosis assay wells were stained with
anti– mouse F4/80 – Super Bright 645 (eBioscience, 64-4801-82;
1:200) for 30 min prior to ﬂow cytometry analysis.
siRNA transfection and in vivo treatment
siRNA transfection was performed using an RNATransMate kit
(Sangon Biotech, E607402) at 20 nmol·L
−1 for 12 h. The knockdown
efﬁciency was validated with qRT‒PCR. For in vivo RNA interference,
cholesterol-modiﬁed Cd24a siRNA or scramble siRNA were designed
and synthesized by Sangon Biotech Co., Ltd., (Shanghai, China) and
were intratumorally injected at a dose of 1 OD every second day. The
sequence of siRNA we used can be found in Table S1.
Fluorescence in situ hybridization imaging
For ﬂuorescence in situ hybridization (FISH), the bone marrow was
centrifuged before ﬁxation, while tissues were ﬁxed directly in 4%
PFA/PBS overnight. These tissues were dehydrated before embed-
ding. For all FISH imaging, sections were washed with proteinase K
(Servicebio, G1205) before pre liminary hybridization. Then, we
removed the prehybridization solu tion, added probe hybridization
solution at a concentration of 500 nmol·L
−1, and hybridized
overnight at 42 °C. Finally, the sections were incubated with DAPI
for 8 min in the dark. The imaging was collected by Pannoramic MIDI
II-3Dhistech and analyzed by CaseViewer Software (version 2.4). The
sequence of the probe we used can be found in Table S1.
CNV inference of cancer cells
The InferCNV package (version 1.2.2; https://github.com/
broadinstitute/inferCNV/wiki) in R was applied to infer the CNVs
in OS cells. We identi ﬁed and annotated endothelial cells and
ﬁbroblast cells based on the expression of known marker genes
and then introduced them as a reference for CNV estimation.
Pathway analysis
DEGs between clusters were identi ﬁed by the FindMarkers
function of Seurat with the cut off threshold at adj. P val <0.01
and fold change (FC) > 1.3. The DEGs were subsequently used for
GO enrichment analysis as well as KEGG analysis with clusterPro-
ﬁler. The GSVA package in R was applied for GSVA.
Gene regulatory network analysis
SCENIC is an algorithm to identify transcription factors and cell
states through the analysis of gene regulatory networks from
scRNA-seq data. The pySCENIC refactored and reimplemented this
algorithm in Python. The area under the curve (AUC) of each
regulon of cells was calculated by pySCENIC. The difference in
AUCs among cell clusters was identi ﬁed through the Limma
package, and the regulons with an adjusted p value (adj. p val) less
than 0.05 were used for further analysis.
51 The AUCell package in R
was applied to embed the AUC score into UMAP.
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
9
Bone Research            (2023) 11:4 

Immunoﬂuorescence
Whole tumors were ﬁxed in 4% PFA/PBS overnight and
dehydrated before embedding. For all morphologic examinations,
4 μm-thick sections were prepared for H&E and IHC staining. H&E
and IHC staining were performed according to the manufacturer ’s
protocols (Solarbio, G1120). For multi-immuno ﬂuorescence ima-
ging of tumor tissues, sections were ﬁrst stained with primary
antibodies in PBS. After staining with horseradish peroxidase-
conjugated secondary antibodies, the sections were incubated
with ﬂuorescent tyramide signal ampli ﬁcation (TSA) reagent. Then,
the antigen-antibody complexes on sections were eluted.
Subsequent immuno ﬂuorescence staining was performed. Multi-
spectral images were collected by Pannoramic MIDI II-3Dhistech
and analyzed by CaseViewer Software (version 2.4).
The following reagents were used in IHC staining: anti-MHC-I
(rabbit, 1:100, HuaAn, ET1702-47), anti-B2M (rabbit, 1:100, ABclonal,
A12404), anti-MHC-II (rabbit, 1:200, Invitrogen, PA5-116876), anti-CD4
(rat, 1:50, BD Pharmingen, 550278), anti-CD24 (rabbit, 1:100, ABclonal,
A2207), anti-FOXP3 (rabbit, 1:1 000, Servicebio, GB112323), anti-CD63
(mouse, 1:100, Arigo, ARG41312), anti-CCR7 (rabbit, 1:100, HUABIO,
ET1602-22), anti-CD83 (rabbit, 1:1 000, ABclonal, A2040), HRP
conjugated Goat Anti-Rabbit IgG (1:500, Servicebio, GB23303), CY3-
Tyramide (1:2 000, Servicebio, G1223), FITC-Tyramide (1:1 000,
Servicebio, G1222), CY3-Tyramide (1:2 000, Servicebio, G1223), and
Cy5 conjugated Goat Anti-Mouse IgG (1:400, Servicebio, GB27301).
Flow cytometry assay
The tumors were minced and digested with digestion cocktail
(collagenase 1.5 mg·mL
−1,h y a l u r o n i d a s e1 . 5 m g · m L−1, DNase
20 μg·mL−1) at 37 °C for 30 min. Then, the suspension was transferred
onto a 70- μm cell strainer to remove undigested tissue. ACK lysis
buffer was used to exclude red bl ood cells. After CD16/32 blocking
(BD Biosciences, 553141, 1:100) for 30 min, the suspensions were
incubated with antibodies for 30 min at 4 °C. The antibodies used in
the experiments were as follows: Fixable Viability Stain 510 (BD
Biosciences, 564406, 1:1 000), anti – mouse CD45 – APC– Cy7 (BD
Biosciences, 557659; 1:100), anti-mouse CD11b – BB700 (BD Bios-
ciences, 746004; 1:100), anti – mouse F4/80 – Super Bright 645
(eBioscience, 64-4801-82; 1:200), and anti – mouse MHC-II– APC (BD
Biosciences, 562823; 1:100). Cells were resuspended in staining buffer
before ﬂow cytometry and were analyzed on a BD FACSCelesta™ ﬂow
cytometer. Data were analyzed using FlowJo version 10.0 (Treestar).
Micro-CT scanning ( μCT) analyses
The tumor-bearing leg was harvested, and the normal soft tissue
around the femur was removed. After that, μCT analyses were
performed with a SkyScan 1174 μCT scanner. The scanning
procedure was performed at 63 kV with a 153- μA current and a
resolution of 9 μm/pixel. CTAn (version 1.9, SkyScan) was used for
quantitative analysis as well as 3D reconstruction. CTVol (version
2.0, SkyScan) was used for the visualization of 3D models.
Cell– cell interaction analysis
CellPhoneDB is a Python-based algorithm for cell – cell commu-
nication through the known ligand ‒receptor database. Interaction
pairs whose ligands/receptors belong to the CD, VEGF, TNF, TGF,
FGF, CCL, or CXCL families and have P values < 0.05 were used to
evaluate the interactions between the cell populations.
Correlation to bulk-RNA seq from clinical cohort
CibersortX and the average expression of signature genes were
used to decipher the in ﬁltration score of each cell subtype in the
a
f
siNC
b
siCd24a #2
cd e
** **
**25%
20%
15%
10%
5%
0
30%
20%
*
10%
0
500
400
300
200
100
0
2 000
1 500
1 000
500
0
25%
siNC siCd24a #2 IgG
20%
15%
10% BV/TV
H&EMHC-II
Number of MHC-II+ cells per mm2
Number of CD4+ cells per mm2
CD4
SSC-A
CD11b
CD11b
MHC-II
FSC-H
Percent of
MHC-II+ macrophages
Percent of
GFP+ macrophages
5%
0
siNC
Single cell
Live cell
Myeloid
cell
Macrophage
Live/Dead CD45 F4/80
CD45+CD11b+ myeloid cell CD45+CD11b+F4/80+ macrophage
siNC
F4/80 GFP
siCd24a #2 siNC siCd24a #2
Live cell Myeloid cell gh
siCd24a #2
siNC siCd24a #2
siNC siCd24a #2 siNC siCd24a #2
Fig. 6 Interference with the expression of Cd24a promotes phagocytosis and the M1-like phenotype of macrophages in vivo.
a, b Representative images and analysis of micro-CT scanning of the distal femur in each group. Scale bar, 1 mm. BV, bone volume; TV,
total volume. c–e Representative images and analysis of IHC staining of MHC-II and CD4 in tumors treated with cholesterol-modi ﬁed Cd24a
siRNA or scramble siRNA. Scale bar, 100 μm. f–h Representative images of the gating strategy and statistical analysis for the in vivo
phagocytosis assay and M1-like macrophage assay. Data are the means ± SEMs. * P < 0.05; ** P < 0.01; *** P < 0.001
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
10
Bone Research            (2023) 11:4 

clinical cohort from TARGET. Then, the patients were divided into
a high in ﬁltration group and a low in ﬁltration group for each cell
cluster. The prognostic value of these clusters was assessed by Cox
regression analysis. Spearman correlation analysis was performed
to decipher the correlation between cell clusters ( P values < 0.05
were considered meaningful correlations).
DATA AVAILABILITY
The datasets and supplemental information can be acquired online or by contacting
the corresponding authors.
ACKNOWLEDGEMENTS
This work was supported by the National Natural Sciences Foundation of China (grant
91949203, grant 82072979 and grant 81673456), the Nonpro ﬁt Central Research
Institute Fund of the Chinese Academy of Medical Sciences (2019PT320001), and the
Natural Sciences Foundation of Hubei Province (2020CFB778).
AUTHOR CONTRIBUTIONS
Z.S., B.W. and Y.Z. conceived the idea. Q.S. and X.D. collected and analyzed the data.
W.L. ﬁnished the bioinformatics analysis. L.X. performed the immuno ﬂuorescence
staining. Y.H. contributed to the animal experiments. T.G. evaluated the pathological
grading of tumor sections from patients. W.L., H.H. and L.X. wrote the manuscript. All
authors reviewed and approved the manuscript.
ADDITIONAL INFORMATION
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1038/s41413-022-00237-6.
Competing interests: The authors declare no competing interests.
TNF_TNFRSF1B
VEGFA_KDR
Cancer
SPP1+ TAM
mregDC
cDC1
cDC2
C1QC+ TAM
FCN1+ Macro
Treg
cDC2
C1QC+ TAM
FCN1+ Macro
SPP1+ TAM
mregDC
cDC1
CD4 T
CD8 T
Endothelial
iCAF
mCAF
PVL
TNF_VSIR
VEGFA_FLT1
VEGFA_EPHB2
TNFSF12_TNFRSF25
TNFSF12_TNFRSF12A
TNFRSF1A_GRN
TNFRSF1B_GRN
TNF_TNFRSF1A
TNF_NOTCH1
TNF_ICOS
TNF_FLT4
TNF_FAS
TNF_DAG1
TGFB3_TGFBR3
TGFB3_TGFbeta receptor1
TGFB1_TGFBR3
TGFB1_TGFbeta receptor2
TGFB1_TGFbeta receptor1
TFRC_TNFSF13B
SPP1_CD44
SIRPA_CD47
PGRMC2_CCL4L2
NRP2_VEGFA
NRP1_VEGFB
NRP1_VEGFA
MIF_TNFRSF14
LTBR_LTB
LGALS9_CD47
LGALS9_CD44
IGF1_TGF1R
ICAM1_aXb2 complex
lCAM1_AREG
ICAM1_aMb2 complex
HLA–F_LlLRB2
HLA–DPB1_TNFSF13B
HGF_CD44
FLT1_VEGFB
FLT1 complex_yEGFB
FLT1 complex_VEGFA
FGFR1_FGF7
EGFR_TGFB1
CXCL8_ACKR1
 CXCL12_CXCR4
 CXCL1_ACKR1
CSF1_SIRPA
 CD99_PILRA
CD74_MIF
CD74_COPA
CD74_APP
CD55_ADGRE5
CD47_SIRPG
CD46_JAG1
CD44_HBEGF
CD40_TNFSF13B
CD40_CD40LG
CD2_CD58
CCR1_CCL14
CCL4L2_VSIR
CCL2_ACKR1
BTLA_TNFRSF14
ACKR3_CXCL12
a Ligand
CD24 SIGLEC10
SIRP A
PDCD1
ITGAV
ITGA5
CXCR3
TIGIT
Receptor
CD47
CD274
SPP1
FN1
CXCL10
PVR
Normalized expression
02
iCAF
mCAF
Endothelial
SPP1+ TA M
C1QC+ TA M
Cancer
Mean
0
1.3 6
3
-log10(P-value + 0.000 01)
b Endothelial
C1QC+T AM
SPP1+ TA M
Endothelial
C1QC+ TA M
SPP1+ TA M
mCAF
iCAF
Endothelial
mCAF
iCAF
Cancer
Endothelial
mCAF
iCAF
Cancer
C1QC+ TA M
SPP1+ TA M
FCN1+ Mac
cDC1
cDC2
regDC
T reg
Fig. 7 Predicted cell –cell interaction network in the OS TME. a Heatmap showing the normalized expression of ligands and receptors in the
indicated clusters in OS. Red represents high expression; blue represents low expression. b Bubble plots showing ligand ‒receptor pairs
predicted between cell clusters. Dot size indicates the P value generated by CellPhoneDB, colored by mean attraction strength levels
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
11
Bone Research            (2023) 11:4 

REFERENCES
1. Pingping, B. et al. Incidence and mortality of sarcomas in Shanghai, China, During
2002– 2014. Front. Oncol. 9, 662 (2019).
2. Isakoff, M. S. et al. A phase II study of eribulin in recurrent or refractory osteo-
sarcoma: A report from the Children ’s Oncology Group. Pediatr. Blood Cancer 66,
e27524 (2019).
3. Topalian, S. L., Taube, J. M., Anders, R. A. & Pardoll, D. M. Mechanism-driven
biomarkers to guide immune checkpoint blockade in cancer therapy. Nat. Rev.
Cancer 16, 275 – 287 (2016).
4. Ratti, C. et al. Trabectedin overrides osteosarcoma differentiative block and
reprograms the tumor immune environment enabling effective combination
with immune checkpoint inhibitors. Clin. Cancer Res. 23, 5149 – 5161 (2017).
5. Wang, S. D. et al. The role of CTLA-4 and PD-1 in anti-tumor immune response
and their potential ef ﬁcacy against osteosarcoma. Int. Immunopharmacol. 38,
81– 89 (2016).
6. Hennessy, M. et al. Bempegaldesleukin (BEMPEG; NKTR-214) ef ﬁcacy as a single
agent and in combination with checkpoint-inhibitor therapy in mouse models of
osteosarcoma. Int. J. Cancer 148, 1928 – 1937 (2021).
7. Thanindratarn, P., Dean, D. C., Nelson, S. D., Hornicek, F. J. & Duan, Z. Advances in
immune checkpoint inhibitors for bone sarcoma therapy. J. Bone Oncol. 15,
100221 (2019).
8. Suehara, Y. et al. Clinical genomic sequencing of pediatric and adult osteo-
sarcoma reveals distinct molecular subsets with potentially targetable alterations.
Clin. Cancer Res. 25, 6346 – 6356 (2019).
9. Mereu, E. et al. Benchmarking single-cell RNA-sequencing protocols for cell atlas
projects. Nat. Biotechnol. 38, 747 – 755 (2020).
10. Zhang, M. et al. Single-cell transcriptomic architecture and intercellular crosstalk
of human intrahepatic cholangiocarcinoma. J. Hepatol. 73, 1118 – 1130 (2020).
11. Zhou, Y. et al. Single-cell RNA landscape of intratumoral heterogeneity and
immunosuppressive microenvironment in advanced osteosarcoma. Nat. Com-
mun. 11, 6322 (2020).
12. Niu, J. et al. Identi ﬁcation of Potential Therapeutic Targets and Immune Cell
Inﬁltration Characteristics in Osteosarcoma Using Bioinformatics Strategy. Front.
Oncol. 10, 1628 (2020).
13. Cao, S. et al. Reduction-responsive RNAi nanoplatform to reprogram tumor lipid
metabolism and repolarize macrophage for combination pancreatic cancer
therapy. Biomaterials 280, 121264 (2021).
14. Öhlund, D. et al. Distinct populations of in ﬂammatory
ﬁbroblasts and myo ﬁbro-
blasts in pancreatic cancer. J. Exp. Med . 214, 579 – 596 (2017).
15. Wu, S. Z. et al. Stromal cell diversity associated with immune evasion in human
triple-negative breast cancer. Embo J. 39, e104063 (2020).
16. Maier, B. et al. A conserved dendritic-cell regulatory program limits antitumour
immunity. Nature 580, 257 – 262 (2020).
17. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-cell data with
Harmony. Nat. Methods 16, 1289 – 1296 (2019).
18. Zhang, Q. et al. Landscape and dynamics of single immune cells in hepatocellular
carcinoma. Cell 179, 829 – 845.e820 (2019).
19. Cheng, S. et al. A pan-cancer single-cell transcriptional atlas of tumor in ﬁltrating
myeloid cells. Cell 184, 792 – 809.e723 (2021).
20. Berlato, C. et al. A CCR4 antagonist reverses the tumor-promoting micro-
environment of renal cancer. J. Clin. Invest . 127, 801 – 813 (2017).
21. Pere, H. et al. A CCR4 antagonist combined with vaccines induces antigen-
speciﬁc CD8 + T cells and tumor immunity against self antigens. Blood 118,
4853– 4862 (2011).
22. Newman, A. M. et al. Determining cell type abundance and expression from bulk
tissues with digital cytometry. Nat. Biotechnol. 37, 773 – 782 (2019).
23. Van de Sande, B. et al. A scalable SCENIC work ﬂow for single-cell gene regulatory
network analysis. Nat. Protoc. 15, 2247 – 2276 (2020).
24. Yu, G., Wang, L. G., Han, Y. & He, Q. Y. clusterPro ﬁler: an R package for comparing
biological themes among gene clusters. Omics 16, 284 – 287 (2012).
25. Hänzelmann, S., Castelo, R. & Guinney, J. GSVA: gene set variation analysis for
microarray and RNA-seq data. BMC Bioinforma. 14, 7 (2013).
26. Ren, J. et al. Histone methyltransferase WHSC1 loss dampens MHC-I antigen
presentation pathway to impair IFN- γ-stimulated antitumor immunity. J. Clin.
Invest. 132, e153167 (2022).
27. Cassetta, L. et al. Human tumor-associated macrophage and monocyte tran-
scriptional landscapes reveal cancer-speci ﬁc reprogramming, biomarkers, and
therapeutic targets. Cancer Cell 35, 588 – 602.e510 (2019).
28. Barkal, A. A. et al. CD24 signalling through macrophage Siglec-10 is a target for
cancer immunotherapy. Nature 572, 392 – 396 (2019).
29. Efremova, M., Vento-Tormo, M., Teichmann, S. A. & Vento-Tormo, R. CellPhoneDB:
inferring cell-cell communication from combined expression of multi-subunit
ligand-receptor complexes. Nat. Protoc. 15, 1484 – 1506 (2020).
30. Erdogan, B. et al. Cancer-associated ﬁbroblasts promote directional cancer cell
migration by aligning ﬁbronectin. J. Cell Biol. 216, 3799 – 3816 (2017).
31. Attieh, Y. et al. Cancer-associated ﬁbroblasts lead tumor invasion through
integrin-β3-dependent ﬁbronectin assembly. J. Cell Biol. 216, 3509 – 3520 (2017).
32. Zilionis, R. et al. Single-cell transcriptomics of human and mouse lung cancers
reveals conserved myeloid populations across individuals and species. Immunity
50, 1317 – 1334.e1310 (2019).
33. Guilliams, M. et al. Dendritic cells, monocytes and macrophages: a uni ﬁed
nomenclature based on ontogeny. Nat. Rev. Immunol. 14, 571 – 578 (2014).
34. Binnewies, M. et al. Unleashing type-2 dendritic cells to drive protective anti-
tumor CD4 + T cell immunity. Cell 177, 556 – 571.e516 (2019).
35. Ferris, S. T. et al. cDC1 prime and are licensed by CD4 + T cells to induce anti-
tumour immunity. Nature 584, 624 – 629 (2020).
36. Corrales, L., Matson, V., Flood, B., Spranger, S. & Gajewski, T. F. Innate immune
signaling and regulation in cancer immunotherapy. Cell Res. 27,9 6 – 108 (2017).
37. Jang, J. E. et al. Crosstalk between regulatory T cells and tumor-associated
dendritic cells negates anti-tumor immunity in pancreatic cancer. Cell Rep. 20,
558– 571 (2017).
38. Zhou, Y. et al. Activation of NF-
κB and p300/CBP potentiates cancer che-
moimmunotherapy through induction of MHC-I antigen presentation. Proc. Natl.
Acad. Sci. USA 118, e2025840118 (2021).
39. Algarra, I., Garrido, F. & Garcia-Lora, A. M. MHC heterogeneity and response of
metastases to immunotherapy. Cancer Metastasis Rev. 40, 501 – 517 (2021).
40. Garrido, F. & Aptsiauri, N. Cancer immune escape: MHC expression in primary
tumours versus metastases. Immunology 158, 255 – 266 (2019).
41. Morrissey, M. A., Kern, N. & Vale, R. D. CD47 ligation repositions the inhibitory
receptor sirpa to suppress integrin activation and phagocytosis. Immunity 53,
290– 302.e296 (2020).
42. Mohanty, S., Aghighi, M., Yerneni, K., Theruvath, J. L. & Daldrup-Link, H. E.
Improving the ef ﬁcacy of osteosarcoma therapy: combining drugs that turn
cancer cell ‘don’t eat me ’ signals off and ‘eat me ’ signals on. Mol. Oncol. 13,
2049– 2061 (2019).
43. Fang, S. et al. Anti-CD47 antibody eliminates bone tumors in rats. Saudi J. Biol. Sci.
26, 2074 – 2078 (2019).
44. Advani, R. et al. CD47 Blockade by Hu5F9-G4 and Rituximab in Non-Hodgkin ’s
Lymphoma. N. Engl. J. Med. 379, 1711 – 1721 (2018).
45. Fujiwara, S. et al. Acquisition of cancer stem cell properties in osteosarcoma cells
by de ﬁned factors. Stem Cell Res. Ther. 11, 429 (2020).
46. Tang, J. et al. Increased expression of CD24 is associated with tumor progression
and prognosis in patients suffering osteosarcoma. Clin. Transl. Oncol. 15, 541– 547
(2013).
47. Zhou, Z. et al. The CD24 + cell subset promotes invasion and metastasis in human
osteosarcoma. EBioMedicine 51, 102598 (2020).
48. Bradley, C. A. CD24 - a novel ‘don’t eat me ’ signal. Nat. Rev. Cancer 19, 541 (2019).
49. Liu, Y. et al. Single-cell transcriptomics reveals the complexity of the tumor micro-
environment of treatment-naive osteosarcoma.Front. Oncol. 11, 709210 (2021).
50. Butler, A., Hoffman, P., Smibert, P., Papalexi, E. & Satija, R. Integrating single-cell
transcriptomic data across different conditions, technologies, and species. Nat.
Biotechnol. 36, 411 – 420 (2018).
51. Ritchie, M. E. et al. limma powers differential expression analyses for RNA-
sequencing and microarray studies. Nucleic Acids Res . 43, e47 (2015).
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons license, and indicate if changes were made. The images or other third party
material in this article are included in the article ’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons license and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this license, visit http://
creativecommons.org/licenses/by/4.0/.
© The Author(s) 2023
Characterizing tumor microenvironment in osteosarcoma
W Liu et al.
12
Bone Research            (2023) 11:4 