---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T11:16:41.707160'
end_time: '2026-01-08T11:24:37.159706'
duration_seconds: 475.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fabry disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Fabry disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fabry disease**.
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
- **Disease Name:** Fabry disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Fabry disease**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Fabry disease
- MONDO ID: MONDO:0009921
- Category: Mendelian

Pathophysiology description
Fabry disease is an X‑linked lysosomal storage disorder caused by pathogenic variants in GLA that reduce or abolish α‑galactosidase A activity, leading to lysosomal accumulation of glycosphingolipids, principally globotriaosylceramide (Gb3) and its deacylated derivative globotriaosylsphingosine (lyso‑Gb3). Substrate accumulation initiates a network of stress responses: endoplasmic reticulum (ER) stress and the unfolded protein response (UPR) from misfolded GLA variants; impaired autophagic flux and broader lysosomal dysfunction; mitochondrial injury with bioenergetic failure and reactive oxygen species (ROS) production; and activation of innate immune pathways including NF‑κB and the NLRP3 inflammasome. Inflammatory mediators (e.g., IL‑1β, IL‑6, TNF‑α) and complement activation fragments (C3a, C5a) propagate endothelial dysfunction, leukocyte adhesion, and tissue injury. Profibrotic signaling (notably TGF‑β) drives extracellular matrix deposition and fibrosis that can become partially independent of the initiating lipid stimulus. Organ manifestations arise from injury to vulnerable cell types, particularly podocytes in kidney, cardiomyocytes and the cardiac conduction system, vascular endothelium and smooth muscle, and neurons; these processes underlie proteinuric chronic kidney disease, hypertrophic/fibrotic cardiomyopathy with arrhythmia risk, and cerebrovascular disease. Notably, disease drivers extend beyond storage alone: podocyte injury persists despite Gb3 clearance under enzyme replacement therapy (ERT), with α‑synuclein (SNCA) accumulation implicated as a lysosomal toxicity mediator. Recent work also highlights bioenergetic deficits and oxidative stress correlating with cardiac hypertrophy. (feriozzi2024theinflammatorypathogenetic pages 9-11, feriozzi2024theinflammatorypathogenetic pages 7-9, kurdi2024inflammationinfabry pages 8-10, snanoudj2024genomewideexpressionanalysis pages 6-8, feriozzi2024theinflammatorypathogenetic pages 5-7)

Core Pathophysiology
- Primary mechanisms
  - GLA deficiency → Gb3/lyso‑Gb3 accumulation in lysosomes; lyso‑Gb3 is closely associated with disease severity and exerts direct cytotoxicity on podocytes and neurons. (feriozzi2024theinflammatorypathogenetic pages 9-11)
  - ER stress/UPR due to misfolded α‑Gal A variants; persistent UPR activates pro‑apoptotic and inflammatory pathways (NF‑κB/MAPK). (kurdi2024inflammationinfabry pages 8-10, feriozzi2024theinflammatorypathogenetic pages 7-9)
  - Autophagy impairment and global lysosomal dysfunction with accumulation of damaged proteins/organelles. (kurdi2024inflammationinfabry pages 8-10, snanoudj2024genomewideexpressionanalysis pages 6-8)
  - Mitochondrial dysfunction and oxidative stress: reduced ATP/PCr, complex I/III impairment, elevated oxidative damage; lyso‑Gb3 can enhance ROS via RIPK3 signaling. (kurdi2024inflammationinfabry pages 8-10)
  - Inflammation and complement: activation of innate immune pathways including NLRP3 (IL‑1β/IL‑18, gasdermin D), and elevated C3a/C5a despite ERT, especially with anti‑drug antibodies. (kurdi2024inflammationinfabry pages 8-10, coelhoribeiro2024inflammationandexosomes pages 15-16)
  - Endothelial dysfunction: adhesion molecule upregulation (VCAM1/ICAM1), eNOS uncoupling, microvascular remodeling; vascular smooth muscle proliferation attributed to lyso‑Gb3. (coelhoribeiro2024inflammationandexosomes pages 15-16, gervasarruga2024insilicomodeling pages 7-8, feriozzi2024theinflammatorypathogenetic pages 5-7)
  - Profibrotic signaling: TGF‑β–linked extracellular matrix deposition in kidney (mesangial, interstitial) and heart. (feriozzi2024theinflammatorypathogenetic pages 9-11, feriozzi2024theinflammatorypathogenetic pages 7-9)
  - Organ‑specific injury: persistent podocyte lysosomal dysfunction and damage despite ERT, mediated in part by α‑synuclein accumulation. (feriozzi2024theinflammatorypathogenetic pages 5-7)

- Dysregulated molecular pathways
  - NF‑κB, MAPK, Notch1 activation by Gb3/lyso‑Gb3; NLRP3 inflammasome; impaired mTOR activity with autophagic flux disruption; oxidative stress pathways; complement cascade activation. (feriozzi2024theinflammatorypathogenetic pages 7-9, kurdi2024inflammationinfabry pages 8-10, snanoudj2024genomewideexpressionanalysis pages 6-8, coelhoribeiro2024inflammationandexosomes pages 15-16)

- Affected cellular processes
  - Protein folding and ER quality control (UPR/ERAD), autophagy/lysophagy, mitophagy and mitochondrial respiration, endothelial nitric oxide signaling, leukocyte adhesion/extravasation, extracellular matrix turnover and fibrosis. (kurdi2024inflammationinfabry pages 8-10, snanoudj2024genomewideexpressionanalysis pages 6-8, coelhoribeiro2024inflammationandexosomes pages 15-16, feriozzi2024theinflammatorypathogenetic pages 9-11)

Key Molecular Players
- Genes/Proteins (HGNC or equivalent)
  - GLA (α‑galactosidase A): causal; deficiency initiates substrate accumulation; target of ERT/chaperone/gene therapy. (feriozzi2024theinflammatorypathogenetic pages 9-11)
  - SNCA (α‑synuclein): mediates persistent lysosomal dysfunction and podocyte injury; inhibition improves lysosomal structure/function in Fabry podocytes. (feriozzi2024theinflammatorypathogenetic pages 5-7)
  - VEGFA: elevated in Fabry patients; correlates with albuminuria and cardiac biomarkers; marker of endothelial dysfunction. (coelhoribeiro2024inflammationandexosomes pages 15-16)
  - Complement C3/C5 (C3a/C5a fragments): elevated in serum despite ERT, especially in nonsense variants with anti‑drug antibodies; indicates complement‑driven inflammation. (coelhoribeiro2024inflammationandexosomes pages 15-16)
  - Cytokines: IL‑6, IL‑10, TGF‑β1, TNF‑α; increased and associated with renal/cardiac involvement. (coelhoribeiro2024inflammationandexosomes pages 15-16, kurdi2024inflammationinfabry pages 8-10, feriozzi2024theinflammatorypathogenetic pages 9-11)
  - Adhesion molecules: VCAM1, ICAM1; implicated in leukocyte recruitment and endothelial dysfunction. (gervasarruga2024insilicomodeling pages 7-8, coelhoribeiro2024inflammationandexosomes pages 15-16)

- Chemical Entities (CHEBI)
  - Globotriaosylceramide (Gb3) and globotriaosylsphingosine (lyso‑Gb3): storage lipids and circulating biomarkers; lyso‑Gb3 exerts direct cytotoxic and signaling effects. (feriozzi2024theinflammatorypathogenetic pages 9-11)

- Cell Types (CL)
  - Podocytes: principal renal target; autophagy impairment, lysosomal toxicity, foot process effacement, podocyturia. (snanoudj2024genomewideexpressionanalysis pages 6-8, feriozzi2024theinflammatorypathogenetic pages 5-7)
  - Endothelial cells and vascular smooth muscle cells: endothelial dysfunction and VSMC proliferation/remodeling. (coelhoribeiro2024inflammationandexosomes pages 15-16, feriozzi2024theinflammatorypathogenetic pages 5-7)
  - Cardiomyocytes and conduction system cells: hypertrophy, inflammation, fibrosis, arrhythmogenic substrate. (kurdi2024inflammationinfabry pages 8-10)
  - Neurons (peripheral and central): sensitization, neurovascular involvement. (coelhoribeiro2024inflammationandexosomes pages 15-16)

- Anatomical Locations (UBERON)
  - Kidney (glomerulus; tubulointerstitium): proteinuria, fibrosis, CKD progression. (feriozzi2024theinflammatorypathogenetic pages 9-11, snanoudj2024genomewideexpressionanalysis pages 6-8)
  - Heart (myocardium; conduction tissue; microvasculature): LV hypertrophy, fibrosis, arrhythmia. (kurdi2024inflammationinfabry pages 8-10)
  - Brain/cerebral vasculature: microvascular dysfunction; stroke risk. (gervasarruga2024insilicomodeling pages 7-8)

Biological Processes (GO, representative)
- Lysosomal catabolic process; glycosphingolipid metabolic process; response to ER stress; unfolded protein response; autophagy and mitophagy; regulation of mitochondrial membrane potential; reactive oxygen species metabolic process; NF‑κB signaling; NLRP3 inflammasome activation; complement activation; leukocyte adhesion to endothelium; nitric oxide–mediated signaling; extracellular matrix organization; TGF‑β signaling and epithelial‑to‑mesenchymal transition/myofibroblast activation. (kurdi2024inflammationinfabry pages 8-10, feriozzi2024theinflammatorypathogenetic pages 7-9, snanoudj2024genomewideexpressionanalysis pages 6-8, coelhoribeiro2024inflammationandexosomes pages 15-16, feriozzi2024theinflammatorypathogenetic pages 9-11)

Cellular Components (GO, representative)
- Lysosome and late endosome; endoplasmic reticulum; ER–Golgi intermediate compartment; autophagosome–lysosome; mitochondrion (cristae, respiratory chain complexes); plasma membrane lipid rafts; endothelial glycocalyx; extracellular matrix. (kurdi2024inflammationinfabry pages 8-10, snanoudj2024genomewideexpressionanalysis pages 6-8, coelhoribeiro2024inflammationandexosomes pages 15-16)

Disease Progression
- Initiation: GLA variant → α‑Gal A deficiency with early Gb3/lyso‑Gb3 accumulation in endothelial cells, podocytes, cardiomyocytes, neurons. (feriozzi2024theinflammatorypathogenetic pages 9-11)
- Cellular stress phase: ER stress/UPR, autophagy blockade, mitochondrial dysfunction and ROS; innate immune activation (NLRP3, NF‑κB), complement activation. (kurdi2024inflammationinfabry pages 8-10, coelhoribeiro2024inflammationandexosomes pages 15-16)
- Tissue remodeling: endothelial dysfunction and VSMC proliferation, adhesion molecule upregulation; mesangial and interstitial fibrosis (TGF‑β–driven); cardiac hypertrophy and interstitial fibrosis; these changes can become partly substrate‑independent. (feriozzi2024theinflammatorypathogenetic pages 7-9, coelhoribeiro2024inflammationandexosomes pages 15-16)
- Clinical manifestations: proteinuria → CKD; LV hypertrophy → arrhythmia and heart failure; cerebrovascular disease (TIA/stroke). Persistent podocyte injury despite Gb3 clearance suggests a pathophysiologic “point of no return” if treatment is delayed. (feriozzi2024theinflammatorypathogenetic pages 5-7, feriozzi2024theinflammatorypathogenetic pages 9-11)

Phenotypic Manifestations and Mechanistic Links
- Renal: early albuminuria/proteinuria progressing to CKD; mechanistic drivers include podocyte autophagy/lysosomal dysfunction, lyso‑Gb3 toxicity, TGF‑β–mediated fibrosis, and persistent inflammatory signaling. (snanoudj2024genomewideexpressionanalysis pages 6-8, feriozzi2024theinflammatorypathogenetic pages 9-11)
- Cardiac: concentric LV hypertrophy, inflammation and fibrosis, arrhythmias; linked to cardiomyocyte lipid accumulation, oxidative stress/bioenergetic failure, inflammation and fibrosis; arrhythmogenic substrate evolves across phases (accumulation → hypertrophy → inflammation → fibrosis). (kurdi2024inflammationinfabry pages 8-10)
- Vascular/Cerebrovascular: endothelial dysfunction, microvascular remodeling, pro‑thrombotic milieu; stroke/TIA risk. (coelhoribeiro2024inflammationandexosomes pages 15-16, gervasarruga2024insilicomodeling pages 7-8)
- Neurologic and pain: neuronal sensitization likely from lyso‑Gb3 effects and lysosomal/autophagic dysfunction. (coelhoribeiro2024inflammationandexosomes pages 15-16)

Recent Developments (2023–2024), Applications, Expert Opinions, and Statistics
- Persistent injury beyond storage: Serial human kidney biopsies and CRISPR GLA‑KO podocytes show ERT reduces Gb3 but does not reverse podocyte injury; α‑synuclein accumulation identified as a key mediator; genetic/pharmacologic SNCA inhibition improved lysosomal structure/function beyond ERT. This reconceptualizes Fabry nephropathy and suggests adjunct targets. Journal of Clinical Investigation, 2023; DOI: 10.1172/JCI157782. (feriozzi2024theinflammatorypathogenetic pages 5-7)
- Inflammation/complement despite ERT: In 17 classical male FD patients, strong complement activation was demonstrated (elevated C3a/C5a) before and after ERT; levels increased particularly in nonsense variants with anti‑drug antibodies; cytokines (IL‑6, IL‑10, TGF‑β1) were elevated and associated with renal involvement, supporting inflammation as a therapeutic target. Frontiers in Immunology, 2024; DOI: 10.3389/fimmu.2024.1307558. (coelhoribeiro2024inflammationandexosomes pages 15-16)
- Integrative mechanism review (cardiac focus): ER stress/UPR, autophagy impairment, mitochondrial dysfunction and oxidative stress interact to promote remodeling, fibrosis and arrhythmias; treatment effectiveness remains limited, underscoring need for novel strategies. Current Heart Failure Reports, 2024; DOI: 10.1007/s11897-024-00645-1. (kurdi2024inflammationinfabry pages 8-10)
- In vitro podocyte transcriptomics: GLA‑edited human podocytes show differential expression consistent with oxidative stress, ER folding/UPR (SIL1), autophagy/mTOR disruption, ECM remodeling, and innate immune activation via TLRs by Gb3/lyso‑Gb3. Heliyon, 2024; DOI: 10.1016/j.heliyon.2024.e34357. (snanoudj2024genomewideexpressionanalysis pages 6-8)
- Human models and translation: Patient‑derived organoids display decreased α‑Gal A, Gb3 storage, impaired vascularization (rescued by ERT), and glutathione depletion (restorable); overview of ongoing/registered trials (e.g., AAV and lentiviral gene therapies, GCS inhibitors, SGLT2 inhibitor adjuncts). Journal of Translational Medicine, 2024; DOI: 10.1186/s12967-024-05756-w. (borisch2024humaninvitro pages 11-12)

Current therapies and mechanistic/biomarker implications (real‑world implementations)
- Enzyme replacement therapies (ERT): agalsidase alfa/beta and pegunigalsidase alfa restore α‑Gal A activity and reduce Gb3/lyso‑Gb3. However, cellular signaling alterations and fibrosis may persist; anti‑drug antibodies can provoke complement activation. Frontiers in Immunology, 2024 (complement/ADA); translational organoid and review data emphasize early initiation. (coelhoribeiro2024inflammationandexosomes pages 15-16, borisch2024humaninvitro pages 11-12)
- Pharmacological chaperone therapy (migalastat): stabilizes amenable mutant GLA and improves lysosomal trafficking; PK modeling in ESRD suggests a 123 mg every‑other‑week regimen around hemodialysis achieves target exposure with minimal accumulation, informing use in advanced CKD. PLOS One, 2024; DOI: 10.1371/journal.pone.0314030. (kurdi2024inflammationinfabry pages 8-10)
- Gene therapy: Preclinical AAV‑ and lentiviral‑based strategies demonstrate sustained α‑Gal A expression and clearance of Gb3/lyso‑Gb3 in plasma, kidney and heart; early Canadian lentiviral clinical experience monitored comprehensive glycosphingolipid biomarker profiles over five years. Gene Therapy 2023; Mol Ther Methods Clin Dev 2024; Rare Disease and Orphan Drugs Journal 2024. (borisch2024humaninvitro pages 11-12)
- Biomarkers: lyso‑Gb3 remains a central diagnostic and therapeutic biomarker; emerging inflammatory/endothelial markers (VEGFA, GDF‑15, MPO, ADAMTS‑13, TNF‑α) provide complementary disease‑activity signatures and may track ERT effects. International Journal of Molecular Sciences, 2024. (coelhoribeiro2024inflammationandexosomes pages 15-16)

Direct quotations (supporting key statements)
- “Substrate accumulation (Gb3 and lyso‑Gb3) triggers inflammation and ER stress/UPR… Lysosomal Gb3 accumulation impairs autophagy… Mitochondrial dysfunction and bioenergetic impairment… The NLRP3 inflammasome is implicated, leading to caspase‑1–dependent IL‑1β/IL‑18 release.” Frontiers in Cardiovascular Medicine, 2024. (kurdi2024inflammationinfabry pages 8-10)
- “Elevated globotriaosylsphingosine is a hallmark of Fabry disease… α‑Gal A missense variants… can lead to ER stress and induction of the unfolded protein response… Defective lysosomal storage… modifies mitochondrial structure, metabolism and turnover.” Rare Disease and Orphan Drugs Journal, 2024. (feriozzi2024theinflammatorypathogenetic pages 9-11)
- “Strong activation of the complement system… evidenced by high C3a and C5a serum levels… in contrast to the strong reduction of lyso‑Gb3 under ERT, C3a and C5a markedly increased… most of whom developed anti‑drug antibodies.” Frontiers in Immunology, 2024. (coelhoribeiro2024inflammationandexosomes pages 15-16)
- “Long‑term use of ERT reduced Gb3 accumulation in podocytes but did not reverse podocyte injury… α‑synuclein accumulation as a key event mediating podocyte injury… inhibition of SNCA improved lysosomal structure and function.” Journal of Clinical Investigation, 2023. (feriozzi2024theinflammatorypathogenetic pages 5-7)

Gene/protein annotations with ontology terms
- GLA (HGNC:4296); α‑galactosidase A (UniProt: P06280); GO:0005759 mitochondrion; GO:0006914 autophagy; GO:0006986 response to unfolded protein; GO:0007165 signal transduction; GO:0006954 inflammatory response; GO:0006956 complement activation. (kurdi2024inflammationinfabry pages 8-10, feriozzi2024theinflammatorypathogenetic pages 9-11)
- SNCA (HGNC:11138); GO:0005773 vacuole/lysosome; GO:0006914 autophagy; implicated in lysosomal dysfunction in podocytes. (feriozzi2024theinflammatorypathogenetic pages 5-7)
- VEGFA (HGNC:12680); GO:0001525 angiogenesis; elevated as endothelial dysfunction biomarker. (coelhoribeiro2024inflammationandexosomes pages 15-16)
- VCAM1 (HGNC:12663), ICAM1 (HGNC:5344); GO:0007155 cell adhesion; endothelial leukocyte adhesion. (gervasarruga2024insilicomodeling pages 7-8)
- TNF (HGNC:11892), IL6 (HGNC:6018), TGFB1 (HGNC:11766); GO:0006954 inflammatory response; GO:0006959 humoral immune response; GO:0006957 complement pathway (contextual); GO:0007165 signal transduction; GO:0001501 skeletal system development (TGFB1 fibrosis context). (kurdi2024inflammationinfabry pages 8-10, feriozzi2024theinflammatorypathogenetic pages 9-11)

Phenotype associations (HP terms)
- HP:0000093 Proteinuria; HP:0000112 Chronic kidney disease; HP:0001639 Cardiomyopathy; HP:0001707 Arrhythmia; HP:0001297 Stroke; HP:0000975 Angiokeratoma; HP:0001250 Peripheral neuropathy; mechanistic links as above. (feriozzi2024theinflammatorypathogenetic pages 9-11, kurdi2024inflammationinfabry pages 8-10, gervasarruga2024insilicomodeling pages 7-8)

Cell type involvement (CL terms)
- CL:0000653 Podocyte; CL:0000115 Endothelial cell; CL:0000746 Cardiomyocyte; CL:0000746 conduction variants; CL:0000749 Vascular smooth muscle cell; CL:0000540 Neuron. (snanoudj2024genomewideexpressionanalysis pages 6-8, coelhoribeiro2024inflammationandexosomes pages 15-16)

Anatomical locations (UBERON terms)
- UBERON:0002113 Kidney; UBERON:0000948 Heart; UBERON:0000955 Brain; UBERON:0001981 Cerebral vasculature. (feriozzi2024theinflammatorypathogenetic pages 9-11, gervasarruga2024insilicomodeling pages 7-8)

Chemical entities (CHEBI)
- CHEBI:XXXXX Globotriaosylceramide (Gb3); CHEBI:XXXXX Globotriaosylsphingosine (lyso‑Gb3). (feriozzi2024theinflammatorypathogenetic pages 9-11)

Evidence items with PMIDs/URLs/dates
- Kurdi H, et al. Inflammation in Fabry disease: stages, molecular pathways, and therapeutic implications. Front Cardiovasc Med. 2024 Jun; URL: https://doi.org/10.3389/fcvm.2024.1420067 (mechanisms: UPR, autophagy, mitochondria, NLRP3, oxidative stress; cardiac links). (kurdi2024inflammationinfabry pages 8-10)
- Feriozzi S, Rozenfeld P. The inflammatory pathogenetic pathways of Fabry nephropathy. Rare Dis Orphan Drugs J. 2024 Apr; URL: https://doi.org/10.20517/rdodj.2023.37 (lyso‑Gb3 toxicity, ER stress/UPR, autophagy/mitochondria, fibrosis; podocyte and tubular mechanisms). (feriozzi2024theinflammatorypathogenetic pages 9-11, feriozzi2024theinflammatorypathogenetic pages 7-9)
- Coelho‑Ribeiro B, et al. Inflammation and Exosomes in Fabry Disease Pathogenesis. Cells. 2024 Apr; URL: https://doi.org/10.3390/cells13080654 (endothelial dysfunction, adhesion molecules, oxidative stress; therapy context). (coelhoribeiro2024inflammationandexosomes pages 15-16)
- Gervas‑Arruga J, et al. In silico modeling… IJMS. 2024 Sep; URL: https://doi.org/10.3390/ijms251910329 (adhesion molecules, endothelial dysfunction, biomarker candidates). (gervasarruga2024insilicomodeling pages 7-8)
- Snanoudj S, et al. Genome‑wide expression analysis in a Fabry disease human podocyte cell line. Heliyon. 2024 Jul; URL: https://doi.org/10.1016/j.heliyon.2024.e34357 (podocyte transcriptomics: UPR/autophagy/ECM/innate immunity). (snanoudj2024genomewideexpressionanalysis pages 6-8)
- Borisch C, et al. Human in vitro models for Fabry disease. J Transl Med. 2024 Oct; URL: https://doi.org/10.1186/s12967-024-05756-w (organoid mechanisms; ongoing trials and applications). (borisch2024humaninvitro pages 11-12)
- Braun F, et al. Accumulation of α‑synuclein mediates podocyte injury in Fabry nephropathy. J Clin Invest. 2023 Jun; URL: https://doi.org/10.1172/jci157782 (ERT reduces Gb3 but not podocyte injury; SNCA as mediator). (feriozzi2024theinflammatorypathogenetic pages 5-7)
- Laffer B, et al. Complement activation and cellular inflammation in Fabry disease patients despite ERT. Front Immunol. 2024 Jan; URL: https://doi.org/10.3389/fimmu.2024.1307558 (C3a/C5a elevation; cytokines; ADA context). (coelhoribeiro2024inflammationandexosomes pages 15-16)

Artifacts
| Category | Name | Ontology namespace.term | Role/notes | Evidence (Context IDs) |
|---|---|---|---|---|
| Gene | GLA | HGNC:GLA | Causal gene encoding alpha-galactosidase A; loss-of-function causes substrate accumulation | (feriozzi2024theinflammatorypathogenetic pages 9-11, feriozzi2024theinflammatorypathogenetic pages 7-9) |
| Protein | alpha-galactosidase A | UniProt:GLA (alpha-galactosidase A) | Lysosomal hydrolase deficient in Fabry disease; target of ERT/chaperone/gene therapies | (feriozzi2024theinflammatorypathogenetic pages 9-11, feriozzi2024theinflammatorypathogenetic pages 7-9) |
| Metabolite | Globotriaosylceramide (Gb3) | CHEBI:globotriaosylceramide (Gb3) | Primary accumulating glycosphingolipid that disrupts lysosomal function and cells | (feriozzi2024theinflammatorypathogenetic pages 9-11, coelhoribeiro2024inflammationandexosomes pages 15-16) |
| Metabolite | Globotriaosylsphingosine (lyso-Gb3) | CHEBI:globotriaosylsphingosine (lyso-Gb3) | Deacylated Gb3 derivative; biomarker and direct mediator of cytotoxicity/inflammation | (feriozzi2024theinflammatorypathogenetic pages 9-11, coelhoribeiro2024inflammationandexosomes pages 15-16) |
| Gene/Protein | Alpha-synuclein (SNCA) | HGNC:SNCA | Identified as mediator of persistent podocyte lysosomal dysfunction and candidate therapeutic target | (feriozzi2024theinflammatorypathogenetic pages 5-7) |
| Gene/Protein | VEGFA | HGNC:VEGFA | Angiogenic factor upregulated in endothelial dysfunction and proposed as vascular biomarker | (coelhoribeiro2024inflammationandexosomes pages 15-16, gervasarruga2024insilicomodeling pages 7-8) |
| Proteins/Fragments | Complement C3a / C5a | HGNC:C3, HGNC:C5 (C3a/C5a) | Evidence of complement activation (elevated C3a/C5a) contributing to inflammation despite ERT | (coelhoribeiro2024inflammationandexosomes pages 15-16, kurdi2024inflammationinfabry pages 8-10) |
| Cytokine | IL-6 | HGNC:IL6 | Pro-inflammatory cytokine elevated in FD-related inflammation and renal/cardiac injury | (feriozzi2024theinflammatorypathogenetic pages 5-7, kurdi2024inflammationinfabry pages 8-10) |
| Cytokine | TNF-alpha | HGNC:TNF | Pro-inflammatory mediator implicated in organ damage and inflammatory signaling | (feriozzi2024theinflammatorypathogenetic pages 5-7, kurdi2024inflammationinfabry pages 8-10) |
| Cytokine / Growth factor | TGF-beta1 | HGNC:TGFB1 | Profibrotic mediator linked to mesangial ECM deposition and interstitial fibrosis | (feriozzi2024theinflammatorypathogenetic pages 5-7, feriozzi2024theinflammatorypathogenetic pages 9-11) |
| Adhesion molecule | VCAM1 | HGNC:VCAM1 | Upregulated adhesion molecule promoting leukocyte recruitment and endothelial dysfunction | (gervasarruga2024insilicomodeling pages 7-8, coelhoribeiro2024inflammationandexosomes pages 15-16) |
| Adhesion molecule | ICAM1 | HGNC:ICAM1 | Endothelial adhesion molecule involved in leukocyte adhesion/extravasation | (gervasarruga2024insilicomodeling pages 7-8, coelhoribeiro2024inflammationandexosomes pages 15-16) |
| Cell type | Podocyte | CL:podocyte | Principal renal cell target; Gb3/lyso-Gb3–driven injury, autophagy impairment, podocyturia and proteinuria | (snanoudj2024genomewideexpressionanalysis pages 6-8, feriozzi2024theinflammatorypathogenetic pages 5-7) |
| Cell type | Endothelial cell | CL:endothelial_cell | Early vascular target; endothelial dysfunction, eNOS uncoupling, adhesion-molecule upregulation | (coelhoribeiro2024inflammationandexosomes pages 15-16, kurdi2024inflammationinfabry pages 8-10) |
| Cell type | Cardiomyocyte | CL:cardiomyocyte | Cardiac lipid deposition → hypertrophy, inflammation, fibrosis, arrhythmogenic substrate | (kurdi2024inflammationinfabry pages 8-10, coelhoribeiro2024inflammationandexosomes pages 15-16) |
| Cell type | Vascular smooth muscle cell | CL:vascular_smooth_muscle_cell | Lyso-Gb3–driven proliferation and vascular wall remodeling | (feriozzi2024theinflammatorypathogenetic pages 5-7) |
| Cell type | Neuron | CL:neuron | Peripheral/central neuronal sensitization and CNS involvement linked to lyso-Gb3 and lysosomal dysfunction | (coelhoribeiro2024inflammationandexosomes pages 15-16, gervasarruga2024insilicomodeling pages 7-8) |
| Anatomy | Kidney | UBERON:kidney | Major organ of Fabry nephropathy (podocyte loss, proteinuria, CKD progression) | (feriozzi2024theinflammatorypathogenetic pages 5-7, snanoudj2024genomewideexpressionanalysis pages 6-8) |
| Anatomy | Heart | UBERON:heart | Organ affected by sphingolipid deposition: hypertrophy, fibrosis, arrhythmia, heart failure | (kurdi2024inflammationinfabry pages 8-10, coelhoribeiro2024inflammationandexosomes pages 15-16) |
| Anatomy | Brain / cerebral vasculature | UBERON:brain_vasculature | Cerebrovascular involvement (stroke risk), microvascular dysfunction and neuronal effects | (gervasarruga2024insilicomodeling pages 7-8, coelhoribeiro2024inflammationandexosomes pages 15-16) |


*Table: A compact ontology-mapped table of genes, proteins, metabolites, cell types and organs implicated in Fabry disease with brief roles and matched evidence IDs for provenance; useful for knowledge-base ingestion and mechanistic annotation. Citations link to collected context items supporting each entry.*

Notes and limitations
- GO, CL, UBERON, CHEBI identifiers are provided at the term level for integration; specific numeric IDs for CHEBI Gb3/lyso‑Gb3 should be completed during curation. Where direct PMIDs are not provided in the excerpt, DOI/URL and journal/date are supplied; underlying primary studies are cited within the reviews. The complement and SNCA findings are supported by recent primary evidence. Remaining open questions include the extent to which inflammation becomes substrate‑independent and the optimal timing/combination of anti‑inflammatory or complement‑targeting therapies alongside disease‑specific treatments. (kurdi2024inflammationinfabry pages 8-10, coelhoribeiro2024inflammationandexosomes pages 15-16, feriozzi2024theinflammatorypathogenetic pages 5-7)

References

1. (feriozzi2024theinflammatorypathogenetic pages 9-11): Sandro Feriozzi and Paula Rozenfeld. The inflammatory pathogenetic pathways of fabry nephropathy. Rare Disease and Orphan Drugs Journal, Apr 2024. URL: https://doi.org/10.20517/rdodj.2023.37, doi:10.20517/rdodj.2023.37. This article has 4 citations.

2. (feriozzi2024theinflammatorypathogenetic pages 7-9): Sandro Feriozzi and Paula Rozenfeld. The inflammatory pathogenetic pathways of fabry nephropathy. Rare Disease and Orphan Drugs Journal, Apr 2024. URL: https://doi.org/10.20517/rdodj.2023.37, doi:10.20517/rdodj.2023.37. This article has 4 citations.

3. (kurdi2024inflammationinfabry pages 8-10): Hibba Kurdi, Lucia Lavalle, James C. C. Moon, and Derralynn Hughes. Inflammation in fabry disease: stages, molecular pathways, and therapeutic implications. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1420067, doi:10.3389/fcvm.2024.1420067. This article has 21 citations and is from a peer-reviewed journal.

4. (snanoudj2024genomewideexpressionanalysis pages 6-8): Sarah Snanoudj, Céline Derambure, Cheng Zhang, Nguyen Thi Hai Yen, Céline Lesueur, Sophie Coutant, Lénaïg Abily-Donval, Stéphane Marret, Hong Yang, Adil Mardinoglu, Soumeya Bekri, and Abdellah Tebani. Genome-wide expression analysis in a fabry disease human podocyte cell line. Heliyon, 10:e34357, Jul 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e34357, doi:10.1016/j.heliyon.2024.e34357. This article has 6 citations and is from a peer-reviewed journal.

5. (feriozzi2024theinflammatorypathogenetic pages 5-7): Sandro Feriozzi and Paula Rozenfeld. The inflammatory pathogenetic pathways of fabry nephropathy. Rare Disease and Orphan Drugs Journal, Apr 2024. URL: https://doi.org/10.20517/rdodj.2023.37, doi:10.20517/rdodj.2023.37. This article has 4 citations.

6. (coelhoribeiro2024inflammationandexosomes pages 15-16): Bruna Coelho-Ribeiro, Helena G. Silva, Belém Sampaio-Marques, Alexandra G. Fraga, Olga Azevedo, Jorge Pedrosa, and Paula Ludovico. Inflammation and exosomes in fabry disease pathogenesis. Cells, 13:654, Apr 2024. URL: https://doi.org/10.3390/cells13080654, doi:10.3390/cells13080654. This article has 12 citations and is from a poor quality or predatory journal.

7. (gervasarruga2024insilicomodeling pages 7-8): Javier Gervas-Arruga, Miguel Ángel Barba-Romero, Jorge Julián Fernández-Martín, Jorge Francisco Gómez-Cerezo, Cristina Segú-Vergés, Giacomo Ronzoni, and Jorge J. Cebolla. In silico modeling of fabry disease pathophysiology for the identification of early cellular damage biomarker candidates. International Journal of Molecular Sciences, 25:10329, Sep 2024. URL: https://doi.org/10.3390/ijms251910329, doi:10.3390/ijms251910329. This article has 6 citations and is from a poor quality or predatory journal.

8. (borisch2024humaninvitro pages 11-12): Carla Borisch, Thomas Thum, Christian Bär, and Jeannine Hoepfner. Human in vitro models for fabry disease: new paths for unravelling disease mechanisms and therapies. Journal of Translational Medicine, Oct 2024. URL: https://doi.org/10.1186/s12967-024-05756-w, doi:10.1186/s12967-024-05756-w. This article has 9 citations and is from a peer-reviewed journal.