---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:51.215484'
end_time: '2025-12-18T09:54:28.294218'
duration_seconds: 517.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Inflammatory Demyelinating Polyneuropathy
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Chronic Inflammatory Demyelinating Polyneuropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Inflammatory Demyelinating Polyneuropathy**.
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
- **Disease Name:** Chronic Inflammatory Demyelinating Polyneuropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Inflammatory Demyelinating Polyneuropathy**.
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
- Disease Name: Chronic Inflammatory Demyelinating Polyneuropathy (CIDP)
- MONDO ID: not definitively assigned for the entire CIDP spectrum in sources cited here
- Category: Autoimmune

## Pathophysiology Description (current understanding)
CIDP is an immune-mediated disorder of peripheral nerves characterized by heterogeneous, overlapping mechanisms that variably involve cellular immunity (T cells, macrophages), humoral autoimmunity (B cells, autoantibodies), complement activation, and disruption of the blood–nerve barrier (BNB). Pathology classically shows macrophage-mediated segmental demyelination, with inflammatory infiltrates of T cells and macrophages within endoneurium; humoral mechanisms are supported by immunoglobulin deposition and, in defined subgroups, pathogenic autoantibodies against nodal/paranodal proteins that disrupt axo–glial junctions without prominent inflammation. Complement activation (including terminal C5b-9 deposition) appears to promote demyelination and correlates with inflammatory cell infiltration and severity in biopsy cohorts. Therapeutic responsiveness to IVIg, corticosteroids, and plasma exchange underscores antibody and immune effector contributions, while newer strategies—FcRn blockade and complement inhibition—further link specific pathways to disease activity. Overall, CIDP encompasses at least two mechanistic archetypes: (1) macrophage/complement-driven segmental demyelination; and (2) nodal/paranodal autoantibody-mediated “autoimmune nodopathies,” now defined as distinct from classical CIDP, with unique treatment implications. (vallat2024pathologyexplainsvarious pages 8-8, caballeroavila2025apathophysiologicaland pages 1-2, caballeroavila2025apathophysiologicaland pages 5-6, caballeroavila2025apathophysiologicaland pages 2-3)

| Mechanism/Process | Key molecules (HGNC) | Cell types (CL) | Cellular components (GO-CC) | Biological processes (GO-BP) | Evidence & year (PMID/DOI, URL) |
|---|---|---|---|---|---|
| Macrophage-mediated segmental demyelination | Fc gamma receptors (FCGRs, e.g., FCGR3A); myelin proteins (e.g., MPZ, PMP22) | Macrophage (CL: macrophage), Schwann cell (CL: Schwann cell) | Myelin sheath (GO:0043209); endoneurium | Macrophage-mediated phagocytosis of myelin; segmental demyelination | (vallat2024pathologyexplainsvarious pages 8-8) Vallat & Mathis 2024; DOI: 10.1111/bpa.13184; https://doi.org/10.1111/bpa.13184 |
| T- and B-cell involvement (adaptive immunity) | CD4 (CD4), CD8A (CD8A), CD20 (MS4A1), BAFF (TNFSF13B) | CD4+ T cell, CD8+ T cell, B cell / plasma cell | Immune synapse / lymphocyte plasma membrane (GO-CC) | Antigen processing and presentation; T-cell cytotoxicity; B-cell antibody production | (kmezic2025biomarkerandpathogenic pages 150-152, kmezic2025biomarkerandpathogenic pages 178-181) Kmezic 2025; DOI: 10.69622/28457924.v1; https://doi.org/10.69622/28457924.v1 |
| Nodal/paranodal autoantibodies (autoimmune nodopathy) | NFASC (isoforms NF155, NF186/140), CNTN1, CNTNAP1 (CASPR1) | Schwann cell (paranodal glia), axonal paranode | Node of Ranvier (GO:0033268); paranodal junction (GO-CC) | Disruption of node/paranode assembly, loss of ion-channel clustering, conduction block | (vallat2024pathologyexplainsvarious pages 8-8, appeltshauser2024casereporttarget pages 8-8) Vallat 2024; Appeltshauser 2024 (case report) DOI: 10.1111/bpa.13184, 10.3389/fimmu.2024.1475478 |
| Complement activation (terminal pathway / MAC) | Complement components C3, C5, membrane attack complex (C5b-9) | Macrophages, endoneurial endothelial cells, Schwann cells | Membrane attack complex (GO:0030442); endoneurial capillary | Complement activation, opsonization, MAC-mediated membrane injury and promotion of demyelination | (caballeroavila2025apathophysiologicaland pages 5-6, vallat2024pathologyexplainsvarious pages 8-8) Caballero-Ávila 2025 DOI: 10.3389/fimmu.2025.1575464; Vallat 2024 DOI: 10.1111/bpa.13184 |
| Blood–nerve barrier (BNB) disruption / increased permeability | Tight junction proteins (e.g., CLDN5), chemokines (e.g., CCLs) | Peripheral nerve microvascular endothelial cell (CL), pericyte | Blood–nerve barrier / tight junction (GO-CC) | Increased vascular permeability, leukocyte extravasation into endoneurium | (kmezic2025biomarkerandpathogenic pages 178-181, kmezic2025biomarkerandpathogenic pages 29-35) Kmezic 2025 DOI: 10.69622/28457924.v1; (supporting BNB findings in related studies) |
| Fluid/serologic biomarkers (diagnostic/prognostic) | NEFL (NfL), IL8 (IL-8), PTGDS (beta-trace protein) | Neurons/axons (NEFL), immune cells (IL8), CSF-producing cells (PTGDS) | Neuronal cytoskeleton (GO:0043227); extracellular region/CSF (GO:0005576) | Axonal injury release (NfL); chemokine signaling (IL-8); CSF protein changes reflecting barrier dysfunction (beta-trace) | (kmezic2025biomarkerandpathogenic pages 150-152, kmezic2025biomarkerandpathogenic pages 178-181) Kmezic 2025 DOI: 10.69622/28457924.v1 (NfL, IL-8, beta-trace validated in cohorts) |
| Therapeutic mechanisms (mechanism-linked interventions) | IVIg (polyclonal IgG), FCGRT (FcRn target for efgartigimod), MS4A1 (CD20; rituximab), C5 / C1s (eculizumab / anti-complement agents) | B cells / plasma cells (targeted by rituximab), FcR-expressing macrophages, endothelial cells | Extracellular region; endosomal FcRn recycling compartment (GO-CC) | IgG neutralization and Fc modulation (IVIg); immunosuppression (corticosteroids); antibody removal (PLEX); B-cell depletion (rituximab); IgG lowering via FcRn blockade (efgartigimod); complement blockade (anti-C5/anti-C1s) | (caballeroavila2025apathophysiologicaland pages 5-6, kmezic2025biomarkerandpathogenic pages 178-181, appeltshauser2024casereporttarget pages 8-8) Caballero-Ávila 2025 DOI: 10.3389/fimmu.2025.1575464; Kmezic 2025 DOI: 10.69622/28457924.v1; Appeltshauser 2024 DOI: 10.3389/fimmu.2024.1475478 |


*Table: Compact summary linking major CIDP mechanisms to molecules, cell types, cellular locations (GO-CC), processes (GO-BP) and recent evidence (context IDs, DOIs/URLs). Useful for ontology annotation and knowledge-base entry drafting.*

## 1. Core Pathophysiology
- Primary mechanisms
  - Macrophage-mediated demyelination: Endoneurial macrophages strip compact myelin, producing segmental demyelination and onion-bulb change; this is the signature lesion on nerve biopsy in many CIDP patients. (vallat2024pathologyexplainsvarious pages 8-8)
  - Adaptive immunity: CD4+ and CD8+ T cells infiltrate peripheral nerves; cytokine milieu suggests Th1/Th17 polarization; Schwann cells may upregulate antigen presentation molecules, sustaining local inflammation. (caballeroavila2025apathophysiologicaland pages 1-2, kmezic2025biomarkerandpathogenic pages 44-47)
  - Humoral autoimmunity at nodes/paranodes: Autoantibodies to neurofascin isoforms (NF155; nodal NF186/140), contactin-1 (CNTN1) and CASPR1 define autoimmune nodopathies, with disruption of paranodal septate junctions and conduction failure, often with poor response to IVIg but responsiveness to B cell–directed therapy. (vallat2024pathologyexplainsvarious pages 8-8)
  - Complement activation: Evidence includes deposition of terminal complement complex (C5b-9) on endoneurial microvessels and myelin, with proposed roles in opsonization and macrophage recruitment; motivates evaluation of complement inhibitors. (caballeroavila2025apathophysiologicaland pages 5-6, vallat2024pathologyexplainsvarious pages 8-8)
  - BNB disruption: Increased permeability allows immune cell ingress and antibody access to axo–glial targets, facilitating chronic inflammation. (kmezic2025biomarkerandpathogenic pages 29-35)
- Dysregulated molecular pathways
  - Complement cascades (classical/alternative) converging on C3/C5 and MAC; IgG effector pathways engaging Fcγ receptors on phagocytes; FcRn-mediated IgG recycling as a regulator of IgG pool; cytokine/chemokine networks (e.g., IL-8) reflecting intrathecal inflammation. (caballeroavila2025apathophysiologicaland pages 5-6, kmezic2025biomarkerandpathogenic pages 178-181)
- Affected cellular processes
  - Myelin phagocytosis, antigen presentation, lymphocyte activation, axo–glial junction assembly, and conduction at the node of Ranvier; secondary axonal degeneration with chronicity (elevated NfL). (vallat2024pathologyexplainsvarious pages 8-8, kmezic2025biomarkerandpathogenic pages 178-181)

## 2. Key Molecular Players
- Genes/Proteins (HGNC)
  - NFASC (Neurofascin isoforms NF155 [Schwann cell], NF186/140 [axonal]): paranodal/nodal adhesion; autoantibody targets in autoimmune nodopathy. (vallat2024pathologyexplainsvarious pages 8-8)
  - CNTN1 (Contactin-1), CNTNAP1 (CASPR1): paranodal axoglial complex; autoantibody targets. (vallat2024pathologyexplainsvarious pages 8-8)
  - Complement components C3, C5; terminal complement complex C5b-9 (MAC): effector injury mechanisms and vascular deposition. (caballeroavila2025apathophysiologicaland pages 5-6)
  - FCGRT (FcRn): regulates IgG recycling and serum half-life; therapeutic target for IgG lowering. (caballeroavila2025apathophysiologicaland pages 5-6)
  - NEFL (Neurofilament light chain): axonal injury biomarker in CSF/plasma. (kmezic2025biomarkerandpathogenic pages 178-181)
  - IL8 (CXCL8): chemokine elevated in CIDP CSF; diagnostic/prognostic value. (kmezic2025biomarkerandpathogenic pages 178-181)
  - PTGDS (beta-trace protein): elevated in CIDP CSF; may outperform albumin quotient in some analyses. (kmezic2025biomarkerandpathogenic pages 150-152)
- Chemical entities (CHEBI/drugs)
  - IVIg (polyclonal IgG), corticosteroids (glucocorticoids), plasma exchange (PLEX), rituximab (anti-CD20), efgartigimod (FcRn blocker), complement inhibitors (e.g., anti-C5, anti-C1s such as riliprubart). (caballeroavila2025apathophysiologicaland pages 5-6, appeltshauser2024casereporttarget pages 8-8)
- Cell types (CL)
  - Macrophages (endoneurial), CD4+ T cells, CD8+ T cells, B cells/plasma cells, Schwann cells, endoneurial endothelial cells. (vallat2024pathologyexplainsvarious pages 8-8, kmezic2025biomarkerandpathogenic pages 44-47)
- Anatomical locations (UBERON)
  - Peripheral nerve and nerve roots, sural nerve, node of Ranvier, paranode, blood–nerve barrier (endoneurial microvasculature). (vallat2024pathologyexplainsvarious pages 8-8, caballeroavila2025apathophysiologicaland pages 5-6)

## 3. Biological Processes (GO terms)
- Immune effector processes: complement activation (classical/alternative), Fc receptor signaling, leukocyte extravasation, cytokine-mediated signaling (e.g., IL-8). (caballeroavila2025apathophysiologicaland pages 5-6, kmezic2025biomarkerandpathogenic pages 178-181)
- Myelin and conduction: axo–glial junction assembly, paranodal organization, myelin sheath maintenance, action potential propagation at nodes. (vallat2024pathologyexplainsvarious pages 8-8)
- Phagocytosis and demyelination: macrophage-mediated myelin phagocytosis, segmental demyelination, antigen processing and presentation. (vallat2024pathologyexplainsvarious pages 8-8, kmezic2025biomarkerandpathogenic pages 44-47)
- Axonal injury responses: cytoskeletal damage with neurofilament release. (kmezic2025biomarkerandpathogenic pages 178-181)

## 4. Cellular Components (GO-CC)
- Node of Ranvier; paranodal junction; myelin sheath; endoneurial capillaries and BNB; membrane attack complex; endosomal FcRn recycling compartment. (vallat2024pathologyexplainsvarious pages 8-8, caballeroavila2025apathophysiologicaland pages 5-6)

## 5. Disease Progression
- Proposed sequence
  1) Predisposition/triggers (e.g., HLA background, metabolic/infectious modifiers) → 2) BNB dysfunction with permeability changes → 3) Entry of autoreactive T cells, macrophages, and antibodies into endoneurium → 4a) Classical CIDP: opsonization and macrophage-mediated segmental demyelination with complement participation; 4b) Autoimmune nodopathy: IgG (frequently IgG4) against nodal/paranodal targets causing paranodal dissection and conduction failure with minimal inflammation → 5) Secondary axonal loss and chronic disability. (kmezic2025biomarkerandpathogenic pages 29-35, vallat2024pathologyexplainsvarious pages 8-8)
- Stages/phases
  - Relapsing-remitting and progressive courses occur; early treatment prevents irreversible axonal degeneration. (caballeroavila2025apathophysiologicaland pages 1-2)

## 6. Phenotypic Manifestations (HP)
- Symmetric proximal and distal weakness, sensory loss with sensory ataxia, tremor, areflexia; CSF cytoalbuminologic dissociation (elevated protein); variable conduction block and demyelinating features on NCS; nodopathy often shows tremor, sensory ataxia, younger onset, poor IVIg response, better rituximab response. (caballeroavila2025apathophysiologicaland pages 1-2, vallat2024pathologyexplainsvarious pages 8-8)

## Current Applications and Real-World Implementations
- Diagnostics and biomarkers
  - Testing for nodal/paranodal antibodies (NF155, NF186/140, CNTN1, CASPR1) is now integrated into clinical workflows for suspected nodopathies, directing therapy choices. (vallat2024pathologyexplainsvarious pages 8-8)
  - Fluid biomarkers: CSF/plasma NfL correlates with axonal injury; CSF IL-8 shows diagnostic/prognostic value; CSF beta-trace protein elevation may aid diagnosis independent of albumin quotient. (kmezic2025biomarkerandpathogenic pages 178-181, kmezic2025biomarkerandpathogenic pages 150-152)
- Therapeutics (mechanism-linked)
  - IVIg, corticosteroids, and PLEX remain first-line, consistent with antibody/immune effector mechanisms. (caballeroavila2025apathophysiologicaland pages 2-3)
  - Rituximab shows benefit in IgG4-seropositive nodopathy subsets (B-cell mediation). (appeltshauser2024casereporttarget pages 8-8)
  - FcRn blockade: efgartigimod lowers total IgG and reduces relapse risk; represents a targeted strategy against circulating pathogenic IgG. (caballeroavila2025apathophysiologicaland pages 5-6)
  - Complement pathway inhibition: early studies with anti-complement agents (e.g., riliprubart; anti-C5) reflect the role of complement in macrophage-mediated demyelination; mixed results emphasize need for biomarker-guided selection. (caballeroavila2025apathophysiologicaland pages 5-6)

## Expert Opinions and Analysis
- Contemporary reviews emphasize that CIDP is a clinicopathologic umbrella with mechanistic heterogeneity; understanding whether a given patient has macrophage/complement-driven demyelination versus nodal/paranodal antibody-mediated disruption is critical for precision therapy and explains differential responses to IVIg versus rituximab or FcRn/complement modulators. (caballeroavila2025apathophysiologicaland pages 1-2, caballeroavila2025apathophysiologicaland pages 2-3)
- Pathology continues to be pivotal: the presence of macrophage clusters and segmental demyelination versus paranodal dissection without inflammation helps stratify mechanisms and likely therapeutic responses. (vallat2024pathologyexplainsvarious pages 8-8)

## Relevant Statistics and Data (recent)
- FcRn blockade: Phase-stage data summarized in 2025 review reported longer relapse-free proportions with efgartigimod vs comparator (e.g., 73.1% vs 46.4% at a key timepoint in Stage B of a large trial), supporting IgG-lowering efficacy in CIDP. (caballeroavila2025apathophysiologicaland pages 5-6)
- Complement: Biopsy-based analyses report prominent C5b-9 deposition on endoneurial capillaries in most patients, correlating with inflammatory cell infiltration and clinical severity, supporting a complement-mediated component in a substantial subset. (caballeroavila2025apathophysiologicaland pages 5-6)
- Biomarkers: CSF/plasma NfL elevated across immune-mediated neuropathies and associates with prognosis; CSF IL-8 validated as diagnostic/prognostic; beta-trace protein elevated in CIDP independent of albumin quotient. (kmezic2025biomarkerandpathogenic pages 178-181, kmezic2025biomarkerandpathogenic pages 150-152)

## Evidence Items with Citations (PMIDs/DOIs and URLs)
- Pathology of macrophage-mediated demyelination and nodal/paranodal autoimmunity; conceptualization of nodopathies distinct from classical CIDP: Vallat & Mathis, Brain Pathology (2024), DOI: 10.1111/bpa.13184, https://doi.org/10.1111/bpa.13184. (vallat2024pathologyexplainsvarious pages 8-8)
- Mechanistic and therapeutic review linking complement, FcRn, and immune pathways; FcRn blockade approval and trial outcomes; complement inhibitor development: Caballero-Ávila et al., Frontiers in Immunology (2025), DOI: 10.3389/fimmu.2025.1575464, https://doi.org/10.3389/fimmu.2025.1575464. (caballeroavila2025apathophysiologicaland pages 1-2, caballeroavila2025apathophysiologicaland pages 5-6, caballeroavila2025apathophysiologicaland pages 2-3)
- Biomarkers in CIDP and immune neuropathies: elevated plasma/CSF NfL, IL‑8 in CSF as diagnostic/prognostic, and beta-trace protein in CIDP CSF; translational BNB insights: Kmezic (Thesis, 2025), DOI: 10.69622/28457924.v1, https://doi.org/10.69622/28457924.v1. (kmezic2025biomarkerandpathogenic pages 150-152, kmezic2025biomarkerandpathogenic pages 178-181, kmezic2025biomarkerandpathogenic pages 29-35)
- Autoimmune nodopathy case with antigen/subclass switch; rituximab responsiveness; NfL tracking: Appeltshauser et al., Frontiers in Immunology (2024), DOI: 10.3389/fimmu.2024.1475478, https://doi.org/10.3389/fimmu.2024.1475478. (appeltshauser2024casereporttarget pages 8-8)

## Ontology Annotations (examples)
- Genes/Proteins (HGNC): NFASC; CNTN1; CNTNAP1; C3; C5; FCGRT; NEFL; IL8; PTGDS. (caballeroavila2025apathophysiologicaland pages 5-6, vallat2024pathologyexplainsvarious pages 8-8, kmezic2025biomarkerandpathogenic pages 178-181, kmezic2025biomarkerandpathogenic pages 150-152)
- Biological Processes (GO-BP): complement activation; macrophage-mediated phagocytosis; antigen processing and presentation; axo–glial junction assembly; chemokine-mediated signaling pathway; regulation of IgG catabolic process (FcRn). (caballeroavila2025apathophysiologicaland pages 5-6, vallat2024pathologyexplainsvarious pages 8-8, kmezic2025biomarkerandpathogenic pages 178-181)
- Cellular Components (GO-CC): node of Ranvier; paranodal junction; myelin sheath; endoneurial capillary; membrane attack complex; endosomal recycling compartment (FcRn). (vallat2024pathologyexplainsvarious pages 8-8, caballeroavila2025apathophysiologicaland pages 5-6)
- Cell Types (CL): macrophage; CD4+ T cell; CD8+ T cell; B cell; Schwann cell; endothelial cell. (vallat2024pathologyexplainsvarious pages 8-8, kmezic2025biomarkerandpathogenic pages 44-47)
- Anatomy (UBERON): peripheral nerve; sural nerve; blood–nerve barrier; node of Ranvier; paranode. (vallat2024pathologyexplainsvarious pages 8-8, caballeroavila2025apathophysiologicaland pages 5-6)
- Chemicals (CHEBI): IVIg; glucocorticoids; rituximab; efgartigimod; eculizumab; riliprubart. (caballeroavila2025apathophysiologicaland pages 5-6, appeltshauser2024casereporttarget pages 8-8)

## Direct quotes (selected)
- “It has been shown that immunoglobulin G from the serum of about 30% of CIDP patients immunolabels nodes of Ranvier or paranodes of myelinated axons… In these cases, paranodal dissection develops in the absence of macrophage‑induced demyelination.” (Vallat & Mathis 2024) (vallat2024pathologyexplainsvarious pages 8-8)
- “The complement pathway plays a key role in promoting macrophage‑mediated demyelination… The neonatal Fc receptor (FcRn) has also been targeted… Efgartigimod is the first FcRn blocker approved for the treatment of CIDP.” (Caballero‑Ávila et al. 2025) (caballeroavila2025apathophysiologicaland pages 5-6)
- “IL‑8 in CSF is validated as a diagnostic biomarker for GBS and CIDP… beta‑trace protein… may serve as a more informative diagnostic biomarker than albumin [in CIDP].” (Kmezic 2025) (kmezic2025biomarkerandpathogenic pages 178-181, kmezic2025biomarkerandpathogenic pages 150-152)
- “Plasma exchange and rituximab treatment led to a serological remission and corresponding significant clinical improvement” in anti‑paranodal autoimmune nodopathy. (Appeltshauser et al. 2024) (appeltshauser2024casereporttarget pages 8-8)

Limitations and open questions: Several mechanistic details remain unresolved in seronegative CIDP; the extent and clinical utility of complement profiling and antibody discovery beyond established nodal/paranodal targets require larger studies; biomarker cutoffs and implementation pathways continue to evolve.


References

1. (vallat2024pathologyexplainsvarious pages 8-8): Jean‐Michel Vallat and Stéphane Mathis. Pathology explains various mechanisms of auto‐immune inflammatory peripheral neuropathies. Brain Pathology, Jun 2024. URL: https://doi.org/10.1111/bpa.13184, doi:10.1111/bpa.13184. This article has 22 citations and is from a domain leading peer-reviewed journal.

2. (caballeroavila2025apathophysiologicaland pages 1-2): Marta Caballero-Ávila, Lorena Martin-Aguilar, Roger Collet-Vidiella, Luis Querol, and Elba Pascual-Goñi. A pathophysiological and mechanistic review of chronic inflammatory demyelinating polyradiculoneuropathy therapy. Frontiers in Immunology, Apr 2025. URL: https://doi.org/10.3389/fimmu.2025.1575464, doi:10.3389/fimmu.2025.1575464. This article has 6 citations and is from a peer-reviewed journal.

3. (caballeroavila2025apathophysiologicaland pages 5-6): Marta Caballero-Ávila, Lorena Martin-Aguilar, Roger Collet-Vidiella, Luis Querol, and Elba Pascual-Goñi. A pathophysiological and mechanistic review of chronic inflammatory demyelinating polyradiculoneuropathy therapy. Frontiers in Immunology, Apr 2025. URL: https://doi.org/10.3389/fimmu.2025.1575464, doi:10.3389/fimmu.2025.1575464. This article has 6 citations and is from a peer-reviewed journal.

4. (caballeroavila2025apathophysiologicaland pages 2-3): Marta Caballero-Ávila, Lorena Martin-Aguilar, Roger Collet-Vidiella, Luis Querol, and Elba Pascual-Goñi. A pathophysiological and mechanistic review of chronic inflammatory demyelinating polyradiculoneuropathy therapy. Frontiers in Immunology, Apr 2025. URL: https://doi.org/10.3389/fimmu.2025.1575464, doi:10.3389/fimmu.2025.1575464. This article has 6 citations and is from a peer-reviewed journal.

5. (kmezic2025biomarkerandpathogenic pages 150-152): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.

6. (kmezic2025biomarkerandpathogenic pages 178-181): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.

7. (appeltshauser2024casereporttarget pages 8-8): Luise Appeltshauser, Helena Glenewinkel, Sophia Rohrbacher, Lena Wessely, Carmen Villmann, Claudia Sommer, and Kathrin Doppler. Case report: target antigen and subclass switch in a patient with autoimmune nodopathy. Frontiers in Immunology, Oct 2024. URL: https://doi.org/10.3389/fimmu.2024.1475478, doi:10.3389/fimmu.2024.1475478. This article has 4 citations and is from a peer-reviewed journal.

8. (kmezic2025biomarkerandpathogenic pages 29-35): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.

9. (kmezic2025biomarkerandpathogenic pages 44-47): Ivan Kmezic. Biomarker and pathogenic study of immune-mediated neuropathies. Apr 2025. URL: https://doi.org/10.69622/28457924.v1, doi:10.69622/28457924.v1.