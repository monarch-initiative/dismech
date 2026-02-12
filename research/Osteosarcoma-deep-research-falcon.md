---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T16:39:11.604927'
end_time: '2026-01-31T16:47:07.194779'
duration_seconds: 475.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteosarcoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Osteosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteosarcoma**.
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
- **Disease Name:** Osteosarcoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Osteosarcoma**.
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
- Disease Name: Osteosarcoma
- MONDO ID: MONDO:0005301
- Category: Cancer

Plan status: We identified and analyzed recent literature (2023–2024 priority) and extracted mechanistic evidence; we synthesized ontology-linked annotations and organized a summary artifact to embed below.

| Category | Key Mechanisms / Entities | Ontologies (HGNC / GO / CL / UBERON / CHEBI) | Evidence (DOI / Journal / Year / URL; context ID) |
|---|---|---|---|
| Genomic instability | Chromothripsis, kataegis; TP53, RB1, ATRX; copy-number gains (MYC, MDM2) and losses; chromosomal rearrangement | HGNC: TP53, RB1, ATRX, MYC, MDM2; GO: DNA damage response, chromatin organization; CL: mesenchymal stem cell, osteoblast; UBERON: bone | DOI:10.3390/ijms241411367; Int J Mol Sci (2023); https://doi.org/10.3390/ijms241411367 (nirala2023decipheringthesignaling pages 2-4); DOI:10.3390/ijms241310463; Int J Mol Sci (2023); https://doi.org/10.3390/ijms241310463 (pires2023analysisofthe pages 2-5); DOI:10.3390/biom14020145; Biomolecules (2024); https://doi.org/10.3390/biom14020145 (alansari2024unveilingtheprotective pages 6-8) |
| Signaling pathways | PI3K/AKT/mTOR; Wnt/β-catenin; TGF-β; JAK/STAT; NOTCH; Hedgehog (SHH/GLI); RANK/RANKL; NF-κB (driving proliferation, survival, EMT, invasion, metastasis, therapy resistance) | HGNC: PIK3CA, AKT1, MTOR, CTNNB1, TGFBR2, JAK2, NOTCH1, SMO, TNFSF11, NFKB1; GO: signal transduction, regulation of cell proliferation, EMT; CL: tumor cell; UBERON: bone | DOI:10.3390/ijms241411367; Int J Mol Sci (2023); https://doi.org/10.3390/ijms241411367 (nirala2023decipheringthesignaling pages 2-4); DOI:10.3892/ijmm.2025.5533; Int J Mol Med (2025); https://doi.org/10.3892/ijmm.2025.5533 (chen2025harnessingmultiomicsto pages 4-5) |
| Tumor microenvironment (TME) | SPP1+ tumor-associated macrophages (TAMs); mregDCs (LAMP3+ CCR7+ CD83+); cancer-associated fibroblasts (CAFs); osteoclasts; endothelial cells; PD-L1 (CD274) upregulation; MHC-I/B2M downregulation; CD24 'don't eat me' signal | HGNC: SPP1, CD274, B2M, CD24; GO: antigen processing/presentation, immune evasion, inflammatory response; CL: macrophage, dendritic cell, fibroblast, osteoclast, endothelial cell; UBERON: bone | DOI:10.1038/s41413-022-00237-6; Bone Research (2023); https://doi.org/10.1038/s41413-022-00237-6 (liu2023characterizingthetumor pages 2-3); DOI:10.1007/s00432-024-05787-2; J Cancer Res Clin Oncol (2024); https://doi.org/10.1007/s00432-024-05787-2 (zheng2024singlecelltranscriptomicinsights pages 1-2) |
| Metabolic rewiring | Increased glycolysis (SLC2A1/GLUT1); enhanced glutaminolysis (GLS); lipid metabolic shifts (e.g., ACSL5); metabolic-immune crosstalk reshaping TME | HGNC: SLC2A1, GLS, ACSL5; GO: glycolytic process (GO:0006096), glutamine metabolic process, fatty acid metabolic process; CL: cancer stem cell, immune effector cell | DOI:10.3892/ijmm.2025.5533; Int J Mol Med (2025); https://doi.org/10.3892/ijmm.2025.5533 (chen2025harnessingmultiomicsto pages 4-5); DOI:10.3390/ijms24098401; Int J Mol Sci (2023) (reviewed metabolic CSC pathways) (nirala2023decipheringthesignaling pages 2-4) |
| Metastasis to lung | Chemokine/chemotaxis axes (pre-metastatic niche), EMT/mesenchymal programs, ECM remodeling (MMPs), platelet/immune-cell-mediated dissemination; selection for genomic/epigenetic clones | GO: cell migration, chemotaxis, extracellular matrix organization; CL: circulating tumor cell; UBERON: lung | DOI:10.3390/ijms241411367; Int J Mol Sci (2023); https://doi.org/10.3390/ijms241411367 (nirala2023decipheringthesignaling pages 2-4); DOI:10.3390/ijms241310463; Int J Mol Sci (2023); https://doi.org/10.3390/ijms241310463 (pires2023analysisofthe pages 2-5); DOI:10.3892/ijmm.2025.5533; Int J Mol Med (2025); https://doi.org/10.3892/ijmm.2025.5533 (chen2025harnessingmultiomicsto pages 4-5) |
| Treatment-induced remodeling (post-chemotherapy) | Residual tumor cells upregulate stemness programs; enrichment/activation of CAFs with ECM-remodeling capacity; endothelial changes and depletion/suppression of antitumor immune subsets (myeloid, T/NK) | GO: regulation of stem cell population maintenance, extracellular matrix organization, immune response; CL: cancer stem cell, CAF, T cell, NK cell, myeloid cell | DOI:10.1007/s00432-024-05787-2; J Cancer Res Clin Oncol (2024); https://doi.org/10.1007/s00432-024-05787-2 (zheng2024singlecelltranscriptomicinsights pages 1-2); DOI:10.1038/s41413-022-00237-6; Bone Research (2023); https://doi.org/10.1038/s41413-022-00237-6 (liu2023characterizingthetumor pages 2-3) |


*Table: Compact, evidence-linked summary of key molecular mechanisms, cell types, ontology categories and primary citations for osteosarcoma pathophysiology (genomic instability, signaling, TME, metabolism, metastasis, and post‑chemotherapy remodeling). Useful as a knowledge‑base row or quick reference with direct source links.*

Pathophysiology description
Osteosarcoma (OS) is a high-grade primary malignant bone tumor characterized by profound genomic instability, dysregulated developmental and stress-response signaling, metabolic rewiring, and a uniquely immunosuppressive bone tumor microenvironment (TME) that collectively drive invasion, lung metastasis, and treatment resistance (nirala2023decipheringthesignaling pages 1-2). Genomic catastrophe is a defining feature: chromothripsis and kataegis co-occur with frequent loss of key tumor suppressors (TP53, RB1, ATRX) and gains of oncogenes (MYC, MDM2), with epigenetic dysregulation superimposed on widespread copy-number alterations (nirala2023decipheringthesignaling pages 1-2, pires2023analysisofthe pages 2-5, alansari2024unveilingtheprotective pages 6-8). Convergent activation of PI3K/AKT/mTOR, Wnt/β‑catenin, TGF‑β, JAK/STAT, NOTCH, Hedgehog/GLI, RANK/RANKL, and NF‑κB pathways promotes proliferation, survival, EMT-like migration, osteoclastogenic crosstalk, and metastasis (nirala2023decipheringthesignaling pages 2-4). Single-cell analyses reveal immune-evasion programs including downregulation of MHC-I/B2M and upregulation of PD‑L1 and the anti-phagocytic ligand CD24 on cancer cells, accompanied by expansion of immunoregulatory LAMP3+CCR7+CD83+ dendritic cells (mregDCs) and SPP1+ tumor-associated macrophages (TAMs) (liu2023characterizingthetumor pages 2-3). Neoadjuvant chemotherapy remodels this ecosystem toward stemness-enriched tumor cells, ECM‑remodeling CAFs, altered endothelium, and depletion of effector myeloid and T/NK compartments, contributing to resistance and relapse (zheng2024singlecelltranscriptomicinsights pages 1-2).

Key concepts and definitions (current understanding)
- Chromothripsis: catastrophic one-off chromosome shattering and rejoining that accelerates karyotype evolution; prevalent in OS and linked to micronuclei and decatenation defects (quote: mechanisms include “micronuclear DNA damage”; RanGAP1 reduction increases chromothripsis risk) (nirala2023decipheringthesignaling pages 2-4). URL: https://doi.org/10.3390/ijms241411367 (Jul 2023).
- Kataegis: localized hypermutation tracts; reported in roughly half of OS and often co‑occurs with chromothripsis (nirala2023decipheringthesignaling pages 2-4, pires2023analysisofthe pages 2-5, alansari2024unveilingtheprotective pages 6-8). URLs: https://doi.org/10.3390/ijms241411367 (Jul 2023); https://doi.org/10.3390/ijms241310463 (Jun 2023); https://doi.org/10.3390/biom14020145 (Jan 2024).
- mregDCs: LAMP3+CCR7+CD83+ mature regulatory dendritic cells enriched in OS tumors; associated with Treg recruitment and poorer survival; increasing inhibitory ligands (PD‑L1, LAG3, LGALS9, SIRPA, TIGIT, PD‑L2) along DC maturation trajectories (liu2023characterizingthetumor pages 2-3). URL: https://doi.org/10.1038/s41413-022-00237-6 (Jan 2023).
- SPP1+ TAMs: osteopontin-expressing macrophages linked to immune suppression and adverse prognosis in OS ecosystems (liu2023characterizingthetumor pages 2-3). URL: https://doi.org/10.1038/s41413-022-00237-6 (Jan 2023).

Recent developments and latest research (2023–2024 priority)
- Genomic landscape in new primary OS: 28-tumor cohort delineated 445 deleterious coding variants with recurrent TP53 (~60% considering SNV/indel/CNA), RB1, ATRX, and complex CNA patterns reminiscent of chromothripsis/chromoanasynthesis; pathway enrichment implicated immunity and bone development programs (pires2023analysisofthe pages 2-5). URL: https://doi.org/10.3390/ijms241310463 (Jun 2023).
- Single-cell TME remodeling after chemotherapy: residual cells upregulate stemness; CAFs expand and increase ECM-remodeling capacity; endothelial cells increase with impaired differentiation; anti-tumor myeloid and T/NK subsets are depleted (zheng2024singlecelltranscriptomicinsights pages 1-2). URL: https://doi.org/10.1007/s00432-024-05787-2 (Jul 2024).
- Single-cell immune evasion mechanisms: inferCNV-linked CNV‑high cancer cells downregulate interferon pathways and MHC-I/B2M; mregDCs correlate with Tregs; CD24 identified as a “don’t eat me” signal on OS cells (liu2023characterizingthetumor pages 2-3). URL: https://doi.org/10.1038/s41413-022-00237-6 (Jan 2023).

Current applications and real-world implementations
- Molecular risk and target identification: Copy-number and expression assessment of TP53/RB1 loss, MDM2 gain, and MYC amplification inform prognosis and experimental targeting (e.g., MDM2–p53 axis) (pires2023analysisofthe pages 2-5, nirala2023decipheringthesignaling pages 1-2). URL: https://doi.org/10.3390/ijms241310463 (Jun 2023); https://doi.org/10.3390/ijms241411367 (Jul 2023).
- Immune profiling for trial design: scRNA-seq-defined mregDC and SPP1+ TAM signatures, MHC-I/B2M loss, and PD‑L1 expression guide rational immunotherapy combinations (checkpoint blockade + myeloid/DC modulation) (liu2023characterizingthetumor pages 2-3). URL: https://doi.org/10.1038/s41413-022-00237-6 (Jan 2023).
- Therapy sequencing considerations: Post-chemotherapy scRNA-seq suggests combining cytotoxic therapy with CAF/ECM-targeting or immune-restoring agents to mitigate stemness/ECM/immune escape (zheng2024singlecelltranscriptomicinsights pages 1-2). URL: https://doi.org/10.1007/s00432-024-05787-2 (Jul 2024).

Expert opinions and analysis (authoritative sources)
- 2023 signaling review emphasizes the convergence of PI3K/AKT/mTOR, Wnt/β‑catenin, TGF‑β, JAK/STAT, NOTCH, Hedgehog, RANK/RANKL, and NF‑κB as drivers of proliferation, invasion, and lung metastasis; also highlights chromothripsis/kataegis as frequent, and immune–tumor crosstalk as clinically relevant (nirala2023decipheringthesignaling pages 2-4, nirala2023decipheringthesignaling pages 1-2). URL: https://doi.org/10.3390/ijms241411367 (Jul 2023).
- 2023 mutational landscape study concludes “high genomic OS instability and heterogeneity,” identifying novel disrupted genes linked to poor outcomes and reinforcing TP53/RB1 centrality (pires2023analysisofthe pages 2-5). URL: https://doi.org/10.3390/ijms241310463 (Jun 2023).
- 2023 single-cell atlas authors state that mregDCs “promote tumor immune tolerance through recruitment of Tregs” and that CNV‑high tumor cells exhibit “reduced interferon‑γ pathway activity and lower MHC‑I/B2M” (liu2023characterizingthetumor pages 2-3). URL: https://doi.org/10.1038/s41413-022-00237-6 (Jan 2023).

Relevant statistics and data (recent studies)
- Genomic burden: 74,880 SNVs/indels across 28 primaries; filtered 445 coding non-synonymous candidates; TP53 alterations ~60% including SNV/indel/CNA; frequent gains 1q21, 6p21, 8q; losses 10q26, 13q14–21; complex CNA patterns (pires2023analysisofthe pages 2-5). URL: https://doi.org/10.3390/ijms241310463 (Jun 2023).
- scRNA-seq TME composition (pre-therapy OS): myeloid ~35%, tumor ~27%, plus T/ILC, B cells, osteoclasts, endothelial, mesenchymal stromal cells (zheng2024singlecelltranscriptomicinsights pages 1-2). URL: https://doi.org/10.1007/s00432-024-05787-2 (Jul 2024).

Structured knowledge base annotations
- Genes/Proteins (HGNC): TP53, RB1, ATRX, MYC, MDM2, PIK3CA, AKT1, MTOR, CTNNB1, TGFBR2, JAK2, NOTCH1, SMO, NFKB1, SPP1, CD274 (PD‑L1), B2M, HLA‑A/B/E, CD24 (nirala2023decipheringthesignaling pages 2-4, pires2023analysisofthe pages 2-5, liu2023characterizingthetumor pages 2-3).
- Biological processes (GO): DNA damage response; chromatin organization; mitotic cell cycle; signal transduction via PI3K/AKT/mTOR; Wnt signaling; TGF‑β signaling; JAK/STAT cascade; NOTCH signaling; Hedgehog signaling; NF‑κB signaling; osteoclast differentiation (RANK/RANKL); antigen processing and presentation via MHC class I; regulation of macrophage activation; extracellular matrix organization; glycolytic process; glutamine metabolic process; fatty acid metabolic process (nirala2023decipheringthesignaling pages 2-4, pires2023analysisofthe pages 2-5, liu2023characterizingthetumor pages 2-3, zheng2024singlecelltranscriptomicinsights pages 1-2).
- Cellular components: micronuclei (chromothripsis mechanism); nucleus/chromatin; plasma membrane (PD‑L1, CD24); MHC-I complex; extracellular matrix; exocytic vesicles; endothelium; osteoclastic resorption lacunae (nirala2023decipheringthesignaling pages 2-4, liu2023characterizingthetumor pages 2-3, zheng2024singlecelltranscriptomicinsights pages 1-2).
- Cell types (CL): osteoblast-like tumor cell; mesenchymal stromal cell; cancer-associated fibroblast; SPP1+ tumor-associated macrophage; mature regulatory dendritic cell (LAMP3+CCR7+CD83+); osteoclast; endothelial cell; T cell and NK cell (liu2023characterizingthetumor pages 2-3, zheng2024singlecelltranscriptomicinsights pages 1-2).
- Anatomical locations (UBERON): bone (primary); lung (metastatic); bone marrow niche; perivascular/endosteal/hypoxic niches (nirala2023decipheringthesignaling pages 1-2, alansari2024unveilingtheprotective pages 6-8).
- Chemical entities (ChEBI): lactate (glycolysis), glutamine, fatty acids; cisplatin context for chemosensitivity; growth factors such as TGF‑β; cytokines/chemokines influencing niches (zheng2024singlecelltranscriptomicinsights pages 1-2, nirala2023decipheringthesignaling pages 2-4, alansari2024unveilingtheprotective pages 6-8).

Evidence items with PMIDs/DOIs, key mechanistic quotes
- Nirala 2023 (IJMS; Jul 2023): “Massive genomic rearrangement (chromothripsis) is highly prevalent in OS… loss/reduction of RanGAP1 increases chromothripsis risk… Alterations in PI3K/AKT/mTOR, JAK/STAT, Wnt/β‑catenin, NOTCH, Hedgehog/Gli, TGF‑β, RTKs, RANK/RANKL, and NF‑κB have been identified in OS development and metastasis.” DOI: 10.3390/ijms241411367. https://doi.org/10.3390/ijms241411367 (nirala2023decipheringthesignaling pages 2-4, nirala2023decipheringthesignaling pages 1-2).
- Pires 2023 (IJMS; Jun 2023): “TP53 was the most recurrently mutated gene, with an overall rate of ~60%… Seven cases presented CNA patterns reminiscent of complex events (chromothripsis and chromoanasynthesis)… A protein–protein network enrichment highlighted biological pathways involved in immunity and bone development.” DOI: 10.3390/ijms241310463. https://doi.org/10.3390/ijms241310463 (pires2023analysisofthe pages 2-5).
- Liu 2023 (Bone Research; Jan 2023): “mregDCs promote tumor immune tolerance through recruitment of Tregs… CNV-high cells exhibited reduced interferon‑gamma pathway activity and lower MHC‑I (HLA‑A, HLA‑B, HLA‑E) and B2M expression… CD24 was identified as a novel ‘don’t eat me’ signal that contributed to the immune evasion of OS cells.” DOI: 10.1038/s41413-022-00237-6. https://doi.org/10.1038/s41413-022-00237-6 (liu2023characterizingthetumor pages 2-3).
- Zheng 2024 (J Cancer Res Clin Oncol; Jul 2024): “Chemotherapy caused the remaining OS cells to express higher levels of genes associated with stemness… enhances the presence of cancer-associated fibroblasts, increasing their ability to modify the extracellular matrix… reduced the immune cell population, including myeloid and T/NK cells, particularly subpopulations with tumor-fighting capabilities.” DOI: 10.1007/s00432-024-05787-2. https://doi.org/10.1007/s00432-024-05787-2 (zheng2024singlecelltranscriptomicinsights pages 1-2).
- Al‑Ansari 2024 (Biomolecules; Jan 2024): summarizes ranges for chromothripsis (~20–89%) and kataegis (~50–85%) and high frequencies of TP53 (75–90%) and RB1 (50–78%) defects pooled from literature (context for variability across cohorts). DOI: 10.3390/biom14020145. https://doi.org/10.3390/biom14020145 (alansari2024unveilingtheprotective pages 6-8).

Disease progression (sequence of events)
1) Initiation: developmental osteoblast/MSC lineage acquires catastrophic structural lesions (chromothripsis/kataegis), with early loss of TP53/RB1/ATRX and focal oncogene gains (MYC/MDM2) (nirala2023decipheringthesignaling pages 1-2, pires2023analysisofthe pages 2-5).
2) Clonal selection: dysregulated PI3K/AKT/mTOR, Wnt/β‑catenin, TGF‑β, NOTCH, Hedgehog, JAK/STAT and NF‑κB drive proliferation, survival, osteoid production, invasion (nirala2023decipheringthesignaling pages 2-4).
3) Microenvironmental conditioning: RANK/RANKL promotes osteoclastogenesis; TAMs (SPP1+) and mregDCs accumulate; cancer cells reduce MHC‑I/B2M and elevate PD‑L1/CD24 to evade immunity (liu2023characterizingthetumor pages 2-3).
4) Metastatic dissemination: EMT-like programs, ECM remodeling, and chemotactic axes enable intravasation and lung colonization; AKT1/FGFR signaling contribute to invasive/metastatic phenotypes (nirala2023decipheringthesignaling pages 2-4, chen2025harnessingmultiomicsto pages 4-5).
5) Treatment remodeling: chemotherapy enriches stem-like tumor cells and CAF-driven ECM programs while depleting effectors, fostering resistance and recurrence (zheng2024singlecelltranscriptomicinsights pages 1-2).

Phenotypic manifestations (link to mechanisms)
- Clinical: destructive metaphyseal bone lesions with periosteal reaction; osteoid production by malignant cells; high propensity for lung metastases. Mechanistic correlates: osteoblast-lineage origin with RANKL–osteoclast crosstalk; ECM remodeling and immune evasion supporting dissemination (nirala2023decipheringthesignaling pages 2-4, liu2023characterizingthetumor pages 2-3).

Citations and metadata (URLs and dates)
- Nirala BK et al., Int J Mol Sci, Jul 2023, https://doi.org/10.3390/ijms241411367 (nirala2023decipheringthesignaling pages 2-4, nirala2023decipheringthesignaling pages 1-2).
- Pires SF et al., Int J Mol Sci, Jun 2023, https://doi.org/10.3390/ijms241310463 (pires2023analysisofthe pages 2-5).
- Liu W et al., Bone Research, Jan 2023, https://doi.org/10.1038/s41413-022-00237-6 (liu2023characterizingthetumor pages 2-3).
- Zheng X et al., J Cancer Res Clin Oncol, Jul 2024, https://doi.org/10.1007/s00432-024-05787-2 (zheng2024singlecelltranscriptomicinsights pages 1-2).
- Al‑Ansari N et al., Biomolecules, Jan 2024, https://doi.org/10.3390/biom14020145 (alansari2024unveilingtheprotective pages 6-8).
- Chen X et al., Int J Mol Med, Apr 2025, https://doi.org/10.3892/ijmm.2025.5533 (chen2025harnessingmultiomicsto pages 4-5).

Notes on evidence scope
- Where possible, we prioritized 2023–2024 primary and integrative studies; one 2025 precision‑medicine review is included to connect AKT/FGFR signaling to metastasis and resistance. Future updates should incorporate emerging 2024–2026 genomics (e.g., chromothripsis dynamics) as they are peer‑reviewed.


References

1. (nirala2023decipheringthesignaling pages 2-4): Bikesh K. Nirala, Taku Yamamichi, and Jason T. Yustein. Deciphering the signaling mechanisms of osteosarcoma tumorigenesis. International Journal of Molecular Sciences, 24:11367, Jul 2023. URL: https://doi.org/10.3390/ijms241411367, doi:10.3390/ijms241411367. This article has 41 citations and is from a poor quality or predatory journal.

2. (pires2023analysisofthe pages 2-5): Sara Ferreira Pires, Juliana Sobral de Barros, Silvia Souza da Costa, Gabriel Bandeira do Carmo, Marília de Oliveira Scliar, André van Helvoort Lengert, Érica Boldrini, Sandra Regini Morini da Silva, Daniel Onofre Vidal, Mariana Maschietto, and Ana Cristina Victorino Krepischi. Analysis of the mutational landscape of osteosarcomas identifies genes related to metastasis and prognosis and disrupted biological pathways of immune response and bone development. International Journal of Molecular Sciences, 24:10463, Jun 2023. URL: https://doi.org/10.3390/ijms241310463, doi:10.3390/ijms241310463. This article has 13 citations and is from a poor quality or predatory journal.

3. (alansari2024unveilingtheprotective pages 6-8): Nojoud Al-Ansari, Samson Mathews Samuel, and Dietrich Büsselberg. Unveiling the protective role of melatonin in osteosarcoma: current knowledge and limitations. Biomolecules, 14:145, Jan 2024. URL: https://doi.org/10.3390/biom14020145, doi:10.3390/biom14020145. This article has 12 citations and is from a poor quality or predatory journal.

4. (chen2025harnessingmultiomicsto pages 4-5): Xuesong Chen, Bin Tian, Yiqun Wang, Jiang Zheng, and Xin Kang. Harnessing multi-omics to revolutionize understanding and management of osteosarcoma: a pathway to precision medicine (review). International Journal of Molecular Medicine, 55:1-20, Apr 2025. URL: https://doi.org/10.3892/ijmm.2025.5533, doi:10.3892/ijmm.2025.5533. This article has 2 citations and is from a peer-reviewed journal.

5. (liu2023characterizingthetumor pages 2-3): Weijian Liu, Hongzhi Hu, Zengwu Shao, Xiao Lv, Zhicai Zhang, Xiangtian Deng, Qingcheng Song, Yong Han, Tao Guo, Liming Xiong, Baichuan Wang, and Yingze Zhang. Characterizing the tumor microenvironment at the single-cell level reveals a novel immune evasion mechanism in osteosarcoma. Bone Research, Jan 2023. URL: https://doi.org/10.1038/s41413-022-00237-6, doi:10.1038/s41413-022-00237-6. This article has 78 citations and is from a domain leading peer-reviewed journal.

6. (zheng2024singlecelltranscriptomicinsights pages 1-2): Xuejing zheng, Wence Wu, Zhen-guo Zhao, Xin-xin Zhang, and Shengji Yu. Single-cell transcriptomic insights into chemotherapy-induced remodeling of the osteosarcoma tumor microenvironment. Journal of Cancer Research and Clinical Oncology, Jul 2024. URL: https://doi.org/10.1007/s00432-024-05787-2, doi:10.1007/s00432-024-05787-2. This article has 5 citations and is from a peer-reviewed journal.

7. (nirala2023decipheringthesignaling pages 1-2): Bikesh K. Nirala, Taku Yamamichi, and Jason T. Yustein. Deciphering the signaling mechanisms of osteosarcoma tumorigenesis. International Journal of Molecular Sciences, 24:11367, Jul 2023. URL: https://doi.org/10.3390/ijms241411367, doi:10.3390/ijms241411367. This article has 41 citations and is from a poor quality or predatory journal.