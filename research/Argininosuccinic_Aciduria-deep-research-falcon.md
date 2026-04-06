---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:22:08.878364'
end_time: '2026-02-23T23:45:17.548155'
duration_seconds: 1388.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Argininosuccinic Aciduria
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Argininosuccinic Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Argininosuccinic Aciduria**.
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
- **Disease Name:** Argininosuccinic Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Argininosuccinic Aciduria**.
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


Title: Pathophysiology of Argininosuccinic Aciduria (Argininosuccinate Lyase Deficiency, ASLD)

Publication focus: molecular and cellular mechanisms underlying disease progression, emphasizing 2023–2024 literature when available.

1. Disease identifiers and definition

Argininosuccinic aciduria (ASA) is caused by inherited deficiency of argininosuccinate lyase (ASL), the urea-cycle enzyme that cleaves argininosuccinate to produce arginine and fumarate. ASL deficiency creates a block in ureagenesis, predisposing to hyperammonemia, and simultaneously disrupts arginine availability for nitric oxide (NO) production (citrulline–NO cycle), producing multisystem disease in which neurological and liver phenotypes may be partly ammonia-independent. (kho2023argininosuccinatelyasedeficiency pages 1-2, gurung2024mrnatherapycorrects pages 1-3)

The 2024 UK multicentre cohort paper frames ASL as “integral to the urea cycle detoxifying neurotoxic ammonia and the nitric oxide (NO) biosynthesis cycle” and notes ASA as “a rare disease with hyperammonemia and NO deficiency.” (gurung2024theincidenceof pages 1-3)

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Primary metabolic lesion: urea-cycle block → hyperammonemia

Core mechanism: ASL deficiency reduces conversion of ammonia-derived nitrogen to urea, leading to hyperammonemia (classically neonatal/early life decompensation) and acute encephalopathy risk. Gurung et al. (2024) state ASL “enables the clearance of neurotoxic ammonia and the biosynthesis of arginine,” and patients “present with argininosuccinic aciduria… with hyperammonemia.” (gurung2024mrnatherapycorrects pages 1-3)

However, multiple sources emphasize that ammonia control does not fully prevent chronic complications, indicating additional tissue-autonomous mechanisms. Gurung et al. (2024) note progression of liver disease despite ammonia control, “suggesting hyperammonaemia is not the sole cause.” (gurung2024mrnatherapycorrects pages 3-4)

2.2 NO deficiency as a cell-autonomous mechanism (endothelium, vasculature, BBB)

A distinctive mechanistic hallmark of ASLD is NO deficiency that is not merely secondary to low arginine concentration. ASL is described as required both for arginine synthesis and for channeling extracellular arginine to nitric oxide synthase (NOS), enabling tissue NO production; loss of ASL produces “cell-autonomous… NOS-dependent NO deficiency.” (kho2023argininosuccinatelyasedeficiency pages 1-2)

Blood–brain barrier (BBB) disruption: Kho et al. (2023, JCI Insight) directly link ASLD to BBB dysfunction via NO-mediated tight junction changes. In human brain microvascular endothelial cells, ASL knockdown decreased transendothelial electrical resistance (TEER), indicating increased permeability, and barrier integrity was improved by NO donor or by inhibiting claudin-1. In vivo, a hypomorphic ASLD mouse model exhibited increased BBB leakage that was partially rescued by NO supplementation. (kho2023argininosuccinatelyasedeficiency pages 1-2)

Systemic vascular dysfunction and hypertension: Kho et al. (2018, AJHG) reports that endothelial-specific loss of ASL leads to endothelial-dependent vascular dysfunction with “reduced nitric oxide (NO) production,” plus “increased oxidative stress, and impaired angiogenesis,” establishing a mechanistic link from ASL deficiency → endothelial NO deficit → vascular pathology. (kho2018argininosuccinatelyasedeficiency pages 1-2)

2.3 Oxidative stress and glutathione dysregulation (liver and systemic redox)

A major recent mechanistic advance (2024) is identification of glutathione pathway disruption in ASLD/ASA. Gurung et al. (2024, Science Translational Medicine) report “dysregulation of glutathione biosynthesis and upstream cysteine utilization” in ASL-deficient patients and mice, where “up-regulation of cysteine metabolism contrasted with glutathione depletion and down-regulated antioxidant pathways.” (gurung2024mrnatherapycorrects pages 1-3)

Quantitatively, in the AslNeo/Neo model, plasma total glutathione is decreased and liver total glutathione is decreased more markedly; hepatic GGT activity/expression showed a “5-fold increase” vs wild type, with increased urine glutathione, indicating altered glutathione turnover/handling. (gurung2024mrnatherapycorrects pages 3-4)

2.4 Liver disease mechanisms: chronic hepatocellular injury, fibrosis, and altered glycogen metabolism

Chronic liver disease is a common component of ASA and may progress despite metabolic “control” of ammonia. Gurung et al. (2024) describe chronic liver disease in ASA with hepatomegaly and transaminitis and potential progression to liver failure and hepatocellular carcinoma, noting the absence of reliable biomarkers to predict severity. (gurung2024mrnatherapycorrects pages 1-3)

Burrage et al. (2020, JCI Insight) provides evidence that liver injury is prevalent and can be detectable beyond ALT/AST. In ASLD, prevalence of chronic aminotransferase elevation is high: “for ≥2 ALT levels above 100 U/L, the prevalence was 37%… for ASLD.” Elevated ALT in ASLD was significantly associated with hyperammonemia (P<0.001) and nitrogen-scavenger use (P=0.001), linking more severe urea-cycle dysfunction to hepatocellular injury. (burrage2020chronicliverdisease pages 2-3, burrage2020chronicliverdisease pages 1-2)

Noninvasive fibrosis/liver-stiffness abnormalities may be present even when aminotransferases are normal. In a clinical subset (n=8 ASLD), 5 (63%) had elevated liver stiffness by shear wave elastography (SWE; median shear wave speed ≥1.35), and 3 (38%) had elevated FibroTest (2 F1, 1 F1–F2). Two participants showed increased echogenicity, elevated liver stiffness, and elevated FibroTest despite normal ALT/AST on the exam day, supporting that ALT/AST can under-detect disease. (burrage2020chronicliverdisease pages 3-5, burrage2020chronicliverdisease pages 5-6)

Mechanistically, Burrage et al. show excessive hepatic glycogen accumulation and impaired glycogenolysis in AslNeo/Neo mice, with reduced glycogen phosphorylase protein/activity, and rescue of liver phenotype by liver-targeted ASL gene delivery (helper-dependent adenovirus expressing Asl). The authors propose hypotheses linking urea cycle dysfunction and NO deficiency to glycogen phosphorylase stability/activity (e.g., reduced nitrosylation), among other mechanisms. (burrage2020chronicliverdisease pages 1-2, burrage2020chronicliverdisease pages 9-11)

2.5 Neurological disease beyond ammonia: chronic encephalopathy, epilepsy, movement disorder

The neurological phenotype in ASA is increasingly understood as multifactorial and not strictly explained by hyperammonemic crises. Gurung et al. (2024, JIMD) explicitly states that movement disorders become more prevalent with age and are “independent from the age of onset of hyperammonemia.” (gurung2024theincidenceof pages 1-3)

In the UK cohort (n=60), neurodegeneration-related symptoms (movement disorder, hypotonia/fatigue, behavioural change) were reported in 17 individuals (28%). Movement disorder occurred in 9 (15%) with median onset 10 years (range 8–25). Hypotonia/fatigue also affected 9 (15%), median onset 11.5 years (range 1–18). Behavioural changes occurred in 4 (7%), median onset 16.5 years (range 10–28). (gurung2024theincidenceof pages 4-5)

Neuroimaging: conventional MRI can be subtle; diffusion tensor imaging (DTI) may reveal basal-ganglia–predominant microstructural abnormalities, and the paper reports region-of-interest DTI abnormalities and symptom-associated basal ganglia involvement. (gurung2024theincidenceof pages 1-3, gurung2024theincidenceof pages 7-8)

A proposed mechanistic bridge from ASL/NO deficiency to movement disorder is central catecholamine dysregulation: the JIMD paper highlights NO-mediated downregulation of catecholamine biosynthesis as a contributor to movement disorder, and supports a “cell-autonomous functional central catecholamine dysregulation” with limited dopaminergic neurodegeneration in their analyses. (gurung2024theincidenceof pages 1-3)

Clinical cohort experience also indicates high epilepsy burden even with good metabolic control. In a Saudi cohort (n=12) with classic severe neonatal phenotype, “Developmental delay and seizures disorder were seen in all of the affected patients,” with genotype (c.1060C>T p.Q354X) associated with intractable seizures and psychomotor regression; hepatic findings included persistent mild transaminase elevation and hepatomegaly in all, with fibrosis observed in older patients. (alhaidar2023argininosuccinatelyase(asl) pages 1-3, alhaidar2023argininosuccinatelyase(asl) pages 3-4)

3. Key molecular players (genes/proteins, metabolites, cell types, tissues)

3.1 Genes and proteins

Causal gene: ASL (argininosuccinate lyase). Functional roles include enzymatic cleavage in the urea cycle and facilitation of NO synthesis via an NO-synthesis complex; endothelial deletion models support causality for vascular phenotypes (hypertension, endothelial dysfunction). (kho2018argininosuccinatelyasedeficiency pages 1-2, kho2023argininosuccinatelyasedeficiency pages 1-2)

Downstream/related proteins and processes highlighted in evidence include:

• NOS-dependent NO production and tight junction regulation (claudins) in brain endothelium. (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Hepatic glycogen phosphorylase (reduced protein/activity in AslNeo/Neo liver; impaired glycogenolysis). (burrage2020chronicliverdisease pages 1-2, burrage2020chronicliverdisease pages 9-11)
• Gamma-glutamyl transferase (GGT) upregulation (5-fold) in ASLD mouse liver, linked to glutathione turnover. (gurung2024mrnatherapycorrects pages 3-4)

3.2 Chemical entities (metabolites/drugs)

Key metabolites: ammonia (neurotoxic), argininosuccinate (accumulates), arginine (deficient), nitric oxide (deficient), cysteine (altered utilization), glutathione (depleted). (gurung2024mrnatherapycorrects pages 1-3, gurung2024mrnatherapycorrects pages 3-4)

Therapeutically relevant chemicals/drugs in real-world use: sodium benzoate and phenylbutyrate (nitrogen scavengers), arginine supplementation, NO supplements (nitrite-based), and investigational mRNA (hASL mRNA in lipid nanoparticles). (vega2023ureacycledisorders pages 1-2, NCT02252770 chunk 1, NCT03064048 chunk 1, gurung2024mrnatherapycorrects pages 1-3)

Imaging/biomarker chemical: [18F]FSPG PET tracer used to monitor glutathione dysregulation and therapeutic response in preclinical work. (gurung2024mrnatherapycorrects pages 1-3)

3.3 Cell types and anatomical locations

Key affected sites and cell types supported by mechanistic evidence:

• Liver (UBERON:liver): hepatocytes with glycogen accumulation, hepatomegaly, chronic injury/fibrosis. (burrage2020chronicliverdisease pages 1-2, burrage2020chronicliverdisease pages 3-5)
• Brain microvascular endothelium / BBB (UBERON:blood-brain barrier): human brain microvascular endothelial cells show permeability changes upon ASL knockdown; BBB leakage in ASLD mice. (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Basal ganglia / brain motor circuitry (UBERON:basal ganglion region): DTI abnormalities preferentially affecting basal ganglia in symptomatic cases. (gurung2024theincidenceof pages 1-3, gurung2024theincidenceof pages 7-8)
• Systemic vasculature/endothelium: endothelial NO deficiency causes vascular dysfunction and hypertension. (kho2018argininosuccinatelyasedeficiency pages 1-2)

4. Dysregulated pathways and biological processes (GO-oriented)

From the evidence base, the most directly supported disrupted processes include:

• Urea cycle / nitrogen disposal (ammonia detoxification): impaired ureagenesis leading to hyperammonemia. (gurung2024mrnatherapycorrects pages 1-3)
• Arginine biosynthetic process and citrulline–NO cycle / nitric oxide biosynthetic process: ASL is required for systemic and tissue-specific NO generation and channels arginine to NOS. (kho2023argininosuccinatelyasedeficiency pages 1-2, kho2018argininosuccinatelyasedeficiency pages 1-2)
• Regulation of blood-brain barrier permeability / tight junction assembly: NO-mediated dysregulation of claudin expression contributing to BBB disruption. (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Response to oxidative stress / glutathione metabolic process: glutathione depletion, altered cysteine utilization, and downregulated antioxidant pathways in ASA. (gurung2024mrnatherapycorrects pages 1-3, gurung2024mrnatherapycorrects pages 3-4)
• Glycogen metabolic process / glycogenolysis: impaired glycogenolysis and reduced glycogen phosphorylase activity in ASLD liver, with rescue by hepatic ASL gene delivery. (burrage2020chronicliverdisease pages 1-2, burrage2020chronicliverdisease pages 9-11)
• Catecholamine biosynthetic process regulation (proposed NO-mediated downregulation): implicated in movement disorder phenotype. (gurung2024theincidenceof pages 1-3)

5. Cellular components (GO CC-oriented)

Supported cellular/structural compartments include:

• Cytosol/mitochondria-associated urea-cycle enzymatic network (ureagenesis context) (supported conceptually by urea-cycle function; direct compartmentalization not quantified in extracted snippets). (gurung2024mrnatherapycorrects pages 1-3)
• Endothelial cell junctions / tight junctions (claudin-related BBB integrity). (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Hepatocyte cytoplasm with glycogen deposition (electron microscopy showing cytoplasmic glycogen displacing organelles). (burrage2020chronicliverdisease pages 5-6)

6. Disease progression (sequence of events)

A mechanistically consistent progression model supported by the retrieved literature:

(1) Genetic ASL deficiency → reduced argininosuccinate cleavage → impaired ureagenesis and impaired de novo arginine generation. (gurung2024mrnatherapycorrects pages 1-3, kho2023argininosuccinatelyasedeficiency pages 1-2)
(2) Early life: hyperammonemic crises drive acute encephalopathy risk; treated by nitrogen scavengers, protein restriction, and supportive care. (vega2023ureacycledisorders pages 1-2, naji2023anovelvariant pages 1-3)
(3) Chronic phase: despite ammonia control, tissue-autonomous mechanisms contribute to progressive multisystem complications, including NO deficiency (endothelial dysfunction, BBB disruption, hypertension), hepatic metabolic derangements (glycogen accumulation, fibrosis), and neurocognitive/motor phenotypes. (kho2023argininosuccinatelyasedeficiency pages 1-2, burrage2020chronicliverdisease pages 1-2, gurung2024theincidenceof pages 1-3)
(4) Later life: movement disorders and related symptoms may emerge after a symptom-free interval, particularly in second–third decades, suggesting ongoing vulnerability of motor/catecholamine systems. (gurung2024theincidenceof pages 4-5, gurung2024theincidenceof pages 7-8)

7. Phenotypic manifestations (HP-oriented) and mechanism linkage

Key phenotypes supported by cohort evidence:

• Hyperammonemic encephalopathy (acute) linked to urea-cycle block. (gurung2024mrnatherapycorrects pages 1-3)
• Developmental delay / neurocognitive impairment and epilepsy: in a 12-patient cohort, all had developmental delay and seizures; deficits can occur even with fewer hyperammonemia episodes, supporting ammonia-independent contributions. (alhaidar2023argininosuccinatelyase(asl) pages 1-3, NCT03064048 chunk 1)
• Movement disorder (tremor/ataxia/dystonia): 15% in the 60-patient UK cohort, increasing with age and independent of hyperammonemia onset; mechanistically tied to NO-mediated catecholamine dysregulation and possibly nitro-oxidative stress. (gurung2024theincidenceof pages 4-5, gurung2024theincidenceof pages 1-3)
• Chronic liver disease: ALT elevation prevalence 37% in ASLD; fibrosis/stiffness can be present even with normal aminotransferases. (burrage2020chronicliverdisease pages 2-3, burrage2020chronicliverdisease pages 5-6)
• Renal tubular acidosis / hypokalemia (reported in the Saudi cohort). (alhaidar2023argininosuccinatelyase(asl) pages 3-4)

8. Recent developments (2023–2024 prioritized)

8.1 BBB/endothelial mechanism (2023)

Kho et al. (2023, JCI Insight; Sep 2023, https://doi.org/10.1172/jci.insight.168475) demonstrate BBB disruption and identify a mechanistic axis: ASL loss → NO deficiency → claudin dysregulation → impaired barrier function, with partial rescue by NO supplementation. This provides a plausible ammonia-independent mechanism for neurocognitive vulnerability. (kho2023argininosuccinatelyasedeficiency pages 1-2)

8.2 Glutathione metabolism and mRNA therapy (2024)

Gurung et al. (2024, Science Translational Medicine; Jan 2024, https://doi.org/10.1126/scitranslmed.adh1334) report glutathione depletion with altered cysteine utilization in patients and mice and propose [18F]FSPG PET as a noninvasive tool to monitor hepatic glutathione dysregulation and treatment response. They show lipid nanoparticle–delivered human ASL mRNA improves glutathione metabolism and chronic liver disease and rescues ASL-deficient mouse phenotypes while enhancing ureagenesis, supporting clinical translation. (gurung2024mrnatherapycorrects pages 1-3)

8.3 Late-onset movement-disorder phenotyping (2024)

Gurung et al. (2024, J Inherit Metab Dis; Dec 2024, https://doi.org/10.1002/jimd.12691) provide multicentre cohort quantification and multimodal neuroimaging evidence suggesting movement symptoms arise with age and may reflect functional catecholamine dysregulation with limited dopaminergic neurodegeneration, raising the possibility of targeted symptomatic therapies. (gurung2024theincidenceof pages 1-3)

9. Current applications and real-world implementations

9.1 Standard metabolic management

Current standard-of-care aims to normalize ammonia and arginine via low-protein diet, nitrogen scavengers, and arginine supplementation. (gurung2024mrnatherapycorrects pages 1-3)

9.2 Liver transplantation (LT)

In a 33-patient UCD transplant-indications cohort (Frontiers in Pediatrics; Mar 2023, https://doi.org/10.3389/fped.2023.1103757), 16/33 (59% of neonatal survivors) underwent LT with 100% survival; transplantation restored normal protein tolerance, but neurologic sequelae were present in 69% (with no progression of brain damage after transplant). Although only a small number were ASL deficiency, this report represents real-world LT outcomes in UCD care pathways. (vega2023ureacycledisorders pages 1-2)

A large severity-adjusted analysis (Genetics in Medicine; Apr 2024, https://doi.org/10.1016/j.gim.2023.101039) reports overall 5-year patient survival >90% and 5-year graft survival >85% after LT in UCDs; LT prevents further hyperammonemic events and removes need for protein restriction/nitrogen scavengers, but did not improve neurocognitive outcomes compared with medical management when severity-adjusted. (posset2024severityadjustedevaluationof pages 1-2)

9.3 Post-transplant amino-acid supplementation

A 2024 cohort (Molecular Genetics and Metabolism; Mar 2024, https://doi.org/10.1016/j.ymgme.2023.108112) of 52 post-transplant UCD patients found that continuing L-citrulline/arginine supplementation after LT (supplemented n=16 vs non-supplemented n=36; follow-up ~4–5 years) did not improve anthropometric or neurocognitive endpoints and did not increase disease-specific plasma mean amino acid levels. (posset2024impactofsupplementation pages 1-2)

9.4 NO supplementation (clinical trials)

Two completed interventional ClinicalTrials.gov trials reflect translation of the NO-deficiency mechanism into real-world testing.

• NCT02252770 “Nitric Oxide Supplementation in Argininosuccinic Aciduria” (Baylor College of Medicine; trial start 2014; completion May 2018): triple-masked randomized placebo-controlled crossover; Neo40® 40 mg/kg/day for 14 days then crossover; primary endpoints were flow-mediated dilation (FMD) and blood pressure, motivated by the hypothesis of impaired arterial dilation due to NO deficiency. (NCT02252770 chunk 1)

• NCT03064048 “Effect of Nitric Oxide (NO) Supplementation on Neurocognitive Measures in ASLD” (Baylor College of Medicine; start 15-Sep-2017; completion 31-Jan-2023; https://clinicaltrials.gov/study/NCT03064048): randomized triple-masked crossover; Neo-ASA vs placebo for 24 weeks each; enrolled 16 participants; primary outcomes included executive function (Delis-Kaplan Tower), memory (Stanford-Binet subtests), IQ tests (Wechsler), fine motor measures (Grooved Pegboard, grip strength), and attention (Conners CPT-3). The rationale explicitly states neurocognitive deficits can be seen “even in individuals without any documented hyperammonemia” and proposes NOS-independent NO supplementation as a rational therapeutic option. (NCT03064048 chunk 1)

10. Expert interpretation and synthesis

The mechanistic picture emerging from 2023–2024 literature supports ASA as a combined disorder of: (i) nitrogen detoxification failure (hyperammonemia risk), and (ii) arginine/NO axis disruption and redox imbalance producing chronic organ dysfunction. Endothelial/BBB dysfunction via NO-dependent tight-junction regulation provides a plausible route for neurocognitive disease that is decoupled from episodic hyperammonemia. (kho2023argininosuccinatelyasedeficiency pages 1-2)

The 2024 glutathione findings are particularly impactful because they connect a biochemical signature (glutathione depletion and altered cysteine utilization) with a potential quantitative imaging biomarker ([18F]FSPG PET) and a candidate disease-modifying therapy (LNP-delivered hASL mRNA) that improves both ureagenesis and hepatic redox/liver disease phenotypes in vivo. (gurung2024mrnatherapycorrects pages 1-3)

Finally, the 2024 cohort characterization of movement disorders emphasizes a late-emerging neurological burden and suggests that not all manifestations reflect irreversible neurodegeneration, consistent with the authors’ conclusion that symptoms may be “amenable to targeted therapy.” (gurung2024theincidenceof pages 1-3)

11. Evidence tables for knowledge-base population (ontology-oriented)

11.1 Gene/protein annotations (HGNC)

• ASL (argininosuccinate lyase) — causal gene for ASA/ASLD; required for ureagenesis and systemic/tissue NO production; loss causes NO deficiency, endothelial dysfunction and BBB disruption. Evidence: Kho 2023; Gurung 2024; Kho 2018. (kho2023argininosuccinatelyasedeficiency pages 1-2, gurung2024mrnatherapycorrects pages 1-3, kho2018argininosuccinatelyasedeficiency pages 1-2)

11.2 GO Biological Processes (illustrative set)

• Urea cycle / ammonia detoxification → impaired; leads to hyperammonemia. (gurung2024mrnatherapycorrects pages 1-3)
• Nitric oxide biosynthetic process / arginine metabolic process → reduced; endothelial dysfunction and BBB permeability changes. (kho2018argininosuccinatelyasedeficiency pages 1-2, kho2023argininosuccinatelyasedeficiency pages 1-2)
• Regulation of blood–brain barrier permeability / tight junction organization → disrupted via claudin dysregulation. (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Glutathione metabolic process / cellular response to oxidative stress → disrupted; glutathione depletion and altered cysteine utilization. (gurung2024mrnatherapycorrects pages 1-3, gurung2024mrnatherapycorrects pages 3-4)
• Glycogen metabolic process / glycogenolysis → impaired; glycogen accumulation and reduced glycogen phosphorylase activity. (burrage2020chronicliverdisease pages 1-2, burrage2020chronicliverdisease pages 9-11)

11.3 GO Cellular Components (illustrative)

• Tight junction (endothelial) / BBB structural components (claudins). (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Hepatocyte cytoplasm (glycogen deposition displacing organelles). (burrage2020chronicliverdisease pages 5-6)

11.4 Cell types (CL-oriented; evidence-supported)

• Brain microvascular endothelial cells (HBMECs): ASL knockdown reduces TEER; NO donor rescues barrier integrity. (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Hepatocytes: glycogenosis, fibrosis/stiffness; altered glycogen metabolism. (burrage2020chronicliverdisease pages 5-6, burrage2020chronicliverdisease pages 3-5)

11.5 Anatomical locations (UBERON-oriented)

• Liver: chronic injury, stiffness/fibrosis; glycogen accumulation. (burrage2020chronicliverdisease pages 3-5, burrage2020chronicliverdisease pages 1-2)
• Blood–brain barrier / brain microvasculature: increased leakage/permeability. (kho2023argininosuccinatelyasedeficiency pages 1-2)
• Basal ganglia: preferentially affected in DTI abnormalities in symptomatic movement disorders. (gurung2024theincidenceof pages 1-3, gurung2024theincidenceof pages 7-8)

11.6 Chemical entities (CHEBI-oriented; evidence-supported)

• Ammonia; L-arginine; argininosuccinate; nitric oxide; cysteine; glutathione. (gurung2024mrnatherapycorrects pages 1-3)
• Sodium benzoate; sodium phenylbutyrate (nitrogen scavengers). (naji2023anovelvariant pages 1-3, vega2023ureacycledisorders pages 1-2)
• Nitrite-based NO supplements (Neo40®, Neo-ASA). (NCT02252770 chunk 1, NCT03064048 chunk 1)
• [18F]FSPG PET tracer. (gurung2024mrnatherapycorrects pages 1-3)

12. Notes on evidence limitations

Although this report prioritizes 2023–2024 mechanistic studies, several foundational mechanistic insights (e.g., systemic NO production requirement, endothelial-dependent hypertension) come from high-quality earlier primary studies (2018–2020) and remain essential for coherent mechanistic mapping. Outcomes from NO-supplementation trials were not available in the retrieved ClinicalTrials.gov text excerpts (design/endpoints only), and some mechanistic proposals in cohort studies are presented as hypotheses rather than proven causal pathways. (NCT02252770 chunk 1, NCT03064048 chunk 1, burrage2020chronicliverdisease pages 9-11)


References

1. (kho2023argininosuccinatelyasedeficiency pages 1-2): Jordan Kho, Urszula Polak, Ming-Ming Jiang, John D. Odom, Jill V. Hunter, Saima M. Ali, Lindsay C. Burrage, Sandesh C.S. Nagamani, Robia G. Pautler, Hannah P. Thompson, Akihiko Urayama, Zixue Jin, and Brendan Lee. Argininosuccinate lyase deficiency causes blood-brain barrier disruption via nitric oxide–mediated dysregulation of claudin expression. JCI Insight, Sep 2023. URL: https://doi.org/10.1172/jci.insight.168475, doi:10.1172/jci.insight.168475. This article has 9 citations and is from a domain leading peer-reviewed journal.

2. (gurung2024mrnatherapycorrects pages 1-3): Sonam Gurung, Oskar Vilhelmsson Timmermand, Dany Perocheau, Ana Luisa Gil-Martinez, Magdalena Minnion, Loukia Touramanidou, Sherry Fang, Martina Messina, Youssef Khalil, Justyna Spiewak, Abigail R. Barber, Richard S. Edwards, Patricia Lipari Pinto, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Deborah Ridout, Wendy Heywood, Ian Hargreaves, Simon Heales, Philippa B. Mills, Simon N. Waddington, Paul Gissen, Simon Eaton, Mina Ryten, Martin Feelisch, Andrea Frassetto, Timothy H. Witney, and Julien Baruteau. Mrna therapy corrects defective glutathione metabolism and restores ureagenesis in preclinical argininosuccinic aciduria. Science translational medicine, 16:eadh1334-eadh1334, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adh1334, doi:10.1126/scitranslmed.adh1334. This article has 31 citations and is from a highest quality peer-reviewed journal.

3. (gurung2024theincidenceof pages 1-3): Sonam Gurung, Saketh Karamched, Dany Perocheau, Kiran K. Seunarine, Tom Baldwin, Haya Alrashidi, Loukia Touramanidou, Claire Duff, Nour Elkhateeb, Karolina M. Stepien, Reena Sharma, Andrew Morris, Thomas Hartley, Laura Crowther, Stephanie Grunewald, Maureen Cleary, Helen Mundy, Anupam Chakrapani, Spyros Batzios, James Davison, Emma Footitt, Karin Tuschl, Robin Lachmann, Elaine Murphy, Saikat Santra, Mari‐Liis Uudelepp, Mildrid Yeo, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Andrea Frassetto, Simon Heales, Philippa B. Mills, Paul Gissen, Jonathan D. Clayden, Christopher A. Clark, Simon Eaton, Tammy L. Kalber, and Julien Baruteau. The incidence of movement disorder increases with age and contrasts with subtle and limited neuroimaging abnormalities in argininosuccinic aciduria. Journal of Inherited Metabolic Disease, 47:1213-1227, Dec 2024. URL: https://doi.org/10.1002/jimd.12691, doi:10.1002/jimd.12691. This article has 9 citations and is from a peer-reviewed journal.

4. (gurung2024mrnatherapycorrects pages 3-4): Sonam Gurung, Oskar Vilhelmsson Timmermand, Dany Perocheau, Ana Luisa Gil-Martinez, Magdalena Minnion, Loukia Touramanidou, Sherry Fang, Martina Messina, Youssef Khalil, Justyna Spiewak, Abigail R. Barber, Richard S. Edwards, Patricia Lipari Pinto, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Deborah Ridout, Wendy Heywood, Ian Hargreaves, Simon Heales, Philippa B. Mills, Simon N. Waddington, Paul Gissen, Simon Eaton, Mina Ryten, Martin Feelisch, Andrea Frassetto, Timothy H. Witney, and Julien Baruteau. Mrna therapy corrects defective glutathione metabolism and restores ureagenesis in preclinical argininosuccinic aciduria. Science translational medicine, 16:eadh1334-eadh1334, Jan 2024. URL: https://doi.org/10.1126/scitranslmed.adh1334, doi:10.1126/scitranslmed.adh1334. This article has 31 citations and is from a highest quality peer-reviewed journal.

5. (kho2018argininosuccinatelyasedeficiency pages 1-2): Jordan Kho, Xiaoyu Tian, Wing-Tak Wong, Terry Bertin, Ming-Ming Jiang, Shan Chen, Zixue Jin, Oleg A. Shchelochkov, Lindsay C. Burrage, Anilkumar K. Reddy, Hong Jiang, Reem Abo-Zahrah, Shuangtao Ma, Ping Zhang, Karl-Dimiter Bissig, Jean J. Kim, Sridevi Devaraj, George G. Rodney, Ayelet Erez, Nathan S. Bryan, Sandesh C.S. Nagamani, and Brendan H. Lee. Argininosuccinate lyase deficiency causes an endothelial-dependent form of hypertension. American journal of human genetics, 103 2:276-287, Aug 2018. URL: https://doi.org/10.1016/j.ajhg.2018.07.008, doi:10.1016/j.ajhg.2018.07.008. This article has 65 citations and is from a highest quality peer-reviewed journal.

6. (burrage2020chronicliverdisease pages 2-3): Lindsay C. Burrage, Simran Madan, Xiaohui Li, Saima Ali, Mahmoud Mohammad, Bridget M. Stroup, Ming-Ming Jiang, Racel Cela, Terry Bertin, Zixue Jin, Jian Dai, Danielle Guffey, Milton Finegold, Sandesh Nagamani, Charles G. Minard, Juan Marini, Prakash Masand, Deborah Schady, Benjamin L. Shneider, Daniel H. Leung, Deeksha Bali, and Brendan Lee. Chronic liver disease and impaired hepatic glycogen metabolism in argininosuccinate lyase deficiency. JCI Insight, Feb 2020. URL: https://doi.org/10.1172/jci.insight.132342, doi:10.1172/jci.insight.132342. This article has 16 citations and is from a domain leading peer-reviewed journal.

7. (burrage2020chronicliverdisease pages 1-2): Lindsay C. Burrage, Simran Madan, Xiaohui Li, Saima Ali, Mahmoud Mohammad, Bridget M. Stroup, Ming-Ming Jiang, Racel Cela, Terry Bertin, Zixue Jin, Jian Dai, Danielle Guffey, Milton Finegold, Sandesh Nagamani, Charles G. Minard, Juan Marini, Prakash Masand, Deborah Schady, Benjamin L. Shneider, Daniel H. Leung, Deeksha Bali, and Brendan Lee. Chronic liver disease and impaired hepatic glycogen metabolism in argininosuccinate lyase deficiency. JCI Insight, Feb 2020. URL: https://doi.org/10.1172/jci.insight.132342, doi:10.1172/jci.insight.132342. This article has 16 citations and is from a domain leading peer-reviewed journal.

8. (burrage2020chronicliverdisease pages 3-5): Lindsay C. Burrage, Simran Madan, Xiaohui Li, Saima Ali, Mahmoud Mohammad, Bridget M. Stroup, Ming-Ming Jiang, Racel Cela, Terry Bertin, Zixue Jin, Jian Dai, Danielle Guffey, Milton Finegold, Sandesh Nagamani, Charles G. Minard, Juan Marini, Prakash Masand, Deborah Schady, Benjamin L. Shneider, Daniel H. Leung, Deeksha Bali, and Brendan Lee. Chronic liver disease and impaired hepatic glycogen metabolism in argininosuccinate lyase deficiency. JCI Insight, Feb 2020. URL: https://doi.org/10.1172/jci.insight.132342, doi:10.1172/jci.insight.132342. This article has 16 citations and is from a domain leading peer-reviewed journal.

9. (burrage2020chronicliverdisease pages 5-6): Lindsay C. Burrage, Simran Madan, Xiaohui Li, Saima Ali, Mahmoud Mohammad, Bridget M. Stroup, Ming-Ming Jiang, Racel Cela, Terry Bertin, Zixue Jin, Jian Dai, Danielle Guffey, Milton Finegold, Sandesh Nagamani, Charles G. Minard, Juan Marini, Prakash Masand, Deborah Schady, Benjamin L. Shneider, Daniel H. Leung, Deeksha Bali, and Brendan Lee. Chronic liver disease and impaired hepatic glycogen metabolism in argininosuccinate lyase deficiency. JCI Insight, Feb 2020. URL: https://doi.org/10.1172/jci.insight.132342, doi:10.1172/jci.insight.132342. This article has 16 citations and is from a domain leading peer-reviewed journal.

10. (burrage2020chronicliverdisease pages 9-11): Lindsay C. Burrage, Simran Madan, Xiaohui Li, Saima Ali, Mahmoud Mohammad, Bridget M. Stroup, Ming-Ming Jiang, Racel Cela, Terry Bertin, Zixue Jin, Jian Dai, Danielle Guffey, Milton Finegold, Sandesh Nagamani, Charles G. Minard, Juan Marini, Prakash Masand, Deborah Schady, Benjamin L. Shneider, Daniel H. Leung, Deeksha Bali, and Brendan Lee. Chronic liver disease and impaired hepatic glycogen metabolism in argininosuccinate lyase deficiency. JCI Insight, Feb 2020. URL: https://doi.org/10.1172/jci.insight.132342, doi:10.1172/jci.insight.132342. This article has 16 citations and is from a domain leading peer-reviewed journal.

11. (gurung2024theincidenceof pages 4-5): Sonam Gurung, Saketh Karamched, Dany Perocheau, Kiran K. Seunarine, Tom Baldwin, Haya Alrashidi, Loukia Touramanidou, Claire Duff, Nour Elkhateeb, Karolina M. Stepien, Reena Sharma, Andrew Morris, Thomas Hartley, Laura Crowther, Stephanie Grunewald, Maureen Cleary, Helen Mundy, Anupam Chakrapani, Spyros Batzios, James Davison, Emma Footitt, Karin Tuschl, Robin Lachmann, Elaine Murphy, Saikat Santra, Mari‐Liis Uudelepp, Mildrid Yeo, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Andrea Frassetto, Simon Heales, Philippa B. Mills, Paul Gissen, Jonathan D. Clayden, Christopher A. Clark, Simon Eaton, Tammy L. Kalber, and Julien Baruteau. The incidence of movement disorder increases with age and contrasts with subtle and limited neuroimaging abnormalities in argininosuccinic aciduria. Journal of Inherited Metabolic Disease, 47:1213-1227, Dec 2024. URL: https://doi.org/10.1002/jimd.12691, doi:10.1002/jimd.12691. This article has 9 citations and is from a peer-reviewed journal.

12. (gurung2024theincidenceof pages 7-8): Sonam Gurung, Saketh Karamched, Dany Perocheau, Kiran K. Seunarine, Tom Baldwin, Haya Alrashidi, Loukia Touramanidou, Claire Duff, Nour Elkhateeb, Karolina M. Stepien, Reena Sharma, Andrew Morris, Thomas Hartley, Laura Crowther, Stephanie Grunewald, Maureen Cleary, Helen Mundy, Anupam Chakrapani, Spyros Batzios, James Davison, Emma Footitt, Karin Tuschl, Robin Lachmann, Elaine Murphy, Saikat Santra, Mari‐Liis Uudelepp, Mildrid Yeo, Patrick F. Finn, Alex Cavedon, Summar Siddiqui, Lisa Rice, Paolo G. V. Martini, Andrea Frassetto, Simon Heales, Philippa B. Mills, Paul Gissen, Jonathan D. Clayden, Christopher A. Clark, Simon Eaton, Tammy L. Kalber, and Julien Baruteau. The incidence of movement disorder increases with age and contrasts with subtle and limited neuroimaging abnormalities in argininosuccinic aciduria. Journal of Inherited Metabolic Disease, 47:1213-1227, Dec 2024. URL: https://doi.org/10.1002/jimd.12691, doi:10.1002/jimd.12691. This article has 9 citations and is from a peer-reviewed journal.

13. (alhaidar2023argininosuccinatelyase(asl) pages 1-3): Atheer Alhaidar and Nouriya AlSannaa. Argininosuccinate lyase (asl) deficiency; outcome of patients with an early presentation at johns hopkins aramco healthcare (jhah). Unknown journal, Aug 2023. URL: https://doi.org/10.21203/rs.3.rs-3279667/v1, doi:10.21203/rs.3.rs-3279667/v1.

14. (alhaidar2023argininosuccinatelyase(asl) pages 3-4): Atheer Alhaidar and Nouriya AlSannaa. Argininosuccinate lyase (asl) deficiency; outcome of patients with an early presentation at johns hopkins aramco healthcare (jhah). Unknown journal, Aug 2023. URL: https://doi.org/10.21203/rs.3.rs-3279667/v1, doi:10.21203/rs.3.rs-3279667/v1.

15. (vega2023ureacycledisorders pages 1-2): Marta García Vega, José D. Andrade, Ana Morais, Esteban Frauca, Gema Muñoz Bartolo, María D. Lledín, Ana Bergua, and Loreto Hierro. Urea cycle disorders and indications for liver transplantation. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1103757, doi:10.3389/fped.2023.1103757. This article has 16 citations.

16. (NCT02252770 chunk 1): Sandesh Chakravarthy Sreenath Nagamani. Nitric Oxide Supplementation in Argininosuccinic Aciduria. Baylor College of Medicine. 2014. ClinicalTrials.gov Identifier: NCT02252770

17. (NCT03064048 chunk 1): Sandesh Chakravarthy Sreenath Nagamani. Nitric Oxide Supplementation on Neurocognitive Functions in Patients With ASLD. Baylor College of Medicine. 2017. ClinicalTrials.gov Identifier: NCT03064048

18. (naji2023anovelvariant pages 1-3): HAMOUCHE Naji, TOHME Rana, EL ACHKAR Mariella, HMAIMESS Ghassan, BAYDOUN Abed El Karim, SOKHN Maroun, GHABRIL Ramy, GHADIEH Joëlle M, NAOUFAL Rania, KHNEISSER Issam, FATTAH Mohamad, KHOURY Jacqueline, and MANSOUR Hicham. A novel variant of asl gene mutation in a lebanese neonate with severe argininosuccinic aciduria phenotype. SVOA Paediatrics, 2:156-159, Oct 2023. URL: https://doi.org/10.58624/svoapd.2023.02.050, doi:10.58624/svoapd.2023.02.050. This article has 0 citations.

19. (posset2024severityadjustedevaluationof pages 1-2): Roland Posset, Sven F. Garbade, Florian Gleich, Svenja Scharre, Jürgen G. Okun, Andrea L. Gropman, Sandesh C.S. Nagamani, Ann-Catrin Druck, Friederike Epp, Georg F. Hoffmann, Stefan Kölker, Matthias Zielonka, Nicholas Ah Mew, Jennifer Seminara, Lindsay C. Burrage, Gerard T. Berry, Margo Breilyn, Andreas Schulze, Cary O. Harding, Susan A. Berry, Derek Wong, Shawn E. McCandless, Matthias R. Baumgartner, Laura Konczal, Can Ficicioglu, George A. Diaz, Curtis R. Coughlin, Gregory M. Enns, Renata C. Gallagher, Christina Lam, Tamar Stricker, Greta Wilkening, Carlo Dionisi-Vici, Dries Dobbelaere, Javier Blasco-Alonso, Alberto B. Burlina, Peter Freisinger, Peter M. van Hasselt, Anastasia Skouma, Allan M. Lund, Roshni Vara, Adrijan Sarajlija, Andrew A. Morris, Anupam Chakrapani, Ivo Barić, Persephone Augoustides-Savvopoulou, Yin-Hsiu Chien, Elisenda Cortès-Saladelafont, Francois Eyskens, Gwendolyn Gramer, Jiri Zeman, Daniela Karall, Maria L. Couce, Chris Mühlhausen, Consuelo Pedrón-Giner, Ute Spiekerkoetter, Jolanta Sykut-Cegielska, Margreet Wagenmakers, and Frits A. Wijburg. Severity-adjusted evaluation of liver transplantation on health outcomes in urea cycle disorders. Genetics in Medicine, 26:101039, Apr 2024. URL: https://doi.org/10.1016/j.gim.2023.101039, doi:10.1016/j.gim.2023.101039. This article has 11 citations and is from a highest quality peer-reviewed journal.

20. (posset2024impactofsupplementation pages 1-2): Roland Posset, Sven F. Garbade, Florian Gleich, Sandesh C.S. Nagamani, Andrea L. Gropman, Friederike Epp, Nesrine Ramdhouni, Ann-Catrin Druck, Georg F. Hoffmann, Stefan Kölker, Matthias Zielonka, Andreas Schulze, Angeles García-Cazorla, Can Ficicioglu, Cary O. Harding, Christina Lam, Curtis R. Coughlin, Cynthia Le Mons, Derek Wong, Dries Dobbelaere, George A. Diaz, Gerard T. Berry, Gregory M. Enns, Greta Wilkening, J. Lawrence Merritt, Jennifer Seminara, Laura Konczal, Lindsay C. Burrage, Margo Breilyn, Martin Lindner, Matthias R. Baumgartner, Nicholas Ah. Mew, Renata C. Gallagher, Shawn E. McCandless, Susan A. Berry, and Tamar Stricker. Impact of supplementation with l-citrulline/arginine after liver transplantation in individuals with urea cycle disorders. Mar 2024. URL: https://doi.org/10.1016/j.ymgme.2023.108112, doi:10.1016/j.ymgme.2023.108112. This article has 6 citations and is from a peer-reviewed journal.
