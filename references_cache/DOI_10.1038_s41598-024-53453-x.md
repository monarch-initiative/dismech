---
reference_id: DOI:10.1038/s41598-024-53453-x
title: Exploring the association between rosacea and acne by integrated bioinformatics analysis
authors:
- Jingchen Liang
- Ying Chen
- Zihao Wang
- Yawen Wang
- Shengzhi Mu
- Dewu Zhang
- Zhao Wang
- Weihui Zeng
journal: Scientific Reports
year: '2024'
doi: 10.1038/s41598-024-53453-x
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41598-024-53453-x.pdf"
oa_status: gold
license: cc-by
local_pdf_path: files/DOI_10.1038_s41598-024-53453-x.pdf
---

# Exploring the association between rosacea and acne by integrated bioinformatics analysis
**Authors:** Jingchen Liang, Ying Chen, Zihao Wang, Yawen Wang, Shengzhi Mu, Dewu Zhang, Zhao Wang, Weihui Zeng
**Journal:** Scientific Reports (2024)
**DOI:** [10.1038/s41598-024-53453-x](https://doi.org/10.1038/s41598-024-53453-x)

## Content

Abstract
Clinically, rosacea occurs frequently in acne patients, which hints the existence of shared signals. However, the connection between the pathophysiology of rosacea and acne are not yet fully understood. This study aims to unveil molecular mechanism in the pathogenesis of rosacea and acne. We identified differentially expressed genes (DEGs) by limma and weighted gene co-expression network analysis and screened hub genes by constructing a protein–protein interaction network. The hub genes were verified in different datasets. Then, we performed a correlation analysis between the hub genes and the pathways. Finally, we predicted and verified transcription factors of hub genes, performed the immune cell infiltration analysis using CIBERSORT, and calculated the correlation between hub genes and immune cells. A total of 169 common DEGs were identified, which were mainly enriched in immune-related pathways. Finally, hub genes were identified as IL1B, PTPRC, CXCL8, MMP9, CCL4, CXCL10, CD163, CCR5, CXCR4, and TLR8. 9 transcription factors that regulated the expression of hub genes were identified. The infiltration of γδT cells was significantly increased in rosacea and acne lesions and positively linked with almost all hub genes. These identified hub genes and immune cells may play a crucial role in the development of rosacea and acne.

1
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports
Exploring the association 
between rosacea and acne 
by integrated bioinformatics 
analysis
Jingchen Liang 1,4, Ying Chen 1,4, Zihao Wang 2, Yawen Wang 1, Shengzhi Mu 3, Dewu Zhang 1, 
Zhao Wang 1* & Weihui Zeng 1*
Clinically, rosacea occurs frequently in acne patients, which hints the existence of shared signals. 
However, the connection between the pathophysiology of rosacea and acne are not yet fully 
understood. This study aims to unveil molecular mechanism in the pathogenesis of rosacea and acne. 
We identified differentially expressed genes (DEGs) by limma and weighted gene co-expression 
network analysis and screened hub genes by constructing a protein–protein interaction network. The 
hub genes were verified in different datasets. Then, we performed a correlation analysis between the 
hub genes and the pathways. Finally, we predicted and verified transcription factors of hub genes, 
performed the immune cell infiltration analysis using CIBERSORT, and calculated the correlation 
between hub genes and immune cells. A total of 169 common DEGs were identified, which were 
mainly enriched in immune-related pathways. Finally, hub genes were identified as IL1B, PTPRC, 
CXCL8, MMP9, CCL4, CXCL10, CD163, CCR5, CXCR4, and TLR8. 9 transcription factors that regulated 
the expression of hub genes were identified. The infiltration of γδT cells was significantly increased in 
rosacea and acne lesions and positively linked with almost all hub genes. These identified hub genes 
and immune cells may play a crucial role in the development of rosacea and acne.
Rosacea is a chronic inflammatory disease that typically affects women over 30. Clinically, rosacea can be divided 
into four subtypes: erythematotelangiectatic rosacea (ETR), papulopustular rosacea (PPR), phymatous rosacea 
(PHR), and ocular rosacea (OR). According to the global ROSacea COnsensus 2019 panel, the major features 
of rosacea include: (a) Temporary increase in centrofacial redness, which may include sensations of warmth, 
heat, burning and/or pain; (b) Red papules and pustules, usually in the centrofacial area. Some may be larger 
and deeper; (c) Visible vessels in the centrofacial region but not only in the alar  area1. Rosacea can be induced 
by external factors such as sun exposure, heat and cold, hot drinks, and spicy food, but its specific etiology 
remains  unknown2.
Acne vulgaris (also known as acne) is also a chronic inflammatory disease that mostly affects the face, neck, 
chest, and back. Acne characterized by inflammatory papules, pustules, nodules, cysts, etc. It may be caused by 
androgen-induced increased sebum production, altered keratinization, inflammation, and bacterial colonization 
of hair follicles by Propionibacterium acnes (P . acnes)3. Although some predisposing factors have been identified, 
exactly what triggers acne and how treatment affects the course of the disease remain  unclear3. Due to the clinical 
characteristics of these two diseases, they frequently have substantial negative impacts on mood and quality of 
life of patients and, in extreme circumstances, can induce anxiety and  depression4.
Clinically, people with rosacea are often combined with other skin diseases, such as acne, folliculitis, sebor -
rheic dermatitis, and hormone-dependent dermatitis, especially acne. And we also frequently see patients who 
develop from acne to rosacea. According to Chen’s study, ETR is the most common rosacea type in 563 female 
acne patients combined with  rosacea5. Due to the fact that acne also includes clinical manifestations such as 
papules and pustules, and some acne patients also have papules and erythema at the same time, rosacea is often 
easily to be missed or misdiagnosed when acne and rosacea coexist. Although the causative association between 
rosacea and acne is still unclear, genetics, microbiomes, innate and adaptive immunological dysregulation, and 
OPEN
1Department of Dermatology, The Second Affiliated Hospital of Xi’an Jiaotong University, Xi’an, China. 2Department 
of Cardiology, The First Affiliated Hospital of Xi’an Jiaotong University, Xi’an, China. 3Department of Burn and 
Plastic Surgery, Shaanxi Provincial People’s Hospital, Xi’an, China.  4 These authors contributed equally: Jingchen 
Liang and Ying Chen. *email: wang.zhao@xjtu.edu.cn; zengwh88@126.com

2
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
skin barrier dysfunction have been implicated as cross-pathogenetic  factors5. To explore the common pathogen-
esis of rosacea and acne, we used the datasets from the Gene Expression Omnibus (GEO) database to perform 
related analyses to identify the common DEGs, pathways and immune mechanisms of these two diseases. Addi-
tionally, we screened out the hub genes and transcription factors (TFs) that promote the pathogenesis of these 
two diseases in order to provide a novel insight into the common pathogenesis of rosacea and acne.
Results
Datasets processing and identification of DEGs
To maximize sample size, we pooled  GSE1081106 and  GSE537957. Batch effects refer to technical differences aris-
ing from the processing and measurement of samples in different batches. To avoid batch effects having an impact 
on subsequent analyses, we eliminated the batch effects from the merging dataset. The boxplot revealed that the 
distributions of the samples in each dataset differed significantly before batch effects were eliminated, suggesting 
the presence of batch effects (Supplementary Fig. 1A). After eliminating the batch effect, the sample distribution 
of two datasets converged, with the median falling on a straight line (Supplementary Fig. 1B). Uniform Manifold 
Approximation and Projection (UMAP) indicated that the samples of two datasets were clustered and intertwined 
after the batch effect was eliminated, suggesting that the batch effect was eliminated effectively (Supplementary 
Fig. 1C,D). The merging dataset and  GSE659148 were deduplicated and averaged according to the gene name.
To identify genes that were significantly up-regulated and down-regulated in the rosacea and acne datasets, 
we performed differential gene expression analysis of the two datasets. We compared the expression levels of all 
genes in the rosacea and acne datasets and identified 913 DEGs (552 up-regulated genes and 361 down-regulated 
genes) and 424 DEGs (286 up-regulated genes and 138 down-regulated genes) in rosacea and acne datasets, 
respectively (adjusted P-value < 0.05 and |log2FC (fold change)|> 1). The volcano plot showed DEGs with adjusted 
P-value < 0.05 and |log2FC|> 1 (Fig. 1A,C), where orange indicated higher gene expression, blue indicated lower 
gene expression, and black indicated genes with no significant difference in expression. All DEGs of rosacea and 
acne datasets were shown as heatmaps (Fig. 1B,D). Each column in the heatmaps represented a sample, the blue 
part on the left is the healthy control (HC) group, and the pink part on the right is the lesional group. Each row 
represented a gene, where orange indicated higher gene expression and blue indicated lower gene expression, 
displaying rough separation of lesional and HC groups.
WGCNA of GSE65914
To further identify the hub genes of the rosacea dataset, weighted gene co-expression network analysis (WGCNA) 
was performed on GSE65914. In the results of our study, soft thresholding power (β) was selected as 6. Fig-
ure 2A showed the correlation between rosacea and gene co-expression modules. We found that the magenta 
and brown modules had the strongest correlation with rosacea. There were 1350 genes in the magenta module 
and 1070 genes in the brown module. Then, we took the intersection of the DEGs of rosacea dataset with genes 
in the magenta module and the DEGs of rosacea dataset with genes in the brown module separately, a total of 
672 rosacea-co-DEGs were identified (Fig.  2B,C). Subsequently, we took the intersection of rosacea-co-DEGs 
and the DEGs of acne dataset, a total of 169 co-DEGs were identified, including 151 up-regulated genes and 18 
down-regulated genes (adjusted P-value < 0.05) (Fig. 2D,E).
GO and KEGG pathway enrichment analysis
To identify the functions and the pathways enriched by the genes which we interested in, Gene Ontology (GO) 
and Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway enrichment analysis were performed for 
rosacea-co-DEGs (Supplementary Fig. 2), DEGs of acne dataset (Supplementary Fig. 3), and co-DEGs (Fig.  3), 
respectively. Here, we focused on illustrating the results of the enrichment analysis of co-DEGs. The GO pathways 
of the up-regulated co-DEGs were mainly enriched in leukocyte chemotaxis, neutrophil migration, leukocyte 
migration, etc. (Fig. 3A). While the GO pathways of down-regulated co-DEGs were mainly enriched in keratan 
sulfate catabolic process, keratan sulfate biosynthetic process, keratan sulfate metabolic process, etc. (Fig.  3C). 
Furthermore, KEGG pathway analysis demonstrated that up-regulated co-DEGs participated in chemokine 
signaling pathway, cytokine-cytokine receptor interaction, IL-17 signaling pathway, rheumatoid arthritis, NF-κB 
signaling pathway, TNF signaling pathway, and Toll-like receptor signaling pathway (Fig.  3B). While down-
regulated co-DEGs participated in ErbB signaling pathway and ECM-receptor interaction (Fig.  3C).
Construction of PPI network and identification of hub genes
In order to further identify the common hub genes of rosacea and acne, the protein–protein interaction (PPI) 
network of co-DEGs was constructed and visualized (Fig. 4A). The genes in the intersection of eight commonly 
used algorithms in cytoHubba plug-in were identified as hub genes (Fig.  4C). Then, based on the PPI network, 
we identified 11 hub genes, including IL1B, PTPRC, CXCL8, MMP9, CCL4, CXCL10, CD163, CCR5, CXCR4, 
TLR8, and CXCL9. Their full names and functions were listed in Supplementary Table 1. Figure 4B was the cluster 
with the highest score selected by the MCODE plug-in, all 11 hub genes were marked in red.
Verification of hub genes in GSE6475 and correlation between hub genes
To verify the hub genes, the expression levels and ROC analysis of 11 hub genes were performed in  GSE64759 
(Fig. 5). Genes with significantly different expression levels (P-value < 0.05) and an AUC > 0.8 were regarded 
as hub genes. Finally, IL1B, PTPRC, CXCL8, MMP9, CCL4, CXCL10, CD163, CCR5, CXCR4, and TLR8 were 
identified, and the corheatmap showed that there was a positive strong correlation between all hub genes in 
rosacea and acne lesions (Fig. 6C,D).

3
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
The co-expression network of hub genes was shown in Fig.  4D. GO pathway enrichment analysis revealed 
that these hub genes were mainly enriched in cytokine-mediated signaling pathway, cellular response to cytokine 
stimulus, response to cytokine, etc. (P-value < 0.05) (Fig. 6A). KEGG pathway enrichment analysis revealed that 
they were mainly involved in viral protein interaction with cytokine and cytokine receptor, Toll-like receptor 
signaling pathway, etc. (P-value < 0.05) (Fig. 6B).
Correlation between hub genes and pathways
To explore the relationship between the hub genes and pathways, the gene set enrichment analysis (GSEA) of the 
KEGG pathway was performed in the rosacea and acne datasets separately based on the expression of all genes 
in the two datasets, and the common GSEA pathways were identified. The GSEA of the KEGG pathway revealed 
that there were 37 activated and 2 suppressed pathways in the rosacea dataset, and there were 42 activated and 
17 suppressed pathways in the acne dataset (P-value < 0.05, q-value < 0.25). Only the activated and suppressed 
pathways with the highest normalized enrichment scores were shown in the Fig. 7A,B. There were 22 common 
GSEA pathways in the rosacea and acne datasets, all of which were activated pathways. Supplementary Figure 5 
showed that there was a clear separation of the gene set variation analysis (GSV A) scores for common GSEA 
pathways between the lesional and HC groups. Based on the expression of hub genes and the GSV A scores of 
common GSEA pathways in each sample, the relationship between hub genes and pathways were calculated. 
Figure 7C,D showed that all hub genes were significantly positively correlated with cytokine-cytokine receptor 
interaction, chemokine signaling pathway, Toll-like receptor signaling pathway, NOD-like receptor signaling 
pathway, JAK/STAT signaling pathway, etc. (P-value < 0.05).
Figure 1.  Identification of DEGs in rosacea and acne datasets. (A) Volcano plot of DEGs from all samples in 
the rosacea dataset, orange indicated higher gene expression, blue indicated lower gene expression, and black 
indicated genes with no significant difference in expression. (B) Heatmap of the DEGs in the rosacea dataset, 
the blue part on the left is the HC group, and the pink part on the right is the lesional group. Orange indicated 
higher gene expression and blue indicated lower gene expression. (C) Volcano plot of DEGs from all samples 
in the acne dataset. (D) Heatmap of DEGs in the acne dataset. DEGs differentially expressed genes, HC healthy 
control.

4
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
Immune cell infiltration analysis by CIBERSORT
To explore the infiltration of 22 immune cells in each sample and identify the immune cells associated with the 
pathogenesis of rosacea and acne, the immune cell infiltration analysis were performed on all samples of rosacea 
and acne datasets. Principal component analysis (PCA) cluster plot depicted that there were significant differ -
ences in immune cell infiltration between lesional and HC groups of rosacea and acne datasets (Fig. 8A,B). The 
heatmap showed that the distribution of 22 immune cells in all samples of rosacea and acne datasets (Supple-
mentary Fig. 4A,B). The barplot showed the relative percentage of 22 immune cells in all samples (Supplementary 
Fig. 4C,D). The average proportions of each type of immune cell and the difference between lesional and HC 
groups were calculated (Fig.  8C–H). Compared with HC, the proportions of infiltrated M1 macrophages, M0 
macrophages, gamma delta T cells, and activated memory CD4 + T cells increased most in rosacea lesions, while 
resting mast cells and resting dendritic cells decreased most. Meanwhile, compared with HC, the proportions of 
infiltrated neutrophils, M0 macrophages and activated mast cells increased most in acne lesions, while resting 
mast cells and resting dendritic cells decreased most.
The violin plot revealed that activated memory CD4 + T cells, M0 macrophages, M1 macrophages, and gamma 
delta T cells infiltrated significantly more in rosacea lesional group than HC group, while Tregs, activated NK 
cells, resting dendritic cells, and resting mast cells infiltrated significantly less (P-value  < 0.001) (Fig. 9A). Neu-
trophils, monocytes, and activated mast cells infiltrated significantly more in acne lesional group than HC group, 
while memory B cells, plasma cells, Tregs, and resting mast cells infiltrated significantly less (P-value < 0.001) 
(Fig. 9B).
The Corheatmap revealed that there was a positive strong correlation between resting NK cells and activated 
dendritic cells, activated mast cells and Tregs, monocytes and M1 macrophages, while there was a negative cor-
relation between gamma delta T cells and resting dendritic cells, activated memory CD4 + T cell and follicular 
Figure 2.  Weighted gene co-expression network analysis for GSE65914. (A) Heatmap of the association 
between rosacea and gene co-expression modules. Numbers at the top are the correlation coefficients, numbers 
at the bottom brackets are the corresponding P-values. (B) Venn diagram of the DEGs of rosacea and genes 
in the magenta module. (C) Venn diagram of the DEGs of rosacea with genes in the brown module. (D) Venn 
diagram of the up-regulated rosacea-co-DEGs and the up-regulated DEGs of acne. (E) Venn diagram of the 
down-regulated rosacea-co-DEGs and the down-regulated DEGs of acne. DEGs differentially expressed genes, 
HC healthy control, ETR erythematotelangiectatic rosacea, PPR papulopustular rosacea, PhR phymatous 
rosacea.

5
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
helper T cells in rosacea lesions (Supplementary Fig. 6A). And there was a positive strong correlation between 
activated NK cells and Tregs, activated memory CD4 + T cells and gamma delta T cells, neutrophils and acti-
vated mast cells, whereas there was a negative correlation between activated mast cells and resting mast cells, 
neutrophils and resting mast cells in acne lesions (Supplementary Fig. 6B).
Correlation of the hub genes and immune cells
Subsequently, the correlation of 10 hub genes with immune cells whose infiltration was significantly different 
between lesional and HC groups was explored. In rosacea lesions, the results showed that all hub genes were 
negatively correlated with resting mast cells, and 9 (except CXCR4) were negatively correlated with resting 
dendritic cells. All hub genes had a positive correlation with M1 macrophages, 9 (except CXCR4) and 8 (except 
CXCL8 and CXCR4) hub genes had a positive correlation with activated memory CD4 + T cells and gamma delta 
T cells, respectively (Fig. 10A). In acne lesions, all hub genes were negatively correlated with resting mast cells, 
whereas 9 (except CXCL10), 9 (except MMP9) and 8 (except MMP9 and CXCL10) hub genes were positively 
correlated with activated mast cells, gamma delta T cells, and neutrophils, respectively (Fig. 10B). And notably, 
MMP9 was significantly positively correlated with M0 macrophages in both rosacea and acne lesions (R > 0.75, 
P-value < 0.01). The correlation between all hub genes and these immune cells was shown in the lollipop chart 
(Supplementary Figs. 7, 8).
Figure 3.  Enrichment analysis of co-DEGs. (A,B) GO and KEGG pathway enrichment analysis of the 
up-regulated co-DEGs. (C) GO and KEGG pathway enrichment analysis of the down-regulated co-DEGs. DEGs 
differentially expressed genes, GO gene ontology, KEGG Kyoto Encyclopedia of Genes and Genomes.

6
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
Prediction and verification of TFs
To identify the TFs that may regulate the expression of the hub genes, we identified 23 TFs based on the TRRUST 
database (Supplementary Table 2). A total of 9 TFs were significantly differentially expressed in rosacea and acne 
datasets. Compared with HC, IRF1, STAT1, STAT3, IKBKB, HDAC1, ETS1, and CEBPB were highly expressed 
in rosacea and acne lesions (P-value < 0.05) (Fig.  11A–N). The expression of CXCL10, MMP9, IL1B, CXCL8, 
and CXCR4 were co-regulated by these TFs (Fig. 11O).
Discussion
Rosacea and acne are the most common inflammatory chronic skin diseases. Clinically, we frequently see acne 
patients with rosacea or patients who develop from acne to rosacea. Genetics, microbiomes, innate and adaptive 
immunological dysregulation, and skin barrier dysfunction have been implicated as shared pathogenetic factors 
in both rosacea and  acne5. When rosacea and acne coexist, rosacea is frequently missed or misdiagnosed due 
to the similarity of their clinical manifestations. However, few studies have investigated their relationship. The 
purpose of this study was to explore the relationship between rosacea and acne. In this study, hub genes were 
identified by screening DEGs and constructing weighted gene co-expression and PPI networks. And TFs that 
regulate the expression of these hub genes have been identified. Finally, we performed immune cell infiltration 
analysis to compare the immune cell infiltration characteristics of rosacea and acne lesions.
A total of 151 up-regulated and 18 down-regulated co-DEGs were identified. KEGG pathway analysis of up-
regulated co-DEGs demonstrated that the they were mainly involved in IL-17 signaling pathway, NF-κB signal-
ing pathway, Toll-like receptor signaling pathway, and TNF signaling pathway. This is consistent with previous 
findings that these pathways are involved in the development of both rosacea and  acne7,10–15. 10 co-DEGs, IL1B, 
PTPRC, CXCL8, MMP9, CCL4, CXCL10, CD163, CCR5, CXCR4, and TLR8, were identified as hub genes. The 
GO and the KEGG pathways analysis of hub genes revealed that they were mainly involved in immunological 
and inflammatory processes. And 14 pathways were significantly positively correlated with hub genes in both 
rosacea and acne datasets. The expression of CXCL10, MMP9, IL1B, CXCL8, and CXCR4 were co-regulated by 
IRF1, STAT1, STAT3, IKBKB, HDAC1, ETS1, and CEBPB, which were highly expressed in rosacea and acne 
Figure 4.  PPI network of co-DEGs, screening and constructing co-expression network of hub genes. (A) PPI 
network of co-DEGs. (B) The cluster with the highest score selected by the MCODE plug-in, hub genes were 
marked in red. (C) Hub genes were screened out using 8 algorithms. (D) Co-expression network of hub genes. 
PPI, protein–protein interaction.

7
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
lesions. Moreover, MMP9 was significantly positively correlated with M0 macrophages in both rosacea and 
acne lesions. The infiltration of gamma delta T cells was significantly increased and positively correlated with 
almost all hub genes in both rosacea and acne, suggesting that gamma delta T cells may play a crucial role in the 
pathogenesis of these two diseases.
Interleukin (IL)-1β is a potent proinflammatory cytokine which belongs to the IL-1 family. Previous studies 
have indicated that IL-1β plays a crucial role in the development of inflammation in rosacea and acne. Meng 
Figure 5.  Verification of hub genes in GSE6475. (A) Expression levels of 11 hub genes in the lesional and HC 
groups in GSE6475. (B) The diagnostic effectiveness of 11 hub genes. P-value < 0.05 was considered statistically 
significant. ***p < 0.001, **p < 0.01, *p < 0.05, ns p ≥ 0.05. HC healthy control.

8
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
et al. found that the expression of IL-1β in lesions of rosacea patients was significantly higher than age- and 
sex-matched healthy volunteers, especially PPR. In acne, all patients with inflammatory acne have dermal and 
epidermal IL-1β expression, and the expression level correlates with disease  severity16. Ultraviolet B and P . acnes 
are triggers for IL-1β secretion, and the inflammation induced by P . acnes causes the massive secretion of IL-1β 
from  monocytes17–19.
Matrix metalloproteases 9 (MMP9) is a member of the MMPs family that can degrade and remodel extracellu-
lar matrix  proteins20. MMPs mediate the rupture of the pilosebaceous follicle, whereby promotes the exacerbation 
of  inflammation21. The level of MMP9 expression is significantly increased in the lesions and serum of rosacea 
 patients22,23. In addition, the expression of MMP9 in the dermis of granulomatous rosacea lesions is significantly 
higher than that of non-granulomatous rosacea lesions, especially at the granuloma’s  center24. MMP9 induced by 
ultraviolet radiation has a role in the development of granuloma by promoting tissue remodeling and enhancing 
recruitment of inflammatory cells into the  granuloma24. MMP9 also participates in various cellular processes, 
including angiogenesis and  vasodilation20,25. Additionally, MMP9 contributes to the progression of acne. Kang 
et al. found that the expression level of MMP9 in acne lesions was significantly higher than in non-lesional  skin26. 
As one of the major pathogeneses of acne, P . acne was reported to induce the production of MMP9. Isotretinoin, 
quercetin, and daylight photodynamic therapy are all effective acne therapies that have been shown to decrease 
MMP9  expression27–29. MMP9 induces the production of pro-inflammatory cytokine, participates in angiogen-
esis, vasodilation, and tissue remodeling, which may make it the common hub gene in rosacea and acne.
CD163 is a macrophage-specific protein that is a member of group B of the scavenger receptor cysteine-
rich superfamily and plays a crucial role in the regulation of the immune  response30,31. The upregulation of 
CD163 is one of the major alterations in the macrophage transition to alternate activated phenotypes during 
 inflammation30. In rheumatoid arthritis, psoriasis, atopic dermatitis (AD), and rosacea, CD163 levels have been 
shown to be  elevated32–37. In a study including 50 rosacea patients, significant overexpression of CD163 was 
observed in the skin samples of PPR patients compared to the age- and sex-matched healthy  volunteers32. In 
addition,  CD163+ macrophages also play a crucial role in the progression of atherosclerosis (AS). Both rosacea 
and acne are closely related to AS. Several studies have shown a higher risk of AS in rosacea  patients38–40. Massive 
Figure 6.  Enrichment analysis of hub genes and correlation between hub genes. (A,B) GO and KEGG pathway 
enrichment analysis of hub genes. (C) Correlation between hub genes in lesional samples of rosacea. (D) 
Correlation between hub genes in lesional samples of acne. GO gene ontology, KEGG Kyoto Encyclopedia of 
Genes and Genomes.

9
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
Figure 7.  Correlation between hub genes and pathways. (A) The result of the GSEA of the KEGG pathway in 
rosacea dataset. (B) The result of the GSEA of the KEGG pathway in acne dataset. (C) Correlation heatmap 
between the expression of hub genes and the GSV A scores of the common pathways in rosacea dataset. (D) 
Correlation heatmap between the expression of hub genes and the GSV A scores of the common pathways in 
acne dataset. GSEA gene set enrichment analysis, KEGG Kyoto Encyclopedia of Genes and Genomes; GSVA 
gene set variation analysis.

10
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
uptake of oxidized lipid by macrophages and neutrophils (called foam cells) is believed to contribute to the 
common pathogenesis of acne and  AS41. In AS,  CD163+ macrophages are associated with plaque progression, 
microvascularity, and a high level of HIF1α (hypoxia-inducible factor 1α) and VEGF-A (vascular endothe-
lial growth factor-A)  expression42. Therefore,  CD163+ macrophages may contribute to the development of AS 
in rosacea and acne patients.
Toll-like receptor 8 (TLR8), a type I transmembrane protein localized on the surface of endosomes, is 
expressed in monocytes, macrophages, myeloid dendritic cells, and  neutrophils43. TLR8 induces NF-κB activa-
tion via the myeloid differentiation factor 88 (MyD88)-mediated signaling pathway and promotes the production 
of inflammatory  factors44, which is crucial for innate  immunity43. Previous studies demonstrated that TLR8 is 
involved in inflammatory dermatosis and autoimmune diseases, which is in the upstream of NF-κB-NLRP3 
and associated with the production of IL-1β, interferon (IFN)-α, and IL-645–48. However, the role of TLR8 in the 
pathogenesis of rosacea and acne requires further exploration.
CXCL8, CXCL10, CCL4, CCR5, and CXCR4 all belong to the chemokine superfamily and play important 
roles in inflammatory processes and immune  responses49. CXCL10 is a member of the  ELR-CXC subfamily 
Figure 8.  PCA cluster plot and the infiltration of immune cells among lesional and HC groups. (A) PCA 
cluster plot of immune cell infiltration in rosacea lesional and HC groups. (B) PCA cluster plot of immune cell 
infiltration in acne lesional and HC groups. (C,D) The proportions of 22 immune cells in rosacea lesional and 
HC groups separately. (E) The difference of the proportions of 22 immune cells between rosacea lesional and HC 
groups. (F,G) The proportions of 22 immune cells in acne lesional and HC groups separately. (H) The difference 
of the proportions of 22 immune cells between acne lesional and HC groups. PCA principal component analysis, 
HC healthy control.

11
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
chemokines, which play a crucial role in a variety of autoimmune  diseases50. CXCL10 binds to its ligand CXCR3 
to guide  CXCR3+ effector  CD4+ and  CD8+ T cells selectively migrated to autoimmune sites and tumor  sites51. 
CXCL10 and CXCR3 were found in keratinocytes and dermal infiltrates from active psoriasis plaques, and pso-
riasis patients had higher serum levels of  CXCL1052. Buhl et al. demonstrated that the expression of CXCL10 was 
increased in the lesional skin of rosacea  patients8. Similar results were observed in a cohort study, the CXCR3 
ligands CXCL9, CXCL10, and CXCL11 were overexpressed in acne  lesions7. All of these findings indicate that 
the expression levels of CXCL10 are elevated in rosacea and acne lesions, and its role in the pathogenesis of these 
two diseases requires further study. In addition, we also found that the expression level of CXCR4 is increased 
in these two diseases in our study. Helfrich et al. found an eightfold increase in CXCR4 expression in lesional 
skin from ETR patients compared to  HC53. Su et al. demonstrated that in the mouse model of allergic contact 
dermatitis, the CXCL12/CXCR4 signaling pathway induces itching and pain  feeling54. It requires further study 
Figure 9.  The difference of immune cells infiltration between lesional and HC groups. (A) The difference of 
immune cells infiltration between rosacea lesional (red) and HC groups (blue). (B) The difference of immune 
cells infiltration between acne lesional (red) and HC groups (blue). HC healthy control.

12
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
to determine whether the CXCL12/CXCR4 signaling pathway has a role in some rosacea and acne patients with 
itching and pain.
By the prediction and verification analysis of TFs, we found that IRF1, STAT1, STAT3, IKBKB, HDAC1, 
ETS1, and CEBPB regulate the expression of hub genes in a synergistic manner. Several previous studies have 
demonstrated that these TFs play a crucial role in the pathogenesis of rosacea and acne. Signal Transducers and 
Activators of Transcription 1 (STAT1) is a member of the STAT family, it is activated by Janus kinases (JAK)55. 
STAT1 is critical in inflammatory diseases, such as systemic lupus erythematosus, inflammatory bowel disease, 
Figure 10.  The correlation between hub genes and immune cells. (A) The heatmap of the correlation between 
hub genes and immune cells in rosacea lesions. (B) The heatmap of the correlation between hub genes and 
immune cells in acne lesions.

13
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
and  psoriasis56–58. Activation of STAT1 leads to the upregulation of several pro-inflammatory chemokines in 
the epidermis, such as CXCL9, CXCL10, and  CCL259. Saez-de-Ocariz et al. found that rosacea is a striking 
Figure 11.  Prediction and verification of TFs, and transcriptional regulatory network. (A–G) The expression 
levels of IRF1, STAT1, STAT3, IKBKB, HDAC1, ETS1, and CEBPB in rosacea dataset. P-value < 0.05 was 
considered statistically significant. (H–N) The expression levels of IRF1, STAT1, STAT3, IKBKB, HDAC1, ETS1, 
and CEBPB in acne dataset. P-value < 0.05 was considered statistically significant. (O) Transcriptional regulatory 
network. Hub genes were marked in red, TFs were marked in yellow. TFs, transcription factors.

14
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
feature in family members with a STAT1 gain-of-function mutation, indicating that STAT1 may contribute to the 
development of chronic  inflammation60. Deng et al. performed RNA-seq on lesional skin from rosacea patients 
and found that the epidermal STAT1/IRF1 signature were observed in all rosacea  subtypes61. STAT1-regulated 
gene transcription mediates many of the immune and inflammatory actions of IFN-γ 62. Previous studies have 
implicated that IFN-γ is implicated in the pathogenesis of rosacea and acne. P . acnes can induce IFN-γ secretion 
by Th17 cells and  CD4+ T  cells63,64. In an in vitro experiment, acne-associated P . acnes phylotypes induced 2–3 
times higher levels of IFN-γ in PBMCs than healthy  phylotypes65. In addition, the expression level of IFN-γ was 
significantly increased in rosacea lesions, which was validated by immunocytochemistry to have a largely higher 
staining for IFN-γ in  lesions8. Whether STAT1 has a role in the pathogenesis of rosacea and acne by regulating 
gene transcription to mediate the immune and inflammatory actions of IFN-γ remains to be confirmed in the 
future.
Signal Transducers and Activators of Transcription 3 (STAT3) is a component of the IL-6 activated acute 
phase response factor complex and is also a member of the STAT  family66. It has been demonstrated that the IL-6/
STAT3 signaling pathway plays a role in  inflammation67–69. Wang et al. found that STAT3 and related pathways 
are up-regulated in rosacea, and they speculated that STAT3 expression is up-regulated in keratinocyte after 
skin barrier dysfunction, leading to the secretion of inflammatory factors and immune  infiltration70. In a model 
in which HaCaT cells treated with the antibacterial peptide LL-37 to simulate rosacea caused by Demodex fol-
liculorum (D. folliculorum) infection, JAK 2 and STAT3 expression levels were increased, indicating that rosacea 
caused by D. folliculorum infection may be associated with the activation of the JAK/STAT signaling  pathway71. 
These evidences indicate that STAT3 may be an important gene in the pathogenesis of rosacea and acne, and it 
remains to be confirmed whether medications that target STAT3 may effectively treat rosacea and acne.
NF-κB is normally sequestered in the cytoplasm, bound to inhibitory κB (IκB) proteins as an inactive 
 complex72. In response to lipopolysaccharide (LPS), an endotoxin recognized by the TLR4 receptor on immune 
cells, cellular IκB kinase (IKK) complex is activated and the cytoplasmic IκB protein is  phosphorylates73. The 
phosphorylated forms of IκB are subjected to ubiquitination and then degraded in the proteasome, which frees 
NF-κB to translocate to the nucleus where it regulates gene  transcription74. Then NF-κB moves into the nucleus 
and binds to the κB motif of inflammation and immune genes, such as IL-1β75. As a component of the IKK com-
plex, IKKβ is intimately associated with the expression of NF-κB. And in our study, we found that the expression 
levels of IKKβ is increased in both rosacea and acne lesions, and that it may regulate the expression of hub genes. 
It has been demonstrated that the NF-κB signaling pathway plays a crucial role in the pathogenesis of rosacea 
and  acne26,76–79. Most inflammatory stimuli, including LPS, require the IKKβ subunit for NF-κB  activation80. 
Benzothiazolone derivatives have been used in the treatment of  acne81. Kim et al. found that LYR-71, a benzo-
thiazolone derivative, is a potent IKKβ inhibitor that prevents NF-κB activation in macrophages and may help 
in inhibiting the expression of inflammatory  cytokines75. These findings suggest that IKKβ may play a role in 
the pathogenesis of rosacea and acne by influencing the NF-κB signaling pathway and regulating the secretion 
of pro-inflammatory cytokines.
In addition, we also performed immune infiltration analysis for the rosacea and acne datasets, respectively. 
Notably, MMP9 was significantly positively correlated with M0 macrophages in both rosacea and acne lesions 
in our study. And the infiltration of gamma delta T cells in rosacea and acne lesions was higher than in HC and 
positively correlated with the most of hub genes. However, few previous studies have reported the role of gamma 
delta T cells in this process.
Gamma delta T cells (also called γδT cells) are an unconventional population of T lymphocytes. They are 
significantly enriched in mucosal and epithelial sites, such as the skin and respiratory, digestive, and reproductive 
 tracts82. γδT cells has a variety of functions, including cytokine and chemokine production, antigen-presenting 
functions, and regulation  abilities83, and therefore play a crucial role in autoimmune, infection, allergy, cancer, 
among  others84–87. They produce a variety of cytokines, such as IL-17 and IFN-γ 82. IL-17-producing γδT cells 
induces the recruitment of neutrophils and monocytes and increases the inflammation  response82. In a variety of 
immune skin diseases, including AD, alopecia areata, and psoriasis, the number of intracutaneous γδT cells has 
been demonstrated to be  increased88–90. Cai et al. found that epidermal hyperplasia and inflammatory response 
induced by IL-23 and IMQ were significantly decreased in T cell receptor δ deficient  mice91. These evidences 
suggest that γδT cells are crucial in inflammatory diseases and may be therapeutic targets in the future. As for 
the role of γδT cells in the progression of rosacea and acne, additional research is required.
In addition, we also found that there was a significant positive correlation between MMP9 and M0 mac-
rophages in rosacea and acne lesions. It has been demonstrated that MMP9 expression and M0 macrophage 
infiltration were significantly increased in both rosacea and acne  lesions22,23,26,92, which is consistent with our 
results. MMP9 can degrade extracellular matrix and plays a crucial role in the development and spread of inflam-
matory  response21. M0 macrophages (resting macrophages) can be polarized into M1 macrophages (classically 
activated macrophages) under the stimulation of IFN-γ and LPS and into M2 macrophages (alternatively acti -
vated macrophages) under the stimulation of IL-4 and IL-13. M1 macrophages then secrete a large number of 
pro-inflammatory factors, which mainly promote the development of inflammation. Anti-inflammatory factors 
are secreted by M1 macrophages, which serve an anti-inflammatory  function93. Inflammation in rosacea and 
acne can be aggravated by polarizing macrophages towards the M1  phenotype94–97, indicating that macrophages 
play a crucial role in the pathogenesis of these two diseases. Previous studies have shown a significant positive 
correlation between MMP9 expression and M0 macrophages infiltration in inflammation-related diseases, such 
as coronary artery disease (CAD), AS, adhesive capsulitis, and  cancers98–101. However, the causal relationship 
between them has not yet been clarified. Linton et al. found that M0 macrophages secrete MMP9 in the early 
phases of pancreatic cancer to promote tumor  progression102. Therefore, we hypothesized that M0 macrophages 
may secrete MMP9 and act in concert with it to promote the development of inflammatory responses in rosacea 
and acne.

15
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
Despite the fact that rosacea and acne frequently occur together clinically and have cross pathogenesis, it is 
important to note that rosacea and acne are two separate diseases with distinct pathogenesis, and their clinical 
manifestations are not identical. The main difference between the clinical manifestations of rosacea and acne is 
that rosacea patients have persistent facial erythema, flushing, a burning sensation, telangiectasia, and in some 
cases hyperplasia of the facial  tissue1. Rosacea is primarily caused by the dysregulation and upregulation of 
the innate immune system, leading to in excessive inflammation and vasodilation. In addition, hyperreactive 
neurovascular and exogenous factors play a significant role in the pathogenesis of  rosacea13. Transient receptor 
potential (TRP) cation channels are widely expressed on keratinocytes and endothelial cells. Activation of the 
TRP family of channels leads to the release of mediators of neurogenic inflammation and pain, such as substance 
P and calcitonin gene-related peptide. Persistent facial flushing in rosacea patients is mainly induced by these 
vasoregulatory  neuropeptides10. The decreased thermal pain threshold and increased burning sensation in the 
skin of rosacea patients may be related to the increased activity of the TRPs. In addition, connective tissue 
hyperplasia in some rosacea patients is related to the persistence of inflammation, the activation of mast cells 
and the release of MMP1, MMP9, IL-6, and histamine, and the increased activity of the  TRPs14. However, acne 
is mainly caused by follicular hyperkeratinization, excess sebum, inflammation, and P . acnes , which does not 
typically involve neurovascular  dysergulation77. Consequently, persistent erythema, flushing, burning sensation, 
and telangiectasia are not typically observed in acne patients. Therefore, despite the fact that rosacea and acne 
share some clinical manifestations and pathogenesis, great care must be taken not to confuse these two diseases 
in order to avoid missed and misdiagnosis.
However, our study also has some limitations. Firstly, there is limited availability of datasets in the GEO data-
base related to rosacea and acne. Despite pooling two acne datasets, the sample size remains small, potentially 
leading to instability in statistical analyses. Secondly, we were unable to identify additional rosacea datasets to 
verify the hub genes that have already been confirmed. Thirdly, inherent variability in biological systems may 
impact the analysis outcomes. Fourthly, the results of the analysis are also influenced by the quality of the raw 
data. Low-quality sequencing, chip data, or other experimental data may result in inaccurate analytical outcomes. 
Fifthly, our research conclusions need further validation in in vitro models, which will be a focus of our future 
studies. In addition, we believe that our study may provide ideas and directions for future research.
In summary, we identified 169 common DEGs after analyzing the datasets of rosacea and acne. Then we 
identified 10 hub genes that may play important roles in the pathogenesis of these two diseases by verifying in 
another dataset, and we also identified TFs that may regulate the expression of these hub genes. Then we found 
the pathogenesis of rosacea and acne had some similarity in terms of immune responses through immune cell 
infiltration analysis. This is the first study to explore the common hub genes and critical immune cells of rosacea 
and acne, which helped to further clarify the common molecular pathogenesis of these two diseases.
Methods
Datasets source and processing
The workflow is depicted in Fig. 12. Searched for “rosacea” and “acne” in the GEO database (https:// www. ncbi. 
nlm. nih. gov/ geo/) and chose datasets with the following characteristics: (a) The study includes lesional skin 
samples as well as non-lesional skin samples or HC skin samples. (b) The experiment type is expression profil -
ing by array. Consequently, we identified one rosacea dataset (GSE65914) and three acne datasets (GSE108110, 
GSE53795, and GSE6475) meeting these criteria. To maximize sample size, we pooled GSE108110 and GSE53795, 
and GSE6475 was used as the verification dataset. The description of these datasets was shown in Table  1. To 
ensure the consistency of acne lesional samples, papule samples from GSE108110 at 21 days were excluded. We 
processed downloaded datasets and annotated probes with platform annotation files using R software (version: 
4.2.1). Logarithmic conversion was uniformly applied to all microarrays. Each dataset’s gene expression matrix 
file was deduplicated and averaged according to gene name. The gene expression matrix file of GSE108110 and 
GSE53795 were then pooled using the “inSilicoMerging” R package. Additionally, the combat function from the 
“sva” R package was used to eliminate the batch effect.
Identification of DEGs
The “Limma” R package was used to identify DEGs between lesional and HC groups of the rosacea and acne 
datasets. The “Limma” R package is frequently employed for the identification of DEGs in both microarray and 
RNA-seq data. The statistical analysis is conducted using linear models and Bayesian methods. Flod change value 
and P-value were calculated for each gene in each sample. Adjusted P-value < 0.05 and |log2FC|> 1 were used as 
the cut-offs to identify DEGs. Independently, up- and down-regulated genes were obtained. The “ggplot2” and 
“pheatmap” R packages were used to generate the volcano plot and heatmap, respectively.
WGCNA for GSE65914
The “WGCNA ” R package was used to construct the gene co-expression network of GSE65914. Firstly, the 
similarity matrix was defined and the outlier samples were eliminated. CutHeight was set to 80. Soft threshold-
ing power (β) was selected, and the similarity matrix was converted into an adjacency matrix representing the 
connection strength relationship between genes. Then the adjacency was converted into a topological overlap 
matrix and the distance between genes was calculated for hierarchical clustering based on the topological overlap 
dissimilarity measure. Dynamic tree-cutting algorithm was used to construct cluster dendrogram and divide 
modules. MinModuleSizes was set to 30, deepSplit was set to 2, and mergeCutHeight was set to 0. 25. The cor -
relation between modules and rosacea was calculated using Pearson’s correlation analysis, and the significant 
module were identified. Then, using the “ggplot2” R package for visualization, we took the intersection of the 
DEGs of rosacea dataset and genes in the two most significant modules, regarding these genes as common DEGs 

16
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
in rosacea dataset, i.e., “rosacea-co-DEGs” . Finally, we took the intersection of rosacea-co-DEGs and the DEGs 
of acne dataset, regarding them as common DEGs, i.e., “co-DEGs” .
GO and KEGG pathway enrichment analysis
GO and KEGG pathway enrichment analysis were performed for DEGs of acne dataset, rosacea-co-DEGs, and 
co-DEGs  separately103–105. The “ClusterProfiler” R package was used for GO and KEGG pathway enrichment 
analysis, the entire human genome was used as universe. And the “org.Hs.eg.db” and “ggplot2” R packages were 
used for ID conversion and visualization, respectively.
Construction of PPI network and identification of hub genes
Using STRING online tools (https:// cn. string- db. org) and Cytoscape software (version: 3.9.1), a PPI network 
was constructed and visualized. MCODE plug-in was used to select the cluster with highest score. Hub genes 
were identified from the genes at the junction of eight commonly used algorithms in cytoHubba plug-in of 
Cytoscape (Maximal Clique Centrality (MCC), Maximum Neighborhood Component (MNC), Edge Percolated 
Component (EPC), Betweenness, Closeness, Radiality, Stress, and Degree), and the “UpSet” R package was used 
for visualization.
Verification of hub genes in GSE6475 and correlation of hub genes
In GSE6475, which comprises 6 lesional samples and 12 non-lesional samples of acne, the mRNA expression of 
11 hub genes was validated. First, the gene expression levels of the microarray were logarithmic transformed. 
The T-test was used to compare two groups, and a P-value < 0.05 was considered statistically significant. Using 
the “pROC” and “ggplot2” R packages, ROC analysis and visualization were performed to predict the diagnostic 
Figure 12.  Flow chart summarizing the procedures used in this study.
Table 1.  Description of the selected datasets.
GSE number Platform Experiment type Source type
Samples
Country Attribute AuthorPatients Controls Tota l
GSE65914 GPL570 Array Human Skin 38 20 58 France Test Buhl et al. 
(2015)
GSE108110 GPL570 Array Human Skin 18 18 36 France Test Carlavan et al. 
(2018)
GSE53795 GPL570 Array Human Skin 12 12 24 France Test Kelhälä et al. 
(2014)
GSE6475 GPL571 Array Human Skin 6 12 18 USA Verification Trivedi et al. 
(2006)

17
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
efficiency of hub genes. Correlation between all hub genes was calculated using Pearson’s correlation analysis, 
and the “corrplot” R package was used for visualization. Using Genemania online tools (http:// www. genem ania. 
org/), the co-expression network of hub genes was constructed subsequently. Then, GO and KEGG pathway 
enrichment analyses were performed on hub genes.
Correlation between hub genes and pathways
The “clusterProfiler” R package was used for GSEA analysis, and the “ggplot2” R package was used for visualiza-
tion. Then, we performed GSV A of the common GSEA pathways in the rosacea and acne datasets separately by 
using the “GSV A ” R package, adjusted P-value < 0.05 and q-value < 0.25 were considered significant. The “pheat-
map” R package was used to construct heatmap based on the GSV A score of the common GSEA pathways in each 
sample. And based on the expression of the hub genes and the GSV A scores of the common GSEA pathways in 
each sample, the correlation between hub genes and pathways was calculated using Pearson’s correlation analysis, 
and the “corrplot” R package was used for visualization. P-value < 0.05 was considered significant.
Immune cell infiltration analysis by CIBERSORT
CIBERSORT is a computational tool for analyzing the proportion of diverse immune cells in tissues according 
to the known reference set LM22 (leukocyte signature matrix) based on microarray and RNA-seq data. The 
“CIBERSORT” R package was used to explore the infiltration of 22 immune cells in every sample. The “ggplot2” 
R package was used to perform PCA and visualize the results of it. Then, we visualized the distribution of 22 
immune cells in all samples using the “pheatmap” R package. After that, using the “ggplot2” R package, the relative 
percentage of 22 immune cells in all samples was reflected via a barplot when the total infiltration of immune 
cells was regarded as 100%. Then, the average proportion of each type of immune cell in the lesional and HC 
groups was calculated, as well as the difference between the two groups. The “ggplot2” R package was used to 
visualize the results. Using the “vioplot” R package, the difference in infiltration of 22 immune cells between 
the lesional and HC groups was visualized as a violin plot. Finally, the relationship between all immune cells in 
lesional samples was analyzed and visualized using “corrplot” R package.
Correlation of the hub genes and immune cells
Then, the Pearson’s correlation analysis was used to calculate the correlation between all hub genes and immune 
cells that infiltrated significantly differently between lesional and HC groups, and the “ggplot2” R package was 
used to visualize the results. In order to show the correlation between all hub genes and immune cells more 
intuitively, the “ggpubr” R package was used to obtain the lollipop chart.
Prediction and verification of transcription factors
The TFs of hub genes with an adjusted P-value < 0.05 were obtained from TRRUST database (https:// www. grnpe 
dia. org/ trrust). The expression levels of these TFs were then compared between the lesional and HC groups using 
the T-test and visualized using the “limma” and “ggpubr” R packages. P-value < 0.05 was considered significant. 
Cytoscape (version: 3.9.1) was used for constructing transcriptional regulatory network.
Data availability
The datasets used and/or analyzed during the current study are available from the corresponding author on 
reasonable request.
Received: 4 July 2023; Accepted: 31 January 2024
References
 1. Schaller, M. et al. Recommendations for rosacea diagnosis, classification and management: Update from the global ROSacea 
COnsensus 2019 panel. Br. J. Dermatol. 182, 1269–1276. https:// doi. org/ 10. 1111/ bjd. 18420 (2020).
 2. Wollina, U. Is rosacea a systemic disease?. Clin. Dermatol. 37, 629–635. https:// doi. org/ 10. 1016/j. clind ermat ol. 2019. 07. 032 
(2019).
 3. Williams, H. C., Dellavalle, R. P . & Garner, S. Acne vulgaris. Lancet  379, 361–372. https:// doi. org/ 10. 1016/ S0140- 6736(11) 
60321-8 (2012).
 4. Ozcan, Y ., Sungur, M. A., Ozcan, B. Y ., Eyup, Y . & Ozlu, E. The psychosocial impact of chronic facial dermatoses in adults. 
Dermatol. Pract. Concept 13, e2023029. https:// doi. org/ 10. 5826/ dpc. 1301a 29 (2023).
 5. Chen, H., Lai, W . & Zheng, Y . Rosacea in acne vulgaris patients: Subtype distribution and triggers assessment: A cross-sectional 
study. J. Cosmet Dermatol. 20, 1889–1896. https:// doi. org/ 10. 1111/ jocd. 13762 (2021).
 6. Carlavan, I. et al. Atrophic scar formation in patients with acne involves long-acting immune responses with plasma cells and 
alteration of sebaceous glands. Br. J. Dermatol. 179, 906–917. https:// doi. org/ 10. 1111/ bjd. 16680 (2018).
 7. Kelhala, H. L. et al. IL-17/Th17 pathway is activated in acne lesions. PLoS ONE 9, e105238. https:// doi. org/ 10. 1371/ journ al. pone. 
01052 38 (2014).
 8. Buhl, T. et al. Molecular and morphological characterization of inflammatory infiltrate in rosacea reveals activation of Th1/Th17 
pathways. J. Invest. Dermatol. 135, 2198–2208. https:// doi. org/ 10. 1038/ jid. 2015. 141 (2015).
 9. Trivedi, N. R., Gilliland, K. L., Zhao, W ., Liu, W . & Thiboutot, D. M. Gene array expression profiling in acne lesions reveals 
marked upregulation of genes involved in inflammation and matrix remodeling. J. Invest. Dermatol. 126, 1071–1079. https:// 
doi. org/ 10. 1038/ sj. jid. 57002 13 (2006).
 10. Ahn, C. S. & Huang, W . W . Rosacea pathogenesis. Dermatol. Clin. 36, 81–86. https:// doi. org/ 10. 1016/j. det. 2017. 11. 001 (2018).
 11. Beylot, C. et al.  Propionibacterium acnes: An update on its role in the pathogenesis of acne. J. Eur. Acad. Dermatol. Venereol.  
28, 271–278. https:// doi. org/ 10. 1111/ jdv. 12224 (2014).
 12. Hazarika, N. Acne vulgaris: New evidence in pathogenesis and future modalities of treatment. J. Dermatol. Treat. 32, 277–285. 
https:// doi. org/ 10. 1080/ 09546 634. 2019. 16540 75 (2021).

18
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
 13. Marson, J. W . & Baldwin, H. E. Rosacea: A wholistic review and update from pathogenesis to diagnosis and therapy. Int. J. 
Dermatol. 59, e175–e182. https:// doi. org/ 10. 1111/ ijd. 14757 (2020).
 14. Rodrigues-Braz, D. et al. Cutaneous and ocular rosacea: Common and specific physiopathogenic mechanisms and study models. 
Mol. Vis. 27, 323–353 (2021).
 15. Two, A. M., Wu, W ., Gallo, R. L. & Hata, T. R. Rosacea: Part I. Introduction, categorization, histology, pathogenesis, and risk 
factors. J. Am. Acad. Dermatol. 72, 749–758. https:// doi. org/ 10. 1016/j. jaad. 2014. 08. 028 (2015).
 16. Thanh, L. T. V . et al. Immunohistochemical expression of interleukin 1 beta in papule biopsies from patients with acne vulgaris. 
Dermatol. Rep. 14, 9444. https:// doi. org/ 10. 4081/ dr. 2022. 9444 (2022).
 17. Kistowska, M. et al. IL-1beta drives inflammatory responses to propionibacterium acnes in vitro and in vivo. J. Invest. Dermatol. 
134, 677–685. https:// doi. org/ 10. 1038/ jid. 2013. 438 (2014).
 18. Qin, M. et al. Propionibacterium acnes Induces IL-1beta secretion via the NLRP3 inflammasome in human monocytes. J. Invest. 
Dermatol. 134, 381–388. https:// doi. org/ 10. 1038/ jid. 2013. 309 (2014).
 19. Suhng, E. et al. Increased expression of IL-33 in rosacea skin and UVB-irradiated and LL-37-treated HaCaT cells. Exp. Dermatol. 
27, 1023–1029. https:// doi. org/ 10. 1111/ exd. 13702 (2018).
 20. Cabral-Pacheco, G. A. et al. The roles of matrix metalloproteinases and their inhibitors in human diseases. Int. J. Mol. Sci.  21, 
9739. https:// doi. org/ 10. 3390/ ijms2 12497 39 (2020).
 21. Jugeau, S. et al. Induction of toll-like receptors by Propionibacterium acnes. Br. J. Dermatol. 153, 1105–1113. https:// doi. org/ 
10. 1111/j. 1365- 2133. 2005. 06933.x (2005).
 22. Falay Gur, T. et al. The investigation of the relationships of demodex density with inflammatory response and oxidative stress 
in rosacea. Arch. Dermatol. Res. 310, 759–767. https:// doi. org/ 10. 1007/ s00403- 018- 1857-1 (2018).
 23. Muto, Y . et al. Mast cells are key mediators of cathelicidin-initiated skin inflammation in rosacea. J. Invest. Dermatol. 134, 
2728–2736. https:// doi. org/ 10. 1038/ jid. 2014. 222 (2014).
 24. Jang, Y . H., Sim, J. H., Kang, H. Y ., Kim, Y . C. & Lee, E. S. Immunohistochemical expression of matrix metalloproteinases in the 
granulomatous rosacea compared with the non-granulomatous rosacea. J. Eur. Acad. Dermatol. Venereol. 25, 544–548. https:// 
doi. org/ 10. 1111/j. 1468- 3083. 2010. 03825.x (2011).
 25. Chen, J. et al. Neutrophils enhance cutaneous vascular dilation and permeability to aggravate psoriasis by releasing matrix 
metallopeptidase 9. J. Invest. Dermatol. 141, 787–799. https:// doi. org/ 10. 1016/j. jid. 2020. 07. 028 (2021).
 26. Kang, S. et al. Inflammation and extracellular matrix degradation mediated by activated transcription factors nuclear factor-
kappaB and activator protein-1 in inflammatory acne lesions in vivo. Am. J. Pathol. 166, 1691–1699. https:// doi. org/ 10. 1016/ 
s0002- 9440(10) 62479-0 (2005).
 27. Kwon, H. H. et al. Daylight photodynamic therapy with 1.5% 3-butenyl 5-aminolevulinate gel as a convenient, effective and 
safe therapy in acne treatment: A double-blind randomized controlled trial. J. Dermatol. 43, 515–521. https:// doi. org/ 10. 1111/ 
1346- 8138. 13191 (2016).
 28. Lim, H. J., Kang, S. H., Song, Y . J., Jeon, Y . D. & Jin, J. S. Inhibitory effect of quercetin on propionibacterium acnes-induced skin 
inflammation. Int. Immunopharmacol. 96, 107557. https:// doi. org/ 10. 1016/j. intimp. 2021. 107557 (2021).
 29. Papakonstantinou, E. et al. Matrix metalloproteinases of epithelial origin in facial sebum of patients with acne and their regula-
tion by isotretinoin. J. Invest. Dermatol. 125, 673–684. https:// doi. org/ 10. 1111/j. 0022- 202X. 2005. 23848.x (2005).
 30. Etzerodt, A. & Moestrup, S. K. CD163 and inflammation: Biological, diagnostic, and therapeutic aspects. Antioxid. Redox Signal. 
18, 2352–2363. https:// doi. org/ 10. 1089/ ars. 2012. 4834 (2013).
 31. Kowal, K. et al. CD163 and its role in inflammation. Folia Histochem Cytobiol  49, 365–374. https:// doi. org/ 10. 5603/ fhc. 2011. 
0052 (2011).
 32. Casas, C. et al. Quantification of Demodex folliculorum by PCR in rosacea and its relationship to skin innate immune activation. 
Exp. Dermatol. 21, 906–910. https:// doi. org/ 10. 1111/ exd. 12030 (2012).
 33. Karakike, E. & Giamarellos-Bourboulis, E. J. Macrophage activation-like syndrome: A distinct entity leading to early death in 
sepsis. Front. Immunol. 10, 55. https:// doi. org/ 10. 3389/ fimmu. 2019. 00055 (2019).
 34. Matsushita, N. et al. Elevated levels of soluble CD163 in sera and fluids from rheumatoid arthritis patients and inhibition of the 
shedding of CD163 by TIMP-3. Clin. Exp. Immunol. 130, 156–161. https:// doi. org/ 10. 1046/j. 1365- 2249. 2002. 01963.x (2002).
 35. Matsushita, T. & Takehara, K. Soluble CD163 is a potential biomarker in systemic sclerosis. Expert Rev. Mol. Diagn. 19, 197–199. 
https:// doi. org/ 10. 1080/ 14737 159. 2019. 15719 11 (2019).
 36. Sugaya, M. et al. Association of the numbers of CD163(+) cells in lesional skin and serum levels of soluble CD163 with disease 
progression of cutaneous T cell lymphoma. J. Dermatol. Sci. 68, 45–51. https:// doi. org/ 10. 1016/j. jderm sci. 2012. 07. 007 (2012).
 37. Weiss, M. & Schneider, E. M. Soluble CD163: An age-dependent, anti-inflammatory biomarker predicting outcome in sepsis. 
Crit. Care Med. 34, 2682–2683. https:// doi. org/ 10. 1097/ 01. CCM. 00002 40242. 10583. 86 (2006).
 38. Gurel, G. & Turan, Y . Noninvasive assessment of subclinical atherosclerosis in patients with rosacea. Ital. J. Dermatol. Venerol. 
156, 51–56. https:// doi. org/ 10. 23736/ S2784- 8671. 19. 06218-7 (2021).
 39. Hua, T. C. et al. Cardiovascular comorbidities in patients with rosacea: A nationwide case-control study from Taiwan. J. Am. 
Acad. Dermatol. 73, 249–254. https:// doi. org/ 10. 1016/j. jaad. 2015. 04. 028 (2015).
 40. Caf, N. et al. Evaluation of subclinical atherosclerosis in rosacea patients by flow-mediated dilatation method. J. Cosmet. Der -
matol. 22, 1001–1010. https:// doi. org/ 10. 1111/ jocd. 15492 (2023).
 41. Jiang, H. & Li, C. Common pathogenesis of acne vulgaris and atherosclerosis. Inflammation  42, 1–5. https:// doi. org/ 10. 1007/ 
s10753- 018- 0863-y (2019).
 42. Guo, L. et al. CD163+ macrophages promote angiogenesis and vascular permeability accompanied by inflammation in athero-
sclerosis. J. Clin. Invest. 128, 1106–1124. https:// doi. org/ 10. 1172/ JCI93 025 (2018).
 43. Dowling, D. J. Recent advances in the discovery and delivery of TLR7/8 agonists as vaccine adjuvants. Immunohorizons  2, 
185–197. https:// doi. org/ 10. 4049/ immun ohori zons. 17000 63 (2018).
 44. Wang, Y . et al. Suppressive effect of beta, beta-dimethylacryloyl alkannin on activated dendritic cells in psoriasis by the TLR7/8 
pathway. Int. Immunopharmacol. 40, 410–418. https:// doi. org/ 10. 1016/j. intimp. 2016. 09. 029 (2016).
 45. Demaria, O. et al. TLR8 deficiency leads to autoimmunity in mice. J. Clin. Invest. 120, 3651–3662. https:// doi. org/ 10. 1172/ JCI42 
081 (2010).
 46. Desnues, B. et al. TLR8 on dendritic cells and TLR9 on B cells restrain TLR7-mediated spontaneous autoimmunity in C57BL/6 
mice. Proc. Natl. Acad. Sci. U S A 111, 1497–1502. https:// doi. org/ 10. 1073/ pnas. 13141 21111 (2014).
 47. Fejtkova, M. et al. TLR8/TLR7 dysregulation due to a novel TLR8 mutation causes severe autoimmune hemolytic anemia and 
autoinflammation in identical twins. Am. J. Hematol. 97, 338–351. https:// doi. org/ 10. 1002/ ajh. 26452 (2022).
 48. Guo, Y . et al. Increased activation of toll-like receptors-7 and -8 of peripheral blood mononuclear cells and upregulated serum 
cytokines in patients with pediatric systemic lupus erythematosus. Int. J. Clin. Exp. Med. 8, 20472–20480 (2015).
 49. Zlotnik, A. & Y oshie, O. The chemokine superfamily revisited. Immunity 36, 705–716. https:// doi. org/ 10. 1016/j. immuni. 2012. 
05. 008 (2012).
 50. Antonelli, A. et al. Chemokine (C-X-C motif) ligand (CXCL)10 in autoimmune diseases. Autoimmun. Rev. 13, 272–280. https:// 
doi. org/ 10. 1016/j. autrev. 2013. 10. 010 (2014).
 51. Karin, N. & Razon, H. Chemokines beyond chemo-attraction: CXCL10 and its significant role in cancer and autoimmunity. 
Cytokine 109, 24–28. https:// doi. org/ 10. 1016/j. cyto. 2018. 02. 012 (2018).

19
Vol.:(0123456789)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
 52. Ferrari, S. M. et al. CXCL10 in psoriasis. Adv. Med. Sci. 60, 349–354. https:// doi. org/ 10. 1016/j. advms. 2015. 07. 011 (2015).
 53. Helfrich, Y . R. et al. Clinical, histologic, and molecular analysis of differences between erythematotelangiectatic rosacea and 
telangiectatic photoaging. JAMA Dermatol. 151, 825–836. https:// doi. org/ 10. 1001/ jamad ermat ol. 2014. 4728 (2015).
 54. Su, W ., Yu, J., Liu, Q., Ma, L. & Huang, Y . CXCL12/CXCR4 signaling induced itch and pain sensation in a murine model of 
allergic contact dermatitis. Mol. Pain 16, 1744806920926426. https:// doi. org/ 10. 1177/ 17448 06920 926426 (2020).
 55. Osterlund, P . I., Pietila, T. E., Veckman, V ., Kotenko, S. V . & Julkunen, I. IFN regulatory factor family members differentially 
regulate the expression of type III IFN (IFN-lambda) genes. J. Immunol. 179, 3434–3442. https:// doi. org/ 10. 4049/ jimmu nol. 
179.6. 3434 (2007).
 56. Alunno, A., Padjen, I., Fanouriakis, A. & Boumpas, D. T. Pathogenic and therapeutic relevance of JAK/STAT signaling in systemic 
lupus erythematosus: Integration of distinct inflammatory pathways and the prospect of their inhibition with an oral agent. Cells 
8, 898. https:// doi. org/ 10. 3390/ cells 80808 98 (2019).
 57. Bai, L. et al. STAT1 activation represses IL-22 gene expression and psoriasis pathogenesis. Biochem. Biophys. Res. Commun. 501, 
563–569. https:// doi. org/ 10. 1016/j. bbrc. 2018. 05. 042 (2018).
 58. Yu, Y . L. et al. STAT1 epigenetically regulates LCP2 and TNFAIP2 by recruiting EP300 to contribute to the pathogenesis of 
inflammatory bowel disease. Clin. Epigenet. 13, 127. https:// doi. org/ 10. 1186/ s13148- 021- 01101-w (2021).
 59. Blazanin, N., Cheng, T., Carbajal, S. & DiGiovanni, J. Activation of a protumorigenic IFNgamma/STAT1/IRF-1 signaling pathway 
in keratinocytes following exposure to solar ultraviolet light. Mol. Carcinog.  58, 1656–1669. https:// doi. org/ 10. 1002/ mc. 23073 
(2019).
 60. Saez-de-Ocariz, M. et al. Rosacea as a striking feature in family members with a STAT1 gain-of-function mutation. J. Eur. Acad. 
Dermatol. Venereol. 34, e265–e267. https:// doi. org/ 10. 1111/ jdv. 16241 (2020).
 61. Deng, Z. et al. Keratinocyte-immune cell crosstalk in a STAT1-mediated pathway: Novel insights into rosacea pathogenesis. 
Front. Immunol. 12, 674871. https:// doi. org/ 10. 3389/ fimmu. 2021. 674871 (2021).
 62. Chung, E. Y . et al. The benzoxathiolone LYR-71 down-regulates interferon-gamma-inducible pro-inflammatory genes by uncou-
pling tyrosine phosphorylation of STAT-1 in macrophages. Br. J. Pharmacol. 158, 1971–1981. https:// doi. org/ 10. 1111/j. 1476- 5381. 
2009. 00496.x (2009).
 63. Agak, G. W . et al. Phenotype and antimicrobial activity of Th17 cells induced by propionibacterium acnes strains associated 
with healthy and acne skin. J. Invest. Dermatol. 138, 316–324. https:// doi. org/ 10. 1016/j. jid. 2017. 07. 842 (2018).
 64. Contassot, E. & French, L. E. Propionibacterium acnes strains differentially regulate the fate of Th17 responses in the skin. J. 
Invest. Dermatol. 138, 251–253. https:// doi. org/ 10. 1016/j. jid. 2017. 09. 041 (2018).
 65. Yu, Y . et al. Different propionibacterium acnes phylotypes induce distinct immune responses and express unique surface and 
secreted proteomes. J. Invest. Dermatol. 136, 2221–2228. https:// doi. org/ 10. 1016/j. jid. 2016. 06. 615 (2016).
 66. Hillmer, E. J., Zhang, H., Li, H. S. & Watowich, S. S. STAT3 signaling in immunity. Cytokine Growth Factor Rev. 31, 1–15. https:// 
doi. org/ 10. 1016/j. cytog fr. 2016. 05. 001 (2016).
 67. Carey, R. et al. Activation of an IL-6:STAT3-dependent transcriptome in pediatric-onset inflammatory bowel disease. Inflamm. 
Bowel Dis. 14, 446–457. https:// doi. org/ 10. 1002/ ibd. 20342 (2008).
 68. Li, Y . et al. Disease-related expression of the IL6/STAT3/SOCS3 signalling pathway in ulcerative colitis and ulcerative colitis-
related carcinogenesis. Gut 59, 227–235. https:// doi. org/ 10. 1136/ gut. 2009. 184176 (2010).
 69. Stoian, I., Manolescu, B., Atanasiu, V ., Lupescu, O. & Busu, C. IL-6 - STAT-3 - hepcidin: Linking inflammation to the iron 
metabolism. Rom. J. Intern. Med 45, 305–309 (2007).
 70. Wang, Y . et al. Multi-transcriptomic analysis and experimental validation implicate a central role of STAT3 in skin barrier 
dysfunction induced aggravation of rosacea. J. Inflamm. Res. 15, 2141–2156. https:// doi. org/ 10. 2147/ JIR. S3565 51 (2022).
 71. Li, T. et al. The therapeutic effect of artesunate on rosacea through the inhibition of the JAK/STAT signaling pathway. Mol. Med. 
Rep. 17, 8385–8390. https:// doi. org/ 10. 3892/ mmr. 2018. 8887 (2018).
 72. Baeuerle, P . A. & Baltimore, D. I kappa B: A specific inhibitor of the NF-kappa B transcription factor. Science  242, 540–546. 
https:// doi. org/ 10. 1126/ scien ce. 31403 80 (1988).
 73. Nagai, Y . et al. Essential role of MD-2 in LPS responsiveness and TLR4 distribution. Nat. Immunol. 3, 667–672. https:// doi. org/ 
10. 1038/ ni809 (2002).
 74. Karin, M. & Ben-Neriah, Y . Phosphorylation meets ubiquitination: The control of NF-[kappa]B activity. Annu. Rev. Immunol. 
18, 621–663. https:// doi. org/ 10. 1146/ annur ev. immun ol. 18.1. 621 (2000).
 75. Kim, M. H. et al. Novel iminobenzoxathiolone compound inhibits nuclear factor-kappaB activation targeting inhibitory kap -
paB kinase beta and down-regulating interleukin-1beta expression in lipopolysaccharide-activated macrophages. Biochem. 
Pharmacol. 76, 373–381. https:// doi. org/ 10. 1016/j. bcp. 2008. 05. 013 (2008).
 76. Chen, Q. et al. Propionibacterium acnes-induced IL-8 production may be mediated by NF-kappaB activation in human mono-
cytes. J. Dermatol. Sci. 29, 97–103. https:// doi. org/ 10. 1016/ s0923- 1811(02) 00013-0 (2002).
 77. Huang, Y . C., Y ang, C. H., Li, T. T., Zouboulis, C. C. & Hsu, H. C. Cell-free extracts of Propionibacterium acnes stimulate cytokine 
production through activation of p38 MAPK and Toll-like receptor in SZ95 sebocytes. Life Sci.  139, 123–131. https:// doi. org/ 
10. 1016/j. lfs. 2015. 07. 028 (2015).
 78. Wladis, E. J., Lau, K. W . & Adam, A. P . Nuclear factor kappa-B Is enriched in eyelid specimens of rosacea: Implications for 
pathogenesis and therapy. Am. J. Ophthalmol. 201, 72–81. https:// doi. org/ 10. 1016/j. ajo. 2019. 01. 018 (2019).
 79. Zhou, B. R. et al. Palmitic acid induces production of proinflammatory cytokines interleukin-6, interleukin-1beta, and tumor 
necrosis factor-alpha via a NF-kappaB-dependent mechanism in HaCaT keratinocytes. Mediators Inflamm. 2013, 530429. https:// 
doi. org/ 10. 1155/ 2013/ 530429 (2013).
 80. Li, Z. W . et al. The IKKbeta subunit of IkappaB kinase (IKK) is essential for nuclear factor kappaB activation and prevention of 
apoptosis. J. Exp. Med. 189, 1839–1845. https:// doi. org/ 10. 1084/ jem. 189. 11. 1839 (1999).
 81. Lius, V . & Sennerfeldt, P . Local treatment of acne with tioxolone. Lakartidningen 76, 39–41 (1979).
 82. Qi, C., Wang, Y ., Li, P . & Zhao, J. Gamma Delta T cells and their pathogenic role in psoriasis. Front. Immunol. 12, 627139. https:// 
doi. org/ 10. 3389/ fimmu. 2021. 627139 (2021).
 83. Kabelitz, D. & He, W . The multifunctionality of human Vgamma9Vdelta2 gammadelta T cells: Clonal plasticity or distinct 
subsets?. Scand. J. Immunol. 76, 213–222. https:// doi. org/ 10. 1111/j. 1365- 3083. 2012. 02727.x (2012).
 84. Riganti, C., Massaia, M., Davey, M. S. & Eberl, M. Human gammadelta T-cell responses in infection and immunotherapy: Com-
mon mechanisms, common mediators?. Eur. J. Immunol. 42, 1668–1676. https:// doi. org/ 10. 1002/ eji. 20124 2492 (2012).
 85. Saura-Esteller, J. et al. Gamma delta T-cell based cancer immunotherapy: Past-present-future. Front. Immunol.  13, 915837. 
https:// doi. org/ 10. 3389/ fimmu. 2022. 915837 (2022).
 86. Shiromizu, C. M. & Jancic, C. C. gammadelta T lymphocytes: An effector cell in autoimmunity and infection. Front. Immunol. 
9, 2389. https:// doi. org/ 10. 3389/ fimmu. 2018. 02389 (2018).
 87. Zheng, R. & Y ang, Q. The role of the gamma delta T cell in allergic diseases. J. Immunol. Res. 2014, 963484. https:// doi. org/ 10. 
1155/ 2014/ 963484 (2014).
 88. Laggner, U. et al. Identification of a novel proinflammatory human skin-homing Vgamma9Vdelta2 T cell subset with a potential 
role in psoriasis. J. Immunol. 187, 2783–2793. https:// doi. org/ 10. 4049/ jimmu nol. 11008 04 (2011).
 89. Spidale, N. A. et al. Neonatal-derived IL-17 producing dermal gammadelta T cells are required to prevent spontaneous atopic 
dermatitis. Elife 9, 51188. https:// doi. org/ 10. 7554/ eLife. 51188 (2020).

20
Vol:.(1234567890)Scientific Reports |         (2024) 14:3065  | https://doi.org/10.1038/s41598-024-53453-x
www.nature.com/scientificreports/
 90. Uchida, Y . et al. Pro-inflammatory Vdelta1(+)T-cells infiltrates are present in and around the hair bulbs of non-lesional and 
lesional alopecia areata hair follicles. J. Dermatol. Sci. 100, 129–138. https:// doi. org/ 10. 1016/j. jderm sci. 2020. 09. 001 (2020).
 91. Cai, Y . et al. Pivotal role of dermal IL-17-producing gammadelta T cells in skin inflammation. Immunity  35, 596–610. https:// 
doi. org/ 10. 1016/j. immuni. 2011. 08. 001 (2011).
 92. Y ang, L., Shou, Y . H., Y ang, Y . S. & Xu, J. H. Elucidating the immune infiltration in acne and its comparison with rosacea by 
integrated bioinformatics analysis. PLoS ONE 16, e0248650. https:// doi. org/ 10. 1371/ journ al. pone. 02486 50 (2021).
 93. Funes, S. C., Rios, M., Escobar-Vera, J. & Kalergis, A. M. Implications of macrophage polarization in autoimmunity. Immunology 
154, 186–195. https:// doi. org/ 10. 1111/ imm. 12910 (2018).
 94. Liu, P . et al. ALA-PDT augments intense inflammation in the treatment of acne vulgaris by COX2/TREM1 mediated M1 mac-
rophage polarization. Biochem. Pharmacol. 208, 115403. https:// doi. org/ 10. 1016/j. bcp. 2022. 115403 (2023).
 95. Zhou, L. et al. GBP5 exacerbates rosacea-like skin inflammation by skewing macrophage polarization towards M1 phenotype 
through the NF-kappaB signalling pathway. J. Eur. Acad. Dermatol. Venereol. 37, 796–809. https://  doi. org/ 10. 1111/ jdv. 18725 
(2023).
 96. Liu, Z. et al. Paeoniflorin inhibits the macrophage-related rosacea-like inflammatory reaction through the suppressor of cytokine 
signaling 3-apoptosis signal-regulating kinase 1–p38 pathway. Medicine 100, e23986. https:// doi. org/ 10. 1097/ MD. 00000 00000 
023986 (2021).
 97. Liu, T. et al. ADAMDEC1 promotes skin inflammation in rosacea via modulating the polarization of M1 macrophages. Biochem. 
Biophys. Res. Commun. 521, 64–71. https:// doi. org/ 10. 1016/j. bbrc. 2019. 10. 073 (2020).
 98. Huang, K. K., Zheng, H. L., Li, S. & Zeng, Z. Y . Identification of hub genes and their correlation with immune infiltration in 
coronary artery disease through bioinformatics and machine learning methods. J. Thorac. Dis. 14, 2621–2634. https:// doi. org/ 
10. 21037/ jtd- 22- 632 (2022).
 99. Jin, Z. et al. Identification of core genes associated with the anti-atherosclerotic effects of Salvianolic acid B and immune cell 
infiltration characteristics using bioinformatics analysis. BMC Complement. Med. Ther. 22, 190. https:// doi. org/ 10. 1186/ s12906- 
022- 03670-6 (2022).
 100. Wang, Y . et al. Analyzing the pathogenesis of systemic lupus erythematosus complicated by atherosclerosis using transcriptome 
data. Front. Immunol. 13, 935545. https:// doi. org/ 10. 3389/ fimmu. 2022. 935545 (2022).
 101. Liu, H. et al. Role of immune cell infiltration and small molecule drugs in adhesive capsulitis: Novel exploration based on 
bioinformatics analyses. Front. Immunol. 14, 1075395. https:// doi. org/ 10. 3389/ fimmu. 2023. 10753 95 (2023).
 102. Linton, S. S. et al. Tumor-promoting effects of pancreatic cancer cell exosomes on THP-1-derived macrophages. PLoS ONE 13, 
e0206759. https:// doi. org/ 10. 1371/ journ al. pone. 02067 59 (2018).
 103. Kanehisa, M. & Goto, S. KEGG: Kyoto encyclopedia of genes and genomes. Nucleic Acids Res. 28, 27–30. https:// doi. org/ 10. 
1093/ nar/ 28.1. 27 (2000).
 104. Kanehisa, M. Toward understanding the origin and evolution of cellular organisms. Protein Sci. 28, 1947–1951. https:// doi. org/ 
10. 1002/ pro. 3715 (2019).
 105. Kanehisa, M., Furumichi, M., Sato, Y ., Kawashima, M. & Ishiguro-Watanabe, M. KEGG for taxonomy-based analysis of pathways 
and genomes. Nucleic Acids Res. 51, D587–D592. https:// doi. org/ 10. 1093/ nar/ gkac9 63 (2023).
Acknowledgements
We thank the authors of the GSE65914, GSE108110, GSE53795, and GSE6475 datasets. This work was funded 
by the Natural Science Basic Research Program of Shaanxi (2023-JC-YB-787), Shaanxi Provincial Administra -
tion of Traditional Chinese Medicine (SZY-KJCYC-2023-062), and Xi’an Science and Technology Plan Project 
(2023JH-YXYB-0009) to Weihui Zeng.
Author contributions
Z.W . and W .Z. contributed to the study design. J.L., Y .C., Y .W . and S.M. contributed to the datasets processing 
and analysis. J.L., Z.W ., and D.Z. contributed to image processing. All authors contributed to the article and 
approved the submitted version.
Competing interests 
The authors declare no competing interests.
Additional information
Supplementary Information The online version contains supplementary material available at https:// doi. org/ 
10. 1038/ s41598- 024- 53453-x.
Correspondence and requests for materials should be addressed to Z.W . or W .Z.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International 
License, which permits use, sharing, adaptation, distribution and reproduction in any medium or 
format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the 
Creative Commons licence, and indicate if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the 
material. If material is not included in the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from 
the copyright holder. To view a copy of this licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.
© The Author(s) 2024