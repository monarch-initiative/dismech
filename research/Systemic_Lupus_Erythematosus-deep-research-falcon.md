---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:48:19.374296'
end_time: '2025-12-15T09:54:15.090699'
duration_seconds: 355.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Systemic Lupus Erythematosus
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Systemic Lupus Erythematosus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Systemic Lupus Erythematosus**.
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
- **Disease Name:** Systemic Lupus Erythematosus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Systemic Lupus Erythematosus**.
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
- Define scope and structure: summarize core mechanisms; enumerate key genes/proteins, cells, organs; map to ontologies; outline disease progression; relate mechanisms to phenotypes, biomarkers, and therapies; cite recent (2023–2025) literature with URLs and dates.
- Gather recent evidence emphasizing IFN-I axis, nucleic-acid sensing (TLR7/9), B/T cell crosstalk (Tfh/Tph, ABCs), complement/apoptotic clearance, NETosis/oxidative stress, organ damage (LN, NPSLE), and mechanism-led therapies.
- Synthesize narrative and structured annotations (GO, HGNC, CL, UBERON, CHEBI; HP). Provide direct quotes where they substantively support claims.

Disease entry overview
- Target Disease: Systemic Lupus Erythematosus
- MONDO ID: MONDO:0003582
- Category: Complex autoimmune disease

Pathophysiology description (current understanding)
Systemic lupus erythematosus (SLE) is a prototypic systemic autoimmune disease driven by breakdown of immune tolerance, chronic activation of innate nucleic acid–sensing pathways (especially the type I interferon axis), aberrant B- and T-cell help, impaired clearance of apoptotic and NETotic debris, and complement pathway perturbations leading to immune complex deposition and organ inflammation (kidney, skin, CNS, vasculature). Contemporary reviews highlight a unifying framework that integrates type I IFN signaling, TLR7/9-driven autoreactivity, neutrophil extracellular traps (NETs) and oxidative stress, B cell extrafollicular and germinal-center responses (including age-associated B cells, ABCs), and tissue injury mediated by immune complexes and complement activation (Oct 2024; https://doi.org/10.3390/ijms252010905) (moysidou2024lymphocyteschangetheir pages 18-20). NETs are now recognized as amplifiers of the pDC–TLR9–IFN-α loop and as sources of modified autoantigens; “impaired NET catabolism due to deficient serum DNase1 is associated with renal involvement,” while NET DNA–peptide complexes can protect nucleic acids from degradation and activate pDCs to produce IFN-α (Jul 2024; https://doi.org/10.1016/j.heliyon.2024.e33350) (yuan2024globalresearchtrends pages 10-10). 

Key mechanistic axes
- Type I interferon signature: An IFN-I–inflamed milieu is present in a majority of patients and shapes dysregulation across immune cell lineages. Stratified analyses link elevated IFN gene signatures and chemokines (e.g., CXCL10/CXCL13) to clinical phenotypes and therapy responses; notably, “High IFN gene signature [is associated with] favorable response to anifrolumab therapy” (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (wu2025immunecellaberrations pages 29-30).
- Nucleic-acid sensing via endosomal TLRs: B cell–intrinsic TLR7 signaling is a central driver of lupus pathology, whereas TLR9 can exert counter-regulatory effects; genetic and mechanistic data show that when TLR9 is absent, unrestrained TLR7 signaling worsens disease (2024; dissertation/manuscript synthesis) (cosgrove2024tolllikereceptor7 pages 160-164). As one concise conclusion from this body of work: “B cell–intrinsic TLR7 drives severe lupus,” and NOX2 (CYBB)–dependent ROS can negatively regulate TLR7–NF-κB signaling (cosgrove2024tolllikereceptor7 pages 160-164).
- Impaired clearance and complement: Defective apoptotic cell clearance and complement deficiencies increase exposure to nuclear antigens, propagate immune complex formation, and correlate with lupus nephritis; early-component complement defects (e.g., C1q) and impaired NET degradation are linked to renal injury and complement activation (Oct 2024; https://doi.org/10.3390/ijms252010905; Jul 2024; https://doi.org/10.1016/j.heliyon.2024.e33350) (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10).
- B–T collaboration and tolerance failure: Extrafollicular and GC pathways are both implicated. T follicular helper–like cells (ICOS+, PD-1+, IL-21+) expand and drive autoreactive B-cell differentiation; murine and human data show that blocking Tfh development ameliorates disease (Jul 2025; https://doi.org/10.3390/cells14141080) (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3). Age-associated B cells (ABCs; CD11c+, T-bet+) are enriched in SLE and correlate with IFN signatures and disease activity, linking IFN-BAFF-IL-21 circuits to persistent autoantibody production (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z; 2024 mechanistic synthesis) (wu2025immunecellaberrations pages 29-30, cosgrove2024tolllikereceptor7 pages 160-164).
- NETosis and oxidative stress: NETs fuel IFN-α production, directly activate autoreactive B cells, and trigger complement; oxidative stress and defective NET clearance amplify this loop (Jul 2024; https://doi.org/10.1016/j.heliyon.2024.e33350; Oct 2024; https://doi.org/10.3390/ijms252010905) (yuan2024globalresearchtrends pages 10-10, moysidou2024lymphocyteschangetheir pages 18-20).
- Neurovascular and CNS injury: Neuropsychiatric SLE reflects composite mechanisms (vasculopathy, microthrombi, inflammatory mediators) superimposed on systemic autoimmunity; “no single laboratory test is currently available to definitively confirm the diagnosis of NPSLE,” emphasizing mechanistic heterogeneity (Feb 2024; https://doi.org/10.3390/molecules29040747) (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).

Direct supporting statements (selected quotes)
- “Impairment of neutrophil extracellular trap degradation is associated with lupus nephritis… NETs… protect DNA from degradation, enabling activation of plasmacytoid dendritic cells (pDCs) through TLR9 and driving IFN-α production.” (Jul 2024; https://doi.org/10.1016/j.heliyon.2024.e33350) (yuan2024globalresearchtrends pages 10-10).
- “High IFN gene signature [→] favorable response to anifrolumab therapy,” underscoring mechanism-based stratification (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (wu2025immunecellaberrations pages 29-30).
- “B cell–intrinsic TLR7 drives severe lupus… [and] TLR9 can restrain differentiation of age/autoimmune-associated B cells and plasmablasts,” highlighting TLR7/9 counterpoints (2024; mechanistic synthesis) (cosgrove2024tolllikereceptor7 pages 160-164).
- “No single laboratory test is currently available to definitively confirm the diagnosis of NPSLE,” reflecting complex pathophysiology (Feb 2024; https://doi.org/10.3390/molecules29040747) (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).

Key molecular players
- Genes (HGNC):
  - TLR7 (HGNC:15631) – B cell–intrinsic driver; promotes RNA-associated autoantibodies and disease; counterbalanced by TLR9 (cosgrove2024tolllikereceptor7 pages 160-164).
  - MYD88 (HGNC:7562) – adaptor downstream of TLR7/9, required in B cells for autoantibody production and glomerulonephritis in models (conceptual synthesis) (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).
  - CYBB (NOX2; HGNC:2553) – NOX2-generated ROS negatively regulate TLR7 NF-κB signaling; loss exaggerates disease (cosgrove2024tolllikereceptor7 pages 160-164).
- Cytokines/ligands (UniProt/protein classes):
  - IFN-α (type I interferon) – signature pathway with clinical and therapeutic implications (wu2025immunecellaberrations pages 29-30).
  - BAFF (TNFSF13B) – supports B-cell survival and extrafollicular responses; integrated with IFN/Tfh circuits (wu2025immunecellaberrations pages 29-30, zhou2024cartcelltherapy pages 4-4).
  - IL-21 – Tfh-derived; drives B-cell differentiation to plasma cells; Tfh IL-21 blockade ameliorates disease in models (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3, zhou2024cartcelltherapy pages 4-4).
- Autoantibodies: ANA, anti-dsDNA, anti-Sm; anti-C1q associated with nephritis activity; immune complexes underlie type III injury and complement consumption (Feb 2024; https://doi.org/10.3390/molecules29040747) (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4, moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10).
- Complement (components/regulators): C1q/C3/C4 perturbations and complement activation/consumption integrate with immune complexes and NET persistence (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10).

Cell types (CL ontology exemplars)
- Plasmacytoid dendritic cells (pDCs; CL:0000784) – principal IFN-α producers downstream of NET DNA/RNA and TLR9/TLR7 ligation (yuan2024globalresearchtrends pages 10-10, moysidou2024lymphocyteschangetheir pages 18-20).
- B cells (CL:0000236); age-associated B cells (ABCs; CL subclass) – enriched, T-bet/CD11c+ phenotypes; extrafollicular activation; autoantibody production (wu2025immunecellaberrations pages 29-30, cosgrove2024tolllikereceptor7 pages 160-164).
- T follicular helper cells (Tfh; CL:0002038) and T peripheral helper cells (Tph) – IL-21/ICOS/PD-1+ subsets that support autoreactive B cells (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3, zhou2024cartcelltherapy pages 4-4).
- Neutrophils and low-density granulocytes (LDGs; CL:0000096 variant) – heightened NETosis and oxidant stress; impaired NET clearance (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10).
- Cytotoxic/effector T cells – contribute to tissue injury and, in NPSLE, inflammatory milieu and vascular injury (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4, moysidou2024lymphocyteschangetheir pages 18-20).

Anatomical locations/organs (UBERON)
- Kidney/glomerulus (UBERON:0002113/0000071) – immune complex GN, NET/complement interplay (yuan2024globalresearchtrends pages 10-10, moysidou2024lymphocyteschangetheir pages 18-20).
- Skin (UBERON:0002097) – cutaneous lupus; Tfh/Tph and local immune complexes (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3, moysidou2024lymphocyteschangetheir pages 18-20).
- CNS (UBERON:0000955) – neuropsychiatric SLE with vasculopathy/microthrombi/inflammation (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).
- Vasculature (UBERON:0001981) – accelerated vascular damage and atherogenesis in SLE inflammatory milieu (moysidou2024lymphocyteschangetheir pages 18-20).

Chemical entities (CHEBI) and biomarkers
- DNA/RNA in NETs (CHEBI:16991; CHEBI:33697) – ligands for TLR9/TLR7; NET remnants (e.g., MPO-DNA, CitH3) as activity biomarkers in LN (yuan2024globalresearchtrends pages 10-10).
- Cytokines/chemokines: IFN-α, IL-21, CXCL10/CXCL13 as mechanistic biomarkers and stratifiers (wu2025immunecellaberrations pages 29-30).
- Complement split products (e.g., C3/C4 consumption) as activity markers linked to immune complex burden (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4, moysidou2024lymphocyteschangetheir pages 18-20).

GO biological processes (disrupted)
- Type I interferon signaling pathway (GO:0060337): chronic activation across cell types (wu2025immunecellaberrations pages 29-30).
- Toll-like receptor signaling (GO:0002224/GO:0035663): TLR7/9 in B cells/pDCs; MyD88–NF-κB axis (cosgrove2024tolllikereceptor7 pages 160-164, moysidou2024lymphocyteschangetheir pages 18-20).
- B cell activation and differentiation (GO:0042113; GO:0030183): IL-21 and BAFF-driven plasma cell formation; ABC expansion (wu2025immunecellaberrations pages 29-30, shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).
- Neutrophil degranulation and NET formation (GO:0043312; GO:0036349): NETs driving IFN/complement loops (yuan2024globalresearchtrends pages 10-10, moysidou2024lymphocyteschangetheir pages 18-20).
- Complement activation, classical pathway (GO:0006958): immune complex–triggered activation; links to LN (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10).
- Apoptotic cell clearance/efferocytosis (GO:0043277): defects expose nuclear antigens (moysidou2024lymphocyteschangetheir pages 18-20).

Cellular components (where processes occur)
- Endosome/lysosome (GO:0005768/GO:0005764): TLR7/9 nucleic-acid sensing (cosgrove2024tolllikereceptor7 pages 160-164).
- Extracellular region (GO:0005576): NET scaffolds (DNA, histones, granule proteins) and immune complexes (yuan2024globalresearchtrends pages 10-10, moysidou2024lymphocyteschangetheir pages 18-20).
- Plasma membrane/immune synapse (GO:0005886; GO:0001772): Tfh–B cell interactions (ICOS, PD-1) (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).

Disease progression (sequence of events)
- Initiation/triggers: genetic predisposition and environmental insults (infections; repeated innate triggers) lower activation thresholds; repeated infections can “break T cell anergy,” driving autoreactive Tfh development (Jul 2025; https://doi.org/10.3390/cells14141080) (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).
- Amplification: impaired apoptotic/NET debris clearance and early complement pathway insufficiency promote endogenous nucleic-acid presentation to TLR7/9 (B cells, pDCs) → IFN-α programs and BAFF elevation → ABC and Tfh/Tph expansion → extrafollicular and GC autoantibody responses (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10, wu2025immunecellaberrations pages 29-30, shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).
- Tissue injury: immune complex deposition and complement activation; leukocyte infiltration; NET-associated oxidant injury; organ-specific patterns (glomerulonephritis; cutaneous lesions; neurovascular injury) (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10, justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).
- Chronicity and flares: self-sustaining IFN–TLR–B/T feedback loops; persistence of long-lived plasma cells and NET–IFN circuits; fluctuating complement consumption and autoantibody titers (wu2025immunecellaberrations pages 29-30, moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10).

Phenotypic manifestations (HP terms) and mechanistic links
- Lupus nephritis (HP:0000127): immune complexes, complement, NETs (yuan2024globalresearchtrends pages 10-10, moysidou2024lymphocyteschangetheir pages 18-20).
- Cutaneous photosensitive rash (HP:0000988/HP:0000684): immune complex vasculitis in skin; Tfh/Tph involvement (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3, moysidou2024lymphocyteschangetheir pages 18-20).
- Neuropsychiatric features (HP:0100022; HP:0000716): vasculopathy, microthrombi, inflammatory mediators; diagnostic complexity (Feb 2024; https://doi.org/10.3390/molecules29040747) (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).
- Cytopenias (HP:0001873/HP:0001876/HP:0001877): immune-mediated cytopenias consonant with systemic immune complex/complement activation (moysidou2024lymphocyteschangetheir pages 18-20, justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).

Current applications and real-world implementations
- IFN-I pathway therapeutics: Anifrolumab (anti–IFNAR1) efficacy is enriched in patients with high IFN gene signatures, enabling mechanism-based stratification (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (wu2025immunecellaberrations pages 29-30).
- B-cell–directed strategies: BAFF pathway modulation (belimumab) fits B-cell survival/tolerance failure paradigm summarized here; reviews underscore integrating BAFF/IFN biomarkers with therapeutic selection (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (wu2025immunecellaberrations pages 29-30).
- Cellular therapy: Anti-CD19 CAR-T has induced drug-free remissions in early experiences and is rationalized by B-cell centrality in SLE pathogenesis (Dec 2024; https://doi.org/10.3389/fimmu.2024.1476859) (zhou2024cartcelltherapy pages 4-4).
- Biomarkers: NET remnants (e.g., MPO-DNA/CitH3), IFN gene signatures, and chemokines (CXCL10/CXCL13) are candidate activity/response biomarkers tied to the mechanisms above (Jul 2024; https://doi.org/10.1016/j.heliyon.2024.e33350; Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (yuan2024globalresearchtrends pages 10-10, wu2025immunecellaberrations pages 29-30).

Expert opinions and analysis
- Reviews integrating immune cell perturbations argue for moving “from single-target blockade to reconstruction of immune network homeostasis,” cautioning against compensatory remodeling and advocating dynamic immunomonitoring (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (wu2025immunecellaberrations pages 29-30).
- Mechanistic syntheses emphasize the TLR7–driven, B cell–intrinsic nature of disease with regulatory inputs from TLR9 and redox signaling (NOX2), suggesting strategies that antagonize TLR7 while preserving/leveraging TLR9’s counter-regulation (2024 synthesis) (cosgrove2024tolllikereceptor7 pages 160-164).

Relevant statistics and data (recent)
- NETs: impaired degradation associates with LN; mechanistically, LL37/HNP–DNA complexes resist nucleases and activate pDC TLR9 to induce IFN-α (Jul 2024; https://doi.org/10.1016/j.heliyon.2024.e33350) (yuan2024globalresearchtrends pages 10-10).
- IFN biomarker–therapy link: high IFN gene signature correlates with better response to anifrolumab (precise wording per review figure/text) (Jun 2025; https://doi.org/10.1186/s11658-025-00749-z) (wu2025immunecellaberrations pages 29-30).
- B cell–intrinsic TLR7: genetic deletion of Tlr7 in B cells rescues severe disease in specific lupus-prone backgrounds; NOX2 deficiency augments TLR7–NF-κB signaling (experimental findings synthesized in 2024 work) (cosgrove2024tolllikereceptor7 pages 160-164).
- NPSLE: clinicopathologic heterogeneity and absence of a single confirmatory laboratory test underscore the need for multimodal biomarkers (Feb 2024; https://doi.org/10.3390/molecules29040747) (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).

Gene/protein annotations and ontology mappings
- HGNC: TLR7 (HGNC:15631); MYD88 (HGNC:7562); CYBB/NOX2 (HGNC:2553); TNFSF13B/BAFF (HGNC:11929); IL21 (HGNC:6008); IFNA1 family (HGNC:5399).
- GO processes: GO:0060337 (type I IFN signaling); GO:0002224/GO:0035663 (TLR signaling); GO:0030183 (B cell differentiation); GO:0036349 (NET formation); GO:0006958 (complement activation, classical pathway); GO:0043277 (apoptotic cell clearance).
- CL: pDCs (CL:0000784); B cells (CL:0000236) including ABCs; Tfh (CL:0002038); neutrophils (CL:0000096); Tph-like cells.
- UBERON: kidney (UBERON:0002113), glomerulus (UBERON:0000071); skin (UBERON:0002097); brain (UBERON:0000955); vasculature (UBERON:0001981).
- CHEBI: nucleic acids (DNA, CHEBI:16991; RNA, CHEBI:33697); chemokines/cytokines as applicable.
- HP: lupus nephritis (HP:0000127); malar/photosensitive rash (HP:0000988); neuropsychiatric features (HP:0100022); leukopenia/thrombocytopenia/anemia (HP:0001882/HP:0001873/HP:0001876).

Evidence items (PMIDs/DOIs/URLs and dates)
- Moysidou E, et al. Lymphocytes change their phenotype and function in SLE and LN. Int J Mol Sci. Oct 2024. URL: https://doi.org/10.3390/ijms252010905 (moysidou2024lymphocyteschangetheir pages 18-20).
- Yuan Z, et al. Global precision-targeted therapies in SLE; NETs–IFN loop and biomarkers. Heliyon. Jul 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e33350 (yuan2024globalresearchtrends pages 10-10).
- Wu YX, et al. Immune cell aberrations and precision management in SLE; IFN signature–anifrolumab link. Cell Mol Biol Lett. Jun 2025. URL: https://doi.org/10.1186/s11658-025-00749-z (wu2025immunecellaberrations pages 29-30).
- Zhou J, et al. CAR T-cell therapy for SLE: current status and perspectives. Front Immunol. Dec 2024. URL: https://doi.org/10.3389/fimmu.2024.1476859 (zhou2024cartcelltherapy pages 4-4).
- Cosgrove HA. TLR7 in SLE: B cell–intrinsic roles and NOX2 regulation. 2024 research synthesis (cosgrove2024tolllikereceptor7 pages 160-164).
- Shiozawa S. Tfh and infection-triggered models; ICOS/IL-21 involvement. Cells. Jul 2025. URL: https://doi.org/10.3390/cells14141080 (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).
- Justiz-Vaillant AA, et al. NPSLE: molecules, features, treatment; diagnostic caveats. Molecules. Feb 2024. URL: https://doi.org/10.3390/molecules29040747 (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).

Limitations and open questions
- While IFN-I and TLR7/9 biology are strongly implicated, the relative contributions of endosomal sensing versus cytosolic nucleic-acid–sensing (e.g., cGAS–STING) pathways in human SLE subsets remain active areas. Mechanism-guided stratification (IFN gene signatures; NET biomarkers) shows promise but requires prospective standardization (wu2025immunecellaberrations pages 29-30, yuan2024globalresearchtrends pages 10-10).
- The protective–pathogenic duality of TLR9 and context-dependent roles of redox signaling (NOX2) suggest that pathway-selective modulation, not blanket inhibition, may be necessary (cosgrove2024tolllikereceptor7 pages 160-164).

Citations (support for major claims)
- Core mechanisms (IFN axis, TLR7/9, impaired clearance, NETosis/complement, B/T help): (moysidou2024lymphocyteschangetheir pages 18-20, yuan2024globalresearchtrends pages 10-10, cosgrove2024tolllikereceptor7 pages 160-164, shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3).
- IFN signature and therapy response (anifrolumab): (wu2025immunecellaberrations pages 29-30).
- NETs as mechanistic drivers and LN biomarkers: (yuan2024globalresearchtrends pages 10-10).
- CAR-T and B-cell centrality: (zhou2024cartcelltherapy pages 4-4).
- NPSLE pathogenesis complexity and diagnostics: (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4).


References

1. (moysidou2024lymphocyteschangetheir pages 18-20): Eleni Moysidou, Michalis Christodoulou, Georgios Lioulios, Stamatia Stai, Theodoros Karamitsos, Theodoros Dimitroulas, Asimina Fylaktou, and Maria Stangou. Lymphocytes change their phenotype and function in systemic lupus erythematosus and lupus nephritis. International Journal of Molecular Sciences, 25:10905, Oct 2024. URL: https://doi.org/10.3390/ijms252010905, doi:10.3390/ijms252010905. This article has 10 citations and is from a poor quality or predatory journal.

2. (yuan2024globalresearchtrends pages 10-10): Zengze Yuan, Weiqing Zhang, Zhaokai Jin, Yihan Wang, Zhiting Lin, Zhimin Xie, and Xinchang Wang. Global research trends in precision-targeted therapies for systemic lupus erythematosus (2003–2023): a bibliographic study. Heliyon, 10:e33350, Jul 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e33350, doi:10.1016/j.heliyon.2024.e33350. This article has 2 citations and is from a peer-reviewed journal.

3. (wu2025immunecellaberrations pages 29-30): YuXian Wu, Wangzheqi Zhang, Yan Liao, Ting Sun, Yang Liu, and Yaoyang Liu. Immune cell aberrations in systemic lupus erythematosus: navigating the targeted therapies toward precision management. Cellular & Molecular Biology Letters, Jun 2025. URL: https://doi.org/10.1186/s11658-025-00749-z, doi:10.1186/s11658-025-00749-z. This article has 6 citations and is from a peer-reviewed journal.

4. (cosgrove2024tolllikereceptor7 pages 160-164): HA Cosgrove. Toll-like receptor 7 in systemic lupus erythematosus: characterization of cell-intrinsic roles and regulation by nadph oxidase. Unknown journal, 2024.

5. (shiozawa2025pathogenesisofautoimmunitysystemic pages 1-3): Shunichi Shiozawa. Pathogenesis of autoimmunity/systemic lupus erythematosus (sle). Cells, 14:1080, Jul 2025. URL: https://doi.org/10.3390/cells14141080, doi:10.3390/cells14141080. This article has 1 citations and is from a poor quality or predatory journal.

6. (justizvaillant2024neuropsychiatricsystemiclupus pages 2-4): Angel A. Justiz-Vaillant, Darren Gopaul, Sachin Soodeen, Rodolfo Arozarena-Fundora, Odette Arozarena Barbosa, Chandrashehkar Unakal, Reinand Thompson, Bijay Pandit, Srikanth Umakanthan, and Patrick E. Akpaka. Neuropsychiatric systemic lupus erythematosus: molecules involved in its imunopathogenesis, clinical features, and treatment. Molecules, 29:747, Feb 2024. URL: https://doi.org/10.3390/molecules29040747, doi:10.3390/molecules29040747. This article has 58 citations and is from a poor quality or predatory journal.

7. (zhou2024cartcelltherapy pages 4-4): Jincai Zhou, Bixia Lei, Feifei Shi, Xinran Luo, Kai Wu, Yanhong Xu, Yuting Zhang, Rongjiao Liu, Huajing Wang, Joy Zhou, and Xiaowen He. Car t-cell therapy for systemic lupus erythematosus: current status and future perspectives. Frontiers in Immunology, Dec 2024. URL: https://doi.org/10.3389/fimmu.2024.1476859, doi:10.3389/fimmu.2024.1476859. This article has 22 citations and is from a peer-reviewed journal.