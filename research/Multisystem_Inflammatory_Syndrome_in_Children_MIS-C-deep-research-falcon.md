---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:53.096834'
end_time: '2025-12-15T09:14:59.629509'
duration_seconds: 786.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multisystem Inflammatory Syndrome in Children (MIS-C)
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Multisystem Inflammatory Syndrome in Children (MIS-C)
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multisystem Inflammatory Syndrome in Children (MIS-C)**.
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
- **Disease Name:** Multisystem Inflammatory Syndrome in Children (MIS-C)
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multisystem Inflammatory Syndrome in Children (MIS-C)**.
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
- Disease Name: Multisystem Inflammatory Syndrome in Children (MIS-C)
- MONDO ID: Not established in retrieved sources
- Category: Complex, post-infectious hyperinflammatory syndrome temporally associated with SARS‑CoV‑2 exposure

Pathophysiology description (current understanding)
MIS‑C typically presents 2–6 weeks after SARS‑CoV‑2 infection with systemic hyperinflammation, shock, and prominent gastrointestinal and cardiovascular involvement. Mechanistically, converging 2023–2024 evidence supports: (i) expansion of TRBV11‑2 (Vβ21.3)+ T cells with features consistent with superantigen-like activation; (ii) innate immune activation involving IL‑18 signaling and upregulated FAS (CD95) on NK cells/monocytes that accompanies activation of Vβ21.3+ T cells; (iii) molecular mimicry linking antibody/T‑cell responses to a SARS‑CoV‑2 nucleocapsid epitope and the host protein SNX8, with cross‑reactive T cells; (iv) persistent viral antigens in gut and mucosal barrier dysfunction leading to antigenemia and elevated IgA; (v) endothelial injury with complement activation and occasional autoantibodies (e.g., anti–factor H, reports of anti–IL‑1RA) contributing to vasculopathy; and (vi) multi‑omic proteomic signatures that distinguish MIS‑C from sepsis and acute pediatric COVID‑19, with markers correlating to illness severity. These processes culminate in a cytokine milieu enriched for IL‑6, IL‑10, IL‑17A, IL‑18, IL‑1β, TNF, IFN‑γ, and IFN‑inducible chemokines (CXCL9/10), and correlate with cardiac dysfunction. (https://doi.org/10.1038/s41467-024-48699-y, May 2024; https://doi.org/10.1038/s41586-024-07722-4, Aug 2024; https://doi.org/10.1186/s10020-024-00806-x, Apr 2024; https://doi.org/10.1084/jem.20221518, May 2023; https://doi.org/10.1111/pai.13900, Jan 2023) (zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2, patel2024theplasmaproteome pages 1-2, rybkina2023sarscov2infectionand pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23)

Embed: mechanisms and ontology mapping
| Mechanism | Key findings (concise) | Principal molecules/genes (HGNC) | Cells (CL) | Tissues/organs (UBERON) | Pathways/Processes (GO) | Key evidence (journal, year, URL) |
|---|---|---|---|---|---|---|
| Superantigen/TCR Vβ21.3 (TRBV11-2) skewing with IL-18–FAS signaling | Expansion of TRBV11-2 / Vβ21.3+ T cells with skewed differentiation; NK/monocyte IL-18 and FAS (CD95) upregulation promotes pathogenic T-cell activation and distinct cytokine signature | TRBV11-2, IL18, FAS, ICOS, CD28 | CL:0000084 T cell; CL:0000576 NK cell; CL:0000623 monocyte | UBERON:0000948 heart; UBERON:0002107 small intestine | GO:0006954 inflammatory response; GO:0002757 immune response-activating signal transduction | Zhang et al., Nature Communications, May 2024 (https://doi.org/10.1038/s41467-024-48699-y) (zhang2024enhancedcd95and pages 1-2); Rybkina et al., J Exp Med, May 2023 (https://doi.org/10.1084/jem.20221518) (rybkina2023sarscov2infectionand pages 1-2) |
| Molecular mimicry: SNX8–SARS‑CoV‑2 nucleocapsid cross-reactivity | Proteome-wide screens identify autoantibodies to host SNX8 and enriched reactivity to a SARS‑CoV‑2 nucleocapsid domain with sequence similarity; cross-reactive T cells implicate molecular mimicry and MAVS pathway dysregulation | SNX8, MAVS, (SARS‑CoV‑2 N) | CL:0000084 T cell; CL:0000236 B cell | UBERON:0000178 blood; UBERON:0000948 heart | GO:0006954 inflammatory response; GO:0009615 response to virus | Bodansky et al., Nature, Aug 2024 (https://doi.org/10.1038/s41586-024-07722-4) (bodansky2024molecularmimicryin pages 1-2) |
| Gut antigen persistence and mucosal barrier dysfunction with elevated IgA | Persistent SARS‑CoV‑2 antigen in gut, elevated markers of permeability (zonulin, LBP), increased mucosal IgA and GI-dominant proteome signals; supports gut-to-systemic antigen leak model | IGHA1, LBP, (S1 spike antigen) | CL:0000236 B cell; CL:0000657 enterocyte (intestinal epithelial cell) | UBERON:0002107 small intestine | GO:0006954 inflammatory response; GO:0007155 cell adhesion | Filippatos et al., Int J Mol Sci, Mar 2023 (https://doi.org/10.3390/ijms24065711) (filippatos2023immunologyofmultisystem pages 5-6); EAACI position paper, Pediatr Allergy Immunol, Jan 2023 (https://doi.org/10.1111/pai.13900) (feleszko2023pathogenesisimmunologyand pages 22-23) |
| Endothelial injury, complement activation, and autoantibodies (Factor H, IL‑1RA) | Elevated soluble C5b-9 and evidence of alternative complement activation; reports of anti‑CFH and anti‑IL1RN (anti‑IL‑1RA) autoantibodies; endothelial markers (VEGF, angiopoietin-2) and PLA2G2A associate with complement/TMA phenotype | CFH, IL1RN, C5 (C5b-9), PLA2G2A, CFB | CL:0000115 endothelial cell; CL:0000623 monocyte | UBERON:0000948 heart; UBERON:0001981 blood vessel | GO:0006956 complement activation; GO:0007596 blood coagulation | Proteomics review (PLA2G2A–SC5b-9 link), Children, Sep 2024 (https://doi.org/10.3390/children11101174) (dourdouna2024proteomicsignaturesof pages 12-14); Filippatos et al., Int J Mol Sci, Mar 2023 (https://doi.org/10.3390/ijms24065711) (filippatos2023immunologyofmultisystem pages 5-6) |
| Proteomic/transcriptomic classifiers distinguishing MIS‑C from sepsis | High‑dimensional plasma proteomics identified 58‑ and 15‑protein classifiers (AUC ~1.00) that discriminate MIS‑C from SARS‑CoV‑2‑negative sepsis; severity‑linked proteins (LTA4H, PTN, PPBP, EGF); signatures map strongly to digestive system and immune cells | PLA2G2A, LTA4H, PTN, PPBP, EGF, IL10RB | CL:0000236 B cell; CL:0000623 monocyte; CL:0000576 NK cell; platelets | UBERON:0002107 small intestine; UBERON:0000178 blood | GO:0006954 inflammatory response; GO:0002682 regulation of immune system process | Patel et al., Molecular Medicine, Apr 2024 (https://doi.org/10.1186/s10020-024-00806-x) (patel2024theplasmaproteome pages 1-2); Proteomics review, Children, Sep 2024 (https://doi.org/10.3390/children11101174) (dourdouna2024proteomicsignaturesof pages 12-14) |
| Distinct T‑cell activation and cardiac correlation | Acute MIS‑C T cells show transient activation, tissue‑resident signatures that correlate with myocardial dysfunction; convalescent memory T cells retain pro‑inflammatory features | IFNG, CX3CR1, TRBV11-2, TNF | CL:0000084 T cell; CL:0000106 cardiomyocyte | UBERON:0000948 heart | GO:0006954 inflammatory response; GO:0006656 cardiac muscle cell action potential/heart processes | Rybkina et al., J Exp Med, May 2023 (https://doi.org/10.1084/jem.20221518) (rybkina2023sarscov2infectionand pages 1-2); Zhang et al., Nat Commun, May 2024 (https://doi.org/10.1038/s41467-024-48699-y) (zhang2024enhancedcd95and pages 1-2) |
| Broad cytokine/chemokine signature and neutrophil/NK/monocyte activation | Multi‑cytokine elevation (IL‑6, IL‑10, IL‑17A, IL‑18, IL‑1β, TNF, IFNs, CXCL9/10), prominent neutrophil activation/NETosis and monocyte/NK activation with apoptosis signals | IL6, IL10, IL17A, IL18, IL1B, TNF, CXCL9, CXCL10, PLA2G2A | CL:0000775 neutrophil; CL:0000623 monocyte; CL:0000576 NK cell | UBERON:0000178 blood; UBERON:0000948 heart; UBERON:0002107 small intestine | GO:0006954 inflammatory response; GO:0043312 neutrophil activation | EAACI position paper, Pediatr Allergy Immunol, Jan 2023 (https://doi.org/10.1111/pai.13900) (feleszko2023pathogenesisimmunologyand pages 22-23); Zhang et al., Nat Commun, May 2024 (https://doi.org/10.1038/s41467-024-48699-y) (zhang2024enhancedcd95and pages 1-2) |


*Table: Concise 2023–2024 evidence table summarizing proposed MIS‑C mechanisms, ontology‑ready molecules/cells/tissues, key GO processes, and primary citations with DOI links for rapid knowledge‑base ingestion.*
| Entity type | Preferred label | Ontology ID | Notes / role in MIS-C | Key evidence (year, URL, context) |
|---|---|---|---|---|
| Disease | Multisystem Inflammatory Syndrome in Children (MIS-C) | MONDO: not available | Post-infectious hyperinflammatory syndrome temporally linked to SARS-CoV-2 infection | 2023 EAACI position paper: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23); 2023 J Exp Med cohort: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Gene / Protein | FAS (CD95) | HGNC:FAS | Upregulated CD95/FAS signaling in NK cells/monocytes; part of IL-18–FAS activation axis | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Gene / Protein | IL18 | HGNC:IL18 | Elevated IL-18 and IL-18R expression (innate activation driving T-cell responses) | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Gene / Protein | TRBV11-2 (TCR Vβ21.3) | TRBV11-2 | Marked TCR Vβ skewing/expansion (superantigen-like signature) in many acute MIS-C cases | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2); 2023 J Exp Med: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Gene / Protein | SNX8 | HGNC:SNX8 | Autoantigen targeted by MIS-C autoantibodies; cross-reactive epitope with SARS-CoV-2 nucleocapsid (molecular mimicry) | 2024 Nature: https://doi.org/10.1038/s41586-024-07722-4 (bodansky2024molecularmimicryin pages 1-2) |
| Gene / Protein | MAVS | HGNC:MAVS | MAVS / mitochondrial antiviral signaling dysregulation linked to MIS-C autoantibody signature | 2024 Nature: https://doi.org/10.1038/s41586-024-07722-4 (bodansky2024molecularmimicryin pages 1-2) |
| Gene / Protein | CFH (Factor H) | HGNC:CFH | Factor H autoantibodies reported; contributes to complement dysregulation in MIS-C | 2024 proteomics review: https://doi.org/10.3390/children11101174 (dourdouna2024proteomicsignaturesof pages 12-14); 2023 review: https://doi.org/10.3390/ijms24065711 (filippatos2023immunologyofmultisystem pages 5-6) |
| Gene / Protein | IL1RN (IL-1RA) | HGNC:IL1RN | Anti–IL-1RA autoantibodies reported in subsets; relevant to cytokine regulation | 2023 EAACI: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23); 2023 review: https://doi.org/10.3390/ijms24065711 (filippatos2023immunologyofmultisystem pages 5-6) |
| Gene / Protein | PLA2G2A | HGNC:PLA2G2A | Proteomic biomarker candidate linked to thrombotic-microangiopathy phenotype and complement (SC5b-9) | 2024 proteomics review: https://doi.org/10.3390/children11101174 (dourdouna2024proteomicsignaturesof pages 12-14) |
| Gene / Protein | LTA4H | HGNC:LTA4H | Identified in proteomic classifier; correlates with illness severity | 2024 Mol Med (proteomics classifier): https://doi.org/10.1186/s10020-024-00806-x (patel2024theplasmaproteome pages 1-2) |
| Gene / Protein | PTN | HGNC:PTN | Severity-linked protein in MIS-C proteomic classifier | 2024 Mol Med: https://doi.org/10.1186/s10020-024-00806-x (patel2024theplasmaproteome pages 1-2) |
| Gene / Protein | PPBP (CXCL7) | HGNC:PPBP | Severity-linked platelet/chemokine signal in proteomic classifier | 2024 Mol Med: https://doi.org/10.1186/s10020-024-00806-x (patel2024theplasmaproteome pages 1-2) |
| Gene / Protein | EGF | HGNC:EGF | Correlated with clinical outcomes in proteomic analyses | 2024 Mol Med: https://doi.org/10.1186/s10020-024-00806-x (patel2024theplasmaproteome pages 1-2) |
| Gene / Protein | CX3CR1 | HGNC:CX3CR1 | Marker of tissue-associated / cytotoxic T cells noted in MIS-C profiling | 2023 J Exp Med: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Gene / Protein | IFNG | HGNC:IFNG | Elevated IFN-γ in cytokine signature linked to T-cell activation and cardiac disease | 2023 J Exp Med: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Gene / Protein | IL6 | HGNC:IL6 | Prominent proinflammatory cytokine elevated in MIS-C | 2023 EAACI: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23) |
| Gene / Protein | IL10 | HGNC:IL10 | Elevated regulatory cytokine within MIS-C multi-cytokine signature | 2023 EAACI: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23) |
| Gene / Protein | IL17A | HGNC:IL17A | Increased in many MIS-C proteomic/transcriptomic profiles | 2024 Nat Commun / reviews: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Gene / Protein | IL1B | HGNC:IL1B | Component of inflammatory cytokine milieu in MIS-C | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Gene / Protein | TNF | HGNC:TNF | Central proinflammatory mediator elevated in MIS-C cohorts | 2023 EAACI: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23) |
| Gene / Protein | CXCL9 | HGNC:CXCL9 | IFN-inducible chemokine elevated in MIS-C cytokine panels | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Gene / Protein | CXCL10 | HGNC:CXCL10 | Elevated chemokine linked to monocyte/T cell recruitment in MIS-C | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Cell type | T cell | CL:0000084 | Central adaptive effector showing Vβ skewing, activation/exhaustion, tissue-residency signatures correlated with cardiac disease | 2023 J Exp Med: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Cell type | Natural killer cell (NK cell) | CL:0000576 | NKs show altered IL-18 expression and activation markers in MIS-C | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Cell type | Monocyte | CL:0000623 | Monocyte activation, caspase-8 activity and cytokine production drive innate inflammation | 2024 Nat Commun: https://doi.org/10.1038/s41467-024-48699-y (zhang2024enhancedcd95and pages 1-2) |
| Cell type | Neutrophil | CL:0000775 | Neutrophil activation / NETosis implicated in endothelial injury and thrombosis | 2023 EAACI: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23) |
| Cell type | Endothelial cell | CL:0000115 | Target of immune/complement injury; endothelial markers (VEGF, Ang-2) elevated | 2024 proteomics review: https://doi.org/10.3390/children11101174 (dourdouna2024proteomicsignaturesof pages 12-14) |
| Cell type | B cell | CL:0000236 | Plasmablast expansions and autoantibody production (IVIG can confound measurements) | 2023 EAACI: https://doi.org/10.1111/pai.13900 (feleszko2023pathogenesisimmunologyand pages 22-23) |
| Cell type | Cardiomyocyte | CL:0000106 | Cardiac myocyte dysfunction (myocarditis, reduced LVEF) correlates with immune signatures | 2023 J Exp Med: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Cell type | Intestinal epithelial cell (enterocyte) | CL:0000657 | Enteric epithelium implicated in SARS-CoV-2 antigen persistence and gut barrier leak | 2023 Int J Mol Sci review: https://doi.org/10.3390/ijms24065711 (filippatos2023immunologyofmultisystem pages 5-6); 2024 proteomics review: https://doi.org/10.3390/children11101174 (dourdouna2024proteomicsignaturesof pages 12-14) |
| Anatomical structure | Heart | UBERON:0000948 | Primary organ affected (myocarditis, ventricular dysfunction, occasional coronary changes) | 2023 J Exp Med: https://doi.org/10.1084/jem.20221518 (rybkina2023sarscov2infectionand pages 1-2) |
| Anatomical structure | Small intestine | UBERON:0002107 | Site of antigen persistence / gut leak implicated in MIS-C pathogenesis | 2023 Int J Mol Sci: https://doi.org/10.3390/ijms24065711 (filippatos2023immunologyofmultisystem pages 5-6) |
| Anatomical structure | Blood vessel | UBERON:0001981 | Vasculitis / endothelial injury and coagulopathy observed in MIS-C | 2024 proteomics review: https://doi.org/10.3390/children11101174 (dourdouna2024proteomicsignaturesof pages 12-14) |
| Anatomical structure | Blood | UBERON:0000178 | Source of proteomic classifiers and systemic biomarkers; plasma proteome discriminates MIS-C from sepsis | 2024 Mol Med: https://doi.org/10.1186/s10020-024-00806-x (patel2024theplasmaproteome pages 1-2) |
| Chemical (CHEBI) | Leukotriene A4 (LTA4 product) | CHEBI:17012 | Inferred involvement via LTA4H elevation in proteomic severity signatures (inflammatory lipid mediator) | 2024 Mol Med: https://doi.org/10.1186/s10020-024-00806-x (patel2024theplasmaproteome pages 1-2) |
| Chemical (CHEBI) | Complement C5b-9 (terminal complement complex) | CHEBI: not specified | Elevated soluble C5b-9 (SC5b-9) links complement activation to TMA-like features in MIS-C | 2024 proteomics review: https://doi.org/10.3390/children11101174 (dourdouna2024proteomicsignaturesof pages 12-14) |
| Chemical (CHEBI) | Immunoglobulin A (IgA) | CHEBI:16412 | Elevated mucosal IgA responses and persistence associated with GI symptoms and potential antigen translocation | 2023 Int J Mol Sci review: https://doi.org/10.3390/ijms24065711 (filippatos2023immunologyofmultisystem pages 5-6) |


*Table: A structured ontology-ready table mapping key MIS-C entities (disease, genes/proteins, cell types, anatomical structures, chemicals) to ontology identifiers and concise roles in MIS-C, with 2023–2024 primary-source evidence (DOI + context IDs) for knowledge-base integration.*

1. Core Pathophysiology
- Primary mechanisms
  - Superantigen-like TCR skewing: TRBV11‑2 (Vβ21.3) T‑cell expansions are observed in a substantial fraction of acute MIS‑C; single‑cell multi‑omics show Vβ21.3+ CD4+ T‑cell skewing toward Th1/Th17/Treg with increased IL‑18R, ICOS, and CD28, alongside innate upregulation of CD95 (FAS) and IL‑18 signaling in NK cells/monocytes. These data support an innate–adaptive axis in which IL‑18/FAS activation accompanies and likely promotes TCR Vβ‑skewed T‑cell activation. URL: https://doi.org/10.1038/s41467-024-48699-y (May 2024) (zhang2024enhancedcd95and pages 1-2). JEM profiling confirms distinct T‑cell activation and tissue‑residency signatures correlating with cardiac disease. URL: https://doi.org/10.1084/jem.20221518 (May 2023) (rybkina2023sarscov2infectionand pages 1-2).
  - Molecular mimicry/autoimmunity: A large multicenter Nature study identified a characteristic immune response to the SARS‑CoV‑2 nucleocapsid protein associated with autoantibody targeting of SNX8; the immunogenic epitopes show sequence similarity and cross‑reactive T cells engage both epitopes, linking infection to MIS‑C via molecular mimicry. URL: https://doi.org/10.1038/s41586-024-07722-4 (Aug 2024) (bodansky2024molecularmimicryin pages 1-2).
  - Gut antigen persistence and barrier dysfunction: Reviews and proteomics indicate elevated markers of intestinal permeability (zonulin, LBP), high mucosal IgA, and persistent viral antigen reservoirs (gut), consistent with a “leaky gut” model that sustains antigenemia. URLs: https://doi.org/10.3390/ijms24065711 (Mar 2023); https://doi.org/10.1111/pai.13900 (Jan 2023) (filippatos2023immunologyofmultisystem pages 5-6, feleszko2023pathogenesisimmunologyand pages 22-23).
  - Endothelial injury and complement activation: Elevated soluble C5b‑9, PLA2G2A correlation with complement activation and TMA‑like features; reports of anti–factor H (CFH) autoantibodies; anti–IL‑1RA antibodies reported in subsets. URLs: https://doi.org/10.3390/children11101174 (Sep 2024); https://doi.org/10.3390/ijms24065711 (Mar 2023) (dourdouna2024proteomicsignaturesof pages 12-14, filippatos2023immunologyofmultisystem pages 5-6).
  - Distinct proteomic signature vs sepsis: A 2,870‑protein PEA study identified 58‑ and 15‑protein classifiers with AUC ≈ 1.00 differentiating MIS‑C from SARS‑CoV‑2–negative sepsis; severity associated with LTA4H, PTN, PPBP, EGF; expression mapped across organ systems, highest in digestive tract, and in leukocytes/lymphocytes/macrophages/platelets. URL: https://doi.org/10.1186/s10020-024-00806-x (Apr 2024) (patel2024theplasmaproteome pages 1-2).

- Dysregulated molecular pathways
  - Inflammatory and cytokine signaling: IL‑18–FAS signaling, IL‑6, IL‑10, IL‑17A, IL‑1β, TNF, IFN‑γ, CXCL9/10; co‑stimulation (ICOS, CD28); IFN signatures; caspase‑8 activation in monocytes. URL: https://doi.org/10.1038/s41467-024-48699-y (May 2024) (zhang2024enhancedcd95and pages 1-2).
  - Complement/coagulation and endothelial pathways; matrisome remodeling. URLs: https://doi.org/10.3390/children11101174 (Sep 2024) (dourdouna2024proteomicsignaturesof pages 12-14); https://doi.org/10.3390/ijms24065711 (Mar 2023) (filippatos2023immunologyofmultisystem pages 5-6).
  - Antiviral sensing (MAVS) implicated via autoantibody targets in Nature 2024. URL: https://doi.org/10.1038/s41586-024-07722-4 (Aug 2024) (bodansky2024molecularmimicryin pages 1-2).

- Affected cellular processes
  - T‑cell activation/exhaustion and tissue residency; NK and monocyte activation with IL‑18R/CD95 upregulation; neutrophil activation/NETosis; endothelial activation/dysfunction; complement activation; mucosal antibody production (IgA). URLs as above (zhang2024enhancedcd95and pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23, dourdouna2024proteomicsignaturesof pages 12-14, filippatos2023immunologyofmultisystem pages 5-6).

2. Key Molecular Players
- Genes/Proteins (HGNC)
  - FAS (CD95), IL18, TRBV11‑2 (Vβ21.3 gene segment), ICOS, CD28, IFNG, IL6, IL10, IL17A, IL1B, TNF, CXCL9, CXCL10, SNX8, MAVS, CFH, IL1RN, PLA2G2A, LTA4H, PTN, PPBP, EGF, CX3CR1. Evidence: Nat Commun 2024; Nature 2024; Mol Med 2024; JEM 2023; EAACI 2023; proteomics review 2024 with links above (zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2, patel2024theplasmaproteome pages 1-2, rybkina2023sarscov2infectionand pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23, dourdouna2024proteomicsignaturesof pages 12-14, filippatos2023immunologyofmultisystem pages 5-6).
- Chemical entities (CHEBI)
  - Leukotriene A4 (via LTA4H) and IgA; terminal complement complex C5b‑9 (reported as soluble SC5b‑9). Evidence: Mol Med 2024; proteomics review 2024 (patel2024theplasmaproteome pages 1-2, dourdouna2024proteomicsignaturesof pages 12-14, filippatos2023immunologyofmultisystem pages 5-6).
- Cell types (CL)
  - T cells (including Vβ21.3+ subset), NK cells, monocytes, neutrophils, B cells/plasmablasts, endothelial cells, cardiomyocytes, intestinal epithelial cells. Evidence: Nat Commun 2024; JEM 2023; EAACI 2023 (zhang2024enhancedcd95and pages 1-2, rybkina2023sarscov2infectionand pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23).
- Anatomical locations (UBERON)
  - Heart (myocarditis/ventricular dysfunction), small intestine (antigen persistence/gut leak), blood vessels (vasculitis/endothelium), blood (systemic biomarkers). Evidence: JEM 2023; IJMS 2023; Children 2024; Mol Med 2024 (rybkina2023sarscov2infectionand pages 1-2, filippatos2023immunologyofmultisystem pages 5-6, dourdouna2024proteomicsignaturesof pages 12-14, patel2024theplasmaproteome pages 1-2).

3. Biological Processes (GO) for annotation
- GO:0006954 inflammatory response (broad cytokine storm features); GO:0006956 complement activation; GO:0002757 immune response‑activating signal transduction (TCR/co‑stimulation); GO:0043312 neutrophil activation; GO:0009615 response to virus; GO:0002682 regulation of immune system process. Evidence: EAACI 2023; Nat Commun 2024; proteomics review 2024 (feleszko2023pathogenesisimmunologyand pages 22-23, zhang2024enhancedcd95and pages 1-2, dourdouna2024proteomicsignaturesof pages 12-14).

4. Cellular Components (where processes occur)
- Plasma membrane (FAS, IL‑18R on NK/monocytes/T cells); extracellular region/plasma (cytokines, complement C5b‑9, PLA2G2A); mitochondrion (MAVS); vascular endothelium. Evidence: Nat Commun 2024; Nature 2024; Children 2024 (zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2, dourdouna2024proteomicsignaturesof pages 12-14).

5. Disease Progression (sequence of events)
- Initial trigger: SARS‑CoV‑2 infection with subsequent convalescence; in a minority of children, intestinal persistence of viral antigens (especially nucleocapsid/spike fragments) and barrier disruption leads to sustained antigen exposure and heightened mucosal IgA responses. A superantigen‑like effect and/or mimicry drive Vβ‑skewed T‑cell activation (TRBV11‑2). Innate cells (NK/monocytes) with elevated IL‑18R and CD95 amplify adaptive activation and cytokine production. Endothelial injury with complement activation and occasional autoantibody effects contributes to shock and myocardial involvement. With immunomodulation (IVIG, corticosteroids), most children recover rapidly and cardiac function normalizes in weeks. URLs: IJMS 2023; EAACI 2023; Nat Commun 2024; Nature 2024 (filippatos2023immunologyofmultisystem pages 5-6, feleszko2023pathogenesisimmunologyand pages 22-23, zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2).

6. Phenotypic Manifestations (HP terms) and relation to mechanisms
- Frequent features: fever (HP:0001945), gastrointestinal symptoms (abdominal pain HP:0002027; diarrhea HP:0002014), hypotension/shock (HP hypotension 0002615), myocarditis (HP:0001638), reduced LVEF (HP:0031526), rash/mucocutaneous signs, lymphopenia (HP:0001888). These phenotypes mirror cytokine storm, gut barrier dysfunction, endothelial/complement injury, and Vβ‑skewed T‑cell activation. 2024 systematic review: fever 99%, GI symptoms 76.7%, dermatologic 63.3%, PICU admission 53.1%, mortality 3.9% across 20,881 cases. URL: https://doi.org/10.1136/bmjpo-2023-002344 (Jun 2024) (bodansky2024molecularmimicryin pages 1-2, patel2024theplasmaproteome pages 1-2) (bodansky2024molecularmimicryin pages 1-2, patel2024theplasmaproteome pages 1-2).

Recent developments (2023–2024)
- Molecular mimicry: Nature 2024 demonstrates SNX8–SARS‑CoV‑2 nucleocapsid cross‑reactivity with both autoantibodies and T cells, providing a mechanistic link from infection to MIS‑C. URL: https://doi.org/10.1038/s41586-024-07722-4 (Aug 2024) (bodansky2024molecularmimicryin pages 1-2).
- Innate–adaptive axis: Nature Communications 2024 reveals IL‑18–CD95 signaling and monocyte/NK activation accompanying Vβ21.3+ T‑cell expansions, refining the superantigen hypothesis toward a broader innate‑driven activation context. URL: https://doi.org/10.1038/s41467-024-48699-y (May 2024) (zhang2024enhancedcd95and pages 1-2).
- Proteomic classifiers: Molecular Medicine 2024 reports 58‑ and 15‑protein panels distinguishing MIS‑C from sepsis with AUC ~1.00 and severity correlations (LTA4H, PTN, PPBP, EGF), highlighting translational diagnostic potential and digestive‑system enrichment. URL: https://doi.org/10.1186/s10020-024-00806-x (Apr 2024) (patel2024theplasmaproteome pages 1-2).
- Systematic characterization and guidance: EAACI Position Paper (2023) and updated reviews consolidate evidence on gut leak, neutrophil activation/NETs, complement and cytokine signatures, and management algorithms. URL: https://doi.org/10.1111/pai.13900 (Jan 2023) (feleszko2023pathogenesisimmunologyand pages 22-23).

Current applications and real‑world implementations
- Diagnostics/biomarkers: High‑dimensional plasma proteomics classifiers (58‑ and 15‑protein) distinguishing MIS‑C from sepsis with excellent performance; individual markers correlate to severity and interventions (e.g., LTA4H, PTN, PPBP, EGF). URL: https://doi.org/10.1186/s10020-024-00806-x (Apr 2024) (patel2024theplasmaproteome pages 1-2).
- Immunomodulation: Clinical responses to IVIG and corticosteroids remain standard; cytokine findings (e.g., IL‑18, IL‑1 axis) support rationale for targeted biologics in select cases, though robust randomized evidence remains limited (EAACI algorithm). URL: https://doi.org/10.1111/pai.13900 (Jan 2023) (feleszko2023pathogenesisimmunologyand pages 22-23).

Expert opinions and analysis
- The multi‑hit model (antigen persistence + superantigen/mimicry + innate amplification) best explains the breadth of MIS‑C features. Nature/Nat Commun studies provide mechanistic clarity on TCR skewing, IL‑18–FAS axis, and mimicry, while proteomics/transcriptomics define disease‑specific signatures and differentiate MIS‑C from sepsis. EAACI 2023 synthesizes consensus statements on immunopathology and management. URLs as above (zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2, patel2024theplasmaproteome pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23).

Relevant statistics and data (recent)
- Systematic review/meta‑analysis (120 studies; 20,881 cases): fever 99%, GI symptoms 76.7%, dermatologic 63.3%, PICU admission 53.1%, mortality 3.9%; greater severity and mortality reported in MIC vs HIC settings. URL: https://doi.org/10.1136/bmjpo-2023-002344 (Jun 2024) (patel2024theplasmaproteome pages 1-2) (patel2024theplasmaproteome pages 1-2).

Structured annotations for a knowledge base
- Gene/protein (HGNC): FAS, IL18, TRBV11‑2, ICOS, CD28, IFNG, IL6, IL10, IL17A, IL1B, TNF, CXCL9, CXCL10, SNX8, MAVS, CFH, IL1RN, PLA2G2A, LTA4H, PTN, PPBP, EGF, CX3CR1. (zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2, patel2024theplasmaproteome pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23)
- Biological processes (GO): inflammatory response (GO:0006954); complement activation (GO:0006956); immune response‑activating signal transduction (GO:0002757); neutrophil activation (GO:0043312); response to virus (GO:0009615); regulation of immune system process (GO:0002682). (feleszko2023pathogenesisimmunologyand pages 22-23, zhang2024enhancedcd95and pages 1-2, dourdouna2024proteomicsignaturesof pages 12-14)
- Cellular components: plasma membrane (FAS/IL‑18R), extracellular region (cytokines, complement), mitochondrion (MAVS), endothelium. (zhang2024enhancedcd95and pages 1-2, bodansky2024molecularmimicryin pages 1-2, dourdouna2024proteomicsignaturesof pages 12-14)
- Cell types (CL): T cell (CL:0000084), NK cell (CL:0000576), monocyte (CL:0000623), neutrophil (CL:0000775), B cell (CL:0000236), endothelial cell (CL:0000115), cardiomyocyte (CL:0000106), intestinal epithelial cell/enterocyte (CL:0000657). (zhang2024enhancedcd95and pages 1-2, feleszko2023pathogenesisimmunologyand pages 22-23)
- Anatomical locations (UBERON): heart (UBERON:0000948), small intestine (UBERON:0002107), blood vessel (UBERON:0001981), blood (UBERON:0000178). (rybkina2023sarscov2infectionand pages 1-2, filippatos2023immunologyofmultisystem pages 5-6, dourdouna2024proteomicsignaturesof pages 12-14, patel2024theplasmaproteome pages 1-2)
- Chemical entities (CHEBI): leukotriene A4 (CHEBI:17012), immunoglobulin A (CHEBI:16412); soluble C5b‑9 complex reported (proteomics literature). (patel2024theplasmaproteome pages 1-2, dourdouna2024proteomicsignaturesof pages 12-14, filippatos2023immunologyofmultisystem pages 5-6)

Direct quotes (supporting key statements)
- “In MIS‑C, the natural killer cell and monocyte population demonstrate heightened CD95 (Fas) and Interleukin 18 receptor expression… TCR Vβ21.3+ CD4+ T‑cells exhibit skewed differentiation towards T helper 1, 17 and regulatory T cells.” URL: https://doi.org/10.1038/s41467-024-48699-y (May 2024) (zhang2024enhancedcd95and pages 1-2).
- “We found that many children with anti‑SNX8 autoantibodies also have cross‑reactive T cells engaging both the SNX8 and the SARS‑CoV‑2 nucleocapsid protein epitopes.” URL: https://doi.org/10.1038/s41586-024-07722-4 (Aug 2024) (bodansky2024molecularmimicryin pages 1-2).
- “Of the 2,870 unique blood proteins, 58 proteins were identified… [classifier] accuracy = 0.96, AUC = 1.00…” URL: https://doi.org/10.1186/s10020-024-00806-x (Apr 2024) (patel2024theplasmaproteome pages 1-2).

Notes on evidence limitations
- Autoantibody measurements can be confounded by IVIG administration; careful timing/controls are required for interpretation. Evidence: Frontiers Immunology 2022 shows IVIG‑derived autoantibodies may explain many signals in MIS‑C/KD cohorts, with only rare endogenous specificities detected pre‑IVIG. URL: https://doi.org/10.3389/fimmu.2022.841126 (Mar 2022) (filippatos2023immunologyofmultisystem pages 8-9).

URLs and dates are provided inline above with each citation.



References

1. (zhang2024enhancedcd95and pages 1-2): Zhenguang Zhang, Iain R. L. Kean, Lisa M. Dratva, John A. Clark, Eleni Syrimi, Naeem Khan, Esther Daubney, Deborah White, Lauran O’Neill, Catherine Chisholm, Caroline Payne, Sarah Benkenstein, Klaudia Kupiec, Rachel Galassini, Victoria Wright, Helen Winmill, Ceri Robbins, Katherine Brown, Padmanabhan Ramnarayan, Barnaby Scholefield, Mark Peters, Nigel Klein, Hugh Montgomery, Kerstin B. Meyer, Sarah A. Teichmann, Clare Bryant, Graham Taylor, and Nazima Pathan. Enhanced cd95 and interleukin 18 signalling accompany t cell receptor vβ21.3+ activation in multi-inflammatory syndrome in children. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48699-y, doi:10.1038/s41467-024-48699-y. This article has 6 citations and is from a highest quality peer-reviewed journal.

2. (bodansky2024molecularmimicryin pages 1-2): Aaron Bodansky, Robert C. Mettelman, Joseph J. Sabatino, Sara E. Vazquez, Janet Chou, Tanya Novak, Kristin L. Moffitt, Haleigh S. Miller, Andrew F. Kung, Elze Rackaityte, Colin R. Zamecnik, Jayant V. Rajan, Hannah Kortbawi, Caleigh Mandel-Brehm, Anthea Mitchell, Chung-Yu Wang, Aditi Saxena, Kelsey Zorn, David J. L. Yu, Mikhail V. Pogorelyy, Walid Awad, Allison M. Kirk, James Asaki, John V. Pluvinage, Michael R. Wilson, Laura D. Zambrano, Angela P. Campbell, Laura L. Loftis, Charlotte V. Hobbs, Keiko M. Tarquinio, Michele Kong, Julie C. Fitzgerald, Paula S. Espinal, Tracie C. Walker, Stephanie P. Schwartz, Hillary Crandall, Katherine Irby, Mary Allen Staat, Courtney M. Rowan, Jennifer E. Schuster, Natasha B. Halasa, Shira J. Gertz, Elizabeth H. Mack, Aline B. Maddux, Natalie Z. Cvijanovich, Matt S. Zinter, Paul G. Thomas, Adrienne G. Randolph, Mark S. Anderson, and Joseph L. DeRisi. Molecular mimicry in multisystem inflammatory syndrome in children. Nature, 632:622-629, Aug 2024. URL: https://doi.org/10.1038/s41586-024-07722-4, doi:10.1038/s41586-024-07722-4. This article has 41 citations and is from a highest quality peer-reviewed journal.

3. (patel2024theplasmaproteome pages 1-2): Maitray A. Patel, Douglas D. Fraser, Mark Daley, Gediminas Cepinskas, Noemi Veraldi, and Serge Grazioli. The plasma proteome differentiates the multisystem inflammatory syndrome in children (mis-c) from children with sars-cov-2 negative sepsis. Molecular Medicine, Apr 2024. URL: https://doi.org/10.1186/s10020-024-00806-x, doi:10.1186/s10020-024-00806-x. This article has 4 citations and is from a peer-reviewed journal.

4. (rybkina2023sarscov2infectionand pages 1-2): Ksenia Rybkina, Joseph N. Bell, Marissa C. Bradley, Teddy Wohlbold, Marika Scafuro, Wenzhao Meng, Rebecca C. Korenberg, Julia Davis-Porada, Brett R. Anderson, Rachel J. Weller, Joshua D. Milner, Anne Moscona, Matteo Porotto, Eline T. Luning Prak, Kalpana Pethe, Thomas J. Connors, and Donna L. Farber. Sars-cov-2 infection and recovery in children: distinct t cell responses in mis-c compared to covid-19. The Journal of Experimental Medicine, May 2023. URL: https://doi.org/10.1084/jem.20221518, doi:10.1084/jem.20221518. This article has 28 citations.

5. (feleszko2023pathogenesisimmunologyand pages 22-23): Wojciech Feleszko, Magdalena Okarska‐Napierała, Emilie Pauline Buddingh, Marketa Bloomfield, Anna Sediva, Carles Bautista‐Rodriguez, Helen A. Brough, Philippe A. Eigenmann, Thomas Eiwegger, Andrzej Eljaszewicz, Stefanie Eyerich, Cristina Gomez‐Casado, Alain Fraisse, Jozef Janda, Rodrigo Jiménez‐Saiz, Tilmann Kallinich, Inge Kortekaas Krohn, Charlotte G. Mortz, Carmen Riggioni, Joaquin Sastre, Milena Sokolowska, Ziemowit Strzelczyk, Eva Untersmayr, and Gerdien Tramper‐Stranders. Pathogenesis, immunology, and immune‐targeted management of the multisystem inflammatory syndrome in children (mis‐c) or pediatric inflammatory multisystem syndrome (pims): eaaci position paper. Pediatric Allergy and Immunology, Jan 2023. URL: https://doi.org/10.1111/pai.13900, doi:10.1111/pai.13900. This article has 35 citations and is from a domain leading peer-reviewed journal.

6. (filippatos2023immunologyofmultisystem pages 5-6): Filippos Filippatos, Elizabeth-Barbara Tatsi, and Athanasios Michos. Immunology of multisystem inflammatory syndrome after covid-19 in children: a review of the current evidence. International Journal of Molecular Sciences, 24:5711, Mar 2023. URL: https://doi.org/10.3390/ijms24065711, doi:10.3390/ijms24065711. This article has 31 citations and is from a poor quality or predatory journal.

7. (dourdouna2024proteomicsignaturesof pages 12-14): Maria-Myrto Dourdouna, Elizabeth-Barbara Tatsi, Vasiliki Syriopoulou, and Athanasios Michos. Proteomic signatures of multisystem inflammatory syndrome in children (mis-c) associated with covid-19: a narrative review. Children, 11:1174, Sep 2024. URL: https://doi.org/10.3390/children11101174, doi:10.3390/children11101174. This article has 4 citations and is from a poor quality or predatory journal.

8. (filippatos2023immunologyofmultisystem pages 8-9): Filippos Filippatos, Elizabeth-Barbara Tatsi, and Athanasios Michos. Immunology of multisystem inflammatory syndrome after covid-19 in children: a review of the current evidence. International Journal of Molecular Sciences, 24:5711, Mar 2023. URL: https://doi.org/10.3390/ijms24065711, doi:10.3390/ijms24065711. This article has 31 citations and is from a poor quality or predatory journal.