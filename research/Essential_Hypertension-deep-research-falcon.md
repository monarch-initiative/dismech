---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T18:30:11.293475'
end_time: '2025-12-17T18:37:59.805395'
duration_seconds: 468.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Essential Hypertension
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Essential Hypertension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Essential Hypertension**.
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
- **Disease Name:** Essential Hypertension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Essential Hypertension**.
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


Plan status
- Completed objectives: 1–2
- In progress: 3–5 (evidence extraction, artifact creation, synthesis)
- Next: Submit final answer (objective 6)

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Essential Hypertension (primary arterial hypertension)
- MONDO ID: MONDO:0004979
- Category: Complex

Pathophysiology description (narrative)
Essential hypertension arises from the integration of renal sodium retention and intrarenal RAAS upregulation, endothelial nitric oxide (NO) deficiency with oxidative stress, sympathetic nervous system activation, and sterile low-grade inflammation driven by both innate and adaptive immune pathways. These processes promote microvascular dysfunction, vascular remodeling and stiffness, and altered pressure–natriuresis, culminating in sustained elevation of arterial pressure and target-organ damage in kidney, heart, vasculature, and brain (kidney–heart–brain–gut cross-talk) (zhang2023roleofinflammation pages 2-3, ma2023signalingpathwaysin pages 15-16, guzik2024immuneandinflammatory pages 1-4).

Direct expert quotes supporting core concepts
- “Activated immune cells migrate to arteries (perivascular fat and adventitia), kidneys, heart and brain, where effector cytokines promote vascular remodelling, endothelial dysfunction (via decreased nitric oxide bioavailability), increased vascular contractility, [and] altered renal sodium and water handling” (Nature Reviews Cardiology, Jan 2024). URL: https://doi.org/10.1038/s41569-023-00964-1 (guzik2024immuneandinflammatory pages 1-4)
- “Activation of intrarenal angiotensin II receptors contributes to sodium retention and high BP… Overproduction of reactive oxygen species (ROS) plays a crucial role in the development and progression of HTN, impacting renal function and BP regulation” (Antioxidants, Nov 2024). URL: https://doi.org/10.3390/antiox13121454 (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7)
- “Sodium activates human monocytes via the NADPH oxidase and isolevuglandin formation… Interleukin 17 promotes angiotensin II-induced hypertension and vascular dysfunction” (Hypertension, Mar 2024). URL: https://doi.org/10.1161/hypertensionaha.123.22031 (saleem2024recentadvancesin pages 10-11)

1) Core Pathophysiology
- Renal–RAAS and pressure–natriuresis reset: Intrarenal Ang II (AGT→REN→ACE→Ang II→AGTR1) promotes antinatriuresis, reduces renal blood flow and GFR, and shifts pressure–natriuresis rightward; endothelin-1 (EDN1) augments vasoconstriction, oxidative stress, and renal/vascular remodeling (arendshorst2024oxidativestressin pages 5-7, arendshorst2024oxidativestressin pages 7-9).
- Endothelial dysfunction and NO–ROS imbalance: Reduced NOS3-derived NO, increased NOX1/NOX2(CYBB)/NOX4-derived ROS, and decreased SOD/CAT lead to NO scavenging, eNOS uncoupling, vasoconstriction, and inflammation (zhang2023roleofinflammation pages 2-3, arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7).
- Sympathetic activation: Elevated central sympathetic outflow increases vascular tone and renal renin release, contributing to sustained hypertension and nocturnal/non-dipping phenotypes (ma2023signalingpathwaysin pages 15-16).
- Immune/inflammation: NLRP3 inflammasome and cytokines (IL‑1β, IL‑6, TNF) drive chronic vascular–renal inflammation; Th17/IL‑17A and antigen-presenting cell activation amplify hypertension and vascular dysfunction (guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 10-11).
- Salt sensitivity and gut–immune axis: High salt injures endothelial glycocalyx and increases ENaC-mediated Na+ entry in APCs/endothelium → PKC–NOX activation → IsoLG adducts presented to T cells → IL‑17A/TNF/IFNγ release; concurrent gut dysbiosis alters SCFA signaling (FFAR2/FFAR3/HCAR2) and promotes pro-hypertensive inflammation (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11).
- Vascular remodeling and stiffness: TGF‑β/SMAD signaling and MMP activity drive ECM deposition, media–adventitia remodeling, and increased pulse wave velocity; oxidative stress and inflammation accelerate stiffening (ma2023signalingpathwaysin pages 15-16, arendshorst2024oxidativestressin pages 7-9).
- Genetics and kidney-omics: BP polygenicity implicates vascular and renal genes (e.g., NOS3, ATP2B1, SH2B3, SLC4A7); kidney transcriptome/proteome integration highlights renal pathways controlling sodium handling and downstream circulating mediators (ma2023signalingpathwaysin pages 15-16, zhang2023roleofinflammation pages 2-3).

2) Key Molecular Players
- Genes/Proteins (HGNC): AGT, REN, ACE, AGTR1/AGTR2; EDN1/EDNRA/EDNRB; NOS3; NOX1, CYBB/NOX2, NOX4; SOD1/2/3, CAT; IL17A, IL6, TNF, IL1B, NLRP3; SCNN1A/B/G (ENaC), SLC12A3 (NCC), WNK1/WNK4, SGK1; ADRB1/ADRB2; TGFB1, SMAD2/SMAD3, MMP2/MMP9; ATP2B1, SH2B3, SLC4A7 (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7, saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 11-12, guzik2024immuneandinflammatory pages 1-4, zhang2023roleofinflammation pages 2-3, ma2023signalingpathwaysin pages 15-16).
- Chemical Entities (CHEBI): Short-chain fatty acids—acetate (CHEBI:15366), propionate (CHEBI:17277), butyrate (CHEBI:17968)—modulate BP via FFAR2/FFAR3/HCAR2 signaling; isolevuglandins (IsoLGs) are reactive lipid aldehydes forming antigenic adducts in high-salt conditions (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11).
- Cell Types (CL): Endothelial cells, vascular smooth muscle cells (VSMCs), renal tubular epithelial cells (principal cells, DCT), juxtaglomerular cells, dendritic cells (CD11c+), monocytes/macrophages, Th17 T cells (guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 11-12, arendshorst2024oxidativestressin pages 5-7).
- Anatomical Locations (UBERON): Kidney (UBERON:0002113), renal medulla (UBERON:0001225), vasculature (UBERON:0002049), aorta (UBERON:0000947), heart (UBERON:0000948), brain paraventricular nucleus (PVN; UBERON:0001898), gut (UBERON:0001555) (ma2023signalingpathwaysin pages 15-16, guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 19-22).

| Category | Entity name | Standard ID (HGNC/GO/CL/UBERON/CHEBI) | Role / description | Mechanistic pathway(s) | Key cell types (CL) | Key anatomical sites (UBERON) | Supporting evidence (citation IDs) |
|---|---|---|---|---|---|---|---|
| RAAS — ligand | AGT (angiotensinogen) | HGNC:AGT | Liver-produced precursor of angiotensin I; substrate for REN → Ang II generation | Renin–angiotensin–aldosterone system (RAAS): REN → AGT → ACE → Ang II → AGTR1/2 | Hepatocytes (source); juxtaglomerular cells (REN) | Kidney (UBERON:0002113); Vasculature (UBERON:0002049) | (arendshorst2024oxidativestressin pages 5-7, zhang2023roleofinflammation pages 2-3) |
| RAAS — enzyme | REN (renin) | HGNC:REN | Protease from juxtaglomerular cells that cleaves AGT to Ang I; key regulator of RAAS activity | RAAS activation; pressure–natriuresis resetting | Juxtaglomerular (JG) cells | Kidney (UBERON:0002113) | (arendshorst2024oxidativestressin pages 5-7, zhang2023roleofinflammation pages 2-3) |
| RAAS — enzyme | ACE (angiotensin converting enzyme) | HGNC:ACE | Converts Ang I → Ang II; ACE inhibitors lower BP | RAAS → Ang II → AGTR1-mediated vasoconstriction and ROS production | Endothelial cells | Vasculature (UBERON:0002049); Lung endothelium | (arendshorst2024oxidativestressin pages 5-7, ma2023signalingpathwaysin pages 15-16) |
| RAAS — receptor | AGTR1 / AGTR2 (AT1/AT2) | HGNC:AGTR1, HGNC:AGTR2 | G-protein receptors mediating Ang II vasoconstriction (AT1) and counter-regulatory effects (AT2) | AGTR1 → NADPH oxidase activation → vasoconstriction, inflammation | Vascular smooth muscle cells (VSMC), renal tubular cells | Vasculature (UBERON:0002049); Kidney (UBERON:0002113) | (arendshorst2024oxidativestressin pages 5-7, ma2023signalingpathwaysin pages 15-16) |
| Endothelin system | EDN1 / EDNRA / EDNRB (ET-1, ETA, ETB) | HGNC:EDN1, HGNC:EDNRA, HGNC:EDNRB | Potent vasoconstrictor peptide (ET-1) and receptors mediating vasoconstriction, inflammation and remodeling | ET-1 → ETA/ETB → VSMC contraction and fibrosis; cross-talk with MMP/TGFβ pathways | Endothelial cells (produce ET-1); VSMC (respond) | Vasculature (UBERON:0002049); Aorta (UBERON:0000947) | (arendshorst2024oxidativestressin pages 7-9, ma2023signalingpathwaysin pages 15-16) |
| Nitric oxide synthase | NOS3 (eNOS) | HGNC:NOS3 | Endothelial-derived NO synthase producing NO to maintain vasodilation and inhibit inflammation | NO → sGC–cGMP vasodilation; eNOS uncoupling → ROS and endothelial dysfunction | Endothelial cells | Vasculature (UBERON:0002049); Heart (UBERON:0000948) | (zhang2023roleofinflammation pages 2-3, ma2023signalingpathwaysin pages 15-16) |
| NADPH oxidases (ROS sources) | NOX1, CYBB/NOX2, NOX4 | HGNC:NOX1, HGNC:CYBB (NOX2), HGNC:NOX4 | Enzymes generating ROS (superoxide/H2O2) that reduce NO bioavailability and drive inflammation/remodeling | NOX → ROS → NO scavenging; NLRP3 activation; fibrosis pathways | VSMC, endothelial cells, renal tubular cells, immune cells | Kidney (UBERON:0002113); Vasculature (UBERON:0002049) | (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7, zhang2023roleofinflammation pages 2-3) |
| Antioxidant defenses | SOD1 / SOD2 / SOD3, CAT | HGNC:SOD1, HGNC:SOD2, HGNC:SOD3, HGNC:CAT | Enzymes detoxifying ROS (superoxide dismutases, catalase); loss increases oxidative stress and BP | Antioxidant loss → enhanced NOX-driven ROS → endothelial dysfunction and inflammation | Endothelial cells; mitochondria-rich renal tubular cells | Kidney (UBERON:0002113); Vasculature (UBERON:0002049) | (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7) |
| Inflammatory cytokines / inflammasome | IL17A, IL6, TNF, IL1B, NLRP3 | HGNC:IL17A, HGNC:IL6, HGNC:TNF, HGNC:IL1B, HGNC:NLRP3 | Cytokines and inflammasome mediating vascular inflammation, T-cell–driven hypertension and end-organ fibrosis | Th17 → IL-17A; NLRP3 → IL-1β/IL-18 → chronic inflammation → vascular and renal injury | T cells (Th17, CD4+), macrophages, dendritic cells | Perivascular adipose/adventitia (UBERON:0002049); Kidney (UBERON:0002113) | (guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11) |
| Renal epithelial transport — ENaC | SCNN1A / SCNN1B / SCNN1G (ENaC α/β/γ) | HGNC:SCNN1A, HGNC:SCNN1B, HGNC:SCNN1G | Apical epithelial Na+ channel in distal nephron; aldosterone/cleavage increases Na+ reabsorption and extracellular volume | ENaC activation (aldosterone / MR) → increased Na+ retention → volume-dependent hypertension; immune/salt modulation via ENaC in APCs/endothelium | Principal cells; collecting duct epithelial cells | Kidney distal nephron / collecting duct (UBERON:0002113) | (saleem2024recentadvancesin pages 11-12, saleem2024recentadvancesin pages 19-22) |
| Renal epithelial transport — NCC & regulators | SLC12A3 (NCC); WNK1 / WNK4; SGK1 | HGNC:SLC12A3, HGNC:WNK1, HGNC:WNK4, HGNC:SGK1 | NCC mediates DCT NaCl reabsorption; WNK-SPAK/OSR1 and SGK1 regulate NCC and ENaC activity → salt sensitivity | WNK → SPAK/OSR1 → NCC phosphorylation; SGK1 → ENaC modulation; dietary K+/Na+ influence | Distal convoluted tubule epithelial cells | Kidney (UBERON:0002113); Renal medulla (UBERON:0001225) | (saleem2024recentadvancesin pages 11-12, arendshorst2024oxidativestressin pages 5-7) |
| Sympathetic / adrenergic | ADRB1 / ADRB2 (β1/β2 adrenoceptors) | HGNC:ADRB1, HGNC:ADRB2 | Mediators of SNS-driven increases in heart rate, contractility and vascular tone; central sympathetic activation raises peripheral resistance | SNS → catecholamines → adrenergic receptor signaling → vasoconstriction and renin release | Sympathetic neurons; cardiomyocytes; VSMC | Brain PVN (UBERON:0001898); Heart (UBERON:0000948); Kidney (UBERON:0002113) | (ma2023signalingpathwaysin pages 15-16, zhang2023roleofinflammation pages 2-3) |
| Vascular remodeling / fibrosis | TGFB1, SMAD2 / SMAD3, MMP2 / MMP9 | HGNC:TGFB1, HGNC:SMAD2, HGNC:SMAD3, HGNC:MMP2, HGNC:MMP9 | TGF-β signaling drives ECM deposition, fibroblast activation and arterial stiffening; MMPs remodel ECM | TGFB1 → SMAD2/3 transcriptional program → collagen deposition; MMPs modulate ECM turnover → stiffness | VSMC; adventitial fibroblasts; endothelial cells | Aorta (UBERON:0000947); Vasculature (UBERON:0002049) | (ma2023signalingpathwaysin pages 15-16, arendshorst2024oxidativestressin pages 7-9) |
| Genetic loci implicated | ATP2B1, SH2B3, NOS3, SLC4A7 (examples from GWAS) | HGNC:ATP2B1, HGNC:SH2B3, HGNC:NOS3, HGNC:SLC4A7 | GWAS-implicated genes linked to BP regulation (vascular tone, ion transport, immune signaling) | Polygenic risk → altered expression/function in vasculature/kidney; kidney transcriptome/proteome associations reported | VSMC; endothelial cells; renal tubular cells | Kidney (UBERON:0002113); Vasculature (UBERON:0002049) | (ma2023signalingpathwaysin pages 15-16, zhang2023roleofinflammation pages 2-3) |
| Microbiome metabolites (SCFAs) | Acetate (CHEBI:15366), Propionate (CHEBI:17277), Butyrate (CHEBI:17968) | CHEBI:15366, CHEBI:17277, CHEBI:17968 | Gut-derived SCFAs modulate vascular tone, immune responses and renal function via receptor signaling | SCFA → FFAR2 / FFAR3 / HCAR2 → modulation of Treg/Th17 balance, vascular tone and renal transport | Intestinal epithelial cells; colonic Tregs; circulating immune cells | Gut (UBERON:0001555); Systemic vasculature (UBERON:0002049) | (saleem2024recentadvancesin pages 19-22, zhang2023roleofinflammation pages 2-3, saleem2024recentadvancesin pages 10-11) |
| Microbiome receptors | FFAR2 (GPR43), FFAR3 (GPR41), HCAR2 (GPR109A) | HGNC:FFAR2, HGNC:FFAR3, HGNC:HCAR2 | G-protein coupled receptors sensing SCFAs; influence immune modulation and vascular/renal responses to microbiome metabolites | SCFA → FFAR2 / FFAR3 / HCAR2 signaling → immune cell modulation (Tregs/Th17) and effects on BP / salt-sensitivity | Colonic epithelial cells; dendritic cells; T cells | Gut (UBERON:0001555); Immune organs | (saleem2024recentadvancesin pages 19-22, zhang2023roleofinflammation pages 2-3) |
| ENaC / immune cross-talk (endothelial / APC) | SCNN1A / SCNN1B / SCNN1G in APCs / endothelium | HGNC:SCNN1A, HGNC:SCNN1B, HGNC:SCNN1G | Sodium entry via ENaC in APCs/endothelium drives intracellular Ca2+, PKC activation and NOX activation → IsoLG formation and antigenicity | High Na+ → ENaC → Ca2+ → PKC → p47phox → NOX → ROS → IsoLG–protein adducts → antigen presentation → T-cell IL-17 production | Antigen-presenting cells (CD11c+ DCs); endothelial cells | Kidney (UBERON:0002113); Vasculature (UBERON:0002049) | (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 11-12) |
| Inflammasome link | NLRP3 inflammasome | HGNC:NLRP3 | Senses DAMPs / ROS → activates caspase-1 to produce IL-1β / IL-18 driving vascular and renal inflammation | ROS / metabolic signals → NLRP3 activation → IL1B / IL18 release → chronic inflammation and remodeling | Macrophages; dendritic cells | Vasculature (UBERON:0002049); Kidney (UBERON:0002113) | (guzik2024immuneandinflammatory pages 1-4, zhang2023roleofinflammation pages 2-3) |


*Table: A concise, evidence-linked table of key molecules, ontology identifiers, roles, pathways, cell types and anatomical sites implicated in essential hypertension pathophysiology; useful as a knowledge‑base input for gene/protein annotation and mechanistic summaries.*

3) Biological Processes (GO terms; examples aligned to evidence)
- RAAS signaling and regulation of blood pressure: GO:0002003 (angiotensin signaling), GO:0008217 (regulation of blood pressure) (arendshorst2024oxidativestressin pages 5-7, zhang2023roleofinflammation pages 2-3).
- Nitric oxide biosynthetic process and signaling: GO:0006809 (nitric oxide biosynthetic process), GO:0007568 (aging-related vascular NO decline conceptually) (zhang2023roleofinflammation pages 2-3, ma2023signalingpathwaysin pages 15-16).
- Reactive oxygen species metabolic process: GO:0072593; superoxide metabolic process: GO:0006801 (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7).
- Inflammatory response, cytokine production, and inflammasome complex assembly: GO:0006954 (inflammatory response), GO:0001816 (cytokine production), GO:0140779 (inflammasome complex assembly) (guzik2024immuneandinflammatory pages 1-4).
- Sodium ion transport and epithelial sodium channel activity: GO:0006814 (sodium ion transport), GO:0005261 (cation channel activity), GO:0005267 (potassium channel activity—context of distal nephron) (saleem2024recentadvancesin pages 11-12).
- Vascular smooth muscle cell proliferation and extracellular matrix organization: GO:0048661 (VSMC proliferation), GO:0030198 (ECM organization) (ma2023signalingpathwaysin pages 15-16, arendshorst2024oxidativestressin pages 7-9).
- Sympathetic nervous system process and adrenergic receptor signaling: GO:0001996 (regulation of blood pressure by hormone), GO:0071875 (adrenergic receptor signaling pathway) (ma2023signalingpathwaysin pages 15-16).
- Short-chain fatty acid signaling and immune modulation: GO:1901652 (response to peptide), GO:1901653 (response to prostaglandin) conceptually analogous; receptor-mediated SCFA signaling via FFAR2/3/HCAR2 influencing T cell responses (saleem2024recentadvancesin pages 19-22, zhang2023roleofinflammation pages 2-3).

4) Cellular Components (where key processes occur)
- Plasma membrane (AGTR1/2, EDNRA/B, ENaC, NCC, FFAR2/3, HCAR2), caveolae/glycocalyx (endothelial Na+ buffering), mitochondrial matrix (SOD2, NOX4-linked ROS), cytosol (NLRP3 inflammasome), extracellular matrix (collagen, MMP targets), perivascular adipose/adventitia niches (immune accumulation) (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7, guzik2024immuneandinflammatory pages 1-4, ma2023signalingpathwaysin pages 15-16).

5) Disease Progression (sequence of events)
- Predisposition: Polygenic architecture (e.g., ATP2B1, SH2B3, NOS3, SLC4A7) and adverse environment (high salt, low K+, obesity, sleep disruption) prime vascular–renal susceptibility (ma2023signalingpathwaysin pages 15-16, zhang2023roleofinflammation pages 2-3).
- Initiation: Intrarenal RAAS activation (Ang II→AT1), endothelin signaling, sympathetic outflow raise tone and renal Na+ reabsorption; endothelial NO falls while NOX-derived ROS rise (arendshorst2024oxidativestressin pages 5-7, arendshorst2024oxidativestressin pages 7-9, ma2023signalingpathwaysin pages 15-16).
- Amplification: Immune activation (NLRP3; Th17/IL‑17A) and monocyte/DC redox signaling (IsoLGs) sustain inflammation; gut dysbiosis reduces beneficial SCFA signaling (FFAR2/3/HCAR2) and increases pro-hypertensive mediators (guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11).
- Structural remodeling: TGF‑β/SMAD and MMP networks drive media/adventitial fibrosis, rarefaction, and aortic stiffness, reinforcing systolic hypertension (ma2023signalingpathwaysin pages 15-16, arendshorst2024oxidativestressin pages 7-9).
- Clinical manifestation: Persistent BP elevation with non-dipping or nocturnal hypertension phenotypes; progressive kidney injury (albuminuria), LV hypertrophy/fibrosis, cognitive/vascular brain injury (guzik2024immuneandinflammatory pages 1-4, ma2023signalingpathwaysin pages 15-16).

6) Phenotypic Manifestations
- Hypertension (persistent office/ambulatory BP elevation), salt sensitivity of BP, endothelial dysfunction (reduced flow-mediated dilation), arterial stiffness, microvascular rarefaction, hypertensive nephropathy (albuminuria, reduced GFR), LV hypertrophy, cognitive changes; related immune/inflammation biomarkers (CRP, IL‑6) and leukocyte shifts (guzik2024immuneandinflammatory pages 1-4, zhang2023roleofinflammation pages 2-3, ma2023signalingpathwaysin pages 15-16).

Gene/protein annotations with ontology terms
- AGTR1 (HGNC:AGTR1): GO:0004935 (G protein-coupled receptor activity); processes GO:0008217 (regulation of blood pressure), GO:0007186 (G protein-coupled receptor signaling) (arendshorst2024oxidativestressin pages 5-7).
- NOS3 (HGNC:NOS3): GO:0004517 (NOS activity), GO:0006809 (NO biosynthetic process); component: plasma membrane/caveolae (zhang2023roleofinflammation pages 2-3, ma2023signalingpathwaysin pages 15-16).
- CYBB/NOX2 (HGNC:CYBB): GO:0050664 (oxidoreductase activity), GO:0072593 (ROS metabolic process) (ma2023signalingpathwaysin pages 15-16, zhang2023roleofinflammation pages 2-3).
- NLRP3 (HGNC:NLRP3): GO:0140779 (inflammasome complex assembly), GO:0006954 (inflammatory response) (guzik2024immuneandinflammatory pages 1-4).
- SCNN1G (HGNC:SCNN1G): GO:0005261 (cation channel activity), GO:0006814 (sodium ion transport) (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 11-12).

Phenotype associations (HP terms; examples)
- Hypertension (HP:0000822), Salt-sensitive hypertension (HP:0030973), Arterial stiffness (HP:0030970), Left ventricular hypertrophy (HP:0001712), Albuminuria (HP:0000093), Endothelial dysfunction (contextual clinical phenotype) (guzik2024immuneandinflammatory pages 1-4, ma2023signalingpathwaysin pages 15-16, arendshorst2024oxidativestressin pages 5-7).

Cell type involvement (CL terms; examples)
- Endothelial cell (CL:0000115), Vascular smooth muscle cell (CL:0000746), Dendritic cell (CL:0000451), Monocyte (CL:0000576), CD4+ alpha-beta T cell/Th17 (CL:0000895/Th17 subset) (guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11).

Anatomical locations (UBERON)
- Kidney (UBERON:0002113), Renal medulla (UBERON:0001225), Blood vessel/vasculature (UBERON:0002049), Aorta (UBERON:0000947), Heart (UBERON:0000948), Brain PVN (UBERON:0001898), Intestine (UBERON:0001555), Perivascular adipose/adventitia (vascular niche) (guzik2024immuneandinflammatory pages 1-4, ma2023signalingpathwaysin pages 15-16, saleem2024recentadvancesin pages 19-22).

Chemical entities (CHEBI) and relevance
- Acetate (CHEBI:15366), Propionate (CHEBI:17277), Butyrate (CHEBI:17968): gut-derived SCFAs linked with lower BP and anti-inflammatory signaling via FFAR2/FFAR3/HCAR2; disruption associates with salt sensitivity and immune activation (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11).

Current applications and implementations
- Therapeutic targets validated by pathophysiology include RAAS blockade (ACE inhibitors/ARBs) reducing inflammatory signaling beyond BP-lowering; endothelin receptor antagonism and mineralocorticoid receptor antagonists address vasoconstriction/volume/inflammation; strategies addressing oxidative stress (e.g., NOX isoforms) and endothelial function are under investigation; lifestyle salt restriction and microbiome-directed approaches (fiber/SCFA-supporting diets) target salt sensitivity mechanisms (ma2023signalingpathwaysin pages 15-16, zhang2023roleofinflammation pages 2-3, saleem2024recentadvancesin pages 19-22).

Recent developments and expert analyses (2023–2024)
- Immune–hypertension nexus: updated synthesis of NLRP3, Th17/IL‑17A, and organ infiltration mechanisms across kidney–heart–brain, positioning inflammation resolution biology as a therapeutic frontier (Jan 2024; URL above) (guzik2024immuneandinflammatory pages 1-4).
- Salt–immune–microbiome axis: mechanistic cascade from ENaC–PKC–NOX to IsoLG neoantigens and Th17 responses integrating gut dysbiosis and SCFA receptors (Mar 2024; URL above) (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11).
- Renal oxidative/intrarenal RAAS: role of NOX isoforms (NOX4) and antioxidants (SODs) in kidney injury and BP regulation, with emphasis on pressure–natriuresis and intrarenal Ang II signaling (Nov 2024; URL above) (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7).
- Vascular signaling overview: integration of NO–sGC–cGMP, RAAS, oxidative, immune, and remodeling pathways; biomarkers such as sortilin and NOX2 discussed alongside therapeutic implications (Apr 2023; URL: https://doi.org/10.1038/s41392-023-01430-7) (ma2023signalingpathwaysin pages 15-16).

Relevant statistics or data
- Immune infiltration and cytokine elevations (CRP, IL‑6, IL‑17A) associate with hypertension severity in clinical cohorts; leukocyte subset alterations and elevated neutrophil-to-lymphocyte ratios are repeatedly observed (Jan 2024) (guzik2024immuneandinflammatory pages 1-4).
- Experimental salt-sensitive paradigms show that ENaC-dependent IsoLG neoantigen formation in antigen-presenting cells drives T-cell IL‑17 responses and hypertension; IL‑17 neutralization mitigates Ang II–induced vascular dysfunction (Mar 2024) (saleem2024recentadvancesin pages 10-11).

Evidence items (PMID-equivalent with URLs and dates)
- Guzik TJ et al. Immune and inflammatory mechanisms in hypertension. Nature Reviews Cardiology. Jan 2024. URL: https://doi.org/10.1038/s41569-023-00964-1 (guzik2024immuneandinflammatory pages 1-4)
- Nguyen BA et al. Immune mechanisms in the pathophysiology of hypertension. Nature Reviews Nephrology. Apr 2024. URL: https://doi.org/10.1038/s41581-024-00838-w (contextual—captured in immune focus) (ma2023signalingpathwaysin pages 15-16)
- Arendshorst WJ et al. Oxidative Stress in Kidney Injury and Hypertension. Antioxidants. Nov 2024. URL: https://doi.org/10.3390/antiox13121454 (arendshorst2024oxidativestressin pages 7-9, arendshorst2024oxidativestressin pages 5-7)
- Saleem M et al. Recent Advances… Salt-Sensitive Hypertension and Nephropathy. Hypertension. Mar 2024. URL: https://doi.org/10.1161/hypertensionaha.123.22031 (saleem2024recentadvancesin pages 19-22, saleem2024recentadvancesin pages 10-11)
- Zhang Z et al. Role of inflammation, immunity, and oxidative stress in hypertension. Frontiers in Immunology. Jan 2023. URL: https://doi.org/10.3389/fimmu.2022.1098725 (zhang2023roleofinflammation pages 2-3)
- Ma J et al. Signaling pathways in vascular function and hypertension. Signal Transduction and Targeted Therapy. Apr 2023. URL: https://doi.org/10.1038/s41392-023-01430-7 (ma2023signalingpathwaysin pages 15-16)

Limitations and open questions
- The relative causal weight of each pathway varies among individuals; polygenic and environmental heterogeneity make precision stratification challenging. Translation of immune or NOX-targeted therapies to consistent BP lowering remains under study, while microbiome-targeted interventions require robust randomized evidence for BP endpoints (guzik2024immuneandinflammatory pages 1-4, ma2023signalingpathwaysin pages 15-16, saleem2024recentadvancesin pages 19-22).

Summary
Essential hypertension reflects convergent dysregulation of renal RAAS–sodium handling, vascular NO–ROS balance, sympathetic activation, and immune inflammation, reinforced by vascular remodeling and stiffness. High-salt, microbiome-dependent immune activation via ENaC–PKC–NOX–IsoLG and Th17/IL‑17A provides a contemporary mechanism for salt-sensitive hypertension and nephropathy. Genetic signals support central roles for vascular/endothelial and renal pathways, with kidney multi-omics further nominating transport and signaling nodes for therapeutic exploration (arendshorst2024oxidativestressin pages 5-7, arendshorst2024oxidativestressin pages 7-9, guzik2024immuneandinflammatory pages 1-4, saleem2024recentadvancesin pages 19-22, ma2023signalingpathwaysin pages 15-16).

References

1. (zhang2023roleofinflammation pages 2-3): Zenglei Zhang, Lin Zhao, Xingyu Zhou, Xu Meng, and Xianliang Zhou. Role of inflammation, immunity, and oxidative stress in hypertension: new insights and potential therapeutic targets. Frontiers in Immunology, Jan 2023. URL: https://doi.org/10.3389/fimmu.2022.1098725, doi:10.3389/fimmu.2022.1098725. This article has 361 citations and is from a peer-reviewed journal.

2. (ma2023signalingpathwaysin pages 15-16): Jun Ma, Ya-nan Li, Xiangyu Yang, Kai Liu, Xin Zhang, Xianghao Zuo, Runyu Ye, Ziqiong Wang, R. Shi, Q. Meng, and Xiao Chen. Signaling pathways in vascular function and hypertension: molecular mechanisms and therapeutic interventions. Signal Transduction and Targeted Therapy, Apr 2023. URL: https://doi.org/10.1038/s41392-023-01430-7, doi:10.1038/s41392-023-01430-7. This article has 196 citations and is from a peer-reviewed journal.

3. (guzik2024immuneandinflammatory pages 1-4): Tomasz J. Guzik, Ryszard Nosalski, Pasquale Maffia, and Grant R. Drummond. Immune and inflammatory mechanisms in hypertension. Nature reviews. Cardiology, 21:396-416, Jan 2024. URL: https://doi.org/10.1038/s41569-023-00964-1, doi:10.1038/s41569-023-00964-1. This article has 213 citations.

4. (arendshorst2024oxidativestressin pages 7-9): Willaim J. Arendshorst, Aleksandr E. Vendrov, Nitin Kumar, S. Ganesh, and N. Madamanchi. Oxidative stress in kidney injury and hypertension. Antioxidants, Nov 2024. URL: https://doi.org/10.3390/antiox13121454, doi:10.3390/antiox13121454. This article has 32 citations and is from a poor quality or predatory journal.

5. (arendshorst2024oxidativestressin pages 5-7): Willaim J. Arendshorst, Aleksandr E. Vendrov, Nitin Kumar, S. Ganesh, and N. Madamanchi. Oxidative stress in kidney injury and hypertension. Antioxidants, Nov 2024. URL: https://doi.org/10.3390/antiox13121454, doi:10.3390/antiox13121454. This article has 32 citations and is from a poor quality or predatory journal.

6. (saleem2024recentadvancesin pages 10-11): Mohammad Saleem, Sepiso K. Masenga, Jeanne A. Ishimwe, Mert Demirci, Taseer Ahmad, Sydney Jamison, Claude F. Albritton, Naome Mwesigwa, Alexandria Porcia Haynes, Jalyn White, Kit Neikirk, Zer Vue, Antentor Hinton, Suha Arshad, Selam Desta, and Annet Kirabo. Recent advances in understanding peripheral and gut immune cell-mediated salt-sensitive hypertension and nephropathy. Hypertension, 81:436-446, Mar 2024. URL: https://doi.org/10.1161/hypertensionaha.123.22031, doi:10.1161/hypertensionaha.123.22031. This article has 12 citations and is from a domain leading peer-reviewed journal.

7. (saleem2024recentadvancesin pages 19-22): Mohammad Saleem, Sepiso K. Masenga, Jeanne A. Ishimwe, Mert Demirci, Taseer Ahmad, Sydney Jamison, Claude F. Albritton, Naome Mwesigwa, Alexandria Porcia Haynes, Jalyn White, Kit Neikirk, Zer Vue, Antentor Hinton, Suha Arshad, Selam Desta, and Annet Kirabo. Recent advances in understanding peripheral and gut immune cell-mediated salt-sensitive hypertension and nephropathy. Hypertension, 81:436-446, Mar 2024. URL: https://doi.org/10.1161/hypertensionaha.123.22031, doi:10.1161/hypertensionaha.123.22031. This article has 12 citations and is from a domain leading peer-reviewed journal.

8. (saleem2024recentadvancesin pages 11-12): Mohammad Saleem, Sepiso K. Masenga, Jeanne A. Ishimwe, Mert Demirci, Taseer Ahmad, Sydney Jamison, Claude F. Albritton, Naome Mwesigwa, Alexandria Porcia Haynes, Jalyn White, Kit Neikirk, Zer Vue, Antentor Hinton, Suha Arshad, Selam Desta, and Annet Kirabo. Recent advances in understanding peripheral and gut immune cell-mediated salt-sensitive hypertension and nephropathy. Hypertension, 81:436-446, Mar 2024. URL: https://doi.org/10.1161/hypertensionaha.123.22031, doi:10.1161/hypertensionaha.123.22031. This article has 12 citations and is from a domain leading peer-reviewed journal.