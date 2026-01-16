---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T10:05:01.844506'
end_time: '2026-01-08T10:15:10.152690'
duration_seconds: 608.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Semicircular Canal Dehiscence Syndrome
  mondo_id: ''
  category: Structural
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
- **Disease Name:** Semicircular Canal Dehiscence Syndrome
- **MONDO ID:**  (if available)
- **Category:** Structural

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Semicircular Canal Dehiscence Syndrome**.
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
- **Disease Name:** Semicircular Canal Dehiscence Syndrome
- **MONDO ID:**  (if available)
- **Category:** Structural

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Semicircular Canal Dehiscence Syndrome**.
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
Objective 1 (completed): Identify recent (2023–2024) and foundational sources on semicircular canal dehiscence/third-window pathophysiology.
Objective 2 (completed): Extract mechanistic evidence (molecular, cellular, biomechanical) and diagnostic correlates (audiometry, VEMPs) from full texts.
Objective 3 (completed): Expand evidence via citation-chasing as needed to cover bone remodeling biology.
Objective 4 (completed): Map entities to ontologies (HGNC, GO, HP, CL, UBERON, CHEBI) and prepare supporting artifact.
Objective 5 (completed): Synthesize into a comprehensive, well-cited report with URLs and publication dates.
Objective 6 (completed): Submit the final answer.

Disease Pathophysiology Research Report
Target Disease
- Disease Name: Semicircular Canal Dehiscence Syndrome (typically superior SCDS)
- MONDO ID: not firmly established (entity often covered under third-window syndromes)
- Category: Structural

Pathophysiology Description
Core concept: A dehiscence (or extreme thinning) of otic capsule bone over a semicircular canal creates a pathological “third mobile window,” which lowers impedance on the vestibular side of the inner ear and shunts acoustic and pressure energy away from the cochlea toward the dehiscence. This redistributes fluid pressures, alters cochlear and vestibular mechanics, and produces the characteristic combination of low-frequency air–bone gaps (pseudoconductive hearing loss), supranormal bone conduction, and sound/pressure-induced vestibular symptoms (Tullio/Hennebert signs). Mechanistically, to generate conductive hearing loss the third window must be on the scala vestibuli side; patching/plugging the dehiscence can resolve the air–bone gap (mechanistic proof) (Apr 2008, Otology & Neurotology; https://doi.org/10.1097/mao.0b013e318161ab24) (merchant2008conductivehearingloss pages 4-5).

Hydromechanics and vestibular activation: The third window introduces a low-impedance pathway; “a third window will introduce a low mechanical impedance,” shunting sound/pressure, generating large transmembrane pressure gradients and traveling waves in the membranous labyrinth, with outbound flow at the dehiscence balancing inflow at the oval window (Aug 2020, Frontiers in Neurology; https://doi.org/10.3389/fneur.2020.00891) (iversen2020biomechanicsofthird pages 6-7). These waves drive hair-bundle vibration at stimulus frequency (phase-locked irregular afferent firing) and, via nonlinear fluid interactions, endolymph pumping that deflects the cupula (sustained firing in regular afferents). Plugging abolishes these phase-locked responses, consistent with mechanical origin (iversen2020biomechanicsofthird pages 6-7).

Histopathology and anatomy: Temporal bone histology from a clinically diagnosed SCDS case showed a focal bony defect (1.4 × 0.6 mm) with dura directly contacting the endosteum and membranous duct at the defect; notably, “No osteoclastic process was evident within the otic capsule,” and sensory epithelia were preserved without hydrops—supporting a developmental thin-bone predisposition with trauma trigger (Jan 2012, Annals of Otology, Rhinology & Laryngology; https://doi.org/10.1177/000348941212100102) (teixido2012histopathologyofthe pages 1-2).

Bone biology/remodeling: The otic capsule exhibits unique bone physiology with greatly suppressed remodeling. Osteoprotegerin (OPG; TNFRSF11B) is expressed in the inner ear and “may inhibit bone remodeling in the otic capsule,” providing a molecular explanation for its quiescent remodeling state (Jan 2005, The Laryngoscope; https://doi.org/10.1097/01.mlg.0000150702.28451.35) (tikka2023investigationofserum pages 6-6). In a 2023 gerbil SSCD model, fenestrations of the superior canal produced reversible diagnostic features—worsened low-frequency ABR thresholds (proxy for pseudoconductive hearing loss) and increased cVEMP amplitudes with low thresholds—and healed by osteoneogenesis that “resurfac[es] the SSCD without obliteration,” returning electrophysiology toward baseline (Jan 2023, Frontiers in Neurology; https://doi.org/10.3389/fneur.2022.1035478) (wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15). Clinical biochemical work has explored calcium/vitamin D and bone turnover markers in SSCD patients, aligning SSCD with otic capsule bone metabolism hypotheses (Jan 2023, Journal of Otology; https://doi.org/10.1016/j.joto.2022.12.005) (tikka2023investigationofserum pages 6-6).

Diagnostic correlations: Third-window mechanics predict low-frequency air–bone gaps with normal tympanometry, improved bone conduction thresholds, and characteristically low-threshold/high-amplitude VEMPs; surgical repair normalizes measures such as SP/AP ratios on ECoG and resolves the air–bone gap in many cases (merchant2008conductivehearingloss pages 4-5, iversen2020biomechanicsofthird pages 6-7). Contemporary clinical/biomechanical overviews and editorials emphasize that SSCD is the most common third-window disorder and summarize consistent VEMP and vestibulo-ocular reflex findings (Jun 2021, Frontiers in Neurology; https://doi.org/10.3389/fneur.2021.704095) (wackym2021editorialthirdwindow pages 3-4).

Recent developments and latest research (prioritized)
- Reversible animal model (2023): Surgical SSCD in gerbils demonstrated (a) low-frequency ABR threshold worsening, (b) increased cVEMP amplitudes/low thresholds, and (c) spontaneous reversal associated with osteoneogenesis and resurfacing of the dehiscence, with many measures returning toward baseline (Jan 2023; Frontiers in Neurology) (wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15).
- Biochemical context (2023): Case–control work investigated serum calcium and vitamin D in SSCD, referencing bone turnover markers (alkaline phosphatase, bone alkaline phosphatase, osteocalcin) and literature on osteoclastic activity in temporal bone, suggesting systemic mineral metabolism may interact with local otic capsule biology (Jan 2023; Journal of Otology) (tikka2023investigationofserum pages 6-6).
- Mechanistic synthesis: Biomechanical reviews consolidate the role of pressure-driven flows, near-incompressible lymphs, and resultant traveling waves/cupular deflection in third-window states, supporting the diagnostic signatures and explaining symptom triggers (Aug 2020; Frontiers in Neurology) (iversen2020biomechanicsofthird pages 6-7).

Current applications and real-world implementations
- Clinical diagnostics: High-resolution temporal bone CT to identify dehiscence; audiometry demonstrating low-frequency air–bone gaps with normal middle-ear tests; VEMPs with reduced thresholds and increased amplitudes; ECoG SP/AP ratio elevation with normalization post-plugging (merchant2008conductivehearingloss pages 4-5, iversen2020biomechanicsofthird pages 6-7, wackym2021editorialthirdwindow pages 3-4).
- Surgical repair: Middle cranial fossa or transmastoid canal plugging/resurfacing to eliminate the third window, with resolution of the air–bone gap and improvement of sound/pressure-induced vertigo in many patients, consistent with mechanical mechanism (merchant2008conductivehearingloss pages 4-5, iversen2020biomechanicsofthird pages 6-7).
- Emerging models: The 2023 gerbil model offers a platform for testing molecular and biomechanical interventions, showing osteoneogenesis-mediated resurfacing without canal obliteration (wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15).

Expert opinions and authoritative analyses
- “A third window will introduce a low mechanical impedance,” shunting energy and generating pressure gradients/waves that activate vestibular afferents; plugging abolishes phase-locked responses—biomechanical proof linking lesion to physiology (Aug 2020; Frontiers in Neurology) (iversen2020biomechanicsofthird pages 6-7).
- “To produce a conductive hearing loss the third window must be on the scala vestibuli side,” and “patching/plugging the dehiscence resolves the air–bone gap” (Apr 2008; Otology & Neurotology) (merchant2008conductivehearingloss pages 4-5).
- “No osteoclastic process was evident within the otic capsule” in a histopathologically verified clinical SCDS case, consistent with a thin-bone predisposition and trauma-trigger model (Jan 2012; Ann Otol Rhinol Laryngol) (teixido2012histopathologyofthe pages 1-2).
- SSCD is the most common third mobile window; editorials summarize diagnostic and QOL impacts and emphasize specific biomarkers such as cochlin-tomoprotein under evaluation (Jun 2021; Frontiers in Neurology) (wackym2021editorialthirdwindow pages 3-4).

Relevant statistics and data
- Audiometry: Third-window lesions (including SSCD) typically cause low- to mid-frequency air–bone gaps up to ~2 kHz with improved bone conduction and normal middle-ear measures; correction after plugging confirms causality (Apr 2008; Otology & Neurotology) (merchant2008conductivehearingloss pages 4-5).
- VEMPs: Abnormally low thresholds and high amplitudes are characteristic of SSCD and reverse after repair; animal model shows cVEMP amplitude increases with larger fenestrations and returns toward baseline with resurfacing (Jan 2023; Frontiers in Neurology) (wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15, iversen2020biomechanicsofthird pages 6-7).
- Histology: Clinical SCDS case with 1.4 × 0.6 mm defect; dura contacting membranous duct; no osteoclasts observed (Jan 2012; Ann Otol Rhinol Laryngol) (teixido2012histopathologyofthe pages 1-2).
- Biochemistry: Case–control exploration of serum calcium and vitamin D in SSCD; references to bone turnover markers and literature on temporal bone osteoclastic activity (Jan 2023; Journal of Otology) (tikka2023investigationofserum pages 6-6).

Evidence summary table
| Citation (authors, year) | Publication date | Journal | URL | Focus (mechanism / diagnostic) | Core finding (1–2 sentences) |
|---|---|---|---|---|---|
| Wackym PA et al., 2023 | Jan 2023 | Frontiers in Neurology | https://doi.org/10.3389/fneur.2022.1035478 | Animal model / mechanism & diagnostics | Gerbil SSCD model produced reversible pseudoconductive hearing loss (worse low-frequency ABR) and increased cVEMP amplitudes/low thresholds; micro-CT and histology show bone resurfacing (osteoneogenesis) with recovery of electrophysiologic measures (wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15). |
| Iversen MM & Rabbitt RD, 2020 | Aug 2020 | Frontiers in Neurology | https://doi.org/10.3389/fneur.2020.00891 | Biomechanics / mechanism | Detailed biomechanical account of third-window hydromechanics: dehiscence introduces a low-impedance pathway that shunts sound/pressure, generates transmembrane pressure gradients and traveling waves that activate canal and utricular afferents, explaining VEMP and vertigo phenomena (iversen2020biomechanicsofthird pages 6-7). |
| Merchant SN & Rosowski JJ, 2008 | Apr 2008 | Otology & Neurotology | https://doi.org/10.1097/mao.0b013e318161ab24 | Mechanism / clinical audiology | Seminal description of third-window effects: vestibular-side dehiscence lowers impedance, producing low-frequency air–bone gaps and enhanced bone conduction (pseudoconductive hearing loss), with resolution after surgical patching/plugging confirming mechanism (merchant2008conductivehearingloss pages 4-5). |
| Chien W et al., 2007 | Feb 2007 | Otology & Neurotology | https://doi.org/10.1097/01.mao.0000244370.47320.9a | Human ear mechanics / measurements | Experimental measurements show that superior canal dehiscence behaves as a third window altering middle/inner ear mechanics, redistributing pressure and explaining clinical audiometric patterns and vestibular responses associated with SSCD (supported by biomechanical reviews) (iversen2020biomechanicsofthird pages 6-7). |
| Teixidó M et al., 2012 | Jan 2012 | Annals of Otology, Rhinology & Laryngology | https://doi.org/10.1177/000348941212100102 | Histopathology / anatomy | Temporal bone histology of a clinical SSCD case showed a focal bony dehiscence with dura contacting the membranous duct; no clear osteoclastic resorption was seen, supporting thin/developmental bone predisposition and trauma-trigger hypotheses (teixido2012histopathologyofthe pages 1-2). |
| Tikka T et al., 2023 | Jan 2023 | Journal of Otology | https://doi.org/10.1016/j.joto.2022.12.005 | Bone biology / clinical biochemistry | Case–control study linking SSCD with investigations of serum calcium and vitamin D; places SSCD in context of otic capsule bone metabolism and suggests roles for calcium/Vit D pathways and osteoclastic activity hypotheses in dehiscence etiology (tikka2023investigationofserum pages 6-6). |


*Table: Concise summary of foundational and recent papers on superior semicircular canal dehiscence (SCDS)/third-window pathophysiology, showing publication details, URLs, focus, and 1–2 sentence core findings with supporting context citations.*

Structured Annotations
Key molecular players (HGNC) and related entities
- TNFRSF11B (OPG; HGNC:11909): Secreted decoy receptor inhibiting RANKL; “may inhibit bone remodeling in the otic capsule,” supporting the quiescent remodeling milieu and the biology of thin bone versus active resorption in SCDS (tikka2023investigationofserum pages 6-6).
- Bone turnover markers referenced clinically: alkaline phosphatase (ALPL; HGNC:436), bone alkaline phosphatase isoform; osteocalcin (BGLAP; HGNC:1048). Discussed as markers in SSCD biochemical evaluation (tikka2023investigationofserum pages 6-6).
- Cochlin-tomoprotein (COCH fragment): Investigated as a specific inner-ear biomarker in perilymphatic disorders within third-window discourse (editorial context) (wackym2021editorialthirdwindow pages 3-4).

Cell types (CL)
- Osteoclast (CL:0000098): Multinucleated bone-resorbing cells; implicated by broader temporal bone literature and bone marker context, though histology in one SCDS case did not show osteoclastic activity (teixido2012histopathologyofthe pages 1-2, tikka2023investigationofserum pages 6-6).
- Osteoblast (CL:0000062) and bone lining cells: The otic capsule is characterized by bone quiescence with specialized lining cells; resurfacing (osteoneogenesis) observed in animal SSCD healing (wackym2023newmodelof pages 14-15).
- Vestibular hair cells (e.g., CL:0000201) and afferent neurons: Activated by third-window pressure gradients/traveling waves, producing phase-locked and sustained responses (iversen2020biomechanicsofthird pages 6-7).

Anatomical locations (UBERON)
- Superior semicircular canal (UBERON:0010740); otic capsule (UBERON:0001755); oval window (UBERON:0001752); round window (UBERON:0001753); utricle (UBERON:0001756). Lesion resides on vestibular side; thin or absent bone over SSC produces third-window mechanics (merchant2008conductivehearingloss pages 4-5, teixido2012histopathologyofthe pages 1-2, iversen2020biomechanicsofthird pages 6-7).

Chemical entities (CHEBI)
- Calcium ion (CHEBI:29108); vitamin D (e.g., cholecalciferol, CHEBI:28940). Explored in SSCD case–control biochemistry (tikka2023investigationofserum pages 6-6).

Gene Ontology (GO) biological processes (disrupted or engaged)
- Bone remodeling (GO:0046850) and regulation of osteoclast differentiation (GO:0045670): OPG/RANKL axis in otic capsule (tikka2023investigationofserum pages 6-6).
- Mechanotransduction and sensory perception of sound (GO:0050957) and vestibular receptor cell stimulus detection (GO:0050911): Altered by third-window hydromechanics that impose abnormal pressure gradients/waves on hair cells (iversen2020biomechanicsofthird pages 6-7).
- Endolymph and perilymph fluid transport dynamics (related to fluid shear and cupula deflection; aligns with GO terms such as cilium movement GO:0003341 in vestibular hair cell kinocilia context) (iversen2020biomechanicsofthird pages 6-7).

Cellular components (GO CC)
- Otic capsule extracellular matrix (bone matrix) and perilymph/endolymph compartments; stereocilia bundle (GO:0032420) and cupula of ampulla (anatomical structure). Third-window mechanics produce transmembrane pressure differences across these compartments (iversen2020biomechanicsofthird pages 6-7, merchant2008conductivehearingloss pages 4-5).

Disease Progression (sequence of events)
1) Predisposition: Congenitally thin otic capsule bone over SSC and/or developmental anatomy predisposes to third-window formation; systemic mineral metabolism might modulate risk (teixido2012histopathologyofthe pages 1-2, tikka2023investigationofserum pages 6-6).
2) Trigger: Minor trauma, pressure events, or chronic pulsation at the middle cranial fossa can disrupt thin bone, creating a dehiscence with dura contacting the membranous duct (teixido2012histopathologyofthe pages 1-2).
3) Third-window hydromechanics: Dehiscence lowers vestibular-side impedance, shunting sound/pressure and generating pressure gradients and traveling waves in the vestibular labyrinth (merchant2008conductivehearingloss pages 4-5, iversen2020biomechanicsofthird pages 6-7).
4) Sensory consequences: Hair-bundle vibration and cupular deflection evoke phase-locked and sustained vestibular afferent activity, respectively; cochlear energy shunting yields low-frequency air–bone gaps with supranormal bone conduction (iversen2020biomechanicsofthird pages 6-7, merchant2008conductivehearingloss pages 4-5).
5) Clinical manifestation: Autophony, aural fullness, pulsatile tinnitus, sound/pressure-induced vertigo/oscillopsia, and conductive-pattern hearing loss. Diagnostics: low-threshold/high-amplitude VEMPs, CT-visible dehiscence, ECoG SP/AP changes (teixido2012histopathologyofthe pages 1-2, merchant2008conductivehearingloss pages 4-5, iversen2020biomechanicsofthird pages 6-7, wackym2021editorialthirdwindow pages 3-4).
6) Repair/healing: Surgical plugging/resurfacing often normalizes diagnostics and symptoms; in animal models, osteoneogenesis can resurface the defect and reverse electrophysiologic changes (merchant2008conductivehearingloss pages 4-5, wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15).

Phenotypic manifestations (HP) and links to mechanism
- Tullio phenomenon (HP:0011510) and Hennebert sign (HP:0033533): Sound/pressure-induced vertigo/oscillopsia due to third-window-driven vestibular activation (iversen2020biomechanicsofthird pages 6-7, merchant2008conductivehearingloss pages 4-5).
- Autophony (HP:0001601) and pulsatile tinnitus (HP:0000842): Aberrant hydromechanics and direct transmission pathways in third-window states (teixido2012histopathologyofthe pages 1-2, merchant2008conductivehearingloss pages 4-5).
- Conductive hearing impairment (air–bone gap) (HP:0000405; low-frequency): Shunting of acoustic energy at scala vestibuli side reduces cochlear partition drive; improves with plugging (merchant2008conductivehearingloss pages 4-5).
- Abnormal VEMP (HP:0033781; low thresholds, high amplitudes): Enhanced vestibular sensitivity due to third-window impedance shunting (iversen2020biomechanicsofthird pages 6-7, wackym2023newmodelof pages 1-2).

Key mechanistic evidence (with direct supporting quotes where available)
- “A third window will introduce a low mechanical impedance,” generating pressure gradients/waves that activate vestibular afferents; plugging abolishes phase-locked responses (Aug 2020; Frontiers in Neurology) (iversen2020biomechanicsofthird pages 6-7).
- “To produce a conductive hearing loss the third window must be on the scala vestibuli side” and plugging “resolves the air–bone gap” (Apr 2008; Otology & Neurotology) (merchant2008conductivehearingloss pages 4-5).
- “No osteoclastic process was evident within the otic capsule” in histology of a clinical SCDS case (Jan 2012; Ann Otol Rhinol Laryngol) (teixido2012histopathologyofthe pages 1-2).
- SSCD model “heals in situ by bony resurfacing of the SSCD without obliteration,” with ABR and cVEMP changes reversing toward baseline (Jan 2023; Frontiers in Neurology) (wackym2023newmodelof pages 14-15, wackym2023newmodelof pages 1-2).

Evidence items (primary literature; URLs and dates)
- Wackym PA et al. New model of superior semicircular canal dehiscence with reversible diagnostic findings characteristic of patients with the disorder. Frontiers in Neurology. Jan 2023. https://doi.org/10.3389/fneur.2022.1035478 (wackym2023newmodelof pages 1-2, wackym2023newmodelof pages 14-15).
- Iversen MM, Rabbitt RD. Biomechanics of Third Window Syndrome. Frontiers in Neurology. Aug 2020. https://doi.org/10.3389/fneur.2020.00891 (iversen2020biomechanicsofthird pages 6-7).
- Merchant SN, Rosowski JJ. Conductive Hearing Loss Caused by Third-Window Lesions of the Inner Ear. Otology & Neurotology. Apr 2008. https://doi.org/10.1097/mao.0b013e318161ab24 (merchant2008conductivehearingloss pages 4-5).
- Teixidó M et al. Histopathology of the Temporal Bone in a Case of Superior Canal Dehiscence Syndrome. Ann Otol Rhinol Laryngol. Jan 2012. https://doi.org/10.1177/000348941212100102 (teixido2012histopathologyofthe pages 1-2).
- Tikka T et al. Investigation of serum calcium and vitamin D levels in superior semicircular canal dehiscence syndrome: A case-control study. Journal of Otology. Jan 2023. https://doi.org/10.1016/j.joto.2022.12.005 (tikka2023investigationofserum pages 6-6).
- Wackym PA et al. Editorial: Third Window Syndrome. Frontiers in Neurology. Jun 2021. https://doi.org/10.3389/fneur.2021.704095 (wackym2021editorialthirdwindow pages 3-4).

Notes and limitations
- Direct genetic causality for SCDS remains unestablished; molecular insights largely relate to bone remodeling biology (e.g., OPG/RANKL pathways) and unique quiescence of otic capsule bone. Histopathology can show thin bone and dura contact without active osteoclastic resorption, though other temporal bone studies document osteoclastic activity in general (teixido2012histopathologyofthe pages 1-2, tikka2023investigationofserum pages 6-6).
- While most mechanistic claims are grounded in biomechanical and histologic evidence, targeted molecular pathways beyond OPG in the otic capsule require further study in human SCDS.


References

1. (merchant2008conductivehearingloss pages 4-5): Saumil N. Merchant and John J. Rosowski. Conductive hearing loss caused by third-window lesions of the inner ear. Otology & Neurotology, 29:282-289, Apr 2008. URL: https://doi.org/10.1097/mao.0b013e318161ab24, doi:10.1097/mao.0b013e318161ab24. This article has 431 citations and is from a peer-reviewed journal.

2. (iversen2020biomechanicsofthird pages 6-7): Marta M. Iversen and Richard D. Rabbitt. Biomechanics of third window syndrome. Frontiers in Neurology, Aug 2020. URL: https://doi.org/10.3389/fneur.2020.00891, doi:10.3389/fneur.2020.00891. This article has 58 citations and is from a peer-reviewed journal.

3. (teixido2012histopathologyofthe pages 1-2): Michael Teixido, Brian Kung, John J. Rosowski, and Saumil N. Merchant. Histopathology of the temporal bone in a case of superior canal dehiscence syndrome. Annals of Otology, Rhinology & Laryngology, 121:12-7, Jan 2012. URL: https://doi.org/10.1177/000348941212100102, doi:10.1177/000348941212100102. This article has 30 citations.

4. (tikka2023investigationofserum pages 6-6): Theofano Tikka, Mohd Afiq Mohd Slim, Trung Ton, Anna Sheldon, Louise J. Clark, and Georgios Kontorinis. Investigation of serum calcium and vitamin d levels in superior semicircular canal dehiscence syndrome: a case control study. Journal of Otology, 18:49-54, Jan 2023. URL: https://doi.org/10.1016/j.joto.2022.12.005, doi:10.1016/j.joto.2022.12.005. This article has 2 citations and is from a peer-reviewed journal.

5. (wackym2023newmodelof pages 1-2): P. Ashley Wackym, Carey D. Balaban, Olivia J. Van Osch, Brian T. Morris, Mark-Avery Tamakloe, Victoria L. Salvatore, Sudan Duwadi, Jennifer D. Gay, and Todd M. Mowery. New model of superior semicircular canal dehiscence with reversible diagnostic findings characteristic of patients with the disorder. Frontiers in Neurology, Jan 2023. URL: https://doi.org/10.3389/fneur.2022.1035478, doi:10.3389/fneur.2022.1035478. This article has 6 citations and is from a peer-reviewed journal.

6. (wackym2023newmodelof pages 14-15): P. Ashley Wackym, Carey D. Balaban, Olivia J. Van Osch, Brian T. Morris, Mark-Avery Tamakloe, Victoria L. Salvatore, Sudan Duwadi, Jennifer D. Gay, and Todd M. Mowery. New model of superior semicircular canal dehiscence with reversible diagnostic findings characteristic of patients with the disorder. Frontiers in Neurology, Jan 2023. URL: https://doi.org/10.3389/fneur.2022.1035478, doi:10.3389/fneur.2022.1035478. This article has 6 citations and is from a peer-reviewed journal.

7. (wackym2021editorialthirdwindow pages 3-4): P. Ashley Wackym, Yuri Agrawal, Tetsuo Ikezono, and Carey D. Balaban. Editorial: third window syndrome. Frontiers in Neurology, Jun 2021. URL: https://doi.org/10.3389/fneur.2021.704095, doi:10.3389/fneur.2021.704095. This article has 26 citations and is from a peer-reviewed journal.