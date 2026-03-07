---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-07T18:43:52.335586'
end_time: '2026-03-07T18:55:08.930403'
duration_seconds: 676.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Houge-Janssens Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Houge-Janssens Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Houge-Janssens Syndrome**.
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
- **Disease Name:** Houge-Janssens Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Houge-Janssens Syndrome**.
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


# Houge–Janssens Syndrome (HJS) Pathophysiology Report (PP2A-related neurodevelopmental disorders)

## 0. Scope, disease definition, and identifiers
Houge–Janssens syndrome (HJS) is a spectrum of Mendelian neurodevelopmental disorders caused by monoallelic pathogenic variants in genes encoding subunits of the serine/threonine phosphatase protein phosphatase 2A (PP2A) holoenzyme, most prominently **PPP2R5D** (HJS type 1; also termed Jordan syndrome), **PPP2R1A** (HJS type 2), and **PPP2CA** (HJS type 3), with emerging expansion to **PPP2R5C** in the “HJS spectrum.” (janssens2024newinsightsinto pages 1-1, verbinnen2025pathogenicdenovo pages 1-3).

* Disease ontology mappings captured in this run: **MONDO_0957553** (Houge-Janssens syndrome), **MONDO_0014605** (Houge-Janssens syndrome 2; OMIM 616362), **MONDO_0032697** (Houge-Janssens syndrome 3). (Derived from Open Targets evidence captured during planning; mechanistic/clinical evidence in texts cited above.)

## 1. Key concepts and definitions (current understanding)
### 1.1 PP2A holoenzyme architecture
PP2A functions as a **heterotrimeric holoenzyme**, built from a **catalytic C subunit**, a **scaffolding A subunit**, and a **regulatory/substrate-specifying B subunit**. Variants in different subunits can converge on impaired holoenzyme assembly, altered catalytic activity, and/or altered substrate recruitment/dephosphorylation specificity (verbinnen2025pathogenicdenovo pages 1-3, lee2025clinicalandmolecular pages 1-2).

### 1.2 Unifying mechanistic concept: “dephosphorylation network disease”
Across HJS subtypes, the central pathophysiologic hypothesis is that **PP2A dysfunction alters serine/threonine dephosphorylation programs**, particularly in the developing brain, leading to abnormal growth-signaling, cell-cycle/mitotic control, and neuronal circuit development—manifesting clinically as developmental delay/intellectual disability (DD/ID), hypotonia, epilepsy, and variable head-size abnormalities (macrocephaly/microcephaly) (janssens2024newinsightsinto pages 1-1, lee2025clinicalandmolecular pages 1-2).

## 2. Core pathophysiology (molecular and cellular mechanisms)
### 2.1 PPP2R5D (HJS1/Jordan syndrome): dysregulated mTORC1–p70S6K–RPS6 signaling with variant-specific upstream wiring
A major recent mechanistic advance is direct quantitative evidence that PPP2R5D pathogenic variants can drive **convergent hyperactivation of mTORC1 output**, measured as **ribosomal protein S6 (RPS6) hyperphosphorylation**.

*Shared downstream signature:* In engineered heterozygous PPP2R5D **E198K** and **E420K** cell lines, Smolen et al. report: **“We observed ribosomal protein S6 (RPS6) hyperphosphorylation as a shared signaling alteration”** (J Biol Chem; 2023-09; https://doi.org/10.1016/j.jbc.2023.105154) (smolen2023quantitativeproteomicsand pages 1-3). The same work reports **increased phosphorylation of RPS6 on S235/236 and S240/244** in both variant backgrounds (smolen2023quantitativeproteomicsand pages 11-13).

*Variant-specific upstream wiring:* The same study concludes **ERK-dependent activation of mTORC1** occurs in both E198K and E420K, with **additional AKT-mediated mTORC1 activation** in E420K (smolen2023quantitativeproteomicsand pages 1-3). Mechanistically, E420K is linked to increased phosphorylation of TSC2 at AKT sites S1130/S1132, consistent with AKT-mediated relief of TSC1/2 inhibition over Rheb–mTORC1 (smolen2023quantitativeproteomicsand pages 11-13).

*Quantitative scale of signaling disruption:* In Smolen et al., the phosphoproteome is more extensively rewired in E420K than E198K: **~6% of phosphopeptides** vs **~2.1%** changed by ≥2-fold (smolen2023quantitativeproteomicsand pages 11-13). In the bioRxiv version, the same magnitudes are reported as **~6.1%** and **2.1%** (2023-03; https://doi.org/10.1101/2023.03.27.534397) (smolen2023quantitativeproteomicsanda pages 13-16).

### 2.2 PPP2R5D (HJS1): structural autoinhibition and cell-cycle/mitotic defects as a plausible developmental mechanism
Cryo-EM structural work proposes that PP2A–B56δ (PPP2R5D) exists in **closed/latent** and **open/active** forms, where **long disordered N- and C-terminal arms** establish dual autoinhibition of the **phosphatase active site** and the **substrate-binding groove**. This extended interface spans **>190 Å** and contains “nearly all” residues mutated in ID-associated PPP2R5D (bioRxiv; 2023-04; https://doi.org/10.1101/2023.03.09.530109) (wu2023extendedregulationinterface pages 1-5).

Functionally, these PPP2R5D ID mutations are reported to perturb **activation phosphorylation rates**, and “severe variants” **increase mitotic duration and mitotic error rates** relative to wild-type (wu2023extendedregulationinterface pages 1-5). This supports a mechanistic bridge from altered PP2A regulation → cell-cycle abnormalities → disrupted neurodevelopment.

### 2.3 PPP2R5D (HJS1): PP2A holoenzyme assembly defects and substrate recruitment
A 2024 clinical-genetic series that functionally tested variants reports that most PPP2R5D missense variants **impair PP2A holoenzyme assembly**, while a novel frameshift yields a truncated protein with lower expression (~50 kDa). In vitro, “other missense variants impaired holoenzyme assembly” (except E420K and T536R), supporting a dominant-negative mechanism affecting formation of functional PP2A complexes (Children; 2024-07; https://doi.org/10.3390/children11080897) (jiang2024thirteennewpatients pages 1-2).

### 2.4 PPP2R5D (HJS1) and vasculature: PI3K/AKT/mTOR links to angiogenesis (emerging phenotype)
A 2024 case report proposes a mechanistic link between PPP2R5D dysfunction and **angiogenesis** via dysregulated **PI3K/AKT and PI3K/AKT/mTOR signaling**, motivated by a patient with multiple haemangiomas and a de novo PPP2R5D E198K variant (Pediatric Reports; 2024-12; https://doi.org/10.3390/pediatric16040101) (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4). While evidence is currently case-level, it highlights that PP2A–B56δ can intersect with growth/angiogenic pathways.

### 2.5 PPP2R1A (HJS2): scaffold disruption of PP2A complex formation and brain developmental consequences
PPP2R1A encodes the PP2A **Aα scaffolding subunit**. Variants cluster in structural HEAT repeats and are summarized as disrupting **“holoenzyme stability or subunit binding”** (lee2025clinicalandmolecular pages 1-2). A 2024 knock-in mouse model summary reports that Ppp2r1a M180T and R182W mice recapitulate key disease hallmarks, including neurodevelopmental delay and epileptic seizures (R182W), and indicates alterations in neural cell populations and growth-related pathways (verbinnen2024…ofppp2r1a pages 1-1).

### 2.6 PPP2R5C (HJS spectrum): dominant-negative impairment of substrate and/or C-subunit binding
The latest mechanistic expansion of the HJS spectrum shows PPP2R5C missense variants (B56γ) frequently disrupt **substrate binding** and/or **C-subunit binding**, with most tested variants affecting one or both interaction modes. Quantitatively, variant classes were reported as **2/19 substrate-binding only**, **2/19 C-binding only**, and **15/19 both**; catalytic activity was “variably affected,” and the authors argue for dominant-negative disease mechanisms rather than haploinsufficiency (AJHG; 2025-02; https://doi.org/10.1016/j.ajhg.2025.01.021) (verbinnen2025pathogenicdenovo pages 1-3).

## 3. Recent developments and latest research (prioritize 2023–2024)
### 3.1 2023 quantitative phosphoproteomics establishes a tractable biomarker axis (RPS6) and pharmacologic reversibility
Smolen et al. (2023-09) provide a quantitative molecular phenotype (RPS6 hyperphosphorylation) shared across PPP2R5D variants, and show it is **pharmacologically suppressible** using mTORC1 or p70S6K inhibition (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand pages 11-13).

### 3.2 2023 cryo-EM and allostery: a mechanistic model for how PPP2R5D missense variants perturb regulation
Wu et al. (2023-04) propose that disease mutations lie within an extended autoinhibitory/allosteric interface, linking variant location to altered activation phosphorylation and downstream mitotic phenotypes (wu2023extendedregulationinterface pages 1-5).

### 3.3 2024 genotype–phenotype and functional assembly testing for PPP2R5D
Jiang et al. (2024-07) add new patients and provide functional evidence that many variants reduce holoenzyme assembly, helping connect genotype to biochemical defect (jiang2024thirteennewpatients pages 1-2).

### 3.4 2024 systems-level “expert synthesis” highlights remaining gaps
A 2024 expert perspective emphasizes that while PP2A is a major serine/threonine phosphatase and HJS phenotypes are consistent across subtypes (DD/ID, hypotonia, high epilepsy risk), **“precise molecular mechanisms and affected PP2A brain substrates remain to be defined”** (as summarized in excerpt) (janssens2024newinsightsinto pages 1-1).

## 4. Current applications and real-world implementations
### 4.1 Mechanism-informed candidate therapeutics (preclinical)
**Rapamycin (mTORC1 inhibitor)** and **LY2584702 (p70S6K inhibitor)** suppress PPP2R5D-variant–associated RPS6 hyperphosphorylation in cellular models, suggesting a potential route for mechanism-based therapy prioritization and biomarker-driven readouts in translational studies (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand media 5b277c86).

### 4.2 Model systems used in practice
* Cell models: engineered heterozygous HEK293 variant lines for PPP2R5D E198K/E420K (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand pages 11-13).
* Animal models: Ppp2r1a M180T/R182W knock-in mice for HJS2-like phenotypes (verbinnen2024…ofppp2r1a pages 1-1).

## 5. Expert opinions and analysis (authoritative perspectives)
1) **Convergence with heterogeneity:** The PPP2R5D data indicate convergent downstream activation of mTORC1 output (RPS6), while upstream mechanisms differ by allele (AKT-dependent vs AKT-independent), implying that downstream biomarkers may be more generalizable than upstream pathway nodes for stratification (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand pages 11-13).

2) **Allostery and development:** The cryo-EM autoinhibition model suggests many PPP2R5D disease residues sit in a regulatory interface, making altered conformational switching and phosphorylation-based activation a plausible upstream lesion that can propagate to cell-cycle errors—consistent with neurodevelopmental phenotypes (wu2023extendedregulationinterface pages 1-5).

3) **Unresolved substrate specificity:** The 2024 expert synopsis stresses that identifying which PP2A brain substrates are most critical remains a key gap; this has direct implications for therapy design (targeting downstream signaling vs restoring substrate-specific dephosphorylation) (janssens2024newinsightsinto pages 1-1).

## 6. Relevant statistics and quantitative data (recent)
### 6.1 PPP2R5D/Jordan syndrome quantitative points
* E198K frequency: reported as **~40% of reported cases** in the 2023 preprint text (smolen2023quantitativeproteomicsanda pages 1-5).
* Phosphoproteome changes: **~6% (E420K)** vs **~2.1% (E198K)** of phosphopeptides changed ≥2-fold (smolen2023quantitativeproteomicsand pages 11-13).
* Incidence estimate for PPP2R5D-related disorder: **2.32–2.87 per 100,000 births**, with ~250,000 potentially undiagnosed cases (as estimated in the 2023 bioRxiv excerpt) (wu2023extendedregulationinterface pages 1-5).

### 6.2 PPP2R1A/HJS2 phenotype frequencies (systematic review)
In a 60-patient systematic review, reported phenotype frequencies include: DD/ID **100% (58/58)**, epilepsy **50.9% (29/57)**, structural brain abnormalities **83.1% (49/59)**, corpus callosum abnormalities **40.7% (24/59)**, ventriculomegaly **32.2% (19/59)**, microcephaly **17.2% (10/58)**, macrocephaly **25.9% (15/58)**, dysmorphic features **53.4% (31/58)** (lee2025clinicalandmolecular pages 1-2).

### 6.3 PPP2R5D haemangioma case quantitative clinical measures
A 2024 case report provides neonatal glucose values (35→70 mg/dL over 9 hours) and haemangioma sizes (5×4 mm; 14×9 mm), supporting the vascular phenotype description (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4).

## 7. Knowledge-base style annotations

### 7.1 Causal genes/proteins (HGNC)
* **PPP2R5D (B56δ regulatory subunit)** – HJS1/Jordan syndrome; affects PP2A–B56δ regulation, holoenzyme assembly, and downstream growth signaling (smolen2023quantitativeproteomicsand pages 1-3, wu2023extendedregulationinterface pages 1-5, jiang2024thirteennewpatients pages 1-2).
* **PPP2R1A (Aα scaffold subunit)** – HJS2; affects scaffold-mediated assembly/stability of PP2A holoenzyme (lee2025clinicalandmolecular pages 1-2, verbinnen2024…ofppp2r1a pages 1-1).
* **PPP2CA (Cα catalytic subunit)** – HJS3; catalytic dephosphorylation dysfunction within PP2A system (janssens2024newinsightsinto pages 1-1).
* **PPP2R5C (B56γ regulatory subunit)** – HJS spectrum; dominant-negative disruption of substrate/C-subunit binding (verbinnen2025pathogenicdenovo pages 1-3).

### 7.2 Biological processes (GO-style; evidence-backed candidates)
* Regulation of protein dephosphorylation / serine-threonine phosphatase activity (PP2A-centric) (janssens2024newinsightsinto pages 1-1, verbinnen2025pathogenicdenovo pages 1-3).
* **mTORC1 signaling**, **p70S6K activity**, **RPS6 phosphorylation** (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand pages 11-13).
* **PI3K/AKT signaling** and PI3K/AKT/mTOR axis (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4, smolen2023quantitativeproteomicsand pages 11-13).
* **ERK/MAPK signaling** as an input to mTORC1 in PPP2R5D variants (smolen2023quantitativeproteomicsand pages 1-3).
* **Cell cycle / mitosis** (mitotic duration/error rates) and checkpoint signaling (G2/M, DNA damage response) (wu2023extendedregulationinterface pages 1-5).
* **Angiogenesis / vasculature development** (emerging) (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4).

### 7.3 Cellular components (GO-style)
* **PP2A holoenzyme / heterotrimeric complex** (verbinnen2025pathogenicdenovo pages 1-3, smolen2023quantitativeproteomicsanda pages 1-5).
* **Phosphatase active site** and **substrate-binding groove** in PP2A–B56δ regulatory architecture (wu2023extendedregulationinterface pages 1-5).
* Nucleus and cytoplasm (cellular compartments noted for PPP2R5D-related disorder context) (smolen2023quantitativeproteomicsanda pages 25-27).

### 7.4 Cell types (CL-style; evidence-limited within retrieved texts)
The retrieved 2023–2024 mechanistic sources primarily use **mammalian cell lines** and infer brain impact from disease phenotypes; explicit CL-level brain cell types are not enumerated in the available excerpts. Evidence does support involvement of **neural cell populations** (mouse model summary) and **vascular cells/vasculature** (haemangioma case) (verbinnen2024…ofppp2r1a pages 1-1, comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4).

### 7.5 Anatomical locations (UBERON-style)
* Brain (global), corpus callosum, ventricles (ventriculomegaly), and neurodevelopmental context (lee2025clinicalandmolecular pages 1-2, janssens2024newinsightsinto pages 1-1).
* Vasculature/skin lesions consistent with haemangioma anatomy (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4).

### 7.6 Chemical entities (CHEBI-style) with evidence
* **Rapamycin** (mTORC1 inhibitor): suppresses PPP2R5D variant-associated RPS6 phosphorylation (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand media 5b277c86).
* **LY2584702** (p70S6K inhibitor): suppresses PPP2R5D variant-associated RPS6 phosphorylation (smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsand media 5b277c86).
* Upstream kinases and signaling modulators mentioned mechanistically include **PKA**, **Chk1**, **ATM**, and **cAMP** (as pathway components rather than therapeutics) (wu2023extendedregulationinterface pages 1-5).

### 7.7 Phenotypic manifestations (HP-style; evidence-backed)
Core phenotypes across HJS: DD/ID, language delay, hypotonia, epilepsy, macrocephaly and/or microcephaly, brain malformations (corpus callosum abnormalities, ventriculomegaly), behavioral problems/ASD, and in HJS1 an increased risk of parkinsonism; microtia is noted as more specific to HJS2 in the expert summary (janssens2024newinsightsinto pages 1-1, lee2025clinicalandmolecular pages 1-2, smolen2023quantitativeproteomicsanda pages 1-5).

## 8. Disease progression model (sequence of events)
1) **Initiating event:** de novo (typically) pathogenic missense variant affecting a PP2A subunit (PPP2R5D/PPP2R1A/PPP2R5C; PPP2CA in HJS3) (janssens2024newinsightsinto pages 1-1, verbinnen2025pathogenicdenovo pages 1-3).
2) **Primary molecular defect:** PP2A holoenzyme dysregulation via altered autoinhibition/allostery (PPP2R5D), reduced assembly/stability (PPP2R5D/PPP2R1A), or disrupted substrate/C-subunit binding (PPP2R5C) (wu2023extendedregulationinterface pages 1-5, jiang2024thirteennewpatients pages 1-2, lee2025clinicalandmolecular pages 1-2, verbinnen2025pathogenicdenovo pages 1-3).
3) **Network-level consequences:** altered phosphorylation states across growth-signaling and cell-cycle modules, including mTORC1→p70S6K→RPS6 hyperphosphorylation and mitotic defects (smolen2023quantitativeproteomicsand pages 1-3, wu2023extendedregulationinterface pages 1-5).
4) **Cellular/tissue outcomes:** abnormal neural development (altered neural cell populations in models), disrupted circuit function and seizure susceptibility; in some contexts, dysregulated angiogenic signaling may contribute to vascular phenotypes (verbinnen2024…ofppp2r1a pages 1-1, comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4).
5) **Clinical manifestation:** early-onset developmental delay/ID, hypotonia, epilepsy, structural brain abnormalities and head-size phenotypes, with variable additional features (janssens2024newinsightsinto pages 1-1, lee2025clinicalandmolecular pages 1-2).

## 9. Evidence table (subtypes, mechanisms, phenotypes)
| HJS subtype / gene (HGNC) | Molecular role in PP2A holoenzyme | Key mechanistic findings (2023–2024 prioritized) | Key phenotypes (quantitative where available) | Representative recent references (year; DOI/URL) | Evidence IDs |
|---|---|---|---|---|---|
| HJS1 – PPP2R5D (HGNC:9325) | B' (B56δ) regulatory subunit; substrate-specifying/regulatory subunit of PP2A AC core | Patient-like variants (e.g., E198K, E420K) activate mTORC1→p70S6K with RPS6 hyperphosphorylation; pharmacologic suppression by rapamycin or p70S6K inhibitor (variant-specific AKT dependence) (smolen2023quantitativeproteomicsand pages 11-13, smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsanda pages 13-16, smolen2023quantitativeproteomicsanda pages 1-5, smolen2023quantitativeproteomicsand media 5b277c86). Structural cryo-EM shows extended autoinhibition/allosteric interface in B56δ with ID mutations altering activation phosphorylation and increasing mitotic duration/errors (wu2023extendedregulationinterface pages 1-5). Multiple missense variants impair PP2A holoenzyme assembly; genotype-phenotype correlations (macrocephaly linked to substrate-binding residues) (jiang2024thirteennewpatients pages 11-12, jiang2024thirteennewpatients pages 1-2). Possible PI3K/AKT dysregulation and novel angiogenesis link (multiple haemangiomas) (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4). | Core HJS1 features: developmental delay/ID, hypotonia, seizures, macrocephaly common; variable ASD/behavioral issues; emerging haemangiomas (case-level) (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4, jiang2024thirteennewpatients pages 1-2). | Smolen KA et al., J Biol Chem (2023); 10.1016/j.jbc.2023.105154 (smolen2023quantitativeproteomicsand pages 11-13, smolen2023quantitativeproteomicsand pages 1-3). Smolen KA et al., bioRxiv (2023); 10.1101/2023.03.27.534397 (smolen2023quantitativeproteomicsanda pages 13-16, smolen2023quantitativeproteomicsanda pages 1-5). Wu C-G et al., bioRxiv (2023); 10.1101/2023.03.09.530109 (wu2023extendedregulationinterface pages 1-5). Comisi F et al., Pediatr Rep (2024); 10.3390/pediatric16040101 (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4). Jiang Y et al., Children (2024); 10.3390/children11080897 (jiang2024thirteennewpatients pages 11-12, jiang2024thirteennewpatients pages 1-2). Figure: RPS6 rescue by rapamycin/LY2584702 (smolen2023quantitativeproteomicsand media 5b277c86). | (smolen2023quantitativeproteomicsand pages 11-13, smolen2023quantitativeproteomicsand pages 1-3, smolen2023quantitativeproteomicsanda pages 13-16, smolen2023quantitativeproteomicsanda pages 1-5, wu2023extendedregulationinterface pages 1-5, comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4, jiang2024thirteennewpatients pages 11-12, jiang2024thirteennewpatients pages 1-2, smolen2023quantitativeproteomicsand media 5b277c86) |
| HJS2 – PPP2R1A (HGNC:9322) | Scaffolding Aα subunit; bridges catalytic C subunit with B regulatory subunits | De novo missense variants cluster in HEAT repeats (5–7), disrupt B-subunit binding/holoenzyme stability; genotype–phenotype correlations (HEAT5 p.Arg182Trp/p.Arg183Gln severe) (lee2025clinicalandmolecular pages 1-2, lee2025clinicalandmolecular pages 8-10). Knock-in mice (M180T/R182W) recapitulate neurodevelopmental delay, seizures, behavioral phenotypes (verbinnen2024…ofppp2r1a pages 1-1). | Systematic review (n=60): DD/ID 100% (58/58), structural brain abnorm. 83.1% (49/59) incl. corpus callosum abnorm. 40.7% (24/59), ventriculomegaly 32.2% (19/59), epilepsy 50.9% (29/57), microcephaly 17.2% (10/58), macrocephaly 25.9% (15/58) (lee2025clinicalandmolecular pages 1-2, lee2025clinicalandmolecular pages 8-10). | Lee J et al., Genes (2025); 10.3390/genes16121508 (lee2025clinicalandmolecular pages 1-2, lee2025clinicalandmolecular pages 8-10). Verbinnen I et al., 2024 (mouse model; preprint/unknown journal) (verbinnen2024…ofppp2r1a pages 1-1). | (lee2025clinicalandmolecular pages 1-2, lee2025clinicalandmolecular pages 8-10, verbinnen2024…ofppp2r1a pages 1-1) |
| HJS3 – PPP2CA (HGNC:9309) | Catalytic Cα subunit; executes Ser/Thr dephosphorylation within PP2A holoenzyme | PP2A catalytic dysfunction within PP2A-related HJS spectrum; overlapping phenotypes with other HJS types; mechanistic axis is impaired dephosphorylation of neuronal substrates; precise substrate/variant landscape still emerging (janssens2024newinsightsinto pages 1-1). | Overlap with HJS spectrum: global DD/ID, hypotonia, epilepsy, structural brain anomalies reported; macro/microcephaly variable (janssens2024newinsightsinto pages 1-1). | Janssens V & Verbinnen I., 2024 (review/insight; unknown journal) (janssens2024newinsightsinto pages 1-1). | (janssens2024newinsightsinto pages 1-1) |
| HJS spectrum – PPP2R5C (HGNC:9322? Note: PPP2R5C HGNC:9323) | B' (B56γ) regulatory subunit; substrate-specifying/regulatory subunit of PP2A AC core | Dominant-negative missense variants disrupt substrate and/or C-subunit binding; variant classes: impaired substrate binding (2/19), impaired C binding (2/19), both (15/19); catalytic activity variably affected; overall model supports dominant-negative over simple haploinsufficiency (verbinnen2025pathogenicdenovo pages 1-3). | Neurodevelopmental disorder within HJS spectrum: DD/ID (often milder than other HJS), hypotonia, high epilepsy risk, behavioral problems, mild facial dysmorphism; increased head circumference/macrocephaly frequent (verbinnen2025pathogenicdenovo pages 1-3). | Verbinnen I et al., Am J Hum Genet (2025); 10.1016/j.ajhg.2025.01.021 (verbinnen2025pathogenicdenovo pages 1-3). | (verbinnen2025pathogenicdenovo pages 1-3) |


*Table: Comparative summary of PP2A-subunit Houge-Janssens syndrome subtypes, highlighting molecular roles, 2023–2024 mechanistic advances (e.g., mTORC1→RPS6, cryo-EM autoinhibition, holoenzyme disruption), and key phenotypes with quantitative data where available. Recent references and evidence IDs enable traceability to primary sources.*

## 10. Key figure supporting a translationally actionable mechanism
Smolen et al. show that rapamycin and LY2584702 suppress elevated phospho-RPS6 in PPP2R5D E198K/E420K lines (Figure 7), supporting mTORC1/p70S6K pathway modulation as a mechanism-based intervention concept (smolen2023quantitativeproteomicsand media 5b277c86).

## 11. Evidence items (PMID-oriented note)
The evidence excerpts available in this run did not consistently include PubMed identifiers (PMIDs). Where available in the retrieved texts, PMIDs should be attached at ingestion time; for this report, DOIs/URLs and publication months/years are included for traceability (e.g., J Biol Chem 2023-09, bioRxiv 2023-03/04, Children 2024-07, Pediatric Reports 2024-12) (smolen2023quantitativeproteomicsand pages 1-3, wu2023extendedregulationinterface pages 1-5, jiang2024thirteennewpatients pages 1-2, comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4).



References

1. (janssens2024newinsightsinto pages 1-1): V Janssens and I Verbinnen. New insights into pp2a-related houge-janssens syndrome from model systems and biochemical studies. Unknown journal, 2024.

2. (verbinnen2025pathogenicdenovo pages 1-3): Iris Verbinnen, Sofia Douzgou Houge, Tzung-Chien Hsieh, Hellen Lesmann, Aron Kirchhoff, David Geneviève, Elise Brimble, Lisa Lenaerts, Dorien Haesen, Rebecca J. Levy, Julien Thevenon, Laurence Faivre, Elysa Marco, Jessica X. Chong, Mike Bamshad, Karynne Patterson, Ghayda M. Mirzaa, Kimberly Foss, William Dobyns, Susan M. White, Lynn Pais, Emily O’Heir, Raphaela Itzikowitz, Kirsten A. Donald, Celia Van der Merwe, Alessandro Mussa, Raffaela Cervini, Elisa Giorgio, Tony Roscioli, Kerith-Rae Dias, Carey-Anne Evans, Natasha J. Brown, Anna Ruiz, Juan Pablo Trujillo Quintero, Rachel Rabin, John Pappas, Hai Yuan, Katherine Lachlan, Simon Thomas, Anita Devlin, Michael Wright, Richard Martin, Joanna Karwowska, Renata Posmyk, Nicolas Chatron, Zornitza Stark, Oliver Heath, Martin Delatycki, Rebecca Buchert, Georg-Christoph Korenke, Keri Ramsey, Vinodh Narayanan, Dorothy K. Grange, Judith L. Weisenberg, Tobias B. Haack, Stephanie Karch, Patricia Kipkemoi, Moses Mangi, Karen G.C.B. Bindels de Heus, Marie-Claire Y. de Wit, Tahsin Stefan Barakat, Derek Lim, Géraldine Van Winckel, Rebecca C. Spillmann, Vandana Shashi, Maureen Jacob, Antonia M. Stehr, Peter Krawitz, Gunnar Douzgos Houge, and Veerle Janssens. Pathogenic de novo variants in ppp2r5c cause a neurodevelopmental disorder within the houge-janssens syndrome spectrum. American journal of human genetics, Feb 2025. URL: https://doi.org/10.1016/j.ajhg.2025.01.021, doi:10.1016/j.ajhg.2025.01.021. This article has 4 citations and is from a highest quality peer-reviewed journal.

3. (lee2025clinicalandmolecular pages 1-2): Jaewoong Lee, Ari Ahn, Jaeeun Yoo, and Seungok Lee. Clinical and molecular spectrum of ppp2r1a-related neurodevelopmental disorders: a systematic review. Genes, 16:1508, Dec 2025. URL: https://doi.org/10.3390/genes16121508, doi:10.3390/genes16121508. This article has 0 citations.

4. (smolen2023quantitativeproteomicsand pages 1-3): Kali A. Smolen, Cinta M. Papke, Mark R. Swingle, Alla Musiyenko, Chenchen Li, E. Alan Salter, Ashley D. Camp, Richard E. Honkanen, and Arminja N. Kettenbach. Quantitative proteomics and phosphoproteomics of pp2a-ppp2r5d variants reveal deregulation of rps6 phosphorylation via converging signaling cascades. Journal of Biological Chemistry, 299:105154, Sep 2023. URL: https://doi.org/10.1016/j.jbc.2023.105154, doi:10.1016/j.jbc.2023.105154. This article has 18 citations and is from a domain leading peer-reviewed journal.

5. (smolen2023quantitativeproteomicsand pages 11-13): Kali A. Smolen, Cinta M. Papke, Mark R. Swingle, Alla Musiyenko, Chenchen Li, E. Alan Salter, Ashley D. Camp, Richard E. Honkanen, and Arminja N. Kettenbach. Quantitative proteomics and phosphoproteomics of pp2a-ppp2r5d variants reveal deregulation of rps6 phosphorylation via converging signaling cascades. Journal of Biological Chemistry, 299:105154, Sep 2023. URL: https://doi.org/10.1016/j.jbc.2023.105154, doi:10.1016/j.jbc.2023.105154. This article has 18 citations and is from a domain leading peer-reviewed journal.

6. (smolen2023quantitativeproteomicsanda pages 13-16): Katrina Smolen, CM Papke, M. Swingle, A. Musiyenko, Chun Xing Li, A.D. Camp, R. Honkanen, and AN Kettenbach. Quantitative proteomics and phosphoproteomics of ppp2r5d variants reveal deregulation of rps6 phosphorylation through converging signaling cascades. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.27.534397, doi:10.1101/2023.03.27.534397. This article has 3 citations.

7. (wu2023extendedregulationinterface pages 1-5): Cheng-Guo Wu, Vijaya K. Balakrishnan, Pankaj S. Parihar, Kirill Konovolov, Yu-Chia Chen, Ronald A Merrill, Hui Wei, Bridget Carragher, Ramya Sundaresan, Qiang Cui, Brian E. Wadzinski, Mark R. Swingle, Alla Musiyenko, Richard Honkanen, Wendy K. Chung, Aussie Suzuki, Stefan Strack, Xuhui Huang, and Yongna Xing. Extended regulation interface coupled to the allosteric network and disease mutations in the pp2a-b56δ holoenzyme. bioRxiv, Apr 2023. URL: https://doi.org/10.1101/2023.03.09.530109, doi:10.1101/2023.03.09.530109. This article has 0 citations.

8. (jiang2024thirteennewpatients pages 1-2): Yinmo Jiang, Bingbing Wu, Xi Zhang, Lin Yang, Sujuan Wang, Huiping Li, Shuizhen Zhou, Yanyan Qian, and Huijun Wang. Thirteen new patients of ppp2r5d gene mutation and the fine profile of genotype–phenotype correlation unraveling the pathogenic mechanism underlying macrocephaly phenotype. Children, 11:897, Jul 2024. URL: https://doi.org/10.3390/children11080897, doi:10.3390/children11080897. This article has 1 citations.

9. (comisi2024ppp2r5drelatedneurodevelopmentaldisorder pages 2-4): Francesco Comisi, Consolata Soddu, Francesco Lai, Monica Marica, Michela Lorrai, Giancarlo Mancuso, Sabrina Giglio, and Salvatore Savasta. Ppp2r5d-related neurodevelopmental disorder and multiple haemangiomas: a novel phenotypic trait? Pediatric Reports, 16:1200-1206, Dec 2024. URL: https://doi.org/10.3390/pediatric16040101, doi:10.3390/pediatric16040101. This article has 0 citations.

10. (verbinnen2024…ofppp2r1a pages 1-1): I Verbinnen, L Lenaerts, and Z Callaerts-Végh. … of ppp2r1a m180t and r182w variants in mice recapitulates disease hallmarks of houge-janssens syndrome type 2, a pp2a-related neurodevelopmental disorder. Unknown journal, 2024.

11. (smolen2023quantitativeproteomicsand media 5b277c86): Kali A. Smolen, Cinta M. Papke, Mark R. Swingle, Alla Musiyenko, Chenchen Li, E. Alan Salter, Ashley D. Camp, Richard E. Honkanen, and Arminja N. Kettenbach. Quantitative proteomics and phosphoproteomics of pp2a-ppp2r5d variants reveal deregulation of rps6 phosphorylation via converging signaling cascades. Journal of Biological Chemistry, 299:105154, Sep 2023. URL: https://doi.org/10.1016/j.jbc.2023.105154, doi:10.1016/j.jbc.2023.105154. This article has 18 citations and is from a domain leading peer-reviewed journal.

12. (smolen2023quantitativeproteomicsanda pages 1-5): Katrina Smolen, CM Papke, M. Swingle, A. Musiyenko, Chun Xing Li, A.D. Camp, R. Honkanen, and AN Kettenbach. Quantitative proteomics and phosphoproteomics of ppp2r5d variants reveal deregulation of rps6 phosphorylation through converging signaling cascades. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.27.534397, doi:10.1101/2023.03.27.534397. This article has 3 citations.

13. (smolen2023quantitativeproteomicsanda pages 25-27): Katrina Smolen, CM Papke, M. Swingle, A. Musiyenko, Chun Xing Li, A.D. Camp, R. Honkanen, and AN Kettenbach. Quantitative proteomics and phosphoproteomics of ppp2r5d variants reveal deregulation of rps6 phosphorylation through converging signaling cascades. bioRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.27.534397, doi:10.1101/2023.03.27.534397. This article has 3 citations.

14. (jiang2024thirteennewpatients pages 11-12): Yinmo Jiang, Bingbing Wu, Xi Zhang, Lin Yang, Sujuan Wang, Huiping Li, Shuizhen Zhou, Yanyan Qian, and Huijun Wang. Thirteen new patients of ppp2r5d gene mutation and the fine profile of genotype–phenotype correlation unraveling the pathogenic mechanism underlying macrocephaly phenotype. Children, 11:897, Jul 2024. URL: https://doi.org/10.3390/children11080897, doi:10.3390/children11080897. This article has 1 citations.

15. (lee2025clinicalandmolecular pages 8-10): Jaewoong Lee, Ari Ahn, Jaeeun Yoo, and Seungok Lee. Clinical and molecular spectrum of ppp2r1a-related neurodevelopmental disorders: a systematic review. Genes, 16:1508, Dec 2025. URL: https://doi.org/10.3390/genes16121508, doi:10.3390/genes16121508. This article has 0 citations.