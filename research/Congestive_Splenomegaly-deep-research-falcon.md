---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-09T14:34:22.570933'
end_time: '2026-02-09T14:44:25.385576'
duration_seconds: 602.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congestive Splenomegaly
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Congestive Splenomegaly
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Congestive Splenomegaly**.
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
- **Disease Name:** Congestive Splenomegaly
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Congestive Splenomegaly**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Congestive Splenomegaly
- MONDO ID: Not clearly distinguished as a standalone entity in MONDO; typically modeled under portal hypertension–related splenomegaly and hypersplenism.
- Category: Complex

## Executive Summary
Congestive splenomegaly is a mechanistic consequence of venous outflow impedance and hyperdynamic splanchnic inflow, most commonly in portal hypertension (cirrhotic and non‑cirrhotic), but also in isolated left‑sided portal hypertension (splenic vein obstruction) and systemic venous congestion (right‑sided heart failure). Core drivers include: (i) hemodynamic load (backward/forward flow model) with splanchnic hyperemia; (ii) microvascular remodeling (sinusoidal capillarization, endothelial dysfunction, matrix deposition, angiogenesis and lymphangiogenesis); (iii) immune–stromal remodeling of white/red pulp and stress hematopoiesis; and (iv) hematologic sequelae of hypersplenism (sequestration/destruction) compounded by decreased hepatic thrombopoietin and iron–hepcidin dysregulation. These pathways correlate with collateral formation, variceal risk, and measurable increases in spleen stiffness on elastography. (yoshida2023theroleof pages 1-2, marginean2023diagnosticapproachand pages 6-7, weinzirl2021splenicrhythmsand pages 4-5, pastrovic2024serumproteomicprofiling pages 20-20)

| Mechanistic theme | Key mediators / players (HGNC where applicable) | Primary cell types (CL terms) | Key processes / GO terms | Anatomical sites (UBERON) | Representative evidence (Year, DOI URL, brief quoted/supporting note) |
|---|---|---|---|---|---|
| Hemodynamics: backward/forward flow, splanchnic hyperemia | NOS3 (eNOS), PTGIS (prostacyclin synthase), EDN1 (endothelin‑1), vasoactive peptides | Splanchnic endothelial cells; splenic arterial/venous endothelium | Splanchnic vasodilation, increased portal inflow, altered venous return | Portal vein, splenic vein, splenic artery (UBERON:0002107, UBERON:0001973) | 2023: "Splenomegaly in portal hypertension arises from a local hyperdynamic state around the spleen...splenic artery resistance index is selectively elevated in cirrhosis"; DOI: https://doi.org/10.1272/jnms.jnms.2023_90-104 (yoshida2023theroleof pages 1-2) |
| Sinusoidal / endothelial remodeling: LSEC capillarization & COL4 deposition (TNF‑α / NF‑κB) | COL4A1/COL4A2, TNF, NFKB1 | Liver sinusoidal endothelial cells (LSECs), splenic sinus lining cells | Capillarization, basement membrane (COL4) deposition, ECM remodeling | Hepatic sinusoid, splenic sinusoids (UBERON:0002106, UBERON:0002107) | 2024: Proteomics and LSEC studies implicate endothelial-driven ECM (collagen IV) and sinusoidal remodeling in portal hypertension; DOI: https://doi.org/10.1371/journal.pone.0301416 (pastrovic2024serumproteomicprofiling pages 20-20) |
| Angiogenesis & lymphangiogenesis: VEGF‑C / LYVE‑1 | VEGFC (HGNC:12683), VEGFD, LYVE1 | Lymphatic endothelial cells, vascular endothelium | Angiogenesis, lymphangiogenesis, vascular remodeling | Periportal regions, splenic hilum, lymphatic vessels (UBERON:0002106, UBERON:0002107) | 2024: "VEGF‑C and LYVE‑1 were found solely in CSPH group"; proteomic data support lymphangiogenic signatures in clinically significant portal HTN; DOI: https://doi.org/10.1371/journal.pone.0301416 (pastrovic2024serumproteomicprofiling pages 20-20) |
| Immune–stromal remodeling: white/red pulp expansion, macrophage TGF‑β1, extramedullary hematopoiesis | TGFB1, CXCL12, CSF1 | Splenic macrophages (red pulp macrophage), stromal fibroblasts, lymphocytes | White‑pulp hyperplasia, macrophage activation, extramedullary hematopoiesis | Spleen (white pulp, red pulp) (UBERON:0002107) | 2023–2024: "Enlargement and hyperactivation of splenic lymphoid tissue" and spleen as site of extramedullary hematopoiesis in systemic congestion; DOI: https://doi.org/10.1272/jnms.jnms.2023_90-104; DOI: https://doi.org/10.1007/s10741-024-10418-6 (yoshida2023theroleof pages 2-4, hiraiwa2024interplayofthe pages 2-4) |
| Hematologic cytopenias: sequestration/destruction, decreased hepatic TPO, hepcidin/iron dysregulation | THPO (thrombopoietin), HAMP (hepcidin), IL6, TNF | Platelets, splenic macrophages, hepatocytes, megakaryocytes | Phagocytosis, platelet sequestration, decreased thrombopoiesis, altered iron homeostasis | Spleen, liver (UBERON:0002107, UBERON:0002106) | 2023: "Hypersplenism...is associated with peripheral cytopenia" and reduced hepatic TPO production; DOI: https://doi.org/10.3390/gastroent14030024 (marginean2023diagnosticapproachand pages 6-7) |
| Collateralization & varices (compensatory pathways) | VEGFA, angiopoietins, matrix remodelers | Vascular endothelial cells, perivascular stromal cells | Development of portosystemic collaterals, variceal formation, altered hemodynamics | Paraumbilical veins, left gastric vein, short gastric veins (UBERON:0002113 regionally) | 2021: Splenic enlargement and loss of rhythmic venous regulation correlate with collateral formation and varices; DOI: https://doi.org/10.1159/000507346 (weinzirl2021splenicrhythmsand pages 4-5) |
| Left‑sided portal hypertension: splenic vein thrombosis / torsion | Coagulation factors (F2, F5), platelet activation mediators | Splenic venous endothelium, platelets | Venous thrombosis, outflow obstruction, focal congestion | Splenic vein, short gastric veins (UBERON:0001973) | 2023: Reviews note splenic‑vein occlusion (thrombosis/torsion) causes left‑sided portal HTN with splenomegaly and isolated gastric varices; DOI: https://doi.org/10.1272/jnms.jnms.2023_90-104 (yoshida2023theroleof pages 1-2) |
| Systemic venous congestion / right‑sided HF effects on spleen | Sympathetic mediators, IL‑1β, alarmins | Splenic immune cells, vascular endothelium, stromal cells | Plasma extravasation, congestion‑driven inflammation, splenic metabolic activation | Spleen, hepatic venous outflow, systemic veins (UBERON:0002107) | 2024: "Interplay of the heart, spleen, and bone marrow...splenic extramedullary hematopoiesis" in HF models; DOI: https://doi.org/10.1007/s10741-024-10418-6 (hiraiwa2024interplayofthe pages 2-4) |
| Proteomic / inflammatory signatures in CSPH: NETs, CD44, ECM mediators | MPO, PADI4 (NETs), CD44, autotaxin (ENPP2) | Neutrophils, macrophages, endothelial cells | NET formation, ECM remodeling, inflammatory signaling | Spleen, blood plasma, liver | 2024: Serum proteomics identified NET‑related proteins, CD44, VEGF‑C and LYVE‑1 enriched in CSPH; "altered inflammatory response...vascular contractility and lymphangiogenesis"; DOI: https://doi.org/10.1371/journal.pone.0301416 (pastrovic2024serumproteomicprofiling pages 20-20) |


*Table: A compact, evidence‑linked summary table (2021–2024) of major mechanisms driving congestive splenomegaly and hypersplenism, mapping mediators, cell types, processes, sites, and representative citations useful for knowledge‑base annotation and mechanistic review.*

## 1. Core Pathophysiology
- Hemodynamic mechanisms
  - Backward/forward flow: Intrahepatic vascular resistance increases (backward flow) while compensatory increases in portal inflow (forward flow) produce a local hyperdynamic state around the spleen. Yoshida et al. emphasize a “selectively elevated splenic artery resistance index” in cirrhosis and that the splenic contribution to portal inflow rises (to ~50% in chronic hepatitis/cirrhosis; ~75% in idiopathic portal hypertension), supporting congestion plus active inflow recruitment. URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (Feb 2023). Quote: “In portal hypertension, a local hyperdynamic state occurs around the spleen… The splenic artery resistance index is significantly and selectively elevated in cirrhotic patients.” (yoshida2023theroleof pages 1-2, yoshida2023theroleof pages 2-4)
  - Splanchnic vasodilation: NO and prostacyclin (PGI2)–mediated vasodilation with hyperdynamic circulation increases splanchnic inflow, further augmenting portal pressure and splenic congestion, while endothelin‑1 contributes to vasoconstrictor–vasodilator imbalance. URL: https://doi.org/10.3390/gastroent14030024 (Aug 2023). (marginean2023diagnosticapproachand pages 6-7)

- Microvascular/endothelial remodeling
  - Sinusoidal capillarization and basement membrane deposition: Endothelial capillarization with collagen IV (COL4) deposition is a recognized driver of increased sinusoidal resistance in portal hypertension. Proteomic and endothelial literature identify endothelial dysfunction, ECM remodeling, and angiogenesis signatures in clinically significant portal hypertension (CSPH), including tenascin C, autotaxin, and NET‑related proteins. URL: https://doi.org/10.1371/journal.pone.0301416 (Apr 2024). (pastrovic2024serumproteomicprofiling pages 20-20)
  - Lymphangiogenesis: Serum proteomics in cACLD with CSPH found VEGF‑C and LYVE‑1 only in CSPH, suggesting lymphangiogenic remodeling that may influence splenic and periportal lymph flow and congestion. URL: https://doi.org/10.1371/journal.pone.0301416 (Apr 2024). (pastrovic2024serumproteomicprofiling pages 20-20)

- Immune and stromal remodeling
  - Spleen is not enlarged merely by passive congestion; chronic portal hypertension induces “enlargement and hyperactivation of splenic lymphoid tissue,” with increased reticular fibers and diffuse fibrosis, plus red‑pulp pooling. mTOR inhibition (rapamycin) reduced spleen size by ~44% in experimental settings, implying proliferative/growth signals. URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (Feb 2023). (yoshida2023theroleof pages 1-2, yoshida2023theroleof pages 2-4)
  - Extramedullary hematopoiesis (EMH): Heart‑failure literature implicates splenic EMH during systemic congestion and inflammatory stress, linking cardio‑splenic–marrow axes to chronic inflammation. URL: https://doi.org/10.1007/s10741-024-10418-6 (Jul 2024). (hiraiwa2024interplayofthe pages 2-4)

- Hematologic consequences (hypersplenism)
  - Sequestration and destruction: The spleen stores ~1/3 of platelets; with splenomegaly, increased phagocytic activity causes platelet, erythrocyte, and leukocyte destruction, leading to cytopenias. URL: https://doi.org/10.3390/gastroent14030024 (Aug 2023). (marginean2023diagnosticapproachand pages 6-7)
  - Decreased hepatic thrombopoietin (THPO) and iron–hepcidin axis: Reduced hepatic TPO production and inflammatory regulation of hepcidin (HAMP) contribute to thrombocytopenia and anemia in chronic liver disease. URL: https://doi.org/10.3390/gastroent14030024 (Aug 2023). (marginean2023diagnosticapproachand pages 6-7)

- Collateralization and varices; splenic stiffness
  - In portal hypertension, loss of splenic rhythmic regulation, venous sinusoid enlargement, and connective tissue hypertrophy accompany collateral vessel formation and variceal risk; postprandial and baseline spleen stiffness rise with portal flow/fibrosis. URL: https://doi.org/10.1159/000507346 (May 2021). (weinzirl2021splenicrhythmsand pages 4-5)

## 2. Key Molecular Players
- Genes/proteins (HGNC):
  - Vasoactive/endothelial: NOS3 (eNOS), PTGIS (prostacyclin synthase), EDN1 (endothelin‑1) (vasodilator–vasoconstrictor imbalance in splanchnic bed). (marginean2023diagnosticapproachand pages 6-7)
  - Matrix/endothelial remodeling: COL4A1/COL4A2 (collagen IV), CD44 (matrix receptor), ENPP2/autotaxin (vascular contractility), mediators of NETs (MPO, PADI4) (CSPH proteomics). (pastrovic2024serumproteomicprofiling pages 20-20)
  - Lymphangiogenesis: VEGFC, LYVE1 (CSPH‑specific detection). (pastrovic2024serumproteomicprofiling pages 20-20)
  - Cytokine axes: TNF (NF‑κB–dependent endothelial activation), TGFB1 (splenic macrophages; fibrosis signaling). (yoshida2023theroleof pages 2-4)
  - Hematology: THPO (liver‑derived), HAMP (hepcidin). (marginean2023diagnosticapproachand pages 6-7)

- Chemical entities (CHEBI):
  - Nitric oxide (CHEBI:16480), prostacyclin/PGI2 (CHEBI:15552), endothelin‑1 peptide (CHEBI:6801). (marginean2023diagnosticapproachand pages 6-7)

- Cell types (CL terms):
  - Liver sinusoidal endothelial cells (LSECs), splenic sinus lining endothelial cells; splenic red‑pulp macrophages; lymphatic endothelial cells; splenic lymphocytes; megakaryocytes. (pastrovic2024serumproteomicprofiling pages 20-20, yoshida2023theroleof pages 2-4, marginean2023diagnosticapproachand pages 6-7)

- Anatomical locations (UBERON):
  - Spleen (UBERON:0002107), hepatic sinusoid (UBERON:0002106), portal vein/splenic vein (UBERON:0002107 context; vascular tree), short gastric/left gastric veins (collaterals). (weinzirl2021splenicrhythmsand pages 4-5)

## 3. Biological Processes (GO) Disrupted
- Regulation of systemic arterial blood pressure and vasodilation; nitric‑oxide mediated signaling pathway; prostaglandin biosynthetic process; response to endothelin. (marginean2023diagnosticapproachand pages 6-7)
- Angiogenesis and lymphangiogenesis; extracellular matrix organization; basement membrane assembly (collagen IV deposition); endothelial cell junction organization. (pastrovic2024serumproteomicprofiling pages 20-20)
- Immune activation and leukocyte-mediated cytotoxicity; macrophage activation; extramedullary hematopoiesis; neutrophil extracellular trap formation. (hiraiwa2024interplayofthe pages 2-4, pastrovic2024serumproteomicprofiling pages 20-20)
- Platelet homeostasis; erythrocyte clearance; regulation of thrombopoiesis; iron ion homeostasis via hepcidin. (marginean2023diagnosticapproachand pages 6-7)

## 4. Cellular Components Involved
- Endothelial cell plasma membrane and caveolae; sinusoidal basement membrane (emergent in capillarization) with collagen IV; splenic cords and venous sinusoids (red pulp); white pulp germinal centers; extracellular space/plasma (proteomic signatures). (pastrovic2024serumproteomicprofiling pages 20-20, weinzirl2021splenicrhythmsand pages 4-5, yoshida2023theroleof pages 2-4)

## 5. Disease Progression (Sequence of Events)
1) Initiating lesion: Intrahepatic resistance (fibrosis, sinusoidal capillarization) or splenic venous outflow obstruction (SVT/torsion) or systemic venous congestion (right‑sided HF). (pastrovic2024serumproteomicprofiling pages 20-20, marginean2023diagnosticapproachand pages 6-7)
2) Hemodynamic response: Splanchnic vasodilation (NO/PGI2) and increased portal inflow (forward flow) superimposed on backpressure (backward flow), generating local hyperdynamic state at the spleen. (yoshida2023theroleof pages 1-2, marginean2023diagnosticapproachand pages 6-7)
3) Splenic microvascular remodeling: Sinusoid dilation, endothelial dysfunction, ECM (COL4) deposition, angiogenesis/lymphangiogenesis; loss of rhythmic contractility; increased stiffness. (pastrovic2024serumproteomicprofiling pages 20-20, weinzirl2021splenicrhythmsand pages 4-5)
4) Immune–stromal remodeling: White‑pulp hyperplasia, macrophage activation (TGF‑β1), diffuse fibrosis; in systemic congestion, induction of splenic EMH. (yoshida2023theroleof pages 2-4, hiraiwa2024interplayofthe pages 2-4)
5) Hypersplenism: Increased pooling/sequestration and destruction of platelets/erythrocytes/leukocytes; compounded by decreased hepatic THPO and iron–hepcidin dysregulation. (marginean2023diagnosticapproachand pages 6-7)
6) Clinical complications: Development of portal collaterals and varices; rising spleen stiffness/volume; cytopenias with bleeding risk; in left‑sided PH, isolated gastric varices. (weinzirl2021splenicrhythmsand pages 4-5, yoshida2023theroleof pages 1-2)

## 6. Phenotypic Manifestations (HP terms linkage)
- Splenomegaly (HP:0001744) with increased stiffness/size on ultrasound/elastography; postprandial increases reflect hyperemia. Quote: “postprandial congestion with significant increases in volume… the spleen’s rhythmical function is lost in portal hypertension.” URL: https://doi.org/10.1159/000507346 (May 2021). (weinzirl2021splenicrhythmsand pages 4-5)
- Hypersplenism with cytopenias: Thrombocytopenia (HP:0001873), anemia (HP:0001903), leukopenia (HP:0001882), attributed to sequestration/destruction and low THPO. URL: https://doi.org/10.3390/gastroent14030024 (Aug 2023). (marginean2023diagnosticapproachand pages 6-7)
- Portal hypertension signs: Portosystemic collaterals and varices (HP:0001403), ascites (HP:0001541); splenic contribution to portal inflow increases markedly. URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (Feb 2023). (yoshida2023theroleof pages 2-4)
- Left‑sided portal hypertension: Gastric varices with splenomegaly due to splenic‑vein obstruction (sinistral PH). (yoshida2023theroleof pages 1-2)

## Current Applications and Real‑World Implementations
- Noninvasive assessment: Spleen stiffness (shear‑wave elastography) and platelet count are widely used to infer clinically significant portal hypertension and variceal risk; postprandial changes provide functional readouts of splanchnic hyperemia. Mechanistic basis grounded in splanchnic vasodilation and splenic microvascular remodeling. (weinzirl2021splenicrhythmsand pages 4-5)
- Interventions that modulate splanchnic inflow and portal pressure (e.g., non‑selective beta‑blockers) have the potential to reduce splenic congestion and hypersplenism manifestations indirectly by reversing hyperdynamic splanchnic circulation. Mechanistic underpinnings cited in 2023 overview of CLD anemia and PH physiology. (marginean2023diagnosticapproachand pages 6-7)
- Surgical/IR approaches (partial splenic embolization, splenectomy) target refractory hypersplenism/variceal risk; Yoshida 2023 reviews spleen’s regulatory role and outcomes of such strategies in the hepatosplenic axis. (yoshida2023theroleof pages 2-4)

## Expert Opinions and Authoritative Analyses (2023–2024 priority)
- Yoshida 2023: Positions the spleen as a key regulator in the “forward flow” model of portal hypertension, with data on splenic artery resistance and lymphoid hyperactivation—arguing splenomegaly is not purely passive congestion. URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (Feb 2023). (yoshida2023theroleof pages 1-2, yoshida2023theroleof pages 2-4)
- Pastrovic 2024: Proteomics delineates CSPH‑specific markers (CD44, VEGF‑C, LYVE‑1; NETs), proposing inflammation‑vascular contractility‑lymphangiogenesis triad as key in PH pathogenesis and biomarker discovery. URL: https://doi.org/10.1371/journal.pone.0301416 (Apr 2024). (pastrovic2024serumproteomicprofiling pages 20-20)
- Marginean 2023: Synthesizes anemia mechanisms in CLD, emphasizing hypersplenism (sequestration/destruction), reduced hepatic THPO, and hepcidin‑mediated iron restriction. URL: https://doi.org/10.3390/gastroent14030024 (Aug 2023). (marginean2023diagnosticapproachand pages 6-7)
- Weinzirl 2021: Reviews splenic rhythmic regulation and its loss in portal hypertension; links hemodynamics to structural remodeling and variceal risk; supports stiffness/volume as functional biomarkers. URL: https://doi.org/10.1159/000507346 (May 2021). (weinzirl2021splenicrhythmsand pages 4-5)
- Heart‑failure perspective (Hiraiwa 2024): Highlights splenic EMH and inflammatory crosstalk in systemic venous congestion. URL: https://doi.org/10.1007/s10741-024-10418-6 (Jul 2024). (hiraiwa2024interplayofthe pages 2-4)

## Statistics and Data from Recent Studies
- Splenic inflow contributions: Rising from ~20–40% (normal) to ~50% (chronic hepatitis/cirrhosis) and ~75% (idiopathic portal hypertension), indicating an active role of the spleen in maintaining portal inflow under elevated resistance. (Yoshida 2023). URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (Feb 2023). (yoshida2023theroleof pages 2-4)
- Pharmacology: mTOR inhibition (rapamycin) reduced spleen size by ~44% in portal‑hypertensive models, supporting proliferative/immune activation components of splenomegaly beyond passive congestion. (Yoshida 2023). URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (Feb 2023). (yoshida2023theroleof pages 2-4)
- Proteomics (CSPH vs non‑CSPH): CSPH sera uniquely contained CD44, VEGF‑C, LYVE‑1; NET‑related proteins elevated, suggesting distinct endothelial/lymphatic/inflammatory signatures in patients with CSPH. (Pastrovic 2024). URL: https://doi.org/10.1371/journal.pone.0301416 (Apr 2024). (pastrovic2024serumproteomicprofiling pages 20-20)
- Hematology prevalence: Thrombocytopenia frequent in CLD; mechanisms include hypersplenism and reduced hepatic THPO; pro‑inflammatory cytokines limit iron availability and erythropoiesis (anemia of inflammation). (Marginean 2023). URL: https://doi.org/10.3390/gastroent14030024 (Aug 2023). (marginean2023diagnosticapproachand pages 6-7)

## Evidence Items (PMIDs/DOIs and dates)
- Yoshida H, et al. The Role of the Spleen in Portal Hypertension. Journal of Nippon Medical School, Feb 2023. DOI: 10.1272/jnms.jnms.2023_90-104. URL: https://doi.org/10.1272/jnms.jnms.2023_90-104 (hemodynamics; lymphoid activation; hypersplenism). (yoshida2023theroleof pages 1-2, yoshida2023theroleof pages 2-4)
- Pastrovic F, et al. Serum proteomic profiling… CSPH. PLOS ONE, Apr 2024. DOI: 10.1371/journal.pone.0301416. URL: https://doi.org/10.1371/journal.pone.0301416 (VEGF‑C, LYVE‑1, CD44, NET proteins). (pastrovic2024serumproteomicprofiling pages 20-20)
- Marginean CM, et al. Diagnostic approach and pathophysiological mechanisms of anemia in CLD. Gastroenterology Insights, Aug 2023. DOI: 10.3390/gastroent14030024. URL: https://doi.org/10.3390/gastroent14030024 (hypersplenism; THPO; hepcidin). (marginean2023diagnosticapproachand pages 6-7)
- Weinzirl J, et al. Splenic Rhythms… Digestion, May 2021. DOI: 10.1159/000507346. URL: https://doi.org/10.1159/000507346 (hemodynamics; stiffness; collaterals). (weinzirl2021splenicrhythmsand pages 4-5)
- Hiraiwa H, et al. Interplay of the heart, spleen, and bone marrow in HF. Heart Failure Reviews, Jul 2024. DOI: 10.1007/s10741-024-10418-6. URL: https://doi.org/10.1007/s10741-024-10418-6 (splenic EMH in congestion). (hiraiwa2024interplayofthe pages 2-4)

## Structured Annotations for Knowledge Base
- Pathophysiology description: See Executive Summary and Sections 1–5. (yoshida2023theroleof pages 1-2, marginean2023diagnosticapproachand pages 6-7, pastrovic2024serumproteomicprofiling pages 20-20, weinzirl2021splenicrhythmsand pages 4-5)
- Gene/protein annotations (HGNC): NOS3, PTGIS, EDN1, COL4A1/COL4A2, CD44, ENPP2, VEGFC, LYVE1, TGFB1, THPO, HAMP, MPO, PADI4. (marginean2023diagnosticapproachand pages 6-7, pastrovic2024serumproteomicprofiling pages 20-20, yoshida2023theroleof pages 2-4)
- GO biological processes: nitric‑oxide mediated signaling; prostaglandin biosynthesis; endothelin receptor signaling; extracellular matrix organization; angiogenesis; lymphangiogenesis; NET formation; regulation of thrombopoiesis; iron ion homeostasis. (marginean2023diagnosticapproachand pages 6-7, pastrovic2024serumproteomicprofiling pages 20-20)
- Cellular components: endothelial cell membrane/caveolae; basement membrane (collagen IV); splenic cords/venous sinusoids; white‑pulp follicles; extracellular region/plasma. (pastrovic2024serumproteomicprofiling pages 20-20, weinzirl2021splenicrhythmsand pages 4-5)
- Phenotype associations (HP): Splenomegaly (HP:0001744); Thrombocytopenia (HP:0001873); Anemia (HP:0001903); Leukopenia (HP:0001882); Portal hypertension (HP:0001403); Ascites (HP:0001541). (marginean2023diagnosticapproachand pages 6-7, weinzirl2021splenicrhythmsand pages 4-5)
- Cell types (CL): Liver sinusoidal endothelial cell; splenic red‑pulp macrophage; lymphatic endothelial cell; megakaryocyte; B/T lymphocytes.
- Anatomical locations (UBERON): Spleen (UBERON:0002107); Hepatic sinusoid (UBERON:0002106); Portal vein and splenic vein vascular territories; Left gastric/short gastric veins (collaterals). (weinzirl2021splenicrhythmsand pages 4-5)
- Chemical entities (CHEBI): Nitric oxide (CHEBI:16480); PGI2 (CHEBI:15552); Endothelin‑1 (CHEBI:6801). (marginean2023diagnosticapproachand pages 6-7)

## Gaps and Future Directions
- Direct human mechanistic data for splenic sinus endothelial capillarization and collagen IV deposition remain less developed than hepatic LSEC literature; proteomic and imaging signals suggest analogous processes in the spleen during portal hypertension, warranting targeted histology and single‑cell studies in human spleens from PH contexts. (pastrovic2024serumproteomicprofiling pages 20-20)
- Quantitative thresholds linking spleen stiffness dynamics to specific risks (e.g., variceal bleeding) require harmonized, prospective validation integrating proteomic and imaging biomarkers. (weinzirl2021splenicrhythmsand pages 4-5, pastrovic2024serumproteomicprofiling pages 20-20)



References

1. (yoshida2023theroleof pages 1-2): Hiroshi Yoshida, Tetsuya Shimizu, Masato Yoshioka, Akira Matsushita, Youichi Kawano, Junji Ueda, Mampei Kawashima, Nobuhiko Taniai, and Yasuhiro Mamada. The role of the spleen in portal hypertension. Journal of Nippon Medical School = Nippon Ika Daigaku zasshi, 90 1:20-25, Feb 2023. URL: https://doi.org/10.1272/jnms.jnms.2023\_90-104, doi:10.1272/jnms.jnms.2023\_90-104. This article has 37 citations.

2. (marginean2023diagnosticapproachand pages 6-7): Cristina Maria Marginean, Denisa Pirscoveanu, Mihaela Popescu, Anca Oana Docea, Antonia Radu, Alin Iulian Silviu Popescu, Corina Maria Vasile, Radu Mitrut, Iulia Cristina Marginean, George Alexandru Iacob, Dan Mihai Firu, and Paul Mitrut. Diagnostic approach and pathophysiological mechanisms of anemia in chronic liver disease—an overview. Gastroenterology Insights, 14:327-341, Aug 2023. URL: https://doi.org/10.3390/gastroent14030024, doi:10.3390/gastroent14030024. This article has 13 citations.

3. (weinzirl2021splenicrhythmsand pages 4-5): Johannes Weinzirl, Lydia Garnitschnig, Tom Scheffers, Lukas Andrae, and Peter Heusser. Splenic rhythms and postprandial dynamics in physiology, portal hypertension, and functional hyposplenism: a review. Digestion, 102:326-334, May 2021. URL: https://doi.org/10.1159/000507346, doi:10.1159/000507346. This article has 12 citations and is from a peer-reviewed journal.

4. (pastrovic2024serumproteomicprofiling pages 20-20): Frane Pastrovic, Rudjer Novak, Ivica Grgurevic, Stela Hrkac, Grgur Salai, Marko Zarak, and Lovorka Grgurevic. Serum proteomic profiling of patients with compensated advanced chronic liver disease with and without clinically significant portal hypertension. PLOS ONE, 19:e0301416, Apr 2024. URL: https://doi.org/10.1371/journal.pone.0301416, doi:10.1371/journal.pone.0301416. This article has 1 citations and is from a peer-reviewed journal.

5. (yoshida2023theroleof pages 2-4): Hiroshi Yoshida, Tetsuya Shimizu, Masato Yoshioka, Akira Matsushita, Youichi Kawano, Junji Ueda, Mampei Kawashima, Nobuhiko Taniai, and Yasuhiro Mamada. The role of the spleen in portal hypertension. Journal of Nippon Medical School = Nippon Ika Daigaku zasshi, 90 1:20-25, Feb 2023. URL: https://doi.org/10.1272/jnms.jnms.2023\_90-104, doi:10.1272/jnms.jnms.2023\_90-104. This article has 37 citations.

6. (hiraiwa2024interplayofthe pages 2-4): Hiroaki Hiraiwa, Yoshimitsu Yura, Takahiro Okumura, and Toyoaki Murohara. Interplay of the heart, spleen, and bone marrow in heart failure: the role of splenic extramedullary hematopoiesis. Heart Failure Reviews, 29:1049-1063, Jul 2024. URL: https://doi.org/10.1007/s10741-024-10418-6, doi:10.1007/s10741-024-10418-6. This article has 10 citations and is from a peer-reviewed journal.