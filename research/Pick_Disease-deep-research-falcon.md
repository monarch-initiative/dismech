---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:02:02.243636'
end_time: '2025-12-15T09:10:21.701669'
duration_seconds: 499.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pick Disease
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Pick Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pick Disease**.
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
- **Disease Name:** Pick Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pick Disease**.
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
- Disease Name: Pick disease (PiD; Pick’s disease)
- MONDO ID: [to be confirmed]
- Category: Complex, primary tauopathy within FTLD-tau (3R tau)

## Research Objectives: Pathophysiology of Pick disease (molecular and cellular mechanisms)

### 1. Core Pathophysiology
Pick disease is a primary FTLD-tau tauopathy defined by intraneuronal inclusions (“Pick bodies”) composed predominantly of 3-repeat (3R) tau that assemble into a disease-specific filament fold (the “Pick fold”), distinct from Alzheimer’s disease (AD) and 4R tauopathies such as PSP and CBD (cryo-EM structural classification) (schweighauser2024noveltaufilament pages 11-17). Structural data link isoform composition (3R) to fold identity and downstream consequences for seeding competence and ligand binding. In PiD, tau misfolds and propagates in a prion-like manner, templating native tau to adopt disease-specific conformers that spread along neural networks (schweighauser2024noveltaufilament pages 11-17). Together with tau-driven microtubule dysfunction, this leads to axonal transport deficits and synaptic toxicity in selectively vulnerable circuits, with prominent neocortical and hippocampal involvement (kawles2024phenotypicallyconcordantdistribution pages 1-2, schweighauser2024noveltaufilament pages 11-17).

Neuroinflammatory features are present in FTLD-tau, including PiD cohorts. Post-mortem analyses show astrocyte reactivity (increased GFAP, reduced glutamate-cycling markers) associated with phosphorylated tau burden; microglia show relatively modest activation overall yet exhibit associations between specific microglial markers and pTau epitopes. Adaptive immune involvement is supported by upregulated chemokines and recruitment of CD4+ and CD8+ T cells into affected cortex, correlating with pTau and glial markers (hartnell2024glialreactivityand pages 2-3). These immune signatures likely modulate disease microenvironments but appear qualitatively distinct from AD-type microglial activation (hartnell2024glialreactivityand pages 2-3).

Imaging-pathology correlation indicates that a second-generation tau PET tracer, 18F-florzolotau, binds in vivo to 3R tau in PiD and co-localizes with AT8-immunoreactive Pick bodies, with strong region-wise correlation of cortical SUVR to AT8 burden (r = 0.81, p < 0.001). In contrast, 18F-flortaucipir has shown limited sensitivity to some 3R folds, consistent with ligand–fold selectivity (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4, schweighauser2024noveltaufilament pages 11-17).

### 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - MAPT (HGNC:6833): causal gene encoding tau. A deletion mutation ΔK281 in MAPT produces familial PiD with 3R tau inclusions and cryo-EM filaments indistinguishable from sporadic Pick fold, establishing a direct genetic–structural link for PiD (Acta Neuropathologica, 2023; open-access DOI below) (schweighauser2024noveltaufilament pages 11-17).
  - Tau PTMs/epitopes: disease-associated phosphorylated tau (AT8 pSer202/pThr205 and other epitopes) define regional burden in PiD and correlate with glial/immune readouts (hartnell2024glialreactivityand pages 2-3, suzuki2025neuropathologicalcorrelationsof pages 2-4).
- Cell Types (CL terms):
  - Neurons (principal cellular substrate of Pick bodies); astrocytes (reactive; altered glutamate cycling) (CL:0000127); microglia (innate immune associations with pTau); CD4+ and CD8+ T cells (adaptive infiltration) (hartnell2024glialreactivityand pages 2-3, kawles2024phenotypicallyconcordantdistribution pages 1-2).
- Anatomical Locations (UBERON terms):
  - Neocortex with clinicotype-specific foci: middle frontal gyrus (MFG; frontal cortex; bvFTD) and anterior temporal lobe (ATL; PPA), plus marked vulnerability of hippocampus, especially dentate gyrus (kawles2024phenotypicallyconcordantdistribution pages 1-2). Basal ganglia and frontotemporal regions can be prominently involved in vivo by PET (suzuki2025neuropathologicalcorrelationsof pages 2-4).
- Chemical Entities (CHEBI):
  - 18F-florzolotau (tau PET radioligand) demonstrates in vivo detectability of 3R tau pathology in PiD; 18F-flortaucipir shows limited sensitivity for some 3R folds (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4, schweighauser2024noveltaufilament pages 11-17).

### 3. Biological Processes (GO) and 4. Cellular Components
- Disrupted biological processes (selected GO terms):
  - Tau-driven cytoskeletal dysfunction and axonal transport impairment (GO:0007018 microtubule-based movement; GO:0007010 cytoskeleton organization) (schweighauser2024noveltaufilament pages 11-17, kawles2024phenotypicallyconcordantdistribution pages 1-2).
  - Prion-like seeding/propagation of tau assemblies (pathological protein aggregation and intercellular propagation processes) (schweighauser2024noveltaufilament pages 11-17).
  - Neuroinflammatory signaling and immune cell recruitment (chemokines) in FTLD-tau, including PiD (hartnell2024glialreactivityand pages 2-3).
- Cellular components:
  - Axon/neurites (GO:0030424 axon), neuronal soma and neuropil threads (sites of pathological tau accumulation and spread) (kawles2024phenotypicallyconcordantdistribution pages 1-2, schweighauser2024noveltaufilament pages 11-17).

### 5. Disease Progression (sequence of events and stages)
- Initiation and molecular misfolding: disease-specific misfolding of 3R tau leads to formation of Pick fold filaments, which define PiD inclusions (Pick bodies). These aggregates seed further tau misfolding in a prion-like manner and spread across connected networks (schweighauser2024noveltaufilament pages 11-17).
- Regional vulnerability and clinicotype: distributions of Pick bodies align with phenotype—frontal-dominant peaks (MFG) in behavioral variant FTD, temporal-dominant peaks (ATL, leftward asymmetry) in PPA. Hippocampal (DG) burden is disproportionately high in both groups, implying a common limbic vulnerability alongside neocortical patterns (kawles2024phenotypicallyconcordantdistribution pages 1-2).
- Microenvironmental modulation: astrocyte reactivity and chemokine-driven T-cell recruitment associate with pTau epitopes, suggesting adaptive immunity participates as pathology accumulates; microglial activation is relatively modest but shows epitope–marker associations (hartnell2024glialreactivityand pages 2-3).
- In vivo detectability and late-stage confirmation: 18F-florzolotau PET can reveal regional 3R tau burden with strong correlation to postmortem AT8 pathology in PiD, whereas some first-generation ligands (flortaucipir) may miss 3R folds, stressing fold-specific imaging (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4, schweighauser2024noveltaufilament pages 11-17).

### 6. Phenotypic Manifestations (and links to mechanisms)
- Clinical syndromes: bvFTD and PPA are the most common PiD phenotypes. Pathology quantitation shows clinicopathologic concordance: frontal Pick body peaks in bvFTD, anterior temporal peaks (left-asymmetric STG/IPL) in PPA; both feature marked hippocampal DG burden (mechanistic link to episodic memory/limbic dysfunction) (kawles2024phenotypicallyconcordantdistribution pages 1-2).
- Key metrics: In an 18-case autopsy series (9 bvFTD, 9 PPA), mean age at onset ≈ 58–59 years, mean age at death ≈ 69 years, and mean disease duration ≈ 10.3 years, illustrating the tempo and demographic range of autopsy-confirmed PiD (kawles2024phenotypicallyconcordantdistribution pages 1-2).


Embedded summary table (ontology cross-refs and citations):
|Category|Specific item|Role/mechanism (1–2 lines)|Evidence (authors year)|PMID / DOI|URL|Notes|
|---|---|---|---|---|---|---|
|Core mechanism|3R tau "Pick" filament fold|Disease-specific 3R tau filament conformation that defines Pick disease pathology and influences seeding/ligand binding.|Schweighauser et al. 2024 (schweighauser2024noveltaufilament pages 11-17)|DOI: 10.1101/2024.08.15.608062|https://doi.org/10.1101/2024.08.15.608062|Cryo-EM shows Pick fold composed of 3R tau; impacts PET ligand binding and strain behaviour.|
|Gene/Protein|MAPT ΔK281 (HGNC:MAPT)|MAPT deletion ΔK281 causes familial PiD with abundant 3R tau inclusions and Pick-fold filaments identical to sporadic PiD.|Schweighauser et al. / Schweighauser et al. 2023 (schweighauser2024noveltaufilament pages 11-17)|DOI: 10.1007/s00401-023-02598-6|https://doi.org/10.1007/s00401-023-02598-6|Genetic evidence linking a MAPT variant to PiD (HGNC:MAPT).|
|Core mechanism|Prion-like seeding / propagation|Misfolded tau seeds propagate between cells, templating aggregation and spreading pathology along networks.|Schweighauser et al. 2024 (schweighauser2024noveltaufilament pages 11-17)|DOI: 10.1101/2024.08.15.608062|https://doi.org/10.1101/2024.08.15.608062|Mechanistic basis for network spread of 3R tau aggregates.|
|Cell type (CL:0000127)|Astrocytes|Astrocyte reactivity (↑GFAP) and reduced glutamate-cycling markers associate with pTau in FTLD-tau/PiD, implying astrocytic dysfunction.|Hartnell et al. 2024 (hartnell2024glialreactivityand pages 2-3)|DOI: 10.1093/brain/awad309|https://doi.org/10.1093/brain/awad309|Astrocyte involvement linked to pTau burden and altered metabolism.|
|Cell type|Microglia|Overall modest microglial activation in FTLD-tau, but specific microglial markers associate with pTau epitopes and chemokine expression in PiD.|Hartnell et al. 2024 (hartnell2024glialreactivityand pages 2-3)|DOI: 10.1093/brain/awad309|https://doi.org/10.1093/brain/awad309|Microglia–tau associations detected but activation patterns differ from AD.|
|Cell type|T lymphocytes (CD4+/CD8+)|Chemokine-driven recruitment of CD4+ and CD8+ T cells into PiD brain regions correlates with pTau and glial markers.|Hartnell et al. 2024 (hartnell2024glialreactivityand pages 2-3)|DOI: 10.1093/brain/awad309|https://doi.org/10.1093/brain/awad309|Suggests adaptive-immune involvement in FTLD-tau/PiD.|
|Anatomy (UBERON:0001870)|Middle frontal gyrus (frontal cortex)|bvFTD cases with PiD show peak Pick body density in MFG consistent with frontal-dominant clinical syndrome.|Kawles et al. 2024 (kawles2024phenotypicallyconcordantdistribution pages 1-2)|DOI: 10.1186/s40478-024-01738-7|https://doi.org/10.1186/s40478-024-01738-7|Clinicopathologic concordance: frontal pathology → bvFTD phenotype.|
|Anatomy|Anterior temporal lobe (ATL)|PPA cases with PiD show maximal Pick body burden in ATL with leftward asymmetry, matching language phenotype.|Kawles et al. 2024 (kawles2024phenotypicallyconcordantdistribution pages 1-2)|DOI: 10.1186/s40478-024-01738-7|https://doi.org/10.1186/s40478-024-01738-7|Clinicopathologic concordance: temporal pathology → PPA phenotype.|
|Anatomy|Dentate gyrus (DG) / hippocampus|Hippocampus (notably DG) shows disproportionately high Pick body burden in PiD, indicating hippocampal vulnerability.|Kawles et al. 2024 (kawles2024phenotypicallyconcordantdistribution pages 1-2)|DOI: 10.1186/s40478-024-01738-7|https://doi.org/10.1186/s40478-024-01738-7|Hippocampal involvement notable despite neocortical syndrome.|
|Chemical/Drug (ChEBI)|18F‑florzolotau (tau PET)|In vivo 18F‑florzolotau retention correlates with regional AT8-positive Pick body burden (r = 0.81), demonstrating PET detectability of 3R tau in PiD.|Suzuki et al. 2025 (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4)|DOI: 10.1186/s13550-025-01296-6|https://doi.org/10.1186/s13550-025-01296-6|Supports utility of some second‑generation tau tracers for 3R tau imaging.|
|Chemical/Drug|18F‑flortaucipir (limitation)|Flortaucipir shows limited sensitivity to certain 3R tau Pick-folds and mutant-specific filament conformations, leading to variable detection in PiD.|Schweighauser et al. 2024; Suzuki 2025 (schweighauser2024noveltaufilament pages 11-17, suzuki2025neuropathologicalcorrelationsof pages 4-7)|DOIs: 10.1101/2024.08.15.608062; 10.1186/s13550-025-01296-6|https://doi.org/10.1101/2024.08.15.608062; https://doi.org/10.1186/s13550-025-01296-6|Ligand binding depends on filament fold/isoform composition.|
|Process (GO:0007018)|Microtubule-based movement / axonal transport|Imbalance of tau isoforms (3R vs 4R) and tau aggregation disrupts microtubule stabilization and axonal transport, contributing to synaptic/neuronal dysfunction.|Schweighauser et al. 2024; Kawles et al. 2024 (schweighauser2024noveltaufilament pages 11-17, kawles2024phenotypicallyconcordantdistribution pages 1-2)|DOI: 10.1101/2024.08.15.608062; 10.1186/s40478-024-01738-7|https://doi.org/10.1101/2024.08.15.608062; https://doi.org/10.1186/s40478-024-01738-7|Annotate with GO:0007018; MAPT (HGNC:MAPT) dysfunction central.|
|Cellular Component (GO:0030424)|Axon / neuronal neurites|Pathological tau accumulates in neuronal soma and neurites, impairing axonal compartments and synaptic integrity.|Kawles et al. 2024; Schweighauser et al. 2024 (kawles2024phenotypicallyconcordantdistribution pages 1-2, schweighauser2024noveltaufilament pages 11-17)|DOI: 10.1186/s40478-024-01738-7; 10.1101/2024.08.15.608062|https://doi.org/10.1186/s40478-024-01738-7; https://doi.org/10.1101/2024.08.15.608062|Annotate with GO:0030424 (axon).|


*Table: Compact, citable summary table of key mechanistic features, molecular/cellular actors, anatomical patterns, processes, and imaging/chemical tools in Pick disease (PiD), with primary evidence citations (context IDs) and DOIs/URLs for rapid knowledgebase curation.*


## Evidence Highlights with URLs and Dates
- Cryo-EM and fold-based classification (2024 preprint; bioRxiv): “Novel tau filament folds in individuals with MAPT mutations P301L and P301T” — establishes disease-specific folds, cites ΔK281 → PiD with Pick fold; discusses fold selectivity and ligand binding. DOI: 10.1101/2024.08.15.608062 (posted Aug 2024). URL: https://doi.org/10.1101/2024.08.15.608062 (schweighauser2024noveltaufilament pages 11-17)
- Genetic causality and structural identity (2023; peer-reviewed): “Mutation ΔK281 in MAPT causes Pick’s disease” (Acta Neuropathologica, Jun 2023). DOI: 10.1007/s00401-023-02598-6. URL: https://doi.org/10.1007/s00401-023-02598-6 (schweighauser2024noveltaufilament pages 11-17)
- Clinicopathologic concordance (2024; peer-reviewed): “Phenotypically concordant distribution of pick bodies in aphasic versus behavioral dementias” (Acta Neuropathologica Communications, Feb 2024). DOI: 10.1186/s40478-024-01738-7. URL: https://doi.org/10.1186/s40478-024-01738-7 (kawles2024phenotypicallyconcordantdistribution pages 1-2)
- Neuroinflammation and adaptive immunity (2024; peer-reviewed): “Glial reactivity and T cell infiltration in frontotemporal lobar degeneration with tau pathology” (Brain, Sep 2024). DOI: 10.1093/brain/awad309. URL: https://doi.org/10.1093/brain/awad309 (hartnell2024glialreactivityand pages 2-3)
- In vivo 3R tau imaging and pathology correlation in PiD (2025; peer-reviewed): “Neuropathological correlations of 18F-florzolotau PET in a case with Pick’s disease” (EJNMMI Research, Jul 2025). DOI: 10.1186/s13550-025-01296-6. URL: https://doi.org/10.1186/s13550-025-01296-6 (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4)


## Structured Knowledge Base Annotations
- Pathophysiology description:
  - Primary 3R tauopathy with disease-specific filament (Pick fold), prion-like propagation, and selective network vulnerability in frontal and anterior temporal systems and hippocampus; neuroimmune modulation with astrocyte reactivity and adaptive T-cell infiltration (schweighauser2024noveltaufilament pages 11-17, kawles2024phenotypicallyconcordantdistribution pages 1-2, hartnell2024glialreactivityand pages 2-3).

- Gene/protein annotations:
  - MAPT (HGNC:6833): causal (ΔK281) PiD; protein: tau (3R isoforms predominant in PiD inclusions). Mechanisms: misfolding/aggregation into Pick fold; impaired microtubule stabilization/axonal transport; prion-like seeding (schweighauser2024noveltaufilament pages 11-17).

- Biological process (GO) annotations:
  - GO:0007018 microtubule-based movement; GO:0007010 cytoskeleton organization (tau dysfunction) (schweighauser2024noveltaufilament pages 11-17).
  - Protein aggregation, intercellular propagation (prion-like seeding) (schweighauser2024noveltaufilament pages 11-17).
  - Chemokine-mediated immune cell migration; astrocyte reactivity with altered glutamate cycling (hartnell2024glialreactivityand pages 2-3).

- Cellular component (GO/CC) annotations:
  - GO:0030424 axon; neuronal soma and neurites; hippocampal dentate gyrus granule cells (anatomical cell populations bearing inclusions) (kawles2024phenotypicallyconcordantdistribution pages 1-2).

- Phenotype associations (HP terms, examples):
  - HP:0000737 Behavioral disinhibition; HP:0000719 Apathy; HP:0002460 Progressive aphasia; HP:0002354 Memory impairment. Clinicotype aligns with regional Pick body distributions (MFG → bvFTD; ATL → PPA) (kawles2024phenotypicallyconcordantdistribution pages 1-2).

- Cell type involvement (CL terms):
  - CL:0000540 neuron; CL:0000127 astrocyte; CL:0000234 microglial cell; CD4+ and CD8+ T lymphocytes (hartnell2024glialreactivityand pages 2-3, kawles2024phenotypicallyconcordantdistribution pages 1-2).

- Anatomical locations (UBERON terms):
  - UBERON:0001870 frontal cortex (middle frontal gyrus); UBERON:0001871 temporal lobe (anterior temporal lobe); UBERON:0001954 hippocampal formation (dentate gyrus) (kawles2024phenotypicallyconcordantdistribution pages 1-2).

- Chemical entities (CHEBI):
  - CHEBI: [radiotracers] 18F-florzolotau (tau PET; detects 3R tau in PiD with strong pathology correlation); 18F-flortaucipir (limited sensitivity to some 3R folds) (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4, schweighauser2024noveltaufilament pages 11-17).

- Evidence items (with PMIDs/DOIs/URLs):
  - Cryo-EM folds and propagation: bioRxiv 2024; DOI: 10.1101/2024.08.15.608062; https://doi.org/10.1101/2024.08.15.608062 (schweighauser2024noveltaufilament pages 11-17).
  - Genetic causality: Acta Neuropathologica 2023; DOI: 10.1007/s00401-023-02598-6; https://doi.org/10.1007/s00401-023-02598-6 (schweighauser2024noveltaufilament pages 11-17).
  - Clinicopathology: Acta Neuropathologica Communications 2024; DOI: 10.1186/s40478-024-01738-7; https://doi.org/10.1186/s40478-024-01738-7 (kawles2024phenotypicallyconcordantdistribution pages 1-2).
  - Neuroinflammation and T cells: Brain 2024; DOI: 10.1093/brain/awad309; https://doi.org/10.1093/brain/awad309 (hartnell2024glialreactivityand pages 2-3).
  - PET–pathology correlation: EJNMMI Research 2025; DOI: 10.1186/s13550-025-01296-6; https://doi.org/10.1186/s13550-025-01296-6 (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4).


## Expert Opinions and Analysis (authoritative sources, prioritized 2023–2024)
- Fold-based nosology advances: Disease-defining filament folds (e.g., Pick fold) unify clinicopathologic features with tau isoform biology and explain differences in tracer binding and model generalizability; extrapolating from P301 mutants requires caution because mutant-specific folds can differ from sporadic tauopathies (schweighauser2024noveltaufilament pages 11-17).
- Immune microenvironment: FTLD-tau, including PiD, exhibits astrocytic reactivity and chemokine signatures that recruit T cells rather than the robust AD-like microglial activation profile; therapeutic targeting may need to prioritize astrocyte metabolism and adaptive immune axes alongside tau proteostasis (hartnell2024glialreactivityand pages 2-3).
- Imaging implications: “AT8-positive areas exhibited a significant positive correlation with 18F-florzolotau binding in the corresponding [cortical] regions (Pearson’s r = 0.81, p < 0.001)” and many Pick bodies were co-labeled by non-radioactive florzolotau fluorescence and AT8, supporting 3R tau PET quantification with this tracer; flortaucipir limitations reflect fold selectivity (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4, schweighauser2024noveltaufilament pages 11-17).


## Relevant Statistics and Data from Recent Studies
- Autopsy series (PiD, 18 cases: 9 bvFTD; 9 PPA): mean onset ≈ 58–59 years; mean age at death ≈ 69 years; mean disease duration ≈ 10.33 years. Regional Pick body density peaks aligned with phenotype (MFG in bvFTD; ATL in PPA), with significant leftward STG asymmetry in PPA and rightward STG asymmetry in bvFTD; hippocampal DG showed disproportionately high inclusion burden in both phenotypes (kawles2024phenotypicallyconcordantdistribution pages 1-2).
- PET–pathology correlation (single-case, PiD): cortical 18F-florzolotau SUVR vs AT8-positive area r = 0.81, p < 0.001; frontotemporal dominance including orbital/inferior frontal and inferior temporal regions; negative amyloid PET (11C-PiB) (suzuki2025neuropathologicalcorrelationsof pages 4-7, suzuki2025neuropathologicalcorrelationsof pages 2-4).


## Direct Supporting Quotations (selected)
- “A novel three-lobed tau fold resembling the two-layered tau fold of Pick’s disease was present…”; the authors reference ΔK281 MAPT mutation producing tau filaments indistinguishable from PiD, underscoring fold-defined nosology (Schweighauser 2024 preprint) (schweighauser2024noveltaufilament pages 11-17).
- “AT8-positive areas exhibited a significant positive correlation with 18F-florzolotau binding in the corresponding regions (Pearson’s r = 0.81, p < 0.001)” (Suzuki 2025) (suzuki2025neuropathologicalcorrelationsof pages 4-7).
- “FTLD-tau is associated with astrocyte reactivity… and involvement of adaptive immunity in the form of chemokine-driven recruitment of T lymphocytes” (Hartnell 2024) (hartnell2024glialreactivityand pages 2-3).
- “Neocortical Pick body distributions align with clinical phenotype: bvFTD showed peak densities in the MFG, whereas PPA had maximal involvement of the ATL… hippocampus [DG] disproportionately burdened” (Kawles 2024) (kawles2024phenotypicallyconcordantdistribution pages 1-2).


## Gaps and Open Questions
- Complement activation, oligodendroglial pathology, and endolysosomal/autophagic impairments in PiD were not directly evidenced in the retrieved 2023–2024 PiD-focused sources above and remain areas for targeted follow-up.
- Population-level prevalence of PiD within FTLD was not captured in the current evidence set.


References: see Evidence Highlights (with URLs and dates). All assertions are supported by the context-linked sources above.


References

1. (schweighauser2024noveltaufilament pages 11-17): Manuel Schweighauser, Yang Shi, Alexey G. Murzin, Holly J. Garringer, Ruben Vidal, Jill R. Murrell, M. Elena Erro, Harro Seelaar, Isidro Ferrer, John C. van Swieten, Bernardino Ghetti, Sjors H.W. Scheres, and Michel Goedert. Novel tau filament folds in individuals with mapt mutations p301l and p301t. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.15.608062, doi:10.1101/2024.08.15.608062. This article has 8 citations and is from a poor quality or predatory journal.

2. (kawles2024phenotypicallyconcordantdistribution pages 1-2): Allegra Kawles, Rachel Keszycki, Grace Minogue, Antonia Zouridakis, Ivan Ayala, Nathan Gill, Alyssa Macomber, Vivienne Lubbat, Christina Coventry, Emily Rogalski, Sandra Weintraub, Qinwen Mao, Margaret E. Flanagan, Hui Zhang, Rudolph Castellani, Eileen H. Bigio, M.-Marsel Mesulam, Changiz Geula, and Tamar Gefen. Phenotypically concordant distribution of pick bodies in aphasic versus behavioral dementias. Acta Neuropathologica Communications, Feb 2024. URL: https://doi.org/10.1186/s40478-024-01738-7, doi:10.1186/s40478-024-01738-7. This article has 2 citations and is from a peer-reviewed journal.

3. (hartnell2024glialreactivityand pages 2-3): Iain J Hartnell, Declan Woodhouse, William Jasper, Luke Mason, Pavan Marwaha, Manon Graffeuil, Laurie C Lau, Jeanette L Norman, David S Chatelet, Luc Buee, James A R Nicoll, David Blum, Guillaume Dorothee, and Delphine Boche. Glial reactivity and t cell infiltration in frontotemporal lobar degeneration with tau pathology. Brain, 147:590-606, Sep 2024. URL: https://doi.org/10.1093/brain/awad309, doi:10.1093/brain/awad309. This article has 34 citations and is from a highest quality peer-reviewed journal.

4. (suzuki2025neuropathologicalcorrelationsof pages 4-7): Hisaomi Suzuki, Manabu Kubota, Shin Kurose, Kenji Tagai, Hironobu Endo, Mitsumoto Onaya, Yasuharu Yamamoto, Naruhiko Sahara, Masahiro Ohgidani, Chie Haga, Hiroya Hara, Haruhiko Akiyama, Keisuke Takahata, and Makoto Higuchi. Neuropathological correlations of 18f-florzolotau pet in a case with pick’s disease. EJNMMI Research, Jul 2025. URL: https://doi.org/10.1186/s13550-025-01296-6, doi:10.1186/s13550-025-01296-6. This article has 2 citations and is from a peer-reviewed journal.

5. (suzuki2025neuropathologicalcorrelationsof pages 2-4): Hisaomi Suzuki, Manabu Kubota, Shin Kurose, Kenji Tagai, Hironobu Endo, Mitsumoto Onaya, Yasuharu Yamamoto, Naruhiko Sahara, Masahiro Ohgidani, Chie Haga, Hiroya Hara, Haruhiko Akiyama, Keisuke Takahata, and Makoto Higuchi. Neuropathological correlations of 18f-florzolotau pet in a case with pick’s disease. EJNMMI Research, Jul 2025. URL: https://doi.org/10.1186/s13550-025-01296-6, doi:10.1186/s13550-025-01296-6. This article has 2 citations and is from a peer-reviewed journal.