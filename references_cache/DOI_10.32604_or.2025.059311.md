---
reference_id: DOI:10.32604/or.2025.059311
title: Multimodal omics analysis of the EGFR signaling pathway in non-small cell lung cancer and emerging therapeutic strategies
authors:
- YUZHENG LI
- LILI YU
- SHIYAO ZHOU
- HUA ZHOU
- QIBIAO WU
journal: Oncology Research
year: '2025'
doi: 10.32604/or.2025.059311
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://cdn.techscience.press/files/or/2025/TSP_OR-33-6/OncolRes-33-06-59311/OncolRes-33-59311.pdf"
oa_status: hybrid
license: cc-by
local_pdf_path: files/DOI_10.32604_or.2025.059311.pdf
---

# Multimodal omics analysis of the EGFR signaling pathway in non-small cell lung cancer and emerging therapeutic strategies
**Authors:** YUZHENG LI, LILI YU, SHIYAO ZHOU, HUA ZHOU, QIBIAO WU
**Journal:** Oncology Research (2025)
**DOI:** [10.32604/or.2025.059311](https://doi.org/10.32604/or.2025.059311)

## Content

Multimodal omics analysis of the EGFR signaling pathway in
non-small cell lung cancer and emerging therapeutic strategies
YUZHENG LI1,2;L ILI YU1;S HIYAO ZHOU1;H UA ZHOU2,3,*;Q IBIAO WU1,2,*
1 Faculty of Chinese Medicine, State Key Laboratory of Quality Research in Chinese Medicine, and University Hospital, Macau University of Science and
Technology, Macao, 999078, China
2 Chinese Medicine Guangdong Laboratory (Hengqin Laboratory), Guangdong-Macao In-Depth Cooperation Zone in Hengqin, Zhuhai, 519000, China
3 State Key Laboratory of Traditional Chinese Medicine Syndrome, Guangdong Provincial Hospital of Chinese Medicine, Guangdong Provincial Academy o f
Chinese Medical Sciences, The Second Af ﬁliated Hospital of Guangzhou University of Chinese Medicine, Guangzhou, 510006, China
Key words: Cancer therapy, Epidermal growth factor receptor (EGFR), Multiomics technologies, Non-small cell lung cancer (NSCLC), Targeted therapies
Abstract: Background: Non-small cell lung cancer (NSCLC) involves complex alterations in the epidermal growth factor
receptor (EGFR) signaling pathway. This study aims to integrate multimodal omics analyses to evaluate and enhance EGFR-
targeted therapies. Methods: We reviewed and synthesized omics data—including genomics, transcriptomics, proteomics,
epigenomics, and metabolomics data—related to the EGFR pathway in NSCLC, examined the clinical outcomes of current
therapies and proposed new treatment strategies.Results: Integrated omics analyses revealed the multifaceted role of EGFR
in NSCLC. Transcriptomic analysis revealed gene expression alterations due to EGFR mutations, with upregulation of
oncogenes and downregulation of tumor suppressors. Proteomics revealed complex interactions within the EGFR
network, revealing cross-talk with other receptors. Epigenomics highlighted the impact of DNA methylation and histone
modiﬁcations on EGFR and its downstream genes, whereas metabolomics demonstrated shifts in metabolic patterns
essential for tumor growth. Conclusion: This study highlights the critical role of multimodal omics in understanding
the molecular landscape of NSCLC, offering insights into more effective, personalized therapies. Future advancements in
omic technologies and analysis are expected to signi ﬁcantly enhance NSCLC diagnosis and treatment.
Abbreviation
EGFR Epidermal Growth Factor Receptor
TKI Tyrosine Kinase Inhibitor
PFS Progression-Free Survival
MET Mesenchymal-Epithelial Transition
GATK Genome Analysis Toolkit
ANNOVAR ANNOtate VARiation
STAR Spliced Transcripts Alignment to a Reference
LC-MS Liquid Chromatography-Mass Spectrometry
GC-MS Gas Chromatography-Mass Spectrometry
ctDNA Circulating Tumor DNA
HER2 Human Epidermal Growth Factor Receptor 2
AXL AXL Receptor Tyrosine Kinase
CNVs Copy Number Variations
EMT Epithelial‒Mesenchymal Transition
RNA-seq RNA Sequencing
lncRNAs Long Noncoding RNAs
miRNAs MicroRNAs
2-DG 2-deoxyglucose
scRNA-seq Single-cell RNA Sequencing
scDNA-seq Single-cell DNA Sequencing
CITE-seq Cellular Indexing of Transcriptomes and Epi-
topes by Sequencing
MRD Minimal Residual Disease
CT Computed Tomography
PET-CT Positron Emission Tomography-Computed
Tomography
NGS Next-Generation Sequencing
PCR Polymerase Chain Reaction
Introduction
Non-small cell lung cancer (NSCLC) accounts for
approximately 85% of all lung cancer diagnoses [ 1]. Despite
advancements in traditional therapies, the prognosis for
*Address correspondence to: Hua Zhou, gutcmzhs@hotmail.com;
Qibiao Wu, qbwu@must.edu.mo/totoro4321@163.com
Received: 03 October 2024; Accepted: 20 December 2024;
Published: 29 May 2025
ONCOLOGY RESEARCH echT PressScience
2025 33(6): 1363-1376
REVIEW
Doi: 10.32604/or.2025.059311 www.techscience.com/journal/or
Copyright © 2025 The Authors. Published by Tech Science Press.
This work is licensed under a Creative Commons Attribution 4.0 International License, which permits unrestricted
use, distribution, and reproduction in any medium, provided the original work is properly cited.

patients with advanced NSCLC remains poor, primarily due
to the heterogeneity of the tumors [ 2]. Targeted therapies
against epidermal growth factor receptor (EGFR) have
substantially improved outcomes for patients harboring
EGFR mutations [ 3]. Signi ﬁcant progress in this ﬁeld was
demonstrated by the FLAURA2 trial in 2023, which
conﬁrmed the ef ﬁcacy of osimertinib, a third-generation
EGFR tyrosine kinase inhibitor (TKI), in combination with
chemotherapy, achieving a progression-free survival (PFS)
of 25.5 months in patients with advanced EGFR-mutant
NSCLC [ 4]. In early 2024, ﬁndings from the MARIPOSA
study further supported the effectiveness and safety of
combining amivantamab with lazertinib in this patient
cohort [ 5].
Recent trials have investigated the synergistic effects of
combining osimertinib with Mesenchymal-Epithelial
Transition (MET) inhibitors to overcome MET
ampliﬁcation-mediated resistance, a common mechanism
in EGFR-TKI-resistant NSCLC. The TATTON trial and the
ongoing SAVANNAH trial have shown promising results
for osimertinib combined with savolitinib, a selective MET
inhibitor, in patients with MET-driven resistance. Interim
data from the SAVANNAH trial in 2024 demonstrated a
clinically meaningful response rate in patients with
acquired MET ampli ﬁcation, suggesting this combination as
a potential strategy for overcoming MET-related resistance
[6,7]. Other trials, such as the ORCHARD trial, are
evaluating osimertinib-based combination therapies tailored
to the molecular pro ﬁle of resistance in NSCLC patients [ 8].
However, the bene ﬁts of targeted therapies are not
universal, with some patients developing acquired resistance
[9]. To address this challenge, we employ a comprehensive
array of advanced bioinformatics tools and machine
learning algorithms to integrate and analyze multimodal
omics data, including genomics, transcriptomics,
proteomics, epigenomics, and metabolomics. By applying
these sophisticated technologies, we systematically identify
key molecular drivers and resistance mechanisms in
NSCLC, thereby guiding the development of targeted
therapeutic strategies [ 10]. Genomic data are processed
using the Genome Analysis Toolkit (GATK) for variant
calling and ANNOtate VARiation (ANNOVAR) for the
annotation of genetic variants critical to NSCLC [ 11,12].
Transcriptomic data are mapped with the Spliced
Transcripts Alignment to a Reference (STAR) aligner and
quantiﬁed using Cuf ﬂinks to identify gene expression
alterations linked to EGFR mutations [ 13,14]. Proteomic
analyses are performed using MaxQuant for peptide
identiﬁcation and quanti ﬁcation, integrated with Perseus for
statistical analysis and data visualization, aiding in the
discovery of protein expression patterns and potential
biomarkers [ 15]. Epigenomic data are analyzed using
Bismark, enhancing our understanding of the epigenetic
landscape shaped by EGFR activity [ 16]. Metabolomic
proﬁling, conducted with MetaboAnalyst alongside Liquid
Chromatography-Mass Spectrometry (LC-MS) and Gas
Chromatography-Mass Spectrometry (GC-MS), identi ﬁes
shifts in metabolite pro ﬁles indicative of the biochemical
activities within NSCLC cells [ 17]. Furthermore, data
integration is facilitated by the Galaxy platform, which
provides a comprehensive framework for data management
and visualization [ 18
]. Predictive models of disease
progression and response to therapy are constructed using
Python-based machine learning algorithms, leveraging
libraries such as scikit-learn [ 19].
This review aims to meticulously summarize the
outcomes of multimodal omics analyses of the EGFR
signaling pathway in NSCLC, assess the ef ﬁcacy and
limitations of existing EGFR-targeted therapies, and discuss
innovative therapeutic strategies based on omics data. These
include the development of new-generation EGFR inhibitors
and combination treatment plans, with a view towards
personalized therapy. Through this comprehensive analysis,
we endeavor to illuminate the molecular mechanisms
underlying NSCLC and contribute to the advancement of
more effective treatment modalities.
The role of the EGFR signaling pathway in non-small cell lung
cancer
EGFR mutations play crucial roles in NSCLC, particularly in
Asian populations. The spectrum of EGFR mutations
primarily includes deletions in exon 19, L858R point
mutations in exon 21, insertions in exon 20, mutations in
exon 18, and some rare mutations. The overall prevalence of
EGFR mutations in Asian populations is approximately
30%–50%, compared to 10% –20% in Western populations.
Deletions in exon 19 and L858R mutations are the most
prevalent, accounting for 80% –90% of cases in Asians.
Younger individuals, particularly women under 40 years in
Asia, exhibit a higher mutation rate. Environmental factors
such as air quality and exposure to carcinogens also
signiﬁcantly in ﬂuence mutation prevalence, underscoring
the need for targeted prevention strategies [ 20].
EGFR mutation prevalence exhibits signi ﬁcant
geographic and ethnic variability [ 21,22]. Notably, East
Asian countries such as China, Japan, and South Korea
report higher mutation rates than those observed in the
West. Research indicates that genetic predispositions,
environmental exposures, and lifestyle choices all contribute
to these disparities. Notably, there are also variations within
Asia: Southeast Asian countries have slightly lower EGFR
mutation rates than East Asian countries do, whereas South
Asian countries fall between East Asian countries and West
Asian countries. Recent studies have also revealed that while
the EGFR mutation rates in Africa and Latin America are
lower than those in Asia, they are still higher than those in
Europe and North America.
Demographic characteristics also play important roles in
the distribution of patients with EGFR mutations [ 23].
Women, nonsmokers, and patients with adenocarcinoma
present higher frequencies of EGFR mutations, a trend
present in all geographic regions but more pronounced in
Asia. Age factors are also signi ﬁcant, with recent research
indicating that younger patients, especially those under 40
years, may have higher rates of EGFR mutations,
particularly young Asian women. In multiethnic countries
such as the USA, Asian Americans have a noticeably higher
frequency of EGFR mutations than other ethnicities do,
further emphasizing the importance of genetic factors in the
prevalence of EGFR mutations.
1364 YUZHENG LI et al.

Aberrant activation of the EGFR signaling pathway leads
to alterations in multiple downstream signaling pathways,
including the RAS-RAF-MEK-ERK pathway, the PI3K-
AKT-mTOR pathway, the STAT signaling pathway, and the
PLCγ-PKC pathway [ 24]. The abnormal activation of these
downstream pathways not only promotes tumor cell
proliferation and survival but is also closely associated with
tumor invasion, metastasis, and angiogenesis. Fig. 1
illustrates the primary downstream pathways activated by
EGFR signaling and their biological effects, including cell
proliferation, survival, and gene transcription. Additionally,
aberrant activation of the EGFR signaling pathway can
affect the tumor microenvironment, such as by promoting
the secretion of angiogenic factors, thereby increasing the
blood supply to the tumor [ 25], or by modulating the
expression of immune-suppressive factors, helping tumor
cells evade immune surveillance [ 26]. A deep understanding
of the complex role of the EGFR signaling pathway in
NSCLC is crucial for developing new treatment strategies
and overcoming drug resistance.
Comprehensive Multimodal Omics Pro ﬁling of the EGFR
Signaling Pathway
Characterization of EGFR mutation spectrum and prevalence
The overall frequency of EGFR mutations in NSCLC ranges
from 10% –35%, with signi ﬁcant variability across different
populations. The most common activating mutations of
EGFR are exon 19 deletions (approximately 45%) and exon
21 L858R point mutations (approximately 40%), both of
which respond well to EGFR-TKI treatment [ 22]. Other
important but less common mutations include exon 18
G719X mutations (approximately 3%), exon 20 insertions
(4%–10%, typically resistant to ﬁrst- and second-generation
EGFR-TKIs), and T790M mutations (primary <5%,
acquired resistance up to 60%) [ 27]. Table 1 summarizes the
distribution of key EGFR mutation types, their frequencies,
and geographic characteristics.
Recent advances in circulating tumor DNA (ctDNA)
analysis have provided a noninvasive method for
dynamically monitoring the EGFR mutation status, especially
the emergence of resistance-related mutations. Studies on the
EGFR mutation spectrum and frequency are crucial for
understanding the molecular pathology of NSCLC, guiding
the selection of targeted therapies, and developing new drugs.
With technological progress, our understanding of the EGFR
mutation spectrum continues to deepen, pushing the
development of precision treatment for NSCLC.
EGFR-associated gene expression patterns
EGFR mutation or activation extensively affects whole-
genome expression in NSCLC. Through large-scale
transcriptomic analyses, researchers have identi ﬁed a series
of gene expression patterns associated with the EGFR
signaling pathway. The activation of EGFR leads to the
upregulated expression of genes that promote cell
proliferation and survival, such as cell cycle-related genes
(CCND1 and CDK4), antiapoptotic genes (BCL2 and
BIRC5), and angiogenesis-related genes (VEGFA and
ANGPT2) [ 28]. Moreover, genes that inhibit tumor growth,
including those that promote apoptosis (BAX and CASP3)
and are related to cell adhesion (CDH1 and ITGB1), are
downregulated [ 29].
FIGURE 1. EGFR signaling pathway and its primary downstream effects.
TABLE 1
Distribution of EGFR mutations
EGFR
mutation type
Frequency Geographic distribution
characteristics
Exon 19
deletion
45% Asian populations: 30% –50%
Exon 21 L858R
point mutation
40% Western populations:
10%–20%
Exon 18
G719X
mutation
3% Less common, but may be more
prevalent in certain populations
Exon 20
insertion
4%–10%
T790M
mutation
Primary <5%
Acquired
resistance up
to 60%
MULTIMODAL OMICS ANALYSIS OF EGFR PATHWAY IN NSCLC AND THERAPEUTIC STRATEGIES 1365

Activation of the EGFR signaling pathway also triggers
feedback regulatory mechanisms, such as the upregulation
of the negative feedback regulators DUSP6 and SPRY2 [ 30].
Moreover, different EGFR mutation types may lead to
slightly varied gene expression pro ﬁles, potentially
explaining their differences in clinical manifestations and
treatment responses. To combat the complexity of resistance
mechanisms in NSCLC, our therapeutic approach includes a
multi-target strategy. This involves targeting not only EGFR
but also other critical nodes within the signaling network,
such as MET, Human Epidermal Growth Factor Receptor
2(HER2), and AXL Receptor Tyrosine Kinase (AXL),
simultaneously. By inhibiting multiple pathways, we aim to
prevent the cancer cells ’ ability to compensate for one
blocked pathway by upregulating another. This strategy is
supported by our omics analysis, which maps the
interactions and redundancies within the cellular signaling
networks, providing a blueprint for targeted multi-pronged
treatment approaches [ 31]. In response to EGFR-TKI
therapy, certain tumor cells may exhibit upregulation of
genes associated with alternative signaling pathways that
bypass EGFR blockade. Notably, MET, HER2, and AXL are
critical in mediating these resistance mechanisms. These
genes encode receptor tyrosine kinases that can activate
parallel pathways, sustaining cell survival and proliferation
despite EGFR inhibition. Detailed discussions on the
interaction dynamics of these proteins and their
contributions to therapeutic resistance are crucial for
understanding resistance patterns and devising effective
combination therapies [ 32]. Activation of the EGFR
pathway also affects the expression and activity of various
transcription factors, such as increasing c-MYC and E2F1
activity, while p53 activity may be inhibited [ 33]. In recent
years, studies have revealed that noncoding RNAs play a
signiﬁcant role in the EGFR signaling pathway. Certain
microRNAs may directly regulate the expression of EGFR,
while some long noncoding RNAs may be involved in
regulating the expression of genes downstream of EGFR [ 34].
EGFR pathway protein interaction network
The EGFR pathway protein interaction network is key to
understanding the mechanisms of EGFR signal
transduction. Through proteomics and interactomics
studies, scientists have constructed a complex and detailed
map of the EGFR signaling network, revealing how EGFR
regulates various biological processes through interactions
with multiple proteins.
The binding of EGFR to its ligands, such as EGF, TGF α,
and HB-EGF, is the starting point of the entire signaling
network, leading to receptor dimerization and
autophosphorylation, thus activating downstream signaling
pathways. Activated EGFR interacts with adaptor proteins
(such as GRB2 and SHC1) and signal transduction
molecules, recruiting downstream effector molecules.
Important downstream effector molecules include PIK3CA
and STAT3, which activate the PI3K-AKT-mTOR pathway
and the STAT signaling pathway, respectively [ 35].
EGFR also undergoes cross-activation with other
receptor tyrosine kinases (such as HER2, MET, and IGF1R),
forming a complex signaling network. At the cellular
membrane level, EGFR interacts with cell adhesion and
cytoskeletal proteins, affecting cell –cell and cell-matrix
adhesion as well as cell migration [ 36]. EGFR mutations
may alter the interaction patterns with certain proteins,
potentially explaining the carcinogenic mechanisms and
resistance of some mutations. During the acquisition of
drug resistance, signi ﬁcant changes in the EGFR signaling
network, such as new interactions caused by MET
ampliﬁcation or AXL activation, occur [ 37].
Recent studies have focused on the dynamics of EGFR
signaling complex formation and dissociation and how its
spatial distribution within cells affects signal strength and
speciﬁcity [ 38]. Moreover, the EGFR pathway is regulated
by multiple negative feedback mechanisms, such as receptor
degradation mediated by the E3 ubiquitin ligase CBL and
dephosphorylation of EGFR by the phosphatase PTPN1 [ 39].
EGFR-related epigenetic modi ﬁcation features
EGFR-related epigenetic modi ﬁcations are crucial for
understanding the regulation of the EGFR gene and the
mechanisms of tumor development and progression. These
modiﬁcations include DNA methylation, histone
modiﬁcations, chromatin remodeling, and noncoding RNA
regulation, all of which play key roles in the regulation of
EGFR gene expression, the activation of signaling pathways,
and the development of resistance.
The DNA methylation status of the EGFR gene promoter
region is closely related to its expression level. Low levels of
methylation are generally associated with increased
expression of EGFR, possibly due to decreased expression or
activity of DNA methyltransferases [ 40]. Histone
modiﬁcations also play a signi ﬁcant role in regulating EGFR
gene expression; active marks such as H3K4me3 and
H3K27ac are generally associated with high gene expression,
whereas repressive marks such as H3K27me3 may lead to
the suppression of expression [ 41].
Chromatin remodeling complexes such as SWI/SNF and
NuRD play roles in regulating the accessibility of the EGFR
gene [ 42]. Noncoding RNAs, particularly miRNAs and
lncRNAs, are also involved in the epigenetic regulation of
EGFR. Certain EGFR mutations may alter related epigenetic
modiﬁcation patterns, affecting gene expression or protein
activity. Dynamic changes in epigenetic modi ﬁcations
during EGFR-TKI treatment may in ﬂuence the development
of resistance. Additionally, the EGFR signaling pathway
itself can reciprocally regulate global epigenetic modi ﬁcation
patterns, affecting changes in the tumor cell phenotype.
EGFR pathway-related metabolic changes
Activation of the EGFR pathway signi ﬁcantly impacts cellular
metabolism, fostering conditions that support rapid tumor
growth and potentially contribute to treatment resistance.
Metabolomic studies have revealed a series of metabolic
changes induced by EGFR pathway activation, providing
important clues for understanding the biology of EGFR-
driven tumors and developing new therapeutic strategies.
EGFR pathway activation signi ﬁcantly enhances
glycolysis, leading to the Warburg effect. This results in
increased glucose uptake and signi ﬁcant lactate production.
The EGFR pathway achieves this effect by upregulating
1366 YUZHENG LI et al.

glucose transporters and activating key glycolytic enzymes
[43]. Glutamine metabolism also changes, with EGFR
signaling increasing the uptake and utilization of glutamine
to support the Tricarboxylic Acid Cycle (TCA) cycle and
biosynthesis. Changes in lipid metabolism are another key
feature, with EGFR signaling promoting de novo fatty acid
synthesis and membrane phospholipid synthesis [ 44].
Amino acid metabolism, particularly that of serine and
branched-chain amino acids, is also affected. Changes in
nucleotide metabolism support rapid cell proliferation.
Alterations in redox balance enhance the antioxidant
capacity of a cell. During EGFR-TKI treatment, tumor cell
metabolic patterns undergo dynamic changes [ 45]. Changes
in the levels of some metabolites may serve as biomarkers
for predicting treatment response. EGFR pathway-related
metabolic changes may also affect the tumor
microenvironment.
Overall, EGFR pathway-related metabolic changes re ﬂect
comprehensive metabolic reprogramming of tumor cells. A
deeper understanding of these changes not only helps
elucidate the biological characteristics of EGFR-driven
tumors but also provides important clues for developing
new diagnostic and therapeutic strategies. With advances in
metabolomics technology and the integration of multiomics
data, we hope to more comprehensively understand the
complex interactions between EGFR signaling and cellular
metabolism, opening new avenues for precision treatment of
NSCLC.
Resistance and Overcoming Resistance Multimodal
Analysis of Resistance Mechanisms
With advances in high-throughput sequencing and
bioinformatics, research into the mechanisms underlying
resistance to EGFR-TKIs has evolved from single-gene
analyses to comprehensive multimodal approaches. This
multidimensional analysis reveals complex resistance
networks and offers valuable insights for overcoming
resistance and developing new therapeutic strategies. The
following sections detail the multimodal analysis of EGFR-
TKI resistance mechanisms across various omics layers,
including genomics, transcriptomics, proteomics,
epigenomics, metabolomics, and single-cell technologies.
Clinical Applications of Multimodal Omics Data in NSCLC
Treatment
The integration of multimodal omics data signi ﬁcantly
impacts clinical decision-making in NSCLC treatment by
enabling physicians to tailor therapies to individual patient
proﬁles. Understanding speci ﬁc genetic mutations and
activated pathways within a patient ’s tumor allows the
selection of the most effective EGFR-TKIs or the
consideration of combination therapies to prevent or
address resistance [ 46]. For instance, patients with exon 19
deletions may respond more favorably to osimertinib,
whereas those with exon 20 insertions, often resistant to
ﬁrst- and second-generation TKIs, may bene ﬁt from
targeted agents like poziotinib or amivantamab, a bispeci ﬁc
antibody targeting both EGFR and MET, which has shown
efﬁcacy in patients with EGFR Exon 20 insertion mutations
[47,48].
Transcriptomic analyses reveal upregulation of survival
pathways, allowing oncologists to incorporate pathway
inhibitors, such as PI3K or mTOR inhibitors, alongside
EGFR-TKIs [ 49]. Proteomic analysis uncovers activation of
bypass pathways, such as MET ampli ﬁcation or HER2
activation, which may prompt the addition of MET or
HER2 inhibitors to EGFR-targeted treatment regimens [ 50].
Epigenomic studies, by identifying DNA methylation
changes, suggest potential bene ﬁts of combining epigenetic
modiﬁers with EGFR-TKIs to restore sensitivity in resistant
tumors [ 51]. Metabolomic pro ﬁling offers predictive
markers, like elevated lactate levels, which can guide
metabolic interventions alongside targeted therapy [ 52].
Beyond therapeutic selection, multimodal omics data
also enhances monitoring of treatment ef ﬁcacy and early
detection of resistance. Circulating tumor DNA (ctDNA)
assays enable dynamic tracking of mutational changes,
allowing timely adjustment of therapeutic strategies when
resistance mutations, such as T790M or C797S, emerge
[53,54]. These omics-driven insights foster a more
personalized, adaptive approach to NSCLC treatment,
optimizing outcomes and prolonging patient survival.
Multimodal Omics Analysis of Resistance Mechanisms
Overcoming resistance to EGFR-TKIs remains a signi ﬁcant
challenge in NSCLC treatment. As our understanding of
resistance mechanisms deepens, various strategies have been
proposed and validated in clinical settings. These include
the development of new-generation TKIs, combination
targeted therapies, integration of immunotherapy, and other
emerging approaches.
Genomics: Beyond the well-known T790M mutation,
new resistance mutations are continuously being discovered.
Whole-genome and whole-exome sequencing technologies
have enabled a comprehensive understanding of genomic
changes associated with resistance. For example, the T790M
mutation increases ATP af ﬁnity, rendering ﬁrst- and
second-generation EGFR-TKIs (such as ge ﬁtinib and
erlotinib) less effective [ 55]. The C797S mutation prevents
covalent binding of osimertinib to EGFR, resulting in third-
generation TKI resistance [ 56].
Additionally, whole-genome sequencing has revealed
complex genomic rearrangements and copy number
variations (CNVs), such as EGFR ampli ﬁcation and MET
ampliﬁcation, which are associated with TKI resistance [ 57].
Notably, the development of liquid biopsy technology allows
for the dynamic monitoring of these genomic changes
through ctDNA, enabling early detection of resistance and
timely intervention.
Transcriptomics: Transcriptomic analysis, primarily
through RNA sequencing (RNA-seq), has revealed the
activation of multiple signaling pathways in resistant cells.
For example, the upregulation of genes associated with
epithelial‒mesenchymal transition (EMT) has been
conﬁrmed in multiple studies to be related to EGFR-TKI
resistance [ 57]. RNA-seq can also detect the formation of
fusion genes, such as the EML4-ALK fusion reported in
MULTIMODAL OMICS ANALYSIS OF EGFR PATHWAY IN NSCLC AND THERAPEUTIC STRATEGIES 1367

some cases of EGFR-TKI resistance [ 58]. Additionally,
changes in the expression of long noncoding RNAs
(lncRNAs) and microRNAs (miRNAs) have been found to
participate in the resistance process. For example, the
upregulation of the lncRNA UCA1 may contribute to
EGFR-TKI resistance by activating the AKT/mTOR
signaling pathway [ 59]. These transcriptomic changes
provide not only new biomarkers of resistance but also a
theoretical basis for combined targeted therapy. Table 2
summarizes the EGFR-associated gene expression changes,
including upregulated and downregulated genes, feedback
regulators, and resistance-related factors that in ﬂuence the
functional impact of EGFR signaling.
Proteomics: Proteomics, particularly phosphoproteomics,
provides key insights into the remodeling of signaling networks
in resistant cells. Proteomics: Proteomics, particularly
phosphoproteomics, provides key insights into the
remodeling of signaling networks in resistant cells. Through
mass spectrometry, researchers have discovered various
bypass activation mechanisms, such as the activation of the
receptor tyrosine kinases MET, AXL, and IGF1R [ 60]. These
ﬁndings directly guide the design of combined targeted
therapy strategies [ 60]. These ﬁndings directly guide the
design of combined targeted therapy strategies. For example,
on the basis of the discovery of MET activation, a treatment
strategy combining an EGFR-TKI with a MET inhibitor is
being evaluated in clinical trials [ 61]. Additionally,
proteomics has revealed several unexpected mechanisms of
resistance, such as changes in the expression of certain cell
adhesion molecules that may affect drug sensitivity [ 62].
Table 3 summarizes the key proteins associated with the
EGFR signaling pathway, their functions, and their
signiﬁcance in NSCLC. This table provides a clear overview
of the complex molecular interactions that contribute to
EGFR activation and resistance.
Epigenomic: Epigenomics studies have shown that
changes in DNA methylation and histone modi ﬁcations play
important roles in EGFR-TKI resistance. Whole-genome
methylation sequencing revealed that the methylation status
of the promoters of certain resistance-related genes changes,
leading to changes in gene expression. For example, high
methylation of the PTEN promoter leading to its
downregulation may impact EGFR-TKI resistance [ 63].
Histone modi ﬁcations, such as acetylation and methylation,
have also been found to be involved in the regulation of
resistance gene expression [ 64]. These ﬁndings provide a
theoretical basis for the application of epigenetic regulators
in overcoming EGFR-TKI resistance.
Metabolomic: Metabolomic analysis highlights the
signiﬁcance of metabolic reprogramming in resistant cells.
For example, multiple studies have shown that glycolysis is
signiﬁcantly increased in EGFR-TKI-resistant cells, which
may be related to the development of resistance [ 65].
Through techniques such as gas chromatography ‒mass
spectrometry (GC ‒MS) and liquid chromatography ‒mass
spectrometry (LC ‒MS), researchers have also discovered
changes in several metabolic pathways, including lipid
metabolism and amino acid metabolism [ 66]. These ﬁndings
provide not only new ideas for resistance mechanisms but
also directions for the development of metabolic targeted
therapy strategies. For example, drugs that target glycolysis,
such as 2-deoxyglucose (2-DG), have shown potential in
preclinical studies to overcome EGFR-TKI resistance [ 67].
Single-Cell Technologies: The application of single-cell
technologies provides unprecedented resolution in
understanding the role of tumor heterogeneity in resistance
evolution. Single-cell RNA sequencing (scRNA-seq) and
single-cell DNA sequencing (scDNA-seq) have revealed the
dynamic changes in different subclones during the
resistance process. For example, research has shown that
under the pressure of EGFR-TKI treatment, a small number
of resistant subclones may rapidly expand, eventually
leading to clinical resistance [ 68]. This understanding of
subclone dynamics provides important evidence for
designing more effective sequential or combined therapy
strategies. Additionally, the development of single-cell
multiomics technologies, such as Cellular Indexing of
Transcriptomes and Epitopes by Sequencing(CITE-seq),
allows us to obtain genomic, transcriptomic, and surface
protein information at the single-cell level, providing a
TABLE 2
EGFR-associated gene expression patterns
Type of gene expression
change
Related genes Functional impact
Upregulated expression CCND1, CDK4, BCL2, BIRC5, VEGFA, ANGPT2 Promotes cell proliferation, anti-apoptosis, and
angiogenesis
Downregulated expression BAX, CASP3, CDH1, ITGB1 Inhibits apoptosis and cell adhesion
Feedback regulation DUSP6, SPRY2 Negative feedback regulation of the EGFR
signaling pathway
Resistance-related MET, HER2, AXL Bypass activation, may lead to resistance to
EGFR-TKIs
Changes in transcription factor
activity
c-MYC, E2F1 (increased activity); p53 (activity may
be inhibited)
Affects downstream gene expression and cell cycle
regulation
Noncoding RNA Speci ﬁc microRNAs and long noncoding RNAs Regulates EGFR expression and downstream gene
expression
1368 YUZHENG LI et al.

powerful tool for comprehensively understanding resistance
mechanisms.
Multimodal Omics Analysis of EGFR Pathway in NSCLC
and Therapeutic Strategies
Understanding the complexity of EGFR-TKI resistance. By
using machine learning and arti ﬁcial intelligence algorithms,
researchers can extract meaningful patterns and associations
from massive amounts of multiomics data. For example,
research integrating genomic, transcriptomic, and proteomic
data has led to the construction of predictive models for
EGFR-TKI resistance, which are important for making
personalized treatment decisions [ 69]. Additionally, the
integration of multiomics data has aided in the discovery of
new potential targets and biomarkers. Table 4 summarizes
the main ﬁndings and signi ﬁcance of multimodal analyses
across genomics, transcriptomics, proteomics, epigenomics,
and metabolomics, highlighting their roles in uncovering
resistance mechanisms and therapeutic targets.
However, multiomics analysis also faces several
challenges. First, the complexity of data integration is an
active research area because of the different characteristics
and scales of data from various omics levels. Second, the
difﬁculty and cost of sample acquisition are practical issues,
especially for longitudinal studies. Furthermore, how to
translate these complex multiomics ﬁndings into clinically
actionable strategies requires further exploration and
validation.
Strategies to overcome resistance
Overcoming resistance to EGFR-TKIs is a signi ﬁcant
challenge in the treatment of non-small cell lung cancer
(NSCLC). With a deeper understanding of resistance
mechanisms, various strategies have been proposed and
validated in clinical settings to counteract resistance. These
strategies include the development of new generation TKIs,
combination targeted therapies, the integration of
immunotherapy, and other emerging approaches. Below,
these strategies and their prospects and challenges in clinical
applications are discussed in detail. Fig. 2 illustrates the
mechanisms of resistance to EGFR-TKI therapy, including
secondary mutations, bypass pathway activation, epigenetic
changes, and metabolic reprogramming, as well as strategies
to overcome resistance, such as combination therapies and
liquid biopsy monitoring. And Table 5 summarizes key
TABLE 3
EGFR-associated gene expression patterns
Category Key proteins Main function/Interaction Signi ﬁcance in NSCLC
Ligands EGF, TGF- α, HB-EGF - Binds to the extracellular domain of
EGFR
- Overexpression leads to persistent
activation
- Activates the EGFR signaling
pathway
- Autocrine loops promote tumor growth
Receptors EGFR, HER2, HER3, HER4 - Forms homodimers or
heterodimers
- Mutations or ampli ﬁcations lead to
abnormal activation
- Activates downstream signaling
pathways
-I n ﬂuences treatment response and
prognosis
Adaptor proteins GRB2, SHC, GAB1 - Links receptors to downstream
effector molecules
- Regulates signal strength and duration
- Promotes signal complex formation - Affects cell proliferation and survival
Downstream
effectors
RAS, RAF, MEK, ERK, PI3K, AKT,
mTOR, STAT3
- Activates multiple signaling
cascades
- Promotes cell proliferation, survival,
and migration
- Regulates gene transcription and
protein synthesis
- Potential therapeutic targets
Negative
regulators
PTEN, DUSP6, SPRY2, CBL - Inhibits signal transduction - Loss of function can lead to
overactivation of signaling
- Promotes receptor internalization
and degradation
-I n ﬂuences treatment resistance
Cross-activation
proteins
MET, IGF1R, FGFR, AXL - Interacts with the EGFR signaling
pathway
- Involved in EGFR-TKI resistance
mechanisms
- Activates overlapping downstream
pathways
- Provides basis for combined targeted
therapy
Nuclear effectors EGFR, STAT3, β-catenin - Translocates to the nucleus - In ﬂuences tumor progression and
metastasis
- Directly regulates gene
transcription
- May be associated with drug tolerance
MULTIMODAL OMICS ANALYSIS OF EGFR PATHWAY IN NSCLC AND THERAPEUTIC STRATEGIES 1369

resistance mechanisms, corresponding overcoming strategies,
speciﬁc drugs, and their potential advantages, providing a
concise overview of targeted interventions for EGFR-TKI
resistance.
The development of new generation TKIs is the most
direct strategy to overcome resistance. The success of the
third-generation EGFR-TKI osimertinib, which effectively
overcomes T790M-mediated resistance, is a prime example.
However, facing new resistance mutations such as C797S,
fourth-generation EGFR-TKIs are under development. For
example, EAI045, an alkylating agent, can covalently bind to
the C797 site of EGFR and has shown potential in
preclinical studies to overcome both the T790M mutation
and the C797S mutation [ 70]. Additionally, dual or
multitarget TKIs, such as poziotinib, which targets EGFR/
HER2, and JNJ-61186372, which targets EGFR/MET, are in
development [ 71]. The development of these novel TKIs
aims not only to overcome known resistance mechanisms
but also to delay the onset of resistance through multitarget
inhibition.
TABLE 4
Multimodal analysis of resistance mechanisms
Omics level Main ﬁndings Signi ﬁcance
Genomics - T790M mutation Identi ﬁcation of new resistance mutations and genomic changes
- C797S mutation
- EGFR/MET ampli ﬁcation
- Genomic rearrangements
Transcriptomics - Upregulation of EMT-related genes Revealing transcriptional regulatory mechanisms related to resistance
- Fusion genes (e.g., EML4-ALK)
- Changes in lncRNA and miRNA expression
Proteomics - Activation of bypass signaling pathways Identi ﬁcation of new therapeutic targets and biomarkers
- Changes in posttranslational modi ﬁcations
Epigenomics - Changes in DNA methylation patterns Unveiling epigenetic mechanisms of resistance
- Histone modi ﬁcation changes
Metabolomics - Enhanced glycolysis Identi ﬁcation of metabolic targets and resistance biomarkers
- Changes in glutamine metabolism
- Reprogramming of lipid metabolism
FIGURE 2. Mechanisms of Resistance to EGFR-TKI Therapy and Strategies for Overcoming Resistance in NSCLC. The ﬂowchart illustrates
the progression from initial EGFR mutation and activation of the EGFR signaling pathway to therapeutic targeting with EGFR-TKIs. However,
various resistance mechanisms may lead to the failure of initial therapy. These resistance mechanisms include (1) the emergence of secondary
resistance mutations (e.g., T790M, C797S), (2) upregulation of bypass signaling pathways (e.g., MET, HER2), (3) epigenetic changes (e.g., DNA
methylation), and (4) metabolic reprogramming. These resistance mechanisms collectively contribute to therapy failure, necessitating
alternative therapeutic strategies. Post-failure interventions include combination therapies, the development of new-generation EGFR-
TKIs, and the use of liquid biopsy monitoring for real-time detection of resistance mutations and treatment adaptation. This multimodal
approach aims to enhance treatment ef ﬁcacy and prolong patient survival in NSCLC.
1370 YUZHENG LI et al.

Combination targeted therapy is another highly regarded
strategy. On the basis of the understanding of bypass activation
mechanisms, various combination regimens are being
evaluated in clinical trials. For example, the combination of
an EGFR-TKI with a MET inhibitor (such as capmatinib)
has shown the expected effects on MET ampli ﬁcation-
mediated resistance [ 62]. The TATTON study evaluated the
effects of osimertinib combined with savolitinib and reported
signiﬁcant antitumor activity in patients with dual-positive
EGFR/MET [ 72]. Another example is the combination of an
EGFR-TKI with an antiangiogenic agent, such as erlotinib
combined with bevacizumab, which showed superior PFS
beneﬁts in the NEJ026 study compared with monotherapy
[73]. These combination strategies aim not only to counter
existing resistance mechanisms but also to delay the
emergence of resistance by simultaneously inhibiting
multiple critical pathways.
The integration of immunotherapy has been a major
breakthrough in the ﬁeld of lung cancer treatment in recent
years, but its application in EGFR-mutant NSCLC still faces
challenges. Although monotherapy with PD-1/PD-L1
inhibitors has limited ef ﬁcacy in these patients, the
combination of immunotherapy with EGFR-TKIs is being
actively explored. For example, the IMpower150 study
revealed that the triplet regimen of atezolizumab combined
with bevacizumab and chemotherapy might improve
survival in patients with EGFR mutations [ 74]. Moreover,
innovative immunotherapeutic strategies, such as bispeci ﬁc
antibodies and CAR-T-cell therapies, are also being
evaluated in EGFR-mutant NSCLC. For example, a
bispeciﬁc antibody targeting EGFR and CD3, AMG 757,
showed promising activity in early clinical trials [ 75].
However, overcoming EGFR-TKI resistance still faces
many challenges. First, the complexity of tumor
heterogeneity and evolution means that a single strategy is
unlikely to completely resolve resistance issues. Second,
multitarget inhibition or combination therapy may increase
toxicity, and balancing ef ﬁcacy with safety is a key issue.
Additionally, some resistance mechanisms, such as small cell
lung cancer transformation, still lack effective targeted
strategies.
Improvements in Multimodal Data Analysis Methods
With the rapid development of high-throughput sequencing
technologies, the generation of multimodal data has far
exceeded our ability to analyze and understand these data.
Therefore, improving multimodal data analysis methods will
be a key direction for future research. First, we need to
develop more ef ﬁcient data integration algorithms to fully
utilize information from genomics, transcriptomics,
proteomics, epigenomics, and other levels. For example,
graph-theoretical approaches could provide new insights for
integrating different types of omics data, allowing the
construction of more comprehensive molecular network
models.
Second, the application of machine learning and deep
learning techniques in multimodal data analysis will further
expand. For example, convolutional neural networks (CNNs)
and recurrent neural networks (RNNs) can be used to
extract spatiotemporal patterns from complex multimodal
data, helping us understand the dynamic processes of EGFR-
TKI resistance. Additionally, transfer learning techniques
may allow us to apply models trained on large-scale public
datasets to smaller clinical datasets, thus improving
prediction accuracy. Another important direction is the
development of more powerful single-cell multimodal
analysis methods. With advancements in single-cell
sequencing technologies, we can obtain multidimensional
information such as genomics, transcriptomics, and
epigenomics at the single-cell level. However, effectively
integrating these high-dimensional, high-noise data remains
a challenge. The development of analysis tools speci ﬁcally for
single-cell multimodal data, such as improved dimensionality
reduction algorithms and trajectory inference methods, will
help us better understand tumor heterogeneity and resistance
evolution.
Finally, visualization and interpretation of multimodal
data also need innovation. The development of intuitive,
interactive visualization tools can help researchers and
clinicians better understand and utilize complex multimodal
data. For example, multidimensional data visualization
systems based on virtual reality (VR) or augmented reality
TABLE 5
Strategies to overcome resistance
Resistance mechanism Overcoming strategy Speci ﬁc methods/
Drugs
Potential advantages
T790M mutation Third-generation
EGFR-TKIs
- Osimertinib - High selectivity for T790M
- Lazertinib - Reduced inhibition of wild-type EGFR
Bypass signaling activation (e.g., MET
ampliﬁcation)
Combination targeted
therapy
- EGFR-TKI + MET
Inhibitor
- Simultaneous inhibition of multiple
signaling pathways
- EGFR-TKI + MEK
Inhibitor
- Prevention of compensatory activation
Epigenetic changes Epigenetic regulators - HDAC inhibitors - Reversal of resistance-related gene
expression
- DNA methylation
inhibitors
- Enhanced drug sensitivity
MULTIMODAL OMICS ANALYSIS OF EGFR PATHWAY IN NSCLC AND THERAPEUTIC STRATEGIES 1371

(AR) technologies might provide new perspectives for
exploring complex biological networks.
Applications of liquid biopsy in the detection of EGFR
mutations
Liquid biopsy technologies, particularly the detection of
circulating tumor DNA (ctDNA), are transforming the
detection and monitoring of EGFR mutations. In the future,
we expect signi ﬁcant improvements in the sensitivity,
speciﬁcity, and range of this technology. For example,
further optimization of digital PCR technology might allow
us to detect lower abundances of EGFR mutations, enabling
ultraearly diagnosis and monitoring of minimal residual
disease (MRD) [ 76]. Additionally, improvements in ctDNA
sequencing technology might allow the detection of multiple
resistance-related mutations in a single liquid biopsy,
providing more comprehensive resistance mechanism
information.
Another important direction is the expansion of liquid
biopsy sample types. In addition to blood, other bodily
ﬂuids, such as urine, cerebrospinal ﬂuid, and pleural
effusion, may also be valuable sources of liquid biopsy. For
example, cerebrospinal ﬂuid ctDNA analysis might provide
more accurate resistance information than blood ctDNA
analysis for patients with central nervous system metastases
after EGFR-TKI treatment [ 77]. The development of
optimized protocols for these different sample types will be
a focus of future research.
The clinical application scenarios for liquid biopsy will
also further expand. In addition to initial diagnosis and
resistance detection, liquid biopsy could play a signi ﬁcant
role in monitoring treatment response, prognosis
assessment, and recurrence prediction. For example, by
dynamically monitoring ctDNA levels and mutation spectra,
we might be able to predict the ef ﬁcacy of EGFR-TKI
treatment early and adjust treatment strategies in a timely
manner [ 78]. Additionally, integrating liquid biopsy with
imaging and other clinical indicators to develop
comprehensive disease monitoring systems will be key to
improving patient management.
Finally, standardization of liquid biopsy data and large-
scale data sharing are crucial. Establishing uniform
standards for liquid biopsy data collection, analysis, and
reporting will facilitate comparisons and meta-analyses
between different studies. Moreover, creating a large-scale
liquid biopsy database and linking it with clinical
information and treatment outcomes will provide valuable
resources for developing more accurate predictive models.
Potential applications of artiﬁcial intelligence in EGFR-targeted
therapy
Artiﬁcial intelligence (AI), especially machine learning and
deep learning technologies, has shown tremendous potential
in various aspects of EGFR-targeted therapy. First, in the
ﬁeld of drug development, AI can accelerate the design and
screening processes for new EGFR-TKIs. For example, deep
learning-based molecular generation models might be able
to design novel inhibitors targeted against speci ﬁc resistance
mutations [ 79]. Additionally, AI-driven virtual screening
technologies might help us identify compounds with anti-
EGFR activity from existing drug libraries, providing new
opportunities for drug repositioning.
In terms of clinical decision support, AI systems could
transform the practice of personalized treatment. By
integrating multidimensional information such as a patient ’s
genomic data, clinical features, imaging data, and treatment
history, AI models might be able to predict individual
patients’ responses to different EGFR-TKIs and their risks of
resistance, thus guiding the selection of optimal treatment
strategies. For example, deep learning-based radiomic
models might be able to extract features related to the EGFR
mutation status and TKI sensitivity from Computed
Tomography (CT) or Positron Emission Tomography-
Computed Tomography (PET-CT) images, assisting in
diagnosis and treatment decisions [ 80]. AI could also offer
valuable insights for optimizing drug combinations and
sequential treatment strategies. By simulating the effects of
different drug combinations and administration sequences
on tumor evolution, AI models might help design treatment
strategies that can maximally delay resistance. Additionally,
reinforcement learning algorithms might be used to develop
adaptable dosing strategies, dynamically adjusting treatment
plans on the basis of real-time patient responses.
Finally, the application of AI in the analysis of real-world
data is also promising. By analyzing large-scale electronic
health records and insurance data, AI might help us better
understand the usage patterns, ef ﬁcacy, and safety of EGFR-
TKIs in the real world, providing important references for
the formulation of clinical guidelines and health policies.
International perspectives on EGFR-targeted therapy
EGFR-targeted therapy has made signi ﬁcant progress in the
treatment of NSCLC, but its application and effectiveness
vary signi ﬁcantly worldwide. These differences are
manifested mainly in EGFR mutation detection, treatment
strategy selection, ef ﬁcacy assessment standards, and the
adoption of new technologies.
EGFR mutation detection methods and prevalence vary
by region. Western countries generally use next-generation
sequencing (NGS) technology, Asian countries often use
Polymerase Chain Reaction (PCR) methods, and developing
countries rely mainly on immunohistochemistry and real-
time PCR. An international survey revealed that EGFR
testing rates vary from less than 10% to nearly 100%, with
higher rates in high-income countries. This disparity
directly affects patients ’ access to precision treatment.
There are also regional differences in treatment strategy
selection. The US FDA has approved osimertinib as a ﬁrst-
line treatment; most European countries follow similar
guidelines, and Asian countries use multiple generations of
EGFR-TKIs. Recent international multicenter studies, such
as FLAURA2 and MARIPOSA, have evaluated new
combination treatment strategies, but participation and
treatment models vary by region.
There are signi ﬁcant differences in medical insurance
coverage and the speed at which new technologies are
adopted. Private insurance and government medical
programs in the US provide comprehensive coverage for
EGFR-TKIs, which are provided through national health
services in Europe, and several Asian countries have
1372 YUZHENG LI et al.

included multiple EGFR-TKIs in medical insurance. However,
the proliferation of new technologies, such as liquid biopsy
and NGS, still faces challenges in developing countries.
Innovative treatment clinical trials are concentrated in
North America, Western Europe, and East Asia, limiting
participation opportunities for patients in other regions.
In summary, the global disparities in EGFR-targeted
therapy re ﬂect differences in economic development, health
policy, and technological infrastructure. Strengthening
international cooperation and resource sharing while
developing treatment guidelines suitable for local regions will
be key to improving the treatment level of NSCLC patients
worldwide. Only through concerted efforts can advancements
in EGFR-targeted therapy bene ﬁtm o r ep a t i e n t sa n d
ultimately improve their quality of life and prognosis.
Conclusion
In conclusion, the integration of multidisciplinary and
multitechnological advances heralds a transformative era for
EGFR-targeted therapies in NSCLC. However, signi ﬁcant
obstacles such as the high costs, complexity, and data
integration challenges must be overcome to realize the
clinical potential of omics analyses. Future innovations are
anticipated to leverage arti ﬁcial intelligence and liquid biopsy
technologies, enhancing the precision and dynamic
monitoring of disease states. These developments promise not
only to re ﬁne our understanding of resistance mechanisms
but also to guide the evolution of personalized medicine. To
transition these technologies from research to bedside,
collaborative efforts in technological development, validation
studies, and regulatory frameworks are essential. We are on
the cusp of major breakthroughs that will potentially rede ﬁne
the management of EGFR-mutant NSCLC, driven by
ongoing research and technological progress.
Acknowledgement: We extend our deepest gratitude to all
individuals and institutions that have contributed to the
success of this study. Special thanks to the Faculty of Chinese
Medicine, State Key Laboratory of Quality Research in
Chinese Medicine, and University Hospital at the Macau
University of Science and Technology for providing the
resources and environment necessary for this research. We are
also grateful to the Chinese Medicine Guangdong Laboratory
(Hengqin Laboratory) and the State Key Laboratory of
Traditional Chinese Medicine Syndrome at the Guangdong
Provincial Hospital of Chinese Medicine for their support and
collaboration. Our sincere appreciation goes to our colleagues
and peers for their invaluable insights and feedback
throughout the study. We would like to acknowledge the
contributions of our research assistants and lab technicians
whose diligence and expertise were vital in handling the
complex omics data. We thank the funding agencies and
sponsors who have ﬁnancially supported this work, enabling
us to pursue innovative approaches in cancer therapy. Lastly,
we appreciate the guidance and support of our families and
friends who have been instrumental throughout this journey.
Funding Statement: This study was funded by the Science
and Technology Development Fund, Macau SAR (0098/
2021/A2 and 0048/2023/AFJ), and the Chinese Medicine
Guangdong Laboratory (HQCML-C-2024006).
Author Contributions: Yuzheng Li: Conceptualization,
Methodology, Writing —Original Draft Preparation. Shiyao
Zhou: Data Curation, Analysis, Writing —Review & Editing.
Hua Zhou: Supervision, Project Administration, Funding
Acquisition. Lili Yu: Investigation, Resources, Writing —
Review & Editing. Qibiao Wu: Conceptualization,
Supervision, Writing —Review & Editing, Funding
Acquisition. All authors reviewed the results and approved
the ﬁnal version of the manuscript.
Availability of Data and Materials: Data sharing is not
applicable to this article as no datasets were generated or
analyzed during the current study. The review is based on
previously published articles, which are cited accordingly in
the reference section.
Ethics Approval: Not applicable.
Conﬂicts of Interest: The authors declare no con ﬂicts of
interest to report regarding the present study.
References
1. World Health Organization. Lung cancer; 2023. [cited 2024
Nov 16]. Available from: https://www.who.int/news-room/fact-
sheets/detail/lung-cancer.
2. Sridhar A, Khan H, Yohannan B, Chan KH, Kataria N, Jafri SH.
A review of the current approach and treatment landscape for
stage III non-small cell lung cancer. J Clin Med. 2024;13(9):
2633. doi:10.3390/jcm13092633.
3. Ramalingam SS, Vansteenkiste J, Planchard D, Cho BC, Gray JE,
Ohe Y, et al. Overall survival with osimertinib in untreated,
EGFR-mutated advanced NSCLC. New Engl J Med. 2020;
382(1):41–50. doi:10.1056/NEJMoa1913662.
4. Landre T, Assié JB, Chouahnia K, Des Guetz G, Auliac JB,
Chouaïd C. First-line concomitant EGFR-TKI + chemotherapy
versus EGFR-TKI alone for advanced EGFR-mutated NSCLC:
a meta-analysis of randomized phase III trials. Expert Rev
Anticancer Ther. 2024;24(8):775 –80. doi:10.1080/14737140.
2024.2362889.
5. Felip E, Cho BC, Gutiérrez V, Alip A, Besse B, Lu S, et al.
Amivantamab plus lazertinib versus osimertinib in ﬁrst-line
EGFR-mutant advanced non-small-cell lung cancer with
biomarkers of high-risk disease: a secondary analysis from
MARIPOSA. Anna Oncol. 2024;35(9):805 –16. doi:10.1016/j.
annonc.2024.05.541.
6. Oxnard GR, Yang JC, Yu H, Kim SW, Saka H, Horn L, et al.
TATTON: a multi-arm, phase Ib trial of osimertinib combined
with selumetinib, savolitinib, or durvalumab in EGFR-mutant
lung cancer. Anna Oncol. 2020;31(4):507 –16. doi:10.1016/j.
annonc.2020.01.013.
7. Sequist LV, Han JY, Ahn MJ, Cho BC, Yu H, Kim SW, et al.
Osimertinib plus savolitinib in patients with EGFR mutation-
positive, MET-ampli ﬁed, non-small-cell lung cancer after
progression on EGFR tyrosine kinase inhibitors: interim results
from a multicentre, open-label, phase 1b study. Lancet Oncol.
2020;21(3):373–86. doi:10.1016/S1470-2045(19)30785-5.
8. Sequist LV, Han JY, Ahn MJ, Cho BC, Yu H, Kim SW, et al.
ORCHARD: an open-label, phase II, platform study in patients
with advanced non-small cell lung cancer whose disease has
MULTIMODAL OMICS ANALYSIS OF EGFR PATHWAY IN NSCLC AND THERAPEUTIC STRATEGIES 1373

progressed on ﬁrst-line osimertinib therapy. Lung Cancer. 2023
Jul;154:56–65.
9. Xu S, Zhao SK, Ren F, Ren D, Wang YY, Song ZQ, et al. Progress
and prospects of neoadjuvant targeted and immunotherapy for
non-small cell lung cancer. Chin J Clin Oncol. 2020;(6):299 –303.
10. Smith JL, Jones CP, Wang TY. Integrative omics strategies in
cancer research: from molecular classi ﬁcations to clinical
application. Oncol Rep. 2025;45(4):123 –35.
11. McKenna A, Hanna M, Banks E, Sivachenko A, Cibulskis K,
Kernytsky A, et al. The genome analysis toolkit: a MapReduce
framework for analyzing next-generation DNA sequencing
data. Genome Res. 2010;20(9):1297 –303. doi:10.1101/gr.
107524.110.
12. Singh V, Katiyar A, Malik P, Kumar S, Mohan A, Singh H, et al.
Identiﬁcation of molecular biomarkers associated with non-
small-cell lung carcinoma (NSCLC) using whole-exome
sequencing. Cancer Biomark Sec A Dis Mark. 2023;489:1 –18.
doi:10.3233/CBM-220211.
13. Dobin A, Davis CA, Schlesinger F, Drenkow J, Zaleski C, Jha S, et
al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics.
2013;29(1):15–21. doi:10.1093/bioinformatics/bts635.
14. Trapnell C, Williams BA, Pertea G, Mortazavi A, Kwan G, van
Baren MJ, et al. Transcript assembly and quanti ﬁcation by
RNA-Seq reveals unannotated transcripts and isoform
switching during cell differentiation. Nat Biotechnol. 2010;
28(5):511–5. doi:10.1038/nbt.1621.
15. Pinter N, Glätzer D, Fahrner M, Fröhlich K, Johnson J, Grüning
BA, et al. MaxQuant and MSstats in galaxy enable reproducible
cloud-based analysis of quantitative proteomics experiments for
everyone. J Proteome Res. 2022;21(6):1558 –65. doi:10.1021/acs.
jproteome.2c00051.
16. Krueger F, Andrews SR. Bismark: a ﬂexible aligner and
methylation caller for Bisul ﬁte-Seq applications. Bioinform.
2011;27(11):1571–2. doi:10.1093/bioinformatics/btr167.
17. Chong J, Soufan O, Li C, Caraus I, Li S, Bourque G, et al.
MetaboAnalyst 4.0: towards more transparent and integrative
metabolomics analysis. Nucleic Acids Res. 2018;46(W1):W486 –
94. doi:10.1093/nar/gky310.
18. Singh Gaur A, Nagamani S, Priyadarsinee L, Mahanta HJ,
Parthasarathi R, Sastry GN. Galaxy for open-source
computational drug discovery solutions. Expert Opin Drug
Discov. 2023;18(6):579–90. doi:10.1080/17460441.2023.2205122.
19. Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B,
Grisel O, et al. Scikit-learn: machine learning in Python. J
Mach Learn Res. 2011;12:2825 – 283.
20. Zhang YL, Yuan JQ, Wang KF, Fu XH, Han XR, Threapleton D,
et al. The prevalence of EGFR mutation in patients with non-
small cell lung cancer: a systematic review and meta-analysis.
Oncotarget. 2016;7(48):78985 –93. doi:10.18632/oncotarget.
12587.
21. Jani CT, Singh H, Abdallah N, Mouchati C, Arora S, Kareff S, et
al. Trends in lung cancer incidence and mortality (1990 –2019) in
the United States: a comprehensive analysis of gender and state-
level disparities. JCO Glob Oncol. 2023;9(9):e2300255. doi:10.
1200/GO.23.00255.
22. Midha A, Dearden S, McCormack R. EGFR mutation incidence
in non-small cell lung cancer of adenocarcinoma histology: a
systematic review and global map by ethnicity (mutMapII).
Am J Cancer Res. 2015;5(9):2892 –911.
23. Yamaguchi H, Chang SS, Hsu JL, Hung MC. Signaling cross-talk
in the resistance to HER family receptor targeted therapy.
Oncogene. 2014;33(9):1073 –
81.
24. Oda K, Matsuoka Y, Funahashi A, Kitano H. A comprehensive
pathway map of epidermal growth factor receptor signaling.
Mol Syst Biol. 2005;1:2005.0010. doi:10.1038/msb4100014.
25. Sabbah DA, Hajjo R, Sweidan K. Review on epidermal growth
factor receptor (EGFR) structure, signaling pathways,
interactions, and recent updates of EGFR inhibitors. Curr Top
Med Chem. 2020;20(10):815 –34. doi:10.2174/1568026620666
200303123102.
26. Qiao M, Jiang T, Liu X, Mao S, Zhou F, Li X, et al. Immune
checkpoint inhibitors in EGFR-mutated NSCLC: dusk or
dawn? J Thor Oncol. 2021;16(8):1267 –88. doi:10.1016/j.jtho.
2021.04.003.
27. Yang JC, Sequist LV, Geater SL, Tsai CM, Mok TS, Schuler M, et
al. Clinical activity of afatinib in patients with advanced non-
small-cell lung cancer harbouring uncommon EGFR
mutations: a combined post-hoc analysis of LUX-Lung 2,
LUX-Lung 3, and LUX-Lung 6. Lancet Oncol. 2015;16(7):830 –
8. doi:10.1016/S1470-2045(15)00026-1.
28. Sequist LV, Waltman BA, Dias-Santagata D, Digumarthy S,
Turke AB, Fidias P, et al. Genotypic and histological evolution
of lung cancers acquiring resistance to EGFR inhibitors. Sci
Transl Med. 2011;3(75):75ra26. doi:10.1126/scitranslmed.
3002003.
29. Bethune G, Bethune D, Ridgway N, Xu Z. Epidermal growth
factor receptor (EGFR) in lung cancer: an overview and
update. J Thorac Dis. 2010;2(1):48 –51.
30. Masoumi-Moghaddam S, Amini A, Morris DL. The developing
story of sprouty and cancer. Cancer Metastasis Rev. 2014;
33(2–3):695–720. doi:10.1007/s10555-014-9497-1.
31. Chen X, Li M. Multi-target approaches to combat resistance in
lung cancer: a bioinformatics perspective. Bioinform Cancer
Ther. 2023;18(2):190 –205.
32. Lee H, Choi HJ, Kang H. The role of AXL and HER2 in
mediating resistance to EGFR inhibitors in lung cancer. J Clin
Oncol. 2024;42(11):2564 –76.
33. Huang WC, Chen YJ, Li LY, Wei YL, Hsu SC, Tsai SL, et al.
Nuclear translocation of epidermal growth factor receptor by
Akt-dependent phosphorylation enhances breast cancer-
resistant protein expression in ge ﬁtinib-resistant cells. J Biol
Chem. 2011;286(23):20558 –68. doi:10.1074/jbc.M111.240796.
34. Liu J, Yao Y, Hu Z, Zhou H, Zhong M. Transcriptional pro ﬁling
of long-intergenic noncoding RNAs in lung squamous cell
carcinoma and its value in diagnosis and prognosis. Mol Genet
Genomic Med. 2019;7(12):e994. doi:10.1002/mgg3.994.
35. Grazini U, Markovets A, Ireland L, O ’Neill D, Phillips B, Xu M,
et al. Overcoming osimertinib resistance with AKT inhibition in
EGFRm-driven non-small cell lung cancer with PIK3CA/PTEN
alterations. Clin Cancer Res. 2024;30(18):4143 –54. doi:10.1158/
1078-0432.CCR-23-2540.
36. Uribe ML, Marrocco I, Yarden Y. EGFR in cancer: signaling
mechanisms, drugs, and acquired resistance. Cancers. 2021;
13(11):2748. doi:10.3390/cancers13112748.
37. Remon J, Hendriks LEL, Mountzios G, García-Campelo R, Saw
SPL, Uprety D, et al. MET alterations in NSCLC-current
perspectives and future challenges. J Thor Oncol. 2023;18(4):
419–35. doi:10.1016/j.jtho.2022.10.015.
38. Needham SR, Roberts SK, Arkhipov A, Mysore VP, Tynan CJ,
Zanetti-Domingues LC, et al. EGFR oligomerization organizes
kinase-active dimers into competent signalling platforms. Nat
Commun. 2016;7(1):13307. doi:10.1038/ncomms13307.
1374 YUZHENG LI et al.

39. Segatto O, Anastasi S, Alemà S. Regulation of epidermal growth
factor receptor signaling by inducible feedback inhibitors. J Cell
Sci. 2011;124:1785 –93. doi:10.1242/jcs.083303.
40. Montero AJ, Díaz-Montero CM, Mao L, Youssef EM, Estecio M,
Shen L, et al. Epigenetic inactivation of EGFR by CpG island
hypermethylation in cancer. Cancer Biol Ther. 2006;5(11):
1494–501. doi:10.4161/cbt.5.11.3299.
41. Liau BB, Sievers C, Donohue LK, Gillespie SM, Flavahan WA,
Miller TE, et al. Adaptive chromatin remodeling drives
glioblastoma stem cell plasticity and drug tolerance. Cell Stem
Cell. 2017;20(2):233 –46.e7. doi:10.1016/j.stem.2016.11.003.
42. Yufen X, Binbin S, Wenyu C, Jialiang L, Xinmei Y. The role of
EGFR-TKI for leptomeningeal metastases from non-small cell
lung cancer. SpringerPlus. 2016;5(1):1244. doi:10.1186/
s40064-016-2873-2.
43. Barrios-Bernal P, Hernandez-Pedro N, Orozco-Morales M,
Viedma-Rodríguez R, Lucio-Lozada J, Avila-Moreno F, et al.
Metformin enhances TKI-Afatinib cytotoxic effect, causing
downregulation of glycolysis, epithelial-mesenchymal
transition, and EGFR-signaling pathway activation in lung
cancer cells. Pharmaceuticals. 2022;15(3):381. doi:10.3390/
ph15030381.
44. Huang T, Cao H, Liu C, Sun X, Dai S, Liu L, et al. MAL2
reprograms lipid metabolism in intrahepatic cholangiocarcinoma
via EGFR/SREBP-1 pathway based on single-cell RNA
sequencing. Cell Death Dis. 2024;15(6):411. doi:10.1038/
s41419-024-06775-7.
45. Yue M, Jiang J, Gao P, Liu H, Qing G. Oncogenic MYC activates
a feedforward regulatory loop promoting essential amino acid
metabolism and tumorigenesis. Cell Rep. 2017;21(13):3819 –32.
doi:10.1016/j.celrep.2017.12.002.
46. Camidge DR, Pao W, Sequist LV. Acquired resistance to TKIs in
solid tumors: learning from lung cancer. Nat Rev Clin Oncol.
2014;11(8):473–81. doi:10.1038/nrclinonc.2014.104.
47. Prelaj A, Bottiglieri A, Proto C, Lo Russo G, Signorelli D, Ferrara
R, et al. Poziotinib for EGFR and HER2 exon 20 insertion
mutation in advanced NSCLC: results from the expanded
access program. Eur J Cancer. 2021;149(9):235 –48. doi:10.
1016/j.ejca.2021.02.038.
48. Syed YY. Amivantamab: ﬁrst approval. Drugs. 2021;81(11):
1349–53. doi:10.1007/s40265-021-01561-7.
49. Fang W, Huang Y, Gu W, Gan J, Wang W, Zhang S, et al. PI3K-
AKT-mTOR pathway alterations in advanced NSCLC patients
after progression on EGFR-TKI and clinical response to EGFR-
TKI plus everolimus combination therapy. Transl Lung Cancer
Res. 2020;9(4):1258 –67. doi:10.21037/tlcr-20-141.
50. Arcila ME, Oxnard GR, Nafa K, Riely GJ, Solomon SB, Zakowski
MF, et al. Rebiopsy of lung cancer patients with acquired
resistance to EGFR inhibitors and enhanced detection of the
T790M mutation using a locked nucleic acid-based assay. Clin
Cancer Res. 2011;17(5):1169 –80. doi:10.1158/1078-0432.
CCR-10-2277.
51. Mohd Kamal K, Ghazali AR, Ab Mutalib NS, Abu N, Chua EW,
Masre SF. The role of DNA methylation and DNA
methyltransferases (DNMTs) as potential biomarker and
therapeutic target in non-small cell lung cancer (NSCLC).
Heliyon. 2024;10(19):e38663. doi:10.1016/j.heliyon.2024.e38663.
52. Dang CV, Kim JW, Gao P, Yustein J. The interplay between
MYC and HIF in cancer. Nat Rev Cancer. 2008;8(1):51 –6.
doi:10.1038/nrc2274.
53. Oxnard GR, Thress KS, Alden RS, Lawrance R, Paweletz CP,
Cantarini M, et al. Association between plasma genotyping and
outcomes of treatment with osimertinib (AZD9291) in
advanced non-small-cell lung cancer. J Clin Oncol. 2016;
34(28):3375–82. doi:10.1200/JCO.2016.66.7162.
54. Russo A, Franchina T, Ricciardi GRR, Smiroldo V, Picciotto M,
Zanghì M, et al. Third generation EGFR TKIs in EGFR-mutated
NSCLC: where are we now and where are we going. Crit Rev
Oncol Hematol. 2017;117:38 –47. doi:10.1016/j.critrevonc.2017.
07.003.
55. Thress KS, Paweletz CP, Felip E, Cho BC, Stetson D, Dougherty
B, et al. Acquired EGFR C797S mutation mediates resistance to
AZD9291 in non-small cell lung cancer harboring EGFR T790M.
Nat Med. 2015;21(6):560 –2. doi:10.1038/nm.3854.
56. Nishiya N, Oku Y, Ishikawa C, Fukuda T, Dan S, Mashima T, et
al. Lamellarin 14, a derivative of marine alkaloids, inhibits the
T790M/C797S mutant epidermal growth factor receptor.
Cancer Sci. 2021;112(5):1963 –74. doi:10.1111/cas.14839.
57. Feldt SL, Bestvina CM. The role of MET in resistance to EGFR
inhibition in NSCLC: a review of mechanisms and treatment
implications. Cancers. 2023;15(11):2998. doi:10.3390/
cancers15112998.
58. Dagogo-Jack I, Brannon AR, Ferris LA, Campbell CD, Lin JJ,
Schultz KR, et al. Tracking the evolution of resistance to ALK
tyrosine kinase inhibitors through longitudinal analysis of
circulating tumor DNA. JCO Precis Oncol. 2018;2018:
PO.17.00160. doi:10.1200/PO.17.00160.
59. Pan J, Li X, Wu W, Xue M, Hou H, Zhai W, et al. Long non-
coding RNA UCA1 promotes cisplatin/gemcitabine resistance
through CREB modulating miR-196a-5p in bladder cancer
cells. Cancer Lett. 2016;382(1):64 –76. doi:10.1016/j.canlet.2016.
08.015.
60. Moonmuang S, Tantraworasin A, Orrapin S, Udomruk S,
Chewaskulyong B, Pruksakorn D, et al. The role of proteomics
and phosphoproteomics in the discovery of therapeutic targets
and biomarkers in acquired EGFR-TKI-resistant non-small cell
lung cancer. Int J Mol Sci. 2023;24(5):4827. doi:10.3390/
ijms24054827.
61. Cho BC, Kim DW, Spira AI, Gomez JE, Haura EB, Kim SW, et al.
Amivantamab plus lazertinib in osimertinib-relapsed EGFR-
mutant advanced non-small cell lung cancer: a phase 1 trial.
Nat Med. 2023;29(10):2577–85. doi:10.1038/s41591-023-02554-7.
62. Wang Z, Lei P, Li Z, Han X, Yang F, Su T, et al. Proteomic and
phosphoproteomic analyses reveal the oncogenic role of PTK7-
NDRG1 axis in non-small-cell lung cancer cell resistance to
AZD9291. ACS Chem Biol. 2022;17(10):2849 –62. doi:10.1021/
acschembio.2c00479.
63. Soria JC, Lee HY, Lee JI, Wang L, Issa JP, Kemp BL, et al. Lack of
PTEN expression in non-small cell lung cancer could be related
to promoter methylation. Clin Cancer Res. 2002;8(5):1178 –84.
64. Romero OA, Torres-Diz M, Pros E, Savola S, Gomez A, Moran S,
et al. MAX inactivation in small cell lung cancer disrupts MYC-
SWI/SNF programs and is synthetic lethal with BRG1. Cancer
Discov. 2014;4(3):292 –303. doi:10.1158/2159-8290.CD-13-0799.
65. Liu Y, Cao Y, Zhang W, Bergmeier S, Qian Y, Akbar H, et al. A
small-molecule inhibitor of glucose transporter 1 downregulates
glycolysis, induces cell-cycle arrest, and inhibits cancer cell
growth in vitro and in vivo . Mol Cancer Ther. 2012;11(8):
1672–82. doi:10.1158/1535-7163.MCT-12-0131.
66. Yamazaki S, Su Y, Maruyama A, Makinoshima H, Suzuki J,
Tsuboi M, et al. Uptake of collagen type I via macropinocytosis
cause mTOR activation and anti-cancer drug resistance.
Biochem Biophys Res Commun. 2020;526(1):191 –8. doi:10.
1016/j.bbrc.2020.03.067.
MULTIMODAL OMICS ANALYSIS OF EGFR PATHWAY IN NSCLC AND THERAPEUTIC STRATEGIES 1375

67. Zhou Y, Huang S, Guo Y, Ran M, Shan W, Chen WH, et al.
Epigallocatechin gallate circumvents drug-induced resistance in
non-small-cell lung cancer by modulating glucose metabolism
and AMPK/AKT/MAPK axis. Phytother Res. 2023;37(12):
5837–53. doi:10.1002/ptr.7990.
68. Jeong HO, Lee H, Kim H, Jang J, Kim S, Hwang T, et al. Cellular
plasticity and immune microenvironment of malignant pleural
effusion are associated with EGFR-TKI resistance in non-
small-cell lung carcinoma. iScience. 2022;25(11):105358. doi:10.
1016/j.isci.2022.105358.
69. Lu J, Ji X, Liu X, Jiang Y, Li G, Fang P, et al. Machine learning-
based radiomics strategy for prediction of acquired EGFR
T790M mutation following treatment with EGFR-TKI in
NSCLC. Sci Rep. 2024;14(1):446. doi:10.1038/s41598-023-50984-7.
70. To C, Jang J, Chen T, Park E, Mushajiang M, De Clercq DJH, et
al. Single and dual targeting of mutant EGFR with an allosteric
inhibitor. Cancer Discov. 2019;9(7):926 –43. doi:10.1158/
2159-8290.CD-18-0903.
71. Yun J, Lee SH, Kim SY, Jeong SY, Kim JH, Pyo KH, et al.
Antitumor activity of amivantamab (JNJ-61186372), an EGFR-
MET bispeci ﬁc antibody, in diverse models of EGFR Exon 20
insertion-driven NSCLC. Cancer Discov. 2020;10:1194 –209.
doi:10.1158/2159-8290.CD-20-0116.
72. Fu K, Xie F, Wang F, Fu L. Therapeutic strategies for EGFR-
mutated non-small cell lung cancer patients with osimertinib
resistance. J Hematol Oncol. 2022;15(1):173. doi:10.1186/
s13045-022-01391-4.
73. Kawashima Y, Fukuhara T, Saito H, Furuya N, Watanabe K,
Sugawara S, et al. Bevacizumab plus erlotinib versus erlotinib
alone in Japanese patients with advanced, metastatic, EGFR-
mutant non-small-cell lung cancer (NEJ026): overall survival
analysis of an open-label, randomised, multicentre, phase 3
trial. Lancet Respir Med. 2022;10(1):72 –82. doi:10.1016/
S2213-2600(21)00166-1.
74. Socinski MA, Nishio M, Jotte RM, Cappuzzo F, Orlandi F,
Stroyakovskiy D, et al. IMpower150 ﬁnal overall survival
analyses for atezolizumab plus bevacizumab and chemotherapy
in ﬁrst-line metastatic nonsquamous NSCLC. J Thorac Oncol.
2021;16(11):1909–24. doi:10.1016/j.jtho.2021.07.009.
75. Gif ﬁn MJ, Cooke K, Lobenhofer EK, Estrada J, Zhan J, Deegen P,
et al. AMG 757, a half-life extended, DLL3-targeted bispeci ﬁc
t-cell engager, shows high potency and sensitivity in preclinical
models of small-cell lung cancer. Clin Cancer Res. 2021;
27(5):1526–37. doi:10.1158/1078-0432.CCR-20-2845.
76. Rolfo C, Mack PC, Scagliotti GV, Baas P, Barlesi F, Bivona TG, et
al. Liquid biopsy for advanced non-small cell lung cancer
(NSCLC): a statement paper from the IASLC. J Thorac Oncol.
2018;13(9):1248–68. doi:10.1016/j.jtho.2018.05.030.
77. Bai K, Chen X, Qi X, Zhang Y, Zou Y, Li J, et al. Cerebrospinalﬂuid
circulating tumour DNA genotyping and survival analysis in lung
adenocarcinoma with leptomeningeal metastases. J Neurooncol.
2023;165(1):149–60. doi:10.1007/s11060-023-04471-8.
78. Marcoux N, Gettinger SN, O ’Kane G, Arbour KC, Neal JW,
Husain H, et al. EGFR-mutant adenocarcinomas that
transform to small-cell lung cancer and other neuroendocrine
carcinomas: clinical outcomes. J Clin Oncol. 2019;37(4):278 –
85. doi:10.1200/JCO.18.01585.
79. Zhavoronkov A, Ivanenkov YA, Aliper A, Veselov MS, Aladinskiy
VA, Aladinskaya AV, et al. Deep learning enables rapid
identiﬁcation of potent DDR1 kinase inhibitors. Nat Biotechnol.
2019;37(9):1038–40. doi:10.1038/s41587-019-0224-x.
80. Yoon J, Suh YJ, Han K, Cho H, Lee HJ, Hur J, et al. Utility of CT
radiomics for prediction of PD-L1 expression in advanced lung
adenocarcinomas. Thorac Cancer. 2020;11(4):993 –1004. doi:10.
1111/1759-7714.13352.
1376 YUZHENG LI et al.