---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:22:20.895857'
end_time: '2026-02-23T23:50:01.816674'
duration_seconds: 1660.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: L-2-Hydroxyglutaric Aciduria
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** L-2-Hydroxyglutaric Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **L-2-Hydroxyglutaric Aciduria**.
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
- **Disease Name:** L-2-Hydroxyglutaric Aciduria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **L-2-Hydroxyglutaric Aciduria**.
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


Title: Pathophysiology of L-2-Hydroxyglutaric Aciduria (L2HGA) — 2026 evidence-based report

Target disease: L-2-hydroxyglutaric aciduria (L2HGA)
Category: Genetic neurometabolic disorder (autosomal recessive cerebral organic aciduria; “disorder of metabolite repair”) (kranendijk2012progressinunderstanding pages 7-8)

MONDO ID: Not retrieved from tools in this run (OpenTargets disease mapping failed) (ma2017l2hgdhdeficiencyaccumulates pages 1-2)

1. Key concepts and current definitions

Disease definition and biochemical hallmark
L2HGA is defined by abnormal accumulation of the metabolite L-2-hydroxyglutarate (L-2-HG) in body fluids (urine, plasma, CSF) (kranendijk2012progressinunderstanding pages 1-3). In a large review of 2-hydroxyglutaric acidurias, urinary L-2-HG was reported to be ~10–300× higher than controls, with elevated plasma and CSF; CSF/plasma ratio can exceed 1, consistent with brain enrichment (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 9-11).

Causative gene, enzyme function, and subcellular localization
The core causal gene for L2HGA is L2HGDH, encoding the FAD-dependent enzyme L-2-hydroxyglutarate dehydrogenase (L-2-HGDH) (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 1-3). L-2-HGDH catalyzes oxidation of L-2-HG back to α-ketoglutarate/2-ketoglutarate (2-KG) using FAD (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 9-11). Mechanistically, L-2-HG is produced endogenously as an off-pathway (“non-specific side reaction”) product from 2-KG by L-malate dehydrogenase (L-malDH) using NADH; L-2-HGDH therefore functions as a metabolite-repair enzyme that clears this aberrant metabolite (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 1-3).

Mitochondrial localization is a key concept: L2HGDH is described as a mitochondrial enzyme in a 2024 epilepsy-focused review (direct statement: L2HGDH is “an important mitochondrial enzyme … which oxidizes the L-2-hydroxyglutarate into α-ketoglutarate”) (shi2024disordersoforganic pages 6-7). A clinical genetics/imaging review excerpt further reports L-2-HGDH is present in mitochondria and membrane-associated by subcellular fractionation (erdal2025geneticneuroimagingand pages 4-5). In mouse disease modeling, L2hgdh deficiency caused robust L-2-HG accumulation particularly in brain and testis (ma2017l2hgdhdeficiencyaccumulates pages 1-2).

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Primary trigger: L2HGDH loss-of-function → L-2-HG accumulation
The initiating event in L2HGA is biallelic loss-of-function in L2HGDH, leading to reduced conversion of L-2-HG to 2-KG and systemic/brain accumulation of L-2-HG (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 1-3).

2.2 White-matter vulnerability and demyelination/leukoencephalopathy
Human neuroimaging is characterized by a stereotyped pattern dominated by subcortical white matter involvement with deep gray nuclei (basal ganglia/dentate nucleus) involvement (kranendijk2012progressinunderstanding pages 7-8, kranendijk2012progressinunderstanding pages 8-9). In an L2hgdh knockout mouse model, loss of L2hgdh produced “progressive leukoencephalopathy and neurodegeneration,” with findings consistent with demyelination and white matter pathology, including gliosis and microglial neuroinflammation (ma2017l2hgdhdeficiencyaccumulates pages 1-2). The corresponding figure-based evidence in that model includes T2 MRI changes, myelin staining (Luxol fast blue; FluoroMyelin), and reduced MBP readouts in affected white matter (ma2017l2hgdhdeficiencyaccumulates media 23a1cbfb).

2.3 Mitochondrial dysfunction and impaired respiratory capacity
Several lines of evidence link elevated L-2-HG to impaired mitochondrial bioenergetics:

• Review-level mechanistic claims collated in the mouse model paper note that 2-HG can impair oxidative phosphorylation components (“cytochrome c oxidase and ATP synthase”) and is considered a mitochondrial stressor relevant to white-matter pathology (ma2017l2hgdhdeficiencyaccumulates pages 1-2).
• In a 2024 human neuronal-cell model (SH-SY5Y neuroblastoma), exposure to 0.1 mM L-2-HG for 24 h produced a metabolic shift toward anaerobic glycolysis (e.g., increased lactate:glucose ratio) and reduced maximal respiration capacity (maximal specific respiration decreased to ~66–78% of control, while basal respiration was unchanged) (gondas2024bothenantiomersof pages 6-9, gondas2024bothenantiomersof pages 5-6). Quantitative media-metabolite changes included reduced glucose uptake (control −518 ± 141 to L-2HG −302 ± 22 nmol·h−1·mg−1), increased lactate release (135 ± 23 to 158 ± 9), and increased alanine (7 ± 2 to 13 ± 1), interpreted as less pyruvate entering the TCA cycle (gondas2024bothenantiomersof pages 5-6).

2.4 Oxidative stress and enzyme inhibition (energy metabolism/neuronal injury)
In vitro tissue exposure experiments summarized in the 2012 review report that L-2-HG inhibited creatine kinase and induced oxidative stress in rat cerebellum homogenates, offering a plausible mechanism for neuronal/white-matter injury (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 9-11). A clinical cohort review (2025) similarly frames L2HGA pathophysiology around CNS disruption and oxidative stress, consistent with the broader literature, though the excerpted details are limited (erdal2025geneticneuroimagingand pages 1-2).

2.5 Epigenetic dysregulation via inhibition of α-KG–dependent dioxygenases (emerging/expanded mechanism)
L-2-HG is an α-KG analog and can inhibit α-KG–dependent dioxygenases. In the L2hgdh-deficient mouse model, L-2-HG accumulation was associated with increased histone methylation, consistent with inhibition of JmjC histone demethylases and TET DNA hydroxylases (ma2017l2hgdhdeficiencyaccumulates pages 1-2). More recently, a 2024 glioma case/literature analysis explicitly states that L-2-HG “inhibits TET1 and TET2” and may be more potent than D-2-HG in some measures, supporting a mechanistic bridge between L-2-HG and methylome alteration (cordier2024malignantgliomain pages 7-9). Importantly, Cordier et al. also highlight that high intratumoral 2-HG production in IDH-mutant glioma differs from systemic “passive” accumulation in L2HGA, which could yield different epigenetic outcomes (cordier2024malignantgliomain pages 9-10).

3. Key molecular players

3.1 Genes/proteins (HGNC-level)

Causal gene
• L2HGDH (encodes mitochondrial FAD-dependent L-2-hydroxyglutarate dehydrogenase) (kranendijk2012progressinunderstanding pages 8-9, shi2024disordersoforganic pages 6-7).

Other implicated molecular axes (not necessarily causal)
• L-malate dehydrogenase (L-malDH): the only known human enzyme generating L-2-HG from 2-KG as an off-target reaction (kranendijk2012progressinunderstanding pages 1-3).
• α-KG–dependent dioxygenases (e.g., TET family; JmjC/KDM histone demethylases): mechanistic targets inhibited by 2-HG enantiomers, including L-2-HG (ma2017l2hgdhdeficiencyaccumulates pages 1-2, cordier2024malignantgliomain pages 7-9).
• Mitochondrial respiratory chain/ATP synthase components: implicated as functional targets of 2-HG in mechanistic discussion (ma2017l2hgdhdeficiencyaccumulates pages 1-2).

3.2 Chemical entities (CHEBI-level)
• L-2-hydroxyglutarate (L-2-HG): the main accumulated pathogenic metabolite (kranendijk2012progressinunderstanding pages 1-3).
• α-ketoglutarate / 2-ketoglutarate (2-KG): substrate/product node; precursor for off-pathway L-2-HG formation and target of L-2-HG oxidation back-reaction (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 1-3).
• FAD / riboflavin (vitamin B2 precursor): cofactor/precursor relevant to L-2-HGDH activity and a common supportive therapy; FAD is described as accelerating conversion of L-2-HG to α-ketoglutarate (bozaci2023glutaricaciduriaand pages 2-3, kranendijk2012progressinunderstanding pages 9-11).
• Levocarnitine: commonly used supportive therapy in reported cohorts (bozaci2023glutaricaciduriaand pages 1-2).

3.3 Cell types (CL-level)
Evidence from the L2hgdh mouse model indicates a glial/white-matter process with:
• Oligodendrocyte lineage involvement (expansion of oligodendrocyte progenitor cells, OPCs) (ma2017l2hgdhdeficiencyaccumulates pages 1-2).
• Microglia-mediated neuroinflammation and gliosis (ma2017l2hgdhdeficiencyaccumulates pages 1-2).
• Astrocytic proliferation around dentate nucleus has been reported in human histopathology summarized in an MRS review (sherry2015invivonmr pages 10-12).

3.4 Anatomical locations (UBERON-level)
Predominant CNS involvement, especially:
• Subcortical cerebral white matter (U-fibers/peripheral white matter) (kranendijk2012progressinunderstanding pages 7-8, alamri2024deepbrainstimulation pages 3-4).
• Basal ganglia structures (globus pallidus, putamen, caudate) and dentate nucleus (kranendijk2012progressinunderstanding pages 7-8, kranendijk2012progressinunderstanding pages 8-9).
• Cerebellum/dentate nucleus involvement is frequently linked to cerebellar ataxia (kranendijk2012progressinunderstanding pages 8-9).

4. Biological processes disrupted (GO-style candidates)
The evidence supports disruption of the following process categories:

Metabolite repair / organic acid metabolism
• “Disorder of metabolite repair” framing: L-2-HGDH clears off-pathway L-2-HG generated by L-malDH (kranendijk2012progressinunderstanding pages 7-8, kranendijk2012progressinunderstanding pages 1-3).

Mitochondrial energy metabolism / respiration
• Decreased maximal respiration capacity and bioenergetic reprogramming toward anaerobic glycolysis under L-2-HG exposure (gondas2024bothenantiomersof pages 6-9, gondas2024bothenantiomersof pages 5-6).

Oxidative stress response
• Induction of oxidative stress by L-2-HG exposure in experimental systems (kranendijk2012progressinunderstanding pages 9-11).

Myelination / white matter maintenance
• Progressive leukoencephalopathy/demyelination in mouse model and characteristic white-matter imaging phenotype in humans (ma2017l2hgdhdeficiencyaccumulates pages 1-2, kranendijk2012progressinunderstanding pages 8-9).

Epigenetic regulation of gene expression (DNA/histone modification)
• Increased histone methylation in L2hgdh deficiency and reported TET inhibition by L-2-HG in mechanistic discussion (ma2017l2hgdhdeficiencyaccumulates pages 1-2, cordier2024malignantgliomain pages 7-9).

Neuroinflammation / gliosis
• Gliosis and microglia-mediated neuroinflammation in the L2hgdh knockout model (ma2017l2hgdhdeficiencyaccumulates pages 1-2).

5. Cellular components (subcellular localization)
• Mitochondrion / mitochondrial membrane: L2HGDH is mitochondrial and membrane-associated (shi2024disordersoforganic pages 6-7, erdal2025geneticneuroimagingand pages 4-5).
• Nucleus/chromatin: downstream epigenetic effects are mediated by inhibition of nuclear α-KG–dependent dioxygenases (histone/DNA demethylation machinery), consistent with histone methylation changes observed in L2hgdh deficiency (ma2017l2hgdhdeficiencyaccumulates pages 1-2).

6. Disease progression: sequence of events (mechanistic narrative)

Stage 1 — Metabolite repair failure and metabolite accumulation
Biallelic L2HGDH loss reduces mitochondrial oxidation of L-2-HG to 2-KG, allowing L-2-HG (produced from 2-KG via non-specific L-malDH activity) to accumulate systemically and in brain/CSF (kranendijk2012progressinunderstanding pages 8-9, kranendijk2012progressinunderstanding pages 1-3).

Stage 2 — Cellular metabolic stress (mitochondrial + redox)
Elevated L-2-HG perturbs cellular metabolism, shifting glucose utilization toward anaerobic pathways and reducing maximal mitochondrial respiratory capacity in neuronal cell models; additional literature points to oxidative stress and inhibition of energy enzymes like creatine kinase (gondas2024bothenantiomersof pages 5-6, kranendijk2012progressinunderstanding pages 9-11).

Stage 3 — White-matter injury, gliosis, and neuroinflammation
Selective CNS vulnerability manifests as subcortical white-matter abnormalities with basal ganglia/dentate involvement on imaging; in mouse models, demyelination/leukoencephalopathy is accompanied by gliosis, microglial neuroinflammation, and altered oligodendrocyte lineage dynamics (OPC expansion) (kranendijk2012progressinunderstanding pages 8-9, ma2017l2hgdhdeficiencyaccumulates pages 1-2).

Stage 4 — Progressive neurological disability and potential tumor predisposition
Clinically, L2HGA typically follows a slowly progressive course with developmental delay, epilepsy, cerebellar dysfunction/ataxia, and movement disorders (kranendijk2012progressinunderstanding pages 7-8, bozaci2023glutaricaciduriaand pages 6-7). A subset of patients appear to have increased CNS tumor risk; mechanistic hypotheses implicate L-2-HG’s ability to inhibit epigenetic regulators (e.g., TET enzymes), but molecular tumor signatures may differ from IDH-mutant (D-2-HG) gliomas (cordier2024malignantgliomain pages 1-3, cordier2024malignantgliomain pages 9-10).

7. Phenotypic manifestations (HP-style associations) and mechanistic links

Core phenotypes and linkage to mechanisms
• Seizures/epilepsy: common in cohorts; interpreted in part as downstream of cortical/subcortical white-matter pathology and/or neurotransmitter system disruption; the 2024 epilepsy review links L-2-HG accumulation to GABAergic dysfunction and reports characteristic MRI/MRS changes in this disorder group (shi2024disordersoforganic pages 6-7, bozaci2023glutaricaciduriaand pages 6-7).
• Developmental delay / intellectual disability: prevalent in cohort data (e.g., 2012 review and 2023 cohort) and consistent with early white-matter maturation abnormalities and chronic metabolic/epigenetic perturbation (kranendijk2012progressinunderstanding pages 7-8, bozaci2023glutaricaciduriaand pages 3-4).
• Cerebellar ataxia and extrapyramidal features (dystonia/chorea): align with dentate nucleus and basal ganglia involvement on MRI (kranendijk2012progressinunderstanding pages 8-9, alamri2024deepbrainstimulation pages 3-4).

Recent cohort statistics (2023–2025) for phenotype frequency
In a 2023 multicenter Turkish cohort (n=10 L2HGA), clinical counts at diagnosis included seizures 3/10, developmental delay 2/10, movement disorders 2/10, behavioral problems 2/10; at last follow-up movement disorders 5/10, epilepsy 2/10, developmental delay 4/10, behavioral problems 4/10 (bozaci2023glutaricaciduriaand pages 6-7). The same report notes literature context that macrocephaly (75%) and epilepsy are common but nonspecific (bozaci2023glutaricaciduriaand pages 6-7).

8. Recent developments and latest research (prioritizing 2023–2024)

8.1 2024: Human neuronal-cell metabolic effects of L-2-HG
A 2024 Neurochemical Research study provides quantitative evidence that L-2-HG can directly reprogram neuronal-like cell metabolism and reduce maximal respiration capacity, supporting mitochondrial/energy-pathway involvement beyond purely descriptive clinical imaging (gondas2024bothenantiomersof pages 5-6).

8.2 2024: L2HGA and malignant glioma — molecular characterization and epigenetic analysis
Cordier et al. (2024) provide a detailed case plus literature review exploring whether systemic L-2-HG accumulation drives IDH-like epigenetic glioma signatures. They report that, despite mechanistic rationale (L-2-HG can inhibit TET1/2), the tumor lacked G-CIMP and clustered with IDH-wildtype glioma methylation patterns, alongside somatic alterations (TP53, NF1, BCOR) consistent with a second-hit model (cordier2024malignantgliomain pages 7-9, cordier2024malignantgliomain pages 3-6). This supports an expert interpretation that L-2-HG may contribute to tumor susceptibility but is not necessarily sufficient to impose the classic IDH-mutant methylation phenotype in all cases (cordier2024malignantgliomain pages 9-10).

8.3 2023: Natural history/real-world treatment monitoring in a multicenter cohort
Bozaci et al. (2023) report structured follow-up and real-world therapy use (riboflavin + levocarnitine in all 10 L2HGA cases) and state there was a “significant decrease in urinary 2-HGA with the treatment” (bozaci2023glutaricaciduriaand pages 1-2, bozaci2023glutaricaciduriaand pages 6-7). However, subgroup comparisons by genotype did not show significant differences in biochemical response in the excerpt, and symptom improvements were limited (“relative neurologic improvement” in 3 L2HGA patients) (bozaci2023glutaricaciduriaand pages 1-2, bozaci2023glutaricaciduriaand pages 2-3).

9. Current applications and real-world implementations

9.1 Supportive metabolic therapy (riboflavin/FAD-related; levocarnitine)
Multiple clinical sources describe riboflavin (vitamin B2; FAD precursor) and levocarnitine as commonly used therapies. The 2012 review reports anecdotal responses where FAD (or riboflavin) and levocarnitine lowered urinary L-2-HG and improved some clinical features, consistent with the enzyme’s FAD dependence (kranendijk2012progressinunderstanding pages 9-11). In the 2023 cohort, all L2HGA patients were treated with riboflavin plus levocarnitine, with significant urinary 2-HGA reduction reported and limited neurologic improvement (bozaci2023glutaricaciduriaand pages 1-2).

9.2 Neuromodulation for severe movement disorder (2024 GPi-DBS case report)
A 2024 peer-reviewed case report describes the first reported use of bilateral globus pallidus internus deep brain stimulation (GPi-DBS) for medically refractory dystonia in L2HGA. The family reported “approximately 50% improvement,” and the authors report “significant increases in mobility and decrease in dystonia” at serial follow-up; BFMDRS-M improved (e.g., 46/120 preop to 21.5/120 at 6 months) with subsequent fluctuations related to infection and programming (alamri2024deepbrainstimulation pages 2-3). This represents an emerging real-world intervention for advanced motor disability when pharmacotherapy is insufficient (alamri2024deepbrainstimulation pages 1-2).

9.3 Imaging and metabolite detection in practice
Proton MR spectroscopy (MRS) can show a metabolite-specific peak at ~2.50 ppm attributed to L-2-hydroxyglutaric acid, and decreased NAA with increased Cho/Cr ratio, linking biochemical accumulation to in vivo neurochemical signatures (sherry2015invivonmr pages 10-12). Such imaging is used as part of diagnostic workup alongside urine organic acids and genetic testing (alamri2024deepbrainstimulation pages 2-2).

10. Expert opinions and analysis (authoritative sources)

Metabolite-repair framing
The authoritative 2012 JIMD review classifies L2HGA as a “disorder of metabolite repair,” emphasizing that the pathophysiology arises from failure to clear an abnormal byproduct metabolite rather than blockade of a canonical pathway step (kranendijk2012progressinunderstanding pages 7-8).

Two-hit oncogenesis concept
Cordier et al. (2024) propose a “two-tiered oncogenesis” model: chronic L-2-HG elevation may prime tissue (first hit), but a secondary somatic mutation is required for tumor development (cordier2024malignantgliomain pages 9-10). This interpretation is grounded in their methylation/WES findings and comparison to IDH-mutant glioma biology (cordier2024malignantgliomain pages 3-6).

11. Evidence-linked statistics and data (recent)

Cohort size and phenotype counts (2023)
Bozaci et al. (2023) report 10 L2HGA patients (within a 35-patient cerebral organic aciduria cohort). At diagnosis: seizures 3/10, developmental delay 2/10, movement disorders 2/10, behavioral problems 2/10; at last visit: movement disorders 5/10, epilepsy 2/10, developmental delay 4/10, behavioral problems 4/10 (bozaci2023glutaricaciduriaand pages 6-7, bozaci2023glutaricaciduriaand pages 3-4). Treatment initiation age mean 53.36 ± 47.43 months (range 6–180) in their L2HGA subgroup (bozaci2023glutaricaciduriaand pages 6-7).

Quantitative cellular bioenergetics/metabolic data (2024)
In SH-SY5Y cells exposed to 0.1 mM L-2-HG, maximal respiration capacity decreased (control maximal respiration 73 ± 3 pmol·s−1 per 10^6 cells; maximal capacity decreased to ~66–78% of control under 2-HG enantiomers), and glucose uptake decreased while lactate and alanine release increased (gondas2024bothenantiomersof pages 5-6).

DBS outcomes (2024)
In the GPi-DBS L2HGA case, BFMDRS-M scores improved with stimulation (e.g., to 21.5/120 at 6 months; with longer-term values reported through 13 months) and the family reported ~50% improvement in function and dystonia severity (alamri2024deepbrainstimulation pages 2-3).

12. Clinical trials and research infrastructure
No interventional trials specific to isolated L2HGA were retrieved in this run. Two relevant ClinicalTrials.gov records were retrieved:

• NCT07125066 (start date 2025-07-30): single-patient, open-label Phase 1 study using ACER-001 (sodium phenylbutyrate; Olpruva) for combined D,L-2-hydroxyglutaric aciduria (C-2HGA), with endpoints including urine D,L-2-HG and seizure frequency (NCT07125066 chunk 1).
• NCT04880356 (start date 2021-03-01): observational longitudinal natural-history data collection study of ultra-rare inherited metabolic/degenerative neurological diseases, explicitly including L-2-hydroxyglutaric aciduria; endpoints include cognitive fluency, gait/stance metrics (SARA stance, TUG), upper limb function, and QoL (EQ-5D-5L) over a planned 10-year follow-up (NCT04880356 chunk 1).

13. Knowledge-base annotation suggestions (ontology-oriented)

Gene/protein
• L2HGDH (HGNC symbol; mitochondrial FAD-dependent L-2-hydroxyglutarate dehydrogenase) (kranendijk2012progressinunderstanding pages 8-9).

Proposed GO Biological Process terms (candidate mapping)
• “Organic acid metabolic process” / “2-hydroxyglutarate metabolic process” (supported by L-2-HG accumulation and enzymatic defect) (kranendijk2012progressinunderstanding pages 1-3).
• “Mitochondrial respiratory chain complex activity / oxidative phosphorylation” (supported by reduced maximal respiration capacity and OXPHOS impairment discussion) (gondas2024bothenantiomersof pages 5-6, ma2017l2hgdhdeficiencyaccumulates pages 1-2).
• “Response to oxidative stress” (supported by oxidative stress induction in experimental data summarized in review) (kranendijk2012progressinunderstanding pages 9-11).
• “Myelination” / “axon ensheathment” / “glial cell activation” (supported by leukoencephalopathy/demyelination, gliosis, microglial neuroinflammation) (ma2017l2hgdhdeficiencyaccumulates pages 1-2, ma2017l2hgdhdeficiencyaccumulates media 23a1cbfb).
• “Chromatin modification” / “DNA demethylation” / “histone demethylation” (supported by increased histone methylation and TET inhibition discussion) (ma2017l2hgdhdeficiencyaccumulates pages 1-2, cordier2024malignantgliomain pages 7-9).

Proposed GO Cellular Component terms (candidate mapping)
• Mitochondrion; mitochondrial inner membrane (enzyme localization; respiratory coupling concept) (erdal2025geneticneuroimagingand pages 4-5).
• Nucleus/chromatin (downstream epigenetic targets of 2-HG) (ma2017l2hgdhdeficiencyaccumulates pages 1-2).

Cell types (CL)
• Oligodendrocyte progenitor cell (OPC) (mouse model shows OPC expansion) (ma2017l2hgdhdeficiencyaccumulates pages 1-2).
• Microglia (microglia-mediated neuroinflammation) (ma2017l2hgdhdeficiencyaccumulates pages 1-2).
• Astrocyte (gliosis; astrocytic proliferation around dentate nucleus in human pathology summary) (sherry2015invivonmr pages 10-12).

Anatomy (UBERON)
• Subcortical cerebral white matter/U-fibers; basal ganglia; dentate nucleus; cerebellum (imaging/pathology distribution) (alamri2024deepbrainstimulation pages 3-4, kranendijk2012progressinunderstanding pages 8-9).

Chemicals (CHEBI)
• L-2-hydroxyglutarate; α-ketoglutarate/2-oxoglutarate; FAD; riboflavin; levocarnitine (kranendijk2012progressinunderstanding pages 1-3, bozaci2023glutaricaciduriaand pages 2-3).

14. Evidence items (PMID-focused) — limitations
The retrieved excerpts in this run did not include PubMed IDs (PMIDs) in the tool outputs; therefore, this report provides DOI URLs and journal metadata but cannot reliably attach PMIDs without external lookup. Mechanistic claims and statistics are cited to retrieved sources (pqac IDs) with URLs and publication dates where available.

15. Key references (with URLs and dates from retrieved sources)

• Ma S et al. “L2hgdh Deficiency Accumulates L-2-Hydroxyglutarate with Progressive Leukoencephalopathy and Neurodegeneration.” Molecular and Cellular Biology. Apr 2017. https://doi.org/10.1128/mcb.00492-16 (ma2017l2hgdhdeficiencyaccumulates pages 1-2)
• Kranendijk M et al. “Progress in understanding 2-hydroxyglutaric acidurias.” Journal of Inherited Metabolic Disease. Mar 2012. https://doi.org/10.1007/s10545-012-9462-5 (kranendijk2012progressinunderstanding pages 8-9)
• Bozaci AE et al. “Glutaric aciduria and L-2-hydroxyglutaric aciduria: Clinical and molecular findings of 35 patients from Turkey.” Molecular Genetics and Metabolism Reports. Sep 2023. https://doi.org/10.1016/j.ymgmr.2023.100979 (bozaci2023glutaricaciduriaand pages 3-4)
• Gondáš E et al. “Both Enantiomers of 2-Hydroxyglutarate Modulate the Metabolism of Cultured Human Neuroblastoma Cells.” Neurochemical Research. Jun 2024. https://doi.org/10.1007/s11064-024-04188-8 (gondas2024bothenantiomersof pages 5-6)
• Cordier F et al. “Malignant glioma in L-2-Hydroxy Glutaric Aciduria: thorough molecular characterization of a case and literature review.” Free Neuropathology. May 2024. https://doi.org/10.17879/freeneuropathology-2024-5377 (cordier2024malignantgliomain pages 1-3)
• Alamri A et al. “Deep Brain Stimulation of the Globus Pallidus Internus in a Child with Refractory Dystonia due to L2-Hydroxyglutaric Aciduria.” Stereotactic and Functional Neurosurgery. May 2024. https://doi.org/10.1159/000538418 (alamri2024deepbrainstimulation pages 2-3)
• ClinicalTrials.gov NCT04880356. “Longitudinal Study of Ultra-rare Inherited Metabolic and Degenerative Neurological Diseases.” Start: 2021-03-01. https://clinicaltrials.gov/study/NCT04880356 (retrieved text) (NCT04880356 chunk 1)

Figure evidence used
• White-matter pathology/demyelination summary figure from Ma et al. 2017 (Figure 3) (ma2017l2hgdhdeficiencyaccumulates media 23a1cbfb).

End of report.

References

1. (kranendijk2012progressinunderstanding pages 7-8): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

2. (ma2017l2hgdhdeficiencyaccumulates pages 1-2): Shenghong Ma, Renqiang Sun, Bowen Jiang, Jun Gao, Wanglong Deng, Peng Liu, Ruoyu He, Jing Cui, Minbiao Ji, Wei Yi, Pengyuan Yang, Xiaohui Wu, Yue Xiong, Zilong Qiu, Dan Ye, and Kun-Liang Guan. <i>l2hgdh</i> deficiency accumulates <scp>l</scp>-2-hydroxyglutarate with progressive leukoencephalopathy and neurodegeneration. Molecular and Cellular Biology, Apr 2017. URL: https://doi.org/10.1128/mcb.00492-16, doi:10.1128/mcb.00492-16. This article has 44 citations and is from a domain leading peer-reviewed journal.

3. (kranendijk2012progressinunderstanding pages 1-3): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

4. (kranendijk2012progressinunderstanding pages 8-9): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

5. (kranendijk2012progressinunderstanding pages 9-11): Martijn Kranendijk, Eduard A. Struys, Gajja S. Salomons, Marjo S. Van der Knaap, and Cornelis Jakobs. Progress in understanding 2-hydroxyglutaric acidurias. Journal of Inherited Metabolic Disease, 35:571-587, Mar 2012. URL: https://doi.org/10.1007/s10545-012-9462-5, doi:10.1007/s10545-012-9462-5. This article has 332 citations and is from a peer-reviewed journal.

6. (shi2024disordersoforganic pages 6-7): Yuqing Shi, Zihan Wei, Yan Feng, Ya-Jing Gan, Guo-Yan Li, and Yanchun Deng. Disorders of organic acid metabolism and epilepsy. Acta Epileptologica, Aug 2024. URL: https://doi.org/10.1186/s42494-024-00167-2, doi:10.1186/s42494-024-00167-2. This article has 2 citations.

7. (erdal2025geneticneuroimagingand pages 4-5): Ayşenur Engin Erdal, Sümeyra Zeynep Özbey, Gülten Burcu Civelek Ürey, Aynur Küçükçongar Yavaş, Berrak Bilginer Gürbüz, Mehmet Gündüz, Esra Kiliç, Avni Merter Keçeli, Aydan Değerliyurt, and Çiğdem Seher Kasapkara. Genetic, neuroimaging, and clinical characteristics of a cohort of individuals with l-2-hydroxyglutaric aciduria from türkiye. Journal of pediatric endocrinology & metabolism : JPEM, Jul 2025. URL: https://doi.org/10.1515/jpem-2025-0021, doi:10.1515/jpem-2025-0021. This article has 0 citations.

8. (ma2017l2hgdhdeficiencyaccumulates media 23a1cbfb): Shenghong Ma, Renqiang Sun, Bowen Jiang, Jun Gao, Wanglong Deng, Peng Liu, Ruoyu He, Jing Cui, Minbiao Ji, Wei Yi, Pengyuan Yang, Xiaohui Wu, Yue Xiong, Zilong Qiu, Dan Ye, and Kun-Liang Guan. <i>l2hgdh</i> deficiency accumulates <scp>l</scp>-2-hydroxyglutarate with progressive leukoencephalopathy and neurodegeneration. Molecular and Cellular Biology, Apr 2017. URL: https://doi.org/10.1128/mcb.00492-16, doi:10.1128/mcb.00492-16. This article has 44 citations and is from a domain leading peer-reviewed journal.

9. (gondas2024bothenantiomersof pages 6-9): Eduard Gondáš, Eva Baranovičová, Peter Bystrický, Jakub Šofranko, Andrea Evinová, Matúš Dohál, Zuzana Hatoková, and Radovan Murín. Both enantiomers of 2-hydroxyglutarate modulate the metabolism of cultured human neuroblastoma cells. Neurochemical Research, 49:2480-2490, Jun 2024. URL: https://doi.org/10.1007/s11064-024-04188-8, doi:10.1007/s11064-024-04188-8. This article has 3 citations and is from a peer-reviewed journal.

10. (gondas2024bothenantiomersof pages 5-6): Eduard Gondáš, Eva Baranovičová, Peter Bystrický, Jakub Šofranko, Andrea Evinová, Matúš Dohál, Zuzana Hatoková, and Radovan Murín. Both enantiomers of 2-hydroxyglutarate modulate the metabolism of cultured human neuroblastoma cells. Neurochemical Research, 49:2480-2490, Jun 2024. URL: https://doi.org/10.1007/s11064-024-04188-8, doi:10.1007/s11064-024-04188-8. This article has 3 citations and is from a peer-reviewed journal.

11. (erdal2025geneticneuroimagingand pages 1-2): Ayşenur Engin Erdal, Sümeyra Zeynep Özbey, Gülten Burcu Civelek Ürey, Aynur Küçükçongar Yavaş, Berrak Bilginer Gürbüz, Mehmet Gündüz, Esra Kiliç, Avni Merter Keçeli, Aydan Değerliyurt, and Çiğdem Seher Kasapkara. Genetic, neuroimaging, and clinical characteristics of a cohort of individuals with l-2-hydroxyglutaric aciduria from türkiye. Journal of pediatric endocrinology & metabolism : JPEM, Jul 2025. URL: https://doi.org/10.1515/jpem-2025-0021, doi:10.1515/jpem-2025-0021. This article has 0 citations.

12. (cordier2024malignantgliomain pages 7-9): Fleur Cordier, Pieter Wesseling, Bastiaan B.J. Tops, Lennart Kester, Pim J. French, Martin Van Den Bent, Felix Hinz, Eleonora Aronica, K. Mariam Slot, Floor Abbink, Marjo S. Van Der Knaap, and Mariette Kranendonk. Malignant glioma in l-2-hydroxy glutaric aciduria: thorough molecular characterization of a case and literature review. Free Neuropathology, May 2024. URL: https://doi.org/10.17879/freeneuropathology-2024-5377, doi:10.17879/freeneuropathology-2024-5377. This article has 2 citations and is from a peer-reviewed journal.

13. (cordier2024malignantgliomain pages 9-10): Fleur Cordier, Pieter Wesseling, Bastiaan B.J. Tops, Lennart Kester, Pim J. French, Martin Van Den Bent, Felix Hinz, Eleonora Aronica, K. Mariam Slot, Floor Abbink, Marjo S. Van Der Knaap, and Mariette Kranendonk. Malignant glioma in l-2-hydroxy glutaric aciduria: thorough molecular characterization of a case and literature review. Free Neuropathology, May 2024. URL: https://doi.org/10.17879/freeneuropathology-2024-5377, doi:10.17879/freeneuropathology-2024-5377. This article has 2 citations and is from a peer-reviewed journal.

14. (bozaci2023glutaricaciduriaand pages 2-3): Ayse Ergül Bozaci, Esra Er, Aysel Tekmenuray Ünal, İbrahim Taş, Ercan Ayaz, Mehmet Nuri Ozbek, Asude Durmaz, Ayçe Aykut, and Melis Kose. Glutaric aciduria and l-2-hydroxyglutaric aciduria: clinical and molecular findings of 35 patients from turkey. Molecular Genetics and Metabolism Reports, 36:100979, Sep 2023. URL: https://doi.org/10.1016/j.ymgmr.2023.100979, doi:10.1016/j.ymgmr.2023.100979. This article has 13 citations.

15. (bozaci2023glutaricaciduriaand pages 1-2): Ayse Ergül Bozaci, Esra Er, Aysel Tekmenuray Ünal, İbrahim Taş, Ercan Ayaz, Mehmet Nuri Ozbek, Asude Durmaz, Ayçe Aykut, and Melis Kose. Glutaric aciduria and l-2-hydroxyglutaric aciduria: clinical and molecular findings of 35 patients from turkey. Molecular Genetics and Metabolism Reports, 36:100979, Sep 2023. URL: https://doi.org/10.1016/j.ymgmr.2023.100979, doi:10.1016/j.ymgmr.2023.100979. This article has 13 citations.

16. (sherry2015invivonmr pages 10-12): Erica B. Sherry, Phil Lee, and I. Choi. In vivo nmr studies of the brain with hereditary or acquired metabolic disorders. Neurochemical Research, 40:2647-2685, Nov 2015. URL: https://doi.org/10.1007/s11064-015-1772-1, doi:10.1007/s11064-015-1772-1. This article has 23 citations and is from a peer-reviewed journal.

17. (alamri2024deepbrainstimulation pages 3-4): Abdullah Alamri, Sara Breitbart, Nebras Warsi, Eriberto Rayco, George Ibrahim, Alfonso Fasano, and Carolina Gorodetsky. Deep brain stimulation of the globus pallidus internus in a child with refractory dystonia due to l2-hydroxyglutaric aciduria. Stereotactic and Functional Neurosurgery, 102:209-216, May 2024. URL: https://doi.org/10.1159/000538418, doi:10.1159/000538418. This article has 1 citations and is from a peer-reviewed journal.

18. (bozaci2023glutaricaciduriaand pages 6-7): Ayse Ergül Bozaci, Esra Er, Aysel Tekmenuray Ünal, İbrahim Taş, Ercan Ayaz, Mehmet Nuri Ozbek, Asude Durmaz, Ayçe Aykut, and Melis Kose. Glutaric aciduria and l-2-hydroxyglutaric aciduria: clinical and molecular findings of 35 patients from turkey. Molecular Genetics and Metabolism Reports, 36:100979, Sep 2023. URL: https://doi.org/10.1016/j.ymgmr.2023.100979, doi:10.1016/j.ymgmr.2023.100979. This article has 13 citations.

19. (cordier2024malignantgliomain pages 1-3): Fleur Cordier, Pieter Wesseling, Bastiaan B.J. Tops, Lennart Kester, Pim J. French, Martin Van Den Bent, Felix Hinz, Eleonora Aronica, K. Mariam Slot, Floor Abbink, Marjo S. Van Der Knaap, and Mariette Kranendonk. Malignant glioma in l-2-hydroxy glutaric aciduria: thorough molecular characterization of a case and literature review. Free Neuropathology, May 2024. URL: https://doi.org/10.17879/freeneuropathology-2024-5377, doi:10.17879/freeneuropathology-2024-5377. This article has 2 citations and is from a peer-reviewed journal.

20. (bozaci2023glutaricaciduriaand pages 3-4): Ayse Ergül Bozaci, Esra Er, Aysel Tekmenuray Ünal, İbrahim Taş, Ercan Ayaz, Mehmet Nuri Ozbek, Asude Durmaz, Ayçe Aykut, and Melis Kose. Glutaric aciduria and l-2-hydroxyglutaric aciduria: clinical and molecular findings of 35 patients from turkey. Molecular Genetics and Metabolism Reports, 36:100979, Sep 2023. URL: https://doi.org/10.1016/j.ymgmr.2023.100979, doi:10.1016/j.ymgmr.2023.100979. This article has 13 citations.

21. (cordier2024malignantgliomain pages 3-6): Fleur Cordier, Pieter Wesseling, Bastiaan B.J. Tops, Lennart Kester, Pim J. French, Martin Van Den Bent, Felix Hinz, Eleonora Aronica, K. Mariam Slot, Floor Abbink, Marjo S. Van Der Knaap, and Mariette Kranendonk. Malignant glioma in l-2-hydroxy glutaric aciduria: thorough molecular characterization of a case and literature review. Free Neuropathology, May 2024. URL: https://doi.org/10.17879/freeneuropathology-2024-5377, doi:10.17879/freeneuropathology-2024-5377. This article has 2 citations and is from a peer-reviewed journal.

22. (alamri2024deepbrainstimulation pages 2-3): Abdullah Alamri, Sara Breitbart, Nebras Warsi, Eriberto Rayco, George Ibrahim, Alfonso Fasano, and Carolina Gorodetsky. Deep brain stimulation of the globus pallidus internus in a child with refractory dystonia due to l2-hydroxyglutaric aciduria. Stereotactic and Functional Neurosurgery, 102:209-216, May 2024. URL: https://doi.org/10.1159/000538418, doi:10.1159/000538418. This article has 1 citations and is from a peer-reviewed journal.

23. (alamri2024deepbrainstimulation pages 1-2): Abdullah Alamri, Sara Breitbart, Nebras Warsi, Eriberto Rayco, George Ibrahim, Alfonso Fasano, and Carolina Gorodetsky. Deep brain stimulation of the globus pallidus internus in a child with refractory dystonia due to l2-hydroxyglutaric aciduria. Stereotactic and Functional Neurosurgery, 102:209-216, May 2024. URL: https://doi.org/10.1159/000538418, doi:10.1159/000538418. This article has 1 citations and is from a peer-reviewed journal.

24. (alamri2024deepbrainstimulation pages 2-2): Abdullah Alamri, Sara Breitbart, Nebras Warsi, Eriberto Rayco, George Ibrahim, Alfonso Fasano, and Carolina Gorodetsky. Deep brain stimulation of the globus pallidus internus in a child with refractory dystonia due to l2-hydroxyglutaric aciduria. Stereotactic and Functional Neurosurgery, 102:209-216, May 2024. URL: https://doi.org/10.1159/000538418, doi:10.1159/000538418. This article has 1 citations and is from a peer-reviewed journal.

25. (NCT07125066 chunk 1): Jerry Vockley, MD, PhD. An Individual Patient, Open Label Study to Use ACER-001 to Treat Combined D,L-2 Hydroxyglutaric Aciduria (C-2HGA). Jerry Vockley, MD, PhD. 2025. ClinicalTrials.gov Identifier: NCT07125066

26. (NCT04880356 chunk 1):  Longitudinal Study of Ultra-rare Inherited Metabolic and Degenerative Neurological Diseases.. Fondazione I.R.C.C.S. Istituto Neurologico Carlo Besta. 2021. ClinicalTrials.gov Identifier: NCT04880356
