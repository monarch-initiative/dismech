---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-10T18:08:40.366723'
end_time: '2026-02-10T18:25:31.023583'
duration_seconds: 1010.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mucopolysaccharidosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Mucopolysaccharidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Mucopolysaccharidosis**.
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
- **Disease Name:** Mucopolysaccharidosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Mucopolysaccharidosis**.
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
- Objective 1 (completed): Define scope and subtypes of MPS and core pathophysiology themes. Result: MPS are lysosomal storage diseases caused by deficiencies in enzymes degrading glycosaminoglycans (GAGs: HS, DS, CS, KS, HA). Representative subtypes: MPS I (IDUA), II (IDS), IIIA (SGSH), IIIB (NAGLU), IVA (GALNS), VI (ARSB). Shared mechanisms include lysosomal dysfunction, autophagy impairment, organelle stress (ER/Golgi/mitochondria), oxidative stress, neuroinflammation, skeletal and cardiac involvement (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, mikołajczak2025lysosomalstoragediseases pages 1-4).
- Objective 2 (completed): Collect 2023–2024 literature on molecular/cellular mechanisms. Result: Key recent sources: Ago 2024 review (IJMS; Jan 2024) on molecular mechanisms and staged progression; Scarcella 2024 (iScience; Mar 2024) experimental data linking autophagy-lysosome and metabolic rewiring in MPS IIIB; Wiśniewska 2024 (CIMB; Mar 2024) organelle transcriptomics (ER/Golgi/mitochondria) in neuronopathic MPS; Pandey 2023 (Biomedicines; Apr 2023) neuroinflammatory mediators in LSDs with relevance to MPS (ago2024molecularmechanismsin pages 1-2, scarcella2024metabolicrewiringand pages 10-12, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10).
- Objective 3 (in progress): Summarize current applications/implementations (ERT/HSCT/gene therapy). Outcome to date: Mechanistic limitations of IV-ERT for CNS; rationale for IT/ICV delivery and receptor-mediated transport approaches; early/real-world constraints summarized (ago2024molecularmechanismsin pages 2-3).
- Objective 4 (in progress): Map genes to ontology terms (HGNC, GO/CL/UBERON/CHEBI).
- Objective 5 (in progress): Synthesize disease progression, cellular components, processes, and phenotypes with recent statistics.
- Objective 6 (completed): Create artifact summarizing subtypes, genes, substrates, cell types, organs, disrupted processes with citations.
- Objective 7: Write final comprehensive report embedding artifact.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Mucopolysaccharidosis (MPS)
- MONDO ID: MONDO_0019249 (mucopolysaccharidosis) (derived from OpenTargets search metadata)
- Category: Mendelian

1) Core Pathophysiology: Concepts, Definitions, and Current Understanding
- Definition and unifying mechanism: MPS comprise inherited lysosomal storage disorders caused by deficiency of specific lysosomal hydrolases or sulfatases required for ordered degradation of glycosaminoglycans (GAGs). Primary substrates accumulate in lysosomes as proteoglycan-derived HS, DS, CS, KS, and HA, causing multi-organ dysfunction including CNS, skeletal, and cardiac disease (ago2024molecularmechanismsin pages 2-3, ago2024molecularmechanismsin pages 1-2). “MPSs are a group of inborn errors of the metabolism caused by a deficiency in the lysosomal enzymes required to break down…glycosaminoglycans (GAGs). These GAGs accumulate over time…disrupt…autophagy, and mitochondrial function…increase oxidative stress and activate innate immunity and inflammation” (IJMS, Jan 2024; https://doi.org/10.3390/ijms25021113) (ago2024molecularmechanismsin pages 1-2).
- Staged progression: Recent synthesis highlights a sequence from reversible early storage to irreversible organ injury: “(1) disruption of substrate degradation with pathogenic changes in lysosomal function, (2) cellular dysfunction, secondary/tertiary accumulation (GM2/GM3 ganglioside, etc.), and inflammatory process, and (3) progressive tissue/organ damage and cell death (e.g., skeletal dysplasia, CNS impairment)” (IJMS, Jan 2024) (ago2024molecularmechanismsin pages 1-2). The same review emphasizes limits of current ERT/HSCT and rationale for BBB-penetrant strategies (ago2024molecularmechanismsin pages 2-3).
- Systems perspective of lysosomal dysfunction: Beyond storage, lysosomes regulate vesicle trafficking, signaling, and autophagy; their dysfunction propagates organelle stress, oxidative injury, and inflammation. MPS “perturbs intracellular trafficking and autophagy,” and GAGs can activate innate immunity with cytokine induction; mitochondrial dysfunction contributes to inflammation and ROS elevation (K. Mikołajczak 2025; overview) (mikołajczak2025lysosomalstoragediseases pages 1-4, mikołajczak2025lysosomalstoragediseases pages 10-13).

2) Molecular Pathways and Cellular Processes Affected
- Primary substrate accumulation by GAG species and subtypes: Representative mapping—MPS I (IDUA deficiency; HS/DS), MPS II (IDS deficiency; HS/DS), MPS IIIA/IIIB (SGSH/NAGLU; HS), MPS IVA (GALNS; KS±CS), MPS VI (ARSB; DS) (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, ago2024molecularmechanismsin pages 2-3).
- Secondary storage: Accumulation of gangliosides (GM2, GM3) is reported as secondary/tertiary storage during progression (IJMS, 2024) (ago2024molecularmechanismsin pages 1-2).
- Autophagy-lysosome pathway alterations: In MPS IIIB models, “metabolic rewiring and autophagy inhibition correct lysosomal storage disease,” with AMPK inhibition reducing HS storage and NK1 (HGF spliced variant) engaging PI3K/Akt, decreasing autophagy/lysosome markers (BCN1, LC3, LAMP1) (iScience, Mar 2024; https://doi.org/10.1016/j.isci.2024.108959) (scarcella2024metabolicrewiringand pages 10-12). These experiments provide mechanistic links among energy sensing (AMPK), PI3K/Akt signaling, and autophagy flux in the context of lysosomal HS storage (scarcella2024metabolicrewiringand pages 10-12).
- Mitochondrial dysfunction and metabolic shifts: Brain metabolomics in MPS IIIB indicate broad rewiring (e.g., altered lactate and glutamine), consistent with mitochondrial/energy pathway disruption (iScience, 2024) (scarcella2024metabolicrewiringand pages 10-12). Reviews emphasize mitochondrial dysfunction accompanying GAG accumulation (IJMS, 2024) (ago2024molecularmechanismsin pages 1-2) and oxidative stress in MPS (overview) (mikołajczak2025lysosomalstoragediseases pages 1-4).
- ER and Golgi stress; trafficking defects: Transcriptomics in neuronopathic MPS fibroblasts showed dysregulation of organelle-associated genes and EM evidence of structural disruptions—particularly Golgi apparatus fragmentation and ER stress markers. Up-regulated PDIA3 and MFGE8, down-regulated ARL6IP6, ABHD5, PDE4DIP, YIPF5, CLDN11; increased GM130 (GOLGA2) expression; mechanistic links to impaired ER-to-Golgi transport and Golgi fragmentation (CIMB, Mar 2024; https://doi.org/10.3390/cimb46030169) (wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10). The study notes that Golgi fragmentation “can precede neuronal cell death,” and perturbations in GRASP55/65 alter HS/CS synthesis and secretion, directly linking Golgi structure to GAG handling (wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18).
- Neuroinflammation and innate immune signaling: Reviews and cross-LSD analyses implicate microglial/astrocyte activation with upregulated cytokines/chemokines, and highlight TLR pathways and inflammasome activation in LSDs, also relevant to MPS; authors synthesize “pro-inflammatory immunological mediators” in LSD neuroinflammation (Biomedicines, Apr 2023; https://doi.org/10.3390/biomedicines11041067) (wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10). Contemporary MPS-focused reviews underscore a “profound relationship between immunity and MPS,” with complex inflammatory pathways (IJMS, 2024) (ago2024molecularmechanismsin pages 2-3).
- Synaptic and circuit dysfunction: Neuronopathic MPS subtypes (e.g., MPS III) show pronounced CNS involvement with organelle stress signatures that plausibly impact synaptic homeostasis; organelle gene changes (e.g., GOLGA2, PDIA3) and mitochondrial stress are consistent with synaptic/autophagic deficits that drive neurodegeneration, though direct synaptic electrophysiology data were not retrieved in this evidence batch (CIMB, 2024; IJMS, 2024) (wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10, ago2024molecularmechanismsin pages 1-2).
- Skeletal dysplasia mechanisms: Threshold storage in bone (notably growth plate) engages chondrocytes/osteoblasts/osteoclasts and becomes refractory to reversal once exceeded (IJMS, 2024) (ago2024molecularmechanismsin pages 2-3). Connective-tissue GAG storage (e.g., KS in MPS IVA; DS in MPS VI) disrupts ECM organization, secretion/trafficking, and growth plate architecture (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10).
- Cardiac valve/myocardial disease: Reviews capture multi-system involvement with heart valves and myocardium impacted by GAG deposition and secondary inflammatory/oxidative mechanisms (IJMS, 2024; overview 2025) (ago2024molecularmechanismsin pages 2-3, mikołajczak2025lysosomalstoragediseases pages 10-13).

3) Key Molecular Players
- Genes/Proteins (HGNC): IDUA (MPS I), IDS (MPS II), SGSH (MPS IIIA), NAGLU (MPS IIIB), GALNS (MPS IVA), ARSB (MPS VI). Additional organelle/stress markers: GOLGA2 (GM130), PDIA3, MFGE8, ARL6IP6, ABHD5, PDE4DIP, YIPF5, CLDN11; lysosome/autophagy markers LAMP1, LC3, BECN1; signaling axes AMPK, PI3K/Akt (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10, scarcella2024metabolicrewiringand pages 10-12).
- Chemical entities (metabolites/small molecules; CHEBI): Heparan sulfate (HS), dermatan sulfate (DS), chondroitin sulfate (CS), keratan sulfate (KS), hyaluronan (HA); gangliosides GM2/GM3 (secondary storage); pathway modulators used experimentally (AICAr, SBI-0206965) and NK1 protein therapy concept (iScience 2024) (ago2024molecularmechanismsin pages 1-2, scarcella2024metabolicrewiringand pages 10-12).
- Cell types (CL): Neurons, microglia (CL:0000129), astrocytes (CL:0000127), chondrocytes, osteoblasts, osteoclasts, fibroblasts (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2).
- Anatomical locations (UBERON): Brain (UBERON:0000955), spinal cord, heart/valves (UBERON:0001911), growth plate cartilage (UBERON:0002418), bone, connective tissues (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3).

4) Biological Processes (GO terms) Disrupted
- Lysosomal organization/function and autophagy: GO:0005773 (vacuole/lysosome), GO:0006914 (autophagy), GO:0016236 (macroautophagy), GO:0006629 (lipid metabolism) (ago2024molecularmechanismsin pages 1-2, scarcella2024metabolicrewiringand pages 10-12).
- Innate immune/inflammatory signaling: GO:0006954 (inflammatory response), GO:0002224 (TLR signaling) and inflammasome-related pathways (supported at review level for LSDs with MPS relevance) (wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10, ago2024molecularmechanismsin pages 2-3).
- Organelle stress and trafficking: GO:0006457 (protein folding), GO:0006888 (ER to Golgi vesicle-mediated transport), GO:0007030 (Golgi organization), GO:0007005 (mitochondrion organization) (wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10).
- ECM organization and skeletal development: GO:0030198 (extracellular matrix organization), GO:0001501 (skeletal system development) (ago2024molecularmechanismsin pages 2-3, ago2024molecularmechanismsin pages 1-2).

5) Cellular Components
- Key loci of pathology: Lysosomes (GO:0005764/0005773), autophagosomes (GO:0005776), ER (GO:0005783), Golgi (GO:0005794), mitochondria (GO:0005739), synapses (GO:0045202) (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18, scarcella2024metabolicrewiringand pages 10-12).

6) Disease Progression: Sequence of Events
- Early/reversible storage: Initial HS/DS/KS/CS/HA accumulation within lysosomes (often as proteoglycans) with cellular stress responses that may be reversible if treated early (IJMS, 2024) (ago2024molecularmechanismsin pages 1-2).
- Escalation: Lysosomal dysfunction leads to autophagy impairment, ER/Golgi stress, impaired trafficking and secretion, mitochondrial dysfunction with oxidative stress, and activation of innate immunity (microglia/astrocytes). Secondary/tertiary storage of gangliosides (GM2/GM3) emerges (IJMS, 2024; overview 2025) (ago2024molecularmechanismsin pages 1-2, mikołajczak2025lysosomalstoragediseases pages 1-4).
- Organ damage: Progressive neuronal synaptic/circuit dysfunction and neurodegeneration; growth plate and bone dysplasia becoming refractory beyond storage thresholds; heart valve/myocardial pathology; multi-organ failure (IJMS, 2024) (ago2024molecularmechanismsin pages 2-3, ago2024molecularmechanismsin pages 1-2).

7) Phenotypic Manifestations and Mechanistic Links (HPO terms suggested)
- Neurocognitive regression, behavioral disturbances, seizures (HPO:0001263, HPO:0000708): Associated with HS-driven neuroinflammation, autophagy/mitochondrial dysfunction, and organelle stress in neuronopathic MPS (IJMS 2024; CIMB 2024) (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2).
- Skeletal dysplasia (HPO:0002652), short stature (HPO:0004322), joint contractures (HPO:0001371): Linked to GAG storage in cartilage/bone, secretory and ECM disorganization, chondrocyte dysfunction, and inflammation (IJMS 2024) (ago2024molecularmechanismsin pages 2-3, ago2024molecularmechanismsin pages 1-2).
- Cardiac valvular disease (HPO:0001657), cardiomyopathy (HPO:0001638): Driven by storage/inflammation/oxidative stress in valves and myocardium (IJMS 2024; overview) (ago2024molecularmechanismsin pages 2-3, mikołajczak2025lysosomalstoragediseases pages 10-13).

8) Current Applications and Real-World Implementations (mechanistic perspective)
- Enzyme replacement therapy (ERT) and HSCT: Cross-correction concept underlies current care. However, IV ERT has limited CNS efficacy due to BBB; HSCT carries donor/GvHD risks and is timing-sensitive. New strategies (intrathecal/intracerebroventricular ERT; receptor-mediated “molecular Trojan horse” enzymes) are proposed to target CNS and bone (IJMS, Jan 2024; https://doi.org/10.3390/ijms25021113) (ago2024molecularmechanismsin pages 2-3). “Several potential treatments…that can penetrate the blood–brain barrier and bone have been proposed…including targeting peptides and molecular Trojan horses…Gene therapy trials with AAV, ex vivo LV…are proposed and/or underway” (IJMS, 2024) (ago2024molecularmechanismsin pages 1-2).
- Experimental pathway modulation: In MPS IIIB cells/brain, AMPK inhibition and PI3K/Akt activation (via NK1) reduce HS storage and normalize autophagy-lysosome markers, supporting metabolism–autophagy–lysosome crosstalk as a therapeutic lever (iScience, Mar 2024) (scarcella2024metabolicrewiringand pages 10-12).

9) Relevant Statistics and Data (recent)
- Incidence: Approximate overall MPS incidence cited as ~1 in 20,000 live births (review synthesis) (ago2024molecularmechanismsin pages 1-2).
- Quantitative molecular readouts in MPS IIIB models: AMPK inhibition reduced HS storage and lysosomal vacuolization after 24 h; brain metabolomics revealed significant changes in lactate and glutamine, among others (p/q values significant; detailed figures in iScience 2024) (scarcella2024metabolicrewiringand pages 10-12).

10) Embedded Artifact: Subtype-to-mechanism summary table
| Subtype | Causal gene (HGNC) | Enzyme name | Primary stored GAG(s) | Key affected cells (CL terms) | Key organs/tissues (UBERON terms) | Key disrupted processes (GO terms) | Selected molecular notes | Evidence (citation IDs) |
|---|---|---|---|---|---|---|---|---|
| MPS I | IDUA | alpha-L-iduronidase | Heparan sulfate (HS); Dermatan sulfate (DS) | Microglia (CL:0000129), Astrocytes (CL:0000127), Chondrocytes | Brain (UBERON:0000955); Heart (UBERON:0001911); Growth plate cartilage (UBERON:0002418) | Lysosomal vacuole (GO:0005773); Autophagy (GO:0006914); Inflammatory response (GO:0006954) | Primary HS/DS accumulation → lysosomal dysfunction, secondary substrate perturbation, neuroinflammation and skeletal damage | (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, mikołajczak2025lysosomalstoragediseases pages 1-4) |
| MPS II | IDS | iduronate 2-sulfatase | Heparan sulfate (HS); Dermatan sulfate (DS) | Microglia (CL:0000129), Astrocytes (CL:0000127), Osteoblasts/Chondrocytes | Brain (UBERON:0000955); Heart (UBERON:0001911); Growth plate cartilage (UBERON:0002418) | Lysosomal dysfunction (GO:0005773); Autophagy (GO:0006914); Inflammatory response (GO:0006954) | CNS involvement varies with residual IDS activity; systemic GAG deposition drives skeletal and cardiac pathology | (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, mikołajczak2025lysosomalstoragediseases pages 1-4) |
| MPS IIIA | SGSH | N-sulfoglucosamine sulfohydrolase | Heparan sulfate (HS) (predominantly neuronal storage) | Microglia (CL:0000129), Astrocytes (CL:0000127), Neurons | Brain (UBERON:0000955); Spinal cord | Lysosome/vacuole (GO:0005773); Autophagy (GO:0006914); Inflammatory response (GO:0006954) | Neuronopathic phenotype: HS-driven microglial activation, organelle (ER/Golgi) stress and altered organelle gene expression linked to neurodegeneration | (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10) |
| MPS IIIB | NAGLU | alpha-N-acetylglucosaminidase | Heparan sulfate (HS) | Microglia (CL:0000129), Astrocytes (CL:0000127), Neurons | Brain (UBERON:0000955); Peripheral tissues | Lysosome (GO:0005773); Autophagy (GO:0006914); Inflammatory response (GO:0006954) | Autophagy–lysosome dysregulation and metabolic rewiring (AMPK/PI3K-Akt changes) correct storage in models; metabolic/mitochondrial perturbation accompanies HS storage | (scarcella2024metabolicrewiringand pages 10-12, ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2) |
| MPS IVA | GALNS | galactosamine (N-acetyl)-6-sulfatase | Keratan sulfate (KS) ± chondroitin sulfate (CS) | Chondrocytes, Osteoblasts, Fibroblasts; (microglia/astrocytes in rare CNS cases) | Growth plate cartilage (UBERON:0002418); Bone; Heart (UBERON:0001911) | Lysosomal dysfunction (GO:0005773); ECM organization; Autophagy (GO:0006914) | Predominant skeletal/connective-tissue disease (KS accumulation); Golgi/ER trafficking and secretion disturbances affect GAG handling and matrix assembly | (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10) |
| MPS VI | ARSB | arylsulfatase B | Dermatan sulfate (DS) | Chondrocytes, Osteoclasts/Osteoblasts, Fibroblasts | Growth plate cartilage (UBERON:0002418); Heart (valves) (UBERON:0001911); Skin | Lysosomal dysfunction (GO:0005773); Autophagy (GO:0006914); Inflammatory response (GO:0006954) | Severe somatic/skeletal disease from DS storage; inflammation and oxidative stress contribute to progressive tissue damage | (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, mikołajczak2025lysosomalstoragediseases pages 1-4) |


*Table: Compact mapping of key MPS subtypes showing causal genes, enzymes, principal stored GAGs, affected cells/tissues, disrupted GO processes, brief molecular notes, and source citations; useful as an ontology-ready summary for disease knowledgebases. Evidence is drawn from the provided context (mikołajczak2025lysosomalstoragediseases pages 1-4, mikołajczak2025lysosomalstoragediseases pages 10-13).*

Gene/Protein Annotations and Ontology Mapping
- HGNC: IDUA, IDS, SGSH, NAGLU, GALNS, ARSB; organelle/stress markers: GOLGA2, PDIA3, MFGE8, ARL6IP6, ABHD5, PDE4DIP, YIPF5, CLDN11 (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10, scarcella2024metabolicrewiringand pages 10-12).
- GO Biological Processes: autophagy (GO:0006914), inflammatory response (GO:0006954), ER to Golgi transport (GO:0006888), Golgi organization (GO:0007030), mitochondrial organization (GO:0007005), ECM organization (GO:0030198) (scarcella2024metabolicrewiringand pages 10-12, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18, ago2024molecularmechanismsin pages 2-3).
- Cellular Components: lysosome/vacuole (GO:0005773), ER (GO:0005783), Golgi (GO:0005794), mitochondrion (GO:0005739), synapse (GO:0045202) (ago2024molecularmechanismsin pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18).
- Cell Types (CL): microglia (CL:0000129), astrocyte (CL:0000127), neuron, chondrocyte, osteoblast, osteoclast, fibroblast (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3, wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2).
- Anatomical (UBERON): brain (UBERON:0000955), heart (UBERON:0001911), growth plate cartilage (UBERON:0002418), bone (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3).
- Chemical Entities (CHEBI): heparan sulfate, dermatan sulfate, chondroitin sulfate, keratan sulfate, hyaluronan; GM2/GM3 gangliosides; AICAr; SBI-0206965 (ago2024molecularmechanismsin pages 1-2, scarcella2024metabolicrewiringand pages 10-12).

Expert Opinions and Analysis
- Contemporary reviews converge on an expanded view of lysosomal biology, where primary GAG storage triggers multi-organelle stress responses and maladaptive signaling, notably in autophagy-lysosome and innate immune axes. The staged progression model rationalizes why early intervention is crucial for CNS and skeletal outcomes and why bone disease is especially refractory after a threshold of growth-plate storage is exceeded (ago2024molecularmechanismsin pages 2-3, ago2024molecularmechanismsin pages 1-2). Emerging experimental data (MPS IIIB) corroborate that tuning energy sensors (AMPK) and autophagy-related signaling (PI3K/Akt) can reduce storage and normalize lysosomal/autophagic markers, suggesting tractable nodes for adjunctive therapy alongside substrate- or gene-directed approaches (scarcella2024metabolicrewiringand pages 10-12). Organelle transcriptomics and ultrastructural data tie neuronopathic phenotypes to ER/Golgi/mitochondrial derangements that likely impinge on synaptic function and neuronal viability (wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18).

Citations with URLs and Dates
- Ago Y, Rintz E, Musini KS, Ma Z, Tomatsu S. Molecular Mechanisms in Pathophysiology of Mucopolysaccharidosis and Prospects for Innovative Therapy. International Journal of Molecular Sciences. 2024 Jan;25(2):1113. URL: https://doi.org/10.3390/ijms25021113 (ago2024molecularmechanismsin pages 1-2, ago2024molecularmechanismsin pages 2-3).
- Scarcella M, et al. Metabolic rewiring and autophagy inhibition correct lysosomal storage disease in mucopolysaccharidosis IIIB. iScience. 2024 Mar;27(3):108959. URL: https://doi.org/10.1016/j.isci.2024.108959 (scarcella2024metabolicrewiringand pages 10-12).
- Wiśniewska K, et al. Cellular Organelle-Related Transcriptomic Profile Abnormalities in Neuronopathic Types of MPS. Current Issues in Molecular Biology. 2024 Mar;46:2678–2700. URL: https://doi.org/10.3390/cimb46030169 (wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2, wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18, wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10).
- Pandey MK. Exploring Pro-Inflammatory Immunological Mediators: Neuroinflammation in LSDs. Biomedicines. 2023 Apr;11(4):1067. URL: https://doi.org/10.3390/biomedicines11041067 (wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10).
- Mikołajczak K. Lysosomal storage diseases as a complex pathophysiological and clinical problem—part one. 2025 (overview). Mechanistic statements on inflammation/oxidative stress and multi-organ involvement used as supportive background (mikołajczak2025lysosomalstoragediseases pages 1-4, mikołajczak2025lysosomalstoragediseases pages 10-13).

Limitations
- Some mechanistic details (e.g., definitive roles for TLR4, inflammasome, cGAS-STING specifically in MPS brain) are supported here at the review level across LSDs and MPS-focused reviews without new 2024 primary data in this evidence batch. Direct synaptic physiology evidence and detailed cardiac histopathology from 2023–2024 primary studies were not captured in the retrieved set; claims were framed accordingly (wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10, ago2024molecularmechanismsin pages 2-3).


References

1. (ago2024molecularmechanismsin pages 1-2): Yasuhiko Ago, Estera Rintz, Krishna Sai Musini, Zhengyu Ma, and Shunji Tomatsu. Molecular mechanisms in pathophysiology of mucopolysaccharidosis and prospects for innovative therapy. International Journal of Molecular Sciences, 25:1113, Jan 2024. URL: https://doi.org/10.3390/ijms25021113, doi:10.3390/ijms25021113. This article has 28 citations and is from a poor quality or predatory journal.

2. (ago2024molecularmechanismsin pages 2-3): Yasuhiko Ago, Estera Rintz, Krishna Sai Musini, Zhengyu Ma, and Shunji Tomatsu. Molecular mechanisms in pathophysiology of mucopolysaccharidosis and prospects for innovative therapy. International Journal of Molecular Sciences, 25:1113, Jan 2024. URL: https://doi.org/10.3390/ijms25021113, doi:10.3390/ijms25021113. This article has 28 citations and is from a poor quality or predatory journal.

3. (mikołajczak2025lysosomalstoragediseases pages 1-4): K Mikołajczak. Lysosomal storage diseases as a complex pathophysiological and clinical problem-part one. Unknown journal, 2025.

4. (scarcella2024metabolicrewiringand pages 10-12): Melania Scarcella, Gianluca Scerra, Mariangela Ciampa, Marianna Caterino, Michele Costanzo, Laura Rinaldi, Antonio Feliciello, Serenella Anzilotti, Chiara Fiorentino, Maurizio Renna, Margherita Ruoppolo, Luigi Michele Pavone, Massimo D’Agostino, and Valeria De Pasquale. Metabolic rewiring and autophagy inhibition correct lysosomal storage disease in mucopolysaccharidosis iiib. iScience, 27:108959, Mar 2024. URL: https://doi.org/10.1016/j.isci.2024.108959, doi:10.1016/j.isci.2024.108959. This article has 7 citations and is from a peer-reviewed journal.

5. (wisniewska2024cellularorganellerelatedtranscriptomic pages 1-2): Karolina Wiśniewska, Lidia Gaffke, Magdalena Żabińska, Grzegorz Węgrzyn, and Karolina Pierzynowska. Cellular organelle-related transcriptomic profile abnormalities in neuronopathic types of mucopolysaccharidosis: a comparison with other neurodegenerative diseases. Current Issues in Molecular Biology, 46:2678-2700, Mar 2024. URL: https://doi.org/10.3390/cimb46030169, doi:10.3390/cimb46030169. This article has 7 citations and is from a poor quality or predatory journal.

6. (wisniewska2024cellularorganellerelatedtranscriptomic pages 7-10): Karolina Wiśniewska, Lidia Gaffke, Magdalena Żabińska, Grzegorz Węgrzyn, and Karolina Pierzynowska. Cellular organelle-related transcriptomic profile abnormalities in neuronopathic types of mucopolysaccharidosis: a comparison with other neurodegenerative diseases. Current Issues in Molecular Biology, 46:2678-2700, Mar 2024. URL: https://doi.org/10.3390/cimb46030169, doi:10.3390/cimb46030169. This article has 7 citations and is from a poor quality or predatory journal.

7. (mikołajczak2025lysosomalstoragediseases pages 10-13): K Mikołajczak. Lysosomal storage diseases as a complex pathophysiological and clinical problem-part one. Unknown journal, 2025.

8. (wisniewska2024cellularorganellerelatedtranscriptomic pages 16-18): Karolina Wiśniewska, Lidia Gaffke, Magdalena Żabińska, Grzegorz Węgrzyn, and Karolina Pierzynowska. Cellular organelle-related transcriptomic profile abnormalities in neuronopathic types of mucopolysaccharidosis: a comparison with other neurodegenerative diseases. Current Issues in Molecular Biology, 46:2678-2700, Mar 2024. URL: https://doi.org/10.3390/cimb46030169, doi:10.3390/cimb46030169. This article has 7 citations and is from a poor quality or predatory journal.