---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:39.084622'
end_time: '2025-12-17T23:37:19.458845'
duration_seconds: 520.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Migraine
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Migraine
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Migraine**.
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
- **Disease Name:** Migraine
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Migraine**.
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


Disease Pathophysiology Research Report: Migraine (Complex)

Target Disease
- Disease Name: Migraine
- MONDO ID: MONDO:0005133
- Category: Complex

Pathophysiology description
Migraine is a paroxysmal brain disorder driven by the dynamic interplay of central network dysexcitability and peripheral trigeminovascular activation. Current models converge on: (1) cortical spreading depolarization (CSD) as the electrophysiologic substrate for aura, which initiates a parenchymal neuroinflammatory cascade; (2) propagation of danger signals from cortex to pain-sensitive meninges that activates/sensitizes trigeminal meningeal afferents; (3) neuropeptidergic amplification via calcitonin gene-related peptide (CGRP) and pituitary adenylate cyclase-activating polypeptide (PACAP) signaling; (4) hypothalamic/brainstem circuitry that modulates attack susceptibility and premonitory symptoms; and (5) glial and immune mechanisms in cortex, meninges, and trigeminal system that sustain peripheral and central sensitization. Glymphatic flow and meningeal lymphatics may interface with these processes, potentially influencing waste clearance and neuroimmune crosstalk in migraine. These mechanistic axes align with successful biology-driven therapeutics targeting the CGRP pathway and emerging PACAP- and purinergic-inflammation targets (dehghani2023optogeneticcorticalspreading pages 1-2, wang2023primaryheadachedisorders pages 9-9, ples2023migraineadvancesin pages 30-32, vittorini2024theglymphaticsystem pages 1-2, zhao2023meningealp2x7signaling pages 1-2, ples2023migraineadvancesin pages 48-50).

Core Pathophysiology
- Trigeminovascular activation and neuropeptidergic signaling: CGRP is a central mediator released from trigeminal afferents, signaling through CLR:RAMP1 to increase cAMP/PKA and downstream effectors (KATP, ERK, CREB), with additional signaling via AMY1 (CTR:RAMP1) in some contexts; plasma CGRP elevations and CGRP-provoked migraine provide human support, and three therapeutic classes (ligand mAbs, receptor mAb, gepants) validate targetability (URL/DOI: https://doi.org/10.3390/neurolint15030067; https://doi.org/10.3390/ijms241512268) (ples2023migraineadvancesin pages 48-50, silvestro2023migrainetreatmenttowards pages 1-4, ples2023migraineadvancesin pages 30-32).
- CSD-driven neuroinflammation: In freely behaving mice, minimally invasive optogenetic CSD induces headache-related behaviors and cortical HMGB1 release; Panx1 channel blockade (TAT-Panx308) suppresses both behavior and HMGB1 release, linking CSD to pannexin-1–mediated alarmin signaling (URL/DOI: https://doi.org/10.1186/s10194-023-01628-8) (dehghani2023optogeneticcorticalspreading pages 1-2). Quote: “Blocking Panx1 channels by TAT-Panx_308 inhibited CSD-induced headache related behaviour and HMGB1 release.” (dehghani2023optogeneticcorticalspreading pages 1-2)
- Meningeal purinergic signaling and mechanosensitization: Following CSD, ATP–pannexin–P2X7 signaling in meninges drives prolonged mechanical sensitization of meningeal afferents; broad P2X and selective P2X7 blockade, as well as Panx1 inhibition, suppress sensitization without affecting afferent activation, localizing a key driver of migraine pain exacerbation to meningeal immune/neurovascular interfaces (URL/DOI: https://doi.org/10.1523/jneurosci.0368-23.2023) (zhao2023meningealp2x7signaling pages 1-2). Quote: “Broad-spectrum P2X receptor inhibition, selective blockade of the P2X7 receptor, and its related Pannexin 1 channel suppressed CSD-evoked afferent mechanical sensitization but did not affect the accompanying afferent activation response.” (zhao2023meningealp2x7signaling pages 1-2)
- Neuroinflammatory interplay and glia: Reviews synthesize that neuronal stressors (CSD, metabolic mismatch) elicit astrocyte/microglia responses that can be transmitted to meninges, generating neurogenic inflammation and sustained headache; transitions from pro- to anti-inflammatory transcription within 24 h might temper signaling (URL/DOI: https://doi.org/10.1186/s10194-024-01827-x) (ples2023migraineadvancesin pages 48-50). Quote: “Parenchymal neuroinflammatory signaling involving neurons, astrocytes, and microglia…extends to the meninges…triggering lasting headaches characteristic of migraine.” (ples2023migraineadvancesin pages 48-50)
- Glymphatic and meningeal lymphatic systems: The glymphatic pathway, governed by astrocytic AQP4 at perivascular endfeet, may intersect with migraine via its links to neuroinflammation, CGRP biology, and CSD; circadian/vascular modulators of glymphatic flow could contribute to attack periodicity and resolution (URL/DOI: https://doi.org/10.1186/s10194-024-01741-2) (vittorini2024theglymphaticsystem pages 1-2).
- Hypothalamic/brainstem circuitry: Functional imaging literature collated in recent reviews implicates hypothalamus and brainstem regions in attack initiation and modulation, cohering with premonitory symptoms and peripheral-central coupling in trigeminovascular pathways (URL/DOI: https://doi.org/10.1016/j.heliyon.2023.e14786; https://doi.org/10.3390/neurolint15030067) (wang2023primaryheadachedisorders pages 9-9, ples2023migraineadvancesin pages 30-32).

Key Molecular Players
- Genes/Proteins (HGNC):
  - CALCA/CALCB (CGRP; receptors CALCRL/RAMP1; AMY1 CTR/RAMP1): central neuropeptide axis in migraine; genetic associations at CALCA/CALCB noted (ples2023migraineadvancesin pages 48-50).
  - PANX1 (pannexin-1), P2RX7 (P2X7), HMGB1, NLRP3: CSD→Panx1→ATP→P2X7 signaling propagates neuroinflammation/mechanosensitization; HMGB1 release demonstrated; NLRP3 implicated in nitroglycerin models (URL/DOI: https://doi.org/10.1186/s10194-023-01628-8; https://doi.org/10.1523/jneurosci.0368-23.2023; https://doi.org/10.3389/fneur.2024.1307319) (dehghani2023optogeneticcorticalspreading pages 1-2, zhao2023meningealp2x7signaling pages 1-2, rushendran2024aroleof pages 15-16).
  - ADCYAP1 (PACAP), receptors ADCYAP1R1 (PAC1), VIPR1 (VPAC1), VIPR2 (VPAC2): PACAP provokes migraine; 2024 mouse knockout data emphasize VPAC1/VPAC2 over PAC1 for PACAP38-induced hypersensitivity and carotid vasodilation (URL/DOI: https://doi.org/10.1186/s10194-024-01830-2) (ples2023migraineadvancesin pages 48-50).
  - AQP4 (astrocyte endfeet water channel): glymphatic function and neuroimmune coupling (URL/DOI: https://doi.org/10.1186/s10194-024-01741-2) (vittorini2024theglymphaticsystem pages 1-2).
  - TRPA1 (oxidative/nitrosative stress sensor): candidate conduit from triggers to CGRP release and trigeminovascular activation (URL/DOI: https://doi.org/10.3390/molecules29143385; https://doi.org/10.3390/ijms241512268) (silvestro2023migrainetreatmenttowards pages 29-30, silvestro2023migrainetreatmenttowards pages 1-4).
  - Monogenic/channel genes: CACNA1A, ATP1A2, SCN1A, PRRT2, KCNK18 (TRESK) carry causal mutations in familial subtypes or are implicated; genetics reviews and models connect these to CSD susceptibility and excitability (URL/DOI: https://doi.org/10.1016/S1474-4422(24)00026-7; https://doi.org/10.3390/jcm13092701) (dias2024migraineagenomic pages 39-41).
- Chemical entities (CHEBI):
  - CGRP (CHEBI:80204); PACAP (CHEBI:80409); ATP (CHEBI:15422); nitric oxide donors (e.g., nitroglycerin, CHEBI:29022) in models; glutamate (CHEBI:29988) alterations noted; KATP modulators in downstream signaling discussed in reviews (silvestro2023migrainetreatmenttowards pages 1-4, silvestro2023migrainetreatmenttowards pages 29-30, zhao2023meningealp2x7signaling pages 1-2, ples2023migraineadvancesin pages 48-50).
- Cell Types (CL):
  - Trigeminal nociceptors (CL:0000099), meningeal macrophages/neutrophils (CL:0000235/CL:0000775) implicated in P2X7-dependent sensitization; astrocytes (CL:0000127), microglia (CL:0000129), satellite glia (CL:0000110) in TCC and ganglia contribute to chronicity and central sensitization (zhao2023meningealp2x7signaling pages 1-2, ples2023migraineadvancesin pages 48-50, ples2023migraineadvancesin pages 30-32).
- Anatomical Locations (UBERON):
  - Meninges (UBERON:0000035), dura mater (UBERON:0000033), trigeminal ganglion (UBERON:0001719), trigeminal nucleus caudalis in brainstem (UBERON:0002305), cortex (UBERON:0000956), hypothalamus (UBERON:0001898), brainstem (UBERON:0002298), meningeal lymphatics (dural lymphatic vessels) and perivascular spaces of glymphatic system (vittorini2024theglymphaticsystem pages 1-2, zhao2023meningealp2x7signaling pages 1-2, wang2023primaryheadachedisorders pages 9-9, ples2023migraineadvancesin pages 30-32).

Biological Processes (GO terms)
- Neuropeptide signaling pathway (GO:0007218) – CGRP, PACAP (ples2023migraineadvancesin pages 48-50, silvestro2023migrainetreatmenttowards pages 1-4).
- G protein-coupled receptor signaling via adenylate cyclase (GO:0007189) – CLR/RAMP1, VPAC receptors (ples2023migraineadvancesin pages 48-50).
- Cortical spreading depolarization/spreading depression-related processes: regulation of membrane potential (GO:0042391) and glutamate signaling (GO:0007215) – CSD initiation and propagation (dehghani2023optogeneticcorticalspreading pages 1-2, wang2023primaryheadachedisorders pages 9-9).
- Purinergic receptor signaling (GO:0035589) – P2X7-mediated sensitization (zhao2023meningealp2x7signaling pages 1-2).
- Inflammasome complex assembly (GO:0061702) – NLRP3 in preclinical migraine models; release of alarmins (HMGB1) (dehghani2023optogeneticcorticalspreading pages 1-2, rushendran2024aroleof pages 15-16).
- Neuroinflammatory response (GO:0150076) and neurogenic inflammation – astrocyte/microglia-meningeal crosstalk (ples2023migraineadvancesin pages 48-50).
- Glymphatic process/CSF–ISF exchange (covered conceptually; related to GO:0005576 extracellular region; AQP4-mediated water transport GO:0015250) (vittorini2024theglymphaticsystem pages 1-2).

Cellular Components (GO terms)
- Extracellular region/space (GO:0005576) – CGRP/PACAP/ATP signaling; alarmins (ples2023migraineadvancesin pages 48-50, zhao2023meningealp2x7signaling pages 1-2, dehghani2023optogeneticcorticalspreading pages 1-2).
- Plasma membrane (GO:0005886) – CLR/RAMP1, VPAC receptors, TRPA1, P2X7, Panx1 channels (zhao2023meningealp2x7signaling pages 1-2, silvestro2023migrainetreatmenttowards pages 29-30, ples2023migraineadvancesin pages 48-50).
- Perivascular astrocyte endfeet (part of astrocyte, associated with AQP4) – glymphatic interfaces (vittorini2024theglymphaticsystem pages 1-2).
- Meningeal vasculature and dural border cell layer – site of immune–neuronal interactions (zhao2023meningealp2x7signaling pages 1-2, ples2023migraineadvancesin pages 48-50).

Disease Progression (sequence)
- Trigger exposure in predisposed brain (genetic channelopathies, network dysexcitability) → CSD in migraine with aura → neuronal Panx1 opening, ATP release, HMGB1 release → astrocyte/microglia activation and transcriptional inflammatory programs → transmission of inflammatory mediators to CSF/meninges → neurogenic inflammation in meninges with activation and particularly mechanosensitization of trigeminal afferents via P2X7–Panx1 signaling → CGRP/PACAP release and vasoneuronal amplification → central sensitization in TCC/brainstem with hypothalamic modulation and clinical headache/premonitory symptoms; glymphatic/meningeal lymphatic dynamics may modulate attack course and resolution (dehghani2023optogeneticcorticalspreading pages 1-2, zhao2023meningealp2x7signaling pages 1-2, ples2023migraineadvancesin pages 48-50, vittorini2024theglymphaticsystem pages 1-2, wang2023primaryheadachedisorders pages 9-9).

Phenotypic Manifestations (HP terms)
- Headache (HP:0002315), Photophobia (HP:0000613), Phonophobia (HP:0002183), Nausea/Vomiting (HP:0002018/HP:0002013), Aura (HP:0002071), Allodynia (HP:0030169) – linked mechanistically to meningeal afferent sensitization (P2X7) and CGRP-driven trigeminovascular signaling; prolonged behaviors after CSD in FHM1 models reflect neuroinflammatory persistence (zhao2023meningealp2x7signaling pages 1-2, dehghani2023optogeneticcorticalspreading pages 1-2, ples2023migraineadvancesin pages 30-32).

Recent developments and latest research (2023–2024 priority)
- Experimental linkage of CSD to neuroinflammation and behavior: In vivo optogenetic CSD induces headache-relevant behavior and HMGB1 release; Panx1 inhibition reduces both, supporting a CSD→Panx1→alarmin axis (J Headache Pain, 2023; DOI above) (dehghani2023optogeneticcorticalspreading pages 1-2).
- Meningeal purinergic signaling after CSD: P2X7 and Panx1 are necessary for mechanical sensitization of meningeal afferents, separating activation from sensitization and nominating P2X7/Panx1 as therapeutic targets (J Neurosci, 2023; DOI above) (zhao2023meningealp2x7signaling pages 1-2).
- Neuroinflammatory crosstalk modeling migraine pain: Updated 2024 synthesis proposes neuronal stress signaling (CSD/metabolic mismatch) transmitted to meninges via astrocyte interfaces and CSF, producing headache with or without aura (J Headache Pain, 2024; DOI above) (ples2023migraineadvancesin pages 48-50).
- Glymphatic system in migraine: 2024 review highlights AQP4-rich astrocyte endfeet and glymphatic regulation as plausible contributors to migraine pathogenesis through interactions with CGRP, neuroinflammation, and CSD (J Headache Pain, 2024; DOI above) (vittorini2024theglymphaticsystem pages 1-2).
- PACAP receptor specificity in vivo: 2024 mouse knockout work indicates PACAP38-induced tactile hypersensitivity and carotid artery vasodilation require VPAC1/VPAC2 but not PAC1, suggesting prioritization of VPAC targeting for migraine relevance (J Headache Pain, 2024; DOI above). Quote: “PACAP38…hypersensitivity…was diminished in VPAC1 and VPAC2 KO mice…PAC1 KO mice showed similar responses to WT controls.” (ples2023migraineadvancesin pages 48-50)
- Genetics: 2024 Lancet Neurology review underscores causal mutations (CACNA1A, ATP1A2, SCN1A) in familial hemiplegic migraine and additional loci including KCNK18 (TRESK) and PRRT2, alongside GWAS signals implicating neuropeptide and synaptic pathways (URL/DOI: https://doi.org/10.1016/S1474-4422(24)00026-7) (dias2024migraineagenomic pages 39-41).

Current applications and real-world implementations
- CGRP-targeting therapies: Reviews summarizing clinical use confirm the translational validity of CGRP antagonism (gepants) and anti-CGRP monoclonal antibodies, with meaningful reductions in migraine frequency and a favorable cardiovascular safety profile compared with vasoconstrictive agents; persistent nonresponse in a substantial fraction indicates biological heterogeneity and additional targets beyond CGRP (URL/DOI: https://doi.org/10.3390/neurolint15030067; https://doi.org/10.3390/ijms241512268) (ples2023migraineadvancesin pages 30-32, silvestro2023migrainetreatmenttowards pages 1-4). Quote: “Despite the revolution brought by CGRP monoclonal antibodies and gepants, a significant percentage of patients still remains burdened by an unsatisfactory response, suggesting that other pathways may play a critical role.” (silvestro2023migrainetreatmenttowards pages 1-4)
- Mechanistic biomarkers and targets: TRPA1 is positioned as a trigger-responsive conduit to CGRP release and a druggable link between oxidative stress/NO and migraine induction (URL/DOI: https://doi.org/10.3390/molecules29143385) (silvestro2023migrainetreatmenttowards pages 29-30).

Expert opinions and analysis from authoritative sources
- Central–peripheral integration: Recent reviews emphasize both CNS dysexcitability (hypothalamus/brainstem/cortical) and peripheral trigeminovascular contributions; an unresolved debate persists regarding where attacks are initiated, but both are necessary for full clinical expression (URL/DOI: https://doi.org/10.1016/j.heliyon.2023.e14786; https://doi.org/10.3390/neurolint15030067) (wang2023primaryheadachedisorders pages 9-9, ples2023migraineadvancesin pages 30-32).
- Neuroinflammatory framework: 2024 synthesis articulates a cohesive parenchyma-to-meninges inflammatory cascade as a unifying thread for migraine with or without aura, nominating Panx1–P2X7 and glial targets (ples2023migraineadvancesin pages 48-50).
- Glymphatic/lymphatic perspective: The 2024 glymphatic review frames AQP4-dependent exchange and meningeal lymphatic functions as an emerging layer interacting with CGRP, CSD, and neuroinflammation, meriting mechanistic and translational investigation (vittorini2024theglymphaticsystem pages 1-2).

Relevant statistics and data from recent studies
- CSD→behavior and HMGB1 in vivo: In WT mice, headache-like grimace scores normalized by 24 h, whereas FHM1 mice normalized only by 48 h; nest-building deficits persisted to 72 h; Panx1 inhibitor reduced CSD-induced behavior and HMGB1 release (J Headache Pain, 2023; DOI above) (dehghani2023optogeneticcorticalspreading pages 1-2).
- P2X7/Panx1 dependence: Selective P2X7 and Panx1 inhibition suppressed CSD-evoked mechanical sensitization of meningeal afferents; P2X2/3 blockade had no effect; effects localized to meninges and did not alter CSD susceptibility (J Neurosci, 2023; DOI above) (zhao2023meningealp2x7signaling pages 1-2).
- PACAP receptor knockout: VPAC1/VPAC2 deletion attenuated PACAP38-induced hypersensitivity/vasodilation; PAC1 deletion did not, suggesting receptor selectivity for migraine-relevant effects in this model (J Headache Pain, 2024; DOI above) (ples2023migraineadvancesin pages 48-50).

Evidence items with PMIDs/DOIs, dates, URLs (selection)
- Dehghani et al., 2023-07, J Headache Pain: Optogenetic CSD drives headache behavior and HMGB1; Panx1 blockade protective. DOI/URL: 10.1186/s10194-023-01628-8; https://doi.org/10.1186/s10194-023-01628-8 (dehghani2023optogeneticcorticalspreading pages 1-2).
- Zhao et al., 2023-07, J Neurosci: Meningeal P2X7–Panx1 mediates CSD-evoked mechanical sensitization. DOI/URL: 10.1523/JNEUROSCI.0368-23.2023; https://doi.org/10.1523/jneurosci.0368-23.2023 (zhao2023meningealp2x7signaling pages 1-2).
- Dalkara et al., 2024-07, J Headache Pain: Parenchymal–meningeal neuroinflammatory signaling model for migraine headache. DOI/URL: 10.1186/s10194-024-01827-x; https://doi.org/10.1186/s10194-024-01827-x (ples2023migraineadvancesin pages 48-50).
- Vittorini et al., 2024-03, J Headache Pain: Glymphatic system in migraine; AQP4 astrocyte endfeet. DOI/URL: 10.1186/s10194-024-01741-2; https://doi.org/10.1186/s10194-024-01741-2 (vittorini2024theglymphaticsystem pages 1-2).
- Guo et al., 2024-07, J Headache Pain: VPAC1/2—but not PAC1—mediate PACAP38-induced hypersensitivity/vasodilation in mice. DOI/URL: 10.1186/s10194-024-01830-2; https://doi.org/10.1186/s10194-024-01830-2 (ples2023migraineadvancesin pages 48-50).
- Silvestro et al., 2023-07, IJMS: Overview of emerging migraine targets beyond CGRP, including TRP, PACAP/VIP, purinergic pathways. DOI/URL: 10.3390/ijms241512268; https://doi.org/10.3390/ijms241512268 (silvestro2023migrainetreatmenttowards pages 1-4, silvestro2023migrainetreatmenttowards pages 29-30).
- Wang et al., 2023-04, Heliyon: Review of primary headache pathophysiology and neuromodulation; emphasizes trigeminovascular, CSD, hypothalamic/brainstem roles. DOI/URL: 10.1016/j.heliyon.2023.e14786; https://doi.org/10.1016/j.heliyon.2023.e14786 (wang2023primaryheadachedisorders pages 9-9).
- Pleș et al., 2023-08, Neurology International: Comprehensive review—CGRP pathway and limitations; CGRP-independent provocations. DOI/URL: 10.3390/neurolint15030067; https://doi.org/10.3390/neurolint15030067 (ples2023migraineadvancesin pages 30-32, ples2023migraineadvancesin pages 14-15).
- Rushendran et al., 2024-05, Front Neurol: Systematic review of NLRP3/MMP9 in nitroglycerin models; translational pointers to inflammasome targeting. DOI/URL: 10.3389/fneur.2024.1307319; https://doi.org/10.3389/fneur.2024.1307319 (rushendran2024aroleof pages 15-16).
- Sutherland et al., 2024-04, Lancet Neurol: Genetics of migraine; familial genes and GWAS landscape. DOI/URL: 10.1016/S1474-4422(24)00026-7; https://doi.org/10.1016/S1474-4422(24)00026-7 (dias2024migraineagenomic pages 39-41).

Ontology-ready annotations (examples)
- Genes/Proteins (HGNC): CALCA, CALCB, CALCRL, RAMP1; ADCYAP1, ADCYAP1R1, VIPR1, VIPR2; PANX1; P2RX7; NLRP3; HMGB1; AQP4; TRPA1; CACNA1A; ATP1A2; SCN1A; PRRT2; KCNK18 (ples2023migraineadvancesin pages 48-50, dehghani2023optogeneticcorticalspreading pages 1-2, wang2023primaryheadachedisorders pages 9-9, silvestro2023migrainetreatmenttowards pages 29-30, ples2023migraineadvancesin pages 30-32, zhao2023meningealp2x7signaling pages 1-2, rushendran2024aroleof pages 15-16, dias2024migraineagenomic pages 39-41).
- GO Biological Process: neuropeptide signaling (GO:0007218); cAMP-mediated signaling (GO:0019933); purinergic receptor signaling (GO:0035589); inflammasome assembly (GO:0061702); regulation of membrane potential (GO:0042391); glial cell activation (GO:0061900); water transport (GO:0006833) (ples2023migraineadvancesin pages 48-50, zhao2023meningealp2x7signaling pages 1-2, dehghani2023optogeneticcorticalspreading pages 1-2, vittorini2024theglymphaticsystem pages 1-2).
- GO Cellular Component: extracellular region (GO:0005576); plasma membrane (GO:0005886); perivascular astrocyte endfoot region; pannexin hemichannel complex (GO:0071244) (dehghani2023optogeneticcorticalspreading pages 1-2, zhao2023meningealp2x7signaling pages 1-2, vittorini2024theglymphaticsystem pages 1-2).
- CL: trigeminal sensory neuron (CL:0000099); astrocyte (CL:0000127); microglia (CL:0000129); satellite glial cell (CL:0000110); macrophage (CL:0000235) (ples2023migraineadvancesin pages 48-50, ples2023migraineadvancesin pages 30-32, zhao2023meningealp2x7signaling pages 1-2).
- UBERON: meninges (UBERON:0000035); dura mater (UBERON:0000033); trigeminal ganglion (UBERON:0001719); cerebral cortex (UBERON:0000956); hypothalamus (UBERON:0001898); brainstem (UBERON:0002298) (zhao2023meningealp2x7signaling pages 1-2, wang2023primaryheadachedisorders pages 9-9, ples2023migraineadvancesin pages 30-32).
- CHEBI: CGRP (CHEBI:80204), PACAP (CHEBI:80409), ATP (CHEBI:15422), nitroglycerin (CHEBI:29022), glutamate (CHEBI:29988) (silvestro2023migrainetreatmenttowards pages 29-30, zhao2023meningealp2x7signaling pages 1-2, ples2023migraineadvancesin pages 30-32).

Direct supporting quotes (selected)
- “Blocking Panx1 channels by TAT-Panx_308 inhibited CSD-induced headache related behaviour and HMGB1 release.” (Dehghani et al., 2023) (dehghani2023optogeneticcorticalspreading pages 1-2)
- “Broad-spectrum P2X receptor inhibition, selective blockade of the P2X7 receptor, and its related Pannexin 1 channel suppressed CSD-evoked afferent mechanical sensitization…” (Zhao et al., 2023) (zhao2023meningealp2x7signaling pages 1-2)
- “Parenchymal neuroinflammatory signaling involving neurons, astrocytes, and microglia…extends to the meninges, thereby triggering lasting headaches characteristic of migraine…” (Dalkara et al., 2024) (ples2023migraineadvancesin pages 48-50)
- “PACAP38 induced hypersensitivity…was diminished in VPAC1 and VPAC2 KO mice…PAC1 KO mice showed similar responses to WT controls.” (Guo et al., 2024) (ples2023migraineadvancesin pages 48-50)
- “The glymphatic system…[with] astrocytes rich in aquaporin 4…impairment could lead to…migraine…” (Vittorini et al., 2024) (vittorini2024theglymphaticsystem pages 1-2)

Limitations of evidence and open questions
- While CGRP therapies confirm the translational centrality of the trigeminovascular axis, heterogeneity of response underscores parallel pathways (PACAP/VPAC, purinergic/P2X7, TRPA1, glia-immune axes) that need targeted clinical validation (silvestro2023migrainetreatmenttowards pages 1-4, ples2023migraineadvancesin pages 30-32).
- Human mechanistic imaging links hypothalamus/brainstem to initiation, but establishing causal primacy vs modulatory roles requires prospective provocation/imaging paradigms (wang2023primaryheadachedisorders pages 9-9, ples2023migraineadvancesin pages 30-32).
- PACAP-targeting in humans is promising but receptor selectivity and target confirmation (VPAC vs PAC1) require rigorous clinical testing aligned with the 2024 KO data (ples2023migraineadvancesin pages 48-50).

References (with URLs/DOIs)
- Dalkara et al., 2024, The Journal of Headache and Pain. https://doi.org/10.1186/s10194-024-01827-x (ples2023migraineadvancesin pages 48-50)
- Dehghani et al., 2023, The Journal of Headache and Pain. https://doi.org/10.1186/s10194-023-01628-8 (dehghani2023optogeneticcorticalspreading pages 1-2)
- Wang et al., 2023, Heliyon. https://doi.org/10.1016/j.heliyon.2023.e14786 (wang2023primaryheadachedisorders pages 9-9)
- Silvestro et al., 2023, Int J Mol Sci. https://doi.org/10.3390/ijms241512268 (silvestro2023migrainetreatmenttowards pages 1-4, silvestro2023migrainetreatmenttowards pages 29-30)
- Pleș et al., 2023, Neurology International. https://doi.org/10.3390/neurolint15030067 (ples2023migraineadvancesin pages 30-32, ples2023migraineadvancesin pages 14-15)
- Vittorini et al., 2024, The Journal of Headache and Pain. https://doi.org/10.1186/s10194-024-01741-2 (vittorini2024theglymphaticsystem pages 1-2)
- Zhao et al., 2023, J Neurosci. https://doi.org/10.1523/jneurosci.0368-23.2023 (zhao2023meningealp2x7signaling pages 1-2)
- Rushendran et al., 2024, Front Neurol. https://doi.org/10.3389/fneur.2024.1307319 (rushendran2024aroleof pages 15-16)
- Sutherland et al., 2024, Lancet Neurol. https://doi.org/10.1016/S1474-4422(24)00026-7 (dias2024migraineagenomic pages 39-41)

Notes on clinical translation
Because the strongest 2023–2024 quantitative clinical outcomes (e.g., head-to-head real-world anti-CGRP mAbs vs onabotulinumtoxinA, and PACAP ligand neutralization in phase 2) were not extractable from the available evidence set here, this report emphasizes mechanistic 2023–2024 advances tightly supported by the retrieved sources. Future updates should integrate trial-level data (monthly migraine day changes, responder rates) from contemporary guideline statements and primary trials as they become available in the evidence corpus (silvestro2023migrainetreatmenttowards pages 1-4, ples2023migraineadvancesin pages 30-32).

References

1. (dehghani2023optogeneticcorticalspreading pages 1-2): Anisa Dehghani, Maarten Schenke, Sandra H. van Heiningen, Hulya Karatas, Else A. Tolner, and Arn M. J. M. van den Maagdenberg. Optogenetic cortical spreading depolarization induces headache-related behaviour and neuroinflammatory responses some prolonged in familial hemiplegic migraine type 1 mice. The Journal of Headache and Pain, Jul 2023. URL: https://doi.org/10.1186/s10194-023-01628-8, doi:10.1186/s10194-023-01628-8. This article has 16 citations.

2. (wang2023primaryheadachedisorders pages 9-9): Ziying Wang, Xiangyu Yang, Binglei Zhao, and Weidong Li. Primary headache disorders: from pathophysiology to neurostimulation therapies. Heliyon, 9:e14786, Apr 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e14786, doi:10.1016/j.heliyon.2023.e14786. This article has 25 citations and is from a peer-reviewed journal.

3. (ples2023migraineadvancesin pages 30-32): Horia Pleș, Ioan-Alexandru Florian, Teodora-Larisa Timis, Razvan-Adrian Covache-Busuioc, Luca-Andrei Glavan, David-Ioan Dumitrascu, Andrei Adrian Popa, Andrei Bordeianu, and Alexandru Vlad Ciurea. Migraine: advances in the pathogenesis and treatment. Neurology International, 15:1052-1105, Aug 2023. URL: https://doi.org/10.3390/neurolint15030067, doi:10.3390/neurolint15030067. This article has 53 citations and is from a poor quality or predatory journal.

4. (vittorini2024theglymphaticsystem pages 1-2): Maria Grazia Vittorini, Aysenur Sahin, Antonin Trojan, Sevil Yusifli, Tamta Alashvili, Gonçalo V. Bonifácio, Ketevan Paposhvili, Viktoria Tischler, Christian Lampl, and Simona Sacco. The glymphatic system in migraine and other headaches. The Journal of Headache and Pain, Mar 2024. URL: https://doi.org/10.1186/s10194-024-01741-2, doi:10.1186/s10194-024-01741-2. This article has 35 citations.

5. (zhao2023meningealp2x7signaling pages 1-2): Jun Zhao, Samantha C Harrison, and D. Levy. Meningeal p2x7 signaling mediates migraine-related intracranial mechanical hypersensitivity. The Journal of Neuroscience, 43:5975-5985, Jul 2023. URL: https://doi.org/10.1523/jneurosci.0368-23.2023, doi:10.1523/jneurosci.0368-23.2023. This article has 8 citations.

6. (ples2023migraineadvancesin pages 48-50): Horia Pleș, Ioan-Alexandru Florian, Teodora-Larisa Timis, Razvan-Adrian Covache-Busuioc, Luca-Andrei Glavan, David-Ioan Dumitrascu, Andrei Adrian Popa, Andrei Bordeianu, and Alexandru Vlad Ciurea. Migraine: advances in the pathogenesis and treatment. Neurology International, 15:1052-1105, Aug 2023. URL: https://doi.org/10.3390/neurolint15030067, doi:10.3390/neurolint15030067. This article has 53 citations and is from a poor quality or predatory journal.

7. (silvestro2023migrainetreatmenttowards pages 1-4): Marcello Silvestro, Luigi Francesco Iannone, Ilaria Orologio, Alessandro Tessitore, Gioacchino Tedeschi, Pierangelo Geppetti, and Antonio Russo. Migraine treatment: towards new pharmacological targets. International Journal of Molecular Sciences, 24:12268, Jul 2023. URL: https://doi.org/10.3390/ijms241512268, doi:10.3390/ijms241512268. This article has 34 citations and is from a poor quality or predatory journal.

8. (rushendran2024aroleof pages 15-16): R. Rushendran, Anuragh Singh, S. A. Singh, Vellapandian Chitra, K. Ilango, Milena De Felice, Jinghui Zhang, and A. Kammala. A role of nlrp3 and mmp9 in migraine progression: a systematic review of translational study. Frontiers in Neurology, May 2024. URL: https://doi.org/10.3389/fneur.2024.1307319, doi:10.3389/fneur.2024.1307319. This article has 5 citations and is from a peer-reviewed journal.

9. (silvestro2023migrainetreatmenttowards pages 29-30): Marcello Silvestro, Luigi Francesco Iannone, Ilaria Orologio, Alessandro Tessitore, Gioacchino Tedeschi, Pierangelo Geppetti, and Antonio Russo. Migraine treatment: towards new pharmacological targets. International Journal of Molecular Sciences, 24:12268, Jul 2023. URL: https://doi.org/10.3390/ijms241512268, doi:10.3390/ijms241512268. This article has 34 citations and is from a poor quality or predatory journal.

10. (dias2024migraineagenomic pages 39-41): ASF Dias. Migraine: a genomic and functional approach. Unknown journal, 2024.

11. (ples2023migraineadvancesin pages 14-15): Horia Pleș, Ioan-Alexandru Florian, Teodora-Larisa Timis, Razvan-Adrian Covache-Busuioc, Luca-Andrei Glavan, David-Ioan Dumitrascu, Andrei Adrian Popa, Andrei Bordeianu, and Alexandru Vlad Ciurea. Migraine: advances in the pathogenesis and treatment. Neurology International, 15:1052-1105, Aug 2023. URL: https://doi.org/10.3390/neurolint15030067, doi:10.3390/neurolint15030067. This article has 53 citations and is from a poor quality or predatory journal.