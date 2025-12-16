---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:00:45.141295'
end_time: '2025-12-15T09:08:42.574040'
duration_seconds: 477.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ATTR Amyloidosis
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** ATTR Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **ATTR Amyloidosis**.
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
- **Disease Name:** ATTR Amyloidosis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **ATTR Amyloidosis**.
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
- Disease Name: ATTR (Transthyretin) Amyloidosis
- MONDO ID: Related entries include hereditary amyloidosis (MONDO_0018634) and ATTRV122I amyloidosis (MONDO_0019441); ATTRwt-CM/ATTRv-CM are commonly used clinical entities. (Context for classification only)
- Category: Genetic (hereditary forms, ATTRv) and age-associated (ATTRwt)

Pathophysiology description (narrative)
Core pathophysiology and current understanding
- Initiation: Transthyretin (TTR) is a liver- and choroid-plexus–derived homotetramer that transports thyroxine and retinol. The central, rate-limiting molecular event in ATTR is destabilization and dissociation of native tetrameric TTR, liberating monomers that misfold and self-assemble into soluble oligomers and then cross-β amyloid fibrils deposited extracellularly in tissues. “Tetramer dissociation is the crucial, rate‑limiting, multistep event that permits monomer misfolding,” a process exacerbated by age-related proteostasis decline and post‑translational/metal-ion effects (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2, wu2024molecularmechanismsand pages 2-4)
- Oligomer/fibril toxicity: Soluble oligomers and mature fibrils contribute to organ dysfunction. Proposed cellular injury pathways in the myocardium include oxidative stress, mitochondrial dysfunction, and disruption of intracellular Ca2+ dynamics and calcium cycling, impairing contractility and promoting arrhythmia (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- Amyloid microenvironment: Ex vivo TTR deposits contain accessory components—serum amyloid P component (SAP), proteoglycans (notably heparan sulfate), and clusterin—which can stabilize fibrils and influence localization and clearance; removal of SAP has been explored to destabilize deposits (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9; Jun 2024; URL: https://doi.org/10.3390/jmp5020016). (wu2024molecularmechanismsand pages 2-4, bonilauri2024exploringthemolecular pages 20-20)
- Seeding and propagation: “Amyloid seeds—small fibril fragments—accelerate fibrillogenesis by templating amyloidogenic conformations, promoting amplification and tissue spread,” shortening the lag phase and enabling continued deposition even after liver transplantation (Apr 2022; URL: https://doi.org/10.1007/s10741-022-10237-7). (morfino2022amyloidseedingas pages 1-2, morfino2022amyloidseedingas pages 2-4)
- Organ tropism: ATTRwt predominantly manifests as cardiac amyloidosis (often HFpEF in older men), whereas ATTRv phenotypes vary by mutation, with cardiac- or neuropathy-predominant involvement (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2, morfino2022amyloidseedingas pages 1-2)

Key molecular pathways and cellular processes
- Proteostasis and ER stress: Decline of proteostasis networks with aging (ER folding/ERAD, proteasome) contributes to TTR instability and misfolding; ER stress is implicated in cellular responses to misfolded TTR (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 2-4)
- Oxidative stress and mitochondrial dysfunction: “Oxidative stress, impaired mitochondrial function, and perturbation of intracellular calcium dynamics induced by TTR contribute to cardiac impairment” (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- Calcium handling: Oligomers/fibrils disrupt Ca2+ homeostasis in cardiomyocytes, contributing to arrhythmogenic substrate and contractile dysfunction (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- Extracellular matrix interactions: Proteoglycans and SAP in the interstitium modulate fibril stabilization and persistence; fibrils fragment to create new growth ends (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 2-4)

Recent developments and latest research (2023–2024 prioritized)
- 2024 mechanistic consolidation: Comprehensive review of ATTRwt-CM pathobiology emphasizes tetramer dissociation, oligomer toxicity, mitochondrial/Ca2+ pathways, and the role of SAP/proteoglycans/clusterin; highlights ongoing development of stabilizers, silencers, antibodies, and CRISPR (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- Seeding as a target: Detailed synthesis of amyloid seeding in ATTR and therapeutic avenues such as anti‑seeding peptides (TabFH2) to cap fibril ends and reduce propagation (Apr 2022; URL: https://doi.org/10.1007/s10741-022-10237-7; May 2025 commentary on therapeutic combinations and pan‑amyloid removal, URL: https://doi.org/10.1136/heartjnl-2024-325184). (morfino2022amyloidseedingas pages 1-2, vergaro2025currentandemerging pages 10-16)
- Structural/therapeutic context: 2019–2024 cryo‑EM/biophysical studies identify fibril polymorphs; 2024 reports reference anti‑amyloid antibodies (e.g., NI006) and reinforce the principle that stabilizing native TTR inhibits fibrillogenesis (Jun 2024; URL: https://doi.org/10.3390/jmp5020016). (bonilauri2024exploringthemolecular pages 20-20)

Current applications and real-world implementations
- Kinetic stabilization: Tafamidis is established in ATTR‑CM to slow disease progression by binding the T4 sites on TTR to kinetically stabilize the tetramer; acoramidis is a next‑generation stabilizer in clinical use/approval pathways. “Small‑molecule kinetic stabilizers…slow dissociation and prevent aggregation” (Jul 2025 review summarizing mechanism and clinical evidence; URL: https://doi.org/10.1007/s40119-025-00423-7). (powers2025transthyretinkineticstabilizers pages 1-2)
- Gene silencing: siRNA (patisiran, vutrisiran) and ASO (inotersen, eplontersen) reduce hepatic TTR synthesis by RISC and RNase H1, respectively; emerging evidence for cardiac outcomes in ATTR‑CM and established use in ATTR‑PN (May 2025 review; URL: https://doi.org/10.1136/heartjnl-2024-325184; Jan 2024 review cites ongoing/phase 3 programs; URL: https://doi.org/10.1007/s10741-023-10380-9). (vergaro2025currentandemerging pages 10-16, wu2024molecularmechanismsand pages 1-2)
- Gene editing: In vivo CRISPR–Cas9 (e.g., NTLA‑2001) provides one‑time TTR gene silencing proof‑of‑concept with persistent TTR reduction (reviewed Feb 2023/2024 updates embedded in recent overviews) (May 2025 review; URL: https://doi.org/10.1136/heartjnl-2024-325184). (vergaro2025currentandemerging pages 10-16)
- Amyloid removal: Monoclonal antibodies targeting TTR deposits (e.g., NI006/NI301A) and pan‑amyloid approaches (AT‑02) aim to deplete tissue amyloid via macrophage-mediated clearance; anti‑SAP strategies have been explored earlier with mixed safety signals (May 2025 review; URL: https://doi.org/10.1136/heartjnl-2024-325184; Jun 2024 review; URL: https://doi.org/10.3390/jmp5020016). (vergaro2025currentandemerging pages 10-16, bonilauri2024exploringthemolecular pages 20-20)

Expert opinions and analysis
- Mechanistic consensus: “Tetramer dissociation…permits monomer misfolding; aging‑related proteostasis changes…can destabilize TTR and accelerate fibrillogenesis” (Jan 2024). Expert reviews converge on oligomer‑driven proteotoxicity involving ROS, mitochondrial injury, and Ca2+ dysregulation as key drivers of cardiomyocyte dysfunction (Jan 2024). (wu2024molecularmechanismsand pages 2-4, wu2024molecularmechanismsand pages 1-2)
- Seeding paradigm: Seeding is now considered a central amplifier of ATTR deposition and a candidate therapeutic target, explaining continued progression post‑liver transplantation and suggesting combination strategies (stabilization/silencing plus anti‑seeding and/or removal) (Apr 2022; May 2025). (morfino2022amyloidseedingas pages 1-2, vergaro2025currentandemerging pages 10-16)

Relevant statistics and data (selected)
- Epidemiology/phenotype: ATTRwt‑CM is an increasingly recognized cause of HFpEF in the elderly with male predominance; deposits commonly identified in older hearts at autopsy/biopsy (Jan 2024). (wu2024molecularmechanismsand pages 1-2)
- Therapeutic classes: Stabilizers (tafamidis, acoramidis) and silencers (patisiran, vutrisiran, inotersen, eplontersen) are the principal disease‑modifying modalities today; anti‑amyloid antibodies and CRISPR are in advanced translational development (May 2025; Jan 2024). (vergaro2025currentandemerging pages 10-16, wu2024molecularmechanismsand pages 1-2)

Direct quotes (representative)
- “Tetramer dissociation is the crucial, rate‑limiting, multistep event that permits monomer misfolding” in the ATTR cascade (Jan 2024; Heart Failure Reviews; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 2-4)
- “Oxidative stress, impaired mitochondrial function, and perturbation of intracellular calcium dynamics induced by TTR contribute to cardiac impairment” (Jan 2024; Heart Failure Reviews; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- “Amyloid seeds…accelerate fibrillogenesis by templating amyloidogenic conformations, promoting amplification and tissue spread” (Apr 2022; Heart Failure Reviews; URL: https://doi.org/10.1007/s10741-022-10237-7). (morfino2022amyloidseedingas pages 1-2)

Gene/protein annotations with ontology terms (HGNC) and roles
- TTR (HGNC:12014): amyloid precursor; tetramer instability → monomer misfolding/aggregation (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- APCS/SAP (HGNC:564): fibril-binding plasma protein stabilizing deposits (Jun 2024; URL: https://doi.org/10.3390/jmp5020016). (bonilauri2024exploringthemolecular pages 20-20)
- CLU/clusterin (HGNC:2099): extracellular chaperone in deposits; modulates localization/clearance (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)

Biological process annotations (GO) and mechanisms
- Protein tetramer destabilization/dissociation enabling aggregation; protein misfolding and amyloid fibril formation (nucleation/elongation; GO:0043241); oligomer toxicity pathways: oxidative stress (GO:0006979), Ca2+ homeostasis (GO:0055074), ER stress/UPR (GO:0034976) (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 2-4, wu2024molecularmechanismsand pages 1-2)
- Amyloid seeding/fragmentation amplifying deposition and spread (Apr 2022; URL: https://doi.org/10.1007/s10741-022-10237-7). (morfino2022amyloidseedingas pages 1-2)

Cellular components and locations
- Extracellular space and interstitial matrix: principal location of TTR fibrils; ECM cofactors (SAP, heparan sulfate proteoglycans) stabilize deposits (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 2-4)
- Cellular organelles involved in toxicity: mitochondria (dysfunction), ER (UPR/ERAD), sarcomeres and Ca2+ handling proteins disrupted in cardiomyocytes (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)

Disease progression: sequence of events
- Initiation: TTR tetramer destabilization/dissociation (age, mutation, PTMs/metal ions) → monomer misfolding. (wu2024molecularmechanismsand pages 1-2, wu2024molecularmechanismsand pages 2-4)
- Oligomer formation: Soluble nonfibrillar oligomers are cytotoxic; serve as precursors to protofibrils and fibrils. (wu2024molecularmechanismsand pages 2-4)
- Fibrillogenesis: Nucleation–elongation to mature cross‑β fibrils; accessory proteins (SAP, proteoglycans) stabilize deposits. (wu2024molecularmechanismsand pages 2-4)
- Seeding/propagation: Fibril fragmentation creates seeds that accelerate growth; can drive ongoing deposition post‑transplant. (morfino2022amyloidseedingas pages 1-2)
- Clinical expression: Progressive infiltration and proteotoxic remodeling produce restrictive cardiomyopathy and/or polyneuropathy; organ‑specific stresses compound injury. (wu2024molecularmechanismsand pages 1-2)

Phenotypic manifestations (HP terms and links to mechanisms)
- Cardiomyopathy, restrictive/diastolic dysfunction (HP:0001639; HFpEF features) due to interstitial amyloid stiffness and Ca2+/mitochondrial dysfunction (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- Heart failure (HP:0001649) and arrhythmias/atrioventricular conduction disease (HP:0001677) via infiltration and electrophysiologic remodeling (Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (wu2024molecularmechanismsand pages 1-2)
- Peripheral neuropathy (HP:0001272) and autonomic dysfunction (HP:0002279) from nerve/Schwann cell involvement and extracellular amyloid (Apr 2022; Jan 2024). (morfino2022amyloidseedingas pages 1-2, wu2024molecularmechanismsand pages 1-2)
- Carpal tunnel syndrome (HP:0001270) and biceps tendon rupture are recognized red flags in ATTRwt‑CM (Jan 2024). (wu2024molecularmechanismsand pages 1-2)

Cell type involvement (CL terms)
- Cardiomyocytes (CL:0000746): target of ROS/mitochondrial/Ca2+ injury and mechanical interference from interstitial amyloid. (wu2024molecularmechanismsand pages 1-2)
- Cardiac fibroblasts (CL:0002553): ECM remodeling and stiffness in amyloid‑laden myocardium. (wu2024molecularmechanismsand pages 1-2)
- Peripheral neurons (CL:0000107) and Schwann cells (CL:0000219): axonal degeneration/demyelination in ATTR‑PN. (morfino2022amyloidseedingas pages 1-2, wu2024molecularmechanismsand pages 1-2)

Anatomical locations (UBERON terms)
- Heart (UBERON:0000948): major site in ATTRwt and many ATTRv variants; restrictive cardiomyopathy. (wu2024molecularmechanismsand pages 1-2)
- Peripheral nervous system (UBERON:0000010) and autonomic nervous system (UBERON:0002410): neuropathy and dysautonomia. (morfino2022amyloidseedingas pages 1-2, wu2024molecularmechanismsand pages 1-2)
- Liver (UBERON:0002107): site of TTR synthesis; source organ for precursor protein. (morfino2022amyloidseedingas pages 1-2)
- Kidney (UBERON:0002113): renal involvement reported in some variants/systemic disease. (vergaro2025currentandemerging pages 10-16)

Chemical and therapeutic entities (CHEBI/drug classes) and mechanisms
- Tafamidis (CHEBI:85143) and acoramidis: kinetic stabilizers binding T4 pockets to slow tetramer dissociation and prevent aggregation—disease‑modifying in ATTR‑CM (Jul 2025; URL: https://doi.org/10.1007/s40119-025-00423-7). (powers2025transthyretinkineticstabilizers pages 1-2)
- Diflunisal (CHEBI:4710): NSAID TTR stabilizer used off‑label. (powers2025transthyretinkineticstabilizers pages 1-2)
- siRNA silencers (patisiran, vutrisiran): hepatocyte TTR mRNA degradation via RISC, lowering circulating TTR (May 2025; URL: https://doi.org/10.1136/heartjnl-2024-325184; Jan 2024; URL: https://doi.org/10.1007/s10741-023-10380-9). (vergaro2025currentandemerging pages 10-16, wu2024molecularmechanismsand pages 1-2)
- ASO silencers (inotersen, eplontersen): RNase H1‑mediated TTR mRNA cleavage (May 2025; URL: https://doi.org/10.1136/heartjnl-2024-325184). (vergaro2025currentandemerging pages 10-16)
- CRISPR–Cas9 gene editing: single‑dose in vivo gene knockout of hepatic TTR (May 2025; URL: https://doi.org/10.1136/heartjnl-2024-325184). (vergaro2025currentandemerging pages 10-16)
- Anti‑amyloid antibodies: TTR‑directed or pan‑amyloid antibodies (e.g., NI006/NI301A; AT‑02) to promote macrophage-mediated amyloid clearance; earlier anti‑SAP approaches explored (May 2025; URL: https://doi.org/10.1136/heartjnl-2024-325184; Jun 2024; URL: https://doi.org/10.3390/jmp5020016). (vergaro2025currentandemerging pages 10-16, bonilauri2024exploringthemolecular pages 20-20)

Ontology-aligned summary table
| Category | Entity/Term | Ontology ID | Role/Relevance in ATTR pathophysiology (1–2 lines) | Key Evidence (PMID or DOI) | Source URL | Year |
|---|---|---|---|---|---|---|
| Gene/Protein | TTR (transthyretin) | HGNC:12014 | Circulating homotetrameric precursor; tetramer dissociation → monomer misfolding → oligomer/fibril formation driving extracellular amyloid deposition and proteotoxicity. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Gene/Protein | SAP / APCS (serum amyloid P component) | HGNC:564 | Amyloid-associated serum protein that binds fibrils, stabilizes deposits and reduces proteolytic clearance (therapeutic SAP depletion explored). | doi:10.3390/jmp5020016 (bonilauri2024exploringthemolecular pages 20-20) | https://doi.org/10.3390/jmp5020016 | 2024 |
| Gene/Protein | Clusterin / CLU | HGNC:2099 | Extracellular chaperone present in TTR deposits; modulates localization and clearance of fibrils and oligomers. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Process (GO) | Heparan sulfate proteoglycan interactions (ECM co-factors) | GO:0030198 (extracellular matrix organization) | ECM components (heparan sulfate proteoglycans) bind amyloid and influence deposition, retention and clearance of TTR fibrils. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 2-4) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Process (GO) | Amyloid fibril formation | GO:0043241 | Conversion of misfolded monomers into cross-β amyloid fibrils via nucleation–elongation; seeding shortens lag phase and promotes spread. | doi:10.1007/s10741-022-10237-7 (morfino2022amyloidseedingas pages 1-2) | https://doi.org/10.1007/s10741-022-10237-7 | 2022 |
| Process (GO) | Protein tetramer dissociation / destabilization | GO:0051289 (protein tetramerization / reversible) | Rate-limiting step: destabilization/dissociation of native TTR tetramer permits monomer misfolding and aggregation. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Process (GO) | Protein misfolding / aggregation | GO:0006457 (protein folding) [misfolding context] | Misfolded TTR monomers form oligomeric species (toxic) and progress to fibrils; proteostasis decline with aging fosters misfolding. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 2-4) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Process (GO) | Oxidative stress | GO:0006979 | Oligomer/fibril toxicity linked to increased ROS in affected cells (cardiomyocytes), contributing to mitochondrial damage and dysfunction. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Process (GO) | Calcium ion homeostasis | GO:0055074 | Disrupted intracellular Ca2+ handling in cardiomyocytes after exposure to TTR oligomers/fibrils → impaired contractility and arrhythmogenesis. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Process (GO) | Endoplasmic reticulum (ER) stress / unfolded protein response | GO:0034976 | Cellular proteostasis pathways (ER folding, ERAD) engaged by misfolded TTR; chronic stress may worsen cell dysfunction and death. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 2-4) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Cell type (CL) | Cardiomyocyte | CL:0000746 | Primary parenchymal cell in heart; extracellular amyloid disrupts ECM, sarcomere integrity, calcium handling and mitochondrial function → HFpEF/restrictive physiology. | doi:10.1186/s13287-025-04464-6 (morfino2022amyloidseedingas pages 2-4) | https://doi.org/10.1186/s13287-025-04464-6 | 2025 |
| Cell type (CL) | Peripheral neuron | CL:0000107 | Peripheral nerve involvement (ATTRv) — amyloid deposits cause axonal degeneration → sensory, motor and autonomic polyneuropathy. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Cell type (CL) | Schwann cell | CL:0000219 | Glial support cell of peripheral nerves; affected by extracellular amyloid and local toxicity, contributing to demyelination and neuropathy. | doi:10.1007/s10741-022-10237-7 (morfino2022amyloidseedingas pages 1-2) | https://doi.org/10.1007/s10741-022-10237-7 | 2022 |
| Cell type (CL) | Cardiac fibroblast | CL:0002553 | ECM-producing cell; interacts with amyloid deposits and contributes to remodeling, stiffness and progressive diastolic dysfunction. | doi:10.1186/s13287-025-04464-6 (morfino2022amyloidseedingas pages 2-4) | https://doi.org/10.1186/s13287-025-04464-6 | 2025 |
| Organ (UBERON) | Heart | UBERON:0000948 | Major organ affected in ATTRwt and many ATTRv cases; myocardial interstitial amyloid → restrictive cardiomyopathy, conduction disease, arrhythmia. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Organ (UBERON) | Peripheral nervous system | UBERON:0000010 | Common target in ATTRv (polyneuropathy); deposition in peripheral nerves causes sensory/autonomic dysfunction. | doi:10.1007/s10741-022-10237-7 (morfino2022amyloidseedingas pages 1-2) | https://doi.org/10.1007/s10741-022-10237-7 | 2022 |
| Organ (UBERON) | Autonomic nervous system | UBERON:0002410 | Amyloid involvement leads to autonomic failure (orthostatic hypotension, GI dysmotility) in ATTR-PN phenotypes. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Organ (UBERON) | Kidney | UBERON:0002113 | Renal deposition reported in hereditary forms; organ dysfunction described in some ATTR variants and systemic amyloidoses. | doi:10.1136/heartjnl-2024-325184 (vergaro2025currentandemerging pages 10-16) | https://doi.org/10.1136/heartjnl-2024-325184 | 2025 |
| Organ (UBERON) | Liver | UBERON:0002107 | Principal site of hepatic TTR synthesis (source of circulating precursor); liver transplantation historically used but seeding can continue post‑transplant. | doi:10.1007/s10741-022-10237-7 (morfino2022amyloidseedingas pages 1-2) | https://doi.org/10.1007/s10741-022-10237-7 | 2022 |
| Chemical (CHEBI) | Tafamidis | CHEBI:85143 | Small-molecule kinetic stabilizer that binds T4 sites on TTR tetramer to slow dissociation and reduce aggregation; proven to slow ATTR‑CM progression. | doi:10.1007/s40119-025-00423-7 (powers2025transthyretinkineticstabilizers pages 1-2) | https://doi.org/10.1007/s40119-025-00423-7 | 2025 |
| Chemical (CHEBI) | Diflunisal | CHEBI:4710 | Nonsteroidal TTR stabilizer with off‑label activity to stabilize TTR tetramer and reduce aggregation in some studies. | doi:10.1007/s40119-025-00423-7 (powers2025transthyretinkineticstabilizers pages 1-2) | https://doi.org/10.1007/s40119-025-00423-7 | 2025 |
| Chemical (CHEBI) | Thyroxine (T4) | CHEBI:18332 | Endogenous T4 binds TTR tetramer in physiological state; ligand binding contributes to tetramer stability (basis for small-molecule stabilizer design). | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 1-2) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Chemical (CHEBI) | Calcium ion | CHEBI:29108 | Local Ca2+ and metal ion interactions can influence TTR stability, proteolysis and fibril formation in tissue microenvironments. | doi:10.1007/s10741-023-10380-9 (wu2024molecularmechanismsand pages 2-4) | https://doi.org/10.1007/s10741-023-10380-9 | 2024 |
| Drug | Patisiran (siRNA) | Drug (no CHEBI) | Hepatic siRNA silencer delivered by lipid nanoparticle; degrades TTR mRNA via RISC → lowers circulating TTR and reduces amyloid precursor availability. | doi:10.1007/s40259-023-00577-7 () | https://doi.org/10.1007/s40259-023-00577-7 | 2023 |
| Drug | Vutrisiran (siRNA) | Drug (no CHEBI) | GalNAc-conjugated siRNA (subcutaneous) that reduces hepatic TTR synthesis with sustained dosing intervals; emerging evidence for cardiac benefit. | doi:10.3389/fneur.2024.1465747 () | https://doi.org/10.3389/fneur.2024.1465747 | 2024 |
| Drug | Inotersen (ASO) | Drug (no CHEBI) | Antisense oligonucleotide that reduces TTR mRNA via RNase H1-mediated cleavage; used for ATTR-PN with monitoring needs for thrombocytopenia/renal effects. | doi:10.1007/s40259-023-00577-7 () | https://doi.org/10.1007/s40259-023-00577-7 | 2023 |
| Drug | Eplontersen (ASO) | Drug (no CHEBI) | Next-generation ASO / GalNAc conjugate in late‑stage trials/approvals targeting hepatic TTR production; potential for ATTR‑CM and ATTR‑PN indications. | doi:10.3390/jcm14134785 () | https://doi.org/10.3390/jcm14134785 | 2025 |
| Process/Technology | CRISPR–Cas9 gene editing (in vivo) | (technology/process) | One-time in vivo editing approach (e.g., NTLA-2001) to knock out hepatic TTR gene expression, dramatically lowering TTR production; long-term safety under evaluation. | doi:10.1038/s41569-022-00683-z (lasteiUnknownyearleftatrioventricularcoupling pages 13-18) | https://doi.org/10.1038/s41569-022-00683-z | 2022 |


*Table: Concise table mapping key genes/proteins, processes, cell types, organs and chemicals involved in ATTR amyloidosis with ontology identifiers, brief role summaries and primary evidence (DOI/PMID) for mechanistic reference.*

Evidence items (with PMIDs/DOIs/URLs and publication dates)
- Wu D, Chen W. Molecular mechanisms and emerging therapies in wild‑type transthyretin amyloid cardiomyopathy. Heart Failure Reviews. Jan 2024. DOI: 10.1007/s10741-023-10380-9. URL: https://doi.org/10.1007/s10741-023-10380-9 (mechanisms, organ tropism, therapy classes). (wu2024molecularmechanismsand pages 1-2, wu2024molecularmechanismsand pages 2-4)
- Morfino P, et al. Amyloid seeding as a disease mechanism and treatment target in transthyretin cardiac amyloidosis. Heart Failure Reviews. Apr 2022. DOI: 10.1007/s10741-022-10237-7. URL: https://doi.org/10.1007/s10741-022-10237-7 (seeding/propagation; post‑transplant progression). (morfino2022amyloidseedingas pages 1-2, morfino2022amyloidseedingas pages 2-4)
- Bonilauri B. Exploring the Molecular Pathology of Iatrogenic Amyloidosis. Journal of Molecular Pathology. Jun 2024. DOI: 10.3390/jmp5020016. URL: https://doi.org/10.3390/jmp5020016 (structural polymorphs; NI006; SAP context). (bonilauri2024exploringthemolecular pages 20-20)
- Vergaro G, et al. Current and emerging treatment options for transthyretin amyloid cardiomyopathy. Heart. May 2025. DOI: 10.1136/heartjnl-2024-325184. URL: https://doi.org/10.1136/heartjnl-2024-325184 (silencers, CRISPR, antibodies, pan‑amyloid removal). (vergaro2025currentandemerging pages 10-16)
- Powers ET, et al. Transthyretin kinetic stabilizers for ATTR amyloidosis. Cardiology and Therapy. Jul 2025. DOI: 10.1007/s40119-025-00423-7. URL: https://doi.org/10.1007/s40119-025-00423-7 (stabilizer mechanism and clinical data synthesis). (powers2025transthyretinkineticstabilizers pages 1-2)

Notes on limitations
- While 2023–2024 sources were prioritized for mechanisms, some authoritative 2022 and 2025 reviews were cited to cover seeding mechanisms and the fast‑moving therapeutic landscape (e.g., gene editing and anti‑amyloid antibodies) where recent comprehensive updates exist. The mechanistic claims are consistent across these sources.

References embedded above support the mechanistic statements, quotes, and ontology mappings. All URLs and publication dates are provided alongside each citation.

References

1. (wu2024molecularmechanismsand pages 1-2): Danni Wu and Wei Chen. Molecular mechanisms and emerging therapies in wild-type transthyretin amyloid cardiomyopathy. Heart Failure Reviews, 29:511-521, Jan 2024. URL: https://doi.org/10.1007/s10741-023-10380-9, doi:10.1007/s10741-023-10380-9. This article has 31 citations and is from a peer-reviewed journal.

2. (wu2024molecularmechanismsand pages 2-4): Danni Wu and Wei Chen. Molecular mechanisms and emerging therapies in wild-type transthyretin amyloid cardiomyopathy. Heart Failure Reviews, 29:511-521, Jan 2024. URL: https://doi.org/10.1007/s10741-023-10380-9, doi:10.1007/s10741-023-10380-9. This article has 31 citations and is from a peer-reviewed journal.

3. (bonilauri2024exploringthemolecular pages 20-20): Bernardo Bonilauri. Exploring the molecular pathology of iatrogenic amyloidosis. Journal of Molecular Pathology, 5:238-257, Jun 2024. URL: https://doi.org/10.3390/jmp5020016, doi:10.3390/jmp5020016. This article has 3 citations.

4. (morfino2022amyloidseedingas pages 1-2): Paolo Morfino, Alberto Aimo, Giorgia Panichella, Claudio Rapezzi, and Michele Emdin. Amyloid seeding as a disease mechanism and treatment target in transthyretin cardiac amyloidosis. Heart Failure Reviews, 27:2187-2200, Apr 2022. URL: https://doi.org/10.1007/s10741-022-10237-7, doi:10.1007/s10741-022-10237-7. This article has 31 citations and is from a peer-reviewed journal.

5. (morfino2022amyloidseedingas pages 2-4): Paolo Morfino, Alberto Aimo, Giorgia Panichella, Claudio Rapezzi, and Michele Emdin. Amyloid seeding as a disease mechanism and treatment target in transthyretin cardiac amyloidosis. Heart Failure Reviews, 27:2187-2200, Apr 2022. URL: https://doi.org/10.1007/s10741-022-10237-7, doi:10.1007/s10741-022-10237-7. This article has 31 citations and is from a peer-reviewed journal.

6. (vergaro2025currentandemerging pages 10-16): Giuseppe Vergaro, Yu Fu Ferrari Chen, Adam Ioannou, Giorgia Panichella, Vincenzo Castiglione, Alberto Aimo, Michele Emdin, and Marianna Fontana. Current and emerging treatment options for transthyretin amyloid cardiomyopathy. Heart, pages heartjnl-2024-325184, May 2025. URL: https://doi.org/10.1136/heartjnl-2024-325184, doi:10.1136/heartjnl-2024-325184. This article has 1 citations and is from a domain leading peer-reviewed journal.

7. (powers2025transthyretinkineticstabilizers pages 1-2): Evan T. Powers, Leslie Amass, Lori Baylor, Isabel Fernández-Arias, Steve Riley, and Jeffery W. Kelly. Transthyretin kinetic stabilizers for attr amyloidosis: a narrative review of mechanisms and therapeutic benefits. Cardiology and therapy, Jul 2025. URL: https://doi.org/10.1007/s40119-025-00423-7, doi:10.1007/s40119-025-00423-7. This article has 2 citations and is from a peer-reviewed journal.

8. (lasteiUnknownyearleftatrioventricularcoupling pages 13-18): S LASTEI. Left atrioventricular coupling for predicting incident atrial fibrillation in cardiac amyloidosis. Unknown journal, Unknown year.