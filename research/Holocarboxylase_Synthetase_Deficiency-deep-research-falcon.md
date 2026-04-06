---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:22:08.955620'
end_time: '2026-02-23T23:37:11.578171'
duration_seconds: 902.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Holocarboxylase Synthetase Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Holocarboxylase Synthetase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Holocarboxylase Synthetase Deficiency**.
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
- **Disease Name:** Holocarboxylase Synthetase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Holocarboxylase Synthetase Deficiency**.
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


Title: Pathophysiology of Holocarboxylase Synthetase Deficiency (HLCS deficiency; biotin‑responsive multiple carboxylase deficiency)

MONDO / classification
Holocarboxylase synthetase deficiency is an autosomal recessive inborn error of metabolism caused by loss‑of‑function variants in HLCS, resulting in “multiple carboxylase deficiency” due to impaired biotinylation (activation) of biotin‑dependent carboxylases. OpenTargets lists the disease as MONDO_0009666 (“holocarboxylase synthetase deficiency”) with HLCS as the associated target (MONDO_0009666 as returned by OpenTargets search; primary literature PMIDs in that resource were not retrieved as full texts here). (ling2023clinicalbiochemicaland pages 1-2)

Executive mechanistic summary (current understanding)
Holocarboxylase synthetase (HLCS; also called holocarboxylase synthase) is responsible for covalently attaching biotin to specific apocarboxylases, thereby converting inactive apo‑carboxylases into active holo‑carboxylases. The principal human targets highlighted in recent clinical literature include pyruvate carboxylase (PC), propionyl‑CoA carboxylase (PCC), 3‑methylcrotonyl‑CoA carboxylase (MCC), and acetyl‑CoA carboxylase (ACC). Loss of HLCS activity reduces activities of these enzymes and disrupts major metabolic pathways: gluconeogenesis, fatty acid synthesis, and amino‑acid catabolism (particularly leucine and propionyl/odd‑chain fatty acid metabolism). Clinically, this manifests as episodic or persistent metabolic decompensation characterized by metabolic acidosis (often with lactic acidosis), organic aciduria, ketosis, and hyperammonemia; dermatologic and neurologic features are common; untreated disease can progress to coma and death. (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2, gaschignard2024casereporttwo pages 1-3)

1) Core pathophysiology
1.1 Primary mechanism: impaired protein biotinylation → multi‑enzyme deficiency
Recent cohort and case reports describe the central mechanism as failure of HLCS‑mediated biotinylation of carboxylases, causing “multiple carboxylase deficiency.” (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2)

Direct mechanistic phrasing from the literature includes that HLCS is “responsible for covalently linking biotin” to biotin‑dependent carboxylases and that this biotinylation is “crucial for their enzymatic activities.” (kim2024dramaticclinicalimprovement pages 1-2)

1.2 Dysregulated pathways
Because PCC, MCC, PC, and ACC sit at key junctions of intermediary metabolism, HLCS deficiency produces pathway‑level dysfunction across:

• Gluconeogenesis/anaplerosis: PC deficiency reduces conversion of pyruvate to oxaloacetate, contributing to lactic acidosis and impaired glucose homeostasis (hypoglycemia in some cases). (kim2024dramaticclinicalimprovement pages 1-2, wu2020impairedglucosehomeostasis pages 4-5)
• Amino‑acid catabolism: MCC deficiency disrupts leucine catabolism, contributing to elevations of 3‑hydroxyisovalerate/3‑methylcrotonylglycine and related acylcarnitines (e.g., C5OH). (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2)
• Propionate metabolism: PCC deficiency contributes to elevations of propionyl‑derived metabolites (e.g., methylcitrate) and acylcarnitine perturbations (C3). (ling2023clinicalbiochemicaland pages 1-2, ling2023clinicalbiochemicaland pages 4-5)
• Fatty acid metabolism: ACC impairment affects fatty acid synthesis; more broadly, energy failure is invoked in severe decompensations. (kim2024dramaticclinicalimprovement pages 1-2, zou2024casereporta pages 2-4)

1.3 Biotin cycle / homeostasis framing
A 2024 review situates HLCS deficiency within the “biotin cycle,” in which HLCS biotinylates apocarboxylases to form active holocarboxylases; subsequent proteolysis yields biocytin/biotinyl‑peptides, and biotinidase releases free biotin for recycling. Deficient HLCS therefore “impairs formation of biotinylated proteins” and functionally mimics severe biotin deficiency at the enzyme‑activity level. (karachaliou2024biotinhomeostasisand pages 4-5)

2) Key molecular players
2.1 Genes/proteins (causal and proximal)
Causal gene:
• HLCS (holocarboxylase synthetase). Cohort genetics demonstrate many missense and other variants; in one 28‑patient cohort, 17 different mutations were observed and 89.3% of alleles were missense; a frequent allele in that cohort was c.1522C>T (p.R508W), representing 41.1% of alleles. (ling2023clinicalbiochemicaland pages 4-5)

Direct biochemical targets (biotin‑dependent carboxylases emphasized in recent clinical reports):
• PC (pyruvate carboxylase), PCC (propionyl‑CoA carboxylase), MCC (3‑methylcrotonyl‑CoA carboxylase), ACC (acetyl‑CoA carboxylase). (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2)

2.2 Chemical entities / metabolites / biomarkers
Key diagnostic and pathophysiology‑linked biomarkers used in newborn screening and confirmatory testing:

Blood (MS/MS) biomarkers:
• 3‑hydroxyisovalerylcarnitine (C5‑OH): described as an NBS marker; in the 28‑patient cohort, C5OH was “far beyond the cutoff” in all patients. (ling2023clinicalbiochemicaland pages 1-2, ling2023clinicalbiochemicaland pages 4-5)
• C3 (propionylcarnitine), C2, and ratios such as C3/C2 and C5OH/C3 may show characteristic patterns (C3/C2 only slightly elevated in ~half the cohort, while C5OH/C3 often elevated). (ling2023clinicalbiochemicaland pages 4-5)

Urine (GC/MS) organic acid biomarkers:
• Increased lactic acid, 3‑hydroxyisovaleric acid, 3‑hydroxypropionic acid, 3‑methylcrotonylglycine, methylcitric acid, tiglylglycine, pyruvate (and others) recur across reports. (kim2024dramaticclinicalimprovement pages 1-2, demaret2024insulintherapyin pages 1-2)

Quantitative examples from a 2024 neonatal case (illustrating severity of metabolic intoxication):
• C5‑OH 3.6955 μmol/L; plasma lactate 10.09 mmol/L; ammonia 392 μg/dL; urine lactic acid 6419.9 mmol/mol creatinine; urine 3‑hydroxyisovaleric acid 1956.4 mmol/mol creatinine. (kim2024dramaticclinicalimprovement pages 1-2)

Key therapeutic chemical entity:
• Biotin (vitamin B7). Pharmacologic/high‑dose biotin is the main disease‑modifying therapy. (ling2023clinicalbiochemicaland pages 5-6, ling2023clinicalbiochemicaland pages 4-5)

2.3 Cell types and tissues (functional involvement)
Although the cited clinical papers focus more on systemic metabolism than specific cell biology, the phenotypes and mechanistic pathways strongly implicate:
• Hepatic metabolism (gluconeogenesis and organic acid handling),
• Central nervous system (seizures, encephalopathy, developmental outcomes),
• Skin/hair follicle biology (rash, eczema, alopecia),
• Respiratory system during decompensation (tachypnea/respiratory distress as a response to acidosis and/or energy deficit). (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2, zou2024casereporta pages 2-4)

A 2024 review of biotin homeostasis notes that intracellular biotin is “mainly in mitochondria and the cytosol,” with “minor amounts in nuclei (histones) and microsomal fractions,” supporting a mitochondria/cytosol‑centric view of metabolic dysfunction while leaving open additional nuclear roles. (karachaliou2024biotinhomeostasisand pages 4-5)

2.4 Anatomical locations involved
Clinically and mechanistically, the highest‑impact organs are those with high flux through affected pathways:
• Liver (gluconeogenesis; propionate handling),
• Brain (energy failure and excitability → seizures/encephalopathy),
• Skin/hair. (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2)

3) Biological processes disrupted (GO‑oriented)
The following biological processes are directly supported or strongly implied by the enzyme‑defect narrative:
• Protein biotinylation / covalent protein modification (HLCS function as the biotin‑attaching enzyme). (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2)
• Gluconeogenesis and pyruvate metabolic process (via PC impairment and lactic acidosis/hypoglycemia presentations). (kim2024dramaticclinicalimprovement pages 1-2, wu2020impairedglucosehomeostasis pages 4-5)
• Leucine catabolic process (via MCC impairment and 3‑hydroxyisovalerate/3‑methylcrotonylglycine accumulation). (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2)
• Propionate metabolic process / anaplerotic replenishment of TCA intermediates (via PCC dysfunction; methylcitrate elevation). (ling2023clinicalbiochemicaland pages 1-2, demaret2024insulintherapyin pages 1-2)
• Fatty acid biosynthetic process (via ACC as a biotin‑dependent enzyme). (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2)
• Response to metabolic acidosis / detoxification of organic acids (clinical consequence of pathway failure). (gaschignard2024casereporttwo pages 1-3, ling2023clinicalbiochemicaland pages 1-2)

4) Cellular components (where processes occur)
The disease is driven by enzyme dysfunction in core metabolic compartments:
• Mitochondrion (mitochondrial carboxylase activity is described as affected; intracellular biotin is mainly mitochondrial). (kim2024dramaticclinicalimprovement pages 2-4, karachaliou2024biotinhomeostasisand pages 4-5)
• Cytosol (intracellular biotin mainly cytosolic; ACC is cytosolic). (karachaliou2024biotinhomeostasisand pages 4-5, kim2024dramaticclinicalimprovement pages 1-2)
• Nucleus (minor biotin in nuclei/histones suggests potential regulatory layer, though not essential for the clinical metabolic phenotype as presented in the clinical cohort). (karachaliou2024biotinhomeostasisand pages 4-5)

5) Disease progression (sequence of events)
A mechanistically consistent sequence supported by cohort/case observations is:

Step 1: Genetic HLCS deficiency → reduced HLCS enzymatic activity or reduced functional biotinylation capacity.
• Reported as impaired biotinylation/activation of biotin‑dependent carboxylases. (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2)

Step 2: Multi‑carboxylase dysfunction → metabolic pathway block(s).
• Leads to accumulation of characteristic organic acids and acylcarnitines (e.g., C5OH, methylcitrate, lactate). (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2)

Step 3: Systemic metabolic decompensation.
• Manifests as metabolic acidosis (often severe), lactic acidosis, ketosis, and hyperammonemia; can include hypoglycemia or hyperglycemic ketoacidosis in certain contexts. (gaschignard2024casereporttwo pages 1-3, demaret2024insulintherapyin pages 1-2, wu2020impairedglucosehomeostasis pages 1-2)

Step 4: Tissue injury and phenotype.
• Neurologic: lethargy, hypotonia, seizures, coma; MRI abnormalities reported in a subset. (ling2023clinicalbiochemicaland pages 1-2, ling2023clinicalbiochemicaland pages 4-5)
• Dermatologic: rash/eczema and alopecia. (ling2023clinicalbiochemicaland pages 1-2, wu2020impairedglucosehomeostasis pages 1-2)
• Respiratory: tachypnea and respiratory distress, sometimes as presenting features. (kim2024dramaticclinicalimprovement pages 1-2, zou2024casereporta pages 2-4)

Step 5: Treatment modifies course.
• Prompt pharmacologic biotin often produces rapid clinical and biochemical improvement and strongly improves prognosis; delayed recognition can be fatal. (ling2023clinicalbiochemicaland pages 4-5, kim2024dramaticclinicalimprovement pages 1-2)

Distinct phases / age‑of‑onset heterogeneity
Classic descriptions emphasize neonatal/infant onset with severe acidosis; however, late‑onset and even very late‑onset cases occur. A 2024 report documents symptomatic presentation as late as 11 years and diagnosis at 23 years in siblings, stressing that unexplained metabolic acidosis beyond infancy should still trigger evaluation. (gaschignard2024casereporttwo pages 1-3)

6) Phenotypic manifestations (HP‑oriented) and mechanistic links
Key phenotypes in recent cohort/case literature include:
• Metabolic acidosis / ketoacidosis (from organic acid accumulation and energy failure). (gaschignard2024casereporttwo pages 1-3, demaret2024insulintherapyin pages 1-2)
• Lactic acidosis (from impaired gluconeogenesis/anaplerosis and secondary mitochondrial/TCA dysfunction). (kim2024dramaticclinicalimprovement pages 1-2, demaret2024insulintherapyin pages 1-2)
• Hyperammonemia (likely from catabolic stress/secondary urea cycle impairment during decompensation). (kim2024dramaticclinicalimprovement pages 1-2, gaschignard2024casereporttwo pages 1-3)
• Seizures and encephalopathy (brain vulnerability to metabolic crisis); one cohort reports that seizures can be “particularly sensitive to biotin therapy, often stopping within minutes to hours of administration.” (ling2023clinicalbiochemicaland pages 4-5)
• Rash/eczema and alopecia (consistent clinical hallmarks). (ling2023clinicalbiochemicaland pages 1-2, wu2020impairedglucosehomeostasis pages 1-2)
• Hypotonia and developmental delay, which may improve with early treatment. (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2)
• Glucose homeostasis disturbances: hypoglycemia is reported in some cases (with profound acidosis), but hyperglycemic ketoacidosis also occurs, particularly during acute management with high glucose infusion. (wu2020impairedglucosehomeostasis pages 1-2, demaret2024insulintherapyin pages 1-2)

Recent developments and latest research (prioritized 2023–2024)
A. Larger contemporary cohort quantifying outcomes and biomarker response (2023)
Ling et al. (Orphanet J Rare Dis; publication date Mar 2023; URL https://doi.org/10.1186/s13023-023-02656-y) analyzed 28 Chinese patients and provided cohort‑level statistics:
• Outcomes: 23/28 (82.1%) “developed healthy,” 3/28 (10.7%) died, and 2/28 (7.1%) were lost to follow‑up; deaths occurred during initial unrecognized metabolic crises without timely biotin. (ling2023clinicalbiochemicaland pages 4-5)
• Biochemical response: median C5OH decreased from 7.01 (3.26–15.01) to 0.35 (0.08–1.87) after biotin therapy (P < 0.001). (ling2023clinicalbiochemicaland pages 4-5, ling2023clinicalbiochemicaland media bf654274)
• Newborn screening: 6 were screened and only 1 was missed, illustrating both feasibility and false‑negative risk if C5OH falls below cutoff. (ling2023clinicalbiochemicaland pages 1-2, ling2023clinicalbiochemicaland pages 5-6)

B. Genotype–biotin responsiveness framework (2023)
The same cohort/report also provides a clinically actionable interpretation of biotin responsiveness:
• Variants in the C‑terminal biotin‑binding domain (aa 448–701) are described as generally biotin‑responsive.
• Variants in the N‑terminal extension/substrate‑binding region (aa 159–314) may be less responsive.
• Dosing guidance summarized: oral biotin commonly 10–40 mg/day, with tapering possible under biochemical monitoring. (ling2023clinicalbiochemicaland pages 5-6)

C. Biotin homeostasis review and subcellular context (2024)
Karachaliou & Livaniou (Int J Mol Sci; Jun 2024; URL https://doi.org/10.3390/ijms25126578) synthesize “recent findings and perspectives” on biotin homeostasis, emphasizing the biotin cycle and the role of HLCS and biotinidase, and noting intracellular distribution of biotin predominantly in mitochondria/cytosol with minor nuclear fractions. This provides an updated conceptual scaffold for HLCS deficiency as a disorder of cofactor activation and recycling. (karachaliou2024biotinhomeostasisand pages 4-5)

D. Acute management innovation: insulin for hyperglycemic ketoacidosis (2024)
Demaret et al. (Mol Genet Metab Rep; Jun 2024; URL https://doi.org/10.1016/j.ymgmr.2024.101073) report hyperglycemic ketoacidosis in HLCS deficiency precipitated by IV glucose intended to promote anabolism; insulin “rapidly corrected biochemical abnormalities and clinical status.” They hypothesize insulinopenia from secondary Krebs cycle disturbances impairing glucose‑stimulated insulin secretion in beta cells. This adds a practical, mechanistically motivated management insight for acute crises. (demaret2024insulintherapyin pages 1-2)

E. Expanded phenotypic spectrum: very late onset (2024)
Gaschignard et al. (Front Genet; Sep 2024; URL https://doi.org/10.3389/fgene.2024.1249480) emphasize that very late onset can occur (11 years symptomatic; 23 years diagnosed), underscoring a need for awareness beyond infancy and potential value of newborn screening to prevent decompensation even in late‑onset genotypes. (gaschignard2024casereporttwo pages 1-3)

Current applications and real‑world implementations
1) Newborn screening
• Many settings use tandem mass spectrometry newborn screening based on elevated C5‑OH (3‑hydroxyisovalerylcarnitine) in dried blood spots; abnormal screens are typically followed by confirmatory urine organic acids by GC/MS and molecular testing of HLCS. (ling2023clinicalbiochemicaland pages 1-2)
• The 2023 cohort explicitly highlights that C5OH can be below cutoff in some cases (false negatives), so second‑tier testing (e.g., urine 3‑hydroxypropionate and methylcitrate) supports differentiation from primary 3‑MCC deficiency and other conditions. (ling2023clinicalbiochemicaland pages 5-6)

2) Molecular diagnosis / precision treatment
• Next‑generation sequencing panels are used for rapid diagnosis in acute neonatal illness and can guide early initiation of biotin therapy. (kim2024dramaticclinicalimprovement pages 2-4)

3) Biotin therapy (disease‑modifying)
• Oral pharmacologic biotin is the primary therapy; a consensus range of 10–40 mg/day is summarized in cohort analysis, with some patients initially treated at 40 mg/day then tapered to 10 mg/day with metabolic monitoring. (ling2023clinicalbiochemicaland pages 5-6)
• Rapid biochemical response is demonstrated in a 2024 neonatal case: lactate decreased from 10.76 to 2.87 mmol/L within one day after biotin, with associated clinical stabilization and subsequent discharge. (kim2024dramaticclinicalimprovement pages 2-4)

4) Acute crisis management
• Standard acute care includes correction of acidosis, provision of calories to suppress catabolism, and rapid initiation of biotin.
• A notable 2024 management update is the use of insulin when high‑glucose infusion precipitates hyperglycemic ketoacidosis during HLCS decompensation, with rapid biochemical and clinical improvement reported. (demaret2024insulintherapyin pages 1-2)

Relevant statistics and data (recent)
Epidemiology:
• Reported incidence estimates vary by source and geography: worldwide ~1/200,000; China ~1/930,600; Japan ~1/100,000 (from a 2023 cohort paper). (ling2023clinicalbiochemicaland pages 1-2)
• A 2024 neonatal case report also cites a broader prevalence range of ~1/100,000 to 1/930,000 live births. (kim2024dramaticclinicalimprovement pages 1-2)

Cohort outcomes and treatment effect (2023):
• In 28 Chinese patients (2006–2021), 23 (82.1%) developed healthy, 3 (10.7%) died, 2 were lost to follow‑up. (ling2023clinicalbiochemicaland pages 4-5)
• Median C5OH improved from 7.01 to 0.35 μmol/L after biotin (P < 0.001). (ling2023clinicalbiochemicaland pages 4-5, ling2023clinicalbiochemicaland media bf654274)

Case‑based quantitative physiology (2024):
• Neonatal HLCS deficiency can present with severe lactic acidosis and hyperammonemia; the 2024 case report provides concrete values (e.g., ammonia 392 μg/dL; lactate 10.09 mmol/L). (kim2024dramaticclinicalimprovement pages 1-2)

Expert opinions / analysis synthesized from authoritative sources
1) Biotin responsiveness is mechanistically and clinically heterogeneous
Cohort analysis indicates that not all genotypes have the same responsiveness and dosing requirements, with domain‑dependent effects (C‑terminal biotin‑binding domain generally responsive vs N‑terminal extension/substrate‑binding region often less responsive). This is a pragmatic genotype‑to‑therapy model that can inform clinical decision‑making and follow‑up biochemical monitoring. (ling2023clinicalbiochemicaland pages 5-6)

2) Early recognition is the major modifiable determinant of outcome
The cohort’s deaths occurred during initial crises without timely biotin, whereas prompt supplementation is repeatedly described as dramatically resolving biochemical abnormalities and supporting normal development for most survivors. The implication is that health‑system interventions (newborn screening, rapid confirmatory testing, and emergent empiric biotin in suspected cases) are central to preventing irreversible neurologic injury and mortality. (ling2023clinicalbiochemicaland pages 4-5, kim2024dramaticclinicalimprovement pages 2-4)

3) Acute management must anticipate atypical metabolic phenotypes
Recent case literature emphasizes that HLCS deficiency can present with glucose dysregulation spanning hypoglycemia to hyperglycemic ketoacidosis. The insulin‑therapy report provides a mechanistic hypothesis (secondary TCA/Krebs cycle disturbance → impaired insulin secretion) and a practical intervention for a potentially iatrogenic complication of high‑glucose therapy during acute organic acidemia management. (demaret2024insulintherapyin pages 1-2, wu2020impairedglucosehomeostasis pages 1-2)

Knowledge‑base–style structured annotations (suggested)

A) Gene/protein annotations
• HLCS (HGNC symbol: HLCS; protein: holocarboxylase synthetase) – causal; GO: “protein biotinylation” (process). Evidence: HLCS deficiency causes loss of biotinylation of multiple carboxylases (PCC, MCC, PC, ACC). (ling2023clinicalbiochemicaland pages 1-2, kim2024dramaticclinicalimprovement pages 1-2)

Proximal enzyme targets:
• PC, PCC, MCC, ACC – decreased activity due to impaired biotinylation. (ling2023clinicalbiochemicaland pages 1-2)

B) GO biological process candidates (dysregulated)
• Protein biotinylation (central).
• Gluconeogenesis / pyruvate metabolism.
• Leucine catabolism.
• Propionate metabolism.
• Fatty acid biosynthesis.
Evidence: described pathway roles for affected carboxylases and associated metabolite changes. (kim2024dramaticclinicalimprovement pages 1-2, ling2023clinicalbiochemicaland pages 1-2)

C) Cellular component candidates
• Mitochondrion; cytosol; nucleus (minor biotin pool).
Evidence: intracellular biotin distribution and mitochondrial carboxylase impact statements. (kim2024dramaticclinicalimprovement pages 2-4, karachaliou2024biotinhomeostasisand pages 4-5)

D) Phenotype (HP) candidates (with mechanistic linkage)
• Metabolic acidosis; lactic acidosis; hyperammonemia; ketosis; seizures; hypotonia; developmental delay; dermatitis/eczema; alopecia; respiratory distress/tachypnea; hypoglycemia; hyperglycemia/ketoacidosis.
Evidence: cohort and multiple case reports. (ling2023clinicalbiochemicaland pages 1-2, ling2023clinicalbiochemicaland pages 4-5, kim2024dramaticclinicalimprovement pages 1-2, demaret2024insulintherapyin pages 1-2)

E) Cell type (CL) candidates (inferred from affected processes)
• Hepatocyte (gluconeogenesis/propionate metabolism), neuron/astrocyte (seizures/encephalopathy), keratinocyte (dermatitis), pancreatic beta cell (insulin secretion hypothesis in hyperglycemic ketoacidosis).
Evidence: clinical phenotype + mechanistic hypothesis for insulinopenia in decompensation. (demaret2024insulintherapyin pages 1-2, ling2023clinicalbiochemicaland pages 1-2)

F) Anatomical location (UBERON) candidates
• Liver; brain; skin; hair follicle; lung (during crisis physiology).
Evidence: phenotype clusters and respiratory presentations. (ling2023clinicalbiochemicaland pages 1-2, zou2024casereporta pages 2-4)

G) Chemical entities (CHEBI) candidates
• Biotin; 3‑hydroxyisovalerylcarnitine (C5OH); lactate; ammonia; methylcitric acid; 3‑hydroxyisovaleric acid; 3‑hydroxypropionic acid; 3‑methylcrotonylglycine; tiglylglycine.
Evidence: screening/urine biomarker panels and case quantitation. (kim2024dramaticclinicalimprovement pages 1-2, demaret2024insulintherapyin pages 1-2)

Evidence items and identifiers (PMIDs)
PMIDs were not provided in the extracted text for most 2023–2024 sources retrieved here; therefore, evidence is referenced using DOI/URL and the cited context IDs. One exception is that OpenTargets evidence for HLCS–holocarboxylase synthetase deficiency includes legacy PMIDs (e.g., 12633764; 27604308; 11735028; 8817339; 9396568) but those papers were not retrieved in full text within this run, so mechanistic quotations were not extracted from them here. (ling2023clinicalbiochemicaland pages 1-2)

Key references (publication date; URL)
• Ling et al. “Clinical, biochemical, and genetic analysis of 28 Chinese patients with holocarboxylase synthetase deficiency.” Orphanet J Rare Dis. Mar 2023. https://doi.org/10.1186/s13023-023-02656-y (ling2023clinicalbiochemicaland pages 1-2, ling2023clinicalbiochemicaland pages 4-5)
• Karachaliou & Livaniou. “Biotin Homeostasis and Human Disorders: Recent Findings and Perspectives.” Int J Mol Sci. Jun 2024. https://doi.org/10.3390/ijms25126578 (karachaliou2024biotinhomeostasisand pages 4-5)
• Demaret et al. “Insulin therapy in acute decompensation of holocarboxylase synthetase deficiency with hyperglycemia and ketoacidosis.” Mol Genet Metab Rep. Jun 2024. https://doi.org/10.1016/j.ymgmr.2024.101073 (demaret2024insulintherapyin pages 1-2)
• Kim et al. “Dramatic Clinical Improvement With Biotin Mega‑Dose Therapy in a Neonate With Holocarboxylase Synthetase Deficiency.” Mol Genet Genomic Med. Aug 2024. https://doi.org/10.1002/mgg3.70002 (kim2024dramaticclinicalimprovement pages 1-2)
• Gaschignard et al. “Case report: Two siblings with very late onset of holocarboxylase synthase deficiency and a mini‑review.” Front Genet. Sep 2024. https://doi.org/10.3389/fgene.2024.1249480 (gaschignard2024casereporttwo pages 1-3)

Included visual evidence
• Table evidence for cohort biochemical response (C5OH pre/post biotin) and outcomes is available from Ling et al. (Table 2 and Table 1 regions). (ling2023clinicalbiochemicaland media bf654274, ling2023clinicalbiochemicaland media ec77cb6e)

References

1. (ling2023clinicalbiochemicaland pages 1-2): Shiying Ling, Wenjuan Qiu, Huiwen Zhang, Lili Liang, Deyun Lu, Ting Chen, Xia Zhan, Yu Wang, Xuefan Gu, and Lianshu Han. Clinical, biochemical, and genetic analysis of 28 chinese patients with holocarboxylase synthetase deficiency. Orphanet Journal of Rare Diseases, Mar 2023. URL: https://doi.org/10.1186/s13023-023-02656-y, doi:10.1186/s13023-023-02656-y. This article has 17 citations and is from a peer-reviewed journal.

2. (kim2024dramaticclinicalimprovement pages 1-2): Seon Woo Kim, Hyeon Joo Lee, Naye Choi, Ee‐Kyung Kim, and Jung Min Ko. Dramatic clinical improvement with biotin mega‐dose therapy in a neonate with holocarboxylase synthetase deficiency. Molecular Genetics & Genomic Medicine, Aug 2024. URL: https://doi.org/10.1002/mgg3.70002, doi:10.1002/mgg3.70002. This article has 2 citations and is from a peer-reviewed journal.

3. (gaschignard2024casereporttwo pages 1-3): Margaux Gaschignard, Louis Domenach, Delphine Lamireau, Claire Guibet, Sandrine Roche, Emmanuel Richard, Isabelle Redonnet-Vernhet, Samir Mesli, and Louis Lebreton. Case report: two siblings with very late onset of holocarboxylase synthase deficiency and a mini-review. Frontiers in Genetics, Sep 2024. URL: https://doi.org/10.3389/fgene.2024.1249480, doi:10.3389/fgene.2024.1249480. This article has 0 citations and is from a peer-reviewed journal.

4. (wu2020impairedglucosehomeostasis pages 4-5): Hsin-Ru Wu, Kuan-Jung Chen, Hui-Pin Hsiao, and Mei-Chyn Chao. Impaired glucose homeostasis and a novel <i>hlcs</i> pathogenic variant in holocarboxylase synthetase deficiency: a report of two cases and brief review. Journal of Pediatric Endocrinology and Metabolism, 33:1481-1486, Aug 2020. URL: https://doi.org/10.1515/jpem-2020-0106, doi:10.1515/jpem-2020-0106. This article has 8 citations and is from a peer-reviewed journal.

5. (ling2023clinicalbiochemicaland pages 4-5): Shiying Ling, Wenjuan Qiu, Huiwen Zhang, Lili Liang, Deyun Lu, Ting Chen, Xia Zhan, Yu Wang, Xuefan Gu, and Lianshu Han. Clinical, biochemical, and genetic analysis of 28 chinese patients with holocarboxylase synthetase deficiency. Orphanet Journal of Rare Diseases, Mar 2023. URL: https://doi.org/10.1186/s13023-023-02656-y, doi:10.1186/s13023-023-02656-y. This article has 17 citations and is from a peer-reviewed journal.

6. (zou2024casereporta pages 2-4): Haiying Zou, Li Yang, Renlong Zhang, and Yao Qin. Case report: a case of holocarboxylase synthetase deficiency with respiratory tract as the initial symptom. Frontiers in Genetics, Nov 2024. URL: https://doi.org/10.3389/fgene.2024.1439343, doi:10.3389/fgene.2024.1439343. This article has 0 citations and is from a peer-reviewed journal.

7. (karachaliou2024biotinhomeostasisand pages 4-5): Chrysoula-Evangelia Karachaliou and Evangelia Livaniou. Biotin homeostasis and human disorders: recent findings and perspectives. International Journal of Molecular Sciences, 25:6578, Jun 2024. URL: https://doi.org/10.3390/ijms25126578, doi:10.3390/ijms25126578. This article has 45 citations.

8. (demaret2024insulintherapyin pages 1-2): Tanguy Demaret, Jean-Sébastien Joyal, Aspasia Karalis, Fabienne Parente, Marie-Ange Delrue, and Grant A. Mitchell. Insulin therapy in acute decompensation of holocarboxylase synthetase deficiency with hyperglycemia and ketoacidosis. Jun 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101073, doi:10.1016/j.ymgmr.2024.101073. This article has 1 citations.

9. (ling2023clinicalbiochemicaland pages 5-6): Shiying Ling, Wenjuan Qiu, Huiwen Zhang, Lili Liang, Deyun Lu, Ting Chen, Xia Zhan, Yu Wang, Xuefan Gu, and Lianshu Han. Clinical, biochemical, and genetic analysis of 28 chinese patients with holocarboxylase synthetase deficiency. Orphanet Journal of Rare Diseases, Mar 2023. URL: https://doi.org/10.1186/s13023-023-02656-y, doi:10.1186/s13023-023-02656-y. This article has 17 citations and is from a peer-reviewed journal.

10. (kim2024dramaticclinicalimprovement pages 2-4): Seon Woo Kim, Hyeon Joo Lee, Naye Choi, Ee‐Kyung Kim, and Jung Min Ko. Dramatic clinical improvement with biotin mega‐dose therapy in a neonate with holocarboxylase synthetase deficiency. Molecular Genetics & Genomic Medicine, Aug 2024. URL: https://doi.org/10.1002/mgg3.70002, doi:10.1002/mgg3.70002. This article has 2 citations and is from a peer-reviewed journal.

11. (wu2020impairedglucosehomeostasis pages 1-2): Hsin-Ru Wu, Kuan-Jung Chen, Hui-Pin Hsiao, and Mei-Chyn Chao. Impaired glucose homeostasis and a novel <i>hlcs</i> pathogenic variant in holocarboxylase synthetase deficiency: a report of two cases and brief review. Journal of Pediatric Endocrinology and Metabolism, 33:1481-1486, Aug 2020. URL: https://doi.org/10.1515/jpem-2020-0106, doi:10.1515/jpem-2020-0106. This article has 8 citations and is from a peer-reviewed journal.

12. (ling2023clinicalbiochemicaland media bf654274): Shiying Ling, Wenjuan Qiu, Huiwen Zhang, Lili Liang, Deyun Lu, Ting Chen, Xia Zhan, Yu Wang, Xuefan Gu, and Lianshu Han. Clinical, biochemical, and genetic analysis of 28 chinese patients with holocarboxylase synthetase deficiency. Orphanet Journal of Rare Diseases, Mar 2023. URL: https://doi.org/10.1186/s13023-023-02656-y, doi:10.1186/s13023-023-02656-y. This article has 17 citations and is from a peer-reviewed journal.

13. (ling2023clinicalbiochemicaland media ec77cb6e): Shiying Ling, Wenjuan Qiu, Huiwen Zhang, Lili Liang, Deyun Lu, Ting Chen, Xia Zhan, Yu Wang, Xuefan Gu, and Lianshu Han. Clinical, biochemical, and genetic analysis of 28 chinese patients with holocarboxylase synthetase deficiency. Orphanet Journal of Rare Diseases, Mar 2023. URL: https://doi.org/10.1186/s13023-023-02656-y, doi:10.1186/s13023-023-02656-y. This article has 17 citations and is from a peer-reviewed journal.
