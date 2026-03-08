---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T22:58:40.117308'
end_time: '2026-02-23T23:14:09.452483'
duration_seconds: 929.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glutaric Aciduria
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Glutaric Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Glutaric Aciduria**.
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
- **Disease Name:** Glutaric Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Glutaric Aciduria**.
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


Comprehensive Pathophysiology Research Report: Glutaric Aciduria (primarily Glutaric Aciduria Type 1, GA1)

Publication scope note
“Glutaric aciduria” can refer to multiple disorders (e.g., GA1 vs GA2/MADD). The mechanistic literature and screening/therapy evidence retrieved here overwhelmingly concern glutaric aciduria type 1 (GA1; glutaric acidemia type I), a lysine/hydroxylysine/tryptophan catabolic defect due to GCDH deficiency. Where the report states “glutaric aciduria,” it refers to GA1 unless noted otherwise. (barzi2023rescueofglutaric pages 1-3, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

Identifiers
- Disease: Glutaric aciduria type 1 (GA1; glutaric acidemia type I). (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, oh2024glutaricaciduriatype pages 1-3)
- OMIM is explicitly referenced as “MIM #231670” in newborn screening genetic second-tier implementation contexts for GA1, indicating established Mendelian disease mapping. (zaunseder2024digitaltierstrategyimproves pages 8-10)
- MONDO ID: not available in the retrieved evidence and therefore not asserted.

1. Key concepts and definitions (current understanding)

1.1 Core biochemical definition
GA1 is an autosomal recessive inborn error of metabolism caused by deficiency of glutaryl‑CoA dehydrogenase (GCDH), a mitochondrial flavoprotein enzyme in lysine/hydroxylysine/tryptophan catabolism. (mateubosch2024systemicdeliveryof pages 1-2, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
- Barroso et al. define GA1 as “an autosomal recessive deficiency of glutaryl‑CoA dehydrogenase (GCDH), a mitochondrial flavoprotein that converts glutaryl‑CoA to crotonyl‑CoA and CO2.” (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

1.2 Key accumulating/toxic metabolites (biochemical footprint)
The metabolic block leads to accumulation of glutaric acid (GA), 3‑hydroxyglutaric acid (3OHGA/3‑OH‑GA), and glutarylcarnitine (C5DC). (mateubosch2024systemicdeliveryof pages 1-2, barzi2023rescueofglutaric pages 1-3, chen2024clinicalfeaturesand pages 1-2)
- Chen et al.: GCDH deficiency causes “the accumulation of glutaric acid (GA), 3-hydroxyglutaric acid (3OHGA), and glutaryl carnitine (C5DC) in body tissues.” (chen2024clinicalfeaturesand pages 1-2)

1.3 Pathway context (lysine catabolism)
A schematic of lysine catabolism and the GCDH block (with GA and 3‑OH‑GA accumulation) is provided in Barzi et al. (Science Translational Medicine, 2023). (barzi2023rescueofglutaric media 22490951)

1.4 Biochemical subtypes (high vs low excretors)
Clinical practice stratifies GA1 into high‑ and low‑excretor phenotypes based on urinary GA excretion (e.g., “high (>100 mmol/molCrea) and low excretors (≤100 mmol/molCrea)”). These subtypes track residual enzyme function and have prognostic relevance. (zaunseder2024digitaltierstrategyimproves pages 1-2, martner2021thebiochemicalsubtype pages 1-2)

2. Core pathophysiology: molecular and cellular mechanisms

2.1 Proximal mechanism: metabolite accumulation → selective brain vulnerability
Untreated individuals “mostly develop striatal injury between the age 3–36 months,” leading to “a complex movement disorder (MD) with predominant dystonia due to bilateral striatal damage.” (martner2021thebiochemicalsubtype pages 1-2)
Striatal/basal ganglia injury is a central clinicopathologic hallmark across clinical and experimental evidence. (mateubosch2024systemicdeliveryof pages 1-2, bian2023glutaricaciduriatype pages 3-5)

2.2 Neurotoxic mechanisms (current mechanistic model)
A convergent mechanistic model supported by mouse brain studies and clinical synthesis includes excitotoxicity, oxidative stress, neuroinflammation, and mitochondrial/ER stress.

2.2.1 Excitotoxicity and inhibitory neurotransmission impairment
- Chen et al. propose that accumulated GA/3OHGA, being structurally similar to glutamate, overactivate glutamatergic signaling and reduce inhibitory tone: glutamate receptor overactivation “inhibits the synthesis of gamma-aminobutyric acid (GABA), resulting in diminished inhibitory neurotransmission and the induction of oxidative stress responses.” (chen2024clinicalfeaturesand pages 1-2)
- Epilepsy-focused review notes downstream excitotoxicity/oxidative stress and carnitine depletion mechanisms in GA1. (shi2024disordersoforganic pages 7-8)

2.2.2 Mitochondrial energy metabolism impairment
- Chen et al. report that GA and 3OHGA “can inhibit neuronal alpha-ketoglutarate dehydrogenase,” leading to disturbed energy metabolism and neuronal injury. (chen2024clinicalfeaturesand pages 1-2)

2.2.3 Oxidative stress and redox imbalance (in vivo brain evidence)
In a Gcdh−/− mouse model, oxidative damage and antioxidant depletion are observed in striatum and cortex under lysine overload: “MDA levels were increased and GSH concentrations decreased in the striatum and cerebral cortex.” (seminotti2022disturbanceofmitochondrial pages 10-12)

2.2.4 Neuroinflammation and NF-κB signaling (in vivo brain evidence)
Seminotti et al. report neuroinflammation with microglial marker changes and canonical inflammatory transcriptional activation: “augmented Iba-1 staining; increased nuclear NF-κB with decreased cytosolic IκBα.” (seminotti2022disturbanceofmitochondrial pages 1-2)

2.2.5 Mitochondrial dynamics and ER–mitochondria contact-site dysfunction
Seminotti et al. show altered mitochondrial fission/fusion balance and impaired ER–mitochondria crosstalk:
- “DRP1 content was significantly elevated… indicating a disturbance in mitochondrial fission.” (seminotti2022disturbanceofmitochondrial pages 10-12)
- ER–mitochondria tethering/communication proteins were reduced: “significant decrease of IP3R and VDAC1 contents,” consistent with “disturbance of ER–mitochondria crosstalk,” and ER stress marker DDIT3 was increased. (seminotti2022disturbanceofmitochondrial pages 10-12)

2.3 A major recent conceptual shift (2023): liver–brain toxic metabolite axis
A key development is the challenge to the long-held view that neurotoxic catabolites in GA1 are produced locally in brain and do not cross the blood–brain barrier. Barzi et al. report that in mice, GA and 3‑OH‑GA can cross the BBB and that brain catabolites originate from liver; liver-directed interventions rescue the neurologic/lethal phenotype. (barzi2023rescueofglutaric pages 1-3)
This finding reframes GA1 as, at least in part, a systemic-to-brain metabolic intoxication where hepatic production and inter-organ transport contribute materially to brain injury risk. (barzi2023rescueofglutaric pages 1-3)

3. Key molecular players and entities (knowledge base–ready)

3.1 Genes/proteins (HGNC-style symbols)
- GCDH (glutaryl‑CoA dehydrogenase): causal gene; mitochondrial enzyme; deficiency is primary defect. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, chen2024clinicalfeaturesand pages 1-2)
- SUGCT (succinyl‑CoA:glutarate‑CoA transferase; also referred to as C7orf10): proposed modifier/targetable enzyme in glutarate handling; authors propose it could modulate GA1 biochemical phenotype by diverting intermediates. (wu2024characterizationstructureand pages 1-3)
- AASS (aminoadipate‑semialdehyde synthase): upstream lysine catabolic enzyme; CRISPR deletion in liver was used to reduce flux through lysine degradation and rescue phenotype in GA1 mice. (barzi2023rescueofglutaric pages 1-3)

3.2 Protein-level molecular disease mechanism (GCDH misfolding)
A 2023 mechanistic study supports GA1 as a protein-misfolding disorder for many missense variants.
- Barroso et al. report variant-mediated “altered oligomerization, loss of protein stability and solubility… augmented susceptibility to aggregation,” and that “reduced cellular activity was associated with loss of tetramerization.” (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
This supports a disease axis beyond “loss of catalytic activity,” implicating proteostasis and quaternary structure stabilization as therapeutic opportunities. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

3.3 Chemical entities (CHEBI-style)
- Glutaric acid (GA): accumulated metabolite; neurotoxicity implicated. (barzi2023rescueofglutaric pages 1-3, chen2024clinicalfeaturesand pages 1-2)
- 3‑Hydroxyglutaric acid (3OHGA/3‑OH‑GA): accumulated metabolite; neurotoxicity implicated. (barzi2023rescueofglutaric pages 1-3, chen2024clinicalfeaturesand pages 1-2)
- Glutarylcarnitine (C5DC): key NBS biomarker and biochemical hallmark. (chen2024clinicalfeaturesand pages 1-2, zaunseder2024digitaltierstrategyimproves pages 1-2)
- L‑carnitine: standard-of-care supplement; also tested for mechanistic mitigation in preclinical work. (oh2024glutaricaciduriatype pages 3-5, seminotti2022disturbanceofmitochondrial pages 10-12)
- Bezafibrate: pan‑PPAR agonist showing neuroprotective/mitochondrial and anti-inflammatory effects in GA1 mouse brain. (seminotti2022disturbanceofmitochondrial pages 1-2, seminotti2022disturbanceofmitochondrial pages 10-12)

3.4 Cell types (CL-style)
- Microglia: implicated by increased Iba‑1 staining (activation) in GA1 mouse brain. (seminotti2022disturbanceofmitochondrial pages 1-2)
- Neurons of basal ganglia/striatum (putamen, caudate): primary vulnerable neuronal populations (imaging/clinical phenotype). (bian2023glutaricaciduriatype pages 3-5, martner2021thebiochemicalsubtype pages 1-2)

3.5 Anatomical locations (UBERON-style)
- Striatum / basal ganglia (putamen, caudate head, globus pallidus): core lesion site, correlating with dystonia severity. (bian2023glutaricaciduriatype pages 1-2, bian2023glutaricaciduriatype pages 3-5)
- Temporal lobe and cerebral white matter: detectable microstructural injury by DKI, with high prevalence of white matter changes. (bian2023glutaricaciduriatype pages 3-5)
- Liver: major source of neurotoxic metabolites in mouse-model evidence (liver–brain axis). (barzi2023rescueofglutaric pages 1-3)

4. Dysregulated pathways, biological processes (GO-style candidates)

The following processes are repeatedly supported across experimental and clinical synthesis evidence:
- Lysine catabolic process / amino acid catabolic process (metabolic block at GCDH). (barzi2023rescueofglutaric media 22490951, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
- Mitochondrial matrix metabolism and oxidative phosphorylation/energy derivation (α‑ketoglutarate dehydrogenase inhibition; bioenergetic disruption). (chen2024clinicalfeaturesand pages 1-2, seminotti2022disturbanceofmitochondrial pages 10-12)
- Response to oxidative stress / redox homeostasis (MDA↑, GSH↓; antioxidant enzyme changes). (seminotti2022disturbanceofmitochondrial pages 10-12)
- Inflammatory response / NF‑κB signaling / microglial activation (Iba‑1↑; NF‑κB nuclear↑; IκBα cytosolic↓). (seminotti2022disturbanceofmitochondrial pages 1-2)
- Mitochondrial fission (DRP1↑). (seminotti2022disturbanceofmitochondrial pages 10-12)
- ER stress / unfolded protein response (DDIT3/CHOP↑; ER–mitochondria tethering proteins reduced). (seminotti2022disturbanceofmitochondrial pages 10-12)
- Synaptic signaling imbalance (glutamate receptor overactivation; reduced GABA synthesis). (chen2024clinicalfeaturesand pages 1-2)

5. Cellular components (cellular localization)
- Mitochondrion / mitochondrial matrix: GCDH is mitochondrial; mitochondrial dynamics and bioenergetics are central. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, seminotti2022disturbanceofmitochondrial pages 10-12)
- ER–mitochondria contact sites (MAMs): reduced IP3R and VDAC1 suggest altered organelle coupling. (seminotti2022disturbanceofmitochondrial pages 10-12)
- Nucleus/cytosol signaling compartments: NF‑κB nuclear accumulation with cytosolic IκBα reduction in mouse brain indicates inflammatory transcriptional activation. (seminotti2022disturbanceofmitochondrial pages 1-2)

6. Disease progression (sequence of events)

6.1 Initiation
Biallelic GCDH dysfunction leads to impaired glutaryl‑CoA oxidation and accumulation of GA/3OHGA/C5DC. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, chen2024clinicalfeaturesand pages 1-2)

6.2 Vulnerable developmental window and triggers
A consistent “window of vulnerability” is early childhood:
- Untreated striatal injury is typically between “3–36 months.” (martner2021thebiochemicalsubtype pages 1-2)
- Review emphasizes vulnerability “infants and children up to six years of age.” (oh2024glutaricaciduriatype pages 3-5)
Triggers include catabolic stressors, prominently infections/fever and also fasting/surgery, with crises leading to irreversible striatal injury. (oh2024glutaricaciduriatype pages 1-3, chen2024clinicalfeaturesand pages 6-7)

6.3 Acute encephalopathic crisis vs insidious course
Two main clinical trajectories:
- Acute encephalopathic crises during catabolism, leading to acute striatal necrosis and movement disorder. (martner2021thebiochemicalsubtype pages 1-2, oh2024glutaricaciduriatype pages 1-3)
- Insidious onset: striatal injury can occur without an identifiable crisis; review suggests “up to 50% of symptomatic NBS cohort patients exhibit insidious-onset striatal injury.” (oh2024glutaricaciduriatype pages 1-3)

6.4 Downstream mechanisms driving progression
In brain tissue (supported by mouse model): metabolite stress aligns with redox imbalance, mitochondrial and ER stress, altered ER–mitochondria coupling, and neuroinflammation (NF‑κB; microglial activation), which plausibly converge on neuronal dysfunction/death in basal ganglia circuits. (seminotti2022disturbanceofmitochondrial pages 10-12, seminotti2022disturbanceofmitochondrial pages 1-2)

7. Phenotypic manifestations and phenotype–mechanism links (HPO-style candidates)

7.1 Key clinical phenotypes
- Macrocephaly: reported “approximately 75%” (review) and 77.19% in a Chinese series. (oh2024glutaricaciduriatype pages 1-3, chen2024clinicalfeaturesand pages 6-7)
- Dystonia / movement disorder: arises from bilateral striatal injury; dystonia severity correlates with putaminal kurtosis imaging metrics. (martner2021thebiochemicalsubtype pages 1-2, bian2023glutaricaciduriatype pages 1-2)
- Seizures/epilepsy: prevalence varies by cohort; 45.90% in the Chinese aggregated series, ~7% in one review summary. (chen2024clinicalfeaturesand pages 6-7, oh2024glutaricaciduriatype pages 1-3)
- Subdural hemorrhage/hygroma: recognized complication and important diagnostic pitfall (can mimic abusive head trauma). (oh2024glutaricaciduriatype pages 1-3, rahman2024glutericaciduria(typei) pages 2-3)

7.2 Neuroimaging phenotypes
Diffusional kurtosis imaging (DKI) provides quantitative markers of microstructural injury.
- Bian et al. (AJNR 2023): 17 GA1 vs 17 controls; routine MRI scores did not correlate with morbidity/BAD, but DKI metrics did correlate with dystonia severity; “mean kurtosis of the anterior and posterior putamen” correlated with BAD (r = 0.721 and r = 0.730), and diagnostic efficiency reached AUC 0.837. (bian2023glutaricaciduriatype pages 1-2)
- Conventional MRI prevalence in this cohort: widened Sylvian fissures 100%, ventricular dilation 94%, white matter changes 88%, and putamen/globus pallidus abnormalities 100%. (bian2023glutaricaciduriatype pages 3-5)

7.3 Cognitive outcomes (modern NBS-era cohort)
In a German prospective follow-up cohort of 107 individuals identified by newborn screening (1999–2020), cognitive performance was reduced vs general population and differed by biochemical subtype: median IQ 87 overall; high-excretor median 84 vs low-excretor 98 (p=0.0164). (martner2021thebiochemicalsubtype pages 1-2)

8. Recent developments and latest research (prioritized 2023–2024)

8.1 Liver-directed therapies and revision of pathophysiology (2023)
Barzi et al. (Science Translational Medicine; Apr 2023; https://doi.org/10.1126/scitranslmed.adf4086) report that GA and 3‑OH‑GA can cross the BBB in a GA1 mouse model and identify the liver as the source of toxic brain catabolites, rescuing phenotype via:
- AAV-mediated hepatic Gcdh gene replacement, and
- CRISPR deletion of Aass to reduce lysine flux.
This “liver–brain axis” both revises disease conceptualization and provides a targeted translational strategy. (barzi2023rescueofglutaric pages 1-3)

8.2 Systemic AAV9-GCDH gene therapy (2024)
Mateu‑Bosch et al. (Molecular Therapy—Methods & Clinical Development; Sep 2024; https://doi.org/10.1016/j.omtm.2024.101276) report neonatal systemic AAV9 delivery of human GCDH in GA1 mice, restoring activity in liver and striatum and preventing high-lysine diet–induced lethality: “protects the mice from HLD-aggressive phenotype with all mice surviving this exposure.” (mateubosch2024systemicdeliveryof pages 1-2)

8.3 Protein misfolding as a therapeutic axis (2023)
Barroso et al. (IJMS; Aug 2023; https://doi.org/10.3390/ijms241713158) provide multi-assay evidence that many GCDH missense variants cause a misfolding/oligomerization defect: “reduced cellular activity was associated with loss of tetramerization,” supporting GA1 as a “protein-misfolding disorder.” (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)

8.4 Modifier enzymes and small-molecule modulation (2024)
Wu et al. (ACS Chemical Biology; Jun 2024; https://doi.org/10.1021/acschembio.4c00204) propose SUGCT as a modulator of glutarate/glutaryl‑CoA handling to “decreas[e] glutaryl‑CoA and the derived 3‑hydroxyglutaric acid,” and identify inhibitors via FDA-compound screening, providing a pharmacology-enabled entry point to pathway manipulation strategies. (wu2024characterizationstructureand pages 1-3)

9. Current applications and real-world implementation

9.1 Newborn screening (NBS): performance, challenges, and improvements
NBS is widely implemented using MS/MS detection of C5DC (glutarylcarnitine). (oh2024glutaricaciduriatype pages 1-3, oh2024glutaricaciduriatype pages 3-5)

9.1.1 False positives and second-tier confirmation
A major operational issue is false positives, motivating second-tier biochemical/genetic confirmation and newer “digital-tier” approaches.
- Zaunseder et al. (International Journal of Neonatal Screening; Dec 2024; https://doi.org/10.3390/ijns10040083) report Heidelberg screening performance (2014–2021): sensitivity 100%, specificity 99.94%, false-positive rate 0.06%, PPV 1.5%. (zaunseder2024digitaltierstrategyimproves pages 2-4)
- In the same program, urinary 3‑OH‑GA excluded GA1 in 90% (n=435) of false positives. (zaunseder2024digitaltierstrategyimproves pages 5-7)

9.1.2 Sex imbalance in false positives
Zaunseder et al. observed “twice as many false-positives male than female newborns,” with quantified distribution 326/485 (67%) male vs 159/485 (33%) female among false positives. (zaunseder2024digitaltierstrategyimproves pages 1-2, zaunseder2024digitaltierstrategyimproves pages 4-5)

9.1.3 Digital-tier machine learning to reduce false positives
Zaunseder et al. implement logistic regression / ridge regression / SVM and report false positive reductions:
- “reduced the false-positive rate by over 90% compared to regular NBS” while identifying all confirmed GA1 correctly. (zaunseder2024digitaltierstrategyimproves pages 1-2)
- Logistic regression reduced false positives by 93.61% (full set) and 95.05% (suspected diagnosis set), with a test-set reduction 235 → 18 (92.34% reduction). (zaunseder2024digitaltierstrategyimproves pages 10-12, zaunseder2024digitaltierstrategyimproves pages 8-10)

9.2 Standard-of-care management and emergency protocols
Clinical management aims to reduce lysine flux/toxic metabolite generation and prevent catabolic decompensation.
- Maintenance therapy: lysine-restricted diet with “lysine-free, tryptophan-reduced amino acid mixtures” and lifelong carnitine supplementation; an example initial carnitine dose is “100 mg/kg/day.” (oh2024glutaricaciduriatype pages 3-5)
- Emergency management: for uncontrolled fever, vomiting/diarrhea, or new neurologic symptoms, review recommends immediate anabolism with “8–15 g/kg/day IV of glucose,” temporary protein restriction for 24–48 h, and increased carnitine. (oh2024glutaricaciduriatype pages 3-5)

9.3 Real-world evidence of treatment timing importance
A 2023 Turkish cohort highlights diagnostic and biomarker variability and the importance of timely emergency management; delayed emergency treatment during illness was associated with subsequent movement disorder in at least one described scenario. (bozaci2023glutaricaciduriaand pages 5-5)

10. Expert opinions/authoritative analysis (what leaders emphasize)

10.1 “Window of vulnerability” framing
The 2024 review emphasizes that catastrophic striatal injury occurs during a defined early-life vulnerability window and may be irreversible once present: “once striatal injury happens, therapeutic intervention cannot prevent the onset of MD.” (oh2024glutaricaciduriatype pages 3-5)

10.2 Need for new therapies beyond diet and carnitine
Multiple 2023–2024 sources note that standard care does not fully prevent neurologic injury in a substantial minority:
- Barzi et al. state that “25–33% of patients still have long-term neurological disability” despite standard management and early diagnosis. (barzi2023rescueofglutaric pages 1-3)
- Mateu‑Bosch et al. similarly report neurological damage persists in “approximately one-third of treated patients” and pursue gene therapy accordingly. (mateubosch2024systemicdeliveryof pages 1-2)

11. Relevant statistics and recent data (selected)

11.1 Incidence/prevalence estimates
- Review incidence estimate: “1 in 90,000 to 1 in 120,000.” (oh2024glutaricaciduriatype pages 1-3)
- Regional incidence examples (China): 1:89,335 and 1:73,076 (reported as regional). (chen2024clinicalfeaturesand pages 1-2)
- German GA1 birth prevalence estimate in NBS context: 1:135,000 (Germany). (zaunseder2024digitaltierstrategyimproves pages 1-2)

11.2 Newborn screening metrics (Heidelberg program)
- 2014–2021 dataset: after cleaning, 1,025,953 NBS profiles analyzed; suspected-diagnosis subset included 485 confirmed false positives and 9 confirmed GA1; no false-negative GA1 case reported in 2014–2021 in that program. (zaunseder2024digitaltierstrategyimproves pages 2-4)
- Screening performance: sensitivity 100%, specificity 99.94%, false-positive rate 0.06%, PPV 1.5%. (zaunseder2024digitaltierstrategyimproves pages 2-4)

11.3 Imaging biomarker performance (AJNR 2023)
- DKI correlations: putaminal mean kurtosis correlated with Barry-Albright dystonia scores (r ~0.72–0.73). (bian2023glutaricaciduriatype pages 1-2)
- Diagnostic efficiency: anterior putamen MK AUC 0.837. (bian2023glutaricaciduriatype pages 1-2)

11.4 Phenotype frequencies (Chinese aggregated series)
- Macrocephaly/increased head circumference: 77.19%
- Motor delay: 65.15%
- Seizures: 45.90%
- Hypotonia: 40.85%
- MRI abnormalities: 86.15%
- EEG abnormalities: 73.33%
(Reported in Chen et al. 2024 synthesis). (chen2024clinicalfeaturesand pages 6-7, chen2024clinicalfeaturesand pages 1-2)

12. Evidence items with PMIDs (limitations)
The retrieved full texts in this run did not include PubMed IDs (PMIDs) in the evidence snippets. Therefore, this report cannot reliably list PMIDs without risking hallucination. All major claims are instead supported with the retrieved paper citations (journal/DOI/URL) and the evidence context IDs above.

13. Ontology-oriented annotation draft (for knowledge base ingestion)

13.1 Pathophysiology (narrative summary)
GA1 is an autosomal recessive mitochondrial organic acidemia caused by GCDH deficiency in lysine/hydroxylysine/tryptophan catabolism, leading to accumulation of GA, 3OHGA, and C5DC. During a vulnerable early childhood period (approximately 3–36 months, broadly up to 6 years), catabolic stress (infection/fever/fasting/surgery) can precipitate acute encephalopathic crises and irreversible bilateral striatal injury, producing dystonia and complex movement disorder; an insidious striatal injury course also occurs. Mechanistically, accumulated metabolites are linked to excitotoxic signaling imbalance (glutamatergic overactivation and reduced GABA synthesis), inhibition of mitochondrial energy metabolism (α‑ketoglutarate dehydrogenase), oxidative stress (GSH depletion, lipid peroxidation), ER stress and disrupted ER–mitochondria coupling (IP3R/VDAC1 reductions; DDIT3/CHOP increase), and neuroinflammation (microglial activation; NF‑κB activation). A key 2023 advance in mouse models suggests a liver–brain axis in which toxic catabolites originate in liver and cross the BBB, motivating liver-directed therapeutic strategies.

13.2 Gene/protein annotations (examples)
- GCDH (causal): mitochondrial matrix enzyme; tetramerization/proteostasis defects for many missense variants; associated with metabolic intoxication and striatal neurodegeneration. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2, martner2021thebiochemicalsubtype pages 1-2)
- AASS (therapeutic flux control target; upstream lysine degradation): liver CRISPR deletion rescues GA1 mice. (barzi2023rescueofglutaric pages 1-3)
- SUGCT (modifier/target concept): proposed to modulate glutarate ↔ glutaryl‑CoA balance, potentially affecting 3OHGA formation. (wu2024characterizationstructureand pages 1-3)

13.3 Suggested GO terms (non-exhaustive; evidence-backed themes)
- Lysine catabolic process (barzi2023rescueofglutaric media 22490951, barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
- Mitochondrial fission (seminotti2022disturbanceofmitochondrial pages 10-12)
- Response to oxidative stress / glutathione metabolic process (seminotti2022disturbanceofmitochondrial pages 10-12)
- NF‑κB signaling / inflammatory response (seminotti2022disturbanceofmitochondrial pages 1-2)
- Endoplasmic reticulum stress / ER–mitochondria tethering and Ca2+ signaling (seminotti2022disturbanceofmitochondrial pages 10-12)
- Regulation of synaptic transmission; GABA biosynthetic process (inferred via explicit inhibition statement) (chen2024clinicalfeaturesand pages 1-2)

13.4 Suggested CL terms
- Microglial cell activation (Iba‑1 marker increase) (seminotti2022disturbanceofmitochondrial pages 1-2)
- Striatal medium spiny neurons / basal ganglia neurons (lesion localization) (bian2023glutaricaciduriatype pages 3-5)

13.5 Suggested UBERON terms
- Putamen, caudate nucleus, globus pallidus (basal ganglia structures) (bian2023glutaricaciduriatype pages 3-5, bian2023glutaricaciduriatype pages 1-2)
- Liver (metabolite source in liver–brain axis model) (barzi2023rescueofglutaric pages 1-3)

13.6 Suggested HPO terms (examples)
- Macrocephaly (oh2024glutaricaciduriatype pages 1-3, chen2024clinicalfeaturesand pages 6-7)
- Dystonia / movement disorder (martner2021thebiochemicalsubtype pages 1-2, bian2023glutaricaciduriatype pages 1-2)
- Seizures (chen2024clinicalfeaturesand pages 6-7)
- Subdural hemorrhage/hygroma (oh2024glutaricaciduriatype pages 1-3, rahman2024glutericaciduria(typei) pages 2-3)

13.7 Suggested CHEBI terms
- Glutaric acid; 3‑hydroxyglutaric acid; glutarylcarnitine; L‑carnitine; bezafibrate (chen2024clinicalfeaturesand pages 1-2, seminotti2022disturbanceofmitochondrial pages 10-12)

URLs and publication dates (selected key sources)
- Barzi et al. “Rescue of glutaric aciduria type I in mice by liver-directed therapies.” Science Translational Medicine. Apr 2023. https://doi.org/10.1126/scitranslmed.adf4086 (barzi2023rescueofglutaric pages 1-3)
- Barroso et al. “Glutaryl-CoA Dehydrogenase Misfolding in Glutaric Acidemia Type 1.” International Journal of Molecular Sciences. Aug 2023. https://doi.org/10.3390/ijms241713158 (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2)
- Wu et al. “Characterization, Structure, and Inhibition of the Human Succinyl-CoA:glutarate-CoA Transferase…” ACS Chemical Biology. Jun 2024. https://doi.org/10.1021/acschembio.4c00204 (wu2024characterizationstructureand pages 1-3)
- Mateu‑Bosch et al. “Systemic delivery of AAV-GCDH…” Molecular Therapy—Methods & Clinical Development. Sep 2024. https://doi.org/10.1016/j.omtm.2024.101276 (mateubosch2024systemicdeliveryof pages 1-2)
- Zaunseder et al. “Digital-Tier Strategy Improves Newborn Screening for Glutaric Aciduria Type 1.” International Journal of Neonatal Screening. Dec 2024. https://doi.org/10.3390/ijns10040083 (zaunseder2024digitaltierstrategyimproves pages 1-2)
- Bian et al. “Glutaric Aciduria Type 1: Comparison between Diffusional Kurtosis Imaging and Conventional MR Imaging.” AJNR. Jul 2023. https://doi.org/10.3174/ajnr.a7928 (bian2023glutaricaciduriatype pages 1-2)
- Seminotti et al. “Disturbance of Mitochondrial Dynamics… in the Brain of GCDH-Deficient Mice…” Molecular Neurobiology. May 2022. https://doi.org/10.1007/s12035-022-02887-3 (seminotti2022disturbanceofmitochondrial pages 1-2)

Image evidence
- Lysine catabolism and GA1 metabolic block schematic (Barzi et al., Figure 1A). (barzi2023rescueofglutaric media 22490951)

References

1. (barzi2023rescueofglutaric pages 1-3): Mercedes Barzi, Collin G. Johnson, Tong Chen, Ramona M. Rodriguiz, Madeline Hemmingsen, Trevor J. Gonzalez, Alan Rosales, James Beasley, Cheryl K. Peck, Yunhan Ma, Ashlee R. Stiles, Timothy C. Wood, Raquel Maeso-Diaz, Anna Mae Diehl, Sarah P. Young, Jeffrey I. Everitt, William C. Wetsel, William R. Lagor, Beatrice Bissig-Choisat, Aravind Asokan, Areeg El-Gharbawy, and Karl-Dimiter Bissig. Rescue of glutaric aciduria type i in mice by liver-directed therapies. Science Translational Medicine, Apr 2023. URL: https://doi.org/10.1126/scitranslmed.adf4086, doi:10.1126/scitranslmed.adf4086. This article has 27 citations and is from a highest quality peer-reviewed journal.

2. (barroso2023glutarylcoadehydrogenasemisfolding pages 1-2): Madalena Barroso, Marcus Gertzen, Alexandra F. Puchwein-Schwepcke, Heike Preisler, Andreas Sturm, Dunja D. Reiss, Marta K. Danecka, Ania C. Muntau, and Søren W. Gersting. Glutaryl-coa dehydrogenase misfolding in glutaric acidemia type 1. International Journal of Molecular Sciences, 24:13158, Aug 2023. URL: https://doi.org/10.3390/ijms241713158, doi:10.3390/ijms241713158. This article has 5 citations.

3. (oh2024glutaricaciduriatype pages 1-3): J Oh. Glutaric aciduria type 1: a review of clinical features, diagnosis, and management. Unknown journal, 2024.

4. (zaunseder2024digitaltierstrategyimproves pages 8-10): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

5. (mateubosch2024systemicdeliveryof pages 1-2): Anna Mateu-Bosch, Eulàlia Segur-Bailach, Emma Muñoz-Moreno, María José Barallobre, Maria Lourdes Arbonés, Sabrina Gea-Sorlí, Frederic Tort, Antonia Ribes, Judit García-Villoria, and Cristina Fillat. Systemic delivery of aav-gcdh ameliorates hld-induced phenotype in a glutaric aciduria type i mouse model. Sep 2024. URL: https://doi.org/10.1016/j.omtm.2024.101276, doi:10.1016/j.omtm.2024.101276. This article has 9 citations.

6. (chen2024clinicalfeaturesand pages 1-2): Yunxi Chen, Qinghua Zhang, Lei Cao, Xuan Feng, Pengwu Lin, Shaohua Zhu, Furong Liu, Xing Wang, Shengju Hao, Yafei Cao, Hongyan Wang, and Yali Ni. Clinical features and gcdh gene variants in three chinese families with glutaric aciduria type 1: a case series and literature review. Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101123, doi:10.1016/j.ymgmr.2024.101123. This article has 1 citations.

7. (barzi2023rescueofglutaric media 22490951): Mercedes Barzi, Collin G. Johnson, Tong Chen, Ramona M. Rodriguiz, Madeline Hemmingsen, Trevor J. Gonzalez, Alan Rosales, James Beasley, Cheryl K. Peck, Yunhan Ma, Ashlee R. Stiles, Timothy C. Wood, Raquel Maeso-Diaz, Anna Mae Diehl, Sarah P. Young, Jeffrey I. Everitt, William C. Wetsel, William R. Lagor, Beatrice Bissig-Choisat, Aravind Asokan, Areeg El-Gharbawy, and Karl-Dimiter Bissig. Rescue of glutaric aciduria type i in mice by liver-directed therapies. Science Translational Medicine, Apr 2023. URL: https://doi.org/10.1126/scitranslmed.adf4086, doi:10.1126/scitranslmed.adf4086. This article has 27 citations and is from a highest quality peer-reviewed journal.

8. (zaunseder2024digitaltierstrategyimproves pages 1-2): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

9. (martner2021thebiochemicalsubtype pages 1-2): E. M. Charlotte Märtner, Eva Thimm, Philipp Guder, Katharina A. Schiergens, Frank Rutsch, Sylvia Roloff, Iris Marquardt, Anibh M. Das, Peter Freisinger, Sarah C. Grünert, Johannes Krämer, Matthias R. Baumgartner, Skadi Beblo, Claudia Haase, Andrea Dieckmann, Martin Lindner, Andrea Näke, Georg F. Hoffmann, Chris Mühlhausen, Magdalena Walter, Sven F. Garbade, Esther M. Maier, Stefan Kölker, and Nikolas Boy. The biochemical subtype is a predictor for cognitive function in glutaric aciduria type 1: a national prospective follow-up study. Scientific Reports, Sep 2021. URL: https://doi.org/10.1038/s41598-021-98809-9, doi:10.1038/s41598-021-98809-9. This article has 31 citations and is from a peer-reviewed journal.

10. (bian2023glutaricaciduriatype pages 3-5): B. Bian, Z. Liu, D. Feng, W. Li, L. Wang, Y. Li, and D. Li. Glutaric aciduria type 1: comparison between diffusional kurtosis imaging and conventional mr imaging. American Journal of Neuroradiology, 44:967-973, Jul 2023. URL: https://doi.org/10.3174/ajnr.a7928, doi:10.3174/ajnr.a7928. This article has 4 citations and is from a peer-reviewed journal.

11. (shi2024disordersoforganic pages 7-8): Yuqing Shi, Zihan Wei, Yan Feng, Ya-Jing Gan, Guo-Yan Li, and Yanchun Deng. Disorders of organic acid metabolism and epilepsy. Acta Epileptologica, Aug 2024. URL: https://doi.org/10.1186/s42494-024-00167-2, doi:10.1186/s42494-024-00167-2. This article has 2 citations.

12. (seminotti2022disturbanceofmitochondrial pages 10-12): Bianca Seminotti, Morgana Brondani, Rafael Teixeira Ribeiro, Guilhian Leipnitz, and Moacir Wajner. Disturbance of mitochondrial dynamics, endoplasmic reticulum–mitochondria crosstalk, redox homeostasis, and inflammatory response in the brain of glutaryl-coa dehydrogenase-deficient mice: neuroprotective effects of bezafibrate. Molecular Neurobiology, 59:4839-4853, May 2022. URL: https://doi.org/10.1007/s12035-022-02887-3, doi:10.1007/s12035-022-02887-3. This article has 16 citations and is from a peer-reviewed journal.

13. (seminotti2022disturbanceofmitochondrial pages 1-2): Bianca Seminotti, Morgana Brondani, Rafael Teixeira Ribeiro, Guilhian Leipnitz, and Moacir Wajner. Disturbance of mitochondrial dynamics, endoplasmic reticulum–mitochondria crosstalk, redox homeostasis, and inflammatory response in the brain of glutaryl-coa dehydrogenase-deficient mice: neuroprotective effects of bezafibrate. Molecular Neurobiology, 59:4839-4853, May 2022. URL: https://doi.org/10.1007/s12035-022-02887-3, doi:10.1007/s12035-022-02887-3. This article has 16 citations and is from a peer-reviewed journal.

14. (wu2024characterizationstructureand pages 1-3): Ruoxi Wu, Susmita Khamrui, Tetyana Dodatko, João Leandro, Amanda Sabovic, Sara Violante, Justin R. Cross, Eric Marsan, Kunal Kumar, Robert J. DeVita, Michael B. Lazarus, and Sander M. Houten. Characterization, structure, and inhibition of the human succinyl-coa:glutarate-coa transferase, a putative genetic modifier of glutaric aciduria type 1. ACS Chemical Biology, 19:1544-1553, Jun 2024. URL: https://doi.org/10.1021/acschembio.4c00204, doi:10.1021/acschembio.4c00204. This article has 3 citations and is from a domain leading peer-reviewed journal.

15. (oh2024glutaricaciduriatype pages 3-5): J Oh. Glutaric aciduria type 1: a review of clinical features, diagnosis, and management. Unknown journal, 2024.

16. (bian2023glutaricaciduriatype pages 1-2): B. Bian, Z. Liu, D. Feng, W. Li, L. Wang, Y. Li, and D. Li. Glutaric aciduria type 1: comparison between diffusional kurtosis imaging and conventional mr imaging. American Journal of Neuroradiology, 44:967-973, Jul 2023. URL: https://doi.org/10.3174/ajnr.a7928, doi:10.3174/ajnr.a7928. This article has 4 citations and is from a peer-reviewed journal.

17. (chen2024clinicalfeaturesand pages 6-7): Yunxi Chen, Qinghua Zhang, Lei Cao, Xuan Feng, Pengwu Lin, Shaohua Zhu, Furong Liu, Xing Wang, Shengju Hao, Yafei Cao, Hongyan Wang, and Yali Ni. Clinical features and gcdh gene variants in three chinese families with glutaric aciduria type 1: a case series and literature review. Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101123, doi:10.1016/j.ymgmr.2024.101123. This article has 1 citations.

18. (rahman2024glutericaciduria(typei) pages 2-3): MZ Rahman, S Ahsan, and R Afroz. Gluteric aciduria (type-i) presenting as bilateral subdural hygroma-a case report with literature review. Unknown journal, 2024.

19. (zaunseder2024digitaltierstrategyimproves pages 2-4): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

20. (zaunseder2024digitaltierstrategyimproves pages 5-7): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

21. (zaunseder2024digitaltierstrategyimproves pages 4-5): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

22. (zaunseder2024digitaltierstrategyimproves pages 10-12): Elaine Zaunseder, Julian Teinert, Nikolas Boy, Sven F. Garbade, Saskia Haupt, Patrik Feyh, Georg F. Hoffmann, Stefan Kölker, Ulrike Mütze, and Vincent Heuveline. Digital-tier strategy improves newborn screening for glutaric aciduria type 1. International Journal of Neonatal Screening, 10:83, Dec 2024. URL: https://doi.org/10.3390/ijns10040083, doi:10.3390/ijns10040083. This article has 1 citations.

23. (bozaci2023glutaricaciduriaand pages 5-5): Ayse Ergül Bozaci, Esra Er, Aysel Tekmenuray Ünal, İbrahim Taş, Ercan Ayaz, Mehmet Nuri Ozbek, Asude Durmaz, Ayçe Aykut, and Melis Kose. Glutaric aciduria and l-2-hydroxyglutaric aciduria: clinical and molecular findings of 35 patients from turkey. Sep 2023. URL: https://doi.org/10.1016/j.ymgmr.2023.100979, doi:10.1016/j.ymgmr.2023.100979. This article has 13 citations.
