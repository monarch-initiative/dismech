---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-15T21:42:19.941157'
end_time: '2026-02-15T21:57:01.162714'
duration_seconds: 881.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alpha Thalassemia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Alpha Thalassemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Alpha Thalassemia**.
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
- **Disease Name:** Alpha Thalassemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Alpha Thalassemia**.
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


# Alpha thalassemia (Mendelian) — Pathophysiology Research Report (molecular/cellular mechanisms)

## 0. Disease definition and key concepts (current understanding)
Alpha thalassemia is a quantitative hemoglobinopathy caused by reduced production of α-globin chains due to pathogenic variants affecting the α-globin gene cluster, most commonly deletions involving **HBA1/HBA2** on chromosome 16. Severity follows **α-globin gene dosage**: silent carrier (1 allele affected), α-thalassemia trait (2), **HbH disease** (3), and **Hb Bart’s hydrops fetalis / α-thalassemia major** (4). (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, zahed2023effectiveutilizationof pages 64-67)

A central mechanistic concept is **globin-chain imbalance**: α-globin deficiency leaves excess non-α chains that self-associate into homotetramers—**HbH (β4)** postnatally and **Hb Bart’s (γ4)** in fetal life—both of which are poor oxygen carriers and/or unstable, driving downstream RBC injury. (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, zahed2023effectiveutilizationof pages 64-67)

## 1. Core pathophysiology
### 1.1 Primary mechanism: α-globin deficiency → globin imbalance
Loss or dysfunction of HBA1/HBA2 reduces α-globin synthesis; clinical severity is determined by the number of affected α-globin genes. (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, sadiq2024thalassemiapathophysiologydiagnosis pages 6-7)

In HbH disease (three α genes affected), excess β chains form **β4 tetramers (HbH)**; HbH is described as unstable, prone to oxidative damage and precipitation in erythroid cells, shortening RBC lifespan and increasing hemolysis. (zahed2023effectiveutilizationof pages 64-67)

In fetal Hb Bart’s disease (four α genes affected), fetuses produce only **Hb Bart’s (γ4)**; Hb Bart’s has high oxygen affinity and is associated with widespread fetal tissue hypoxia and severe anemia, leading to hydrops fetalis and multi-organ injury. (chaemsaithong2023placentaderivedextracellularvesicles pages 1-2, luewan2024fetalhemodynamicchanges pages 4-6)

### 1.2 Oxidative stress and red-cell damage as convergent pathobiology
A unifying downstream mechanism in thalassemia is oxidative stress from precipitated/excess globin and iron, which drives both hemolysis and ineffective erythropoiesis. (kuo2023pyruvatekinaseactivators pages 1-2)

In an authoritative hematology education review, oxidative stress is described as a “major factor” that drives hemolysis and ineffective erythropoiesis in thalassemia, and the oxidative burden can reduce pyruvate kinase activity and ATP availability, worsening red cell integrity and survival. (kuo2023pyruvatekinaseactivators pages 1-2)

### 1.3 Ineffective erythropoiesis (IE) and erythroid maturation defects
In alpha thalassemia, globin imbalance injures erythroid precursors, contributing to ineffective erythropoiesis and intramedullary destruction/hemolysis, manifesting as microcytic hypochromic anemia. (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, sadiq2024thalassemiapathophysiologydiagnosis pages 6-7)

Patient-derived erythroid progenitors from **HbH/Constant Spring (HbH/CS)** demonstrate cellular correlates of IE: a trend toward increased proliferation, reduced viability, and delayed terminal differentiation, consistent with maturation inefficiency under α/β imbalance. (wongkhammul2024erythropoiesisandgene pages 2-4, wongkhammul2024erythropoiesisandgene pages 1-2)

### 1.4 Fetal Hb Bart’s disease: compensation vs cellular injury (hypoxia/mitochondrial dysfunction)
A 2024 prospective study of 18 Hb Bart’s fetuses vs 13 controls (~19 weeks gestation) showed severe fetal anemia (Hb **6.4±1.3** vs **11.2±1.2 g/dL**, p<0.001) with hemodynamic compensation (increased cardiac dimensions and combined cardiac output) but evidence of **mitochondrial structural and functional injury** in heart/brain (mitochondrial swelling/unfolded cristae; increased membrane potential changes; increased ROS particularly in brain). (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)

A complementary 2023 prospective cordocentesis study (20 affected vs 30 controls) found increased fetal serum iron and **non-transferrin-bound iron (NTBI/LPI)** in Hb Bart’s fetuses (NTBI median **0.11 vs 0.07**, p=0.046), and NTBI correlated with worse myocardial performance indices, linking anemia/iron dysregulation to fetal cardiac dysfunction in the pre-hydropic stage. (jatavan2023comparisonsofserum pages 1-2, jatavan2023comparisonsofserum pages 4-5)

## 2. Key molecular players (knowledge-base oriented)
### 2.1 Causal genes and regulatory loci (HGNC-style)
- **HBA1 / HBA2 (α-globin genes)**: Reduced expression or loss causes α-thalassemia; severity scales with the number of affected alleles. (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, sadiq2024thalassemiapathophysiologydiagnosis pages 6-7)
- **α-globin gene cluster enhancers (e.g., MCS-R2/HS-40)**: The cluster is regulated by distal enhancers; **MCS-R2 (HS-40)** is described as the most effective enhancer for α-globin synthesis, and deletions removing critical regulatory elements (including HS-40) can silence intact α-globin genes. (isaiah2024prevalenceofthalassemia pages 3-4, traegersynodinos2024impactofαglobin pages 4-5)
- Common deletion mechanisms: α+ deletions of ~3.7 kb or 4.2 kb from unequal crossover between HBA1/HBA2; α0 deletions removing both α genes also occur and are geographically patterned. (traegersynodinos2024impactofαglobin pages 4-5)

### 2.2 Non-deletional variants: Hb Constant Spring (HbCS)
Hb Constant Spring is caused by **HBA2:c.427T>C**, which replaces the termination codon and produces an elongated α-globin chain (+31 aa) that can form abnormal precipitates and alter RBC membrane proteins; compound heterozygosity with α0-thalassemia can produce more severe **HbH/CS** disease. (wongkhammul2024erythropoiesisandgene pages 1-2)

### 2.3 Modifier pathways and emerging mechanistic layers (2024)
**Epitranscriptomic (m6A) modifiers in HbH disease:** A 2024 PLOS ONE study implicated **METTL16** (m6A writer) and readers including **YTHDF3** and **IGF2BP3** in HbH phenotypic heterogeneity, reporting METTL16 downregulation (FC **0.44**, P<0.001) and correlations with IGF2BP3 (R=0.81, P=0.004) and YTHDF3 (R=0.74, P=0.01). IGF2BP3 expression was negatively correlated with hemoglobin in patients (P<0.001). Functional perturbation in K562 cells linked METTL16 to ROS and intracellular iron changes and altered hemin-induced hemoglobin synthesis. (liao2024mettl16participatesin pages 7-8, liao2024mettl16participatesin pages 1-2)

**Proteostasis/chaperone response:** HbH/CS erythroid progenitors showed elevated expression of molecular chaperones (HSP and CCT gene families), consistent with proteotoxic stress from unstable globin products. (wongkhammul2024erythropoiesisandgene pages 1-2)

## 3. Dysregulated pathways and cellular processes
Key dysregulated processes include:
- **Hemoglobin assembly and oxygen transport** disrupted by abnormal tetramers (HbH, Hb Bart’s). (zahed2023effectiveutilizationof pages 64-67, chaemsaithong2023placentaderivedextracellularvesicles pages 1-2)
- **Oxidative stress / ROS homeostasis** driven by unstable hemoglobin species and iron dysregulation; linked to membrane damage and erythroid cell death. (kuo2023pyruvatekinaseactivators pages 1-2, jatavan2023comparisonsofserum pages 4-5)
- **Erythroid differentiation and maturation** delays/arrest and reduced erythroblast viability (ineffective erythropoiesis). (wongkhammul2024erythropoiesisandgene pages 2-4, sadiq2024thalassemiapathophysiologydiagnosis pages 4-6)
- **Iron handling abnormalities** in severe fetal disease (increased NTBI/LPI) and downstream tissue injury risk. (jatavan2023comparisonsofserum pages 1-2, jatavan2023comparisonsofserum pages 4-5)
- **Mitochondrial dysfunction** in fetal target organs under hypoxic anemia (mitochondrial swelling/cristae changes; increased ΔΨm changes and ROS). (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)

## 4. Biological Processes (GO-style) disrupted (suggested annotations)
(Selected GO-like terms; intended for knowledge-base mapping)
- **Hemoglobin biosynthetic process / hemoglobin metabolic process** (α-globin deficiency; abnormal HbH/Hb Bart’s production). (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, zahed2023effectiveutilizationof pages 64-67)
- **Erythrocyte differentiation / erythrocyte maturation / erythropoiesis** (delayed terminal differentiation; ineffective erythropoiesis). (wongkhammul2024erythropoiesisandgene pages 2-4, sadiq2024thalassemiapathophysiologydiagnosis pages 4-6)
- **Response to oxidative stress / regulation of reactive oxygen species metabolic process** (globin precipitation + iron; fetal tissue ROS increases). (kuo2023pyruvatekinaseactivators pages 1-2, luewan2024fetalhemodynamicchanges pages 4-6)
- **Response to hypoxia** (Hb Bart’s fetal hypoxic anemia driving compensatory hemodynamics and organ injury). (luewan2024fetalhemodynamicchanges pages 4-6, chaemsaithong2023placentaderivedextracellularvesicles pages 1-2)
- **Iron ion homeostasis / iron ion transport** (elevated NTBI/LPI in fetal Hb Bart’s). (jatavan2023comparisonsofserum pages 1-2, jatavan2023comparisonsofserum pages 4-5)
- **Mitochondrial membrane potential / mitochondrial inner membrane organization** (ΔΨm changes; cristae abnormalities in fetal heart/brain). (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)

## 5. Cellular Components (GO-CC style) implicated
- **Hemoglobin complex** (HbH and Hb Bart’s tetramers; altered composition). (zahed2023effectiveutilizationof pages 64-67, sadiq2024thalassemiapathophysiologydiagnosis pages 4-6)
- **Erythrocyte cytosol** (site of hemoglobin accumulation/precipitation). (zahed2023effectiveutilizationof pages 64-67)
- **Erythrocyte membrane** (damage from precipitates/oxidative stress; HbCS can alter membrane proteins). (wongkhammul2024erythropoiesisandgene pages 1-2, zahed2023effectiveutilizationof pages 64-67)
- **Mitochondrion / mitochondrial inner membrane / cristae** (fetal heart/brain mitochondrial swelling/cristae changes; ΔΨm/ROS). (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)
- **Blood microparticle / extracellular vesicle** (placenta-derived EVs proposed for liquid biopsy in Hb Bart’s). (chaemsaithong2023placentaderivedextracellularvesicles pages 1-2)

## 6. Disease progression model (sequence of events)
### 6.1 Genotype to biochemical phenotype
1) **Genetic lesion** (deletions, regulatory deletions, or non-deletional variants) reduces α-globin expression (HBA1/HBA2; enhancer dysfunction such as HS-40/MCS-R2). (isaiah2024prevalenceofthalassemia pages 3-4, traegersynodinos2024impactofαglobin pages 4-5)
2) **Globin-chain imbalance** produces HbH (β4) postnatally and/or Hb Bart’s (γ4) prenatally (depending on developmental stage and gene dosage). (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, zahed2023effectiveutilizationof pages 64-67)

### 6.2 Cellular injury and hematologic consequences
3) **Unstable hemoglobin species / precipitates** → oxidative injury to erythroid precursors and mature RBCs → **ineffective erythropoiesis + hemolysis** → anemia and compensatory erythropoiesis. (zahed2023effectiveutilizationof pages 64-67, sadiq2024thalassemiapathophysiologydiagnosis pages 4-6)
4) In HbH/CS: erythroid progenitors show delayed differentiation and reduced viability; gene expression reflects reduced HBA1/HBA2 and low α/β ratios. (wongkhammul2024erythropoiesisandgene pages 2-4)

### 6.3 Severe fetal stage (Hb Bart’s)
5) **Severe fetal anemia** drives cardiomegaly and increased cardiac output (compensatory) but leaves residual **mitochondrial dysfunction/ROS injury** in heart and brain, suggesting “cellular damage secondary to anemic hypoxia” despite compensation. (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)
6) Elevated fetal NTBI/LPI may contribute additional oxidative stress and correlates with fetal cardiac dysfunction. (jatavan2023comparisonsofserum pages 1-2, jatavan2023comparisonsofserum pages 4-5)

## 7. Phenotypic manifestations (HP-style anchors)
(Representative phenotype groupings; exact HP IDs not enumerated in provided sources)
- **Microcytic hypochromic anemia** in trait and HbH/CS cohorts (low Hb, low MCV/MCH) (wongkhammul2024erythropoiesisandgene pages 2-4, sadiq2024thalassemiapathophysiologydiagnosis pages 4-6)
- **Chronic hemolytic anemia** in HbH disease, often with splenomegaly and hemolysis features (zahed2023effectiveutilizationof pages 64-67)
- **Hydrops fetalis / fetal cardiomegaly / fetal cardiac dysfunction** in Hb Bart’s disease (chaemsaithong2023placentaderivedextracellularvesicles pages 1-2, luewan2024fetalhemodynamicchanges pages 4-6)
- **Neurologic and cardiac cellular injury risk in utero** suggested by fetal brain and myocardial mitochondrial dysfunction and ROS increases (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)

## 8. Cell types (CL-style) and anatomical sites (UBERON-style)
### Primary affected cell types
- **Erythroid progenitor cells / erythroblasts**: differentiation delay/arrest, reduced viability in HbH/CS models. (wongkhammul2024erythropoiesisandgene pages 2-4)
- **Mature erythrocytes / reticulocytes**: hemolysis and inclusion bodies in HbH; epitranscriptomic profiling performed in patient reticulocytes/nucleated erythroid cells. (zahed2023effectiveutilizationof pages 64-67, liao2024mettl16participatesin pages 7-8)
- **Placental cells producing extracellular vesicles (trophoblast lineage)**: placenta-derived EVs detectable in maternal blood and proposed for Hb Bart’s liquid biopsy. (chaemsaithong2023placentaderivedextracellularvesicles pages 1-2)
- **Fetal cardiomyocytes and neurons/brain cells**: mitochondrial dysfunction and ROS increase under fetal anemia. (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)

### Key anatomical locations
- **Bone marrow** (ineffective erythropoiesis), **spleen** (hemolysis-related pathology), and **placenta/fetal heart/fetal brain** in Hb Bart’s disease. (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6, luewan2024fetalhemodynamicchanges pages 4-6, chaemsaithong2023placentaderivedextracellularvesicles pages 1-2)

## 9. Chemical entities / interventions (CHEBI-style anchors) and current applications
### Diagnostics and real-world screening (2023–2024)
**NGS in reproductive/population screening:**
- Southwest China Han cohort (Frontiers in Genetics, Apr 2024): 1,093 individuals screened; carrier detection rate **11.89%**, with α-thalassemia carriers **7.68% (84/1,093)**; NGS found an additional **0.91% (10/1,093)** rare variants not detected by traditional PCR methods. (du2024screeningforthalassemia pages 1-2)
- Changsha County prenatal cohort (Frontiers in Genetics, Nov 2024): 38,810 pregnant women; **5.69%** carriers detected by NGS; 1,594 α-thalassemia carriers with 23 genotypes identified. (xia2024aparticularfocus pages 1-2)

**Third-generation sequencing (TGS) for hard-to-resolve variants:** A Thai pilot study (Obstetric Medicine, Oct 2024) applied TGS to 19 cases; conventional testing left 47.7% undiagnosed, and TGS provided additional diagnoses in **36.8% (7/19)**. (traisrisilp2024thalassemiascreeningby pages 1-2)

### Prenatal identification of Hb Bart’s hydrops fetalis (real-world implementation)
A 2023 review of placenta-derived EVs and Hb Bart’s disease reports: “**Sonographic markers can accurately predict fetal Hb Bart’s disease as early as the late first trimester (12–15 weeks of gestation), with a detection rate of 90–95 percent**,” and serial ultrasound surveillance can achieve “**a sensitivity of 100 percent**…with a **false positive rate of 10.9 percent**” while reducing invasive procedures “**by 70 percent**.” (chaemsaithong2023placentaderivedextracellularvesicles pages 4-5)

### Disease-modifying pharmacology (emerging; includes α-thalassemia)
**Pyruvate kinase activation (mitapivat):** A 2023 American Society of Hematology Education Program review describes oxidative stress as central in thalassemia and positions PK activation as a metabolic therapy. In a phase 2 open-label NTDT study including α-thalassemia (HbH), the primary endpoint (≥1 g/dL Hb increase) was met in **80% (16/20)** overall, and **all 5 α-thalassemia (HbH) patients** met the endpoint. Ongoing phase 3 trials include **ENERGIZE (NCT04770753)** and **ENERGIZE-T (NCT04770779)** in α- or β-thalassemia. (kuo2023pyruvatekinaseactivators pages 3-4, kuo2023pyruvatekinaseactivators pages 4-6)

## 10. Expert synthesis and interpretation (authoritative perspectives)
Recent authoritative reviews emphasize that thalassemia phenotypes arise from a core biochemical lesion (globin imbalance) that triggers oxidative stress, hemolysis, and ineffective erythropoiesis, while newer work adds layers of heterogeneity from modifiers (e.g., RNA methylation machinery). (kuo2023pyruvatekinaseactivators pages 1-2, liao2024mettl16participatesin pages 7-8)

Fetal Hb Bart’s disease demonstrates a clinically important dissociation: measurable hemodynamic compensation can coexist with cellular organ injury (mitochondrial dysfunction and ROS), suggesting that “compensation” does not equal “no damage,” and providing a mechanistic rationale for early detection strategies and (future) in utero interventions. (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)

## 11. Evidence items (PMID note)
The provided full-text evidence extracts include DOIs and journal metadata but do not include PMIDs in the excerpts available to this tool run. Key evidence items with publication dates and URLs include:
- Chaemsaithong et al., *Int J Mol Sci* (Mar 2023): https://doi.org/10.3390/ijms24065658 (chaemsaithong2023placentaderivedextracellularvesicles pages 1-2, chaemsaithong2023placentaderivedextracellularvesicles pages 4-5)
- Jatavan et al., *Frontiers in Medicine* (Jan 2023): https://doi.org/10.3389/fmed.2022.1015306 (jatavan2023comparisonsofserum pages 1-2, jatavan2023comparisonsofserum pages 4-5)
- Kuo, *ASH Education Program* (Dec 2023): https://doi.org/10.1182/hematology.2023000468 (kuo2023pyruvatekinaseactivators pages 3-4, kuo2023pyruvatekinaseactivators pages 4-6)
- Luewan et al., *BMC Pregnancy and Childbirth* (Feb 2024): https://doi.org/10.1186/s12884-023-06232-x (luewan2024fetalhemodynamicchanges pages 4-6, luewan2024fetalhemodynamicchanges pages 1-2)
- Du et al., *Frontiers in Genetics* (Apr 2024): https://doi.org/10.3389/fgene.2024.1356068 (du2024screeningforthalassemia pages 1-2)
- Traeger-Synodinos et al., *Int J Mol Sci* (Mar 2024): https://doi.org/10.3390/ijms25063400 (traegersynodinos2024impactofαglobin pages 4-5)
- Liao et al., *PLOS ONE* (Aug 2024): https://doi.org/10.1371/journal.pone.0306043 (liao2024mettl16participatesin pages 7-8)
- Wongkhammul et al., *Int J Mol Sci* (Oct 2024): https://doi.org/10.3390/ijms252011246 (wongkhammul2024erythropoiesisandgene pages 2-4)
- Xia et al., *Frontiers in Genetics* (Nov 2024): https://doi.org/10.3389/fgene.2024.1422462 (xia2024aparticularfocus pages 1-2)
- Traisrisilp et al., *Obstetric Medicine* (Oct 2024): https://doi.org/10.1177/1753495x231207676 (traisrisilp2024thalassemiascreeningby pages 1-2)

## 12. Key gaps and limitations of this report
- PMIDs were not available in the extracted evidence snippets, so DOI-linked citation is provided. (luewan2024fetalhemodynamicchanges pages 4-6, kuo2023pyruvatekinaseactivators pages 3-4)
- Some advanced therapeutic areas for α-thalassemia (e.g., α-globin enhancer editing for α-thal itself, in utero gene therapy) were identified in searches but not obtainable as full-text evidence in this run; thus mechanistic detail is focused on available 2023–2024 evidence. (li2024hotspotsandstatus pages 13-14)


References

1. (sadiq2024thalassemiapathophysiologydiagnosis pages 4-6): Idris Zubairu Sadiq, Fatima Sadiq Abubakar, Hauwa Salisu Usman, Aliyu Dantani Abdullahi, Bashiru Ibrahim, Babangida Sanusi Kastayal, Maryam Ibrahim, and Hassan Aliyu Hassan. Thalassemia: pathophysiology, diagnosis, and advances in treatment. Thalassemia Reports, 14:81-102, Oct 2024. URL: https://doi.org/10.3390/thalassrep14040010, doi:10.3390/thalassrep14040010. This article has 48 citations.

2. (zahed2023effectiveutilizationof pages 64-67): R Zahed. Effective utilization of molecular genetic screening of patients with sickle cell disease and beta thalassemia major in saudi arabia. Unknown journal, 2023.

3. (sadiq2024thalassemiapathophysiologydiagnosis pages 6-7): Idris Zubairu Sadiq, Fatima Sadiq Abubakar, Hauwa Salisu Usman, Aliyu Dantani Abdullahi, Bashiru Ibrahim, Babangida Sanusi Kastayal, Maryam Ibrahim, and Hassan Aliyu Hassan. Thalassemia: pathophysiology, diagnosis, and advances in treatment. Thalassemia Reports, 14:81-102, Oct 2024. URL: https://doi.org/10.3390/thalassrep14040010, doi:10.3390/thalassrep14040010. This article has 48 citations.

4. (chaemsaithong2023placentaderivedextracellularvesicles pages 1-2): Piya Chaemsaithong, Suchaya Luewan, Mana Taweevisit, Wararat Chiangjong, Pisut Pongchaikul, Paul Scott Thorner, Theera Tongsong, and Somchai Chutipongtanate. Placenta-derived extracellular vesicles in pregnancy complications and prospects on a liquid biopsy for hemoglobin bart’s disease. International Journal of Molecular Sciences, 24:5658, Mar 2023. URL: https://doi.org/10.3390/ijms24065658, doi:10.3390/ijms24065658. This article has 18 citations.

5. (luewan2024fetalhemodynamicchanges pages 4-6): Suchaya Luewan, Nattayaporn Apaijai, Nipon Chattipakorn, Siriporn C. Chattipakorn, and Theera Tongsong. Fetal hemodynamic changes and mitochondrial dysfunction in myocardium and brain tissues in response to anemia: a lesson from hemoglobin bart’s disease. BMC Pregnancy and Childbirth, Feb 2024. URL: https://doi.org/10.1186/s12884-023-06232-x, doi:10.1186/s12884-023-06232-x. This article has 2 citations and is from a peer-reviewed journal.

6. (kuo2023pyruvatekinaseactivators pages 1-2): Kevin H. M. Kuo. Pyruvate kinase activators: targeting red cell metabolism in thalassemia. Hematology. American Society of Hematology. Education Program, 2023 1:114-120, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000468, doi:10.1182/hematology.2023000468. This article has 7 citations.

7. (wongkhammul2024erythropoiesisandgene pages 2-4): Narawich Wongkhammul, Pinyaphat Khamphikham, Siripong Tongjai, Adisak Tantiworawit, Kanda Fanhchaksai, Somsakul Pop Wongpalee, Alisa Tubsuwan, Supawadee Maneekesorn, and Pimlak Charoenkwan. Erythropoiesis and gene expression analysis in erythroid progenitor cells derived from patients with hemoglobin h/constant spring disease. International Journal of Molecular Sciences, 25:11246, Oct 2024. URL: https://doi.org/10.3390/ijms252011246, doi:10.3390/ijms252011246. This article has 1 citations.

8. (wongkhammul2024erythropoiesisandgene pages 1-2): Narawich Wongkhammul, Pinyaphat Khamphikham, Siripong Tongjai, Adisak Tantiworawit, Kanda Fanhchaksai, Somsakul Pop Wongpalee, Alisa Tubsuwan, Supawadee Maneekesorn, and Pimlak Charoenkwan. Erythropoiesis and gene expression analysis in erythroid progenitor cells derived from patients with hemoglobin h/constant spring disease. International Journal of Molecular Sciences, 25:11246, Oct 2024. URL: https://doi.org/10.3390/ijms252011246, doi:10.3390/ijms252011246. This article has 1 citations.

9. (luewan2024fetalhemodynamicchanges pages 1-2): Suchaya Luewan, Nattayaporn Apaijai, Nipon Chattipakorn, Siriporn C. Chattipakorn, and Theera Tongsong. Fetal hemodynamic changes and mitochondrial dysfunction in myocardium and brain tissues in response to anemia: a lesson from hemoglobin bart’s disease. BMC Pregnancy and Childbirth, Feb 2024. URL: https://doi.org/10.1186/s12884-023-06232-x, doi:10.1186/s12884-023-06232-x. This article has 2 citations and is from a peer-reviewed journal.

10. (jatavan2023comparisonsofserum pages 1-2): Phudit Jatavan, Rattanaporn Sekararithi, Thidarat Jaiwongkam, Sirinart Kumfu, Nipon Chattipakorn, and Theera Tongsong. Comparisons of serum non-transferrin-bound iron levels and fetal cardiac function between fetuses affected with hemoglobin bart’s disease and normal fetuses. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2022.1015306, doi:10.3389/fmed.2022.1015306. This article has 1 citations.

11. (jatavan2023comparisonsofserum pages 4-5): Phudit Jatavan, Rattanaporn Sekararithi, Thidarat Jaiwongkam, Sirinart Kumfu, Nipon Chattipakorn, and Theera Tongsong. Comparisons of serum non-transferrin-bound iron levels and fetal cardiac function between fetuses affected with hemoglobin bart’s disease and normal fetuses. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2022.1015306, doi:10.3389/fmed.2022.1015306. This article has 1 citations.

12. (isaiah2024prevalenceofthalassemia pages 3-4): Audu Isaiah, Ibrahim Kalle Kwaifa, Yakubu Abdulrahman, and Obadiah Audu Sunday. Prevalence of thalassemia in nigeria: pathophysiology and clinical manifestations. Clinical Medicine And Health Research Journal, 4:806-815, Mar 2024. URL: https://doi.org/10.18535/cmhrj.v4i2.325, doi:10.18535/cmhrj.v4i2.325. This article has 3 citations.

13. (traegersynodinos2024impactofαglobin pages 4-5): Joanne Traeger-Synodinos, Christina Vrettou, Christalena Sofocleous, Matteo Zurlo, Alessia Finotti, and Roberto Gambari. Impact of α-globin gene expression and α-globin modifiers on the phenotype of β-thalassemia and other hemoglobinopathies: implications for patient management. International Journal of Molecular Sciences, 25(6):3400, Mar 2024. URL: https://doi.org/10.3390/ijms25063400, doi:10.3390/ijms25063400. This article has 14 citations.

14. (liao2024mettl16participatesin pages 7-8): Yuping Liao, Feng Zhang, Fang Yang, Shijin Huang, Sha Su, Xuemei Tan, Linlin Zhong, Lingjie Deng, and Lihong Pang. Mettl16 participates in haemoglobin h disease through m6a modification. PLOS ONE, 19:e0306043, Aug 2024. URL: https://doi.org/10.1371/journal.pone.0306043, doi:10.1371/journal.pone.0306043. This article has 3 citations and is from a peer-reviewed journal.

15. (liao2024mettl16participatesin pages 1-2): Yuping Liao, Feng Zhang, Fang Yang, Shijin Huang, Sha Su, Xuemei Tan, Linlin Zhong, Lingjie Deng, and Lihong Pang. Mettl16 participates in haemoglobin h disease through m6a modification. PLOS ONE, 19:e0306043, Aug 2024. URL: https://doi.org/10.1371/journal.pone.0306043, doi:10.1371/journal.pone.0306043. This article has 3 citations and is from a peer-reviewed journal.

16. (du2024screeningforthalassemia pages 1-2): Yepei Du, Cong Zhou, Jing Wang, Yanting Yang, and Hui Liu. Screening for thalassemia carriers among the han population of childbearing age in southwestern of china. Frontiers in Genetics, Apr 2024. URL: https://doi.org/10.3389/fgene.2024.1356068, doi:10.3389/fgene.2024.1356068. This article has 5 citations and is from a peer-reviewed journal.

17. (xia2024aparticularfocus pages 1-2): Yu Xia, Cailian Huang, Mudan Yang, Meng Zhang, and Yang Lu. A particular focus on the prevalence of α-thalassemia and β-thalassemia among pregnant women in changsha county, hunan province. Frontiers in Genetics, Nov 2024. URL: https://doi.org/10.3389/fgene.2024.1422462, doi:10.3389/fgene.2024.1422462. This article has 0 citations and is from a peer-reviewed journal.

18. (traisrisilp2024thalassemiascreeningby pages 1-2): Kuntharee Traisrisilp, Yu Zheng, Kwong Wai Choy, and Pimlak Chareonkwan. Thalassemia screening by third-generation sequencing: pilot study in a thai population. Obstetric Medicine, 17:101-107, Oct 2024. URL: https://doi.org/10.1177/1753495x231207676, doi:10.1177/1753495x231207676. This article has 1 citations and is from a peer-reviewed journal.

19. (chaemsaithong2023placentaderivedextracellularvesicles pages 4-5): Piya Chaemsaithong, Suchaya Luewan, Mana Taweevisit, Wararat Chiangjong, Pisut Pongchaikul, Paul Scott Thorner, Theera Tongsong, and Somchai Chutipongtanate. Placenta-derived extracellular vesicles in pregnancy complications and prospects on a liquid biopsy for hemoglobin bart’s disease. International Journal of Molecular Sciences, 24:5658, Mar 2023. URL: https://doi.org/10.3390/ijms24065658, doi:10.3390/ijms24065658. This article has 18 citations.

20. (kuo2023pyruvatekinaseactivators pages 3-4): Kevin H. M. Kuo. Pyruvate kinase activators: targeting red cell metabolism in thalassemia. Hematology. American Society of Hematology. Education Program, 2023 1:114-120, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000468, doi:10.1182/hematology.2023000468. This article has 7 citations.

21. (kuo2023pyruvatekinaseactivators pages 4-6): Kevin H. M. Kuo. Pyruvate kinase activators: targeting red cell metabolism in thalassemia. Hematology. American Society of Hematology. Education Program, 2023 1:114-120, Dec 2023. URL: https://doi.org/10.1182/hematology.2023000468, doi:10.1182/hematology.2023000468. This article has 7 citations.

22. (li2024hotspotsandstatus pages 13-14): Qiuying Li, Xinyan Li, Sheng He, and Jiao Li. Hotspots and status of fetal alpha-thalassemia from 2009 to 2023: a bibliometric analysis. Frontiers in Pediatrics, Dec 2024. URL: https://doi.org/10.3389/fped.2024.1467760, doi:10.3389/fped.2024.1467760. This article has 1 citations.