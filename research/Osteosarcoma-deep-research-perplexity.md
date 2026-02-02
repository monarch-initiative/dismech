---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-02-01T09:32:34.209349'
end_time: '2026-02-01T09:34:42.884634'
duration_seconds: 128.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteosarcoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 60
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Osteosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteosarcoma**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

# Comprehensive Pathophysiology of Osteosarcoma: Molecular Mechanisms, Cellular Dysfunction, and Disease Progression

Osteosarcoma (OS) represents the most common primary malignant bone tumor affecting adolescents and young adults, characterized by rapid, aggressive growth and a high propensity for early metastatic dissemination[36]. Despite significant advances in multimodal treatment approaches combining neoadjuvant chemotherapy, surgical resection, and adjuvant chemotherapy, the five-year survival rate for patients with localized disease remains approximately 65 percent, dropping dramatically to approximately 25 percent for those presenting with metastatic disease[47]. This comprehensive analysis elucidates the complex, multifactorial pathophysiology underlying osteosarcoma development, with particular emphasis on the molecular mechanisms driving tumorigenesis, disease progression, and therapeutic resistance. The disease arises from dysregulation of fundamental cellular processes including genome integrity maintenance, proliferative control, differentiation programming, metabolic adaptation, immune surveillance, and cell-cell communication within the tumor microenvironment. Understanding these interconnected mechanisms provides critical insights into potential therapeutic interventions and prognostic biomarkers.

## Genetic and Epigenetic Alterations Driving Osteosarcoma Development

### Tumor Suppressor Gene Inactivation: The Role of TP53 and RB1

The molecular foundation of osteosarcoma development centers on the inactivation of two critical tumor suppressor genes, TP53 and RB1, which regulate fundamental cellular processes including DNA damage response, cell cycle progression, and apoptosis[2][4][5]. Remarkably, whole-genome sequencing studies have demonstrated that approximately 95 percent of osteosarcomas exhibit disruption of the p53 pathway, despite the relatively low prevalence of simple point mutations in sporadic tumors[4]. This paradox has been resolved through identification of complex structural variations and chromosomal translocations that effectively inactivate TP53 function without producing detectable point mutations through conventional analysis methods. Inactivation of the tumor suppressor p53 from translocation into the first intron of the TP53 gene has been detected in 9 out of 19 patient osteosarcoma tumors examined[4]. The most frequent TP53 rearrangements identified include TP53-VAV1, TP53-EMR1, TP53-PPRAD, and TP53-KPNA3, with these fusion products resulting in functional inactivation of p53[4]. Notably, TP53-KPNA3 translocations have been specifically associated with chemotherapy resistance and metastasis[4].

The retinoblastoma pathway similarly exhibits profound dysregulation in the vast majority of osteosarcomas. RB1 mutations are detected in approximately 70 percent of all adolescent osteosarcomas[2], and patients carrying germline mutations in RB1 demonstrate approximately a 500-fold higher incidence of osteosarcoma compared to the general population[2]. At the molecular level, RB1 loss leads to aberrant spliceosome function through upregulation of E2F3a, a mediator of spliceosome gene expression[1]. Critically, while RB1 loss alone proves insufficient to establish osteosarcoma in animal models, robust synergy between TP53 and RB1 inactivation has been demonstrated in osteosarcoma development, with compound mutant mice developing osteosarcoma in 75 percent of animals and exhibiting substantially shortened lifespans compared to single mutant animals[2].

The MDM2 oncogene, which encodes a critical negative regulator of p53, exhibits amplification and overexpression in approximately 17 percent of osteosarcomas[5]. Amplification and overexpression of MDM2 can lead to increased MDM2-p53 binding, resulting in inactivation of p53 function[5]. Remarkably, MDM2 amplification occurs independently of TP53 mutations, suggesting complementary mechanisms of p53 pathway inactivation[5]. Collectively, alterations of the TP53, RB1, and MDM2 genes account for abnormalities in 62 percent of osteosarcomas examined in earlier studies[5].

### Structural Variants and Chromosomal Complexity

Recent comprehensive genomic studies have fundamentally shifted understanding of osteosarcoma genetics by revealing that **structural variations (SVs) and copy number alterations (CNAs), rather than single nucleotide variations (SNVs), represent the primary mechanism of recurrent mutations in osteosarcoma**[4]. Whole genome sequencing from the St. Jude Children's Research Hospital – Washington University Pediatric Cancer Genome Project identified high rates of structural variations and copy number alterations but notably low rates of single nucleotide variations in osteosarcoma tumors[4]. This unique mutational landscape fundamentally distinguishes osteosarcoma from many other malignancies and poses significant challenges for implementing traditional targeted mutation-based therapies.

Clonal evolution analysis of osteosarcoma patients reveals that 62 percent of patient tumors exhibit a simple linear evolutionary pattern, whereas 38 percent display branching evolutionary patterns or contain only single clone clusters[20]. Notably, linear evolutionary patterns predominate in nonmetastatic tumors, whereas metastatic tumors display no clear evolutionary trend, suggesting distinct mechanisms of progression. Among identified mutations, ATRX mutations frequently occur as early events in metastatic tumors and confer strong clonal selectivity advantages[20]. The ATRX gene encodes a chromatin remodeling protein closely related to chromatin remodeling and telomere maintenance[20]. ATRX mutations may lead to genomic instability and increased tumor cell survival, thereby strongly influencing clonal expansion associated with metastasis[20]. Furthermore, analysis of high-frequency gene mutations revealed that CNV in TP53 and ATRX were more prevalent in the metastatic group compared to nonmetastatic tumors, with patients harboring metastases at diagnosis demonstrating generally poorer prognosis[20].

### Chromoanagenesis and Catastrophic Chromosomal Rearrangements

A particularly striking feature of osteosarcoma genomics involves chromoanagenesis, encompassing chromothripsis and chromoanasynthesis, representing catastrophic chromosomal rearrangement events[38]. Chromothripsis, characterized by massive chromosomal shattering followed by random reassembly of fragmented DNA, results in complex segmental copy number alterations and is among the most striking examples of chromothripsis-driven malignancy[38]. Osteosarcoma represents one of the malignancies most profoundly driven by chromothripsis, which contributes significantly to profound genome complexity[38]. This mechanism intersperses chromothripsis patterns with segmental amplifications across multiple chromosomes, achieving biallelic TP53 inactivation and enabling tolerance to whole-genome duplication in approximately half of high-grade osteosarcomas while simultaneously amplifying multiple oncogenes through multi-generational breakage-fusion-bridge cycles[38].

The breakage-fusion-bridge cycle mechanism results from dicentric chromosomes via telomere fusions, which frequently rupture during mitosis, causing catastrophic fragmentation and chromothripsis-like rearrangements often accompanied by kataegis[38]. These mechanisms precipitate chromothriptic fragmentation of missegregated DNA within micronuclei, followed by clonal selection of survival-advantageous rearrangements, thereby underpinning the pervasive copy number alterations observed in 78 percent of certain osteosarcoma models and the oscillating genomic patterns characteristic of chromothripsis[38]. The five most frequently affected chromosomes in osteosarcoma cases with chromoanagenesis are chromosomes 12, 1, 8, 6, and 2[38].

### MYC Amplification and Cell Cycle Dysregulation

Multi-region whole-genome sequencing of pediatric osteosarcoma has revealed that **amplification of the MYC oncogene represents a major driver of childhood osteosarcoma**[45]. Reanalysis of copy number readouts from 258 cases of high-grade osteosarcoma across three different cohorts identified significant enrichment of focal MYC amplifications in children[45]. Furthermore, four additional cases of MYC and CCNE1 coamplification have been identified, representing a rare driver event warranting further investigation[45]. MYC amplification demonstrates association with inferior outcomes in survival analysis conducted on integrated datasets[45]. Although CCNE1 amplification did not correlate with adverse survival in all datasets examined, CCNE1 remains a recognized driver in multiple malignancies including osteosarcoma, having been proven to serve as an independent prognostic factor in triple-negative breast cancer and ovarian cancer[45].

MYC has been demonstrated to directly regulate CCNE1 gene expression as well as CCNE1-CDK2 complex activity[45]. Mouse models have demonstrated the cooperative action of MYC and CCNE1 in contributing to tumor formation in hepatocellular cancer and other malignancies[45]. The cyclin-dependent kinase complexes, particularly cyclin D-CDK4/6 and cyclin E-CDK2 complexes, sequentially phosphorylate retinoblastoma proteins to release restriction of the G1/S checkpoint, thereby allowing cells to enter S phase[29]. Dysregulation of these cell cycle regulatory complexes through MYC and CCNE1 amplification promotes uncontrolled cell cycle progression characteristic of osteosarcoma.

## Dysregulation of Major Signaling Pathways

### PI3K/AKT/mTOR Pathway Hyperactivation

The **PI3K/AKT/mTOR signaling pathway represents one of the most important oncogenic pathways frequently hyperactivated in osteosarcoma**[10][7]. This pathway plays a crucial role in promoting tumor cell proliferation, migration, epithelial-mesenchymal transition, inhibition of apoptosis, and increasing sensitivity to chemotherapy drugs[7]. The pathway becomes dysregulated through multiple mechanisms, with loss of the PTEN gene being a particularly common mechanism leading to overactivation of the PI3K pathway in osteosarcoma patients[7]. During activation, p-Akt promotes activation of mTORC1, which then influences cellular activities directly through its own catalytic actions[7]. Overactivation of this pathway in tumor patients occurs primarily due to dysregulation in the expression of PIK3CA and phosphatase and tensin homolog (PTEN)[7].

The PI3K/AKT/mTOR pathway has been identified as an osteosarcoma driver through sleeping beauty transposon-based forward genetic screening approaches which introduce mutations into the genome[4]. Upstream regulation of this pathway involves increased uptake of leucine and glutamine in osteosarcoma cells through upregulation of LAT2, which activates mTORC1 and subsequent c-Myc-mediated transcription of CD47, enabling evasion of innate immune mechanisms and thereby promoting metastasis[1]. Targeting this pathway through small molecule compounds represents an attractive potential therapeutic approach for osteosarcoma[10].

The interaction between the PI3K/AKT/mTOR pathway and non-coding RNAs has emerged as a critical regulatory mechanism. The long non-coding RNA DANCR binds to miR-33a-5p in a competitive manner, thereby increasing the expression of RTK AXL, which influences expression of downstream proteins in the PI3K/Akt pathway and affects various aspects of tumor cells, such as the self-renewal of cancer stem cells and EMT[7]. Similarly, the lncRNA ANRIL performs an essential function in prognostic prediction of osteosarcoma patients, with ANRIL expression in osteosarcoma tissues notably higher than in adjoining non-cancerous tissues[7]. ANRIL enhances the proliferation and invasion of osteosarcoma cells, and its knockdown appreciably induces mobile apoptosis and confirms association with negative prognosis, specifically through decreased phosphorylation levels of PI3K and Akt[7].

Multiple microRNAs regulate components of the PI3K/AKT/mTOR pathway in osteosarcoma. Downregulation of miR-384 promotes tumor growth by upregulating SLBP and activating the PI3K/Akt pathway[7]. MiR-1224-5p, which is downregulated in osteosarcoma tissues, negatively regulates the PI3K/Akt/mTOR pathway and inhibits tumor growth and EMT[7]. MiR-564, downregulated in osteosarcoma patients, directly targets Akt, inhibits its transcription and translation, and suppresses tumor cell glycolysis, thereby inhibiting cell proliferation[7]. CircRNA-NIRP1, upregulated in osteosarcoma, competitively binds to miR-532-3p to upregulate Akt3, thereby enhancing the activity of the PI3K/Akt pathway and strengthening malignancy[7].

### Wnt/β-Catenin Signaling and RUNX2 Regulation

**WNT/β-catenin signaling is over-activated in osteosarcoma and promotes tumor progression**[8][11]. Importantly, the WNT/β-catenin pathway normally activates RUNX2 gene expression during osteogenic lineage commitment, and this pathway has been demonstrated to control the tumor-related elevation of RUNX2 expression in osteosarcoma[8][11]. Analysis of protein levels and nuclear localization of β-catenin and RUNX2 in human osteosarcoma cell lines reveals that in all six examined cell lines (SAOS, MG63, U2OS, HOS, G292, and 143B), β-catenin and RUNX2 are expressed to different degrees and localized in both the nucleus and cytoplasm[8][11]. Notably, SAOS cells demonstrate the highest levels of RUNX2 protein localized in the nucleus, while MG63 cells exhibit the lowest RUNX2 levels predominantly localized in the cytoplasm[8][11].

Treatment with the GSK3β inhibitor SB216763 enhances levels of both β-catenin and RUNX2 protein in HOS, G292, and 143B cells[8][11]. Small interfering RNA-mediated depletion of β-catenin inhibits RUNX2 expression in G292 cells, demonstrating that **WNT/β-catenin activation is required for RUNX2 expression in at least some osteosarcoma cell types, where RUNX2 is known to promote expression of metastasis-related genes**[8][11]. This pathway dysregulation represents a critical mechanism by which normal developmental signals become hijacked to promote malignant progression.

### JAK-STAT Pathway and Immune Modulation

The Janus kinase-signal transducer and activator of transcription (JAK-STAT) pathway comprises seven STAT members involved in the regulation of cell proliferation, differentiation, and survival[1]. Activation of STAT1 in osteosarcoma cells suppresses epithelial-mesenchymal transition, resulting in increased apoptosis and cell cycle arrest, and decreased colony formation, cell migration, and invasion[1]. Conversely, increased expression of COL6A1 promotes STAT1 degradation, which subsequently facilitates osteosarcoma metastasis[1]. This pathway thus represents a potential therapeutic target, as enhancement of STAT1 activity could theoretically restore anti-tumor differentiation programs.

### NRF2 and Oxidative Stress Management

NRF2 regulates intracellular reactive oxygen species balance, the AMPK/mTOR autophagy signaling pathway, and the Warburg effect[1]. TRIM22 inhibits osteosarcoma progression by binding to and destabilizing NRF2 in a KEAP1-independent manner[1]. This mechanism highlights how dysregulation of oxidative stress response pathways contributes to osteosarcoma pathogenesis by allowing cells to survive under conditions that would normally trigger apoptosis.

## Molecular Pathways Driving Metastatic Progression

### Epithelial-Mesenchymal Transition and Migration

**The epithelial-mesenchymal transition (EMT) represents a vital step in osteosarcoma progression toward metastasis**[13]. This process is associated with a reduction in epithelial-like features of cancer cells and acquisition of mesenchymal-like features necessary to mediate effective invasion and migration[13]. The EMT is a common event observed in a wide range of cancer types undergoing metastasis, and several transcription factors including Twist1, Snail, and ZEB1 cooperate to control this complex process[13].

Although osteosarcoma cells arise from cells that descend from the mesenchyme, they maintain partial epithelial characteristics, including some epithelial markers necessary to mediate cohesiveness during migration and to allow resistance to mechanical stress experienced during migration[13]. Downregulation of miR-22 contributes to epithelial-mesenchymal transition in osteosarcoma, with miR-22 being downregulated in human osteosarcoma in a manner correlating with enhanced tumor progression and metastasis[13]. Overexpression of miR-22 significantly reduces cell proliferation and substantially suppresses epithelial-mesenchymal transition in osteosarcoma cells[13]. Specifically, miR-22 directly targets Twist1 to mediate repression of EMT, with miR-22 expression being negatively correlated with Twist1 expression in patient samples[13].

At the molecular level, cells overexpressing miR-22 demonstrate reduced Vimentin expression and increased E-cadherin expression, directly corresponding to significant reduction in osteosarcoma cell EMT capacity[13]. These findings highlight that **miR-22/Twist1 signaling axis represents a clinically relevant regulatory node for EMT control in osteosarcoma**, suggesting potential utility as either a prognostic biomarker or therapeutic target[13].

### HIF-1α and Hypoxic Adaptation

Hypoxia-inducible factor-1α (HIF-1α) plays an essential role in the mechanisms of osteosarcoma metastasis and has been demonstrated to facilitate rapid tumor cell adaptation to hypoxic environments, thereby contributing to metastatic processes[30]. During hypoxia, HIF-1α expression levels and stability increase, with increased HIF-1α promoting tumor vascular remodeling, epithelial-mesenchymal transformation, and osteosarcoma cell invasiveness, ultimately leading to distant metastasis[30]. Meta-analysis of nine published studies comprising 486 osteosarcoma cases demonstrated that overexpression of HIF-1α correlates with lower survival rate, higher microvessel density, metastasis, higher pathologic grade, tumor stage, and poor chemotherapy response in osteosarcoma[27].

After translocation into the nucleus, HIF-1α binds to HIF-1β, forming a transcriptional complex that binds to hypoxia response elements in the promoter regions of target genes, thereby initiating transcriptional expression of many downstream genes participating in various physiological and pathological processes[30]. HIF-1α is subject to regulation by various factors including the antisense transcription factor aHIF-1α, which exerts negative regulatory effects on transcription of the HIF-1α gene[30]. The regulation of osteosarcoma cell metastasis by HIF-1α involves multiple mechanisms including modulation of invasive and metastatic potential, promotion of EMT processes, enhancement of cellular adhesion, increase in anti-apoptotic properties, induction of immune evasion, facilitation of tumor angiogenesis, and fostering of microenvironmental remodeling[30].

Hypoxia-induced upregulation of miR-18b-5p through HIF-1α transcriptional control inhibits expression of tumor suppressor gene PHD finger protein 2 at the post-transcriptional level, with the miR-18b-5p-PHF2 signal axis involved in HIF-1α-mediated metastasis of osteosarcoma[30]. Under hypoxic conditions, expression of E-cadherin becomes upregulated, while expression of Vimentin, N-cadherin, and snail protein becomes downregulated; all these proteins serve as markers for EMT[30]. With upregulation of HIF-1α and TWIST family bHLH transcription factor 1 expression, E-cadherin expression becomes downregulated, leading to altered EMT processes in osteosarcoma cells[30].

### Vascular Endothelial Growth Factor and Angiogenesis

**VEGF expression and high vascularity within osteosarcoma correlate with poor prognosis**[9]. Studies examining the correlation between VEGF expression with tumor stage and metastasis revealed significantly positive correlation between VEGF expression and tumor stages[9]. Data further suggest higher cancer recurrence and more frequent cases of remote metastasis in high-VEGF groups compared to low-VEGF groups[9]. VEGF expression positively associates with c-fos and c-myc expressions in primary tumor sections[9]. Prior data suggested probability of lung metastasis in VEGF-negative osteosarcoma was 0.15, whereas the incidence ratio of lung metastasis in VEGF-positive osteosarcoma was 0.82[9].

Pro-angiogenic factors become up-regulated in tumors, with such up-regulation linked to poor prognosis[9]. Pro-angiogenic factors within solid tumors stimulate host vascular endothelial cell mitogenesis and possibly chemotaxis. Multiple pro-angiogenic factors have been identified including basic fibroblast growth factor, platelet-derived growth factor, transforming growth factor beta-1, transforming growth factor alpha, and epidermal growth factor[9]. VEGF represents the best characterized pro-angiogenic factor, being relatively unique among growth factors in its specificity for the vascular endothelium[9]. Not only does VEGF function as a diffusible endothelium-specific mitogen and angiogenic factor, it also increases vascular permeability and stimulates maintenance of neovascularization in various tumor types[9].

## Metabolic Reprogramming in Osteosarcoma

### Aerobic Glycolysis and the Warburg Effect

Tumor cells undergo profound metabolic reprogramming to meet their energy and anabolic demands necessary for maintaining their malignant phenotype. **Aerobic glycolysis, also known as the Warburg effect, supports biosynthesis and metabolic processes necessary for osteosarcoma growth and metastasis**[1]. Key enzymes involved in this process, such as PGC1α, PKM2, ALDOA, and LDHA, can directly influence tumor progression and metastasis[1]. For instance, miR-23b-3p downregulates PGC1α and promotes a metabolic shift from oxidative phosphorylation to glycolysis, supporting osteosarcoma progression[1]. This metabolic reprogramming enables rapid ATP generation necessary to support the elevated biosynthetic and proliferative demands of malignant cells.

Metabolic reprogramming in tumor cells mainly involves the glycolytic pathway, pentose phosphate pathway, serine synthesis pathway, enhanced glutamine metabolism or fatty acid anabolism, and abnormal mitochondrial oxidative phosphorylation[31][34]. The tricarboxylic acid cycle represents the central pathway of mitochondrial oxidative phosphorylation, with glucose, amino acid, and fatty acid metabolism all associated with the TCA cycle[31][34]. Genetic alterations in tumor cells, including those involving p53 and other oncogenic and tumor suppressive pathways, promote metabolic reprogramming directly or indirectly by regulating enzymatic activities associated with metabolic pathways[31][34].

### Glutamine Metabolism and GLS-1 Inhibition

Highly metastatic osteosarcoma cell lines require glutamine for proliferation, and conversely, glutaminase-1 (GLS-1) inhibition limits metastatic progression in osteosarcoma[1]. This finding identifies glutamine metabolism as a critical dependency of metastatic osteosarcoma cells. Glutamine serves as both an energy source through the TCA cycle and a biosynthetic precursor for nucleotide and amino acid synthesis, making it particularly critical for rapidly proliferating cancer cells. The dependence on glutamine metabolism in metastatic osteosarcoma versus primary tumors suggests that the metastatic phenotype becomes increasingly dependent on specific metabolic pathways that might represent therapeutic vulnerabilities.

### RNA Modifications and Gene Expression Control

RNA modifications, particularly m6A methylation, play critical roles in osteosarcoma metastasis through regulation of mRNA stability and protein expression. The m6A demethylase FTO mediates mRNA demethylation, promoting decay of KLF3 mRNA and decreasing its expression, consequently facilitating osteosarcoma proliferation and metastasis[1]. Additionally, the destabilizing effects of FTO on DACT1 mRNA promote Wnt signaling and consequently osteosarcoma metastasis[1]. ALKBH5-mediated m6A methylation upregulates expression of USP22 and RNF40, subsequently inhibiting ubiquitination of histone H2A and promoting osteosarcoma growth and metastasis[1]. Upregulation of TRIM7 due to loss of m6A RNA modifications has been reported to promote osteosarcoma metastasis and chemoresistance by inducing ubiquitination of BRMS1[1].

## Cellular Origins and Cancer Stem Cell Biology

### Mesenchymal Stem Cell Versus Osteoblast Origin Hypotheses

There exist two primary competing hypotheses regarding the cellular origin of osteosarcoma, the mesenchymal stem cell (MSC) origin hypothesis and the osteoblast origin hypothesis[3][4]. The MSC hypothesis proposes that a mutation-carrying MSC will give rise to osteosarcoma[4]. A high frequency of pathogenic variants in the TP53 and RB1 tumor suppressor genes and the c-MYC and RAS oncogenes is found in genomic studies of human osteosarcoma[4]. However, mounting evidence increasingly places cells that undergo osteoblast commitment rather than immature MSCs as the most likely cell-of-origin for osteosarcoma[6].

During osteogenic differentiation, depletion of Trp53 or both Trp53 and Rb1 in murine bone marrow-derived MSCs, but notably not in adipose-derived MSCs, induces formation of osteosarcoma-like tumors[4]. This observation suggests that osteoblasts rather than MSCs represent the cells of origin of osteosarcoma. Supporting this notion, RUNX2 and WNT signaling pathways, essential for osteogenic differentiation, have been found disrupted in human osteosarcoma samples, demonstrating loss of RUNX2 transcriptional activity and nuclear accumulation of β-Catenin, thus indicating that osteosarcoma development might entail differentiation defects[4].

**When comparing cells-of-origin directly, P53/RB-disrupted immature MSC and osteoblast committed cells all proved capable of initiating OS formation, though at varying incidence levels**[6]. This finding demonstrates that all types of cells along the osteogenic lineage possessed capacity to initiate osteosarcoma formation, with findings influenced by certain microenvironment signals[6]. Importantly, the level of osteoblastic differentiation of tumors did not correlate with the degree of differentiation of the cell-of-origin, suggesting that epigenetic dedifferentiation mechanisms could be active in mature osteoblasts during osteosarcomagenesis[6].

Evidence of undifferentiated MSC as cell-of-origin for osteosarcoma derives from introduction of other oncogenic events into undifferentiated bone marrow MSCs, such as expression of C-MYC in a P16INK4A−/− P19ARF−/− genetic background or aneuploidization accompanied by loss of the INKA locus, resulting in osteosarcoma development[6]. Nevertheless, accumulated evidence most strongly supports concepts that **osteosarcoma development is initiated by different cell types along the mesenchymal-osteogenic lineage targeted with relevant oncogenic lesions, like inactivation of tumor suppressor genes P53 and RB, and becomes highly influenced by bone microenvironment signals**[6].

### Cancer Stem Cell Characteristics and Maintenance

Experimental evidence supports the notion that sarcomas are hierarchically organized and sustained by a subpopulation of self-renewing cells that can generate the full repertoire of tumor cells and display tumor reinitiating properties[6]. CSC subpopulations emerge after accumulation of further epigenetic and genetic alterations in a cell within the aberrant population initially generated by the cell-of-origin[6]. Hypothesis to explain resistance of osteosarcoma to chemotherapy involves existence of drug-resistant cancer stem cells with progenitor properties responsible for tumor relapses and metastasis[6]. These subpopulations of CSCs commonly emerge during tumor evolution from the cell-of-origin, which represents the normal cells acquiring the first cancer-promoting mutations to initiate tumor formation[6].

CD133 and C-X-C chemokine receptor type 4 (CXCR4) represent frequently applied markers for cancer stem cells in osteosarcoma patients[14]. mRNA of stemness genes such as octamer-binding transcription factor 4 (Oct-4) and NANOG, as well as the metastasis-related receptor CXCR4, are highly expressed in CD133+ osteosarcoma cells[14]. CD133 expression serves as an independent prognostic factor associated with lung metastasis and poor prognosis of osteosarcoma patients[14]. Concomitant expression of CSC markers CD133/CXCR4 might represent a novel marker for predicting poor prognosis in osteosarcoma patients, with CD133 and CXCR4 potentially serving as therapeutic targets[14].

## Tumor Microenvironment and Immune Evasion

### Tumor-Associated Macrophages and Immune Suppression

Tumor-associated macrophages (TAMs) represent the most prevalent immune cells in the tumor microenvironment[15][18]. In osteosarcoma, TAMs may constitute over 50 percent of immune cells, significantly influencing tumor initiation, progression, metastasis, immunosuppression, and drug resistance[18]. Both circulating monocytes and tissue-resident macrophages contribute to accumulation of TAMs, with secreted chemokines from tumor cells and stromal cells, such as macrophage colony-stimulating factor (M-CSF) and C-C motif ligand 2 (CCL-2), inducing and recruiting monocytes to the tumor microenvironment[15]. Notably, TAMs were recruited by interleukin-34 (IL-34) released from osteosarcoma cells, with IL-34 released by osteosarcoma cells promoting recruitment of M2-TAMs into tumor tissue to promote tumor growth and metastasis[15][18].

The osteosarcoma tumor microenvironment exhibits extensive macrophage infiltration, predominantly myeloid CD163+ cells, potentially facilitating tumor immune evasion[18]. M2-related cytokines, chemokines, and cell markers are overexpressed in pulmonary osteosarcoma metastasis[18]. M2 macrophages become enriched in primary osteosarcoma tissue, activating tumor stem cells and inducing drug resistance[18]. TAMs modulate local immunity, angiogenesis, and malignant cell migration, primarily promoting tumor growth by facilitating macrophage polarization toward anti-inflammatory phenotype and enhancing immune infiltration[18].

Metastatic osteosarcoma cells display a more malignant phenotype via exosomal communication with macrophages, with these exosomes significantly increasing M2 macrophage-related cytokines such as IL10 and transforming growth factor-beta 2, thereby modulating macrophages toward tumor-promoting M2 phenotype[15]. This conversion contributes to inhibition of macrophage-mediated tumor surveillance and promotion of immunosuppression within the microenvironment[15]. Infiltrating CD68+ cells were elevated in tumor tissues of osteosarcoma patients poorly reactive to neoadjuvant chemotherapy, with macrophages secreting IL-1β after chemotherapy treatment, activating downstream cancer signaling pathways and reducing sensitivity of osteosarcoma to chemotherapeutic drugs[15].

### T Cell Dysfunction and Checkpoint Exhaustion

The osteosarcoma tumor microenvironment features an inhibitory immune microenvironment with higher numbers of TIM-3+ PD-1+ T cells compared to peripheral blood[18]. This specific immune suppression of TIM-3+ PD-1+ T cells becomes amplified by M2 TAMs[18]. T cell activation plays pivotal roles in tumor immune response through two pathways: interaction between T cell receptor and major histocompatibility complex presenting antigens, and binding of co-stimulatory transmembrane receptor CD28 on T cells to its ligands CD80/86[39]. Tumor-infiltrating lymphocytes predominantly localize in areas expressing human leukocyte antigen class I, whereas CD4+ and CD8+ T cells concentrate at the interface of lung metastases[39].

### Natural Killer Cell Suppression

In the osteosarcoma microenvironment, NK cells become suppressed, with TGF-β expression elevated[39]. TGF-β plays pivotal role in diminishing natural killer cell-mediated killing, with tumor-derived TGF-β downregulating activation receptor expression such as NKG2D on NK cells, impairing their ability to recognize and kill osteosarcoma cells[42]. Furthermore, osteosarcoma cells frequently shed soluble ligands for NKG2D, further inhibiting NK cell-mediated cytotoxicity[42]. Infiltration of NK cells in osteosarcoma demonstrates association with gender, with male patients possessing 71 percent more NK cells compared to female patients[18]. The underlying mechanism involves TGF-β promoting angiogenesis, bone remodeling, and cell migration by suppressing expression of activated receptor NKG2D and decreasing release of NK cell-killing perforin[18].

### Regulatory T Cells and Myeloid-Derived Suppressor Cells

Regulatory T cells (Tregs) play dual-edged role in osteosarcoma pathogenesis, not only assisting tumor cells in evading immune surveillance but also playing key role in promoting tumor angiogenesis[18][39]. Within the osteosarcoma microenvironment, Tregs operate through various mechanisms, secreting immunosuppressive cytokines including IL-10, IL-35, and TGF-β to hinder activity of effector T cells and suppress osteoclast formation via direct cell contact-dependent means[18][39]. Myeloid-derived suppressor cells (MDSCs) inhibit T cell proliferation, diminish T cell-mediated immune responses, and promote T cell apoptosis by depleting L-arginine and generating reactive oxygen species within the microenvironment[18]. Additionally, MDSCs suppress functionality of NK cells and dendritic cells[18]. Furthermore, under hypoxic microenvironment stimuli, MDSCs facilitate angiogenesis and establishment of pre-metastatic niches, closely linked to osteosarcoma metastasis[18].

### Osteoclasts and Bone Remodeling

Loss of osteoclasts contributes to development of osteosarcoma metastasis, with ablation of osteoclasts with zoledronic acid increasing number of metastatic lung lesions in orthotopic osteosarcoma models, whereas fulvestrant treatment increases osteoclast numbers and reduces metastatic lesions[40]. Tartrate-resistant acid phosphatase (ACP5/TRAP) is significantly downregulated in osteosarcoma compared with nonmalignant bone, with lesions from osteosarcoma patients with pulmonary metastases demonstrating 2-fold less ACP5/TRAP expression than lesions from patients without metastases[40]. Mature bone-resorbing osteoclasts secrete several enzymes including tartrate-resistant acid phosphatase 5, considered the classic marker for bone resorption and osteoclast differentiation[40]. Metastatic osteosarcoma cells prove significantly more migratory in presence of bone marrow factors than nonmetastatic cells, with osteoclasts secreting factors that significantly reduce migration of metastatic osteosarcoma cells[40].

## Disease Progression, Metastasis, and Clinical Manifestations

### Staging and Prognostic Factors

Osteosarcoma tumors are classified based on whether they are localized in one place or metastatic, meaning they have spread to other parts of the body[33]. **Low-grade, localized tumors represent stage I osteosarcoma; high-grade, localized tumors represent stage II; and metastatic tumors (regardless of grade) represent stage III**[33]. The Musculoskeletal Tumor Society (MSTS) staging system, also known as the Enneking system, bases staging on three key pieces of information: tumor grade (G), extent of primary tumor (T) classified as either intracompartmental or extracompartmental, and presence of metastasis (M)[33].

Site of main tumor influences prognosis significantly, with tumors arising from bones of arms or legs often demonstrating better outlook than those in pelvis or spine[33]. Size of main tumor affects prognosis as well, with smaller tumors proving easier to surgically remove than larger tumors[33]. Histological characteristics significantly influence outcome, with high-grade tumors demonstrating high cell-to-matrix ratio, poor differentiation, and malignant cytologic characteristics including degree of pleomorphism, mitotic index, lymphovascular invasion, amount of necrosis, and invasiveness[56]. Grade I and grade II osteosarcomas demonstrate significantly better prognosis than grade III osteosarcomas[56].

### Clinical Presentation and Diagnostic Approaches

Most common presenting symptom of osteosarcoma represents bone pain, initially with activity then at rest[54]. Pain and swelling at local site, usually at growing ends of an extremity or long bones, constitute most common presenting symptoms[51]. Around 10 percent of patients present with pathological fractures due to primary tumors or bony metastases[51]. Systemic symptoms seen in other malignancies remain rare[51]. Respiratory symptoms indicating extensive lung involvement remain uncommon[51]. Physical examination findings typically focus on primary tumor location, including palpable tender mass, decreased range of motion of adjacent joint with possible effusion, pain on weight-bearing or inability to bear weight, and local or regional lymphadenopathy[51].

Diagnosis of osteosarcoma requires multidisciplinary approach integrating clinical evaluation, imaging, and laboratory testing[36]. Radiographs of conventional osteosarcoma usually demonstrate medullary and cortical bone destruction with mixed lytic and blastic appearance, with high-grade osteosarcoma often described as demonstrating permeative or "moth-eaten" appearance with "sunburst" configuration due to aggressive periostitis or "Codman triangle" configuration due to elevation of periosteum away from bone[51]. MRI is utilized to assess local invasion, while CT and bone scans help evaluate metastatic spread[36]. Elevated alkaline phosphatase levels support diagnosis by indicating increased bone turnover[36]. Definitive diagnosis requires biopsy and histopathological analysis, with staging subsequently determined based on tumor size, metastatic involvement, and histological grade to guide treatment planning[36].

### Metastatic Disease and Lymph Node Involvement

Approximately 10 to 20 percent of osteosarcoma patients present with metastases, primarily to the lungs[51]. The lung metastases, representing the primary target of metastasis in osteosarcoma, demonstrate five-year survival rates of approximately 30 percent[57]. In extrapulmonary metastatic osteosarcoma, patients with lymph node metastases demonstrate worse clinical outcomes, with five-year survival rates of only 10 percent[57]. However, only 3 percent of osteosarcoma patients are diagnosed with lymph node metastasis, leading to lack of adequate clinical data for exploring lymph node involvement in osteosarcoma[57].

Osteosarcoma lymphatic metastasis demonstrates significant association with distant metastasis, with osteosarcoma lymphatic metastasis being significantly associated with poor prognosis[57]. Osteosarcoma metastases, typically secondary to hematogenous dissemination, represent secondary events of profound prognostic significance[57]. Due to lack of lymphatic drainage in normal cortical and spongy bone, lymph node metastasis remains rare in bone sarcomas[57]. Regional lymph node involvement in osteosarcoma may result from infiltration of enlarged tumor parenchyma into periphery, such as joint capsule or synovium, leading to dissemination into lymphatic system[57].

## Therapeutic Resistance and Chemotherapy Escape

### Mechanisms of Drug Resistance

Osteosarcoma remains difficult to treat, with standard chemotherapy regimen having not improved survival for past three decades, with resistance to chemotherapy remaining major clinical challenge[44]. Multiple molecular mechanisms contribute to chemoresistance in osteosarcoma, including decreased intracellular accumulation of drugs, inactivation of drugs, improved DNA repair, modulations of signaling pathways, resistance linked to autophagy, disruption in genes expression linked to cell cycle, and implications of microenvironment[22].

Impaired drug transport represents one described resistance mechanism to chemotherapy in osteosarcoma, particularly due to decreased transporters on tumor cell surfaces[22]. Increased drug efflux has been reported as partly responsible for osteosarcoma resistance, with cancer cells exposed to one chemotherapy agent developing resistance to many other anticancer drugs, called multidrug resistance[22]. This acquired resistance results mainly from overexpression of members of ATP-binding cassette family of efflux transporters[22]. P-glycoprotein associates with cytoskeleton linker named ezrin, with complex located in plasma membrane lipid rafts, and multidrug resistance in osteosarcoma cell lines could result from this cytoskeleton linker, with ezrin inhibition increasing drug sensitivity and ezrin expression associating with poor outcomes[22].

Alterations in structure or expression of target enzyme can explain resistance of some chemotherapeutic agents through increased levels of target enzymes or decreased drug affinity due to mutations[22]. MTX-resistant osteosarcoma cell lines exhibit high expression of DHFR, with relationship demonstrated between high DHFR expression in xenografts and emergence of resistance[22]. Osteosarcoma cells treated with DOX or CDP exhibit upregulation of GSTP1 expression, with GSTP1 expression inducible by chemotherapeutic agents leading to resistance of tumor cells[22]. GSTP1 overexpression was associated with failure of preoperative chemotherapy, suggesting that overexpression associates with chemotherapy failure[22].

### Autophagy-Mediated Survival and Drug Resistance

Autophagy demonstrates dual role in osteosarcoma, potentially promoting cell survival by protecting malignant cells from unfavorable conditions while also serving as tumor suppressor by impairing malignant transformation and promoting malignant cell death[44]. Activation of PI3K/AKT/mTOR signaling pathway inhibits autophagy in osteosarcoma, with use of rapamycin, an mTOR inhibitor, inducing autophagy and increasing cell death in osteosarcoma cells[44]. HMGB1-mediated autophagy induction leads to chemotherapy resistance, with inhibition of both HMGB1 and autophagy leading to increased drug sensitivity[44].

The dual role of autophagy proves context-dependent, with different osteosarcoma cell lines and treatments demonstrating distinct autophagy-outcome relationships[44]. Treatment of murine osteosarcoma cell lines with camptothecin induced autophagy, but autophagy inhibition decreased CPT-induced cell death in one line while increasing it in another[44]. Similarly, treatment of human osteosarcoma cell lines with gemcitabine induced autophagy, with autophagy inhibition increasing cell death in certain lines while increasing survival in others[44]. This duality proves not species-specific, with effects observed in mouse and human cells alike[44].

### miRNA-Mediated Chemoresistance Regulation

MiR-26a expression declines in chemoresistant osteosarcoma after neoadjuvant chemotherapy, with expression correlating with clinical outcome[19]. Compared with sensitive parental cells, miR-26a expression also declines in osteosarcoma multidrug-resistant cells[19]. Enforced expression of miR-26a reverses multidrug resistance in osteosarcoma cells, while miR-26a knockdown confers multidrug resistance in chemosensitive osteosarcoma cells treated with doxorubicin, methotrexate, or cisplatin[19]. MiR-26a reverses resistance to doxorubicin in osteosarcoma multidrug-resistant cells xenografted in nude mice[19]. The critical mechanism by which miR-26a negatively regulates multidrug resistance in osteosarcoma involves targeting and suppressing MCL1 expression, with restored MCL1 expression substantially recovering chemoresistance caused by miR-26a enforcement[19].

## Conclusion: Integrating Pathophysiology into Therapeutic Development

Osteosarcoma represents a complex, heterogeneous malignancy driven by multifactorial dysregulation of fundamental cellular processes encompassing genome integrity, proliferative control, differentiation programming, metabolic adaptation, immune surveillance, and microenvironmental interactions. The disease arises from inactivation of critical tumor suppressors TP53 and RB1, often accompanied by structural chromosomal variations, copy number alterations, and catastrophic rearrangement events including chromothripsis. These genetic alterations initiate transformation in cells along the osteogenic lineage under influence of specific microenvironmental signals, generating cancer stem cell populations responsible for metastatic dissemination and therapeutic resistance. Dysregulation of major signaling pathways including PI3K/AKT/mTOR, Wnt/β-catenin, and HIF-1α drive proliferation, migration, and angiogenesis. Metabolic reprogramming enables aggressive tumor growth through Warburg effect activation and glutamine dependency. The tumor microenvironment becomes extensively infiltrated with immunosuppressive cell populations including macrophages, regulatory T cells, and myeloid-derived suppressor cells, facilitating immune evasion. Multiple mechanisms of chemotherapy resistance emerge through drug transport alterations, enhanced DNA repair, autophagy-mediated survival, and microRNA-regulated pathway dysregulation.

Future therapeutic strategies must address this complex pathophysiology through multiple complementary approaches. Direct targeting of dysregulated signaling pathways through small molecule inhibitors and biologics shows promise, particularly approaches targeting PI3K/AKT/mTOR and immune checkpoints. Restoration of p53 function through MDM2 inhibitors or synthetic lethality approaches exploiting DNA repair deficiencies represents another avenue. Metabolic therapy targeting glutamine metabolism and glycolysis offers additional possibilities. Immunotherapeutic approaches using checkpoint blockade combined with strategies to convert immunosuppressive macrophages toward anti-tumor phenotypes show emerging potential. Patient-derived preclinical models integrating comprehensive genomic profiling and functional testing will increasingly enable discovery of tumor-specific vulnerabilities. Continued investigation of the interactions between genetic alterations, signaling dysregulation, metabolic transformation, and microenvironmental influence will ultimately drive development of personalized, multimodal therapeutic strategies improving outcomes for this aggressive malignancy affecting adolescents and young adults.