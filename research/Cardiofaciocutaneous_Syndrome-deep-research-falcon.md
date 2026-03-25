---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-04T22:32:52.502130'
end_time: '2026-02-04T22:39:57.804118'
duration_seconds: 425.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cardiofaciocutaneous Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Cardiofaciocutaneous Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cardiofaciocutaneous Syndrome**.
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
- **Disease Name:** Cardiofaciocutaneous Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Cardiofaciocutaneous Syndrome**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Cardiofaciocutaneous Syndrome (CFC)
- MONDO ID: MONDO_0015280 (CFC); related subtypes include MONDO_0007265 (CFC1), MONDO_0014112 (CFC2), MONDO_0014113 (CFC3)
- Category: Mendelian (RASopathy)

Pathophysiology description
Cardiofaciocutaneous syndrome is a multisystem RASopathy caused by germline gain‑of‑function variants that hyperactivate the RAS–RAF–MEK–ERK (MAPK) cascade, impairing developmental programs that govern proliferation, differentiation, migration, survival and metabolism across ectodermal, cardiac, and neural tissues (e.g., skin/hair, myocardium, brain). At the molecular level, missense variants in pathway components—most often BRAF, and less frequently MAP2K1 (MEK1), MAP2K2 (MEK2), and rarely KRAS; de novo 14‑3‑3 (YWHAZ) variants have also been reported—drive ERK1/2 hyperactivation and downstream transcriptional reprogramming, establishing a cell‐state bias that produces the characteristic craniofacial, cutaneous, cardiac, and neurodevelopmental phenotype (reviewed Nov 22, 2023; DOI:10.3390/genes14122111) (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2, scorrano2023thecardiofaciocutaneoussyndrome pages 2-3, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5). Dysregulation manifests prenatally as lymphatic dysfunction (e.g., polyhydramnios, hydrops), fetal overgrowth parameters (macrocephaly/macrosomia), and structural anomalies (cardiac and renal), reflecting perturbed signaling in lymphatic endothelial, cardiac progenitor/myocyte, and neuroepithelial lineages (AJMG A, Oct 2023; DOI:10.1002/ajmg.a.63020) (jelin2023obstetricalandneonatal pages 2-2, jelin2023obstetricalandneonatal pages 1-1). 

Although oncogenic BRAF/MAPK activation is common in cancer, historically CFC was thought to have minimal malignancy risk; however, an updated pooled analysis suggests an elevated early‑childhood cancer incidence, warranting nuanced surveillance across RASopathies (medRxiv preprint, Aug 2025; DOI:10.1101/2024.08.09.24311751) (bess2025aliteraturereview pages 9-13). Preclinical and early translational observations indicate MEK inhibition can normalize hyperactive ERK signaling in relevant models, and limited clinical experience across RASopathies (notably Noonan syndrome) supports off‑label MEK inhibitor use for life‑threatening lymphatic and cardiac complications; targeted trials are needed for CFC (Genes 2023; DOI:10.3390/genes14122111) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).

Core Pathophysiology
- Primary mechanisms: germline gain‑of‑function or pathway‑activating missense variants in RAS/MAPK components that elevate ERK1/2 activity and perturb developmental gene expression programs in multiple tissues (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 1-2).
- Dysregulated pathways: canonical RAS–RAF–MEK–ERK signaling; positive regulation of ERK1/2 cascade predominates, overwhelming feedback control (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
- Affected cellular processes: proliferation, differentiation (neuronal, cardiomyocyte, keratinocyte), migration, survival; lymphangiogenesis and endothelial function are implicated by prenatal/neonatal lymphatic findings (AJMG A 2023) (jelin2023obstetricalandneonatal pages 2-2, jelin2023obstetricalandneonatal pages 1-1, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).

Key Molecular Players
- Genes/Proteins (HGNC): BRAF (dominant cause, ~75% of molecularly confirmed CFC), MAP2K1 (MEK1) and MAP2K2 (MEK2) (each up to ~25% collectively across cohorts), rare KRAS, with recent reports of YWHAZ de novo variants that enhance RAF‑stimulated ERK phosphorylation; all converge on ERK1/2 hyperactivation (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 2-3, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
  - Quote: “Currently, BRAF, MAP2K1, MAP2K2 and, rarely, KRAS have been associated with CFC… variants are mainly missense with a gain‑of‑function mechanism… leading to ERK1‑2 hyperactivation.” (Genes 2023; published Nov 22, 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
  - Quote: “YWHAZ… S230W variant that ‘enhanced Raf‑stimulated Erk phosphorylation’ consistent with gain‑of‑function.” (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).
- Chemical Entities (CHEBI): MEK inhibitors—trametinib and selumetinib—are the principal targeted agents explored off‑label across RASopathies (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).
- Cell Types (CL): cardiomyocytes (HCM), neural progenitors/neurons (ID, epilepsy), keratinocytes and dermal fibroblasts (skin/hair phenotypes), lymphatic endothelial cells (chylothorax/lymphatic dysplasia) (Genes 2023; AJMG A 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, jelin2023obstetricalandneonatal pages 2-2).
- Anatomical Locations (UBERON): heart (pulmonary valve, ventricular myocardium), skin, brain, lymphatic vasculature (Genes 2023; AJMG A 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, jelin2023obstetricalandneonatal pages 2-2).

Biological Processes (for GO annotation)
- MAPK cascade (GO:0000165); positive regulation of ERK1/2 cascade (GO:0070374); cell proliferation (GO:0008283); neuron differentiation (GO:0030182); cardiac muscle cell development (GO:0055013); keratinocyte differentiation (GO:0030216); lymphangiogenesis (GO:0001946). These processes map directly to observed neurodevelopmental, cardiac, skin, and lymphatic phenotypes (Genes 2023; AJMG A 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, jelin2023obstetricalandneonatal pages 2-2).

Cellular Components
- Plasma membrane (RAS activation), cytosol (RAF–MEK–ERK relay), and nucleus (ERK‑dependent transcriptional programs) are critical compartments of dysregulated signaling in CFC (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).

Disease Progression
- Initiation: de novo germline activating variant in BRAF/MEK1/MEK2/KRAS (or YWHAZ) establishes constitutive or exaggerated ERK signaling.
- Prenatal phase: lymphatic dysfunction and growth pattern anomalies detectable by ultrasound—polyhydramnios, (sometimes) nonimmune hydrops, macrocephaly/macrosomia, and structural cardiac/renal anomalies; increased operative delivery and neonatal complications are reported (AJMG A; published Oct 2023; DOI:10.1002/ajmg.a.63020) (jelin2023obstetricalandneonatal pages 2-2, jelin2023obstetricalandneonatal pages 1-1).
- Neonatal/infancy: hypotonia and feeding difficulties; congenital heart disease (pulmonary valve stenosis, septal defects, and/or HCM) commonly present; progressive skin/hair features emerge (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 1-2).
- Childhood: neurodevelopmental disability (moderate ID common), epilepsy with gene‑specific frequencies; brain MRI often shows ventriculomegaly and other anomalies; dermatologic features (ichthyosis, xerosis, nevi; hair abnormalities) are typical; variable growth abnormalities (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 1-2).
- Adolescent/adult: persistent multisystem morbidity; evolving data suggest non‑zero malignancy risk that may be enriched in early childhood (medRxiv 2025) (bess2025aliteraturereview pages 9-13).

Phenotypic Manifestations (HPO)
- Cardiac: pulmonary valve stenosis (HP:0001642) and hypertrophic cardiomyopathy (HP:0001639) are frequent; atrial/ventricular septal defects occur (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
- Neurologic: intellectual disability (HP:0001249) with high prevalence; seizures (HP:0001250) show gene‑specific frequencies and severity; hypotonia (neonatal onset common); ventriculomegaly on imaging (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
- Dermatologic: ichthyosis/xerosis (HP:0008064), sparse/curly/friable hair (HP:0008070), numerous nevi; expert cohorts describe a characteristic but heterogeneous dermatologic pattern (Genes 2023; BJD 2019) (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).
- Growth/prenatal: macrocephaly (HP:0000256), macrosomia (when present), polyhydramnios (HP:0001561); neonatal complications are more common than background (AJMG A 2023) (jelin2023obstetricalandneonatal pages 1-1, jelin2023obstetricalandneonatal pages 2-2).

Genotype–Phenotype Correlations (recent synthesis)
- Gene‑level trends: BRAF is most frequent and associates with high rates of cardiac disease and epilepsy/ID; MAP2K1 associates with higher seizure frequency and greater motor impairment; MAP2K2 tends to have lower seizure risk and milder neurocognitive impact compared with MAP2K1; KRAS is rare with cardiac prominence; YWHAZ de novo variants enhance ERK signaling (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 2-3, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).
  - Quote: seizure frequencies “57%… with BRAF…, 61%… with MAP2K1… and 30%… with MAP2K2,” and MAP2K1 p.Y130C/H/N and BRAF kinase-domain variants correlate with severe epilepsy (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
- Prenatal genotype distribution: in a 43‑case survey cohort, pathogenic variants were BRAF 81%, MEK1 14%, MEK2 5% (AJMG A 2023) (jelin2023obstetricalandneonatal pages 1-1).

Immune involvement and cancer risk
- Immune dysregulation: emerging multi‑center cohort data (n=56) describe recurrent but heterogeneous immunologic abnormalities in CFC—lymphopenia, hypogammaglobulinemia (IgG, IgA, IgM reductions), and increased infection susceptibility—with genotype links (BRAF with T‑cell lymphopenia; MAP2K1 with monocytosis and B‑cell abnormalities) (Frontiers in Immunology, Jul 2025; DOI:10.3389/fimmu.2025.1598896) (majo2025cardiofaciocutaneoussyndromeand pages 11-11).
- Cancer risk: pooled literature review (n≈690) estimates cumulative cancer incidence by age 10 of 3% (95% CI 1.1–5.5), with elevated standardized incidence ratios (all sites SIR≈4.96; ALL SIR≈24.23); the authors caution about limitations and potential biases and call for refined surveillance studies (medRxiv, Aug 2025; DOI:10.1101/2024.08.09.24311751) (bess2025aliteraturereview pages 9-13).

Current applications and real‑world implementations
- Prenatal diagnostics: prenatal phenotype definition (polyhydramnios, macrocephaly/macrosomia, structural anomalies) supports the increasing use of prenatal exome/NGS for suspected RASopathies; counseling includes elevated rates of operative delivery and neonatal complications (AJMG A 2023; DOI:10.1002/ajmg.a.63020) (jelin2023obstetricalandneonatal pages 2-2, jelin2023obstetricalandneonatal pages 1-1).
- Targeted pathway therapy (off‑label MEK inhibition): preclinical models (zebrafish; human lymphatic endothelial cells) demonstrate rescue of RASopathy phenotypes with MEK inhibitors, and case experiences across RASopathies (notably Noonan syndrome) report improvement in life‑threatening lymphatic disease and hypertrophic cardiomyopathy; disease‑specific trials for CFC are lacking (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10). 
  - Representative clinical example in RASopathies: trametinib led to resolution of refractory chylothorax and ventricular hypertrophy in a newborn with Noonan syndrome at 18‑month follow‑up (Children, Oct 2024; DOI:10.3390/children11111342) (). While not CFC, it exemplifies pathway‑directed therapy in germline RAS/MAPK hyperactivation and informs potential CFC indications.

Expert opinions and analysis
- Contemporary expert review emphasizes RAS/MAPK hyperactivation as the unifying mechanism in RASopathies, with MEK inhibitors as promising repurposed agents for severe, progressive complications; however, standardized protocols and trials specific to each disorder (including CFC) remain unmet needs (Genes 2023; published Nov 22, 2023; DOI:10.3390/genes14122111) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10). 
  - Quote: “There is no specific treatment for CFC syndrome. Encouraging zebrafish model system studies suggested that, in the future, MEK inhibitors could be a suitable treatment of progressive phenotypes of CFC in children.” (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2).
- Surveillance: updated pediatric cancer predisposition perspectives for RASopathies support nuanced, syndrome‑specific surveillance, acknowledging improved outcomes with targeted agents in low‑grade and benign neoplasms and the need for multidisciplinary care; recommendations continue to evolve as risk estimates are refined (context summarized within Genes 2023 and bolstered by pooled risk analysis) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10, bess2025aliteraturereview pages 9-13).

Relevant statistics and data (recent)
- Genotype distribution in a 43‑case cohort: BRAF 81%, MEK1 14%, MEK2 5%; median GA 37 weeks; median birthweight 3501 g; cesarean 48% (AJMG A, Oct 2023; DOI:10.1002/ajmg.a.63020; URL: https://doi.org/10.1002/ajmg.a.63020) (jelin2023obstetricalandneonatal pages 1-1).
- Prenatal complications: hyperemesis 12%, gestational diabetes 9%, gestational hypertension 7%, preeclampsia 7%; ultrasound abnormalities (polyhydramnios, macrocephaly, macrosomia, renal/cardiac) commonly observed (AJMG A 2023; published Oct 2023) (jelin2023obstetricalandneonatal pages 1-1).
- Cardiac and neurologic frequencies (synthesis): cardiac disease ~75% (PVS ~45%, HCM ~40%); seizure prevalence by gene: BRAF ~57%, MAP2K1 ~61%, MAP2K2 ~30%; ventriculomegaly on MRI ~44% (Genes 2023; open‑access review, Nov 2023; DOI:10.3390/genes14122111) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
- Cancer risk: cumulative incidence by age 10 ≈3% (95% CI 1.1–5.5), with SIR ≈4.96 for all cancers and ≈24.23 for ALL (medRxiv, Aug 2025; DOI:10.1101/2024.08.09.24311751; URL: https://doi.org/10.1101/2024.08.09.24311751) (bess2025aliteraturereview pages 9-13).

Embedded ontology‑aligned summary
| Category | Item (name) | Identifier (ontology ID/code) | Role/Relevance | Notes |
|---|---|---:|---|---|
| Genes/Proteins | BRAF | HGNC:BRAF | RAF-family serine/threonine kinase; primary causal gene | Major CFC gene (~75% cases); somatic oncogenic roles noted (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10, jelin2023obstetricalandneonatal pages 2-2) |
| Genes/Proteins | MAP2K1 (MEK1) | HGNC:MAP2K1 | Dual-specificity kinase activating ERK1/2 | Causally implicated in CFC; variants alter ERK signaling and seizure risk (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Genes/Proteins | MAP2K2 (MEK2) | HGNC:MAP2K2 | Partner MEK kinase activating ERK1/2 | CFC-linked; distinct genotype–phenotype trends vs MAP2K1 (koslaUnknownyearmap2k2(mek2)in pages 1-4) |
| Genes/Proteins | KRAS | HGNC:KRAS | Small GTPase upstream of RAF | Rare causal gene in CFC; associated with cardiac/coarse facies (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Genes/Proteins | NRAS | HGNC:NRAS | RAS-family GTPase | Reported in RASopathies/CFC spectrum (koslaUnknownyearmap2k2(mek2)in pages 1-4) |
| Genes/Proteins | YWHAZ | HGNC:YWHAZ | 14-3-3 adaptor modulating RAF/ERK signaling | Recently reported de novo variants perturb RAS/MAPK (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Primary pathway | RAS/MAPK cascade | GO:0000165 (MAPK cascade) | Central dysregulated signaling cascade in CFC | Pathogenic variants cause ERK1/2 hyperactivation driving multisystem disease (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Dysregulated process | Positive regulation of ERK1/2 cascade | GO:0070374 | Upstream→ERK overactivation | Mechanistic core of CFC pathophysiology (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Dysregulated process | Cell proliferation | GO:0008283 | Altered growth control in multiple tissues | Explains organ overgrowth/oncogenic potential (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10, bess2025aliteraturereview pages 9-13) |
| Dysregulated process | Neuron differentiation | GO:0030182 | Neurodevelopmental disruption | Underlies ID, seizures and brain MRI anomalies (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Dysregulated process | Cardiac muscle cell development | GO:0055013 | Cardiogenesis and cardiomyopathy mechanisms | Links to PVS, HCM and septal defects in CFC (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Dysregulated process | Keratinocyte differentiation | GO:0030216 | Skin/ectodermal phenotypes | Explains ichthyosis, abnormal hair/skin findings (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 1-2) |
| Dysregulated process | Lymphangiogenesis | GO:0001946 | Lymphatic development/abnormalities | Relates to chylothorax/lymphatic phenotypes described (jelin2023obstetricalandneonatal pages 2-2, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Cellular component | Plasma membrane | GO:0005886 | Location of receptor/RAS activation | RAS activation at membrane initiates cascade (koslaUnknownyearmap2k2(mek2)in pages 1-4) |
| Cellular component | Cytosol | GO:0005829 | Cytoplasmic signaling/transduction | MEK/ERK signaling transduces in cytosol before nuclear entry (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Cellular component | Nucleus | GO:0005634 | ERK-dependent transcriptional effects | Downstream transcriptional programs affecting development (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Cell type | Cardiomyocyte | CL:0000746 | Primary cardiac muscle cell affected in HCM | Hypertrophy and dysfunction described in CFC/RASopathies (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Cell type | Neural progenitor cell | CL:0000047 | Neurodevelopmental cell population | Implicated in ID, cortical malformations and seizures (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Cell type | Keratinocyte | CL:0000312 | Epidermal cell type | Skin phenotypes (hyperkeratosis, nevi) in CFC (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2) |
| Cell type | Lymphatic endothelial cell | CL:0002138 | Lymphatic vessel lining cells | Involved in chylothorax/lymphatic dysplasia responses (jelin2023obstetricalandneonatal pages 2-2) |
| Cell type | Fibroblast | CL:0000057 | Connective tissue cell; model cell type | Patient fibroblasts used in functional studies (koslaUnknownyearmap2k2(mek2)in pages 10-10) |
| Anatomical location | Heart | UBERON:0000948 | Major organ with congenital and progressive disease | PVS, HCM, ASD/VSD frequent in CFC (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Anatomical location | Skin | UBERON:0002097 | Ectodermal organ with characteristic findings | Hair anomalies, pigmented nevi, ichthyosis reported (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2) |
| Anatomical location | Brain | UBERON:0000955 | CNS site of neurodevelopmental impact | Ventriculomegaly, cortical anomalies, epilepsy (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Anatomical location | Lymphatic vessel | UBERON:0004535 | Lymphatic system involvement site | Neonatal chylothorax/lymphatic disease reports (jelin2023obstetricalandneonatal pages 2-2) |
| Phenotype | Hypertrophic cardiomyopathy | HPO:HP:0001639 | Key cardiac morbidity in CFC | Reported in ~40% of cases; therapeutic target for MEK inhibitors (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Phenotype | Pulmonary valve stenosis | HPO:HP:0001642 | Common congenital cardiac lesion | Frequent in CFC cohorts (~45%) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Phenotype | Seizures | HPO:HP:0001250 | Neurological morbidity with gene-specific rates | High prevalence; gene-specific frequencies reported (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Phenotype | Intellectual disability | HPO:HP:0001249 | Core neurodevelopmental outcome | Varies by gene (BRAF/MAP2K1 > MAP2K2) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5) |
| Phenotype | Ichthyosis | HPO:HP:0008064 | Dermatologic manifestation | Documented in mutation-positive cohorts (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2) |
| Phenotype | Sparse hair | HPO:HP:0008070 | Ectodermal/signature finding | Part of craniofacial/skin phenotype (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2) |
| Phenotype | Macrocephaly | HPO:HP:0000256 | Prenatal/postnatal growth feature | Reported prenatally and postnatally in cohorts (jelin2023obstetricalandneonatal pages 2-2) |
| Phenotype | Polyhydramnios (prenatal) | HPO:HP:0001561 | Obstetrical ultrasound finding | Observed in CFC pregnancies (jelin2023obstetricalandneonatal pages 2-2) |
| Chemical entities | Trametinib | CHEBI:85083 | MEK1/2 inhibitor; repurposed/off-label in RASopathies | Case reports/series show benefit for cardiac/lymphatic disease; trials needed (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |
| Chemical entities | Selumetinib | CHEBI:90227 | MEK1/2 inhibitor; approved for NF1 plexiform neurofibromas | Potentially repurposed in RASopathies; emerging case evidence (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10) |


*Table: Compact ontology-aligned mapping of genes, pathways, processes, cells, anatomy, phenotypes and repurposed drugs relevant to Cardiofaciocutaneous syndrome, with concise role notes and literature context citations for use in knowledgebases and curation.*

Gene/protein annotations with ontology terms
- BRAF (HGNC:BRAF): kinase in RAF family; pathway: MAPK cascade (GO:0000165); processes: positive regulation of ERK1/2 cascade (GO:0070374), cell proliferation (GO:0008283); components: plasma membrane→cytosol→nucleus; evidence: review synthesis and cohort summaries (Genes 2023; Nov 22, 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 1-2).
- MAP2K1 (HGNC:MAP2K1) and MAP2K2 (HGNC:MAP2K2): dual‑specificity kinases that activate ERK1/2; processes as above; gene‑specific seizure/ID and motor phenotypes (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5).
- KRAS/NRAS (HGNC:KRAS/HGNC:NRAS): small GTPases upstream of RAF; rare causes of CFC but central to pathway dysregulation (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 2-3).
- YWHAZ (HGNC:YWHAZ): 14‑3‑3 adaptor; de novo variants enhance RAF‑ERK signaling (Genes 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).

Phenotype associations (HPO terms)
- Hypertrophic cardiomyopathy (HP:0001639); Pulmonary valve stenosis (HP:0001642); Seizures (HP:0001250); Intellectual disability (HP:0001249); Ichthyosis (HP:0008064); Sparse hair (HP:0008070); Macrocephaly (HP:0000256); Polyhydramnios (HP:0001561) (Genes 2023; AJMG A 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 1-2, jelin2023obstetricalandneonatal pages 2-2, jelin2023obstetricalandneonatal pages 1-1).

Cell type involvement (CL terms)
- Cardiomyocyte (CL:0000746); Neural progenitor cell (CL:0000047); Keratinocyte (CL:0000312); Lymphatic endothelial cell (CL:0002138); Fibroblast (CL:0000057) (Genes 2023; AJMG A 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, jelin2023obstetricalandneonatal pages 2-2).

Anatomical locations (UBERON terms)
- Heart (UBERON:0000948); Skin (UBERON:0002097); Brain (UBERON:0000955); Lymphatic vessel (UBERON:0004535) (Genes 2023; AJMG A 2023) (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, jelin2023obstetricalandneonatal pages 2-2).

Chemical entities (CHEBI terms)
- Trametinib (CHEBI:85083); Selumetinib (CHEBI:90227)—MEK1/2 inhibitors considered for pathway overactivation in RASopathies including prospective use in CFC (Genes 2023; case evidence in RASopathies) (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).

Evidence items and sources (selected, with dates/links)
- Scorrano G et al. The Cardiofaciocutaneous Syndrome: From Genetics to Prognostic–Therapeutic Implications. Genes. Published Nov 22, 2023. DOI:10.3390/genes14122111. URL: https://doi.org/10.3390/genes14122111 (review) (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2, scorrano2023thecardiofaciocutaneoussyndrome pages 2-3, scorrano2023thecardiofaciocutaneoussyndrome pages 3-5, scorrano2023thecardiofaciocutaneoussyndrome pages 8-10).
- Jelin AC et al. Obstetrical and neonatal outcomes of CFC: prenatal consequences of Ras/MAPK dysregulation. Am J Med Genet A. Published Oct 2023. DOI:10.1002/ajmg.a.63020. URL: https://doi.org/10.1002/ajmg.a.63020 (jelin2023obstetricalandneonatal pages 2-2, jelin2023obstetricalandneonatal pages 1-1).
- Bess J et al. A Literature Review and Pooled Case Analysis of CFC to Estimate Cancer Risk. medRxiv. Posted Aug 2025. DOI:10.1101/2024.08.09.24311751. URL: https://doi.org/10.1101/2024.08.09.24311751 (bess2025aliteraturereview pages 9-13).
- Di Majo BE et al. Cardiofaciocutaneous syndrome and immunodeficiency: international multicenter cohort. Frontiers in Immunology. Published Jul 2025. DOI:10.3389/fimmu.2025.1598896. URL: https://doi.org/10.3389/fimmu.2025.1598896 (majo2025cardiofaciocutaneoussyndromeand pages 11-11).
- Pascarella A et al. Refractory Chylothorax and Ventricular Hypertrophy Treated with Trametinib in Noonan Syndrome: 18‑Month Follow‑Up. Children. Published Oct 2024. DOI:10.3390/children11111342. URL: https://doi.org/10.3390/children11111342 ().

Notes and gaps
- While 2023–2024 literature consolidates CFC molecular mechanisms and prenatal phenotype, high‑quality prospective data on immune complications and cancer risk are still emerging and largely derive from 2025 analyses; CFC‑specific interventional data for MEK inhibitors remain limited to preclinical models and extrapolation from related RASopathies. This motivates genotype‑informed surveillance and participation in disease‑specific trials when available (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10, bess2025aliteraturereview pages 9-13, majo2025cardiofaciocutaneoussyndromeand pages 11-11).


References

1. (scorrano2023thecardiofaciocutaneoussyndrome pages 1-2): Giovanna Scorrano, Emanuele David, Elisa Calì, Roberto Chimenz, Saverio La Bella, Armando Di Ludovico, Gabriella Di Rosa, Eloisa Gitto, Kshitij Mankad, Rosaria Nardello, Giuseppe Donato Mangano, Chiara Leoni, and Giorgia Ceravolo. The cardiofaciocutaneous syndrome: from genetics to prognostic–therapeutic implications. Genes, 14:2111, Nov 2023. URL: https://doi.org/10.3390/genes14122111, doi:10.3390/genes14122111. This article has 18 citations and is from a poor quality or predatory journal.

2. (scorrano2023thecardiofaciocutaneoussyndrome pages 2-3): Giovanna Scorrano, Emanuele David, Elisa Calì, Roberto Chimenz, Saverio La Bella, Armando Di Ludovico, Gabriella Di Rosa, Eloisa Gitto, Kshitij Mankad, Rosaria Nardello, Giuseppe Donato Mangano, Chiara Leoni, and Giorgia Ceravolo. The cardiofaciocutaneous syndrome: from genetics to prognostic–therapeutic implications. Genes, 14:2111, Nov 2023. URL: https://doi.org/10.3390/genes14122111, doi:10.3390/genes14122111. This article has 18 citations and is from a poor quality or predatory journal.

3. (scorrano2023thecardiofaciocutaneoussyndrome pages 3-5): Giovanna Scorrano, Emanuele David, Elisa Calì, Roberto Chimenz, Saverio La Bella, Armando Di Ludovico, Gabriella Di Rosa, Eloisa Gitto, Kshitij Mankad, Rosaria Nardello, Giuseppe Donato Mangano, Chiara Leoni, and Giorgia Ceravolo. The cardiofaciocutaneous syndrome: from genetics to prognostic–therapeutic implications. Genes, 14:2111, Nov 2023. URL: https://doi.org/10.3390/genes14122111, doi:10.3390/genes14122111. This article has 18 citations and is from a poor quality or predatory journal.

4. (jelin2023obstetricalandneonatal pages 2-2): Angie C. Jelin, Amanda Mahle, Susan H. Tran, Teresa N. Sparks, and Katherine A. Rauen. Obstetrical and neonatal outcomes of cardio‐facio‐cutaneous syndrome: prenatal consequences of ras/mapk dysregulation. American Journal of Medical Genetics Part A, 191:323-331, Oct 2023. URL: https://doi.org/10.1002/ajmg.a.63020, doi:10.1002/ajmg.a.63020. This article has 5 citations.

5. (jelin2023obstetricalandneonatal pages 1-1): Angie C. Jelin, Amanda Mahle, Susan H. Tran, Teresa N. Sparks, and Katherine A. Rauen. Obstetrical and neonatal outcomes of cardio‐facio‐cutaneous syndrome: prenatal consequences of ras/mapk dysregulation. American Journal of Medical Genetics Part A, 191:323-331, Oct 2023. URL: https://doi.org/10.1002/ajmg.a.63020, doi:10.1002/ajmg.a.63020. This article has 5 citations.

6. (bess2025aliteraturereview pages 9-13): Jazmyn Bess, Toniya Brown, Sonia Bhala, Anaqa Faizer, Muzzammil Ahmadzada, Alicia A Livinski, Alex Pemov, Jung Kim, Philip S Rosenberg, Gina M Ney, and Douglas R Stewart. A literature review and pooled case analysis of cardiofaciocutaneous syndrome to estimate cancer risk. medRxiv : the preprint server for health sciences, Aug 2025. URL: https://doi.org/10.1101/2024.08.09.24311751, doi:10.1101/2024.08.09.24311751. This article has 2 citations.

7. (scorrano2023thecardiofaciocutaneoussyndrome pages 8-10): Giovanna Scorrano, Emanuele David, Elisa Calì, Roberto Chimenz, Saverio La Bella, Armando Di Ludovico, Gabriella Di Rosa, Eloisa Gitto, Kshitij Mankad, Rosaria Nardello, Giuseppe Donato Mangano, Chiara Leoni, and Giorgia Ceravolo. The cardiofaciocutaneous syndrome: from genetics to prognostic–therapeutic implications. Genes, 14:2111, Nov 2023. URL: https://doi.org/10.3390/genes14122111, doi:10.3390/genes14122111. This article has 18 citations and is from a poor quality or predatory journal.

8. (majo2025cardiofaciocutaneoussyndromeand pages 11-11): Benedetta Elena Di Majo, Chiara Leoni, Eleonora Cartisano, Chiara Fossati, Germana Viscogliosi, Valentina Trevisan, Lucia Pia Bruno, Francesca Conti, Mattia Moratti, Emilia Monaco, Donato Rigante, Beatrice Rivalta, Caterina Cancrini, Aleksandra Szczawińska-Popłonyk, Aleksander Jamsheer, Monika Obara-Moszyńska, Viktoria Zakharova, Anna Shcherbina, Julija Rodina, Beyhan Tüysüz, Saumya Shekhar Jamuar, Jiin Ying Lim, Jeannette Goh, Anna Cereda, Teresa Agovino, Ilaria Contaldo, Maria Luigia Gambardella, Adriana Cristina Balduzzi, Alessia Cherubino, Giovanni Antonio Marrocco, Silvia Bellesi, Valentina Carusi, Gabriele Rumi, Andrea Biondi, Giuseppe Zampino, and Francesco Saettini. Cardiofaciocutaneous syndrome and immunodeficiency: data from an international multicenter cohort. Frontiers in Immunology, Jul 2025. URL: https://doi.org/10.3389/fimmu.2025.1598896, doi:10.3389/fimmu.2025.1598896. This article has 2 citations and is from a peer-reviewed journal.

9. (koslaUnknownyearmap2k2(mek2)in pages 1-4): M Kośla. Map2k2 (mek2) in cardiofaciocutaneous (cfc) syndrome-research roadmap. Unknown journal, Unknown year.

10. (koslaUnknownyearmap2k2(mek2)in pages 10-10): M Kośla. Map2k2 (mek2) in cardiofaciocutaneous (cfc) syndrome-research roadmap. Unknown journal, Unknown year.