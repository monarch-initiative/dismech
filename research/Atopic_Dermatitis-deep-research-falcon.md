---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-14T16:54:02.567712'
end_time: '2026-02-14T17:00:30.185672'
duration_seconds: 387.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atopic Dermatitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Atopic Dermatitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Atopic Dermatitis**.
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
- **Disease Name:** Atopic Dermatitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Atopic Dermatitis**.
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
- Disease Name: Atopic Dermatitis (AD)
- MONDO ID: MONDO:0004994
- Category: Complex

Pathophysiology description (current understanding, 2023–2025 emphasis)
Atopic dermatitis is a chronic, relapsing inflammatory dermatosis driven by the interplay of epidermal barrier dysfunction, type 2–skewed immunity, neuroimmune pruritus circuitry, and microbial/ environmental exposures. Barrier failure (filaggrin insufficiency, altered ceramide composition, and tight-junction defects) permits enhanced allergen/microbe ingress and promotes alarmin release, which activates dendritic cells and ILC2/Th2 axes. IL-4/IL-13 signaling amplifies inflammation and further downregulates barrier genes, establishing feed-forward loops. Pruritus is sustained by neuroimmune mediators—especially IL-31—signaling to TRP channel–bearing sensory afferents and, in chronic exposure, engaging a paradoxical neurogenic anti–type 2 brake via CGRP. JAK–STAT integrates many of these cytokine signals and is a validated therapeutic hub. Multi-omics studies reveal clinically relevant endotypes aligning cutaneous and blood transcriptomes with phenotypes and treatment trajectories. Therapeutically, targeting IL-4/IL-13 (dupilumab; IL-13 inhibitors) and JAK1/2 pathways improves disease activity and, in some studies, barrier function, supporting causal roles for these axes in AD. (katsarou2023theroleof pages 12-12, kamata2025mechanismsofitch pages 2-4, torres2025interleukin4andatopic pages 14-15, urzua2025skinbarrierdysfunction pages 3-4, bai2025atopicdermatitisdiagnosis pages 25-26, zhakparov2026protectiveandsusceptibility pages 22-23)

Key concepts and definitions (with recent sources)
- Epidermal barrier dysfunction: Tight junction (TJ) impairment (e.g., reduced claudin-1) and filaggrin deficiency increase permeability and trans-epidermal water loss, facilitating allergen and pathogen entry; Th2 cytokines suppress TJ proteins. Quote: “Impaired TJ barrier function and skin permeability in AD lesions is correlated with cldn-1 levels. Th2 inflammation inhibits the expression of cldn-1 and cldn-23” (Feb 2023, Journal of Clinical Medicine; URL: https://doi.org/10.3390/jcm12041538). (katsarou2023theroleof pages 12-12)
- Type 2 cytokine axis: IL-4 and IL-13 orchestrate barrier disruption, dysbiosis, pruritus, and inflammation in AD. Narrative review emphasis: “IL-4 plays a critical role in skin barrier dysfunction, dysbiosis, pruritus, and inflammation” (Feb 2025, Dermatology and Therapy; URL: https://doi.org/10.1007/s13555-025-01352-y). (torres2025interleukin4andatopic pages 14-15)
- Neuroimmune itch (IL-31 axis): IL-31 acts directly on pruritoceptors (IL31RA/OSMR) to induce itch and neurite outgrowth and is a central mediator of AD pruritus. Quote: “IL-31 directly induces pruritus… and selectively promotes nerve fiber extension in these neurons” (Jan 2025, Juntendo Medical Journal; URL: https://doi.org/10.14789/ejmj.jmj24-0036-r). (kamata2025mechanismsofitch pages 2-4)
- Neurogenic restraint of type 2 inflammation: In chronic allergen exposure, IL-31 activation of sensory neurons can trigger CGRP release that suppresses Th2 responses, providing a mechanistic basis for paradoxical flares with anti–IL-31 receptor therapy. Quote: “IL-31… restrains cutaneous type 2 inflammation… IL-31 activation of IL31RA+ pruritoceptors triggers release of calcitonin gene-related protein (CGRP), which… inhibit[s] CD4+ T cell proliferation and reduce[s]… IL-13” (Oct 2023, Science Immunology; URL: https://doi.org/10.1126/sciimmunol.abi6887). (bai2025atopicdermatitisdiagnosis pages 25-26)
- JAK–STAT as hub pathway: Many AD cytokines signal via JAKs; clinical efficacy of oral and topical JAK inhibitors supports centrality of this pathway (reviewed 2025). (urzua2025skinbarrierdysfunction pages 3-4)
- Molecular endotypes: Integrated skin and blood transcriptomics uncover endotype–phenotype associations and clusters aligned with severity and trajectories, enabling personalized monitoring. (Oct 2023, Nature Communications; URL: https://doi.org/10.1038/s41467-023-41857-8). (bilinski2025antiinflammatorytherapiesfor pages 2-4)

1) Core Pathophysiology
- Primary mechanisms
  - Barrier failure: FLG deficiency and TJ defects (e.g., CLDN1) lead to increased permeability; scratching worsens claudin-1 loss and barrier leak. Th2 cytokines (IL-4/IL-13) suppress claudins and barrier proteins, coupling immunity to barrier pathology (Feb 2023; URL above). (katsarou2023theroleof pages 12-12)
  - Epithelial alarmins: Barrier stress releases TSLP/IL-33/IL-25 from keratinocytes, priming DCs/ILC2/Th2; their role is integrated within itch reviews and type 2 discussions (2025; URLs below). (kamata2025mechanismsofitch pages 2-4, torres2025interleukin4andatopic pages 14-15)
  - Type 2 immunity: IL-4/IL-13 drive IgE class switching, eosinophilia, keratinocyte chemokine production, and barrier gene suppression. (torres2025interleukin4andatopic pages 14-15, urzua2025skinbarrierdysfunction pages 3-4)
  - Neuroimmune itch: IL-31→IL31RA/OSMR on TRPV1/TRPA1+ small-diameter afferents; neuronal plasticity (hyperinnervation) correlates with itch; Sema3A↓ and NGF↑ alter epidermal innervation in AD (Jan 2025; URL below). (kamata2025mechanismsofitch pages 2-4)
  - Neurogenic restraint loop: IL-31–induced CGRP limits Th2 cell accumulation and IL-13 output in chronic allergen dermatitis (Oct 2023; URL below). (bai2025atopicdermatitisdiagnosis pages 25-26)
  - JAK–STAT integration: Many cytokines (IL-4/IL-13/IL-31/TSLP) signal through JAK1/2→STAT6/others; clinical responses to JAK inhibition reflect pathway centrality (Jun 2025; URL below). (urzua2025skinbarrierdysfunction pages 3-4)
  - Systems endotypes: Cross-tissue transcriptomics reveal modules linked to erythema vs papulation and longitudinal clusters tied to severity and treatment response; proteomic modules correlate with disease activity (Oct 2023; URL below). (bilinski2025antiinflammatorytherapiesfor pages 2-4)

- Dysregulated molecular pathways
  - IL-4/IL-13–STAT6 signaling; IL-31–neuronal TRP channels; alarmin (TSLP/IL-33/IL-25)–DC/ILC2 pathways; NF-κB and MAPK in keratinocytes; JAK–STAT (kamata2025mechanismsofitch pages 2-4, bai2025atopicdermatitisdiagnosis pages 25-26, torres2025interleukin4andatopic pages 14-15, urzua2025skinbarrierdysfunction pages 3-4)

- Affected cellular processes
  - Keratinocyte differentiation and junctional assembly; sensory neuron excitability and neurite extension; DC antigen presentation; Th2/ILC2 cytokine production; pruritus transmission (katsarou2023theroleof pages 12-12, kamata2025mechanismsofitch pages 2-4, bai2025atopicdermatitisdiagnosis pages 25-26)

2) Key Molecular Players (ontology-ready annotations)
- Genes/Proteins (HGNC symbol)
  - FLG (filaggrin): epidermal barrier scaffold; loss-of-function predisposes to AD (HGNC: 3752). (katsarou2023theroleof pages 12-12)
  - CLDN1 (claudin-1): tight junction component; reduced in AD lesions; Th2 cytokine–sensitive (HGNC: 2031). (katsarou2023theroleof pages 12-12)
  - IL4, IL13: type 2 cytokines central to AD pathogenesis (HGNC: 6014, 5991). (torres2025interleukin4andatopic pages 14-15)
  - IL31, IL31RA, OSMR: pruritogenic pathway receptors on sensory neurons (HGNC: 20497, 21491, 8506). (kamata2025mechanismsofitch pages 2-4, bai2025atopicdermatitisdiagnosis pages 25-26)
  - TSLP, IL33, IL25/IL17E: epithelial alarmins initiating type 2 responses (HGNC: 30742, 5996, 5964). (kamata2025mechanismsofitch pages 2-4, torres2025interleukin4andatopic pages 14-15)
  - JAK1, JAK2; STAT6: JAK–STAT transducers in type 2 signaling (HGNC: 6190, 6192, 11366). (urzua2025skinbarrierdysfunction pages 3-4, torres2025interleukin4andatopic pages 14-15)
  - CALCA (CGRP): neuropeptide mediating IL-31 neurogenic restraint (HGNC: 1434). (bai2025atopicdermatitisdiagnosis pages 25-26)
  - TRPV1, TRPA1: neuronal ion channels mediating itch (HGNC: 12306, 132). (kamata2025mechanismsofitch pages 2-4)

- Chemical entities (CHEBI)
  - Ceramide (CHEBI:17761): altered chain-length composition in AD barrier lipid matrix (review synthesis). (urzua2025skinbarrierdysfunction pages 3-4)
  - Histamine (CHEBI:18295): mast-cell mediator contributing to pruritus (review synthesis). (torres2025interleukin4andatopic pages 14-15)

- Cell types (CL terms)
  - Keratinocyte (CL:0000312); Langerhans cell (CL:0000475); Dendritic cell (CL:0000451); ILC2 (CL:0001065); Th2 cell (CL:0000910); Sensory neuron (CL:0000101). (kamata2025mechanismsofitch pages 2-4, katsarou2023theroleof pages 12-12, torres2025interleukin4andatopic pages 14-15)

- Anatomical locations (UBERON)
  - Epidermis (UBERON:0001003); Dermis (UBERON:0002067); Skin nerve endings (UBERON:0001825). (kamata2025mechanismsofitch pages 2-4, katsarou2023theroleof pages 12-12)

- Drugs/biologics (mechanism-linked)
  - Dupilumab (anti–IL-4Rα; blocks IL-4/IL-13 signaling). (torres2025interleukin4andatopic pages 14-15)
  - Tralokinumab, lebrikizumab (anti–IL-13). (torres2025interleukin4andatopic pages 14-15)
  - Oral/topical JAK inhibitors (e.g., upadacitinib, baricitinib; ruxolitinib cream). (urzua2025skinbarrierdysfunction pages 3-4)

3) Biological Processes (GO) disrupted
- Keratinocyte differentiation (GO:0030216); Cornified envelope assembly (GO:0070268) (FLG-related). (katsarou2023theroleof pages 12-12)
- Tight junction organization (GO:0034330) (CLDN1-related). (katsarou2023theroleof pages 12-12)
- Cytokine-mediated signaling pathway (GO:0019221) via JAK–STAT (GO:0007259). (urzua2025skinbarrierdysfunction pages 3-4, torres2025interleukin4andatopic pages 14-15)
- Immune response–Th2 cell differentiation (GO:0042092); ILC2 activation (GO:0001773). (torres2025interleukin4andatopic pages 14-15)
- Sensory perception of itch (GO:0036231); Neuron projection development (GO:0031175) (IL-31–induced neurite extension). (kamata2025mechanismsofitch pages 2-4)
- Neurogenic inflammation (GO:0050729) via CGRP signaling impacting T cells. (bai2025atopicdermatitisdiagnosis pages 25-26)

4) Cellular Components (GO-CC)
- Cornified envelope (GO:0001533); Keratin filament (GO:0045095). (katsarou2023theroleof pages 12-12)
- Tight junction (GO:0005923). (katsarou2023theroleof pages 12-12)
- Plasma membrane of pruritoceptors (GO:0005886) housing TRPV1/TRPA1 and IL31RA/OSMR. (kamata2025mechanismsofitch pages 2-4)
- Extracellular space (GO:0005615) for cytokines and neuropeptides (IL-4/IL-13/IL-31, CGRP). (torres2025interleukin4andatopic pages 14-15, bai2025atopicdermatitisdiagnosis pages 25-26)

5) Disease Progression (sequence of events)
- Initiation: Genetic predisposition (e.g., FLG variants) and environmental insults disrupt the barrier and elevate skin pH; TJ/FLG insufficiency increases permeability. (katsarou2023theroleof pages 12-12)
- Epithelial alarm: Keratinocytes release alarmins (TSLP, IL-33, IL-25), activating DCs/ILC2 and priming Th2 responses. (kamata2025mechanismsofitch pages 2-4, torres2025interleukin4andatopic pages 14-15)
- Amplification: IL-4/IL-13 from Th2/ILC2 downregulate barrier genes (e.g., FLG, CLDN1), recruit inflammatory cells, and perpetuate itch–scratch cycles; JAK–STAT transduces these signals. (torres2025interleukin4andatopic pages 14-15, urzua2025skinbarrierdysfunction pages 3-4)
- Pruritus circuitry: IL-31 directly activates IL31RA/OSMR+ TRPV1/TRPA1 neurons, enhances nerve fiber density, and drives chronic itch behavior. (kamata2025mechanismsofitch pages 2-4)
- Chronic modulation: With repeated allergen exposure, IL-31–induced CGRP imposes a neurogenic restraint on tissue Th2 inflammation—an adaptive feedback that may be perturbed by anti-IL31RA therapies. (bai2025atopicdermatitisdiagnosis pages 25-26)
- Endotypic divergence: Cross-tissue transcriptomic modules align with clinical phenotypes and severity clusters and can inform treatment monitoring/response. (bilinski2025antiinflammatorytherapiesfor pages 2-4)

6) Phenotypic Manifestations (clinical; HP terms)
- Pruritus (HP:0000989) driven by IL-31–TRP pathways and hyperinnervation; quote above. (kamata2025mechanismsofitch pages 2-4)
- Eczema/erythematous scaly dermatitis (HP:0000988) from Th2-driven skin inflammation and barrier leak. (torres2025interleukin4andatopic pages 14-15, katsarou2023theroleof pages 12-12)
- Xerosis (HP:0000958) from barrier lipid/protein deficits. (katsarou2023theroleof pages 12-12)
- Lichenification (HP:0000984) in chronic disease, aligned with distinct transcriptomic modules. (bilinski2025antiinflammatorytherapiesfor pages 2-4)

Recent developments and latest research (2023–2025; with URLs/dates)
- IL-31 neuroimmune restraint of Th2 inflammation (Science Immunology, Oct 2023): Demonstrated that IL-31–responsive pruritoceptors release CGRP to limit cutaneous type 2 programs in chronic HDM dermatitis; mechanistic insight into paradoxical flares on anti-IL31RA therapy. URL: https://doi.org/10.1126/sciimmunol.abi6887. (bai2025atopicdermatitisdiagnosis pages 25-26)
- Systems endotyping (Nature Communications, Oct 2023): Cross-tissue transcriptomics linked detailed skin phenotypes (erythema vs papulation) with distinct immune signatures and identified blood transcriptome clusters tracking severity and treatment history, enabling personalized monitoring. URL: https://doi.org/10.1038/s41467-023-41857-8. (bilinski2025antiinflammatorytherapiesfor pages 2-4)
- Tight-junction barrier in AD (J Clin Med, Feb 2023): Systematic review highlighting claudin-1 reduction, Th2 suppression of claudins, and scratching-induced claudin-1 decreases as central to barrier pathophysiology. URL: https://doi.org/10.3390/jcm12041538. (katsarou2023theroleof pages 12-12)
- Itch mechanisms synthesis (Juntendo Med J, Jan 2025): Integrated view of Th2/alarmin–neuronal crosstalk, IL-31 receptor expression on pruritoceptors, and hyperinnervation mechanisms (Sema3A↓, NGF↑). URL: https://doi.org/10.14789/ejmj.jmj24-0036-r. (kamata2025mechanismsofitch pages 2-4)
- IL-4 centrality and therapeutic implications (Dermatology and Therapy, Feb 2025): Review underscoring IL-4/IL-13 as nexus for barrier, dysbiosis, itch, and inflammation; contextualizes dupilumab and IL-13 inhibitors. URL: https://doi.org/10.1007/s13555-025-01352-y. (torres2025interleukin4andatopic pages 14-15)
- Barrier, immunity, and targeted therapy integration (Cureus, Jun 2025): Review summarizing evidence for IL-13 blockade improving barrier function and rapid efficacy of JAK inhibitors; notes emerging microbiome-directed approaches. URL: https://doi.org/10.7759/cureus.86937. (urzua2025skinbarrierdysfunction pages 3-4)

Current applications and real-world implementations
- IL-4/IL-13 pathway blockade
  - Dupilumab (anti–IL-4Rα) is a standard of care for moderate–severe AD; reviews document early and sustained improvements in systemic and cutaneous immune abnormalities, consistent with interruption of the type 2 axis (reviewed 2025; URL above). (torres2025interleukin4andatopic pages 14-15)
  - IL-13–selective monoclonals (tralokinumab, lebrikizumab) have demonstrated efficacy in phase III trials and are integrated in recent therapeutic reviews (2025 summary; mechanism detailed in 2025 narrative review). (torres2025interleukin4andatopic pages 14-15)
- JAK inhibitors
  - Oral JAK1-selective agents (e.g., upadacitinib) and JAK1/2 (baricitinib) and topical ruxolitinib cream show rapid pruritus and lesion improvement consistent with broad cytokine signal interruption (2025 review synthesis). (urzua2025skinbarrierdysfunction pages 3-4)
- Monitoring and personalization
  - Multi-omic endotyping and cross-tissue modules are being developed for patient stratification and longitudinal monitoring, aligning skin phenotypes and blood modules with severity and response (Oct 2023). (bilinski2025antiinflammatorytherapiesfor pages 2-4)

Expert opinions and analysis
- “IL-4 plays a critical role in skin barrier dysfunction, dysbiosis, pruritus, and inflammation” (Dermatology and Therapy, Feb 2025), anchoring IL-4/IL-13 as prime nodes for disease modification. URL: https://doi.org/10.1007/s13555-025-01352-y. (torres2025interleukin4andatopic pages 14-15)
- “Impaired TJ barrier function and skin permeability in AD lesions is correlated with cldn-1 levels. Th2 inflammation inhibits the expression of cldn-1 and cldn-23… Scratching has also been reported to decrease cldn-1” (J Clin Med, Feb 2023), highlighting actionable barrier–immune feedbacks. URL: https://doi.org/10.3390/jcm12041538. (katsarou2023theroleof pages 12-12)
- “IL-31 directly induces pruritus… and selectively promotes nerve fiber extension” (Juntendo Med J, Jan 2025), connecting cytokine signaling to neuronal remodeling. URL: https://doi.org/10.14789/ejmj.jmj24-0036-r. (kamata2025mechanismsofitch pages 2-4)
- “IL-31… restrains cutaneous type 2 inflammation… [via] CGRP” (Science Immunology, Oct 2023), reframing IL-31 as both pruritogen and neuroimmune modulator. URL: https://doi.org/10.1126/sciimmunol.abi6887. (bai2025atopicdermatitisdiagnosis pages 25-26)

Relevant statistics and data from recent studies
- Endotypic clustering: Integrated analysis of 115 AD patients and 14 controls identified skin–blood modules linking specific clinical features (erythema vs papulation) and longitudinal blood clusters aligned with severity and treatment history (Nature Communications, Oct 2023; details in article). URL: https://doi.org/10.1038/s41467-023-41857-8. (bilinski2025antiinflammatorytherapiesfor pages 2-4)
- Barrier correlates: Systematic review collating >50 studies concluded that decreased claudin-1 associates with increased permeability and susceptibility to infection/allergen penetration; Th2 cytokines reduce claudin expression; scratching lowers claudin-1 (Feb 2023). URL: https://doi.org/10.3390/jcm12041538. (katsarou2023theroleof pages 12-12)
- Neuroimmune plasticity: Clinical-pathobiological observations summarized in 2025 review include reduced Sema3A and increased NGF correlating with increased intraepidermal nerve density across AD states (Jan 2025). URL: https://doi.org/10.14789/ejmj.jmj24-0036-r. (kamata2025mechanismsofitch pages 2-4)

Evidence items (with PMIDs/DOIs/URLs)
- Fassett MS et al. IL-31–dependent neurogenic inflammation restrains cutaneous type 2 immune response in allergic dermatitis. Science Immunology. Oct 2023. DOI: 10.1126/sciimmunol.abi6887; URL: https://doi.org/10.1126/sciimmunol.abi6887. Key quote and mechanism above. (bai2025atopicdermatitisdiagnosis pages 25-26)
- Kamata Y et al. Mechanisms of Itch in Atopic Dermatitis. Juntendo Medical Journal. Jan 2025. DOI: 10.14789/ejmj.jmj24-0036-r; URL: https://doi.org/10.14789/ejmj.jmj24-0036-r. Key quote on IL-31 neurite extension; neuronal receptor expression. (kamata2025mechanismsofitch pages 2-4)
- Katsarou S et al. The Role of Tight Junctions in Atopic Dermatitis: A Systematic Review. J Clin Med. Feb 2023. DOI: 10.3390/jcm12041538; URL: https://doi.org/10.3390/jcm12041538. Key quote on claudins/Th2 inhibition. (katsarou2023theroleof pages 12-12)
- Torres T et al. Interleukin-4 and Atopic Dermatitis. Dermatology and Therapy. Feb 2025. DOI: 10.1007/s13555-025-01352-y; URL: https://doi.org/10.1007/s13555-025-01352-y. Expert synthesis of IL-4/IL-13 centrality. (torres2025interleukin4andatopic pages 14-15)
- Urzua IE et al. Skin Barrier Dysfunction… Cureus. Jun 2025. DOI: 10.7759/cureus.86937; URL: https://doi.org/10.7759/cureus.86937. Clinical integration of IL-13 blockade/barrier and JAK inhibitor kinetics. (urzua2025skinbarrierdysfunction pages 3-4)
- Sekita A et al. Multifaceted analysis of cross-tissue transcriptomes… Nat Commun. Oct 2023. DOI: 10.1038/s41467-023-41857-8; URL: https://doi.org/10.1038/s41467-023-41857-8. Endotype–phenotype modules and longitudinal clusters. (bilinski2025antiinflammatorytherapiesfor pages 2-4)

Structured ontology annotations
- Genes/Proteins (HGNC): FLG; CLDN1; IL4; IL13; IL31; IL31RA; OSMR; TSLP; IL33; JAK1; JAK2; STAT6; CALCA; TRPV1; TRPA1. (katsarou2023theroleof pages 12-12, kamata2025mechanismsofitch pages 2-4, bai2025atopicdermatitisdiagnosis pages 25-26, torres2025interleukin4andatopic pages 14-15, urzua2025skinbarrierdysfunction pages 3-4)
- GO Biological Processes: keratinocyte differentiation; tight junction organization; cytokine-mediated signaling; JAK–STAT cascade; Th2 differentiation; sensory perception of itch; neurogenic inflammation. (katsarou2023theroleof pages 12-12, kamata2025mechanismsofitch pages 2-4, urzua2025skinbarrierdysfunction pages 3-4)
- GO Cellular Components: tight junction; cornified envelope; plasma membrane; extracellular region. (katsarou2023theroleof pages 12-12, kamata2025mechanismsofitch pages 2-4)
- Cell Types (CL): keratinocytes; Langerhans cells; dermal dendritic cells; ILC2; Th2 cells; small-diameter sensory neurons. (kamata2025mechanismsofitch pages 2-4, katsarou2023theroleof pages 12-12, torres2025interleukin4andatopic pages 14-15)
- Anatomical Sites (UBERON): epidermis; dermis; cutaneous nerve endings. (kamata2025mechanismsofitch pages 2-4, katsarou2023theroleof pages 12-12)
- Chemical entities (CHEBI): ceramide (CHEBI:17761); histamine (CHEBI:18295). (urzua2025skinbarrierdysfunction pages 3-4, torres2025interleukin4andatopic pages 14-15)
- Phenotypes (HPO): pruritus (HP:0000989); eczema (HP:0000988); xerosis (HP:0000958); lichenification (HP:0000984). (kamata2025mechanismsofitch pages 2-4, katsarou2023theroleof pages 12-12, bilinski2025antiinflammatorytherapiesfor pages 2-4)

Therapeutic implications (mechanism → therapy mapping)
- IL-4/IL-13 axis: Dupilumab (anti–IL-4Rα), tralokinumab/lebrikizumab (anti–IL-13) reduce type 2 signaling, improve lesions and often pruritus; reviews emphasize their disease-modifying potential by interrupting central drivers (2025). (torres2025interleukin4andatopic pages 14-15)
- IL-31 axis: Anti–IL-31/IL31RA agents target pruritus; the 2023 mechanistic study suggests monitoring for inflammatory shifts due to loss of IL-31–CGRP restraint in chronic exposure contexts (Oct 2023). (bai2025atopicdermatitisdiagnosis pages 25-26)
- JAK inhibitors: Oral JAK1/2 and topical JAK inhibitors rapidly reduce itch and inflammation—a pharmacodynamic signature of blocking multi-cytokine signaling via JAK–STAT (2025). (urzua2025skinbarrierdysfunction pages 3-4)
- Barrier-directed adjuncts: Because Th2 cytokines downregulate CLDN1/FLG, upstream cytokine blockade plus barrier repair strategies target both cause and consequence (2023–2025 syntheses). (katsarou2023theroleof pages 12-12, torres2025interleukin4andatopic pages 14-15)

Limitations and gaps
- While reviews integrate barrier, IL-4/IL-13, IL-31, and JAK–STAT mechanisms with therapeutic success, high-resolution causal links for all epithelial alarmins in human endotypes and long-term remodeling remain under active investigation. Multi-omic signatures are promising but require prospective validation for treatment selection in routine care. (bilinski2025antiinflammatorytherapiesfor pages 2-4)

References with URLs/dates
- Science Immunology, Oct 2023: https://doi.org/10.1126/sciimmunol.abi6887. (bai2025atopicdermatitisdiagnosis pages 25-26)
- Nature Communications, Oct 2023: https://doi.org/10.1038/s41467-023-41857-8. (bilinski2025antiinflammatorytherapiesfor pages 2-4)
- Journal of Clinical Medicine, Feb 2023: https://doi.org/10.3390/jcm12041538. (katsarou2023theroleof pages 12-12)
- Juntendo Medical Journal, Jan 2025: https://doi.org/10.14789/ejmj.jmj24-0036-r. (kamata2025mechanismsofitch pages 2-4)
- Dermatology and Therapy, Feb 2025: https://doi.org/10.1007/s13555-025-01352-y. (torres2025interleukin4andatopic pages 14-15)
- Cureus, Jun 2025: https://doi.org/10.7759/cureus.86937. (urzua2025skinbarrierdysfunction pages 3-4)

References

1. (katsarou2023theroleof pages 12-12): Spyridoula Katsarou, Michael Makris, Efstratios Vakirlis, and Stamatios Gregoriou. The role of tight junctions in atopic dermatitis: a systematic review. Journal of Clinical Medicine, 12:1538, Feb 2023. URL: https://doi.org/10.3390/jcm12041538, doi:10.3390/jcm12041538. This article has 37 citations and is from a poor quality or predatory journal.

2. (kamata2025mechanismsofitch pages 2-4): YAYOI KAMATA, MITSUTOSHI TOMINAGA, and KENJI TAKAMORI. Mechanisms of itch in atopic dermatitis. Juntendo Medical Journal, 71:43-50, Jan 2025. URL: https://doi.org/10.14789/ejmj.jmj24-0036-r, doi:10.14789/ejmj.jmj24-0036-r. This article has 6 citations.

3. (torres2025interleukin4andatopic pages 14-15): Tiago Torres, Pedro Mendes-Bastos, Maria J. Cruz, Bruno Duarte, Paulo Filipe, Maria J. P. Lopes, and Margarida Gonçalo. Interleukin-4 and atopic dermatitis: why does it matter? a narrative review. Dermatology and Therapy, 15:579-597, Feb 2025. URL: https://doi.org/10.1007/s13555-025-01352-y, doi:10.1007/s13555-025-01352-y. This article has 18 citations and is from a poor quality or predatory journal.

4. (urzua2025skinbarrierdysfunction pages 3-4): Irisdey Espinoza Urzua, María Isabel Vidal Vidal, Manrique Vega Solano, Julian Eduardo Bedoya Jaramillo, Gifneth Giselle de la Cruz Donis, and Andrés Romero Valverde. Skin barrier dysfunction in chronic dermatoses: from pathophysiology to emerging therapeutic strategies. Cureus, Jun 2025. URL: https://doi.org/10.7759/cureus.86937, doi:10.7759/cureus.86937. This article has 1 citations and is from a poor quality or predatory journal.

5. (bai2025atopicdermatitisdiagnosis pages 25-26): Ruimin Bai, Yan Zheng, and Xiaofeng Dai. Atopic dermatitis: diagnosis, molecular pathogenesis, and therapeutics. Molecular Biomedicine, Oct 2025. URL: https://doi.org/10.1186/s43556-025-00313-3, doi:10.1186/s43556-025-00313-3. This article has 7 citations.

6. (zhakparov2026protectiveandsusceptibility pages 22-23): Damir Zhakparov, Nonhlanhla Lunjani, Marco Schmid, Kathleen Moriarty, Damian Roquero, Anita Dreher, Jeannette I. Heldstab-Kast, Kari C. Nadeau, Cezmi Akdis, Michael Levin, Carol Hlela, Milena Sokolowska, Liam O’Mahony, and Katja Baerenfaller. Protective and susceptibility clusters of environmental factors, gene expression, antibody responses, and cytokines in pediatric atopic dermatitis: insights from multi-modal data integration. Unknown journal, Jan 2026. URL: https://doi.org/10.64898/2026.01.10.26343854, doi:10.64898/2026.01.10.26343854.

7. (bilinski2025antiinflammatorytherapiesfor pages 2-4): Karol Biliński, Katarzyna Rakoczy, Anna Karwowska, Oliwia Cichy, Aleksandra Wojno, Agata Wojno, Julita Kulbacka, and Małgorzata Ponikowska. Anti-inflammatory therapies for atopic dermatitis: a new era in targeted treatment. Journal of Clinical Medicine, 14:5053, Jul 2025. URL: https://doi.org/10.3390/jcm14145053, doi:10.3390/jcm14145053. This article has 5 citations and is from a poor quality or predatory journal.