---
reference_id: DOI:10.1186/s12943-025-02287-w
title: Single-cell and spatial transcriptomic analyses revealing tumor microenvironment remodeling after neoadjuvant chemoimmunotherapy in non-small cell lung cancer
authors:
- Xiaolu Cui
- Siyuan Liu
- He Song
- Jingjing Xu
- Yanbin Sun
journal: Molecular Cancer
year: '2025'
doi: 10.1186/s12943-025-02287-w
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://molecular-cancer.biomedcentral.com/counter/pdf/10.1186/s12943-025-02287-w"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1186_s12943-025-02287-w.pdf
---

# Single-cell and spatial transcriptomic analyses revealing tumor microenvironment remodeling after neoadjuvant chemoimmunotherapy in non-small cell lung cancer
**Authors:** Xiaolu Cui, Siyuan Liu, He Song, Jingjing Xu, Yanbin Sun
**Journal:** Molecular Cancer (2025)
**DOI:** [10.1186/s12943-025-02287-w](https://doi.org/10.1186/s12943-025-02287-w)

## Content

Cui et al. Molecular Cancer          (2025) 24:111  
https://doi.org/10.1186/s12943-025-02287-w
RESEARCH Open Access
© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 
International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if 
you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or 
parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To 
view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.
Molecular Cancer
Single-cell and spatial transcriptomic 
analyses revealing tumor microenvironment 
remodeling after neoadjuvant 
chemoimmunotherapy in non-small cell lung 
cancer
Xiaolu Cui1†, Siyuan Liu2†, He Song3*, Jingjing Xu4* and Yanbin Sun2* 
Abstract 
Non-small cell lung cancer (NSCLC) represents the most common pathological type of lung cancer, and the com-
bination of neoadjuvant immunotherapy with chemotherapy has emerged as the first-line treatment for NSCLC. 
Nevertheless, the efficacy of this therapeutic approach remains variable. The present study aims to examine 
the impact of chemoimmunotherapy in NSCLC patients, with a view to identifying key molecules, critical cell sub-
populations, communication patterns and spatial distributions that potentially correlate with therapeutic sensitivity. 
A total of 16 lung cancer tissue samples were collected from a cohort of 12 NSCLC patients and subjected to single-
cell RNA and spatial transcriptome sequencing. Our data demonstrated that the distribution of CD4 + Treg T cells 
and mCAFs indicated an immunosuppressive tumor microenvironment, while the accumulation of CD4 + Th17 T 
cells and iCAFs could act as a positive marker for the sensitivity to chemoimmunotherapy. Furthermore, a significant 
high level of SELENOP-macrophages was observed in tissues from positive responders, and a strong co-localiza-
tion between SELENOP-macrophages and antigen-presenting cancer associated fibroblasts (CAFs) in the tumor 
boundaries was identified, indicating the cooperative roles of these two cell types in response to combined therapy. 
Moreover, SELENOP-macrophages were observed to be accumulated in tertiary lymphoid structures, which further 
suggested its critical role in recruiting lymphocytes. Furthermore, analysis of cell–cell communication, based on spa-
tial transcriptomics, suggests that the interactions between SELENOP-macrophages, apCAFs, CD4 + and CD8 + T 
cells were significantly enhanced in responders. In addition, SELENOP-macrophages recruited CD4 + Naïve, Helper 
and CD8 + Naïve T cells through pathways such as the cholesterol, interleukin, chemokine and HLA when responding 
to combined therapy. The present study further unveils the dynamic spatial and transcriptional changes in the tumor 
microenvironment of non-small cell lung cancer in response to combination therapy.
†Xiaolu Cui and Siyuan Liu contributed equally to this work.
*Correspondence:
He Song
hsong@cmu.edu.cn
Jingjing Xu
xujj@cmu.edu.cn
Yanbin Sun
ybsun@cmu.edu.cn
Full list of author information is available at the end of the article

Page 2 of 33Cui et al. Molecular Cancer          (2025) 24:111 
Keywords Non-small cell lung cancer, Single-cell RNA sequencing, Spatial transcriptome, Neoadjuvant 
chemoimmunotherapy, Tertiary lymphoid structures
Graphical Abstract
Introduction
Lung cancer is the leading cause of death for cancer 
patients worldwide, accounting for 20% of all cancer-
related deaths [1, 2]. Lung cancer is the second most 
common cancer in terms of the estimated number of 
new cancer cases in 2024 [1]. Non-small cell lung cancer 
(NSCLC) accounts for 85% of all lung cancer cases [3], 
adenocarcinoma accounts for approximately 40%, and 
squamous cell carcinoma accounts for 25–30% of all 
lung cancer cases. Over the past decade, immunotherapy 
has changed the treatment landscape for NSCLC [4, 5]. 
Immune checkpoint blockade (ICB) has significantly 

Page 3 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
extended progression-free survival (PFS) and overall sur -
vival (OS) in patients with stage III NSCLC, with a high 
response rate (RR) [6, 7]. Notably, combination chemo -
immunotherapy has shown greater treatment efficacy 
than chemotherapy alone does, and this combination 
treatment strategy benefits patients with both nonsqua -
mous and squamous cancers, regardless of the expression 
status of programmed cell death ligand 1 (PD-L1) [8, 9]. 
Immunotherapy has become the first-line treatment for 
NSCLC, and neoadjuvant immunotherapy before sur -
gical resection in patients with resectable NSCLC has 
resulted in longer event-free survival and a higher rate of 
pathological complete response [10, 11]. Nonetheless, a 
proportion of patients remain unresponsive to ICB, and 
the mechanisms of immunotherapy resistance are poorly 
understood.
In addition to PD-L1 expression levels, several fac -
tors can predict the response to immunotherapy in can -
cer patients, including alterations in genomic signature 
genes, tumor mutation burden and the status of distinct 
T-cell subtypes [12–15]. The tumor microenvironment 
(TME) plays a critical role in tumor progression, metasta-
sis and sensitivity to anticancer therapy [14, 16]. The TME 
is a highly heterogeneous ecosystem containing a variety 
of cellular components, including immune cells, fibro -
blasts, endothelial cells and epithelial cells. The intricate 
interactions between immune cells and cancer-associated 
fibroblasts, malignant epithelial cells and endothelial cells 
are essential for the remodeling of the TME, including 
immune activation, immune escape, extracellular matrix 
(ECM) remodeling and tumor metastasis [17, 18]. ICB is 
capable of reshaping the TME, and the remodeled TME 
can evolve in different directions, such as enhanced 
therapeutic sensitivity or induced therapeutic resistance, 
ultimately leading to different therapeutic outcomes, i.e., 
pathological complete response (pCR) of the tumors or 
immune escape and therapeutic resistance [19, 20]. ICB 
in combination with chemotherapy has become a first-
line treatment option for early-stage NSCLC patients 
before surgical resection, and clinical trial data have 
confirmed that neoadjuvant chemoimmunotherapy can 
significantly increase the rates of major pathological 
response (MPR) and pCR [8, 10, 21]. However, the effects 
of immune checkpoint blockade on the re-establishment 
of the TME in NSCLC and how the altered responsive -
ness of the TME to ICB affects the course of treatment 
response are not well characterized.
Recently, studies have focused on the dynamic changes in 
the TME in response to immunotherapy and analyzed the 
associations between TME remodeling and the clinical out-
comes of immunotherapy. As a predominant cytotoxic cell 
component in the TME, clonal expansion and infiltration 
of T cells have been shown to be positive responses to ICB 
therapy, among which specific subtypes of T cells, such as 
CD137 + CD8 + T cells, PD-1 + Ki-67 + CD8 + T cells and 
Tregs, have been found to predict the response to neoadju-
vant chemoimmunotherapy in NSCLC patients [12, 13, 22]. 
Tumor-infiltrating B (TIB) cells have also been associated 
with the therapeutic responsiveness of immunotherapy in 
NSCLC, and among the B-cell subtypes, memory B cells 
with G protein–coupled receptor 183 have been found to 
be correlated with a positive therapeutic response [23]. 
The number of tumor-infiltrating neutrophils increases 
after successful immunotherapy, and therapy-induced neu-
trophils, which require an interferon gene signature, are 
essential for an effective response to immunotherapy [24]. 
In NSCLC, Hui et al. investigated immune cell profiles after 
neoadjuvant chemoimmunotherapy via single-cell RNA 
sequencing (scRNA-seq) and reported that several criti -
cal events, including the inhibition of activated TNFRSF4 
regulatory T cells (Tregs), increased LAMP3 dendritic cells 
(DCs), and the expansion of intratumoral CD4 T clones 
and peripheral C3 cytotoxic CD8 T clones, were correlated 
with positive clinical outcomes [19]. They focused mainly 
on immune cell changes in their study. Hu et al. provided 
a more comprehensive analysis of TME changes, including 
malignant epithelial cells and key immune cells, after neo-
adjuvant chemoimmunotherapy in NSCLC patients [20]. 
They also compared the scRNA-seq data from patients 
with MPR or non-major pathological response (NMPR) 
after treatment and reported significant changes in T cells, 
B cells, macrophages, neutrophils and cancer cells. How -
ever, owing to the limitations of scRNA-seq in these stud-
ies, their analysis did not include changes in the spatial 
distribution of cells, which are likely closely linked to the 
response to immunotherapy. In addition, the focus of their 
study was on immune cells, and although they discussed 
the changes in the fraction of malignant epithelial cells after 
combination therapy, they did not provide in-depth insight 
into the differentiation of malignant epithelial cells and 
their communication with other cell types.
To gain insight into the dynamic changes in the 
tumor microenvironment of non-small cell lung can -
cer patients following neoadjuvant chemoimmuno -
therapy, we conducted comprehensive and in-depth 
single-cell RNA sequencing and spatial transcriptome 
sequencing on tumor tissue samples from a cohort of 
12 NSCLC patients who underwent surgically resec -
tion of the tumors in our center. The validation cohort 
including two independent cohorts of NSCLC patients 
was also employed to validate some of the findings. This 
study aimed to investigate the changes in gene expres -
sion patterns, biological functions, cell development 
and interactions among immune cells, stromal cells and 
malignant cells in response to the therapy.

Page 4 of 33Cui et al. Molecular Cancer          (2025) 24:111 
Materials and methods
Patient cohorts and tissue collection
A total of 12 patients were included in this study, all of 
whom underwent surgical resection of the tumors at 
the Department of Thoracic Surgery, First Hospital of 
China Medical University, from January 2022 to March 
2023 and were pathologically diagnosed with NSCLC 
(Table  S1a). Informed consent was obtained from each 
patient prior to sample collection, and the study was 
approved by the Ethics Committee of China Medical 
University (Authorization number: AF-SOP-07–1.2–01). 
Patient inclusion criteria was as follows: (1) Age from 
50 – 80 years old. (2) Underwent percutaneous lung 
tumor biopsy before surgery and were diagnosed with 
NSCLC. (3) Written informed consent was obtained 
from each patient for both surgery and research pur -
poses. (4) The enrollment of the patients complied with 
the ethical requirements by ethics committee of First 
Hospital of China Medical University. Among them, six 
patients received 3‒5 cycles of neoadjuvant immuno -
therapy (PD-L1 blockade) combined with cisplatin-based 
chemotherapy prior to surgery, and are categorized as the 
post-treatment (PT) group, whereas the other six patients 
received thoracoscopic lobectomy without any neoad -
juvant therapy, and these patients are categorized as the 
treatment-naïve (TN) group. All patients who received 
neoadjuvant therapy showed a significant reduction in 
tumor volume by computed tomography (CT) imaging, 
and the final pathological diagnosis was as follows: non-
major pathologic response in 3 patients, major pathologi-
cal response (≤ 10% residual viable tumor in the primary 
tumor and lymph nodes) in 2 patients and pathologic 
complete response (0% residual viable tumor in the pri -
mary tumor and lymph nodes) in 1 patient [25, 26]. In all 
cases, fresh lung tumor tissue was collected immediately 
after surgical resection for tissue processing and scRNA-
seq. Additionally, in order to identify the reshaping of 
NSCLC tumor microenvironment by neoadjuvant ther -
apy, formalin-fixed paraffin-embedded (FFPE) sections 
from four patients with pathological assessments from 
NMPR to pCR in the neoadjuvant cohort were collected 
for spatial transcriptome sequencing.
For the two patients (patient 08 and patient 09) evalu -
ated as NMPR, their tumor tissue samples were able to 
demonstrate the characteristics of a “cold” tumor micro -
environment that was unresponsive to neoadjuvant 
therapy. In contrast, although patient 12 was evaluated 
as NMPR, we observed a significant boundary between 
the malignant regions and non-malignant structures 
in the tumor sections by hematoxylin‒eosin (H&E) 
staining. Therefore, the tissue sample from patient 12 
should reflect the characteristics of the tumor micro -
environment that was in the process of responding 
to neoadjuvant therapy. Finally, the samples from the 
patient evaluated as pCR (patient 10) were able to reflect 
the characteristics of the tumor microenvironment that 
had reached a complete pathological response after neo -
adjuvant therapy. These four tumor samples should be 
able to reflect the different sensitivities of NSCLC tumors 
in response to neoadjuvant therapy, alongside the differ -
ent stages of the tumors in the process of responding to 
neoadjuvant therapy. Hence, they were selected for spa -
tial transcriptome sequencing.
FFPE sections from a cohort of 10 NSCLC patients 
who underwent surgical resection of the tumors at the 
Department of Thoracic Surgery, First Hospital of China 
Medical University were collected for validation. Among 
them, 6 patients received 3‒5 cycles of neoadjuvant 
immunotherapy (PD-L1 blockade) combined with cispl -
atin-based chemotherapy prior to surgery. The final path-
ological diagnosis for the post-treatment patients was as 
follows: NMPR in 3 patients, MPR in 1 patient and pCR 
in 2 patients (Table S1b).
Tissue dissociation and scRNA‑seq
Fresh NSCLC tumor tissues were obtained from patients, 
washed with ice-cold phosphate-buffered saline (PBS) 
and processed with a tumor dissociation kit (Miltenyi 
Biotec, Germany) to prepare single-cell suspensions. Cel-
lular suspensions were loaded on a 10X Genomics Gem -
Code single-cell instrument that generates single-cell 
gel bead-in-EMlusion (GEMs). Libraries were generated 
and sequenced from the cDNAs with Chromium Next 
GEM Single Cell 5’ Reagent Kits v3. Barcoded, full-length 
cDNAs were then reverse-transcribed from polyade -
nylated mRNAs to generate sufficient masses for library 
construction, which were sequenced on an Illumina 
NovaSeq 6000 platform at Gene Denovo Biotechnology 
(Guangzhou, China).
Data quality control and gene expression quantification
Genome alignment was performed via 10X Genomics 
Cell Ranger software (version 6.1.0). Following align -
ment, briefly, cells meeting the following criteria were 
retained through Seurat (Version 3.0) and were passed 
to downstream analysis: (1) nFeature range from 300 
to 6500; (2) 600 to 43,000 unique molecular identifiers 
(UMI)s; (3) < 15% UMIs of mitochondria genes. Potential 
doublets and multiplets were filtered by DoubletFinder 
to avoid influencing cell clustering and annotation. After 
quality control, the gene expressions were normalized by 
Seurat LogNormalize, which is a global-scaling normali -
zation method [27].Subsequently, Harmony algorithm 
was used to integrate all samples, minimizing batch 
effect. Principal component analysis was then carried 

Page 5 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
out on the integrated expression matrix for dimensional 
reduction and downstream analysis.
Cell clustering and annotation
The integrated expression matrix is then scaled, and prin-
cipal component analysis (PCA) is performed for dimen -
sional reduction. Then, we implemented a resampling 
test inspired by the jackStraw procedure. We identified 
‘significant’ PCs as those with strong enrichment of genes 
with low p values for downstream clustering and dimen -
sionality reduction. The distances between the cells were 
calculated on the basis of previously identified PCs. The 
log-normalized matrices were then loaded on SingleR 
R packages (version 1.8.1) for cell type annotation and 
verified by manual annotation, which was based on cor -
relating the gene expression of reference cell types with 
single-cell expression.
Differentially expressed gene analysis
The expression values of each gene in a given cluster were 
compared against those of the remaining cells via the 
Wilcoxon rank sum test. Significantly upregulated genes 
were identified via several criteria. First, genes had to be 
at least 1.28-fold overexpressed in the target cluster. Sec -
ond, genes had to be expressed in more than 25% of the 
cells belonging to the target cluster. Third, the p value is 
less than 0.05.
Differentially expressed gene analysis for groups
Seurat (version 4.1.0) was used for differentially 
expressed gene analysis. New individuals were set up as 
“group_cluster” or “group_cell type” for analysis. We sub-
sequently used a hurdle model in MAST (Model-based 
Analysis of Single-cell Transcriptomics) to identify dif -
ferentially expressed genes for a group in one cluster. We 
identified differentially expressed genes (DEGs) accord -
ing to the following criteria: 1) |logFC|≥ 1; 2) p_value_
adj ≤ 0.05; and 3) the percentage of cells where the gene 
was detected in a specific cluster was greater than 10%.
Single‑cell V(D)J analysis
After GEM generation, the gel beads are ruptured, and 
the cells are lysed. GEMs are then incubated, and polyA 
mRNA in cell lysates is reverse transcribed to generate 
barcoded full-length first-strand cDNA. The cDNA was 
then purified and amplified via PCR. The cDNA product 
was then purified and subjected to subsequent T-cell and 
B-cell enrichment. Before constructing the library, the 
enriched V(D)J fragments were digested and screened 
to generate DNA fragments of different lengths. An Illu -
mina sequencing library with V(D)J enrichment and 5’ 
gene expression was constructed via the single-cell V(D)J 
Kit. Sequencing was performed via an Illumina NovaSeq 
6000 at Gene Denovo Biotechnology (Guangzhou, 
China). We used Trust4 software to analyze the bioinfor -
matics data, construct an immune library, and visualize 
the analysis results.
Spatial transcriptomics (ST)
ST was performed via the Visium Spatial Gene Expres -
sion System (10 × Genomics). We first performed RNA 
quality control and trimming on paraffin-embedded 
blocks of lung cancer tissue, and then the sections were 
prepared at room temperature at a thickness of 5 μm and 
subjected to deparaffinization, HE staining, 85% glycerol 
sealing and brightfield imaging experiments. Next, we 
used probe hybridization to detect transcripts. The probe 
hybridization system uses the RTL (RNA-templated liga -
tion) technique, where each gene is detected via two 
probes, the left arm and the right arm. Then, the polyA 
end of the DNA strand can be captured by binding to the 
poly(dT) of the capture sequence, and the read2 end pro -
vides the binding site for the amplification primer, which 
completes the amplification of the DNA with barcode 
information. DNA with barcode information is ampli -
fied. Once the probes have been purified, library con -
struction begins. The mRNA in the tissue is degraded 
via RNase, which releases the probe, which hybridizes to 
the mRNA. The polyA of the probe was attached to the 
poly(dT) of the capture sequence on the chip, and PCR 
amplification was performed using read2 sequences to 
extend the probe, allowing the probe to be coupled with 
the barcode sequence and the UMI sequence. We then 
used 0.08 M KOH in an alkaline environment to break 
the hydrogen bond between the extended probe and 
the capture sequence, and the probe with the labeled 
sequence could be transferred from the solid-phase vec -
tor to the liquid-phase system to facilitate subsequent 
library construction. Single-stranded DNA is ampli -
fied by PCR to increase its abundance and added to the 
sequencing junction to complete library construction. 
The cDNA libraries were sequenced on the Illumina 
sequencing platform by Genedenovo Biotechnology Co., 
Ltd. (Guangzhou, China). Alignment and demultiplex -
ing were conducted via the Space Ranger pipeline, and 
subsequent analyses were conducted via Seurat (version 
4.2.0) in R. We obtained the expression abundance infor -
mation of different genes in different spots on the basis of 
the genome comparison results, UMI counts and barcode 
sequence information.
Before spot clustering, the data were normalized for 
more accurate clustering. We employ a normaliza -
tion algorithm “SCTransform” that normalizes the gene 
expression for each spot in a regression model with a 
negative binomial error distribution and log link func -
tion. The primary function of the SCTransform algorithm 

Page 6 of 33Cui et al. Molecular Cancer          (2025) 24:111 
is to perform data pre-processing and normalization on 
spatial transcriptome data. It is employed to reduce tech -
nical noise, correct the batch effects and provide reliable 
and comparable data for subsequent analysis. To over -
come the extensive technical noise in any single gene for 
ST data, Seurat clusters spots on the basis of their PCA 
scores, with each PC essentially representing a ‘meta -
gene’ that combines information across a correlated gene 
set. We used MAST (Model-based Analysis of Single-
cell Transcriptomics) to find differential expression for 
a single cluster compared with all the other clusters. 
We identified DEGs according to the following criteria: 
1) p value ≤ 0.01. 2) log2FC ≥ 0.360674. 3) The percent -
age of cells where the gene is detected in a specific clus -
ter > 25%. We further selected the top 20 genes as the 
marker genes according to the results of the differentially 
expressed genes per cluster. The expression distribution 
of each marker gene was subsequently demonstrated via 
a heatmap, t-distributed stochastic neighbor embedding 
(t-SNE) distribution and bubble diagram.
Correlation analysis of the two omics methods
For the single-cell transcriptome, we calculated the aver -
age gene expression in each sample. For the spatial tran -
scriptome, we calculated the average amount of gene 
expression in each slice. We then calculated Pearson cor-
relations between samples of the single-cell transcrip -
tome and slices of the spatial transcriptome. Pearson 
correlation was used to measure the correlation between 
omics data.
Spot deconvolution
We used a residual convolutional neural network with 
the transformer decoder (RCTD) tool to predict the cell 
composition of each spot on the basis of the single-cell 
transcriptome data. We then used heatmaps, tissue maps, 
and Circos maps to visualize the distributions of different 
cell types in the tissues.
Identification of malignant cells
Gene expression data and cell type annotations extracted 
from the Seurat object were used as inputs in the 
InferCNV package to detect copy number variations 
(CNVs) and recognize malignant cells. Endothelial cells 
containing nonmalignant-derived cells were used as the 
control group. To reduce the possibility of false positive 
CNV calls, the default Bayesian latent mixture model 
was implemented to identify the posterior probabilities 
of alterations in each cell. Low-probability CNVs were 
filtered using the default value of “0.5” for the threshold. 
Cells with consistent patterns of CNV were partitioned 
into groups via the default hierarchical clustering ward. 
D2.
Multiplex immunohistochemistry (mIHC) analysis
mIHC analysis was performed via a Quadruple-Fluores -
cence Immunohistochemical Mouse/Rabbit Kit (pH 9.0) 
following the manufacturer’s protocol (ImmunoWay, 
Wuhan, China). The 9A working solution was placed in 
the repair cartridge and heated until boiling. The paraf -
fin sections were subsequently placed into boiling rea -
gent 9A working solution, heated for 30 min, and then 
cooled at room temperature. After the sections were 
removed, 50–100 µl of Reagent B was added to the sec -
tions, which were incubated at room temperature for 15 
min and then rinsed with PBST for 2 min 3 times. The 
sections were then removed, and the tissues were col -
lected with an immunohistochemistry pen. Then, the 
corresponding primary antibody was added, and the 
samples were incubated at 37 °C for 1–2 h. Next, the tis -
sues were rewarmed at 37 °C for 30 min and rinsed with 
PBST 3 times for 2 min each. The slides were dried, and 
50–100 µl of Reagent C working solution was added. The 
slides were incubated at room temperature for 30 min 
and then rinsed with PBST 3 times for 2 min each. Sub -
sequently, 50–100 µl of fluorescent dye reagent D-594 
working solution was added. Following a 10-min inter -
val, the sections were rinsed with PBST for 2 min 3 times 
and then placed in the repair box, and reagent F was 
added. The sections were incubated in a microwave oven 
at high power for three minutes. Once cooled, the sec -
tions were rinsed with PBST 3 times for 2 min each. The 
aforementioned steps were repeated, with the intermedi -
ate fluorescent dye changed to Reagent D-488, and the 
slides were labeled with a second primary antibody. Steps 
6–9 were repeated, the intermediate fluorescent dye was 
replaced with Reagent D-647, and the mixture was incu -
bated with the third primary antibody. Steps 6–8 were 
repeated, the intermediate fluorochrome was replaced 
with Reagent D-525, and the mixture was incubated with 
the fourth primary antibody. Then, 30–50 µl of Reagent 
G was added to the sections. After that, the sections 
were scanned via a Pannoramic MIDI digital scanner 
(3D Histech, Hungary), and the software used for analy -
sis of the pathology results was SlideViewer_2.5_RTM_
v2.5.0.143918. Antibodies against CD68 (YM6022), 
PanCK (YM6815), CXCL9 (YT6008), and SPP1 (YT3467) 
were purchased from ImmunoWay (Wuhan, China).
Immunohistochemistry (IHC) staining
The expression of indicated proteins in NSCLC tissue 
specimens was detected using an UltraSensitiveTM SP 
(Mouse/Rabbit) IHC kit (Maxin-Bio, Fuzhou, Fujian, 
China) according to the manufacturer’s instructions. 
Briefly, sections were dewaxed in xylene and ethanol, 
and antigen retrieval was performed using a microwave 
for 10 min at 100◦C. The sections were then incubated 

Page 7 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
with antibodies for 1 h, followed by biotinylated anti-IgG 
antibody and streptavidin-biotinylated-complex horse -
radish peroxidase. DAB and hematoxylin were used for 
nuclear staining. The antibodies were as listed as follows: 
STAT3 (RM8010), STAT5 (RM0478), IL-2 (BD-PE0366), 
Beta Catenin (RM1224), TGF-beta (RM3267), E2F1 
(RM4981). The antibodies were all purchased from Bio -
dragon (Suzhou, China).
Cell‒cell interaction analysis
CellPhoneDB V5 software was used to conduct the cell‒
cell interaction analysis. The software uses a single-cell 
gene expression matrix to predict the abundant ligand‒
receptor interactions between two cell states accord -
ing to the expression of receptors in one cell type and 
ligand expression in another cell type and then analyzes 
the number of ligand‒receptor pairs in the cell pair and 
their expression abundance information. On the basis of 
the results of the expression abundance and significance 
P value of ligand–receptor pairs in each cell pair, we fur -
ther screened the number of significant ligand–receptor 
pairs in each cell pair; thus, the communication relation -
ships between cells can be evaluated globally. To evalu -
ate whether a pair of matching receptors is significant, we 
screened them with a P value ≤ 0.05, calculated the prod-
uct of ligand gene expression and receptor gene expres -
sion, and then sequenced them from large to small.
Gene signature estimation
To estimate the cytotoxic and exhausted signatures of T 
cells and NK cells, we calculated the cytotoxic score and 
exhaustion score for each cell via the canonical cyto -
toxic (GZMA, GZMB, GZMK, GNLY, IFNG, PRF1, and 
NKG7) and exhausted (LAG3, TIGIT, PCCD1, HAVCR2, 
CTLA4, LAYN, and ENTPD1) markers, respectively. 
With the same method, we estimated the phenotypes 
(M1 or M2) and functions of angiogenesis and phago -
cytosis for each macrophage with previously reported 
markers (Table S11). In addition, the antigen processing 
and presentation signatures of apCAFs were calculated 
via the same method (Table S11). The mean value of the 
module scores of a cell cluster (≥ 10 cells) from an indi -
vidual sample was calculated to present the signature 
level.
Functional enrichment analysis
Pathway enrichment analysis was performed to investi -
gate the pathways and biological processes enriched in 
different cell types. The significantly upregulated genes of 
the cell subtypes were identified by comparing the gene 
expression in a given cluster with that in the remain -
ing cells via the Wilcoxon rank-sum test. The cutoff cri -
teria were set as a fold change > 1.28 and an adjusted 
p value < 0.05. The upregulated genes were subjected 
to GO enrichment analysis and Kyoto Encyclopedia of 
Genes and Genomes (KEGG) analysis. In addition, gene 
set enrichment analysis (GSEA) of a given cell type was 
conducted with software (http:// softw  are. broad insti tute. 
org/ gsea/ index. jsp). Moreover, we performed gene set 
variation analysis (GSVA) via a collection of gene sets 
from MSigDB to identify pathways and cellular processes 
enriched in different clusters. GSVA was performed as 
implemented in the GSVA R package version 1.26 on the 
basis of the cluster-averaged log-transformed expression 
matrix.
Trajectory analysis
RNA velocity analysis
The RNA velocity analysis was performed via the package 
velocyto (v0.17.13) with the default parameters, and the 
BAM files were used as inputs. For visualization, veloc -
ity vectors were plotted as locally average vector fields on 
the tSNE embeddings of our high-quality cells from the 
previous step.
Monocle2 pipeline
We used Monocle2 (version 2.22) to perform dimen -
sion reduction of the gene expression matrix and con -
struct the differentiation trajectory of the cell clusters. 
The cells are organized into a tree-like trajectory that 
includes branches and nodes. The most primitive cell 
clusters of the differentiation state along the trajectory 
are subsequently defined as the cell clusters with the 
smallest pseudotime values, after which the pseudotime 
values for all the cells are calculated. Genes that are dif -
ferentially expressed with different differentiation states 
are filtered out. The genes whose filtering threshold 
was set to an FDR < 1e-5 were selected as differentially 
expressed genes. To identify genes with different expres -
sion patterns between two branches, negative binomial 
generalized linear models are fitted to each branch, and 
differentially expressed genes dependent on different 
branches are computed and tested. The filtering thresh -
old was set to FDR < 1e-7.
Monocle3 pipeline
We used Monocle3 (version 1.3.1) to divide different cell 
clusters into different differentiation partitions on the 
basis of potential differentiation relationships. We used a 
simple principal tree algorithm, “simplePPT, ” to construct 
individual trajectories and calculate pseudotime values, 
achieving simultaneous construction of multiple differ -
entiation trajectories. The pseudotime values calculated 
by Monocle3 and the differentiation partition informa -
tion are mapped to the original UMAP graph in Seurat.

Page 8 of 33Cui et al. Molecular Cancer          (2025) 24:111 
Slingshot pipeline
We used Slingshot (version 2.2.0) to identify the lineages 
of the cell clusters and construct trajectories for the cell 
clusters. Slingshot identified lineages of cell clusters on 
a two-dimensional space via a minimum spanning tree 
(MST), which determines the number of lineages and 
branches. Differentiated lineages have different endpoint 
cell clusters but share a common starting cell cluster. 
Using simultaneous principal curves and orthogonal pro-
jection, Slingshot subsequently fits each differentiation 
lineage on a two-dimensional space and calculates the 
corresponding pseudotime values for the cell clusters, 
resulting in multiple linear cell differentiation trajectories 
originating from a common starting cell cluster. Pseudo -
time value mapping can map the pseudotime values and 
differentiation trajectories of cell clusters on different dif-
ferentiation trajectories.
Statistics
All the statistical analyses and presentations were per -
formed via R software (version 4.1.3). All the statistical 
tests used are defined in the figure legends. Statistical sig-
nificance was set at P or adjusted P < 0.05.
Results
High‑resolution single‑cell and spatial transcriptomic 
analyses characterized the TME landscape of NSCLC 
patients after adjuvant chemoimmunotherapy
The freshly collected NSCLC samples were immediately 
digested into a single-cell suspension, and all single-cell 
transcriptomes were generated via the commercial BD 
Rhapsody platform. FFPE samples were collected and 
subjected to spatial transcriptomic analysis. The overall 
design and patients enrollment in this study were shown 
in Fig.  1A. The detailed technical processes, including 
the steps of quality control and filtering, are presented in 
the Methods and Materials. A total of 58,210 cells with 
a median of 4887 genes per cell passed quality control 
and were subjected to further analysis (Figure S1A, S1B, 
Table  S2). All the cells were annotated into 8 cell types 
according to the well-recognized marker genes by the 
dimensional reduction method of t-distributed stochas -
tic neighbor embedding (t-SNE): T-NK cells, B-plasma 
cells, endothelial cells, epithelial cells, fibroblasts, mast 
cells, myeloid cells, and smooth muscle cells. The dis -
tributions of cells in different cell types (Fig.  1B), TN/
PT groups (Figure S1C) and each patient (Figure S1D) 
and the distribution of UMIs (Figure S1E, Table  S3) are 
shown by t-SNE maps. The expression patterns of the 
common marker genes for each cell type are shown in 
Fig.  1C, and the selected marker genes are also shown 
in t-distributed stochastic neighbor embedding (t-SNE) 
maps (Figure S1F). The fractions of the cell clusters in 
each patient showed strong heterogeneity (Fig.  1D). In 
PA04, the fraction of myeloid cells was the highest (2704 
cells, 44.62%), whereas in PA07 (MPR), PA10 (pCR) and 
PA11 (MPR), the levels of epithelial cells were notably 
decreased (0.69%, 0.65%, and 0.18%, respectively), which 
is consistent with the pathological assessment. By com -
paring the numbers and fractions of cell types between 
the TN and PT groups (Fig.  1E, Figure S1G, Table  S4), 
we found that the number of fibroblasts significantly 
increased after chemoimmunotherapy. Additionally, in 
the PT group, the proportions of T-NK cells and mast 
cells tended to increase, whereas the proportion of epi -
thelial cells tended to decrease (57.76% vs 40.86%, PT vs 
TN). Notably, in PA10, the only pCR patient, there was 
a significant increase in the proportions of B-plasma and 
T-NK cells, the sum of which reached 90%.
To characterize the transcriptomic landscape of the 
tumor tissues after chemoimmunotherapy, FFPE sec -
tions from 4 patients (PA08, PA09, PA10, and PA12) were 
sampled for spatial transcriptome analysis via the Visium 
(10 × Genomics) platform. The computed tomography 
(CT) images before and after chemoimmunotherapy 
were used to identify the tumors at baseline and after 
treatment (Fig. 1F). Upon filtering out the mitochondrial 
protein-coding genes, the resulting dataset consisted of 
12,741 individual spots, with an average of ∼7,651 genes 
and ∼7,500 UMIs per spot. The fraction of spots in each 
section, the distributions of spots in each cluster and sec -
tion, and the numbers of UMI counts in each spot were 
inferred and are shown in the Supplementary files (Figure 
S2A to S2D).
We performed correlation analyses on sample data 
from the single-cell transcriptome and spatial transcrip -
tome (Figure S2E). Next, a residual convolutional neural 
network with transformer decoder (RCTD) algorithm 
was employed to annotate each spot with cell types 
on the basis of the integrative analysis of the scRNA-
seq and ST data (Figure S2F to Figure S2L). The spatial 
atlas of major cell types in the NSCLC sections inferred 
by the RCTD algorithm, as well as the H&E staining of 
the sections, is shown in Fig.  1G. The cellular composi -
tion of each section was also characterized (Fig.  1H). The 
fraction of epithelial cells in PA08 (tumor-1) and PA09 
(tumor-4) was dramatically expanded; in contrast, in 
PA10 (tumor-2), the predominant cellular components 
were B-Plasm cells (20.04%) and fibroblasts (35.28%). In 
PA12 (tumor-3), the proportion of myeloid cells was the 
highest, accounting for 25.22%, and the proportion of 
epithelial cells was significantly lower than that in PA08 
and PA09, which was replaced by an increased propor -
tion of fibroblasts. The proportions of epithelial cells and 
immune cells in PA12 were intermediate between those 
in the NMPR samples (PA08 and PA09) and the pCR 

Page 9 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
Fig. 1 High-resolution single-cell and spatial transcriptomic analyses characterized the TME landscape of NSCLC patients after adjuvant 
chemoimmunotherapy. A Overview of sample collection and analysis pipeline, created in biorender (agreement number: OZ267FB6PD). B t-SNE 
plot showing the distributions of 8 distinct cell types from all NSCLC samples. C Heatmap showing the marker genes for each cell type in this 
study. D Bar plot showing the distribution of different cell types in each patient and each group. MPR: major pathologic response, NMPR: nonmajor 
pathologic response, pCR: pathologic complete response. E Comparison of the cell fraction between TNs and PTs by Wilcoxon signed-rank test; 
* indicates statistical significance. F CT images before and after chemoimmunotherapy from PA08, PA09, PA10, and PA12. Red arrows indicate 
the tumor regions. G The spatial annotation of 8 cell types in 4 NSCLC tumor sections inferred by the RCTD algorithm (lower), as well as the relative 
H&E staining (upper) of the sections. The black arrows in the H&E-stained sections indicate the TLS region. TLS: tertiary lymphoid structure. H 
Bar plot showing the percentages of different cell types annotated in the NSCLC sections. I Neighboring analysis showing the colocalization 
relationships between different cell types annotated in the NSCLC sections. Red indicates a close distance between cell types

Page 10 of 33Cui et al. Molecular Cancer          (2025) 24:111 
sample (PA10). Therefore, we assumed that the tumor tis-
sue of PA12 was in a therapy-responsive state, which was 
in agreement with our observations obtained by H&E 
staining. In addition, the spatial distribution of the PA12 
cells revealed that the epithelial cells were confined by 
myeloid cells, lymphocytes and stromal cells, which fur -
ther supported that tumor-3 is a therapy response region. 
As in tumor-1 and tumor-4, the tissues were dominated 
by epithelial cells, and only a small number of T-NK 
cells and myeloid cells infiltrated the tissues. Overall, we 
defined tumor-1 and tumor-4 regions as immunother -
apy-unresponsive regions (non-responders), tumor-2 
regions as pCR regions and tumor-3 regions as immuno -
therapy-responsive regions (responders).
Recent studies have highlighted the importance of ter -
tiary lymphoid structures (TLSs) in antitumor immunity 
[28, 29], as TLSs are composed of tumor-infiltrating lym -
phocytes and feature germinal centers, which are com -
monly observed in secondary lymphoid organs. TLSs 
are typically defined as an organization of infiltrating 
lymphocytes in nonhematopoietic organs triggered by 
chronic inflammation, including cancer, and the exist -
ence of TLSs has been associated with favorable progno -
ses and better responses to immunotherapy [28–30]. In 
tumor-2, T-NK cells and B cells were found to be signifi -
cantly infiltrated and organized in several regions, which 
could be observed as distinct discrete entities by H&E 
staining; therefore, the regions were identified as TLSs 
(Fig. 1G). The presence of TLSs in tumor-2 further con -
firmed that the section is an immunotherapy-responsive 
region, whereas no TLS regions were observed in the 
tumor-1 and tumor-4 sections, which were identified as 
non-responders. Furthermore, the Stereoscope algorithm 
was used to visualize the distribution of all cell types in 
TLS-positive sections and TLS-negative sections, from 
which we observed notable enrichment of NK-T cells and 
B cells in the TLS regions (Figure S3A to Figure S3F).
By establishing the spatial architectures of the tumor 
tissues, we then performed neighboring analysis of major 
cell types (Fig.  1I). The results revealed that in tumor-1 
and tumor-3, myeloid cells colocalized with T-NK cells, 
and epithelial cells spatially colocalized with myeloid 
cells and T-NK cells. In tumor 2, B-plasma cells are spa -
tially close to myeloid cells and fibroblasts. Epithelial cells 
neighbor fibroblasts in tumor-1 and tumor-4. The neigh -
boring relationships between different cell types indicate 
potential interactions between them. In conclusion, the 
results of the ST analysis revealed that the tumor tissues 
exhibited diverse cellular architectures, and the TME 
landscapes from the NSCLC sections showed a dynamic 
change in response to chemoimmunotherapy.
Chemoimmunotherapy enhances cellular metabolism 
in malignant cells and induces an immunosuppressive 
microenvironment in normal epithelial cells
Next, we investigated the population of epithelial cells. 
A total of 4963 epithelial cells were identified, and the 
cells were clustered into eight subclusters. The distribu -
tions of the cells and UMIs per spot were visualized via 
2D t-SNE plots (Fig.  2A, Figure S4A), and the marker 
genes of each subcluster are shown in Fig.  4B. The frac -
tions of the cells in each patient and group are shown in 
Fig. 4C, which revealed a significantly greater population 
of basal cells in the PT group (40% vs 80%, TN vs PT). 
The malignant cells and normal cells were distinguished 
via the inferCNV algorithm on the basis of copy number 
variations (CNVs) (Fig.  2D, Figure S4B, Table  S5). We 
further investigated the distributions of epithelial cells 
in the aneuploid and diploid groups via traditional mark -
ers and found that basal cells accounted for 73% of ane -
uploid cells, whereas in diploid cells, basal cells (36%) and 
Fig. 2 Chemoimmunotherapy enhances cellular metabolism in malignant cells and induces an immunosuppressive microenvironment in normal 
epithelial cells. A t-SNE maps showing the distribution of epithelial cells in each sample and the distribution of different epithelial subtypes. B 
Heatmap showing the marker genes used for identification. C Bar plot showing the proportions of epithelial subtypes in each sample and group. 
LUAD: lung adenocarcinoma; LUSC: lung squamous cell carcinoma. D Clustering of the epithelial cells from all samples into aneuploid cells 
and diploid cells and t-SNE maps showing the distribution of epithelial cells in the TN and PT groups. E Bar plot (left) and heatmap (right) showing 
the fraction of each epithelial cell type in tumor cells and normal epithelial cells. F Volcano map showing the differentially expressed genes (DEGs) 
of tumor cells between TNs and PTs, and the top 10 DEGs are labeled. G Bar plot showing the significantly enriched pathways in malignant cells 
before and after chemoimmunotherapy. Bars in blue color indicate the enriched pathways after treatment, and bars in green indicate the enriched 
pathways before treatment. The pathways are ranked by GSVA score. Red arrows indicate the pathways selected for experimental validation. H 
Images from IHC staining for the clinical sample sections from five NSCLC patients. The detected proteins were labled on the top of the panel, 
and the number of patients with treatment information /pathological assessment were labeled on the left of the panel. Scale bar = 30 μM, 
magnificent = 400 X. I, J The spatial localizations of tumor cells, normal epithelial cells and other cell types were annotated in NSCLC sections 
via the RCTD algorithm, and the percentage of each cell type is shown in a bar plot. The tumor boundaries in tumor-3 were marked in yellow, 
and the boundaries of transition zone were marked in green. The areas of TLSs in tumor-2 were labeled by yellow dot lines. K Neighboring analysis 
of the spatial distance between all cell types. Within the white dotted line are pairs of cell types that show significant changes in spatial distance 
with increasing sensitivity to chemoimmunotherapy
(See figure on next page.)

Page 11 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
AT2 cells (24%) accounted for the largest two populations 
(Fig.  2E), indicating that the malignant cells originated 
mostly from basal cells. The top 20 upregulated genes in 
malignant cells and normal cells after combined therapy 
are shown in Fig.  2F, Figure S4C, and Table  S6. KEGG 
analysis was performed on the upregulated genes in 
malignant cells and normal cells to identify their biologi -
cal functions (Figure S4D, Figure S4E). The upregulated 
genes in both populations were enriched in the terms 
“ribosome” and “chemical carcinogenesis–reactive oxy -
gen species”; however, the upregulated genes in malig -
nant cells were enriched in “cellular senescence” , “RNA 
degradation” , “thermogenesis” , “spliceosome” , and “ubiq-
uitin-mediated proteolysis” , suggesting that in malignant 
cells, the activities of RNA degradation and splicing are 
significantly increased, and ubiquitin-mediated prote -
olysis is increased, which reflects the cellular response 
to malignant transformation. The upregulated genes in 
Fig. 2 (See legend on previous page.)

Page 12 of 33Cui et al. Molecular Cancer          (2025) 24:111 
normal epithelial cells were enriched in the “p53 signaling 
pathway” , “cell cycle” , “ECM–receptor interaction” , and 
“pyrimidine metabolism” . To study the changes in the bio-
logical functions of epithelial cells, we performed GSEA 
(Figure S4F, Figure S4G). The results revealed that in 
malignant cells, the functions enriched in the PT groups 
were related to cell metabolism, such as “drug metabo -
lism” , “glutathione metabolism” , “tyrosine metabolism” , 
and “pyruvate metabolism” . In addition, “ferroptosis” and 
“protein digestion and absorption” were enhanced, sug -
gesting that neoadjuvant treatment might induce ferrop -
tosis and protein degradation and digestion in malignant 
cells. In addition, “EGFR tyrosine kinase inhibitor resist -
ance” was weakened in the PT group, which may suggest 
that neoadjuvant treatment has the potential to increase 
the sensitivity of EGFR tyrosine kinase inhibitors (TKIs) 
in EGFR-TKI-resistant NSCLC patients. In normal epi -
thelial cells, immune-related pathways, such as the “JAK-
STAT signaling pathway” , “Toll-like receptor signaling 
pathway” , “IL-17 signaling pathway” , “Th1 and Th2 cell 
differentiation” , “cytokine‒cytokine receptor interaction” , 
and “antigen processing and presentation” , were weak -
ened in the PT group. In addition, some hallmark path -
ways, such as the “PI3K-Akt signaling pathway” , “mTOR 
signaling pathway” , and “Hippo signaling pathway” , were 
deactivated in the PT group. These findings indicate an 
exhausted and immunosuppressive microenvironment 
in normal epithelial cells after immunotherapy, and the 
activity of hallmark pathways, which may lead to the car -
cinogenesis of epithelial cells, is also inhibited.
To experimentally validate the alterations of hallmark 
pathways related to anti-tumor immunity and oncogen -
esis, we performed GSVA analysis to find the differen -
tial hallmark pathways in epithelial cells before and after 
chemoimmunotherapy. The most significant pathways 
were shown by a bar char and ranked by GSVA score. 
Among them, we noticed that JAK/STAT3 pathway and 
IL2-STAT5 pathways were enhanced in PT group, while 
pathways closely related to tumor formation such as E2F 
pathway, TGF-beta pathway and WNT/Beta-catenin 
pathway were significantly inhibited in malignant cells 
after chemotherapy (Fig.  2G). IHC staining was per -
formed in FFPE sections from the validation cohort, and 
results validated our findings from GSVA analysis, that 
chemoimmunotherapy enhanced the activity of path -
ways related to anti-tumor immunity and inhibited the 
hallmark pathways which are markers for tumorigenesis 
(Fig. 2H).
Next, we aimed to investigate the developmental tra -
jectory of epithelial cells. Identifying the trajectory of 
malignant cells could reveal the key molecules and mech-
anisms that may drive the carcinogenesis of epithelial 
cells. The lineage trajectory for epithelial development 
was inferred via Monocle 2 (Figure S3H). The trajec -
tory begins with normal epithelial cells (diploid, state 2) 
and then progresses in two separate directions, with one 
direction leading to a carcinogenesis-like state but ending 
with normal cells (state 1), while the other direction even-
tually ending with malignant cells (state 3). Therefore, we 
believe that the trajectory from state 2 to state 3 simu -
lates the development from normal epithelial cells to can-
cer cells. We next investigated the different branches of 
the development trajectory. Branch 1 started from state 
2 and ended at state 1, and branch 2 started from state 
2 and ended at state 3. In accordance with the observed 
alterations in gene expression, the genes were catego -
rized into five distinct clusters (Figure S4I), and KEGG 
analysis was performed to identify the functions of the 
gene sets in each cluster. The genes in cluster 1, including 
the cancer biomarkers KRTs (KRT14, 17, and 19), TNF 
receptor genes (TNFRSF18 and TNFRSF1A), chemokine 
ligands (CXCL6, CXCL10, and CXCL14), and cell cycle 
regulators (CDK1, CDK4, CDKN1A, and CDKN2A), 
were significantly overexpressed in branch 2 but down -
regulated in branch 1. The genes in cluster 4, which 
included immunoglobulin proteins (IGHV1, IGHG1, and 
IGHV3), collagens (COL9A2, COL9A3, and COL2A1), 
fibroblast growth factors (FGF8, FGF17, and FGF18), and 
cell cycle regulators (CDK6, CCND1, and CCND2), were 
significantly overexpressed in state 1 but downregulated 
in state 3. The top 10 genes associated with the develop -
ment of cell fate were shown in Figure S4J.
We investigated the cell compositions and spatial dis -
tributions in NSCLC tumors via data from spatial tran -
scriptomic analysis (Fig.  2I, J). The RCTD algorithm was 
used to annotate the major cell types onto the paraffin 
sections. The populations of malignant cells reached over 
80% in non-responders (tumor-1 and tumor-4) but were 
rarely observed in tumor-2. In tumor-3, the population 
of myeloid cells was the highest (30.69%). In addition, in 
tumor-2, the highest population of cells was fibroblasts. 
In addition, we observed the highest number of NK-T 
cells in the pCR group (tumor-2). Neighboring analysis 
was performed to assess the spatial distance between the 
major cell types (Fig.  2K). The results are shown from 
non-responders to pCR patients (from left to right). 
We found that the spatial distance from fibroblasts to 
tumor cells decreased as immunotherapy sensitivity 
increased, whereas the spatial distance to B cells gradu -
ally increased. In addition, the spatial distance between 
NK-T cells and B cells decreased. In addition, fibroblasts 
appeared to gradually colocalize with macrophages and 
NK-T cells at a distance, whereas this colocalization dis -
appeared in pCR tissues because of a decrease in the pro -
portion of fibroblasts.

Page 13 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
Immunotherapy inhibited the differentiation and function 
of Th17 CD4 + T cells and rescued CD4 + T cells 
from exhaustion
Lymphocytes play key roles in anticancer immunity. The 
colony expansion of T cells has been recognized as a key 
marker for predicting the response to immunotherapy. 
Therefore, we investigated CD4 + and CD8 + T cells via 
single-cell RNA and single-cell T cell receptor sequenc -
ing (scTCR-seq) to determine the dynamics of T cells in 
NSCLC patients after neoadjuvant therapy.
Eight distinct cell subtypes were identified by replas -
tering 14,260 CD4 + T cells, including naïve, regulatory 
CD4 + T cells (Tregs), T helper 1 CD4 + T cells (Th1), 
T helper 17 CD4 + T cells (Th17), T follicular helper 
CD4 + T cells (Tfhs), T effector memory (Tem) CD4 + T 
cells, T resident memory (Trm) CD4 + T cells, and Trm-
Foxp3 + CD4 + T cells (Fig.  3A). The distribution of 
CD4 + T cells in each sample and the UMIs in CD4 + T 
cells are shown by t-SNE plots (Figure S5A). The pro -
portions of the CD4 + T-cell subtypes across different 
patients and groups were plotted (Figure S5B). To char -
acterize the changes in CD4 + T-cell clonotypes after 
chemoimmunotherapy, the scTCR-seq data were ana -
lyzed to detect T-cell receptor (TCR) clonality and diver -
sity. However, no significant differences were found in 
the expansion or diversity of CD4 + TCRs between TNs 
and PTs (Figure S5C to S5F). A comparison of the cell 
proportions between the TN and PT groups revealed a 
significant decrease in the number of Th17 cells, whereas 
the populations of Trm, Th1, and Tem cells tended to 
increase following neoadjuvant therapy (Fig.  3C). Th17 
cells primarily secrete IL-17A, IL-17F, IL-21, IL-22, and 
CCL20 and have been identified as crucial regulators of 
host immune responses against infection [31]. In human 
cancers, the Th17 lineage is known to perform both anti -
tumor and carcinogenic functions [32, 33], and the Th17/
Treg balance plays a pivotal role in antitumor immunity 
and autoimmunity [34]. In addition, high levels of IL-17A, 
which is mainly secreted by Th17 cells, increase resist -
ance to PD-L1 blockade [35, 36]. Therefore, we believe 
that immunotherapy might block the differentiation of 
naïve CD4 T cells into Th17 cells. Next, a KEGG analy -
sis of genes upregulated in Th17 cells was performed to 
assess the biological functions of the cells (Fig.  3D). We 
found that the functions were enriched mainly in inflam -
mation and infection diseases, such as COVID-19, Sal -
monella infection, shigellosis, and inflammatory bowel 
disease. Additionally, several hallmark pathways, such 
as the MAPK signaling pathway, the TGF-beta signal -
ing pathway, and the FoxO signaling pathway, were also 
found to be associated with Th17 cells. The upregulated 
genes were also enriched in immune-related pathways 
such as cytokine‒cytokine receptor interactions and the 
TNF signaling pathway, which is consistent with the find-
ings that Th17 cells secrete cytokines such as IL-17A and 
activate the downstream pathway of TNF signaling. Next, 
we analyzed the exhaustion signature of CD4 + T cells 
by using exhaustion markers (LAG3, TIGIT, PCCD1, 
HAVCR2, CTLA4, LAYN, ENTPD1). Compared with 
those in the TN group, the exhausted signature of 
CD4 + T cells in the PT group was notably lower (Fig. 3E). 
When the subtypes were compared, Th17 and Trm cells 
presented the lowest exhaustion signature, whereas Tem 
cells presented the highest exhaustion signature (Fig.  3F, 
Figure S5G). The DEGs in each subtype between the TN 
and PT groups were analyzed, and the top 5 upregulated 
(See figure on next page.)
Fig. 3 Remodeling of CD4 + T cells after chemoimmunotherapy and the spatial distribution of CD4 + T-cell subclusters in NSCLC tumors. A 
Reclustering of CD4 + T cells into 8 subpopulations shown by a t-SNE plot (left) and the distribution of CD4 + T cells in the treatment-naïve 
and posttreatment groups (right). B Heatmaps showing the significantly upregulated genes in all the CD4 + T-cell subclusters. C Box plot showing 
the comparison of the fractions of CD4 + T-cell subtypes between the TN and PT (Wilcoxon, * indicates P < 0.05). D The top 20 KEGG pathways 
enriched with the upregulated genes in the CD4 + Th17 subtype (adjusted P < 0.05). E Violin plots comparing the average exhausted gene 
signature of CD4 + T cells between the TN and PT groups. The violin is bounded by the first and third quartile with a horizontal line at the median 
and whiskers extend to the maximum and minimum value. P values determined by two-sided Wilcoxon rank-sum test. F Violin plots comparing 
the average exhausted gene signature between CD4 + T-cell subtypes in the PT group. P values determined by two-sided Wilcoxon rank-sum 
test. G Bubble plot showing the top 20 KEGG pathways enriched by the DEGs from the CD4 + Th17 subtype between the TN and PT groups. Each 
bubble indicates a signaling pathway (left), and the top 20 pathways associated with the relative bubbles are labeled, as listed in the right panel. 
Box plot indicating the proportion of Th17 CD4 + T cells (H), Treg CD4 + T cells (I) and ratio of Th17/Treg (J) in responder and non-responder. P 
values determined by Wilcoxon tests. K UMAP plot showing the cell subtypes identified in Hu’s cohort. L UMAP plot showing the identification 
of subclusters of CD4 + T cells. UMAP plots demonstrating the expression of maker genes GZMA (M) and FOXP3 (N) in subclusters of CD4 + T cells. 
O The proportions of Th17 (left), Treg CD4 + T cells (middle) and ratio of Th17/Treg (right) in pre-treatment and post-treatment groups were shown 
by box plots. P values determined by Wilcoxon tests. P The proportions of Th17 (left), Treg CD4 + T cells (middle) and ratio of Th17/Treg (right) 
in non-responders and responders were shown by box plots. P values determined by Wilcoxon tests. Q Differentiation trajectory of all CD4 + T-cell 
subtypes; the subtypes are labeled with different colors. The numbers on the trajectory tree indicate the branch nodes, and the differentiation tree 
was divided into 5 branches. R Heatmaps showing the signature scores of Th17/Treg in each spot of the tissue sections. The spots were labeled 
with colors, and red color indicates high score, while blue color indicates low score. S Box plots showing the level of Log2(Th17/Treg) in each 
section (left) and each group (right). Each spot is considered as a duplicate, and P values were determined by two-sided Wilcoxon rank-sum test

Page 14 of 33Cui et al. Molecular Cancer          (2025) 24:111 
genes in CD4 + T cells after combined therapy were iden-
tified (Figure S5H, Table  S7). KEGG analysis and GSEA 
were performed on the DEGs of Th17 cells to analyze 
the alterations in the cellular functions of Th17 cells in 
response to immunotherapy (Fig.  3G, Figure S5I). Anal -
ysis of the top 20 enriched pathways by KEGG revealed 
that cellular functions such as the NF-kappa B signaling 
pathway (ko04064), antigen processing and presentation 
(ko04612), and Th17 cell differentiation (ko04659) were 
inhibited after immunotherapy, which further confirmed 
that the fraction of Th17 cells was significantly reduced 
in PT patients. “ Apoptosis” (ko04210) and “protein pro -
cessing in the endoplasmic reticulum” (ko04210) were 
increased, suggesting that neoadjuvant therapy not only 
inhibited the differentiation but also induced the apopto -
sis of Th17 cells. GSEA also revealed significant inhibi -
tion of cellular functions related to infection, the immune 
response and carcinogenesis, such as the “B-cell receptor 
Fig. 3 (See legend on previous page.)

Page 15 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
signaling pathway” , “natural killer cell-mediated cytotox-
icity” , “Yersinia infection” , “PI3K-Akt signaling pathway” , 
and “proteoglycans in cancer” .
In order to further investigate the correlation between 
alterations in Th17 and Treg cells and the sensitivity of 
chemo-immunotherapy, the proportions of Th17 cells 
and Treg cells were analyzed in responders (MPR and 
pCR patients) and non-responders (NMPR patients). 
The results demonstrated that, in responders, the dis -
tribution of Th17 cells was elevated (Fig.  3H) while the 
percentage of Treg cells showed a decreasing tendency 
(F ig. 3I). Furthermore, the ratio of Th17 and Treg cells 
showed an elevation (Fig. 3J), although this result did not 
reach statistical significance. To validate this finding, we 
downloaded single-cell transcriptomic data from a study 
by Hu et al. [20]. In Hu’s cohort, 3 pre-treatment and 12 
post-treatment NSCLC patients (8 NMPR patients, 3 
MPR patients and 1 pCR patient) were enrolled. The cell 
clusters were identified using the same marker genes, and 
the distribution of cell clusters was shown by UMAP plot 
(Fig. 3K), with 14,368 CD4 + T cells identified (Figure S5J, 
Fig. 3L). The expression of marker genes GZMA (Th17) 
and FOXP3 (Treg) were color-coded and indicated by 
UMAP plots (Fig.  3M, N). In accordance with the find -
ings of this study, the proportion of Th17 cells and the 
ratio of Th17/Treg cells exhibited a downward trend in 
patients who had undergone post-treatment (Fig.  3O). 
Furthermore, the proportion of Th17 cells and the ratio 
of Th17/Treg cells increased following chemo-immu -
notherapy, while the proportion of Treg cells decreased 
after neoadjuvant therapy (Fig.  3P). The results from 
Hu’s cohort further confirmed our findings that the dis -
tribution of Th17 cells within the TME and a markedly 
elevated Th17/Treg ratio can predict a favorable respon -
siveness to immunotherapy.
To clarify the differentiation pathways of CD4 + T cells 
and the characteristic genes associated with the differ -
entiation states, we next reconstructed the proposed 
temporal differentiation trajectories of CD4 + T cells 
via Monocle 2 (Fig.  3Q, Figure S5K). In addition, RNA 
velocity was employed to construct a dynamic model of 
cell differentiation (Figure S5L). The reconstruction by 
Monocle 2 identified seven different developmental hier -
archies (states 1—7), with cells differentiating from naïve 
cells and showing two major branches of differentiation 
(states 3 and 6). Additionally, two different developmen -
tal trajectories of further differentiation were identi -
fied, one of which commenced from state 3 (state 1 and 
state 2). Trm cells are located at the end of state 6, and 
Treg cells are located at the end of state 3. From state 3 
onward, the cells exhibited two distinct branches of dif -
ferentiation, subsequently differentiating into two popu -
lations of Tfh (state 1) and Trm-Foxp3 + cells (state 2) 
(Figure S5M). To elucidate the function of characteristic 
genes in the process of cell differentiation, we conducted 
an analysis of genes that exhibited significant alterations 
in conjunction with disparate cell differentiation paths. 
Our investigation focused on genes that underwent mod-
ification along two principal branches: one from state 
5 to state 1 (Tfh cells located at the end of the branch), 
and the other from state 5 to state 6 (Trm cells located 
at the end of the branch). As shown in Figure S5N, the 
Fig. 4 Reshaping of CD8 + T-cell subclusters in NSCLC tissues by chemoimmunotherapy. A CD8 + T cells were reclustered into 8 subtypes, 
as shown by the t-SNE plot (left), and the distribution of CD8 + T cells in the TN and PT groups, as shown by the t-SNE plot (right). B Heatmap 
showing the significantly upregulated genes in each CD8 + T-cell subtype. C Box plot showing the comparison of the fractions of CD8 + T-cell 
subtypes between the TN and PT (Wilcoxon, ** indicates P < 0.01). D Violin plots comparing the average exhausted gene signature of CD8 + T 
cells between the TN and PT groups. The violin is bounded by the first and third quartile with a horizontal line at the median and whiskers 
extend to the maximum and minimum value. P values determined by two-sided Wilcoxon rank-sum test. E Violin plots comparing the average 
cytotoxic gene signatures of CD8 + T cells between the TN and PT groups (P values from two-sided Wilcoxon rank-sum test). F Violin plots 
comparing the exhausted gene signature between CD8 + T-cell subtypes in the PT group. G Violin plots comparing the cytotoxic gene signatures 
of CD8 + T-cell subtypes in the PT group. H The top 20 KEGG pathways enriched with the upregulated genes in the CD8 + Teff KLRG-high 
subgroup (adjusted P < 0.05). I Top 10 upregulated or downregulated KEGG pathways enriched with the DEGs in the CD8 + Teff KLRG-high 
subgroup between the TN and PT groups (adjusted P < 0.05). J The top 20 KEGG pathways enriched with the upregulated genes in the CD8 + Teff 
ZNF683-high subtype (adjusted P < 0.05). K Top 10 upregulated or downregulated KEGG pathways enriched by the DEGs in the CD8 + Teff 
ZNF683-high subtype between the TN and PT groups (adjusted P < 0.05). L The developmental trajectory of CD4 + T cells from all samples colored 
according to pseudotime; the color from light to dark indicates the progression of pseudotime. M The developmental trajectory of CD8 + T cells 
colored according to their differentiation state. N Differential trajectory of all CD8 + T-cell subtypes; the subtypes are labeled with different colors. 
The numbers on the trajectory tree indicate the branch nodes, and the differentiation tree was divided into 3 branches. O, P The developmental 
trajectory of CD8 + T cells in the TN group and PT groups. Q Pseudo-heatmap showing the significant genes correlated with the differentiation 
of CD8 + T cells from state 2 to state 4 (from naïve to regulator) and state 2 to state 1 (from naïve to memory). The genes were subjected to 5 
clusters, and the top 50 genes correlated with pseudotime are shown, with the selected KEGG pathways enriched in each gene cluster labeled 
on the left. R Spatial distributions of CD4 + and CD8 + T cells in 4 NSCLC sections according to the RCTD algorithm; each color indicates a distinct 
cell type. S Violin plot showing the proportion of CD8 + T cells in each section. Each spot is considered as a duplicate, and P values were determined 
by two-sided Wilcoxon rank-sum test, **** indicates P < 0.0001, Wilcoxon test
(See figure on next page.)

Page 16 of 33Cui et al. Molecular Cancer          (2025) 24:111 
genes were classified into 5 clusters on the basis of their 
expression trends, and KEGG analysis was performed to 
assess the biological functions of each gene cluster. The 
trends in gene expression exhibited two distinct direc -
tions. The first was a notable elevation in gene expres -
sion levels as the pseudotime progressed from state 5 
to state 6 (clusters 1 and 4). The second was a similarly 
pronounced increase in gene expression levels as the 
pseudotime time progressed from state 5 to state 1 (clus -
ters 2, 3, and 5). We found that genes in cluster 1 were 
enriched in functions such as Th17 differentiation (FOS, 
HSP90AA1, NKFB1, NFKBIA, and STAT3), antigen pro -
cessing and presentation (HLA-A), cytokine‒cytokine 
receptor interaction (CXCR3), and the T-cell receptor 
signaling pathway. Intriguingly, genes in cluster 2 were 
enriched in pathways related to non-small cell lung 
Fig. 4 (See legend on previous page.)

Page 17 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
cancer (GADD45G, CDKN1A, PRKCA), transcription 
misregulation in cancer, and the estrogen signaling path -
way (Figure S5O).
In order to further elucidate the spatial distribution of 
Th17 and Treg cells in NSCLC tumors, the RCTD algo -
rithm was employed to annotate the coordinates of Th17 
and Treg cells in four NSCLC sections, including two 
non-responders and two responders. Furthermore, the 
Th17/Treg ratio was scored in each spot of the sections 
to demonstrate the significance of the Th17/Treg ratio 
in assessing the sensitivity of immunotherapy. A signifi -
cant high score of the Th17/Treg ratio was observed in 
responders, especially in the non-malignant regions 
(Fig.  3R). Statistical analysis demonstrated a significant 
high ratio of Th17/Treg and a high level of Th17 cells in 
responders (Fig.  3S, Figure S5P), and a high level of Treg 
cells in non-responders, thereby supporting our findings 
from the single-cell RNA sequencing analysis.
Responders to chemoimmunotherapy exhibited 
significantly increased infiltration of effector CD8 + T cells 
in NSCLC tumors
A total of 12,755 CD8 + T cells were identified via 
scRNA-seq and were clustered by canonical marker 
genes: naïve, exhausted, effector, and memory. The effec -
tors were further clustered into 3 subpopulations by 
high expression of the marker genes KLRG1, KLRC1, 
and GZMA, while the memory cells were divided by the 
expression level of ZNF683 (Fig.  4A, B). The distribution 
of CD8 + T cells in each sample and the UMIs in CD8 + T 
cells are shown by t-SNE plots (Figure S6A). GZMA is a 
canonical cytotoxic marker, while CD8 + T cells highly 
expressing KLRG1 are defined as short-lived effector cells 
but are also recognized as having a cytotoxic phenotype 
[37, 38]. KLRC1, also known as NKG2A, is an inhibi -
tory receptor expressed in cytotoxic T cells and NK cells 
[39, 40]. The ligand of KLRC1 is the MHC I class HLA-E 
molecule [41], and the recognition of HLA-E by KLRC1 
can lead to the immune evasion of HLA-E-positive 
tumor cells [42]. Therefore, KLRC1 has also been iden -
tified as an immune checkpoint molecule, and KLRC1 
blockade was shown to work with ICBs to potentiate the 
immunity of CD8 + T cells [42–44]. The proportions of 
CD8 + T cells in each sample and group are shown in a 
bar plot (Figure S6B). When we compared the fraction 
of subclusters of CD8 + T cells between TNs and PTs, 
we found a significant decrease in the number of effec -
tor-KLRG1 cells in the PT group (Fig.  4C). We also ana -
lyzed the exhausted and cytotoxic signatures of CD8 + T 
cells between TNs and PTs, and the cytotoxic signature 
was evaluated via canonical cytotoxic markers (GZMA, 
GZMB, GZMK, GNLY, IFNG, PRF1, and NKG7). We 
found that neoadjuvant therapy significantly inhibited 
the exhausted signature and enhanced the cytotoxic 
capacity of CD8 + T cells (Fig.  4D, Fig.  4E). In addition, 
we compared the exhausted and cytotoxic signatures 
of each subtype (Fig.  4F, Figure S6C), and exhausted 
CD8 + T cells presented the strongest exhaustion score, 
as expected. In addition, exhausted CD8 + T cells also 
presented the highest cytotoxic score in the PT group, 
whereas in the TN group, exhausted, Trm ZNF683high 
and GZMA + effector high cells presented relatively 
high cytotoxic scores (Fig.  4G, Figure S6D). The DEGs 
in each subcluster between TNs and PTs were analyzed 
(Table S8), and the significantly upregulated genes in PTs 
are shown in a bubble plot (Figure S6E). With the help of 
scTCR-seq analysis, alterations in the TCR clonotypes of 
CD8 + T cells were analyzed to investigate the expansion 
and diversity of TCRs after combined therapy. However, 
no significant differences were found between the TN 
and PT groups (Figure S6F to Figure S6I).
We then investigated the functions of Teff-KLRG1 
in CD8 + T cells, the number of which is inhibited by 
combined therapy. KEGG analysis was performed on 
the genes whose expression was upregulated in Teff-
KLRG1 cells. The results revealed that the pathways 
enriched were “antigen presenting and presentation” 
(CD74, HLA-F), “T-cell receptor signaling pathway” 
(FYN, NKC2), and “natural killer cell-mediated cyto -
toxicity” (FYN, SH2D1A) (Fig.  4H). Teff-KLRG1 cells 
highly express CD44, which is commonly expressed in 
cancer stem cells and is related to cancer development 
and metastasis. CD27, which is involved in T-cell activa -
tion and B-cell immunity [45], is also highly expressed in 
Teff-KLRG1. KEGG and GSEA analyses were performed 
to measure alterations in Teff-KLRG1 cell functions 
after combined therapy, and the results revealed that 
“antigen presenting and presentation” was significantly 
enhanced in PTs; however, immune-related pathways 
such as the “B-cell receptor signaling pathway” , “natural 
killer cell-mediated cytotoxicity” , the “NF-kappa B sign -
aling pathway” , “neutrophil extracellular trap formation” , 
and “primary immunodeficiency” were inhibited after 
combined therapy. In addition, some hallmark pathways, 
such as the “PI3K-Akt signaling pathway” , “Hippo signal-
ing pathway” , “small cell lung cancer” , and “WNT signal-
ing pathway” , were also inhibited in PTs. These findings 
indicate a controversial role of Teff-KLRG1 cells in the 
TME (Fig.  4I, Figure S6J). ZNF683-high CD8 + T cells 
are associated with antitumor immunity following PD-1 
blockade [46], and we also assessed the function of Teff-
ZNF683-high T cells by analyzing the upregulated genes. 
Teff-ZNF683 cells highly expressed T-cell receptors 
(TRAC, TRBC1), killer cell lectin-like receptor subfam -
ily genes (KLRD1, KLRK1), PIK3R1, FOS, and MAPK1, 
and the upregulated genes were enriched in the “antigen 

Page 18 of 33Cui et al. Molecular Cancer          (2025) 24:111 
processing and presentation” , “MAPK signaling” , “natural 
killer cell-mediated cytotoxic” , “PD-L1 expression and 
PD-1 checkpoint pathway in cancer” , and “T-cell recep -
tor signaling pathway” pathways (Fig.  4J). KEGG analysis 
was also performed to evaluate the functional enrich -
ment of the DEGs in Teff-ZNF683 cells, and the results 
revealed the top 10 upregulated and downregulated path-
ways. The “antigen processing and presentation” pathway 
was enhanced, whereas the “natural killer cell-mediated 
cytotoxic” and “B-cell receptor signaling pathway” path -
ways were inhibited after PD-1 blockade (Fig.  4K). These 
findings indicated that Teff-ZNF683 cells switched to 
an inactivated and antigen-presenting phenotype after 
immunotherapy.
To investigate the differentiation paths of CD8 + T 
cells, the RNA velocity was used to construct a dynamic 
model of cell differentiation (Figure S6K). Next, we used 
Monocle 2 and Slingshot to perform the cell develop -
mental trajectory analysis. Monocle 2 identified 5 states 
and two major branches, which started from naïve cells, 
and the exhausted cells were located at the ends of both 
branches (Fig.  4L, M). From the branch node, the cell 
trajectory went in two different directions: one direction 
was differentiation to effector cells, mainly GZMA high 
effectors, and the other path direction was to memory 
cells, including Trm-ZNF683 high and ZNF683low cells 
(Fig.  4N, Figure S6L to S6O). The differentiation trajec -
tory of TNs and PTs suggested a significant improvement 
in the progression of cell development following neoad -
juvant therapy (Fig.  4O, P). Slingshot revealed three dif -
ferent lineages of CD8 + T cells (Figure S6P): lineage 1 is 
from Naïve, goes through Teff-KLRC1 and Trm-ZNF683 
low, and ends at exhausted; lineage 2 starts from Naïve 
and goes through Teff-KLRG1 high, Teff-GZMA high 
and ends at exhausted; lineage 3 starts from Naïve and 
goes through Teff-KLRC1, Trm-ZNF683 low and ends 
at Trm-ZNF683 high. The cell trajectory identified by 
Slingshot supported the differentiation model identi -
fied by monocle 2. Having established the cell trajectory 
of CD8 + T cells, we then investigated the genes cor -
related with cell development. The genes were grouped 
into 5 clusters according to their expression trends, and 
the top 10 genes in each cluster are shown by a heatmap 
(Figure S6Q). The genes within the gene set cluster 2, 
whose expression increased with increasing pseudotime, 
presented a pattern of change that was consistent with 
the differentiation of CD8 + T cells. The genes in cluster 
2 were enriched in pathways related to TCR signaling, 
NF-kB signaling, TNF signaling, HIF-1 signaling, TGF-
beta signaling, the cell cycle, and P53 signaling. Next, we 
analyzed the genes correlated with different developmen-
tal fates of CD8 + T cells. There are two major branches 
of the trajectory: branch 1 ends at the state of exhausted 
and memory T cells (states 2 to 1), whereas branch 2 ends 
at the state of exhausted and effector T cells (states 2 to 
4). We identified 1764 genes that correlated with the two 
major developmental branches, and the top 60 genes are 
shown in Fig.  4Q. Notably, with respect to cell fate from 
naïve cells to effectors, upregulated genes were enriched 
in “cytokine‒cytokine receptor interaction” , “T-cell recep-
tor signaling pathway” , “Th17 cell differentiation” , “natural 
killer cell-mediated cytotoxicity” , and “PD-L1 expression 
and the PD-1 checkpoint pathway in cancer” , suggesting 
that the CD8 + T cells developed a cytotoxic and acti -
vated phenotype.
Next, we studied the spatial distribution of CD8 + T-cell 
subtypes, and neighboring analysis was subsequently 
performed to assess the spatial distance between 
CD8 + T-cell subtypes and other major cell types, includ -
ing cancer cells, B-plasma cells, CAFs, and macrophages 
(Figure S6R). However, the results revealed no positive 
neighboring relationships between CD8 + T cells and the 
other cell types The RCTD algorithm was employed to 
annotate the coordinates of CD4 + T cells and CD8 + T 
cells in the section slides to visualize the distribution of 
T lymphocytes in the four NSCLC sections (Fig.  4R). 
The proportions of CD8 + T cells and CD8 + effector 
cells in each section were subsequently calculated, and 
the results revealed significant enrichment of CD8 + T 
cells and CD8 + effector cells in tumor-2 (pCR) tumors, 
followed by tumor-3 (responder) tumors (Fig.  4S, Figure 
S6S). The sections were then subgrouped into respond -
ers (tumor-2 and tumor-3) and non-responders (tumor-1 
and tumor-4), and not surprisingly, the fractions of 
CD8 + T cells and CD8 + effectors were significantly ele -
vated in the responders (Figure S6T, Figure S6U). These 
results from four NSCLC tumor sections suggested that 
the infiltration level of CD8 + T cells was correlated with 
the responsiveness to chemoimmunotherapy in NSCLC 
patients.
Anti‑PD‑L1 therapy increased the infiltration 
of IgG + plasma cells and enhanced the communication 
between plasma cells and CAFs/macrophages
Tumor-infiltrating B cells are important components of 
the TME, and the activation of TIBs has been shown to 
be involved in the immune checkpoint inhibitor response 
in NSCLC. To further clarify the effects of chemoim -
munotherapy on B-cell differentiation and activation, 
we identified a total of 12,823 B cells via scRNA-seq and 
recustered them into 5 subpopulations, including naïve 
B cells (TCL1A, IL4R, CD200, YBX3, FCER2), germinal 
center B cells (MYBL1, RGS13, SUGCT, MEF2B, SER -
PINA9), plasma cells (IGHV3–29, IGHV2–5, IGKV1–
39, IGKV1–17, IGLV1–47), memory B cells (NR4A2, 
DNAJA1, NR4A1, CD83, DUSP2) and follicular B 

Page 19 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
cells (TMPO, ARHGEF18, H1–4, ALOX5, RALGPS2) 
(Fig.  5A, Figure S8A to S8D). The immunoglobin (Ig) 
isotypes were inferred via single-cell B cell receptor 
sequencing (scBCR-seq), and 4 antibody isotypes were 
detected, namely, IgA, IgG, IgD, and IgM (Fig.  5B). In 
addition, the antibody isotypes in each B-cell subcluster 
were analyzed via scBCR-seq. The naïve B-cell cluster 
was dominated by the IgM isotype, the germinal center 
B cell (GCB) and plasma cell clusters presented high 
enrichment of the IgG isotype, and the memory B-cell 
and follicular B-cell subtypes presented different isotypes 
(Fig.  5C). The percentages of B-cell subclusters in each 
sample and subgroup were also analyzed, and the results 
suggested a significant decrease in the plasma cell sub -
type after combined therapy, whereas the memory B-cell 
subtype tended to increase in the PT group (Fig.  5D, E). 
The ratios of antibody isotypes between subtypes were 
also compared, which revealed that the enrichment of 
the IgG isotype decreased after therapy, which was con -
sistent with the dynamics of plasma B cells, as IgG is the 
dominant antibody isotype in plasma cells (Fig.  5F). The 
DEGs in B-cell subclusters between TNs and PTs were 
analyzed, and the top 5 upregulated genes in the PT 
group were identified (Figure S8E, Table S9). ScBCR-seq 
was also performed to evaluate the colony diversity and 
expansion of B cells; however, no positive findings were 
detected in B cells between the TN and PT groups (Fig -
ure S8F to S8I).
Next, we aimed to perform an in-depth analysis of the 
differentiation of B cells. We first constructed the dif -
ferentiation trajectory of B cells via Monocle 2, and the 
results revealed that cellular differentiation started with 
naïve B cells and progressed in two different branching 
directions, ending with memory B cells and plasma B 
cells, respectively, and three different cellular differen -
tiation states were obtained (Fig.  5G). Monocle 3 yielded 
a more complex cellular differentiation trajectory but 
broadly supported the results of Monocle 2, suggesting 
that cells differentiated from naïve B cells in two distinct 
directions, i.e., toward plasma cells and memory B cells, 
and that follicular B cells are basically located at the inter-
section of the branches involved in cellular differentiation 
(Fig.  5H, I). The cell differentiation trajectory map con -
structed by monocle 3 revealed the differentiation posi -
tions of the TIBs subpopulations over pseudotime, with 
the majority of memory B cells and a small proportion of 
plasma cells at the end of the pseudotemporal trajectory, 
whereas CytoTRACE analyses revealed that plasma cells 
presented a greater degree of cell differentiation (Fig. 5J).
Having constructed the cell differentiation trajec -
tory, we first analyzed the genes that exhibited dynamic 
changes with the progression of pseudotime (Figure S8J). 
The genes were grouped into 3 clusters according to their 
dynamic changes in expression. The cell cycle and DNA 
damage regulators CDKN1A and CKS2 and the acti -
vation marker for antigen-presenting CD83 cells were 
highly expressed at the root of the pseudotemporal tra -
jectory, and the MHC-related genes HLA-B and HLA-
DOB and the immunoglobin genes, mainly the IGKV 
cluster, were highly expressed in the middle of the trajec -
tory. We further investigated the genes correlated with 
two major developmental branches of B cells (Fig.  5K). 
Branch 1 is from state 3 to state 1, and memory B cells are 
located at the end of the path. Branch 2 spans from state 
3 to state 2, indicating that the cell differentiated from 
naïve B cells to plasma cells. The genes associated with 
(See figure on next page.)
Fig. 5 In response to anti-PD-L1 therapy, increased infiltration of IgG + plasma cells and enhanced communication between plasma cells and CAFs/
macrophages were detected. A Reclustering of B cells into 5 subpopulations shown in the UMAP plot, colored by subtype. B UMAP showing 
the distribution of antibody isotypes identified by scBCR-seq, colored according to different antibody isotypes. C Bar plot showing the percentages 
of different antibody isotypes in B-cell subtypes. D The percentages of B-cell subtypes in each sample and group. E Box plot showing 
the comparison of the fractions of CD4 + T-cell subtypes between the TN and PT (Wilcoxon, * indicates P < 0.05). F Box plot showing the comparison 
of the percentages of antibody isotypes between TNs and PTs (Wilcoxon, * indicates P < 0.05). G The developmental trajectory of B cells from all 
samples colored with pseudotime; the color from light to dark indicates the progression of pseudotime (upper). The differentiation trajectories 
of B-cell subtypes (middle) and differentiation states (lower) are labeled with different colors. The numbers on the trajectory tree indicate the branch 
nodes, and the differentiation tree was divided into 2 branches. H t-SNE plot showing the B cells colored according to pseudotime, inferred 
by monocle 3. I t-SNE map showing the distribution of B cells of different subtypes inferred via monocle 3. J UMAP plot showing the differentiation 
of B cells according to pseudotime (left) or the CytoTRACE score (right), inferred by monocle 3 or CytoTRACE. The memory B cells and plasma B 
cells are labeled with black dotted lines. K Pseudo-heatmap showing the significant genes correlated with the differentiation of B cells from stage 
3 to stage 1 (from naïve to memory) and from stage 3 to stage 2 (from naïve to plasma). The genes were subjected to 5 clusters, and the top 10 
genes correlated with pseudotime in each cluster are shown, with the selected KEGG pathways enriched in each gene cluster labeled on the left. L 
Spatial annotation of B-cell subtypes, tumor cells, macrophages, T cells, Endos, and CAFs in 4 NSCLC tumor sections inferred via the RCTD algorithm. 
The white dotted lines indicate the TLS region, and the TLS regions were labeled TLS-1 to TLS-4. M Heatmap showing the neighboring relationships 
between B-cell subtypes and tumor cells, macrophages, T cells, Endos, and CAFs in each NSCLC section. The white dotted line represents the pair 
of plasma B-CAFs, which shows significant changes in spatial distance with increasing sensitivity to chemoimmunotherapy. The number on the bar 
indicates the number of cells that have neighboring relationships

Page 20 of 33Cui et al. Molecular Cancer          (2025) 24:111 
cell differentiation were grouped into 5 clusters according 
to the dynamic changes in gene expression. The cluster 2 
genes, including the NF-kB signaling genes NFKB1 and 
RELB and chemokines and chemokine receptors such 
as CXCL8, CCL3, and CXCR5, were highly expressed at 
the end of branch 1. The cluster 3 genes were correlated 
with the developmental trajectory of plasma B cells, and 
KEGG analysis suggested that the genes were signifi -
cantly enriched in the BCR signaling, NF-kB signaling, 
natural killer cell-mediated cytotoxicity, and neutrophil 
extracellular trap formation pathways, indicating an acti -
vated phenotype of B cells. In addition, cluster 5 genes, 
which were highly expressed at the end of the trajectory 
of plasma cells, were enriched in the pathways “non-
small cell lung cancer” (GADD45A, GADD45B, KRAS, 
PIK3CA, PIK3CB, and FOXO3) and “PD-L1 expression 
and PD-1 checkpoint pathway in cancer” (EGFR, FOS, 
Fig. 5 (See legend on previous page.)

Page 21 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
JUN, and HIF1A). The overexpression of oncogenes 
might enhance tumor proliferation and immune evasion.
To analyze the spatial distribution and proximity of B 
cells to other major cell types in NSCLC tissue sections, 
we performed spatial annotation and neighboring analy -
sis of B-cell subpopulations, as well as malignant epithe -
lial cells, macrophages, CAFs, and T cells, in 4 NSCLC 
tissue sections via the RCTD algorithm. The infiltration 
of plasma cells and follicular B cells was markedly ele -
vated in pCR (tumor-2) and responder (tumor-3) tissues, 
whereas it was nearly undetectable in nonresponder tis -
sues (tumor-1 and tumor-4) (Fig. 5L). This finding is con-
sistent with the reported results that high infiltration of 
B cells predicts better responsiveness to immune block -
age therapy [47–49]. In addition, we detected a high pro -
portion of follicular B cells within the TLS structures. In 
TLS-3, a high diversity of B cells, including naïve B cells, 
GCBs, plasma B cells, and follicular B cells, was observed. 
Neighboring analysis suggested that plasma cells notably 
colocalized with CAFs and macrophages in the tumor tis-
sues of responders but not in those of non-responders. 
We analyzed the antibody isotypes in the four NSCLC 
sections and found that only the IgG isotype showed 
the highest intensity in the pCR section (tumor-2) (Fig -
ure S8K). Next, we further analyzed the intensity of the 
antibody isotypes in the pCR section and found that the 
intensity of IgM isotype significantly overlapped with that 
of the TLS structures, whereas that of IgG isotype over -
lapped with that of plasma cells (Figure S8L), which sug -
gests that plasma cells of the IgG isotype show significant 
tissue infiltration with increased sensitivity to ICB ther -
apy, whereas B cells in the TLSs are predominantly of the 
IgM isotype. Neighboring analysis demonstrated notable 
colocalization between plasma cells (mainly IgG + plasma 
cells) and CAFs/macrophages in responders, indicating 
that the infiltration of IgG + plasma cells and neighbor -
ing relationships with CAFs and macrophages might sug-
gest a positive response to anti-PD-L1 therapy (Fig.  5M). 
In contrast, evidence suggests that the co-occurrence of 
IgA plasma cells and CAFs/macrophages in lung adeno -
carcinoma supports an immunosuppressive TME [50]. 
In addition, the occurrence of follicular B cells (mainly 
the IgM isotype) was found to be associated with the for -
mation of TLSs, and were localized in the center of TLS 
regions.
Since we found that plasma cells colocalized with 
CAFs/macrophages in positive responders to chemoim -
munotherapy, we then performed a cell‒cell interaction 
analysis to investigate alterations in cell communication 
patterns after chemoimmunotherapy by using CellChat. 
The relative pathways related to the information flow 
between the cell types in TNs and PTs are shown in a bar 
plot (Figure S8M, Table  S10), which demonstrated that 
pathways such as MHC-II, GAS, and SPP1 were signifi -
cantly enriched before therapy; however, the communi -
cation pathways of IL-16, MHC-I, CXCL, and MIF were 
notably enhanced after therapy (Figure S8N). In addition, 
pathways including the IGF, CSF, and VCAM pathways 
were distinct in the PT group, suggesting newly estab -
lished communication patterns between the cell types.
Chemoimmunotherapy notably changed the proportions 
of CXCL9 and SPP1 macrophages and enhanced 
the infiltration of TAMs in the NSCLC TME
To investigate the heterogeneity of myeloid cells exten -
sively, 5725 myeloid cells were clustered into 11 sub -
populations, among which 8 subtypes were Mφs, 2 were 
dendritic cells (DCs), and 1 was a monocyte cell subtype 
(mono-CX3CR1) (Fig.  6A, Figure S9A, Figure S9B, and 
Figure S9C). The fractions of the cell subpopulations 
in each sample and group were analyzed (Figure S9D). 
Among the myeloid cells, we focused on the heterogene -
ity and functions of Mφ subpopulations in the TME, as 
the crucial role of Mφ in the inflammatory response and 
antitumor immunity has been firmly established; addi -
tionally, Mφ constitute the majority of myeloid cells in 
our data. The classical marker gene was used to catego -
rize Mφs into 8 distinct subpopulations: Macro-ISG15, 
Macro-SELENOP , Macro-CXCL9, Macro-CXCL2, 
Macro-SPP1, Macro-MCEMP1, and Macro-proliferating. 
The macro-MCEMP1 subtype comprises tissue-resi -
dent alveolar macrophages (AMs), as it highly expresses 
canonical AM markers (MCEMP1 and MARCO). In con-
trast, other Mφ subtypes were identified as tumor-associ-
ated macrophages (TAMs). Mφ-SPP1 has been reported 
to be involved in tumor angiogenesis and immune escape 
[51, 52]. Our findings revealed that Mφ-SPP1 cells highly 
expressed numerous oncogenes, including GRB2, ENO1 
and SLC3A2. Additionally, KEGG analysis indicated 
that this subcluster may be involved in oncogenic signal -
ing pathways, such as the mTOR signaling pathway, the 
HIF-1 signaling pathway and the ferroptosis pathway. 
Mφ-SELENOP reportedly has anti-inflammatory func -
tions [53]. Mφ-CXCL9 highly expresses proinflammatory 
chemokines such as CXCL9 and CXCL10, which attract 
T cells and NK cells through their antigen-presenting 
capacity. Mφ-ISG15 highly expresses the interferon-
responsive factor ISG15, suggesting that it may act as a 
proinflammatory and antigen-presenting agent by acti -
vating the interferon signaling pathway. Mφ-CXCL2 cells 
play a role in the induction of neutrophil aggregation 
via the CXCL2-CXCR2 pathway [54, 55]. Furthermore, 
CXCL2 is involved in the crosstalk between macrophages 
and other immune cells, as well as between macrophages 
and tumor cells [56]. Mφ-proliferating cells are known 

Page 22 of 33Cui et al. Molecular Cancer          (2025) 24:111 
to highly express genes related to the cell cycle and DNA 
replication, such as MKI67 and CDKN3.
To further elucidate the function of macrophage sub -
types and the impact of combination therapy on mac -
rophage function and polarization trends, we conducted 
a comprehensive analysis of the M1 and M2 phenotypes, 
angiogenesis signatures, and phagocytosis signatures 
(Fig. 6B, Table S11) of the macrophages as a whole [57], 
as well as of individual subpopulations. Additionally, we 
examined the alterations in these functions between the 
TN and PT groups. We found that the M1 signature of 
macrophages was significantly elevated in the PT group, 
whereas the M2 signature was significantly decreased 
in the PT group. In addition, both the angiogenesis 
and phagocytosis signatures of macrophages were sig -
nificantly decreased in the PT group. The functions of 
individual macrophage subpopulations were analyzed, 
and the phagocytosis signatures of Mφ-SELENOP and 
Mφ-ISG15 were significantly greater than those of the 
other subpopulations (Figure S9E, Figure S9F). Fur -
thermore, almost all the TAMs, with the exception of 
Mφ-CXCL9, presented higher M2 signatures, particu -
larly Mφ-SPP1, Mφ-SELENOP and Mφ-ISG15. The 
results of the aforementioned analysis demonstrated that 
Mφ-SPP1, Mφ-SELENOP and Mφ-ISG15 exhibited a 
more pronounced trend toward M2 polarization and are 
likely to be involved in tumor progression and metasta -
sis as pro-oncogenic factors. Furthermore, CXCL9 mac -
rophages display cytokine secretion characteristics that 
may be involved in antigen presentation, as well as anti-
inflammatory or antitumor immunity. More importantly, 
we examined the difference in the fractions of myeloid 
cells between the TN and PT groups and discovered 
that the proportion of Mφ‒CXCL9 cells was markedly 
elevated in the PT group (Fig.  6C), substantiating the 
hypothesis that combination therapy markedly enhances 
the antigen-presenting and immune-activating functions 
of macrophages in the TME. KEGG analysis revealed 
that CXCL9 macrophages highly expressed chemokines, 
proinflammatory factors and MHC genes and were 
involved in immune-related signaling pathways such as 
the “chemokine signaling pathway” , “antigen processing 
and presentation” , “TNF signaling pathway” , and “IL-17 
signaling pathway” (Fig.  6D). Furthermore, DEGs of each 
cell subpopulation between TNs and PTs were analyzed 
(Figure S9G, Table S12), and KEGG analysis of the DEGs 
in Mφ-CXCL9 between TNs and PTs suggested that 
most cellular functions, including “antigen processing 
and presentation” , “IL-17 signaling pathway” , “TNF sign-
aling pathway” , and “toll-like receptor signaling pathway” 
(Fig. 6E), were enhanced, indicating that the characteris -
tic functions of Mφ-CXCL9 macrophages were further 
activated after chemoimmunotherapy.
To provide further clarification regarding the differ -
entiation trajectories of the macrophage subpopula -
tions, we employed Monocle 2 software to construct 
a tree of macrophage differentiation (Fig.  6F, G). Our 
analysis indicated that the cellular differentiation tra -
jectory started with Mφ-MCEMP1 and subsequently 
exhibited two principal differentiation branches, 
with Mφ-SPP1 in the beginning, Mφ-ISG15 and 
Mφ-proliferating near the first branch point, ending 
with Mφ-CXCL9 and Mφ-CXCL2, and Mφ-SELENOP , 
respectively (Fig.  6H). In addition, developmental tra -
jectory analysis revealed five different cell differen -
tiation states. The cell differentiation trajectories were 
Fig. 6 Chemoimmunotherapy notably changed the proportions of CXCL9 and SPP1 macrophages and enhanced the infiltration of TAMs 
in the NSCLC TME. A Reclustering of myeloid cells into 11 subpopulations, as shown by the t-SNE plot. B Violin plots comparing the M1 signature, 
M2 signature, angiogenesis signature, and phagocytosis signature of all macrophages between the TN and PT groups (P values from Wilcoxon 
tests). C Box plot showing the comparison of the fractions of macrophage subtypes between TNs and PTs (Wilcoxon, * indicates P < 0.05, ** 
indicates P < 0.01). D The top 20 KEGG pathways enriched with the upregulated genes in the CXCL9 + macrophage subtype (adjusted P < 0.05). 
E Bubble plot showing the top 20 KEGG pathways enriched with the DEGs from the CXCL9 + macrophage subtype between the TN and PT 
groups. Each bubble indicates a signaling pathway (left), and the top 20 pathways associated with the relative bubbles are labeled, as listed 
in the right panel. F The developmental trajectory of the macrophages from all the samples colored according to pseudotime; the color 
from light to dark indicates the progression of pseudotime. G The developmental trajectory of B cells according to their differentiation state. 
H The differentiation trajectory of all the macrophage subtypes; the subtypes are labeled with different colors. The numbers on the trajectory 
tree indicate the branch nodes, and the differentiation tree was divided into 4 branches. J The pseudo-heatmap showing the significant genes 
correlated with the differentiation of macrophages. The genes were subjected to 5 clusters, and the top 10 significant genes are shown. I Spatial 
annotation of macrophage subtypes, tumor cells, NK cells, T cells, and CAFs in 4 NSCLC tumor sections inferred via the RCTD algorithm. J The 
percentages of indicated cell types in 4 NSCLC tumor sections were calculated and shown by bar plot. K Violin plots showing the proportions 
of SPP1 (left), CXCL9 (middle) and SELENOP (right) macrophages in non-responders and responders. Each spot is considered as a duplicate, and P 
values were determined by two-sided Wilcoxon rank-sum test. L Heatmap showing the neighboring relationships between macrophage subtypes 
and tumor cells, NK cells, T cells, and CAFs in each NSCLC section. The pairs of cells that show significant changes in spatial distance with increasing 
sensitivity to chemoimmunotherapy are within the white dotted line. The number on the bar indicates the number of cells that have neighboring 
relationships. Multiple immunofluorescence (mIHC) staining of the macrophage subpopulations, SPP1 and CXCL9, and tumor cells in NSCLC tissue 
sections from the TN (M) and PT (N) groups. The scale bar represents 100 μM
(See figure on next page.)

Page 23 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
demonstrated for each subgroup, and the distribution 
of cells in the PT group exhibited notable progression 
toward the branch ends (Figure S9H, S9I). These find -
ings suggest that the combination treatment facilitated 
the differentiation process of macrophages toward 
Mφ-CXCL9 and Mφ-SELENOP . To validate the cell 
differentiation tree obtained from Monocle 2 analysis, 
a differentiation trajectory map of macrophages was 
constructed via Slingshot software (Figure S9J, Figure 
S9K). The results demonstrated that the starting point 
of cellular differentiation was observed in Mφ-MCEMP , 
which was in accordance with the initial stage identified 
by Monocle2 analysis. Furthermore, two distinct line -
age trajectories were identified for macrophages. The 
first lineage trajectory originated from Mφ-SELENOP 
and ended in Mφ-CXCL9. The second trajectory passed 
through Mφ-SPP1 and rooted in Mφ-proliferation. The 
cell trajectories predicted by Slingshot and Monocle 
Fig. 6 (See legend on previous page.)

Page 24 of 33Cui et al. Molecular Cancer          (2025) 24:111 
2 both originated from Mφ-MCEMP and ended with 
Mφ-CXCL9 as one of the terminations.
We also studied genes that exhibited dynamic expres -
sion with the development of macrophages, 1771 genes 
were identified to exhibit dynamic changes in line with 
cellular differentiation into different branches (Figure 
S9L). The genes were grouped into 5 clusters on the 
basis of changes in expression, and KEGG analysis was 
performed to study the functions enriched by the gene 
clusters. We found that during differentiation from state 
5 to state 1 (Mφ-CXCL9), the expression of chemokines 
and proinflammatory factors such as CXCL2, CXCL3, 
CXCL8, CCL3, CCL4, NFKBIA, TNFAIP3, HSPA1A, 
HSPA1B, and HSP90AA1 was significantly elevated. 
SELENOP was highly expressed with the trajectory 
from state 5 to state 4, indicating the differentiation of 
Mφ-SELENOP in that branch. In addition, during the 
cellular differentiation of Mφ-SELENOP , the expression 
of MHC genes and CD74 increased.
The RCTD algorithm was employed for the spatial 
annotation of macrophage subpopulations and other 
major cell subpopulations in NSCLC tissue sections 
(Fig.  6I). Tumor tissue 2 exhibited substantial infiltra -
tion of T cells, accompanied by a considerable number 
of Mφ-SELENOP subpopulations. In tumor tissue 3, a 
significant number of Mφ-SELENOP subpopulations 
were observed in proximity to malignant epithelial cells, 
along with T cells (Fig. 6J). The spatial data indicated that 
Mφ-SELENOP subpopulations constituted the major -
ity of all the macrophage subpopulations. The distri -
butions of CXCL9, SPP1, and SENELOP macrophages 
between responders and non-responders were also 
compared, and the level of SELENOP and CXCL9 cells 
was found to be dramatically increased in responders, 
while the level of SPP1 cells was decreased in respond -
ers (Fig.  6K). We conducted spatial neighboring analysis 
of macrophage subpopulations, T cells, NK cells, malig -
nant epithelial cells, and CAFs on the basis of spatial 
transcriptomic data from four NSCLC tissue sections. 
Mφ-SELENOP cells colocalized with CAFs, T cells and 
tumor cells, whereas in the pCR tissue, the cl-localization 
of Mφ-SELENOP cells and tumor cells disappeared as 
the number of tumor cells decreased (Fig.  6L). The spa -
tial colocalization of Mφ-SELENOP , CAFs, T cells, and 
tumor cells indicated the reconstruction of the TME in 
response to chemoimmunotherapy. To experimentally 
investigate the reshaping of macrophages in NSCLC 
tumors, we employed multiple immunofluorescence 
staining for the macrophage subpopulations SPP1 and 
CXCL9 in conjunction with malignant epithelial cells 
in NSCLC tissues with or without combined therapy 
(Fig. 6M, N). Our findings revealed a notable increase in 
the proportion of macrophages (CD68) in NSCLC tissues 
following combination therapy. Furthermore, the spatial 
localization of macrophages was markedly restricted to 
lung cancer tissues prior to immunotherapy. However, 
in lung cancer tissues following combination therapy, 
CXCL9 + SPP1 + macrophages were not only widely dis -
tributed but also more closely adjacent to tumor cells 
(PanCK).
Chemoimmunotherapy reshaped the TME by changing 
the proportion of matrix CAFs and inflammatory CAFs 
and enhancing the activity of antigen‑presenting CAFs
Cancer-associated fibroblasts (CAFs) are highly impor -
tant within the microenvironment of solid tumors and 
are closely associated with tumor growth, metastasis and 
responsiveness to immunotherapy. A total of 2801 fibro -
blasts were obtained from 12 NSCLC patients, which 
were then divided into 5 subsubpopulations on the basis 
of classical marker genes, namely, antigen-presenting 
CAFs (apCAFs), inflammatory CAFs (iCAFs), matrix 
CAFs (mCAFs), metabolic CAFs (meCAFs) and prolifer -
ative CAFs (pCAFs) (Fig.  7A). The marker genes of each 
fibroblast subsubpopulation are presented, and the Kyoto 
Encyclopedia of Genes and Genomes (KEGG) method 
was used to analyze the differentially upregulated genes 
of the subsubpopulations to identify their biological 
functions (Fig.  7B). Furthermore, the proportions of 
each fibroblast subpopulation in different samples and 
subgroups were analyzed (Fig.  7C, Figure S10A). The 
results demonstrated that the proportion of apCAFs was 
significantly lower in the PT group than in the control 
group, whereas the proportion of meCAFs was signifi -
cantly greater. These findings suggest that the combined 
therapy significantly altered the distribution and function 
of the fibroblast population in the tumor microenviron -
ment and that these changes might be associated with 
immunotherapy responsiveness. In contrast, a greater 
proportion of iCAFs was observed in PA10 samples (pCR 
sample), indicating that iCAFs may play a role in tissue 
reconstruction following tumor necrosis.
We next investigated the functions of CAF subclusters 
(Fig.  7B). mCAFs highly expressed ECM-related genes 
and were found to be associated with ECM-receptor 
interactions and the TGF-beta signaling pathway. iCAFs 
expressed proinflammatory genes, and KEGG analysis 
suggested that the genes whose expression was upregu -
lated in iCAFs were enriched in “Pathways in cancer” , 
“Small cell lung cancer” , and “PI3K-Akt signaling path -
way” , indicating an oncogenic role of iCAFs. KEGG 
analysis revealed that “DNA replication” , “cell cycle” , 
and “cell senescence” were enriched with the marker 
genes of pCAFs. Furthermore, the GSVA method was 
employed to conduct a comparative analysis of the func -
tional enrichment of the five subpopulations of CAF cells 

Page 25 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
Fig. 7 Chemoimmunotherapy reshaped the TME by changing the proportion of matrix CAFs to inflammatory CAFs and enhancing the activity 
of antigen-presenting CAFs. A Reclustering of cancer-associated fibroblasts into 8 subpopulations shown by a t-SNE plot (upper), the distribution 
of CD4 + T cells in each sample (lower left), and the treatment-naïve and posttreatment groups (lower right). B Heatmaps showing the significantly 
upregulated genes in all CAF subclusters. C Box plot showing the comparison of the fractions of CD4 + T-cell subtypes between TNs and PTs 
(Wilcoxon, * indicates P < 0.05, ** indicates P < 0.01). D Volcano maps showing the DEGs in bulk CAFs, apCAFs, and meCAFs, and the top 10 
DEGs are labeled. E Violin plots comparing the antigen-presentation gene signatures of CAFs in the TN and PT groups (P values from Wilcoxon 
tests). F Spatial annotation of CAF subtypes, tumor cells, macrophages, and T cells in 4 NSCLC tumor sections inferred via the RCTD algorithm. G 
The percentages of each cell type identified in the NSCLC sections. H Heatmap showing the neighboring relationships between CAF subtypes 
and tumor cells, T cells, and macrophages in each NSCLC section. The pairs of cells that show significant changes in spatial distance with increasing 
sensitivity to chemoimmunotherapy are within the white dotted line. The number on the bar indicates the number of cells that have neighboring 
relationships. I Violin plots showing the proportions of apCAFs (left), mCAFs (middle) and iCAFs (right) in non-responders and responders (P value). 
J Violin plots showing the proportions of apCAFs (left), mCAFs (middle) and iCAFs (right) in non-responders (NMPR patients, n = 3) and responders 
(MPR and pCR patients, n = 3), data from scRNA-seq (P values determined by Wilcoxon tests). Signature scores of apCAFs (K), iCAFs (L) and mCAFs 
(M) in each NSCLC section were calculated and inferred by heatmaps. Light green color indicates high score, dark blue color indicates low score

Page 26 of 33Cui et al. Molecular Cancer          (2025) 24:111 
(Figure S10B). This analysis revealed that iCAFs were sig-
nificantly enriched in the Notch pathway and the angio -
genic pathway. In contrast, mCAFs were significantly 
enriched in the WNT pathway and EMT pathway. Addi -
tionally, apCAFs were significantly enriched in the PI3K-
Akt pathway. pCAFs were enriched in genes related to 
the cell cycle, mitosis, and DNA damage repair. The most 
functionally distinctive meCAFs were found to be signifi -
cantly enriched in proinflammatory pathways, including 
the chemokine and interferon pathways, as well as in the 
EMT and TGF-beta pathways.
Furthermore, the genes differentially expressed in sub -
populations of CAFs between the TN and PT groups 
were analyzed to evaluate the effects of combination 
therapy on cellular function. Our findings revealed 995 
upregulated genes and 2313 downregulated genes in 
CAFs, 1191 upregulated genes and 633 downregulated 
genes in apCAFs, and 128 upregulated genes and 255 
downregulated genes in meCAFs (Fig.  7D). The upregu -
lated genes in each CAF subcluster in the PT group are 
shown in bubble plots (Figure S10C, Table S13). Further -
more, the antigen processing and presentation signa -
tures of apCAFs were analyzed, and the results revealed 
that apCAFs in the PT group presented significantly 
enhanced antigen-presenting function (Fig. 7E). We eval-
uated the changes in the biological functions of the CAF 
subclusters by analyzing the DEGs via KEGG analysis. 
The enrichment results revealed a diversity of pathways 
related to the DEGs, and we identified several of these 
pathways. The results of the KEGG analysis revealed that 
the pathways associated with TNF signaling, p53 signal -
ing, NOD-like receptor signaling, apoptosis, and TGF-
beta signaling were increased in apCAFs but inhibited in 
the cell cycle, non-small cell lung cancer, and notch sign -
aling pathways (Figure S10D). The expression of meCAFs 
was found to be increased in pathways related to protein 
export, the proteasome, and oxidative phosphorylation 
and inhibited in pathways related to the spliceosome, pro-
tein processing in the endoplasmic reticulum, and ther -
mogenesis (Figure S10E). In addition, iCAFs inhibited 
several hallmark pathways, such as the TGF-beta signal -
ing, WNT signaling, Hippo signaling, and mTOR sign -
aling pathways, suggesting the transition of iCAFs to an 
antitumor phenotype (Figure S10F). GSEA revealed sev -
eral pathways related to the immune response; however, 
the pathways associated with natural killer cell-mediated 
cytotoxicity, BCR signaling, neutrophil extracellular trap 
formation, NF-kB signaling apCAFs and meCAFs were 
inhibited in apCAFs and meCAFs after combined ther -
apy (Figure S10G, Figure S10H).
To elucidate the interrelationship between CAF sub -
populations and other key cell types in tissue sections, 
we spatially mapped the CAF subpopulations with 
malignant epithelial cells, macrophages, and T cells 
via the RCTD algorithm (Fig.  7F, G) and performed a 
neighboring analysis to evaluate the spatial relationships 
between the cells (Fig.  7H). As immunotherapeutic sen -
sitivity increases (from nonresponder to pCR), apCAFs 
co-localized with macrophages (mostly SELENOP-mac -
rophages), accumulated in tumor boundaries and infil -
trated within tumor regions, indicating the cooperative 
roles of apCAFs and SELENOP-macrophages in the anti-
tumor activity induced by immunotherapy. In addition, 
with the deceasing of malignant areas, iCAFs were found 
to be accumulated in the non-malignant areas. Further -
more, matrix CAFs had the closest spatial relationships 
with tumor cells in the nonresponder region, especially 
in tumor-4, which exhibited the worst response in all the 
ST samples. These findings indicate that matrix CAFs 
might support an immunosuppressive TME, while iCAFs 
were aggregated in non-tumor regions. Next, propor -
tions of CAFs subclusters between responders and non-
responders were analyzed, and results showed that the 
levels of iCAFs and meCAFs were significantly increased 
in responders, however the levels of apCAFs, mCAFs and 
pCAFs were notably decreased in responders (Fig. 7I, Fig-
ure S10I, Figure S10J). Data from scRNA-seq suggested 
an elevation of iCAFs and a decrease in the proportion 
of mCAFs in responders (Fig.  7J). We scored the distri -
butions of apCAFs (Fig.  7K), iCAFs (Fig.  7L) and mCAFs 
(Fig.  7M) in each NSCLC section, and the results dem -
onstrated that apCAFs and iCAFs mostly aggregated in 
non-malignant areas, while mCAFs were widely distrib -
uted in malignant areas, which further supported their 
roles in the TME. mCAFs were more correlated with an 
immunosuppressive microenvironment and an unfa -
vorable sensitivity to immunotherapy, while iCAFs were 
accumulated in an immune activated and non-malignant 
areas, suggesting its critical role in TME reconstruction 
after immunotherapy.
Effective chemoimmunotherapy enhanced the cell–cell 
communications between SELENOP‑macrophages, apCAFs 
and T cells in NSCLC tumor microenvironment
As demonstrated in the former analyses, there is a signifi-
cant enrichment of SELENOP macrophages and apCAFs 
in immunotherapy-sensitive tissues at the tumor bound -
aries, as well as in non-tumor tissues, and these cells 
demonstrate significant spatial co-localization relation -
ships. Furthermore, the proportion of SELENOP mac -
rophages is significantly increased after immunotherapy. 
We therefore hypothesized that SELENOP macrophages 
and apCAFs play an important role in immunotherapy-
induced immune activation and immune cell recruit -
ment. Next, we investigated the cell–cell communication 
patterns between SELENOP macrophages, apCAFs, and 

Page 27 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
T cells in responders and non-responders basing on the 
data from spatial transcriptomic analysis, in order to 
find out how these cells interact with each other when 
responding to chemoimmunotherapy.
CD4 + and CD8 + T cells were re-clustered by cellular 
functions. CD4 + T cells were re-clustered into Helper, 
Memory, Naïve and Treg, and CD8 + T cells were re-
clustered into Effector, Exhausted, Memory and Naïve. 
RCTD algorithm was employed to annotate the T cell 
subclusters, apCAFs and SELENOP-macrophages on 
each section, and neighboring analysis was subsequently 
performed on these three groups of cells. Results demon -
strated no significant co-localization between T cells and 
other two cell types in non-responders, while in respond-
ers CD4 + memory and Naïve cells showed some spatial 
correlation with apCAFs and SELENOP-macrophages 
(Fig.  8A, B). We next investigated the cell–cell commu -
nication patterns by using CellPhoneDB algorithm, and 
the results demonstrated that the T cell subcluster that 
communicated with SELENOP macrophages as well 
as apCAFs in the non-responder was CD4 + memory 
cells. In responders, a variety of T cell clusters were 
observed to communicate with SELENOP macrophages 
and apCAFs, including CD4 + Helper, CD4 + Naïve and 
CD8 + Naïve T cells. This finding suggests that effective 
immunotherapeutic responses strengthened the com -
munications between T cells and these two cell types. 
(Fig.  8C). The differential signaling pathways connected 
T cells, SELENOP-macrophages and apCAFs between 
responders and non-responders were analyzed, and the 
top 20 pathways in each group were shown by a bar plot 
(Fig. 8D, Table S14).
We next investigated the outgoing and incoming 
signaling patterns in the communication network of 
T cells, SELENOP-macrophages and apCAFs. The 
results showed that the variety of communication pat -
terns in this network was significantly increased in 
responders, as the the outgoing and incoming signals 
from and into CD8 Naïve T cells were significantly 
enhanced (Fig.  8E, F). In addition, in non-responders, 
CD4 + memory T cells were the dominant cell type that 
sending signals, while in responders, SELENOP-mac -
rophages and apCAFs were dominant in sending sig -
nals, and CD4 Naïve T cells received strong incoming 
signals. We also found that CD8 + Naïve T cells sent 
and received signals through pathways including inter -
leukin, transforming growth factor and HLA in this 
network. The top 15 signaling pathways with the high -
est possibilities in non-responders (Fig.  8G, Table S15) 
and responders (Fig.  8H, Table  S16) were shown by 
bubble plots. In non-responders, Apolipoprotein path -
way connected SELENOP-macrophages with the other 
cell clusters in the network, while Annexin connected 
the signaling from CD4 Memory T cells to the other 
cell clusters. In responders, cholesterol pathway con -
nected the signals sent from SELENOP-macrophages 
to the other cell clusters in the network, while inter -
feron pathway connected signals sent from CD4 
Helper T cells to the other cell clusters. SELENOP-
macrophages played the central role in Apolipopro -
tein signaling network in non-responders (Fig.  8I), and 
APOE-TREM2 pair is the key ligand-receptor pair in 
this pathway, the signaling network was visualized and 
plotted in tumor-1 (Fig.  8K) and tumor-4 (Fig.  8L). In 
Fig. 8 Effetive chemoimmunotherapy changes the communication patterns between SELENOP-macrophages, apCAFs and T cell subclusters. 
A Heatmap showing the neighboring relationships between T cell subclusters, SELENOP-macrophages and apCAFs. The number on the bar 
indicates the number of cells that have neighboring relationships. B Spatial annotation of indicated T cell subclusters, SELENOP-macrophages 
and apCAFs in 4 NSCLC tumor sections inferred via the RCTD algorithm. C Circle plots showing the differential number of interactions and strength 
in the network of T cell subclusters, SELENOP-macrophages and apCAFs, between non-responders and responders, inferred via CellPhoneDB 
algorithm. The arrows indicate the direction of signaling flow. Red color or blue color indicate the strengthening or weakening of the signaling 
flow, respectively. Thickness of the lines indicates the number (left) and strength (right) of the interactions. D Bar graph showing the differential 
signaling pathways between non-responders and responders. The selected significant signaling pathways were ranked top 20 on the basis 
of their differences in overall information flow within the inferred networks between non-responders and responders. The pathways colored 
in red are more enriched in non-responders, and those colored in green are more enriched in responders. Heatmaps showing the strength 
of outgoing (E) and incoming (F) signaling patterns with the network between non-responders and non-responders. Green color indicates 
the strengthening of signaling. The top 15 significant pathways within the cell–cell communication network in non-responders (G) and responders 
(H) were shown by bubble plots. Indicated pathways and relative communication patterns were colored in red or blue. The scale of the bubble 
indicates the p-values, and color indicates the expression level of ligands and receptors contributed to the pathways. I The social network model 
of Apolipoprotein pathway in non-responders was shown by a heat plot. The Color indicates the importance of indicated cell cluster in the network. 
J The ligand-receptor pair that contributed to Apolipoprotein pathway was shown by a bubble plot. The color indicates the communication 
possibility. K, L The spatial distribution of indicated cell clusters and communication patterns within the network in non-responder sections 
were inferred by CellPhoneDB. M The social network model of Cholesterol pathway in responders was shown by a heat plot. The Color indicates 
the importance of indicated cell cluster in the network. J The ligand-receptor pairs contributed to Cholesterol pathway were shown by a bubble 
plot. The color indicates the communication possibility. K, L The spatial distribution of indicated cell clusters and communication patterns 
within the network in responder sections were inferred by CellPhoneDB
(See figure on next page.)

Page 28 of 33Cui et al. Molecular Cancer          (2025) 24:111 
responders, cholesterol is the most significant pathway 
that linked the signals from SELENOP-macrophages 
to other cell clusters in the network (Fig.  8M), and 
the pairs of LIPA-RORC and LIPA-RORA were the 
key ligand-receptor pairs in the pathway (Fig.  8N), the 
cholesterol signaling network in responders were plot -
ted and visualized (Fig. 8 O, P).
Discussion
The emergence of immunotherapies, including immune 
checkpoint blockade and engineered T-cell therapy, has 
brought a new era of hope to cancer patients. The poten -
tial of neoadjuvant immunotherapy extends beyond the 
inhibition of unresectable tumors; it also presents oppor -
tunities for surgical resection. Consequently, neoadjuvant 
Fig. 8 (See legend on previous page.)

Page 29 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
immunotherapy has emerged as a highly efficacious 
therapeutic strategy for NSCLC and has even become 
a first-line therapeutic option. Nevertheless, the precise 
effective rate remains uncertain, prompting the con -
duction of numerous studies targeting immunotherapy 
responsiveness with the aim of elucidating the relation -
ship between tumor heterogeneity and immunotherapy 
responsiveness. The application of single-cell sequencing 
and spatial transcription technologies enables the dissec -
tion of the tumor immune microenvironment at the sin -
gle-cell level. In this study, we enrolled 6 NSCLC patients 
who underwent neoadjuvant immunotherapy followed 
by surgical resection and 6 patients who directly under -
went surgical resection of the tumor. Tumor tissues were 
obtained from both groups and subjected to single-cell 
sequencing and spatial transcriptome sequencing. The 
dynamic changes in the cellular composition, spatial dis -
tribution, gene expression and cellular communication 
between the two groups of samples were identified, and 
a spatial transcriptomic atlas of the NSCLC TME before 
and after immunotherapy was generated. Our study pro -
vides an in-depth analysis of the reshaping of the NSCLC 
TME caused by neoadjuvant immunotherapy.
Clonal expansion and infiltration of tumor-associated 
lymphocytes represent critical aspects of the response 
to immunotherapy [58]. A number of previous studies 
have conducted in-depth analyses of treatment-naïve 
NSCLC tissues, providing extensive baseline informa -
tion [59–61]. However, profiling of cancer tissues after 
immunotherapy remains insufficiently explored. The 
data demonstrated that immunotherapy resulted in a 
reduction in the proportion of Th17 CD4 + T cells and 
the suppression of gene expression associated with the 
pathway of Th17 cell differentiation. Th17 cells are cru -
cial for host resistance to pathogens [62]; however, 
Th17-secreted IL-17 and IL-22 are postulated to facili -
tate tumor growth [63]. Furthermore, in NSCLC, high 
expression of Th17 cell-associated genes has been linked 
to a poor response to anti-PD-1 therapy [64]. Our data 
demonstrated that the proportion of Th17 cells and 
the expression of related genes were reduced in the PT 
group. Th17 cells exhibited a significantly low exhaus -
tion signature, and the results of the analysis of the cel -
lular developmental trajectory indicated that Th17 cells 
were located not at the end but throughout one branch of 
the differentiation trajectory. Additionally, the differen -
tiation path of Th17 cells overlaps with that of Trm cells, 
which is the opposite of that of Tregs. The data demon -
strated that immunotherapy significantly decreased the 
proportion of KLRG1 + CD8 + T cells in NSCLC tumors. 
KLRG1 + CD8 + T cells are a subtype of cytotoxic effec -
tor T cells that are induced by strong T-cell receptors 
as well as inflammatory signals [65, 66]. PD-1 blockade 
in combination with chemotherapy enhances the intra -
tumor infiltration of KLRG1 + CD8 + T cells, which in 
turn leads to an improved prognosis in NSCLC patients 
[67]. However, KLRG + CD8 + T cells reportedly exhibit 
impaired antitumor immunity in a variety of cancers, 
including NSCLC [67, 68]. Furthermore, KLRG has 
been shown to recognize E-cadherin and to inhibit the 
activity of T cells and NK cells [69], thereby inducing 
immune escape [67, 70]. We propose that the lower level 
of KLRG1 + CD8 + T cells in the PT group is attributable 
to the impact of chemoimmunotherapy on the cellular 
differentiation of CD8 + T cells and that the combined 
therapy stimulated the progression of cell differentiation, 
whereas KLRG1 + CD8 + T cells were located at the ini -
tial stage of the developmental trajectory. However, the 
association between the infiltration of KLRG + T cells 
and immunotherapy response remains to be elucidated.
The intratumor infiltration of plasma cells indicates 
a favorable response to PD-1 blockade [71, 72], and 
the presence of a high abundance of follicular B cells in 
tumor tissue has been associated with sensitivity to anti -
tumor therapy and favorable outcomes [73]. Although 
our single-cell data revealed a notable decrease in the 
proportion of plasma cells following treatment, spatial 
transcriptomic data revealed substantial B-cell infil -
tration in pCR and responder tumor tissues, whereas 
B-cell infiltration was largely absent in nonresponder 
tissues. Moreover, diverse B-cell subtypes, especially 
those in TLS regions, including GCB and follicular B 
cells, were observed in pCR tissue. A substantial num -
ber of IgG + plasma cells are present in pCR tissue, 
which we believe is a strong predictor of immunotherapy 
responsiveness.
Tumor associated macrophages represent a prominent 
element of the TME, exerting a profound influence on 
tumor cell growth and treatment resistance [74, 75]. Our 
single-cell data revealed a notable increase in the pro -
portion of CXCL9 + macrophages following treatment, 
whereas the proportions of SPP1 + and SELENOP + mac-
rophages tended to decrease. Furthermore, spatial 
transcriptome analysis revealed that SELENOP + mac-
rophages were extensively distributed in NSCLC tissues, 
with the highest proportion of distribution in responder 
tissues. In both pCR and responder tissues, SELENOP 
macrophages exhibited notable spatial colocalization 
with T cells, indicating a close relationship between 
them. Notably, in responder tissues, SELENOP + mac-
rophages, in conjunction with CAFs, constitute a ram -
part-like structure that separates tumor cells from T cells 
and B cells. The literature demonstrates that ICB therapy 
induces CXCL9 secretion from macrophages and pro -
motes the immune infiltration of CD8 + T cells [76]. Con-
sequently, increased CXCL9 secretion is associated with 

Page 30 of 33Cui et al. Molecular Cancer          (2025) 24:111 
favorable immunotherapy responsiveness [76]. Recently, 
the ratio of CXCL9 to SPP1 gene expression has been 
proposed as a means of defining TAM polarization and 
evaluating global changes in the tumor microenviron -
ment and patient prognosis [77]. The data revealed a 
significant increase in the proportion of CXCL9 + mac-
rophages and a notable reduction in the SPP1 + mac-
rophages fraction in response to chemoimmunotherapy. 
The overall TMA polarization was found to be more 
M1-like in the PT group, indicating that the functions of 
TAMs had undergone a switch toward proinflammatory 
and antitumor activity. Furthermore, Monocle 3 revealed 
that CXCL9 and SPP1 cells are located at the ends of two 
distinct branches, indicating disparities in cell fate and 
biological functions. Our analyses revealed a substantial 
number of SELENOP + macrophages, which were sig -
nificantly clustered around tumor cells in responder tis -
sues. The function of SELENOP + macrophages remains 
unclear; however, Wang et  al. proposed that they may 
play an antitumor role [53]. Our data indicated that, in 
addition to their involvement in cellular metabolism, 
SELENOP + macrophages may also play an antigen-
presenting role, as evidenced by their high expression of 
the MHC I and MHC II genes. The significant colocali -
zation observed with T cells, as revealed by our spatial 
transcriptomic analysis, further suggested that these cells 
may be involved in antigen presentation and the induc -
tion of T-cell aggregation.
Fibroblasts represent a significant component of the 
cellular stroma. Cancer-associated fibroblasts exhibit 
considerable heterogeneity and assume a variety of roles 
within the TME. These roles include reshaping the TME 
by promoting tumor growth and inflammation, as well as 
remodeling the extracellular matrix. Our data revealed 
a notable decrease in the proportion of apCAFs in the 
PT group, whereas the proportion of meCAFs markedly 
increased. Additionally, the proportion of mCAFs tended 
to increase. Spatial transcriptomic data indicated that 
apCAFs were significantly present in responder tissues 
and strongly colocalized with SELENOP + TAMs, sug -
gesting that they may work together to conduct antigen 
presentation. In contrast, in pCR tissue, iCAFs were the 
predominant CAF subtype, accounting for the majority 
of the tissue. This finding is consistent with the findings 
of Cords et  al., who reported that iCAFs are associ -
ated with an inflammatory TME and a good prognosis 
for NSCLC patients [78]. In contrast, the infiltration of 
apCAFs was extremely limited in nonresponder tis -
sues. Furthermore, meCAFs were observed to colocal -
ize with mCAFs and to be present closely to tumor cells. 
mCAFs promote the invasiveness of tumors and inhibit 
immune infiltration [78, 79]. meCAFs have been demon -
strated to participate in glycolysis and alanine, aspartate, 
and glutamate metabolism [80]. Our data indicated that 
meCAFs expressed a range of genes involved in immune 
regulation, including MHC I genes, STAT genes, and 
cytokines. Compared with other CAF subtypes, meCAFs 
were significantly enriched in pathways associated with 
epithelial-to-mesenchymal transition (EMT), transform -
ing growth factor beta (TGF-beta), Janus kinase-signal 
transducers and activators of transcription 3 (JAK-
STAT3), interferon, and tumor necrosis factor (TNF) 
signaling. These findings suggest that meCAFs may play 
a complicated and activated role in the TME of NSCLC. 
To date, no studies have reported the infiltration and 
colocalization of meCAFs and mCAFs in tumor tissues. 
It may be hypothesized that mCAFs work in conjunction 
with meCAFs to regulate the reconstruction of the extra -
cellular matrix, thereby creating an immunosuppressive 
microenvironment. Our data from scRNA-seq and ST 
analysis suggested that the accumulation of iCAFs and 
less distribution of mCAFs in the TME correlated with 
the favorable responsiveness to chemoimmunotherapy.
NSCLC cells are derived from epithelial cells. The 
literature indicates that AT2 and club cells have the 
potential to develop into lung adenocarcinoma cells, 
whereas basal cells and club cells can develop into 
lung squamous cell carcinoma cells [81, 82]. Our study 
identified 8 distinct epithelial cell subtypes and classi -
fied them as diploid or aneuploid cells on the basis of 
CNVs. The epithelial cells exhibited strong heterogene -
ity. The comparison revealed that approximately 70% of 
the aneuploid cells were derived from basal cells, 4.99% 
from AT2 cells, and 4.42% from club cells, whereas the 
diploid cells were derived from a wide range of epithe -
lial cells (33% from basal cells, 22.39% from AT2 cells, 
and 9.17% from club cells). These findings suggested 
that NSCLC cells might be predominantly differenti -
ated from basal cells. By performing cell trajectory 
analysis, we identified genes that exhibited dynamic 
changes with pseudotime progression. Our find -
ings revealed that the expression of the KRAS gene 
increased with the transformation of epithelial cells to 
malignant epithelium. Additionally, we observed a sim -
ilar trend in the expression of keratin genes, including 
KRT 14, 16, 17 and 19. KRT19 has been recognized to 
play a prognostic role in NSCLC patients [83, 84], and 
KRT genes are reportedly associated with the estrogen 
response [85]. This finding suggests the possibility of 
simultaneous activation of the estrogen receptor path -
way alongside the malignant transformation of epi -
thelial cells. Elevated serum estrogen levels have been 
reported in NSCLC patients with poor responses to 
immunotherapy [20], which suggests that the activity 
of the estrogen pathway may be associated with unre -
sponsiveness to immunotherapy.

Page 31 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
This study is not without limitations. First, the neo -
adjuvant therapy employed in the study consisted of 
immunotherapy in conjunction with chemotherapy 
rather than immunotherapy alone. Consequently, the 
observed alterations in the tumor immune microenvi -
ronment are attributable not only to immunotherapy but 
also to the response to chemotherapy. Second, although 
4 NSCLC tumor tissue sections were included in this 
study for spatial transcription analysis, there is still a lack 
of treatment-naïve tissue samples for the control. Third, 
the sample size was insufficient to support the grouping 
of patients after neoadjuvant therapy, thereby hindering 
further investigation into the features of TME changes 
associated with immunotherapy responsiveness in the 
PT group. Furthermore, the considerable individual vari -
ability observed in this study reflected the tumor het -
erogeneity among NSCLC patients. However, this also 
contributed to the absence of statistically significant 
findings when comparing between groups, such as the 
differences in TCR colony expansion between groups. 
Additionally, individual patient characteristics, tumor 
stage, and the relatively limited sample size may have 
influenced the results. Fourth, although 4 TLS regions 
were identified in this study, further analysis of the TLS 
regions, such as cell-to-cell distance, genomic alterations 
and biological functions, should be conducted.
In conclusion, our study revealed dynamic changes in 
the tumor microenvironment subsequent to neoadjuvant 
chemoimmunotherapy. The SELENOP-macrophages 
were found to be aggregated within the tumor bound -
ary and TLSs regions, and the interaction between 
SELENOP-macrophages and apCAFs plays a critical 
role in the anti-tumor immunity and reconstruction of 
the TME induced by successful chemoimmunotherapy. 
Distribution of CD4 + Treg T cells and mCAFs indicated 
an immunosuppressive TME, while the accumulation 
of CD4 + Th17 T cells and iCAFs could act as a positive 
marker for the sensitivity to chemoimmunotherapy.
Abbreviations
NSCLC  Non-small cell lung cancer
ICB  Immune checkpoint blockage
PFS  Progression free survival
OS  Overall survival
RR  Response rate
PD-L1  Programmed cell death ligand 1
TME  Tumor microenvironment
ECM  Extracellular matrix
TIB  Tumor infiltrating B cells
MPR  Major pathological response
NMPR  Non-major pathological response
pCR  Pathological complete response
FFPE  Formalin-fixed paraffin-embedded
ST  Spatial transcriptome
UMI  Unique molecular identifiers
mIHC  Multiplex immunohistochemistry
IHC  Immunohistochemistry
TN  Treatment naïve
PT  Post treatment
CT  Computed tomography
RCTD  Residual convolutional neural network with the transformer decoder
H&E  Hematoxylin‒eosin
TLS  Tertiary lymphoid structures
CNV  Copy number variations
TKI  Tyrosine kinase inhibitors
t-SNE  T-distributed stochastic neighbor embedding
DEGs  Differentially expressed genes
TCR   T cell receptor
BCR  B cell receptor
Supplementary Information
The online version contains supplementary material available at https:// doi. 
org/ 10. 1186/ s12943- 025- 02287-w.
Supplementary Material 1.
Supplementary Material 2.
Acknowledgements
We thank all the members of the research team for their generous support of 
this work, and we thank all the patients who participated in this study. We are 
grateful to Gene Denovo (Guangzhou, China) for assisting in the bioinformat-
ics analysis in this study. We especially thank Dr. Kangping Song from Gene 
Denovo for his assistance and support in the study. Bioinformatic analysis 
was performed using Omicsmart, a dynamic real-time interactive online 
platform for data analysis (http:// www. omics mart. com). The graphic abstract 
was created by Figdraw (https:// www. figdr aw. com) with the authorization ID 
(PRPPI98f48).
Authors’ contributions
X.C. and S.L. contributed equally to this work. X.C. and Y.S. conceived the 
project and designed the experiments. Y.S. and S.L. collected the samples 
and performed the sequencing experiments, and X.C. and S.L. processed the 
data and performed the experiments. X.C. wrote the manuscript. H.S., J.X., 
and Y.S. acquired funding. All the authors have read and approved the final 
manuscript.
Funding
Not applicable.
Data availability
All single-cell sequencing raw data from this study are available from the NCBI 
under accession number PRJNA1068179 by visiting https:// www. ncbi. nlm. 
nih. gov/ biopr oject/ PRJNA 10681 79. The spatial transcriptome sequencing raw 
data are available from the NCBI under accession number PRJNA1139087 by 
visiting https:// www. ncbi. nlm. nih. gov/ biopr oject/ PRJNA 11390 87. The public 
scRNA-seq data used in this study for validation are available from Gene 
Expression Omnibus, under accession number GSE207422 (https:// www. ncbi. 
nlm. nih. gov/ geo/ query/ acc. cgi? acc= GSE20 7422). The other resources used in 
this study are available upon request from the corresponding author.
Declarations
Ethics approval and consent to participate
This study was conducted in accordance with ethical standards and national 
and international guidelines. This study was approved by the Research Ethics 
Committee of China Medical University, and all patients provided written 
informed consent. The collection of patient samples and related experiments 
in this study were approved by the Medical Ethics Committee of the First Hos-
pital of China Medical University (Authorization number: AF-SOP-07–1.2–01).
Competing interests
The authors declare no competing interests.

Page 32 of 33Cui et al. Molecular Cancer          (2025) 24:111 
Author details
1 Department of Urology, First Hospital of China Medical University, Shenyang, 
Liaoning Province 110001, China. 2 Department of Thoracic Surgery, First 
Hospital of China Medical University, Shenyang, Liaoning Province 110001, 
China. 3 Department of Gastrointestinal Surgery, First Hospital of China Medical 
University, Shenyang, Liaoning Province 110001, China. 4 Department of Rheu-
matology and Immunology, Shengjing Hospital of China Medical University, 
Shenyang, Liaoning Province  110004, China. 
Received: 4 October 2024   Accepted: 28 February 2025
References
 1. Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. CA Cancer J Clin. 
2024;74(1):12–49.
 2. Bray F, Laversanne M, Sung H, et al. Global cancer statistics 2022: GLOBO-
CAN estimates of incidence and mortality worldwide for 36 cancers in 
185 countries. CA Cancer J Clin. 2024;74(3):229–63.
 3. Herbst RS, Morgensztern D, Boshoff C. The biology and management of 
non-small cell lung cancer. Nature. 2018;553(7689):446–54.
 4. Reck M, Remon J, Hellmann MD. First-line immunotherapy for non-small-
cell lung cancer. J Clin Oncol. 2022;40(6):586–97.
 5. Lahiri A, Maji A, Potdar PD, et al. Lung cancer immunotherapy: progress, 
pitfalls, and promises. Mol Cancer. 2023;22(1):40.
 6. Cortiula F, Reymen B, Peters S, et al. Immunotherapy in unresectable 
stage III non-small-cell lung cancer: state of the art and novel therapeutic 
approaches. Ann Oncol. 2022;33(9):893–908.
 7. Girard N, Bar J, Garrido P , et al. Treatment characteristics and real-world 
progression-free survival in patients with unresectable stage III NSCLC 
who received durvalumab after chemoradiotherapy: findings from the 
PACIFIC-R study. J Thorac Oncol. 2023;18(2):181–93.
 8. Forde PM, Spicer J, Lu S, et al. Neoadjuvant nivolumab plus chemother-
apy in resectable lung cancer. N Engl J Med. 2022;386(21):1973–85.
 9. Chen Y, Yan B, Xu F, et al. Neoadjuvant chemoimmunotherapy in resect-
able stage IIIA/IIIB non-small cell lung cancer. Transl Lung Cancer Res. 
2021;10(5):2193–204.
 10. Passaro A, Attili I, de Marinis F. Neoadjuvant chemotherapy plus immuno-
therapy in early-stage resectable non-small-cell lung cancer. J Clin Oncol. 
2022;40(25):2871–7.
 11. Forde PM, Chaft JE, Smith KN, et al. Neoadjuvant PD-1 blockade in resect-
able lung cancer. N Engl J Med. 2018;378(21):1976–86.
 12. Rahim MK, Okholm T, Jones KB, et al. Dynamic CD8(+) T cell responses to 
cancer immunotherapy in human regional lymph nodes are disrupted in 
metastatic lymph nodes. Cell. 2023;186(6):1127–1143.e18.
 13. He J, Xiong X, Yang H, et al. Defined tumor antigen-specific T cells poten-
tiate personalized TCR-T cell therapy and prediction of immunotherapy 
response. Cell Res. 2022;32(6):530–42.
 14. Kong J, Ha D, Lee J, et al. Network-based machine learning approach 
to predict immunotherapy response in cancer patients. Nat Commun. 
2022;13(1):3703.
 15. Deng H, Zhao Y, Cai X, et al. PD-L1 expression and tumor mutation 
burden as pathological response biomarkers of neoadjuvant immuno-
therapy for early-stage non-small cell lung cancer: a systematic review 
and meta-analysis. Crit Rev Oncol Hematol. 2022;170: 103582.
 16. Pitt JM, Marabelle A, Eggermont A, Soria JC, Kroemer G, Zitvogel L. Target-
ing the tumor microenvironment: removing obstruction to anticancer 
immune responses and immunotherapy. Ann Oncol. 2016;27(8):1482–92.
 17. Baharom F, Ramirez-Valdez RA, Khalilnezhad A, et al. Systemic vaccination 
induces CD8(+) T cells and remodels the tumor microenvironment. Cell. 
2022;185(23):4317–4332.e15.
 18. Kim R, An M, Lee H, et al. Early tumor-immune microenvironmen-
tal remodeling and response to first-line fluoropyrimidine and 
platinum chemotherapy in advanced gastric cancer. Cancer Discov. 
2022;12(4):984–1001.
 19. Hui Z, Zhang J, Ren Y, et al. Single-cell profiling of immune cells after 
neoadjuvant pembrolizumab and chemotherapy in IIIA non-small cell 
lung cancer (NSCLC). Cell Death Dis. 2022;13(7):607.
 20. Hu J, Zhang L, Xia H, et al. Tumor microenvironment remodeling after 
neoadjuvant immunotherapy in non-small cell lung cancer revealed by 
single-cell RNA sequencing. Genome Med. 2023;15(1):14.
 21. Chang JY, Lin SH, Dong W, et al. Stereotactic ablative radiotherapy with 
or without immunotherapy for early-stage or isolated lung parenchymal 
recurrent node-negative non-small-cell lung cancer: an open-label, 
randomised, phase 2 trial. Lancet. 2023;402(10405):871–81.
 22. Yi L, Xu Z, Ma T, et al. T-cell subsets and cytokines are indicative of neo-
adjuvant chemoimmunotherapy responses in NSCLC. Cancer Immunol 
Immunother. 2024;73(6):99.
 23. Hou L, Zhang S, Yu W, et al. Single-cell transcriptomics reveals tumor-
infiltrating B cell function after neoadjuvant pembrolizumab and chemo-
therapy in non-small cell lung cancer. J Leukoc Biol. 2023 : qiad138 [pii].
 24. Gungabeesoon J, Gort-Freitas NA, Kiss M, et al. A neutrophil response 
linked to tumor control in immunotherapy. Cell. 2023;186(7):1448–1464.
e20.
 25. Hellmann MD, Chaft JE, William WN Jr, et al. Pathological response after 
neoadjuvant chemotherapy in resectable non-small-cell lung cancers: 
proposal for the use of major pathological response as a surrogate end-
point. Lancet Oncol. 2014;15(1):e42–50.
 26. Blakely CM, Weder W, Bubendorf L, et al. Primary endpoints to assess the 
efficacy of novel therapeutic approaches in epidermal growth factor 
receptor-mutated, surgically resectable non-small cell lung cancer: A 
review. Lung Cancer. 2023;177:59–72.
 27. Seth S, Mallik S, Bhadra T, Zhao Z. Dimensionality reduction and louvain 
agglomerative hierarchical clustering for cluster-specified frequent 
biomarker discovery in single-cell sequencing data. Front Genet. 2022;13: 
828479.
 28. Vanhersecke L, Brunet M, Guégan JP , et al. Mature tertiary lymphoid 
structures predict immune checkpoint inhibitor efficacy in solid tumors 
independently of PD-L1 expression. Nat Cancer. 2021;2(8):794–802.
 29. Sautès-Fridman C, Petitprez F, Calderaro J, Fridman WH. Tertiary lym-
phoid structures in the era of cancer immunotherapy. Nat Rev Cancer. 
2019;19(6):307–25.
 30. Sun X, Liu W, Sun L, et al. Maturation and abundance of tertiary lymphoid 
structures are associated with the efficacy of neoadjuvant chemoim-
munotherapy in resectable non-small cell lung cancer. J Immunother 
Cancer. 2022;10(11): e005531.
 31. Moser T, Akgün K, Proschmann U, Sellner J, Ziemssen T. The role of TH17 
cells in multiple sclerosis: therapeutic implications. Autoimmun Rev. 
2020;19(10): 102647.
 32. Chen CL, Wang Y, Huang CY, et al. IL-17 induces antitumor immunity by 
promoting beneficial neutrophil recruitment and activation in esopha-
geal squamous cell carcinoma. Oncoimmunology. 2017;7(1): e1373234.
 33. Lee YH, Chuah S, Nguyen P , et al. IFNγ(-)IL-17(+) CD8 T cells contribute to 
immunosuppression and tumor progression in human hepatocellular 
carcinoma. Cancer Lett. 2023;552: 215977.
 34. Marshall EA, Ng KW, Kung SH, et al. Emerging roles of T helper 17 and 
regulatory T cells in lung cancer progression and metastasis. Mol Cancer. 
2016;15(1):67.
 35. Liu C, Liu R, Wang B, et al. Blocking IL-17A enhances tumor response to 
anti-PD-1 immunotherapy in microsatellite stable colorectal cancer. J 
Immunother Cancer. 2021;9(1): e001895.
 36. Chen X, Zhao J, Herjan T, et al. IL-17-induced HIF1α drives resistance 
to anti-PD-L1 via fibroblast-mediated immune exclusion. J Exp Med. 
2022;219(6): e20210693.
 37. Wu H, Tang X, Kim HJ, et al. Expression of KLRG1 and CD127 defines 
distinct CD8(+) subsets that differentially impact patient outcome in 
follicular lymphoma. J Immunother Cancer. 2021;9(7): e002662.
 38. Remmerswaal E, Hombrink P , Nota B, et al. Expression of IL-7Rα and 
KLRG1 defines functionally distinct CD8(+) T-cell populations in humans. 
Eur J Immunol. 2019;49(5):694–708.
 39. Braud VM, Allan DS, O’Callaghan CA, et al. HLA-E binds to natural killer cell 
receptors CD94/NKG2A. B C Nat. 1998;391(6669):795–9.
 40. Le Dréan E, Vély F, Olcese L, et al. Inhibition of antigen-induced T cell 
response and antibody-induced NK cell cytotoxicity by NKG2A: associa-
tion of NKG2A with SHP-1 and SHP-2 protein-tyrosine phosphatases. Eur J 
Immunol. 1998;28(1):264–76.
 41. Boyington JC, Riaz AN, Patamawenu A, Coligan JE, Brooks AG, Sun 
PD. Structure of CD94 reveals a novel C-type lectin fold: implications 

Page 33 of 33
Cui et al. Molecular Cancer          (2025) 24:111 
 
for the NK cell-associated CD94/NKG2 receptors. Immunity. 
1999;10(1):75–82.
 42. van Hall T, André P , Horowitz A, et al. Monalizumab: inhibiting the novel 
immune checkpoint NKG2A. J Immunother Cancer. 2019;7(1):263.
 43. Herbst RS, Majem M, Barlesi F, et al. COAST: an open-label, phase II, 
multidrug platform study of durvalumab alone or in combination with 
oleclumab or monalizumab in patients with unresectable, stage III 
non-small-cell lung cancer. J Clin Oncol. 2022;40(29):3383–93.
 44. Liu X, Song J, Zhang H, et al. Immune checkpoint HLA-E:CD94-NKG2A 
mediates evasion of circulating tumor cells from NK cell surveillance. 
Cancer Cell. 2023;41(2):272–287.e9.
 45. Starzer AM, Berghoff AS. New emerging targets in cancer immuno -
therapy: CD27 (TNFRSF7). ESMO Open. 2020;4(Suppl 3): e000629.
 46. Parry EM, Lemvigh CK, Deng S, et al. ZNF683 marks a CD8(+ ) T cell 
population associated with anti-tumor immunity following anti-PD-1 
therapy for Richter syndrome. Cancer Cell. 2023;41(10):1803–16.e8.
 47. Laumont CM, Banville AC, Gilardi M, Hollern DP , Nelson BH. Tumour-
infiltrating B cells: immunological mechanisms, clinical impact and 
therapeutic opportunities. Nat Rev Cancer. 2022;22(7):414–30.
 48. Cabrita R, Lauss M, Sanna A, et al. Tertiary lymphoid structures 
improve immunotherapy and survival in melanoma. Nature. 
2020;577(7791):561–5.
 49. Helmink BA, Reddy SM, Gao J, et al. B cells and tertiary lym-
phoid structures promote immunotherapy response. Nature. 
2020;577(7791):549–55.
 50. Hao D, Han G, Sinjab A, et al. The single-cell immunogenomic 
landscape of b and plasma cells in early-stage lung adenocarcinoma. 
Cancer Discov. 2022;12(11):2626–45.
 51. Chen P , Zhao D, Li J, et al. Symbiotic macrophage-glioma cell interac-
tions reveal synthetic lethality in PTEN-Null glioma. Cancer Cell. 
2019;35(6):868–84.e6.
 52. Zhang Y, Du W, Chen Z, Xiang C. Upregulation of PD-L1 by SPP1 medi-
ates macrophage polarization and facilitates immune escape in lung 
adenocarcinoma. Exp Cell Res. 2017;359(2):449–57.
 53. Wang C, Yu Q, Song T, et al. The heterogeneous immune landscape 
between lung adenocarcinoma and squamous carcinoma revealed by 
single-cell RNA sequencing. Signal Transduct Target Ther. 2022;7(1):289.
 54. De Filippo K, Dudeck A, Hasenberg M, et al. Mast cell and macrophage 
chemokines CXCL1/CXCL2 control the early stage of neutrophil recruit -
ment during tissue inflammation. Blood. 2013;121(24):4930–7.
 55. Liu Y, Xiao J, Cai J, et al. Single-cell immune profiling of mouse liver 
aging reveals Cxcl2+  macrophages recruit neutrophils to aggravate 
liver injury. Hepatology. 2024;79(3):589–605.
 56. Nie F, Zhang J, Tian H, et al. The role of CXCL2-mediated crosstalk 
between tumor cells and macrophages in Fusobacterium nucleatum-
promoted oral squamous cell carcinoma progression. Cell Death Dis. 
2024;15(4):277.
 57. Cheng S, Li Z, Gao R, et al. A pan-cancer single-cell transcriptional atlas of 
tumor infiltrating myeloid cells. Cell. 2021;184(3):792–809.e23.
 58. Liu B, Hu X, Feng K, et al. Temporal single-cell tracing reveals clonal revival 
and expansion of precursor exhausted T cells during anti-PD-1 therapy in 
lung cancer. Nat Cancer. 2022;3(1):108–21.
 59. Wu F, Fan J, He Y, et al. Single-cell profiling of tumor heterogeneity and 
the microenvironment in advanced non-small cell lung cancer. Nat Com-
mun. 2021;12(1):2540.
 60. Guo X, Zhang Y, Zheng L, et al. Global characterization of T cells 
in non-small-cell lung cancer by single-cell sequencing. Nat Med. 
2018;24(7):978–85.
 61. Zheng L, Qin S, Si W, et al. Pan-cancer single-cell landscape of tumor-
infiltrating T cells. Science. 2021;374(6574):abe6474.
 62. Knochelmann HM, Dwyer CJ, Bailey SR, et al. When worlds collide: 
Th17 and Treg cells in cancer and autoimmunity. Cell Mol Immunol. 
2018;15(5):458–69.
 63. Dong C. TH17 cells in development: an updated view of their molecular 
identity and genetic programming. Nat Rev Immunol. 2008;8(5):337–48.
 64. Peng DH, Rodriguez BL, Diao L, et al. Th17 cells contribute to combina-
tion MEK inhibitor and anti-PD-L1 therapy resistance in KRAS/p53 mutant 
lung cancers. Nat Commun. 2021;12(1):2606.
 65. Herndler-Brandstetter D, Ishigame H, Shinnakasu R, et al. KLRG1(+) effec-
tor CD8(+) T cells lose KLRG1, differentiate into all memory T cell lineages, 
and convey enhanced protective immunity. Immunity. 2018;48(4):716–
29.e8.
 66. Joshi NS, Cui W, Chandele A, et al. Inflammation directs memory precur-
sor and short-lived effector CD8(+) T cell fates via the graded expression 
of T-bet transcription factor. Immunity. 2007;27(2):281–95.
 67. Hui Z, Ren Y, Zhang D, et al. PD-1 blockade potentiates neoadjuvant 
chemotherapy in NSCLC via increasing CD127(+) and KLRG1(+) CD8 T 
cells. NPJ Precis Oncol. 2023;7(1):48.
 68. Lou C, Wu K, Shi J, Dai Z, Xu Q. N-cadherin protects oral cancer cells from 
NK cell killing in the circulation by inducing NK cell functional exhaustion 
via the KLRG1 receptor. J Immunother Cancer. 2022;10(9): e005061.
 69. Nakamura S, Kuroki K, Ohki I, et al. Molecular basis for E-cadherin 
recognition by killer cell lectin-like receptor G1 (KLRG1). J Biol Chem. 
2009;284(40):27327–35.
 70. Zeng J, Zhang L, Ma S, et al. Dysregulation of peripheral and intratumoral 
KLRG1(+) CD8(+)T cells is associated with immune evasion in patients 
with non-small-cell lung cancer. Transl Oncol. 2024;45: 101968.
 71. Patil NS, Nabet BY, Müller S, et al. Intratumoral plasma cells predict 
outcomes to PD-L1 blockade in non-small cell lung cancer. Cancer Cell. 
2022;40(3):289–300.e4.
 72. Meylan M, Petitprez F, Becht E, et al. Tertiary lymphoid structures generate 
and propagate anti-tumor antibody-producing plasma cells in renal cell 
cancer. Immunity. 2022;55(3):527–41.e5.
 73. Germain C, Gnjatic S, Tamzalit F, et al. Presence of B cells in tertiary lym-
phoid structures is associated with a protective immunity in patients with 
lung cancer. Am J Respir Crit Care Med. 2014;189(7):832–44.
 74. Xiang X, Wang J, Lu D, Xu X. Targeting tumor-associated macrophages 
to synergize tumor immunotherapy. Signal Transduct Target Ther. 
2021;6(1):75.
 75. Zhang H, Liu L, Liu J, et al. Roles of tumor-associated macrophages 
in anti-PD-1/PD-L1 immunotherapy for solid cancers. Mol Cancer. 
2023;22(1):58.
 76. House IG, Savas P , Lai J, et al. Macrophage-derived CXCL9 and CXCL10 are 
required for antitumor immune responses following immune checkpoint 
blockade. Clin Cancer Res. 2020;26(2):487–504.
 77. Bill R, Wirapati P , Messemaker M, et al. CXCL9:SPP1 macrophage polarity 
identifies a network of cellular programs that control human cancers. 
Science. 2023;381(6657):515–24.
 78. Cords L, Engler S, Haberecker M, et al. Cancer-associated fibroblast 
phenotypes are associated with patient outcome in non-small cell lung 
cancer. Cancer Cell. 2024;42(3):396–412.e5.
 79. Li X, Sun Z, Peng G, et al. Single-cell RNA sequencing reveals a 
pro-invasive cancer-associated fibroblast subgroup associated with 
poor clinical outcomes in patients with gastric cancer. Theranostics. 
2022;12(2):620–38.
 80. Ma C, Yang C, Peng A, et al. Pan-cancer spatially resolved single-cell analy-
sis reveals the crosstalk between cancer-associated fibroblasts and tumor 
microenvironment. Mol Cancer. 2023;22(1):170.
 81. Sarode P , Mansouri S, Karger A, et al. Epithelial cell plasticity defines 
heterogeneity in lung cancer. Cell Signal. 2020;65: 109463.
 82. Cheung WK, Nguyen DX. Lineage factors and differentiation states in 
lung cancer progression. Oncogene. 2015;34(47):5771–80.
 83. Wang W, He J, Lu H, Kong Q, Lin S. KRT8 and KRT19, associated with EMT, 
are hypomethylated and overexpressed in lung adenocarcinoma and link 
to unfavorable prognosis. Biosci Rep. 2020;40(7):BSR20193468.
 84. Yuan X, Yi M, Dong B, Chu Q, Wu K. Prognostic significance of KRT19 in 
lung squamous cancer. J Cancer. 2021;12(4):1240–8.
 85. Han W, Hu C, Fan ZJ, Shen GL. Transcript levels of keratin 
1/5/6/14/15/16/17 as potential prognostic indicators in melanoma 
patients. Sci Rep. 2021;11(1):1023.
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in pub-
lished maps and institutional affiliations.