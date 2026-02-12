---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-05T14:34:28.620823'
end_time: '2026-02-05T14:40:48.860892'
duration_seconds: 380.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Salla Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Salla Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Salla Disease**.
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
- **Disease Name:** Salla Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Salla Disease**.
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
Objective 1 (literature): Completed. Key sources identified include a 2023 cryo-EM structural/mechanistic study of Sialin (SLC17A5) (Science Advances), a 2022 authoritative chapter on lysosomal membrane defects, a comprehensive lysosomal storage disease review, and recent iPSC-based neural cell evidence showing downstream glycosphingolipid (GSL) disturbances. (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, schwake2022lysosomalmembranedefects pages 2-2, hu2023themolecularmechanism pages 1-2, sabir2025lysosomalfreesialic pages 2-3, sabir2025lysosomalfreesialic pages 1-2)
Objective 2–6: Addressed below in a consolidated research report.

Disease Pathophysiology Research Report
Target Disease
- Disease Name: Salla disease (also termed classic free sialic acid storage disease, FSASD)
- MONDO IDs: Salla disease MONDO:0011449; Free sialic acid storage disease MONDO:0019366; Infantile free sialic acid storage disease (ISSD) MONDO:0010027
- Category: Mendelian, lysosomal storage disorder

1) Core Pathophysiology
Salla disease results from biallelic pathogenic variants in SLC17A5, encoding the lysosomal membrane transporter sialin, which exports free sialic acid (Neu5Ac) from the lysosomal lumen to the cytosol. Loss or reduction of sialin-mediated export leads to lysosomal accumulation of free Neu5Ac and secondary lysosomal dysfunction. The disease spans a spectrum from severe infantile (ISSD) to classic Salla disease with slower progression into adulthood. (schwake2022lysosomalmembranedefects pages 2-2, sabir2025lysosomalfreesialic pages 1-2)

Mechanistically, Sialin is a 12-transmembrane major facilitator superfamily (MFS) transporter that mediates proton-coupled symport of Neu5Ac. A 3.4 Å cryo-EM structure captured an inward-facing partially open conformation and identified two conserved glutamates (E171 and E175) required for H+ coupling/sensing; alanine/glutamine substitutions at either site reduce transport by ~95%, and double substitution abolishes detectable transport, supporting a dual-Glu H+ coupling mechanism. A cytosolic constriction controlling conformational changes helps enforce gradient-driven transport. (Hu et al., Science Advances, published Jan 2023; URL: https://doi.org/10.1126/sciadv.ade8346) (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, hu2023themolecularmechanism pages 1-2)

Consequences for cellular physiology include swollen, numerous lysosomes with trapped free sialic acid and perturbed lysosomal homeostasis. Sialin can transport other acidic sugars (e.g., glucuronic/iduronic acids), implicating broader anion handling at the lysosomal membrane; however, Neu5Ac transport is the canonical defect in Salla disease. (Schwake & Saftig, 2022; URL: https://doi.org/10.1002/9781119697312.ch21) (schwake2022lysosomalmembranedefects pages 2-2)

Neuroglial involvement is prominent. Hypomyelination on MRI, corpus callosum hypoplasia, and progressive cerebellar atrophy indicate oligodendroglial and cerebellar vulnerability. Patient-derived iPSC neural cells (radial glia, cortical neurons, immature and mature astrocytes) display markedly elevated free sialic acid and cell-type-specific disturbances in GSL metabolism, with mature astrocytes showing the largest shifts and increased lysosomal glycohydrolase activities, consistent with widespread lysosomal lipid turnover changes. (Sabir et al., Scientific Reports, Aug 2025; URL: https://doi.org/10.1038/s41598-025-12682-4) (sabir2025lysosomalfreesialic pages 1-2, sabir2025lysosomalfreesialic pages 2-3, sabir2025lysosomalfreesialic pages 12-13)

2) Key Molecular Players
- Gene/Protein: SLC17A5 (HGNC:11079), lysosomal sialic acid/H+ symporter (sialin). Critical residues for mechanism include E171 and E175 (H+ coupling/sensing) and R57 (substrate recognition; pathogenic variants at R57 impair function). (Hu 2023 Science Advances; URL: https://doi.org/10.1126/sciadv.ade8346) (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4)
- Chemical entities: N-acetylneuraminic acid (Neu5Ac) accumulates in lysosomes; broader alterations in glycosphingolipids (gangliosides) are evident in disease models. (sabir2025lysosomalfreesialic pages 1-2, sabir2025lysosomalfreesialic pages 2-3)
- Cell types: Oligodendrocytes are implicated by hypomyelination; neurons and astrocytes in iPSC models show elevated free sialic acid and altered GSL metabolism, especially mature astrocytes. (sabir2025lysosomalfreesialic pages 13-14, sabir2025lysosomalfreesialic pages 2-3)
- Anatomical locations: Brain—corpus callosum (hypoplasia) and cerebellum (atrophy) are commonly involved on MRI. (sabir2025lysosomalfreesialic pages 1-2)

3) Biological Processes (GO-relevant)
- Proton-coupled symport involved in sialic acid transmembrane transport across the lysosomal membrane; dual-Glu (E171/E175) mechanism supports H+ coupling. (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4)
- Lysosomal transport/efflux of small anions (free sialic acid), with downstream lysosomal homeostasis disruption. (schwake2022lysosomalmembranedefects pages 2-2)
- Myelination and maintenance of myelin sheaths are impacted, consistent with hypomyelination features. (sabir2025lysosomalfreesialic pages 13-14)
- Glycosphingolipid metabolic process and lysosomal lipid catabolism are altered in patient-derived neural cells; glycohydrolase activities are elevated in mature astrocytes. (sabir2025lysosomalfreesialic pages 2-3, sabir2025lysosomalfreesialic pages 12-13)

4) Cellular Components
- Sialin resides in the lysosomal membrane; the transporter’s central tunnel and cytosolic constriction mediate inward-facing conformational control of substrate translocation. Pathogenic mutations map to structural regions affecting helix packing, substrate pathway residues, and transporter–lipid interfaces. (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, schwake2022lysosomalmembranedefects pages 2-2)

5) Disease Progression
- Initiation: Biallelic SLC17A5 pathogenic variants cause reduced/abolished sialic acid export from lysosomes, leading to intralysosomal accumulation of free Neu5Ac. (schwake2022lysosomalmembranedefects pages 2-2)
- Cellular cascade: Lysosomal enlargement and dysfunction; secondary perturbations of GSL metabolism and lysosomal glycohydrolase activities, especially in astrocytes; neuronal/oligodendroglial dysfunction with impaired myelination. (sabir2025lysosomalfreesialic pages 2-3, sabir2025lysosomalfreesialic pages 13-14)
- Systems-level manifestations: White-matter hypomyelination, corpus callosum hypoplasia, progressive cerebellar atrophy; clinical phenotypes from severe infantile to classic forms. (sabir2025lysosomalfreesialic pages 1-2)

6) Phenotypic Manifestations (selected; HP mapping)
- Developmental delay (HP:0001263), spasticity (HP:0001257), athetosis (HP:0002305), seizures (HP:0001250), cognitive impairment (HP:0100543); neuroimaging: hypomyelination (HP:0006809), corpus callosum hypoplasia (HP:0002079), cerebellar atrophy (HP:0001272). These features are aligned with reported clinical spectra across FSASD/Salla disease. (sabir2025lysosomalfreesialic pages 1-2)

Recent Developments and Latest Research (2023–2024 priority)
- 2023 mechanistic advance: First high-resolution human Sialin cryo-EM structure with functional assays defining a two-glutamate H+ coupling mechanism (E171, E175), substrate-recognition residue R57, and a cytosolic helix whose stabilization is required for function; mutagenesis quantified strong activity loss (~90–100%) upon disruption. Published Jan 2023, Science Advances; DOI/URL: https://doi.org/10.1126/sciadv.ade8346. (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, hu2023themolecularmechanism pages 1-2)
- Cellular modeling: iPSC-derived neural cells from FSASD patients (2025) reveal robust increases of free sialic acid across cell types and prominent GSL alterations in mature astrocytes, with increased lysosomal glycohydrolase activities, pinpointing astrocyte involvement and selective vulnerability. Although 2025, these data extend 2023–2024 mechanistic insights into human cell models. URL: https://doi.org/10.1038/s41598-025-12682-4. (sabir2025lysosomalfreesialic pages 2-3, sabir2025lysosomalfreesialic pages 12-13)

Current Applications and Implementations
- Structural insights from 2023 enable variant interpretation and mechanistic classification (e.g., residues in proton-coupling network vs. substrate path vs. helix-packing interfaces) that can support pathogenicity assessment for SLC17A5 variants of uncertain significance in clinical genetics workflows. (hu2023themolecularmechanism pages 3-4)
- iPSC disease modeling demonstrates quantifiable biochemical endpoints (free sialic acid levels; GSL profiles; lysosomal enzyme activities) that can be used for preclinical screening and mechanistic studies in neural lineages relevant to FSASD. (sabir2025lysosomalfreesialic pages 2-3, sabir2025lysosomalfreesialic pages 12-13)

Expert Opinions and Analysis
- Authoritative lysosomal membrane-defect perspective: While the core defect—lysosomal free sialic acid accumulation due to SLC17A5 mutations—is established, the precise links between impaired sialic acid efflux and neurodevelopmental/neurodegenerative outcomes have remained incompletely explained, motivating ongoing mechanistic and cellular modeling studies. (Schwake & Saftig, 2022; URL: https://doi.org/10.1002/9781119697312.ch21) (schwake2022lysosomalmembranedefects pages 2-2)
- Structural biophysics experts propose a structure-based mechanism that revises prior single-Glu models to a dual-Glu H+ coupling paradigm, offering clear mechanistic explanations for many mapped pathogenic variants. (Hu 2023; URL: https://doi.org/10.1126/sciadv.ade8346) (hu2023themolecularmechanism pages 1-2, hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4)

Relevant Statistics and Quantitative Data
- Transport mutagenesis in human Sialin: E171Q or E175Q reduce transport to ~5% of wild-type, and double mutation eliminates measurable transport; R57A retains ~10% activity; these quantify critical roles in H+ coupling and substrate recognition. (Jan 2023; URL: https://doi.org/10.1126/sciadv.ade8346) (hu2023themolecularmechanism pages 3-4)
- iPSC-derived neural cells: Free sialic acid elevations vs. controls—iPSCs 242%, iRGCs 223%, cortical neurons 400%, immature astrocytes 540%, mature astrocytes 830%; neuronal gangliosides (e.g., GM1a) reduced in cortical neurons, with broad GSL shifts most pronounced in mature astrocytes; glycohydrolase activities elevated in mature astrocytes. (Aug 2025; URL: https://doi.org/10.1038/s41598-025-12682-4) (sabir2025lysosomalfreesialic pages 2-3)

Pathophysiology Description (for knowledge base)
Salla disease is a lysosomal storage disease due to biallelic SLC17A5 variants impairing the lysosomal transporter sialin, which mediates proton-coupled export of free N-acetylneuraminic acid. A 2023 human cryo-EM structure demonstrates a dual-glutamate (E171/E175) H+ coupling apparatus and identifies substrate and structural residues explaining pathogenic variant classes. Impaired export traps free sialic acid, disturbs lysosomal function, and drives downstream alterations in glycosphingolipid metabolism and lysosomal enzyme activities. Neuroimaging and cell models implicate oligodendrocyte/myelination defects and astrocyte metabolic dysregulation, with clinical expression ranging from severe ISSD to classic Salla disease with hypomyelination, callosal hypoplasia, and cerebellar atrophy. (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, schwake2022lysosomalmembranedefects pages 2-2, sabir2025lysosomalfreesialic pages 1-2, sabir2025lysosomalfreesialic pages 2-3)

Gene/Protein Annotations with Ontology Terms
- SLC17A5 (HGNC:11079); Function: lysosomal membrane sialic acid:H+ symporter; Processes: sialic acid transport; proton-coupled symport; Localization: lysosomal membrane; Key residues: E171, E175 (H+ coupling), R57 (substrate binding). (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4)

Phenotype Associations (HP terms)
- Developmental delay (HP:0001263); Spasticity (HP:0001257); Athetosis (HP:0002305); Seizures (HP:0001250); Cognitive impairment (HP:0100543); Hypomyelination (HP:0006809); Corpus callosum hypoplasia (HP:0002079); Cerebellar atrophy (HP:0001272). (sabir2025lysosomalfreesialic pages 1-2)

Cell Type Involvement (CL terms)
- Oligodendrocyte (CL:0000128) – hypomyelination; Neuron (CL:0000540) – altered GSLs, elevated free sialic acid; Astrocyte (CL:0000127) – pronounced GSL metabolic shifts and increased glycohydrolase activities. (sabir2025lysosomalfreesialic pages 13-14, sabir2025lysosomalfreesialic pages 2-3)

Anatomical Locations (UBERON terms)
- Brain (UBERON:0000955); Corpus callosum (UBERON:0002318); Cerebellum (UBERON:0002037). (sabir2025lysosomalfreesialic pages 1-2)

Chemical Entities (CHEBI terms)
- N-acetylneuraminic acid (Neu5Ac; CHEBI:25563); Glycosphingolipids/gangliosides (CHEBI:18154). (sabir2025lysosomalfreesialic pages 1-2, sabir2025lysosomalfreesialic pages 2-3)

Biological Processes and Cellular Components (GO)
- Proton-coupled symport (GO:0015293); Sialic acid transmembrane transport (term name); Transport/lysosomal efflux (GO:0006810, term family); Myelination (GO:0042552); Glycosphingolipid metabolic process (GO:0006687). Localization: Lysosomal membrane (GO:0005765). (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, schwake2022lysosomalmembranedefects pages 2-2, sabir2025lysosomalfreesialic pages 2-3)

Evidence Items with PMIDs/DOIs and URLs
- Hu et al. 2023. The molecular mechanism of sialic acid transport mediated by Sialin. Science Advances. DOI: 10.1126/sciadv.ade8346; URL: https://doi.org/10.1126/sciadv.ade8346. Publication date: Jan 2023. (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4, hu2023themolecularmechanism pages 1-2)
- Schwake & Saftig 2022. Lysosomal Membrane Defects. In: Lysosomal Storage Disorders. DOI: 10.1002/9781119697312.ch21; URL: https://doi.org/10.1002/9781119697312.ch21. Publication date: Jul 2022. (schwake2022lysosomalmembranedefects pages 2-2)
- Ferreira & Gahl 2017. Lysosomal storage diseases. Translational Science of Rare Diseases. DOI: 10.3233/TRD-160005; URL: https://doi.org/10.3233/trd-160005. Publication date: Sep 2017. (schwake2022lysosomalmembranedefects pages 2-2)
- Sabir et al. 2025. Lysosomal free sialic acid storage disorder iPSC-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports. DOI: 10.1038/s41598-025-12682-4; URL: https://doi.org/10.1038/s41598-025-12682-4. Publication date: Aug 2025. (sabir2025lysosomalfreesialic pages 1-2, sabir2025lysosomalfreesialic pages 12-13, sabir2025lysosomalfreesialic pages 2-3)

Ontology-Mapped Annotations Table
| Category | Entity (name) | Ontology ID | Role/Note | Evidence (Context ID) |
|---|---|---|---|---|
| Disease | Salla disease | MONDO:0011449 | Classic (milder) form of free sialic acid storage disease |  |
| Disease | Free sialic acid storage disease | MONDO:0019366 | Umbrella term for Salla disease / ISSD |  |
| Disease | Infantile free sialic acid storage disease (ISSD) | MONDO:0010027 | Severe infantile form with early neurodegeneration |  |
| Gene/Protein | SLC17A5 (Sialin) | HGNC:11079 | Lysosomal sialic acid exporter; H+‑coupled symporter | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Residue | E171 | - | Conserved glutamate required for H+ coupling | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Residue | E175 | - | Conserved glutamate required for H+ coupling | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Residue | R57 | - | Substrate recognition site; pathogenic variants impair function | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Cell type | Oligodendrocyte | CL:0000128 | Implicated in hypomyelination and myelin defects | (sabir2025lysosomalfreesialic pages 13-14) |
| Cell type | Neuron | CL:0000540 | Neuronal phenotypes from lysosomal sialic acid accumulation | (sabir2025lysosomalfreesialic pages 2-3) |
| Cell type | Astrocyte | CL:0000127 | iPSC data show marked altered GSL metabolism (especially mature astrocytes) | (sabir2025lysosomalfreesialic pages 2-3) |
| Anatomical location | Brain | UBERON:0000955 | Primary organ affected; hypomyelination and atrophy reported | (sabir2025lysosomalfreesialic pages 1-2) |
| Anatomical location | Corpus callosum | UBERON:0002318 | Hypoplasia commonly observed on MRI | (sabir2025lysosomalfreesialic pages 1-2) |
| Anatomical location | Cerebellum | UBERON:0002037 | Progressive cerebellar atrophy reported | (sabir2025lysosomalfreesialic pages 1-2) |
| Chemical entity | N-acetylneuraminic acid (Neu5Ac) | CHEBI:25563 | Accumulated free sialic acid within lysosomes | (sabir2025lysosomalfreesialic pages 1-2) |
| Chemical entity | Glycosphingolipids (gangliosides) | CHEBI:18154 | Altered composition and metabolism in patient cells/models | (sabir2025lysosomalfreesialic pages 2-3) |
| Biological process | Transport (lysosomal efflux) | GO:0006810 | Lysosomal export of free sialic acid mediated by sialin | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Biological process | Proton-coupled symport (H+ cotransport) | GO:0015293 | H+ coupling via E171/E175 required for Neu5Ac translocation | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Biological process | Sialic acid transport (specific) | - | Specific translocation of Neu5Ac across lysosomal membrane | (hu2023themolecularmechanism pages 2-3, hu2023themolecularmechanism pages 3-4) |
| Biological process | Myelination | GO:0042552 | Disrupted myelination underlying hypomyelination phenotype | (sabir2025lysosomalfreesialic pages 13-14) |
| Biological process | Glycosphingolipid metabolic process | GO:0006687 | Altered GSL metabolism observed in iPSC-derived neural cells | (sabir2025lysosomalfreesialic pages 2-3) |
| Cellular component | Lysosome (membrane) | GO:0005765 | Localization of sialin on lysosomal membrane | (schwake2022lysosomalmembranedefects pages 2-2) |


*Table: Table mapping key diseases, genes, residues, cell types, anatomical sites, chemicals, biological processes, and cellular components relevant to Salla disease to common ontologies, with primary supporting context citations for mechanistic and cellular evidence.*

References

1. (hu2023themolecularmechanism pages 2-3): Wenxin Hu, Congwu Chi, Kunhua Song, and Hongjin Zheng. The molecular mechanism of sialic acid transport mediated by sialin. Science Advances, Jan 2023. URL: https://doi.org/10.1126/sciadv.ade8346, doi:10.1126/sciadv.ade8346. This article has 25 citations and is from a highest quality peer-reviewed journal.

2. (hu2023themolecularmechanism pages 3-4): Wenxin Hu, Congwu Chi, Kunhua Song, and Hongjin Zheng. The molecular mechanism of sialic acid transport mediated by sialin. Science Advances, Jan 2023. URL: https://doi.org/10.1126/sciadv.ade8346, doi:10.1126/sciadv.ade8346. This article has 25 citations and is from a highest quality peer-reviewed journal.

3. (schwake2022lysosomalmembranedefects pages 2-2): Michael Schwake and Paul Saftig. Lysosomal membrane defects. Lysosomal Storage Disorders, pages 232-240, Jul 2022. URL: https://doi.org/10.1002/9781119697312.ch21, doi:10.1002/9781119697312.ch21. This article has 2 citations.

4. (hu2023themolecularmechanism pages 1-2): Wenxin Hu, Congwu Chi, Kunhua Song, and Hongjin Zheng. The molecular mechanism of sialic acid transport mediated by sialin. Science Advances, Jan 2023. URL: https://doi.org/10.1126/sciadv.ade8346, doi:10.1126/sciadv.ade8346. This article has 25 citations and is from a highest quality peer-reviewed journal.

5. (sabir2025lysosomalfreesialic pages 2-3): M. Sabir, V. Jovanovic, Seungmi Ryu, Chaitali Sen, Pinar Ormanoglu, Laura Pollard, Richard Steet, William A. Gahl, M. Huizing, Carlos A. Tristan, Frances M. Platt, and M. Malicdan. Lysosomal free sialic acid storage disorder ipsc-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-12682-4, doi:10.1038/s41598-025-12682-4. This article has 2 citations and is from a peer-reviewed journal.

6. (sabir2025lysosomalfreesialic pages 1-2): M. Sabir, V. Jovanovic, Seungmi Ryu, Chaitali Sen, Pinar Ormanoglu, Laura Pollard, Richard Steet, William A. Gahl, M. Huizing, Carlos A. Tristan, Frances M. Platt, and M. Malicdan. Lysosomal free sialic acid storage disorder ipsc-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-12682-4, doi:10.1038/s41598-025-12682-4. This article has 2 citations and is from a peer-reviewed journal.

7. (sabir2025lysosomalfreesialic pages 12-13): M. Sabir, V. Jovanovic, Seungmi Ryu, Chaitali Sen, Pinar Ormanoglu, Laura Pollard, Richard Steet, William A. Gahl, M. Huizing, Carlos A. Tristan, Frances M. Platt, and M. Malicdan. Lysosomal free sialic acid storage disorder ipsc-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-12682-4, doi:10.1038/s41598-025-12682-4. This article has 2 citations and is from a peer-reviewed journal.

8. (sabir2025lysosomalfreesialic pages 13-14): M. Sabir, V. Jovanovic, Seungmi Ryu, Chaitali Sen, Pinar Ormanoglu, Laura Pollard, Richard Steet, William A. Gahl, M. Huizing, Carlos A. Tristan, Frances M. Platt, and M. Malicdan. Lysosomal free sialic acid storage disorder ipsc-derived neural cells display altered glycosphingolipid metabolism. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-12682-4, doi:10.1038/s41598-025-12682-4. This article has 2 citations and is from a peer-reviewed journal.