---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T22:58:40.117415'
end_time: '2026-02-23T23:19:25.769499'
duration_seconds: 1245.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Methylmalonic Acidemia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Methylmalonic Acidemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Methylmalonic Acidemia**.
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
- **Disease Name:** Methylmalonic Acidemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Methylmalonic Acidemia**.
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


Title: Pathophysiology of Methylmalonic Acidemia (Isolated MMA / Methylmalonic Aciduria)

1. Disease definition and core concepts (current understanding)

Methylmalonic acidemia (MMA) is an inborn error of propionate metabolism in which impaired conversion of methylmalonyl‑CoA to succinyl‑CoA disrupts mitochondrial anaplerosis and leads to systemic accumulation of methylmalonic acid (MMA) and related metabolites. The canonical biochemical lesion is methylmalonyl‑CoA mutase (MMUT/MUT) deficiency, but isolated MMA can also arise from defects in adenosylcobalamin (AdoCbl) cofactor synthesis/handling (cblA/cblB) and other related genes depending on classification scheme. (head2023newinsightsinto pages 1-3, manoli2023biomarkerstopredict pages 15-16, tejero2024methylmalonicacidin pages 3-4)

A concise systems-level schematic of dysregulated pathways in MMA—MMUT block, metabolite accumulation, downstream TCA/ETC/urea-cycle effects, and aberrant acylation regulated by mitochondrial sirtuins—is provided in Figure 5 of Head et al. 2023. (head2023newinsightsinto media 2be035c5)

Scope note: This report focuses on isolated MMA (mut/MMUT; cblA/MMAA; cblB/MMAB) but includes mechanistic insights that overlap with related cobalamin and mitochondrial disorders when explicitly supported by the retrieved sources.

2. Core pathophysiology: dysregulated pathways and affected cellular processes

2.1 Metabolite accumulation and mitochondrial energetic failure

Primary accumulated/toxic metabolites reported across recent reviews include: MMA, methylmalonyl‑CoA, propionyl‑CoA, 2‑methylcitrate, 3‑hydroxypropionate, propionyl‑carnitine (C3), and ammonia; these occur together with reduced succinyl‑CoA production (loss of anaplerotic input into the TCA cycle). (tejero2024methylmalonicacidin pages 3-4, head2023newinsightsinto pages 3-4, manoli2023biomarkerstopredict pages 17-21)

Mechanistically, multiple sources emphasize direct and indirect inhibition of mitochondrial enzymes/respiratory chain components by MMA and related metabolites. Head et al. (2023) describe inhibition of succinate dehydrogenase (SDH/Complex II) and respiratory complexes including Complex I and Complex II+III, along with inhibition of β‑hydroxybutyrate dehydrogenase (HBDH), mitochondrial creatine kinase, and lactate dehydrogenase—collectively consistent with impaired oxidative metabolism and ATP depletion. (head2023newinsightsinto pages 3-4, head2023newinsightsinto pages 12-13)

Tejero et al. (2024) further summarize that MMA competitively inhibits SDH (Complex II) and also inhibits Complex I, and report reduced abundance of multiple TCA enzymes (e.g., 2‑oxoglutarate dehydrogenase, fumarate hydratase, malate dehydrogenase) in disease models, supporting broad mitochondrial/TCA dysfunction. (tejero2024methylmalonicacidin pages 3-4)

2.2 Hyperammonemia via urea-cycle disruption

A key mechanistic connection between propionate-pathway dysfunction and hyperammonemia is inhibition of N‑acetylglutamate synthetase (NAGS) by propionyl‑CoA, which reduces activation of the urea cycle. Head et al. (2023) also link 2‑methylcitrate exposure to ammonium accumulation and report cerebral ammonium accumulation in brain-specific Mut−/− models. (head2023newinsightsinto pages 12-13)

2.3 Aberrant mitochondrial protein acylation/methylmalonylation (a recent conceptual advance)

A major 2023 mechanistic theme is that MMA is not only a “metabolite toxicity” disorder but also a disorder of mitochondrial protein hyperacylation. Head et al. (2023) describe increased pools of malonyl‑, propionyl‑, and methylmalonyl‑CoA driving widespread malonylation/propionylation/methylmalonylation of mitochondrial proteins across pathways including TCA cycle, β‑oxidation, amino acid metabolism, urea cycle, glutathione/oxidative-stress pathways, and mitochondrial DNA maintenance. (head2023newinsightsinto pages 7-9)

This conceptual framework also highlights reduced levels of mitochondrial sirtuins (SIRT3/4/5) in MMA tissues and the role of SIRT5 as a demalonylase/desuccinylase that can also remove methylmalonylation, suggesting that impaired deacylation may amplify dysfunction. (head2023newinsightsinto pages 7-9)

2.4 Mitochondrial quality control failure (mitophagy), and lysosome/autophagy dysfunction

Mitochondrial dysfunction in MMA is increasingly linked to impaired mitochondrial quality control.

Renal epithelial models (2023): In patient-derived renal epithelial cells, Schumann et al. (2023) report mitophagy impairment (PINK1 down to ~0.7-fold at baseline and further suppressed under metabolic stress), a shift toward mitochondrial fission (DRP1 up to 4.3-fold under high-protein load; OPA1 down to 0.2-fold under high-protein load), and increased bulk autophagy marker SQSTM1, consistent with altered mitochondrial turnover and stress vulnerability. (schumann2023theimpactof pages 4-5, schumann2023theimpactof pages 8-8)

Fibroblast and engineered models (2024): Costanzo et al. (2024) provide direct evidence that MUT deficiency causes lysosomal/autophagy dysfunction, including enlarged LAMP1+ lysosomes, reduced autophagosome–lysosome fusion, reduced lysosomal acidity and degradative function, and severely reduced autophagic flux. They explicitly state: “Lysosomes of MMA cells present as enlarged vacuoles with low degradative capabilities.” (costanzo2024methylmalonicacidemiatriggers pages 1-2)

Quantitatively, Costanzo et al. report autophagic flux (J) of 0.96 in controls versus J < 0.1 in MUT-deficient lines, impaired LysoTracker signal (reduced lysosomal acidity), and impaired EGFR degradation kinetics. (costanzo2024methylmalonicacidemiatriggers pages 7-10)

Importantly, these lysosomal defects were pharmacologically reversible: treatment with 2,2-dimethylbutanoic acid (DMBA; also referred to as an anti-propionigenic approach related to HST5040 development) rescued lysosomal morphology and function and improved degradative capacity in MUT-deficient cells. (costanzo2024methylmalonicacidemiatriggers pages 12-14, costanzo2024methylmalonicacidemiatriggers pages 10-12)

2.5 Oxidative stress and redox imbalance

Multiple sources connect MMA to oxidative stress. Head et al. (2023) discuss free-radical generation and oxidative stress–linked neurotoxicity (e.g., glial activation, seizures) in experimental systems. (head2023newinsightsinto pages 3-4, head2023newinsightsinto pages 12-13)

In kidney models, Schumann et al. (2023) report compromised antioxidant defenses and a lowered reduced:oxidized glutathione ratio under high-protein or isoleucine/valine exposure, consistent with increased oxidative stress under metabolic stressors relevant to MMA. (schumann2023theimpactof pages 5-6, schumann2023theimpactof pages 6-8)

2.6 ER stress, Ca2+ dysregulation, and impaired selective autophagy (hepatocyte evidence)

A hepatocyte model reported in a 2023 preprint (Research Square) links high MMA exposure to ER stress (IRE1α–XBP1 activation), disrupted Ca2+ handling, inhibited ER-phagy (via downregulation of FAM134B), and inhibited mitophagy (mt‑Keima evidence of reduced mitochondria entering lysosomes), providing a mechanistic hypothesis for hepatocyte injury that integrates ER stress and mitochondrial quality control defects. (zhang2023transcriptomeanalysisreveals pages 7-10)

3. Key molecular players (genes/proteins, chemicals, cells, anatomy)

3.1 Genes/proteins (HGNC-style entities)

Causal/primary genes for isolated MMA in recent reviews:

• MMUT (MUT; methylmalonyl‑CoA mutase): defines mut0 (non–B12 responsive) and mut− (partial/B12 responsive) phenotypes. (tejero2024methylmalonicacidin pages 3-4)
• MMAA (cblA) and MMAB (cblB): genes required for AdoCbl cofactor formation/handling for MUT activity; Manoli et al. (2023) explicitly link cblA to MMAA and cblB to MMAB. (manoli2023biomarkerstopredict pages 15-16)

Additional genes listed in a 2024 expert review as implicated in MMAemia phenotypes (may include broader/related MMA biology and specific subclasses): MMADHC, MCEE, SUCLG1, SUCLA2. (tejero2024methylmalonicacidin pages 3-4)

Mitochondrial protein deacylation/quality control regulators implicated:

• SIRT3, SIRT4, SIRT5: reduced protein levels in MMA tissues; SIRT5 can remove methylmalonylation and other negatively charged acylations. (head2023newinsightsinto pages 7-9)
• PINK1 (mitophagy priming) and DRP1/OPA1 (fission/fusion) in renal epithelial MMA models. (schumann2023theimpactof pages 4-5)
• LAMP1/LAMP2 (lysosomal membrane proteins), TFEB (lysosomal biogenesis regulator), LC3 and p62/SQSTM1 (autophagy markers) in MUT-deficient cells. (costanzo2024methylmalonicacidemiatriggers pages 5-7, costanzo2024methylmalonicacidemiatriggers pages 10-12)

3.2 Chemical entities / metabolites (CHEBI-style entities)

Key metabolites and biomarkers reported across sources:

• Methylmalonic acid; methylmalonyl‑CoA; propionyl‑CoA; 2‑methylcitrate; 3‑hydroxypropionate; propionyl‑carnitine (C3); ammonia. (tejero2024methylmalonicacidin pages 3-4, manoli2023biomarkerstopredict pages 17-21, head2023newinsightsinto pages 12-13)
• Methylcitrate-to-citrate ratio and methylcitrate as biomarkers in blood spots/clinical monitoring contexts. (head2023newinsightsinto pages 12-13)
• Mitochondrial stress/organ injury biomarkers: FGF21, GDF15 (mitochondrial stress), LCN2 (kidney injury marker). (manoli2023biomarkerstopredict pages 9-10, manoli2023biomarkerstopredict pages 10-12)

Reference-level statistic: normal blood MMA levels are reported as <270 nmol/L (general clinical reference, not MMAemia-specific); this is relevant for conceptualizing “supraphysiologic” elevations in disease. (tejero2024methylmalonicacidin pages 3-4)

3.3 Cell types (CL-style) and anatomy (UBERON-style)

Organ systems and cell types repeatedly implicated:

• Liver/hepatocytes: central to propionate metabolism and targeted for liver-directed therapies; hepatomegaly/steatosis and mitochondrial ultrastructural abnormalities are described in clinical biomarker reviews. (manoli2023biomarkerstopredict pages 10-12, manoli2023biomarkerstopredict pages 12-13)
• Kidney/renal proximal tubular epithelial cells: chronic kidney disease is a key long-term complication; proximal tubular mitochondrial dysfunction, oxidative stress, and mitophagy defects are implicated. (manoli2023biomarkerstopredict pages 10-12, schumann2023theimpactof pages 4-5)
• Brain/CNS (neurons and glia; basal ganglia/striatum): neurotoxicity with oxidative stress, glial activation, and seizures described in metabolite exposure and model systems. (head2023newinsightsinto pages 12-13)
• Heart/cardiomyocytes: cardiomyopathy and QT prolongation occur in a subset of organic aciduria patients (including MMA). (passantino2023cardiacinvolvementin pages 1-2, passantino2023cardiacinvolvementin pages 6-8)
• Adipose tissue (white and brown adipocytes): a 2024 JCI Insight study describes a distinct adipose distribution and “beiging” phenotype with metabolic stress markers and methylmalonylation in adipose. (manoli2024lipodystrophyinmethylmalonic pages 2-4, manoli2024lipodystrophyinmethylmalonic pages 10-11)

4. Biological processes and cellular components (GO-oriented annotation candidates)

The following GO Biological Process (BP) candidates are directly motivated by mechanisms described in the cited sources:

• Propionate metabolic process / methylmalonyl‑CoA metabolic process (MMUT block; MMAA/MMAB involvement). (tejero2024methylmalonicacidin pages 3-4, manoli2023biomarkerstopredict pages 15-16)
• Tricarboxylic acid cycle and anaplerotic processes (loss of succinyl‑CoA; TCA rewiring; reduced TCA enzyme abundance). (tejero2024methylmalonicacidin pages 3-4, head2023newinsightsinto pages 12-13)
• Mitochondrial electron transport / oxidative phosphorylation (Complex I/II inhibition; respiratory chain impairment). (head2023newinsightsinto pages 3-4, tejero2024methylmalonicacidin pages 3-4)
• Urea cycle and ammonia detoxification (NAGS inhibition; ammonia accumulation). (head2023newinsightsinto pages 12-13)
• Protein acylation (including lysine methylmalonylation/malonylation/propionylation) and protein deacylation (sirtuin-regulated). (head2023newinsightsinto pages 7-9)
• Mitophagy and macroautophagy, including autophagosome–lysosome fusion and lysosomal acidification/degradative function. (costanzo2024methylmalonicacidemiatriggers pages 7-10, schumann2023theimpactof pages 4-5)
• Cellular oxidant detoxification / glutathione metabolism and oxidative stress response. (schumann2023theimpactof pages 6-8, head2023newinsightsinto pages 3-4)
• Endoplasmic reticulum stress / unfolded protein response (IRE1α–XBP1) and selective ER-phagy (hepatocyte model evidence). (zhang2023transcriptomeanalysisreveals pages 7-10)

GO Cellular Component (CC) candidates:

• Mitochondrial matrix and mitochondrial inner membrane (MMUT, TCA enzymes, ETC complexes; sirtuins; respiratory chain inhibition). (tejero2024methylmalonicacidin pages 3-4, head2023newinsightsinto pages 7-9)
• Lysosome and autophagosome (LAMP1/2 changes; LC3/p62 accumulation; reduced fusion and acidity). (costanzo2024methylmalonicacidemiatriggers pages 12-14, costanzo2024methylmalonicacidemiatriggers pages 5-7)
• Endoplasmic reticulum (ER stress and ER-phagy findings in hepatocyte model). (zhang2023transcriptomeanalysisreveals pages 7-10)

5. Disease progression model (sequence of events)

A mechanistic sequence consistent with current evidence:

(1) Genetic lesion (MMUT; MMAA; MMAB; other listed genes) → impaired conversion of methylmalonyl‑CoA to succinyl‑CoA. (tejero2024methylmalonicacidin pages 3-4, manoli2023biomarkerstopredict pages 15-16)

(2) Metabolite accumulation (MMA, methylmalonyl‑CoA, propionyl‑CoA, methylcitrate, etc.) plus anaplerotic deficit (low succinyl‑CoA input). (tejero2024methylmalonicacidin pages 3-4, head2023newinsightsinto pages 3-4)

(3) Mitochondrial dysfunction via (i) direct inhibition of respiratory/TCA enzymes and (ii) widespread hyperacylation/methylmalonylation of mitochondrial proteins, with reduced sirtuin deacylation capacity, leading to multi-pathway enzymatic impairment. (head2023newinsightsinto pages 3-4, head2023newinsightsinto pages 7-9)

(4) Secondary stress responses (oxidative stress; hyperammonemia; metabolic inflexibility), and failure of mitochondrial quality control (impaired mitophagy; altered fission/fusion). (head2023newinsightsinto pages 12-13, schumann2023theimpactof pages 4-5)

(5) Downstream organelle homeostasis failure: lysosomal/autophagy system dysfunction (reduced autophagic flux, reduced lysosomal acidity/degradation, impaired autophagosome–lysosome fusion), which can further amplify mitochondrial dysfunction by preventing clearance of damaged organelles. (costanzo2024methylmalonicacidemiatriggers pages 7-10, costanzo2024methylmalonicacidemiatriggers pages 12-14)

(6) Organ-specific injury phenotypes emerge over time (CKD, cardiomyopathy/QT issues, neurodevelopmental injury, adipose remodeling), influenced by metabolic stressors and disease severity. (manoli2023biomarkerstopredict pages 9-10, passantino2023cardiacinvolvementin pages 1-2, manoli2024lipodystrophyinmethylmalonic pages 2-4)

6. Phenotypic manifestations and mechanistic links (HP-style concepts)

Kidney disease: Chronic kidney disease is a major long-term complication and is mechanistically linked to proximal tubular mitochondrial dysfunction, oxidative stress, and altered mitophagy/dynamics. LCN2 (lipocalin-2) is highlighted as a kidney injury biomarker linked to proximal tubule mitochondrial dysfunction and oxidative stress in MMA models. (manoli2023biomarkerstopredict pages 10-12, schumann2023theimpactof pages 4-5)

Neurologic injury: Experimental evidence links methylmalonate and methylcitrate exposure to oxidative stress, inflammation, glial activation, and seizure-related phenotypes; ammonia may potentiate oxidative damage and seizures. (head2023newinsightsinto pages 12-13)

Cardiac involvement: In a 2000–2022 pediatric cohort of classical organic acidurias (including MMA; combined MMA with homocystinuria excluded), cardiac involvement occurred in 23/60 (~38%) and was confined to PA and MMA; dilated cardiomyopathy was predominant and long-QT was observed in a subset. Five-year MACE rates were 35% for MMA with cardiomyopathy and 23% for MMA without cardiomyopathy. (passantino2023cardiacinvolvementin pages 1-2)

Adipose/lipodystrophy-like phenotype: A distinct pattern of subcutaneous fat distribution and beiging markers is reported in MMA and associated with elevated FGF21 and abnormal adipose methylmalonylation. In 46 MMA patients vs 99 controls, subtotal fat mass % was higher (30.9% ± 10.5% vs 26.5% ± 9.8%, P=0.0147). (manoli2024lipodystrophyinmethylmalonic pages 2-4)

7. Recent developments (2023–2024) and real-world implementations

7.1 Newborn screening and prognosis (2024, large real-world cohort)

A 2024 multicenter Chinese cohort compared mut-type MMA detected by newborn screening (NBS) (n=168) vs clinically diagnosed after symptom onset (n=210). Key outcome statistics:

• Mortality: 12.5% (21/168) in NBS-detected vs 32.7% (69/210) in clinically diagnosed. (ling2024clinicaloutcomesof pages 5-6, ling2024clinicaloutcomesof pages 4-5)
• Outcomes: normal outcome 51.79% (87/168) in NBS vs 15.71% (33/210) clinically; poor outcomes 43.45% vs 78.57%. (ling2024clinicaloutcomesof pages 5-6)
• Biochemistry (examples): baseline blood C3 median 7.88 vs 11.49 μmol/L; baseline C3/C2 0.58 vs 0.72; urinary MMA 160.9 vs 366 mmol/mol Cr (NBS vs clinical). (ling2024clinicaloutcomesof pages 5-6)
• Vitamin B12 responsiveness: 54.76% (92/168) in NBS vs 33.33% (70/210) clinical. (ling2024clinicaloutcomesof pages 5-6)

This supports NBS as an implementation that can shift disease course by enabling earlier therapy and reducing metabolic crises and mortality. (ling2024clinicaloutcomesof pages 6-8, ling2024clinicaloutcomesof pages 5-6)

7.2 Biomarkers for severity and therapeutic monitoring (2023)

Manoli et al. (2023) emphasize FGF21 and GDF15 as mitochondrial stress biomarkers in MMA, with FGF21 correlating with disease severity and complications attributed to mitochondrial dysfunction (e.g., renal failure, optic neuropathy, cardiomyopathy) and responding to liver-targeted therapies/transplantation. (manoli2023biomarkerstopredict pages 9-10)

The same review highlights LCN2 as a renal injury biomarker tied to proximal tubule mitochondrial dysfunction and oxidative stress, with preclinical evidence that Lcn2 can rise earlier and be more sensitive than creatinine or serum MMA in therapeutic contexts. (manoli2023biomarkerstopredict pages 10-12)

7.3 Therapeutic development and clinical trial landscape (ClinicalTrials.gov; accessed via retrieved records)

mRNA replacement therapy (mRNA‑3705, Moderna) for MUT deficiency:

• NCT04899310 (posted record year 2021): Phase 1/2; status ACTIVE_NOT_RECRUITING; estimated enrollment 74. Intervention is IV infusion of a modified mRNA encoding human methylmalonyl‑CoA mutase, dosed Q2W or Q3W in Part 1 for up to 10 doses. Primary endpoints include safety (TEAEs/AESIs/SAEs) for Parts 1 and 3 and % change in plasma MMA at Month 3 for Part 2. (NCT04899310 chunk 1)
• NCT05295433: Phase 1/2 open-label extension; status RECRUITING; estimated enrollment 56. Secondary endpoints include % change in plasma MMA and 2‑methylcitric acid (2‑MC), annualized metabolic decompensation event rates, and healthcare utilization, among others. (NCT05295433 chunk 1)

Liver-targeted AAV genome integration approach (hLB‑001; LK03 capsid; SUNRISE study):

• NCT04581785: Phase 1/2 open-label; status TERMINATED; actual enrollment 4; termination reason “Due to low likelihood of clinical benefit in treated participants.” The intervention is an IV infusion of a liver-targeted engineered rAAV (LK03 capsid) designed to integrate human MMUT at the albumin locus. Primary outcomes are safety-focused (TEAEs; infusion toxicities) through Week 52. (NCT04581785 chunk 1)

Anti-propionigenic/small-molecule approach (HST5040):

• NCT04732429: Phase 2; status TERMINATED; actual enrollment 26; termination due to sponsor business considerations. Primary endpoint: change in plasma 2‑methylcitric acid (MCA) over 6 months. Secondary endpoints include changes in C3, C3:C2 ratio, 3‑OH propionate, MMA (in MMA subjects), ammonia, and acute metabolic decompensation frequency, among others. (NCT04732429 chunk 1)

Mechanistic bridge to lysosomal rescue: In MUT-deficient cells, DMBA (2,2-dimethylbutanoic acid) rescued lysosomal morphology, acidity (LysoTracker), and degradative function, providing a mechanistic rationale for targeting downstream cellular homeostasis in addition to metabolite lowering. (costanzo2024methylmalonicacidemiatriggers pages 12-14)

7.4 Adjunct mitochondrial/metabolic modulation (2024 mechanistic phenotype study)

A 2024 JCI Insight study identifies a lipodystrophy-like phenotype in MMA and links it to elevated FGF21, acyl-CoA accretion, and aberrant methylmalonylation in adipose tissue. In a liver-rescued MMA mouse model, bezafibrate treatment increased Ucp1 expression, improved survival (P=0.009), and partially rescued GFR (42.14% ± 3.35% → 61.29% ± 7.24%, P=0.02), suggesting that modulating mitochondrial/adipose programs can alter systemic phenotypes in MMA models. (manoli2024lipodystrophyinmethylmalonic pages 10-11)

8. Expert synthesis and analysis (authoritative interpretations anchored to cited sources)

The 2023–2024 literature supports a “multi-hit” pathophysiology in which (i) anaplerotic deficit and metabolite accumulation, (ii) mitochondrial enzyme/ETC inhibition, (iii) mitochondrial protein hyperacylation/methylmalonylation with impaired deacylation, and (iv) organelle quality-control failure (mitophagy plus lysosome/autophagy dysfunction) together drive progressive multiorgan pathology. This integrated view is explicitly emphasized in the 2023 JIMD review, which reframes MMA around aberrant post-translational modifications and mitochondrial sirtuin biology as potentially actionable mechanisms. (head2023newinsightsinto pages 7-9)

In parallel, the 2024 Cell & Bioscience study adds a new mechanistic layer by showing that MUT deficiency directly perturbs the lysosome–autophagy system and that these defects are pharmacologically reversible, strengthening the hypothesis that “downstream” cell-biological dysfunctions contribute materially to disease progression beyond metabolite accumulation alone. (costanzo2024methylmalonicacidemiatriggers pages 12-14, costanzo2024methylmalonicacidemiatriggers pages 7-10)

Finally, biomarker-focused 2023 work supports the view that mitochondrial stress readouts (FGF21/GDF15) and kidney injury markers (LCN2) can serve as nearer-term pharmacodynamic endpoints than classic metabolites alone, which are confounded by diet and renal function, and are therefore central to trial design and precision stratification in emerging therapies. (manoli2023biomarkerstopredict pages 9-10, manoli2023biomarkerstopredict pages 10-12)

9. Knowledge-base style annotation blocks

9.1 Pathophysiology (narrative)

Isolated MMA arises from defects in mitochondrial MMUT or its AdoCbl cofactor synthesis/handling (MMAA/MMAB), causing accumulation of MMA-related metabolites and loss of succinyl‑CoA production. Accumulated MMA/methylcitrate/propionyl-CoA disrupt mitochondrial metabolism via inhibition of respiratory chain complexes (Complex I; Complex II/SDH) and multiple dehydrogenases, and by driving widespread mitochondrial protein lysine hyperacylation/methylmalonylation. Reduced mitochondrial sirtuins (SIRT3/4/5) and impaired deacylation capacity may amplify dysfunction. Mitochondrial quality control is impaired (reduced PINK1-dependent priming; altered fission/fusion), and new evidence demonstrates lysosomal/autophagy system failure (reduced lysosomal acidity, reduced autophagosome–lysosome fusion, low autophagic flux) that is reversible by an anti-propionigenic small molecule (DMBA). These combined mechanisms produce multi-organ disease dominated by renal proximal tubule injury/CKD, neurologic injury (oxidative stress/glial activation and metabolic stroke risk), cardiac involvement (cardiomyopathy/QT issues), and systemic metabolic stress phenotypes including altered adipose remodeling. (tejero2024methylmalonicacidin pages 3-4, head2023newinsightsinto pages 3-4, head2023newinsightsinto pages 7-9, schumann2023theimpactof pages 4-5, costanzo2024methylmalonicacidemiatriggers pages 12-14)

9.2 Gene/protein annotations (examples)

• MMUT (methylmalonyl‑CoA mutase): mitochondrial anaplerotic enzyme; loss causes mut0/mut− isolated MMA. (tejero2024methylmalonicacidin pages 3-4)
• MMAA (cblA): AdoCbl cofactor handling for MMUT. (manoli2023biomarkerstopredict pages 15-16)
• MMAB (cblB): cob(I)alamin adenosyltransferase activity; AdoCbl formation. (manoli2023biomarkerstopredict pages 15-16)
• SIRT5 (mitochondrial deacylase): removes methylmalonylation; reduced protein levels in MMA liver; implicated in hyperacylation state. (head2023newinsightsinto pages 7-9)
• PINK1 / DRP1 / OPA1 (mitochondrial quality control and dynamics): altered in renal epithelial MMA models under metabolic stress. (schumann2023theimpactof pages 4-5)

9.3 Phenotype associations (HP-style concepts; examples)

• Metabolic acidosis/metabolic decompensation crises; hyperammonemia (urea-cycle impairment). (head2023newinsightsinto pages 12-13)
• Chronic kidney disease / proximal tubular dysfunction. (manoli2023biomarkerstopredict pages 10-12, schumann2023theimpactof pages 4-5)
• Dilated cardiomyopathy; acquired long QT. (passantino2023cardiacinvolvementin pages 1-2, passantino2023cardiacinvolvementin pages 6-8)
• Neurodevelopmental impairment, seizures/metabolic stroke risk (mechanistically linked to oxidative stress and ammonia). (head2023newinsightsinto pages 12-13)
• Abnormal adipose distribution / lipodystrophy-like phenotype; altered thermogenesis and “beiging.” (manoli2024lipodystrophyinmethylmalonic pages 2-4, manoli2024lipodystrophyinmethylmalonic pages 10-11)

9.4 Cell types and anatomical locations (CL/UBERON-style; examples)

• Hepatocyte / liver: central metabolic organ and therapeutic target. (manoli2023biomarkerstopredict pages 10-12)
• Renal proximal tubule epithelial cell / kidney cortex: CKD driver; mitochondrial stress and mitophagy defects. (manoli2023biomarkerstopredict pages 10-12, schumann2023theimpactof pages 4-5)
• Neuron and glial cell / basal ganglia (striatum, globus pallidus as referenced by review): vulnerable to metabolite/ammonia-driven oxidative injury. (head2023newinsightsinto pages 12-13)
• Cardiomyocyte / heart ventricle: cardiomyopathy phenotype in OA cohorts. (passantino2023cardiacinvolvementin pages 1-2)
• White and brown adipocyte / subcutaneous adipose tissue and BAT depots: beiging and thermogenic dysfunction. (manoli2024lipodystrophyinmethylmalonic pages 10-11, manoli2024lipodystrophyinmethylmalonic pages 2-4)

9.5 Cellular components (subcellular localization)

• Mitochondrial matrix and inner membrane (MMUT; TCA/ETC; sirtuins; respiratory chain targets). (tejero2024methylmalonicacidin pages 3-4, head2023newinsightsinto pages 7-9)
• Lysosome and autophagosome (LAMP1/2, LC3/p62; fusion; acidification). (costanzo2024methylmalonicacidemiatriggers pages 12-14, costanzo2024methylmalonicacidemiatriggers pages 7-10)
• Endoplasmic reticulum (ER stress/UPR; ER-phagy evidence in hepatocyte model). (zhang2023transcriptomeanalysisreveals pages 7-10)

10. Evidence items (PMID/URL notes)

The retrieved texts provide stable DOIs/URLs and ClinicalTrials.gov identifiers; PubMed IDs (PMIDs) were not present in the extracted evidence snippets and therefore are not asserted here.

Key peer-reviewed sources (publication date; URL):

• Head et al. “New insights into the pathophysiology of methylmalonic acidemia.” Journal of Inherited Metabolic Disease. May 2023. https://doi.org/10.1002/jimd.12617 (head2023newinsightsinto pages 1-3, head2023newinsightsinto pages 3-4)
• Manoli et al. “Biomarkers to predict disease progression and therapeutic response in isolated methylmalonic acidemia.” Journal of Inherited Metabolic Disease. Jun 2023. https://doi.org/10.1002/jimd.12636 (manoli2023biomarkerstopredict pages 9-10, manoli2023biomarkerstopredict pages 10-12)
• Costanzo et al. “Methylmalonic acidemia triggers lysosomal-autophagy dysfunctions.” Cell & Bioscience. May 2024. https://doi.org/10.1186/s13578-024-01245-1 (costanzo2024methylmalonicacidemiatriggers pages 7-10, costanzo2024methylmalonicacidemiatriggers pages 1-2)
• Tejero et al. “Methylmalonic acid in aging and disease.” Trends in Endocrinology & Metabolism. Mar 2024. https://doi.org/10.1016/j.tem.2023.11.001 (tejero2024methylmalonicacidin pages 3-4)
• Schumann et al. “The impact of metabolic stressors on mitochondrial homeostasis in a renal epithelial cell model of methylmalonic aciduria.” Scientific Reports. May 2023. https://doi.org/10.1038/s41598-023-34373-8 (schumann2023theimpactof pages 4-5, schumann2023theimpactof pages 6-8)
• Manoli et al. “Lipodystrophy in methylmalonic acidemia associated with elevated FGF21 and abnormal methylmalonylation.” JCI Insight. Feb 2024. https://doi.org/10.1172/jci.insight.174097 (manoli2024lipodystrophyinmethylmalonic pages 2-4, manoli2024lipodystrophyinmethylmalonic pages 10-11)
• Ling et al. “Clinical outcomes of patients with mut-type methylmalonic acidemia identified through expanded newborn screening in China.” Human Genomics. Jul 2024. https://doi.org/10.1186/s40246-024-00646-0 (ling2024clinicaloutcomesof pages 5-6, ling2024clinicaloutcomesof pages 4-5)
• Passantino et al. “Cardiac involvement in classical organic acidurias: clinical profile and outcome in a pediatric cohort.” Diagnostics. Dec 2023. https://doi.org/10.3390/diagnostics13243674 (passantino2023cardiacinvolvementin pages 1-2, passantino2023cardiacinvolvementin pages 6-8)

Selected ClinicalTrials.gov records:

• NCT04899310 (mRNA‑3705). Phase 1/2. ACTIVE_NOT_RECRUITING. Estimated enrollment 74. (NCT04899310 chunk 1)
• NCT05295433 (mRNA‑3705 extension). Phase 1/2. RECRUITING. Estimated enrollment 56. (NCT05295433 chunk 1)
• NCT04581785 (hLB‑001 AAV LK03 albumin-locus integration). Phase 1/2. TERMINATED. Enrollment 4. (NCT04581785 chunk 1)
• NCT04732429 (HST5040). Phase 2. TERMINATED. Enrollment 26. (NCT04732429 chunk 1)

End of report.

References

1. (head2023newinsightsinto pages 1-3): PamelaSara E. Head, Jordan L. Meier, and Charles P. Venditti. New insights into the pathophysiology of methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:436-449, May 2023. URL: https://doi.org/10.1002/jimd.12617, doi:10.1002/jimd.12617. This article has 38 citations and is from a peer-reviewed journal.

2. (manoli2023biomarkerstopredict pages 15-16): Irini Manoli, Abigael Gebremariam, Samantha McCoy, Alexandra R. Pass, Jack Gagné, Camryn Hall, Susan Ferry, Carol Van Ryzin, Jennifer L. Sloan, Elisa Sacchetti, Giulio Catesini, Cristiano Rizzo, Diego Martinelli, Marco Spada, Carlo Dionisi‐Vici, and Charles P. Venditti. Biomarkers to predict disease progression and therapeutic response in isolated methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:554-572, Jun 2023. URL: https://doi.org/10.1002/jimd.12636, doi:10.1002/jimd.12636. This article has 28 citations and is from a peer-reviewed journal.

3. (tejero2024methylmalonicacidin pages 3-4): Joanne D Tejero, Felicia Lazure, and Ana P Gomes. Methylmalonic acid in aging and disease. Trends in Endocrinology &amp; Metabolism, 35:188-200, Mar 2024. URL: https://doi.org/10.1016/j.tem.2023.11.001, doi:10.1016/j.tem.2023.11.001. This article has 43 citations and is from a domain leading peer-reviewed journal.

4. (head2023newinsightsinto media 2be035c5): PamelaSara E. Head, Jordan L. Meier, and Charles P. Venditti. New insights into the pathophysiology of methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:436-449, May 2023. URL: https://doi.org/10.1002/jimd.12617, doi:10.1002/jimd.12617. This article has 38 citations and is from a peer-reviewed journal.

5. (head2023newinsightsinto pages 3-4): PamelaSara E. Head, Jordan L. Meier, and Charles P. Venditti. New insights into the pathophysiology of methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:436-449, May 2023. URL: https://doi.org/10.1002/jimd.12617, doi:10.1002/jimd.12617. This article has 38 citations and is from a peer-reviewed journal.

6. (manoli2023biomarkerstopredict pages 17-21): Irini Manoli, Abigael Gebremariam, Samantha McCoy, Alexandra R. Pass, Jack Gagné, Camryn Hall, Susan Ferry, Carol Van Ryzin, Jennifer L. Sloan, Elisa Sacchetti, Giulio Catesini, Cristiano Rizzo, Diego Martinelli, Marco Spada, Carlo Dionisi‐Vici, and Charles P. Venditti. Biomarkers to predict disease progression and therapeutic response in isolated methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:554-572, Jun 2023. URL: https://doi.org/10.1002/jimd.12636, doi:10.1002/jimd.12636. This article has 28 citations and is from a peer-reviewed journal.

7. (head2023newinsightsinto pages 12-13): PamelaSara E. Head, Jordan L. Meier, and Charles P. Venditti. New insights into the pathophysiology of methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:436-449, May 2023. URL: https://doi.org/10.1002/jimd.12617, doi:10.1002/jimd.12617. This article has 38 citations and is from a peer-reviewed journal.

8. (head2023newinsightsinto pages 7-9): PamelaSara E. Head, Jordan L. Meier, and Charles P. Venditti. New insights into the pathophysiology of methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:436-449, May 2023. URL: https://doi.org/10.1002/jimd.12617, doi:10.1002/jimd.12617. This article has 38 citations and is from a peer-reviewed journal.

9. (schumann2023theimpactof pages 4-5): Anke Schumann, Marion Brutsche, Monique Havermans, Sarah C. Grünert, Stefan Kölker, Olaf Groß, Luciana Hannibal, and Ute Spiekerkoetter. The impact of metabolic stressors on mitochondrial homeostasis in a renal epithelial cell model of methylmalonic aciduria. Scientific Reports, May 2023. URL: https://doi.org/10.1038/s41598-023-34373-8, doi:10.1038/s41598-023-34373-8. This article has 11 citations and is from a peer-reviewed journal.

10. (schumann2023theimpactof pages 8-8): Anke Schumann, Marion Brutsche, Monique Havermans, Sarah C. Grünert, Stefan Kölker, Olaf Groß, Luciana Hannibal, and Ute Spiekerkoetter. The impact of metabolic stressors on mitochondrial homeostasis in a renal epithelial cell model of methylmalonic aciduria. Scientific Reports, May 2023. URL: https://doi.org/10.1038/s41598-023-34373-8, doi:10.1038/s41598-023-34373-8. This article has 11 citations and is from a peer-reviewed journal.

11. (costanzo2024methylmalonicacidemiatriggers pages 1-2): Michele Costanzo, Armando Cevenini, Laxmikanth Kollipara, Marianna Caterino, Sabrina Bianco, Francesca Pirozzi, Gianluca Scerra, Massimo D’Agostino, Luigi Michele Pavone, Albert Sickmann, and Margherita Ruoppolo. Methylmalonic acidemia triggers lysosomal-autophagy dysfunctions. Cell & Bioscience, May 2024. URL: https://doi.org/10.1186/s13578-024-01245-1, doi:10.1186/s13578-024-01245-1. This article has 16 citations and is from a peer-reviewed journal.

12. (costanzo2024methylmalonicacidemiatriggers pages 7-10): Michele Costanzo, Armando Cevenini, Laxmikanth Kollipara, Marianna Caterino, Sabrina Bianco, Francesca Pirozzi, Gianluca Scerra, Massimo D’Agostino, Luigi Michele Pavone, Albert Sickmann, and Margherita Ruoppolo. Methylmalonic acidemia triggers lysosomal-autophagy dysfunctions. Cell & Bioscience, May 2024. URL: https://doi.org/10.1186/s13578-024-01245-1, doi:10.1186/s13578-024-01245-1. This article has 16 citations and is from a peer-reviewed journal.

13. (costanzo2024methylmalonicacidemiatriggers pages 12-14): Michele Costanzo, Armando Cevenini, Laxmikanth Kollipara, Marianna Caterino, Sabrina Bianco, Francesca Pirozzi, Gianluca Scerra, Massimo D’Agostino, Luigi Michele Pavone, Albert Sickmann, and Margherita Ruoppolo. Methylmalonic acidemia triggers lysosomal-autophagy dysfunctions. Cell & Bioscience, May 2024. URL: https://doi.org/10.1186/s13578-024-01245-1, doi:10.1186/s13578-024-01245-1. This article has 16 citations and is from a peer-reviewed journal.

14. (costanzo2024methylmalonicacidemiatriggers pages 10-12): Michele Costanzo, Armando Cevenini, Laxmikanth Kollipara, Marianna Caterino, Sabrina Bianco, Francesca Pirozzi, Gianluca Scerra, Massimo D’Agostino, Luigi Michele Pavone, Albert Sickmann, and Margherita Ruoppolo. Methylmalonic acidemia triggers lysosomal-autophagy dysfunctions. Cell & Bioscience, May 2024. URL: https://doi.org/10.1186/s13578-024-01245-1, doi:10.1186/s13578-024-01245-1. This article has 16 citations and is from a peer-reviewed journal.

15. (schumann2023theimpactof pages 5-6): Anke Schumann, Marion Brutsche, Monique Havermans, Sarah C. Grünert, Stefan Kölker, Olaf Groß, Luciana Hannibal, and Ute Spiekerkoetter. The impact of metabolic stressors on mitochondrial homeostasis in a renal epithelial cell model of methylmalonic aciduria. Scientific Reports, May 2023. URL: https://doi.org/10.1038/s41598-023-34373-8, doi:10.1038/s41598-023-34373-8. This article has 11 citations and is from a peer-reviewed journal.

16. (schumann2023theimpactof pages 6-8): Anke Schumann, Marion Brutsche, Monique Havermans, Sarah C. Grünert, Stefan Kölker, Olaf Groß, Luciana Hannibal, and Ute Spiekerkoetter. The impact of metabolic stressors on mitochondrial homeostasis in a renal epithelial cell model of methylmalonic aciduria. Scientific Reports, May 2023. URL: https://doi.org/10.1038/s41598-023-34373-8, doi:10.1038/s41598-023-34373-8. This article has 11 citations and is from a peer-reviewed journal.

17. (zhang2023transcriptomeanalysisreveals pages 7-10): Zhilei Zhang, Xin Wang, Yanyun Wang, Yahong Li, Peiying Yang, Yun Sun, and jiang tao. Transcriptome analysis reveals a new insights toward molecular mechanisms of methylmalonic acidemia in hepatocytes. Unknown journal, Dec 2023. URL: https://doi.org/10.21203/rs.3.rs-3691276/v1, doi:10.21203/rs.3.rs-3691276/v1.

18. (costanzo2024methylmalonicacidemiatriggers pages 5-7): Michele Costanzo, Armando Cevenini, Laxmikanth Kollipara, Marianna Caterino, Sabrina Bianco, Francesca Pirozzi, Gianluca Scerra, Massimo D’Agostino, Luigi Michele Pavone, Albert Sickmann, and Margherita Ruoppolo. Methylmalonic acidemia triggers lysosomal-autophagy dysfunctions. Cell & Bioscience, May 2024. URL: https://doi.org/10.1186/s13578-024-01245-1, doi:10.1186/s13578-024-01245-1. This article has 16 citations and is from a peer-reviewed journal.

19. (manoli2023biomarkerstopredict pages 9-10): Irini Manoli, Abigael Gebremariam, Samantha McCoy, Alexandra R. Pass, Jack Gagné, Camryn Hall, Susan Ferry, Carol Van Ryzin, Jennifer L. Sloan, Elisa Sacchetti, Giulio Catesini, Cristiano Rizzo, Diego Martinelli, Marco Spada, Carlo Dionisi‐Vici, and Charles P. Venditti. Biomarkers to predict disease progression and therapeutic response in isolated methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:554-572, Jun 2023. URL: https://doi.org/10.1002/jimd.12636, doi:10.1002/jimd.12636. This article has 28 citations and is from a peer-reviewed journal.

20. (manoli2023biomarkerstopredict pages 10-12): Irini Manoli, Abigael Gebremariam, Samantha McCoy, Alexandra R. Pass, Jack Gagné, Camryn Hall, Susan Ferry, Carol Van Ryzin, Jennifer L. Sloan, Elisa Sacchetti, Giulio Catesini, Cristiano Rizzo, Diego Martinelli, Marco Spada, Carlo Dionisi‐Vici, and Charles P. Venditti. Biomarkers to predict disease progression and therapeutic response in isolated methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:554-572, Jun 2023. URL: https://doi.org/10.1002/jimd.12636, doi:10.1002/jimd.12636. This article has 28 citations and is from a peer-reviewed journal.

21. (manoli2023biomarkerstopredict pages 12-13): Irini Manoli, Abigael Gebremariam, Samantha McCoy, Alexandra R. Pass, Jack Gagné, Camryn Hall, Susan Ferry, Carol Van Ryzin, Jennifer L. Sloan, Elisa Sacchetti, Giulio Catesini, Cristiano Rizzo, Diego Martinelli, Marco Spada, Carlo Dionisi‐Vici, and Charles P. Venditti. Biomarkers to predict disease progression and therapeutic response in isolated methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:554-572, Jun 2023. URL: https://doi.org/10.1002/jimd.12636, doi:10.1002/jimd.12636. This article has 28 citations and is from a peer-reviewed journal.

22. (passantino2023cardiacinvolvementin pages 1-2): Silvia Passantino, Serena Chiellino, Francesca Girolami, Mattia Zampieri, Giovanni Calabri, Gaia Spaziani, Elena Bennati, Giulio Porcedda, Elena Procopio, Iacopo Olivotto, and Silvia Favilli. Cardiac involvement in classical organic acidurias: clinical profile and outcome in a pediatric cohort. Diagnostics, 13:3674, Dec 2023. URL: https://doi.org/10.3390/diagnostics13243674, doi:10.3390/diagnostics13243674. This article has 1 citations.

23. (passantino2023cardiacinvolvementin pages 6-8): Silvia Passantino, Serena Chiellino, Francesca Girolami, Mattia Zampieri, Giovanni Calabri, Gaia Spaziani, Elena Bennati, Giulio Porcedda, Elena Procopio, Iacopo Olivotto, and Silvia Favilli. Cardiac involvement in classical organic acidurias: clinical profile and outcome in a pediatric cohort. Diagnostics, 13:3674, Dec 2023. URL: https://doi.org/10.3390/diagnostics13243674, doi:10.3390/diagnostics13243674. This article has 1 citations.

24. (manoli2024lipodystrophyinmethylmalonic pages 2-4): Irini Manoli, Justin R. Sysol, PamelaSara E. Head, Madeline W. Epping, Oksana Gavrilova, Melissa K. Crocker, Jennifer L. Sloan, Stefanos A. Koutsoukos, Cindy Wang, Yiouli P. Ktena, Sophia Mendelson, Alexandra R. Pass, Patricia M. Zerfas, Victoria Hoffmann, Hilary J. Vernon, Laura A. Fletcher, James C. Reynolds, Maria G. Tsokos, Constantine A. Stratakis, Stephan D. Voss, Kong Y. Chen, Rebecca J. Brown, Ada Hamosh, Gerard T. Berry, Xiaoyuan Shawn Chen, Jack A. Yanovski, and Charles P. Venditti. Lipodystrophy in methylmalonic acidemia associated with elevated fgf21 and abnormal methylmalonylation. JCI Insight, Feb 2024. URL: https://doi.org/10.1172/jci.insight.174097, doi:10.1172/jci.insight.174097. This article has 3 citations and is from a domain leading peer-reviewed journal.

25. (manoli2024lipodystrophyinmethylmalonic pages 10-11): Irini Manoli, Justin R. Sysol, PamelaSara E. Head, Madeline W. Epping, Oksana Gavrilova, Melissa K. Crocker, Jennifer L. Sloan, Stefanos A. Koutsoukos, Cindy Wang, Yiouli P. Ktena, Sophia Mendelson, Alexandra R. Pass, Patricia M. Zerfas, Victoria Hoffmann, Hilary J. Vernon, Laura A. Fletcher, James C. Reynolds, Maria G. Tsokos, Constantine A. Stratakis, Stephan D. Voss, Kong Y. Chen, Rebecca J. Brown, Ada Hamosh, Gerard T. Berry, Xiaoyuan Shawn Chen, Jack A. Yanovski, and Charles P. Venditti. Lipodystrophy in methylmalonic acidemia associated with elevated fgf21 and abnormal methylmalonylation. JCI Insight, Feb 2024. URL: https://doi.org/10.1172/jci.insight.174097, doi:10.1172/jci.insight.174097. This article has 3 citations and is from a domain leading peer-reviewed journal.

26. (ling2024clinicaloutcomesof pages 5-6): Shiying Ling, Shengnan Wu, Ruixue Shuai, Yue Yu, Wenjuan Qiu, Haiyan Wei, Chiju Yang, Peng Xu, Hui Zou, Jizhen Feng, Tingting Niu, Haili Hu, Huiwen Zhang, Lili Liang, Yu Wang, Ting Chen, Feng Xu, Xuefan Gu, and Lianshu Han. Clinical outcomes of patients with mut-type methylmalonic acidemia identified through expanded newborn screening in china. Human Genomics, Jul 2024. URL: https://doi.org/10.1186/s40246-024-00646-0, doi:10.1186/s40246-024-00646-0. This article has 3 citations and is from a peer-reviewed journal.

27. (ling2024clinicaloutcomesof pages 4-5): Shiying Ling, Shengnan Wu, Ruixue Shuai, Yue Yu, Wenjuan Qiu, Haiyan Wei, Chiju Yang, Peng Xu, Hui Zou, Jizhen Feng, Tingting Niu, Haili Hu, Huiwen Zhang, Lili Liang, Yu Wang, Ting Chen, Feng Xu, Xuefan Gu, and Lianshu Han. Clinical outcomes of patients with mut-type methylmalonic acidemia identified through expanded newborn screening in china. Human Genomics, Jul 2024. URL: https://doi.org/10.1186/s40246-024-00646-0, doi:10.1186/s40246-024-00646-0. This article has 3 citations and is from a peer-reviewed journal.

28. (ling2024clinicaloutcomesof pages 6-8): Shiying Ling, Shengnan Wu, Ruixue Shuai, Yue Yu, Wenjuan Qiu, Haiyan Wei, Chiju Yang, Peng Xu, Hui Zou, Jizhen Feng, Tingting Niu, Haili Hu, Huiwen Zhang, Lili Liang, Yu Wang, Ting Chen, Feng Xu, Xuefan Gu, and Lianshu Han. Clinical outcomes of patients with mut-type methylmalonic acidemia identified through expanded newborn screening in china. Human Genomics, Jul 2024. URL: https://doi.org/10.1186/s40246-024-00646-0, doi:10.1186/s40246-024-00646-0. This article has 3 citations and is from a peer-reviewed journal.

29. (NCT04899310 chunk 1):  A Study to Assess the Safety, Pharmacokinetics, and Pharmacodynamics of mRNA-3705 in Participants With Isolated Methylmalonic Acidemia. ModernaTX, Inc.. 2021. ClinicalTrials.gov Identifier: NCT04899310

30. (NCT05295433 chunk 1):  An Extension Study to Evaluate the Long-Term Safety and Clinical Activity of mRNA-3705 in Participants Previously Enrolled in Other Clinical Studies of mRNA-3705. ModernaTX, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05295433

31. (NCT04581785 chunk 1):  Gene Therapy With hLB-001 in Pediatric Patients With Severe Methylmalonic Acidemia. LogicBio Therapeutics, Inc. 2021. ClinicalTrials.gov Identifier: NCT04581785

32. (NCT04732429 chunk 1):  Study of HST5040 in Subjects With Propionic or Methylmalonic Acidemia. HemoShear Therapeutics. 2021. ClinicalTrials.gov Identifier: NCT04732429
