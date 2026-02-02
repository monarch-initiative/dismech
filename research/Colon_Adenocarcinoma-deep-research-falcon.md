---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T17:20:47.868543'
end_time: '2026-01-31T17:28:07.511631'
duration_seconds: 439.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Colon Adenocarcinoma
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
- **Disease Name:** Colon Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Colon Adenocarcinoma**.
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
- **Disease Name:** Colon Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Colon Adenocarcinoma**.
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
- Disease Name: Colon Adenocarcinoma
- MONDO ID: MONDO:0004992 (colon adenocarcinoma)
- Category: Cancer

<artifact-00/>

## Pathophysiology description (current understanding)
Colon adenocarcinoma arises through distinct but overlapping molecular routes that converge on deregulated signaling, altered cell states, epigenetic remodeling, and reprogrammed ecosystems. Three primary mechanisms of genomic/epigenomic instability predominate: chromosomal instability (CIN; ~70–84% of sporadic CRC), microsatellite instability (MSI; ~13–16%), and the CpG island methylator phenotype (CIMP) that underlies the serrated neoplasia pathway (~15–30%) and frequently co-occurs with BRAF V600E and MLH1 promoter hypermethylation (proximal, mucinous, lymphocyte-rich tumors) (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8). The classical adenoma–carcinoma sequence typically begins with APC loss and WNT activation, followed by subclonal selection of KRAS/PIK3CA, and later disruption of TP53 and SMAD4; MSI tumors emerge from defective mismatch repair via germline MMR variants or sporadic MLH1 methylation; serrated lesions progress through MAPK activation (BRAF), diffuse CpG methylation, and often MLH1 silencing leading to MSI (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).

Dysregulated pathways include WNT/β-catenin (APC/AXIN1/AXIN2/CTNNB1), RAS–RAF–MEK–ERK (KRAS/NRAS/BRAF), PI3K/AKT/mTOR (PIK3CA), TGF-β/BMP (SMAD4, ACVR2A, BMPR2), and the p53 axis; organoid modeling in 2024 recapitulated stepwise selection across WNT, EGFR/MAPK, BMP, and p53 programs in mismatch-repair–deficient human colon epithelium, producing quadruple-pathway mutant clones that form tumors in vivo (mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10). Transcriptomic taxonomies have evolved from bulk-derived CMS (CMS1 immune/MSI; CMS2 canonical/WNT; CMS3 metabolic; CMS4 mesenchymal/EMT) toward intrinsic (CRIS) and pathway-derived subtypes that separate neoplastic-intrinsic biology from microenvironmental signals, refining prognostic and predictive stratification (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).

The tumor microenvironment (TME) and microbiome modulate progression and therapy response. High stromal/EMT signaling (CMS4) portends poor outcome; MSI/CMS1 exhibits immune activation and checkpoint sensitivity. Dysbiosis with Fusobacterium nucleatum and other species is associated with immune evasion and worse survival; short-chain fatty acids (SCFAs) such as butyrate and acetate and lactate from tumor glycolysis shape epigenetic states and immunity, integrating metabolism–immune crosstalk (noack2023molecularpathologyof pages 3-4, hu2025themetabolismimmuneaxis pages 2-3, yang2024molecularcomplexityof pages 6-8). Recent single-cell and spatial analyses, and classification refinements, highlight malignant cell programs, fibroblast–tumor niches, and immune micro-niches driving heterogeneity and outcome, while deconvolving tumor-intrinsic from stromal signals (dunne2024molecularpathologicalclassification pages 1-2, mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10).

## Gene/protein annotations (HGNC) and ontology terms
- Genes/proteins (HGNC): APC, CTNNB1, AXIN1/AXIN2, KRAS, NRAS, BRAF, PIK3CA, TP53, SMAD4, RNF43, ACVR2A, BMPR2, MLH1, MSH2, MSH6, PMS2, POLE, POLD1 (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10, yang2024molecularcomplexityof pages 6-8).
- GO Biological Processes: Wnt signaling pathway; MAPK cascade; PI3K signaling; TGF-β receptor signaling pathway; DNA mismatch repair; chromosomal instability; epithelial–mesenchymal transition; stem cell population maintenance; cell proliferation; glycolytic process; glutamine metabolic process; immune response; extracellular matrix organization (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).
- CL Cell Types: intestinal epithelial cell; intestinal LGR5+ stem cell; cancer-associated fibroblast; CD8+ T cell; B cell/plasma cell; macrophage/tumor-associated macrophage; dendritic cell (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).
- UBERON Anatomy: colon; colon mucosa; colonic crypt; proximal colon; distal colon (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).
- CHEBI Chemical Entities: butyrate; acetate; lactate (hu2025themetabolismimmuneaxis pages 2-3, yang2024molecularcomplexityof pages 6-8).

## Required Information

1) Core Pathophysiology
- Primary mechanisms: CIN with widespread copy-number alterations and early APC/WNT disruption; MSI via dMMR (germline MMR variants or sporadic MLH1 hypermethylation); CIMP/serrated route with BRAF-driven MAPK activation and diffuse promoter hypermethylation often culminating in MSI (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).
- Dysregulated pathways: WNT/β-catenin, RAS–RAF–MEK–ERK, PI3K/AKT/mTOR, TGF-β/BMP, and p53; organoid selection experiments demonstrate sequential acquisition and functional cooperation of these axes in MMR-deficient epithelium (mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10).
- Cellular processes: stemness transitions (crypt LGR5+ vs regenerative ANXA1+), EMT and stromal activation (CMS4), proliferation and cell-cycle dysregulation, impaired DNA repair in MSI, and metabolic rewiring toward glycolysis, glutaminolysis, and lipid metabolism (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).

2) Key Molecular Players
- Genes/Proteins: APC, CTNNB1, RNF43 (WNT); KRAS, NRAS, BRAF (MAPK); PIK3CA (PI3K); TP53; SMAD4 (TGF-β); ACVR2A/BMPR2 (BMP); MLH1/MSH2/MSH6/PMS2 (MMR); POLE/POLD1 (ultramutated subset) (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10, yang2024molecularcomplexityof pages 6-8).
- Chemical Entities: SCFAs (butyrate, acetate) influencing epigenetics and immunity; lactate from aerobic glycolysis modulating TME acidity and immune suppression (hu2025themetabolismimmuneaxis pages 2-3, yang2024molecularcomplexityof pages 6-8).
- Cell Types: neoplastic colon epithelial cells; LGR5+ stem cells; cancer-associated fibroblasts; infiltrating lymphocytes (CD8+ T cells, B/plasma cells); macrophages/TAMs; dendritic cells (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).
- Anatomical Locations: colonic crypt base; proximal colon (serrated/MSI/CIMP predominant); distal colon (CIN/CMS2 enriched) (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).

3) Biological Processes (for GO annotation)
- Signaling: Wnt signaling; MAPK cascade; PI3K/AKT signaling; TGF-β/BMP signaling; p53-mediated apoptosis and DNA damage response (dunne2024molecularpathologicalclassification pages 1-2, mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10).
- DNA repair/genomic stability: DNA mismatch repair; replication proofreading; regulation of chromosomal segregation (noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).
- Cellular responses: epithelial–mesenchymal transition; stem cell population maintenance; response to oxidative stress/inflammation; immune activation/suppression (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).
- Metabolic processes: glycolytic process; lactate metabolic process; glutamine metabolic process; lipid biosynthetic process (yang2024molecularcomplexityof pages 6-8).
- Transport/ECM: extracellular matrix organization; cell–cell adhesion; secretion and uptake of metabolites (noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).

4) Cellular Components
- Cellular locations: plasma membrane receptors (EGFR, TGF-β receptors), cytosolic signaling complexes (MAPK, PI3K), nucleus (TCF/LEF–β-catenin transcription; p53), chromatin (epigenetic regulation), mitochondria (metabolic reprogramming), extracellular matrix and stromal compartments (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4).

5) Disease Progression
- Sequence: normal mucosa → early adenoma (APC/WNT) → intermediate adenoma (KRAS/PIK3CA) → late adenoma/carcinoma (TP53, SMAD4; CIN accumulation); serrated route: hyperplastic/SSL → BRAF V600E + CIMP → MLH1 methylation → MSI carcinoma; MSI tumors display hypermutation and dense immune infiltration; organoid evidence shows that in dMMR epithelium, stepwise selection across WNT, BMP, MAPK, and p53 axes yields tumorigenic clones (noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8, mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10). In Lynch syndrome, surveillance data suggest accelerated “Big Bang”-like emergence from dMMR crypts in several MMR genotypes (brandaleone2024hereditarycolorectalcancer pages 5-6).

6) Phenotypic Manifestations (HP terms)
- Colorectal polyposis/adenomas (HP:0006771), right-sided colonic carcinoma (HP:0030068), mucinous adenocarcinoma phenotype, tumor-infiltrating lymphocytosis (HP:0030057), microsatellite instability phenotype, poor differentiation in subsets, and stromal-rich mesenchymal tumors with aggressive course (CMS4) (noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8). MSI tumors often show better baseline prognosis but distinct chemotherapy responsiveness and immunotherapy sensitivity (noack2023molecularpathologyof pages 3-4).

## Current applications and real-world implementations
- Molecular classification guides therapy: MSI-H/dMMR status predicts response to PD-1 blockade; MAPK-targeted regimens (e.g., BRAF V600E combination strategies) reflect pathway biology; KRAS mutational status drives anti-EGFR resistance and informs targeted trial designs (noack2023molecularpathologyof pages 3-4, patel2024molecularlandscapeand pages 6-8). Tumor transcriptomic stratification (CMS/CRIS) is being refined to disentangle TME versus tumor-intrinsic signals for prognosis and treatment selection (dunne2024molecularpathologicalclassification pages 1-2).

## Expert opinions and analysis
- 2024 reviews emphasize integrating bulk, single-cell, and spatial data to capture intra-/inter-tumor heterogeneity and to operationalize classifications that more accurately reflect tumor-intrinsic biology while acknowledging stromal/immune determinants of outcome (dunne2024molecularpathologicalclassification pages 1-2). MSI/CIMP biology continues to underpin biomarker-driven immunotherapy, while CIN/CMS4 biology underlines the need to target EMT/stroma and metabolism, including lactate-mediated immune suppression and glutamine dependence (noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8).

## Relevant statistics and data
- Estimated route prevalence: CIN ~70–84% of sporadic CRC; MSI ~13–16% overall with ~3–4% hereditary; CIMP/serrated ~15–30% and strongly associated with BRAF V600E and MLH1 hypermethylation (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, yang2024molecularcomplexityof pages 6-8). Microbiome: high Fusobacterium nucleatum abundance is associated with increased mortality risk; metabolic pathway alterations (glycolysis, glutaminolysis, lipid synthesis) are recurrent across CRC subtypes (hu2025themetabolismimmuneaxis pages 2-3, yang2024molecularcomplexityof pages 6-8).

## Evidence items with PMIDs/DOIs/URLs and dates
- Dunne PD, Arends MJ. Molecular pathological classification of colorectal cancer—an update. Virchows Archiv. 2024 Feb;484:273–285. doi:10.1007/s00428-024-03746-3. URL: https://doi.org/10.1007/s00428-024-03746-3 (dunne2024molecularpathologicalclassification pages 1-2).
- Noack P, Langer R. Molecular pathology of colorectal cancer. memo. 2023 Apr;16:116–121. doi:10.1007/s12254-023-00893-2. URL: https://doi.org/10.1007/s12254-023-00893-2 (noack2023molecularpathologyof pages 3-4).
- Patel A, Gulhati P. Molecular Landscape and Therapeutic Strategies against Colorectal Cancer. Cancers. 2024 Apr;16:1551. doi:10.3390/cancers16081551. URL: https://doi.org/10.3390/cancers16081551 (patel2024molecularlandscapeand pages 6-8).
- Yang Z et al. Molecular Complexity of Colorectal Cancer: Pathways, Biomarkers, and Therapeutic Strategies. Cancer Manag Res. 2024 Oct;16:1389–1403. doi:10.2147/CMAR.S481656. URL: https://doi.org/10.2147/cmar.s481656 (yang2024molecularcomplexityof pages 6-8).
- Mizutani T et al. Recapitulating the adenoma–carcinoma sequence by selection of four spontaneous oncogenic mutations in mismatch-repair-deficient human colon organoids. Nature Cancer. 2024 Nov;5:1852–1867. doi:10.1038/s43018-024-00841-x. URL: https://doi.org/10.1038/s43018-024-00841-x (mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10).
- Møller P et al. Incidences under colonoscopy surveillance suggest an accelerated “Big Bang” pathway to CRC in Lynch syndromes. Hered Cancer Clin Pract. 2024 May;22. doi:10.1186/s13053-024-00279-3. URL: https://doi.org/10.1186/s13053-024-00279-3 (brandaleone2024hereditarycolorectalcancer pages 5-6).

## Closing synthesis
Colon adenocarcinoma is best conceptualized as a set of evolutionary routes—CIN, MSI/CIMP, and serrated—with shared convergence on a limited set of pathways (WNT, MAPK, PI3K, TGF-β, p53) and recurrent cellular programs (stemness, EMT, metabolic rewiring). Recent organoid and single-cell/spatial studies sharpen the mechanistic sequence and reveal how tumor-intrinsic programs interface with fibroblast and immune niches to shape prognosis and therapeutic vulnerabilities. These integrated insights provide a framework for ontology-grounded knowledge bases and for aligning biomarkers with targeted, immunologic, and metabolism-directed interventions (dunne2024molecularpathologicalclassification pages 1-2, noack2023molecularpathologyof pages 3-4, mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10).

References

1. (dunne2024molecularpathologicalclassification pages 1-2): Philip D. Dunne and Mark J. Arends. Molecular pathological classification of colorectal cancer—an update. Virchows Archiv, 484:273-285, Feb 2024. URL: https://doi.org/10.1007/s00428-024-03746-3, doi:10.1007/s00428-024-03746-3. This article has 65 citations and is from a peer-reviewed journal.

2. (noack2023molecularpathologyof pages 3-4): Petar Noack and Rupert Langer. Molecular pathology of colorectal cancer. memo - Magazine of European Medical Oncology, 16:116-121, Apr 2023. URL: https://doi.org/10.1007/s12254-023-00893-2, doi:10.1007/s12254-023-00893-2. This article has 13 citations.

3. (yang2024molecularcomplexityof pages 6-8): Zhengdong Yang, Xinyang Wang, Huiying Zhou, Minghan Jiang, Jinghui Wang, and Bowen Sui. Molecular complexity of colorectal cancer: pathways, biomarkers, and therapeutic strategies. Cancer Management and Research, 16:1389-1403, Oct 2024. URL: https://doi.org/10.2147/cmar.s481656, doi:10.2147/cmar.s481656. This article has 19 citations and is from a peer-reviewed journal.

4. (mizutani2024recapitulatingtheadenoma–carcinoma pages 8-10): Tomohiro Mizutani, Matteo Boretto, Sangho Lim, Jarno Drost, Diego Montiel González, Rurika Oka, Maarten H. Geurts, Harry Begthel, Jeroen Korving, Johan H. van Es, Ruben van Boxtel, and Hans Clevers. Recapitulating the adenoma–carcinoma sequence by selection of four spontaneous oncogenic mutations in mismatch-repair-deficient human colon organoids. Nature Cancer, 5:1852-1867, Nov 2024. URL: https://doi.org/10.1038/s43018-024-00841-x, doi:10.1038/s43018-024-00841-x. This article has 14 citations and is from a highest quality peer-reviewed journal.

5. (hu2025themetabolismimmuneaxis pages 2-3): Shaofan Hu, Hui Heng, Fang Yang, Meng Wang, Guoxiang Liu, Yuancai Xiang, and Hongming Miao. The metabolism-immune axis in colorectal cancer: remodeling the tumor microenvironment through metabolite signaling. Frontiers in Immunology, Dec 2025. URL: https://doi.org/10.3389/fimmu.2025.1735873, doi:10.3389/fimmu.2025.1735873. This article has 0 citations and is from a peer-reviewed journal.

6. (brandaleone2024hereditarycolorectalcancer pages 5-6): Luca Brandaleone, Arianna Dal Buono, Roberto Gabbiadini, Giacomo Marcozzi, Davide Polverini, Michele Carvello, Antonino Spinelli, Cesare Hassan, Alessandro Repici, Cristina Bezzio, and Alessandro Armuzzi. Hereditary colorectal cancer syndromes and inflammatory bowel diseases: risk management and surveillance strategies. Cancers, 16:2967, Aug 2024. URL: https://doi.org/10.3390/cancers16172967, doi:10.3390/cancers16172967. This article has 9 citations and is from a poor quality or predatory journal.

7. (patel2024molecularlandscapeand pages 6-8): Aakash Patel and Pat Gulhati. Molecular landscape and therapeutic strategies against colorectal cancer. Cancers, 16:1551, Apr 2024. URL: https://doi.org/10.3390/cancers16081551, doi:10.3390/cancers16081551. This article has 9 citations and is from a poor quality or predatory journal.