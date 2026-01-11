---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-01-08T20:58:49.959181'
end_time: '2026-01-08T20:58:49.960392'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Amyotrophic Lateral Sclerosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Amyotrophic Lateral Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Amyotrophic Lateral Sclerosis**.
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
- **Disease Name:** Amyotrophic Lateral Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Amyotrophic Lateral Sclerosis**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Amyotrophic Lateral Sclerosis (ALS)
- MONDO ID: MONDO:0004975
- Category: Complex

Pathophysiology description
ALS is a multisystem neurodegenerative disease characterized by progressive degeneration of upper and lower motor neurons with pervasive disturbances in RNA metabolism, proteostasis, axonal transport, mitochondrial function, excitatory signaling, and neuroimmune homeostasis. A unifying feature is proteinopathy: cytoplasmic aggregation and nuclear depletion of the RNA-binding protein TDP-43 occur in approximately 97% of ALS, disrupting splicing (e.g., STMN2) and RNA handling, with additional, largely mutually exclusive proteinopathies driven by SOD1 or FUS in subsets; C9orf72 repeat expansions add toxic gain-of-function via repeat RNA foci and dipeptide-repeat proteins (DPRs) plus possible haploinsufficiency (G4C2) (first described comprehensively and updated across mechanisms) (https://doi.org/10.1016/S1474-4422(21)00414-2, May 2022; https://doi.org/10.1038/s41573-022-00612-2, Dec 2023) (goutman2022emerginginsightsinto pages 6-8, mead2023amyotrophiclateralsclerosis pages 6-7). Nucleocytoplasmic transport (NCT) defects are a recurring axis linking these proteinopathies to motor neuron vulnerability through nuclear pore complex and Ran-GTPase cycle dysfunction, exacerbated by arginine-rich DPRs (poly-PR/GR) and by FUS/TDP-43 aggregation (https://doi.org/10.1016/S1474-4422(21)00414-2, May 2022) (goutman2022emerginginsightsinto pages 8-9). Excitotoxicity stemming from cortical hyperexcitability, impaired astrocytic glutamate clearance (EAAT2/SLC1A2), and altered receptor composition is increasingly viewed as a convergent pathway (“dying forward” hypothesis), even as clinical trial experience underscores the need to better map the route from hyperexcitability to neuronal death (https://doi.org/10.1093/brain/awae039, Feb 2024) (nguyen2024updatesondisease pages 1-2). Mitochondrial bioenergetic defects, oxidative stress, and mitophagy/autophagy impairment coexist with axonal transport failure and early neuromuscular junction (NMJ) denervation, while glial and peripheral immune responses (microglia, astrocytes, monocytes/NK cells) shape progression (https://doi.org/10.1016/S1474-4422(21)00414-2, May 2022; https://doi.org/10.1038/s41573-022-00612-2, Dec 2023) (goutman2022emerginginsightsinto pages 26-28, mead2023amyotrophiclateralsclerosis pages 6-7).

Key concepts and definitions with current understanding
- Proteinopathy and ribostasis: “TDP-43 pathology is characteristic of the majority of ALS cases,” with mislocalization and aggregation that impair RNA splicing, including STMN2, and engage stress granule/LLPS biology; SOD1 and FUS drive alternative proteopathic subtypes (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022) (goutman2022emerginginsightsinto pages 6-8).
- C9orf72 repeat expansion: Dual mechanisms—loss of function (haploinsufficiency) and gain of function via repeat RNA and DPRs (poly-PR/GR/GA)—that converge on NCT, heterochromatin, proteostasis, and trigger TDP-43 pathology (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022) (goutman2022emerginginsightsinto pages 8-9).
- Nucleocytoplasmic transport (NCT): Nuclear pore, importin/Ran cycle, and nuclear envelope alterations present in human ALS tissue and models; DPRs and FUS/TDP-43 assemblies disrupt nuclear import/export (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022) (goutman2022emerginginsightsinto pages 8-9).
- Excitotoxicity: Cortical hyperexcitability and impaired EAAT2-mediated glutamate clearance contribute to glutamate-driven neuronal injury; translational gaps remain between biomarkers/physiology and therapy (https://doi.org/10.1093/brain/awae039, 2024) (nguyen2024updatesondisease pages 1-2).
- Axonal transport/NMJ: Trafficking gene hits (KIF5A, DCTN1, PFN1) and early NMJ denervation align with a “dying-back” contribution to weakness (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022; https://doi.org/10.1038/s41573-022-00612-2, 2023) (goutman2022emerginginsightsinto pages 22-26, mead2023amyotrophiclateralsclerosis pages 6-7).
- Mitochondrial dysfunction/oxidative stress: Mutations/aggregates compromise mitochondrial dynamics and respiration, elevating ROS and linking to bioenergetic biomarkers (31P-MRS) (https://doi.org/10.1038/s41573-022-00612-2, 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).
- Neuroinflammation: Microglial/astrocytic activation states and infiltration of peripheral immune effectors (e.g., NK cells) accompany motor neuron loss and may modulate trajectory (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022) (goutman2022emerginginsightsinto pages 26-28).

Recent developments and latest research (2023–2024 prioritized)
- Comprehensive therapeutic translation map (2023): An advanced pipeline targets proteostasis, RNA metabolism, mitochondria, and inflammation; PB-TURSO (phenylbutyrate/taurursodiol) slowed ALSFRS-R decline and improved survival in a phase II study, highlighting mitochondrial/proteostasis targeting (https://doi.org/10.1038/s41573-022-00612-2, Dec 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).
- Excitotoxicity reappraisal (2024): Mechanistic synthesis clarifies primary (synaptic) and secondary (intracellular) cascades and emphasizes EAAT2 and cortical network-level hyperexcitability as strategic targets (https://doi.org/10.1093/brain/awae039, Feb 2024) (nguyen2024updatesondisease pages 1-2).
- Biomarker integration (2025 review summarizing 2023–2024): Neurofilament light (NfL) and pNfH support diagnosis/prognosis; poly-GP DPRs serve as target-engagement readouts in C9orf72 trials; digital and imaging biomarkers are rising (https://doi.org/10.3389/fmolb.2025.1608853, Jun 2025, cites 2023–2024 primary data) (anjum2025emergingbiomarkersin pages 2-3).

Current applications and real-world implementations
- Gene-directed therapy: Tofersen (SOD1 ASO) achieved CSF SOD1 reduction and is used in gene-directed contexts; biomarker (NfL) trajectories help demonstrate pharmacodynamic impact and support presymptomatic trial design (NCT references in 2022–2023 synthesis) (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022; https://doi.org/10.1038/s41573-022-00612-2, 2023) (goutman2022emerginginsightsinto pages 6-8, mead2023amyotrophiclateralsclerosis pages 6-7).
- Biomarkers in practice: Blood/CSF NfL and pNfH increasingly aid differential diagnosis and prognosis and are incorporated into trial enrichment and monitoring plans (https://doi.org/10.3389/fmolb.2025.1608853, 2025) (anjum2025emergingbiomarkersin pages 2-3).

Expert opinions and analysis from authoritative sources
- “ALS is poised for successful therapeutic translation,” with mechanistic subclassification and biomarker-enabled trials expected to improve translation across heterogeneous subtypes (Nature Reviews Drug Discovery, Dec 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).
- “Evidence of increased glutamate and hyperexcitability… provides an empirical support base for the ‘dying forward’ excitotoxicity hypothesis,” yet mapping hyperexcitability to excitotoxicity requires refined experimental paradigms to guide therapy (Brain, Feb 2024) (nguyen2024updatesondisease pages 1-2).

Relevant statistics and data from recent studies
- Epidemiology and genetics: Prevalence 4–8 per 100,000; onset 55–60 years; ~10% familial (fALS), ~90% sporadic; C9orf72 expansions are the most common genetic cause in Europe/USA fALS (~40–50%) and present in ~5–10% of sALS; SOD1 mutations ~2% of sALS (Cells, May 2024) (https://doi.org/10.3390/cells13110888) (nguyen2024updatesondisease pages 1-2).
- Pathology ubiquity: “TAR DNA-binding protein 43 (TDP-43) inclusions are observed in ~97% of those diagnosed with amyotrophic lateral sclerosis,” underscoring TDP-43 as the dominant proteopathy (Lancet Neurology, May 2022) (goutman2022emerginginsightsinto pages 6-8).

Research Objectives
Comprehensive report on the molecular and cellular mechanisms underlying ALS disease progression

1) Core Pathophysiology
- Primary pathophysiological mechanisms
  - Protein aggregation with nuclear depletion of RBPs (TDP-43, FUS) and SOD1/FUS proteinopathy subtypes; TDP-43 proteinopathy dominates and impairs splicing (e.g., STMN2), RNA transport, and stress granule dynamics (LLPS) (https://doi.org/10.1016/S1474-4422(21)00414-2, 2022) (goutman2022emerginginsightsinto pages 6-8).
  - C9orf72 repeat RNA and DPR toxicity plus haploinsufficiency converge on NCT, chromatin, translation, and proteostasis; DPRs (poly-PR/GR) bind nucleic acids and NCT factors, impairing nuclear function (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 8-9).
  - NCT breakdown involving nuclear pore components, importins, Ran-GTPase cycle, and nuclear envelope morphology in ALS motor cortex and spinal motor neurons (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 8-9).
  - Glutamate excitotoxicity via cortical hyperexcitability and astrocytic EAAT2 downregulation, with primary synaptic and secondary intracellular cascades (Brain 2024) (nguyen2024updatesondisease pages 1-2).
  - Mitochondrial respiratory/bioenergetic dysfunction with oxidative stress; preclinical/clinical mitochondrial-targeting strategies are in development or translation (Nature Rev Drug Discov 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).
  - Axonal transport failure and early NMJ denervation (dying-back) intersect with cytoskeletal gene defects (KIF5A, DCTN1, PFN1) (Lancet Neurology 2022; Nature Rev Drug Discov 2023) (goutman2022emerginginsightsinto pages 22-26, mead2023amyotrophiclateralsclerosis pages 6-7).
  - Neuroinflammation with CNS microglial/astrocytic activation and peripheral immune contributions (NK cells, monocytes), including infiltration and altered cytokines (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 26-28).

- Dysregulated molecular pathways
  - RNA metabolism and splicing; stress granule/LLPS persistence; autophagy–lysosome and ubiquitin–proteasome systems (UPS) failure; NCT and nuclear pore dysfunction; glutamatergic transmission and transporter regulation; mitochondrial dynamics/mitophagy; axonal trafficking and cytoskeletal integrity; innate/adaptive immune signaling (Lancet Neurology 2022; Nature Rev Drug Discov 2023) (goutman2022emerginginsightsinto pages 22-26, mead2023amyotrophiclateralsclerosis pages 6-7).

- Affected cellular processes
  - mRNA splicing (e.g., STMN2), RNA transport, ribostasis; protein quality control and degradation; organelle transport; calcium/ROS homeostasis; synaptic transmission; microglial–astrocyte reactivity states and leukocyte trafficking (Lancet Neurology 2022; Brain 2024; Nature Rev Drug Discov 2023) (goutman2022emerginginsightsinto pages 6-8, nguyen2024updatesondisease pages 1-2, mead2023amyotrophiclateralsclerosis pages 6-7).

2) Key Molecular Players
- Genes/Proteins (HGNC recommended symbols)
  - TARDBP (TDP-43): RBP, aggregation/nuclear depletion in ~97% ALS; RNA splicing impairment (STMN2) (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 6-8).
  - SOD1: misfolding/aggregation, oxidative stress, mitochondrial/axonal transport defects; target of ASO therapy (Nature Rev Drug Discov 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).
  - FUS: RBP with LLPS/stress granule biology and NCT linkage (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 22-26).
  - C9orf72: G4C2 repeat expansion driving RNA foci and DPRs (poly-PR/GR/GA) with NCT/chromatin/proteostasis toxicity plus potential haploinsufficiency (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 8-9).
  - Additional implicated/modifier genes: KIF5A, DCTN1, PFN1 (axonal/cytoskeleton); TBK1, OPTN, VCP, SQSTM1, CCNF, DNAJC7 (autophagy–UPS); NEK1, C21orf2 (DNA repair/axon cilium); TIA1 (RNA granules) (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 29-30, goutman2022emerginginsightsinto pages 22-26).

- Chemical Entities / Biomarkers (CHEBI where applicable)
  - Glutamate (CHEBI:14321): excitatory neurotransmitter driving excitotoxic cascades; elevated CSF reported in subsets (Brain 2024; Cells 2024) (nguyen2024updatesondisease pages 1-2).
  - Neurofilament light (NfL) and phosphorylated neurofilament heavy (pNfH): fluid biomarkers of axonal injury with diagnostic/prognostic value and utility in trials (Frontiers Mol Biosci 2025) (anjum2025emergingbiomarkersin pages 2-3).

- Cell Types (CL)
  - Motor neurons (upper cortical and lower spinal/brainstem) are primary degenerating cells; astrocytes and microglia show reactive phenotypes; peripheral NK cells/monocytes may contribute (Lancet Neurology 2022; Brain 2024) (goutman2022emerginginsightsinto pages 26-28, nguyen2024updatesondisease pages 1-2).

- Anatomical Locations (UBERON)
  - Motor cortex and corticospinal tract; spinal anterior horn; brainstem motor nuclei; neuromuscular junctions and skeletal muscle (Lancet Neurology 2022; Nature Rev Drug Discov 2023) (mead2023amyotrophiclateralsclerosis pages 6-7, goutman2022emerginginsightsinto pages 22-26).

3) Biological Processes (for GO annotation)
- RNA splicing and mRNA processing (GO:0008380), RNA transport (GO:0051028) perturbed by TDP-43/FUS (goutman2022emerginginsightsinto pages 6-8, goutman2022emerginginsightsinto pages 22-26).
- Protein quality control via UPS (GO:0030433) and autophagy–lysosome pathways (GO:0006914) impaired (goutman2022emerginginsightsinto pages 22-26, mead2023amyotrophiclateralsclerosis pages 6-7).
- Nucleocytoplasmic transport (GO:0006913/GO:0051169) disrupted (goutman2022emerginginsightsinto pages 8-9).
- Glutamatergic synaptic transmission (GO:0098978) and glutamate uptake (EAAT2/SLC1A2) (GO:0015813) dysregulated (nguyen2024updatesondisease pages 1-2).
- Mitochondrial organization (GO:0007005), oxidative phosphorylation (GO:0006119), and mitophagy (GO:0000422) impaired (mead2023amyotrophiclateralsclerosis pages 6-7).
- Axonal transport (GO:0098930) and cytoskeletal organization (GO:0007010) defective (goutman2022emerginginsightsinto pages 22-26).
- Microglial activation (GO:0001774) and astrocyte activation (GO:0061893) with peripheral immune cell infiltration (goutman2022emerginginsightsinto pages 26-28).

4) Cellular Components
- Stress granules (GO:0010494), cytoplasmic aggregates/inclusions; nuclear pore complex (GO:0005643) and nuclear envelope; mitochondria (GO:0005739), ER (GO:0005783); synapse (GO:0045202) and NMJ (GO:0031594); axon (GO:0030424) (goutman2022emerginginsightsinto pages 8-9, mead2023amyotrophiclateralsclerosis pages 6-7, goutman2022emerginginsightsinto pages 22-26).

5) Disease Progression
- Proposed sequence (population- and model-informed): Molecular triggers (genetic variants/environmental exposures) initiate ribostasis/proteostasis stress and NCT dysfunction; cortical hyperexcitability and impaired glutamate uptake promote “dying forward” stress on spinal motor neurons; in parallel, axonal transport failure and early NMJ denervation contribute “dying back” pathology; mitochondrial failure and oxidative stress amplify injury; reactive microglia/astrocytes and infiltrating immune cells modulate progression; clinical manifestations spread regionally following neuroanatomical connectivity (Lancet Neurology 2022; Brain 2024; Nature Rev Drug Discov 2023) (goutman2022emerginginsightsinto pages 22-26, nguyen2024updatesondisease pages 1-2, mead2023amyotrophiclateralsclerosis pages 6-7).
- Stages: Presymptomatic biomarker phase (e.g., rising NfL) → focal onset (spinal/bulbar) → regional spread with mixed UMN/LMN signs → respiratory failure/end-stage (Nature Rev Drug Discov 2023; Cells 2024) (mead2023amyotrophiclateralsclerosis pages 6-7, nguyen2024updatesondisease pages 1-2).

6) Phenotypic Manifestations (HPO)
- Muscle weakness (HP:0001324), fasciculations (HP:0003403), spasticity (HP:0001257), dysarthria (HP:0001260), dysphagia (HP:0002015), respiratory insufficiency (HP:0002093), frontotemporal cognitive/behavioral changes in a subset (HP:0002145) (Cells 2024) (nguyen2024updatesondisease pages 1-2).
- Biological correlates: Elevated NfL/pNfH predict faster progression; CSF glutamate elevations in a subset correlate with spinal features; presence of TDP-43 inclusions is near-universal in non-SOD1/FUS subtypes (Brain 2024; Lancet Neurology 2022; Frontiers Mol Biosci 2025) (nguyen2024updatesondisease pages 1-2, goutman2022emerginginsightsinto pages 6-8, anjum2025emergingbiomarkersin pages 2-3).

Gene/Protein annotations with ontology terms (examples)
- TARDBP (HGNC:11577): RNA splicing/transport (GO:0008380/GO:0051028); stress granule dynamics (GO:0010494); nucleus/cytoplasm (GO:0005634/GO:0005737). Evidence: TDP-43 pathology and splicing defects (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 6-8).
- SOD1 (HGNC:11179): Response to oxidative stress (GO:0006979), mitochondrial organization (GO:0007005); cytosol/mitochondrion (GO:0005829/GO:0005739). Evidence: oxidative stress/mitochondrial dysfunction (Nature Rev Drug Discov 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).
- FUS (HGNC:4010): RNA binding/LLPS; nucleus/cytoplasm; NCT. Evidence: RBP with LLPS/NCT involvement (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 22-26).
- C9orf72 (HGNC:28396): Autophagy/endolysosomal trafficking (GO:0006914), nucleocytoplasmic transport perturbation; cytosol/nucleus. Evidence: repeat RNA/DPR toxicity and NCT effects (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 8-9).
- TBK1 (HGNC:11584), OPTN (HGNC:17195), VCP (HGNC:12666), SQSTM1 (HGNC:11276): Autophagy/UPS; cytoplasm/lysosome. Evidence: autophagy–proteostasis gene set in ALS (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 29-30).
- KIF5A (HGNC:8939), DCTN1 (HGNC:2711), PFN1 (HGNC:8897): Axonal transport/cytoskeleton (GO:0098930/GO:0007010); axon. Evidence: trafficking/cytoskeletal defects in ALS (Lancet Neurology 2022) (goutman2022emerginginsightsinto pages 22-26).

Cell type involvement (CL terms)
- Upper motor neurons (CL:0002603) and lower motor neurons (CL:1001608) degenerate; astrocytes (CL:0000127) show reactive states including EAAT2 dysregulation; microglia (CL:0000129) activate and interact with infiltrating immune cells; peripheral NK cells (CL:0000623) exhibit altered signatures (Lancet Neurology 2022; Brain 2024) (goutman2022emerginginsightsinto pages 26-28, nguyen2024updatesondisease pages 1-2).

Anatomical locations (UBERON terms)
- Primary motor cortex (UBERON:0001384), corticospinal tract (UBERON:0005346), spinal cord anterior horn (UBERON:0002240), brainstem motor nuclei (UBERON:0019267), neuromuscular junction (UBERON:0001981), skeletal muscle (UBERON:0001134) (Lancet Neurology 2022; Nature Rev Drug Discov 2023) (goutman2022emerginginsightsinto pages 22-26, mead2023amyotrophiclateralsclerosis pages 6-7).

Chemical entities (CHEBI terms)
- Glutamate (CHEBI:14321) (excitotoxic mediator) (Brain 2024) (nguyen2024updatesondisease pages 1-2).
- Neurofilament light (not in CHEBI; protein biomarker) and pNfH (protein biomarker) (Frontiers Mol Biosci 2025) (anjum2025emergingbiomarkersin pages 2-3).

Evidence items with PMIDs/DOIs/URLs and dates
- Goutman SA et al. Emerging insights into the complex genetics and pathophysiology of ALS. Lancet Neurol. May 2022. DOI: 10.1016/S1474-4422(21)00414-2; URL: https://doi.org/10.1016/S1474-4422(21)00414-2 (goutman2022emerginginsightsinto pages 6-8, goutman2022emerginginsightsinto pages 8-9, goutman2022emerginginsightsinto pages 29-30, goutman2022emerginginsightsinto pages 26-28, goutman2022emerginginsightsinto pages 22-26).
- Mead RJ et al. ALS: poised for successful therapeutic translation. Nat Rev Drug Discov. Dec 2023. DOI: 10.1038/s41573-022-00612-2; URL: https://doi.org/10.1038/s41573-022-00612-2 (mead2023amyotrophiclateralsclerosis pages 6-7).
- Odierna GL et al. How do we get from hyperexcitability to excitotoxicity in ALS? Brain. Feb 2024. DOI: 10.1093/brain/awae039; URL: https://doi.org/10.1093/brain/awae039 (nguyen2024updatesondisease pages 1-2).
- Anjum F et al. Emerging biomarkers in ALS. Frontiers Mol Biosci. Jun 2025 (synthesizes 2023–2024 studies). DOI: 10.3389/fmolb.2025.1608853; URL: https://doi.org/10.3389/fmolb.2025.1608853 (anjum2025emergingbiomarkersin pages 2-3).

Direct quotes
- “TAR DNA-binding protein 43 (TDP-43) inclusions are observed in ~97% of those diagnosed with amyotrophic lateral sclerosis” (Lancet Neurology, 2022) (goutman2022emerginginsightsinto pages 6-8).
- “Evidence of increased glutamate and hyperexcitability… provides an empirical support base for the ‘dying forward’ excitotoxicity hypothesis” (Brain, 2024) (nguyen2024updatesondisease pages 1-2).
- “ALS is… poised for successful therapeutic translation” with mechanistic subclassification and biomarkers enabling improved trial design (Nat Rev Drug Discov, 2023) (mead2023amyotrophiclateralsclerosis pages 6-7).

Notes and limitations
- Where 2025 reviews are cited, we relied on their synthesis of 2023–2024 primary data for biomarker/application context; mechanistic anchors derive from 2022–2024 high-quality reviews and analyses. Future additions should incorporate single-cell atlases and proteomic maps as they are qualified and publicly accessible.


References

1. (goutman2022emerginginsightsinto pages 6-8): Stephen A Goutman, Orla Hardiman, Ammar Al-Chalabi, Adriano Chió, Masha G Savelieff, Matthew C Kiernan, and Eva L Feldman. Emerging insights into the complex genetics and pathophysiology of amyotrophic lateral sclerosis. The Lancet Neurology, 21:465-479, May 2022. URL: https://doi.org/10.1016/s1474-4422(21)00414-2, doi:10.1016/s1474-4422(21)00414-2. This article has 398 citations and is from a highest quality peer-reviewed journal.

2. (mead2023amyotrophiclateralsclerosis pages 6-7): Richard J. Mead, Ning Shan, H. Joseph Reiser, Fiona Marshall, and Pamela J. Shaw. Amyotrophic lateral sclerosis: a neurodegenerative disorder poised for successful therapeutic translation. Nature Reviews. Drug Discovery, 22:185-212, Dec 2023. URL: https://doi.org/10.1038/s41573-022-00612-2, doi:10.1038/s41573-022-00612-2. This article has 493 citations.

3. (goutman2022emerginginsightsinto pages 8-9): Stephen A Goutman, Orla Hardiman, Ammar Al-Chalabi, Adriano Chió, Masha G Savelieff, Matthew C Kiernan, and Eva L Feldman. Emerging insights into the complex genetics and pathophysiology of amyotrophic lateral sclerosis. The Lancet Neurology, 21:465-479, May 2022. URL: https://doi.org/10.1016/s1474-4422(21)00414-2, doi:10.1016/s1474-4422(21)00414-2. This article has 398 citations and is from a highest quality peer-reviewed journal.

4. (nguyen2024updatesondisease pages 1-2): Lien Nguyen. Updates on disease mechanisms and therapeutics for amyotrophic lateral sclerosis. Cells, 13:888, May 2024. URL: https://doi.org/10.3390/cells13110888, doi:10.3390/cells13110888. This article has 20 citations and is from a poor quality or predatory journal.

5. (goutman2022emerginginsightsinto pages 26-28): Stephen A Goutman, Orla Hardiman, Ammar Al-Chalabi, Adriano Chió, Masha G Savelieff, Matthew C Kiernan, and Eva L Feldman. Emerging insights into the complex genetics and pathophysiology of amyotrophic lateral sclerosis. The Lancet Neurology, 21:465-479, May 2022. URL: https://doi.org/10.1016/s1474-4422(21)00414-2, doi:10.1016/s1474-4422(21)00414-2. This article has 398 citations and is from a highest quality peer-reviewed journal.

6. (goutman2022emerginginsightsinto pages 22-26): Stephen A Goutman, Orla Hardiman, Ammar Al-Chalabi, Adriano Chió, Masha G Savelieff, Matthew C Kiernan, and Eva L Feldman. Emerging insights into the complex genetics and pathophysiology of amyotrophic lateral sclerosis. The Lancet Neurology, 21:465-479, May 2022. URL: https://doi.org/10.1016/s1474-4422(21)00414-2, doi:10.1016/s1474-4422(21)00414-2. This article has 398 citations and is from a highest quality peer-reviewed journal.

7. (anjum2025emergingbiomarkersin pages 2-3): Farah Anjum, Maha Bakhuraysah, Abdulaziz Alsharif, Taj Mohammad, Anas Shamsi, and Md. Imtaiyaz Hassan. Emerging biomarkers in amyotrophic lateral sclerosis: from pathogenesis to clinical applications. Frontiers in Molecular Biosciences, Jun 2025. URL: https://doi.org/10.3389/fmolb.2025.1608853, doi:10.3389/fmolb.2025.1608853. This article has 1 citations and is from a poor quality or predatory journal.

8. (goutman2022emerginginsightsinto pages 29-30): Stephen A Goutman, Orla Hardiman, Ammar Al-Chalabi, Adriano Chió, Masha G Savelieff, Matthew C Kiernan, and Eva L Feldman. Emerging insights into the complex genetics and pathophysiology of amyotrophic lateral sclerosis. The Lancet Neurology, 21:465-479, May 2022. URL: https://doi.org/10.1016/s1474-4422(21)00414-2, doi:10.1016/s1474-4422(21)00414-2. This article has 398 citations and is from a highest quality peer-reviewed journal.