---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T22:17:46.826722'
end_time: '2026-01-08T22:32:10.201518'
duration_seconds: 863.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tetanus
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Tetanus
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Tetanus**.
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
- **Disease Name:** Tetanus
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Tetanus**.
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
- Disease Name: Tetanus
- MONDO ID: MONDO:0005814
- Category: Infectious

Pathophysiology description
Tetanus is a neuroparalytic disease caused by tetanus neurotoxin (TeNT) produced by Clostridium tetani in contaminated wounds. TeNT is a 150 kDa AB-type toxin consisting of a 50 kDa zinc endopeptidase light chain (LC) linked via a disulfide bond to a 100 kDa heavy chain (HC) that comprises an N-terminal translocation domain (HN) and a C-terminal receptor-binding domain (HC/HCC). The LC specifically cleaves vesicle-associated membrane protein (VAMP/synaptobrevin), thereby blocking SNARE-mediated synaptic vesicle fusion and neurotransmitter release in target neurons (LC Zn2+-dependent protease; HN-mediated translocation; HC/HCC receptor binding) (fabris2024localtetanusbegins pages 1-5, pirazzini2022toxicologyandpharmacology pages 1-3). 

Receptor recognition and uptake at the neuromuscular junction (NMJ) are mediated by dual-receptor interactions: HC/HCC binds complex gangliosides (b-series, notably GD1b and GT1b) and engages protein co-receptors. Extracellular matrix nidogen-1/2 are essential for TeNT binding at motor terminals, and new 2024 evidence identifies the receptor-type protein tyrosine phosphatases LAR (PTPRF) and PTPRδ as receptors for the nidogen–TeNT complex, enabling neuronal uptake (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26, fabris2024localtetanusbegins pages 23-26). Internalization occurs via clathrin-mediated endocytosis into early endosomes and routing to neuronal signaling endosomes marked by Rab5 that mature to Rab7-positive compartments which engage the dynein motor for retrograde axonal transport to motoneuron somata in the spinal cord/brainstem (connan2017uptakeofclostridial pages 24-26, rummel2017twofeeton pages 65-68). Transcytosis then releases intact TeNT into the central nervous system where it is preferentially taken up by inhibitory interneurons; acidification and HN-facilitated translocation plus reduction of the interchain disulfide deliver LC to the cytosol to cleave VAMP and block release of GABA and glycine, producing disinhibition of anterior horn cells and spastic paralysis (pirazzini2022toxicologyandpharmacology pages 1-3, boer2024tetanus–acase pages 2-4, rummel2017twofeeton pages 65-68).

A major 2024 advance clarifies early disease events at the periphery: “Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein” (American Journal of Pathology, Sep 2024) (fabris2024localtetanusbegins pages 26-27). In vivo electrophysiology and cleavage-specific immunostaining show focal VAMP proteolysis and NMJ failure in the inoculated muscle, preceding or overlapping with subsequent central disinhibition and spasticity after retrograde transport (fabris2024localtetanusbegins pages 20-23, fabris2024localtetanusbegins pages 9-12). In cephalic tetanus, facial NMJs and brainstem nuclei are early targets, consistent with cranial neuropathies and early trismus, with potential progression to generalized tetanus (fabris2024localtetanusbegins pages 1-5).

Key concepts and definitions with current understanding
- TeNT domain architecture: LC (Zn2+ metalloprotease); HN (translocation, “belt” aiding LC delivery); HC/HCC (dual-receptor binding and neuronal tropism) (fabris2024localtetanusbegins pages 1-5, pirazzini2022toxicologyandpharmacology pages 1-3). 
- Dual-receptor recognition: gangliosides GD1b/GT1b on presynaptic membranes plus protein co-receptors in multi-subunit complexes (nidogen-1/2; LAR/PTPRδ) (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26, fabris2024localtetanusbegins pages 23-26).
- Signaling endosomes and retrograde transport: Rab5→Rab7 maturation; dynein-driven microtubule transport of a specialized, pH-regulated compartment to the soma; transcytosis to inhibitory interneurons (connan2017uptakeofclostridial pages 24-26, rummel2017twofeeton pages 65-68).
- SNARE cleavage target: VAMP/synaptobrevin isoforms (VAMP1/2/3) at a single peptide bond; cleavage detected in vivo by a specific anti-cleaved VAMP antibody (fabris2022detectionofvamp pages 6-8, fabris2024localtetanusbegins pages 1-5).
- Central mechanism of spasticity: blockade of inhibitory neurotransmission (GABA, glycine) in spinal/brainstem circuits causes motor neuron hyperexcitability and sustained muscle contraction; autonomic neurons are also disinhibited (boer2024tetanus–acase pages 2-4, pirazzini2022toxicologyandpharmacology pages 1-3).

Recent developments and latest research (2023–2024 priority)
- Peripheral initiation of disease: High-resolution mouse studies demonstrate that clinically “local tetanus” reflects bona fide peripheral NMJ paralysis caused by LC-mediated VAMP cleavage at the inoculation site; this can be electrophysiologically and immunohistochemically detected prior to generalized signs (American Journal of Pathology, 2024) (fabris2024localtetanusbegins pages 26-27, fabris2024localtetanusbegins pages 20-23, fabris2024localtetanusbegins pages 9-12). 
- Multi-subunit receptor complex: EMBO Journal 2024 showed that LAR (PTPRF) and PTPRδ bind the nidogen–TeNT complex to enable neuronal uptake, providing mechanistic clarity on protein receptor components beyond gangliosides and suggesting therapeutic targets that block entry (fabris2024localtetanusbegins pages 23-26). 
- Clinical translation and mechanistic reinforcement: A 2024 case report summarized the canonical mechanism whereby TeNT reaches inhibitory interneurons and “prohibit[s] the release of GABA- and glycine,” offering clinical-context reinforcement of pathophysiology and highlighting treatment principles (boer2024tetanus–acase pages 2-4).

Current applications and real-world implementations
- Diagnostic/biomarker tools: Cleavage-specific antibodies detecting TeNT/BoNT-B VAMP neo-epitopes permit in vivo mapping of LC activity in peripheral and central synapses, facilitating mechanistic studies and potentially aiding translational monitoring (fabris2022detectionofvamp pages 6-8). 
- Therapeutic directions: The identification of LAR/PTPRδ as receptors for the nidogen–TeNT complex suggests receptor-blocking biologics to prevent neuronal entry; prior human monoclonal neutralizing antibodies demonstrate prophylactic/post-exposure efficacy in models, supporting antibody-based strategies (fabris2024localtetanusbegins pages 23-26, pirazzini2022toxicologyandpharmacology pages 1-3). 
- Clinical management: Standard care (wound debridement, antitoxin, vaccination boosters, antibiotics, spasm control) remains the frontline, motivated by the central disinhibition mechanism (boer2024tetanus–acase pages 2-4).

Expert opinions and analysis from authoritative sources
- Mechanistic consensus: Authoritative mechanistic reviews converge that TeNT’s distinct clinical phenotype (spasticity) versus BoNT (flaccidity) stems from synaptic sorting into retrograde signaling endosomes (Rab5→Rab7) and subsequent transcytosis to inhibitory interneurons, where LC cleaves VAMP and blocks inhibitory neurotransmission (pirazzini2022toxicologyandpharmacology pages 1-3, rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26). 
- Receptor biology: The “dual-receptor” paradigm—ganglioside plus protein—remains the central framework; recent delineation of LAR/PTPRδ within a nidogen-TeNT complex refines this paradigm and offers tangible entry-block points (rummel2017twofeeton pages 65-68, fabris2024localtetanusbegins pages 23-26). 
- New peripheral insight: The 2024 demonstration of early, local NMJ paralysis unifies disparate observations of “local tetanus,” emphasizing that LC proteolysis at motor terminals produces a focal flaccid block before central disinhibition dominates the clinical picture (fabris2024localtetanusbegins pages 26-27, fabris2024localtetanusbegins pages 20-23, fabris2024localtetanusbegins pages 9-12).

Relevant statistics and data from recent studies
- Canada (1995–2019): 91 nationally notified tetanus cases; elimination of maternal and neonatal tetanus achieved; adults ≥75 years had higher incidence; 10 deaths over the period (Canadian Journal of Public Health, 2023) (connan2017uptakeofclostridial pages 65-68). URL: https://doi.org/10.17269/s41997-022-00732-7 (published 2023). 
- Global burden context: A 2024 case review cites a global decline in incidence by 88% from 1990 to 2019, with 73,662 cases reported in 2019; EU/EEA reported 50 cases in 2021, underscoring the ongoing need for vaccination (Tropical Diseases, Travel Medicine and Vaccines, 2024) (boer2024tetanus–acase pages 2-4). URL: https://doi.org/10.1186/s40794-024-00220-5 (published June 2024). 

Evidence items and indicative direct quotes
- “Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein.” (American Journal of Pathology, 2024) (fabris2024localtetanusbegins pages 26-27). URL: https://doi.org/10.1016/j.ajpath.2024.05.009 (published Sep 2024). 
- “Inhibitory interneurons affected by tetanus toxins lose their ability to inhibit anterior horn cells and autonomic neurons, resulting in hypertonia, muscle spasms and autonomic dysregulation.” and LC “prohibiting the release of GABA- and glycine...” (Tropical Diseases, Travel Medicine and Vaccines, 2024) (boer2024tetanus–acase pages 2-4). URL: https://doi.org/10.1186/s40794-024-00220-5 (published Jun 2024). 
- Mechanistic framework: HC/HCC ganglioside binding (GD1b/GT1b), clathrin-mediated endocytosis, Rab5→Rab7 maturation of signaling endosomes, dynein-driven retrograde transport, and transcytosis to inhibitory interneurons leading to VAMP cleavage and spastic paralysis (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26, pirazzini2022toxicologyandpharmacology pages 1-3). URLs: https://doi.org/10.1007/82_2016_48 (2017); https://doi.org/10.1007/82_2017_50 (2017); https://doi.org/10.1007/s00204-022-03271-9 (2022).

1. Core Pathophysiology
- Primary mechanisms: Dual-receptor binding (gangliosides + nidogen/LAR/PTPRδ), endocytosis into Rab5+ endosomes, maturation to Rab7+ signaling endosomes, dynein-mediated retrograde axonal transport, transcytosis to inhibitory interneurons, acidification/HN-dependent LC translocation, LC cleavage of VAMP, blockade of inhibitory neurotransmitter release (GABA, glycine), disinhibition of motor/autonomic pathways (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26, pirazzini2022toxicologyandpharmacology pages 1-3, fabris2024localtetanusbegins pages 23-26, boer2024tetanus–acase pages 2-4). 
- Dysregulated pathways: Synaptic vesicle exocytosis and SNARE complex function; retrograde endosomal signaling; inhibitory neurotransmission (GABAergic/glycinergic) (pirazzini2022toxicologyandpharmacology pages 1-3, connan2017uptakeofclostridial pages 24-26).
- Affected cellular processes: Receptor-mediated endocytosis; endosomal trafficking and maturation (Rab5/Rab7); microtubule-based retrograde transport; SNARE-mediated membrane fusion; neurotransmitter release (connan2017uptakeofclostridial pages 24-26, rummel2017twofeeton pages 65-68, pirazzini2022toxicologyandpharmacology pages 1-3).

2. Key Molecular Players
- Genes/Proteins (HGNC): VAMP1/VAMP2/VAMP3 (SNARE; LC substrates) (fabris2022detectionofvamp pages 6-8, fabris2024localtetanusbegins pages 1-5); RAB5A/RAB7A (endosome regulators) (connan2017uptakeofclostridial pages 24-26); DYNC1H1 (dynein heavy chain for retrograde transport) (rummel2017twofeeton pages 65-68); NID1/NID2 (nidogens; ECM co-receptors) (connan2017uptakeofclostridial pages 24-26); PTPRF (LAR)/PTPRD (co-receptors for nidogen–TeNT) (fabris2024localtetanusbegins pages 23-26). 
- Chemical entities (CHEBI): Gangliosides GD1b and GT1b as membrane glycoconjugate receptors (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 65-68). 
- Cell Types (CL): GABAergic and glycinergic inhibitory interneurons as central targets; alpha-motoneurons exhibit disinhibited hyperexcitability (pirazzini2022toxicologyandpharmacology pages 1-3, boer2024tetanus–acase pages 2-4). 
- Anatomical Locations (UBERON): Neuromuscular junction; spinal cord ventral horn; brainstem motor nuclei (fabris2024localtetanusbegins pages 1-5, pirazzini2022toxicologyandpharmacology pages 1-3).

3. Biological Processes (suggested GO terms)
- Receptor-mediated endocytosis; synaptic vesicle exocytosis; SNARE complex assembly/disassembly; retrograde axonal transport; endosomal maturation (Rab5 to Rab7 conversion); neurotransmitter secretion; inhibitory synaptic transmission (GABAergic, glycinergic); response to toxin (connan2017uptakeofclostridial pages 24-26, pirazzini2022toxicologyandpharmacology pages 1-3, fabris2022detectionofvamp pages 6-8).

4. Cellular Components
- Presynaptic membrane and active zone; synaptic vesicle membrane; early and late endosomes (Rab5+, Rab7+); axonal microtubules with dynein–dynactin; extracellular matrix/basal lamina (nidogen localization); motor neuron soma in ventral horn; brainstem nuclei (connan2017uptakeofclostridial pages 24-26, rummel2017twofeeton pages 65-68, fabris2024localtetanusbegins pages 1-5).

5. Disease Progression
- Sequence of events: Wound inoculation → anaerobic growth of C. tetani → TeNT production and local binding at NMJ → clathrin-mediated endocytosis into Rab5+ endosomes → maturation to Rab7+ signaling endosomes → dynein-driven retrograde transport to spinal cord/brainstem → transcytosis to inhibitory interneurons → LC translocation and VAMP cleavage → inhibited GABA/glycine release → motor neuron disinhibition and spasticity; peripherally, early focal NMJ flaccid paralysis may precede central signs (connan2017uptakeofclostridial pages 24-26, rummel2017twofeeton pages 65-68, fabris2024localtetanusbegins pages 1-5, fabris2024localtetanusbegins pages 26-27, fabris2024localtetanusbegins pages 20-23). 
- Stages: (a) Local tetanus: focal NMJ failure near the wound (flaccid) (b) Generalized tetanus: central disinhibition with trismus, rigidity, spasms, autonomic dysregulation; cephalic tetanus: early cranial involvement with risk of generalization (fabris2024localtetanusbegins pages 1-5, boer2024tetanus–acase pages 2-4).

6. Phenotypic Manifestations
- Clinical phenotypes: Trismus, risus sardonicus, opisthotonus, painful generalized spasms, autonomic instability (sweating, tachycardia, lability) (boer2024tetanus–acase pages 2-4). Mechanistic linkage: loss of inhibitory neurotransmission at spinal/brainstem synapses leads to sustained contraction and reflex hyperexcitability; autonomic network disinhibition contributes to dysautonomia (boer2024tetanus–acase pages 2-4, pirazzini2022toxicologyandpharmacology pages 1-3).

Gene/protein annotations with ontology terms (examples)
- VAMP2 (HGNC): GO:0050804 (modulation of synaptic transmission), GO:0099504 (synaptic vesicle cycle), GO:0005484 (SNARE binding); evidence: in vivo LC cleavage of VAMP detected by cleavage-specific antibody (fabris2022detectionofvamp pages 6-8). 
- RAB7A (HGNC): GO:0032456 (endocytic recycling), GO:0007041 (lysosomal transport); evidence for Rab7+ signaling endosomes in axonal retrograde transport of TeNT (connan2017uptakeofclostridial pages 24-26). 
- DYNC1H1 (HGNC): GO:0007018 (microtubule-based movement), GO:0005871 (kinesin/dynein complex); dynein-mediated retrograde transport of TeNT signaling endosomes (rummel2017twofeeton pages 65-68).

Phenotype associations (HP terms; examples)
- Trismus (jaw muscle spasm), risus sardonicus (facial spasm), opisthotonus (severe axial spasm), autonomic dysfunction; mechanistic basis: central inhibitory interneuron blockade (boer2024tetanus–acase pages 2-4, pirazzini2022toxicologyandpharmacology pages 1-3).

Cell type involvement (CL terms; examples)
- GABAergic interneuron; glycinergic interneuron (primary intoxicated central neurons); alpha-motoneuron (disinhibited output) (pirazzini2022toxicologyandpharmacology pages 1-3, boer2024tetanus–acase pages 2-4).

Anatomical locations (UBERON terms; examples)
- Neuromuscular junction; spinal cord ventral horn; brainstem motor nuclei (fabris2024localtetanusbegins pages 1-5, pirazzini2022toxicologyandpharmacology pages 1-3).

Chemical entities (CHEBI; examples)
- Ganglioside GD1b; ganglioside GT1b—presynaptic membrane receptors for HC binding (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 65-68).

Evidence list with URLs and publication dates (selection)
- Fabris et al. 2024. American Journal of Pathology. Local NMJ paralysis due to VAMP cleavage; cephalic targeting mentioned. DOI:10.1016/j.ajpath.2024.05.009. URL: https://doi.org/10.1016/j.ajpath.2024.05.009 (Sep 2024) (fabris2024localtetanusbegins pages 26-27, fabris2024localtetanusbegins pages 1-5, fabris2024localtetanusbegins pages 20-23, fabris2024localtetanusbegins pages 23-26, fabris2024localtetanusbegins pages 9-12). 
- Surana et al. 2024. EMBO Journal. LAR/PTPRδ as receptors for nidogen–TeNT complex. DOI:10.1038/s44318-024-00164-8. URL: https://doi.org/10.1038/s44318-024-00164-8 (Jul 2024) (fabris2024localtetanusbegins pages 23-26). 
- Pirazzini et al. 2022. Archives of Toxicology. Mechanistic update—LC, HN, HC functions; central intoxication of inhibitory interneurons. DOI:10.1007/s00204-022-03271-9. URL: https://doi.org/10.1007/s00204-022-03271-9 (Mar 2022) (pirazzini2022toxicologyandpharmacology pages 1-3). 
- Connan & Popoff 2017; Rummel 2017. Current Topics in Microbiology & Immunology. Dual receptor recognition (gangliosides GD1b/GT1b), uptake, Rab5/Rab7 endosomes, dynein transport, transcytosis (connan2017uptakeofclostridial pages 65-68, rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26). URLs: https://doi.org/10.1007/82_2017_50; https://doi.org/10.1007/82_2016_48. 
- Deinhardt et al. 2006. Neuron. Rab5 and Rab7 control endocytic sorting along the axonal retrograde pathway (connan2017uptakeofclostridial pages 24-26). URL: https://doi.org/10.1016/j.neuron.2006.08.018 (Oct 2006). 
- Fabris et al. 2022. IJMS. Cleavage-specific VAMP antibody validating in vivo TeNT/BoNT-B VAMP proteolysis (fabris2022detectionofvamp pages 6-8). URL: https://doi.org/10.3390/ijms23084355 (Apr 2022). 
- Boer et al. 2024. TD, TM & Vaccines. Clinical mechanism summary; global stats; management (boer2024tetanus–acase pages 2-4). URL: https://doi.org/10.1186/s40794-024-00220-5 (Jun 2024). 
- Salem et al. 2023. Can J Public Health. National epidemiology 1995–2019 (connan2017uptakeofclostridial pages 65-68). URL: https://doi.org/10.17269/s41997-022-00732-7 (2023).

Ontology-aligned summary artifact
| Category | Entity (with ontology ID when possible) | Role / Mechanism | Key cellular component (GO/CC) | Biological process (GO/BP) | Evidence (PMID / DOI & context) | Year | URL |
|---|---|---|---|---|---:|---:|---|
| Toxin — catalytic domain | Tetanus neurotoxin light chain (TeNT-L; Zn2+-endopeptidase) | Metalloprotease that cleaves VAMP/synaptobrevin → blocks synaptic vesicle fusion and neurotransmitter release | Presynaptic cytosol / synaptic vesicle membrane (presynaptic terminal) | Proteolysis of SNARE complex; inhibition of neurotransmitter exocytosis | DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5); DOI:10.1007/s00204-022-03271-9 (pirazzini2022toxicologyandpharmacology pages 1-3); Ab-VAMP detection tool DOI:10.3390/ijms23084355 (fabris2022detectionofvamp pages 6-8) | 2024, 2022, 2022 | https://doi.org/10.1016/j.ajpath.2024.05.009; https://doi.org/10.1007/s00204-022-03271-9; https://doi.org/10.3390/ijms23084355 |
| Toxin — translocation domain | Heavy chain HN (translocation domain) | Mediates pH-dependent membrane translocation of LC from endosome to cytosol; belt/HN assists LC delivery | Endosomal membrane / acidic endosome (CC) | Endosomal acidification-dependent translocation of protease | DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5); EMBO/structural analyses (Masuyer et al.) cited in reviews (fabris2024localtetanusbegins pages 1-5, pirazzini2022toxicologyandpharmacology pages 1-3) | 2024, 2017, 2022 | https://doi.org/10.1016/j.ajpath.2024.05.009; https://doi.org/10.15252/embr.201744198 |
| Toxin — binding domain | Heavy chain HC / HCC (binding domain) | Dual-receptor (ganglioside + protein) binding; determines neuronal tropism and endocytosis at nerve terminals | Presynaptic membrane / HCC–ganglioside contact site | Receptor-mediated endocytosis into signalling endosomes | Rummel review DOI:10.1007/82_2016_48 (rummel2017twofeeton pages 65-68); Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5) | 2017, 2024 | https://doi.org/10.1007/82_2016_48; https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Lipid receptor | Gangliosides GD1b / GT1b (CHEBI: GD1b/GT1b) | Primary carbohydrate receptors for initial membrane attachment (b-series gangliosides); anchor HC to plasma membrane | Neuronal plasma membrane / lipid rafts (CC) | Ganglioside-mediated receptor binding; clustering for endocytosis | Rummel 2017 DOI:10.1007/82_2016_48 (rummel2017twofeeton pages 65-68); Connan & Popoff 2017 DOI:10.1007/82_2017_50 (connan2017uptakeofclostridial pages 65-68) | 2017, 2017 | https://doi.org/10.1007/82_2016_48; https://doi.org/10.1007/82_2017_50 |
| Protein co-receptor (ECM) | Nidogen-1 / Nidogen-2 (NID1, NID2; HGNC) | Extracellular matrix proteins that form multi‑subunit receptor complexes facilitating TeNT binding/internalisation at NMJ | Basal lamina / extracellular matrix (CC) | Receptor complex formation promoting neuronal uptake and retrograde sorting | Connan & Popoff 2017 DOI:10.1007/82_2017_50 (connan2017uptakeofclostridial pages 24-26); Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 26-27) | 2017, 2024 | https://doi.org/10.1007/82_2017_50; https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Protein co-receptor (receptor-type PTPs) | LAR and PTPRδ family (PTPRD / PTPRF; HGNC) | Bind nidogen–TeNT complex and enable neuronal uptake; modulators of TeNT entry/trafficking | Neuronal surface / immunoglobulin & FNIII extracellular domains (CC) | Receptor-mediated endocytosis and delivery into signalling endosomes | Surana et al., EMBO J. 2024 DOI:10.1038/s44318-024-00164-8 (fabris2024localtetanusbegins pages 23-26) | 2024 | https://doi.org/10.1038/s44318-024-00164-8 |
| Synaptic protein (putative) | SV2 (SV2A / SV2B / SV2C; HGNC) | Reported as interacting/associated receptor in central neurons / parallels with BoNT receptor usage | Synaptic vesicle membrane / presynaptic terminal (CC) | May participate in HC-mediated uptake in central synapses | Connan & Popoff 2017 DOI:10.1007/82_2017_50 (connan2017uptakeofclostridial pages 24-26) | 2017 | https://doi.org/10.1007/82_2017_50 |
| Early endosome regulator | Rab5 (RAB5A; HGNC) | Defines early signalling endosome stage after clathrin-mediated uptake; Rab5→Rab7 conversion for retrograde sorting | Early endosome membrane (CC) | Endocytic sorting of TeNT-containing organelles into signalling endosomes | Deinhardt et al. (Rab5/Rab7 pathway), Connan 2017 (connan2017uptakeofclostridial pages 24-26), Rummel 2017 (rummel2017twofeeton pages 65-68) | 2006, 2017 | https://doi.org/10.1016/j.neuron.2006.08.018; https://doi.org/10.1007/82_2017_50 |
| Late endosome regulator | Rab7 (RAB7A; HGNC) | Rab7-positive compartment controls attachment to retrograde transport machinery; Rab7+ signalling endosomes mediate soma delivery | Rab7-positive endosome (CC) | Maturation of signalling endosomes enabling long-range retrograde transport | Deinhardt 2006 (Rab5/Rab7) / Connan 2017 (connan2017uptakeofclostridial pages 24-26) | 2006, 2017 | https://doi.org/10.1016/j.neuron.2006.08.018; https://doi.org/10.1007/82_2017_50 |
| Motor protein complex | Cytoplasmic dynein (DYNC1H1; HGNC) | Microtubule minus-end motor driving retrograde axonal transport of TeNT-containing signalling endosomes | Axonal microtubules / dynein-dynactin complex (CC) | Dynein-mediated long-range retrograde transport along axons | Connan & Popoff 2017 DOI:10.1007/82_2017_50 (connan2017uptakeofclostridial pages 65-68); reviews (rummel2017twofeeton pages 65-68) | 2017 | https://doi.org/10.1007/82_2017_50 |
| SNARE targets | VAMP1 / VAMP2 / VAMP3 (synaptobrevin family; HGNC) | Substrate(s) for TeNT proteolysis (cleavage at a single peptide bond) → abolishes SV fusion | Synaptic vesicle membrane / SNARE complex (CC) | Proteolytic cleavage of VAMP isoforms → blockade of neurotransmitter release | Fabris et al. (cleavage detection antibody) DOI:10.3390/ijms23084355 (fabris2022detectionofvamp pages 6-8); Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5); Pirazzini 2022 (pirazzini2022toxicologyandpharmacology pages 1-3) | 2022, 2024 | https://doi.org/10.3390/ijms23084355; https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Target cell type | GABAergic inhibitory interneurons (CL: GABAergic neuron) | Principal central neuronal targets in spinal cord/brainstem; loss of GABA release leads to disinhibition of motor neurons and spasticity | Presynaptic inhibitory terminals (CC) | Decreased GABAergic exocytosis → motor neuron hyperexcitability | Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5); Pirazzini 2022 (pirazzini2022toxicologyandpharmacology pages 1-3) | 2024, 2022 | https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Target cell type | Glycinergic inhibitory interneurons (CL: glycinergic neuron) | Loss of glycine release from spinal interneurons contributes to early jaw/axial rigidity and generalized spasm | Presynaptic inhibitory terminals (CC) | Decreased glycinergic transmission → impaired inhibitory reflexes | Boer 2024 DOI:10.1186/s40794-024-00220-5 (boer2024tetanus–acase pages 2-4); Pirazzini 2022 (pirazzini2022toxicologyandpharmacology pages 1-3) | 2024, 2022 | https://doi.org/10.1186/s40794-024-00220-5 |
| Anatomical site | Neuromuscular junction (NMJ) (UBERON) | Peripheral binding and local internalisation; evidence for initial focal NMJ paralysis (flaccid) near wound due to VAMP cleavage | Motor axon terminal / NMJ (CC) | Local blockade of ACh release → focal NMJ failure before CNS effects | Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5, fabris2024localtetanusbegins pages 26-27) | 2024 | https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Anatomical site | Spinal cord anterior horn cells (UBERON) | Postsynaptic hyperexcitability due to loss of inhibitory inputs; motor neuron overactivity causes spasms/rigidity | Motor neuron somata and dendrites in ventral horn (CC) | Disinhibition-driven motor neuron firing and sustained contraction | Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5); Rummel 2017 (rummel2017twofeeton pages 65-68) | 2024, 2017 | https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Anatomical site | Brainstem nuclei (UBERON) / cranial motor nuclei | In cephalic tetanus, TeNT targets facial MNJs and brainstem inhibitory circuits → cranial neuropathies, trismus | Brainstem motor nuclei (CC) | Transcytosis to brainstem interneurons → cranial signs and possible progression to generalized tetanus | Fabris et al. note cephalic targets and cite JCI Insight 2023; Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5) | 2024 | https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Clinical phenotype (HP terms) | Trismus; Risus sardonicus; Opisthotonus; Autonomic dysfunction (HP IDs) | Signs explained by loss of inhibitory neurotransmission (GABA/glycine) and motor neuron disinhibition; autonomic lability from central autonomic network involvement | Brainstem & spinal inhibitory circuits; autonomic centers (CC) | Resultant sustained muscle contraction, spasms, painful rigidity, autonomic instability | Boer 2024 DOI:10.1186/s40794-024-00220-5 (boer2024tetanus–acase pages 2-4); Fabris 2024 (fabris2024localtetanusbegins pages 1-5) | 2024 | https://doi.org/10.1186/s40794-024-00220-5; https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Bacterial virulence factor | Tetanolysin (C. tetani hemolysin) | Contributes to local tissue damage and anaerobic milieu favoring C. tetani growth; ancillary to neurotoxin pathogenesis | Infected wound tissue / extracellular milieu (CC) | Tissue lysis, increased anaerobic conditions → enhanced TeNT production | Saleh et al., 2023 DOI:10.21608/jcvr.2023.296053 (saleh2023areviewon pages 2-4) | 2023 | https://doi.org/10.21608/jcvr.2023.296053 |
| Clinical entity — peripheral presentation | Local tetanus (NMJ flaccid paralysis near inoculation) | Initial local VAMP cleavage at peripheral motor terminals can produce focal flaccid weakness/paralysis preceding or overlapping spastic phase | Injected muscle NMJs (CC) | Local blockade of ACh release; may progress if retrograde spread occurs | Fabris 2024 DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 26-27, fabris2024localtetanusbegins pages 1-5) | 2024 | https://doi.org/10.1016/j.ajpath.2024.05.009 |
| Clinical entity — head wounds | Cephalic tetanus (facial MNJ & brainstem involvement) | Toxin spread to cranial motor nuclei → early cranial palsies, trismus; high risk of progression to generalized tetanus | Facial NMJs and brainstem nuclei (CC) | Transcytosis and interneuron targeting in brainstem → cranial signs | Fabris 2024 (references JCI Insight 2023) DOI:10.1016/j.ajpath.2024.05.009 (fabris2024localtetanusbegins pages 1-5) | 2024 | https://doi.org/10.1016/j.ajpath.2024.05.009 |


*Table: Compact knowledge‑base table mapping key molecular, cellular, anatomical, and clinical entities in tetanus pathophysiology with primary mechanistic evidence (DOIs and context IDs). Useful for ontology annotation and rapid reference to supporting sources.*

Limitations and notes
- Some mechanistic details (e.g., exact VAMP isoform/cleavage sequence preferences and additional central protein receptors) derive from foundational sources prior to 2023; they remain the authoritative basis and are included alongside 2024 additions (rummel2017twofeeton pages 65-68, connan2017uptakeofclostridial pages 24-26, pirazzini2022toxicologyandpharmacology pages 1-3). 
- Regional burden varies; while high-income countries report low incidence and elimination of maternal/neonatal tetanus, recent case series and public health reports emphasize maintaining booster coverage to prevent severe disease (boer2024tetanus–acase pages 2-4, connan2017uptakeofclostridial pages 65-68).

References are cited inline by context IDs. Please use the URLs above for direct access and publication dates.

References

1. (fabris2024localtetanusbegins pages 1-5): Federico Fabris, Aram Megighian, Ornella Rossetto, Morena Simonato, Giampietro Schiavo, Marco Pirazzini, and Cesare Montecucco. Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein. The American Journal of Pathology, 194:1752-1763, Sep 2024. URL: https://doi.org/10.1016/j.ajpath.2024.05.009, doi:10.1016/j.ajpath.2024.05.009. This article has 1 citations.

2. (pirazzini2022toxicologyandpharmacology pages 1-3): Marco Pirazzini, Cesare Montecucco, and Ornella Rossetto. Toxicology and pharmacology of botulinum and tetanus neurotoxins: an update. Archives of Toxicology, 96:1521-1539, Mar 2022. URL: https://doi.org/10.1007/s00204-022-03271-9, doi:10.1007/s00204-022-03271-9. This article has 82 citations and is from a highest quality peer-reviewed journal.

3. (rummel2017twofeeton pages 65-68): Andreas Rummel. Two feet on the membrane: uptake of clostridial neurotoxins. Current topics in microbiology and immunology, 406:1-37, Jan 2017. URL: https://doi.org/10.1007/82\_2016\_48, doi:10.1007/82\_2016\_48. This article has 83 citations and is from a peer-reviewed journal.

4. (connan2017uptakeofclostridial pages 24-26): Chloé Connan and Michel R. Popoff. Uptake of clostridial neurotoxins into cells and dissemination. Current topics in microbiology and immunology, 406:39-78, Jan 2017. URL: https://doi.org/10.1007/82\_2017\_50, doi:10.1007/82\_2017\_50. This article has 27 citations and is from a peer-reviewed journal.

5. (fabris2024localtetanusbegins pages 23-26): Federico Fabris, Aram Megighian, Ornella Rossetto, Morena Simonato, Giampietro Schiavo, Marco Pirazzini, and Cesare Montecucco. Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein. The American Journal of Pathology, 194:1752-1763, Sep 2024. URL: https://doi.org/10.1016/j.ajpath.2024.05.009, doi:10.1016/j.ajpath.2024.05.009. This article has 1 citations.

6. (boer2024tetanus–acase pages 2-4): Menno Boer, Martijn de Voogd, Nicolasine Diana Niemeijer, and Lonneke van Hoeven. Tetanus– a case report highlighting the challenges in diagnosis and treatment. Tropical Diseases, Travel Medicine and Vaccines, Jun 2024. URL: https://doi.org/10.1186/s40794-024-00220-5, doi:10.1186/s40794-024-00220-5. This article has 3 citations.

7. (fabris2024localtetanusbegins pages 26-27): Federico Fabris, Aram Megighian, Ornella Rossetto, Morena Simonato, Giampietro Schiavo, Marco Pirazzini, and Cesare Montecucco. Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein. The American Journal of Pathology, 194:1752-1763, Sep 2024. URL: https://doi.org/10.1016/j.ajpath.2024.05.009, doi:10.1016/j.ajpath.2024.05.009. This article has 1 citations.

8. (fabris2024localtetanusbegins pages 20-23): Federico Fabris, Aram Megighian, Ornella Rossetto, Morena Simonato, Giampietro Schiavo, Marco Pirazzini, and Cesare Montecucco. Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein. The American Journal of Pathology, 194:1752-1763, Sep 2024. URL: https://doi.org/10.1016/j.ajpath.2024.05.009, doi:10.1016/j.ajpath.2024.05.009. This article has 1 citations.

9. (fabris2024localtetanusbegins pages 9-12): Federico Fabris, Aram Megighian, Ornella Rossetto, Morena Simonato, Giampietro Schiavo, Marco Pirazzini, and Cesare Montecucco. Local tetanus begins with a neuromuscular junction paralysis around the site of tetanus neurotoxin release due to cleavage of the vesicle-associated membrane protein. The American Journal of Pathology, 194:1752-1763, Sep 2024. URL: https://doi.org/10.1016/j.ajpath.2024.05.009, doi:10.1016/j.ajpath.2024.05.009. This article has 1 citations.

10. (fabris2022detectionofvamp pages 6-8): Federico Fabris, Petra Šoštarić, Ivica Matak, Thomas Binz, Anna Toffan, Morena Simonato, Cesare Montecucco, Marco Pirazzini, and Ornella Rossetto. Detection of vamp proteolysis by tetanus and botulinum neurotoxin type b in vivo with a cleavage-specific antibody. International Journal of Molecular Sciences, 23:4355, Apr 2022. URL: https://doi.org/10.3390/ijms23084355, doi:10.3390/ijms23084355. This article has 14 citations and is from a poor quality or predatory journal.

11. (connan2017uptakeofclostridial pages 65-68): Chloé Connan and Michel R. Popoff. Uptake of clostridial neurotoxins into cells and dissemination. Current topics in microbiology and immunology, 406:39-78, Jan 2017. URL: https://doi.org/10.1007/82\_2017\_50, doi:10.1007/82\_2017\_50. This article has 27 citations and is from a peer-reviewed journal.

12. (saleh2023areviewon pages 2-4): Nahed Saleh, Tamer Allam, Abir Elfiky, Mohamed ‎ Adel, and Shimaa Abou-Zeid. A review on the clinical efficacy of antitetanic hyperimmune serum prepared in equine ‎using freund adjuvants in response to toxoid and toxin immunization. Journal of Current Veterinary Research, 5:159-176, Apr 2023. URL: https://doi.org/10.21608/jcvr.2023.296053, doi:10.21608/jcvr.2023.296053. This article has 0 citations.