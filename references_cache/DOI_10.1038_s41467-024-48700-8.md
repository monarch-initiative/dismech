---
reference_id: "DOI:10.1038/s41467-024-48700-8"
title: Single-cell and spatial transcriptomics analysis of non-small cell lung cancer
authors:
- Marco De Zuani
- Haoliang Xue
- Jun Sung Park
- Stefan C. Dentro
- Zaira Seferbekova
- Julien Tessier
- Sandra Curras-Alonso
- Angela Hadjipanayis
- Emmanouil I. Athanasiadis
- Moritz Gerstung
- Omer Bayraktar
- Ana Cvejic
journal: Nature Communications
year: '2024'
doi: 10.1038/s41467-024-48700-8
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-024-48700-8.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41467-024-48700-8.pdf
---

# Single-cell and spatial transcriptomics analysis of non-small cell lung cancer
**Authors:** Marco De Zuani, Haoliang Xue, Jun Sung Park, Stefan C. Dentro, Zaira Seferbekova, Julien Tessier, Sandra Curras-Alonso, Angela Hadjipanayis, Emmanouil I. Athanasiadis, Moritz Gerstung, Omer Bayraktar, Ana Cvejic
**Journal:** Nature Communications (2024)
**DOI:** [10.1038/s41467-024-48700-8](https://doi.org/10.1038/s41467-024-48700-8)

## Content

AbstractLung cancer is the second most frequently diagnosed cancer and the leading cause of cancer-related mortality worldwide. Tumour ecosystems feature diverse immune cell types. Myeloid cells, in particular, are prevalent and have a well-established role in promoting the disease. In our study, we profile approximately 900,000 cells from 25 treatment-naive patients with adenocarcinoma and squamous-cell carcinoma by single-cell and spatial transcriptomics. We note an inverse relationship between anti-inflammatory macrophages and NK cells/T cells, and with reduced NK cell cytotoxicity within the tumour. While we observe a similar cell type composition in both adenocarcinoma and squamous-cell carcinoma, we detect significant differences in the co-expression of various immune checkpoint inhibitors. Moreover, we reveal evidence of a transcriptional “reprogramming” of macrophages in tumours, shifting them towards cholesterol export and adopting a foetal-like transcriptional signature which promotes iron efflux. Our multi-omic resource offers a high-resolution molecular map of tumour-associated macrophages, enhancing our understanding of their role within the tumour microenvironment.

Article https://doi.org/10.1038/s41467-024-48700-8
Single-cell and spatial transcriptomics
analysis of non-small cell lung cancer
Marco De Zuani 1,2,3,4,11, Haoliang Xue 1,2,3,4,11,J u nS u n gP a r k1,2,5,
Stefan C. Dentro5,6,Z a i r aS e f e r b e k o v a5,J u l i e nT e s s i e r7, Sandra Curras-Alonso8,
Angela Hadjipanayis7, Emmanouil I. Athanasiadis 2,9,M o r i t zG e r s t u n g2,5,6,
Omer Bayraktar 1,2 & Ana Cvejic 1,2,3,10
Lung cancer is the second most frequently diagnosed cancer and the leading
cause of cancer-related mortality worldwide. Tumour ecosystems feature
diverse immune cell types. Myeloid cells, in particular, are prevalent and have a
well-established role in promoting the disease. In our study, we proﬁle
approximately 900,000 cells from 25 treatment-naive patients with adeno-
carcinoma and squamous-cell carcinoma by single-cell and spatial tran-
scriptomics. We note an inverse relationship between anti-inﬂammatory
macrophages and NK cells/T cells, and with reduced NK cell cytotoxicity within
the tumour. While we observe a similar cell type composition in both adeno-
carcinoma and squamous-cell carcinoma, we detect signiﬁcant differences
in the co-expression of various immune checkpoint inhibitors. Moreover, we
reveal evidence of a transcriptional“reprogramming” of macrophages in
tumours, shifting them towards cholesterol export and adopting a foetal-like
transcriptional signature which promotes iron efﬂux. Our multi-omic resource
offers a high-resolution molecular mapof tumour-associated macrophages,
enhancing our understanding of their role within the tumour
microenvironment.
Lung cancer is the second most commonly diagnosed cancer and the
ﬁrst cause of cancer death worldwide1, with a 5-year survival of ~6% in
patients with the most advanced stages 2. Non-small-cell lung cancer
(NSCLC) is the most common type of lung cancer (~85% of total cases),
followed by small-cell lung cancer (15% of total cases)
3.L u n gc a n c e ri sa
complex disease in which the tumour microenvironment plays a cri-
tical role and macrophages (M ɸ) are intimately involved in the pro-
gression of the disease. In particular, tumour-associated M ɸ (TAMs)
can exhibit a dual role, contributing to tumour promotion by
suppressing the immune response, facilitating angiogenesis, and aid-
ing in tissue remodelling, but also tumour suppression by promoting
inﬂammation and engaging in cytotoxic activity against cancer cells
4,5.
The intricate interplay between lung cancer and M ɸ highlights the
importance of understanding their dynamic relationship in order to
develop more effective therapeutic strategies.
Within NSCLC, adenocarcinoma (LUAD) is the most common
histological subtype, followed by squamous-cell carcinoma (LUSC).
Lobectomy (i.e., the anatomical resection of a lung lobe) is currently
Received: 2 November 2023
Accepted: 8 May 2024
Check for updates
1Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, UK.2OpenTargets, Wellcome Genome Campus, Hinxton, UK.3Department of Haema-
tology, University of Cambridge, Cambridge, UK.4Wellcome Trust— Medical Research Council Cambridge Stem Cell Institute, Cambridge, UK.5European
Molecular Biology Laboratory, European Bioinformatics Institute EMBL-EBI, Wellcome Genome Campus, Hinxton, UK.6Division of Artiﬁcial Intelligence in
Oncology, DKFZ, Heidelberg, Germany.7Precision Medicine and Computational Biology, Sanoﬁ, Cambridge, MA, USA. 8Precision Medicine and Computa-
tional Biology, Sanoﬁ, Paris, France. 9Medical Image and Signal Processing Laboratory (MEDISP), Department of Biomedical Engineering, University of West
Attica, Athens, Greece. 10Biotech Research & Innovation Centre (BRIC), University of Copenhagen, Copenhagen, Denmark.11These authors contributed
equally: Marco De Zuani, Haoliang Xue. e-mail: ana.cvejic@bric.ku.dk
Nature Communications|         (2024) 15:4388 1
1234567890():,;
1234567890():,;

the gold standard for the treatment of early stages of NSCLC (stage I/
II), while patients with unresectable stage III or metastatic stage IV
NSCLC are treated with a combination of chemotherapy and neoad-
juvant targeting vascular endothelial growth factor (VEGF) or immune
checkpoint inhibitors (ICIs) like PD1, PDL1 and CTLA4. Advancements
made in the last decade in uncovering predictive biomarkers have
paved the way for novel therapeutic prospects in theﬁelds of targeted
therapy and immunotherapy on the basis of tumour histology and
PDL1 expression
6.
A number of studies have employed single-cell technologies to
explore transcriptional changes in NSCLC 7–9.T h e yh a v ee x t e n s i v e l y
examined the lung tumour microenvironment revealing diverse T-cell
functions linked to patient prognosis, relevance of diversity of B cells
in NSCLC for anti-tumour therapy, multiple states of tumour-
inﬁltrating myeloid cells, proposing them as a new target in immu-
notherapy, as well as the association of tissue-resident neutrophils
with anti-PDL1 therapy failure
7,10–14. They further unveiled tumour
heterogeneity and cellular changes in advanced and metastatic
tumours
8,9 as well as tumour therapy-induced transition of cancer cells
to a primitive cell state15. In many of these studies, a limited number of
cells was analysed per patient, and often there was no systematic
collection of patient-matched non-tumour tissue, thus restricting dis-
section of the biological heterogeneity within tumour and adjacent
non-tumour tissue. Additionally, with some exceptions
9,14,L U A Da n d
LUSC were considered as a single entity thus hindering the investiga-
tion of speciﬁc hallmarks of the two cancer types which are radically
distinct both at the molecular and pathological level. While single-cell
RNA-seq (scRNA-seq) can identify cell types and their states at high
resolution within tissues, it lacks the capability to pinpoint their spatial
distribution or capture the local cell–cell interactions as well as ligands
and receptors that mediate these interactions. Therefore, impeding
our ability to fully explore the tumour microenvironment (TME) and
the complexity of cell–cell interactions therein.
To overcome above mentioned limitations, we combined scRNA-
seq data from nearly 900,000 cells from 25 treatment-naive patients
with LUAD or LUSC and spatial transcriptomics from eight patients to
investigate the differences in cellular organisation in tumour and
adjacent non-tumour tissue. We further examined Mɸ populations and
molecular changes they undergo in the tumour environment, some of
which resemble those observed in M ɸ during human foetal
development.
Results
ScRNA-seq and spatial atlas of NSCLC samples
To determine the heterogeneity of immune and non-immune cellular
states and their spatial landscape in LUAD and LUSC, we collected lung
tissue resections from 25 treatment-naive patients with either LUAD
(n =1 3 ) ,L U S C(n = 8) or undetermined lung cancer (LC,n =4 ) ,a n dt w o
healthy deceased donors (Fig. 1A, B and Supplementary Data 1). We
collected both tumour and matched normal non-tumorigenic tissue
(i.e., background), isolated CD45+ immune cells (Supplementary
Fig. 1A) as well as tumour and other non-immune populations (using
CD235a column to deplete erythroid cells), and performed scRNA-seq.
In addition, tumour and background tissue sections from eight
patients (of the aforementioned 25) were processed for spatial tran-
scriptomics using the 10x Genomics Visium platform (n =3 6 s e c t i o n s
in total) (Fig. 1A and Supplementary Data 1).
Tumours exhibit a higher diversity of immune and non-immune
cells compared to adjacent lung tissue
Following quality control (QC) on the scRNA-seq dataset, we identiﬁed
895,806 high-quality cells in total, of which 503,549 were from
tumour and 392,257 from combined background and healthy tissue
(from here on referred to as B/H). After performing normalisation and
log1p transformation, highly-variable gene selection, dimensionality
reduction, batch correction, and Leiden clustering, cells originating
from tumour and B/H were separately annotated into distinct broad
cell types and visualised via Uniform Manifold Approximation and
Projection (UMAP) (Fig.1C, Supplementary Fig. 1B, C, and“Methods”).
We identiﬁed clusters of myeloid cells with transcriptional signatures
of monocytes, macrophages, dendritic cells (DCs), as well as mast cells,
natural killer (NK) cells, T cells, B cells and non-immune cells
(Fig. 1C, D). We did not detect neutrophilic granulocytes, most prob-
ably due to their sensitivity to degradation after collection and in
particular to the freezing-thawing cycle. Finally, we identiﬁed a cluster
characterised by the co-expression of myeloid (LYZ, CD68, CD14, MRC1)
and epithelial genes ( KRT19, EPCAM )( F i g .1D–F). These cells were
found within the tumour and exhibited similarities to previously
described cancer-associated macrophage-like cells (CAMLs)
16–18.
CAMLs represent a distinct population of large myeloid cells with
concomitant epithelial tumour protein expression 19. These unique
cells have been observed in blood samples of patients with various
malignancies, including NSCLC
20. The abundance of CAMLs exhibits a
direct correlation with response to therapeutic interventions, high-
lighting their functional signiﬁcance
21. Even after further subclustering,
CAMLs maintained their distinct dual myeloid-epithelial signature
(Supplementary Fig. 1D). It is noteworthy that doublet detection soft-
ware Scrublet assigned a low doublet score to CAMLs, suggesting their
expression proﬁle is unlikely to be explained as a combined signature
arising from the coincidental sequencing of a tumour cell and a mac-
rophage (Supplementary Fig. 1E). All clusters included cells from
multiple patients, with the cluster size ranging from 2520 to 124,459
cells (Supplementary Fig. 1F, G). Furthermore, we conducted
reference-query mapping using scArches
22 to conﬁrm the consistency
of our annotations in the tumour and B/H dataset (Supplementary
Fig. 2A–C and Supplementary Notes).
The composition of the immune and non-immune compartment
was markedly different between the tumour and background. In the
tumour, we detected ﬁbroblasts and a decrease in the fraction of
lymphatic endothelial cells (LECs) (P
adj = 0.0025, Fig. 1G and Supple-
mentary Data 2). Furthermore, the population of epithelial cells
showed higher diversity, with the presence of alveolar type II (AT2),
atypical epithelial cells which downregulated epithelial markers
(KRT19, EPCAM, CDH1), transitioning epithelial cells which upregulated
myeloid markers (LYZ), and cycling epithelial cells in tumour tissues
(Fig. 1G, Supplementary Notes, and Supplementary Fig. 2D, E). These
differences are in agreement with the fact that in tumour specimens,
epithelial cells are likely to be a mixture of mutant tumour and non-
mutant normal cells, and suggest that neoplastic transformation leads
to further diversity of cell states. We did not detect alveolar type I (AT1)
or basal cells, possibly due to their loss during dissociations, as pre-
viously reported by others
8.
As previously reported, the proportion of monocytes and imma-
ture myeloid cells was signiﬁcantly reduced in tumour samples com-
pared to background (Padj =0 . 0 2 2a n dPadj = 0.00001, respectively)7,
while DCs and B cells were overall expanded 7 (Padj =0 . 0 0 2 3a n d
Padj = 0.0044, respectively; Fig.1H and Supplementary Data 3). To get
further insight into the cellular c omposition of tumour versus back-
ground tissue, we subclustered each of the broad clusters and identiﬁed
46 cell types/states (Supplementary Fig. 2D, E, Supplementary
Data 4 and 5, Supplementary Fig. 3, and Supplementary Notes). In the
tumour, we found that a signiﬁcantly higher proportion of NK cells had
a lower cytotoxicity phenotype (Supplementary Notes), and that the
signiﬁcant majority of DCs were derived from monocytes (i.e., mo-DC2),
(Supplementary Notes) compared to background (P
adj = 0.00002 and
Padj = 0.00002, respectively, Fig.1I and Supplementary Data 6). This is
consistent with the monocytic origin of mo-DC2s under inﬂammatory
conditions23. Similarly, we found an expansion of B cells expressingLYZ
and TNF, and depletion of NKB cells (Fig.1Ia n dS u p p l e m e n t a r yN o t e s ) .
Among T cells, tumour samples showed an accumulation of regulatory
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 2

T cells (Tregs), known to hinder the immune surveillance of tumours24
(Fig.1I). Conversely, there was a reduction of exhausted cytotoxic T cells
(Padj = 0.00002) in the tumour and absence of γδ T cells, which have
been associated with survival in NSCLC 25 (Fig. 1Ia n dS u p p l e m e n t a r y
Data 6). γδ T cells are capable of recognising and lysing diverse ranges
of cancer cells, and thus have been suggested for a role in pan-cancer
immunotherapy26. Finally, we saw an increase in heterogeneity and
proportion of anti-inﬂammatory Mɸ (AIMɸ), with a subset of cycling
anti-inﬂammatory Mɸ, STAB1+M ɸ (Fig. 1I) and CAMLs (Fig. 1H) being
abundantly present in tumour tissue. Interestingly, we found a strong
Broad immune subsets
Tumour
Background
T cells
B cells **
Macrophages
DCs **
Mast cells
Immature myeloid***
Monocytes *
CAMLs
NK cells
0
100
80
40
60
20Percentage of total
10x Genomics scRNA-seq (N=24 patients)
Unenriched
&
CD45+
A
D E
H
I
G
CB
10x Genomics Visium (N=8 patients)
TUMOUR HEALTHY + BACKGROUND
UMAP2
UMAP1
UMAP3
UMAP2
10080604020
Fraction of cells 
in group (%)
01
Mean expression
in group
EPCAMKR
T19
CD79ACD3DNKG7CPA3CCL17CD1EMRC1MARCO
IL1BFCN1CD14CD68
Monocytes
Macrophages
Immature myeloid
CAMLs
DCs
Mast cells
NK cells
T cells
B cells
Non-immune
LYZ
Non-immune subsets
Tumour
Background
0
100
80
40
60
20
AT2 cells
Cycling AT2 cells
Ciliated epithelial cells
Atypical epithelial cells
Transitioning epithelial cells
Cycling epithelial cells
Club cells
Fibroblasts
Activated adventitial fibroblasts
Lymphatic endothelial cells **
Percentage of total
T1
T2
T3
T4
NC
Healthy LUAD LUSC
Tumour stage
Female
Male
scRNA-seq
scRNA-seq
10x Visium
Tumour 
resection
Background
NK cell subsets:
Higher 
cytotoxicity
Lower
cytotoxicity
Tumour
Background
***
***0
100
80
40
60
20
DC subsets:
Cycling mo-DC2
Cycling cDC2
mo-DC2 ***
cDC2 ***
pDCs
100
80
40
60
20
0
Tumour
Background
Cycling plasma B
B cells
Downregulated B
TNF+ B
LYZ+ B
Plasma B
Immature plasma B
NKB cells
B cell subsets:
100
80
40
60
20
0
Tumour
Background
Downregulated T
Naive T
Cycling T
Cycling cytotoxic T
Exhausted
cytotoxic T
Exhausted T
Cytotoxic T
Cycling exhausted
cytotoxic T
Tregs
γδ T
T cell subsets:
Tumour
Background
100
80
40
60
20
0
***
Cycling anti-inflammatory MΦ
STAB1+ MΦ
Anti-inflammatory MΦ ***
Alveolar MΦ ***
Cycling alveolar MΦ
100
80
40
60
20
0
Tumour
Background
Macrophage subsets:
Percentage of total
F
LYZ APOE CD68 MRC1 EPCAM KRT8 KRT19
8
6
2
0
4Norm-log-scaled counts
Epithelial cells (AT2)
Macrophages (AIMΦ)
CAMLs
EPCAM
LYZ
-1 0 2 3 1
8
6
4
2
0
Epithelial cells (AT2)
Macrophages (AIMΦ)
CAMLs
EPCAM
CD68
-1 0 2 3 1
8
6
4
2
0
4
EPCAM
MRC1
-1 0 2 3 1
8
6
4
2
0
45
Macrophages
Monocytes
CAMLs
DCs
Mast cells
Immature cells
B cells
T cells
NK cells
Non-immune
Fig. 1 | Single-cell transcriptomics reveal the heterogeneity of NSCLC. AStudy
overview. Single-cell suspensions of resected tumour tissue, adjacent non-involved
tissue (background) and healthy lung from deceased donors were enriched for
CD45+ or CD235− and subjected to scRNA-seq. Cryosections of fresh,ﬂash-frozen
tumour, background and healthy tissues were used for 10x Visium spatial tran-
scriptomics.B Cohort overview. Symbols represent individual patients and per-
formed analyses. C UMAP projection of tumour and combined background
+healthy datasets.D Dotplot of representative genes used for broad cell-type
annotations in tumour samples.E Contour plot showing the co-expression of
myeloid (LYZ, CD68, MRC1) and epithelial (EPCAM) genes in AT2 cells (44,399 cells),
CAMLs (2520 cells) and AIMɸ (16,120 cells). Normalised, scaled and log-
transformed gene expression.F Boxplot showing normalised, scaled and log-
transformed gene expression of myeloid (LYZ, APOE, CD68, MRC1) and epithelial
(EPCAM, KRT8, KRT19) genes in AT2 cells, CAMLs and AIM ɸ. Boxes: quartiles.
Whiskers: 1.5× interquartile range.G Relative proportion of non-immune cell sub-
sets in tumour and background, calculated within the CD235− enrichment. Arrows
indicate increase (↑)o rd e c r e a s e(↓) in tumour versus background. Pairwise
comparisons by two-sided Wilcoxon rank test and Bonferroni correction for mul-
tiple comparisons. **P < 0.01. Arrows without asterisks indicate that the cell type
was found only in tumour or background.H Relative proportion of broad immune
cells in tumour and background, calculated within all immune cells identiﬁed in the
CD235- enrichment. Arrows indicate an increase (↑)o rd e c r e a s e(↓) in tumour
versus background. Pairwise comparisons by two-sided Wilcoxon rank test and
Bonferroni correction for multiple comparisons. *P <0 . 0 5 ,* *P < 0.01, ***P <0 . 0 0 1 .
Arrows without asterisks indicate that the cell type was found only in tumour or
background.I Relative proportion of NK, DC, B, T and macrophage subsets within
the broad annotations in tumour and background, calculated within the CD235-
enrichment. Arrows indicate increase (↑)o rd e c r e a s e(↓) in tumour versus back-
ground. Pairwise comparisons by two-sided Wilcoxon rank test and Bonferroni
correction for multiple comparisons. ***P < 0.001. Arrows without asterisks indicate
that the cell type was found only in tumour or background.
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 3

negative correlation between the frequency ofSTAB1+M ɸ/AIMɸ and T/
NK cells across patients, highlighting the key role of Mɸ in restraining
the inﬁltration of cytotoxic cells in the lung tumour tissue (Fig.2A). This
is in line with a recent work describing that monocyte-derived M ɸ in
h u m a nN S C L Ca c q u i r ea ni m m u n o s u ppressive phenotype and restrain
the inﬁltration of NK cells27.
LUAD and LUSC have similar cellular composition but utilise
different cell–cell interaction networks
LUAD and LUSC have very different prognoses and are often con-
sidered as different clinical entities 28. To examine if differences in
clinical features stem from distinct cellular composition, we compared
the frequency of immune and non-immune cell subsets within CD235-
samples from LUAD versus LUSC patients. We observed minor differ-
ences in cell frequency that did not reach statistical signiﬁcance afterP
value correction (Supplementary Fig. 4A and Supplementary
Data 7 and 8). Furthermore, there was no clear association between the
frequency of immune and non-immune cells observed in patients and
the cancer subtype, cancer stage or sex (Supplementary Fig. 4B, C),
suggesting that the TME composition is rather similar in LUAD and
LUSC. While LUAD and LUSC shared similar cellular compositions, the
observed clinical distinctions may arise from varying intercellular
A
Tregs
TNF+ B cells
STAB1+ MΦ
Monocytes
Plasma B cells
pDCs
NK cells (LC)
NK cells (HC)
mo−DC2
Mast cells
L YZ+ B cells
Immature myeloid cells
Fibroblasts
Exhausted T
Exhausted CTL
Downregulated B cells
Cycling T cells
Cycling plasma B cells
Cycling mast cells
Cycling exhausted CTL
Cycling EC
Cycling AT2 cells
Cycling AIMΦ
Ciliated EC
cDC2
CAMLs
B cells
Atypical EC
AT2 cells
AIMΦ
AMΦ
Activ. adv. fibrobl.
MIF
HBEGF
EREG
AREG
EGFR
Cycling EC
Cycling
AT2 cells
AT2 cells
F
B
STAB1+ MΦ
Monocytes
pDCs
mo−DC2
Mast cells
Cycl. plasma B
Cycl. mast cells
Cycl. EC
Cycl. AT2 cells
Cycl. AIMΦ
Ciliated EC
cDC2
CAMLs
AT2 cells
AIMΦ
AMΦ
Activ. adv. fibrobl.
VEGFB
VEGFA
NRP2
NRP1
KDR
FLT1
LEC
Fibroblasts
STAB1+ MΦ
pDCs
Cycling EC
Cycling AT2 cells
Cycling AIMΦ
Ciliated EC
CAMLs
AT2 cells
AIMΦ
AMΦ
Activ. adv. fibrobl.
Common
LUAD
LUSC
E
Tregs
STAB1+ MΦ
Monocytes
NK cells (LC)
NK cells (HC)
Naive T cells
mo−DC2
Exhausted T cells
Exhausted CTL
Cytotoxic T
Cycling TCycling mast cells
Cycling exhausted CTL
Cycling AIMΦ
cDC2
CAMLs
AIMΦ
AMΦ
pDCs
LEC
Immature myeloid
Fibroblasts
Cycling EC
Cycling AT2 cells
AT2 cells
Activ. adv. fibrobl.
STAB1+ MΦ
Monocytes
mo−DC2
Cycling mast cells
Cycling AIMΦ
cDC2
CAMLs
AIMΦ
AMΦ
TIGIT
HAVCR2
CTLA4
CD96
CD226
NECTIN3
NECTIN2
NECTIN1
LGALS9
CD86
CD80
 Common
LUAD
LUSC
C
D
CTLA4CD80CD86TIM3
LGALS9
TIGITDNAM1NECTIN2NECTIN3
CD96
NECTIN1
PD1PDL1
Tregs
Naive T cells
CTL
Cycling T cells
Exhausted T cells
Exhausted CTL
Cycling exhausted CTL
NK cells (HC)
NK cells (LC)
Monocytes
Anti-inflammatory MΦ
STAB1+ MΦ
Alveolar MΦ
Cycling AIMΦ
CAMLs
AT2 cells
Cycling AT2 cells
Fraction of cells
in group (%)
20406080100
Mean expression
LUAD
LUSC
01
01
-1
-0.8
-0.6
-0.4
-0.2
0
0.2
0.4
0.6
0.8
1
CTL
NK cell
s (LC)
Naiv
eT cells
NK cells (HC)
Do
wnreg. T cellsExhausted CTL
Tregs
Exhausted T cells
B cells
LYZ+ B cellsCycling T cells
Cycl. plasma B cells
TNF + B cells
Mast cells
Cycl. mast cellsDownreg. B cells
Cycl.
exhausted CTLPlasma B cells
Monocytes
pDCs
Cycl. AIMΦ
AM
Φ
Immature
myeloid
CAMLscDC2
STAB1+ M
Φ
mo
 DC2AIM
Φ
 NK cells (HC)
CTL
 NK cells (LC)
 Naive T cells
 Downregulated T cells
 Exhausted CTL
Tregs
 Exhausted T cells
 B cells
L YZ+ B cells
 Cycling T cells
 Cycling plasma B cells
 TNF + B cells
 Mast cells
 Cycling mast cells
 Downregulated B cells
 Cycling exhausted CTL
 Plasma B cells
Monocytes
 pDCs
 Cycling AIMΦ
AIMΦ
 AMΦ
 Immature myeloid cells
 CAMLs
 cDC2
 STAB1+ MΦ
 mo DC2
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
** **
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
**
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
LUAD LUSC
Non-immune
Immature myeloid
CAMLs
Monocytes
Macrophages
Mast cells
DCsNKsB cellsT cells
Macrophages
Non-immune
T cells
DCs
Monocytes
CAMLs
NKs
B cells
Mast cells
Immature myeloid
Non-immune
Immature myeloid
CAMLs
Monocytes
Macrophages
Mast cells
DCsNKsB cellsT cells
0200400600800
N of LR pairs
Fig. 2 | Integrated single cell and spatial transcriptomics uncovers different
interaction networks in LUAD and LUSC. A Heatmap showing the Pearson cor-
relation between the relative cell-type abundance for each immune cell type (cal-
culated within the CD235− enrichment). Colour indicates the Pearson correlation
value, asterisks indicate the level of signiﬁcance of the two-sided association test
computed on Pearson’s product-moment correlation coefﬁcients (*P <0 . 0 5 ,
**P < 0.01, ***P < 0.001).B Heatmap showing the number of LR interactions between
all cell types summarised by broad cell annotations in LUAD (left) and LUSC (right).
Rows were hierarchically clustered using the complete linkage method on eucli-
dean distances. C Sankey diagram showing the tumour-speciﬁc interactions in
LUAD and LUSC for selected ICIs detected by cellphoneDB. Line colour identiﬁes
whether the LR interaction between each cell type was found in LUAD only
(orange), in LUSC only (green) or in both tumour types (blue).D Dotplot for the ICI
genes and cell types highlighted in (C), split by tumour type. The size of each dot
represents the percentage of cells in the cluster expressing the gene, while the
colour represents the mean normalised scaled log-transformed expression of each
gene in each group. E Sankey diagram showing the tumour-speciﬁc interactions in
LUAD and LUSC for VEGFA/B interactors detected by cellphoneDB. Line colour
identiﬁes whether the LR interaction between each cell type was found in LUAD
only (orange), in LUSC only (green) or in both tumours (blue). F Sankey diagram
showing the tumour-speciﬁc interactions in LUAD and LUSC for EGFR interactors
detected by cellphoneDB. Line colour identiﬁes whether the LR interaction
between each cell type was found in LUAD only (orange), in LUSC only (green) or in
both tumours (blue).
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 4

interactions. Therefore, we examined whether different cell –cell
interaction networks were employed within the TME in LUAD versus
LUSC. To this end, we identiﬁed a putative list of cell–cell interactions
exclusively observed in each tumour type environment by inferring
statistically signiﬁcant ligand –receptor pairs (L –Rs) that were not
detected in background or healthy and their corresponding cell types,
using CellPhoneDB
29. Although the two tumour subtypes showed a
similar interaction network that mostly involved interactions between
non-immune cells, AIMɸ and T cells (Fig. 2B), there were also some
notable differences.
First, we identiﬁed overall a higher number of L –Rs in the LUAD
dataset (Supplementary Fig. 4D and Supplementary Data 9–12), which
was not driven by a difference in the number of cells in the LUAD
(n = 105,749 cells) vs LUSC ( n = 230,066 cells) dataset. Secondly, sev-
eral pairs of immune checkpoint inhibitors (ICI) and their respective
inhibitory molecules were differentially co-expressed in LUAD versus
LUSC (Fig. 2C, D). For example, LGALS9-HAVCR2 (TIM3), NECTIN2-
CD226 (DNAM1)and NECTIN2/NECTIN3-TIGITwere frequently identiﬁed
in LUAD, and the putative ICICD96-NECTIN1was found preferentially in
LUSC (Fig. 2C, D). In contrast, CD80/CD86-CTLA4 and HLAF-LILRB1/2
were found in both tumour subtypes (Fig.2C, D). LILRBs (leucocyte Ig-
like receptors) are emerging as potential targets for next-generation
immunotherapeutics as their blocking can potentiate immune
responses
30. The most commonly used immunotherapies for lung
cancer block the interaction between PD1 and PDL1, and recent clinical
trials suggested that anti-CTLA4 and anti-PD1 combination therapy
improved the survival of patients independent of tumour PD1
expression
31,32. Within our dataset, we did not observe PD1-PDL1
interactions in either of the tumour subtypes (Fig. 2C, D). Our initial
analysis suggests that other ICIs (such as CTLA4, TIGIT, LILRB1/2 and
TIM3) might be promising targets in the treatment of NSCLC.
Of the signiﬁcant L–Rs detected in both LUAD and LUSC we noted
several pairs involved in angiogenic signalling in different populations
of myeloid cells such asVEGFA/B-FLT1, VEGFA-KDRand VEGFA-NRP1/2.
AlthoughVEGFA and VEGFB were found to be expressed in both LUAD
and LUSC, their receptors were more frequently found in LUAD,
especially in ﬁbroblasts (Fig.2E and Supplementary Fig. 4E). Similarly,
we observed signiﬁcant expression of EGFR ligands signalling in AT2
and cycling epithelial cells, such as EGFR-EREG, EGFR-AREG, EGFR-
HBEGF and EGFR-MIF, although MIF expression was found more fre-
quently in cells from LUSC (Fig.2F and Supplementary Fig. 4F). Finally,
we observed key co-stimulatory signals required to support lymphoid
cell activation, such as CD40-CD40LG, CD2-CD58, CD28-CD86, CCL21-
CCR7,a n dTNFRSF13B/C-TNFSF13B(TACI/BAFFR-BAFF) (Supplementary
Fig. 4G), which are often associated with the presence of ectopic
lymphoid organs mainly consisting of B cells, T cells, and DCs i.e.,
tertiary lymphoid structures (TLS). TLS are usually correlated with the
longer relapse-free survival in NSCLC
33.
Integration of scRNA-seq and spatial transcriptomics validates
L–R interactions in situ
The signiﬁcant L–Rs and their interacting cell types were calculated
based on the co-expression of genes in different cell-type clusters from
the scRNA-seq dataset using CellPhoneDB. However, in order to dis-
cern biologically signi ﬁcant interactions, it is essential to ascertain
whether the cell types identi ﬁed as interacting are indeed physically
co-located. To achieve this, we considered how the scRNA-seq-
identiﬁed cell types are spatially arranged on tissue sections. We
applied an integrative approach which combines the scRNA-seq of the
tumour and background samples with the spatial transcriptomic (STx)
proﬁle of the fresh frozen tumour and background tissue sections. We
performed 10× Visium on two consecutive, 10-µms e c t i o n s ,f r o me i g h t
patients, seven of which matched the samples used for the scRNA-seq.
We analysed 36 sections in total (n
tumour =2 0 ,nbackground=1 6 )w i t ha n
average UMI count of 6894/spot in tumour and 3350/spot in the
background. Next, we used cell2location 34 and cell-type speci ﬁc
expression proﬁles from our scRNA-seq dataset to deconvolute cell-
type abundances on the tissue (Fig. 3A, see “Methods”).
O n c et h ec e l lt y p e sw e r er e s o l v e do nt h et i s s u es e c t i o n s ,w e
examined the frequency of different cell types across all sections from
tumour and background tissue. The cell-type abundance in tumour
a n db a c k g r o u n dw e r ec o m p u t e db ys u m m i n gu pt h ep o s t e r i o r5 %
quantile (q05) value of estimated cell abundance by cell2location,
across spots that passed QC (“Methods”). Our analysis conﬁrmed that
the differences in the frequency of cell types across all sections
in tumour versus background was in line with the results obtained
in the scRNA-seq data (Fig. 3B). For example, in tumours we found
an increase in the proportion of B cells ( P
adj = 0.0372) and
cycling AT2 cells ( Padj = 0.0147) compared to the background tissue,
and a decrease in the proportion of immature cells (Padj = 0.0012), NK
cells ( Padj = 0.0012), and LECs ( Padj = 0.00077, Supplementary
Data 13 and 14). However, the proportions of other cell types estimated
from the scRNA-seq data or the STx data within the tumour or back-
ground showed some discrepancies (Supplementary Fig. 4H, I). This
was particularly evident within the non-immune populations, where
STx estimated higher proportions of LECs, activated adventitial
ﬁbroblasts and cycling subsets, compared to scRNA-seq. Disparities in
cell proportions between different methodologies were previously
shown by others
35,36, underscoring the potential in ﬂuence of distinct
sampling biases inherent to scRNA-seq and STx techniques like Visium.
In the case of scRNA-seq, variations in cell digestion sensitivity can lead
to differential representation of cell types. Meanwhile, with Visium,
discrepancies might arise from variations in the location of tumour
resections as well as differences in sample sizes compared to scRNA-
seq studies. Nevertheless, the overall concordance in the results
obtained by scRNA-seq and Visium suggests that our spatial“map” of
different cell types faithfully represents their distribution in the tissue.
Next, we examined the spatial co-localisation of the L –Rs identi-
ﬁed by cellphoneDB. The L–Rs were considered to co-localise if both
g e n e sw e r ee x p r e s s e di nt h es a m es p o ta n da b o v em e d i a nv a l u ef o rt h e
given genes across the section spots. We then compared the frequency
of spots in which L–R genes were colocalising versus non-colocalising
in the matched tumour versus background sections, using a χ
2 test
(“Methods”). Due to the low number of tissue blocks collected from
LUSC and LUAD patients (N LUSC =3 , N LUAD = 5), the statistical power
was not sufﬁcient to perform a comparative analysis between spatial
localisation of LUAD/LUSC-speciﬁcL –Rs. Nevertheless, we conﬁrmed
that several of the aforementioned tumour-speciﬁcL –Rs colocalized
signiﬁcantly more in tumour than in background sections, including
NRP1-VEGFA and the ICIs NECTIN2-TIGIT, LGALS9-HAVCR2,a n d CD96-
NECTIN1 (Fig. 3C–E and Supplementary Data 15 ). Consistent with the
cellphoneDB results, we found no signi ﬁcant colocalization of PD1-
PDL1 in the tumour sections.
CAMLs share similar copy number aberrations (CNAs) with
tumour cells
Tumour samples obtained from surgical resection contain both
malignant and residual normal epithelial cells. A signiﬁcant challenge
in scRNA-seq of human tumours lies in the differentiation of cancer
cells from non-malignant counterparts. Therefore, we applied Copy-
number Karyotyping of Tumors (CopyKAT
37) to discern genome-wide
aneuploidy within individual cells. The principle driving the compu-
tation of DNA copy number events from scRNA-seq data is rooted
in the notion that the expression levels of neighbouring genes
can provide valuable information to infer genomic copy numbers
within that speciﬁc genomic segment. Since aneuploidy is common in
human cancers, cells with genome-wide CNAs are considered as
tumour cells.
Analysis using CopyKAT revealed extensive, patient-speciﬁcC N A s
in tumour tissue (Fig. 4A and Supplementary Fig. 5A) but not in the
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 5

background. Within individual tumour samples, the CNAs were
detected in AT2 and cycling AT2 cells, and in some patients these
genetic alterations were shared between AT2/cycling AT2 cells and
atypical epithelial cells, suggesting a close lineage relationship
between different epithelial subpopulations (Fig.4A and Supplemen-
tary Fig. 5A). We con ﬁrmed this ﬁnding by inferring the trajectory of
non-blood cell populations in tumour using Partition-Based Graph
Abstraction (PAGA)
38. PAGA showed differentiation continuity
between AT2 cells, cycling AT2/epithelial cells, and atypical epithelial
cells on one side and ciliated epithelial cells and transitioning epithelial
c e l l so nt h eo t h e r( F i g .4B). Furthermore, blinded histological evalua-
tion conﬁrmed the overlap between pathologist-deﬁned tumour sites
and AT2 and cycling AT2 cells predicted by cell2location, suggesting
their tumour cells status (Fig. 4C). Less overlap was observed for aty-
pical epithelial cells (Fig. 4C). The differential expression analysis
(DEA) of AT2 cells from tumours compared to background showed
upregulation of genes involved in hypoxia, TP53 pathways, and
metabolic rewiring in tumours. AT2 cells in tumour-upregulated genes
involved both in glycolysis and oxidative phosphorylation (Fig.4Da n d
Supplementary Data 16). While the importance of glycolysis in tumour
A B
C D
EGFR−AREGCCL21−CCR7CD96−NECTIN1EGFR−HBEGFEGFR−EREGCTLA4−CD86
TNFRSF13C−TNFSF13B
PDCD1−CD274
TNFRSF13B−TNFSF13B
CD40−CD40LGNECTIN2−CD226
HLA-F−LILRB1CD28−CD86NRP2−VEGFANRP1−VEGFBFLT1−VEGFBCD2−CD58KDR−VEG
FA
NRP1−VEG
FA
FLT1−VEG
FA
EGFR−MIF
LGALS9−H
AVCR2
NECTIN2−TIGITHLA-F−LILRB2
P11
P17
P24
P19
P16
P25
P10
P15
LR pass?
YES
NO
padj
<0.05
>0.05
Tumour
LUAD
LUSC
CD2−CD58
CD96−NECTIN1
EGFR−HBEGF
EGFR−MIF
FLT1−VEGFA
FLT1−VEGFB
HLA-F−LILRB2
KDR−VEGFA
LGALS9−HAVCR2
NECTIN2−TIGIT
NRP1−VEGFA
NRP1−VEGFB
01 0 2 0 3 0
Percentage of colocalising spots
Background
Tumour
4.0
2.0
1.0
3.5
3.0
2.5
1.5
0.5
0.0
Anti-inflammatory MΦAT2 cells Tregs
0.00
0.10
0.02
0.04
0.06
0.08
0.30
0.20
0.15
0.10
0.05
0.00
0.25
0
25
50
75
100
Tumour
Background
Percentage abundance
Broad immune cells
Macrophages
B cells
CAMLs
DCs
Immature myeloid
Mast cells
NKs
Monocytes
T cells
Tumour
Background
0
25
50
75
100Percentage abundance
Non-immune cells
Activated adventitial 
fibroblasts
AT2 cells
Atypical ECs
Ciliated ECs
Club cells
Cycling AT2 cells
Cycling ECs
Fibroblasts
Lymphatic
endothelial cells
Transitioning ECs
***
*
**
**
*
E
Tumour (P10)Background (P10)
YES
NO
co-expression:
PD1−PDL1NECTIN2−TIGITNRP1−VEGFA CD96-NECTIN1 HAVCR2-LGALS9
Fig. 3 | 10x Visium con ﬁrms the spatial colocalization of key
ligand–receptor pairs. ASpatial images depicting the cell abundance estimated by
cell2location for AT2 cells, AIMɸ and Tregs on a representative tumour section.
B Relative proportion of immune (left) and non-immune (right) cell types calcu-
lated on the cell abundance estimations by cell2location in tumour and background
sections. Immune cells were grouped according to their broad annotations. Arrows
indicate an increase (↑) or a decrease ( ↓) in the tumour, compared to the back-
ground. Pairwise comparisons were performed with a two-sided Wilcoxon rank test
and Bonferroni correction for multiple comparisons. *P <0 . 0 5 ,* *P <0 . 0 1 ,
***P < 0.001. Arrows without asterisks indicate that the cell type was found only in
the tumour or background. Please refer to Supplementary Data 13 and 14 for the
exact P values. C Heatmap of spatial LR colocalization. LR gene pair co-expression
was estimated in each spot for all sections, and the frequency of colocalising vs.
non-colocalising spots in the tumour and background was compared using aχ
2 test
followed by Bonferroni multiple comparison correction. Dark-grey tiles indicate
that the frequency of colocalising gene pairs was signiﬁcantly different in tumour
and background sections. Green column annotations indicate the LR pairs which
were signiﬁcant in at least four out of eight patients. Row annotations indicate
tumour type.D Boxplot showing the frequency of colocalising LR pairs signiﬁcantly
different in tumour vs background in each section analysed. N = 8 patients. Boxes
are plotted with default settings in the Python Seaborn package, i.e., boxes show
quartiles with whisker length being 1.5 times the interquartile range. Source data is
provided as a Source Data ﬁle. E Spatial images depicting the location of spots in
which the LR pair was found co-expressed in tumour (top) and background (bot-
tom), for NRP1-VEGFA, NECTIN2-TIGIT, PD1-PDL1, CD96-NECTIN1and HAVCR2-
LGALS9. Representative sections from one patient.
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 6

cells is well-established39, it was recently reported that human NSCLC
use glucose and lactate to fuel the tricarboxylic acid (TCA) cycle40.I n
addition, the tumour AT2 cells were noted to express more LYPD3
compared to background AT2 cells (log2FC = 2.04, Padj = 0.039, Sup-
plementary Data 16), an adhesion protein which has previously been
connected to poor prognosis in NSCLC and is currently being targeted
in preclinical and clinical studies
41,42.
Interestingly, the population of CAMLs also showed substantial
CNAs that were similar to those of AT2 cells and cycling AT2 cells
f r o mt h es a m ep a t i e n t( F i g .4A, E and Supplementary Fig. 5A, B). To
measure the difference of the distribution of genomic gain and loss
between cell types in a statistically robust manner, we calculated the
Kullback–Leibler (KL) divergence (Fig.4F and Supplementary Fig. 5C).
CAMLs had KL divergence values comparable to CNA-harbouring
A 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 1819202122 X
Activ. adventitial fibrobl. (128)Tumour 8
AT2 cells (370)
Atypical epithelial cells (187)
CAMLs (205)
Ciliated epithelial cells (336)
Fibroblasts (322)
Immune cells (25346)
Transitioning epithelial cells (408)
AT2 cells (5624)Tumour 17
Atypical epithelial cells (544)
CAMLs (602)
Ciliated epithelial cells (174)
Cycling AT2 cells (838)
Cycling epithelial cells (228)
Immune cells (28478)
AT2 cells (1606)Tumour 23
Atypical epithelial cells (249)
CAMLs (843)
Ciliated epithelial cells (492)
Immune cells (86326)
Transitioning epithelial cells (255)
AT2 cells (4970)Tumour 24
Atypical epithelial cells (965)
CAMLs (618)
Ciliated epithelial cells (229)
Cycling AT2 cells (687)
Fibroblasts (129)
Immune cells (19386)
Chromosome / Position
Patient / Cell type in tumour dataset
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
2122
23
-1.0
-0.5
0.0
0.5
1.0
Chromosome / Position
Fraction of cells called
Tumour 17 - AT2 cells
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
2122
23
-1.0
-0.5
0.0
0.5
1.0
Chromosome / Position
Fraction of cells called
Tumour 17 - CAMLs
Immune cells
CAMLs
Atypical EC
AT2 cells
Ciliated EC
Cycling AT2
Cycling EC
0
5
- 3 036
Loss (x1000)
Gain (x1000)
Tumour 17
E F
C
D
I
Gain
Loss
HG
Response to
hypoxia
Oxidative
phosphorylation
Canonical glycolysis
Pyruvate metabolic process
TP53 regulates
metabolic genes
Cellular response
to hypoxia
TCA cycle and respiratory electron transport
Glycolysis
GO:BP REACTOME
23456
-log(adj.p)
AT2 cells - Tumour vs Background
0.0
4.0
3.0
2.0
1.0
1.5
0.5
2.5
3.5
0.00
0.25
0.50
0.75
1.00
1.75
1.50
1.25
0.00
0.25
0.50
0.75
1.00
1.75
1.50
1.25
0.0
2.5
2.0
1.5
1.0
0.5
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
AT2 cells CAMLs
Lympatic endothelial cells
Cycling mast cells
NK cells (lower cytotoxicity)
NK cells (higher cytotoxicity)
pDCs
Mast cells
Activated adventitial fibroblasts
Cycling T cells
Naive T cells
Cytotoxic T cells
Downregulated B cells
Exhausted cytotoxic T cells
Exhausted T cells
Cycling exhausted cytotoxic T cells
mo-DC2
cDC2
Alveolar MΦ
Anti-inflammatory MΦ
Cycling anti-inflammatory MΦ
Monocytes
STAB1+ MΦ
Immature myleoid cells
LYZ+ B cells
TNF+ B cells
B cells
Plasma B cells
Cycling plasma B cells
Cycling AT2 cells
Ciliated epithelial cells
Cycling epithelial cells
Atypical epithelial cells
Transitioning epithelial cells
Fibroblasts
Downregulated T cells
Tregs
CAMLs
AT2 cells
10
Downregulated T cells
Downregulated B cells
Activated adventitial fibroblasts
Cycling plasma B cells
pDCs
Cytotoxic T cells
NK cells (lower cytotoxicity)
B cells
TNF+ B cells
Exhausted T cells
LYZ+ B cells
Naive T cells
Exhausted cytotoxic T cells
Tregs
Mast cells
NK cells (higher cytotoxicity)
STAB1+ MΦ
Alveolar MΦ
Anti-inflammatory MΦ
Cycling epithelial cells
Cycling T cells
Cycling exhausted cytotoxic T cells
Atypical epithelial cells
Cycling AT2 cells
Cycling anti-inflammatory MΦ
AT2 cells
CAMLs
mo-DC2
Immature myeloid cells
cDC2
Cycling mast cells
Fibroblasts
Lymphatic endothelial cells
Plasma B cells
Monocytes
Ciliated epithalial cells
Transitioning epithelial cells
Fact_7
Fact_6
Fact_5
Fact_4
Fact_3
Fact_2
Fact_1
Fact_0
0.0
0.2
0.4
0.6
0.8
1.0
AT2 cells
Atypical ECs
Fibroblasts
Ciliated ECs
Transitioning ECs
Cycling ECs
Cycling
AT2 cells
FLE1
FLE1
Tumour areas Tumour areas (binned) QC
Pass
Fail
1.41.21.00.80.60.40.20.0
AT2 cells Cycling AT2 cells
1.00.0 0.2 0.4 0.6 0.8
Atypical epithelial cells
0.000.010.020.030.040.050.060.07
B
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 7

tumour cells, thus con ﬁrming the similarity of their CNA pro ﬁles
(Fig. 4F and Supplementary Fig. 5C). As CAMLs co-expressed a wide
array of myeloid genes as well as typical epithelial genes (Fig.1D–Fa n d
Supplementary Fig. 1D), had a low doublet score and shared the same
CNA signature as tumour cells, we hypothesised that these cells might
represent a subset of Mɸ tightly attached to a cancer cell. It is possible
that these Mɸ were undergoing phagocytosis or fusion.
CAMLs have been previously isolated from peripheral blood of
cancer patients and described to facilitate circulating tumour cells
seeding of distant metastases
16. Our analysis suggested that CAMLs can
also be isolated from tumour tissue. To validate that CAMLs are in
physical proximity to tumour cells in situ we examined our STx sec-
tions. We calculated across all sections (8 patients, n
sections=2 0 ) t h e
Pearson correlation between the relative abundance of the cell types
that reside in the same spot and are therefore co-localised. Our analysis
showed that CAMLs indeed co-localised with AT2 cells (Fig.4G, H). We
conﬁrmed this ﬁnding using non-negative matrix factorisation (NMF)
on the absolute cell-type abundances estimated by cell2location that
deﬁned factors of co-occurring cell states (Fig. 4I).
To determine the speci ﬁcM ɸ population from which CAMLs
likely originate, we employed PAGA to elucidate the differentiation
path of the myeloid cell population in our tumour dataset (Supple-
mentary Fig. 5D). The analysis revealed continuity of the differentia-
tion transitions between diverse populations of myeloid cells
43.W i t h i n
the PAGA trajectory, alveolar Mɸ (AMɸ)a n dA I Mɸ showed high PAGA
connectivity indicating their high transcriptional similarity. Both AIMɸ
and AMɸ showed the strongest connectivity on the PAGA trajectory
with STAB1 +M ɸ which, in turn, were linked with CAMLs. In line with
trajectory analysis, CAMLs co-expressed many of the genes speciﬁct o
STAB1 +M ɸ (Supplementary Fig. 2A), supporting the hypothesis that
CAMLs are likely derived from STAB1 +M ɸ following their close
interaction with tumour cells. Finally, DEA analysis between CAMLs
from LUSC versus LUAD patients, showed upregulation ofKRT17, KRT5
and KRT6A in LUSC samples (Supplementary Data 17). TheseKRT genes
were previously identiﬁed as markers of LUSC in multiple studies
44,45,
which supports hypothesis that CAMLs arise from the interaction
between Mɸ and tumour cell.
TAMs promote cholesterol and iron efﬂux in tumour
Mɸ, traditionally categorised into distinct M1 (classically activated)
and M2 (alternatively activated) phenotypes, are now understood to
exist along a dynamic spectrum of functional states
46. This concept of
Mɸ plasticity underscores their ability to seamlessly transition
between pro-inﬂammatory and anti-inﬂammatory roles in response to
intricate cues from their microenvironment (Supplementary Fig. 5D).
To better understand the transcriptional changes that different M ɸ
populations undergo in the TME, we performed DEA. In tumours, both
AMɸ and AIMɸ upregulated genes involved in cholesterol and lipid
transport and metabolism (such as ABCA1, APOC1, APOE, FABP3 and
FABP5) compared to the background tissue (Fig. 5A, B and Supple-
mentary Data 18 and 19). Cholesterol plays a vital role in tumour
growth due to the high demand of newly synthesised cellular mem-
branes during cancer cell proliferation. Hypoxia-related genes were
upregulated in AT2 cells in tumour compared to the background
(Fig. 4D), which can promote cholesterol auxotrophy in tumour cells
by suppressing cholesterol synthesis, thereby forcing them to rely on
exogenous cholesterol uptake
47. In our dataset, we detected higher
expression of the cholesterol exporter ABCA1 and no expression of
low-density lipoprotein receptor (LDLR)i nA M ɸ and AIMɸ,t h el a t t e r
gene being responsible for the uptake of cholesterol-carrying lipo-
protein particles into cells, suggesting preferential export of choles-
terol from TAMs to the TME (Fig. 5A). Interestingly, we also noted a
high expression ofTREM2 in both AMɸ and AIMɸ (Fig. 5A), which plays
a prominent role in ef ﬂux of cholesterol in microglia
48–50. To validate
the increased levels of cholesterol in the TME, we stained matched
tumour and background tissue sections with BODIPY™ 493/503, a stain
targeting cholesterol and other neutral lipids. We found a signi ﬁcant
increase in the BODIPY signal in the tumour sections, compared to
background tissue (Fig.5C, D), conﬁrming an increased availability of
neutral lipids in the tumour, possibly as a result of an increased export
by TAMs.
STAB1 +M ɸ were identiﬁed in the tumour resections (Fig. 5E–H,
Supplementary Fig. 2 and Supplementary Notes), so we used DEA to
identify a set of genes that were speciﬁcf o rSTAB1 +M ɸ compared to
tumour AIMɸ or AMɸ.W ei d e n t iﬁed 20 genes, from here on referred to
as “STAB1 signature genes” (Fig. 5I). Interestingly,STAB1 +M ɸ uniquely
expressedSLC40A1, which encodes for the ferroportin, the only known
protein that exports ferrous iron from the cytoplasm across the plasma
membrane and is key for the iron-releasing activity of macrophages
(Fig. 5I, J and Supplementary Data 20 and 21)
51. Ferroportin-mediated
release of free iron by M2 M ɸ was reported to promote the pro-
liferation of renal carcinoma cells in vitro, possibly by supporting the
high iron requirement due to increased DNA synthesis
52.F u r t h e r m o r e ,
compared to AMɸ, STAB1 +M ɸ expressed lower levels of ferritin heavy
chain 1 (FTH1) and ferritin light chain (FTL) encoding for the iron storer
ferritin (Fig. 5J and Supplementary Data 20). Consistent with the
hypothesis of their sustained export of free iron to the extracellular
milieu, STAB1 + Mɸ downregulated genes involved in iron sequestra-
tion (Fig. 5K). Taken together, our analysis suggests that macrophages
undergo “reprogramming” within the TME and adopt a transcriptional
signature that facilitates cholesterol efﬂux and iron export, thus sup-
porting tumour progression.
STAB1 + Mɸ in tumour tissue undergo oncofoetal
reprogramming
Embryonic development shares many characteristics with tumour
tissue, including rapid cell division, cellular ﬂexibility, and a highly
vascular microenvironment. It has been recently reported that during
tumorigenesis, M ɸ can undergo oncofoetal reprogramming 53 and
acquire a foetal-like transcriptional identity that supports tumour
growth and metastasis
53. Considering that some of the STAB1 signature
genes are typically expressed by foetal M ɸ (such as STAB1, FOLR2,
Fig. 4 | CAMLs share tumour CNAs and colocalise with tumour cells. A CNA
analysis. The plot shows chromosomal gains (red lines) and losses (blue lines)
estimated by CopyKat in each chromosome arm for different cell types and patients
in the tumour dataset. All immune cell types were grouped together for plotting
purposes.B PAGA graph overlaid on the diffusion maps (force-directed layout— FLE
embedding) computed for non-immune cell types in tumour.C First three panels—
Representative blind annotations from a qualiﬁed pathologist, indicating the areas
of tumour inﬁltration (left), binning of the tumour area on the Visium spots (centre)
and the spots that passed QC (right). The last three panels— cell2location estimation
for AT2 cells (left), Cycling AT2 cells (centre) and Atypical epithelial cells (right) on
the same sections, overlaid with the pathologist’s annotation for the tumour inﬁl-
tration (green contour).D Overrepresentation analysis on gene ontology— biolo-
gical processes (GO:BP) and REACTOME database by clusterProﬁler R package,
using DEGs upregulated by AT2 cells in tumour vs background. Source data is
provided as a Source Dataﬁle. E Detailed overview of CNAs in AT2 and CAMLs from
the tumour of one representative patient. Bars indicate the frequency of cells
harbouring chromosomal gains (red bar) or losses (blue bars) in speciﬁcc h r o m o -
somal regions. F Scatterplot of the KL divergence for losses (x axis) and gains (y
axis) between each cell type in the tumour dataset calculated using their gain and
loss distribution. All immune cell types were grouped together for plotting pur-
poses. G Spatial images depicting the cell abundance estimated by cell2location for
AT2 cells and CAMLs on three representative tumour sections.H Hierarchical
clustering of the correlation distance calculated on cell-type composition (as esti-
mated by cell2location) across spots that passed QC in all tumour sections.I Non-
negative matrix factorisation built on the q05 estimation of cell-type abundance
across spots that passed QC (as estimated by cell2location) in all tumour sections.
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 8

SLC40A1, MERTK, GPR34 and F13A1)54, we wanted to explore if further
transcriptional commonalities exist between tumour-originating
STAB1 +M ɸ and M ɸ isolated from human foetal lung. To this end,
we combined tumour- and background-originating myeloid cells from
our dataset (n = 347,364 cells) with myeloid and progenitor cells from a
publicly available foetal lung scRNA-seq dataset
55 (n =6 , 9 4 7 c e l l s )
using Harmony. Next, we performed Leiden clustering on the neigh-
bourhood graph and examined how cell types are distributed within
the clusters (Supplementary Fig. 6A, B). To examine similarity in their
gene expression proﬁle, we applied hierarchical clustering and built a
-2.5 2.5 0.0 5.0
log2(fold-change)
0
5
10
15-Log10(padj)
AMΦ (tumour vs. background)
APOE
SPP1
TREM2
APOC1
ABCA1
A DC
0.0246
0
25
50
75
100
Background Tumour
BODIPY area [px] x1000
50μm Background
DAPI
AMΦ
AIMΦ
CAMLs
Cycling AIMΦ
Monocytes
STAB1+ MΦ
BODIPY 493/503CD68
E
J
-2.5 2.5 0.0 5.0
log2(fold-change)
0
20
40-Log10(padj)
PPARG
MCEMPSLC40A1
F13A1
FTL
SELENOP
FOLR2
FTH1
AMΦ vs STAB1+ MΦI K
Acute
inflammatory
response
Response to 
iron ion
Sequestering
of metal ion
Defense
response
to bacterium
AIM vs 
STAB1+ MΦ
AMΦ vs 
STAB1+ MΦ
5
0
5
10
AIMΦ & AMΦSTAB1+ MΦ
Log10(padj)
Acute
inflammatory
response
Sequestering
of metal ion
Granulocyte
activation
Granulocyte
activation
Fraction of cells in group (%)
10 30 50 70
Mean expression in group
ADAM28
USP53
ADORA3
C3
ENPP2
EPB41L2
F13A1
FCGBP
FOLR2
GPR34
IL2RA
MERTK
OLFML2B
OLFML3
PLD4
SDC3
SELENOP
SLC40A1
ST6GAL1
STAB1
Lipid transport
Cholesterol efflux
Fatty acid
biosynthetic
process
Regulation of 
endocytosis
Phagocytosis
Cholesterol
efflux
Regulation of
endocytosis
Negative regulation
of immune
system process
Phagocytosis
AIMΦAMΦ
2
3
4
Log10(padj)
Tumour vs BackgroundB
0.5 1
20μm
STAB1CD68DAPI
F
STAB1CD68DAPI STAB1CD68DAPI PanCK
GH
20μmTumour Background 20μm
50μmTumour
DAPI BODIPY 493/503CD68
Tum
ou
r
Backgr
ound
0
10
20
30
40
50
% of STAB1+ cells in CD68+ population
0
5
10
15
20
25
Tumour
% of STAB1+ cells in CD68+ population
Fig. 5 | Tumour macrophages undergo oncofoetal reprogramming. AVolcano
plot of DEGs (red) for AIMɸ in tumour vs background, extracted using the py_DE-
Seq2 package. B Overrepresentation analysis on gene ontology— biological pro-
cesses database by clusterProﬁler R package, using the DEGs upregulated by
Alveolar Mɸ and AIMɸ in tumour vs background. Source data is provided as a
Source Data ﬁle. C IHC for CD68 and neutral lipids (BODIPY 493/503) on tumour
and background tissue sections. Maximum intensity projection of Z-stacks. Scale
bar 50 µm. D Area covered by the BODIPY signal in tumour and background section.
The difference in BODIPY area coverage was determined with a paired, two-sided t
test, matching tumour and background sections from the same patients.N =5
patients. Source data is provided as a Source Dataﬁle. E IHC for CD68 and STAB1 on
tumour (left) and background (right) tissue sections. Maximum intensity projection
of Z-stacks. Inlets show a detailed magniﬁcation on a single cell. Scale bar 20 µm.
F Quantiﬁcation of STAB1+ cells within the CD68+ macrophage population. The
fraction of the STAB1 + CD68+ area is shown as a percentage of the total CD68+
area. Data are presented as mean value and standard deviation (n = 3 biological
replicates). Source data is provided as a Source Data ﬁle. G Staining for CD68,
STAB1 and PanCK on tumour tissue sections. Maximum intensity projection of
Z-stacks. Inlets show a detailed magniﬁcation on a single cell. Scale bar 20 µm.
H Quantiﬁcation of STAB1 + CD68+ cells within the CD68+ macrophage population
in NSCLC. Data are presented as mean value and individual data points (n =2b i o -
logical replicates). Source data is provided as a Source Dataﬁle. I Dotplot showing
the expression of the “STAB1 signature genes” across all macrophage subsets and
CAMLs in tumour.J Volcano plot of DEGs identiﬁed by py_DESeq2 (red) for Alveolar
Mɸ vs STAB1 Mɸ in tumour. K Overrepresentation analysis on gene ontology—
biological processes database by clusterProﬁler R package, using the DEGs from
Alveolar Mɸ vs STAB1 Mɸ (top) and AIMɸ vs STAB1 M
ɸ (bottom) in tumour (left—
upregulated by STAB1 Mɸ;r i g h t— upregulated by Alveolar Mɸ or AIMɸ). Source
data is provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 9

dendrogram by estimating the correlation distance between cell types
on the harmonised PC embedding space, under the complete linkage
criterion of hierarchical clustering (Fig.6A).
We observed that tumour cDC2 exhibited the strongest corre-
lation with background cDC2, whereas tumour mo-DC2 displayed
the highest correlation with foetal DC2 and, in a broader context,
with background mo-DC2. The population of pDC from tumour,
background and foetal lung were closely correlated. Similarly,
tumour monocytes were correlated with foetal classical monocytes
and background monocytes. In contrast, macrophage populations in
tumour, and in particular STAB1 +M ɸ, were correlated with foetal
macrophages. STAB1 +M ɸ clustered predominantly with foetal
SPP1 +M ɸ (Fig. 6A), which accounted for over 80% of all foetal
lung macrophages reported in ref. 55. Consistent with this
ﬁnding, SPP1 +M ɸ had a high expression of the “STAB1 signature
genes” compared to other haematopoietic populations (Fig. 6B, C).
Our analysis substantiates the idea that monocytes within the
tumour environment, as they undergo differentiation into anti-
inﬂammatory macrophages, acquire a transcriptional signature akin
to that of foetal macrophages. This distinctive transcriptional sig-
nature was not observed in the macrophages from surrounding
normal tissue.
BA
E
-0.5
0.0
0.5
1.0
APOE+ MΦ1APOE+ MΦ2
Basophil
CMP
CX3CR1+ MΦ CXCL9+ MΦ Cycling DC
DC1DC2 DC3
Eosinophil
GMP HSC
HSC/ELP
MEP
MegakaryocyteMyelocyte−like
Neutrophil
Non−cla. mono.
Platelet
Promonocyte−likePromyelocyte−like
S100A12−hi cla. mono.S100A12−lo cla. mono.
SPP1+ M
Φ
aDC 1aDC 2pDC
pre−pDC/DC5
C
ADAM28ADORA3
C3
ENPP2EPB41L2
F13A1FCGBPFOLR2GPR34IL2RAMERTKOLFML2BOLFML3
PLD4SDC3
SELENOPSLC40A1ST6GAL1
STAB1USP53
APOE+ MΦ1
APOE+ MΦ2
CX3CR1+ MΦ
CXCL9+ MΦ
SPP1+ MΦ
01234
FTL MΦ - 17
MΦ - 7
IL4I1 MΦ - 6
HES1 MΦ - 2
TREM2 MΦ - 3
C1Q MΦ - 16
MΦ - 11
MΦ - 13
ADAM28ADORA3
C3
ENPP2EPB41L2
F13A1FCGBPFOLR2GPR34IL2RAMERTKOLFML2BOLFML3
PLD4SDC3
SELENOPSLC40A1ST6GAL1
STAB1USP53
Percent Expressed
02 55 07 51 0 0
Average Expression
D
HES1 M
Φ - 
2
FTL MΦ - 17
MΦ - 7MΦ - 
11
MΦ - 13
C1Q MΦ
 - 16
TREM2 MΦ - 
3
Proliferating cells - 10
DC2/DC3 - 14IL4I1 MΦ - 6
T cell doublets - 9
ISG Mono - 4
CD16- Mono - 8CD16- Mono - 12CD16+ Mono - 5CD16+ Mono - 1IL1B Mono - 15
-0.5
0.0
0.5
1.0
STAB1 gene signature score STAB1 gene signature score
0.0 0.5 1.0 1.5
0.0
0.3
0.6
0.9
APOE+ MΦ2APOE+ MΦ1
Neutrophil
S100A12−hi cla. mono.
Basophil
Non−cla. mono.Myelocyte−like
SPP1+ MΦ
DC3
Promonocyte−like
Megakaryocyte
Eosinophil
MEP
Promyelocyte−like
aDC 2
S100A12−lo cla. mono.
CXCL9+ MΦCX3CR1+ MΦ
GMPCMPHSCDC2
Cycling DC
aDC 1
HSC/ELP
DC1
pre−pDC/DC5
Platelet
pDC
AMΦ gene signature score
0.0
0.5
1.0
C1Q MΦ - 16TREM2 MΦ - 3
MΦ - 11MΦ - 13
FTL MΦ - 17HES1 MΦ - 2
Prolif
era
ting
 cells - 
10
MΦ - 
7
IL4I1 
MΦ - 
6
ISG Mono
 - 4
Tcell doubl
ets - 9
CD16− M
ono - 12
IL1B Mono
 15
CD16+ Mono - 
5
CD16− Mo
no - 8
DC2/DC3 - 14CD16
+ Mono - 1
AMΦ gene signature score
1.5
FG
I
H
FTL MΦ - 17
MΦ - 7
IL4I1 MΦ - 6
HES1 MΦ - 2
TREM2 MΦ - 3
C1Q MΦ - 16
MΦ - 11
MΦ - 13
AC026369.3
ACO1ACOT7ACP5
AKR1C3ALDH1A1AMIGO2APOC1APOEAQP3
ARRDC4CCL18CD52CD9CES1
COLEC12
CSTBCTSD
CYP27A1
FABP3FABP4FABP5FAM89A
FDX1FN1FTL
GCHFRGLDNGPNMBHPGDHSD3B7IGFBP2LGALS3
LIPALPL
LTA4HMARCOMCEMP1MGST1MLPHMMENCEH1NUPR1
PCOLCE2PDLIM1PHLDA3PPARG
PPICRBP4RMDN3S100A13SCCPDH
SCDSNTB1
UBASH3B
VAT1VSIG4
Percent Expressed 0
24 6
25 50 75 100 Average Expression
APOE+ MΦ1
APOE+ MΦ2
CX3CR1+ MΦ
CXCL9+ MΦ
SPP1+ MΦ
AC026369.3
ACO1
ACOT7ACP5
AKR1C3ALDH1A1AMIGO2APOC1APOEAQP3
ARRDC4CCL18CD52CD9CES1
COLEC12
CSTBCTSD
CYP27A1
FABP3FABP4FABP5
FAM89AFDX1FN1FTL
GCHFRGPNMBHPGDHSD3B7IGFBP2LGALS3
LIP ALPLLTA4H
MARCOMCEMP1MGST1MMENCEH1NUPR1
PCOLCE2PDLIM1PHLD
A3
PP ARGPPICRBP4RMDN3S100A13SCCPDH
SCDSNTB1
UBASH3B
VAT1VSIG4
Percent Expressed 02 55 07 5 1 0 0
0246
Average Expression
0.5 1 21.5
Percent Expressed
02 55 07 51 0 0
Average Expression
Human foetal lung atlas Human foetal lung atlas
MoMac-VERSE
MoMac-VERSE
MoMac-VERSE Human foetal lung atlas
tumour - cDC2
tumour - pDCs
background - pDCs
foetal - DC2
foetal - Cycling DC
foetal - DC1
foetal - aDC2
background - cDC2
background - mo-DC2
foetal - aDC1
foetal - Neutrophils
background - Monocytes
foetal - Basophils
foetal - Eosinophils
foetal - Myelocyte-like
foetal - Promyelocyte-like
foetal - Promonocyte-like
foetal - HSC/ELP
foetal - HSC
foetal - MEP
foetal - CMP
foetal - GMP
foetal - S100A12-lo cla. mono.
foetal - CXCL9+ MΦ
foetal - SPP1+ MΦ
foetal - CX3CR1+ MΦ
foetal - APOE+ MΦ2
foetal - APOE+ MΦ1
foetal - Platelet
foetal - Megakaryocyte
foetal - pDC
foetal - pre-pDC/DC5
tumour - Cycling AIMΦ
background - Cycling AMΦ
background - Cycling cDC2
background - Cycling mo-DC2
tumour - STAB1+ AIMΦ
tumour - AIMΦ
tumour - AMΦ
tumour - mo-DC2
tumour - Immature myeloid
background - Immature myeloid
background - AMΦ
background - AIMΦ
foetal - S100A12-hi cla. mono.
tumour - Monocytes
foetal - DC3
foetal - Non-cla. mono.
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 10

To further examine the prevalence of STAB1 +M ɸ in other
pathologies, including other cancers, we examined the expression of
“STAB1 signature genes”across a diverse group of myeloid cells using a
published atlas of human monocytes and M ɸ collected from 12 dif-
ferent healthy and pathologic tissues (n = 140,327 cells), called MoMac-
VERSE56.T h ec l u s t e ro f“HES1+ macrophages” identiﬁed in MoMac-
VERSE showed the highest expression of the “STAB1 signature genes”
(Fig.6D, E). Similar toSTAB1 +M ɸ, HES1+ macrophages accumulated in
tumours of lung cancer patients but also liver cancer patients 57 and
were suggested to represent a cluster of “long-term resident-like” Mɸ
with foetal-like transcriptional signature56.I nc o n t r a s t ,“C1Q” Mɸ from
MoMac-VERSE, which have been described as lung alveolar Mɸ, had a
high expression of genes unique to our tumour alveolar AM ɸ (from
here on referred as“AMɸ signature genes”,F i g .6F, H). In the context of
foetal lung, a rare population of APOE + Mɸ, which accounted for less
than 1% of all foetal lung macrophages reported in ref. 55,h a dah i g h
AMɸ signature genes score (Supplementary Notes and Fig. 6G, I, see
“Methods”).
Taken together, our analysis suggests that tumour macrophages,
especially STAB1 +M ɸ, exhibited a transcriptional signature reminis-
cent of Mɸ during foetal lung development, suggesting that they have
undergone oncofoetal reprogr amming within the NSCLC tumour
environment.
Discussion
Our study represents a large single-cell multiomics analysis of samples
collected from treatment-naive patients with NSCLC. We integrated
scRNA-seq data from nearly 900,000 cells from tumour resections and
adjacent non-malignant tissue from 25 treatment- naive patients with
spatial transcriptomics to build an atlas of immune and non-immune
compartments in lung cancer.
LUAD and LUSC, the two most common NSCLC subtypes, exhibit
markedly different prognostic outcomes and have shown potential for
subtype-speciﬁct h e r a p i e s
28. Despite similar cell-type composition, we
observed signiﬁcant differences in the co-expression of several ICIs
and inhibitory molecules between LUAD and LUSC, highlighting ther-
apeutic opportunities. LUAD samples frequently expressedTIGIT and
TIM3 (HAVCR2), while in LUSC we found the putative ICICD96-NECTIN1.
While different advanced clinical trials targeting TIGIT, including in
patients affected by NSCLC, are ongoing
58, progress on TIM3 and CD96
is more limited 59.A ﬁrst-in-human phase-I study evaluating the anti-
CD96 monoclonal antibody GSK6097608 as monotherapy alone or in
combination with anti-PD1 (dostarlimab) started recruiting patients
only recently
60. Taken together, our datasuggest that LUAD and LUSC
patients might beneﬁt from speciﬁc immunotherapy targeting ICIs as
TIM3, TIGIT and CD96.
The TME plays a crucial role in modulating the population and
behaviour of M ɸ4. We found that, compared to the adjacent non-
tumour tissue, tumour resections harboured a lower proportion of
monocytes but a higher proportion of monocyte-derived cells, such as
mo-DC2s and anti-in ﬂammatory M ɸ, suggestive of an enhanced
monocyte differentiation in the TME
7,9. The prevalence of anti-
inﬂammatory M ɸ,i n c l u d i n gSTAB1 +M ɸ, exhibited an inverse rela-
tionship with the abundance of natural killer (NK) cells and T cells in
the tumour environment; and the NK cells within the tumour exhibited
reduced cytotoxic activity. Our results are in line with the recent
ﬁndings that the removal of tumour cell debris by lung M ɸ leads to
their conversion into an immunosuppressive phenotype, conse-
quently hindering the inﬁltration of NK cells into the TME
27.M ɸ with
elevated levels of tumoural debris were reported to upregulate genes
involved in cholesterol trafﬁcking and lipid metabolism, a character-
istic shared with anti-inﬂammatory Mɸ in our dataset. As a result, they
downregulated co-stimulatory molecules, cytokines and chemokines
27
essential for the recruitment of CD8 + T cells, therefore becoming
more immunosuppressive.
Among the M ɸ population within tumours, we also identi ﬁed
STAB1 +M ɸ that exhibited the highest level of immunosuppression
markers. These STAB1 +M ɸ displayed a gene expression pattern akin
to that of foetal lung M ɸ a n dd e m o n s t r a t e dam o d iﬁed iron metabo-
lism, marked by the increased expression of genes associated with iron
release in the TME. Therefore, we hypothesise thatSTAB1 +M ɸ might
play a crucial role in supporting tumour progression by sustaining the
increased iron requirement of highly-cycling tumour cells
52,61.I na
subcutaneous LLC1 Lewis lung adenocarcinoma model, mice lacking
Stab1 expression in Mɸ, tumour growth was diminished. This outcome
was attributed to a shift towards a pro-in ﬂammatory phenotype in
TAM and a robust in ﬁltration of CD8 + T cells within the TME 62.
STAB1 +M ɸ displayed a transcriptional resemblance to CAMLs, which
concurrently expressed genes associated with both Mɸ and epithelial
cells, and exhibited copy number alterations (CNAs) similar to those
found in tumour cells. STAB1+ plays a pivotal role in facilitating the
adhesion and engulfment of apoptotic cells by engaging in a speci ﬁc
interaction with phosphatidylserine, supporting the hypothesis of a
strong interaction of a Mɸ with a tumour cell in CAMLs
63.I np r e v i o u s
studies, CAMLs were identi ﬁed by immuno ﬂuorescence in the per-
ipheral blood of individuals affected by various solid tumours and
were proposed to facilitate the dissemination and establishment of
circulating tumour cells in distant metastatic sites
16. Here, we report
their presence in multiple tumour resections, based on a combination
of a compound gene expression signature, tumour-speci ﬁcc o p y
number alterations and physical proximity to tumour cells, as evident
from Visium sections. Taken together, our comprehensive
dataset allowed identifying a multitude of molecular changes in the
Mɸ population of the lung tumour microenvironment, which will help
pave the way for the development of therapeutic strategies
against NSCLC.
Methods
Ethics and tissue acquisition
Tissue used in the research study was obtained from the Papworth
Hospital Research Tissue Bank. Written consent was obtained for all
tissue samples using Papworth Hospital Research Tissue Bank’se t h i c a l
Fig. 6 | STAB1 +M ɸ undergo oncofoetal reprogramming. AHierarchical clus-
tering of the correlation distance calculated on each cell in the harmonised (tumour
myeloid + background myeloid + foetal lung myeloid) PC space. B Violin plot
showing the expression level of the“STAB1 gene signature” across myeloid cell and
progenitor populations identiﬁed in a publicly available human foetal lung atlas.
C Dotplot of the expression of each gene in the“STAB1 gene signature” in selected
foetal lung macrophage populations. The size of each dot represents the percen-
tage of cells in the cluster expressing the gene, while the colour represents the
mean expression of each gene in each cluster.D Violin plot showing the expression
level of the “STAB1 gene signature” across the clusters identiﬁed in the publicly
available MoMac-VERSE dataset.E Dotplot of the expression of each gene in the
“STAB1 gene signature” in selected macrophage populations from the MoMac-
VERSE. The size of each dot represents the percentage of cells in the cluster
expressing the gene, while the colour represents the mean expression of each gene
in each cluster. F Violin plot showing the expression level of the “AMɸ gene sig-
nature” across myeloid cell and progenitor populations identiﬁed in the publicly
available“MoMac-VERSE” dataset.G Violin plot showing the expression level of the
“AMɸ gene signature” across myeloid cell and progenitor populations identiﬁed in
a publicly available human foetal lung atlas. H Dotplot of the expression of each
gene in the “AMɸ gene signature” in selected macrophages populations identiﬁed
in the “MoMac-VERSE” dataset. The size of each dot represents the percentage of
cells in the cluster expressing the gene, while the colour represents the mean
expression of each gene in each cluster.I Dotplot of the expression of each gene in
the “AMɸ gene signature” in selected foetal lung macrophage populations. The size
of each dot represents the percentage of cells in the cluster expressing the gene,
while the colour represents the mean expression of each gene in each cluster.
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 11

approval (East of England— Cambridge East Research Ethics Commit-
tee). Human tumour and adjacent background tissues, collected from
the edges of the lungs, were obtained from 25 patients following
tumour resection. Human healthy lung samples were obtained from
two healthy deceased donors. Both healthy samples were evaluated by
an expert pathologist to exclude the presence of malignancies. The
human material was provided by the Royal Papworth Tissue Bank
(T02229), in accordance with the HMDMC Human Tissue Act Sample
Custodian Form Version 7.0 (UK NRES REC approval reference num-
ber(s): 08/H0304/56 + 5; HMDMC 16 | 094). NSCLC FFPE tumour
blocks (n = 2) used for validation of STAB1+ macrophages with Akoya
were obtained from 2 different donors and purchased from BioIVT (ex-
Asterand Bioscience). Informed Consent Form (ICF) and Institutional
Review Board Approval Letter (IRBA) were obtained for all tissue
samples.
Sex was assigned (15 male and 12 female patients/donors). Sex-
based analyses were not performed due to the limited sample size.
Gender was not determined.
Tissue processing
Tissues were kept in cold complete RPMI medium (RPMI [Invitrogen]
supplemented with 10% FBS [Sigma Millipore, catalogue number:
F9665], 2 mM L-Glutamine [Life Technologies, catalogue number:
25030-024] and 100 U/ml Penicillin-Streptomycin [Thermoﬁsher, cat-
alogue number: 15140122]) until dissociation, which was performed on
the same day of collection. Single-cell suspensions were generated as
follows: tissues were placed into a petri dish and cut into small pieces
of 2–4 mm and transferred into a 1.5-ml tube containing the digestion
mix (complete RPMI media supplemented with 1 mg ml
−1 collagenase
IV and 0.1 mg ml−1 DNase I) and minced using surgical scissors. Minced
tissues were incubated for 45 min at 37 °C and vortexed every 15 min.
Digested tissues were passed through a 100-μms t r a i n e ri n t oaf a l c o n
tube preﬁl l e dw i t hc o l dP B S .
Cells were then centrifuged for 5 min at 300 × g,4 ° Ca n dt h e
pellet was resuspended into 1× RBC lysis buffer (eBioscience) for 2 min
at room temperature, after which 20 ml of cold PBS were added to stop
the lysis reaction. Cells were cryopreserved in 5% DMSO in KnockOut
Serum Replacement (KOSR; Gibco
TM, catalogue number: 10828010)
until further use.
FACS sorting
On the day of FACS sorting, cells were rapidly thawed at 37 °C and
transferred to complete RPMI media. Live-cell enrichment was per-
formed using MACS Dead Cell Removal Kit (Miltenyi Biotec) following
the manufacturer’s instructions. Red blood cells were further depleted
by negative selection using CD235a Microbeads (Miltenyi Biotec) and
MACS LS columns (Miltenyi Biotec), following the manufacturer ’s
instructions.
For FACS sorting, cells were stained with Zombie Aqua to exclude
dead cells and the cocktail of antibodies for 30 min at 4 °C. Cells were
centrifuged for 5 min at 300 ×g, 4 °C, resuspended in 500μlo f5 %F B S
in PBS and subsequently ﬁltered into polypropylene FACS tubes.
Immune cells were sorted as live, CD45 + ; MDSC were sorted as
l i v e ,C D 4 5 + ,L i n e a g e -( L i n :C D 3 ,C D 5 6 ,C D 1 9 ) ,C D 3 3 + ,H L A - D R - / l o w
(Supplementary Data 22 and Supplementary Fig. 1A). Cells were sorted
into a 1.5-ml tube, counted and submitted for 10x scRNA-seq library
preparation.
scRNA sequencing
Each cell suspension was submitted for 3’single-cell RNA sequencing
using Single Cell G Chip Kit, chemistry v3.1 (10x Genomics Pleasanton,
CA, USA), following the manufacturer ’s instructions. Libraries
were sequenced on an Illumina NovaSeq 6000, and mapped to the
GRCh38 human reference genome using the CellRanger toolkit (ver-
sion 3.1.0).
scRNA sequencing data analysis
Integrating numerous samples, notably from diverse cancer subtypes
and adjacent normal tissues, is challenging due to variations in gene
programmes between samples. Consequently, these differences often
hinder a coherent biological alignment when attempting simultaneous
embedding. Most current integration techniques, primarily focused on
batch correction, operate under the assumption of shared cell states
across samples. However, while they aim to mitigate technical dis-
parities, they might inadvertently erase genuine biological distinc-
tions. Therefore, we applied the QCﬁltration and doublet removal on
the merged dataset (Tumour + B/H) but we split the datasets between
tumour and B/H for HVG selection, PCA, batch correction (using Har-
mony), clustering and annotations.
Starting from the unnormalised, uncorrected gene expression
matrices produced (per sample) by the CellRanger protocol, we per-
formed careful downstream analysis of the scRNA-seq data. For each
CellRanger output (corresponding to a speciﬁc technical and biologi-
cal replicate of the separate tumour, background and healthy data) we
identiﬁed low-quality cells or empty droplets by applying the barco-
deRanks and emptyDropsfunctions using the R packageDropletUtils
64.
Following per-sample droplets removal, the complete set of cell
expression matrices was merged (we merged tumour, background,
and healthy samples), and quality control (QC) was applied to the
resultant merged matrix. The remaining analysis is implemented using
standard approaches in the Scanpy
65 framework. The QC is based on
three parameters: the total UMI count (lower-upper threshold [400,
100,000]), the number of detected genes (lower-upper threshold [180,
6000]), and the proportion of mitochondrial gene count per cell (20%
fraction upper bound). We applied Scrublet
66 to remove potential
doublets with 0.06 as the expected doublet rate and then ﬁltered the
results using the parameter values (2 for minimum read count of cell, 3
for minimum detected cell of gene, 85 for minimum gene variability
percentage, and 30 for the number of principal components used to
embed the transcriptomes prior to k-nearest-neighbour graph con-
struction). The resulting merged andﬁltered expression matrix is then
normalised using the scaling factor 10,000, followed by log1p
transformation.
For dimensionality reduction, we ﬁrst selected sets of highly-
variable genes (HVGs) from the initial gene set of 25,718. Starting from
the HVG selection, the merged matrix was split into two separate
matrices: tumour, and combined background/healthy which we refer
to as B/H. After HVG selection, 1604 genes were selected from the
tumour matrix and 1486 from B/H. From these separate HVG sets, we
applied dimensionality reduction using Principal Component Analysis
(PCA). Next, we performed PCA separately for tumour and for B/H and
retained the top 15 components, according to the Scree plot elbow
rule. The resulting matrix is then batch corrected to account for
additional technical variations arising between samples which are non-
biological in origin. We apply batch correction by usingharmonypy (a
Python version of the original harmonyR
67 package), based on
recommended benchmarking68 against other procedures.
Following between-sample batch correction, we computed a
neighbourhood graph a nd applied Leiden 69 clustering (with Leiden
resolution being 1) to the 15-dimensionalharmonisedPCA space69.F o r
visualisation purposes, we used Uniform Manifold Approximation and
Projection (UMAP) manifold embedding
70 to capture the global fea-
tures of the 15-dimensional clustered manifold and represent the glo-
bal structure in two and three dimensions. We identi ﬁed top 100
representative genes for each cluster by performing the Wilcoxon
signed-rank test
71 with the Bonferroni correction, followed by a ﬁlter-
ing to obtain genes overexpressed in the target group (minimum log
fold change as 0) and expressed in at least 30% of cells within the
group. We did not control the fraction of gene expression of other
clusters, by setting the maximum threshold as 100%. We then anno-
tated each cell cluster according to the the expression proﬁle of these
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 12

marker genes and the expression of other canonical genes signiﬁcant
for different lung cell types based on the literature (see extended
results). The annotation procedure was done iteratively. With this
approach we generated two separate annotated UMAPs, together with
associated marker genes, for the tumour and B/H datasets.
Contrasting cell-type abundances between different samples
To compare cell-type abundances, we calculated the proportion of
each cell type within each patient and broad cell annotation in the
unenriched (CD235-) samples. We contrasted cell-type proportions
between groups (tumour vs. background or LUAD vs. LUSC) using a
Wilcoxon rank-sum test. Finally, we corrected for multiple testing
using a two-sided Bonferroni correction independently for each group
analysed.
The association between the relative cell-type abundance for each
immune cell type was evaluated on the Pearson ’s product-moment
correlation coefﬁcients.
Label transfer
To test consistency in cell-type annotation performed separately in
tumour and B/H, we performed reference-query mapping from
tumour to B/H using scArches
22. For the 828,191 immune cells (464,952
in tumour and 363,239 in B/H) identi ﬁed through our separate anno-
tations, we selected a common set of 10,000 HVGs. We ﬁrst built an
scVI model and trained it on the tumour dataset using broad cell types
for reference, and applied scHPL method (provided in the scArches
package, parameters set to use KNN classi ﬁer, 100 neighbours and
with PCA dimensionality reduction) to obtain the hierarchy for the
tumour cell types. We then applied the B/H dataset to the pretrained
reference model for a query, and predicted B/H broad cell types based
on tumour hierarchy (probability threshold set as 0.2). Finally, we
compared the predicted cell types with our separate annotations in B/
H using a heatmap to visualise the confusion matrix.
CellPhoneDB
We initially identiﬁed a putative long list of cell –cell interactions dif-
ferentially observed in the tumour environment by inferring statisti-
cally signiﬁcant ligand–receptor pairs, and their corresponding cell
types, using CellPhoneDB29.W et r e a t e dt h et u m o u r( L U A Do rL U S C ) ,
background, and healthy scRNA-seq proﬁles as independent datasets
and ran CellPhoneDB separately. To reduce the impact of randomness
in the way CellPhoneDB samples from input datasets, we required that
any ligand–receptor pair of interest from the CellPhoneDB database be
expressed in at least 30% of cells in a particular cell-type cluster of
interest. The ﬁnal ligand –receptor lists were further ﬁltered by
requiring that the mean log(1 + expression) of the ligand–receptor pair
be greater than 1.0, and the Bonferroni-adjusted
72 P value be less than
0.01. From these ﬁltered long lists, ligand –receptor pairs and corre-
sponding cell types relevant to the tumour data are identiﬁed.
When evaluating the ligand –receptor lists calculated with Cell-
PhoneDB, we did not run on the complete datasets due to the difﬁculty
in scaling up the CellPhoneDB statistical permutation tests to scRNA-
seq with more than 10
6 cells. Instead, we separately strati ﬁed the
tumour, healthy and background datasets such that the proportion of
cell types, patients, and samples in the reduced 50% of the data reca-
pitulated the proportions in the full dataset.
Differential expression analysis
Differentiation expression analysis (DEA) was performed for AT2 cells,
anti-inﬂammatory macrophages and alveolar macrophages using a
pseudo-bulk approach to compare tumour versus background. Pseu-
dobulks were built for each patient by summing raw gene counts
across all cells in each cell type investigated. The patients 1 and 4 were
not included in the analysis as their cancer subtype and stage were not
known at the time of analysis. Since there were differences in the cell
count between datasets we downsampled the biggest cluster to the
size of the smaller. The downsampling routine was repeated 100 times,
such that 100 new datasets were created that match the smaller
dataset. DEA was performed using sample-level pseudobulks and a
Pythonic version of the DESeq2 pipeline (py_DESeq2), including the
patient information as co-variate
73. The median adjusted p value by
Benjamini–Hochberg procedure and median log2FC for each differ-
entially expressed gene (DEG) was calculated across 100 iterations. We
veriﬁed the robustness of this choice of 100 iterations by visualising
the variability of the medianp value across iterations, in order to assess
its stability (Supplementary Fig. 6C). DEGs were ﬁltered with med-
ian(padj)≤0.05 and |median(logFC)| ≥1. Prior to performing over-
representation analysis, the genes that were commonly upregulated in
more than 50% of the contrasts were removed (DNAJB1, HSPA1A,
HSPA1B, HSPB1, HSPE1, IGHA1, IGKC, IGLC2). DEGs were used to per-
form gene ontology (GO) overrepresentation using the clusterProﬁler
package
74.T od e ﬁne STAB1 +M ɸ and AMɸ gene signatures, we com-
pared DEA results and intersected the genes signiﬁcantly upregulated
by STAB1 +M ɸ (or AM ɸ) compared to the other M ɸ populations in
tumour.
Trajectory inference—PAGA
To analyse myeloid cell trajectory in tumour dataset, we recomputed a
neighbourhood graph from the same 15-dimensional harmonised PCA
space as above, but only within myeloid cell populations. We next
applied PAGA
38 within the Scanpy 65 package to the neighbourhood
graph. In parallel, we computed the diffusion map and its force-
directed layout for visualisation using the Pegasus package75.W e ﬁnally
overlaid the PAGA network with the diffusion map using the scVelo
package. We repeated the same analysis workﬂow but on non-immune
cells in the tumour dataset.
Copy number analysis
We applied the CopyKAT package to the single-cell RNA-seq data to
obtain copy number calls. The Copykat pipeline was extended to
obtain conﬁdent copy number calls per cell, per chromosome arm,
beyond the hierarchical clustering the standard pipeline produces.
Per cell copy number calls were obtained as follows: ﬁrst, the
regular CopyKAT (v1.0.5) pipeline was run on the unmodi ﬁed UMI
counts of a particular patient/environment (i.e., tumour or back-
ground) combination with default parameters, except for norm.cell.-
names. The norm.cell.names parameter allows for specifying which
cells are used as con ﬁdent diploid normals during expression nor-
malisation. CopyKAT was set to use all cells labelled as cDC2 dendritic
cells, as they are available in great numbers across all patients and an
initial inspection of their expression pro ﬁles revealed no systematic
copy number alterations.
After CopyKAT has completed, a calling step was applied that is
aimed to call whole chromosome arm alterations in individual cells. We
reasoned that, on a chromosome arm basis, the distribution of binned-
and-normalised expression from CopyKAT should be signi ﬁcantly
different (higher or lower) than the distribution of the same bins in all
conﬁdently diploid cells. For each chromosome arm, we model the
distribution of all data bins from the con ﬁdently diploid cells as a
normal distribution. Each bin on that same chromosome arm from a
candidate aneuploid cell is then tested against that distribution.
Finally, when more than 50% of bins across that chromosome arm are
signiﬁcant, the arm is marked as altered in that cell.
The above-described procedure yields a conservative true/false
call per cell, per chromosome arm without directly distinguishing
between gains and losses. To obtain a proﬁle with gains and losses as is
shown in Fig.4A, we discretise the values for each bin in each cell: If the
arm is altered and the expression value of the bin is negative:−1, if the
arm is altered and the expression value is positive: +1, if the arm is
unaltered: 0. The discretized values are then ﬁnally summed per bin
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 13

across all cells of a particular cell type and divided by the number of
cells of that cell type to obtain the fraction of cells with an alteration as
shown in Fig. 4A.
Immunohistochemistry (IHC) and neutral lipid staining
Tissues were frozen in dry-ice-cooled isopentane and stored in air-tight
tissue cryovials at −80 °C. The tissues were embedded in an optimal
cutting temperature compound (OCT) and cryosectioned in a pre-
cooled cryostat at 10μm thickness on SuperFrost slides. On the day of
the experiment, slides were thawed at room temperature for less than
5 min, then immersed in aﬁxation solution (4% PFA in PBS) for 20 min.
After three washes with PBS, each section was permeabilized with
freshly prepared 0.2% Triton-X100 (Sigma Aldrich) for 10 min at room
temperatures, followed by three washes in PBS. Unspeciﬁcb i n d i n gw a s
blocked by incubating the sections in PBS + 2.5% BSA for 1 h at room
temperature. Following two washes in PBS, sections were incubated
with recombinant rabbit anti-CD68 (Abcam ab213363, 1:50) and mouse
anti-STAB1 (Santa Cruz Biotechnology sc-293254, 10 µg/ml) in PBS +
0.5% BSA overnight at 4 °C. Primary antibodies were removed and
sections washed three times with PBS, then incubated with the
appropriate secondary antibodies (goat anti-rabbit AlexaFluor 594 and
goat anti-mouse AlexaFluor 488 Abcam) 1:500 in PBS + 0.5% BSA for
2 h at room temperature, protected from light. Two confocal immu-
nohistochemistry z-stacks each for tumour and background tissue
from three patients were analysed. Using Fiji (ImageJ) software, the
STAB1+ and CD68+ areas were segmented by automatic thresholding
and quantiﬁed in each image of the z-stack.
To assess the levels of cholesterol and neutral lipids we further
stained tumour and background tissue sections with BODIPY ™ 493/
503 (Invitrogen). After three washes in PBS, sections were incubated
with a 10 µg/ml solution of BODIPY ™ 493/503 in PBS (1:100 from a
stock 1 mg/ml solution in DMSO) for 15 min at room temperature.
Following four washes in PBS, sections were incubated for 90 s with
TrueVIEW (Vector Laboratories), washed by immersing in PBS for
5 min, then tap-dried and mounted in VECTASHIELD Vibrance™ Anti-
fade. Sections were imaged using a Zeiss LSM 710 confocal microscope
at ×20 (Plan-Apochromat ×20/0.8 M27) and ×63 (Plan-Apochromat
×63/1.40 Oil DIC M27) magni ﬁcation. Tile scans were set to cover an
area of 3541 × 3542 microns for all sections. ImageJ was used to remove
background BODIPY signals and calculate the area covered by the
t h r e s h o l d e dB O D I P Yo nt h es t i t c h e di m a g e s .T oc o m p a r et h ea r e a
covered by BODIPY in tumour and background, we used a pairedt test
at a patient level, after conﬁrming the normal distribution of the data
using a Shapiro–Wilk test.
Foetal lung integration
To investigate the oncofetal reprogramming of myeloid cells in
NSCLC, we took advantage of a published scRNA-seq dataset of foetal
lung myeloid cells 55 and the published “MoMac-VERSE”[ 56.T h e
expression of the “STAB1 signature genes” and of the “AMɸ signature
genes” across lung foetal myeloid cells was determined using the
AddModuleScorefunction in Seurat v4.3. To combine foetal lung and
adult lung tumour-inﬁltrating myeloid cells, we isolated the myeloid
cells from our tumour and background datasets and integrated those
with the aforementioned foetal lung myeloid dataset using the Pegasus
package, following the following workﬂow: (i) remove rarely expressed
genes (less than 10 cells), normalisation and log1p transformation, (ii)
robust and highly-variable gene selection, (iii) PCA with optimal PC
number determined by random matrix theory (resulting in 75 PCs), (iv)
batch effect correction using Harmony
67, and (v) Leiden clustering on
neighbourhood graph. The dendrogram was built by estimating the
correlation distance between cell types on the harmonised PC
embedding space, under complete linkage criterion of hierarchical
clustering. The UMAP was computed to obtain a 2D summary of the
harmonised PC space.
10x Genomics Visium spatial transcriptomics
Tissues were frozen in dry-ice-cooled isopentane and stored in air-tight
tissue cryovials at −80 °C. Prior to undertaking any spatial tran-
scriptomics protocol, the tissues were embedded in OCT compound
and tested for RNA quality with an Agilent BioAnalyser. Tissues with
RNA integrity (RIN) values > 7 were cryosectioned in a pre-cooled
cryostat at 10 μm thickness. Two consecutive sections were cryosec-
tioned at 10 μm thickness in a pre-cooled cryostat and transferred to
the four 6.5 mm × 6.5 mm capture areas of the gene expression slide.
Slides wereﬁxed in methanol for 30 min prior to staining with H&E and
then imaged using the Nanozoomer slide scanner. The tissues under-
went permeabilization for 24 min. Reverse transcription and second
strand synthesis was performed on the slide with cDNA quantiﬁcation
using qRT-PCR using KAPA SYBR FAST-qPCR kit (KAPA Biosystems)
and analysed on the QuantStudio (ThermoFisher). Following library
construction, these were quanti ﬁed and pooled at 2.25 nM con-
centration. Pooled libraries from each slide were sequenced on
NovaSeq SP (Illumina) using 150 base pair paired-end dual-indexed set-
up to obtain a sequencing depth of ~50,000 reads as per 10x Genomics
recommendations. The sequencing libraries were then processed by
SpaceRanger (version 1.1.0) on the reference GRCh38 human reference
genome to estimate gene expression on spots.
Spatial cell typing with cell2location
We used cell2location 34 to deconvolute the cellular composition of
each capture area (spot). As our scRNA-seq cells were annotated
independently for tumour and the combined B/H datasets, we applied
the deconvolution model separately as well, using tumour annotation
to infer spatial cell composition of tumour sections, and background
annotations for background datasets. Only spots with total UMI counts
above 800 were used in downstream analysis.
The cell-type abundance in tumour and background sections were
computed by summing up the q05 cell abundance, as estimated by
cell2location, across spots that passed QC. Cell-type composition was
computed by normalising each cell type ’s abundance with the total
abundance of all cell types. We compared cell-type composition
between tumour and background with Wilcoxon signed-rank test,
followed by Bonferroni correction.
On tumour sections, we estimated the correlation distance on
cell-type composition across valid spots, applied hierarchical cluster-
i n gw i t hc o m p l e t el i n k a g e ,a n dv i s u a l i s e dt h er e s u l t sa sad e n d r o g r a m .
In addition, we applied non-negative matrix factorisation analysis to
the q05 estimation of cell-type abundance with eight factors.
Ligand–receptor colocalization analysis
To study the expression of ligand–receptor pairs on the 10X Visium, we
ﬁrst binarised the expression of each gene in the LR pairs in the spots
that passed QC. We considered a gene being expressed in a spot if its
cell2location estimated abundance were higher than the median
counts for that gene in the corresponding section. We counted spots
where both genes in each LR pair were either co-expressed or not, in
tumour and background sections from the same patient, and subse-
quently, applied the χ
2 test on the contingency table. To correct for
multiple comparisons, we adjusted the P value using a conservative
Bonferroni correction for all the LRs enriched in tumours in the cell-
phoneDB analysis (309 * 8 patients). LRs were considered signiﬁcantly
enriched in tumour if the Bonferroni-adjustedP value was lower than
0.05 in at least four patients.
Multiplexed Immunoﬂuorescence
5 μm thick sections were generated from NSCLC FFPE tumour blocks.
An antibody cocktail was prepared with optimal dilutions of each of
the following conjugated antibodies: anti-human Stabilin-1 antibody
(clone #840449, catalogue #MAB3825, R&D systems) was conjugated
to a custom oligo barcode according to instructions in Akoya
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 14

Biosciences’ antibody conjugation kit (Conjugation kit, #7000009;
Akoya) while human CD68 (clone #KP1, catalogue #4550113, Akoya)
and human PanCK (clone AE-1/AE-3, catalogue #4150020, Akoya) were
obtained directly pre-conjugated to oligo barcodes from Akoya Bios-
ciences. Complementary oligo-conjugatedﬂuorophore reporters were
obtained from Akoya Biosciences. Tissue multiplexed immuno-
ﬂuorescence staining and image acquisition were performed accord-
ing to Akoya Phenocycler-Fusion user guide (PD-000011 Rev. A.,
Akoya). OME-TIFF ﬁles were generated and processed for image
analysis.
Image analysis
Analysis of the multiplexed immuno ﬂuorescence images (generated
from Akoya Phenocycler-Fusion platform) was performed using Vis-
iopharm (version 2023.09.3.15043 × 64) on the entire tissue area.
Brieﬂy, cell segmentation (including both nuclear and cytoplasmic
segmentation) wasﬁrst performed using Visiopharm’s “Cell Detection,
AI (Fluorescence) ” (version 2023.09.3.15043 × 64) with its default
parameters. After cell segmentation, Visiopharm’s “Phenoplex Guided
Workﬂow” was used. DAPI (nucleus), CD68 (cell body) and STAB1 (cell
body) variables were selected and manually thresholded to de ﬁne
positive and negative cells for each marker and generate a co-
occurrence matrix. Macrophages were de ﬁned as [DAPI + , CD68 + ]
while STAB1+ macrophages were de ﬁned as [DAPI + , CD68 + ,
STAB1 + ].
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
The scRNA-seq and Visium datasets generated in this study are publicly
available at BioStudies ( https://www.ebi.ac.uk/biostudies/)w i t h
accession numbers E-MTAB-13526 and E-MTAB-13530,r e s p e c t i v e l y .
The remaining data are available within the Article, Supplementary
Information or Source Data ﬁle Source data are provided with
this paper.
Code availability
The scripts used for all the analyses and to produce all theﬁgures in the
manuscript are available at https://gitlab.com/cvejic-group/lungand
https://github.com/sdentro/copykat_pipeline.
References
1. Sung, H. et al. Global cancer statistics 2020: GLOBOCAN estimates
of incidence and mortality worldwide for 36 cancers in 185 coun-
tries. CA. Cancer J. Clin. 71,2 0 9–249 (2021).
2 . S i e g e l ,R .L . ,M i l l e r ,K .D .&J e m a l ,A .C a n c e rs t a t i s t i c s ,2 0 1 8 .Ca.
Cancer J. Clin. 68,7 –30 (2018).
3. Nicholson, A. G. et al. The International Association for the Study of
Lung Cancer Lung Cancer Staging Project: proposals for the revi-
sion of the clinical and pathologic staging of small cell lung cancer
in the forthcoming eighth edition of the TNM classiﬁcation for lung
cancer. J. Thorac. Oncol. 11,3 0 0–311 (2016).
4. Mantovani, A., Allavena, P., Marchesi, F. & Garlanda, C. Macro-
phages as tools and targets in cancer therapy. Nat. Rev. Drug Dis-
cov. 21,7 9 9–820 (2022).
5. DeNardo, D. G. & Ruffell, B. Macrophages as regulators of tumour
immunity and immunotherapy.Nat. Rev. Immunol. 19,
369–382 (2019).
6 . T h a i ,A .A . ,S o l o m o n ,B .J . ,S e q u i s t ,L .V . ,G a i n o r ,J .F .&H e i s t ,R .S .
Lung cancer. Lancet 398,5 3 5–554 (2021).
7. Leader, A. M. et al. Single-cell analysis of human non-small cell lung
cancer lesions reﬁnes tumor classiﬁcation and patient stratiﬁcation.
Cancer Cell 39,1 5 9 4–1609.e12 (2021).
8 . W u ,F .e ta l .S i n g l e - c e l lp r oﬁling of tumor heterogeneity and the
microenvironment in advanced non-small cell lung cancer.Nat.
Commun. 12,2 5 4 0( 2 0 2 1 ) .
9. Kim, N. et al. Single-cell RNA sequencing demonstrates the mole-
cular and cellular reprogramming of metastatic lung adenocarci-
noma. Nat. Commun. 11, 2285 (2020).
10. Guo, X. et al. Global characterization of T cells in non-small-cell
lung cancer by single-cell sequencing.Nat. Med. 24,
978–985 (2018).
11. Chen, J. et al. Single-cell transcriptome and antigen-immunoglobin
analysis reveals the diversity of Bcells in non-small cell lung cancer.
Genome Biol. 21,1 5 2( 2 0 2 0 ) .
12. Zilionis, R. et al. Single-cell transcriptomics of human and mouse
lung cancers reveals conserved myeloid populations across indi-
viduals and species. Immunity 50,1 3 1 7–1334.e10 (2019).
13. Lavin, Y. et al. Innate immune land scape in early lung adenocarci-
noma by paired single-cell analyses.Cell 169,7 5 0–765.e17 (2017).
14. Salcher, S. et al. High-resolution single-cell atlas reveals diversity
and plasticity of tissue-residentneutrophils in non-small cell lung
cancer. Cancer Cell 40,1 5 0 3–1520.e8 (2022).
15. Maynard, A. et al. Therapy-induced evolution of human lung cancer
revealed by single-cell RNA sequencing.Cell 182,
1232–1251.e22 (2020).
16. Adams, D. L. et al. Circulating giant macrophages as a potential
biomarker of solid tumors. P r o c .N a t l .A c a d .S c i .U S A111,
3514–3519 (2014).
1 7 . A l i ,A . ,A d a m s ,D .L . ,K a s a b w a l a ,D .M . ,T a n g ,C . - M .&H o ,T .H .
Cancer associated macrophage-like cells in metastatic renal cell
carcinoma predicts for poor prognosis and tracks treatment
response in real time. Sci. Rep. 13,1 0 5 4 4( 2 0 2 3 ) .
1 8 . G i r o n d a ,D .J .e ta l .C a n c e ra s s ociated macrophage-like cells and
prognosis of esophageal cancer after chemoradiation therapy.J.
Transl. Med. 18, 413 (2020).
19. Manjunath, Y. et al. Tumor-cell –macrophage fusion cells as liquid
biomarkers and tumor enhancers in cancer.Int. J. Mol. Sci. 21,
1872 (2020).
20. Manjunath, Y. et al. Circulating giant tumor-macrophage fusion
cells are independent prognosticators in patients with NSCLC. J.
Thorac. Oncol. 15,1 4 6 0–1471 (2020).
21. Sutton, T. L. et al. Circulating cells with macrophage-like char-
acteristics in cancer: the importance of circulating neoplastic-
immune hybrid cells in cancer. Cancers 14, 3871 (2022).
22. Lotfollahi, M. et al. Mapping single-cell data to reference atlases by
transfer learning.Nat. Biotechnol.40,1 2 1–130 (2022).
23. Collin, M. & Bigley, V. Human dendritic cell subsets: an update.
Immunology154,3 –20 (2018).
24. Li, C., Jiang, P., Wei, S., Xu, X. & Wang, J. Regulatory T cells in tumor
microenvironment: new mechanisms, potential therapeutic strate-
gies and future prospects. Mol. Cancer 19, 116 (2020).
25. Wu, Y. et al. A local human V δ1 T cell population is associated with
survival in nonsmall-cell lung cancer.Nat. Cancer3, 696–709 (2022).
26. Mensurado, S., Blanco-Domínguez, R. & Silva-Santos, B. The
emerging roles of γδ T cells in cancer immunotherapy.Nat. Rev.
Clin. Oncol. 20,1 7 8–191 (2023).
27. Park, M. D. et al. TREM2 macrophages drive NK cell paucity and
dysfunction in lung cancer.Nat. Immunol. 24,7 9 2–801 (2023).
28. Relli, V., Trerotola, M., Guerra, E. & Alberti, S. Abandoning the notion
of non-small cell lung cancer.Trends Mol. Med.25,5 8 5–594 (2019).
29. Efremova, M., Vento-Tormo, M., Teichmann, S. A. & Vento-Tormo, R.
CellPhoneDB: inferring cell-cell communication from combined
expression of multi-subunit ligand-receptor complexes.Nat. Pro-
toc. 15,1 4 8 4–1506 (2020).
30. Louche, C. D. D. & Roghanian, A. Human inhibitory leukocyte Ig-like
receptors: from immunotolerance to immunotherapy.JCI Insight7,
e151553 (2022).
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 15

31. Camidge, D. R., Doebele, R. C. & Kerr, K. M. Comparing and con-
trasting predictive biomarkers for immunotherapy and targeted
therapy of NSCLC. Nat. Rev. Clin. Oncol. 16,3 4 1–355 (2019).
32. Chae, Y. K. et al. Current landscape and future of dual anti-CTLA4
and PD-1/PD-L1 blockade immunotherapy in cancer; lessons
learned from clinical trials with melanoma and non-small cell lung
cancer (NSCLC). J. Immunother. Cancer6,3 9( 2 0 1 8 ) .
33. Fukuhara, M. et al. The clinical signi ﬁcance of tertiary lymphoid
structure and its relationship with peripheral blood characteristics
in patients with surgically resected non-small cell lung cancer: a
single-center, retrospective study.Cancer Immunol. Immunother.
71, 1129–1137 (2022).
34. Kleshchevnikov, V. et al. Cell2location mapsﬁne-grained cell types
in spatial transcriptomics.Nat. Biotechnol.40,6 6 1–671 (2022).
35. Liu, J. et al. Concordance of MERFISH spatial transcriptomics with
bulk and single-cell RNA sequencing.Life Sci. Alliance 6,
e202201701 (2023).
36. Chananchida, S., Robin, B., Ruth, S. & Yvan, S. Spotless: a repro-
ducible pipeline for benchmarking cell type deconvolution in spa-
tial transcriptomics.eLife 12, RP88431 (2023).
37. Gao, R. et al. Delineating copy n umber and clonal substructure in
human tumors from single-cell transcriptomes.Nat. Biotechnol.39,
599–608 (2021).
38. Wolf, F. A. et al. PAGA: graph abstr action reconciles clustering with
trajectory inference through a topology preserving map of single
cells. Genome Biol. 20,5 9( 2 0 1 9 ) .
39. DeBerardinis, R. J. & Chandel, N. S. Fundamentals of cancer meta-
bolism. Sci. Adv. 2, e1600200 (2016).
40. American Association for Cancer Research. Lactate fuels the
TCA cycle in non-small cell lung cancer. Cancer Discov. 7,
OF10 (2017).
41. Hansen, L. V., Skov, B. G., Ploug, M. & Pappot, H. Tumour cell
expression of C4.4A, a structural homologue of the urokinase
receptor, correlates with poor prognosis in non-small cell lung
cancer. Lung Cancer 58,2 6 0–266 (2007).
42. Willuda, J. et al. Pr eclinical antitumor efﬁcacy of BAY 1129980— a
novel Auristatin-based anti-C4.4A (LYPD3) antibody–drug con-
jugate for the treatment of non-small cell lung cancer.Mol. Cancer
Ther. 16,8 9 3–904 (2017).
43. Gibbings, S. L. et al. Transcriptome analysis highlights the con-
served difference between embryonic and postnatal-derived
alveolar macrophages.Blood 126,1 3 5 7
–1366 (2015).
44. Chen, J. W. & Dhahbi, J. Lung adenocarcinoma and lung squamous
cell carcinoma cancer classiﬁcation, biomarker identiﬁcation, and
gene expression analysis using overlapping feature selection
methods. Sci. Rep. 11,1 3 3 2 3( 2 0 2 1 ) .
45. Xiao, J. et al. Eight potential biomarkers for distinguishing between
lung adenocarcinoma and squamous cell carcinoma.Oncotarget8,
71759–71771 (2017).
46. Blériot, C., Chakarov, S. & Ginhoux, F. Determinants of resident
tissue macrophage identity and function.Immunity 52,
957–970 (2020).
4 7 . H u a n g ,B . ,S o n g ,B .&X u ,C .C h o l e s t e r o lm e t a b o l i s mi nc a n c e r :
mechanisms and therapeutic opportunities.Nat. Metab. 2,
132–141 (2020).
48. Nugent, A. A. et al. TREM2 regulates microglial cholesterol meta-
bolism upon chronic phagocytic challenge.Neuron 105,
837–854.e9 (2020).
49. Molgora, M. et al. TREM2 modulation remodels the tumor myeloid
landscape enhancing anti-PD-1 immunotherapy.Cell 182,
886–900.e17 (2020).
50. Khantakova, D., Brioschi, S. & Molgora, M. Exploring the impact of
TREM2 in tumor-associated macrophages.Vaccines10, 943 (2022).
51. Ward, D. M. & Kaplan, J. Ferropo rtin-mediated iron transport:
expression and regulation.Biochim. Biophys. Acta1823,
1426–1433 (2012).
52. Recalcati, S. et al. Differential regulation of iron homeostasis during
human macrophage polarized activation.Eur. J. Immunol. 40,
824–835 (2010).
53. Sharma, A., Blériot, C., Currenti, J. & Ginhoux, F. Oncofetal repro-
gramming in tumour development and progression.Nat. Rev.
Cancer 22,5 9 3–602 (2022).
54. Bian, Z. et al. Deciphering human macrophage development at
single-cell resolution.Nature 582,5 7 1–576 (2020).
55. He, P. et al. A human fetal lung cell atlas uncovers proximal-distal
gradients of differentiation and key regulators of epithelial fates.
Cell 185,4 8 4 1–4860.e25 (2022).
56. Mulder, K. et al. Cross-tissue single-cell landscape of human
monocytes and macrophages in health and disease.Immunity 54
,
1883–1900.e5 (2021).
57. Sharma, A. et al. Onco-fetal reprogramming of endothelial cells
drives immunosuppressive macrophages in hepatocellular carci-
noma. Cell 183,3 7 7–394.e21 (2020).
58. Chauvin, J.-M. & Zarour, H. M. TIGIT in cancer immunotherapy. J.
Immunother. Cancer8, e000957 (2020).
59. Acharya, N., Sabatos-Peyton, C. & Anderson, A. C. Tim-3 ﬁnds its
place in the cancer immunotherapy landscape.J. Immunother.
Cancer 8, e000911 (2020).
60. GlaxoSmithKline. A Phase 1 First-Time-in-Human, Open-Label Study
of GSK6097608 Administered as Monotherapy and in Combination
With Anticancer Agents in Participants With Advanced Solid Tumors.
https://clinicaltrials.gov/study/NCT04446351(2023).
61. Chen, Y., Fan, Z., Yang, Y. & Gu, C. Iron metabolism and its con-
tribution to cancer (review).Int. J. Oncol. 54, 1143–1154 (2019).
62. Viitala, M. et al. Immunotherapeutic blockade of macrophage
clever-1 reactivates the CD8+ T-cell response against immunosup-
pressive tumors.Clin. Cancer Res. 25,3 2 8 9–3303 (2019).
63. Park, S.-Y. et al. Stabilin-1 mediates phosphatidylserine-dependent
clearance of cell corpses in alternatively activated macrophages.J.
Cell Sci. 122, 3365–3373 (2009).
64. Lun, A. T. L. et al. EmptyDrops: distinguishing cells from empty
droplets in droplet-based single-cell RNA sequencing data.Gen-
ome Biol. 20, 63 (2019).
65. Wolf, F. A., Angerer, P. & Theis, F. J. SCANPY: large-scale single-cell
gene expression data analysis.Genome Biol. 19,1 5( 2 0 1 8 ) .
66. Wolock, S. L., Lopez, R. & Klein, A. M. Scrublet: computational
identiﬁcation of cell doublets in single-cell transcriptomic data.Cell
Syst. 8,2 8 1–291.e9 (2019).
67. Korsunsky, I. et al. Fast, sensitive and accurate integration of single-
cell data with harmony. Nat. Methods 16,1 2 8 9–1296 (2019).
68. Tran, H. T. N. et al. A benchmark of batch-effect correction methods
for single-cell RNA sequencing data.Genome Biol. 21, 12 (2020).
69. Traag, V. A., Waltman, L. & van Eck, N. J. From Louvain to Leiden:
guaranteeing well-connected communities.Sci. Rep. 9,
5233 (2019).
70. McInnes, L., Healy, J. & Melville, J. UMAP: uniform manifold
approximation and projection for dimension reduction. Preprint at
https://arxiv.org/abs/1802.03426(2018).
71. Mann, H. B. & Whitney, D. R. On a test of whether one of two random
variables is stochastically larger than the other.Ann. Math. Stat.
18,
50–60 (1947).
72. Haynes, W. Bonferroni correction. In Encyclopedia of Systems
Biology (eds Dubitzky, W. et al.) 154–154 (Springer New York, 2013).
73. Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold
change and dispersion for RNA-seq data with DESeq2.Genome Biol.
15,5 5 0( 2 0 1 4 ) .
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 16

74. Yu, G., Wang, L.-G., Han, Y. & He, Q.-Y. clusterProﬁler: an R package
for comparing biological themes among gene clusters.Omics J.
Integr. Biol. 16,2 8 4–287 (2012).
75. Li, B. et al. Cumulus provides cl oud-based data analysis for large-
scale single-cell and single-nucleus RNA-seq.Nat. Methods 17,
793–798 (2020).
Acknowledgements
The authors are greatly thankful to the Papworth Hospital Research
Tissue Bank for providing samples with data, and in particular to D. Rassl.
The authors would like to thank L. Campos for the annotation of tumour
histologies; A.M. Ranzoni, B. Myersand E. Panada for sample collection
and processing; M. Nelson for computational support with initial clus-
tering of scRNA-Seq and application of cell2location; Alessandro Di
Tullio, GSK for insightful discussions; Cancer Research UK Cambridge
Institute (CRUK CI) (Grant # CTRQQR-2021\100012) Genomics Core
Facility for library preparation and sequencing services; Wellcome
Sanger Institute (WSI) DNA pipelinesfor their contribution to sequencing
the data; S. Leonard from New Pipeline Group (NPG) for pre-processing
of sequencing data; the Cambridge NIHR BRC Cell Phenotyping Hub for
support with cell sorting. We thank R. Möller, P. Rainer, and U. Tiemann
for critically reading the manuscript. This study was conceived and
funded by Open Targets (OTAR2060, A.C.); Core support grants from
the Wellcome Trust and Wellcome Sanger Institute and both Wellcome
and the MRC to the Wellcome Trust-Medical Research Council Cam-
bridge Stem Cell Institute (203151/Z/16/Z, A.C.); European Research
Council (CONTEXT 101043559, A.C.); Views and opinions expressed are
however those of the author(s) only and do not necessarily reﬂect those
of the European Union or the European Research Council Executive
Agency. Neither the European Union nor the granting authority can be
held responsible for them.
Author contributions
A.C. conceived the study and oversaw all experiments and analysis.
M . D . Z .p e r f o r m e de x p e r i m e n t sa n da n a l y s i s .H . X .l e ds p a t i a lt r a n -
scriptomics analyses and co-analysed the scRNA-seq data. J.S.P. per-
formed Visum experiments under O.B. supervision. Z.S. led the
application of CellPhoneDB under M.G. supervision. S.C.D. led CopyCAT
analysis. J.T. and S.C.A. performed Multiplexed Immunoﬂuorescence
under A.H. supervision. A.H. contributed to the interpretation of results.
E.A. performed DEA. A.C. and M.D.Z. wrote the manuscript, and all
authors edited and reviewed the manuscript.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-024-48700-8.
Correspondenceand requests for materials should be addressed to
Ana Cvejic.
Peer review informationNature Communicationsthanks Charles Powell
and the other, anonymous, reviewer(s)for their contribution to the peer
review of this work. A peer review ﬁle is available.
Reprints and permissions informationis available at
http://www.nature.com/reprints
Publisher’s note Springer Nature remains neutral with regard to jur-
isdictional claims in published maps and institutional afﬁliations.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if
changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visithttp://creativecommons.org/
licenses/by/4.0/.
© The Author(s) 2024
Article https://doi.org/10.1038/s41467-024-48700-8
Nature Communications|         (2024) 15:4388 17