---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:04:38.756075'
end_time: '2026-02-23T23:29:28.653480'
duration_seconds: 1489.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Very Long-Chain Acyl-CoA Dehydrogenase Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Very Long-Chain Acyl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Very Long-Chain Acyl-CoA Dehydrogenase Deficiency**.
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
- **Disease Name:** Very Long-Chain Acyl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Very Long-Chain Acyl-CoA Dehydrogenase Deficiency**.
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


Title: Pathophysiology of Very Long-Chain Acyl-CoA Dehydrogenase Deficiency (VLCADD)

Publication window emphasized: 2023–2024, with mechanistic primary studies and authoritative reviews.

1. Disease definition, identifiers, and current understanding

Disease and identifiers
VLCAD deficiency (VLCADD) is an autosomal recessive inborn error of mitochondrial long-chain fatty-acid β-oxidation (LC-FAO) caused by pathogenic variants in ACADVL (HGNC:92), encoding very long-chain acyl-CoA dehydrogenase (VLCAD). It is characterized biochemically by accumulation of long-chain acylcarnitines (classically C14:1 and related ratios) and clinically by energy failure and lipotoxicity in high-energy-demand organs (heart, skeletal muscle, liver), particularly during catabolic stress. (sebaa2023adistinctivemetabolomics pages 1-2, bandari2024managementandoutcomes pages 1-2)

MONDO ID
OpenTargets lists “very long chain acyl-CoA dehydrogenase deficiency” as MONDO:0008723. (bandari2024managementandoutcomes pages 1-2)

Canonical biochemical defect
VLCAD catalyzes the first dehydrogenation step in the β-oxidation spiral for long-chain acyl-CoAs (reported as chain length 12–20 carbons in a 2023 metabolomics paper, and broader long-chain ranges in other sources). Impaired VLCAD function reduces LC-FAO flux, decreases acetyl-CoA generation (thereby limiting ketogenesis), and promotes accumulation of long-chain acylcarnitines, fatty acids, and related lipid intermediates that can be toxic and arrhythmogenic. (sebaa2023adistinctivemetabolomics pages 1-2, nurjanah2023modificationofdietary pages 14-17)

Epidemiology (recently reported ranges)
A 2024 clinical cohort review reports prevalence ~1:30,000–1:100,000 births. (bandari2024managementandoutcomes pages 1-2)
A 2024 immunometabolism study reports worldwide prevalence 1:31,500–1:94,569. (mosegaard2024humaninbornerrors pages 1-2)
A 2024 genetics paper reports region-specific prevalence ranges and cites China incidence estimates (e.g., 1/236,655–1/70,424) and broader Europe/America vs Asia differences. (li2024fournovelvariants pages 1-2)

2. Core pathophysiology (molecular/cellular mechanisms)

2.1 Energy failure and impaired metabolic flexibility
Loss of LC-FAO reduces availability of reducing equivalents and acetyl-CoA for mitochondrial ATP production and hepatic ketogenesis, forcing compensatory reliance on glucose utilization and gluconeogenesis. In long-chain FAO defects, liver FAO normally supports gluconeogenesis and ureagenesis; when FAO is impaired, hypoketotic hypoglycemia and hyperammonemia can occur in decompensation. (penaquintana2024nutritionalmanagementof pages 1-3, nurjanah2023modificationofdietary pages 14-17)

2.2 Lipotoxic metabolite accumulation and mitochondrial dysfunction
Accumulating long-chain acylcarnitines (e.g., C14:1 and longer C14–C18 species) are central biochemical hallmarks and may contribute directly to pathology. A 2023 metabolomics study explicitly links acylcarnitine accumulation to increased cellular permeability, inflammation, reduced insulin-stimulated glucose uptake via Ca2+-mediated pathways, lipid toxicity, cellular stress, and cell death—providing a mechanistic bridge from biochemistry to organ dysfunction. (sebaa2023adistinctivemetabolomics pages 1-2)

A 2023 mRNA-therapy study discusses additional mitochondrial toxicity hypotheses: saturated/unsaturated dicarboxylic acids and long-chain fatty acids (e.g., cis-5-tetradecenoic, myristic acids) may act as metabolic inhibitors, uncouplers, or modulators of mitochondrial permeability transition, and VLCAD deficiency is associated with reduced electron transport chain (ETC) supercomplexes and disruption of an FAO–ETC macromolecular complex. (zhao2023syntheticmrnarescues pages 6-8)

2.3 Oxidative stress and glutathione vulnerability
Oxidative stress is increasingly highlighted as a component of VLCAD pathophysiology. A 2023 study focusing on VLCAD patient fibroblasts describes secondary mitochondrial defects including increased reactive oxygen species (ROS) and vulnerability of the glutathione (GSH) antioxidant system; it frames mitochondrial NADPH production (e.g., via isocitrate dehydrogenase 2, IDH2) as relevant to GSH recycling and cellular resilience under metabolic stress. (lund2023oddandevennumbered pages 1-3)

Consistent with oxidative stress in vivo, an untargeted dried-blood-spot metabolomics study reports elevated glutathione in VLCADD newborns, interpreted as suggesting oxidative stress events resulting from the disease pathology. (sebaa2023adistinctivemetabolomics pages 8-10)

2.4 Immunometabolic dysregulation (2024 advance)
A 2024 FASEB BioAdvances study provides human genetic evidence that LC-FAO genes are required for adequate innate immune responses: patient fibroblasts with deleterious ACADVL variants show “reduced TLR4 expression levels, impaired TLR4 signaling, and reduced or absent induction of pro-inflammatory cytokines such as IL-6” after LPS stimulation. This ties VLCADD to impaired inflammatory signaling and helps explain why infection/inflammation is a common trigger of metabolic decompensation. (mosegaard2024humaninbornerrors pages 1-2, mosegaard2024humaninbornerrors pages 2-4)

3. Key molecular players (genes/proteins), metabolites, cells, and anatomy

3.1 Genes/proteins
Causal gene:
• ACADVL (VLCAD). (bandari2024managementandoutcomes pages 1-2, sebaa2023adistinctivemetabolomics pages 1-2)

Mechanistically implicated (from 2023–2024 mechanistic sources in context):
• Carnitine shuttle / fatty acid import machinery (CPT1/CPT2/CACT as a system-level requirement for long-chain FAO). (penaquintana2024nutritionalmanagementof pages 1-3, nurjanah2023modificationofdietary pages 14-17)
• ETFDH (electron transfer flavoprotein dehydrogenase) and ETF/ETF-QO (used as comparative lcFAOD evidence in immune study). (mosegaard2024humaninbornerrors pages 1-2)
• TLR4 signaling axis (immune trigger response). (mosegaard2024humaninbornerrors pages 1-2, mosegaard2024humaninbornerrors pages 2-4)
• TCA cycle enzymes/metabolites relevant to immunometabolism: SDH, succinate, itaconate, HIF1α. (mosegaard2024humaninbornerrors pages 1-2)
• ETC supercomplexes and adenine nucleotide translocator (mitochondrial inner membrane bioenergetics). (zhao2023syntheticmrnarescues pages 6-8)
• Antioxidant/redox support: glutathione, NADPH, and mitochondrial matrix NADPH sources (e.g., IDH2 discussed in oxidative-stress study). (lund2023oddandevennumbered pages 1-3)

3.2 Chemical entities (metabolites, nutritional therapeutics)
Key diagnostic/pathogenic lipid intermediates:
• Tetradecenoylcarnitine (C14:1 acylcarnitine) and related long-chain acylcarnitines (C14, C14:2; C16, C18 species). (sebaa2023adistinctivemetabolomics pages 1-2, zhao2023syntheticmrnarescues pages 6-8)
• Long-chain fatty acids; saturated/unsaturated dicarboxylic acids (proposed toxic intermediates). (zhao2023syntheticmrnarescues pages 6-8)

Oxidative stress / immunometabolism:
• Glutathione (elevated in newborn DBS metabolomics; mechanistically central in fibroblast stress model). (sebaa2023adistinctivemetabolomics pages 8-10, lund2023oddandevennumbered pages 1-3)
• Succinate (immunometabolic signaling after LPS). (mosegaard2024humaninbornerrors pages 1-2)

Therapeutic nutritional substrates:
• Medium-chain triglycerides (MCT) and long-chain triglycerides (LCT) as modulated dietary inputs. (bandari2024managementandoutcomes pages 1-2)
• Triheptanoin (heptanoate triglyceride; “UX007”; “C7 oil”), providing propionyl-CoA for anaplerosis and supporting gluconeogenesis. (nurjanah2023heptanoateimprovescompensatory pages 1-2, NCT01886378 chunk 1)

3.3 Cell types (CL-oriented)
Evidence directly includes:
• Dermal fibroblasts (patient-derived mechanistic and immune-response assays). (mosegaard2024humaninbornerrors pages 2-4, zhao2023syntheticmrnarescues pages 6-8)

Pathophysiology and clinical manifestations implicate (organ-demand driven):
• Hepatocytes/liver metabolic cells (gluconeogenesis/ketogenesis; mRNA therapy hepatic targeting). (nurjanah2023heptanoateimprovescompensatory pages 1-2, zhao2023syntheticmrnarescues pages 6-8)
• Cardiomyocytes and skeletal myocytes (myopathy, cardiomyopathy, rhabdomyolysis). (bandari2024managementandoutcomes pages 1-2, mosegaard2024humaninbornerrors pages 1-2)

3.4 Anatomical locations (UBERON-oriented)
Primary affected tissues:
• Heart (cardiomyopathy/arrhythmia). (bandari2024managementandoutcomes pages 1-2, liu2024casereporton pages 2-3)
• Skeletal muscle (exercise intolerance, rhabdomyolysis). (mosegaard2024humaninbornerrors pages 1-2, rouyer2024long‐termprognosisof pages 7-9)
• Liver (hypoketotic hypoglycemia, hyperammonemia; supports gluconeogenesis). (penaquintana2024nutritionalmanagementof pages 1-3, liu2024casereporton pages 2-3)

4. Biological processes and cellular components (GO-ready)

4.1 Disrupted biological processes (GO: Biological Process)
Core:
• Mitochondrial long-chain fatty acid β-oxidation / fatty acid oxidation. (bandari2024managementandoutcomes pages 1-2, nurjanah2023modificationofdietary pages 14-17)
• Ketone body metabolic process (impaired ketogenesis; contributing to hypoketotic hypoglycemia). (nurjanah2023modificationofdietary pages 14-17)
• Oxidative phosphorylation / mitochondrial respiration / ATP production. (zhao2023syntheticmrnarescues pages 6-8)

Secondary/associated:
• Response to oxidative stress; glutathione metabolic process; ROS handling. (lund2023oddandevennumbered pages 1-3, sebaa2023adistinctivemetabolomics pages 8-10)
• Tricarboxylic acid cycle (anaplerosis and immune-metabolic coupling). (mosegaard2024humaninbornerrors pages 1-2, lund2023oddandevennumbered pages 1-3)
• Gluconeogenesis and endogenous glucose production compensation. (nurjanah2023heptanoateimprovescompensatory pages 1-2)
• Innate immune response pathways: TLR4 signaling pathway; cytokine production (IL-6; IL-1β context). (mosegaard2024humaninbornerrors pages 1-2, mosegaard2024humaninbornerrors pages 2-4)

4.2 Cellular components (GO: Cellular Component)
• Mitochondrial matrix and inner mitochondrial membrane (β-oxidation enzymes and ETC coupling). (nurjanah2023modificationofdietary pages 14-17, zhao2023syntheticmrnarescues pages 6-8)
• Respiratory chain complexes / ETC supercomplexes (bioenergetic assemblies). (zhao2023syntheticmrnarescues pages 6-8)
• Plasma membrane TLR4 complex (immune recognition/signaling). (mosegaard2024humaninbornerrors pages 1-2)
• Endoplasmic reticulum (as a site of fatty-acid elongation in lcFAOD biomarker work; relevant to lipid remodeling when FAO is impaired). (schwantje2024tracerbasedlipidomicsenablesa pages 14-14)

5. Disease progression: sequence of events from trigger to clinical manifestation

Triggering conditions
Catabolic stressors (fasting, illness/infection/inflammation, and exercise) increase reliance on FAO; VLCADD patients often decompensate under these triggers, with infection recognized clinically as a trigger that can precipitate metabolic decompensation and rhabdomyolysis. (mosegaard2024humaninbornerrors pages 1-2, rouyer2024long‐termprognosisof pages 11-12)

Stepwise pathophysiological cascade (integrated)
1) Trigger increases FA mobilization and mitochondrial LC-FAO demand.
2) VLCAD block reduces LC-FAO flux → reduced acetyl-CoA and ATP generation; ketogenesis fails to increase appropriately → hypoketotic hypoglycemia risk, especially with fasting. (nurjanah2023modificationofdietary pages 14-17, nurjanah2023heptanoateimprovescompensatory pages 1-2)
3) Long-chain acylcarnitines and lipid intermediates accumulate (C14:1 and longer) → proposed direct cellular toxicity, altered membrane integrity/permeability, Ca2+-linked signaling disruption, and arrhythmogenic potential. (sebaa2023adistinctivemetabolomics pages 1-2, nurjanah2023modificationofdietary pages 14-17)
4) Secondary mitochondrial defects emerge (ETC supercomplex disruption, permeability transition/uncoupling hypotheses) → worsened bioenergetics and oxidative stress. (zhao2023syntheticmrnarescues pages 6-8, lund2023oddandevennumbered pages 1-3)
5) Tissue-level failure in heart/skeletal muscle/liver manifests as cardiomyopathy/arrhythmias, rhabdomyolysis, hepatic dysfunction, hyperammonemia, and multi-organ crisis. (bandari2024managementandoutcomes pages 1-2, liu2024casereporton pages 2-3)
6) Immune/inflammatory coupling: impaired TLR4 signaling and cytokine induction in VLCADD cells may alter host response to infection and influence how inflammatory triggers precipitate crisis. (mosegaard2024humaninbornerrors pages 1-2)

Distinct clinical phases
A 2024 clinical review summarizes a spectrum including: severe early-onset cardiac phenotype, hepatic/hypoketotic hypoglycemia phenotype, and later-onset myopathic phenotype with intermittent rhabdomyolysis. (bandari2024managementandoutcomes pages 1-2)

6. Phenotypic manifestations (mechanism-linked; HP-ready)

Key clinical phenotypes
• Hypoketotic hypoglycemia (HP:0001943) as a feared complication; in a severe neonatal case, glucose reached 0.02 mmol/L. (stenlid2023lowfastingconcentrations pages 1-2, liu2024casereporton pages 2-3)
• Rhabdomyolysis (HP:0003201) / hyperCKemia: neonatal case CK 19,448 U/L; cohort peak CK as high as 76,656 U/L; adult FAOD cohort mean CK during rhabdomyolysis 68,958 U/L. (liu2024casereporton pages 2-3, bandari2024managementandoutcomes pages 7-8, rouyer2024long‐termprognosisof pages 1-2)
• Cardiomyopathy (HP:0001638) and arrhythmia/ventricular fibrillation (HP:0001663): neonatal case had ventricular fibrillation with echocardiographic dysfunction and pulmonary hypertension. (liu2024casereporton pages 2-3)
• Hyperammonemia (HP:0001987) and lactic acidosis (HP:0003128) during crisis. (liu2024casereporton pages 2-3, penaquintana2024nutritionalmanagementof pages 1-3)

Adult/long-term outcomes (recent cohort statistics)
In a 2024 adult cohort of muscular FAODs including VLCAD, rhabdomyolysis occurred in 84% of patients overall, with mean pre-diagnosis rhabdomyolysis rate 1.92 episodes/year (VLCAD subgroup reported 4.9) declining to 0.82/year post-diagnosis (VLCAD subgroup 2.5). Only one new ICU admission occurred after diagnosis (VLCAD). (rouyer2024long‐termprognosisof pages 7-9)

7. Recent developments and latest research (2023–2024 prioritized)

7.1 Metabolomics-based biomarker refinement (2023)
Untargeted LC-HRMS metabolomics in dried blood spots (n=15 VLCADD vs n=15 controls) identified 206 dysregulated metabolites and proposed high-performing biomarkers: 3,4-dihydroxytetradecanoylcarnitine (AUC=1), PIP(20:1)/PGF1alpha (AUC=0.982), PIP2(16:0/22:3) (AUC=0.978). Pathway enrichment and biomarker ROC visualizations are shown in Figures 4–5. (sebaa2023adistinctivemetabolomics pages 1-2, sebaa2023adistinctivemetabolomics media cf95c180, sebaa2023adistinctivemetabolomics media f4e325fd)

7.2 Immunometabolic mechanism (2024)
Patient-cell evidence that ACADVL variants impair TLR4 pathway responsiveness to LPS (lower TLR4 expression/signaling and IL-6 induction), connecting LC-FAO to innate immune competence and supporting the clinical observation that infections can trigger crises. (mosegaard2024humaninbornerrors pages 1-2, mosegaard2024humaninbornerrors pages 2-4)

7.3 Triheptanoin/heptanoate mechanism (2023)
Tracer studies in VLCAD−/− mice show increased contribution of glycerol-derived gluconeogenesis to blood glucose; this difference normalized with heptanoate (C7), consistent with heptanoate providing substrates that reduce the need for compensatory gluconeogenesis and support glucose homeostasis. (nurjanah2023heptanoateimprovescompensatory pages 1-2)

7.4 Emerging causal therapy approaches (2023)
LNP-formulated human VLCAD mRNA restored VLCAD activity and improved mitochondrial FAO/respiration/ATP in patient cells and Acadvl−/− mice; systemic serum C14–C18 acylcarnitines decreased after treatment. The authors note treatment was not proinflammatory in the tested acute mouse setting. (zhao2023syntheticmrnarescues pages 6-8)

8. Current applications and real-world implementations

8.1 Newborn screening (NBS) workflows
Ontario’s real-world protocol (NBS since 2006) uses dried blood spot MS/MS acylcarnitines with C14:1 as the main marker, followed by confirmatory plasma/serum acylcarnitines, lymphocyte VLCAD enzyme activity, and ACADVL molecular testing when activity is abnormal. Newborn-screen C14:1 strongly correlates with residual enzyme activity (p=0.0003 reported). (bandari2024managementandoutcomes pages 1-2, bandari2024managementandoutcomes pages 2-4)

8.2 Dietary management (expert synthesis 2024)
Core approach: provide sufficient glucose to prevent lipolysis and minimize reliance on FAO; in long-chain FAODs, quantitative guidance includes restricting LCT to ~10% of energy and supplementing MCT (10–25% of energy) with total MCT+LCT 20–35% of energy, while monitoring essential fatty acids and fat-soluble vitamins. (penaquintana2024nutritionalmanagementof pages 1-3)

8.3 Triheptanoin implementation and dosing guidance
A 2024 nutrition review describes triheptanoin as an FDA-approved odd-chain triglyceride therapy for LC-FAODs, with dosing described as 20% of total energy and/or 25–35% total energy, and also cited in g/kg/day ranges by age group; GI adverse effects are common but may improve with dose fractionation. (penaquintana2024nutritionalmanagementof pages 6-7)

ClinicalTrials.gov implementation example
NCT01886378 (Ultragenyx; “UX007”) is an open-label phase 2 study in LC-FAODs (including VLCAD) with dosing titrated to 25–35% of total caloric intake (or maximum tolerated dose) and follow-up over 24 weeks (treatment period) with extension to 78 weeks total. Primary outcomes include changes in exercise tolerance during cycle ergometry (workload AUC/time), respiratory exchange ratio AUC, and exercise duration; functional outcomes include walk tests and HR-based indices. (NCT01886378 chunk 1)

9. Expert opinion and analysis (authoritative sources)

Clinical management perspective
The 2024 Ontario chart review emphasizes that genotype–phenotype prediction is imperfect and that functional testing (enzyme activity) can help differentiate carriers/mildly affected individuals and inform management; it also emphasizes avoiding overtreatment as NBS increases detection of milder phenotypes. (bandari2024managementandoutcomes pages 1-2, bandari2024managementandoutcomes pages 2-4)

Adult neuromuscular perspective
The 2024 European Journal of Neurology cohort highlights a long diagnostic delay in adult FAODs and reports reduced rhabdomyolysis frequency after diagnosis and management, supporting the practical value of diagnosis plus lifestyle/diet adaptation even when pharmacologic options are limited. (rouyer2024long‐termprognosisof pages 1-2, rouyer2024long‐termprognosisof pages 7-9)

10. Relevant recent statistics and data (selected)

Newborn/child cohort (2024; Ontario; n=12)
• Enzyme activity stratification: 7/12 >10% residual activity; 5/12 <10%. (bandari2024managementandoutcomes pages 1-2)
• Correlation: newborn-screen C14:1 vs enzyme activity p=0.0003; at diagnosis p=0.0295. (bandari2024managementandoutcomes pages 1-2)
• Rhabdomyolysis marker: peak CK up to 76,656 U/L; no significant correlation between enzyme activity and admissions/CK. (bandari2024managementandoutcomes pages 7-8)

Adult cohort (2024; n=44 muscular FAOD; 13 VLCAD)
• Rhabdomyolysis in 84% overall; mean CK 68,958 U/L. (rouyer2024long‐termprognosisof pages 1-2)
• Rhabdomyolysis rate reduced: mean 1.92/year pre-diagnosis to 0.82/year post-diagnosis; VLCAD subgroup 4.9/year to 2.5/year. (rouyer2024long‐termprognosisof pages 7-9)

Metabolomics biomarkers (2023; DBS n=15 vs 15)
• 206 dysregulated metabolites; top biomarker AUCs 0.978–1.0 and top-ranked ROC AUC range ~0.986–0.992 shown. (sebaa2023adistinctivemetabolomics pages 1-2, sebaa2023adistinctivemetabolomics pages 8-10)

Neonatal case (2024)
• C14:1 5.053 μmol/L at 3 days → 0.192 μmol/L by 5 months with treatment. (liu2024casereporton pages 2-3)
• Glucose 0.02 mmol/L; CK 19,448 U/L; AST 384.2 U/L; ammonia 83.2 μmol/L; ventricular fibrillation and echocardiographic dysfunction. (liu2024casereporton pages 2-3)

11. Knowledge-base–oriented annotation blocks

11.1 Pathophysiology description (narrative)
VLCADD results from ACADVL loss-of-function causing a mitochondrial long-chain β-oxidation block. Under catabolic stress, impaired LC-FAO reduces ATP and acetyl-CoA supply (limiting ketogenesis and hepatic support for gluconeogenesis/ureagenesis), while long-chain acylcarnitines and lipid intermediates accumulate, promoting mitochondrial dysfunction, oxidative stress, and inflammatory/immune dysregulation. This combined energy deficiency plus lipotoxicity underlies cardiomyopathy/arrhythmias, rhabdomyolysis, and hypoketotic hypoglycemia, with severity modulated by residual enzyme activity and physiological stress exposure. (bandari2024managementandoutcomes pages 1-2, sebaa2023adistinctivemetabolomics pages 1-2, zhao2023syntheticmrnarescues pages 6-8)

11.2 Gene/protein annotations (HGNC)
• ACADVL (acyl-CoA dehydrogenase very long chain; VLCAD). (bandari2024managementandoutcomes pages 1-2)

11.3 Suggested GO terms (not exhaustive; evidence-aligned)
Biological Process:
• fatty acid beta-oxidation (mitochondrial) (supported generally across VLCAD sources). (bandari2024managementandoutcomes pages 1-2, nurjanah2023modificationofdietary pages 14-17)
• oxidative phosphorylation / mitochondrial respiration / ATP synthesis coupled electron transport. (zhao2023syntheticmrnarescues pages 6-8)
• tricarboxylic acid cycle; anaplerotic reactions (heptanoate/triheptanoin rationale; immune succinate axis). (mosegaard2024humaninbornerrors pages 1-2, lund2023oddandevennumbered pages 1-3)
• response to oxidative stress; glutathione metabolic process. (sebaa2023adistinctivemetabolomics pages 8-10, lund2023oddandevennumbered pages 1-3)
• toll-like receptor 4 signaling pathway; cytokine production (IL-6). (mosegaard2024humaninbornerrors pages 1-2)

Cellular Component:
• mitochondrion; mitochondrial matrix; inner mitochondrial membrane; respiratory chain complexes/supercomplexes. (nurjanah2023modificationofdietary pages 14-17, zhao2023syntheticmrnarescues pages 6-8)
• plasma membrane (TLR4). (mosegaard2024humaninbornerrors pages 1-2)
• endoplasmic reticulum (lipid elongation context in lcFAOD biomarker work). (schwantje2024tracerbasedlipidomicsenablesa pages 14-14)

11.4 Suggested HP terms (examples)
• Hypoketotic hypoglycemia (HP:0001943). (stenlid2023lowfastingconcentrations pages 1-2)
• Rhabdomyolysis / elevated creatine kinase (HP:0003201 / HP:0003236). (bandari2024managementandoutcomes pages 7-8, liu2024casereporton pages 2-3)
• Cardiomyopathy (HP:0001638). (liu2024casereporton pages 2-3)
• Cardiac arrhythmia / ventricular fibrillation (HP:0001663 / HP:0004756). (liu2024casereporton pages 2-3)
• Hyperammonemia (HP:0001987). (liu2024casereporton pages 2-3)

11.5 Suggested UBERON tissues
• Heart; liver; skeletal muscle. (bandari2024managementandoutcomes pages 1-2, penaquintana2024nutritionalmanagementof pages 1-3)

11.6 Suggested CL cell types
• Dermal fibroblast (directly used in mechanistic studies). (mosegaard2024humaninbornerrors pages 2-4)
• Hepatocyte (implicated by liver glucose homeostasis role and hepatic-targeted mRNA therapy). (nurjanah2023heptanoateimprovescompensatory pages 1-2, zhao2023syntheticmrnarescues pages 6-8)

11.7 Suggested CHEBI entities (examples)
• Tetradecenoylcarnitine (C14:1 acylcarnitine), long-chain acylcarnitines. (sebaa2023adistinctivemetabolomics pages 1-2, zhao2023syntheticmrnarescues pages 6-8)
• Glutathione. (sebaa2023adistinctivemetabolomics pages 8-10)
• Succinate. (mosegaard2024humaninbornerrors pages 1-2)
• Propionyl-CoA; succinyl-CoA (triheptanoin/heptanoate anaplerosis). (lund2023oddandevennumbered pages 1-3)

12. Evidence items with PMIDs (as available from retrieved sources)

Note: The OpenTargets evidence list includes older key mechanistic/genetic PubMed records (e.g., 9973285, 8739957, 25929793, 27604308, 8845838, 10077518, 9461620), but PMIDs were not present in the retrieved full-text snippets for the 2023–2024 papers above. Therefore, PMIDs for the 2023–2024 sources could not be programmatically verified from the provided tool outputs.

Where DOI/URL/date are available (for user traceability):
• Al Bandari et al., Int J Neonatal Screening, Published 30 Mar 2024. https://doi.org/10.3390/ijns10020029 (bandari2024managementandoutcomes pages 1-2)
• Mosegaard et al., FASEB BioAdvances, Accepted 21 Jul 2024 (Aug 2024 issue). https://doi.org/10.1096/fba.2024-00060 (mosegaard2024humaninbornerrors pages 1-2)
• Sebaa et al., Metabolites, Published 5 Jun 2023. https://doi.org/10.3390/metabo13060725 (sebaa2023adistinctivemetabolomics pages 1-2)
• Nurjanah et al., Nutrients, Published 5 Nov 2023. https://doi.org/10.3390/nu15214689 (nurjanah2023heptanoateimprovescompensatory pages 1-2)
• Lund et al., BBA Mol Cell Biol Lipids, Feb 2023. https://doi.org/10.1016/j.bbalip.2022.159248 (lund2023oddandevennumbered pages 1-3)
• Zhao et al., Mol Genet Metab, Jan 2023. https://doi.org/10.1016/j.ymgme.2022.106982 (zhao2023syntheticmrnarescues pages 6-8)
• Rouyer et al., Eur J Neurol, Nov 2024. https://doi.org/10.1111/ene.16138 (rouyer2024long‐termprognosisof pages 1-2)
• Peña-Quintana & Correcher-Medina, Nutrients, Published 14 Aug 2024. https://doi.org/10.3390/nu16162707 (penaquintana2024nutritionalmanagementof pages 1-3)
• ClinicalTrials.gov: NCT01886378 (UX007 triheptanoin; start 6 Feb 2014; results posted 11 Feb 2021). https://clinicaltrials.gov/study/NCT01886378 (NCT01886378 chunk 1)

Limitations
This report is constrained to the documents successfully retrieved in this run; several highly relevant reviews (e.g., a 2023 Journal of Inherited Metabolic Disease “Fifty years…” review) were listed as unobtainable by the tool. Additionally, PMIDs for the 2023–2024 articles were not available in the retrieved text snippets, preventing PMID-verified citations for those specific papers.


References

1. (sebaa2023adistinctivemetabolomics pages 1-2): Rajaa Sebaa, Reem H. AlMalki, Wafaa Alseraty, and Anas M. Abdel Rahman. A distinctive metabolomics profile and potential biomarkers for very long acylcarnitine dehydrogenase deficiency (vlcadd) diagnosis in newborns. Metabolites, 13:725, Jun 2023. URL: https://doi.org/10.3390/metabo13060725, doi:10.3390/metabo13060725. This article has 13 citations.

2. (bandari2024managementandoutcomes pages 1-2): Maria Al Bandari, Laura Nagy, Vivian Cruz, Stacy Hewson, Alomgir Hossain, and Michal Inbar-Feigenberg. Management and outcomes of very long-chain acyl-coa dehydrogenase deficiency (vlcad deficiency): a retrospective chart review. International Journal of Neonatal Screening, 10:29, Mar 2024. URL: https://doi.org/10.3390/ijns10020029, doi:10.3390/ijns10020029. This article has 11 citations.

3. (nurjanah2023modificationofdietary pages 14-17): Modification of dietary substrates impacts glucose homeostasis in very long-chain Acyl-CoA dehydrogenase deficient (VLCAD-/-) mice This article has 0 citations.

4. (mosegaard2024humaninbornerrors pages 1-2): Signe Mosegaard, Krishna S. Twayana, Simone W. Denis, Jeffrey Kroon, Bauke V. Schomakers, Michel van Weeghel, Riekelt H. Houtkooper, Rikke K. J. Olsen, and Christian K. Holm. Human inborn errors of long‐chain fatty acid oxidation show impaired inflammatory responses to tlr4‐ligand lps. FASEB BioAdvances, 6:337-350, Aug 2024. URL: https://doi.org/10.1096/fba.2024-00060, doi:10.1096/fba.2024-00060. This article has 5 citations.

5. (li2024fournovelvariants pages 1-2): Lulu Li, Yueling Tang, Jin-qi Zhao, L. Gong, N. Yang, Shunan Wang, Hai-he Yang, and Yuanyuan Kong. Four novel variants identified in the acadvl gene causing very-long-chain acyl-coenzyme a dehydrogenase deficiency in four unrelated chinese families. Frontiers in Genetics, Aug 2024. URL: https://doi.org/10.3389/fgene.2024.1433160, doi:10.3389/fgene.2024.1433160. This article has 3 citations and is from a peer-reviewed journal.

6. (penaquintana2024nutritionalmanagementof pages 1-3): Luis Peña-Quintana and Patricia Correcher-Medina. Nutritional management of patients with fatty acid oxidation disorders. Nutrients, 16:2707, Aug 2024. URL: https://doi.org/10.3390/nu16162707, doi:10.3390/nu16162707. This article has 7 citations.

7. (zhao2023syntheticmrnarescues pages 6-8): Xue-Jun Zhao, AI-Walid Mohsen, Stephanie Mihalik, Keaton Solo, Ermal Aliu, Huifang Shi, Shakuntala Basu, Catherine Kochersperger, Clinton Van’t Land, Anuradha Karunanidhi, Kimberly A. Coughlan, Summar Siddiqui, Lisa M. Rice, Shawn Hillier, Eleonora Guadagnin, Paloma H. Giangrande, Paolo G.V. Martini, and Jerry Vockley. Synthetic mrna rescues very long-chain acyl-coa dehydrogenase deficiency in patient fibroblasts and a murine model. Molecular Genetics and Metabolism, 138(1):106982, Jan 2023. URL: https://doi.org/10.1016/j.ymgme.2022.106982, doi:10.1016/j.ymgme.2022.106982. This article has 16 citations and is from a peer-reviewed journal.

8. (lund2023oddandevennumbered pages 1-3): Martin Lund, Robert Heaton, Iain P. Hargreaves, Niels Gregersen, and Rikke K.J. Olsen. Odd- and even-numbered medium-chained fatty acids protect against glutathione depletion in very long-chain acyl-coa dehydrogenase deficiency. Biochimica et Biophysica Acta (BBA) - Molecular and Cell Biology of Lipids, 1868(2):159248, Feb 2023. URL: https://doi.org/10.1016/j.bbalip.2022.159248, doi:10.1016/j.bbalip.2022.159248. This article has 6 citations and is from a peer-reviewed journal.

9. (sebaa2023adistinctivemetabolomics pages 8-10): Rajaa Sebaa, Reem H. AlMalki, Wafaa Alseraty, and Anas M. Abdel Rahman. A distinctive metabolomics profile and potential biomarkers for very long acylcarnitine dehydrogenase deficiency (vlcadd) diagnosis in newborns. Metabolites, 13:725, Jun 2023. URL: https://doi.org/10.3390/metabo13060725, doi:10.3390/metabo13060725. This article has 13 citations.

10. (mosegaard2024humaninbornerrors pages 2-4): Signe Mosegaard, Krishna S. Twayana, Simone W. Denis, Jeffrey Kroon, Bauke V. Schomakers, Michel van Weeghel, Riekelt H. Houtkooper, Rikke K. J. Olsen, and Christian K. Holm. Human inborn errors of long‐chain fatty acid oxidation show impaired inflammatory responses to tlr4‐ligand lps. FASEB BioAdvances, 6:337-350, Aug 2024. URL: https://doi.org/10.1096/fba.2024-00060, doi:10.1096/fba.2024-00060. This article has 5 citations.

11. (nurjanah2023heptanoateimprovescompensatory pages 1-2): Siti Nurjanah, Albert Gerding, Marcel A. Vieira-Lara, Bernard Evers, Miriam Langelaar-Makkinje, Ute Spiekerkoetter, Barbara M. Bakker, and Sara Tucci. Heptanoate improves compensatory mechanism of glucose homeostasis in mitochondrial long-chain fatty acid oxidation defect. Nutrients, 15:4689, Nov 2023. URL: https://doi.org/10.3390/nu15214689, doi:10.3390/nu15214689. This article has 5 citations.

12. (NCT01886378 chunk 1):  A Study of UX007 (Triheptanoin) in Participants With Long-Chain Fatty Acid Oxidation Disorders (LC-FAOD). Ultragenyx Pharmaceutical Inc. 2014. ClinicalTrials.gov Identifier: NCT01886378

13. (liu2024casereporton pages 2-3): R Liu, J Nie, Q Cao, S Cui, X Miao, J Pan, and X Chen. Case report on very long chain acyl-coa dehydrogenase deficiency in a term neonate. Journal of Case Reports and Medical Images, Dec 2024. URL: https://doi.org/10.52768/jcaserepclinimages/1159, doi:10.52768/jcaserepclinimages/1159. This article has 0 citations.

14. (rouyer2024long‐termprognosisof pages 7-9): Alice Rouyer, Céline Tard, Anne‐Frédérique Dessein, Marco Spinazzi, Anne‐Laure Bédat‐Millet, Dalia Dimitri‐Boulos, Aleksandra Nadaj‐Pakleza, Jean‐Baptiste Chanson, Guillaume Nicolas, Claire Douillard, and Pascal Laforêt. Long‐term prognosis of fatty‐acid oxidation disorders in adults: optimism despite the limited effective therapies available. European Journal of Neurology, Nov 2024. URL: https://doi.org/10.1111/ene.16138, doi:10.1111/ene.16138. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (schwantje2024tracerbasedlipidomicsenablesa pages 14-14): M Schwantje and S Mosegaard. Tracer-based lipidomics enables the discovery of disease-specific candidate biomarkers in mitochondrial β-oxidation disorders. Unknown journal, 2024.

16. (rouyer2024long‐termprognosisof pages 11-12): Alice Rouyer, Céline Tard, Anne‐Frédérique Dessein, Marco Spinazzi, Anne‐Laure Bédat‐Millet, Dalia Dimitri‐Boulos, Aleksandra Nadaj‐Pakleza, Jean‐Baptiste Chanson, Guillaume Nicolas, Claire Douillard, and Pascal Laforêt. Long‐term prognosis of fatty‐acid oxidation disorders in adults: optimism despite the limited effective therapies available. European Journal of Neurology, Nov 2024. URL: https://doi.org/10.1111/ene.16138, doi:10.1111/ene.16138. This article has 11 citations and is from a domain leading peer-reviewed journal.

17. (stenlid2023lowfastingconcentrations pages 1-2): Rasmus Stenlid, Hannes Manell, Rikard Seth, Sara Y. Cerenius, Azazul Chowdhury, Camilla Roa Cortés, Isabelle Nyqvist, Thomas Lundqvist, Maria Halldin, and Peter Bergsten. Low fasting concentrations of glucagon in patients with very long-chain acyl-coa dehydrogenase deficiency. Metabolites, 13:780, Jun 2023. URL: https://doi.org/10.3390/metabo13070780, doi:10.3390/metabo13070780. This article has 3 citations.

18. (bandari2024managementandoutcomes pages 7-8): Maria Al Bandari, Laura Nagy, Vivian Cruz, Stacy Hewson, Alomgir Hossain, and Michal Inbar-Feigenberg. Management and outcomes of very long-chain acyl-coa dehydrogenase deficiency (vlcad deficiency): a retrospective chart review. International Journal of Neonatal Screening, 10:29, Mar 2024. URL: https://doi.org/10.3390/ijns10020029, doi:10.3390/ijns10020029. This article has 11 citations.

19. (rouyer2024long‐termprognosisof pages 1-2): Alice Rouyer, Céline Tard, Anne‐Frédérique Dessein, Marco Spinazzi, Anne‐Laure Bédat‐Millet, Dalia Dimitri‐Boulos, Aleksandra Nadaj‐Pakleza, Jean‐Baptiste Chanson, Guillaume Nicolas, Claire Douillard, and Pascal Laforêt. Long‐term prognosis of fatty‐acid oxidation disorders in adults: optimism despite the limited effective therapies available. European Journal of Neurology, Nov 2024. URL: https://doi.org/10.1111/ene.16138, doi:10.1111/ene.16138. This article has 11 citations and is from a domain leading peer-reviewed journal.

20. (sebaa2023adistinctivemetabolomics media cf95c180): Rajaa Sebaa, Reem H. AlMalki, Wafaa Alseraty, and Anas M. Abdel Rahman. A distinctive metabolomics profile and potential biomarkers for very long acylcarnitine dehydrogenase deficiency (vlcadd) diagnosis in newborns. Metabolites, 13:725, Jun 2023. URL: https://doi.org/10.3390/metabo13060725, doi:10.3390/metabo13060725. This article has 13 citations.

21. (sebaa2023adistinctivemetabolomics media f4e325fd): Rajaa Sebaa, Reem H. AlMalki, Wafaa Alseraty, and Anas M. Abdel Rahman. A distinctive metabolomics profile and potential biomarkers for very long acylcarnitine dehydrogenase deficiency (vlcadd) diagnosis in newborns. Metabolites, 13:725, Jun 2023. URL: https://doi.org/10.3390/metabo13060725, doi:10.3390/metabo13060725. This article has 13 citations.

22. (bandari2024managementandoutcomes pages 2-4): Maria Al Bandari, Laura Nagy, Vivian Cruz, Stacy Hewson, Alomgir Hossain, and Michal Inbar-Feigenberg. Management and outcomes of very long-chain acyl-coa dehydrogenase deficiency (vlcad deficiency): a retrospective chart review. International Journal of Neonatal Screening, 10:29, Mar 2024. URL: https://doi.org/10.3390/ijns10020029, doi:10.3390/ijns10020029. This article has 11 citations.

23. (penaquintana2024nutritionalmanagementof pages 6-7): Luis Peña-Quintana and Patricia Correcher-Medina. Nutritional management of patients with fatty acid oxidation disorders. Nutrients, 16:2707, Aug 2024. URL: https://doi.org/10.3390/nu16162707, doi:10.3390/nu16162707. This article has 7 citations.
