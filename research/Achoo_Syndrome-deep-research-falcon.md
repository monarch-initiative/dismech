---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-05T16:39:03.335167'
end_time: '2025-12-05T16:43:33.388854'
duration_seconds: 270.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Achoo Syndrome
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
- **Disease Name:** Achoo Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Achoo Syndrome**.
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
- **Disease Name:** Achoo Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Achoo Syndrome**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: ACHOO Syndrome (Photic Sneeze Reflex)
- MONDO ID: Not established/curated as of latest literature; disorder is described in reviews and GWAS reports rather than a stabilized disease ontology entry (cross-referenced historically in OMIM).
- Category: Genetic (complex, polygenic; familial clustering reported)

## Pathophysiology description
ACHOO syndrome, formally the photic sneeze reflex (PSR), is an involuntary sneeze or nasal prickle provoked by sudden exposure to bright light. Contemporary reviews emphasize that several mechanistic hypotheses exist but no single model has been conclusively validated. Proposed mechanisms include optic–trigeminal summation (interaction of retinal/optic inputs with trigeminal pathways) and parasympathetic generalization or hypersensitivity (light-evoked activation in one parasympathetic division spreading to nasal secretomotor pathways). Neurophysiologic observations synthesized in a 2025 mini-review note visual cortex excitability (particularly in cuneus) and co-activation of somatosensory cortices (insula and secondary somatosensory cortex) during photic sneezing, with a notable absence of reproducible electrical activity in the nasal mucosa despite subjective nasal tickling, suggesting a centrally mediated reflex involving visual and somatosensory networks rather than a purely peripheral nasal origin. Nonetheless, trigeminal and autonomic outflow pathways are still implicated by clinical correlations and reflex literature. Current evidence supports a complex, polygenic architecture with GWAS-identified intergenic loci near ZEB2/ACVR2A (rs10427255) and near CADM2 (rs1032507), which may exert distal regulatory effects. Population prevalence is variably reported across cohorts; self-report in a Chinese GWAS cohort was 25.6%, while a large Japanese survey reported 3.1%. Associations with migraine and elevated psychological distress have been observed. Together, these data support a model where abrupt luminance change engages visual pathways that in susceptible individuals cross-activate trigeminal/autonomic circuits to produce prickle and sneeze, with genetic variants modulating susceptibility thresholds. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5, wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3, sasayama2019possibleassociationbetween pages 1-2)

Direct supporting quotes
- “Multiple mechanistic hypotheses exist but lack conclusive evidence: optic-trigeminal summation […] parasympathetic hypersensitivity, and parasympathetic generalization.” (mini-review summary) (trinkl2025stimulusconditionseliciting pages 1-2)
- “No parametric relationship between light parameters and the PSR [has been] examined.” (trinkl2025stimulusconditionseliciting pages 6-7)
- “The minor alleles respectively contributed to increased or reduced risk for PSR with odds ratio […] 1.68 […] for rs10427255 and 0.65 […] for rs1032507.” (Scientific Reports GWAS) (wang2019agenomewideassociation pages 1-2)
- “Self-reported PSR prevalence 25.6% […] Male 30.1% vs Female 21.1%.” (wang2019agenomewideassociation pages 2-3)
- “PSS was associated with migraine (OR = 1.97 […]), and psychological distress (K6 ≥5: OR = 1.40; K6 ≥13: OR = 1.49).” (sasayama2019possibleassociationbetween pages 1-2)

## Gene/protein annotations with ontology terms
- Nearby/implicated genes by GWAS locus proximity (noncoding associations):
  - ZEB2 (HGNC:11642) and ACVR2A (HGNC:171) near rs10427255 (2q22.3); intergenic association suggests possible long-range regulatory effects rather than coding variation. Mechanistic role in PSR remains hypothetical. (wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3) 
  - CADM2 (HGNC:17867) near rs1032507 (3p12.1); locus possibly within/promoter region; CADM2 is involved in synaptic adhesion and neuronal excitability, offering a plausible neurobiological link. (wang2019agenomewideassociation pages 1-2)

- Putative functional pathways (by hypothesis and neurophysiology):
  - Optic–trigeminal interaction: integration of retinal/visual cortex activity with trigeminal sensory pathways. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)
  - Parasympathetic generalization/hypersensitivity: cross-activation of parasympathetic branches causing nasal secretomotor activation and prickle. (sasayama2019possibleassociationbetween pages 1-2, trinkl2025stimulusconditionseliciting pages 1-2)

## Phenotype associations (HPO terms; labels with supporting evidence)
- Sneezing provoked by light (light-triggered sneezing) – core phenotype; recurrent immediately after abrupt light exposure. (trinkl2025stimulusconditionseliciting pages 1-2, wang2019agenomewideassociation pages 1-2)
- Nasal prickle/tickling preceding sneeze. (trinkl2025stimulusconditionseliciting pages 3-5)
- Photophobia-like sensitivity to bright light (not diagnostic of photophobia per se but overlap noted in reviews). (trinkl2025stimulusconditionseliciting pages 1-2)
- Comorbid migraine risk increased. (sasayama2019possibleassociationbetween pages 1-2)
- Psychological distress measures elevated (K6). (sasayama2019possibleassociationbetween pages 1-2)

## Cell type involvement (CL terms; labels)
- Retinal ganglion cells (including melanopsin-expressing intrinsically photosensitive RGCs) – proposed sensory input. (trinkl2025stimulusconditionseliciting pages 1-2)
- Trigeminal ganglion neurons and brainstem trigeminal nuclei – candidate sensory integration nodes. (trinkl2025stimulusconditionseliciting pages 1-2)
- Autonomic (parasympathetic) preganglionic neurons – hypothesized efferent limb for nasal secretomotor responses. (trinkl2025stimulusconditionseliciting pages 1-2, sasayama2019possibleassociationbetween pages 1-2)
- Cortical neurons in visual cortex (cuneus), insula, and secondary somatosensory cortex – observed co-activation in response to photic sneezing. (trinkl2025stimulusconditionseliciting pages 3-5)

## Anatomical locations (UBERON terms; labels)
- Retina/optic pathways; primary/associative visual cortex (cuneus). (trinkl2025stimulusconditionseliciting pages 3-5)
- Trigeminal brainstem complex. (trinkl2025stimulusconditionseliciting pages 1-2)
- Nasal mucosa (target of secretomotor drive; lacks reproducible peripheral electrical correlate during reflex). (trinkl2025stimulusconditionseliciting pages 3-5)

## Chemical entities (CHEBI; labels)
- Light as a physical stimulus (photic input; not a chemical entity). Reviews discuss intensity, spectral composition (wavelength), duration, timing, spatial configuration as critical stimulus dimensions; no specific pharmacologic mediator is established for ACHOO reflex. (trinkl2025stimulusconditionseliciting pages 6-7, trinkl2025stimulusconditionseliciting pages 1-2)

## Biological processes (GO-style labels)
- Visual signal transduction and cortical visual processing. (trinkl2025stimulusconditionseliciting pages 3-5)
- Trigeminal sensory processing and sensorimotor integration. (trinkl2025stimulusconditionseliciting pages 1-2)
- Parasympathetic nervous system activation and generalization. (sasayama2019possibleassociationbetween pages 1-2, trinkl2025stimulusconditionseliciting pages 1-2)
- Sneezing reflex arc execution (respiratory reflex pattern generation). (trinkl2025stimulusconditionseliciting pages 1-2)

## Core Pathophysiology
- Primary mechanisms: cross-activation between visual pathways and trigeminal/autonomic circuits (optic–trigeminal summation) and/or parasympathetic generalization leading to nasal prickle and sneeze. Cortical involvement (visual and somatosensory areas) likely participates in reflex initiation in susceptible individuals. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5, sasayama2019possibleassociationbetween pages 1-2)
- Dysregulated pathways: sensory integration between visual and trigeminal/autonomic systems; altered thresholds for luminance-change detection and downstream autonomic outflow. (trinkl2025stimulusconditionseliciting pages 1-2)
- Affected cellular processes: sensory transduction of light, central sensory integration, parasympathetic secretomotor activation, and sneeze pattern generation. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)

## Key Molecular Players
- Genes/Proteins: intergenic associations near ZEB2/ACVR2A (rs10427255) and near CADM2 (rs1032507) suggest regulatory influences on neuronal circuits; precise effector molecules remain to be proven. (wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3)
- Chemical entities: no specific endogenous ligand established; the triggering “agent” is abrupt bright light (stimulus-level parameterization pending). (trinkl2025stimulusconditionseliciting pages 6-7)
- Cell types: retinal ganglion cells; trigeminal sensory neurons; parasympathetic preganglionic neurons; cortical neurons in cuneus/insula/S2. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)
- Anatomical sites: retina/optic pathways; visual cortex (cuneus); trigeminal brainstem; nasal mucosa. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)

## Cellular Components
- Plasma membrane phototransduction machinery in retinal ganglion cells; cortical synaptic networks in cuneus/insula/S2; autonomic synapses in parasympathetic pathways; nasal mucosal glands as end-organ targets of secretomotor drive. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)

## Disease Progression and Sequence of Events
1) Trigger: abrupt increase in light intensity (luminance change). (trinkl2025stimulusconditionseliciting pages 1-2)
2) Sensory processing: visual pathway activation with cortical excitability in cuneus; subjective nasal prickle arises without local nasal electrical activity, consistent with central co-activation. (trinkl2025stimulusconditionseliciting pages 3-5)
3) Circuit cross-activation: hypothesized integration between visual and trigeminal/autonomic circuits (optic–trigeminal summation; parasympathetic generalization/hypersensitivity). (trinkl2025stimulusconditionseliciting pages 1-2, sasayama2019possibleassociationbetween pages 1-2)
4) Effector response: parasympathetic secretomotor outflow to nasal mucosa with prickle/tickle followed by sneeze motor pattern. (sasayama2019possibleassociationbetween pages 1-2, trinkl2025stimulusconditionseliciting pages 1-2)

Distinct phases: immediate onset within seconds of bright light exposure; number of sneezes may be a few in sequence; the response habituates with sustained exposure, consistent with central adaptation. (trinkl2025stimulusconditionseliciting pages 1-2)

## Phenotypic Manifestations
- Core: light-triggered sneezing; nasal prickle. (trinkl2025stimulusconditionseliciting pages 3-5, trinkl2025stimulusconditionseliciting pages 1-2)
- Associated: overlap with photophobia-like sensitivity and higher odds of migraine; elevated psychological distress scores in some cohorts. (trinkl2025stimulusconditionseliciting pages 1-2, sasayama2019possibleassociationbetween pages 1-2)

## Recent developments and latest research (2023–2025 prioritized)
- A 2025 mini-review consolidated the sparse and heterogeneous literature on stimulus parameters, underscoring the need for standardized parametric experiments varying intensity, wavelength/spectral content, duration, timing, and spatial configuration; it reiterated the leading mechanistic hypotheses and highlighted cortical involvement. Publication date: Feb 2025. URL/DOI: https://doi.org/10.1007/s00221-024-06988-4 (Experimental Brain Research). (trinkl2025stimulusconditionseliciting pages 6-7, trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)

## Current applications and real-world implementations
- Occupational/safety relevance: reflex can be a potential safety concern (e.g., drivers/pilots) during abrupt light transitions; literature calls for better stimulus characterization to inform mitigation (e.g., visor/sunshade strategies). (trinkl2025stimulusconditionseliciting pages 1-2)
- Clinical practice: diagnosis remains history/self-report as provocation is unreliable; reviews note filtering lenses may be ineffective if the primary trigger is luminance change rather than specific wavelengths. Publication date: Mar 2019. URL/DOI: https://doi.org/10.1038/s41598-019-41551-0 (Scientific Reports). (wang2019agenomewideassociation pages 1-2)

## Expert opinions and analysis
- Reviews converge that ACHOO/PSR likely reflects central integration of visual and trigeminal/autonomic circuits, with insufficient evidence to elevate any single hypothesis to consensus. The absence of clear parametric stimulus–response functions is a major gap; standardized experiments are needed to link specific retinal mechanisms (including melanopsin pathways) to reflex probability and magnitude. (trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)

## Relevant statistics and data from recent studies
- Prevalence: 25.6% (95% CI 24.1–27.1) in a Chinese GWAS cohort (n=3,417); male 30.1% vs female 21.1%, P < 1×10⁻⁸. Publication date: Mar 2019. URL/DOI: https://doi.org/10.1038/s41598-019-41551-0. (wang2019agenomewideassociation pages 2-3)
- Japanese population self-report: 3.1% in a large online sample (n ≈ 11,840). Publication date: Jul 2019. URL/DOI: https://doi.org/10.1002/npr2.12067. (sasayama2019possibleassociationbetween pages 1-2)
- Genetics: rs10427255 (2q22.3) OR 1.68 (1.50–1.88) in Chinese cohort (replication of prior U.S. association); rs1032507 (3p12.1) OR 0.65 (0.58–0.72); both intergenic. Publication date: Mar 2019. URL/DOI: https://doi.org/10.1038/s41598-019-41551-0. (wang2019agenomewideassociation pages 1-2)
- Clinical associations: migraine OR 1.97 (P = 2.18×10⁻⁹); psychological distress K6≥5 OR 1.40 (P = 0.00143), K6≥13 OR 1.49 (P = 0.0486). Publication date: Jul 2019. URL/DOI: https://doi.org/10.1002/npr2.12067. (sasayama2019possibleassociationbetween pages 1-2)

## Evidence items with PMIDs/DOIs/URLs and publication dates
- Trinkl J et al., Stimulus conditions eliciting sneezing in response to bright light. Experimental Brain Research. Feb 2025. DOI: 10.1007/s00221-024-06988-4; URL: https://doi.org/10.1007/s00221-024-06988-4. (trinkl2025stimulusconditionseliciting pages 6-7, trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5)
- Wang M et al., A genome-wide association study on photic sneeze reflex in the Chinese population. Scientific Reports. Mar 2019. DOI: 10.1038/s41598-019-41551-0; URL: https://doi.org/10.1038/s41598-019-41551-0. (wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3, wang2019agenomewideassociation pages 7-8)
- Sasayama D et al., Possible association between photic sneeze syndrome and migraine and psychological distress. Neuropsychopharmacology Reports. Jul 2019. DOI: 10.1002/npr2.12067; URL: https://doi.org/10.1002/npr2.12067. (sasayama2019possibleassociationbetween pages 1-2)

Embedded artifact of key evidence
| Category | Item (HGNC/DB symbol when applicable) | Evidence / Mechanism | Effect size / statistic (if applicable) | Year | Source (journal) | DOI / URL | Context ID for citation |
|---|---|---|---:|---:|---|---|---|
| SNP | rs10427255 (intergenic; near ZEB2 / ACVR2A) | GWAS association with photic sneeze reflex; proposed noncoding/regulatory effect | OR 1.68 (95% CI 1.50–1.88) in Chinese cohort; replication OR ~1.32 in prior US study | 2019 (GWAS), 2010 (replication) | Scientific Reports; PLoS Genetics | https://doi.org/10.1038/s41598-019-41551-0 ; https://doi.org/10.1371/journal.pgen.1000993 | (wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3) |
| SNP | rs1032507 (intergenic; near CADM2) | GWAS novel locus; possible promoter/regulatory effect on CADM2 | OR 0.65 (95% CI 0.58–0.72) in Chinese cohort | 2019 | Scientific Reports | https://doi.org/10.1038/s41598-019-41551-0 | (wang2019agenomewideassociation pages 1-2) |
| Prevalence (cohort) | Chinese cohort prevalence | Self-reported PSR in GWAS cohort (n=3,417) | 25.6% (95% CI 24.1%–27.1%) | 2019 | Scientific Reports | https://doi.org/10.1038/s41598-019-41551-0 | (wang2019agenomewideassociation pages 1-2) |
| Prevalence (sex difference) | Male vs Female prevalence | Sex-stratified prevalence reported in Chinese GWAS | Male 30.1% vs Female 21.1%; P < 1×10⁻⁸ | 2019 | Scientific Reports | https://doi.org/10.1038/s41598-019-41551-0 | (wang2019agenomewideassociation pages 2-3) |
| Prevalence (general) | Population estimate | Review and cohort estimates converge on ~1 in 4 people affected | ~25% overall (approximate) | 2025 (review) / 2019 | Experimental Brain Research; Scientific Reports | https://doi.org/10.1007/s00221-024-06988-4 ; https://doi.org/10.1038/s41598-019-41551-0 | (trinkl2025stimulusconditionseliciting pages 1-2, wang2019agenomewideassociation pages 1-2) |
| Prevalence (Japanese) | Japanese cohort prevalence | Large self-report study in Japan | 3.1% (n≈11,840) | 2019 | Neuropsychopharmacology Reports | https://doi.org/10.1002/npr2.12067 | (sasayama2019possibleassociationbetween pages 1-2) |
| Inheritance | Reported familial pattern | Pedigree/family reports suggest autosomal dominant transmission; GWAS indicates complex/polygenic architecture | Familial reports vs GWAS: complex (non-Mendelian) | cited across studies | Scientific Reports; review / case reports | https://doi.org/10.1038/s41598-019-41551-0 ; (various references) | (wang2019agenomewideassociation pages 2-3, sasayama2019possibleassociationbetween pages 1-2) |
| Mechanistic hypotheses | Optic–trigeminal summation; parasympathetic generalization / hypersensitivity | Proposed models: cross-activation between retinal/optic pathways and trigeminal/autonomic circuits; parasympathetic spread to nasal mucosa | N/A (hypotheses; not conclusively proven) | 2019–2025 (reviews & studies) | Experimental Brain Research; Neuropsychopharmacology Reports; Scientific Reports | https://doi.org/10.1007/s00221-024-06988-4 ; https://doi.org/10.1002/npr2.12067 ; https://doi.org/10.1038/s41598-019-41551-0 | (trinkl2025stimulusconditionseliciting pages 1-2, sasayama2019possibleassociationbetween pages 1-2, wang2019agenomewideassociation pages 1-2) |
| Neural activity (neurophys) | Visual cortex (cuneus); insula; S2; nasal recordings | EEG/fMRI studies: visual-cortex excitability and co-activation of somatosensory areas; no reproducible nasal electrical activity recorded | Observed cortical activations; absence of nasal electrical correlate reported | cited in review (behavioral/neurophys studies) | Experimental Brain Research (review citing primary studies) | https://doi.org/10.1007/s00221-024-06988-4 | (trinkl2025stimulusconditionseliciting pages 3-5) |
| Light stimulus parameters | Intensity, spectral composition, duration, timing, spatial configuration | Reviews note these parameters are critical but systematic parametric studies are lacking | No parametric dose–response established | 2025 (mini-review) | Experimental Brain Research | https://doi.org/10.1007/s00221-024-06988-4 | (trinkl2025stimulusconditionseliciting pages 6-7, trinkl2025stimulusconditionseliciting pages 1-2, trinkl2025stimulusconditionseliciting pages 3-5) |
| Clinical associations | Migraine; psychological distress (K6) | Observational association analyses report higher odds of migraine and elevated psychological distress in PSS cases | Migraine OR = 1.97 (P = 2.18×10⁻⁹); K6≥5 OR = 1.40 (P = 0.00143); K6≥13 OR = 1.49 (P = 0.0486) | 2019 | Neuropsychopharmacology Reports | https://doi.org/10.1002/npr2.12067 | (sasayama2019possibleassociationbetween pages 1-2) |


*Table: Compact table summarizing genetic loci, prevalence estimates, proposed mechanisms, neural findings, stimulus parameter gaps, and clinical associations for photic sneeze reflex (ACHOO), with DOIs and context citations for traceability.*

## Gaps and open questions
- Lack of parametric stimulus–response data (intensity/wavelength/duration) prevents definitive linkage to specific retinal photoreceptor pathways. (trinkl2025stimulusconditionseliciting pages 6-7)
- Intergenic GWAS associations implicate regulatory mechanisms but causal variants, target genes, and neuronal circuit effects remain to be experimentally demonstrated. (wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3)
- The magnitude of epidemiologic variation across populations (e.g., 3.1% vs ~25%) suggests survey methods, definitions, and cultural/reporting differences may substantially influence prevalence estimates; standardized phenotyping is needed. (sasayama2019possibleassociationbetween pages 1-2, wang2019agenomewideassociation pages 2-3)

Conclusion
ACHOO/PSR appears to be a common, heritable reflex with polygenic susceptibility. Abrupt luminance changes activate visual cortical networks that, in predisposed individuals, likely cross-activate trigeminal/autonomic pathways to drive nasal prickle and sneezing. Intergenic loci near ZEB2/ACVR2A and CADM2 modulate risk, but causal biology awaits functional dissection. Recent reviews call for standardized, parametric light-stimulus studies and circuit-level neurophysiology to close mechanistic gaps and inform risk mitigation in safety-critical contexts. (trinkl2025stimulusconditionseliciting pages 1-2, wang2019agenomewideassociation pages 1-2, wang2019agenomewideassociation pages 2-3, sasayama2019possibleassociationbetween pages 1-2)

References

1. (trinkl2025stimulusconditionseliciting pages 1-2): Josef Trinkl, Lucien Bickerstaff, Stephan Munkwitz, and Manuel Spitschan. Stimulus conditions eliciting sneezing in response to bright light. Experimental Brain Research, Feb 2025. URL: https://doi.org/10.1007/s00221-024-06988-4, doi:10.1007/s00221-024-06988-4. This article has 3 citations and is from a peer-reviewed journal.

2. (trinkl2025stimulusconditionseliciting pages 3-5): Josef Trinkl, Lucien Bickerstaff, Stephan Munkwitz, and Manuel Spitschan. Stimulus conditions eliciting sneezing in response to bright light. Experimental Brain Research, Feb 2025. URL: https://doi.org/10.1007/s00221-024-06988-4, doi:10.1007/s00221-024-06988-4. This article has 3 citations and is from a peer-reviewed journal.

3. (wang2019agenomewideassociation pages 1-2): Mengqiao Wang, Xinghan Sun, Yang Shi, Xiaojun Song, and Hao Mi. A genome-wide association study on photic sneeze reflex in the chinese population. Scientific Reports, Mar 2019. URL: https://doi.org/10.1038/s41598-019-41551-0, doi:10.1038/s41598-019-41551-0. This article has 9 citations and is from a peer-reviewed journal.

4. (wang2019agenomewideassociation pages 2-3): Mengqiao Wang, Xinghan Sun, Yang Shi, Xiaojun Song, and Hao Mi. A genome-wide association study on photic sneeze reflex in the chinese population. Scientific Reports, Mar 2019. URL: https://doi.org/10.1038/s41598-019-41551-0, doi:10.1038/s41598-019-41551-0. This article has 9 citations and is from a peer-reviewed journal.

5. (sasayama2019possibleassociationbetween pages 1-2): Daimei Sasayama, Shinya Asano, Shun Nogawa, Shoko Takahashi, Kenji Saito, and Hiroshi Kunugi. Possible association between photic sneeze syndrome and migraine and psychological distress. Neuropsychopharmacology Reports, 39:217-222, Jul 2019. URL: https://doi.org/10.1002/npr2.12067, doi:10.1002/npr2.12067. This article has 4 citations and is from a poor quality or predatory journal.

6. (trinkl2025stimulusconditionseliciting pages 6-7): Josef Trinkl, Lucien Bickerstaff, Stephan Munkwitz, and Manuel Spitschan. Stimulus conditions eliciting sneezing in response to bright light. Experimental Brain Research, Feb 2025. URL: https://doi.org/10.1007/s00221-024-06988-4, doi:10.1007/s00221-024-06988-4. This article has 3 citations and is from a peer-reviewed journal.

7. (wang2019agenomewideassociation pages 7-8): Mengqiao Wang, Xinghan Sun, Yang Shi, Xiaojun Song, and Hao Mi. A genome-wide association study on photic sneeze reflex in the chinese population. Scientific Reports, Mar 2019. URL: https://doi.org/10.1038/s41598-019-41551-0, doi:10.1038/s41598-019-41551-0. This article has 9 citations and is from a peer-reviewed journal.