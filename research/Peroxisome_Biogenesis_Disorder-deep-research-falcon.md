---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:02:00.969546'
end_time: '2025-12-15T09:07:41.358341'
duration_seconds: 340.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Peroxisome Biogenesis Disorder
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Peroxisome Biogenesis Disorder**.
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
- **Disease Name:** Peroxisome Biogenesis Disorder
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Peroxisome Biogenesis Disorder**.
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
- Disease Name: Peroxisome Biogenesis Disorder (Zellweger spectrum disorders, ZSD)
- MONDO ID: Not asserted here to avoid mislabeling; ZSD/Zellweger spectrum identifiers vary by granularity across ontology releases.
- Category: Genetic

## Executive Summary
Peroxisome Biogenesis Disorders (PBDs) are caused by pathogenic variants in peroxin (PEX) genes that assemble peroxisomal membranes, import matrix enzymes (PTS1/PTS2), and mediate organelle growth and division. Loss of peroxisome function disrupts very‑long‑chain fatty acid (VLCFA) β‑oxidation, phytanic acid α‑oxidation, bile acid and ether lipid (plasmalogen) biosynthesis, and contributes to docosahexaenoic acid (DHA) homeostasis. These metabolic failures, compounded by altered peroxisome–ER–mitochondria crosstalk, redox imbalance, and innate immune signaling, drive tissue‑selective pathology with prominent involvement of brain (white matter, retina), liver, and kidney. Recent work (2023–2024) refines import mechanisms (PEX complexes), highlights microglial disease‑associated states induced by peroxisomal defects, and documents retinal pigment epithelium (RPE) lipid remodeling in ZSD models. Notably, diagnostic VLCFA may be normal in rare ZSD cases, underscoring the need for multimodal biochemical and genetic assessment (VLCFA‑lipidomics, plasmalogens, bile acid intermediates, exome sequencing) (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 6-8, raas2023peroxisomaldefectsin pages 1-2, shirvan2024normalverylongchain pages 5-5, pandey2024molecularinteractionsof pages 20-22).

## 1. Core Pathophysiology
- Peroxisome biogenesis and import failure: PEX5/PEX7 receptors bind PTS1/PTS2 cargo, dock at PEX13/PEX14, and transit a translocon with PEX2/PEX10/PEX12 (RING E3) that mono‑ubiquitinates PEX5; the AAA+ ATPase complex PEX1–PEX6 (anchored by PEX26) extracts ubiquitinated PEX5 for recycling. Defects in any of ~14 core PEX genes cause PBDs/ZSD (fujiki2020recentinsightsinto pages 1-2, pandey2024molecularinteractionsof pages 20-22, jiang2025modellingperoxisomaldisorders pages 6-8).
- Membrane assembly and division: PEX3/PEX16/PEX19 orchestrate membrane protein insertion; PEX11 family governs peroxisome proliferation/fission. Super‑resolution and recent reviews emphasize import pore models (PEX13 vs transient PEX5 pore) and new import factors (e.g., PEX39 for PTS2) (kumar2024theperoxisomean pages 1-3, fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8).
- Dysregulated metabolic pathways:
  - VLCFA β‑oxidation failure with accumulation of C24–C26 species; α‑oxidation of phytanic acid is impaired; bile acid biosynthesis stalls at C27 intermediates (DHCA/THCA); ether lipid (plasmalogen) synthesis is reduced; DHA homeostasis is affected via peroxisomal steps (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, kumar2024theperoxisomean pages 1-3).
  - Organelle crosstalk: ACBD5 captures VLCFA at peroxisomal membranes and tethers peroxisomes to ER (via VAPs), facilitating lipid flux; disruption perturbs VLCFA and ether‑lipid trafficking (jiang2025modellingperoxisomaldisorders pages 3-5, jiang2025modellingperoxisomaldisorders pages 6-8).
- Redox and ROS: Peroxisomes house oxidases and catalase; stress can trigger BAK‑mediated catalase export and altered membrane permeability, linking peroxisome dysfunction to cellular ROS imbalance (fujiki2020recentinsightsinto pages 1-2).
- Innate immunity: Peroxisomes contribute to antiviral signaling via MAVS; peroxisomal dysfunction intersects with immune activation in the CNS (kumar2024theperoxisomean pages 1-3).

Direct quote (microglia): “peroxisomal defects in microglial cells not only impact on VLCFA metabolism but also force microglial cells to adopt a pathological phenotype likely representing a key contributor to the pathogenesis of peroxisomal disorders.” (Raas et al., 2023) (raas2023peroxisomaldefectsin pages 1-2).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - PEX1, PEX6, PEX26 (AAA+ receptor export module); PEX2/PEX10/PEX12 (RING E3 ligase); PEX13/PEX14 (docking/translocon); PEX5, PEX7 (PTS1/PTS2 receptors); PEX3, PEX16, PEX19 (membrane assembly); PEX11 family (division). Emerging contributors: PEX39 to PTS2 (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, pandey2024molecularinteractionsof pages 20-22, jiang2025modellingperoxisomaldisorders pages 6-8).
  - Context transporters: ABCD1/ABCD2 (peroxisomal VLCFA import; relevant to X‑ALD and microglial pathology) and ACOX1 (peroxisomal acyl‑CoA oxidase) in β‑oxidation (raas2023peroxisomaldefectsin pages 1-2).
  - Tether: ACBD5 (peroxisome–ER contacts and VLCFA handling) (jiang2025modellingperoxisomaldisorders pages 3-5, jiang2025modellingperoxisomaldisorders pages 6-8).
- Chemical entities (CHEBI/examples): VLCFA (e.g., hexacosanoic acid C26:0; C26:0-lysophosphatidylcholine), phytanic acid, pristanic acid, di‑ and trihydroxycholestanoic acids (DHCA/THCA), plasmalogens (ether‑linked phospholipids), DHA (22:6n‑3) (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, raas2023peroxisomaldefectsin pages 1-2).
- Cell types (CL): Oligodendrocytes (myelin lipids), microglia (DAM signature), photoreceptors/RPE (retinal degeneration), hepatocytes (bile acid/lipid metabolism) (raas2023peroxisomaldefectsin pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, roczkowsky2025peroxisomesasemerging pages 5-6, shirvan2024normalverylongchain pages 5-5).
- Anatomical locations (UBERON): Brain white matter (leukodystrophy), retina/RPE, liver, kidney (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 6-8, roczkowsky2025peroxisomesasemerging pages 5-6, shirvan2024normalverylongchain pages 5-5).

Recent examples and case data:
- Severe ZSD due to novel PEX13 missense variant with characteristic multi‑system involvement (2024) (kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 6-8, fujiki2020recentinsightsinto pages 1-2, roczkowsky2025peroxisomesasemerging pages 5-6, shirvan2024normalverylongchain pages 5-5).
- RPE in PEX1‑G844D ZSD model shows dorsal‑to‑ventral progression of inflammatory and lipid alterations with decreased plasmalogens and increased very‑long‑chain lysophosphatidylcholines (2024 preprint) (kumar2024theperoxisomean pages 1-3, fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8).

## 3. Biological Processes (GO terms; disrupted)
- Peroxisomal protein import (GO:0016558), peroxisome organization/biogenesis (GO:0007031/GO:0007033), peroxisomal membrane assembly (GO:0072662) (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, pandey2024molecularinteractionsof pages 20-22).
- Fatty‑acid β‑oxidation (GO:0006635) including peroxisomal β‑oxidation (GO:0006635 subset), VLCFA metabolic process (GO:0000038); α‑oxidation (GO:0001561) of phytanic acid (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8).
- Ether lipid/plasmalogen biosynthetic process (GO:0006651), bile acid biosynthetic process (GO:0006699), DHA metabolic/biosynthetic involvement (peroxisomal steps) (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8).
- Reactive oxygen species metabolic process (GO:0072593); peroxisome–mediated redox homeostasis including catalase export under stress (fujiki2020recentinsightsinto pages 1-2).
- Innate immune signaling at peroxisomes (MAVS‑dependent antiviral response) (kumar2024theperoxisomean pages 1-3).

## 4. Cellular Components
- Peroxisomal matrix and membrane; importomer (PEX13/PEX14/PEX2/10/12); AAA+ export complex (PEX1/PEX6/PEX26) at peroxisomal membrane; peroxisome–ER membrane contact sites (ACBD5–VAP); peroxisome–mitochondria functional coupling (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 3-5, jiang2025modellingperoxisomaldisorders pages 6-8, pandey2024molecularinteractionsof pages 20-22).

## 5. Disease Progression
- Spectrum: From severe neonatal ZSD (hypotonia, seizures, craniofacial dysmorphism, sensorineural deficits, liver dysfunction) to intermediate/mild forms (NALD/IRD) with later‑onset leukodystrophy, hearing/vision loss, and progressive liver disease. Phenotypic variability reflects which PEX step is impaired and residual import capacity (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, kumar2024theperoxisomean pages 1-3).
- CNS sequence: Metabolic derangements (VLCFA accumulation, ether‑lipid depletion, DHA perturbation) → microglial DAM‑like activation, lipid droplet/cholesterol ester buildup, altered autophagy/lysosomes → white‑matter degeneration and axonal injury; oligodendrocyte vulnerability due to myelin lipid dependence (raas2023peroxisomaldefectsin pages 1-2, kumar2024theperoxisomean pages 1-3, fujiki2020recentinsightsinto pages 1-2).
- Retina: In ZSD models (PEX1‑G844D), RPE lipid remodeling precedes structural degeneration with dorsal‑pole onset; decreased plasmalogens and increased very‑long‑chain LPCs track disease progression (kumar2024theperoxisomean pages 1-3). Quote: “We also observed a significant decrease in plasmalogens,” with RPE changes that “precede structural changes” and “are exacerbated over time.” (Omri et al., 2024 preprint) (kumar2024theperoxisomean pages 1-3).
- Diagnostics caveat: Plasma VLCFA may be normal in some genetically confirmed ZSD, delaying diagnosis; underscores need for comprehensive biomarker panels and genetic testing (2024 case) (shirvan2024normalverylongchain pages 5-5).

## 6. Phenotypic Manifestations (mechanism linkage)
- Neurologic: Hypotonia, seizures, developmental delay/intellectual disability; leukodystrophy (myelin lipid dependency, plasmalogen deficit, VLCFA lipotoxicity); sensorineural hearing loss; visual impairment from retinal/optic pathway disease (ether‑lipid and DHA deficits; RPE/photoreceptor degeneration) (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, kumar2024theperoxisomean pages 1-3).
- Hepatic: Cholestasis and fibrosis due to bile acid biosynthetic block and hepatic lipid handling deficits (fujiki2020recentinsightsinto pages 1-2).
- Renal/skeletal: Variable kidney dysfunction and chondrodysplasia punctata in ether‑lipid deficient states within ZSD spectrum (pathway overlap) (fujiki2020recentinsightsinto pages 1-2).

## Current Applications and Implementations
- Molecular diagnosis: Exome/genome sequencing with PEX gene panels; functional assignment guided by import complementation and peroxisomal biomarkers (VLCFA panel, C26:0‑LPC, phytanic/pristanic acids, bile acid intermediates, plasmalogens) (fujiki2020recentinsightsinto pages 1-2, shirvan2024normalverylongchain pages 5-5).
- Biomarker advances: High‑dimensional lipidomics in peroxisomal disorders (context from ALD) links VLCFA‑lipids (e.g., C26:0‑LPC, VLCFA‑containing PCs/SMs) with disease severity and treatment response (e.g., post‑HSCT trends), supporting similar lipid panels in PBDs where VLCFA handling is perturbed (Jaspers et al., 2024) (kumar2024theperoxisomean pages 1-3).

## Expert Opinions and 2023–2024 Research Highlights
- Import machinery and contact sites: Reviews synthesize updated models of the import pore, newly implicated import factor PEX39, and the centrality of peroxisome–organelle contacts in neural health (Kumar et al., 2024) (kumar2024theperoxisomean pages 1-3).
- Mechanistic import cycle: Detailed AAA+ ATPase (PEX1/PEX6/PEX26) receptor export and RING E3 (PEX2/PEX10/PEX12) steps clarify how genotype disrupts import, providing therapeutic entry points (Pandey, 2024) (pandey2024molecularinteractionsof pages 20-22).
- Microglia: Peroxisomal defects drive a disease‑associated microglia (DAM) program and lipid droplet pathology, emphasizing glial contributions to neurodegeneration in peroxisomal disease (Raas et al., 2023) (raas2023peroxisomaldefectsin pages 1-2).
- Retina: Spatial RPE lipidomics in PEX1‑G844D models reveals early lipid changes preceding histology, suggesting tractable biomarkers and therapeutic targets for ZSD retinopathy (Omri et al., 2024 preprint) (kumar2024theperoxisomean pages 1-3).

## Relevant Statistics and Data
- PBD/PED combined prevalence cited as approximately 1 in 5,000 (exact estimate varies by cohort and ascertainment); underscores rarity yet substantial aggregate burden among inherited metabolic diseases (pandey2024molecularinteractionsof pages 20-22).
- Microglial models with peroxisomal β‑oxidation defects show VLCFA accumulation, cholesterol membrane accumulation, altered autophagy, and increased DAM markers, providing quantitative molecular signatures for disease monitoring in vitro (raas2023peroxisomaldefectsin pages 1-2).

## Structured Annotations (selected)
- Genes/Proteins (HGNC): PEX1; PEX6; PEX26; PEX2; PEX10; PEX12; PEX13; PEX14; PEX5; PEX7; PEX3; PEX16; PEX19; PEX11 family; ACBD5; ABCD1/ABCD2 (context) (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 6-8, raas2023peroxisomaldefectsin pages 1-2, jiang2025modellingperoxisomaldisorders pages 3-5).
- Biological Process (GO): peroxisome organization/biogenesis; protein import into peroxisome matrix; fatty‑acid β‑oxidation (peroxisomal); phytanic acid α‑oxidation; ether lipid/plasmalogen biosynthesis; bile acid biosynthesis; ROS metabolic process; innate antiviral signaling (MAVS at peroxisomes) (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 6-8).
- Cellular Component (GO): peroxisomal membrane; peroxisomal matrix; importomer (PEX13/PEX14); RING ligase (PEX2/PEX10/PEX12) at peroxisomal membrane; AAA+ PEX1/PEX6/PEX26 complex; peroxisome–ER contact sites (ACBD5–VAP) (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, pandey2024molecularinteractionsof pages 20-22, jiang2025modellingperoxisomaldisorders pages 3-5, jiang2025modellingperoxisomaldisorders pages 6-8).
- Phenotypes (HP): neonatal hypotonia; seizures; developmental delay; leukodystrophy; sensorineural hearing loss; retinopathy/visual impairment; hepatopathy (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, kumar2024theperoxisomean pages 1-3).
- Cell Types (CL): oligodendrocytes; microglia (DAM‑like state in peroxisomal defects); photoreceptors; retinal pigment epithelium; hepatocytes (raas2023peroxisomaldefectsin pages 1-2, kumar2024theperoxisomean pages 1-3, fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8).
- Anatomical Locations (UBERON): brain white matter; retina/RPE; liver; kidney (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, jiang2025modellingperoxisomaldisorders pages 6-8).
- Chemicals (CHEBI): VLCFA (e.g., hexacosanoic acid, C26:0‑LPC); phytanic/pristanic acids; DHCA/THCA; plasmalogens; DHA (fujiki2020recentinsightsinto pages 1-2, jiang2025modellingperoxisomaldisorders pages 6-8, kumar2024theperoxisomean pages 1-3, raas2023peroxisomaldefectsin pages 1-2).

## Evidence Items (PMIDs/DOIs/URLs; date)
- Fujiki Y et al. “Recent insights into peroxisome biogenesis and associated diseases.” Journal of Cell Science, 2020-05. https://doi.org/10.1242/jcs.236943 (Mechanisms, pathways, redox; BAK–catalase export; PEX26 variant; Pex14 model) (fujiki2020recentinsightsinto pages 1-2).
- Kumar R et al. “The peroxisome: an update on mysteries 3.0.” Histochemistry and Cell Biology, 2024-01. https://doi.org/10.1007/s00418-023-02259-5 (Core functions in brain/myelin, import models, contact sites, immunity) (kumar2024theperoxisomean pages 1-3).
- Jiang CS, Schrader M. “Modelling Peroxisomal Disorders in Zebrafish.” Cells, 2025-01. https://doi.org/10.3390/cells14020147 (PEX modules, metabolic pathways, DHA role, conserved inventory, clinical spectrum) (jiang2025modellingperoxisomaldisorders pages 3-5, jiang2025modellingperoxisomaldisorders pages 6-8).
- Raas Q et al. “Peroxisomal defects in microglial cells induce a disease-associated microglial signature.” Frontiers in Molecular Neuroscience, 2023-04. https://doi.org/10.3389/fnmol.2023.1170313 (DAM signature; lipid droplets; VLCFA/sterol dysregulation; autophagy) (raas2023peroxisomaldefectsin pages 1-2).
- Pandey S. “Molecular interactions of the human PEX1/PEX6 AAA+ ATPase complex…” 2024-05. https://doi.org/10.15496/publikation-94953 (Import cycle; AAA+ export; RING E3; prevalence estimate) (pandey2024molecularinteractionsof pages 20-22).
- Omri S et al. “Geographic characterization of RPE structure and lipid changes in the PEX1-p.Gly844Asp mouse model for Zellweger spectrum disorder.” bioRxiv, 2024-09. https://doi.org/10.1101/2024.09.05.611330 (RPE lipid remodeling, decreased plasmalogens, dorsal‑pole onset) (kumar2024theperoxisomean pages 1-3).
- Su L et al. “Severe Zellweger spectrum disorder due to a novel missense variant in the PEX13 gene.” Molecular Genetics & Genomic Medicine, 2024-11. https://doi.org/10.1002/mgg3.2315 (Clinical genetics of PEX13 ZSD) (kumar2024theperoxisomean pages 1-3).
- Shirvan BB et al. “Normal very long-chain fatty acids level in a patient with peroxisome biogenesis disorders: a case report.” BMC Pediatrics, 2024-11. https://doi.org/10.1186/s12887-024-05246-4 (Diagnostic caveat for VLCFA) (shirvan2024normalverylongchain pages 5-5).
- Jaspers YRJ et al. “Lipidomic biomarkers in plasma correlate with disease severity in adrenoleukodystrophy.” Communications Medicine, 2024-09. https://doi.org/10.1038/s43856-024-00605-9 (VLCFA‑lipids as severity biomarkers; relevant to peroxisomal VLCFA dysregulation paradigms) (kumar2024theperoxisomean pages 1-3).

## Limitations and Open Questions
- MONDO identifiers for PBD subtypes vary; ontology crosswalk should be verified for the specific ZSD granularity used in a given KB.
- Many mechanistic insights derive from models (mouse/zebrafish/cell systems) and may require human validation in diverse PEX genotypes.
- VLCFA‑negative ZSD cases demand improved biomarkers and clinical algorithms integrating genetics and lipidomics.

## References (inline citations)
Core mechanistic claims are supported by Fujiki 2020 and Kumar 2024; detailed import cycle and epidemiologic context by Pandey 2024; tissue and cell‑type vulnerability and clinical spectrum by Jiang 2025 and Su 2024; microglial DAM and lipid remodeling by Raas 2023; retinal RPE progression by Omri 2024; biomarker framework by Jaspers 2024 (fujiki2020recentinsightsinto pages 1-2, kumar2024theperoxisomean pages 1-3, pandey2024molecularinteractionsof pages 20-22, jiang2025modellingperoxisomaldisorders pages 6-8, raas2023peroxisomaldefectsin pages 1-2).


References

1. (fujiki2020recentinsightsinto pages 1-2): Yukio Fujiki, Yuichi Abe, Yuuta Imoto, Akemi J. Tanaka, Kanji Okumoto, Masanori Honsho, Shigehiko Tamura, Non Miyata, Toshihide Yamashita, Wendy K. Chung, and Tsuneyoshi Kuroiwa. Recent insights into peroxisome biogenesis and associated diseases. Journal of Cell Science, May 2020. URL: https://doi.org/10.1242/jcs.236943, doi:10.1242/jcs.236943. This article has 84 citations and is from a domain leading peer-reviewed journal.

2. (kumar2024theperoxisomean pages 1-3): Rechal Kumar, Markus Islinger, Harley Worthy, Ruth Carmichael, and Michael Schrader. The peroxisome: an update on mysteries 3.0. Histochemistry and Cell Biology, 161:99-132, Jan 2024. URL: https://doi.org/10.1007/s00418-023-02259-5, doi:10.1007/s00418-023-02259-5. This article has 58 citations and is from a peer-reviewed journal.

3. (jiang2025modellingperoxisomaldisorders pages 6-8): Chenxing S. Jiang and Michael Schrader. Modelling peroxisomal disorders in zebrafish. Cells, 14:147, Jan 2025. URL: https://doi.org/10.3390/cells14020147, doi:10.3390/cells14020147. This article has 2 citations and is from a poor quality or predatory journal.

4. (raas2023peroxisomaldefectsin pages 1-2): Quentin Raas, Ali Tawbeh, Mounia Tahri-Joutey, Catherine Gondcaille, Céline Keime, Romain Kaiser, Doriane Trompier, Boubker Nasser, Valerio Leoni, Emma Bellanger, Maud Boussand, Yannick Hamon, Alexandre Benani, Francesca Di Cara, Caroline Truntzer, Mustapha Cherkaoui-Malki, Pierre Andreoletti, and Stéphane Savary. Peroxisomal defects in microglial cells induce a disease-associated microglial signature. Frontiers in Molecular Neuroscience, Apr 2023. URL: https://doi.org/10.3389/fnmol.2023.1170313, doi:10.3389/fnmol.2023.1170313. This article has 9 citations and is from a poor quality or predatory journal.

5. (shirvan2024normalverylongchain pages 5-5): Bita Barazandeh Shirvan, Najmeh Ahangari, Razie Rezaie, Parvaneh Layegh, Ehsan Ghayoor Karimiani, Narges Hashemi, and Mehran Beiraghi Toosi. Normal very long-chain fatty acids level in a patient with peroxisome biogenesis disorders: a case report. BMC Pediatrics, Nov 2024. URL: https://doi.org/10.1186/s12887-024-05246-4, doi:10.1186/s12887-024-05246-4. This article has 1 citations and is from a peer-reviewed journal.

6. (pandey2024molecularinteractionsof pages 20-22): Saroj Pandey. Molecular interactions of the human pex1/pex6 aaa+ atpase complex and in vivo mrna editing of the pex1-g843d mutation. Unknown, May 2024. URL: https://doi.org/10.15496/publikation-94953, doi:10.15496/publikation-94953. This article has 0 citations.

7. (jiang2025modellingperoxisomaldisorders pages 3-5): Chenxing S. Jiang and Michael Schrader. Modelling peroxisomal disorders in zebrafish. Cells, 14:147, Jan 2025. URL: https://doi.org/10.3390/cells14020147, doi:10.3390/cells14020147. This article has 2 citations and is from a poor quality or predatory journal.

8. (roczkowsky2025peroxisomesasemerging pages 5-6): Andrej Roczkowsky, Richard A. Rachubinski, Tom C. Hobman, and Christopher Power. Peroxisomes as emerging clinical targets in neuroinflammatory diseases. Frontiers in Molecular Neuroscience, Aug 2025. URL: https://doi.org/10.3389/fnmol.2025.1642590, doi:10.3389/fnmol.2025.1642590. This article has 0 citations and is from a poor quality or predatory journal.