---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-15T19:42:40.459306'
end_time: '2026-02-15T19:51:48.170017'
duration_seconds: 547.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Houge-Janssens Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Houge-Janssens Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Houge-Janssens Syndrome**.
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
- **Disease Name:** Houge-Janssens Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Houge-Janssens Syndrome**.
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


Plan (current status):
- Objective 1 (complete): Clarified disease definition, nomenclature, and genetic etiology, centered on UBTF E210K and related UBTF variants (p.Q203R). (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
- Objective 2 (complete): Gathered 2023–2024 primary/review literature and landmark 2018 study. (braden2024anoverviewof pages 1-2, pietra2023expandingtheclinical pages 3-5, theophanous2023transcriptionfactorubf pages 6-8, hussein2023earlymaturationand pages 2-4, ledoux2024polymeraseias pages 9-11, moss2023hmgboxesribosomopathiesand pages 2-3, toro2018arecurrentde pages 1-1)
- Objective 3–8 (complete in report below): Integrated pathophysiology, ontology annotations, disease progression, phenotypes, statistics, and therapeutic hypotheses with recent citations.

| Year | First author | Title | Journal (month) | Focus | Key mechanistic points | URL / DOI (context) | Notes on quality |
|---|---|---|---|---|---|---|---|
| 2018 | Toro | A recurrent de novo missense mutation in UBTF causes developmental neuroregression | Human Molecular Genetics (Feb 2018) | clinical / mechanism | Recurrent de novo UBTF c.628G>A (p.Glu210Lys, E210K); ↑ pre-rRNA/18S, nucleolar abnormalities, DNA breaks, cell-cycle defects and apoptosis in patient fibroblasts | https://doi.org/10.1093/hmg/ddy049 (toro2018arecurrentde pages 1-1) | Landmark case series with cellular assays and early mechanistic data |
| 2024 | Braden | An Overview of UBTF Neuroregression Syndrome | Brain Sciences (Feb 2024) | review / clinical-mechanism | Synthesizes E210K clinical phenotype and MRI features; emphasizes rRNA dysregulation, nucleolar stress and DNA damage response as therapeutic hypotheses | https://doi.org/10.3390/brainsci14020179 (braden2024anoverviewof pages 1-2) | Recent open-access review summarizing 2017–2024 literature |
| 2023 | Pietra | Expanding the Clinical Spectrum of UBTF-Related Neurodevelopmental Disorder | Neurology: Genetics (Dec 2023) | clinical / pathology | Case series (2 patients) showing mitochondrial abnormalities on muscle biopsy; confirms E210K pathogenicity and expands phenotype severity | https://doi.org/10.1212/NXG.0000000000200098 (pietra2023expandingtheclinical pages 3-5) | Case reports with histology and metabolic data; adds clinical heterogeneity |
| 2023 | Moss | HMG-boxes, ribosomopathies and neurodegenerative disease | Frontiers in Genetics (Aug 2023) | mechanism / review | Frames UBTF E210K as a ribosomopathy affecting rDNA chromatin/topology; discusses context-dependent gain- and loss-of-function effects on rRNA synthesis | https://doi.org/10.3389/fgene.2023.1225832 (moss2023hmgboxesribosomopathiesand pages 2-3) | Mechanistic review linking UBTF variants to ribosome biology and neurodegeneration |
| 2023 | Theophanous | Transcription factor UBF depletion in mouse cells results in downregulation of both downstream and upstream elements of the rRNA transcription network | Journal of Biological Chemistry (Oct 2023) | mechanism / cell biology | UBF depletion reduces UBTF1/pUBF and RRN3, perturbs Pol I PIC and rRNA transcription network; ChIP and WB evidence in mouse cells | https://doi.org/10.1016/j.jbc.2023.105203 (theophanous2023transcriptionfactorubf pages 6-8) | Experimental mechanistic study (mouse cells) informing functional consequences of UBTF perturbation |
| 2023 | Hussein | Early maturation and hyperexcitability is a shared phenotype of cortical neurons derived from different ASD-associated mutations (includes UBTF E210K) | Translational Psychiatry / preprint (May 2023) | cellular model / electrophysiology | iPSC-derived cortical neurons with UBTF E210K show early hyperexcitability: ↑ Na+ currents and ↑ EPSC amplitude; suggests neuronal hyperexcitability contributes to seizures/phenotype | https://doi.org/10.1101/2022.11.02.514882 (hussein2023earlymaturationand pages 2-4) | iPSC electrophysiology evidence supporting neuronal excitability phenotype (preprint with peer-reviewed lineage) |
| 2024 | LeDoux | Polymerase I as a Target for Treating Neurodegenerative Disorders | Biomedicines (May 2024) | therapy / perspective | Reviews rationale for Pol I inhibition as a therapeutic strategy for disorders with rRNA dysregulation (including UBTF E210K); outlines safety and delivery concerns (BBB, neuronal tolerance, off-target effects) | https://doi.org/10.3390/biomedicines12051092 (ledoux2024polymeraseias pages 9-11) | Therapeutic perspective highlighting feasibility and unanswered questions |


*Table: A curated markdown table of principal clinical, mechanistic, and therapeutic publications on UBTF-related neuroregression (Houge-Janssens/CONDBA) from 2018–2024, with DOIs/URLs and context IDs for traceable evidence.*

Comprehensive Research Report: Houge-Janssens Syndrome (UBTF Neuroregression Syndrome, CONDBA)

Target disease and identifiers
- Disease name: Houge-Janssens Syndrome (also: UBTF Neuroregression Syndrome; Childhood-Onset Neurodegeneration with Brain Atrophy, CONDBA) (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
- MONDO ID: Not definitively assigned as a distinct MONDO entry under “Houge-Janssens Syndrome” at time of writing; disease is commonly indexed under UBTF-related neuroregression/neurodevelopmental disorder in the literature. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
- Category: Mendelian (autosomal dominant, typically de novo) (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)

1) Core pathophysiology
- Primary pathophysiological mechanism: Disruption of RNA polymerase I (Pol I)-dependent ribosomal RNA (rRNA) transcription due to pathogenic variants in UBTF, a nucleolar HMG-box transcription factor that shapes rDNA chromatin and cooperates with SL1 to form the Pol I pre-initiation complex (PIC). This leads to altered rDNA chromatin/topology, rRNA dysregulation (often increased pre‑rRNA/18S), nucleolar stress, accumulation of DNA double-strand breaks, defective cell-cycle progression, and apoptosis in patient cells. “This variant causes unstable preinitiation complexes to form, resulting in altered rDNA chromatin structures, rRNA dysregulation, DNA damage, and ultimately, neurodegeneration.” (Braden 2024). Patient fibroblasts: ↑ pre‑rRNA (>3x), ↑ 18S rRNA (~2x), fewer nucleoli, ↑ 53BP1 foci, apoptosis; iPSC neurons show hyperexcitability. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3, ledoux2024polymeraseias pages 9-11, hussein2023earlymaturationand pages 2-4)
- Molecular nuance and context dependence: Evidence supports a gain-of-function aspect for E210K in human fibroblasts (increased UBTF occupancy at rDNA and elevated rRNA), while a homozygous E210K mouse knock‑in shows reduced UBTF1/SL1 promoter association and lowered pre‑rRNA synthesis, suggesting cell-type/species/context dependence of gain-/loss-of-function effects and a central role for disturbed rDNA transcription and topology. (moss2023hmgboxesribosomopathiesand pages 2-3)
- Network-level consequences: Depletion/perturbation of UBF (UBTF) in mouse cells downregulates both downstream and upstream elements of the rRNA transcription network (including RRN3), confirming that UBF levels critically set Pol I initiation capacity. (theophanous2023transcriptionfactorubf pages 6-8)
- Putative links to neuronal vulnerability: As post-mitotic, highly transcriptionally active, long-lived cells, neurons may be particularly susceptible to nucleolar stress and genome instability arising from dysregulated rRNA synthesis and rDNA chromatin remodeling; hyperexcitability phenotypes in patient-derived cortical neurons provide an additional cellular stressor that may contribute to seizures and disease progression. (braden2024anoverviewof pages 1-2, hussein2023earlymaturationand pages 2-4)
- Emerging mitochondrial dimension: Case-series muscle biopsies show subsarcolemmal mitochondrial proliferation with slightly reduced complex I activity; UBTF perturbation may trigger compensatory PPARGC1A upregulation and mitochondrial biogenesis; decreased CSF biopterin was also reported in one patient, suggesting metabolic involvement worthy of further study. (pietra2023expandingtheclinical pages 3-5)

2) Key molecular players
- Genes/proteins (HGNC):
  - UBTF (HGNC:12592): encodes Upstream Binding Transcription Factor (UBF), a nucleolar, multi–HMG-box protein that bends promoter DNA and cooperates with SL1 to recruit Pol I to rDNA. Two isoforms: UBTF1 (Pol I/rRNA) and UBTF2 (impacts Pol II at select genes). (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
  - SL1 complex (TBP and TAFIs) and RRN3: Pol I basal machinery interacting with UBTF to form the PIC; RRN3 is reduced when UBF is depleted in mouse cells, implicating concerted control of the rRNA transcription network. (theophanous2023transcriptionfactorubf pages 6-8, moss2023hmgboxesribosomopathiesand pages 2-3)
- Variant spectrum:
  - Recurrent de novo E210K (c.628G>A; p.Glu210Lys) in HMG-box 2 is the defining pathogenic variant for the classic neuroregression syndrome; reported across independent cohorts since 2017–2018. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
  - Additional rare missense variants include Q203R (associated with earlier regression and pontine/thalamic involvement). Many UBTF variants exist in databases but with uncertain pathogenicity. (moss2023hmgboxesribosomopathiesand pages 2-3, braden2024anoverviewof pages 8-10)
- Chemical entities (CHEBI) and metabolites:
  - Biopterin (CHEBI:17097): decreased CSF biopterin reported in an affected individual; potential metabolic biomarker under investigation. (pietra2023expandingtheclinical pages 3-5)
  - Sodium ion (CHEBI:29101): increased Na+ currents reported in patient-derived cortical neurons (hyperexcitability phenotype). (hussein2023earlymaturationand pages 2-4)
- Cell types (CL):
  - Cortical neurons (CL:0002604): patient-derived iPSC cortical neurons show early hyperexcitability with increased sodium currents and EPSC amplitudes. (hussein2023earlymaturationand pages 2-4)
  - Additional neural/glial involvement is inferred from imaging and clinical progression; definitive cell-type–resolved human neuropathology remains limited. (braden2024anoverviewof pages 1-2)
- Anatomical locations (UBERON):
  - Cerebral cortex (UBERON:0000956): progressive cortical atrophy predominates (supratentorial > infratentorial). (braden2024anoverviewof pages 5-6, moss2023hmgboxesribosomopathiesand pages 2-3)
  - White matter (UBERON:0002436): diffuse/symmetric T2 hyperintensities; secondary demyelination is suggested rather than primary leukodystrophy. (braden2024anoverviewof pages 5-6, moss2023hmgboxesribosomopathiesand pages 2-3)
  - Corpus callosum (UBERON:0002353): thinning common. Ventriculomegaly by ex vacuo dilation frequent. (braden2024anoverviewof pages 5-6)
  - Cerebellum (UBERON:0002037): variable cerebellar atrophy. (braden2024anoverviewof pages 5-6)
  - Thalamus (UBERON:0001897): bilateral hyperintensities reported in some patients; thalamic involvement may be informative mechanistically. (braden2024anoverviewof pages 5-6)

3) Biological processes for GO annotation (disrupted)
- rRNA transcription by RNA polymerase I (GO:0006360); ribosome biogenesis (GO:0042254); pre-initiation complex assembly at rDNA (GO:0070897); chromatin organization/topology at rDNA (GO:0006325); nucleolar organization (GO:0005730 as CC; process term: GO:0007000 cellular component organization); DNA damage response to double-strand breaks (GO:0006974); apoptotic signaling (e.g., p53-mediated) consequent to nucleolar stress (GO:0072331). Evidence: mechanistic reviews and patient-cell/mouse-cell studies. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3, theophanous2023transcriptionfactorubf pages 6-8, ledoux2024polymeraseias pages 9-11)

4) Cellular components (GO CC)
- Nucleolus (GO:0005730) and rDNA chromatin within nucleolar organizer regions; RNA polymerase I complex (GO:0005671); UBTF located in nucleolus binding rDNA promoters and external transcribed spacers; fewer/larger nucleoli observed in patient cells. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3, ledoux2024polymeraseias pages 9-11)

5) Disease progression (sequence of events)
- Initial trigger: de novo heterozygous UBTF missense (classically E210K in HMG-box 2) alters UBTF–DNA interactions and Pol I PIC stability/topology at rDNA. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
- Early cellular effects: rRNA dysregulation (↑ pre‑rRNA/18S in fibroblasts), altered nucleolar morphology (fewer/larger nucleoli), increased DNA double-strand breaks and impaired cell-cycle progression, apoptosis; in neurons, early hyperexcitability phenotypes. (moss2023hmgboxesribosomopathiesand pages 2-3, ledoux2024polymeraseias pages 9-11, hussein2023earlymaturationand pages 2-4)
- Tissue-level evolution: progressive cerebral atrophy (supratentorial > infratentorial), diffuse white-matter T2 hyperintensities, corpus callosum thinning, ventriculomegaly; variable cerebellar and possible thalamic involvement. (braden2024anoverviewof pages 5-6, moss2023hmgboxesribosomopathiesand pages 2-3)
- Clinical course: onset typically 2–4 years with developmental regression (language, motor, cognition), hypotonia, gait ataxia, behavioral changes; progression to extrapyramidal signs (dystonia, parkinsonism), aphasia, feeding difficulties, ambulatory loss by early teens; seizures in a minority (~35%) with ~12% EEG abnormalities without seizures and ~53% with neither. Microcephaly in ~75% of reported cases. (braden2024anoverviewof pages 1-2, braden2024anoverviewof pages 5-6)

6) Phenotypic manifestations and HPO mapping
- Developmental regression (HP:0002376), intellectual disability (HP:0001249), speech/language regression/aphasia (HP:0002371), dysarthria (HP:0001260), hypotonia (HP:0001252), ataxia (HP:0001251), dystonia (HP:0001332), parkinsonism (HP:0001300), abnormal gait (HP:0001288), seizures (HP:0001250; ~35% prevalence), behavioral abnormalities resembling ASD (HP:0000729), feeding difficulties/dysphagia (HP:0002015), postnatal microcephaly (HP:0000252). (braden2024anoverviewof pages 1-2, braden2024anoverviewof pages 5-6)
- Neuroimaging/HPO: Cerebral atrophy (HP:0002059), thinning of corpus callosum (HP:0002079), ventriculomegaly (HP:0002119), white matter hyperintensities (HP:0030171), possible thalamic signal anomaly (not universally coded). (braden2024anoverviewof pages 5-6)
- Additional observations: Mitochondrial proliferation in muscle; slightly reduced complex I activity; decreased CSF biopterin in one case; pseudobulbar syndrome and brainstem atrophy reported in a severe presentation. (pietra2023expandingtheclinical pages 3-5)

7) Current applications and real-world implementation
- Diagnostics: High suspicion in children with regression at 2–4 years plus progressive brain atrophy and diffuse white-matter T2 signal, thinning callosum, ventriculomegaly; MRI is uniformly abnormal; EEG variably abnormal. Genetic confirmation via WES/WGS including UBTF; recurrent E210K strongly supports diagnosis. (braden2024anoverviewof pages 5-6, braden2024anoverviewof pages 1-2)
- Cellular modeling: Patient iPSC-derived cortical neurons enable functional readouts (e.g., Na+ currents, EPSC amplitude, hyperexcitability), providing mechanistic biomarkers for preclinical testing. (hussein2023earlymaturationand pages 2-4)

8) Expert opinions and therapeutic hypotheses (2023–2024)
- Pol I/rRNA synthesis as a therapeutic axis: Given that “UBTF-associated neuroregression is a potential target for treatment with Pol I inhibition” and that E210K fibroblasts show ↑ pre‑rRNA/18S, nucleolar stress, and apoptosis, selective, brain-penetrant Pol I modulators are proposed to mitigate nucleolar stress and downstream DNA damage; key open questions concern neuronal tolerance, dosing paradigms, and off-target effects on proliferative tissues. (ledoux2024polymeraseias pages 9-11)
- Mechanistic framing: Reviews emphasize that UBTF E210K represents a ribosomopathy centered on rDNA transcription and chromatin topology, with context-dependent gain-/loss-of-function features; therapeutic strategies could target rDNA transcriptional balance, DDR modulation, and possibly metabolic/mitochondrial support in select patients. (moss2023hmgboxesribosomopathiesand pages 2-3, braden2024anoverviewof pages 1-2, pietra2023expandingtheclinical pages 3-5)

9) Relevant statistics and data from recent studies
- Case counts: As of early 2024, ~17 reported E210K cases synthesized in a contemporary review; numbers remain small and evolving. (braden2024anoverviewof pages 1-2)
- Seizures/EEG: Seizures in ~35%, abnormal EEG without seizures ~12%, neither in ~53%. (braden2024anoverviewof pages 5-6)
- Imaging: All reported cases with cerebral atrophy and diffuse/symmetric white-matter T2 hyperintensities; ventriculomegaly and corpus callosum thinning frequent; some with cerebellar atrophy; occasional thalamic T2 hyperintensities. (braden2024anoverviewof pages 5-6)
- Cellular: Patient fibroblasts with E210K: >3x pre‑rRNA, >2x 18S rRNA; fewer nucleoli and increased 53BP1 foci; apoptosis and G2-phase abnormalities. (ledoux2024polymeraseias pages 9-11)

10) Evidence items with PMIDs/DOIs and key quotes
- Braden 2024 (review; Brain Sciences; Published Feb 15, 2024): “This variant causes unstable preinitiation complexes to form, resulting in altered rDNA chromatin structures, rRNA dysregulation, DNA damage, and ultimately, neurodegeneration.” URL: https://doi.org/10.3390/brainsci14020179 (braden2024anoverviewof pages 1-2)
- Moss 2023 (Frontiers in Genetics; Aug 2023): Contextualizes UBTF E210K as a ribosomopathy; notes increased rRNA in patient fibroblasts vs reduced promoter association in a homozygous mouse knock‑in, indicating context dependence. URL: https://doi.org/10.3389/fgene.2023.1225832 (moss2023hmgboxesribosomopathiesand pages 2-3)
- Pietra 2023 (Neurology Genetics; Dec 2023): Reports mitochondrial proliferation and reduced complex I activity; “PPARGC1A was upregulated in UBTF1 p.Glu210Lys human fibroblasts… suggest[ing] mitochondrial dysfunction as a new direction for further investigations.” URL: https://doi.org/10.1212/NXG.0000000000200098 (pietra2023expandingtheclinical pages 3-5)
- Theophanous 2023 (JBC; Oct 2023): UBF depletion reduces pUBF, total UBF1/2, and RRN3; ChIP shows reduced UBF occupancy across rDNA, demonstrating network-level downregulation of Pol I transcription when UBF is limited. URL: https://doi.org/10.1016/j.jbc.2023.105203 (theophanous2023transcriptionfactorubf pages 6-8)
- Hussein 2023 (Translational Psychiatry, posted May 14, 2023): iPSC cortical neurons with UBTF E210K show increased Na+ currents and EPSC amplitude, indicating early hyperexcitability. URL: https://doi.org/10.1101/2022.11.02.514882 (hussein2023earlymaturationand pages 2-4)
- LeDoux 2024 (Biomedicines; May 2024): “UBTF-associated neuroregression is a potential target for treatment with Pol I inhibition.” Reviews E210K cell data and discusses key translational questions. URL: https://doi.org/10.3390/biomedicines12051092 (ledoux2024polymeraseias pages 9-11)
- Toro 2018 (Human Molecular Genetics; Feb 2018): Landmark report of recurrent E210K with cellular phenotypes (↑ pre‑rRNA/18S, nucleolar abnormalities, DNA breaks, apoptosis) and progressive neuroimaging and clinical decline. DOI: https://doi.org/10.1093/hmg/ddy049 (toro2018arecurrentde pages 1-1)

Ontology-structured annotations for knowledge base integration
- Gene/protein (HGNC): UBTF (HGNC:12592) (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3)
- Biological process (GO): rRNA transcription by RNA polymerase I (GO:0006360); ribosome biogenesis (GO:0042254); preinitiation complex assembly (GO:0070897); chromatin organization (GO:0006325); DNA damage response (GO:0006974); apoptotic signaling (GO:0072331) (braden2024anoverviewof pages 1-2, theophanous2023transcriptionfactorubf pages 6-8, moss2023hmgboxesribosomopathiesand pages 2-3, ledoux2024polymeraseias pages 9-11)
- Cellular component (GO CC): Nucleolus (GO:0005730); RNA polymerase I complex (GO:0005671); rDNA chromatin within NORs (braden2024anoverviewof pages 1-2, ledoux2024polymeraseias pages 9-11, moss2023hmgboxesribosomopathiesand pages 2-3)
- Cell type (CL): Cortical neuron (CL:0002604) (hussein2023earlymaturationand pages 2-4)
- Anatomy (UBERON): Cerebral cortex (UBERON:0000956); White matter (UBERON:0002436); Corpus callosum (UBERON:0002353); Cerebellum (UBERON:0002037); Thalamus (UBERON:0001897) (braden2024anoverviewof pages 5-6, moss2023hmgboxesribosomopathiesand pages 2-3)
- Phenotypes (HPO): Developmental regression (HP:0002376); Intellectual disability (HP:0001249); Aphasia (HP:0002371); Dysarthria (HP:0001260); Hypotonia (HP:0001252); Ataxia (HP:0001251); Dystonia (HP:0001332); Parkinsonism (HP:0001300); Seizures (HP:0001250); Microcephaly (HP:0000252); Cerebral atrophy (HP:0002059); Thinning corpus callosum (HP:0002079); Ventriculomegaly (HP:0002119); White matter hyperintensities (HP:0030171) (braden2024anoverviewof pages 5-6, braden2024anoverviewof pages 1-2)
- Chemicals/metabolites (CHEBI): Biopterin (CHEBI:17097); Sodium ion (CHEBI:29101) (pietra2023expandingtheclinical pages 3-5, hussein2023earlymaturationand pages 2-4)

Current limitations and open questions
- Small cohort size (~17 cases synthesized as of Feb 2024) limits genotype–phenotype correlations and natural history precision; more prospective data are needed. (braden2024anoverviewof pages 1-2)
- Mechanistic dichotomy across model systems (human fibroblasts vs mouse homozygous knock-in) underscores the need for human neuronal models and in vivo validation. (moss2023hmgboxesribosomopathiesand pages 2-3)
- Therapeutic development will require selective CNS-targeted modulation of Pol I/rRNA synthesis with defined windows of neuronal tolerance, plus biomarker strategies (e.g., nucleolar morphology, rRNA intermediates, neuronal excitability readouts). (ledoux2024polymeraseias pages 9-11, hussein2023earlymaturationand pages 2-4)

URLs and publication dates (selected key sources)
- Braden 2024 (Published Feb 15, 2024): https://doi.org/10.3390/brainsci14020179 (braden2024anoverviewof pages 1-2)
- LeDoux 2024 (Published May 2024): https://doi.org/10.3390/biomedicines12051092 (ledoux2024polymeraseias pages 9-11)
- Moss 2023 (Published Aug 2023): https://doi.org/10.3389/fgene.2023.1225832 (moss2023hmgboxesribosomopathiesand pages 2-3)
- Theophanous 2023 (Published Oct 2023): https://doi.org/10.1016/j.jbc.2023.105203 (theophanous2023transcriptionfactorubf pages 6-8)
- Pietra 2023 (Published Dec 2023): https://doi.org/10.1212/NXG.0000000000200098 (pietra2023expandingtheclinical pages 3-5)
- Hussein 2023 (Preprint posted May 14, 2023): https://doi.org/10.1101/2022.11.02.514882 (hussein2023earlymaturationand pages 2-4)
- Toro 2018 (Published Feb 2018): https://doi.org/10.1093/hmg/ddy049 (toro2018arecurrentde pages 1-1)

Conclusion
Houge-Janssens syndrome (UBTF neuroregression/CONDBA) is a ribosomopathy of rDNA transcription and nucleolar function, most often due to a recurrent de novo E210K substitution in UBTF HMG-box 2. Converging evidence from patient cells, iPSC-derived neurons, and mechanistic studies indicates dysregulated Pol I-dependent rRNA synthesis, altered rDNA chromatin topology, nucleolar stress, DNA damage, and neuronal hyperexcitability as central features that align with a progressive neurodegenerative course beginning in early childhood. Imaging uniformly demonstrates progressive cerebral atrophy with diffuse white matter signal abnormalities and corpus callosum thinning, with variable cerebellar and thalamic involvement. Therapeutically, carefully titrated modulation of Pol I activity and mitigation of nucleolar stress/DNA damage are leading hypotheses, with additional attention to mitochondrial/metabolic abnormalities in subsets of patients. Further human neuronal modeling and longitudinal natural-history studies are priorities to refine mechanisms, biomarkers, and therapeutic windows. (braden2024anoverviewof pages 1-2, moss2023hmgboxesribosomopathiesand pages 2-3, pietra2023expandingtheclinical pages 3-5, theophanous2023transcriptionfactorubf pages 6-8, hussein2023earlymaturationand pages 2-4, ledoux2024polymeraseias pages 9-11, toro2018arecurrentde pages 1-1)

References

1. (braden2024anoverviewof pages 1-2): Anneliesse A Braden, Jianfeng Xiao, Roderick T. Hori, Chester Brown, and Mohammad Moshahid Khan. An overview of ubtf neuroregression syndrome. Brain Sciences, 14:179, Feb 2024. URL: https://doi.org/10.3390/brainsci14020179, doi:10.3390/brainsci14020179. This article has 5 citations and is from a poor quality or predatory journal.

2. (moss2023hmgboxesribosomopathiesand pages 2-3): Tom Moss, Mark S. LeDoux, and Colyn Crane-Robinson. Hmg-boxes, ribosomopathies and neurodegenerative disease. Frontiers in Genetics, Aug 2023. URL: https://doi.org/10.3389/fgene.2023.1225832, doi:10.3389/fgene.2023.1225832. This article has 10 citations and is from a peer-reviewed journal.

3. (pietra2023expandingtheclinical pages 3-5): Andrea Pietra, Flavia Palombo, Melania Giannotta, Monica Maffei, Claudio Fiorini, Roberta Costa, Giovanna Cenacchi, Valerio Carelli, Duccio Maria Cordelli, Antonella Pini, and Caterina Garone. Expanding the clinical spectrum of <i>ubtf</i> -related neurodevelopmental disorder. Neurology Genetics, Dec 2023. URL: https://doi.org/10.1212/nxg.0000000000200098, doi:10.1212/nxg.0000000000200098. This article has 5 citations.

4. (theophanous2023transcriptionfactorubf pages 6-8): Andria Theophanous, Andri Christodoulou, Charalambia Mattheou, Dany S. Sibai, Tom Moss, and Niovi Santama. Transcription factor ubf depletion in mouse cells results in downregulation of both downstream and upstream elements of the rrna transcription network. Journal of Biological Chemistry, 299:105203, Oct 2023. URL: https://doi.org/10.1016/j.jbc.2023.105203, doi:10.1016/j.jbc.2023.105203. This article has 12 citations and is from a domain leading peer-reviewed journal.

5. (hussein2023earlymaturationand pages 2-4): Yara Hussein, Utkarsh Tripathi, Ashwani Choudhary, Ritu Nayak, David Peles, Idan Rosh, Tatiana Rabinski, Jose Djamus, Gad Vatine, Ronen Spiegel, Tali Garin-Shkolnik, and Shani Stern. Early maturation and hyperexcitability is a shared phenotype of cortical neurons derived from different asd-associated mutations. Translational Psychiatry, May 2023. URL: https://doi.org/10.1101/2022.11.02.514882, doi:10.1101/2022.11.02.514882. This article has 47 citations and is from a peer-reviewed journal.

6. (ledoux2024polymeraseias pages 9-11): Mark S. LeDoux. Polymerase i as a target for treating neurodegenerative disorders. Biomedicines, 12:1092, May 2024. URL: https://doi.org/10.3390/biomedicines12051092, doi:10.3390/biomedicines12051092. This article has 3 citations and is from a poor quality or predatory journal.

7. (toro2018arecurrentde pages 1-1): Camilo Toro, Roderick T Hori, May Christine V Malicdan, Cynthia J Tifft, Amy Goldstein, William A Gahl, David R Adams, Harper B Fauni, Lynne A Wolfe, Jianfeng Xiao, Mohammad M Khan, Jun Tian, Kevin A Hope, Lawrence T Reiter, Michel G Tremblay, Tom Moss, Alexis L Franks, Chris Balak, and Mark S LeDoux. A recurrent de novo missense mutation in ubtf causes developmental neuroregression. Human Molecular Genetics, 27:1310-1310, Feb 2018. URL: https://doi.org/10.1093/hmg/ddy049, doi:10.1093/hmg/ddy049. This article has 55 citations and is from a domain leading peer-reviewed journal.

8. (braden2024anoverviewof pages 8-10): Anneliesse A Braden, Jianfeng Xiao, Roderick T. Hori, Chester Brown, and Mohammad Moshahid Khan. An overview of ubtf neuroregression syndrome. Brain Sciences, 14:179, Feb 2024. URL: https://doi.org/10.3390/brainsci14020179, doi:10.3390/brainsci14020179. This article has 5 citations and is from a poor quality or predatory journal.

9. (braden2024anoverviewof pages 5-6): Anneliesse A Braden, Jianfeng Xiao, Roderick T. Hori, Chester Brown, and Mohammad Moshahid Khan. An overview of ubtf neuroregression syndrome. Brain Sciences, 14:179, Feb 2024. URL: https://doi.org/10.3390/brainsci14020179, doi:10.3390/brainsci14020179. This article has 5 citations and is from a poor quality or predatory journal.