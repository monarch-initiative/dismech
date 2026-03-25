---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T21:46:16.978269'
end_time: '2026-01-08T21:51:08.760682'
duration_seconds: 291.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lyme Disease
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 11
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Lyme Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lyme Disease**.
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
- **Disease Name:** Lyme Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lyme Disease**.
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
- Disease Name: Lyme disease (Borreliella/Borrelia burgdorferi infection)
- MONDO ID: [not provided]
- Category: Infectious

Pathophysiology description (current understanding)
Lyme disease pathophysiology reflects a sequence of vector-mediated inoculation, early dermal colonization, hematogenous dissemination with vascular-interstitial transitions, and tissue-specific persistence, enabled by a large repertoire of outer-surface lipoproteins that coordinate adhesion, immune evasion (especially complement inhibition), and antigenic variation. The host response spans robust innate and adaptive activation with characteristic cytokine/chemokine patterns and, in subsets, post-infectious immune dysregulation (including autoimmunity) that underlies antibiotic-refractory manifestations such as post-infectious Lyme arthritis and post-treatment Lyme disease syndrome (PTLDS). Mechanistic highlights from recent literature (2023–2024 priority; later data included when highly pertinent) are summarized below with genes/proteins and processes mapped to ontology terms.

1) Core pathophysiology
- Immune evasion via complement inhibition and antigenic variation
  • Classical pathway inhibition: The multifunctional surface lipoprotein BBK32 binds C1r (initiator protease of the classical pathway) and reduces C4 deposition, attenuating antibody-dependent complement-mediated killing while simultaneously retaining fibronectin adhesion functionality (mechanistic evidence and imaging/flow cytometry) (https://doi.org/10.1371/journal.ppat.1013361; PLOS Pathogens, 2025) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
  • Alternative pathway inhibition: B. burgdorferi expresses a suite of complement regulator–acquiring surface proteins (CRASPs; e.g., CspA, CspZ, OspE family) that bind factor H or FHL-1 to block alternative pathway activation and membrane attack complex formation; variant-specific factor H binding contributes to host tropism and transmission biology (review synthesis) (farooq2025osteoimmunologicalcharacterizationof pages 42-44, powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
  • Antigenic variation: The vlsE locus undergoes continuous segmental recombination with ~15 silent cassettes during mammalian infection, driving immune escape of surface antigenicity (farooq2025osteoimmunologicalcharacterizationof pages 42-44).

- Dissemination and tissue adhesion
  • BBK32–fibronectin binding supports vascular interactions and, together with glycosaminoglycan (GAG) binding, facilitates endothelial adhesion and extravasation; BBK32’s dual complement- and fibronectin-binding functionalities allow parallel immune evasion and tissue dissemination (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
  • Decorin-binding proteins (DbpA/DbpB) promote ECM engagement and tissue tropism; computational/biophysical evidence further implicates integrin interactions and plasminogen activation in trans-endothelial migration (nasrallah2023screeninginsilico pages 8-14).
  • OspC is upregulated at tick feeding/early mammalian infection and is required for infectivity; OspC–Salp15 interactions contribute to immune evasion at the vector–host interface (farooq2025osteoimmunologicalcharacterizationof pages 42-44).

- Inflammatory drivers and persistence factors
  • Spirochetal peptidoglycan (localized to the periplasmic space with periplasmic flagella) is a potent innate stimulus; in comparative contexts B. burgdorferi evokes higher IL-6, IL-8, IL-10, CCL3/4, and TNF responses than some Eurasian species (farooq2025osteoimmunologicalcharacterizationofa pages 35-38). Motility up to ~4.25 μm/s and chemotaxis toward host carbohydrates (e.g., N-acetylglucosamine) facilitate tissue spread and immune engagement (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
  • Neuroinflammatory cytokines (e.g., IL-6) are implicated in disease models; host IL-6 modulation has been linked to altered neuroinflammatory readouts in preclinical systems (farooq2025osteoimmunologicalcharacterizationof pages 42-44).

- Post-infectious immune dysregulation
  • PTLDS occurs in an estimated 10–20% of appropriately treated patients and has been hypothesized to involve immune dysfunction, autoimmunity, neuroinflammation, and/or persistent antigen; transcriptomic studies report hundreds of genes differentially expressed months after therapy. Clinical evidence also links higher CCL19 at 1 month (e.g., >~112 pg/mL) with a markedly increased odds of PTLDS at 6–12 months (review synthesis) (Cureus, 2024; https://doi.org/10.7759/cureus.64987) (wester2024whatmakesit pages 4-5).

2) Key molecular players
- Genes/Proteins (HGNC symbols where relevant)
  • BBK32 (borrelial lipoprotein; complement C1r inhibitor and fibronectin adhesin) – classical complement pathway evasion; fibronectin binding (GO:0006956; GO:0005515) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
  • CspA (CRASP family; factor H–binding) – alternative pathway inhibition (GO:0030449 complement regulation) (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
  • CspZ (CRASP family; factor H–binding) – host-specific FH binding contributing to tropism (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
  • OspE paralogs (CRASP family; FH/FHL-1 binding) – alternative pathway evasion (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
  • VlsE – antigenic variation via gene conversion; immune evasion (GO:0019048 modulation by host) (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
  • DbpA/DbpB – decorin binding; ECM adhesion and tissue localization (GO:0007155 cell adhesion) (nasrallah2023screeninginsilico pages 8-14).
  • OspC – early infection factor; vector-host immune-modulatory interactions (farooq2025osteoimmunologicalcharacterizationof pages 42-44).

- Chemical entities (CHEBI)
  • Complement components targeted functionally (C1r, C4 deposition reduced by BBK32 activity) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
  • Host GAGs and ECM ligands (fibronectin, decorin) engaged by BBK32/DbpA/DbpB (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14).

- Cell types (CL)
  • Neutrophils and macrophages responding to spirochetal peptidoglycan and lipoproteins (elevated inflammatory cytokines/chemokines) (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
  • Endothelial cells at vascular interface for adhesion/extravasation (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14).
  • T and B lymphocytes in post-infectious dysregulation/autoimmunity hypotheses (wester2024whatmakesit pages 4-5).

- Anatomical locations (UBERON)
  • Skin at bite site; blood vasculature and endothelium during dissemination; joints (synovium) and nervous system in disseminated disease (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14, farooq2025osteoimmunologicalcharacterizationofa pages 35-38, wester2024whatmakesit pages 4-5).

3) Biological processes (candidate GO annotations)
- Complement evasion and regulation: negative regulation of complement activation (GO:0045916); classical pathway inhibition via C1r interaction (BBK32) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
- Adhesion and dissemination: cell adhesion (GO:0007155), extracellular matrix binding (GO:0050840), plasminogen activation-dependent migration (GO:0031639) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14).
- Antigenic variation: DNA recombination and gene conversion (GO:0006310) at vlsE (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- Chemotaxis and motility: chemotaxis (GO:0006935) and locomotion (GO:0040011) of spirochetes (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
- Cytokine-mediated signaling: inflammatory response (GO:0006954) with IL-6, IL-8, TNF, CCL3/4 upregulation (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).

4) Cellular components (GO CC)
- Outer membrane and surface-exposed lipoprotein layer where BBK32, OspC, DbpA/B, and CRASPs reside (GO:0009279 cell outer membrane) (farooq2025osteoimmunologicalcharacterizationof pages 42-44, powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14).
- Extracellular matrix (host) for fibronectin/decorin binding (GO:0031012 extracellular matrix) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14).
- Periplasmic space with peptidoglycan and periplasmic flagella (GO:0030288 outer membrane-bounded periplasmic space) (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).

5) Disease progression (sequence of events)
- Tick feeding induces OspC upregulation and transmission from midgut to salivary glands; early dermal colonization follows (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- Early localized infection: erythema migrans with high local innate activation to lipoproteins/peptidoglycan (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
- Hematogenous dissemination: BBK32–fibronectin and DbpA/B–decorin interactions promote vascular adhesion and tissue entry; classical complement inhibition (BBK32) and alternative pathway inhibition (CRASPs) permit survival in serum and tissues (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14, farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- Disseminated infection: involvement of joints, nervous system, heart; cytokine/chemokine programs vary by tissue, with IL-6 prominent in neuroinflammatory contexts (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- Post-infectious sequelae in subsets: persistent symptoms ≥6 months (PTLDS) with associations to immune dysregulation and elevated early CCL19; autoimmunity hypothesized in joint disease (wester2024whatmakesit pages 4-5).

6) Phenotypic manifestations and mechanistic links (HP terms)
- Early localized skin lesion: erythema migrans (HP:0000978) linked to dermal innate responses to lipoproteins/peptidoglycan (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
- Neuroborreliosis: radiculitis, meningitis, cranial neuropathies (HP:0001288, HP:0003401) with cytokine-driven neuroinflammation (e.g., IL-6) (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- Lyme arthritis: episodic or persistent synovitis (HP:0100769) connected to strong inflammatory responses; in some patients, post-infectious immune dysregulation/autoimmunity (wester2024whatmakesit pages 4-5).
- PTLDS: fatigue, pain, cognitive complaints persisting >6 months after therapy (HP:0012378, HP:0002355) with reported 10–20% incidence and evidence for immune activation signatures (wester2024whatmakesit pages 4-5).

Evidence items (primary literature; URLs and dates where available)
- BBK32 and complement evasion/adhesion: Powell-Pierce AD et al. BBK32 attenuates antibody-dependent complement-mediated killing of infectious Borreliella burgdorferi isolates. PLOS Pathogens, 2025-07; doi:10.1371/journal.ppat.1013361; URL: https://doi.org/10.1371/journal.ppat.1013361 (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
- CRASPs, VlsE antigenic variation, OspC stage regulation, ECM interactions, and IL-6 in neuroinflammation: Farooq I. Osteoimmunological characterization of Borrelia burgdorferi-induced bone loss: From phenotype to molecular mechanisms. 2025 (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- Peptidoglycan location, periplasmic flagella, motility/chemotaxis, and stronger proinflammatory cytokine induction by B. burgdorferi vs. some Eurasian species: Farooq I. 2025 (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
- ECM adhesion repertoire, integrin/plasminogen pathways aiding invasion; DbpA/BBK32 as adhesins: Nasrallah H. Screening in silico… 2023 (nasrallah2023screeninginsilico pages 8-14).
- PTLDS burden (10–20%), transcriptomic persistence after treatment, and early CCL19 as a risk indicator for later PTLDS: Wester KE et al. Cureus, 2024-07; doi:10.7759/cureus.64987; URL: https://doi.org/10.7759/cureus.64987 (wester2024whatmakesit pages 4-5).

Gene/protein annotations with ontology terms
- BBK32 (borrelial lipoprotein; adhesin and complement inhibitor)
  • Functions: fibronectin binding (GO:0005515), negative regulation of classical complement activation (GO:0045916)
  • Process: cell adhesion (GO:0007155); immune evasion (GO:0006956)
  • Cellular component: outer membrane (GO:0009279)
  • Evidence: (powellpierce2025bbk32attenuatesantibodydependent pages 19-20)
- CspA/CspZ/OspE family (CRASPs)
  • Functions: factor H/FHL-1 binding; negative regulation of alternative pathway (GO:0045916)
  • Component: outer membrane (GO:0009279)
  • Evidence: (farooq2025osteoimmunologicalcharacterizationof pages 42-44, powellpierce2025bbk32attenuatesantibodydependent pages 19-20)
- VlsE
  • Process: antigenic variation via gene conversion/recombination (GO:0006310)
  • Component: outer membrane lipoprotein layer (GO:0009279)
  • Evidence: (farooq2025osteoimmunologicalcharacterizationof pages 42-44)
- DbpA/DbpB
  • Functions: decorin binding; ECM binding (GO:0050840)
  • Process: cell adhesion (GO:0007155)
  • Evidence: (nasrallah2023screeninginsilico pages 8-14)
- OspC
  • Process: early infection/host colonization; interaction with Salp15 (vector immune modulation)
  • Evidence: (farooq2025osteoimmunologicalcharacterizationof pages 42-44)

Cell type involvement (CL terms)
- Endothelial cell (CL:0000115): vascular adhesion/extravasation interface (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14)
- Neutrophil (CL:0000096) and macrophage (CL:0000235): early innate cytokine responses to peptidoglycan/lipoproteins (farooq2025osteoimmunologicalcharacterizationofa pages 35-38)
- T cell (CL:0000084) and B cell (CL:0000236): adaptive responses; dysregulation in PTLDS hypotheses (wester2024whatmakesit pages 4-5)

Anatomical locations (UBERON terms)
- Skin (UBERON:0002097): inoculation site and early colonization (farooq2025osteoimmunologicalcharacterizationof pages 42-44)
- Blood vessel/endothelium (UBERON:0001981/0001986): dissemination axis (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14)
- Synovial membrane (UBERON:0002387): Lyme arthritis site (wester2024whatmakesit pages 4-5)
- Central nervous system/meninges (UBERON:0001017/0002410): neuroinflammatory involvement (farooq2025osteoimmunologicalcharacterizationof pages 42-44)

Chemical entities (CHEBI)
- Complement components (e.g., C1r, C4) (CHEBI:4887 C1r; CHEBI:33697 C4) as functional targets of BBK32-mediated inhibition (powellpierce2025bbk32attenuatesantibodydependent pages 19-20)
- Fibronectin (CHEBI:8009; proteinaceous ECM) and decorin (CHEBI:16991; proteoglycan core protein) as host ligands for adhesion (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, nasrallah2023screeninginsilico pages 8-14)
- Glycosaminoglycans (CHEBI:18085) in ECM binding (powellpierce2025bbk32attenuatesantibodydependent pages 19-20)

Expert opinions and analysis (authoritative perspectives)
- Complement evasion is multifactorial and redundant. The BBK32 study demonstrates simultaneous binding to fibronectin and C1r, underscoring that adhesion and immune evasion are coupled rather than sequential, a principle that helps explain efficient dissemination despite antibody/complement pressure (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
- Antigenic variation at vlsE is a sustained, cassette-driven engine for immune escape in mammalian hosts, complementing complement evasion proteins and explaining serologic complexity and persistence under immune pressure (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- PTLDS remains mechanistically heterogeneous; however, data synthesized in recent clinical reviews point to persistent immune activation, early chemokine risk signals (CCL19), and a subset of autoimmune phenomena, aligning with a model of post-infectious immune dysregulation rather than ongoing high-burden viable infection in most cases (wester2024whatmakesit pages 4-5).

Relevant statistics and data
- PTLDS prevalence: approximately 10–20% of treated Lyme disease patients; early elevated CCL19 (~>112 pg/mL at 1 month) associated with markedly higher risk of PTLDS at 6–12 months (wester2024whatmakesit pages 4-5).
- Motility: B. burgdorferi achieves speeds up to ~4.25 μm/s; chemotaxis toward N-acetylglucosamine, glucosamine, chitosan, glutamate reported, consistent with nutrient-sensing dissemination (farooq2025osteoimmunologicalcharacterizationofa pages 35-38).
- Antigenic variation architecture: vlsE with ~15 silent cassettes contributing to continual sequence diversification (farooq2025osteoimmunologicalcharacterizationof pages 42-44).

Limitations and gaps (2023–2024 focus)
- While 2024–2025 primary data robustly support BBK32-mediated classical pathway inhibition and dual-function adhesion, larger in vivo human correlative datasets linking specific adhesin/CRASP expression patterns to clinical phenotypes remain limited (powellpierce2025bbk32attenuatesantibodydependent pages 19-20, farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- High-quality prospective biomarker studies for neuroborreliosis (e.g., CSF chemokines) and PTLDS are still sparse; CCL19 is a candidate but needs external validation and standardization (wester2024whatmakesit pages 4-5).

References (with citation IDs)
- Powell-Pierce AD, et al. BBK32 attenuates antibody-dependent complement-mediated killing… PLOS Pathogens. 2025-07. https://doi.org/10.1371/journal.ppat.1013361 (powellpierce2025bbk32attenuatesantibodydependent pages 19-20)
- Farooq I. Osteoimmunological characterization of Borrelia burgdorferi-induced bone loss… 2025. [Mechanistic review content on CRASPs, vlsE, OspC, IL-6] (farooq2025osteoimmunologicalcharacterizationof pages 42-44)
- Farooq I. Osteoimmunological characterization… (peptidoglycan, motility/chemotaxis, cytokines). 2025. (farooq2025osteoimmunologicalcharacterizationofa pages 35-38)
- Nasrallah H. Screening in silico… OspA/vector proteins; DbpA, BBK32, plasminogen/integrins. 2023. (nasrallah2023screeninginsilico pages 8-14)
- Wester KE, et al. What Makes It Tick: Exploring the Mechanisms of Post-treatment Lyme Disease Syndrome. Cureus. 2024-07. https://doi.org/10.7759/cureus.64987 (wester2024whatmakesit pages 4-5)

Notes on evidence strength
- BBK32 mechanistic inhibition of the classical pathway and concurrent fibronectin binding has strong experimental support (binding/functional assays) (powellpierce2025bbk32attenuatesantibodydependent pages 19-20).
- CRASP-mediated alternative pathway evasion and vlsE-driven antigenic variation are supported by convergent lines of evidence across models (farooq2025osteoimmunologicalcharacterizationof pages 42-44).
- PTLDS immunopathophysiology remains an active research area; clinical synthesis suggests immune dysregulation and biomarkers such as CCL19 may stratify risk, but causal chains are not fully established (wester2024whatmakesit pages 4-5).

References

1. (powellpierce2025bbk32attenuatesantibodydependent pages 19-20): Alexandra D. Powell-Pierce, Charles E. Booth, Payton G. Smith, Brittany L. Shapiro, Shannon S. Allen, Brandon L. Garcia, and Jon T. Skare. Bbk32 attenuates antibody-dependent complement-mediated killing of infectious borreliella burgdorferi isolates. PLOS Pathogens, 21:e1013361, Jul 2025. URL: https://doi.org/10.1371/journal.ppat.1013361, doi:10.1371/journal.ppat.1013361. This article has 0 citations and is from a highest quality peer-reviewed journal.

2. (farooq2025osteoimmunologicalcharacterizationof pages 42-44): I Farooq. Osteoimmunological characterization of borrelia burgdorferi-induced bone loss: from phenotype to molecular mechanisms. Unknown journal, 2025.

3. (nasrallah2023screeninginsilico pages 8-14): H NASRALLAH. Screening in silico delle interazioni proteina-proteina tra borrelia burgdorferi e zecche: uno studio di fattibilità su ospa e proteine salivari di zecca. Unknown journal, 2023.

4. (farooq2025osteoimmunologicalcharacterizationofa pages 35-38): I Farooq. Osteoimmunological characterization of borrelia burgdorferi-induced bone loss: from phenotype to molecular mechanisms. Unknown journal, 2025.

5. (wester2024whatmakesit pages 4-5): Kate E Wester, Bianca C Nwokeabia, Rehana Hassan, Taylor Dunphy, Michael Osondu, Carson Wonders, and Misbahuddin Khaja. What makes it tick: exploring the mechanisms of post-treatment lyme disease syndrome. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64987, doi:10.7759/cureus.64987. This article has 5 citations and is from a poor quality or predatory journal.