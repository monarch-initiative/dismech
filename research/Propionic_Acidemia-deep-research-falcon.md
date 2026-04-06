---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T22:58:40.117673'
end_time: '2026-02-23T23:20:24.173667'
duration_seconds: 1304.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Propionic Acidemia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Propionic Acidemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Propionic Acidemia**.
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
- **Disease Name:** Propionic Acidemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Propionic Acidemia**.
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


Title: Pathophysiology of Propionic Acidemia (PA): Molecular and Cellular Mechanisms, Disease Progression, and Translational Landscape (focus 2023–2024)

1. Disease overview and key definitions

Propionic acidemia (PA; also called propionic aciduria) is an autosomal recessive “intoxication-type” organic acidemia caused by deficiency of the mitochondrial, biotin-dependent enzyme propionyl‑CoA carboxylase (PCC), which normally converts propionyl‑CoA to methylmalonyl‑CoA. Pathogenic variants in PCCA (PCC alpha subunit) or PCCB (PCC beta subunit) reduce PCC activity and lead to accumulation of propionyl‑CoA/propionate and related metabolites. (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)

A core contemporary view is that PA pathophysiology reflects (i) direct or indirect toxicity of accumulating metabolites (propionyl‑CoA and derived organic acids), plus (ii) secondary mitochondrial dysfunction with impaired energy metabolism, redox imbalance, and downstream organ vulnerability (brain, heart, kidney), even under standard-of-care metabolic control. (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2, wang2024theattenuatedhepatic pages 19-21, schumann2024renalphenotypingin pages 1-2)

MONDO ID: Not available from the retrieved evidence in this run (no source text provided a MONDO identifier for PA).

2. Core pathophysiology (molecular/cellular mechanisms)

2.1 Primary metabolic block and toxic metabolite accumulation
PCC deficiency leads to accumulation of propionyl‑CoA and downstream/alternative metabolites used clinically as biochemical markers, including propionylcarnitine (C3), 2‑methylcitric acid (2‑methylcitrate; 2MCA), propionylglycine, 3‑hydroxypropionate, and glycine. (zhang2023prevalenceofpropionic pages 1-2)

Mechanistic links between these metabolites and disease include diversion of key TCA-cycle intermediates and inhibition of mitochondrial enzymes. In particular, elevated propionyl‑CoA can compete with acetyl‑CoA at citrate synthase, and propionyl‑CoA plus oxaloacetate yields 2‑methylcitrate, which inhibits multiple TCA enzymes (citrate synthase, aconitase, isocitrate dehydrogenase), creating an anaplerotic deficit and energy failure phenotype. (zhang2023prevalenceofpropionic pages 1-2)

2.2 Mitochondrial dysfunction, TCA-cycle disruption, and oxidative stress
Multiple sources converge on secondary mitochondrial dysfunction as a central mediator of organ injury in PA, including inhibition of TCA/respiratory-chain function, oxidative stress, and energetic failure. The Atlas chapter describes that propionyl‑CoA “can inhibit the mitochondrial respiratory chain and tricarboxylic acid cycle and produce an energetic stroke,” consistent with acute neurologic decompensation and basal ganglia vulnerability. (nyhan2024propionicacidemia pages 2-4)

A key 2024 mechanistic development is an explicitly defined liver–heart axis for propionate: impaired hepatic first-pass clearance of microbiome-derived propionate increases circulating propionate, which becomes the dominant source of cardiac propionyl‑CoA load and promotes cardiac oxidative stress. In PA patients, plasma propionate was reported to vary widely (38–506 μM), supporting a plausible exposure–risk relationship for cardiac injury. (wang2024theattenuatedhepatic pages 14-15)

In the Pcca−/−(A138T) mouse model, oral propionate challenge raised plasma propionate to 132 ± 69.9 μM vs 12.1 ± 5.1 μM in wild-type, and was associated with oxidative stress readouts in heart (e.g., decreased GSH/GSSG ratio; increased methionine sulfoxide), and mild diastolic dysfunction signals. (wang2024theattenuatedhepatic pages 12-14)

2.3 Hyperammonemia mechanism (urea-cycle dysfunction via NAG/CPS1 axis)
Hyperammonemia in PA is mechanistically linked to secondary deficiency of N‑acetylglutamate (NAG), the obligate allosteric activator of carbamoyl phosphate synthetase 1 (CPS1), the irreversible rate-limiting step of the urea cycle. The 2024 expert review states that cataplerosis/CoA depletion leads to low glutamate/glutamine that “inhibits synthesis of N‑acetylglutamate (NAG),” impairing CPS1 activation and ammonia disposal. (yap2024roleofcarglumic pages 1-2)

Carglumic acid (N‑carbamylglutamate) is a synthetic NAG analog that restores urea-cycle flux by directly activating CPS1; the review states: “CGA, which acts as NAG substitution therapy, ensures continued elimination of ammonia via the urea cycle by direct allosteric activation of CPS1.” (yap2024roleofcarglumic pages 2-5)

3. Key molecular players (knowledge-base oriented)

3.1 Genes / proteins (HGNC)

Causal genes
- PCCA (HGNC: PCCA): encodes PCC alpha subunit; loss reduces PCC activity. (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)
- PCCB (HGNC: PCCB): encodes PCC beta subunit; loss reduces PCC activity. (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)

Mechanistically implicated metabolic nodes (examples)
- CPS1 (carbamoyl phosphate synthetase 1; urea cycle) as the NAG-activated, rate-limiting step affected in secondary hyperammonemia. (yap2024roleofcarglumic pages 1-2, yap2024roleofcarglumic pages 2-5)
- NAGS (N‑acetylglutamate synthase) as the producer of NAG; NAG deficiency is central to hyperammonemia rationale. (yap2024roleofcarglumic pages 1-2, head2023newinsightsinto pages 12-13)
- PGC‑1α (PPARGC1A; mitochondrial biogenesis regulator) markedly reduced in PA kidney model, linking mitochondrial quality control to CKD. (schumann2024renalphenotypingin pages 4-6)
- DRP1 (DNM1L; fission mediator) elevated in PA kidney model, shifting mitochondrial dynamics toward fission. (schumann2024renalphenotypingin pages 4-6)

3.2 Chemical entities / metabolites (CHEBI labels)
Representative relevant chemicals (CHEBI names; IDs not provided by retrieved sources)
- Propionyl‑CoA (key trapped acyl‑CoA) (zhang2023prevalenceofpropionic pages 1-2, nyhan2024propionicacidemia pages 2-4)
- Propionate / propionic acid (circulating substrate; microbiome-derived) (wang2024theattenuatedhepatic pages 14-15, wang2024theattenuatedhepatic pages 12-14)
- 2‑methylcitrate / 2‑methylcitric acid (2MCA; toxic anaplerotic/TCA inhibitor) (zhang2023prevalenceofpropionic pages 1-2, shchelochkov2024intellectualdisabilityand pages 3-5)
- Propionylcarnitine (C3; biomarker and metabolite sink) (shchelochkov2024intellectualdisabilityand pages 3-5, zhang2023prevalenceofpropionic pages 4-5)
- 3‑hydroxypropionate (urinary organic acid marker) (nyhan2024propionicacidemia pages 2-4, wang2025sixchinesepatients pages 1-2)
- Glutamine (cataplerosis marker; linked to outcomes) (shchelochkov2024intellectualdisabilityand pages 3-5, shchelochkov2024intellectualdisabilityand pages 1-2)
- N‑acetylglutamate (NAG; CPS1 activator) and carglumic acid (NAG analog therapy) (yap2024roleofcarglumic pages 1-2, yap2024roleofcarglumic pages 2-5)

3.3 Cell types (CL term labels)
- Hepatocyte (site of major propionate clearance; hepatic PCC deficiency drives systemic propionate) (wang2024theattenuatedhepatic pages 14-15, wang2024theattenuatedhepatic pages 12-14)
- Cardiomyocyte (target of propionate-driven CoA trapping/oxidative stress; cardiomyopathy/arrhythmia substrate) (wang2024theattenuatedhepatic pages 19-21, wang2024theattenuatedhepatic pages 12-14)
- Neuron and astrocyte (CNS excitotoxicity/energetic failure; basal ganglia vulnerability; astrocytic glutamine/glutamate axis in hyperammonemia) (nyhan2024propionicacidemia pages 1-2)
- Renal tubular epithelial cell (proximal/distal tubule mitochondrial network disruption; CKD progression) (schumann2024renalphenotypingin pages 1-2, schumann2024renalphenotypingin pages 6-7)

3.4 Anatomical locations (UBERON term labels)
- Liver (first-pass propionate metabolism; key modifier of systemic propionate burden) (wang2024theattenuatedhepatic pages 14-15, wang2024theattenuatedhepatic pages 12-14)
- Heart (dilated cardiomyopathy, long-QT, arrhythmia) (maines2023understandingthepathogenesis pages 2-4, passantino2023cardiacinvolvementin pages 1-2)
- Brain, especially basal ganglia/striatum (metabolic-stroke-like injury, movement disorders) (nyhan2024propionicacidemia pages 1-2, nyhan2024propionicacidemia pages 2-4)
- Kidney (progressive CKD; tubular injury; mitochondrial quality control defects) (schumann2024renalphenotypingin pages 1-2, schumann2024renalphenotypingin pages 4-6)

4. Dysregulated pathways and biological processes (GO-oriented)

Representative disrupted processes (GO term labels)
- Propionate metabolic process / propionyl‑CoA metabolic process (primary enzymatic block at PCC) (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)
- Tricarboxylic acid cycle (TCA cycle) and anaplerotic processes (oxaloacetate diversion to methylcitrate; reduced succinyl‑CoA replenishment) (zhang2023prevalenceofpropionic pages 1-2, maines2023understandingthepathogenesis pages 2-4)
- Mitochondrial electron transport / oxidative phosphorylation (secondary OXPHOS dysfunction across organs; energetic deficiency) (nyhan2024propionicacidemia pages 2-4, maines2023understandingthepathogenesis pages 5-7)
- Cellular response to oxidative stress / redox homeostasis (heart and kidney oxidative stress markers and antioxidant response) (wang2024theattenuatedhepatic pages 12-14, schumann2024renalphenotypingin pages 1-2)
- Mitochondrial fission / fusion and mitophagy (kidney model: fission up, fusion/mitophagy down) (schumann2024renalphenotypingin pages 4-6)
- Urea cycle / ammonia detoxification (secondary NAG deficiency and CPS1 activation failure) (yap2024roleofcarglumic pages 1-2, yap2024roleofcarglumic pages 2-5)

5. Cellular components (where processes occur)

Core subcellular localization
- Mitochondrial matrix (PCC and TCA cycle; propionyl‑CoA trapping; urea-cycle-related NAGS/CPS1 activation in liver mitochondria is implicated by mechanism) (nyhan2024propionicacidemia pages 1-2, head2023newinsightsinto pages 12-13)
- Mitochondrial inner membrane / respiratory chain (OXPHOS inhibition and energetic failure) (nyhan2024propionicacidemia pages 2-4, maines2023understandingthepathogenesis pages 5-7)

6. Disease progression model (sequence from trigger to phenotype)

6.1 Initiation and acute decompensation
Primary trigger: catabolic stress (infection/fasting) increases propiogenic substrate flux (branched-chain amino acids, odd-chain fatty acids, gut-derived propionate), overwhelming residual PCC capacity and increasing toxic metabolite load, causing metabolic acidosis and hyperammonemia. Clinically, PA presents in neonatal vs later-onset forms; early-onset cases can show rapid acute deterioration soon after birth. (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)

Mechanistic cascade: metabolite accumulation → TCA/OXPHOS inhibition → ATP deficit and oxidative stress → organ dysfunction. Hyperammonemia contributes to neurotoxicity, with astrocytic glutamine/glutamate shifts contributing to excitotoxic injury. (nyhan2024propionicacidemia pages 1-2, nyhan2024propionicacidemia pages 2-4)

6.2 Chronic disease evolution
Despite improved survival, long-term neurologic morbidity may persist; the Atlas chapter notes that early strategies improved survival “but has not modified neurodevelopment.” (nyhan2024propionicacidemia pages 2-4)

End-organ progression may be driven by sustained mitochondrial stress/quality-control failure. For example, in the kidney, a murine hypomorphic Pcca model shows progressive injury with mitochondrial network disorganization, increased fission, reduced mitophagy, and reduced PGC‑1α. (schumann2024renalphenotypingin pages 1-2, schumann2024renalphenotypingin pages 4-6)

7. Phenotypic manifestations and mechanism links (HP-oriented)

CNS
- Intellectual disability and autism spectrum disorder: In an NIH cohort (n=33), 61% had intellectual disability and 39% had ASD. ID severity was associated with higher propionylcarnitine and total 2‑methylcitrate, elevated mitochondrial stress biomarkers FGF21 and GDF15, and reduced in vivo 1‑13C‑propionate oxidation; ASD associated mainly with erythropoietin and glutamine changes. These findings support a model where biochemical severity and mitochondrial dysfunction contribute to CNS outcomes. (shchelochkov2024intellectualdisabilityand pages 1-2, shchelochkov2024intellectualdisabilityand pages 3-5)
- Basal ganglia lesions / movement disorders (“metabolic stroke”-like): basal ganglia are described as particularly vulnerable, with movement disorders linked to endothelial and neuronal toxicity. (nyhan2024propionicacidemia pages 1-2)

Heart
- Cardiomyopathy and arrhythmia: PA is associated with DCM and acquired long-QT; a 2023 review summarizes DCM prevalence around ~23% in one cohort and cardiomyopathy prevalence 39% in another, with arrhythmia/aLQTS prevalence reported across series. (maines2023understandingthepathogenesis pages 2-4, maines2023understandingthepathogenesis pages 1-2)
- Pediatric outcome data: In a pediatric organic aciduria cohort, 5-year major adverse cardiac event rate was 55% in PA patients with cardiomyopathy, and liver transplantation performed for worsening cardiac impairment stabilized metabolic status and cardiac function in transplanted patients. (passantino2023cardiacinvolvementin pages 1-2)
- Mechanistic link: propionate-driven CoA trapping and impaired anaplerosis/TCA fuel delivery with oxidative stress/mitochondrial dysfunction. (maines2023understandingthepathogenesis pages 2-4, wang2024theattenuatedhepatic pages 12-14)

Kidney
- CKD: PA is associated with chronic kidney disease; one 2024 murine phenotyping paper notes that CKD can begin in childhood and that ~50% of adults have GFR <60 mL/min, consistent with clinically significant progressive nephropathy. (schumann2024renalphenotypingin pages 1-2)

8. Recent developments and latest research (prioritizing 2023–2024)

8.1 2024: Liver–heart axis for circulating propionate and cardiac oxidative stress
Wang et al. (Jul 2024) provide mechanistic evidence that gut microbiome-derived circulating propionate is the dominant source of cardiac propionyl‑CoA (~74% in their tracing context), and that attenuated hepatic clearance increases systemic propionate and cardiac oxidative stress. The work includes quantitative human plasma propionate ranges (38–506 μM) and mouse challenge data (132 ± 69.9 μM vs 12.1 ± 5.1 μM WT). (wang2024theattenuatedhepatic pages 14-15, wang2024theattenuatedhepatic pages 12-14)

8.2 2024: Biomarker–behavior links implicating mitochondrial dysfunction in CNS outcomes
Shchelochkov et al. (Jan 2024) quantified neurodevelopmental burden and identified associations between ID and biochemical/mitochondrial biomarkers (propionylcarnitine, 2‑methylcitrate, FGF21, GDF15, erythropoietin, glutamine, 1‑13C‑propionate oxidation). This supports biomarker-driven stratification and reinforces mitochondrial biology as a mechanistic bridge from metabolic block to neurodevelopmental phenotype. (shchelochkov2024intellectualdisabilityand pages 1-2, shchelochkov2024intellectualdisabilityand pages 3-5, shchelochkov2024intellectualdisabilityand pages 5-6)

8.3 2024: Renal mitochondrial quality-control mechanisms as candidate drivers of CKD
Schumann et al. (Dec 2024) demonstrate renal mitochondrial-network alterations, oxidative stress activation, TCA-cycle metabolic signatures, increased fission (Drp1 ~threefold), reduced fusion proteins (OPA1 ~0.4-fold; Mfn1/2 ~0.5-fold), reduced PINK1 (~0.3–0.5-fold), and reduced PGC‑1α (~0.7-fold) in a hypomorphic Pcca model, implicating mitochondrial dynamics and impaired mitophagy as actionable mechanistic nodes. (schumann2024renalphenotypingin pages 4-6)

9. Current applications and real-world implementations

9.1 Newborn screening (NBS) and diagnosis
Primary NBS markers include elevated propionylcarnitine (C3) and increased C3/C2 ratio. A 2023 review reports typical screening reference ranges of C3 = 0.2–4.3 μmol/L and C3/C2 = 0.03–0.2, and notes confirmatory urine organic-acid markers (2‑methylcitrate, 3‑hydroxypropionate, propionylglycine). (zhang2023prevalenceofpropionic pages 2-4, wang2025sixchinesepatients pages 1-2)

Epidemiology: the 2023 China review reports wide global incidence ranges (e.g., US ~1/105,000–1/130,000) and variable incidences across regions and Chinese provinces, highlighting dependence on screening scope and population genetics. (zhang2023prevalenceofpropionic pages 4-5, zhang2023prevalenceofpropionic pages 5-7)

9.2 Nutritional and medical management
Standard chronic management includes energy support and protein restriction by oral/enteral nutrition with individualized titration to maximize natural protein while maintaining metabolic stability. (yap2024roleofcarglumic pages 9-10, yap2024roleofcarglumic pages 2-5)

9.3 Hyperammonemia: carglumic acid (carglumic acid / N‑carbamylglutamate)
Mechanism: Carglumic acid is a NAG analog that allosterically activates CPS1 to restore ureagenesis. (yap2024roleofcarglumic pages 1-2, yap2024roleofcarglumic pages 2-5)

Clinical effectiveness (long-term): the 2024 expert review summarizes evidence that adding carglumic acid to dietary management can reduce acute decompensations and hospital use; reported outcomes include a 51% reduction in emergency room admissions over 2 years and fewer inpatient days (32.8 vs 51.3). (yap2024roleofcarglumic pages 2-5)

Trial/real-world quantitative data include an open-label randomized study reporting reduced hospitalizations (1.2 vs 4.3; p=0.013) and lower plasma ammonia (means reported as 69.6 vs 55.3 μmol/L in evaluable patients) with long-term dosing, and Table 1 summarizes multiple long-term studies and NCT identifiers. (yap2024roleofcarglumic pages 5-6, yap2024roleofcarglumic media 5814ca18)

9.4 Liver transplantation
Liver transplantation is used for selected severe phenotypes and can stabilize metabolic status and, in some cases, cardiac function; however it is not curative and does not eliminate all metabolite abnormalities or organ risks. (passantino2023cardiacinvolvementin pages 1-2, yap2024roleofcarglumic pages 10-12)

9.5 Emerging disease-modifying therapies
mRNA therapy: The 2024 review reports an ongoing phase I/II trial of mRNA-3927 with 16 patients enrolled and interim data suggesting ~70% reduction in risk of metabolic decompensation events among eight patients with prior events. (yap2024roleofcarglumic pages 10-12, yap2024roleofcarglumic pages 9-10)

10. Expert interpretation and analysis (authoritative synthesis)

Cardiac disease in PA appears multifactorial, integrating impaired TCA substrate delivery/anaplerosis, CoA trapping, mitochondrial dysfunction, oxidative stress, and additional modifiers (e.g., CoQ10 status, neurohormonal activation). The 2023 cardiac-focused review emphasizes that “multiple cellular pathways” are involved and argues for therapies that target dysregulated mechanisms beyond merely correcting the enzymatic defect. (maines2023understandingthepathogenesis pages 2-4)

The 2024 liver–heart axis work reframes cardiac risk toward systemic propionate exposure (microbiome-derived plus impaired hepatic clearance), suggesting that interventions reducing circulating propionate and improving hepatic disposal could have direct cardioprotective effects. (wang2024theattenuatedhepatic pages 15-17, wang2024theattenuatedhepatic pages 12-14)

11. Evidence items (PMID-oriented)

PMIDs were not available in the tool-returned evidence snippets for the key 2023–2024 articles in this run. The report therefore cites each source using DOI URLs and PaperQA context IDs. (zhang2023prevalenceofpropionic pages 1-2, maines2023understandingthepathogenesis pages 2-4, wang2024theattenuatedhepatic pages 14-15, shchelochkov2024intellectualdisabilityand pages 3-5, schumann2024renalphenotypingin pages 4-6, yap2024roleofcarglumic pages 2-5)

12. Ontology-oriented annotation summary (for knowledge-base ingestion)

Disease entity
- Propionic acidemia / propionic aciduria (genetic organic acidemia) (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)

Causal genes (HGNC)
- PCCA; PCCB (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)

Representative disrupted GO biological processes (labels)
- Propionyl-CoA metabolic process; propionate metabolic process (nyhan2024propionicacidemia pages 1-2, zhang2023prevalenceofpropionic pages 1-2)
- Tricarboxylic acid cycle; anaplerotic processes (zhang2023prevalenceofpropionic pages 1-2, maines2023understandingthepathogenesis pages 2-4)
- Oxidative phosphorylation; mitochondrial electron transport (nyhan2024propionicacidemia pages 2-4, maines2023understandingthepathogenesis pages 5-7)
- Response to oxidative stress / redox homeostasis (wang2024theattenuatedhepatic pages 12-14, schumann2024renalphenotypingin pages 1-2)
- Mitophagy; mitochondrial fission/fusion dynamics (schumann2024renalphenotypingin pages 4-6)
- Urea cycle / ammonia detoxification (CPS1 activation via NAG) (yap2024roleofcarglumic pages 1-2, yap2024roleofcarglumic pages 2-5)

Representative cellular components (labels)
- Mitochondrial matrix; mitochondrial inner membrane (nyhan2024propionicacidemia pages 1-2, nyhan2024propionicacidemia pages 2-4)

Representative phenotypes (HP term labels)
- Metabolic acidosis; hyperammonemia; developmental delay/intellectual disability; autism spectrum disorder; cardiomyopathy; long QT/arrhythmia; basal ganglia lesions; chronic kidney disease. (nyhan2024propionicacidemia pages 1-2, shchelochkov2024intellectualdisabilityand pages 1-2, passantino2023cardiacinvolvementin pages 1-2, schumann2024renalphenotypingin pages 1-2)

Representative cell types (CL term labels)
- Hepatocyte; cardiomyocyte; neuron; astrocyte; renal tubular epithelial cell. (nyhan2024propionicacidemia pages 1-2, wang2024theattenuatedhepatic pages 12-14, schumann2024renalphenotypingin pages 4-6)

Representative anatomical sites (UBERON term labels)
- Liver; heart; basal ganglia/brain; kidney tubules. (nyhan2024propionicacidemia pages 1-2, wang2024theattenuatedhepatic pages 14-15, schumann2024renalphenotypingin pages 4-6)

Representative chemicals (CHEBI labels)
- Propionyl‑CoA; propionate; 2‑methylcitrate; propionylcarnitine; 3‑hydroxypropionate; glutamine; N‑acetylglutamate; carglumic acid. (zhang2023prevalenceofpropionic pages 1-2, shchelochkov2024intellectualdisabilityand pages 3-5, yap2024roleofcarglumic pages 2-5)

Key URLs and publication dates (selected)
- Zhang et al. “Prevalence of propionic acidemia in China.” Orphanet J Rare Dis. Sep 2023. https://doi.org/10.1186/s13023-023-02898-w (zhang2023prevalenceofpropionic pages 4-5)
- Maines et al. “Understanding the Pathogenesis of Cardiac Complications in… Propionic Acidemia…” Metabolites. Apr 2023. https://doi.org/10.3390/metabo13040563 (maines2023understandingthepathogenesis pages 2-4)
- Shchelochkov et al. “Intellectual disability and autism in propionic acidemia…” Molecular Psychiatry. Jan 2024. https://doi.org/10.1038/s41380-023-02385-5 (shchelochkov2024intellectualdisabilityand pages 1-2)
- Wang et al. “The attenuated hepatic clearance of propionate increases cardiac oxidative stress in propionic acidemia.” Basic Res Cardiol. Jul 2024. https://doi.org/10.1007/s00395-024-01066-w (wang2024theattenuatedhepatic pages 12-14)
- Schumann et al. “Renal phenotyping in a hypomorphic murine model of propionic aciduria…” Scientific Reports. Dec 2024. https://doi.org/10.1038/s41598-024-79572-z (schumann2024renalphenotypingin pages 1-2)
- Yap et al. “Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias.” Orphanet J Rare Dis. Dec 2024. https://doi.org/10.1186/s13023-024-03468-4 (yap2024roleofcarglumic pages 2-5)



References

1. (nyhan2024propionicacidemia pages 1-2): W. Nyhan, G. Hoffmann, A. Al-aqeel, and B. Barshop. Propionic acidemia. Atlas of Inherited Metabolic Diseases, Feb 2024. URL: https://doi.org/10.1016/b978-0-12-374105-9.00373-7, doi:10.1016/b978-0-12-374105-9.00373-7. This article has 75 citations.

2. (zhang2023prevalenceofpropionic pages 1-2): Yixing Zhang, Chuwen Peng, Lifang Wang, Sitong Chen, Junwei Wang, Ziheng Tian, Chuangong Wang, Xiaoxin Chen, Suhong Zhu, Guo-Fang Zhang, and You Wang. Prevalence of propionic acidemia in china. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02898-w, doi:10.1186/s13023-023-02898-w. This article has 19 citations and is from a peer-reviewed journal.

3. (wang2024theattenuatedhepatic pages 19-21): You Wang, Suhong Zhu, Wentao He, Hannah Marchuk, Eva Richard, Lourdes R. Desviat, Sarah P. Young, Dwight Koeberl, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. The attenuated hepatic clearance of propionate increases cardiac oxidative stress in propionic acidemia. Basic research in cardiology, 119:1045-1062, Jul 2024. URL: https://doi.org/10.1007/s00395-024-01066-w, doi:10.1007/s00395-024-01066-w. This article has 8 citations and is from a domain leading peer-reviewed journal.

4. (schumann2024renalphenotypingin pages 1-2): Anke Schumann, Ainhoa Martinez-Pizarro, Eva Richard, Christoph Schell, Anna Laura Kössinger, Karina A. Zeyer, Stefan Tholen, Oliver Schilling, Michael Barry, Björn Neubauer, Michael Köttgen, Luciana Hannibal, Lourdes R. Desviat, and Ute Spiekerkötter. Renal phenotyping in a hypomorphic murine model of propionic aciduria reveals common pathomechanisms in organic acidurias. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-79572-z, doi:10.1038/s41598-024-79572-z. This article has 0 citations and is from a peer-reviewed journal.

5. (nyhan2024propionicacidemia pages 2-4): W. Nyhan, G. Hoffmann, A. Al-aqeel, and B. Barshop. Propionic acidemia. Atlas of Inherited Metabolic Diseases, Feb 2024. URL: https://doi.org/10.1016/b978-0-12-374105-9.00373-7, doi:10.1016/b978-0-12-374105-9.00373-7. This article has 75 citations.

6. (wang2024theattenuatedhepatic pages 14-15): You Wang, Suhong Zhu, Wentao He, Hannah Marchuk, Eva Richard, Lourdes R. Desviat, Sarah P. Young, Dwight Koeberl, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. The attenuated hepatic clearance of propionate increases cardiac oxidative stress in propionic acidemia. Basic research in cardiology, 119:1045-1062, Jul 2024. URL: https://doi.org/10.1007/s00395-024-01066-w, doi:10.1007/s00395-024-01066-w. This article has 8 citations and is from a domain leading peer-reviewed journal.

7. (wang2024theattenuatedhepatic pages 12-14): You Wang, Suhong Zhu, Wentao He, Hannah Marchuk, Eva Richard, Lourdes R. Desviat, Sarah P. Young, Dwight Koeberl, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. The attenuated hepatic clearance of propionate increases cardiac oxidative stress in propionic acidemia. Basic research in cardiology, 119:1045-1062, Jul 2024. URL: https://doi.org/10.1007/s00395-024-01066-w, doi:10.1007/s00395-024-01066-w. This article has 8 citations and is from a domain leading peer-reviewed journal.

8. (yap2024roleofcarglumic pages 1-2): Sufin Yap, Serena Gasperini, Shirou Matsumoto, and François Feillet. Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03468-4, doi:10.1186/s13023-024-03468-4. This article has 5 citations and is from a peer-reviewed journal.

9. (yap2024roleofcarglumic pages 2-5): Sufin Yap, Serena Gasperini, Shirou Matsumoto, and François Feillet. Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03468-4, doi:10.1186/s13023-024-03468-4. This article has 5 citations and is from a peer-reviewed journal.

10. (head2023newinsightsinto pages 12-13): PamelaSara E. Head, Jordan L. Meier, and Charles P. Venditti. New insights into the pathophysiology of methylmalonic acidemia. Journal of Inherited Metabolic Disease, 46:436-449, May 2023. URL: https://doi.org/10.1002/jimd.12617, doi:10.1002/jimd.12617. This article has 38 citations and is from a peer-reviewed journal.

11. (schumann2024renalphenotypingin pages 4-6): Anke Schumann, Ainhoa Martinez-Pizarro, Eva Richard, Christoph Schell, Anna Laura Kössinger, Karina A. Zeyer, Stefan Tholen, Oliver Schilling, Michael Barry, Björn Neubauer, Michael Köttgen, Luciana Hannibal, Lourdes R. Desviat, and Ute Spiekerkötter. Renal phenotyping in a hypomorphic murine model of propionic aciduria reveals common pathomechanisms in organic acidurias. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-79572-z, doi:10.1038/s41598-024-79572-z. This article has 0 citations and is from a peer-reviewed journal.

12. (shchelochkov2024intellectualdisabilityand pages 3-5): Oleg A. Shchelochkov, Cristan A. Farmer, Colby Chlebowski, Dee Adedipe, Susan Ferry, Irini Manoli, Alexandra Pass, Samantha McCoy, Carol Van Ryzin, Jennifer Sloan, Audrey Thurm, and Charles P. Venditti. Intellectual disability and autism in propionic acidemia: a biomarker-behavioral investigation implicating dysregulated mitochondrial biology. Molecular Psychiatry, 29:974-981, Jan 2024. URL: https://doi.org/10.1038/s41380-023-02385-5, doi:10.1038/s41380-023-02385-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

13. (zhang2023prevalenceofpropionic pages 4-5): Yixing Zhang, Chuwen Peng, Lifang Wang, Sitong Chen, Junwei Wang, Ziheng Tian, Chuangong Wang, Xiaoxin Chen, Suhong Zhu, Guo-Fang Zhang, and You Wang. Prevalence of propionic acidemia in china. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02898-w, doi:10.1186/s13023-023-02898-w. This article has 19 citations and is from a peer-reviewed journal.

14. (wang2025sixchinesepatients pages 1-2): Shunan Wang, Lulu Li, Yulan Ma, Hai-he Yang, Yuting Sang, Yueling Tang, L. Gong, Jin-qi Zhao, Lijin Gu, Yuanyuan Kong, and Xinmei Mao. Six chinese patients with propionic acidemia: from asymptomatic to death in the neonatal period. Orphanet Journal of Rare Diseases, Mar 2025. URL: https://doi.org/10.1186/s13023-025-03622-6, doi:10.1186/s13023-025-03622-6. This article has 0 citations and is from a peer-reviewed journal.

15. (shchelochkov2024intellectualdisabilityand pages 1-2): Oleg A. Shchelochkov, Cristan A. Farmer, Colby Chlebowski, Dee Adedipe, Susan Ferry, Irini Manoli, Alexandra Pass, Samantha McCoy, Carol Van Ryzin, Jennifer Sloan, Audrey Thurm, and Charles P. Venditti. Intellectual disability and autism in propionic acidemia: a biomarker-behavioral investigation implicating dysregulated mitochondrial biology. Molecular Psychiatry, 29:974-981, Jan 2024. URL: https://doi.org/10.1038/s41380-023-02385-5, doi:10.1038/s41380-023-02385-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

16. (schumann2024renalphenotypingin pages 6-7): Anke Schumann, Ainhoa Martinez-Pizarro, Eva Richard, Christoph Schell, Anna Laura Kössinger, Karina A. Zeyer, Stefan Tholen, Oliver Schilling, Michael Barry, Björn Neubauer, Michael Köttgen, Luciana Hannibal, Lourdes R. Desviat, and Ute Spiekerkötter. Renal phenotyping in a hypomorphic murine model of propionic aciduria reveals common pathomechanisms in organic acidurias. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-79572-z, doi:10.1038/s41598-024-79572-z. This article has 0 citations and is from a peer-reviewed journal.

17. (maines2023understandingthepathogenesis pages 2-4): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 5 citations.

18. (passantino2023cardiacinvolvementin pages 1-2): Silvia Passantino, Serena Chiellino, Francesca Girolami, Mattia Zampieri, Giovanni Calabri, Gaia Spaziani, Elena Bennati, Giulio Porcedda, Elena Procopio, Iacopo Olivotto, and Silvia Favilli. Cardiac involvement in classical organic acidurias: clinical profile and outcome in a pediatric cohort. Diagnostics, 13:3674, Dec 2023. URL: https://doi.org/10.3390/diagnostics13243674, doi:10.3390/diagnostics13243674. This article has 1 citations.

19. (maines2023understandingthepathogenesis pages 5-7): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 5 citations.

20. (maines2023understandingthepathogenesis pages 1-2): Evelina Maines, Michele Moretti, Nicola Vitturi, Giorgia Gugelmo, Ilaria Fasan, Livia Lenzini, Giovanni Piccoli, Vincenza Gragnaniello, Arianna Maiorana, Massimo Soffiati, Alberto Burlina, and Roberto Franceschi. Understanding the pathogenesis of cardiac complications in patients with propionic acidemia and exploring therapeutic alternatives for those who are not eligible or are waiting for liver transplantation. Metabolites, 13(4):563, Apr 2023. URL: https://doi.org/10.3390/metabo13040563, doi:10.3390/metabo13040563. This article has 5 citations.

21. (shchelochkov2024intellectualdisabilityand pages 5-6): Oleg A. Shchelochkov, Cristan A. Farmer, Colby Chlebowski, Dee Adedipe, Susan Ferry, Irini Manoli, Alexandra Pass, Samantha McCoy, Carol Van Ryzin, Jennifer Sloan, Audrey Thurm, and Charles P. Venditti. Intellectual disability and autism in propionic acidemia: a biomarker-behavioral investigation implicating dysregulated mitochondrial biology. Molecular Psychiatry, 29:974-981, Jan 2024. URL: https://doi.org/10.1038/s41380-023-02385-5, doi:10.1038/s41380-023-02385-5. This article has 13 citations and is from a highest quality peer-reviewed journal.

22. (zhang2023prevalenceofpropionic pages 2-4): Yixing Zhang, Chuwen Peng, Lifang Wang, Sitong Chen, Junwei Wang, Ziheng Tian, Chuangong Wang, Xiaoxin Chen, Suhong Zhu, Guo-Fang Zhang, and You Wang. Prevalence of propionic acidemia in china. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02898-w, doi:10.1186/s13023-023-02898-w. This article has 19 citations and is from a peer-reviewed journal.

23. (zhang2023prevalenceofpropionic pages 5-7): Yixing Zhang, Chuwen Peng, Lifang Wang, Sitong Chen, Junwei Wang, Ziheng Tian, Chuangong Wang, Xiaoxin Chen, Suhong Zhu, Guo-Fang Zhang, and You Wang. Prevalence of propionic acidemia in china. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02898-w, doi:10.1186/s13023-023-02898-w. This article has 19 citations and is from a peer-reviewed journal.

24. (yap2024roleofcarglumic pages 9-10): Sufin Yap, Serena Gasperini, Shirou Matsumoto, and François Feillet. Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03468-4, doi:10.1186/s13023-024-03468-4. This article has 5 citations and is from a peer-reviewed journal.

25. (yap2024roleofcarglumic pages 5-6): Sufin Yap, Serena Gasperini, Shirou Matsumoto, and François Feillet. Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03468-4, doi:10.1186/s13023-024-03468-4. This article has 5 citations and is from a peer-reviewed journal.

26. (yap2024roleofcarglumic media 5814ca18): Sufin Yap, Serena Gasperini, Shirou Matsumoto, and François Feillet. Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03468-4, doi:10.1186/s13023-024-03468-4. This article has 5 citations and is from a peer-reviewed journal.

27. (yap2024roleofcarglumic pages 10-12): Sufin Yap, Serena Gasperini, Shirou Matsumoto, and François Feillet. Role of carglumic acid in the long-term management of propionic and methylmalonic acidurias. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03468-4, doi:10.1186/s13023-024-03468-4. This article has 5 citations and is from a peer-reviewed journal.

28. (wang2024theattenuatedhepatic pages 15-17): You Wang, Suhong Zhu, Wentao He, Hannah Marchuk, Eva Richard, Lourdes R. Desviat, Sarah P. Young, Dwight Koeberl, Takhar Kasumov, Xiaoxin Chen, and Guo-Fang Zhang. The attenuated hepatic clearance of propionate increases cardiac oxidative stress in propionic acidemia. Basic research in cardiology, 119:1045-1062, Jul 2024. URL: https://doi.org/10.1007/s00395-024-01066-w, doi:10.1007/s00395-024-01066-w. This article has 8 citations and is from a domain leading peer-reviewed journal.
