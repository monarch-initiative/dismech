---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:46:26.240645'
end_time: '2025-12-18T09:56:25.370475'
duration_seconds: 599.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Hepatitis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Autoimmune Hepatitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Autoimmune Hepatitis**.
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
- **Disease Name:** Autoimmune Hepatitis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Autoimmune Hepatitis**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Autoimmune Hepatitis (AIH)
- MONDO ID: not retrieved in this search
- Category: Autoimmune

Pathophysiology overview
Autoimmune hepatitis is a chronic, immune-mediated inflammatory liver disease characterized by serum IgG elevation, autoantibodies, and interface hepatitis with a lymphoplasmacytic infiltrate. Genetic predisposition is dominated by HLA risk alleles; adaptive immunity against liver autoantigens (notably SepSecS/SLA, CYP2D6, FTCD/LC1) is driven by autoreactive CD4+ T cells and B cells with class-switched, affinity-matured responses. Disruption of tolerance involves T cell activation/exhaustion programs and B cell antigen presentation. Hepatic injury and fibrosis are propagaged by inflammatory cytokine signaling pathways and sustained immune cell infiltration. Gut–liver axis perturbations (metabolites and barrier dysfunction) further amplify hepatic immune activation. Immune checkpoint modulation can precipitate a clinically similar immune-mediated hepatitis, underscoring a T cell–centric mechanism of injury. (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3, sun2024thesignificanceof pages 1-2, liu2023immunemediatedhepatitisinduced pages 1-2, kocheise2024pd1pdl1immunecheckpoint pages 1-2)

1) Core pathophysiology: key mechanisms, pathways, processes
- Genetic susceptibility (HLA): Fine-mapping in 1,622 AIH type 1 cases (Han Chinese) identified independent MHC signals with strongest association at HLA-B*35:01 (OR 7.32), additional HLA-B*08:01 and rs7765379, and peptide-binding groove residue HLA-B Phe67, with transethnic support for classic DRB1 alleles (DRB1*03:01, DRB1*04:01/04:05) known in European cohorts. Quote: “A total of 588 HLA variants were significantly associated with AIH… the strongest allele was in the HLA-B gene (HLA-B*35:01, p = 8.17×10−304; OR = 7.32)… position 67… phenylalanine of the HLA-B molecule… at the peptide binding groove.” (JHEP Reports, 2024-01 online, https://doi.org/10.1016/j.jhepr.2023.100926) (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- Non-HLA risk: Case-control genetics in North Indian adults reported predisposition with HLA-DRB1*03 and implicated non-HLA immune-regulatory loci CTLA4 and PTPN22 polymorphisms in AIH susceptibility. (Frontiers in Immunology, 2023-01, https://doi.org/10.3389/fimmu.2022.984083) (ahuja2023hlaandnonhla pages 10-11)
- Autoantigens and adaptive autoimmunity: Clonal B/T-cell analysis demonstrates anti-SepSecS (SLA) responses are class-switched (IgG1), affinity-matured, recognizing multiple epitopes, with SepSecS-specific CD4+ T cell clones producing IFN-γ, IL-4 and IL-10 and clonal expansion detectable in blood and liver. Quote: “The anti-SepSecS mAbs isolated were primarily IgG1, affinity-matured… SepSecS-specific CD4+ T cell clones… produced IFN-γ, IL-4, and IL-10… clonally expanded in both blood and liver biopsy.” (J Clin Invest, 2025-01, https://doi.org/10.1172/JCI183776) (kramer2025clonalanalysisof pages 1-2)
- B cells and plasma cells: B cells contribute via antigen presentation to autoreactive T cells, autoantibody production, cytokine generation (promoting Th1/Th17), and inhibition of Treg/Breg; B cell–targeted therapy is effective in refractory AIH, supporting mechanistic involvement. (Semin Liver Dis, 2019-11, https://doi.org/10.1055/s-0039-1688751) (taylor2019thecontributionof pages 1-3)
- T cell dysregulation and checkpoints: In immune checkpoint inhibitor (ICI)–mediated hepatitis, the mechanism is “mainly the overactivation of T cells,” providing a human model of T cell–driven hepatic autoimmunity that resembles AIH. Quote: “the mechanism of IMH induced by immune checkpoint inhibitors is mainly the overactivation of T cells.” (Frontiers in Pharmacology, 2023-01, https://doi.org/10.3389/fphar.2022.1077468) (liu2023immunemediatedhepatitisinduced pages 1-2)
- Microbiome–gut–liver axis: AIH is associated with reduced bacterial diversity and altered metabolites—decreased secondary bile acids, SCFAs, polyamines; increased LPS and certain amino acid metabolites—implicated in immune activation via PRR and cytokine pathways. Quote: “decreased in secondary bile acids, short-chain fatty acids (SCFAs), and polyamines, and increased in lipopolysaccharide (LPS)… can disrupt immune homeostasis by activating various immune cells and immune-related signaling pathways.” (Frontiers in Cellular and Infection Microbiology, 2024-02, https://doi.org/10.3389/fcimb.2024.1337223) (sun2024thesignificanceof pages 1-2)
- Fibrosis signaling: While specific single-cell fibrosis programs were not directly profiled in AIH in the retrieved texts, inflammatory cytokines (e.g., IFN-γ, IL-17 family), chemokines (e.g., CXCL10 cited in related AIH transcriptomics), and canonical pathways (NF-κB, JAK–STAT) are implicated by proximity to T cell/B cell activation, and by overlap with immune-mediated hepatitis biology. (chi2025decodingthedistinct pages 16-16, liu2023immunemediatedhepatitisinduced pages 1-2)

2) Key molecular players
- Genes/Proteins (HGNC):
  - HLA-DRB1 (risk alleles DRB1*03:01, DRB1*04 subtypes), HLA-B (notably B*35:01; peptide-binding residue 67), HLA-DQB1 (e.g., DQB1*04:01, *06:02) (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
  - CTLA4 (Cytotoxic T-lymphocyte–associated protein 4) (ahuja2023hlaandnonhla pages 10-11)
  - PTPN22 (Protein tyrosine phosphatase non-receptor type 22) (ahuja2023hlaandnonhla pages 10-11)
  - SEPSECS (SLA/LP antigen), CYP2D6 (LKM1 antigen), FTCD (LC1 antigen) (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
  - Cytokines: IFNG, IL4, IL10 (produced by SepSecS-specific CD4+ T cells) (kramer2025clonalanalysisof pages 1-2)
- Chemical entities (ChEBI):
  - Short-chain fatty acids (e.g., butyrate), secondary bile acids, lipopolysaccharide (LPS) (sun2024thesignificanceof pages 1-2)
- Cell types (CL):
  - CD4+ T cells (CL:0000624); Regulatory T cells (Tregs, CL:0000815); Th17 cells (CL:0000894); Peripheral helper/Tfh-like CD4+ cells (inferred from B cell help); CD8+ T cells (CL:0000625); B cells (CL:0000236); Plasma cells (CL:0000786) (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- Anatomical locations (UBERON):
  - Liver (UBERON:0002107), portal tracts/interface; bile ducts (UBERON:0002394) (context of overlap syndromes) (taylor2019thecontributionof pages 1-3)

3) Biological processes (GO terms) implicated
- Antigen processing and presentation of peptide antigen via MHC class I/II (GO:0042590; GO:0019882) – supported by HLA fine mapping and peptide-binding residue association (HLA-B 67) (li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- T cell activation and differentiation, including regulation of T cell activation (GO:0050863), Th1/Th2/Th17 differentiation (GO:0042093; GO:0042094; GO:1902105) – reflected by SepSecS-specific CD4+ T cell cytokine profiles and B cell cytokine effects (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- B cell activation, antigen presentation and immunoglobulin production (GO:0042113; GO:0002376; GO:0002377) – based on B cell roles and affinity-matured anti-SepSecS antibodies (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- Response to lipopolysaccharide (GO:0032496), bile acid metabolic process (GO:0008206), and SCFA signaling (GO processes related to GPCR signaling) – microbiome-mediated immune activation (sun2024thesignificanceof pages 1-2)
- Cytokine-mediated signaling pathways including JAK–STAT (GO:0007259) and NF-κB (GO:0043122) – inferred from immune activation and IMH pathophysiology (liu2023immunemediatedhepatitisinduced pages 1-2)

4) Cellular components
- MHC class I/II protein complexes (GO:0042612; GO:0042611) (li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- Immunological synapse (GO:0001772) – site of T–B interaction and T cell activation (taylor2019thecontributionof pages 1-3)
- Plasma membrane (GO:0005886) – CTLA4, TCR signaling; endoplasmic reticulum/Golgi – immunoglobulin synthesis and glycosylation (supported by plasma glycome signatures) (pongracz2024autoimmunehepatitisdisplays pages 1-2)
- Extracellular space (GO:0005615) – circulating IgG, polyreactive IgG, cytokines (engel2024detectionofpolyreactive pages 1-2)

5) Disease progression: sequence of events
- Initiation: Genetic susceptibility (HLA class II and class I loci; non-HLA CTLA4/PTPN22) permits presentation of liver/self antigens. Environmental triggers (infections, dysbiosis) alter antigenic load and innate signaling (e.g., LPS) along the gut–liver axis, lowering tolerance thresholds. (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5, ahuja2023hlaandnonhla pages 10-11, sun2024thesignificanceof pages 1-2)
- Autoimmunity establishment: Autoreactive CD4+ T cells recognizing SepSecS (SLA) and other autoantigens expand, providing B-cell help; B cells undergo affinity maturation and produce class-switched antibodies. (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- Hepatocellular injury: Cytokine-driven inflammation and cytotoxic T cell activity produce interface hepatitis; persistent activation engages pro-fibrotic remodeling pathways (inflammatory chemokines/cytokines; NF-κB/JAK–STAT). (chi2025decodingthedistinct pages 16-16, liu2023immunemediatedhepatitisinduced pages 1-2)
- Biomarker manifestations: Hypergammaglobulinemia with elevated IgG; disease-specific biomarker candidates include plasma N-glycome changes (high tetra-antennary sialylation) and polyreactive IgG signatures. (pongracz2024autoimmunehepatitisdisplays pages 1-2, engel2024detectionofpolyreactive pages 1-2)

6) Phenotypic manifestations and links to mechanisms
- Elevated transaminases (ALT/AST) and IgG: reflect ongoing T and B cell–mediated hepatic inflammation and plasmacytosis. (taylor2019thecontributionof pages 1-3)
- Autoantibody positivity: ANA/SMA for AIH-1; anti-LKM1 and anti-LC1 for AIH-2; anti-SLA/LP (SepSecS) across types, correlating with more severe phenotype; mechanistically linked to affinity-matured anti-SepSecS response. (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- Interface hepatitis with plasma cell–rich portal infiltrates: pathologic correlate of B cell and T cell activation. (taylor2019thecontributionof pages 1-3)
- Overlap features with PBC/PSC (variant syndromes): shared autoimmunity to biliary structures and HLA backgrounds; clinically recognized overlaps require biopsy/serology correlation. (kocheise2024pd1pdl1immunecheckpoint pages 1-2, taylor2019thecontributionof pages 1-3)

Recent developments (priority 2023–2024) with data, URLs, dates
- HLA fine mapping in AIH type 1 (Han Chinese): Identification of HLA-B*35:01 (OR 7.32), HLA-B*08:01, peptide-binding residue Phe67, and transethnic confirmation of DRB1 risk architecture; association with clinical phenotypes (e.g., higher AST/ALT, lower IgG in B*35:01 carriers). JHEP Reports (online 2024-01-05), https://doi.org/10.1016/j.jhepr.2023.100926 (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- SepSecS (SLA)–specific immunity at clonal resolution in AIH: IgG1, affinity-matured antibodies to multiple epitopes; SepSecS-specific CD4+ T cells producing IFN-γ/IL-4/IL-10; clonal expansion in liver; B cells present SepSecS to T cells. J Clin Invest (2025-01-16 online early), https://doi.org/10.1172/JCI183776 (kramer2025clonalanalysisof pages 1-2)
- AIH plasma glycome biomarker: “Autoimmune hepatitis displays distinctively high multi-antennary sialylation on plasma N-glycans compared to other liver diseases,” with tetraantennary sialylation per galactose (A4GS) differentiating AIH from other liver diseases. Journal of Translational Medicine (2024-05), https://doi.org/10.1186/s12967-024-05173-z (pongracz2024autoimmunehepatitisdisplays pages 1-2)
- Polyreactive IgG (pIgG) improves AIH diagnosis in children (multi-center European cohort, n=285): AUC 0.900 vs non-AIH liver diseases; higher specificity than ANA/ASMA; sensitivity far exceeding anti-SLA/LC1/LKM in pediatric cohorts; independent of treatment response. Hepatology International (2024-07-08), https://doi.org/10.1007/s12072-024-10695-1 (engel2024detectionofpolyreactive pages 1-2)
- Microbiome narrative review in AIH: Summarizes decreased SCFAs/secondary bile acids and increased LPS and amino acid metabolites, linking to immune activation and barrier dysfunction along the gut–liver axis. Frontiers in Cellular and Infection Microbiology (2024-02-09), https://doi.org/10.3389/fcimb.2024.1337223 (sun2024thesignificanceof pages 1-2)
- ICI-induced immune-mediated hepatitis overview: “Overactivation of T cells” as central mechanism; incidence 1–15%, diagnostic/management considerations; provides mechanistic parallel to T cell–mediated hepatic autoimmunity. Frontiers in Pharmacology (2023-01-09), https://doi.org/10.3389/fphar.2022.1077468 (liu2023immunemediatedhepatitisinduced pages 1-2)
- PD-1/PD-L1 inhibitor safety in AILD: Multicenter European series (n=22; 4 AIH) reported no grade ≥3 irAEs and no significant liver test changes over 1 year, suggesting PD-1/PD-L1 agents “appear to be safe” in selected AILD patients with cancer. Frontiers in Immunology (2024-01-10), https://doi.org/10.3389/fimmu.2023.1326078 (kocheise2024pd1pdl1immunecheckpoint pages 1-2)

Current applications and real-world implementations
- Diagnostics
  - Serology: Standard ANA/SMA (AIH-1), LKM1/LC1 (AIH-2), SLA/LP (SepSecS) where available; pIgG quantification may increase diagnostic accuracy in pediatrics and possibly adults. (engel2024detectionofpolyreactive pages 1-2, kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
  - Biomarkers under evaluation: Plasma glycome (A4GS), as a noninvasive discriminator versus other liver diseases; could reduce need for biopsy if validated longitudinally. (pongracz2024autoimmunehepatitisdisplays pages 1-2)
- Risk stratification and genetics: HLA typing is informative in research and some clinical contexts (e.g., DRB1*03/*04 risk backgrounds; B*35:01 in East Asian cohorts); associations with phenotype at presentation (enzymes, IgG) reported. (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- Therapeutics
  - Standard: Corticosteroids ± azathioprine remain first-line (contextualized by B/T cell pathobiology). (taylor2019thecontributionof pages 1-3)
  - Refractory options: B cell–targeted therapy (e.g., anti-CD20) has shown efficacy in difficult AIH, aligning with B cell role in pathogenesis. (taylor2019thecontributionof pages 1-3)
  - Safety of PD-1/PD-L1 cancer therapy in AILD: cautious use appears feasible in selected cases with close monitoring. (kocheise2024pd1pdl1immunecheckpoint pages 1-2)

Expert opinions and analyses
- B cell centrality and therapeutic targeting: “Autoreactive B cells can promote autoimmunity through antigen presentation to autoreactive T cells, production of autoantibodies… and inhibition of regulatory T cells,” with clinical evidence for B cell–depleting therapy efficacy in refractory AIH. (Semin Liver Dis, 2019, https://doi.org/10.1055/s-0039-1688751) (taylor2019thecontributionof pages 1-3)
- T cell–centric injury model from ICI hepatitis: mechanistic insight that loss of checkpoint restraint leads to T cell overactivation and hepatitis provides a human perturbation model analogous to AIH immune injury. (Frontiers in Pharmacology, 2023, https://doi.org/10.3389/fphar.2022.1077468) (liu2023immunemediatedhepatitisinduced pages 1-2)

Relevant statistics and data
- HLA associations (Han Chinese AIH type 1): HLA-B*35:01 OR 7.32; HLA-B*08:01 OR 4.26; lead SNP rs2243621 OR 3.76; peptide-binding residue association HLA-B Phe67 (p=3.39×10−139). (JHEP Reports 2024, https://doi.org/10.1016/j.jhepr.2023.100926) (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- Pediatric pIgG diagnostic performance: AUC 0.900 vs non-AIH liver diseases; 31–73% higher specificity vs ANA/SMA and 6–20× higher sensitivity vs anti-SLA/LC1/LKM in children; positive in 43–75% with normal total IgG. (Hepatology International 2024, https://doi.org/10.1007/s12072-024-10695-1) (engel2024detectionofpolyreactive pages 1-2)
- Plasma glycome: Tetraantennary sialylation (A4GS) significantly differentiates AIH from other liver diseases; bisection tracks cirrhosis severity. (Journal of Translational Medicine 2024, https://doi.org/10.1186/s12967-024-05173-z) (pongracz2024autoimmunehepatitisdisplays pages 1-2)
- ICI hepatitis epidemiology: IMH incidence 1–15% across settings; pathogenesis attributed to T cell overactivation. (Frontiers in Pharmacology 2023, https://doi.org/10.3389/fphar.2022.1077468) (liu2023immunemediatedhepatitisinduced pages 1-2)
- PD-1/PD-L1 safety in AILD with cancer: 22 patients (12 PBC, 5 PSC, 4 AIH, 1 AIH-PSC) – no grade ≥3 irAEs; no significant liver test changes in first year. (Frontiers in Immunology 2024, https://doi.org/10.3389/fimmu.2023.1326078) (kocheise2024pd1pdl1immunecheckpoint pages 1-2)

Structured knowledge base annotations
- Genes/Proteins (HGNC): HLA-DRB1; HLA-B; HLA-DQB1; CTLA4; PTPN22; SEPSECS (SLA/LP antigen); CYP2D6 (LKM1 antigen); FTCD (LC1 antigen). Evidence: HLA fine mapping; case-control genetics; clonal SepSecS immunity; established autoantibody specificities. (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5, ahuja2023hlaandnonhla pages 10-11, kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- GO Biological Process: Antigen presentation via MHC I/II; T cell activation and differentiation (Th1/Th2/Th17); B cell activation and immunoglobulin production; response to LPS; bile acid metabolism; cytokine-mediated signaling (JAK–STAT; NF-κB). (li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5, kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3, sun2024thesignificanceof pages 1-2, liu2023immunemediatedhepatitisinduced pages 1-2)
- Cellular Components: MHC complexes; immunological synapse; plasma membrane; ER/Golgi (IgG glycosylation); extracellular region (serum IgG/pIgG). (pongracz2024autoimmunehepatitisdisplays pages 1-2, engel2024detectionofpolyreactive pages 1-2)
- Cell types (CL): CD4+ T cell; Treg; Th17 cell; CD8+ T cell; B cell; Plasma cell. (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- Anatomical locations (UBERON): Liver; portal tracts; bile ducts. (taylor2019thecontributionof pages 1-3)
- Phenotypes (HPO): Hypergammaglobulinemia; Elevated serum IgG; Autoantibody positivity; Interface hepatitis; Overlap cholangiopathy features. (taylor2019thecontributionof pages 1-3, engel2024detectionofpolyreactive pages 1-2, pongracz2024autoimmunehepatitisdisplays pages 1-2)
- Chemical entities (ChEBI): SCFAs (e.g., butyrate); secondary bile acids; LPS. (sun2024thesignificanceof pages 1-2)

Direct evidence quotes (illustrative)
- “A total of 588 HLA variants were significantly associated with AIH… the strongest allele was in the HLA-B gene (HLA-B*35:01, p = 8.17×10−304; OR = 7.32)… position 67… phenylalanine of the HLA-B molecule… at the peptide binding groove.” (JHEP Reports 2024) (li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- “The anti-SepSecS mAbs isolated were primarily IgG1, affinity-matured… SepSecS-specific CD4+ T cell clones… produced IFN-γ, IL-4, and IL-10, … clonally expanded in both blood and liver biopsy.” (J Clin Invest 2025) (kramer2025clonalanalysisof pages 1-2)
- “the mechanism of IMH induced by immune checkpoint inhibitors is mainly the overactivation of T cells.” (Frontiers in Pharmacology 2023) (liu2023immunemediatedhepatitisinduced pages 1-2)
- “decreased in secondary bile acids, short-chain fatty acids (SCFAs), and polyamines, and increased in lipopolysaccharide (LPS)… can disrupt immune homeostasis…” (Frontiers in Cellular and Infection Microbiology 2024) (sun2024thesignificanceof pages 1-2)
- “Glycan traits… tetraantennary sialylation per galactose (A4GS)… were found as discriminators between AIH and healthy controls… High A4GS differentiated AIH from other liver diseases.” (Journal of Translational Medicine 2024) (pongracz2024autoimmunehepatitisdisplays pages 1-2)
- “pIgG had an AUC of 0.900… 31–73% higher specificity than ANA and anti-SMA… 6–20 times higher than of anti-SLA/LP, anti-LC1 and anti-LKM.” (Hepatology International 2024) (engel2024detectionofpolyreactive pages 1-2)

Open questions and limits of current evidence
- The relative contributions of specific T helper lineages (e.g., Th17/Treg balance) and innate-like T cells (e.g., MAIT/NKT) in human AIH liver tissue require more single-cell/functional datasets; current mechanistic anchors are supported by clonal anti-SepSecS responses and B cell roles, rather than comprehensive spatial-omics in AIH. (kramer2025clonalanalysisof pages 1-2, taylor2019thecontributionof pages 1-3)
- Microbiome causality versus consequence remains unresolved; however, convergent metabolite patterns (SCFAs↓, secondary bile acids↓, LPS↑) provide plausible immunologic levers. (sun2024thesignificanceof pages 1-2)

References (with URLs and dates)
- Li Y et al. Fine mapping identifies independent HLA associations in autoimmune hepatitis type 1. JHEP Reports. Online 2024-01-05. https://doi.org/10.1016/j.jhepr.2023.100926 (li2024finemappingidentifies pages 1-2, li2024finemappingidentifies pages 2-4, li2024finemappingidentifies pages 4-5)
- Kramer M et al. Clonal analysis of SepSecS-specific B and T cells in autoimmune hepatitis. J Clin Invest. 2025-01-16. https://doi.org/10.1172/JCI183776 (kramer2025clonalanalysisof pages 1-2)
- Taylor SA, Assis DN, Mack CL. The Contribution of B Cells in Autoimmune Liver Diseases. Semin Liver Dis. 2019-11. https://doi.org/10.1055/s-0039-1688751 (taylor2019thecontributionof pages 1-3)
- Engel B et al. Detection of polyreactive immunoglobulin G facilitates diagnosis in children with autoimmune hepatitis. Hepatology International. 2024-07-08. https://doi.org/10.1007/s12072-024-10695-1 (engel2024detectionofpolyreactive pages 1-2)
- Pongracz T et al. Autoimmune hepatitis displays distinctively high multi-antennary sialylation on plasma N-glycans… J Transl Med. 2024-05. https://doi.org/10.1186/s12967-024-05173-z (pongracz2024autoimmunehepatitisdisplays pages 1-2)
- Sun C et al. The significance of gut microbiota in the etiology of autoimmune hepatitis: a narrative review. Front Cell Infect Microbiol. 2024-02-09. https://doi.org/10.3389/fcimb.2024.1337223 (sun2024thesignificanceof pages 1-2)
- Liu Z et al. Immune-mediated hepatitis induced by immune checkpoint inhibitors: Current updates and future perspectives. Front Pharmacol. 2023-01-09. https://doi.org/10.3389/fphar.2022.1077468 (liu2023immunemediatedhepatitisinduced pages 1-2)
- Kocheise L et al. PD-1/PD-L1 immune checkpoint therapy demonstrates favorable safety… AILD. Front Immunol. 2024-01-10. https://doi.org/10.3389/fimmu.2023.1326078 (kocheise2024pd1pdl1immunecheckpoint pages 1-2)
- Ahuja N et al. HLA and Non-HLA gene polymorphisms in autoimmune hepatitis patients of North Indian adults. Front Immunol. 2023-01. https://doi.org/10.3389/fimmu.2022.984083 (ahuja2023hlaandnonhla pages 10-11)
- Chi G et al. Integrated scRNA-seq/bulk RNA-seq landscape in AIH (supportive evidence for cytotoxic and chemokine axes). PLOS One. 2025-12. https://doi.org/10.1371/journal.pone.0335605 (chi2025decodingthedistinct pages 16-16)


References

1. (kramer2025clonalanalysisof pages 1-2): Michael Kramer, F. Mele, Sandra Jovic, Blanca Fernandez, D. Jarrossay, Jun Siong Low, Christiane Sokollik, Magdalena Filipowicz Sinnreich, Sylvie Ferrari-Lacraz, G. Mieli-Vergani, D. Vergani, Antonio Lanzavecchia, Antonino Cassotta, B. Terziroli Beretta‐Piccoli, and Federica Sallusto. Clonal analysis of sepsecs-specific b and t cells in autoimmune hepatitis. The Journal of Clinical Investigation, Jan 2025. URL: https://doi.org/10.1172/jci183776, doi:10.1172/jci183776. This article has 11 citations.

2. (taylor2019thecontributionof pages 1-3): Sarah A. Taylor, David N. Assis, and Cara L. Mack. The contribution of b cells in autoimmune liver diseases. Seminars in Liver Disease, 39:422-431, Jun 2019. URL: https://doi.org/10.1055/s-0039-1688751, doi:10.1055/s-0039-1688751. This article has 78 citations and is from a peer-reviewed journal.

3. (sun2024thesignificanceof pages 1-2): Chen Sun, Dongzi Zhu, Qi Zhu, Zeping He, Yichao Lou, and Desheng Chen. The significance of gut microbiota in the etiology of autoimmune hepatitis: a narrative review. Frontiers in Cellular and Infection Microbiology, Feb 2024. URL: https://doi.org/10.3389/fcimb.2024.1337223, doi:10.3389/fcimb.2024.1337223. This article has 17 citations and is from a poor quality or predatory journal.

4. (liu2023immunemediatedhepatitisinduced pages 1-2): Zherui Liu, Yun Zhu, Huan Xie, and Zhengsheng Zou. Immune-mediated hepatitis induced by immune checkpoint inhibitors: current updates and future perspectives. Frontiers in Pharmacology, Jan 2023. URL: https://doi.org/10.3389/fphar.2022.1077468, doi:10.3389/fphar.2022.1077468. This article has 59 citations and is from a poor quality or predatory journal.

5. (kocheise2024pd1pdl1immunecheckpoint pages 1-2): Lorenz Kocheise, Ignazio Piseddu, Joscha Vonderlin, Eric T. Tjwa, Gustav Buescher, Lucy Meunier, Pia Goeggelmann, Francesca Fianchi, Jérôme Dumortier, Mar Riveiro Barciela, Tom J. G. Gevers, Benedetta Terziroli Beretta-Piccoli, Maria-Carlota Londoño, Sona Frankova, Thomas Roesner, Vincent Joerg, Constantin Schmidt, Fabian Glaser, Jan P. Sutter, Thorben W. Fründt, Ansgar W. Lohse, Samuel Huber, Johann von Felden, Marcial Sebode, and Kornelius Schulze. Pd-1/pd-l1 immune checkpoint therapy demonstrates favorable safety profile in patients with autoimmune and cholestatic liver disease. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1326078, doi:10.3389/fimmu.2023.1326078. This article has 16 citations and is from a peer-reviewed journal.

6. (li2024finemappingidentifies pages 1-2): You Li, Lu Zhou, Zuxiong Huang, Yue Yang, Jiming Zhang, Ling Yang, Yun Xu, Junping Shi, Shanhong Tang, Xiaoling Yuan, Jie Xu, Yiling Li, Xu Han, Jia Li, Yanmin Liu, Ying Sun, Xiaozhi Jin, Xiao Xiao, Bangmao Wang, Qiuxiang Lin, Yang Zhou, Xuejiao Song, Yong Cui, Lilin Hu, Yuhu Song, Jie Bao, Ling Gong, M. Eric Gershwin, Xianbo Zuo, Huiping Yan, Zhengsheng Zou, Ruqi Tang, and Xiong Ma. Fine mapping identifies independent hla associations in autoimmune hepatitis type 1. JHEP Reports, 6:100926, Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100926, doi:10.1016/j.jhepr.2023.100926. This article has 6 citations and is from a peer-reviewed journal.

7. (li2024finemappingidentifies pages 2-4): You Li, Lu Zhou, Zuxiong Huang, Yue Yang, Jiming Zhang, Ling Yang, Yun Xu, Junping Shi, Shanhong Tang, Xiaoling Yuan, Jie Xu, Yiling Li, Xu Han, Jia Li, Yanmin Liu, Ying Sun, Xiaozhi Jin, Xiao Xiao, Bangmao Wang, Qiuxiang Lin, Yang Zhou, Xuejiao Song, Yong Cui, Lilin Hu, Yuhu Song, Jie Bao, Ling Gong, M. Eric Gershwin, Xianbo Zuo, Huiping Yan, Zhengsheng Zou, Ruqi Tang, and Xiong Ma. Fine mapping identifies independent hla associations in autoimmune hepatitis type 1. JHEP Reports, 6:100926, Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100926, doi:10.1016/j.jhepr.2023.100926. This article has 6 citations and is from a peer-reviewed journal.

8. (li2024finemappingidentifies pages 4-5): You Li, Lu Zhou, Zuxiong Huang, Yue Yang, Jiming Zhang, Ling Yang, Yun Xu, Junping Shi, Shanhong Tang, Xiaoling Yuan, Jie Xu, Yiling Li, Xu Han, Jia Li, Yanmin Liu, Ying Sun, Xiaozhi Jin, Xiao Xiao, Bangmao Wang, Qiuxiang Lin, Yang Zhou, Xuejiao Song, Yong Cui, Lilin Hu, Yuhu Song, Jie Bao, Ling Gong, M. Eric Gershwin, Xianbo Zuo, Huiping Yan, Zhengsheng Zou, Ruqi Tang, and Xiong Ma. Fine mapping identifies independent hla associations in autoimmune hepatitis type 1. JHEP Reports, 6:100926, Jan 2024. URL: https://doi.org/10.1016/j.jhepr.2023.100926, doi:10.1016/j.jhepr.2023.100926. This article has 6 citations and is from a peer-reviewed journal.

9. (ahuja2023hlaandnonhla pages 10-11): Nishtha Ahuja, Jagdeep Singh, Ranjana Walker Minz, Shashi Anand, Ashim Das, and Sunil Taneja. Hla and non-hla gene polymorphisms in autoimmune hepatitis patients of north indian adults. Frontiers in Immunology, Jan 2023. URL: https://doi.org/10.3389/fimmu.2022.984083, doi:10.3389/fimmu.2022.984083. This article has 8 citations and is from a peer-reviewed journal.

10. (chi2025decodingthedistinct pages 16-16): Gang Chi, Yijia Che, Jinhong Pei, Xueqing Li, and Junmei Wang. Decoding the distinct immune landscape and possible regulatory mechanisms of autoimmune hepatitis through integrated single-cell and bulk rna sequencing. PLOS One, 20:e0335605, Dec 2025. URL: https://doi.org/10.1371/journal.pone.0335605, doi:10.1371/journal.pone.0335605. This article has 0 citations and is from a peer-reviewed journal.

11. (pongracz2024autoimmunehepatitisdisplays pages 1-2): Tamas Pongracz, Maaike Biewenga, Anna Eva Charlotte Stoelinga, Marco René Bladergroen, Simone Nicolardi, Leendert Adrianus Trouw, Manfred Wuhrer, Noortje de Haan, and Bart van Hoek. Autoimmune hepatitis displays distinctively high multi-antennary sialylation on plasma n-glycans compared to other liver diseases. Journal of Translational Medicine, May 2024. URL: https://doi.org/10.1186/s12967-024-05173-z, doi:10.1186/s12967-024-05173-z. This article has 8 citations and is from a peer-reviewed journal.

12. (engel2024detectionofpolyreactive pages 1-2): Bastian Engel, Jana Diestelhorst, Katharina Luise Hupa-Breier, Theresa Kirchner, Nicole Henjes, Stephanie Loges, Muhammed Yuksel, Wojciech Janczyk, Claudine Lalanne, Kalliopi Zachou, Ye H. Oo, Jérôme Gournay, Simon Pape, Joost P. H. Drenth, Amédée Renand, George N. Dalekos, Luigi Muratori, Piotr Socha, Yun Ma, Cigdem Arikan, Ulrich Baumann, Michael P. Manns, Heiner Wedemeyer, Norman Junge, Elmar Jaeckel, and Richard Taubert. Detection of polyreactive immunoglobulin g facilitates diagnosis in children with autoimmune hepatitis. Hepatology International, 18:1214-1226, Jul 2024. URL: https://doi.org/10.1007/s12072-024-10695-1, doi:10.1007/s12072-024-10695-1. This article has 9 citations and is from a peer-reviewed journal.