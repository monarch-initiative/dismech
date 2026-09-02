---
reference_id: DOI:10.1038/s41467-024-50527-2
title: Single cell transcriptomic profiling identifies tumor-acquired and therapy-resistant cell states in pediatric rhabdomyosarcoma
authors:
- Sara G. Danielli
- Yun Wei
- Michael A. Dyer
- Elizabeth Stewart
- Heather Sheppard
- Marco Wachtel
- Beat W. Schäfer
- Anand G. Patel
- David M. Langenau
journal: Nature Communications
year: '2024'
doi: 10.1038/s41467-024-50527-2
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41467-024-50527-2.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41467-024-50527-2.pdf
---

# Single cell transcriptomic profiling identifies tumor-acquired and therapy-resistant cell states in pediatric rhabdomyosarcoma
**Authors:** Sara G. Danielli, Yun Wei, Michael A. Dyer, Elizabeth Stewart, Heather Sheppard, Marco Wachtel, Beat W. Schäfer, Anand G. Patel, David M. Langenau
**Journal:** Nature Communications (2024)
**DOI:** [10.1038/s41467-024-50527-2](https://doi.org/10.1038/s41467-024-50527-2)

## Content

Abstract
Rhabdomyosarcoma (RMS) is a pediatric tumor that resembles undifferentiated muscle cells; yet the extent to which cell state heterogeneity is shared with human development has not been described. Using single-cell/nucleus RNA sequencing from patient tumors, patient-derived xenografts, primary in vitro cultures, and cell lines, we identify four dominant muscle-lineage cell states: progenitor, proliferative, differentiated, and ground cells. We stratify these RMS cells/nuclei along the continuum of human muscle development and show that they share expression patterns with fetal/embryonal myogenic precursors rather than postnatal satellite cells. Fusion-negative RMS (FN-RMS) have a discrete stem cell hierarchy that recapitulates fetal muscle development and contain therapy-resistant FN-RMS progenitors that share transcriptomic similarity with bipotent skeletal mesenchymal cells. Fusion-positive RMS have tumor-acquired cells states, including a neuronal cell state, that are not found in myogenic development. This work identifies previously underappreciated cell state heterogeneity including unique treatment-resistant and tumor-acquired cell states that differ across RMS subtypes.

Article https://doi.org/10.1038/s41467-024-50527-2
Single cell transcriptomic proﬁling identiﬁes
tumor-acquired and therapy-resistant cell
states in pediatric rhabdomyosarcoma
Sara G. Danielli 1,8,Y u nW e i2,3,4,8,M i c h a e lA .D y e r5,E l i z a b e t hS t e w a r t5,6,
Heather Sheppard 7,M a r c oW a c h t e l1,9 ,B e a tW .S c h ä f e r1,9 ,
Anand G. Patel 5,6,9 & David M. Langenau 2,3,4,9
Rhabdomyosarcoma (RMS) is a pediatric tumor that resembles undiffer-
entiated muscle cells; yet the extent to which cell state heterogeneity is shared
with human development has not been described. Using single-cell/nucleus
RNA sequencing from patient tumors, patient-derived xenografts, primary in
vitro cultures, and cell lines, we identify four dominant muscle-lineage cell
states: progenitor, proliferative, differentiated, and ground cells. We stratify
these RMS cells/nuclei along the continuum of human muscle development
and show that they share expression patterns with fetal/embryonal myogenic
precursors rather than postnatal satellite cells. Fusion-negative RMS (FN-RMS)
have a discrete stem cell hierarchy that recapitulates fetal muscle development
and contain therapy-resistant FN-RMS progenitors that share transcriptomic
similarity with bipotent skeletal mesenchymal cells. Fusion-positive RMS have
tumor-acquired cells states, including a neuronal cell state, that are not found
in myogenic development. This work identiﬁes previously underappreciated
cell state heterogeneity including unique treatment-resistant and tumor-
acquired cell states that differ across RMS subtypes.
Rhabdomyosarcoma (RMS) is a pediatric solid tumor that shares fea-
tures with arrested skeletal muscle precursors 1,2. Pediatric RMS has
been classiﬁed into three major subtypes that have divergent mole-
cular drivers: (i) fusion-positive RMS (FP-RMS) have DNA transloca-
tions that juxtapose PAX3 or PAX7 with FOXO1 (PAX3::FOXO1 or
PAX7::FOXO1); (ii) fusion-negative RMS (FN-RMS) lack pathognomonic
translocation events, but commonly have oncogenic activation of RAS
signaling; and (iii) spindle cell/sclerosing rhabdomyosarcoma (SS-
RMS, a subclass previously classiﬁed as FN-RMS) are driven either by
NCOA2::VGLL2 translocations or a p.Leu122Arg mutation in theMYOD1
transcription factor
3– 13. Despite aggressive therapies combining
radiation, chemotherapy, and surgery, 70% of patients with unresect-
able or disseminated disease develop recurrent RMS that has a dismal
5-year overall survival rate of under 20%14– 17.
Like many pediatric cancers, RMS tumors have a low mutational
burden, and few known genetic alterations reliably predict recurrent
disease
8,18– 20. Thus, it is critical to understand the non-genetic hetero-
geneity within RMS, and the role that speciﬁc cell subpopulations play
in driving the clinical behavior of RMS. Indeed, multiple groups have
applied single-cell transcriptomics to discover distinct RMS cell
Received: 26 October 2023
Accepted: 11 July 2024
Check for updates
1Department of Oncology and Children ’s Research Center, University Children ’s Hospital of Zurich, Zürich, Switzerland. 2Molecular Pathology Unit,
Massachusetts General Research Institute, Charlestown, MA, USA. 3Krantz Family Center for Cancer Research, Massachusetts General Hospital,
Charlestown, MA, USA. 4Harvard Stem Cell Institute, Cambridge, MA, USA. 5Department of Developmental Neurobiology, St. Jude Children ’sR e s e a r c h
Hospital, Memphis, TN, USA. 6Department of Oncology, St. Jude Children ’s Research Hospital, Memphis, TN, USA. 7Department of Pathology, St. Jude
Children’s Research Hospital, Memphis, TN, USA. 8These authors contributed equally: Sara G. Danielli, Yun Wei. 9These authors jointly supervised this
work: Marco Wachtel, Beat W Schäfer, Anand G Patel, David M Langenau. e-mail: marco.wachtel@kispi.uzh.ch ; beat.schaefer@kispi.uzh.ch ;
anand.patel2@stjude.org ; dlangenau@mgh.harvard.edu
Nature Communications|         (2024) 15:6307 1
1234567890():,;
1234567890():,;

subpopulations21– 24. These studies consistently identi ﬁed malignant
cells with expression patterns similar to developing skeletal muscle;
yet, each study introduced different nomenclature and classi ﬁcation
strategies due to limited sample numbers, differences in bioinformatic
approaches, and mapping shared developmental cell states across
mouse and/or human muscle. As a result, there is a need to clearly
deﬁne cell states, to assess developmental similarity between RMS and
human muscle, and to evaluate the dynamics of cell state transitions
during therapy.
Here, we present a consensus evaluation of intratumoral hetero-
geneity in human RMS by combining datasets encompassing 72 samples
from patient tumors, patient-derived xenograft (PDX) models, PDX-
derived primary cell cultures (PDCs), and commercial cell lines
(CLs)
21,22,24,25. By uniformly processing and integrating these datasets, we
generated a comprehensive and uniﬁed annotation of RMS-speciﬁcc e l l
subpopulations. In total, we identiﬁed four major RMS cell subpopula-
tions— (1) progenitor cells that are largely quiescent and express
characteristic mesenchymal and extracellular matrix genes; (2) differ-
entiated cells that are post-mitotic and resemble mature skeletal muscle;
(3) proliferative cells that are actively dividing but lack expression of
progenitor or differentiated cell programs; and, (4) ground state cells
that lack expression of the other three dominant signatures. While we
identiﬁed shared RMS cell states with embryonal and fetal skeletal
muscle development, we also found subtype-speciﬁcc e l ls t a t e s .S o m e
FP-RMS contain a unique neuronal cell state, indicating that a subset of
FP-RMS acquire non-myogenic gene expression programs during
tumorigenesis. In addition, progenitor cells in FN-RMS closely resemble
bipotent SkM. Mesenchymal cells found in fetal muscle development,
which was not observed in FP-RMS. Both FN-RMS and FP-RMS failed to
share similarity with postnatal satellite cells. Together, these results
challenge the dogma that RMS follow rigid muscle developmental
hierarchies and that RMS originate from or resemble satellite-cell
derived post-natal muscle. Finally, we show that our cell state signatures
can be used to identify treatment-persistent cell populations. Speciﬁ-
cally, progenitor and neuronal signatures were signiﬁcantly enriched in
treated samples in FN-RMS and FP-RMS, respectively. In total, this work
presents a harmonized model of intratumoral heterogeneity within RMS
and provides insights into the intersection of normal development and
therapy resistance within cancer.
Results
A single-cell/nucleus transcriptomic atlas of RMS
Several groups have investigated the transcriptional heterogeneity of
rhabdomyosarcoma (RMS) using single-cell RNA (scRNAseq) and/or
single-nucleus RNA sequencing (snRNAseq). These studies identiﬁed
RMS cell states using different bioinformatic methods, leading to
divergent and often confusing nomenclature
21,22,24. To overcome these
limitations, we collected and uniformly processed 72 scRNAseq or
snRNAseq datasets from four previously published studies that used
the 10X Genomics platform21,22,24,25 (n = 107,523 malignant cells/nuclei).
This uniﬁed cohort included tumors and experimental models derived
from patients seen across four medical centers worldwide, along with
established cell line models. This dataset encompasses the largest
transcriptomic atlas for any sarcoma analyzed to date and includes
patient tumors (n = 21), PDXs (patient-derived xenograft,n =3 2 ) ,P D C s
(patient derived cell culture, n = 14), and conventional CLs (cell
lines, n =5 ) ( F i g .1A). Forty-ﬁve datasets were generated from either
patient tumor samples or PDXs from the St. Jude Childhood Solid
Tumor Network (CSTN)
26, and an additional 6 PDCs were generated
from CSTN xenografts (Supplementary Data 1) 22. Importantly, these
samples are representative of intermediate and high-risk RMS, and
include primary, recurrent, and metastatic tumors (Supplementary
Data 1). All major subtypes of disease were represented including FP-
RMS (n = 27, previously known as alveolar RMS), FN-RMS (n =4 3 ,p r e -
viously known as embryonal RMS), and two SS-RMS cases with
MYOD1
L122R-mutations (Supplementary Data 1). After merging datasets
and performing dimensionality reduction, malignant cells/nuclei
grouped separately based on patient and model systems, consistent
with observations in other cancer types
27– 29 (Fig. 1Ba n dS 1 A ) .
To identify shared transcriptomic signatures across different
samples, we corrected for inter-patient variation utilizing anchor-
based integration
30. Following integration, samples were intermixed
and as expected, we did not identify outlier cells/nuclei that were
attributable to only one patient, dataset, or model system (Fig. S1B).
We next applied unsupervised clustering and identi ﬁed 12 Louvain
clusters that could be grouped into distinct subpopulations based on
shared transcriptomic proﬁles (Fig. 1C, D and S1C). These subpopula-
tions include: (1) two clusters with cells/nuclei expressing varying
levels of mesoderm transcription factors (e.g., MEOX2), cell surface
markers (e.g.,CD44, EGFR), and extracellular matrix proteins (e.g.,FN1)
which we call “progenitor” and “transiting-progenitor” (“TR-pro-
genitor”) that were distinguished from each other based on overall
levels of marker expression; (2) a “proliferative” subpopulation that
comprised four clusters that shared GSEA signature similarity with
proliferative and DNA replication gene modules; (3) two clusters of
“transiting-differentiated” (“TR-differentiated”)a n d “differentiated”
muscle cells/nuclei expressing transcription factors from committed
muscle cells (e.g.,MYOG) and muscle contraction proteins (e.g.,TNNI1,
MYH8); (4) an “apoptotic” subpopulation expressing genes associated
with cell death (e.g., BNIP3); and, (5) “ground” cells that do not show
any enrichment of these signatures (Fig.1C– E and S1C; Supplementary
Data 2 and 3). Importantly, we compared ﬁve matched PDX samples
that were generated by the St. Jude Childhood Solid Tumor Network
26
and that were independently expanded and processed in different
labs
21,24. We noted consistency in cell subpopulation distributions for
these samples derived from the same patient, indicating that our
analysis was not skewed by experimental setting, xenograft passaging,
or protocol differences in cell isolation for scRNAseq (Fig. S1D). We
next performed single-cell compositional data analysis (scCODA) that
uses Bayesian modeling to quantify differences within single-cell RNA-
seq clusters across cohorts
31. scCODA analysis identi ﬁed statistically
credible increases in progenitor and TR-progenitor cell fractions in FN-
RMS while FP-RMS had elevated numbers of TR-differentiated cell
states proportions (Fig. S1E).
A tripartite cell state landscape of RMS
In previous reports, each group identiﬁed clusters of cells/nuclei with
transcriptomic similarity to muscle-lineage cells 21,22,24. Despite these
similarities, each used different sample types, computational methods
to deﬁne gene expression signatures, and differing nomenclature for
each subpopulation. For example, Patel et al. analyzed 18 matched
samples from primary patient and orthotopic PDX models and iden-
tiﬁed three cell populations which they called mesoderm, myoblast,
and myocyte cells based on perceived similarity with mouse muscle
development
24. In their study, the myoblast compartment included
both proliferative and non-proliferative cells. In contrast, Wei et al.
examined 9 PDX and 4 patient tumors to identify four RMS-speciﬁcc e l l
subpopulations that they called mesenchymal, proliferative, differ-
entiated, and ground cells
21. Finally, Danielli et al. studied 14 PDCs and
3 conventional cell lines to group RMS cells into muscle stem-cell-like
cells, cycling progenitors, and differentiated cells
22.
We leveraged our uniﬁed RMS cell atlas to re ﬁne these cell state
signatures. We scored single-cell and single-nucleus proﬁles within the
integrated RMS atlas using published signatures from each prior study.
Signatures from all three studies identi ﬁed similar patterns of het-
erogeneity in the progenitor-like and differentiated-like cells (Fig.2A).
T h eo n ee x c e p t i o nw a st h em y o b l a s ts i g n a t u r ef r o mP a t e le ta l . ,w h i c h
was broadly expressed in most RMS cells or nuclei, and thus does not
identify a discernable cell state in RMS. For all other cell states deﬁned
in these publications, we detected signi ﬁcant overlap between gene
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 2

Fig. 1 | Integrated analysis of single cell and single nuclei sequencing identiﬁes
dominant cell states in human RMS. A Schematic of approach and RMS models
proﬁled by single-cell analysis, created with BioRender.com.B UMAP plot of tumor
cells/nuclei (n = 72 datasets) colored by model of origin21,22,24. C UMAP plot of
integrated tumor cells/nuclei using reciprocal PCA (RPCA) projection. Cells/nuclei
are colored by Louvain cluster (left) or assigned cell states (right).D Heatmap of the
genes (x axis) enriched in Louvain clusters (y axis) across the integrated RMS
dataset (FC > 0.25; n = 400 representative cells/nuclei shown with exception of
cluster 11 that containedn = 101 cells/nuclei). The percentage of cycling cells within
each cluster is shown in the bar plot below.E Summary of the cell state composition
of each RMS dataset (n = 72) with clinical information included as an oncoplot
below. FN-RMS, fusion-negative RMS; FP-RMS, fusion-positive RMS; PDC, PDX-
derived primary culture; CL, cell line; PDX, patient-derived xenograft; snRNAseq,
single-nuclei RNA sequencing; scRNAseq, single-cell RNA sequencing; NA, not
available; TR-progenitor, transiting-progenitor; TR-differentiated, transiting-
differentiated. Gene lists used for generating panels D and E are shown in Sup-
plementary Data 2.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 3

signatures indicating that the previously published studies had inde-
pendently uncovered similar RMS cell states. These data are also
consistent with recently publishedﬁndings from DeMartino et al. that
deﬁned a tripartite cell state landscape in FN- and FP-RMS using a
different nomenclature
23.
To construct consensus signatures for the three dominant RMS
cell states, we selected genes that were present in at least two datasets
to generate signatures for each of the major RMS cell subpopulations.
We generated three signatures that we call progenitor (n =1 7 1g e n e s ) ,
proliferative (n = 157 genes), and differentiated ( n =2 1 5 g e n e s ) s i g -
natures (Fig. 2B and Supplementary Data 4). Because these uni ﬁed
gene signature lists were generated from a variety of models (patient
tumors, PDXs, PDCs, and CLs), they represent a robust and broadly
applicable set of markers for deﬁning each RMS cell state. As expected,
these new high-con ﬁdence consensus cell state signatures demon-
strated signiﬁcant overlap with those originally reported, with the
exception of the Patel, et al. myoblast signature (Fig. 2C).
The muscle lineage score reveals key distinctions between RMS
subtypes
Unsupervised clustering identiﬁed previously unknown transitory cells
within RMS (Fig. 1C– E), which led us to test whether tumor cell het-
erogeneity exists within a continuum between progenitor and differ-
entiated RMS cell states. By comparing the progenitor and
differentiated signature scores to our categorical cell subpopulations,
we found that both the progenitor and the differentiated signatures
showed a gradient of expression across the molecularly de ﬁned sub-
populations (Fig. S2A). Moreover, most cycling cells/nuclei pre-
ferentially mapped to cells with low progenitor and differentiated
scores, irrespective of the RMS subtype (Fig. S2B). These results led us
to create a “muscle lineage score,” deﬁned as the difference between
the differentiated and progenitor signature scores, and to apply this
scoring metric to every single-cell/nucleus proﬁle within our atlas in
relation to their proliferation properties. Indeed, we observed sig-
niﬁcant inter- and intra-tumoral heterogeneity when stratifying tumor
cells using the muscle lineage score. FP-RMS samples had an overall
higher muscle-lineage score when compared to FN-RMS, both at the
single-cell and pseudo-bulk level (Fig. 3A– C). Also of note, the FP-
(n = 93 genes) and FN-RMS (n = 67 genes) core signatures reported by
Wei et al.
21 also separated these two sub types along a continuous
spectrum (Fig. S2C), suggesting underlying gene program differences
between these two subtypes of tumors.
To independently validate our results, we next analyzed an addi-
tional dataset of 19 single-cell RNA-seq datasets from RMS patients
reported by DeMartino et al. that used a plate-based single-cell RNA-
seq technique called SORT-seq
23. Indeed, FN-RMS tumors from
DeMartino et al. had higher overall fractions of cells with progenitor
signatures, while FP-RMS tumors had elevated numbers of cells with
differentiated signatures (Fig. S2D). Moreover, our lineage scoring
method validated that FN-RMS tumors consistently had lower overall
A B
1
-1
0
Pearson 
correlation
Louvain 
Cluster
Assignments
MuSC-like
Cycling
Differentiated
Mesoderm
Myoblast
Myocyte
Mesenchymal
Proliferative
Differentiated
Progenitor 0.92 -0.18 -0.42 0.94 -0.26 -0.42 0.98 -0.24 -0.43
Proliferative -0.23 0.95 -0.14 -0.32 0.02 -0.23 -0.27 0.99 -0.20
Differentiated -0.36 -0.16 0.97 -0.34 -0.01 0.95 -0.39 -0.18 0.98
Danielli et al. Patel et al. Wei et al.
C
UMAP_RPCA_1
Mesenchymal-like
(n = 133)
Proliferation
(n = 114)
Muscle
(n = 75)
Muscle stem-cell-like
(n = 99)
Cycling progenitors
(n = 115)
Differentiated
(n = 119)
Mesoderm
(n = 212)
Myoblast
(n = 291)
Myocyte
(n = 446)
Wei et al. Nat.Cancer. 2022
Patel et al. Dev. Cell. 2022
Danielli et al. Sci. Adv. 2023
highlow
metaprogram score
UMAP_RPCA_2
Harmonized gene markers
Progenitor
(n = 171)
Proliferative(n = 157) Differentiated
(n = 215)
Mes
enchymal-
like (Wei)
Mesoderm 
(Patel)
Muscle stem-cell-like
(Danielli)
Progenit
or
(RMS atlas
)
127
27 38
136
5 0 25
2 12
3 13 49
6 25
31
261
0 10
155
0 0 25
0 70
1 7 32
2 0
5
Proliferation(Wei)
Myoblast(Patel)
Cycling progen
itors(Danielli)
Proliferativ
e
(RMS atlas
)
284
6 14
157
2 0 34
0 12
3 35 7
21 13
88
Muscle(Wei)
My
ocyte
(Patel)
Differentiated
(Danielli)
Differentiated(RMS atlas)
highlow
metaprogram score
Genes present in ≥ 2 datasets
UMAP_RPCA_1
UMAP_RPCA_2
Fig. 2 | A tripartite cell state landscape of RMS tumors and identiﬁcation of cell
state RMS metaprograms. A UMAP plots of integrated tumor cells/nuclei
(n = 107,523 cells) scored for the metaprograms identiﬁed in the original publica-
tions. Number of genes within each metaprogram noted. B Comparison of pub-
lished cell state metaprograms and those deﬁned by our Louvain clustering
approach. Top: Venn diagrams showing overlap of gene markers across the three
original publications and our new analysis (“RMS atlas”). Bottom: UMAP plots of
integrated tumor cells/nuclei (n = 107,523 cells) showing expression of the newly
deﬁned, high conﬁdence cell state gene signatures. Number of genes within each
metaprogram noted. Icons created with BioRender.com.C Pearson correlation
coefﬁcients for the metaprograms identiﬁed in the three original publications and
the new metaprogram signatures deﬁned by our work.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 4

muscle lineage scores, while FP-RMS tumors had elevated muscle
lineage scores (Fig. S2D). In total, our data support a model where RMS
cells lie in a continuum of gene expression deﬁned by three dominant
cell states including progenitor, proliferative, and differentiated cell
states while also containing subtype speci ﬁc gene programs found
within all RMS cells from a given tumor.
Despite overall trends in lower muscle lineage scores in FN-RMS
compared with FP-RMS, we did observe considerable inter-tumoral
variability of the muscle lineage scores across tumors (Fig. 3D). For
example, we identiﬁed FP-RMS with exceptionally high muscle lineage
scores including 20082 and SJRHB013759_A2. By contrast, FN-RMS
SJRHB010928_R1, a pre-treated FN-RMS, and MYOD1
L122R-mutant
MSK74711 had exceptionally low muscle lineage scores.
Neuronal cells are a unique feature of FP-RMS
Our initial analyses centered on combining RMS subtypes together to
identify conserved cell states shared across pediatric RMS. While this
approach enabled us to de ﬁne key muscle-lineage cell states shared
across RMS, it would likely fail to identify subtype-speciﬁc subpopula-
tions or differences in gene expression within deﬁned subpopulations in
RMS subtypes. Our combined large cohort of RMS samples enabled us
to evaluate heterogeneity within FN-RMS, PAX3::FOXO1 FP-RMS, and
FP-RMSFN-RMS
Proliferative score, arb. units
Inter-sample heterogeneity
n = 72 samples
DifferentiatedProgenitor
A
D
BC Muscle lineage 
score
Proliferative 
score
p < 2.2e−16p < 2.2e−16
DifferentiatedProgenitor
FP-RMSFN-RMS
Score, arb.units
Score, arb. units
0.0
0.1
0.2
−0.2 −0.1 0.0 0.1 0.2 0.3
Muscle lineage score, arb. units
(= Differentiated - Progenitor score)
Proliferative score, arb. units
DifferentiatedProgenitor
FN-RMS FP-RMS
Muscle lineage score, arb. units
(= Differentiated - Progenitor score)
Intra-tumor heterogeneity
n = 107,523 cells/nuclei
−0.5
0.0
0.5
1.0
1.5
−1.0 −0.5 0.0 0.5 1.0 1.5
SJRHB010928_R1MSK7471120082 SJRHB013759_A2
UMAP 1UMAP 2
Progenitor
TR−progenitor
Proliferative
Ground
TR−differentiated
Differentiated
Apoptosis
FP-RMS FN-RMS
−1.0
−0.5
0.0
0.5
1.0
20082
aRMS−1
aRMS−2
aRMS−3
aRMS−4
aRMS−5
KFR
Mast118
Mast95
MSK72117
MSK72117_SC
MSK82489
Rh4
Rh41
RMS
SJRHB010468_D1
SJRHB010468_X1
SJRHB013757_D2
SJRHB013757_X1
SJRHB013759_A1
SJRHB013759_A2
SJRHB013759_X14
SJRHB013759_X15
SJRHB031320_D1
SJRHB031320_X1
SJRHB046156_A1
SJRHB046156_X1
20696
21202
29806
eRMS−1.1
eRMS−1.2
eRMS−2.1
eRMS−2.2
eRMS−3.2
eRMS−4
eRMS−8.1
eRMS−8.2
eRMS−8.3
Mast111
Mast139
Mast139_SC
Mast39
Mast85_r1
Mast85_r2
Mast85_r2_SC
MSK74711
RD
SJRHB000026_R2
SJRHB000026_R3
SJRHB000026_X1
SJRHB000026_X2
SJRHB010927_D1
SJRHB010927_X1
SJRHB010928_R1
SJRHB010928_X1
SJRHB011_D
SJRHB011_X
SJRHB012_R
SJRHB012_S
SJRHB012_Y
SJRHB012_Z
SJRHB012405_D1
SJRHB012405_X1
SJRHB013758_D1
SJRHB013758_D2
SJRHB013758_X1
SJRHB013758_X2
SJRHB030680_R1
SJRHB030680_X1
SJRHB049189_D1
SJRHB049189_X1
Muscle lineage score, arb. units
DifferentiatedProgenitor
0.0
0.5
1.0
1.5
−1.0
−0.5
0.0
0.5
1.0
FP-RMSFN-RMS
Fig. 3 | RMS cells lie in a continuum of gene expression de ﬁned by three
dominant cell states including progenitor, proliferative, and differentiated cell
states. A Graphical analysis showing“muscle lineage score” deﬁned as the differ-
ence between the differentiated and progenitor signature scores, and proliferation
score of all RMS cells/nuclei. Subtypes are denoted by purple (FN-RMS) and blue
(FP-RMS). B Average muscle lineage and proliferation scores calculated with
pseudo-bulk data for each of the 72 RMS samples.C Violin plots showing individual
cell expression of proliferative (left) and muscle lineage score (right) across FP-RMS
(n = 40,526 cells/nuclei) and FN-RMS (n = 69,997 cells/nuclei) cells. Boxplots
denote Tukey’sw h i s k e r s( 2 5– 75 percentile represented by minima-maxima; sta-
tistical median as center). Two-sided student’s t test with p values noted in the
ﬁgure. D Violin plots showing cell expression of the muscle-lineage score across
each of the 72 RMS samples. Boxplots denote Tukey’sw h i s k e r s( 2 5– 75 percentile
represented by minima-maxima; statistical median as center). The UMAP plots of
two representative samples for each subtype are shown, withn = 1500 cells/nuclei
for each individual sample. The number of cells/nuclei analyzed for each sample are
reported in Supplementary Data 1.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 5

PAX7::FOXO1 FP-RMS translocated tumors as distinct entities. As
expected, we identiﬁed progenitor, proliferative, and differentiated cell
subpopulations in each molecular subtype (Fig.4Aa n dS 3 A ) .Y e t ,w ea l s o
identiﬁed unexpected differences in gene expression between pro-
genitor cell populations from FP-RMS and FN-RMS (Fig. S3B) and two
previously unreported gene expression clusters (Supplementary
Data 5 and 6). In particular, we found: (1) a group of cells/nuclei in FN-
RMS that express interferon response genes such as ISG15 and IFIT1-3
(“IFN” cluster; 1.5% of total cells/nuclei); and, (2) a tumor subpopulation
in FP-RMS tumors that expresses neuronal marker genes includingDCX,
L1CAM, SYP,a n d CHGA (‘neuronal’cluster; 1.4% and 4.8% of total cells/
nuclei from PAX3::FOXO1 and PAX7::FOXO1 FP-RMS, respectively,
Fig. 4A, S4A and S4B).
To better characterize the FP-RMS neuronal cell state, we ﬁrst
performed gene set enrichment analysis with highly expressed
genes found in this cell cluster and con ﬁrmed enrichment of genes
associated with neurogenesis pathways including axonogenesis
(GO:0007409), central nervous system development (GO:0007417)
and central nervous system neuron differentiation (GO:0021953;
Supplementary Data 6). Second, we scored each FP-RMS subpopula-
tion for the activity of PAX3::FOXO1 fusion oncogene using a pre-
viously deﬁned list of fusion target genes
32. We found that neuronal
cells scored for the highest activity of fusion oncogene activity
(Fig. S4C). Last, we performed immunohistochemistry validation on
PDX tumor tissue (n = 5) and conﬁrmed in situ expression of the neu-
ronal marker synaptophysin (SYP), which correlated with fraction of
neuronal cells detected in our single-cell meta-analysis (Fig. 4B, C).
Overall, these results con ﬁrm that FP-RMS tumors contain a unique
subpopulation of tumor cells that expresses markers of neuronal cells.
Importantly, cells/nuclei expressing the neuronal gene signature were
detected only in a subset of FP-RMS samples ( n =5 o u t o f 1 1 P A X 7 : : -
FOXO1 FP-RMS andn = 5 out of 15 PAX3::FOXO1 FP-RMS, deﬁned as >1%
of total cells/nuclei; Fig. S4D and Supplementary Data 7). Despite
tumors retaining the tripartite muscle lineage programs across models
(Fig. S3C), neuronal subpopulations were detected in larger numbers
in patient tumors and PDXs, but rarely or not at all in primary cultures
or commercial cell lines [Figs. S4E and S4F ; Supplementary Data 7].
The absence of neuronal cells within cell lines may explain why this
rare subpopulation has not been deeply investigated before; more-
over, the rarity of these cells most likely prevented their identiﬁcation
in prior single-institution single-cell cohorts
23,24.
Lastly, we sought to identify potential candidate cell surface
markers in our consensus analysis that could be used to both address
future research questions and/or therapeutic targeting. We cross-
referenced the gene expression markers identiﬁed across each tumor
subpopulation for each RMS entity with known cell surface proteins
from the Human Protein Atlas. We identiﬁed several cell surface mar-
kers, including CD44 for Progenitor, ERBB3 for Differentiated, and
L1CAM for Neuronal cells (Supplementary Data 8).
Mapping shared cell heterogeneity between RMS and human
skeletal muscle development
Human skeletal myogenesis proceeds in three de ﬁned waves33. First,
mesodermal progenitors (MPs) from the somite create embryonic
myoblasts (MBs) and myocytes (MCs) that drive early skeletal muscle
deposition. A second wave of muscle development occurs coincident
with the transition of embryonic to fetal development, where both MP
and bipotent skeletal muscle mesenchymal progenitor (SkM.Mesen)
cells likely drive muscle formation
33,34. Finally, a third wave of muscle
growth is regulated by classically de ﬁned muscle stem cells called
satellite cells that expand during early postnatal growth to create
muscle and then become a reserve stem cell population later in life to
aid in repair after injury
35– 37. Here, we took advantage of cell annota-
tions from normal human myogenic development to compare RMS
cells/nuclei to these established myogenic cell states
33 (Fig. S5A, B).
We used transfer learning with SingleR, a computational frame-
work that takes a dataset with known labels as an input and then
transfers them onto a test dataset based on similarity to the
reference
38. We show that FN-RMS tumor cells shared similarity with a
variety of developing human muscle cell types including skeletal
mesenchymal cells (SkM.Mesen), myogenic progenitors (MPs), myo-
blasts (MBs), and myocytes (MCs) (Fig.4D, E and S5D; Supplementary
Data 9). In particular, FN-Progenitor cells preferentially mapped to
SkM.Mesen cells and expressed high levels of marker genes of this
developmental subpopulation (OGN, THY1, POSTN)( F i g .4Ea n dS 5 C ) .
FN-RMS have shared cell states with those found in the second wave of
muscle development that starts at week >7 (Fig. S5D). Of note, the
number of SkM.Mesen cells peak at 12 – 14 weeks of development,
where they comprise 23.5% of the fetal myogenic cells (Fig. S5B).
Similarly, we measured 15.7% of cells/nuclei within FN-RMS mapped to
SkM.Mesen cells (Fig. 4E and Supplementary Data 9). This contrasts
with FP-RMS that largely lack cell state similarity with SkM.Mesen cells.
These results are also in keeping with the identiﬁcation of differences
in gene expression between progenitor cell populations from FP-RMS
and FN-RMS (Fig. S3B). PAX3::FOXO1 and PAX7::FOXO1 FP-RMS shared
cell state similarity with MBs, MCs and/or myoblasts-myocytes (MB-
MCs), with only a minority of cells mapping to MPs, and few to no cells
sharing similarity with SkM.Mesen cells (Fig. 4E and S5C; Supplemen-
tary Data 9). Finally, RMS do not contain appreciable numbers of cells
with shared similarity to postnatal satellite cells and do not map to the
third wave of muscle development (Fig. 4E and S5D; Supplementary
Data 9). Based on these ﬁndings, we propose a reﬁned nomenclature
based on shared developmental similarity (or not) with human muscle
development: “FN-skeletal muscle mesenchymal-like” (FN-SkM.Mes-
like) for FN-RMS Progenitor cell states; and “FP-progenitor” and “FP-
neuronal” for cells that represent tumor-acquired cell states in FP-RMS.
Identiﬁcation of therapy-resistant cells states in RMS
Treatment recurrence is a major hurdle to achieving durable long-term
treatment responses in RMS, and we reasoned that RMS cell states
might also deﬁne therapy persistent tumor cells. In an effort to identify
single-cell signatures that correlate with therapy resistance or tumor
recurrence, we compared snRNA-seq datasets from patient FN-RMS
samples obtained before therapy ( n = 4) or amidst therapy ( n =7 )
(Fig. S6A). We observed an enrichment for the Progenitor score and a
commensurate reduction in the Diffe rentiated score within treated
samples. This observation was particularly pronounced in a pair
of samples obtained from the same patient before therapy
(SJRHB00026_R2) and amidst therapy (SJRHB00026_R3) (Fig. 5A).
Interestingly, the difference was still detectable, though less exag-
gerated, in orthotopic PDXs gene rated from those patient samples
(SJRHB00026_X1 and _X2; Fig. 5B). Likewise, PDCs generated from
another patient obtained before and after therapy (eRMS-8.1, -8.2, and
-8.3) showed a similar pattern with a persistent increase in FN-
SkM.Mes-like progenitor expression scores (Fig. S6B).
Our observation of cell state shifts within single-cell data from FN-
RMS patient samples led us to evaluate a cohort of matched pairs of
tumor samples from a single-institution clinical trial, which were
obtained from patients who had received a diagnostic biopsy followed
by a mid-treatment delayed resection. While a prior study had repor-
ted an enrichment for MEOX2 immunopositivity during therapy within
these samples
24, we performed RNA-sequencing from ﬁxed clinical
samples and applied RMS signatures for the three dominant cell states
(Fig. 5C, n =9 , [n =7 F N - R M S ,n = 2 FP-RMS]). In the FN-RMS samples,
we detected a signi ﬁcant increase in progenitor scores within the
treated patient samples compared to samples from the primary diag-
nostic biopsy (p = 0.026; Wilcoxon signed rank test) and a decrease in
proliferative scores ( p = 0.023; Wilcoxon signed rank test; Fig. 5D).
Collectively, these ﬁndings demonstrate a treatment-induced selec-
tion for the progenitor state in FN-RMS.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 6

A
D
5
10
Neur.
Absent
45
Absent
FP-Progenitor
Differentiated
Ground
Neuronal
ProliferativeProliferative
FN-Progenitor IFN
Differentiated
Ground
Ground
Proliferative
FP-Progenitor
Apoptosis
Differentiated
Neuronal
56
Neur.
Absent
UMAP_RPCA_1
UMAP_RPCA_2
Nr. of samples 
with neuronal
Nr. of samples 
with neuronal
Nr. of samples 
with neuronal
B
FN-RMS
(n = 66,697 cells/nuclei; n = 45 samples)
FP-RMS (PAX7::FOXO1)
(n = 16,500 cells/nuclei; n = 11 samples)
FP-RMS (PAX3::FOXO1)
(n = 22,526 cells/nuclei; n = 15 samples)
FP−RMS (PAX3::FOXO1)FN−RMS
Myogenic 
progenitors
Myoblast−
myocytes
Myoblasts
Myocytes
Skeletal 
mesenchymal
Postnatal 
satellite cells
FN-
Progenitor
Proliferative
Ground
Differentiated
IFN
FP−RMS (PAX7::FOXO1)
Myogenic 
progenitors
Myoblast−
myocytes
Myoblasts
Myocytes
Skeletal 
mesenchymal
Postnatal 
satellite cells
FP-
Progenitor
Proliferative
Ground
Differentiated
Neuronal
Myogenic 
progenitors
Myoblast−
myocytes
Myoblasts
Myocytes
Skeletal 
mesenchymal
Postnatal 
satellite cells
FP-
Progenitor
Proliferative
Ground
Differentiated
Neuronal
Apoptosis
E
100 μm
SJRHB010468_X1
(FP-RMS)
SJRHB013758_X1
(FN-RMS)
H&E Myogenin
(Differentiated)
Synaptophysin
(Neuronal)
100 μm
100 μm
100 μm 100 μm
100 μm
C
FP-RMS 
(PAX3::FOXO1)
FP-RMS 
(PAX7::FOXO1)FN-RMS
0%
25%
50%
75%
100%
20696
21202
29806
eRMS−1.1
eRMS−1.2
eRMS−2.1
eRMS−2.2
eRMS−3.2
eRMS−4
eRMS−8.1
eRMS−8.2
eRMS−8.3
Mast111
Mast139
Mast139_SC
Mast39
Mast85_r1
Mast85_r2
Mast85_r2_SC
MSK74711
RD
SJRHB000026_R2
SJRHB000026_R3
SJRHB000026_X1
SJRHB000026_X2
SJRHB010927_D1
SJRHB010927_X1
SJRHB010928_R1
SJRHB010928_X1
SJRHB011_D
SJRHB011_X
SJRHB012_R
SJRHB012_S
SJRHB012_Y
SJRHB012_Z
SJRHB012405_D1
SJRHB012405_X1
SJRHB013758_D1
SJRHB013758_D2
SJRHB013758_X1
SJRHB013758_X2
SJRHB030680_R1
SJRHB030680_X1
SJRHB049189_D1
SJRHB049189_X1
Mast95
MSK72117
MSK72117_SC
SJRHB010468_D1
SJRHB010468_X1
SJRHB013757_D2
SJRHB013757_X1
SJRHB031320_D1
SJRHB031320_X1
SJRHB046156_A1
SJRHB046156_X1
aRMS−1
aRMS−2
aRMS−3
aRMS−4
aRMS−5
KFR
Mast118
MSK82489
Rh4
Rh41
RMS
SJRHB013759_A1
SJRHB013759_A2
SJRHB013759_X14
SJRHB013759_X15
Percentage
Cell Type
Skeletal mesenchymal
Myogenic Progenitors
Myoblast−Myocytes
Myoblasts
Myocytes
Postnatal satellite cells
02468
0.0
0.5
1.0
1.5
2.0
Neuronal % with scRNA-seq
Synaptophysin expression,
%a r e a
Synaptophysin (SYP )
R2 = 0.89
P = 0.0157
0 5 10 15
0
20
40
60
80
Differentiated % with scRNA-seq
Myogenin expression,
%a r e a
Myogenin (MYOG )
R2 = 0.96
P = 0.0202
Fig. 4 | Subtype analysis reveals shared RMS cell heterogeneity with human
skeletal muscle development and tumor-derived cells states. AUMAP plots of
FN-RMS, PAX7::FOXO1, and PAX3::FOXO1 FP-RMS. Cells/nuclei were integrated
independently and colored based on cell state. The number of samples having≥1%
neuronal cells are shown in the pie charts at the bottom right of each graph.
B Immunohistochemistry staining of O-PDX samples stained for myogenin (MYOG,
marker of the muscle differentiated subpopulation) and synaptophysin (SYP,
marker of the neuronal subpopulation). Staining is representative ofn =4t e s t e d
samples for myogenin and n = 5 tested samples for synaptophysin.C Correlation
between the proportion of neuronal or differentiated cells identiﬁed by sc/snRNA-
seq and immunohistochemistry for synaptophysin and myogenin, respectively
(n =5o r n = 4 FP-RMS PDXs, respectively). The coefﬁcients of determination (R
2)
and P values of the linear regressions are shown. Source data are provided as a
Source Data ﬁle. D Comparison of RMS cell state heterogeneity with cell types
found in human skeletal muscle development as deﬁned by Xi et al. 2020 33.C e l l
types from human skeletal muscle development were projected onto RMS cells
using an unbiased cell-type prediction analysis.E Sankey plots showing the pro-
portion of tumor cells classiﬁed according to their most similar human develop-
mental equivalent from Xi et al. 2020
33 based on unbiased cell-type prediction
analysis.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 7

Due to the rarity of FP-RMS, our matched cohort had few evalu-
able samples (n = 2; Fig. S6C), which limited our ability to investigate
treatment-induced shifts speciﬁcally within FP-RMS. To overcome this
limitation, we performed bulk RNA-sequencing of tissue obtained
from longitudinal biopsies of a FP-RMS orthotopic PDX,
SJRHB013759_X14
24. Xenograft-bearing mice were either treated with
vehicle or with chemotherapy (vincristine+irinotecan), and sedated
needle biopsies were obtained at 5 time points during therapy: day 0
(pre-treatment), day 3, day 7, day 14, and at recurrence (Fig. 5E).
Compared to the vehicle-treated control, tissue obtained from
chemotherapy-treated tumors sh owed upregulation of the differ-
entiated and neuronal signatures at early time points and a return
to basal levels at recurrence (Fig. 5F). Proliferative scores were down-
regulated at early time points and returned to basal levels at
recurrence consistent with the anti-proliferative properties of che-
motherapy (Fig. 5F). We also observed that Progenitor and Differ-
entiated muscle scores showed a trend of enrichment in delayed
resection, whereas Proliferative score was lower in two matched FP-
RMS bulk RNA-sequencing. In total, these studies identify important
cell states that are retained and expanded after therapy in both FN- and
FP-RMS.
Discussion
Single-cell sequencing technologies have provided unprecedented
insight into the intratumoral heterogeneity of a variety of cancers.
However, the application of this technology to rare pediatric cancers
has been limited by tissue availability, cost, and standardization of
bioinformatic analyses. For example, there are approximately 350 new
diagnoses of pediatric RMS in the United States annually
2, which limits
the ability of any one institute to accrue a sizeable cohort of samples.
Here, we combine datasets from three independent studies to deﬁne
distinct tumor cell heterogeneity and malignant cell states shared with
human muscle cells. This consensus analysis also provides a frame-
work for multi-investigator cooperation that we hope will be an
example for future efforts to better understand rare and understudied
tumors. Importantly, this work uncovered unexpected biology
related to transitional and therapy-resistant cells states and challenge
ﬁndings across our and others ’ previous work, which could only be
Fig. 5 | Identiﬁcation of therapy-resistant RMS metaprograms and cells states
in RMS. Metaprogram scores assigned across all cells/nuclei derived from a mat-
ched patient sample collected before (SJRHB000026_R2) and during
(SJRHB000026_R3) treatment (A) or from PDXs derived from those patient sam-
ples (B). Boxplots denote Tukey’s whiskers (25– 75 percentile represented by
minima-maxima; statistical median as center). Two-sided student’s t test with
p values noted in the ﬁgure. C Paired samples obtained from patients who under-
went a pre-treatment biopsy and a delayed resection amidst therapy were pro-
cessed using bulk RNA-sequencing. Created with BioRender.com.D Violin plots
showing metaprogram scores calculated using the RMS-atlas signature gene sets
for 7 matched pairs of FN-RMS samples. Two-sided student’s t test with p values
noted in theﬁgure. E Longitudinal biopsies from mice bearing a FP-RMS orthotopic
PDX, SJRHB013759_X14, which were treated with vehicle or vincristine+irinotecan
(VCR + IRN). Five longitudinal samples were obtained from each mouse, and
samples underwent bulk RNA-sequencing. Created with BioRender.com.
F Metaprogram scores of control treated mouse or those treated with VCR + IRN.
Scores were calculated using signature gene sets from PAX3::FOXO1 FP-RMS
(Supplementary Data 5). Source data are provided as a Source Data ﬁle.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 8

accomplished with a consensus view of our data and cross-institutional
cooperation.
In total, we analyzed 72 samples including 27 FP-RMS, 43 FN-RMS,
and 2 MYOD1 L122R mutant SS-RMS samples. We identi ﬁed shared cell
states across RMS samples, which we named based on expression
similarity shared with human skeletal muscle development including:
(1) progenitor cells that express mesenchymal markers and we now
name “FN-skeletal muscle mesenchymal-like” (FN-SkM.Mes-like) and
“FP-progenitor” cells; (2) differentiated cells that express differ-
entiated muscle-lineage markers; (3) proliferative cells that are enri-
ched for expression of cell cycle genes and largely fail to express
progenitor/mesenchymal genes or differentiated muscle genes; and,
(4) ground state cells that do not show enrichment of any cell state
markers. Our new analysis also identiﬁed previously underappreciated
transitional cell states in both FN- and FP-RMS, suggesting a continuum
of states across RMS. Finally, we identify that a subset of FP-RMS
harbor small numbers of cells that express neuronal genes referred to
as “FP-neuronal” cells, and that these cells are enriched during che-
motherapy. In total, this work provides a standardized nomenclature
for RMS cell subpopulations, introduces a transcriptomic muscle-
lineage score for assessing cell state, provides cell state signature
proﬁles for harmonizing future studies of RMS heterogeneity, and
conﬁrmed the existence of a tumor-acquired neuronal cell state in a
subset of FP-RMS (Fig. 6). While the 72 datasets used to generate this
meta-analysis were exclusively generated from droplet-based 3’-biased
sequencing methods, we demonstrate that our signatures are broadly
applicable to other single-cell sequencing technologies by validating
them against a cohort of 19 samples generated from a plate-based
method, SORT-seq
23. One limitation of the de ﬁned RMS atlas is that
RNA sequencing largely contains 3’enriched sequences and provides
limited full-length gene coverage. Thus, we were unable to map
somatic mutations within individual cells and assess impacts on overall
cell state. We anticipate that new and emerging techniques, such as
long-read sequencing of droplet-based single-cell libraries
39,40 or
combined single-cell DNA/RNA sequencing41,42, will be powerful tools
to simultaneously interrogate clonal heterogeneity and cell state
heterogeneity.
Our cohort included a diversity of datasets generated from
patient tumors, PDXs, primary cultures, and commercially available
cell lines. Consistent with earlier reports
21,22,24,w en o t et h a tP D X s
maintain the underlying heterogeneity of patient tumors. PDXs
expanded and processed at two different institutions present similar
diversity of cell subpopulations (Fig. S1D), indicating that PDXs
represent a reproducible experimental model for studying RMS het-
erogeneity. In contrast, both primary and commercial cell lines were
enriched for the most proliferative compartment of RMS tumors and
were depleted of FP-neuronal cells (Fig. S3C), suggesting that caution
must be applied in using cell lines to model therapy response. The
emergence of 3-dimensional culture models of RMS
23,43,44 may present
ap o t e n t i a l“middle ground” for in vitro models that may more faith-
fully recapitulate the underlying heterogeneity of RMS. Indeed, recent
work from DeMartino et al. indicate that organoids preserve the
malignant cell states of RMS, with absence of non-malignant cells
of the tumor microenvironment
23. Genetically-engineered models
represent an alternate approach to model RMS, and multiple genetic
models of RMS and have been generated in mice and zebraﬁsh
45– 50.I t
r e m a i n sa no p e nq u e s t i o no ft ow h a td e g r e et h e s ee n g i n e e r e dm o d e l s
mimic the heterogeneity of human RMS. We anticipate that the
expression signatures and lineage score generated within this study
will be applicable as a future tool for comparing genetically engineered
models of RMS to that of patient samples.
Our ﬁndings also contribute to a growing body of literature
describing rare cancer cells with the capacity to propagate and
re-establish tumors after therapy, which have sometimes been called
cancer stem cells or tumor-propagating cells
51– 53.W ei d e n t iﬁed a group
of cells expressing a progenitor signature including markers of early
muscle progenitors such as CD44, EGFR,a n d THY1 (CD90). Previous
work using ﬂow sorting for cell surface markers such as CD133, CD44,
and EGFR have validated the existence of these cells in FN-RMS and
demonstrated that they propagate FN-RMS both in vitro and when
grown in immunocompromised mice
21,24,54– 58. Intriguingly,‘Progenitor’
FN-RMS cells shared gene expression similarity to a newly de ﬁned
Skeletal muscle mesenchymal cell state that has bipotent capability to
make muscle and osteogenic lineage cells
33. Based on functional stu-
dies showing that this RMS cell state can drive tumor growth after
stress and has the capacity to make osteogenic lineage cells
21, we have
reﬁned our naming of this cell state as “FN-SkM.Mesen-like”.O u r
analysis also suggested that FN-RMS replicate the broad diversity of
fetal muscle development cell states and have a shared developmental
hierarchy with early developing fetal muscle found after 7 weeks post-
conception. These ﬁndings contrast with Patel et al. which proposed
that FN-RMS recapitulate an earlier mesodermal speciﬁcation program
in mice
24. This difference is likely attributable to interspecies variation
in myogenesis, especially since bipotent SkM.Mesen cells have yet to
On-therapy
(persister cell state)
Primary Tumor
FP-RMS
(PAX3/PAX7::FOXO1)
FN-SkM. Mes-like
Proliferative
Ground
FN-RMS
Relapse
FP-Progenitor*
Proliferative
Ground
FP-Neuronal*
Fig. 6 | Graphical summary.Proposed model of persister cells during treatment that contribute to relapse in FN-RMS (top) and FP-RMS (bottom). Asterisks denote tumor
acquired cells states. Image created with BioRender.com.
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 9

be identiﬁed in mice, or that comparison with human muscle devel-
opment did not include cell types from the earliest stages of meso-
dermal speciﬁcation that begin at 24 days post-conception in humans.
Finally, our data suggests that FN-SkM.Mesen-like cells are largely
quiescent and are likely the therapy persistent cells that re-establish
tumors after treatment. Indeed, a similar phenomenon where cells
with characteristics of progenitors from the hematopoietic, colon, and
brain lineages have been proposed to play roles in leukemia, colorectal
cancer, and glioblastoma, respectively
59– 61.
Our analysis also uncovered that FP-RMS do not display the same
rigid developmental hierarchies as found in normal development and
may contain different therapy persister cell states. For example, FP-
RMS tumors have fewer overall proportions of progenitor cells with
some tumors seemingly lacking this cell state completely. Moreover,
although the FP-progenitor cells do expresses mesenchymal markers,
they are transcriptionally distinct from the SkM.Mesen cells found in
fetal muscle development and the FN-SkM.Mes-like state discovered
here. Indeed, DeMartino et al., also independently identi ﬁed key dif-
ferences in mesenchymal-pathway enriched cell states in comparing
scRNA sequencing expression of FP- and FN-RMS
23. In addition, a
subset of FP-RMS have tumor cells that have neuronal-pathway acti-
vation that are not found in human muscle development and yet are
enriched after chemotherapy. The existence of this FP-RMS cell state is
supported by immunohistochemical studies of 42 FP-RMS tumors that
identiﬁed a subset of FP-RMS express marker genes including chro-
mogranin, CD56, and synaptophysin
62. While RMS have demonstrated
histological resemblance to cells of the myogenic lineage 2,20,63,o u r
work suggests that FP-RMS are able to transition to cell states not
found in normal myogenic development. Intriguingly, lineage plasti-
city and neuroendocrine transdifferentiation have been reported as
resistance mechanisms in multiple adult cancer types, including mel-
anoma and castration-resistant prostate cancer
64– 66. Indeed, earlier
experiments using limiting dilution cell transplantation assays into
immune deﬁcient mice showed that FP-RMS have a high frequency of
tumor initiation, raising the possibility that most if not all FP-RMS cells
can acquire the ability to propagate tumors in vivo
67.T h ef r e q u e n c yb y
which this tumor-acquired cell states are found in FP-RMS and deﬁning
their possible role in driving therapy resistance will clearly be a major
research focus for theﬁeld. Moreover, future work is needed to clarify
the relationship between the myogenic and neuronal cell states, and
the mechanism by which FP-RMS tumors adopt the neuronal state.
In total, our work has de ﬁned cell state heterogeneity in RMS
including identifying a continuum of progenitor and muscle differ-
entiation gene expression, two FP-RMS cell states that are not shared in
muscle development, and subtype speci ﬁc, therapy-persistent cell
states that likely drive tumor regrowth at relapse.
Methods
Human subjects and animal experiments
De-identiﬁed human tumor tissue for this study were obtained and
processed after approval by the St. Jude Institutional Review Board. In
particular, formalin-ﬁxed tissues from diagnostic and on-treatment
RMS tumors were obtained as part of the RMS13 trial at St. Jude Chil-
dren’s Research Hospital (NCT01871766) for the analysis performed in
Fig. 5C, D.
Animal experiments
Frozen needle biopsy tissue from orthotopic patient xenograft tissue
for Fig. 5 were obtained after approval for all procedures and handling
by the St. Jude Institutional Animal Care Use Committee (IACUC).
Biopsied tissue were generated as part of an earlier study24.I m m u n o -
deﬁcient mice were housed according to IACUC standards using bar-
rier conditions and isolation cages to minimize pathogen exposure.
The housing facility operates with an alternating light schedule
(12 h on, 12 h off) and has a dedicated isolated ventilation system. All
mice were fed and provided water ad libitum.
scRNAseq/snRNA analysis
Public datasets. The 10X Genomics scRNAseq/snRNAseq data was
collected from previously published datasets21,22,24,25. All datasets are
available at the NCBI Gene Expression Omnibus (GEO) database under
the following accession numbers: GEO: GSE218974 (Danielli et al.;
n = 17 samples), GEO: GSE195709 (Wei et al.; n = 18 samples), GEO:
GSE174376 (Patel et al.;n = 36 samples), GEO: GSE113660 (Cheng et al.;
n = 1 sample).
Data pre-processing. For samples derived from Wei et al. and Danielli
et al., ﬁltered Seurat objects were downloaded from GEO repositories.
Those objects were generated as previously described
21,22 using the
10X Genomics Cell Ranger pipeline (version 3.0.1 in Danielli et al.;
version 3.1.0 in Wei et al.) to map raw sequencing FASTQ ﬁles to the
human genome reference (hg19 for patient samples, hg38 for primary
c u l t u r e s )o rt ob o t ht h eh u m a nh g 1 9a n dm o u s em m 1 0r e f e r e n c e s( f o r
PDX samples). Low-quality cells, deﬁned as cells with high mitochon-
drial ratio (>15% in Danielli et al., >20% in Wei et al.), low expressed
gene number (<200 in Danielli et al., <1000 in Wei et al.), high
expressed gene number (>8000), and PDX cells potentially derived
from mice (mouse reads ratio >5% in Wei et al.) were already
ﬁltered out.
For samples derived from Patel et al., we generated single-cell
Seurat objects following the original pipeline
24. In short, raw sequen-
cing FASTQ ﬁles available from GEO were aligned to the human hg19
(for patient samples) or to the combined human hg19 and mouse
mm10 references (for PDX samples) using the 10X Genomics Cell
Ranger pipeline (version 3.0.0). Low-quality cells, deﬁned as cells with
high mitochondrial ratio (>10%), low (<400) or high expressed gene
number (>7000), were ﬁltered out.
In their original studies, Wei et al. and Patel et al. both used
inference of copy-number alteration analysis on the patient-derived
datasets to differentiate between malignant cells (i.e., cells/nuclei
harbor tumor-speciﬁc copy-number alterations) and non-malignant
cells. In this study, we included only single-cell/nucleus pro ﬁles that
were annotated as malignant in their respective original papers.
For the cell line Rh41, we downloaded theﬁltered gene-cell matrix
available on GEO, that was generated as previously described
25 using
the 10X Genomics Cell Ranger pipeline (version 2.0.1) to map raw
sequencing FASTQ ﬁles to the human hg38 genome reference. Low-
quality cells, deﬁned as cells with high mitochondrial ratio (>15%), low
(<200) or high expressed gene number (>8000) were ﬁltered out.
Merging of single-cell transcriptome data. To create the RMS atlas,
we ﬁrst subset each sample to typically n = 1500 randomly selected
cells (Supplementary Data 1), and then merged raw count matrices
using Seurat’s merge function. This resulted in a total of n =1 0 7 , 5 2 3
cells from n = 72 RMS samples (Supplementary Data 1).
To create the three subtype-speci ﬁc RMS atlases [(1): FN-RMS
(n = 45 samples); (2): PAX3::FOXO1 FP-RMS ( n =1 5 s a m p l e s ) ; ( 3 ) :
PAX7::FOXO1 FP-RMS ( n = 11 samples)], we merged subtype-speci ﬁc
raw count matrices using Seurat’s merge function.
Normalization and data reduction. After merging, we log-normalized
the data, selected the top 2000 variable features for downstream
analyses, and scaled the gene expression. We then performed principal
component analysis (PCA) and, based on elbow plot, selected the
top n = 15 principal components (PCs) to consider for downstream
analysis. To visualize the cells, we reduced the dimensionality of
the datasets using Uniform Manifold Approximation and Projec-
tion (UMAP).
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 10

Batch correction and clustering. To remove the batch effects from
different samples, we integrated the datasets following Seurat’si n t e -
gration pipeline (https://satijalab.org/seurat/archive/v3.0/integration.
html), which is based on the identi ﬁcation of anchor cells between
pairs of datasets. We ﬁrst normalized and selected n = 2000 variable
features for downstream integration from each dataset. We then
scaled the data and ran PCA on each object. We identi ﬁed anchors
using reciprocal PCA (RPCA), the suggested option for large datasets,
a n di n t e g r a t e dt h ed a t a s e t su s i n gt h eIntegrateDatafunction. We then
scaled and centered the gene expression, performed PCA. Based on
elbow plot, we then selected the number of PCs to retain for down-
stream analyses. We built a K-nearest neighbor (KNN) graph, used the
Louvain algorithm for clustering the cells (resolution of 0.2– 0.3), and
visualized the cells using UMAP plots. The number of identi ﬁed clus-
ters stabilizes at a resolution of around 0.3, yielding a total of 12
clusters. For this reason, we performed our analyses using a resolution
of 0.3. To identify genes that were enriched within each cluster, we
used Seurat’s FindAllMarkers function ﬁltering for genes with fold-
change >log
2(0.25) in the subtype-speciﬁcd a t a s e t sa n d> l o g2(0.3) in
the integrated dataset, and expressed in at least 25% of cells in the
cluster.
Annotation of cell clusters. After clustering, we assigned cell states
based on the expression of known markers and gene set enrichment
analysis
68– 70.S p e c iﬁcally, we used the marker genes of each cluster as
input for Enrichr (https://maayanlab.cloud/Enrichr/)68– 70, and looked at
the GO Biological Process 2023 enriched terms. To annotate and col-
lapse the clusters that contained similar lineages, we used the
expression of known markers and gene set enrichment analysis
68– 70.
For example, clusters 6 and 9 of Fig. 1D both expressed high levels of
the muscle differentiation markers MYOG, MYL4, MYH3 , and were
therefore collapsed into one category (‘Differentiated’); clusters 8 and
1 both expressed high levels of the collagen and extracellular matrix
genes COL3A1, COL1A1, FN1, and were therefore collapsed into one
category (‘Progenitor’).
RMS cell scoring for meta-programs
Cell-state speciﬁc module scoring . To score each cell based on
previously identiﬁed metaprograms, we selected the gene markers of
the original publications as gene inputs (ref. Supplementary Data 4).
We then assigned cell state-speciﬁcm o d u l es c o r e su s i n gt h eAddMo-
duleScoreSeurat’s function. This function works by taking an input set
of genes and comparing their average relative expression to that of a
control set of n =1 0 0g e n e sr a n d o m l ys a m p l e d
71.
To calculate the consensus progenitor, proliferative,a n d differ-
entiated marker gene set, we selected cell state markers that
were enriched in at least two original publications 21,22,24 (Supple-
mentary Data 4), or in one of the original publications and in the
integrated RMS atlas clusters. We then assigned cell state-speci ﬁc
module scores using the AddModuleScore Seurat’s function, as
described above.
To score each RMS cell (i) along a continuum of myogenic dif-
ferentiation, we deﬁned the muscle lineage score(MLSi). We calculated
the MLSi for each cell by subtracting theprogenitor(Pi) score from the
differentiated(Di) score. Unless otherwise speciﬁed, cells were scored
using the new consensus progenitor, proliferative,a n d differentiated
markers. The scores were scaled using theScaleDataSeurat’s function
to center the expression values.
Cell-cycle scoring. After integration, we assigned cell cycle scores
using Seurat ’s CellCycleScoring function, which relies on gene sig-
natures that have been previously shown to characterize S and G2/M
cell cycle phases
71. We distinguished high cycling (S-scores or G2/M
scores >0) from low cycling cells (S-scores <0 and G2/M scores <0)
based on S and G2/M scores.
Comparison of RMS tumors with single-cell reference data from
human development. To infer comparisons between RMS tumors and
human skeletal muscle development, we re-analyzed a scRNAseq
dataset of human skeletal muscle development (GEO: GSE147457)
33.
We downloaded gene expression matrices and their corresponding
metadata information for the myogenic subsets derived from
embryonic development (1), fetal development (2), juvenile (3) and
adult (4) directly from the authors (http://cells.ucsc.edu/?ds=skeletal-
muscle). After merging the raw count matrices of the individual data-
s e t s ,w el o g - n o r m a l i z e dt h ed a t a ,s e l e c t e dt h et o p2 0 0 0v a r i a b l ef e a -
tures for downstream analyses, and scaled the gene expression. We
then performed PCA and, based on elbow plot, selected the topn =1 0
PCs for downstream analysis. To visualize the cells, we reduced the
dimensionality of the datasets using Uniform Manifold Approximation
and Projection (UMAP).
To recognize the cell types and developmental time points at
which RMS tumors might arise, we used SingleR
38, a computational
framework that takes a dataset with known labels as an input and that
transfers them onto a test dataset based on similarity to the reference.
Speciﬁcally, we projected signatures from the human development
dataset
33 onto our combined FN-RMS, PAX3::FOXO1 FP-RMS and
PAX7::FOXO1 FP-RMS single cell objects.
scCODA. Bayesian compositional modeling was used to perform dif-
ferential populations testing using scCODA with default parameters31.
A false discovery rate of 0.05 was used as a cutoff between statistically
credible and non-credible differences.
Bulk RNA-seq
Sample collection. Flash-frozen orthotopic PDX biopsy tissue gener-
ated from ref. 24. underwent RNA isolation using Trizol (Invitrogen)
extraction, as per manufacturer instructions. Samples were manually
homogenized in 800 μl Trizol within microcentrifuge tubes using a
disposable plastic pestle (Fisher Scienti ﬁc). An additional 200 μlo f
chloroform was added and mixed via inverting for 3 min at room
temperature. Samples were then centrifuged at 12,000 xg for 15 min at
4 °C. The aqueous layer was transferred to a new microcentrifuge tube,
and RNA was precipitated by the addition of an equal volume
(approximately 500 μl) of isopropanol and 1 μlg l y c o g e n( T h e r m o
Scientiﬁc). Samples were incubated at room temperature for 10 min,
followed by centrifugation at 12,000 xg for 15 min at 4 °C. Pellets were
washed twice with 75% ethanol and resuspended in nuclease-free
water. RNA quality was estimated using RNA ScreenTape on a TapeS-
tation automated electrophoresis instrument (Agilent). Sequencing
libraries were generated using the TruSeq Total Stranded RNA Library
kit (Illumina) using 250 – 1000 ng of input RNA. Libraries underwent
100 nucleotide paired end sequencing on a NovaSeq 6000 (Illumina).
For extracting RNA from formalin-ﬁxed parafﬁn-embedded (FFPE)
tissue of patient tumors, 5 μm tissue scrolls were processed using the
Maxwell RSC RNA FFPE instrument (Promega). RNA concentration and
quality was determined using a TapeStation automated electrophor-
esis instrument (Agilent). Samples with a DV
200 score (calculated as a
percentage of nucleic acid fragments >200 nucleotides) above 20%
were used for downstream library generation using the SMARTer
Stranded Total RNA – Pico RNA-seq kit v2 (Takara). Libraries were
sequenced using 100 nucleotide paired-end sequencing on a NovaSeq
6000 (Illumina).
Data pre-processing. Following sequencing, all RNA-seq libraries were
processed using an automated computational pipeline. Brie ﬂy,
sequenced reads were trimmed and underwent quality control using
FastQC, followed by aligning and counting using STAR
72. To generate
additional alignment metrics, the STAR-aligned BAMﬁle were analyzed
using the ‘CollectRNASeqMetrics’command from the Picard pipeline.
Duplicate reads were removed using the GATK ‘MarkDupliates’
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 11

command, and then RSEM was used to generate tpm count matrices
using the ‘rsem-calculate-expression’command.
Bulk-RNAseq scoring. To score FFPE tissues and orthotopic PDX
biopsies for the progenitor, proliferative or differentiated scores, we
ﬁrst created a Seurat object using the already TPM-normalized read
count matrix, and log-normalized the count matrix expression
values + 1. We then scored individual samples for the cell state-speciﬁc
module scores using the AddModuleScoreSeurat’s function. We plot-
ted the scores after scaling and centering the expression values using
the ScaleData Seurat’s function.
Immunohistochemistry
Tissues were ﬁxed in 10% neutral buffered formalin, paraf ﬁn embed-
ded, sectioned at 4 μm, and mounted onto glass slides (Superfrost
Plus; 12-550-15, Thermo Fisher Scienti ﬁc, Waltham, MA). Slides were
then dried for 20 min at 60 °C, deparaf ﬁnized, and stained with
hematoxylin and eosin (Richard-Allan Scientiﬁc) or used in immuno-
histochemistry experiments. HE sections were stained and cover-
slipped using the HistoCore SPECTRA Workstation (Lecia Biosystems).
Serial sections were immunolabeled with Synaptophysin (Abcam,
ab32127, 1:400) using a Ventana Discovery Ultra autostainer (Roche,
Indianapolis, IN) and the following conditions: Heat-induced epitope
retrieval, Cell Conditioning Solution ULTRA CC1 (950-224, Roche) for
32 min and visualization with DISCOVERY OmniMap anti-Rb HRP (760-
4311, Roche), Hematoxylin II (790-2208, Roche), and Bluing reagent
(760-2021, Roche). MYOGENIN staining (Abcam, ab1835, 1:150) was
performed on a Ventana Discovery Ultra autostainer (Roche, Indiana-
polis, IN) using the following conditions: Heat-induced epitope
retrieval, Cell Conditioning Solution ULTRA CC2 (950-223, Roche) for
60 min and visualization with DISCOVERY OmniMap anti-Rb HRP (760-
4311, Roche), Hematoxylin II (790-2208, Roche), and Bluing reagent
(760-2021, Roche). Whole slide images to a 20x scalable magniﬁcation
were created using a PANNORAMIC 250 Flash III digital slide scanner
(3DHISTECH Ltd, Budapest, Hungary). Images were taken using the
HALO v3.6.4134.137 software program (Indica Labs) and analyzed
using HALO v3.2.1851.354 and the Area Quanti ﬁcation FL v2.3 algo-
rithm to determine the area of immunoreactivity for each marker (all
Indica Labs, Albuquerque, NM). Visual interpretations of immunohis-
tochemical staining were conducted by a board-certi ﬁed veterinary
pathologist and in a manner that w as blinded to the experimental
condition of each mouse and compared with image analysis ﬁndings.
Statistics and reproducibility
No data were excluded from the analyses. The experiments in this
study were not randomized. All box plots in this study are reported as
using the Tukey method, with bars extending from the 25th to 75
th
percentiles and center bar denoting the statistical median. Relevant
statistical testing for differential expression analyses and two-way
comparison are reported in the text and ﬁgure legend.
Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.
Data availability
Published single-cell/nucleus RNA-sequencing data were obtained
from the Gene Expression Omnibus (GEO): Danielli et al. (GSE218974);
Patel et al. (GSE174376); Wei, et al. (GSE195709); Cheng et al.
(GSE113660). RNA-sequencing data generated from matched patient
samples before and during therapy as well as biopsied FP-RMS
orthotopic PDXs are available at the GEO under accession number
GSE240287 and GSE240308, respectively. The RMS single-cell objects
generated in this study have been uploaded on FigShare [ https://
ﬁgshare.com/projects/RMS_consensus_analysis/194417]. Source data
are provided as a Source Data ﬁle. Source data are provided with
this paper.
Code availability
The code used to generate the results reported in this manuscript are
available through a Github repository [ https://github.com/Sara-
Danielli/RMS-metadata].
References
1. Kashi, V. P., Hatley, M. E. & Galindo, R. L. Probing for a deeper
understanding of rhabdomyosarcoma: insights from com-
plementary model systems.Nat. Rev. Cancer 15,4 2 6– 439 (2015).
2 . S k a p e k ,S .X .e ta l .R h a b d o m y o s a r c o m a .Nat. Rev. Dis. Primers 5,
1( 2 0 1 9 ) .
3. Dasgupta, R., Fuchs, J. & Rodeberg, D. Rhabdomyosarcoma. Semin.
Pediatr. Surg. 25,2 7 6– 283 (2016).
4 . D a v i c i o n i ,E .e ta l .I d e n t iﬁcation of a PAX-FKHR gene expression sig-
nature that deﬁnes molecular classes and determines the prognosis
of alveolar rhabdomyosarcomas.Cancer Res.66, 6936–6946 (2006).
5. Davicioni, E. et al. Molecular classi ﬁcation of rhabdomyosarcoma-
genotypic and phenotypic determinants of diagnosis: a report from
the Children’s Oncology Group.A m .J .P a t h o l .174,5 5 0– 564 (2009).
6. WHO Classi ﬁcation of Tumours Editorial Board. Soft tissue and
bone tumors. Lyon (France): International Agency for Research on
Cancer. WHO classiﬁcation of tumorus series, 5th ed., vol. 3. (2020)
https://publications.iarc.fr/588.
7. Rekhi, B., Upadhyay, P., Ramteke, M. P. & Dutt, A. MYOD1 (L122R)
mutations are associated with spindle cell and sclerosing rhabdo-
myosarcomas with aggressive clinical outcomes.Mod. Pathol. 29,
1532– 1540 (2016).
8. Shern, J. F. et al. Genomic classi ﬁcation and clinical outcome in
rhabdomyosarcoma: a report from an international consortium.J.
Clin. Oncol. 39,2 8 5 9– 2871 (2021).
9. Kohsaka, S. et al. A recurrent neomorphic mutation in MYOD1
deﬁnes a clinically aggressive subset of embryonal rhabdomyo-
sarcoma associated with PI3K-AKT pathway mutations.Nat. Genet.
46,5 9 5– 600 (2014).
10. Agaram, N. P. et al. MYOD1-mutant spindle cell and sclerosing
rhabdomyosarcoma: an aggressive subtype irrespective of age. A
reappraisal for molecular classiﬁcation and risk stratiﬁcation. Mod.
Pathol. 32,2 7– 36 (2019).
11. Alaggio, R. et al. A Molecular study of pediatric spindle and scler-
osing rhabdomyosarcoma: identiﬁcation of novel and recurrent
VGLL2-related fusions in infantile cases.Am. J. Surg. Pathol. 40,
224– 235 (2016).
12. Butel, T. et al. Integrative clinical and biopathology analyses to
understand the clinical heterogeneity of infantile rhabdomyo-
sarcoma: a report from the French MMT committee.Cancer Med.9,
2698– 2709 (2020).
13. Mosquera, J. M. et al. Recurrent NCOA2 gene rearrangements in
congenital/infantile spindle cell rhabdomyosarcoma.Genes Chro-
mosomes Cancer 52,5 3 8– 550 (2013).
14. Mascarenhas, L. et al. Randomized phase II window trial of two
schedules of irinotecan with vincristine in patients withﬁrst relapse
or progression of rhabdomyosarcoma: a report from the Children’s
Oncology Group. J. Clin. Oncol. 28, 4658– 4663 (2010).
15. Pappo, A. S. et al. Survival after relapse in children and adolescents
with rhabdomyosarcoma: a report from the Intergroup Rhabdo-
myosarcoma Study Group.J. Clin. Oncol. 17,3 4 8 7– 3493 (1999).
16. Smith, L. M. et al. Which patients with microscopic disease and
rhabdomyosarcoma experience relapse after therapy? A report
from the soft tissue sarcoma committee of the children’s oncology
group. J. Clin. Oncol. 19,4 0 5 8– 4064 (2001).
17. Chisholm, J. C. et al. Prognostic factors after relapse in nonmeta-
static rhabdomyosarcoma: a nomogram to better deﬁne patients
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 12

who can be salvaged with further therapy. J. Clin. Oncol. 29,
1319– 1325 (2011).
18. Grobner, S. N. et al. The landscape of genomic alterations across
childhood cancers.Nature 555,3 2 1– 327 (2018).
19. Chen, L. et al. Clonality and evolutionary history of rhabdomyo-
sarcoma. PLoS Genet. 11, e1005075 (2015).
20. Chen, X. et al. Targeting oxidative stress in embryonal rhabdo-
myosarcoma.Cancer Cell 24,7 1 0– 724 (2013).
21. Wei, Y. et al. Single-cell analysis and functional characterization
uncover the stem cell hierarchies and developmental origins of
rhabdomyosarcoma.Nat. Cancer 3, 961– 975 (2022).
22. Danielli, S. G. et al. Single-cell pro ﬁling of alveolar rhabdomyo-
sarcoma reveals RAS pathway inhibitors as cell-fateh i j a c k e r sw i t h
therapeutic relevance.Sci. Adv. 9, eade9238 (2023).
23. DeMartino, J. et al. Single-cell transcriptomics reveals immune
suppression and cell states predictive of patient outcomes in
rhabdomyosarcoma.Nat. Commun. 14,3 0 7 4( 2 0 2 3 ) .
24. Patel, A. G. et al. The myogenesis program drives clonal selection
and drug resistance in rhabdomyosarcoma.Dev. Cell. https://doi.
org/10.1016/j.devcel.2022.04.003(2022).
25. Cheng, C. et al. Latent cellular analysis robustly reveals subtle
diversity in large-scale single-cell RNA-seq data.Nucleic Acids Res.
47, e143 (2019).
26. Stewart, E. et al. Orthotopic patient-derived xenografts of paediatric
solid tumours. Nature 549,9 6– 100 (2017).
27. Neftel, C. et al. An integrative mo del of cellular states, plasticity,
and genetics for glioblastoma.Cell 178,8 3 5– 849.e821 (2019).
28. Wu, S. Z. et al. A single-cell and spatially resolved atlas of human
breast cancers. Nat. Genet. 53,1 3 3 4– 1347 (2021).
29. Izar, B. et al. A single -cell landscape of high-grade serous ovarian
cancer. Nat. Med. 26,1 2 7 1– 1279 (2020).
30. Hao, Y. et al. Integrated analysis of multimodal single-cell data.Cell
184,3 5 7 3– 3587.e3529 (2021).
31. Buttner, M., Ostner, J., Muller, C. L., Theis, F. J. & Schubert, B.
scCODA is a Bayesian model for compositional single-cell data
analysis. Nat. Commun. 12, 6876 (2021).
32. Gryder, B. E. et al. Miswired enha ncer logic drives a cancer of the
muscle lineage. iScience 23,1 0 1 1 0 3( 2 0 2 0 ) .
33. Xi, H. et al. A human skeletal muscle atlas identiﬁes the trajectories
of stem and progenitor cells across development and from human
pluripotent stem cells.Cell Stem Cell 27,1 8 1– 185 (2020).
34. Castiglioni, A. et al. Isolation of progenitors that exhibit myogenic/
osteogenic bipotency in vitro byﬂuorescence-activated cell sorting
from human fetal muscle. Stem Cell Rep. 2,9 2– 106 (2014).
35. Chal, J. & Pourquie, O. Making muscle: skeletal myogenesis in vivo
and in vitro. Development144,2 1 0 4– 2122 (2017).
36. Bentzinger, C. F., Wang, Y. X. & Rudnicki, M. A. Building muscle:
molecular regulation of myogenesis.Cold Spring Harb Perspect.
Biol. 4. https://doi.org/10.1101/cshperspect.a008342(2012).
3 7 . S h i ,X .&G a r r y ,D .J .M u s c l es t e mcells in development, regenera-
tion, and disease. Genes Dev. 20,1 6 9 2– 1708 (2006).
38. Aran, D. et al. Reference-based analysis of lung single-cell
sequencing reveals a transitional proﬁbrotic macrophage.Nat.
Immunol. 20,1 6 3– 172 (2019).
39. Penter, L. et al. Integrative genotyping of cancer and immune
phenotypes by long-read sequencing.Nat. Commun.15,3 2( 2 0 2 4 ) .
40. Al ’Khafaji, A. M. et al. High-throughput RNA isoform sequencing
using programmed cDNA concatenation.Nat. Biotechnol. https://
doi.org/10.1038/s41587-023-01815-7(2023).
41. Macaulay, I. C. et al. G&T-seq: p arallel sequencing of single-cell
genomes and transcriptomes.Nat. Methods 12,5 1 9– 522 (2015).
4 2 . Z a c h a r i a d i s ,V . ,C h e n g ,H . ,A n d r e w s ,N .&E n g e ,M .Ah i g h l ys c a l a b l e
method for joint whole-genome sequencing and gene-expression
proﬁling of single cells. Mol Cell 80,5 4 1– 553.e545 (2020).
43. Savary, C. et al. Fusion-negative rhabdomyosarcoma 3D organoids
to predict effective drug combinations: a proof-of-concept on cell
death inducers. Cell Rep. Med. 4
, 101339 (2023).
44. Meister, M. T. et al. Mesenchymal tumor organoid models recapitulate
rhabdomyosarcoma subtypes.EMBO Mol. Med.14, e16001 (2022).
45. Searcy, M. B. et al. PAX3-FOXO1 dictates myogenic reprogramming
and rhabdomyosarcoma identity in endothelial progenitors.Nat.
Commun. 14, 7291 (2023).
46. Drummond, C. J. et al. Hedgehog pathway drives fusion-negative
rhabdomyosarcoma initiated from non-myogenic endothelial pro-
genitors. Cancer Cell 33,1 0 8– 124.e105 (2018).
47. Nakahata, K. et al. K-Ras and p53 mouse model with molecular
characteristics of human rhabdomyosarcoma and translational
applications.Dis. Model Mech. 15 https://doi.org/10.1242/dmm.
049004 (2022).
48. Nishijo, K. et al. Credentialing a preclinical mouse model of alveolar
rhabdomyosarcoma.Cancer Res. 69,2 9 0 2– 2911 (2009).
4 9 . K e n d a l l ,G .C .e ta l .P A X 3 - F O X O 1t r a n s g e n i cz e b r aﬁsh models
identify HES3 as a mediator of rhabdomyosarcoma tumorigenesis.
Elife 7 https://doi.org/10.7554/eLife.33800(2018).
50. Yan, C. et al. Visualizing eng rafted human cancer and therapy
responses in immunodeﬁcient Zebraﬁsh. Cell 177,
1903– 1914.e1914 (2019).
51. Genadry, K. C., Pietrobono, S., Rota, R. & Linardic, C. M. Soft
tissue sarcoma cancer stem cells: an overview.Front. Oncol. 8,
475 (2018).
52. Dela Cruz, F. S. Cancer stem cells in pediatric sarcomas. Front.
Oncol. 3, 168 (2013).
53. Hettmer, S. & Wagers, A. J. Muscling in: Uncovering the origins of
rhabdomyosarcoma.Nat. Med. 16,1 7 1– 173 (2010).
54. Walter, D. et al. CD133 positi ve embryonal rhabdomyosarcoma
stem-like cell population is enriched in rhabdospheres.PLoS ONE
6, e19506 (2011).
55. Blum, J. M. et al. Distinct and overlapping sarcoma subtypes initi-
ated from muscle stem and progenitor cells.Cell Rep. 5,
933– 940 (2013).
56. Radzikowska, J. et al. Cancer stem cell markers in rhabdomyo-
sarcoma in children. Diagnostics12 https://doi.org/10.3390/
diagnostics12081895(2022).
57. Linardic, C. M., Downie, D. L., Qualman, S., Bentley, R. C. & Counter,
C. M. Genetic modeling of human rhabdomyosarcoma.Cancer Res.
65, 4490–
4495 (2005).
58. Ignatius, M. S. et al. In vivo imaging of tumor-propagating cells,
regional tumor heterogeneity,and dynamic cell movements in
embryonal rhabdomyosarcoma.Cancer Cell 21,6 8 0– 693 (2012).
5 9 . S i n g h ,S .K .e ta l .I d e n t iﬁcation of human brain tumour initiating
cells. Nature 432,3 9 6– 401 (2004).
60. Ricci-Vitiani, L. et al. Identi ﬁcation and expansion of human colon-
cancer-initiating cells.Nature 445, 111– 115 (2007).
61. Lapidot, T. et al. A cell initiat ing human acute myeloid leukaemia
after transplantation into SCID mice.Nature 367,6 4 5– 648 (1994).
6 2 . B a h r a m i ,A . ,G o w n ,A .M . ,B a i r d ,G .S . ,H i c k s ,M .J .&F o l p e ,A .L .
Aberrant expression of epithelial and neuroendocrine markers in
alveolar rhabdomyosarcoma: a potentially serious diagnostic pit-
fall. Mod. Pathol. 21,7 9 5– 806 (2008).
63. Kahn, H. J. et al. Immunohistochemical and electron microscopic
assessment of childhood rhabdomyosarcoma. Increased fre-
quency of diagnosis over routine histologic methods.Cancer 51,
1897– 1903 (1983).
64. Zou, M. et al. Transdifferentiation as a mechanism of treatment
resistance in a mouse model of castration-resistant prostate cancer.
Cancer Discov. 7,7 3 6– 749 (2017).
65. Rambow, F. et al. Toward minimal residual disease-directed therapy
in melanoma. Cell 174,8 4 3– 855.e819 (2018).
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 13

66. Davies, A., Zoubeidi, A., Beltran, H. & Selth, L. A. The transcriptional
and epigenetic landscape of cancer cell lineage plasticity.Cancer
Discov. 13,1 7 7 1– 1788 (2023).
67. Generali, M. et al. High frequency of tumor propagating cells in
fusion-positive rhabdomyosarcoma.Genes 12 https://doi.org/10.
3390/genes12091373(2021).
68. Kuleshov, M. V. et al. Enrichr: a comprehensive gene set enrichment
analysis web server 2016 update.Nucleic Acids Res. 44,
W90– W97 (2016).
69. Chen, E. Y. et al. Enrichr: interactive and collaborative HTML5 gene
list enrichment analysis tool.BMC Bioinform. 14, 128 (2013).
7 0 . X i e ,Z .e ta l .G e n es e tk n o w ledge discovery with enrichr.Curr.
Protoc. 1,e 9 0( 2 0 2 1 ) .
71. Tirosh, I. et al. Dissecting the multicellular ecosystem of metastatic
melanoma by single-cell RNA-seq.Science 352,1 8 9– 196 (2016).
72. Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner.Bioinform.
29,1 5– 21 (2013).
Acknowledgements
This work was funded by the Sarcoma Foundation of America (2022 SFA
13-22, B.W.S. and S.G.D.), the Hyundai Hope on Wheels Foundation
(A.G.P.), the Damon Runyon Cancer Foundation (#DRSG-33P-20, A.G.P.).
the Alex’s Lemonade Stand Foundation (M.A.D. and A.G.P.), CureSearch
(D.M.L.), American Lebanese Syrian Associated Charities (M.A.D. and
A.G.P.), the Friends of TJ and Summer’s Way Foundation (Y.W.), MGH
ECOR Medical Discovery Award (Y.W.), the Rally Foundation (D.M.L.),
Inﬁnite Love for Kids Fighting Cancer (D.M.L.), and the NCI
K99CA278696 (Y.W.), R01CA276116 (D.M.L.), R01CA269213 (D.M.L.),
R01CA226926 (D.M.L), U54CA231630 (D.M.L.), the Childhood Cancer
Research Foundation Switzerland(B.W.S.), and the V-foundation
(D.M.L.). We thank the St. Jude Clinical Biomarkers Laboratory for
assistance with RNA extraction of formalin-ﬁxed parafﬁn embedded
tissues, the St. Jude Comparative Pathology Core for assistance with
immunohistochemical staining of samples, the St. Jude Hartwell Center
for Biotechnology for sequencing support, and the St. Jude Center for
Applied Bioinformatics for support with RNA-sequencing analysis. Sev-
eral ﬁgures were created with BioRender.com (Figs.1A, 5C, E and 6).
Author contributions
D.M.L., A.G.P., M.W., and B.W.S supervised the study design and writing.
S.G.D. performed the analysis and generatedﬁgures. S.G.D. and Y. W.
coordinated the collaboration,provided feedback on ideas andﬁgures,
and wrote the manuscript. M.A.D. and E.S. provided samples for the
analysis of treatment-induced expression signatures. H.S. supervised
immunohistochemical staining andperformed analysis of histolo-
gic data.
Competing interests
The authors declare no competing interests.
Additional information
Supplementary informationThe online version contains
supplementary material available at
https://doi.org/10.1038/s41467-024-50527-2.
Correspondenceand requests for materials should be addressed to
Marco Wachtel, Beat W. Schäfer, Anand G. Patel or David M. Langenau.
Peer review informationNature Communicationsthanks the anon-
ymous, reviewer(s) for their contribution to the peer review of this work.
Ap e e rr e v i e wﬁle is available.
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
This is a U.S. Government work and not under copyright protection in the
US; foreign copyright protection may apply 2024
Article https://doi.org/10.1038/s41467-024-50527-2
Nature Communications|         (2024) 15:6307 14