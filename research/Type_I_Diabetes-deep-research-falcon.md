---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T10:10:14.278165'
end_time: '2025-12-15T10:17:21.072234'
duration_seconds: 426.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Type I Diabetes
  mondo_id: ''
  category: Metabolic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Type I Diabetes
- **MONDO ID:**  (if available)
- **Category:** Metabolic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Type I Diabetes**.
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
- **Disease Name:** Type I Diabetes
- **MONDO ID:**  (if available)
- **Category:** Metabolic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Type I Diabetes**.
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


Plan (concise)
- Define scope per template and prioritize 2023–2024 evidence (completed). (No citation)
- Retrieve and synthesize recent immunology, interferon/beta-cell stress, genetics, staging, screening, and implementation data; extract quotes (completed). (No citation)
- Map entities to ontologies and assemble artifacts (completed). (No citation)
- Write comprehensive, citation-rich report and submit (completed). (No citation)

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Type 1 Diabetes (T1D)
- MONDO ID: MONDO_0005147
- Category: Metabolic (immune-mediated endocrine disease)

Pathophysiology description (current understanding)
Type 1 diabetes is an immune-mediated disease in which T cells destroy insulin-producing pancreatic β-cells, with other islet cell types relatively preserved, and autoantibodies serve as population-level markers of islet autoimmunity and risk. “T1D is characterized as an autoimmune disease in which T cells destroy β-cells while other islet cell types are relatively preserved. Autoantibodies (insulin, GAD65, IA-2, ZnT8) are population-level markers predicting dysglycemia” (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 2-3). Core genetic risk is dominated by HLA class II, with additional non-HLA loci contributing to immune regulation and β-cell susceptibility (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3, michels2025challengesandopportunities pages 3-4). Interferon signaling is a central driver of β-cell intrinsic responses: type I and II interferons upregulate antigen presentation and chemokines in β-cells, while downregulating oxidative phosphorylation, thereby increasing immunogenicity amid metabolic stress (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7). The natural history spans silent autoimmunity (stage 1), dysglycemia (stage 2), and symptomatic hyperglycemia (stage 3) (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02; URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (herold2024theimmunologyof pages 1-3, michels2025challengesandopportunities pages 1-2).

Core pathophysiology
- Autoimmunity: Autoreactive CD8+ and CD4+ T cells mediate β-cell killing, supported by B-cell antigen presentation and autoantibodies. The recent approval of a T-cell–targeting therapy that delays clinical disease underscores the central role of T cells (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3). 
- Interferon-driven β-cell intrinsic programs: “Our data identified IFN-α and IFN-γ as key drivers of the beta cell inflammatory response,” inducing HLA class I, HLA-E, PD-L1, and CXCL10, with enriched IFN signaling and antigen processing/presentation pathways and downregulated oxidative phosphorylation (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7).
- Cytokine and stress signaling: Synergy of interferons with cytokines (e.g., IL‑1β) promotes β-cell dysfunction and death via ER stress and apoptosis; an interferon-induced gene signature precedes autoantibody seroconversion (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 3-4).
- Genetics and antigen presentation: HLA-DR/DQ haplotypes confer dominant risk/protection; non-HLA loci (INS, PTPN22, CTLA4, IL2RA, TYK2, IFIH1, BACH2) implicate adaptive immunity, tolerance, and interferon pathways (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02; URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (herold2024theimmunologyof pages 3-4, michels2025challengesandopportunities pages 3-4).

Key molecular players
- Genes/Proteins (HGNC): HLA class II (HLA-DRB1/DQA1/DQB1), INS, PTPN22, IL2RA (CD25), TYK2, IFIH1 (MDA5), CTLA4, BACH2. Herold et al. summarize “strong HLA class II associations” and non-HLA loci including “PTPN22, CTLA4 and IL2RA” and interferon pathway gene TYK2 (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3). The Endocrine Society statement emphasizes HLA risk and protection (e.g., DQB1*06:02) and >75 GWAS loci across immune and β-cell pathways (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 3-4).
- Cell types (CL): CD8+ T cells (primary effectors), CD4+ T cells (Th1/Th17 help), B cells (antigen presentation/autoantibodies), regulatory T cells (FOXP3+; tolerance), dendritic cells and macrophages (antigen handling/cytokines), β-cells (targets that also present antigen), NK/neutrophils contribute early innate responses (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 3-4, herold2024theimmunologyof pages 1-3). Role of B cells as APCs and autoantibody sources is reviewed (URL: https://doi.org/10.1101/cshperspect.a041593; 2024-08) ().
- Chemical entities (CHEBI): Insulin; cytokines IL‑1β, IFN‑α/γ; chemokine CXCL10. Interferons induce PD‑L1, HLA‑ABC/E and CXCL10 (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7).
- Anatomical locations (UBERON): Pancreatic islets within pancreas; pancreas-draining lymph nodes and spleen orchestrate priming/expansion of autoreactive lymphocytes (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 2-3).

Biological processes (GO) and cellular components (GO-CC)
- Disrupted processes: type I interferon signaling; antigen processing and presentation via MHC I; cytokine-mediated signaling; chemokine production (e.g., CXCL10); unfolded protein response (ER stress); apoptosis; oxidative phosphorylation (downregulated in β-cells under IFNs) (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7). 
- Cellular components: MHC class I complex and plasma membrane (antigen display/immune checkpoints); endoplasmic reticulum (UPR); mitochondrion (OXPHOS); secretory granules (insulin) (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7).

Ontology mapping summary
| Category | Entity (preferred label) | Ontology | Example terms | Notes (mechanistic role) |
|---|---|---|---|---|
| Gene / Protein | HLA class II (HLA-DR / HLA-DQ) | HGNC / HLA | HLA-DRB1, HLA-DQA1, HLA-DQB1 | Primary genetic risk locus shaping peptide presentation to CD4+ T cells and influencing tolerance. |
| Gene / Protein | INS | HGNC | INS | Insulin gene; VNTR/INS expression influences central/peripheral tolerance to insulin. |
| Gene / Protein | PTPN22 | HGNC | PTPN22 | Tyrosine phosphatase that negatively regulates TCR signaling; risk alleles alter T cell activation thresholds. |
| Gene / Protein | IL2RA (CD25) | HGNC | IL2RA | IL-2 receptor alpha chain; modulates regulatory T cell (Treg) fitness and homeostasis. |
| Gene / Protein | TYK2 | HGNC | TYK2 | Janus-family kinase in type I IFN/JAK signaling; variants affect interferon responses and beta-cell sensitivity. |
| Gene / Protein | IFIH1 (MDA5) | HGNC | IFIH1 | Cytosolic viral RNA sensor implicated in antiviral signaling and linkage to autoimmune risk. |
| Gene / Protein | CTLA4 | HGNC | CTLA4 | Immune-checkpoint receptor that limits T cell activation and promotes tolerance. |
| Gene / Protein | BACH2 | HGNC | BACH2 | Transcriptional regulator controlling immune-cell differentiation and tolerance maintenance. |
| Biological Process | Type I interferon signaling pathway | GO (BP) | IFN-α signaling, STAT/IRF activation | Drives beta-cell antiviral programs and upregulates antigen-presentation/chemokine genes. |
| Biological Process | Antigen processing & presentation via MHC class I | GO (BP) | HLA-ABC peptide display | Enables beta-cell peptide presentation to CD8+ cytotoxic T cells. |
| Biological Process | Cytokine-mediated signaling | GO (BP) | IL-1β, IFN-γ, TNFα pathways | Inflammatory cytokines induce beta-cell stress, chemokine release and immune recruitment. |
| Biological Process | Unfolded protein response (ER stress) | GO (BP) | PERK / IRE1 / ATF6 UPR branches | Beta-cell ER stress contributes to dysfunction, altered identity, and apoptosis under inflammation. |
| Biological Process | Apoptosis | GO (BP) | Caspase-mediated cell death | Programmed beta-cell death downstream of immune attack and unresolved stress. |
| Biological Process | Oxidative phosphorylation (downregulated) | GO (BP) | Mitochondrial respiration / OXPHOS | Downregulation linked to metabolic dysfunction of beta cells during inflammatory states. |
| Biological Process | Chemokine production (e.g., CXCL10) | GO (BP) | CXCL10, CCL5 | Chemokines recruit autoreactive T and innate cells to islets. |
| Cellular Component | MHC class I complex | GO (CC) | HLA-A/B/C on plasma membrane | Surface peptide display platform for CD8+ T cell recognition of beta cells. |
| Cellular Component | Plasma membrane | GO (CC) | Cytokine receptors, PD-L1 | Site of cytokine receptor signaling and immune–cell interactions. |
| Cellular Component | Endoplasmic reticulum | GO (CC) | ER lumen, chaperones | Site of proinsulin folding and UPR activation in beta cells. |
| Cellular Component | Mitochondrion | GO (CC) | OXPHOS complexes | Cellular energy metabolism affected during inflammatory stress. |
| Cellular Component | Secretory granule | GO (CC) | Insulin granules | Storage and regulated secretion site for insulin peptide. |
| Cell Type | CD8+ T cell | CL | Cytotoxic T lymphocyte | Principal effector mediating antigen-specific killing of beta cells. |
| Cell Type | CD4+ T cell | CL | Helper T cell (Th1/Th17) | Provide help for autoreactive responses and coordinate inflammation. |
| Cell Type | B cell | CL | Naive / memory B cell, plasma cell | Produce islet autoantibodies and act as antigen-presenting cells. |
| Cell Type | Regulatory T cell (Treg) | CL | FOXP3+ Treg | Maintain peripheral tolerance; impaired function/number linked to autoimmunity. |
| Cell Type | Dendritic cell | CL | Conventional DC | Prime and present islet antigens to naive/autoreactive T cells. |
| Cell Type | Macrophage | CL | Islet-resident macrophage | Source of cytokines/ROS and contributors to local inflammation and antigen handling. |
| Cell Type | Pancreatic beta cell | CL | Insulin-producing β cell | Target of autoimmune attack and active participant via IFN responses and antigen presentation. |
| Cell Type | Pancreatic ductal cell | CL | Ductal epithelial cell | May amplify islet inflammation through proinflammatory signaling and immune recruitment. |
| Anatomy | Pancreas | UBERON | Pancreas organ | Organ containing islets (site of autoimmune destruction). |
| Anatomy | Pancreatic islet | UBERON | Islet of Langerhans | Micro-organ housing β cells and site of insulitis. |
| Anatomy | Pancreas-draining lymph node | UBERON | pLN | Lymphoid site for priming and expansion of autoreactive lymphocytes. |
| Anatomy | Spleen | UBERON | Spleen | Secondary lymphoid organ involved in systemic immune responses. |
| Phenotype | Hyperglycemia | HP | Elevated blood glucose | Clinical consequence of insufficient insulin secretion. |
| Phenotype | Polyuria | HP | Excessive urination | Symptom resulting from osmotic diuresis. |
| Phenotype | Polydipsia | HP | Excessive thirst | Compensatory response to fluid loss. |
| Phenotype | Weight loss | HP | Unintended weight loss | Catabolic consequence of insulin deficiency. |
| Phenotype | Diabetic ketoacidosis (DKA) | HP | DKA | Acute life‑threatening metabolic decompensation at presentation. |
| Chemical | Insulin | CHEBI | Therapeutic insulin peptide | Hormone deficient in T1D; replaced therapeutically. |
| Chemical | Glucose | CHEBI | Blood glucose | Metabolite measured for diagnosis and staging. |
| Chemical | Interferon-alpha (IFN-α) | CHEBI | Type I interferon | Drives antiviral/antigen-presentation programs in beta cells. |
| Chemical | Interleukin-1 beta (IL-1β) | CHEBI | Proinflammatory cytokine | Contributes to beta-cell stress, UPR activation and dysfunction. |


*Table: Compact mapping of genes, processes, cell types, anatomical sites, phenotypes and chemicals relevant to T1D pathophysiology; entries synthesize current mechanistic roles from recent reviews (e.g., Herold et al. 2024; de Brachène et al. 2024; Michels et al. 2025) to support ontology annotation and knowledge‑base curation (herold2024theimmunologyof pages 3-4, brachene2024interferonsarekey pages 4-7, michels2025challengesandopportunities pages 1-2).*

Disease progression and staging
- Staging: Stage 1—≥2 islet autoantibodies with normoglycemia; Stage 2—≥2 autoantibodies with dysglycemia; Stage 3—clinical diabetes with hyperglycemia. “Stage 1 = ≥2 autoantibodies with normal glucose tolerance; stage 2 = multiple autoantibodies plus dysglycemia…; stage 3 = hyperglycemia with autoimmunity” (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 1-2). 
- Natural history and risk: Stage 1 has ~35–50% 5–6-year progression risk; stage 2 has ~75% risk with median ~2 years to diagnosis (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3).
- Heterogeneity: Rates of C‑peptide decline, patterns of insulitis, and B‑cell infiltration vary by age and genotype; β-cells are active participants in pathogenesis (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 2-3, michels2025challengesandopportunities pages 3-4).

Phenotypic manifestations (HP terms)
- Hyperglycemia with polyuria, polydipsia, weight loss; frequent presentation with diabetic ketoacidosis (DKA), especially in youth; lifelong insulin dependence (URL: https://doi.org/10.1186/s42269-024-01197-z; 2024-04) (addissouky2024type1diabetes pages 1-2).

Recent developments, implementations, and expert perspectives (2023–2024 focus)
- Teplizumab (anti-CD3): FDA‑approved to delay stage 3 onset; delays progression by approximately 2–3 years in stage 2, confirming pathogenic role of T cells (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 2-3). “The first immune-targeted drug for type 1 diabetes (T1D), teplizumab, received regulatory approval by the US FDA in 2022,” and immune mechanisms are emphasized for therapy (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3).
- Coxsackie B vaccine PRV-101: Phase I randomized, placebo-controlled trial showed the multivalent CVB vaccine was well tolerated and “induced dose-dependent neutralising antibody responses against all five CVB serotypes… Protective titres ≥8 against all five serotypes were seen in >90% of participants” (URL: https://doi.org/10.1007/s00125-024-06092-w; 2024-02) (). This supports further clinical development of primary prevention strategies targeting suspected viral triggers.
- Interferons in islets: Comprehensive 2024 Diabetologia analysis identifies IFN‑α/γ as “key drivers of the beta cell inflammatory response,” expanding β-cell immunogenicity via HLA upregulation and chemokine induction, while suppressing OXPHOS (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7).
- Screening and precision diagnostics: Systematic review concluded “current evidence most strongly supports the application of autoantibody features to more precisely define T1D before diagnosis,” endorsing staging by number/type/affinity and interactions with age/genetics (URL: https://doi.org/10.1038/s43856-024-00478-y; 2024-04) ().

Statistics and epidemiology
- Global burden: “Global burden in 2021 was estimated at 8.4 million people with ~510,000 new cases” (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3).
- Incidence and heterogeneity: Geographic and ethnic variation are substantial; pediatric incidence ranges widely (URL: https://doi.org/10.1186/s42269-024-01197-z; 2024-04) (addissouky2024type1diabetes pages 1-2).
- SARS‑CoV‑2 and T1D risk severity: Two large Nordic registry cohorts found “no significant increase in type 1 diabetes after documented infections” and no consistent association with vaccination; no “break in time-trends” for severity metrics at diagnosis 2016–2023 (URL: https://doi.org/10.1101/2024.07.03.24309894; 2024-07) (aamodt2025thepathophysiologypresentation pages 2-4). A Portuguese registry study similarly found no overall significant increase in T1D cases during the pandemic nor changes in DKA/HbA1c at diagnosis across centers (URL: https://doi.org/10.1186/s12902-024-01667-5; 2024-08) ().

Evidence items (selected quotes supporting mechanistic claims)
- “IFNα and IFNγ… [are] key drivers of the beta cell inflammatory response… [inducing] HLA‑ABC, CXCL10, PDL1, HLA‑E… [and] IFN signalling and antigen processing and presentation” (URL: https://doi.org/10.1007/s00125-024-06106-7; 2024-02) (brachene2024interferonsarekey pages 4-7).
- “The first immune-targeted drug for type 1 diabetes (T1D), teplizumab, received regulatory approval by the US FDA in 2022” (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 1-3). 
- “Stage 1 = ≥2 autoantibodies…; stage 2 = multiple autoantibodies plus dysglycemia…; stage 3 = hyperglycemia with autoimmunity” (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 1-2).
- PRV‑101 “induced dose-dependent neutralising antibody responses against all five CVB serotypes… Protective titres ≥8… in >90%” (URL: https://doi.org/10.1007/s00125-024-06092-w; 2024-02) ().

Knowledge gaps and expert perspectives
- Heterogeneity/endotypes across genetics, autoimmunity, and β‑cell biology necessitate stage-tailored and combination approaches; improved biomarkers and collaborative, human-focused research are priorities (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 2-3, michels2025challengesandopportunities pages 3-4).
- Environmental triggers: Enteroviruses remain leading candidates; antiviral activity in new-onset disease has been reported, motivating vaccine and antiviral trials (URL: https://doi.org/10.1038/s41577-023-00985-4; 2024-02) (herold2024theimmunologyof pages 3-4). 

Structured annotations for knowledge-base curation
- Genes/Proteins (HGNC): HLA-DRB1/DQA1/DQB1; INS; PTPN22; IL2RA; TYK2; IFIH1; CTLA4; BACH2 (herold2024theimmunologyof pages 1-3, michels2025challengesandopportunities pages 3-4, herold2024theimmunologyof pages 3-4).
- Biological Processes (GO): type I interferon signaling; antigen processing/presentation (MHC I); cytokine-mediated signaling; UPR/ER stress; apoptosis; chemokine production; oxidative phosphorylation (downregulated) (brachene2024interferonsarekey pages 4-7).
- Cellular Components (GO-CC): MHC class I complex; plasma membrane; endoplasmic reticulum; mitochondrion; secretory granule (brachene2024interferonsarekey pages 4-7).
- Cell types (CL): CD8+ T cell; CD4+ T cell; B cell; regulatory T cell; dendritic cell; macrophage; β-cell (herold2024theimmunologyof pages 3-4).
- Anatomy (UBERON): pancreas; pancreatic islet; pancreas-draining lymph node; spleen (michels2025challengesandopportunities pages 2-3).
- Phenotypes (HP): hyperglycemia; polyuria; polydipsia; weight loss; DKA (addissouky2024type1diabetes pages 1-2).
- Chemical entities (CHEBI): insulin; glucose; interferon‑α; interleukin‑1β; chemokine CXCL10 (brachene2024interferonsarekey pages 4-7, addissouky2024type1diabetes pages 1-2).

Current applications and real-world implementations
- Disease modification: Teplizumab implementation in stage 2 (screen‑detected multiple autoantibodies), with delay of progression by ~2–3 years and ongoing efforts to broaden immunomodulator portfolios (URL: https://doi.org/10.1210/clinem/dgaf267; 2025-07) (michels2025challengesandopportunities pages 2-3).
- Screening: Precision use of islet autoantibody number, type, order of appearance, and titer for staging and risk stratification; guidelines and standardization are emphasized (URL: https://doi.org/10.1038/s43856-024-00478-y; 2024-04) ().
- Primary prevention research: CVB vaccination (PRV‑101) shows safety and immunogenicity as a step toward pathogen-targeted prevention (URL: https://doi.org/10.1007/s00125-024-06092-w; 2024-02) ().

References (URLs and dates)
- Herold KC et al. The Immunology of type 1 diabetes. Nat Rev Immunol. 2024-02. URL: https://doi.org/10.1038/s41577-023-00985-4 (herold2024theimmunologyof pages 3-4, herold2024theimmunologyof pages 1-3).
- de Brachène AC et al. Interferons are key cytokines acting on pancreatic islets in T1D. Diabetologia. 2024-02. URL: https://doi.org/10.1007/s00125-024-06106-7 (brachene2024interferonsarekey pages 4-7).
- Michels AW et al. Endocrine Society Scientific Statement. J Clin Endocrinol Metab. 2025-07. URL: https://doi.org/10.1210/clinem/dgaf267 (michels2025challengesandopportunities pages 2-3, michels2025challengesandopportunities pages 3-4, michels2025challengesandopportunities pages 1-2).
- Felton JL et al. Islet autoantibodies as precision diagnostic tools… Communications Medicine. 2024-04. URL: https://doi.org/10.1038/s43856-024-00478-y ().
- Hyöty H et al. PRV‑101 CVB vaccine Phase I. Diabetologia. 2024-02. URL: https://doi.org/10.1007/s00125-024-06092-w ().
- Stene LC et al. T1D risk after SARS‑CoV‑2 infection or vaccination (Nordic registries). medRxiv. 2024-07. URL: https://doi.org/10.1101/2024.07.03.24309894 (aamodt2025thepathophysiologypresentation pages 2-4).
- Bjerregaard-Andersen M et al. COVID‑19 and T1D incidence in Portugal (registry). BMC Endocr Disord. 2024-08. URL: https://doi.org/10.1186/s12902-024-01667-5 ().
- Addissouky TA et al. Type 1 diabetes mellitus: retrospect and prospect. Bull Natl Res Centre. 2024-04. URL: https://doi.org/10.1186/s42269-024-01197-z (addissouky2024type1diabetes pages 1-2).

Expert consensus and analysis
Authoritative 2024–2025 reviews converge on a model wherein HLA-driven adaptive immunity targets β-cells, whose interferon-primed antigen presentation and stress responses amplify immunogenicity; staging by autoantibodies enables early identification, and T-cell–directed therapy can delay progression, while primary prevention (e.g., CVB vaccination) is advancing (herold2024theimmunologyof pages 1-3, brachene2024interferonsarekey pages 4-7, michels2025challengesandopportunities pages 1-2, michels2025challengesandopportunities pages 2-3).

References

1. (michels2025challengesandopportunities pages 2-3): Aaron W Michels, Todd M Brusko, Carmella Evans-Molina, Dirk Homann, Sarah J Richardson, and Alvin C Powers. Challenges and opportunities for understanding the pathogenesis of type 1 diabetes: an endocrine society scientific statement. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf267, doi:10.1210/clinem/dgaf267. This article has 3 citations.

2. (herold2024theimmunologyof pages 1-3): Kevan C. Herold, Thomas Delong, Ana Luisa Perdigoto, Noah Biru, Todd M. Brusko, and Lucy S. K. Walker. The immunology of type 1 diabetes. Nature reviews. Immunology, 24:435-451, Feb 2024. URL: https://doi.org/10.1038/s41577-023-00985-4, doi:10.1038/s41577-023-00985-4. This article has 167 citations.

3. (michels2025challengesandopportunities pages 3-4): Aaron W Michels, Todd M Brusko, Carmella Evans-Molina, Dirk Homann, Sarah J Richardson, and Alvin C Powers. Challenges and opportunities for understanding the pathogenesis of type 1 diabetes: an endocrine society scientific statement. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf267, doi:10.1210/clinem/dgaf267. This article has 3 citations.

4. (brachene2024interferonsarekey pages 4-7): Alexandra Coomans de Brachène, Maria Ines Alvelos, Florian Szymczak, Priscila L. Zimath, Angela Castela, Bianca Marmontel de Souza, Arturo Roca Rivada, Sandra Marín-Cañas, Xiaoyan Yi, Anne Op de Beeck, Noel G. Morgan, Sebastian Sonntag, Sayro Jawurek, Alexandra C. Title, Burcak Yesildag, François Pattou, Julie Kerr-Conte, Eduard Montanya, Montserrat Nacher, Lorella Marselli, Piero Marchetti, Sarah J. Richardson, and Decio L. Eizirik. Interferons are key cytokines acting on pancreatic islets in type 1 diabetes. Diabetologia, 67:908-927, Feb 2024. URL: https://doi.org/10.1007/s00125-024-06106-7, doi:10.1007/s00125-024-06106-7. This article has 37 citations and is from a highest quality peer-reviewed journal.

5. (michels2025challengesandopportunities pages 1-2): Aaron W Michels, Todd M Brusko, Carmella Evans-Molina, Dirk Homann, Sarah J Richardson, and Alvin C Powers. Challenges and opportunities for understanding the pathogenesis of type 1 diabetes: an endocrine society scientific statement. The Journal of clinical endocrinology and metabolism, Jul 2025. URL: https://doi.org/10.1210/clinem/dgaf267, doi:10.1210/clinem/dgaf267. This article has 3 citations.

6. (herold2024theimmunologyof pages 3-4): Kevan C. Herold, Thomas Delong, Ana Luisa Perdigoto, Noah Biru, Todd M. Brusko, and Lucy S. K. Walker. The immunology of type 1 diabetes. Nature reviews. Immunology, 24:435-451, Feb 2024. URL: https://doi.org/10.1038/s41577-023-00985-4, doi:10.1038/s41577-023-00985-4. This article has 167 citations.

7. (addissouky2024type1diabetes pages 1-2): Tamer A. Addissouky, Majeed M. A. Ali, Ibrahim El Tantawy El Sayed, and Yuliang Wang. Type 1 diabetes mellitus: retrospect and prospect. Bulletin of the National Research Centre, 48:1-15, Apr 2024. URL: https://doi.org/10.1186/s42269-024-01197-z, doi:10.1186/s42269-024-01197-z. This article has 54 citations.

8. (aamodt2025thepathophysiologypresentation pages 2-4): Kristie I. Aamodt and Alvin C. Powers. The pathophysiology, presentation and classification of type 1 diabetes. Diabetes, Obesity & Metabolism, 27:15-27, Jul 2025. URL: https://doi.org/10.1111/dom.16628, doi:10.1111/dom.16628. This article has 7 citations.