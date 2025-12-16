---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:15.208670'
end_time: '2025-12-15T09:18:34.595268'
duration_seconds: 319.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency**.
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
- **Disease Name:** Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency**.
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
- Disease Name: Glucose-6-Phosphate Dehydrogenase (G6PD) Deficiency
- MONDO ID: not specified in retrieved sources
- Category: Genetic (X-linked enzymopathy) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2)

Pathophysiology description
G6PD deficiency is an X-linked enzymopathy that reduces activity of the rate-limiting enzyme of the oxidative pentose phosphate pathway (PPP). In red blood cells (RBCs), which lack mitochondria, PPP-derived NADPH is the dominant source of reducing equivalents to maintain the glutathione system and broader redox homeostasis. In G6PD deficiency, diminished NADPH generation impairs glutathione reductase-mediated recycling of oxidized glutathione (GSSG) to reduced glutathione (GSH). This lowers cellular antioxidant capacity, promoting oxidative modification of hemoglobin (Heinz bodies), membrane lipid peroxidation, band 3 clustering, decreased deformability, and premature clearance or intravascular hemolysis. Oxidative stressors—especially certain drugs, infections, and oxidant foods such as fava beans—precipitate acute hemolytic anemia. Clinical phenotypes range from asymptomatic baseline to episodic hemolysis, neonatal jaundice, and in severe variants, chronic nonspherocytic hemolytic anemia (URLs: https://doi.org/10.3390/biom13081262, Aug 2023; https://doi.org/10.1155/2021/5529256, Apr 2021; https://doi.org/10.1016/j.tips.2021.07.002, Oct 2021) (orrico2023oxidativestressin pages 10-11, dore2021thecontroversialrole pages 1-2, garcia2021treatmentstrategiesfor pages 1-2).

1) Core Pathophysiology
- Primary mechanisms
  - PPP/NADPH impairment: G6PD catalyzes the first, rate-limiting step of the oxidative PPP that produces NADPH; reduced enzyme activity lowers NADPH supply in RBCs (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.1155/2021/5529256) (orrico2023oxidativestressin pages 10-11, dore2021thecontroversialrole pages 1-2).
  - Glutathione redox failure: Inadequate NADPH limits glutathione reductase recycling of GSSG to GSH, compromising detoxification of hydrogen peroxide and organic peroxides (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.1016/j.tips.2021.07.002) (orrico2023oxidativestressin pages 10-11, garcia2021treatmentstrategiesfor pages 1-2).
  - RBC oxidative injury: Hemoglobin oxidative denaturation (Heinz bodies), membrane lipid peroxidation, and cytoskeletal alterations reduce deformability and promote hemolysis (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.4314/sokjmls.v10i1.35) (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2).
  - Triggered hemolysis: Exposures that increase oxidant load—e.g., primaquine, sulfonamides, dapsone; infections; and fava bean metabolites (vicine/divicine)—precipitate acute hemolytic anemia in deficient individuals (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.5195/ijms.2020.637) (orrico2023oxidativestressin pages 10-11, ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).
  - Neonatal hyperbilirubinemia: In neonates with G6PD deficiency, unconjugated hyperbilirubinemia can occur rapidly, sometimes with minimal overt hemolysis, reflecting immature bilirubin conjugation/excretion superimposed on increased heme turnover and impaired antioxidant defenses (URL: https://doi.org/10.5195/ijms.2020.637) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).

- Dysregulated molecular pathways
  - Oxidative PPP and NADPH regeneration (G6PD; 6-phosphogluconate dehydrogenase) are diminished, altering the balance between glycolytic and PPP flux and limiting antioxidant capacity (URLs: https://doi.org/10.1155/2021/5529256; https://doi.org/10.3390/biom13081262) (dore2021thecontroversialrole pages 1-2, orrico2023oxidativestressin pages 10-11).
  - Antioxidant systems dependent on NADPH (glutathione reductase, peroxiredoxins, catalase in non-RBC tissues) are secondarily compromised in RBCs, with GSH depletion central to susceptibility (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.1016/j.tips.2021.07.002) (orrico2023oxidativestressin pages 10-11, garcia2021treatmentstrategiesfor pages 1-2).

- Affected cellular processes
  - Redox homeostasis; ROS detoxification; hemoglobin stability; membrane integrity; erythrocyte deformability and survival (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.4314/sokjmls.v10i1.35) (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2).

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - G6PD (HGNC:4421): X-linked enzyme catalyzing oxidation of glucose-6-phosphate to 6-phosphogluconolactone with reduction of NADP+ to NADPH (URLs: https://doi.org/10.1155/2021/5529256; https://doi.org/10.3390/biom13081262) (dore2021thecontroversialrole pages 1-2, orrico2023oxidativestressin pages 10-11).
  - GSR/glutathione reductase (HGNC:4635): NADPH-dependent enzyme for GSH regeneration; functionally impacted by NADPH deficit (URL: https://doi.org/10.1016/j.tips.2021.07.002) (garcia2021treatmentstrategiesfor pages 1-2).
  - Hemoglobin (HBB/HBA): Target of oxidation leading to Heinz bodies and precipitates (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).

- Chemical Entities (CHEBI)
  - NADPH (CHEBI:16474); reduced glutathione GSH (CHEBI:16856); oxidized glutathione GSSG (CHEBI:57925); hydrogen peroxide (CHEBI:16240); primaquine (CHEBI:8365); dapsone (CHEBI:4320). These entities mediate redox reactions and/or act as triggers of oxidative hemolysis (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.1016/j.tips.2021.07.002) (orrico2023oxidativestressin pages 10-11, garcia2021treatmentstrategiesfor pages 1-2).

- Cell Types (CL)
  - Erythrocyte (CL:0000232): Primary clinically affected cell; uniquely PPP-dependent for NADPH (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).
  - Leukocytes (e.g., neutrophils, CL:0000096): G6PD-dependent NADPH can modulate oxidative burst; severe deficiency can impair host defense (supportive background) (URL: https://doi.org/10.3390/cells11193041) (garciadominguez2022glucose6pdehydrogenase—an pages 5-6).

- Anatomical Locations (UBERON)
  - Blood (UBERON:0000178): Intravascular hemolysis, circulating RBCs (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).
  - Spleen (UBERON:0002106): Extravascular culling of damaged RBCs (URL: https://doi.org/10.4314/sokjmls.v10i1.35) (kwaifa2025pathophysiologyandcurrent pages 1-2).
  - Liver (UBERON:0002107): Bilirubin conjugation/excretion relevant to neonatal hyperbilirubinemia (URL: https://doi.org/10.5195/ijms.2020.637) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).

3) Biological Processes (GO annotations)
- Pentose-phosphate shunt, oxidative branch (GO:0006098): Diminished flux due to G6PD deficiency (URLs: https://doi.org/10.1155/2021/5529256; https://doi.org/10.3390/biom13081262) (dore2021thecontroversialrole pages 1-2, orrico2023oxidativestressin pages 10-11).
- NADPH regeneration (GO:0006739): Reduced capacity in RBCs (URL: https://doi.org/10.1016/j.tips.2021.07.002) (garcia2021treatmentstrategiesfor pages 1-2).
- Glutathione metabolic process (GO:0006749) and response to oxidative stress (GO:0006979): Impaired GSH homeostasis increases susceptibility to ROS-mediated RBC injury (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.4314/sokjmls.v10i1.35) (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2).
- Hemolysis (GO:0002937): Triggered by oxidant stress in G6PD-deficient RBCs (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).

4) Cellular Components
- Cytosol: PPP enzymes and GSH/GSSG cycling occur in the RBC cytosol (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).
- RBC membrane/cytoskeleton: Oxidative damage to spectrin/ankyrin and band 3 promotes rigidity and splenic sequestration (URL: https://doi.org/10.4314/sokjmls.v10i1.35) (kwaifa2025pathophysiologyandcurrent pages 1-2).
- Heinz bodies (inclusions): Oxidized hemoglobin precipitates attached to the inner membrane (URL: https://doi.org/10.4314/sokjmls.v10i1.35) (kwaifa2025pathophysiologyandcurrent pages 1-2).

5) Disease Progression
- Initial trigger: exposure to oxidant drug (e.g., primaquine, sulfonamides, dapsone), intercurrent infection (inflammation-driven ROS), or fava bean ingestion (vicine/divicine) increases oxidant burden (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).
- Molecular defect: limited PPP flux reduces NADPH; GSH/GSSG ratio declines; peroxides accumulate (URLs: https://doi.org/10.1155/2021/5529256; https://doi.org/10.3390/biom13081262) (dore2021thecontroversialrole pages 1-2, orrico2023oxidativestressin pages 10-11).
- Cellular injury: hemoglobin denaturation (Heinz bodies), membrane lipid peroxidation, band 3 clustering; decreased deformability (URL: https://doi.org/10.4314/sokjmls.v10i1.35) (kwaifa2025pathophysiologyandcurrent pages 1-2).
- Clinical hemolysis: intravascular and/or extravascular hemolysis with anemia, jaundice, hemoglobinuria; in neonates, rapid unconjugated hyperbilirubinemia can develop with risk for bilirubin neurotoxicity if not promptly managed (URL: https://doi.org/10.5195/ijms.2020.637) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).

6) Phenotypic Manifestations (HPO)
- Acute hemolytic anemia (HP:0001878): fatigue, pallor, tachycardia following oxidative triggers (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).
- Neonatal hyperbilirubinemia (HP:0002904) and jaundice (HP:0000952): often early, can be severe, occasionally with limited overt signs of hemolysis (URL: https://doi.org/10.5195/ijms.2020.637) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).
- Hemoglobinuria (HP:0002905) during intravascular hemolysis; splenomegaly (HP:0001744) with recurrent/extravascular hemolysis; Heinz bodies (HP:0011893) on smear (URL: https://doi.org/10.4314/sokjmls.v10i1.35) (kwaifa2025pathophysiologyandcurrent pages 1-2).

Recent developments and latest research (2023–2024 priority)
- RBC oxidative stress in health and disease (2023): Comprehensive review underscoring the central role of PPP-derived NADPH and glutathione in RBC redox control; details oxidative triggers of hemolysis in G6PD deficiency, including drugs, infections, and fava beans (URL: https://doi.org/10.3390/biom13081262, Aug 2023) (orrico2023oxidativestressin pages 10-11).
- Systems and tissue perspectives (2022–2021): Although slightly older, state-of-the-art reviews in Cells and Trends in Pharmacological Sciences integrate PPP/NADPH biochemistry with clinical G6PD phenotypes and therapeutic concepts (URLs: https://doi.org/10.3390/cells11193041, Sep 2022; https://doi.org/10.1016/j.tips.2021.07.002, Oct 2021) (garciadominguez2022glucose6pdehydrogenase—an pages 5-6, garcia2021treatmentstrategiesfor pages 1-2).

Current applications and real-world implementations
- Avoidance of oxidant drugs and triggers: Clinical management relies on patient education and screening to prevent exposure to high-risk drugs (e.g., primaquine, sulfonamides, dapsone) that precipitate hemolysis (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).
- Newborn screening and early diagnosis: Programs increasingly screen for G6PD activity to mitigate neonatal hyperbilirubinemia risk; prompt phototherapy and supportive care reduce neurotoxicity (URL: https://doi.org/10.5195/ijms.2020.637) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).
- Therapeutic concepts under evaluation: Small-molecule stabilization/activation of G6PD, augmentation of GSH pools (e.g., N-acetylcysteine), and compensatory NADPH pathways are discussed as future strategies (URL: https://doi.org/10.1016/j.tips.2021.07.002) (garcia2021treatmentstrategiesfor pages 1-2).

Expert opinions and analysis
- Consensus across recent and foundational reviews emphasizes that in RBCs, “erythrocytes rely solely on PPP-derived NADPH” and that “G6PD deficiency thus impairs GSH regeneration, reducing disposal of oxidants and predisposing to oxidative membrane damage and hemolysis.” These mechanistic insights underpin current prevention-first clinical strategies and motivate development of enzyme-stabilizing therapies (URLs: https://doi.org/10.3390/biom13081262; https://doi.org/10.1155/2021/5529256; https://doi.org/10.1016/j.tips.2021.07.002) (orrico2023oxidativestressin pages 10-11, dore2021thecontroversialrole pages 1-2, garcia2021treatmentstrategiesfor pages 1-2).

Relevant statistics and data
- Prevalence and genetics: G6PD deficiency is the most common human enzymopathy, with hundreds of variants producing a spectrum of residual activity and phenotypes; X-linked inheritance yields higher expression in males (URL: https://doi.org/10.5195/ijms.2020.637) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).
- Triggers and risk: Multiple commonly used drugs can trigger hemolysis in deficient individuals; infections and fava beans are frequent natural precipitants (URL: https://doi.org/10.3390/biom13081262) (orrico2023oxidativestressin pages 10-11).

Gene/protein annotations and ontology terms
- Gene/Protein (HGNC):
  - G6PD (HGNC:4421) (dore2021thecontroversialrole pages 1-2, orrico2023oxidativestressin pages 10-11)
  - GSR (HGNC:4635) (garcia2021treatmentstrategiesfor pages 1-2)

- Biological Process (GO):
  - GO:0006098 pentose-phosphate shunt, oxidative branch (dore2021thecontroversialrole pages 1-2, orrico2023oxidativestressin pages 10-11)
  - GO:0006739 NADPH regeneration (garcia2021treatmentstrategiesfor pages 1-2)
  - GO:0006749 glutathione metabolic process; GO:0006979 response to oxidative stress (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2)

- Cellular Component (GO/CC):
  - Cytosol; plasma membrane/cytoskeleton; Heinz body inclusion (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2)

- Cell Types (CL):
  - CL:0000232 erythrocyte; CL:0000096 neutrophil (orrico2023oxidativestressin pages 10-11, garciadominguez2022glucose6pdehydrogenase—an pages 5-6)

- Anatomical Locations (UBERON):
  - UBERON:0000178 blood; UBERON:0002106 spleen; UBERON:0002107 liver (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2, ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2)

- Chemical Entities (CHEBI):
  - CHEBI:16474 NADPH; CHEBI:16856 glutathione (GSH); CHEBI:57925 oxidized glutathione (GSSG); CHEBI:16240 hydrogen peroxide; CHEBI:8365 primaquine; CHEBI:4320 dapsone (orrico2023oxidativestressin pages 10-11, garcia2021treatmentstrategiesfor pages 1-2)

Phenotype associations (HPO)
- HP:0001878 acute hemolytic anemia; HP:0002904 neonatal hyperbilirubinemia; HP:0000952 jaundice; HP:0002905 hemoglobinuria; HP:0001744 splenomegaly; HP:0011893 Heinz bodies (orrico2023oxidativestressin pages 10-11, kwaifa2025pathophysiologyandcurrent pages 1-2, ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).

Evidence items with PMIDs/identifiers, URLs, dates
- Orrico F, et al. Oxidative Stress in Healthy and Pathological Red Blood Cells. Biomolecules. Aug 2023. URL: https://doi.org/10.3390/biom13081262 (mechanisms, triggers, RBC redox) (orrico2023oxidativestressin pages 10-11).
- Dore MP, et al. The Controversial Role of G6PD Deficiency on Cardiovascular Disease. Oxid Med Cell Longev. Apr 2021. URL: https://doi.org/10.1155/2021/5529256 (PPP/NADPH overview in G6PD) (dore2021thecontroversialrole pages 1-2).
- García-Domínguez E, et al. Glucose 6-P Dehydrogenase—Regulatory Functions. Cells. Sep 2022. URL: https://doi.org/10.3390/cells11193041 (systems implications; immune/redox) (garciadominguez2022glucose6pdehydrogenase—an pages 5-6).
- Garcia AA, et al. Treatment strategies for G6PD deficiency. Trends Pharmacol Sci. Oct 2021. URL: https://doi.org/10.1016/j.tips.2021.07.002 (therapeutic concepts; GSH/NADPH) (garcia2021treatmentstrategiesfor pages 1-2).
- Kwaifa IK, et al. Pathophysiology and current laboratory investigations. Sokoto J Med Lab Sci. Jun 2025. URL: https://doi.org/10.4314/sokjmls.v10i1.35 (mechanistic summaries; Heinz bodies, hemolysis) (kwaifa2025pathophysiologyandcurrent pages 1-2).
- Ravikumar N, Greenfield G. G6PD Deficiency: A Review. Int J Med Students. Dec 2020. URL: https://doi.org/10.5195/ijms.2020.637 (clinical overview; neonatal jaundice) (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2).

Notes on evidence strength and gaps
- Mechanistic foundations (PPP/NADPH/GSH and RBC hemolysis) are consistent across reviews. The most recent RBC-focused review (2023) supports current understanding and clinical triggers. High-quality 2023–2024 primary mechanistic studies specific to neonatal bilirubin handling in G6PD deficiency were not retrieved in the provided evidence; therefore, neonatal mechanistic details are supported primarily by clinical overviews and prior reviews.


References

1. (ravikumar2020glucose6phosphatedehydrogenasedeficiency pages 1-2): Nidhruv Ravikumar and Graeme Greenfield. Glucose-6-phosphate dehydrogenase deficiency: a review. International Journal of Medical Students, 8:281-287, Dec 2020. URL: https://doi.org/10.5195/ijms.2020.637, doi:10.5195/ijms.2020.637. This article has 12 citations.

2. (orrico2023oxidativestressin pages 10-11): Florencia Orrico, Sandrine Laurance, Ana C. Lopez, Sophie D. Lefevre, Leonor Thomson, Matias N. Möller, and Mariano A. Ostuni. Oxidative stress in healthy and pathological red blood cells. Biomolecules, 13:1262, Aug 2023. URL: https://doi.org/10.3390/biom13081262, doi:10.3390/biom13081262. This article has 120 citations and is from a poor quality or predatory journal.

3. (dore2021thecontroversialrole pages 1-2): Maria Pina Dore, Guido Parodi, Michele Portoghese, and Giovanni Mario Pes. The controversial role of glucose-6-phosphate dehydrogenase deficiency on cardiovascular disease: a narrative review. Oxidative Medicine and Cellular Longevity, Apr 2021. URL: https://doi.org/10.1155/2021/5529256, doi:10.1155/2021/5529256. This article has 47 citations and is from a poor quality or predatory journal.

4. (garcia2021treatmentstrategiesfor pages 1-2): Adriana A. Garcia, Ana Koperniku, Julio C.B. Ferreira, and Daria Mochly-Rosen. Treatment strategies for glucose-6-phosphate dehydrogenase deficiency: past and future perspectives. Trends in Pharmacological Sciences, 42:829-844, Oct 2021. URL: https://doi.org/10.1016/j.tips.2021.07.002, doi:10.1016/j.tips.2021.07.002. This article has 59 citations and is from a highest quality peer-reviewed journal.

5. (kwaifa2025pathophysiologyandcurrent pages 1-2): Ibrahim Kalle Kwaifa, Osaro Erhabor, Abdulrahman Yakubu, Aliyu Ibrahim Bagudo, Buhari Hauwa Ali, Onuigwe Festus Uchechukwu, Nura Muhammad Bunza, Mustapha Umar Kalgo, Abdullahi Isiyaku, Mukhtar Yeldu, Dahiru Isah, Moses Akila, Solomon Moses, Zainab Abubakar Ibrahim, Ukashat Almustapha, Muhammad Lubabatu Abbas, Addra Sumaiya Ibrahim, Stephen Cecilia, Ismail Usman Adenkunle, Nasiru Sadiq, and Muhammad Buhari. Pathophysiology and current laboratory investigations of glucose-6-phosphate dehydrogenase deficiency. Sokoto Journal of Medical Laboratory Science, 10:358-379, Jun 2025. URL: https://doi.org/10.4314/sokjmls.v10i1.35, doi:10.4314/sokjmls.v10i1.35. This article has 0 citations.

6. (garciadominguez2022glucose6pdehydrogenase—an pages 5-6): Esther García-Domínguez, Aitor Carretero, Aurora Viña-Almunia, Julio Domenech-Fernandez, Gloria Olaso-Gonzalez, Jose Viña, and Mari Carmen Gomez-Cabrera. Glucose 6-p dehydrogenase—an antioxidant enzyme with regulatory functions in skeletal muscle during exercise. Cells, 11:3041, Sep 2022. URL: https://doi.org/10.3390/cells11193041, doi:10.3390/cells11193041. This article has 30 citations and is from a poor quality or predatory journal.