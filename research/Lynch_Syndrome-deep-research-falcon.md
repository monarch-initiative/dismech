---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:41.575666'
end_time: '2025-12-15T09:12:09.059093'
duration_seconds: 627.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lynch Syndrome
  mondo_id: ''
  category: ''
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
- **Disease Name:** Lynch Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lynch Syndrome**.
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
- **Disease Name:** Lynch Syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lynch Syndrome**.
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
- Disease Name: Lynch Syndrome (LS; hereditary nonpolyposis colorectal cancer)
- MONDO ID: [not definitively confirmed here]
- Category: Hereditary cancer predisposition syndrome (DNA mismatch repair deficiency)

## Research Objectives: Pathophysiology of Lynch Syndrome

| Element | Representative items (IDs where requested) | Real-world implementations | Key 2023–24 statistics | Evidence |
|---|---|---|---:|---|
| Core pathophysiology | Germline heterozygous MMR defects → somatic "second hit" → MMR deficiency (dMMR) → microsatellite instability (MSI), hypermutation, frameshift neoantigens; cGAS–STING → type I IFN activation (GO:0006281; GO:0060337) | Tumor IHC (MLH1/MSH2/MSH6/PMS2) and MSI testing; germline multigene panels; somatic MLH1 methylation/BRAF to triage | LS explains ≈3% of CRC; dMMR produces hypermutated/MSI-H phenotype linked to neoantigens and immune activation | (sowter2024identifyingcandidatesfor pages 45-48, buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 2-3) |
| Key molecular players | HGNC symbols: MLH1, MSH2, MSH6, PMS2, EPCAM; CHEBI:15365 (acetylsalicylic acid = aspirin) | Diagnostic: four-stain IHC; NGS panels for germline/somatic; functional assays for VUS | Gene-specific penetrance: MLH1/MSH2 higher CRC risk; MSH6/PMS2 lower but significant; PMS2 carriage estimates (population) noted in recent series | (pallatt2025abriefreview pages 3-5, gomezmolina2025lynchsyndromeand pages 2-3) |
| Disrupted GO biological processes | DNA repair (GO:0006281); response to DNA damage (GO:0006974); type I interferon signaling (GO:0060337); immune response (GO:0006955) | Mechanistic rationale for PD-1/PD-L1 therapy and trials of STING/ATR modulators | dMMR/MSI-H tumours have high TMB and elevated neoantigen burden; immunotherapy ORR in dMMR cohorts reported in the literature in the ~40–60% range | (awosika2025deficientmismatchrepair pages 3-4, buono2024lynchsyndromefrom pages 1-2, sowter2024identifyingcandidatesfor pages 45-48) |
| Cellular components (GO CC) | Nucleus (GO:0005634); nucleoplasm (GO:0005654); cytosol (GO:0005829); endoplasmic reticulum (STING localization) (GO:0005783) | IHC staining patterns (loss/retention of MMR proteins) guide downstream testing | MMR protein loss by IHC (sensitivity ~83–92%; specificity ~89% reported for tumor screening workflows) | (sowter2024identifyingcandidatesfor pages 45-48, gomezmolina2025lynchsyndromeand pages 2-3) |
| Phenotypes (HPO) | Colorectal carcinoma; Endometrial carcinoma; multiple primary tumours; early-onset cancers (HPO terms used in KBs) | Clinical surveillance (colonoscopy, gynaecologic screening), risk-reducing surgery options | Lifetime risks vary by gene (examples: MLH1/MSH2 substantially elevated CRC/EC risk; MSH6/PMS2 more variable) | (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 2-3) |
| Cell types (CL) | Colonic/intestinal epithelial cells (colonocytes), endometrial epithelial cells, tumour-infiltrating CD8+ T cells | Studies of tumour microenvironment, vaccine targets (frameshift peptides) and biomarker assays | dMMR tumours characteristically show brisk lymphoid infiltration (TILs) and inflammatory signatures | (awosika2025deficientmismatchrepair pages 3-4, buono2024lynchsyndromefrom pages 3-5) |
| Anatomical locations (UBERON) | Colon (UBERON:0001155), endometrium, ovary, stomach, urinary tract, pancreas (LS tumour spectrum) | Site-specific surveillance programs and expanded universal screening in CRC/EC | LS contributes to increased lifetime risk across these organs; percent contribution of LS varies by tumour type (e.g., ~3% CRC, higher proportions among dMMR cases) | (buono2024lynchsyndromefrom pages 1-2, gomezmolina2025lynchsyndromeand pages 2-3) |
| Real-world implementations | Universal tumor screening (IHC/MSI), reflex MLH1 methylation and BRAF testing to distinguish sporadic MLH1-silenced tumours; germline testing; PD-1 inhibitors for dMMR/MSI-H cancers; aspirin chemoprevention (CAPP trials) and experimental FSP vaccines | Health-system pathways: tumor -> methylation/BRAF -> germline referral; ICI approved for dMMR/MSI-H across tumour types | Implementation gaps reported (underdiagnosis / incomplete testing uptake); established therapeutic benefit of checkpoint blockade in dMMR tumours | (sowter2024identifyingcandidatesfor pages 45-48, buono2024lynchsyndromefrom pages 3-5, buono2024lynchsyndromefrom pages 1-2) |
| Key 2023–24 statistics | Population prevalence estimates: LS carrier frequency reported in range ~1:300–1:1000 (variable by cohort); LS accounts for ~3% of CRC; IHC/MSI testing sensitivity/specificity and immunotherapy ORR ranges | Examples: proportion of CRCs screened and referral gaps documented; immunotherapy response rates in dMMR cohorts reported in recent trials/reviews | Screening and surveillance modify observed penetrance; actionable ICI response rates commonly reported ~40–60% in dMMR cohorts; aspirin/resistant starch trials ongoing for prevention | (sowter2024identifyingcandidatesfor pages 45-48, awosika2025deficientmismatchrepair pages 3-4, buono2024lynchsyndromefrom pages 1-2) |


*Table: Compact, evidence-linked table summarizing core pathophysiology, molecular players (HGNC/CHEBI), disrupted GO processes and cellular components, phenotypes, cell types, anatomical sites, implementations and key 2023–24 statistics for Lynch syndrome; intended for embedding in a knowledge-base entry. Evidence column lists the context IDs supporting each row.*

> "A germline hit plus somatic second alteration leads to dMMR, producing accelerated carcinogenesis, high frameshift mutation rates and MSI." (buono2024lynchsyndromefrom pages 3-5)

> "Only 44% of CRCs were screened for dMMR." (mcronald2024identificationofpeople pages 1-2)

> "Only 1.3% of CRC patients had a germline MMR genetic test performed." (mcronald2024identificationofpeople pages 1-2)

> "Only 22.73% (45/198 MSI-high cases) underwent germline testing; ... MLH1 methylation testing is 'barely ever requested' in clinical practice." (papadopoulou2024microsatelliteinstabilityis pages 1-2)

> "The ORR was 58.8% and the PFS24 rate was 64.7%." (friedman2024nivolumabformismatchrepairdeficient pages 1-2)

> "Hereditary syndromes associated with EC include Lynch syndrome." (ranganathan2023prevalenceandclinical pages 10-11)


*Blockquote: Direct, citable quotes highlighting core mechanism (germline + second hit → dMMR/MSI), major implementation gaps in tumor/germline testing in England and practice, limited use of MLH1 methylation reflex testing, and immunotherapy outcomes (nivolumab) in dMMR gynecologic cancers.*

### 1) Core Pathophysiology: Key concepts and definitions
- Definition and inheritance: Lynch syndrome is an autosomal-dominant cancer predisposition syndrome caused by germline pathogenic variants in DNA mismatch repair (MMR) genes—MLH1, MSH2, MSH6, PMS2—or 3′ EPCAM deletions that epigenetically silence MSH2. Tumorigenesis follows a “two-hit” model: the germline hit plus a somatic second hit inactivates the remaining allele, leading to mismatch repair deficiency (dMMR) and microsatellite instability (MSI) with a hypermutated phenotype (reviewed in 2024–2025 sources). URL: https://doi.org/10.3390/cancers16050849; https://doi.org/10.32604/or.2025.063951 (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 1-2, gomezmolina2025lynchsyndromeand pages 2-3)
- Molecular mechanism: Loss of MMR function impairs recognition and repair of base–base mismatches and insertion/deletion loops (MutSα: MSH2/MSH6; MutSβ: MSH2/MSH3; MutLα: MLH1/PMS2), driving genome-wide MSI and accumulation of frameshift mutations in coding repeats. These frameshifts generate neoantigens and underlie the immunogenic tumor microenvironment typical of dMMR/MSI-H cancers. URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Immune consequences: Hypermutation and frameshift neoantigens are associated with brisk lymphocytic infiltration and clinical sensitivity to PD-1 blockade across dMMR/MSI-H tumors. URL: https://doi.org/10.3390/ijms26094394; https://doi.org/10.3390/cancers16050849 (awosika2025deficientmismatchrepair pages 3-4, buono2024lynchsyndromefrom pages 3-5)
- Screening paradigm (definition in practice): Tumor-based universal screening for dMMR/MSI by IHC and/or MSI testing with reflex MLH1 promoter methylation and BRAF V600E testing distinguishes sporadic MLH1-hypermethylated tumors from LS, and positive screens prompt germline testing. URL: (overview) https://doi.org/10.3390/cancers16050849; implementation data: https://doi.org/10.1038/s41431-024-01550-w; https://doi.org/10.1200/po.23.00332 (buono2024lynchsyndromefrom pages 3-5, mcronald2024identificationofpeople pages 1-2, papadopoulou2024microsatelliteinstabilityis pages 1-2)

Latest mechanistic understanding (2023–2024 emphasis):
- dMMR/MSI produces high tumor mutational burden and frameshift peptide neoantigens; the dMMR microenvironment is often “hot,” with effector T-cell infiltration, contributing to responsiveness to checkpoint inhibitors (PD-1/PD-L1). URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Early MSI/dMMR crypts in normal mucosa are reported as potential occult precursors in LS, supporting accelerated adenoma-to-carcinoma progression in some carriers. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)

### 2) Key molecular players
- Genes/Proteins (HGNC): MLH1, MSH2, MSH6, PMS2, EPCAM (EPCAM 3′ deletions cause MSH2 silencing). URL: https://doi.org/10.3390/cancers16050849; https://doi.org/10.32604/or.2025.063951 (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 1-2, gomezmolina2025lynchsyndromeand pages 2-3)
- Chemical entities (CHEBI): Acetylsalicylic acid (aspirin; CHEBI:15365) has emerging chemopreventive evidence in LS; resistant starch is also under study. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)
- Cell types (CL): Colonic/intestinal epithelium and endometrial epithelium are primary tissues of origin; tumor-infiltrating lymphocytes (notably CD8+ T cells) typify dMMR/MSI-H tumors. URL: https://doi.org/10.3390/ijms26094394; https://doi.org/10.3390/cancers16050849 (awosika2025deficientmismatchrepair pages 3-4, buono2024lynchsyndromefrom pages 3-5)
- Anatomical locations (UBERON): Colon and rectum, endometrium, ovary, stomach, urinary tract, and other LS-spectrum sites. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)

### 3) Biological processes (GO terms) dysregulated
- DNA repair (GO:0006281), mismatch repair (component of GO:0006281), response to DNA damage stimulus (GO:0006974). URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Antigen processing/immune response (GO:0006955) and Type I interferon signaling (GO:0060337) consistent with immunogenic dMMR/MSI-H microenvironments. URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)

### 4) Cellular components
- Nucleus/nucleoplasm where MMR operates (GO:0005634; GO:0005654) and cytosol (GO:0005829); checkpoint signaling impacts antigen presentation pathways. URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Practical laboratory components: Loss of MLH1/MSH2/MSH6/PMS2 staining by IHC supports dMMR designation; IHC sensitivity ~83–92% and specificity ~89% are reported in screening workflows. URL: (overview) [Sowter 2024, assay performance described] (sowter2024identifyingcandidatesfor pages 45-48)

### 5) Disease progression (sequence of events)
- From germline predisposition to cancer: (i) germline pathogenic variant (MLH1/MSH2/MSH6/PMS2; EPCAM deletion), (ii) somatic “second hit” (mutation/LOH/epigenetic inactivation), (iii) dMMR and MSI leading to hypermutation and frameshifted coding sequences, (iv) clonal expansion of MSI adenomas/carcinomas with an immunogenic TME. URL: https://doi.org/10.3390/cancers16050849; https://doi.org/10.32604/or.2025.063951 (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 1-2, gomezmolina2025lynchsyndromeand pages 2-3)
- Accelerated adenoma–carcinoma sequence relative to sporadic CRC has been reported in LS, consistent with interval cancers and detection of dMMR crypts. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)

### 6) Phenotypic manifestations (clinical)
- Cancer spectrum and penetrance: Elevated lifetime risks of colorectal cancer (CRC), endometrial cancer (EC), and several extracolonic cancers. Gene-specific risks are higher for MLH1/MSH2 and generally lower for MSH6/PMS2, though substantial and variable by cohort and surveillance intensity. URLs: https://doi.org/10.3390/cancers16050849; https://doi.org/10.32604/or.2025.063951 (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 2-3)
- Tumor biology: dMMR/MSI-H tumors are typically right-sided in CRC, hypermutated, with lymphoid infiltration and favorable immunotherapy responsiveness. URL: https://doi.org/10.3390/ijms26094394; https://doi.org/10.3390/cancers16050849 (awosika2025deficientmismatchrepair pages 3-4, buono2024lynchsyndromefrom pages 3-5)

## Recent developments and latest research (2023–2024 priority)
- Real-world implementation in England (2019 baseline): Only 44% of CRCs underwent tumor dMMR testing; among dMMR-positive tumors, only 51% received subsequent diagnostic testing; just 1.3% of all CRC patients had germline MMR testing, with marked geographic variation—indicating large gaps in universal screening and cascade to germline. Full implementation could identify ~700 additional LS index cases per year in England. URL (online 15 Feb 2024): https://doi.org/10.1038/s41431-024-01550-w (mcronald2024identificationofpeople pages 1-2, mcronald2024identificationofpeople pages 7-8)
- Pan-cancer MSI biomarker underused for LS work-up: In a 2020–2023 series (n=4,553), MSI-high rate was 5.27% overall (endometrial 15.69%, gastric 8.54%, colorectal 7.40%), yet only 22.73% of MSI-high cases underwent germline testing; MLH1 promoter methylation could explain sporadic origin in 42.5% of MSI-high cases, but methylation testing was “barely ever requested”—highlighting reflex testing shortfalls. URL (Feb 2024): https://doi.org/10.1200/po.23.00332 (papadopoulou2024microsatelliteinstabilityis pages 1-2)
- Immunotherapy outcomes in dMMR gynecologic cancers: A phase 2 single-arm trial of nivolumab in dMMR uterine/ovarian cancers (n=35) reported ORR 58.8%, 24-week PFS 64.7%, DCR 73.5%, median OS not reached at 42.1 months’ follow-up; safety acceptable (29% grade 3–4 TRAEs, no grade 5). URL (Apr 2024): https://doi.org/10.1038/s41591-024-02942-7 (friedman2024nivolumabformismatchrepairdeficient pages 1-2)
- Contemporary reviews reinforce LS mechanisms and clinical strategies, including multigene testing, surveillance, and the promise of aspirin/resistant starch and vaccines targeting frameshift peptides. URLs: https://doi.org/10.3390/cancers16050849; https://doi.org/10.32604/or.2025.063951 (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 1-2)

## Current applications and real-world implementations
- Universal tumor screening: IHC for MLH1/MSH2/MSH6/PMS2 and/or MSI testing; reflex MLH1 promoter methylation and BRAF V600E to triage sporadic MLH1-deficient tumors; positive cases proceed to genetic counseling and germline testing. Practical assay performance (IHC sensitivity/specificity) and pipeline considerations are summarized in recent 2024 overviews, but substantial implementation gaps persist (see above). URLs: overview (2024) [Sowter], https://doi.org/10.1038/s41431-024-01550-w; https://doi.org/10.1200/po.23.00332 (sowter2024identifyingcandidatesfor pages 45-48, mcronald2024identificationofpeople pages 1-2, papadopoulou2024microsatelliteinstabilityis pages 1-2)
- Immunotherapy: PD-1 inhibitors (e.g., nivolumab, pembrolizumab) are effective across dMMR/MSI-H tumors; in dMMR gynecologic cancers, nivolumab achieved ORR ~59% with durable control in a phase 2 trial. URL: https://doi.org/10.1038/s41591-024-02942-7 (friedman2024nivolumabformismatchrepairdeficient pages 1-2)
- Prevention: Aspirin chemoprevention is supported by randomized trial data historically (CAPP), with ongoing optimization of dose/implementation; resistant starch and frameshift peptide vaccines are emerging strategies discussed in 2024 reviews. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)

## Expert opinions and authoritative guidance (2023–2024)
- Guidance trend: Expert reviews emphasize multigene panel testing for suspected LS, universal tumor screening in incident CRC and EC, and reflex MLH1 methylation/BRAF testing before germline referral, noting continued underdiagnosis due to real-world pathway attrition. URL: https://doi.org/10.3390/cancers16050849; https://doi.org/10.1038/s41431-024-01550-w; https://doi.org/10.1200/po.23.00332 (buono2024lynchsyndromefrom pages 3-5, mcronald2024identificationofpeople pages 1-2, papadopoulou2024microsatelliteinstabilityis pages 1-2)
- Immunotherapy perspective: High dMMR/MSI-H immunogenicity rationalizes PD-1 blockade as standard; new gynecologic-cancer data (nivolumab) add disease-specific validation and suggest microenvironmental biomarkers associated with durability (e.g., dysfunctional CD8+PD-1+ T cells). URL: https://doi.org/10.1038/s41591-024-02942-7 (friedman2024nivolumabformismatchrepairdeficient pages 1-2)

## Relevant statistics and data (recent)
- England 2019 national dataset: 44% of CRCs tested for dMMR; among dMMR, only 51% had further diagnostic testing; 1.3% of all CRC patients had germline MMR testing; estimated +700 LS cases/year with full implementation. URL: https://doi.org/10.1038/s41431-024-01550-w (mcronald2024identificationofpeople pages 1-2, mcronald2024identificationofpeople pages 7-8)
- Real-world MSI-to-germline cascade: Only 22.73% of MSI-high cases had germline testing; MLH1 methylation could explain 42.5% sporadic origin in CRC/EC, but methylation testing rarely requested. URL: https://doi.org/10.1200/po.23.00332 (papadopoulou2024microsatelliteinstabilityis pages 1-2)
- dMMR gynecologic cancer trial: Nivolumab ORR 58.8%, PFS24 64.7%, DCR 73.5%, median OS not reached at ~42 months’ follow-up; 29% grade 3–4 TRAEs, no grade 5. URL: https://doi.org/10.1038/s41591-024-02942-7 (friedman2024nivolumabformismatchrepairdeficient pages 1-2)

## Knowledge base annotations
- Pathophysiology description: Germline pathogenic variants in MLH1/MSH2/MSH6/PMS2 (or EPCAM deletions) predispose to cancer. Biallelic inactivation in tumors causes dMMR and MSI, leading to hypermutation and frameshift neoantigens, an inflamed tumor microenvironment, and sensitivity to PD-1 blockade. URL: https://doi.org/10.3390/cancers16050849; https://doi.org/10.3390/ijms26094394 (buono2024lynchsyndromefrom pages 3-5, awosika2025deficientmismatchrepair pages 3-4)
- Gene/protein annotations (HGNC): MLH1; MSH2; MSH6; PMS2; EPCAM. EPCAM 3’ deletions silence MSH2 via promoter methylation. URL: https://doi.org/10.32604/or.2025.063951 (gomezmolina2025lynchsyndromeand pages 1-2)
- GO biological processes: DNA repair (GO:0006281); response to DNA damage (GO:0006974); immune response (GO:0006955); type I interferon signaling (GO:0060337). URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Cellular components: Nucleus (GO:0005634), nucleoplasm (GO:0005654), cytosol (GO:0005829). URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Phenotype associations (HPO): Colorectal carcinoma; endometrial carcinoma; multiple primary tumors; early-onset malignancy. URLs: https://doi.org/10.3390/cancers16050849; https://doi.org/10.32604/or.2025.063951 (buono2024lynchsyndromefrom pages 3-5, gomezmolina2025lynchsyndromeand pages 2-3)
- Cell type involvement (CL): Colonic epithelial cells; endometrial epithelial cells; tumor-infiltrating CD8+ T cells. URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- Anatomical locations (UBERON): Colon (UBERON:0001155), endometrium, ovary, stomach, urinary tract. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)
- Chemical entities (CHEBI): Acetylsalicylic acid (CHEBI:15365) as chemoprevention under study. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)

## Evidence items (with PMIDs or URLs)
- Buono AD et al., 2024 (Cancers): Multidisciplinary management, molecular carcinogenesis, and prevention strategies in LS; includes aspirin/resistant starch/vaccine discussion. URL: https://doi.org/10.3390/cancers16050849 (buono2024lynchsyndromefrom pages 3-5)
- Gómez-Molina R et al., 2025 (Oncology Research): Molecular genetics of LS, EPCAM mechanism, surveillance strategies; penetrance variation. URL: https://doi.org/10.32604/or.2025.063951 (gomezmolina2025lynchsyndromeand pages 1-2, gomezmolina2025lynchsyndromeand pages 2-3)
- Awosika JA et al., 2025 (IJMS): Overview of dMMR/MSI across solid tumors; immunogenic profile and ICI responsiveness. URL: https://doi.org/10.3390/ijms26094394 (awosika2025deficientmismatchrepair pages 3-4)
- McRonald F et al., 2024 (Eur J Hum Genet): England 2019 real-world LS diagnostic pathway; under-testing and under-referral; potential +700 LS/year with full implementation. URL: https://doi.org/10.1038/s41431-024-01550-w (mcronald2024identificationofpeople pages 1-2, mcronald2024identificationofpeople pages 7-8)
- Papadopoulou E et al., 2024 (JCO Precision Oncology): MSI as biomarker; low rates of germline testing and MLH1 methylation reflex in practice. URL: https://doi.org/10.1200/po.23.00332 (papadopoulou2024microsatelliteinstabilityis pages 1-2)
- Friedman CF et al., 2024 (Nature Medicine): Nivolumab in dMMR gynecologic cancers—ORR 58.8%, PFS24 64.7%, durable control. URL: https://doi.org/10.1038/s41591-024-02942-7 (friedman2024nivolumabformismatchrepairdeficient pages 1-2)
- Sowter P., 2024: Screening pipelines and assay performance; IHC sensitivity/specificity context and UK testing frameworks. (sowter2024identifyingcandidatesfor pages 45-48)

## Plan status and completion
Objectives were defined, evidence gathered, structured artifacts created, and the comprehensive report compiled with 2023–2024 prioritized sources and precise URLs. All objectives are completed.


References

1. (sowter2024identifyingcandidatesfor pages 45-48): P Sowter. Identifying candidates for chemopreventative aspirin prophylaxis: improving the detection of mmrd. Unknown journal, 2024.

2. (buono2024lynchsyndromefrom pages 3-5): Arianna Dal Buono, Alberto Puccini, Gianluca Franchellucci, Marco Airoldi, Michela Bartolini, Paolo Bianchi, Armando Santoro, Alessandro Repici, and Cesare Hassan. Lynch syndrome: from multidisciplinary management to precision prevention. Cancers, 16:849, Feb 2024. URL: https://doi.org/10.3390/cancers16050849, doi:10.3390/cancers16050849. This article has 20 citations and is from a poor quality or predatory journal.

3. (gomezmolina2025lynchsyndromeand pages 2-3): Raquel Gómez-Molina, Raquel Martínez, Miguel Suárez, Ana PEÑA-CABIA, MARíA CONCEPCIóN Calderón, and Jorge Mateo. Lynch syndrome and colorectal cancer: a review of current perspectives in molecular genetics and clinical strategies. Oncology Research, 33:1531-1545, Jun 2025. URL: https://doi.org/10.32604/or.2025.063951, doi:10.32604/or.2025.063951. This article has 5 citations and is from a peer-reviewed journal.

4. (pallatt2025abriefreview pages 3-5): Sneha Pallatt, Sibin Nambidi, Subhamay Adhikary, Antara Banerjee, Surajit Pathak, and Asim K. Duttaroy. A brief review of lynch syndrome: understanding the dual cancer risk between endometrial and colorectal cancer. Oncology Reviews, May 2025. URL: https://doi.org/10.3389/or.2025.1549416, doi:10.3389/or.2025.1549416. This article has 4 citations.

5. (awosika2025deficientmismatchrepair pages 3-4): Joy A. Awosika, James L. Gulley, and Danielle M. Pastor. Deficient mismatch repair and microsatellite instability in solid tumors. International Journal of Molecular Sciences, 26:4394, May 2025. URL: https://doi.org/10.3390/ijms26094394, doi:10.3390/ijms26094394. This article has 6 citations and is from a poor quality or predatory journal.

6. (buono2024lynchsyndromefrom pages 1-2): Arianna Dal Buono, Alberto Puccini, Gianluca Franchellucci, Marco Airoldi, Michela Bartolini, Paolo Bianchi, Armando Santoro, Alessandro Repici, and Cesare Hassan. Lynch syndrome: from multidisciplinary management to precision prevention. Cancers, 16:849, Feb 2024. URL: https://doi.org/10.3390/cancers16050849, doi:10.3390/cancers16050849. This article has 20 citations and is from a poor quality or predatory journal.

7. (mcronald2024identificationofpeople pages 1-2): Fiona E. McRonald, Joanna Pethick, Francesco Santaniello, Brian Shand, Adele Tyson, Oliver Tulloch, Shilpi Goel, Margreet Lüchtenborg, Gillian M. Borthwick, Clare Turnbull, Adam C. Shaw, Kevin J. Monahan, Ian M. Frayling, Steven Hardy, and John Burn. Identification of people with lynch syndrome from those presenting with colorectal cancer in england: baseline analysis of the diagnostic pathway. European Journal of Human Genetics, 32:529-538, Feb 2024. URL: https://doi.org/10.1038/s41431-024-01550-w, doi:10.1038/s41431-024-01550-w. This article has 13 citations and is from a domain leading peer-reviewed journal.

8. (papadopoulou2024microsatelliteinstabilityis pages 1-2): Eirini Papadopoulou, George Rigas, Elena Fountzilas, Anastasios Boutis, Stylianos Giassas, Nikolaos Mitsimponas, Danai Daliani, Dimitrios C Ziogas, Michalis Liontos, Vasileios Ramfidis, Charalampos Christophilakis, Dimitris Matthaios, Theofanis Floros, Chrysiida Florou-Chatzigiannidou, Konstantinos Agiannitopoulos, Angeliki Meintani, Aikaterini Tsantikidi, Anastasia Katseli, Kevisa Potska, Georgios Tsaousis, Vasiliki Metaxa-Mariatou, and George Nasioulas. Microsatellite instability is insufficiently used as a biomarker for lynch syndrome testing in clinical practice. JCO Precision Oncology, Feb 2024. URL: https://doi.org/10.1200/po.23.00332, doi:10.1200/po.23.00332. This article has 13 citations and is from a peer-reviewed journal.

9. (friedman2024nivolumabformismatchrepairdeficient pages 1-2): Claire F. Friedman, Beryl L. Manning-Geist, Qin Zhou, Tara Soumerai, Aliya Holland, Arnaud Da Cruz Paula, Hunter Green, Melih Arda Ozsoy, Alexia Iasonos, Travis Hollmann, Mario M. Leitao, Jennifer J. Mueller, Vicky Makker, William P. Tew, Roisin E. O’Cearbhaill, Ying L. Liu, Maria M. Rubinstein, Tiffany Troso-Sandoval, Stuart M. Lichtman, Alison Schram, Chrisann Kyi, Rachel N. Grisham, Pamela Causa Andrieu, E. John Wherry, Carol Aghajanian, Britta Weigelt, Martee L. Hensley, and Dmitriy Zamarin. Nivolumab for mismatch-repair-deficient or hypermutated gynecologic cancers: a phase 2 trial with biomarker analyses. Nature Medicine, 30:1330-1338, Apr 2024. URL: https://doi.org/10.1038/s41591-024-02942-7, doi:10.1038/s41591-024-02942-7. This article has 22 citations and is from a highest quality peer-reviewed journal.

10. (ranganathan2023prevalenceandclinical pages 10-11): Megha Ranganathan, Rosalba E. Sacca, Magan Trottier, Anna Maio, Yelena Kemel, Erin Salo-Mullen, Amanda Catchings, Sarah Kane, Chiyun Wang, Vignesh Ravichandran, Ryan Ptashkin, Nikita Mehta, Julio Garcia-Aguilar, Martin R. Weiser, Mark T.A. Donoghue, Michael F. Berger, Diana Mandelker, Michael F. Walsh, Maria Carlo, Ying L. Liu, Andrea Cercek, Rona Yaeger, Leonard Saltz, Neil H. Segal, Robin B. Mendelsohn, Arnold J. Markowitz, Kenneth Offit, Jinru Shia, Zsofia K. Stadler, and Alicia Latham. Prevalence and clinical implications of mismatch repair-proficient colorectal cancer in patients with lynch syndrome. JCO Precision Oncology, May 2023. URL: https://doi.org/10.1200/po.22.00675, doi:10.1200/po.22.00675. This article has 15 citations and is from a peer-reviewed journal.

11. (gomezmolina2025lynchsyndromeand pages 1-2): Raquel Gómez-Molina, Raquel Martínez, Miguel Suárez, Ana PEÑA-CABIA, MARíA CONCEPCIóN Calderón, and Jorge Mateo. Lynch syndrome and colorectal cancer: a review of current perspectives in molecular genetics and clinical strategies. Oncology Research, 33:1531-1545, Jun 2025. URL: https://doi.org/10.32604/or.2025.063951, doi:10.32604/or.2025.063951. This article has 5 citations and is from a peer-reviewed journal.

12. (mcronald2024identificationofpeople pages 7-8): Fiona E. McRonald, Joanna Pethick, Francesco Santaniello, Brian Shand, Adele Tyson, Oliver Tulloch, Shilpi Goel, Margreet Lüchtenborg, Gillian M. Borthwick, Clare Turnbull, Adam C. Shaw, Kevin J. Monahan, Ian M. Frayling, Steven Hardy, and John Burn. Identification of people with lynch syndrome from those presenting with colorectal cancer in england: baseline analysis of the diagnostic pathway. European Journal of Human Genetics, 32:529-538, Feb 2024. URL: https://doi.org/10.1038/s41431-024-01550-w, doi:10.1038/s41431-024-01550-w. This article has 13 citations and is from a domain leading peer-reviewed journal.