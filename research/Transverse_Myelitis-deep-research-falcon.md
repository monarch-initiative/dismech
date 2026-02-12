---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-01-31T14:27:54.410545'
end_time: '2026-01-31T14:27:54.412721'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Transverse Myelitis
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Transverse Myelitis
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Transverse Myelitis**.
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
- **Disease Name:** Transverse Myelitis
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Transverse Myelitis**.
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
- We identified recent literature (2024 prospective cohort and observational studies; 2024 systematic review) and an interventional trial relevant to inflammatory myelitis, and included a foundational NEJM review for core mechanisms (completed). We synthesized mechanistic and clinical distinctions among idiopathic TM, NMOSD, and MOGAD. We mapped key entities to ontology terms and created an artifact for rapid reference. We summarized disease progression, phenotypes, and outcomes with quantitative data where available. We included current applications and trials and cited all major claims with URLs and dates.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Transverse Myelitis (TM)
- Category: Neurological Disorder

Pathophysiology description
Transverse myelitis is an acute or subacute immune-mediated inflammatory syndrome of the spinal cord characterized by motor, sensory, and autonomic dysfunction, often following infection or vaccination, with 15–30% of cases remaining idiopathic. Histopathology shows focal perivascular collections of lymphocytes and monocytes, with variable demyelination, axonal injury, and activation of astroglia and microglia. In neuromyelitis optica spectrum disorder (NMOSD), lesions exhibit perivascular immunoglobulin and complement deposition and, in severe cases, necrosis, supporting antibody- and complement-mediated astrocytopathy as a core mechanism. MRI evidence of cord inflammation typically includes gadolinium enhancement of intramedullary lesions; CSF may show pleocytosis and/or elevated IgG index. Symptoms evolve over hours to days and reach nadir within ~4 hours to 21 days; most recovery occurs within 3 months but may continue up to one year (NEJM review; Aug 2010; https://doi.org/10.1056/NEJMcp1001112) (frohman2010transversemyelitis pages 1-2, frohman2010transversemyelitis pages 2-4).

Core Pathophysiology
- Primary mechanisms: immune-mediated inflammation of the spinal cord, with adaptive humoral immunity central in NMOSD (AQP4-IgG binding to astrocytic AQP4, complement activation, perivascular deposition; necrotic LETM). In MOGAD, demyelinating pathology linked to anti-MOG antibodies; many cases are para-infectious. Idiopathic TM involves focal inflammatory demyelination with glial activation and axonal injury (NEJM; 2010; https://doi.org/10.1056/NEJMcp1001112). Distinct clinical sequelae such as spinal movement disorders are more prevalent in AQP4-IgG–positive NMOSD, aligning with greater tract involvement in extensive lesions (J Neurol; Jul 2024; https://doi.org/10.1007/s00415-024-12527-6) (frohman2010transversemyelitis pages 1-2, abboud2024spinalmovementdisorders pages 1-2, abboud2024spinalmovementdisorders pages 5-7).
- Molecular pathways: antibody binding to AQP4 on astrocytic endfeet leading to classical complement cascade activation and astrocyte injury; secondary demyelination and axonal loss. Para-/post-infectious mechanisms include molecular mimicry and cross-reactivity between pathogen- or vaccine-derived antigens and myelin proteins (e.g., MBP, MOG). Proposed mechanisms in vaccine/infection-associated TM include mimicry and immune dysregulation (Ann Med & Surgery; Jul 2022; https://doi.org/10.1016/j.amsu.2022.103870) (frohman2010transversemyelitis pages 1-2, naeem2022theassociationbetween pages 3-4, naeem2022theassociationbetween pages 2-3).
- Cellular processes: astrocyte injury (NMOSD) with downstream BBB disruption; oligodendrocyte/myelin injury (demyelination) prominent in idiopathic TM and MOGAD; microglial activation and myelin phagocytosis; axonal injury correlating with long-term disability (NEJM 2010; https://doi.org/10.1056/NEJMcp1001112; Arquivos de Neuro-Psiquiatria; Aug 2024; https://doi.org/10.1055/s-0044-1789342) (frohman2010transversemyelitis pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11).

Key Molecular Players
- Genes/Proteins (HGNC):
  - AQP4 (HGNC:633): target of AQP4-IgG in NMOSD; mediates complement-dependent cytotoxicity on astrocytes (NEJM 2010; https://doi.org/10.1056/NEJMcp1001112) (frohman2010transversemyelitis pages 1-2).
  - MOG (HGNC:7106): anti-MOG antibodies associated with inflammatory demyelination (MOGAD), including post-/para-infectious myelitis; Zika-associated cases with anti-MOG reported (Rev Inst Med Trop São Paulo; Dec 2024; https://doi.org/10.1590/S1678-9946202466066) (colognese2024zikavirusinfection pages 8-10, colognese2024zikavirusinfection pages 5-6).
- Antibodies: AQP4-IgG; MOG-IgG; anti-ganglioside antibodies (GM1, GD1a, GD1b) observed in Zika-associated ATM indicating para-infectious autoimmunity (Dec 2024; https://doi.org/10.1590/S1678-9946202466066) (colognese2024zikavirusinfection pages 8-10, colognese2024zikavirusinfection pages 5-6).
- Cell Types (CL):
  - Astrocytes (CL:0000127): primary cellular target in NMOSD astrocytopathy (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
  - Oligodendrocytes (CL:0000128): demyelination in TM/MOGAD (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
  - Microglia (CL:0000129): activation and cytokine/chemokine amplification; phagocytosis of myelin (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
  - Neurons (CL:0000540): axonal injury contributes to persistent deficits (NEJM 2010; Arquivos de Neuro-Psiquiatria 2024) (frohman2010transversemyelitis pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11).
- Anatomical Locations (UBERON): spinal cord (UBERON:0002240); longitudinally extensive transverse myelitis (LETM) defined as lesions spanning ≥3 vertebral levels (NEJM 2010; https://doi.org/10.1056/NEJMcp1001112) (frohman2010transversemyelitis pages 2-4).
- Chemical Entities (CHEBI) and Interventions:
  - High-dose corticosteroids (e.g., methylprednisolone) are first-line acute therapy; used across idiopathic/postinfectious and Zika-associated ATM (NEJM 2010; Zika review 2024) (frohman2010transversemyelitis pages 1-2, colognese2024zikavirusinfection pages 8-10).
  - Therapeutic plasma exchange (PLEX) is used for severe or steroid-refractory antibody-mediated myelitis; ongoing pragmatic Phase 3 trial testing early vs rescue PLEX (TIMELY-PLEX; NCT07100990; recruiting 2025) (NCT07100990).

Biological Processes (GO terms; suggested mappings)
- Complement activation, classical pathway (GO:0006958/GO:0006956): implicated by perivascular Ig/complement deposition in NMOSD lesions (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Antibody-dependent cytotoxicity (GO:0001788) and humoral immune response (GO:0006959): central to AQP4-IgG–mediated injury (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Myelination/demyelination (GO:0042552/GO:0008366) and axon degeneration (GO:0030422): core pathological processes (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Astrocyte activation (GO:0048143), microglial activation (GO:0001774), inflammatory response (GO:0006954): observed in TM lesions (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Blood–brain barrier disruption (GO:0035633 as related processes): secondary to astrocyte injury in NMOSD (NEJM 2010) (frohman2010transversemyelitis pages 1-2).

Cellular Components (GO terms; suggested mappings)
- Astrocyte endfoot and perivascular space (perivascular endfeet enriched for AQP4) where Ig/complement deposition occurs in NMOSD lesions (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Myelin sheath (GO:0043209) and node of Ranvier: loci of demyelination and conduction failure (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Extracellular space/perivascular regions for immune complex deposition; cytotoxic effectors likely operate at astrocyte plasma membrane AQP4 assemblies (NEJM 2010) (frohman2010transversemyelitis pages 1-2).

Disease Progression
- Sequence of events:
  1) Trigger (infection, vaccination, systemic autoimmune disease; parasitic or viral infections in some cases) leads to immune activation (NEJM 2010; Zika systematic review 2024) (frohman2010transversemyelitis pages 1-2, colognese2024zikavirusinfection pages 5-6).
  2) Autoantibody generation or dysregulated cell-mediated responses drive spinal cord inflammation; in NMOSD, AQP4-IgG binds astrocytes, activates complement; in MOGAD, anti-MOG promotes demyelinating attack (NEJM 2010; Zika review 2024) (frohman2010transversemyelitis pages 1-2, colognese2024zikavirusinfection pages 8-10).
  3) Lesion formation: perivascular immune deposition, astrocyte loss and demyelination, axonal injury; MRI shows intramedullary T2 hyperintense lesions with enhancement acutely (NEJM 2010) (frohman2010transversemyelitis pages 2-4).
  4) Clinical nadir within hours to 3 weeks; recovery phase mostly within 3 months; residual disability correlates with lesion extent and nadir severity (NEJM 2010; Arquivos 2024 LETM cohort) (frohman2010transversemyelitis pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11).
- Staging/phases: prodromal infectious symptoms (if present) → acute inflammatory phase with rapid neurological worsening → subacute stabilization → recovery/remodeling with potential chronic sequelae (NEJM 2010; Zika systematic review 2024) (frohman2010transversemyelitis pages 1-2, colognese2024zikavirusinfection pages 5-6).

Phenotypic Manifestations and Outcomes
- Core phenotypes: bilateral motor deficits (paresis/paraplegia), sensory level, Lhermitte’s sign, sphincter/autonomic dysfunction (urinary retention/incontinence, constipation) (NEJM 2010) (frohman2010transversemyelitis pages 2-4, naeem2022theassociationbetween pages 1-2).
- Spinal movement disorders: highly prevalent across non-MS inflammatory myelopathies—73% overall; most frequent in AQP4-IgG–positive NMOSD (92%) and least frequent in MOGAD (57%). Phenomena include tonic spasms (57%), focal dystonia (25%), spinal tremor (16%), spontaneous clonus (9.5%), secondary restless limb syndrome (9.5%), and spinal myoclonus (8%). LETM and AQP4-IgG were independent risk factors for movement disorders; MOG-IgG was associated with lower risk. Resolution at mean 11 months occurred in 19.5%, partial improvement in 37%, and persistent/worsening in 43% (J Neurol; Jul 2024; https://doi.org/10.1007/s00415-024-12527-6) (abboud2024spinalmovementdisorders pages 1-2, abboud2024spinalmovementdisorders pages 5-7).
- LETM long-term outcomes: In a 10-year follow-up cohort of first-episode LETM (n=39), final diagnoses included 51% monophasic seronegative LETM, 28% AQP4-IgG NMOSD, 7.7% seronegative NMOSD, 5% MOGAD, 5% recurrent seronegative LETM, and 2.6% MS. Mortality reached 10% (median time to death 3 years). Severe disability (EDSS ≥7) persisted in 17% of survivors; higher age at onset and higher EDSS at nadir predicted worse outcomes (Arquivos de Neuro-Psiquiatria; Aug 2024; https://doi.org/10.1055/s-0044-1789342) (silva2024longitudinallyextensivetransversemyelitis pages 10-11).

Triggers and Special Etiologies
- Post-/para-infectious triggers: Zika virus infection has been associated with ATM, sometimes with coinfection by dengue or chikungunya. Proposed mechanisms include direct neurotropism, systemic immune activation, and para-infectious autoimmunity (antiganglioside and anti-MOG antibodies). Mixed infection presentations showed shorter prodrome and worse disability than isolated ATM. MRI often shows multilevel cervical/thoracic T2 hyperintense lesions; enhancement is variable; brain involvement can co-occur. In a synthesis of 20 subjects, 6/14 isolated ATM had mRS ≤3, while 5/6 mixed cases had mRS 4–5 at short follow-up (Rev Inst Med Trop São Paulo; Dec 2024; https://doi.org/10.1590/S1678-9946202466066) (colognese2024zikavirusinfection pages 6-8, colognese2024zikavirusinfection pages 5-6, colognese2024zikavirusinfection pages 8-10).
- Parasitic infection: case-based literature documents schistosomiasis-associated myelitis; details in 2024 reports emphasize the importance of differential diagnosis in endemic settings, though mechanistic specifics are limited in the available excerpt (Arquivos de Neuro-Psiquiatria; Oct 2024; https://doi.org/10.1055/s-0045-1806986) (frohman2010transversemyelitis pages 1-2).
- Vaccination: TM has been reported after vaccines including COVID-19; hypothesized mechanisms include molecular mimicry and immune cross-reactivity (e.g., spike protein with myelin proteins). CSF in reported cases often shows elevated protein and pleocytosis; MRI shows intramedullary hyperintense lesions. Causality remains uncertain and mechanisms are incompletely understood (Ann Med & Surgery; Jul 2022; https://doi.org/10.1016/j.amsu.2022.103870) (naeem2022theassociationbetween pages 3-4, naeem2022theassociationbetween pages 2-3).

CSF/MRI Biomarkers
- MRI: acute gadolinium-enhancing intramedullary lesions; LETM defined by ≥3 vertebral segments carries greater morbidity; in Zika-associated ATM, lesions may be extensive from cervical levels to conus, sometimes non-enhancing and with concurrent brain lesions (NEJM 2010; Zika 2024) (frohman2010transversemyelitis pages 2-4, colognese2024zikavirusinfection pages 6-8, colognese2024zikavirusinfection pages 5-6).
- CSF: pleocytosis, elevated IgG index, or oligoclonal bands may support inflammatory myelitis; Zika-associated cases showed variable pleocytosis with sometimes low protein; pathogen PCR/IgM may be positive (NEJM 2010; Zika 2024) (frohman2010transversemyelitis pages 2-4, colognese2024zikavirusinfection pages 5-6).

Current applications and real-world implementations
- Acute treatment: high-dose IV corticosteroids remain first-line; PLEX is used as escalation or for antibody-mediated disease (NEJM 2010) (frohman2010transversemyelitis pages 1-2).
- Clinical trials: TIMELY-PLEX (NCT07100990), a pragmatic randomized Phase 3 trial, is evaluating early concurrent PLEX versus rescue PLEX after high-dose corticosteroids for severe optic neuritis and transverse myelitis; outcomes include EDSS at 6 months for TM and visual measures for ON (ClinicalTrials.gov; recruiting 2025) (NCT07100990).

Expert opinions and analysis
- The NEJM review emphasizes immune-mediated pathogenesis, particularly antibody/complement mechanisms in NMOSD, and recommends full spinal MRI with contrast and CSF analysis to confirm inflammation and exclude mimics. Prognosis relates to lesion extent, severity at nadir, and underlying etiology (NEJM 2010) (frohman2010transversemyelitis pages 1-2, frohman2010transversemyelitis pages 2-4).
- Prospective observational data underscore clinical distinctions among NMOSD, MOGAD, and idiopathic TM, with AQP4-IgG and LETM conferring higher risk for movement complications and indicating more extensive tract involvement—consistent with antibody-mediated astrocytopathy leading to secondary demyelination (J Neurol 2024) (abboud2024spinalmovementdisorders pages 1-2, abboud2024spinalmovementdisorders pages 5-7).

Relevant statistics and data
- Incidence: idiopathic/postinfectious TM estimated 1.3–8/million annually; 15–30% remain idiopathic (NEJM 2010; Aug 2010) (frohman2010transversemyelitis pages 1-2).
- Outcomes: LETM 10-year cohort—10% mortality, 17% severe disability among survivors; higher age at onset and higher EDSS nadir predicted worse outcomes (Arquivos; Aug 2024) (silva2024longitudinallyextensivetransversemyelitis pages 10-11).
- Movement disorders: 73% overall prevalence across myelitis types; 92% in AQP4-IgG NMOSD vs 57% in MOGAD; tonic spasms 57% (J Neurol; Jul 2024) (abboud2024spinalmovementdisorders pages 1-2, abboud2024spinalmovementdisorders pages 5-7).
- Zika-associated ATM: in short-term follow-up, 6/14 isolated ATM achieved mRS ≤3; mixed presentations frequently had mRS 4–5; dysautonomia present in a minority (Rev Inst Med Trop São Paulo; Dec 2024) (colognese2024zikavirusinfection pages 5-6, colognese2024zikavirusinfection pages 6-8).

Gene/protein annotations with ontology terms (HGNC, GO) and structured entities
- AQP4 (HGNC:633): biological processes—complement activation (GO:0006956), humoral immune response (GO:0006959). Cellular component—astrocyte plasma membrane/perivascular endfeet. Evidence: NEJM 2010 (frohman2010transversemyelitis pages 1-2).
- MOG (HGNC:7106): biological processes—myelination/demyelination (GO:0042552/GO:0008366). Evidence: Zika-associated anti-MOG; J Neurol distinctions (colognese2024zikavirusinfection pages 8-10, abboud2024spinalmovementdisorders pages 1-2).
- Complement components (process-level): classical pathway activation in NMOSD lesions (NEJM 2010) (frohman2010transversemyelitis pages 1-2).

Phenotype associations (HP terms; examples)
- Pyramidal weakness/paraparesis, sensory level, Lhermitte’s sign, urinary retention/incontinence, constipation; spinal movement disorders (tonic spasms, dystonia, tremor, clonus). Evidence: NEJM 2010; J Neurol 2024 (frohman2010transversemyelitis pages 2-4, abboud2024spinalmovementdisorders pages 1-2, abboud2024spinalmovementdisorders pages 5-7).

Cell type involvement (CL terms)
- Astrocytes (CL:0000127), oligodendrocytes (CL:0000128), microglia (CL:0000129), neurons (CL:0000540) (NEJM 2010; Arquivos 2024) (frohman2010transversemyelitis pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11).

Anatomical locations (UBERON terms)
- Spinal cord (UBERON:0002240); LETM spans ≥3 vertebral segments (NEJM 2010) (frohman2010transversemyelitis pages 2-4).

Chemical entities (CHEBI terms; interventions)
- Glucocorticoids (e.g., methylprednisolone) and therapeutic plasma exchange used acutely (NEJM 2010; ClinicalTrials.gov 2025) (frohman2010transversemyelitis pages 1-2, NCT07100990).

Evidence items with URLs/date
- Frohman EM, Wingerchuk DM. Transverse Myelitis. NEJM. Aug 2010. https://doi.org/10.1056/NEJMcp1001112 (frohman2010transversemyelitis pages 1-2, frohman2010transversemyelitis pages 2-4)
- Abboud H et al. Spinal movement disorders in NMOSD, MOGAD, and idiopathic TM. J Neurol. Jul 2024. https://doi.org/10.1007/s00415-024-12527-6 (abboud2024spinalmovementdisorders pages 1-2, abboud2024spinalmovementdisorders pages 5-7)
- Silva PBR et al. Longitudinally-extensive transverse myelitis: 10-year cohort. Arquivos de Neuro-Psiquiatria. Aug 2024. https://doi.org/10.1055/s-0044-1789342 (silva2024longitudinallyextensivetransversemyelitis pages 10-11)
- Colognese BA, Argollo N. Zika infection and acute transverse myelitis: systematic review. Rev Inst Med Trop São Paulo. Dec 2024. https://doi.org/10.1590/S1678-9946202466066 (colognese2024zikavirusinfection pages 8-10, colognese2024zikavirusinfection pages 6-8, colognese2024zikavirusinfection pages 5-6)
- Naeem FN et al. SARS‑CoV‑2 vaccines and transverse myelitis: review. Ann Med & Surgery. Jul 2022. https://doi.org/10.1016/j.amsu.2022.103870 (naeem2022theassociationbetween pages 3-4, naeem2022theassociationbetween pages 1-2, naeem2022theassociationbetween pages 2-3)
- TIMELY-PLEX Trial. ClinicalTrials.gov Identifier: NCT07100990. Recruiting (planned 2025 start). https://clinicaltrials.gov/ct2/show/NCT07100990 (NCT07100990)

Key artifact
| Entity type | Name | Ontology ID | Role in pathophysiology (1–2 sentences) | Evidence / citation (DOI or URL) | Evidence ID |
|---|---|---|---|---|---|
| Gene/Protein | Aquaporin-4 (AQP4) | HGNC:633 | AQP4 is the target antigen in NMOSD; AQP4-IgG binding leads to complement-mediated astrocyte injury with perivascular Ig/complement deposition and can produce necrotic, longitudinally extensive lesions. | https://doi.org/10.1056/NEJMcp1001112 (NEJM review) | (frohman2010transversemyelitis pages 1-2, abboud2024spinalmovementdisorders pages 1-2) |
| Gene/Protein | Myelin oligodendrocyte glycoprotein (MOG) | HGNC:7106 | Anti-MOG antibodies are associated with an inflammatory demyelinating myelitis phenotype (MOGAD), often para-infectious, characterized by prominent demyelination with distinct clinical/imaging features from AQP4-NMOSD. | https://doi.org/10.1590/S1678-9946202466066 (Zika–ATM review noting anti‑MOG) | (colognese2024zikavirusinfection pages 8-10, abboud2024spinalmovementdisorders pages 1-2) |
| Cell type | Astrocyte | CL:0000127 | Astrocytes (AQP4-expressing endfeet) are primary targets in NMOSD; astrocyte loss triggers secondary inflammation, blood–brain barrier disruption, and downstream demyelination. | https://doi.org/10.1056/NEJMcp1001112 | (frohman2010transversemyelitis pages 1-2) |
| Cell type | Oligodendrocyte | CL:0000128 | Oligodendrocyte dysfunction or loss underlies demyelination in TM and MOGAD; inflammatory mediators and antibody/opsonization can lead to myelin loss and impaired conduction. | https://doi.org/10.1056/NEJMcp1001112 | (frohman2010transversemyelitis pages 1-2) |
| Cell type | Microglia | CL:0000129 | Microglial activation contributes to lesion inflammation, phagocytosis of myelin, and secretion of cytokines/chemokines that amplify tissue injury. | https://doi.org/10.1056/NEJMcp1001112 | (frohman2010transversemyelitis pages 1-2) |
| Cell type | Neuron | CL:0000540 | Axonal and neuronal injury within the cord cause persistent disability; axonal loss correlates with poor long-term outcomes after severe TM/LETM. | https://doi.org/10.1056/NEJMcp1001112; https://doi.org/10.1055/s-0044-1789342 | (frohman2010transversemyelitis pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11) |
| Tissue | Spinal cord | UBERON:0002240 | The spinal cord is the anatomical locus of TM; longitudinally extensive transverse myelitis (LETM, ≥3 vertebral segments) associates with greater morbidity and mortality. | https://doi.org/10.1056/NEJMcp1001112; https://doi.org/10.1055/s-0044-1789342 | (frohman2010transversemyelitis pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11) |
| Intervention | High-dose corticosteroids | none | First-line acute immunotherapy to suppress spinal cord inflammation in ATM; commonly used in idiopathic, postinfectious, and Zika-associated cases. | https://doi.org/10.1056/NEJMcp1001112; https://doi.org/10.1590/S1678-9946202466066 | (frohman2010transversemyelitis pages 1-2, colognese2024zikavirusinfection pages 8-10) |
| Intervention | Therapeutic plasma exchange (PLEX) | none | PLEX is used for severe or steroid-refractory antibody-mediated myelitis; a randomized trial (TIMELY-PLEX) is testing early versus rescue PLEX timing in inflammatory myelitis. | https://clinicaltrials.gov/ct2/show/NCT07100990 | (NCT07100990) |
| Antibody | Anti-ganglioside antibodies (GM1, GD1a, GD1b) | none | Anti-ganglioside antibodies have been reported in Zika-associated ATM and may reflect para-infectious autoimmunity contributing to motor dysfunction via complement/Fc-mediated mechanisms. | https://doi.org/10.1590/S1678-9946202466066 | (colognese2024zikavirusinfection pages 8-10) |


*Table: Table summarizing principal genes/proteins, cell types, tissues, interventions, and antibodies implicated in transverse myelitis and related disorders, with ontology IDs and cited evidence (pqac IDs) for quick reference in a disease knowledgebase.*

Notes on scope and limitations
- Cytokine/chemokine-specific profiles and detailed lesion immunohistochemistry beyond complement/Ig deposition were not available in the extracted sources and remain areas for further sourcing. Where possible, we relied on a high-quality NEJM review for core mechanisms and 2024 studies for recent developments and outcomes (frohman2010transversemyelitis pages 1-2, abboud2024spinalmovementdisorders pages 1-2, silva2024longitudinallyextensivetransversemyelitis pages 10-11, colognese2024zikavirusinfection pages 8-10).

References

1. (frohman2010transversemyelitis pages 1-2): Elliot M. Frohman and Dean M. Wingerchuk. Transverse myelitis. New England Journal of Medicine, 363:564-572, Aug 2010. URL: https://doi.org/10.1056/nejmcp1001112, doi:10.1056/nejmcp1001112. This article has 265 citations and is from a highest quality peer-reviewed journal.

2. (frohman2010transversemyelitis pages 2-4): Elliot M. Frohman and Dean M. Wingerchuk. Transverse myelitis. New England Journal of Medicine, 363:564-572, Aug 2010. URL: https://doi.org/10.1056/nejmcp1001112, doi:10.1056/nejmcp1001112. This article has 265 citations and is from a highest quality peer-reviewed journal.

3. (abboud2024spinalmovementdisorders pages 1-2): Hesham Abboud, Rongyi Sun, Nikhil Modak, Mohamed Elkasaby, Alexander Wang, and Michael Levy. Spinal movement disorders in nmosd, mogad, and idiopathic transverse myelitis: a prospective observational study. Journal of Neurology, 271:5875-5885, Jul 2024. URL: https://doi.org/10.1007/s00415-024-12527-6, doi:10.1007/s00415-024-12527-6. This article has 6 citations and is from a domain leading peer-reviewed journal.

4. (abboud2024spinalmovementdisorders pages 5-7): Hesham Abboud, Rongyi Sun, Nikhil Modak, Mohamed Elkasaby, Alexander Wang, and Michael Levy. Spinal movement disorders in nmosd, mogad, and idiopathic transverse myelitis: a prospective observational study. Journal of Neurology, 271:5875-5885, Jul 2024. URL: https://doi.org/10.1007/s00415-024-12527-6, doi:10.1007/s00415-024-12527-6. This article has 6 citations and is from a domain leading peer-reviewed journal.

5. (naeem2022theassociationbetween pages 3-4): Fatima Naz Naeem, Syeda Fatima Saba Hasan, Muskaan Doulat Ram, Summaiyya Waseem, Syed Hassan Ahmed, and Taha Gul Shaikh. The association between sars-cov-2 vaccines and transverse myelitis: a review. Annals of Medicine &amp; Surgery, Jul 2022. URL: https://doi.org/10.1016/j.amsu.2022.103870, doi:10.1016/j.amsu.2022.103870. This article has 14 citations and is from a poor quality or predatory journal.

6. (naeem2022theassociationbetween pages 2-3): Fatima Naz Naeem, Syeda Fatima Saba Hasan, Muskaan Doulat Ram, Summaiyya Waseem, Syed Hassan Ahmed, and Taha Gul Shaikh. The association between sars-cov-2 vaccines and transverse myelitis: a review. Annals of Medicine &amp; Surgery, Jul 2022. URL: https://doi.org/10.1016/j.amsu.2022.103870, doi:10.1016/j.amsu.2022.103870. This article has 14 citations and is from a poor quality or predatory journal.

7. (silva2024longitudinallyextensivetransversemyelitis pages 10-11): Paula Baleeiro Rodrigues Silva, Samira Luisa Apóstolos-Pereira, Graziella Aguiar Santos Faria, Sara Terrim, Flávio Vieira Marques Filho, Mariana Gondim Peixoto Spricigo, Mateus Boaventura de Oliveira, Guilherme Diogo Silva, Douglas Kazutoshi Sato, and Tarso Adoni. Longitudinally-extensive transverse myelitis: impact on functional prognosis and mortality in a 10-year follow-up cohort. Arquivos de Neuro-Psiquiatria, Aug 2024. URL: https://doi.org/10.1055/s-0044-1789342, doi:10.1055/s-0044-1789342. This article has 0 citations and is from a peer-reviewed journal.

8. (colognese2024zikavirusinfection pages 8-10): Bianca Aparecida Colognese and Nayara Argollo. Zika virus infection and acute transverse myelitis: a comprehensive systematic review. Revista do Instituto de Medicina Tropical de São Paulo, Dec 2024. URL: https://doi.org/10.1590/s1678-9946202466066, doi:10.1590/s1678-9946202466066. This article has 2 citations.

9. (colognese2024zikavirusinfection pages 5-6): Bianca Aparecida Colognese and Nayara Argollo. Zika virus infection and acute transverse myelitis: a comprehensive systematic review. Revista do Instituto de Medicina Tropical de São Paulo, Dec 2024. URL: https://doi.org/10.1590/s1678-9946202466066, doi:10.1590/s1678-9946202466066. This article has 2 citations.

10. (NCT07100990): John J Chen. Treatment of Inflammatory Myelitis and Optic Neuritis With Early vs Rescue Plasma Exchange (TIMELY-PLEX). Mayo Clinic. 2025. ClinicalTrials.gov Identifier: NCT07100990

11. (naeem2022theassociationbetween pages 1-2): Fatima Naz Naeem, Syeda Fatima Saba Hasan, Muskaan Doulat Ram, Summaiyya Waseem, Syed Hassan Ahmed, and Taha Gul Shaikh. The association between sars-cov-2 vaccines and transverse myelitis: a review. Annals of Medicine &amp; Surgery, Jul 2022. URL: https://doi.org/10.1016/j.amsu.2022.103870, doi:10.1016/j.amsu.2022.103870. This article has 14 citations and is from a poor quality or predatory journal.

12. (colognese2024zikavirusinfection pages 6-8): Bianca Aparecida Colognese and Nayara Argollo. Zika virus infection and acute transverse myelitis: a comprehensive systematic review. Revista do Instituto de Medicina Tropical de São Paulo, Dec 2024. URL: https://doi.org/10.1590/s1678-9946202466066, doi:10.1590/s1678-9946202466066. This article has 2 citations.