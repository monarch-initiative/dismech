---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:04:38.756111'
end_time: '2026-02-23T23:32:16.743315'
duration_seconds: 1657.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nonketotic Hyperglycinemia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Nonketotic Hyperglycinemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Nonketotic Hyperglycinemia**.
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
- **Disease Name:** Nonketotic Hyperglycinemia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Nonketotic Hyperglycinemia**.
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


Title: Pathophysiology of Nonketotic Hyperglycinemia (NKH; Glycine Encephalopathy)

Publication window emphasized: 2023–2024 (with selected 2022 supportive clinical implementation data where needed).

1. Disease concept, definitions, and current understanding

1.1 Definition and nosology
Nonketotic hyperglycinemia (NKH), also called glycine encephalopathy, is a rare autosomal recessive inborn error of glycine metabolism caused by deficient activity of the mitochondrial glycine cleavage system (GCS)/glycine cleavage enzyme (GCE). It is characterized biochemically by elevated glycine in blood and cerebrospinal fluid (CSF), with an increased CSF:plasma glycine ratio as a hallmark diagnostic feature. (nyhan2023nonketotichyperglycinemia pages 1-2, zhou2024naturalhistoryand pages 1-2, hirtum2024thebehavioralphenotype pages 1-2)

A commonly cited diagnostic hallmark is an increased CSF:plasma glycine ratio “> 0.08; normal < 0.04”. (nyhan2023nonketotichyperglycinemia pages 1-2)

Clinical categorization is used along two axes:
• Age of onset: neonatal/classical (0–4 weeks), infantile (5 weeks–2 years), and late-onset (>2 years). (zhou2024naturalhistoryand pages 1-2)
• Severity/outcome: severe (“classic”) versus attenuated (sometimes subdivided by developmental quotient into poor/intermediate/good). (hirtum2024thebehavioralphenotype pages 1-2)

1.2 Core biochemical lesion
The GCS normally catabolizes glycine via decarboxylation and transfers a one-carbon unit to tetrahydrofolate (THF) to form 5,10-methylene-THF, thereby supporting serine–glycine–one-carbon (SGOC) metabolism. In NKH, GLDC or AMT mutations (and less commonly GCSH or lipoylation pathway defects) reduce this flux, producing systemic and CNS glycine accumulation and downstream one-carbon deficits. (arribascarreira2024metabolicrewiringand pages 1-2)

2. Core pathophysiology: molecular and cellular mechanisms

2.1 Primary mechanisms: glycine accumulation + one-carbon product deficiency
A recent expert reassessment emphasizes that NKH pathophysiology should be conceptualized as both (i) excess glycine (upstream of the enzymatic block) and (ii) deficiency of 5,10-methylene-tetrahydrofolate (downstream product), with “multifold” adverse effects. (hove2024theroleof pages 3-5)

2.2 Neurotransmission dysregulation: NMDA and glycine receptors
Excess glycine has long been hypothesized to overactivate NMDA receptors because glycine is an endogenous agonist at the NMDA receptor allosteric (co-agonist) site; thus, glycine elevation was proposed to “result in increased activation… leading to seizures, and through neuronal apoptosis to cell death,” motivating NMDA-antagonist trials with dextromethorphan or ketamine. (hove2024theroleof pages 1-3)

However, newer mechanistic interpretation is nuanced: d-serine is also a major NMDA co-agonist and is reduced in NKH brain/CSF, likely due to reduced l-serine availability and inhibition of serine racemase by glycine; this could yield NMDA underactivation depending on region/developmental stage. A 2024 reassessment states that direct experimental evidence for net NMDA over- vs under-activation “has not been explored to date.” (hove2024theroleof pages 1-3)

In parallel, glycine acts at inhibitory strychnine-sensitive glycine receptors, especially in spinal cord and brainstem; a 2024 iPSC-based NKH model review highlights glycine action “on both NMDA receptors in the cortex and glycine receptors in the spinal cord and brain stem neurons,” consistent with mixed excitatory/inhibitory and respiratory network effects (e.g., apnea). (arribascarreira2024metabolicrewiringand pages 1-2)

2.3 SGOC metabolic disruption: nucleotide, redox, and epigenetic consequences
The SGOC axis provides one-carbon units for synthesis of amino acids, nucleotides, and phospholipids and for epigenetic remodeling. Disruption of SGOC metabolism is therefore a plausible contributor to neurodevelopmental pathology beyond excitotoxicity. (arribascarreira2024metabolicrewiringand pages 1-2)

A 2024 patient-derived GLDC-deficient iPSC-to-astrocyte study provides direct cellular evidence of SGOC rewiring:
• GLDC-deficient cells exhibited a “metabolic switch to an altered serine–glycine–one-carbon metabolism” with a “coordinated cell growth and cell cycle proliferation response.” (arribascarreira2024metabolicrewiringand pages 1-2)
• They reported impaired mitochondrial one-carbon enzymes (SHMT2, MTHFD2) with compensatory increases in cytosolic SHMT1/MTHFD1, consistent with shifted subcellular one-carbon partitioning. (arribascarreira2024metabolicrewiringand pages 13-14)
• They observed “nearly 50% decline in the levels of nucleotide metabolites,” reduced proliferative capacity, increased quiescence/senescence signals, and that such rewiring “could influence cell fate during the differentiation process.” (arribascarreira2024metabolicrewiringand pages 13-14, arribascarreira2024metabolicrewiringand pages 14-16)
• Redox stress was implicated by a “substantial decrease in glutathione levels,” suggesting compromised antioxidant buffering and increased ROS burden. (arribascarreira2024metabolicrewiringand pages 14-16)

2.4 Glial biology and neurodevelopment: altered astrocyte-lineage differentiation
The same 2024 iPSC-based model directly supports a glial contribution to disease biology:
• During differentiation, GLDC-deficient neural progenitor cells “shifted towards a more heterogeneous astrocyte lineage” with increased radial glial markers (GFAP, GLAST) and unexpected neuronal marker expression (MAP2, NeuN). (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2024metabolicrewiringand pages 14-16)
• Functional transporter changes were detected, including increased glycine uptake and upregulation of glycine transporters (GLYT1/GLYT2) in patient-derived astrocyte-lineage cells. (arribascarreira2024metabolicrewiringand pages 9-13)
These findings link GLDC deficiency to altered glial differentiation and neurotransmitter handling, which may shape excitability and developmental trajectories. (arribascarreira2024metabolicrewiringand pages 14-16, arribascarreira2024metabolicrewiringand pages 9-13)

2.5 Mitochondrial bioenergetics and lipoylation: “variant NKH” mechanisms
A major 2023 advance is the definition of “variant NKH” caused by defects in protein lipoylation that secondarily disrupt the GCS and key mitochondrial dehydrogenases. The GCSH-encoded H-protein is “moonlighting”: it is required for glycine cleavage and is a mitochondrial lipoate carrier/donor in lipoate biogenesis and transfer. (arribascarreira2023pathogenicvariantsingcshencoding pages 2-3, arribascarreira2023pathogenicvariantsingcshencoding pages 1-2)

Mechanistically, the H-protein cycle depicts how H-protein donates lipoyl groups to bioenergetic enzymes (PDH E2 subunit DLAT; 2-ketoglutarate dehydrogenase E2 subunit DLST) and also participates in glycine degradation by the GCS. (arribascarreira2023pathogenicvariantsingcshencoding media 0157c767)

Functionally, patient cell data show that pathogenic GCSH variants can cause “strongly reduced lipoylated proteins of the E2 subunits of PDH (DLAT) and 2-KGDH (DLST)” and reduced PDH activities, directly linking NKH phenotypes to mitochondrial energy metabolism. (arribascarreira2023pathogenicvariantsingcshencoding pages 5-5)

2.6 Putative additional toxic mediators: oxidative stress and guanidinoacetate
An expert 2024 synthesis lists oxidative stress, direct glycine toxicity, elevation of neurotoxic metabolites such as guanidinoacetate, and secondary neurotransmitter disturbances (e.g., d-serine deficiency) as part of the multifactorial biochemical landscape of NKH. (hove2024theroleof pages 3-5)

Consistent with this, the 2024 iPSC model reports AGAT upregulation and increased arginine absorption compatible with increased guanidinoacetate synthesis as a glycine “exit” route, providing a mechanistic bridge between glycine overload and neurotoxic guanidino compounds. (arribascarreira2024metabolicrewiringand pages 14-16)

3. Key molecular players (knowledge-base oriented)

3.1 Causal genes and protein complex
Core GCS genes/proteins (HGNC symbols):
• GLDC (glycine decarboxylase; “P-protein/GCSP”) (arribascarreira2024metabolicrewiringand pages 1-2, hirtum2024thebehavioralphenotype pages 1-2)
• AMT (aminomethyltransferase; “T-protein/GCST”) (arribascarreira2024metabolicrewiringand pages 1-2, hirtum2024thebehavioralphenotype pages 1-2)
• GCSH (H-protein; lipoyl carrier; “moonlighting” in lipoylation) (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2023pathogenicvariantsingcshencoding pages 2-3)
• DLD (L-protein; dihydrolipoamide dehydrogenase) (arribascarreira2024metabolicrewiringand pages 1-2)

Lipoylation/bioenergetic links:
• LIAS, LIPT1 (lipoate synthesis/transfer; pathway context) (arribascarreira2023pathogenicvariantsingcshencoding pages 2-3)
• DLAT (PDH E2), DLST (2-KGDH E2) (arribascarreira2023pathogenicvariantsingcshencoding pages 5-5, arribascarreira2023pathogenicvariantsingcshencoding media 0157c767)

SGOC and associated metabolic rewiring observed in patient-derived models:
• SHMT1/SHMT2, MTHFD1/MTHFD2; PHGDH, PSAT1, PSPH; SRR (serine racemase); SLC6A9 (GlyT1), SLC6A5 (GlyT2); GFAP, SLC1A3 (GLAST); AGAT (GATM). (arribascarreira2024metabolicrewiringand pages 13-14, arribascarreira2024metabolicrewiringand pages 14-16, arribascarreira2024metabolicrewiringand pages 9-13)

3.2 Key chemical entities / metabolites (CHEBI-aligned)
• Glycine (diagnostic and toxic mediator) (zhou2024naturalhistoryand pages 1-2, hirtum2024thebehavioralphenotype pages 1-2)
• THF / 5,10-methylene-THF (downstream one-carbon product deficiency concept) (arribascarreira2024metabolicrewiringand pages 1-2, hove2024theroleof pages 3-5)
• l-serine / d-serine (NMDA co-agonist biology; d-serine reduced in NKH) (hove2024theroleof pages 1-3)
• Lipoic acid (cofactor biology via GCSH) (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2023pathogenicvariantsingcshencoding pages 2-3)
• Glutathione (redox buffering decreased in GLDC-deficient iPSC model) (arribascarreira2024metabolicrewiringand pages 14-16)
• Guanidinoacetate (neurotoxic metabolite implicated) (arribascarreira2024metabolicrewiringand pages 14-16, hove2024theroleof pages 3-5)
• Hippurate (benzoate conjugation product for glycine excretion) (hirtum2024thebehavioralphenotype pages 1-2, yuan2025theprecisemolecular pages 3-4)

4. Cellular components and subcellular localization
Key processes localize to:
• Mitochondria: GCS complex, lipoylation cycle (H-protein), PDH/2-KGDH lipoylation, mitochondrial one-carbon enzymes (e.g., SHMT2/MTHFD2) (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2023pathogenicvariantsingcshencoding pages 2-3)
• Cytosol: compensatory one-carbon flux (SHMT1/MTHFD1 upregulation in GLDC-deficient cells) (arribascarreira2024metabolicrewiringand pages 13-14)
• Plasma membrane: glycine/glutamate transporters (GLYT1/2, GLAST) in patient-derived astrocytes (arribascarreira2024metabolicrewiringand pages 9-13)

5. Disease progression and stages (sequence of events)

5.1 Typical clinical sequence (severe neonatal form)
Many patients present within hours to days after birth with poor feeding, profound hypotonia, apnea, hiccups, and severe myoclonic seizures progressing rapidly to coma. Survivors often develop intractable seizures and intellectual disability. (nyhan2023nonketotichyperglycinemia pages 1-2)

5.2 Heterogeneity and attenuated courses
Attenuated NKH can present neonatally or later and can include treatable/absent epilepsy and variable developmental progress. In attenuated/intermediate-to-good cohorts, ADHD-like maladaptive behaviors occur frequently (reported in >2/3). (hirtum2024thebehavioralphenotype pages 1-2)

6. Phenotypic manifestations and links to mechanisms (HP-aligned)

Key phenotypes observed across cohorts and consistent with the mechanistic landscape include:
• Developmental and epileptic encephalopathy / seizures / status epilepticus (NMDA/glycine receptor dysregulation; metabolic toxicity) (zhou2024naturalhistoryand pages 1-2, hove2024theroleof pages 5-6)
• Hypotonia and lethargy (global metabolic/neurotransmitter disruption) (zhou2024naturalhistoryand pages 1-2)
• Apnea/respiratory failure (brainstem glycinergic signaling and severe neonatal encephalopathy) (zhou2024naturalhistoryand pages 1-2, arribascarreira2024metabolicrewiringand pages 1-2)
• Structural brain abnormalities including corpus callosum dysplasia/hypogenesis and white matter abnormalities (neurodevelopmental and metabolic mechanisms; possibly SGOC/epigenetic and glial differentiation effects) (zhou2024naturalhistoryand pages 1-2, nyhan2023nonketotichyperglycinemia pages 1-2)
• Behavioral dysregulation (ADHD-like features) in attenuated NKH (mechanisms unclear; association with dextromethorphan use reported) (hirtum2024thebehavioralphenotype pages 1-2)

7. Recent developments (2023–2024 prioritized)

7.1 2024: Human cell models implicate SGOC rewiring and glial differentiation defects
Patient-derived GLDC-deficient iPSC-to-astrocyte differentiation revealed: altered serine–glycine–one-carbon metabolism, reduced nucleotide pools, reduced glutathione (redox stress), altered proliferation/cell cycle, and a shift toward heterogeneous astrocyte/radial glial phenotypes with transporter changes. These findings provide a mechanistic bridge between the enzymatic defect and neurodevelopmental phenotypes beyond “glycine excitotoxicity.” (arribascarreira2024metabolicrewiringand pages 13-14, arribascarreira2024metabolicrewiringand pages 14-16)

7.2 2024: Expert reassessment challenges simplistic NMDA-overactivation model
A 2024 critical reassessment highlights that d-serine deficiency complicates the assumption that elevated glycine necessarily overactivates NMDA receptors, and notes the lack of direct experimental proof for net NMDA over- vs under-activation in NKH models/organoids. (hove2024theroleof pages 1-3)

7.3 2023: “Variant NKH” via GCSH moonlighting links NKH to lipoate/PDH/2-KGDH defects
Identification of pathogenic GCSH variants causing combined NKH and lipoate deficiency expands disease biology from a single metabolic block to coupled bioenergetic failure via impaired lipoylation of PDH/2-KGDH E2 subunits. (arribascarreira2023pathogenicvariantsingcshencoding pages 2-3, arribascarreira2023pathogenicvariantsingcshencoding pages 5-5)

8. Current applications and real-world implementations

8.1 Diagnostics (biochemical + genetic)
Biochemical diagnosis uses plasma and CSF glycine and CSF:plasma glycine ratio; a commonly cited cutoff is ratio >0.08 (normal <0.04). (nyhan2023nonketotichyperglycinemia pages 1-2, zhou2024naturalhistoryand pages 1-2)

Recent cohort statistics (China; Frontiers in Neurology, published 14 Aug 2024, https://doi.org/10.3389/fneur.2024.1440883): median CSF glycine 135.2 μmol/L (range 6.3–546.3), median plasma glycine 998.2 μmol/L (range 75–3084), median CSF/plasma ratio 0.16 (range 0.03–0.60). (zhou2024naturalhistoryand pages 1-2)

Genetic confirmation commonly identifies GLDC and AMT variants; in the 2024 China cohort, GLDC variants were observed in 65% (13/20) and AMT in 35% (7/20). (zhou2024naturalhistoryand pages 1-2)

8.2 Standard-of-care: glycine reduction
Sodium benzoate is a mainstay to lower glycine. In attenuated NKH management descriptions, benzoate “conjugates with glycine and is excreted in the urine as hippurate.” (hirtum2024thebehavioralphenotype pages 1-2)

Clinical targets commonly aim for plasma glycine ~120–300 μM. (hirtum2024thebehavioralphenotype pages 1-2, shelkowitz2022ketogenicdietas pages 1-2)

8.3 Dietary implementation: ketogenic diet (KD)
KD is used clinically as an additional glycine-lowering strategy, described mechanistically as using glycine as a gluconeogenic precursor. (hirtum2024thebehavioralphenotype pages 1-2)

In a multi-center retrospective series (published 12 Dec 2022; https://doi.org/10.1186/s13023-022-02581-6), six infants switching from high-dose benzoate to KD + low-dose benzoate had ~28% lower plasma glycine on KD vs benzoate monotherapy; brain glycine by MRS was reduced but not normalized; half had seizure reduction. (shelkowitz2022ketogenicdietas pages 1-2)

8.4 Symptom-targeted neurotransmission modulation: dextromethorphan and ketamine
NMDA antagonists (dextromethorphan, ketamine) are used in practice, often for refractory neonatal seizures/status epilepticus. (hove2024theroleof pages 5-6)

Evidence quality is limited. A 2024 expert review states: “Controlled clinical studies of dextromethorphan or ketamine… have never been done,” and “Today insufficient evidence exists to consider it a proven primary treatment.” (hove2024theroleof pages 1-3)

Safety and implementation considerations include complex pharmacology of dextromethorphan and potential behavioral effects in attenuated NKH cohorts, and concerns about chronic ketamine use. (hove2024theroleof pages 1-3, hirtum2024thebehavioralphenotype pages 1-2)

8.5 Medication cautions
Sodium valproate is commonly discouraged because it “increases both CSF and plasma glycine level, leading to worsening of seizures.” (nyhan2023nonketotichyperglycinemia pages 2-3)

9. Natural history, epidemiology, and recent statistics

9.1 Incidence
A 2024 NKH cohort paper cites worldwide incidence ~1/76,000 and higher prevalence in northern Finland (1:12,000), and Taiwan incidence 7.2/1,000,000. (zhou2024naturalhistoryand pages 1-2)

9.2 Symptom frequencies and outcomes (2024 cohort statistics)
In the 2024 China series (n=20), 85% were neonatal-onset and 15% infantile-onset. Presenting features included seizures (15/20), lethargy (14/20), hypotonia (11/20), apnea (9/20). (zhou2024naturalhistoryand pages 1-2)

Outcome data were available for 18 cases: 9 died, with 8 deaths in the neonatal period; survivors had varying developmental disorders. The authors conclude glycine measures do not reliably predict prognosis, whereas MRI/EEG abnormalities may indicate poor outlook. (zhou2024naturalhistoryand pages 1-2)

10. Ontology-oriented annotation sets (starter mappings)

10.1 Genes/proteins (HGNC)
• GLDC; AMT; GCSH; DLD; DLAT; DLST (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2023pathogenicvariantsingcshencoding pages 5-5)

10.2 Candidate disrupted GO biological processes (examples)
• Glycine catabolic process / glycine cleavage (GCS function) (arribascarreira2024metabolicrewiringand pages 1-2)
• One-carbon metabolic process / folate-mediated one-carbon metabolism (5,10-methylene-THF generation; SGOC flux) (arribascarreira2024metabolicrewiringand pages 1-2)
• Mitochondrial protein lipoylation (GCSH moonlighting; PDH/2-KGDH lipoylation) (arribascarreira2023pathogenicvariantsingcshencoding pages 2-3, arribascarreira2023pathogenicvariantsingcshencoding pages 5-5)
• Regulation of cell cycle / cellular proliferation (iPSC model: proliferation/quiescence shifts) (arribascarreira2024metabolicrewiringand pages 14-16)
• Response to oxidative stress / glutathione metabolic process (reduced glutathione) (arribascarreira2024metabolicrewiringand pages 14-16)

10.3 Cellular components (GO CC; examples)
• Mitochondrial matrix / mitochondrion (GCS complex; lipoylation; mitochondrial one-carbon enzymes) (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2023pathogenicvariantsingcshencoding pages 2-3)
• Cytosol (compensatory cytosolic one-carbon enzymes) (arribascarreira2024metabolicrewiringand pages 13-14)
• Plasma membrane transporter complexes (GLYT1/2, GLAST changes) (arribascarreira2024metabolicrewiringand pages 9-13)

10.4 Cell types (CL; examples)
• Astrocyte-lineage cells / iPSC-derived astrocytes (altered differentiation and transport) (arribascarreira2024metabolicrewiringand pages 9-13)
• Radial glia / neural progenitor cells (shift in lineage markers; proposed relevance of GCS expression in radial glia) (arribascarreira2024metabolicrewiringand pages 14-16)

10.5 Anatomy (UBERON; examples)
• Brain/CNS, including cortex (NMDA co-agonism), brainstem/spinal cord (glycinergic receptor biology), white matter/basal ganglia regions affected on MRI/MRS (arribascarreira2024metabolicrewiringand pages 1-2, zhou2024naturalhistoryand pages 1-2)
• Liver, kidney, lung as GCS-active tissues in adults (arribascarreira2024metabolicrewiringand pages 1-2)

10.6 Phenotypes (HP; examples)
• Seizures, burst suppression/hypsarrhythmia (EEG) (zhou2024naturalhistoryand pages 1-2)
• Hypotonia, lethargy, apnea (zhou2024naturalhistoryand pages 1-2)
• Developmental delay/intellectual disability; behavioral abnormalities (hyperactivity/ADHD-like) (hirtum2024thebehavioralphenotype pages 1-2)
• Corpus callosum abnormalities; white matter abnormalities (zhou2024naturalhistoryand pages 1-2)

11. Evidence items (selected, with URLs and dates)

A. Natural history/outcomes cohort
• Zhou et al., “Natural history and outcome of nonketotic hyperglycinemia in China,” Frontiers in Neurology, published 14 Aug 2024. https://doi.org/10.3389/fneur.2024.1440883 (zhou2024naturalhistoryand pages 1-2)

B. Mechanistic human cellular model
• Arribas-Carreira et al., “Metabolic Rewiring and Altered Glial Differentiation in an iPSC-Derived Astrocyte Model Derived from a Nonketotic Hyperglycinemia Patient,” Int J Mol Sci, published 28 Feb 2024. https://doi.org/10.3390/ijms25052814 (arribascarreira2024metabolicrewiringand pages 1-2, arribascarreira2024metabolicrewiringand pages 14-16)

C. Variant NKH / lipoylation biology
• Arribas-Carreira et al., “Pathogenic variants in GCSH encoding the moonlighting H-protein cause combined nonketotic hyperglycinemia and lipoate deficiency,” Human Molecular Genetics, published 2023 (issue dated Oct 2023). https://doi.org/10.1093/hmg/ddac246 (arribascarreira2023pathogenicvariantsingcshencoding pages 2-3, arribascarreira2023pathogenicvariantsingcshencoding pages 5-5)
• Key pathway schematic image (Figure 1: H-protein cycle) (arribascarreira2023pathogenicvariantsingcshencoding media 0157c767)

D. Expert reassessment of NMDA antagonist therapy
• Van Hove, “The role of NMDA-receptor type glutamatergic antagonists dextromethorphan or ketamine in the treatment of nonketotic hyperglycinemia: A critical reassessment,” Molecular Genetics and Metabolism, Nov 2024. https://doi.org/10.1016/j.ymgme.2024.108594 (hove2024theroleof pages 1-3, hove2024theroleof pages 3-5)

E. Attenuated phenotype and treatment framing
• Van Hirtum et al., “The behavioral phenotype of children and adolescents with attenuated non-ketotic hyperglycinemia,” Orphanet J Rare Dis, Apr 2024. https://doi.org/10.1186/s13023-024-03172-3 (hirtum2024thebehavioralphenotype pages 1-2)

12. Gaps and expert interpretation

Despite mechanistic plausibility and widespread off-label clinical use of NMDA antagonists, the best available expert review (2024) concludes that controlled trials have not been done and evidence is insufficient to designate dextromethorphan/ketamine as proven primary therapies; by contrast, glycine reduction (benzoate and/or KD) has accumulating observational evidence for improved alertness and seizure control. (hove2024theroleof pages 1-3)

Recent iPSC-based disease modeling supports that NKH pathophysiology plausibly includes (and may substantially depend on) SGOC-driven limitations in nucleotide/redox metabolism and altered glial differentiation, suggesting that future therapies may need to target both neurotransmission and metabolic/one-carbon/bioenergetic biology. (arribascarreira2024metabolicrewiringand pages 14-16)


References

1. (nyhan2023nonketotichyperglycinemia pages 1-2): W. L. Nyhan, Georg F. Hoffmann, A. Al-aqeel, and B. Barshop. Nonketotic hyperglycinemia. Atlas of Inherited Metabolic Diseases, Jul 2023. URL: https://doi.org/10.1201/b15310-25, doi:10.1201/b15310-25. This article has 33 citations.

2. (zhou2024naturalhistoryand pages 1-2): Zhizi Zhou, Yanna Cai, Xiuzhen Li, Zongcai Liu, Minzhi Peng, Yunting Lin, Xiaojian Mao, Chunhua Zeng, Li Liu, and Wen Zhang. Natural history and outcome of nonketotic hyperglycinemia in china. Frontiers in Neurology, Aug 2024. URL: https://doi.org/10.3389/fneur.2024.1440883, doi:10.3389/fneur.2024.1440883. This article has 3 citations and is from a peer-reviewed journal.

3. (hirtum2024thebehavioralphenotype pages 1-2): Liesbet D. F. M. Van Hirtum, Tine Van Damme, Johan L. K. Van Hove, and Jean G. Steyaert. The behavioral phenotype of children and adolescents with attenuated non-ketotic hyperglycinemia, intermediate to good subtype. Orphanet Journal of Rare Diseases, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03172-3, doi:10.1186/s13023-024-03172-3. This article has 4 citations and is from a peer-reviewed journal.

4. (arribascarreira2024metabolicrewiringand pages 1-2): Laura Arribas-Carreira, Margarita Castro, Fernando García, Rosa Navarrete, Irene Bravo-Alonso, Francisco Zafra, Magdalena Ugarte, Eva Richard, Belén Pérez, and Pilar Rodríguez-Pombo. Metabolic rewiring and altered glial differentiation in an ipsc-derived astrocyte model derived from a nonketotic hyperglycinemia patient. International Journal of Molecular Sciences, 25:2814, Feb 2024. URL: https://doi.org/10.3390/ijms25052814, doi:10.3390/ijms25052814. This article has 4 citations.

5. (hove2024theroleof pages 3-5): Johan L.K. Van Hove. The role of nmda-receptor type glutamatergic antagonists dextromethorphan or ketamine in the treatment of nonketotic hyperglycinemia: a critical reassessment. Molecular Genetics and Metabolism, 143(3):108594, Nov 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108594, doi:10.1016/j.ymgme.2024.108594. This article has 8 citations and is from a peer-reviewed journal.

6. (hove2024theroleof pages 1-3): Johan L.K. Van Hove. The role of nmda-receptor type glutamatergic antagonists dextromethorphan or ketamine in the treatment of nonketotic hyperglycinemia: a critical reassessment. Molecular Genetics and Metabolism, 143(3):108594, Nov 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108594, doi:10.1016/j.ymgme.2024.108594. This article has 8 citations and is from a peer-reviewed journal.

7. (arribascarreira2024metabolicrewiringand pages 13-14): Laura Arribas-Carreira, Margarita Castro, Fernando García, Rosa Navarrete, Irene Bravo-Alonso, Francisco Zafra, Magdalena Ugarte, Eva Richard, Belén Pérez, and Pilar Rodríguez-Pombo. Metabolic rewiring and altered glial differentiation in an ipsc-derived astrocyte model derived from a nonketotic hyperglycinemia patient. International Journal of Molecular Sciences, 25:2814, Feb 2024. URL: https://doi.org/10.3390/ijms25052814, doi:10.3390/ijms25052814. This article has 4 citations.

8. (arribascarreira2024metabolicrewiringand pages 14-16): Laura Arribas-Carreira, Margarita Castro, Fernando García, Rosa Navarrete, Irene Bravo-Alonso, Francisco Zafra, Magdalena Ugarte, Eva Richard, Belén Pérez, and Pilar Rodríguez-Pombo. Metabolic rewiring and altered glial differentiation in an ipsc-derived astrocyte model derived from a nonketotic hyperglycinemia patient. International Journal of Molecular Sciences, 25:2814, Feb 2024. URL: https://doi.org/10.3390/ijms25052814, doi:10.3390/ijms25052814. This article has 4 citations.

9. (arribascarreira2024metabolicrewiringand pages 9-13): Laura Arribas-Carreira, Margarita Castro, Fernando García, Rosa Navarrete, Irene Bravo-Alonso, Francisco Zafra, Magdalena Ugarte, Eva Richard, Belén Pérez, and Pilar Rodríguez-Pombo. Metabolic rewiring and altered glial differentiation in an ipsc-derived astrocyte model derived from a nonketotic hyperglycinemia patient. International Journal of Molecular Sciences, 25:2814, Feb 2024. URL: https://doi.org/10.3390/ijms25052814, doi:10.3390/ijms25052814. This article has 4 citations.

10. (arribascarreira2023pathogenicvariantsingcshencoding pages 2-3): Laura Arribas-Carreira, Cristina Dallabona, Michael A Swanson, Joseph Farris, Elsebet Østergaard, Konstantinos Tsiakas, Maja Hempel, Cecile Aquaviva-Bourdain, Stefanos Koutsoukos, Nicholas V Stence, Martina Magistrati, Elaine B Spector, Kathryn Kronquist, Mette Christensen, Helena G Karstensen, René G Feichtinger, Melanie T Achleitner, J Lawrence Merritt II, Belén Pérez, Magdalena Ugarte, Stephanie Grünewald, Anthony R Riela, Natalia Julve, Jean-Baptiste Arnoux, Kasturi Haldar, Claudia Donnini, René Santer, Allan M Lund, Johannes A Mayr, Pilar Rodriguez-Pombo, and Johan L K Van Hove. Pathogenic variants in<i>gcsh</i>encoding the moonlighting h-protein cause combined nonketotic hyperglycinemia and lipoate deficiency. Human Molecular Genetics, 32(6):917-933, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac246, doi:10.1093/hmg/ddac246. This article has 16 citations and is from a domain leading peer-reviewed journal.

11. (arribascarreira2023pathogenicvariantsingcshencoding pages 1-2): Laura Arribas-Carreira, Cristina Dallabona, Michael A Swanson, Joseph Farris, Elsebet Østergaard, Konstantinos Tsiakas, Maja Hempel, Cecile Aquaviva-Bourdain, Stefanos Koutsoukos, Nicholas V Stence, Martina Magistrati, Elaine B Spector, Kathryn Kronquist, Mette Christensen, Helena G Karstensen, René G Feichtinger, Melanie T Achleitner, J Lawrence Merritt II, Belén Pérez, Magdalena Ugarte, Stephanie Grünewald, Anthony R Riela, Natalia Julve, Jean-Baptiste Arnoux, Kasturi Haldar, Claudia Donnini, René Santer, Allan M Lund, Johannes A Mayr, Pilar Rodriguez-Pombo, and Johan L K Van Hove. Pathogenic variants in<i>gcsh</i>encoding the moonlighting h-protein cause combined nonketotic hyperglycinemia and lipoate deficiency. Human Molecular Genetics, 32(6):917-933, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac246, doi:10.1093/hmg/ddac246. This article has 16 citations and is from a domain leading peer-reviewed journal.

12. (arribascarreira2023pathogenicvariantsingcshencoding media 0157c767): Laura Arribas-Carreira, Cristina Dallabona, Michael A Swanson, Joseph Farris, Elsebet Østergaard, Konstantinos Tsiakas, Maja Hempel, Cecile Aquaviva-Bourdain, Stefanos Koutsoukos, Nicholas V Stence, Martina Magistrati, Elaine B Spector, Kathryn Kronquist, Mette Christensen, Helena G Karstensen, René G Feichtinger, Melanie T Achleitner, J Lawrence Merritt II, Belén Pérez, Magdalena Ugarte, Stephanie Grünewald, Anthony R Riela, Natalia Julve, Jean-Baptiste Arnoux, Kasturi Haldar, Claudia Donnini, René Santer, Allan M Lund, Johannes A Mayr, Pilar Rodriguez-Pombo, and Johan L K Van Hove. Pathogenic variants in<i>gcsh</i>encoding the moonlighting h-protein cause combined nonketotic hyperglycinemia and lipoate deficiency. Human Molecular Genetics, 32(6):917-933, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac246, doi:10.1093/hmg/ddac246. This article has 16 citations and is from a domain leading peer-reviewed journal.

13. (arribascarreira2023pathogenicvariantsingcshencoding pages 5-5): Laura Arribas-Carreira, Cristina Dallabona, Michael A Swanson, Joseph Farris, Elsebet Østergaard, Konstantinos Tsiakas, Maja Hempel, Cecile Aquaviva-Bourdain, Stefanos Koutsoukos, Nicholas V Stence, Martina Magistrati, Elaine B Spector, Kathryn Kronquist, Mette Christensen, Helena G Karstensen, René G Feichtinger, Melanie T Achleitner, J Lawrence Merritt II, Belén Pérez, Magdalena Ugarte, Stephanie Grünewald, Anthony R Riela, Natalia Julve, Jean-Baptiste Arnoux, Kasturi Haldar, Claudia Donnini, René Santer, Allan M Lund, Johannes A Mayr, Pilar Rodriguez-Pombo, and Johan L K Van Hove. Pathogenic variants in<i>gcsh</i>encoding the moonlighting h-protein cause combined nonketotic hyperglycinemia and lipoate deficiency. Human Molecular Genetics, 32(6):917-933, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac246, doi:10.1093/hmg/ddac246. This article has 16 citations and is from a domain leading peer-reviewed journal.

14. (yuan2025theprecisemolecular pages 3-4): Fang Yuan, Xiaozhen Song, Rongrong Yin, Xiaoping Lan, Jingjing Sun, Xiaojun Tang, Wuhen Xu, Shaohua Hu, Man Xiao, Hong Zhang, Wenhao Weng, Yuanfeng Zhang, and Shengnan Wu. The precise molecular diagnosis of novel gldc compound heterozygous variants highlights the benefits for a chinese family with nonketotic hyperglycinemia. Jun 2025. URL: https://doi.org/10.1016/j.ymgmr.2025.101209, doi:10.1016/j.ymgmr.2025.101209. This article has 1 citations.

15. (hove2024theroleof pages 5-6): Johan L.K. Van Hove. The role of nmda-receptor type glutamatergic antagonists dextromethorphan or ketamine in the treatment of nonketotic hyperglycinemia: a critical reassessment. Molecular Genetics and Metabolism, 143(3):108594, Nov 2024. URL: https://doi.org/10.1016/j.ymgme.2024.108594, doi:10.1016/j.ymgme.2024.108594. This article has 8 citations and is from a peer-reviewed journal.

16. (shelkowitz2022ketogenicdietas pages 1-2): Emily Shelkowitz, Russell P. Saneto, Walla Al-Hertani, Charlotte M. A. Lubout, Nicholas V. Stence, Mark S. Brown, Patrick Long, Diana Walleigh, Julie A. Nelson, Francisco E. Perez, Dennis W. W. Shaw, Emma J. Michl, and Johan L. K. Van Hove. Ketogenic diet as a glycine lowering therapy in nonketotic hyperglycinemia and impact on brain glycine levels. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02581-6, doi:10.1186/s13023-022-02581-6. This article has 19 citations and is from a peer-reviewed journal.

17. (nyhan2023nonketotichyperglycinemia pages 2-3): W. L. Nyhan, Georg F. Hoffmann, A. Al-aqeel, and B. Barshop. Nonketotic hyperglycinemia. Atlas of Inherited Metabolic Diseases, Jul 2023. URL: https://doi.org/10.1201/b15310-25, doi:10.1201/b15310-25. This article has 33 citations.
