---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-18T23:09:37.586149'
end_time: '2026-03-18T23:22:19.122667'
duration_seconds: 761.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: RPGR-Related Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** RPGR-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **RPGR-Related Retinopathy**.
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
- **Disease Name:** RPGR-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **RPGR-Related Retinopathy**.
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


## Research Report: Pathophysiology of RPGR-Related Retinopathy (RPGR-associated X-linked retinal dystrophy)

### Target disease and identifiers
- **Disease:** RPGR-related retinopathy (RPGR-associated X-linked retinitis pigmentosa / cone–rod dystrophy spectrum)
- **MONDO mapping (closest available in retrieved evidence):** **retinitis pigmentosa (MONDO:0019200)** with specific subtypes (e.g., **retinitis pigmentosa 3 (MONDO:0010227)**) linked to **RPGR** in Open Targets (mcdonald2024retinalciliopathiesand pages 6-7).

### Executive mechanistic summary (current understanding)
RPGR-related retinopathy is best understood as a **photoreceptor ciliopathy** driven by loss-of-function or dysfunctional **RPGR (retinitis pigmentosa GTPase regulator)** isoforms—particularly the photoreceptor-enriched **RPGRORF15**—leading to **impaired connecting-cilium/transition-zone function**, **mis-trafficking of outer-segment proteins (including opsins)**, **dysregulated cytoskeletal remodeling (actin/cofilin)** essential for outer-segment disc morphogenesis and turnover, and **post-translational modification (PTM) disturbances** (notably **glutamylation**) that destabilize ciliary architecture and intraflagellar transport (IFT). These cellular defects culminate in progressive rod and cone dysfunction and photoreceptor cell death. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, mcdonald2024retinalciliopathiesand pages 18-20, megaw2024ciliarytipactin pages 1-2, mercey2024glutamylationimbalanceimpairs pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

---

## 1) Key concepts and definitions (core pathophysiology)

### 1.1 Disease definition and clinical spectrum
- RPGR-related disease is typically an **X-linked recessive** inherited retinal degeneration with **childhood onset** and **severe visual impairment by mid-adulthood** in many affected males. (Publication date: Oct 2023; URL: https://doi.org/10.4103/sjopt.sjopt_168_23) (wongchaisuwat2023retinitispigmentosagtpase pages 1-2)
- Phenotypes span **rod–cone dystrophy (XLRP)** as the common presentation, but also **cone–rod dystrophy (CRD)** and **cone dystrophy**, with strong genotype–phenotype structure across RPGR regions (including distal ORF15 enrichment in cone-dominant presentations). (birch2023overcomingthechallenges pages 2-4, benson2023rpgrdeepphenotyping pages 1-2, hadalin2023geneticcharacteristicsand pages 1-2)

### 1.2 The photoreceptor connecting cilium as the central disease compartment
Photoreceptors are highly specialized ciliated neurons in which the **outer segment** is a modified primary cilium; the **connecting cilium (CC)** functions as the **gateway** for protein trafficking between inner and outer segments. RPGR localizes to this compartment and its dysfunction disrupts this gate, producing downstream photoreceptor failure. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, sladen2024aavrpgrgenetherapy pages 1-2)

### 1.3 RPGR isoforms and mutation hotspot biology
- RPGR has many splice isoforms; the **retina-predominant RPGRORF15** contains a repetitive, purine-rich ORF15 exon that is a major mutational hotspot and technically difficult to sequence. (Publication date: Jun 2023; URL: https://doi.org/10.1167/tvst.12.6.5) (birch2023overcomingthechallenges pages 2-4)
- In a large clinical sequencing cohort of **1,033 tests**, pathogenic/likely pathogenic variants were enriched in **exon 15/ORF15**, with most being **frameshift or nonsense**. (Publication date: Jan 2024; URL: https://doi.org/10.63500/mv_v30_49) (hadalin2023geneticcharacteristicsand pages 1-2)

---

## 2) Molecular and cellular mechanisms underlying disease progression

### 2.1 Dysregulated ciliary trafficking → opsin mislocalization
A dominant mechanistic theme is that RPGR participates in **ciliary trafficking complexes** at the CC/transition zone and centrosome, enabling correct localization of phototransduction proteins. A review of RPGR biology highlights interacting partners consistent with this role (e.g., **RAB8A, RPGRIP1, CEP290, PDE6D**), supporting a trafficking/transition-zone complex model. (Publication date: Oct 2023; URL: https://doi.org/10.4103/sjopt.sjopt_168_23) (wongchaisuwat2023retinitispigmentosagtpase pages 2-3)

Human retinal organoid evidence provides mechanistic confirmation: AAV-mediated RPGR supplementation in RPGR-deficient retinal organoids restored RPGR localization to the CC and corrected **rhodopsin mislocalization**, consistent with trafficking failure as a proximal cellular defect. (Publication date: Feb 2024; URL: https://doi.org/10.3390/ijms25031839) (sladen2024aavrpgrgenetherapy pages 1-2)

**Ontology-ready biological processes (GO candidates):**
- **Cilium-dependent protein transport / ciliary trafficking** (e.g., intraflagellar transport-related processes) (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, mercey2024glutamylationimbalanceimpairs pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

### 2.2 RPGR–actin/cofilin axis in disc genesis and outer-segment turnover (major 2024 advance)
A 2024 Nature Communications mechanistic study links RPGR directly to **actin dynamics at the photoreceptor cilium tip**, a process needed for disc formation and outer-segment integrity. The authors report that disc genesis is driven by actin-mediated membrane remodeling and that RPGR **“regulates actin-binding protein activity central to this process”** and **binds the actin-severing protein cofilin** in distal cilia, regulating its activity. (Publication date: May 2024; URL: https://doi.org/10.1038/s41467-024-48639-w) (megaw2024ciliarytipactin pages 1-2)

They further report that in Rpgr models, disturbed actin dynamics lead to **“aborted membrane shedding as ectosome-like vesicles, photoreceptor death and visual loss.”** (megaw2024ciliarytipactin pages 1-2)

A schematic of the implicated subcellular site (connecting-cilium tip and nascent basal discs) is shown in the figure excerpted from this study. (megaw2024ciliarytipactin media e7ecfeb0)

**Ontology-ready biological processes (GO candidates):**
- **Actin cytoskeleton organization**
- **Cilium morphogenesis / cilium organization**
- **Membrane remodeling / vesicle formation at cilium tip (ectocytosis-like)** (megaw2024ciliarytipactin pages 1-2, megaw2024ciliarytipactin media e7ecfeb0)

### 2.3 Post-translational modification: RPGRORF15 glutamylation and the TTLL5 pathway
Multiple sources converge on the importance of **glutamylation** for RPGRORF15 and/or the photoreceptor cilium:
- Review-level synthesis notes RPGRORF15 glutamylation is mediated by the glutamylation enzyme **TTLL5**, and TTLL5 loss-of-function can produce an RPGR-like retinal phenotype, implicating glutamylation defects in disease. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, mcdonald2024retinalciliopathiesand pages 18-20)
- In RPGR knockout retinal organoids, AAV-RPGR supplementation restored RPGR expression/localization and vector-derived RPGR showed **WT-like glutamylation**, linking glutamylation restoration with corrected opsin localization. (sladen2024aavrpgrgenetherapy pages 1-2)

**Chemical entity (CHEBI):**
- Glutamylation involves addition of glutamate residues (e.g., **L-glutamate; CHEBI:29987**) as a PTM concept (supported mechanistically by glutamylation-focused sources). (mercey2024glutamylationimbalanceimpairs pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

### 2.4 Tubulin PTM imbalance disrupts ciliary architecture and reduces IFT/RPGR levels
A 2024 EMBO Journal paper provides direct mechanistic evidence that altered tubulin PTM balance (polyglutamylation) at the connecting cilium disrupts photoreceptor ciliary architecture and ciliary trafficking machinery, with associated reduction in RPGR abundance. Hyperglutamylation models displayed outer-segment architectural defects (e.g., loss of bulge region, distal axoneme destabilization), and the authors report reduced levels of **intrfla gellar transport proteins** along with reduced **RPGR**. (Publication date: Nov 2024; URL: https://doi.org/10.1038/s44318-024-00284-1) (mercey2024glutamylationimbalanceimpairs pages 1-2)

**Ontology-ready biological processes (GO candidates):**
- **Microtubule-based process**
- **Post-translational protein modification (tubulin polyglutamylation)**
- **Intraflagellar transport** (mercey2024glutamylationimbalanceimpairs pages 1-2)

---

## 3) Key molecular players (and where they act)

### 3.1 Genes/proteins (HGNC symbols) with mechanistic implication
**Core causal gene**
- **RPGR (HGNC: 10273; “retinitis pigmentosa GTPase regulator”)**: central ciliary protein at the photoreceptor CC/transition zone with roles in trafficking and cytoskeletal regulation. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, sladen2024aavrpgrgenetherapy pages 1-2)

**Mechanism-linked interactors / pathway components (implicated in recent synthesis and/or experiments)**
- **RAB8A** (small GTPase, ciliary trafficking association) (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, mcdonald2024retinalciliopathiesand pages 18-20)
- **RPGRIP1 / CEP290 / PDE6D** (ciliary/transition zone and trafficking-associated partners) (wongchaisuwat2023retinitispigmentosagtpase pages 2-3)
- **TTLL5** (glutamylation-related enzyme stabilizing/functionalizing RPGRORF15; linked to RPGR-like phenotype when perturbed) (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, mcdonald2024retinalciliopathiesand pages 18-20)
- **Cofilin (actin-severing; RPGR binding partner in distal cilia)** (megaw2024ciliarytipactin pages 1-2)
- **IFT proteins** (reduced when polyglutamylation is imbalanced; linked to cilium trafficking defects) (mercey2024glutamylationimbalanceimpairs pages 1-2)

### 3.2 Cell types (Cell Ontology; CL) primarily affected
- **Rod photoreceptor cell (CL:0000210)** and **cone photoreceptor cell (CL:0000211)** are primary targets of disease mechanisms (ciliary trafficking failure; disc genesis defects; opsin mislocalization; death). (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, megaw2024ciliarytipactin pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)
- Secondary retinal support-cell contributions are discussed in ciliopathy context (e.g., RPE primary cilium, Müller glia interactions) but the dominant RPGR mechanisms highlighted here are photoreceptor-intrinsic. (mcdonald2024retinalciliopathiesand pages 6-7)

### 3.3 Anatomical locations (UBERON)
- **Retina (UBERON:0000966)**, particularly the **outer retina / photoreceptor layer** and **macula** as assessed by OCT biomarkers. (christou2024establishingclinicaltrial pages 1-2, christou2024establishingclinicaltrial pages 2-4)
- Subcellular retina compartments central to pathophysiology: connecting cilium between inner/outer segments and the outer segment disc compartment. (megaw2024ciliarytipactin pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

### 3.4 Cellular components (GO Cellular Component candidates)
- **Cilium / photoreceptor connecting cilium / transition zone** (RPGR localization; trafficking gateway) (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, sladen2024aavrpgrgenetherapy pages 1-2)
- **Ciliary tip / distal axoneme** (site of disc genesis regulation by RPGR–cofilin; architecture altered by PTM imbalance) (megaw2024ciliarytipactin pages 1-2, mercey2024glutamylationimbalanceimpairs pages 1-2, megaw2024ciliarytipactin media e7ecfeb0)
- **Outer segment discs / nascent basal discs** (disc genesis and turnover) (megaw2024ciliarytipactin media e7ecfeb0)

---

## 4) Disease progression: sequence of events (molecular → clinical)

### Proposed progression model (integrating 2023–2024 evidence)
1. **Primary insult:** Germline RPGR pathogenic variant (often in ORF15) alters RPGRORF15 abundance, localization, or PTM state (e.g., glutamylation-dependent function). (birch2023overcomingthechallenges pages 2-4, hadalin2023geneticcharacteristicsand pages 1-2)
2. **Early cellular dysfunction:** Defective CC/transition-zone function leads to **mis-trafficking** and **opsin mislocalization**, with early photoreceptor functional deficits. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, sladen2024aavrpgrgenetherapy pages 1-2)
3. **Outer segment structural destabilization:** RPGR–cofilin dysregulation perturbs actin dynamics necessary for **disc formation/turnover**, promoting aberrant membrane shedding and outer-segment instability. (megaw2024ciliarytipactin pages 1-2, megaw2024ciliarytipactin media e7ecfeb0)
4. **Amplifying ciliary architecture/transport impairment:** Tubulin PTM imbalance can reduce IFT proteins and RPGR levels, further compounding trafficking defects and ciliary structural failure. (mercey2024glutamylationimbalanceimpairs pages 1-2)
5. **Photoreceptor death and retinal degeneration:** Structural and molecular defects culminate in progressive rod/cone cell death, measurable as shrinking ellipsoid zone and declining retinal sensitivity. (christou2024establishingclinicaltrial pages 1-2, christou2024establishingclinicaltrial pages 2-4)

---

## 5) Phenotypic manifestations (and links to mechanism)

### Core phenotypes (Human Phenotype Ontology; HP)
- **Night blindness (nyctalopia; HP:0000662)** and **peripheral visual field loss (HP:0007994)** are typical of rod-cone dystrophy/XLRP progression described in clinical synthesis. (wongchaisuwat2023retinitispigmentosagtpase pages 1-2, birch2023overcomingthechallenges pages 2-4)
- **Reduced visual acuity (HP:0007663)** and progression to severe impairment/legal blindness in many males. (wongchaisuwat2023retinitispigmentosagtpase pages 1-2, birch2023overcomingthechallenges pages 2-4)
- **OCT outer-retina abnormalities**: altered ellipsoid zone structure; a subset with distal ORF15 variants shows “abnormally broad hyper-reflective ellipsoid zone band” and a tapetal-like sheen phenotype. (Publication date: Sep 2023; URL: https://doi.org/10.1167/iovs.64.12.19) (benson2023rpgrdeepphenotyping pages 1-2)

### Quantitative clinical data (recent)
- **Biomarkers for progression / trial selection (2024):** In 31 RPGR patients (62 eyes), median **EZ length** was **921 μm (RE)** and **865 μm (LE)**; median **microperimetry mean sensitivity** was **2.0 dB (RE)** and **1.1 dB (LE)**. EZ/ELM correlated strongly with microperimetry, and EZ below ~600 μm predicted sensitivity ≈0 dB. (Publication date: Sep 2024; URL: https://doi.org/10.1167/tvst.13.9.18) (christou2024establishingclinicaltrial pages 1-2, christou2024establishingclinicaltrial pages 2-4)
- **Longitudinal acuity data (2023 cohort):** In Slovenian males with RP, median BCVA worsened from **0.30 logMAR** (median age 32) to **0.48 logMAR** (median age 39); COD cases had later onset (median 25 years) and poorer baseline acuity. (Publication date: Feb 2023; URL: https://doi.org/10.3390/ijms24043840) (hadalin2023geneticcharacteristicsand pages 1-2)

---

## 6) Recent developments (prioritizing 2023–2024)

### 6.1 2024: RPGR regulates actin dynamics for disc morphogenesis
The 2024 Nature Communications study provides a direct mechanistic bridge between RPGR dysfunction and failure of outer-segment renewal, placing **actin/cofilin regulation** as a tractable pathway downstream of RPGR. (May 2024; https://doi.org/10.1038/s41467-024-48639-w) (megaw2024ciliarytipactin pages 1-2)

### 6.2 2024: Human retinal organoids validate opsin mislocalization rescue by RPGR gene supplementation
The 2024 organoid study demonstrates disease-relevant correction of **RPGR localization** and **rhodopsin mislocalization** by AAV-RPGR, strengthening causality for trafficking failure and supporting translational gene augmentation. (Feb 2024; https://doi.org/10.3390/ijms25031839) (sladen2024aavrpgrgenetherapy pages 1-2)

### 6.3 2024: Tubulin PTM balance as a structural determinant of the connecting cilium
The 2024 EMBO Journal evidence adds a ciliary structural/PTM layer: polyglutamylation imbalance disrupts CC architecture and reduces IFT proteins and RPGR abundance. (Nov 2024; https://doi.org/10.1038/s44318-024-00284-1) (mercey2024glutamylationimbalanceimpairs pages 1-2)

---

## 7) Current applications and real-world implementations

### 7.1 Clinical genetics and molecular diagnosis
- **High ORF15 burden in clinical testing:** In 1,033 RPGR-inclusive tests, 184 RPGR variants were identified, with 78 pathogenic/likely pathogenic; among these, **87% were frameshift/nonsense** and **67% enriched in exon 15/ORF15**; 23 pathogenic/likely pathogenic variants were novel. (Jan 2024; https://doi.org/10.63500/mv_v30_49) (hadalin2023geneticcharacteristicsand pages 1-2)

### 7.2 AAV gene therapy: pipeline, endpoints, and deployment in trials
A 2024 peer-reviewed review summarizes multiple RPGR gene therapy programs and typical endpoints (microperimetry/retinal sensitivity, OCT structure, BCVA, functional vision). (Jul 2024; https://doi.org/10.1007/s40291-024-00722-0) (mcclements2024genetherapiesin pages 2-4)

**Key ClinicalTrials.gov implementations (URLs embedded in identifiers):**
- **Botaretigene sparoparvovec (AAV5-hRKp.RPGR), Phase 3 (completed):**
  - Registry: **NCT04671433** (ClinicalTrials.gov). Sponsor: Janssen R&D.
  - Enrollment: **105**; randomized parallel-group; completed **2024-09-30**.
  - Primary endpoint: change baseline to Week 52 in **Vision-guided Mobility Assessment (VMA)**. Secondary endpoints include **mean retinal sensitivity within central 10° (MRS10)** and other visual function measures. (NCT04671433 chunk 1)
- **AGTC-501 / laruparetigene zovaparvovec (rAAV2tYF-GRK1-hRPGRco), Phase 2/3 (active not recruiting):**
  - Registry: **NCT04850118** (ClinicalTrials.gov). Sponsor: Beacon Therapeutics.
  - Enrollment: **85**; randomized controlled masked multi-center.
  - Primary endpoint: proportion achieving **≥15-letter LLVA increase** through Month 12; key secondary endpoints include MAIA microperimetry mean sensitivity and FST. (NCT04850118 chunk 1)

**Expert / authoritative analysis:**
- The 2024 Molecular Diagnosis & Therapy review notes that some clinical-trial data in the field may be incomplete or press-release based (field-wide limitation), and describes progress of multiple RPGR programs (including phase I/II to phase III transitions). (mcclements2024genetherapiesin pages 2-4)

---

## 8) Knowledge base-ready annotations

### 8.1 Pathophysiology narrative (for disease KB entry)
RPGR-related retinopathy is a photoreceptor cilium disorder in which RPGR dysfunction at the connecting cilium/transition zone disrupts ciliary trafficking and outer-segment renewal. Defective transport leads to opsin mislocalization and diminished phototransduction capacity; RPGR also regulates actin/cofilin activity in distal cilia required for disc genesis, and disruption causes aberrant ectosome-like shedding and progressive photoreceptor loss. PTM pathways (RPGRORF15 glutamylation and broader tubulin polyglutamylation balance) modulate ciliary architecture and IFT protein abundance, creating compounding defects in ciliary integrity and cargo movement that ultimately drive rod and cone degeneration. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, megaw2024ciliarytipactin pages 1-2, mercey2024glutamylationimbalanceimpairs pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

### 8.2 Gene/protein annotations (HGNC → candidate GO processes/components)
- **RPGR (HGNC:10273)**
  - **GO: Biological process (candidates):** cilium-dependent protein transport; intraflagellar transport; actin cytoskeleton organization; outer segment disc morphogenesis/maintenance (process-level supported by mechanistic descriptions). (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, megaw2024ciliarytipactin pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)
  - **GO: Cellular component (candidates):** photoreceptor connecting cilium/transition zone; distal cilium/ciliary tip; axoneme. (megaw2024ciliarytipactin pages 1-2, mercey2024glutamylationimbalanceimpairs pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)
- **TTLL5**
  - **GO: Biological process (candidates):** protein glutamylation / PTM; modulation of ciliary protein function. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, sladen2024aavrpgrgenetherapy pages 1-2)
- **Cofilin**
  - **GO: Biological process (candidates):** actin filament severing; actin-mediated membrane remodeling. (megaw2024ciliarytipactin pages 1-2)

### 8.3 Phenotype associations (HP)
- HP:0000662 **Nyctalopia**, HP:0007994 **Peripheral visual field loss**, HP:0007663 **Reduced visual acuity**, and OCT outer-retina abnormalities (ellipsoid zone alterations) are central manifestations described in recent clinical synthesis and phenotyping. (wongchaisuwat2023retinitispigmentosagtpase pages 1-2, birch2023overcomingthechallenges pages 2-4, benson2023rpgrdeepphenotyping pages 1-2)

### 8.4 Cell type involvement (CL)
- CL:0000210 **Rod photoreceptor cell**, CL:0000211 **Cone photoreceptor cell**. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, megaw2024ciliarytipactin pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

### 8.5 Anatomical locations (UBERON)
- UBERON:0000966 **Retina**, outer retina/photoreceptor layer; connecting cilium between inner and outer segments (supported by localization/biomarker measurements). (sladen2024aavrpgrgenetherapy pages 1-2, christou2024establishingclinicaltrial pages 1-2, megaw2024ciliarytipactin media e7ecfeb0)

### 8.6 Chemical entities (CHEBI)
- **L-glutamate (CHEBI:29987)** as the residue added in polyglutamylation/glutamylation PTMs affecting ciliary microtubules and RPGRORF15. (mercey2024glutamylationimbalanceimpairs pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2)

---

## 9) Evidence items (PMID-oriented where available in retrieved sources)
The following PMIDs are explicitly linked to RPGR–retinitis pigmentosa association in Open Targets evidence and/or within the retrieved review context:
- Open Targets lists supporting literature PMIDs for RPGR–retinitis pigmentosa including **PMID:12657579, 8673101, 9990021, 10482958, 10094550, 10932196, 10970770, 11857109, 11875055, 11950860, 12920075, 15914600, 16055928, 16387007, 17480003, 23150612**. (mcdonald2024retinalciliopathiesand pages 6-7)
- A 2024 RPGR review excerpt also cites earlier mechanistic work linking RPGR ablation to altered ciliary composition (e.g., Sci Rep 2015 PMID:26068394) and actin stability/cilia formation (Hum Mol Genet 2011 PMID:21933838). (baltaziak2024retinitispigmentosacaused pages 5-6)

---

## Mechanism summary table
| Mechanistic theme | Molecular/cellular details (1-3 sentences) | Key molecules (genes/proteins, enzymes) | Cell types & anatomical site | Evidence type (review/primary/clinical) | Key quantitative data (if any) | Citation IDs |
|---|---|---|---|---|---|---|
| Connecting cilium/transition zone trafficking and opsin mislocalization | RPGR is a ciliary/centrosomal protein enriched at the photoreceptor connecting cilium/transition zone, where it supports trafficking of phototransduction proteins between inner and outer segments. Loss of RPGR function disrupts this gateway and is associated with rhodopsin/opsin mislocalization into inner retinal compartments, consistent with defective ciliary transport as an early pathogenic event. | RPGR, RPGRORF15, RAB8A, RPGRIP1, CEP290, PDE6D, rhodopsin/opsins | Rod and cone photoreceptors; connecting cilium/transition zone between inner and outer segments | Review + primary human organoid/model evidence | RPGR variants account for ~70-80% of X-linked RP; RPGR-deficient organoids show rescue of rhodopsin localization after AAV-RPGR supplementation | (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, wongchaisuwat2023retinitispigmentosagtpase pages 1-2, sladen2024aavrpgrgenetherapy pages 1-2) |
| RPGRORF15 glutamylation and TTLL5 pathway | The retina-enriched RPGRORF15 isoform contains a Glu-Gly-rich C-terminal region that undergoes glutamylation, a modification important for RPGR function and/or interaction at the cilium. TTLL5 is implicated in this pathway; loss of TTLL5 or impaired RPGR glutamylation produces an RPGR-like retinal phenotype and is proposed to contribute especially to cone-dominant disease. | RPGRORF15, TTLL5, glutamylated RPGR | Rod and cone photoreceptors; connecting cilium | Review + organoid/model evidence | RPGRORF15 glutamylation restored to WT-like levels after AAV-RPGR in KO organoids; ORF15 encodes the mutation-prone terminal region | (mcdonald2024retinalciliopathiesand pages 6-7, wongchaisuwat2023retinitispigmentosagtpase pages 2-3, mcdonald2024retinalciliopathiesand pages 18-20, sladen2024aavrpgrgenetherapy pages 1-2) |
| Actin/cofilin-mediated disc formation and ectocytosis at ciliary tip | A 2024 primary study links RPGR to actin-dependent membrane remodeling required for basal disc genesis and outer-segment maintenance. RPGR binds/regulates the actin-severing factor cofilin in distal photoreceptor cilia; Rpgr deficiency perturbs actin dynamics, causing aborted membrane shedding as ectosome-like vesicles and leading to photoreceptor death and visual loss. | RPGR, cofilin, F-actin, gelsolin-related actin regulators | Photoreceptors; distal connecting cilium/ciliary tip, nascent basal discs of outer segment | Primary mechanistic study + review/model context | Study states RPGR mutations account for 70-90% of X-linked RP; qualitative phenotype includes ectosome-like vesicles, photoreceptor death, visual loss | (megaw2024ciliarytipactin pages 1-2, mcdonald2024retinalciliopathiesand pages 6-7, megaw2024ciliarytipactin media e7ecfeb0) |
| Tubulin PTM imbalance affecting IFT and RPGR levels | Polyglutamylation balance in the connecting cilium is required for photoreceptor ciliary architecture. Hyperglutamylation models show loss of the bulge region, distal axoneme destabilization, impaired glycylation, reduced IFT proteins, and reduced RPGR levels, supporting a mechanism in which altered tubulin PTMs secondarily impair ciliary trafficking and RPGR maintenance. | Tubulin polyglutamylation, CCP5/AGBL5, CCP1, TTLL enzymes, IFT proteins, RPGR | Photoreceptors; connecting cilium, distal axoneme, outer segment | Primary mechanistic study | No single clinical biomarker given; structural defects include exacerbated connecting cilium and loss of bulge region in mouse/human photoreceptor analyses | (mercey2024glutamylationimbalanceimpairs pages 1-2) |
| Natural history biomarkers (EZ, ELM, microperimetry) | Structural and functional biomarkers are being refined for trial selection and progression monitoring in RPGR disease. EZ and ELM lengths on OCT correlate strongly with microperimetry sensitivity, and EZ around 600 µm marks a threshold below which sensitivity approaches 0 dB; high inter-eye symmetry supports use in clinical trials. | Ellipsoid zone (EZ), external limiting membrane (ELM), microperimetry sensitivity | Retina/macula of RPGR-affected eyes; outer retina | Clinical observational study | 31 patients/62 eyes; median age 31 years; median EZ 921 µm (RE) and 865 µm (LE); median ELM 2056 µm (RE) and 1860 µm (LE); median microperimetry 2.0 dB (RE) and 1.1 dB (LE); EZ <~600 µm predicts ~0 dB; EZ vs ELM R²=0.931 | (christou2024establishingclinicaltrial pages 1-2, christou2024establishingclinicaltrial pages 2-4) |
| Variant spectrum and ORF15 hotspot | ORF15 is the principal mutational hotspot because its repetitive purine-rich sequence is unstable and technically difficult to sequence. Recent cohorts show major enrichment of pathogenic variants in ORF15, especially frameshift/nonsense alleles, and distal 3′ ORF15 variants are associated with cone/cone-rod phenotypes and distinctive retinal sheen/OCT reflectivity patterns. | RPGR, RPGRORF15 | Germline variant spectrum affecting photoreceptors; RPGR locus on X chromosome | Clinical genetics + phenotyping + review | In >1,000 tests, 184 RPGR variants identified, 78 pathogenic/likely pathogenic; 23 novel; 87% of pathogenic/likely pathogenic variants were frameshift or nonsense and 67% were in exon 15/ORF15. ORF15 accounts for ~60% of RPGR cases in one phenotyping study; 12/66 patients (18.2%) had retinal sheen, three-fourths male and mostly distal ORF15-associated cone-rod disease | (benson2023rpgrdeepphenotyping pages 1-2, hadalin2023geneticcharacteristicsand pages 1-2) |


*Table: This table summarizes the main mechanistic themes, molecular players, clinical biomarkers, and variant-spectrum findings for RPGR-related retinopathy using only the provided citation contexts. It is structured for direct reuse in a disease knowledge base or evidence summary.*

## Mechanistic figure (disc formation site)
A schematic locating disc genesis and the connecting-cilium tip compartment implicated in the RPGR–actin/cofilin mechanism is available from Megaw et al. 2024 (Figure 1a). (megaw2024ciliarytipactin media e7ecfeb0)

---

## Source list (2023–2024 prioritized; with dates and URLs)
- Wongchaisuwat N et al. **Retinitis pigmentosa GTPase regulator-related retinopathy and gene therapy.** *Saudi J Ophthalmol.* **Oct 2023**. https://doi.org/10.4103/sjopt.sjopt_168_23 (wongchaisuwat2023retinitispigmentosagtpase pages 2-3, wongchaisuwat2023retinitispigmentosagtpase pages 1-2)
- Birch DG et al. **Overcoming the Challenges to Clinical Development of X-Linked Retinitis Pigmentosa Therapies: Proceedings of an Expert Panel.** *TVST.* **Jun 2023**. https://doi.org/10.1167/tvst.12.6.5 (birch2023overcomingthechallenges pages 2-4)
- Benson MD et al. **RPGR: Deep phenotyping…** *IOVS.* **Sep 2023**. https://doi.org/10.1167/iovs.64.12.19 (benson2023rpgrdeepphenotyping pages 1-2)
- Hadalin V et al. **Genetic Characteristics and Long-Term Follow-Up…** *Int J Mol Sci.* **Feb 2023**. https://doi.org/10.3390/ijms24043840 (hadalin2023geneticcharacteristicsand pages 1-2)
- Pantrangi M et al. **Clinical sequencing of RPGR in over 1,000 cases.** *Mol Vis.* **Jan 2024**. https://doi.org/10.63500/mv_v30_49 (hadalin2023geneticcharacteristicsand pages 1-2)
- Sladen PE et al. **AAV-RPGR gene therapy rescues opsin mislocalisation in a human retinal organoid model…** *Int J Mol Sci.* **Feb 2024**. https://doi.org/10.3390/ijms25031839 (sladen2024aavrpgrgenetherapy pages 1-2)
- McDonald A, Wijnholds J. **Retinal ciliopathies and potential gene therapies…** *Int J Mol Sci.* **Mar 2024**. https://doi.org/10.3390/ijms25052887 (mcdonald2024retinalciliopathiesand pages 6-7, mcdonald2024retinalciliopathiesand pages 18-20)
- Megaw R et al. **Ciliary tip actin dynamics regulate photoreceptor outer segment integrity.** *Nat Commun.* **May 2024**. https://doi.org/10.1038/s41467-024-48639-w (megaw2024ciliarytipactin pages 1-2, megaw2024ciliarytipactin media e7ecfeb0)
- McClements ME et al. **Gene Therapies in Clinical Development to Treat Retinal Disorders.** *Mol Diagn Ther.* **Jul 2024**. https://doi.org/10.1007/s40291-024-00722-0 (mcclements2024genetherapiesin pages 2-4)
- Christou EE et al. **Establishing Clinical Trial Endpoints in Selecting Patients for RPGR Retinal Gene Therapy.** *TVST.* **Sep 2024**. https://doi.org/10.1167/tvst.13.9.18 (christou2024establishingclinicaltrial pages 1-2, christou2024establishingclinicaltrial pages 2-4)
- Mercey O et al. **Glutamylation imbalance impairs the molecular architecture of the photoreceptor cilium.** *EMBO J.* **Nov 2024**. https://doi.org/10.1038/s44318-024-00284-1 (mercey2024glutamylationimbalanceimpairs pages 1-2)
- ClinicalTrials.gov: **NCT04671433** (start **2020-12-04**, completed **2024-09-30**) (NCT04671433 chunk 1)
- ClinicalTrials.gov: **NCT04850118** (posted/updated **2024** in retrieved registry record) (NCT04850118 chunk 1)


References

1. (mcdonald2024retinalciliopathiesand pages 6-7): Andrew McDonald and Jan Wijnholds. Retinal ciliopathies and potential gene therapies: a focus on human ipsc-derived organoid models. International Journal of Molecular Sciences, 25:2887, Mar 2024. URL: https://doi.org/10.3390/ijms25052887, doi:10.3390/ijms25052887. This article has 14 citations.

2. (wongchaisuwat2023retinitispigmentosagtpase pages 2-3): Nida Wongchaisuwat, Alessia Amato, Andrew E. Lamborn, Paul Yang, Lesley Everett, and Mark E. Pennesi. Retinitis pigmentosa gtpase regulator-related retinopathy and gene therapy. Saudi Journal of Ophthalmology, 37:276-286, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_168\_23, doi:10.4103/sjopt.sjopt\_168\_23. This article has 5 citations.

3. (mcdonald2024retinalciliopathiesand pages 18-20): Andrew McDonald and Jan Wijnholds. Retinal ciliopathies and potential gene therapies: a focus on human ipsc-derived organoid models. International Journal of Molecular Sciences, 25:2887, Mar 2024. URL: https://doi.org/10.3390/ijms25052887, doi:10.3390/ijms25052887. This article has 14 citations.

4. (megaw2024ciliarytipactin pages 1-2): Roly Megaw, Abigail Moye, Zhixian Zhang, Fay Newton, Fraser McPhie, Laura C. Murphy, Lisa McKie, Feng He, Melissa K. Jungnickel, Alex von Kriegsheim, Peter A. Tennant, Chloe Brotherton, Christine Gurniak, Alecia K. Gross, Laura M. Machesky, Theodore G. Wensel, and Pleasantine Mill. Ciliary tip actin dynamics regulate photoreceptor outer segment integrity. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48639-w, doi:10.1038/s41467-024-48639-w. This article has 16 citations and is from a highest quality peer-reviewed journal.

5. (mercey2024glutamylationimbalanceimpairs pages 1-2): Olivier Mercey, Sudarshan Gadadhar, Maria M Magiera, Laura Lebrun, Corinne Kostic, Alexandre Moulin, Yvan Arsenijevic, Carsten Janke, Paul Guichard, and Virginie Hamel. Glutamylation imbalance impairs the molecular architecture of the photoreceptor cilium. The EMBO Journal, 43:6679-6704, Nov 2024. URL: https://doi.org/10.1038/s44318-024-00284-1, doi:10.1038/s44318-024-00284-1. This article has 11 citations.

6. (sladen2024aavrpgrgenetherapy pages 1-2): Paul E. Sladen, Arifa Naeem, Toyin Adefila-Ideozu, Tijmen Vermeule, Sophie L. Busson, Michel Michaelides, Stuart Naylor, Alexandria Forbes, Amelia Lane, and Anastasios Georgiadis. Aav-rpgr gene therapy rescues opsin mislocalisation in a human retinal organoid model of rpgr-associated x-linked retinitis pigmentosa. International Journal of Molecular Sciences, 25:1839, Feb 2024. URL: https://doi.org/10.3390/ijms25031839, doi:10.3390/ijms25031839. This article has 22 citations.

7. (wongchaisuwat2023retinitispigmentosagtpase pages 1-2): Nida Wongchaisuwat, Alessia Amato, Andrew E. Lamborn, Paul Yang, Lesley Everett, and Mark E. Pennesi. Retinitis pigmentosa gtpase regulator-related retinopathy and gene therapy. Saudi Journal of Ophthalmology, 37:276-286, Oct 2023. URL: https://doi.org/10.4103/sjopt.sjopt\_168\_23, doi:10.4103/sjopt.sjopt\_168\_23. This article has 5 citations.

8. (birch2023overcomingthechallenges pages 2-4): David G. Birch, Janet K. Cheetham, Stephen P. Daiger, Carel Hoyng, Christine Kay, Ian M. MacDonald, Mark E. Pennesi, and Lori S. Sullivan. Overcoming the challenges to clinical development of x-linked retinitis pigmentosa therapies: proceedings of an expert panel. Translational Vision Science &amp; Technology, 12:5, Jun 2023. URL: https://doi.org/10.1167/tvst.12.6.5, doi:10.1167/tvst.12.6.5. This article has 22 citations and is from a peer-reviewed journal.

9. (benson2023rpgrdeepphenotyping pages 1-2): Matthew D. Benson, Souvick Mukherjee, Aime R. Agather, Delphine Blain, Denise Cunningham, Robert Mays, Xun Sun, Tiansen Li, Robert B. Hufnagel, Brian P. Brooks, Laryssa A. Huryn, Wadih M. Zein, and Catherine A. Cukras. <i>rpgr</i>: deep phenotyping and genetic characterization with findings specific to the 3′-end of orf15. Investigative Opthalmology &amp; Visual Science, 64:19, Sep 2023. URL: https://doi.org/10.1167/iovs.64.12.19, doi:10.1167/iovs.64.12.19. This article has 10 citations.

10. (hadalin2023geneticcharacteristicsand pages 1-2): Vlasta Hadalin, Maša Buscarino, Jana Sajovic, Andrej Meglič, Martina Jarc-Vidmar, Marko Hawlina, Marija Volk, and Ana Fakin. Genetic characteristics and long-term follow-up of slovenian patients with rpgr retinal dystrophy. International Journal of Molecular Sciences, 24:3840, Feb 2023. URL: https://doi.org/10.3390/ijms24043840, doi:10.3390/ijms24043840. This article has 4 citations.

11. (megaw2024ciliarytipactin media e7ecfeb0): Roly Megaw, Abigail Moye, Zhixian Zhang, Fay Newton, Fraser McPhie, Laura C. Murphy, Lisa McKie, Feng He, Melissa K. Jungnickel, Alex von Kriegsheim, Peter A. Tennant, Chloe Brotherton, Christine Gurniak, Alecia K. Gross, Laura M. Machesky, Theodore G. Wensel, and Pleasantine Mill. Ciliary tip actin dynamics regulate photoreceptor outer segment integrity. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48639-w, doi:10.1038/s41467-024-48639-w. This article has 16 citations and is from a highest quality peer-reviewed journal.

12. (christou2024establishingclinicaltrial pages 1-2): Evita Evangelia Christou, Amandeep S. Josan, Jasmina Cehajic-Kapetanovic, and Robert E. MacLaren. Establishing clinical trial endpoints in selecting patients for rpgr retinal gene therapy. Translational Vision Science &amp; Technology, 13:18, Sep 2024. URL: https://doi.org/10.1167/tvst.13.9.18, doi:10.1167/tvst.13.9.18. This article has 6 citations and is from a peer-reviewed journal.

13. (christou2024establishingclinicaltrial pages 2-4): Evita Evangelia Christou, Amandeep S. Josan, Jasmina Cehajic-Kapetanovic, and Robert E. MacLaren. Establishing clinical trial endpoints in selecting patients for rpgr retinal gene therapy. Translational Vision Science &amp; Technology, 13:18, Sep 2024. URL: https://doi.org/10.1167/tvst.13.9.18, doi:10.1167/tvst.13.9.18. This article has 6 citations and is from a peer-reviewed journal.

14. (mcclements2024genetherapiesin pages 2-4): Michelle E. McClements, Maram E. A. Abdalla Elsayed, Lauren Major, Cristina Martinez-Fernandez de la Camara, and Robert E. MacLaren. Gene therapies in clinical development to treat retinal disorders. Molecular Diagnosis & Therapy, 28:575-591, Jul 2024. URL: https://doi.org/10.1007/s40291-024-00722-0, doi:10.1007/s40291-024-00722-0. This article has 25 citations and is from a peer-reviewed journal.

15. (NCT04671433 chunk 1):  Gene Therapy Trial for the Treatment of X-linked Retinitis Pigmentosa Associated With Variants in the RPGR Gene. Janssen Research & Development, LLC. 2020. ClinicalTrials.gov Identifier: NCT04671433

16. (NCT04850118 chunk 1):  A Clinical Trial Evaluating the Safety and Efficacy of a Single Subretinal Injection of AGTC-501 in Participants With XLRP. Beacon Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT04850118

17. (baltaziak2024retinitispigmentosacaused pages 5-6): K Baltaziak and K Nowomiejska. Retinitis pigmentosa caused by mutations in the rpgr gene—review of the literature. Unknown journal, 2024.