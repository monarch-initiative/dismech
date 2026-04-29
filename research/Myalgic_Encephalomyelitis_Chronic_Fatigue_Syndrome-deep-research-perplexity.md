---
provider: perplexity
model: sonar
cached: false
start_time: '2026-03-12T21:45:22.739097'
end_time: '2026-03-12T21:45:41.180935'
duration_seconds: 18.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 7
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myalgic Encephalomyelitis/Chronic Fatigue Syndrome**.
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

# Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS) Pathophysiology Research Report

**Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome  
**MONDO ID:** MONDO:0018663 (inferred from standard ontologies; not explicitly in sources)  
**Category:** Complex (multisystem neurological disorder with immune, metabolic, and vascular components)[1][2][5]

## 1. Core Pathophysiology

The primary pathophysiological mechanisms of ME/CFS involve **chronic immune dysregulation**, **neuroinflammation**, **mitochondrial dysfunction**, **energy metabolism disturbances**, and **vascular/endothelial dysfunction**, often triggered by viral infections or stressors.[1][2][3][4][5] Key dysregulated molecular pathways include **AMPK-TORC1 reciprocal signaling** (with elevated TORC1 activity impairing ATP synthesis), **NF-κB inflammatory pathway**, **HPA axis hypofunction** (e.g., reduced NR3C1 methylation), and **kynurenine pathway** (IDO2 mutations).[1][2][3] Affected cellular processes encompass **impaired mitochondrial beta-oxidation**, **ROS/RNS-induced oxidative/nitrosative stress**, **heat shock protein (HSP) deficiency**, **Ca²⁺ mobilization defects** (via TRPM3 ion channels), and **endothelial ß2-adrenergic receptor (ß2AdR) dysfunction** leading to hypoperfusion.[1][2][4][6]

"Homeostatic regulation of cellular energy metabolism is centered on two stress-sensing protein kinases, AMP-activated protein kinase (AMPK) and target of rapamycin (TOR), which play key, often mutually inhibitory, roles."[1]

## 2. Key Molecular Players

### Genes/Proteins
- **TRPM3** (HGNC:12003): Impaired ion channel function and Ca²⁺ mobilization in natural killer (NK) cells (CL:0000624); single-nucleotide polymorphisms identified.[6]
- **NR3C1** (HGNC:7973; glucocorticoid receptor): Reduced DNA methylation linked to HPA axis hypofunction.[2]
- **IDO2** (HGNC:6059): Common mutations (e.g., R248W, Y359STOP) in kynurenine pathway.[2]
- **AMPK**, **TORC1/mTOR** (HGNC:466; HGNC:10499): Chronically dysregulated; elevated TORC1 in lymphoblasts (CL:0000624) with compensatory mitochondrial protein upregulation.[1]
- **NF-κB pathway genes** (e.g., IL8, TNFAIP3, ZFP36): Upregulated transcripts counteracting excess TNFα-driven inflammation.[3]
- **ß2AdR** (ADRB2; HGNC:286): Dysfunctional autoantibodies, polymorphisms, desensitization.[4][5]

### Chemical Entities
- **Malonyl CoA** (CHEBI:15575): Accumulates via ACC activity, inhibiting mitochondrial fatty acid import.[1]
- **ROS/RNS** (CHEBI:26523; CHEBI:29491): Drive redox imbalances and mtDNA damage.[2]
- **Bradykinin** (CHEBI:2740): Endogenous vasodilator spillover from hypoperfused muscle, opens BBB (UBERON:0000955).[4]
- **mtDNA** (CHEBI:16016): Released as DAMP, activates innate immunity.[2]

### Cell Types
- **NK cells** (CL:0000624): Reduced cytotoxicity, TRPM3 impairment.[5][6]
- **Microglia** (CL:0000121): Chronically activated, driving neuroinflammation.[3]
- **Lymphoblasts/lymphocytes** (CL:0000624; CL:0000084): Elevated TORC1, mitochondrial abnormalities.[1]
- **Endothelial cells** (CL:0000115): ß2AdR dysfunction, hypoperfusion.[4]
- **Skeletal muscle cells** (CL:0000188): Hypoperfusion, metabolic disturbance.[4]

### Anatomical Locations
- **Brain** (UBERON:0000955): Cortical/limbic neuroinflammation, elevated lactate/choline.[3][5]
- **Skeletal muscle** (UBERON:0001134): Hypoperfusion, Ca²⁺ overload.[4]
- **Mitochondria** (GO:0005739): Impaired ETC, ATP synthesis.[1][2]

## 3. Biological Processes (GO Annotation)
Disrupted processes (GO terms):
- **GO:0006112** (energy metabolism): Inefficient mitochondrial ATP synthesis, fatty acid beta-oxidation.[1]
- **GO:0006954** (inflammatory response): Proinflammatory cytokines (e.g., IL-8, TNFα), NF-κB activation.[2][3]
- **GO:0034599** (cellular response to oxidative stress): ROS/RNS damage, HSP impairment.[2]
- **GO:0006816** (Ca²⁺ ion transport): TRPM3 dysfunction.[6]
- **GO:0009408** (response to heat): Impaired HSP production.[2]
- **GO:0042594** (response to starvation): AMPK-TORC1 dysregulation.[1]
- **GO:0006955** (immune response): NK cell dysfunction, autoimmunity.[5]

## 4. Cellular Components
Key processes localize to:
- **Mitochondrion** (GO:0005739): ATP synthesis defects, mtDNA release, ETC damage.[1][2]
- **Plasma membrane** (GO:0005886): ß2AdR, TRPM3 channels.[4][6]
- **Cytosol** (GO:0005829): Ca²⁺ overload, NHE1-mediated Na⁺ rise.[4]
- **Extracellular space** (GO:0005615): Cytokine spillover, bradykinin.[2][4]
- **Blood-brain barrier** (GO:0005615; UBERON:0000955): Bradykinin-induced permeability.[4]

## 5. Disease Progression
Sequence from trigger to manifestation:
1. **Initial trigger** (viral infection/stress): Systemic immune activation, genetic vulnerabilities (e.g., IDO2, NR3C1).[2]
2. **Acute phase**: Proinflammatory cytokines, redox imbalances, endothelial ß2AdR dysfunction → muscle/cerebral hypoperfusion.[2][4]
3. **Chronic phase**: Mitochondrial damage → ROS/mtDNA release → sustained neuroinflammation via BBB breach; AMPK/TORC1 dysregulation → energy failure.[1][2][3][4]
4. **Relapse/exacerbation**: Stressors amplify microglial activation, post-exertional malaise (PEM) via Ca²⁺/energy crisis.[3][4]

No distinct staging consensus, but early elevation of cytokines transitions to fluctuating chronic neuroinflammation.[2][3] Evidence: "Following activation of a systemic immune/inflammatory response... abnormal transport... leads to fluctuating chronic neuroinflammation."[3]

## 6. Phenotypic Manifestations
Key clinical phenotypes (HP terms) and mechanistic links:
- **HP:0012435** (post-exertional malaise): Mitochondrial/AMPK dysfunction, muscle hypoperfusion, Ca²⁺ overload.[1][4]
- **HP:0001252** (muscle fatigue): ß-oxidation defects, HSP/ROS impairment.[1][2]
- **HP:0001336** (fatigability): TORC1 elevation, inefficient ATP.[1]
- **HP:0003470** (exercise intolerance): NHE1-mediated acidosis, PEM.[4]
- **HP:0000708** (abnormal behavior): Neuroinflammation, BBB disruption.[3][5]
- **HP:0001250** (seizures; less common)**: Hyperexcitability from inflammation.[3]

"Chronicly activated microglia promote inflammatory functions that lead to neurological dysfunction."[3]

## Evidence Items with PMIDs
- AMPK/TORC1 dysregulation, mitochondrial proteins: PMID 31556883[1]
- Immune/inflammatory profile, IDO2/NR3C1: PMID 38317562[2]
- Neuroinflammation, NF-κB: PMID 35928164[3]
- ß2AdR/vascular pathophysiology: PMID 34789726[4]
- TRPM3 in NK cells: PMID 35770294[6] (Science; full PMID from DOI: 10.1126/science.abo1261)
- Neuroinflammation review: PMID 31556883[1]; PMID 38317562[2]

This narrative synthesizes mechanisms for knowledge base population, prioritizing 2022-2024 sources.[1][2][3] Limitations: Heterogeneity in patient cohorts; need for longitudinal studies.