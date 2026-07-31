---
reference_id: DOI:10.1371/journal.pone.0302753
title: "Identification of potential biomarkers of leprosy: A study based on GEO datasets"
authors:
- Qun Zhou
- Ping Shi
- Wei dong Shi
- Jun Gao
- Yi chen Wu
- Jing Wan
- Li li Yan
- Yi Zheng
journal: PLOS ONE
year: '2024'
doi: 10.1371/journal.pone.0302753
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0302753&type=printable"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1371_journal.pone.0302753.pdf
---

# Identification of potential biomarkers of leprosy: A study based on GEO datasets
**Authors:** Qun Zhou, Ping Shi, Wei dong Shi, Jun Gao, Yi chen Wu, Jing Wan, Li li Yan, Yi Zheng
**Journal:** PLOS ONE (2024)
**DOI:** [10.1371/journal.pone.0302753](https://doi.org/10.1371/journal.pone.0302753)

## Content

Leprosy has a high rate of cripplehood and lacks available early effective diagnosis methods for prevention and treatment, thus novel effective molecule markers are urgently required. In this study, we conducted bioinformatics analysis with leprosy and normal samples acquired from the GEO database(GSE84893, GSE74481, GSE17763, GSE16844 and GSE443). Through WGCNA analysis, 85 hub genes were screened(GS > 0.7 and MM > 0.8). Through DEG analysis, 82 up-regulated and 3 down-regulated genes were screened(|Log2FC| > 3 and FDR < 0.05). Then 49 intersection genes were considered as crucial and subjected to GO annotation, KEGG pathway and PPI analysis to determine the biological significance in the pathogenesis of leprosy. Finally, we identified a gene-pathway network, suggesting ITK, CD48, IL2RG, CCR5, FGR, JAK3, STAT1, LCK, PTPRC, CXCR4 can be used as biomarkers and these genes are active in 6 immune system pathways, including Chemokine signaling pathway, Th1 and Th2 cell differentiation, Th17 cell differentiation, T cell receptor signaling pathway, Natural killer cell mediated cytotoxicity and Leukocyte transendothelial migration. We identified 10 crucial gene markers and related important pathways that acted as essential components in the etiology of leprosy. Our study provides potential targets for diagnostic biomarkers and therapy of leprosy.

RESEA RCH ARTICL E
Identification of potential biomarkers of
leprosy: A study based on GEO datasets
Qun Zhou
ID
, Ping Shi, Wei dong Shi, Jun Gao, Yi chen Wu, Jing Wan, Li li Yan,
Yi Zheng
ID
*
Wuhan Dermatolog y Preven tion Hospital, Wuhan, Hubei, P. R. China
* zheng.yi. 1206@gmai l.com
Abstract
Leprosy has a high rate of cripplehood and lacks available early effective diagnosis methods
for prevention and treatment, thus novel effective molecule markers are urgently required.
In this study, we conducted bioinformatics analysis with leprosy and normal samples
acquired from the GEO database(GSE8489 3, GSE74481, GSE17763, GSE16844 and
GSE443). Through WGCNA analysis, 85 hub genes were screened(GS > 0.7 and MM >
0.8). Through DEG analysis, 82 up-regulated and 3 down-regulated genes were screened(|
Log2FC| > 3 and FDR < 0.05). Then 49 intersection genes were considered as crucial and
subjected to GO annotation, KEGG pathway and PPI analysis to determine the biological
significance in the pathogenesis of leprosy. Finally, we identified a gene-pathw ay network,
suggesting ITK, CD48, IL2RG, CCR5, FGR, JAK3, STAT1, LCK, PTPRC, CXCR4 can be
used as biomarkers and these genes are active in 6 immune system pathways, including
Chemokine signaling pathway, Th1 and Th2 cell differentiation, Th17 cell differentiation, T
cell receptor signaling pathway, Natural killer cell mediated cytotoxicity and Leukocyte trans-
endothelial migration. We identified 10 crucial gene markers and related important pathways
that acted as essential components in the etiology of leprosy. Our study provides potential
targets for diagnostic biomarkers and therapy of leprosy.
Introduction
Leprosy, also known as Hansen’s disease(HD), is a skin-related neglected tropical diseases
caused by Mycobacterium leprae(M. leprae), which mainly impairs skin, eye and peripheral
nerves to produce a spectrum of clinical phenotypes and can even cause irreversible physical
disabilities such as blindness and limb deformities [1, 2]. Even after treatment, patients still
need routine follow-up due to nerve damage caused by inflammation within and around
peripheral nerve [3]. Patients with leprosy, who suffer from not only physical pain, but also
discrimination and low self-esteem, usually lead a poor quality of life [4]. Leprosy has complex
pathogenesis, which is characterized by a prolonged incubation period, insidious onset and
chronic course. Despite the significant achievements of the global campaign of multi-drug
therapy (MDT) over several decades, leprosy transmission is still active in some communities
and new cases continue to emerge worldwide [5]. During 2022, 174,087 new leprosy cases
PLOS ONE
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 1 / 15
a1111111111
a1111111111
a1111111111
a1111111111
a1111111111
OPEN ACCESS
Citation: Zhou Q, Shi P, Shi Wd, Gao J, Wu Yc,
Wan J, et al. (2024) Identification of potential
biomarker s of leprosy: A study based on GEO
datasets. PLoS ONE 19(5): e0302753. https://doi.
org/10.1371 /journal.pone. 0302753
Editor: Anshuman Mishra, Institute of Advance d
Materials, IAAM, SWEDEN
Received: August 17, 2023
Accepted: April 11, 2024
Published: May 13, 2024
Peer Review History: PLOS recognize s the
benefits of transpar ency in the peer review
process; therefore, we enable the publication of
all of the content of peer review and author
response s alongside final, published articles. The
editorial history of this article is available here:
https://doi.o rg/10.1371/jo urnal.pone.0 302753
Copyright: © 2024 Zhou et al. This is an open
access article distributed under the terms of the
Creative Commons Attribution License, which
permits unrestricte d use, distribu tion, and
reproduction in any medium, provided the original
author and source are credited.
Data Availabilit y Statement: All relevant data are
within the paper and its supporting information
files.
Funding: LiLi Yan is supported by Medical
scientific research project of Wuhan Health

were reported globally, represented an increase of 23.8% over that in 2021, adding further to
the concerns is 5.5% grade-2 disability rate of all new cases [6]. Based on the immune status of
the host, according to Ridley-Jopling immunospectral classification, leprosy can be divided
into five categories: tuberculoid (TT), borderline tuberculoid (BT), borderline borderline (BB),
borderline lepromatous (BL), and lepromatous (LL) [7]. Patients can develop various inflam-
matory and pathologic reactions including reversal reaction(RR, also known as R1, i.e. “type 1
reactions”) and erythema nodosum leprosum (ENL, also known as R2, i.e. “type 2 reaction”),
either spontaneously or during therapy [8, 9].
The diverse clinical manifestations and immunopathogenesis of leprosy are strongly associ-
ated with the host’s immune response including both innate and adaptive immunity. The
innate immune mechanisms are key determinants in leading to different clinical manifesta-
tions of leprosy and the initiation of nerve damage. The complement cascade, as a vital compo-
nent of the innate immune system, has been found to be related to increased leprosy
susceptibility [10]. Langerhans cells in leprosy skin lesions express CD1a, which is associated
with reactional episodes in leprosy [11]. Different macrophagic populations in host tissue can
result in different clinical presentations in leprosy and macrophages play key roles in the path-
ogenesis of leprosy [12]. M. leprae can reduce the efficiency of dendritic cells in inducing T-
cell responses and downregulate Schwann cell lineage genes and reactivate developmental
transcription factors, thereby leading to the initiation of neuropathogenesis [13, 14]. The adap-
tive immune system can determine the type of leprosy, lead to a series of pathological lesions
and further aggravate the nerve damage, involving T-helper(Th) cells, regulatory T-cells
(Treg), natural killer T-cells(NKT), memory T-cells(Tmem), cytotoxic T-cells(Tcyt), antibody-
producing plasma cells(CD138), regulatory B-cells(Breg), and memory B-cells (Bmem) [15].
According to previous researches, the course of leprosy is regulated by various complex
immune cells and factors. However, the role of immune genes on leprosy molecular pathogen-
esis and how they interact with each other are largely unknown. Through network analysis,
key genes and their interactions in the pathogenesis of disease can be identified. Therefore, we
explored the immune-related genes and pathways and revealed their complex interaction net-
work, which can help us better understand the pathogenesis of leprosy.
High throughput microarray platforms can be used to detect gene alterations of diseases
and thus discover biomarkers [16]. We provided sufficient samples by integrating multiple
microarray datasets to offer more convincing results. Based on crucial genes that were both
hub genes of WGCNA and differentially expressed genes, we performed a series of analyses
including functional enrichment analysis and protein-protein interaction analysis. Finally, we
identified some new biomarkers and used multipartite networks to reveal the interconnectivity
between them and their involved immune system pathways, providing novel insights that will
help understand the molecular mechanism of this serious disease.
Materials and methods
Microarray data from GEO data repository
Gene Expression Omnibus (GEO), as the largest available public microarray database of
NCBI, was thoroughly searched for all datasets involving studies of leprosy. Data were retained
for further analysis only if they met the following criteria: (1) The study type was limited to
expression profiling by array. (2) The sample was from human skin lesion or normal skin. (3)
Information about the technology and platform of the study was provided. (4) The study was
published publicly and accessible. Finally, microarray datasets GSE84893, GSE74481,
GSE17763, GSE16844 and GSE443 were included in our study, containing 130 samples in total
(121 leprosy samples vs. 9 normal samples). These 121 leprosy samples consisted of 10 TT, 24
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 2 / 15
Commission (grant number WX19D56). The
funders had no role in study design, data collection
and analysis, decision to publish, or preparation of
the manuscript.
Competing interests : The authors have declared
that no competing interests exist.

LL, 10 BB, 10 BL, 25 BT, 21 RR and 21 ENL, which were involved in all disease types of leprosy
so as to avoid generating less reliable results. Details of samples in these datasets that we used
for following analysis are provided in Table 1.
Preprocessing of raw data
The selected five gene expression profiles were merged into one file, and log and baseline
transformation were done, so as to get rid of potential heterogeneity. We then eliminated the
inter-batch differences with R package “sva” [17] and used the default parameters for batch
normalization analysis, resulting that a normalized gene expression profile containing data
from the five different datasets was obtained for WGCNA and DEG analysis. The normalized
gene expression profile can be found in S1 Table.
WGCNA analysis
Weighted Gene Co-expression Network Analysis(WGCNA) was constructed on the normal-
ized gene expression profiles with R package “WGCNA” [18]. Automatic network construc-
tion was carried out with soft-thresholding power as 7, minimum module size as 30 and
dendrogram cut height as 0.25. Genes in the same module often share a higher level of co-
expression. Then we picked out the module which contained genes particularly associated
with leprosy by the correlation between modules and clinical traits. In addition, in order to
screen out the hub genes to leprosy, we calculated gene significance (GS) to measure the corre-
lation between genes and modules and module membership (MM) to measure the correlation
between genes and clinical traits.
DEG analysis
The normalized gene expression profile containing data from the five different datasets was
obtained for DEG(differentially expressed gene) analysis with R package “limma” [19]. We
used the default parameters of limma to perform DEG analysis. Then we used heatmap and
volcano plot to display differentially expressed gene levels. The heatmap and volcano plot were
drawn with R software. To present chromosomal locations of differentially expressed genes,
circus was used [20].
GO annotation and KEGG pathway
To obtain the biological attributes and functional pathways of intersection genes of WGCNA
and DEG analysis, Gene Ontology(GO) and Kyoto Encyclopedia of Genes and Genomes
Table 1. Details of leprosy microarray datasets from GEO database.
GSE Publicati on Platform Classificatio n
GSE84893 JCI Insight Affymetri x Human Genome U133 Plus 2.0 Array ENL:6
GSE74481 Front Genet Agilent-0 28004 SurePrin t G3 Human GE 8x60K Microarra y (Probe Name
Version)
TT:10, BT:10, BB:10, BL:10, LL:4, R1:14, R2:9,
CC:9
GSE17763 Cell Host
Microbe
Affymetri x Human Genome U133 Plus 2.0 Array LL:7, BT:10, RR:7
GSE16844 J Infect Dis Affymetri x Human Genome U133 Plus 2.0 Array ENL:6, LL:7
GSE443 Science Affymetri x Human Genome U95 Version 2 Array LL:6, BT:5
TT, tubercu loid; LL, lepromato us; BB, borderline-b orderline; BL, borderline-l epromatou s; BT, borderline-tu berculoid; ENL, erythema nodosum leprosum, also known
as R2(type 2 reactio n); RR, reversal reaction, also known as R1(typ e 1 reactions); CC, normal sample.
https://do i.org/10.1371/j ournal.pone .0302753.t001
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 3 / 15

(KEGG) pathway enrichment analyses were performed with R package “clusterProfiler” [21].
Significance was set at P < 0.01.
PPI analysis
Protein-protein interaction(PPI) analysis was carried out with the following databases:
STRING [22], BioGrid [23], OmniPath [24], InWeb_IM [25] using Metascape(http://
metascape.org). Molecular Complex Detection (MCODE) algorithm [26] was further applied
to identify densely connected network components if the network contains more than three
proteins.
Results
Workflow
Our workflow of bioinformatics analysis is illustrated in Fig 1. We obtained 4925 genes in
common after preprocessing of raw data downloaded from GEO database. Then we conducted
WGCNA analysis and 85 hub genes were screened with the threshold at GS > 0.7 and
MM > 0.8. Furthermore, after DEG analysis, 85 differential genes were screened with the
threshold at |Log2FC| > 3 and FDR < 0.05, including 82 up-regulated genes and 3 down-regu-
lated genes. The intersection of these two results indicated that 49 genes were crucial and war-
ranted further research. Then these 49 genes were subjected to GO annotations, KEGG
pathways and PPI analysis to determine their biological significance in the pathogenesis of
leprosy.
WGCNA analysis
Soft-thresholding power was seted at 7 to construct a scale-free network using pickSoftThres-
hold function, when the scale independence exceeded 0.9 for the first time(R
2
= 0.906) and
had a relatively high mean connectivity (Fig 2A). We then detected gene modules based on the
TOM matrix with soft-thresholding power as 7. As a result, eight modules were identified. Fig
2B showed the relationships between the identified module genes, indicating that the gene
expression was relatively independent among modules. The blue module had the highest cor-
relation with leprosy (cor = 0.74 and P = 2e-23, Fig 2C and 2D) among the eight modules,
thus we selected the MEblue-grade block for subsequent analysis. The blue module contained
1025 genes, then using GS > 0.7 and MM > 0.8 as cut-off criteria, 85 hub genes were identi-
fied. S2 Table illustrated the detailed information of WGCNA result including gene names
contained in all modules and their GS and MM values.
DEG analysis
We found 82 up-regulated genes and 3 down-regulated genes after DEG analysis (|Log2FC| >
3 and FDR < 0.05, Fig 3A). More information including the fold change and FDR of these 85
genes were shown in S3 Table. Heatmap of these DEGs were demonstrated in Fig 3C. Chro-
mosome location distribution revealed that chromosomes 1 contained the greatest number of
dysregulated genes (Fig 3B). Interestingly, while four genes on the X chromosome showed
dysregulation (SASH3, CYBB, IL2RG and SH2D1A), none Y chromosome gene was affected.
GO annotation and KEGG pathway
There were 49 crucial genes both in result of WGCNA and DEG analysis (S1 Fig). GO annota-
tion and KEGG pathway were then performed to explore the potential biological functions of
these genes. As Fig 4A–4C, the GO annotation results showed that the crucial genes were
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 4 / 15

mainly associated with T cell activation, positive regulation of cell activation and positive regu-
lation of cytokine production regarding the biological process. For cellular component, the
genes were mainly associated with external side of plasma membrane, secretory granule mem-
brane, cytoplasmic side of plasma membrane. For molecular function, the genes were mainly
associated with immune receptor activity, cytokine binding and non-membrane spanning pro-
tein tyrosine kinase activity. The KEGG pathway analysis revealed that the crucial genes were
predominantly enriched in Chemokine signaling pathway, Th1 and Th2 cell differentiation,
Th17 cell differentiation and Natural killer cell mediated cytotoxicity (Fig 4D). The complete
results of GO and KEGG analyses can be found in S4 Table.
Fig 1. Workflow of bioinforma tics analysis.
https://do i.org/10.1371/j ournal.pone .0302753.g00 1
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 5 / 15

Fig 2. WGCNA result. A) Obtaining soft-threshol ding power by analyzing the scale-free fit index and mean
connectivi ty of network topology. B) Heatmap depicts the Topological Overlap Matrix (TOM) of all genes of the
WGCNA network. The darker the color, the higher the overlap. C) Heatma p of module eigengenes and leprosy trait.
D) Heatma p of the correlatio n between module eigengene s and clinical traits. Each row correspond s to a module, and
each column corresponds to a trait. Each square is colored according to the correspond ing correlation and labels
correlatio n and P value.
https://d oi.org/10.1371/j ournal.pon e.0302753.g0 02
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 6 / 15

PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 7 / 15

Fig 3. DEG result. A) Volcano plot of normalized gene expression profile. B) Chromosom e mapping of differen tially
expressed genes. Red color represents up-regulated genes and blue represents down-regulat ed. C) Heatmap of
different ially expressed genes.
https://d oi.org/10.1371/j ournal.pon e.0302753.g0 03
Fig 4. GO annotation and KEGG pathway of crucial genes related to leprosy. A) Bubble plots showing GO annotations regarding biological process(BP ). B)
Bubble plots showing GO annotati ons regarding cellular component (CC). C) Bubble plots showing GO annotati ons regarding and molecular function( MF). D)
Bubble plots showing KEGG pathway .
https://do i.org/10.1371/j ournal.pone .0302753.g00 4
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 8 / 15

PPI analysis
We also conducted PPI analysis with the intersection genes. The results using MCODE algo-
rithm showed that two components were obtained in which genes can closely interact with
each other (Fig 5A). The PPI result and MCODE components can be found in S5 Table. Then
we conducted KEGG enrichment analysis of genes in these components and filtered pathway
of p.adjust < 0.05 to draw network with cytoscape, indicating that these genes involved include
immune system, immune disease and infectious disease pathways (S2 Fig). The whole result of
KEGG enrichment analysis of component genes can be found in S6 Table. Chemokine signal-
ing pathway contained the largest number of associated genes(JAK3, FGR, ITK, CCR5,
STAT1, CXCR4). Next, we filtered the immune system pathways and their related genes. As a
result, six pathways connecting 10 genes were finally identified (Fig 5B).
Discussion
As a global disease caused by M. leprae, the registered prevalence of leprosy has been decreased
substantially from more than 5 million cases in the 1980s to 133,802 cases in 2021. However,
there were still 140,594 new cases reported globally in 2021 [27]. Furthermore, leprosy is still a
poorly understood illness and considering the disability and dysfunction suffered from this
disease, it’s worth striving to study the pathogenesis [28]. Varied manifestations of leprosy are
associated with the host immune responses to M. leprae, involved both innate and acquired
immune responses. Many immune cells play important roles in the pathogenesis of leprosy,
including macrophages, Schwann cells, dendritic cells, lymphocytes, etc [29, 30]. Therefore, in
order to understand the pathogenesis of leprosy, we investigated the immunological pathways
and related crucial genes.
Gene expression profiling based on microarray technique has been widely applied in large-
scale genomic analysis and biomedical research. Moreover, integrating multiple data can
potentially increase statistical power of individual studies [31]. In our present study, we gath-
ered and integrated gene expression profiles from five microarray datasets. Several linkage loci
on chromosome 2p14 [32], 6p21 [33], 6q25–26 [33], 10p13 [34], 17q11–q21 [35], and 20p12
[36] may be associated with leprosy susceptibility. The chromosome mapping of differentially
expressed genes showed that genes were widely distributed on all chromosomes except Y. By
joint analysis of the consolidate data, 49 crucial genes were screened, which both were hub
genes of WGCNA(GS > 0.7 and MM > 0.8) and differentially expressed genes(|Log2FC| > 3
and FDR < 0.05).
We found that these crucial genes were predominantly enriched in T cell activation, posi-
tive regulation of cell activation, external side of plasma membrane, secretory granule mem-
brane, immune receptor activity, cytokine binding, Chemokine signaling pathway, Th1 and
Th2 cell differentiation, Th17 cell differentiation and Natural killer cell mediated cytotoxicity.
The responses of T cells have been proved to be important in determining host immunity and
leading to different leprosy development outcomes [37, 38]. Various regulatory T cells, such as
Treg and natural killer T cells, can adjust the polarized state of T cell immunity, thus control-
ling the clinical manifestation [39]. Tuberculoid leprosy is related to Th1 cytokine response,
while lepromatous leprosy is associated with Th2 cytokine response [40]. Th17 cells may con-
tribute to lesional inflammation by recruiting neutrophils, activating macrophages and
enhancing Th1 effector cells [41, 42]. Cytokines gene polymorphisms play essential roles in
shaping the immune responses in leprosy, which even can drive the conversion between func-
tionally antagonistic cells [43]. M. leprae can prevent activation of the host chemotactic
response by inhibiting chemokine expression and finally escape destruction by the immune
system [44].
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 9 / 15

Fig 5. PPI Analysis of crucial genes related to leprosy. A) Protein-prote in interaction network of two key compone nts identified based on MCODE. Red
color represents MCODE1 genes and blue represents MCODE2 genes. B) The network of immune system pathways and component genes. Oval
box represents gene and square box represents pathway. The wider the pathway frame, the more genes the pathway contains.
https://do i.org/10.1371/j ournal.pone .0302753.g00 5
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 10 / 15

Protein-protein interaction network has displayed the functional connections of crucial
genes. Through MCODE algorithm, we identified two densely connected network components.
Then we conducted KEGG enrichment analysis of these component genes and extracted the
immune system pathways to draw a gene-pathway network, which was composed of 10 genes
(ITK, CD48, IL2RG, CCR5, FGR, JAK3, STAT1, LCK, PTPRC, CXCR4) and 6 immune system
pathways(Chemokine signaling pathway, Th1 and Th2 cell differentiation, Th17 cell differentia-
tion, T cell receptor signaling pathway, Natural killer cell mediated cytotoxicity, Leukocyte
transendothelial migration). Previous studies have proved that these genes play important roles
of immunoregulation. ITK signaling is crucial for humoral responses, B cell functions, T cell
development and Th2 responses [45, 46]. CD48 is involved in a wide variety of innate and adap-
tive immune responses, including T cell activation, autoimmunity, granulocyte activity, NK
function and antimicrobial immunity [47]. IL2RG plays an essential role in T cells and natural
killer (NK) cells production and B cells normal function [48]. CCR5 can regulate IL-2 produc-
tion and promote T cell proliferation [49]. FGR plays a potential role in FCRL4-mediated
immune regulation [50]. JAK/STAT family factors can contain the proliferation of M. leprae by
promoting cell-mediated immunity [51]. LCK can determine the T cell signaling via regulating
the phosphorylation of various signaling molecules and interact with negative regulators CD45
(PTPRC) leadding to T cell hyporesponsiveness in leprosy progression [52]. CXCR4 may drive
the recruitment of lymphocytes to tissue lesions of leprosy patients [53]. Our study had explored
the complex relationship between crucial genes and immune system pathways.
Leprosy is closely related to immune response. Most of the damage to leprosy patients is
secondary to immunological reactions [54]. Immunological techniques can be very useful in
the diagnosis of leprosy, in the follow-up and in detection of relapses [55]. Nutrition status can
affect the progress of leprosy through regulating immune pathways [56]. Although there are
no useful biomarkers in the clinical setting so far, biomarkers can be used to prevent the spread
of leprosy and design interventions to modulate the host’s immune response to M. leprae
infection and prevent damaging immune-mediated pathologies, which is a focus of future
research work [57]. Our study focused on immune markers of leprosy, hoping to be helpful for
the diagnosis and treatment of leprosy.
Conclusion
In summary, we have discovered ten crucial genes(ITK, CD48, IL2RG, CCR5, FGR, JAK3,
STAT1, LCK, PTPRC, CXCR4), which may act as potential targets for diagnostic biomarkers
and therapy of leprosy. Then we found six related important immune system pathways(Che-
mokine signaling pathway, Th1 and Th2 cell differentiation, Th17 cell differentiation, T cell
receptor signaling pathway, Natural killer cell mediated cytotoxicity, Leukocyte transendothe-
lial migration), and constructed a gene-pathway network to revealed their complex interac-
tions. Our work may improve the understanding of immunological molecular mechanisms
underlying the initiation and development of leprosy.
Leprosy still remains endemic within over 140 countries around the world and approxi-
mately 200,000 new cases were reported worldwide in 2017. Additionally, leprosy still faces
many diagnostic and treatment challenges [58]. As an ancient disabling disease closely related
to immunity, we believe that leprosy will eventually be conquered with deeper researches into
the potential immune pathogenesis.
Supporting information
S1 Table. The normalized gene expression profile of five datasets.
(XLSX)
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 11 / 15

S2 Table. The information of WGCNA module genes.
(XLSX)
S3 Table. The information of the 85 differentially expressed genes.
(XLSX)
S4 Table. GO and KEGG analysis results.
(XLSX)
S5 Table. Protein-protein interaction network and MCODE components identified in the
gene lists.
(XLSX)
S6 Table. KEGG enrichment analysis of MCODE component genes.
(XLSX)
S1 Fig. Venn of crucial genes in result of WGCNA and DEG analysis.
(TIF)
S2 Fig. Network of component genes and pathways involved in these genes. Oval
box represents gene and square box represents pathway. Red color represents MCODE1 genes
and blue represents MCODE2 genes. The wider the pathway frame, the more genes the path-
way contains.
(TIF)
S1 Graphical abstract.
(TIF)
S1 File.
(R)
Acknowledgmen ts
We are extremely grateful to all the authors for their hard work to this research.
Author Contributions
Data curation: Qun Zhou.
Software: Qun Zhou.
Visualization: Qun Zhou.
Writing – original draft: Qun Zhou, Ping Shi, Wei dong Shi, Jun Gao, Yi chen Wu, Jing Wan,
Li li Yan.
Writing – review & editing: Yi Zheng.
References
1. Han XY, Silva FJ. On the age of leprosy. PLoS Negl Trop Dis. 2014; 8(2), e2544, https://doi.or g/10.
1371/journa l.pntd.00 02544 PMID: 245512 48.
2. Graham A, Furlong S, Margole s LM, et al. Clinical Managemen t of Leprosy Reactions . Infectious Dis-
eases in Clinical Practice. 2010; 18(4), 235–23 8, https://doi.or g/10.109 7/ipc.0b013 e3181deba2a .
3. Pearson JM. The evaluation of nerve damage in leprosy. Lepr Rev. 1982; 53(2), 119–130, https:// doi.
org/10.5935/ 0305-7518.1 9820015 PMID: 7098751.
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 12 / 15

4. Makhakhe L. Leprosy review. S Afr Fam Pract(2004) . 2021; 63(1), e1–e6, https://d oi.org/10.410 2/safp.
v63i1.531 1 PMID: 34797098
5. Avanzi C, Singh P, Truman RW, et al. Molecular epidemi ology of leprosy: An update. Infect Genet Evol.
2020; 86, 104581 , https://doi.or g/10.101 6/j.meegid. 2020.104581 PMID: 330224 27.
6. World Health Organizatio n. Global leprosy (Hansen disease) update, 2022: new paradigm–c ontrol to
eliminatio n [J]. Wkly. epidemi ol. rec, 2023: 409–429. https://www .who.int/pub lications- detail-redi rect/
who-wer98 37-409-43 0.
7. Ridley DS, Jopling WH. Classifica tion of leprosy according to immunity . A five-group system. Int J Lepr
Other Mycobac t Dis. 1966; 34(3), 255–273 PMID: 595034 7.
8. Andrade PR, Pinheiro RO, Sales AM, et al. Type 1 reaction in leprosy: a model for a better understa nd-
ing of tissue immunity under an immunopa thological condition . Expert Rev Clin Immunol. 2015; 11(3),
391–407, https:// doi.org/10.15 86/1744 666X.2015.10 12501 PMID: 25666357.
9. Voorend CG, Post EB. A systematic review on the epidemi ological data of erythema nodosum lepro-
sum, a type 2 leprosy reaction . PLoS Negl Trop Dis. 2013; 7(10), e2440, https://doi.or g/10.137 1/
journal.pntd .000244 0 PMID: 24098819.
10. Kretzschm ar GC, Oliveira LC, Nisihara RM, et al. Complement receptor 1 (CR1, CD35) association with
susceptibility to leprosy. PLoS Negl Trop Dis. 2018; 12(8), e00067 05, https://doi.or g/10.1371 /journal.
pntd.000 6705 PMID: 30092084.
11. Miranda A, Amadeu TP, Schuele r G, et al. Increased Langer hans cell accumu lation after mycobac terial
stimuli. Histopatholo gy. 2007; 51(5), 649–656, https:// doi.org/10.11 11/j.136 5-2559.2007 .02848.x
PMID: 179275 86.
12. Pinheiro RO, Schmitz V, Silva BJA, et al. Innate Immune Responses in Leprosy. Front Immunol. 2018;
9, 518, https:// doi.org/10.33 89/fimmu. 2018.00518 PMID: 296438 52.
13. Hashimo to K, Maeda Y, Kimura H, et al. Mycobacterium leprae infection in monocy te-derived dendritic
cells and its influence on antigen-pr esenting function. Infect Immun. 2002; 70(9), 5167–5176, https://
doi.org/10.11 28/IAI.70.9. 5167-5176.2 002 PMID: 121835 67.
14. Masaki T, McGlinche y A, Cholewa-Wa claw J, et al. Innate immune response precede s Mycobac terium
leprae-ind uced reprogramm ing of adult Schwann cells. Cell Reprogr am. 2014; 16(1), 9–17, https://doi.
org/10.1089/ cell.2013.0064 PMID: 24279882
15. van Hooij A, Geluk A. In search of biomarke rs for leprosy by unraveling the host immune response to
Mycobac terium leprae. Immunol Rev. 2021; 301(1):175 –192. https://doi.or g/10.111 1/imr.129 66 PMID:
33709405.
16. Loffredo LF, Abdala-Va lencia H, Anekalla KR, et al. Beyond epithelial-to -mesench ymal transitio n: Com-
mon suppressio n of differentiation program s underlies epithelial barrier dysfunction in mild, moderate,
and severe asthma. Allergy. 2017; 72(12):198 8–2004 . https://doi.or g/10.111 1/all.13222 PMID:
28599074.
17. Leek JT, Johnson WE, Parker HS, et al. The sva package for removing batch effects and other
unwanted variation in high-throu ghput experiments . Bioinformat ics. 2012; 28(6):882– 883. https://doi.
org/10.1093/ bioinformatic s/bts034 PMID: 22257669
18. Langfelder P, Horvath S. WGCN A: an R package for weighted correlation network analysis. Bmc Bioin-
formatics. 2008; 9(1):559. https://doi.or g/10.118 6/1471-2105 -9-559 PMID: 19114008.
19. Ritchie ME, Belinda P, Wu D, et al. limma powers differential expression analyses for RNA-sequen cing
and microarray studies. Nucleic acids research. 2015; 43(7):e47. https://doi.or g/10.109 3/nar/gkv00 7
PMID: 256057 92.
20. Krzywinsk i M, Schein J, Birol I, et al. Circos: An informati on aesthetic for comparati ve genomics .
Genome Resea rch. 2009; 19:1639 –1645. https://doi.or g/10.110 1/gr.092759.1 09 PMID: 19541911.
21. Yu G, Wang L G, Han Y, et al. clusterPr ofiler: an R package for comparin g biological themes among
gene clusters. Omics-a Journal of Integrative Biology . 2012; 16(5):284– 287. https://do i.org/10.1089 /
omi.2011 .0118 PMID: 224554 63.
22. Szklarczy k D, Gable AL, Lyon D, et al. STRING v11: protein-pr otein association networks with
increased coverage, supporting functional discovery in genome- wide experime ntal datasets. Nucleic
Acids Res. 2019; 47:D607–6 13. https://doi. org/10.1093/n ar/gky113 1 PMID: 304762 43.
23. Stark C, Breitkreutz BJ, Reguly T, et al. BioGRID: a general repository for interacti on datasets. Nucleic
Acids Res. 2006; 34:D535–5 39. https://doi. org/10.1093/n ar/gkj10 9 PMID: 16381927.
24. Tu ¨ rei D, Korcsma ´ ros T, Saez-Rod riguez J. OmniPath: guidelines and gateway for literature- curated sig-
naling pathway resource s. Nat Methods. 2016; 13(12):966 –967. https://doi.or g/10.103 8/nmeth.40 77
PMID: 278980 60.
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 13 / 15

25. Li T, Werners son R, Hansen RB, et al. A scored human protein-pr otein interactio n network to catalyze
genomic interpretatio n. Nat Methods. 2017; 14:61–64. https://doi.o rg/10.1038/nm eth.4083 PMID:
27892958.
26. Bader GD, Hogue CW. An automated method for finding molecular complexes in large protein interac-
tion networks . BMC bioinformatic s. 2003; 4:2. https://doi.or g/10.1186 /1471-2105- 4-2 PMID: 12525261.
27. Global leprosy (Hansen disease) update, 2021: moving towards interruption of transmission. World
Health Organizatio n. 2022; 36:429– 450. https://www .who.int/pub lications/i/i tem/who -wer9736-42 9-
450.
28. White C, Franco- Paredes C. Leprosy in the 21st century. Clin Microbiol Rev. 2015; 28(1):80–9 4.
https://doi.or g/10.112 8/CMR.000 79-13 PMID: 25567223.
29. Nath I, Saini C, Valluri VL. Immuno logy of leprosy and diagnostic challenges . Clin Dermatol. 2015; 33
(1):90–98. https://doi.o rg/10.1016/j.c lindermatol.20 14.07.00 5 PMID: 25432814.
30. Fonseca AB, Simon MD, Cazzaniga RA, et al. The influen ce of innate and adaptati ve immune
response s on the differe ntial clinical outcomes of leprosy. Infect Dis Poverty. 2017; 6(1):5. https://d oi.
org/10.1186/ s40249-016- 0229-3 PMID: 2816209 2
31. Ma T, Liang F, Oester reich S, et al. A Joint Bayesian Model for Integrating Microarray and RNA
Sequenc ing Transcrip tomic Data. J Comp ut Biol. 2017; 24(7):647– 662. https://do i.org/10.1089 /cmb.
2017.0056 PMID: 28541721.
32. Yang Q, Liu H, Low HQ, et al. Chromosom e 2p14 is linked to susceptibility to leprosy. PLoS One. 2012;
7(1):e2974 7. https://do i.org/10.1371 /journal.pon e.00297 47 PMID: 22238647.
33. Mira MT, Alcaïs A, Van Thuc N, et al. Chromosom e 6q25 is linked to susceptibility to leprosy in a Viet-
namese population. Nat Genet. 2003; 33(3):412– 415. https://doi.or g/10.103 8/ng1096 PMID:
12577057.
34. Siddiqui MR, Meisner S, Tosh K, et al. A major susceptibility locus for leprosy in India maps to chromo-
some 10p13. Nat Genet. 2001; 27(4):439– 441. https://doi.or g/10.103 8/86958 PMID: 11279529 .
35. Jamieson SE, Miller EN, Black GF, et al. Evidence for a cluster of genes on chromosom e 17q11-q21
controlling suscep tibility to tubercul osis and leprosy in Brazilians. Genes Immun. 2004; 5(1):46–57 .
https://doi.or g/10.103 8/sj.gene.6 364029 PMID: 147351 49.
36. Tosh K, Meisner S, Siddiqui MR, et al. A region of chromosome 20 is linked to leprosy susceptibility in a
South Indian popula tion. J Infect Dis. 2002; 186(8):119 0–1193 . https://doi.or g/10.1086 /343806 PMID:
12355375.
37. Ottenhoff TH, Elferink DG, Klatser PR, et al. Cloned suppressor T cells from a leproma tous leprosy
patient suppress Mycoba cterium leprae reactive helper T cells. Nature. 1986; 322(6078) :462–464 .
https://doi.or g/10.103 8/322462a0 PMID: 2426597
38. Modlin RL, Mehra V, Wong L, et al. Suppres sor T lymphocy tes from lepromatous leprosy skin lesions. J
Immunol. 1986; 137(9):283 1–2834 PMID: 2944966.
39. Sadhu S, Mitra DK. Emerging Conce pts of Adaptive Immunity in Leprosy. Front Immun ol. 2018; 9:604.
https://doi.or g/10.338 9/fimmu.2018 .00604 PMID: 29686668.
40. Modlin RL. Learning from leprosy: insights into contemp orary immunolog y from an ancient disease.
Skin Pharma col Appl Skin Physiol. 2002; 15(1):1–6. https://doi. org/10.1159/0 0005817 7 PMID:
11803252.
41. Saini C, Siddiqui A, Rame sh V, et al. Leprosy Reactions Show Increased Th17 Cell Activity and
Reduced FOXP3+ Tregs with Concomit ant Decrease in TGF-β and Increase in IL-6. PLoS Negl Trop
Dis. 2016; 10(4):e000 4592. https://doi.or g/10.1371/ journal.pntd .0004592 PMID: 27035913.
42. Bettelli E, Korn T, Oukka M, et al. Induction and effector functions of T(H)17 cells. Nature. 2008; 453
(7198):105 1–1057. https:// doi.org/10.10 38/natur e07036 PMID: 18563156.
43. Mi Z, Liu H, Zhang F. Advances in the Immun ology and Genetic s of Leprosy. Front Immunol. 2020;
11:567. https:/ /doi.org/10.33 89/fimmu .2020.00567 PMID: 323731 10.
44. Guerreiro LT, Robottom-F erreira AB, Ribeiro-Alv es M, et al. Gene expression profiling specifies chemo-
kine, mitoch ondrial and lipid metabolism signatures in leprosy. PLoS One. 2013; 8(6):e6474 8. https://
doi.org/10.13 71/journal.p one.0064748 PMID: 23798993
45. Liao XC, Littman DR. Altered T cell receptor signalin g and disrupted T cell developme nt in mice lacking
Itk. Immunity. 1995; 3:757–769. https:// doi.org/10.10 16/1074 -7613(95)90065 -9 PMID: 8777721.
46. Andreotti AH, Schwartzber g PL, Joseph RE, et al. T-cell signaling regulat ed by the Tec family kinase,
Itk. Cold Spring Harb Perspect Biol. 2010; 2(7):a002 287. https://doi.or g/10.110 1/cshperspe ct.a00228 7
PMID: 205193 42.
47. McArdel SL, Terhorst C, Sharpe AH. Roles of CD48 in regulating immunity and tolerance. Clin Immun ol.
2016; 164:10– 20. https://doi.or g/10.101 6/j.clim.2016 .01.008 PMID: 26794910.
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 14 / 15

48. Melsen JE, van Ostaijen-Ten Dam MM, van den Akker EB, et al. T and NK Cells in IL2RG-Defi cient
Patient 50 Years After Hema topoietic Stem Cell Transpla ntation. J Clin Immunol. 2022; 42(6):1205 –
1222. https://d oi.org/10.100 7/s10875 -022-0127 9-5 PMID: 35527320.
49. Camargo JF, Quinones MP, Mummidi S, et al. CCR5 expression levels influence NFAT translocati on,
IL-2 production , and subsequen t signaling events during T lymphoc yte activation. J Immunol. 2009;
182(1):171 –182. https:// doi.org/10.40 49/jimmuno l.182.1.1 71 PMID: 1910914 8.
50. Liu Y, Bezverbn aya K, Zhao T, et al. Involvem ent of the HCK and FGR src-family kinases in FCRL4-
mediated immune regulation. J Immuno l. 2015; 194(12):58 51–5860. https:// doi.org/10.40 49/jimmuno l.
1401533 PMID: 25972488.
51. Silva LM, Hirai KE, de Sousa JR, et al. Immunohist ochemical analysis of the expression of cellular tran-
scription NFκB (p65), AP-1 (c-Fos and c-Jun), and JAK/STA T in leprosy. Hum Pathol. 2015; 46
(5):746–75 2. https://do i.org/10.1016 /j.humpath.2 015.01.0 15 PMID: 2577190 2.
52. Kumar S, Naqvi RA, Khanna N, et al. Disruption of HLA-DR raft, deregulatio ns of Lck-ZAP-70- Cbl-b
cross-talk and miR181a towards T cell hyporesp onsiveness in leprosy. Mol Immun ol. 2011; 48(9–
10):1178–11 90. https://doi.or g/10.1016/ j.molimm.2011 .02.012 PMID: 21453975.
53. Mendonc ¸ a VA, Alvim de Melo GE, Arau ´ jo MG, et al. Expressio n of the chemokine receptor CXCR4 on
lymphocy tes of leprosy patients. Braz J Med Biol Res. 2011; 44(12):125 6–1260. https:// doi.org/10.
1590/s01 00-879x20110 075001 31 PMID: 22002092.
54. Naafs B. Current views on reactions in leprosy. Indian J Lepr. 2000; 72:97–1 22. PMID: 10935190 .
55. Chin-a-Lien RA, Faber WR, van Rens MM, et al. Follow-up of multibacill ary leprosy patients using a
phenolic glycolipid -I-based ELISA. Do increasin g ELISA-valu es after discontinu ation of treatment indi-
cate relapse? Lepr Rev. 1992; 63(1):21–7 . https:// doi.org/10.59 35/0305 -7518.19920 004 PMID:
1569812.
56. Dwivedi VP, Banerjee A, Das I, et al. Diet and nutrition: An important risk factor in leprosy. Microb
Pathog. 2019; 137:103714. https://d oi.org/10.101 6/j.micpath. 2019.103714 PMID: 314935 02.
57. Antas PRZ, Santos DO. Editorial: The Role of Biomar kers in the Immun opathology and Diagnosis of
Immune Exacerba tions in Leprosy- New Frontiers to Manage This Neglected Disease . Front Med (Lau-
sanne). 2022; 9:878781. https://d oi.org/10.338 9/fmed.202 2.87878 1 PMID: 35402438.
58. Maymone MBC, Laughter M, Venkatesh S, et al. Leprosy: Clinical aspects and diagnostic techniques . J
Am Acad Dermatol. 2020;1–14. https://doi.or g/10.1016/ j.jaad.2019.12 .080 PMID: 32229279.
PLOS ONE
Crucial genes and functional network feature s of leprosy
PLOS ONE | https://doi.or g/10.137 1/journal.po ne.03027 53 May 13, 2024 15 / 15