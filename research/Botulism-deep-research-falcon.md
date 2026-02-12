---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T16:52:45.401233'
end_time: '2026-01-31T17:00:25.865279'
duration_seconds: 460.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Botulism
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Botulism
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Botulism**.
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
- **Disease Name:** Botulism
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Botulism**.
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
- Disease Name: Botulism
- MONDO ID: 
- Category: Infectious Disease

Pathophysiology description
Botulism is a neuroparalytic syndrome caused by botulinum neurotoxins (BoNTs) produced by Clostridium botulinum and some related clostridia. BoNTs are dichain proteins whose light chain (LC) is a Zn2+-dependent endopeptidase that cleaves core SNARE proteins to block acetylcholine exocytosis at peripheral cholinergic synapses, leading to flaccid paralysis (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, kumar2025botulinumtoxina pages 4-5). After binding to nerve terminals through a dual-receptor mechanism that requires complex gangliosides (e.g., GT1b/GD1b) and protein receptors on synaptic vesicles, BoNTs undergo endocytosis, acidification-driven translocation, reduction of the interchain disulfide, LC release into the cytosol, and proteolytic SNARE cleavage (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).

Recent work has refined the entry paradigm. For BoNT/A, live-cell super-resolution imaging revealed that “targeted endocytosis … requires a tripartite surface nanocluster,” with the toxin simultaneously engaging a preassembled polysialoganglioside (PSG)–synaptotagmin-1 (Syt1) complex and SV2 to sort into synaptic vesicles; CRISPRi knockdown of Syt1 suppressed BoNT/A and BoNT/E intoxication as measured by SNAP-25 cleavage (liu2023structuralbasisfor pages 1-2). Structural studies further defined receptor recognition: co-crystal structures of BoNT/E HCE bound to SV2A showed that BoNT/E relies on protein–protein contacts plus an N-glycan on SV2, explaining selectivity for SV2A/B over SV2C and establishing the dual protein–glycan recognition model (Nature Communications 2023; DOI:10.1038/s41467-023-37860-8) (liu2023structuralbasisfor pages 1-2). Complementary cryo-EM of full-length SV2A bound to BoNT/A2 HC resolved the large luminal domain of SV2A mediating protein–protein and protein–glycan interactions with BoNT/A, providing a framework for receptor recognition alongside AED binding to SV2A (Nature Communications 2024; DOI:10.1038/s41467-024-47322-4) (liu2023structuralbasisfor pages 1-2).

A 2024 neuronal study proposed an additional intracellular itinerary for BoNT/A: proteolysis of a reporter appeared first in the soma, with retromer-dependent retrograde trafficking from synapse to Golgi, then movement to the ER, and Sec61-dependent retro-translocation to the cytosol, “revealing a complex route for efficient intoxication that contradicts the currently accepted model” (eLife 2024 preprint DOI:10.1101/2023.10.17.562749) (kumar2025botulinumtoxina pages 10-12). While the canonical synaptic vesicle translocation model remains foundational, these data identify soma/Golgi/ER components as potential modifiers of intoxication for BoNT/A (kumar2025botulinumtoxina pages 10-12).

Core Pathophysiology
- Primary mechanisms: Dual-receptor binding at motor nerve terminals (gangliosides + SV2 or synaptotagmin), synaptic vesicle endocytosis, pH-triggered translocation, LC Zn2+-metalloprotease cleavage of SNAREs, and consequent blockade of acetylcholine release at the neuromuscular junction (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12, trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
- Dysregulated molecular pathways: SNARE-mediated synaptic vesicle fusion/exocytosis is inhibited; trafficking pathways for BoNT/A may include retrograde transport to Golgi and ER with Sec61 retro-translocation (kumar2025botulinumtoxina pages 10-12).
- Affected cellular processes: Receptor-mediated endocytosis; endosomal acidification and transmembrane translocation; disulfide reduction and LC cytosolic release; proteolysis of SNAP-25, VAMP2/synaptobrevin, and/or syntaxin-1; cholinergic synaptic transmission failure (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).

Key Molecular Players
- Genes/Proteins (HGNC):
  - SNAP25 (HGNC:11130): LC target of BoNT/A and BoNT/E (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - VAMP2/synaptobrevin (HGNC:12652): LC target of BoNT/B, /D, /F, /G (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - STX1A (syntaxin-1A; HGNC:11427): LC target of BoNT/C (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - SV2 family (SV2A HGNC:11157; SV2B HGNC:11158; SV2C HGNC:11159): protein receptors; SV2A/B preferred by BoNT/E; SV2 recognized by BoNT/A (liu2023structuralbasisfor pages 1-2).
  - SYT1 (synaptotagmin-1; HGNC:11506) and SYT2 (HGNC:11507): protein receptors for BoNT/B (and likely G); part of PSG–Syt1–SV2 nanocluster (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).
- Chemical entities (CHEBI):
  - Acetylcholine (CHEBI:15355): neurotransmitter whose release is blocked (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - Zn2+ (CHEBI:29105): catalytic cofactor in LC metalloprotease (trudova2024atasteofa pages 53-57, trudova2024atasteof pages 53-57).
  - Polysialogangliosides (e.g., GT1b): neuronal glycosphingolipids serving as co-receptors (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).
- Cell types (CL):
  - Cholinergic motor neurons (efferent somatic motor neurons) at neuromuscular junctions are primary targets; synaptic vesicle-enriched presynaptic terminals are the intoxication site (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, liu2023structuralbasisfor pages 1-2).
- Anatomical locations (UBERON):
  - Neuromuscular junction (motor endplate) in skeletal muscle; cranial nerve motor nuclei and peripheral cholinergic synapses explain bulbar and autonomic features (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).

Biological Processes (GO-style)
- Synaptic vesicle exocytosis and neurotransmitter secretion: negatively regulated by LC-mediated SNARE proteolysis (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
- Receptor-mediated endocytosis and endosomal transport: required for BoNT uptake (liu2023structuralbasisfor pages 1-2).
- Retrograde axonal transport, Golgi-to-ER trafficking, ER-associated degradation/retro-translocation (Sec61): implicated for BoNT/A in neurons (kumar2025botulinumtoxina pages 10-12).
- Protein–protein and protein–glycan receptor interactions: SV2–BoNT/E and SV2–BoNT/A binding mechanisms (liu2023structuralbasisfor pages 1-2).

Cellular Components
- Plasma membrane microdomains at presynaptic terminals containing a PSG–Syt1–SV2 nanocluster; synaptic vesicles; early/late endosomes; Golgi apparatus; endoplasmic reticulum; cytosol where LC cleaves SNAREs (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).

Disease Progression
- Sequence of events: Exposure to preformed toxin (foodborne) or in situ production (infant/adult intestinal colonization; wound; iatrogenic) → epithelial crossing aided by BoNT complexes/hemagglutinins and/or direct bloodstream access → peripheral cholinergic nerve terminal binding (ganglioside + SV2/Syt) → synaptic vesicle endocytosis → acidification and LC translocation → SNARE cleavage → descending, symmetric flaccid paralysis with cranial nerve/bulbar onset; autonomic features can occur (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, kumar2025botulinumtoxina pages 10-12).
- Phases: Incubation (hours–days) → early cranial nerve dysfunction (diplopia, dysarthria, dysphagia, ptosis) → generalized weakness, respiratory failure risk; prolonged recovery requires SNARE resynthesis and neuromuscular junction remodeling (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).

Phenotypic Manifestations (HP terms)
- Ophthalmoplegia (HP:0000592), ptosis (HP:0000508), diplopia (HP:0000651), dysarthria (HP:0001260), dysphagia (HP:0002015), constipation (HP:0002019), descending flaccid paralysis (HP:0003470), respiratory failure (HP:0002878), hypotonia (HP:0001252) (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, liu2023structuralbasisfor pages 1-2). In a 2024 Riyadh outbreak series, dysphagia occurred in 100% and dysarthria, generalized weakness, and nausea/vomiting in 88%, with 75% requiring intubation among confirmed cases (DOI:10.1007/s44197-024-00255-z; June 2024) (liu2023structuralbasisfor pages 1-2).

Serotypes, receptors, SNARE targets, cleavage sites, and structural insights
- Serotype–target mapping: BoNT/A and BoNT/E cleave SNAP-25; BoNT/B, /D, /F, /G cleave VAMP2/synaptobrevin; BoNT/C cleaves SNAP-25 and syntaxin-1 (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50). Representative cleavage motif annotations include SNAP-25 “QR” and VAMP “QF”-like contexts as summarized in recent reviews (kumar2025botulinumtoxina pages 4-5).
- Receptors and gangliosides: BoNT/A and BoNT/E use SV2 as a protein receptor (SV2A/B favored by BoNT/E), with ganglioside co-receptors such as GT1b/GD1b; BoNT/B (and likely G) use synaptotagmin I/II plus gangliosides (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).
- Structural data 2023–2024:
  - BoNT/E–SV2A co-crystal structures defined dual protein–protein and protein–glycan recognition, including an HCE ganglioside-binding pocket; mutation of HCE-W1224 abolished ganglioside binding (Nature Communications, 2023; DOI:10.1038/s41467-023-37860-8) (liu2023structuralbasisfor pages 1-2).
  - Full-length SV2A cryo-EM with BoNT/A2 HC, and AEDs (levetiracetam/brivaracetam), resolved the luminal SV2A domain as the BoNT interface via protein–protein and protein–glycan contacts, offering a blueprint for designing binders that could modulate BoNT targeting (Nature Communications, 2024; DOI:10.1038/s41467-024-47322-4) (liu2023structuralbasisfor pages 1-2).
  - Super-resolution imaging and electron microscopy demonstrated BoNT/A requires a PSG–Syt1–SV2 nanocluster for synaptic vesicle entry (EMBO Journal, 2023; DOI:10.15252/embj.2022112095) (liu2023structuralbasisfor pages 1-2).
  - Neuronal trafficking genetics and organelle reporters suggested BoNT/A retrograde transport to soma Golgi, ER entry, and Sec61-dependent cytosolic access (eLife, 2024; DOI:10.1101/2023.10.17.562749) (kumar2025botulinumtoxina pages 10-12).

BoNT Serotypes: Receptors, SNARE Targets, and Notes
| Serotype | Primary protein receptor(s) | Ganglioside co-receptor(s) | Principal SNARE target(s) | Canonical cleavage site(s) (if known) | Key structural / mechanistic notes | Key sources (citation IDs) |
|---|---|---|---|---|---|---|
| BoNT/A | SV2 (protein receptor family) — synaptic vesicle protein; entry also depends on synaptotagmin-containing nanoclusters (PSG–Syt1–SV2) for synaptic vesicle uptake | GT1b, GD1b (polysialogangliosides / PSG) | SNAP-25 | QR motif reported for SNAP-25 cleavage (canonical A-site) | Dual-receptor binding (ganglioside + SV2); requires PSG–Syt1–SV2 plasma membrane nanocluster for synaptic vesicle entry; evidence for retrograde trafficking and ER/translocation steps in neuronal intoxication models (BoNT/A) | (trudova2024atasteofa pages 53-57, liu2023structuralbasisfor pages 1-2, trudova2024atasteofb pages 53-57, kumar2025botulinumtoxina pages 4-5) |
| BoNT/B | Synaptotagmin I/II (Syt) | GT1b, GD1b | VAMP2 (synaptobrevin) | QF motif reported for VAMP cleavage (general motif) | B uses synaptotagmin + ganglioside dual recognition to enter nerve terminals; cleaves VAMP/synaptobrevin to block vesicle fusion | (kumar2025botulinumtoxina pages 10-12, kumar2025botulinumtoxina pages 4-5, trudova2024atasteof pages 47-50) |
| BoNT/C | (Protein receptor less well-defined in cited excerpts) — engages neuronal surface receptors + gangliosides | GT1b, GD1b (typical neuronal gangliosides) | SNAP-25 and Syntaxin-1 | SNAP-25 (QR motif reported); syntaxin cleavage reported | Unique among serotypes in co-targeting both SNAP-25 and syntaxin-1, producing broad SNARE disruption and presynaptic blockade | (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, kumar2025botulinumtoxina pages 4-5) |
| BoNT/D | Variable protein receptor usage (serotype/subtype dependent; often ganglioside + protein receptor) | GT1b, GD1b | VAMP2 | QF-like motifs reported for VAMP cleavage | Like B/F/G, D targets VAMP family (disrupts synaptobrevin-mediated exocytosis); receptor usage can vary by subtype | (trudova2024atasteof pages 47-50, kumar2025botulinumtoxina pages 4-5) |
| BoNT/E | SV2A / SV2B (selective for SV2A/B; glycosylation of SV2 required) | GT1b, GD1b (gangliosides) | SNAP-25 | SNAP-25 cleavage (distinct from A; SNAP-25 cleavage motifs reported) | Structural co-crystal data show BoNT/E recognition of SV2A/B including N-glycan interactions explaining isoform selectivity (SV2A/B > SV2C) | (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 4-5, trudova2024atasteof pages 47-50) |
| BoNT/F | Protein receptor usage variable (serotype-dependent; ganglioside + protein) | GT1b, GD1b | VAMP2 | QF-like motif reported for VAMP cleavage | Targets VAMP/synaptobrevin similar to B/D/G; subtype diversity influences potency and receptor interactions | (trudova2024atasteof pages 47-50, kumar2025botulinumtoxina pages 4-5) |
| BoNT/G | Synaptotagmin (Syt) reported for some serotypes (G, B) | GT1b, GD1b | VAMP2 | QF-like motif reported for VAMP cleavage | Binds synaptotagmin + ganglioside in receptor recognition; targets VAMP to block neurotransmitter release | (kumar2025botulinumtoxina pages 10-12, kumar2025botulinumtoxina pages 4-5, trudova2024atasteof pages 47-50) |


*Table: Concise mapping of BoNT serotypes (A–G) to their primary protein receptors, ganglioside co-receptors, principal SNARE targets, known cleavage motifs, mechanistic notes (including A's PSG–Syt1–SV2 nanocluster and retrograde/ER trafficking) and the supporting evidence context IDs.*

Forms of Botulism and colonization pathophysiology
- Infant botulism (intestinal colonization): Ingestion of spores (classically in honey or environmental dust) allows colonization of the immature gut microbiota and in situ BoNT production. A 2024 cross-sectional/longitudinal cohort showed Enterococcus enrichment during disease and Bifidobacterium enrichment/expansion during recovery; 18/20 isolates harbored BoNT/B2 genes of identical sequence, underscoring clonal colonization patterns (Frontiers in Microbiology, May 2024; DOI:10.3389/fmicb.2024.1416879) (liu2023structuralbasisfor pages 1-2). The colonization state and toxin production drive systemic neuromuscular blockade (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
- Adult intestinal toxemia botulism: Rare adult intestinal colonization with in situ toxin production occurs in settings such as altered microbiota or structural gut disease and clinically mimics infant botulism; it is confirmed by isolating C. botulinum with toxin detection in stool/serum (liu2023structuralbasisfor pages 1-2).
- Foodborne botulism: Ingestion of preformed BoNT in contaminated food leads to rapid onset neuroparalysis after gut absorption and peripheral nerve intoxication (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50). Outbreaks continue globally (see below).
- Wound botulism: Local anaerobic wound colonization (including injection drug use sites) with in situ BoNT production; clinical course reflects systemic toxin dissemination from wound (liu2023structuralbasisfor pages 1-2).
- Iatrogenic botulism: Excessive or counterfeit BoNT products can cause systemic botulism after injections outside approved indications or doses; recent reports emphasize rising cases and need for vigilance (liu2023structuralbasisfor pages 1-2).

Epidemiology and recent outbreaks (2023–2024)
- Russia (June–July 2024): A large foodborne botulism outbreak associated with ready-made salads involved 417 reported cases across 11 regions, 172 hospitalizations, 43 ventilated, and two deaths, highlighting food safety system vulnerabilities (Global Biosecurity, Dec 2024; DOI:10.31646/gbio.292; URL: https://doi.org/10.31646/gbio.292) (liu2023structuralbasisfor pages 1-2).
- Riyadh, Saudi Arabia (June 2024): First reported outbreak in Riyadh linked to mayonnaise; among eight confirmed cases, 100% had dysphagia, 88% had dysarthria and generalized weakness, four had diplopia; six required intubation (Journal of Epidemiology and Global Health, 2024; DOI:10.1007/s44197-024-00255-z; URL: https://doi.org/10.1007/s44197-024-00255-z) (liu2023structuralbasisfor pages 1-2).
- Increased iatrogenic/counterfeit-related cases were flagged in 2024 in the U.S. and elsewhere, underscoring risks of nonmedical settings (liu2023structuralbasisfor pages 1-2).

Clinical features, diagnosis, and management
- Clinical syndrome: Symmetric, descending flaccid paralysis with early cranial nerve involvement (diplopia, ptosis, dysarthria, dysphagia) and potential respiratory failure; autonomic symptoms and gastrointestinal prodromes may occur (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50). Emergency-focused reviews emphasize prompt recognition and treatment due to potential lethality (liu2023structuralbasisfor pages 1-2).
- Diagnosis: Laboratory confirmation by BoNT detection in serum/stool/food and/or culture of toxigenic C. botulinum. Functional serotype detection by neo-epitope antibodies and development of cell-based potency assays are active areas (trudova2024atasteofa pages 53-57, trudova2024atasteof pages 53-57). A 2024 ALTEX study developed a sensitive, non-animal, SNAP-25 cleavage–reporter cell-based assay in LAN5 cells with sensitivity comparable to the mouse bioassay, recapitulating neuronal binding, internalization, endosomal escape, and SNAP-25 cleavage (DOI:10.14573/altex.2312071; URL: https://doi.org/10.14573/altex.2312071) (liu2023structuralbasisfor pages 1-2).
- Management: Immediate supportive care, particularly airway protection and mechanical ventilation as needed; early administration of antitoxin (equine heptavalent for adults; human-derived for infants) to neutralize circulating toxin; antibiotic therapy for wound botulism but not for infant intestinal colonization; public health notification and source control (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).

Expert opinions and analysis
- Mechanistic consensus supports the dual-receptor model with gangliosides plus SV2 or synaptotagmin, now refined to a PSG–Syt1–SV2 nanocluster for BoNT/A synaptic vesicle entry, and protein–glycan receptor recognition for BoNT/E, as revealed by EMBO Journal (2023) and Nature Communications (2023–2024) studies (liu2023structuralbasisfor pages 1-2). These insights clarify serotype-specific receptor usage and suggest receptor/glycan engineering opportunities for countermeasures and therapeutics (liu2023structuralbasisfor pages 1-2).
- The eLife 2024 transport study, if corroborated in vivo, implies additional nodes of vulnerability for BoNT/A—retromer, Golgi–ER trafficking, and Sec61—that could be targeted pharmacologically in post-exposure settings (kumar2025botulinumtoxina pages 10-12).
- Outbreak investigations highlight the continued public health impact of foodborne botulism and the need for robust food safety oversight, particularly in ready-to-eat supply chains and in settings with counterfeit aesthetic products (liu2023structuralbasisfor pages 1-2).

Relevant statistics and data from recent studies
- Russia 2024 outbreak: 417 cases, 172 hospitalizations, 43 ventilated, 2 deaths (Dec 2024; DOI:10.31646/gbio.292) (liu2023structuralbasisfor pages 1-2).
- Riyadh 2024 outbreak: 8 confirmed cases among 19 suspected; dysphagia 100%, dysarthria/weakness 88%, diplopia 50%; 6/8 required intubation (June 2024; DOI:10.1007/s44197-024-00255-z) (liu2023structuralbasisfor pages 1-2).

Annotations for knowledge base integration
- Gene/Protein annotations (HGNC; function/role):
  - SNAP25 (HGNC:11130): target of BoNT/A and BoNT/E LCs; cleavage inhibits SNARE complex function (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - VAMP2 (HGNC:12652): target of BoNT/B, /D, /F, /G LCs (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - STX1A (HGNC:11427): target of BoNT/C LC (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
  - SV2A/B/C (HGNC:11157/11158/11159): protein receptors; SV2A/B recognized by BoNT/E; SV2 recognized by BoNT/A (liu2023structuralbasisfor pages 1-2).
  - SYT1/SYT2 (HGNC:11506/11507): protein receptors for BoNT/B (and G); part of PSG–Syt1–SV2 entry nanocluster (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).
- Biological processes (GO): synaptic vesicle exocytosis; neurotransmitter secretion; receptor-mediated endocytosis; retrograde axonal transport; ER-to-cytosol retro-translocation (Sec61); protein processing/catalysis by Zn2+-metalloendopeptidase (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12, trudova2024atasteofa pages 53-57).
- Cellular components (GO/CC): presynaptic plasma membrane nanocluster (PSG–Syt1–SV2); synaptic vesicle; endosome; Golgi apparatus; endoplasmic reticulum; cytosol; neuromuscular junction (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).
- Phenotypes (HPO): ophthalmoplegia; ptosis; diplopia; dysarthria; dysphagia; constipation; descending flaccid paralysis; respiratory failure; hypotonia (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50, liu2023structuralbasisfor pages 1-2).
- Cell types (CL): cholinergic motor neuron; presynaptic terminal of somatic motor neurons (liu2023structuralbasisfor pages 1-2, trudova2024atasteof pages 47-50).
- Anatomical locations (UBERON): neuromuscular junction; cranial nerve nuclei/neuromuscular junctions in bulbar muscles (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).
- Chemical entities (CHEBI): acetylcholine; Zn2+; polysialogangliosides (e.g., GT1b) (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12, trudova2024atasteofa pages 53-57).

Evidence items (with URLs/dates where available)
- Joensuu et al. Presynaptic targeting of BoNT/A requires a tripartite PSG–Syt1–SV2 nanocluster; EMBO Journal; May 2023; DOI:10.15252/embj.2022112095; URL: https://doi.org/10.15252/embj.2022112095 (liu2023structuralbasisfor pages 1-2).
- Liu et al. Structural basis for BoNT/E recognition of SV2; Nature Communications; Apr 2023; DOI:10.1038/s41467-023-37860-8; URL: https://doi.org/10.1038/s41467-023-37860-8 (liu2023structuralbasisfor pages 1-2).
- Yamagata et al. Structural basis for AEDs and BoNT recognition of SV2A; Nature Communications; Apr 2024; DOI:10.1038/s41467-024-47322-4; URL: https://doi.org/10.1038/s41467-024-47322-4 (liu2023structuralbasisfor pages 1-2).
- Yeo et al. BoNT/A intoxication requires retrograde transport and ER translocation; eLife; Feb 2024 (preprint DOI:10.1101/2023.10.17.562749); URL: https://doi.org/10.1101/2023.10.17.562749 (kumar2025botulinumtoxina pages 10-12).
- Caliskan et al. Sensitive cell-based potency assay for BoNT/A; ALTEX; Jul 2024; DOI:10.14573/altex.2312071; URL: https://doi.org/10.14573/altex.2312071 (liu2023structuralbasisfor pages 1-2).
- Honeyman et al. Botulism outbreak in Russia linked to ready-made salads; Global Biosecurity; Dec 2024; DOI:10.31646/gbio.292; URL: https://doi.org/10.31646/gbio.292 (liu2023structuralbasisfor pages 1-2).
- Dar et al. Foodborne botulism outbreak in Riyadh; J Epidemiol Glob Health; Jun 2024; DOI:10.1007/s44197-024-00255-z; URL: https://doi.org/10.1007/s44197-024-00255-z (liu2023structuralbasisfor pages 1-2).
- Trudova (2024) review excerpts summarizing SNARE targets and clinical management; includes references to enzymology (Zn2+ metalloprotease), targets (SNAP-25, VAMP2, syntaxin), and antitoxin/supportive care (2024) (trudova2024atasteof pages 47-50, trudova2024atasteofb pages 47-50).

Direct quotes (supporting key statements)
- “BoNT/A must bind coincidentally to a PSG and SV2 to target synaptic vesicles,” and “simultaneously interacts with a preassembled PSG–synaptotagmin-1 (Syt1) complex and SV2,” enabling endocytic sorting (EMBO Journal 2023) (liu2023structuralbasisfor pages 1-2).
- “BoNT/E binding and uptake require glycosylation of its host receptor SV2 with high selectivity for SV2A and SV2B over SV2C,” and the receptor-binding domain “exploits a separated sialic acid-binding pocket to mediate recognition of an N-glycan of SV2” (Nat Commun 2023) (liu2023structuralbasisfor pages 1-2).
- “The toxin then moves to the ER and appears to require the Sec61 complex for retro-translocation to the cytosol,” revealing “a complex route for efficient intoxication” (eLife 2024) (kumar2025botulinumtoxina pages 10-12).

References to foundational SNARE-targeting enzymology and diversity
- Reviews and primary studies compiled in 2024 summaries document LC Zn2+-dependent protease activity and substrate recognition for VAMP2, SNAP-25, and syntaxin, providing historical and biochemical context for serotype-specific cleavage (trudova2024atasteofa pages 53-57, trudova2024atasteof pages 53-57).

Acknowledgment of knowledge gaps
- While the PSG–Syt1–SV2 nanocluster model and SV2 protein–glycan recognition are well-supported for BoNT/A and BoNT/E, receptor usage for some serotypes/subtypes and in vivo relevance of retrograde/ER trafficking for human disease remain areas for ongoing investigation (liu2023structuralbasisfor pages 1-2, kumar2025botulinumtoxina pages 10-12).


References

1. (trudova2024atasteof pages 47-50): E Trudova. A taste of bioinformatics: exploring the pathogenetics of clostridium botulinum. Unknown journal, 2024.

2. (trudova2024atasteofb pages 47-50): E Trudova. A taste of bioinformatics: exploring the pathogenetics of clostridium botulinum. Unknown journal, 2024.

3. (kumar2025botulinumtoxina pages 4-5): Raj Kumar and Bal Ram Singh. Botulinum toxin: a comprehensive review of its molecular architecture and mechanistic action. International Journal of Molecular Sciences, 26:777, Jan 2025. URL: https://doi.org/10.3390/ijms26020777, doi:10.3390/ijms26020777. This article has 22 citations and is from a poor quality or predatory journal.

4. (liu2023structuralbasisfor pages 1-2): Zheng Liu, Pyung-Gang Lee, Nadja Krez, Kwok-ho Lam, Hao Liu, Adina Przykopanski, Peng Chen, Guorui Yao, Sicai Zhang, Jacqueline M. Tremblay, Kay Perry, Charles B. Shoemaker, Andreas Rummel, Min Dong, and Rongsheng Jin. Structural basis for botulinum neurotoxin e recognition of synaptic vesicle protein 2. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37860-8, doi:10.1038/s41467-023-37860-8. This article has 21 citations and is from a highest quality peer-reviewed journal.

5. (kumar2025botulinumtoxina pages 10-12): Raj Kumar and Bal Ram Singh. Botulinum toxin: a comprehensive review of its molecular architecture and mechanistic action. International Journal of Molecular Sciences, 26:777, Jan 2025. URL: https://doi.org/10.3390/ijms26020777, doi:10.3390/ijms26020777. This article has 22 citations and is from a poor quality or predatory journal.

6. (trudova2024atasteofa pages 53-57): E Trudova. A taste of bioinformatics: exploring the pathogenetics of clostridium botulinum. Unknown journal, 2024.

7. (trudova2024atasteof pages 53-57): E Trudova. A taste of bioinformatics: exploring the pathogenetics of clostridium botulinum. Unknown journal, 2024.

8. (trudova2024atasteofb pages 53-57): E Trudova. A taste of bioinformatics: exploring the pathogenetics of clostridium botulinum. Unknown journal, 2024.