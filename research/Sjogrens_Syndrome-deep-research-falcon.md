---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:16.229557'
end_time: '2025-12-18T09:52:36.367805'
duration_seconds: 440.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sjogren's Syndrome
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Sjogren's Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Sjogren's Syndrome**.
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
- **Disease Name:** Sjogren's Syndrome
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Sjogren's Syndrome**.
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
- Disease Name: Sjogren's Syndrome (primary Sjögren’s disease, SjD)
- MONDO ID: MONDO:0005268
- Category: Autoimmune

Pathophysiology description (narrative)
Primary Sjögren’s disease is an autoimmune exocrinopathy driven by epithelial cell–intrinsic innate immune activation and sustained cross-talk with innate and adaptive lymphocytes, culminating in focal lymphocytic sialadenitis, loss of secretory acini, tissue remodeling/fibrosis, systemic features, and an elevated risk of B‑cell lymphoma. Multi-omic and single-cell studies from 2023–2024 converge on a pathogenic axis centered on type I interferon (IFN) signaling and JAK–STAT activation in salivary gland epithelial cells (SGECs) and circulating myeloid cells, with epithelial PRR pathways (TLR7/8/9; cGAS–STING) acting as upstream triggers. This IFN-dominant milieu amplifies BAFF/APRIL-mediated B-cell survival, T follicular helper (Tfh) support, ectopic germinal center/TLS formation, clonal B-cell expansion, and cytotoxic CD8+ tissue-resident memory (Trm) cell–mediated epithelial damage, promoting disease chronicity and complications (Ann Rheum Dis, Aug 2024; Clin Exp Rheumatol, Nov 2024) (zhao2024acomprehensivereview pages 3-4, baldini2024pathogenesisofsjögrens pages 5-7, baldini2024pathogenesisofsjögrens pages 3-4, baldini2024pathogenesisofsjögrens pages 2-3).

Key concepts and definitions with current understanding
- Epithelial cell–intrinsic autoimmunity: SGECs are not passive targets; they upregulate MHC II/co-stimulatory molecules, produce type I IFN and chemokines, and misexpress molecules such as LAMP3 under IFN stimulation, establishing positive feedback with endosomal TLR7 and sustaining the IFN signature (Clin Exp Rheumatol, Nov 2024) (baldini2024pathogenesisofsjögrens pages 3-4, baldini2024pathogenesisofsjögrens pages 2-3).
- Type I IFN signature and JAK–STAT activation: Elevated ISGs in minor salivary glands and blood, correlating with focus score and anti-SSA seropositivity; ex vivo, JAK inhibition normalizes pSTAT and ISGs in SGECs and PBMCs, supporting a targetable pathway (Ann Rheum Dis, Aug 2024; URL: https://doi.org/10.1136/ard-2023-224842) (zhao2024acomprehensivereview pages 3-4).
- PRR pathways: TLR7/8/9 and cGAS–STING link nucleic-acid sensing and mitochondrial/ER stress to type I IFN production in SGECs and pDCs; these axes are implicated in initiating and sustaining glandular inflammation (Clin Exp Rheumatol, Sep 2024; Front Immunol, Jul 2024) (qi2024advancesincellular pages 2-4, zhao2024acomprehensivereview pages 3-4).
- Adaptive immune dysregulation: Tfh–B cell synapses drive local affinity maturation in TLS; BAFF/APRIL signaling sustains plasmablast/plasma cell survival; gland-infiltrating BCR repertoires display clonal expansion and repertoire biases associated with clinical activity (Arthritis Res Ther, Mar 2024) (qi2024advancesincellular pages 2-4).
- Cytotoxic CD8+ Trm: Spatial and functional studies show expanded CD8+CD103+ Trm expressing GZMB/GZMK and IFN-γ, localized within inflammatory foci and contributing to epithelial injury; anti‑CD103 blockade reduces Trm and improves salivary flow in models (Ann Rheum Dis, Oct 2024) (zhao2024acomprehensivereview pages 3-4).
- Genetics/epigenetics: Strong HLA class II associations in anti‑SSA+ SjD, and non‑HLA loci (IRF5, STAT4) implicate IFN and antigen presentation pathways; ISGs show DNA hypomethylation in immune and epithelial cells, correlating with severity (Nat Rev Rheumatol, Mar 2023; Front Immunol, Mar 2024; Heliyon, Sep 2024) (zhao2024acomprehensivereview pages 3-4, baldini2024pathogenesisofsjögrens pages 2-3).

Recent developments (2023–2024) and latest research
- One‑year pathogenesis review 2024 synthesizes new single-cell/spatial evidence: SGEC LAMP3/IFN loops, mitochondrial dysfunction, m6A-dependent IFN control, myeloid skewing (NLRP3+ clusters), and cytotoxic GZMK+ CD8+ T-cell–driven acinar loss; links to pre‑lymphomatous lesions and emergence of MALT lymphoma clones (Clin Exp Rheumatol, Nov 2024; https://doi.org/10.55563/clinexprheumatol/i8iszc) (baldini2024pathogenesisofsjögrens pages 5-7, baldini2024pathogenesisofsjögrens pages 3-4, baldini2024pathogenesisofsjögrens pages 2-3).
- Interventional immune signaling: Human tissue and ex vivo work demonstrate that JAK inhibition corrects IFN–JAK–STAT activity in glands and PBMCs, prompting a phase Ib/IIa trial of tofacitinib (Ann Rheum Dis, Aug 2024; https://doi.org/10.1136/ard-2023-224842) (zhao2024acomprehensivereview pages 3-4).
- BCR repertoire and single-cell atlases: Paired scRNA/BCR-seq identifies gland-specific BCR expansions, altered isotype usage (reduced IgA2), and light-chain skewing correlating with disease activity (Arthritis Res Ther, Mar 2024; https://doi.org/10.1186/s13075-024-03283-z). Single-cell profiles (iScience, Oct 2023; J Transl Autoimmunity, Dec 2024) refine immune–stromal heterogeneity in labial glands (qi2024advancesincellular pages 2-4).
- PRR specialization: TLR7-focused review highlights endosomal ssRNA sensing in pDCs and SGECs with MyD88-dependent induction of IFN-I, integrating with the IFN signature observed in SjD (Clin Exp Rheumatol, Sep 2024; https://doi.org/10.55563/clinexprheumatol/cmmkod) (qi2024advancesincellular pages 2-4).
- Multi-omics epigenetics: Integrative MR suggests causal interplay between IFN-signaling gene expression, DNA methylation, and inflammatory cytokines in SjD, nominating SH2B3, LGALS9, CD40, GRB2, DTX3L in blood and APOBEC3G, IFI27L2, TMEM50B, SH2B3 in gland tissue as IFN-associated causal genes (May 2024; https://doi.org/10.21203/rs.3.rs-4371628/v1) (he2024interplayofinterferon pages 18-21).

Current applications and real-world implementations
- Mechanism-based therapy: JAK inhibitors to modulate glandular IFN–JAK–STAT signaling; B cell–directed approaches (rituximab strategies and BAFF/APRIL-targeted agents) for hyperactive B-cell states and TLS-positive disease, with biomarker guidance by IFN signatures and BCR features (Ann Rheum Dis, 2024; Clin Exp Rheumatol, 2024) (zhao2024acomprehensivereview pages 3-4, baldini2024pathogenesisofsjögrens pages 5-7).
- Biomarker-guided stratification: IFN signatures in glands and blood, chemokines (CXCL10, CXCL13), BAFF levels, and BCR repertoire metrics associate with activity, serostatus, and lymphoma risk; DNA methylation of ISGs in salivary glands reflects severity (Front Immunol, 2024; Heliyon, 2024) (qi2024advancesincellular pages 2-4, zhao2024acomprehensivereview pages 3-4).

Expert opinions and analysis from authoritative sources
- “The innate immune system plays a crucial role in initiation… amplification requires continual interaction between innate and adaptive immunity” and ectopic GC-like structures are “critically involved in autoreactive B cell activation… associated with progression towards B cell lymphomas” (Clin Exp Rheumatol, Nov 2024) (baldini2024pathogenesisofsjögrens pages 5-7).
- Human tissue data show that “activated JAK–STAT pathway in SjD MSGs… elevated ISG expression associated with focus scores and anti-SSA positivity” and “JAKi normalises this aberrant signalling at the tissue level and in PBMCs” (Ann Rheum Dis, Aug 2024) (zhao2024acomprehensivereview pages 3-4).

Relevant statistics and data from recent studies
- Gland and blood IFN–JAK–STAT activation correlates with histology and serology; ex vivo JAKi normalized basal pSTAT levels in SjD-derived SGECs and PBMCs and reduced IFN-β exaggerated responses in SGECs without cytotoxicity (Ann Rheum Dis, 2024) (zhao2024acomprehensivereview pages 3-4).
- BCR repertoire work demonstrated decreased IgA2 usage in glandular B cells and a positive correlation between κ/λ light chain usage and clinical activity (Arthritis Res Ther, 2024) (qi2024advancesincellular pages 2-4).
- Spatial/single-cell analyses identified CD8+CD103+ Trm accumulation with GZMB/GZMK/IFN-γ expression; anti‑CD103 intervention reduced Trm, glandular damage and improved flow in the ESS model (Ann Rheum Dis, 2024) (zhao2024acomprehensivereview pages 3-4).

1. Core Pathophysiology
- Primary mechanisms: epithelial PRR activation (TLR7/8/9; cGAS–STING), IFN–JAK–STAT signaling, BAFF/APRIL-driven B-cell survival, Tfh-mediated help, TLS/ectopic GCs, cytotoxic CD8+ Trm-mediated epithelial injury, and epigenetic ISG hypomethylation (Clin Exp Rheumatol, 2024; Front Immunol, 2024; Ann Rheum Dis, 2024) (qi2024advancesincellular pages 2-4, baldini2024pathogenesisofsjögrens pages 5-7, baldini2024pathogenesisofsjögrens pages 3-4, baldini2024pathogenesisofsjögrens pages 2-3, zhao2024acomprehensivereview pages 3-4).
- Dysregulated pathways: IFN-α/β signaling; TLR7/8/9–MyD88; cGAS–STING–TBK1–IRF3; BAFF/APRIL–BAFF-R/TACI/BCMA; Tfh–IL-21–BCR; JAK–STAT; inflammasome/NLRP3; EMT/TGF‑β–SMAD; chemokine axes (CXCL10/CXCL13) (Front Immunol, 2024; Heliyon, 2024) (qi2024advancesincellular pages 2-4, zhao2024acomprehensivereview pages 3-4).
- Affected cellular processes: antigen presentation by SGECs, ISG transcriptional programs, BCR diversification and clonal expansion, cytotoxic granule pathways in Trm, ER/mitochondrial stress, EMT and fibrosis (Clin Exp Rheumatol, 2024; Front Immunol, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, qi2024advancesincellular pages 2-4).

2. Key Molecular Players
- Genes/Proteins (HGNC): IRF5; STAT4; HLA-DQA1/DQB1; TNFSF13B (BAFF); TNFSF13 (APRIL); TNFRSF13C (BAFF-R); TNFRSF13B (TACI); TNFRSF17 (BCMA); CXCL10; CXCL13; IL21; LAMP3 (Clin Exp Rheumatol, 2024; Heliyon, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, zhao2024acomprehensivereview pages 3-4).
- Chemical Entities (CHEBI/drug class): JAK inhibitors (class); BAFF/APRIL inhibitors (class) (Ann Rheum Dis, 2024) (zhao2024acomprehensivereview pages 3-4).
- Cell Types (CL): salivary gland epithelial cells; plasmacytoid dendritic cells; monocytes/macrophages; Tfh cells; CD8+ Trm cells; B cells/plasmablasts/plasma cells (Clin Exp Rheumatol, 2024; Front Immunol, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, qi2024advancesincellular pages 2-4).
- Anatomical Locations (UBERON): labial and parotid salivary glands; lacrimal gland (Heliyon, 2024) (zhao2024acomprehensivereview pages 3-4).

3. Biological Processes (GO terms)
- GO: type I interferon signaling pathway; GO: toll-like receptor signaling pathway (TLR7/8/9); GO: cGAS–STING DNA sensing; GO: B cell activation; GO: germinal center formation; GO: T cell activation; GO: JAK–STAT cascade; GO: epithelial to mesenchymal transition; GO: inflammatory response; GO: antigen processing and presentation via MHC class II (Front Immunol, 2024; Clin Exp Rheumatol, 2024) (qi2024advancesincellular pages 2-4, baldini2024pathogenesisofsjögrens pages 5-7).

4. Cellular Components
- Key cellular locales: endosomes (TLR7/8/9), ER and mitochondria (stress, ER–mitochondrial crosstalk), cytosol (cGAS–STING), plasma membrane (BAFF-R/TACI/BCMA), extracellular space (cytokines/chemokines), epithelial tight junctions and basal membrane interfaces (Heliyon, 2024; Clin Exp Rheumatol, 2024) (zhao2024acomprehensivereview pages 3-4, baldini2024pathogenesisofsjögrens pages 3-4).

5. Disease Progression
- Sequence of events: epithelial PRR/IFN activation → chemokine release (CXCL10/CXCL13), pDC/myeloid recruitment → IFN–JAK–STAT amplification → B-cell hyperactivity (BAFF/APRIL), Tfh help → TLS/ectopic GC formation, BCR clonal expansion and plasma cell survival → cytotoxic CD8+ Trm–mediated acinar injury → chronic sialadenitis with fibrosis/EMT → systemic features; in a subset, pre-lymphomatous lymphoepithelial lesions and MALT lymphoma (Clin Exp Rheumatol, 2024; Front Immunol, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, qi2024advancesincellular pages 2-4).
- Stages/phases: early epithelial/IFN phase; adaptive/TLS expansion phase; remodeling/fibrotic phase; lymphoma risk phase in TLS-high, RF+ clones (Clin Exp Rheumatol, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, baldini2024pathogenesisofsjögrens pages 3-4).

6. Phenotypic Manifestations
- Clinical phenotypes (HP): keratoconjunctivitis sicca; xerostomia; salivary gland enlargement; fatigue; arthralgia; extraglandular involvement (interstitial lung disease, neuropathy, renal tubular acidosis); increased risk of B‑cell lymphoma (Heliyon, 2024; Clin Exp Rheumatol, 2024) (zhao2024acomprehensivereview pages 3-4, baldini2024pathogenesisofsjögrens pages 5-7).
- Mechanistic links: sicca arises from acinar/ductal injury by CD8+ Trm cytotoxicity and IFN/chemokine-driven inflammation; hypergammaglobulinemia and autoantibodies (anti‑SSA/SSB) reflect Tfh–BAFF/APRIL–B cell activation; systemic features correlate with systemic IFN signatures; lymphoma risk associates with TLS, parotid lymphoepithelial lesions, RF+ clonotypes and BCR hypermutation (Clin Exp Rheumatol, 2024; Arthritis Res Ther, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, qi2024advancesincellular pages 2-4).

Gene/protein annotations with ontology terms (HGNC) and evidence
- IRF5 (HGNC:6117): innate IFN pathway regulator; risk locus in SjD (Nat Rev Rheumatol, Mar 2023) (baldini2024pathogenesisofsjögrens pages 2-3).
- STAT4 (HGNC:11364): downstream of cytokine receptors; SjD risk locus; ties to Th1/Tfh programs (Nat Rev Rheumatol, 2023) (baldini2024pathogenesisofsjögrens pages 2-3).
- HLA-DQA1/HLA-DQB1 (HGNC): antigen presentation; strongest in anti‑SSA+ patients (Heliyon, Sep 2024) (zhao2024acomprehensivereview pages 3-4).
- TNFSF13B (BAFF), TNFSF13 (APRIL), TNFRSF13C (BAFF-R), TNFRSF13B (TACI), TNFRSF17 (BCMA): B‑cell survival axis in glands (Front Immunol, Jul 2024) (qi2024advancesincellular pages 2-4).
- LAMP3: IFN-inducible epithelial molecule; misexpression amplifies TLR7/IFN loops (Clin Exp Rheumatol, Nov 2024) (baldini2024pathogenesisofsjögrens pages 3-4).
- CXCL10/CXCL13/IL21: chemokines/cytokines recruiting/educating T and B cells in TLS (Heliyon, Sep 2024) (zhao2024acomprehensivereview pages 3-4).

Phenotype associations (HP terms) and evidence
- HP:0001098 Keratoconjunctivitis sicca; HP:0000217 Xerostomia; HP:0001396 Fatigue; HP:0001382 Arthralgia; HP:0002664 Lymphoma (risk increased); HP:0006530 Interstitial lung disease; HP:0002093 Peripheral neuropathy (Heliyon, 2024; Clin Exp Rheumatol, 2024) (zhao2024acomprehensivereview pages 3-4, baldini2024pathogenesisofsjögrens pages 5-7).

Cell type involvement (CL terms) and evidence
- CL: salivary gland epithelial cell; CL: plasmacytoid dendritic cell; CL: monocyte/macrophage; CL: T follicular helper cell; CL: CD8+ tissue-resident memory T cell; CL: B cell/plasma cell (Clin Exp Rheumatol, 2024; Front Immunol, 2024; Ann Rheum Dis, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, qi2024advancesincellular pages 2-4, zhao2024acomprehensivereview pages 3-4).

Anatomical locations (UBERON terms) and evidence
- UBERON:0001044 Salivary gland (labial, parotid); UBERON:0001811 Lacrimal gland (Heliyon, Sep 2024) (zhao2024acomprehensivereview pages 3-4).

Chemical entities (CHEBI) and evidence
- CHEBI: class “Janus kinase inhibitor” (JAK inhibitor) — normalizes IFN–JAK–STAT activity ex vivo (Ann Rheum Dis, 2024) (zhao2024acomprehensivereview pages 3-4).
- BAFF/APRIL inhibitors (biologic class) — rationale from glandular B-cell survival axis (Front Immunol, 2024) (qi2024advancesincellular pages 2-4).

Selected evidence items with URLs and publication dates
- Gupta et al., Annals of the Rheumatic Diseases, Aug 2024: human gland and PBMC IFN–JAK–STAT activation corrected by JAK inhibitors; DOI: 10.1136/ard-2023-224842; URL: https://doi.org/10.1136/ard-2023-224842 (zhao2024acomprehensivereview pages 3-4).
- Baldini et al., Clinical and Experimental Rheumatology, Nov 2024: one‑year pathogenesis review detailing epithelial IFN/LAMP3, cytotoxic CD8+ T-cell injury, TLS/lymphoma links; DOI: 10.55563/clinexprheumatol/i8iszc; URL: https://doi.org/10.55563/clinexprheumatol/i8iszc (baldini2024pathogenesisofsjögrens pages 5-7, baldini2024pathogenesisofsjögrens pages 3-4, baldini2024pathogenesisofsjögrens pages 2-3).
- Qi et al., Frontiers in Immunology, Jul 2024: cellular/molecular pathways of salivary gland damage (TLRs, BAFF/APRIL, EMT/EMT, inflammasome); DOI: 10.3389/fimmu.2024.1405126; URL: https://doi.org/10.3389/fimmu.2024.1405126 (qi2024advancesincellular pages 2-4).
- Chang et al., Arthritis Research & Therapy, Mar 2024: gland BCR repertoire features linked to clinical activity; DOI: 10.1186/s13075-024-03283-z; URL: https://doi.org/10.1186/s13075-024-03283-z (qi2024advancesincellular pages 2-4).
- Song & Zhou, Clinical and Experimental Rheumatology, Sep 2024: TLR7 pathway in pSS; DOI: 10.55563/clinexprheumatol/cmmkod; URL: https://doi.org/10.55563/clinexprheumatol/cmmkod (qi2024advancesincellular pages 2-4).
- He et al., multi-omics MR, May 2024: IFN–DNA methylation–cytokine interactions; URL: https://doi.org/10.21203/rs.3.rs-4371628/v1 (he2024interplayofinterferon pages 18-21).
- Zhao et al., Heliyon, Sep 2024: genetics, signaling pathways, clinical course; DOI: 10.1016/j.heliyon.2024.e36220; URL: https://doi.org/10.1016/j.heliyon.2024.e36220 (zhao2024acomprehensivereview pages 3-4).

Embedded summary artifact
| Category | Item (ontology / symbol) | Mechanistic role (1–2 lines) | Notes / applications |
|---|---|---|---|
| Innate cytokine signaling | Type I IFN — JAK-STAT (GO: type I interferon signaling pathway) | Amplifies ISG expression via JAK-STAT in epithelial & immune cells, driving chronic inflammation. | Biomarker (IFN signature); targetable with JAK inhibitors (normalises ISG expression). |
| Pattern recognition receptors | TLR7 / TLR8 / TLR9 (GO: toll-like receptor signaling) | Endosomal sensing of ssRNA/DNA in pDCs/SGECs → MyD88-dependent type I IFN and proinflammatory cytokines. | Linked to autoantibody-driven activation; TLR7 gain-of-function associated with disease. |
| Cytosolic DNA sensing | cGAS–STING (GO: cGAS-STING pathway) | Detects cytosolic DNA → TBK1/IRF3 activation and type I IFN production; implicated in SGEC stress responses. | Possible therapeutic target (STING inhibitors); connects metabolic/mitochondrial stress to IFN. |
| B‑cell survival axis | BAFF / APRIL — TNFSF13B / TNFSF13; receptors TNFRSF13C (BAFF-R), TNFRSF13B (TACI), TNFRSF17 (BCMA) | Promotes B-cell survival, plasmablast/plasma cell maintenance and class switching in glands. | Rationale for BAFF/APRIL inhibitors (reduce autoantibodies, relapse after B-cell depletion). |
| Helper T cells | T follicular helper (CL: Tfh cell) | Provide IL-21/IL-4 help to B cells, support ectopic GC formation and affinity maturation. | Tfh frequency correlates with autoantibody production; therapeutic interest (blockade of T–B interactions). |
| Innate plasmacytoid cells | Plasmacytoid dendritic cell (CL: pDC) | Major source of IFN-α in response to nucleic-acid containing immune complexes, initiating IFN signature. | pDC-targeting strategies may dampen systemic IFN-driven pathology. |
| Myeloid effectors | Monocytes / Macrophages (CL: monocyte, macrophage) | Produce IL-1β/TNF and chemokines (CCL3, CX3CL1) that recruit/activate lymphocytes and shape TLS formation. | Myeloid skewing linked to gland inflammation and fibrosis; potential biomarker axes. |
| Cytotoxic residence | CD8+ tissue-resident memory T cell (CL: CD8+ Trm) | Local cytotoxicity (GZMB/GZMK, IFN-γ) causing acinar/ductal cell injury and loss of secretory cells. | CD103 blockade reduced gland damage in models — therapeutic proof-of-concept. |
| Target tissue | Salivary gland epithelial cells (CL: salivary gland epithelial cell) | Active participants: antigen presentation (MHC II), PRR signaling, cytokine/chemokine secretion and IFN production. | SGECs drive local immune recruitment and may undergo EMT/ferroptosis; target for tissue-protective therapies. |
| Adaptive receptor features | BCR repertoire alterations (concept) | Gland-infiltrating B cells show clonal expansion, somatic hypermutation and biased isotype/chain usage. | BCR features associate with clinical activity and lymphoma risk; useful for molecular stratification. |
| Lymphoid architecture | Ectopic germinal centers / tertiary lymphoid structures (TLS) (concept) | Sites of local affinity maturation and long-lived plasma cell generation within glands. | TLS presence correlates with higher lymphoma risk; target for B-cell–directed interventions. |
| Tissue remodeling | Fibrosis / EMT (GO: epithelial to mesenchymal transition) | Chronic inflammation induces TGF-β/SMAD-driven EMT and ECM deposition, leading to irreversible gland damage. | Explains progressive loss of function; antifibrotic strategies may preserve gland structure. |
| Histopathology | Lymphoepithelial lesions (concept) | Epithelial hyperplasia with dense lymphoid infiltration, often pre-lymphomatous in parotid glands. | Clinicopathologic marker for severe gland involvement and lymphoma surveillance. |
| Genetic susceptibility | IRF5, STAT4, HLA class II (HGNC: IRF5, STAT4, HLA-DQA1/HLA-DQB1) | Modulate innate IFN responses, antigen presentation and adaptive immunity; HLA associations stronger in anti-SSA+ cases. | Inform risk stratification and mechanistic subtyping; link to IFN-driven endotypes. |
| Epigenetics | DNA hypomethylation of ISGs (concept) | Demethylation of IFN-regulated loci increases ISG expression in immune and epithelial cells. | Epigenetic markers correlate with severity; potential for biomarker/therapeutic epigenetic modulation. |
| Chemokines / cytokines | CXCL13, CXCL10, IL21, BAFF (HGNC: CXCL13, CXCL10, IL21; TNFSF13B) | CXCL13/CXCL10 recruit B/T cells and drive TLS; IL-21 mediates Tfh help; BAFF sustains B cells. | Serum/tissue levels serve as activity biomarkers; targets for biologic therapies. |
| Anatomy | Labial salivary gland; parotid salivary gland; lacrimal gland (UBERON: salivary gland, lacrimal gland) | Primary sites of lymphocytic infiltration, acinar loss and TLS formation leading to sicca symptoms. | Biopsy sites and imaging targets for diagnosis and spatial profiling. |
| Therapeutics (small molecules / biologics) | JAK inhibitors (CHEBI: JAK inhibitor class); BAFF/APRIL inhibitors (drug class) | JAKi block IFN-JAK-STAT signaling in glands/PBMCs; BAFF/APRIL inhibitors reduce B-cell survival and autoantibody production. | Supported by ex vivo tissue studies and clinical trials; guide mechanism-based therapy selection. |


*Table: Concise, citable map linking key pathways, cells, molecules and targets in primary Sjögren's syndrome pathogenesis; compiled from recent mechanistic reviews and multi-omic studies (qi2024advancesincellular pages 2-4, baldini2024pathogenesisofsjögrens pages 5-7, he2024interplayofinterferon pages 18-21).*

Limitations and open questions
- The precise initiating triggers (viral vs sterile nucleic-acid stress; epithelial metabolic/m6A defects) and their contribution across serostatus-defined subtypes remain under active investigation. The degree to which targeting epithelial-intrinsic PRR/IFN pathways (e.g., STING) alters long-term glandular outcomes is not yet established in clinical trials (Clin Exp Rheumatol, 2024; Ann Rheum Dis, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, zhao2024acomprehensivereview pages 3-4).

Overall synthesis
A coherent mechanistic model links epithelial PRR/IFN activation and JAK–STAT signaling to the recruitment and licensing of innate and adaptive immunity, with BAFF/APRIL and Tfh orchestrating TLS-dependent B-cell maturation and CD8+ Trm executing cytotoxic damage. Genetic/epigenetic predisposition tunes these responses, while chronic inflammation drives EMT/fibrosis and predisposes to lymphoma in a subset. These insights enable IFN- and B cell–targeted strategies and support molecular endotyping for precision therapy (Clin Exp Rheumatol, 2024; Ann Rheum Dis, 2024; Front Immunol, 2024) (baldini2024pathogenesisofsjögrens pages 5-7, zhao2024acomprehensivereview pages 3-4, qi2024advancesincellular pages 2-4).

References

1. (zhao2024acomprehensivereview pages 3-4): Ting Zhao, Runrun Zhang, Zhaofu Li, Dongdong Qin, and Xinchang Wang. A comprehensive review of sjögren's syndrome: classification criteria, risk factors, and signaling pathways. Heliyon, 10:e36220, Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e36220, doi:10.1016/j.heliyon.2024.e36220. This article has 8 citations and is from a peer-reviewed journal.

2. (baldini2024pathogenesisofsjögrens pages 5-7): Chiara Baldini, Loukas G. Chatzis, Giovanni Fulvio, Gaetano La Rocca, Elena Pontarini, and Michele Bombardieri. Pathogenesis of sjögren's disease: one year in review 2024. Clinical and experimental rheumatology, Nov 2024. URL: https://doi.org/10.55563/clinexprheumatol/i8iszc, doi:10.55563/clinexprheumatol/i8iszc. This article has 15 citations and is from a peer-reviewed journal.

3. (baldini2024pathogenesisofsjögrens pages 3-4): Chiara Baldini, Loukas G. Chatzis, Giovanni Fulvio, Gaetano La Rocca, Elena Pontarini, and Michele Bombardieri. Pathogenesis of sjögren's disease: one year in review 2024. Clinical and experimental rheumatology, Nov 2024. URL: https://doi.org/10.55563/clinexprheumatol/i8iszc, doi:10.55563/clinexprheumatol/i8iszc. This article has 15 citations and is from a peer-reviewed journal.

4. (baldini2024pathogenesisofsjögrens pages 2-3): Chiara Baldini, Loukas G. Chatzis, Giovanni Fulvio, Gaetano La Rocca, Elena Pontarini, and Michele Bombardieri. Pathogenesis of sjögren's disease: one year in review 2024. Clinical and experimental rheumatology, Nov 2024. URL: https://doi.org/10.55563/clinexprheumatol/i8iszc, doi:10.55563/clinexprheumatol/i8iszc. This article has 15 citations and is from a peer-reviewed journal.

5. (qi2024advancesincellular pages 2-4): Wenxia Qi, Jiexiang Tian, Gang Wang, Yanfeng Yan, Tao Wang, Yong Wei, Zhandong Wang, Guohua Zhang, Yuanyuan Zhang, and Jia Wang. Advances in cellular and molecular pathways of salivary gland damage in sjögren’s syndrome. Frontiers in Immunology, Jul 2024. URL: https://doi.org/10.3389/fimmu.2024.1405126, doi:10.3389/fimmu.2024.1405126. This article has 13 citations and is from a peer-reviewed journal.

6. (he2024interplayofinterferon pages 18-21): Jiale He, Fengtao Pang, Xueyan Shan, Ruihua Liu, Zilin Guo, Minlan Ye, Wenjing Liu, Kefei Yang, Xinyao Zhou, and Xiaopo Tang. Interplay of interferon signalling gene expression, dna methylation, and inflammatory cytokines in sjögren’s syndrome: a multi-omics mendelian randomization study. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4371628/v1, doi:10.21203/rs.3.rs-4371628/v1.