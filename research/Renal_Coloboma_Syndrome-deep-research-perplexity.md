---
provider: perplexity
model: sonar-reasoning-pro
cached: false
start_time: '2026-09-09T20:00:48.574571'
end_time: '2026-09-09T20:04:05.793014'
duration_seconds: 197.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Renal Coloboma Syndrome
  mondo_id: MONDO:0007352
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 52
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 55
  not_found: 0
  obsolete: 3
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 56
  labels_matching: 14
  labels_mismatched: 29
  mislabelled_terms:
  - term_id: HP:0000128
    reported_labels:
    - Small kidney
    ontology_label: Renal potassium wasting
  - term_id: HP:0000112
    reported_labels:
    - Chronic kidney disease
    - 'HPO: *Chronic kidney disease'
    - CKD
    ontology_label: Nephropathy
  - term_id: HP:0000585
    reported_labels:
    - Optic disc dysplasia
    ontology_label: Band keratopathy
  - term_id: HP:0001103
    reported_labels:
    - Retinal coloboma
    - 'HPO: *Retinal coloboma'
    ontology_label: Abnormal macular morphology
  - term_id: GO:0072043
    reported_labels:
    - nephron development
    - Nephron development
    ontology_label: regulation of pre-tubular aggregate formation by cell-cell signaling
  - term_id: GO:0030839
    reported_labels:
    - podocyte differentiation
    ontology_label: regulation of intermediate filament polymerization
  - term_id: GO:0036052
    reported_labels:
    - glomerular filtration barrier maintenance
    ontology_label: protein localization to uropod
  - term_id: GO:0008038
    reported_labels:
    - optic nerve development
    - Optic nerve development
    ontology_label: neuron recognition
  - term_id: CL:0002518
    reported_labels:
    - nephron progenitor cell
    - 'Kidney: *nephron progenitor cell'
    - Nephron progenitor cell
    ontology_label: kidney epithelial cell
  - term_id: CL:0002511
    reported_labels:
    - parietal epithelial cell
    ontology_label: CD11b-low, CD103-negative, langerin-negative lymph node dendritic
      cell
  - term_id: CL:0002066
    reported_labels:
    - renal tubular epithelial cell
    ontology_label: Feyrter cell
  - term_id: UBERON:0005052
    reported_labels:
    - metanephros
    - Metanephros
    ontology_label: gizzard
  - term_id: UBERON:0001626
    reported_labels:
    - optic nerve
    - 'UBERON: *optic nerve'
    - 'Eyes: optic nerve'
    - Optic nerve
    ontology_label: left coronary artery
  - term_id: GO:0072033
    reported_labels:
    - nephron
    ontology_label: renal vesicle formation
  - term_id: GO:0098853
    reported_labels:
    - podocyte foot process
    ontology_label: endoplasmic reticulum-vacuole membrane contact site
  - term_id: HP:0008672
    reported_labels:
    - Bilateral renal hypoplasia
    ontology_label: Calcium oxalate nephrolithiasis
  - term_id: HP:0001123
    reported_labels:
    - Bilateral optic disc coloboma
    ontology_label: Visual field defect
  - term_id: NCIT:C14432
    reported_labels:
    - Genetic Testing
    ontology_label: Swiss Strains
  - term_id: NCIT:C17772
    reported_labels:
    - Renal Ultrasound
    ontology_label: CD44 Antigen
  - term_id: NCIT:C17895
    reported_labels:
    - Ophthalmologic Examination
    ontology_label: Cell Lineage
  - term_id: NCIT:C230
    reported_labels:
    - Antihypertensive Therapy
    ontology_label: Amikacin Sulfate
  - term_id: NCIT:C16888
    reported_labels:
    - Renal Dialysis
    ontology_label: Myelogram
  - term_id: NCIT:C15273
    reported_labels:
    - Kidney Transplantation
    - contextual
    ontology_label: Longitudinal Study
  - term_id: NCIT:C51880
    reported_labels:
    - related concept
    ontology_label: Study Coordinator
  - term_id: NCIT:C50439
    reported_labels:
    - Ophthalmic Surgery
    ontology_label: Joint Disorder
  - term_id: NCIT:C16088
    reported_labels:
    - Supportive Care
    ontology_label: Extraordinary Opportunities for Investment
  - term_id: NCIT:C94406
    reported_labels:
    - Genetic Counseling
    ontology_label: Autologous Bone Marrow
  - term_id: NCIT:C17226
    reported_labels:
    - Prenatal Diagnosis
    ontology_label: Tyrosinase
  - term_id: NCIT:C128244
    reported_labels:
    - Preimplantation Genetic Testing
    ontology_label: Vulvar Small Cell Neuroendocrine Carcinoma
  labels_variant: 13
  obsolete_terms:
  - term_id: HP:0001388
    ontology_label: obsolete Joint laxity
    replaced_by: HP:0001382
  - term_id: NCIT:C14432
    ontology_label: Swiss Strains
  - term_id: NCIT:C50439
    ontology_label: Joint Disorder
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Coloboma Syndrome
- **MONDO ID:** MONDO:0007352 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Renal Coloboma Syndrome** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

Renal coloboma syndrome (RCS), now largely subsumed under the broader concept of **PAX2‑related disorder**, is a rare autosomal dominant developmental disease characterized primarily by renal hypodysplasia and optic nerve anomalies that frequently progress to chronic kidney disease and may cause significant visual impairment.[16][41][46][49][50][33][36]

---

## 1. Disease Information

**Definition and clinical overview**

Renal coloboma syndrome (OMIM 120330) is a congenital developmental disorder defined by the combination of structural kidney abnormalities (typically bilateral renal hypodysplasia) and optic nerve malformations (classically optic nerve coloboma or dysplasia).[46][49][50][33][36]  
Consequences of renal hypodysplasia include hypertension, proteinuria, renal insufficiency, and a high risk of progression to end‑stage kidney disease (ESKD).[33][36][31][38]  
Ocular anomalies range from subtle optic disc dysplasia to large optic nerve colobomas or “morning glory” disc anomalies, with visual outcomes ranging from normal vision to severe visual impairment and blindness.[33][36][42][44]  
The disorder is now typically conceptualized as **PAX2‑related disorder**, encompassing classic RCS plus broader renal and ocular phenotypes, including CAKUT (congenital anomalies of the kidney and urinary tract) and hereditary focal segmental glomerulosclerosis (FSGS) type 7.[2][16][22][28][63]

**Key identifiers and classification**

- OMIM: 120330 (Renal coloboma syndrome).[46][49][54][60]  
- Orphanet: ORPHA:1475 (Renal coloboma syndrome).[46][47][57][60]  
- MONDO: MONDO:0007352 (Renal Coloboma Syndrome).[51][52][53][56][60]  
- MedGen: C1852759 (Renal coloboma syndrome / PAX2‑related disorder).[41][51][52][46]  
- Disease Ontology: DOID:0090006 (renal coloboma syndrome).[60]  
- UMLS: C1852759.[46][41]  
- ICD‑10‑CM: Q60.4 (renal hypoplasia) is listed as an alternative ID in the Disease Ontology entry for RCS.[60]

**Synonyms and alternative names**

Commonly used synonyms include:[49][50][58][60][51][52]  

- Papillorenal syndrome / papillo‑renal syndrome  
- Papillorenal (papillo‑renal) syndrome with macular abnormalities  
- Optic nerve coloboma with renal disease  
- Coloboma of optic nerve with renal disease  
- Optic coloboma, vesicoureteral reflux, and renal anomalies  
- CAKUT with or without ocular abnormalities  
- Renal‑coloboma syndrome (RCS)

**Data sources**

Most information derives from aggregated disease‑level resources (OMIM, Orphanet, GeneReviews, MedGen, GARD, Disease Ontology) and published case series and cohort studies rather than individual EHR‑level datasets.[46][49][50][16][33][36][20]  
Key narrative and management information comes from GeneReviews (PAX2‑Related Disorder, major revision 2025) and expert reviews.[16][17][29][33][36]

---

## 2. Etiology

### 2.1 Primary causal factors

RCS/PAX2‑related disorder is predominantly caused by **heterozygous loss‑of‑function variants in PAX2**, a paired box transcription factor gene on chromosome 10q24.[46][49][50][26][14][63]  
Mutations in PAX2 are identified in approximately 50% of individuals with classic renal hypodysplasia and optic nerve abnormalities meeting historical criteria for RCS.[46][20][26][44]  
PAX2 variants are the **only well‑established genetic cause** of classic RCS to date.[26][49][50]

Direct quote (human clinical, 1999 AJHG, PMID:10466411):  
> “Optic nerve coloboma combined with renal disease, also called renal‑coloboma syndrome (… OMIM), … results from autosomal dominant mutations in the PAX2 gene.”[49]

PAX2‑related disorder also includes nonsyndromic CAKUT (kidney hypoplasia, vesicoureteral reflux, multicystic dysplastic kidney) and hereditary FSGS7.[2][22][63][75][28]  

### 2.2 Genetic risk factors

**Causal variants**

Multiple studies and locus‑specific databases have catalogued at least 30–40 unique PAX2 mutations in RCS families.[20][23][24][25]  
An updated literature review identified 33 unique PAX2 mutations across 53 families, with the recurrent hotspot **c.76dupG (p.V26Gfs*28)** in exon 2 reported in ~40% of cases in one series.[20][19][22][25]  
Pathogenic variants include frameshift, nonsense, splice‑site, missense, and small multi‑nucleotide deletions/insertions, predominantly in exons 2–4 encoding the paired domain and in the homeodomain.[26][22][23][25]  

Direct quote (review; human clinical, Frontiers in Pediatrics 2022, PMID:8787321):  
> “These mutations are mostly located at the paired domain (exons 2–4) and the homeodomain. The most common type of pathogenic variant is frameshift mutation, and the most frequently reported mutation is c.76dupG (p.V26Gfs*28).”[22]

ClinGen curation supports PAX2 **haploinsufficiency** as the pathogenic dosage mechanism.[14]  

**Penetrance and expressivity**

PAX2‑related disorder is highly penetrant: renal structural or functional abnormalities are present in ~92% and ophthalmologic abnormalities in ~77% of mutation carriers in GeneReviews and MedGen datasets.[16][41][22]  
Expressivity is strikingly variable, even among individuals carrying identical mutations, with intra‑familial variability ranging from severe bilateral renal hypodysplasia and blindness to mildly impaired renal function or isolated optic disc abnormalities.[30][33][36][24]  

### 2.3 Environmental and lifestyle risk factors

Specific environmental or lifestyle risk factors for *developing* RCS are not identified, as PAX2‑related disease is primarily a monogenic, autosomal dominant disorder.[16][46][49]  
However, progression of kidney disease in affected individuals is likely influenced by general CKD modifiers such as hypertension, proteinuria, and possibly nephrotoxic exposures, as inferred from CKD literature and highlighted in clinical reviews.[33][36][29][38]  

### 2.4 Protective factors

No specific genetic protective alleles or environmental protective factors have been defined for RCS/PAX2‑related disorder.[16][22][29][63]  
Standard CKD protective measures (blood pressure control, RAAS blockade, avoidance of nephrotoxins) are extrapolated as beneficial but have not been formally studied specifically in PAX2 cohorts.[33][36][29]

### 2.5 Gene–environment interactions

Formal gene–environment interaction studies in PAX2‑related disorder have not been reported, and current understanding centers on **gene‑driven developmental defects** with secondary environmental modulation of CKD progression.[63][22][29][36]

---

## 3. Phenotypes

Key human phenotypes are summarized from Orphanet, MedGen, GARD, GeneReviews, and clinical series.[46][47][41][31][33][36][20][44][43]

### 3.1 Major renal phenotypes

1. **Renal hypodysplasia / hypoplasia**  
   - Phenotype type: structural kidney abnormality (clinical sign).  
   - HPO term: *Renal hypodysplasia* (HP:0000089); *Small kidney* (HP:0000128).  
   - Characteristics: Usually bilateral, often detected in childhood via ultrasound or CKD workup; severity is highly variable.[33][36][42][46]  
   - Frequency: Reported as the most common renal manifestation, present in ~65% or more of affected individuals in series and >90% in mutation carriers when broader kidney abnormalities are included.[36][22][16][41]  
   - Progression: Frequently progressive to CKD and ESKD; age at ESKD highly variable.[33][35][36][38]  
   - QoL impact: Progressive CKD requiring dialysis or transplant substantially impairs physical functioning and long‑term health.[33][36][35][38]

2. **Chronic kidney disease and end‑stage renal disease (ESRD/ESKD)**  
   - Phenotype type: laboratory abnormality / systemic disease.  
   - HPO: *Chronic kidney disease* (HP:0000112); *End‑stage renal failure* (HP:0003774).  
   - Characteristics: Proteinuria, reduced GFR, hypertension; many patients progress to ESRD, often in childhood or young adulthood.[33][36][31][38][29]  
   - Frequency: One article aimed at clinicians reports that approximately 33% of RCS patients develop ESRD.[38]  
   - QoL impact: Dialysis dependence and transplant candidacy are major determinants of morbidity and health‑related quality of life.[33][35][36]

3. **Vesicoureteral reflux (VUR) and CAKUT spectrum**  
   - HPO: *Vesicoureteral reflux* (HP:0000076); *Abnormal renal morphology* (HP:0012210).  
   - Characteristics: VUR, ureteral anomalies, multicystic dysplastic kidney, kidney cysts, and other CAKUT phenotypes are frequently reported.[43][54][75][36][38]  
   - Frequency: Variable; VUR reported in multiple RCS families and CAKUT phenotypes are common in broader PAX2 disorder cohorts.[43][54][75][23][28]  
   - QoL impact: Recurrent urinary tract infections and renal scarring add morbidity.[33][36][38]

4. **Proteinuria and hypertension**  
   - HPO: *Proteinuria* (HP:0000093); *Hypertension* (HP:0000822).  
   - Characteristics: Common clinical manifestations resulting from reduced nephron number and secondary glomerular injury.[33][32][34][36][38]  
   - Frequency: Described as “most frequent clinical symptoms” in a 2024/2025 review: hypertension, proteinuria, vesicoureteral reflux, renal failure.[32][34]  
   - QoL impact: Long‑term cardiovascular and renal burden.[33][36]

5. **Hereditary focal segmental glomerulosclerosis (FSGS type 7)**  
   - HPO: *Focal segmental glomerulosclerosis* (HP:0000097).  
   - Characteristics: In some PAX2‑related families, dominant podocyte disease with FSGS and proteinuria is the predominant phenotype, sometimes with subtle structural kidney changes.[24][28][70][63]  
   - Evidence: Human clinical (families with FSGS7); supported by podocyte and parietal epithelial cell models.[24][28][70]

### 3.2 Ocular phenotypes

1. **Optic nerve coloboma / dysplasia**  
   - Phenotype type: structural ocular anomaly.  
   - HPO: *Optic disc coloboma* (HP:0000589); *Optic disc dysplasia* (HP:0000585).  
   - Characteristics: Wide, dysplastic optic disc with anomalous retinal vessel emergence; deep excavation or pits; sometimes termed “morning glory disc anomaly.”[33][36][42][44][37][58]  
   - Frequency: Optic nerve anomalies present in the majority of RCS patients; classic database counts show optic nerve coloboma in 84/125 cases, disc dysplasia in 21, pits in 14, morning glory discs in 10, etc.[44]  
   - Age of onset: Congenital; recognized in infancy/childhood during ophthalmic examination.[33][36][42][44]  
   - QoL impact: Visual acuity ranges from normal to blindness; retinal detachment risk contributes to further visual loss.[33][36][44]

   Direct quote (human clinical summary, 2012 database, PMC):  
   > “Classic ophthalmologic findings include optic nerve coloboma, morning glory anomaly, and excavation of the optic disc.”[44]

2. **Retinal and macular anomalies**

   - HPO: *Retinal coloboma* (HP:0001103); *Pigmentary macular dystrophy* (HP:0007754).  
   - Findings: Retinal coloboma, pigmentary macular dysplasia, scleral staphyloma, optic nerve cyst, and other posterior segment abnormalities are described.[36][42][44][37]  
   - QoL impact: May severely reduce central vision in some patients.[33][36]

3. **Other ocular features**

   - HPO: *Small cornea* (HP:0000482); *Cataract* (HP:0000518).  
   - Less common findings: small corneal diameter, cataract, scleral staphyloma.[36][45][39]  

Notably, iris colobomas **have not been reported** in PAX2‑related disorder, an important differentiator from other colobomatous syndromes.[41]

### 3.3 Extra‑renal, extra‑ocular phenotypes

Reported additional features include:[33][36][39][43][31]

- High‑frequency sensorineural hearing loss (HPO: *Sensorineural hearing impairment*, HP:0000407).[33][39][43]  
- Joint laxity / loose joints (HP:0001388).[31]  
- Central nervous system anomalies (e.g., corpus callosum anomalies) (HP:0002190).[43][39]  
- Genital anomalies (HP:0000083) in some families.[43][39]  
- Mild growth or developmental issues reported sporadically.[33][36]

Quality‑of‑life impact for these features is variable; formal QOL studies specific to RCS are lacking, but combined visual, renal, auditory, and neurological impairments can substantially affect daily functioning.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

- **PAX2** (paired box 2)  
  - HGNC: HGNC:8619  
  - Chromosome: 10q24.31.[3][11][14][57]  
  - Gene function: Transcription factor of the paired box family, critical in kidney, urinary tract, optic nerve, inner ear, and CNS development.[69][71][62][63]

Direct quote (NCBI Gene summary):  
> “Mutations within PAX2 have been shown to result in optic nerve colobomas and renal hypoplasia.”[14]

ClinGen dosage curation identifies **sufficient evidence for haploinsufficiency pathogenicity**.[14]

### 4.2 Pathogenic variants

**Variant classes and locations**

- Frameshift variants (e.g., c.76dupG, c.70‑72delinsA, c.576del) causing premature truncation and loss of function.[20][22][25][23][24]  
- Nonsense variants leading to truncated proteins.[20][26][23]  
- Splice‑site variants affecting exon–intron boundaries.[20][22][23]  
- Missense variants, often within the paired domain (exons 2–4), resulting in hypomorphic alleles.[73][26][18][27]  
- Multi‑exon deletions and duplications detected by MLPA or copy‑number analysis in some families.[9][15][52][51]

Direct quote (clinical utility gene card; human clinical, 2011 EJHG):  
> “The majority of mutations are deletions or duplications of a single nucleotide, missense mutations, nonsense mutations or small deletions or duplications of two or more nucleotides occurring in exons 2, 3 and 4 encoding the paired domain.”[26]

**Variant examples (human clinical)**

- c.76dupG (p.V26Gfs*28) frameshift hotspot.[20][19][22]  
- c.70‑72delinsA (Gly24Argfs*29) truncating mutation in exon 2.[25]  
- c.418C>T (p.R140W) missense mutation in a papillorenal patient.[8]  
- Novel deletion mutations associated with multicystic dysplastic kidney.[54]  
- Various intronic variants near exon 5 reported in an Indian family (e.g., c.617‑70C>A).[21]

**ACMG classification and ClinVar**

Most classic truncating or canonical splice‑site variants are classified as **pathogenic** or **likely pathogenic** under ACMG criteria.[15][51][52][55]  
ClinVar entries for RCS list numerous pathogenic and likely pathogenic PAX2 variants with MONDO:0007352, OMIM 120330, Orphanet 1475 identifiers.[51][52][55]

**Somatic vs germline**

All clinically relevant PAX2 variants in RCS are **germline**; tests are designed for heritable germline changes and not for somatic tumor variants.[4][3][14]  

### 4.3 Allele frequencies

Pathogenic PAX2 variants are rare in population databases (gnomAD, ExAC) and usually either absent or present at extremely low frequency, consistent with their strong effect and autosomal dominant inheritance; specific allele frequencies for canonical RCS variants are generally <0.0001.[22][23][63]  

### 4.4 Functional consequences

Functional studies and animal models support **loss of function and haploinsufficiency** as the core mechanism for most RCS variants:[69][64][73][61]

- Pax2 germline null mice show complete renal agenesis and absence of ureters and genital tracts.[69][66]  
- Pax2+/– mice and Pax2+/–;Pax8+/– mice have severe renal hypodysplasia, reduced nephron number and ureteric tips, increased apoptosis in developing nephrons, and impaired distal tubule formation.[67][64][73][72]  
- Human papillorenal missense variants in PAX2 behave as hypomorphic alleles in mouse and cell models, causing reduced transcriptional activity rather than complete loss.[73][18]  

Direct quote (mouse/human functional, hypomorphic alleles):  
> “Papillorenal Syndrome‑Causing Missense Mutations in PAX2/Pax2 Result in Hypomorphic Alleles in Mouse and Human.”[73]

### 4.5 Modifier genes and epigenetics

No robust human modifier genes have been identified in RCS, though variability in phenotype suggests potential genetic background effects.[30][24][36]  
Specific epigenetic mechanisms (PAX2 promoter methylation, chromatin changes) in RCS have not been systematically characterized, though PAX2 epigenetic regulation is studied in other renal contexts.[63]

### 4.6 Chromosomal abnormalities

Large‑scale chromosomal rearrangements involving 10q24 and encompassing PAX2 have been reported in a few individuals, but are rare compared to intragenic variants.[52][51]  

---

## 5. Environmental Information

No disease‑specific environmental etiologies have been identified; PAX2‑related disorder is primarily genetic.[16][46][49]  

**Non‑genetic contributing factors (secondary)**  
Progression to CKD and ESRD is influenced by conventional environmental and lifestyle factors (such as hypertension, proteinuria, salt intake, and nephrotoxins), inferred from CKD management literature and noted in reviews as important targets for monitoring and intervention.[33][36][29][38]  

There is currently **no evidence** for infectious agents or specific toxins causing RCS directly.[63][22]

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (conceptual)

1. **Heterozygous loss‑of‑function or hypomorphic mutation in PAX2** → leads to reduced PAX2 transcriptional activity and impaired regulation of nephric and optic nerve developmental programs (demonstrated in mouse and human models).[69][64][73][61][71][68]  
2. Impaired PAX2 function in intermediate mesoderm and ureteric bud → results in defective nephron progenitor specification, reduced ureteric bud branching, and increased apoptosis of nephric lineage cells, causing CAKUT and reduced nephron endowment (demonstrated).[69][64][67][72][62]  
3. Reduced nephron number and structural kidney anomalies (renal hypodysplasia, VUR, cysts) → lead to hyperfiltration and susceptibility to chronic glomerular stress, culminating in chronic kidney disease and ESRD (inferred from CKD pathophysiology combined with human RCS cohorts).[33][36][70][75]  
4. Impaired PAX2 function in podocytes and parietal epithelial cells → results in reduced “podocyte fitness,” nuclear maintenance defects, and decreased regenerative capacity under stress, predisposing to focal segmental glomerulosclerosis (FSGS7) and disproportionate albuminuria (demonstrated in podocyte models and murine Pax2 variants).[70][24][28]  
5. PAX2 deficiency in optic nerve and ventral eye structures → leads to abnormal closure of the optic fissure, mispatterned optic stalk, altered neuronal/glial fate (favoring astroglial development and blocking neuronal differentiation), producing optic nerve coloboma, pits, and dysplastic optic discs (demonstrated).[71][68][74]  
6. Optic nerve malformations and retinal anomalies → result in decreased visual acuity, retinal detachment risk, and variable visual impairment (demonstrated clinically).[33][36][44]  
7. Secondary CKD consequences (hypertension, proteinuria, cardiovascular strain) and visual impairment → together cause long‑term morbidity, potential ESRD, and significant impact on quality of life (demonstrated clinically).[33][35][36][38]

### 6.2 Molecular pathways and cellular processes

**Kidney development and CAKUT**

PAX2 acts as a key transcriptional regulator in intermediate mesoderm, ureteric bud, and nephron progenitors.[69][64][62][72][65]  

- GO biological processes (suggested):  
  - *kidney development* (GO:0001822).[62][69]  
  - *nephron development* (GO:0072043).[64][72][65]  
  - *branching morphogenesis of an epithelial tube* (GO:0048754).[67][72]  
  - *regulation of apoptosis* (GO:0042981).[67][73]  

Mouse studies show that Pax2–/– embryos lack kidneys, ureters, and genital tracts because nephrogenic mesenchyme fails to undergo mesenchymal–epithelial transition and ureteric bud induction.[69][64]  
Pax2/Pax8 double mutants fail to form pronephros or later nephric structures, with intermediate mesoderm lost by apoptosis.[64]  
Pax2+/–;Pax8+/– kidneys are severely hypodysplastic, with reduced nephron number and ureteric tips and strong reduction of Lim1 expression, a regulator of nephron differentiation.[67]  

Direct quote (mouse, organogenesis, PMID:8575306):  
> “Pax2 homozygous mutant newborn mice lack kidneys, ureters and genital tracts. … Mesenchyme of the nephrogenic cord fails to undergo epithelial transformation and is not able to form tubules.”[69]

**Podocyte and parietal epithelial cell injury**

An editorial on PAX2‑associated nephropathy integrates human and experimental data, proposing dual developmental and podocyte pathways:[70]

Direct quote (human + experimental; 2025 commentary, PMC):  
> “The clinical data assembled … suggest that PAX2 nephropathy reflects the convergence of 2 mechanistic pathways: (i) a developmental pathway, in which impaired kidney morphogenesis … results in CAKUT and reduced nephron endowment … and (ii) a podocyte pathway, in which otherwise properly formed nephrons exhibit reduced ‘podocyte fitness,’ leading to disproportionate albuminuria and progression to FSGS.”[70]

CRISPR‑based correction of PAX2 mutations restored podocyte resilience in vitro, and murine Pax2 variants disrupted nuclear maintenance in parietal epithelial cells and podocyte homeostasis, reducing regenerative capacity under stress.[70]  

Suggested GO terms:  

- *podocyte differentiation* (GO:0030839).[70]  
- *glomerular filtration barrier maintenance* (GO:0036052).[70]  
- *epithelial cell proliferation* (GO:0050673).[73][72]

**Optic nerve and eye development**

Pax2 regulates patterning of the optic stalk, closure of the optic fissure, and neuronal vs glial fate in the optic nerve.[71][68][74]  

Direct quote (mouse optic nerve; PMID:8951055):  
> “Our results identify Pax2 as a major regulator of patterning during organogenesis of the eye and inner ear and indicate its function in morphogenetic events required for closure of the optic fissure and neural tube.”[71]

In explanted optic nerves, Pax2 down‑regulation permits neuronal differentiation, whereas overexpression blocks neuronal fate and allows glial development, indicating a critical role in astroglial specification.[68]  

Suggested GO terms:  

- *optic nerve development* (GO:0008038).[71][68]  
- *glial cell differentiation* (GO:0010001).[68][74]  

**Cell types (suggested CL terms)**  

- Kidney: *nephron progenitor cell* (CL:0002518), *podocyte* (CL:0000653), *parietal epithelial cell* (CL:0002511), *renal tubular epithelial cell* (CL:0002066).[65][73][70]  
- Optic nerve: *astrocyte* (CL:0000127), *retinal ganglion cell* (CL:0000740).[68][71][74]

**Tissue and cellular compartments (suggested UBERON / GO CC terms)**  

- UBERON: *kidney* (UBERON:0002113), *metanephros* (UBERON:0005052).[69][62]  
- UBERON: *optic nerve* (UBERON:0001626).[71][74]  
- GO Cellular Component: *nucleus* (GO:0005634), *nephron* (GO:0072033), *podocyte foot process* (GO:0098853).[70][73]

**Epigenetics and multi‑omics**

While multi‑omics data specific to RCS are limited, transcriptomic analyses of PAX2‑regulated gene networks in kidney development have identified candidate downstream genes and pathways, supporting PAX2 as an essential transcription factor for nephrogenesis.[62][63]  
Formal single‑cell or spatial transcriptomics datasets specifically focused on PAX2‑related disorder in humans have not yet been reported (as of 2024–2025 literature).[62][65][70]

---

## 7. Anatomical Structures Affected

### 7.1 Organ‑level involvement

Primary organs:[33][36][42][46][41]

- Kidneys (UBERON:0002113): small, hypodysplastic, structurally abnormal; often bilateral.  
- Eyes: optic nerve (UBERON:0001626), retina (UBERON:0001476), optic disc.  

Secondary systems:[33][36][43][39]

- Urinary tract (ureters, bladder) – vesicoureteral reflux and CAKUT.  
- Cardiovascular system – secondary hypertension and CKD‑associated cardiovascular risk.  
- Auditory system – inner ear involvement leading to high‑frequency hearing loss.  
- CNS and genital tract – occasional anomalies consistent with PAX2 expression during development.[43][69][71]

### 7.2 Tissue and cell types

- Renal: nephron progenitors, podocytes, parietal epithelial cells, tubular epithelium.[64][65][72][73][70]  
- Optic nerve: retinal ganglion cell axons and astroglial cells.[71][68][74]  
- Inner ear: structures involved in patterning and sensory function.[71][69]

### 7.3 Subcellular compartments

PAX2 is a nuclear transcription factor; disease mechanisms relate to altered transcriptional programs rather than specific organellar defects.[63][73]  
Suggested GO CC: *nucleus* (GO:0005634), *chromatin* (GO:0000785).[63][73]

### 7.4 Localization and lateralization

Kidney abnormalities are usually bilateral but can be asymmetric; optic nerve anomalies are often bilateral but may be more severe in one eye.[33][36][35][44]  
HPO: *Bilateral renal hypoplasia* (HP:0008672); *Bilateral optic disc coloboma* (HP:0001123).

---

## 8. Temporal Development

### 8.1 Onset

RCS is fundamentally **congenital**, with renal and ocular anomalies present from birth due to disrupted embryonic development.[33][36][46][49][50]  
Renal disease may present in infancy, childhood, or later depending on severity; some individuals are diagnosed in adulthood after incidental findings.[33][36][22][29]  
Ocular anomalies are typically recognized in infancy or childhood through fundus examination, although subtle disc dysplasia may be detected only on detailed ophthalmologic assessment.[33][36][41][44]

### 8.2 Progression

Renal disease course is generally **chronic and progressive**, often culminating in ESRD.[33][35][36][38][29]  
The rate of progression is variable; some individuals reach ESRD in childhood, while others maintain moderate CKD into adulthood.[33][35][36]  
Ocular anomalies are structurally static but carry cumulative risk of complications such as retinal detachment and progressive visual decline.[33][36][44]

There are no defined formal stages analogous to cancer staging; progression is typically described in CKD stages according to GFR.[33][36]

### 8.3 Patterns and critical periods

There is no remission in structural anomalies; renal function may be stable for years before declining, especially in individuals with milder hypodysplasia.[33][36][24][75]  
Critical periods include prenatal and early postnatal kidney and optic nerve development, when PAX2 function is essential.[69][64][71][62]  

---

## 9. Inheritance and Population

### 9.1 Inheritance pattern

RCS/PAX2‑related disorder follows **autosomal dominant inheritance**.[49][50][58][56]  

Direct quote (clinical review):  
> “Renal coloboma (papillorenal) syndrome is an autosomal dominant condition that can be caused by mutations in PAX2.”[58]

Penetrance is high, but expressivity is highly variable.[16][22][30][24]  
De novo mutations and possible germline mosaicism have been documented; for example, a novel exon 2 deletion (delT602) was identified in a child but absent in parents, demonstrating de novo mutation or germline mosaicism.[27]

### 9.2 Epidemiology

RCS is rare; Orphanet categorizes it as a **rare genetic disease** with very low prevalence, and exact incidence/prevalence figures are not available.[46]  
By 2012, database reviews had compiled 53 families and 125 cases with documented optic nerve abnormalities, suggesting several hundred reported individuals worldwide.[20][44]  
There are no robust population‑based prevalence or incidence estimates.[46][36][20]

### 9.3 Population demographics

Cases have been reported worldwide (Europe, North America, Asia, including India), with no clear ethnic predilection.[20][23][21][24][36]  
Sex distribution appears approximately equal in reported series; no strong sex bias is noted.[33][36][20]  
Age at diagnosis spans from infancy to adulthood; pediatric presentations predominate due to congenital anomalies and CKD.[33][36][23][6]  

Founder mutations have not been well defined, though recurrent hotspot c.76dupG suggests possible founder effects in some populations.[20][19][22]  
Consanguinity is not a major driver, given autosomal dominant inheritance.[49][58][26]

Carrier frequency for pathogenic PAX2 alleles is presumed to be extremely low globally, consistent with rarity and high penetrance.[22][23][63]

---

## 10. Diagnostics

### 10.1 Clinical evaluation

Core diagnostic triad: **renal hypodysplasia/CKD + optic nerve anomalies + heterozygous PAX2 pathogenic variant**.[16][13][33][36][41]

Direct quote (GeneReviews, human clinical, PMID:20301624):  
> “The diagnosis of PAX2‑related disorder is established in a proband with the characteristic renal and/or eye findings by the identification of a heterozygous pathogenic variant in PAX2 by molecular genetic testing.”[13][16]

**Laboratory tests**

- Serum creatinine and estimated GFR to stage CKD.[33][36][41]  
- Urinalysis for proteinuria and hematuria.[33][36][13]  
- Blood pressure measurement for hypertension.[33][36][13]  

LOINC terms (suggested): *Creatinine [Mass/volume] in Serum or Plasma*, *Protein [Presence] in Urine*, *Blood pressure systolic & diastolic*.

**Imaging**

- Renal ultrasound to detect small kidneys, hypodysplasia, cysts, and CAKUT.[33][36][13][36]  
- Voiding cystourethrography (VCUG) when VUR is suspected.[43][54][75]  

**Ophthalmologic examination**

- Dilated fundus examination to assess optic disc coloboma, dysplasia, pits, morning glory anomaly, and retinal coloboma.[33][36][44][37][42][58]  

**Other evaluations**

- Audiology for high‑frequency hearing loss.[33][39][43]  
- Neurological imaging if CNS anomalies are suspected.[43][36]

### 10.2 Genetic testing

Genetic testing is central to diagnosis and family management.[16][13][15][3][10][6][23]

Testing modalities:

1. **Single‑gene PAX2 testing**  
   - Sanger sequencing of all 12 coding exons and exon–intron boundaries was historically the standard; expected analytical sensitivity >99% for missense, frameshift, and splice‑site mutations.[15][9][26]  
   - Modern NGS‑based PAX2 sequencing assays are widely available and designed for germline variant detection.[3][4][11]

2. **Copy‑number analysis**  
   - MLPA or quantitative PCR for exon deletions/duplications; used when Sanger sequencing is negative but suspicion remains.[9][15][52]

3. **Gene panels**  
   - CAKUT and hereditary nephropathy panels that include PAX2, used for unexplained renal malformations and proteinuric CKD.[10][23][6][11]

4. **Whole‑exome sequencing (WES) / genome sequencing (WGS)**  
   - WES/WGS identifies PAX2 variants incidentally or in diagnostic workups for pediatric renal disorders and syndromic cases.[6][23][22]  
   - WES was used systematically in a 2025 cohort of children with PAX2 mutation‑associated disorders, followed by Sanger verification for cosegregation.[6]

5. **Prenatal and preimplantation genetic testing**  
   - When a familial PAX2 pathogenic variant is known, prenatal diagnosis and preimplantation genetic testing are possible.[13][15][17]

GTR and GeneReviews list many clinical tests, including targeted PAX2 sequencing for “renal coloboma syndrome” and “renal hypoplasia.”[3][5][11][13][17]

### 10.3 Clinical criteria and differential diagnosis

While no formal consensus criteria exist, typical diagnostic features include:[33][36][16][41]

- Bilateral or unilateral renal hypodysplasia or other CAKUT phenotype.  
- Optic nerve coloboma/dysplasia or related disc anomaly.  
- Autosomal dominant family history or de novo mutation.  
- Heterozygous PAX2 pathogenic variant.

Differential diagnoses include other syndromes combining ocular coloboma and renal disease or CAKUT, such as CHARGE syndrome, CAT eye syndrome, COACH syndrome, and isolated CAKUT without ocular anomalies; absence of iris colobomas and presence of characteristic optic disc changes support RCS.[33][36][41][42]

### 10.4 Screening

Population‑level newborn screening is not implemented.  
Cascade screening (testing at‑risk relatives for a known PAX2 variant) and ophthalmologic/renal surveillance in families are recommended.[13][17][15]  

Suggested NCIT (NCI Thesaurus) intervention terms:

- *Genetic Testing* (NCIT:C14432).  
- *Renal Ultrasound* (NCIT:C17772).  
- *Ophthalmologic Examination* (NCIT:C17895).  

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

No large survival datasets exist, but mortality risk is primarily driven by progression to ESRD and its complications.[33][36][35]  
Dialysis and transplantation outcomes are comparable to other pediatric ESRD etiologies; RCS itself does not appear to confer unusual transplant risk.[33][36]

### 11.2 Morbidity and function

Morbidity arises from:[33][36][38][35]

- CKD/ESRD (fatigue, growth impairment, cardiovascular risk).  
- Visual impairment (loss of driving eligibility, educational impact, risk of retinal detachment).  
- Hearing and CNS anomalies in some patients.

Formal QOL measures (EQ‑5D, SF‑36) have not been systematically reported in RCS, but clinical narratives emphasize substantial impact in individuals with severe renal and ocular disease.[33][36][35]

### 11.3 Disease course and complications

Complications include:[33][36][44][38]

- ESRD requiring dialysis or transplant (reported in up to about one‑third of individuals in some series).[38][33][36]  
- Retinal detachment due to colobomatous anomalies.[33][36][44]  
- Recurrent urinary tract infections and scarring in VUR.[43][54][75]  
- Cardiovascular disease secondary to CKD and hypertension.[33][36]

Prognosis is worse in individuals with truncating PAX2 variants affecting the paired domain or causing protein‑truncating loss of function; a 2025 genotype‑phenotype study found that protein loss‑of‑function (pLoF) variants were associated with more severe kidney and ocular outcomes.[28][19][22]

Direct quote (human genotype–phenotype, 2025, PMID:39994403):  
> “pLoF variants in PAX2 were associated with worse kidney and ocular outcomes.”[28]

---

## 12. Treatment

### 12.1 Pharmacotherapy and CKD management

There is no PAX2‑specific pharmacologic therapy; treatment follows standard CKD and ESRD guidelines.[33][36][29]

Main strategies:[33][36][29][38]

- Blood pressure control (often with ACE inhibitors or ARBs) to reduce proteinuria and slow CKD progression.  
- Management of proteinuria and hyperfiltration injury.  
- Correction of anemia, bone/mineral disorders, and metabolic derangements associated with CKD.  
- Renal replacement therapy (hemodialysis, peritoneal dialysis) and kidney transplantation for ESRD.

Suggested NCIT terms:

- *Antihypertensive Therapy* (NCIT:C230).  
- *Renal Dialysis* (NCIT:C16888).  
- *Kidney Transplantation* (NCIT:C15273).

Pharmacogenomic data specific to PAX2‑related CKD are not available; drug response is managed according to general CKD pharmacogenomics.[33][36]

### 12.2 Surgical and interventional management

- Surgical correction of high‑grade vesicoureteral reflux when indicated.[43][54]  
- Ophthalmologic interventions (e.g., retinal detachment repair, cataract surgery) in patients with ocular complications.[33][36][44]  

NCIT terms:

- *Surgical Repair of Vesicoureteral Reflux* (NCIT:C51880 – related concept).  
- *Ophthalmic Surgery* (NCIT:C50439).

### 12.3 Supportive and rehabilitative care

- Visual rehabilitation (low‑vision aids, educational adaptations).[33][36]  
- Hearing aids for high‑frequency hearing loss.[33][39][43]  
- Nephrology and ophthalmology follow‑up, psychosocial support.

NCIT: *Supportive Care* (NCIT:C16088), *Rehabilitation* (NCIT:C15273 – contextual).

### 12.4 Experimental and advanced therapeutics

Experimental work includes in vitro **CRISPR‑based correction of PAX2 mutations** in podocytes, which restored podocyte resilience in models.[70]  
No gene therapy, RNA‑based therapy, or in vivo CRISPR trials targeting PAX2‑related disorder are yet in clinical use (as of 2025–2026 literature).  
These preclinical findings suggest future potential for precision therapies but remain investigational.[70][65][62]

---

## 13. Prevention

### 13.1 Primary prevention

Primary prevention of RCS is feasible only through **reproductive genetic interventions** (PGT, selective prenatal diagnosis) in families with known PAX2 variants.[13][15][17]  
No vaccines or environmental interventions prevent the underlying genetic lesion.

### 13.2 Secondary and tertiary prevention

Secondary prevention focuses on early detection and treatment of CKD and VUR:[33][36][29][38]

- Regular monitoring of renal function and blood pressure in PAX2 mutation carriers.  
- Early treatment of hypertension and proteinuria.  
- Prompt management of VUR and urinary tract infections to limit scarring.

Tertiary prevention centers on CKD management to avoid ESRD and cardiovascular complications.[33][36][35]

### 13.3 Genetic counseling and public health

GeneReviews recommends offering molecular testing to at‑risk relatives when a familial PAX2 variant is known and providing genetic counseling regarding 50% recurrence risk in autosomal dominant inheritance.[13][17][15]  

Direct quote (GeneReviews):  
> “Evaluation of relatives at risk: Offer molecular genetic testing if a PAX2 pathogenic variant has been identified in an affected family member. … Prenatal testing and preimplantation genetic testing are possible if the pathogenic PAX2 pathogenic variant has been identified in the family.”[13]

NCIT terms: *Genetic Counseling* (NCIT:C94406), *Prenatal Diagnosis* (NCIT:C17226), *Preimplantation Genetic Testing* (NCIT:C128244).

---

## 14. Other Species / Natural Disease

Natural RCS‑like disease in companion animals has not been well documented, although PAX2 orthologs exist across vertebrates.[64][74]  

Experimental work in non‑human species:

- Mouse: Pax2 and Pax8 double mutants (kidney agenesis), Pax2 missense models recapitulating papillorenal hypoplasia.[64][73][61][67][69][72][65][66]  
- Fish (goldfish): Pax2 in optic nerve development as a model of continuous growth and glial patterning.[74]  

These represent **model systems**, not naturally occurring clinical disease in veterinary practice.  
Comparative biology supports evolutionary conservation of PAX2 roles in nephric and optic nerve development across vertebrates.[64][74][69][71]

---

## 15. Model Organisms

### 15.1 Model types and systems

**Mouse models (mammalian)** – principal models for RCS mechanisms:[69][64][73][61][67][71][65][72][66]

- Pax2–/– (germline null) mice: complete renal and ureteric agenesis; lack kidneys, ureters, genital tracts.[69][66]  
- Pax2+/– heterozygotes: renal hypoplasia, vesicoureteral reflux, reduced nephron number.[69][62][72]  
- Pax2+/–;Pax8+/– compound heterozygotes: severely hypodysplastic kidneys with reduced ureter tips and nephron number and decreased Lim1 expression.[67][64]  
- Pax2 A220G/A220G missense model: hypomorphic allele causing small kidneys, reduced glomerular formation, cystic changes.[73][61]  
- Conditional Pax2 ablation in nephron progenitors: failure of nephron differentiation and transdifferentiation of progenitors into interstitial lineages.[65]  
- Pax2 optic nerve models: defective optic fissure closure, altered axonal pathways, aberrant glial patterning.[71][68]

### 15.2 Phenotype recapitulation

Mouse Pax2 models recapitulate key human RCS features:[69][64][73][61][71]

- Renal hypoplasia and CAKUT (kidney agenesis in null models).  
- Decreased nephron number and hydronephrosis/hydroureter (as in human CAKUT).[72][73]  
- Optic nerve anomalies and closure defects mimicking optic nerve coloboma.[71]  

Limitations include more extreme phenotypes in null mice than typical human heterozygous mutations and differences in ocular anatomy between mice and humans.[69][64][71][73]

### 15.3 Research applications

Pax2 models have been used to:[64][69][72][65][73][70][61][71][68]

- Map nephron progenitor lineage decisions and branching morphogenesis.  
- Investigate apoptosis and nephron endowment in CAKUT.  
- Dissect podocyte and parietal epithelial cell injury and regeneration pathways.  
- Explore optic nerve development, glial differentiation, and axon guidance.  
- Identify candidate PAX2‑regulated genes via transcriptomics.[62]

These models underpin current mechanistic understanding of RCS and PAX2‑related disorders and help identify potential therapeutic targets.

---

### Ontology summary (suggested)

- Disease: MONDO:0007352 (Renal Coloboma Syndrome); DOID:0090006.  
- Gene: PAX2 (HGNC:8619).  
- Key HPO terms: HP:0000089 (Renal hypodysplasia), HP:0000112 (CKD), HP:0000589 (Optic disc coloboma), HP:0000822 (Hypertension), HP:0000093 (Proteinuria), HP:0000407 (Sensorineural hearing impairment).  
- Key GO terms: GO:0001822 (Kidney development), GO:0072043 (Nephron development), GO:0048754 (Branching morphogenesis of an epithelial tube), GO:0008038 (Optic nerve development), GO:0010001 (Glial cell differentiation).  
- CL terms: CL:0002518 (Nephron progenitor cell), CL:0000653 (Podocyte), CL:0000127 (Astrocyte).  
- UBERON:0002113 (Kidney), UBERON:0001626 (Optic nerve), UBERON:0005052 (Metanephros).  
- NCIT treatment/diagnostic concepts: C14432 (Genetic Testing), C16888 (Renal Dialysis), C15273 (Kidney Transplantation), C94406 (Genetic Counseling).

This body of evidence, spanning human clinical studies (case series, cohort analyses, GeneReviews), model organism work (mouse Pax2/Pax8 genetics), and in vitro functional experiments (podocyte and parietal epithelial cell models), provides a coherent framework for describing RCS/PAX2‑related disorder within a disease knowledge base.[16][20][22][23][24][25][28][33][36][63][69][64][73][70]

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 2 |
| Terms whose name was checked | 56 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 29 |
| Terms whose name is worth a second look | 13 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000128` (1 mention) - the report calls it "Small kidney"; HP calls it **Renal potassium wasting**
- `HP:0000112` (2 mentions) - the report calls it "Chronic kidney disease", "HPO: *Chronic kidney disease", "CKD"; HP calls it **Nephropathy**
- `HP:0000585` (1 mention) - the report calls it "Optic disc dysplasia"; HP calls it **Band keratopathy**
- `HP:0001103` (1 mention) - the report calls it "Retinal coloboma", "HPO: *Retinal coloboma"; HP calls it **Abnormal macular morphology**
- `GO:0072043` (2 mentions) - the report calls it "nephron development", "Nephron development"; GO calls it **regulation of pre-tubular aggregate formation by cell-cell signaling**
- `GO:0030839` (1 mention) - the report calls it "podocyte differentiation"; GO calls it **regulation of intermediate filament polymerization**
- `GO:0036052` (1 mention) - the report calls it "glomerular filtration barrier maintenance"; GO calls it **protein localization to uropod**
- `GO:0008038` (2 mentions) - the report calls it "optic nerve development", "Optic nerve development"; GO calls it **neuron recognition**
- `CL:0002518` (2 mentions) - the report calls it "nephron progenitor cell", "Kidney: *nephron progenitor cell", "Nephron progenitor cell"; CL calls it **kidney epithelial cell**
- `CL:0002511` (1 mention) - the report calls it "parietal epithelial cell"; CL calls it **CD11b-low, CD103-negative, langerin-negative lymph node dendritic cell**
- `CL:0002066` (1 mention) - the report calls it "renal tubular epithelial cell"; CL calls it **Feyrter cell**
- `UBERON:0005052` (2 mentions) - the report calls it "metanephros", "Metanephros"; UBERON calls it **gizzard**
- `UBERON:0001626` (3 mentions) - the report calls it "optic nerve", "UBERON: *optic nerve", "Eyes: optic nerve", "Optic nerve"; UBERON calls it **left coronary artery**
- `GO:0072033` (1 mention) - the report calls it "nephron"; GO calls it **renal vesicle formation**
- `GO:0098853` (1 mention) - the report calls it "podocyte foot process"; GO calls it **endoplasmic reticulum-vacuole membrane contact site**
- `HP:0008672` (1 mention) - the report calls it "Bilateral renal hypoplasia"; HP calls it **Calcium oxalate nephrolithiasis**
- `HP:0001123` (1 mention) - the report calls it "Bilateral optic disc coloboma"; HP calls it **Visual field defect**
- `NCIT:C14432` (1 mention) - the report calls it "Genetic Testing"; NCIT calls it **Swiss Strains**
- `NCIT:C17772` (1 mention) - the report calls it "Renal Ultrasound"; NCIT calls it **CD44 Antigen**
- `NCIT:C17895` (1 mention) - the report calls it "Ophthalmologic Examination"; NCIT calls it **Cell Lineage**
- `NCIT:C230` (1 mention) - the report calls it "Antihypertensive Therapy"; NCIT calls it **Amikacin Sulfate**
- `NCIT:C16888` (1 mention) - the report calls it "Renal Dialysis"; NCIT calls it **Myelogram**
- `NCIT:C15273` (2 mentions) - the report calls it "Kidney Transplantation", "contextual"; NCIT calls it **Longitudinal Study**
- `NCIT:C51880` (1 mention) - the report calls it "related concept"; NCIT calls it **Study Coordinator**
- `NCIT:C50439` (1 mention) - the report calls it "Ophthalmic Surgery"; NCIT calls it **Joint Disorder**
- `NCIT:C16088` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Extraordinary Opportunities for Investment**
- `NCIT:C94406` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Autologous Bone Marrow**
- `NCIT:C17226` (1 mention) - the report calls it "Prenatal Diagnosis"; NCIT calls it **Tyrosinase**
- `NCIT:C128244` (1 mention) - the report calls it "Preimplantation Genetic Testing"; NCIT calls it **Vulvar Small Cell Neuroendocrine Carcinoma**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001388` (obsolete Joint laxity) (1 mention) - replaced by `HP:0001382`
- `NCIT:C14432` (Swiss Strains) (1 mention)
- `NCIT:C50439` (Joint Disorder) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000089` (2 mentions) - the report calls it "Renal hypodysplasia", "HPO term: *Renal hypodysplasia"; HP calls it **Renal hypoplasia**
- `HP:0000076` (1 mention) - the report calls it "Vesicoureteral reflux", "HPO: *Vesicoureteral reflux"; HP calls it **Vesicoureteral reflux**
- `HP:0000093` (2 mentions) - the report calls it "Proteinuria", "HPO: *Proteinuria"; HP calls it **Proteinuria**
- `HP:0000097` (1 mention) - the report calls it "Focal segmental glomerulosclerosis", "HPO: *Focal segmental glomerulosclerosis"; HP calls it **Focal segmental glomerulosclerosis**
- `HP:0000589` (2 mentions) - the report calls it "Optic disc coloboma", "HPO: *Optic disc coloboma"; HP calls it **Coloboma**, and lists "Ocular coloboma" among its other names
- `HP:0007754` (1 mention) - the report calls it "Pigmentary macular dystrophy"; HP calls it **Macular dystrophy**
- `HP:0000482` (1 mention) - the report calls it "Small cornea", "HPO: *Small cornea"; HP calls it **Microcornea**
- `HP:0001388` (1 mention) - the report calls it "Joint laxity / loose joints"; HP calls it **obsolete Joint laxity**
- `HP:0000083` (1 mention) - the report calls it "Genital anomalies"; HP calls it **Renal insufficiency**, and lists "Renal failure" among its other names
- `GO:0042981` (1 mention) - the report calls it "regulation of apoptosis"; GO calls it **regulation of apoptotic process**, and lists "regulation of apoptosis" among its other names
- `CL:0000127` (2 mentions) - the report calls it "astrocyte", "Optic nerve: *astrocyte", "Astrocyte"; CL calls it **astrocyte**
- `UBERON:0002113` (3 mentions) - the report calls it "kidney", "UBERON: *kidney", "Kidneys", "Kidney"; UBERON calls it **kidney**
- `GO:0005634` (2 mentions) - the report calls it "nucleus", "GO Cellular Component: *nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000089` - called "Renal hypodysplasia", "HPO term: *Renal hypodysplasia"
- `HP:0000112` - called "Chronic kidney disease", "HPO: *Chronic kidney disease", "CKD"
- `HP:0000076` - called "Vesicoureteral reflux", "HPO: *Vesicoureteral reflux"
- `HP:0000093` - called "Proteinuria", "HPO: *Proteinuria"
- `HP:0000097` - called "Focal segmental glomerulosclerosis", "HPO: *Focal segmental glomerulosclerosis"
- `HP:0000589` - called "Optic disc coloboma", "HPO: *Optic disc coloboma"
- `HP:0001103` - called "Retinal coloboma", "HPO: *Retinal coloboma"
- `HP:0000482` - called "Small cornea", "HPO: *Small cornea"
- `GO:0001822` - called "kidney development", "Kidney development"
- `GO:0072043` - called "nephron development", "Nephron development"
- `GO:0048754` - called "branching morphogenesis of an epithelial tube", "Branching morphogenesis of an epithelial tube"
- `GO:0008038` - called "optic nerve development", "Optic nerve development"
- `GO:0010001` - called "glial cell differentiation", "Glial cell differentiation"
- `CL:0002518` - called "nephron progenitor cell", "Kidney: *nephron progenitor cell", "Nephron progenitor cell"
- `CL:0000653` - called "podocyte", "Podocyte"
- `CL:0000127` - called "astrocyte", "Optic nerve: *astrocyte", "Astrocyte"
- `UBERON:0002113` - called "kidney", "UBERON: *kidney", "Kidneys", "Kidney"
- `UBERON:0005052` - called "metanephros", "Metanephros"
- `UBERON:0001626` - called "optic nerve", "UBERON: *optic nerve", "Eyes: optic nerve", "Optic nerve"
- `GO:0005634` - called "nucleus", "GO Cellular Component: *nucleus"
- `NCIT:C15273` - called "Kidney Transplantation", "contextual"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.