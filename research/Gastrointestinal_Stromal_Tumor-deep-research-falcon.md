---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-01-24T18:43:51.519968'
end_time: '2026-01-24T18:43:51.521581'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gastrointestinal Stromal Tumor
  mondo_id: ''
  category: ''
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
- **Disease Name:** Gastrointestinal Stromal Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Gastrointestinal Stromal Tumor**.
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
- **Disease Name:** Gastrointestinal Stromal Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Gastrointestinal Stromal Tumor**.
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
- Disease Name: Gastrointestinal Stromal Tumor (GIST)
- MONDO ID: not specified in available sources
- Category: Mesenchymal tumor of the gastrointestinal tract

Pathophysiology description
GISTs are mesenchymal neoplasms arising from or sharing lineage with interstitial cells of Cajal (ICC), the GI pacemaker cells that physiologically express KIT and orchestrate peristaltic signaling ("GISTs mostly derive from Cajal cell precursors"), explaining the near-universal diagnostic utility of KIT (CD117) and DOG1 immunostaining (publication date: 27 Feb 2023) (unk2023molecularmechanismsof pages 1-2). Constitutive activation of receptor tyrosine kinases (RTKs)—most commonly KIT and less often PDGFRA—drives ligand‑independent signaling through MAPK and PI3K/AKT cascades to promote proliferation, survival, and tumor progression (publication date: 27 Feb 2023; 30 Mar 2023) (unk2023molecularmechanismsof pages 1-2, catalano2023moleculartailoredtherapeutic pages 1-2). SDH-deficient GIST represents a distinct metabolic/epigenetic class characterized by loss of succinate dehydrogenase activity, oncometabolite (succinate) accumulation, and genome‑wide hypermethylation that alters transcriptional programs and hypoxia signaling; this subtype is typically KIT/PDGFRA-wild type and shows reduced sensitivity to classical KIT-directed TKIs (publication dates: Feb 2024; May 2024) (zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13). Rarer drivers include NF1 loss (RAS pathway hyperactivation), BRAF V600E, and fusions affecting NTRK or FGFR1, which converge on MAPK/PI3K networks and confer sensitivity to pathway- or fusion-directed agents in select cases (publication dates: 27 Feb 2023; May 2024) (unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).

Direct quotes supporting key statements
- “Gastrointestinal stromal tumors (GISTs) are soft tissue sarcomas that mostly derive from Cajal cell precursors… identified using characteristic immunohistochemical staining for CD117 and DOG1.” (27 Feb 2023; URL: https://doi.org/10.3390/cancers15051498) (unk2023molecularmechanismsof pages 1-2)
- “Gain-of-function mutations in KIT or PDGFRA genes represent the driving mutations in more than 90% of all GISTs.” (27 Feb 2023; URL: https://doi.org/10.3390/cancers15051498) (unk2023molecularmechanismsof pages 1-2)
- “SDH-deficient GISTs… [show] metabolic consequences with oncometabolite succinate accumulation and epigenetic reprogramming.” (Feb 2024; URL: https://doi.org/10.1186/s12964-023-01411-x) (zhou2024kitmutationsand pages 16-17)
- “Advances in DNA and RNA sequencing… revealed novel, potentially actionable drivers… including… NTRK3 (ETV6‑NTRK3) or FGFR1 (FGFR1‑TACC1).” (May 2024; URL: https://doi.org/10.5935/2526-8732.20240468) (lima2024gastrointestinalstromaltumors pages 12-13)

1) Core Pathophysiology
- Primary mechanisms: Constitutive RTK activation (KIT, PDGFRA) drives downstream MAPK and PI3K/AKT/mTOR signaling; SDH loss produces succinate accumulation that inhibits α‑ketoglutarate–dependent dioxygenases (e.g., KDMs/TETs), causing global DNA/histone hypermethylation and pseudohypoxia programs; RAS pathway activation appears in NF1- or BRAF‑driven tumors; rare NTRK/FGFR fusions act as oncogenic drivers converging on MAPK/PI3K (publication dates: 27 Feb 2023; Feb 2024; May 2024; 30 Mar 2023) (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13, catalano2023moleculartailoredtherapeutic pages 1-2).
- Dysregulated pathways: RTK signaling; MAPK cascade; PI3K/AKT/mTOR; epigenetic regulation in SDH-deficient GIST; possible Hippo/YAP‑TAZ activation in KIT‑independent states (publication dates: Feb 2024; 2024) (zhou2024kitmutationsand pages 16-17, pedone2024evaluationofgene pages 13-17).
- Affected cellular processes: Cell-cycle progression and survival signaling downstream of KIT/PDGFRA; metabolic rewiring and epigenetic remodeling in SDH deficiency; lineage programs of ICC-like cells; potential TME-mediated immune suppression contributing to resistance (publication dates: 27 Feb 2023; Feb 2024; 2024) (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, pedone2024evaluationofgene pages 13-17).

2) Key Molecular Players
- Genes/Proteins (HGNC): KIT; PDGFRA; SDHA/SDHB/SDHC/SDHD; NF1; BRAF; NTRK1/2/3; FGFR1 (publication dates: 27 Feb 2023; May 2024; Feb 2024) (unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13, zhou2024kitmutationsand pages 16-17).
- Chemical Entities (CHEBI): Succinate (oncometabolite in SDH-deficient GIST) (Feb 2024; May 2024) (zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13).
- Cell Types (CL): Interstitial cells of Cajal as the putative cell of origin; tumor/immune stromal constituents variably represented (27 Feb 2023) (unk2023molecularmechanismsof pages 1-2).
- Anatomical Locations (UBERON): Stomach and small intestine are dominant primary sites; gastric GIST is enriched for PDGFRA and SDH-deficient tumors; small intestine shows a higher frequency of KIT exon 9 and NF1-associated cases (30 Mar 2023; May 2024) (catalano2023moleculartailoredtherapeutic pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).

3) Biological Processes (GO annotation)
- Positive regulation of MAPK cascade; RAS signaling; phosphatidylinositol 3‑kinase signaling; receptor tyrosine kinase signaling; cell cycle progression; metabolic process of TCA cycle; regulation of chromatin organization and DNA methylation (27 Feb 2023; Feb 2024; May 2024; 2024) (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13, pedone2024evaluationofgene pages 13-17).

4) Cellular Components (GO/locations)
- Plasma membrane (KIT/PDGFRA RTKs); cytosol and nucleus (MAPK/PI3K signal transduction and transcriptional responses); mitochondrion (SDH complex in inner mitochondrial membrane); extracellular space (ligands/growth factors); potential Golgi retention of KIT under certain resistance states (Feb 2024) (zhou2024kitmutationsand pages 16-17).

5) Disease Progression
- Sequence of events: Initiating driver alteration (KIT/PDGFRA activation; SDH loss; or NF1/BRAF/fusion) → constitutive signaling or metabolic/epigenetic dysregulation → expansion of ICC‑lineage tumor cells → local growth and risk-stratified progression by size/mitoses/site → metastatic spread (commonly liver/peritoneum) → under TKI pressure, emergence of heterogeneous secondary resistance mutations (especially multiple subclones with secondary KIT mutations) and/or pathway reactivation or noncanonical RTK trafficking (publication dates: 27 Feb 2023; Feb 2024; 30 Mar 2023) (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, catalano2023moleculartailoredtherapeutic pages 1-2).
- Distinct stages/phases: Localized resectable disease; advanced/metastatic disease (systemic therapy required); resistance evolution under sequential TKIs (imatinib→sunitinib→regorafenib→ripretinib; avapritinib for PDGFRA D842V) (30 Mar 2023) (catalano2023moleculartailoredtherapeutic pages 1-2).

6) Phenotypic Manifestations (HPO-style)
- Gastrointestinal bleeding, abdominal pain/mass, anemia, and obstruction correlate with tumor location/size; multifocal gastric tumors in SDH-deficient or syndromic contexts; early‑onset presentation in SDH-deficient and pediatric cases; indolent but metastatic potential in SDH-deficient subtype; immunohistochemical KIT (CD117) and DOG1 positivity as diagnostic phenotypes (publication dates: 27 Feb 2023; May 2024; 30 Mar 2023) (unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13, catalano2023moleculartailoredtherapeutic pages 1-2).

Recent developments and latest research (2023–2024 priority)
- KIT/PDGFRA and resistance biology: A 2024 mechanistic review synthesizes how KIT expression/trafficking, PI3K-driven KIT overexpression, and noncanonical maintenance (e.g., “Golgi retention”) sustain oncogenic signaling and contribute to imatinib resistance, underscoring the need for strategies that suppress MAPK/PI3K reactivation and address intracellular localization (publication date: 12 Feb 2024; URL: https://doi.org/10.1186/s12964-023-01411-x) (zhou2024kitmutationsand pages 16-17).
- SDH-deficient GIST: 2024–2024 reviews highlight succinate-driven inhibition of 2‑OG–dependent dioxygenases and the resulting global hypermethylation as central to pathogenesis. Comprehensive profiling reveals frequent SDH subunit alterations and SDHC epimutations, and advocates broader germline/methylation testing in wild-type GISTs (publication dates: Feb 2024; May 2024; URLs: https://doi.org/10.1186/s12964-023-01411-x; https://doi.org/10.5935/2526-8732.20240468) (zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13).
- Rare drivers and fusion biology: 2023–2024 reviews report NTRK (ETV6‑NTRK3) and FGFR1 (FGFR1‑TACC) fusions in triple‑negative GIST, with therapeutic implications for TRK/FGFR inhibition; emerging cases and panels now capture these events more routinely (publication dates: May 2024; 2024; URLs: https://doi.org/10.5935/2526-8732.20240468) (lima2024gastrointestinalstromaltumors pages 12-13, pedone2024evaluationofgene pages 13-17).
- Therapy implications: 2023 and 2024 overviews reiterate mutation-tailored sequencing of TKIs (imatinib, sunitinib, regorafenib, ripretinib; avapritinib for PDGFRA D842V) and emphasize comprehensive genomic profiling in wild‑type GIST to detect NF1/BRAF/fusion drivers guiding non‑KIT therapy (publication dates: 30 Mar 2023; 27 Feb 2023; URLs: https://doi.org/10.3390/cancers15072074; https://doi.org/10.3390/cancers15051498) (catalano2023moleculartailoredtherapeutic pages 1-2, unk2023molecularmechanismsof pages 1-2).

Current applications and real-world implementations
- Diagnostics: Standard IHC with KIT (CD117) and DOG1, with reflex next‑generation sequencing to define KIT/PDGFRA exon variants, detect SDH deficiency (including immunohistochemical SDHB loss and SDHC promoter methylation), and find alternative oncogenic drivers (publication dates: 30 Mar 2023; 27 Feb 2023; May 2024) (catalano2023moleculartailoredtherapeutic pages 1-2, unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).
- Treatment: Mutation‑guided TKI selection (e.g., imatinib sensitivity for most KIT exon 11/9; avapritinib for PDGFRA D842V; reduced TKI benefit in SDH‑deficient/NF1), and consideration of tumor‑agnostic TRK inhibitors when NTRK fusions are present (publication dates: 30 Mar 2023; May 2024) (catalano2023moleculartailoredtherapeutic pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).
- Surveillance and risk: Integration of anatomic site, size, and mitotic count in risk models, acknowledging distinct behaviors (e.g., gastric SDH-deficient patterns) (publication date: 30 Mar 2023) (catalano2023moleculartailoredtherapeutic pages 1-2).

Expert opinions and analysis (authoritative sources)
- Reviews from 2023–2024 converge on a model wherein KIT/PDGFRA signaling and SDH‑loss epigenetics represent two principal and biologically divergent axes of GIST pathogenesis. These demand tailored diagnostics (IHC + exon‑level sequencing + SDH IHC/methylation + fusion detection) and tailored therapeutics (mutation‑specific TKIs vs. metabolic/epigenetic or pathway‑directed strategies), with emerging attention to resistance mechanisms beyond kinase mutations (e.g., altered trafficking, pathway rewiring) (publication dates: 27 Feb 2023; 12 Feb 2024; 30 Mar 2023) (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, catalano2023moleculartailoredtherapeutic pages 1-2).

Relevant statistics and data from recent studies
- Molecular frequency (approximate ranges summarized across recent reviews): KIT mutations ~75–80%, PDGFRA ~5–10%, wild‑type (including SDH‑deficient, NF1, BRAF, fusion‑positive) ~15%—with SDH deficiency a notable subset in wild‑type disease (publication dates: 30 Mar 2023; 27 Feb 2023; May 2024) (catalano2023moleculartailoredtherapeutic pages 1-2, unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).
- Diagnostic performance: KIT (CD117) IHC positive in >95% of cases, while DOG1 adds sensitivity, particularly in KIT‑negative cases (publication date: 30 Mar 2023) (catalano2023moleculartailoredtherapeutic pages 1-2).

Ontology-structured annotations
- Genes/Proteins (HGNC): KIT; PDGFRA; SDHA; SDHB; SDHC; SDHD; NF1; BRAF; NTRK1; NTRK2; NTRK3; FGFR1 (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13, catalano2023moleculartailoredtherapeutic pages 1-2).
- Biological Processes (GO): receptor tyrosine kinase signaling; MAPK cascade; phosphatidylinositol 3‑kinase signaling; cell cycle; tricarboxylic acid cycle; regulation of chromatin organization; DNA methylation (unk2023molecularmechanismsof pages 1-2, zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13, pedone2024evaluationofgene pages 13-17).
- Cellular Components (GO): plasma membrane (KIT/PDGFRA); mitochondrion inner membrane (SDH complex); cytosol and nucleus (signal transduction/transcription); Golgi apparatus (noncanonical KIT trafficking in resistance) (zhou2024kitmutationsand pages 16-17, unk2023molecularmechanismsof pages 1-2).
- Cell Types (CL): interstitial cells of Cajal; tumor-associated immune/stromal cells (concept) (unk2023molecularmechanismsof pages 1-2, pedone2024evaluationofgene pages 13-17).
- Anatomical Locations (UBERON): stomach; small intestine (jejunum/ileum) (catalano2023moleculartailoredtherapeutic pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).
- Chemical Entities (CHEBI): succinate (zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13).
- Phenotype associations (HPO examples): gastrointestinal bleeding; abdominal mass; anemia; early-onset neoplasm (SDH-deficient); multifocal gastric tumors (SDH-deficient/NF1 contexts) (unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13).

Embedded summary artifact
| Category | Item (ontology) | Mechanistic role in GIST | Subtype(s) | Key downstream / related pathways | Notes on therapeutic relevance | Evidence sources |
|---|---|---|---|---|---|---|
| Driver RTK | KIT (HGNC:KIT) | Constitutive activating RTK (gain-of-function mutations, often exon 11/9) driving proliferation/survival | KIT-mutant GIST (majority) | MAPK (RAS/RAF/MEK/ERK), PI3K/AKT/mTOR, JAK/STAT | Primary target of imatinib; secondary KIT mutations cause acquired resistance; guides TKI choice | (zhou2024kitmutationsand pages 16-17, catalano2023moleculartailoredtherapeutic pages 1-2) |
| Driver RTK | PDGFRA (HGNC:PDGFRA) | Activating RTK mutations (e.g., exon 18 D842V) → ligand-independent signaling | PDGFRA-mutant GIST (subset) | MAPK, PI3K/AKT | PDGFRA D842V is primary imatinib‑resistant; avapritinib effective for D842V | (zhou2024kitmutationsand pages 16-17, catalano2023moleculartailoredtherapeutic pages 1-2) |
| Metabolic tumor suppressor | SDHA/SDHB/SDHC/SDHD (SDH complex) | Loss of SDH → succinate accumulation (oncometabolite), metabolic rewiring and epigenetic hypermethylation | SDH-deficient GIST (KIT/PDGFRA‑WT) | TCA cycle disruption; inhibition of 2‑OG–dependent dioxygenases → altered chromatin/HIF signaling | Poor TKI sensitivity; rationale for metabolic/epigenetic therapeutic strategies | (pedone2024evaluationofgene pages 13-17, lima2024gastrointestinalstromaltumors pages 12-13, zhou2024kitmutationsand pages 16-17) |
| RAS-pathway regulator | NF1 (HGNC:NF1) | Tumor suppressor loss → RAS pathway hyperactivation | NF1‑associated / wild‑type GIST (often multifocal, small intestine) | RAS/MAPK | Less benefit from imatinib; profiling can reveal alternate actionable nodes | (lima2024gastrointestinalstromaltumors pages 12-13, unk2023molecularmechanismsof pages 1-2) |
| MAPK driver | BRAF (HGNC:BRAF) | Oncogenic mutations (e.g., V600E) activate MAPK signaling in a minority of cases | BRAF‑mutant GIST (rare) | MAPK | May respond to BRAF-targeted therapy in select cases | (pedone2024evaluationofgene pages 13-17, unk2023molecularmechanismsof pages 1-2) |
| Fusion oncogenes | NTRK fusions (HGNC:NTRK1/2/3) | Fusion → constitutive TRK kinase activity activating proliferation/survival programs | Triple‑WT / fusion‑positive GISTs (rare) | MAPK, PI3K, PLCγ | Tumor‑agnostic TRK inhibitors (larotrectinib/entrectinib) are effective when present | (pedone2024evaluationofgene pages 13-17, lima2024gastrointestinalstromaltumors pages 12-13) |
| Fusion oncogenes | FGFR1 fusions (HGNC:FGFR1) | Constitutive FGFR signaling via fusions/amplification | WT/fusion GIST subsets (rare) | MAPK, PI3K/AKT, PLCγ | FGFR inhibitors considered experimentally; potential mechanism of imatinib resistance via bypass signaling | (lima2024gastrointestinalstromaltumors pages 12-13, pedone2024evaluationofgene pages 13-17) |
| Core signaling | PI3K/AKT pathway (GO) | Mediates survival, metabolism and growth downstream of RTKs | Across KIT/PDGFRA and some WT GISTs | PI3K → AKT → mTOR | Targetable with PI3K/mTOR axis inhibitors in trials/combination strategies | (zhou2024kitmutationsand pages 16-17, catalano2023moleculartailoredtherapeutic pages 1-2) |
| Core signaling | MAPK pathway (GO:MAPK cascade) | Drives proliferation and transcriptional programs downstream of RTKs/RAS | Across multiple molecular subtypes | RAS → RAF → MEK → ERK | MAPK pathway reactivation contributes to resistance; MAPK-targeting strategies under investigation | (zhou2024kitmutationsand pages 16-17, unk2023molecularmechanismsof pages 1-2) |
| Transcriptional regulator | Hippo / YAP‑TAZ (GO) | YAP/TAZ activation promotes KIT‑independent proliferation and drug resistance | Imatinib‑resistant / KIT‑independent tumors (models) | TEAD‑mediated transcription → CCND1, CTGF | Preclinical rationale for YAP inhibition to overcome KIT‑independence | (pedone2024evaluationofgene pages 13-17) |
| Cell of origin | Interstitial cells of Cajal (CL:interstitial cells of Cajal) | Putative cell‑of‑origin with KIT expression and pacemaker physiology | Gastric and small intestinal GIST | KIT signaling axis | Explains lineage marker expression (KIT/DOG1) and tissue predilection | (unk2023molecularmechanismsof pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13) |
| Tumor ecosystem | Tumor microenvironment / immune features (concept) | Immune cell composition (Tregs, IDO1+ DCs, TAMs), immunosuppressive interactions contribute to resistance and progression | Advanced / imatinib‑resistant GISTs show distinct immunosuppressive signatures | Immune checkpoints, TIGIT‑NECTIN2, BTLA‑TNFRSF14 axes | Limited ICI activity so far; TME profiling may enable combination immunotherapies | (zhou2024kitmutationsand pages 16-17, unk2023molecularmechanismsof pages 1-2) |
| Anatomy | Stomach; small intestine / jejunum (UBERON:stomach; UBERON:small_intestine) | Primary anatomical sites with differing molecular spectra (gastric vs small bowel) | Gastric GIST (more PDGFRA/SDH), small intestine (more KIT exon9, NF1) | — | Site influences prognosis, risk stratification and surgical approach | (catalano2023moleculartailoredtherapeutic pages 1-2, lima2024gastrointestinalstromaltumors pages 12-13) |
| Metabolite / oncometabolite | Succinate (CHEBI:succinate) | Accumulates with SDH loss → inhibits 2‑OG‑dependent dioxygenases → epigenetic reprogramming and HIF stabilization | SDH‑deficient GIST | TCA cycle disruption; epigenetic modifiers (KDMs) affected | Targets: epigenetic modulators, metabolic interventions (emerging) | (zhou2024kitmutationsand pages 16-17, lima2024gastrointestinalstromaltumors pages 12-13) |
| Diagnostic marker | DOG1 (ANO1; HGNC:ANO1) | Sensitive IHC marker for GIST diagnosis independent of mutation | All histologic subtypes | — | Important diagnostic marker when KIT IHC/clinical context ambiguous | (catalano2023moleculartailoredtherapeutic pages 1-2) |
| Diagnostic marker | CD117 (KIT) IHC marker | High sensitivity (>95%) reflecting KIT protein expression | All / KIT‑mutant and many WT GISTs | — | Standard diagnostic test; correlates with KIT pathway activity | (catalano2023moleculartailoredtherapeutic pages 1-2, unk2023molecularmechanismsof pages 1-2) |
| Resistance mechanisms | PDGFRA D842V; secondary KIT mutations; noncanonical KIT trafficking (Golgi retention) | Primary resistance (D842V), acquired polyclonal secondary KIT mutations, and alternative KIT localization/trafficking sustaining signaling | Drives primary non‑response or later relapse across treated patients | Alters inhibitor binding or reactivates MAPK/PI3K | Therapeutic implications: avapritinib for D842V; sequential TKIs (sunitinib/regorafenib/ripretinib); need for combination/novel agents | (zhou2024kitmutationsand pages 16-17, catalano2023moleculartailoredtherapeutic pages 1-2, qasim2026gastrointestinalstromaltumors pages 1-2) |


*Table: Compact table summarizing molecular, cellular, metabolic, diagnostic, and resistance anchors in GIST, with ontology tags and primary evidence references to inform mechanistic understanding and therapeutic decisions.*

Evidence items (with URLs and publication dates)
- Zhou et al., Cell Communication and Signaling. “KIT mutations and expression… overcoming IM resistance in GIST.” Published 12 Feb 2024. URL: https://doi.org/10.1186/s12964-023-01411-x (zhou2024kitmutationsand pages 16-17)
- Unk et al., Cancers. “Molecular Mechanisms of GIST and Impact on Therapy.” Published 27 Feb 2023. URL: https://doi.org/10.3390/cancers15051498 (unk2023molecularmechanismsof pages 1-2)
- Catalano et al., Cancers. “Molecular Tailored Therapeutic Options for GISTs.” Published 30 Mar 2023. URL: https://doi.org/10.3390/cancers15072074 (catalano2023moleculartailoredtherapeutic pages 1-2)
- Lima et al., Brazilian Journal of Oncology. “Advances in molecular characterization and therapeutic implications.” Published May 2024. URL: https://doi.org/10.5935/2526-8732.20240468 (lima2024gastrointestinalstromaltumors pages 12-13)
- Pedone et al., 2024. “Evaluation of gene expression and gene fusions in GIST” (publication venue/URL not specified in retrieved record) (pedone2024evaluationofgene pages 13-17)
- Qasim et al., Cureus. “GIST: histopathological spectrum, molecular subtypes, targeted therapy.” Published Jan 2026. URL: https://doi.org/10.7759/cureus.101180 (qasim2026gastrointestinalstromaltumors pages 11-12, qasim2026gastrointestinalstromaltumors pages 2-3, qasim2026gastrointestinalstromaltumors pages 1-2)

Limitations
Some items above cite narrative or regional reviews; direct primary datasets for certain statistics (e.g., exact subtype frequencies by site) were summarized from recent reviews rather than meta-analyses. Fusion prevalence remains low and heterogeneous across cohorts; detection depends on assay sensitivity (lima2024gastrointestinalstromaltumors pages 12-13, pedone2024evaluationofgene pages 13-17).

References

1. (unk2023molecularmechanismsof pages 1-2): Mojca Unk, Barbara Jezeršek Novaković, and Srdjan Novaković. Molecular mechanisms of gastrointestinal stromal tumors and their impact on systemic therapy decision. Cancers, 15:1498, Feb 2023. URL: https://doi.org/10.3390/cancers15051498, doi:10.3390/cancers15051498. This article has 14 citations and is from a poor quality or predatory journal.

2. (catalano2023moleculartailoredtherapeutic pages 1-2): Fabio Catalano, Malvina Cremante, Bruna Dalmasso, Chiara Pirrone, Agostina Lagodin D’Amato, Massimiliano Grassi, and Danila Comandini. Molecular tailored therapeutic options for advanced gastrointestinal stromal tumors (gists): current practice and future perspectives. Cancers, 15:2074, Mar 2023. URL: https://doi.org/10.3390/cancers15072074, doi:10.3390/cancers15072074. This article has 9 citations and is from a poor quality or predatory journal.

3. (zhou2024kitmutationsand pages 16-17): Shishan Zhou, Omar Abdihamid, Fengbo Tan, Haiyan Zhou, Heli Liu, Zhi Li, Sheng Xiao, and Bin Li. Kit mutations and expression: current knowledge and new insights for overcoming im resistance in gist. Cell Communication and Signaling : CCS, Feb 2024. URL: https://doi.org/10.1186/s12964-023-01411-x, doi:10.1186/s12964-023-01411-x. This article has 48 citations.

4. (lima2024gastrointestinalstromaltumors pages 12-13): Nildevande Firmino Lima, Marcello Moro Queiroz, Julia Sousa Leal Franco, Julia Sousa Lins, Eduardo Felício de Campos, Beatriz Mendes Awni, Luiz Guilherme Cernaglia Aureliano de Lima, Frederico Teixeira, Fábio de Oliveira Ferreira, Eduardo Hiroshi Akaishi, Fernanda Cunha Capareli, and Rodrigo Ramella Munhoz. Gastrointestinal stromal tumors: advances in molecular characterization and therapeutic implications. Brazilian Journal of Oncology, May 2024. URL: https://doi.org/10.5935/2526-8732.20240468, doi:10.5935/2526-8732.20240468. This article has 0 citations.

5. (pedone2024evaluationofgene pages 13-17): E Pedone. Evaluation of gene expression profile and gene fusions in gastrointestinal stromal tumors: looking for novel predictive and prognostic biomarkers. Unknown journal, 2024.

6. (qasim2026gastrointestinalstromaltumors pages 1-2): Hussein Qasim, Mohammad Abu Shugaer, Ahmad N Awawdeh, Tamara Dawaymeh, Karis Khattab, Musallam Al-oweiwi, Matteo Luigi Giuseppe Leoni, and Giustino Varrassi. Gastrointestinal stromal tumors: histopathological spectrum, molecular subtypes, and implications for targeted therapy. Cureus, Jan 2026. URL: https://doi.org/10.7759/cureus.101180, doi:10.7759/cureus.101180. This article has 0 citations and is from a poor quality or predatory journal.

7. (qasim2026gastrointestinalstromaltumors pages 11-12): Hussein Qasim, Mohammad Abu Shugaer, Ahmad N Awawdeh, Tamara Dawaymeh, Karis Khattab, Musallam Al-oweiwi, Matteo Luigi Giuseppe Leoni, and Giustino Varrassi. Gastrointestinal stromal tumors: histopathological spectrum, molecular subtypes, and implications for targeted therapy. Cureus, Jan 2026. URL: https://doi.org/10.7759/cureus.101180, doi:10.7759/cureus.101180. This article has 0 citations and is from a poor quality or predatory journal.

8. (qasim2026gastrointestinalstromaltumors pages 2-3): Hussein Qasim, Mohammad Abu Shugaer, Ahmad N Awawdeh, Tamara Dawaymeh, Karis Khattab, Musallam Al-oweiwi, Matteo Luigi Giuseppe Leoni, and Giustino Varrassi. Gastrointestinal stromal tumors: histopathological spectrum, molecular subtypes, and implications for targeted therapy. Cureus, Jan 2026. URL: https://doi.org/10.7759/cureus.101180, doi:10.7759/cureus.101180. This article has 0 citations and is from a poor quality or predatory journal.