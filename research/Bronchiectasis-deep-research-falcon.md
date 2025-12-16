---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:00:54.817963'
end_time: '2025-12-15T09:10:49.051530'
duration_seconds: 594.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bronchiectasis
  mondo_id: ''
  category: Respiratory Disease
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Bronchiectasis
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Bronchiectasis**.
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
- **Disease Name:** Bronchiectasis
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Bronchiectasis**.
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
- Disease Name: Bronchiectasis (non–cystic fibrosis)
- MONDO ID: 
- Category: Respiratory Disease

Research Objectives: Pathophysiology of Bronchiectasis

Overview and key concepts
- Definition and core model: Bronchiectasis is radiologically defined by permanent bronchial dilatation and clinically by chronic cough, sputum, recurrent infections, and airflow limitation. Its pathobiology is best captured by the “vicious cycle” revised to a “vicious vortex,” in which mucociliary dysfunction, persistent infection (microbiome dysbiosis), chronic airway inflammation, and structural damage mutually reinforce one another rather than proceeding linearly ("interconnected and not strictly sequential") (keir2021pathophysiologyofbronchiectasis pages 2-2, keir2021pathophysiologyofbronchiectasis pages 1-2). 
- Central role of neutrophilic inflammation: Neutrophils dominate airway inflammation; delayed neutrophil apoptosis, NETosis, and excessive release of neutrophil serine proteases (NSPs: neutrophil elastase [NE], proteinase 3 [PR3], cathepsin G [CatG]) drive protease–antiprotease imbalance, epithelial injury, mucus abnormalities, and disease progression (chalmers2025neutrophilicinflammationin pages 1-2, perea2024pathophysiologyandgenomics pages 2-3).

1) Core pathophysiology
- Mucociliary dysfunction
  - Ciliary impairment arises from primary causes (e.g., PCD) and secondary injury. Infection-derived factors such as Pseudomonas pyocyanin reduce ciliary beat frequency; NE decreases ciliary beat and upregulates MUC5AC, increasing mucus viscosity. Goblet cell hyperplasia/metaplasia and dehydrated, hyperconcentrated mucus (MUC5AC/MUC5B) further impair clearance (keir2021pathophysiologyofbronchiectasis pages 3-4, keir2021pathophysiologyofbronchiectasis pages 2-3).
  - Ion transport abnormalities contribute: ENaC hyperactivity (SCNN1A) dehydrates the airway surface liquid, while CFTR’s modulatory role on ENaC links to mucus hydration even in non‑CF bronchiectasis (debated) (keir2021pathophysiologyofbronchiectasis pages 3-4).

- Infection and microbiome dysbiosis
  - The stable-state airway microbiome shows reduced alpha diversity and Proteobacteria dominance; Pseudomonas aeruginosa and Haemophilus influenzae are frequent and associate with worse outcomes (exacerbations, lung function decline, mortality). Bronchiectasis cohorts report P. aeruginosa in 15–50% by sputum identification; chronic infection can reach 8–32% with eradication response often waning over 12 months (e.g., prospective tobramycin/colistin eradication 90.9%/61.2% at 1–3 months dropping to 76.5%/40.3% at 12 months) (perea2024pathophysiologyandgenomics pages 2-3, aogain2024infectionandthe pages 1-2, aogain2024infectionandthe pages 4-5, aogain2024infectionandthe pages 6-7).
  - In bronchiectasis with fixed airflow obstruction (FAO), 16S rRNA BAL sequencing demonstrates lower diversity and Proteobacteria enrichment compared with COPD; P. aeruginosa correlates with higher IL‑1β, IL‑8, TNF‑α and greater severity/exacerbation risk (Respiratory Research, 2024-08; doi:10.1186/s12931-024-02931-x) (chen2024theclinicalimpacts pages 1-2).

- Neutrophil-driven inflammation, NETs, and proteases
  - NETs: Overabundant NETs (extracellular DNA/histones + NE/MPO) are associated with higher disease severity, exacerbations, and mortality; NET-associated proteins (MPO, NE, resistin, azurocidin) identify severe endotypes, and NETs decrease with intravenous antibiotics and macrolides in observational cohorts (European Respiratory Review, 2024-07; doi:10.1183/16000617.0234-2023) (johnson2024biomarkersinbronchiectasis pages 3-4, aogain2024infectionandthe pages 4-5).
  - NE as a mechanistic biomarker: “High NE activity in sputum is associated with severe bronchiectasis, risk and frequency of exacerbations, airway bacterial load, and treatment response” (European Respiratory Review, 2024-07; doi:10.1183/16000617.0055-2024) (perea2024pathophysiologyandgenomics pages 2-3). Point-of-care NE activity (NEATstik) stratifies future exacerbation risk (johnson2024biomarkersinbronchiectasis pages 3-4, chalmers2025neutrophilicinflammationin pages 9-10).
  - Other NSPs: PR3 rises in exacerbations and correlates with NE; CatG induces ciliary dysfunction and epithelial destruction; low SLPI (antiprotease) associates with severity, infection, and exacerbation risk (perea2024pathophysiologyandgenomics pages 2-3).

- Inflammasome/IL‑1β axis and epithelial barrier dysfunction
  - “A subset of stable bronchiectasis patients show increased airway IL‑1β,” with higher caspase‑1 activity and Th1/Th2/neutrophilic responses, Proteobacteria-enriched microbiome, increased mucus solid content/viscoelasticity, and worse severity; IL‑1β exposure in primary airway epithelial cultures reduces ciliary function and tight-junction integrity (European Respiratory Journal, 2024‑05; doi:10.1183/13993003.01966-2023) (chen2024theclinicalimpacts pages 1-2). These data functionally link inflammasome activation to mucus hyperconcentration and epithelial barrier impairment in bronchiectasis.

- Protease–antiprotease imbalance and therapeutic validation
  - Excess free NSP activity (NE, PR3, CatG) over antiproteases (e.g., SLPI, A1AT) drives matrix degradation, ciliary dysfunction, and mucus abnormalities. Mechanistic validation: dipeptidyl peptidase‑1 (DPP‑1/cathepsin C) inhibition (e.g., brensocatib) reduces airway NE, PR3, and CatG activity and improves exacerbation outcomes in clinical trials, supporting causality of NSPs (European Respiratory Review, 2024-07; doi:10.1183/16000617.0055-2024) (perea2024pathophysiologyandgenomics pages 2-3).

2) Key molecular players
- Genes/Proteins (HGNC where applicable)
  - ELANE (neutrophil elastase), PRTN3 (proteinase 3), CTSG (cathepsin G), CTSC (DPP‑1/cathepsin C): central to neutrophil-mediated tissue injury; clinically linked to severity/exacerbations; DPP‑1 inhibition validated in trials (perea2024pathophysiologyandgenomics pages 2-3, chalmers2025neutrophilicinflammationin pages 9-10).
  - Cytokines/chemoattractants: IL‑1β (inflammasome product), CXCL8/IL‑8, TNF‑α, LTB4; IL‑17 axis contributes to neutrophilic recruitment and chronicity (keir2021pathophysiologyofbronchiectasis pages 3-4, aogain2024infectionandthe pages 1-2, chalmers2025neutrophilicinflammationin pages 9-10, chen2024theclinicalimpacts pages 1-2).
  - Mucins/ion channels: MUC5AC, MUC5B, CFTR, ENaC (SCNN1A) influence mucus rheology and airway surface liquid (keir2021pathophysiologyofbronchiectasis pages 3-4).

- Chemical entities (CHEBI)
  - cfDNA (component of NETs) increases sputum viscoelasticity; target of DNase in related airway diseases (johnson2024biomarkersinbronchiectasis pages 3-4).
  - LTB4 (neutrophil chemoattractant) and macrolides (e.g., azithromycin) with antimicrobial/immunomodulatory effects; hypertonic saline (sodium chloride) for mucus hydration (aogain2024infectionandthe pages 1-2, johnson2024biomarkersinbronchiectasis pages 3-4, aogain2024infectionandthe pages 6-7).

- Cell types (CL)
  - Neutrophils (NETosis, degranulation), airway epithelial cells (barrier, mucociliary apparatus), goblet cells (mucus production), macrophages (resolution vs. propagation) (keir2021pathophysiologyofbronchiectasis pages 3-4, perea2024pathophysiologyandgenomics pages 2-3, johnson2024biomarkersinbronchiectasis pages 3-4, chalmers2025neutrophilicinflammationin pages 9-10).

- Anatomical locations (UBERON)
  - Conducting airways/bronchi, airway surface liquid, mucus layer, extracellular space; regional disease often corresponds to lobes/segments with dominant pathogens (e.g., Pseudomonas) (chalmers2025neutrophilicinflammationin pages 9-10).

3) Biological processes (for GO annotation)
- Disrupted processes
  - Mucociliary clearance (impaired), cilium movement (reduced beat frequency), neutrophil degranulation, NET formation, inflammatory response, epithelial barrier (tight junction) integrity (keir2021pathophysiologyofbronchiectasis pages 3-4, perea2024pathophysiologyandgenomics pages 2-3, johnson2024biomarkersinbronchiectasis pages 3-4, chen2024theclinicalimpacts pages 1-2).
- Signaling pathways
  - IL‑1 inflammasome (caspase‑1 → IL‑1β), IL‑17 axis (Type‑17 responses), chemokine signaling (CXCL8/IL‑8), lipid mediator signaling (LTB4/TNF‑α) (keir2021pathophysiologyofbronchiectasis pages 3-4, aogain2024infectionandthe pages 1-2, chen2024theclinicalimpacts pages 1-2).

4) Cellular components (GO)
- Key components
  - Azurophil granules (neutrophil protease stores), extracellular space (NETs/cfDNA/proteases), tight junctions (epithelial barrier), cilia/axoneme (motility apparatus) (perea2024pathophysiologyandgenomics pages 2-3, johnson2024biomarkersinbronchiectasis pages 3-4, chalmers2025neutrophilicinflammationin pages 9-10, chen2024theclinicalimpacts pages 1-2).

5) Disease progression and phenotypes
- Sequence of events (typical pathway)
  - Initial insult (e.g., infection) → epithelial injury and impaired mucociliary clearance → mucus retention → microbial colonization/dysbiosis (Proteobacteria dominance) → neutrophil recruitment (CXCL8, LTB4, TNF‑α) → NETs/NSP release → epithelial barrier disruption, matrix degradation, mucus hyperconcentration → airway remodeling/bronchial dilatation → exacerbation-prone state; processes operate as a “vicious vortex” with feedback loops (keir2021pathophysiologyofbronchiectasis pages 2-2, perea2024pathophysiologyandgenomics pages 2-3, aogain2024infectionandthe pages 1-2, chen2024theclinicalimpacts pages 1-2).
- Stages/Endophenotypes
  - Frequent exacerbator phenotype and chronic P. aeruginosa infection correlate with worse outcomes (mortality/severe exacerbations) (johnson2024biomarkersinbronchiectasis pages 1-2, aogain2024infectionandthe pages 6-7).
  - Eosinophilic endotype in a subset (not the focus here) (keir2021pathophysiologyofbronchiectasis pages 1-2).
  - Bronchiectasis with FAO: Proteobacteria-predominant microbiome and higher neutrophilic cytokines (IL‑1β, IL‑8, TNF‑α) (chen2024theclinicalimpacts pages 1-2).

6) Phenotypic manifestations (HP terms)
- Chronic productive cough, daily sputum, frequent exacerbations, dyspnea, hemoptysis in some; fixed airflow obstruction may develop; radiological bronchial dilatation (johnson2024biomarkersinbronchiectasis pages 1-2, aogain2024infectionandthe pages 6-7).

Recent developments and latest research (priority 2023–2024)
- Comprehensive 2024 ERS reviews consolidate the “vicious vortex” model and position neutrophil-driven mechanisms and microbiome dysbiosis as central, with precision-medicine direction through biomarker/endotype discovery (European Respiratory Review, 2024-07; doi:10.1183/16000617.0055-2024; 10.1183/16000617.0038-2024; 10.1183/16000617.0234-2023) (perea2024pathophysiologyandgenomics pages 2-3, aogain2024infectionandthe pages 1-2, johnson2024biomarkersinbronchiectasis pages 1-2).
- Inflammasome/IL‑1β: Multicenter cohort (n=269; validation n=53) links high sputum IL‑1β with severe disease, Proteobacteria enrichment, mucus hyperconcentration, and impaired ciliary function/tight junctions; in vitro IL‑1β directly reduces ciliary function and epithelial barrier (European Respiratory Journal, 2024-05; doi:10.1183/13993003.01966-2023) (chen2024theclinicalimpacts pages 1-2). 
- Microbiome-outcome links: Metagenomic resistome profiling in 2024 shows airway resistotypes (RT2 with higher multidrug resistance and P. aeruginosa) associate with worse outcomes and can revert toward favorable RT1 with targeted eradication (AJRCCM, 2024-07; doi:10.1164/rccm.202306-1059oc) (aogain2024infectionandthe pages 6-7). 
- FAO-specific findings: Prospective BAL 16S study (Taiwan, 2024) shows bronchiectasis±FAO clusters are Proteobacteria-enriched and distinct from COPD; P. aeruginosa correlates with IL‑1β/IL‑8/TNF‑α and higher severity/exacerbation risk (Respiratory Research, 2024-08; doi:10.1186/s12931-024-02931-x) (chen2024theclinicalimpacts pages 1-2).

Current applications and real-world implementations
- Airway clearance: Registry data (EMBARC, n=16,723) show only ~52% report regular airway clearance, despite guideline recommendations; use correlates with greater disease severity and sputum volume—highlighting implementation gaps (European Respiratory Journal, 2024-04; doi:10.1183/13993003.01689-2023) (aogain2024infectionandthe pages 6-7).
- Antimicrobials: Culture-directed/inhaled antibiotics for chronic infection; eradication of incident P. aeruginosa is feasible but durability varies, with reductions over 12 months (aogain2024infectionandthe pages 4-5).
- Anti-inflammatory strategies: Long-term macrolides reduce exacerbations and may reduce NET signatures; DPP‑1 inhibition reduces NSP activity and exacerbations, supporting neutrophil-targeted precision therapy (perea2024pathophysiologyandgenomics pages 2-3, johnson2024biomarkersinbronchiectasis pages 1-2, johnson2024biomarkersinbronchiectasis pages 3-4).

Expert opinions and analysis (authoritative sources, 2023–2024)
- “Understanding the bronchiectasis microbiome… has provided key information on the interplay of the microbiome and host immunity, a central feature of disease progression” (European Respiratory Review, 2024-07; doi:10.1183/16000617.0038-2024) (aogain2024infectionandthe pages 1-2).
- “High NE activity in sputum is associated with severe bronchiectasis, risk and frequency of exacerbations, airway bacterial load, and treatment response” (European Respiratory Review, 2024-07; doi:10.1183/16000617.0055-2024) (perea2024pathophysiologyandgenomics pages 2-3).
- “Airway IL‑1β is a marker of severe disease, mucus hyperconcentration, Proteobacteria-dominant microbiome… [and] directly impairs cilia function and epithelial integrity” (European Respiratory Journal, 2024-05; doi:10.1183/13993003.01966-2023) (chen2024theclinicalimpacts pages 1-2).

Relevant statistics and data
- Epidemiology: Prevalence globally is heterogeneous; registry data demonstrate high burden with rising incidence and notable mortality (16–24.8% over 4–5 years in some regions) (European Respiratory Review, 2024-10; doi:10.1183/16000617.0091-2024) (keir2021pathophysiologyofbronchiectasis pages 3-4).
- EMBARC airway clearance management: 16,723 people, mean age 67; 72% expectoration, 52% regular airway clearance; access to specialist physiotherapy is limited and variable across Europe (European Respiratory Journal, 2024-04; doi:10.1183/13993003.01689-2023) (aogain2024infectionandthe pages 6-7).
- Microbiome clinical associations: Pseudomonas/Stenotrophomonas-dominant bacteriomes increased risk of mortality or severe exacerbations in a large cohort; P. aeruginosa presence correlates with higher neutrophilic cytokines and severity in FAO (aogain2024infectionandthe pages 6-7, chen2024theclinicalimpacts pages 1-2).
- NET/NE biomarkers: Observational cohorts link sputum NET complexes and NE activity to exacerbations, lung-function decline, and mortality; macrolides and IV antibiotics reduce NET signals; NEATstik offers risk stratification (johnson2024biomarkersinbronchiectasis pages 3-4).

Structured annotations for knowledge-base population
- Gene/protein annotations (HGNC examples)
  - ELANE (HGNC:3309), PRTN3, CTSG, CTSC; IL1B; CXCL8; MUC5AC; MUC5B; CFTR; SCNN1A.
- Biological processes (GO)
  - GO:0003351 (mucociliary clearance); GO:0003341 (cilium movement); GO:0043312 (neutrophil degranulation); GO:0036348 (NET formation); GO:0006954 (inflammatory response); IL‑1 inflammasome and IL‑17 pathways (as curated processes).
- Cellular components (GO)
  - GO:0042582 (azurophil granule); GO:0005923 (tight junction); GO:0005615 (extracellular space).
- Cell types (CL)
  - CL:0000775 (neutrophil); CL:0002062 (airway epithelial cell); CL:0000160 (goblet cell); CL:0000235 (macrophage).
- Anatomical locations (UBERON)
  - Bronchial/airway structures of the lung; mucus/extracellular compartments.
- Chemical entities (CHEBI)
  - CHEBI:16991 (DNA/cfDNA), CHEBI:15650 (LTB4), CHEBI:2955 (azithromycin), CHEBI:26710 (sodium chloride; hypertonic saline).

Bronchiectasis molecular–cellular map (artifact)
| Entity | Type | Identifier | Primary role in bronchiectasis | Key evidence (DOI, year) |
|---|---|---|---|---|
| ELANE (neutrophil elastase) | Gene/Protein [HGNC] | ELANE (HGNC:3309) | Major neutrophil serine protease; degrades ECM, impairs ciliary function, biomarker of severity and exacerbation risk | 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3); 10.1183/16000617.0234-2023 (2024) (johnson2024biomarkersinbronchiectasis pages 3-4) |
| PRTN3 (proteinase 3) | Gene/Protein [HGNC] | PRTN3 | Neutrophil serine protease released with NE; increases during exacerbations and correlates with NE | 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3) |
| CTSG (cathepsin G) | Gene/Protein [HGNC] | CTSG | NSP linked to ciliary dysfunction and epithelial destruction | 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3) |
| CTSC (DPP1 / cathepsin C) | Gene/Protein [HGNC] | CTSC | Activates NSPs during neutrophil maturation; therapeutic target (DPP1/CatC inhibitors) | 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3) |
| IL1B (Interleukin-1β) | Cytokine | IL1B | Inflammasome-dependent proinflammatory cytokine; associated with mucus hyperconcentration, impaired ciliary/tight-junction function and severe disease | 10.1183/13993003.01966-2023 (2024) (perea2024pathophysiologyandgenomics pages 2-3, chen2024theclinicalimpacts pages 1-2) |
| NLRP3 | Gene/Protein (inflammasome) | NLRP3 | Inflammasome sensor activating caspase-1 → IL-1β release; implicated in airway inflammation | 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3) |
| CXCL8 (IL-8) | Cytokine/chemokine | CXCL8 | Potent neutrophil chemoattractant; drives neutrophilic inflammation and exacerbations | 10.1055/s-0041-1730891 (2021), 10.1183/16000617.0038-2024 (2024) (keir2021pathophysiologyofbronchiectasis pages 3-4, aogain2024infectionandthe pages 1-2) |
| IL17A | Cytokine | IL17A | Type-17 axis promotes neutrophilic recruitment and chronic airway inflammation | 10.1055/s-0041-1730891 (2021), 10.1183/16000617.0179-2024 (2025) (keir2021pathophysiologyofbronchiectasis pages 3-4, chalmers2025neutrophilicinflammationin pages 9-10) |
| MUC5AC | Gene/Protein (mucin) | MUC5AC | Goblet-cell–derived gel-forming mucin; increased expression → mucus hyperconcentration and impaired clearance | 10.1055/s-0041-1730891 (2021), 10.1183/16000617.0055-2024 (2024) (keir2021pathophysiologyofbronchiectasis pages 3-4, perea2024pathophysiologyandgenomics pages 2-3) |
| MUC5B | Gene/Protein (mucin) | MUC5B | Airway mucin contributing to mucus rheology and retention | 10.1055/s-0041-1730891 (2021) (keir2021pathophysiologyofbronchiectasis pages 3-4) |
| CFTR | Gene/Protein | CFTR | Ion transport regulator; altered ion/fluid transport contributes to mucus dehydration and impaired mucociliary clearance (relevance in non-CF bronchiectasis debated) | 10.1055/s-0041-1730891 (2021) (keir2021pathophysiologyofbronchiectasis pages 3-4) |
| SCNN1A (ENaC α) | Gene/Protein | SCNN1A | ENaC overactivity → airway surface dehydration and increased mucus viscosity | 10.1055/s-0041-1730891 (2021) (keir2021pathophysiologyofbronchiectasis pages 3-4) |
| Neutrophil | Cell [CL] | CL:0000775 | Central effector: phagocytosis, degranulation (NE/PR3/CatG), NET formation → protease release, tissue damage, inflammation | 10.1183/16000617.0055-2024 (2024), 10.1183/16000617.0179-2024 (2025) (perea2024pathophysiologyandgenomics pages 2-3, chalmers2025neutrophilicinflammationin pages 9-10) |
| Airway epithelial cell | Cell [CL] | CL:0002062 | Barrier & mucociliary apparatus; target of protease/IL-1β-mediated damage leading to impaired clearance | 10.1055/s-0041-1730891 (2021), 10.1183/16000617.0055-2024 (2024) (keir2021pathophysiologyofbronchiectasis pages 3-4, perea2024pathophysiologyandgenomics pages 2-3) |
| Goblet cell | Cell [CL] | CL:0000160 | Mucin-secreting cell; hyperplasia/metaplasia increases mucus production (MUC5AC/MUC5B) | 10.1055/s-0041-1730891 (2021) (keir2021pathophysiologyofbronchiectasis pages 3-4) |
| Macrophage | Cell [CL] | CL:0000235 | Modulates resolution vs. persistence of inflammation; interacts with NETs and proteases | 10.1183/16000617.0234-2023 (2024) (johnson2024biomarkersinbronchiectasis pages 3-4) |
| NET formation | Process [GO] | GO:0036348 | Extracellular DNA + granule proteins (NE, MPO) formation by neutrophils; linked to protease dispersal, inflammation, severity and exacerbations | 10.1183/16000617.0234-2023 (2024), 10.3390/jcm13082390 (2024) (johnson2024biomarkersinbronchiectasis pages 3-4, chalmers2025neutrophilicinflammationin pages 9-10) |
| Neutrophil degranulation | Process [GO] | GO:0043312 | Release of NE/PR3/CatG from azurophil granules → protease–antiprotease imbalance and tissue injury | 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3) |
| Inflammatory response | Process [GO] | GO:0006954 | Chronic airway inflammation driving exacerbations and remodeling | 10.1055/s-0041-1730891 (2021), 10.1183/16000617.0038-2024 (2024) (keir2021pathophysiologyofbronchiectasis pages 3-4, aogain2024infectionandthe pages 1-2) |
| Mucociliary clearance | Process [GO] | GO:0003351 | Impaired in bronchiectasis (ciliary dysfunction + abnormal mucus) → sputum retention and infection | 10.1055/s-0041-1730891 (2021), 10.1183/16000617.0038-2024 (2024) (keir2021pathophysiologyofbronchiectasis pages 3-4, aogain2024infectionandthe pages 1-2) |
| Cilium movement | Process/Component [GO] | GO:0003341 | Ciliary beat frequency reduced by infection/proteases (pyocyanin, NE) → impaired clearance | 10.1055/s-0041-1730891 (2021) (keir2021pathophysiologyofbronchiectasis pages 3-4) |
| Tight junction | Component [GO] | GO:0005923 | Epithelial barrier structure; disrupted by IL-1β and protease activity causing increased permeability | 10.1183/13993003.01966-2023 (2024), 10.1183/16000617.0055-2024 (2024) (perea2024pathophysiologyandgenomics pages 2-3, johnson2024biomarkersinbronchiectasis pages 3-4) |
| Azurophil granule | Component [GO] | GO:0042582 | Granule storing NE/PR3/CatG; source of extracellular proteases in airways | 10.1183/16000617.0179-2024 (2025), 10.1183/16000617.0055-2024 (2024) (chalmers2025neutrophilicinflammationin pages 9-10, perea2024pathophysiologyandgenomics pages 2-3) |
| Extracellular space | Component [GO] | GO:0005615 | Site of NETs, free proteases and cfDNA in sputum/BAL | 10.1183/16000617.0234-2023 (2024) (johnson2024biomarkersinbronchiectasis pages 3-4) |
| DNA (cell-free DNA / cfDNA) | Chemical [CHEBI] | CHEBI:16991 | Structural component of NETs; contributes to sputum viscoelasticity; target of DNase therapy | 10.1183/23120541.00312-2024 (2024) (chalmers2025neutrophilicinflammationin pages 9-10, johnson2024biomarkersinbronchiectasis pages 3-4) |
| Leukotriene B4 (LTB4) | Chemical [CHEBI] | CHEBI:15650 | Potent neutrophil chemoattractant implicated in recruitment and persistent inflammation | 10.1055/s-0041-1730891 (2021) (keir2021pathophysiologyofbronchiectasis pages 3-4) |
| Azithromycin | Chemical [CHEBI] | CHEBI:2955 | Macrolide with antimicrobial and immunomodulatory effects; reduces exacerbations and can modulate NETs/inflammation | 10.1183/16000617.0038-2024 (2024), 10.1183/16000617.0234-2023 (2024) (aogain2024infectionandthe pages 1-2, johnson2024biomarkersinbronchiectasis pages 3-4) |
| Sodium chloride (hypertonic saline) | Chemical [CHEBI] | CHEBI:26710 | Mucoactive therapy to improve mucus hydration and clearance (airway clearance adjunct) | 10.1183/13993003.01689-2023 (2024) (aogain2024infectionandthe pages 6-7, aogain2024infectionandthe pages 1-2) |


*Table: A concise molecular and cellular mapping of key entities, ontology identifiers, roles in non‑CF bronchiectasis, and primary 2023–2024 evidence citations (DOIs) supporting each entry; useful for ontology annotation and knowledge‑base population. (keir2021pathophysiologyofbronchiectasis pages 3-4, perea2024pathophysiologyandgenomics pages 2-3, aogain2024infectionandthe pages 1-2, johnson2024biomarkersinbronchiectasis pages 3-4, chalmers2025neutrophilicinflammationin pages 9-10, chen2024theclinicalimpacts pages 1-2)*

Evidence items (selected 2023–2024 primary/review sources with URLs and dates)
- Perea L, Faner R, Chalmers JD, Sibila O. Pathophysiology and genomics of bronchiectasis. European Respiratory Review. 2024-07. doi:10.1183/16000617.0055-2024; URL: https://doi.org/10.1183/16000617.0055-2024 (perea2024pathophysiologyandgenomics pages 2-3).
- Mac Aogáin M, Dicker AJ, Mertsch P, Chotirmall SH. Infection and the microbiome in bronchiectasis. European Respiratory Review. 2024-07. doi:10.1183/16000617.0038-2024; URL: https://doi.org/10.1183/16000617.0038-2024 (aogain2024infectionandthe pages 1-2, aogain2024infectionandthe pages 4-5, aogain2024infectionandthe pages 6-7).
- Perea L, et al. Airway IL‑1β is related to disease severity and mucociliary function in bronchiectasis. European Respiratory Journal. 2024-05. doi:10.1183/13993003.01966-2023; URL: https://doi.org/10.1183/13993003.01966-2023 (chen2024theclinicalimpacts pages 1-2).
- Johnson ED, Long MB, Chalmers JD. Biomarkers in bronchiectasis. European Respiratory Review. 2024-07. doi:10.1183/16000617.0234-2023; URL: https://doi.org/10.1183/16000617.0234-2023 (NET/NE biomarkers) (johnson2024biomarkersinbronchiectasis pages 1-2, johnson2024biomarkersinbronchiectasis pages 3-4).
- Aogáin MM, et al. Airway “Resistotypes” and Clinical Outcomes in Bronchiectasis. American Journal of Respiratory and Critical Care Medicine. 2024-07. doi:10.1164/rccm.202306-1059oc; URL: https://doi.org/10.1164/rccm.202306-1059oc (aogain2024infectionandthe pages 6-7).
- Chen Y‑F, et al. Clinical impacts of lung microbiome in bronchiectasis with FAO. Respiratory Research. 2024-08. doi:10.1186/s12931-024-02931-x; URL: https://doi.org/10.1186/s12931-024-02931-x (chen2024theclinicalimpacts pages 1-2).
- Spinou A, et al. Airway clearance management in EMBARC. European Respiratory Journal. 2024-04. doi:10.1183/13993003.01689-2023; URL: https://doi.org/10.1183/13993003.01689-2023 (aogain2024infectionandthe pages 6-7).
- Keir HR, Chalmers JD. Pathophysiology of Bronchiectasis. Seminars in Respiratory and Critical Care Medicine. 2021-07. doi:10.1055/s-0041-1730891; URL: https://doi.org/10.1055/s-0041-1730891 (foundational model/mechanisms) (keir2021pathophysiologyofbronchiectasis pages 2-2, keir2021pathophysiologyofbronchiectasis pages 3-4, keir2021pathophysiologyofbronchiectasis pages 1-2, keir2021pathophysiologyofbronchiectasis pages 2-3).

Pathophysiology description (concise knowledge-base narrative)
Non‑CF bronchiectasis arises from a self-sustaining “vicious vortex” of mucociliary dysfunction, persistent infection with Proteobacteria-dominant dysbiosis (notably Pseudomonas aeruginosa), and chronic neutrophil-driven inflammation that releases proteases and NETs, injuring the epithelium and altering mucus rheology, thereby worsening clearance and perpetuating infection. Inflammasome activation with airway IL‑1β links to higher severity, mucus hyperconcentration, epithelial barrier dysfunction, and Proteobacteria enrichment. Excess NSP activity (NE, PR3, CatG) over antiproteases is a causative axis, validated by clinical benefit of DPP‑1 inhibition that reduces airway protease activity and exacerbations. Clinically, frequent exacerbators and those with chronic P. aeruginosa have worse outcomes; airway clearance use remains suboptimal despite guideline recommendations (keir2021pathophysiologyofbronchiectasis pages 2-2, perea2024pathophysiologyandgenomics pages 2-3, aogain2024infectionandthe pages 1-2, johnson2024biomarkersinbronchiectasis pages 1-2, johnson2024biomarkersinbronchiectasis pages 3-4, aogain2024infectionandthe pages 6-7, chen2024theclinicalimpacts pages 1-2).

References

1. (keir2021pathophysiologyofbronchiectasis pages 2-2): Holly R. Keir and James D. Chalmers. Pathophysiology of bronchiectasis. Seminars in Respiratory and Critical Care Medicine, 42:499-512, Jul 2021. URL: https://doi.org/10.1055/s-0041-1730891, doi:10.1055/s-0041-1730891. This article has 81 citations and is from a peer-reviewed journal.

2. (keir2021pathophysiologyofbronchiectasis pages 1-2): Holly R. Keir and James D. Chalmers. Pathophysiology of bronchiectasis. Seminars in Respiratory and Critical Care Medicine, 42:499-512, Jul 2021. URL: https://doi.org/10.1055/s-0041-1730891, doi:10.1055/s-0041-1730891. This article has 81 citations and is from a peer-reviewed journal.

3. (chalmers2025neutrophilicinflammationin pages 1-2): James D. Chalmers, Mark Metersky, Stefano Aliberti, Lucy Morgan, Sebastian Fucile, Melanie Lauterio, and Patrick P. McDonald. Neutrophilic inflammation in bronchiectasis. European Respiratory Review, 34:240179, Apr 2025. URL: https://doi.org/10.1183/16000617.0179-2024, doi:10.1183/16000617.0179-2024. This article has 20 citations and is from a peer-reviewed journal.

4. (perea2024pathophysiologyandgenomics pages 2-3): Lidia Perea, Rosa Faner, James D. Chalmers, and Oriol Sibila. Pathophysiology and genomics of bronchiectasis. European Respiratory Review, 33:240055, Jul 2024. URL: https://doi.org/10.1183/16000617.0055-2024, doi:10.1183/16000617.0055-2024. This article has 29 citations and is from a peer-reviewed journal.

5. (keir2021pathophysiologyofbronchiectasis pages 3-4): Holly R. Keir and James D. Chalmers. Pathophysiology of bronchiectasis. Seminars in Respiratory and Critical Care Medicine, 42:499-512, Jul 2021. URL: https://doi.org/10.1055/s-0041-1730891, doi:10.1055/s-0041-1730891. This article has 81 citations and is from a peer-reviewed journal.

6. (keir2021pathophysiologyofbronchiectasis pages 2-3): Holly R. Keir and James D. Chalmers. Pathophysiology of bronchiectasis. Seminars in Respiratory and Critical Care Medicine, 42:499-512, Jul 2021. URL: https://doi.org/10.1055/s-0041-1730891, doi:10.1055/s-0041-1730891. This article has 81 citations and is from a peer-reviewed journal.

7. (aogain2024infectionandthe pages 1-2): Micheál Mac Aogáin, Alison J. Dicker, Pontus Mertsch, and Sanjay H. Chotirmall. Infection and the microbiome in bronchiectasis. European Respiratory Review, 33:240038, Jul 2024. URL: https://doi.org/10.1183/16000617.0038-2024, doi:10.1183/16000617.0038-2024. This article has 24 citations and is from a peer-reviewed journal.

8. (aogain2024infectionandthe pages 4-5): Micheál Mac Aogáin, Alison J. Dicker, Pontus Mertsch, and Sanjay H. Chotirmall. Infection and the microbiome in bronchiectasis. European Respiratory Review, 33:240038, Jul 2024. URL: https://doi.org/10.1183/16000617.0038-2024, doi:10.1183/16000617.0038-2024. This article has 24 citations and is from a peer-reviewed journal.

9. (aogain2024infectionandthe pages 6-7): Micheál Mac Aogáin, Alison J. Dicker, Pontus Mertsch, and Sanjay H. Chotirmall. Infection and the microbiome in bronchiectasis. European Respiratory Review, 33:240038, Jul 2024. URL: https://doi.org/10.1183/16000617.0038-2024, doi:10.1183/16000617.0038-2024. This article has 24 citations and is from a peer-reviewed journal.

10. (chen2024theclinicalimpacts pages 1-2): Yen-Fu Chen, Hsin-Han Hou, Ning Chien, Kai-Zen Lu, Chieh-Hua Lin, Yu-Chieh Liao, Kuo-Lung Lor, Jung-Yien Chien, Chung-Ming Chen, Chung-Yu Chen, Shih-Lung Cheng, Hao-Chien Wang, Po-Ren Hsueh, and Chong-Jen Yu. The clinical impacts of lung microbiome in bronchiectasis with fixed airflow obstruction: a prospective cohort study. Respiratory Research, Aug 2024. URL: https://doi.org/10.1186/s12931-024-02931-x, doi:10.1186/s12931-024-02931-x. This article has 6 citations and is from a domain leading peer-reviewed journal.

11. (johnson2024biomarkersinbronchiectasis pages 3-4): Emma D Johnson, Merete B. Long, and James D. Chalmers. Biomarkers in bronchiectasis. European Respiratory Review, 33:230234, Jul 2024. URL: https://doi.org/10.1183/16000617.0234-2023, doi:10.1183/16000617.0234-2023. This article has 17 citations and is from a peer-reviewed journal.

12. (chalmers2025neutrophilicinflammationin pages 9-10): James D. Chalmers, Mark Metersky, Stefano Aliberti, Lucy Morgan, Sebastian Fucile, Melanie Lauterio, and Patrick P. McDonald. Neutrophilic inflammation in bronchiectasis. European Respiratory Review, 34:240179, Apr 2025. URL: https://doi.org/10.1183/16000617.0179-2024, doi:10.1183/16000617.0179-2024. This article has 20 citations and is from a peer-reviewed journal.

13. (johnson2024biomarkersinbronchiectasis pages 1-2): Emma D Johnson, Merete B. Long, and James D. Chalmers. Biomarkers in bronchiectasis. European Respiratory Review, 33:230234, Jul 2024. URL: https://doi.org/10.1183/16000617.0234-2023, doi:10.1183/16000617.0234-2023. This article has 17 citations and is from a peer-reviewed journal.