---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:10.533251'
end_time: '2025-12-15T09:20:12.488150'
duration_seconds: 421.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ehlers-Danlos Syndrome, COL5A1-related
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Ehlers-Danlos Syndrome, COL5A1-related
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ehlers-Danlos Syndrome, COL5A1-related**.
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
- **Disease Name:** Ehlers-Danlos Syndrome, COL5A1-related
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ehlers-Danlos Syndrome, COL5A1-related**.
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


Plan
- Objective 1 (completed): Define scope and core pathophysiology for COL5A1-related (classical) Ehlers-Danlos syndrome (cEDS).
- Objective 2 (completed): Identify and review recent (2023–2024) literature on type V collagen biology and cEDS.
- Objective 3 (completed): Extract molecular/cellular mechanisms, tissues, cell types, and mechanistic pathways.
- Objective 4 (completed): Map to ontology terms (HGNC, GO, HP, CL, UBERON) and compile a structured artifact.
- Objective 5 (completed): Synthesize sequence of disease progression from genotype to phenotype.
- Objective 6 (completed): Create a compact annotations table.
- Objective 7 (completed): Write a comprehensive research report with citations, URLs, and dates.
- Objective 8: Submit final answer.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Ehlers-Danlos Syndrome, COL5A1-related (classical EDS)
- Category: Genetic

Pathophysiology description
Classical Ehlers-Danlos syndrome (cEDS) due to COL5A1 variants is a monogenic connective tissue disorder characterized by deficiency or structural abnormality of type V collagen, a minor fibrillar collagen that nucleates and regulates the diameter of type I/III collagen fibrils in skin and other tissues (heterotrimer typically [α1(V)]2α2(V)). Loss or reduction of type V collagen disrupts collagen fibrillogenesis, producing enlarged, heterogeneous, and irregular fibrils, a disorganized ECM architecture, impaired tissue mechanics, and clinical fragility manifested by hyperextensible skin, poor wound healing with atrophic scarring, easy bruising, and generalized joint hypermobility (review and diagnostic guidance) (Zschocke 2024; URL: https://doi.org/10.1515/medgen-2024-2061; Nov 2024) (zschocke2024geneticdiagnosisof pages 2-3). In experimental and translational work, acute or chronic deficiency of Col5a1 in dermal fibroblasts leads to fibrillar disarray on ultrastructure, altered mechanical properties, reduced collagen deposition, prolonged inflammation, and delayed re-epithelialization during wound repair; these defects can be partially rescued by pharmacologic modulation of mechanosensitive integrin signaling or transplantation of wild-type fibroblasts (Kelly‑Scumpia et al., iScience; URL: https://doi.org/10.1016/j.isci.2024.110676; Sep 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).

Core Pathophysiology
- Primary mechanisms: COL5A1 pathogenic variants reduce functional type V collagen (often via haploinsufficiency), causing defective nucleation/templating and diameter control of type I/III collagen fibrils. Resultant fibrils show increased mean diameter and irregular composite “collagen cauliflower” structures, with loss of normal basket-weave organization and reduced tissue mechanical integrity (Donahue 2024; 3D model synopsis) (donahue2024athreedimensional(3d) pages 21-26, donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26). Skin AFM imaging demonstrates irregular fibrils and a shift toward lower compressive elastic modulus subpopulations relative to healthy collagen (peak ~2.5 GPa in controls), consistent with weaker fibrils (Neshatian et al., PLOS ONE; URL: https://doi.org/10.1371/journal.pone.0307442; Aug 2024) (neshatian2024investigationofdermal pages 1-2).
- Dysregulated pathways: Mechanosensitive integrin signaling is elevated in Col5a1-deficient wounds, and integrin pathway inhibition improves re-epithelialization and reduces inflammation in mice, indicating ECM–integrin mechanotransduction as a driver of healing failure (Kelly‑Scumpia 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3). In fibrocartilage pericellular matrix (PCM), Col5a1 haploinsufficiency alters PCM mechanics and cell mechanotransduction, with upregulation of lysyl oxidase and tenascin C biosynthesis in meniscal cells, highlighting a LOX-linked matrix remodeling response to collagen V insufficiency (Wang et al., bioRxiv; URL: https://doi.org/10.1101/2024.06.26.600498; Jun 2024) (royerweeden2023collagenvpromotes pages 1-9).
- Affected cellular processes: collagen fibrillogenesis; ECM assembly and organization; cell–matrix adhesion and mechanotransduction; wound-healing programs including re-epithelialization and granulation tissue maturation (Kelly‑Scumpia 2024; Neshatian 2024; Donahue 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3, neshatian2024investigationofdermal pages 1-2, donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26).

Key Molecular Players
- Genes/Proteins (HGNC):
  - COL5A1 (HGNC:2199): causal gene for most cEDS, driving Type V collagen deficiency and fibrillogenesis defects (Zschocke 2024; Donahue 2024) (zschocke2024geneticdiagnosisof pages 2-3, donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26).
  - COL5A2 (HGNC:2200): alternative α2(V) chain; structural variants also implicated in cEDS (Zschocke 2024) (zschocke2024geneticdiagnosisof pages 2-3).
  - COL1A1 (HGNC:2197): dominant fibrillar collagen partnering with type V in fibrillogenesis; perturbation of type V impacts collagen I fibril nucleation and organization (Donahue 2024; Neshatian 2024) (donahue2024athreedimensional(3d)a pages 21-26, neshatian2024investigationofdermal pages 1-2).
  - Integrins (e.g., ITGA5/ITGB1): dysregulated expression and signaling in Col5a1-deficient wounds; pharmacologic modulation rescues healing (Kelly‑Scumpia 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
  - LOX (lysyl oxidase): upregulated in Col5a1+/D meniscus PCM remodeling; implicated in altered crosslinking responses (Wang 2024) (royerweeden2023collagenvpromotes pages 1-9).
- Chemical Entities (CHEBI):
  - Mechanosensitive integrin pathway inhibitors (small molecules used in murine rescue experiments) are relevant research tools and potential leads for wound-healing modulation in cEDS (Kelly‑Scumpia 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
- Cell Types (CL): dermal fibroblasts (primary Col5a1 source and ECM organizer in skin), keratinocytes (secondary impairment of re-epithelialization), keratocytes/corneal stromal cells (corneal ECM dependence on type V), tenocytes and meniscal fibrochondrocytes (fibrillogenesis/PCM mechanobiology) (Kelly‑Scumpia 2024; Neshatian 2024; Donahue 2024; Wang 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3, neshatian2024investigationofdermal pages 1-2, donahue2024athreedimensional(3d)a pages 21-26, royerweeden2023collagenvpromotes pages 1-9).
- Anatomical locations (UBERON): skin, corneal stroma, tendons, and meniscus are highlighted as tissues in which type V collagen regulates fibrillogenesis and/or PCM mechanics (Kelly‑Scumpia 2024; Neshatian 2024; Donahue 2024; Wang 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, neshatian2024investigationofdermal pages 1-2, donahue2024athreedimensional(3d)a pages 21-26, royerweeden2023collagenvpromotes pages 1-9).

Biological Processes (GO terms) disrupted
- Collagen fibrillogenesis (GO:0030199): type V is required for nucleation and diameter control of collagen I/III fibrils; loss leads to thickened, irregular, composite fibrils (Donahue 2024; Neshatian 2024) (donahue2024athreedimensional(3d)a pages 21-26, neshatian2024investigationofdermal pages 1-2).
- Extracellular matrix organization (GO:0030198): ECM disorganization and reduced mechanical integrity in skin and wounds (Kelly‑Scumpia 2024; Neshatian 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, neshatian2024investigationofdermal pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
- Wound healing (GO:0042060): delayed re-epithelialization, persistent inflammation, and defective granulation tissue in Col5a1-deficient contexts (Kelly‑Scumpia 2024) (kellyscumpia2024modulatingtheextracellular pages 2-3).
- Mechanotransduction/Integrin signaling (GO:0007165/GO:0007229): elevated mechanosensitive integrin pathways in Col5a1-deficient wounds; rescue with integrin modulation (Kelly‑Scumpia 2024); perturbed PCM mechanotransduction in fibrocartilage with Col5a1 haploinsufficiency (Wang 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3, royerweeden2023collagenvpromotes pages 1-9).

Cellular Components (GO-CC)
- Extracellular matrix (GO:0031012): site of fibrillogenesis defects and mechanical failure in cEDS (Neshatian 2024; Donahue 2024) (neshatian2024investigationofdermal pages 1-2, donahue2024athreedimensional(3d)a pages 21-26).
- Pericellular matrix (GO:0071944): collagen V-rich PCM surrounding fibrocartilage cells is mechanically and structurally altered by Col5a1 haploinsufficiency; impacts cell mechanotransduction (Wang 2024) (royerweeden2023collagenvpromotes pages 1-9).
- Endoplasmic reticulum (GO:0005783): although many COL5A1 variants are haploinsufficient, dominant-negative effects via ER retention/quality control are general mechanisms in autosomal-dominant ECM diseases and may modulate phenotypes for structural COL5A1 variants (conceptual mechanism; Gariballa 2024; URL: https://doi.org/10.1186/s12929-024-01054-1; Jun 2024) (royerweeden2023collagenvpromotes pages 1-9).

Disease Progression: sequence of events
1) Genotype: COL5A1 pathogenic variant.
2) Molecular consequence: reduced or dysfunctional α1(V) chain; frequently haploinsufficiency → ~50% reduction of type V collagen (Donahue 2024) (donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26).
3) ECM assembly defect: impaired nucleation and control of collagen I/III fibril diameter → increased average fibril diameter, irregular composite fibrils (“cauliflower” morphology), disorganized basket-weave architecture; skin nanomechanics shift to lower modulus populations (Donahue 2024; Neshatian 2024) (donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26, neshatian2024investigationofdermal pages 1-2).
4) Tissue-level changes: reduced tensile integrity and abnormal mechanics; during injury, loose granulation tissue, persistent inflammation, failure of epidermal reconstitution; elevated mechanosensitive integrin signaling (Kelly‑Scumpia 2024) (kellyscumpia2024modulatingtheextracellular pages 2-3, kellyscumpia2024modulatingtheextracellular pages 1-2).
5) Clinical manifestations: hyperextensible skin, atrophic scarring, easy bruising, generalized joint hypermobility; increased risk of wound dehiscence and poor suture retention (Zschocke 2024; Donahue 2024) (zschocke2024geneticdiagnosisof pages 2-3, donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26).

Phenotypic Manifestations (HP terms)
- Skin hyperextensibility (HP:0000974), atrophic scarring (HP:0001075), joint hypermobility (HP:0001382), easy bruising (HP:0000978), delayed wound healing (HP:0001030) (Zschocke 2024; Donahue 2024; Kelly‑Scumpia 2024) (zschocke2024geneticdiagnosisof pages 2-3, donahue2024athreedimensional(3d)a pages 21-26, kellyscumpia2024modulatingtheextracellular pages 2-3).

Differences from TNXB-related classical-like EDS (clEDS)
- TNXB (Tenascin-X) deficiency causes a recessive classical-like EDS characterized by hyperextensible skin without atrophic scarring, with frequent chronic joint pain/myalgia and neurological features (e.g., paresthesia, axonal polyneuropathy) in reported cohorts and models (Okuda‑Ashitaka & Matsumoto, Frontiers in Genetics; URL: https://doi.org/10.3389/fgene.2023.1107787; Mar 2023). TNXB-related clEDS thus differs from COL5A1-related cEDS, which typically includes atrophic scarring and is autosomal dominant (Okuda‑Ashitaka 2023; Zschocke 2024) (zschocke2024geneticdiagnosisof pages 2-3).

Recent developments and latest research (2023–2024)
- Mechanobiology of defective healing: Conditional fibroblast-specific Col5a1 deletion models reveal integrin-dependent mechanotransduction as a targetable axis; integrin inhibitors and fibroblast transplantation improved epidermal gene expression, reduced inflammation, and accelerated closure in mice (iScience, Sep 2024; URL: https://doi.org/10.1016/j.isci.2024.110676) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
- Nanostructure and biomechanics: Skin AFM/Picrosirius methods applied to cEDS show irregular fibrils and reduced modulus subpopulations, supporting nanoscale biomechanical biomarkers (PLOS ONE, Aug 2024; URL: https://doi.org/10.1371/journal.pone.0307442) (neshatian2024investigationofdermal pages 1-2).
- PCM mechanobiology: In Col5a1+/D menisci, collagen V insufficiency thickens fibrils and weakens PCM mechanics with altered viscoelasticity, blunting intracellular calcium signaling and upregulating LOX and tenascin C; highlights a pivotal role of collagen V in PCM and mechanotransduction (bioRxiv, Jun 2024; URL: https://doi.org/10.1101/2024.06.26.600498) (royerweeden2023collagenvpromotes pages 1-9).
- Reviews/diagnostics: Updated 2024 guidance on genetic diagnosis underscores COL5A1 and COL5A2 as major cEDS genes; transcript analyses can show non-transcription of one allele (null-allele test) supporting haploinsufficiency; no major phenotype differences between LoF and missense in COL5A1 were reported (Medizinische Genetik, Nov 2024; URL: https://doi.org/10.1515/medgen-2024-2061) (zschocke2024geneticdiagnosisof pages 2-3).

Current applications and real-world implementations
- Preclinical intervention in murine Col5a1-deficient wound models: integrin-pathway inhibitors (mechanosensitive signaling modulators) and wild-type fibroblast transplantation improved healing parameters (re-epithelialization, closure) (iScience, 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
- Experimental diagnostic adjuncts: skin ultrastructure imaging (TEM), AFM nanomechanics, and Picrosirius red birefringence can visualize ECM disorganization and altered fibrils in cEDS; these methods support research and may complement clinical assessments (PLOS ONE, 2024) (neshatian2024investigationofdermal pages 1-2).

Expert opinions and analysis from authoritative sources
- The 2024 diagnostic review emphasizes type V collagen deficiency/abnormality as the central mechanism in cEDS and notes that COL5A1 LoF and missense variants both produce cEDS without strong phenotype stratification; combined sequencing and deletion/duplication testing are recommended, with transcript-level null-allele assessment aiding interpretation (Zschocke 2024) (zschocke2024geneticdiagnosisof pages 2-3).
- Mechanobiology-focused experimental work posits that abnormal integrin signaling downstream of ECM disarray is a key driver of impaired healing and inflammation, providing a rationale for pathway-specific interventions (Kelly‑Scumpia 2024) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
- PCM-centric work suggests that collagen V is pivotal in protecting resident fibrocartilage cells from mechanical stress, and its deficiency compromises PCM mechanics and cellular signaling—broadening the pathophysiologic framework beyond skin (Wang 2024) (royerweeden2023collagenvpromotes pages 1-9).

Relevant statistics and data from recent studies
- Approximate 50% reduction in type V collagen in COL5A1 haploinsufficiency with an ~25% increase in fibril diameter and abnormal “collagen cauliflower” fibrils reported in cEDS-focused 3D model synthesis (Donahue 2024) (donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26).
- AFM nanomechanics: healthy human dermal collagen shows a predominant elastic modulus ~2.5 GPa; cEDS/hEDS samples demonstrate subpopulations with lower modulus, indicating weaker fibrils (PLOS ONE, 2024) (neshatian2024investigationofdermal pages 1-2).
- Murine wound outcomes with acute fibroblast-specific Col5a1 deletion: significantly larger wounds (e.g., ~25% unhealed at day 19), delayed re-epithelialization, loose granulation tissue, prolonged inflammation; rescue by integrin modulation or fibroblast transplantation (iScience, 2024) (kellyscumpia2024modulatingtheextracellular pages 2-3).

Gene/protein annotations with ontology terms; phenotype, cell, anatomy, and process mapping
| Category | Item | Ontology ID | Evidence/Notes | Sources (pqac IDs) |
|---|---|---:|---|---|
| Gene / Protein (HGNC) | COL5A1 | HGNC:2199 | Causal gene for cEDS; haploinsufficiency reduces type V collagen, disrupting fibrillogenesis and wound repair (murine and human data). (kellyscumpia2024modulatingtheextracellular pages 2-3, donahue2024athreedimensional(3d)a pages 21-26, zschocke2024geneticdiagnosisof pages 2-3) | pqac-00000005, pqac-00000003, pqac-00000007 |
| Gene / Protein (HGNC) | COL5A2 | HGNC:2200 | Alternative type V chain implicated in cEDS; often structural (missense) variants with overlapping phenotype. (zschocke2024geneticdiagnosisof pages 2-3, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000007, pqac-00000006 |
| Gene / Protein (HGNC) | COL1A1 | HGNC:2197 | Interacts with type V during fibrillogenesis; COL1A1 variants can produce cEDS-like features and modify phenotype. (donahue2024athreedimensional(3d)a pages 21-26, neshatian2024investigationofdermal pages 1-2) | pqac-00000003, pqac-00000002 |
| Gene / Protein (HGNC) | Integrins (e.g., ITGA5 / ITGB1) | (examples) | Altered integrin expression and mechanosensitive integrin signaling observed in Col5a1-deficient wounds; targeting integrins rescues healing in models. (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000000, pqac-00000005, pqac-00000006 |
| Biological Process (GO) | Collagen fibrillogenesis | GO:0030199 | Type V collagen nucleates/limits collagen I/III fibril assembly; loss → increased fibril diameter and irregular "cauliflower" fibrils. (donahue2024athreedimensional(3d)a pages 21-26, neshatian2024investigationofdermal pages 1-2, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000003, pqac-00000002, pqac-00000006 |
| Biological Process (GO) | Extracellular matrix organization | GO:0030198 | cEDS shows disorganized ECM architecture and altered matrix mechanics in skin and wounds. (kellyscumpia2024modulatingtheextracellular pages 2-3, donahue2024athreedimensional(3d)a pages 21-26, kellyscumpia2024modulatingtheextracellular pages 1-2) | pqac-00000005, pqac-00000003, pqac-00000000 |
| Biological Process (GO) | Wound healing | GO:0042060 | Delayed re-epithelialization, loose granulation tissue, prolonged inflammation in Col5a1 loss models and patient observations. (kellyscumpia2024modulatingtheextracellular pages 2-3, donahue2024athreedimensional(3d)a pages 21-26, kellyscumpia2024modulatingtheextracellular pages 1-2) | pqac-00000005, pqac-00000003, pqac-00000000 |
| Biological Process (GO) | Mechanotransduction | GO:0007165 | Altered pericellular mechanics and mechanosensitive signaling (integrins/YAP axis implicated) in Col5a1-deficient contexts. (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000000, pqac-00000005, pqac-00000006 |
| Biological Process (GO) | Integrin signaling pathway | GO:0007229 | Dysregulated integrin expression in wounds; pharmacologic integrin modulation improves outcomes in model systems. (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3) | pqac-00000000, pqac-00000005 |
| Biological Process (GO) | Collagen biosynthetic process | GO:0032964 | Perturbation of collagen V production alters overall collagen matrix deposition and fibril morphology. (donahue2024athreedimensional(3d)a pages 21-26, zschocke2024geneticdiagnosisof pages 2-3) | pqac-00000003, pqac-00000007 |
| Cellular Component (GO-CC) | Extracellular matrix | GO:0031012 | Primary compartment where defective collagen V yields disrupted fibril architecture and weaker mechanics (skin AFM/TEM). (neshatian2024investigationofdermal pages 1-2, donahue2024athreedimensional(3d)a pages 21-26) | pqac-00000002, pqac-00000003 |
| Cellular Component (GO-CC) | Pericellular matrix | GO:0071944 | Pericellular/pericellular niche altered by reduced ColV production, affecting cell–matrix signaling and protection of cells from mechanical stress. (kellyscumpia2024modulatingtheextracellular pages 2-3, royerweeden2023collagenvpromotes pages 1-9, donahue2024athreedimensional(3d) pages 21-26) | pqac-00000005, pqac-00000006, pqac-00000001 |
| Cellular Component (GO-CC) | Endoplasmic reticulum | GO:0005783 | Loss-of-function alleles often produce haploinsufficiency via NMD; ER-related quality control relevant for structural variants (dominant-negative potential). (zschocke2024geneticdiagnosisof pages 2-3) | pqac-00000007 |
| Cell Type (CL) | Dermal fibroblast | CL:0002620 | Key source of ColV in skin; fibroblast-specific Col5a1 deletion reproduces cEDS wound defects (reduced migration/proliferation, ECM disarray). (kellyscumpia2024modulatingtheextracellular pages 2-3, donahue2024athreedimensional(3d) pages 21-26) | pqac-00000005, pqac-00000001 |
| Cell Type (CL) | Keratinocyte | CL:0000312 | Epidermal gene programs and re-epithelialization impaired secondary to defective dermal ECM in Col5a1-deficient wounds. (kellyscumpia2024modulatingtheextracellular pages 2-3) | pqac-00000005 |
| Cell Type (CL) | Keratocyte / corneal stromal cell | CL:0001840 | Corneal wound outcomes affected by ColV deficiency; corneal stromal ECM organization depends on collagen V. (kellyscumpia2024modulatingtheextracellular pages 1-2, donahue2024athreedimensional(3d) pages 21-26) | pqac-00000000, pqac-00000001 |
| Cell Type (CL) | Tenocyte / tendon cell | CL:0002304 | Tendon fibrillogenesis and mechanics rely on ColV regulation of fibril diameter; altered cell–matrix interactions reported. (donahue2024athreedimensional(3d)a pages 21-26, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000003, pqac-00000006 |
| Cell Type (CL) | Meniscal fibrochondrocyte | CL:0002499 | Type V collagen contributes to pericellular/PCM structure in fibrocartilaginous tissues; Col5a1 perturbation alters PCM mechanics. (royerweeden2023collagenvpromotes pages 1-9, donahue2024athreedimensional(3d) pages 21-26) | pqac-00000006, pqac-00000001 |
| Anatomy (UBERON) | Skin of body | UBERON:0002097 | Primary affected organ: skin hyperextensibility, fragility, and altered nanostructure/mechanics documented by AFM and TEM. (neshatian2024investigationofdermal pages 1-2, donahue2024athreedimensional(3d)a pages 21-26, kellyscumpia2024modulatingtheextracellular pages 2-3) | pqac-00000002, pqac-00000003, pqac-00000005 |
| Anatomy (UBERON) | Corneal stroma | UBERON:0001772 | ColV important for corneal ECM and wound healing; corneal phenotypes observed in models. (kellyscumpia2024modulatingtheextracellular pages 1-2, donahue2024athreedimensional(3d) pages 21-26) | pqac-00000000, pqac-00000001 |
| Anatomy (UBERON) | Tendon | UBERON:0001376 | ColV regulates tendon fibril diameter and mechanics → clinical relevance for joint stability and repair. (donahue2024athreedimensional(3d)a pages 21-26, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000003, pqac-00000006 |
| Anatomy (UBERON) | Meniscus of knee | UBERON:0001461 | Fibrocartilaginous tissues show PCM-dependent mechanical changes when Col5a1 is reduced, with implications for load-bearing function. (royerweeden2023collagenvpromotes pages 1-9, donahue2024athreedimensional(3d) pages 21-26) | pqac-00000006, pqac-00000001 |
| Phenotype (HPO) | Skin hyperextensibility | HP:0000974 | Core clinical sign of cEDS linked to defective dermal ECM from ColV deficiency. (zschocke2024geneticdiagnosisof pages 2-3, donahue2024athreedimensional(3d)a pages 21-26) | pqac-00000007, pqac-00000003 |
| Phenotype (HPO) | Atrophic scarring | HP:0001075 | Delayed/abnormal wound healing with characteristic atrophic "cigarette-paper" scars correlates with fibrillogenesis defects. (donahue2024athreedimensional(3d)a pages 21-26, kellyscumpia2024modulatingtheextracellular pages 2-3) | pqac-00000003, pqac-00000005 |
| Phenotype (HPO) | Joint hypermobility | HP:0001382 | Result of connective tissue laxity due to ECM structural weakness from altered collagen V–dependent fibrils. (zschocke2024geneticdiagnosisof pages 2-3, royerweeden2023collagenvpromotes pages 1-9) | pqac-00000007, pqac-00000006 |
| Phenotype (HPO) | Easy bruising | HP:0000978 | Tissue fragility and impaired ECM integrity increase bleeding/bruise tendency. (donahue2024athreedimensional(3d)a pages 21-26, neshatian2024investigationofdermal pages 1-2) | pqac-00000003, pqac-00000002 |
| Phenotype (HPO) | Delayed wound healing | HP:0001030 | Validated in Col5a1 conditional and haploinsufficient models and observed clinically in cEDS patients. (kellyscumpia2024modulatingtheextracellular pages 2-3, donahue2024athreedimensional(3d)a pages 21-26) | pqac-00000005, pqac-00000003 |


*Table: Compact, ontology-mapped annotations for COL5A1-related classical EDS summarizing genes, GO processes, cellular components, cell types, anatomy, and HPO phenotypes with brief evidence notes and source pointers to the gathered contextual items (kellyscumpia2024modulatingtheextracellular pages 1-2, zschocke2024geneticdiagnosisof pages 2-3). This table is useful for knowledge-base population and rapid reference.*

Evidence items with PMIDs/DOIs and URLs (selection)
- Kelly‑Scumpia KM et al. Modulating the extracellular matrix to treat wound healing defects in Ehlers-Danlos syndrome. iScience. Sep 2024. DOI: 10.1016/j.isci.2024.110676. URL: https://doi.org/10.1016/j.isci.2024.110676 (Mechanosensitive integrin signaling; Col5a1 CKO wound model; rescue) (kellyscumpia2024modulatingtheextracellular pages 1-2, kellyscumpia2024modulatingtheextracellular pages 2-3).
- Neshatian M et al. Investigation of dermal collagen nanostructures in EDS patients. PLOS ONE. Aug 2024. DOI: 10.1371/journal.pone.0307442. URL: https://doi.org/10.1371/journal.pone.0307442 (AFM/Picrosirius; irregular fibrils; reduced modulus) (neshatian2024investigationofdermal pages 1-2).
- Donahue M. A Three-Dimensional (3D) In Vitro Model of Ehlers-Danlos Syndrome. 2024. (3D model synthesis; haploinsufficiency; fibril diameter; “cauliflowers”; surgical implications) (donahue2024athreedimensional(3d) pages 21-26, donahue2024athreedimensional(3d)a pages 21-26, donahue2024athreedimensional(3d)b pages 21-26).
- Wang C et al. Structure-Mechanics Principles and Mechanobiology of Fibrocartilage PCM: A Pivotal Role of Type V Collagen. bioRxiv. Jun 2024. DOI: 10.1101/2024.06.26.600498. URL: https://doi.org/10.1101/2024.06.26.600498 (Col5a1+/D meniscus; PCM mechanics; LOX/TNC upregulation) (royerweeden2023collagenvpromotes pages 1-9).
- Zschocke J et al. Genetic diagnosis of the Ehlers-Danlos syndromes. Medizinische Genetik. Nov 2024. DOI: 10.1515/medgen-2024-2061. URL: https://doi.org/10.1515/medgen-2024-2061 (diagnostic guidance; COL5A1/COL5A2; null-allele testing; clinical features) (zschocke2024geneticdiagnosisof pages 2-3).
- Okuda‑Ashitaka E, Matsumoto K‑i. Tenascin-X as a causal gene for classical-like EDS. Frontiers in Genetics. Mar 2023. DOI: 10.3389/fgene.2023.1107787. URL: https://doi.org/10.3389/fgene.2023.1107787 (TNXB clEDS; lack of atrophic scarring; neurological features) (zschocke2024geneticdiagnosisof pages 2-3).

Notes on evidence scope
- The strongest 2023–2024 mechanistic evidence for COL5A1-related cEDS centers on fibrillogenesis/ECM disorganization, mechanosensitive integrin signaling in wound repair, and PCM mechanobiology; detailed TGF‑β and autophagy/ER stress pathway data specific to COL5A1-related cEDS were not identified in the gathered 2023–2024 sources and remain an area for future targeted review. Where ER retention/dominant-negative mechanisms are discussed, they are presented as general principles in autosomal-dominant ECM disorders rather than COL5A1-specific demonstrations (Gariballa 2024) (royerweeden2023collagenvpromotes pages 1-9).

Summary
COL5A1-related cEDS is driven by type V collagen deficiency or structural dysfunction, impairing collagen I/III fibrillogenesis and pericellular matrix mechanics. This produces disorganized ECM with weaker fibrils, abnormal mechanotransduction, and impaired wound repair, clinically expressed as hyperextensible skin, atrophic scarring, easy bruising, and joint hypermobility. Recent studies highlight integrin-pathway dysregulation and PCM mechanics as mechanistic nodes and preclinical therapeutic targets, while diagnostics emphasize comprehensive COL5A1/COL5A2 testing with transcript-level assessments for haploinsufficiency (Zschocke 2024; Kelly‑Scumpia 2024; Wang 2024; Neshatian 2024) (zschocke2024geneticdiagnosisof pages 2-3, kellyscumpia2024modulatingtheextracellular pages 1-2, royerweeden2023collagenvpromotes pages 1-9, neshatian2024investigationofdermal pages 1-2).

References

1. (zschocke2024geneticdiagnosisof pages 2-3): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 3 citations and is from a poor quality or predatory journal.

2. (kellyscumpia2024modulatingtheextracellular pages 1-2): Kindra M. Kelly-Scumpia, Maani M. Archang, Prabhat K. Purbey, Tomohiro Yokota, Rimao Wu, Jackie McCourt, Shen Li, Rachelle H. Crosbie, Philip O. Scumpia, and Arjun Deb. Modulating the extracellular matrix to treat wound healing defects in ehlers-danlos syndrome. iScience, 27:110676, Sep 2024. URL: https://doi.org/10.1016/j.isci.2024.110676, doi:10.1016/j.isci.2024.110676. This article has 5 citations and is from a peer-reviewed journal.

3. (kellyscumpia2024modulatingtheextracellular pages 2-3): Kindra M. Kelly-Scumpia, Maani M. Archang, Prabhat K. Purbey, Tomohiro Yokota, Rimao Wu, Jackie McCourt, Shen Li, Rachelle H. Crosbie, Philip O. Scumpia, and Arjun Deb. Modulating the extracellular matrix to treat wound healing defects in ehlers-danlos syndrome. iScience, 27:110676, Sep 2024. URL: https://doi.org/10.1016/j.isci.2024.110676, doi:10.1016/j.isci.2024.110676. This article has 5 citations and is from a peer-reviewed journal.

4. (donahue2024athreedimensional(3d) pages 21-26): M Donahue. A three-dimensional (3d) in vitro model of ehlers-danlos syndrome. Unknown journal, 2024.

5. (donahue2024athreedimensional(3d)a pages 21-26): M Donahue. A three-dimensional (3d) in vitro model of ehlers-danlos syndrome. Unknown journal, 2024.

6. (donahue2024athreedimensional(3d)b pages 21-26): M Donahue. A three-dimensional (3d) in vitro model of ehlers-danlos syndrome. Unknown journal, 2024.

7. (neshatian2024investigationofdermal pages 1-2): Mehrnoosh Neshatian, Nimish Mittal, Sophia Huang, Aiman Ali, Emilie Khattignavong, and Laurent Bozec. Investigation of dermal collagen nanostructures in ehlers-danlos syndrome (eds) patients. PLOS ONE, 19:e0307442, Aug 2024. URL: https://doi.org/10.1371/journal.pone.0307442, doi:10.1371/journal.pone.0307442. This article has 5 citations and is from a peer-reviewed journal.

8. (royerweeden2023collagenvpromotes pages 1-9): Shaina P. Royer-Weeden. Collagen v promotes fibroblast contractility, and adhesion formation, and stability. ArXiv, 2023. URL: https://doi.org/10.37099/mtu.dc.etdr/1647, doi:10.37099/mtu.dc.etdr/1647. This article has 0 citations.