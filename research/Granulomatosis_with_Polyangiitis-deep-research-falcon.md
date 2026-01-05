---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:46:25.057363'
end_time: '2025-12-18T09:53:56.529607'
duration_seconds: 451.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Granulomatosis with Polyangiitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Granulomatosis with Polyangiitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Granulomatosis with Polyangiitis**.
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
- **Disease Name:** Granulomatosis with Polyangiitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Granulomatosis with Polyangiitis**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Granulomatosis with Polyangiitis (GPA)
- MONDO ID: 
- Category: Autoimmune

## Pathophysiology Description (Narrative)
Granulomatosis with polyangiitis is a necrotizing, pauci-immune small-vessel vasculitis within the ANCA-associated vasculitides (AAV), clinically enriched for ENT and pulmonary granulomatous inflammation and often accompanied by glomerulonephritis. Classification and pathobiology are increasingly organized by ANCA serotype rather than eponym, with GPA most often PR3-ANCA positive and biologically distinct from MPO-ANCA vasculitis (MPA) ("Large GWAS demonstrate stronger genetic associations with ANCA serotype than clinical phenotype") (austin2022ancaassociatedvasculitis pages 1-3). Loss of tolerance to neutrophil granule antigens—particularly proteinase 3 (PR3) and myeloperoxidase (MPO)—is central. Cytokines such as TNF and IL-1β and chemoattractants such as C5a “prime” neutrophils, leading to surface translocation of PR3/MPO, enabling ANCA to engage both the antigen and Fcγ receptors. This dual engagement activates Syk-dependent signaling, NADPH oxidase (NOX2)–driven reactive oxygen species, degranulation, and substrate-dependent NETosis, culminating in endothelial injury and small-vessel inflammation (quotes below) (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 1-2, drouzas2025currentunderstandingof pages 1-2).

NETs serve as both effectors of tissue damage and sources of modified autoantigen that perpetuate autoimmunity, forming a feed-forward loop with complement amplification. C5a generated by the alternative pathway primes and recruits neutrophils via C5aR1, which is clinically validated by the steroid-sparing efficacy of C5aR1 blockade during induction (avacopan) (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2). Dendritic cells present antigens (including from NETs) to T cells, providing B-cell help and promoting ANCA-producing plasma cells; reduced/dysfunctional regulatory lymphocytes and heightened Th1/Th17 polarization contribute to granuloma formation in the upper airway and lung (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 2-4). In the kidney, the end result is pauci-immune necrotizing crescentic glomerulonephritis; although “pauci-immune,” immunohistology can show complement products and membrane attack complex in lesions (drouzas2025currentunderstandingof pages 1-2).

Serotype-specific genetics underscore distinct pathogenetic programs. PR3-ANCA disease associates with HLA-DPB1*04:01 and non-HLA loci such as PRTN3 and SERPINA1, whereas MPO-ANCA disease more often associates with HLA-DQ; these differences mirror clinical phenotypes (ENT/granulomatous disease in PR3-ANCA, renal-limited disease in MPO-ANCA) (fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3). Environmental factors—especially nasal microbiome perturbations and Staphylococcus aureus carriage—are implicated in priming and relapse risk in GPA, although eradication strategies show mixed impact on activity in recent cohorts (fouka2024pathogenesisofpulmonary pages 4-5, fouka2024pathogenesisofpulmonary pages 1-2).

## Directly Supported Key Quotes
- “Priming of neutrophils by specific triggers leads to exposition of MPO and PR3 to the membrane… ANCA bind their antigens … but also FcR on the membrane … leading to neutrophil activation.” (Autoimmunity Reviews 2025; URL: https://doi.org/10.1016/j.autrev.2025.103824) (triaille2025theemergingconcept pages 2-3)
- “The pathogenesis of AAV includes ANCA-mediated neutrophil activation … and formation of neutrophil extracellular traps (NETs). Excessive NETs could participate not only in ANCA-mediated vascular injury but also in the production of ANCAs per se as autoantigens.” (Frontiers in Immunology 2023; URL: https://doi.org/10.3389/fimmu.2023.1261151) (shiratoriaso2023theinvolvementof pages 4-5)
- “The alternative complement pathway amplifies this: C5a primes neutrophils for ANCA-induced respiratory burst … linking inflammation to hypercoagulability.” (International Journal of Molecular Sciences 2024; URL: https://doi.org/10.3390/ijms25105278) (fouka2024pathogenesisofpulmonary pages 5-7)
- “PR3-AAV was significantly associated with … HLA-DPB1*04:01 … MPO-AAV was significantly associated with HLA-DRB1*04:04.” (RMD Open 2024; URL: https://doi.org/10.1136/rmdopen-2023-004039) (fouka2024pathogenesisofpulmonary pages 4-5)
- “GWAS demonstrate stronger genetic associations with ANCA serotype than clinical phenotype… PR3-AAV links to HLA-DP, PRTN3 and SERPINA1 variants, whereas MPO-AAV associates with HLA-DQ.” (Journal of Inflammation Research 2022; URL: https://doi.org/10.2147/jir.s284768) (austin2022ancaassociatedvasculitis pages 1-3)
- “Nasal dysbiosis is common in active AAV… Staphylococcus aureus nasal carriage is associated with GPA relapses” (International Journal of Molecular Sciences 2024; URL: https://doi.org/10.3390/ijms25105278) (fouka2024pathogenesisofpulmonary pages 4-5)
- “ANCA-GN is classically ‘pauci-immune’, [but] immunohistology reveals the presence of complement products and membrane attack complex” (Life 2025; URL: https://doi.org/10.3390/life15050756) (drouzas2025currentunderstandingof pages 1-2)
- In a cohort with ENT involvement, “Nasal S. aureus colonization does not influence systemic or local disease activity. Antibiotic treatment aimed at eradication did not modify disease activity.” (Rheumatology International 2023; URL: https://doi.org/10.1007/s00296-022-05228-8) (fouka2024pathogenesisofpulmonary pages 1-2)

## 1. Core Pathophysiology
- Primary mechanisms: ANCA (typically PR3-ANCA in GPA) bind primed neutrophils and Fcγ receptors, inducing Syk-dependent activation, degranulation, ROS production, and NETosis; NETs perpetuate antigen exposure and complement activation, leading to endothelial injury and necrotizing small-vessel vasculitis with granulomatous inflammation in ENT/lung and pauci-immune GN in kidney (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2, fouka2024pathogenesisofpulmonary pages 1-2).
- Dysregulated pathways: Alternative complement pathway (C5→C5a–C5aR1 axis) that primes neutrophils; Th1/Th17 skewing; BAFF-driven B-cell activation sustaining ANCA production; adhesion/integrin signaling enabling substrate-dependent NETosis (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 2-4).
- Affected cellular processes: Neutrophil activation and oxidative burst; NET formation (PAD4-dependent chromatin decondensation); antigen presentation from NET-derived cargo; endothelial adhesion/diapedesis; granuloma organization in mucosal tissues (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7).

## 2. Key Molecular Players
- Genes/Proteins (HGNC): PRTN3/PR3 (autoantigen; neutrophil granule serine protease) (fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3); MPO (autoantigen; peroxidase) (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7); SERPINA1/α1-antitrypsin (regulator of PR3 bioavailability, implicated in PR3-ANCA pathogenesis) (austin2022ancaassociatedvasculitis pages 1-3); HLA-DPB1*04:01 (antigen presentation; PR3-ANCA susceptibility) (fouka2024pathogenesisofpulmonary pages 4-5); C5 (precursor of C5a); C5AR1/C5aR1 (neutrophil priming receptor) (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7); FCGR family (Fcγ receptors) and SYK (signal transduction) (shiratoriaso2023theinvolvementof pages 4-5); PADI4 (NETosis) and CYBB/NOX2 (oxidative burst) (shiratoriaso2023theinvolvementof pages 4-5).
- Chemical entities (CHEBI/drugs): C5a (chemoattractant) (fouka2024pathogenesisofpulmonary pages 5-7); Avacopan (C5aR1 antagonist; clinical validation of complement axis) (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7); DNase I (NET clearance; experimental) (shiratoriaso2023theinvolvementof pages 4-5).
- Cell types (CL): Neutrophils (primary effectors) (shiratoriaso2023theinvolvementof pages 4-5); B cells/plasma cells (ANCA production) (fouka2024pathogenesisofpulmonary pages 5-7); CD4+ Th1 and Th17 cells (granulomatous inflammation) (drouzas2025currentunderstandingof pages 2-4, fouka2024pathogenesisofpulmonary pages 5-7); Macrophages (granuloma architecture) (fouka2024pathogenesisofpulmonary pages 5-7); Endothelial cells (injury target) (drouzas2025currentunderstandingof pages 1-2).
- Anatomical locations (UBERON): Upper airway/nasal cavity and sinuses; lung parenchyma (granulomas, capillaritis); kidney glomerulus (pauci-immune necrotizing crescentic GN) (fouka2024pathogenesisofpulmonary pages 1-2, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).

Embedded artifact of ontology mappings and roles:

| Entity | Standard name | Role in GPA pathophysiology (1–2 sentences) | Key biological processes (GO term names) | Cellular components (GO CC term names) | Evidence |
|---|---|---|---|---|---|
| PRTN3 (PR3) | PRTN3 | Primary ANCA antigen in PR3-AAV; surface-exposed PR3 on primed neutrophils is target for PR3-ANCA driving neutrophil activation and tissue damage. | antigen processing and presentation; neutrophil activation | secretory granule; plasma membrane | (fouka2024pathogenesisofpulmonary pages 4-5, triaille2025theemergingconcept pages 2-3, austin2022ancaassociatedvasculitis pages 1-3) |
| MPO | MPO | Major ANCA antigen (MPO-ANCA) that when targeted induces neutrophil activation, ROS release and pauci-immune glomerulonephritis. | oxidative burst; neutrophil activation; antigen presentation | azurophil granule; extracellular space | (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, austin2022ancaassociatedvasculitis pages 1-3) |
| SERPINA1 (α1-antitrypsin) | SERPINA1 | Regulates PR3 activity and membrane localization; dysfunctional or oxidized AAT permits increased membrane-PR3 and heightened PR3-ANCA pathogenicity. | regulation of proteolysis; negative regulation of enzyme activity | plasma; extracellular region | (triaille2025theemergingconcept pages 2-3, fouka2024pathogenesisofpulmonary pages 4-5) |
| HLA-DPB1*04:01 | HLA-DPB1 | HLA class II allele strongly associated with PR3-AAV, influencing antigen presentation and loss of tolerance to PR3. | antigen processing and presentation; adaptive immune response | MHC class II protein complex; endosomal antigen processing compartments | (fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3, triaille2025theemergingconcept pages 2-3) |
| C5a | C5a (CHEBI) | Complement-derived chemoattractant that primes neutrophils and amplifies ANCA-induced activation, linking complement to inflammation in GPA. | complement activation, alternative pathway; chemotaxis | extracellular space; plasma | (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2, shiratoriaso2023theinvolvementof pages 4-5) |
| C5AR1 (C5aR1) | C5AR1 | G protein–coupled receptor for C5a; mediates neutrophil priming and recruitment and is the pharmacologic target of avacopan. | complement receptor signaling; neutrophil chemotaxis | plasma membrane; G-protein coupled receptor complex | (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2) |
| Fcγ receptors | FCGR family | Facilitate ANCA-Fc engagement on neutrophils, triggering Syk signaling, respiratory burst and degranulation. | antibody-mediated phagocytosis; Fc receptor signaling | plasma membrane; phagocytic cup | (shiratoriaso2023theinvolvementof pages 4-5, triaille2025theemergingconcept pages 2-3) |
| SYK | SYK | Tyrosine kinase downstream of FcγR engagement that propagates ANCA-induced neutrophil activation and NETosis. | Fc receptor signaling pathway; signal transduction | cytosol; plasma membrane signaling complex | (shiratoriaso2023theinvolvementof pages 4-5) |
| PADI4 (PAD4) | PADI4 | Enzyme mediating histone citrullination required for chromatin decondensation during NET formation (NETosis). | neutrophil extracellular trap formation; chromatin modification | nucleus; cytosol | (shiratoriaso2023theinvolvementof pages 4-5) |
| CYBB (NOX2) | CYBB | Catalytic subunit of NADPH oxidase generating ROS crucial for ANCA-triggered respiratory burst and NET release. | reactive oxygen species metabolic process; oxidative burst | plasma membrane; phagosome membrane | (shiratoriaso2023theinvolvementof pages 4-5) |
| Neutrophil (CL) | Neutrophil | Central effector cell: primed by cytokines/C5a, bound by ANCA, undergoes degranulation, ROS production and NETosis causing vessel injury and antigen presentation. | neutrophil activation; neutrophil extracellular trap formation; degranulation | granule; plasma membrane; extracellular space | (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 4-5) |
| B cell (CL) | B cell | Source of ANCA-producing plasma cells; BAFF and T-cell help sustain autoreactive B-cell responses in GPA. | B cell activation; humoral immune response; antibody production | B cell receptor complex; endoplasmic reticulum (secretory) | (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 2-4) |
| CD4+ Th1 (CL) | CD4+ Th1 cell | Th1 cytokines (IFNγ, TNFα) contribute to macrophage activation and granuloma formation characteristic of ENT/lung GPA. | T cell activation; interferon-gamma–mediated signaling pathway | immunological synapse; cytosol | (drouzas2025currentunderstandingof pages 2-4, fouka2024pathogenesisofpulmonary pages 5-7) |
| Th17 cell (CL) | Th17 cell | IL-17–producing T cells promote neutrophil recruitment and sustain granulomatous inflammation in GPA. | interleukin-17 production; inflammatory response | immunological synapse; cytosol | (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 2-4) |
| Macrophage (CL) | Macrophage | Phagocytes that form granulomas with activated T cells and release cytokines that sustain necrotizing inflammation in ENT and lung. | granuloma formation; phagocytosis; cytokine production | phagosome; lysosome; extracellular space | (fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 4-5) |
| Endothelial cell (CL) | Endothelial cell | Target of ANCA- and neutrophil-mediated injury leading to small-vessel vasculitis and glomerular damage; expresses adhesion molecules during inflammation. | regulation of blood vessel size; leukocyte adhesion; inflammatory response | plasma membrane; intercellular junction; basement membrane | (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2) |
| Kidney glomerulus (UBERON) | Kidney glomerulus | Site of pauci-immune necrotizing crescentic glomerulonephritis driven by ANCA-activated neutrophils and complement amplification. | inflammatory response; complement activation; glomerulus development | glomerular basement membrane; podocyte slit diaphragm | (triaille2025theemergingconcept pages 2-3, fouka2024pathogenesisofpulmonary pages 5-7) |
| Lung (UBERON) | Lung (alveolus / airway) | Frequent site of granulomatous inflammation, alveolar capillaritis and hemorrhage in GPA due to local neutrophil/NET and complement activity. | inflammatory response; neutrophil chemotaxis; tissue remodeling | alveolar capillary membrane; extracellular matrix | (fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 1-2) |
| Nasal cavity / upper airway (UBERON) | Nasal cavity / upper airway | Common anatomical focus for PR3-AAV granulomatous disease and a reservoir for microbial triggers (e.g., S. aureus) implicated in relapse. | mucosal immune response; microbial colonization; inflammatory response | nasal epithelium; nasal mucosa; extracellular region | (fouka2024pathogenesisofpulmonary pages 4-5, fouka2024pathogenesisofpulmonary pages 1-2) |
| NETs (process/structure) | Neutrophil extracellular traps (NETs) | NETs expose and modify PR3/MPO antigens, propagate endothelial injury, activate complement and perpetuate ANCA production in a pathogenic feedback loop. | neutrophil extracellular trap formation; antigen presentation; complement activation | extracellular web-like chromatin structures; extracellular space | (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 4-5) |
| Avacopan (drug) | Avacopan (C5aR1 antagonist) | Small-molecule C5aR1 inhibitor that blocks C5a-driven neutrophil priming, reduces steroid need and improves renal outcomes in AAV induction. | inhibition of complement receptor signaling; reduction of neutrophil chemotaxis | binds C5aR1 at plasma membrane | (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2) |
| DNase I (drug) | DNase I | Therapeutic enzyme that degrades NET chromatin, promoting NET clearance and reducing NET-driven autoantigen exposure and tissue injury in models. | nuclease activity on extracellular DNA; clearance of neutrophil extracellular traps | extracellular space; plasma | (shiratoriaso2023theinvolvementof pages 4-5, drouzas2025currentunderstandingof pages 2-4) |


*Table: Concise ontology-aligned table mapping key genes/proteins, cells, anatomical sites, and therapeutics to their roles, relevant GO processes and cellular components in GPA pathophysiology, with supporting evidence (pqac IDs). This supports ontology annotation and evidence-linked knowledgebase entry creation.*

## 3. Biological Processes (candidate GO terms)
- Neutrophil activation involved in immune response; neutrophil degranulation; respiratory burst; neutrophil extracellular trap formation (NETosis) (shiratoriaso2023theinvolvementof pages 4-5).
- Complement activation, alternative pathway; C5a-mediated signaling; leukocyte chemotaxis (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).
- Antigen processing and presentation of peptide antigen via MHC class II (HLA-DP) (fouka2024pathogenesisofpulmonary pages 4-5).
- B cell activation and antibody (ANCA) production; BAFF signaling (fouka2024pathogenesisofpulmonary pages 5-7).
- T cell activation; Th1 and Th17 differentiation; interferon-gamma–mediated signaling (drouzas2025currentunderstandingof pages 2-4, fouka2024pathogenesisofpulmonary pages 5-7).
- Granuloma formation; macrophage activation (fouka2024pathogenesisofpulmonary pages 5-7).
- Endothelial cell activation and leukocyte adhesion (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).

## 4. Cellular Components (candidate GO CC terms)
- Neutrophil azurophil/secretory granule; plasma membrane; Fc receptor complex; NADPH oxidase complex; extracellular space/NET structures (shiratoriaso2023theinvolvementof pages 4-5).
- MHC class II protein complex; endosomal antigen processing compartments (fouka2024pathogenesisofpulmonary pages 4-5).
- Complement components in plasma/extracellular space; membrane attack complex at sites of injury (drouzas2025currentunderstandingof pages 1-2).
- Endothelial intercellular junctions and basement membrane (injury site) (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).

## 5. Disease Progression (staged model)
- Initiation/priming: Genetic susceptibility (HLA-DPB1*04:01, PRTN3, SERPINA1 for PR3-ANCA) combined with environmental triggers (e.g., nasal dysbiosis/S. aureus) promotes neutrophil priming and altered antigen handling (fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3).
- Autoantibody generation: NET persistence provides modified PR3/MPO to antigen-presenting cells, driving ANCA production with T-cell help and B-cell activation (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7).
- Effector amplification: ANCA binds primed neutrophils and FcγR, triggering ROS, degranulation, and NETosis; C5a-C5aR1 signaling amplifies neutrophil recruitment/priming (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).
- Tissue-specific injury: In ENT/lung, Th1/Th17 and macrophage programs organize necrotizing granulomas; in kidney, pauci-immune necrotizing crescentic GN arises with complement byproducts detectable in lesions (fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).
- Relapse/chronification: Continued environmental exposures (e.g., nasal colonization) and serotype-specific biology (PR3-ANCA) sustain relapse risk (fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3, fouka2024pathogenesisofpulmonary pages 1-2).

## 6. Phenotypic Manifestations (clinical; selected HP terms)
- Upper airway involvement: chronic sinusitis, nasal crusting/ulceration, septal perforation (HP:0011109, HP:0031140) (fouka2024pathogenesisofpulmonary pages 1-2).
- Pulmonary disease: nodules/cavitations, alveolar hemorrhage (HP:0006538, HP:0025422) (fouka2024pathogenesisofpulmonary pages 1-2, fouka2024pathogenesisofpulmonary pages 5-7).
- Renal disease: rapidly progressive glomerulonephritis with hematuria/proteinuria (HP:0000093, HP:0001001) (drouzas2025currentunderstandingof pages 1-2).
- Systemic: constitutional symptoms and small-vessel vasculitis manifestations (purpura, neuropathy) vary by serotype and burden (austin2022ancaassociatedvasculitis pages 1-3).

## Expert Opinions and Analysis
- Serotype-centered view: Robust genetics demonstrate PR3-ANCA and MPO-ANCA are distinct at HLA and non-HLA loci, supporting serotype-based classification with therapeutic implications (e.g., relapse risk, preferred biologics) (austin2022ancaassociatedvasculitis pages 1-3, fouka2024pathogenesisofpulmonary pages 4-5).
- Complement as amplifier and target: Evidence across mechanistic studies and clinical trials indicates C5a–C5aR1 is a key amplification axis; C5aR1 antagonism enables steroid minimization and improved renal outcomes during induction, validating complement as a druggable hub (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).
- NETs as central nodes: NETosis integrates neutrophil activation, antigen availability, and complement crosstalk, rationalizing emerging NET-directed strategies (e.g., DNase I, PAD4 inhibition) alongside existing B-cell–targeted therapy (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7).
- Microbiome and relapse: While historical and mechanistic links implicate S. aureus carriage in GPA relapse, contemporary cohort data show inconsistent benefit from eradication, underscoring the need for controlled interventional studies (fouka2024pathogenesisofpulmonary pages 4-5, fouka2024pathogenesisofpulmonary pages 1-2).

## Relevant Statistics and Data (recent)
- HLA-class II associations in Scandinavia: PR3-AAV significantly associated with HLA-DPB1*04:01; MPO-AAV with HLA-DRB1*04:04; organ involvement and relapse not directly tied to these alleles in that cohort (RMD Open 2024) (fouka2024pathogenesisofpulmonary pages 4-5).
- ENT involvement prevalence: ENT disease is common in GPA and contributes to diagnostic suspicion in otolaryngology and general medicine practice (2023–2024 reviews) (fouka2024pathogenesisofpulmonary pages 1-2, austin2022ancaassociatedvasculitis pages 1-3).
- Nasal S. aureus: In a Netherlands retrospective cohort (n=213 with ENT involvement), colonization (44% of tested) and targeted eradication were not associated with differences in systemic or local disease activity (Rheumatology International 2023) (fouka2024pathogenesisofpulmonary pages 1-2).

## Gene/Protein Annotations and Ontology Terms
- HGNC: PRTN3, MPO, SERPINA1, C5, C5AR1, SYK, PADI4, CYBB; HLA-DPB1 (fouka2024pathogenesisofpulmonary pages 4-5, shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, austin2022ancaassociatedvasculitis pages 1-3).
- GO Biological Process: neutrophil activation; NET formation; respiratory burst; complement activation (alternative pathway); antigen processing/presentation; B cell activation; Th1/Th17 differentiation; granuloma formation (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 4-5, drouzas2025currentunderstandingof pages 2-4).
- GO Cellular Component: neutrophil granules; plasma membrane; Fc receptor complex; MHC class II complex; extracellular space/NETs; membrane attack complex (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 4-5, drouzas2025currentunderstandingof pages 1-2).

## Phenotype Associations (HP terms; examples)
- HP:0011109 (Chronic sinusitis), HP:0031140 (Nasal septal perforation), HP:0006538 (Pulmonary nodules), HP:0025422 (Pulmonary hemorrhage), HP:0000093 (Glomerulonephritis), HP:0001001 (Proteinuria) (fouka2024pathogenesisofpulmonary pages 1-2, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).

## Cell Type Involvement (CL terms; examples)
- CL: Neutrophil; B cell; CD4+ Th1; Th17; Macrophage; Endothelial cell (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 2-4, drouzas2025currentunderstandingof pages 1-2).

## Anatomical Locations (UBERON; examples)
- UBERON: Nasal cavity/sinuses; Lung; Kidney glomerulus (fouka2024pathogenesisofpulmonary pages 1-2, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).

## Chemical Entities (CHEBI; examples)
- CHEBI: C5a; Small-molecule drug avacopan (C5aR1 antagonist) (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2).

## Current Applications and Real-World Implementations
- Complement blockade: Avacopan is used with standard induction to reduce glucocorticoid exposure and improve renal recovery in AAV, mechanistically interrupting C5a–C5aR1 neutrophil priming (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, drouzas2025currentunderstandingof pages 1-2). Case-level implementation strategies include early transition approaches in clinical practice accompanying induction regimens (case-based literature) (fouka2024pathogenesisofpulmonary pages 5-7).
- B-cell depletion: Rituximab remains standard-of-care for induction/maintenance, consistent with B-cell centrality to ANCA production (austin2022ancaassociatedvasculitis pages 1-3, fouka2024pathogenesisofpulmonary pages 5-7).
- ENT/lung management: Recognition of GPA ENT-pulmonary tropism informs multidisciplinary care and surveillance for relapse, though the benefit of S. aureus eradication for disease control is uncertain in recent cohorts (fouka2024pathogenesisofpulmonary pages 1-2, fouka2024pathogenesisofpulmonary pages 4-5).

## Distinctions vs MPO-AAV (mechanism and phenotype)
- Genetics: PR3-ANCA AAV links to HLA-DP/PRTN3/SERPINA1, whereas MPO-ANCA AAV links to HLA-DQ/DR variants; these serotype-specific genetic backbones support different immunobiology (fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3).
- Tissue pattern: PR3-ANCA disease (GPA) is enriched for granulomatous ENT and lung inflammation; MPO-ANCA disease is more commonly renal-limited and lacks granulomatous pathology (fouka2024pathogenesisofpulmonary pages 5-7, austin2022ancaassociatedvasculitis pages 1-3).
- Regulatory axes: Differences in antigen biology (PR3 vs MPO) and in serine protease inhibition (SERPINA1/α1-antitrypsin) are implicated in PR3-ANCA–specific pathogenicity (austin2022ancaassociatedvasculitis pages 1-3).

## Evidence Items (PMID/DOI/URLs and dates)
- Shiratori-Aso S, Nakazawa D. Frontiers in Immunology, 2023-09. DOI:10.3389/fimmu.2023.1261151; URL: https://doi.org/10.3389/fimmu.2023.1261151 (shiratoriaso2023theinvolvementof pages 4-5)
- Fouka E et al. International Journal of Molecular Sciences, 2024-05. DOI:10.3390/ijms25105278; URL: https://doi.org/10.3390/ijms25105278 (fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 1-2, fouka2024pathogenesisofpulmonary pages 4-5)
- Drouzas K et al. Life, 2025-05. DOI:10.3390/life15050756; URL: https://doi.org/10.3390/life15050756 (drouzas2025currentunderstandingof pages 1-2)
- Austin K et al. Journal of Inflammation Research, 2022-04. DOI:10.2147/JIR.S284768; URL: https://doi.org/10.2147/jir.s284768 (austin2022ancaassociatedvasculitis pages 1-3)
- Lundtoft C et al. RMD Open, 2024-04. DOI:10.1136/rmdopen-2023-004039; URL: https://doi.org/10.1136/rmdopen-2023-004039 (fouka2024pathogenesisofpulmonary pages 4-5)
- Schaap CM et al. Rheumatology International, 2023-10. DOI:10.1007/s00296-022-05228-8; URL: https://doi.org/10.1007/s00296-022-05228-8 (fouka2024pathogenesisofpulmonary pages 1-2)
- Triaille C et al. Autoimmunity Reviews, 2025-06. DOI:10.1016/j.autrev.2025.103824; URL: https://doi.org/10.1016/j.autrev.2025.103824 (triaille2025theemergingconcept pages 2-3)

## Summary
GPA pathophysiology is driven by serotype-specific autoimmunity to PR3, integrating primed neutrophil activation, NETosis, and alternative-pathway complement amplification with maladaptive B/T cell responses. Distinct genetic architecture in PR3-ANCA disease (HLA-DP, PRTN3, SERPINA1) and environmental triggers in the upper airway help explain GPA’s ENT–lung tropism and relapse behavior. Complement C5a–C5aR1 signaling is a validated therapeutic node (avacopan), while NET-targeted and B-cell–directed strategies address upstream and downstream arms of the pathogenic cycle (shiratoriaso2023theinvolvementof pages 4-5, fouka2024pathogenesisofpulmonary pages 5-7, fouka2024pathogenesisofpulmonary pages 4-5, austin2022ancaassociatedvasculitis pages 1-3, drouzas2025currentunderstandingof pages 1-2, fouka2024pathogenesisofpulmonary pages 1-2).

References

1. (austin2022ancaassociatedvasculitis pages 1-3): Keziah Austin, Shalini Janagan, Matthew Wells, Helena Crawshaw, Stephen McAdoo, and Joanna C Robson. Anca associated vasculitis subtypes: recent insights and future perspectives. Journal of Inflammation Research, 15:2567-2582, Apr 2022. URL: https://doi.org/10.2147/jir.s284768, doi:10.2147/jir.s284768. This article has 60 citations and is from a peer-reviewed journal.

2. (shiratoriaso2023theinvolvementof pages 4-5): Satoka Shiratori-Aso and Daigo Nakazawa. The involvement of nets in anca-associated vasculitis. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1261151, doi:10.3389/fimmu.2023.1261151. This article has 33 citations and is from a peer-reviewed journal.

3. (fouka2024pathogenesisofpulmonary pages 5-7): Evangelia Fouka, Fotios Drakopanagiotakis, and Paschalis Steiropoulos. Pathogenesis of pulmonary manifestations in anca-associated vasculitis and goodpasture syndrome. International Journal of Molecular Sciences, 25:5278, May 2024. URL: https://doi.org/10.3390/ijms25105278, doi:10.3390/ijms25105278. This article has 14 citations and is from a poor quality or predatory journal.

4. (fouka2024pathogenesisofpulmonary pages 1-2): Evangelia Fouka, Fotios Drakopanagiotakis, and Paschalis Steiropoulos. Pathogenesis of pulmonary manifestations in anca-associated vasculitis and goodpasture syndrome. International Journal of Molecular Sciences, 25:5278, May 2024. URL: https://doi.org/10.3390/ijms25105278, doi:10.3390/ijms25105278. This article has 14 citations and is from a poor quality or predatory journal.

5. (drouzas2025currentunderstandingof pages 1-2): Konstantinos Drouzas, Petros Kalogeropoulos, George Liapis, and Sophia Lionaki. Current understanding of the pathogenesis of anca-associated vasculitis and novel treatment options targeting complement activation. Life, 15:756, May 2025. URL: https://doi.org/10.3390/life15050756, doi:10.3390/life15050756. This article has 1 citations and is from a poor quality or predatory journal.

6. (drouzas2025currentunderstandingof pages 2-4): Konstantinos Drouzas, Petros Kalogeropoulos, George Liapis, and Sophia Lionaki. Current understanding of the pathogenesis of anca-associated vasculitis and novel treatment options targeting complement activation. Life, 15:756, May 2025. URL: https://doi.org/10.3390/life15050756, doi:10.3390/life15050756. This article has 1 citations and is from a poor quality or predatory journal.

7. (fouka2024pathogenesisofpulmonary pages 4-5): Evangelia Fouka, Fotios Drakopanagiotakis, and Paschalis Steiropoulos. Pathogenesis of pulmonary manifestations in anca-associated vasculitis and goodpasture syndrome. International Journal of Molecular Sciences, 25:5278, May 2024. URL: https://doi.org/10.3390/ijms25105278, doi:10.3390/ijms25105278. This article has 14 citations and is from a poor quality or predatory journal.

8. (triaille2025theemergingconcept pages 2-3): Clément Triaille, Benjamin Terrier, Alice Hadchouel, Elie Haddad, Augusto Vaglio, and Marie-Louise Frémond. The emerging concept of anca-associated vasculitis related to inborn errors of immunity. Autoimmunity Reviews, 24:103824, Jun 2025. URL: https://doi.org/10.1016/j.autrev.2025.103824, doi:10.1016/j.autrev.2025.103824. This article has 4 citations and is from a peer-reviewed journal.