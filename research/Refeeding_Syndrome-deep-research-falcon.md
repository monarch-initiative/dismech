---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-01T14:13:32.996192'
end_time: '2026-02-01T14:18:54.776654'
duration_seconds: 321.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Refeeding Syndrome
  mondo_id: ''
  category: Nutritional
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
- **Disease Name:** Refeeding Syndrome
- **MONDO ID:**  (if available)
- **Category:** Nutritional

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Refeeding Syndrome**.
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
- **Disease Name:** Refeeding Syndrome
- **MONDO ID:**  (if available)
- **Category:** Nutritional

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Refeeding Syndrome**.
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
- Disease Name: Refeeding Syndrome (RFS)
- MONDO ID: Not definitively established in MONDO as a distinct entity; treated as a clinical syndrome spanning malnutrition and iatrogenic complications in guidelines (will use guideline definitions). (silva2020aspenconsensusrecommendations pages 2-3, mazur2024advancesinunderstanding pages 5-8)
- Category: Nutritional

Pathophysiology description
Core pathophysiology and current understanding
Refeeding syndrome is a spectrum of metabolic and clinical disturbances that occur within approximately 1–5 days after reintroduction or escalation of nutrition (especially carbohydrate) in malnourished individuals. The central mechanism is a carbohydrate-triggered insulin surge that switches metabolism from catabolism (lipolysis/ketosis) to anabolism (glycolysis, glycogenesis, protein synthesis), with rapid intracellular uptake of phosphate, potassium, and magnesium and increased vitamin (thiamine) demand. ASPEN summarizes: “When glucose appears in the bloodstream, insulin secretion rises… rising insulin levels drive phosphorus and potassium intracellularly both by demand (phosphorylation of glucose as glycolysis is initiated) and through the direct effects of insulin (stimulation of the sodium-potassium adenosine triphosphatase [ATPase]).” This intracellular shift produces hypophosphatemia, hypokalemia, and hypomagnesemia, precipitating organ dysfunction, arrhythmias, respiratory failure, and sudden death in severe cases (URL: https://doi.org/10.1002/ncp.10474; published Mar 2020). (silva2020aspenconsensusrecommendations pages 2-3)

Recent reviews corroborate that refeeding abruptly activates glycolysis and other insulin-responsive pathways, with “sudden activation of intracellular enzymes,” increased cofactor demand, and sharp extracellular drops in electrolytes. Thiamine deficiency may become manifest as carbohydrate flux increases, contributing to lactic acidosis and Wernicke encephalopathy. Fluid and sodium retention with hyperinsulinemia compound risks of heart failure and pulmonary edema. Timing is typically within the first 2–5 days. URL: https://doi.org/10.3390/nu17111866; published May 2025. (borriello2025understandingrefeedingsyndrome pages 4-5)

Molecular pathways and cellular processes
- Insulin → PI3K–AKT–mTOR axis: Carbohydrate intake stimulates insulin, activating canonical insulin signaling to promote glucose uptake and anabolic metabolism, driving phosphate-requiring biosynthesis (ATP, 2,3‑DPG, glycogen), thereby depleting extracellular phosphate. Although guidelines emphasize insulin’s effects and glycolysis rather than naming PI3K–AKT–mTOR explicitly, the metabolic shift and insulin-stimulated Na+/K+-ATPase are consistently described. URL: https://doi.org/10.1002/ncp.10474; Mar 2020. (silva2020aspenconsensusrecommendations pages 2-3)
- Na+/K+-ATPase stimulation: Insulin directly stimulates the sodium-potassium ATPase, accelerating intracellular K+ influx and contributing to hypokalemia; Mg2+ is a cofactor for this ATPase. URL: https://doi.org/10.1002/ncp.10474; Mar 2020. (silva2020aspenconsensusrecommendations pages 2-3)
- Glycolysis and phosphoryl transfer: Increased phosphorylation steps (e.g., hexokinase) increase intracellular Pi utilization; depleted intracellular stores after starvation plus enhanced uptake drop serum phosphate. Reviews note reduced ATP and 2,3‑DPG with consequences for muscle and erythrocyte function. URL: https://doi.org/10.12775/qs.2024.19.53773; Aug 2024. (mazur2024advancesinunderstanding pages 3-5)
- Thiamine-dependent carbohydrate metabolism: PDH and α‑ketoglutarate dehydrogenase (TCA) and transketolase (PPP) require thiamine. With increased carbohydrate flux during refeeding, relative thiamine deficiency can shunt pyruvate to lactate (lactic acidosis) and produce Wernicke encephalopathy. URL (review): APGHN 2024 (no DOI provided in excerpt). (aini2024refeedingsyndromeina pages 9-10)
- Phosphate transport regulation: Cellular Pi influx is mediated by SLC20 family transporters (PiT1/SLC20A1, PiT2/SLC20A2), while XPR1 mediates efflux; recent data show endosomal recycling of PiT1 and InsP8–SPX domain regulation of XPR1 as part of an intracellular Pi homeostatic loop. These mechanisms contextualize the profound hypophosphatemia during refeeding. URL: https://doi.org/10.3389/fphar.2023.1163442; Mar 2023. (borriello2025understandingrefeedingsyndrome pages 2-4)
- Fluid/sodium retention: Hyperinsulinemia promotes renal sodium retention; reviews note additional mechanisms (e.g., capillary leak or altered natriuretic signaling) may contribute to early edema and heart failure in high-risk patients. URL: https://doi.org/10.3390/nu17111866; May 2025; and mechanistic overview in 2024 review. (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8)

Cellular and organ-level effects
- Cardiac: Hypokalemia and hypomagnesemia alter membrane potentials and QT intervals, increasing malignant arrhythmia risk; hypophosphatemia and low ATP impair contractility; fluid retention precipitates heart failure. URL: https://doi.org/10.1002/ncp.10474; Mar 2020; https://doi.org/10.3390/nu17111866; May 2025. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5)
- Respiratory: Hypophosphatemia causes respiratory muscle dysfunction and acute respiratory failure; diaphragmatic weakness reflects ATP depletion and impaired muscle energetics. URL: https://doi.org/10.1002/ncp.10474; Mar 2020; https://doi.org/10.25060/residpediatr-2024.v14n3-1101; Jan 2024. (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4)
- Neurologic: Thiamine deficiency during refeeding increases risk of Wernicke encephalopathy (ophthalmoplegia, ataxia, encephalopathy) and contributes to lactic acidosis with high carbohydrate loads. URL: APGHN 2024 excerpt; Jan 2024 pediatric review. (aini2024refeedingsyndromeina pages 9-10, machado2024refeedingsyndromein pages 2-4)
- Hematologic: Hypophosphatemia lowers erythrocyte 2,3‑DPG and ATP, impairing oxygen delivery and risking hemolysis. URL: https://doi.org/10.25060/residpediatr-2024.v14n3-1101; Jan 2024. (machado2024refeedingsyndromein pages 2-4)
- Hepatic: Rapid shift to carbohydrate metabolism and cofactor demands may contribute to refeeding-associated steatosis and transaminitis during early refeeding. URL: 2024–2025 narrative review context. (borriello2025understandingrefeedingsyndrome pages 4-5)

Sequence of events and disease progression
Typical sequence: (1) Starvation with depletion of intracellular phosphate, K+, Mg2+, and thiamine; (2) Nutrition reintroduction (often carbohydrate-rich) triggers insulin surge within hours; (3) 12–72 h: intracellular shifts cause serum hypophosphatemia (often first observable within 48–72 h), hypokalemia, hypomagnesemia; thiamine-dependent pathways become rate-limited, with possible lactic acidosis; (4) 1–5 days: clinical manifestations such as arrhythmias, heart failure, respiratory failure, edema, neurologic signs emerge; risk peaks early and mandates close monitoring. URLs: https://doi.org/10.1002/ncp.10474 (Mar 2020); https://doi.org/10.25060/residpediatr-2024.v14n3-1101 (Jan 2024). (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4)

Key Molecular Players
- Genes/Proteins (HGNC): INS; ATP1A1 (Na+/K+-ATPase α1); PDHA1 (PDH complex); OGDH (α‑ketoglutarate dehydrogenase); TKT (transketolase); SLC20A1 (PiT1), SLC20A2 (PiT2); XPR1 (phosphate efflux). Roles summarized above (insulin signaling, Na+/K+-ATPase activation, thiamine-dependent metabolism, phosphate transport). URLs: https://doi.org/10.1002/ncp.10474 (Mar 2020); https://doi.org/10.3389/fphar.2023.1163442 (Mar 2023). (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 2-4)
- Chemical Entities (CHEBI): glucose (trigger); insulin; inorganic phosphate (Pi); potassium (K+); magnesium (Mg2+); thiamine (vitamin B1). Mechanistic roles summarized above. URLs as above; 2024 and 2025 reviews. (silva2020aspenconsensusrecommendations pages 2-3, mazur2024advancesinunderstanding pages 3-5, borriello2025understandingrefeedingsyndrome pages 4-5)
- Cell Types (CL): cardiac myocyte; skeletal muscle (diaphragm); hepatocyte; neuron; erythrocyte. Organ-specific vulnerabilities described above. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5, machado2024refeedingsyndromein pages 2-4)
- Anatomical Locations (UBERON): heart; diaphragm; liver; brain; lung. Clinical manifestations localized as above. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5, machado2024refeedingsyndromein pages 2-4)

Biological Processes (GO terms)
- Response to insulin (GO:0032868) and insulin receptor signaling (GO:0008286): drive metabolic switch and ion shifts. Evidence: insulin surge on refeeding with electrolyte shifts. (silva2020aspenconsensusrecommendations pages 2-3)
- Glycolytic process (GO:0006096): increased flux consumes Pi for phosphoryl intermediates. (mazur2024advancesinunderstanding pages 3-5)
- Cellular potassium ion homeostasis (GO:0030007) and magnesium ion homeostasis (GO:0032026): disrupted by insulin-stimulated uptake and Mg2+ depletion. (silva2020aspenconsensusrecommendations pages 2-3, mazur2024advancesinunderstanding pages 3-5)
- Phosphate ion transport (GO:0006817) and regulation of intracellular phosphate (via SLC20 and XPR1): underpin hypophosphatemia. (borriello2025understandingrefeedingsyndrome pages 2-4)
- Cellular response to thiamine starvation (GO:0042356) / carbohydrate metabolic process (GO:0005975): thiamine dependency of PDH/OGDH/TKT and consequences of deficiency during high carbohydrate loads. (aini2024refeedingsyndromeina pages 9-10)
- Sodium ion transport (GO:0006814): Na+/K+-ATPase activation shifts K+ intracellularly. (silva2020aspenconsensusrecommendations pages 2-3)

Cellular Components
- Plasma membrane: Na+/K+-ATPase (ATP1A1) and SLC20 PiT1/PiT2; insulin receptor signaling localization. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 2-4)
- Cytosol/mitochondria: PDH complex and OGDH (mitochondrial matrix) for carbohydrate oxidation; cytosolic glycolytic enzymes and PPP/transketolase. (aini2024refeedingsyndromeina pages 9-10)
- Extracellular space/serum: measurable hypophosphatemia, hypokalemia, hypomagnesemia as diagnostic markers. (silva2020aspenconsensusrecommendations pages 2-3)

Disease Progression and Phases
- Pre-refeeding: catabolic state with intracellular depletion despite normal serum values. (mazur2024advancesinunderstanding pages 3-5)
- Early refeeding (0–72 h): insulin surge, glycolysis activation, electrolyte shifts; earliest biochemical changes. (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4)
- Clinical phase (1–5 days): organ dysfunction (cardiac, respiratory, neurologic), fluid overload/edema. (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8)

Phenotypic Manifestations (with HP terms)
- Hypophosphatemia (HP:0002141) and related hemolysis, muscle weakness, decreased 2,3‑DPG/ATP. URL: Jan 2024. (machado2024refeedingsyndromein pages 2-4)
- Hypokalemia (HP:0002900) and arrhythmias/QT changes. URL: Mar 2020; May 2025. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5)
- Hypomagnesemia (HP:0002142) exacerbating refractory hypokalemia and arrhythmias. URL: Aug 2024 review; May 2025 review. (mazur2024advancesinunderstanding pages 3-5, borriello2025understandingrefeedingsyndrome pages 4-5)
- Lactic acidosis (HP:0002151) under thiamine deficiency. URL: APGHN 2024 excerpt; Jan 2024. (aini2024refeedingsyndromeina pages 9-10, machado2024refeedingsyndromein pages 2-4)
- Heart failure (HP:0001715), pulmonary edema (HP:0002206), arrhythmia (HP:0011675). URL: Mar 2020; May 2025; Aug 2024. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8)
- Respiratory failure (HP:0002878) from diaphragmatic weakness. URL: Mar 2020; Jan 2024. (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4)
- Wernicke encephalopathy (HP:0001697). URL: APGHN 2024 excerpt. (aini2024refeedingsyndromeina pages 9-10)

Diagnostic definitions and risk criteria
- ASPEN 2020 consensus definition: “a decrease in any 1, 2, or 3 of serum phosphorus, potassium, and/or magnesium levels by 10%–20% (mild), 20%–30% (moderate), or >30% and/or organ dysfunction resulting from a decrease in any of these and/or due to thiamin deficiency (severe), occurring within 5 days of reintroduction of calories.” URL: https://doi.org/10.1002/ncp.10474; Mar 2020. (silva2020aspenconsensusrecommendations pages 2-3)
- NICE-type risk criteria: low BMI, recent significant weight loss, prolonged minimal intake, or low baseline electrolytes define risk strata in many implementations summarized in 2024 review; high-risk patients need cautious caloric initiation and close monitoring. URL: https://doi.org/10.12775/qs.2024.19.53773; Aug 2024. (mazur2024advancesinunderstanding pages 5-8)

Recent developments and latest research (2023–2024 priority) and real-world data
- Transporter-level Pi homeostasis (2023): Jennings details dynamic regulation of PiT1 recycling and XPR1 efflux via InsP8–SPX, refining cellular explanations for rapid Pi shifts on refeeding. URL: https://doi.org/10.3389/fphar.2023.1163442; Mar 2023. (borriello2025understandingrefeedingsyndrome pages 2-4)
- Hospital outcomes (2024): A Japanese cohort of 955 urgent HDU admissions stratified by modified NICE risk found very high-risk patients had markedly increased 30‑day mortality (21.7%; adjusted OR 5.54), underscoring prognostic relevance and the need for preventive strategies. URL: https://doi.org/10.3390/nu16193287; Sep 2024. ()
- Pediatric/AN practice (2024): In adolescents with anorexia nervosa (n=113), RS occurred in 41% using ASPEN criteria; olanzapine use correlated with more positive phosphate balance but not RS incidence, highlighting complex pharmacologic interactions during refeeding. URL: https://doi.org/10.1007/s00431-024-05430-9; Feb 2024. ()
- Narrative/pragmatic reviews (2024): Multiple 2024 reviews reinforce early timing (2–5 days), electrolyte monitoring, and thiamine supplementation as prevention. URLs: https://doi.org/10.12775/qs.2024.19.53773 (Aug 2024); https://doi.org/10.25060/residpediatr-2024.v14n3-1101 (Jan 2024). (mazur2024advancesinunderstanding pages 5-8, machado2024refeedingsyndromein pages 2-4)

Applications and implementations
- Guideline-driven prevention: ASPEN recommends conservative initiation (e.g., 10–20 kcal/kg/day or 100–150 g dextrose in first 24 h), frequent electrolyte monitoring (q12h for first 3 days in high-risk), and prefeeding thiamine 100 mg then daily for 5–7 days or longer. URL: https://doi.org/10.1002/ncp.10474; Mar 2020. (silva2020aspenconsensusrecommendations pages 12-14)
- Risk stratification and monitoring in practice: NICE-style risk criteria commonly used to identify high-risk patients; reviews emphasize sodium restriction and fluid vigilance to mitigate edema and heart failure. URL: https://doi.org/10.12775/qs.2024.19.53773; Aug 2024. (mazur2024advancesinunderstanding pages 5-8)

Expert opinions and consensus
- Consensus documents emphasize that RFS is often preventable with careful assessment, slow advancement, and electrolyte/thiamine repletion; yet true incidence remains uncertain due to heterogeneous definitions. URL: ASPEN 2020. (silva2020aspenconsensusrecommendations pages 2-3, silva2020aspenconsensusrecommendations pages 12-14)
- Critical care perspective highlights the need for early identification and careful caloric strategies outside ICU as well, given the prognostic impact in high-dependency settings. URL: https://doi.org/10.3390/nu17111866; May 2025; https://doi.org/10.3390/nu16193287; Sep 2024. (borriello2025understandingrefeedingsyndrome pages 4-5)

Relevant statistics and data from recent studies
- HDU cohort (Japan, 2024): 955 patients; 2.4% very high risk; 30‑day mortality 21.7% in very high risk vs ~5% others; adjusted OR 5.54 (95% CI 1.73–17.79). URL: https://doi.org/10.3390/nu16193287; Sep 2024. ()
- AN pediatric cohort (2016–2020 admissions analyzed in 2024 report): RS in 41% (mostly mild); mean intake ~1378 ± 289 kcal/day; olanzapine associated with improved phosphate balance but not RS incidence. URL: https://doi.org/10.1007/s00431-024-05430-9; Feb 2024. ()
- Timing of hypophosphatemia: Pediatric review notes phosphate decline typically appears 48–72 h after feeding initiation, aligning with early monitoring windows. URL: https://doi.org/10.25060/residpediatr-2024.v14n3-1101; Jan 2024. (machado2024refeedingsyndromein pages 2-4)

Direct supporting quotes
- “When glucose appears in the bloodstream, insulin secretion rises… rising insulin levels drive phosphorus and potassium intracellularly… and [stimulate] the sodium-potassium adenosine triphosphatase [ATPase].” URL: https://doi.org/10.1002/ncp.10474; Mar 2020. (silva2020aspenconsensusrecommendations pages 2-3)
- Hypophosphatemia timing: “the decrease in phosphate usually appears 48–72 hours after starting feeding.” URL: https://doi.org/10.25060/residpediatr-2024.v14n3-1101; Jan 2024. (machado2024refeedingsyndromein pages 2-4)
- RS spectrum and fluid retention: refeeding induces “abrupt surge in insulin… immediate shift…,” increased cofactor demand and electrolyte uptake; edema/heart failure may reflect multiple mechanisms beyond anti‑natriuresis alone. URL: https://doi.org/10.3390/nu17111866; May 2025. (borriello2025understandingrefeedingsyndrome pages 4-5)

Gene/protein annotations with ontology terms
- INS (HGNC:6081): insulin; process: insulin receptor signaling (GO:0008286). (silva2020aspenconsensusrecommendations pages 2-3)
- ATP1A1 (HGNC:813): Na+/K+-ATPase α1; component: plasma membrane; process: potassium ion transport (GO:0006813). (silva2020aspenconsensusrecommendations pages 2-3)
- PDHA1 (HGNC:8806): PDH E1 alpha; component: mitochondrial matrix; process: pyruvate dehydrogenase complex (GO:0045254); cofactor: thiamine diphosphate. (aini2024refeedingsyndromeina pages 9-10)
- OGDH (HGNC:8125): 2‑oxoglutarate dehydrogenase; mitochondrial; process: TCA cycle (GO:0006099); thiamine-dependent. (aini2024refeedingsyndromeina pages 9-10)
- TKT (HGNC:11849): transketolase; cytosol; process: pentose-phosphate shunt (GO:0006098); thiamine-dependent. (aini2024refeedingsyndromeina pages 9-10)
- SLC20A1 (HGNC:10919)/SLC20A2 (HGNC:10920): Na+-phosphate cotransport; process: phosphate ion transport (GO:0006817). (borriello2025understandingrefeedingsyndrome pages 2-4)
- XPR1 (HGNC:12801): phosphate efflux transporter; process: phosphate export from cell (GO:1902480). (borriello2025understandingrefeedingsyndrome pages 2-4)

Phenotype, cell type, and anatomical annotations
- HP:0002141 hypophosphatemia; HP:0002900 hypokalemia; HP:0002142 hypomagnesemia; HP:0002151 lactic acidosis; HP:0011675 arrhythmia; HP:0001715 heart failure; HP:0002878 respiratory failure; HP:0001697 Wernicke encephalopathy; HP:0000969 edema. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5, machado2024refeedingsyndromein pages 2-4, aini2024refeedingsyndromeina pages 9-10, mazur2024advancesinunderstanding pages 5-8)
- CL: cardiac myocyte; CL: skeletal muscle cell (diaphragm); CL: hepatocyte; CL: neuron; CL: erythrocyte. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5, machado2024refeedingsyndromein pages 2-4)
- UBERON: heart; diaphragm; liver; brain; lung. (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5, machado2024refeedingsyndromein pages 2-4)
- CHEBI: glucose (CHEBI:17234); insulin; phosphate (CHEBI:18367); potassium (CHEBI:29103); magnesium (CHEBI:27627); thiamine (CHEBI:15377). (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 2-4, mazur2024advancesinunderstanding pages 3-5)

Embedded artifact
| Category | Entity (preferred name) | Identifier (HGNC/GO/HP/CL/UBERON/CHEBI as applicable) | Mechanistic role in RFS (1 sentence) | Key evidence |
|---|---|---|---|---|
| Pathway | Insulin → PI3K–AKT–mTOR signaling | INS / PIK3CA / AKT1 / MTOR (HGNC) | Carbohydrate refeeding raises insulin which activates PI3K–AKT–mTOR to shift metabolism from catabolism to anabolism, increasing cellular glucose uptake and anabolic phosphate demand that precipitates extracellular electrolyte falls. | (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Protein | Na+/K+-ATPase (alpha subunit) | ATP1A1 (HGNC:ATP1A1) | Stimulated directly by insulin to drive cellular K+ influx and contribute to rapid extracellular hypokalemia during early refeeding. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Enzyme complex | Pyruvate dehydrogenase complex (PDH) | PDHA1 (HGNC:PDHA1) (component of PDH complex) | Thiamine-dependent PDH increases flux of glycolysis into the TCA cycle during refeeding; thiamine deficiency impairs PDH causing pyruvate→lactate shunting and lactic acidosis. | (aini2024refeedingsyndromeina pages 9-10, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Enzyme | 2-oxoglutarate dehydrogenase (alpha-ketoglutarate dehydrogenase) | OGDH (HGNC:OGDH) | Thiamine-dependent TCA enzyme whose increased activity in refeeding raises cofactor demand and is vulnerable when thiamine is depleted, impairing aerobic metabolism. | (aini2024refeedingsyndromeina pages 9-10, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Enzyme | Transketolase | TKT (HGNC:TKT) | Thiamine-dependent pentose phosphate pathway enzyme; increased carbohydrate flux raises thiamine demand and transketolase activity, linking deficiency to metabolic dysfunction. | (aini2024refeedingsyndromeina pages 9-10, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Transporter | SLC20A1 (PiT1) | SLC20A1 (HGNC:SLC20A1) | Na+-dependent phosphate importer contributing to cellular Pi uptake during refeeding-driven increased phosphate demand. | (borriello2025understandingrefeedingsyndrome pages 2-4) |
| Transporter | SLC20A2 (PiT2) | SLC20A2 (HGNC:SLC20A2) | Alternate Na+-Pi cotransporter implicated in adjusting cellular phosphate influx when extracellular phosphate is repleted or shifted. | (borriello2025understandingrefeedingsyndrome pages 2-4) |
| Transporter | XPR1 (phosphate efflux) | XPR1 (HGNC:XPR1) | Mediates phosphate efflux from cells; regulation of XPR1 contributes to intracellular/extracellular Pi homeostasis during refeeding. | (borriello2025understandingrefeedingsyndrome pages 2-4) |
| Process | Glycolysis | GO:0006096 (Glycolysis) | Rapid carbohydrate provision increases glycolytic flux requiring phosphorylation steps that consume intracellular phosphate and drive hypophosphatemia. | (borriello2025understandingrefeedingsyndrome pages 4-5, machado2024refeedingsyndromein pages 2-4) |
| Ion homeostasis | Phosphate homeostasis | — | Increased cellular phosphorylation (ATP, 2,3‑DPG) and transporter-mediated uptake during refeeding cause a net fall in serum phosphate (hypophosphatemia). | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Ion homeostasis | Potassium homeostasis | — | Insulin-stimulated cellular uptake via Na+/K+-ATPase and increased anabolism causes extracellular hypokalemia and risk of arrhythmia. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Ion homeostasis | Magnesium homeostasis | — | Mg2+ is a cofactor for Na+/K+-ATPase and many kinases; depletion exacerbates hypokalemia and contributes to neuromuscular/cardiac instability in RFS. | (mazur2024advancesinunderstanding pages 3-5, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Cell type | Cardiac myocyte | CL: cardiac muscle cell (CL identifier as applicable) | High ATP demand and sensitivity to hypophosphatemia/hypokalemia/hypomagnesemia predispose to arrhythmia, contractile dysfunction and heart failure during RFS. | (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Cell type | Diaphragm muscle cell (skeletal muscle) | CL: skeletal muscle cell (diaphragm region) | Hypophosphatemia reduces ATP and 2,3‑DPG in muscle causing diaphragmatic weakness and possible respiratory failure. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Cell type | Hepatocyte | CL: hepatocyte | Liver shifts from fatty acid to carbohydrate metabolism on refeeding, can develop hepatic steatosis and altered handling of glucose/phosphate and thiamine-dependent metabolism. | (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8) |
| Cell type | Neuron | CL: neuron | Thiamine deficiency and electrolyte disturbances (particularly hypophosphatemia) impair neuronal metabolism and can precipitate Wernicke encephalopathy. | (aini2024refeedingsyndromeina pages 9-10, mazur2024advancesinunderstanding pages 5-8) |
| Cell type | Erythrocyte | CL: erythrocyte | Intracellular phosphate is critical for 2,3‑DPG; hypophosphatemia impairs oxygen delivery via reduced 2,3‑DPG and can cause hemolysis. | (machado2024refeedingsyndromein pages 2-4, aini2024refeedingsyndromeina pages 9-10) |
| Anatomy | Heart | UBERON:heart (where applicable) | Organ-level manifestation: susceptibility to fluid overload, arrhythmia and pump failure when electrolytes and ATP are depleted during refeeding. | (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Anatomy | Diaphragm | UBERON:diaphragm (where applicable) | Respiratory compromise due to diaphragmatic weakness from low intracellular phosphate and ATP during early refeeding. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Anatomy | Liver | UBERON:liver (where applicable) | Site of metabolic shift and thiamine-dependent TCA activity; vulnerable to steatosis and metabolic dysregulation on rapid refeeding. | (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8) |
| Anatomy | Brain | UBERON:brain (where applicable) | Target of thiamine deficiency (Wernicke) and electrolyte-mediated dysfunction leading to encephalopathy and neuromuscular signs. | (aini2024refeedingsyndromeina pages 9-10, mazur2024advancesinunderstanding pages 5-8) |
| Anatomy | Lung | UBERON:lung (where applicable) | Pulmonary edema and respiratory failure may follow fluid retention and cardiac dysfunction during RFS. | (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8) |
| Chemical | Glucose | CHEBI:17234 (glucose) | Exogenous glucose is the trigger for insulin release and the metabolic shift that drives intracellular electrolyte/phosphate demand. | (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Chemical | Insulin | HGNC:INS | Hormone that acutely stimulates cellular uptake of glucose and K+, activates Na+/K+-ATPase, and promotes anabolic phosphate utilization. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Chemical | Phosphate (inorganic) | CHEBI:18367 (inorganic phosphate) | Central substrate for ATP and 2,3‑DPG synthesis; cellular sequestration during refeeding causes hypophosphatemia with multi‑system effects. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Chemical | Potassium (K+) | CHEBI:29103 (potassium ion) | Rapid intracellular shift driven by insulin/Na+/K+-ATPase causes serum hypokalemia and electrical instability. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Chemical | Magnesium (Mg2+) | CHEBI:27627 (magnesium ion) | Cofactor for ATPases and kinases; depletion worsens K+ losses and neuromuscular/cardiac complications in RFS. | (mazur2024advancesinunderstanding pages 3-5, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Chemical | Thiamine (vitamin B1) | CHEBI:15377 (thiamine) | Essential cofactor for PDH, OGDH and transketolase; deficiency during refeeding impairs aerobic metabolism and risks lactic acidosis and Wernicke encephalopathy. | (aini2024refeedingsyndromeina pages 9-10, mazur2024advancesinunderstanding pages 5-8) |
| Phenotype | Hypophosphatemia | HP:0002141 (hypophosphatemia) | Hallmark biochemical abnormality in RFS that causes muscle weakness, hemolysis, impaired oxygen delivery and organ dysfunction. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Phenotype | Hypokalemia | HP:0002900 (hypokalemia) | Causes membrane hyperpolarization, arrhythmia risk and muscle weakness during refeeding-driven intracellular K+ shifts. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Phenotype | Hypomagnesemia | HP:0002142 (hypomagnesemia) | Exacerbates refractory hypokalemia and contributes to arrhythmias and neuromuscular instability in RFS. | (mazur2024advancesinunderstanding pages 3-5, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Phenotype | Lactic acidosis | HP:0002151 (lactic acidosis) | Results from impaired PDH flux when thiamine is deficient or mitochondrial metabolism is overwhelmed during early refeeding. | (aini2024refeedingsyndromeina pages 9-10, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Phenotype | Arrhythmia | HP:0011675 (arrhythmia) | Electrolyte disturbances (low K+, Mg2+, PO4) and reduced myocardial ATP predispose to potentially fatal arrhythmias. | (silva2020aspenconsensusrecommendations pages 2-3, borriello2025understandingrefeedingsyndrome pages 4-5) |
| Phenotype | Heart failure | HP:0001715 (heart failure) | Fluid retention plus weakened myocardial energetics from hypophosphatemia/hypokalemia can precipitate acute decompensated heart failure. | (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8) |
| Phenotype | Respiratory failure | HP:0002878 (respiratory failure) | Diaphragmatic weakness from phosphate/ATP depletion can cause hypoventilation and need for ventilatory support. | (silva2020aspenconsensusrecommendations pages 2-3, machado2024refeedingsyndromein pages 2-4) |
| Phenotype | Wernicke encephalopathy | HP:0001697 (Wernicke encephalopathy) | Thiamine deficiency after refeeding can produce ophthalmoplegia, ataxia and encephalopathy requiring urgent thiamine replacement. | (aini2024refeedingsyndromeina pages 9-10, mazur2024advancesinunderstanding pages 5-8) |
| Phenotype | Edema / fluid overload | HP:0000969 (edema) | Insulin-mediated anti-natriuresis and retained sodium/water during refeeding can produce rapid fluid gain and pulmonary edema. | (borriello2025understandingrefeedingsyndrome pages 4-5, mazur2024advancesinunderstanding pages 5-8) |


*Table: Concise ontology-mapped table summarizing key pathways, proteins, transporters, cell types, organs, chemicals and phenotypes involved in refeeding syndrome (RFS), with one-line mechanistic notes and evidence citations for each entry.*

Limitations and open questions
- While insulin-mediated mechanisms are clear, precise contributions of aldosterone/ADH and endothelial leak to fluid overload require further elucidation; transporter-level regulation (PiT1 recycling, XPR1–InsP8) is emerging and has not yet been directly studied in clinical RFS cohorts. (borriello2025understandingrefeedingsyndrome pages 2-4, borriello2025understandingrefeedingsyndrome pages 4-5)

References (URLs and dates)
- ASPEN Consensus Recommendations for Refeeding Syndrome. Nutrition in Clinical Practice. Published Mar 2020. URL: https://doi.org/10.1002/ncp.10474. (silva2020aspenconsensusrecommendations pages 2-3, silva2020aspenconsensusrecommendations pages 12-14)
- Understanding Refeeding Syndrome in Critically Ill Patients: A Narrative Review. Nutrients. Published May 2025. URL: https://doi.org/10.3390/nu17111866. (borriello2025understandingrefeedingsyndrome pages 4-5, borriello2025understandingrefeedingsyndrome pages 2-4)
- Advances in Understanding and Managing Refeeding Syndrome: A Comprehensive Review. Quality in Sport. Published Aug 2024. URL: https://doi.org/10.12775/qs.2024.19.53773. (mazur2024advancesinunderstanding pages 3-5, mazur2024advancesinunderstanding pages 5-8)
- Refeeding syndrome in the severe malnourished: the nutricional challenges. Residência Pediátrica. Published Jan 2024. URL: https://doi.org/10.25060/residpediatr-2024.v14n3-1101. (machado2024refeedingsyndromein pages 2-4)
- Role of transporters in regulating mammalian intracellular inorganic phosphate. Frontiers in Pharmacology. Published Mar 2023. URL: https://doi.org/10.3389/fphar.2023.1163442. (borriello2025understandingrefeedingsyndrome pages 2-4)
- Association between Poor Outcomes and Risk of Refeeding Syndrome among Patients Urgently Admitted to the High Dependency Unit. Nutrients. Published Sep 2024. URL: https://doi.org/10.3390/nu16193287. ()
- Refeeding syndrome and psychopharmacological interventions in children and adolescents with Anorexia Nervosa. Eur J Pediatr. Published Feb 2024. URL: https://doi.org/10.1007/s00431-024-05430-9. ()

References

1. (silva2020aspenconsensusrecommendations pages 2-3): Joshua S. V. da Silva, David S. Seres, Kim Sabino, Stephen C. Adams, Gideon J. Berdahl, Sandra Wolfe Citty, M. Petrea Cober, David C. Evans, June R. Greaves, Kathleen M. Gura, Austin Michalski, Stephen Plogsted, Gordon S. Sacks, Anne M. Tucker, Patricia Worthington, Renee N. Walker, and Phil Ayers. Aspen consensus recommendations for refeeding syndrome. Nutrition in clinical practice : official publication of the American Society for Parenteral and Enteral Nutrition, 35:178-195, Mar 2020. URL: https://doi.org/10.1002/ncp.10474, doi:10.1002/ncp.10474. This article has 580 citations.

2. (mazur2024advancesinunderstanding pages 5-8): Agata Mazur, Aleksy Bizan, Natalia Dąbrowska, Aleksandra Kublińska, Magdalena Madera, Krzysztof Marcinkowski, Sylwia Mazur, Emilia Nagórska, Karolina Strus, and Roksana Zdunek. Advances in understanding and managing refeeding syndrome: a comprehensive review. Quality in Sport, 19:53773, Aug 2024. URL: https://doi.org/10.12775/qs.2024.19.53773, doi:10.12775/qs.2024.19.53773. This article has 0 citations.

3. (borriello2025understandingrefeedingsyndrome pages 4-5): Raffaele Borriello, Giorgio Esposto, Maria Elena Ainora, Giorgio Podagrosi, Giuliano Ferrone, Irene Mignini, Linda Galasso, Antonio Gasbarrini, and Maria Assunta Zocco. Understanding refeeding syndrome in critically ill patients: a narrative review. Nutrients, 17:1866, May 2025. URL: https://doi.org/10.3390/nu17111866, doi:10.3390/nu17111866. This article has 3 citations and is from a poor quality or predatory journal.

4. (mazur2024advancesinunderstanding pages 3-5): Agata Mazur, Aleksy Bizan, Natalia Dąbrowska, Aleksandra Kublińska, Magdalena Madera, Krzysztof Marcinkowski, Sylwia Mazur, Emilia Nagórska, Karolina Strus, and Roksana Zdunek. Advances in understanding and managing refeeding syndrome: a comprehensive review. Quality in Sport, 19:53773, Aug 2024. URL: https://doi.org/10.12775/qs.2024.19.53773, doi:10.12775/qs.2024.19.53773. This article has 0 citations.

5. (aini2024refeedingsyndromeina pages 9-10): MT Aini and K Yuliarti. Refeeding syndrome in malnutrition–diagnosis and management. Unknown journal, 2024.

6. (borriello2025understandingrefeedingsyndrome pages 2-4): Raffaele Borriello, Giorgio Esposto, Maria Elena Ainora, Giorgio Podagrosi, Giuliano Ferrone, Irene Mignini, Linda Galasso, Antonio Gasbarrini, and Maria Assunta Zocco. Understanding refeeding syndrome in critically ill patients: a narrative review. Nutrients, 17:1866, May 2025. URL: https://doi.org/10.3390/nu17111866, doi:10.3390/nu17111866. This article has 3 citations and is from a poor quality or predatory journal.

7. (machado2024refeedingsyndromein pages 2-4): Maria Machado, Ary Cardoso, Rosana Tumas, Christiane Kawano, and Camila Seo. Refeeding syndrome in the severe malnourished: the nutricional challenges. Residência Pediátrica, Jan 2024. URL: https://doi.org/10.25060/residpediatr-2024.v14n3-1101, doi:10.25060/residpediatr-2024.v14n3-1101. This article has 0 citations.

8. (silva2020aspenconsensusrecommendations pages 12-14): Joshua S. V. da Silva, David S. Seres, Kim Sabino, Stephen C. Adams, Gideon J. Berdahl, Sandra Wolfe Citty, M. Petrea Cober, David C. Evans, June R. Greaves, Kathleen M. Gura, Austin Michalski, Stephen Plogsted, Gordon S. Sacks, Anne M. Tucker, Patricia Worthington, Renee N. Walker, and Phil Ayers. Aspen consensus recommendations for refeeding syndrome. Nutrition in clinical practice : official publication of the American Society for Parenteral and Enteral Nutrition, 35:178-195, Mar 2020. URL: https://doi.org/10.1002/ncp.10474, doi:10.1002/ncp.10474. This article has 580 citations.