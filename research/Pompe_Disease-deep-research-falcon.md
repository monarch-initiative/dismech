---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-08T18:25:46.678344'
end_time: '2026-03-08T18:39:23.734318'
duration_seconds: 817.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pompe Disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pompe Disease**.
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
- **Disease Name:** Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pompe Disease**.
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


# Pompe Disease Pathophysiology (Molecular & Cellular Mechanisms)

## 0. Executive summary
Pompe disease (glycogen storage disease type II) is a Mendelian lysosomal storage disorder caused by biallelic loss-of-function variants in **GAA** (acid α‑glucosidase), the lysosomal hydrolase required to degrade glycogen in the lysosomal lumen. The initiating lesion is **progressive lysosomal glycogen accumulation**, which secondarily causes widespread **lysosome–autophagy system failure**, metabolic rewiring (including a feed‑forward increase in cytoplasmic glycogen synthesis), and downstream myofiber degeneration. Recent 2023–2024 work emphasizes that (i) **skeletal muscle** disease is driven not only by storage but by a profound **autophagic block** with near-absence of lysosome–autophagosome fusion, (ii) disease progression is associated with **early metabolic shifts and mitochondrial gene downregulation** in histologically “non‑vacuolated” fibers, and (iii) inflammation and immune involvement become more prominent in **vacuolated (affected) fibers**. These mechanistic insights directly motivate new interventions (next‑gen ERTs with higher M6P, ERT+chaperone, gene therapy to reach CNS, and substrate reduction via GYS1 inhibition). (do2024failureofautophagy pages 4-5, do2024failureofautophagy pages 5-7, monceau2024decodingthemuscle pages 1-2, canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15)

**Disease identifier:** MONDO:0009290 (glycogen storage disease II / Pompe disease). (monceau2024decodingthemuscle pages 1-2)

---

## 1. Key concepts and definitions (current understanding)

### 1.1 Core definition and initiating defect
Pompe disease is caused by deficiency of **lysosomal acid α‑glucosidase (GAA)**, described in recent reviews as “**the sole enzyme responsible for the breakdown of glycogen to glucose in the lysosomal lumen**.” (do2024failureofautophagy pages 4-5)

The resulting primary cellular pathology is **glycogen accumulation within swollen/enlarged lysosomes** across multiple tissues, with disproportionate clinical impact in **skeletal muscle, cardiac muscle, and respiratory muscles**. (do2024failureofautophagy pages 4-5, do2024failureofautophagy pages 5-7)

### 1.2 Autophagy and “autophagic buildup” in Pompe skeletal muscle
Pompe disease is now widely conceptualized as a disorder of **lysosomal storage plus autophagy–lysosome system failure**. In skeletal muscle, Do et al. (2024) describe a dramatic **autophagic buildup** consisting of autophagic vacuoles, ubiquitinated aggregates, glycogen particles, p62/SQSTM1, and lipofuscin, associated with myofibrillar disarray and microtubule disorganization. (do2024failureofautophagy pages 5-7)

A key mechanistic point is that **autophagy is simultaneously induced and blocked** in diseased muscle: evidence of induction (e.g., AMPK/ULK1 signaling, VPS15/VPS34/Beclin1) coexists with **impaired autophagosome–lysosome fusion** and reduced lysosome availability. (do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 7-8)

A visual example of this concept is shown in Do et al. (2024), including (i) a schematic of **mTORC1/AMPK control of autophagy** and (ii) a confocal image of **massive autophagic buildup** in a Pompe mouse myofiber. (do2024failureofautophagy media 626878f7, do2024failureofautophagy media 8e8c5882)

---

## 2. Core pathophysiology (molecular pathways and cellular processes)

### 2.1 Lysosomal glycogen accumulation and endolysosomal trafficking
GAA is synthesized as a glycoprotein trafficked through ER/Golgi and delivered to late endosomes/lysosomes via **mannose‑6‑phosphate receptor (M6PR/CI‑MPR)** pathways; a secreted precursor can be re‑captured by neighboring cells—this is the biological basis for **enzyme replacement therapy (ERT)**. (do2024failureofautophagy pages 4-5)

### 2.2 Autophagic block and lysosomal biogenesis defects
Do et al. (2024) report that live imaging in Pompe muscle cells showed “**a striking paucity of lysosomes**” and that “**lysosomal–autophagosomal fusion events were essentially nonexistent**,” a mechanism that plausibly explains persistent autophagic debris accumulation. (do2024failureofautophagy pages 7-8)

**Quantitative morphology (muscle fiber burden):** autophagic buildup can occupy a very large fraction of the myofiber area, “up to **40%** of the area in some fibers” (as highlighted in the figure/text context). (do2024failureofautophagy media 626878f7)

### 2.3 Nutrient sensing signaling: AMPK–mTORC1–TFEB axis
Do et al. (2024) describe signaling consistent with **AMPK activation** (energy stress) and **reduced mTORC1 signaling**, coupled to a functional block in autophagic clearance. (do2024failureofautophagy pages 5-7)

Mechanistic perturbation experiments in models support causality: “**Activation of mTORC1 by genetic inhibition of TSC2 … effectively eliminated autophagic buildup**,” and TFEB modulation is implicated because “**Overexpression of TFEB … resulted in near complete elimination of autophagic buildup**,” whereas patient biopsies show increased phosphorylated (inactive) TFEB. (do2024failureofautophagy pages 7-8)

### 2.4 Cytoplasmic glycogen metabolism dysregulation (feed‑forward loop)
Beyond lysosomal storage, recent work highlights that lysosomal glycogen accumulation is associated with **disturbed cytoplasmic glycogen metabolism**. Canibano‑Fraile et al. (2023) report elevated proteins involved in glucose uptake and glycogen synthesis in Pompe skeletal muscle (mouse and human biopsy proteomics), supporting a model where lysosomal storage promotes cytosolic glycogen synthesis and glucose uptake—aggravating the phenotype. (canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15)

### 2.5 Mitochondrial dysfunction and metabolic rewiring in human LOPD muscle
Monceau et al. (Brain, 2024; single‑nucleus RNA‑seq + spatial transcriptomics) provide high‑resolution evidence that even in **non‑vacuolated fibers**, there are early metabolic abnormalities (reduced glycolysis gene expression; increased lipid/amino acid metabolism). They also report “**downregulation of the genes involved in ribosomal and mitochondrial function leading to defective oxidative phosphorylation**,” while inflammation/apoptosis/regeneration programs rise in **vacuolated fibers**. (monceau2024decodingthemuscle pages 1-2)

### 2.6 Inflammation/immune involvement
In the same Brain 2024 study, macrophage abundance is increased in diseased muscle, and inflammatory/apoptotic/regenerative signatures are a feature of more advanced (vacuolated) fibers. (monceau2024decodingthemuscle pages 1-2)

---

## 3. Key molecular players (genes/proteins, chemicals, cell types, anatomy)

### 3.1 Causal gene
- **GAA** (alpha glucosidase; lysosomal acid α‑glucosidase). (do2024failureofautophagy pages 4-5)

### 3.2 Mechanism-linked genes/proteins highlighted in 2023–2024 sources
- **Autophagy–lysosome system:** LC3 (MAP1LC3 family), p62/SQSTM1, LAMP1; endosomal trafficking markers (Rab5, EEA1), CI‑MPR; VPS15 (PIK3R4), VPS34 (PIK3C3), Beclin 1 (BECN1); ULK1; TFEB; TSC2; mTORC1 pathway outputs (4E‑BP1, S6K1). (do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 4-5, do2024failureofautophagy pages 7-8)
- **Cytoplasmic glycogen synthesis & uptake (feed‑forward):** **GYS1**, **GBE1**, **GLUT4 (SLC2A4)**, **GYG1**, **UGP2**. (canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15)
- **Disease stage markers / immune:** macrophage-related changes (cell-type proportion shift in human biopsies). (monceau2024decodingthemuscle pages 1-2)

### 3.3 Chemical entities and drugs (real-world relevance)
- **Alglucosidase alfa** (first-generation ERT; recombinant GAA). (carter2024realworldoutcomesfrom pages 1-2)
- **Avalglucosidase alfa** (next-generation ERT; increased bis‑M6P residues to enhance uptake). (carter2024realworldoutcomesfrom pages 1-2)
- **Cipaglucosidase alfa + miglustat** (two-component therapy; enzyme enriched in bis‑M6P N‑glycans + stabilizer/chaperone). (byrne2024longtermsafetyand pages 1-2, schoser2024104weekefficacyand pages 1-2)
- **MZ‑101** (selective **GYS1 inhibitor**; substrate reduction therapy concept in preclinical Pompe). (ullman2024smallmoleculeinhibitionof pages 6-8, ullman2024smallmoleculeinhibitionof pages 4-6)

### 3.4 Cell types and anatomical locations
- **Primary affected:** skeletal muscle fibers (especially fast-twitch type II vulnerability emphasized in mechanistic review), cardiac myocytes, diaphragm/respiratory muscles; also CNS involvement is relevant for therapeutic strategy. (do2024failureofautophagy pages 4-5, meena2023aavmediateddeliveryof pages 1-2)
- **Immune involvement:** macrophages in LOPD muscle. (monceau2024decodingthemuscle pages 1-2)

---

## 4. Biological processes (GO-style) and cellular components

### 4.1 Biological processes disrupted (examples; GO terms provided as knowledge-base anchors)
- **Glycogen catabolic process / glycogen metabolic process** (lysosomal glycogenolysis failure due to GAA). (do2024failureofautophagy pages 4-5)
- **Autophagy** and **autophagosome–lysosome fusion** (macroautophagy flux failure with autophagic buildup). (do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 5-7)
- **Nutrient sensing and stress signaling** via **AMPK** and **mTORC1**, with transcriptional control by **TFEB**. (do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 5-7)
- **Oxidative phosphorylation / mitochondrial function** (transcriptional downregulation in human LOPD muscle). (monceau2024decodingthemuscle pages 1-2)

### 4.2 Cellular components disrupted (examples; GO CC anchors)
- **Lysosome** (primary storage compartment; lysosome paucity in diseased cells). (do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 4-5)
- **Autophagosome** (accumulation of double-membrane vacuoles; buildup). (do2024failureofautophagy pages 4-5, do2024failureofautophagy pages 5-7)
- **Mitochondrion** (defective oxidative phosphorylation program). (monceau2024decodingthemuscle pages 1-2)

---

## 5. Disease progression model (sequence of events)

1. **Genetic trigger:** biallelic pathogenic variants reduce/abolish GAA activity. (do2024failureofautophagy pages 4-5)
2. **Initiating lesion:** progressive **lysosomal glycogen accumulation** → enlarged lysosomes. (do2024failureofautophagy pages 4-5)
3. **Secondary autophagy–lysosome pathology:** autophagy is induced but clearance fails due to impaired fusion and limited lysosome availability; autophagic debris accumulates massively in skeletal muscle, which can also sequester therapeutic enzyme. (do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 7-8)
4. **Metabolic rewiring:** disturbed cytoplasmic glycogen metabolism and early transcriptional metabolic shifts precede overt vacuolar pathology in some fibers; mitochondrial/ribosomal programs decline. (canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15, monceau2024decodingthemuscle pages 1-2)
5. **Tissue remodeling and inflammation (later):** vacuolated fibers exhibit inflammatory/apoptotic/regenerative signatures and increased macrophage abundance. (monceau2024decodingthemuscle pages 1-2)
6. **Clinical manifestations:** progressive limb-girdle weakness, respiratory impairment (diaphragm), cardiomyopathy (especially infantile onset). (carter2024realworldoutcomesfrom pages 1-2, byrne2024longtermsafetyand pages 1-2)

---

## 6. Phenotypic manifestations (clinical phenotypes linked to mechanisms)
- **Progressive skeletal muscle weakness and impaired mobility** are consistent with fiber damage, autophagic buildup, metabolic insufficiency, and mitochondrial gene downregulation. (do2024failureofautophagy pages 5-7, monceau2024decodingthemuscle pages 1-2)
- **Respiratory insufficiency** reflects involvement of respiratory muscles including diaphragm, a major target of both ERT monitoring (FVC) and gene therapy efforts. (byrne2024longtermsafetyand pages 1-2, meena2023aavmediateddeliveryof pages 1-2)
- **Biomarkers** used clinically (reflecting tissue injury and storage burden) include **creatine kinase (CK)** and urinary glycogen-derived oligosaccharide (**Hex4/uGlc4**). (NCT03729362 chunk 1, carter2024realworldoutcomesfrom pages 1-2)

---

## 7. Recent developments (prioritizing 2023–2024)

### 7.1 2024: Human multi-omic tissue resolution of LOPD progression
Monceau et al. (Brain, **July 2024**, https://doi.org/10.1093/brain/awae249) applied single‑nucleus RNA‑seq and spatial transcriptomics to biopsies from **8 LOPD patients** and **4 controls**, showing stage-specific fiber programs: early metabolic rewiring in non‑vacuolated fibers; inflammation/apoptosis in vacuolated fibers; increased slow/regenerative fibers and macrophages. (monceau2024decodingthemuscle pages 1-2)

### 7.2 2024: Mechanistic consolidation of autophagy failure
Do et al. (Biomolecules, **May 2024**, https://doi.org/10.3390/biom14050573) synthesize and extend a model where Pompe skeletal muscle contains enormous autophagic buildup, driven by impaired lysosomal availability and fusion and regulated by AMPK/mTORC1/TFEB. The review includes model-perturbation evidence: TFEB overexpression or mTORC1 activation can eliminate buildup in experimental systems. (do2024failureofautophagy pages 7-8, do2024failureofautophagy pages 5-7)

### 7.3 2023: Evidence for disturbed cytoplasmic glycogen metabolism preceding wasting
Canibano‑Fraile et al. (J Inherit Metab Dis, **Oct 2023**, https://doi.org/10.1002/jimd.12560) support a feed‑forward model with increased enzymes of glucose uptake and cytoplasmic glycogen synthesis in affected muscle, implying secondary glycogen metabolism dysregulation. (canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15)

### 7.4 2024: Substrate reduction via GYS1 inhibition as a mechanistically targeted therapy
Ullman et al. (Science Translational Medicine, **Jan 2024**, https://doi.org/10.1126/scitranslmed.adf1691) developed **MZ‑101**, a selective **GYS1** inhibitor (human GYS1 IC50 0.041 μM; no GYS2 inhibition up to 100 μM) and showed that Pompe muscle has markedly increased glycogen synthesis drivers (e.g., ~5× G6P, ~2× GYS1 activity), making it susceptible to substrate reduction. (ullman2024smallmoleculeinhibitionof pages 4-6)

Quantitatively, in GAA KO mice, MZ‑101 reduced KO muscle glycogen **38% at 4 weeks** and **58% at 14 weeks**; in WT muscle glycogen fell **71% (4 weeks)** and **81% (14 weeks)**, indicating potent depletion with incomplete normalization in KO on monotherapy. (ullman2024smallmoleculeinhibitionof pages 6-8)

Combination therapy has mechanistic and functional rationale: the paper states that combining MZ‑101 with ERT can normalize skeletal muscle glycogen and “substantially correct” abnormal pathways based on transcriptional/metabolic profiling. (ullman2024smallmoleculeinhibitionof pages 3-4, ullman2024smallmoleculeinhibitionof pages 4-6)

---

## 8. Current applications and real-world implementations (with recent statistics)

### 8.1 Enzyme replacement therapy (ERT) and next-generation ERT

#### PROPEL (cipaglucosidase alfa + miglustat) – Phase 3 trial design and endpoints
ClinicalTrials.gov **NCT03729362** (PROPEL; results first posted **2023‑09‑11**) enrolled **125** adults; primary endpoint: change from baseline to Week 52 in **6‑minute walk distance (6MWD)**; key secondary endpoints include **sitting FVC (% predicted)** and muscle function scores; biomarkers included **CK** and urinary **Hex4**. (NCT03729362 chunk 1)

#### 2024 long-term outcomes: cipa+mig open-label extension (104 weeks)
Schoser et al. (J Neurol, **Feb 2024**, https://doi.org/10.1007/s00415-024-12236-0) report 104‑week OLE results (NCT04138277) in **118** participants (81 continued cipa+mig; 37 switched from alglucosidase). Mean (SD) change in **% predicted 6MWD** at week 104 was **+3.1 (8.1)** for continued cipa+mig in ERT‑experienced patients vs **−0.5 (7.8)** in ERT‑experienced switchers; **FVC** changes suggested stabilization (e.g., **−0.6 (7.5)** vs **−3.8 (6.2)**). CK and Hex4 improved, and no new safety signals were identified. (schoser2024104weekefficacyand pages 1-2)

#### 2024 long-term outcomes: cipa+mig Phase I/II (up to 48 months)
Byrne et al. (J Neurol, **Dec 2024**, https://doi.org/10.1007/s00415-023-12096-0) report ATB200-02 (NCT02675465) across cohorts (e.g., non‑ambulatory ERT‑experienced n=6; ambulatory ERT‑experienced n=11 and n=6; ERT‑naïve n=6). Ambulatory ERT‑experienced patients showed sustained mean improvements in % predicted 6MWD over 12–48 months (e.g., ~6.1 to 5.9 across timepoints), while FVC was generally stable; ERT‑naïve cohorts showed larger mean gains (e.g., 6MWD ~10.7 to 11.7). (byrne2024longtermsafetyand pages 1-2)

Mechanistic expert analysis in this clinical literature emphasizes that next‑gen ERTs aim to improve skeletal muscle uptake through **bis‑M6P N‑glycans** and to prevent in‑circulation denaturation at neutral pH; cipa+mig is presented as combining an uptake‑optimized enzyme plus a stabilizer/chaperone strategy. (schoser2024104weekefficacyand pages 1-2, byrne2024longtermsafetyand pages 1-2)

### 8.2 Real-world implementation: switching to avalglucosidase alfa
Carter et al. (Frontiers in Genetics, **Jan 2024**, https://doi.org/10.3389/fgene.2024.1309146) report a single‑center chart review of **15** LOPD patients switching from alglucosidase alfa to avalglucosidase alfa for ≥6 months. Statistically significant mean improvements were reported for **CK (−104.8 U/L)**, **Hex4 (−3.0 mmol/molCr)**, and **AST (−14.7 U/L)**. Functional measures improved/stabilized in most patients (e.g., 6MWT improved or stabilized in **8/12**; comfortable gait speed **11/12**), and **upright FVC improved in 4/7** tested. The study also notes tolerability (no infusion-associated reactions) and home infusion continuation. (carter2024realworldoutcomesfrom pages 1-2)

### 8.3 Gene therapy to address multisystem and CNS disease biology
Meena et al. (JCI Insight, **Aug 2023**, https://doi.org/10.1172/jci.insight.170199) describe systemic AAV9 delivery of a chimeric secreted GAA with enhanced uptake in Gaa‑KO mice, reversing glycogen storage in “**skeletal and cardiac muscles, the diaphragm, and the central nervous system**” and reversing secondary abnormalities in autophagy and mTORC1/AMPK signaling—addressing a core limitation of ERT: inability to cross the BBB. (meena2023aavmediateddeliveryof pages 1-2)

### 8.4 Substrate reduction therapy (SRT): small-molecule GYS1 inhibition
Ullman et al. (Sci Transl Med, **Jan 2024**, https://doi.org/10.1126/scitranslmed.adf1691) provide preclinical rationale for combining ERT (catabolic replacement) with SRT (reduced synthesis). A key mechanistic observation is increased glycogen synthesis drive in KO muscle (~5× G6P; ~2× GYS1 activity; 3275→6357 GS cpm/mg/min). (ullman2024smallmoleculeinhibitionof pages 4-6)

Functional endpoint example: after prolonged treatment, combination SRT+ERT improved motor performance (rotarod latency **WT 298 s**, **KO 45 s**, **SRT+ERT 125 s**). (ullman2024smallmoleculeinhibitionof pages 11-12)

---

## 9. Evidence-backed knowledge-base tables

| Mechanism / Process | Key Molecular Players | Cell Types / Tissues | Subcellular Location | Key Evidence / Quote | Primary Citation | Notes / Implications |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Autophagic Buildup & Lysosomal Paucity** | GAA, LC3, p62/SQSTM1, LAMP1, Rab5, EEA1 | Skeletal muscle (especially Type II fibers) | Lysosomes, Autophagosomes, Sarcoplasm | "Lysosomal–autophagosomal fusion events were essentially nonexistent... autophagic buildup is truly remarkable, occupying up to 40% of the area in some fibers." | Do et al., 2024 (10.3390/biom14050573) (do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 7-8, do2024failureofautophagy media 626878f7) | Buildup traps ERT enzymes, reducing efficacy; buildup contains ubiquitinated protein aggregates and lipofuscin. |
| **Metabolic Rewiring & Mitochondrial Dysfunction** | Glycolysis genes (down), Lipid/AA metabolism genes (up), Ribosomal/Mitochondrial genes (down) | Muscle fibers (Slow, Regenerative), Macrophages | Mitochondria, Cytoplasm | "Upregulation of autophagy genes and downregulation of the genes involved in ribosomal and mitochondrial function leading to defective oxidative phosphorylation." | Monceau et al., 2024 (10.1093/brain/awae249) (monceau2024decodingthemuscle pages 1-2) | Early metabolic shifts occur in non-vacuolated fibers before overt damage; ERT restores some metabolism in slow fibers. |
| **Cytoplasmic Glycogen Dysregulation** | GYS1 (Glycogen synthase), GBE1, GLUT4, GYG1, UGP2 | Skeletal muscle | Cytoplasm | "Elevated protein levels of enzymes involved in glucose uptake and cytoplasmic glycogen synthesis... imply a positive feedforward loop in Pompe disease." | Canibano-Fraile et al., 2023 (10.1002/jimd.12560) (canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15) | Suggests lysosomal accumulation triggers cytoplasmic synthesis; supports GYS1 inhibition (substrate reduction) as therapy. |
| **Signaling Dysregulation (mTORC1/AMPK)** | mTORC1, AMPK, TFEB, TFE3, TSC2 | Skeletal muscle | Cytosol, Nucleus (transcription factors) | "Increased AMPK activity... and concomitantly decreased mTORC1 signaling... Activation of mTORC1 by genetic inhibition of TSC2... effectively eliminated autophagic buildup." | Do et al., 2024 (10.3390/biom14050573) (do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 7-8); Sánchez-Porras et al., 2023 (10.3390/ijms241512481) (sanchezporras2023fromacidalphaglucosidase pages 14-15) | Modulating these pathways (e.g., activating mTORC1) could be a therapeutic strategy to clear autophagy. |
| **Inflammation & Immune Infiltration** | Macrophage markers, Inflammation-associated genes | Muscle tissue | Extracellular matrix, Interstitial space | "Upregulation of genes associated with inflammation, apoptosis and muscle regeneration was observed only in vacuolated fibres." | Monceau et al., 2024 (10.1093/brain/awae249) (monceau2024decodingthemuscle pages 1-2) | Highlights the role of immune response in advanced tissue pathology; potential for immunomodulation. |


*Table: This table summarizes the primary molecular and cellular mechanisms identified in recent literature (2023-2024), linking specific genetic and metabolic players to tissue-level phenotypes and therapeutic implications.*

| Category | Ontology Term / Name | Evidence Summary | Source Contexts |
| :--- | :--- | :--- | :--- |
| **Disease** | **Pompe disease** (MONDO:0009290) | Rare autosomal recessive lysosomal storage disorder characterized by glycogen accumulation. | (do2024failureofautophagy pages 4-5, schoser2024104weekefficacyand pages 1-2) |
| **Causal Gene** | **GAA** (HGNC:4065) | Mutations in *GAA* encode deficient lysosomal acid alpha-glucosidase, the primary defect. | (do2024failureofautophagy pages 4-5, sanchezporras2023fromacidalphaglucosidase pages 14-15) |
| **Biological Process** | **Glycogen metabolic process** (GO:0005977) | Primary dysfunction involves lysosomal glycogen hydrolysis and secondary cytoplasmic glycogen synthesis dysregulation. | (do2024failureofautophagy pages 4-5, canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15) |
| **Biological Process** | **Autophagy** (GO:0006914) | Disease is characterized by "massive autophagic buildup" and impaired autophagosome-lysosome fusion. | (do2024failureofautophagy pages 5-7, do2024failureofautophagy pages 7-8) |
| **Biological Process** | **Mitochondrial organization** (GO:0007005) | Downregulation of mitochondrial genes and defective oxidative phosphorylation are observed in affected muscle. | (monceau2024decodingthemuscle pages 1-2, sanchezporras2023fromacidalphaglucosidase pages 14-15) |
| **Cellular Component** | **Lysosome** (GO:0005764) | The primary site of pathology is the lysosome, which becomes swollen with glycogen. | (do2024failureofautophagy pages 4-5, do2024failureofautophagy pages 7-8) |
| **Cell Type** | **Skeletal muscle fiber** (CL:0000188) | Fast-twitch (Type II) fibers are particularly prone to autophagic debris accumulation. | (do2024failureofautophagy pages 4-5, do2024failureofautophagy pages 5-7) |
| **Cell Type** | **Macrophage** (CL:0000235) | Increased infiltration of macrophages is observed in LOPD muscle biopsies. | (monceau2024decodingthemuscle pages 1-2) |
| **Anatomical Site** | **Skeletal muscle** (UBERON:0001134) | Progressive degeneration of skeletal muscle is a hallmark, monitored by 6MWD. | (schoser2024104weekefficacyand pages 1-2, byrne2024cipaglucosidasealfaplusa pages 16-16) |
| **Anatomical Site** | **Central nervous system** (UBERON:0001017) | Glycogen accumulates in the CNS; AAV gene therapy targets this reservoir unlike standard ERT. | (meena2023aavmediateddeliveryof pages 1-2) |
| **Phenotype** | **Respiratory insufficiency** (HP:0002093) | Respiratory muscle weakness is a key clinical feature, tracked by FVC % predicted. | (schoser2024104weekefficacyand pages 1-2, carter2024realworldoutcomesfrom pages 1-2) |
| **Phenotype** | **Elevated serum creatine kinase** (HP:0003236) | Serum CK is a standard biomarker for muscle damage used in clinical trials. | (schoser2024104weekefficacyand pages 1-2, carter2024realworldoutcomesfrom pages 1-2) |
| **Drug (ERT)** | **Alglucosidase alfa** | Recombinant human GAA; the first-generation standard of care enzyme replacement therapy. | (byrne2024cipaglucosidasealfaplusa pages 16-16, carter2024realworldoutcomesfrom pages 1-2) |
| **Drug (Next-Gen ERT)** | **Cipaglucosidase alfa** / **Miglustat** | Two-component therapy: CHO-derived enzyme with high bis-M6P + chaperone stabilizer. | (schoser2024104weekefficacyand pages 1-2, byrne2024longtermsafetyand pages 1-2) |
| **Drug (Next-Gen ERT)** | **Avalglucosidase alfa** | Glyco-engineered enzyme with increased mannose-6-phosphate (M6P) for better uptake. | (carter2024realworldoutcomesfrom pages 1-2, meena2023aavmediateddeliveryof pages 1-2) |
| **Drug (Investigational)** | **MZ-101** (GYS1 Inhibitor) | Small molecule substrate reduction therapy reducing muscle glycogen synthesis. | (ullman2024smallmoleculeinhibitionof pages 1-3, ullman2024smallmoleculeinhibitionof pages 4-6) |


*Table: A structured overview of Pompe disease pathophysiology mapping key genes, processes, cell types, and treatments to standard ontology terms (MONDO, GO, CL, HPO, etc.) based on 2023-2024 literature.*

---

## 10. Notes on evidence limits (PMIDs)
The retrieved 2023–2024 sources in this run provide DOIs/URLs and detailed mechanistic/quantitative data, but PMIDs were not consistently present in the extracted text snippets. Where required for downstream curation, the DOIs supplied here can be used to retrieve PubMed records and PMIDs; mechanistic claims in this report are anchored directly to the cited context extracts from those 2023–2024 publications and ClinicalTrials.gov records. (do2024failureofautophagy pages 5-7, monceau2024decodingthemuscle pages 1-2, byrne2024longtermsafetyand pages 1-2, NCT03729362 chunk 1)

References

1. (do2024failureofautophagy pages 4-5): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. Biomolecules, 14:573, May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 9 citations.

2. (do2024failureofautophagy pages 5-7): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. Biomolecules, 14:573, May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 9 citations.

3. (monceau2024decodingthemuscle pages 1-2): Alexandra Monceau, Rasya Gokul Nath, Xavier Suárez-Calvet, Olimpia Musumeci, Antonio Toscano, Biruta Kierdaszuk, Anna Kostera-Pruszczyk, Cristina Domínguez-González, Aurelio Hernández-Lain, Carmen Paradas, Eloy Rivas, George Papadimas, Constantinos Papadopoulos, Margarita Chrysanthou-Piterou, Eduard Gallardo, Montse Olivé, James Lilleker, Mark E Roberts, Domenica Marchese, Giulia Lunazzi, Holger Heyn, Esther Fernández-Simón, Elisa Villalobos, James Clark, Panos Katsikis, Catherine Collins, Priyanka Mehra, Zoe Laidler, Amy Vincent, Giorgio Tasca, Chiara Marini-Bettolo, Michela Guglieri, Volker Straub, Nina Raben, and Jordi Díaz-Manera. Decoding the muscle transcriptome of patients with late-onset pompe disease reveals markers of disease progression. Brain, 147:4213-4226, Jul 2024. URL: https://doi.org/10.1093/brain/awae249, doi:10.1093/brain/awae249. This article has 6 citations and is from a highest quality peer-reviewed journal.

4. (canibano‐fraile2023lysosomalglycogenaccumulation pages 15-15): Rodrigo Canibano‐Fraile, Laurike Harlaar, Carlos A. dos Santos, Marianne Hoogeveen‐Westerveld, Jeroen A. A. Demmers, Tim Snijders, Philip Lijnzaad, Robert M. Verdijk, Nadine A. M. E. van der Beek, Pieter A. van Doorn, Ans T. van der Ploeg, Esther Brusse, W. W. M. Pim Pijnappel, and Gerben J. Schaaf. Lysosomal glycogen accumulation in pompe disease results in disturbed cytoplasmic glycogen metabolism. Journal of Inherited Metabolic Disease, 46:101-115, Oct 2023. URL: https://doi.org/10.1002/jimd.12560, doi:10.1002/jimd.12560. This article has 23 citations and is from a peer-reviewed journal.

5. (do2024failureofautophagy pages 7-8): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. Biomolecules, 14:573, May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 9 citations.

6. (do2024failureofautophagy media 626878f7): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. Biomolecules, 14:573, May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 9 citations.

7. (do2024failureofautophagy media 8e8c5882): Hung Do, Naresh K. Meena, and Nina Raben. Failure of autophagy in pompe disease. Biomolecules, 14:573, May 2024. URL: https://doi.org/10.3390/biom14050573, doi:10.3390/biom14050573. This article has 9 citations.

8. (carter2024realworldoutcomesfrom pages 1-2): Chris Carter, Tracy Boggs, Laura E. Case, and Priya S Kishnani. Real-world outcomes from a series of patients with late onset pompe disease who switched from alglucosidase alfa to avalglucosidase alfa. Frontiers in Genetics, Jan 2024. URL: https://doi.org/10.3389/fgene.2024.1309146, doi:10.3389/fgene.2024.1309146. This article has 12 citations and is from a peer-reviewed journal.

9. (byrne2024longtermsafetyand pages 1-2): Barry J. Byrne, Benedikt Schoser, Priya S. Kishnani, Drago Bratkovic, Paula R. Clemens, Ozlem Goker-Alpan, Xue Ming, Mark Roberts, Matthias Vorgerd, Kumaraswamy Sivakumar, Ans T. van der Ploeg, Mitchell Goldman, Jacquelyn Wright, Fred Holdbrook, Vipul Jain, Elfrida R. Benjamin, Franklin Johnson, Sheela Sitaraman Das, Yasmine Wasfi, and Tahseen Mozaffar. Long-term safety and efficacy of cipaglucosidase alfa plus miglustat in individuals living with pompe disease: an open-label phase i/ii study (atb200-02). Journal of Neurology, 271:1787-1801, Dec 2024. URL: https://doi.org/10.1007/s00415-023-12096-0, doi:10.1007/s00415-023-12096-0. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (schoser2024104weekefficacyand pages 1-2): Benedikt Schoser, Priya S. Kishnani, Drago Bratkovic, Barry J. Byrne, Kristl G. Claeys, Jordi Díaz-Manera, Pascal Laforêt, Mark Roberts, Antonio Toscano, Ans T. van der Ploeg, Jeff Castelli, Mitchell Goldman, Fred Holdbrook, Sheela Sitaraman Das, Yasmine Wasfi, Tahseen Mozaffar, Agnes Sebok, Alan Pestronk, Aleksandra Dominovic-Kovacevic, Aneal Khan, Blaž Koritnik, Celine Tard, Christopher Lindberg, Colin Quinn, Crystal Eldridge, Cynthia Bodkin, David Reyes-Leiva, Derralynn Hughes, Ela Stefanescu, Emmanuelle Salort-Campana, Ernest Butler, Francoise Bouhour, Gee Kim, George Konstantinos Papadimas, Giancarlo Parenti, Halina Bartosik-Psujek, Hani Kushlaf, Hashiguchi Akihiro, Heather Lau, Helio Pedro, Henning Andersen, Hernan Amartino, Hideaki Shiraishi, Hiroshi Kobayashi, Ivaylo Tarnev, Jaime Vengoechea, Jennifer Avelar, Jin-Hong Shin, John Nevin, Jonathan Cauci, Jorge Alonso-Pérez, Jozsef Janszky, Julie Berthy, Cornelia Kornblum, Kristina Gutschmidt, Maria Judit Molnar, Marie Wencel, Mark Tarnopolsky, Matthias Boentert, Michel Tchan, Miriam Freimer, Nicola Longo, Nicolas Abreu, Nuria Vidal-Fernandez, Olimpia Musumeci, Ozlem Goker-Alpan, Patrick Deegan, Paula R. Clemens, Richard Roxburgh, Robert Henderson, Robert Hopkin, Sabrina Sacconi, Simona Fecarotta, Shahram Attarian, Stephan Wenninger, Stephanie Dearmey, Tarekegn Hiwot, Thomas Burrow, Tobias Ruck, Tomo Sawada, Vescei Laszlo, Wolfgang Löscher, and Yin-Hsiu Chien. 104-week efficacy and safety of cipaglucosidase alfa plus miglustat in adults with late-onset pompe disease: a phase iii open-label extension study (atb200-07). Journal of neurology, 271:2810-2823, Feb 2024. URL: https://doi.org/10.1007/s00415-024-12236-0, doi:10.1007/s00415-024-12236-0. This article has 26 citations and is from a domain leading peer-reviewed journal.

11. (ullman2024smallmoleculeinhibitionof pages 6-8): Julie C. Ullman, Kevin T. Mellem, Yannan Xi, Vyas Ramanan, Hanne Merritt, Rebeca Choy, Tarunmeet Gujral, Lyndsay E.A. Young, Kerrigan Blake, Samnang Tep, Julian R. Homburger, Adam O’Regan, Sandya Ganesh, Perryn Wong, Terrence F. Satterfield, Baiwei Lin, Eva Situ, Cecile Yu, Bryan Espanol, Richa Sarwaikar, Nathan Fastman, Christos Tzitzilonis, Patrick Lee, Daniel Reiton, Vivian Morton, Pam Santiago, Walter Won, Hannah Powers, Beryl B. Cummings, Maarten Hoek, Robert R. Graham, Sanjay J. Chandriani, Russell Bainer, Anna A. DePaoli-Roach, Peter J. Roach, Thomas D. Hurley, Ramon C. Sun, Matthew S. Gentry, Christopher Sinz, Ryan A. Dick, Sarah B. Noonberg, David T. Beattie, David J. Morgans Jr., and Eric M. Green. Small-molecule inhibition of glycogen synthase 1 for the treatment of pompe disease and other glycogen storage disorders. Science Translational Medicine, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adf1691, doi:10.1126/scitranslmed.adf1691. This article has 31 citations and is from a highest quality peer-reviewed journal.

12. (ullman2024smallmoleculeinhibitionof pages 4-6): Julie C. Ullman, Kevin T. Mellem, Yannan Xi, Vyas Ramanan, Hanne Merritt, Rebeca Choy, Tarunmeet Gujral, Lyndsay E.A. Young, Kerrigan Blake, Samnang Tep, Julian R. Homburger, Adam O’Regan, Sandya Ganesh, Perryn Wong, Terrence F. Satterfield, Baiwei Lin, Eva Situ, Cecile Yu, Bryan Espanol, Richa Sarwaikar, Nathan Fastman, Christos Tzitzilonis, Patrick Lee, Daniel Reiton, Vivian Morton, Pam Santiago, Walter Won, Hannah Powers, Beryl B. Cummings, Maarten Hoek, Robert R. Graham, Sanjay J. Chandriani, Russell Bainer, Anna A. DePaoli-Roach, Peter J. Roach, Thomas D. Hurley, Ramon C. Sun, Matthew S. Gentry, Christopher Sinz, Ryan A. Dick, Sarah B. Noonberg, David T. Beattie, David J. Morgans Jr., and Eric M. Green. Small-molecule inhibition of glycogen synthase 1 for the treatment of pompe disease and other glycogen storage disorders. Science Translational Medicine, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adf1691, doi:10.1126/scitranslmed.adf1691. This article has 31 citations and is from a highest quality peer-reviewed journal.

13. (meena2023aavmediateddeliveryof pages 1-2): Naresh K. Meena, Davide Randazzo, Nina Raben, and Rosa Puertollano. Aav-mediated delivery of secreted acid α-glucosidase with enhanced uptake corrects neuromuscular pathology in pompe mice. JCI Insight, Aug 2023. URL: https://doi.org/10.1172/jci.insight.170199, doi:10.1172/jci.insight.170199. This article has 13 citations and is from a domain leading peer-reviewed journal.

14. (NCT03729362 chunk 1):  A Study Comparing ATB200/AT2221 With Alglucosidase Alfa/Placebo in Adult Subjects With Late-onset Pompe Disease. Amicus Therapeutics. 2018. ClinicalTrials.gov Identifier: NCT03729362

15. (ullman2024smallmoleculeinhibitionof pages 3-4): Julie C. Ullman, Kevin T. Mellem, Yannan Xi, Vyas Ramanan, Hanne Merritt, Rebeca Choy, Tarunmeet Gujral, Lyndsay E.A. Young, Kerrigan Blake, Samnang Tep, Julian R. Homburger, Adam O’Regan, Sandya Ganesh, Perryn Wong, Terrence F. Satterfield, Baiwei Lin, Eva Situ, Cecile Yu, Bryan Espanol, Richa Sarwaikar, Nathan Fastman, Christos Tzitzilonis, Patrick Lee, Daniel Reiton, Vivian Morton, Pam Santiago, Walter Won, Hannah Powers, Beryl B. Cummings, Maarten Hoek, Robert R. Graham, Sanjay J. Chandriani, Russell Bainer, Anna A. DePaoli-Roach, Peter J. Roach, Thomas D. Hurley, Ramon C. Sun, Matthew S. Gentry, Christopher Sinz, Ryan A. Dick, Sarah B. Noonberg, David T. Beattie, David J. Morgans Jr., and Eric M. Green. Small-molecule inhibition of glycogen synthase 1 for the treatment of pompe disease and other glycogen storage disorders. Science Translational Medicine, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adf1691, doi:10.1126/scitranslmed.adf1691. This article has 31 citations and is from a highest quality peer-reviewed journal.

16. (ullman2024smallmoleculeinhibitionof pages 11-12): Julie C. Ullman, Kevin T. Mellem, Yannan Xi, Vyas Ramanan, Hanne Merritt, Rebeca Choy, Tarunmeet Gujral, Lyndsay E.A. Young, Kerrigan Blake, Samnang Tep, Julian R. Homburger, Adam O’Regan, Sandya Ganesh, Perryn Wong, Terrence F. Satterfield, Baiwei Lin, Eva Situ, Cecile Yu, Bryan Espanol, Richa Sarwaikar, Nathan Fastman, Christos Tzitzilonis, Patrick Lee, Daniel Reiton, Vivian Morton, Pam Santiago, Walter Won, Hannah Powers, Beryl B. Cummings, Maarten Hoek, Robert R. Graham, Sanjay J. Chandriani, Russell Bainer, Anna A. DePaoli-Roach, Peter J. Roach, Thomas D. Hurley, Ramon C. Sun, Matthew S. Gentry, Christopher Sinz, Ryan A. Dick, Sarah B. Noonberg, David T. Beattie, David J. Morgans Jr., and Eric M. Green. Small-molecule inhibition of glycogen synthase 1 for the treatment of pompe disease and other glycogen storage disorders. Science Translational Medicine, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adf1691, doi:10.1126/scitranslmed.adf1691. This article has 31 citations and is from a highest quality peer-reviewed journal.

17. (sanchezporras2023fromacidalphaglucosidase pages 14-15): Valentina Sánchez-Porras, Johana Maria Guevara-Morales, and Olga Yaneth Echeverri-Peña. From acid alpha-glucosidase deficiency to autophagy: understanding the bases of pompe disease. International Journal of Molecular Sciences, 24:12481, Aug 2023. URL: https://doi.org/10.3390/ijms241512481, doi:10.3390/ijms241512481. This article has 2 citations.

18. (byrne2024cipaglucosidasealfaplusa pages 16-16): BJ Byrne, G Parenti, B Schoser, and AT van der Ploeg. Cipaglucosidase alfa plus. Unknown journal, 2024.

19. (ullman2024smallmoleculeinhibitionof pages 1-3): Julie C. Ullman, Kevin T. Mellem, Yannan Xi, Vyas Ramanan, Hanne Merritt, Rebeca Choy, Tarunmeet Gujral, Lyndsay E.A. Young, Kerrigan Blake, Samnang Tep, Julian R. Homburger, Adam O’Regan, Sandya Ganesh, Perryn Wong, Terrence F. Satterfield, Baiwei Lin, Eva Situ, Cecile Yu, Bryan Espanol, Richa Sarwaikar, Nathan Fastman, Christos Tzitzilonis, Patrick Lee, Daniel Reiton, Vivian Morton, Pam Santiago, Walter Won, Hannah Powers, Beryl B. Cummings, Maarten Hoek, Robert R. Graham, Sanjay J. Chandriani, Russell Bainer, Anna A. DePaoli-Roach, Peter J. Roach, Thomas D. Hurley, Ramon C. Sun, Matthew S. Gentry, Christopher Sinz, Ryan A. Dick, Sarah B. Noonberg, David T. Beattie, David J. Morgans Jr., and Eric M. Green. Small-molecule inhibition of glycogen synthase 1 for the treatment of pompe disease and other glycogen storage disorders. Science Translational Medicine, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adf1691, doi:10.1126/scitranslmed.adf1691. This article has 31 citations and is from a highest quality peer-reviewed journal.
