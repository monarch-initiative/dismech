---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-05T16:09:09.271034'
end_time: '2025-12-05T16:17:16.628767'
duration_seconds: 487.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
  mondo_id: MONDO:0005404
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 11
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
- **MONDO ID:** MONDO:0005404 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myalgic Encephalomyelitis/Chronic Fatigue Syndrome**.
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
- **Disease Name:** Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
- **MONDO ID:** MONDO:0005404 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myalgic Encephalomyelitis/Chronic Fatigue Syndrome**.
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
- Disease Name: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome (ME/CFS)
- MONDO ID: MONDO:0005404
- Category: Complex, multisystem, post-infectious syndrome

Pathophysiology description (current understanding)
ME/CFS is characterized by a network of immune, vascular, neuroimmune, and metabolic abnormalities that likely initiate after an infectious trigger and are sustained by maladaptive immune–neurovascular crosstalk. Convergent 2023–2025 evidence indicates: persistent innate immune hyperreactivity; reproducible natural killer (NK) cell dysfunction and altered T‑cell immunometabolism; endothelial dysfunction with coagulopathy and microcirculatory impairment; complement/coagulation pathway remodeling; possible autoantibody contributions in subsets (e.g., G‑protein–coupled receptor GPCR targets), though with conflicting evidence across platforms; TRPM3 ion-channel dysfunction in NK cells with impaired Ca2+ flux; neurovascular changes involving brainstem and reduced cerebral perfusion; and metabolic inflexibility/mitochondrial stress that worsen with exertion and underlie post‑exertional malaise (PEM). Multi-omics and proteomic studies document exercise-provoked shifts in inflammatory and metabolic mediators, supporting PEM as a biologically measurable exacerbation rather than a purely symptomatic phenomenon (DOI: 10.1101/2025.07.23.25332049, 2025-07-24; DOI: 10.1101/2025.05.28.25328245, 2025-05-28). (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25)

Direct quotes supporting key concepts
- “Heightened innate immunity may trigger chronic inflammation, fatigue and post-exertional malaise in ME/CFS,” with exercise provoking increases in inflammatory and oxidative stress signals and complement activation (medRxiv, DOI: 10.1101/2025.07.23.25332049). (che2025heightenedinnateimmunity pages 9-11)
- Senescent/exhausted immune cells “secrete high levels of pro-inflammatory cytokines… resulting in chronic sterile inflammation (inflammaging)” and drive muscle catabolism (Comprehensive Physiology, DOI: 10.1002/cph4.70056). (luo2025understandingmyalgicencephalomyelitischronic pages 9-10)

Recent developments and latest research (2023–2024 priority; 2025 where essential)
- Biomarkers review (BMC Medicine, 2023) synthesized 101 studies and concluded immune dysfunction—especially reduced NK cell cytotoxicity—is the most consistent biological signature across cohorts; it also emphasized methodological rigor and careful control selection to avoid false inferences (DOI: 10.1186/s12916-023-02893-9, 2023-05). (maksoud2023biomarkersformyalgic pages 10-11)
- Exercise-challenge multi-omics (medRxiv 2025) showed innate hyper-responsiveness (e.g., IL‑6 responses to LPS/poly I:C), ECM disruption (e.g., reduced tetranectin/CLEC3B), oxidative stress surrogates, and a rise in GDF15 correlating with fatigue after exertion—integrating immune, redox, peroxisomal/mitochondrial and lipid pathway derangements that flare during PEM (DOI: 10.1101/2025.07.23.25332049, 2025-07-24). (che2025heightenedinnateimmunity pages 9-11)
- Circulating proteome profiling (preprint, 2025) reported increased secreted proteins from brain, intestine, liver, skeletal muscle and lymphoid tissue; elevations in coagulation/complement proteins; reductions in enzyme classes and neutrophil-released proteins; and higher triglycerides (TAG 1.35±0.89 vs 0.87±0.31 mM, p≈0.025) and non-esterified fatty acids (NEFA 0.40±0.28 vs 0.21±0.13 mM, p≈0.026) in ME/CFS versus controls (DOI: 10.1101/2025.05.28.25328245, 2025-05-28). (hoel2025chartingthecirculating pages 21-25)
- Immunosenescence perspective (Comprehensive Physiology, 2025) integrates immune aging/exhaustion, chronic cytokine signaling (SASP), mitochondrial dysfunction, dysautonomia, and PEM-related bioenergetics, proposing testable axes (PD‑1/PD‑L1, TRPM3/PIP2, mTOR/AMPK) for stratified trials (DOI: 10.1002/cph4.70056, 2025-09). (luo2025understandingmyalgicencephalomyelitischronic pages 9-10, luo2025understandingmyalgicencephalomyelitischronic pages 13-13)
- Synthesis papers (2024–2025) emphasize a unifying system-level model with endothelial dysfunction, coagulation anomalies, and hypoperfusion, coupled to immune/metabolic changes and neurovascular dysregulation (URLs/DOIs in artifact table). (hoel2025chartingthecirculating pages 21-25, pavlovichUnknownyearcomparisonofclinical pages 41-44)

Current applications and real-world implementations
- Immunoadsorption/plasmapheresis and immunomodulatory strategies are being trialed in subsets (e.g., patients with GPCR autoantibodies), with preliminary improvements reported alongside antibody titer reductions; however, heterogeneity, rebounds, and need for randomized replication remain (trial overviews and clinical discussions, 2023–2025). (pavlovichUnknownyearcomparisonofclinical pages 41-44, kavyani2024…ofa pages 35-36)
- TRPM3 restoration by naltrexone (LDN) has been demonstrated in vitro/ex vivo for NK cells, positioning TRPM3 as a potential treatment biomarker; translation to controlled clinical efficacy in ME/CFS requires definitive trials (reviewed in 2024–2025 translational work). (renzpolsterUnknownyearguardianangelsoff pages 17-20, luo2025understandingmyalgicencephalomyelitischronic pages 13-13)

Expert opinions and analysis from authoritative sources
- The BMC Medicine systematic review (2023) concludes that immune dysfunction—particularly NK cytotoxicity deficits—represents the most reproducible biological signal; it also cautions about case definition heterogeneity and technical biases in immune assays, underscoring the need for standardized protocols (DOI: 10.1186/s12916-023-02893-9). (maksoud2023biomarkersformyalgic pages 10-11)
- Immunosenescence framing (Comprehensive Physiology, 2025) provides a mechanistic link between chronic low-grade inflammation, immune exhaustion, mitochondrial impairment, skeletal muscle atrophy pathways, and dysautonomia, aligning with observed PEM exacerbation after exertion (DOI: 10.1002/cph4.70056). (luo2025understandingmyalgicencephalomyelitischronic pages 9-10, luo2025understandingmyalgicencephalomyelitischronic pages 13-13)

Relevant statistics and data from recent studies
- Exercise-challenge multi-omics: post-exertional increases in GDF15 correlated with fatigue; innate responses to microbial ligands were exaggerated; complement activation increased after exercise; ECM proteins (e.g., CLEC3B) reduced; lipid abnormalities and oxidative stress signatures were present (medRxiv, 2025; DOI: 10.1101/2025.07.23.25332049). (che2025heightenedinnateimmunity pages 9-11)
- Serum proteome/biochemistry: triglycerides (TAG) 1.35±0.89 vs 0.87±0.31 mM (p≈0.025) and NEFA 0.40±0.28 vs 0.21±0.13 mM (p≈0.026) were higher in ME/CFS; secretome skewed toward coagulation/complement and inflammatory mediators (medRxiv, 2025; DOI: 10.1101/2025.05.28.25328245). (hoel2025chartingthecirculating pages 21-25)
- Immune cell bioenergetics: ME/CFS CD8+ T cells exhibit reduced mitochondrial membrane potential and both CD4+/CD8+ T cells show reduced glycolysis (JCI-linked synthesis cited in 2023 review) (BMC Medicine 2023). (maksoud2023biomarkersformyalgic pages 10-11)

Core Pathophysiology (mechanisms, pathways, processes)
- Innate immune hyperreactivity and PEM: Evidence of exaggerated cytokine responses to microbial ligands and exercise-triggered complement activation, ECM disruption, lipid/oxidative stress shifts; GDF15 rises correlate with fatigue, indicating a stress-responsive mitochondrial signal (DOI: 10.1101/2025.07.23.25332049). (che2025heightenedinnateimmunity pages 9-11)
- Adaptive immune dysfunction and immunometabolism: Reproducible deficits in NK function; T‑cell metabolic remodeling deficits (reduced glycolysis and mitochondrial potential), consistent with chronic immune stress/exhaustion (BMC Medicine 2023). (maksoud2023biomarkersformyalgic pages 10-11)
- Endothelial dysfunction, coagulation anomalies, microcirculatory impairment: Proteomic and clinical data indicate dysregulated coagulation/complement signatures and lipid perturbations that align with impaired endothelial function and hypoperfusion in tissues (DOI: 10.1101/2025.05.28.25328245). (hoel2025chartingthecirculating pages 21-25, pavlovichUnknownyearcomparisonofclinical pages 41-44)
- Complement/coagulation remodeling: Reports include downregulation of terminal complement (e.g., C9) with increased clotting-related proteins and inflammatory S100A8/A9; patterns may vary by cohort and platform but converge on immune–coagulation crosstalk. (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25)
- Autoantibodies to GPCRs: Evidence heterogeneous—some cohorts and interventional reports suggest pathogenic ß‑adrenergic/muscarinic antibodies in subsets; large-scale antigen profiling has yielded mixed or null findings, emphasizing careful phenotyping and assay selection. (kavyani2024…ofa pages 35-36, pavlovichUnknownyearcomparisonofclinical pages 41-44)
- Ion-channel dysfunction (TRPM3): Documented impaired Ca2+ flux in NK cells; restoration by naltrexone in vitro/ex vivo supports a modifiable channelopathy impacting immune and sensory/autonomic pathways. (renzpolsterUnknownyearguardianangelsoff pages 17-20, luo2025understandingmyalgicencephalomyelitischronic pages 13-13)
- Neurovascular/neuroinflammatory changes: Imaging/physiological syntheses describe brainstem involvement and reduced cerebral blood flow, consistent with dysautonomia and cognitive symptoms; a CNS stress‑response regulatory defect may sustain PEM and symptom relapses. (renzpolsterUnknownyearguardianangelsoff pages 17-20, hoel2025chartingthecirculating pages 21-25)
- Immunosenescence and chronic inflammation: SASP cytokines, NFκB/JAK‑STAT/FoxO signaling, and muscle atrophy gene programs (MuRF1/Atrogin1) provide a framework for persistent fatigue and exercise intolerance. (luo2025understandingmyalgicencephalomyelitischronic pages 9-10)

Key Molecular Players (with ontology-style labels)
- Genes/Proteins (HGNC): TRPM3 (TRPM3; Ca2+ channel); ADRB2 (β2‑adrenergic receptor); CHRM3 (M3 muscarinic receptor); THBS1 (thrombospondin‑1); PF4 (platelet factor 4); PROS1 (Protein S); C9 (Complement C9; MAC component); S100A8/S100A9 (calgranulins); GDF15 (stress-response cytokine) (examples reported across proteomic/multi-omic studies). (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25, renzpolsterUnknownyearguardianangelsoff pages 17-20)
- Chemical entities (CHEBI): triglycerides (triacylglycerols), non‑esterified fatty acids, lactate; redox mediators and prostaglandins implicated post-exertion; steroidal neuroactive ligand Pregnenolone sulfate (TRPM3 agonist) used experimentally. (che2025heightenedinnateimmunity pages 9-11, renzpolsterUnknownyearguardianangelsoff pages 17-20, hoel2025chartingthecirculating pages 21-25)
- Cell types (CL): natural killer cell (CL:0000623); CD8+ T cell (CL:0000625); CD4+ T cell (CL:0000624); endothelial cell (CL:0000115); platelet (CL:0000233); monocyte (CL:0000576); glial cells (microglia/astroglia implicated by neuroinflammatory frameworks). (maksoud2023biomarkersformyalgic pages 10-11, hoel2025chartingthecirculating pages 21-25, renzpolsterUnknownyearguardianangelsoff pages 17-20)
- Anatomical locations (UBERON): blood/plasma (UBERON:0001969); microvasculature/capillary (UBERON:0001982); brain (UBERON:0000955) and brainstem (UBERON:0002298); skeletal muscle (UBERON:0001134); small intestine/gut (UBERON:0002108). (hoel2025chartingthecirculating pages 21-25, renzpolsterUnknownyearguardianangelsoff pages 17-20)

Biological Processes (GO) disrupted
- Innate immune response (GO:0045087); complement activation (GO:0006956); blood coagulation/platelet activation (GO:0007596/GO:0030168); regulation of blood vessel diameter (GO:0097746); extracellular matrix organization (GO:0030198); calcium ion transmembrane transport (GO:0070588); T‑cell activation/metabolic reprogramming (GO:0042110/GO:0006096 glycolysis; GO:0005759 mitochondrial matrix involvement); fatty‑acid β‑oxidation (GO:0006635); response to oxidative stress (GO:0006979). (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25, maksoud2023biomarkersformyalgic pages 10-11, renzpolsterUnknownyearguardianangelsoff pages 17-20)

Cellular Components (GO-CC)
- Plasma membrane (GO:0005886; GPCRs, TRPM3); extracellular space (GO:0005615; secreted proteome shifts); platelet alpha granule (GO:0031091; PF4/THBS1 release); complement membrane attack complex (GO:0005579; C9); mitochondrion (GO:0005739; membrane potential); vascular endothelium (GO:0005930/CL term). (hoel2025chartingthecirculating pages 21-25, maksoud2023biomarkersformyalgic pages 10-11)

Disease Progression (sequence from trigger to clinical manifestation)
- Trigger: Often post-infectious. Early phase of innate hyperreactivity with dysregulated cytokine responses and complement activation. (che2025heightenedinnateimmunity pages 9-11)
- Establishment: Endothelial dysfunction and coagulation abnormalities with microcirculatory hypoperfusion, coupled with metabolic inflexibility and immune-cell bioenergetic impairment (T‑cell glycolysis↓, mitochondrial potential↓). (hoel2025chartingthecirculating pages 21-25, maksoud2023biomarkersformyalgic pages 10-11)
- Maintenance/Sustaining factors: Chronic low-grade inflammation (SASP), possible autoantibody networks in subsets, TRPM3 channelopathy impacting immune/autonomic signaling, and gut dysbiosis with microbial translocation; a CNS stress‑response regulatory defect may perpetuate PEM cycles. (luo2025understandingmyalgicencephalomyelitischronic pages 9-10, kavyani2024…ofa pages 35-36, renzpolsterUnknownyearguardianangelsoff pages 17-20, che2025heightenedinnateimmunity pages 9-11)
- PEM episodes: Exertion triggers coordinated increases in inflammatory/oxidative pathways, complement activity, ECM perturbations, lipid utilization shifts, and stress signals like GDF15, worsening hypoperfusion and mitochondrial stress—manifesting as delayed multi-symptom relapses. (che2025heightenedinnateimmunity pages 9-11)

Phenotypic Manifestations (HP) and links to mechanisms
- Post-exertional malaise (HP:0033630): Biologically tied to post-exercise innate activation, complement increase, oxidative stress, ECM/lipid shifts, and GDF15 rise (multi-omics). (che2025heightenedinnateimmunity pages 9-11)
- Orthostatic intolerance (HP:0001278) and dysautonomia (HP:0002271): Consistent with endothelial dysfunction, cerebral hypoperfusion, GPCR/autonomic signaling alterations, and brainstem involvement. (renzpolsterUnknownyearguardianangelsoff pages 17-20, pavlovichUnknownyearcomparisonofclinical pages 41-44)
- Cognitive impairment (“brain fog,” HP:0100543): Linked to neuroinflammation and reduced cerebral blood flow; stress‑response dysregulation in CNS/brainstem circuits. (renzpolsterUnknownyearguardianangelsoff pages 17-20)
- Fatigue (HP:0012378) and myalgia (HP:0003326): Correlate with immune exhaustion, mitochondrial dysfunction, muscle catabolic signaling (MuRF1/Atrogin1), and hypoperfusion. (luo2025understandingmyalgicencephalomyelitischronic pages 9-10, hoel2025chartingthecirculating pages 21-25)

Evidence items with PMIDs/DOIs/URLs and dates
- Maksoud R, et al. Biomarkers for ME/CFS: Immune dysfunction, NK deficits most consistent; BMC Medicine; DOI: 10.1186/s12916-023-02893-9; 2023-05-17. (maksoud2023biomarkersformyalgic pages 10-11)
- Che X, et al. Heightened innate immunity may trigger chronic inflammation, fatigue and PEM; medRxiv; DOI: 10.1101/2025.07.23.25332049; 2025-07-24. (che2025heightenedinnateimmunity pages 9-11)
- Hoel A, et al. Charting the circulating proteome in ME/CFS; medRxiv; DOI: 10.1101/2025.05.28.25328245; 2025-05-28. (hoel2025chartingthecirculating pages 21-25)
- Luo Y, et al. Immunosenescence perspective on ME/CFS; Comprehensive Physiology; DOI: 10.1002/cph4.70056; 2025-09. (luo2025understandingmyalgicencephalomyelitischronic pages 9-10, luo2025understandingmyalgicencephalomyelitischronic pages 13-13)
- Kavyani B. Multi-platform overview (immune, autoantibodies, metabolism); 2024 (preprint/compendium). (kavyani2024…ofa pages 35-36)
- Renz‑Polster H. CNS stress-response dysregulation hypothesis; year n/a (post‑2022 synthesis). (renzpolsterUnknownyearguardianangelsoff pages 17-20)
- Pavlovich CL, Yehuda S. Mechanistic synthesis (immune/vascular/metabolic); year n/a (refers to 2023–2024 sources). (pavlovichUnknownyearcomparisonofclinical pages 41-44)

Ontology-style annotations for knowledge base
- Genes/Proteins (HGNC): TRPM3; ADRB2; CHRM3; THBS1; PF4; PROS1; C9; S100A8; S100A9; GDF15. (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25, renzpolsterUnknownyearguardianangelsoff pages 17-20)
- Biological Processes (GO): GO:0045087; GO:0006956; GO:0007596; GO:0030168; GO:0097746; GO:0030198; GO:0070588; GO:0042110; GO:0006096; GO:0006635; GO:0006979. (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25, maksoud2023biomarkersformyalgic pages 10-11)
- Cellular Components (GO-CC): GO:0005886; GO:0005615; GO:0031091; GO:0005579; GO:0005739. (hoel2025chartingthecirculating pages 21-25, maksoud2023biomarkersformyalgic pages 10-11)
- Cell Types (CL): CL:0000623; CL:0000625; CL:0000624; CL:0000115; CL:0000233; CL:0000576. (maksoud2023biomarkersformyalgic pages 10-11, hoel2025chartingthecirculating pages 21-25)
- Anatomical Locations (UBERON): UBERON:0001969; UBERON:0001982; UBERON:0000955; UBERON:0002298; UBERON:0001134; UBERON:0002108. (renzpolsterUnknownyearguardianangelsoff pages 17-20, hoel2025chartingthecirculating pages 21-25)
- Chemical Entities (CHEBI): triacylglycerol; non‑esterified fatty acid; lactate; prostaglandin; pregnenolone sulfate. (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25, renzpolsterUnknownyearguardianangelsoff pages 17-20)

Mechanism-to-evidence summary
| Mechanism | Molecular / Cellular details | Key quantitative / quoted findings | Source (DOI / URL, date) |
|---|---|---:|---|
| Innate immune hyperreactivity / PEM | Exaggerated innate responses to microbial ligands (PBMC hyper-responsiveness), exercise-triggered increases in proinflammatory signals, complement activation, ECM disruption (tetranectin/CLEC3B down), lipid abnormalities and GDF15 rise after exertion | "Heightened innate immunity may trigger chronic inflammation, fatigue and post-exertional malaise in ME/CFS"; exercise-provoked proteomic/metabolomic shifts (GDF15 ↑ correlates with fatigue); complement activation after exercise (proteomic signal) (quote/paraphrase). | https://doi.org/10.1101/2025.07.23.25332049 (medRxiv, Jul 24 2025) (che2025heightenedinnateimmunity pages 9-11) |
| NK / T-cell immunometabolism | Reduced NK cytotoxicity and dysfunctional NK phenotype; CD8+ T cells with reduced mitochondrial membrane potential and impaired glycolysis at rest/after activation; altered immunometabolic cytokine associations | Reproducible NK abnormalities and impaired T-cell bioenergetics reported across cohorts; impaired mitochondrial membrane potential in CD8+ cells and reduced glycolysis in CD4+/CD8+ (Mandarano et al. syntheses). | BMC Med review DOI: 10.1186/s12916-023-02893-9 (May 2023); review/meta syntheses (maksoud2023biomarkersformyalgic pages 10-11, kavyani2024…ofa pages 35-36, luo2025understandingmyalgicencephalomyelitischronic pages 13-13) |
| Endothelial dysfunction & coagulation / microclots | Endothelial dysregulation, platelet hyperactivation, fibrinaloid (amyloid) microclots and impaired microcirculatory perfusion; dysregulated clotting proteins (eg TSP‑1/THBS1, PF4, Protein S/PROS1) | Clinical/proteomic biochemistry: higher triglycerides TAG 1.35±0.89 vs 0.87±0.31 mM and NEFA 0.40±0.28 vs 0.21±0.13 mM in ME/CFS vs controls (p≈0.025), supporting metabolic/vascular perturbation linked to endothelial pathology. | Proteome/secretion profiling (preprint) https://doi.org/10.1101/2025.05.28.25328245 (May 2025) (hoel2025chartingthecirculating pages 21-25); endothelial reviews (pavlovichUnknownyearcomparisonofclinical pages 41-44) |
| Complement / coagulation proteomics | Circulating proteomics show dysregulated coagulation proteins and altered complement components (e.g., reduced C9 in some data), upregulation of inflammatory S100 proteins (S100A9/A8) | Proteomics identify coherent shifts: complement machinery downregulation (C9 noted) alongside upregulated clotting-related proteins and inflammatory protein S100A8/A9 after profiling. | Nunes et al. proteomic signals summarized in Me/CFS proteome reviews and multi-omics (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25) |
| Autoantibodies to GPCRs (adrenergic / muscarinic) — conflicting evidence | Reports of autoantibodies to β‑adrenergic and muscarinic receptors in subsets; passive-transfer and apheresis/immunomodulation interventions explored, but large antigen‑profiling studies show mixed/null signals depending on platform | "Evidence for an autoimmune disease" discussed in reviews; autoantibody removal (immunoadsorption/plasmapheresis) produced preliminary clinical signals in subsets but findings are heterogeneous and assay-dependent. | Biomarker/systematic reviews and autoantibody analyses (BMC Med 2023; multi-platform reviews) (maksoud2023biomarkersformyalgic pages 10-11, kavyani2024…ofa pages 35-36, pavlovichUnknownyearcomparisonofclinical pages 41-44) |
| TRPM3 ion‑channel dysfunction & low‑dose naltrexone (LDN) | TRPM3 (Ca2+-permeable) dysfunction reported in NK cells → reduced Ca2+ flux; in vitro/ex vivo restoration of TRPM3 function by naltrexone/LDN suggests a modifiable ion‑channel deficit | TRPM3 dysfunction implicated in impaired pathogen clearance and immune signaling; TRPM3 function has been reported to be restored by naltrexone in cellular studies (proposed as therapeutic biomarker). | Reviews and translational studies emphasizing TRPM3 and treatment signal (luo2025understandingmyalgicencephalomyelitischronic pages 13-13, renzpolsterUnknownyearguardianangelsoff pages 17-20) |
| Neurovascular / neuroinflammation (brainstem & cerebral blood flow) | Brainstem volumetric changes, altered connectivity and reduced cerebral perfusion reported; neuroinflammatory signalling and impaired interoceptive/stress regulation implicated | Hypothesis: impaired CNS stress‑response and brainstem dysfunction sustain dysautonomia and impaired cerebral perfusion, contributing to cognitive dysfunction and PEM (conceptual and imaging evidence). | Conceptual and imaging syntheses (Renz‑Polster narrative; Hoel proteomics linking secreted brain proteins) (renzpolsterUnknownyearguardianangelsoff pages 17-20, hoel2025chartingthecirculating pages 21-25) |
| Gut dysbiosis, barrier disruption & ECM signalling | Reduced butyrate-producing taxa, microbial translocation/endotoxemia, extracellular matrix alterations (reduced tetranectin/CLEC3B, COMP) linked to systemic innate activation | Gut dysbiosis associated with reduced SCFA producers; ECM protein changes and translocation of microbial products may sustain innate immune hyperreactivity and systemic inflammation after exertion. | Multi-omics and proteome reports linking gut → immune signals (che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25) |
| Immunosenescence framework | Chronic immune aging/exhaustion (senescent T/NK cells, SASP secretion) drives low‑grade sterile inflammation, mitochondrial impairment and muscle catabolism (MuRF1/Atrogin1 activation pathways) | Quote: "secrete high levels of pro‑inflammatory cytokines... resulting in chronic sterile inflammation (inflammaging)." Senescence model links persistent inflammation to metabolic/mitochondrial dysfunction and fatigue. | Immunosenescence perspective and integrative reviews (Comprehensive Physiology review DOI: 10.1002/cph4.70056; multi-platform summaries) (luo2025understandingmyalgicencephalomyelitischronic pages 9-10, kavyani2024…ofa pages 35-36) |
| Clinical trials / real‑world implementations (immunoadsorption overview) | Immunoadsorption/plasmapheresis and other immunomodulatory interventions (B‑cell depletion, IVIG) trialed in subsets with elevated GPCR autoantibodies; ongoing exploratory randomized and cohort studies | Preliminary controlled exploratory trials of immunoadsorption and cohort reports show autoantibody titre reduction and some functional improvements in subsets, but rebound and heterogeneity reported; further RCTs recommended. | Clinical-trial overviews and trial discussions in ME/CFS literature and reviews (pavlovichUnknownyearcomparisonofclinical pages 41-44, kavyani2024…ofa pages 35-36, hoel2025chartingthecirculating pages 21-25) |


*Table: Table summarizing core molecular and cellular mechanisms in ME/CFS (2023–2025), key findings/quotes, quantitative signals (where available) and primary sources (context IDs). Useful as a compact evidence map linking mechanism → biomarkers → citations for a disease knowledge base.*

Plan status
- Evidence gathered, synthesized, and organized into ontology-aligned annotations and an evidence table. Remaining uncertainties chiefly involve heterogeneity in autoantibody findings and the need for randomized, mechanism-enriched clinical trials. (maksoud2023biomarkersformyalgic pages 10-11, che2025heightenedinnateimmunity pages 9-11, hoel2025chartingthecirculating pages 21-25, kavyani2024…ofa pages 35-36)

References

1. (che2025heightenedinnateimmunity pages 9-11): Xiaoyu Che, Amit Ranjan, Cheng Guo, Keming Zhang, Rochelle Goldsmith, Susan Levine, Kegan J. Moneghetti, Yali Zhai, Liner Ge, Nischay Mishra, Mady Hornig, Lucinda Bateman, Nancy G. Klimas, Jose G. Montoya, Daniel L. Peterson, Sabra L. Klein, Oliver Fiehn, Anthony L. Komaroff, and W. Ian Lipkin. Heightened innate immunity may trigger chronic inflammation, fatigue and post-exertional malaise in me/cfs. medRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.23.25332049, doi:10.1101/2025.07.23.25332049. This article has 3 citations.

2. (hoel2025chartingthecirculating pages 21-25): August Hoel, Fredrik Hoel, Sissel Elisabeth Furesund Dyrstad, Henrique Chapola, Ingrid Gurvin Rekeland, Kristin Risa, Kine Alme, Kari Sørland, Karl Albert Brokstad, Hans-Peter Marti, Olav Mella, Øystein Fluge, and Karl Johan Tronstad. Charting the circulating proteome in me/cfs: cross system profiling and mechanistic insights. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.28.25328245, doi:10.1101/2025.05.28.25328245. This article has 0 citations.

3. (luo2025understandingmyalgicencephalomyelitischronic pages 9-10): Yingzhe Luo, Huimin Xu, Shaoquan Xiong, and Jianlong Ke. Understanding myalgic encephalomyelitis/chronic fatigue syndrome physical fatigue through the perspective of immunosenescence. Comprehensive Physiology, Sep 2025. URL: https://doi.org/10.1002/cph4.70056, doi:10.1002/cph4.70056. This article has 1 citations and is from a peer-reviewed journal.

4. (maksoud2023biomarkersformyalgic pages 10-11): Rebekah Maksoud, Chandi Magawa, Natalie Eaton-Fitch, Kiran Thapaliya, and Sonya Marshall-Gradisnik. Biomarkers for myalgic encephalomyelitis/chronic fatigue syndrome (me/cfs): a systematic review. BMC Medicine, May 2023. URL: https://doi.org/10.1186/s12916-023-02893-9, doi:10.1186/s12916-023-02893-9. This article has 48 citations and is from a domain leading peer-reviewed journal.

5. (luo2025understandingmyalgicencephalomyelitischronic pages 13-13): Yingzhe Luo, Huimin Xu, Shaoquan Xiong, and Jianlong Ke. Understanding myalgic encephalomyelitis/chronic fatigue syndrome physical fatigue through the perspective of immunosenescence. Comprehensive Physiology, Sep 2025. URL: https://doi.org/10.1002/cph4.70056, doi:10.1002/cph4.70056. This article has 1 citations and is from a peer-reviewed journal.

6. (pavlovichUnknownyearcomparisonofclinical pages 41-44): CL Pavlovich and S Yehuda. Comparison of clinical and pathophysiological characteristics of myalgic encephalomyelitis/chronic fatigue syndrome …. Unknown journal, Unknown year.

7. (kavyani2024…ofa pages 35-36): B Kavyani. … of a multi-platform approach to identify new biomarkers of disease severity and progression in myalgic encephalomyelitis/chronic fatigue syndrome (me/cfs). Unknown journal, 2024.

8. (renzpolsterUnknownyearguardianangelsoff pages 17-20): H Renz-Polster. Guardian angels off duty? me/cfs is sustained by an impaired stress response in the central nervous system. Unknown journal, Unknown year.

## Citations

1. che2025heightenedinnateimmunity pages 9-11
2. luo2025understandingmyalgicencephalomyelitischronic pages 9-10
3. maksoud2023biomarkersformyalgic pages 10-11
4. hoel2025chartingthecirculating pages 21-25
5. luo2025understandingmyalgicencephalomyelitischronic pages 13-13
6. https://doi.org/10.1101/2025.07.23.25332049
7. https://doi.org/10.1101/2025.05.28.25328245
8. https://doi.org/10.1101/2025.07.23.25332049,
9. https://doi.org/10.1101/2025.05.28.25328245,
10. https://doi.org/10.1002/cph4.70056,
11. https://doi.org/10.1186/s12916-023-02893-9,