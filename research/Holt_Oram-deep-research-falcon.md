---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-07T13:48:32.160875'
end_time: '2026-01-07T13:56:24.446724'
duration_seconds: 472.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Holt-Oram syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Holt-Oram syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Holt-Oram syndrome**.
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
- **Disease Name:** Holt-Oram syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Holt-Oram syndrome**.
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
- Frame scope: TBX5-driven developmental mechanisms in heart and forelimb; dosage sensitivity; cofactor network (GATA4, NKX2-5, ZFPM2/FOG2); chromatin partners (BAF/SWI-SNF, CHD4/NuRD); enhancer and 3D genome effects; genotype–phenotype and clinical phenotypes. (completed)
- Gather recent primary literature and reviews (prioritize 2023–2024) and extract direct mechanistic evidence with PMIDs/DOIs/URLs. (completed)
- Map evidence to ontology terms (HGNC, GO, CL, UBERON, CHEBI) and assemble structured artifacts. (completed)
- Synthesize disease pathophysiology narrative and populate knowledge-base style annotations with citations. (completed)

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Holt-Oram syndrome (HOS)
- MONDO ID: —
- Category: Genetic

Pathophysiology description (narrative)
Holt–Oram syndrome is a dosage-sensitive developmental disorder caused predominantly by heterozygous variants in the T-box transcription factor TBX5, which coordinates gene regulatory networks in cardiogenesis and forelimb development. TBX5 acts at enhancers within accessible chromatin to drive atrial and chamber-specific programs, and its dosage reduction disrupts atrial identity, conduction system development, and septation; in the limb, TBX5 initiates forelimb formation from lateral plate mesoderm, and haploinsufficiency yields radial ray defects. Mechanistically, TBX5 cooperates with other core cardiac transcription factors, notably GATA4 and NKX2-5, and recruits or functions with chromatin remodeling complexes (SWI/SNF-BAF, NuRD via CHD4) to shape enhancer activity and 3D genome architecture. Recent studies demonstrate conserved TBX5/GATA4/FOG2 co-occupied atrial enhancers controlling conduction and Ca2+ handling genes and show that reducing TBX5 dose perturbs enhancer–promoter looping and topologically associating domains, providing a direct molecular basis for arrhythmia and septation phenotypes in HOS. (broman2024agenomiclink pages 42-46, grant2025dosedependentsensitivityof pages 20-23, sweat2024chd4interactswith pages 1-6, cervantessalazar2024geneticinsightsinto pages 8-10, lang2023casereportnovel pages 3-5)

Direct evidence and quotes
- TBX5 maintains atrial identity through an enhancer network: “TBX5 maintains atrial identity in postnatal cardiomyocytes by regulating an atrial-specific enhancer network,” including hundreds of TBX5 dosage-sensitive chromatin loops. Nature Cardiovascular Research, Oct 2023. URL: https://doi.org/10.1038/s44161-023-00334-7 (grant2025dosedependentsensitivityof pages 20-23)
- Atrial enhancer co-regulation and AF risk: “FOG2 bound a subset of GATA4 and TBX5 co-bound genomic locations… FOG2 repressed TBX5-dependent transcription from a subset of co-bound enhancers,” and “Atrial rhythm abnormalities in mice caused by Tbx5 haploinsufficiency were rescued by Zfpm2 haploinsufficiency.” Circulation, Apr 2024. URL: https://doi.org/10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46)
- TBX5–CHD4 chromatin collaboration in atrial cardiomyocytes: “TBX5 also physically interacts with chromodomain helicase DNA binding protein 4 (CHD4)… atrial-selective Chd4 knockout increases susceptibility to pacing-induced atrial fibrillation.” bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.04.626894 (sweat2024chd4interactswith pages 1-6)
- TBX5 dose regulates 3D genome: “Genome organization, including compartments, TADs, and chromatin loops, are sensitive to reduced TBX5 dosage… co-occupancy with CTCF partially protects TBX5-bound TAD boundaries and loop anchors.” bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.09.632202 (grant2025dosedependentsensitivityof pages 20-23)
- TBX5 dosage and limb initiation: “TBX5… critical for heart and forelimb development… TBX5 binds to [downstream] promoter regions to promote gene transcription,” and 3′-UTR variants may modulate TBX5 expression via miRNAs. Frontiers in Genetics, Mar 2023. URL: https://doi.org/10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5)
- Septation and chamber identity roles for TBX5 with GATA4/NKX2-5 in CHDs: narrative review summarizing TBX5 dosage sensitivity and roles in septation and conduction. Biology, Nov 2024. URL: https://doi.org/10.3390/biology13110911 (cervantessalazar2024geneticinsightsinto pages 8-10)

Recent developments and latest research (2023–2024 priority)
- Atrial enhancer logic and AF: Circulation 2024 identified a TBX5/GATA4-dependent atrial enhancer network modulated by ZFPM2/FOG2. Genetic interaction between Tbx5 and Zfpm2 reshaped atrial conduction and mitigated AF substrate, providing mechanistic insight into conduction phenotypes and arrhythmia risk relevant to HOS. Apr 2024. URL: https://doi.org/10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46)
- Maintenance of atrial identity by TBX5: A 2023 study mapped TBX5-sensitive enhancer loops and showed dosage-sensitive atrial identity maintenance in postnatal cardiomyocytes, linking TBX5 dose to chromatin architecture and gene expression. Oct 2023. URL: https://doi.org/10.1038/s44161-023-00334-7 (grant2025dosedependentsensitivityof pages 20-23)
- Chromatin partners in atrial cardiomyocytes: 2024 work demonstrated TBX5 interaction with CHD4 (NuRD) to maintain atrial gene networks and rhythm homeostasis; loss of CHD4 enhanced AF susceptibility, highlighting chromatin-level contributions to HOS electrophysiology. Dec 2024. URL: https://doi.org/10.1101/2024.12.04.626894 (sweat2024chd4interactswith pages 1-6)
- 3D genome dosage effects: Early 2025 preprint showed dose-dependent disruption of 3D genome features by TBX5 reduction in human cardiomyocytes, supporting a structural mechanism for enhancer malfunction in congenital heart disease. Jan 2025. URL: https://doi.org/10.1101/2025.01.09.632202 (grant2025dosedependentsensitivityof pages 20-23)
- Case-based TBX5 regulatory mechanisms: A 2023 case report proposed 3′-UTR variants and miRNA-mediated modulation of TBX5 and documented TBX5’s direct transcriptional activation of novel cardiac targets (TEKT2/TEKT4/SPTB) in cardiomyocytes, illustrating dosage and regulatory complexity. Mar 2023. URL: https://doi.org/10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5)

Current applications and real-world implementations
- Risk gene network for atrial arrhythmia: The TBX5/GATA4/FOG2 enhancer network and observed genetic rescue (Tbx5 haploinsufficiency mitigated by Zfpm2 haploinsufficiency) suggest targetable cofactors and enhancers for rhythm modulation in congenital atrial disease, informing therapeutic hypothesis generation for arrhythmia in HOS. Apr 2024. URL: https://doi.org/10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46)
- Chromatin-targeted approaches: The requirement for TBX5 to partner with CHD4 and BAF suggests that modulating chromatin remodeling might stabilize atrial identity and conduction programs. Although not yet clinical in HOS, these findings guide disease modeling strategies with hiPSC-derived cardiomyocytes and organoid systems. Dec 2024; Oct 2023. URLs: https://doi.org/10.1101/2024.12.04.626894; https://doi.org/10.1038/s44161-023-00334-7 (sweat2024chd4interactswith pages 1-6, grant2025dosedependentsensitivityof pages 20-23)

Expert opinions and analysis from authoritative sources
- The Circulation 2024 study integrates mouse genetics, human atrial chromatin, and enhancer biochemistry to conclude that HF-associated transcriptional changes antagonize a TBX5/GATA4 atrial rhythm network, directly linking TBX5 dosage perturbation to atrial electrophysiology and AF risk. Apr 2024. URL: https://doi.org/10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46)
- Biology 2024 review underscores TBX5 dosage sensitivity and cooperative action with GATA4/NKX2-5 in septation and chamber-specific programs, synthesizing developmental and CHD genetics literature into a cohesive model applicable to HOS. Nov 2024. URL: https://doi.org/10.3390/biology13110911 (cervantessalazar2024geneticinsightsinto pages 8-10)

Relevant statistics and data
- Atrial enhancers: The 2023 study reported “510 chromatin loops sensitive to TBX5 dosage” in atrial cardiomyocytes, underscoring the scope of dose effects on the 3D genome. Oct 2023. URL: https://doi.org/10.1038/s44161-023-00334-7 (grant2025dosedependentsensitivityof pages 20-23)
- Genetic interaction metrics from Circulation 2024 included alterations in P-wave duration and AF induction susceptibility with Tbx5/Zfpm2 compound genotypes, supporting conduction phenotypes in TBX5 dosage reduction. Apr 2024. URL: https://doi.org/10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46)

Core Pathophysiology
- Primary mechanisms: TBX5 haploinsufficiency reduces enhancer activity and disrupts dosage-sensitive 3D chromatin architecture in atrial cardiomyocytes, impairing chamber identity and conduction gene networks; TBX5 cooperates with GATA4 and NKX2-5 at conserved enhancers and requires chromatin remodeling partners (BAF/SWI-SNF; CHD4/NuRD) to maintain cardiomyocyte-specific programs. In limb, TBX5 is essential for forelimb initiation and radial patterning. (broman2024agenomiclink pages 42-46, grant2025dosedependentsensitivityof pages 20-23, sweat2024chd4interactswith pages 1-6, cervantessalazar2024geneticinsightsinto pages 8-10, lang2023casereportnovel pages 3-5)
- Dysregulated pathways: Atrial enhancer networks controlling Ca2+ handling and conduction (e.g., Atp2a2, Ryr2; connexins) and atrial identity factors are compromised when TBX5 dose falls; TBX5/GATA4/FOG2 interactions repress or activate subsets of enhancers, modulating atrial rhythm. (broman2024agenomiclink pages 42-46, grant2025dosedependentsensitivityof pages 20-23)
- Affected cellular processes: Enhancer accessibility (H3K27ac), chromatin looping/TAD integrity, transcriptional activation/repression via cofactor complexes, atrial cardiomyocyte identity maintenance, and conduction system maturation. (sweat2024chd4interactswith pages 1-6, grant2025dosedependentsensitivityof pages 20-23, broman2024agenomiclink pages 42-46)

Key Molecular Players
- Genes/Proteins: TBX5 (HGNC:11610), GATA4 (HGNC:4172), NKX2-5 (HGNC:7781), ZFPM2/FOG2 (HGNC:12855), CHD4 (HGNC:1914), SMARCA4/BRG1 (HGNC:11100). (broman2024agenomiclink pages 42-46, sweat2024chd4interactswith pages 1-6, cervantessalazar2024geneticinsightsinto pages 8-10, vanlerberghe2024déterminismemoléculairedes pages 125-128)
- Chemical entities: Retinoic acid can modulate chamber identity in differentiation systems intersecting TBX5 networks. (grant2025dosedependentsensitivityof pages 20-23)
- Cell types: Atrial cardiomyocytes, conduction system cells (including Purkinje lineage), limb bud mesenchyme. (broman2024agenomiclink pages 42-46, sweat2024chd4interactswith pages 1-6, lang2023casereportnovel pages 3-5)
- Anatomical locations: Atria and atrial conduction system; forelimb bud/radial ray. (broman2024agenomiclink pages 42-46, lang2023casereportnovel pages 3-5, vanlerberghe2024déterminismemoléculairedes pages 125-128)

Biological Processes (GO) disrupted
- Atrial septum morphogenesis (GO:0003181): TBX5 dosage/cofactor interactions needed for endocardial survival and septation programs. (cervantessalazar2024geneticinsightsinto pages 8-10)
- Cardiac conduction (GO:0061337): Enhancer-controlled connexins and Ca2+ handling genes under TBX5/GATA4/FOG2 regulate atrial conduction and AF susceptibility. (broman2024agenomiclink pages 42-46)
- Limb bud formation (GO:0030326): TBX5-dependent initiation/outgrowth of forelimb LPM; haploinsufficiency → radial anomalies. (lang2023casereportnovel pages 3-5)
- Regulation of gene expression, epigenetic (GO:0040029): TBX5 relies on BAF and CHD4 to remodel chromatin at cardiac enhancers. (sweat2024chd4interactswith pages 1-6)

Cellular Components
- Chromatin (GO:0000785) and enhancer (GO:0035326): TBX5 binds active enhancers and loop anchors; TBX5 dose affects loops/TADs. (grant2025dosedependentsensitivityof pages 20-23, broman2024agenomiclink pages 42-46)
- Nucleosome (GO:0000786): BAF/NuRD remodelers at TBX5 targets mediate access and repression/activation dynamics. (sweat2024chd4interactswith pages 1-6, vanlerberghe2024déterminismemoléculairedes pages 125-128)

Disease Progression (sequence of events)
1) Germline variant reduces TBX5 dosage/function (often haploinsufficiency). 2) In the embryo, TBX5 insufficiency impairs enhancer activation and 3D chromatin organization in atrial/chamber myocardium; cofactor balance (GATA4, NKX2-5, ZFPM2/FOG2) and chromatin partners (BAF, CHD4) are dysregulated. 3) Downstream targets critical for septation, atrial identity, conduction, and Ca2+ handling (e.g., Atp2a2, Ryr2, connexins) are misregulated; atrial enhancer function is compromised. 4) Clinically, defects manifest as atrial/ventricular septal defects, atrial conduction delay/arrhythmia (AF risk), and upper-limb radial ray malformations due to failed forelimb initiation/patterning. (broman2024agenomiclink pages 42-46, grant2025dosedependentsensitivityof pages 20-23, sweat2024chd4interactswith pages 1-6, lang2023casereportnovel pages 3-5, cervantessalazar2024geneticinsightsinto pages 8-10)

Phenotypic Manifestations (key clinical phenotypes)
- Radial ray anomalies (e.g., triphalangeal thumb, hypoplasia/aplasia). (vanlerberghe2024déterminismemoléculairedes pages 125-128)
- Atrial septal defect, ventricular septal defect. (cervantessalazar2024geneticinsightsinto pages 8-10)
- Conduction system disease (e.g., prolonged P-wave, atrioventricular block), atrial fibrillation susceptibility. (broman2024agenomiclink pages 42-46)

Gene/protein annotations with ontology terms
- TBX5 (HGNC:11610): DNA-binding transcription factor; dosage-sensitive regulator of cardiac and limb development; acts at enhancers within chromatin; interacts with GATA4/NKX2-5/FOG2; partners with BAF and CHD4. (broman2024agenomiclink pages 42-46, sweat2024chd4interactswith pages 1-6, cervantessalazar2024geneticinsightsinto pages 8-10, grant2025dosedependentsensitivityof pages 20-23)
- GATA4 (HGNC:4172): Cardiac zinc-finger TF; co-occupies atrial enhancers with TBX5; modulates conduction gene expression. (broman2024agenomiclink pages 42-46)
- NKX2-5 (HGNC:7781): Homeobox TF; synergizes with TBX5 for chamber/conduction gene activation (e.g., connexins). (cervantessalazar2024geneticinsightsinto pages 8-10)
- ZFPM2/FOG2 (HGNC:12855): Cofactor that represses or modulates TBX5/GATA4-dependent enhancers; genetic interaction with TBX5 affects atrial conduction and AF. (broman2024agenomiclink pages 42-46)
- CHD4 (HGNC:1914): NuRD ATPase partnering with TBX5 to maintain atrial identity and rhythm homeostasis. (sweat2024chd4interactswith pages 1-6)
- SMARCA4/BRG1 (HGNC:11100): BAF/SWI-SNF ATPase; collaborates with TBX5 in cardiac development and septation. (vanlerberghe2024déterminismemoléculairedes pages 125-128)

Phenotype associations (HP terms)
- Atrial septal defect (HP:0001631). (cervantessalazar2024geneticinsightsinto pages 8-10)
- Ventricular septal defect (HP:0001629). (cervantessalazar2024geneticinsightsinto pages 8-10)
- Atrial fibrillation (HP:0005110). (broman2024agenomiclink pages 42-46)
- Atrioventricular block (HP:0001678) and P-wave prolongation (HP:0031646). (broman2024agenomiclink pages 42-46)
- Radial ray abnormality (HP:0002984), Triphalangeal thumb (HP:0004098), Thumb aplasia (HP:0011304). (vanlerberghe2024déterminismemoléculairedes pages 125-128)

Cell type involvement (CL terms)
- Atrial cardiomyocyte (CL:0002495): TBX5-dependent identity and enhancer function. (sweat2024chd4interactswith pages 1-6)
- Cardiac Purkinje fiber cell (CL:0000731): conduction phenotype relevance via TBX5-regulated network. (broman2024agenomiclink pages 42-46)
- Limb bud mesenchyme (CL:0002322): forelimb initiation via TBX5 program. (lang2023casereportnovel pages 3-5)

Anatomical locations (UBERON terms)
- Heart atrium (UBERON:0002373) and atrial conduction system (UBERON:0004535): primary cardiac sites of TBX5 enhancer network action relevant to HOS phenotypes. (broman2024agenomiclink pages 42-46)
- Forelimb bud (UBERON:0004385) and radial ray (UBERON:0004380): limb structures impacted by TBX5 insufficiency. (lang2023casereportnovel pages 3-5, vanlerberghe2024déterminismemoléculairedes pages 125-128)

Chemical entities (CHEBI)
- Retinoic acid (CHEBI:26536): modulates chamber identity and intersects TBX5-regulated differentiation trajectories in human cardiomyocyte models. (grant2025dosedependentsensitivityof pages 20-23)

Evidence items with PMIDs/DOIs/URLs
- Circulation 2024 (Broman et al.), DOI: 10.1161/circulationaha.123.066804; Apr 2024; URL: https://doi.org/10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46)
- Nature Cardiovascular Research 2023 (Sweat et al.), DOI: 10.1038/s44161-023-00334-7; Oct 2023; URL: https://doi.org/10.1038/s44161-023-00334-7 (grant2025dosedependentsensitivityof pages 20-23)
- bioRxiv 2024 (Sweat et al.), DOI: 10.1101/2024.12.04.626894; Dec 2024; URL: https://doi.org/10.1101/2024.12.04.626894 (sweat2024chd4interactswith pages 1-6)
- bioRxiv 2025 (Grant et al.), DOI: 10.1101/2025.01.09.632202; Jan 2025; URL: https://doi.org/10.1101/2025.01.09.632202 (grant2025dosedependentsensitivityof pages 20-23)
- Biology 2024 (Cervantes-Salazar et al.), DOI: 10.3390/biology13110911; Nov 2024; URL: https://doi.org/10.3390/biology13110911 (cervantessalazar2024geneticinsightsinto pages 8-10)
- Frontiers in Genetics 2023 (Lang et al.), DOI: 10.3389/fgene.2023.1063202; Mar 2023; URL: https://doi.org/10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5)
- Additional background (interactions/older foundations) referenced within 2024 review and radial anomalies overview (Vanlerberghe 2024): TBX5–NKX2-5–GATA4 synergy and BAF dependence in septation. (vanlerberghe2024déterminismemoléculairedes pages 125-128)

Ontology mapping artifact
| Entity type | Standard ID (ontology) | Entity/term | Mechanistic role in Holt–Oram syndrome pathophysiology | Supporting source (PMID/DOI) |
|---|---:|---|---|---|
| Gene / TF | HGNC:11610 | TBX5 | Dosage-sensitive T-box transcription factor; haploinsufficiency disrupts cardiac chamber identity, atrial enhancer activity, conduction genes and forelimb initiation | 10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5) |
| Gene / TF | HGNC:4172 | GATA4 | Cardiac cofactor that co-occupies enhancers with TBX5 to regulate atrial/chamber genes and conduction-related targets | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Gene / TF | HGNC:7781 | NKX2-5 | Synergizes with TBX5 to activate conduction and chamber-specific genes (e.g., CX40); important for septation and cardiomyocyte differentiation | 10.3390/biology13110911 (cervantessalazar2024geneticinsightsinto pages 8-10) |
| Gene / TF | HGNC:1914 | CHD4 | Chromatin remodeler (NuRD) that interacts with TBX5 to maintain atrial cardiomyocyte gene networks and rhythm homeostasis | 10.1101/2024.12.04.626894 (sweat2024chd4interactswith pages 1-6) |
| Gene / TF | HGNC:11100 | SMARCA4 / BRG1 | SWI/SNF (BAF) ATPase partner of TBX5 involved in chromatin remodelling required for cardiac septation and chamber patterning | 10.1016/j.devcel.2016.01.009 (vanlerberghe2024déterminismemoléculairedes pages 125-128) |
| Gene / TF | HGNC:12855 | ZFPM2 / FOG2 | Modulates a TBX5/GATA4-dependent atrial enhancer network; genetic interaction alters atrial conduction and AF risk | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Biological process | GO:0003181 | Atrial septum morphogenesis | TBX5 dosage and cofactor interactions regulate endocardial/myocardial programs required for septum formation | 10.3390/biology13110911 (cervantessalazar2024geneticinsightsinto pages 8-10) |
| Biological process | GO:0061337 | Cardiac conduction | TBX5–NKX2-5–GATA4 enhancer program controls connexins and Ca2+ handling genes affecting conduction/arrhythmia susceptibility | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Biological process | GO:0030326 | Limb bud formation | TBX5 initiates forelimb program in lateral plate mesoderm via interactions with SALL4/FGF signaling; haploinsufficiency → radial defects | 10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5) |
| Biological process | GO:0040029 | Regulation of gene expression, epigenetic | TBX5 function depends on chromatin remodellers (BAF/CHD4) and enhancer accessibility (H3K27ac) to set cardiomyocyte identity | 10.1101/2024.12.04.626894 (sweat2024chd4interactswith pages 1-6) |
| Cellular component | GO:0000785 | Chromatin | TBX5 binds enhancers/loop anchors within chromatin; TBX5 dosage alters 3D chromatin folding and loop/TAD integrity | 10.1101/2025.01.09.632202 (grant2025dosedependentsensitivityof pages 20-23) |
| Cellular component | GO:0035326 | Enhancer | TBX5/GATA4/FOG2 co-occupy conserved enhancers (H3K27ac+/ATAC+) that regulate atrial/conduction genes; enhancer sensitivity is dose-dependent | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Cellular component | GO:0000786 | Nucleosome | SWI/SNF (BAF) and NuRD components remodel nucleosomes at TBX5-target loci to permit or restrict cardiac transcription programs | 10.1016/j.devcel.2016.01.009 (vanlerberghe2024déterminismemoléculairedes pages 125-128) |
| Cell type | CL_0002495 | Atrial cardiomyocyte | Primary cardiac cell type where TBX5 maintains atrial identity, enhancer accessibility and rhythm gene programs; loss → arrhythmia susceptibility | 10.1101/2024.12.04.626894 (sweat2024chd4interactswith pages 1-6) |
| Cell type | CL_0000731 | Cardiac Purkinje fiber cell | Conduction-cell lineage influenced indirectly by TBX5-driven regulation of connexins and conduction gene networks | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Cell type | CL_0002322 | Limb bud mesenchyme | TBX5 expression in lateral plate mesoderm/mesenchyme initiates forelimb outgrowth and radial specification; haploinsufficiency → radial ray anomalies | 10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5) |
| Anatomical structure | UBERON:0002373 | Heart atrium | Atrial-specific gene regulatory networks (TBX5/GATA4) and enhancers are central to atrial development and conduction phenotypes in HOS | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Anatomical structure | UBERON:0004535 | Atrial conduction system | TBX5 dosage affects genes (e.g., CX40/Atp2a2/Ryr2) and enhancer topology important for atrial conduction and AF risk | 10.1161/circulationaha.123.066804 (broman2024agenomiclink pages 42-46) |
| Anatomical structure | UBERON:0004385 | Forelimb bud | TBX5-driven transcriptional program initiates forelimb bud formation and patterning; perturbation causes radial defects of HOS | 10.3389/fgene.2023.1063202 (lang2023casereportnovel pages 3-5) |
| Anatomical structure | UBERON:0004380 | Radial ray | Classic HOS phenotype reflecting disrupted TBX5-dependent radial patterning and FGF/SALL4 interactions | (vanlerberghe2024déterminismemoléculairedes pages 125-128) |
| Chemical entity | CHEBI:26536 | Retinoic acid | Modulates chamber/ventricular identity during cardiomyocyte differentiation and can influence TBX5-associated chamber specification programs | 10.1101/2025.01.09.632202 (grant2025dosedependentsensitivityof pages 20-23) |


*Table: Compact mapping of key genes, processes, cell types, anatomical locations and a chemical relevant to Holt–Oram syndrome, showing their ontology IDs, mechanistic roles, and primary supporting literature (DOI plus context ID). This table is useful for ontology annotation and evidence tracking in a disease knowledge base.*

Limitations and notes
- While the atrial enhancer and chromatin remodeling findings are robust and recent, direct clinical intervention studies in HOS leveraging these mechanisms are not yet available. Some chromatin studies are preprints and await peer review. (grant2025dosedependentsensitivityof pages 20-23, sweat2024chd4interactswith pages 1-6)

Conclusion
HOS pathophysiology centers on TBX5 haploinsufficiency disrupting enhancer-driven, chromatin-dependent transcriptional programs in atrial cardiomyocytes and forelimb mesenchyme. Cooperative regulation with GATA4/NKX2-5 and modulation by ZFPM2/FOG2, together with dependence on BAF and CHD4, mechanistically explain septation defects, conduction disease, and arrhythmia risk alongside radial ray limb malformations. Recent 2023–2024 studies provide convergent evidence that TBX5 dosage modulates atrial identity through enhancer networks and 3D chromatin architecture, offering testable translational hypotheses for rhythm stabilization and developmental precision medicine in HOS. (broman2024agenomiclink pages 42-46, grant2025dosedependentsensitivityof pages 20-23, sweat2024chd4interactswith pages 1-6, cervantessalazar2024geneticinsightsinto pages 8-10, lang2023casereportnovel pages 3-5, vanlerberghe2024déterminismemoléculairedes pages 125-128)

References

1. (broman2024agenomiclink pages 42-46): Michael T. Broman, Rangarajan D. Nadadur, Carlos Perez-Cervantes, Ozanna Burnicka-Turek, Sonja Lazarevic, Anna Gams, Brigitte Laforest, Jeffrey D. Steimle, Sabrina Iddir, Zhezhen Wang, Linsin Smith, Stefan R. Mazurek, Harold E. Olivey, Pingzhu Zhou, Margaret Gadek, Kaitlyn M. Shen, Zoheb Khan, Joshua W.M. Theisen, Xinan H. Yang, Kohta Ikegami, Igor R. Efimov, William T. Pu, Christopher R. Weber, Elizabeth M. McNally, Eric C. Svensson, and Ivan P. Moskowitz. A genomic link from heart failure to atrial fibrillation risk: fog2 modulates a tbx5/gata4-dependent atrial gene regulatory network. Circulation, 149:1205-1230, Apr 2024. URL: https://doi.org/10.1161/circulationaha.123.066804, doi:10.1161/circulationaha.123.066804. This article has 8 citations and is from a highest quality peer-reviewed journal.

2. (grant2025dosedependentsensitivityof pages 20-23): Zoe L. Grant, Shuzhen Kuang, Shu Zhang, Abraham J. Horrillo, Kavitha S. Rao, Vasumathi Kameswaran, Carine Joubran, Pik Ki Lau, Keyi Dong, Bing Yang, Weronika M. Bartosik, Nathan R. Zemke, Bing Ren, Irfan S. Kathiriya, Katherine S. Pollard, and Benoit G. Bruneau. Dose-dependent sensitivity of human 3d chromatin to a heart disease-linked transcription factor. bioRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.09.632202, doi:10.1101/2025.01.09.632202. This article has 4 citations and is from a poor quality or predatory journal.

3. (sweat2024chd4interactswith pages 1-6): Mason E. Sweat, Wei Shi, Erin M. Keating, Anna Ponek, Jie Li, Qing Ma, Chaehyoung Park, Michael A. Trembley, Yi Wang, Vassilios J. Bezzerides, Frank L. Conlon, and William T. Pu. Chd4 interacts with tbx5 to maintain the gene regulatory network of postnatal atrial cardiomyocytes. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.04.626894, doi:10.1101/2024.12.04.626894. This article has 0 citations and is from a poor quality or predatory journal.

4. (cervantessalazar2024geneticinsightsinto pages 8-10): Jorge L. Cervantes-Salazar, Nonanzit Pérez-Hernández, Juan Calderón-Colmenero, José Manuel Rodríguez-Pérez, María G. González-Pacheco, Clara Villamil-Castañeda, Angel A. Rosas-Tlaque, and Diego B. Ortega-Zhindón. Genetic insights into congenital cardiac septal defects—a narrative review. Biology, 13:911, Nov 2024. URL: https://doi.org/10.3390/biology13110911, doi:10.3390/biology13110911. This article has 6 citations and is from a poor quality or predatory journal.

5. (lang2023casereportnovel pages 3-5): Yuheng Lang, Yue Zheng, Bingcai Qi, Weifeng Zheng, Chengxiu Zhao, Hu Zhai, Gang Wang, Zhiqiang Luo, and Tong Li. Case report: novel tbx5-related pathogenic mechanism of holt–oram syndrome. Frontiers in Genetics, Mar 2023. URL: https://doi.org/10.3389/fgene.2023.1063202, doi:10.3389/fgene.2023.1063202. This article has 8 citations and is from a peer-reviewed journal.

6. (vanlerberghe2024déterminismemoléculairedes pages 125-128): C Vanlerberghe. Déterminisme moléculaire des anomalies radiales. Unknown journal, 2024.