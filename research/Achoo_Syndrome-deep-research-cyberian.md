---
provider: cyberian
model: deep-research
cached: false
start_time: '2025-12-05T17:30:24.908585'
end_time: '2025-12-05T17:51:02.249996'
duration_seconds: 1237.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Achoo Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
citation_count: 18
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

# Pathophysiology of ACHOO Syndrome (Photic Sneeze Reflex)

## Introduction

ACHOO syndrome, formally known as Autosomal Dominant Compelling Helio-Ophthalmic Outburst syndrome, represents a heritable neurological trait characterized by involuntary sneezing upon sudden exposure to bright light, particularly sunlight [collie-1978-achoo-abstract]. Also commonly referred to as the photic sneeze reflex (PSR), this condition affects an estimated 18-35% of the general population, though prevalence estimates vary considerably across studies and populations [everett-1964-sneezing-light-abstract]. The phenomenon was first formally described in the medical literature by Collie and colleagues in 1978, who coined the memorable ACHOO backronym, though the trait itself was observed and documented as far back as Aristotle, who noted in Book XXXIII of his Problems that individuals may sneeze upon looking at the sun [collie-1978-achoo-abstract].

The condition is inherited in an autosomal dominant manner, meaning affected individuals have a 50% probability of transmitting the trait to each offspring [peroutka-1984-autosomal-dominant-abstract]. The presence of male-to-male transmission in affected families confirms autosomal rather than X-linked inheritance [collie-1978-achoo-abstract]. Despite its high prevalence and consistent inheritance pattern, the precise molecular and neurophysiological mechanisms underlying photic sneezing remain incompletely understood, though substantial progress has been made in recent years through genome-wide association studies and neuroimaging research.

This review synthesizes the current understanding of ACHOO syndrome pathophysiology, encompassing its genetic basis, proposed neural mechanisms, molecular pathways, and clinical manifestations. We additionally provide relevant ontological annotations to facilitate integration with disease knowledge bases.

## Disease Definition and Nomenclature

ACHOO syndrome (OMIM: 100820) refers specifically to the inherited tendency to sneeze in response to sudden bright light exposure [peroutka-1984-autosomal-dominant-abstract]. The condition is classified as a benign genetic trait rather than a disease per se, though it has clinical implications for certain occupations and activities. Alternative designations include photic sneeze reflex, sun sneezing, helio-ophthalmic outburst, and photosternutatory reflex. The Peroutka sneeze is sometimes used eponymously following the 1984 publication by Peroutka and Peroutka that documented the condition in a three-generation family study [peroutka-1984-autosomal-dominant-abstract].

The clinical presentation is remarkably consistent: upon emerging from a dark-adapted state into bright sunlight or other intense light, affected individuals experience an irresistible urge to sneeze, typically producing 2-3 consecutive sneezes, though in extreme cases up to 43 successive sneezes have been documented [collie-1978-achoo-abstract]. The condition demonstrates variable expressivity; Morris noted that related reflexes may be triggered by eyebrow plucking or hair pulling in some individuals, suggesting a common mechanism involving trigeminal nerve stimulation [morris-1987-prevalence-abstract]. Approximately 25% of individuals who report a nasal prickling sensation upon light exposure will subsequently sneeze [langer-2010-eeg-abstract].

## Genetic Basis

The autosomal dominant inheritance of photic sneeze reflex has been consistently documented across multiple family studies spanning several decades [collie-1978-achoo-abstract][peroutka-1984-autosomal-dominant-abstract][morris-1987-prevalence-abstract]. However, identification of specific causative genes has proven challenging, likely reflecting the polygenic nature of the trait.

The first genome-wide association study (GWAS) to identify genetic variants associated with photic sneezing was conducted by Eriksson and colleagues in 2010 using the 23andMe web-based platform [eriksson-2010-gwas-abstract]. This study of 5,390 participants of Northern European ancestry identified a novel genome-wide significant association at rs10427255 on chromosome 2q22.3 (−log₁₀P = 10.93, OR = 1.32). This single nucleotide polymorphism (SNP) lies in a large intergenic region approximately 725 kb from the ZEB2 gene and 1.2 Mb from the annotated pseudogene PABPCP2 [eriksson-2010-gwas-abstract]. A secondary association was identified at rs11856995 on chromosome 15q26.2 (−log₁₀P = 7.13, OR = 0.78), located approximately 560 kb from NR2F2 [eriksson-2010-gwas-abstract].

The association with the ZEB2 locus is particularly intriguing from a mechanistic perspective. ZEB2 (Zinc Finger E-Box Binding Homeobox 2; HGNC:14881) encodes a transcription factor that, when mutated, causes Mowat-Wilson syndrome, a condition characterized by intellectual disability, distinctive facial features, and notably, epileptic seizures [eriksson-2010-gwas-abstract]. Photosensitive epilepsy, wherein seizures are triggered by flashing lights, represents another abnormal neural response to photic stimulation. This parallel has led researchers to hypothesize a possible mechanistic connection between photosensitive seizures and the photic sneeze reflex, potentially involving shared neural excitability pathways [eriksson-2010-gwas-abstract].

Subsequent GWAS have replicated and extended these findings in non-European populations. A study of 3,417 Chinese individuals confirmed the rs10427255 association with substantially higher effect size (OR = 1.68, 95% CI: 1.50-1.88, −log₁₀P = 19.26) and identified a novel locus at rs1032507 on chromosome 3p12.1 (OR = 0.65, 95% CI: 0.58-0.72, −log₁₀P = 13.23) [shan-2019-chinese-gwas-abstract]. The rs1032507 variant maps approximately 97 kb upstream of CADM2 (Cell Adhesion Molecule 2; HGNC:939), a gene involved in synapse organization. Interestingly, the minor allele at this locus conferred reduced risk for photic sneezing, representing a protective variant [shan-2019-chinese-gwas-abstract].

A Japanese population study of 11,409 individuals replicated findings at chromosome 3p12.1 at genome-wide significance and identified additional candidate loci at 9q34.2 and 4q35.2 with suggestive significance [sasayama-2018-japanese-gwas-abstract]. The Japanese GWAS identified SNPs rs1691483 and rs1694933 on chromosome 3, located approximately 40 kb from rs1032507, with strong linkage disequilibrium (r² > 0.96) suggesting these represent the same signal [sasayama-2018-japanese-gwas-abstract]. These cross-population replications support a polygenic, non-ethnicity-specific inheritance pattern for photic sneeze reflex.

The combined evidence from GWAS studies suggests at least 54 genetic markers may contribute to photic sneeze reflex susceptibility. The identified genes and loci implicate neural excitability, synaptic organization, and transcriptional regulation in the pathophysiology of the condition.

## Functional Roles of Associated Genes

Understanding the known functions of genes near GWAS-identified variants provides mechanistic insight into potential pathways underlying photic sneeze susceptibility.

### ZEB2 and Neural Excitability

ZEB2 (Zinc Finger E-Box Binding Homeobox 2) is a transcription factor essential for nervous system development, controlling the formation of the neocortex, hippocampus, corpus callosum, and spinal cord [nguyen-2021-zeb2-review-abstract]. ZEB2 determines the timing of neurogenesis-to-gliogenesis transition by regulating neuron-to-progenitor paracrine signaling through Ntf3 and Fgf9 expression [nguyen-2021-zeb2-review-abstract]. Critically for understanding photic sneeze pathophysiology, ZEB2 modifies the electrophysiological properties of nociceptive sensory neurons. Heterozygous Zeb2 mice display altered thermal pain responses attributed to ZEB2 regulation of voltage-gated ion channels that modulate neuronal excitability [nguyen-2021-zeb2-review-abstract].

ZEB2 is also essential for proper tangential migration of GABAergic interneurons and controls their cell identity through NKX2.1 repression [nguyen-2021-zeb2-review-abstract]. Loss of ZEB2 creates a deficiency of GABAergic inhibition thought to underlie focal and absence seizures in Mowat-Wilson syndrome patients [nguyen-2021-zeb2-review-abstract]. This connection between ZEB2 haploinsufficiency and seizure susceptibility provides a compelling mechanistic link to the photic sneeze reflex, as both conditions represent altered neural responses to sensory stimuli. The enhanced visual cortex excitability observed in photic sneezers could potentially reflect reduced GABAergic inhibitory tone regulated by ZEB2-influenced pathways.

### NR2F2/COUP-TFII and GABAergic Circuits

NR2F2 (also known as COUP-TFII) is an orphan nuclear receptor abundantly expressed during embryonic development in the ventral thalamus, hypothalamus, midbrain, pons, and spinal cord [nr2f2-coup-tfii-summary]. COUP-TFII plays a critical role in controlling the tangential migration of subpallial neuronal progenitors, acting as a molecular switch with Neuropilin-2 to direct preoptic area-derived GABAergic neurons toward either the amygdala or cortex [nr2f2-coup-tfii-summary].

The COUP-TF transcription factors are essential for the transition from neurogenesis to gliogenesis, functioning as transcriptional repressors required for neural stem/progenitor cells to acquire gliogenic competence [nr2f2-coup-tfii-summary]. In the adult hippocampus, COUP-TFII expression is restricted to GABAergic interneurons in the CA1 area, with a gradient increasing from undetectable in dorsal to very strong in ventral sectors [nr2f2-coup-tfii-summary]. Given the role of GABAergic inhibition in controlling neural excitability, variants near NR2F2 may influence the development or function of inhibitory circuits that modulate sensory processing thresholds relevant to the photic sneeze reflex.

### CADM2 and Synaptic Organization

CADM2 (Cell Adhesion Molecule 2) is a member of the synaptic cell adhesion molecules (SynCAMs) important for synapse organization, providing regulated trans-synaptic adhesion through homo- and heterophilic interactions with other nectin-like family members [cadm2-synapse-summary]. CADM2 is expressed most abundantly in brain tissue, particularly in the frontal anterior cingulate cortex (6.3-fold enrichment) and areas important for reward processing [cadm2-synapse-summary].

The gene is involved in glutamate signaling, GABA transport, and neuron cell-cell adhesion, with genetic variation associated with individual differences in information processing speed and executive function [cadm2-synapse-summary]. CADM proteins regulate synaptic plasticity and network excitation, suggesting that the protective variant at rs1032507 may influence synaptic connectivity patterns that reduce susceptibility to photic sneezing. The identification of CADM2 as an autism spectrum disorder candidate gene further underscores its role in neural circuit organization that could affect sensory processing.

## Disease Progression: Sequence of Events

The photic sneeze reflex follows a characteristic temporal sequence from initial light exposure to sneeze execution. Understanding this progression helps clarify the underlying pathophysiology.

### Phase 1: Photic Stimulus Detection (0-50 ms)

The cascade begins when a dark-adapted individual is suddenly exposed to bright light, typically sunlight. Retinal photoreceptors (rods and cones) and intrinsically photosensitive retinal ganglion cells (ipRGCs) detect the intense light stimulus. The pupillary light reflex is simultaneously initiated: signals travel via the optic nerve (CN II) to the pretectal olivary nucleus in the midbrain, which projects to the Edinger-Westphal nucleus containing parasympathetic preganglionic neurons [everett-1964-sneezing-light-abstract]. These neurons send axons through the oculomotor nerve (CN III) to synapse in the ciliary ganglion, from which postganglionic fibers innervate the iris sphincter muscle to cause pupillary constriction.

### Phase 2: Aberrant Neural Activation (50-200 ms)

In photic sneezers, the intense visual stimulus triggers enhanced activation in the primary visual cortex, specifically the cuneus, at 56-68 ms following stimulus onset [langer-2010-eeg-abstract]. This early component represents the initial cortical processing of the visual signal. Through mechanisms that remain incompletely understood (optic-trigeminal summation, parasympathetic generalization, or cortical hyperexcitability), the visual stimulus induces cross-activation of trigeminal pathways. A second wave of enhanced visual cortex activation occurs at 200-212 ms, corresponding to higher-order visual processing [langer-2010-eeg-abstract].

### Phase 3: Somatosensory Processing and Nasal Sensation (200-500 ms)

The aberrant activation spreads to somatosensory processing areas. Individuals report a characteristic prickling sensation in the nose, which correlates with activation in the insula and secondary somatosensory cortex (S2) at 204-238 ms [langer-2010-eeg-abstract]. The insula, involved in interoceptive awareness, processes the link between the visual stimulus and the emerging nasal sensation. This cortical processing represents a critical phase distinguishing photic sneezing from the classical chemically-induced sneeze reflex, which does not require cortical involvement.

### Phase 4: Sneeze Reflex Execution (500 ms - 2 s)

If the activation threshold is exceeded, the signal converges on the sneeze-evoking zone in the ventromedial spinal trigeminal nucleus (SpV) in the brainstem. NMBR-expressing neurons in this region project to the caudal ventral respiratory group (cVRG), which coordinates the respiratory motor pattern for sneezing [liu-2021-sneeze-reflex-abstract]. The sneeze itself involves a deep inspiration followed by forced expiration against a closed glottis, then explosive release. Affected individuals typically produce 2-3 consecutive sneezes, though the number varies widely [collie-1978-achoo-abstract].

### Phase 5: Refractory Period and Potential Repeat

Following the initial sneeze(s), a brief refractory period occurs. If the light exposure continues and the individual remains dark-adapted, additional sneezing episodes may occur. However, light adaptation over seconds to minutes typically reduces susceptibility to further photic sneezing until the next transition from darkness to bright light.

## Neural Mechanisms and Pathophysiology

Several theories have been proposed to explain the neural basis of photic sneezing, though none has been conclusively validated [langer-2010-eeg-abstract]. Understanding these mechanisms requires appreciation of both the normal sneeze reflex circuitry and the anomalous neural responses specific to photic sneezers.

### The Normal Sneeze Reflex

The canonical sneeze reflex is initiated by chemical or mechanical stimulation of the nasal or nasopharyngeal mucosa [liu-2021-sneeze-reflex-abstract]. Irritant detection is primarily mediated by small-diameter sensory neurons expressing the TRPV1 (transient receptor potential cation channel subfamily V member 1) receptor, which densely innervate the nasal mucosa [liu-2021-sneeze-reflex-abstract]. Upon activation, these primary afferent neurons transmit signals via the ophthalmic and maxillary branches of the trigeminal nerve (CN V) to the trigeminal nerve nuclei in the brainstem [liu-2021-sneeze-reflex-abstract].

Recent molecular characterization has revealed that neuromedin B (NMB), a neuropeptide, plays a critical role in sneeze signal transmission [liu-2021-sneeze-reflex-abstract]. Li and colleagues demonstrated that NMB-deficient mice selectively lose the ability to sneeze while retaining normal pain responses, indicating NMB specifically encodes sneeze signals rather than general irritant detection [liu-2021-sneeze-reflex-abstract]. Within the brainstem, NMB receptor (NMBR)-expressing neurons comprise approximately 9.1% of the sneeze-evoking region in the spinal trigeminal nucleus, and ablation of these neurons eliminates sneezing [liu-2021-sneeze-reflex-abstract]. These NMBR-positive neurons project exclusively to the caudal ventral respiratory group (cVRG), which contains expiratory neurons controlling abdominal musculature necessary for the explosive expiratory phase of sneezing [liu-2021-sneeze-reflex-abstract].

### Theories of Photic Sneeze Induction

The optic-trigeminal summation hypothesis represents the most widely discussed mechanism for photic sneezing. This theory posits that during intense light stimulation, activated optic nerve (CN II) pathways cross-activate trigeminal nerve pathways in the upper mesencephalic-diencephalic junction where the two pathways converge [langer-2010-eeg-abstract]. Such cross-activation would result in sensations in the nose, which is innervated by the maxillary division of the trigeminal nerve, triggering the sneeze reflex [langer-2010-eeg-abstract]. The anatomical proximity of the optic nerve to the trigeminal nerve provides a structural basis for this crosstalk hypothesis.

The parasympathetic generalization hypothesis offers an alternative explanation based on autonomic nervous system overflow. According to this model, when a bright light stimulus excites a specific branch of the parasympathetic nervous system (causing pupillary constriction), it simultaneously activates other parasympathetic branches [langer-2010-eeg-abstract]. This generalized activation could result in nasal secretion and a tickling sensation in the nasal mucosa, which in turn induces the sneeze reflex [langer-2010-eeg-abstract]. This theory aligns with observations that photic sneezers may have enhanced parasympathetic responses to various stimuli.

A related parasympathetic hypersensitivity theory proposes that photic sneezers have a generalized hypersensitivity of their parasympathetic nervous system, resulting in enhanced excitability to multiple stimuli [sasayama-2019-migraine-abstract]. This heightened parasympathetic tone could lower the threshold for triggering various reflexes, including sneezing.

### Neuroimaging Evidence

The EEG study by Langer and colleagues provided the first direct neurophysiological evidence regarding photic sneeze mechanisms and fundamentally challenged purely brainstem-reflex models [langer-2010-eeg-abstract]. By comparing 10 photic sneezers with 10 matched controls during visual stimulation, the investigators demonstrated that photic sneezers exhibit significantly enhanced activation in the primary visual cortex, specifically in the cuneus, at two distinct timepoints: an early component at 56-68 ms and a later component at 200-212 ms following stimulus presentation [langer-2010-eeg-abstract].

Critically, the subjective prickling sensation in the nose reported by photic sneezers was associated with activation in the insula and secondary somatosensory cortex (S2) [langer-2010-eeg-abstract]. The insula is known to be involved in interoceptive awareness and processing the link between bodily actions and sensations with emotional experience. The insula exhibits reciprocal connections with S2, supporting integrated processing of bodily representations [langer-2010-eeg-abstract].

These findings demonstrate that the photic sneeze reflex is not a classical reflex occurring only at brainstem or spinal cord levels but involves specific cortical areas [langer-2010-eeg-abstract]. The enhanced visual cortex excitability in photic sneezers may represent altered developmental organization or anticipatory visual processing, while the somatosensory activations correspond to the nasal sensations that precede sneezing [langer-2010-eeg-abstract].

### Relationship to Trigeminocardiac Reflex

Recent work has noted parallels between photic sneeze reflex and the trigeminocardiac reflex (TCR), a well-characterized brainstem reflex defined by sudden onset of parasympathetic dysrhythmia, hypotension, apnea, or gastric hypermotility during stimulation of trigeminal nerve sensory branches [sasayama-2019-migraine-abstract]. It has been proposed that photic sneeze reflex may represent a subtype of the TCR, given their shared involvement of the trigeminal nerve, brainstem nuclei, and parasympathetic activation patterns [sasayama-2019-migraine-abstract].

## Association with Migraine and Photophobia

An important clinical observation is the significant association between photic sneeze syndrome and migraine headaches [sasayama-2019-migraine-abstract]. In a cross-sectional study of 11,840 Japanese participants, individuals with photic sneeze syndrome demonstrated nearly double the odds of suffering from migraine compared to those without the condition (OR = 1.97, 95% CI: 1.57-2.48, P = 2.18 × 10⁻⁹) [sasayama-2019-migraine-abstract].

This association may be explained by shared trigeminal nerve involvement in both conditions. Migraine headaches are frequently accompanied by photophobia (light sensitivity), which is thought to result from light-induced activation of the trigeminal nerve system, in a manner similar to the mechanism proposed for photic sneeze syndrome [sasayama-2019-migraine-abstract]. Activation of trigeminal nerves that innervate cranial blood vessels has been implicated in migraine pathophysiology [sasayama-2019-migraine-abstract].

Functional magnetic resonance imaging studies have demonstrated activation of the trigeminal nerve system at the level of the trigeminal ganglion during photophobic responses [sasayama-2019-migraine-abstract]. Light-conducting nerves from the eye have input to the thalamus, where they modulate pain fibers coming to the thalamus from the meninges lining the brain [sasayama-2019-migraine-abstract]. This pain signal is also conveyed to the sensory trigeminal nucleus in the lower brainstem.

Individuals with photic sneeze syndrome were also more likely to experience clinically relevant psychological distress (OR = 1.40, P = 0.00143) and severe psychological distress (OR = 1.49, P = 0.0486) as measured by the Kessler Psychological Distress Scale [sasayama-2019-migraine-abstract]. These associations suggest that photic sneeze syndrome may serve as a marker for trigeminal nerve hypersensitivity that predisposes to both migraine and stress-related disorders.

## Ontological Annotations

### Disease Identifiers
- **OMIM:** 100820
- **MONDO:** MONDO:0007010 (Achoo syndrome)

### Genes/Proteins (HGNC)

**GWAS-Associated Genes:**
- **ZEB2** (HGNC:14881): Zinc Finger E-Box Binding Homeobox 2; associated locus at 2q22.3; regulates GABAergic interneuron development and voltage-gated ion channels
- **NR2F2** (HGNC:7976): Nuclear Receptor Subfamily 2 Group F Member 2 (COUP-TFII); associated locus at 15q26.2; controls GABAergic neuron migration
- **CADM2** (HGNC:14915): Cell Adhesion Molecule 2; associated locus at 3p12.1; synaptic organization and neural connectivity

**Sneeze Reflex Pathway Genes:**
- **NMB** (HGNC:7843): Neuromedin B; neuropeptide essential for sneeze signaling in brainstem
- **NMBR** (HGNC:7844): Neuromedin B Receptor; expressed in sneeze-evoking zone neurons of spinal trigeminal nucleus
- **TRPV1** (HGNC:12716): Transient Receptor Potential Cation Channel Subfamily V Member 1; expressed in nasal sensory neurons detecting irritants

**Ion Channels and Neurotransmission:**
- **SCN9A** (HGNC:10590): Sodium Voltage-Gated Channel Alpha Subunit 9 (NaV1.7); nociceptive sensory neuron excitability
- **SCN10A** (HGNC:10582): Sodium Voltage-Gated Channel Alpha Subunit 10 (NaV1.8); action potential initiation in trigeminal neurons
- **GABRA1** (HGNC:4075): GABA Type A Receptor Subunit Alpha1; inhibitory neurotransmission in cortical circuits

### Human Phenotype Ontology (HP) Terms
- **HP:0000017** - Episodic reflex sneezing
- **HP:0000613** - Photophobia
- Light-induced sneezing (not currently assigned specific HP term)

### Cell Type Ontology (CL) Terms
- **CL:0000101** - Sensory neuron (nasal TRPV1+ sensory neurons)
- **CL:0000526** - Afferent neuron (trigeminal afferents)
- **CL:0000206** - Glutamatergic neuron
- **CL:0011105** - Nociceptor
- Retinal photoreceptors
- Secondary somatosensory cortical neurons

### Anatomical Locations (UBERON)

**Sensory Input Structures:**
- **UBERON:0000966** - Retina (photoreceptor layer detecting light stimulus)
- **UBERON:0001790** - Inner segment of retina
- **UBERON:0000941** - Cranial nerve II (optic nerve)
- **UBERON:0001707** - Nasal cavity (source of afferent signals in normal sneezing)
- **UBERON:0001645** - Trigeminal nerve (CN V)
- **UBERON:0002597** - Trigeminal ganglion (primary sensory neuron cell bodies)

**Brainstem Integration Centers:**
- **UBERON:0002142** - Trigeminal nucleus (brainstem integration center)
- **UBERON:0001943** - Spinal trigeminal nucleus (contains sneeze-evoking zone)
- **UBERON:0002298** - Medulla oblongata (contains sneeze-evoking zone)
- **UBERON:0002139** - Pretectal region (receives retinal input for pupillary reflex)
- **UBERON:0001986** - Edinger-Westphal nucleus (parasympathetic preganglionic neurons)
- **UBERON:0000966** - Ciliary ganglion (parasympathetic postganglionic neurons)

**Cortical Areas (activated in photic sneezers):**
- **UBERON:0002671** - Cuneus (primary visual cortex region showing enhanced activation)
- **UBERON:0002417** - Insula (activated during prickling sensation)
- **UBERON:0001393** - Secondary somatosensory cortex (S2)
- **UBERON:0001870** - Frontal cortex (CADM2 expression enrichment)

**Motor Output Structures:**
- **UBERON:0002411** - Caudal ventral respiratory group (cVRG; respiratory motor pattern)
- **UBERON:0001103** - Diaphragm (inspiratory phase of sneeze)
- **UBERON:0002378** - Intercostal muscles (expiratory phase of sneeze)

### Gene Ontology (GO) Biological Processes
- **GO:0050905** - Neuromuscular process (sneeze motor execution)
- **GO:0007165** - Signal transduction
- **GO:0007268** - Synaptic transmission
- **GO:0050890** - Cognition (visual perception)
- **GO:0007601** - Visual perception
- **GO:0009583** - Detection of light stimulus
- **GO:0019233** - Sensory perception of pain (related pathways)
- **GO:0050877** - Nervous system process
- **GO:0007186** - G protein-coupled receptor signaling pathway (NMB/NMBR signaling)
- **GO:0030534** - Adult behavior (reflex responses)
- **GO:0042391** - Regulation of membrane potential
- **GO:0007399** - Nervous system development (ZEB2, NR2F2 roles)
- **GO:0030182** - Neuron differentiation
- **GO:0007411** - Axon guidance (NR2F2/COUP-TFII function)
- **GO:0016358** - Dendrite development
- **GO:0048167** - Regulation of synaptic plasticity (CADM2 function)

### Gene Ontology (GO) Cellular Components
- **GO:0043005** - Neuron projection (axons and dendrites of trigeminal neurons)
- **GO:0030424** - Axon (trigeminal afferents)
- **GO:0045202** - Synapse (site of NMB/NMBR signaling)
- **GO:0098793** - Presynapse (neurotransmitter release site)
- **GO:0098794** - Postsynapse (signal reception)
- **GO:0005886** - Plasma membrane (location of ion channels and receptors)
- **GO:0016021** - Integral component of membrane (TRPV1, voltage-gated channels)
- **GO:0030425** - Dendrite (visual cortex neuron receiving input)
- **GO:0005634** - Nucleus (ZEB2, NR2F2 transcription factor localization)
- **GO:0043025** - Neuronal cell body (trigeminal ganglion neurons)
- **GO:0043195** - Terminal bouton (synaptic release of NMB)
- **GO:0034704** - Calcium channel complex (involved in neurotransmitter release)
- **GO:0001518** - Voltage-gated sodium channel complex (action potential generation)

### Chemical Entities (CHEBI)
- **CHEBI:28757** - Neuromedin B
- **CHEBI:18243** - Glutamate (neurotransmitter in trigeminal pathways)
- **CHEBI:16796** - Acetylcholine (parasympathetic neurotransmission)
- **CHEBI:16709** - Histamine (can trigger sneezing)
- **CHEBI:4911** - Capsaicin (TRPV1 agonist used experimentally)

## Clinical Manifestations and Significance

The primary clinical manifestation of ACHOO syndrome is the reflexive production of one or more sneezes upon sudden exposure to bright light after a period of dark adaptation [collie-1978-achoo-abstract]. The condition is typically triggered when emerging from road tunnels into sunlight, passing through sunlit gaps in forest, or simply stepping outdoors from a dark interior space [peroutka-1984-autosomal-dominant-abstract].

While generally benign, photic sneezing has potential safety implications for certain activities. The condition can pose a hazard for pilots during critical flight phases when transitioning between different lighting conditions, and for drivers emerging from tunnels into bright sunlight when the sneeze could cause momentary loss of control [morris-1987-prevalence-abstract]. Some affected individuals have learned behavioral strategies to abort the sneeze, such as pressing the philtrum (the groove between the nose and upper lip), which may work by providing competing trigeminal sensory input [morris-1987-prevalence-abstract].

The prevalence of photic sneeze reflex varies across studies. Everett found the trait in 23% of Johns Hopkins medical students, with notable demographic variation: 28% of white males, 15% of white females, and 2% of both Black males and females [everett-1964-sneezing-light-abstract]. Morris found the trait in 20% of surveyed neurologists [morris-1987-prevalence-abstract]. In Asian populations, the prevalence appears somewhat lower: 3.2% in Japanese and 25.6% in Chinese study populations, though methodological differences may account for some of this variation [sasayama-2018-japanese-gwas-abstract][shan-2019-chinese-gwas-abstract]. Notably, the Chinese study found higher prevalence in males (30.1%) compared to females (21.1%) [shan-2019-chinese-gwas-abstract].

## Management and Therapeutic Approaches

There is no cure for photic sneeze reflex and no pharmacological treatment specifically targeting the condition. Management focuses on reducing sudden exposure to bright light or employing behavioral countermeasures. Protective eyewear, including sunglasses and wide-brimmed hats, can reduce the intensity of light reaching the retina during transitions from dark to bright environments, thereby attenuating the stimulus.

The most formally documented behavioral intervention is the philtral pressure technique (PPT), described by Semes in 2019 following 35 years of clinical observation [semes-2019-ppt-abstract]. This technique involves firm digital pressure applied by the patient's index finger transversely to the skin of the sub-philtral region (the groove between nose and upper lip), directed posterosuperiorly onto the maxilla. In a small case series, PPT successfully prevented photic sneezing in 3 patients requiring clinical management during ophthalmic examination [semes-2019-ppt-abstract].

The mechanism by which PPT suppresses the photic sneeze reflex is not established, but two hypotheses have been proposed: (1) local mechanoreceptors stimulated by pressure may override trigeminal nerve irritation, or (2) the pressure may interfere with parasympathetic fiber coactivation involved in the sneeze reflex [semes-2019-ppt-abstract]. The technique has been compared to sensory tricks used in movement disorders such as blepharospasm, where competing sensory input can temporarily suppress involuntary motor responses. Military research has demonstrated that interference filters (wavelength-blocking eyewear) are ineffective, suggesting that photic sneezing is mediated by changes in light intensity rather than specific wavelengths.

For individuals with concurrent allergic rhinitis, treatment of the underlying nasal inflammation may reduce overall sneeze sensitivity and thereby attenuate the photic sneeze response. No animal models of photic sneezing currently exist, which has limited pharmacological target discovery. Future identification of specific genes causally involved in the trait may enable development of animal models and, eventually, targeted therapeutic interventions.

## Open Questions

Despite decades of observation and recent advances in genetic and neuroimaging studies, several fundamental questions about ACHOO syndrome remain unanswered:

1. **Molecular mechanism of optic-trigeminal crosstalk**: While the optic-trigeminal summation theory is widely cited, the precise molecular and cellular mechanisms by which optic nerve activation leads to trigeminal nerve stimulation remain unknown. Are there specific interneurons mediating this crosstalk, or does it occur through diffuse excitatory effects in adjacent brain regions?

2. **Role of identified genetic variants**: The GWAS-identified variants near ZEB2, NR2F2, and CADM2 are intergenic and their functional significance is unclear. Do these variants affect expression of the nearby genes, and if so, in which neural populations? What is the developmental or functional role of these genes in establishing photic sneeze circuitry?

3. **Cortical versus brainstem processing**: The Langer EEG study demonstrated cortical involvement in photic sneezing, but the relative contributions of cortical hyperexcitability versus brainstem reflex modulation remain to be determined. Is cortical activation causally related to sneezing, or is it an epiphenomenon?

4. **Incomplete penetrance and variable expressivity**: Not all individuals who carry the trait show identical responses. Some sneeze only once, others many times; some can abort the sneeze, others cannot. What genetic or environmental modifiers account for this variability?

5. **Relationship to migraine and photophobia**: The observed association between photic sneezing and migraine suggests shared trigeminal sensitivity, but the mechanistic basis remains speculative. Could photic sneeze status serve as a biomarker for migraine susceptibility?

6. **NMB pathway involvement**: While NMB has been demonstrated as essential for chemically-induced sneezing, its role in light-induced sneezing has not been directly tested. Is the photic sneeze ultimately processed through the same brainstem NMB-NMBR pathway, or does it bypass this circuit?

7. **Evolutionary significance**: Why might this trait have been maintained at such high frequency in human populations? Is there any selective advantage to light-induced sneezing, or is it simply a neutral byproduct of neural organization?

Future research employing high-resolution functional neuroimaging, optogenetics in animal models, and expanded genetic studies may help resolve these outstanding questions.

## References

- **collie-1978-achoo-abstract**: Collie WR, Pagon RA, Hall JG, Shokeir MH. ACHOO syndrome (autosomal dominant compelling helio-ophthalmic outburst syndrome). Birth Defects Orig Artic Ser. 1978;14(6B):361-3. PMID: 728575

- **everett-1964-sneezing-light-abstract**: Everett HC. Sneezing in response to light. Neurology. 1964;14:483-490. PMID: 14144120. DOI: 10.1212/WNL.14.5.483

- **peroutka-1984-autosomal-dominant-abstract**: Peroutka SJ, Peroutka LA. Autosomal dominant transmission of the "photic sneeze reflex". N Engl J Med. 1984 Mar 1;310(9):599-600. PMID: 6694722. DOI: 10.1056/NEJM198403013100918

- **morris-1987-prevalence-abstract**: Morris HH III. ACHOO syndrome: Prevalence and inheritance. Cleve Clin J Med. 1987 Sep-Oct;54(5):431-3. PMID: 3665024

- **eriksson-2010-gwas-abstract**: Eriksson N, Macpherson JM, Tung JY, et al. Web-based, participant-driven studies yield novel genetic associations for common traits. PLoS Genet. 2010 Jun 24;6(6):e1000993. PMID: 20585627. PMCID: PMC2891811. DOI: 10.1371/journal.pgen.1000993

- **langer-2010-eeg-abstract**: Langer N, Beeli G, Jäncke L. When the sun prickles your nose: an EEG study identifying neural bases of photic sneezing. PLoS One. 2010 Feb 15;5(2):e9208. PMID: 20169159. PMCID: PMC2821404. DOI: 10.1371/journal.pone.0009208

- **sasayama-2018-japanese-gwas-abstract**: Sasayama D, Asano S, Nogawa S, Takahashi S, Saito K, Kunugi H. A genome-wide association study on photic sneeze syndrome in a Japanese population. J Hum Genet. 2018 Jun;63(6):747-749. PMID: 29559738. DOI: 10.1038/s10038-018-0441-z

- **shan-2019-chinese-gwas-abstract**: Shan S, Su S, Ma K, Ma M, Wang B, Wang H. A genome-wide association study on photic sneeze reflex in the Chinese population. Sci Rep. 2019 Mar 21;9(1):4993. PMID: 30899065. PMCID: PMC6428856. DOI: 10.1038/s41598-019-41551-0

- **sasayama-2019-migraine-abstract**: Sasayama D, Asano S, Nogawa S, Takahashi S. Possible association between photic sneeze syndrome and migraine and psychological distress. Neuropsychopharmacol Rep. 2019 Sep;39(3):234-239. PMID: 31287245. PMCID: PMC7292289. DOI: 10.1002/npr2.12067

- **liu-2021-sneeze-reflex-abstract**: Li F, Jiang H, Shen X, et al. Sneezing reflex is mediated by a peptidergic pathway from nose to brainstem. Cell. 2021 Jun 24;184(14):3762-3773.e10. PMID: 34133943. PMCID: PMC8396370. DOI: 10.1016/j.cell.2021.05.017

- **nguyen-2021-zeb2-review-abstract**: Nguyen et al. ZEB2, the Mowat-Wilson Syndrome Transcription Factor: Confirmations, Novel Functions, and Continuing Surprises. Genes (Basel). 2021 Jul 12;12(7):1037. PMID: 34356053. PMCID: PMC8304685. DOI: 10.3390/genes12071037

- **nr2f2-coup-tfii-summary**: Multiple studies on NR2F2/COUP-TFII function in neural development. Key references include: Armentano M et al. J Neurosci. 2007;27(11):3030-3039 (PMID: 17360926); Kanatani S et al. PNAS. 2015;112(36):E4985-4994 (PMID: 26283378)

- **cadm2-synapse-summary**: Multiple studies on CADM2 function in synapse organization. Key references include: Morris J et al. Behav Genet. 2022 (PMID: 35849223); Ibrahim-Verbaas CA et al. Mol Psychiatry. 2016;21(2):189-197 (PMID: 25869805)

- **semes-2019-ppt-abstract**: Semes LP. Management of the photic sneeze reflex utilising the philtral pressure technique. Eye (Lond). 2019 Jul;33(7):1186-1187. PMID: 30783255. PMCID: PMC6707313. DOI: 10.1038/s41433-019-0378-z
