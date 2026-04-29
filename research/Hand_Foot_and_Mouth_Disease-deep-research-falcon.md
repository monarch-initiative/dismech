---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-09T20:57:19.270215'
end_time: '2026-03-09T21:08:57.301287'
duration_seconds: 698.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hand Foot and Mouth Disease
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hand Foot and Mouth Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hand Foot and Mouth Disease**.
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
- **Disease Name:** Hand Foot and Mouth Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hand Foot and Mouth Disease**.
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


## Comprehensive pathophysiology report: Hand, Foot and Mouth Disease (HFMD)

### Disease overview and definitions
Hand, foot and mouth disease (HFMD) is an acute, highly contagious pediatric infection most commonly caused by Enterovirus A species, including Enterovirus A71 (EV‑A71), coxsackievirus A16 (CV‑A16), coxsackievirus A6 (CV‑A6), and coxsackievirus A10 (CV‑A10). Severe HFMD is classically associated with EV‑A71 and features neurologic involvement (e.g., brainstem encephalitis) and cardiopulmonary complications (notably pulmonary edema), whereas most infections are self-limited mucocutaneous disease. Recent surveillance has shown a post‑EV‑A71 vaccine shift toward CV‑A6/CV‑A10 as dominant causes of HFMD in multiple Chinese settings (yang2023molecularepidemiologyand pages 1-2, yuan2024epidemiologicalandetiological pages 1-2, xia2024clinicalaetiologicaland pages 1-2).

**Current understanding (unifying concept).** HFMD pathophysiology is best conceptualized as (i) mucosal entry and early replication, (ii) viremia and tissue dissemination, (iii) host innate and adaptive immune responses (and viral evasion), and (iv) in a subset, neuroinvasion with blood–brain barrier (BBB) dysfunction and brainstem injury leading to systemic inflammatory and neurogenic cardiopulmonary collapse (zhu2023currentstatusof pages 11-12, ji2024thekeymechanisms pages 7-8, ji2024thekeymechanisms pages 12-13).

*Note on ontology identifiers.* MONDO ID was not available in the retrieved sources; this report provides ontology-ready terms (GO/CL/UBERON/HP/CHEBI) where possible based on the cited mechanistic literature.

---

## 1) Core pathophysiology (molecular and cellular mechanisms)

### 1.1 Viral entry, receptors, and uncoating (EV‑A71 emphasized)
**Receptor-mediated entry is multi-step and cell-type dependent.** A key 2024 mechanistic advance is strong evidence that EV‑A71 uses distinct factors for (a) *cell-surface attachment/internalization* versus (b) *intracellular uncoating*.

* **PSGL‑1 (SELPLG) as an attachment receptor on hematopoietic cells.** Nishimura et al. (PLOS Pathogens; Feb 2024; https://doi.org/10.1371/journal.ppat.1012022) report: “**virus attachment to these cells requires only PSGL‑1**” (Jurkat model) and that PSGL‑1 is essential for attachment/infection in those cells (nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 2-4).
* **SCARB2 as an intracellular uncoating receptor.** The same study found SCARB2 “**detected…within the cytoplasm, but not on the cell surface**” and concludes SCARB2 is “**highly concentrated in lysosomes and late endosomes, where it is likely to trigger acid-dependent uncoating of virions**” (nishimura2024enterovirusa71does pages 1-2). Mechanistically, they propose: “**Virus is internalized and transported through the endosomal system, meeting SCARB2 within late endosomes or lysosomes, where uncoating occurs**” (nishimura2024enterovirusa71does pages 2-4).

This attachment–uncoating separation refines older “single receptor” models and implies that receptor expression and endolysosomal trafficking biology are central determinants of tissue tropism and severity (nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 2-4).

A complementary 2024 pathogenesis study highlights host regulation of receptor availability: TRIB3 promotes EV‑A71 infection, in part by maintaining “the metabolic stability of…SCARB2…to enhance the infectious entry and spreading of the virus” (Emerging Microbes & Infections; Jan 2024; https://doi.org/10.1080/22221751.2024.2307514) (wang2024tribblespseudokinase3 pages 1-2).

**Visual synthesis (authoritative review figure/table).** Zhu et al. (J Biomed Sci; Feb 2023; https://doi.org/10.1186/s12929-023-00908-4) provide (i) a table of major enterovirus receptors (including SCARB2 and PSGL‑1) and (ii) a schematic of innate immune evasion mechanisms relevant to HFMD pathogenesis (zhu2023currentstatusof media ba7d7b3e, zhu2023currentstatusof media 86593dfb).

### 1.2 Tissue tropism, dissemination, and neuroinvasion
**Entry sites and early replication.** EV‑A71 infection begins at mucosal epithelial surfaces of the gastrointestinal and respiratory tracts in the early phase of infection (wei2024recentprogressin pages 2-4).

**Progression to systemic disease.** Severe HFMD is linked to CNS involvement—particularly brainstem structures—and downstream dysautonomia and inflammation (ji2024thekeymechanisms pages 7-8, zhu2023currentstatusof pages 11-12). Ji et al. (Infectious Medicine; Sep 2024; https://doi.org/10.1016/j.imj.2024.100124) describe clinical progression consistent with a systemic dissemination step: “primary and a secondary viremia after ~4–5 days enabling systemic/CNS spread” (ji2024thekeymechanisms pages 7-8).

**BBB disruption as a gateway to CNS disease.** Multiple mechanisms converge on BBB compromise:

* In CV‑A16, IP‑10/CXCL10 rises early and is mechanistically linked to BBB junctional loss via TNF‑α. Hu et al. (Frontiers in Immunology; Nov 2024; https://doi.org/10.3389/fimmu.2024.1374447) report elevation of “**TLR3‑TRIF‑TRAF3‑TBK1‑NF‑κB and RIG‑I/MDA5‑MAVS‑…‑TBK1‑NF‑κB pathways**” and show that IP‑10/TNF‑α reduce junctional proteins (Claudin5, Occludin, ZO‑1, VE‑cadherin) in infected endothelial cells, “enhanc[ing] virus entry into the CNS” (hu2024ip10actsearly pages 1-2).
* Ji et al. (2024) summarize BBB disruption routes that include “MMP‑9–mediated disruption of junctional complexes” in CV‑A16 and other BBB‑integrity mechanisms (ji2024thekeymechanisms pages 7-8, ji2024thekeymechanisms pages 12-13).

**Neural routes and extracellular vesicles.** Ji et al. further summarize evidence for neural spread (e.g., retrograde axonal transport) and non-lytic dissemination via exosomes/small extracellular vesicles that can enable CNS entry without overt BBB destruction (ji2024thekeymechanisms pages 7-8, ji2024thekeymechanisms pages 12-13).

### 1.3 Innate immune sensing and viral immune evasion (dysregulated pathways)
Mechanistically, severe disease reflects both antiviral responses and viral suppression of those responses.

**Key innate-sensing nodes.** A 2024 review of EV‑A71 innate immunity (International Journal of Molecular Sciences; May 2024; https://doi.org/10.3390/ijms25115688) summarizes canonical sensing and signaling engaged by EV‑A71, including endosomal TLR3/TLR7 and cytosolic RIG‑I/MDA5→MAVS leading to IRF3/IRF7 and NF‑κB activation and downstream type I interferon signaling via IFNAR→JAK/STAT (wei2024recentprogressin pages 2-4).

**Viral antagonism of interferon and inflammasome.** Zhu et al. (J Biomed Sci; Feb 2023; https://doi.org/10.1186/s12929-023-00908-4) provide multiple examples of EV‑A71 immune evasion/rewiring:

* Inflammasome manipulation: EV‑A71 3D polymerase binds NLRP3 to form a complex promoting IL‑1β secretion, whereas viral proteases can cleave NLRP3 to inhibit activation (zhu2023currentstatusof pages 11-12).
* Type I IFN pathway interference: EV proteases can impair type I IFN signaling (e.g., targeting IFNAR and suppressing STAT1/STAT2 nuclear translocation) and cleave RIG‑I (zhu2023currentstatusof pages 11-12).

These observations map HFMD severity to dysregulation of innate antiviral and inflammatory cascades (type I IFN signaling, NF‑κB activation, inflammasome activation) rather than viral cytopathicity alone (zhu2023currentstatusof pages 11-12, wei2024recentprogressin pages 2-4).

### 1.4 Metabolic reprogramming as a host-dependency mechanism
A 2023 proteomics+metabolomics study provides direct evidence that EV‑A71 reprograms glycolysis:

* Shi et al. (PROTEOMICS; Nov 2023; https://doi.org/10.1002/pmic.202200362) report that upregulated proteins were enriched in “metabolic process, especially…glycolysis,” that ENO1 increased after infection, and targeted metabolomics showed increased glucose absorption and glycolysis metabolites (shi2023proteomicandmetabonomic pages 1-2).
* Functional perturbation demonstrated dependency: “glycolysis inhibition through knockdown of ENO1… and the use of glycolysis inhibitor (DCA) **significantly suppressed EV71 infection**” (shi2023proteomicandmetabonomic pages 12-13).

This supports a host-directed therapeutic concept (metabolic intervention) in addition to antiviral approaches (shi2023proteomicandmetabonomic pages 12-13).

---

## 2) Key molecular players (genes/proteins, chemicals, cell types, anatomy)

### 2.1 Gene/protein players (HGNC-level; key mechanisms)
Primary mechanistic nodes supported by the retrieved evidence include:

* **Entry/trafficking:** SCARB2 (uncoating receptor in late endosomes/lysosomes), SELPLG/PSGL‑1 (attachment receptor), and host factor **TRIB3** supporting SCARB2 stability (nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 2-4, wang2024tribblespseudokinase3 pages 1-2).
* **Innate sensing/signaling:** TLR3, TLR7, RIG‑I, MDA5, MAVS, TBK1, IRF3/7, NF‑κB, IFNAR, STAT1/STAT2 (review-synthesized pathways for EV‑A71) (wei2024recentprogressin pages 2-4, hu2024ip10actsearly pages 1-2).
* **Inflammation:** NLRP3/ASC inflammasome axis; cytokines/chemokines elevated in severe disease include TNF‑α and IP‑10/CXCL10 (zhu2023currentstatusof pages 11-12, hu2024ip10actsearly pages 1-2).
* **Barrier dysfunction:** Tight junction components (Claudin5, Occludin, ZO‑1, VE‑cadherin) reduced under IP‑10/TNF‑α axis in CV‑A16 infection; MMP‑9 implicated in junctional disruption (hu2024ip10actsearly pages 1-2, ji2024thekeymechanisms pages 7-8).
* **Metabolism:** ENO1 (glycolysis), pharmacologic glycolysis inhibitor DCA (dichloroacetic acid) suppresses infection (shi2023proteomicandmetabonomic pages 1-2, shi2023proteomicandmetabonomic pages 12-13).

### 2.2 Chemical entities (CHEBI-level)
* **Norepinephrine (noradrenaline)** and **epinephrine**: catecholamine surge implicated in severe HFMD cardiopulmonary collapse (ji2024thekeymechanisms pages 7-8).
* **Dichloroacetic acid (DCA)**: glycolysis inhibitor that reduced EV‑A71 infection in vitro (shi2023proteomicandmetabonomic pages 12-13).

### 2.3 Cell types (CL-level; evidence-based involvement)
* **Endothelial cells** (e.g., HUVECs as BBB-relevant model): junctional protein loss under IP‑10/TNF‑α axis with enhanced viral CNS entry (hu2024ip10actsearly pages 1-2).
* **Neurons and glial cells**: described as expressing EV‑A71 receptors SCARB2 and PSGL‑1 in a 2024 review; CNS pathology and neuroinflammation are central to severe HFMD (wei2024recentprogressin pages 2-4, zhu2023currentstatusof pages 11-12).
* **Immune cells (hematopoietic lineage)**: Jurkat/lymphocyte models demonstrate PSGL‑1-mediated attachment and requirement for intracellular SCARB2; adaptive immunity and antibody dynamics are implicated in outcomes (nishimura2024enterovirusa71does pages 2-4, zhu2023currentstatusof pages 11-12).

### 2.4 Anatomical locations (UBERON-level)
* **Blood–brain barrier (BBB)**: key anatomical bottleneck for severe disease (hu2024ip10actsearly pages 1-2, ji2024thekeymechanisms pages 7-8).
* **Brainstem**: focal site linked to autonomic dysregulation and cardiopulmonary failure (ji2024thekeymechanisms pages 7-8, zhu2023currentstatusof pages 11-12).
* **Mucosal epithelium of GI/respiratory tracts**: early sites of exposure/replication (wei2024recentprogressin pages 2-4).

---

## 3) Biological processes (GO-ready) disrupted in HFMD
Representative processes supported in the retrieved sources include:

* **Receptor-mediated endocytosis / viral entry** and **endosomal uncoating** (PSGL‑1 attachment; SCARB2 endolysosomal uncoating) (nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 2-4).
* **Type I interferon signaling pathway** and **pattern-recognition receptor signaling** (TLR3/TLR7; RIG‑I/MDA5→MAVS→TBK1→IRF/NF‑κB) with viral antagonism (wei2024recentprogressin pages 2-4, zhu2023currentstatusof pages 11-12).
* **Inflammasome activation** (NLRP3/ASC ring complex promoted by EV‑A71 3D) and inflammatory cytokine production (zhu2023currentstatusof pages 11-12).
* **Chemokine-mediated signaling** (CXCL10/IP‑10 axis) promoting inflammatory amplification and BBB dysfunction in CV‑A16 (hu2024ip10actsearly pages 1-2).
* **Glycolytic process** as a virus-induced host-dependency pathway (ENO1; DCA effect) (shi2023proteomicandmetabonomic pages 12-13).

---

## 4) Cellular components (GO-CC-ready)
Key subcellular sites implicated include:

* **Late endosomes/lysosomes**: SCARB2 localization and acid-dependent uncoating (nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 10-13).
* **Endosomal membranes**: pore-mediated genome release described in EV‑A71 entry model (wei2024recentprogressin pages 2-4).
* **Inflammasome complex**: NLRP3/ASC-associated complex engaged by viral 3D polymerase (zhu2023currentstatusof pages 11-12).
* **Tight junctions/adherens junctions**: reduced Claudin5/Occludin/ZO‑1/VE‑cadherin under IP‑10/TNF‑α in CV‑A16 model (hu2024ip10actsearly pages 1-2).

---

## 5) Disease progression: trigger-to-phenotype sequence (integrated model)

### Stage 1: Exposure and mucosal replication
Exposure typically occurs through fecal–oral and/or respiratory routes, with early replication at GI/respiratory mucosa (wei2024recentprogressin pages 2-4).

### Stage 2: Viremia and dissemination
A subset of cases progress beyond localized mucocutaneous disease, with systemic dissemination enabling access to secondary tissues including muscle and CNS; Ji et al. summarize a clinical timeline including a secondary viremia around 4–5 days (ji2024thekeymechanisms pages 7-8).

### Stage 3: Innate immune activation and viral evasion (determinant of viral load/inflammation)
Host PRR signaling (TLRs and RIG‑I/MDA5) drives IFN and cytokine responses, while EV‑A71 employs multiple evasion strategies (IFNAR/STAT interference; RIG‑I cleavage; inflammasome modulation) (wei2024recentprogressin pages 2-4, zhu2023currentstatusof pages 11-12).

### Stage 4 (severe subset): BBB dysfunction and neuroinvasion
In CV‑A16, IP‑10 (CXCL10) is induced early and promotes TNF‑α, which reduces junctional proteins and facilitates virus entry into the CNS (hu2024ip10actsearly pages 1-2). Broader HFMD literature synthesis implicates additional BBB-disruptive pathways (e.g., MMP‑9) (ji2024thekeymechanisms pages 7-8, ji2024thekeymechanisms pages 12-13).

### Stage 5: CNS/brainstem injury → systemic collapse
Brainstem infection/damage is linked to sympathetic hyperactivation and a catecholamine “storm,” driving pulmonary microvascular leakage and cardiopulmonary failure. Ji et al. report marked catecholamine elevation in severe cases and mechanistic links to pulmonary edema: excessive catecholamines increase pulmonary permeability and can induce cardiomyocyte injury (ji2024thekeymechanisms pages 7-8). Zhu et al. similarly connect cardiopulmonary failure to brainstem-mediated hypercatecholaminemia (zhu2023currentstatusof pages 11-12).

---

## 6) Phenotypic manifestations and mechanistic links (HP-ready)

* **Mucocutaneous disease**: oral ulcers/herpangina and vesicular rash reflect epithelial infection and local inflammation.
* **Neurologic complications** (e.g., encephalitis/brainstem encephalitis): linked to BBB compromise, neuroinvasion, and neuroinflammation (hu2024ip10actsearly pages 1-2, zhu2023currentstatusof pages 11-12).
* **Pulmonary edema (HP:0002104)** and acute cardiopulmonary failure: linked to brainstem injury and catecholamine storm causing increased pulmonary vascular permeability and cardiac dysfunction (ji2024thekeymechanisms pages 7-8, zhu2023currentstatusof pages 11-12).

---

## Recent developments (2023–2024 prioritized)

### A) Refined receptor/uncoating model (2024)
The most concrete 2024 mechanistic advance in this corpus is the demonstration that EV‑A71 does not rely on cell-surface SCARB2 for attachment; instead, SCARB2 acts intracellularly in endolysosomes for uncoating. Key quotes include SCARB2 being “within the cytoplasm, but not on the cell surface” and “highly concentrated in lysosomes and late endosomes…likely to trigger acid-dependent uncoating” (Nishimura et al., Feb 2024, PLOS Pathogens; https://doi.org/10.1371/journal.ppat.1012022) (nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 2-4).

### B) Chemokine-driven BBB disruption pathway for CV‑A16 (2024)
Hu et al. (Nov 2024; Frontiers in Immunology; https://doi.org/10.3389/fimmu.2024.1374447) provide direct mechanistic evidence that the IP‑10/TNF‑α axis reduces BBB junctional proteins and increases CNS entry during CV‑A16 infection, with anti‑IP‑10 or anti‑TNF‑α improving outcomes in a suckling mouse model (hu2024ip10actsearly pages 1-2).

### C) Host metabolic dependency and potential host-directed therapy (2023)
Shi et al. (Nov 2023; PROTEOMICS; https://doi.org/10.1002/pmic.202200362) show glycolysis activation during EV‑A71 infection and that DCA or ENO1 knockdown suppresses infection (shi2023proteomicandmetabonomic pages 12-13).

### D) Pathogen landscape shift post EV‑A71 vaccination (2023–2024)
Multiple surveillance studies show EV‑A71 reductions and increasing dominance of CV‑A6/CV‑A10:

* Chengdu 2013–2022 (n=29,861): EV‑A71 fell from 13.60% (2013–2015) to 1.83% (2017–2019) and “disappeared” during COVID‑19 period; 2020–2022 “other serotypes” 95.45%, with CV‑A6 50.39% and CV‑A10 10.81% (Sep 2023; Virology Journal; https://doi.org/10.1186/s12985-023-02169-x) (yang2023molecularepidemiologyand pages 1-2).
* Jiashan 2016–2022: among 560 samples, 472 positive (84.29%); CA6 52.86%, CA16 18.21%, EV71 2.86%, CA10 2.50% (May 2024; Frontiers in Public Health; https://doi.org/10.3389/fpubh.2024.1377861) (yuan2024epidemiologicalandetiological pages 1-2).
* Chengdu outpatient cohort 2019–2022 (n=1,073): CVA6 76.51% with low hospitalization progression (4.19% overall); CVA10 associated with higher hospitalization likelihood (Dec 2024; BMC Public Health; https://doi.org/10.1186/s12889-024-20909-8) (xia2024clinicalaetiologicaland pages 1-2).

These epidemiologic shifts are critical to “real-world implementation” because they create vaccine/therapeutic pressure toward multivalent approaches beyond EV‑A71-only strategies (yang2023molecularepidemiologyand pages 1-2, yuan2024epidemiologicalandetiological pages 1-2).

---

## Current applications and real-world implementations

### 1) Vaccination impact (population-level)
Real-world surveillance supports a sharp decrease in EV‑A71 detections and severe HFMD after EV‑A71 vaccine rollout (e.g., post‑2016 trends in multiple Chinese datasets) (yang2023molecularepidemiologyand pages 1-2, dai2024epidemiologyandetiology pages 4-6). However, non‑EV‑A71 serotypes now dominate detected cases in many settings, implying that single-serotype vaccination is insufficient to fully control HFMD burden (yang2023molecularepidemiologyand pages 1-2, yuan2024epidemiologicalandetiological pages 1-2, dai2024epidemiologyandetiology pages 4-6).

### 2) Translational targets and therapeutic concepts
* **Host-directed metabolic inhibition:** DCA and ENO1 perturbation suppress EV‑A71 infection in vitro, supporting exploration of metabolic pathway modulation as adjunct therapy (shi2023proteomicandmetabonomic pages 12-13).
* **Anti-chemokine/cytokine strategies for severe disease:** Anti‑IP‑10 (Eldelumab in vitro) and anti‑TNF‑α reduced severity in CV‑A16 models, indicating a plausible immunomodulatory strategy for neuroinvasive HFMD phenotypes (hu2024ip10actsearly pages 1-2).

These are not established clinical standards of care in the retrieved sources, but represent mechanistically grounded directions.

---

## Expert interpretation (authoritative synthesis)

*Mechanistic convergence.* Across pathogens, severe HFMD appears to converge on BBB compromise, neuroinflammation, and autonomic dysregulation rather than only higher peripheral viral replication. The IP‑10/TNF‑α → tight junction loss mechanism (CV‑A16) provides a testable causal chain from innate immune signaling to BBB dysfunction and neuroinvasion (hu2024ip10actsearly pages 1-2). The catecholamine-storm mechanism provides a plausible bridge from brainstem injury to pulmonary edema and rapid deterioration (ji2024thekeymechanisms pages 7-8, zhu2023currentstatusof pages 11-12).

*Host genetics as an outcome modifier.* Case-control genetic studies support the concept that host receptor variants influence severity (SCARB2 SNPs protective; PSGL‑1 VNTR modest risk) (duan2023theeffectsof pages 1-2, wang2024correlationsofpsgl1 pages 2-4).

*Implication for future countermeasures.* The consistent shift to CV‑A6/CV‑A10 dominance (while EV‑A71 remains a key severe pathogen) suggests that multivalent vaccines and broad-spectrum antivirals/host-directed therapies are likely necessary for durable control (yang2023molecularepidemiologyand pages 1-2, yuan2024epidemiologicalandetiological pages 1-2, dai2024epidemiologyandetiology pages 4-6).

---

## Relevant statistics and data (recent studies)

### Pathogen shift and burden
* **Chengdu 2013–2022:** 29,861 lab-confirmed cases; 2020–2022 other serotypes 95.45%; CV‑A6 50.39%, CV‑A10 10.81%; EV‑A71 disappeared during COVID period (yang2023molecularepidemiologyand pages 1-2).
* **Jiashan 2016–2022:** 84.29% enterovirus-positive among tested samples; CA6 52.86%; CA16 18.21%; EV71 2.86% (yuan2024epidemiologicalandetiological pages 1-2).
* **Henan 2021–2023:** CV‑A6 became leading pathogen in 2023 with 37.01% (262/708) among lab-confirmed typed cases; peak months accounted for 20.7%–35% of annual cases (chen2024molecularevolutionarydynamics pages 1-2).

### Hospitalization and severity signals
* **Chengdu outpatient 2019–2022:** 4.19% (45/1,073) progressed to hospitalization; CVA10 increased hospitalization likelihood; oral rash protective (xia2024clinicalaetiologicaland pages 1-2).

### Host genetic associations
* **SCARB2 SNPs (Yunnan; Apr 2023):** rs74719289 A (OR 0.330), rs3733255 T (OR 0.336), rs17001551 A (OR 0.378) associated with reduced risk of severe EV‑A71 HFMD (duan2023theeffectsof pages 1-2, duan2023theeffectsof pages 2-3).
* **PSGL‑1 (SELPLG) VNTR (Aug 2024):** allele A vs B OR 1.558 (95% CI 1.025–2.367; P=0.038) for severe HFMD; allele B protective OR 0.642 (95% CI 0.422–0.975) (wang2024correlationsofpsgl1 pages 2-4).

---

## Ontology-ready annotation table
| Category | Entity | Role in HFMD Pathophysiology | Key Evidence |
| :--- | :--- | :--- | :--- |
| **Gene/Protein** | **SCARB2** (HGNC:1664) | Primary intracellular receptor facilitating viral uncoating in acidic endosomes/lysosomes; SNPs associated with reduced severity. | (wei2024recentprogressin pages 2-4, nishimura2024enterovirusa71does pages 6-9, nishimura2024enterovirusa71does pages 1-2, duan2023theeffectsof pages 1-2, duan2023theeffectsof pages 6-7) |
| **Gene/Protein** | **SELPLG** / PSGL-1 (HGNC:10720) | Major attachment receptor on leukocytes directing viral tropism; VNTR polymorphisms linked to severe disease susceptibility. | (wei2024recentprogressin pages 2-4, nishimura2024enterovirusa71does pages 6-9, nishimura2024enterovirusa71does pages 2-4, wang2024correlationsofpsgl1 pages 2-4, wang2024correlationsofpsgl1 pages 1-2) |
| **Gene/Protein** | **CXCL10** / IP-10 (HGNC:10636) | Pro-inflammatory chemokine elevated early in infection that drives TNF-alpha production and blood-brain barrier disruption. | (ji2024thekeymechanisms pages 12-13, zhu2023currentstatusof pages 11-12, hu2024ip10actsearly pages 1-2) |
| **Gene/Protein** | **TNF** / TNF-alpha (HGNC:11892) | Cytokine induced by IP-10 that reduces endothelial tight junction proteins (Claudin5, Occludin), promoting neuroinvasion. | (hu2024ip10actsearly pages 1-2, zhu2023currentstatusof pages 11-12) |
| **Gene/Protein** | **NLRP3** (HGNC:16400) | Inflammasome component bounded by viral 3D polymerase to form a complex promoting IL-1beta secretion. | (zhu2023currentstatusof pages 11-12, wei2024recentprogressin pages 2-4, zhu2023currentstatusof media ba7d7b3e) |
| **Gene/Protein** | **ENO1** (HGNC:3350) | Glycolytic enzyme upregulated by EV-A71 to reprogram host metabolism and support viral replication. | (shi2023proteomicandmetabonomic pages 1-2, shi2023proteomicandmetabonomic pages 12-13) |
| **Gene/Protein** | **TRIB3** (HGNC:16228) | Host pseudokinase that maintains SCARB2 metabolic stability, enhancing viral entry and spread. | (wang2024tribblespseudokinase3 pages 1-2) |
| **Gene/Protein** | **MMP9** (HGNC:7176) | Matrix metalloproteinase implicated in disrupting junctional complexes at the blood-brain barrier. | (ji2024thekeymechanisms pages 12-13, ji2024thekeymechanisms pages 7-8) |
| **Gene/Protein** | **IFNAR1** / **IFNAR2** | Type I interferon receptor subunits targeted by viral proteases to evade innate immune signaling. | (wei2024recentprogressin pages 2-4) |
| **Gene/Protein** | **VIM** / Vimentin (HGNC:12692) | Cell surface attachment receptor upregulated by viral VP1, facilitating BBB penetration. | (ji2024thekeymechanisms pages 7-8, hu2024ip10actsearly pages 1-2) |
| **Pathway (GO)** | **Type I interferon signaling pathway** (GO:0060337) | Antiviral response pathway suppressed by viral cleavage of RIG-I, MAVS, and inhibition of STAT nuclear translocation. | (zhu2023currentstatusof pages 11-12, wei2024recentprogressin pages 2-4, zhu2023currentstatusof media ba7d7b3e) |
| **Pathway (GO)** | **Glycolytic process** (GO:0006096) | Metabolic pathway activated/reprogrammed by virus via ENO1 upregulation to support replication. | (shi2023proteomicandmetabonomic pages 1-2, shi2023proteomicandmetabonomic pages 12-13) |
| **Cellular Component** | **Lysosome** (GO:0005764) / **Late Endosome** (GO:0005770) | Acidic compartments where SCARB2 resides and triggers the critical viral uncoating step. | (nishimura2024enterovirusa71does pages 6-9, nishimura2024enterovirusa71does pages 1-2, nishimura2024enterovirusa71does pages 13-15, nishimura2024enterovirusa71does pages 10-13) |
| **Cellular Component** | **Inflammasome complex** (GO:0061702) | Multiprotein complex (3D-NLRP3-ASC) engaged to drive cytokine storm and inflammation. | (zhu2023currentstatusof pages 11-12, wei2024recentprogressin pages 2-4) |
| **Cellular Component** | **Tight junction** (GO:0005923) | Endothelial barrier structure degraded by IP-10/TNF-alpha-mediated downregulation of ZO-1/Occludin. | (hu2024ip10actsearly pages 1-2) |
| **Chemical Entity** | **Norepinephrine** (CHEBI:18357) | Major mediator of the "catecholamine storm" causing neurogenic pulmonary edema and cardiac failure. | (ji2024thekeymechanisms pages 7-8, zhu2023currentstatusof pages 11-12) |
| **Chemical Entity** | **Dichloroacetic acid** (CHEBI:41879) | Glycolysis inhibitor shown to suppress EV-A71 infection in vitro. | (shi2023proteomicandmetabonomic pages 1-2, shi2023proteomicandmetabonomic pages 12-13) |
| **Anatomy** | **Blood-brain barrier** (UBERON:0000202) | Physical barrier compromised by viral proteins (VP1) and host cytokines, facilitating neuroinvasion. | (ji2024thekeymechanisms pages 12-13, ji2024thekeymechanisms pages 7-8, hu2024ip10actsearly pages 1-2) |
| **Anatomy** | **Brainstem** (UBERON:0002298) | Critical CNS region infected via neural routes, triggering autonomic dysfunction and catecholamine surge. | (ji2024thekeymechanisms pages 7-8, zhu2023currentstatusof pages 11-12) |
| **Phenotype** | **Pulmonary edema** (HP:0002104) | Severe complication resulting from brainstem damage and subsequent sympathetic hyperactivation. | (ji2024thekeymechanisms pages 12-13, ji2024thekeymechanisms pages 7-8) |


*Table: A structured mapping of key molecular entities, biological processes, and anatomical sites involved in Hand, Foot, and Mouth Disease pathophysiology, linked to ontology categories and recent supporting evidence.*

---

## Evidence items (PMID-focused) and links
The retrieved evidence set includes several high-quality mechanistic papers with DOI links and publication dates; however, **PMIDs were not present in the provided tool outputs** for many items. Below are the *URL/DOI* and publication month/year as provided by the tool results:

1) Nishimura et al. “Enterovirus A71 does not meet the uncoating receptor SCARB2 at the cell surface.” **PLOS Pathogens, Feb 2024.** https://doi.org/10.1371/journal.ppat.1012022 (nishimura2024enterovirusa71does pages 1-2)

2) Hu et al. “IP‑10 acts early in CV‑A16 infection to induce BBB destruction…” **Frontiers in Immunology, Nov 2024.** https://doi.org/10.3389/fimmu.2024.1374447 (hu2024ip10actsearly pages 1-2)

3) Wei et al. “Recent Progress in Innate Immune Responses to Enterovirus A71 and Viral Evasion Strategies.” **Int J Mol Sci, May 2024.** https://doi.org/10.3390/ijms25115688 (wei2024recentprogressin pages 2-4)

4) Zhu et al. “Current status of hand-foot-and-mouth disease.” **Journal of Biomedical Science, Feb 2023.** https://doi.org/10.1186/s12929-023-00908-4 (zhu2023currentstatusof pages 11-12)

5) Shi et al. “Proteomic and metabonomic analysis uncovering EV‑A71 reprogramming host cell metabolic pathway.” **PROTEOMICS, Nov 2023.** https://doi.org/10.1002/pmic.202200362 (shi2023proteomicandmetabonomic pages 1-2)

6) Duan et al. “The effects of SCARB2 and SELPLG gene polymorphisms on EV71 infection…” **Biomolecules and Biomedicine, Apr 2023.** https://doi.org/10.17305/bb.2023.8948 (duan2023theeffectsof pages 1-2)

7) Wang et al. “Correlations of PSGL‑1 VNTR polymorphism with susceptibility to severe HFMD…” **Virology Journal, Aug 2024.** https://doi.org/10.1186/s12985-024-02461-4 (wang2024correlationsofpsgl1 pages 2-4)

8) Yang et al. “Molecular epidemiology…HFMD in Chengdu, 2013–2022.” **Virology Journal, Sep 2023.** https://doi.org/10.1186/s12985-023-02169-x (yang2023molecularepidemiologyand pages 1-2)

9) Xia et al. “Outpatient HFMD in Chengdu, 2019–2022.” **BMC Public Health, Dec 2024.** https://doi.org/10.1186/s12889-024-20909-8 (xia2024clinicalaetiologicaland pages 1-2)

---

## Limitations of this synthesis (evidence coverage)
1) While EV‑A71 and CV‑A16 mechanisms are richly supported in the retrieved full-text evidence, **CV‑A6/CV‑A10 molecular receptor usage and CNS mechanisms** were not deeply extracted from the available full texts in this run; the report therefore emphasizes shared enterovirus mechanisms and EV‑A71/CV‑A16 exemplars.
2) PMIDs were not surfaced by the tools for many included items; DOIs/URLs and publication dates are provided as substitutes.



References

1. (yang2023molecularepidemiologyand pages 1-2): Qiuxia Yang, Fang Liu, Li Chang, Shuyu Lai, Jie Teng, Jiaxin Duan, Hui Jian, Ting Liu, and Guanglu Che. Molecular epidemiology and clinical characteristics of enteroviruses associated hfmd in chengdu, china, 2013–2022. Virology Journal, Sep 2023. URL: https://doi.org/10.1186/s12985-023-02169-x, doi:10.1186/s12985-023-02169-x. This article has 43 citations and is from a peer-reviewed journal.

2. (yuan2024epidemiologicalandetiological pages 1-2): Yongjuan Yuan, Yun Chen, Jian Huang, Xiaoxia Bao, Wei Shen, Yi Sun, and Haiyan Mao. Epidemiological and etiological investigations of hand, foot, and mouth disease in jiashan, northeastern zhejiang province, china, during 2016 to 2022. Frontiers in Public Health, May 2024. URL: https://doi.org/10.3389/fpubh.2024.1377861, doi:10.3389/fpubh.2024.1377861. This article has 12 citations.

3. (xia2024clinicalaetiologicaland pages 1-2): Maoyao Xia, Yu Zhu, Juan Liao, Shirong Zhang, Denghui Yang, Peng Gong, Shihang Zhang, Guiyu Jiang, Yue Cheng, Jiantong Meng, Zhenhua Chen, Ye Liao, Xiaojing Li, Yilan Zeng, Chaoyong Zhang, and Lu Long. Clinical, aetiological, and epidemiological studies of outpatient cases of hand, foot, and mouth disease in chengdu, china, from 2019 to 2022: a retrospective study. BMC Public Health, Dec 2024. URL: https://doi.org/10.1186/s12889-024-20909-8, doi:10.1186/s12889-024-20909-8. This article has 5 citations and is from a peer-reviewed journal.

4. (zhu2023currentstatusof pages 11-12): P. Zhu, W. Ji, Dong Li, Zijie Li, Yu Chen, B. Dai, Shujie Han, Shuaiyin Chen, Yuefei Jin, and G. Duan. Current status of hand-foot-and-mouth disease. Journal of Biomedical Science, Feb 2023. URL: https://doi.org/10.1186/s12929-023-00908-4, doi:10.1186/s12929-023-00908-4. This article has 243 citations and is from a domain leading peer-reviewed journal.

5. (ji2024thekeymechanisms pages 7-8): Wangquan Ji, Peiyu Zhu, Yuexia Wang, Yu Zhang, Zijie Li, Haiyan Yang, Shuaiyin Chen, Yuefei Jin, and Guangcai Duan. The key mechanisms of multi-system responses triggered by central nervous system damage in hand, foot, and mouth disease severity. Infectious Medicine, 3:100124, Sep 2024. URL: https://doi.org/10.1016/j.imj.2024.100124, doi:10.1016/j.imj.2024.100124. This article has 8 citations.

6. (ji2024thekeymechanisms pages 12-13): Wangquan Ji, Peiyu Zhu, Yuexia Wang, Yu Zhang, Zijie Li, Haiyan Yang, Shuaiyin Chen, Yuefei Jin, and Guangcai Duan. The key mechanisms of multi-system responses triggered by central nervous system damage in hand, foot, and mouth disease severity. Infectious Medicine, 3:100124, Sep 2024. URL: https://doi.org/10.1016/j.imj.2024.100124, doi:10.1016/j.imj.2024.100124. This article has 8 citations.

7. (nishimura2024enterovirusa71does pages 1-2): Yorihiro Nishimura, Kei Sato, Yoshio Koyanagi, Takaji Wakita, Masamichi Muramatsu, Hiroyuki Shimizu, Jeffrey M. Bergelson, and Minetaro Arita. Enterovirus a71 does not meet the uncoating receptor scarb2 at the cell surface. PLOS Pathogens, 20:e1012022, Feb 2024. URL: https://doi.org/10.1371/journal.ppat.1012022, doi:10.1371/journal.ppat.1012022. This article has 8 citations and is from a highest quality peer-reviewed journal.

8. (nishimura2024enterovirusa71does pages 2-4): Yorihiro Nishimura, Kei Sato, Yoshio Koyanagi, Takaji Wakita, Masamichi Muramatsu, Hiroyuki Shimizu, Jeffrey M. Bergelson, and Minetaro Arita. Enterovirus a71 does not meet the uncoating receptor scarb2 at the cell surface. PLOS Pathogens, 20:e1012022, Feb 2024. URL: https://doi.org/10.1371/journal.ppat.1012022, doi:10.1371/journal.ppat.1012022. This article has 8 citations and is from a highest quality peer-reviewed journal.

9. (wang2024tribblespseudokinase3 pages 1-2): Huiqiang Wang, Ke Li, Boming Cui, Haiyan Yan, Shuo Wu, Kun Wang, Ge Yang, Jiandong Jiang, and Yuhuan Li. Tribbles pseudokinase 3 promotes enterovirus a71 infection via dual mechanisms. Emerging Microbes &amp; Infections, Jan 2024. URL: https://doi.org/10.1080/22221751.2024.2307514, doi:10.1080/22221751.2024.2307514. This article has 9 citations and is from a domain leading peer-reviewed journal.

10. (zhu2023currentstatusof media ba7d7b3e): P. Zhu, W. Ji, Dong Li, Zijie Li, Yu Chen, B. Dai, Shujie Han, Shuaiyin Chen, Yuefei Jin, and G. Duan. Current status of hand-foot-and-mouth disease. Journal of Biomedical Science, Feb 2023. URL: https://doi.org/10.1186/s12929-023-00908-4, doi:10.1186/s12929-023-00908-4. This article has 243 citations and is from a domain leading peer-reviewed journal.

11. (zhu2023currentstatusof media 86593dfb): P. Zhu, W. Ji, Dong Li, Zijie Li, Yu Chen, B. Dai, Shujie Han, Shuaiyin Chen, Yuefei Jin, and G. Duan. Current status of hand-foot-and-mouth disease. Journal of Biomedical Science, Feb 2023. URL: https://doi.org/10.1186/s12929-023-00908-4, doi:10.1186/s12929-023-00908-4. This article has 243 citations and is from a domain leading peer-reviewed journal.

12. (wei2024recentprogressin pages 2-4): Jialong Wei, Linxi Lv, Tian Wang, Wei Gu, Yang Luo, and Hui Feng. Recent progress in innate immune responses to enterovirus a71 and viral evasion strategies. International Journal of Molecular Sciences, 25:5688, May 2024. URL: https://doi.org/10.3390/ijms25115688, doi:10.3390/ijms25115688. This article has 12 citations.

13. (hu2024ip10actsearly pages 1-2): Yajie Hu, Yunguang Hu, Anguo Yin, Yaming Lv, Jiang Li, Jingyuan Fan, Baojiang Qian, Jie Song, and Yunhui Zhang. Ip-10 acts early in cv-a16 infection to induce bbb destruction and promote virus entry into the cns by increasing tnf-α expression. Frontiers in Immunology, Nov 2024. URL: https://doi.org/10.3389/fimmu.2024.1374447, doi:10.3389/fimmu.2024.1374447. This article has 4 citations and is from a peer-reviewed journal.

14. (shi2023proteomicandmetabonomic pages 1-2): Huichun Shi, Siyuan Liu, Zhimi Tan, Lin Yin, Liyan Zeng, Tiefu Liu, Shuye Zhang, and Lijun Zhang. Proteomic and metabonomic analysis uncovering enterovirus a71 reprogramming host cell metabolic pathway. Nov 2023. URL: https://doi.org/10.1002/pmic.202200362, doi:10.1002/pmic.202200362. This article has 8 citations and is from a peer-reviewed journal.

15. (shi2023proteomicandmetabonomic pages 12-13): Huichun Shi, Siyuan Liu, Zhimi Tan, Lin Yin, Liyan Zeng, Tiefu Liu, Shuye Zhang, and Lijun Zhang. Proteomic and metabonomic analysis uncovering enterovirus a71 reprogramming host cell metabolic pathway. Nov 2023. URL: https://doi.org/10.1002/pmic.202200362, doi:10.1002/pmic.202200362. This article has 8 citations and is from a peer-reviewed journal.

16. (nishimura2024enterovirusa71does pages 10-13): Yorihiro Nishimura, Kei Sato, Yoshio Koyanagi, Takaji Wakita, Masamichi Muramatsu, Hiroyuki Shimizu, Jeffrey M. Bergelson, and Minetaro Arita. Enterovirus a71 does not meet the uncoating receptor scarb2 at the cell surface. PLOS Pathogens, 20:e1012022, Feb 2024. URL: https://doi.org/10.1371/journal.ppat.1012022, doi:10.1371/journal.ppat.1012022. This article has 8 citations and is from a highest quality peer-reviewed journal.

17. (dai2024epidemiologyandetiology pages 4-6): Bowen Dai, Yu Chen, Shujie Han, Shouhang Chen, Fang Wang, Huifen Feng, Xiaolong Zhang, Wenlong Li, Shuaiyin Chen, Haiyan Yang, Guangcai Duan, Guowei Li, and Yuefei Jin. Epidemiology and etiology of hand, foot, and mouth disease in zhengzhou, china, from 2009 to 2021. Infectious Medicine, 3:100114, Jun 2024. URL: https://doi.org/10.1016/j.imj.2024.100114, doi:10.1016/j.imj.2024.100114. This article has 8 citations.

18. (duan2023theeffectsof pages 1-2): Feng Yuan Duan, Zeng-Qing Du, Yang Wang, Lan Luo, Li-Jiang Du, Hong Jiang, Yantuanjin Ma, and Yu-Ling Yang. The effects of scarb2 and selplg gene polymorphisms on ev71 infection in hand, foot, and mouth disease. Biomolecules and Biomedicine, 23:815-824, Apr 2023. URL: https://doi.org/10.17305/bb.2023.8948, doi:10.17305/bb.2023.8948. This article has 3 citations.

19. (wang2024correlationsofpsgl1 pages 2-4): Xia Wang, Jing Qian, Yuqiang Mi, Ying Li, Yu Cao, and Kunyan Qiao. Correlations of psgl-1 vntr polymorphism with the susceptibility to severe hfmd associated with ev-71 and the immune status after infection. Virology Journal, Aug 2024. URL: https://doi.org/10.1186/s12985-024-02461-4, doi:10.1186/s12985-024-02461-4. This article has 2 citations and is from a peer-reviewed journal.

20. (chen2024molecularevolutionarydynamics pages 1-2): Yu Chen, Shouhang Chen, Yuanfang Shen, Zhi Li, Xiaolong Li, Yaodong Zhang, Xiaolong Zhang, Fang Wang, and Yuefei Jin. Molecular evolutionary dynamics of coxsackievirus a6 causing hand, foot, and mouth disease from 2021 to 2023 in china: genomic epidemiology study. JMIR Public Health and Surveillance, 10:e59604-e59604, Jul 2024. URL: https://doi.org/10.2196/59604, doi:10.2196/59604. This article has 18 citations and is from a peer-reviewed journal.

21. (duan2023theeffectsof pages 2-3): Feng Yuan Duan, Zeng-Qing Du, Yang Wang, Lan Luo, Li-Jiang Du, Hong Jiang, Yantuanjin Ma, and Yu-Ling Yang. The effects of scarb2 and selplg gene polymorphisms on ev71 infection in hand, foot, and mouth disease. Biomolecules and Biomedicine, 23:815-824, Apr 2023. URL: https://doi.org/10.17305/bb.2023.8948, doi:10.17305/bb.2023.8948. This article has 3 citations.

22. (nishimura2024enterovirusa71does pages 6-9): Yorihiro Nishimura, Kei Sato, Yoshio Koyanagi, Takaji Wakita, Masamichi Muramatsu, Hiroyuki Shimizu, Jeffrey M. Bergelson, and Minetaro Arita. Enterovirus a71 does not meet the uncoating receptor scarb2 at the cell surface. PLOS Pathogens, 20:e1012022, Feb 2024. URL: https://doi.org/10.1371/journal.ppat.1012022, doi:10.1371/journal.ppat.1012022. This article has 8 citations and is from a highest quality peer-reviewed journal.

23. (duan2023theeffectsof pages 6-7): Feng Yuan Duan, Zeng-Qing Du, Yang Wang, Lan Luo, Li-Jiang Du, Hong Jiang, Yantuanjin Ma, and Yu-Ling Yang. The effects of scarb2 and selplg gene polymorphisms on ev71 infection in hand, foot, and mouth disease. Biomolecules and Biomedicine, 23:815-824, Apr 2023. URL: https://doi.org/10.17305/bb.2023.8948, doi:10.17305/bb.2023.8948. This article has 3 citations.

24. (wang2024correlationsofpsgl1 pages 1-2): Xia Wang, Jing Qian, Yuqiang Mi, Ying Li, Yu Cao, and Kunyan Qiao. Correlations of psgl-1 vntr polymorphism with the susceptibility to severe hfmd associated with ev-71 and the immune status after infection. Virology Journal, Aug 2024. URL: https://doi.org/10.1186/s12985-024-02461-4, doi:10.1186/s12985-024-02461-4. This article has 2 citations and is from a peer-reviewed journal.

25. (nishimura2024enterovirusa71does pages 13-15): Yorihiro Nishimura, Kei Sato, Yoshio Koyanagi, Takaji Wakita, Masamichi Muramatsu, Hiroyuki Shimizu, Jeffrey M. Bergelson, and Minetaro Arita. Enterovirus a71 does not meet the uncoating receptor scarb2 at the cell surface. PLOS Pathogens, 20:e1012022, Feb 2024. URL: https://doi.org/10.1371/journal.ppat.1012022, doi:10.1371/journal.ppat.1012022. This article has 8 citations and is from a highest quality peer-reviewed journal.