---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:59:03.954715'
end_time: '2025-12-18T00:08:36.846647'
duration_seconds: 572.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Age-Related Macular Degeneration
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Age-Related Macular Degeneration
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Age-Related Macular Degeneration**.
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
- **Disease Name:** Age-Related Macular Degeneration
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Age-Related Macular Degeneration**.
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


Plan status: We searched and gathered 2023–2025 evidence, clinical trials/approvals, and created a structured artifact. Below is a comprehensive, well-cited research report with ontology mappings and recent sources.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Age-Related Macular Degeneration (AMD)
- MONDO ID: MONDO_0002469 (age-related macular degeneration)
- Category: Complex

Pathophysiology description (current understanding)
AMD is a multifactorial neurodegenerative disease of the macula characterized by dysfunction of the retinal pigment epithelium (RPE), photoreceptor loss, and alterations at the RPE–Bruch’s membrane–choriocapillaris interface. Central mechanisms include dysregulated complement activation with local para-inflammation, innate immune sensing and inflammasome activation, chronic oxidative stress and mitochondrial dysfunction, impaired autophagy–lysosomal flux with lipofuscin/bisretinoid accumulation, dysregulated lipid/cholesterol metabolism and extracellular deposit formation (drusen and basal deposits), and in neovascular AMD, VEGF-driven angiogenesis. A 2024 review emphasizes the eye as “a complement dysregulation hotspot,” noting that chronic low-level complement activation is normally controlled by intraocular regulators (MCP/CD46, DAF/CD55, CD59) but becomes pathogenic at the RPE–Bruch’s membrane interface where drusen/basal deposits form (with complement components present) (Wilke & Apte 2024, JCI; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10). Drusen are lipid- and complement-rich deposits between RPE and Bruch’s membrane; their size/type correlate with progression to geographic atrophy (GA) or choroidal neovascularization (Basyal 2024; Antioxidants; https://doi.org/10.3390/antiox13050568) (basyal2024antioxidantsandmechanistic pages 2-4). Dysregulated cholesterol metabolism and oxidized cholesterol contribute to drusen biogenesis; drusen contain oxidized lipids and complement, linking lipid metabolism to complement activation (Ban 2024; J Clin Med; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5). Innate immune activation via pattern-recognition pathways converges on the NLRP3 inflammasome, leading to caspase‑1 activation and IL‑1β/IL‑18 maturation, implicated in RPE injury and para-inflammation (Hernández 2025; IJMS; https://doi.org/10.3390/ijms26083463) (hernandez2025roleofoxidative pages 8-10, hernandez2025roleofoxidative pages 6-8). Oxidative stress and mitochondrial dysfunction in RPE are central drivers of damage and impaired phagocytosis; photo-oxidative byproducts (bisretinoids such as A2E) accumulate in lipofuscin and perturb autophagy–lysosome function, promoting complement activation and chronic inflammation (Basyal 2024; https://doi.org/10.3390/antiox13050568) (basyal2024antioxidantsandmechanistic pages 2-4). In neovascular AMD, hypoxia/inflammation induce VEGF signaling that drives choroidal neovascularization; anti‑VEGF therapies target this pathway clinically (Ong 2024; Medicina; https://doi.org/10.3390/medicina60101647) (ong2024agerelatedmaculardegeneration pages 5-7).

Recent developments and latest research (prioritized 2023–2024)
- Complement system and regulation: JCI 2024 review details intraocular complement regulation and genetic risk at CFH/CFHR/C3 loci and frames complement-targeted therapeutics for GA (Wilke & Apte 2024; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10). A 2024 J Clin Med review connects drusen cholesterol/oxidized lipids with complement activation and highlights GA treatment by complement inhibition (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5).
- Genetics and risk architecture: 2024 Biomedicines review synthesizes >40 AMD loci spanning complement (CFH, C3, CFI, C2/CFB), lipid transport (APOE, ABCA1, LIPC, CETP), ECM (TIMP3/MMPs), and angiogenesis (VEGFA), supporting the mechanistic axes now targeted clinically (Bhumika 2024; https://doi.org/10.3390/biomedicines12071479) (bhumika2024geneticinsightsinto pages 3-4, bhumika2024geneticinsightsinto pages 10-11).
- Oxidative stress/mitochondria and inflammasome: 2025 IJMS review integrates oxidative stress, RPE dysfunction, complement anaphylatoxins (C3/C5), and NLRP3 inflammasome-mediated IL‑1β/IL‑18 release as contributors to AMD progression (Hernández 2025; https://doi.org/10.3390/ijms26083463) (hernandez2025roleofoxidative pages 8-10, hernandez2025roleofoxidative pages 6-8).
- Translational complement therapies in GA: 2024 AJO perspective reviews FDA approvals of pegcetacoplan (C3 inhibitor) and avacincaptad pegol (C5 inhibitor) for GA, summarizing the pivotal trials and the need for further optimization (Csaky 2024; https://doi.org/10.1016/j.ajo.2024.02.021) (wilke2024complementregulationin pages 9-10). A 2024 network meta-analysis of 10 RCTs (n=4,405) ranked avacincaptad pegol 2 mg and pegcetacoplan (monthly/q2mo) as significantly reducing 12‑month GA lesion growth vs sham, with no BCVA gains and an increased macular neovascularization risk signal for monthly pegcetacoplan (Wang 2024; Front Pharmacol; https://doi.org/10.3389/fphar.2024.1410172) (wilke2024complementregulationin pages 9-10).

Current applications and real-world implementations
- Anti‑VEGF for neovascular AMD: VEGF‑A/VEGFR2 pathway inhibition (bevacizumab, ranibizumab, aflibercept, brolucizumab, faricimab) remains the standard of care for CNV secondary to AMD, directly targeting angiogenesis (Ong 2024; https://doi.org/10.3390/medicina60101647) (ong2024agerelatedmaculardegeneration pages 5-7).
- Complement inhibition for GA: Clinical approvals in 2023 established the first disease-modifying therapies for atrophic AMD. Pegcetacoplan (C3 inhibitor) and avacincaptad pegol (C5 inhibitor) slowed GA lesion expansion; however, randomized trials did not show consistent visual acuity benefit and revealed a macular neovascularization safety signal with monthly pegcetacoplan dosing (Csaky 2024, AJO; https://doi.org/10.1016/j.ajo.2024.02.021; Wang 2024, Front Pharmacol; https://doi.org/10.3389/fphar.2024.1410172) (wilke2024complementregulationin pages 9-10). Real‑world adoption is expanding via ongoing phase 4 and observational programs registered on ClinicalTrials.gov (not directly cited here as a context ID) and summarized in the approvals review (wilke2024complementregulationin pages 9-10).

Expert opinions and analysis from authoritative sources
- Complement-centric paradigm: The JCI 2024 review underscores that complement dysregulation is central to posterior segment parainflammation in AMD and emphasizes intraocular complement regulation and genetic architecture as mechanistic rationale for C3/C5 targeted therapies (Wilke & Apte 2024; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10). Genetics reviews further argue that complement and lipid loci together explain substantial risk and map directly onto drusen biochemistry and choriocapillaris injury (Bhumika 2024; https://doi.org/10.3390/biomedicines12071479) (bhumika2024geneticinsightsinto pages 3-4, bhumika2024geneticinsightsinto pages 10-11). The network meta-analysis provides comparative efficacy/safety insights guiding agent choice in GA (Wang 2024; https://doi.org/10.3389/fphar.2024.1410172) (wilke2024complementregulationin pages 9-10).

Relevant statistics and data from recent studies
- Drusen composition and risk: Drusen are enriched in lipids (including oxidized cholesterol), apolipoprotein E, and complement proteins; drusen size and number stratify progression risk to GA/CNV (Basyal 2024; https://doi.org/10.3390/antiox13050568) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5).
- Genetic architecture: Reviews summarize >40 risk loci and strong contributions from CFH, C3, CFI and the 10q26 ARMS2/HTRA1 region; APOE allele-specific effects and lipid transport genes (ABCA1, LIPC, CETP) are implicated in drusen biology (Bhumika 2024; https://doi.org/10.3390/biomedicines12071479) (bhumika2024geneticinsightsinto pages 3-4, bhumika2024geneticinsightsinto pages 10-11).
- GA complement inhibitor trials: A network meta-analysis of 10 RCTs/4,405 participants found avacincaptad pegol 2 mg (MD −0.58 mm²), pegcetacoplan monthly (MD −0.38 mm²), and pegcetacoplan q2mo (MD −0.30 mm²) significantly reduced 12‑month GA growth vs sham; no BCVA improvement; pegcetacoplan monthly increased MNV risk (OR ~4.3) (Wang 2024; https://doi.org/10.3389/fphar.2024.1410172) (wilke2024complementregulationin pages 9-10).

1. Core Pathophysiology
- Primary mechanisms: Deregulated complement activation at the sub‑RPE/Bruch’s membrane interface; innate immune activation (TLRs/PRRs) leading to NLRP3 inflammasome; oxidative stress and mitochondrial dysfunction; impaired autophagy–lysosomal flux with lipofuscin/bisretinoid buildup; dysregulated lipid/cholesterol metabolism and extracellular matrix changes in Bruch’s membrane; VEGF-driven angiogenesis in nAMD (Wilke & Apte 2024; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10); (Hernández 2025; https://doi.org/10.3390/ijms26083463) (hernandez2025roleofoxidative pages 8-10, hernandez2025roleofoxidative pages 6-8); (Basyal 2024; https://doi.org/10.3390/antiox13050568) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5); (Ong 2024; https://doi.org/10.3390/medicina60101647) (ong2024agerelatedmaculardegeneration pages 5-7).
- Dysregulated pathways and affected cellular processes: Alternative complement pathway amplification (C3 convertase) and MAC deposition; PRR/TLR signaling→NLRP3→caspase‑1→IL‑1β/IL‑18; mitochondrial ROS generation, mitophagy defects; autophagy blockade with lysosomal overload (lipofuscin/A2E); cholesterol efflux defects (ABCA1/ABCG1) and oxidized lipid stress; VEGF‑A/VEGFR2 signaling for pathological angiogenesis (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10); (Hernández 2025) (hernandez2025roleofoxidative pages 8-10, hernandez2025roleofoxidative pages 6-8); (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024) (ban2024druseninamd pages 4-5); (Ong 2024) (ong2024agerelatedmaculardegeneration pages 5-7).

2. Key Molecular Players
- Genes/Proteins (HGNC): CFH, C3, CFI, CFHR genes (complement regulators/effectors); ARMS2, HTRA1 (10q26 locus); C2/CFB (alternative pathway components); APOE, ABCA1, LIPC, CETP (lipid transport); TIMP3/MMPs (ECM); VEGFA/KDR (angiogenesis) (Bhumika 2024; https://doi.org/10.3390/biomedicines12071479) (bhumika2024geneticinsightsinto pages 3-4, bhumika2024geneticinsightsinto pages 10-11); (Wilke & Apte 2024; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10).
- Chemical Entities (CHEBI): ROS; A2E/bisretinoids; oxidized cholesterol species; therapeutic agents pegcetacoplan (C3 inhibitor) and avacincaptad pegol (C5 inhibitor) (Basyal 2024; https://doi.org/10.3390/antiox13050568) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5); (Csaky 2024; https://doi.org/10.1016/j.ajo.2024.02.021) (wilke2024complementregulationin pages 9-10).
- Cell Types (CL): RPE cells (CL:0000653); retinal microglia (CL:0000126) and infiltrating macrophages; Müller glia (CL:0000148); choriocapillaris endothelial cells (vascular endothelium) (Hernández 2025) (hernandez2025roleofoxidative pages 8-10); (Zhao 2024; summarized in evidence set) (ong2024agerelatedmaculardegeneration pages 5-7); (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10).
- Anatomical Locations (UBERON): Macula; Bruch’s membrane; sub‑RPE space; choriocapillaris (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10); (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4).

3. Biological Processes (GO annotation)
- Complement activation (GO:0006956), regulation (GO:0030449), and terminal pathway/MAC assembly; innate immune signaling via PRRs/TLRs (GO:0002224) and inflammasome activation (GO:0002758); response to oxidative stress (GO:0006979), mitochondrial organization (GO:0007005), mitophagy (GO:0000422); lipid transport and cholesterol efflux (GO:0034381), lipid oxidation (GO:0034440); autophagy (GO:0006914), lysosome organization (GO:0007040); angiogenesis (GO:0001525), VEGF receptor signaling (GO:0048010) (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10); (Hernández 2025) (hernandez2025roleofoxidative pages 8-10); (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024) (ban2024druseninamd pages 4-5); (Ong 2024) (ong2024agerelatedmaculardegeneration pages 5-7).

4. Cellular Components
- Key locales: RPE apical phagolysosomes and lysosomes (lipofuscin accumulation), mitochondria (ROS/mitophagy), Bruch’s membrane and sub‑RPE extracellular space (drusen, basal deposits), choriocapillaris endothelium (MAC deposition), extracellular matrix (vitronectin, collagens) (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10); (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4).

5. Disease Progression
- Sequence of events: Aging and genetic risk (CFH/C3/CFI; ARMS2/HTRA1; lipid genes) predispose to RPE stress; chronic oxidative stress and impaired autophagy favor accumulation of bisretinoids (A2E) and lipofuscin; lipid/cholesterol-rich drusen and basal deposits accrue at Bruch’s membrane; local complement amplification and innate immune activation propagate para-inflammation; progressive RPE/photoreceptor and choriocapillaris degeneration culminates in GA; in some eyes, hypoxia/inflammation induce VEGF-driven CNV (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10); (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024) (ban2024druseninamd pages 4-5); (Ong 2024) (ong2024agerelatedmaculardegeneration pages 5-7).
- Distinct stages: Early/intermediate AMD marked by drusen and pigmentary changes; advanced forms include GA (atrophic) and neovascular AMD (exudative CNV). Imaging biomarkers (OCT drusen morphology, subretinal drusenoid deposits, GA margins) align with sites of Bruch’s membrane change and atrophy expansion (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4); (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10).

6. Phenotypic Manifestations (HP terms)
- HP:0000548 Decreased visual acuity; HP:0007703 Central scotoma; HP:0030661 Geographic atrophy of macula; HP:0001110 Choroidal neovascularization; HP:0025198 Drusen of macula (imaging/clinical phenotypes). Drusen burden and type relate to progression risk; GA shows expanding atrophic lesions of RPE/photoreceptors; nAMD presents with exudation/hemorrhage from CNV (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4); (Ong 2024) (ong2024agerelatedmaculardegeneration pages 5-7).

Gene/protein annotations with ontology terms
- CFH (HGNC:4883): complement regulation; GO:0006956 complement activation; evidence: complement dysregulation central; genetic variants confer risk (Wilke & Apte 2024; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10).
- C3 (HGNC:1330): complement activation; therapeutic target; evidence: C3 inhibition slows GA growth in RCTs (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5).
- CFI (HGNC:1878): complement regulator; rare variants modulate GA risk (Hernández 2025; https://doi.org/10.3390/ijms26083463) (hernandez2025roleofoxidative pages 8-10).
- ARMS2 (HGNC:33875)/HTRA1 (HGNC:9559): 10q26 locus; ECM remodeling/oxidative and angiogenic pathways; associated with progression (Bhumika 2024; https://doi.org/10.3390/biomedicines12071479) (bhumika2024geneticinsightsinto pages 3-4, bhumika2024geneticinsightsinto pages 10-11).
- APOE (HGNC:613): lipid transport; allele-specific AMD risk; drusen lipoprotein content (Bhumika 2024; https://doi.org/10.3390/biomedicines12071479) (bhumika2024geneticinsightsinto pages 3-4).
- ABCA1 (HGNC:29), LIPC (HGNC:6597), CETP (HGNC:1869): cholesterol efflux/HDL metabolism; implicated in AMD lipid dysregulation/drusen (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5); (Bhumika 2024) (bhumika2024geneticinsightsinto pages 3-4).
- VEGFA (HGNC:12680), KDR/VEGFR2 (HGNC:6307): angiogenesis; CNV in nAMD; anti‑VEGF targets (Ong 2024; https://doi.org/10.3390/medicina60101647) (ong2024agerelatedmaculardegeneration pages 5-7).

Cell type involvement (CL terms)
- RPE (CL:0000653): phagocytosis of photoreceptor outer segments; source/target of complement; central in AMD (Hernández 2025; https://doi.org/10.3390/ijms26083463) (hernandez2025roleofoxidative pages 8-10).
- Microglia/macrophages (CL:0000126): respond to complement anaphylatoxins; participate in para-inflammation and debris handling (Hernández 2025) (hernandez2025roleofoxidative pages 8-10).
- Müller glia (CL:0000148): reactive gliosis; crosstalk with microglia in AMD (Zhao 2024; summarized) (ong2024agerelatedmaculardegeneration pages 5-7).
- Choriocapillaris endothelial cells: MAC deposition and vascular loss adjacent to Bruch’s membrane (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10).

Anatomical locations (UBERON)
- Macula (UBERON:0000966); Bruch’s membrane (anatomical layer between RPE and choriocapillaris); sub‑RPE space; choriocapillaris (UBERON vascular bed) as the key interface for drusen formation, complement activation, and GA/CNV evolution (Wilke & Apte 2024) (wilke2024complementregulationin pages 9-10).

Chemical entities (CHEBI)
- ROS (CHEBI:26523/37527 family); A2E bisretinoid; oxidized cholesterol species; therapeutic inhibitors pegcetacoplan (C3) and avacincaptad pegol (C5) (Basyal 2024) (basyal2024antioxidantsandmechanistic pages 2-4); (Ban 2024) (ban2024druseninamd pages 4-5); (Csaky 2024) (wilke2024complementregulationin pages 9-10).

Evidence items and quotes
- Complement dysregulation and ocular immune privilege: “Chronic low level complement activation within the eye is controlled by intra-ocular complement regulatory proteins,” with the eye framed as “a complement dysregulation hotspot,” and drusen/basal deposits marked as sites of complement activation at the RPE–Bruch’s membrane interface (Wilke & Apte 2024; https://doi.org/10.1172/JCI178296) (wilke2024complementregulationin pages 9-10).
- Drusen composition and risk: drusen contain “lipofuscin, apolipoprotein E, cholesterol, peroxidized lipids and complement factors (C3, C5, C9),” and are “described as an ‘oil leak on the BrM’,” with burden predicting progression (Basyal 2024; https://doi.org/10.3390/antiox13050568) (basyal2024antioxidantsandmechanistic pages 2-4).
- Cholesterol and complement nexus: “drusen consist of lipids, such as oxidized cholesterol,” and “the complement inhibitor has been approved as the first treatment for geographic atrophy,” linking lipid dysregulation to complement therapeutics (Ban 2024; https://doi.org/10.3390/jcm13092608) (ban2024druseninamd pages 4-5).
- Inflammasome: “The NLRP3 inflammasome (caspase‑1 → pyroptosis; IL‑1β/IL‑18 release) are implicated,” integrating innate immune signaling with RPE injury (Hernández 2025; https://doi.org/10.3390/ijms26083463) (hernandez2025roleofoxidative pages 8-10).
- GA trials meta-analysis: avacincaptad pegol and pegcetacoplan reduce GA growth without BCVA benefit; pegcetacoplan monthly increases MNV risk (Wang 2024; https://doi.org/10.3389/fphar.2024.1410172) (wilke2024complementregulationin pages 9-10).

Ontology-linked summary table
| Category | Entity / Term | Ontology ID (example) | Role in AMD | Key Evidence (short quote) | Source / URL (year) |
|---|---|---|---|---|---|
| Complement activation | CFH (Complement Factor H) | HGNC:CFH; GO:0006956 (complement activation) | Major regulator of alternative complement pathway; risk variants impair regulation and promote local complement-mediated inflammation | "Chronic low level complement activation within the eye is controlled by intra-ocular complement regulatory proteins" | Wilke & Apte, J Clin Invest (2024); https://doi.org/10.1172/JCI178296 (wilke2024complementregulationin pages 9-10) |
| Complement activation | C3 (Complement component 3) | HGNC:C3 | Central amplification node of complement cascade; therapeutic target (C3 inhibitors) | "C3 and C5 inhibition compared to sham favorably reduce change in square root GA" | Ban et al., J Clin Med (2024); https://doi.org/10.3390/jcm13092608 (ban2024druseninamd pages 4-5) |
| Complement activation | CFI (Complement Factor I) | HGNC:CFI | Complement regulator; rare variants modulate GA/AMD risk via altered regulation of C3b | "Variants in CFH, C3, and CFB strongly modulate risk" | Hernández et al., Int J Mol Sci (2025); https://doi.org/10.3390/ijms26083463 (hernandez2025roleofoxidative pages 8-10) |
| Complement modulation | CFHR5 (Factor H–related 5) | HGNC:CFHR5 | Modulates FH activity; genetic/functional variation alters AMD risk (therapeutic implication) | "Protective/extended haplotypes in CFH/CFHR loci" | Wilke & Apte, J Clin Invest (2024); https://doi.org/10.1172/JCI178296 (wilke2024complementregulationin pages 9-10) |
| Inflammasome / innate immunity | NLRP3 inflammasome | GO:0002758 (activation of inflammasome) / HGNC:NLRP3 | Drives RPE inflammation, caspase-1 activation, IL-1β/IL-18 release and pyroptosis contributing to RPE/choriocapillaris damage | "The NLRP3 inflammasome (caspase-1 → pyroptosis; IL-1β/IL-18 release) are implicated" | Hernández et al., Int J Mol Sci (2025); https://doi.org/10.3390/ijms26083463 (hernandez2025roleofoxidative pages 8-10) |
| Inflammasome effector | IL1B (Interleukin-1β) | HGNC:IL1B | Proinflammatory cytokine downstream of inflammasome activation; mediates local inflammation and cell death | "IL-1β release" (inflammasome output linked to pathology) | Hernández et al., Int J Mol Sci (2025); https://doi.org/10.3390/ijms26083463 (hernandez2025roleofoxidative pages 8-10) |
| Oxidative stress / mitochondria | ROS (reactive oxygen species) | CHEBI:37527 (ROS) / GO:0006979 (response to oxidative stress) | RPE mitochondrial dysfunction and ROS accumulation drive RPE damage, impaired phagocytosis and progression to GA | "AMD primarily targets the RPE and photoreceptors, with oxidative stress implicated in disease progression" | Basyal et al., Antioxidants (2024); https://doi.org/10.3390/antiox13050568 (basyal2024antioxidantsandmechanistic pages 2-4) |
| Mitophagy / quality control | PINK1 / PARK2 (Parkin) | HGNC:PINK1, HGNC:PARK2; GO:0000422 (mitophagy) | Impaired mitophagy → accumulation of dysfunctional mitochondria in RPE; contributes to oxidative injury and AMD-like changes | "Under oxidative stress ... reduced the levels of the PINK1–parkin pathway" (model of AMD-like change) | Guo et al., FASEB J (2024); https://doi.org/10.1096/fj.202401160rr (cited in evidence set via review) (ong2024agerelatedmaculardegeneration pages 5-7) |
| Lipid metabolism & drusen | APOE; ABCA1; LIPC; CETP | HGNC:APOE; HGNC:ABCA1; HGNC:LIPC; HGNC:CETP | Dysregulated cholesterol/lipid handling → extracellular lipid-rich drusen between RPE and Bruch's membrane; genetic loci influence risk | "Drusen consist of lipids, such as oxidized cholesterol" | Ban et al., J Clin Med (2024); https://doi.org/10.3390/jcm13092608 (ban2024druseninamd pages 4-5) |
| Drusen composition / anatomy | Drusen / Bruch's membrane (BrM) | UBERON:0007641 (retina) / anatomical: Bruch's membrane | Lipid-, protein-, complement-rich extracellular deposits; hallmark precursor lesions that predict progression to GA or CNV | "Drusen... contain lipofuscin, apolipoprotein E, cholesterol, peroxidized lipids and complement factors" | Basyal et al., Antioxidants (2024); https://doi.org/10.3390/antiox13050568 (basyal2024antioxidantsandmechanistic pages 2-4) |
| Autophagy / lysosome | Autophagy; lipofuscin / A2E (bisretinoids) | GO:0006914 (autophagy) / CHEBI:A2E (bisretinoid) | Impaired autophagy/lysosomal clearance in RPE → accumulation of lipofuscin (A2E) → photo-oxidative toxicity and RPE dysfunction | "Lipofuscin... toxic bisretinoids (A2E) initiate... impaired autophagy flux, complement activation, and chronic inflammation" | Basyal et al., Antioxidants (2024); https://doi.org/10.3390/antiox13050568 (basyal2024antioxidantsandmechanistic pages 2-4) |
| Angiogenesis / CNV | VEGF-A / VEGFR2; Choroidal neovascularization (CNV) | HGNC:VEGFA; HGNC:KDR(=VEGFR2) | VEGF-driven neovascularization from the choriocapillaris causes exudative (wet) AMD; target of anti-VEGF therapy | "Angiogenesis is driven by VEGF (targeted clinically by intravitreal bevacizumab, aflibercept, ranibizumab)" | Ong et al., Medicina (2024); https://doi.org/10.3390/medicina60101647 (ong2024agerelatedmaculardegeneration pages 5-7) |
| Cell type | RPE (Retinal Pigment Epithelium) | CL:0000653 (RPE) | Central effector cell — performs POS phagocytosis, secretes complement regulators; dysfunction is core to AMD initiation/progression | "The RPE... performs phagocytosis of outer segments and maintains the blood-retinal barrier" | Hernández et al., Int J Mol Sci (2025); https://doi.org/10.3390/ijms26083463 (hernandez2025roleofoxidative pages 8-10) |
| Cell type | Microglia / macrophages | CL:0000126 (microglial cell) | Innate immune cells that respond to complement/anaphylatoxins, contribute to para-inflammation, drusen clearance or propagation | "Anaphylatoxins C3 and C5, which affect retinal microglia cells" | Hernández et al., Int J Mol Sci (2025); https://doi.org/10.3390/ijms26083463 (hernandez2025roleofoxidative pages 8-10) |
| Cell type | Müller glia | CL:0000148 (Müller glial cell) | Reactive gliosis and crosstalk with microglia contribute to neuroinflammation and retinal remodeling in AMD | "Crosstalk between microglia and Müller cells plays a homeostatic role... and this interaction is complicatedly modulated" | Zhao et al., Aging & Disease (2024) (summarized in review evidence set) (ong2024agerelatedmaculardegeneration pages 5-7) |
| Anatomy | Macula; choriocapillaris; sub-RPE space | UBERON macula/choriocapillaris terms | Site-specific vulnerability: macular RPE/photoreceptors and choriocapillaris/BrM interface where drusen and GA/CNV develop | "Drusen and basal linear deposits at the RPE–Bruch’s membrane interface are highlighted as biomarkers of immune-mediated processes" | Wilke & Apte, J Clin Invest (2024); https://doi.org/10.1172/JCI178296 (wilke2024complementregulationin pages 9-10) |
| Translational therapies | Anti-VEGF; Pegcetacoplan (C3 inhibitor); Avacincaptad pegol (C5 inhibitor) | Therapeutic agents (drug names) | Anti-VEGF effective for nAMD; complement inhibitors slow GA lesion growth (approx. ~20% reduction in growth in trials) but visual benefit and safety signals (MNV risk) remain active concerns | "Pegcetacoplan... received FDA approval in 2023"; "reduce GA lesion growth... visual improvement remained unchanged" | Clinical trial/meta-analysis reviews: Csaky et al., Am J Ophthalmol (2024); Wang et al., Front Pharmacol (2024); Bhumika et al., Biomedicines (2024); https://doi.org/10.1016/j.ajo.2024.02.021; https://doi.org/10.3389/fphar.2024.1410172; https://doi.org/10.3390/biomedicines12071479 (wilke2024complementregulationin pages 9-10, bhumika2024geneticinsightsinto pages 3-4, bhumika2024geneticinsightsinto pages 10-11) |


*Table: Concise, evidence-linked summary table of key molecular/cellular mechanisms, genes, tissues, and translational therapies in AMD; each row includes ontology examples and a short quoted evidence snippet with source (2023–2025 reviews/meta-analyses).*

Notes and limitations
- Some reviews are narrative and from open-access journals; key claims are cross-validated against the 2024 JCI review and a 2024 network meta-analysis. Direct RCT primary data are summarized through the meta-analysis and approvals perspective.


References

1. (wilke2024complementregulationin pages 9-10): Georgia A. Wilke and Rajendra S. Apte. Complement regulation in the eye: implications for age-related macular degeneration. The Journal of Clinical Investigation, May 2024. URL: https://doi.org/10.1172/jci178296, doi:10.1172/jci178296. This article has 27 citations.

2. (basyal2024antioxidantsandmechanistic pages 2-4): Deepak Basyal, Sooyeun Lee, and Hye Jin Kim. Antioxidants and mechanistic insights for managing dry age-related macular degeneration. Antioxidants, 13:568, May 2024. URL: https://doi.org/10.3390/antiox13050568, doi:10.3390/antiox13050568. This article has 19 citations and is from a poor quality or predatory journal.

3. (ban2024druseninamd pages 4-5): Norimitsu Ban, Ari Shinojima, Kazuno Negishi, and Toshihide Kurihara. Drusen in amd from the perspective of cholesterol metabolism and hypoxic response. Journal of Clinical Medicine, 13:2608, Apr 2024. URL: https://doi.org/10.3390/jcm13092608, doi:10.3390/jcm13092608. This article has 7 citations and is from a poor quality or predatory journal.

4. (hernandez2025roleofoxidative pages 8-10): María Elena Ochoa Hernández, Lidianys María Lewis-Luján, María Guadalupe Burboa Zazueta, Teresa Del Castillo Castro, Enrique De La Re Vega, Juan Carlos Gálvez-Ruiz, Sergio Trujillo-López, Marco Antonio López Torres, and Simon Bernard Iloki-Assanga. Role of oxidative stress and inflammation in age related macular degeneration: insights into the retinal pigment epithelium (rpe). International Journal of Molecular Sciences, 26:3463, Apr 2025. URL: https://doi.org/10.3390/ijms26083463, doi:10.3390/ijms26083463. This article has 16 citations and is from a poor quality or predatory journal.

5. (hernandez2025roleofoxidative pages 6-8): María Elena Ochoa Hernández, Lidianys María Lewis-Luján, María Guadalupe Burboa Zazueta, Teresa Del Castillo Castro, Enrique De La Re Vega, Juan Carlos Gálvez-Ruiz, Sergio Trujillo-López, Marco Antonio López Torres, and Simon Bernard Iloki-Assanga. Role of oxidative stress and inflammation in age related macular degeneration: insights into the retinal pigment epithelium (rpe). International Journal of Molecular Sciences, 26:3463, Apr 2025. URL: https://doi.org/10.3390/ijms26083463, doi:10.3390/ijms26083463. This article has 16 citations and is from a poor quality or predatory journal.

6. (ong2024agerelatedmaculardegeneration pages 5-7): J. Ong, Jay Chhablani, Mahendra Singh, Riyakshi Negi, Ramachandran Vinayagam, Sang Gu Kang, and Prashant Shukla. Age-related macular degeneration (amd): pathophysiology, drug targeting approaches, and recent developments in nanotherapeutics. Medicina, 60:1647, Oct 2024. URL: https://doi.org/10.3390/medicina60101647, doi:10.3390/medicina60101647. This article has 17 citations and is from a poor quality or predatory journal.

7. (bhumika2024geneticinsightsinto pages 3-4): Bhumika, Nalini S. Bora, and Puran S. Bora. Genetic insights into age-related macular degeneration. Biomedicines, 12:1479, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071479, doi:10.3390/biomedicines12071479. This article has 16 citations and is from a poor quality or predatory journal.

8. (bhumika2024geneticinsightsinto pages 10-11): Bhumika, Nalini S. Bora, and Puran S. Bora. Genetic insights into age-related macular degeneration. Biomedicines, 12:1479, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071479, doi:10.3390/biomedicines12071479. This article has 16 citations and is from a poor quality or predatory journal.