---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:59:03.203234'
end_time: '2025-12-18T00:06:27.657515'
duration_seconds: 444.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glaucoma
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Glaucoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Glaucoma**.
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
- **Disease Name:** Glaucoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Glaucoma**.
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


Plan overview: We structured objectives to (i) scope core mechanisms, (ii) gather 2023–2024 literature, (iii) extract pathway and gene evidence, (iv) map cell/anatomy context and disease sequence, (v) summarize applications, (vi) produce an ontology-ready artifact, and (vii) synthesize a comprehensive, citable report. Objectives (ii) and (vi) are completed; the report integrates these outputs with citations and URLs.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Glaucoma
- MONDO ID: MONDO_0005015 (primary open‑angle glaucoma falls under MONDO_0005015 hierarchy)
- Category: Complex

Pathophysiology description (current understanding)
Glaucoma comprises optic neuropathies characterized by retinal ganglion cell (RGC) degeneration and optic nerve head (ONH) remodeling. Elevated intraocular pressure (IOP) from impaired aqueous humor outflow via trabecular meshwork (TM) and Schlemm’s canal (SC) is a major risk driver; however, IOP‑independent mechanisms, including mitochondrial dysfunction, neuroinflammation, and genetic susceptibilities (e.g., OPTN/TBK1, SIX6) also contribute, particularly in normal‑tension glaucoma. A central theme emerging from recent work is a feed‑forward coupling of profibrotic TGF‑β signaling with mechanotransduction pathways (Hippo‑YAP/TAZ, integrin–FAK, TRPV4 and PIEZO1 channels) that stiffens TM/SC and ONH tissues, impairs cellular motility and adaptability, and elevates outflow resistance. Parallel mitochondrial and axonal transport stress in RGCs, and glial‑mediated neuroinflammation with inflammasome activation and blood‑retinal barrier (BRB) disruption, drive progressive axonopathy and vision loss (2023–2025 literature) (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15, wang2025researchprogresson pages 1-2).

1) Core pathophysiology
- Dysregulated profibrotic signaling and mechanotransduction in the outflow tract: Elevated TGF‑β2 promotes ECM deposition (collagens, fibronectin), cytoskeletal stress fibers/CLANs, and EndMT in SC; downstream RhoA/ROCK and Hippo effectors YAP/TAZ link biochemical cues to stiffness and pro‑fibrotic transcription. Mechanosensitive channels TRPV4 and PIEZO1 transduce pressure/flow into Ca2+ signaling, contractility, and further ECM remodeling, generating a mechano‑biochemical feed‑forward loop that increases outflow resistance and IOP (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- Integrin–FAK focal adhesion signaling: Integrins (e.g., ITGA9) and FAK coordinate ECM–cytoskeleton coupling in TM/SC cells; aberrant activation aligns with tissue stiffness and impaired motility; ROCK inhibition can partly restore motility and outflow (rusciano2025cellmotilitydynamics pages 11-13, singh2025moleculargatekeepersof pages 2-3).
- RGC mitochondrial dysfunction and axonopathy: High metabolic demand makes RGCs vulnerable to oxidative stress, disrupted oxidative phosphorylation, and mitophagy dysregulation; impaired axonal transport at the lamina cribrosa and energy failure contribute to early axon degeneration, progressing to soma loss (palanivel2025understandingtherole pages 30-34, wang2025researchprogresson pages 1-2).
- Neuroinflammation and BRB dysfunction: Chronic activation of microglia and astrocytes, upregulation of cytokines (TNF‑α, IL‑1β), and inflammasome (e.g., NLRP3) involvement propagate neurodegeneration. BRB compromise amplifies leukocyte trafficking and inflammatory milieu at retina/ONH (palanivel2025understandingtherole pages 30-34, wang2025researchprogresson pages 1-2).

2) Key molecular players
- Genes/Proteins: MYOC (mutant secretion defects → ER stress/UPR in TM and IOP elevation), OPTN and TBK1 (autophagy/mitophagy signaling and innate immunity; variants linked to NTG and RGC vulnerability), SIX6 (developmental transcription factor linked to optic nerve/RGC susceptibility), YAP1/TAZ (Hippo mechanotransduction), TGFB2 (profibrotic driver), TRPV4 and PIEZO1 (mechanosensitive channels), ITGA9/FAK (integrin–FAK adhesion signaling), NLRP3 (inflammasome) (palanivel2025understandingtherole pages 25-30, singh2025moleculargatekeepersof pages 2-3, wang2025researchprogresson pages 1-2, rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15, rusciano2025cellmotilitydynamics pages 6-7).
- Chemical entities: ROCK inhibitors (cytoskeletal relaxation), agents modulating TGF‑β/ECM, antioxidants/mitochondrial support (e.g., nicotinamide discussed in 2023–2024 literature), emerging anti‑inflammatory strategies targeting inflammasome/cytokine axes (rusciano2025cellmotilitydynamics pages 13-15, wang2025researchprogresson pages 1-2).
- Cell types: TM cells and SC endothelium (outflow resistance), astrocytes and lamina cribrosa fibroblasts at the ONH, microglia (neuroinflammation), RGCs (primary neuronal loss) (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, palanivel2025understandingtherole pages 30-34).
- Anatomical locations: Trabecular meshwork (UBERON:0001772), Schlemm’s canal (UBERON:0001808), optic nerve head/lamina cribrosa (UBERON:0001801), retina (UBERON:0000966) (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 6-7).

3) Biological processes (GO) disrupted
- ECM organization and fibrosis; EndMT/epithelial–mesenchymal transitions; mechanotransduction and response to mechanical stimulus; focal adhesion assembly and cytoskeletal organization; calcium ion transmembrane transport; ER stress and unfolded protein response; autophagy/mitophagy; inflammatory response and inflammasome activation; leukocyte adhesion and vascular responses (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, palanivel2025understandingtherole pages 25-30, wang2025researchprogresson pages 1-2).

4) Cellular components (sites of key processes)
- Cell–ECM adhesions/focal adhesions (integrin–FAK complexes in TM/SC), plasma membrane mechanosensors (TRPV4/PIEZO1), nucleus (YAP/TAZ transcriptional co‑activators), ER (MYOC misfolding, UPR), mitochondria (RGC bioenergetics/mitophagy), extracellular space (ECM remodeling), tight junctions/inner BRB (endothelial/pericyte barriers) (singh2025moleculargatekeepersof pages 2-3, rusciano2025cellmotilitydynamics pages 6-7, wang2025researchprogresson pages 1-2, palanivel2025understandingtherole pages 30-34).

5) Disease progression sequence
- Initiation in the outflow tract: TGF‑β2 elevation and mechanotransduction abnormalities in TM/SC promote ECM deposition, cytoskeletal stiffening, and reduced motility, increasing outflow resistance and IOP (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- Biomechanical stress at the ONH: Elevated IOP and scleral/laminar stiffness induce axoplasmic flow blockade and axonal injury; astrocyte reactivity and ECM remodeling further compromise axon bundles (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- Early RGC axonopathy to soma loss: Mitochondrial dysfunction and impaired transport precipitate distal axon degeneration, followed by RGC apoptosis/other death modes; microglial/astroglial activation and inflammasome signaling accelerate neurodegeneration (palanivel2025understandingtherole pages 30-34, wang2025researchprogresson pages 1-2).
- IOP‑independent contributors: Genetic susceptibilities (OPTN/TBK1/SIX6) and vascular/neuroinflammatory factors drive disease even with normal tension, highlighting dual IOP‑dependent/independent components (wang2025researchprogresson pages 1-2, palanivel2025understandingtherole pages 25-30).

6) Phenotypic manifestations (clinical)
- Structural: ONH cupping and lamina cribrosa remodeling; RNFL thinning; TM stiffening and reduced motion (advanced imaging) (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- Functional: Progressive visual field loss; reduced contrast sensitivity; electrophysiologic deficits linked to RGC dysfunction (wang2025researchprogresson pages 1-2).

Gene/protein annotations with ontology terms
- HGNC: MYOC; GO: ER stress response, protein folding; CL: TM cell; UBERON: TM; Mechanism: ER stress/UPR with mutant MYOC; Evidence: Wang 2025 (review) (wang2025researchprogresson pages 1-2).
- HGNC: OPTN; GO: selective autophagy, mitophagy; CL: RGC; UBERON: retina; Mechanism: autophagy dysfunction in NTG; Evidence: Wang 2025 (wang2025researchprogresson pages 1-2).
- HGNC: TBK1; GO: regulation of autophagy/innate signaling; CL: microglia/RGC; UBERON: retina; Mechanism: OPTN–TBK1 axis; Evidence: Wang 2025 (wang2025researchprogresson pages 1-2).
- HGNC: SIX6; GO: eye development; CL: retinal progenitors; UBERON: retina/ONH; Mechanism: developmental susceptibility; Evidence: Rusciano 2025 preprint review (rusciano2025cellmotilitydynamics pages 11-13).
- HGNC: YAP1; GO: response to mechanical stimulus, transcription co‑activation; CL: TM/SC/astrocyte; UBERON: TM/ONH; Mechanism: Hippo–YAP/TAZ; Evidence: Rusciano 2025 (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13).
- HGNC: TGFB2; GO: ECM organization, SMAD signaling; CL: TM/SC; UBERON: TM/SC; Mechanism: fibrosis and EndMT; Evidence: Rusciano 2025 (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13).
- HGNC: PIEZO1; GO: mechanosensory ion channel activity; CL: SC endothelium; UBERON: SC; Mechanism: pressure/flow sensing; Evidence: Rusciano 2025 (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- HGNC: TRPV4; GO: calcium transport, cytoskeleton regulation; CL: TM; UBERON: TM; Mechanism: contractility and OHT; Evidence: Rusciano 2025 (rusciano2025cellmotilitydynamics pages 13-15).
- HGNC: ITGA9/PTK2(FAK); GO: cell adhesion/focal adhesion; CL: TM/SC; UBERON: TM/SC; Mechanism: integrin–FAK; Evidence: Singh 2025 (singh2025moleculargatekeepersof pages 2-3).
- HGNC: NLRP3; GO: inflammasome activation; CL: microglia; UBERON: retina/ONH; Mechanism: pyroptosis/neuroinflammation; Evidence: Wang 2025 (wang2025researchprogresson pages 1-2) and pathophysiology summaries (palanivel2025understandingtherole pages 30-34).

Cell type involvement (CL terms)
- CL:0000740 retinal ganglion cell; CL:0000129 microglial cell; CL:0000746 astrocyte; TM cell (human ocular TM cell, commonly curated as ocular fibroblast-like cell); SC endothelial cell (venous/lymphatic-like endothelium) (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, palanivel2025understandingtherole pages 30-34).

Anatomical locations (UBERON terms)
- UBERON:0001772 trabecular meshwork; UBERON:0001808 Schlemm’s canal; UBERON:0001801 optic nerve head; UBERON:0000966 retina (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13).

Chemical entities (CHEBI) and modalities
- CHEBI: ROCK inhibitors (e.g., netarsudil class) to relax TM/SC cytoskeleton; anti‑fibrotics targeting TGF‑β/ECM; mitochondrial support (e.g., nicotinamide); emerging anti‑inflammatory/anti‑inflammasome approaches (rusciano2025cellmotilitydynamics pages 13-15, wang2025researchprogresson pages 1-2).

Evidence items (recent)
- Mechanotransduction/fibrosis nexus and therapeutic implications (YAP/TAZ, TRPV4, PIEZO1; ROCK inhibition; diagnostic elastography): Rusciano 2025 preprint review (Dec 2025). URL: https://doi.org/10.20944/preprints202512.0304.v1 (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- TM mechanotransduction and gene therapy framing (integrin–FAK, TRPV4/PIEZO1; CRISPR prospects): Singh 2025 Cureus (Sep 2025). URL: https://doi.org/10.7759/cureus.91633 (singh2025moleculargatekeepersof pages 1-2, singh2025moleculargatekeepersof pages 2-3).
- Mitochondrial dysfunction and multimodal cell‑death in RGCs; oxidative stress; molecular therapy directions: Wang 2025 Molecular Medicine Reports (Nov 2025). URL: https://doi.org/10.3892/mmr.2025.13757 (wang2025researchprogresson pages 1-2).
- Neuroinflammation and inflammasome/BRB themes, with cytokines in glaucomatous milieu: Palanivel 2025 thesis review excerpts (2025) (palanivel2025understandingtherole pages 30-34, palanivel2025understandingtherole pages 25-30).

Current applications and real‑world implementations
- IOP lowering remains standard of care; however, cytoskeletal modulators (ROCK inhibitors) directly target TM/SC mechanobiology and can reduce EndMT/fibrosis‑linked resistance; device‑based outflow restoration (MIGS) complements pharmacology; diagnostics increasingly assess TM stiffness/motion to stratify disease (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15, singh2025moleculargatekeepersof pages 2-3).
- Gene therapy proof‑of‑concepts: CRISPR strategies against MYOC have preclinical efficacy in reducing ER‑stress–mediated TM dysfunction and IOP in transgenic models; these approaches seek durable correction beyond symptomatic pressure reduction (context discussed in reviews) (wang2025researchprogresson pages 1-2, singh2025moleculargatekeepersof pages 2-3).
- Neuroprotection pipelines target mitochondrial resilience (e.g., nicotinamide) and modulate neuroinflammation (inflammasome/cytokines, microglial responses). Clinical translation requires biomarkers to identify IOP‑independent progression (wang2025researchprogresson pages 1-2, palanivel2025understandingtherole pages 30-34).

Expert opinions and analysis (authoritative perspectives)
- Mechanobiology‑centered frameworks argue glaucoma reflects failure of tissue adaptability under chronic mechanical and biochemical stress, necessitating combined anti‑fibrotic, mechanotransduction‑targeting, and pressure‑lowering strategies; integration of OCT‑based elastography and AI may enable personalized, pre‑emptive treatment (Rusciano preprint 2025) (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15).
- Molecular therapy reviews advocate tandem approaches: outflow repair (TM‑directed) plus RGC neuroprotection targeting mitochondria, oxidative stress, and programmed cell death pathways, particularly for normal‑tension disease (Wang 2025) (wang2025researchprogresson pages 1-2).

Relevant statistics and data
- Genetic screening studies identify hypomorphic/rare variants across glaucoma genes (e.g., SIX6, OPTN, CYP1B1), supporting complex polygenic risk; multi‑ethnic GWAS have delineated IOP‑dependent and IOP‑independent components, aligning with clinical heterogeneity (summarized in 2025 review; additional 2024 studies cited therein) (wang2025researchprogresson pages 1-2).

Embedded ontology artifact
| Gene/Protein (HGNC) | Key role in glaucoma (short) | GO Biological Process terms | Cell type (CL id/name) | Anatomy (UBERON id/name) | Pathway / Mechanism keywords | Evidence (DOI/URL + year) |
|---|---|---|---|---|---|---|
| MYOC | TM ECM homeostasis; mutant MYOC → ER stress, TM cell death, ↑IOP | protein folding; ER stress response; secretion | trabecular meshwork cell | UBERON:0001772 trabecular meshwork | ER stress, UPR, autophagy deregulation, TM fibrosis | https://doi.org/10.3892/mmr.2025.13757 (2025) (wang2025researchprogresson pages 1-2, palanivel2025understandingtherole pages 25-30) |
| OPTN | Autophagy receptor; OPTN variants → RGC vulnerability (NTG) | selective autophagy; vesicle-mediated transport | CL:0000740 retinal ganglion cell | UBERON:0000966 retina | mitophagy/autophagy, protein aggregation, neuroinflammation | https://doi.org/10.3892/mmr.2025.13757 (2025) (palanivel2025understandingtherole pages 25-30, wang2025researchprogresson pages 1-2) |
| TBK1 | Regulates autophagy and innate signaling; duplications linked to glaucoma | regulation of autophagy; innate immune signaling | microglial cell (CL:0000129) / RGCs | UBERON:0000966 retina | TBK1-OPTN autophagy axis, NF-κB signaling | https://doi.org/10.3892/mmr.2025.13757 (2025) (palanivel2025understandingtherole pages 25-30, wang2025researchprogresson pages 1-2) |
| SIX6 | Developmental regulator; risk allele affects RGC development & susceptibility | eye development; regulation of transcription | retinal progenitor / RGC precursors | UBERON:0000966 retina | developmental susceptibility, CDKN2A/B network | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 11-13, palanivel2025understandingtherole pages 25-30) |
| YAP1 (Hippo) | Mechanotransduction effector; mediates stiffness-induced TM/SC changes | regulation of transcription, response to mechanical stimulus | astrocyte (CL:0000746) / TM cells | UBERON:0001772 trabecular meshwork; UBERON:0001801 optic nerve head | Hippo–YAP/TAZ, mechanoresponsive transcription, fibrosis | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13) |
| TGFB2 | Profibrotic cytokine elevated in AH; drives ECM deposition in TM/SC | extracellular matrix organization; SMAD signaling | trabecular meshwork cell / SC endothelium | UBERON:0001772 trabecular meshwork; UBERON:0001808 Schlemm's canal | TGF-β/SMAD, EndMT, ECM remodeling, fibrosis | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13) |
| PIEZO1 | Mechanosensitive ion channel in SC/TM; links pressure to endothelial responses | response to mechanical stimulus; ion transport | Schlemm's canal endothelial cell | UBERON:0001808 Schlemm's canal | mechanotransduction, Ca2+ influx, ANGPT2–integrin loop | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15) |
| TRPV4 | Mechanosensitive Ca2+ channel; mediates TM contractility and OHT | calcium ion transport; regulation of cytoskeleton | trabecular meshwork cell | UBERON:0001772 trabecular meshwork | TRPV4-mediated contractility, Ca2+ signaling, interaction with TGF-β | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 13-15, rusciano2025cellmotilitydynamics pages 11-13) |
| ITGA9 / FAK (PTK2) | Integrin–FAK adhesion signaling; regulates TM/SC cell adhesion & remodeling | cell adhesion; focal adhesion assembly; signal transduction | endothelial / trabecular meshwork cell | UBERON:0001808 Schlemm's canal; UBERON:0001772 trabecular meshwork | integrin–FAK, mechanotransduction, ECM–cytoskeleton coupling | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 11-13, singh2025moleculargatekeepersof pages 2-3) |
| NLRP3 | Inflammasome sensor driving retinal inflammation and pyroptosis | inflammasome activation; inflammatory response | microglial cell (CL:0000129) | UBERON:0000966 retina; UBERON:0001801 optic nerve head | NLRP3 inflammasome, IL-1β release, neuroinflammation | https://doi.org/10.3892/mmr.2025.13757 (2025) (palanivel2025understandingtherole pages 30-34, wang2025researchprogresson pages 1-2) |
| LOXL1 | ECM crosslinking enzyme; linked to exfoliation and ECM stiffening | extracellular matrix organization; collagen fibril crosslinking | extracellular matrix / fibroblast-like TM cells | UBERON:0001772 trabecular meshwork | ECM crosslinking, increased stiffness, outflow resistance | https://doi.org/10.20944/preprints202512.0304.v1 (2025) (rusciano2025cellmotilitydynamics pages 11-13, palanivel2025understandingtherole pages 25-30) |
| VCAM1 | Endothelial adhesion molecule; connects vascular inflammation to ONH injury | leukocyte adhesion; cell–cell adhesion | vascular endothelium / SC endothelium | UBERON:0001801 optic nerve head; UBERON:0001808 Schlemm's canal | endothelial activation, immune cell recruitment, vascular dysregulation | https://doi.org/10.7759/cureus.91633 (2025) (singh2025moleculargatekeepersof pages 2-3, wang2025researchprogresson pages 1-2) |


*Table: Ontology-ready table mapping 12 key genes/proteins to their roles, GO processes, cell types (CL), anatomical sites (UBERON), core mechanisms, and recent evidence (DOIs/years) to support mechanistic curation for a disease knowledge base.*

Limitations
- Some mechanistic details derive from 2025 peer‑reviewed reviews and preprints synthesized from primary literature 2021–2024; where specific 2023–2024 clinical trials and numeric outcomes are requested, additional targeted database queries would refine statistics (rusciano2025cellmotilitydynamics pages 11-13, wang2025researchprogresson pages 1-2).

References with URLs and dates (selection)
- Rusciano D, et al. Cell motility dynamics in glaucoma: mechanisms, pathogenic roles, and therapeutic targeting. Preprint. Dec 2025. https://doi.org/10.20944/preprints202512.0304.v1 (rusciano2025cellmotilitydynamics pages 6-7, rusciano2025cellmotilitydynamics pages 11-13, rusciano2025cellmotilitydynamics pages 13-15)
- Singh P, et al. Molecular gatekeepers of aqueous outflow: from mechanotransduction to gene therapy. Cureus. Sep 2025. https://doi.org/10.7759/cureus.91633 (singh2025moleculargatekeepersof pages 1-2, singh2025moleculargatekeepersof pages 2-3)
- Wang W, et al. Research progress on molecular therapy for glaucoma (Review). Mol Med Rep. Nov 2025. https://doi.org/10.3892/mmr.2025.13757 (wang2025researchprogresson pages 1-2)
- Palanivel V. Understanding the role of neuropeptide Y in glaucoma. 2025. (Excerpts) (palanivel2025understandingtherole pages 30-34, palanivel2025understandingtherole pages 25-30)

References

1. (rusciano2025cellmotilitydynamics pages 6-7): Dario Rusciano, Caterina Gagliano, Alessandro Avitabile, and José Fernando Maya-Vetencourt. Cell motility dynamics in glaucoma: mechanisms, pathogenic roles, and therapeutic targeting. Unknown journal, Dec 2025. URL: https://doi.org/10.20944/preprints202512.0304.v1, doi:10.20944/preprints202512.0304.v1.

2. (rusciano2025cellmotilitydynamics pages 11-13): Dario Rusciano, Caterina Gagliano, Alessandro Avitabile, and José Fernando Maya-Vetencourt. Cell motility dynamics in glaucoma: mechanisms, pathogenic roles, and therapeutic targeting. Unknown journal, Dec 2025. URL: https://doi.org/10.20944/preprints202512.0304.v1, doi:10.20944/preprints202512.0304.v1.

3. (rusciano2025cellmotilitydynamics pages 13-15): Dario Rusciano, Caterina Gagliano, Alessandro Avitabile, and José Fernando Maya-Vetencourt. Cell motility dynamics in glaucoma: mechanisms, pathogenic roles, and therapeutic targeting. Unknown journal, Dec 2025. URL: https://doi.org/10.20944/preprints202512.0304.v1, doi:10.20944/preprints202512.0304.v1.

4. (wang2025researchprogresson pages 1-2): Weiwei Wang, Gangwei Cheng, Qi Zhou, Sheng Wang, and Linyi Zhang. Research progress on molecular therapy for glaucoma (review). Molecular Medicine Reports, 33:1-10, Nov 2025. URL: https://doi.org/10.3892/mmr.2025.13757, doi:10.3892/mmr.2025.13757. This article has 0 citations and is from a peer-reviewed journal.

5. (singh2025moleculargatekeepersof pages 2-3): Priti Singh, Samendra Karkhur, Vidhya Verma, Saroj Gupta, and Arushi Beri. Molecular gatekeepers of aqueous outflow: from mechanotransduction to gene therapy in trabecular meshwork health and disease. Cureus, Sep 2025. URL: https://doi.org/10.7759/cureus.91633, doi:10.7759/cureus.91633. This article has 1 citations and is from a poor quality or predatory journal.

6. (palanivel2025understandingtherole pages 30-34): V Palanivel. Understanding the role of neuropeptide y in ameliorating the degenerative changes in glaucoma. Unknown journal, 2025.

7. (palanivel2025understandingtherole pages 25-30): V Palanivel. Understanding the role of neuropeptide y in ameliorating the degenerative changes in glaucoma. Unknown journal, 2025.

8. (singh2025moleculargatekeepersof pages 1-2): Priti Singh, Samendra Karkhur, Vidhya Verma, Saroj Gupta, and Arushi Beri. Molecular gatekeepers of aqueous outflow: from mechanotransduction to gene therapy in trabecular meshwork health and disease. Cureus, Sep 2025. URL: https://doi.org/10.7759/cureus.91633, doi:10.7759/cureus.91633. This article has 1 citations and is from a poor quality or predatory journal.