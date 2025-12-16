---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:22.671493'
end_time: '2025-12-15T09:20:54.966472'
duration_seconds: 452.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hirschsprung Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hirschsprung Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hirschsprung Disease**.
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
- **Disease Name:** Hirschsprung Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hirschsprung Disease**.
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
- Disease Name: Hirschsprung Disease (HSCR)
- MONDO ID: MONDO:0005790
- Category: Genetic (neurocristopathy)

Pathophysiology description
Hirschsprung disease is a congenital enteric neuropathy caused by failure of enteric neural crest–derived progenitors to migrate, proliferate, survive, and differentiate to form the enteric nervous system (ENS) along variable lengths of distal gut, resulting in aganglionosis and functional obstruction ("HSCR is a congenital enteric neuropathy in which the enteric nervous system (ENS) fails to develop along variable lengths of the distal gastrointestinal tract," and GDNF is "mitogenic, neurotrophic, and chemoattractive" for ENS precursors) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7, burns2024causesandconsequences pages 7-8). Developmental control of ENS progenitors critically depends on RET/GDNF and EDN3/EDNRB signaling, which maintain precursor proliferation, chemoattraction, and lineage allocation; deficiency of these pathways reduces neural crest progenitor number and fate potential and produces Hirschsprung-like phenotypes in model systems (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7, burns2024causesandconsequences pages 7-8). Beyond embryogenesis, recent data suggest postnatal ischemic stress can aggravate enteric neuronal loss via mitochondrial injury and caspase-dependent apoptosis, linking tissue ischemia to hypertrophic nerve trunk formation and ongoing neuropathology (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).

Core pathophysiology
- Primary mechanisms
  - Disrupted cranio-caudal colonization of gut by enteric neural crest cells due to failure of migration, proliferation, survival, or differentiation, producing distal aganglionosis and obstruction (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).
  - RET/GDNF axis: GDNF provides chemoattraction and trophic support, RET loss diminishes neural crest progenitor proliferation and fate potential; “GDNF availability determines enteric neuron number by controlling precursor proliferation” (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
  - EDN3/EDNRB axis: endothelin signaling is essential for ENS development; in Ednrb−/− mice, Hirschsprung phenotypes and selective neuronal lineage deficits occur (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (burns2024causesandconsequences pages 7-8, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
  - Complex polygenic architecture and epistasis within RET regulatory elements modulate risk and penetrance (Nov 2022; https://doi.org/10.1038/s41598-022-24077-w) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Dysregulated molecular pathways
  - Neurotrophic signaling (GDNF/RET, NRTN/RET) and endothelin (EDN3/EDNRB) signaling (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
  - Ischemia–NO–mitochondria–caspase axis in postnatal/complicating pathology, with NO donors preventing ischemia-induced ENC death (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).
  - Network-level inflammatory, vascular-permeability, and epithelial ion-transport alterations implicated in HAEC (Jan 2024; https://doi.org/10.3390/biom14020164; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (lucenapadros2024bioinformaticspredictionfor pages 27-28, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Affected cellular processes
  - Neural crest cell chemotaxis, proliferation, lineage specification and synaptic connectivity (e.g., altered nitrergic balance and interstitial cells of Cajal involvement in postoperative dysfunction) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
  - Mucosal barrier and immune functions predisposing to enterocolitis (Jun 2022; https://doi.org/10.1055/s-0042-1745780) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).

Key molecular players
- Genes/Proteins (HGNC):
  - RET (HGNC:9967): receptor tyrosine kinase for GDNF family ligands; coding and noncoding variants confer major HSCR risk; epistatic enhancer interactions within the RET TAD modulate susceptibility (Nov 2022; https://doi.org/10.1038/s41598-022-24077-w; Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7, burns2024causesandconsequences pages 6-7).
  - GDNF (HGNC:4231) and NRTN (HGNC:7995): neurotrophic ligands guiding chemotaxis and supporting proliferation/survival; reduced availability lowers enteric neuron number (“GDNF availability determines enteric neuron number…”) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
  - EDNRB (HGNC:3189) and EDN3 (HGNC:3175): endothelin signaling required for ENS progenitor expansion/differentiation; EDNRB loss yields colonic aganglionosis and enterocolitis in models (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (burns2024causesandconsequences pages 7-8, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
  - SOX10 (HGNC:11195), PHOX2B (HGNC:9140), NRG1 (HGNC:7997), ZEB2 (HGNC:11776): core ENS regulatory genes implicated by human genetics and GRNs; RET–EDNRB epistasis is explained by shared transcriptional control (“A gene regulatory network explains RET-EDNRB epistasis…”) (Jul 2019; https://doi.org/10.1093/hmg/ddz149; Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7, burns2024causesandconsequences pages 6-7).
  - NCAM1 (HGNC:7659): adhesion receptor whose signaling is required for GDNF-based therapeutic responses in experimental HSCR (May 2025 preprint; https://doi.org/10.1101/2025.05.23.655388) (gary2025successofgdnfbased pages 25-34).
- Chemical entities (CHEBI) and modulators:
  - Nitric oxide donors (e.g., sodium nitroprusside; CHEBI:9306) attenuate ischemia-induced enteric neuron death via mitophagy induction (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).
- Cell types (CL):
  - Enteric neural crest–derived progenitors/ENCDCs (CL:0002563, progenitor-like): primary cells affected in colonization failure (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).
  - Enteric neurons (CL:1001608) and enteric glia (CL:0002573): neuronal subtype imbalance (e.g., nitrergic) and glial alterations linked to dysfunction and HAEC (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (burns2024causesandconsequences pages 7-8, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
  - Fibroblasts (CL:0000057): ischemia-associated CLDN1+ fibroblast wrapping of hypertrophic nerve trunks (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).
- Anatomical locations (UBERON):
  - Distal colon/rectosigmoid (UBERON:0001155/0001052) as the most commonly aganglionic segment; myenteric and submucosal plexuses (UBERON:8410064/0001271) are absent in affected bowel (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).

Biological processes for GO annotation
- ENS development and NCC biology: neural crest cell migration (GO:0014032), cell proliferation (GO:0008283), neuronal differentiation (GO:0030182), axon guidance/synaptogenesis (GO:0007411/GO:0007416); GDNF–RET signaling (GO:0048011) and endothelin signaling (GO:0007193) underpin these processes (“GDNF is a chemoattractant…”; “Interaction of endothelin-3 with endothelin-B receptor is essential…”) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7, burns2024causesandconsequences pages 7-8).
- Inflammatory and vascular responses relevant to HAEC: regulation of vascular permeability (GO:0043114), epithelial barrier maintenance (GO:0030277), immune response (GO:0006955), and NF-κB signaling/inflammatory transcriptional programs (surveyed in 2024 biomolecular network review of HSCR/HAEC) (Jan 2024; https://doi.org/10.3390/biom14020164) (lucenapadros2024bioinformaticspredictionfor pages 27-28).
- Mitochondrial stress and apoptosis under ischemia: response to hypoxia (GO:0001666), mitochondrial membrane organization (GO:0007005), mitophagy (GO:0000422), and activation of cysteine-type endopeptidase activity involved in apoptotic process (GO:0006919) (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).

Cellular components
- Plasma membrane receptor complexes for RET and EDNRB signaling (GO:0005886; GO:0004930), growth cone/axon compartments during ENS wiring (GO:0030426), myenteric and submucosal plexus ganglia (UBERON:8410064/0001271), epithelial tight junctions pertinent to HAEC pathobiology (GO:0005923) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Jan 2024; https://doi.org/10.3390/biom14020164) (burns2024causesandconsequences pages 6-7, lucenapadros2024bioinformaticspredictionfor pages 27-28).

Disease progression (sequence of events)
- Embryonic initiation: reduced RET/EDNRB pathway dosage, plus polygenic modifiers, lower the pool and motility of ENCDCs at the wavefront (Nov 2022; https://doi.org/10.1038/s41598-022-24077-w; Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7, burns2024causesandconsequences pages 6-7).
- Migration failure: incomplete caudal colonization leaves a distal aganglionic segment lacking myenteric and submucosal ganglia (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).
- Neonatal presentation: functional obstruction with megacolon; surgery removes aganglionic bowel but residual dysmotility can persist due to neuronal subtype imbalance and pan-enteric abnormalities (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
- Complications: HAEC arises from converging dysmotility, barrier dysfunction, immune dysregulation, and dysbiosis; postoperative vascular permeability and inflammatory pathways can heighten risk (Jan 2024; https://doi.org/10.3390/biom14020164; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (lucenapadros2024bioinformaticspredictionfor pages 27-28, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Postnatal aggravating factors: intestinal ischemia can drive hypertrophic nerve trunk formation and enteric neuron apoptosis; nitric oxide signaling protects against this cascade (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).

Phenotypic manifestations (HP terms)
- Intestinal aganglionosis with distal colonic obstruction and delayed meconium passage (HP:0002251; HP:0004844), megacolon (HP:0002257), severe constipation (HP:0002019), abdominal distension (HP:0003270), and Hirschsprung-associated enterocolitis with fever, diarrhea, and sepsis risk (HP:0002014, HP:0002017) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (burns2024causesandconsequences pages 6-7, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).

Recent developments and latest research (2023–2024 emphasis)
- Integrative reviews and translational framing (2024): Comprehensive synthesis reaffirms that "critical numbers of neural crest cells are required" and that RET/GDNF and EDN3/EDNRB signaling orchestrate ENS colonization; it also highlights organoid/iPSC models and the trajectory toward cell replacement therapies (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).
- Polygenic and regulatory architecture: WGS in East Asian cohorts demonstrates epistatic interactions between RET enhancer variants within the RET TAD, suggesting synergistic cis-regulatory effects on RET transcription as a mechanism for variable penetrance (Nov 2022; https://doi.org/10.1038/s41598-022-24077-w) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Ischemia and neuronal death (2024): Spatial/single-cell transcriptomics in patient tissue, an ischemic mouse model, and cell assays show ischemia induces ENC zinc accumulation, mitochondrial injury, and caspase-dependent apoptosis; NO donor rescues by inducing mitophagy (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 24-28, xu2024ischemiapromoteshypertrophic pages 1-4).
- HAEC biology (2024): Network-based multi-omics review points to increased vascular permeability, inflammatory signaling, and epithelial transport/barrier perturbations as contributors, integrating miRNA and immune links with HSCR genetics (Jan 2024; https://doi.org/10.3390/biom14020164) (lucenapadros2024bioinformaticspredictionfor pages 27-28).

Current applications and real-world implementations
- Surgical management remains standard (pull-through), but recognition of persistent pan-enteric dysfunction and neuronal subtype imbalance informs postoperative care and risk stratification (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
- Risk assessment: genetic architecture insights (RET regulatory epistasis) and GRN-driven models of RET–EDNRB interactions improve interpretation of variants and counseling (Nov 2022; https://doi.org/10.1038/s41598-022-24077-w; Jul 2019; https://doi.org/10.1093/hmg/ddz149) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- HAEC mitigation: emerging evidence supports surveillance of vascular permeability/barrier function and inflammatory states in high-risk patients, consistent with network findings (Jan 2024; https://doi.org/10.3390/biom14020164) (lucenapadros2024bioinformaticspredictionfor pages 27-28).

Expert opinions and analysis
- Burns & Goldstein (2024) emphasize the centrality of GDNF/RET and EDN3/EDNRB axes, critical cell-number thresholds for successful colonization, and the promise of organoid and regenerative strategies; they also note altered neuronal subtypes and interstitial cells of Cajal as contributors to long-term dysfunction (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7, burns2024causesandconsequences pages 7-8).
- Zhang et al. (2022) synthesize HAEC pathogenesis across genetics, microbiome, barrier, and immune dimensions and underscore the clinical burden and mortality risk of HAEC, motivating translational work (Jun 2022; https://doi.org/10.1055/s-0042-1745780) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).

Relevant statistics and data
- Genetic architecture: RET remains the major susceptibility locus, and epistatic enhancer interactions (65 variants within the RET TAD interacting with rs2435357) were identified in East Asian WGS, supporting polygenic regulatory control (Nov 2022; https://doi.org/10.1038/s41598-022-24077-w) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Ischemia model and patient data: ischemia induced ENC apoptosis with mitochondrial/mitophagy signatures, and NO donor treatment reduced neuronal death and inflammatory markers in experimental systems (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).

Emerging therapies and models
- GDNF-based strategies: preclinical findings indicate that the "success of GDNF-based treatment of Hirschsprung disease depends on NCAM1 signaling" and the presence of responsive enteric progenitor subtypes, aligning with known roles of GDNF in precursor proliferation (May 2025 preprint; https://doi.org/10.1101/2025.05.23.655388; Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (gary2025successofgdnfbased pages 25-34, burns2024causesandconsequences pages 7-8).
- ENS progenitor transplantation: regenerative medicine reviews and translational discourse highlight “cell replacement and other regenerative therapies” as an emerging direction for HSCR management, supported by advancing organoid/iPSC platforms and progenitor isolation methods (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).

Gene/protein annotations with ontology terms
- RET (HGNC:9967): GO:0048011 (neurotrophin TRK receptor signaling via GDNF/RET); cellular component: plasma membrane (GO:0005886); process: neural crest cell migration (GO:0014032). Evidence: human genetics/functional studies summarized in 2024 review (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).
- GDNF (HGNC:4231): GO:0030935 (regulation of neuron differentiation); process: chemoattraction and proliferation of ENS progenitors; quote: “GDNF availability determines enteric neuron number by controlling precursor proliferation” (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 7-8).
- EDNRB (HGNC:3189)/EDN3 (HGNC:3175): GO:0007193 (G protein-coupled receptor signaling); process: regulation of ENCDC proliferation/differentiation; essential for enteric neuron development (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).
- SOX10 (HGNC:11195), PHOX2B (HGNC:9140), NRG1 (HGNC:7997), ZEB2 (HGNC:11776): GO:0006355 (regulation of transcription); participate in ENS GRNs; RET–EDNRB epistasis via shared TF control (Jul 2019; https://doi.org/10.1093/hmg/ddz149) (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).

Phenotype associations (HPO)
- HP:0002251 (Intestinal aganglionosis), HP:0002257 (Megacolon), HP:0002019 (Constipation), HP:0002014 (Diarrhea), HP:0002017 (Enterocolitis) linked mechanistically to ENS absence and HAEC pathobiology (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Jun 2022; https://doi.org/10.1055/s-0042-1745780) (burns2024causesandconsequences pages 6-7, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).

Cell type involvement (CL)
- ENCDCs (CL:0002563), enteric neurons (CL:1001608), enteric glia (CL:0002573), interstitial cells of Cajal (CL:0000632), fibroblasts (CL:0000057) in ischemia-associated HNTs (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (burns2024causesandconsequences pages 7-8, xu2024ischemiapromoteshypertrophic pages 1-4).

Anatomical locations (UBERON)
- Colon (UBERON:0001155), rectosigmoid (UBERON:0001052), myenteric plexus (UBERON:8410064), submucosal plexus (UBERON:0001271) (Nov 2024; https://doi.org/10.1136/wjps-2024-000903) (burns2024causesandconsequences pages 6-7).

Chemical entities (ChEBI)
- Nitric oxide donor sodium nitroprusside (CHEBI:9306) as a modulator of ischemia-induced neuronal death pathways in ENS (Mar 18, 2024 preprint; https://doi.org/10.1101/2024.03.14.24304192) (xu2024ischemiapromoteshypertrophic pages 1-4).

Evidence items (selected with PMIDs/DOIs/URLs and dates)
- Burns AJ, Goldstein AM. Causes and consequences: development and pathophysiology of Hirschsprung disease. World J Pediatr Surg. Nov 2024. DOI: 10.1136/wjps-2024-000903; URL: https://doi.org/10.1136/wjps-2024-000903. Key quotes: “GDNF is mitogenic, neurotrophic, and chemoattractive,” and “GDNF availability determines enteric neuron number by controlling precursor proliferation” (burns2024causesandconsequences pages 6-7, burns2024causesandconsequences pages 7-8).
- Wang Y et al. Whole genome sequencing reveals epistasis effects within RET for Hirschsprung disease. Sci Rep. Nov 2022. DOI: 10.1038/s41598-022-24077-w; URL: https://doi.org/10.1038/s41598-022-24077-w. Summary: 65 epistatic variants within the RET TAD interact with lead enhancer rs2435357, consistent with synergistic cis-regulatory control (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Xu D et al. Ischemia promotes hypertrophic nerve trunk formation and enteric neuron cell death in Hirschsprung's disease. medRxiv. Mar 18, 2024. DOI: 10.1101/2024.03.14.24304192; URL: https://doi.org/10.1101/2024.03.14.24304192. Key quote: ischemia triggers ENC mitochondrial injury/caspase-dependent apoptosis and NO donor “prevented enteric neuron cell death” by inducing mitophagy (xu2024ischemiapromoteshypertrophic pages 1-4).
- Zhang Z et al. Hirschsprung-Associated Enterocolitis: Transformative Research from Bench to Bedside. Eur J Pediatr Surg. Jun 2022. DOI: 10.1055/s-0042-1745780; URL: https://doi.org/10.1055/s-0042-1745780. Synthesis: HAEC involves microbiome, mucus barrier, immune defects, and endothelin pathway susceptibility; Ednrb/Edn3-null models show lymphoid depletion and enterocolitis (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7).
- Lucena-Padrós H et al. Bioinformatics prediction for network-based integrative multi-omics… in Hirschsprung Disease. Biomolecules. Jan 2024. DOI: 10.3390/biom14020164; URL: https://doi.org/10.3390/biom14020164. Highlights: increased vascular permeability in an HSCR murine model and integrative inflammatory/ion-transport pathways implicated in HAEC (lucenapadros2024bioinformaticspredictionfor pages 27-28).
- Gary A et al. Success of GDNF-based treatment of Hirschsprung disease depends on NCAM1 signaling… bioRxiv. May 2025. DOI: 10.1101/2025.05.23.655388; URL: https://doi.org/10.1101/2025.05.23.655388. Implication: NCAM1 signaling as determinant of GDNF-based therapy responsiveness (gary2025successofgdnfbased pages 25-34).

Limitations and open questions
- While foundational mechanisms (RET/GDNF, EDN3/EDNRB) are well supported, finer-grained single-cell human datasets, metabolic programs (e.g., oxidative phosphorylation in ENCDCs), and NF-κB-specific inflammatory circuits in HSCR/HAEC require additional primary evidence integration beyond the evidence included here; 2024–2025 preprints/reporting on ischemia and GDNF/NCAM1 provide plausible, but not yet fully peer-reviewed, mechanisms (Mar 18, 2024; May 2025) (xu2024ischemiapromoteshypertrophic pages 1-4, gary2025successofgdnfbased pages 25-34).

Conclusions
HSCR pathophysiology centers on ENS colonization failure driven by dosage-sensitive RET/GDNF and EDN3/EDNRB signaling within a polygenic regulatory architecture, with downstream consequences for neuronal subtype balance and gut function; complications such as HAEC reflect converging dysmotility, barrier/immune dysfunction, and, as newly suggested, ischemia–mitochondrial injury cascades that may be mitigated by NO signaling. Advances in organoid/iPSC and regenerative strategies point to GDNF- and cell replacement–based interventions, with emerging evidence that NCAM1 signaling and progenitor subtype composition will influence therapeutic success (Nov 2024; https://doi.org/10.1136/wjps-2024-000903; Nov 2022; https://doi.org/10.1038/s41598-022-24077-w; Mar 18, 2024; https://doi.org/10.1101/2024.03.14.24304192; May 2025; https://doi.org/10.1101/2025.05.23.655388) (burns2024causesandconsequences pages 6-7, zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7, xu2024ischemiapromoteshypertrophic pages 1-4, gary2025successofgdnfbased pages 25-34).

References

1. (burns2024causesandconsequences pages 6-7): Alan J. Burns and Allan M Goldstein. Causes and consequences: development and pathophysiology of hirschsprung disease. World Journal of Pediatric Surgery, 7:e000903, Nov 2024. URL: https://doi.org/10.1136/wjps-2024-000903, doi:10.1136/wjps-2024-000903. This article has 2 citations and is from a peer-reviewed journal.

2. (burns2024causesandconsequences pages 7-8): Alan J. Burns and Allan M Goldstein. Causes and consequences: development and pathophysiology of hirschsprung disease. World Journal of Pediatric Surgery, 7:e000903, Nov 2024. URL: https://doi.org/10.1136/wjps-2024-000903, doi:10.1136/wjps-2024-000903. This article has 2 citations and is from a peer-reviewed journal.

3. (xu2024ischemiapromoteshypertrophic pages 1-4): Deshu Xu, Weiwei Liang, Chaoting Lan, Lanying Li, Weiyong Zhong, Meng Yao, Xiaoyu Zuo, Jixiao Zeng, Wei Zhong, Qiang Wu, Andrew M Lew, Wenhao Zhou, Huimin Xia, Fan Bai, Yuxia Zhang, and Yan Zhang. Ischemia promotes hypertrophic nerve trunk formation and enteric neuron cell death in hirschsprung's disease. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.14.24304192, doi:10.1101/2024.03.14.24304192. This article has 0 citations.

4. (zhang2022hirschsprungassociatedenterocolitistransformative pages 7-7): Zhen Zhang, Bo Li, Qian Jiang, Qi Li, Agostino Pierro, and Long Li. Hirschsprung-associated enterocolitis: transformative research from bench to bedside. European journal of pediatric surgery : official journal of Austrian Association of Pediatric Surgery ... [et al] = Zeitschrift fur Kinderchirurgie, 32:383-390, Jun 2022. URL: https://doi.org/10.1055/s-0042-1745780, doi:10.1055/s-0042-1745780. This article has 7 citations.

5. (lucenapadros2024bioinformaticspredictionfor pages 27-28): Helena Lucena-Padros, Nereida Bravo-Gil, Cristina Tous, Elena Rojano, Pedro Seoane-Zonjic, Raquel María Fernández, Juan A. G. Ranea, Guillermo Antiñolo, and Salud Borrego. Bioinformatics prediction for network-based integrative multi-omics expression data analysis in hirschsprung disease. Biomolecules, 14:164, Jan 2024. URL: https://doi.org/10.3390/biom14020164, doi:10.3390/biom14020164. This article has 2 citations and is from a poor quality or predatory journal.

6. (gary2025successofgdnfbased pages 25-34): Alassane Gary, Rodolphe Soret, Marie A. Lefèvre, Nejia Lassoued, Ann Aspirot, Christophe Faure, and Nicolas Pilon. Success of gdnf-based treatment of hirschsprung disease depends on ncam1 signaling and various subtypes of enteric neural progenitors. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.23.655388, doi:10.1101/2025.05.23.655388. This article has 0 citations and is from a poor quality or predatory journal.

7. (xu2024ischemiapromoteshypertrophic pages 24-28): Deshu Xu, Weiwei Liang, Chaoting Lan, Lanying Li, Weiyong Zhong, Meng Yao, Xiaoyu Zuo, Jixiao Zeng, Wei Zhong, Qiang Wu, Andrew M Lew, Wenhao Zhou, Huimin Xia, Fan Bai, Yuxia Zhang, and Yan Zhang. Ischemia promotes hypertrophic nerve trunk formation and enteric neuron cell death in hirschsprung's disease. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.14.24304192, doi:10.1101/2024.03.14.24304192. This article has 0 citations.