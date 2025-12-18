---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:25.256583'
end_time: '2025-12-17T23:38:13.892356'
duration_seconds: 588.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gastroesophageal Reflux Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Gastroesophageal Reflux Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Gastroesophageal Reflux Disease**.
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
- **Disease Name:** Gastroesophageal Reflux Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Gastroesophageal Reflux Disease**.
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
- Disease Name: Gastroesophageal Reflux Disease (GERD)
- MONDO ID: Not assigned here
- Category: Complex

Plan status note: A structured search and evidence-gathering process identified recent, authoritative sources (priority 2023–2024) and mechanistic reviews. Evidence items are cited with context IDs and include URLs and dates where available.

Pathophysiology description
GERD arises from failure of the anti-reflux barrier at the gastroesophageal junction (lower esophageal sphincter, crural diaphragm, flap valve), leading to retrograde flow of gastric and duodenal contents (acid, pepsin, bile acids) that disrupt epithelial barrier integrity, activate mucosal immune signaling, and sensitize esophageal nociceptors. Transient lower esophageal sphincter relaxations (TLESRs) and hypotensive LES drive reflux events, with obesity, postprandial physiology, and hiatal hernia amplifying proximal reflux exposure. Beyond acid injury, bile acids and weakly acidic reflux perturb tight and adherens junctions, increase permeability/dilated intercellular spaces (DIS), generate reactive oxygen species (ROS), and promote inflammatory cytokines (e.g., IL‑6, IL‑8, TNF), COX‑2, and NO/iNOS pathway activity. Microbiome dysbiosis in the esophagus and gut causally associates with GERD and can impair the epithelial barrier via TLR‑mediated signaling (e.g., a LPS–TLR2–IL‑6–claudin‑1–DIS axis). These barrier and inflammatory changes facilitate access of refluxate to submucosal sensory fibers, producing afferent sensitization through TRPV1/TRPA1/ASIC channels and neuropeptides (e.g., CGRP), thereby generating heartburn and related symptoms. Chronic reflux-inflammation drives metaplastic adaptation (Barrett’s esophagus), in which claudin‑18-dominant tight junctions contribute to acid resistance, while progressive genomic instability with TP53 and CDKN2A alterations underlies dysplasia and adenocarcinoma risk (URLs/dates provided inline below). (arguero2024pathophysiologyofgastrooesophageal pages 2-4, arguero2024pathophysiologyofgastrooesophageal pages 6-7, leech2024mucosalneuroimmunemechanisms pages 1-3, chen2024esophagealmicrobialdysbiosis pages 8-12, wang2024causalrelationshipbetween pages 5-8, jovov2007claudin18adominant pages 3-4, moe2024mechanisticinsightson pages 8-10)

1) Core Pathophysiology
- Mechanical drivers: A multifactorial model links gastric factors (acid pocket, accommodation), the anti-reflux barrier (LES, crural diaphragm), and clearance to symptom generation. Argüero & Sifrim highlight delayed gastric emptying in up to 40% of GERD, obesity effects on reflux physiology, and the central role of TLESRs; management implications include TLESR reduction with baclofen and addressing hiatal hernia and LES hypotension (Nature Reviews Gastroenterology & Hepatology, Jan 2024; https://doi.org/10.1038/s41575-023-00883-z). (arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- Epithelial barrier disruption: Weakly acidic solutions with bile acids increase mucosal permeability and DIS; bile acids increase hydrogen ion permeability. These changes are associated with symptom generation and mucosal injury (same 2024 review). (arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Inflammatory signaling: Upregulation of IL‑6, IL‑8, TNF and COX‑2 in reflux-exposed mucosa is consistently reported, with mast cells, eosinophils, dendritic cells, and T/B lymphocytes contributing to “macro- and micro-inflammation.” (Journal of Gastroenterology, Jan 2024; https://doi.org/10.1007/s00535-023-02065-9). (leech2024mucosalneuroimmunemechanisms pages 1-3)
- Neurosensory mechanisms: TRPV1+ CGRP+ afferents lie near the lumen, and mast cell mediators (histamine, PGD2) sensitize vagal C‑fibers; epithelial permeability exposes nociceptors to refluxate, driving pain. (Leech & Peiris 2024). (leech2024mucosalneuroimmunemechanisms pages 1-3, leech2024mucosalneuroimmunemechanisms pages 6-7)
- Microbiome and TLR signaling: A 2024 translational study demonstrated that Gram‑negative enrichment in patients with reflux symptoms increases mucosal TLR2 and IL‑6, downregulates claudin‑1, and induces DIS, all mitigated by TLR2/IL‑6 blockade; the authors delineate a “LPS–TLR2–IL‑6–claudin‑1–DIS” axis (Journal of Translational Medicine, Dec 2024; https://doi.org/10.1186/s12967-024-05878-1). (chen2024esophagealmicrobialdysbiosis pages 8-12, chen2024esophagealmicrobialdysbiosis pages 1-2, chen2024esophagealmicrobialdysbiosis pages 14-14)
- Gut microbiome causality: A 2024 bidirectional Mendelian randomization study found causal links between specific gut taxa and GERD risk (e.g., protective Actinobacteria, Methanobrevibacter; risk Mollicutes, Tenericutes), supporting microecological therapeutic strategies (Frontiers in Immunology, Feb 2024; https://doi.org/10.3389/fimmu.2024.1327503). (wang2024causalrelationshipbetween pages 5-8)
- Oxidative stress and bile/pepsin cytotoxicity: Bile acids and weakly acidic reflux provoke ROS generation, DNA damage and injury in ex vivo/clinical contexts, complementing protease-mediated barrier degradation by pepsin (2024 review). (arguero2024pathophysiologyofgastrooesophageal pages 6-7)

2) Key Molecular Players
- Junctional/Barrier proteins: Claudin‑1 (CLDN1) downregulation (via LPS–TLR2–IL‑6) and adherens junction involvement (E‑cadherin) contribute to DIS and permeability; in Barrett’s, claudin‑18 is the dominant TJ protein co-localized with ZO‑1 and likely contributes to acid resistance (AJP‑GI, Dec 2007; https://doi.org/10.1152/ajpgi.00158.2007). (chen2024esophagealmicrobialdysbiosis pages 8-12, chen2024esophagealmicrobialdysbiosis pages 14-14, jovov2007claudin18adominant pages 3-4)
- Inflammatory mediators and pathways: IL‑6, IL‑8, TNF, COX‑2/PTGS2, and NO/iNOS are implicated; immune cell infiltration and mediator release sensitize neurons and sustain inflammation (Leech 2024; Argüero & Sifrim 2024). (leech2024mucosalneuroimmunemechanisms pages 1-3, arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Neurosensory channels and neuropeptides: TRPV1, TRPA1 and acid‑sensing ion channels (e.g., ASIC3) contribute to pain/hypersensitivity; CGRP marks nociceptive afferents (Leech 2024; supportive review of TRP channel crosstalk, Biomolecules, Jul 2024; https://doi.org/10.3390/biom14070877). (leech2024mucosalneuroimmunemechanisms pages 1-3, wu2024theroleand pages 7-8, ismail2025understandingthemechanisms pages 7-9)
- LES/TLESRs circuitry: Vagal pathways and nitrergic signaling modulate sphincter function; autonomic dysregulation in GERD is documented, and neuromodulation can enhance vagal activity and downregulate nNOS in related models (Expert Review of Gastroenterology & Hepatology, Nov 2023; https://doi.org/10.1080/17474124.2023.2288156). (yin2023noninvasiveelectricalneuromodulation pages 11-12)
- Bile acids/pepsin: Bile acids increase permeability and ROS; pepsin contributes to mucosal protein degradation (Argüero & Sifrim 2024). (arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Barrett’s esophagus progression: Claudin‑18 is highly expressed in BE and localizes to TJs; chronic reflux‑inflammation and dysbiosis promote NF‑κB/MAPK/STAT axis activation with subsequent genomic instability involving TP53 and CDKN2A (Cancers, Sep 2024; https://doi.org/10.3390/cancers16193305). (jovov2007claudin18adominant pages 3-4, moe2024mechanisticinsightson pages 8-10)

3) Biological Processes (GO-like)
- Tight junction assembly/disassembly; adherens junction organization; epithelial cell–cell adhesion and permeability regulation (driven by CLDN1, CDH1 changes). (chen2024esophagealmicrobialdysbiosis pages 8-12, chen2024esophagealmicrobialdysbiosis pages 14-14)
- TLR signaling pathway activation (LPS–TLR2) and downstream IL‑6 production; NF‑κB/MAPK/STAT activation; prostaglandin biosynthetic process (COX‑2). (chen2024esophagealmicrobialdysbiosis pages 8-12, leech2024mucosalneuroimmunemechanisms pages 1-3, moe2024mechanisticinsightson pages 8-10)
- Nitric oxide biosynthetic process (iNOS, nitrergic neurons); regulation of smooth muscle contraction (LES). (yin2023noninvasiveelectricalneuromodulation pages 11-12, arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Sensory perception of pain, neurogenic inflammation; TRP channel signaling; response to acid and chemical stimulus. (leech2024mucosalneuroimmunemechanisms pages 1-3, wu2024theroleand pages 7-8)
- Response to bile acid; ROS metabolic process; DNA damage response. (arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Microbiome-mediated modulation of epithelial barrier and immune responses; causal gut microbiome influences on GERD risk. (chen2024esophagealmicrobialdysbiosis pages 8-12, wang2024causalrelationshipbetween pages 5-8)

4) Cellular Components
- Apical tight junction complexes (ZO‑1 co-localization with claudin‑18 in BE) and basolateral membranes (E‑cadherin). (jovov2007claudin18adominant pages 3-4)
- Nociceptive nerve terminals near the epithelial surface (TRPV1+ CGRP+ fibers); vagal C‑fiber endings. (leech2024mucosalneuroimmunemechanisms pages 1-3)
- LES smooth muscle and myenteric plexus (nitrergic neurons). (yin2023noninvasiveelectricalneuromodulation pages 11-12)
- Extracellular lumen containing refluxate (acid, bile acids, pepsin) contacting squamous epithelium and exposing submucosal afferents when barrier compromised. (arguero2024pathophysiologyofgastrooesophageal pages 6-7, leech2024mucosalneuroimmunemechanisms pages 1-3)

5) Disease Progression
- Initial triggers: Postprandial TLESRs and LES hypotension allow reflux; proximal extent increases especially postprandially. (arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- Early mucosal events: Acid/weakly acidic bile salt exposure increases permeability and DIS; epithelial IL‑6/IL‑8/TNF and COX‑2 induction with immune cell recruitment; nociceptor sensitization (TRPV1/TRPA1/ASIC) generates heartburn. (arguero2024pathophysiologyofgastrooesophageal pages 6-7, leech2024mucosalneuroimmunemechanisms pages 1-3)
- Microbiome contribution: Gram‑negative enrichment drives TLR2–IL‑6–claudin‑1 downregulation and DIS, potentially in GERD and functional reflux phenotypes; gut taxa show bidirectional causal relationships with GERD. (chen2024esophagealmicrobialdysbiosis pages 8-12, wang2024causalrelationshipbetween pages 5-8)
- Chronicity and remodeling: Persistent ROS and inflammation; neuroimmune crosstalk (mast cell mediators, CGRP) maintains hypersensitivity. (leech2024mucosalneuroimmunemechanisms pages 1-3, arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Metaplastic adaptation and neoplastic risk: In chronic reflux, BE develops, characterized by claudin‑18‑dominant TJs and acid resistance; genomic instability with early/central TP53 and CDKN2A changes underlies dysplasia/EAC progression (Cancers 2024; AJP‑GI 2007). (moe2024mechanisticinsightson pages 8-10, jovov2007claudin18adominant pages 3-4)

6) Phenotypic Manifestations
- Typical symptoms: Heartburn and regurgitation; their severity relates to reflux frequency/proximal extent and impaired mucosal integrity (lower mucosal impedance with hiatal hernia). (arguero2024pathophysiologyofgastrooesophageal pages 6-7, arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- Extraesophageal symptoms: Proximal reflux and airway reflex activation via shared TRP pathways can contribute to cough/throat symptoms; neuromodulation of vagal pathways is under study. (leech2024mucosalneuroimmunemechanisms pages 1-3, yin2023noninvasiveelectricalneuromodulation pages 11-12)
- Risk modifiers and statistics: Obesity increases GERD risk (OR ~1.8 overweight; ~2.6 obesity) and associates with hiatal hernia and low LES pressure; each BMI unit associates with 0.35% increase in distal esophageal pH<4 time (Nature Reviews Gastroenterology & Hepatology, 2024). (arguero2024pathophysiologyofgastrooesophageal pages 2-4)

Embedded ontology-ready mapping
| Category | Entity (standard name) | Ontology (namespace:ID) | Mechanistic role in GERD (1 sentence) | Evidence (short citation with context ID) |
|---|---|---|---|---|
| Receptor / PRR | TLR2 | HGNC:11850 | Mediates esophageal epithelial responses to LPS from Gram-negative dysbiosis leading to IL-6 upregulation and claudin-1 downregulation (DIS). | Chen 2024 J Transl Med (chen2024esophagealmicrobialdysbiosis pages 8-12), Wang 2024 Front Immunol (wang2024causalrelationshipbetween pages 5-8) |
| Cytokine | IL-6 | HGNC:6018 | Pro-inflammatory cytokine induced by epithelial TLR signaling that contributes to tight-junction disruption and inflammation. | Chen 2024 J Transl Med (chen2024esophagealmicrobialdysbiosis pages 8-12), Argüero & Sifrim 2024 Nat Rev Gastroenterol Hepatol (arguero2024pathophysiologyofgastrooesophageal pages 6-7) |
| Enzyme / Mediator | PTGS2 / COX-2 | HGNC:9605 | Induced in reflux-exposed epithelium, produces prostaglandins that sensitize afferents and sustain mucosal inflammation. | Argüero & Sifrim 2024 Nat Rev Gastroenterol Hepatol (arguero2024pathophysiologyofgastrooesophageal pages 6-7), Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 1-3) |
| Enzyme / Mediator | NOS2 / iNOS | HGNC:7873 | Inducible NO synthase contributes to inflammatory signaling and nitrosative stress in reflux-damaged mucosa and is linked to neurogenic/motility effects. | Zheng 2025 Front Immunol (zheng2025multidimensionalmechanismsand pages 1-2), Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7) |
| Tight junction protein | CLDN1 (Claudin-1) | HGNC:2033 | Tight-junction component downregulated by LPS–TLR2–IL-6 signaling, causing dilated intercellular spaces and increased permeability. | Chen 2024 J Transl Med (chen2024esophagealmicrobialdysbiosis pages 8-12) |
| Adherens junction protein | CDH1 / E-cadherin | HGNC:1748 | Loss or mislocalization reduces cell–cell adhesion and increases epithelial permeability in reflux states. | Argüero & Sifrim 2024 Nat Rev Gastroenterol Hepatol (arguero2024pathophysiologyofgastrooesophageal pages 6-7), Chen 2024 J Transl Med (chen2024esophagealmicrobialdysbiosis pages 14-14) |
| Tight junction protein (BE) | CLDN18 (Claudin-18) | HGNC:20628 | Dominant TJ protein in Barrett's columnar epithelium and implicated in acid resistance of metaplastic mucosa. | Jovov 2007 AJP-GI (jovov2007claudin18adominant pages 3-4), Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7) |
| Ion channel / nociceptor | TRPV1 | HGNC:18888 | Proton/acid-activated cation channel on sensory fibers that mediates heartburn and afferent sensitization. | Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 1-3), Wu 2024 Biomolecules (wu2024theroleand pages 7-8) |
| Ion channel / nociceptor | TRPA1 | HGNC:11320 | Chemosensory channel co-expressed on nociceptors that contributes to chemical/oxidative sensitization and cough/airway reflexes. | Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 1-3), Moe 2024 Cancers (moe2024mechanisticinsightson pages 8-10) |
| Ion channel / nociceptor | ASIC3 / ACCN3 | HGNC:135 | Acid-sensing ion channel expressed in esophageal afferents that contributes to visceral acid hypersensitivity. | Ismail 2025 systematic review (ismail2025understandingthemechanisms pages 7-9), Leech 2024 (leech2024mucosalneuroimmunemechanisms pages 1-3) |
| Neuropeptide | CGRP (CALCA) | HGNC:1433 | Neuropeptide released from TRPV1+ afferents that mediates neurogenic inflammation and pain signaling. | Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 1-3) |
| Receptor (adenosine) | ADORA2A | HGNC:262 | Adenosine receptor implicated in activation/modulation of esophageal nociceptors and pain signaling. | Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 1-3), Moe 2024 Cancers (moe2024mechanisticinsightson pages 8-10) |
| Tumor suppressor | TP53 | HGNC:11998 | Frequently mutated in progression from Barrett's esophagus to dysplasia and adenocarcinoma, marking genomic instability. | Moe 2024 Cancers (moe2024mechanisticinsightson pages 8-10), Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7) |
| Tumor suppressor / cell-cycle | CDKN2A (p16) | HGNC:1787 | Early genetic alteration associated with Barrett's progression and dysplasia risk. | Moe 2024 Cancers (moe2024mechanisticinsightson pages 8-10), Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7) |
| Small molecule (bile) | Deoxycholic acid (DCA) | CHEBI:27314 | A hydrophobic bile acid that disrupts epithelial TJs, generates ROS and DNA damage, and promotes metaplasia risk. | Argüero & Sifrim 2024 Nat Rev Gastroenterol Hepatol (arguero2024pathophysiologyofgastrooesophageal pages 6-7), Xu 2023 / related analyses (moe2024mechanisticinsightson pages 8-10) |
| Chemical class | Bile acids | CHEBI:36264 | Components of refluxate that increase mucosal permeability, induce oxidative stress and inflammatory signaling. | Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7), Zhao 2025 review (moe2024mechanisticinsightson pages 8-10) |
| Chemical entity | Hydrochloric acid / H+ | CHEBI:15378 | Gastric acid component that injures epithelium, activates acid sensors (e.g., TRPV1) and contributes to pain and mucosal damage. | Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 1-3), Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7) |
| Enzyme (digestive) | Pepsin (PGA family, note: pepsin) | HGNC:8897 family (PGA genes) | Proteolytic enzyme in refluxate that degrades extracellular proteins, weakens barrier and promotes inflammation/oxidative stress. | Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 6-7), Ismail 2025 systematic review (ismail2025understandingthemechanisms pages 7-9) |
| Cell type | Esophageal squamous epithelial cell (SCE) | CL:0002495 | Primary epithelial cell type lining the oesophagus that is injured by reflux leading to barrier loss and inflammation. | Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 2-4), Jovov 2007 AJP-GI (jovov2007claudin18adominant pages 3-4) |
| Immune cell | Mast cell | CL:0000097 | Releases histamine, prostaglandins and other mediators that sensitize nociceptors and promote mucosal inflammation. | Leech 2024 J Gastroenterol (leech2024mucosalneuroimmunemechanisms pages 6-7) |
| Neuron type | Vagal sensory neuron | CL:0000100 | Vagal afferents mediate reflexes (including TLESRs) and transmit chemical/mechanical nociception from the oesophagus. | Yin & Chen 2023 Expert Rev Gastroenterol Hepatol (yin2023noninvasiveelectricalneuromodulation pages 11-12), Leech 2024 (leech2024mucosalneuroimmunemechanisms pages 1-3) |
| Anatomy | Esophagus | UBERON:0001043 | Organ affected by reflux where mucosal barrier, immune and neural interactions determine symptom and injury patterns. | Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 2-4) |
| Anatomy / sphincter | Lower esophageal sphincter (LES) | UBERON:0002469 | Functional barrier whose transient relaxations (TLESRs) and hypotension permit reflux episodes that expose mucosa to injurious contents. | Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 2-4), Yin & Chen 2023 (yin2023noninvasiveelectricalneuromodulation pages 11-12) |
| Anatomy / junction | Gastroesophageal junction | UBERON:0002350 | Anatomical anti-reflux zone (including flap valve, diaphragm relationships) whose disruption (hiatal hernia) increases reflux and mucosal exposure. | Argüero & Sifrim 2024 (arguero2024pathophysiologyofgastrooesophageal pages 2-4) |


*Table: Concise mapping of key genes/proteins, chemicals, cells and anatomical terms relevant to GERD pathophysiology with ontology identifiers and one-line mechanistic roles, supported by 2023–2024 evidence (context IDs). This table is formatted for ontology annotation and evidence traceability.*

Evidence items with URLs/dates and key quotes
- Epithelial barrier and bile acids: “Weakly acidic solutions with bile acids cause increased mucosal permeability and dilation of intercellular spaces… bile acids increase mucosal permeability to hydrogen ion… induce reactive oxygen species in ex vivo Barrett tissue” (Nature Reviews Gastroenterology & Hepatology, Jan 2024; https://doi.org/10.1038/s41575-023-00883-z). (arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Microbiome–TLR–IL‑6–TJ axis: “Gram‑negative enrichment… higher TLR2, reduced claudin‑1 and DIS… LPS increased TLR2 and IL‑6; claudin‑1 downregulation and DIS were mitigated by TLR2 or IL‑6 blockade,” supporting a “LPS–TLR2–IL‑6–claudin‑1–DIS pathway” (Journal of Translational Medicine, Dec 2024; https://doi.org/10.1186/s12967-024-05878-1). (chen2024esophagealmicrobialdysbiosis pages 8-12, chen2024esophagealmicrobialdysbiosis pages 1-2, chen2024esophagealmicrobialdysbiosis pages 14-14)
- Neuroimmune nociception: “TRPV1 activation on CGRP+ sensory nerves… mast cell-derived histamine and prostaglandin D2 sensitize vagal nodose C‑fibres” (Journal of Gastroenterology, Jan 2024; https://doi.org/10.1007/s00535-023-02065-9). (leech2024mucosalneuroimmunemechanisms pages 1-3, leech2024mucosalneuroimmunemechanisms pages 6-7)
- LES/TLESRs physiology and management: Multifactorial pathophysiology with TLESRs and hiatal hernia highlighted; therapeutic implications include baclofen for TLESRs and addressing gastric factors (Nature Reviews Gastroenterology & Hepatology, Jan 2024; https://doi.org/10.1038/s41575-023-00883-z). (arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- Autonomic/neuromodulation evidence: Noninvasive neuromodulation improves GI symptoms by enhancing vagal activity; rodent vagal stimulation restored ENS/ICC and downregulated nNOS (Expert Review of Gastroenterology & Hepatology, Nov 2023; https://doi.org/10.1080/17474124.2023.2288156). (yin2023noninvasiveelectricalneuromodulation pages 11-12)
- Gut microbiome causality: Protective (Actinobacteria, Methanobrevibacter; ORs <1) and risk (Mollicutes, Tenericutes; ORs >1) taxa identified by MR; bidirectional GERD–microbiome links (Frontiers in Immunology, Feb 2024; https://doi.org/10.3389/fimmu.2024.1327503). (wang2024causalrelationshipbetween pages 5-8)
- Barrett’s barrier and acid resistance: Claudin‑18 is “highly and exclusively expressed in BE” and co‑localizes with ZO‑1 at TJs, supporting an acid‑resistant barrier phenotype (AJP‑GI, Dec 2007; https://doi.org/10.1152/ajpgi.00158.2007). (jovov2007claudin18adominant pages 3-4)
- Inflammation–carcinogenesis link in esophagus: Dysbiosis activates NF‑κB/MAPK/STAT and inflammasome pathways with IL‑1β/IL‑6/IL‑8/TNF; chronic inflammation compromises the epithelial barrier and promotes DNA damage and oncogenic signaling (Cancers, Sep 2024; https://doi.org/10.3390/cancers16193305). (moe2024mechanisticinsightson pages 8-10)

Gene/protein annotations (HGNC, GO-like), phenotype (HP), cell types (CL), anatomical sites (UBERON), chemicals (CHEBI)
- HGNC: CLDN1 (HGNC:2033), CDH1 (HGNC:1748), CLDN18 (HGNC:20628), IL6 (HGNC:6018), PTGS2 (HGNC:9605), NOS2 (HGNC:7873), TRPV1 (HGNC:18888), TRPA1 (HGNC:11320), ACCN3/ASIC3 (HGNC:135), CALCA (CGRP; HGNC:1433), TP53 (HGNC:11998), CDKN2A (HGNC:1787). (chen2024esophagealmicrobialdysbiosis pages 8-12, leech2024mucosalneuroimmunemechanisms pages 1-3, jovov2007claudin18adominant pages 3-4, moe2024mechanisticinsightson pages 8-10)
- GO-like processes: tight junction organization; TLR signaling; NF‑κB and MAPK cascade; nitric oxide biosynthesis; response to acid; sensory perception of pain; ROS metabolism; DNA damage response. (chen2024esophagealmicrobialdysbiosis pages 8-12, leech2024mucosalneuroimmunemechanisms pages 1-3, arguero2024pathophysiologyofgastrooesophageal pages 6-7, moe2024mechanisticinsightson pages 8-10, yin2023noninvasiveelectricalneuromodulation pages 11-12)
- HP terms (examples): HP:0002027 Heartburn; HP:0002573 Chest pain; HP:0002015 Dysphagia; HP:0031410 Chronic cough (extraesophageal). Ties: nociceptive sensitization, barrier disruption, proximal reflux. (arguero2024pathophysiologyofgastrooesophageal pages 2-4, leech2024mucosalneuroimmunemechanisms pages 1-3, arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- CL: Esophageal squamous epithelial cell (CL:0002495), Mast cell (CL:0000097), Vagal sensory neuron (CL:0000100). (leech2024mucosalneuroimmunemechanisms pages 6-7, leech2024mucosalneuroimmunemechanisms pages 1-3)
- UBERON: Esophagus (UBERON:0001043), Lower esophageal sphincter (UBERON:0002469), Gastroesophageal junction (UBERON:0002350). (arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- CHEBI: Deoxycholic acid (CHEBI:27314), Bile acids (CHEBI:36264), Hydrochloric acid/H+ (CHEBI:15378). (arguero2024pathophysiologyofgastrooesophageal pages 6-7)

Current applications and real-world implementations
- Diagnostic implications: Baseline impedance and DIS reflect impaired mucosal integrity; combined impedance‑pH monitoring and postprandial assessment capture weakly acidic/bile reflux reaching proximal esophagus. (arguero2024pathophysiologyofgastrooesophageal pages 6-7, arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- Therapeutic implications: Algorithmic management includes targeting TLESRs (baclofen), LES hypotension (prokinetics, surgery when indicated), gastric factors (diet, alginates to cap acid pocket), obesity interventions (weight loss, bariatric surgery selection), and emerging neuromodulation to enhance vagal tone in refractory motility/GERD phenotypes. (arguero2024pathophysiologyofgastrooesophageal pages 2-4, yin2023noninvasiveelectricalneuromodulation pages 11-12)
- Microbiome-informed approaches: The MR study supports exploration of microecological therapies to shift taxa with protective profiles (e.g., Actinobacteria) and reduce harmful classes (e.g., Mollicutes). (wang2024causalrelationshipbetween pages 5-8)

Expert opinions and analysis (authoritative sources)
- Nature Reviews (2024) synthesizes GERD’s multifactorial pathophysiology and ties specific mechanisms to management, underscoring that weakly acidic and bile reflux can drive symptoms/injury even with acid suppression. (arguero2024pathophysiologyofgastrooesophageal pages 2-4, arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Journal of Gastroenterology (2024) emphasizes neuroimmune crosstalk—barrier failure, immune activation, and nerve sensitization—as a central driver of pain/hypersensitivity in GORD. (leech2024mucosalneuroimmunemechanisms pages 1-3, leech2024mucosalneuroimmunemechanisms pages 6-7)
- Translational and MR studies (2024) extend mechanisms to human cohorts and genetics, respectively, strengthening causality for microbiome–barrier interactions and gut taxa–GERD risk. (chen2024esophagealmicrobialdysbiosis pages 8-12, wang2024causalrelationshipbetween pages 5-8)

Relevant statistics and data
- Obesity: Odds ratio for GERD ≈1.8 (overweight) and 2.6 (obesity); per‑unit BMI increase associates with +0.35% time pH<4 in distal esophagus (Nature Reviews Gastroenterology & Hepatology, 2024; https://doi.org/10.1038/s41575-023-00883-z). (arguero2024pathophysiologyofgastrooesophageal pages 2-4)
- Microbiome MR: Protective associations (e.g., Phylum Actinobacteria OR 0.82, 95% CI 0.68–0.99; Genus Methanobrevibacter OR 0.95, 95% CI 0.91–0.99) and risk associations (e.g., Class Mollicutes OR 1.09, 95% CI 1.01–1.19; Phylum Tenericutes OR 1.11, 95% CI 1.01–1.22) with GERD risk (Frontiers in Immunology, 2024; https://doi.org/10.3389/fimmu.2024.1327503). (wang2024causalrelationshipbetween pages 5-8)

Limitations and open questions
- Direct molecular mapping of iNOS/COX‑2 and nociceptor subtypes in human esophageal biopsies across GERD phenotypes remains heterogeneous across studies; mechanistic interventional trials that modulate the microbiome–TLR axis and measure barrier/neurosensory endpoints are needed. (leech2024mucosalneuroimmunemechanisms pages 1-3, chen2024esophagealmicrobialdysbiosis pages 8-12)

Primary evidence (selection; all with URLs/dates)
- Argüero J, Sifrim D. Pathophysiology of gastro‑oesophageal reflux disease: implications for diagnosis and management. Nature Reviews Gastroenterology & Hepatology. Jan 2024. https://doi.org/10.1038/s41575-023-00883-z. (arguero2024pathophysiologyofgastrooesophageal pages 2-4, arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- Leech T, Peiris M. Mucosal neuroimmune mechanisms in GORD pathogenesis. Journal of Gastroenterology. Jan 2024. https://doi.org/10.1007/s00535-023-02065-9. (leech2024mucosalneuroimmunemechanisms pages 1-3, leech2024mucosalneuroimmunemechanisms pages 6-7)
- Chen S et al. Esophageal microbial dysbiosis impairs mucosal barrier integrity via TLR2 pathway in patients with reflux symptoms. Journal of Translational Medicine. Dec 2024. https://doi.org/10.1186/s12967-024-05878-1. (chen2024esophagealmicrobialdysbiosis pages 8-12, chen2024esophagealmicrobialdysbiosis pages 1-2, chen2024esophagealmicrobialdysbiosis pages 14-14)
- Wang K et al. Causal relationship between gut microbiota and risk of GERD: bidirectional MR. Frontiers in Immunology. Feb 2024. https://doi.org/10.3389/fimmu.2024.1327503. (wang2024causalrelationshipbetween pages 5-8)
- Yin J, Chen JDZ. Noninvasive electrical neuromodulation for GI motility disorders. Expert Review of Gastroenterology & Hepatology. Nov 2023. https://doi.org/10.1080/17474124.2023.2288156. (yin2023noninvasiveelectricalneuromodulation pages 11-12)
- Jovov B et al. Claudin‑18: dominant tight junction protein in Barrett’s and likely contributor to acid resistance. AJP‑GI. Dec 2007. https://doi.org/10.1152/ajpgi.00158.2007. (jovov2007claudin18adominant pages 3-4)
- Moe KT, Tan KSW. Mechanistic insights on microbiota‑mediated development and progression of esophageal cancer. Cancers. Sep 2024. https://doi.org/10.3390/cancers16193305. (moe2024mechanisticinsightson pages 8-10)

Direct quotes (where available)
- “LPS–TLR2–IL‑6–claudin‑1–DIS pathway” (Chen 2024 J Transl Med). (chen2024esophagealmicrobialdysbiosis pages 14-14)
- “Weakly acidic solutions with bile acids cause increased mucosal permeability and dilation of intercellular spaces” (Argüero & Sifrim 2024 Nat Rev Gastroenterol Hepatol). (arguero2024pathophysiologyofgastrooesophageal pages 6-7)
- “Mast cell‑derived histamine and prostaglandin D2 have been found to sensitize vagal nodose C‑fibres” (Leech 2024 Journal of Gastroenterology). (leech2024mucosalneuroimmunemechanisms pages 6-7)

Summary
Recent high-quality studies converge on a mechanistic cascade: mechanical reflux exposure → epithelial barrier injury (tight/adherens junction disruption and DIS) → innate/immune activation (TLR–NF‑κB/MAPK/STAT; COX‑2; iNOS) → nociceptor sensitization (TRPV1/TRPA1/ASIC; CGRP) → symptoms. Bile acids and pepsin potentiate ROS/DNA damage and, with chronic inflammation and dysbiosis, enable Barrett’s metaplasia, in which claudin‑18‑dominant TJs confer acid resistance but progressive genomic instability (TP53, CDKN2A) increases neoplastic risk. Human cohort and genetic studies in 2023–2024 add causal evidence for microbiome involvement and define actionable axes (e.g., TLR2–IL‑6–claudin‑1) for therapeutic development. (arguero2024pathophysiologyofgastrooesophageal pages 2-4, arguero2024pathophysiologyofgastrooesophageal pages 6-7, leech2024mucosalneuroimmunemechanisms pages 1-3, chen2024esophagealmicrobialdysbiosis pages 8-12, wang2024causalrelationshipbetween pages 5-8, jovov2007claudin18adominant pages 3-4, moe2024mechanisticinsightson pages 8-10)

References

1. (arguero2024pathophysiologyofgastrooesophageal pages 2-4): Julieta Argüero and Daniel Sifrim. Pathophysiology of gastro-oesophageal reflux disease: implications for diagnosis and management. Nature reviews. Gastroenterology & hepatology, 21:282-293, Jan 2024. URL: https://doi.org/10.1038/s41575-023-00883-z, doi:10.1038/s41575-023-00883-z. This article has 51 citations.

2. (arguero2024pathophysiologyofgastrooesophageal pages 6-7): Julieta Argüero and Daniel Sifrim. Pathophysiology of gastro-oesophageal reflux disease: implications for diagnosis and management. Nature reviews. Gastroenterology & hepatology, 21:282-293, Jan 2024. URL: https://doi.org/10.1038/s41575-023-00883-z, doi:10.1038/s41575-023-00883-z. This article has 51 citations.

3. (leech2024mucosalneuroimmunemechanisms pages 1-3): Tom Leech and Madusha Peiris. Mucosal neuroimmune mechanisms in gastro-oesophageal reflux disease (gord) pathogenesis. Journal of Gastroenterology, 59:165-178, Jan 2024. URL: https://doi.org/10.1007/s00535-023-02065-9, doi:10.1007/s00535-023-02065-9. This article has 14 citations and is from a domain leading peer-reviewed journal.

4. (chen2024esophagealmicrobialdysbiosis pages 8-12): Songfeng Chen, Dianxuan Jiang, Qianjun Zhuang, Xun Hou, Xingyu Jia, Jing Chen, Huiting Lin, Mengyu Zhang, Niandi Tan, and Yinglian Xiao. Esophageal microbial dysbiosis impairs mucosal barrier integrity via toll-like receptor 2 pathway in patients with gastroesophageal reflux symptoms. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-05878-1, doi:10.1186/s12967-024-05878-1. This article has 6 citations and is from a peer-reviewed journal.

5. (wang2024causalrelationshipbetween pages 5-8): Kui Wang, Suijian Wang, Yuhua Chen, Xinchen Lu, Danshu Wang, Yao Zhang, Wei Pan, Chunhua Zhou, and Duowu Zou. Causal relationship between gut microbiota and risk of gastroesophageal reflux disease: a genetic correlation and bidirectional mendelian randomization study. Frontiers in Immunology, Feb 2024. URL: https://doi.org/10.3389/fimmu.2024.1327503, doi:10.3389/fimmu.2024.1327503. This article has 31 citations and is from a peer-reviewed journal.

6. (jovov2007claudin18adominant pages 3-4): Biljana Jovov, Christina M. Van Itallie, Nicholas J. Shaheen, Johnny L. Carson, Todd M. Gambling, James M. Anderson, and Roy C. Orlando. Claudin-18: a dominant tight junction protein in barrett's esophagus and likely contributor to its acid resistance. American Journal of Physiology-Gastrointestinal and Liver Physiology, 293:G1106-G1113, Dec 2007. URL: https://doi.org/10.1152/ajpgi.00158.2007, doi:10.1152/ajpgi.00158.2007. This article has 171 citations.

7. (moe2024mechanisticinsightson pages 8-10): Kyaw Thu Moe and Kevin Shyong Wei Tan. Mechanistic insights on microbiota-mediated development and progression of esophageal cancer. Cancers, Sep 2024. URL: https://doi.org/10.3390/cancers16193305, doi:10.3390/cancers16193305. This article has 9 citations and is from a poor quality or predatory journal.

8. (leech2024mucosalneuroimmunemechanisms pages 6-7): Tom Leech and Madusha Peiris. Mucosal neuroimmune mechanisms in gastro-oesophageal reflux disease (gord) pathogenesis. Journal of Gastroenterology, 59:165-178, Jan 2024. URL: https://doi.org/10.1007/s00535-023-02065-9, doi:10.1007/s00535-023-02065-9. This article has 14 citations and is from a domain leading peer-reviewed journal.

9. (chen2024esophagealmicrobialdysbiosis pages 1-2): Songfeng Chen, Dianxuan Jiang, Qianjun Zhuang, Xun Hou, Xingyu Jia, Jing Chen, Huiting Lin, Mengyu Zhang, Niandi Tan, and Yinglian Xiao. Esophageal microbial dysbiosis impairs mucosal barrier integrity via toll-like receptor 2 pathway in patients with gastroesophageal reflux symptoms. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-05878-1, doi:10.1186/s12967-024-05878-1. This article has 6 citations and is from a peer-reviewed journal.

10. (chen2024esophagealmicrobialdysbiosis pages 14-14): Songfeng Chen, Dianxuan Jiang, Qianjun Zhuang, Xun Hou, Xingyu Jia, Jing Chen, Huiting Lin, Mengyu Zhang, Niandi Tan, and Yinglian Xiao. Esophageal microbial dysbiosis impairs mucosal barrier integrity via toll-like receptor 2 pathway in patients with gastroesophageal reflux symptoms. Journal of Translational Medicine, Dec 2024. URL: https://doi.org/10.1186/s12967-024-05878-1, doi:10.1186/s12967-024-05878-1. This article has 6 citations and is from a peer-reviewed journal.

11. (wu2024theroleand pages 7-8): Zunan Wu, Shuai Peng, Wensha Huang, Yuling Zhang, Yashi Liu, Xiaoyun Yu, and Lei Shen. The role and function of trpm8 in the digestive system. Biomolecules, 14:877, Jul 2024. URL: https://doi.org/10.3390/biom14070877, doi:10.3390/biom14070877. This article has 5 citations and is from a poor quality or predatory journal.

12. (ismail2025understandingthemechanisms pages 7-9): MA ISMAIL, HA ALTHIYABI, and NM ALOTAIBI. Understanding the mechanisms underlying gastroesophageal reflux disease (gerd) development: a systematic review. Unknown journal, 2025.

13. (yin2023noninvasiveelectricalneuromodulation pages 11-12): Jieyun Yin and Jiande DZ Chen. Noninvasive electrical neuromodulation for gastrointestinal motility disorders. Expert Review of Gastroenterology & Hepatology, 17:1221-1232, Nov 2023. URL: https://doi.org/10.1080/17474124.2023.2288156, doi:10.1080/17474124.2023.2288156. This article has 22 citations and is from a peer-reviewed journal.

14. (zheng2025multidimensionalmechanismsand pages 1-2): Jiajing Zheng and Lin Tao. Multidimensional mechanisms and therapies underlying gastroesophageal reflux disease: focus on immunity, signaling pathways, and the microbiota-gut-brain axis. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1629944, doi:10.3389/fimmu.2025.1629944. This article has 2 citations and is from a peer-reviewed journal.