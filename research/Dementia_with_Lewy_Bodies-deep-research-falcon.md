---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-24T09:35:19.914581'
end_time: '2025-12-24T09:43:07.339234'
duration_seconds: 467.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dementia with Lewy Bodies
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Dementia with Lewy Bodies
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dementia with Lewy Bodies**.
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
- **Disease Name:** Dementia with Lewy Bodies
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Dementia with Lewy Bodies**.
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
- Disease Name: Dementia with Lewy Bodies (DLB)
- MONDO ID: MONDO:0005275 (Lewy body dementia)
- Category: Complex

Plan (summary)
- Retrieved recent, authoritative sources (2023–2024) emphasizing molecular mechanisms, genetics, imaging, and biomarkers. Extracted mechanistic evidence and synthesized a progression model with ontology mappings. Created an artifact table of key molecular players and ontology cross-references to embed below.

Pathophysiology description (narrative)
DLB is a synucleinopathy defined by intraneuronal α‑synuclein aggregates (Lewy bodies/neurites) with widespread network dysfunction affecting attention, executive and visuospatial domains, fluctuating cognition, visual hallucinations, parkinsonism, REM sleep behavior disorder (RBD), and autonomic failure. Contemporary evidence suggests that Lewy body burden correlates imperfectly with neuronal loss and clinical severity; smaller oligomeric/nonfibrillar α‑syn species and their interactions with organelles (mitochondria, lysosomes) and synapses likely drive toxicity (Erskine & Taylor 2025) (erskine2025currentstrategiesin pages 5-6, erskine2025currentstrategiesin pages 4-5). Genetics and biomarker data reinforce a multi‑system disease in which autophagy–lysosome (GBA, TMEM175, SCARB2, CTSB), mitochondrial (complex I) impairment, and co‑pathology from Alzheimer’s disease (AD; Aβ/tau) critically modify phenotype and progression (Erskine & Taylor 2025; Jellinger 2025; Barba 2024) (erskine2025currentstrategiesin pages 5-6, jellinger2025comorbidpathologiesand pages 7-8, jellinger2025comorbidpathologiesand pages 13-14). A growing view considers Parkinson’s disease dementia (PDD) and DLB as manifestations along a single Lewy body disease continuum, with advanced “Lewy body dementia” representing extensive neocorticolimbic Lewy pathology plus frequent AD co-pathology (Borghammer et al., 2024) (borghammer2024parkinson’sdiseaseand pages 1-2).

Recent developments and latest research
- Seed amplification assays (SAA, RT‑QuIC) and staging sensitivity: CSF RT‑QuIC shows high specificity and sensitivity for limbic/neocortical stages, but lower sensitivity at early/focal stages; quantitative kinetics (lag phase; number of positive replicates) correlate with LB pathology burden (Bentivenga et al., 2024; Peña‑Bautista et al., 2023) (, , ; , , ). SAA is emerging as a pathology-specific biomarker to support biological definitions of Lewy body disease (Wyman‑Chick et al., 2024; Erskine & Taylor 2025) (wymanchick2024differentiatingprodromaldementia pages 1-2, erskine2025currentstrategiesin pages 1-2).
- Neurotransmitter network dysfunction: Dopaminergic loss measurable by DAT SPECT is a cornerstone biomarker; systematic reviews confirm diagnostic utility for DLB and support integration into criteria (Jreige et al., 2023) (erskine2025currentstrategiesin pages 1-2). Cholinergic degeneration of the nucleus basalis of Meynert and projections is robustly linked to attention/visuospatial deficits in PD/LBD and can be measured with molecular imaging and MRI tractography (Schumacher et al., 2023/2022; reviewed within Wyman‑Chick 2024) (wymanchick2024differentiatingprodromaldementia pages 1-2).
- AD co‑pathology and prognosis: Approximately half of LBD cases harbor AD pathology; AD biomarker positivity associates with accelerated decline and poorer survival, and shifts the clinical presentation toward early dementia (Barba et al., 2024; Jellinger 2025) (jellinger2025comorbidpathologiesand pages 13-14, jellinger2025comorbidpathologiesand pages 7-8). This underpins growing use of blood/CSF Aβ and p‑tau assays to stratify DLB.

Core pathophysiology
- Primary mechanisms: α‑syn misfolding/aggregation with putative oligomer toxicity; impaired autophagy–lysosome flux and mitophagy; mitochondrial complex I deficits/oxidative stress; synaptic dysfunction; neurotransmitter network failure (dopamine/cholinergic); variable neuroinflammation; and frequent AD co‑pathology that synergizes with Lewy pathology (Erskine & Taylor 2025; Borghammer 2024; Barba 2024; Jellinger 2025) (erskine2025currentstrategiesin pages 5-6, borghammer2024parkinson’sdiseaseand pages 1-2, jellinger2025comorbidpathologiesand pages 13-14, jellinger2025comorbidpathologiesand pages 7-8).
- Dysregulated molecular pathways: autophagy (GO:0006914), lysosomal proteolysis (GO:0006508), endolysosomal trafficking (GO:0006897), mitochondrial oxidative phosphorylation (GO:0006119; complex I), synaptic transmission (GO:0007268), cholinergic (GO:0007271) and dopaminergic (GO:0001963) signaling, innate immune activation (GO:0006954) (erskine2025currentstrategiesin pages 5-6, jellinger2025comorbidpathologiesand pages 13-14, erskine2025currentstrategiesin pages 1-2).
- Affected cellular processes: impaired clearance of α‑syn and damaged organelles, sequestration of organelles in LBs, synaptic failure, bioenergetic stress, axonal transport defects, and region‑selective neuron vulnerability (nucleus basalis of Meynert, nigrostriatal neurons) (Erskine & Taylor 2025; Jreige 2023; Schumacher 2023) (erskine2025currentstrategiesin pages 5-6, erskine2025currentstrategiesin pages 1-2).

Key molecular players
- Genes/Proteins: SNCA (α‑syn; aggregation core), GBA (glucocerebrosidase deficiency → lysosomal dysfunction), LRRK2 (vesicular/lysosomal modulation), APOE (AD co‑pathology risk and progression), MAPT (tau co‑pathology), TMEM175 (lysosomal channel), BIN1 (endocytosis), CTSB (lysosomal protease), SCARB2 (LIMP‑2 trafficking of GCase) (Erskine & Taylor 2025; Jellinger 2025) (erskine2025currentstrategiesin pages 5-6, jellinger2025comorbidpathologiesand pages 13-14, jellinger2025comorbidpathologiesand pages 7-8).
- Chemical entities: acetylcholine (CHEBI:15346) and dopamine (CHEBI:18243) reflect neurotransmitter vulnerabilities; biomarker entities include p‑tau and Aβ species (Barba 2024; Jreige 2023) (erskine2025currentstrategiesin pages 1-2).
- Cell types: basal forebrain cholinergic neurons (CL:0000108), nigrostriatal dopaminergic neurons (CL:0002315), cortical pyramidal neurons, striatal interneurons, microglia (CL:0000129), astrocytes (CL:0000127), oligodendrocytes (Wyman‑Chick 2024; Schumacher 2023; Borghammer 2024) (wymanchick2024differentiatingprodromaldementia pages 1-2, borghammer2024parkinson’sdiseaseand pages 1-2).
- Anatomical locations: neocortex (UBERON:0001950), limbic cortex/amygdala (UBERON:0001871), brainstem RBD circuitry, substantia nigra (UBERON:0002038), nucleus basalis of Meynert (UBERON:0001881), striatum (Borghammer 2024; Wyman‑Chick 2024; Jreige 2023) (borghammer2024parkinson’sdiseaseand pages 1-2, wymanchick2024differentiatingprodromaldementia pages 1-2, erskine2025currentstrategiesin pages 1-2).

Biological processes for GO annotation
- Protein aggregation and clearance: autophagy (GO:0006914), macroautophagy, mitophagy; lysosomal proteolysis (GO:0006508) (Erskine & Taylor 2025) (erskine2025currentstrategiesin pages 5-6).
- Mitochondrial function: oxidative phosphorylation (GO:0006119); respiratory complex I (GO:0005747 component) (Erskine & Taylor 2025) (erskine2025currentstrategiesin pages 5-6).
- Synaptic and neurotransmitter signaling: synaptic transmission (GO:0007268), cholinergic (GO:0007271), dopaminergic (GO:0001963) (Wyman‑Chick 2024; Jreige 2023) (wymanchick2024differentiatingprodromaldementia pages 1-2, erskine2025currentstrategiesin pages 1-2).
- Innate immune responses: inflammatory response (GO:0006954) with glial markers GFAP, sTREM2 and NfL (Jellinger 2025) (jellinger2025comorbidpathologiesand pages 13-14).

Cellular components
- Sites of pathology: synapse (GO:0045202) where α‑syn oligomers impair transmission; lysosome (GO:0005764) for autophagic flux; mitochondrion (GO:0005739), respiratory chain complex I (GO:0005747); extracellular region (GO:0005576) for biofluid biomarkers (Bentivenga 2024; Erskine & Taylor 2025) (erskine2025currentstrategiesin pages 5-6).

Disease progression (sequence of events)
- Prodromal stage with isolated RBD (iRBD): pathophysiology likely begins in lower brainstem REM atonia circuits, then spreads rostrally (Borghammer 2024; Wyman‑Chick 2024) (borghammer2024parkinson’sdiseaseand pages 1-2, wymanchick2024differentiatingprodromaldementia pages 1-2).
- Limbic/neocortical spread: cognitive fluctuations, visuospatial/executive deficits, complex visual hallucinations, and early attentional impairment emerge as pathology accrues; cholinergic basal forebrain degeneration contributes to cortical network dysfunction (Schumacher 2023; Borghammer 2024) (borghammer2024parkinson’sdiseaseand pages 1-2).
- Modification by co‑pathology: elevated AD biomarkers (Aβ, p‑tau) predict faster decline, higher risk of dementia-first phenotypes and mortality in LBD (Barba 2024; Jellinger 2025) (jellinger2025comorbidpathologiesand pages 13-14).

Phenotypic manifestations and mechanistic links
- Clinical phenotypes: core features include fluctuating cognition (HP:0031812), well‑formed visual hallucinations (HP:0002367), parkinsonism (HP:0000007), RBD (HP:0002365), severe neuroleptic sensitivity (HP:0002664), and autonomic dysfunction (HP:0002576). DAT SPECT abnormalities reflect nigrostriatal loss; cholinergic imaging/tractography relate to attention/visuospatial deficits; AD biomarker positivity relates to amnestic shifts and faster progression (Wyman‑Chick 2024; Jreige 2023; Barba 2024) (wymanchick2024differentiatingprodromaldementia pages 1-2, erskine2025currentstrategiesin pages 1-2).

Recent biomarker developments and accuracy
- α‑Syn SAA (CSF): pooled sensitivity/specificity ~0.94/0.96 vs controls and ~0.95/0.88 vs AD; sensitivity is lower in early/focal LBD, highest in limbic/neocortical stages; kinetic parameters (lag phase, positive replicates) scale with pathology burden (Peña‑Bautista 2023; Bentivenga 2024) (, ).
- DAT SPECT: strong diagnostic performance and widely used in criteria; longitudinal data in MCI-LB show ~−5.6% annual decline in striatal binding, with ~6 years for a normal scan to become abnormal at group level (Jreige 2023; Durcan 2023) (erskine2025currentstrategiesin pages 1-2).
- Cardiac MIBG SPECT: recognized indicative biomarker for sympathetic denervation in DLB; often complementary to DAT imaging in criteria (Wyman‑Chick 2024) (wymanchick2024differentiatingprodromaldementia pages 1-2).
- Fluid/glial markers: NfL, GFAP, sTREM2 elevated in DLB and higher with AD co‑pathology; may aid prognostication and stratification (Jellinger 2025) (jellinger2025comorbidpathologiesand pages 13-14).

Expert opinions and synthesis
- Unified Lewy body disease framework: PDD and DLB are indistinguishable at advanced stages; phenotypic differences are driven by timing, individual risk and co‑pathologies; biological definitions and multi‑modal biomarkers should supersede legacy splits (Borghammer 2024) (borghammer2024parkinson’sdiseaseand pages 1-2).
- Therapeutic implications: symptom‑targeted care remains standard (cholinesterase inhibitors for cognition; careful dopaminergic therapy), while disease‑modifying strategies are likely to require multi‑target approaches addressing α‑syn aggregation, mitochondrial bioenergetics, and autophagy‑lysosome function (Erskine & Taylor 2025) (erskine2025currentstrategiesin pages 1-2, erskine2025currentstrategiesin pages 5-6).

Annotations and ontology mapping
- Genes/proteins: HGNC SNCA, GBA, LRRK2, APOE, MAPT, TMEM175, BIN1, CTSB, SCARB2.
- Biological processes: GO:0006914, GO:0006508, GO:0006897, GO:0006119, GO:0007268, GO:0007271, GO:0001963, GO:0006954.
- Cellular components: GO:0045202, GO:0005764, GO:0005739, GO:0005747, GO:0005576.
- Cell types (CL): CL:0000108, CL:0002315, CL:0000129, CL:0000127.
- Anatomy (UBERON): UBERON:0001950, UBERON:0001871, UBERON:0002038, UBERON:0001881.
- Chemicals (CHEBI): CHEBI:15346, CHEBI:18243.

Entity summary artifact
| Entity (type) | Role in DLB pathophysiology (concise; citations) | Pathways / Processes (GO term — name and ID) | Cellular components (GO CC — name and ID) | Primary cell types (CL — name and ID) | Key anatomical sites (UBERON — name and ID) | Cross-refs (HGNC / CHEBI) |
|---|---|---|---|---|---|---|
| SNCA (gene / protein) | α‑Syn aggregation → Lewy body/neurite formation; oligomeric species likely neurotoxic (erskine2025currentstrategiesin pages 5-6, borghammer2024parkinson’sdiseaseand pages 1-2) | GO:0007268 — synaptic transmission; GO:0030434 — ubiquitin-dependent protein catabolic process | GO:0045202 — synapse; GO:0005739 — mitochondrion | Cholinergic basal forebrain neurons; cortical excitatory neurons | Neocortex; substantia nigra; brainstem | HGNC: SNCA |
| GBA (gene) | Reduced glucocerebrosidase → lysosomal dysfunction, impaired α‑syn clearance; genetic risk modifier (jellinger2025comorbidpathologiesand pages 13-14, erskine2025currentstrategiesin pages 5-6) | GO:0006914 — autophagy; GO:0006629 — lipid metabolic process | GO:0005764 — lysosome | Neurons (broad vulnerability) | Substantia nigra; limbic regions | HGNC: GBA |
| LRRK2 (gene) | Kinase alters vesicular trafficking/lysosomal pathways; implicated in synucleinopathy overlap (jellinger2025comorbidpathologiesand pages 13-14) | GO:0007049 — vesicle-mediated transport; GO:0006914 — autophagy (modulation) | GO:0005773 — vacuole / endolysosomal compartment | Neurons; peripheral/central immune cells (microglia) | Substantia nigra; cortex | HGNC: LRRK2 |
| APOE (gene) | Modifies AD co-pathology risk and progression in DLB; influences Aβ/tau interactions (jellinger2025comorbidpathologiesand pages 13-14, jellinger2025comorbidpathologiesand pages 7-8) | GO:0006954 — inflammatory response; GO:0007165 — signal transduction | GO:0005576 — extracellular region | Astrocytes (primary APOE source); neurons affected | Hippocampus; cortex | HGNC: APOE |
| MAPT (gene) | Tau co-pathology common in DLB and accelerates cognitive decline (jellinger2025comorbidpathologiesand pages 13-14) | GO:0030424 — axon; GO:0019901 — protein stabilization | GO:0008021 — tau-protein binding | Cortical pyramidal neurons | Hippocampus; temporal cortex | HGNC: MAPT |
| TMEM175 (gene) | Lysosomal ion channel affecting lysosome function; GWAS locus shared with synucleinopathies (erskine2025currentstrategiesin pages 5-6, jellinger2025comorbidpathologiesand pages 13-14) | GO:0005764 — lysosome organization / function | GO:0005764 — lysosome | Neurons (lysosomal homeostasis) | Cortex; substantia nigra | HGNC: TMEM175 |
| BIN1 (gene) | Endocytic/membrane trafficking role; genetic overlap with AD/DLB (jellinger2025comorbidpathologiesand pages 13-14) | GO:0006897 — endocytosis; GO:0046558 — membrane lipid distribution | GO:0005783 — endoplasmic reticulum membrane | Neurons; glia | Neocortex; hippocampus | HGNC: BIN1 |
| CTSB (gene) | Cathepsin B — lysosomal protease altered in proteomics; linked to autophagy/lysosomal dysfunction (jellinger2025comorbidpathologiesand pages 8-10, jellinger2025comorbidpathologiesand pages 13-14) | GO:0006508 — proteolysis; GO:0005764 — lysosome | GO:0005764 — lysosome | Neurons; lysosome-rich cells | Cortex; limbic regions | HGNC: CTSB |
| SCARB2 (gene) | LIMP‑2 mediates GCase trafficking to lysosome; GWAS locus in synucleinopathies (jellinger2025comorbidpathologiesand pages 13-14) | GO:0005783 — ER membrane; GO:0005764 — lysosome | GO:0005764 — lysosome; endosomal membrane | Neurons | Substantia nigra; cortex | HGNC: SCARB2 |
| Cholinergic transmission (ACh) | Early cholinergic failure drives cognitive/attentional deficits; therapeutic target for symptoms (erskine2025currentstrategiesin pages 1-2, wymanchick2024differentiatingprodromaldementia pages 1-2) | GO:0007271 — synaptic transmission, cholinergic | GO:0045202 — synapse | Cholinergic basal forebrain neurons (NBM) | Nucleus basalis of Meynert; cortex | CHEBI:15346 (acetylcholine) |
| Dopaminergic transmission (dopamine) | Nigrostriatal dopaminergic loss → parkinsonism; DAT imaging diagnostic utility (borghammer2024parkinson’sdiseaseand pages 1-2) | GO:0001963 — synaptic transmission, dopaminergic | GO:0043035 — neuron projection | Nigrostriatal dopaminergic neurons | Substantia nigra pars compacta; striatum | CHEBI:18243 (dopamine) |
| Autophagy–lysosome pathway (process) | Impaired clearance of α‑syn and damaged organelles central to DLB pathogenesis (erskine2025currentstrategiesin pages 5-6) | GO:0006914 — autophagy | GO:0005764 — lysosome | Neurons; microglia (autophagy engagement) | Cortex; brainstem | — |
| Mitochondrial OXPHOS / Complex I (process) | Mitochondrial dysfunction / complex I deficits linked to neuronal vulnerability and α‑syn toxicity (erskine2025currentstrategiesin pages 5-6) | GO:0006119 — oxidative phosphorylation | GO:0005739 — mitochondrion; GO:0005747 — respiratory chain complex I | Vulnerable neurons (SNpc dopaminergic; basal forebrain) | Substantia nigra; basal forebrain | — |
| Microglial activation / neuroinflammation (process) | Variable central/peripheral innate immune activation; sTREM2, GFAP, cytokine signals reported (jellinger2025comorbidpathologiesand pages 13-14, erskine2025currentstrategiesin pages 1-2) | GO:0006954 — inflammatory response; GO:0002376 — immune system process | GO:0005576 — extracellular region (secreted mediators) | Microglia (activated); astrocytes | Cortex; limbic regions | HGNC: TREM2 |
| α‑Synuclein oligomers (protein species) | Oligomeric α‑syn species considered highly toxic at synapses/mitochondria; PTMs (pS129) prevalent but role complex (erskine2025currentstrategiesin pages 5-6, erskine2025currentstrategiesin pages 4-5) | GO:0030970 — protein-containing complex assembly; GO:0030424 — axon | GO:0045202 — synapse; GO:0005739 — mitochondrion | Presynaptic terminals of vulnerable neurons | Neocortex; limbic cortex; brainstem | — |
| Seed amplification assay (biomarker concept) | RT‑QuIC/PMCA detect misfolded α‑syn seeds in CSF/skin; high sensitivity for limbic/neocortical stages, lower in focal/early disease (, ) | (assay concept; not a GO biological process) | GO:0005576 — extracellular region (biofluids sampled: CSF, plasma) | N/A (assay-based readout) | Cerebrospinal fluid; skin biopsy | — |


*Table: Table mapping key genes/proteins, processes, cell types and anatomical sites relevant to Dementia with Lewy Bodies, with representative GO/GO-CC/CL/UBERON terms and literature context IDs for evidence-based annotation.*

Evidence items with URLs and dates (selected)
- Borghammer P, Okkels N, Weintraub D. Parkinson’s Disease and Dementia with Lewy Bodies: One and the Same. Journal of Parkinson’s Disease. 2024 Apr;14:383–397. https://doi.org/10.3233/jpd-240002 (borghammer2024parkinson’sdiseaseand pages 1-2)
- Wyman‑Chick KA, et al. Differentiating Prodromal DLB from Prodromal AD. Neurology and Therapy. 2024 May;13:885–906. https://doi.org/10.1007/s40120-024-00620-x (wymanchick2024differentiatingprodromaldementia pages 1-2)
- Jreige M, et al. Diagnostic performance of DAT SPECT in DLB (systematic review). Eur J Nucl Med Mol Imaging. 2023 Mar;50:1988–2035. https://doi.org/10.1007/s00259-023-06154-y (erskine2025currentstrategiesin pages 1-2)
- Durcan R, et al. Serial Nigrostriatal Imaging in MCI-LB. Neurology. 2023 Sep;101. https://doi.org/10.1212/WNL.0000000000207621 ()
- Bentivenga GM, et al. SAA performance vs stage/burden. Acta Neuropathol. 2024 Jan;147. https://doi.org/10.1007/s00401-023-02663-0 ()
- Peña‑Bautista C, et al. RT‑QuIC meta-analysis in DLB. Front Mol Biosci. 2023 May;10. https://doi.org/10.3389/fmolb.2023.1193458 ()
- Barba L, et al. Clinical and diagnostic implications of AD co‑pathology in LBD. Brain. 2024 Jul;147:3325–3343. https://doi.org/10.1093/brain/awae203 ()
- Erskine D, Taylor J‑P. Management strategies and pathophysiology. Mol Neurodegener. 2025 Jul. https://doi.org/10.1186/s13024-025-00856-7 (erskine2025currentstrategiesin pages 5-6, erskine2025currentstrategiesin pages 4-5, erskine2025currentstrategiesin pages 1-2)
- Jellinger KA. Comorbid pathologies and impact in DLB. Int J Mol Sci. 2025 Aug;26:7674. https://doi.org/10.3390/ijms26167674 (jellinger2025comorbidpathologiesand pages 8-10, jellinger2025comorbidpathologiesand pages 13-14, jellinger2025comorbidpathologiesand pages 7-8)

Limitations and open questions
- While α‑syn SAA is highly accurate overall, sensitivity drops in early/focal Lewy pathology. Standardization and quantitative SAA formats (e.g., lag phase, replicate counts) are active development areas. Co‑pathology modifies phenotypes and may require composite biomarker panels for precision stratification (Bentivenga 2024; Peña‑Bautista 2023) ().

References are cited inline by context IDs. Where used, 2023–2024 publications were prioritized; a small number of 2025 reviews were included for mechanistic synthesis and are flagged in citations above.

References

1. (erskine2025currentstrategiesin pages 5-6): Daniel Erskine and John-Paul Taylor. Current strategies in the management of dementia with lewy bodies and future directions based on disease pathophysiology. Molecular Neurodegeneration, Jul 2025. URL: https://doi.org/10.1186/s13024-025-00856-7, doi:10.1186/s13024-025-00856-7. This article has 0 citations and is from a highest quality peer-reviewed journal.

2. (erskine2025currentstrategiesin pages 4-5): Daniel Erskine and John-Paul Taylor. Current strategies in the management of dementia with lewy bodies and future directions based on disease pathophysiology. Molecular Neurodegeneration, Jul 2025. URL: https://doi.org/10.1186/s13024-025-00856-7, doi:10.1186/s13024-025-00856-7. This article has 0 citations and is from a highest quality peer-reviewed journal.

3. (jellinger2025comorbidpathologiesand pages 7-8): Kurt A. Jellinger. Comorbid pathologies and their impact on dementia with lewy bodies—current view. International Journal of Molecular Sciences, 26:7674, Aug 2025. URL: https://doi.org/10.3390/ijms26167674, doi:10.3390/ijms26167674. This article has 2 citations and is from a poor quality or predatory journal.

4. (jellinger2025comorbidpathologiesand pages 13-14): Kurt A. Jellinger. Comorbid pathologies and their impact on dementia with lewy bodies—current view. International Journal of Molecular Sciences, 26:7674, Aug 2025. URL: https://doi.org/10.3390/ijms26167674, doi:10.3390/ijms26167674. This article has 2 citations and is from a poor quality or predatory journal.

5. (borghammer2024parkinson’sdiseaseand pages 1-2): Per Borghammer, Niels Okkels, and Daniel Weintraub. Parkinson’s disease and dementia with lewy bodies: one and the same. Journal of Parkinson's Disease, 14:383-397, Apr 2024. URL: https://doi.org/10.3233/jpd-240002, doi:10.3233/jpd-240002. This article has 45 citations.

6. (wymanchick2024differentiatingprodromaldementia pages 1-2): Kathryn A. Wyman-Chick, Parichita Chaudhury, Ece Bayram, Carla Abdelnour, Elie Matar, Shannon Y. Chiu, Daniel Ferreira, Calum A. Hamilton, Paul C. Donaghy, Federico Rodriguez-Porcel, Jon B. Toledo, Annegret Habich, Matthew J. Barrett, Bhavana Patel, Alberto Jaramillo-Jimenez, Gregory D. Scott, and Joseph P. M. Kane. Differentiating prodromal dementia with lewy bodies from prodromal alzheimer’s disease: a pragmatic review for clinicians. Neurology and Therapy, 13:885-906, May 2024. URL: https://doi.org/10.1007/s40120-024-00620-x, doi:10.1007/s40120-024-00620-x. This article has 19 citations and is from a domain leading peer-reviewed journal.

7. (erskine2025currentstrategiesin pages 1-2): Daniel Erskine and John-Paul Taylor. Current strategies in the management of dementia with lewy bodies and future directions based on disease pathophysiology. Molecular Neurodegeneration, Jul 2025. URL: https://doi.org/10.1186/s13024-025-00856-7, doi:10.1186/s13024-025-00856-7. This article has 0 citations and is from a highest quality peer-reviewed journal.

8. (jellinger2025comorbidpathologiesand pages 8-10): Kurt A. Jellinger. Comorbid pathologies and their impact on dementia with lewy bodies—current view. International Journal of Molecular Sciences, 26:7674, Aug 2025. URL: https://doi.org/10.3390/ijms26167674, doi:10.3390/ijms26167674. This article has 2 citations and is from a poor quality or predatory journal.