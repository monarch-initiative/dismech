---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:20:51.078320'
end_time: '2026-02-23T23:43:48.189548'
duration_seconds: 1377.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple Acyl-CoA Dehydrogenase Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Multiple Acyl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple Acyl-CoA Dehydrogenase Deficiency**.
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
- **Disease Name:** Multiple Acyl-CoA Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Multiple Acyl-CoA Dehydrogenase Deficiency**.
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


Title: Pathophysiology of Multiple Acyl‑CoA Dehydrogenase Deficiency (MADD) / Glutaric aciduria type II (GAII)

Publication window emphasized: 2023–2024, with key mechanistic anchors from landmark primary literature.

1. Disease definition, nomenclature, and identifiers

Multiple acyl‑CoA dehydrogenase deficiency (MADD) is an autosomal recessive inborn error of mitochondrial energy metabolism, also called glutaric aciduria/acidemia type II (GAII). (bisschoff2024clinicalbiochemicaland pages 1-2)

Identifiers reported in recent literature/databases:

• MONDO: MONDO_0009282 (multiple acyl‑CoA dehydrogenase deficiency) (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)
• ORPHAcode: 26791 (MADD) (bisschoff2024clinicalbiochemicaland pages 1-2)
• OMIM/MIM disease: 231680 (GAII/MADD) (li2024fatalmultipleacylcoa pages 3-4, martino2024deepintronicetfdh pages 1-2, schee2024multipleacylcoadehydrogenase pages 1-2)

Clinical phenotype groupings are commonly described as three forms:

• Type I: neonatal onset with congenital anomalies (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2)
• Type II: neonatal onset without congenital anomalies (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2)
• Type III: later onset (often “late‑onset” or “mild”), frequently riboflavin responsive (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2)

Incidence estimates in recent sources are approximately ~1 in 200,000 births globally (bisschoff2024clinicalbiochemicaland pages 1-2, martino2024deepintronicetfdh pages 1-2), and a Russia expanded newborn screening report observed 1:205,233 live births (баранова2024клиникогенетическаяхарактеристикапациентов pages 1-2).

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Normal electron transfer hub that couples substrate oxidation to the respiratory chain

The defining biochemical lesion in MADD is impaired electron transfer from multiple flavoprotein dehydrogenases to the mitochondrial ubiquinone (coenzyme Q) pool.

Recent review language: “These proteins transfer electrons from acyl‑CoA dehydrogenases to coenzyme Q10 in the mitochondrial respiratory chain,” and deficiency of ETFDH or ETFA/ETFB causes MADD. (aragao2024revitalisingriboflavinunveiling pages 10-12)

Mechanistic “wiring diagram” (2024 Nature Metabolism): ETFDH “receives electrons from electron‑transfer flavoprotein (ETF) and reduces Q to QH2.” (martin2024anetfdhdrivenmetabolon pages 1-2) A pathway schematic depicting electron flow from fatty acids/BCAAs/choline through ETF→ETFDH→CoQ and into OXPHOS is shown in the figures from this work. (martin2024anetfdhdrivenmetabolon media f5fb06a9)

Landmark mechanistic statement (2007 Brain): MADD reflects defective transfer of electrons from multiple FAD‑dependent dehydrogenases to the respiratory chain, with electrons transferred via ETF and ETF:QO (ETFDH) to ubiquinone (CoQ). (olsen2007etfdhmutationsas pages 2-2)

2.2 Dysregulated pathways and cellular processes

A. Mitochondrial fatty‑acid β‑oxidation (FAO) and amino‑acid catabolism

Because ETF/ETFDH is a shared acceptor system for multiple acyl‑CoA dehydrogenases, impaired ETF/ETFDH function produces a “multiple dehydrogenase” block. Clinically and biochemically, this manifests as accumulation of fatty‑acid and amino‑acid derived metabolites and broad acylcarnitine elevations. (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2, martino2024deepintronicetfdh pages 1-2)

B. CoQ redox homeostasis and OXPHOS dysfunction (recent mechanistic advance)

A major 2024 advance is the demonstration that ETFDH is not only an electron acceptor for substrate dehydrogenation, but can participate structurally/organizationally in respiratory chain function through a proposed “metabolon”:

Martín et al. (Nature Metabolism, publication date Jan 2024, https://doi.org/10.1038/s42255-023-00956-y) identify a complex comprising ETFDH, complex III (CIII), and the Q‑biosynthesis regulator COQ2 that “maintains total Q levels, minimizes QH2‑reductive stress and improves OXPHOS efficiency.” (martin2024anetfdhdrivenmetabolon pages 1-2)

Loss of ETFDH in vivo caused CIII inhibition, pathological accumulation of reduced Q (QH2) and “reductive stress,” with increased ROS and bioenergetic impairment, supporting a mechanistic bridge from the primary ETFDH lesion to broader respiratory chain dysfunction. (martin2024anetfdhdrivenmetabolon pages 1-2)

C. Oxidative stress and apoptosis (neuronal vulnerability)

A 2024 cellular‑mechanistic study links ETFDH mutations to pro‑apoptotic signaling and neurite pathology:

Lin et al. (Scientific Reports, publication date Oct 2024, https://doi.org/10.1038/s41598-024-75286-4) report that cellular models carrying a common ETFDH mutation show “neurite growth defects and excessive apoptosis,” with increased pro‑apoptotic markers (including BAX, cytochrome c, caspase‑9 and caspase‑3) consistent with a BCL‑2 family/MOMP apoptotic cascade. (lin2024etfdhmutationinvolves pages 1-2, lin2024etfdhmutationinvolves pages 7-8)

In the same work, coenzyme Q10 reduced apoptotic protein activation and mitigated neurite growth defects, supporting a mechanistic chain from impaired ETFDH→CoQ/ETC redox disturbance→ROS stress→apoptosis/axon‑neurite degeneration. (lin2024etfdhmutationinvolves pages 1-2)

D. Lipid storage myopathy as a cellular/organ consequence

Clinical cohorts repeatedly document lipid accumulation in skeletal muscle consistent with defective FAO and energy deficiency. (aragao2024revitalisingriboflavinunveiling pages 10-12, schee2024multipleacylcoadehydrogenase pages 2-3)

3. Key molecular players (genes/proteins, metabolites/chemicals, cells, and tissues)

3.1 Causal genes/proteins (HGNC symbols)

Core causal genes:

• ETFA (electron transfer flavoprotein subunit alpha) (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2)
• ETFB (electron transfer flavoprotein subunit beta) (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2)
• ETFDH (electron transfer flavoprotein dehydrogenase; ETF‑QO/ETF:ubiquinone oxidoreductase) (li2024fatalmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 1-2)

Additional genes that can phenocopy “riboflavin‑responsive MADD” by disrupting FAD supply/handling:

• FLAD1 (FAD synthetase; riboflavin‑responsive lipid storage myopathy/MADD‑like phenotype described and compared with ETFDH‑MADD) (wen2024acomparativestudy pages 4-6, OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)
• SLC25A32 (mitochondrial flavin transporter; OpenTargets association evidence) (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)

Evidence links between disease and these targets are curated in Open Targets (MONDO_0009282) with supporting literature PMIDs listed (e.g., ETFDH: PMID 16527485, 12359134, 19249206, 20370797; ETFA/ETFB also have multiple PMIDs listed). (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)

3.2 Chemical entities / metabolites (examples; mapable to ChEBI)

Diagnostic/accumulating metabolites:

• Acylcarnitines: broad elevations (short/medium/long chain), used in NBS and in acute workups (martino2024deepintronicetfdh pages 1-2, rao2023lateonsetmultipleacylcoa pages 2-3)
• Glutaric acid and related dicarboxylic acids; ethylmalonic acid; 2‑hydroxyglutarate; glycine conjugates (martino2024deepintronicetfdh pages 1-2)

Therapeutic/management chemicals:

• Riboflavin (vitamin B2) → precursor of FAD/FMN; often clinically effective, especially in late‑onset ETFDH‑MADD (murgia2023newinsightsinto pages 7-8, schee2024multipleacylcoadehydrogenase pages 2-3)
• L‑carnitine (used to address secondary carnitine depletion and support acyl group handling) (rao2023lateonsetmultipleacylcoa pages 4-5, bisschoff2024clinicalbiochemicaland pages 1-2)
• Coenzyme Q10 (CoQ10; ubiquinone) supplementation used in practice and supported by cellular mechanistic rescue in neurite/apoptosis model (lin2024etfdhmutationinvolves pages 1-2, daher2024diagnosticchallengesand pages 6-8)

3.3 Cell types (examples; mapable to CL)

• Skeletal muscle myofibers (lipid droplet accumulation; lipid storage myopathy) (schee2024multipleacylcoadehydrogenase pages 2-3)
• Motor neuron–like cells in vitro (NSC‑34) used to model neurite/apoptosis phenotypes in ETFDH mutation context (lin2024etfdhmutationinvolves pages 1-2)

3.4 Anatomical locations / organs (examples; mapable to UBERON)

Dominant organ systems involved are consistent with high oxidative demand and FAO reliance:

• Skeletal muscle (myopathy, rhabdomyolysis, lipid storage myopathy) (schee2024multipleacylcoadehydrogenase pages 2-3)
• Liver (hepatomegaly/liver dysfunction in severe presentations) (rao2023lateonsetmultipleacylcoa pages 3-4)
• Heart (cardiomyopathy/arrhythmia risk) (rao2023lateonsetmultipleacylcoa pages 3-4)
• Brain (encephalopathy, hyperammonemic crises; neurite/apoptosis mechanisms) (rao2023lateonsetmultipleacylcoa pages 2-3, lin2024etfdhmutationinvolves pages 1-2)

4. Biological processes and cellular components (GO-oriented annotation suggestions)

The following GO terms are consistent with mechanistic evidence in 2007–2024 literature (term names provided for knowledge‑base mapping; exact GO IDs should be assigned in curation workflows):

Disrupted biological processes (GO:BP term names):

• Fatty acid beta‑oxidation / mitochondrial fatty acid oxidation (blocked upstream at multiple acyl‑CoA dehydrogenases due to ETF/ETFDH electron transfer failure) (schee2024multipleacylcoadehydrogenase pages 1-2, olsen2007etfdhmutationsas pages 2-2)
• Electron transport chain / mitochondrial electron transport to ubiquinone (ETF→ETFDH→Q) (martin2024anetfdhdrivenmetabolon pages 1-2, olsen2007etfdhmutationsas pages 2-2)
• Ubiquinone (coenzyme Q) redox homeostasis; regulation of respiratory chain complex III activity (ETFDH–CIII–COQ2 metabolon concept) (martin2024anetfdhdrivenmetabolon pages 1-2)
• Response to oxidative stress / reactive oxygen species metabolic process (ETFDH loss → ROS increase) (martin2024anetfdhdrivenmetabolon pages 1-2, lin2024etfdhmutationinvolves pages 7-8)
• Intrinsic apoptotic signaling pathway (mitochondrial outer membrane permeabilization; caspase cascade) (lin2024etfdhmutationinvolves pages 1-2, lin2024etfdhmutationinvolves pages 7-8)

Cellular components (GO:CC term names):

• Mitochondrion
• Inner mitochondrial membrane (ETFDH is an IMM protein with FAD and 4Fe‑4S cluster) (martin2024anetfdhdrivenmetabolon pages 1-2)
• Respiratory chain complex III (functional interaction/metabolon with ETFDH) (martin2024anetfdhdrivenmetabolon pages 1-2)

5. Disease progression model (from molecular defect to clinical manifestations)

5.1 Initiating lesion

Biallelic pathogenic variants in ETFA/ETFB/ETFDH (and in some related flavin homeostasis genes such as FLAD1) reduce functional electron transfer from multiple acyl‑CoA dehydrogenases to ubiquinone, leading to impaired substrate oxidation and energy deficit. (li2024fatalmultipleacylcoa pages 3-4, OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II, olsen2007etfdhmutationsas pages 2-2)

5.2 Early biochemical consequences

• Accumulation of characteristic acylcarnitines (often broad) and organic acids (dicarboxylic acids, glutaric acid, ethylmalonic acid, 2‑hydroxyglutarate, glycine conjugates). (martino2024deepintronicetfdh pages 1-2, rao2023lateonsetmultipleacylcoa pages 2-3)
• Secondary carnitine depletion can occur (noted in late‑onset fatal case report as reduced carnitine with broad acylcarnitine elevations). (li2024fatalmultipleacylcoa pages 3-4)

5.3 Cellular pathophysiology

• Mitochondrial bioenergetic impairment due to reduced electron flow and altered Q pool redox state; recent evidence indicates ETFDH helps maintain complex III activity and Q homeostasis in skeletal muscle, limiting electron leak/ROS. (martin2024anetfdhdrivenmetabolon pages 1-2)
• Increased ROS and redox stress downstream of ETFDH loss (Etfdh−/− models) (martin2024anetfdhdrivenmetabolon pages 1-2)
• Neuronal susceptibility via BCL‑2 family/MOMP apoptosis signaling and impaired neurite outgrowth in ETFDH mutation models; CoQ10 can mitigate these defects in vitro. (lin2024etfdhmutationinvolves pages 1-2)

5.4 Clinical decompensation triggers and crises

Catabolic stress increases reliance on FAO; when FAO is compromised, patients can decompensate.

Rao et al. (BMJ Case Rep, May 2023, https://doi.org/10.1136/bcr-2022-252668) describe a late‑onset case with recent gastroenteritis and postpartum state, with hypoglycemia, high anion gap metabolic acidosis, hyperammonemia, and elevated ketones (noting that ketones may still be present but inappropriately low for hypoglycemia). (rao2023lateonsetmultipleacylcoa pages 2-3, rao2023lateonsetmultipleacylcoa pages 4-5)

6. Phenotypic manifestations (HP-oriented mapping suggestions) and recent statistics

6.1 Clinical phenotypes (examples; mapable to HPO)

Severe neonatal forms (types I/II; or severe MADD‑S):

• Early severe metabolic acidosis and hypoglycemia, hypotonia, hepatomegaly; high mortality is noted in cohort descriptions/reviews. (martino2024deepintronicetfdh pages 1-2, rao2023lateonsetmultipleacylcoa pages 1-2)

Late‑onset (type III; often riboflavin responsive):

• Proximal muscle weakness, exercise intolerance, myalgia, episodic rhabdomyolysis; can present with encephalopathy/hyperammonemia during crises. (rao2023lateonsetmultipleacylcoa pages 1-2, rao2023lateonsetmultipleacylcoa pages 2-3)

6.2 Cohort statistics (recent)

Sex distribution (systematic review/meta-analysis):

Ma et al. (Orphanet J Rare Dis, Feb 2024, https://doi.org/10.1186/s13023-024-03072-6) included 34 studies with 609 late‑onset MADD patients and found the pooled proportion of males was 58% (95% CI 54–63%; I2 = 2.99%). Ethnicity was a moderator, with East‑Asian studies showing higher male proportion and higher ETFDH hotspot variant proportion. (ma2024themaletofemaleratio pages 1-2, ma2024themaletofemaleratio pages 2-5)

Clinical severity in a 2024 late‑onset cohort:

Schee et al. (J Clin Neurol, May 2024, https://doi.org/10.3988/jcn.2023.0265) reported 14 late‑onset patients; 3/14 (21%) had respiratory insufficiency requiring mechanical ventilation at first presentation, and 1 patient died during an ICU admission with severe metabolic crisis/rhabdomyolysis/acute renal failure. (schee2024multipleacylcoadehydrogenase pages 2-3)

7. Diagnostics and real-world implementation (2023–2024)

7.1 Newborn screening and biochemical confirmation

Biochemical screening and diagnostic testing remain central:

• Tandem MS/MS acylcarnitine profiling is widely used in newborn screening programs and to support diagnosis, while urine organic acids (GC–MS) are used for confirmation and characterization of accumulated metabolites. (martino2024deepintronicetfdh pages 1-2, martino2024deepintronicetfdh pages 2-3)

Real-world program examples:

• Russia expanded NBS (added Jan 2023): 27 referrals for confirmatory testing; 6 confirmed GA2 cases; observed frequency 1:205,233 live births. (баранова2024клиникогенетическаяхарактеристикапациентов pages 1-2)
• A large neonatal tandem MS screening cohort (2018–2021; N=29,948) identified FAOD cases including at least one MADD recall; the authors emphasize combining TMS with urine GC–MS and gene sequencing. (wang2023clinicalandgene pages 1-2)

7.2 Genetic testing advances (2024): deep intronic variants and RNA-based diagnosis

Martino et al. (IJMS, Sep 2024, https://doi.org/10.3390/ijms25179637) highlight that exome/gene panels may miss deep intronic splice-altering variants, and demonstrate that combining WGS with RNA‑seq identified a deep intronic ETFDH variant causing pseudo‑exon inclusion in lethal neonatal MADD. (martino2024deepintronicetfdh pages 1-2)

8. Current applications and treatments (standard-of-care; real-world outcomes)

8.1 Riboflavin responsiveness and dosing ranges

Riboflavin is commonly used, particularly in late‑onset ETFDH‑MADD.

• Clinical cohort: Schee et al. used riboflavin 100 mg/day; survivors “improved dramatically” with symptom resolution and CK normalization, and remained in remission on maintenance 100 mg/day. (schee2024multipleacylcoadehydrogenase pages 2-3)
• Practice guidance in late‑onset case-based review: riboflavin “100–300 mg/day,” carnitine “100–200 mg/kg/day,” and CoQ10 when indicated, with emphasis on fasting avoidance and sick-day plans. (rao2023lateonsetmultipleacylcoa pages 4-5)
• Mechanistic framing of responsiveness: riboflavin increases FAD availability and may stabilize mutant ETFDH/ETF‑QO folding/function; structural and biochemical evidence supporting this model appears in both 2007 Brain and 2023 Nutrition & Metabolism discussions. (olsen2007etfdhmutationsas pages 6-7, murgia2023newinsightsinto pages 7-8)

8.2 L‑carnitine and CoQ10 supplementation

• In a Lebanese late‑onset MAD deficiency case (Daher et al., Aug 2024, https://doi.org/10.1186/s13023-024-03325-4), riboflavin (300 mg/day), high-dose L‑carnitine (50 mg/kg/day), and CoQ10 (200 mg/day) were reported with “significant myopathy improvement” and prevention of recurrent rhabdomyolysis. (daher2024diagnosticchallengesand pages 6-8)

• Lin et al. provide experimental support that CoQ10 can mitigate apoptosis/neurite defects in ETFDH‑mutant cells. (lin2024etfdhmutationinvolves pages 1-2)

8.3 Dietary and emergency management

• Dietary strategies in late‑onset MADD focus on avoiding fasting and limiting fat/protein while ensuring adequate carbohydrate intake; Rao et al. describe inpatient use of IV dextrose/insulin to suppress catabolism during crisis and later low-protein feeding plus riboflavin and carnitine, with explicit “sick day plan” planning. (rao2023lateonsetmultipleacylcoa pages 2-3, rao2023lateonsetmultipleacylcoa pages 3-4)

9. Expert interpretation (authoritative analysis grounded in the cited sources)

9.1 Updated “systems” view of MADD pathophysiology

Recent mechanistic work suggests that MADD should be conceptualized not only as a proximal FAO/AA oxidation block, but also as a disorder of mitochondrial redox organization: ETFDH can regulate coenzyme Q homeostasis and complex III efficiency in skeletal muscle, and ETFDH deficiency can therefore propagate dysfunction across the OXPHOS system through Q pool redox stress and ROS. (martin2024anetfdhdrivenmetabolon pages 1-2)

9.2 Tissue vulnerability

The convergence of (i) energy failure in FAO‑dependent states, (ii) redox stress/ROS propagation, and (iii) apoptosis signaling provides a mechanistic rationale for the observed multi-organ phenotype spanning skeletal muscle (lipid storage myopathy/rhabdomyolysis), liver metabolic failure, cardiomyopathy risk, and encephalopathy/neurologic involvement. (rao2023lateonsetmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 2-3, lin2024etfdhmutationinvolves pages 1-2)

10. Evidence items (PMID-focused list where available in provided sources)

Primary mechanistic anchors:

• ETFDH→ubiquinone electron transfer / riboflavin-responsive MADD genetics: Olsen et al., Brain (Aug 2007), https://doi.org/10.1093/brain/awm135. (olsen2007etfdhmutationsas pages 1-2, olsen2007etfdhmutationsas pages 2-2)
• ETFDH–CIII–COQ2 metabolon; Q redox stress; ROS/OXPHOS efficiency: Martín et al., Nature Metabolism (Jan 2024), https://doi.org/10.1038/s42255-023-00956-y. (martin2024anetfdhdrivenmetabolon pages 1-2)
• Apoptosis/neurite defects and CoQ10 rescue in ETFDH mutation models: Lin et al., Scientific Reports (Oct 2024), https://doi.org/10.1038/s41598-024-75286-4. (lin2024etfdhmutationinvolves pages 1-2)

PMIDs explicitly listed in Open Targets evidence for MONDO_0009282 (ETFDH association) include: 16527485, 12359134, 19249206, 20370797. (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)

11. Knowledge-base-ready annotation block (structured summary)

Pathophysiology description (narrative)

MADD/GAII is an autosomal recessive disorder caused by biallelic pathogenic variants in ETFA, ETFB, or ETFDH (and related flavin handling genes in some riboflavin-responsive MADD-like phenotypes). These genes encode components of the electron transfer flavoprotein system that shuttles electrons from multiple FAD-dependent acyl‑CoA dehydrogenases to the mitochondrial ubiquinone (coenzyme Q) pool. Defective ETF/ETFDH-mediated electron transfer produces a functional block in mitochondrial fatty‑acid β‑oxidation and related amino‑acid oxidation pathways, resulting in characteristic acylcarnitine and organic-acid accumulations and a systemic tendency to energy failure during catabolic stress. Recent work further demonstrates that ETFDH can participate in an ETFDH–complex III–COQ2 “metabolon” that supports complex III function and coenzyme Q homeostasis; ETFDH deficiency can thereby induce QH2 reductive stress, increase mitochondrial ROS, and impair OXPHOS efficiency. In neuronal models of ETFDH mutations, oxidative stress links to BCL‑2 family/MOMP signaling with caspase activation, causing apoptosis and neurite outgrowth defects, which can be mitigated by coenzyme Q10.

Gene/protein annotations (HGNC symbols; suggested GO term names)

• ETFDH: inner mitochondrial membrane flavoprotein; electron transfer from ETF to ubiquinone; regulation of respiratory chain complex III efficiency; coenzyme Q redox homeostasis; response to oxidative stress. (martin2024anetfdhdrivenmetabolon pages 1-2, olsen2007etfdhmutationsas pages 2-2)
• ETFA/ETFB: ETF subunits enabling electron transfer from multiple acyl‑CoA dehydrogenases into ETFDH/CoQ. (olsen2007etfdhmutationsas pages 2-2, aragao2024revitalisingriboflavinunveiling pages 10-12)
• FLAD1: FAD synthesis; riboflavin-responsive MADD-like lipid storage myopathy. (wen2024acomparativestudy pages 4-6)
• SLC25A32: mitochondrial flavin transport association evidence (Open Targets). (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)

Phenotype associations (suggested HPO term names)

• Hypoglycemia; metabolic acidosis; hyperammonemia; encephalopathy; muscle weakness; rhabdomyolysis; lipid storage myopathy; cardiomyopathy/arrhythmia risk; hepatomegaly/liver dysfunction; respiratory insufficiency in severe late-onset cohorts. (rao2023lateonsetmultipleacylcoa pages 2-3, rao2023lateonsetmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 2-3)

Cell types (suggested CL term names)

• Skeletal muscle cell / myofiber; motor neuron–like cells (NSC-34 model). (schee2024multipleacylcoadehydrogenase pages 2-3, lin2024etfdhmutationinvolves pages 1-2)

Anatomy (suggested UBERON term names)

• Skeletal muscle, liver, heart, brain. (rao2023lateonsetmultipleacylcoa pages 3-4, schee2024multipleacylcoadehydrogenase pages 2-3)

Chemical entities (examples; mapable to ChEBI)

• Riboflavin; FAD; coenzyme Q10; L‑carnitine; acylcarnitines; glutaric acid; ethylmalonic acid; 2‑hydroxyglutarate. (martino2024deepintronicetfdh pages 1-2, rao2023lateonsetmultipleacylcoa pages 4-5)

Figure evidence

A pathway schematic of ETF→ETFDH→CoQ electron flow and its connection to OXPHOS is provided in the Nature Metabolism 2024 figures. (martin2024anetfdhdrivenmetabolon media f5fb06a9)

URLs and publication dates (selected)

• Martín et al., Nature Metabolism, Jan 2024: https://doi.org/10.1038/s42255-023-00956-y (martin2024anetfdhdrivenmetabolon pages 1-2)
• Lin et al., Scientific Reports, Oct 2024: https://doi.org/10.1038/s41598-024-75286-4 (lin2024etfdhmutationinvolves pages 1-2)
• Martino et al., Int J Mol Sci, Sep 2024: https://doi.org/10.3390/ijms25179637 (martino2024deepintronicetfdh pages 1-2)
• Ma et al., Orphanet J Rare Dis, Feb 2024: https://doi.org/10.1186/s13023-024-03072-6 (ma2024themaletofemaleratio pages 1-2)
• Schee et al., J Clin Neurol, May 2024: https://doi.org/10.3988/jcn.2023.0265 (schee2024multipleacylcoadehydrogenase pages 2-3)
• Rao et al., BMJ Case Reports, May 2023: https://doi.org/10.1136/bcr-2022-252668 (rao2023lateonsetmultipleacylcoa pages 2-3)
• Olsen et al., Brain, Aug 2007: https://doi.org/10.1093/brain/awm135 (olsen2007etfdhmutationsas pages 1-2)

Limitations note

Some requested items (e.g., comprehensive GO/HP/CL/UBERON ID codes and a fully enumerated list of all causal/associated PMIDs beyond those explicitly present in the provided evidence snippets and OpenTargets listing) require a dedicated ontology cross-referencing step and/or additional full-text retrieval beyond the current evidence set; the mechanistic narrative and statistics above are restricted to statements supported directly by the cited sources. (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II)

References

1. (bisschoff2024clinicalbiochemicaland pages 1-2): Michelle Bisschoff, Izelle Smuts, Marli Dercksen, Maryke Schoonen, Barend C. Vorster, George van der Watt, Careni Spencer, Kireshnee Naidu, Franclo Henning, Surita Meldau, Robert McFarland, Robert W. Taylor, Krutik Patel, Mahmoud R. Fassad, Jana Vandrovcova, Ronald J. A. Wanders, and Francois H. van der Westhuizen. Clinical, biochemical, and genetic spectrum of madd in a south african cohort: an icgnmd study. Orphanet Journal of Rare Diseases, Jan 2024. URL: https://doi.org/10.1186/s13023-023-03014-8, doi:10.1186/s13023-023-03014-8. This article has 3 citations and is from a peer-reviewed journal.

2. (OpenTargets Search: Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II): Open Targets Query (Multiple acyl-CoA dehydrogenase deficiency,Glutaric acidemia type II,Glutaric aciduria type II, 20 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (li2024fatalmultipleacylcoa pages 3-4): Xue-Xia Li, Xiao-Nan Yang, Hu-Dan Pan, and Liang Liu. Fatal multiple acyl-coa dehydrogenase deficiency caused by etfdh gene mutation: a case report. World Journal of Clinical Cases, 12:5422-5430, Aug 2024. URL: https://doi.org/10.12998/wjcc.v12.i23.5422, doi:10.12998/wjcc.v12.i23.5422. This article has 0 citations.

4. (martino2024deepintronicetfdh pages 1-2): Stefania Martino, Pietro D’Addabbo, Antonella Turchiano, Francesca Clementina Radio, Alessandro Bruselles, Viviana Cordeddu, Cecilia Mancini, Alessandro Stella, Nicola Laforgia, Donatella Capodiferro, Simonetta Simonetti, Rosanna Bagnulo, Orazio Palumbo, Flaviana Marzano, Ornella Tabaku, Antonella Garganese, Michele Stasi, Marco Tartaglia, Graziano Pesole, and Nicoletta Resta. Deep intronic etfdh variants represent a recurrent pathogenic event in multiple acyl-coa dehydrogenase deficiency. International Journal of Molecular Sciences, 25:9637, Sep 2024. URL: https://doi.org/10.3390/ijms25179637, doi:10.3390/ijms25179637. This article has 3 citations.

5. (schee2024multipleacylcoadehydrogenase pages 1-2): Jie Ping Schee, Joo San Tan, Cheng Yin Tan, Nortina Shahrizaila, Kum Thong Wong, and Khean Jin Goh. Multiple acyl-coa dehydrogenase deficiency: phenotypic and genetic features of a malaysian cohort. Journal of Clinical Neurology (Seoul, Korea), 20:422-430, May 2024. URL: https://doi.org/10.3988/jcn.2023.0265, doi:10.3988/jcn.2023.0265. This article has 2 citations.

6. (баранова2024клиникогенетическаяхарактеристикапациентов pages 1-2): ПВ Баранова and ГВ Байдакова. Клинико-генетическая характеристика пациентов с глутаровой ацидурией типа 2, выявленных по программе расширенного неонатального скрининга в …. Unknown journal, 2024.

7. (aragao2024revitalisingriboflavinunveiling pages 10-12): M. Ângela Aragão, Lara Pires, Celestino Santos-Buelga, Lillian Barros, and Ricardo C. Calhelha. Revitalising riboflavin: unveiling its timeless significance in human physiology and health. Foods, 13:2255, Jul 2024. URL: https://doi.org/10.3390/foods13142255, doi:10.3390/foods13142255. This article has 31 citations.

8. (martin2024anetfdhdrivenmetabolon pages 1-2): Juan Cruz Herrero Martín, Beñat Salegi Ansa, Gerardo Álvarez-Rivera, Sonia Domínguez-Zorita, Pilar Rodríguez-Pombo, Belén Pérez, Enrique Calvo, Alberto Paradela, David G. Miguez, Alejandro Cifuentes, José M. Cuezva, and Laura Formentini. An etfdh-driven metabolon supports oxphos efficiency in skeletal muscle by regulating coenzyme q homeostasis. Nature Metabolism, 6:209-225, Jan 2024. URL: https://doi.org/10.1038/s42255-023-00956-y, doi:10.1038/s42255-023-00956-y. This article has 33 citations and is from a domain leading peer-reviewed journal.

9. (martin2024anetfdhdrivenmetabolon media f5fb06a9): Juan Cruz Herrero Martín, Beñat Salegi Ansa, Gerardo Álvarez-Rivera, Sonia Domínguez-Zorita, Pilar Rodríguez-Pombo, Belén Pérez, Enrique Calvo, Alberto Paradela, David G. Miguez, Alejandro Cifuentes, José M. Cuezva, and Laura Formentini. An etfdh-driven metabolon supports oxphos efficiency in skeletal muscle by regulating coenzyme q homeostasis. Nature Metabolism, 6:209-225, Jan 2024. URL: https://doi.org/10.1038/s42255-023-00956-y, doi:10.1038/s42255-023-00956-y. This article has 33 citations and is from a domain leading peer-reviewed journal.

10. (olsen2007etfdhmutationsas pages 2-2): R. K. J. Olsen, S. E. Olpin, B. S. Andresen, Z. H. Miedzybrodzka, M. Pourfarzam, B. Merinero, F. E. Frerman, M. W. Beresford, J. C. S. Dean, N. Cornelius, O. Andersen, A. Oldfors, E. Holme, N. Gregersen, D. M. Turnbull, and A. A. M. Morris. Etfdh mutations as a major cause of riboflavin-responsive multiple acyl-coa dehydrogenation deficiency. Brain : a journal of neurology, 130 Pt 8:2045-54, Aug 2007. URL: https://doi.org/10.1093/brain/awm135, doi:10.1093/brain/awm135. This article has 374 citations.

11. (lin2024etfdhmutationinvolves pages 1-2): Chuang-Yu Lin, Wen-Chen Liang, Yi-Chen Yu, Shin-Cheng Chang, Ming-Chi Lai, and Yuh-Jyh Jong. Etfdh mutation involves excessive apoptosis and neurite outgrowth defect via bcl2 pathway. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-75286-4, doi:10.1038/s41598-024-75286-4. This article has 1 citations and is from a peer-reviewed journal.

12. (lin2024etfdhmutationinvolves pages 7-8): Chuang-Yu Lin, Wen-Chen Liang, Yi-Chen Yu, Shin-Cheng Chang, Ming-Chi Lai, and Yuh-Jyh Jong. Etfdh mutation involves excessive apoptosis and neurite outgrowth defect via bcl2 pathway. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-75286-4, doi:10.1038/s41598-024-75286-4. This article has 1 citations and is from a peer-reviewed journal.

13. (schee2024multipleacylcoadehydrogenase pages 2-3): Jie Ping Schee, Joo San Tan, Cheng Yin Tan, Nortina Shahrizaila, Kum Thong Wong, and Khean Jin Goh. Multiple acyl-coa dehydrogenase deficiency: phenotypic and genetic features of a malaysian cohort. Journal of Clinical Neurology (Seoul, Korea), 20:422-430, May 2024. URL: https://doi.org/10.3988/jcn.2023.0265, doi:10.3988/jcn.2023.0265. This article has 2 citations.

14. (wen2024acomparativestudy pages 4-6): Bing Wen, Runqi Tang, Shuyao Tang, Yuan Sun, Jingwen Xu, Dandan Zhao, Tan Wang, and Chuanzhu Yan. A comparative study on riboflavin responsive multiple acyl-coa dehydrogenation deficiency due to variants in flad1 and etfdh gene. Journal of human genetics, 69:125-131, Jan 2024. URL: https://doi.org/10.1038/s10038-023-01216-3, doi:10.1038/s10038-023-01216-3. This article has 10 citations and is from a peer-reviewed journal.

15. (rao2023lateonsetmultipleacylcoa pages 2-3): Naini Nishita Rao, Kharis Burns, Catherine Manolikos, and Samantha Hodge. Late-onset multiple acyl-coa dehydrogenase deficiency: an insidious presentation. BMJ Case Reports, 16:e252668, May 2023. URL: https://doi.org/10.1136/bcr-2022-252668, doi:10.1136/bcr-2022-252668. This article has 6 citations and is from a peer-reviewed journal.

16. (murgia2023newinsightsinto pages 7-8): Chiara Murgia, Ankush Dehlia, and Mark A. Guthridge. New insights into the nutritional genomics of adult-onset riboflavin-responsive diseases. Nutrition & Metabolism, Oct 2023. URL: https://doi.org/10.1186/s12986-023-00764-x, doi:10.1186/s12986-023-00764-x. This article has 18 citations and is from a peer-reviewed journal.

17. (rao2023lateonsetmultipleacylcoa pages 4-5): Naini Nishita Rao, Kharis Burns, Catherine Manolikos, and Samantha Hodge. Late-onset multiple acyl-coa dehydrogenase deficiency: an insidious presentation. BMJ Case Reports, 16:e252668, May 2023. URL: https://doi.org/10.1136/bcr-2022-252668, doi:10.1136/bcr-2022-252668. This article has 6 citations and is from a peer-reviewed journal.

18. (daher2024diagnosticchallengesand pages 6-8): Rose T. Daher, Katia El Taoum, Jinane Samaha, and Pascale E. Karam. Diagnostic challenges and outcome of fatty acid oxidation defects in a tertiary care center in lebanon. Orphanet Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1186/s13023-024-03325-4, doi:10.1186/s13023-024-03325-4. This article has 0 citations and is from a peer-reviewed journal.

19. (rao2023lateonsetmultipleacylcoa pages 3-4): Naini Nishita Rao, Kharis Burns, Catherine Manolikos, and Samantha Hodge. Late-onset multiple acyl-coa dehydrogenase deficiency: an insidious presentation. BMJ Case Reports, 16:e252668, May 2023. URL: https://doi.org/10.1136/bcr-2022-252668, doi:10.1136/bcr-2022-252668. This article has 6 citations and is from a peer-reviewed journal.

20. (rao2023lateonsetmultipleacylcoa pages 1-2): Naini Nishita Rao, Kharis Burns, Catherine Manolikos, and Samantha Hodge. Late-onset multiple acyl-coa dehydrogenase deficiency: an insidious presentation. BMJ Case Reports, 16:e252668, May 2023. URL: https://doi.org/10.1136/bcr-2022-252668, doi:10.1136/bcr-2022-252668. This article has 6 citations and is from a peer-reviewed journal.

21. (ma2024themaletofemaleratio pages 1-2): Jing Ma, Huiqiu Zhang, Feng Liang, Guanxi Li, Xiaomin Pang, Rongjuan Zhao, Juan Wang, Xueli Chang, Junhong Guo, and Wei Zhang. The male-to-female ratio in late-onset multiple acyl-coa dehydrogenase deficiency: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Feb 2024. URL: https://doi.org/10.1186/s13023-024-03072-6, doi:10.1186/s13023-024-03072-6. This article has 10 citations and is from a peer-reviewed journal.

22. (ma2024themaletofemaleratio pages 2-5): Jing Ma, Huiqiu Zhang, Feng Liang, Guanxi Li, Xiaomin Pang, Rongjuan Zhao, Juan Wang, Xueli Chang, Junhong Guo, and Wei Zhang. The male-to-female ratio in late-onset multiple acyl-coa dehydrogenase deficiency: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Feb 2024. URL: https://doi.org/10.1186/s13023-024-03072-6, doi:10.1186/s13023-024-03072-6. This article has 10 citations and is from a peer-reviewed journal.

23. (martino2024deepintronicetfdh pages 2-3): Stefania Martino, Pietro D’Addabbo, Antonella Turchiano, Francesca Clementina Radio, Alessandro Bruselles, Viviana Cordeddu, Cecilia Mancini, Alessandro Stella, Nicola Laforgia, Donatella Capodiferro, Simonetta Simonetti, Rosanna Bagnulo, Orazio Palumbo, Flaviana Marzano, Ornella Tabaku, Antonella Garganese, Michele Stasi, Marco Tartaglia, Graziano Pesole, and Nicoletta Resta. Deep intronic etfdh variants represent a recurrent pathogenic event in multiple acyl-coa dehydrogenase deficiency. International Journal of Molecular Sciences, 25:9637, Sep 2024. URL: https://doi.org/10.3390/ijms25179637, doi:10.3390/ijms25179637. This article has 3 citations.

24. (wang2023clinicalandgene pages 1-2): Xiaoxia Wang and Haining Fang. Clinical and gene analysis of fatty acid oxidation disorders found in neonatal tandem mass spectrometry screening. Pharmacogenomics and Personalized Medicine, 16:577-587, Jun 2023. URL: https://doi.org/10.2147/pgpm.s402760, doi:10.2147/pgpm.s402760. This article has 4 citations and is from a peer-reviewed journal.

25. (olsen2007etfdhmutationsas pages 6-7): R. K. J. Olsen, S. E. Olpin, B. S. Andresen, Z. H. Miedzybrodzka, M. Pourfarzam, B. Merinero, F. E. Frerman, M. W. Beresford, J. C. S. Dean, N. Cornelius, O. Andersen, A. Oldfors, E. Holme, N. Gregersen, D. M. Turnbull, and A. A. M. Morris. Etfdh mutations as a major cause of riboflavin-responsive multiple acyl-coa dehydrogenation deficiency. Brain : a journal of neurology, 130 Pt 8:2045-54, Aug 2007. URL: https://doi.org/10.1093/brain/awm135, doi:10.1093/brain/awm135. This article has 374 citations.

26. (olsen2007etfdhmutationsas pages 1-2): R. K. J. Olsen, S. E. Olpin, B. S. Andresen, Z. H. Miedzybrodzka, M. Pourfarzam, B. Merinero, F. E. Frerman, M. W. Beresford, J. C. S. Dean, N. Cornelius, O. Andersen, A. Oldfors, E. Holme, N. Gregersen, D. M. Turnbull, and A. A. M. Morris. Etfdh mutations as a major cause of riboflavin-responsive multiple acyl-coa dehydrogenation deficiency. Brain : a journal of neurology, 130 Pt 8:2045-54, Aug 2007. URL: https://doi.org/10.1093/brain/awm135, doi:10.1093/brain/awm135. This article has 374 citations.
