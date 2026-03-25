---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-31T17:00:33.196945'
end_time: '2026-01-31T17:08:39.447627'
duration_seconds: 486.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary von Willebrand Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hereditary von Willebrand Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hereditary von Willebrand Disease**.
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
- **Disease Name:** Hereditary von Willebrand Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hereditary von Willebrand Disease**.
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
- Disease Name: Hereditary von Willebrand Disease (VWD)
- MONDO ID: —
- Category: Genetic

Executive Summary
Hereditary von Willebrand disease is caused by quantitative or qualitative defects of the multimeric glycoprotein von Willebrand factor (VWF), synthesized predominantly by endothelial cells (and by megakaryocytes for platelet VWF). Dysregulation spans biosynthesis, post-translational processing and multimerization in the ER/Golgi, storage in Weibel–Palade bodies (WPBs), regulated exocytosis, plasma survival and clearance, and VWF’s adhesive and carrier interactions with platelet GPIbα, subendothelial collagen, and factor VIII (FVIII). Recent research emphasizes glycosylation—particularly O-glycans and sialylation—as modulators of intracellular trafficking, conformational activation, and clearance, and genetic epidemiology suggests far higher global prevalence than historically recognized (gnomAD v4.1, 2023–2026) (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159, seidizadeh2026updatedglobalprevalence pages 1-5).

1) Core Pathophysiology
- Synthesis and processing: VWF is produced by endothelial cells and megakaryocytes. After translation, VWF undergoes folding and disulfide bond formation in the ER, followed by dimerization/concatemerization and propeptide processing in the Golgi, creating ultra-large multimers packaged into WPBs in endothelial cells (platelet VWF is stored in alpha granules) (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Storage and regulated secretion: WPBs are specialized endothelial organelles whose size and content are determined by Golgi-based mechanisms; WPB size modulates VWF adhesive activity. Exocytosis is triggered by cAMP/Ca2+-elevating agonists (e.g., vasopressin/epinephrine) and hemodynamic shear, rapidly releasing ultra-large VWF into plasma (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Functional interactions: Circulating VWF supports primary hemostasis via A1–GPIbα-mediated platelet tethering under shear, A3–collagen binding at sites of injury, and serves as a carrier for FVIII via the D′D3 region, stabilizing FVIII and prolonging its half-life (parnian2024mechanismandconsequences pages 157-159).
- Proteolysis and multimer regulation: ADAMTS13 cleaves the A2 domain of VWF, reducing ultra-large multimer size and regulating adhesiveness; imbalances in cleavage and multimerization contribute to qualitative phenotypes (parnian2024mechanismandconsequences pages 157-159).
- Plasma survival and clearance: ABO blood group and VWF glycosylation modify plasma half‑life; group O is associated with shorter VWF survival and lower levels. O‑linked sialylation protects VWF from lectin-mediated clearance by macrophage galactose-type lectins; desialylation can both enhance clearance and destabilize the autoinhibitory module that masks the A1 domain, increasing adhesive activity (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).

2) Key Molecular Players
- Genes/Proteins:
  - VWF (HGNC:12721): central effector; variant classes determine type 1/2/3 VWD (karampini2024oglycandeterminantsregulate pages 12-13).
  - FVIII (F8; HGNC:3547): VWF’s carrier; impaired binding (type 2N) yields hemophilia A‑like phenotype (parnian2024mechanismandconsequences pages 157-159).
  - ADAMTS13 (HGNC:14378): metalloprotease regulating VWF multimer size via A2 cleavage (parnian2024mechanismandconsequences pages 157-159).
  - Lectin receptors (e.g., macrophage galactose‑type lectin pathway): mediate clearance of desialylated VWF (karampini2024oglycandeterminantsregulate pages 12-13).
- Chemical entities and modifiers:
  - Sialic acid on O‑glycans: preserves VWF survival; desialylation increases clearance and can activate VWF adhesiveness (karampini2024oglycandeterminantsregulate pages 12-13).
  - Therapeutics: desmopressin (triggers WPB release), antifibrinolytics (tranexamic acid), recombinant VWF concentrates, and investigational VWF‑A1–binding aptamers (rondaptivon pegol/BT200) that can raise VWF/FVIII and correct thrombocytopenia in 2B (clinical development) (moser2024progressinvon pages 1-1).
- Cell types: endothelial cells (biosynthesis, storage/exocytosis), megakaryocytes and platelets (storage in alpha granules and primary adhesion substrate) (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Anatomical locations: blood vessel endothelium is the key site of regulated VWF release; the extracellular blood compartment mediates VWF–platelet–collagen–FVIII interactions (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).

3) Biological Processes (GO, disrupted in VWD)
- Platelet adhesion to damaged vessel (GO:0030168): impaired in qualitative VWD variants; exaggerated in gain‑of‑function states (parnian2024mechanismandconsequences pages 157-159, karampini2024oglycandeterminantsregulate pages 12-13).
- Protein O-linked glycosylation (GO:0006493) and protein sialylation (GO:0097503): regulate VWF trafficking to WPBs, conformational stability, and clearance (karampini2024oglycandeterminantsregulate pages 12-13).
- Regulation of exocytosis (GO:0017157): altered WPB release affects circulating VWF availability (parnian2024mechanismandconsequences pages 157-159).
- Protein folding (GO:0006457), multimerization (GO:0051260): ER/Golgi processes critical for HMW multimers; defects underlie type 2A and some type 1/3 (karampini2024oglycandeterminantsregulate pages 12-13).
- Proteolysis (GO:0006508): ADAMTS13 cleavage of A2 domain regulates multimer distribution (parnian2024mechanismandconsequences pages 157-159).
- Receptor-mediated endocytosis (GO:0006898): lectin-mediated uptake of desialylated VWF modulates half-life (karampini2024oglycandeterminantsregulate pages 12-13).

4) Cellular Components (GO-CC, primary sites)
- Weibel–Palade body (GO:0042581): endothelial storage organelle; size and packing determine adhesive function of released VWF (karampini2024oglycandeterminantsregulate pages 12-13).
- Platelet alpha granule (GO:0031091): storage of platelet VWF (parnian2024mechanismandconsequences pages 157-159).
- Endoplasmic reticulum (GO:0005783) and Golgi apparatus (GO:0005794): VWF folding, disulfide-bond formation, dimerization/concatemerization, and propeptide processing (karampini2024oglycandeterminantsregulate pages 12-13).
- Extracellular region (GO:0005576): site of VWF interactions with platelets, collagen, FVIII, and ADAMTS13 proteolysis (parnian2024mechanismandconsequences pages 157-159).

5) Disease Progression: Sequence of Events
- Genetic variant determines primary defect in quantity (type 1/3) or quality (type 2 subclasses 2A/2B/2M/2N) of VWF (karampini2024oglycandeterminantsregulate pages 12-13, seidizadeh2026updatedglobalprevalence pages 15-19).
- Cellular/molecular alterations include impaired folding/trafficking/multimerization (2A and some 1/3), conformational gain-of-function for A1–GPIbα binding (2B), adhesive dysfunction without multimer loss (2M), reduced FVIII binding (2N), or increased clearance (a subset of type 1) (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- System-level consequences include decreased VWF activity and/or HMW multimer content, reduced FVIII levels (2N, 3), or paradoxical platelet consumption in 2B; clinically, mucocutaneous bleeding predominates, with severity correlating with defect magnitude and VWF/FVIII levels (du2023vonwillebranddisease pages 9-10).

6) Subtype-specific Mechanisms and Clinical Correlates
- Type 1 (partial quantitative): reduced synthesis and/or increased clearance; influenced by ABO and glycosylation (shorter survival in group O). Laboratory: parallel reduction in VWF antigen and activity; multimer pattern relatively preserved; many respond to desmopressin (parnian2024mechanismandconsequences pages 157-159, du2023vonwillebranddisease pages 9-10).
- Type 2A (qualitative—loss of HMW multimers): defective multimerization or increased proteolysis (e.g., A2 domain susceptibility) leading to loss of high‑molecular‑weight (HMW) multimers and impaired platelet adhesion; VWF:CB and GPIb-based assays disproportionately low vs antigen (karampini2024oglycandeterminantsregulate pages 12-13).
- Type 2B (qualitative—gain-of-function A1–GPIbα): increased spontaneous binding to GPIbα causes platelet aggregation/clearance, thrombocytopenia, and secondary loss of HMW multimers; rictocetin/GPIbM activity high relative to antigen in specific contexts; thrombocytopenia may worsen with desmopressin; investigational A1‑binding aptamer (rondaptivon pegol) can raise VWF/FVIII and correct thrombocytopenia (karampini2024oglycandeterminantsregulate pages 12-13, moser2024progressinvon pages 1-1).
- Type 2M (qualitative—adhesive defect without multimer loss): impaired A1–GPIbα and/or A3–collagen interactions with normal multimer distribution; activity (GPIb or collagen binding) disproportionately low vs antigen (karampini2024oglycandeterminantsregulate pages 12-13).
- Type 2N (qualitative—FVIII binding defect): variants in D′D3 reduce FVIII affinity; FVIII levels decline due to rapid clearance, mimicking mild hemophilia A; VWF antigen/activity may be near normal; specialized FVIII‑binding assays confirm diagnosis (parnian2024mechanismandconsequences pages 157-159, seidizadeh2025globalprevalenceand pages 6-8).
- Type 3 (virtual absence): biallelic loss-of-function yielding near absence of VWF and very low FVIII; severe bleeding including joint bleeds; no response to desmopressin, require VWF concentrates (seidizadeh2026updatedglobalprevalence pages 15-19, du2023vonwillebranddisease pages 9-10).

7) Phenotypic Manifestations and Burden (HP terms)
- Mucocutaneous bleeding (HP:0001977): epistaxis (HP:0000421), gingival bleeding, easy bruising; heavy menstrual bleeding/menorrhagia (HP:0000132) is highly prevalent in women with VWD (du2023vonwillebranddisease pages 9-10).
- Surgical and dental bleeding; gastrointestinal bleeding; in severe forms, hemarthrosis and deep tissue bleeds (du2023vonwillebranddisease pages 9-10).
- Population-level data: Bleeding events occur in a majority of patients across types; in the Dutch WiN cohort, bleeding scores were progressively higher from type 1 to 2 to 3, consistent with severity gradients (du2023vonwillebranddisease pages 9-10).

8) Recent Developments (2023–2024) and Applications
- Glycosylation and trafficking: Human endothelial studies show O‑glycan composition critically regulates VWF trafficking to WPBs; O‑glycan inhibition activates the A1 domain and alters WPB size, linking glycan determinants to adhesive function and storage biology (Blood Advances, 2024; DOI: 10.1182/bloodadvances.2023012499) (karampini2024oglycandeterminantsregulate pages 12-13).
- Autoinhibitory module and activation: Contemporary structural and biophysical work (cited within 2024 review material) indicates desialylation can destabilize the autoinhibitory module that masks A1, enhancing shear-dependent activation; these insights refine models for 2B-like gain-of-function and clearance interplay (karampini2024oglycandeterminantsregulate pages 12-13).
- Therapeutic landscape: Reviews in 2024 summarize evolution toward newer therapies—rVWF concentrates, nuanced desmopressin use, and clinical development of the VWF A1-binding aptamer rondaptivon pegol/BT200 that increases VWF/FVIII and normalizes platelet counts in 2B—alongside half-life extension strategies and more personalized approaches (Semin Thromb Hemost, 2024; DOI: 10.1055/s-0044-1779485) (moser2024progressinvon pages 1-1).
- Diagnostics and multimer analysis: Updated multimer analysis approaches remain central to differentiating quantitative vs qualitative subtypes and interpreting multimer patterns in context of clearance and proteolysis defects (Semin Thromb Hemost, 2023; DOI: 10.1055/s-0042-1757183) (saadalla2023vonwillebrandfactor pages 1-1).

9) Prevalence and Genetic Epidemiology (2023+)
- gnomAD-based estimates using 321 curated pathogenic/likely pathogenic VWF variants (n=807,162 individuals; v4.1) reveal much higher genetic prevalence than clinical registries: per 1,000—type 1 ≈10.6–11, 2A ≈1.3, 2B ≈1.7, 2M ≈1.5; per million—2N ≈31–34, type 3 ≈1.2–1.8 (range reflects inclusion of loss-of-function SVs/CNVs) (npj Genomic Medicine, 2023; Sci Rep, 2026) (seidizadeh2023populationbasedprevalenceand pages 2-5, seidizadeh2026updatedglobalprevalence pages 1-5, seidizadeh2026updatedglobalprevalence pages 15-19, seidizadeh2025globalprevalenceand pages 4-6, seidizadeh2025globalprevalenceand pages 1-4, seidizadeh2026updatedglobalprevalence pages 5-10).
- Ethnic variation is pronounced (e.g., 2N enriched in European populations due to p.Arg854Gln; type 3 varies widely by ancestry), supporting an underdiagnosis narrative and the need for population-specific awareness (seidizadeh2025globalprevalenceand pages 6-8, seidizadeh2026updatedglobalprevalence pages 15-19, seidizadeh2023populationbasedprevalenceand pages 2-5).
- Burden of illness: Systematic review data underscore frequent mucocutaneous bleeding, delayed diagnosis, and substantive quality-of-life impacts in real-world settings (J Blood Med, 2023; DOI: 10.2147/JBM.S389241) (du2023vonwillebranddisease pages 9-10).

10) Ontology-Linked Annotations and Evidence Table
| Category | Entity / Term | Ontology ID / Code | Role in VWD pathophysiology (1-2 sentences) | Key evidence (DOI/URL and context IDs) |
|---|---|---:|---|---|
| Gene / Protein | VWF (von Willebrand factor) | HGNC:12721 | Central multimeric glycoprotein mediating platelet adhesion and carrying/protecting FVIII; defects cause quantitative (type 1/3) or qualitative (type 2) VWD via impaired synthesis, multimerization, storage, secretion or increased clearance. | DOI: 10.1182/bloodadvances.2023012499 https://doi.org/10.1182/bloodadvances.2023012499 (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159, saadalla2023vonwillebrandfactor pages 1-1) |
| Gene / Protein | F8 (Factor VIII) | HGNC:3547 | FVIII is stabilized in plasma by binding to VWF (D′D3 region); loss of binding (type 2N) reduces FVIII half-life and produces hemophilia-like phenotype. | Review summaries and mechanistic notes (parnian2024mechanismandconsequences pages 157-159, saadalla2023vonwillebrandfactor pages 1-1) |
| Gene / Protein | ADAMTS13 | HGNC:14378 | Metalloprotease that cleaves ULVWF multimers (A2 domain cleavage); insufficient proteolysis alters multimer distribution and contributes to VWF-mediated pathology. | Mechanistic reviews noting ADAMTS13 proteolysis (parnian2024mechanismandconsequences pages 157-159) |
| Gene / Protein | LRP1 (LDL receptor related protein 1) | HGNC:6692 | Putative clearance receptor implicated in hepatic/mononuclear phagocyte-mediated VWF/VWF-fragment uptake, modulating plasma VWF levels and contributing to quantitative defects. | Clearance receptor discussions and ABO/sialylation impacts (parnian2024mechanismandconsequences pages 157-159, karampini2024oglycandeterminantsregulate pages 12-13) |
| Gene / Protein | CLEC10A (macrophage galactose-type lectin) | HGNC:15903 | Lectin recognizing desialylated O-glycans on VWF; mediates macrophage-dependent clearance of VWF and influences plasma survival. | Ward et al.; sialylation studies (referenced) DOI: 10.1182/bloodadvances.2023012499 (karampini2024oglycandeterminantsregulate pages 12-13) |
| Cell type | Endothelial cell | CL:0000115 | Primary site of VWF synthesis, multimerization (ER/Golgi), storage in Weibel–Palade bodies and regulated secretion in response to cAMP/Ca2+ and shear. | WPB and endothelial biosynthesis reviews (parnian2024mechanismandconsequences pages 157-159, karampini2024oglycandeterminantsregulate pages 12-13) |
| Cell type | Megakaryocyte | CL:0000556 | Synthesizes platelet VWF incorporated into platelet alpha-granules; contributes to platelet-associated VWF function. | VWF biosynthesis notes (parnian2024mechanismandconsequences pages 157-159, saadalla2023vonwillebrandfactor pages 1-1) |
| Cell type | Platelet | CL:0000233 | Platelet adhesion is mediated by VWF A1–GPIbα interactions; aberrant VWF–platelet binding (e.g., 2B gain-of-function) causes thrombocytopenia and HMW multimer loss. | Mechanistic subtype descriptions (parnian2024mechanismandconsequences pages 157-159, seidizadeh2025globalprevalenceand pages 6-8) |
| Anatomical location | Blood vessel endothelium | UBERON:0001981 | Site of regulated release of ultralarge VWF multimers from WPBs into the vascular lumen, critical for primary hemostasis and a source of pathological ULVWF in exocytosis disorders. | WPB biology and exocytosis references (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159) |
| Cellular component (GO-CC) | Weibel–Palade body | GO:0042581 | Endothelial storage organelle for multimerized VWF; WPB size/packing influences VWF adhesive activity and regulated secretion dynamics. | Ferraro et al., WPB reviews DOI: https://doi.org/10.1182/bloodadvances.2023012499 (karampini2024oglycandeterminantsregulate pages 12-13) |
| Cellular component (GO-CC) | Platelet alpha granule | GO:0031091 | Intracellular compartment in platelets storing VWF and other hemostatic proteins; contributes to local VWF release upon platelet activation. | Platelet VWF storage mention (parnian2024mechanismandconsequences pages 157-159, saadalla2023vonwillebrandfactor pages 1-1) |
| Cellular component (GO-CC) | Endoplasmic reticulum | GO:0005783 | Site of initial VWF translation, propeptide folding and formation of disulfide bonds required for multimerization. | ER/Golgi multimerization and disulfide-exchange studies (karampini2024oglycandeterminantsregulate pages 12-13, du2023vonwillebranddisease pages 9-10) |
| Cellular component (GO-CC) | Golgi apparatus | GO:0005794 | Location of VWF concatemerization and propeptide cleavage; Golgi-to-WPB trafficking controls multimer size and WPB formation. | Golgi-based control of WPB size and VWF concatemerization (karampini2024oglycandeterminantsregulate pages 12-13, du2023vonwillebranddisease pages 9-10) |
| Cellular component (GO-CC) | Extracellular region | GO:0005576 | Circulating compartment where VWF multimers interact with platelets, collagen, FVIII and are subject to proteolysis/clearance. | Circulating VWF functional interactions (parnian2024mechanismandconsequences pages 157-159, saadalla2023vonwillebrandfactor pages 1-1) |
| Biological process (GO) | Platelet adhesion to damaged vessel | GO:0030168 | VWF-mediated tethering of platelets via A1–GPIbα under shear; defects cause impaired primary hemostasis or pathologic platelet aggregation. | Functional binding domain and shear activation literature (parnian2024mechanismandconsequences pages 157-159, karampini2024oglycandeterminantsregulate pages 12-13) |
| Biological process (GO) | Protein O-linked glycosylation | GO:0006493 | O-glycans and sialylation of VWF regulate trafficking to WPBs, multimer compaction, conformational stability and plasma clearance. | Karampini et al. DOI: 10.1182/bloodadvances.2023012499 (karampini2024oglycandeterminantsregulate pages 12-13) |
| Biological process (GO) | Protein sialylation | GO:0097503 | Sialylation protects VWF from lectin-mediated clearance; desialylation exposes galactose residues promoting macrophage uptake and can activate VWF. | Ward SE and sialylation studies (karampini2024oglycandeterminantsregulate pages 12-13) |
| Biological process (GO) | Regulation of exocytosis | GO:0017157 | cAMP/Ca2+-dependent signaling and shear-triggered pathways control WPB exocytosis and release of ULVWF. | Parnian Alavi and WPB exocytosis notes DOI: 10.7939/r3-8e39-4057 (parnian2024mechanismandconsequences pages 157-159) |
| Biological process (GO) | Protein folding | GO:0006457 | Proper folding of VWF propeptide (VWFpp) and disulfide bond formation are required for multimer assembly; misfolding leads to secretion defects and some type 1/3 variants. | Folding/misfolding references (karampini2024oglycandeterminantsregulate pages 12-13, du2023vonwillebranddisease pages 9-10) |
| Biological process (GO) | Protein multimerization | GO:0051260 | Disulfide-mediated concatemerization in Golgi/WPB is essential for HMW multimer formation; loss/reduction underlies type 2A and some type 1 cases. | Concatemerization and A1 insertion studies (karampini2024oglycandeterminantsregulate pages 12-13, du2023vonwillebranddisease pages 9-10) |
| Biological process (GO) | Proteolysis | GO:0006508 | ADAMTS13-mediated cleavage of the A2 domain regulates multimer size; altered proteolysis shifts HMW multimer balance (relevant in 2A, TTP contexts). | ADAMTS13 mechanism reviews (parnian2024mechanismandconsequences pages 157-159) |
| Biological process (GO) | Receptor-mediated endocytosis | GO:0006898 | Clearance of circulating VWF via hepatic/endothelial receptors (lectins, LRP1/STAB2 family) affects plasma half-life and quantitative VWF levels. | Clearance receptor discussions (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159) |
| Chemical entity (ChEBI) | Desmopressin (DDAVP) | CHEBI:4321 | Therapeutic that triggers endothelial VWF release from WPBs (useful in many type 1 patients); response depends on baseline storage and secretory capacity. | Treatment review DOI: 10.1055/s-0044-1779485 (moser2024progressinvon pages 1-1) |
| Chemical entity (ChEBI) | Tranexamic acid | CHEBI:4560 | Antifibrinolytic supportive therapy for mucocutaneous bleeding in VWD; adjunctive hemostatic agent. | Clinical management reviews (moser2024progressinvon pages 1-1, du2023vonwillebranddisease pages 9-10) |
| Chemical entity (investigational) | Rondaptivon pegol / BT200 (investigational aptamer) | investigational aptamer | A VWF A1-binding agent shown to increase VWF/FVIII levels and reduce clearance in certain VWD subtypes (in clinical development). | Therapeutic developments review DOI: 10.1055/s-0044-1779485 (moser2024progressinvon pages 1-1) |
| Chemical entity (ChEBI) | Sialic acid | CHEBI:15764 | Terminal sugar on O-glycans protecting VWF from lectin-mediated clearance; sialylation status modulates plasma half-life and activation propensity. | Sialylation and clearance studies (karampini2024oglycandeterminantsregulate pages 12-13) |
| Phenotype (HP) | Epistaxis | HP:0000421 | Frequent mucocutaneous bleeding manifestation of VWD reflecting defective primary hemostasis. | Epidemiology and phenotype burden (du2023vonwillebranddisease pages 9-10, seidizadeh2025globalprevalenceand pages 6-8) |
| Phenotype (HP) | Menorrhagia | HP:0000132 | Common severe bleeding phenotype in women with VWD, often driving diagnosis and treatment need. | Clinical burden reviews (du2023vonwillebranddisease pages 9-10, moser2024progressinvon pages 1-1) |
| Phenotype (HP) | Mucocutaneous bleeding | HP:0001977 | Umbrella phenotype (epistaxis, gum bleeding, easy bruising) typical of VWF deficiency/dysfunction. | Systematic review and clinical studies (du2023vonwillebranddisease pages 9-10, saadalla2023vonwillebrandfactor pages 1-1) |
| Phenotype (HP) | Thrombocytopenia (type 2B) | HP:0001873 | Result of pathologic gain-of-function VWF variants with increased platelet binding causing platelet aggregation/clearance and loss of HMW multimers. | Type 2B mechanistic descriptions and prevalence data (parnian2024mechanismandconsequences pages 157-159, seidizadeh2025globalprevalenceand pages 6-8) |


*Table: Compact mapping of key genes, cells, compartments, processes, chemicals, and phenotypes relevant to hereditary von Willebrand disease with ontology codes and primary evidence citations (pqac IDs and DOIs/URLs).*

11) Evidence Items with PMIDs/DOIs/URLs and Publication Dates
- O‑glycan determinants regulate VWF trafficking to WPBs (Blood Advances, 2024-06-25). DOI: 10.1182/bloodadvances.2023012499; URL: https://doi.org/10.1182/bloodadvances.2023012499 (karampini2024oglycandeterminantsregulate pages 12-13).
- Mechanism and consequences of VWF upregulation (Thesis/monograph, 2024). DOI: 10.7939/r3-8e39-4057; URL: https://doi.org/10.7939/r3-8e39-4057 (wpb secretion, ABO, signaling) (parnian2024mechanismandconsequences pages 157-159).
- Population-based prevalence and mutational landscape (npj Genomic Medicine, 2023-10). DOI: 10.1038/s41525-023-00375-8; URL: https://doi.org/10.1038/s41525-023-00375-8 (seidizadeh2023populationbasedprevalenceand pages 2-5).
- Updated global prevalence and ethnic diversity (Scientific Reports, 2026-01). DOI: 10.1038/s41598-026-36145-6; URL: https://doi.org/10.1038/s41598-026-36145-6 (seidizadeh2026updatedglobalprevalence pages 1-5, seidizadeh2026updatedglobalprevalence pages 15-19, seidizadeh2026updatedglobalprevalence pages 5-10).
- VWD epidemiology, burden, and management (Journal of Blood Medicine, 2023-03). DOI: 10.2147/JBM.S389241; URL: https://doi.org/10.2147/JBM.S389241 (du2023vonwillebranddisease pages 9-10).
- Progress in VWD treatment: newer therapies including rondaptivon pegol/BT200 (Seminars in Thrombosis and Hemostasis, 2024-02). DOI: 10.1055/s-0044-1779485; URL: https://doi.org/10.1055/s-0044-1779485 (moser2024progressinvon pages 1-1).
- VWF multimer analysis and classification (Seminars in Thrombosis and Hemostasis, 2023-09). DOI: 10.1055/s-0042-1757183; URL: https://doi.org/10.1055/s-0042-1757183 (saadalla2023vonwillebrandfactor pages 1-1).

12) Expert Opinions and Analysis
- Integrated interpretation: Contemporary evidence positions glycosylation—in particular O‑glycan sialylation—as a central regulator of both intracellular VWF trafficking (WPB formation/size) and extracellular fate (clearance, conformational activation), offering mechanistic explanations for variable penetrance in type 1 and for phenotypes that blend clearance and function (karampini2024oglycandeterminantsregulate pages 12-13).
- Genetic epidemiology (gnomAD v4.1) suggests VWD alleles are far more frequent than clinical diagnoses, implying substantial underrecognition and advocating for refined diagnostic algorithms that combine activity/antigen ratios, multimer assessment, collagen/GPIbM assays, and FVIII‑binding testing for suspected 2N (seidizadeh2023populationbasedprevalenceand pages 2-5, seidizadeh2026updatedglobalprevalence pages 15-19).
- Therapeutic implications: Responses to desmopressin hinge on intact endothelial storage and exocytic signaling; patients with increased clearance or 2B may benefit from alternative strategies (rVWF concentrates; investigational A1 aptamer) rather than DDAVP, aligning therapy with pathophysiology (moser2024progressinvon pages 1-1, parnian2024mechanismandconsequences pages 157-159).

Structured Knowledge Base Fields
- Gene/Protein annotations (HGNC): VWF (HGNC:12721); F8 (HGNC:3547); ADAMTS13 (HGNC:14378) (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Biological Process (GO): GO:0030168; GO:0006493; GO:0097503; GO:0017157; GO:0006457; GO:0051260; GO:0006508; GO:0006898 (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Cellular Component (GO-CC): GO:0042581; GO:0031091; GO:0005783; GO:0005794; GO:0005576 (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Cell type (CL): Endothelial cell (CL:0000115); Megakaryocyte (CL:0000556); Platelet (CL:0000233) (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Anatomical locations (UBERON): Blood vessel endothelium (UBERON:0001981) (karampini2024oglycandeterminantsregulate pages 12-13).
- Chemical entities (ChEBI): Desmopressin (CHEBI:4321); Tranexamic acid (CHEBI:4560); Sialic acid (CHEBI:15764); Rondaptivon pegol/BT200 (investigational) (moser2024progressinvon pages 1-1, karampini2024oglycandeterminantsregulate pages 12-13).
- Phenotypes (HP): Mucocutaneous bleeding (HP:0001977); Epistaxis (HP:0000421); Menorrhagia (HP:0000132); Thrombocytopenia (type 2B) (HP:0001873) (du2023vonwillebranddisease pages 9-10).

Limitations and Notes
- Some mechanistic inferences (e.g., specific clearance receptors beyond lectin pathways) remain under active investigation and may vary by context; where possible, claims have been restricted to evidence in recent peer‑reviewed sources (karampini2024oglycandeterminantsregulate pages 12-13, parnian2024mechanismandconsequences pages 157-159).
- Prevalence estimates are genetic and likely exceed clinically diagnosed case counts due to penetrance and ascertainment biases; ethnicity-specific prevalences vary substantially (seidizadeh2026updatedglobalprevalence pages 1-5, seidizadeh2025globalprevalenceand pages 6-8).

References (selected with URLs/dates)
- Karampini E, et al. Blood Advances. 2024-06-25. DOI: 10.1182/bloodadvances.2023012499. https://doi.org/10.1182/bloodadvances.2023012499 (karampini2024oglycandeterminantsregulate pages 12-13).
- Alavi P. University of Alberta Library. 2024. DOI: 10.7939/r3-8e39-4057. https://doi.org/10.7939/r3-8e39-4057 (parnian2024mechanismandconsequences pages 157-159).
- Seidizadeh O, et al. npj Genomic Medicine. 2023-10. DOI: 10.1038/s41525-023-00375-8. https://doi.org/10.1038/s41525-023-00375-8 (seidizadeh2023populationbasedprevalenceand pages 2-5).
- Seidizadeh O, et al. Scientific Reports. 2026-01. DOI: 10.1038/s41598-026-36145-6. https://doi.org/10.1038/s41598-026-36145-6 (seidizadeh2026updatedglobalprevalence pages 1-5, seidizadeh2026updatedglobalprevalence pages 15-19).
- Du P, et al. Journal of Blood Medicine. 2023-03. DOI: 10.2147/JBM.S389241. https://doi.org/10.2147/JBM.S389241 (du2023vonwillebranddisease pages 9-10).
- Moser MM, et al. Seminars in Thrombosis and Hemostasis. 2024-02. DOI: 10.1055/s-0044-1779485. https://doi.org/10.1055/s-0044-1779485 (moser2024progressinvon pages 1-1).
- Saadalla A, et al. Seminars in Thrombosis and Hemostasis. 2023-09. DOI: 10.1055/s-0042-1757183. https://doi.org/10.1055/s-0042-1757183 (saadalla2023vonwillebrandfactor pages 1-1).

References

1. (karampini2024oglycandeterminantsregulate pages 12-13): Ellie Karampini, Dearbhla Doherty, Petra E. Bürgisser, Massimiliano Garre, Ingmar Schoen, Stephanie Elliott, Ruben Bierings, and James S. O’Donnell. O-glycan determinants regulate vwf trafficking to weibel-palade bodies. Blood Advances, 8:3254-3266, Jun 2024. URL: https://doi.org/10.1182/bloodadvances.2023012499, doi:10.1182/bloodadvances.2023012499. This article has 7 citations and is from a peer-reviewed journal.

2. (parnian2024mechanismandconsequences pages 157-159): Parnian Alavi. Mechanism and consequences of von willebrand factor upregulation in response to aging and organ transplantation. Text, 2024. URL: https://doi.org/10.7939/r3-8e39-4057, doi:10.7939/r3-8e39-4057. This article has 0 citations and is from a peer-reviewed journal.

3. (seidizadeh2026updatedglobalprevalence pages 1-5): Omid Seidizadeh, Andrea Cairo, Camilla Oriani, and Flora Peyvandi. Updated global prevalence and ethnic diversity of von willebrand disease based on population genetics analysis. Scientific Reports, Jan 2026. URL: https://doi.org/10.1038/s41598-026-36145-6, doi:10.1038/s41598-026-36145-6. This article has 0 citations and is from a peer-reviewed journal.

4. (moser2024progressinvon pages 1-1): Miriam M. Moser, Christian Schoergenhofer, and Bernd Jilma. Progress in von willebrand disease treatment: evolution towards newer therapies. Seminars in Thrombosis and Hemostasis, 50:720-732, Feb 2024. URL: https://doi.org/10.1055/s-0044-1779485, doi:10.1055/s-0044-1779485. This article has 9 citations and is from a peer-reviewed journal.

5. (seidizadeh2026updatedglobalprevalence pages 15-19): Omid Seidizadeh, Andrea Cairo, Camilla Oriani, and Flora Peyvandi. Updated global prevalence and ethnic diversity of von willebrand disease based on population genetics analysis. Scientific Reports, Jan 2026. URL: https://doi.org/10.1038/s41598-026-36145-6, doi:10.1038/s41598-026-36145-6. This article has 0 citations and is from a peer-reviewed journal.

6. (du2023vonwillebranddisease pages 9-10): Ping Du, Aurore Bergamasco, Yola Moride, Françoise Truong Berthoz, Gülden Özen, and Spiros Tzivelekis. Von willebrand disease epidemiology, burden of illness and management: a systematic review. Journal of Blood Medicine, 14:189-208, Mar 2023. URL: https://doi.org/10.2147/jbm.s389241, doi:10.2147/jbm.s389241. This article has 55 citations.

7. (seidizadeh2025globalprevalenceand pages 6-8): Omid Seidizadeh, Andrea Cairo, Camilla Oriani, and Flora Peyvandi. Global prevalence and ethnic diversity of von willebrand disease: an updated population-based genetic analysis. May 2025. URL: https://doi.org/10.21203/rs.3.rs-6577209/v1, doi:10.21203/rs.3.rs-6577209/v1.

8. (saadalla2023vonwillebrandfactor pages 1-1): Abdulrahman Saadalla, Jansen Seheult, Rajiv K. Pruthi, and Dong Chen. Von willebrand factor multimer analysis and classification: a comprehensive review and updates. Seminars in Thrombosis and Hemostasis, 49:580-591, Sep 2023. URL: https://doi.org/10.1055/s-0042-1757183, doi:10.1055/s-0042-1757183. This article has 16 citations and is from a peer-reviewed journal.

9. (seidizadeh2023populationbasedprevalenceand pages 2-5): Omid Seidizadeh, Andrea Cairo, Luciano Baronciani, Luca Valenti, and Flora Peyvandi. Population-based prevalence and mutational landscape of von willebrand disease using large-scale genetic databases. NPJ Genomic Medicine, Oct 2023. URL: https://doi.org/10.1038/s41525-023-00375-8, doi:10.1038/s41525-023-00375-8. This article has 39 citations and is from a peer-reviewed journal.

10. (seidizadeh2025globalprevalenceand pages 4-6): Omid Seidizadeh, Andrea Cairo, Camilla Oriani, and Flora Peyvandi. Global prevalence and ethnic diversity of von willebrand disease: an updated population-based genetic analysis. May 2025. URL: https://doi.org/10.21203/rs.3.rs-6577209/v1, doi:10.21203/rs.3.rs-6577209/v1.

11. (seidizadeh2025globalprevalenceand pages 1-4): Omid Seidizadeh, Andrea Cairo, Camilla Oriani, and Flora Peyvandi. Global prevalence and ethnic diversity of von willebrand disease: an updated population-based genetic analysis. May 2025. URL: https://doi.org/10.21203/rs.3.rs-6577209/v1, doi:10.21203/rs.3.rs-6577209/v1.

12. (seidizadeh2026updatedglobalprevalence pages 5-10): Omid Seidizadeh, Andrea Cairo, Camilla Oriani, and Flora Peyvandi. Updated global prevalence and ethnic diversity of von willebrand disease based on population genetics analysis. Scientific Reports, Jan 2026. URL: https://doi.org/10.1038/s41598-026-36145-6, doi:10.1038/s41598-026-36145-6. This article has 0 citations and is from a peer-reviewed journal.