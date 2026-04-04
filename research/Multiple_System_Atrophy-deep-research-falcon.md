---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-13T09:34:36.975324'
end_time: '2026-03-13T09:46:15.288463'
duration_seconds: 698.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple System Atrophy
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
- **Disease Name:** Multiple System Atrophy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple System Atrophy**.
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
- **Disease Name:** Multiple System Atrophy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple System Atrophy**.
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


# Multiple System Atrophy (MSA) Pathophysiology—Molecular and Cellular Mechanisms (Knowledge-Base–Ready Research Report)

**Target disease:** Multiple system atrophy (MSA)  
**Disease IDs (available in retrieved sources):** Open Targets disease label corresponds to **“multiple system atrophy”** (EFO_1001050) (not an ontology lookup step; provided by retrieved data source). A MONDO identifier for MSA was not retrieved in the provided evidence set.

## Executive summary (current understanding)
MSA is a rapidly progressive, uniformly fatal **α-synucleinopathy** whose **pathognomonic** lesion is the **glial cytoplasmic inclusion (GCI)**—intracytoplasmic, phosphorylated α-synuclein aggregates within **oligodendrocytes**—with secondary neuronal degeneration in striatonigral and olivopontocerebellar systems. (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2, nishimura2023earlyandextensive pages 1-2)

Convergent evidence supports a multi-hit disease model where (i) **misfolded/aggregated α-synuclein** (including strain-like conformers) accumulates in oligodendroglia, (ii) **myelin–axon unit failure** emerges early (e.g., selective MAG loss; paranodal disruption; connexin/gap-junction alterations), (iii) early **innate and adaptive neuroinflammation** accompanies pathology, and (iv) downstream **proteostasis/autophagy–lysosome dysfunction** and **mitochondrial bioenergetic/oxidative stress** contribute to propagation and cell death. (torremuruzabal2023hostoligodendrogliopathyand pages 1-3, nishimura2023earlyandextensive pages 1-2, boing2024distinctultrastructuralphenotypes pages 10-11, compagnoni2019understandingthepathogenesis pages 4-6)

---

## 1) Key concepts and definitions

### Clinical-pathologic definition
MSA is clinically characterized by **parkinsonism with poor L-DOPA responsiveness**, **cerebellar ataxia**, and **severe autonomic dysfunction**, typically with onset around the 6th decade and average disease duration ~7–9 years in reviews focusing on early-stage disease biology. (tanaka2025pathologicalandmolecular pages 1-2)

MSA is commonly partitioned into **MSA-P** (parkinsonian/striatonigral predominant) and **MSA-C** (cerebellar/olivopontocerebellar predominant); epidemiologically, MSA-C is reported more frequently in Asian populations (e.g., 67–84%), whereas MSA-P is more common in Western cohorts (e.g., 70–80%). (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2)

### Pathognomonic lesion: glial cytoplasmic inclusion (GCI)
GCIs are **oligodendroglial cytoplasmic** inclusions enriched in pathological **α-synuclein** (often detected as phosphorylated α-synuclein), and are required for neuropathologically established diagnosis. (nishimura2023earlyandextensive pages 1-2, federoff2015multiplesystematrophy pages 3-4)

### “Oligodendrogliopathy” framing
Modern conceptualization emphasizes MSA as a primary **oligodendroglial disease** (oligodendrogliopathy) with downstream neuronal degeneration, rather than a purely neuronal synucleinopathy. (hsiao2023roleofoligodendrocyte pages 2-4, federoff2015multiplesystematrophy pages 3-4)

### α-Synuclein strain biology and prion-like propagation
Experimental work indicates α-synuclein can form conformationally distinct “**strains**” with different cell tropism and pathogenic outcomes; prion-like behavior is invoked to explain templated conversion and spreading along networks/cell-to-cell transfer, though precise initiating triggers remain unsettled. (torremuruzabal2023hostoligodendrogliopathyand pages 1-3, sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2)

---

## 2) Core pathophysiology: primary mechanisms, pathways, and cellular processes

### 2.1 α-Synuclein aggregation in oligodendrocytes (GCIs): origins and propagation
**Core problem:** GCIs are abundant in oligodendrocytes even though oligodendrocyte α-synuclein expression is debated; thus, both **cell-autonomous** and **cell non-autonomous** models (neuron → oligodendrocyte transfer) are actively studied. (tanaka2025pathologicalandmolecular pages 2-5, nuccio2023oligodendrocytespruneaxons pages 1-2)

**Neuron-to-oligodendrocyte transfer via axonal pruning/engulfment (2023 primary study):** In a mouse model seeded with a synthetic human α-syn fibril strain (“1B”), pathology first appeared as **axonal Lewy neurites**, followed months later by **fragmentation/pruning** and **engulfment of diseased axonal segments by oligodendrocytes**, forming GCI-like inclusions. This supports a mechanistic route whereby oligodendrocytes acquire aggregated α-syn from neurons/axons. (nuccio2023oligodendrocytespruneaxons pages 1-2)

**Strain–host interactions drive severity (2023 Brain primary study):** Injection of distinct recombinant α-syn strains (“fibrils” vs “ribbons”) into an MSA transgenic model produced **strain-dependent** oligodendroglial inclusion structure, neurodegeneration/brain atrophy, and immune activation patterns, supporting a model where MSA phenotype depends on both **α-syn conformer** and **host environment**. (torremuruzabal2023hostoligodendrogliopathyand pages 1-3)

### 2.2 Oligodendrocyte and myelin dysfunction (early demyelination; gap junctions; paranodes)
A neuropathology study of **15 autopsied MSA cases** staged cerebellar afferent fiber demyelination (Stage I–III) and found evidence for **early distal oligodendrogliopathy-type demyelination**, with **MAG** reduced already at Stage I while **MOG** reduction began later (Stage II–III). (nishimura2023earlyandextensive pages 1-2, nishimura2023earlyandextensive pages 6-8)

**Connexin/gap junction disruption:** Oligodendrocytic **Cx32** was “nearly absent” from myelin early (Stage I), redistributed into oligodendrocyte cytoplasm, and **co-localized with p-αSyn-positive GCIs**, implying co-aggregation and early loss of glial coupling. **Cx47** decreased in a stage-dependent manner but did not show the same cytoplasmic co-localization pattern. Astrocytic **Cx43** was downregulated early and later upregulated with astrogliosis, and **Cx43/Cx47** heterotypic gap junctions declined across stages. (nishimura2023earlyandextensive pages 6-8)

**Nodal/paranodal disruption:** Paranodal proteins (e.g., neurofascin, claudin-11/OSP, Caspr1) decreased from early-stage lesions and worsened with stage, consistent with progressive impairment of saltatory conduction architecture in affected tracts. (nishimura2023earlyandextensive pages 6-8)

**Visual evidence:** Staging, MAG/MOG changes, p-αSyn+ oligodendrocytes, and connexin redistribution/co-localization are shown in extracted figure panels from Nishimura et al. (nishimura2023earlyandextensive media b572b16d, nishimura2023earlyandextensive media aa3bf217).

### 2.3 Neuroinflammation and immune involvement (microglia; macrophages; T cells)
In the same staged neuropathology series, **CD68+ microglia/macrophage infiltration** and **scattered CD3+ T cells** were more prominent in **early-stage lesions (Stage I)** than later stages; CD4 and CD8 cells were both present, and B cells (CD20) were not observed. (nishimura2023earlyandextensive pages 6-8)

Strain-dependent models further show that immune activation (microglial/astroglial responses, recruitment of central and peripheral immune cells) accompanies neurodegeneration and varies with α-syn strain structural properties. (torremuruzabal2023hostoligodendrogliopathyand pages 1-3)

### 2.4 Proteostasis and autophagy–lysosome/peroxisome involvement (2024 EM evidence)
Correlative light/electron microscopy in post-mortem MSA brain demonstrated that **GCIs** are strongly associated with autophagy-related organelles: across **>100 GCIs**, “almost all” contained **lysosomes** and multivesicular bodies; vesicles co-localizing with α-syn pathology were confirmed as **lysosomes and peroxisomes**, supporting a role for **autophagy–lysosomal pathway perturbation** in GCI biology. (boing2024distinctultrastructuralphenotypes pages 10-11)

This aligns with broader mechanistic framing that impaired protein clearance (autophagy and proteasomal systems) contributes to α-syn accumulation and toxicity in MSA/PD. (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2)

### 2.5 Mitochondrial dysfunction and oxidative stress (CoQ10/COQ2 axis)
Multiple lines of evidence implicate mitochondrial bioenergetics and oxidative stress as contributors:

* **CoQ10 reduction in MSA and COQ2 biology:** COQ2 encodes an enzyme in CoQ10 biosynthesis; post-mortem measurements reported CoQ10 reductions selectively in cerebellum and patient-derived COQ2-mutant cells showed oxidative stress and apoptosis that could be partially rescued by CoQ10 supplementation in mechanistic summaries. (compagnoni2019understandingthepathogenesis pages 4-6)
* **Plasma CoQ10 is lower in MSA (quantitative):** In a case-control study (44 MSA vs 39 controls), mean plasma CoQ10 was **0.51 ± 0.22 μg/mL** in MSA vs **0.72 ± 0.42 μg/mL** in controls (P=0.01; association remained significant after adjustment). (mitsui2016plasmacoenzymeq10 pages 1-2)
* **ATP reductions in affected brain regions and CoQ biosynthesis gene expression:** In frozen tissues (8 MSA, 10 controls), ATP was significantly decreased in cerebellum and motor cortex white matter, with reduced **COQ2** and **COQ7** mRNA in disease-affected regions and correlations between COQ2/COQ7 expression and ATP in cerebellum, supporting bioenergetic compromise linked to CoQ pathway expression. (hsiao2019reductionsincoq2 pages 2-4)

### 2.6 Genetics and susceptibility
MSA is largely sporadic, but genetic susceptibility exists with low estimated heritability. A 2023 genetics review reports pooled heritability estimates of **~2.09–6.65%**, and discusses associations in categories including PD-related genes, oxidative stress/inflammation genes, and repeat expansions; **SNCA SNP associations** have been reported in European cohorts but not consistently replicated in Asian cohorts (in part due to allele frequency differences and neuropathologic confirmation differences). (tseng2023thegeneticbasis pages 1-2)

---

## 3) Key molecular players, cell types, and anatomical loci (knowledge-base entity lists)

### 3.1 Genes/proteins (HGNC symbols; selected high-confidence in provided evidence)
**α-synuclein:** **SNCA** (central aggregate component; GCIs; strain/propagation concepts) (torremuruzabal2023hostoligodendrogliopathyand pages 1-3, sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2)

**Myelin/oligodendrocyte cytoskeleton/aggregation facilitation:** **TPPP** (p25α; relocalizes and co-aggregates with GCI biology; early-stage oligodendrocyte marker dynamics) (nishimura2023earlyandextensive pages 6-8, tanaka2025pathologicalandmolecular pages 2-5)

**Gap junction / glial coupling:** **GJB1** (Cx32), **GJC2** (Cx47), **GJA1** (Cx43) (protein-level pathology: redistribution/loss, co-localization with p-αSyn, stage-dependent decreases) (nishimura2023earlyandextensive pages 6-8)

**Myelin sheath proteins:** **MAG** (early preferential reduction), **MOG** (later reduction) (nishimura2023earlyandextensive pages 6-8)

**Mitochondrial CoQ biosynthesis:** **COQ2**, **COQ7** (reduced expression correlating with ATP reductions), and plasma CoQ10 deficiency hypothesis (hsiao2019reductionsincoq2 pages 2-4, mitsui2016plasmacoenzymeq10 pages 1-2)

**Microglial/homeostatic marker used in staging:** **P2RY12** (distribution changes in early lesions) (nishimura2023earlyandextensive pages 6-8)

### 3.2 Chemical entities / small molecules (CHEBI; used mechanistically or clinically)
* **Coenzyme Q10 (ubiquinone-10)**—bioenergetics and antioxidant; reduced levels in MSA plasma and in disease models/reviews; potential supplementation target (mitsui2016plasmacoenzymeq10 pages 1-2, compagnoni2019understandingthepathogenesis pages 4-6)
* **Verdiperstat (BHV-3241)**—a **myeloperoxidase (MPO) inhibitor** evaluated clinically to modulate microglial activation/inflammation in MSA (NCT04616456 chunk 1, NCT03952806 chunk 1)

### 3.3 Cell types (Cell Ontology style; principal affected/active populations)
* **Oligodendrocytes** (primary site of GCIs; connexin redistribution; MAG/MOG changes) (nishimura2023earlyandextensive pages 6-8)
* **Microglia / macrophages** (CD68+ infiltration early; strain-dependent activation patterns) (nishimura2023earlyandextensive pages 6-8, torremuruzabal2023hostoligodendrogliopathyand pages 1-3)
* **T cells** (CD3+ infiltration early; CD4 and CD8 subsets present) (nishimura2023earlyandextensive pages 6-8)
* **Neurons (axons)** (sources/targets of α-syn propagation; axonal Lewy neurites proposed precursors to GCIs in transfer model) (nuccio2023oligodendrocytespruneaxons pages 1-2)

### 3.4 Anatomical locations (UBERON style; commonly involved systems)
* **Striatonigral system** (MSA-P predominant; putamen/substantia nigra involvement) (tanaka2025pathologicalandmolecular pages 1-2)
* **Olivopontocerebellar system** (MSA-C predominant; cerebellar pathways; cerebellar afferent fiber demyelination staging) (tanaka2025pathologicalandmolecular pages 1-2, nishimura2023earlyandextensive pages 1-2)
* **Cerebellar white matter / cerebellar afferent fibers** (site of staged demyelination and connexin pathology) (nishimura2023earlyandextensive pages 1-2)

---

## 4) GO-style biological processes and cellular components (for annotation)

### 4.1 Disrupted biological processes (representative GO terms; mapped to evidence)
* **Protein aggregation / amyloid fibril formation** (α-syn misfolding and strain behavior; GCIs) (torremuruzabal2023hostoligodendrogliopathyand pages 1-3)
* **Cell-to-cell propagation of misfolded proteins** (“prion-like” transmission concept) (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2, nuccio2023oligodendrocytespruneaxons pages 1-2)
* **Autophagy and lysosome-mediated degradation** (lysosomes/peroxisomes within GCIs; autophagy pathway implication) (boing2024distinctultrastructuralphenotypes pages 10-11)
* **Myelination and myelin maintenance** (MAG/MOG changes; distal oligodendrogliopathy-type demyelination) (nishimura2023earlyandextensive pages 6-8)
* **Gap junction assembly/communication** (Cx32 loss/redistribution; Cx43/Cx47 junction reduction) (nishimura2023earlyandextensive pages 6-8)
* **Immune activation / neuroinflammatory response** (CD68+ microglia/macrophages; T cell infiltration early) (nishimura2023earlyandextensive pages 6-8)
* **Mitochondrial electron transport / ATP synthesis** (COQ2/COQ7 expression associated with ATP reductions; CoQ10 deficiency) (hsiao2019reductionsincoq2 pages 2-4, mitsui2016plasmacoenzymeq10 pages 1-2)

### 4.2 Cellular components (representative GO CC terms; mapped to evidence)
* **Oligodendrocyte cytoplasm** (GCIs) (nishimura2023earlyandextensive pages 1-2)
* **Lysosome / multivesicular body** (abundant in GCIs by EM) (boing2024distinctultrastructuralphenotypes pages 10-11)
* **Peroxisome** (identified vesicles co-localizing with α-syn pathology) (boing2024distinctultrastructuralphenotypes pages 10-11)
* **Myelin sheath / paranode** (MAG/MOG changes; paranodal protein loss; connexin localization changes) (nishimura2023earlyandextensive pages 6-8)
* **Mitochondrion** (bioenergetic/CoQ10 axis; ATP deficits) (hsiao2019reductionsincoq2 pages 2-4)

---

## 5) Disease progression model (sequence of events)
A synthesis consistent with the retrieved evidence is:

1. **Initiation/early molecular events**: α-syn conformers emerge and/or are introduced/propagate; strain-like conformations may influence cell specificity and severity. (torremuruzabal2023hostoligodendrogliopathyand pages 1-3)
2. **Early oligodendroglial pathology**: p-αSyn+ oligodendrocytes/GCIs appear early in staged lesions; in some models, neuronal pathology precedes oligodendroglial inclusions via transfer mechanisms. (nishimura2023earlyandextensive pages 6-8, nuccio2023oligodendrocytespruneaxons pages 1-2)
3. **Early myelin–axon unit failure**: selective early **MAG** loss, early Cx32 loss/redistribution, and early paranodal marker reductions suggest impaired metabolic and electrical coupling and axonal support. (nishimura2023earlyandextensive pages 6-8)
4. **Inflammatory amplification**: stage I lesions show pronounced microglia/macrophage infiltration and T-cell presence; strain-host interaction can modify immune response patterns. (nishimura2023earlyandextensive pages 6-8, torremuruzabal2023hostoligodendrogliopathyand pages 1-3)
5. **Proteostasis failure and organelle pathology**: GCIs are enriched in lysosomes/multivesicular bodies and include peroxisomal components, implicating autophagy–lysosome axis in aggregate handling or dysfunction. (boing2024distinctultrastructuralphenotypes pages 10-11)
6. **Bioenergetic decline and oxidative stress**: CoQ10/COQ2-linked mitochondrial compromise and ATP reductions in affected regions contribute to vulnerability and neurodegeneration. (hsiao2019reductionsincoq2 pages 2-4, mitsui2016plasmacoenzymeq10 pages 1-2)
7. **System degeneration and clinical convergence**: initially predominant striatonigral vs olivopontocerebellar involvement can converge over time with widespread pathology. (tanaka2025pathologicalandmolecular pages 1-2)

---

## 6) Phenotypic manifestations linked to mechanisms (HP-style mapping)
* **Parkinsonism with poor levodopa response**: linked to striatonigral degeneration and widespread network dysfunction in α-synucleinopathy with oligodendroglial dominance. (tanaka2025pathologicalandmolecular pages 1-2)
* **Cerebellar ataxia**: linked to olivopontocerebellar atrophy and demyelination/oligodendroglial pathology in cerebellar pathways. (nishimura2023earlyandextensive pages 1-2, tanaka2025pathologicalandmolecular pages 1-2)
* **Autonomic dysfunction/failure**: core clinical feature of MSA; reflects degeneration in autonomic pathways (clinical characterization in reviews and trial protocols). (tanaka2025pathologicalandmolecular pages 1-2, NCT05167721 chunk 1)
* **Cognitive impairment (subset)**: up to **~37%** reported in clinicopathological studies summarized in early-stage review; may relate to broader inclusion distribution and neuronal dysfunction. (tanaka2025pathologicalandmolecular pages 1-2)

---

## 7) Recent developments and “latest research” emphasis (2023–2024)

### 7.1 2023–2024 advances in mechanistic understanding
* **Strain biology and host restriction (2023, Brain):** Demonstrated that recombinant α-syn conformers differentially shape oligodendroglial inclusion properties, neurodegeneration, and immune activation, providing an experimental basis for heterogeneity in MSA progression. Publication: Feb 2023; URL: https://doi.org/10.1093/brain/awac061 (torremuruzabal2023hostoligodendrogliopathyand pages 1-3)
* **Axon-to-oligodendrocyte transfer model (2023, Biomolecules):** Proposed and experimentally supported a mechanism where oligodendrocytes acquire aggregated α-syn by pruning/engulfing diseased axonal segments, leading to GCI formation after an initial axonal/neuritic phase. Publication: Feb 2023; URL: https://doi.org/10.3390/biom13020269 (nuccio2023oligodendrocytespruneaxons pages 1-2)
* **Stage-resolved glial coupling and demyelination (2023, Brain Pathology):** Introduced histopathological staging of cerebellar afferent demyelination and identified early **Cx32 loss/redistribution** and early immune infiltration. Publication: Nov 2023; URL: https://doi.org/10.1111/bpa.13131 (nishimura2023earlyandextensive pages 1-2, nishimura2023earlyandextensive pages 6-8)
* **Ultrastructural implicature of autophagy–lysosome and peroxisomes (2024, Brain):** EM data show lysosomes and peroxisomes co-localize with α-syn pathology in GCIs (observed across >100 GCIs), strengthening the hypothesis that organelle trafficking/clearance pathways are centrally involved. Publication: May 2024; URL: https://doi.org/10.1093/brain/awae137 (boing2024distinctultrastructuralphenotypes pages 10-11)

### 7.2 Current expert synthesis (authoritative reviews)
A 2024 review emphasizes convergent “players” in MSA and PD—oxidative stress, iron-related pathology, mitochondrial/respiratory-chain dysfunction, proteasomal function loss, microglial activation and neuroinflammation—while acknowledging that precise causative mechanisms remain unclear and likely synergistic. Publication online: 25 May 2023; journal issue: May 2024; URL: https://doi.org/10.1007/s00702-023-02653-2 (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2)

---

## 8) Current applications and real-world implementations

### 8.1 Biomarkers and imaging implementations
* **Biofluid α-synuclein oligomers (clinical research):** Observational biomarker study assessing oligomeric α-synuclein levels in CSF and plasma (BIOAMS). ClinicalTrials.gov NCT01485549; first posted 2011-12-05; completion 2018-11-21. (NCT01485549 chunk 1)
* **Neuroinflammation imaging (TSPO PET) as pharmacodynamic biomarker:** A completed pilot trial uses **[18F]PBR06 TSPO PET** to measure microglial activation and evaluate whether verdiperstat reduces TSPO signal in MSA. ClinicalTrials.gov NCT04616456; first posted 2020-11-05; completion 2022-01-30. (NCT04616456 chunk 1)
* **α-synuclein PET tracer development (real-world translational R&D):** A completed observational study aims to develop an α-syn PET tracer (Morphomer-based; [18F]ACI-3847) to quantify in vivo α-syn load in MSA/PD/DLB and support future trials. ClinicalTrials.gov NCT05067192; first posted 2021-10-05; completion 2021-09-01. (NCT05067192 chunk 1)

### 8.2 Therapeutic strategies linked to mechanisms (clinical trials)
* **Anti-inflammatory/oxidative pathway targeting (MPO inhibitor):** Verdiperstat (BHV-3241), an MPO inhibitor, tested in Phase 3 MSA trial with clinical endpoints (modified UMSARS over 48 weeks). ClinicalTrials.gov NCT03952806 (M-STAR); first posted 2019-05-16; results first posted 2023-09-29. (NCT03952806 chunk 1)
* **Regenerative/neurotrophic strategy:** Intrathecal autologous mesenchymal stem cells (MSCs) are being evaluated for safety and exploratory efficacy with MRI/CSF biomarkers. ClinicalTrials.gov NCT02315027; first posted 2014-12-11; active-not-recruiting with estimated completion 2026-03. (NCT02315027 chunk 1)
* **Placebo-controlled MSC trial (adaptive design):** Intrathecal adipose-derived autologous MSCs with UMSARS outcomes and NfL as biomarker. ClinicalTrials.gov NCT05167721; first posted 2021-12-22; active-not-recruiting with estimated completion 2026-12. (NCT05167721 chunk 1)

---

## 9) Recent statistics and data (from retrieved studies)

* **Neuropathology cohort and staging:** 15 autopsied MSA cases staged into Stage I–III demyelination; early stage showed MAG loss, Cx32 loss/redistribution and higher immune infiltration. (nishimura2023earlyandextensive pages 1-2, nishimura2023earlyandextensive pages 6-8)
* **Ultrastructural sampling:** Lysosomes/peroxisomes observed in **>100 GCIs** by EM, with “almost all” GCIs containing lysosomes and multivesicular bodies. (boing2024distinctultrastructuralphenotypes pages 10-11)
* **Genetic heritability:** pooled heritability estimate **~2.09–6.65%** reported in 2023 genetics review. (tseng2023thegeneticbasis pages 1-2)
* **Plasma CoQ10 (quantitative):** 44 MSA vs 39 controls, **0.51 ± 0.22 μg/mL** vs **0.72 ± 0.42 μg/mL**, P=0.01. (mitsui2016plasmacoenzymeq10 pages 1-2)
* **Clinical trial sizes (implementation scale):** Verdiperstat Phase 3 enrolled **421** participants (NCT03952806). (NCT03952806 chunk 1)

---

## 10) Evidence items (PMID/DOI-indexed)
PMIDs were not consistently present in the retrieved full-text excerpts; therefore, items are indexed by DOI/URL from the extracted evidence.

1. Nishimura Y et al. **Brain Pathology**. 2023-11. “Early and extensive alterations of glial connexins…” DOI: 10.1111/bpa.13131. https://doi.org/10.1111/bpa.13131 (nishimura2023earlyandextensive pages 1-2, nishimura2023earlyandextensive pages 6-8)
2. Böing C et al. **Brain**. 2024-05. “Distinct ultrastructural phenotypes…” DOI: 10.1093/brain/awae137. https://doi.org/10.1093/brain/awae137 (boing2024distinctultrastructuralphenotypes pages 10-11)
3. Torre-Muruzabal T et al. **Brain**. 2023-02. “Host oligodendrogliopathy and α-synuclein strains…” DOI: 10.1093/brain/awac061. https://doi.org/10.1093/brain/awac061 (torremuruzabal2023hostoligodendrogliopathyand pages 1-3)
4. De Nuccio F et al. **Biomolecules**. 2023-02. “Oligodendrocytes prune axons…” DOI: 10.3390/biom13020269. https://doi.org/10.3390/biom13020269 (nuccio2023oligodendrocytespruneaxons pages 1-2)
5. Tseng FS et al. **Journal of Translational Medicine**. 2023-02. “The genetic basis of multiple system atrophy.” DOI: 10.1186/s12967-023-03905-1. https://doi.org/10.1186/s12967-023-03905-1 (tseng2023thegeneticbasis pages 1-2)
6. Sian-Hulsmann J, Riederer P. **Journal of Neural Transmission**. Online 2023-05-25; issue 2024-05. DOI: 10.1007/s00702-023-02653-2. https://doi.org/10.1007/s00702-023-02653-2 (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2)
7. Mitsui J et al. **JAMA Neurology**. 2016-08. “Plasma coenzyme Q10 levels…” DOI: 10.1001/jamaneurol.2016.1325. https://doi.org/10.1001/jamaneurol.2016.1325 (mitsui2016plasmacoenzymeq10 pages 1-2)
8. Hsiao J-HT et al. **Frontiers in Neuroscience**. 2019-11. “Reductions in COQ2 expression relate to reduced ATP…” DOI: 10.3389/fnins.2019.01187. https://doi.org/10.3389/fnins.2019.01187 (hsiao2019reductionsincoq2 pages 2-4)

---

## 11) Notes on limitations of this report
* A high-impact 2023 Nature Reviews Neuroscience review (“Multiple system atrophy: at the crossroads of cellular, molecular and genetic mechanisms”) and a 2024 Lancet Neurology review were identified by search but were **unobtainable** in the current tool context and therefore are not cited here.
* PMIDs were not reliably present in the extracted evidence snippets; DOI/URL citations are used instead.

---

## Appendix: Figure evidence (cropped)
* Staged demyelination with MAG/MOG changes and p-αSyn+ oligodendrocytes (nishimura2023earlyandextensive media b572b16d)
* Connexin redistribution (Cx32 vs Cx47) and Cx32 co-localization with p-αSyn+ GCIs (nishimura2023earlyandextensive media aa3bf217)


References

1. (sianhulsmann2024the‘αsynucleinopathysyndicate’ pages 1-2): Jeswinder Sian-Hulsmann and Peter Riederer. The ‘α-synucleinopathy syndicate’: multiple system atrophy and parkinson’s disease. Journal of Neural Transmission, 131:585-595, May 2024. URL: https://doi.org/10.1007/s00702-023-02653-2, doi:10.1007/s00702-023-02653-2. This article has 13 citations and is from a peer-reviewed journal.

2. (nishimura2023earlyandextensive pages 1-2): Yuji Nishimura, Katsuhisa Masaki, Dai Matsuse, Hiroo Yamaguchi, Tatsunori Tanaka, Eriko Matsuo, Shotaro Hayashida, Mitsuru Watanabe, Takuya Matsushita, Shoko Sadashima, Naokazu Sasagasako, Ryo Yamasaki, Noriko Isobe, Toru Iwaki, and Jun‐ichi Kira. Early and extensive alterations of glial connexins, distal oligodendrogliopathy type demyelination, and nodal/paranodal pathology are characteristic of multiple system atrophy. Brain Pathology, Nov 2023. URL: https://doi.org/10.1111/bpa.13131, doi:10.1111/bpa.13131. This article has 8 citations and is from a domain leading peer-reviewed journal.

3. (torremuruzabal2023hostoligodendrogliopathyand pages 1-3): Teresa Torre-Muruzabal, Anke Van der Perren, Audrey Coens, Géraldine Gelders, Anna Barber Janer, Sara Camacho-Garcia, Therése Klingstedt, Peter Nilsson, Nadia Stefanova, Ronald Melki, Veerle Baekelandt, and Wouter Peelaerts. Host oligodendrogliopathy and ɑ-synuclein strains dictate disease severity in multiple system atrophy. Brain : a journal of neurology, 146:237-251, Feb 2023. URL: https://doi.org/10.1093/brain/awac061, doi:10.1093/brain/awac061. This article has 20 citations.

4. (boing2024distinctultrastructuralphenotypes pages 10-11): Carolin Böing, Marta Di Fabrizio, Domenic Burger, John G J M Bol, Evelien Huisman, Annemieke J M Rozemuller, Wilma D J van de Berg, Henning Stahlberg, and Amanda J Lewis. Distinct ultrastructural phenotypes of glial and neuronal alpha-synuclein inclusions in multiple system atrophy. Brain, 147:3727-3741, May 2024. URL: https://doi.org/10.1093/brain/awae137, doi:10.1093/brain/awae137. This article has 24 citations and is from a highest quality peer-reviewed journal.

5. (compagnoni2019understandingthepathogenesis pages 4-6): Giacomo Monzio Compagnoni and Alessio Di Fonzo. Understanding the pathogenesis of multiple system atrophy: state of the art and future perspectives. Acta Neuropathologica Communications, Jul 2019. URL: https://doi.org/10.1186/s40478-019-0730-6, doi:10.1186/s40478-019-0730-6. This article has 111 citations and is from a peer-reviewed journal.

6. (tanaka2025pathologicalandmolecular pages 1-2): Makoto T. Tanaka, Yasuo Miki, Tomoya Kon, Fumiaki Mori, and Koichi Wakabayashi. Pathological and molecular insights into the early stage of multiple system atrophy. Cells, 14:1966, Dec 2025. URL: https://doi.org/10.3390/cells14241966, doi:10.3390/cells14241966. This article has 4 citations.

7. (federoff2015multiplesystematrophy pages 3-4): Monica Federoff, Lucia V. Schottlaender, Henry Houlden, and Andrew Singleton. Multiple system atrophy: the application of genetics in understanding etiology. Clinical Autonomic Research, 25:19-36, Feb 2015. URL: https://doi.org/10.1007/s10286-014-0267-5, doi:10.1007/s10286-014-0267-5. This article has 39 citations and is from a peer-reviewed journal.

8. (hsiao2023roleofoligodendrocyte pages 2-4): Jen-Hsiang T. Hsiao, Onur Tanglay, Anne A. Li, Aysha Y. G. Strobbe, Woojin Scott Kim, Glenda M. Halliday, and YuHong Fu. Role of oligodendrocyte lineage cells in multiple system atrophy. Cells, 12:739, Feb 2023. URL: https://doi.org/10.3390/cells12050739, doi:10.3390/cells12050739. This article has 17 citations.

9. (tanaka2025pathologicalandmolecular pages 2-5): Makoto T. Tanaka, Yasuo Miki, Tomoya Kon, Fumiaki Mori, and Koichi Wakabayashi. Pathological and molecular insights into the early stage of multiple system atrophy. Cells, 14:1966, Dec 2025. URL: https://doi.org/10.3390/cells14241966, doi:10.3390/cells14241966. This article has 4 citations.

10. (nuccio2023oligodendrocytespruneaxons pages 1-2): Francesco De Nuccio, Marianna Kashyrina, Francesca Serinelli, Florent Laferrière, Dario Domenico Lofrumento, Francesca De Giorgi, and François Ichas. Oligodendrocytes prune axons containing α-synuclein aggregates in vivo: lewy neurites as precursors of glial cytoplasmic inclusions in multiple system atrophy? Biomolecules, 13:269, Feb 2023. URL: https://doi.org/10.3390/biom13020269, doi:10.3390/biom13020269. This article has 19 citations.

11. (nishimura2023earlyandextensive pages 6-8): Yuji Nishimura, Katsuhisa Masaki, Dai Matsuse, Hiroo Yamaguchi, Tatsunori Tanaka, Eriko Matsuo, Shotaro Hayashida, Mitsuru Watanabe, Takuya Matsushita, Shoko Sadashima, Naokazu Sasagasako, Ryo Yamasaki, Noriko Isobe, Toru Iwaki, and Jun‐ichi Kira. Early and extensive alterations of glial connexins, distal oligodendrogliopathy type demyelination, and nodal/paranodal pathology are characteristic of multiple system atrophy. Brain Pathology, Nov 2023. URL: https://doi.org/10.1111/bpa.13131, doi:10.1111/bpa.13131. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (nishimura2023earlyandextensive media b572b16d): Yuji Nishimura, Katsuhisa Masaki, Dai Matsuse, Hiroo Yamaguchi, Tatsunori Tanaka, Eriko Matsuo, Shotaro Hayashida, Mitsuru Watanabe, Takuya Matsushita, Shoko Sadashima, Naokazu Sasagasako, Ryo Yamasaki, Noriko Isobe, Toru Iwaki, and Jun‐ichi Kira. Early and extensive alterations of glial connexins, distal oligodendrogliopathy type demyelination, and nodal/paranodal pathology are characteristic of multiple system atrophy. Brain Pathology, Nov 2023. URL: https://doi.org/10.1111/bpa.13131, doi:10.1111/bpa.13131. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (nishimura2023earlyandextensive media aa3bf217): Yuji Nishimura, Katsuhisa Masaki, Dai Matsuse, Hiroo Yamaguchi, Tatsunori Tanaka, Eriko Matsuo, Shotaro Hayashida, Mitsuru Watanabe, Takuya Matsushita, Shoko Sadashima, Naokazu Sasagasako, Ryo Yamasaki, Noriko Isobe, Toru Iwaki, and Jun‐ichi Kira. Early and extensive alterations of glial connexins, distal oligodendrogliopathy type demyelination, and nodal/paranodal pathology are characteristic of multiple system atrophy. Brain Pathology, Nov 2023. URL: https://doi.org/10.1111/bpa.13131, doi:10.1111/bpa.13131. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (mitsui2016plasmacoenzymeq10 pages 1-2): Jun Mitsui, Takashi Matsukawa, Tsutomu Yasuda, Hiroyuki Ishiura, and Shoji Tsuji. Plasma coenzyme q10 levels in patients with multiple system atrophy. JAMA neurology, 73 8:977-80, Aug 2016. URL: https://doi.org/10.1001/jamaneurol.2016.1325, doi:10.1001/jamaneurol.2016.1325. This article has 65 citations and is from a highest quality peer-reviewed journal.

15. (hsiao2019reductionsincoq2 pages 2-4): Jen-Hsiang T. Hsiao, Sivaraman Purushothuman, Poul H. Jensen, Glenda M. Halliday, and Woojin Scott Kim. Reductions in coq2 expression relate to reduced atp levels in multiple system atrophy brain. Frontiers in Neuroscience, Nov 2019. URL: https://doi.org/10.3389/fnins.2019.01187, doi:10.3389/fnins.2019.01187. This article has 20 citations and is from a peer-reviewed journal.

16. (tseng2023thegeneticbasis pages 1-2): Fan Shuen Tseng, Joel Qi Xuan Foo, Aaron Shengting Mai, and Eng-King Tan. The genetic basis of multiple system atrophy. Journal of Translational Medicine, Feb 2023. URL: https://doi.org/10.1186/s12967-023-03905-1, doi:10.1186/s12967-023-03905-1. This article has 25 citations and is from a peer-reviewed journal.

17. (NCT04616456 chunk 1): Vikram Khurana, MD PhD. Effect of Verdiperstat on Microglial Activation in Well-characterized MSA Patients. Brigham and Women's Hospital. 2020. ClinicalTrials.gov Identifier: NCT04616456

18. (NCT03952806 chunk 1):  Study of BHV-3241 in Participants With Multiple System Atrophy. Biohaven Pharmaceuticals, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03952806

19. (NCT05167721 chunk 1): Wolfgang Singer, MD. Randomized Double-Blind Placebo-Controlled Adaptive Design Trial Of Intrathecally Administered Autologous Mesenchymal Stem Cells In Multiple System Atrophy. Mayo Clinic. 2021. ClinicalTrials.gov Identifier: NCT05167721

20. (NCT01485549 chunk 1):  Oligomeric Alpha-synuclein in Multiple System Atrophy. University Hospital, Bordeaux. 2012. ClinicalTrials.gov Identifier: NCT01485549

21. (NCT05067192 chunk 1): Oskar Hansson. Optimization of Morphomer-based Alpha-synuclein PET Tracers. Skane University Hospital. 2021. ClinicalTrials.gov Identifier: NCT05067192

22. (NCT02315027 chunk 1): Wolfgang Singer, MD. Mesenchymal Stem Cell Therapy in Multiple System Atrophy. Mayo Clinic. 2012. ClinicalTrials.gov Identifier: NCT02315027