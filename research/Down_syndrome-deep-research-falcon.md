---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:01:05.496369'
end_time: '2025-12-15T09:08:15.769113'
duration_seconds: 430.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Down syndrome
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Down syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Down syndrome**.
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
- **Disease Name:** Down syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Down syndrome**.
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
- Disease Name: Down syndrome (trisomy 21)
- MONDO ID: MONDO:0000508
- Category: Genetic

Pathophysiology overview (current understanding)
Down syndrome (DS) is caused by constitutive trisomy of human chromosome 21 (Hsa21). Contemporary multi-omic and single-cell studies converge on several mechanistic pillars: dosage effects of Hsa21 genes drive chronic interferon (IFN) pathway hyperactivation and JAK–STAT signaling (“interferonopathy”), broad immune remodeling, altered neurodevelopment with neuron-to-astrocyte fate shifts and microglial activation, and metabolic stress pathways including redox and tryptophan–kynurenine dysregulation. These processes interact with APP gene dose to produce near-universal Alzheimer-like neuropathology in adulthood, with microglia- and IFN-linked inflammation shaping amyloid/tau pathophysiology. Modulation of JAK–STAT signaling normalizes IFN signatures in people with DS and rescues inflammatory gene programs and cognition in DS–AD mouse models, motivating trials of immune-modulatory strategies in DS. (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)

> - IFN/JAK‑STAT: "constitutive hyperactivation of interferon signaling" in trisomy 21 is driven in part by triplication of IFN receptor genes on chr21; "JAK inhibition normalizes interferon signatures" (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3)
> - DS→AD links: APP dose effect produces early amyloid pathology and DS‑AD features; spatial transcriptomics and microglial activation link IFN/inflammation to accelerated amyloid/tau, and systemic JAK inhibition rescued inflammatory gene expression and cognition in a DS‑AD mouse model (araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)
> - Neurodevelopmental defects: reduced neurogenesis, progenitor cell‑cycle dysregulation, OLIG2 overexpression driving gliogenesis at the expense of neurons, and persistent dendritic/spine deficits that impair circuit formation ("shift from neuron to astrocyte differentiation") (russo2024consequencesoftrisomy pages 17-18, uguagliati2024astrocyticalterationsand pages 1-2)
> - Glia & complement: increased astrocyte numbers, reactive microglial / disease‑associated microglia states, and complement pathway dysregulation accompany neuroinflammation and synaptic alterations in DS (uguagliati2024astrocyticalterationsand pages 1-2, galbraith2023multidimensionaldefinitionof pages 1-2)
> - Mitochondria & metabolism: mitochondrial dysfunction, oxidative stress and altered metabolic pathways (notably tryptophan→kynurenine dysregulation linked to neurotoxic catabolites) are recurrent features in DS and correlate with amyloid burden and cognitive decline (galbraith2023multidimensionaldefinitionof pages 1-2, risgaard2025molecularandcellular pages 31-33)
> - Airway/epithelia antiviral responses: recent preclinical/clinical reports describe impaired type‑III IFN responses and amplified airway inflammation during RSV in DS (preprint evidence), consistent with systemic IFN hypersensitivity in T21 (araya2025interferonsignalingmodulates pages 18-18, galbraith2023multidimensionaldefinitionof pages 1-2)
> - DYRK1A dosage: DYRK1A triplication perturbs neurodevelopment, immune and peripheral phenotypes; therapeutic approaches (small‑molecule inhibitors, EGCG trials, emerging ASO strategies) show promise but mixed preclinical/clinical results and safety/ specificity concerns (llambrich2024pleiotropiceffectsof pages 34-35, araya2025interferonsignalingmodulates pages 1-3)
> - AD biomarkers & pathology in DS: APP dyshomeostasis underlies near‑universal AD neuropathology in DS (amyloid accumulation, altered plaque proteome, tau spread and CAA peptide signatures), motivating trials of anti‑amyloid and other targeted therapies in DS populations (araya2025interferonsignalingmodulates pages 1-3, galbraith2023multidimensionaldefinitionof pages 1-2)


*Blockquote: Concise, evidence‑linked bullet lines summarizing mechanistic findings (2023–2025) across interferon/JAK signaling, neurodevelopment, glia, mitochondria, DYRK1A and APP/AD biology in Down syndrome; citations point to the aggregated context evidence used.*

1) Core pathophysiology
- Interferon/JAK–STAT hyperactivation and immune remodeling
  - Multi-omic profiling of hundreds of individuals with DS defined a chronic IFN-hyperactive state that stratifies clinical phenotypes, including increased cytotoxic T cells, B-cell depletion, monocyte activation, and enriched autoimmunity and congenital heart disease; the authors conclude DS is an interferonopathy partially driven by triplication of IFN receptor genes on Hsa21 (IFNAR1, IFNAR2, IFNGR2, IL10RB). Normalization of IFN signatures with JAK inhibition was shown in a longitudinal DS case (Science Advances, 2023). (galbraith2023multidimensionaldefinitionof pages 1-2)
  - In DS–AD mouse models, spatial transcriptomics and flow cytometry demonstrate genome-wide IFN program upregulation, disease-associated microglial states, neuronal loss, and that systemic JAK inhibition rescues inflammatory gene expression and improves cognition, directly implicating IFN/JAK–STAT in DS neurodegeneration. (araya2025interferonsignalingmodulates pages 1-3)

- Neurodevelopmental alterations: neuron–glia lineage balance, circuit formation
  - Human iPSC and fetal studies show 20–50% fewer cortical neurons from birth; impaired neurogenesis with progenitor cell-cycle and differentiation defects, OLIG2 overexpression favoring astrogliogenesis, and persistent deficits in dendritic arborization and spines that disrupt circuit formation. Modulation of pathways such as SHH and experimental silencing of the extra chromosome rescue aspects of neurogenesis in vitro, highlighting targetability of lineage and morphogen programs. (russo2024consequencesoftrisomy pages 17-18)
  - Astrocyte-centric pathology: prenatal shift from neuron to astrocyte differentiation, increased astrocyte numbers and reactive states, and downstream effects on synaptogenesis and excitatory/inhibitory balance link astrocytic dysfunction to cognitive phenotypes. (uguagliati2024astrocyticalterationsand pages 1-2)

- Neuroinflammation and microglia
  - Disease-associated microglia (DAM-like) states and interferon-responsive microglia are repeatedly observed in DS and DS–AD models; these states associate with neuronal loss and inflammatory transcriptomes and are suppressible by JAK inhibition in vivo. (araya2025interferonsignalingmodulates pages 1-3)

- Metabolic stress and redox/tryptophan pathways
  - IFN hyperactivation links to tryptophan catabolism and kynurenine pathway remodeling, associating with neurotoxic catabolites and systemic metabolic changes in DS; these features co-segregate with high IFN scores and clinical burden. (galbraith2023multidimensionaldefinitionof pages 1-2)

- APP dose and Alzheimer-like pathology
  - APP trisomic dose drives early, widespread amyloid pathology in DS; in DS–AD mouse genetics, additional Hsa21 gene dose modifies cognition and inflammatory states while JAK inhibition reduces inflammatory gene expression and improves cognitive outcomes. (araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)

2) Key molecular players
- Genes/Proteins (HGNC):
  - IFNAR1, IFNAR2, IFNGR2, IL10RB (interferon receptors; dosage on Hsa21) – drive IFN hypersensitivity and JAK–STAT hyperactivation in DS. (galbraith2023multidimensionaldefinitionof pages 1-2)
  - JAK1/2–STAT axis (signaling mediators downstream of IFN receptors) – targetable; inhibition normalizes IFN signatures and improves neuroinflammatory/cognitive readouts in models. (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3)
  - APP (amyloid precursor protein; Hsa21) – dose effect underpins DS-associated Alzheimer pathology; amyloid deposition is modified by inflammatory and microglial states. (araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)
  - OLIG2 (bHLH TF) – overexpression shifts neurogenesis toward gliogenesis; contributes to reduced neuronal output. (russo2024consequencesoftrisomy pages 17-18)
  - Astrocytic markers (GFAP and others) – upregulated, reflecting increased astrocytogenesis and reactive astrogliosis. (uguagliati2024astrocyticalterationsand pages 1-2)

- Chemical entities (CHEBI):
  - JAK inhibitors (e.g., tofacitinib class) – systemically reduce IFN-inducible inflammatory programs and improve cognitive endpoints in DS–AD mice. (araya2025interferonsignalingmodulates pages 1-3)
  - Kynurenine pathway metabolites – implicated in IFN-driven metabolic remodeling and neurotoxicity. (galbraith2023multidimensionaldefinitionof pages 1-2)

- Cell types (CL):
  - Microglia (CL:0000129) – adopt disease-associated and IFN-responsive states; key in synaptic and inflammatory remodeling. (araya2025interferonsignalingmodulates pages 1-3)
  - Astrocytes (CL:0000127) – increased numbers/reactivity; influence neurogenesis, synaptogenesis, and E/I balance. (uguagliati2024astrocyticalterationsand pages 1-2)
  - Neural progenitors (radial glia) – reduced proliferation/dysregulated cell cycle; impaired neuronal output. (russo2024consequencesoftrisomy pages 17-18)
  - Peripheral T and B cells, monocytes – remodeled with high IFN scores in DS blood multi-omics. (galbraith2023multidimensionaldefinitionof pages 1-2)

- Anatomical locations (UBERON):
  - Cortex (UBERON:0000956), hippocampus (UBERON:0001954), cerebellum (UBERON:0002037) – sites of reduced neurons, altered lineage dynamics, and glial dysregulation in DS; neuroinflammatory signatures and spatial transcriptomic changes in DS–AD mice. (russo2024consequencesoftrisomy pages 17-18, araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)
  - Blood (UBERON:0000178) – systemic interferonopathy and immune remodeling detectable in multi-omics. (galbraith2023multidimensionaldefinitionof pages 1-2)

3) Biological processes (GO) disrupted
- Type I/II interferon signaling (GO:0060337; GO:0060333), response to interferon (GO:0034340) – chronically upregulated; drives systemic and CNS phenotypes; reversed by JAK inhibition. (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3)
- JAK–STAT cascade (GO:0007259) – aberrant activation downstream of IFN receptors; targetable with JAK inhibitors. (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3)
- Neurogenesis and neuron differentiation (GO:0022008; GO:0030182) – reduced neuronal output; lineage skewing to astrocytes (gliogenesis, GO:0014002). (russo2024consequencesoftrisomy pages 17-18, uguagliati2024astrocyticalterationsand pages 1-2)
- Synapse organization and dendrite development (GO:0050808; GO:0016358) – persistent dendritic/spine deficits and circuit disruption. (russo2024consequencesoftrisomy pages 17-18)
- Immune effector processes and microglial activation (GO:0002252; GO:0001774) – DAM-like and IFN-responsive microglia in DS brain; suppressed by JAK inhibition. (araya2025interferonsignalingmodulates pages 1-3)
- Tryptophan metabolic process to kynurenine (GO:0006586) – IFN-associated metabolic remodeling linked to neurotoxic catabolites. (galbraith2023multidimensionaldefinitionof pages 1-2)

4) Cellular components (GO)
- Plasma membrane IFN receptor complexes (GO:0005886 context; specific receptor complexes) – dosage increased (IFNAR1/2, IFNGR2, IL10RB) with downstream JAK–STAT activation. (galbraith2023multidimensionaldefinitionof pages 1-2)
- Synapse (GO:0045202) and postsynapse (GO:0098794) – affected by dendritic/spine and microglial-mediated remodeling. (russo2024consequencesoftrisomy pages 17-18, araya2025interferonsignalingmodulates pages 1-3)
- Microglial cell soma/processes within brain parenchyma – spatially enriched IFN/inflammatory states in DS–AD models. (araya2025interferonsignalingmodulates pages 1-3)

5) Disease progression (sequence of events)
- Genetic trigger: trisomy 21 → dosage increase of Hsa21 genes (including IFN receptor subunits and APP). (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3)
- Early development: progenitor cell-cycle and differentiation defects; neuron-to-astrocyte shift; reduced neuronal output and synaptic maturation → altered circuits from prenatal/early postnatal stages. (russo2024consequencesoftrisomy pages 17-18, uguagliati2024astrocyticalterationsand pages 1-2)
- Systemic immune milieu: chronic IFN hyperactivation with immune remodeling and metabolic (kynurenine) changes detectable in blood; clinical associations with congenital heart disease and autoimmunity. (galbraith2023multidimensionaldefinitionof pages 1-2)
- CNS inflammation: interferon-responsive microglia and DAM-like states, astrocyte reactivity, and neuronal loss; these inflammatory programs are modulable by JAK inhibition. (araya2025interferonsignalingmodulates pages 1-3)
- AD emergence: APP dose accelerates amyloid pathology; IFN/microglial states and broader trisomic gene dose modify progression and cognition; JAK inhibition improves inflammatory signatures and cognitive performance in DS–AD models. (araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)

6) Phenotypic manifestations (HP terms) linked to mechanisms
- Intellectual disability (HP:0001249) – linked to reduced neurogenesis, dendrite/spine deficits, and astrocyte/microglia dysregulation. (russo2024consequencesoftrisomy pages 17-18, uguagliati2024astrocyticalterationsand pages 1-2)
- Autoimmunity and immune dysregulation (HP:0002960 aggregate) – associated with high IFN scores and immune remodeling. (galbraith2023multidimensionaldefinitionof pages 1-2)
- Early-onset Alzheimer disease pathology (HP:0002511) – driven by APP dose, with microglial/IFN modulation of progression; cognitive decline in DS–AD models is rescueable with JAK inhibition. (araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)

Current applications and real-world implementations
- JAK inhibition as immunomodulation in DS:
  - Blood multi-omics in people with DS demonstrate normalization of IFN signatures in a longitudinal case under JAK inhibition, motivating clinical testing of JAK inhibitors for DS immune and inflammatory complications (Science Advances, 2023; DOI: 10.1126/sciadv.adg6218). (galbraith2023multidimensionaldefinitionof pages 1-2)
  - In DS–AD mouse models, systemic JAK inhibition decreased inflammatory gene expression and improved cognition, supporting translational rationale for modulating IFN/JAK–STAT in DS-associated neurodegeneration (iScience, 2025; DOI: 10.1016/j.isci.2025.113130). (araya2025interferonsignalingmodulates pages 1-3)

Expert opinions and analysis (authoritative sources)
- “DS displays chronic hyperactivation of interferon signaling … high interferon activity associates with a distinct proinflammatory phenotype” and “JAK inhibition normalizes interferon signatures with therapeutic benefit in DS.” (Science Advances, 2023). (galbraith2023multidimensionaldefinitionof pages 1-2)
- Preclinical DS–AD work integrates spatial transcriptomics, immune cytometry, and behavioral readouts to conclude that IFN/JAK–STAT actively modulates pathology and cognition, positioning JAK inhibitors as candidate disease-modifying agents in DS–AD (iScience, 2025). (araya2025interferonsignalingmodulates pages 1-3)
- Neurodevelopmental consensus (Nature Reviews Neuroscience, 2024): trisomy 21 disrupts neurogenesis and lineages (e.g., OLIG2-driven gliogenesis) and yields lasting dendritic/synaptic deficits; mechanistic rescue in vitro by morphogen/epigenetic interventions highlights tractable pathways. (russo2024consequencesoftrisomy pages 17-18)

Relevant statistics and data points from recent studies
- Multi-omic stratification by interferon score in DS identified strongest peripheral immune remodeling (↑ cytotoxic T cells, B-cell depletion, monocyte activation) in individuals with highest IFN activity; IFN hyperactivation co-segregated with congenital heart disease and autoimmunity (Science Advances, 2023). (galbraith2023multidimensionaldefinitionof pages 1-2)
- In DS–AD mice, JAK inhibition reduced brain inflammatory transcriptomes and improved cognition compared with vehicle, linking pathway suppression to functional benefit (iScience, 2025). (araya2025interferonsignalingmodulates pages 1-3)

Evidence items (primary literature, with quotes when available)
- “Individuals with Down syndrome (DS) display chronic hyperactivation of interferon signaling… Interferon hyperactivity associates with a distinct proinflammatory phenotype… [and] a longitudinal case study demonstrated that JAK inhibition normalizes interferon signatures with therapeutic benefit in DS.” Science Advances (Jun 2023). (galbraith2023multidimensionaldefinitionof pages 1-2)
- “Spatial transcriptomics revealed genome-wide changes dominated by upregulated interferon signatures… Systemic JAK inhibition… rescued gene expression changes and improved cognition,” in DS–AD mouse models. iScience (Aug 2025). (araya2025interferonsignalingmodulates pages 1-3)
- “Reduced neurogenesis, progenitor cell-cycle disruption… OLIG2 overexpression… persistent dendritic/spine deficits” summarized for DS brain development. Nature Reviews Neuroscience (Oct 2024). (russo2024consequencesoftrisomy pages 17-18)
- “Shift from neuron to astrocyte differentiation… increased astrocyte numbers… detrimental consequences for brain development,” with impacts on synaptogenesis and E/I balance. Cells (Dec 2024). (uguagliati2024astrocyticalterationsand pages 1-2)

Ontology-aligned annotations
- Genes/Proteins (HGNC): IFNAR1 (HGNC:5433), IFNAR2 (HGNC:5434), IFNGR2 (HGNC:5437), IL10RB (HGNC:5961), JAK1 (HGNC:6190), JAK2 (HGNC:6192), STAT1 (HGNC:11362), APP (HGNC:620)
- Biological Process (GO): type I interferon signaling (GO:0060337); JAK–STAT cascade (GO:0007259); neurogenesis (GO:0022008); gliogenesis (GO:0014002); synapse organization (GO:0050808); tryptophan metabolic process (GO:0006586)
- Cellular Component (GO): plasma membrane receptor complex; synapse (GO:0045202); postsynapse (GO:0098794)
- Phenotype (HPO): Intellectual disability (HP:0001249); Autoimmunity (HP:0002960); Early-onset Alzheimer disease (HP:0002511)
- Cell Types (CL): Microglia (CL:0000129); Astrocyte (CL:0000127); Neural progenitor/radial glia (CL:0002320 subset)
- Anatomical (UBERON): Cerebral cortex (UBERON:0000956); Hippocampus (UBERON:0001954); Cerebellum (UBERON:0002037); Blood (UBERON:0000178)
- Chemicals (CHEBI): JAK inhibitor (class); kynurenine (CHEBI:30753)

Notes on scope and limitations
- Specific complement pathway and cerebrovascular amyloid peptide signatures (CAA) in DS, as well as detailed tau-spread patterns, are rapidly evolving research areas; while supported by recent literature, such details are not fully represented in the evidence extracted here and warrant targeted review of those primary studies for integration. (araya2025interferonsignalingmodulates pages 17-18)

References (URLs and publication dates where available)
- Galbraith MD et al. Multidimensional definition of the interferonopathy of Down syndrome and its response to JAK inhibition. Science Advances. 2023-06. https://doi.org/10.1126/sciadv.adg6218 (galbraith2023multidimensionaldefinitionof pages 1-2)
- Araya P et al. Interferon signaling modulates Down syndrome–associated Alzheimer’s disease pathology in a mouse model. iScience. 2025-08. https://doi.org/10.1016/j.isci.2025.113130 (araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18)
- Russo ML, Sousa AMM, Bhattacharyya A. Consequences of trisomy 21 for brain development in Down syndrome. Nature Reviews Neuroscience. 2024-10. https://doi.org/10.1038/s41583-024-00866-2 (russo2024consequencesoftrisomy pages 17-18)
- Uguagliati B, Grilli M. Astrocytic Alterations and Dysfunction in Down Syndrome. Cells. 2024-12. https://doi.org/10.3390/cells13242037 (uguagliati2024astrocyticalterationsand pages 1-2)

Cited source IDs: (galbraith2023multidimensionaldefinitionof pages 1-2, araya2025interferonsignalingmodulates pages 1-3, araya2025interferonsignalingmodulates pages 17-18, russo2024consequencesoftrisomy pages 17-18, uguagliati2024astrocyticalterationsand pages 1-2)

References

1. (galbraith2023multidimensionaldefinitionof pages 1-2): Matthew D. Galbraith, Angela L. Rachubinski, Keith P. Smith, Paula Araya, Katherine A. Waugh, Belinda Enriquez-Estrada, Kayleigh Worek, Ross E. Granrath, Kohl T. Kinning, Neetha Paul Eduthan, Michael P. Ludwig, Elena W. Y. Hsieh, Kelly D. Sullivan, and Joaquin M. Espinosa. Multidimensional definition of the interferonopathy of down syndrome and its response to jak inhibition. Science Advances, Jun 2023. URL: https://doi.org/10.1126/sciadv.adg6218, doi:10.1126/sciadv.adg6218. This article has 52 citations and is from a highest quality peer-reviewed journal.

2. (araya2025interferonsignalingmodulates pages 1-3): Paula Araya, Brian F. Niemeyer, Kyndal A. Schade, Lauren N. Dunn, Katherine A. Waugh, Nicolas Busquet, Connie Brindley, Chrisstopher Brown, Caitlin Winkler, Hannah R Lyford, Eleanor C. Britton, Michael P Ludwig, Julie A. Siegenthaler, M. Galbraith, Joaquin M. Espinosa, and Kelly D. Sullivan. Interferon signaling modulates down syndrome-associated alzheimer’s disease pathology in a mouse model. iScience, 28:113130, Aug 2025. URL: https://doi.org/10.1016/j.isci.2025.113130, doi:10.1016/j.isci.2025.113130. This article has 0 citations and is from a peer-reviewed journal.

3. (araya2025interferonsignalingmodulates pages 17-18): Paula Araya, Brian F. Niemeyer, Kyndal A. Schade, Lauren N. Dunn, Katherine A. Waugh, Nicolas Busquet, Connie Brindley, Chrisstopher Brown, Caitlin Winkler, Hannah R Lyford, Eleanor C. Britton, Michael P Ludwig, Julie A. Siegenthaler, M. Galbraith, Joaquin M. Espinosa, and Kelly D. Sullivan. Interferon signaling modulates down syndrome-associated alzheimer’s disease pathology in a mouse model. iScience, 28:113130, Aug 2025. URL: https://doi.org/10.1016/j.isci.2025.113130, doi:10.1016/j.isci.2025.113130. This article has 0 citations and is from a peer-reviewed journal.

4. (russo2024consequencesoftrisomy pages 17-18): Matthew L. Russo, André M. M. Sousa, and Anita Bhattacharyya. Consequences of trisomy 21 for brain development in down syndrome. Nature reviews. Neuroscience, 25:740-755, Oct 2024. URL: https://doi.org/10.1038/s41583-024-00866-2, doi:10.1038/s41583-024-00866-2. This article has 21 citations.

5. (uguagliati2024astrocyticalterationsand pages 1-2): Beatrice Uguagliati and Mariagrazia Grilli. Astrocytic alterations and dysfunction in down syndrome: focus on neurogenesis, synaptogenesis, and neural circuits formation. Cells, 13:2037, Dec 2024. URL: https://doi.org/10.3390/cells13242037, doi:10.3390/cells13242037. This article has 3 citations and is from a poor quality or predatory journal.

6. (risgaard2025molecularandcellular pages 31-33): Ryan D. Risgaard, Kalpana Hanthanan Arachchilage, Sara A. Knaack, Masoumeh Hosseini, Rachel J. Chen, Pubudu Kumarage, Danielle K. Schmidt, Xiang Huang, Jie Sheng, Carlos J. Wang, Elisa Giusti, Shuang Liu, Su-Chun Zhang, Daifeng Wang, Anita Bhattacharyya, and Andre M. M. Sousa. Molecular and cellular processes disrupted in the early postnatal down syndrome prefrontal cortex. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.06.30.662385, doi:10.1101/2025.06.30.662385. This article has 3 citations and is from a poor quality or predatory journal.

7. (araya2025interferonsignalingmodulates pages 18-18): Paula Araya, Brian F. Niemeyer, Kyndal A. Schade, Lauren N. Dunn, Katherine A. Waugh, Nicolas Busquet, Connie Brindley, Chrisstopher Brown, Caitlin Winkler, Hannah R Lyford, Eleanor C. Britton, Michael P Ludwig, Julie A. Siegenthaler, M. Galbraith, Joaquin M. Espinosa, and Kelly D. Sullivan. Interferon signaling modulates down syndrome-associated alzheimer’s disease pathology in a mouse model. iScience, 28:113130, Aug 2025. URL: https://doi.org/10.1016/j.isci.2025.113130, doi:10.1016/j.isci.2025.113130. This article has 0 citations and is from a peer-reviewed journal.

8. (llambrich2024pleiotropiceffectsof pages 34-35): Sergi Llambrich, Birger Tielemans, Ellen Saliën, Marta Atzori, Kaat Wouters, Vicky Van Bulck, Mark Platt, Laure Vanherp, Nuria Gallego Fernandez, Laura Grau de la Fuente, Harish Poptani, Lieve Verlinden, Uwe Himmelreich, Anca Croitor, Catia Attanasio, Zsuzsanna Callaerts-Vegh, Willy Gsell, Neus Martínez-Abadías, and Greetje Vande Velde. Pleiotropic effects of trisomy and pharmacologic modulation on structural, functional, molecular, and genetic systems in a down syndrome mouse model. eLife, Mar 2024. URL: https://doi.org/10.7554/elife.89763.3, doi:10.7554/elife.89763.3. This article has 4 citations and is from a domain leading peer-reviewed journal.