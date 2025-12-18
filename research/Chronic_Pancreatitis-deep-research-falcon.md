---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:28.416870'
end_time: '2025-12-17T23:38:52.411572'
duration_seconds: 623.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Pancreatitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Chronic Pancreatitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Pancreatitis**.
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
- **Disease Name:** Chronic Pancreatitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chronic Pancreatitis**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Chronic Pancreatitis
- MONDO ID: MONDO:0005359 (Chronic pancreatitis)
- Category: Complex

Pathophysiology description
Chronic pancreatitis (CP) is a progressive fibroinflammatory disease of the exocrine pancreas characterized by recurrent acinar injury, ductal dysfunction, persistent immune activation, pancreatic stellate cell (PSC) activation, and extracellular matrix deposition leading to irreversible fibrosis, pain, and exocrine/endocrine insufficiency (steatorrhea and type 3c diabetes) (whitcomb20242.diagnosisof pages 1-3). Mechanistically, repeated acute pancreatitis (AP) episodes promote acinar damage, release of damage-associated molecular patterns (DAMPs; HMGB1, HSP70, ATP), and activation of pattern-recognition receptors such as TLR4, triggering NF-κB signaling, upregulation of NLRP3, and inflammasome assembly with caspase-1–dependent maturation of IL‑1β and IL‑18; ATP (via P2X7) and neutrophil extracellular trap–derived ROS further activate NLRP3, amplifying inflammation (tsomidis2024thepathogenesisof pages 13-15). Ductal bicarbonate secretion defects—often involving CFTR—impair luminal alkalinization, favor protein plugs and obstruction, and perpetuate injury (whitcomb20242.diagnosisof pages 3-4). Within the injured milieu, macrophage-derived cytokines (e.g., TGF‑β1) and other mediators activate PSCs, which deposit collagen I/III and fibronectin, driving desmoplasia; alcohol and tobacco can directly activate PSCs (villaca2024pancreaticcrosstalkin pages 12-14). Intracellular stress pathways contribute: ER stress, defective autophagy (e.g., LAMP-2 deficiency), mitochondrial dysfunction, and aberrant calcium signaling promote premature trypsinogen activation and acinar cell death, sustaining chronic inflammation (tsomidis2024thepathogenesisof pages 32-34, belfrageUnknownyearacademicdissertation pages 23-26). Neuro-immune remodeling (including TRPV1-positive sensory fibers and Schwann cells) contributes to chronic pain (belfrageUnknownyearacademicdissertation pages 23-26, cosquer2023pancreaticcancerin pages 2-3). Over years, CP increases pancreatic ductal adenocarcinoma (PDAC) risk via chronic inflammatory signaling (NF‑κB/STAT3), oxidative stress, and metaplastic programs (acinar-to-ductal metaplasia), with progression through PanIN lesions and canonical oncogenic changes (KRAS activation; TP53, CDKN2A, SMAD4 loss) (cosquer2023pancreaticcancerin pages 2-3).

Core Pathophysiology
- Primary mechanisms:
  - Trypsin-dependent acinar injury: premature intrapancreatic trypsinogen activation with autodigestion and inflammation; genetic drivers include PRSS1 gain-of-function and reduced anti-trypsin activity from SPINK1/CTRC variants (osoriovasquez2024identificationofmolecular pages 15-18).
  - Ductal pathway dysfunction: impaired CFTR-mediated Cl−/HCO3− secretion reduces ductal pH/flow, fosters protein plugs and obstruction (whitcomb20242.diagnosisof pages 3-4).
  - Innate immune activation: DAMP→TLR4→NF‑κB drives NLRP3 inflammasome activation, IL‑1β/IL‑18 release, and recruitment of neutrophils/monocytes/macrophages (tsomidis2024thepathogenesisof pages 13-15).
  - PSC activation and fibrosis: TGF‑β autocrine and paracrine signaling converts quiescent PSCs to α‑SMA+ myofibroblast-like cells producing ECM (villaca2024pancreaticcrosstalkin pages 12-14).
  - Intracellular stress and organelle dysfunction: ER stress, defective autophagy, and mitochondrial dysfunction exacerbate acinar injury and inflammation (tsomidis2024thepathogenesisof pages 32-34).
  - Neuro-immune remodeling: TRPV1+ sensory nerves and Schwann cells participate in neurogenic inflammation and pain (cosquer2023pancreaticcancerin pages 2-3, belfrageUnknownyearacademicdissertation pages 23-26).

- Dysregulated pathways:
  - TGF‑β/SMAD signaling in PSC activation and fibrogenesis (villaca2024pancreaticcrosstalkin pages 12-14).
  - IL‑1/IL‑6/TNF–NF‑κB axis and NLRP3 inflammasome in innate immune amplification (tsomidis2024thepathogenesisof pages 13-15).
  - Trypsinogen activation cascade and protease–antiprotease imbalance (PRSS1/SPINK1/CTRC) (osoriovasquez2024identificationofmolecular pages 15-18).
  - Ductal ion transport pathways (CFTR-dependent anion/bicarbonate secretion) (whitcomb20242.diagnosisof pages 3-4).
  - ER stress–autophagy–mitochondrial stress networks driving acinar cell death (tsomidis2024thepathogenesisof pages 32-34).
  - Oncogenic inflammation (NF‑κB/STAT3) and oxidative stress linking CP to PDAC risk (cosquer2023pancreaticcancerin pages 2-3).

- Affected cellular processes:
  - Proteolysis and zymogen activation within acinar cells; aberrant autophagy flux and UPR; mitochondrial ROS generation and permeability changes; cytokine signaling (IL‑1β/IL‑6/TNF); ECM deposition and tissue remodeling; neurogenic inflammation and nociception (tsomidis2024thepathogenesisof pages 13-15, tsomidis2024thepathogenesisof pages 32-34, villaca2024pancreaticcrosstalkin pages 12-14, cosquer2023pancreaticcancerin pages 2-3).

Key Molecular Players
- Genes/Proteins (HGNC):
  - PRSS1 (cationic trypsinogen): causal in hereditary CP via premature activation (osoriovasquez2024identificationofmolecular pages 15-18).
  - SPINK1 (trypsin inhibitor): risk allele reduces trypsin inhibition, increasing injury (osoriovasquez2024identificationofmolecular pages 15-18).
  - CFTR (chloride/bicarbonate channel): ductal dysfunction, reduced HCO3− secretion, obstruction (whitcomb20242.diagnosisof pages 3-4).
  - CTRC (chymotrypsin C): regulates trypsinogen activation; loss-of-function predisposes to CP (osoriovasquez2024identificationofmolecular pages 15-18).
  - CPA1 (carboxypeptidase A1): misfolding variants cause ER stress–mediated pancreatitis (osoriovasquez2024identificationofmolecular pages 15-18).
  - CLDN2 (claudin-2): tight junction risk locus linked to CP susceptibility and inflammatory milieu (whitcomb20242.diagnosisof pages 1-3, cosquer2023pancreaticcancerin pages 2-3).
  - CASR (calcium-sensing receptor): modulates pathological calcium signaling and trypsinogen activation (osoriovasquez2024identificationofmolecular pages 15-18).

- Chemical entities (CHEBI): bicarbonate (ductal secretion) and reactive oxygen species (ROS) as inflammatory mediators in acinar injury (whitcomb20242.diagnosisof pages 3-4, tsomidis2024thepathogenesisof pages 13-15).

- Cell types (CL): acinar cells (injury site), ductal epithelial cells (CFTR-mediated transport), PSCs (fibrosis), macrophages and T cells (immune regulation), Schwann cells/neurons (pain circuitry) (villaca2024pancreaticcrosstalkin pages 12-14, tsomidis2024thepathogenesisof pages 13-15, cosquer2023pancreaticcancerin pages 2-3).

- Anatomical locations (UBERON): exocrine pancreas, pancreatic duct system (cosquer2023pancreaticcancerin pages 2-3, whitcomb20242.diagnosisof pages 3-4).

Biological Processes (for GO annotation)
- Proteolysis/zymogen activation (GO:0006508) in acinar cells (PRSS1/CTRC) (osoriovasquez2024identificationofmolecular pages 15-18).
- Anion/bicarbonate transport (GO:0006820) and regulation of exocrine pancreatic secretion (GO:0044060) in ducts (CFTR) (whitcomb20242.diagnosisof pages 3-4).
- TGF‑β receptor signaling pathway (GO:0007179) driving PSC activation and ECM deposition (villaca2024pancreaticcrosstalkin pages 12-14).
- Activation of NLRP3 inflammasome (GO:0072559) and cytokine-mediated signaling (IL‑1β/IL‑18) (tsomidis2024thepathogenesisof pages 13-15).
- Response to oxidative stress (GO:0006979), ER stress, defective autophagy/lysosomal pathways, mitochondrial dysfunction (tsomidis2024thepathogenesisof pages 32-34).
- Calcium ion homeostasis (GO:0055074) perturbations fueling trypsin activation (osoriovasquez2024identificationofmolecular pages 15-18).

Cellular Components
- Zymogen granules (GO:0042588) in acinar cells (trypsinogen localization/activation) (osoriovasquez2024identificationofmolecular pages 15-18).
- Endoplasmic reticulum (GO:0005783) and mitochondria (GO:0005739) as hubs of ER/mitochondrial stress (tsomidis2024thepathogenesisof pages 32-34).
- Plasma membrane (GO:0005886) for CFTR and calcium/PRR signaling (whitcomb20242.diagnosisof pages 3-4, tsomidis2024thepathogenesisof pages 13-15).
- Extracellular matrix (GO:0031012) deposition by PSCs (villaca2024pancreaticcrosstalkin pages 12-14).

Disease Progression (sequence of events)
- Environmental/genetic triggers (alcohol, tobacco, gallstones; PRSS1/SPINK1/CFTR/CTRC/CPA1/CLDN2/CASR variants) initiate AP via acinar injury and zymogen activation (osoriovasquez2024identificationofmolecular pages 15-18, belfrageUnknownyearacademicdissertation pages 23-26).
- AP events release DAMPs → TLR4/NF‑κB and NLRP3 inflammasome activation → IL‑1β/IL‑18 cytokine cascade, neutrophil/monocyte recruitment (tsomidis2024thepathogenesisof pages 13-15).
- Ductal CFTR dysfunction reduces ductal bicarbonate/flow → protein plugs, intraductal hypertension and recurrent injury (whitcomb20242.diagnosisof pages 3-4).
- Persistent inflammation activates PSCs via TGF‑β and other cytokines → ECM accumulation, fibrosis, ductal strictures (villaca2024pancreaticcrosstalkin pages 12-14).
- Chronic fibrosis and neuronal remodeling produce persistent pain; progressive acinar loss causes exocrine insufficiency; islet involvement yields type 3c diabetes (whitcomb20242.diagnosisof pages 1-3, villaca2024pancreaticcrosstalkin pages 12-14).
- Longstanding CP increases PDAC risk through chronic inflammatory/oxidative signaling (NF‑κB/STAT3) and precursor lesion evolution (PanIN), especially with tobacco exposure (cosquer2023pancreaticcancerin pages 2-3).

Phenotypic Manifestations (HPO) and links to mechanisms
- Recurrent abdominal pain (HPO:0012531): neurogenic inflammation, TRPV1+ nerve remodeling; inflammatory mediators (cosquer2023pancreaticcancerin pages 2-3, belfrageUnknownyearacademicdissertation pages 23-26).
- Exocrine pancreatic insufficiency (HPO:0001738) and steatorrhea (HPO:0002570): acinar loss; ductal obstruction (whitcomb20242.diagnosisof pages 1-3).
- Diabetes mellitus due to pancreatic disease (type 3c) (HPO:0005978): islet involvement following exocrine injury (“exocrine–endocrine crosstalk”) (villaca2024pancreaticcrosstalkin pages 12-14).
- Pancreatic duct stones/strictures (HPO:0025031): protein plugs and fibrosis related to ductal CFTR dysfunction and PSC-mediated remodeling (whitcomb20242.diagnosisof pages 3-4, villaca2024pancreaticcrosstalkin pages 12-14).
- Increased risk of pancreatic cancer (HPO:0100626): chronic inflammatory milieu, KRAS/STAT3/NF‑κB pathways (cosquer2023pancreaticcancerin pages 2-3).

Expert opinions and analysis (authoritative sources)
- Precision-medicine perspective emphasizes CP as an immune-mediated fibroinflammatory disorder with genetic subtypes (trypsin-dependent, protein-misfolding, ductal/CFTR, cellular injury/ER-response), underscoring need for early-stage biomarkers and genetic testing beyond PRSS1/SPINK1/CFTR/CTRC to include CLDN2 and other modifiers (whitcomb20242.diagnosisof pages 1-3).
- Immune pathophysiology highlights TLR4–NLRP3 axis as central to progression from AP to CP with DAMP-driven cycles of inflammasome activation, supporting targeting of IL‑1β/IL‑18 and upstream signals (tsomidis2024thepathogenesisof pages 13-15).
- PSC-centric fibrosis is maintained by TGF‑β autocrine loops and accounts for irreversible parenchymal remodeling; alcohol and tobacco directly activate PSCs, aligning with public health guidance for risk reduction (villaca2024pancreaticcrosstalkin pages 12-14).

Relevant statistics and data (recent)
- CP is radiologically defined by chronic morphologic changes and functionally by exocrine/endocrine failure; major clinical unmet needs include diagnosing early CP and predicting progression (whitcomb20242.diagnosisof pages 1-3).
- PDAC risk rises with long-standing CP; mechanistic links include chronic oxidative/inflammatory signaling and PanIN progression, with tobacco as an additional co-factor (cosquer2023pancreaticcancerin pages 2-3). Quantified risk varies by etiology (e.g., higher in hereditary forms), though precise pooled estimates were not provided in the retrieved excerpts and remain context-dependent.

Gene/protein annotations with ontology terms (examples)
- PRSS1 (HGNC:9488): GO:0006508 proteolysis; GO:0042588 zymogen granule; Evidence: genetic causality in CP (osoriovasquez2024identificationofmolecular pages 15-18).
- SPINK1 (HGNC:11244): GO:0006508 proteolysis; secreted inhibitor; Evidence: risk allele in CP (osoriovasquez2024identificationofmolecular pages 15-18).
- CFTR (HGNC:1884): GO:0006820 anion transport; GO:0005886 plasma membrane; Evidence: ductal dysfunction in CP (whitcomb20242.diagnosisof pages 3-4).
- CTRC (HGNC:2540): GO:0006508 proteolysis; Evidence: loss-of-function increases CP risk (osoriovasquez2024identificationofmolecular pages 15-18).
- CPA1 (HGNC:2293): GO:0005783 ER; misfolding/ER stress pathway (osoriovasquez2024identificationofmolecular pages 15-18).
- CLDN2 (HGNC:2045): tight junction; inflammatory susceptibility (whitcomb20242.diagnosisof pages 1-3, cosquer2023pancreaticcancerin pages 2-3).
- CASR (HGNC:1514): GO:0055074 calcium ion homeostasis; Evidence: trypsin activation context (osoriovasquez2024identificationofmolecular pages 15-18).

Cell type involvement (CL terms)
- Pancreatic stellate cell (CL:0000632): PSC activation → ECM fibrosis (villaca2024pancreaticcrosstalkin pages 12-14).
- Macrophage (CL:0000235): NLRP3 activation, cytokine production (tsomidis2024thepathogenesisof pages 13-15).
- T cell (CL:0000084): adaptive modulation, potential Th17/Treg balance (villaca2024pancreaticcrosstalkin pages 12-14).
- Schwann cell/Neuron (CL:0002573/CL:0000540): neurogenic inflammation and pain (cosquer2023pancreaticcancerin pages 2-3).

Anatomical locations (UBERON terms)
- Pancreas (UBERON:0001264); Exocrine pancreas (UBERON:0001044); Pancreatic duct (UBERON:0008970) (cosquer2023pancreaticcancerin pages 2-3, whitcomb20242.diagnosisof pages 3-4).

Chemical entities (CHEBI terms)
- Bicarbonate (CHEBI:17544) and ROS (CHEBI:26523) in ductal transport and oxidative injury (whitcomb20242.diagnosisof pages 3-4, tsomidis2024thepathogenesisof pages 13-15).

Evidence items and URLs (selected with quotes)
- DAMP–TLR4–NLRP3/IL‑1β axis (tsomidis2024thepathogenesisof pages 13-15): “DAMPs (HMGB1, HSP70, ATP) activate NF‑κB via TLR4 and upregulate NLRP3 … resulting in IL‑1β/IL‑18 maturation and secretion.” 2024; https://doi.org/10.3390/gastroent15020022.
- PSC activation/fibrosis (villaca2024pancreaticcrosstalkin pages 12-14): “Active PSCs express TGFβ, promoting autocrine inhibition of collagen degradation and fibrosis.” 2024; https://doi.org/10.1002/cphy.c230008.
- Autophagy defects (tsomidis2024thepathogenesisof pages 32-34): “Impaired autophagy induces chronic atrophic pancreatitis.” 2024; https://doi.org/10.3390/gastroent15020022.
- Ductal CFTR dysfunction (whitcomb20242.diagnosisof pages 3-4): genetic framework and ductal physiology; 2024; https://doi.org/10.69734/f83fbc79.
- Genetic risk (osoriovasquez2024identificationofmolecular pages 15-18): PRSS1, SPINK1, CFTR, CTRC, CPA1 highlighted in CP genetics; 2024 preprint; https://doi.org/10.1101/2024.10.30.620903.
- CP→PDAC links (cosquer2023pancreaticcancerin pages 2-3): “Mechanisms implicated include oxidative stress … activation of NF‑κB and STAT3 pathways.” 2023; https://doi.org/10.3390/cancers15030761.

Structured artifacts
|Entity type|Name (ontology ID / HGNC / CHEBI / CL / UBERON)|Role in CP pathophysiology (1–2 sentences)|Pathway / GO BP terms (selected)|Cellular component (GO CC terms)|Evidence (year; URL)|Citation ID|
|---|---|---|---|---|---|---|
|Gene|PRSS1 (HGNC:PRSS1)|Encodes cationic trypsinogen; gain‑of‑function PRSS1 variants cause premature intrapancreatic trypsin activation driving acinar autodigestion and recurrent injury.|Proteolysis (GO:0006508)|Zymogen granule (GO:0042588)|2024; https://doi.org/10.1101/2024.10.30.620903|(osoriovasquez2024identificationofmolecular pages 15-18)|
|Gene|SPINK1 (HGNC:SPINK1)|Secreted trypsin inhibitor; loss or reduced function lowers protection against intrapancreatic trypsin activity and increases CP risk.|Proteolysis (GO:0006508)|Zymogen granule / secreted (GO:0042588)|2024; https://doi.org/10.1101/2024.10.30.620903|(osoriovasquez2024identificationofmolecular pages 15-18)|
|Gene|CFTR (HGNC:CFTR)|Apical chloride/bicarbonate channel in ductal epithelium; CFTR dysfunction reduces ductal bicarbonate/fluid secretion, promoting protein plugs and obstructive injury.|Anion transport (GO:0006820); regulation of exocrine pancreatic secretion (GO:0044060)|Plasma membrane (GO:0005886)|2024; https://doi.org/10.69734/f83fbc79|(whitcomb20242.diagnosisof pages 3-4)|
|Gene|CTRC (HGNC:CTRC)|Chymotrypsin C degrades active trypsin and regulates trypsinogen activation; CTRC loss‑of‑function variants reduce trypsin degradation and predispose to CP.|Proteolysis (GO:0006508)|Zymogen granule (GO:0042588)|2024; https://doi.org/10.1101/2024.10.30.620903|(osoriovasquez2024identificationofmolecular pages 15-18)|
|Gene|CPA1 (HGNC:CPA1)|Carboxypeptidase A1; certain misfolding variants cause ER stress and acinar cell injury leading to CP (protein‑misfolding pathway).|Proteolysis (GO:0006508); response to ER stress (related to GO:0006979)|Endoplasmic reticulum (GO:0005783)|2024; https://doi.org/10.1101/2024.10.30.620903|(osoriovasquez2024identificationofmolecular pages 15-18)|
|Gene|CLDN2 (HGNC:CLDN2)|Claudin‑2, a tight junction protein in ducts; risk variants alter ductal barrier/ion permeability and are associated with increased CP susceptibility and inflammation.|Regulation of exocrine pancreatic secretion (GO:0044060); calcium ion homeostasis (GO:0055074)|Plasma membrane / tight junction (GO:0005886)|2023; https://doi.org/10.3390/cancers15030761|(cosquer2023pancreaticcancerin pages 2-3)|
|Gene|CASR (HGNC:CASR)|Calcium‑sensing receptor expressed in pancreatic cells; modulates calcium signaling that can influence trypsinogen activation and acinar injury.|Calcium ion homeostasis (GO:0055074)|Plasma membrane (GO:0005886)|2024; https://doi.org/10.1101/2024.10.30.620903|(osoriovasquez2024identificationofmolecular pages 15-18)|
|Cell type (CL)|Pancreatic stellate cell (CL:0000632)|Quiescent PSCs activate after injury to secrete ECM (collagens, fibronectin) and α‑SMA, driving desmoplasia and progressive pancreatic fibrosis.|TGF‑beta receptor signaling pathway (GO:0007179)|Extracellular matrix (GO:0031012)|2024; https://doi.org/10.1002/cphy.c230008|(villaca2024pancreaticcrosstalkin pages 12-14)|
|Cell type (CL)|Macrophage (CL:0000235)|Infiltrating and resident macrophages produce IL‑1β/IL‑6/TNF and activate inflammasomes (NLRP3), amplifying inflammation and promoting PSC activation and fibrosis.|Activation of NLRP3 inflammasome (GO:0072559); response to oxidative stress (GO:0006979)|Mitochondrion / cytosol (ROS and inflammasome signaling) (GO:0005739)|2024; https://doi.org/10.3390/gastroent15020022|(tsomidis2024thepathogenesisof pages 13-15)|
|Cell type (CL)|T cell (CL:0000084)|Adaptive immune cells (e.g., Th17, regulatory T cells) modulate chronic inflammation in CP and can shape macrophage/PSC responses and disease severity.|Response to oxidative stress (GO:0006979); cytokine‑mediated signaling (related pathways)|Plasma membrane / immunological synapse (GO:0005886)|2024; https://doi.org/10.1002/cphy.c230008|(villaca2024pancreaticcrosstalkin pages 12-14)|
|Cell type (CL)|Schwann cell / Neuron (CL:0002573 / CL:0000540)|Peripheral nerves and Schwann cells undergo remodeling (TRPV1‑mediated neurogenic inflammation), driving neurogenic pain and neuro‑immune crosstalk in CP.|Calcium ion homeostasis (GO:0055074); neurogenic inflammation (related pathways)|Plasma membrane / synapse (GO:0005886)|2023; https://doi.org/10.3390/cancers15030761|(cosquer2023pancreaticcancerin pages 2-3)|
|Anatomical (UBERON)|Pancreas (UBERON:0001264)|Organ‑level site of exocrine (acinar/ductal) injury in CP; progressive acinar loss, ductal changes and fibrosis lead to exocrine/endocrine insufficiency.|Regulation of exocrine pancreatic secretion (GO:0044060)|Zymogen granule / secretory compartments (GO:0042588)|2023; https://doi.org/10.3390/cancers15030761|(cosquer2023pancreaticcancerin pages 2-3)|
|Anatomical (UBERON)|Pancreatic duct (UBERON:0008970)|Ductal epithelium where CFTR‑dependent bicarbonate secretion maintains lumenal pH; duct dysfunction predisposes to protein plug formation and obstruction.|Anion transport (GO:0006820)|Plasma membrane (GO:0005886)|2024; https://doi.org/10.69734/f83fbc79|(whitcomb20242.diagnosisof pages 3-4)|
|Chemical (CHEBI)|Bicarbonate (CHEBI:17544)|Secreted by ductal cells via CFTR/SLC26A9 to alkalinize lumen; reduced bicarbonate favors mucoprotein aggregation and ductal obstruction in CP.|Anion transport (GO:0006820)|Extracellular / lumenal space; associated with apical transporters (GO:0005886)|2024; https://doi.org/10.69734/f83fbc79|(whitcomb20242.diagnosisof pages 3-4)|


*Table: Compact table mapping key genes, cells, anatomical sites and a chemical relevant to chronic pancreatitis to ontology identifiers, concise roles, representative GO biological processes and cellular components, and supporting 2023–2024 evidence (with source URLs). This can be used to populate ontology‑annotated knowledge bases and support curated mechanistic claims.*

> "DAMPs (HMGB1, HSP70, ATP) activate NF-κB via TLR4 and upregulate NLRP3, promoting assembly of the NLRP3 inflammasome with ASC and pro-caspase-1; ATP (via P2X7) and ROS (including NET-derived ROS) activate NLRP3/caspase-1, resulting in IL-1β/IL-18 maturation and secretion." — 2024; https://doi.org/10.3390/gastroent15020022 (tsomidis2024thepathogenesisof pages 13-15)

> "Active PSCs express TGFβ, promoting autocrine inhibition of collagen degradation and fibrosis." — 2024; https://doi.org/10.1002/cphy.c230008 (villaca2024pancreaticcrosstalkin pages 12-14)

> "PSCs produce ECM (collagen I/III, fibronectin) leading to fibrosis." — 2024; https://doi.org/10.1002/cphy.c230008 (villaca2024pancreaticcrosstalkin pages 12-14)

> "Impaired autophagy induces chronic atrophic pancreatitis." — 2024; https://doi.org/10.3390/gastroent15020022 (tsomidis2024thepathogenesisof pages 32-34)

> "we identified a high prevalence of ductal CFTR dysfunction, which could be restored using a combination of CFTR correctors and potentiators." — 2024; https://doi.org/10.1101/2024.10.30.620903 (osoriovasquez2024identificationofmolecular pages 15-18)

> "pancreatitis susceptibility genes commonly tested ("PRSS1, CFTR, SPINK1 and CTRC")" — 2024; https://doi.org/10.69734/f83fbc79 (whitcomb20242.diagnosisof pages 3-4)

> "Mechanisms implicated include oxidative stress, COX2-driven inflammation, and activation of NF-κB and STAT3 pathways." — 2023; https://doi.org/10.3390/cancers15030761 (cosquer2023pancreaticcancerin pages 2-3)


*Blockquote: Selected verbatim quotes from 2023–2024 sources that support core chronic pancreatitis mechanisms (innate immune inflammasome activation, PSC/TGF‑β fibrosis, autophagy defects, CFTR/ductal dysfunction, genetic risk, and links to oncogenic inflammation). These provide citable evidence snippets for knowledge‑base entries.*

Limitations and gaps
- While multiple recent sources substantiate genetic and immuno‑fibrotic mechanisms, precise global incidence/prevalence of CP and pooled PDAC risk estimates could not be extracted from the retrieved excerpts and should be supplemented from epidemiologic syntheses for 2023–2024 where available.

References (by citation IDs with URLs)
- pqac-00000004: Whitcomb & Yadav. 2. Diagnosis of Chronic Pancreatitis. 2024. https://doi.org/10.69734/f83fbc79.
- pqac-00000000: Tsomidis et al. The pathogenesis of pancreatitis and the role of autophagy. 2024. https://doi.org/10.3390/gastroent15020022.
- pqac-00000007: Villaca & Mastracci. Pancreatic Crosstalk… 2024. https://doi.org/10.1002/cphy.c230008.
- pqac-00000005: Tsomidis et al. (additional sections on autophagy/NETs). 2024. https://doi.org/10.3390/gastroent15020022.
- pqac-00000003: Whitcomb & Yadav. Genetics/ductal physiology. 2024. https://doi.org/10.69734/f83fbc79.
- pqac-00000006: Osorio‑Vasquez et al. CP organoids/genetics (preprint). 2024. https://doi.org/10.1101/2024.10.30.620903.
- pqac-00000002: Le Cosquer et al. Pancreatic Cancer in Chronic Pancreatitis. 2023. https://doi.org/10.3390/cancers15030761.

References

1. (whitcomb20242.diagnosisof pages 1-3): David Whitcomb and Dhiraj Yadav. 2. diagnosis of chronic pancreatitis. SMART-MD Journal of Precision Medicine, 1:4-13, Jul 2024. URL: https://doi.org/10.69734/f83fbc79, doi:10.69734/f83fbc79. This article has 0 citations.

2. (tsomidis2024thepathogenesisof pages 13-15): Ioannis Tsomidis, A. Voumvouraki, and E. Kouroumalis. The pathogenesis of pancreatitis and the role of autophagy. Gastroenterology Insights, Apr 2024. URL: https://doi.org/10.3390/gastroent15020022, doi:10.3390/gastroent15020022. This article has 10 citations.

3. (whitcomb20242.diagnosisof pages 3-4): David Whitcomb and Dhiraj Yadav. 2. diagnosis of chronic pancreatitis. SMART-MD Journal of Precision Medicine, 1:4-13, Jul 2024. URL: https://doi.org/10.69734/f83fbc79, doi:10.69734/f83fbc79. This article has 0 citations.

4. (villaca2024pancreaticcrosstalkin pages 12-14): Catharina B.P. Villaca and Teresa L. Mastracci. Pancreatic crosstalk in the disease setting: understanding the impact of exocrine disease on endocrine function. Comprehensive Physiology, 14 2:5371-5387, Mar 2024. URL: https://doi.org/10.1002/cphy.c230008, doi:10.1002/cphy.c230008. This article has 3 citations and is from a peer-reviewed journal.

5. (tsomidis2024thepathogenesisof pages 32-34): Ioannis Tsomidis, A. Voumvouraki, and E. Kouroumalis. The pathogenesis of pancreatitis and the role of autophagy. Gastroenterology Insights, Apr 2024. URL: https://doi.org/10.3390/gastroent15020022, doi:10.3390/gastroent15020022. This article has 10 citations.

6. (belfrageUnknownyearacademicdissertation pages 23-26): H Belfrage. Academic dissertation. Unknown journal, Unknown year.

7. (cosquer2023pancreaticcancerin pages 2-3): Guillaume Le Cosquer, Charlotte Maulat, Barbara Bournet, Pierre Cordelier, Etienne Buscail, and Louis Buscail. Pancreatic cancer in chronic pancreatitis: pathogenesis and diagnostic approach. Cancers, 15:761, Jan 2023. URL: https://doi.org/10.3390/cancers15030761, doi:10.3390/cancers15030761. This article has 65 citations and is from a poor quality or predatory journal.

8. (osoriovasquez2024identificationofmolecular pages 15-18): Victoria Osorio-Vasquez, Jan C. Lumibao, Kristina L. Peck, Kathryn Lande, Jonathan Zhu, McKenna Stamp, Shira R. Okhovat, Hyemin Song, Satoshi Ogawa, Jasper Hsu, Yang Dai, Angelica Rock, Chelsea Bottomley, Ethan Thomas, Alexandra Fowler, T’Onj McGriff, Siri Larsen, Muhamad Abdulla, Phil Greer, Jessica Gibson, Michael Downes, Ronald Evans, Jingjing Zou, Andrew M. Lowy, David C. Whitcomb, Rebekah White, Melena Bellin, Herve Tiriac, and Dannielle D. Engle. Identification of molecular and functional subtypes using chronic pancreatitis patient-derived organoid models. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.10.30.620903, doi:10.1101/2024.10.30.620903. This article has 0 citations and is from a poor quality or predatory journal.