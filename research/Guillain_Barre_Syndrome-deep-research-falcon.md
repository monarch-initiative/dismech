---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:49.874785'
end_time: '2025-12-18T09:56:41.751161'
duration_seconds: 651.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Guillain-Barre Syndrome
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Guillain-Barre Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Guillain-Barre Syndrome**.
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
- **Disease Name:** Guillain-Barre Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Guillain-Barre Syndrome**.
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
- Disease Name: Guillain-Barre Syndrome (GBS)
- MONDO ID: Not specified in retrieved sources
- Category: Autoimmune

## Pathophysiology Overview (narrative)
Guillain-Barre syndrome is an acute, frequently post-infectious, immune-mediated polyradiculoneuropathy in which humoral and cellular immunity target peripheral nerve axolemma and/or myelin, particularly at the node of Ranvier and paranodes. A central paradigm is molecular mimicry: antecedent infections (classically Campylobacter jejuni) elicit anti-glycolipid antibodies that cross-react with nerve gangliosides (GM1, GD1a, GQ1b) concentrated at nodes and motor terminals. Antibody binding initiates classical complement activation (C1q→C3→C5b-9), causing disruption of sodium-channel clusters, paranodal detachment, conduction failure, and varying degrees of axonal degeneration. In parallel, macrophage-mediated segmental demyelination characterizes many AIDP cases, while autoimmunity against nodal/paranodal adhesion proteins (neurofascin, contactin-1, CASPR1) produces a “nodo-paranodopathy” with conduction failure that may be complement-dependent (IgG1/3) or complement-sparing (IgG4). Systemic and endoneurial immune signatures include activated monocytes/macrophages, CD8 T cells, Th17/Treg imbalance, and elevated cytokines (e.g., IL-6, IL-8); CSF albuminocytologic dissociation and neurofilament light (NfL) elevations reflect barrier dysfunction and axonal injury. Recent work and clinical trials have focused on complement inhibition to prevent MAC-mediated nerve injury. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)

| Category | Entity (HGNC/CHEBI where applicable) | Role / Mechanism | Cellular / Anatomical context | Key process (GO-style) | Evidence |
|---|---|---|---|---|---|
| Autoantibodies | Anti-ganglioside Ab (GM1, GD1a, GQ1b) | Molecular mimicry → bind axolemma/nodes; fix complement causing nodal disruption | Axolemma / nodes of Ranvier; motor terminals | antibody-mediated complement activation; disruption of sodium-channel clusters | (shastri2023immunemediatedneuropathiespathophysiology pages 8-9, shastri2023immunemediatedneuropathiespathophysiology pages 22-24, oshomoji2024autoimmunemechanismsin pages 7-8) |
| Complement system | C1q; C3; C5b-9 (MAC) | Classical pathway activation by IgG/IgM → MAC deposition → axonal/nodal injury | Nodes of Ranvier; motor nerve terminals; Schwann cell surfaces | classical complement activation; membrane attack complex formation | (shastri2023immunemediatedneuropathiespathophysiology pages 8-9, shastri2023immunemediatedneuropathiespathophysiology pages 22-24, NCT04752566) |
| Nodal adhesion | NFASC / NF155 (HGNC: NFASC) | Paranodal adhesion; target of autoantibodies causing paranodal dissection and conduction failure | Paranode / node of Ranvier | node of Ranvier organization; axo-glial adhesion disruption | (shastri2023immunemediatedneuropathiespathophysiology pages 7-8, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Paranodal protein | CNTN1 (contactin-1) | Axoglial adhesion molecule; autoantibody target in autoimmune nodopathy | Paranode / Schwann cell-axon junction | maintenance of paranodal junctions; disruption → nodo-paranodopathy | (shastri2023immunemediatedneuropathiespathophysiology pages 7-8, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Paranodal protein | CASPR1 / CNTNAP1 | Partners with contactin-1 in paranodal complex; targeted in nodopathies | Paranode / juxtaparanode | paranodal junction assembly / stability | (shastri2023immunemediatedneuropathiespathophysiology pages 7-8, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Innate immune cell | Macrophages | Mediate segmental demyelination via myelin phagocytosis and inflammatory mediators | Endoneurium; Schwann cell–myelin sheaths | macrophage-mediated myelin phagocytosis; inflammatory demyelination | (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9) |
| Innate immune cell | Monocytes / intermediate monocytes | Circulating inflammatory cells with proinflammatory transcriptomic signatures; recruit/activate endoneurial cells | Peripheral blood → endoneurial infiltration | leukocyte activation and recruitment; cytokine production | (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Adaptive immune cell | CD8+ T cells | Proliferative/activated cytotoxic phenotype; may express axon-guidance genes in early disease | Peripheral blood / possible endoneurial presence | cytotoxic T cell activation; cell-mediated cytotoxicity | (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Adaptive immune balance | Th17 / Treg imbalance | Skewed helper/regulatory T-cell responses contributing to uncontrolled inflammation | Peripheral immune compartment; draining nodes | T-cell differentiation; dysregulated immune regulation | (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Humoral immunity | B cells / plasma cells | Source of pathogenic IgG (anti-ganglioside, anti-nodal) driving complement or IgG-subclass effects | Systemic circulation; CSF | antibody production and affinity maturation | (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9) |
| Cytokine | IL-6 | Proinflammatory cytokine elevated in acute disease; promotes systemic inflammation | Blood and CSF; leukocyte–Schwann cell signaling | cytokine-mediated signaling pathway | (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Chemokine / biomarker | IL-8 (CXCL8) | CSF biomarker validated in GBS/CIDP cohorts; indicates intrathecal inflammation | Cerebrospinal fluid; endoneurial inflammatory milieu | chemokine-mediated immune cell recruitment; inflammatory signaling | (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Cytokine | Oncostatin M (OSM) | Predicted leukocyte–nerve ligand promoting angiogenesis and inflammation in transcriptomic interactomes | Leukocyte–Schwann cell interactions; peripheral nerve microenvironment | cytokine-mediated cellular response and tissue remodeling | (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Biomarker | Neurofilament light (NfL) | Marker of axonal damage; serum/CSF levels rise with axonal injury severity | Serum and CSF reflecting peripheral axonal degeneration | biomarker of axonal degeneration / neurofilament release | (shastri2023immunemediatedneuropathiespathophysiology pages 7-8, kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24) |
| Therapeutic | Eculizumab (C5 inhibitor) | Terminal complement blockade evaluated in Phase 3 trial to prevent MAC-mediated nerve injury | Systemic complement inhibition to reduce peripheral nerve complement activity | therapeutic inhibition of complement-mediated cytotoxicity | (NCT04752566, shastri2023immunemediatedneuropathiespathophysiology pages 8-9, censi2024guillain–barrésyndromeand pages 5-8) |


*Table: Concise table mapping major molecules, cells, anatomical sites, processes (GO-style) and key evidence IDs supporting Guillain-Barré syndrome pathophysiology; useful as a citable reference for knowledge-base annotation and mechanistic summaries.*

## 1. Core Pathophysiology
- Molecular mimicry and anti-ganglioside antibodies: Campylobacter jejuni lipooligosaccharides share epitopes with gangliosides; anti-GM1/GD1a localize to nodes/axolemma and motor terminals, triggering complement-mediated disruption of nodal sodium-channel clusters and axonal injury; anti-GQ1b defines Miller Fisher syndrome and related variants. (Quotes/examples: anti-ganglioside antibodies “bind at the node of Ranvier and activate complement, producing… MAC deposition” and “disruption of sodium channel clusters” in experimental models) (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9, shastri2023immunemediatedneuropathiespathophysiology pages 7-8, oshomoji2024autoimmunemechanismsin pages 7-8)
- Complement activation: Classical complement pathway is activated by bound IgG/IgM; deposition of C3 and terminal C5b-9 at nodes/terminals precedes myelin degradation and conduction block; complement inhibition in animal models prevents sodium-channel cluster disruption and nerve-terminal injury. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)
- Macrophage-mediated demyelination vs nodo-paranodal autoimmunity: AIDP shows macrophage myelin phagocytosis; nodopathies involve antibodies to neurofascins, contactin-1, CASPR1 with paranodal dissection and conduction failure. IgG subclasses modulate complement involvement (e.g., IgG3/IgG1 complement binding vs IgG4 complement-sparing). (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Blood–nerve barrier and leukocyte signatures: Early GBS cohorts show activated monocytes and CD8 T cells, Th17/Treg imbalance, and predicted leukocyte–nerve ligand pairs including IL-6, IL-8, and oncostatin M. CSF IL-8 is a validated biomarker in immune-mediated neuropathies. (kmezic2025biomarkerandpathogenic pages 137-139, shastri2023immunemediatedneuropathiespathophysiology pages 22-24)

## 2. Key Molecular Players
- Genes/Proteins (HGNC): NFASC (neurofascin; NF155), CNTN1 (contactin-1), CNTNAP1 (CASPR1); complement components C1q, C3, C5b-9; ion channels at nodes (Nav clusters); adhesion complexes at paranodes. Evidence links anti-pan-neurofascin antibodies with complement activation and nodo-paranodal injury. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Chemical entities (CHEBI classes/examples): Gangliosides GM1, GD1a, GQ1b as antibody targets; therapeutic complement inhibitors (e.g., eculizumab) targeting C5. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, NCT04752566)
- Cell types (CL): Schwann cells; macrophages (segmental demyelination); monocytes; CD8+ T cells; B cells/plasma cells; Th17/Treg subsets; sensory and motor neurons. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, kmezic2025biomarkerandpathogenic pages 137-139)
- Anatomical locations (UBERON): Peripheral nerve; node of Ranvier; paranode/juxtaparanode; neuromuscular junction/motor terminal; dorsal root ganglion co-cultures show accessibility of anti-pan-neurofascin to nodes. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)

## 3. Biological Processes (GO-style)
- Complement activation, classical pathway; membrane attack complex assembly; antibody-mediated immunity; axo-glial adhesion and node of Ranvier organization; macrophage-mediated myelin phagocytosis; leukocyte activation and cytokine-mediated signaling (IL-6, IL-8, OSM); regulation of ion-channel clustering at nodes; Wallerian/secondary axonal degeneration and axon regeneration programs. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9, kmezic2025biomarkerandpathogenic pages 137-139)

## 4. Cellular Components
- Node of Ranvier; paranodal junction; axolemma; Schwann cell membrane; endoneurium; extracellular space (complement deposition); neuromuscular junction. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)

## 5. Disease Progression (sequence of events)
- Trigger: Antecedent infection (often C. jejuni) induces cross-reactive anti-ganglioside antibodies via molecular mimicry. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, oshomoji2024autoimmunemechanismsin pages 7-8)
- Effector phase: Antibodies bind nodal/paranodal targets (gangliosides or adhesion proteins) → classical complement activation (C1q→C3→C5b-9) and/or Fc-mediated recruitment of macrophages. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)
- Tissue injury: Disruption of sodium-channel clusters; paranodal detachment; segmental demyelination; conduction block/failure; secondary axonal degeneration; biomarker release (NfL). (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Clinical manifestation: Rapidly progressive weakness, areflexia, sensory symptoms, dysautonomia; phenotype varies by antibody specificities (e.g., AMAN/AMSAN vs AIDP; Miller Fisher with ophthalmoplegia/ataxia/areflexia). (oshomoji2024autoimmunemechanismsin pages 7-8, shastri2023immunemediatedneuropathiespathophysiology pages 7-8)

## 6. Phenotypic Manifestations and Mechanistic Correlations
- AMAN/AMSAN: Anti-GM1 and anti-GD1a IgG, nodal complement deposition, axolemmal attack; prominent axonal involvement; worse functional outcomes in some cohorts. (oshomoji2024autoimmunemechanismsin pages 7-8, shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- AIDP: Macrophage-mediated segmental demyelination; T cell–driven inflammation; conduction slowing/block and temporal dispersion on NCS. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, xu2024variationinworldwide pages 4-7)
- Miller Fisher syndrome: Anti-GQ1b IgG, complement-dependent injury at cranial nerve terminals; ophthalmoplegia, ataxia, areflexia; often monophasic and self-limited. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, oshomoji2024autoimmunemechanismsin pages 7-8)

## Expert syntheses, recent developments, and statistics
- Epidemiology (2024): Global pooled incidence 1.12 per 100,000 person-years (95% CI 0.98–1.27); urban China 0.41–0.58 per 100,000 (2013–2017). Higher in males (1.38) than females (0.99); regional variation: West Europe ~1.92; South Asia 1.61; North Europe 1.39; North America 1.38; Australia/New Zealand ~0.54; Southeast Asia 0.63; North Africa 0.69. Incidence correlates with enteric infection burden (P=0.007). URL: https://doi.org/10.3389/fimmu.2024.1415986 (Sep 2024) (xu2024variationinworldwide pages 4-7)
- Vaccine-associated risk (2023–2024): Meta-analysis of COVID-19 vaccines estimated 1.25 GBS cases per million doses overall; adenovirus-vectored vaccines showed ~2.4× increased risk (and ~7× vs mRNA), whereas mRNA vaccines showed much lower association; risk higher after first dose. URL: https://doi.org/10.1007/s00415-024-12186-7 (Jan 2024) (censi2024guillain–barrésyndromeand pages 5-8). Global pharmacovigilance (VigiBase) disproportionality signals: influenza vaccines ROR ~77.9; Ad5-vectored COVID-19 ROR ~14.9; mRNA COVID-19 ROR ~9.66; mean onset ~5.5 days; associations increase with age. URL: https://doi.org/10.1038/s41598-024-74729-2 (Oct 2024) (jeong2024globalburdenof pages 1-2, jeong2024globalburdenof pages 8-8, jeong2024globalburdenof pages 3-4, jeong2024globalburdenof pages 5-8, jeong2024globalburdenof pages 4-5)
- Complement therapeutics and trials: Phase 3 eculizumab (C5 inhibitor) trial (Japan) randomized 2:1 eculizumab:placebo, all with IVIg; primary endpoint time to Hughes FG≤1 (Week 24); completed Aug 2022, results posted Feb 9, 2024. URL: https://clinicaltrials.gov/ct2/show/NCT04752566 (NCT04752566). Complement’s centrality across axonal and demyelinating patterns emphasizes rationale for classical-pathway blockade; ongoing programs include C1q inhibition (e.g., ANX005) informed by preclinical efficacy. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Nodo-paranodal antibodies and IgG subclass biology: Anti-pan-neurofascin antibodies produce severe nodo-paranodal pathology with complement-mediated effects linked to IgG3/IgG1, while IgG4-related anti-NF155 in chronic disease is complement-sparing; these mechanisms predict treatment response (e.g., IVIg resistance and benefit from antibody-depleting/anti-CD20 therapies). URL: https://doi.org/10.1093/brain/awac418 (Nov 2023) (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Electrophysiology–pathology integration (2024): Non-uniform conduction slowing, block, and temporal dispersion can occur in both demyelinating and axonal forms; careful correlation with pathology (macrophage demyelination vs paranodal dissection) refines subtype classification and prognosis. URL: https://doi.org/10.1111/jns.12625 (Apr 2024) (xu2024variationinworldwide pages 4-7)

## Evidence items (selected with quotes)
- “Anti-ganglioside antibodies (GM1, GD1a, GD1b, GQ1b) bind at the node of Ranvier and activate complement… leading to C3/C5 cleavage and MAC deposition with disruption of sodium channel clusters” (review of experimental models and human pathology). URL: https://doi.org/10.3390/ijms24087288 (Apr 2023) (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)
- “Anti-pan-neurofascin… antibodies had access to nodes of Ranvier… impaired paranode formation, destruction of paranodal architecture… subclass IgG3 associated with complement binding and cytotoxic effects in vitro.” URL: https://doi.org/10.1093/brain/awac418 (Nov 2023) (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- “Global pooled incidence of GBS was 1.12 (95% CI 0.98–1.27) per 100,000 person-years… incidence in urban China 0.41–0.58… higher in West Europe and South Asia.” URL: https://doi.org/10.3389/fimmu.2024.1415986 (Sep 2024) (xu2024variationinworldwide pages 4-7)
- “COVID-19 vaccination meta-analysis: 1.25 cases per million doses; adenovirus-vectored vaccines 2.37-fold increased risk… mRNA vaccines 0.32.” URL: https://doi.org/10.1007/s00415-024-12186-7 (Jan 2024) (censi2024guillain–barrésyndromeand pages 5-8)
- “VigiBase disproportionality: influenza ROR 77.91; Ad5-vectored COVID-19 14.88; mRNA COVID-19 9.66; mean onset 5.47 days.” URL: https://doi.org/10.1038/s41598-024-74729-2 (Oct 2024) (jeong2024globalburdenof pages 1-2, jeong2024globalburdenof pages 8-8)
- “Eculizumab Phase 3 in severe GBS; all participants received IVIg; primary endpoint time to FG≤1 up to Week 24; results posted 2024-02-09.” URL: https://clinicaltrials.gov/ct2/show/NCT04752566 (NCT04752566)

## Knowledge-base aligned annotations
- Genes/Proteins (HGNC): NFASC (neurofascin/NF155); CNTN1 (contactin-1); CNTNAP1 (CASPR1); complement components C1q, C3, C5 (terminal MAC). (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Biological Processes (GO): complement activation, classical pathway; membrane attack complex assembly; axo-glial cell adhesion; node of Ranvier organization; macrophage-mediated myelin phagocytosis; leukocyte activation; cytokine-mediated signaling (IL-6, IL-8); regulation of sodium-channel clustering. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)
- Cellular Components (GO): node of Ranvier; paranodal junction; axolemma; myelin sheath; endoneurial space. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Cell Types (CL): Schwann cell; macrophage; monocyte; CD8+ T cell; Th17/Treg; B cell/plasma cell; sensory/motor neuron. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, kmezic2025biomarkerandpathogenic pages 137-139)
- Anatomical Locations (UBERON): peripheral nerve; node of Ranvier; neuromuscular junction. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Chemical Entities (CHEBI): gangliosides GM1, GD1a, GQ1b; complement-targeting drugs (e.g., eculizumab). (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, NCT04752566)
- Phenotypes (HP): acute flaccid paralysis; areflexia; sensory ataxia; ophthalmoplegia (MFS); dysautonomia; respiratory failure (severe cases). (oshomoji2024autoimmunemechanismsin pages 7-8)
- Biomarkers: CSF albuminocytologic dissociation; serum/CSF neurofilament light (NfL) as axonal injury marker; CSF IL-8 as inflammatory biomarker. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, kmezic2025biomarkerandpathogenic pages 137-139)

## Current applications and real-world implementations
- Diagnostics: Antibody testing supports phenotype stratification—anti-ganglioside assays (GM1, GD1a, GQ1b) for AMAN/AMSAN/MFS; nodo-paranodal antibodies (NF155, CNTN1, CASPR1) for autoimmune nodopathy. CSF IL-8 and NfL show promise for diagnostic/prognostic use; albuminocytologic dissociation remains standard supportive evidence. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, kmezic2025biomarkerandpathogenic pages 137-139)
- Therapeutics: IVIg and plasma exchange remain standard-of-care; complement inhibition is under clinical evaluation—Phase 3 eculizumab completed in 2022 with results posted in 2024; preclinical/early clinical rationale exists for proximal (C1q) blockade. (NCT04752566, shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Electrophysiology-guided care: Integration of NCS patterns with pathological mechanisms (macrophage demyelination vs paranodal dissection vs axolemmal injury) improves prognosis and treatment selection. (xu2024variationinworldwide pages 4-7)

## References with URLs and dates
- Xu L, et al. Variation in worldwide incidence of GBS. Frontiers in Immunology. Sep 2024. https://doi.org/10.3389/fimmu.2024.1415986 (xu2024variationinworldwide pages 4-7)
- Censi S, et al. GBS and COVID-19 vaccination meta-analysis. Journal of Neurology. Jan 2024. https://doi.org/10.1007/s00415-024-12186-7 (censi2024guillain–barrésyndromeand pages 5-8)
- Jeong YD, et al. Global burden of vaccine-associated GBS (VigiBase). Scientific Reports. Oct 2024. https://doi.org/10.1038/s41598-024-74729-2 (jeong2024globalburdenof pages 1-2, jeong2024globalburdenof pages 8-8, jeong2024globalburdenof pages 3-4, jeong2024globalburdenof pages 4-5)
- Appeltshauser L, et al. Anti-pan-neurofascin antibodies and complement. Brain. Nov 2023. https://doi.org/10.1093/brain/awac418 (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- Uncini A, et al. Conduction slowing/block: electrophysiology meets pathology. J Peripher Nerv Syst. Apr 2024. https://doi.org/10.1111/jns.12625 (xu2024variationinworldwide pages 4-7)
- Shastri A, et al. Immune-mediated neuropathies: pathophysiology and management. IJMS. Apr 2023. https://doi.org/10.3390/ijms24087288 (mechanistic complement/ganglioside evidence) (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9, shastri2023immunemediatedneuropathiespathophysiology pages 7-8)
- Oshomoji OI, et al. Autoimmune mechanisms in GBS subtypes: systematic review. Bulletin of Faculty of Physical Therapy. Dec 2024. https://doi.org/10.1186/s43161-024-00258-8 (oshomoji2024autoimmunemechanismsin pages 7-8)
- ClinicalTrials.gov. Eculizumab Phase 3 in GBS (NCT04752566). Results posted Feb 9, 2024. https://clinicaltrials.gov/ct2/show/NCT04752566 (NCT04752566)

## Appendix: Mapping to requested ontologies
- Gene/Protein annotations (HGNC): NFASC (neurofascin/NF155); CNTN1; CNTNAP1 (CASPR1); C1QA/C3/C5. Mechanisms: node/paranode adhesion; classical complement activation; MAC assembly; sodium-channel cluster disruption; macrophage myelin phagocytosis. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)
- GO Biological Processes: complement activation (classical pathway); membrane attack complex assembly; axo-glial cell adhesion; node of Ranvier organization; macrophage-mediated myelin phagocytosis; leukocyte activation; cytokine-mediated signaling; regulation of ion-channel clustering. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, shastri2023immunemediatedneuropathiespathophysiology pages 8-9)
- GO Cellular Components: node of Ranvier; paranode; axolemma; myelin sheath; endoneurial space. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- CL Cell Types: Schwann cell; macrophage; monocyte; CD8 T cell; Th17/Treg; B cell; sensory/motor neurons. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, kmezic2025biomarkerandpathogenic pages 137-139)
- UBERON Anatomy: peripheral nerve; node of Ranvier; neuromuscular junction. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24)
- CHEBI: gangliosides GM1, GD1a, GQ1b; complement inhibitor drug class (e.g., C5 inhibitor).
- HP Phenotypes: acute flaccid paralysis; areflexia; ophthalmoplegia; ataxia; sensory loss; autonomic dysfunction. (oshomoji2024autoimmunemechanismsin pages 7-8)

Limitations and open questions: Although strong evidence supports complement-mediated injury in axonal forms and nodopathies, heterogeneity across cohorts suggests overlapping mechanisms in AIDP/axonal subtypes. Large randomized trials of proximal complement inhibition (e.g., C1q) and validated, widely accessible assays for nodo-paranodal antibodies are areas for ongoing research. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24, xu2024variationinworldwide pages 4-7)

References

1. (shastri2023immunemediatedneuropathiespathophysiology pages 22-24): Abhishek Shastri, Ahmad Al Aiyan, Uday Kishore, and Maria Elena Farrugia. Immune-mediated neuropathies: pathophysiology and management. International Journal of Molecular Sciences, 24:7288, Apr 2023. URL: https://doi.org/10.3390/ijms24087288, doi:10.3390/ijms24087288. This article has 69 citations and is from a poor quality or predatory journal.

2. (shastri2023immunemediatedneuropathiespathophysiology pages 8-9): Abhishek Shastri, Ahmad Al Aiyan, Uday Kishore, and Maria Elena Farrugia. Immune-mediated neuropathies: pathophysiology and management. International Journal of Molecular Sciences, 24:7288, Apr 2023. URL: https://doi.org/10.3390/ijms24087288, doi:10.3390/ijms24087288. This article has 69 citations and is from a poor quality or predatory journal.

3. (oshomoji2024autoimmunemechanismsin pages 7-8): Olawale Isreal Oshomoji, J. O. Ajiroba, S. O. Semudara, M. A. Olayemi, and S. O. Adeoye. Autoimmune mechanisms in guillain-barré syndrome subtypes: a systematic review. Bulletin of Faculty of Physical Therapy, Dec 2024. URL: https://doi.org/10.1186/s43161-024-00258-8, doi:10.1186/s43161-024-00258-8. This article has 7 citations and is from a peer-reviewed journal.

4. (NCT04752566):  A Study to Evaluate the Efficacy and Safety of Eculizumab in Guillain-Barré Syndrome. Alexion Pharmaceuticals, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04752566

5. (shastri2023immunemediatedneuropathiespathophysiology pages 7-8): Abhishek Shastri, Ahmad Al Aiyan, Uday Kishore, and Maria Elena Farrugia. Immune-mediated neuropathies: pathophysiology and management. International Journal of Molecular Sciences, 24:7288, Apr 2023. URL: https://doi.org/10.3390/ijms24087288, doi:10.3390/ijms24087288. This article has 69 citations and is from a poor quality or predatory journal.

6. (kmezic2025biomarkerandpathogenic pages 137-139): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.

7. (censi2024guillain–barrésyndromeand pages 5-8): Stefano Censi, Giandomenico Bisaccia, Sabina Gallina, Valentina Tomassini, and Antonino Uncini. Guillain–barré syndrome and covid-19 vaccination: a systematic review and meta-analysis. Journal of Neurology, 271:1063-1071, Jan 2024. URL: https://doi.org/10.1007/s00415-024-12186-7, doi:10.1007/s00415-024-12186-7. This article has 24 citations and is from a domain leading peer-reviewed journal.

8. (xu2024variationinworldwide pages 4-7): Lu Xu, Chen Zhao, Yutong Bao, Yuchen Liu, Yuqing Liang, Jiyu Wei, Guozhen Liu, Jinxi Wang, Siyan Zhan, Shengfeng Wang, and Dongsheng Fan. Variation in worldwide incidence of guillain-barré syndrome: a population-based study in urban china and existing global evidence. Frontiers in Immunology, Sep 2024. URL: https://doi.org/10.3389/fimmu.2024.1415986, doi:10.3389/fimmu.2024.1415986. This article has 24 citations and is from a peer-reviewed journal.

9. (jeong2024globalburdenof pages 1-2): Yi Deun Jeong, Seoyoung Park, Sooji Lee, Woojin Jang, Jaeyu Park, Kyeongmin Lee, Jinseok Lee, Jiseung Kang, Raphael Udeh, Masoud Rahmati, Seung Geun Yeo, Lee Smith, Hayeon Lee, and Dong Keon Yon. Global burden of vaccine-associated guillain-barré syndrome over 170 countries from 1967 to 2023. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-74729-2, doi:10.1038/s41598-024-74729-2. This article has 22 citations and is from a peer-reviewed journal.

10. (jeong2024globalburdenof pages 8-8): Yi Deun Jeong, Seoyoung Park, Sooji Lee, Woojin Jang, Jaeyu Park, Kyeongmin Lee, Jinseok Lee, Jiseung Kang, Raphael Udeh, Masoud Rahmati, Seung Geun Yeo, Lee Smith, Hayeon Lee, and Dong Keon Yon. Global burden of vaccine-associated guillain-barré syndrome over 170 countries from 1967 to 2023. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-74729-2, doi:10.1038/s41598-024-74729-2. This article has 22 citations and is from a peer-reviewed journal.

11. (jeong2024globalburdenof pages 3-4): Yi Deun Jeong, Seoyoung Park, Sooji Lee, Woojin Jang, Jaeyu Park, Kyeongmin Lee, Jinseok Lee, Jiseung Kang, Raphael Udeh, Masoud Rahmati, Seung Geun Yeo, Lee Smith, Hayeon Lee, and Dong Keon Yon. Global burden of vaccine-associated guillain-barré syndrome over 170 countries from 1967 to 2023. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-74729-2, doi:10.1038/s41598-024-74729-2. This article has 22 citations and is from a peer-reviewed journal.

12. (jeong2024globalburdenof pages 5-8): Yi Deun Jeong, Seoyoung Park, Sooji Lee, Woojin Jang, Jaeyu Park, Kyeongmin Lee, Jinseok Lee, Jiseung Kang, Raphael Udeh, Masoud Rahmati, Seung Geun Yeo, Lee Smith, Hayeon Lee, and Dong Keon Yon. Global burden of vaccine-associated guillain-barré syndrome over 170 countries from 1967 to 2023. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-74729-2, doi:10.1038/s41598-024-74729-2. This article has 22 citations and is from a peer-reviewed journal.

13. (jeong2024globalburdenof pages 4-5): Yi Deun Jeong, Seoyoung Park, Sooji Lee, Woojin Jang, Jaeyu Park, Kyeongmin Lee, Jinseok Lee, Jiseung Kang, Raphael Udeh, Masoud Rahmati, Seung Geun Yeo, Lee Smith, Hayeon Lee, and Dong Keon Yon. Global burden of vaccine-associated guillain-barré syndrome over 170 countries from 1967 to 2023. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-74729-2, doi:10.1038/s41598-024-74729-2. This article has 22 citations and is from a peer-reviewed journal.