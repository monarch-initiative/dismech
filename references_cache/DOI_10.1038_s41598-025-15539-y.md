---
reference_id: DOI:10.1038/s41598-025-15539-y
title: Major pathophysiological changes in pulmonary disease provided a molecular insight based on deep learning approach
authors:
- Swaraj Mohanty
- Poornima Sharma
- Yasmin Ahmad
journal: Scientific Reports
year: '2025'
doi: 10.1038/s41598-025-15539-y
content_type: full_text_pdf
is_preprint: false
full_text_attempted: true
full_text_provider: openalex
full_text_url: "https://www.nature.com/articles/s41598-025-15539-y.pdf"
oa_status: gold
license: cc-by-nc-nd
local_pdf_path: files/DOI_10.1038_s41598-025-15539-y.pdf
---

# Major pathophysiological changes in pulmonary disease provided a molecular insight based on deep learning approach
**Authors:** Swaraj Mohanty, Poornima Sharma, Yasmin Ahmad
**Journal:** Scientific Reports (2025)
**DOI:** [10.1038/s41598-025-15539-y](https://doi.org/10.1038/s41598-025-15539-y)

## Content

Major pathophysiological changes 
in pulmonary disease provided a 
molecular insight based on deep 
learning approach
Swaraj Mohanty, Poornima Sharma & Yasmin Ahmad
The outburst of pulmonary disorders among the society has shown the devastating effect of 
undergoing a delay in diagnosis and treatment. Sometimes the traditional methods in detecting and 
treating the airway disease fail to cure efficiently due to a lack of pathophysiological descriptions along 
with the molecular expression. The studies published so far are missing the collective information 
of the pathways and the role of signature molecules during the disease that constricts the use of 
therapeutics like nitric oxide(NO) and hydrogen sulfide(H2S). In this mini systemic research article, we 
have followed the deep machine learning approach that is based on the artificial intelligence algorithm 
as a background search engine that compares various reported scientific studies and database 
information by building a network analysis platform to better understand the molecular pathways that 
show a correlation with the other molecules. We followed the MEDLINE search to list the published 
studies for all the major pulmonary diseases, and the published literature from the NIH database 
was used to list out the genes and translated proteins associated with the major pulmonary diseases. 
For the pathways and the associated molecular information, the ShinyGo tool has been used. The 
published studies till December 2023 have been represented in this article. Bioinformatics analysis of 
the disease was analyzed based on the expression profiles of the genes and the major proteins from 
the protein-protein interaction STRING network, concluding that the perturbed molecules interplay 
a vital role in the progression of airway diseases and targeting the major pathways can be a possible 
therapeutic intervention for curing the disease.
Keywords Pulmonary disease, Hypoxia, Gene ontology, STRING, Disease network pathways
In the last decade, the expanding growth in population and atmospheric changes due to the sustainable 
developments for a better lifestyle are leading to various diseases. In this context, the pulmonary diseases are 
the major lethal diseases, depending upon the pathophysiology. Due to the direct gaseous exchange from the 
atmosphere and the major site of gaseous exchange with the body fluid, the pulmonary system is considered 
to be a major system of any living individual. The airways and the organ i.e. the lung are believed to be the 
most affected sites during the pulmonary disease1,2. As per the World Health Organization(WHO) based on the 
damage and clinical severity, there are mainly three categories of lung disease: airway disease, lung tissue disease 
and lung circulating disease 3. The narrowing and blockage caused to the tubes that carry oxygen and other 
gases leads to the following clinical conditions, like bronchiectasis, asthma and chronic obstructive pulmonary 
disease(COPD), in which an individual feels they struggle to breathe out through a straw 4–7. Sometimes the 
structural organization of the lung tissues deforms in such a way that the patient feels like they are wearing a very 
tight vest or sweater and the lungs are unable to expand up to their maximum capacity, causing sarcoidosis and 
pulmonary fibrosis(PF)8–10. And the patho-physiologically most active and lethal condition developed with a 
prolonged inflammation, scarring and clotting underlying the blood vessel affecting the normal cardiac function 
with a shortening of the expiratory volume of impure gases unbalancing the circulatory fluid is commonly 
termed as pulmonary hypertension(PH). In almost all the above-mentioned conditions we can observe an 
onset of physiological dysregulation of the molecular signatures starting from the epithelial cell line of the 
lungs and the redox regulatory effects of pro-inflammatory cell signaling molecules of the tissue disturbing the 
homeostasis of the cells11–13. In this article we have explained the molecular and pathophysiological information 
Disruptive & Deterrence Technology (DDT) Division, Defence Institute of Physiology & Allied Sciences (DIPAS), 
Defence R & D Organization (DRDO), Timarpur, New Delhi 110054, India. email: yasminchem@gmail.com
OPEN
Scientific Reports |        (2025) 15:32024 1| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports


from the network biology and the possible role of the associated chemically active biomolecules as a therapeutic 
intervention.
Methodology
The most commonly occurring respiratory diseases were taken into account in designing the study; hence the 
list of published genes in Homo sapiens related to the disease has been retrieved from the National Center for 
Biotechnology Information(NCBI) database(http://www.ncbi.nlm.nih.gov/gene/). The literature search process 
was retrieved by entering the keywords such as Asthma, Bronchiectasis, COPD, PF , PH & Sarcoidosis in PubMed 
and only published literature after the year 2000 has been included to gather information. The more focused 
molecular mechanisms, reported case studies on humans have been taken into consideration. The retrieved 
information on gene symbols was considered for the gene ontology(GO) study through the  s e r v e r (   h t t p : / / b i o i n f 
o r m a t i c s . s d s t a t e . e d u / g o 8 0 /     ) separately for all five different diseases Table-1 (Supplementary File 1)14. The main 
basic algorithm uses a knowledge-base deep machine learning approach on gene level differential expression 
analysis normalization with the Fragments Per Kilobase per Million mapped fragments(FPKMs) of each gene 
across all the samples. The background computations were based on the fold change information with the log 
transformations, K-means & hierarchical clustering to perform the functional enrichment analysis and gene 
ontology prediction from the submitted gene sets. Similarly, the list of mapped gene symbols from the GO 
analysis was listed and uploaded into a web-based tool for the common gene pool interaction through Venn 
diagram representation(https://bioinformatics.psb.ugent.be/webtools/Venn/).
Here we set the best matching species as human, Kyoto Encyclopedia of Genes and Genomes(KEGG) as the 
searching database, with a false discovery rate(FDR) of 0.05 as the cutoff. After analysis the fold enrichment 
bar chart of genes and different disease plots, the number of genes located in all sets of chromosomes, enriched 
disease pathways and their associated network interaction, chi-squared distribution of the number of coding 
genes, exons, transcript isoforms were generated. The gene information from the curated data available in the 
public literature has been analyzed and based on the fold enrichment and number of differentially expressed genes 
identified or mapped to date, we have shortlisted the disease pathways for our study, like cancer progression, 
cytokine-cytokine interaction, PI3-AKT and chemokine signaling pathways for all the major pulmonary diseases 
in this study Table-3 (Supplementary File 3) (Fig. 1). The functional analysis of the differentially expressed genes 
in the disease pathways was studied by gene set enrichment analysis(GSEA) from the curated information stored 
in the KEGG database of the top 30 pathways with an FDR cutoff of < 0.05 and an edge cutoff of 0.3.
Results and discussions
Genetic association
The genetic similarity between the major pulmonary diseases has been diagrammatically correlated with the 
differential gene information data available in the public databases and the similarities among the genes have 
been represented in the Venn diagram form (Fig.  2). There is variation among the chromosome pairs with a 
variable p-value; the enriched regions in different chromosome loci vary i.e. 14 in the case of Asthma, 16 in 
Bronchiectasis, 10 in COPD, 8 in PF , 5 in PH and 13 in Sarcoidosis (Fig. 3). The distributed pattern of the genes 
in the chromosome was found to be higher in all the considered disease conditions than the expected number 
of genes at the normal condition of any individuals. The higher the genetic distribution in the chromosomes the 
more the possibilities of developing resistant to disease conditions (Fig. 4).
Signaling pathways & associated proteins
Disease network
The list of genes in different disease conditions was downloaded from the database and listed for further study. 
After the analysis we observed the, number of differentially expressed genes in the above disease with respect 
to the total number of reported mapped genes in the same disease Table-2 (Supplementary File 2). And the 
distribution of differentially expressed genes involved in the top 30 pathways was shown in lollipop chart plot 
form (Fig.  5). In case of Asthma, the pathways of cancer, cytokine-cytokine receptor interaction, PI3k-AKT 
signaling and chemokine signaling are the most focused pathways due to the maximum number of differentially 
expressed genes in the available public literature. The mucosal layer of the inner airways undergoes mucosal 
metaplasia during the progression of bronchiectasis due to bacterial and viral infection, leading to the production 
of oxidative stress and inflammatory cell production15,16. Chronic bronchiectasis and emphysema sometimes are 
the lead causes of COPD hence based on the differential expression of the proteins only, we have considered the 
pathways of cancer, cytokine-cytokine receptor interaction, PI3k-AKT signaling and chemokine signaling in 
our study. Due to environmental changes and smoking habitat lifestyles, a variety of pulmonary fibrosis have 
emerged in the population and are sometimes not detectable unless the disease reaches a severe stage. The 
idiopathic pulmonary fibrosis is the most fatal type of disease that is very difficult to treat and the lifespan of 
the patient may last till 10 years17. Hence, we have taken into focus the signaling pathways of cancer, cytokine-
cytokine receptor interactions and the PI3k-AKT pathway to check the interaction of the genes during this 
disease condition. The pulmonary circulation is mostly affected due to the severe conditions like coronary artery 
disease, connective tissue disease, heart disease, chronic lung disease, development of hypoxia-like conditions, 
or clots in the lungs, which ultimately triggers the pulmonary hypertension in an individual 18–21. There is no 
specific cure for this disease and hence we have considered the following pathways of cancer progression, 
interaction of cytokine-cytokine receptors, the PI3k-AKT pathway and chemokine signaling for gene expression 
study. Sarcoidosis is a multisystem inflammatory disease that mainly occurs in the lymph nodes of the body 
and may last for years, causing temporary or permanent damage at the tissue lining; hence, we have focused on 
Scientific Reports |        (2025) 15:32024 2| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

the cancer progression, cytokine-cytokine receptor interaction, PI3k-AKT signal transduction and chemokine 
signaling pathway for this analysis22.
The green nodes represent the GO terms and the connections among them with gray lines; larger the size of 
node, more the number of differentially expressed genes and thicker the gray edges represent the occurrence of 
the common genes among the disease genes. The cancer progression and cytokine-cytokine receptor signaling 
are the most prominent pathways containing the greatest number of differential genes in case of all the diseases 
mentioned above, excluding bronchiectasis. The PI3k-AKT and chemokine signaling pathways are the related 
pathways with the other major protein signaling pathways like mitogen activated protein kinase(MAPK), 
hypoxia-inducible factor(HIF)−1 and Ras proximate(Rap)−1 hence, to better understand the gene expression 
and activation of signal cascades during the pulmonary disease considered for this expression study (Fig. 6).
The enriched disease network associations are also observed from the KEGG pathway as predicted 
computational protein-protein interactions of the top 30 related proteins through the STRING analysis platform 
that talks about the physical and functional relationship among different proteins available in a primary database 
Fig. 1. Shows the schematic methodology of the data retrieval process from the public literature and gene 
ontology analysis through machine learning approach.
 
Scientific Reports |        (2025) 15:32024 3| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

Fig. 3. Distribution of the listed genes associated with different diseases like Asthma(A), Bronchiectasis(B), 
COPD(C), Pulmonary Fibrosis(D), Pulmonary Hypertension(E) and Sarcoidosis(F) along with the significant 
enriched regions of the genes on the chromosome.
 
Fig. 2. Distribution of the listed genes associated with different diseases like Asthma, Bronchiectasis, COPD, 
Pulmonary Fibrosis, Pulmonary Hypertension and Sarcoidosis in the Venn diagrammatic representation.
 
Scientific Reports |        (2025) 15:32024 4| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

(Fig. 7)23,24. It has also been studied that there are many similarities among the signaling pathways and molecules 
get al.tered during pulmonary diseases, cancer progression, inflammation and high-altitude illness, so there 
may exist a similar pattern of molecular mechanism 25–28. During the tumor progression and angiogenesis, the 
supply of oxygen and nutrients is essential to keep the angiogenic switch activated. The cells that are present at 
the center of tumor microenvironment undergo hypoxic stress, leading to the accumulation of hypoxia-inducing 
factors(HIF) that also trigger the expression of target genes like vascular endothelial growth factor(VEGF) 29,30. 
Janus kinase 1(JAK1) is the protein coded from the locus of the JAK gene activated by the cellular surface 
receptors during cytokine-cytokine interaction due to phosphorylation and promotes upregulation of the signal 
transducer and activation of transcription(STAT) family proteins coding gene 31–33. Triggering one from both 
the events i.e. activation of HIF or STAT family genes, can activate VEGF signaling regulating the vascular 
permeability during the vasculogenesis 34,35. In asthma, sarcoidosis, PF and PH the JAK1 gene is upregulated, 
activating the JAK/STAT signaling pathway, but in the case of COPD the VEGF is activated, which is due to HIF 
signaling, which denotes that both HIF and STAT family proteins are responsible for VEGF activation.
Cancer signaling pathways
During tumor progression and angiogenesis, the supply of oxygen and nutrients is essential to keep the 
angiogenic switch activated. The cells that are present at the center of the tumor microenvironment undergo 
hypoxic stress, leading to accumulation of hypoxia-inducing factors(HIF) that also trigger the expression of 
target genes like vascular endothelial growth factor(VEGF)29,36. Janus kinase 1(JAK1) is the protein coded from 
the locus of JAK gene activated by the cellular surface receptors during cytokine-cytokine interaction due to 
phosphorylation and promotes upregulation of the signal transducer and activation of transcription(STAT) 
family proteins coding gene. Triggering one from both the events i.e. activation of HIF or STAT family genes, 
can activate VEGF signaling regulating the vascular permeability during the vasculogenesis34,37. In asthma & PH 
the PI3K gene expression triggers the protein kinase B(PKB) gene, downregulating the transcription factor like 
forkhead homologue in rhabdomyosarcoma(FKHR) and the upregulation of mouse double minute 2(MDM2) 
with no regulation of the differential expression of tumor protein 53(p53) leads to the suppression of cell death 
due to apoptosis38,39. The extremity in physiological changes in any individual leading to cellular stress transmits 
a signal from the cytoplasm inside the nucleus through STAT family proteins, showing damages in the hereditary 
unit of cells, and p53 acts as a tumor regulator as it involves approximately 500 genes and modulators to initiate 
the repair, restoration of diverse cellular process and maintenance of cellular homeostasis 40. The mammalian 
target of Rapamycin(mTOR) inhibitors is well proved for its therapeutic properties against tumor progression, 
arthritis, organ transplantation, autoimmune and neurodegenerative disorders41. Han et al.. cited that the mTOR 
signaling activation helps in evading apoptosis by autophagy; same can be observed from the cellular network in 
PF and COPD. mTOR signaling controls cell growth and metabolism by mTOR complex 1 and cell proliferation 
and survival by mTOR complex 2 42,43. Elevation in the expression level of p21 gene reported to inhibit the S 
Fig. 4. Chi-square distribution of the listed genes associated with different diseases like Asthma(A), 
Bronchiectasis(B), COPD(C), Pulmonary Fibrosis(D), Pulmonary Hypertension(E) and Sarcoidosis(F) along 
with the significant enriched regions of the genes on the chromosome.
 
Scientific Reports |        (2025) 15:32024 5| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

phase of cell cycle along with the phosphorylation of Threonine 145 and Serine 146 hence overall inhibits the 
cell proliferation in COPD, PF and sarcoidosis44 (Fig. 8).
Cytokine−cytokine interaction signaling pathway
In a healthy individual, immunity plays a vital role in fighting against the infections and protecting the organs 
from the tissue damage; the cytokines released at the site in the damage area and act as chemical messengers 
for the immune cells when secreted in the body fluids. There are mainly two kinds of cytokines that govern a 
systemic cellular and tissue physiology at the organ level i.e. pro-inflammatory and anti-inflammatory cytokines, 
which trigger and shut down the immune cell activation respectively. There are different types of proteins like 
chemokines, interferons, interleukins, and tumor necrosis factors(TNF), that guide the immune cells to activate 
and suppress after their targeted action. The most chronic respiratory tract infections like asthma, bronchiectasis 
and COPD involve both the pro- and anti-inflammatory cytokines through the Toll-like receptors(TLRs) 
signalling that produces the TNF and Interleukin-1 family cytokines45,46. The CC subfamily cytokines are mainly 
known for the presence of two adjacent cysteines in the amino acid sequence with two distinct C-C chemokine 
receptors(CCR) which guides the immune cells and C-C motif chemokine ligand(CCR) which attracts and 
activates the immune cells towards the site of inflammation47.
In the past Jie et al. reported on its elevated activation and the effect of monocyte chemoattractant protein-
1(MCP-1) in the alveolar macrophages during hypoxia-like pathophysiological conditions in a liposome-
mediated rat model study 48–50. The gene ontology of the similar pulmonary disease considered in this study 
also directs the differential expression of CCL2 and CCL12 genes in the network, which are found to show 
the regulatory effect through CCR2 but in case of PH the direct upregulation has been reported 51 (Fig.  9). 
Transforming growth factor beta(TGFβ) family cytokines are mainly known for their pleiotropic effect during 
immunoregulation, wound healing and angiogenesis with the involvement of other transcription factors. 
Although the roles of different cytokines like growth differentiation factor(GDF) and bone morphogenetic 
proteins(BMP) are topics of interest in case of hypoxia and other pulmonary diseases, they are still an area of 
investigation for COPD52 and sarcoidosis53–56.
PI3-AKT signaling pathway
Exploring the PI3-AKT signaling opens new doors in the complex cellular signal transduction and clinical 
research with the involvement of multiple genes and transcription factors in various disease conditions with a 
direct implication in cell growth, metabolism, inflammation, aging, cancer and personalized medicine research. 
Being an intracellular signal transduction pathway, the activation is mediated through phosphorylation of serine 
Fig. 5. Major highlighted pathways based on the fold enrichment for the differentially expressed genes 
in different diseases Asthma(A), Bronchiectasis(B), COPD(C), Pulmonary Fibrosis(D), Pulmonary 
Hypertension(E) and Sarcoidosis(F).
 
Scientific Reports |        (2025) 15:32024 6| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

or threonine residues of downstream substrates in different cell types. The TLR, GPCR and other cytokine cell 
surface receptors activate the class-I phosphatidylinositol 3-kinase(PI3K) through the phosphatidylinositol-
4,5-bisphosphate (PIP2) to phosphatidylinositol-3,4,5-bisphosphate (PIP3) phosphoinositide metabolism. The 
differential expression of AKT directs various cellular signaling processes like NFkB, p53 signaling, angiogenic 
DNA repair, protein synthesis, glycolysis and gluconeogenesis, cell proliferation, survival and cell cycle 
under different pathophysiological conditions 57. In addition to these signaling cascades the protein synthesis 
during PI3K-AKT pathway is positively regulated due to the repressed expression of phosphatase and tensin 
homolog(PTEN)58,59. Similarly, the negative regulation of AKT activation through the modulation of mTOR 
complex 1 and the S6 kinase1(S6K1) that phosphorylates the insulin receptor substrate-1(IRS-1) suppresses 
the PI3K activation 60. Examining the upstream and downstream nodes, researchers have flagged the role of 
targeting the receptor tyrosine kinases(RTK) during the cancer therapy for the suppression of PI3K activation 
that opens new opportunities in drug discovery61–64.
In case of asthma, PH and PF the AKT activation regulates the VEGF signaling and the MAPK signaling 
pathways through the eNOS and ERK gene expression. During prolonged hypoxia-like conditions, the NFkB 
and c-AMP response element-binding protein(CERB) upregulates the matix-metallopeptidase 1(MMP-1) at 1% 
and 5% of O2
65,66. In contrast, the expression of VEGF , HIF-1α & 1β are not prominent at 5% O2 concentration 
and a clear indication has been reported at 1% O2 controlled conditions. The AKT is not well expressed in COPD 
and sarcoidosis, but the involvement of many accessory transcription factors like NFkB, p21 and CREB helps in 
the cell survival as well as the cell cycle progression (Fig. 10).
Chemokine signaling pathway
The significant implications of the chemokines in the immune system and inflammatory conditions in various 
disease signaling studies can’t be neglected due to their regulatory responses in the cellular signaling and 
mechanistic study. Usually chemokines are small peptide or protein molecules ranging from 7 to 12 kDa size 
classified into four major subfamilies based on the cysteine residues proximity in the amino terminal. Due to 
their ubiquitous size and high binding affinity, the chemokines bind to the similar type of chemokines and 
subsequently with multiple receptors for signal cascade activation within the cell 67. The chemokines are best 
known for guiding the immune cells to the site of infection or tissue damage due to injury or internal and 
external stimulus. Sometimes the over-expression of the chemokine signaling can lead to excessive inflammation 
by the hyperactivation of innate immunity. The activation of chemotactic cytokine receptors present on the cell 
surfaces helps in the process of chemotaxis due to the activation of kinases, changes in calcium level leading 
to the cytoskeletal reorganization and cell movement 68. The cell surface chemokine receptors interact with the 
Fig. 6. Enriched diseases pathways and its associated network interaction Asthma(A), Bronchiectasis(B), 
COPD(C), Pulmonary Fibrosis(D), Pulmonary Hypertension(E) and Sarcoidosis(F).
 
Scientific Reports |        (2025) 15:32024 7| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

active site of the chemokines and activate the signaling molecular cascade inside the cytoplasm and subcellular 
locations.
The major involvement of Janus kinase/signal transducer and activator of transcription(JAK/STAT) signaling 
pathway during cell communication to regulate cellular growth and differentiation, migration, apoptosis, 
hematopoiesis, cytokine production and tissue repair is seen in many cell types 69. Transportation of the 
dimerized form of tyrosine-phosphorylated STATs into the nucleus through the nuclear membrane helps in the 
regulation of accessory genes that maintain cellular homeostasis. In case of asthma, PH and sarcoidosis JAK2/3 
gene is found to be differentially expressed and triggers the STAT family genes to regulate the phosphorylation 
process after binding the cytokines to the chemokine receptors on the cell membrane (Fig. 11). Studies on JAK2 
knockout mice also explain the similarity pattern in the necessity of JAK2 phosphorylation showing defects 
in interferon-γ(IFN- γ) similar to impaired hematopoiesis in the erythropoietin(EPO) knockout model 70,71. 
JAK3 inactivation in the zebrafish model is known for its regulation of autosomal recessive severe combined 
immunodeficiency(SCID) and production of autoreactive T cells in the mice model72. In COPD and asthma, the 
major genes like steroid receptor coactivator(Src)73–75, rat sarcoma(Ras) family76–78, PI3k79, ERK1/280,81, NFkB 
and AKT82,83 genes found to be differentially expressed and maintain the major cellular metabolic processes 84. 
The mucosal inflammation is a major phenomenon during the pulmonary diseases and the cytoskeletal 
remodeling is a major event that governs the immunity to act against the pathogens. During the process of 
inflammation, the free radical generation, cytokine accumulation and lipid disruption in the epithelial tissue 
trigger the transcriptional events of cytoskeletal genes. It has also been investigated by Kayyali et al. that during 
the hypoxia exposure there is an alteration of permeability and the motility of the endothelial barriers of cells85 
needs further investigation.
In a pulmonary endothelial cell line study, authors have indicated the actin filaments show a web-like 
pattern in the normoxic condition, whereas after the 30  min of exposure, they start changing shape and at 
1 h, they show a conformational change into a parallel stress fiber-like arrangement 86. In our gene ontology 
study, we have also seen that the Rac and rhodopsin(RHO) family and Rho-associated protein kinase(ROCK) 
genes show differential expression during asthma, COPD and PH like diseases which play a major role during 
actin cytoskeletal remodeling87–91. The negative feedback regulation of GPCRs is β-arrestins(ARRB1 & ARRB2) 
and acts as the scaffolding protein for many inflammatory signaling and metabolic regulations during chronic 
inflammation, alcoholic liver disease(ALD), aging and asthma like pulmonary disorders92–94. The ability of anti-
apoptotic signal transduction to trigger different signaling processes in the cell places it under the therapeutic 
target in different disease conditions and also makes it well studied in physiological conditions like ischemic 
injury and HAPE95–97.
Fig. 7. Protein−protein interactions for the top 30 enriched proteins for the diseases like Asthma(A), 
Bronchiectasis(B), COPD(C), Pulmonary Fibrosis(D), Pulmonary Hypertension(E) and Sarcoidosis(F).
 
Scientific Reports |        (2025) 15:32024 8| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

Fig. 8. The activation of enriched genes during the cancer progression in cellular signalling pathways for 
different disease pathways like Asthma(A), COPD(B), Pulmonary Fibrosis(C), Pulmonary Hypertension(D) 
and Sarcoidosis(E).
 
Scientific Reports |        (2025) 15:32024 9| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

Study limitations
The framed knowledge-based study conducted in this article comprises the information available in the NCBI 
data repository till the end of 2023 hence, we always recommend the investigators revalidate for any further 
update outcomes if necessary for their study. Due to time constraints and the limited access to the clinical 
Fig. 9. The activation of enriched genes during the cytokine-cytokine interaction signalling pathways in 
different disease like Asthma(A), COPD(B), Pulmonary Fibrosis(C), Pulmonary Hypertension(D) and 
Sarcoidosis(E).
 
Scientific Reports |        (2025) 15:32024 10| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

Fig. 10. The activation of enriched genes during PI3-AKT signalling pathways the different disease pathways 
like Asthma(A), COPD(B), Pulmonary Fibrosis(C), Pulmonary Hypertension(D) and Sarcoidosis(E).
 
Scientific Reports |        (2025) 15:32024 11| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

samples for the major diseases, we couldn’t investigate the above-mentioned molecular signaling pathways and 
cellular processes through wet-lab in this designed study and kept it open for the scientific community working 
to address them with their expertise by referring to our structured article.
Conclusion
Elucidating the outcomes of this study with the machine learning approach not only simplified in getting the 
compilation of major signaling pathways discovered to date but also draws a conclusion on the key molecules 
like VEGF , STAT, PI3K, AKT signaling and the interrelated molecular cascade of eNOS, HSP90, CDK, GPCR 
in the progression of the disease. And from the gene ontology study, it also clear that the expression pattern 
may differ in disease type, but the molecular mechanism has an interlinking molecular cascade activation in 
all types of pulmonary diseases with a common mode of pathophysiological principle triggering its molecular 
signatures. Although in our present study we tried to reveal the possible mechanism relation among the major 
pathways from a data mining approach for different pulmonary diseases in a concise manner, focusing on 
various aspects like inflammation, redox signaling and metabolic perturbed signaling processes, there are many 
gaps and solid evidence on the molecular mechanism of hypoxia that need serious attention from the global 
researchers. The futuristic studies on these lagging areas should involve the high-throughput techniques to 
explore the pathophysiology and molecular mechanistic approach in understanding the therapeutic possibilities 
by targeting the major common pathways in between gene and protein expression studies at the cellular and 
subcellular level. And the exploration of these pathophysiological studies will definitely open new doors in 
Fig. 11. The activation of enriched genes during chemokine signalling pathways in different diseases like 
Asthma(A), COPD(B), Pulmonary Hypertension(C) and Sarcoidosis(D).
 
Scientific Reports |        (2025) 15:32024 12| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

understanding the target molecules and the development of pre-diagnostic therapeutic strategies, leading to a 
pharmaceutical revolution in upcoming days to a disease-free life.
Data availability
All data generated or analyzed during this study are included in this published article (and its Supplementary 
information files) and the data presented in this study are available on request from the corresponding author.
Received: 19 January 2024; Accepted: 8 August 2025
References
 1. Gadkowski, L. B. & Stout, J. E. Cavitary pulmonary disease. Clin. Microbiol. Rev. 21(2), 305–333 (2008).
 2. Becklake, M. R. Asbestos-related diseases of the lung and other organs: their epidemiology and implications for clinical practice. 
114(1), 187–227. (1976).
 3. Garcia, C. K. Insights from human genetic studies of lung and organ fibrosis. J. Clin. Invest. 128 (1), 36–44 (2018).
 4. Vogelmeier, C. F . et al. Efficacy and safety of once-daily QV A149 compared with twice-daily salmeterol–fluticasone in patients 
with chronic obstructive pulmonary disease (ILLUMINATE): a randomised, double-blind, parallel group study. Lancet Respiratory 
Med. 1 (1), 51–60 (2013).
 5. Singh, S. J. et al. An official systematic review of the European respiratory society/american thoracic society: measurement 
properties of field walking tests in chronic respiratory disease. Eur. Respir. J. 44 (6), 1447–1478 (2014).
 6. Behr, J. & Ryu, J. H. Pulmonary hypertension in interstitial lung disease. Eur. Respir. J. 31 (6), 1357–1367 (2008).
 7. Wysham, N. G. et al. Symptom burden of chronic lung disease compared with lung cancer at time of referral for palliative care 
consultation. Annals Am. Thorac. Soc. 12 (9), 1294–1301 (2015).
 8. Costabel, U. Sarcoidosis: clinical update. Eur. Respir J. Suppl. 32 (32 suppl), 56s–68s (2001).
 9. Martinez, F . J. et al. Idiopathic pulmonary fibrosis. Nat. Reviews Disease Primers. 3 (1), 1–19 (2017).
 10. Richeldi, L., Collard, H. R. & Jones, M. G. Idiopathic pulmonary fibrosis. Lancet 389 (10082), 1941–1952 (2017).
 11. Barnes, P . J. The cytokine network in asthma and chronic obstructive pulmonary disease. J. Clin. Invest. 118 (11), 3546–3556 
(2008).
 12. Manevski, M. et al. Cellular stress responses and dysfunctional Mitochondrial–cellular senescence, and therapeutics in chronic 
respiratory diseases. Redox Biol. 33, 101443 (2020).
 13. Sgalla, G. et al. Idiopathic pulmonary fibrosis: pathogenesis and management. Respir Res. 19 (1), 32 (2018).
 14. Ge, S. X., Jung, D. & Y ao, R. ShinyGO: a graphical gene-set enrichment tool for animals and plants. Bioinformatics 36 (8), 2628–
2629 (2020).
 15. Mann, T. S. et al. Azithromycin inhibits mucin secretion, mucous metaplasia, airway inflammation, and airways hyperresponsiveness 
in mice exposed to house dust mite extract. Am. J. Physiol. Lung Cell. Mol. Physiol. 322 (5), L683–L698 (2022).
 16. Jeffery, P . K. Remodeling in asthma and chronic obstructive lung disease. Am. J. Respir Crit. Care Med.  164 (10 Pt 2), S28–38 
(2001).
 17. Aurora, P . et al. A model for predicting life expectancy of children with cystic fibrosis. Eur. Respir J. 16 (6), 1056–1060 (2000).
 18. Mavrogeni, S. et al. Cardiovascular magnetic resonance imaging: clinical implications in the evaluation of connective tissue 
diseases. J. Inflamm. Res. 10, 55–61 (2017).
 19. Ungprasert, P . et al. Cardiac involvement in mixed connective tissue disease: a systematic review. Int. J. Cardiol. 171 (3), 326–330 
(2014).
 20. Seeger, W . et al. Pulmonary hypertension in chronic lung diseases. J. Am. Coll. Cardiol. 62 (25 Suppl), D109–D116 (2013).
 21. Veit, F . et al. Hypoxia-dependent reactive oxygen species signaling in the pulmonary circulation: focus on ion channels. Antioxid. 
Redox Signal. 22 (6), 537–552 (2015).
 22. Hillegass, E. Essentials of Cardiopulmonary Physical Therapy- E-Book (Elsevier, 2022).
 23. Luo, W . & Brouwer, C. Pathview: an r/bioconductor package for pathway-based data integration and visualization. Bioinformatics 
29 (14), 1830–1831 (2013).
 24. Kanehisa, M. et al. KEGG for taxonomy-based analysis of pathways and genomes. Nucleic Acids Res. 51 (D1), D587–D592 (2023).
 25. Mehta, M. et al. Cellular signalling pathways mediating the pathogenesis of chronic inflammatory respiratory diseases: an update. 
Inflammopharmacology 28 (4), 795–817 (2020).
 26. Raguraman, R. et al. Therapeutic approaches targeting molecular signaling pathways common to diabetes, lung diseases and 
cancer. Adv. Drug Deliv Rev. 178, 113918 (2021).
 27. Basnyat, B. & Murdoch, D. R. J. T. L. High-altitude Illn. 361(9373): 1967–1974. (2003).
 28. El Alam, S. et al. Inflammation in pulmonary hypertension and edema induced by hypobaric hypoxia exposure. Int. J. Mol. Sci. 23 
(20), 12656 (2022).
 29. Chen, M. C. et al. Magnolol suppresses hypoxia-induced angiogenesis via Inhibition of HIF-1α/VEGF signaling pathway in human 
bladder cancer cells. Biochem. Pharmacol. 85 (9), 1278–1287 (2013).
 30. Wu, C. et al. Wnt/β-catenin coupled with HIF-1α/VEGF signaling pathways involved in Galangin neurovascular unit protection 
from focal cerebral ischemia. Sci. Rep. 5 (1), 16151 (2015).
 31. Damsky, W . et al. The emerging role of Janus kinase inhibitors in the treatment of autoimmune and inflammatory diseases. J. 
Allergy Clin. Immunol. 147 (3), 814–826 (2021).
 32. Houreld, N. N. Regulation of Cytokine Signaling by the JAK-STAT Pathway. In JAK-STAT Signaling in Diseases 1–8 (CRC Press, 
2020).
 33. Chen, J. et al. Cytokine receptor signaling is required for the survival of ALK– anaplastic large cell lymphoma, even in the presence 
of JAK1/STAT3 mutations. Proc. Natl. Acad. Sci. 114 (15), 3975–3980 (2017).
 34. Guo, Q. et al. Salidroside improves angiogenesis-osteogenesis coupling by regulating the HIF-1α/VEGF signalling pathway in the 
bone environment. Eur. J. Pharmacol. 884, 173394 (2020).
 35. Ganji, P . N. et al. Antiangiogenic effects of Ganetespib in colorectal cancer mediated through Inhibition of HIF-1α and STAT-3. 
Angiogenesis 16, 903–917 (2013).
 36. Wu, C. et al. Wnt/β-catenin coupled with HIF-1α/VEGF signaling pathways involved in Galangin neurovascular unit protection 
from focal cerebral ischemia. Sci. Rep. 5(1), 1–11 (2015).
 37. Ferrara, N. The role of the Vegf signaling pathway in tumor angiogenesis. In Tumor Angiogenesis: A Key Target for Cancer Therapy 
211–226 (Springer, 2019).
 38. Nakano, K. & Vousden, K. H. PUMA, a novel proapoptotic gene, is induced by p53. Mol. Cell. 7 (3), 683–694 (2001).
 39. Letai, A. Apoptosis and cancer. Annual Rev. Cancer Biology. 1, 275–294 (2017).
 40. Aubrey, B. J. et al. How does p53 induce apoptosis and how does this relate to p53-mediated tumour suppression? Cell Death Differ. 
25(1), 104–113 (2018).
 41. Zou, Z. et al. mTOR signaling pathway and mTOR inhibitors in cancer: progress and challenges. Cell. Biosci. 10 (1), 31 (2020).
Scientific Reports |        (2025) 15:32024 13| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

 42. Xie, Y . et al. mTOR in programmed cell death and its therapeutic implications. Cytokine Growth Factor. Rev. 71-72, 66–81 (2023).
 43. Fernald, K. & Kurokawa, M. Evading apoptosis in cancer. Trends Cell. Biol. 23 (12), 620–633 (2013).
 44. Li, Y ., Dowbenko, D. & Lasky, L. A. AKT/PKB phosphorylation of p21Cip/W AF1 enhances protein stability of p21Cip/W AF1 and 
promotes cell survival. J. Biol. Chem. 277 (13), 11352–11361 (2002).
 45. Chung, K. F . Cytokines in chronic obstructive pulmonary disease. Eur. Respir J. Suppl. 34 (34 suppl), 50s–59s (2001).
 46. Barnes, P . J. The cytokine network in chronic obstructive pulmonary disease. Am. J. Respir. Cell Mol. Biol. 41(6), 631–638 (2009).
 47. Novita, B. D. et al. Characterization of chemokine and cytokine expression pattern in tuberculous lymphadenitis patient. Front. 
Immunol. 13, 983269 (2022).
 48. Chao, J. et al. Monocyte chemoattractant protein–1 released from alveolar macrophages mediates the systemic inflammation of 
acute alveolar hypoxia. Am. J. Respir. Cell Mol. Biol. 45 (1), 53–61 (2011).
 49. Mojsilovic-Petrovic, J. et al. Hypoxia-inducible factor-1 (HIF-1) is involved in the regulation of hypoxia-stimulated expression of 
monocyte chemoattractant protein-1 (MCP-1/CCL2) and MCP-5 (Ccl12) in astrocytes. J. Neuroinflamm. 4 (1), 1–15 (2007).
 50. Fröhlich, S., Boylan, J. & McLoughlin, P . Hypoxia-induced inflammation in the lung: a potential therapeutic target in acute lung 
injury? Am. J. Respir. Cell Mol. Biol. 48 (3), 271–279 (2013).
 51. Li, Y . T. et al. Monocyte chemoattractant Protein-1, a possible biomarker of multiorgan failure and mortality in Ventilator-
Associated pneumonia. Int. J. Mol. Sci. 20 (9), 2218 (2019).
 52. Ebihara, T. et al. Cytokine elevation in severe COVID-19 from longitudinal proteomics analysis: comparison with sepsis. Front. 
Immunol. 12, 798338 (2021).
 53. Wang, H. et al. Cellular hypoxia promotes heterotopic ossification by amplifying BMP signaling. J. Bone Min. Res. 31 (9), 1652–
1665 (2016).
 54. Siddiqui, J. A. et al. Pathophysiological role of growth differentiation factor 15 (GDF15) in obesity, cancer, and cachexia. Cytokine 
Growth Factor. Rev. 64, 71–83 (2022).
 55. Verhamme, F . M. et al. GDF-15 in pulmonary and critical care medicine. Am. J. Respir Cell. Mol. Biol. 60 (6), 621–628 (2019).
 56. Alserawan, L. et al. Growth differentiation factor 15 (GDF-15): a novel biomarker associated with poorer respiratory function in 
COVID-19. Diagnostics. 11 (11), 1998 (2021).
 57. Torrealba, N. et al. TGF-β/PI3K/AKT/mTOR/NF-kB pathway. Clinicopathological features in prostate cancer. Aging Male (2019).
 58. Miricescu, D. et al. PI3K/AKT/mTOR signaling pathway in breast cancer: from molecular landscape to clinical aspects. Int. J. Mol. 
Sci. 22 (1), 173 (2020).
 59. Haddadi, N. et al. PTEN/PTENP1:‘Regulating the regulator of RTK-dependent PI3K/Akt signalling’ , new targets for cancer 
therapy. Mol. Cancer. 17 (1), 1–14 (2018).
 60. Holz, M. K. et al. mTOR and S6K1 mediate assembly of the translation preinitiation complex through dynamic protein interchange 
and ordered phosphorylation events. Cell 123 (4), 569–580 (2005).
 61. Osaki, M., Oshimura, M. & Ito, H. PI3K-Akt pathway: its functions and alterations in human cancer. Apoptosis 9 (6), 667–676 
(2004).
 62. He, Y . et al. Targeting PI3K/Akt signal transduction for cancer therapy. Signal. Transduct. Target. Ther. 6 (1), 425 (2021).
 63. Du, Z. & Lovly, C. M. Mechanisms of receptor tyrosine kinase activation in cancer. Mol. Cancer. 17 (1), 58 (2018).
 64. Sudhesh Dev, S. et al. Receptor tyrosine kinases and their signaling pathways as therapeutic targets of Curcumin in cancer. Front. 
Pharmacol. 12, 772510 (2021).
 65. Nakayama, K. cAMP-response element-binding protein (CREB) and NF-κB transcription factors are activated during prolonged 
hypoxia and cooperatively regulate the induction of matrix metalloproteinase MMP1. J. Biol. Chem. 288 (31), 22584–22595 (2013).
 66. Velmurugan, K. et al. Antiapoptotic actions of exendin-4 against hypoxia and cytokines are augmented by CREB. Endocrinology 
153 (3), 1116–1128 (2012).
 67. Kufareva, I. Chemokines and their receptors: insights from molecular modeling and crystallography. Curr. Opin. Pharmacol. 30, 
27–37 (2016).
 68. Curnock, A. P ., Logan, M. K. & Ward, S. G. Chemokine signalling: Pivoting around multiple phosphoinositide 3-kinases. 
Immunology 105 (2), 125–136 (2002).
 69. Hu, X. et al. The JAK/STAT signaling pathway: from bench to clinic. Signal. Transduct. Target. Ther. 6 (1), 402 (2021).
 70. de Bruin, A. M., Voermans, C. & Nolte, M. A. Impact of interferon-gamma on hematopoiesis. Blood 124 (16), 2479–2486 (2014).
 71. Perner, F . et al. Roles of JAK2 in aging, inflammation, hematopoiesis and malignant transformation. Cells 8 (8), 854 (2019).
 72. Degryse, S. et al. JAK3 mutants transform hematopoietic cells through JAK1 activation, causing T-cell acute lymphoblastic 
leukemia in a mouse model. Blood J. Am. Soc. Hematol. 124 (20), 3092–3100 (2014).
 73. Randhawa, V . & Bagler, G. Identification of SRC as a potent drug target for asthma, using an integrative approach of protein 
interactome analysis and in Silico drug discovery. Omics: J. Integr. Biology. 16 (10), 513–526 (2012).
 74. Toumpanakis, D. et al. The role of Src & ERK1/2 kinases in inspiratory resistive breathing induced acute lung injury and 
inflammation. Respir Res. 18 (1), 209 (2017).
 75. Wu, M. et al. Effect of Src tyrosine kinase on a rat model of asthma. Exp. Ther. Med. 23 (2), 172 (2022).
 76. Anderson, G. P . & Bozinovski, s. Acquired somatic mutations in the molecular pathogenesis of COPD. 24(2), 71–76 (2003).
 77. Mascitelli, L., Pezzetta, F . & Goldstein, M. Inhibition of the renin–angiotensin system in severe COPD. Eur. Respir. J. 32 (4), 
1130–1130 (2008).
 78. Gregório, J. F . et al. Asthma: role of the angiotensin-(1‐7)/Mas (MAS1) pathway in pathophysiology and therapy. Br. J. Pharmacol. 
178 (22), 4428–4439 (2021).
 79. Southworth, T. et al. PI3K, p38 and JAK/STAT signalling in bronchial tissue from patients with asthma following allergen challenge. 
Biomark. Res. 6 (1), 14 (2018).
 80. Crosbie, P . A. et al. ERK and AKT phosphorylation status in lung cancer and emphysema using nanocapillary isoelectric focusing. 
BMJ Open. Respir Res. 3 (1), e000114 (2016).
 81. Xie, M. et al. ERK1/2 signaling pathway modulates the airway smooth muscle cell phenotype in the rat model of chronic asthma. 
Respiration 74 (6), 680–690 (2007).
 82. Sun, X., Chen, L. & He, Z. PI3K/Akt-Nrf2 and Anti-Inflammation effect of macrolides in chronic obstructive pulmonary disease. 
Curr. Drug Metab. 20 (4), 301–304 (2019).
 83. Dahlin, A. et al. The phosphatidylinositide 3-kinase (PI3K) signaling pathway is a determinant of Zileuton response in adults with 
asthma. Pharmacogenomics J. 18 (5), 665–677 (2018).
 84. Sandri, B. J. et al. Multi-omic molecular profiling of lung cancer in COPD. Eur. Respir J. 52(1) (2018).
 85. Kayyali, U. S. et al. Cytoskeletal changes in hypoxic pulmonary endothelial cells are dependent on MAPK-activated protein kinase 
MK2. J. Biol. Chem. 277 (45), 42596–42602 (2002).
 86. Bouvry, D. et al. Hypoxia-induced cytoskeleton disruption in alveolar epithelial cells. Am. J. Respir Cell. Mol. Biol. 35 (5), 519–527 
(2006).
 87. Zhang, Y . et al. RhoA/Rho-kinases in asthma: from pathogenesis to therapeutic targets. Clin. Transl Immunol. 9 (5), e01134 (2020).
 88. Ganesan, S. & Sajjan, U. S. Repair and remodeling of airway epithelium after injury in chronic obstructive pulmonary disease. Curr. 
Respir Care Rep. 2 (3), 145–154 (2013).
 89. Nagaraj, C. et al. Hypoxic vascular response and ventilation/perfusion matching in end-stage COPD May depend on p22phox. Eur. 
Respir J. 50(1) (2017).
Scientific Reports |        (2025) 15:32024 14| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/

 90. Chirino, Y . I. et al. Airborne particulate matter in vitro exposure induces cytoskeleton remodeling through activation of the 
ROCK-MYPT1-MLC pathway in A549 epithelial lung cells. Toxicol. Lett. 272, 29–37 (2017).
 91. Liu, B. et al. The level of ROCK1 and ROCK2 in patients with pulmonary hypertension in plateau area. Sci. Rep. 8 (1), 9356 (2018).
 92. van Gastel, J. et al. beta-Arrestin based receptor signaling paradigms: potential therapeutic targets for complex Age-Related 
disorders. Front. Pharmacol. 9, 1369 (2018).
 93. Gu, Y . J. et al. The emerging roles of beta-arrestins in fibrotic diseases. Acta Pharmacol. Sin. 36 (11), 1277–1287 (2015).
 94. Billington, C. K. & Penn, R. B. Signaling and regulation of G protein-coupled receptors in airway smooth muscle. Respir Res. 4 (1), 
2 (2003).
 95. Lombardi, M. S. et al. Hypoxia/ischemia modulates G protein–coupled receptor kinase 2 and β-arrestin-1 levels in the neonatal rat 
brain. Stroke 35 (4), 981–986 (2004).
 96. Bae, W . Y . et al. β-arrestin 2 stimulates degradation of HIF-1α and modulates tumor progression of glioblastoma. Cell. Death Differ. 
28 (11), 3092–3104 (2021).
 97. Gavrilovskaya, I. N., Gorbunova, E. E. & Mackow, E. R. Hypoxia induces permeability and giant cell responses of Andes virus-
infected pulmonary endothelial cells by activating the mTOR-S6K signaling pathway. J. Virol. 87 (23), 12999–13008 (2013).
Acknowledgements
We would like to acknowledge the director of DIPAS, DRDO for the smooth in-house working facility and 
permission for this contribution to the literature on publicly available scientific community. The supporting 
staffs Mr. Ram Niwas Meena, Mr. Alpesh Kumar Shrama, Ms. Arismita Paul, Ms. Sumra and Mr. Jai Ram Singh 
providing the seamless digital facility to conduct this literature study. We would also thank the HRD cell, Mr. 
Vishnu Kumar and Mr. Praveen Negi for the arrangement of documentation related to permission during the 
publication process.
Author contributions
YA conceptualized the study. SM performed the computational data retrieval, analysis and wrote the manuscript 
with the necessary tables and sketched figures for convenient representation in this article. SM and PS checked 
the language and formatting of the manuscript. YA critically evaluated the manuscript and editorial process.
Funding
SM is a recipient of DRDO-SRF fellowship and PS is a recipient of DRDO-JRF fellowship. The authors have not 
received any special funding for this work apart from this institutional financial assistance.
Declarations
Competing interests
The authors declare no competing interests.
Ethical approval
Does not involve any animal or human subjects hence not applicable.
Consent for publication
All authors agreed.
Additional information
Supplementary Information The online version contains supplementary material available at  h t t p s : / / d o i . o r g / 1 
0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 5 - 1 5 5 3 9 - y     .  
Correspondence and requests for materials should be addressed to Y .A.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in 
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide 
a link to the Creative Commons licence, and indicate if you modified the licensed material. Y ou do not have 
permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence 
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to 
obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o 
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .  
© The Author(s) 2025 
Scientific Reports |        (2025) 15:32024 15| https://doi.org/10.1038/s41598-025-15539-y
www.nature.com/scientificreports/