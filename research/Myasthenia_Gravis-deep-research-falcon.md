---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:50.016696'
end_time: '2025-12-18T09:54:07.915621'
duration_seconds: 497.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myasthenia Gravis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Myasthenia Gravis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myasthenia Gravis**.
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
- **Disease Name:** Myasthenia Gravis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Myasthenia Gravis**.
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
- Disease Name: Myasthenia Gravis (MG)
- MONDO ID: MONDO:0005041
- Category: Autoimmune

Pathophysiology description
Myasthenia gravis is a prototypic antibody-mediated autoimmune synaptopathy of the neuromuscular junction (NMJ). In AChR-antibody–positive MG (the most common subtype), IgG1/IgG3 antibodies drive three principal mechanisms: (i) classical complement pathway activation culminating in membrane attack complex (MAC)–mediated injury with loss of postsynaptic folds and AChR-rich membrane, (ii) antigenic modulation with cross-linking–induced endocytosis and degradation of AChR, and (iii) direct functional blockade of the acetylcholine binding site. These mechanisms reduce the safety factor for neuromuscular transmission and produce fatigable weakness (Journal of Clinical Investigation, Jun 2024, https://doi.org/10.1172/jci179742). Complement C5 inhibition clinically validates the centrality of MAC injury in AChR-MG (eculizumab, ravulizumab, zilucoplan) (JCI 2024; Expert Rev Clin Immunol 2022, https://doi.org/10.1080/1744666X.2022.2082946). MuSK-MG is mechanistically distinct: pathogenic antibodies are predominantly IgG4, functionally monovalent after Fab-arm exchange, and block LRP4–MuSK interaction and downstream phosphorylation cascades required for AChR clustering; complement fixation is minimal in MuSK-MG. LRP4 antibodies can activate complement (typically IgG1) and also interfere with agrin–LRP4 signaling, disrupting AChR clustering (Eye, May 2024, https://doi.org/10.1038/s41433-024-03133-x; Cells, Mar 2024, https://doi.org/10.3390/cells13060556). Seronegative MG (by routine assays) is heterogeneous and includes patients with low-affinity/clustered AChR antibodies, LRP4/agrin antibodies, or as-yet-undetected reactivities (JCI 2024). 

Thymic autoimmunity is characteristic of early-onset AChR-MG, with thymic follicular hyperplasia, ectopic germinal centers, and dysregulated T–B collaboration (increased T follicular helper cells, reduced Treg function) that foster intrathymic affinity maturation and long-lived autoantibody responses. Type I interferon–rich signatures, CXCL13, and BAFF pathways are implicated in perpetuating the thymic autoimmune niche. Thymoma-associated MG has distinct serology and autoantibody spectra, whereas MuSK-MG generally lacks prominent thymic pathology (JCI 2024; Frontiers in Immunology, Jan 2023, https://doi.org/10.3389/fimmu.2023.1110499; Frontiers in Neurology, Aug 2023, https://doi.org/10.3389/fneur.2023.1229112). 

Therapeutic mechanism-of-action (MOA) validation underscores these pathways: terminal complement C5 inhibitors reduce MAC injury and improve strength in refractory AChR-MG, while FcRn antagonists accelerate pathogenic IgG catabolism, lowering circulating autoantibody levels and improving outcomes across antibody-defined subtypes; both approaches have translated to approved therapies (Frontiers in Neurology 2023; JCI 2024; Expert Rev Clin Immunol 2022). (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2, bhandari2023fcrnreceptorantagonists pages 1-2, keller2022fcreceptortargetedtherapies pages 2-3)

Key concepts and definitions
- AChR-MG: IgG1/IgG3-mediated disease marked by complement activation, AChR internalization, and receptor blockade at the postsynaptic membrane. (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2)
- MuSK-MG: IgG4-predominant autoimmunity with blocking of LRP4–MuSK signaling and impaired AChR clustering; minimal complement activation; often responds well to B cell depletion. (dziadkowiak2024muskmyastheniagravis—potential pages 13-14, jacob2024treatingmyastheniagravis pages 1-2)
- LRP4-MG: Antibodies disrupt agrin–LRP4–MuSK pathway and can fix complement; may coexist with other autoantibodies. (jacob2024treatingmyastheniagravis pages 1-2)
- Seronegative MG: Heterogeneous; includes low-affinity clustered AChR antibodies or antibodies to LRP4/agrin not detected by standard assays. (kaminski2024myastheniagravisthe pages 2-4)
- FcRn: Endosomal receptor that rescues IgG from lysosomal degradation; therapeutic blockade reduces pathogenic IgG burden systemically. (bhandari2023fcrnreceptorantagonists pages 1-2)

Recent developments and latest research (2023–2024)
- Genetics: A large 2024 GWAS/meta-analysis identified multiple genome-wide significant loci, clarified HLA class II influences, and demonstrated polygenic risk prediction in MG, with distinct early- vs late-onset associations (Nature Communications, Nov 2024, https://doi.org/10.1038/s41467-024-53595-6). Clinical overviews also emphasize PTPN22 and CTLA4 associations across subgroups (JCI 2024). (kaminski2024myastheniagravisthe pages 2-4)
- Epidemiology: Contemporary population-based studies show increasing incidence and prevalence in high-income countries, with strong age and sex effects. Nordic registry data (JNNP, Mar 2024) and US claims analyses (Frontiers in Neurology, Feb 2024) quantify rising prevalence and stable to modestly rising incidence, particularly in older adults. (, )
- ncRNA/epigenetics and inflammation: Reviews highlight altered microRNA profiles in thymus and blood, type I interferon signaling, BAFF/Tfh axes, and inflammatory cytokine networks contributing to MG pathogenesis and heterogeneity, supporting biomarker-guided and epigenetic-targeting strategies (Frontiers in Immunology, Jan 2023; Eye, 2024). (huda2023inflammationandautoimmune pages 1-2, jacob2024treatingmyastheniagravis pages 1-2)
- Therapeutics: FcRn inhibitors (efgartigimod, rozanolixizumab) and complement C5 inhibitors (eculizumab, ravulizumab, zilucoplan) consolidate mechanism-based treatment and enable earlier, targeted intervention strategies (Frontiers in Neurology 2023; Expert Rev Clin Immunol 2022; JCI 2024). (bhandari2023fcrnreceptorantagonists pages 1-2, keller2022fcreceptortargetedtherapies pages 2-3, kaminski2024myastheniagravisthe pages 2-4)

Current applications and real-world implementations
- Complement inhibition (C5): Reduces MAC formation at the NMJ, directly addressing complement-mediated postsynaptic injury validated in AChR-MG. Clinical adoption for refractory generalized AChR-MG has been established (Expert Rev Clin Immunol 2022). (keller2022fcreceptortargetedtherapies pages 2-3)
- FcRn antagonism: Lowers total IgG including pathogenic subclasses and improves clinical scores across subtypes; approved agents are increasingly used in cycles with monitoring of symptom trajectories (Frontiers in Neurology 2023). (bhandari2023fcrnreceptorantagonists pages 1-2)
- B cell–directed therapy: Particularly impactful in MuSK-MG, aligning with IgG4/plasmablast biology and limited complement involvement (Cells 2024; Eye 2024). (dziadkowiak2024muskmyastheniagravis—potential pages 13-14, jacob2024treatingmyastheniagravis pages 1-2)

Expert opinions and analysis (authoritative sources)
- Kaminski et al. (JCI, 2024) synthesize mechanistic, genetic, and therapeutic advances, reinforcing three canonical AChR-MG mechanisms at the NMJ, detailing subtype distinctions, and highlighting precision therapeutics (https://doi.org/10.1172/jci179742). (kaminski2024myastheniagravisthe pages 2-4, kaminski2024myastheniagravisthe pages 10-10)
- Dalakas (Expert Rev Clin Immunol, 2022) argues complement and FcRn pathways are central, with clinical trial success translating to practice for refractory MG (https://doi.org/10.1080/1744666X.2022.2082946). (keller2022fcreceptortargetedtherapies pages 2-3)
- Bhandari & Bril (Frontiers in Neurology, 2023) review FcRn biology/PK-PD and MG indications, supporting real-world utilization and safety (https://doi.org/10.3389/fneur.2023.1229112). (bhandari2023fcrnreceptorantagonists pages 1-2)

Relevant statistics and data (recent studies)
- GWAS/meta-analysis (Nature Communications, 2024): 5708 MG cases/432,028 controls plus replication; 11 loci; PRS explained ~4.2% variance, with HLA signals showing inverse effects by age at onset (Nov 2024) (https://doi.org/10.1038/s41467-024-53595-6). (kaminski2024myastheniagravisthe pages 2-4)
- Nordic epidemiology (JNNP, 2024): Incidence 1.3–1.7 per 100,000; prevalence ~18.6–23.4 per 100,000; standardized mortality ratios 1.20–1.32; rising prevalence over 2000–2020 (Mar 2024, https://doi.org/10.1136/jnnp-2023-333097). ()
- US epidemiology (Frontiers in Neurology, 2024): Age- and sex-standardized incidence ~68.5/million person-years (commercial/Medicare); prevalence ~316/million (2017), estimating ~82,715 adults living with MG in 2021 (Feb 2024, https://doi.org/10.3389/fneur.2024.1339167). ()

Core Pathophysiology (mechanisms, pathways, cells) 
- Primary mechanisms at the NMJ
  - Complement-mediated MAC injury (classical pathway via IgG1/IgG3 anti-AChR) leading to synaptic membrane loss and reduced safety factor (JCI 2024; Eye 2024). (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2)
  - Antigenic modulation and receptor internalization of AChR, reducing receptor density (JCI 2024; Frontiers in Immunology 2023). (kaminski2024myastheniagravisthe pages 2-4, huda2023inflammationandautoimmune pages 1-2)
  - Blockade of ACh–AChR interaction and disruption of rapsyn-stabilized clusters (JCI 2024). (kaminski2024myastheniagravisthe pages 2-4)
  - Agrin–LRP4–MuSK pathway blockade by IgG4 anti-MuSK (non–complement fixing) and IgG1 anti-LRP4, impairing AChR clustering (Eye 2024; Cells 2024). (jacob2024treatingmyastheniagravis pages 1-2, dziadkowiak2024muskmyastheniagravis—potential pages 13-14)

- Dysregulated molecular/cellular pathways
  - Complement activation and MAC assembly in AChR-MG; therapeutic anti-C5 validation (Expert Rev Clin Immunol 2022). (keller2022fcreceptortargetedtherapies pages 2-3)
  - FcRn-mediated IgG recycling: therapeutic antagonism lowers IgG, supporting a causal role for circulating IgG autoantibodies broadly in MG (Frontiers in Neurology 2023). (bhandari2023fcrnreceptorantagonists pages 1-2)
  - Thymic ectopic germinal centers (GCs), Tfh expansion, BAFF enrichment, and type I IFN signatures that sustain intrathymic B cell activation and autoreactive T cell priming; weaker/thymus-sparse signature in MuSK-MG (JCI 2024; Frontiers in Immunology 2023). (kaminski2024myastheniagravisthe pages 2-4, huda2023inflammationandautoimmune pages 1-2)

- Immune cell processes
  - B cell activation, class-switch, and plasmablast/plasma cell antibody production (intrathymic and peripheral) (JCI 2024; Frontiers in Immunology 2023). (kaminski2024myastheniagravisthe pages 2-4, huda2023inflammationandautoimmune pages 1-2)
  - Tfh/Tfr imbalance and reduced Treg function facilitating GC reactions (JCI 2024; Frontiers in Immunology 2023). (kaminski2024myastheniagravisthe pages 2-4, huda2023inflammationandautoimmune pages 1-2)
  - Antigen presentation by medullary thymic epithelial cells (mTECs) and dendritic cells, with tolerance failure in EOMG (Frontiers in Neurology 2023). (bhandari2023fcrnreceptorantagonists pages 1-2)

Key Molecular Players (HGNC genes/proteins; cell types; anatomical sites; chemicals)
- Autoantigens/complex
  - AChR subunits (HGNC: CHRNA1, CHRNB1), rapsyn (HGNC: RAPSN), DOK7 (HGNC: DOK7) (JCI 2024). (kaminski2024myastheniagravisthe pages 2-4)
  - MUSK (HGNC: 7517), LRP4 (HGNC: 6697), AGRN (HGNC: 329) central to clustering and synaptogenesis (Eye 2024; Cells 2024). (jacob2024treatingmyastheniagravis pages 1-2, dziadkowiak2024muskmyastheniagravis—potential pages 13-14)
- Immune genes (selected associations)
  - HLA class II alleles (e.g., HLA-DRB1, HLA-DQB1) with subtype/age-of-onset effects; CTLA4 and PTPN22 highlighted in clinical overviews (Nature Comm 2024; JCI 2024). (kaminski2024myastheniagravisthe pages 2-4)
- Cell types (CL ontology)
  - B cell (CL:0000236), plasmablast (CL:0000980), T follicular helper cell (CL:0000914), regulatory T cell (CL:0000815), dendritic cell (CL:0000451), medullary thymic epithelial cell (CL:0000786) (Frontiers in Immunology 2023; JCI 2024). (huda2023inflammationandautoimmune pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- Anatomical locations (UBERON)
  - Neuromuscular junction (UBERON:0007200), skeletal muscle tissue (UBERON:0001134), thymus (UBERON:0002370) (JCI 2024; Eye 2024). (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2)
- Chemical entities (ChEBI)
  - Acetylcholine (CHEBI:15355), immunoglobulin G (CHEBI:16991); complement component C5 protein targeted by therapeutics (mechanistic) (Expert Rev Clin Immunol 2022). (keller2022fcreceptortargetedtherapies pages 2-3)

Biological Processes for GO annotation (disrupted in MG)
- Complement activation, classical pathway (GO:0006958); membrane attack complex assembly (component of complement activation) (AChR-MG) (JCI 2024; Expert Rev Clin Immunol 2022). (kaminski2024myastheniagravisthe pages 2-4, keller2022fcreceptortargetedtherapies pages 2-3)
- Receptor-mediated endocytosis (GO:0006898) of AChR (antigenic modulation) (JCI 2024). (kaminski2024myastheniagravisthe pages 2-4)
- Cholinergic synaptic transmission (GO:0007271) and neuromuscular junction development (GO:0007528) (disrupted by agrin–LRP4–MuSK blockade) (Eye 2024; Cells 2024). (jacob2024treatingmyastheniagravis pages 1-2, dziadkowiak2024muskmyastheniagravis—potential pages 13-14)
- B cell activation (GO:0042113), germinal center formation (GO:0006955, immune process), T cell activation (GO:0042110), Tfh cell differentiation (GO:0002292) (thymic hyperplasia) (Frontiers in Immunology 2023; JCI 2024). (huda2023inflammationandautoimmune pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- Type I interferon signaling pathway (GO:0060337) and cytokine-mediated signaling (GO:0019221) in thymic microenvironment (Frontiers in Immunology 2023). (huda2023inflammationandautoimmune pages 1-2)

Cellular Components (where key processes occur)
- Postsynaptic membrane (GO:0045211) and synaptic basal lamina/extracellular matrix (basement membrane, GO:0005604) at NMJ—sites of AChR and agrin–LRP4–MuSK signaling (Eye 2024; JCI 2024). (jacob2024treatingmyastheniagravis pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- Membrane attack complex (GO:0005579) on the postsynaptic membrane (Expert Rev Clin Immunol 2022; JCI 2024). (keller2022fcreceptortargetedtherapies pages 2-3, kaminski2024myastheniagravisthe pages 2-4)
- Early/late endosomes and lysosomes (GO:0005768; GO:0005764) mediating AChR internalization and FcRn-dependent IgG recycling (Frontiers in Neurology 2023). (bhandari2023fcrnreceptorantagonists pages 1-2)
- Thymic medulla and germinal center–like niches (thymic follicular hyperplasia) as intrathymic sites of autoimmunity (Frontiers in Immunology 2023; JCI 2024). (huda2023inflammationandautoimmune pages 1-2, kaminski2024myastheniagravisthe pages 2-4)

Disease progression (sequence from trigger to clinical phenotype)
- Predisposition and trigger: Polygenic susceptibility (HLA class II, immune-regulatory loci) and environmental/inflammatory triggers (e.g., type I IFN–rich milieu) prime breakdown of central tolerance in the thymus for EOMG. (kaminski2024myastheniagravisthe pages 2-4, huda2023inflammationandautoimmune pages 1-2)
- Intrathymic autoimmunity: mTEC/dendritic cell antigen presentation of AChR subunits and myoid-cell antigens with GC formation, Tfh help, BAFF signaling, and class-switched B cell responses. (huda2023inflammationandautoimmune pages 1-2, bhandari2023fcrnreceptorantagonists pages 1-2)
- Peripheral effector phase: Circulating IgG autoantibodies reach NMJ; in AChR-MG, complement activation and receptor internalization reduce neuromuscular safety factor; in MuSK-/LRP4-MG, impaired AChR clustering further reduces transmission. (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2, dziadkowiak2024muskmyastheniagravis—potential pages 13-14)
- Clinical manifestation: Fluctuating, fatigable weakness with ocular, bulbar, respiratory, and limb involvement according to antibody specificity and disease burden; crises occur with severe bulbar/respiratory involvement. (jacob2024treatingmyastheniagravis pages 1-2)

Phenotypic manifestations and mechanism links (HP terms)
- Fatigable muscle weakness (HP:0003701): Reduced NMJ safety factor from MAC injury and AChR loss (AChR-MG) or from impaired AChR clustering (MuSK-/LRP4-MG) (JCI 2024; Eye 2024). (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2)
- Ptosis (HP:0000508) and diplopia (HP:0000651): Extraocular NMJ involvement; ocular MG commonly due to AChR antibodies (Eye 2024). (jacob2024treatingmyastheniagravis pages 1-2)
- Dysphagia (HP:0002015), dysarthria (HP:0001260), and respiratory failure (HP:0002878): Bulbar/respiratory muscle NMJ failure; severe in some MuSK-MG and generalized AChR-MG (Eye 2024). (jacob2024treatingmyastheniagravis pages 1-2)

Gene/protein annotations (selected; HGNC and ontology mapping)
- CHRNA1 (HGNC:1956) and CHRNB1 (HGNC:1959): AChR subunits; processes: cholinergic synaptic transmission (GO:0007271), receptor-mediated endocytosis (GO:0006898); component: postsynaptic membrane (GO:0045211). (kaminski2024myastheniagravisthe pages 2-4)
- MUSK (HGNC:7517): Receptor tyrosine kinase for NMJ maintenance; processes: NMJ development (GO:0007528); component: postsynaptic membrane (GO:0045211). (dziadkowiak2024muskmyastheniagravis—potential pages 13-14, jacob2024treatingmyastheniagravis pages 1-2)
- LRP4 (HGNC:6697): Agrin co-receptor; processes: synapse organization (GO:0050808); component: extracellular region/basal lamina. (jacob2024treatingmyastheniagravis pages 1-2)
- AGRN (HGNC:329): Ligand driving AChR clustering; processes: synapse organization; component: synaptic cleft/extracellular matrix. (jacob2024treatingmyastheniagravis pages 1-2)
- HLA-DRB1/DQB1 (HGNC:4948/3115), CTLA4 (HGNC:2505), PTPN22 (HGNC:9653): Genetic susceptibility; processes: antigen presentation (GO:0019882), T cell activation (GO:0042110). (kaminski2024myastheniagravisthe pages 2-4)

Cell type involvement (CL) and anatomical locations (UBERON)
- B cells (CL:0000236) and plasmablasts (CL:0000980): Autoantibody production in thymic GCs and periphery (UBERON:0002370, thymus; UBERON:0007200, NMJ effector site) (Frontiers in Immunology 2023; JCI 2024). (huda2023inflammationandautoimmune pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- Tfh (CL:0000914)/Tfr and Tregs (CL:0000815): GC support vs regulation; imbalance favors autoimmunity (Frontiers in Immunology 2023). (huda2023inflammationandautoimmune pages 1-2)
- Dendritic cells (CL:0000451) and mTECs (CL:0000786): Central tolerance and antigen presentation in thymus (Frontiers in Neurology 2023). (bhandari2023fcrnreceptorantagonists pages 1-2)

Chemical entities (CHEBI) and therapeutics (mechanistic tie-ins)
- Acetylcholine (CHEBI:15355): Neurotransmitter whose postsynaptic signaling is impaired by AChR loss/blockade (Eye 2024). (jacob2024treatingmyastheniagravis pages 1-2)
- IgG (CHEBI:16991): Pathogenic effector molecule; subclasses dictate complement activity (IgG1/3) vs blocking (IgG4) (JCI 2024; Frontiers in Neurology 2023). (kaminski2024myastheniagravisthe pages 2-4, bhandari2023fcrnreceptorantagonists pages 1-2)
- Complement C5 (protein target): Blockade prevents MAC formation at NMJ in AChR-MG, validating complement’s causal role (Expert Rev Clin Immunol 2022). (keller2022fcreceptortargetedtherapies pages 2-3)

Evidence items with PMIDs/DOIs/URLs (recent, prioritized)
- Kaminski HJ et al. Myasthenia gravis: the future is here. Journal of Clinical Investigation. Jun 2024. DOI: 10.1172/jci179742; URL: https://doi.org/10.1172/jci179742 (supports NMJ mechanisms, subtypes, genetics, therapeutics). (kaminski2024myastheniagravisthe pages 2-4, kaminski2024myastheniagravisthe pages 10-10)
- Dalakas MC. Role of complement and targeted immunotherapies in MG. Expert Review of Clinical Immunology. Jun 2022. DOI: 10.1080/1744666X.2022.2082946; URL: https://doi.org/10.1080/1744666X.2022.2082946 (validates complement inhibition). (keller2022fcreceptortargetedtherapies pages 2-3)
- Bhandari V, Bril V. FcRn receptor antagonists in MG. Frontiers in Neurology. Aug 2023. DOI: 10.3389/fneur.2023.1229112; URL: https://doi.org/10.3389/fneur.2023.1229112 (FcRn biology and clinical use). (bhandari2023fcrnreceptorantagonists pages 1-2)
- Jacob S. Treating myasthenia gravis beyond the eye clinic. Eye. May 2024. DOI: 10.1038/s41433-024-03133-x; URL: https://doi.org/10.1038/s41433-024-03133-x (subtype mechanisms, clinical correlations). (jacob2024treatingmyastheniagravis pages 1-2)
- Dziadkowiak E et al. MuSK Myasthenia Gravis—Mechanisms and targeted treatment. Cells. Mar 2024. DOI: 10.3390/cells13060556; URL: https://doi.org/10.3390/cells13060556 (MuSK IgG4 pathology). (dziadkowiak2024muskmyastheniagravis—potential pages 13-14)
- Huda R. Inflammation and autoimmune MG. Frontiers in Immunology. Jan 2023. DOI: 10.3389/fimmu.2023.1110499; URL: https://doi.org/10.3389/fimmu.2023.1110499 (thymic inflammation, Tfh/BAFF/IFN). (huda2023inflammationandautoimmune pages 1-2)
- Braun A et al. Genome-wide meta-analysis of MG. Nature Communications. Nov 2024. DOI: 10.1038/s41467-024-53595-6; URL: https://doi.org/10.1038/s41467-024-53595-6 (genetics, PRS). (kaminski2024myastheniagravisthe pages 2-4)
- Vissing J et al. Epidemiology of MG in Denmark, Finland, Sweden. JNNP. Mar 2024. DOI: 10.1136/jnnp-2023-333097; URL: https://doi.org/10.1136/jnnp-2023-333097 (epidemiology). ()
- Ye Y et al. Epidemiology of MG in the USA. Frontiers in Neurology. Feb 2024. DOI: 10.3389/fneur.2024.1339167; URL: https://doi.org/10.3389/fneur.2024.1339167 (epidemiology). ()

Direct quotes (supporting key statements)
- “AChR antibodies act via three established mechanisms: complement activation with MAC formation… antigenic modulation… and direct blockade of the ACh binding site” (JCI 2024) (kaminski2024myastheniagravisthe pages 2-4).
- “MuSK autoantibodies are predominantly IgG4… block the binding site for LRP4 on MuSK, thereby inhibiting the downstream phosphorylation pathway and compromising the formation of AChR clusters” (Cells 2024) (dziadkowiak2024muskmyastheniagravis—potential pages 13-14).
- “FcRn receptors prevent the catabolism of IgG… blocking the FcRn… leading to outcomes similar to those achieved through plasma exchange” (Frontiers in Neurology 2023) (bhandari2023fcrnreceptorantagonists pages 1-2).

Structured ontology annotations for knowledge base
- Disease: Myasthenia gravis (MONDO:0005041)
- Genes/Proteins (HGNC): CHRNA1, CHRNB1, RAPSN, DOK7, MUSK, LRP4, AGRN, HLA-DRB1, HLA-DQB1, CTLA4, PTPN22 (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2, dziadkowiak2024muskmyastheniagravis—potential pages 13-14)
- GO Processes: complement activation, classical pathway (GO:0006958); receptor-mediated endocytosis (GO:0006898); cholinergic synaptic transmission (GO:0007271); neuromuscular junction development (GO:0007528); B cell activation (GO:0042113); T cell activation (GO:0042110); type I interferon signaling (GO:0060337) (kaminski2024myastheniagravisthe pages 2-4, keller2022fcreceptortargetedtherapies pages 2-3, huda2023inflammationandautoimmune pages 1-2, jacob2024treatingmyastheniagravis pages 1-2)
- Cellular Components: postsynaptic membrane (GO:0045211); membrane attack complex (GO:0005579); endosome (GO:0005768); lysosome (GO:0005764) (kaminski2024myastheniagravisthe pages 2-4, keller2022fcreceptortargetedtherapies pages 2-3, bhandari2023fcrnreceptorantagonists pages 1-2)
- Cell Types (CL): B cell (CL:0000236); plasmablast (CL:0000980); Tfh (CL:0000914); Treg (CL:0000815); dendritic cell (CL:0000451); mTEC (CL:0000786) (huda2023inflammationandautoimmune pages 1-2, bhandari2023fcrnreceptorantagonists pages 1-2)
- Anatomical Sites (UBERON): neuromuscular junction (UBERON:0007200); skeletal muscle tissue (UBERON:0001134); thymus (UBERON:0002370) (jacob2024treatingmyastheniagravis pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- Chemical Entities (ChEBI): acetylcholine (CHEBI:15355); immunoglobulin G (CHEBI:16991) (jacob2024treatingmyastheniagravis pages 1-2, bhandari2023fcrnreceptorantagonists pages 1-2)
- Phenotypes (HP): fatigable muscle weakness (HP:0003701); ptosis (HP:0000508); diplopia (HP:0000651); dysphagia (HP:0002015); dysarthria (HP:0001260); respiratory failure (HP:0002878) (jacob2024treatingmyastheniagravis pages 1-2)

Notes and limitations
- Detailed thymic single-cell and spatial transcriptomic data, and comprehensive ncRNA catalogs, while summarized in reviews, require additional primary sources for subtype-specific differential expression beyond the scope of the citations gathered herein (Frontiers in Immunology 2023; JCI 2024). (huda2023inflammationandautoimmune pages 1-2, kaminski2024myastheniagravisthe pages 2-4)

Citations
- Mechanistic claims at the NMJ: (kaminski2024myastheniagravisthe pages 2-4, jacob2024treatingmyastheniagravis pages 1-2, keller2022fcreceptortargetedtherapies pages 2-3)
- MuSK/LRP4 subclass and signaling: (dziadkowiak2024muskmyastheniagravis—potential pages 13-14, jacob2024treatingmyastheniagravis pages 1-2)
- Thymic pathology and immune subsets: (huda2023inflammationandautoimmune pages 1-2, kaminski2024myastheniagravisthe pages 2-4, bhandari2023fcrnreceptorantagonists pages 1-2)
- Therapeutic mechanistic validation (C5, FcRn): (keller2022fcreceptortargetedtherapies pages 2-3, bhandari2023fcrnreceptorantagonists pages 1-2, kaminski2024myastheniagravisthe pages 2-4)
- Genetics (2024 GWAS/meta): (kaminski2024myastheniagravisthe pages 2-4)
- Epidemiology (2024): (, )

References

1. (kaminski2024myastheniagravisthe pages 2-4): Henry J. Kaminski, Patricia Sikorski, S. Isabel Coronel, and Linda L. Kusner. Myasthenia gravis: the future is here. Journal of Clinical Investigation, Jun 2024. URL: https://doi.org/10.1172/jci179742, doi:10.1172/jci179742. This article has 70 citations and is from a highest quality peer-reviewed journal.

2. (jacob2024treatingmyastheniagravis pages 1-2): Saiju Jacob. Treating myasthenia gravis beyond the eye clinic. Eye, 38:2422-2436, May 2024. URL: https://doi.org/10.1038/s41433-024-03133-x, doi:10.1038/s41433-024-03133-x. This article has 6 citations and is from a peer-reviewed journal.

3. (bhandari2023fcrnreceptorantagonists pages 1-2): Vinaya Bhandari and Vera Bril. Fcrn receptor antagonists in the management of myasthenia gravis. Frontiers in Neurology, Aug 2023. URL: https://doi.org/10.3389/fneur.2023.1229112, doi:10.3389/fneur.2023.1229112. This article has 33 citations and is from a peer-reviewed journal.

4. (keller2022fcreceptortargetedtherapies pages 2-3): Christian W. Keller, Marc Pawlitzki, Heinz Wiendl, and Jan Lünemann. Fc-receptor targeted therapies for the treatment of myasthenia gravis. International Journal of Molecular Sciences, May 2022. URL: https://doi.org/10.3390/ijms22115755, doi:10.3390/ijms22115755. This article has 29 citations and is from a poor quality or predatory journal.

5. (dziadkowiak2024muskmyastheniagravis—potential pages 13-14): Edyta Dziadkowiak, Dagmara Baczyńska, and Marta Waliszewska-Prosół. Musk myasthenia gravis—potential pathomechanisms and treatment directed against specific targets. Cells, 13:556, Mar 2024. URL: https://doi.org/10.3390/cells13060556, doi:10.3390/cells13060556. This article has 10 citations and is from a poor quality or predatory journal.

6. (huda2023inflammationandautoimmune pages 1-2): Ruksana Huda. Inflammation and autoimmune myasthenia gravis. Frontiers in Immunology, Jan 2023. URL: https://doi.org/10.3389/fimmu.2023.1110499, doi:10.3389/fimmu.2023.1110499. This article has 49 citations and is from a peer-reviewed journal.

7. (kaminski2024myastheniagravisthe pages 10-10): Henry J. Kaminski, Patricia Sikorski, S. Isabel Coronel, and Linda L. Kusner. Myasthenia gravis: the future is here. Journal of Clinical Investigation, Jun 2024. URL: https://doi.org/10.1172/jci179742, doi:10.1172/jci179742. This article has 70 citations and is from a highest quality peer-reviewed journal.