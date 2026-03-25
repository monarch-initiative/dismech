---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-04T19:33:43.389249'
end_time: '2026-02-04T19:42:15.184055'
duration_seconds: 511.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type I
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type I
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type I**.
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
- **Disease Name:** Osteogenesis Imperfecta Type I
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type I**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Osteogenesis Imperfecta Type I
- MONDO ID: 
- Category: Mendelian

Pathophysiology description
Osteogenesis imperfecta (OI) type I is the mild, dominantly inherited form of OI caused predominantly by COL1A1 haploinsufficiency. Premature termination codons in one COL1A1 allele trigger nonsense‑mediated mRNA decay (NMD), reducing pro‑α1(I) synthesis and yielding a quantitative type I collagen deficiency without a dominant‑negative effect. As a result, bone matrix is assembled from fewer but structurally normal type I collagen trimers, predisposing to high bone turnover, low bone mass, and impaired bone material quality (reduced cortical thickness, increased porosity, and brittle matrix) that together increase fracture risk (doi:10.1210/endrev/bnab017, May 2022; doi:10.1007/s00223-024-01266-5, Aug 2024). Mechanistically, osteoblast maturation and ER handling of procollagen are perturbed, osteocytes exhibit dysregulated perilacunar/canalicular remodeling and signaling (sclerostin, RANKL), and osteoclastogenesis is enhanced via RANKL, culminating in imbalanced remodeling and poor-quality matrix replacement (S Sithambaram 2024; doi:10.1371/journal.pone.0309801, Feb 2025; doi:10.1210/endrev/bnab017, May 2022). Upregulated TGF‑β signaling—documented across OI models and patient tissues—further skews osteoprogenitor differentiation, elevates turnover, and is being targeted clinically (doi:10.3390/jcm13123484, Jun 2024; NCT03064074, results posted Oct 2024).

Core Pathophysiology
- Primary mechanisms
  - Nonsense-mediated decay and quantitative collagen I deficiency: “nonsense mediated decay of the mRNA message” leads to a reduced amount of α1(I) chains and “about half the amount of structurally normal trimer,” underpinning the mild OI type I phenotype (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33). Endocrine Reviews and a 2024 genetics update reinforce that COL1A1/2 defects drive collagen-related OI; type I results from COL1A1 haploinsufficiency (doi:10.1210/endrev/bnab017, May 2022; doi:10.1007/s00223-024-01266-5, Aug 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5).
- Downstream effects on matrix and bone quality
  - Matrix organization/cross-linking and mineral ultrastructure: disordered collagen fibril organization, altered cross-link profile, and hypermineralized yet brittle matrix with thinner, densely packed mineral platelets; cortical thinning and increased porosity; trabecular BV/TV and connectivity reduced (S Sithambaram 2024; doi:10.1210/endrev/bnab017, May 2022) (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
  - Osteoblast lineage dysfunction: impaired maturation programs and ER chaperone alterations (e.g., downregulation of SERPINH1/HSP47) correlate with defective matrix production and signaling changes (doi:10.1371/journal.pone.0309801, Feb 2025) (corcelli2025pleiotropiceffectsof pages 12-13).
- Dysregulated pathways
  - TGF‑β: Increased TGF‑β/SMAD signaling in OI bone associates with expanded progenitor pools, fewer mature osteoblasts, and higher turnover; anti‑TGF‑β normalizes pSMAD2 and improves bone mass in models; fresolimumab advanced to a Phase 1 safety study in adults with OI (doi:10.3390/jcm13123484, Jun 2024; NCT03064074; results first posted Oct 8, 2024; last update Dec 4, 2024; https://clinicaltrials.gov/study/NCT03064074) (kaspiris2024unravelingthelink pages 5-7, NCT03064074).
  - WNT/sclerostin axis: Osteocytes secrete sclerostin, inhibiting WNT/β‑catenin signaling and limiting osteoblast activity; antisclerostin therapies (setrusumab/romosozumab) pursue anabolic rescue (doi:10.1210/endrev/bnab017, May 2022; S Sithambaram 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33).
  - RANKL/osteocyte PLR: Osteocytes are the main source of soluble RANKL driving osteoclastogenesis and are central to perilacunar/canalicular remodeling that modulates matrix quality; increased osteoclast activity and turnover are features of OI (S Sithambaram 2024; doi:10.1210/endrev/bnab017, May 2022; doi:10.1371/journal.pone.0309801, Feb 2025) (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5, corcelli2025pleiotropiceffectsof pages 12-13).

Key Molecular Players
- Genes/Proteins (HGNC)
  - COL1A1 (HGNC:2197): haploinsufficiency via NMD—quantitative defect causing OI type I (doi:10.1210/endrev/bnab017; doi:10.1007/s00223-024-01266-5) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5).
  - COL1A2 (HGNC:2198): partner α2(I) chain; structural variants modulate severity and DI risk (doi:10.1210/endrev/bnab017; doi:10.1007/s00223-024-01266-5) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5).
  - SERPINH1/HSP47 (HGNC:12209): ER collagen chaperone; downregulated in OI osteoblasts correlating with impaired folding and matrix stability (doi:10.1371/journal.pone.0309801) (corcelli2025pleiotropiceffectsof pages 12-13).
  - SOST (HGNC:11195): osteocyte-derived sclerostin; therapeutic target (doi:10.1210/endrev/bnab017) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
  - TNFSF11/RANKL (HGNC:11901): osteoclastogenic ligand elevated in OI osteoblasts (doi:10.1371/journal.pone.0309801) (corcelli2025pleiotropiceffectsof pages 12-13).
- Chemical Entities (CHEBI)
  - Bisphosphonates (CHEBI:77375): anti-resorptives; increase BMD but fracture benefit/material property rescue are variable (doi:10.1210/endrev/bnab017; S Sithambaram 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33).
  - Losartan (CHEBI:65330): AT1 receptor blocker; preclinical OI work suggests modulation of TGF‑β‑linked osteoblast differentiation and bone mass (M. Morita et al., Sep 2024; doi:10.1016/j.bonr.2024.101795) ().
  - Fresolimumab: pan‑TGF‑β monoclonal antibody; Phase 1 safety in OI (NCT03064074; ClinicalTrials.gov page updated Dec 2024) (NCT03064074).
  - Sclerostin inhibitors (setrusumab/romosozumab): WNT anabolic class in OI trials (doi:10.1210/endrev/bnab017; S Sithambaram 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33).
- Cell Types (CL)
  - Osteoblasts (CL:0000062): impaired differentiation/folding/ER quality control; altered signaling (TGF‑β/WNT) (doi:10.1371/journal.pone.0309801; doi:10.1210/endrev/bnab017) (corcelli2025pleiotropiceffectsof pages 12-13, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
  - Osteocytes (CL:0000138): sclerostin and RANKL source; regulate PLR and bone quality (S Sithambaram 2024; doi:10.1210/endrev/bnab017) (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
  - Osteoclasts (CL:0000092): increased formation/activity driven by RANKL and inflammatory cues; high turnover (S Sithambaram 2024; doi:10.1371/journal.pone.0309801) (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13).
- Anatomical Locations (UBERON)
  - Bone tissue (UBERON:0002481): low mass, brittle matrix (doi:10.1210/endrev/bnab017) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
  - Cortical bone (UBERON:0002487): thinning and porosity increase (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33).
  - Trabecular bone (UBERON:0002488): reduced BV/TV and connectivity (doi:10.1210/endrev/bnab017) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).

Biological Processes (for GO annotation)
- Collagen fibril organization (GO:0030199): disordered fibrils and altered cross-linking underlie brittle matrix (doi:10.1007/s00223-024-01266-5; doi:10.1210/endrev/bnab017) (jovanovic2024updateonthe pages 4-5, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Bone mineralization (GO:0030282): abnormal ultrastructure and heterogeneity despite variable density (S Sithambaram 2024; doi:10.1371/journal.pone.0309801) (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13).
- Osteoblast differentiation (GO:0001649): impaired maturation, altered ER proteostasis and signaling (doi:10.1371/journal.pone.0309801) (corcelli2025pleiotropiceffectsof pages 12-13).
- Osteoclast differentiation (GO:0030316): elevated RANKL drives increased osteoclastogenesis (S Sithambaram 2024; doi:10.1371/journal.pone.0309801) (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13).
- Bone remodeling (GO:0046849): increased turnover with poor-quality replacement (doi:10.1210/endrev/bnab017; S Sithambaram 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33).
- TGF‑β signaling (GO:0007179): upregulated; therapeutic target (doi:10.3390/jcm13123484; NCT03064074) (kaspiris2024unravelingthelink pages 5-7, NCT03064074).
- WNT/β‑catenin signaling (GO:0060070): suppressed by sclerostin; target for antisclerostin agents (doi:10.1210/endrev/bnab017; S Sithambaram 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33).

Cellular Components
- Endoplasmic reticulum (GO:0005783): site of procollagen folding; defects reduce secretion and stress osteoblasts (doi:10.1007/s00223-024-01266-5) (jovanovic2024updateonthe pages 4-5).
- Extracellular matrix (GO:0031012): misorganized collagen/mineral compromises mechanical properties (doi:10.1007/s00223-024-01266-5) (jovanovic2024updateonthe pages 4-5).

Disease Progression
- Sequence of events: COL1A1 haploinsufficiency via NMD reduces type I collagen output → defective fibril assembly/cross-linking and altered mineral ultrastructure → osteoblast maturation stress and ER handling strain; osteocytes signal via elevated sclerostin and RANKL, with diminished PLR quality control → increased osteoclastogenesis and high-turnover remodeling → cortical thinning/porosity, low trabecular BV/TV and connectivity → fractures with often decreasing frequency after adolescence in type I (S Sithambaram 2024; doi:10.1210/endrev/bnab017) (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Phases: childhood/ adolescence with peak fracture frequency; gradual decline after puberty typical of type I (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33).

Phenotypic Manifestations (and mechanistic linkage)
- Recurrent fractures: brittle, low-mass bone from quantitative collagen deficiency and poor material quality (doi:10.1210/endrev/bnab017; doi:10.1007/s00223-024-01266-5) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5).
- Blue sclerae: thinner scleral collagen matrix in type I OI (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33).
- Hearing loss: conductive/sensorineural deficits in adulthood linked to collagen I defects (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33).
- Dentinogenesis imperfecta: dentin matrix abnormalities from collagen defects (more frequent with structural collagen mutations) (doi:10.1007/s00223-024-01266-5) (jovanovic2024updateonthe pages 4-5).

Current applications and real-world implementations (selected, 2023–2024 emphasis)
- Anti‑TGF‑β therapy (fresolimumab): Phase 1 study in adults with moderate‑severe OI (N=11). Single‑dose (1 or 4 mg/kg) and repeat dosing cohorts; safety outcomes posted Oct 2024; mechanistic rationale from elevated TGF‑β in OI bone (NCT03064074; https://clinicaltrials.gov/study/NCT03064074) (NCT03064074, kaspiris2024unravelingthelink pages 5-7).
- Anti‑sclerostin therapy (setrusumab/romosozumab): Ongoing pediatric and mixed-age trials evaluating BMD and fracture endpoints in OI. Examples:
  - NCT05125809 (Phase 2/3; active, not recruiting; 183 participants; sponsor Ultragenyx; URL: https://clinicaltrials.gov/study/NCT05125809) ().
  - NCT05768854 (Phase 3; pediatric head‑to‑head vs bisphosphonates; active, not recruiting; 69 participants; URL: https://clinicaltrials.gov/study/NCT05768854) ().
  - NCT06636071 (Phase 3; pediatric Japanese subjects; active, not recruiting; URL: https://clinicaltrials.gov/study/NCT06636071) ().
  - NCT05312697 (adult long‑term extension; terminated after limited enrollment; URL: https://clinicaltrials.gov/study/NCT05312697) ().
  - NCT05972551 (romosozumab vs bisphosphonates in children/adolescents; recruiting; 106 participants; sponsor Amgen; URL: https://clinicaltrials.gov/study/NCT05972551) ().
- Standard of care anti‑resorptives (bisphosphonates): increase BMD; fracture outcome benefit equivocal and material properties not fully restored (doi:10.1210/endrev/bnab017, May 2022) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Renin‑angiotensin modulation (losartan): Preclinical OI model data indicate TGF‑β pathway modulation with increased bone mass and altered osteoblast differentiation (M. Morita et al., Bone Reports, Sep 2024; doi:10.1016/j.bonr.2024.101795) ().
- Emerging gene editing: AAV‑based correction of collagen I mutations is under preclinical investigation as a future strategy for dominant OI (Molecular Therapy‑Nucleic Acids, Mar 2024; doi:10.1016/j.omtn.2023.102111) (NCT03064074, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).

Expert opinions and analysis
- Authoritative reviews synthesize OI as a collagen‑related disorder in which defects span synthesis, folding, PTM, processing, and trafficking, converging on abnormal ECM and dysregulated signaling (Endocrine Reviews 2022; Calcified Tissue International 2024; URLs: https://doi.org/10.1210/endrev/bnab017; https://doi.org/10.1007/s00223-024-01266-5). Both emphasize that COL1A1 haploinsufficiency yields type I OI with milder skeletal phenotype and extraskeletal features (hearing loss, DI, blue sclerae), while bone material quality deficits persist despite mass gains from antiresorptives (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5).
- A 2024 clinical‑molecular review of TGF‑β in OI links upregulated pathway activity to scoliosis and generalized bone turnover changes, rationalizing clinical testing of TGF‑β blockade (https://doi.org/10.3390/jcm13123484, Jun 2024) (kaspiris2024unravelingthelink pages 5-7).

Relevant statistics and data from recent studies
- Clinical trial landscape (selected metrics from registrations 2022–2024):
  - Setrusumab pediatric Phase 3 head‑to‑head vs bisphosphonates (NCT05768854): target enrollment 69; active, not recruiting (posted 2023; status verified 2025) ().
  - Setrusumab global Phase 2/3 (NCT05125809): target enrollment 183; active, not recruiting (status verified in 2025 listings) ().
  - Romosozumab pediatric Phase 3 (NCT05972551): target enrollment 106; recruiting (first posted 2023; recruiting in 2025 listings) ().
  - Fresolimumab Phase 1 (NCT03064074): enrollment 11; results first posted Oct 8, 2024; last update Dec 4, 2024 (NCT03064074).
- Genetic epidemiology note: In European cohorts, approximately 85–90% of OI cases harbor dominant COL1A1/2 variants (contextualizing the dominance of collagen I pathway biology) (doi:10.1371/journal.pone.0309801, Feb 2025) (corcelli2025pleiotropiceffectsof pages 12-13).

Gene/protein annotations with ontology terms (selected)
- COL1A1 (HGNC:2197) — function: collagen fibril organization (GO:0030199), extracellular matrix (GO:0031012) (doi:10.1007/s00223-024-01266-5) (jovanovic2024updateonthe pages 4-5).
- COL1A2 (HGNC:2198) — as above for partner chain (jovanovic2024updateonthe pages 4-5, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- SERPINH1/HSP47 (HGNC:12209) — endoplasmic reticulum (GO:0005783); collagen folding chaperone (doi:10.1371/journal.pone.0309801) (corcelli2025pleiotropiceffectsof pages 12-13).
- SOST (HGNC:11195) — negative regulation of WNT signaling (GO:0060828) conceptually; osteocyte secretion linked to reduced osteoblastogenesis in OI (doi:10.1210/endrev/bnab017) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- TNFSF11/RANKL (HGNC:11901) — osteoclast differentiation (GO:0030316) (doi:10.1371/journal.pone.0309801) (corcelli2025pleiotropiceffectsof pages 12-13).

Phenotype associations (HPO terms)
- Recurrent fractures (HPO:0002757) (doi:10.1210/endrev/bnab017) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Blue sclerae (HPO:0000592) (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33).
- Hearing loss (HPO:0000365) (S Sithambaram 2024) (sithambaram2024effectofbisphosphonates pages 30-33).
- Dentinogenesis imperfecta (HPO:0000707) (doi:10.1007/s00223-024-01266-5) (jovanovic2024updateonthe pages 4-5).

Cell type involvement (CL terms)
- Osteoblasts (CL:0000062): differentiation impaired; ER proteostasis stress (doi:10.1371/journal.pone.0309801) (corcelli2025pleiotropiceffectsof pages 12-13).
- Osteocytes (CL:0000138): sclerostin/RANKL production; PLR and matrix quality (S Sithambaram 2024; doi:10.1210/endrev/bnab017) (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Osteoclasts (CL:0000092): increased RANKL‑driven formation; high turnover (S Sithambaram 2024; doi:10.1371/journal.pone.0309801) (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13).

Anatomical locations (UBERON terms)
- Bone tissue (UBERON:0002481); cortical bone (UBERON:0002487); trabecular bone (UBERON:0002488) — all show quantitative and qualitative deficits characteristic of OI type I (doi:10.1210/endrev/bnab017; S Sithambaram 2024) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33).

Chemical entities (ChEBI) and interventions
- Bisphosphonates (CHEBI:77375): anti-resorptive standard of care; gains in BMD with variable fracture benefit (doi:10.1210/endrev/bnab017) (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Losartan (CHEBI:65330): preclinical TGF‑β modulation and osteoblast effects in OI model (Sep 2024; doi:10.1016/j.bonr.2024.101795) ().
- Fresolimumab (anti‑TGF‑β): clinical safety established in a small adult OI cohort (NCT03064074) (NCT03064074).
- Sclerostin inhibitors (setrusumab/romosozumab): ongoing OI clinical studies with BMD/clinical endpoints (NCT05125809, NCT05768854, NCT05972551) (, , ).

Embedded ontology-aligned summary
| Category | Entity (common name) | Identifier | Role in OI Type I pathophysiology | Evidence | Support |
|---|---|---|---|---|---|
| Gene | COL1A1 (type I collagen alpha-1) | HGNC:2197 | Haploinsufficiency via NMD reduces proα1(I) synthesis → quantitative collagen I deficiency (~50% normal trimers) driving mild Type I OI | doi:10.1007/s00223-024-01266-5; doi:10.1210/endrev/bnab017 | (jovanovic2024updateonthe pages 4-5, jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Gene | COL1A2 (type I collagen alpha-2) | HGNC:2198 | Partner chain in heterotrimer; mutations alter trimer stoichiometry/structure and contribute to phenotypic variability (DI, severity) | doi:10.1210/endrev/bnab017; doi:10.1007/s00223-024-01266-5 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5) |
| Gene | SERPINH1 / HSP47 (collagen chaperone) | HGNC:12209 | ER chaperone for procollagen folding; dysregulation impairs collagen stability/secretion and matrix quality | doi:10.1371/journal.pone.0309801 | (corcelli2025pleiotropiceffectsof pages 12-13) |
| Gene | SOST (sclerostin) | HGNC:11195 | Osteocyte-secreted Wnt inhibitor; elevated/inappropriate sclerostin signalling limits Wnt-driven bone formation — therapeutic target for antisclerostin antibodies | doi:10.1210/endrev/bnab017; Sithambaram 2024 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33) |
| Gene | TNFSF11 / RANKL | HGNC:11901 | Osteocyte/osteoblast-derived osteoclastogenic ligand; increased RANKL/osteoclast activity contributes to high bone turnover in OI | doi:10.1371/journal.pone.0309801; Sithambaram 2024 | (corcelli2025pleiotropiceffectsof pages 12-13, sithambaram2024effectofbisphosphonates pages 30-33) |
| Pathway | TGFB1 pathway | GO:0007179 | Upregulated TGF‑β signalling in OI → altered osteoprogenitor/osteoblast differentiation, increased turnover; target of anti‑TGF‑β (fresolimumab, NCT03064074) | doi:10.3390/jcm13123484; NCT03064074 | (kaspiris2024unravelingthelink pages 5-7, NCT03064074) |
| Pathway | Wnt/β-catenin signalling | GO:0060070 | Central for osteoblast function/formation; inhibited by sclerostin/DKK1 in disease states — modulation increases bone formation in models | doi:10.1210/endrev/bnab017; Sithambaram 2024 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33) |
| Biological Process | Collagen fibril organization | GO:0030199 | Disordered fibril assembly and altered cross-linking produce a brittle matrix with impaired mechanical properties | doi:10.1007/s00223-024-01266-5; doi:10.1210/endrev/bnab017 | (jovanovic2024updateonthe pages 4-5, jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Biological Process | Bone mineralization | GO:0030282 | Altered mineral ultrastructure (higher/mineralization heterogeneity, disordered platelets) contributes to fragility despite variable BMD | Sithambaram 2024; doi:10.1371/journal.pone.0309801 | (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13) |
| Biological Process | Osteoblast differentiation | GO:0001649 | Impaired osteoblast maturation, ER stress and aberrant osteogenic gene programs reduce quality matrix production | Mohanpuria 2025; doi:10.1371/journal.pone.0309801 | (mohanpuria2025…thromboxanesynthase pages 48-53, corcelli2025pleiotropiceffectsof pages 12-13) |
| Biological Process | Osteoclast differentiation | GO:0030316 | RANKL-driven osteoclastogenesis is increased → elevated resorption and remodelling imbalance | Sithambaram 2024; doi:10.1371/journal.pone.0309801 | (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13) |
| Biological Process | Bone remodeling | GO:0046849 | Net effect: increased turnover with poor matrix replacement → low mass, cortical thinning and brittleness | doi:10.1210/endrev/bnab017; Sithambaram 2024 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33) |
| Cellular Component | Endoplasmic reticulum | GO:0005783 | Site of procollagen synthesis/post‑translational modification; ER folding/trafficking defects reduce secretion and cause osteoblast stress | doi:10.1007/s00223-024-01266-5 | (jovanovic2024updateonthe pages 4-5) |
| Cellular Component | Extracellular matrix | GO:0031012 | Location of collagen fibrils and mineral; altered ECM organization underlies poor material properties | doi:10.1007/s00223-024-01266-5 | (jovanovic2024updateonthe pages 4-5) |
| Cell type | Osteocyte | CL:0000138 | Master regulator: produces sclerostin and RANKL, mediates perilacunar/canalicular remodelling (PLR); osteocyte dysfunction alters matrix quality and remodelling | Sithambaram 2024; doi:10.1210/endrev/bnab017 | (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Cell type | Osteoblast | CL:0000062 | Matrix-secreting lineage; impaired differentiation and ER stress in OI reduce correct collagen production and mineral deposition | doi:10.1371/journal.pone.0309801; doi:10.1210/endrev/bnab017 | (corcelli2025pleiotropiceffectsof pages 12-13, jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Cell type | Osteoclast | CL:0000092 | Resorptive effector increased by RANKL and inflammatory cues in OI, contributing to high turnover | Sithambaram 2024; doi:10.1371/journal.pone.0309801 | (sithambaram2024effectofbisphosphonates pages 30-33, corcelli2025pleiotropiceffectsof pages 12-13) |
| Anatomy | Bone tissue | UBERON:0002481 | Primary affected organ with low mass, altered microarchitecture and poor matrix quality → fracture risk | doi:10.1210/endrev/bnab017 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Anatomy | Cortical bone | UBERON:0002487 | Cortical thinning and increased porosity are key determinants of load-bearing failure in OI | Sithambaram 2024 | (sithambaram2024effectofbisphosphonates pages 30-33) |
| Anatomy | Trabecular bone | UBERON:0002488 | Reduced trabecular number and connectivity (low BV/TV) contribute to skeletal fragility | doi:10.1210/endrev/bnab017 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Phenotype | Dentinogenesis imperfecta | HPO:0000707 | Dental dentin defects linked to collagen abnormalities, more frequent with structural collagen mutations | doi:10.1007/s00223-024-01266-5 | (jovanovic2024updateonthe pages 4-5) |
| Phenotype | Blue sclerae | HPO:0000592 | Thinner/translucent scleral collagen leading to characteristic blue appearance, common in Type I | Sithambaram 2024; doi:10.1210/endrev/bnab017 | (sithambaram2024effectofbisphosphonates pages 30-33, jovanovic2022osteogenesisimperfectamechanisms pages 4-5) |
| Phenotype | Hearing loss | HPO:0000365 | Conductive/sensorineural hearing loss associated with collagen defects; adult-onset risk in Type I | Sithambaram 2024 | (sithambaram2024effectofbisphosphonates pages 30-33) |
| Phenotype | Recurrent fractures | HPO:0002757 | Clinical hallmark from early childhood due to brittle matrix + low bone mass; fracture frequency often declines after adolescence in Type I | doi:10.1210/endrev/bnab017; doi:10.1007/s00223-024-01266-5 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5) |
| Chemical / Drug | Bisphosphonates | CHEBI:77375 | Anti-resorptive widely used off-label in children/adults with OI; increases BMD but variable fracture benefit and does not fully restore material quality | doi:10.1210/endrev/bnab017; Sithambaram 2024 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33) |
| Chemical / Drug | Losartan | CHEBI:65330 | AT1R blocker repurposed in preclinical OI work to modulate TGF‑β signalling and osteoblast differentiation (preclinical evidence) | Mohanpuria 2025; (preclinical reports) | (mohanpuria2025…thromboxanesynthase pages 48-53, corcelli2025pleiotropiceffectsof pages 12-13) |
| Drug / Biologic | Fresolimumab (anti‑TGF‑β) | — | Pan‑TGF‑β neutralizing antibody tested in Phase 1 safety trial in OI (NCT03064074) based on TGF‑β upregulation in models | NCT03064074 | (NCT03064074, kaspiris2024unravelingthelink pages 5-7) |
| Therapy class | Sclerostin inhibition (setrusumab / romosozumab) | — | Antisclerostin antibodies increase Wnt signalling and bone formation; under clinical evaluation in OI (improved BMD in trials/models) | doi:10.1210/endrev/bnab017; Sithambaram 2024 | (jovanovic2022osteogenesisimperfectamechanisms pages 4-5, jovanovic2024updateonthe pages 4-5, sithambaram2024effectofbisphosphonates pages 30-33) |


*Table: Compact ontology-aligned table linking genes, pathways, cells, anatomy, phenotypes and therapies relevant to Osteogenesis Imperfecta Type I, with one-line roles and primary evidence from the assembled context (pqac IDs). This supports fast integration into a disease knowledge base and points to the primary sources used.*

Evidence items with URLs and dates
- Jovanovic & Marini. Update on the Genetics of OI. Calcified Tissue Int. Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5 (jovanovic2024updateonthe pages 4-5).
- Jovanovic et al. Osteogenesis imperfecta: mechanisms and pathways. Endocrine Reviews. May 2022. URL: https://doi.org/10.1210/endrev/bnab017 (jovanovic2022osteogenesisimperfectamechanisms pages 4-5).
- Kaspiris et al. Altered TGF‑β signaling and scoliosis in OI. J Clin Med. Jun 2024. URL: https://doi.org/10.3390/jcm13123484 (kaspiris2024unravelingthelink pages 5-7).
- Fresolimumab Phase 1 in OI (anti‑TGF‑β). NCT03064074. Results first posted Oct 8, 2024; last update Dec 4, 2024. URL: https://clinicaltrials.gov/study/NCT03064074 (NCT03064074).
- Corcelli et al. Pleiotropic effects in an OI model (matrix organization; signaling). PLoS One. Feb 2025. URL: https://doi.org/10.1371/journal.pone.0309801 (corcelli2025pleiotropiceffectsof pages 12-13).
- Sithambaram S. Effect of bisphosphonates/mechanisms overview. 2024. (sithambaram2024effectofbisphosphonates pages 30-33).
- Setrusumab trials: NCT05125809 (posted 2022; status active, not recruiting), NCT05768854 (posted 2023; active, not recruiting), NCT06636071 (posted 2024; active, not recruiting), NCT05312697 (posted 2022; terminated) — ClinicalTrials.gov URLs as in text (, , , ).
- Romosozumab pediatric trial: NCT05972551 (recruiting; first posted 2023; status verified in 2025 listings). URL: https://clinicaltrials.gov/study/NCT05972551 ().

Notes and limitations
- Most mechanistic claims for OI type I derive from collagen biology and bone cell signaling principles summarized in Endocrine Reviews (2022) and the 2024 genetics update; 2023–2024 publications and trial records refine pathway targeting (TGF‑β, antisclerostin). Where specific 2023–2024 human quantitative outcomes (e.g., fracture risk reduction) are pending, we cite active or recently updated trials and translational reviews, and highlight the current status of evidence.


References

1. (sithambaram2024effectofbisphosphonates pages 30-33): S Sithambaram. Effect of bisphosphonates on the response to mechanical stimulation in children with osteogenesis imperfecta. Unknown journal, 2024.

2. (jovanovic2022osteogenesisimperfectamechanisms pages 4-5): Milena Jovanovic, Gali Guterman-Ram, and Joan C Marini. Osteogenesis imperfecta: mechanisms and signaling pathways connecting classical and rare oi types. Endocrine reviews, 43:61-90, May 2022. URL: https://doi.org/10.1210/endrev/bnab017, doi:10.1210/endrev/bnab017. This article has 182 citations and is from a domain leading peer-reviewed journal.

3. (jovanovic2024updateonthe pages 4-5): Milena Jovanovic and Joan C. Marini. Update on the genetics of osteogenesis imperfecta. Calcified Tissue International, 115:891-914, Aug 2024. URL: https://doi.org/10.1007/s00223-024-01266-5, doi:10.1007/s00223-024-01266-5. This article has 48 citations and is from a peer-reviewed journal.

4. (corcelli2025pleiotropiceffectsof pages 12-13): Michelangelo Corcelli, Rachel Sagar, Ellen Petzendorfer, Mohammad Mehedi Hasan, Fleur S. van Dijk, Anna L. David, and Pascale V. Guillot. Pleiotropic effects of a recessive col1a2 mutation occurring in a mouse model of severe osteogenesis imperfecta. PLOS ONE, 20:e0309801, Feb 2025. URL: https://doi.org/10.1371/journal.pone.0309801, doi:10.1371/journal.pone.0309801. This article has 1 citations and is from a peer-reviewed journal.

5. (kaspiris2024unravelingthelink pages 5-7): Angelos Kaspiris, Elias S. Vasiliadis, Georgios Tsalimas, Dimitra Melissaridou, Ioanna Lianou, Fotios Panagopoulos, Galateia Katzouraki, Michail Vavourakis, Ioannis Kolovos, Olga D. Savvidou, Evangelia Papadimitriou, and Spiros G. Pneumaticos. Unraveling the link of altered tgfβ signaling with scoliotic vertebral malformations in osteogenesis imperfecta: a comprehensive review. Journal of Clinical Medicine, 13:3484, Jun 2024. URL: https://doi.org/10.3390/jcm13123484, doi:10.3390/jcm13123484. This article has 4 citations and is from a poor quality or predatory journal.

6. (NCT03064074): Brendan Lee. Safety of Fresolimumab in the Treatment of Osteogenesis Imperfecta. Baylor College of Medicine. 2017. ClinicalTrials.gov Identifier: NCT03064074

7. (mohanpuria2025…thromboxanesynthase pages 48-53): N Mohanpuria. … thromboxane synthase inhibition in osteoblast differentiation and mineralization, and the pathophysiology of the ifitm5 pathogenic variant in osteogenesis imperfecta …. Unknown journal, 2025.