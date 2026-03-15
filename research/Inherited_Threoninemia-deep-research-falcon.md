---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-03-11T14:39:23.594812'
end_time: '2026-03-11T14:53:49.170671'
duration_seconds: 865.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inherited Threoninemia
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
- **Disease Name:** Inherited Threoninemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Inherited Threoninemia**.
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
- **Disease Name:** Inherited Threoninemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Inherited Threoninemia**.
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


# Comprehensive Research Report: Inherited Threoninemia (Hyperthreoninemia/Threoninemia)

## Executive summary
“Inherited threoninemia” (historically also called **threoninemia** or **hyperthreoninemia**) is a rare and poorly genetically defined inborn error described primarily in older literature. The best-documented mechanistic hypothesis is **deficiency of hepatic threonine dehydratase (EC 4.2.1.16)** leading to **marked threonine accumulation** and (in at least one reported patient) **secondary hyperglycinemia** via competition at **serine hydroxymethyltransferase** (serine transhydroxymethylase) at the glycine/serine/threonine intersection. (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3, krieger1984threoninedehydratasedeficiency media c40ef479)

**Critical limitation:** In the retrieved literature set, **no modern (2023–2024) authoritative review, case series, guideline, MONDO mapping, or gene-level causal assignment** for “inherited threoninemia” was found despite targeted searches and citation-chaining; therefore, the report below focuses on the best-supported molecular mechanism from available primary sources (1984–1997) and clearly labels gaps. (darling1997threonineandphenylalanine pages 47-50)

## Disease identity and ontology crosswalk
- **Preferred label (working):** Inherited threoninemia / hyperthreoninemia (historical entity)
- **MONDO ID:** Not retrievable/confirmable from available sources in this corpus.
- **Genetic basis:** **Not established** in the retrieved corpus; historical work implicates an **enzyme activity defect (threonine dehydratase)** but does not identify a gene. (krieger1984threoninedehydratasedeficiency pages 1-2, darling1997threonineandphenylalanine pages 47-50)

## 1) Core pathophysiology

### 1.1 Primary pathophysiological mechanisms
**Mechanism (best-supported historical model):**
1. **Primary block in threonine degradation** at **threonine dehydratase (TD; EC 4.2.1.16)** in liver causes **systemic threonine accumulation** (plasma and CSF markedly elevated). (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3)
2. **Excess threonine perturbs one-carbon amino acid interconversion**: Krieger & Booth proposed that elevated threonine competes within the **glycine–serine–threonine network** at **serine hydroxymethyltransferase (serine transhydroxymethylase; STHM)**, reducing normal glycine-to-serine flux and contributing to **hyperglycinemia** (reported in a patient with non-ketotic hyperglycinemia phenotype). (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3, krieger1984threoninedehydratasedeficiency media c40ef479)

**Direct quote (mechanistic rationale):** Krieger & Booth state, “**Since the affinity of STHM is greatest for serine and lowest for threonine, competition between glycine and threonine can be anticipated**.” (krieger1984threoninedehydratasedeficiency pages 2-3)

### 1.2 Dysregulated molecular pathways
Key dysregulated pathway elements described in the retrieved sources include:
- **Cytosolic threonine dehydratase route:** L-threonine → **2-ketobutyrate** (α-ketobutyrate) → downstream **propionyl-CoA** metabolism. (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 207-211)
- **Mitochondrial threonine dehydrogenase route:** L-threonine → **2-amino-3-oxobutyrate** → cleavage to **glycine + acetyl-CoA** (via 2-amino-3-ketobutyrate CoA ligase). (darling1997threonineandphenylalanine pages 43-47)
- **Interconversion hub:** glycine ↔ serine ↔ threonine via **serine hydroxymethyltransferase/transhydroxymethylase**-linked reactions (conceptualized in Figure 1 of Krieger & Booth). (krieger1984threoninedehydratasedeficiency media c40ef479, krieger1984threoninedehydratasedeficiency pages 1-2)

### 1.3 Cellular processes affected
Based on the proposed mechanism and measured metabolite derangements, likely affected cellular processes include:
- **Amino acid catabolism and mitochondrial acetyl-CoA generation** (threonine dehydrogenase pathway). (darling1997threonineandphenylalanine pages 43-47)
- **Cytosolic amino acid dehydration/transamination flux** through α-ketobutyrate and α-aminobutyrate. (darling1997threonineandphenylalanine pages 207-211)
- **One-carbon amino acid interconversion** at the glycine/serine/threonine node, with potential downstream effects on CNS glycinergic neurotransmission in hyperglycinemic states. (krieger1984threoninedehydratasedeficiency pages 1-2, darling1997threonineandphenylalanine pages 50-54)

## 2) Key molecular players

### 2.1 Genes/Proteins (causal or implicated)
**Causal gene:** Not identified in the retrieved sources.

**Implicated enzymes/proteins (functionally):**
- **Threonine dehydratase (TD; EC 4.2.1.16)** — proposed deficient enzyme in the best-supported primary case. (krieger1984threoninedehydratasedeficiency pages 1-2)
- **Threonine dehydrogenase (EC 1.1.1.103)** — alternative candidate defect proposed by Krieger & Booth; also a major threonine oxidation route in animal liver. (krieger1984threoninedehydratasedeficiency pages 1-2, darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 47-50)
- **Serine hydroxymethyltransferase / serine transhydroxymethylase (STHM; EC 2.1.2.1)** — proposed competitive bottleneck linking threonine excess to glycine accumulation. (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3, krieger1984threoninedehydratasedeficiency media c40ef479)

### 2.2 Chemical entities (metabolites/small molecules)
**Primary metabolites (candidate diagnostic / mechanistic):**
- **L-threonine** (elevated in plasma/CSF/urine). (krieger1984threoninedehydratasedeficiency pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4)
- **Glycine** (elevated in the TD-deficiency/NKH hypothesis; also increased in urine in one hyperthreoninemia case series). (krieger1984threoninedehydratasedeficiency pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4)
- **Serine** (part of the interconversion node; increased urinary serine reported in the LCA-associated hyperthreoninemia case series). (hayasaka1986leberscongenitalamaurosis pages 2-4)
- **2-ketobutyrate (α-ketobutyrate)**, **propionyl-CoA**, **acetyl-CoA**, **2-amino-3-oxobutyrate** (pathway intermediates). (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 207-211)

**Therapeutics/management used (historical, in NKH context):**
- **Sodium benzoate**, anticonvulsants (e.g., clonazepam/valium), plus supportive measures were attempted in the TD-deficiency/NKH patient; withdrawal worsened seizures. (krieger1984threoninedehydratasedeficiency pages 2-3)

### 2.3 Cell types primarily affected
No cell-type–resolved pathology is provided in the retrieved sources. Based on enzyme localization and reported organ involvement, the most plausible primary affected cell types are:
- **Hepatocytes** (primary site of threonine dehydratase activity; enzyme measured in liver tissue). (krieger1984threoninedehydratasedeficiency pages 2-3, darling1997threonineandphenylalanine pages 43-47)
- Potential secondary impact on **neurons/glia** in settings with CNS glycine perturbation (inferred from NKH-like presentation and CSF findings). (krieger1984threoninedehydratasedeficiency pages 2-3, krieger1984threoninedehydratasedeficiency pages 1-2)

### 2.4 Anatomical locations / organs involved
- **Liver**: implicated by absent hepatic TD activity; hepatomegaly/mild liver dysfunction reported in one hyperthreoninemia-associated phenotype series. (krieger1984threoninedehydratasedeficiency pages 2-3, hayasaka1986leberscongenitalamaurosis pages 2-4)
- **Central nervous system**: elevated CSF threonine and hyperglycinemia with seizures/encephalopathy in the TD-deficiency/NKH hypothesis. (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3)
- **Eye/retina**: Leber congenital amaurosis phenotype reported in siblings with hyperthreoninemia (association; causality uncertain). (hayasaka1986leberscongenitalamaurosis pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4)

## 3) Biological processes disrupted (GO-oriented)
*Note: GO identifiers are not supplied by the sources; items below are process concepts supported by the mechanistic evidence.*

- **Threonine catabolic process** (cytosolic dehydration to α-ketobutyrate; mitochondrial oxidation to glycine/acetyl-CoA). (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 207-211)
- **Glycine metabolic process / serine metabolic process** via serine hydroxymethyltransferase node interactions. (krieger1984threoninedehydratasedeficiency media c40ef479, krieger1984threoninedehydratasedeficiency pages 2-3)
- **Mitochondrial acetyl-CoA biosynthetic process** (via threonine dehydrogenase pathway). (darling1997threonineandphenylalanine pages 43-47)
- **Propionyl-CoA metabolic process** downstream of α-ketobutyrate (threonine dehydratase route). (darling1997threonineandphenylalanine pages 207-211)

## 4) Cellular components (GO-oriented)
- **Cytosol**: threonine dehydratase pathway described as cytosolic. (darling1997threonineandphenylalanine pages 43-47)
- **Mitochondrion**: threonine dehydrogenase pathway described as mitochondrial, producing acetyl-CoA and glycine. (darling1997threonineandphenylalanine pages 43-47)

## 5) Disease progression (sequence from trigger to phenotype)

### Proposed sequence (TD deficiency model)
1. **Inherited enzymatic defect** with very low/absent **hepatic TD activity**. (krieger1984threoninedehydratasedeficiency pages 2-3)
2. **Biochemical accumulation of threonine** systemically and in CSF (reported as ~16× in CSF and ~19× in plasma above normal). (krieger1984threoninedehydratasedeficiency pages 1-2)
3. **Perturbation of glycine–serine–threonine interconversion** via competitive effects at STHM, contributing to **hyperglycinemia** and an NKH-like neurotoxic phenotype. (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency media c40ef479)
4. **Clinical manifestations**: neonatal/infantile seizures, lethargy, failure to feed/suck, respiratory arrest reported in the index patient. (krieger1984threoninedehydratasedeficiency pages 2-3)

### Alternative/uncertain trajectories
- In a separate phenotype series (LCA association), hyperthreoninemia may have been **primary** or **secondary to liver dysfunction**; the authors explicitly state uncertainty about causality. (hayasaka1986leberscongenitalamaurosis pages 4-5)

## 6) Phenotypic manifestations and mechanism links

### 6.1 Neurologic phenotype (NKH-like)
- **Seizures, lethargy, feeding difficulty, respiratory arrest** were reported in the patient in whom TD activity was undetectable. These findings align with glycine neurotoxicity in NKH and are mechanistically linked to the hypothesized STHM competition model. (krieger1984threoninedehydratasedeficiency pages 2-3, krieger1984threoninedehydratasedeficiency media c40ef479)

### 6.2 Ocular phenotype (association reported)
- **Leber congenital amaurosis** features (blindness from birth, absent pupillary light reflex, nearly extinguished ERG) were reported in siblings with hyperthreoninemia and hyperthreoninuria. Mechanistic linkage to threonine metabolism is not established in the paper; it is presented as an association requiring further study. (hayasaka1986leberscongenitalamaurosis pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4, hayasaka1986leberscongenitalamaurosis pages 4-5)

### 6.3 Hepatic/systemic phenotype
- **Hepatomegaly and mild liver dysfunction** co-occurred in the LCA-associated hyperthreoninemia cases, raising the possibility of secondary hyperthreoninemia (not resolved). (hayasaka1986leberscongenitalamaurosis pages 2-4, hayasaka1986leberscongenitalamaurosis pages 4-5)

## Evidence summary table
| Disease label used | Proposed causal defect (enzyme) | Pathway node (reaction) | Key metabolites altered (direction) | Quantitative values reported | Phenotypes | Specimen/tissue | Year | DOI/URL |
|---|---|---|---|---|---|---|---|---|
| Non-ketotic hyperglycinaemia (probable threonine dehydratase deficiency) | Hepatic threonine dehydratase (EC 4.2.1.16) deficiency; undetectable TD activity | L-threonine → 2-ketobutyrate (threonine dehydratase); proposed competition at serine hydroxymethyltransferase linking glycine/serine/threonine flux (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3, krieger1984threoninedehydratasedeficiency media c40ef479) | Threonine ↑ (plasma, CSF); Glycine ↑ | Threonine: ~16× (CSF) and ~19× (plasma) above normal; liver TD undetectable by assay (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3) | NKH features: seizures, failure to suck, lethargy, respiratory arrest (krieger1984threoninedehydratasedeficiency pages 2-3) | Liver autopsy (enzyme assay); plasma/CSF amino acids (krieger1984threoninedehydratasedeficiency pages 1-2) | 1984 | https://doi.org/10.1007/bf01805800 |
| Leber's congenital amaurosis with hyperthreoninemia | Not identified | Unknown (metabolic association reported, no enzyme defect established) (hayasaka1986leberscongenitalamaurosis pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4) | Threonine ↑ (plasma, urine); Serine ↑ (urine); Glycine ↑ (urine) | Plasma threonine 5.8–7.5 mg/dL (normal 0.78–1.82); urinary threonine 3.12 μmol/mg creatinine (elevated) (hayasaka1986leberscongenitalamaurosis pages 2-4, hayasaka1986leberscongenitalamaurosis pages 1-2) | Congenital blindness/near-blindness, absent pupillary light reflex, near-absent ERG; hepatomegaly, mild liver dysfunction; developmental delay; pericardial effusion (one case) (hayasaka1986leberscongenitalamaurosis pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4) | Serum and urine amino acids (hayasaka1986leberscongenitalamaurosis pages 2-4) | 1986 | https://doi.org/10.1016/0002-9394(86)90650-1 |
| Hyperthreoninemia (review of neonatal threonine metabolism) | Background: partitioning of threonine catabolism across threonine dehydrogenase (TDG), threonine dehydratase (TDH/TD), and threonine aldolase (TA); human defects not established (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 47-50, darling1997threonineandphenylalanine pages 207-211) | TDG: L-threonine → 2-amino-3-oxobutyrate → glycine + acetyl-CoA; TD (cytosolic): L-threonine → 2-ketobutyrate; TA: L-threonine → glycine + acetaldehyde (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 47-50) | 2-ketobutyrate, 2-amino-3-oxobutyrate, glycine, acetyl-CoA, propionyl-CoA (pathway nodes/metabolites) (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 207-211) | Rat liver: ~87% of threonine oxidation via TDG; reported Km: TDG ~10.6 mM, TD ~87 mM; hepatic [Thr] ~0.26 mM (species data) (darling1997threonineandphenylalanine pages 47-50) | Not applicable (mechanistic review; notes rarity of inherited hyperthreoninemia) (darling1997threonineandphenylalanine pages 47-50) | Narrative review (pathway/tissue distribution synthesis) (darling1997threonineandphenylalanine pages 43-47) | 1997 | — |


*Table: Structured summary of key evidence on inherited threoninemia/hyperthreoninemia from primary reports and a metabolic review, including enzymes implicated, pathway context, metabolites, quantitative findings, phenotypes, and source details. Citations reference the specific tool-extracted contexts supporting each row.*

## Key mechanistic figure (pathway schematic)
Krieger & Booth’s Figure 1 provides a pathway-level schematic of glycine/serine/threonine metabolism and the proposed competitive mechanism (TD or threonine dehydrogenase block leading to threonine accumulation and altered STHM flux). (krieger1984threoninedehydratasedeficiency media c40ef479)

## Current applications and real-world implementations
Because **contemporary (2023–2024) inherited-threoninemia–specific guidance was not retrieved**, the following “applications” reflect historical and broadly applicable clinical chemistry practices implied by the sources:

### Diagnostics
- **Plasma/CSF amino acid profiling**: In the TD-deficiency/NKH hypothesis, the key diagnostic signature included markedly elevated **plasma and CSF threonine** alongside elevated glycine. (krieger1984threoninedehydratasedeficiency pages 1-2)
- **Urine amino acid quantification**: In the LCA-associated cases, **urinary threonine** was elevated (example: 3.12 μmol/mg creatinine; normal trace–0.59) and accompanied by elevated urinary glycine and serine. (hayasaka1986leberscongenitalamaurosis pages 2-4)

### Management (historical, limited)
- In the TD-deficiency/NKH case, management included interventions typical for NKH (e.g., **sodium benzoate**) and anticonvulsants; stopping therapy worsened seizures, suggesting symptomatic benefit in seizure control. (krieger1984threoninedehydratasedeficiency pages 2-3)

## Expert opinion and interpretation (within evidence constraints)
- **Krieger & Booth (1984)** explicitly frame their observation as “**the first documentation of an inborn error of threonine metabolism**,” but they also emphasize the need for confirmation using fresh liver biopsies due to TD assay sensitivity to tissue handling and storage. (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3)
- **Darling (1997)** highlights that, as of that time, **human threonine catabolic enzyme partitioning and inherited defects were poorly defined**, and the literature consisted of only a few case reports—consistent with the persisting difficulty of forming a modern gene-based definition using the retrieved corpus alone. (darling1997threonineandphenylalanine pages 47-50)

## Relevant statistics and quantitative data (from studies retrieved)
- **Threonine elevation (TD-deficiency/NKH hypothesis):** “**16 and 19 fold elevation of threonine in CSF and plasma, respectively**.” (krieger1984threoninedehydratasedeficiency pages 1-2)
- **Enzyme activity (liver threonine dehydratase):** Control liver TD activities were reported in the tens to low hundreds of pmol·h−1·g−1 tissue range, whereas the patient’s TD activity was **undetectable**, with notable assay sensitivity to specimen storage/time at room temperature. (krieger1984threoninedehydratasedeficiency pages 2-3)
- **Hyperthreoninemia ranges (LCA-associated):** plasma threonine **5.8–7.5 mg/dL** (reported normal 0.78–1.82 mg/dL); urinary threonine **3.12 μmol/mg creatinine** (normal trace–0.59). (hayasaka1986leberscongenitalamaurosis pages 2-4)

## Knowledge-base–ready structured annotations

### Disease → molecular mechanism (narrative)
Inherited threoninemia is best supported historically as an **inborn error of threonine catabolism**, proposed to be caused by **hepatic threonine dehydratase deficiency**, leading to **systemic and CSF threonine accumulation** and secondary dysregulation at the **glycine–serine–threonine interconversion node** (serine hydroxymethyltransferase), potentially producing **hyperglycinemia** and an NKH-like neurologic phenotype. (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency media c40ef479, krieger1984threoninedehydratasedeficiency pages 2-3)

### Gene/protein annotations (HGNC)
- **HGNC gene(s):** Not assignable from retrieved sources (enzyme defect described without gene). (krieger1984threoninedehydratasedeficiency pages 1-2)

### Enzyme/protein (functional) entities
- Threonine dehydratase (EC 4.2.1.16) (krieger1984threoninedehydratasedeficiency pages 1-2)
- Serine hydroxymethyltransferase/transhydroxymethylase (EC 2.1.2.1) (krieger1984threoninedehydratasedeficiency pages 2-3)
- Threonine dehydrogenase (EC 1.1.1.103) (darling1997threonineandphenylalanine pages 43-47)

### Phenotype associations (HP-like concepts; IDs not provided in sources)
- Seizures/epileptic seizures; neonatal encephalopathy-like presentation; feeding difficulty (failure to suck); lethargy; respiratory arrest (krieger1984threoninedehydratasedeficiency pages 2-3)
- Congenital blindness / retinal dystrophy consistent with Leber congenital amaurosis; extinguished ERG; abnormal pupillary light reflex (hayasaka1986leberscongenitalamaurosis pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4)
- Hepatomegaly; elevated transaminases / mild liver dysfunction (hayasaka1986leberscongenitalamaurosis pages 2-4)

### Cell type involvement (CL-like concepts)
- Hepatocyte involvement implied by hepatic enzyme deficiency measurement (krieger1984threoninedehydratasedeficiency pages 2-3)

### Anatomical locations (UBERON-like concepts)
- Liver; central nervous system/CSF compartment; retina/eye (krieger1984threoninedehydratasedeficiency pages 2-3, hayasaka1986leberscongenitalamaurosis pages 2-4)

### Chemical entities (CHEBI-like concepts; IDs not provided in sources)
- L-threonine; glycine; serine; 2-ketobutyrate (α-ketobutyrate); propionyl-CoA; acetyl-CoA (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 207-211)

## Primary sources (URLs and publication dates)
1. **Krieger I, Booth F.** *Threonine dehydratase deficiency: A probable cause of non-ketotic hyperglycinaemia.* **Journal of Inherited Metabolic Disease**. **June 1984**. DOI/URL: https://doi.org/10.1007/bf01805800 (krieger1984threoninedehydratasedeficiency pages 1-2, krieger1984threoninedehydratasedeficiency pages 2-3)
2. **Hayasaka S, et al.** *Leber's congenital amaurosis associated with hyperthreoninemia.* **American Journal of Ophthalmology**. **April 1986**. DOI/URL: https://doi.org/10.1016/0002-9394(86)90650-1 (hayasaka1986leberscongenitalamaurosis pages 1-2, hayasaka1986leberscongenitalamaurosis pages 2-4)
3. **Darling PB.** *Threonine and phenylalanine metabolism in the human neonate.* **1997** (journal metadata not available in retrieved text). (darling1997threonineandphenylalanine pages 43-47, darling1997threonineandphenylalanine pages 47-50)

## Gaps and recommended next steps (evidence-based)
- The retrieved evidence base does not include modern genomic characterization; thus, a **gene-first** reinterpretation (e.g., exome/genome sequencing of historical cases or identification of contemporary patients with isolated hyperthreoninemia) is essential to assign HGNC genes and MONDO/OMIM IDs.
- Modern metabolomics/newborn screening literature may contain relevant differential diagnoses (secondary hyperthreoninemia due to liver disease, nutrition, or other IEMs), but such sources were not retrievable within this run.



References

1. (krieger1984threoninedehydratasedeficiency pages 1-2): I. Krieger and F. Booth. Threonine dehydratase deficiency: a probable cause of non-ketotic hyperglycinaemia. Journal of Inherited Metabolic Disease, 7:53-56, Jun 1984. URL: https://doi.org/10.1007/bf01805800, doi:10.1007/bf01805800. This article has 10 citations and is from a peer-reviewed journal.

2. (krieger1984threoninedehydratasedeficiency pages 2-3): I. Krieger and F. Booth. Threonine dehydratase deficiency: a probable cause of non-ketotic hyperglycinaemia. Journal of Inherited Metabolic Disease, 7:53-56, Jun 1984. URL: https://doi.org/10.1007/bf01805800, doi:10.1007/bf01805800. This article has 10 citations and is from a peer-reviewed journal.

3. (krieger1984threoninedehydratasedeficiency media c40ef479): I. Krieger and F. Booth. Threonine dehydratase deficiency: a probable cause of non-ketotic hyperglycinaemia. Journal of Inherited Metabolic Disease, 7:53-56, Jun 1984. URL: https://doi.org/10.1007/bf01805800, doi:10.1007/bf01805800. This article has 10 citations and is from a peer-reviewed journal.

4. (darling1997threonineandphenylalanine pages 47-50): PB Darling. Threonine and phenylalanine metabolism in the human neonate. Unknown journal, 1997.

5. (darling1997threonineandphenylalanine pages 43-47): PB Darling. Threonine and phenylalanine metabolism in the human neonate. Unknown journal, 1997.

6. (darling1997threonineandphenylalanine pages 207-211): PB Darling. Threonine and phenylalanine metabolism in the human neonate. Unknown journal, 1997.

7. (darling1997threonineandphenylalanine pages 50-54): PB Darling. Threonine and phenylalanine metabolism in the human neonate. Unknown journal, 1997.

8. (hayasaka1986leberscongenitalamaurosis pages 2-4): Seiji Hayasaka, Satoshi Hara, Katsuyoshi Mizuno, Kuniaki Narisawa, and Keiya Tada. Leber's congenital amaurosis associated with hyperthreoninemia. American journal of ophthalmology, 101 4:475-9, Apr 1986. URL: https://doi.org/10.1016/0002-9394(86)90650-1, doi:10.1016/0002-9394(86)90650-1. This article has 14 citations and is from a domain leading peer-reviewed journal.

9. (hayasaka1986leberscongenitalamaurosis pages 1-2): Seiji Hayasaka, Satoshi Hara, Katsuyoshi Mizuno, Kuniaki Narisawa, and Keiya Tada. Leber's congenital amaurosis associated with hyperthreoninemia. American journal of ophthalmology, 101 4:475-9, Apr 1986. URL: https://doi.org/10.1016/0002-9394(86)90650-1, doi:10.1016/0002-9394(86)90650-1. This article has 14 citations and is from a domain leading peer-reviewed journal.

10. (hayasaka1986leberscongenitalamaurosis pages 4-5): Seiji Hayasaka, Satoshi Hara, Katsuyoshi Mizuno, Kuniaki Narisawa, and Keiya Tada. Leber's congenital amaurosis associated with hyperthreoninemia. American journal of ophthalmology, 101 4:475-9, Apr 1986. URL: https://doi.org/10.1016/0002-9394(86)90650-1, doi:10.1016/0002-9394(86)90650-1. This article has 14 citations and is from a domain leading peer-reviewed journal.