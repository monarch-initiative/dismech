---
reference_id: DOI:10.48188/so.6.9
title: "Transcriptome analysis of thyroid tissue in patients with Hashimoto’s disease using next-generation sequencing: case–control study"
authors:
- Marija Čikotić
- Marieta Bujak
- Silvija Piškorjanac
- Mario Štefanić
journal: ST-OPEN
year: '2025'
doi: 10.48188/so.6.9
content_type: full_text_pdf
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://st-open.unist.hr/index.php/st-open/article/download/157/142"
oa_status: diamond
license: cc-by
local_pdf_path: files/DOI_10.48188_so.6.9.pdf
---

# Transcriptome analysis of thyroid tissue in patients with Hashimoto’s disease using next-generation sequencing: case–control study
**Authors:** Marija Čikotić, Marieta Bujak, Silvija Piškorjanac, Mario Štefanić
**Journal:** ST-OPEN (2025)
**DOI:** [10.48188/so.6.9](https://doi.org/10.48188/so.6.9)

## Content

Aim: Hashimoto’s thyroiditis (HT) is a common but poorly understood autoimmune disease. Here, we aimed to identify differentially expressed genes and biological signaling pathways associated with HT by comparing whole genome transcriptomes from affected and healthy donors.
Methods: As part of a case–control design, we analyzed thyroid tissue RNA sequencing libraries from the Genotype-Tissue Expression Project (v8 release). Donors were divided into two demographically and technically matched groups according to the presence (n = 31) or absence of histopathologically confirmed HT in their thyroid tissue samples (n = 73). Differential gene expression analysis was performed, followed by pathway enrichment profiling (Hallmark, Kyoto Encyclopedia of Genes and Genomes).
Results: In total, we identified 2,809 upregulated genes and 2,348 downregulated genes (fold change > 1.5, Benjamini-Hochberg adjusted P < 0.05). HT was characterized by pathways associated with T- and B-cell signaling, antigen processing, cytokine-cytokine receptor interactions, phagocytic responses, and cell death. The transition to HT was accompanied by a decreased expression of gene sets related to cell junctions, cell polarity, epithelial and anabolic processes, redox homeostasis, mitochondrial health, and Hippo signaling. Loss of endothelial cell characteristics and positional markers of perivascular fibroblasts followed closely thereafter.
Conclusions: The local expansion of cellular, humoral and innate immunity is a hallmark of HT. Cell death dominated the scene, followed by signs of epithelial, endothelial and stromal remodeling of thyroid tissue. This included reciprocal contraction of the terminally differentiated epithelium and (perivascular) endothelium amidst increasing autoimmune activity. Widespread changes in gene activity were observed in various homeostatic processes, including cell metabolism, cellular energetics, and anabolic and catabolic metabolic pathways.

1
RESEARCH ARTICLE st-open.unist.hr
1
© 2025 The Author(s)
Transcriptome analysis of thyroid tissue 
in patients with Hashimoto’ s disease using 
next-generation sequencing: case–control 
study
Marija Čikotić1, 
Marieta Bujak2
 , 
Silvija Piškorjanac3
 ,  
Mario Štefanić4
1University Hospital Centre Zagreb, 
Zagreb, Croatia
2University of Split School of Medicine, 
Split, Croatia
3Faculty of Dental Medicine and Health, 
Josip Juraj Strossmayer University, 
Osijek, Croatia
4Department of Nuclear Medicine and 
Oncology, Osijek Faculty of Medicine, 
Josip Juraj Strossmayer University, 
Osijek, Croatia
Correspondence to:
Mario Štefanić 
Department of Nuclear Medicine and 
Oncology, Osijek Faculty of Medicine, Josip 
Juraj Strossmayer University, Josipa Huttlera 
4, 31000 Osijek, Croatia 
mstefanic@mefos.hr
Cite as:
Čikotić M, Bujak M, Piškorjanac S, Štefanić 
M. Transcriptome analysis of thyroid tissue 
in patients with Hashimoto’s disease using 
next-generation sequencing: case–control 
study. ST -OPEN. 2025;6:e2025.2219.27.
DOI:
https:/ /doi.org/10.48188/so.6.9
Aim: Hashimoto’s thyroiditis (HT) is a common but poorly 
understood autoimmune disease. Here, we aimed to iden-
tify differentially expressed genes and biological signaling 
pathways associated with HT by comparing whole genome 
transcriptomes from affected and healthy donors.
Methods: As part of a case–control design, we analyzed 
thyroid tissue RNA sequencing libraries from the Genotype-
Tissue Expression Project (v8 release). Donors were di-
vided into two demographically and technically matched 
groups according to the presence (n = 31) or absence of 
histopathologically confirmed HT in their thyroid tissue 
samples (n = 73). Differential gene expression analysis was 
performed, followed by pathway enrichment profiling 
(Hallmark, Kyoto Encyclopedia of Genes and Genomes).
Results: In total, we identified 2,809 upregulated genes and 
2,348 downregulated genes (fold change > 1.5, Benjamini-
Hochberg adjusted P < 0.05). HT was characterized by path-
ways associated with T- and B-cell signaling, antigen pro-
cessing, cytokine-cytokine receptor interactions, phagocytic 
responses, and cell death. The transition to HT was accom-
panied by a decreased expression of gene sets related to cell 
junctions, cell polarity, epithelial and anabolic processes, re-
dox homeostasis, mitochondrial health, and Hippo signaling. 
Loss of endothelial cell characteristics and positional mark-
ers of perivascular fibroblasts followed closely thereafter.
Conclusions: The local expansion of cellular, humoral and 
innate immunity is a hallmark of HT. Cell death dominated 
the scene, followed by signs of epithelial, endothelial and 
stromal remodeling of thyroid tissue. This included recipro-
cal contraction of the terminally differentiated epithelium 
and (perivascular) endothelium amidst increasing autoim-
mune activity. Widespread changes in gene activity were 
observed in various homeostatic processes, including cell 
metabolism, cellular energetics, and anabolic and catabolic 
metabolic pathways.
Keywords: autoimmune; computational biology; gene ex-
pression profiling; RNA-seq; thyroiditis; whole genome se-
quencing

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 2
Introduction
Hashimoto’s thyroiditis (HT) is a common autoimmune disease characterized by the grad-
ual replacement of thyroid follicular architecture by scar tissue and lymphoplasmocytic 
aggregates (1, 2). It occurs predominantly in middle-aged women and shows a strong fa-
milial segregation, as well as a highly variable course of disease. In most patients, thyroid 
hormone levels are well maintained in the initial phase; over time, life-threatening prima-
ry hypothyroidism often develops (1, 2). The etiology of HT remains poorly understood (3), 
and there are currently very few treatment options beyond lifelong hormone replacement 
therapy (4), which is often insufficient to restore well-being and overall quality of life 
(5–7). Thyroid autoimmunity is also associated with pregnancy complications affecting 
both mother and child (8, 9) and, more importantly, with an increased risk of developing 
thyroid malignancies (10, 11). There is therefore an urgent need to improve our under-
standing of the biology of HT.
To achieve this, HT research has recently turned to more advanced technologies, such 
as next-generation sequencing of bulk tissues and single-cell RNA sequencing (RNA-seq). 
Both methods allow comprehensive profiling of gene expression on a genome-wide scale 
and offer a unique opportunity to gain insights into changes in cellular composition and 
gene activity of complex tissues (12, 13). Consequently, RNA-seq has radically changed our 
understanding of inflammatory diseases (12, 14), but its application in HT remains modest 
(15–17). To date, the highest resolution has been achieved in immune cell lines infiltrating 
the thyroid gland (15–17). In contrast, the epithelial and mesenchymal niches have been 
comparatively understudied (16–18), due to the low cellular recovery of follicular and 
stromal components in the single-cell protocols currently in use. In addition, RNA-seq is 
highly sensitive to technical and biological confounding factors (19–22), sample size and 
computational details (23), making interpretation of the data an extremely complex task 
(15). Therefore, it remains difficult to draw a comprehensive picture of HT based on the 
information from these studies alone, and the simultaneous remodeling of the epithelium, 
immune system and stroma has yet to be replicated in a single study (17).
Here, we used publicly available whole genome RNA-seq libraries of thyroid tissue from 
the Genotype-Tissue Expression (GTEx) project (24, 25) to systematically compare the gene 
expression profiles of affected individuals with those of healthy donors. Our aim was to 
better characterize the cascade of transcriptional events and to investigate the extent of 
thyroid tissue remodeling in HT. To this end, we performed an unbiased screening of deep-
ly phenotyped and carefully annotated datasets (26), supported by the extensive literature 
on best practices in GTEx data (19–22, 24–26).

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
3
Methods
Participants
A total of 104 tissue donors were included in this case–control study. Donors were divid -
ed into two independent groups based on the presence or absence of histopathologically 
confirmed HT in their thyroid tissue samples. The whole-genome gene expression profiles 
of the thyroid tissue were then integrated, harmonized and compared between the two 
groups to search for differentially expressed genes and associated biological pathways.
Materials
The study material consisted of whole-genome thyroid tissue libraries (expression matri-
ces, dbGaP phs000424.v8.p2) and associated metadata. The following attributes were re-
corded for each donor: pathology reports, agonal characteristics, technical characteristics, 
sample processing characteristics and the first five principal components of the genotype 
(PC1-5). The PC1-5 components provide information about the structure of the donor popu-
lation in whole-genome genotyping (25). Digitized microscopic images of hematoxylin and 
eosin-stained thyroid tissue sections from HT patients (Aperio, Leica Biosystems) were 
downloaded from the GTEx portal. The photomicrographs were visualized using QuPath 
v0.2.0-m9 (https://github.com/qupath , University of Edinburgh, UK). Anonymous and 
de-identified RNA-seq data were obtained from the GTEx Project Repository (v8, https://
gtexportal.org/home/datasets). The study was approved by the Ethics Committee of the 
Faculty of Medicine in Osijek (REG. NO. 2158-61-46-22-89; April 30, 2022).
Of the 574 libraries classified as thyroid tissue (UBERON0002046), 184 control samples and 
37 thyroid samples showing histopathologic features of HT were selected for further anal-
ysis. Degraded samples, mislabeled libraries, neoplasms, thyroid tissue samples with non-
specific changes, and contaminated samples with large vessels, thymus, muscle, adipose 
tissue, and parathyroid tissue were excluded from the selection (22, 26). After adjusting for 
confounding factors (age, sex, agonal classification on the Hardy scale (27), RNA integrity, 
collection facility, and ischemia time), the final comparison included 73 normal and 31 
affected tissue libraries. All libraries were independent (one library per unrelated donor), 
and all donors were over 21 years of age, with a postmortem interval of less than 24 hours.
RNA sequencing
In brief, RNA sequencing was performed using the Illumina TruSeq protocol (non-strand-
ed, polyA+ selection; Broad Institute; HiSeq 2000 or HiSeq 2500) on 200 ng of total RNA 
extracted from 0.5–2 g of thyroid tissue (PAXgene Tissue miRNA Kit, PreAnalytix, Qiagen). 
The target coverage was ~50 million 76-bp reads (24, 25).
RNA read quality, alignment, and quantification
The RNA quality after fixation (PAXgene Tissue FIX, Qiagen) was assessed using the RNA 
Integrity Number (RIN; Agilent Bioanalyzer), with an exclusion threshold of RIN < 5.5 (24, 
25). Alignment to the human reference genome (GRCh38/hg38) was performed using STAR 

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 4
v2.5.3a with GENCODE v26 annotations (56,200 genes). Gene-level quantification was per-
formed by collapsing all gene isoforms into a single transcript.
Gene expression analysis
Expression values were normalized to the effective library size using the Trimmed Mean of 
M-values (TMM) approach (28) from the edgeR package (29). Variance stabilization was per-
formed using a rank-based inverse normal transformation (30). Systematic variation (31) 
was corrected by applying the function removeBatchEffect (first three genotype PCs + hidden 
factors). Hidden factors (representing batch effects) were identified by nonparametric mod-
eling of the expression matrix using the DASC package (convex clustering and nonnegative 
matrix factorization, regularization parameter lambda = 10-3-10-1, factorization rank = 2-10, 
optimal rank according to cophenetic coefficient = 3, L2 penalty, 100 initializations) (32).
Transcriptome comparison between HT patients and healthy controls
We tested for differential expression using linear modeling with Bayesian modulation in 
the limma package (33–35). Compared to other methods, the lmFit function is particularly 
robust for small samples. We defined differential expression as an absolute fold change 
(|FC|) greater than 1.5 and corrected for a false discovery rate (FDR) less than 0.05 using 
the Benjamini-Hochberg procedure.
Biological pathway analysis
Biological pathway analysis (Hallmark and C2 sets (36) from the MSigDB v7.4 collection 
(37)) was performed using a list of differentially expressed genes as input. The significance 
threshold was set to FDR < 0.05 (1,000 permutations) for gene sets with at least 10 genes 
(38). Visualization of the C2 pathway (Kyoto Encyclopedia of Genes and Genomes) was 
performed using the Pathview package under the GNU General Public License (≥ 3.0) (39). 
The lists of differentially expressed genes were also matched with a table of cell mark-
ers (Azimuth 2023) (40) and tissue-related transcripts (Human Gene Atlas) from Enrichr 
(https://maayanlab.cloud/Enrichr/) (41). The list of stem cell-associated signatures was ob-
tained from StemChecker (http://stemchecker.sysbiolab.eu/) (42).
Gene symbol conversion was performed using the biomaRt package (HUGO Gene 
Nomenclature Committee/HGNC – Ensembl/ENSG, H. sapiens). Gene and transcript classifi-
cation was based on the Ensembl r105 release. HGNC symbols were used for gene naming 
throughout the text. The list of matrisome components was retrieved from the M5889 set 
(the MSigDB collection, Naba_matrisome).
Statistical analysis
Continuous data (demographic and technical attributes) were summarized using the me-
dian and interquartile range. Categorical data are presented as absolute frequencies and 
proportions. Contingency tables were analyzed using Fisher’s exact test. For non-genom-
ic continuous variables, the Mann-Whitney test was used to examine the difference be-
tween the two independent samples. The nonparametric correlation analysis was based 

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
5
on Spearman’s rank test. All P-values were two-sided, with post-hoc correction for the 
number of tests described above. Unless otherwise stated, adjusted P-values are reported 
throughout the text. The Multivariate and Propensity Score Matching Software for Causal 
Inference was used to adjust for confounding factors (43). Results were visualized using 
the packages ComplexHeatMap v2.6.2, RColorBrewer v1.1-2, EnhancedVolcano v1.12.0 and 
ggpubr v0.4.0 in R, version 4.0.3 (R Foundation for Statistical Computing, Vienna, Austria).
Results
The final analysis included a total of 21,077 genes with unique HGNC symbols. Table 1 
shows the demographic characteristics of the donors and technical details of the samples. 
The clear separation between affected and control participants indicates a global differ-
Table 1. Donor demographics with sample processing details (n = 104)*
Attributes Category/unit HT (n = 31) Controls (n = 73) P†
Sex Male/female 12/19 32/41 0.670
Age (years) 20-29 1 2 0.865‡
30-39 2 8
40-49 9 17
50-59 6 19
60-69 13 27
Autolysis score (SMATSSCR) 0 (no autolysis) 5 3 0.182
1 (mild) 22 59
2 (moderate) 4 11
TISCH (SMTSISCH) min. 452 (121-951) 449 (163-706) 0.924
PAX (SMTSPAX) min. 824 (653-1089) 776 (631-1077) 0.582
RIN (SMRIN) - 6.9 (6.4-7.3) 6.7 (6.2-7.2) 0.935
Center (SMCENTER) B1 23 52 0.815‡
C1 8 21
Agonal category (DTHHRDY) 0 (ventilator case) 19 45 0.762‡
1 (fast death, violent) 1 1
2 (fast death, natural) 9 17
3 (intermediate, ill) 1 3
4 (slow death) 1 7
Total mapped reads (SMMPPD) × 107 7.66 (6.39-9.24) 7.83 (6.95-8.99) 0.541
*TISCH – ischemic (post-mortem) interval, PAX – time spent in PAX fixative, RIN – RNA integrity number, Center – sampling 
institution. The labels in parentheses are the original abbreviations for specific attributes. Continuous variables are presented 
as medians with interquartile ranges.
†Mann-Whitney test.
‡Generalized Fisher exact test (Freeman-Halton extension).

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 6
ence in gene expression between diseased and healthy thyroid tissue (Figure 1). Most of 
those affected were women over the age of 40, although age and gender were similarly 
distributed in the control group. The lowest RIN score was 5.5 and the highest recorded 
score was 9.7. Ten donors had histologically severe/diffuse HT, nine had focal areas of lym-
phocytic thyroiditis, and the remainder were classified as moderate HT (Figure S1 in our 
online dataset (44)). Broadly speaking, late-stage HT was associated with higher transcrip-
tional variability, but none of these subgroups were large enough to support subgroup 
analysis. There were no significant differences between groups in terms of sample pres-
ervation, ischemia time, tissue fixation, or cause of death. Sequencing depth was similar 
in both groups.
Among differentially expressed transcripts (FDR < 0.05, |FC| > 1.5), 2,809 genes showed 
significantly higher and 2,348 significantly lower expression in the affected thyroid tis-
sues (Figure 1), with the top 45 hits from both lists presented in Table S1 in our online 
dataset (44). Protein-coding genes were the most abundant transcript type, followed by 
long non-coding RNAs and immunoglobulin variable regions, as presented in Table S2 
in our online dataset (44). The results of the biological pathway analysis for the C2 and H 
sets from MSigDB are summarized in Table 2 and Table 3, respectively. Pathway analysis 
revealed that activation of the immune system was paramount (T cell and B cell signaling, 
Figure 2, along with cell death and cytotoxicity-related processes (Figure 3, Table 2).
Figure 1. Overview of differentially expressed genes. Panel A. Hierarchical clustering (Euclidean distance, meth-
od = complete linkage). Lighter shades correspond to higher expression levels. Panel B. Bland-Altman representation of 
differentially expressed genes. FDR – false discovery rate (Benjamini-Hochberg), HT – Hashimoto’s thyroiditis. Created 
using ComplexHeatmap R package (https://www.rdocumentation.org/packages/ComplexHeatmap/versions/1.10.2).

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
7
Table 2. Pathway analysis, MSigDB v7.4, Kyoto Encyclopedia of Genes and Genomes*
Process
Enriched
Process
Depleted
NES No. genes P* NES No. genes P†
Cytokine-cytokine recep-
tor interactions 2.65 227 1.8 × 10-4 Oxidative phosphory-
lation -2.60 110 3.6 × 10-4
Natural killer cell-medi-
ated cytotoxicity 2.57 87 1.8 × 10-4 AMPK signaling path-
way -2.12 111 3.6 × 10-4
Th1 and Th2 cell differ-
entiation 2.44 72 1.8 × 10-4 Autophagy -1.96 133 3.7 × 10-4
T cell receptor signaling 2.41 95 1.8 × 10-4 Hippo signaling pathway -1.90 27 4.8 × 10-3
Th1 cell differentiation 2.37 84 1.8 × 10-4 Adherent junctions -1.85 68 1.2 × 10-3
B cell receptor signaling 2.37 66 1.8 × 10-4 Insulin signaling 
pathway -1.80 128 3.7 × 10-4
Chemokine signaling 2.36 169 1.8 × 10-4 Mitophagy -1.80 65 2.9 × 10-3
NF-kappa B signaling 
pathway 2.23 96 1.8 × 10-4 Selenocompound 
metabolism -1.79 15 1.6 × 10-2
Cell adhesion molecules 2.20 118 1.8 × 10-4 Tight junctions -1.77 150 3.9 × 10-4
Processing and presen-
tation 1.97 36 8.6 × 10-4 Pentose phosphate 
pathway -1.74 24 2.1 × 10-2
Autoimmune thyroid 
disease 1.96 16 1.7 × 10-3 mTOR signaling path-
way -1.69 143 9.7 × 10-4
Complement and coagu-
lation cascades 1.88 67 5.6 × 10-4 Glutathione metabolism -1.68 44 1.6 × 10-2
Necroptosis 1.86 121 3.6 × 10-4 Fatty acid metabolism -1.61 52 2.3 × 10-2
Leukocyte transendo-
thelial migration 1.80 103 5.9 × 10-4 Focal adhesions -1.55 193 3.2 × 10-3
Apoptosis 1.80 128 4.6 × 10-4 Axon guidance -1.54 170 3.0 × 10-3
Fc receptor-mediated 
phagocytosis 1.76 86 2.5 × 10-3
TNF signaling pathway 1.66 103 5.1 × 10-3
Cell cycle 1.51 119 2.2 × 10-2
*Abbreviations: Th – T helper, NES – normalized enrichment score, mTOR – mammalian target of rapamycin, AMPK 5’ – adenos-
ine monophosphate-dependent protein kinase, NF – nuclear factor, TNF – tumor necrosis factor.
†Corrected P-value.
Table 3. Pathway analysis, MSigDB v7.4, Hallmark*
Process
Enriched expression
Process
Depleted expression
NES No. genes P† NES No. genes P†
Allograft rejection 3.12 175 6.9 × 10-5 Oxidative 
 phosphorylation -2.69 198 1.7 × 10-4
Interferon-gamma 
response 2.90 185 6.9 × 10-5 Protein secretion -2.65 95 1.6 × 10-4
Interferon-alpha 
response 2.56 89 6.9 × 10-5 Adipogenesis -2.38 196 1.7 × 10-4
IL6 JAK STAT3 sig-
naling 2.47 83 6.9 × 10-5 Fatty acid metabolism -2.11 151 1.7 × 10-4
Inflammatory response 2.45 189 6.9 × 10-5 Reactive oxygen 
species -1.81 45 3.4 × 10-3
Complement 2.09 187 6.9 × 10-5 Myogenesis -1.74 188 1.7 × 10-4

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 8
Table 3. (continued)
Process
Enriched expression
Process
Depleted expression
NES No. genes P† NES No. genes P†
IL2 STAT5 signaling 2.03 96 6.9 × 10-5 Androgen response -1.46 98 2.4 × 10-2
TNFA signaling via 
NFKB 2.03 190 6.9 × 10-5 Xenobiotic metabolism -1.37 179 1.9 × 10-2
E2F targets 2.02 197 6.9 × 10-5 Glycolysis -1.35 190 2.0 × 10-2
G2-M checkpoint 1.8 197 6.9 × 10-5 Epithelial-mesenchymal 
transition -1.34 199 2.1 × 10-2
KRAS signaling up 1.7 188 1.6 × 10-4
P53 pathway 1.39 197 3.3 × 10-2
*Abbreviations: NES – normalized enrichment score, IL – interleukin, JAK – Janus kinase, STAT – signal transducer and activator 
of transcription, TNF – tumor necrosis factor.
†Corrected P-value.
Figure 2. The expression of genes related to the B cell receptor and the distal signaling pathways in the thyroid gland. 
The figure was generated using the Pathview package under the GNU General Public License (≥ 3.0), based on data from 
the Kyoto Encyclopedia of Genes and Genomes (KEGG). Gene symbols and their respective names are available at https://
www.genenames.org/.

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
9
Figure 3. Normalized gene expression of cytotoxic-natural killer cell markers. The figure was generated using the 
Pathview package under the GNU General Public License (≥ 3.0), based on data from the Kyoto Encyclopedia of Genes 
and Genomes (KEGG). Gene symbols and their respective names are available at https://www.genenames.org/.
Figure 4. Gene expressions of immu-
ne cell lineage markers (z-scale) in thy-
ro id tissues. HT – Hashimoto’s thyro-
i ditis. Column names (bottom row) 
correspond to the original sample iden-
ti fication codes (n = 104). Created using 
ComplexHeatmap R package (https://
www.rdocumentation.org/packages/
ComplexHeatmap/versions/1.10.2).

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 10
In addition to the T-cell receptor (TCR) chains of conventional (TRAV1‒2neg) αβ-T cells, the 
expression of gamma-chain TCRs (TRGV2/5/7/9-10, TRGC1) was significantly increased. 
Among the lineage-specific markers (Figure 4), the master regulators of T-helper (Th) type 
1 and 2 responses were highly enriched. In the B cell lineage (MS4A1, CD79A), the telltale 
markers of activation and maturation were particularly present (cells of the light and dark 
zone of the germinal center, plasmablasts, activated and memory B cells). In addition to 
lymphoid immunity, myeloid markers were also enriched, indicating the presence of mac-
rophages and dendritic cells (FDCSP, log2FC = 1.21, P = 2 × 1 0-9, Figure 4) (45).
Among the highly enriched cytokine gene transcripts, as presented in Figure S2 in our 
online dataset (44), chemotaxis, adhesion and migration were prominent in functional 
analysis, followed by transendothelial recruitment, lymphoid organization (CCL19, log-
2FC = 1.22, P = 4.3 × 10-9; CXCL9, log 2FC = 1.39, P = 3.9 × 10-12) and tissue retention of inflam-
matory cells (16).
Among the downregulated gene transcripts, loss of key components that support cellular 
architecture and tissue maintenance was evident, along with loss of genes for planar cell 
polarity (PCP4, FAT4, CELSR2, RYK, PHACTR4; -0.7 < log2FC < -0.6, 0.0018 < P < 0.0066) and in-
Figure 5. Gene expression from the iodine organification and thyroxine biosynthesis pathways in thyroid tissue. Green 
color indicates significantly reduced expression (FDR < 0.05). The figure was generated using the Pathview package un-
der the GNU General Public License (≥ 3.0), based on data from the Kyoto Encyclopedia of Genes and Genomes. Gene 
names are available at https://www.genenames.org/ (HGNC symbols).

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
11
tercellular communication (Table 2) (46). Overall, a significant reduction in thyroid-relat-
ed characteristics was observed (P = 5.8 × 10-40, Human Gene Atlas).
Epithelial markers were significantly overrepresented among the downregulated tran-
scripts, reflecting a systematic deviation in the expression of transcriptional regulators 
(NKX2-1, PAX8) and canonical markers of terminally differentiated thyroid follicular cells 
(DIO1, TSHR, TG, TFF3; Table S1, (44)). In addition, there was a pronounced loss of iodine 
transport and thyroxine biosynthesis (TPO, DUOXA2, IYD/DEHAL1, TG, SLC26A7, SLC26A4/
PDS) (Figure 5). Besides thyroid epithelial markers a clear loss of endothelial features was 
observed (CDH5, TIE1, PTPRB, EDNRB, PLVAP, PDPN, PROX1; Table S3, (44)), along with 
reduced angiogenic signaling (VEGFA-FLT1/VEGFC-FLT4), loss of perivascular fibroblastic 
positional markers (NOTCH3, SPARC, CD36, STEAP4; Figure S1 and Table S3) (44, 47, 48), 
and decreased expression of COL4A1 (log2FC = -0.69, P = 2.8 × 10-3) and COL18A1 (log2FC = -0.6, 
P = 5.8 × 10-3), two collagens that underlay the epithelial and endothelial cell sheets. The loss 
of homeostatic basement membrane collagens was mirrored by over-transcription of the 
genes for type VII (COL7A1, log 2FC = 0.83, P = 1.7 × 10-4) and type XXII (fibril-associated) col-
lagen (COL22A1, log2FC = 0.73, P = 9.6 × 10-4).
The mechanisms of follicular and endothelial cell death are still largely unknown. 
Possible mechanisms include complement-mediated lysis, which usually depends on an-
tibodies (Figure 6, Table 2, Table 3) and apoptosis as an expression of cellular cytotox-
icity (Table 2).
Beyond these pathways, transcripts encoding components involved in cellular necroptosis 
have also been identified, suggesting that there may be an additional level of complexity 
under specific circumstances, as presented in Table 2 and Figure S3 (44). In addition, there 
Figure 6. Normalized gene expression, the coagulation pathway (a) and complement pathway (b) in diseased thyroid 
tissue. The figure was generated using the Pathview package under the GNU General Public License (≥ 3.0), based on data 
from the Kyoto Encyclopedia of Genes and Genomes. Gene names are available at https://www.genenames.org/  (HGNC 
symbols).

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 12
was disruption of glutathione metabolism (Table 2) and loss of oxidative stress-responsive 
detoxification (Table 3), both of which play a central, cytoprotective role in maintaining thy-
roid follicular cell redox homeostasis. Metabolically, downregulation of anabolic processes 
(mTOR signaling, insulin signaling, pentose phosphate pathway) coincided with transcrip-
tional dysregulation of autophagy (Table 2), mitochondrial dysfunction, impaired oxida-
tive phosphorylation (Figure 7, Table 2, Table 3), and altered lipid catabolism (β-oxidation) 
(15). Apparently, many transcripts associated with stem cell biology were also lost (Table 
S4, (44)), including β-catenin (CTNNB1), a canonical signal transducer from the Wingless 
signaling pathway (log2FC = -0.64, P = 2.9 × 10-3), the Wingless co-receptor LRP6 (log2FC = -1.18, 
P = 1.7 × 10-8) and Leucine-Rich Repeat-Containing G protein-Coupled Receptor 5, a Wingless 
target (LGR5, log2FC = -0.89, P = 5.9 × 10-5). In contrast, a pronounced increase in downstream 
signaling was observed along the TNFα and interferon-α/γ pathways (Table 3).
In addition to the cell-intrinsic transcriptional reprogramming, there were also signs of 
extensive remodeling of the extracellular matrix, as visible in Figure S4 (44). The loss of 
expression of epithelial markers was accompanied by a strong induction of important fi-
brogenic factors, such as the transforming growth factor TGFB1 (log2FC = 0.96, P = 4.4 × 10-6; 
EPCAM vs. TGFB1, Spearman’s ρ = -0.3, nominal P = 0.002). The increased expression of ly-
sosomal cathepsins (CTS), lysyl oxidases and members of the metalloproteinase superfam-
ily (MMP, ADAM, and ADAMTS proteases) indicates an active remodeling of the cellular 
Figure 7. Mitochondrial electron transport chain (oxidative phosphorylation), normalized gene expression in diseased 
thyroid tissue. The figure was generated using the Pathview package under the GNU General Public License (≥ 3.0), based 
on data from the Kyoto Encyclopedia of Genes and Genomes. Gene names are available at https://www.genenames.org/.

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
13
microenvironment, as shown in Figure S4 (44). Of the 214 differentially expressed genes 
belonging to extracellular matrix components, 139 were overexpressed.
Discussion
In this study, high-quality whole-genome transcriptomes were used to compare gene ex-
pression in healthy and diseased thyroid tissue. The samples reviewed contained detailed 
donor data, allowing advanced corrections to reduce bias. Documented GTEx procedures 
ensure reproducible, systematic RNA-seq analysis and provide structured approaches for 
end users (26).
The comparison shows that extensive transcriptional remodeling occurs in thyroid tis-
sue affected by HT, encompassing multiple cell lineages. No cellular niche was spared, 
with epithelial and endothelial compartments shrinking under the autoimmune assault. 
Particularly striking is the marked increase in transcripts associated with adaptive im-
munity and lymphoid organogenesis (T cells, B cells, plasma cells) (16, 17, 49–51), accom-
panied by increased innate phagocytic activity (52, 53). Both Th1 and Th2 T cell programs 
have been observed, from transcriptional regulators to cytokines (3, 54, 55), alongside 
non-canonical γδ T cells (56), whose role remains unclear (57). There was also evidence of 
inflammatory cell recruitment, antigen presentation (58, 59), complement activation, an-
tibody-dependent cytotoxicity, perforin/granzyme-mediated cytolysis and pro-apoptotic 
signaling (3, 60), consistent with and extending previous findings (3, 61–63). These results 
emphasize that GTEx and bulk RNA-seq are valuable resources when used carefully and 
provide a unified framework linking previous studies of candidate genes, genetic associa-
tions, and animal disease models (54).
This study expands the catalog of downregulated transcripts and highlights the loss of sig-
nature markers for mature follicular epithelial cells (17, 18, 64, 65), decreased expression 
of molecules critical for epithelial communication, and disruption of the thyroxine bio-
synthetic pathway (66). These findings are consistent with histologic evidence of epithelial 
destruction and loss of follicular architecture (1, 3), but have often remained elusive in 
recent mapping efforts (15, 16). We also found transcriptional evidence of mitochondrial 
(15) and ciliary remodeling (67–69), impaired oxidative phosphorylation, impaired ana-
bolic metabolic pathways, and altered planar cell polarity (69, 70). These results comple-
ment the data on the defects in proteostasis (15, 71, 72) and autophagy (73) and provide 
further details on the functional impairments (18). However, the underlying cellular phe-
notypes remain unclear, as thyroid follicular cells likely exist in transitional states along 
the epithelial-mesenchymal continuum (17, 18, 64, 65, 74). The effects of HT on epithelial 
cell composition remain unexplored.
The loss of epithelial markers was accompanied by evidence of endothelial cell dysfunction, 
with significant but uneven downregulation of canonical endothelial (75) and pericyte 
markers, suggesting (peri)vascular remodeling of the angiofollicular unit (76, 77). These 
findings are broadly consistent with concepts of stromal and endothelial reprogramming 
in malignancy and inflammation (48, 78, 79). In such context, perivascular populations 

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 14
may also act as precursors of specialized fibroblasts (16–18, 80), but the fate of the endo-
thelial compartment in HT and its role in thyroid repair or fibrosis remains unclear.
Extensive transcriptional remodeling of the extracellular matrix was observed, including 
the loss of basement membrane collagens and their replacement by newly produced ele-
ments (81). Altered expression of enzymes that regulate collagen deposition, cross-linking 
and matrix turnover was a striking feature of HT thyroids (17). Numerous soluble mole-
cules and growth factors with known roles in stromal and epithelial homeostasis, wound 
healing and stem cell biology were identified (46, 77, 79, 82, 83), linking epithelial-stromal 
interactions (16–18) to differentiation of epithelial stem cells in specialized niches (84, 85). 
The extent of gene deregulation associated with stromal remodeling is consistent with 
thyroid fibrosis, a hallmark of HT, but provides a deeper understanding of the follicular 
microenvironment. A complete single cell count of thyroid fibroblasts remains an unmet 
need.
This transcription atlas provides valuable biomarkers but has important limitations. The 
results have not been replicated in independent cohorts and no immunohistochemical val-
idation of the markers has been performed, which is important because mRNA levels do 
not always correlate with protein expression or cell phenotypes. RNA-seq cannot resolve 
cell-specific gene expression and requires single-cell RNA-seq or scATAC-seq, especially to 
detect rare cell populations. Combining RNA-seq samples across different histologic stages 
of HT can highlight large effects while masking subtle changes. Most of the donors were 
older women, limiting broader applicability. Some of them probably received L-thyroxine 
(T4), which may affect the expression of inflammatory genes to a small extent (86), al-
though it has no effect on overall disease progression.
This study improves and extends the current knowledge of the extent of gene deregula-
tion in thyroid tissue affected by HT. The result of this work is a transcriptomic atlas that 
improves our understanding of the biology of HT and provides a basis for future transla-
tional research.
Provenance: The article is based on the master thesis “Transcriptome analysis of thyroid tissue in 
patients with Hashimoto’s disease by next-generation sequencing” by Marija Čikotić, mag. med. lab. 
diag., at the Josip Juraj Strossmayer University of Osijek, Faculty of Medicine Osijek under the super-
vision of Assoc. Prof. Mario Štefanić, PhD, and is deposited in the repository of Faculty of Medicine 
(https://repozitorij.mefos.hr/islandora/object/mefos%3A1630).
Received: 4 December 2024 / Accepted: 24 July 2025 / Published online: 17 October 2025
Peer review: Externally peer reviewed.
Acknowledgements: The results published here are in part based upon data generated by the 
Genotype-Tissue Expression (GTEx) Project (https://commonfund.nih.gov/gtex). The GTEx Project is 
supported by the Common Fund of the Office of the Director of the NIH, and by National Cancer 
Institute, National Human Genome Research Institute, National Heart, Lung, and Blood Institute, 
National Institute on Drug Abuse, National Institute of Mental Health, and National Institute of 
Neurological Disorders and Stroke. Date of access: 20 Oct 2019.
Ethics considerations: The study was approved by the Ethics Committee of the University of Osijek 
Faculty of Medicine (Reg. No. 2158-61-46-22-89).
Funding: No funding was received for this study.

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
15
Authorship declaration: All authors conceptualized the article, participated in the writing, revising, 
editing, and finalizing the manuscript. All authors read and approved the final manuscript and they 
all take accountability for the work.
Availability of data: Supplementary figures and tables for this study are available at the Open 
Science Framework: https://osf.io/639s2/?view_only=209ef4e6159645369a6d935fcd18531f (44).
Disclosure of interest: The authors completed the ICMJE Disclosure of Interest Form and disclosed 
no relevant interests.
ORCID
Marieta Bujak 
  https://orcid.org/0000-0001-9926-3203
Silvija Piškorjanac 
  https://orcid.org/0009-0002-6133-4285
Mario Štefanić 
  https://orcid.org/0000-0001-8995-6137
References
1. Pearce EN, Farwell AP, Braverman LE. Thyroiditis. N Engl J Med. 2003 Jun 26;348(26):2646–55. 
doi: 10.1056/NEJMra021194
2. Ragusa F, Fallahi P, Elia G, Gonnella D, Paparo SR, Giusti C, et al. Hashimotos’ thyroiditis: 
epidemiology, pathogenesis, clinic and therapy. Best Pract Res Clin Endocrinol Metab. 2019 
Dec;33(6):101367. doi: 10.1016/j.beem.2019.101367
3. Stassi G, De Maria R. Autoimmune thyroid disease: new models of cell death in autoimmunity. 
Nat Rev Immunol. 2002 Mar;2(3):195–204. doi: 10.1038/nri750
4. Wiersinga WM. Paradigm shifts in thyroid hormone replacement therapies for hypothyroidism. 
Nat Rev Endocrinol. 2014 Mar;10(3):164–74. doi: 10.1038/nrendo.2013.258
5. Hegedüs L, Bianco AC, Jonklaas J, Pearce SH, Weetman AP, Perros P. Primary hypothyroidism 
and quality of life. Nat Rev Endocrinol. 2022 Apr;18(4):230–42. doi: 10.1038/s41574-021-00625-8
6. Feller M, Snel M, Moutzouri E, Bauer DC, de Montmollin M, Aujesky D, et al. Association of 
thyroid hormone therapy with quality of life and thyroid-related symptoms in patients 
with subclinical hypothyroidism: A systematic review and meta-analysis. JAMA. 2018 Oct 
2;320(13):1349–59. doi: 10.1001/jama.2018.13770
7. Lillevang-Johansen M, Abrahamsen B, Jørgensen HL, Brix TH, Hegedüs L. Over- and under-
treatment of hypothyroidism is associated with excess mortality: a register-based cohort study. 
Thyroid. 2018 May;28(5):566–74. doi: 10.1089/thy.2017.0517
8. Carafone L, Knutson AJ, Gigliotti BJ. A review of autoimmune thyroid diseases and their complex 
interplay with female fertility. Semin Reprod Med. 2024 Sep;42(3):178–92. doi: 10.1055/s-0044-
1795160
9. De Leo S, Pearce EN. Autoimmune thyroid disease during pregnancy. Lancet Diabetes 
Endocrinol. 2018 Jul;6(7):575–86. doi: 10.1016/S2213-8587(17)30402-3
10. McLeod DSA, Watters KF, Carpenter AD, Ladenson PW, Cooper DS, Ding EL. Thyrotropin 
and thyroid cancer diagnosis: a systematic review and dose–response meta-analysis. J Clin 
Endocrinol Metab. 2012 Aug;97(8):2682–92. doi: 10.1210/jc.2012-1083
11. Resende de Paiva C, Grønhøj C, Feldt-Rasmussen U, von Buchwald C. Association between 
Hashimoto’s thyroiditis and thyroid cancer in 64,628 patients. Front Oncol. 2017 Apr 10;7:53. 
doi: 10.3389/fonc.2017.00053
12. Stark R, Grzelak M, Hadfield J. RNA sequencing: the teenage years. Nat Rev Genet. 2019 
Nov;20(11):631–56. doi: 10.1038/s41576-019-0150-2
13. McCombie WR, McPherson JD, Mardis ER. Next-generation sequencing technologies. Cold 
Spring Harb Perspect Med. 2019 Nov 1;9(11). doi: 10.1101/cshperspect.a036798

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 16
14. Chen H, Ye F, Guo G. Revolutionizing immunology with single-cell RNA sequencing. Cell Mol 
Immunol. 2019 Mar;16(3):242–9. doi: 10.1038/s41423-019-0214-4
15. Cho BA, Yoo SK, Song YS, Kim SJ, Lee KE, Shong M, et al. Transcriptome network analysis reveals 
aging-related mitochondrial and proteasomal dysfunction and immune activation in human 
thyroid. Thyroid. 2018 May;28(5):656–66. doi: 10.1089/thy.2017.0359
16. Zhang QY, Ye XP, Zhou Z, Zhu CF, Li R, Fang Y, et al. Lymphocyte infiltration and thyrocyte 
destruction are driven by stromal and immune cell components in Hashimoto’s thyroiditis. Nat 
Commun. 2022 Feb 9;13(1):775. doi: 10.1038/s41467-022-28120-2
17. Martínez-Hernández R, Sánchez de la Blanca N, Sacristán-Gómez P, Serrano-Somavilla A, 
Muñoz De Nova JL, Sánchez Cabo F, et al. Unraveling the molecular architecture of autoimmune 
thyroid diseases at spatial resolution. Nat Commun. 2024 Jul 13;15:5895. doi: 10.1038/s41467-
024-50192-5
18. Massalha H. Trinh MK, Armingol E, Tuck L, Predeus A, Mazin P, et al. A developmental cell 
atlas of the human thyroid gland. bioRxiv. 2024 Aug 22:2024.08.22.609152. [Preprint]. doi: 
10.1101/2024.08.22.609152
19. Leek JT, Scharpf RB, Bravo HC, Simcha D, Langmead B, Johnson WE, et al. Tackling the 
widespread and critical impact of batch effects in high-throughput data. Nat Rev Genet. 2010 
Oct;11(10):733–9. doi: 10.1038/nrg2825
20. Ferreira PG, Muñoz-Aguirre M, Reverter F, Sá Godinho CP, Sousa A, Amadoz A, et al. The effects 
of death and post-mortem cold ischemia on human tissue transcriptomes. Nat Commun. 2018 
Feb 13;9(1):490. doi: 10.1038/s41467-017-02772-x
21. van den Brink SC, Sage F, Vértesy Á, Spanjaard B, Peterson-Maduro J, Baron CS, et al. Single-
cell sequencing reveals dissociation-induced gene expression in tissue subpopulations. Nat 
Methods. 2017 Sep 29;14:935–6. doi: 10.1038/nmeth.4437
22. Nieuwenhuis TO, Yang SY, Verma RX, Pillalamarri V, Arking DE, Rosenberg AZ, et al. Consistent 
RNA sequencing contamination in GTEx and other data sets. Nat Commun. 2020 Apr 
22;11(1):1933. doi: 10.1038/s41467-020-15821-9
23. Luecken MD, Theis FJ. Current best practices in single-cell RNA-seq analysis: a tutorial. Mol Syst 
Biol. 2019 Jun 19;15(6):e8746. doi: 10.15252/msb.20188746
24. GTEx Consortium. The Genotype-Tissue Expression (GTEx) project. Nat Genet. 2013 
Jun;45(6):580–5. doi: 10.1038/ng.2653
25. GTEx Consortium. Human genomics. The Genotype-Tissue Expression (GTEx) pilot analysis: 
multitissue gene regulation in humans. Science. 2015 May 8;348(6235):648–60. doi: 10.1126/
science.1262110
26. Carithers LJ, Ardlie K, Barcus M, Branton PA, Britton A, Buia SA, et al. A novel approach to 
high-quality postmortem tissue procurement: the GTEx Project. Biopreserv Biobank. 2015 
Oct;13(5):311–9. doi: 10.1089/bio.2015.0032
27. Hardy JA, Wester P, Winblad B, Gezelius C, Bring G, Eriksson A. The patients dying after long 
terminal phase have acidotic brains; implications for biochemical measurements on autopsy 
tissue. J Neural Transm. 1985;61:253–64. doi: 10.1007/BF01251916
28. Robinson MD, Oshlack A. A scaling normalization method for differential expression analysis 
of RNA-seq data. Genome Biol. 2010;11(3):R25. doi: 10.1186/gb-2010-11-3-r25
29. Robinson MD, McCarthy DJ, Smyth GK. edgeR: a Bioconductor package for differential 
expression analysis of digital gene expression data. Bioinformatics. 2010 Jan 1;26(1):139–40. 
doi: 10.1093/bioinformatics/btp616
30. Chien LC. A rank-based normalization method with the fully adjusted full-stage procedure 
in genetic association studies. PLoS One. 2020 Jun 19;15(6):e0233847. doi: 10.1371/journal.
pone.0233847
31. Leek JT, Johnson WE, Parker HS, Jaffe AE, Storey JD. The sva package for removing batch 
effects and other unwanted variation in high-throughput experiments. Bioinformatics. 2012 
Mar;28(6):882–3. doi: 10.1093/bioinformatics/bts034
32. Yi H, Raman AT, Zhang H, Allen GI, Liu Z. Detecting hidden batch factors through data-
adaptive adjustment for biological effects. Bioinformatics. 2018 Apr;34(7):1141–7. doi: 10.1093/
bioinformatics/btx630
33. Robinson MD, Smyth GK. Moderated statistical tests for assessing differences in tag abundance. 
Bioinformatics. 2007 Nov;23(21):2881–7. doi: 10.1093/bioinformatics/btm453

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
17
34. Ritchie ME, Phipson B, Wu D, Hu Y, Law CW, Shi W, et al. limma powers differential expression 
analyses for RNA-sequencing and microarray studies. Nucleic Acids Res. 2015 Apr 20;43(7):e47. 
doi: 10.1093/nar/gkv007
35. Phipson B, Lee S, Majewski IJ, Alexander WS, Smyth GK. Robust hyperparameter estimation 
protects against hypervariable genes and improves power to detect differential expression. 
Ann Appl Stat. 2016 Jun;10(2):946–63. doi: 10.1214/16-AOAS920
36. Kanehisa M, Furumichi M, Tanabe M, Sato Y, Morishima K. KEGG: new perspectives on genomes, 
pathways, diseases and drugs. Nucleic Acids Res. 2017 Jan 4;45(D1):D353–D361. doi: 10.1093/
nar/gkw1092
37. Liberzon A, Birger C, Thorvaldsdóttir H, Ghandi M, Mesirov JP, Tamayo P. The Molecular 
Signatures Database (MSigDB) hallmark gene set collection. Cell Syst. 2015 Dec 23;1(6):417–25. 
doi: 10.1016/j.cels.2015.12.004
38. Tilford CA, Siemers NO. Gene set enrichment analysis. In: Nikolsky Y, Bryant J, editors. Protein 
networks and pathway analysis. Methods in Molecular Biology, vol 563. Totowa, NJ: Humana 
Press; 2009. p. 99–121. doi: 10.1007/978-1-60761-175-2_6
39. Luo W, Brouwer C. Pathview: an R/Bioconductor package for pathway-based data integration 
and visualization. Bioinformatics. 2013 Jul;29(14):1830–1. doi: 10.1093/bioinformatics/btt285
40. Hao Y, Hao S, Andersen-Nissen E, Mauck WM 3rd, Zheng S, Butler A, et al. Integrated analysis of 
multimodal single-cell data. Cell. 2021 Jun 24;184(13):3573–87.e29. doi: 10.1016/j.cell.2021.04.048
41. Xie Z, Bailey A, Kuleshov MV, Clarke DJB, Evangelista JE, Jenkins SL, et al. Gene set knowledge 
discovery with Enrichr. Curr Protoc. 2021 Mar;1(3):e90. doi: 10.1002/cpz1.90
42. Pinto JP, Kalathur RK, Oliveira DV, Barata T, Machado RS, Machado S, et al. StemChecker: a web-
based tool to discover and explore stemness signatures in gene sets. Nucleic Acids Res. 2015 Jul 
1;43(W1):W72–7. doi: 10.1093/nar/gkv529 
43. Sekhon JS. Multivariate and propensity score matching software with automated balance 
optimization: the matching package for R. J Stat Soft. 2011 Jun 14;42(7):1–52. doi: 10.18637/jss.
v042.i07 
44. Bujak M. Transcriptome analysis of thyroid tissue in patients with Hashimoto’s disease using 
next-generation sequencing [Internet]. 2025. [cited 2025 Sep 5]. Available from https://osf.
io/639s2/?view_only=209ef4e6159645369a6d935fcd18531f
45. Domínguez Conde C, Xu C, Jarvis LB, Rainbow DB, Wells SB, Gomes T, et al. Cross-tissue immune 
cell analysis reveals tissue-specific features in humans. Science. 2022 May 13;376(6594):eabl5197. 
doi: 10.1126/science.abl5197
46. Butler MT, Wallingford JB. Planar cell polarity in development and disease. Nat Rev Mol Cell 
Biol. 2017 Jun;18(6):375–88. doi: 10.1038/nrm.2017.11
47. Winkler EA, Kim CN, Ross JM, Garcia JH, Gil E, Oh I, et al. A single-cell atlas of the normal and 
malformed human brain vasculature. Science. 2022 Mar 4;375(6584):eabi7377. doi: 10.1126/
science.abi7377
48. Korsunsky I, Wei K, Pohin M, Kim EY, Barone F, Major T, et al. Cross-tissue, single-cell stromal 
atlas identifies shared pathological fibroblast phenotypes in four chronic inflammatory 
diseases. Med (New York, N.Y.). 2022 Jul 8;3(7):481–518.e14. doi: 10.1016/j.medj.2022.05.002
49. Tang H, Zhu M, Qiao J, Fu YX. Lymphotoxin signalling in tertiary lymphoid structures and 
immunotherapy. Cell Mol Immunol. 2017;14:809–18. doi: 10.1038/cmi.2017.13
50. Marinkovic T, Garin A, Yokota Y, Fu YX, Ruddle NH, Furtado GC, et al. Interaction of mature 
CD3+CD4+ T cells with dendritic cells triggers the development of tertiary lymphoid structures 
in the thyroid. J Clin Invest. 2006 Oct;116(10):2622–32. doi: 10.1172/JCI28993
51. Furtado GC, Marinkovic T, Martin AP, Garin A, Hoch B, Hubner W, et al. Lymphotoxin beta 
receptor signaling is required for inflammatory lymphangiogenesis in the thyroid. Proc Natl 
Acad Sci USA. 2007 Mar 20;104(12):5026–31. doi: 10.1073/pnas.0606697104
52. Sanin DE, Ge Y, Marinkovic E, Kabat AM, Castoldi A, Caputa G, et al. A common framework 
of monocyte-derived macrophage activation. Sci Immunol. 2022 Apr 15;7(70):eabl7482. doi: 
10.1126/sciimmunol.abl7482
53. Villani AC, Satija R, Reynolds G, Sarkizova S, Shekhar K, Fletcher J, et al. Single-cell RNA-seq 
reveals new types of human blood dendritic cells, monocytes, and progenitors. Science. 2017 
Apr 21;356(6335):eaah4573. doi: 10.1126/science.aah4573

RESEARCH ARTICLE
Čikotić et al.
st-open.unist.hr
 18
54. Yang X, Gao T, Shi R, Zhou X, Qu J, Xu J, et al. Effect of iodine excess on Th1, Th2, Th17, and Treg 
cell subpopulations in the thyroid of NOD.H-2h4 mice. Biol Trace Elem Res. 2014;159:288–96. 
doi: 10.1007/s12011-014-9958-y
55. Shi Y, Wang H, Su Z, Chen J, Xue Y, Wang S, et al. Differentiation imbalance of Th1/Th17 in 
peripheral blood mononuclear cells might contribute to pathogenesis of Hashimoto’s thyroiditis. 
Scand J Immunol. 2010;72:250–5. doi: 10.1111/j.1365-3083.2010.02425.x
56. Liu H, Zheng T, Mao Y, Xu C, Wu F, Bu L, et al. γδ T cells enhance B cells for antibody production 
in Hashimoto’s thyroiditis, and retinoic acid induces apoptosis of the γδ T cell. Endocrine. 
2016;51:113–22. doi: 10.1007/s12020-015-0631-9
57. Pizzolato G, Kaminski H, Tosolini M, Franchini DM, Pont F, Martins F, et al. Single-cell RNA 
sequencing unveils the shared and the distinct cytotoxic hallmarks of human TCRVδ1 and 
TCRVδ2 γδ T lymphocytes. Proc Natl Acad Sci USA. 2019 Jun 11;116(24):11906–15. doi: 10.1073/
pnas.1818488116
58. Jacobson EM, Huber A, Tomer Y. The HLA gene complex in thyroid autoimmunity: from 
epidemiology to etiology. J Autoimmun. 2008 Feb–Mar;30(1–2):58–62. doi: 10.1016/j.
jaut.2007.11.010
59. Zeitlin AA, Heward JM, Newby PR, Carr-Smith JD, Franklyn JA, Gough SC, et al. Analysis of HLA 
class II genes in Hashimoto’s thyroiditis reveals differences compared to Graves’ disease. Genes 
Immun. 2008;9:358–63. doi: 10.1038/gene.2008.26
60. Liu Y, You R, Yu N, Gong Y, Qu C, Zhang Y, et al. Increased proportions of Tc17 cells and NK cells 
may be risk factors for disease progression in Hashimoto’s thyroiditis. Int Immunopharmacol. 
2016 Nov;40:332–8. doi: 10.1016/j.intimp.2016.09.016
61. Ajjan RA, Weetman AP. The Pathogenesis of Hashimoto’s Thyroiditis: Further Developments in 
our Understanding. Horm Metab Res. 2015;47(10):702–10. doi: 10.1055/s-0035-1548832
62. Liu J, Mao C, Dong L, Kang P, Ding C, Zheng T, et al. Excessive iodine promotes pyroptosis of 
thyroid follicular epithelial cells in Hashimoto’s thyroiditis through the ROS-NF-κB-NLRP3 
pathway. Front Endocrinol (Lausanne). 2019 Nov 20;10:778. doi: 10.3389/fendo.2019.00778
63. Hwangbo Y, Park YJ. Genome-Wide Association Studies of Autoimmune Thyroid Diseases, 
Thyroid Function, and Thyroid Cancer. Endocrinol Metab (Seoul). 2018 Jun;33(2):175–84. doi: 
10.3803/EnM.2018.33.2.175
64. Liang J, Qian J, Yang L, Chen X, Wang X, Lin X, et al. Modeling human thyroid development 
by fetal tissue-derived organoid culture. Adv Sci (Weinh). 2022;9:e2105568. doi: 10.1002/
advs.202105568
65. Liao T, Zeng Y, Xu W, Shi X, Shen C, Du Y, et al. A spatially resolved transcriptome landscape 
during thyroid cancer progression. Cell Rep Med. 2025 Apr 15;6(4):102043. doi: 10.1016/j.
xcrm.2025.102043
66. Chaker L, Razvi S, Bensenor IM, Azizi F, Pearce EN, Peeters RP. Hypothyroidism. Nat Rev Dis 
Primers. 2022;8:30. doi: 10.1038/s41572-022-00357-7
67. Lee J, Yi S, Eun Kang Y, Young Chang J, Tae Kim J, Joung Sul H, et al. Defective ciliogenesis in thyroid 
Hürthle cell tumors is associated with increased autophagy. Oncotarget. 2016;7(48):79117–30. 
doi: 10.18632/oncotarget.12997
68. Lee J, Park KC, Sul HJ, Hong HJ, Kim KH, Kero J, et al. Loss of primary cilia promotes mitochondria-
dependent apoptosis in thyroid cancer. Sci Rep. 2021 Feb 18;11(1):4181. doi: 10.1038/s41598-
021-83418-3
69. Martínez-Hernández R, Serrano-Somavilla A, Ramos-Leví A, Sampedro-Nuñez M, Lens-Pardo 
A, Muñoz De Nova JL, et al. Integrated miRNA and mRNA expression profiling identifies novel 
targets and pathological mechanisms in autoimmune thyroid diseases. EBioMedicine. 2019 
Dec;50:329–42. doi: 10.1016/j.ebiom.2019.10.061
70. Koumarianou P, Gómez-López G, Santisteban P. Pax8 controls thyroid follicular polarity through 
cadherin-16. J Cell Sci. 2017 Jan 1;130(1):219–31. doi: 10.1242/jcs.184291
71. Wright MT, Kouba L, Plate L. Thyroglobulin interactome profiling defines altered proteostasis 
topology associated with thyroid dyshormonogenesis. Mol Cell Proteomics. 2021;20:100008. 
doi: 10.1074/mcp.RA120.002168
72. Read ML, Brookes K, Thornton CEM, Fletcher A, Nieto HR, Alshahrani M, et al. Targeting non-
canonical pathways as a strategy to modulate the sodium iodide symporter. Cell Chem Biol. 
2022 Mar 17;29(3):502–12.e7. doi: 10.1016/j.chembiol.2021.07.016

RESEARCH ARTICLE
2025 Vol. 6 • e2025.2219.27
st-open.unist.hr
19
73. Zheng T, Xu C, Mao C, Mou X, Wu F, Wang X, et al. Increased interleukin-23 in Hashimoto’s 
thyroiditis disease induces autophagy suppression and reactive oxygen species accumulation. 
Front Immunol. 2018 Jan 29;9:96. doi: 10.3389/fimmu.2018.00096
74. Yang RM, Song SY, Wu FY, Yang RF, Shen YT, Tu PH, et al. Myeloid cells interact with a subset 
of thyrocytes to promote their migration and follicle formation through NF-κB. Nat Commun. 
2023 Dec 6;14(1):8082. doi: 10.1038/s41467-023-43895-8
75. Becker LM, Chen SH, Rodor J, de Rooij LPMH, Baker AH, Carmeliet P. Deciphering endothelial 
heterogeneity in health and disease at single cell resolution: progress and perspectives. 
Cardiovasc Res. 2023 Mar 17;119(1):6–27. doi: 10.1093/cvr/cvac018
76. Buechler MB, Pradhan RN, Krishnamurty AT, Cox C, Calviello AK, Wang AW, et al. Cross-tissue 
organization of the fibroblast lineage. Nature. 2021 May;593(7860):575–9. doi: 10.1038/s41586-
021-03549-5
77. Muhl L, Genové G, Leptidis S, Liu J, He L, Mocci G, et al. Single-cell analysis uncovers fibroblast 
heterogeneity and criteria for fibroblast and mural cell identification and discrimination. Nat 
Commun. 2020 Aug 7;11(1):3953. doi: 10.1038/s41467-020-17740-1
78. Davidson S, Coles M, Thomas T, Kollias G, Ludewig B, Turley S, et al. Fibroblasts as immune 
regulators in infection, inflammation and cancer. Nat rev Immunol. 2021 Nov;21(11):704–17. 
doi: 10.1038/s41577-021-00540-z
79. Lendahl U, Muhl L, Betsholtz C. Identification, discrimination and heterogeneity of fibroblasts. 
Nat Commun. 2022 Jun 14;13(1):3409. doi: 10.1038/s41467-022-30633-9 
80. Di Carlo SE, Peduto L. The perivascular origin of pathological fibroblasts. J Clin Invest. 2018 Jan 
2;128(1):54–63. doi: 10.1172/JCI93558
81. Bignon M, Pichol-Thievend C, Hardouin J, Malbouyres M, Bréchot N, Nasciutti L, et al. Lysyl 
oxidase-like protein-2 regulates sprouting angiogenesis and type IV collagen assembly 
in the endothelial basement membrane. Blood. 2011 Oct 6;118(14):3979–89. doi: 10.1182/
blood-2010-10-313296
82. Nakata Y, Mayassi T, Lin H, Ghosh K, Segerstolpe Å, et al. Genetic vulnerability to Crohn’s 
disease reveals a spatially resolved epithelial restitution program. Sci Transl Med. 2023 Oct 
25;15(719):eadg5252. doi: 10.1126/scitranslmed.adg5252
83. Trempus CS, Papas BN, Sifre MI, Bortner CD, Scappini E, Tucker CJ, et al. Functional 
Pdgfra fibroblast heterogeneity in normal and fibrotic mouse lung. JCI INsight. 2023 Nov 
22;8(22):e164380. doi: 10.1172/jci.insight.164380
84. Kato K, Diéguez-Hurtado R, Park DY, Hong SP, Kato-Azuma S, Adams S, et al. Pulmonary pericytes 
regulate lung morphogenesis. Nat Commun. 2018 Jun 22;9(1):2448. doi: 10.1038/s41467-018-
04913-2
85. Kim JE, Fei L, Yin WC, Coquenlorge S, Rao-Bhatia A, Zhang H, et al. Single-cell and genetic 
analyses reveal conserved populations and signaling mechanisms of gastrointestinal stromal 
niches. Nat Commun. 2020 Jan 17;11(1):334. doi: 10.1038/s41467-019-14058-5
86. Wang L, Li Z, Wan R, Pan X, Li B, Zhao H, et al. Single-cell RNA sequencing provides new insights 
into therapeutic roles of thyroid hormone in idiopathic pulmonary fibrosis. Am J Respir Cell 
Mol Biol. 2023 Oct;69(4):456–69. doi: 10.1165/rcmb.2023-0080OC