---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-01T12:42:04.639173'
end_time: '2026-02-01T12:46:31.619413'
duration_seconds: 266.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neuroblastoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Neuroblastoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Neuroblastoma**.
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
- **Disease Name:** Neuroblastoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Neuroblastoma**.
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
- Disease Name: Neuroblastoma
- MONDO ID: MONDO:0007737
- Category: Pediatric embryonal solid tumor of the sympathetic nervous system

Pathophysiology description
Neuroblastoma (NB) arises from neural crest–derived sympathoadrenal lineage cells and exhibits marked inter- and intra-tumoral heterogeneity. Despite a low tumor mutational burden, disease biology is driven by a limited set of recurrent genomic and epigenomic programs that confer proliferative advantage, telomere immortality, lineage/cell-state plasticity, and an immunologically “cold” tumor microenvironment.

- Genomic drivers and copy-number programs: High-risk NB is frequently defined by MYCN amplification, TERT activation (via rearrangements or copy-number mechanisms), and ATRX alterations, together with segmental chromosomal aberrations including 1p deletion, 11q deletion, and 17q gain; collectively these shape aggressive phenotypes despite overall few point mutations (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3). Telomere programs and copy-number dosage have pervasive effects on transcriptional control and disease pathways; recurrent 11q loss with 17q gain correlates with upregulation of histone variant genes and reduced PRC2 activity, providing a mechanistic route to ALT activation in a subset, while TERT overexpression can be driven by rearrangements and dosage in others (URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024) (burkert2024copynumberdosageregulates pages 18-24).

- Telomere maintenance mechanisms (TMM): High-risk NB nearly always acquires a telomere maintenance mechanism. Two non-overlapping solutions dominate: telomerase activation (often via TERT rearrangement or MYCN-driven TERT transcription) and the alternative lengthening of telomeres (ALT), frequently associated with ATRX dysfunction and chromatin changes at telomeres. Allele-specific dosage and copy-number imbalances further tune TERT levels and ALT-associated programs, linking segmental CNAs to TMM state and outcome (URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024) (burkert2024copynumberdosageregulates pages 18-24); overview also summarized in an immunotherapy-focused review (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3).

- Lineage/cell-state plasticity: NB cells switch between two epigenetically-defined identities—noradrenergic (ADRN) and mesenchymal (MES)—with distinct core regulatory circuitries (ADRN: PHOX2A/PHOX2B, HAND1/2, GATA2/3; MES: AP-1–programs). Transitions are spontaneous and reversible and are shaped by tumor microenvironmental cues; MES-like states are enriched during or after therapy and confer chemoresistance, while in patient tumors the dominant phenotype is often ADRN with subclonal MES-like populations (URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023) (thirant2023reversibletransitionsbetween pages 1-2). Targeted depletion of SWI/SNF ATPases (SMARCA2/4) compacts cis-regulatory elements, displaces ADRN core TFs (e.g., MYCN, HAND2, PHOX2B, GATA3), reduces enhancer activity, inhibits invasion, and—critically—reduces cellular plasticity, positioning SWI/SNF as a mechanistic driver of lineage flexibility and a therapeutic node (URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024) (xu2024targetingswisnfatpases pages 1-2). Additional reviews integrating single-cell multi-omics emphasize ADRN↔MES plasticity, persister states at relapse, and the developmental origin of state diversity (URL: https://doi.org/10.3389/fimmu.2025.1637626, Jul 2025; URL: https://doi.org/10.1038/s41388-025-03635-2, Nov 2025) (wang2025emergingfrontiersin pages 6-7, he2025dissectingneuroblastomaheterogeneity pages 6-7).

- Tumor microenvironment (TME) and immune evasion: NB is typically immunologically “cold,” with low neoantigen load, downregulated MHC class I and antigen processing, and abundant immunosuppressive myeloid populations (TAMs, MDSCs) and Tregs. Additional barriers include CD47-mediated phagocytosis inhibition, inhibitory checkpoints (e.g., B7-H3, PD-L1), and metabolic constraints. These features limit T cell infiltration and efficacy of checkpoint inhibition and shape responses to GD2-directed therapies (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3). Combining chemotherapy and immunotherapy to deliberately exploit ADRN–MES plasticity (e.g., inducing more immunogenic MES features or immunogenic cell death) is a proposed strategy to overcome immune evasion and resistance (URL: https://doi.org/10.3389/fimmu.2023.1268645, Oct 2023) (d’amico2023twobulletsin pages 6-7). Broader pediatric-oncology reviews concur that epigenetic dysregulation (PRC2 imbalance, DNA hypomethylation) intersects with immune coldness, suggesting epigenetic modulators may prime NB for immunotherapy (URL: https://doi.org/10.3389/fimmu.2025.1637626, Jul 2025) (wang2025emergingfrontiersin pages 1-2).

Key concepts and definitions with current understanding
- Segmental chromosomal aberrations (SCA): Partial arm gains/losses (e.g., 17q gain, 1p and 11q loss) that correlate with high-risk disease, telomere program activation, and poor outcome (URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024) (burkert2024copynumberdosageregulates pages 18-24).
- Telomere maintenance mechanisms: Mutually exclusive telomerase activation vs ALT in most tumors; in NB, TERT activation (via rearrangements/MYCN) or ALT (often ATRX-linked) is a hallmark of high-risk biology (URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024) (burkert2024copynumberdosageregulates pages 18-24).
- Core regulatory circuitry (CRC): Super-enhancer–anchored TF networks defining cell identity; ADRN CRC includes PHOX2B/HAND2/GATA3 and is displaced by mSWI/SNF ATPase degradation (URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024) (xu2024targetingswisnfatpases pages 1-2); ADRN↔MES circuits are epigenetically rewired during plasticity (URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023) (thirant2023reversibletransitionsbetween pages 1-2).
- Immunologically “cold” tumor: Low T-cell infiltration/activation with innate suppressive myeloid dominance; characteristic of NB and a barrier to ICI efficacy (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3).

Recent developments and latest research (2023–2024 priority)
- Telomere dosage–ALT axis: Integrative genome/transcriptome analysis links 11q loss/17q gain to histone variant upregulation, PRC2 attenuation, and ALT predisposition, while TERT dosage and rearrangements drive telomerase activation—offering pathway-level biomarkers and vulnerabilities (URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024) (burkert2024copynumberdosageregulates pages 18-24).
- Epigenetic control of plasticity: Dual degradation of SMARCA2/4 collapses enhancer landscapes and reduces ADRN–MES interconversion and invasion, nominating mSWI/SNF ATPases as targets to suppress therapy-evasive states (URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024) (xu2024targetingswisnfatpases pages 1-2). Foundational plasticity evidence in vivo/in patients was consolidated with single-cell profiling and xenografts (URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023) (thirant2023reversibletransitionsbetween pages 1-2).
- Immune microenvironment–informed therapy: Consensus descriptions of NB immune evasion—including MHC downregulation, suppressive myeloid infiltration, CD47 signaling, and checkpoint expression—explain limited ICI activity and motivate combinatorial strategies with cytotoxics/epigenetic modulators to increase tumor immunogenicity (URL: https://doi.org/10.3390/jcm13164765, Aug 2024; URL: https://doi.org/10.3389/fimmu.2023.1268645, Oct 2023) (persaud2024highriskneuroblastomachallenges pages 2-3, d’amico2023twobulletsin pages 6-7).

Current applications and real-world implementations
- GD2-directed immunotherapy: Anti-GD2 monoclonal antibodies are standard in high-risk consolidation/maintenance; their efficacy is impacted by the cold TME and immune-evasion circuitry summarized above, leading to active development of combination immunotherapy approaches (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Epigenetic and plasticity-directed strategies: Preclinical mSWI/SNF ATPase degraders reduce plasticity and invasion, supporting exploration as partners with cytotoxic or immune therapies to prevent emergence of MES-like resistant states (URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024) (xu2024targetingswisnfatpases pages 1-2). Epigenetic agents proposed to reprogram immunogenicity are reviewed (URL: https://doi.org/10.3389/fimmu.2025.1637626, Jul 2025) (wang2025emergingfrontiersin pages 1-2).

Expert opinions and analysis from authoritative sources
- Authoritative clinical-immunology perspective: “Immune-evasion features include central tolerance to oncofetal antigens, downregulation of MHC class I, defective antigen processing, low NK-activating ligands… abundant TAMs, MDSCs and Tregs… resulting in immunologically ‘cold’ tumors.” This synthesis explains the limited efficacy of ICIs and informs rational combination strategies with GD2 antibodies and adoptive cellular therapy (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Fundamental cell-state paradigm: NB plasticity is an epigenetically governed, microenvironment-influenced spectrum between ADRN and MES states; suppressing plasticity or redirecting state can modulate therapy response (URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023; URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024) (thirant2023reversibletransitionsbetween pages 1-2, xu2024targetingswisnfatpases pages 1-2).
- Multi-omics viewpoint: Developmental lineage programs and persister states underlie relapse and resistance; multi-omic single-cell atlases are needed to map vulnerability (URL: https://doi.org/10.1038/s41388-025-03635-2, Nov 2025; URL: https://doi.org/10.3389/fimmu.2025.1637626, Jul 2025) (he2025dissectingneuroblastomaheterogeneity pages 6-7, wang2025emergingfrontiersin pages 1-2).

Relevant statistics and data from recent studies
- While NB as a whole has seen survival gains, high-risk cohorts continue to have 5-year overall survival below 50% in many contemporary series, consistent with the immunotherapy-focused clinical review summarizing outcomes and obstacles (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3).

Required Information
1) Core Pathophysiology
- Primary mechanisms: Oncogene activation (MYCN amplification), telomere maintenance acquisition (TERT activation or ALT), segmental chromosomal instability (1p/11q loss, 17q gain), epigenetic remodeling of lineage programs (CRC, super-enhancers), and an immunosuppressive TME that impairs antigen presentation and T-cell infiltration (URL: https://doi.org/10.3390/jcm13164765, Aug 2024; URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024; URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023; URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3, burkert2024copynumberdosageregulates pages 18-24, thirant2023reversibletransitionsbetween pages 1-2, xu2024targetingswisnfatpases pages 1-2).
- Dysregulated pathways: Telomere biology (TERT/ALT), chromatin remodeling (mSWI/SNF, PRC2 imbalance), super-enhancer–based transcriptional circuitry (ADRN/MES CRCs), immune checkpoint and innate checkpoint signaling (CD47, B7-H3, PD-L1), and myeloid-driven suppression (URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024; URL: https://doi.org/10.1038/s44318-024-00206-1, Aug 2024; URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (burkert2024copynumberdosageregulates pages 18-24, xu2024targetingswisnfatpases pages 1-2, persaud2024highriskneuroblastomachallenges pages 2-3).
- Affected cellular processes: DNA damage tolerance at telomeres, enhancer remodeling and TF occupancy, antigen processing/presentation, macrophage/NK/T-cell crosstalk, and lineage-state transitions under therapy pressure (URL: as above) (burkert2024copynumberdosageregulates pages 18-24, xu2024targetingswisnfatpases pages 1-2, persaud2024highriskneuroblastomachallenges pages 2-3, thirant2023reversibletransitionsbetween pages 1-2).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - MYCN (HGNC:7553): amplified oncogene driving proliferation and TERT transcription; tied to ADRN CRC and displaced from DNA by SMARCA2/4 degradation (URL: https://doi.org/10.3390/jcm13164765; https://doi.org/10.1038/s44318-024-00206-1) (persaud2024highriskneuroblastomachallenges pages 2-3, xu2024targetingswisnfatpases pages 1-2).
  - TERT (HGNC:11730): activated via rearrangement/copy-number and MYCN; defines telomerase-positive NB (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
  - ATRX (HGNC:886): loss disrupts telomeric chromatin, promoting ALT (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
  - SMARCA2/SMARCA4 (HGNC:11100/11103): mSWI/SNF ATPases required for plasticity-permissive chromatin; dual degradation reduces plasticity and invasion (URL: https://doi.org/10.1038/s44318-024-00206-1) (xu2024targetingswisnfatpases pages 1-2).
  - PHOX2B, HAND2, GATA3 (HGNC:9140/4801/4172): ADRN CRC TFs defining noradrenergic identity (URL: https://doi.org/10.1038/s41467-023-38239-5; https://doi.org/10.1038/s44318-024-00206-1) (thirant2023reversibletransitionsbetween pages 1-2, xu2024targetingswisnfatpases pages 1-2).
  - Immune evasion mediators: CD47 (phagocytosis checkpoint), B7-H3 (CD276), PD-L1 (CD274), and MHC-I downregulation are implicated in immune exclusion (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Chemical Entities (CHEBI):
  - Anti-GD2 monoclonal antibodies (therapeutic biologics) used clinically in HR-NB; activity conditioned by TME (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Cell Types (CL):
  - Tumor cell states: adrenergic tumor cells; mesenchymal tumor cells (lineage-plastic cancer cell states) (URL: https://doi.org/10.1038/s41467-023-38239-5) (thirant2023reversibletransitionsbetween pages 1-2).
  - Immune/stromal: tumor-associated macrophages, myeloid-derived suppressor cells, regulatory T cells, NK cells (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Anatomical locations (UBERON):
  - Adrenal medulla and sympathetic chain ganglia as common primaries; bone marrow as a key metastatic niche with immunosuppressive remodeling (review synthesis) (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).

3) Biological Processes (GO annotation candidates, disrupted)
- Telomere organization and maintenance (GO:0000723; GO:0001309): TERT activation or ALT engagement; copy-number dosage reshapes TMM pathways (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
- Chromatin organization and enhancer regulation (GO:0006325; GO:0032204): mSWI/SNF-dependent accessibility enabling CRC function; PRC2 imbalance in ALT contexts (URL: https://doi.org/10.1038/s44318-024-00206-1; https://doi.org/10.1101/2022.08.16.504100) (xu2024targetingswisnfatpases pages 1-2, burkert2024copynumberdosageregulates pages 18-24).
- Regulation of transcription by RNA polymerase II (GO:0006357): super-enhancer/CRC-driven lineage programs (URL: https://doi.org/10.1038/s41467-023-38239-5) (thirant2023reversibletransitionsbetween pages 1-2).
- Antigen processing and presentation of peptide antigen via MHC class I (GO:0002474): downregulated in NB, contributing to immune coldness (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Negative regulation of T cell activation (GO:0050868) and macrophage-mediated immunity (GO:0006955): checkpoint expression (CD47, PD-L1, B7-H3) and suppressive myeloid infiltration (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Epithelial/mesenchymal program regulation (GO:0001837; GO:0001838 proxies for state changes): ADRN↔MES transitions under therapy pressure (URL: https://doi.org/10.1038/s41467-023-38239-5) (thirant2023reversibletransitionsbetween pages 1-2).

4) Cellular Components (where processes occur)
- Telomere nucleoprotein complex (GO:0000781): site of ALT recombination or telomerase action (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
- Nuclear chromatin, enhancers/super-enhancers: mSWI/SNF-regulated cis-elements controlling CRC TF binding (URL: https://doi.org/10.1038/s44318-024-00206-1; https://doi.org/10.1038/s41467-023-38239-5) (xu2024targetingswisnfatpases pages 1-2, thirant2023reversibletransitionsbetween pages 1-2).
- Plasma membrane: GD2 antigen display (therapeutic target), checkpoint molecules (PD-L1, CD47, B7-H3) (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).
- Tumor microenvironment extracellular space: cytokines and suppressive metabolites shaping immune exclusion (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).

5) Disease Progression (sequence of events)
- Developmental origin and transformation: sympathoadrenal progenitor with early segmental CNAs and oncogene activation (e.g., MYCN, TERT) establishes proliferative, ADRN-skewed tumor. Acquisition of telomere maintenance (telomerase or ALT) enables immortalization and genomic stability under replication stress (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
- Therapy pressure and plasticity: cytotoxic exposure enriches MES-like, chemoresistant states; microenvironmental signals can bias reversion to ADRN identity in vivo. Persistent plasticity enables relapse and resistance (URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023) (thirant2023reversibletransitionsbetween pages 1-2).
- Immune evasion and metastasis: MHC-I downregulation, myeloid suppression, and checkpoint signaling facilitate immune escape; bone marrow metastatic niches display pronounced immune suppression and T-cell dysfunction, limiting immunotherapy efficacy (URL: https://doi.org/10.3390/jcm13164765, Aug 2024) (persaud2024highriskneuroblastomachallenges pages 2-3).

6) Phenotypic Manifestations (clinical phenotypes and mechanism links)
- Common phenotypes: abdominal mass (adrenal/sympathetic), bone/bone marrow metastases, opsoclonus–myoclonus in subsets; in high-risk disease, refractory/relapsed course and poor survival are linked to TMM activation and ADRN↔MES plasticity under therapy (URL: https://doi.org/10.3390/jcm13164765, Aug 2024; URL: https://doi.org/10.1101/2022.08.16.504100, Aug 2024; URL: https://doi.org/10.1038/s41467-023-38239-5, May 2023) (persaud2024highriskneuroblastomachallenges pages 2-3, burkert2024copynumberdosageregulates pages 18-24, thirant2023reversibletransitionsbetween pages 1-2).

Gene/protein annotations with ontology terms (examples)
- MYCN (HGNC:7553) – Biological Process: positive regulation of transcription by RNA Pol II; cellular component: nucleus; Molecular Function: DNA-binding TF activity; Evidence: amplification and CRC occupancy in ADRN state; therapeutic vulnerability via mSWI/SNF ATPase degradation reducing TF DNA binding (URL: https://doi.org/10.1038/s44318-024-00206-1) (xu2024targetingswisnfatpases pages 1-2).
- TERT (HGNC:11730) – Biological Process: telomere maintenance via telomerase; Cellular Component: telomerase holoenzyme complex, telomere; Evidence: rearrangements/copy-number/MYCN drive TERT activation in NB (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
- ATRX (HGNC:886) – Biological Process: chromatin assembly at telomeres; ALT association; Cellular Component: nuclear chromatin; Evidence: ATRX dysfunction promotes ALT in NB (URL: https://doi.org/10.1101/2022.08.16.504100) (burkert2024copynumberdosageregulates pages 18-24).
- SMARCA2/SMARCA4 (HGNC:11100/11103) – Biological Process: chromatin remodeling; Cellular Component: SWI/SNF complex; Evidence: dual degradation reduces plasticity and invasion (URL: https://doi.org/10.1038/s44318-024-00206-1) (xu2024targetingswisnfatpases pages 1-2).

Phenotype associations (HP terms, examples)
- HP:0002664 (Neoplasm of the adrenal gland)—common primary site; HP:0002667 (Metastatic neoplasm of the bone); mechanism links include immune suppression and lineage plasticity associated with progression and therapeutic resistance (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).

Cell type involvement (CL terms)
- CL:0000542 (neuron, sympathoadrenal lineage derivatives—tumor of neural crest origin); CL:0000798 (macrophage), CL:0000815 (T cell), CL:0000623 (natural killer cell)—constitute the immune TME implicated in immune evasion (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).

Anatomical locations (UBERON terms)
- UBERON:0002369 (adrenal medulla), UBERON:0001043 (sympathetic trunk), UBERON:0000178 (bone marrow) as sites of origin/metastasis with characteristic microenvironmental programs (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).

Chemical entities (CHEBI)
- Anti-GD2 antibody therapeutics (biologic drugs targeting disialoganglioside GD2) widely implemented in HR-NB; TME features modulate efficacy (URL: https://doi.org/10.3390/jcm13164765) (persaud2024highriskneuroblastomachallenges pages 2-3).

Evidence items (PMID/DOI/URLs; publication dates)
- Persaud et al., Journal of Clinical Medicine, “High-Risk Neuroblastoma Challenges and Opportunities for Antibody-Based Cellular Immunotherapy.” Aug 2024. URL: https://doi.org/10.3390/jcm13164765 (persaud2024highriskneuroblastomachallenges pages 2-3).
- Burkert et al., iScience, “Copy-number dosage regulates telomere maintenance and disease-associated pathways in neuroblastoma.” Aug 2024. URL: https://doi.org/10.1101/2022.08.16.504100 (burkert2024copynumberdosageregulates pages 18-24).
- Thirant et al., Nature Communications, “Reversible transitions between noradrenergic and mesenchymal tumor identities define cell plasticity in neuroblastoma.” May 2023. URL: https://doi.org/10.1038/s41467-023-38239-5 (thirant2023reversibletransitionsbetween pages 1-2).
- Xu et al., The EMBO Journal, “Targeting SWI/SNF ATPases reduces neuroblastoma cell plasticity.” Aug 2024. URL: https://doi.org/10.1038/s44318-024-00206-1 (xu2024targetingswisnfatpases pages 1-2).
- Wang et al., Frontiers in Immunology, “Emerging frontiers in epigenetic-targeted therapeutics for pediatric neuroblastoma.” Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1637626 (wang2025emergingfrontiersin pages 1-2, wang2025emergingfrontiersin pages 6-7).
- He et al., Oncogene, “Dissecting neuroblastoma heterogeneity through single-cell multi-omics: insights into development, immunity, and therapeutic resistance.” Nov 2025. URL: https://doi.org/10.1038/s41388-025-03635-2 (he2025dissectingneuroblastomaheterogeneity pages 6-7).
- D’Amico et al., Frontiers in Immunology, “Combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.” Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1268645 (d’amico2023twobulletsin pages 6-7).

Notes on evidence scope and limitations
- The core mechanistic claims above are supported by recent high-quality primary studies (Nature Communications 2023; EMBO Journal 2024) and integrative analyses (iScience 2024). Where comprehensive clinical statistics (incidence/survival trends) would usually be drawn from national registries, the present synthesis cites a 2024 clinical immunotherapy review for high-risk survival context because those were among the most relevant sources in the retrieved set (persaud2024highriskneuroblastomachallenges pages 2-3). Additional registry-based epidemiology could further refine survival estimates but was outside the current evidence set.

References

1. (persaud2024highriskneuroblastomachallenges pages 2-3): Natasha V. Persaud, Jeong A. Park, and Nai Kong V. Cheung. High-risk neuroblastoma challenges and opportunities for antibody-based cellular immunotherapy. Journal of Clinical Medicine, 13:4765, Aug 2024. URL: https://doi.org/10.3390/jcm13164765, doi:10.3390/jcm13164765. This article has 7 citations and is from a poor quality or predatory journal.

2. (burkert2024copynumberdosageregulates pages 18-24): Martin Burkert, Eric Blanc, Nina Thiessen, Christiane Weber, Joern Toedling, Remo Monti, Victoria M Dombrowe, Maria Stella de Biase, Tom L Kaufmann, Kerstin Haase, Sebastian M Waszak, Angelika Eggert, Dieter Beule, Johannes H Schulte, Uwe Ohler, and Roland F Schwarz. Copy-number dosage regulates telomere maintenance and disease-associated pathways in neuroblastoma. iScience, Aug 2024. URL: https://doi.org/10.1101/2022.08.16.504100, doi:10.1101/2022.08.16.504100. This article has 3 citations and is from a peer-reviewed journal.

3. (thirant2023reversibletransitionsbetween pages 1-2): Cécile Thirant, Agathe Peltier, Simon Durand, Amira Kramdi, Caroline Louis-Brennetot, Cécile Pierre-Eugène, Margot Gautier, Ana Costa, Amandine Grelier, Sakina Zaïdi, Nadège Gruel, Irène Jimenez, Eve Lapouble, Gaëlle Pierron, Déborah Sitbon, Hervé J. Brisse, Arnaud Gauthier, Paul Fréneaux, Sandrine Grossetête, Laura G. Baudrin, Virginie Raynal, Sylvain Baulande, Angela Bellini, Jaydutt Bhalshankar, Angel M. Carcaboso, Birgit Geoerger, Hermann Rohrer, Didier Surdez, Valentina Boeva, Gudrun Schleiermacher, Olivier Delattre, and Isabelle Janoueix-Lerosey. Reversible transitions between noradrenergic and mesenchymal tumor identities define cell plasticity in neuroblastoma. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38239-5, doi:10.1038/s41467-023-38239-5. This article has 77 citations and is from a highest quality peer-reviewed journal.

4. (xu2024targetingswisnfatpases pages 1-2): Man Xu, Jason J Hong, Xiyuan Zhang, Ming Sun, Xingyu Liu, Jeeyoun Kang, Hannah Stack, Wendy Fang, Haiyan Lei, Xavier Lacoste, Reona Okada, Raina Jung, Rosa Nguyen, Jack F Shern, Carol J Thiele, and Zhihui Liu. Targeting swi/snf atpases reduces neuroblastoma cell plasticity. The EMBO Journal, 43:4522-4541, Aug 2024. URL: https://doi.org/10.1038/s44318-024-00206-1, doi:10.1038/s44318-024-00206-1. This article has 12 citations.

5. (wang2025emergingfrontiersin pages 6-7): Xiaokang Wang, Gengrui Xu, Hongyan Ma, Xiaoyan Deng, and Guiping Ma. Emerging frontiers in epigenetic-targeted therapeutics for pediatric neuroblastoma. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1637626, doi:10.3389/fimmu.2025.1637626. This article has 2 citations and is from a peer-reviewed journal.

6. (he2025dissectingneuroblastomaheterogeneity pages 6-7): Guo-qian He, Si-jia He, Xiao-yu Jing, Yi-ling Dai, Xia Guo, Ju Gao, and Wei Zhang. Dissecting neuroblastoma heterogeneity through single-cell multi-omics: insights into development, immunity, and therapeutic resistance. Oncogene, 45:123-139, Nov 2025. URL: https://doi.org/10.1038/s41388-025-03635-2, doi:10.1038/s41388-025-03635-2. This article has 1 citations and is from a domain leading peer-reviewed journal.

7. (d’amico2023twobulletsin pages 6-7): Silvia D’Amico, Patrizia Tempora, Paula Gragera, Kamila Król, Ombretta Melaiu, Maria Antonietta De Ioris, Franco Locatelli, and Doriana Fruci. Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity. Frontiers in Immunology, Oct 2023. URL: https://doi.org/10.3389/fimmu.2023.1268645, doi:10.3389/fimmu.2023.1268645. This article has 5 citations and is from a peer-reviewed journal.

8. (wang2025emergingfrontiersin pages 1-2): Xiaokang Wang, Gengrui Xu, Hongyan Ma, Xiaoyan Deng, and Guiping Ma. Emerging frontiers in epigenetic-targeted therapeutics for pediatric neuroblastoma. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1637626, doi:10.3389/fimmu.2025.1637626. This article has 2 citations and is from a peer-reviewed journal.