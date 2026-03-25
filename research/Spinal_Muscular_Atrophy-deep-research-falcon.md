---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-01T12:32:52.586094'
end_time: '2026-02-01T12:41:54.641457'
duration_seconds: 542.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinal Muscular Atrophy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Spinal Muscular Atrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Spinal Muscular Atrophy**.
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
- **Disease Name:** Spinal Muscular Atrophy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Spinal Muscular Atrophy**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Spinal Muscular Atrophy (5q-SMA)
- MONDO ID: [not provided]
- Category: Genetic

## Pathophysiology description (narrative)
Spinal muscular atrophy (SMA) is caused by homozygous disruption of SMN1, resulting in reduced survival motor neuron (SMN) protein and a spectrum of downstream defects that converge on selective degeneration of lower motor neurons, neuromuscular junction (NMJ) failure, and systemic, multi-organ abnormalities. SMN is a core component of the SMN–Gemins complex essential for spliceosomal snRNP assembly and mRNA splicing; it also associates with ribosomes and translation-related machinery, and regulates axonal/cytoskeletal dynamics and local translation. Recent work emphasizes additional mechanisms: autophagy–lysosome pathway dysregulation; accumulation of R-loops and DNA damage involving senataxin (SETX); innate immune activation; and non-neuronal contributions from muscle, glia, and mesenchymal progenitors. Importantly, SMN-restorative therapies improve outcomes but do not fully normalize downstream cellular biology, particularly in skeletal muscle and metabolism. (haque2024recentprogressin pages 1-2, glynn2025actincytoskeletondysregulation pages 21-24, shi2025cytoskeletondysfunctionof pages 1-3, torri2024beyondmotorneurons pages 1-2, grandi2024characterizationofsma pages 1-2)

Selected quotes supporting key concepts:
- “The underlying cause of Spinal Muscular Atrophy (SMA) is in the reduction of survival motor neuron (SMN) protein levels due to mutations in the SMN1 gene… [SMN] has crucial roles… from ribosome biogenesis to local translation and beyond.” URL: https://doi.org/10.1042/bst20231116 (Biochemical Society Transactions, Feb 2024). (haque2024recentprogressin pages 1-2)
- “In addition, low levels of senataxin (loss-of-function) in spinal muscular atrophy result in the accumulation of R-loops causing DNA damage and motor neuron degeneration.” URL: https://doi.org/10.1093/braincomms/fcae239 (Brain Communications, Jul 2024). (shi2025cytoskeletondysfunctionof pages 1-3)
- “Despite… SMN-dependent disease-modifying therapies… we observed a consistent loss of oxidative phosphorylation (OXPHOS) machinery of the mitochondria… and a correlation between… denervation and increased fibrosis” in treated SMA type II muscle. URL: https://doi.org/10.1172/jci.insight.180992 (JCI Insight, Sep 2024). (grandi2024characterizationofsma pages 1-2)

## 1. Core Pathophysiology
- Primary mechanisms
  - SMN1 loss → reduced SMN protein → defective snRNP biogenesis and splicing, ribosome/translation control, axonal transport and cytoskeleton, and NMJ function. (haque2024recentprogressin pages 1-2, glynn2025actincytoskeletondysregulation pages 21-24, shi2025cytoskeletondysfunctionof pages 1-3, torri2024beyondmotorneurons pages 1-2)
  - Autophagy–lysosome pathway defects: reduced lysosome number/flux and TFEB/lysosomal signaling perturbation in SMA motor neurons and cells; emerging consensus implicates decreased autophagic flux. (rosignol2024understandinghowsmn pages 1-4, torres2025dissectingtherolea pages 28-32)
  - Genome instability axis: R-loop accumulation and DNA damage; SETX interacts with SMN and reduced SETX in SMA increases R-loops leading to neuronal injury. (shi2025cytoskeletondysfunctionof pages 1-3)
  - Innate immune activation: transcriptomic/proteomic studies in Drosophila SMA models show hyperactivation of IMD/Toll pathways and antimicrobial peptides, implying primary immune dysregulation from SMN loss. (chudakova2024insearchof pages 3-5)
  - Mitochondrial/OXPHOS and metabolic abnormalities: persistent skeletal muscle OXPHOS deficiency and mtDNA depletion despite therapy; denervation/fibrosis programs. (grandi2024characterizationofsma pages 1-2)

- Dysregulated molecular pathways
  - Spliceosome/snRNP assembly; translation initiation/elongation; actin–microtubule dynamics (profilin, plastin-3, stathmin-1, MAP1B); endocytosis and vesicle trafficking at synapses; autophagy–lysosome (TFEB–mTOR); DNA damage response/R-loop resolution (SETX); innate immunity (IMD/Toll-like signaling). (haque2024recentprogressin pages 1-2, glynn2025actincytoskeletondysregulation pages 21-24, shi2025cytoskeletondysfunctionof pages 1-3, rosignol2024understandinghowsmn pages 1-4, chudakova2024insearchof pages 3-5)

- Affected cellular processes
  - Axon growth and stability; local mRNA transport/translation; synaptic vesicle dynamics; lysosome biogenesis and autophagic flux; DNA damage repair; mitochondrial respiration and biogenesis; glia–neuron cross-talk and immune signaling. (shi2025cytoskeletondysfunctionof pages 1-3, rosignol2024understandinghowsmn pages 1-4, chudakova2024insearchof pages 3-5, grandi2024characterizationofsma pages 1-2)

## 2. Key Molecular Players
- Genes/Proteins (HGNC)
  - SMN1 (HGNC:11164) and SMN2 (HGNC:11165) – causal locus and disease modifier. (haque2024recentprogressin pages 1-2, torri2024beyondmotorneurons pages 1-2)
  - SETX (HGNC:10759; senataxin) – R-loop resolution; reduced levels in SMA promote DNA damage. (shi2025cytoskeletondysfunctionof pages 1-3)
  - PFN2 (HGNC:8882), PLS3 (HGNC:9071), STMN1 (HGNC:6510) and STMN2 (HGNC:6511), MAP1B (HGNC:6830), NEFL/NEFM (neurofilaments) – cytoskeletal/axonal transport regulators; STMN2 augmentation shows therapeutic benefit in SMA models. (shi2025cytoskeletondysfunctionof pages 1-3)
  - NRXN2 (HGNC:8007), SYNCRIP (HGNC:16642) – motor neuron transcript regulation downstream of SMN. (torri2024beyondmotorneurons pages 1-2)
  - UBA1 (HGNC:12485) – ubiquitination pathway decreased with SMN loss, impacting proteostasis in muscle. (glynn2025actincytoskeletondysregulation pages 21-24)

- Chemical entities (CHEBI; therapeutics/metabolites)
  - Nusinersen (antisense oligonucleotide; Spinraza) – SMN2 splicing modifier. (torri2024beyondmotorneurons pages 1-2)
  - Risdiplam (Evrysdi; CHEBI:145709) – oral SMN2 splicing modifier. (torri2024beyondmotorneurons pages 1-2)
  - Onasemnogene abeparvovec (AAV9-SMN1 gene therapy, Zolgensma) – SMN1 replacement. (torri2024beyondmotorneurons pages 1-2)
  - Prednisolone (CHEBI:8383) – concomitant steroid with OA infusion in practice. (lavie2024respiratoryoutcomesof pages 1-2)

- Cell types (CL)
  - Spinal alpha motor neurons (CL:0000097 motor neuron) – primary vulnerable population. (torres2025dissectingtherolea pages 28-32)
  - Astrocytes (CL:0000127), microglia (CL:0000129), oligodendrocytes (CL:0000128), Schwann cells (CL:0000574) – non-cell autonomous contributors. (torri2024beyondmotorneurons pages 1-2)
  - Skeletal muscle fibers and fibro-adipogenic progenitors – muscle-intrinsic pathology and NMJ maturation support. (grandi2024characterizationofsma pages 1-2)

- Anatomical locations (UBERON)
  - Spinal cord, ventral horn (lower motor neurons); peripheral motor axons; neuromuscular junctions; skeletal muscle (including diaphragm); liver and other peripheral organs implicated in systemic SMA. (torri2024beyondmotorneurons pages 1-2, grandi2024characterizationofsma pages 1-2)

## 3. Biological Processes (GO annotations; illustrative)
- mRNA splicing via spliceosome (GO:0000398) and spliceosomal snRNP assembly (GO:0000387). (haque2024recentprogressin pages 1-2)
- Translation (GO:0006412) and ribosome biogenesis (GO:0042254). (haque2024recentprogressin pages 1-2)
- Axonal transport (GO:0098930) and microtubule cytoskeleton organization (GO:0000226). (shi2025cytoskeletondysfunctionof pages 1-3)
- Autophagy (GO:0006914), lysosome organization (GO:0007040), TFEB signaling/mTOR regulation of autophagy (process-level concept). (rosignol2024understandinghowsmn pages 1-4)
- DNA repair (GO:0006281), response to DNA damage stimulus (GO:0006974), R-loop resolution (process-level concept). (shi2025cytoskeletondysfunctionof pages 1-3)
- Innate immune response (GO:0045087). (chudakova2024insearchof pages 3-5)
- Mitochondrial electron transport chain/oxidative phosphorylation (GO:0022900/GO:0006119). (grandi2024characterizationofsma pages 1-2)

## 4. Cellular Components (GO-CC)
- Nucleus; Cajal/Gem bodies; ribosome; cytoplasm; axon; growth cone; synapse/NMJ; stress granules; lysosome; mitochondrion. (haque2024recentprogressin pages 1-2, shi2025cytoskeletondysfunctionof pages 1-3, rosignol2024understandinghowsmn pages 1-4)

## 5. Disease Progression (sequence of events)
- Genetic lesion: SMN1 homozygous deletion/mutation → reduced full-length SMN; SMN2 modulates residual SMN. (torri2024beyondmotorneurons pages 1-2, haque2024recentprogressin pages 1-2)
- Nuclear and cytoplasmic defects: snRNP assembly/splicing defects; altered translation; impaired RNA transport/local translation in axons. (haque2024recentprogressin pages 1-2)
- Axonal/cytoskeletal dysfunction: disrupted actin–microtubule dynamics (PFN2/PLS3/STMN1/MAP1B), impaired axonal transport and growth cones. (shi2025cytoskeletondysfunctionof pages 1-3)
- Synaptic/NMJ abnormalities: early denervation, neurofilament accumulation, impaired vesicle dynamics, AChR clustering defects. (torres2025dissectingtherolea pages 28-32)
- Quality control and genome stability: reduced autophagic flux/lysosomal alterations; R-loop accumulation and DNA damage with SETX deficiency. (rosignol2024understandinghowsmn pages 1-4, shi2025cytoskeletondysfunctionof pages 1-3)
- Systemic and non-neuronal involvement: muscle-intrinsic mitochondrial OXPHOS deficit and fibrosis despite therapy; contributions from glia and mesenchymal progenitors altering NMJ maturation. (grandi2024characterizationofsma pages 1-2)
- Clinical manifestations: hypotonia, proximal weakness, respiratory insufficiency, feeding/bulbar dysfunction, fatigability; severity stratified by SMN2 copy number and age of onset. (torri2024beyondmotorneurons pages 1-2)

## 6. Phenotypic Manifestations (HPO; illustrative mapping)
- Hypotonia (HP:0001252); Proximal muscle weakness (HP:0003701); Areflexia (HP:0001284); Respiratory failure/insufficiency (HP:0002093); Feeding difficulties (HP:0011968); Fatigability (HP:0012378). (torri2024beyondmotorneurons pages 1-2)

## Current applications and real-world implementations
- Approved SMN-targeted therapies: nusinersen (ASO), risdiplam (small molecule), and onasemnogene abeparvovec (AAV9 gene replacement) have transformed outcomes; earlier treatment (including newborn screening) yields better motor function. (torri2024beyondmotorneurons pages 1-2)
- Real-world registry outcomes (RESTORE): 168 patients treated with onasemnogene abeparvovec monotherapy (data cutoff May 23, 2022). “All patients maintained/achieved motor milestones.” Adverse events: “48.5% (n=81/167) experienced at least one treatment-emergent adverse event (AE), and 31/167 patients (18.6%) experienced at least one serious AE, of which 8/31 were considered treatment-related.” Infants identified by newborn screening had higher final CHOP INTEND scores than clinically diagnosed infants. URL: https://doi.org/10.3233/jnd-230122 (Journal of Neuromuscular Diseases, Jan 2024). (servais2024realworldoutcomesin pages 1-3)
- Respiratory outcomes after OA: National real-world cohort of 25 children (23 SMA1, 2 SMA2), median age at OA 6.1 months; ventilation time decreased (14.3→11.1 h/day) and respiratory hospitalizations decreased by 26% in the post-treatment year; two deaths due to respiratory failure; authors conclude OA may improve respiratory outcomes but emphasize confounders and need for standardized long-term management. URL: https://doi.org/10.1007/s00431-024-05886-9 (European Journal of Pediatrics, Dec 2024). (lavie2024respiratoryoutcomesof pages 1-2)
- 2024 European consensus update on gene therapy: updated guidance on rational use of onasemnogene abeparvovec, including considerations for older/heavier patients and integration with trial and real-world evidence; see EJPN consensus and supplementary material. URL: https://doi.org/10.1016/j.ejpn.2024.06.001 (European Journal of Paediatric Neurology, Jun 2024). (kirschner20242024updateeuropean pages 6-6)

## Expert opinions and analysis
- Reviews synthesize that SMN’s canonical (snRNP) and noncanonical (translation, cytoskeleton, trafficking) roles explain selective motor neuron vulnerability and widespread tissue involvement; combination therapies targeting cytoskeletal stability, NMJ integrity, autophagy–lysosome pathways, and genome stability (R-loops) are being explored to complement SMN restoration. (haque2024recentprogressin pages 1-2, shi2025cytoskeletondysfunctionof pages 1-3, torri2024beyondmotorneurons pages 1-2)
- Autophagy: “decreased autophagic flux as the causative agent underlying the autophagic dysregulation observed” in SMA suggests TFEB–lysosomal axes as therapeutic targets. URL: https://doi.org/10.3389/fncel.2023.1307636 (Frontiers in Cellular Neuroscience, Jan 2024). (rosignol2024understandinghowsmn pages 1-4)
- Innate immunity: SMN depletion can “hyperactivate” conserved immune pathways (IMD/Toll), indicating immune dysregulation is a primary consequence of low SMN, not merely secondary to degeneration. URL: https://doi.org/10.1186/s12915-024-01888-z (BMC Biology, Apr 2024). (chudakova2024insearchof pages 3-5)

## Relevant statistics and data from recent studies
- RESTORE registry OA monotherapy (n=168): 47.6% two SMN2 copies; 41.7% three copies; 58.3% identified by newborn screening. All achieved/maintained milestones; TEAEs in 48.5%, SAEs in 18.6% with 8 treatment-related. URL: https://doi.org/10.3233/jnd-230122 (published 2024-01-18 online). (servais2024realworldoutcomesin pages 1-3)
- Respiratory real-world cohort after OA (n=25): 26% reduction in respiratory hospitalizations per life-year; ventilation time decreased by 3.2 h/day among survivors; 2/25 deaths from respiratory failure within study year. URL: https://doi.org/10.1007/s00431-024-05886-9 (published 2024-12). (lavie2024respiratoryoutcomesof pages 1-2)
- Treated SMA type II muscle: consistent OXPHOS loss and mtDNA copy number decrease despite restored SMN transcripts/protein in many patients. URL: https://doi.org/10.1172/jci.insight.180992 (published 2024-09-12). (grandi2024characterizationofsma pages 1-2)

## Evidence items (with direct quotes, PMIDs/DOIs/URLs where available)
1) SMN roles across translation and ribosomes: “Given the crucial roles of the SMN protein in snRNP biogenesis and its interactions with ribosomes… a decrease in SMN levels… is expected to affect translational control of gene expression.” DOI: 10.1042/bst20231116; URL: https://doi.org/10.1042/bst20231116 (Sharma et al., 2024). (haque2024recentprogressin pages 1-2)
2) R-loops and SETX in SMA: “low levels of senataxin… in spinal muscular atrophy result in the accumulation of R-loops causing DNA damage and motor neuron degeneration.” DOI: 10.1093/braincomms/fcae239; URL: https://doi.org/10.1093/braincomms/fcae239 (Kannan et al., 2024). (shi2025cytoskeletondysfunctionof pages 1-3)
3) Autophagy–lysosome: “propose decreased autophagic flux as the causative agent underlying the autophagic dysregulation observed in these patients.” DOI: 10.3389/fncel.2023.1307636; URL: https://doi.org/10.3389/fncel.2023.1307636 (Rashid & Dimitriadi, 2024). (rosignol2024understandinghowsmn pages 1-4)
4) Muscle OXPHOS deficiency despite SMN-restoration: “we observed a consistent loss of oxidative phosphorylation (OXPHOS) machinery of the mitochondria, a decrease in mitochondrial DNA copy number… [and] increased fibrosis” in treated Type II muscle. DOI: 10.1172/jci.insight.180992; URL: https://doi.org/10.1172/jci.insight.180992 (Grandi et al., 2024). (grandi2024characterizationofsma pages 1-2)
5) Real-world OA outcomes (RESTORE): “All patients maintained/achieved motor milestones. 48.5%… experienced at least one treatment-emergent adverse event… 18.6% experienced at least one serious AE…” DOI: 10.3233/jnd-230122; URL: https://doi.org/10.3233/jnd-230122 (Servais et al., 2024). (servais2024realworldoutcomesin pages 1-3)
6) Real-world respiratory impact after OA: “Ventilation time decreased from 14.3 to 11.1 hours per day, and respiratory hospitalizations decreased by 26%” in the year after treatment. DOI: 10.1007/s00431-024-05886-9; URL: https://doi.org/10.1007/s00431-024-05886-9 (Lavie et al., 2024). (lavie2024respiratoryoutcomesof pages 1-2)
7) Consensus guidance: 2024 European consensus update on the rational use of OA, including older/heavier patients and integration of real-world evidence; see main text and Supplementary Data. DOI: 10.1016/j.ejpn.2024.06.001; URL: https://doi.org/10.1016/j.ejpn.2024.06.001 (Kirschner et al., 2024). (kirschner20242024updateeuropean pages 6-6)

## Gene/Protein annotations (HGNC) with ontology mapping
- SMN1 (HGNC:11164): mRNA splicing via spliceosome (GO:0000398); spliceosomal snRNP assembly (GO:0000387); ribosome/translation (GO:0006412); axon (GO:0030424); Cajal/Gem bodies; cytoskeleton organization (GO:0000226). Evidence: reviews and mechanistic synthesis. (haque2024recentprogressin pages 1-2)
- SMN2 (HGNC:11165): genetic modifier of SMN dosage; target of splicing therapies. (torri2024beyondmotorneurons pages 1-2)
- SETX (HGNC:10759): R-loop resolution/DNA damage response (GO:0006281; concept-level for R-loops). Evidence: Brain Communications 2024. (shi2025cytoskeletondysfunctionof pages 1-3)
- PFN2 (HGNC:8882), PLS3 (HGNC:9071), STMN1/2 (HGNC:6510/6511), MAP1B (HGNC:6830): cytoskeletal dynamics/axon growth (GO:0098930; GO:0000226). Evidence: Journal of Neurology 2025; therapeutic STMN2 augmentation. (shi2025cytoskeletondysfunctionof pages 1-3)
- UBA1 (HGNC:12485): ubiquitination/proteostasis; muscle pathology in SMA. (glynn2025actincytoskeletondysregulation pages 21-24)

## Cell type involvement (CL terms)
- Motor neuron (CL:0000100; spinal alpha motor neuron): degeneration and axonal vulnerability. (torres2025dissectingtherolea pages 28-32)
- Astrocyte (CL:0000127), microglia (CL:0000129), oligodendrocyte (CL:0000128), Schwann cell (CL:0000574): non-neuronal contributions to NMJ/axon pathology and neuroinflammation. (torri2024beyondmotorneurons pages 1-2)
- Skeletal muscle fiber and fibro-adipogenic progenitors: intrinsic OXPHOS and maturation defects; NMJ abnormalities. (grandi2024characterizationofsma pages 1-2)

## Anatomical locations (UBERON)
- Spinal cord (ventral horn), peripheral motor axon, neuromuscular junction, skeletal muscle (including diaphragm), liver/other peripheral tissues (multisystem involvement). (torri2024beyondmotorneurons pages 1-2, grandi2024characterizationofsma pages 1-2)

## Chemical entities (CHEBI)
- Nusinersen (ASO), risdiplam (CHEBI:145709), onasemnogene abeparvovec (AAV9-based gene therapy), prednisolone (CHEBI:8383). (torri2024beyondmotorneurons pages 1-2, lavie2024respiratoryoutcomesof pages 1-2)

## Recent developments (2023–2024 emphasis)
- Mechanistic advances: R-loop/SETX axis in SMA-linked DNA damage (2024); autophagy–lysosome/TFEB dysregulation and reduced autophagic flux as a primary mechanism (2024); persistent muscle OXPHOS impairment and fibrosis post-therapy (2024). (shi2025cytoskeletondysfunctionof pages 1-3, rosignol2024understandinghowsmn pages 1-4, grandi2024characterizationofsma pages 1-2)
- Therapeutic guidance and outcomes: 2024 European consensus on AAV9 gene therapy implementation; real-world registry evidence from RESTORE; respiratory cohort outcomes after OA. (kirschner20242024updateeuropean pages 6-6, servais2024realworldoutcomesin pages 1-3, lavie2024respiratoryoutcomesof pages 1-2)

## References (with URLs and publication dates)
- Sharma G et al. The SMN–ribosome interplay… Biochemical Society Transactions. 2024 Feb. URL: https://doi.org/10.1042/bst20231116 (mechanistic review). (haque2024recentprogressin pages 1-2)
- Torri F et al. Beyond Motor Neurons… IJMS. 2024 Jul 3. URL: https://doi.org/10.3390/ijms25137311 (NMJ-focused review). (torri2024beyondmotorneurons pages 1-2)
- Rashid S, Dimitriadi M. Autophagy in SMA… Front Cell Neurosci. 2024 Jan. URL: https://doi.org/10.3389/fncel.2023.1307636 (autophagy review). (rosignol2024understandinghowsmn pages 1-4)
- Kannan A et al. Role of senataxin… Brain Commun. 2024 Jul. URL: https://doi.org/10.1093/braincomms/fcae239 (R-loop/SMA link). (shi2025cytoskeletondysfunctionof pages 1-3)
- Grandi FC et al. Characterization of SMA type II muscle… JCI Insight. 2024 Sep 12. URL: https://doi.org/10.1172/jci.insight.180992 (treated muscle OXPHOS). (grandi2024characterizationofsma pages 1-2)
- Servais L et al. Real-World Outcomes… RESTORE Registry. J Neuromuscul Dis. 2024 Jan 5 (Epub 2024-01-18). URL: https://doi.org/10.3233/jnd-230122 (OA outcomes). (servais2024realworldoutcomesin pages 1-3)
- Lavie M et al. Respiratory outcomes after OA… Eur J Pediatr. 2024 Dec. URL: https://doi.org/10.1007/s00431-024-05886-9 (respiratory cohort). (lavie2024respiratoryoutcomesof pages 1-2)
- Kirschner J et al. 2024 update: European consensus statement on gene therapy for SMA. EJPN. 2024 Jun. URL: https://doi.org/10.1016/j.ejpn.2024.06.001 (consensus). (kirschner20242024updateeuropean pages 6-6)

## Notes on limitations and open questions
- While SMN restoration improves outcomes, residual deficits (e.g., mitochondrial OXPHOS in muscle) suggest a need for adjunct, SMN-independent approaches (e.g., cytoskeletal stabilization, autophagy–lysosome and mitochondrial support, genome stability/R-loop targeting). (grandi2024characterizationofsma pages 1-2, shi2025cytoskeletondysfunctionof pages 1-3, rosignol2024understandinghowsmn pages 1-4)
- The precise determinants of selective alpha-motor neuron vulnerability remain under study, including differential axonal demands, cytoskeletal dependencies, and local translation control. (shi2025cytoskeletondysfunctionof pages 1-3)


References

1. (haque2024recentprogressin pages 1-2): Umme Sabrina Haque and Toshifumi Yokota. Recent progress in gene-targeting therapies for spinal muscular atrophy: promises and challenges. Genes, Jul 2024. URL: https://doi.org/10.3390/genes15080999, doi:10.3390/genes15080999. This article has 24 citations and is from a poor quality or predatory journal.

2. (glynn2025actincytoskeletondysregulation pages 21-24): A Glynn. Actin cytoskeleton dysregulation in peripheral organs in spinal muscular atrophy (sma). Unknown journal, 2025.

3. (shi2025cytoskeletondysfunctionof pages 1-3): Tianyu Shi, Zijie Zhou, Taiyang Xiang, Yinxuan Suo, Xiaoyan Shi, Yaoyao Li, Peng Zhang, Jun Dai, and Lei Sheng. Cytoskeleton dysfunction of motor neuron in spinal muscular atrophy. Journal of Neurology, Dec 2025. URL: https://doi.org/10.1007/s00415-024-12724-3, doi:10.1007/s00415-024-12724-3. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (torri2024beyondmotorneurons pages 1-2): Francesca Torri, Michelangelo Mancuso, Gabriele Siciliano, and Giulia Ricci. Beyond motor neurons in spinal muscular atrophy: a focus on neuromuscular junction. International Journal of Molecular Sciences, 25:7311, Jul 2024. URL: https://doi.org/10.3390/ijms25137311, doi:10.3390/ijms25137311. This article has 8 citations and is from a poor quality or predatory journal.

5. (grandi2024characterizationofsma pages 1-2): Fiorella Carla Grandi, Stéphanie Astord, Sonia Pezet, Elèna Gidaja, Sabrina Mazzucchi, Maud Chapart, Stéphane Vasseur, Kamel Mamchaoui, and Piera Smeriglio. Characterization of sma type ii skeletal muscle from treated patients shows oxphos deficiency and denervation. JCI Insight, Sep 2024. URL: https://doi.org/10.1172/jci.insight.180992, doi:10.1172/jci.insight.180992. This article has 8 citations and is from a domain leading peer-reviewed journal.

6. (rosignol2024understandinghowsmn pages 1-4): PDI Rosignol. Understanding how smn protein regulates the autophagy-lysosome pathway in spinal muscular atrophy. Unknown journal, 2024.

7. (torres2025dissectingtherolea pages 28-32): P Pacheco Torres. Dissecting the role of oxidative stress in spinal muscular atrophy (sma). Unknown journal, 2025.

8. (chudakova2024insearchof pages 3-5): Daria Chudakova, Ludmila Kuzenkova, Andrey Fisenko, and Kirill Savostyanov. In search of spinal muscular atrophy disease modifiers. International Journal of Molecular Sciences, 25:11210, Oct 2024. URL: https://doi.org/10.3390/ijms252011210, doi:10.3390/ijms252011210. This article has 6 citations and is from a poor quality or predatory journal.

9. (lavie2024respiratoryoutcomesof pages 1-2): Moran Lavie, Mika Rochman, Keren Armoni Domany, Inbal Golan Tripto, Moria Be’er, Omri Besor, Liora Sagi, Sharon Aharoni, Mira Ginsberg, Iris Noyman, and Hagit Levine. Respiratory outcomes of onasemnogene abeparvovec treatment for spinal muscular atrophy: national real-world cohort study. European Journal of Pediatrics, Dec 2024. URL: https://doi.org/10.1007/s00431-024-05886-9, doi:10.1007/s00431-024-05886-9. This article has 5 citations and is from a peer-reviewed journal.

10. (servais2024realworldoutcomesin pages 1-3): Laurent Servais, John W. Day, Darryl C. De Vivo, Janbernd Kirschner, Eugenio Mercuri, Francesco Muntoni, Crystal M. Proud, Perry B. Shieh, Eduardo F. Tizzano, Susana Quijano-Roy, Isabelle Desguerre, Kayoko Saito, Eric Faulkner, Kamal M. Benguerba, Dheeraj Raju, Nicole LaMarca, Rui Sun, Frederick A. Anderson, and Richard S. Finkel. Real-world outcomes in patients with spinal muscular atrophy treated with onasemnogene abeparvovec monotherapy: findings from the restore registry. Journal of Neuromuscular Diseases, 11:425-442, Jan 2024. URL: https://doi.org/10.3233/jnd-230122, doi:10.3233/jnd-230122. This article has 58 citations and is from a peer-reviewed journal.

11. (kirschner20242024updateeuropean pages 6-6): Janbernd Kirschner, Günther Bernert, Nina Butoianu, Liesbeth De Waele, Aviva Fattal-Valevski, Jana Haberlova, Teresa Moreno, Andrea Katharina Klein, Anna Kostera-Pruszczyk, Eugenio Mercuri, Susana Quijano-Roy, Thomas Sejersen, Eduardo F Tizzano, W Ludo van der Pol, Sean Wallace, Dimitrios Zafeiriou, Andreas Ziegler, Francesco Muntoni, and Laurent Servais. 2024 update: european consensus statement on gene therapy for spinal muscular atrophy. European journal of paediatric neurology : EJPN : official journal of the European Paediatric Neurology Society, 51:73-78, Jun 2024. URL: https://doi.org/10.1016/j.ejpn.2024.06.001, doi:10.1016/j.ejpn.2024.06.001. This article has 28 citations.