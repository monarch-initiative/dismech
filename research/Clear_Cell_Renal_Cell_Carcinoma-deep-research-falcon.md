---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-24T13:31:14.612361'
end_time: '2026-01-24T13:37:38.901613'
duration_seconds: 384.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Clear Cell Renal Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Clear Cell Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Clear Cell Renal Cell Carcinoma**.
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Clear Cell Renal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Clear Cell Renal Cell Carcinoma**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Clear Cell Renal Cell Carcinoma (ccRCC)
- MONDO ID: 
- Category: Malignant neoplasm of kidney, epithelial; clear cell subtype

Pathophysiology description (narrative)
Clear cell renal cell carcinoma is driven in the vast majority of cases by loss of the VHL tumor suppressor on chromosome 3p, which prevents pVHL-mediated ubiquitination and proteasomal degradation of HIF-1α and HIF-2α. Stabilized HIFs drive transcriptional programs for angiogenesis (VEGF/PDGF), erythropoiesis (EPO), pH regulation (CA9), glucose metabolism, and cell survival, producing a highly vascular and immunomodulatory tumor microenvironment. HIF-2α (EPAS1) is the predominant oncogenic driver in VHL-deficient ccRCC and has become a direct therapeutic target. Early truncal 3p loss co-deletes or predisposes to loss-of-function mutations in chromatin remodeling/tumor suppressor genes PBRM1, SETD2, and BAP1, which reshape chromatin, RNA processing, DNA repair, and immune–metabolic states to promote progression and metastatic competence (cotta2023currentlandscapeof pages 3-4, liu2025clinicalsignificanceof pages 18-22, liu2025clinicalsignificanceof pages 61-64).

A defining feature of ccRCC is metabolic reprogramming that supports growth in hypoxia and contributes to immune evasion. This includes a Warburg-like shift to aerobic glycolysis with suppressed mitochondrial oxidative metabolism and reduced mitochondrial biogenesis; enhanced glutamine utilization for anaplerosis and biosynthesis; and lipid/cholesterol accumulation with abundant lipid droplets. These changes are closely linked to HIF signaling and other nutrient-sensing pathways (for example, mTOR) and produce therapeutic opportunities in metabolism. RCC overall has been termed a metabolic disease, with pathogenesis tied to oxygen- and nutrient-sensing pathways and TCA-cycle enzymes; although some of these alterations are most characteristic of non-clear cell subtypes, the paradigm of metabolic rewiring is central in ccRCC (coffey2024metabolicalterationsin pages 1-3, cotta2023currentlandscapeof pages 3-4, pezzicoli2023genomicprofilingand pages 8-10).

The tumor microenvironment of ccRCC is highly vascular, hypoxic, and immune-infiltrated, with enrichment of immunosuppressive myeloid populations and exhausted T-cell states. Hypoxia-induced signaling and alternative angiogenic pathways contribute to resistance to VEGF-directed therapy, while immune checkpoints (PD-1/PD-L1, CTLA-4) are associated with poor prognosis. Single-cell and transcriptomic studies (summarized in recent reviews) link specific metastatic or resistant tumor states with distinct immune compositions, supporting personalized combinations of VEGF-TKIs and ICIs (abah2024innovativetherapiestargeting pages 2-4, pezzicoli2023genomicprofilingand pages 8-10).

Translationally, direct blockade of HIF-2α is now a validated strategy. In a first-in-human study of a tumor-targeted siRNA against HIF-2α (ARO-HIF2), objective response rate was 7.7% with disease control in 38.5%; on-target pharmacodynamic effects included variable HIF-2α downregulation in biopsies and rapid suppression of tumor-produced EPO in a patient with paraneoplastic polycythemia, although neurotoxicity limited further development (Clinical Cancer Research, 2024; doi:10.1158/1078-0432.ccr-23-3029) (liu2025clinicalsignificanceof pages 18-22). Together with evidence of HIF-2α oncogenic primacy, these data underpin the clinical development and deployment of HIF-2α–targeted agents and rational combinations in ccRCC (liu2025clinicalsignificanceof pages 18-22, cotta2023currentlandscapeof pages 3-4).

Recent developments and latest research (prioritized 2023–2024)
- Genomic landscape and prognostic associations: VHL is the most frequently mutated gene (≈49–82% across cohorts), with common recurrent mutations in PBRM1 (≈29–41%), SETD2 (≈8–30%), BAP1 (≈6–19%), and KDM5C (≈4–15%). BAP1-mutant tumors have markedly worse outcomes (for example, OS ≈4.6 years for BAP1-mutant vs ≈10.6 years for PBRM1-mutant tumors), while PBRM1 alterations show signals for benefit with PD-1 blockade (e.g., enrichment among nivolumab responders and improved outcomes in CheckMate 025 exploratory analyses) (European Urology, 2023; doi:10.1016/j.eururo.2023.04.003) (cotta2023currentlandscapeof pages 3-4).
- Copy-number landscape: Near-universal loss of 3p (~95%), with additional frequent events including 5q gain (~69%), 14q loss (>42%), 9p loss (~29%), 8p deletion (~32%), and 7q gains (>20%); these alterations correlate with aggressiveness and therapeutic resistance mechanisms (Int J Mol Sci, 2024; doi:10.3390/ijms26010265) (abah2024innovativetherapiestargeting pages 2-4).
- Tumor mutational burden (TMB) and ICI response: ccRCC has low average TMB (~1.1 mutations/Mb) yet responds to ICIs, possibly due to frameshift indels increasing neoantigenicity; higher TMB in a subset can associate with improved survival on ICI-based therapy (Current Oncology, 2023; doi:10.3390/curroncol30100670) (pezzicoli2023genomicprofilingand pages 8-10).
- Metabolic reprogramming and therapeutic implications: Authoritative synthesis in 2024 (Nature Reviews Nephrology; doi:10.1038/s41581-023-00800-2) details glycolytic shift, suppressed glucose oxidation, mitochondrial downregulation, glutamine dependency, and lipid/cholesterol remodeling in RCC, supporting trials of metabolic agents and combinations (coffey2024metabolicalterationsin pages 1-3).
- HIF-2α targeting: Proof-of-concept siRNA study (ARO-HIF2) in 2024 demonstrated tumor-targeted HIF-2α downregulation with on-target effects, an ORR of 7.7%, and DCR of 38.5% in heavily pre-treated ccRCC (Clinical Cancer Research, Apr 2024; doi:10.1158/1078-0432.ccr-23-3029) (liu2025clinicalsignificanceof pages 18-22).

Current applications and real-world implementations
- VEGF-TKIs and ICIs remain standard backbones; genomic features such as PBRM1, BAP1, and SETD2 status influence prognosis and may modulate ICI benefit signals, though no single gene is yet an established predictive biomarker in routine care (European Urology, 2023; doi:10.1016/j.eururo.2023.04.003) (cotta2023currentlandscapeof pages 3-4).
- HIF-2α inhibition strategies are clinically actionable in VHL-driven disease and under investigation in sporadic ccRCC. Tumor-directed HIF-2α siRNA demonstrated biological activity, providing mechanistic validation for HIF-2α as a target and a reference for safety/PD considerations in ongoing trials of small-molecule HIF-2α inhibitors and combinations (Clinical Cancer Research, 2024; doi:10.1158/1078-0432.ccr-23-3029) (liu2025clinicalsignificanceof pages 18-22).

Expert opinions and authoritative analyses
- European Urology 2023 scoping review: genomic biomarkers in ccRCC—emphasizes VHL as foundational, recurrent chromatin-modifying genes (PBRM1/SETD2/BAP1) as key modulators with prognostic value, and the complexity of identifying robust predictive biomarkers; highlights exploratory associations with ICI responsiveness (doi:10.1016/j.eururo.2023.04.003) (cotta2023currentlandscapeof pages 3-4).
- Nature Reviews Nephrology 2024: positions RCC as a metabolic disease and synthesizes oxygen- and nutrient-sensing pathways with TCA-cycle derangements and systemic metabolic states, framing a roadmap for translational metabolism-focused therapies (doi:10.1038/s41581-023-00800-2) (coffey2024metabolicalterationsin pages 1-3).

Relevant statistics and data from recent studies
- Mutation frequencies: VHL 49–82%; PBRM1 29–41%; SETD2 8–30%; BAP1 6–19%; KDM5C 4–15% (European Urology, 2023; doi:10.1016/j.eururo.2023.04.003) (cotta2023currentlandscapeof pages 3-4).
- Prognostic impact: BAP1 mutations associated with substantially worse OS (≈4.6 years) compared with PBRM1-mutated tumors (≈10.6 years); hazard ratios for cancer-specific survival elevated in BAP1-mutant cohorts (European Urology, 2023; doi:10.1016/j.eururo.2023.04.003) (cotta2023currentlandscapeof pages 3-4).
- Copy-number alterations: loss 3p ~95%, gain 5q ~69%, loss 14q >42%, loss 9p ~29%, del 8p ~32%, gains 7q >20% (Int J Mol Sci, 2024; doi:10.3390/ijms26010265) (abah2024innovativetherapiestargeting pages 2-4).
- TMB: ~1.1 mutations/Mb on average with clinically meaningful responses to ICIs; higher TMB subsets may fare better (Current Oncology, 2023; doi:10.3390/curroncol30100670) (pezzicoli2023genomicprofilingand pages 8-10).
- HIF-2α siRNA (ARO-HIF2) Phase 1: ORR 7.7%; DCR 38.5%; notable PD biomarker effect—“rapid suppression of tumor produced erythropoietin (EPO) in a patient with paraneoplastic polycythemia” (Clinical Cancer Research, Apr 2024; doi:10.1158/1078-0432.ccr-23-3029) (quote) (liu2025clinicalsignificanceof pages 18-22).

Core Pathophysiology
- Primary mechanisms: VHL loss → HIF-1α/HIF-2α stabilization; activation of pro-angiogenic (VEGF/PDGF), erythropoietic (EPO), and metabolic (glycolysis, lipid handling) programs; epigenetic/chromatin remodeling via PBRM1/SETD2/BAP1 mutations; additional nutrient/energy-sensing pathway input (mTOR) (cotta2023currentlandscapeof pages 3-4, coffey2024metabolicalterationsin pages 1-3, pezzicoli2023genomicprofilingand pages 8-10).
- Dysregulated pathways: Hypoxia signaling; angiogenesis; glycolysis; glutamine metabolism; lipid/cholesterol metabolism; mTOR signaling; chromatin remodeling (coffey2024metabolicalterationsin pages 1-3, cotta2023currentlandscapeof pages 3-4, pezzicoli2023genomicprofilingand pages 8-10).
- Affected cellular processes: Ubiquitin-mediated proteolysis (VHL–HIF axis); mitochondrial biogenesis/function (downregulated); epigenetic regulation of transcription and RNA processing; endothelial activation/aberrant vasculogenesis; immune checkpoint signaling and myeloid/T-cell dysfunction (coffey2024metabolicalterationsin pages 1-3, cotta2023currentlandscapeof pages 3-4, abah2024innovativetherapiestargeting pages 2-4).

Key Molecular Players
- Genes/Proteins (HGNC): VHL, EPAS1 (HIF-2α), HIF1A (HIF-1α), PBRM1, SETD2, BAP1, MTOR (cotta2023currentlandscapeof pages 3-4, coffey2024metabolicalterationsin pages 1-3, pezzicoli2023genomicprofilingand pages 8-10).
- Chemical entities (CHEBI): glucose, lactate, glutamine, fatty acids, cholesterol (coffey2024metabolicalterationsin pages 1-3, cotta2023currentlandscapeof pages 3-4).
- Cell types (CL): proximal tubule epithelial cell (putative cell-of-origin), tumor-associated macrophages, regulatory T cells, cancer-associated fibroblasts/myofibroblasts; highly vascular endothelial compartments (abah2024innovativetherapiestargeting pages 2-4, cotta2023currentlandscapeof pages 3-4).
- Anatomical locations (UBERON): kidney cortex; proximal tubule; tumor vasculature (cotta2023currentlandscapeof pages 3-4).

Biological Processes (GO terms, disrupted)
- Response to hypoxia; angiogenesis; glycolytic process; glutamine metabolic process; lipid droplet biogenesis/organization; mTOR signaling; chromatin remodeling (coffey2024metabolicalterationsin pages 1-3, cotta2023currentlandscapeof pages 3-4, pezzicoli2023genomicprofilingand pages 8-10).

Cellular Components (GO)
- Nucleus (HIF target transcription; chromatin remodeling); mitochondrion (suppressed OXPHOS, reduced content); lipid droplet (abundant storage of neutral lipids); extracellular space/vasculature (VEGF-rich, abnormal vessels) (coffey2024metabolicalterationsin pages 1-3, cotta2023currentlandscapeof pages 3-4).

Disease Progression (sequence of events)
- Initiation: Proximal tubule lineage accrues 3p loss with VHL inactivation → HIF stabilization and pseudohypoxic signaling (cotta2023currentlandscapeof pages 3-4).
- Early progression: Additional truncal/branch mutations in chromatin modifiers (PBRM1, SETD2, BAP1) drive epigenetic dysregulation, transcriptional reprogramming, and metabolic shifts (cotta2023currentlandscapeof pages 3-4, coffey2024metabolicalterationsin pages 1-3).
- Microenvironmental remodeling: VEGF-driven angiogenesis yields a highly vascular, hypoxic TME; immune infiltration with T-cell dysfunction/exhaustion and suppressive myeloid cells supports immune escape; metabolic byproducts (e.g., lactate) reinforce immunosuppression (abah2024innovativetherapiestargeting pages 2-4, coffey2024metabolicalterationsin pages 1-3).
- Metastatic dissemination: Copy-number imbalances (e.g., 14q, 9p losses) and chromatin/immune–metabolic adaptations contribute to invasion and organotropism; clinical series show diverse patterns, with pancreas a notable site in selected indolent phenotypes (e.g., PBRM1-high, lower 9p/14q losses) (abah2024innovativetherapiestargeting pages 2-4, pezzicoli2023genomicprofilingand pages 8-10).

Phenotypic Manifestations (clinical/HP terms)
- Classic features: Hypervascular renal mass; potential paraneoplastic syndromes including polycythemia due to tumor-derived EPO (HP:0001907). Direct clinical evidence of EPO-driven erythrocytosis and its rapid suppression with HIF-2α targeting was observed in a ccRCC patient on ARO-HIF2 (Clinical Cancer Research, 2024; doi:10.1158/1078-0432.ccr-23-3029) (liu2025clinicalsignificanceof pages 18-22).
- Systemic phenotype of immune–metabolic disease: weight loss, anemia, and immune dysfunction are common in advanced disease; low average TMB yet ICI responsiveness (pezzicoli2023genomicprofilingand pages 8-10).

Ontology-mapped annotations
| Category | Term | Ontology (namespace) | Role in ccRCC (1–2 sentences) | Key recent source(s) (DOI/URL, year) |
|---|---|---|---|---|
| Gene/Protein | VHL | HGNC:VHL | Tumor suppressor; loss/inactivation prevents pVHL-mediated ubiquitination of HIF-α, causing constitutive HIF activation and downstream angiogenic/metabolic programs. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Gene/Protein | HIF1A (HIF-1α) | HGNC:HIF1A | Hypoxia-responsive transcription factor; drives glycolysis and some hypoxic adaptive programs; role can be context-dependent in ccRCC. | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Gene/Protein | EPAS1 (HIF-2α) | HGNC:EPAS1 | Principal oncogenic HIF isoform in VHL-deficient ccRCC that drives angiogenesis, EPO production, lipid metabolism and tumor growth; therapeutic target (HIF-2α inhibitors). | https://doi.org/10.1016/j.eururo.2023.04.003 (2023), https://doi.org/10.1016/j.ccr-23-3029 (2024) (cotta2023currentlandscapeof pages 3-4, liu2025clinicalsignificanceof pages 18-22) |
| Gene/Protein | PBRM1 | HGNC:PBRM1 | Chromatin remodeler (PBAF subunit); frequent truncal mutation after 3p loss, affects transcriptional programs, immunity and therapy response. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Gene/Protein | BAP1 | HGNC:BAP1 | Deubiquitinase involved in chromatin regulation; mutations associate with higher grade, aggressive disease and worse survival. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Gene/Protein | SETD2 | HGNC:SETD2 | H3K36 trimethyltransferase; loss perturbs epigenetic regulation, RNA processing and promotes genomic instability and metabolic changes. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023), https://doi.org/10.1038/s41581-023-00800-2 (2024) (cotta2023currentlandscapeof pages 3-4, coffey2024metabolicalterationsin pages 1-3) |
| Gene/Protein | MTOR | HGNC:MTOR | Central nutrient-sensing kinase; mTOR pathway dysregulation contributes to growth, metabolic reprogramming and is a therapeutic node in ccRCC. | https://doi.org/10.3390/curroncol30100670 (2023) (pezzicoli2023genomicprofilingand pages 8-10) |
| Biological Process | Response to hypoxia | GO:BP (response to hypoxia) | HIF-mediated transcriptional program that upregulates VEGF, glycolysis, EPO and survival pathways driving angiogenesis and metabolic shifts. | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Biological Process | Angiogenesis | GO:BP (angiogenesis) | HIF-driven VEGF/PDGF expression produces highly vascular tumors; central to ccRCC phenotype and targets of VEGF-TKIs. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Biological Process | Glycolytic process | GO:BP (glycolytic process) | Warburg-like shift (increased glycolysis, reduced TCA flux) in VHL/HIF-driven tumors supports proliferation and hypoxic survival. | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Biological Process | Glutamine metabolic process | GO:BP (glutamine metabolic process) | Increased glutamine utilization (anaplerosis) supports biosynthesis and redox balance; potential therapeutic target (glutaminase inhibitors). | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Biological Process | Lipid droplet biogenesis | GO:BP (lipid droplet organization/biogenesis) | ccRCC shows lipid/cholesterol accumulation and droplet formation linked to HIF signaling and altered FA metabolism. | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Biological Process | mTOR signaling | GO:BP (mTOR signaling pathway) | Integrates nutrient/growth signals with metabolism and protein synthesis; altered in subsets of ccRCC and targetable by mTOR inhibitors. | https://doi.org/10.3390/curroncol30100670 (2023) (pezzicoli2023genomicprofilingand pages 8-10) |
| Biological Process | Chromatin remodeling | GO:BP (chromatin remodeling) | Mutations in PBRM1/SETD2/BAP1 remodel epigenome, affecting transcription, DNA repair and tumor progression. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Cellular Component | Nucleus | GO:CC (nucleus) | Location of HIF-dependent transcriptional activity and many chromatin remodeling processes altered in ccRCC. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Cellular Component | Mitochondrion | GO:CC (mitochondrion) | Mitochondrial content/function is reduced in VHL-deficient ccRCC; OXPHOS downregulation contributes to metabolic rewiring. | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Cellular Component | Lipid droplet | GO:CC (lipid droplet) | Sites of stored neutral lipids; abundant in ccRCC and linked to altered FA synthesis/oxidation and ferroptosis susceptibility. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Cellular Component | Extracellular space / Vasculature | GO:CC (extracellular region / blood vessel) | Tumor-secreted VEGF and altered stroma produce abnormal vasculature that shapes TME and drug delivery. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Cell Type | Proximal tubule epithelial cell | CL:proximal tubule epithelial cell | Putative cell of origin for ccRCC; VHL loss in proximal tubule lineage initiates tumorigenesis. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023), https://doi.org/10.1186/s12967-024-04848-x (2024) (cotta2023currentlandscapeof pages 3-4, abah2024innovativetherapiestargeting pages 2-4) |
| Cell Type | Endothelial tip cell | CL:endothelial tip cell | Tumor-associated endothelial phenotypes (tip-like) drive pathological angiogenesis in ccRCC (single-cell evidence). | https://doi.org/10.1038/s42003-024-06478-x (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Cell Type | Tumor-associated macrophage (TAM) | CL:macrophage (tumor-associated) | Immunosuppressive myeloid cells abundant in TME; engage in metabolic crosstalk and limit anti-tumor immunity. | https://doi.org/10.3389/fgene.2023.1207233 (2023) (abah2024innovativetherapiestargeting pages 2-4) |
| Cell Type | Regulatory T cell (Treg) | CL:regulatory T cell | Enriched/exhausted T-cell states (including suppressive Tregs) correlate with immune escape and worse prognosis in subsets. | https://doi.org/10.1186/s12967-024-04848-x (2024) (abah2024innovativetherapiestargeting pages 2-4) |
| Cell Type | Cancer-associated fibroblast / Myofibroblast | CL:cancer-associated fibroblast | CAFs/myofibroblasts modulate ECM, support invasion, angiogenesis and metabolic niches within ccRCC TME. | https://doi.org/10.1007/s12672-024-01175-x (2024) (abah2024innovativetherapiestargeting pages 2-4) |
| Anatomy | Kidney cortex | UBERON:0001225 (kidney cortex) | Primary anatomical site where proximal tubule cells reside and ccRCC arises. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Anatomy | Proximal tubule | UBERON:0002111 (proximal tubule) | Tissue of origin implicated by lineage and molecular studies; tumor architecture often reflects proximal tubule programs. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Anatomy | Tumor vasculature | UBERON:(vasculature) | Highly vascular tumor bed shaped by VEGF-driven angiogenesis; influences therapy (VEGF-TKIs) and hypoxia niches. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Chemical | Glucose | CHEBI:17234 (glucose) | Primary carbon source with increased uptake and glycolytic flux in ccRCC (aerobic glycolysis). | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Chemical | Lactate | CHEBI:24996 (lactate) | Glycolytic end-product that shapes TME immunosuppression and metabolic crosstalk (lactate shuttling). | https://doi.org/10.1186/s12967-024-04848-x (2024) (abah2024innovativetherapiestargeting pages 2-4) |
| Chemical | Glutamine | CHEBI:61657 (glutamine) | Anaplerotic substrate supporting TCA/ biosynthesis in glutamine-dependent ccRCC subtypes; targetable (GLS inhibitors). | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |
| Chemical | Fatty acids | CHEBI:16716 (fatty acid) | Altered FA synthesis/oxidation contributes to lipid droplet accumulation and tumor growth; links to ferroptosis sensitivity. | https://doi.org/10.1038/s41581-023-00800-2 (2024) (coffey2024metabolicalterationsin pages 1-3) |
| Chemical | Cholesterol | CHEBI:16113 (cholesterol) | Dysregulated cholesterol handling and ester accumulation are features of ccRCC metabolic phenotype. | https://doi.org/10.1016/j.eururo.2023.04.003 (2023) (cotta2023currentlandscapeof pages 3-4) |


*Table: Concise mapping of key genes, processes, components, cell types, anatomical sites and chemicals relevant to clear cell renal cell carcinoma (ccRCC) with ontology namespaces and recent 2023–2024 sources for use in knowledgebase annotation.*

Evidence items (with PMIDs/DOIs/URLs)
- Cotta BH et al. Current Landscape of Genomic Biomarkers in Clear Cell Renal Cell Carcinoma. European Urology. Aug 2023. doi:10.1016/j.eururo.2023.04.003; URL: https://doi.org/10.1016/j.eururo.2023.04.003 (cotta2023currentlandscapeof pages 3-4).
- Coffey NJ, Simon MC. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nat Rev Nephrol. Jan 2024. doi:10.1038/s41581-023-00800-2; URL: https://doi.org/10.1038/s41581-023-00800-2 (coffey2024metabolicalterationsin pages 1-3).
- Abah MO et al. Innovative Therapies Targeting Drug-Resistant Biomarkers in Metastatic ccRCC. Int J Mol Sci. Dec 2024. doi:10.3390/ijms26010265; URL: https://doi.org/10.3390/ijms26010265 (abah2024innovativetherapiestargeting pages 2-4).
- Pezzicoli G et al. Genomic Profiling and Molecular Characterization of ccRCC. Current Oncology. Oct 2023. doi:10.3390/curroncol30100670; URL: https://doi.org/10.3390/curroncol30100670 (pezzicoli2023genomicprofilingand pages 8-10).
- Brugarolas J et al. A First-in-Human Phase 1 Study of a Tumor-Directed RNA-Interference Drug against HIF2α in Advanced ccRCC. Clin Cancer Res. Apr 2024. doi:10.1158/1078-0432.ccr-23-3029; URL: https://doi.org/10.1158/1078-0432.ccr-23-3029 (liu2025clinicalsignificanceof pages 18-22).
- Liu P. Clinical significance of recurrently mutated genes in RCC: VHL wild-type tumors. 2025. (mechanistic synthesis on VHL/HIF and metabolic shifts) (liu2025clinicalsignificanceof pages 61-64, liu2025clinicalsignificanceofa pages 61-64).
- Li L et al. The Role of the PAX Genes in RCC. Int J Mol Sci. Jun 2024. doi:10.3390/ijms25126730; URL: https://doi.org/10.3390/ijms25126730 (li2024theroleof pages 7-9).

Citations for key claims are provided inline: genomic drivers and prognostic associations (cotta2023currentlandscapeof pages 3-4); metabolic hallmarks and therapeutic implications (coffey2024metabolicalterationsin pages 1-3, pezzicoli2023genomicprofilingand pages 8-10); copy-number landscape and resistance context (abah2024innovativetherapiestargeting pages 2-4); HIF-2α translational targeting and paraneoplastic EPO suppression (liu2025clinicalsignificanceof pages 18-22); overarching mechanistic framework of VHL–HIF and metabolic reprogramming (liu2025clinicalsignificanceof pages 61-64, liu2025clinicalsignificanceofa pages 61-64).


References

1. (cotta2023currentlandscapeof pages 3-4): Brittney H. Cotta, Toni K. Choueiri, Marcin Cieslik, Pooja Ghatalia, Rohit Mehra, Todd M. Morgan, Ganesh S. Palapattu, Brian Shuch, Ulka Vaishampayan, Eliezer Van Allen, A. Ari Hakimi, and Simpa S. Salami. Current landscape of genomic biomarkers in clear cell renal cell carcinoma. European Urology, 84:166-175, Aug 2023. URL: https://doi.org/10.1016/j.eururo.2023.04.003, doi:10.1016/j.eururo.2023.04.003. This article has 73 citations and is from a highest quality peer-reviewed journal.

2. (liu2025clinicalsignificanceof pages 18-22): P Liu. Clinical significance of recurrently mutated genes in renal cell carcinoma: a closer look at vhl wild-type tumors. Unknown journal, 2025.

3. (liu2025clinicalsignificanceof pages 61-64): P Liu. Clinical significance of recurrently mutated genes in renal cell carcinoma: a closer look at vhl wild-type tumors. Unknown journal, 2025.

4. (coffey2024metabolicalterationsin pages 1-3): Nathan J. Coffey and M. Celeste Simon. Metabolic alterations in hereditary and sporadic renal cell carcinoma. Nature reviews. Nephrology, 20:233-250, Jan 2024. URL: https://doi.org/10.1038/s41581-023-00800-2, doi:10.1038/s41581-023-00800-2. This article has 36 citations.

5. (pezzicoli2023genomicprofilingand pages 8-10): Gaetano Pezzicoli, Federica Ciciriello, Vittoria Musci, Francesco Salonne, Anna Ragno, and Mimma Rizzo. Genomic profiling and molecular characterization of clear cell renal cell carcinoma. Current Oncology, 30:9276-9290, Oct 2023. URL: https://doi.org/10.3390/curroncol30100670, doi:10.3390/curroncol30100670. This article has 17 citations and is from a poor quality or predatory journal.

6. (abah2024innovativetherapiestargeting pages 2-4): Moses Owoicho Abah, Deborah Oganya Ogenyi, Angelina V. Zhilenkova, Freddy Elad Essogmo, Yvan Sinclair Ngaha Tchawe, Ikenna Kingsley Uchendu, Akaye Madu Pascal, Natalia M. Nikitina, Alexander S. Rusanov, Varvara D. Sanikovich, Yuliya N. Pirogova, Alexander Boroda, Aleksandra V. Moiseeva, and Marina I. Sekacheva. Innovative therapies targeting drug-resistant biomarkers in metastatic clear cell renal cell carcinoma (ccrcc). International Journal of Molecular Sciences, 26:265, Dec 2024. URL: https://doi.org/10.3390/ijms26010265, doi:10.3390/ijms26010265. This article has 6 citations and is from a poor quality or predatory journal.

7. (liu2025clinicalsignificanceofa pages 61-64): P Liu. Clinical significance of recurrently mutated genes in renal cell carcinoma: a closer look at vhl wild-type tumors. Unknown journal, 2025.

8. (li2024theroleof pages 7-9): Lei Li, Sultana Mehbuba Hossain, and Michael R. Eccles. The role of the pax genes in renal cell carcinoma. International Journal of Molecular Sciences, 25:6730, Jun 2024. URL: https://doi.org/10.3390/ijms25126730, doi:10.3390/ijms25126730. This article has 7 citations and is from a poor quality or predatory journal.