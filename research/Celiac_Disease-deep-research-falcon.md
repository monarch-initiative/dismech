---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:28.121944'
end_time: '2025-12-17T23:36:53.040017'
duration_seconds: 504.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Celiac Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Celiac Disease**.
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
- **Disease Name:** Celiac Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Celiac Disease**.
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
- Disease Name: Celiac Disease
- MONDO ID: MONDO:0005130
- Category: Complex

Pathophysiology description
Celiac disease (CeD) is an immune-mediated enteropathy initiated by dietary gluten in HLA-DQ2/DQ8–positive individuals. Core steps are: (1) epithelial translocation of gluten peptides via paracellular and transcytotic routes, (2) transglutaminase 2 (TG2) deamidation of gluten peptides increasing affinity for HLA-DQ2/DQ8 on antigen-presenting cells, (3) activation of gluten-specific CD4+ T cells with downstream inflammatory cascades, (4) cytokine-driven epithelial stress responses and cytotoxic intraepithelial lymphocyte (IEL)–mediated epithelial injury, and (5) humoral autoimmunity with anti-TG2 autoantibodies. Recent interventional transcriptomics demonstrate that pharmacologic TG2 inhibition prevents gluten-induced mucosal injury at the molecular level, reinforcing the centrality of TG2-mediated peptide editing and HLA-restricted T cell activation in disease pathogenesis (published online 24 Jun 2024; https://doi.org/10.1038/s41590-024-01867-0) (dotsenko2024transcriptomicanalysisof pages 1-2). Mechanistic overviews further detail epithelial crossing routes, CD4+ T cell cytokines (IFN-γ, IL-17A, IL-21), IL-15–driven IEL cytotoxicity via NK receptors (e.g., NKG2D/CD94–NKG2C) and diagnostic anti-TG2 autoimmunity (Aug 2024; https://doi.org/10.3390/ijms25179412) (rigo2024expressionofmicrornas pages 3-6). Authoritative synthesis confirms IEL cytotoxic effectors are characterized by up-regulation of NKG2D and CD94/NKG2C with epithelial ligands (MICA, HLA-E), and positions IL-15 as a key stress cytokine in driving epithelial damage (Oct 2025; https://doi.org/10.1136/bmj-2024-081353) (doyle2025advancesinthe pages 4-4).

Core Pathophysiology
- Primary mechanisms
  - TG2 deamidation of gluten peptides increases negative charge and HLA-DQ2/DQ8 binding, enabling robust CD4+ T cell activation and proinflammatory mucosal responses; TG2 inhibition (ZED1227) preserved epithelial differentiation, absorptive programs, and prevented gluten-induced injury during challenge (Nature Immunology, 24 Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
  - Gluten peptide transport across epithelium: paracellular (zonulin-associated tight-junction changes) and transcytotic routes (CD71-mediated retrotranscytosis of sIgA–gluten–TG2 complexes) (Aug 2024) (rigo2024expressionofmicrornas pages 3-6). 
  - IEL cytotoxicity: epithelial IL-15 upregulates NK receptors on IELs (e.g., NKG2D), with ligation of stress ligands (MICA/HLA-E) promoting killing of enterocytes; mechanistic reviews emphasize IL-15–NKG2D axis in epithelial destruction (Oct 2025) (doyle2025advancesinthe pages 4-4).
  - Interferon-driven epithelial response: nearly half of gluten-induced gene-expression changes during challenge were linked to epithelial IFN-γ response and type I/II IFN signaling (STAT1/RELA/IRF1 motifs), indicating an IFN-centric transcriptional reprogramming of the mucosa (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
- Dysregulated pathways and cellular processes
  - Antigen processing/presentation: TG2-modified gluten peptides presented by HLA-DQ2/DQ8 to CD4+ T cells (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
  - Cytokine networks: IFN-γ, IL-17A, IL-21 (CD4+ effector signals) and IL-15 (epithelial stress cytokine) (Aug 2024; Oct 2025) (rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4).
  - Barrier and transport programs: TG2 inhibitor preserved epithelial differentiation and nutrient transport signatures under gluten exposure (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).

Key Molecular Players
- Genes/Proteins (HGNC)
  - TGM2 (transglutaminase 2): deamidates gluten peptides; pharmacologic target of ZED1227 (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
  - HLA-DQA1/HLA-DQB1 (DQ2/DQ8) risk alleles: necessary for disease antigen presentation (Jun 2024; Oct 2025) (dotsenko2024transcriptomicanalysisof pages 1-2, doyle2025advancesinthe pages 4-4).
  - IFNG (interferon gamma), STAT1, IRF1: mediators/TFs in epithelial IFN responses during gluten challenge (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
  - IL15 (interleukin-15), KLRK1 (NKG2D), KLRC2 (NKG2C), MICA, HLAE: drivers and ligands of IEL cytotoxicity (Oct 2025) (doyle2025advancesinthe pages 4-4).
  - B cell/autoantibody axis: TG2 (autoantigen) underlies anti-TG2 IgA (Aug 2024) (rigo2024expressionofmicrornas pages 3-6).
- Chemical entities (ChEBI)
  - Gluten immunogenic peptides (proline-/glutamine-rich cereal prolamins) as disease trigger; ZED1227 (small-molecule TG2 inhibitor) as therapeutic probe validating mechanism (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
- Cell types (CL)
  - Gluten-specific CD4+ T helper cells (CL:0000624) drive Th1/Th17/IL-21 responses (Aug 2024) (rigo2024expressionofmicrornas pages 3-6).
  - Intraepithelial lymphocytes (IELs), primarily CD8+ T cells with NK receptor expression (e.g., NKG2D) mediating cytotoxicity (Oct 2025) (doyle2025advancesinthe pages 4-4).
  - B cells/plasma cells producing anti-TG2 (Aug 2024) (rigo2024expressionofmicrornas pages 3-6).
- Anatomical locations (UBERON)
  - Duodenum/small intestinal mucosa (UBERON:0002114/0000160): site of villous atrophy, crypt hyperplasia, IEL expansion, and inflammatory signaling; transcriptomics sampled by biopsy (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).

Biological Processes (GO terms; exemplars)
- Antigen processing and presentation of peptide antigen via MHC class II (GO:0002495): HLA-DQ2/DQ8 presentation of TG2-deamidated gluten (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
- Cytokine-mediated signaling pathway (GO:0019221): IFN-γ, IL-17A, IL-21, IL-15 cascades (Aug 2024; Jun 2024) (rigo2024expressionofmicrornas pages 3-6, dotsenko2024transcriptomicanalysisof pages 1-2).
- Response to interferon-gamma (GO:0034341) and type I interferon signaling pathway (GO:0060337): epithelial signatures under gluten exposure (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
- Regulation of T cell activation (GO:0050863) and NK cell activation (GO:0030101): IEL cytotoxicity via NKG2D/CD94–NKG2C (Oct 2025) (doyle2025advancesinthe pages 4-4).
- Humoral immune response (GO:0006959): anti-TG2 antibody generation (Aug 2024) (rigo2024expressionofmicrornas pages 3-6).

Cellular Components (GO terms)
- MHC class II protein complex (GO:0042613): HLA-DQ2/DQ8 on APCs (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
- External side of plasma membrane (GO:0009897): NKG2D/CD94–NKG2C on IELs; MICA/HLA-E on stressed enterocytes (Oct 2025) (doyle2025advancesinthe pages 4-4).
- Extracellular region (GO:0005576): secreted cytokines (IFN-γ, IL-15, IL-21) (Aug 2024) (rigo2024expressionofmicrornas pages 3-6).

Disease Progression (sequence of events)
- Triggering antigen exposure (gluten) → epithelial translocation (paracellular and CD71-mediated routes) → TG2 deamidation in the lamina propria → HLA-DQ2/DQ8 presentation to CD4+ T cells → Th1/Th17/IL-21 cytokine milieu and B cell activation (anti-TG2) → epithelial stress cytokines (IL-15) and NK receptor upregulation on IELs → cytotoxic killing of enterocytes with villous atrophy and crypt hyperplasia → symptomatic malabsorption (Aug 2024; Oct 2025) (rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4). Molecular interruption of TG2 deamidation blocks much of the ensuing cascade during gluten challenge (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).

Phenotypic Manifestations (HP terms; exemplars)
- Chronic diarrhea (HP:0002028), weight loss (HP:0001824), malabsorption (HP:0002242), anemia (HP:0001903), osteopenia/osteoporosis (HP:0000938/HP:0000939): clinical correlates of villous atrophy and inflammation (contextualized by mechanism in sources cited above) (doyle2025advancesinthe pages 4-4, rigo2024expressionofmicrornas pages 3-6).

Recent developments and latest research (2023–2024 priority)
- Interventional human transcriptomics validates TG2 as a causal therapeutic node: In a randomized, double-blind 6-week gluten-challenge study, oral TG2 inhibitor ZED1227 (100 mg/day) “effectively prevented gluten-induced intestinal damage and inflammation” and preserved epithelial differentiation, nutrient absorption and transporter gene programs; nearly half of gluten-induced changes were attributable to epithelial IFN-γ response with type I/II IFN signatures (published online 24 Jun 2024; DOI:10.1038/s41590-024-01867-0; URL above) (dotsenko2024transcriptomicanalysisof pages 1-2).
- Updated mechanistic synthesis: comprehensive reviews emphasize epithelial translocation mechanisms (CD71-mediated retrotranscytosis), the Th1/Th17/IL-21 axis, and IL-15–driven IEL cytotoxicity via NKG2D/CD94–NKG2C interactions with MICA/HLA-E (Oct 2025; https://doi.org/10.1136/bmj-2024-081353) and highlight anti-TG2 autoimmunity as diagnostic hallmark (Aug 2024; https://doi.org/10.3390/ijms25179412) (doyle2025advancesinthe pages 4-4, rigo2024expressionofmicrornas pages 3-6).

Current applications and real-world implementations
- Pharmacologic probe of mechanism: TG2 inhibitor ZED1227 has been shown in human biopsy transcriptomics to protect mucosa during gluten exposure, supporting potential disease-modifying strategies targeting TG2 (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).
- Diagnostics in clinical practice: anti-TG2 IgA serology and confirmatory duodenal histology remain central; mechanistic reviews describe epithelial transport, T cell responses, and IEL cytotoxicity underlying the histologic lesion (Aug 2024; Oct 2025) (rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4).

Expert opinions and analysis (authoritative sources)
- Nature Immunology investigators conclude that “deamidated gluten–induced adaptive immunity is a sufficient step to set the stage for CeD pathogenesis,” and that transcriptomic protection by TG2 inhibition extends across epithelial morphology, inflammation, and absorptive functions, with HLA-DQ2 gene dose potentially modulating IFN-γ–induced damage (24 Jun 2024; DOI above) (dotsenko2024transcriptomicanalysisof pages 1-2).
- BMJ overview underscores that IEL cytotoxicity is characterized by upregulation of NKG2D and CD94/NKG2C and ligation of MICA/HLA-E, with IL-15 induction on enterocytes facilitating IEL-mediated killing—converging on the IL-15–NKG2D stress axis as a principal effector of epithelial injury (Oct 2025; https://doi.org/10.1136/bmj-2024-081353) (doyle2025advancesinthe pages 4-4).

Relevant statistics and data (recent)
- Prevalence: CeD affects approximately 1% of many populations (preprint summary; Apr 2025; https://doi.org/10.20944/preprints202504.1947.v1) (carreras2025intraepitheliallymphocytesand pages 3-5). 
- Transcriptomic proportioning: nearly half of gluten-induced expression changes are linked to epithelial IFN-γ responses during challenge (Jun 2024) (dotsenko2024transcriptomicanalysisof pages 1-2).

Evidence items (with URLs and publication dates)
- Dotsenko V, et al. Transcriptomic analysis following TG2 inhibitor ZED1227 during gluten challenge (Nature Immunology; published online 24 Jun 2024). URL: https://doi.org/10.1038/s41590-024-01867-0 (dotsenko2024transcriptomicanalysisof pages 1-2).
- Rigo FF, et al. Narrative review of miRNAs summarizing epithelial transport routes, T cell cytokines and anti-TG2 autoimmunity (International Journal of Molecular Sciences; Aug 2024). URL: https://doi.org/10.3390/ijms25179412 (rigo2024expressionofmicrornas pages 3-6).
- Doyle JB, et al. BMJ review detailing NKG2D/CD94–NKG2C on IELs, IL-15 and epithelial ligands (MICA/HLA-E) (BMJ; Oct 2025). URL: https://doi.org/10.1136/bmj-2024-081353 (doyle2025advancesinthe pages 4-4).
- Carreras J, et al. Preprint overview noting ~1% prevalence, HLA dependence and IEL increases (Preprints; 27 Apr 2025). URL: https://doi.org/10.20944/preprints202504.1947.v1 (carreras2025intraepitheliallymphocytesand pages 3-5).
- Siukola E. Spatial transcriptomics thesis/paper summarizing TG2–HLA-DQ2/DQ8 mechanism and genetic/epigenetic contributors (2024; source repository). Citations within describe TG2 deamidation enabling HLA-DQ binding (siukola2024spatialtranscriptomicsofa pages 15-19, siukola2024spatialtranscriptomicsof pages 15-19).

Structured annotations for knowledge base
- Genes/Proteins (HGNC): TGM2; HLA-DQA1/HLA-DQB1; IFNG; STAT1; IRF1; IL15; KLRK1 (NKG2D); KLRC2 (NKG2C); MICA; HLAE (dotsenko2024transcriptomicanalysisof pages 1-2, rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4).
- Biological Processes (GO): antigen presentation via MHC II (GO:0002495); cytokine-mediated signaling (GO:0019221); response to interferon-gamma (GO:0034341); type I interferon signaling (GO:0060337); regulation of T cell activation (GO:0050863); NK cell activation (GO:0030101); humoral immune response (GO:0006959) (dotsenko2024transcriptomicanalysisof pages 1-2, rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4).
- Cellular Components (GO): MHC class II complex (GO:0042613); external side of plasma membrane (GO:0009897); extracellular region (GO:0005576) (dotsenko2024transcriptomicanalysisof pages 1-2, doyle2025advancesinthe pages 4-4, rigo2024expressionofmicrornas pages 3-6).
- Cell Types (CL): CD4+ T helper cell (CL:0000624); intraepithelial T lymphocyte (subset of T cells with NK receptors); B cell/plasma cell (rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4).
- Anatomical Sites (UBERON): small intestine (UBERON:0000160), duodenum (UBERON:0002114), intestinal epithelium (UBERON:0004811) (dotsenko2024transcriptomicanalysisof pages 1-2, doyle2025advancesinthe pages 4-4).
- Chemical Entities (ChEBI): gluten peptides (cereal prolamins); small-molecule TG2 inhibitor ZED1227 (dotsenko2024transcriptomicanalysisof pages 1-2).
- Phenotypes (HP): chronic diarrhea (HP:0002028); malabsorption (HP:0002242); weight loss (HP:0001824); anemia (HP:0001903); osteoporosis (HP:0000939) (mechanistically linked in cited reviews) (doyle2025advancesinthe pages 4-4, rigo2024expressionofmicrornas pages 3-6).

Gaps and open questions (partial evidence)
- Epithelial pyroptosis and IFN–GSDMD axes, refractory CeD clonal evolution with JAK/STAT mutations, viral/microbiome triggers, and flow-cytometric IEL lymphogram performance were not recoverable in the citable context here; these remain active research areas with growing but heterogeneous evidence. Future updates should incorporate primary studies on pyroptosis signatures, RCD genomics, early-life viral exposures, and prospective IEL lymphogram validation cohorts once accessible (dotsenko2024transcriptomicanalysisof pages 1-2, rigo2024expressionofmicrornas pages 3-6, doyle2025advancesinthe pages 4-4).

Citations
- TG2 inhibition prevents gluten-induced injury and reveals IFN-centric epithelial responses: Nature Immunology, 24 Jun 2024. https://doi.org/10.1038/s41590-024-01867-0 (dotsenko2024transcriptomicanalysisof pages 1-2).
- Epithelial transport routes, T helper cytokines, IL-15/IEL cytotoxicity, anti-TG2 autoimmunity: Int J Mol Sci, Aug 2024. https://doi.org/10.3390/ijms25179412 (rigo2024expressionofmicrornas pages 3-6).
- IEL cytotoxic receptors (NKG2D, CD94–NKG2C), ligands (MICA, HLA-E), IL-15 axis: BMJ, Oct 2025. https://doi.org/10.1136/bmj-2024-081353 (doyle2025advancesinthe pages 4-4).
- Population prevalence ≈1%, HLA risk, IEL increases (overview): Preprints, 27 Apr 2025. https://doi.org/10.20944/preprints202504.1947.v1 (carreras2025intraepitheliallymphocytesand pages 3-5).
- TG2–HLA-DQ2/DQ8 canonical mechanism summarized in spatial transcriptomics context: 2024 repository (siukola2024spatialtranscriptomicsofa pages 15-19, siukola2024spatialtranscriptomicsof pages 15-19).

References

1. (dotsenko2024transcriptomicanalysisof pages 1-2): Valeriia Dotsenko, Bernhard Tewes, Martin Hils, Ralf Pasternack, Jorma Isola, Juha Taavela, Alina Popp, Jani Sarin, Heini Huhtala, Pauliina Hiltunen, Timo Zimmermann, Ralf Mohrbacher, Roland Greinwald, Knut E. A. Lundin, Detlef Schuppan, Markku Mäki, Keijo Viiri, Karin Kull, Jari Koskenpato, Mika Scheinin, Marja-Leena Lähdeaho, Michael Schumann, Yurdagül Zopf, Andreas Stallmach, Ansgar W. Lohse, Stefano Fusco, Jost Langhorst, Helga Paula Török, Valerie Byrnes, Juozas Kupcinskas, Øistein Hovde, Jørgen Jahnsen, Luc Biedermann, and Jonas Zeitz. Transcriptomic analysis of intestine following administration of a transglutaminase 2 inhibitor to prevent gluten-induced intestinal damage in celiac disease. Nature Immunology, 25:1218-1230, Jun 2024. URL: https://doi.org/10.1038/s41590-024-01867-0, doi:10.1038/s41590-024-01867-0. This article has 34 citations and is from a highest quality peer-reviewed journal.

2. (rigo2024expressionofmicrornas pages 3-6): Francielen Furieri Rigo, Ellen Cristina Souza de Oliveira, Ana Elisa Valencise Quaglio, Bruna Damásio Moutinho, Luiz Claudio Di Stasi, and Ligia Yukie Sassaki. Expression of micrornas in adults with celiac disease: a narrative review. International Journal of Molecular Sciences, 25:9412, Aug 2024. URL: https://doi.org/10.3390/ijms25179412, doi:10.3390/ijms25179412. This article has 6 citations and is from a poor quality or predatory journal.

3. (doyle2025advancesinthe pages 4-4): John B Doyle, Jocelyn Silvester, Jonas F Ludvigsson, and Benjamin Lebwohl. Advances in the pathophysiology, diagnosis, and management of celiac disease. BMJ, 391:e081353, Oct 2025. URL: https://doi.org/10.1136/bmj-2024-081353, doi:10.1136/bmj-2024-081353. This article has 1 citations and is from a domain leading peer-reviewed journal.

4. (carreras2025intraepitheliallymphocytesand pages 3-5): J Carreras, G Roncador, R Hamoudi, and JA Bombi. Intraepithelial lymphocytes and lair1 expression in celiac disease. Apr 2025. URL: https://doi.org/10.20944/preprints202504.1947.v1, doi:10.20944/preprints202504.1947.v1.

5. (siukola2024spatialtranscriptomicsofa pages 15-19): E Siukola. Spatial transcriptomics of celiac disease small intestine in different stages of inflammation. Unknown journal, 2024.

6. (siukola2024spatialtranscriptomicsof pages 15-19): E Siukola. Spatial transcriptomics of celiac disease small intestine in different stages of inflammation. Unknown journal, 2024.