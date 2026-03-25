---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T13:49:28.936983'
end_time: '2026-01-31T13:56:37.273277'
duration_seconds: 428.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lymphoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Lymphoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lymphoma**.
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
- **Disease Name:** Lymphoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Lymphoma**.
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
- Disease Name: Lymphoma
- MONDO ID: MONDO:0005047
- Category: Cancer

Pathophysiology overview and subtype framework
Lymphomas are clonal malignancies of lymphoid cells that arise through convergent genetic, epigenetic, and microenvironmental mechanisms. Errors during normal lymphocyte diversification (V(D)J recombination, somatic hypermutation, class-switch recombination) generate initiating lesions, while pathway-activating mutations (e.g., BCR/TLR→NF-κB, JAK/STAT, PI3K/AKT/mTOR), chromatin modifier mutations, and tumor–immune crosstalk drive progression and immune evasion (karolova2025molecularcytogeneticanalysisof pages 24-28). In diffuse large B‑cell lymphoma (DLBCL), “cell-of-origin” and newer genetic taxonomies resolve biological diversity with therapeutic implications (herrero2024characterizationoftumor pages 12-16, masnikosa2024tumorbiologyhides pages 12-13). Peripheral T‑cell lymphomas (PTCL), particularly TFH-derived angioimmunoblastic T‑cell lymphoma (AITL), exemplify multistep evolution from clonal hematopoiesis to TCR/JAK-STAT pathway activation with a characteristic microenvironmental imprint (ondrejka2023follicularhelpertcell pages 8-10). Recent umbrella reviews emphasize heterogeneity driven by clonal evolution, epigenetic remodeling, and tumor microenvironment (TME) dynamics as a cross-cutting theme undermining conventional therapy and enabling precision strategies (wang2025molecularpathologyof pages 1-2).

Core pathophysiology by dysregulated pathways
- BCR/TLR/NF-κB and PI3K/AKT/mTOR (B-cell lymphomas): Mutations in the BCR signalosome (CD79B, CARD11), MYD88 (L265P), and related adaptors activate canonical NF-κB and PI3K/AKT pathways, especially in ABC-type DLBCL and mantle cell lymphoma (MCL) (karolova2025molecularcytogeneticanalysisof pages 24-28). “GCB frequently shows t(14;18) BCL2 translocations… and EZH2 mutations, while ABC often harbors PRDM1 inactivation” (quote) (karolova2025molecularcytogeneticanalysisof pages 28-31). These signaling axes are targetable (e.g., BTK inhibitors) (karolova2025molecularcytogeneticanalysisof pages 24-28).
- JAK/STAT signaling (T- and some B-cell lymphomas): Aberrations in JAK1/3 and STAT3/5 contribute to proliferation, survival, and immune modulation across PTCL and subsets of B‑cell lymphomas (karolova2025molecularcytogeneticanalysisof pages 28-31, ribeiro2023epigenetictargetsin pages 2-3). Reviews emphasize “constitutive PI3K-AKT-mTOR activation, and JAK-STAT pathway mutations (e.g., STAT3/5B, JAK1/3/5)” in T‑cell lymphomas (quote) (ribeiro2023epigenetictargetsin pages 2-3).
- NOTCH pathway: NOTCH1/2 lesions are recurrent in B‑cell lymphomas (e.g., BN2 DLBCL subtype) and implicated in MCL biology, with downstream HES1/HEY targets (masnikosa2024tumorbiologyhides pages 12-13, wang2025molecularpathologyof pages 1-2).
- Epigenetic/chromatin regulation: Frequent mutations in histone modifiers CREBBP, EP300, KMT2D, and EZH2 reprogram enhancers/super‑enhancers governing GC fate and immune synapse genes (herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28). Cross-disease reviews highlight epigenetic dysregulation as a major therapeutic axis (ribeiro2023epigenetictargetsin pages 2-3).

Key molecular players (genes/proteins, cells, anatomy, chemicals)
- Recurrent drivers by entity
  • DLBCL: MYD88 L265P, CD79B, EZH2 Y641, BCL2 (t(14;18)), BCL6, MYC, CREBBP, KMT2D, TP53; genetic classes MCD (MYD88/CD79B), BN2 (BCL6/NOTCH2), N1 (NOTCH1), EZB (EZH2/BCL2) (masnikosa2024tumorbiologyhides pages 12-13, herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28).
  • Follicular lymphoma (FL): t(14;18)(IGH–BCL2) as hallmark; early and prevalent mutations in KMT2D, CREBBP, EZH2; these epigenetic lesions shape GC programs and immune interactions (wang2025molecularpathologyof pages 1-2, ribeiro2023epigenetictargetsin pages 2-3).
  • Mantle cell lymphoma (MCL): t(11;14)(IGH–CCND1)→cyclin D1 overexpression; SOX11, ATM, TP53, RB1 alterations; NOTCH signaling implicated (ribeiro2023epigenetictargetsin pages 2-3, wang2025molecularpathologyof pages 1-2).
  • Classical Hodgkin lymphoma (cHL): pervasive JAK/STAT and NF-κB activation with frequent PD‑L1/PD‑L2 locus alterations and epigenetic regulator mutations (CREBBP/EP300/KMT2D reported) in the rare malignant HRS cells within an immune-rich TME (ribeiro2023epigenetictargetsin pages 2-3, wang2025molecularpathologyof pages 1-2).
  • TFH-derived AITL: early TET2/DNMT3A mutations in clonal hematopoiesis; RHOA G17V and IDH2 R172K/S as TFH tumor drivers; TFH markers (PD1, ICOS, BCL6) and characteristic FDC expansion (ondrejka2023follicularhelpertcell pages 8-10). “Recurrent somatic mutations in TFHL include early‑branch hematopoietic mutations (TET2, DNMT3A)… while RHOA G17V and IDH2 R172K are largely confined to the neoplastic T cells” (quote) (ondrejka2023follicularhelpertcell pages 8-10).
  • CTCL: aberrant TCR signaling, JAK/STAT activation (STAT3/5, JAK1/3/5), epigenetic dysregulation and non‑coding RNA control (ribeiro2023epigenetictargetsin pages 2-3).
  • Primary CNS lymphoma (PCNSL): frequent MYD88 L265P and CD79B, BCR/TLR→NF‑κB activation, with immune-privileged site constraints (wang2025molecularpathologyof pages 1-2).
- Cell types and anatomical sites
  • B‑cell GC compartments (dark/light zones) as origin for GCB lymphomas; TFH cells and FDC networks in AITL; immune/stromal-rich milieu encasing HRS cells in cHL; immune‑privileged CNS for PCNSL (herrero2024characterizationoftumor pages 12-16, ondrejka2023follicularhelpertcell pages 8-10, wang2025molecularpathologyof pages 1-2).
- Chemical entities and therapeutics (selected): BTK inhibitors (e.g., ibrutinib), EZH2 inhibitor tazemetostat, HDAC inhibitors, immunomodulatory drugs, anti‑PD‑1, CAR‑T and bispecific antibodies (karolova2025molecularcytogeneticanalysisof pages 24-28, ribeiro2023epigenetictargetsin pages 2-3, masnikosa2024tumorbiologyhides pages 12-13).

Microenvironment and immune evasion
- Antigen presentation defects (B2M/CIITA lesions), PD‑1/PD‑L1 axis upregulation, and T‑cell exhaustion are core to immune escape in aggressive B‑cell lymphomas and cHL (masnikosa2024tumorbiologyhides pages 12-13, herrero2024characterizationoftumor pages 12-16). GC biology intrinsically depends on APC–Tfh–B‑cell crosstalk, which becomes subverted during lymphomagenesis (herrero2024characterizationoftumor pages 12-16). In TFHL/AITL, the TME features arborizing HEVs, expanded FDC networks, and EBV+ B‑cell proliferations that can confound diagnosis (ondrejka2023follicularhelpertcell pages 8-10).
- Viral immunoediting: EBV miRNAs upregulate PD‑L1/2 and “inhibit antigen presentation (TAP2… IFI30, LGMN, CTSB)” and suppress inflammatory cytokines; exosomal EBV miRNAs act on macrophages (quotes) (zhang2024carcinogenicmechanismsof pages 6-7). These mechanisms are prominent in EBV+ cHL and some EBV+ DLBCL variants (zhang2024carcinogenicmechanismsof pages 6-7).

Viral associations and mechanisms
- EBV: latency programs and miRNAs drive immune evasion (PD‑L1/2 induction), hinder antigen processing/presentation, reduce NK recognition, and shape an immunosuppressive TME (zhang2024carcinogenicmechanismsof pages 6-7).
- HBV/HCV and HIV: Chronic antigenic stimulation and potential genomic perturbations contribute to B‑cell NHL risk; HBV is associated with ~2.5‑fold increased NHL risk, with biased IGHV usage reported in HBsAg+ DLBCL (zhang2024carcinogenicmechanismsof pages 6-7). “HBV confers ~2.5‑fold increased NHL risk… HBV integrates into host genomes… in NHL disrupts/exerts cis‑activation on specific genes” (quote) (zhang2024carcinogenicmechanismsof pages 6-7).

Emerging mechanisms (with recent perspectives)
- Epigenetic cooperation and immune synapse control: Loss of CREBBP/KMT2D alters enhancer programs governing immune synapse genes and T‑cell interactions, favoring immune evasion (mechanistic theme across FL/DLBCL) (herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28).
- Metabolism and cell death vulnerabilities: In DLBCL, reviews argue for exploration of lipid metabolism and ferroptosis as adjunct targets to BCR/NF‑κB and epigenetic pathways (masnikosa2024tumorbiologyhides pages 12-13).

Disease progression and transformation
- FL → DLBCL: FL is initiated by IGH–BCL2 with early CREBBP/KMT2D/EZH2 mutations; additional hits (e.g., TP53, MYC), antigen presentation loss, and TME remodeling accompany transformation to DLBCL (wang2025molecularpathologyof pages 1-2, ribeiro2023epigenetictargetsin pages 2-3). DLBCL can also arise de novo or from other indolent lymphomas with acquisition of MYC/BCL2/BCL6 rearrangements (“double/triple‑hit”) and widespread genetic instability (masnikosa2024tumorbiologyhides pages 12-13, herrero2024characterizationoftumor pages 12-16).
- AITL pathogenesis: Age‑related clonal hematopoiesis (TET2/DNMT3A) precedes TFH-restricted drivers (RHOA G17V, IDH2 R172), elaborating cytokine‑rich milieus and EBV+ B‑cell expansions that reflect disease biology rather than a separate lymphoma (ondrejka2023follicularhelpertcell pages 8-10).

Current applications and real‑world implementations
- Targeted therapy alignment
  • BCR/NF‑κB axis: BTK inhibitors show activity in ABC/MCD DLBCL biology and are established in MCL (karolova2025molecularcytogeneticanalysisof pages 24-28, masnikosa2024tumorbiologyhides pages 12-13).
  • Epigenetic therapy: EZH2 inhibition (tazemetostat) is effective in EZH2‑mutant FL and under exploration in DLBCL; HDAC and other epigenetic agents are applied in T‑cell lymphomas and CTCL (ribeiro2023epigenetictargetsin pages 2-3, masnikosa2024tumorbiologyhides pages 12-13).
  • Immune checkpoint therapy: Anti‑PD‑1 agents are standard in cHL, supported by high PD‑L1/2 and immune‑evasive TME (ribeiro2023epigenetictargetsin pages 2-3, wang2025molecularpathologyof pages 1-2).
  • Cellular and bispecific immunotherapy: CAR‑T and bispecific antibodies are integrated into DLBCL care paradigms and under evaluation across subtypes (masnikosa2024tumorbiologyhides pages 12-13, wang2025molecularpathologyof pages 1-2).
- Molecular diagnostics and monitoring
  • Genomic taxonomy (e.g., LymphGen classes) and COO profiling refine DLBCL prognostication and therapeutic choices (masnikosa2024tumorbiologyhides pages 12-13, herrero2024characterizationoftumor pages 12-16).
  • Next‑generation sequencing panels and ctDNA: Reviews highlight NGS as essential for classification and risk stratification, with liquid biopsy increasingly used for non‑invasive genotyping and disease monitoring in lymphoma (wang2025molecularpathologyof pages 1-2).

Direct quotes (selected) with source URLs and dates
- “DLBCL… arises from abnormal B‑cell proliferation either de novo or via transformation from indolent NHL… Key recurrent alterations… include MYC translocations… aberrant EZH2 activity… inactivation of PRDM1 in ABC… mutations/alterations in NF‑κB, CREBBP and EP300.” International Journal (2024). URL: [Unavailable in record metadata] (herrero2024characterizationoftumor pages 12-16).
- “Errors in V(D)J recombination, class-switch recombination and aberrant somatic hypermutation (driven by AID) create chromosomal translocations… t(14;18) placing BCL2 under IGH control… t(11;14) driving cyclin D1 overexpression in MCL… Recurrent mutations include MYD88… TP53… EZH2.” Thesis (2025). URL: [Unavailable] (karolova2025molecularcytogeneticanalysisof pages 24-28).
- “TFHL frequently shows… mutations in TET2, DNMT3A… while RHOA G17V and IDH2 R172K are largely confined to the neoplastic T cells… frequent EBV+ B‑cell proliferations.” Virchows Archiv (Jul 2023). https://doi.org/10.1007/s00428-023-03607-5 (ondrejka2023follicularhelpertcell pages 8-10).
- “Epigenetic dysregulations… are prevalent in both B‑ and T‑cell lymphomas… over the past decade, a large number of epigenetic‑modifying agents have been developed…” Therapeutic Advances in Hematology (May 2023). https://doi.org/10.1177/20406207231173485 (ribeiro2023epigenetictargetsin pages 2-3).
- “EBV‑encoded miRNAs… upregulate PD‑L1/PD‑L2, inhibit antigen presentation (TAP2… IFI30, LGMN, CTSB)… suppress inflammatory cytokines… act via exosomes on macrophages.” Frontiers in Immunology (Feb 2024). https://doi.org/10.3389/fimmu.2024.1361009 (zhang2024carcinogenicmechanismsof pages 6-7).
- “Genetic subtypes (MCD, BN2, N1, EZB)… immune modulators (B2M, CIITA)… MCD/ABC tumors respond to ibrutinib.” IJMS Narrative Review (Oct 2024). https://doi.org/10.3390/ijms252111384 (masnikosa2024tumorbiologyhides pages 12-13).
- “Heterogeneity driven by somatic clonal evolution, epigenetic modifications, and TME remodeling… priorities include molecular stratification and precision diagnostics/therapies.” Frontiers in Immunology (Jul 2025). https://doi.org/10.3389/fimmu.2025.1620895 (wang2025molecularpathologyof pages 1-2).

Biological processes (GO) disrupted
- GO:0050853 B cell receptor signaling pathway; GO:0043122 regulation of I‑kappaB kinase/NF‑κB signaling; GO:0014065 phosphatidylinositol 3‑kinase signaling; GO:0007259 JAK‑STAT cascade; GO:0006338 chromatin remodeling; GO:0016569 covalent chromatin modification; GO:0002376 immune system process; GO:0019882 antigen processing and presentation (supported by above evidence) (herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28, ribeiro2023epigenetictargetsin pages 2-3, zhang2024carcinogenicmechanismsof pages 6-7, masnikosa2024tumorbiologyhides pages 12-13).

Cellular components
- BCR signalosome at plasma membrane; cytoplasmic NF‑κB pathway complexes; nuclear chromatin (enhancers/super‑enhancers) targeted by CREBBP/KMT2D/EZH2; immune synapse interfaces; extracellular milieu of TME (herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28, ribeiro2023epigenetictargetsin pages 2-3).

Disease progression sequence (exemplar)
- FL: Initiation by IGH–BCL2 → early epigenetic mutations (CREBBP, KMT2D, EZH2) that reshape GC enhancer landscape and immune interactions → subclonal diversification with additional hits (TP53/MYC), antigen presentation loss and TME reprogramming → transformation to DLBCL (wang2025molecularpathologyof pages 1-2, ribeiro2023epigenetictargetsin pages 2-3, masnikosa2024tumorbiologyhides pages 12-13).
- AITL: Age‑related CH (TET2/DNMT3A) in HSCs → TFH‑restricted drivers (RHOA G17V, IDH2 R172) → cytokine‑rich, EBV‑laden TME and clinical immune dysregulation (ondrejka2023follicularhelpertcell pages 8-10).

Phenotypic manifestations (HP terms; selected mechanistic links)
- HP:0002715 Lymphadenopathy; HP:0002014 B symptoms (fever/night sweats/weight loss) reflecting cytokine‑rich TME (herrero2024characterizationoftumor pages 12-16, ondrejka2023follicularhelpertcell pages 8-10).
- HP:0001679 Splenomegaly (nodal/extranodal spread in B‑cell lymphomas) (wang2025molecularpathologyof pages 1-2).
- HP:0012735 Immunodeficiency (immune evasion and antigen presentation loss; EBV‑associated cases) (zhang2024carcinogenicmechanismsof pages 6-7, masnikosa2024tumorbiologyhides pages 12-13).

Cell type involvement (CL terms; selected)
- CL:0000236 B cell (GC B cells, memory B cells: DLBCL/FL origins) (herrero2024characterizationoftumor pages 12-16).
- CL:0000895 T follicular helper cell (AITL) (ondrejka2023follicularhelpertcell pages 8-10).
- CL:0000786 T cell (PTCL/CTCL) (ribeiro2023epigenetictargetsin pages 2-3).
- CL:0000235 Dendritic cell, follicular subtype (AITL TME) (ondrejka2023follicularhelpertcell pages 8-10).

Anatomical locations (UBERON terms; selected)
- UBERON:0000029 Lymph node (most subtypes) (herrero2024characterizationoftumor pages 12-16, masnikosa2024tumorbiologyhides pages 12-13).
- UBERON:0002037 Spleen; UBERON:0002048 Bone marrow (dissemination sites) (wang2025molecularpathologyof pages 1-2).
- UBERON:0000955 Brain (PCNSL) (wang2025molecularpathologyof pages 1-2).

Chemical entities (CHEBI; selected approved/under study)
- CHEBI:63637 Ibrutinib (BTK inhibitor) (karolova2025molecularcytogeneticanalysisof pages 24-28, masnikosa2024tumorbiologyhides pages 12-13).
- CHEBI:94436 Tazemetostat (EZH2 inhibitor) (ribeiro2023epigenetictargetsin pages 2-3, masnikosa2024tumorbiologyhides pages 12-13).
- CHEBI:90686 Vorinostat (HDAC inhibitor; CTCL) (ribeiro2023epigenetictargetsin pages 2-3).

Evidence items (with PMIDs/DOIs/URLs and dates)
- Virchows Archiv. TFH lymphomas and clonal hematopoiesis in AITL (Jul 2023). https://doi.org/10.1007/s00428-023-03607-5 (ondrejka2023follicularhelpertcell pages 8-10).
- Therapeutic Advances in Hematology. Epigenetic targets in B- and T-cell lymphomas (May 2023). https://doi.org/10.1177/20406207231173485 (ribeiro2023epigenetictargetsin pages 2-3).
- Frontiers in Immunology. Carcinogenic mechanisms of virus-associated lymphoma (Feb 2024). https://doi.org/10.3389/fimmu.2024.1361009 (zhang2024carcinogenicmechanismsof pages 6-7).
- International Journal of Molecular Sciences. DLBCL tumor biology and genetic subtypes; therapies and novel targets (Oct 2024). https://doi.org/10.3390/ijms252111384 (masnikosa2024tumorbiologyhides pages 12-13).
- Frontiers in Immunology. Molecular pathology of lymphoma; precision strategies (Jul 2025). https://doi.org/10.3389/fimmu.2025.1620895 (wang2025molecularpathologyof pages 1-2).
- Molecular-cytogenetic analysis of aggressive lymphomas (Thesis; 2025). [URL unavailable in record] (karolova2025molecularcytogeneticanalysisof pages 24-28).
- Immune microenvironment and COO biology in DLBCL (2024). [URL unavailable in record] (herrero2024characterizationoftumor pages 12-16).

Embedded artifact
| Subtype | Core dysregulated pathways (GO/processes) | Recurrent driver genes (HGNC symbols/mutations) | Immune evasion & microenvironment | Viral associations | Emerging mechanisms | Real-world applications |
|---|---|---|---|---|---|---|
| DLBCL | B-cell receptor signaling; NF-kappaB pathway activation; PI3K-AKT-mTOR signaling; chromatin modification/epigenetic regulation | MYD88 (L265P); CD79B; BCL2 (t(14;18)); BCL6; MYC; EZH2 (Y641); CREBBP; KMT2D; TP53 | PD-1/PD-L1 upregulation; loss of antigen presentation (B2M, CIITA); immune-rich vs immune-poor TME; T-cell exhaustion | EBV-associated subsets; HBV associations reported in cohorts | Inflammasome (NLRP3) links; ferroptosis vulnerabilities under investigation | BTK inhibitors (ibrutinib) in ABC/MCD; EZH2 inhibitor (tazemetostat) in EZH2-mutant FL/DLBCL contexts; CAR-T, bispecifics; ctDNA for monitoring |
| Follicular lymphoma (FL) | Anti-apoptotic BCL2 signaling (t(14;18)); epigenetic dysregulation (histone modifier GO terms); germinal-center programs | BCL2; KMT2D; CREBBP; EZH2 (Y641); BCL6; occasional TP53 at transformation | Strong microenvironment dependence (Tfh, FDCs); immune-cell composition influences prognosis; altered antigen presentation at progression | Less direct viral drivers; EBV rare | Epigenetic alteration-driven immune remodeling; clonal evolution during transformation | EZH2 inhibitors (tazemetostat) for EZH2-mutant FL; epigenetic-targeted agents; ctDNA for clonal evolution/HT detection |
| Mantle cell lymphoma (MCL) | Cell-cycle dysregulation (GO: cell cycle control); BCR signaling; transcriptional programs (NOTCH) | CCND1 (t(11;14)); SOX11; ATM; TP53; RB1 | Tumor stroma interactions; variable immune infiltration; immune evasion via conventional mechanisms | No dominant viral association | Epigenetic and transcriptional instability; metabolic adaptations in aggressive MCL | BTK inhibitors (ibrutinib, acalabrutinib); venetoclax (BCL2 inhibitor); molecular profiling informs therapy |
| Classical Hodgkin lymphoma (cHL) | JAK-STAT signaling; NF-kappaB activation; chromatin remodeling/epigenetic modifiers (PRC2, SWI/SNF) | Frequent PD-L1/PD-L2 locus alterations; CIITA disruption; mutations in epigenetic regulators (CREBBP, EP300, KMT2D often) | Extremely TME-dominated (few HRS cells amid immune/stromal cells); high PD-L1/PD-L2 expression; antigen-presentation defects; T-reg and exhausted T-cell niches | Strong EBV association in many cases; EBV-driven immune evasion mechanisms | TME-mediated immune suppression; inflammasome and metabolic TME features under study | Anti-PD-1 checkpoint inhibitors (nivolumab, pembrolizumab); brentuximab vedotin (CD30); liquid biopsy/ctDNA emerging for monitoring |
| TFH-derived AITL (peripheral TFH lymphoma) | T-cell receptor signaling; JAK-STAT pathway; epigenetic dysregulation (GO: DNA methylation, chromatin modification) | TET2; DNMT3A (clonal hematopoiesis); RHOA G17V; IDH2 (R172); often additional TFH markers (ICOS, BCL6) | Prominent immune dysregulation; expanded FDC networks; frequent EBV+ B-cell expansions in TME; autoimmunity-like cytokine milieu | Frequently associated with EBV-positive B-cell proliferations (reactive) | Clonal hematopoiesis (early DNMT3A/TET2) shaping pathogenesis; cytokine-driven TME remodeling | Hypomethylating agents and HDAC inhibitors explored; targeted JAK/STAT or IDH2 strategies in trials; molecular profiling guides therapy |
| Cutaneous T-cell lymphoma (CTCL; MF/SS) | TCR signaling aberration; JAK/STAT pathway activation; NF-kappaB; epigenetic and non-coding RNA regulation | STAT3/STAT5; JAK3 alterations reported; diverse mutational spectrum depending on subtype | Cytokine-dominant skin microenvironment; impaired antitumor immunity; altered trafficking of T cells; immune checkpoint molecules in TME | No consistent viral driver (rare associations) | Non-coding RNAs shaping gene expression; inflammasome and metabolic changes under study | HDAC inhibitors (vorinostat, romidepsin); JAK inhibitors under investigation; immunomodulatory and skin-directed therapies; biomarker-driven trials |
| Primary CNS lymphoma (PCNSL) | Constitutive NF-kappaB activation; BCR/TLR signaling; JAK-STAT and PI3K-AKT pathways; altered DNA methylation | MYD88 (L265P); CD79B; BCL6; frequent copy-number changes; TP53 in some cases | Immune-privileged site TME with local immunosuppression; antigen presentation and local immune evasion | EBV in immunocompromised PCNSL subsets (variable) | Microenvironmental metabolic constraints; unique CNS immune interactions; ferroptosis/metabolic vulnerabilities investigated | BTK inhibitors (ibrutinib) evaluated; immune checkpoint and IMiD approaches in trials; CSF/ctDNA liquid biopsy for noninvasive genotyping and MRD monitoring |


*Table: Compact comparison table summarizing core dysregulated pathways, recurrent drivers, microenvironment/immune-evasion features, viral links, emerging mechanisms, and real-world targeted/diagnostic applications across major lymphoma subtypes (compiled from recent mechanistic reviews and studies) (herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28, ondrejka2023follicularhelpertcell pages 8-10, ribeiro2023epigenetictargetsin pages 2-3, zhang2024carcinogenicmechanismsof pages 6-7, masnikosa2024tumorbiologyhides pages 12-13, wang2025molecularpathologyof pages 1-2).*

Expert synthesis
Across lymphoma subtypes, a unifying model emerges: initiating lesions from physiologic diversification processes, reinforced by pathway-activating mutations (BCR/TLR→NF‑κB, JAK/STAT, PI3K/AKT) and epigenetic remodeling (CREBBP/KMT2D/EZH2) that together drive aberrant cell fate, immune synapse dysfunction, and TME-mediated immune escape. DLBCL’s genetic classes and FL’s early epigenetic lesions provide actionable anchors; AITL’s clonal hematopoiesis paradigm underscores the pre-malignant substrate that shapes evolution; and viral programs (EBV) exemplify how exogenous factors hardwire immune evasion. Translationally, BTK/EZH2/HDAC inhibitors, checkpoint blockade, and cellular/bispecific immunotherapies map onto these mechanisms, while NGS/ctDNA supports precision diagnosis and monitoring (herrero2024characterizationoftumor pages 12-16, karolova2025molecularcytogeneticanalysisof pages 24-28, wang2025molecularpathologyof pages 1-2, ondrejka2023follicularhelpertcell pages 8-10, ribeiro2023epigenetictargetsin pages 2-3, zhang2024carcinogenicmechanismsof pages 6-7, masnikosa2024tumorbiologyhides pages 12-13).

References

1. (karolova2025molecularcytogeneticanalysisof pages 24-28): J Karolová. Molecular-cytogenetic analysis of aggressive lymphomas. Unknown journal, 2025.

2. (herrero2024characterizationoftumor pages 12-16): AD Herrero. Characterization of tumor immune microenvironment in human diffuse large b-cell lymphoma. Unknown journal, 2024.

3. (masnikosa2024tumorbiologyhides pages 12-13): R. Masnikosa, Z. Cvetković, and D. Pirić. Tumor biology hides novel therapeutic approaches to diffuse large b-cell lymphoma: a narrative review. International Journal of Molecular Sciences, Oct 2024. URL: https://doi.org/10.3390/ijms252111384, doi:10.3390/ijms252111384. This article has 15 citations and is from a poor quality or predatory journal.

4. (ondrejka2023follicularhelpertcell pages 8-10): Sarah L Ondrejka, Catalina Amador, Fina Climent, Siok-Bian Ng, Lorinda Soma, Alberto Zamo, Stefan Dirnhofer, Leticia Quintanilla-Martinez, Andrew Wotherspoon, Lorenzo Leoncini, and Laurence de Leval. Follicular helper t-cell lymphomas: disease spectrum, relationship with clonal hematopoiesis, and mimics. a report of the 2022 ea4hp/sh lymphoma workshop. Virchows Archiv, 483:349-365, Jul 2023. URL: https://doi.org/10.1007/s00428-023-03607-5, doi:10.1007/s00428-023-03607-5. This article has 18 citations and is from a peer-reviewed journal.

5. (wang2025molecularpathologyof pages 1-2): Zhongyu Wang, Shuai Feng, Xiangmei Yao, Renbin Zhao, Yujin Li, Maofeng Zheng, Zengzheng Li, and Yajie Wang. Molecular pathology of lymphoma and its treatment strategies: from mechanistic elucidation to precision medicine. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1620895, doi:10.3389/fimmu.2025.1620895. This article has 4 citations and is from a peer-reviewed journal.

6. (karolova2025molecularcytogeneticanalysisof pages 28-31): J Karolová. Molecular-cytogenetic analysis of aggressive lymphomas. Unknown journal, 2025.

7. (ribeiro2023epigenetictargetsin pages 2-3): Marcelo Lima Ribeiro, Salvador Sánchez Vinces, Laura Mondragon, and Gael Roué. Epigenetic targets in b- and t-cell lymphomas: latest developments. Therapeutic Advances in Hematology, May 2023. URL: https://doi.org/10.1177/20406207231173485, doi:10.1177/20406207231173485. This article has 5 citations and is from a peer-reviewed journal.

8. (zhang2024carcinogenicmechanismsof pages 6-7): Ying Zhang, Wei Guo, Zhumei Zhan, and Ou Bai. Carcinogenic mechanisms of virus-associated lymphoma. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1361009, doi:10.3389/fimmu.2024.1361009. This article has 21 citations and is from a peer-reviewed journal.