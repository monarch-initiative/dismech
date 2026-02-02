---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T13:56:55.206958'
end_time: '2026-01-31T14:02:55.659728'
duration_seconds: 360.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infectious Disease
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Infectious Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Infectious Disease**.
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
- **Disease Name:** Infectious Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Infectious Disease**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Infectious Disease (general framework across human pathogens)
- MONDO ID: Not a single identifier; refer to pathogen-specific MONDO terms.
- Category: Infectious Disease

## Research Objectives
Comprehensive overview of molecular and cellular mechanisms underlying human infectious disease, with emphasis on 2023–2024 developments and translational implications.

## 1. Core Pathophysiology
Infectious disease pathophysiology emerges from the dynamic interplay between pathogen virulence programs and host defense circuits. Innate pattern recognition by PRRs (e.g., TLRs, RLRs, NLRs, cGAS–STING/cGLRs) triggers type I/III interferon and inflammatory signaling, which in turn induces ISGs and effector programs. Excessive or mistimed responses drive tissue injury, endothelial dysfunction, and organ failure, typified by sepsis and cytokine storm; conversely, late immunosuppression and impaired antimicrobial resistance confer risk for secondary infection. Recent translational work reframes sepsis as heterogenous immune endotypes defined by opposing transcriptional states of “systemic inflammation” versus “antimicrobial resistance” and by axes of immune resistance, disease tolerance, and resilience, motivating precision immunomodulation (URLs, dates, and DOIs below) (brandesleibovitz2024sepsispathogenesisand pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 6-8, shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 5-6).

Mechanistic pillars:
- PRR sensing and interferon programs: Viral RNA/DNA are sensed by RIG-I/MDA5 (RLRs) and cGAS–STING, while endosomal TLRs (e.g., TLR3/7/8/9) and surface TLRs (e.g., TLR2) detect viral and microbial PAMPs. Downstream IRF3/IRF7 and STAT1/STAT2–IRF9 (ISGF3) induce ISGs; dysregulation is a major determinant of disease severity in respiratory viral infections including COVID-19 (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Inflammasomes and programmed inflammatory cell death: NLRP3 activation promotes IL‑1β/IL‑18 maturation and pyroptosis; crosstalk among pyroptosis, apoptosis, and necroptosis (“PANoptosis”) amplifies cytokine storm and multi-organ dysfunction in severe infection and sepsis (you2025rolesofcytokine pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 8-10).
- Sepsis immunobiology: Sepsis heterogeneity reflects imbalanced resistance vs tolerance and organ-specific immune states. “Every organ has a distinctive set of immune sensors and effectors,” underscoring compartmentalized pathobiology and the need for site-specific biomarkers (shankarhari2024reframingsepsisimmunobiology pages 8-10). Transcriptional endotyping shows outcomes relate to the balance between antimicrobial “resistance” programs and a “systemic inflammation” program (brandesleibovitz2024sepsispathogenesisand pages 1-2).
- Cytokine storm networks: Persistent networks including IL‑6, IL‑8, MCP‑1, IL‑10 are implicated early in acute sepsis; IL‑6 emerges as a tractable target with supportive human genetic and interventional evidence (shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - TLR2, TLR3 (PRR sensing; upstream of NF‑κB/IRF3/7) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
  - DDX58/RIG‑I and IFIH1/MDA5 (RLR viral RNA sensors) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
  - MB21D1/cGAS and TMEM173/STING (cytosolic nucleic acid sensing; links to NF‑κB and type I IFN) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
  - IRF3, IRF7; STAT1, STAT2, IRF9 (ISGF3) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
  - NLRP3; CASP1; GSDMD (inflammasome/pyroptosis) (you2025rolesofcytokine pages 1-2).
  - IL6, TNF, IL1B, IL10 (cytokine storm mediators) (shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10, you2025rolesofcytokine pages 1-2).
- Chemical Entities (CHEBI):
  - Cytokines/chemokines such as interleukin‑6 (CHEBI:80354), TNF (CHEBI:27011), IL‑1β (CHEBI:136721), MCP‑1/CCL2 (CHEBI:####) central to storm networks (shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10).
  - Labile heme (CHEBI:30413) as a DAMP linking iron metabolism to regulated cell death and metabolic dysregulation in sepsis; neutralized by haemopexin (shankarhari2024reframingsepsisimmunobiology pages 6-8).
- Cell Types (CL):
  - Neutrophils (CL:0000776): early effector functions and apoptosis drive resolution; dysregulated trafficking contributes to organ injury (shankarhari2024reframingsepsisimmunobiology pages 8-10).
  - Monocytes/macrophages (CL:0000576/CL:0000235): PRR responses, inflammasome activation, and immunometabolic shifts shape outcomes (shankarhari2024reframingsepsisimmunobiology pages 8-10, you2025rolesofcytokine pages 1-2).
  - NK cells (CL:0000623) and T cells (CL:0000084): antiviral effector functions modulated by cytokine milieu; NK impairment noted in severe viral disease (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Anatomical Locations (UBERON):
  - Lung (UBERON:0002048) as primary site in respiratory infections/COVID‑19; organ-specific immunity and compartmentalization emphasized (shankarhari2024reframingsepsisimmunobiology pages 8-10, akkiz2024implicationsofsars‐cov‐2 pages 19-20).
  - Blood/endothelium (UBERON:0000178/UBERON:0001986): systemic inflammation, endothelial dysfunction, and microvascular injury in sepsis (shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 5-6).

## 3. Biological Processes (GO annotation)
- GO:0002221 innate immune response activating cell surface receptor signaling pathway (TLRs) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- GO:0035455 response to type I interferon; GO:0060337 type I interferon signaling (ISGF3) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- GO:0050707 regulation of cytokine secretion; GO:0006954 inflammatory response (shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10).
- GO:0070269 pyroptosis; GO:0140569 PANoptosis-related integration (conceptual) (you2025rolesofcytokine pages 1-2).
- GO:0043312 neutrophil degranulation and GO:0002758 innate immune response signaling (sepsis organ compartmentalization) (shankarhari2024reframingsepsisimmunobiology pages 8-10).
- GO:0006955 immune response; GO:0006952 defense response; GO:0002682 regulation of immune system process (shankarhari2024reframingsepsisimmunobiology pages 8-10, brandesleibovitz2024sepsispathogenesisand pages 1-2).

## 4. Cellular Components
- Endosome and endolysosome (TLR3/7/8/9 localization) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Cytosol and ER-associated compartments (cGAS–STING localization/trafficking to ER–Golgi) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Inflammasome complex (cytosolic NLRP3–ASC–CASP1) (you2025rolesofcytokine pages 1-2).
- Plasma membrane and intercellular junctions/endothelium (cytokine-driven barrier dysfunction in sepsis) (shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 5-6).

## 5. Disease Progression
- Early phase: Pathogen entry and PRR detection elicit IFN and inflammatory cytokines; ISG effectors restrict replication. Viral immune antagonism can blunt IFN while sustaining NF‑κB–biased inflammation, predisposing to tissue injury (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Escalation: Inflammasome activation and PANoptosis amplify DAMP release and cytokine networks (IL‑6/TNF/IL‑1), potentially culminating in cytokine storm, endothelial dysfunction, coagulopathy, and organ failure (you2025rolesofcytokine pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10).
- Sepsis trajectories: Heterogeneous endotypes characterized by high “systemic inflammation” and low “resistance” transcriptional signatures correlate with poor outcomes; organ-specific immune states can diverge from blood, arguing for compartment-informed diagnostics (brandesleibovitz2024sepsispathogenesisand pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 8-10).
- Resolution versus immunosuppression: Active resolution (IL‑10, TGF‑β, neutrophil apoptosis/clearance) may restore homeostasis; alternatively, prolonged immunosuppression with lymphocyte dysfunction increases secondary infection risk (shankarhari2024reframingsepsisimmunobiology pages 8-10).

## 6. Phenotypic Manifestations (HP terms and mechanistic links)
- Fever (HP:0001945) and systemic inflammation via cytokine networks (IL‑6/TNF) (shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10).
- Hypotension (HP:0002615) and shock with endothelial dysfunction; sepsis-related organ dysfunction (multi-organ involvement) (shankarhari2024reframingsepsisimmunobiology pages 8-10, brandesleibovitz2024sepsispathogenesisand pages 1-2).
- Lymphopenia (HP:0001888) and immune paralysis in late sepsis (shankarhari2024reframingsepsisimmunobiology pages 8-10).
- Acute respiratory distress syndrome (ARDS; HP:0033677) in severe respiratory infection and cytokine storm (akkiz2024implicationsofsars‐cov‐2 pages 19-20, reddy2024navigatingthecytokine pages 9-10).

## Applications and Real-World Implementations (2023–2024)
- Precision endotyping in sepsis: Blood transcriptomics delineate resistance vs systemic-inflammation programs to stratify risk and guide immunotherapy; proposed to outperform earlier classifications and to inform target/timing of interventions (Cell Reports Medicine, Nov 2024; https://doi.org/10.1016/j.xcrm.2024.101829) (brandesleibovitz2024sepsispathogenesisand pages 1-2).
- Translational reframing of sepsis immunobiology: Frameworks incorporating resistance, tolerance, resilience; threat scale (soluble PAMPs to “vita‑PAMPs”), and organ compartmentalization inform biomarker development and trial design. IL‑6 highlighted as a priority target; multiplex cytokine profiling and AI-enabled analytics recommended (Lancet Respir Med, Apr 2024; https://doi.org/10.1016/S2213-2600(23)00468-X) (shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 5-6).
- Cytokine-directed therapy and timing: Network-level targeting (e.g., IL‑6 axis) and biomarker-guided selection are emphasized; prior failures often reflect misaligned patient selection/timing (shankarhari2024reframingsepsisimmunobiology pages 5-6). In cytokine storm–dominant sepsis, antagonizing IL‑1/IL‑6/TNF or modulating cell-death pathways is under active study (reddy2024navigatingthecytokine pages 9-10, you2025rolesofcytokine pages 1-2).
- Host-directed tolerance strategies: Preclinical evidence supports targeting labile heme and leveraging autophagy/mitochondrial modulators (e.g., tetracyclines/anthracyclines) to enhance disease tolerance (Lancet Respir Med, 2024) (shankarhari2024reframingsepsisimmunobiology pages 6-8).

## Expert Opinions and Analysis
- Sepsis should be parsed into “resistance vs tolerance vs resilience” programs; organ-specific immune states require compartment-aware biomarkers and earlier, precision interventions. “Every organ has a distinctive set of immune sensors and effectors,” implying blood-only readouts can miss actionable states (Lancet Respir Med, 2024) (shankarhari2024reframingsepsisimmunobiology pages 8-10).
- IL‑6 stands out as a convergent node in acute sepsis; mendelian randomization and COVID‑19 data motivate prioritizing IL‑6–directed strategies in defined endotypes, with attention to timing and cytokine network context (Lancet Respir Med, 2024) (shankarhari2024reframingsepsisimmunobiology pages 5-6).
- Transcriptional R/SI balance provides a clinically useful, mechanism-grounded lens for risk stratification and trial enrichment (Cell Reports Medicine, 2024) (brandesleibovitz2024sepsispathogenesisand pages 1-2).

## Relevant Statistics and Data
- Septic shock mortality remains high; reports note mortality “up to 70%” in severe forms, underscoring urgency for early identification and targeted immunomodulation (Frontiers in Immunology, Nov 2025; https://doi.org/10.3389/fimmu.2025.1696366) (you2025rolesofcytokine pages 1-2).
- Persistent early cytokine networks (including IL‑6, IL‑8, MCP‑1, IL‑10) have been observed over the first 4 days of acute sepsis, supporting the concept of stable inflammatory axes suitable for targeted intervention (Lancet Respir Med, 2024) (shankarhari2024reframingsepsisimmunobiology pages 5-6).

## Evidence Items (PMIDs/DOIs, URLs, dates)
- Shankar-Hari M, Calandra T, Soares MP, et al. Reframing sepsis immunobiology for translation: towards informative subtyping and targeted immunomodulatory therapies. The Lancet Respiratory Medicine. Apr 2024. DOI: 10.1016/S2213-2600(23)00468-X. URL: https://doi.org/10.1016/S2213-2600(23)00468-x (shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 6-8, shankarhari2024reframingsepsisimmunobiology pages 5-6).
- Brandes-Leibovitz R, Netea MG, et al. Sepsis pathogenesis and outcome are shaped by the balance between the transcriptional states of systemic inflammation and antimicrobial response. Cell Reports Medicine. Nov 2024. DOI: 10.1016/j.xcrm.2024.101829. URL: https://doi.org/10.1016/j.xcrm.2024.101829 (brandesleibovitz2024sepsispathogenesisand pages 1-2).
- Akkiz H. Implications of SARS‑CoV‑2 immunity in the context of COVID‑19 pathogenesis, immune evasion, and vaccine effectiveness. Preprints. May 2024. DOI: 10.20944/preprints202405.1826.v1. URL: https://doi.org/10.20944/preprints202405.1826.v1 (PRR/IFN/inflammasome/cell-death mechanisms) (akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Reddy H, et al. Navigating the Cytokine Storm: A Comprehensive Review of Chemokines and Cytokines in Sepsis. Cureus. Feb 2024. DOI: 10.7759/cureus.54275. URL: https://doi.org/10.7759/cureus.54275 (reddy2024navigatingthecytokine pages 9-10).
- You W. Roles of cytokine storm in sepsis progression: biomarkers, and emerging therapeutic strategies. Frontiers in Immunology. Nov 2025. DOI: 10.3389/fimmu.2025.1696366. URL: https://doi.org/10.3389/fimmu.2025.1696366 (PANoptosis; mortality statistic) (you2025rolesofcytokine pages 1-2).

## Structured Annotations (for knowledge base)
- HGNC Genes/Proteins: TLR2; TLR3; DDX58 (RIG‑I); IFIH1 (MDA5); MB21D1 (cGAS); TMEM173 (STING); IRF3; IRF7; STAT1; STAT2; IRF9; NLRP3; CASP1; GSDMD; IL6; TNF; IL1B; IL10 (akkiz2024implicationsofsars‐cov‐2 pages 19-20, you2025rolesofcytokine pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 5-6).
- GO Biological Processes: innate immune signaling (GO:0002221); type I IFN signaling (GO:0060337); inflammatory response (GO:0006954); pyroptosis (GO:0070269); regulation of cytokine secretion (GO:0050707); neutrophil-mediated immunity (GO:0002446); resolution of inflammation (conceptual mapping to GO:0002679) (akkiz2024implicationsofsars‐cov‐2 pages 19-20, shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 5-6).
- Cellular Components: endosome; cytosol; ER–Golgi (STING trafficking); inflammasome complex; plasma membrane/endothelium (akkiz2024implicationsofsars‐cov‐2 pages 19-20, you2025rolesofcytokine pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 8-10).
- Cell Types (CL): neutrophils; monocytes/macrophages; NK cells; T cells (shankarhari2024reframingsepsisimmunobiology pages 8-10, akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Anatomical (UBERON): lung; blood; endothelium; organ-specific tissues reflecting compartmentalized immunity (shankarhari2024reframingsepsisimmunobiology pages 8-10, brandesleibovitz2024sepsispathogenesisand pages 1-2, akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Phenotypes (HP): fever (HP:0001945); hypotension (HP:0002615); lymphopenia (HP:0001888); ARDS (HP:0033677) (shankarhari2024reframingsepsisimmunobiology pages 8-10, reddy2024navigatingthecytokine pages 9-10, brandesleibovitz2024sepsispathogenesisand pages 1-2, akkiz2024implicationsofsars‐cov‐2 pages 19-20).
- Chemicals (CHEBI): interleukin‑6; TNF; IL‑1β; heme (shankarhari2024reframingsepsisimmunobiology pages 5-6, shankarhari2024reframingsepsisimmunobiology pages 6-8, reddy2024navigatingthecytokine pages 9-10).

## Notes on Scope and Gaps
This framework synthesizes cross-cutting mechanisms applicable to viral, bacterial, and fungal infections. Some pathogen‑specific virulence systems (e.g., Type III/IV/VI secretion, quorum sensing, biofilms) and fungal Dectin‑1/2/complement evasion are not directly evidenced in the 2023–2024 items extracted here; they remain established contributors to pathogenesis but should be annotated with pathogen‑specific literature in subsequent iterations.

Citations: (brandesleibovitz2024sepsispathogenesisand pages 1-2, shankarhari2024reframingsepsisimmunobiology pages 6-8, shankarhari2024reframingsepsisimmunobiology pages 8-10, shankarhari2024reframingsepsisimmunobiology pages 5-6, reddy2024navigatingthecytokine pages 9-10, you2025rolesofcytokine pages 1-2, akkiz2024implicationsofsars‐cov‐2 pages 19-20)

References

1. (brandesleibovitz2024sepsispathogenesisand pages 1-2): Rachel Brandes-Leibovitz, Anca Riza, Gal Yankovitz, Andrei Pirvu, Stefania Dorobantu, Adina Dragos, Ioana Streata, Isis Ricaño-Ponce, Aline de Nooijer, Florentina Dumitrescu, Nikolaos Antonakos, Eleni Antoniadou, George Dimopoulos, Ioannis Koutsodimitropoulos, Theano Kontopoulou, Dimitra Markopoulou, Eleni Aimoniotou, Apostolos Komnos, George N. Dalekos, Mihai Ioana, Evangelos J. Giamarellos-Bourboulis, Irit Gat-Viks, and Mihai G. Netea. Sepsis pathogenesis and outcome are shaped by the balance between the transcriptional states of systemic inflammation and antimicrobial response. Cell Reports Medicine, 5:101829, Nov 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101829, doi:10.1016/j.xcrm.2024.101829. This article has 13 citations and is from a peer-reviewed journal.

2. (shankarhari2024reframingsepsisimmunobiology pages 6-8): Manu Shankar-Hari, Thierry Calandra, Miguel P Soares, Michael Bauer, W Joost Wiersinga, Hallie C Prescott, Julian C Knight, Kenneth J Baillie, Lieuwe D J Bos, Lennie P G Derde, Simon Finfer, Richard S Hotchkiss, John Marshall, Peter J M Openshaw, Christopher W Seymour, Fabienne Venet, Jean-Louis Vincent, Christophe Le Tourneau, Anke H Maitland-van der Zee, Iain B McInnes, and Tom van der Poll. Reframing sepsis immunobiology for translation: towards informative subtyping and targeted immunomodulatory therapies. The Lancet Respiratory Medicine, 12:323-336, Apr 2024. URL: https://doi.org/10.1016/s2213-2600(23)00468-x, doi:10.1016/s2213-2600(23)00468-x. This article has 102 citations and is from a highest quality peer-reviewed journal.

3. (shankarhari2024reframingsepsisimmunobiology pages 8-10): Manu Shankar-Hari, Thierry Calandra, Miguel P Soares, Michael Bauer, W Joost Wiersinga, Hallie C Prescott, Julian C Knight, Kenneth J Baillie, Lieuwe D J Bos, Lennie P G Derde, Simon Finfer, Richard S Hotchkiss, John Marshall, Peter J M Openshaw, Christopher W Seymour, Fabienne Venet, Jean-Louis Vincent, Christophe Le Tourneau, Anke H Maitland-van der Zee, Iain B McInnes, and Tom van der Poll. Reframing sepsis immunobiology for translation: towards informative subtyping and targeted immunomodulatory therapies. The Lancet Respiratory Medicine, 12:323-336, Apr 2024. URL: https://doi.org/10.1016/s2213-2600(23)00468-x, doi:10.1016/s2213-2600(23)00468-x. This article has 102 citations and is from a highest quality peer-reviewed journal.

4. (shankarhari2024reframingsepsisimmunobiology pages 5-6): Manu Shankar-Hari, Thierry Calandra, Miguel P Soares, Michael Bauer, W Joost Wiersinga, Hallie C Prescott, Julian C Knight, Kenneth J Baillie, Lieuwe D J Bos, Lennie P G Derde, Simon Finfer, Richard S Hotchkiss, John Marshall, Peter J M Openshaw, Christopher W Seymour, Fabienne Venet, Jean-Louis Vincent, Christophe Le Tourneau, Anke H Maitland-van der Zee, Iain B McInnes, and Tom van der Poll. Reframing sepsis immunobiology for translation: towards informative subtyping and targeted immunomodulatory therapies. The Lancet Respiratory Medicine, 12:323-336, Apr 2024. URL: https://doi.org/10.1016/s2213-2600(23)00468-x, doi:10.1016/s2213-2600(23)00468-x. This article has 102 citations and is from a highest quality peer-reviewed journal.

5. (akkiz2024implicationsofsars‐cov‐2 pages 19-20): Hikmet Akkiz. Implications of sars‐cov‐2 immunity in the context of the pathogenesis of covid‐19, immune evasion of the virus, and the effectiveness of vaccination. May 2024. URL: https://doi.org/10.20944/preprints202405.1826.v1, doi:10.20944/preprints202405.1826.v1.

6. (you2025rolesofcytokine pages 1-2): Weibin You. Roles of cytokine storm in sepsis progression: biomarkers, and emerging therapeutic strategies. Frontiers in Immunology, Nov 2025. URL: https://doi.org/10.3389/fimmu.2025.1696366, doi:10.3389/fimmu.2025.1696366. This article has 4 citations and is from a peer-reviewed journal.

7. (reddy2024navigatingthecytokine pages 9-10): Harshitha Reddy, Chaitanya Kumar Javvaji, Suprit Malali, Sunil Kumar, Sourya Acharya, and Saket Toshniwal. Navigating the cytokine storm: a comprehensive review of chemokines and cytokines in sepsis. Cureus, Feb 2024. URL: https://doi.org/10.7759/cureus.54275, doi:10.7759/cureus.54275. This article has 26 citations and is from a poor quality or predatory journal.