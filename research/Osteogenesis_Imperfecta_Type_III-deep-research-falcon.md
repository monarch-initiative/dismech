---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-04T19:33:44.571328'
end_time: '2026-02-04T19:43:23.978100'
duration_seconds: 579.41
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type III
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type III**.
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
- **Disease Name:** Osteogenesis Imperfecta Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteogenesis Imperfecta Type III**.
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
- Objective 1 (completed): Assemble recent (2023–2024) authoritative sources on OI Type III pathophysiology (Sun 2024; Sillence 2024; Hald 2024; Verdonk 2024; Rapoport 2023) (sun2024emerginglandscapeof pages 18-18, sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 2-3, hald2024osteogenesisimperfectaskeletal pages 11-12, hald2024osteogenesisimperfectaskeletal pages 8-10, verdonk2024isosteogenesisimperfecta pages 1-2, hald2024osteogenesisimperfectaskeletal pages 1-3, sillence2024adyadicnosology pages 11-12).
- Objective 2: Extract core mechanisms/pathways tied to OI Type III severity (completed via evidence synthesis below) (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 9-11, sun2024emerginglandscapeof pages 4-5, sillence2024adyadicnosology pages 17-18).
- Objective 3–4: Catalog key molecular players and map to ontologies (HGNC, GO, CL, UBERON, CHEBI) and cellular components (completed via embedded artifact) (sun2024emerginglandscapeof pages 18-18, sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 2-3, sillence2024adyadicnosology pages 9-11).
- Objective 5: Outline disease progression and phenotype links (completed below) (sun2024emerginglandscapeof pages 2-3, hald2024osteogenesisimperfectaskeletal pages 11-12, sillence2024adyadicnosology pages 11-12, hald2024osteogenesisimperfectaskeletal pages 3-4).
- Objective 6: Create a structured artifact table for knowledge-base use (completed; embedded) (sun2024emerginglandscapeof pages 18-18, sun2024emerginglandscapeof pages 3-4, sillence2024adyadicnosology pages 9-11, verdonk2024isosteogenesisimperfecta pages 1-2).
- Objective 7: Write and submit the comprehensive report (this document).

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Osteogenesis Imperfecta Type III (progressively deforming OI)
- MONDO ID: not specified by source; entry pertains to Mendelian OI classified by Sillence and modern dyadic nosology (sillence2024adyadicnosology pages 11-12).
- Category: Mendelian

1. Core Pathophysiology
Osteogenesis imperfecta (OI) Type III is a severe, progressively deforming phenotype characterized by early and recurrent fractures, extreme short stature, and skeletal deformity. Mechanistically, OI across types is predominantly a collagen type I disorder; “approximately 80–85%” of OI (types I–IV) arises from autosomal-dominant COL1A1/COL1A2 mutations that alter the Gly–X–Y triple helix, perturbing folding, post-translational modifications (PTMs), and fibrillogenesis (Sun 2024, ACS Pharmacol Transl Sci, Jan 2024; DOI: 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 3-4). Type III severity also results from recessive disruptions of the ER-based prolyl 3-hydroxylation/folding complex (P3H1/LEPRE1, CRTAP, PPIB), ER chaperones (SERPINH1/HSP47, FKBP10/FKBP65), ER Ca2+ homeostasis (TMEM38B/TRIC-B), transcriptional regulators of osteoblast differentiation (SP7/Osterix, CREB3L1/OASIS), and WNT1 signaling, as well as extracellular processing (BMP1), cross-linking (PLOD2), and mineralization regulators (SERPINF1/PEDF, IFITM5) (Sun 2024; Sillence 2024, Calcif Tissue Int, Jun 2024; DOI: 10.1007/s00223-024-01248-7) (sun2024emerginglandscapeof pages 2-3, sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 9-11, sun2024emerginglandscapeof pages 4-5, sillence2024adyadicnosology pages 17-18).
- Collagen I misfolding and PTM disruption: Gly substitutions in COL1A1/COL1A2 disrupt helix folding and the timing/extent of proline/lysine hydroxylation and glycosylation during ER assembly, driving matrix weakness and deformity (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 3-4).
- Loss of P3H1–CRTAP–PPIB complex: This ER heterotrimer catalyzes 3-hydroxylation at conserved collagen sites (e.g., Pro986 in α1(I)); loss delays triple-helix formation, leads to excessive alternative modifications, and produces severe growth deficiency and deforming phenotypes consistent with Type III (Sun 2024, Jan 2024; Sillence 2024, Jun 2024; 10.1021/acsptsci.3c00324; 10.1007/s00223-024-01248-7) (sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11, sun2024emerginglandscapeof pages 4-5).
- ER chaperone and trafficking defects: SERPINH1/HSP47 and FKBP10/FKBP65 prevent premature protofibril formation and guide procollagen trafficking; mutations cause “misfolded pre‑collagen molecules,” alter lysine hydroxylation and cross-linking via PLOD2, and reduce collagen assembly (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 17-18).
- ER Ca2+ dysregulation and ER stress: TMEM38B/TRIC-B controls ER Ca2+ flux; loss reduces Ca2+-dependent PTMs, impairs MSC→osteoblast differentiation, and provokes ER stress, compromising osteoblast function (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7).
- Impaired osteoblast differentiation and signaling: SP7 and CREB3L1 regulate osteoblast maturation and collagen expression; WNT1 and MESD (LRP5/6 chaperone) affect canonical WNT/β-catenin signaling in osteoblasts. Disruption in these pathways reduces bone formation and contributes to growth failure and deformity (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 6-7).
- Extracellular processing and mineralization: BMP1 defects impair C-propeptide processing and can cause abnormal mineralization (including hypermineralization). SERPINF1 (PEDF) loss leads to mineralization defects (Type VI OI), and IFITM5 mutations impair PEDF secretion and mineralization, collectively linking matrix processing/mineralization defects to severe fragility (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 4-5, sun2024emerginglandscapeof pages 6-7).
These mechanisms converge in osteoblasts and bone matrix to produce the severe deforming phenotype and extreme short stature typical of Type III (Sun 2024, Jan 2024; Sillence 2024, Jun 2024; 10.1021/acsptsci.3c00324; 10.1007/s00223-024-01248-7) (sun2024emerginglandscapeof pages 2-3, sillence2024adyadicnosology pages 9-11).

2. Key Molecular Players, Cell Types, and Anatomical Sites (ontology-annotated)
- Principal genes/proteins: COL1A1, COL1A2; ER folding/PTM complex (CRTAP, P3H1/LEPRE1, PPIB); ER chaperones (SERPINH1/HSP47, FKBP10/FKBP65, KDELR2); cross-linking/mineralization/processing (PLOD2, BMP1, SERPINF1/PEDF, IFITM5); osteoblast differentiation/signaling (WNT1, SP7, CREB3L1/OASIS, MESD); ER Ca2+ homeostasis (TMEM38B/TRIC-B) (Sun 2024; Sillence 2024) (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 9-11, sun2024emerginglandscapeof pages 4-5, sillence2024adyadicnosology pages 17-18).
- Chemical entities: antiresorptives (bisphosphonates such as pamidronate/zoledronate) widely used in severe OI; sclerostin-pathway biologics under investigation (e.g., romosozumab pediatric Phase 1 completed; NCT04545554) (Sillence 2024, Hald 2024; ClinicalTrials.gov) (sillence2024adyadicnosology pages 9-11, hald2024osteogenesisimperfectaskeletal pages 11-12).
- Cell types: osteoblasts (collagen I synthesis; ER stress/UPR), osteocytes (matrix-embedded mechanosensors), osteoclasts (resorption; coupling imbalance), MSCs (impaired osteogenic differentiation with ER Ca2+ defects) (Sun 2024; Hald 2024) (sun2024emerginglandscapeof pages 3-4, hald2024osteogenesisimperfectaskeletal pages 11-12).
- Anatomical locations: long-bone cortex, vertebral bodies (load-bearing, deformity-prone), growth plate (linear growth failure), aortic root and cardiac valves (extraskeletal collagen I tissues with reported abnormalities) (Sillence 2024; Hald 2024; Verdonk 2024) (sillence2024adyadicnosology pages 11-12, hald2024osteogenesisimperfectaskeletal pages 11-12, verdonk2024isosteogenesisimperfecta pages 1-2).

The following structured table provides ontology-aligned details for knowledge-base ingestion and references.

| Category | Name | Ontology | Identifier | Mechanistic role in OI Type III | Supporting source (DOI/URL) | Year |
|---|---|---|---|---|---|---|
| Gene/Protein | COL1A1 | HGNC | HGNC:COL1A1 | Gly-X-Y Gly substitutions in the α1(I) chain disrupt triple-helix folding, alter PTMs and fibrillogenesis causing severe/deforming phenotype | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4, sillence2024adyadicnosology pages 9-11) | 2024 |
| Gene/Protein | COL1A2 | HGNC | HGNC:COL1A2 | Mutations in α2(I) chain cause helix instability and genotype–phenotype correlation with severe forms (type III) | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4, sillence2024adyadicnosology pages 9-11) | 2024 |
| Gene/Protein | CRTAP | HGNC | HGNC:CRTAP | Component of P3H1–CRTAP–PPIB complex; loss → defective prolyl 3-hydroxylation, delayed helix folding, severe recessive OI | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11) | 2024 |
| Gene/Protein | LEPRE1 (P3H1) | HGNC | HGNC:LEPRE1 | Prolyl 3-hydroxylase (P3H1); required for Pro986 3-hydroxylation of α1(I); loss causes severe growth deficiency and deforming phenotype | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11) | 2024 |
| Gene/Protein | PPIB (CyPB) | HGNC | HGNC:PPIB | Cyclophilin B; part of 3-hydroxylation complex; mutations disrupt complex and collagen PTMs → severe OI | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6) | 2024 |
| Gene/Protein | SERPINH1 (HSP47) | HGNC | HGNC:SERPINH1 | ER chaperone HSP47; mutations → misfolded procollagen and trafficking defects, contributing to severe phenotype | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Gene/Protein | FKBP10 (FKBP65) | HGNC | HGNC:FKBP10 | ER peptidyl-prolyl isomerase; loss alters lysine hydroxylation (PLOD2 activity) and collagen cross-linking → deformity | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Gene/Protein | PLOD2 | HGNC | HGNC:PLOD2 | Lysyl hydroxylase (telopeptide hydroxylation) required for correct collagen cross-links; defects cause progressive deforming phenotypes | https://doi.org/10.1021/acsptsci.3c00324, https://doi.org/10.1007/s00223-024-01248-7 (sun2024emerginglandscapeof pages 3-4, sillence2024adyadicnosology pages 9-11) | 2024 |
| Gene/Protein | BMP1 | HGNC | HGNC:BMP1 | C-propeptide processing metalloprotease; mutations alter procollagen processing and can produce abnormal mineralization/hypermineralization | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 16-17) | 2024 |
| Gene/Protein | WNT1 | HGNC | HGNC:WNT1 | Canonical WNT/β-catenin signaling regulator of osteoblast differentiation; mutations reduce bone formation and contribute to severe OI | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Gene/Protein | SP7 (Osterix) | HGNC | HGNC:SP7 | Transcription factor required for pre-osteoblast → osteoblast maturation; loss impairs osteoblast differentiation and bone formation | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6) | 2024 |
| Gene/Protein | CREB3L1 (OASIS) | HGNC | HGNC:CREB3L1 | ER-to-nucleus transcription factor (RIP-activated) regulating osteoblast genes; mutations linked to severe osteodysplasia and reduced collagen | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 6-7) | 2024 |
| Gene/Protein | TMEM38B (TRIC-B) | HGNC | HGNC:TMEM38B | ER ion channel regulating ER Ca2+ homeostasis; loss → impaired Ca2+-dependent PTMs, ER stress, reduced MSC→osteoblast differentiation | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Gene/Protein | SERPINF1 (PEDF) | HGNC | HGNC:SERPINF1 | Secreted PEDF influences osteoblast mineralization; recessive loss (type VI) causes mineralization defects and fragility | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 4-5) | 2024 |
| Gene/Protein | IFITM5 | HGNC | HGNC:IFITM5 | BRIL protein; pathogenic mutations alter palmitoylation/Golgi localization, impair PEDF secretion and osteoblast mineralization | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 4-5) | 2024 |
| Gene/Protein | KDELR2 | HGNC | HGNC:KDELR2 | ER retrieval receptor; mutations mislocalize HSP47 and reduce HSP47/FKBP65 levels → impaired collagen assembly | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 6-7) | 2024 |
| Gene/Protein | MESD | HGNC | HGNC:MESD | ER chaperone for LRP5/6 trafficking; loss impairs WNT receptor trafficking and downstream osteoblast signaling | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 6-7) | 2024 |
| Biological Process | Collagen fibril organization | GO | GO: collagen fibril organization | Disrupted fibrillogenesis from misfolded collagen and altered cross-linking underlies bone fragility and deformity | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4) | 2024 |
| Biological Process | Prolyl 3-hydroxylation | GO | GO: prolyl 3-hydroxylation | P3H1–CRTAP–PPIB complex normally 3‑hydroxylates Pro986; loss → defective helix stability and severe OI | https://doi.org/10.1021/acsptsci.3c00324, https://doi.org/10.1007/s00223-024-01248-7 (sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11) | 2024 |
| Biological Process | ER protein folding / chaperone activity | GO | GO: ER protein folding | HSP47, FKBP65, CyPB and others ensure procollagen folding; defects produce ER retention/misfolding and UPR/functional osteoblast impairment | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 3-4) | 2024 |
| Biological Process | Unfolded Protein Response (UPR) | GO | GO: UPR / ER stress response | Chronic ER stress from misfolded collagen perturbs osteoblast survival/function contributing to severe phenotype | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6) | 2024 |
| Biological Process | ER calcium homeostasis | GO | GO: ER calcium homeostasis | TMEM38B/TRIC-B defects alter Ca2+ flux, impair Ca2+-dependent PTMs and osteoblast differentiation → skeletal deformity | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Biological Process | Osteoblast differentiation (WNT/β‑catenin) | GO | GO: osteoblast differentiation | WNT1, MESD, SP7 and CREB3L1 disruption reduce osteoblast maturation and matrix production causing growth deficiency | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Biological Process | Extracellular matrix organization | GO | GO: extracellular matrix organization | Abnormal collagen secretion/processing (BMP1, cross‑linking defects) alters ECM structure and mechanical properties | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 16-17) | 2024 |
| Biological Process | Collagen cross-linking | GO | GO: collagen cross-linking | PLOD2 and FKBP10 influence telopeptide hydroxylation and cross-links; defects → weak matrix and progressive deformity | https://doi.org/10.1021/acsptsci.3c00324, https://doi.org/10.1007/s00223-024-01248-7 (sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 9-11) | 2024 |
| Biological Process | Mineralization | GO | GO: biomineralization / mineralization | SERPINF1, IFITM5, BMP1 and abnormal collagen affect mineral deposition, sometimes causing hypomineralization or paradoxical hypermineralization | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 4-5, sun2024emerginglandscapeof pages 6-7) | 2024 |
| Cellular Component | Endoplasmic reticulum (ER) | GO | GO: endoplasmic reticulum | Site of procollagen folding, PTMs and chaperone engagement; central locus of pathology in many Type III cases | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6) | 2024 |
| Cellular Component | ER–Golgi intermediate compartment | GO | GO: ER–Golgi intermediate compartment | Important for procollagen trafficking; perturbation (e.g., KDELR2) alters secretion and assembly | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 6-7) | 2024 |
| Cellular Component | Extracellular matrix / collagen fibril | GO | GO: extracellular matrix / collagen fibril | Final location of collagen; defective assembly yields mechanically weak fibrils and bone fragility | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4) | 2024 |
| Cellular Component | Golgi apparatus | GO | GO: Golgi apparatus | Site for glycosylation/processing of collagen; IFITM5 Golgi sequestration noted to impair osteoblast function | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 4-5) | 2024 |
| Cell Type | Osteoblast | CL | CL:0000189 (osteoblast) | Primary collagen-producing bone cell; ER stress and impaired differentiation in osteoblasts drive Type III severity | https://doi.org/10.1021/acsptsci.3c00324, https://doi.org/10.1007/s00223-024-01236-x (sun2024emerginglandscapeof pages 3-4, hald2024osteogenesisimperfectaskeletal pages 11-12) | 2024 |
| Cell Type | Osteocyte | CL | CL:0001989 (osteocyte) | Embedded bone cell influenced by altered matrix; contributes to bone remodeling signaling imbalance | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4) | 2024 |
| Cell Type | Osteoclast | CL | CL:0000653 (osteoclast) | Resorptive cell; osteoblast–osteoclast imbalance affects net bone mass and deformity risk | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 3-4) | 2024 |
| Cell Type | Bone marrow stromal cell (MSC) | CL | CL:0000711 (MSC) | MSC differentiation into osteoblasts is impaired by ER Ca2+ dysregulation and signaling defects (TMEM38B, WNT pathway) | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 5-6) | 2024 |
| Anatomical Location | Bone cortex (long bone) | UBERON | UBERON:0005924 (long bone cortex) | Principal load‑bearing tissue where abnormal collagen fibrils cause fragility, deformity and fractures (Type III pronounced) | https://doi.org/10.1021/acsptsci.3c00324, https://doi.org/10.1007/s00223-024-01248-7 (sun2024emerginglandscapeof pages 3-4, sillence2024adyadicnosology pages 9-11) | 2024 |
| Anatomical Location | Growth plate | UBERON | UBERON:0002081 (growth plate) | Disrupted collagen/osteoblast function leads to impaired linear growth and extreme short stature in Type III | https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 2-3) | 2024 |
| Anatomical Location | Vertebral body | UBERON | UBERON:0002105 (vertebral body) | Prone to compression fractures and progressive kyphoscoliosis in severe/deforming OI | https://doi.org/10.1007/s00223-024-01236-x (hald2024osteogenesisimperfectaskeletal pages 11-12, hald2024osteogenesisimperfectaskeletal pages 1-3) | 2024 |
| Anatomical Location | Aortic root | UBERON | UBERON:0004217 (aortic root) | Collagen I present in cardiovascular ECM; OI-associated valvular/aortic root abnormalities reported (extraskeletal involvement) | https://doi.org/10.1007/s00223-023-01171-3 (verdonk2024isosteogenesisimperfecta pages 1-2) | 2024 |
| Chemical/Drug | Bisphosphonates (pamidronate, zoledronate) | CHEBI | CHEBI:23688 (bisphosphonate class) | Anti-resorptive therapy widely used to reduce fracture rates and improve mobility in severe OI; long-term adult effects under study | https://doi.org/10.1007/s00223-024-01248-7, https://doi.org/10.1007/s00223-024-01236-x (sillence2024adyadicnosology pages 9-11, hald2024osteogenesisimperfectaskeletal pages 11-12) | 2024 |
| Chemical/Drug | Sclerostin pathway agents (e.g., romosozumab class) | CHEBI | CHEBI: not specific (sclerostin antibody class) | Anabolic/sclerostin-targeting approaches are under investigation to increase bone formation in OI (clinical studies ongoing) | NCT04545554 (romosozumab pediatric study) and reviews https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 18-18, sun2024emerginglandscapeof pages 3-4) | 2024 |


*Table: Concise ontology‑annotated table mapping genes, processes, components, cell types, anatomical sites and therapies implicated in Osteogenesis Imperfecta Type III, with mechanistic roles and 2023–2024 supporting sources (context IDs). This table is designed for knowledge‑base annotation and rapid reference.*

3. Biological Processes (candidate GO annotations)
- Collagen fibril organization; extracellular matrix organization; collagen biosynthetic process; prolyl 3-hydroxylation; collagen cross-linking; ER protein folding; ER Ca2+ homeostasis; unfolded protein response; osteoblast differentiation (WNT/β-catenin); bone mineralization (Sun 2024; Sillence 2024) (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11, sun2024emerginglandscapeof pages 4-5).

4. Cellular Components
- Endoplasmic reticulum; ER–Golgi intermediate compartment; Golgi apparatus; extracellular matrix and collagen fibril; osteoblast/osteocyte lacuno-canalicular system (Sun 2024; Sillence 2024) (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11).

5. Disease Progression: Sequence of Events
- Initiation: Genetic variants affecting collagen I (COL1A1/COL1A2) or collagen processing/folding (CRTAP, P3H1, PPIB; SERPINH1/FKBP10; TMEM38B; BMP1; PLOD2) or osteoblast signaling/differentiation (WNT1, SP7, CREB3L1) (Sun 2024; Sillence 2024) (sun2024emerginglandscapeof pages 3-4, sillence2024adyadicnosology pages 9-11).
- Cellular dysfunction: Misfolded collagen and delayed helix formation; abnormal PTMs and cross-linking; ER retention and ER stress/UPR; reduced osteoblast differentiation and ECM production; aberrant mineralization (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7, sun2024emerginglandscapeof pages 4-5).
- Tissue-level consequences: Weak collagen fibrils and disorganized ECM lead to frequent fractures, vertebral compression, progressive deformity, and growth plate dysfunction with extreme short stature—defining the Type III phenotype (Sillence 2024, Jun 2024; 10.1007/s00223-024-01248-7) (sillence2024adyadicnosology pages 11-12, sillence2024adyadicnosology pages 9-11).
- Systemic/extra-skeletal: Collagen I defects extend to cardiovascular tissues; a systematic review found “valvular disease, heart failure, atrial fibrillation, and hypertension” more prevalent in OI, with “a larger aortic root” vs controls; abnormalities occur “in all types of OI and at all ages,” though progression is unclear (Verdonk 2024, Jan 2024; 10.1007/s00223-023-01171-3) (verdonk2024isosteogenesisimperfecta pages 1-2).
- Modern outcomes: Historically high pediatric respiratory mortality in severe OI has been markedly reduced with multidisciplinary care and cyclic IV bisphosphonates (pre-bisphosphonate era estimate: “60% of children died from respiratory failure before their 18th birthday”) (Sillence 2024, Jun 2024; 10.1007/s00223-024-01248-7) (sillence2024adyadicnosology pages 11-12).

6. Phenotypic Manifestations and Clinical Correlates
- Core skeletal: Severe, progressively deforming bone disease with recurrent fractures, extreme short stature, and kyphoscoliosis/vertebral compression (Sillence 2024; Hald 2024) (sillence2024adyadicnosology pages 11-12, hald2024osteogenesisimperfectaskeletal pages 11-12).
- Spine and joints: Scoliosis reported in 26–76% across ages; ligament laxity and early osteoarthritis contribute to pain and disability (Hald 2024, Jun 2024; 10.1007/s00223-024-01236-x) (hald2024osteogenesisimperfectaskeletal pages 3-4, hald2024osteogenesisimperfectaskeletal pages 8-10).
- Extraskeletal: Hearing loss, dental anomalies (dentinogenesis imperfecta), ocular signs (blue sclerae), cardiopulmonary involvement likely beyond skeletal deformity effects (Hald 2024; Verdonk 2024) (hald2024osteogenesisimperfectaskeletal pages 11-12, verdonk2024isosteogenesisimperfecta pages 1-2).
- Patient-reported burden and adult outcomes: Cross-sectional data report 41.8% chronic pain and ~65% at least moderate fatigue; health-related quality of life reduction is mainly physical; median lifespan 72.4 years (men) and 77.4 years (women) (Hald 2024, Jun 2024; 10.1007/s00223-024-01236-x) (hald2024osteogenesisimperfectaskeletal pages 6-8, hald2024osteogenesisimperfectaskeletal pages 1-3).

Expert Opinions and 2023–2024 Reviews
- Dyadic nosology emphasizes pairing genotype with Sillence phenotypes to reflect matrix biology and genomic complexity (>40 OI/bone fragility genes), providing a modern classification framework (Sillence 2024, Jun 2024; 10.1007/s00223-024-01248-7) (sillence2024adyadicnosology pages 11-12).
- Contemporary adult-focused review argues OI is a systemic disease with significant adult musculoskeletal and extraskeletal morbidity and calls for longitudinal registries to define cardiovascular and other risks (Hald 2024, Jun 2024; 10.1007/s00223-024-01236-x) (hald2024osteogenesisimperfectaskeletal pages 1-3, hald2024osteogenesisimperfectaskeletal pages 11-12, hald2024osteogenesisimperfectaskeletal pages 6-8).
- Mechanistic synthesis (Sun 2024) highlights convergence of collagen I misfolding, ER proteostasis (folding/PTMs, Ca2+ homeostasis), extracellular processing/cross-linking, and osteoblast differentiation signaling (WNT1/SP7/CREB3L1) as drivers of severe deforming phenotypes with growth deficiency (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 18-18, sun2024emerginglandscapeof pages 6-7, sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 3-4).
- Cardiovascular systematic review recommends “low-threshold” cardiology referral given increased prevalence of valvular disease, heart failure, AF, hypertension, and larger aortic root, but notes lack of longitudinal progression data (Verdonk 2024, Jan 2024; 10.1007/s00223-023-01171-3) (verdonk2024isosteogenesisimperfecta pages 1-2).

Current Applications and Real-world Implementations
- Pharmacologic: Cyclic IV bisphosphonates remain standard in severe pediatric OI within multidisciplinary programs, improving mobility and survival (Sillence 2024, Jun 2024; Hald 2024, Jun 2024) (sillence2024adyadicnosology pages 11-12, hald2024osteogenesisimperfectaskeletal pages 11-12). Adult long-term effects and antifracture efficacy remain under evaluation (Hald 2024) (hald2024osteogenesisimperfectaskeletal pages 3-4).
- Anabolic/sclerostin pathway: Pediatric Phase 1 study of romosozumab in OI completed (NCT04545554; ClinicalTrials.gov), reflecting translational application of WNT pathway biology; broader efficacy/safety across subtypes (including Type III) remain areas of active research (sun2024emerginglandscapeof pages 18-18).
- Multisystem care: Adult care increasingly addresses cardiopulmonary, neuromuscular, dental/oral, and women’s health domains in addition to bone, with emphasis on registries and standardized outcomes (Hald 2024; Rapoport 2023, Orphanet J Rare Dis, Feb 2023; 10.1186/s13023-023-02627-3) (hald2024osteogenesisimperfectaskeletal pages 11-12, hald2024osteogenesisimperfectaskeletal pages 8-10).

Selected Direct Quotes
- “Approximately 80–85%” of OI (types I–IV) arise from autosomal‑dominant COL1A1/COL1A2 variants disrupting the triple-helix (Sun 2024, Jan 2024; 10.1021/acsptsci.3c00324) (sun2024emerginglandscapeof pages 3-4).
- “Valvular disease, heart failure, atrial fibrillation, and hypertension appear to be more prevalent in OI… [and] a larger aortic root was observed in OI compared to controls” (Verdonk 2024, Jan 2024; 10.1007/s00223-023-01171-3) (verdonk2024isosteogenesisimperfecta pages 1-2).
- “In the pre-bisphosphonate era, 60% of children died from respiratory failure before their 18th birthday” (Sillence 2024, Jun 2024; 10.1007/s00223-024-01248-7) (sillence2024adyadicnosology pages 11-12).

Ontology Annotations (examples)
- Genes/Proteins (HGNC): COL1A1; COL1A2; CRTAP; LEPRE1/P3H1; PPIB; SERPINH1; FKBP10; PLOD2; BMP1; WNT1; SP7; CREB3L1; TMEM38B; SERPINF1; IFITM5 (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sun2024emerginglandscapeof pages 6-7, sillence2024adyadicnosology pages 9-11).
- Biological Processes (GO): collagen fibril organization; prolyl 3‑hydroxylation; ER protein folding; UPR; ER Ca2+ homeostasis; osteoblast differentiation (WNT/β‑catenin); ECM organization; collagen cross-linking; mineralization (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11, sun2024emerginglandscapeof pages 4-5).
- Cellular Components (GO): endoplasmic reticulum; ER–Golgi intermediate compartment; Golgi apparatus; extracellular matrix/collagen fibril (sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 5-6, sillence2024adyadicnosology pages 9-11).
- Cell Types (CL): osteoblast (CL:0000189); osteocyte (CL:0001989); osteoclast (CL:0000653); bone-marrow stromal cell (CL:0000711) (sun2024emerginglandscapeof pages 3-4, hald2024osteogenesisimperfectaskeletal pages 11-12).
- Anatomical Locations (UBERON): long bone cortex (UBERON:0005924); vertebral body (UBERON:0002105); growth plate (UBERON:0002081); aortic root (UBERON:0004217) (sillence2024adyadicnosology pages 11-12, hald2024osteogenesisimperfectaskeletal pages 11-12, verdonk2024isosteogenesisimperfecta pages 1-2).
- Chemical Entities (CHEBI): bisphosphonates (CHEBI:23688); sclerostin‑pathway monoclonal antibodies (class) (sillence2024adyadicnosology pages 9-11, hald2024osteogenesisimperfectaskeletal pages 11-12).

References (URLs and dates)
- Sun Y et al. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS Pharmacol Transl Sci. Jan 2024. https://doi.org/10.1021/acsptsci.3c00324 (sun2024emerginglandscapeof pages 18-18, sun2024emerginglandscapeof pages 6-7, sun2024emerginglandscapeof pages 4-5, sun2024emerginglandscapeof pages 3-4, sun2024emerginglandscapeof pages 2-3, sun2024emerginglandscapeof pages 5-6).
- Sillence DO. A Dyadic Nosology for Osteogenesis Imperfecta and Bone Fragility Syndromes 2024. Calcif Tissue Int. Jun 2024. https://doi.org/10.1007/s00223-024-01248-7 (sillence2024adyadicnosology pages 11-12, sillence2024adyadicnosology pages 9-11, sillence2024adyadicnosology pages 16-17, sillence2024adyadicnosology pages 17-18).
- Hald JD et al. Osteogenesis imperfecta: skeletal and non-skeletal challenges in adulthood. Calcif Tissue Int. Jun 2024. https://doi.org/10.1007/s00223-024-01236-x (hald2024osteogenesisimperfectaskeletal pages 11-12, hald2024osteogenesisimperfectaskeletal pages 8-10, hald2024osteogenesisimperfectaskeletal pages 1-3, hald2024osteogenesisimperfectaskeletal pages 6-8, hald2024osteogenesisimperfectaskeletal pages 3-4).
- Verdonk SJE et al. Is Osteogenesis Imperfecta Associated with Cardiovascular Abnormalities? Calcif Tissue Int. Jan 2024. https://doi.org/10.1007/s00223-023-01171-3 (verdonk2024isosteogenesisimperfecta pages 1-2).
- Rapoport M et al. The patient clinical journey and socioeconomic impact of osteogenesis imperfecta: a systematic scoping review. Orphanet J Rare Dis. Feb 2023. https://doi.org/10.1186/s13023-023-02627-3 (hald2024osteogenesisimperfectaskeletal pages 8-10).
- ClinicalTrials.gov. Study to Evaluate Romosozumab in Children and Adolescents With Osteogenesis Imperfecta (NCT04545554). Status: Completed. https://clinicaltrials.gov/study/NCT04545554 (sun2024emerginglandscapeof pages 18-18).

Limitations and evidence gaps
- Quantitative measurements of ER stress/UPR activation and specific pathway fluxes in human Type III osteoblasts remain limited in 2023–2024 sources reviewed here; most evidence integrates genetic mechanisms, cellular models, and clinical correlation (Sun 2024; Hald 2024) (sun2024emerginglandscapeof pages 18-18, hald2024osteogenesisimperfectaskeletal pages 11-12). Longitudinal cardiovascular risk trajectories lack robust data, despite higher observed prevalences (Verdonk 2024) (verdonk2024isosteogenesisimperfecta pages 1-2).

References

1. (sun2024emerginglandscapeof pages 18-18): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

2. (sun2024emerginglandscapeof pages 3-4): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

3. (sun2024emerginglandscapeof pages 2-3): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

4. (hald2024osteogenesisimperfectaskeletal pages 11-12): Jannie Dahl Hald, Bente Langdahl, Lars Folkestad, Lena Lande Wekre, Riley Johnson, Sandesh C. S. Nagamani, Cathleen Raggio, Stuart H. Ralston, Oliver Semler, Laura Tosi, and Eric Orwoll. Osteogenesis imperfecta: skeletal and non-skeletal challenges in adulthood. Calcified Tissue International, 115:863-872, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01236-x, doi:10.1007/s00223-024-01236-x. This article has 12 citations and is from a peer-reviewed journal.

5. (hald2024osteogenesisimperfectaskeletal pages 8-10): Jannie Dahl Hald, Bente Langdahl, Lars Folkestad, Lena Lande Wekre, Riley Johnson, Sandesh C. S. Nagamani, Cathleen Raggio, Stuart H. Ralston, Oliver Semler, Laura Tosi, and Eric Orwoll. Osteogenesis imperfecta: skeletal and non-skeletal challenges in adulthood. Calcified Tissue International, 115:863-872, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01236-x, doi:10.1007/s00223-024-01236-x. This article has 12 citations and is from a peer-reviewed journal.

6. (verdonk2024isosteogenesisimperfecta pages 1-2): Sara J. E. Verdonk, Silvia Storoni, Dimitra Micha, Joost G. van den Aardweg, Paolo Versacci, Luca Celli, Ralph de Vries, Lidiia Zhytnik, Otto Kamp, Marianna Bugiani, and Elisabeth M. W. Eekhoff. Is osteogenesis imperfecta associated with cardiovascular abnormalities? a systematic review of the literature. Calcified Tissue International, 114:210-221, Jan 2024. URL: https://doi.org/10.1007/s00223-023-01171-3, doi:10.1007/s00223-023-01171-3. This article has 17 citations and is from a peer-reviewed journal.

7. (hald2024osteogenesisimperfectaskeletal pages 1-3): Jannie Dahl Hald, Bente Langdahl, Lars Folkestad, Lena Lande Wekre, Riley Johnson, Sandesh C. S. Nagamani, Cathleen Raggio, Stuart H. Ralston, Oliver Semler, Laura Tosi, and Eric Orwoll. Osteogenesis imperfecta: skeletal and non-skeletal challenges in adulthood. Calcified Tissue International, 115:863-872, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01236-x, doi:10.1007/s00223-024-01236-x. This article has 12 citations and is from a peer-reviewed journal.

8. (sillence2024adyadicnosology pages 11-12): David Owen Sillence. A dyadic nosology for osteogenesis imperfecta and bone fragility syndromes 2024. Calcified Tissue International, 115:873-890, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01248-7, doi:10.1007/s00223-024-01248-7. This article has 29 citations and is from a peer-reviewed journal.

9. (sun2024emerginglandscapeof pages 5-6): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

10. (sun2024emerginglandscapeof pages 6-7): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

11. (sillence2024adyadicnosology pages 9-11): David Owen Sillence. A dyadic nosology for osteogenesis imperfecta and bone fragility syndromes 2024. Calcified Tissue International, 115:873-890, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01248-7, doi:10.1007/s00223-024-01248-7. This article has 29 citations and is from a peer-reviewed journal.

12. (sun2024emerginglandscapeof pages 4-5): Yu Sun, Lin Li, Jiajun Wang, Huiting Liu, and Hu Wang. Emerging landscape of osteogenesis imperfecta pathogenesis and therapeutic approaches. ACS pharmacology & translational science, 7 1:72-96, Jan 2024. URL: https://doi.org/10.1021/acsptsci.3c00324, doi:10.1021/acsptsci.3c00324. This article has 17 citations and is from a peer-reviewed journal.

13. (sillence2024adyadicnosology pages 17-18): David Owen Sillence. A dyadic nosology for osteogenesis imperfecta and bone fragility syndromes 2024. Calcified Tissue International, 115:873-890, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01248-7, doi:10.1007/s00223-024-01248-7. This article has 29 citations and is from a peer-reviewed journal.

14. (hald2024osteogenesisimperfectaskeletal pages 3-4): Jannie Dahl Hald, Bente Langdahl, Lars Folkestad, Lena Lande Wekre, Riley Johnson, Sandesh C. S. Nagamani, Cathleen Raggio, Stuart H. Ralston, Oliver Semler, Laura Tosi, and Eric Orwoll. Osteogenesis imperfecta: skeletal and non-skeletal challenges in adulthood. Calcified Tissue International, 115:863-872, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01236-x, doi:10.1007/s00223-024-01236-x. This article has 12 citations and is from a peer-reviewed journal.

15. (sillence2024adyadicnosology pages 16-17): David Owen Sillence. A dyadic nosology for osteogenesis imperfecta and bone fragility syndromes 2024. Calcified Tissue International, 115:873-890, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01248-7, doi:10.1007/s00223-024-01248-7. This article has 29 citations and is from a peer-reviewed journal.

16. (hald2024osteogenesisimperfectaskeletal pages 6-8): Jannie Dahl Hald, Bente Langdahl, Lars Folkestad, Lena Lande Wekre, Riley Johnson, Sandesh C. S. Nagamani, Cathleen Raggio, Stuart H. Ralston, Oliver Semler, Laura Tosi, and Eric Orwoll. Osteogenesis imperfecta: skeletal and non-skeletal challenges in adulthood. Calcified Tissue International, 115:863-872, Jun 2024. URL: https://doi.org/10.1007/s00223-024-01236-x, doi:10.1007/s00223-024-01236-x. This article has 12 citations and is from a peer-reviewed journal.