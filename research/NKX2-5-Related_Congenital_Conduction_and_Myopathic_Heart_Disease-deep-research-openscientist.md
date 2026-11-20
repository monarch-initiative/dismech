---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T04:39:42.717804'
end_time: '2026-11-05T05:02:05.504339'
duration_seconds: 1342.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease
  mondo_id: MONDO:0800441
  category: Mendelian
  causal_genes: NKX2-5
  omim_id: not recorded
  synonyms: NKX2-5-related congenital heart disease; atrial septal defect with atrioventricular
    conduction defects; CSX-related congenital heart disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 15
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 0
  labels_mismatched: 17
  mislabelled_terms:
  - term_id: MONDO:0800441
    reported_labels:
    - MONDO
    ontology_label: NKX2.5-related congenital, conduction and myopathic heart disease
  - term_id: HP:0001684
    reported_labels:
    - Physical malformation
    ontology_label: Secundum atrial septal defect
  - term_id: HP:0001678
    reported_labels:
    - Clinical sign (ECG)
    ontology_label: Atrioventricular block
  - term_id: HP:0011705
    reported_labels:
    - Lab/ECG abnormality
    ontology_label: First degree atrioventricular block
  - term_id: HP:0011706
    reported_labels:
    - Lab/ECG abnormality
    ontology_label: Second degree atrioventricular block
  - term_id: HP:0001709
    reported_labels:
    - Lab/ECG abnormality
    ontology_label: Third degree atrioventricular block
  - term_id: HP:0001629
    reported_labels:
    - Physical malformation
    ontology_label: Ventricular septal defect
  - term_id: HP:0001636
    reported_labels:
    - Physical malformation
    ontology_label: Tetralogy of Fallot
  - term_id: HP:0002356
    reported_labels:
    - Physical malformation
    ontology_label: Writer's cramp
  - term_id: HP:0001702
    reported_labels:
    - Physical malformation
    ontology_label: Abnormal tricuspid valve morphology
  - term_id: HP:0030682
    reported_labels:
    - Physical/structural
    ontology_label: Left ventricular noncompaction
  - term_id: HP:0001644
    reported_labels:
    - Clinical sign
    ontology_label: Dilated cardiomyopathy
  - term_id: HP:0001645
    reported_labels:
    - Outcome
    ontology_label: Sudden cardiac death
  - term_id: NCIT:C51658
    reported_labels:
    - Cardiac surgery
    ontology_label: Gastric Antrectomy
  - term_id: NCIT:C50114
    reported_labels:
    - Pacemaker
    ontology_label: Power Module Device
  - term_id: NCIT:C62226
    reported_labels:
    - Implantable defibrillator
    ontology_label: Juvenile Lesion
  - term_id: NCIT:C577
    reported_labels:
    - Anticoagulant therapy
    ontology_label: Industrial Waste
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: NKX2-5-Related_Congenital_Conduction_and_Myopathic_Heart_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: NKX2-5-Related_Congenital_Conduction_and_Myopathic_Heart_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease
- **MONDO ID:** MONDO:0800441 (if available)
- **Causal gene(s):** NKX2-5
- **OMIM:** not recorded
- **Synonyms:** NKX2-5-related congenital heart disease; atrial septal defect with atrioventricular conduction defects; CSX-related congenital heart disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease** covering all of the
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

# NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease — Comprehensive Research Report

**Disease:** NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease
**MONDO ID:** MONDO:0800441 · **OMIM:** #108900 (ASD7, atrial septal defect 7 with or without atrioventricular conduction defects)
**Causal gene:** **NKX2-5** (NK2 homeobox 5; formerly *CSX*, cardiac-specific homeobox; HGNC:2488; chromosome 5q35.1)
**Category:** Mendelian, autosomal dominant

> **Causal gene stated up front:** This report concerns the disease caused by heterozygous, predominantly loss-of-function variants in **NKX2-5**, the homeodomain cardiac transcription factor located at chromosome **5q35.1** (the vertebrate homolog of *Drosophila tinman*). The hallmark combination is **secundum atrial septal defect (ASD) with progressive atrioventricular (AV) conduction block**, together with a broader spectrum of structural malformations and a myopathic/conduction-cell component. All molecular claims below refer to NKX2-5, not to similarly named genes.

---

## Summary

NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease is an autosomal-dominant cardiac disorder caused by heterozygous, predominantly loss-of-function (haploinsufficient) variants in **NKX2-5**, the NK2-class homeodomain cardiac transcription factor located at chromosome 5q35.1. NKX2-5 is the vertebrate ortholog of the *Drosophila* cardiac selector gene *tinman* and is one of the earliest and most essential regulators of cardiac development. The disease was first defined genetically by Schott et al. (1998), who mapped a dominant locus for cardiac malformations plus atrioventricular (AV) conduction abnormalities to 5q35 and identified disease-causing NKX2-5 mutations, two of which impair DNA binding and thereby cause haploinsufficiency [PMID: 9651244].

The clinical syndrome unites three mechanistically linked manifestations. First, **structural congenital heart defects** — most characteristically **secundum atrial septal defect (ASD)**, but also ventricular septal defect (VSD), tetralogy of Fallot, double-outlet right ventricle, and Ebstein anomaly — arising from NKX2-5's role in cardiac looping and septation. Second, a **progressive atrioventricular conduction disease**: the AV node is hypoplastic from birth in a gene-dosage-dependent manner, then undergoes selective postnatal dropout of conduction cells, producing age-progressive AV block that was the primary cardiac manifestation in roughly a quarter of affected individuals in the landmark Benson et al. cohort [PMID: 10587520]. Third, a **myopathic branch** — trabecular/ventricular non-compaction and cardiomyopathy — driven in model systems by ectopic, high-level BMP10 expression in ventricular myocardium when NKX2-5 is lost [PMID: 15109497].

The mechanistic chain is well supported by a mouse allelic series. Homozygous-null embryos form a linear heart tube but fail to initiate looping morphogenesis and die at E9–10, lacking the ventricular marker MLC2V [PMID: 7628699]. Heterozygotes model human haploinsufficiency, with roughly half the normal number of conduction-system cells and a hypoplastic AV node [PMID: 15085192]. Ventricular-restricted conditional knockouts reproduce progressive complete heart block together with trabecular overgrowth via ectopic BMP10 [PMID: 15109497]. Management is phenotype-directed — surgical/device septal closure, permanent pacemaker/ICD for conduction disease and sudden-death risk, and heart-failure therapy — with no gene-specific cure currently available.

---

## Section 1 — Disease Information and Key Identifiers

| Identifier type | Value |
|---|---|
| Disease name | NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease |
| MONDO | MONDO:0800441 |
| OMIM | #108900 (ASD7, atrial septal defect 7 with or without AV conduction defects) |
| Causal gene | NKX2-5 (HGNC:2488; NCBI Gene 1482; UniProt P52952) |
| Cytogenetic locus | 5q35.1 |
| Protein | NK2 homeobox 5 / cardiac-specific homeobox (CSX) |
| Inheritance | Autosomal dominant |

**Synonyms / alternative names:** NKX2-5-related congenital heart disease; atrial septal defect with atrioventricular conduction defects; CSX-related congenital heart disease; cardiac homeobox (CSX) disease. The gene has historically been written NKX2.5, NKX2E, and CSX.

**Source of information:** The content of this report is derived from aggregated disease-level resources — OMIM, MONDO, and primary peer-reviewed human genetic/clinical studies and model-organism literature — rather than from individual-patient electronic health records.

---

## Section 2 — Etiology

**Primary cause (genetic):** Heterozygous pathogenic variants in NKX2-5. The predominant molecular mechanism is **haploinsufficiency**: variants that reduce functional NKX2-5 dosage (truncating variants, and missense variants that impair DNA binding) are sufficient to cause disease [PMID: 9651244]. Some variants may additionally act via dominant-negative effects or reduced transactivation.

**Genetic risk factors:** The causal NKX2-5 variant is itself the principal genetic determinant. Partner cardiac transcription factors (GATA4, TBX5, TBX20, GATA6) that function combinatorially with NKX2-5 cause overlapping CHD phenotypes when mutated and are candidate modifiers.

**Environmental risk factors:** No specific environmental trigger is established for NKX2-5-related disease. General CHD risk factors (maternal diabetes, teratogen exposure, folate status) may plausibly modify expressivity but are not documented as disease-specific for this entity.

**Protective factors:** None established genetically or environmentally specific to this disease.

**Gene–environment interactions:** Variable expressivity within families carrying the same variant (Benson et al.) implies the existence of genetic modifiers and/or environmental contributors, but none are specifically characterized [PMID: 10587520].

---

## Section 3 — Phenotypes

Benson et al. (2000) documented across mutation carriers: AV block (primary manifestation in ~25%), secundum atrial septal defect, ventricular septal defect, tetralogy of Fallot/double-outlet right ventricle (3 individuals), and Ebstein anomaly/tricuspid valve abnormalities [PMID: 10587520]. Schott et al. emphasized that NKX2-5 is important both for septation during cardiac morphogenesis and for maturation and maintenance of AV node function throughout life — i.e., a lifelong, progressive course [PMID: 9651244].

> "Ventricular septal defect was associated with tetralogy of Fallot or double-outlet right ventricle in 3 individuals. Ebstein's anomaly and other tricuspid valve abnormalities were also present." — [PMID: 10587520]

> "NKX2-5 is important for regulation of septation during cardiac morphogenesis and for maturation and maintenance of atrioventricular node function throughout life." — [PMID: 9651244]

**Suggested HPO annotations:**

| Phenotype | Phenotype type | HPO term | Frequency / onset / course |
|---|---|---|---|
| Secundum atrial septal defect | Physical malformation | HP:0001684 | Most common structural lesion; congenital |
| Atrioventricular block | Clinical sign (ECG) | HP:0001678 | Primary in ~25%; progressive |
| First-degree AV block | Lab/ECG abnormality | HP:0011705 | Childhood onset; progresses |
| Second-degree AV block | Lab/ECG abnormality | HP:0011706 | Intermediate progression |
| Third-degree (complete) AV block | Lab/ECG abnormality | HP:0001709 | Adult; sudden-death risk |
| Ventricular septal defect | Physical malformation | HP:0001629 | Frequent; congenital |
| Tetralogy of Fallot | Physical malformation | HP:0001636 | Subset; conotruncal |
| Double-outlet right ventricle | Physical malformation | HP:0002356 | Rare |
| Ebstein anomaly | Physical malformation | HP:0010316 | Reported |
| Tricuspid valve abnormality | Physical malformation | HP:0001702 | Reported |
| Left ventricular noncompaction | Physical/structural | HP:0030682 | Myopathic branch |
| Dilated cardiomyopathy | Clinical sign | HP:0001644 | Myopathic branch |
| Sudden cardiac death | Outcome | HP:0001645 | Conduction-related risk |

**Quality of life impact:** Pacemaker dependence, activity restriction from heart failure/arrhythmia, surgical burden, and lifelong surveillance affect daily functioning; sudden-death risk imposes substantial psychological burden on patients and families.

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** NKX2-5 (HGNC:2488; OMIM gene 600584). **Disease OMIM:** #108900.

**Pathogenic variants:** Reported variants include missense (notably within/affecting the homeodomain, impairing DNA binding), nonsense, frameshift, and splice-site changes. Schott et al. identified 3 mutations (2 DNA-binding-impairing) [PMID: 9651244]; Benson et al. added 7 novel mutations across 26 probands [PMID: 10587520]. Variant classification follows ACMG/AMP criteria in ClinVar (pathogenic/likely pathogenic for established LoF alleles).

**Allele frequency:** Pathogenic NKX2-5 variants are rare and largely family-private; they are essentially absent/ultra-rare in gnomAD, consistent with a highly constrained developmental transcription factor.

**Somatic vs. germline:** Germline (congenital disorder). De novo and inherited dominant variants both occur.

**Functional consequences:** Predominantly **loss of function / haploinsufficiency**; impaired DNA binding is a demonstrated mechanism [PMID: 9651244]. Dominant-negative effects have been proposed for some variants.

**Modifier genes:** GATA4, TBX5, TBX20, GATA6 (combinatorial partners) are candidate modifiers; variable expressivity implies modifiers but none are definitively mapped.

**Epigenetic / chromosomal:** No disease-specific methylation signature is established. Large 5q35 deletions/structural changes involving NKX2-5 can produce the phenotype and are detectable by chromosomal microarray.

---

## Section 5 — Environmental Information

No specific environmental factors, lifestyle factors, or infectious agents are established as causes or triggers of NKX2-5-related disease. The disorder is fundamentally genetic/developmental. General CHD environmental modifiers (maternal metabolic state, teratogens) are not documented as disease-specific for this entity. **Not applicable / not established** for this Mendelian condition.

---

## Section 6 — Mechanism / Pathophysiology

**Ordered causal chain:**

1. A heterozygous loss-of-function NKX2-5 variant (nonsense, frameshift, splice, or DNA-binding-impairing missense) **leads to** reduced functional NKX2-5 protein — i.e., haploinsufficiency (demonstrated for DNA-binding-impairing alleles; [PMID: 9651244]).
2. Reduced NKX2-5 dosage **results in** diminished combinatorial transcriptional activation (with GATA4/TBX5/GATA6) of chamber- and conduction-specific target genes (inferred from network studies; target genes shown in [PMID: 15109497, 15085192]).
3. **Branch A — Structural:** Impaired transcriptional program **leads to** failed/abnormal cardiac looping and septation during embryogenesis → **results in** secundum ASD, VSD, conotruncal defects (tetralogy of Fallot, DORV), and Ebstein anomaly (looping requirement demonstrated in null mice [PMID: 7628699]; human spectrum [PMID: 10587520]).
4. **Branch B — Conduction:** Reduced dosage **leads to** a hypoplastic AV node at birth (dosage-dependent cell number) → **results in** selective postnatal dropout/failed retention of conduction cells → **leads to** progressive first- → second- → third-degree AV block and sudden-death risk ([PMID: 15085192, 15109497]).
5. **Branch C — Myopathic:** Loss of NKX2-5 repression **results in** ectopic high-level BMP10 in ventricular myocardium → **leads to** trabecular overgrowth / ventricular non-compaction and cardiomyopathy (demonstrated in conditional KO; BMP10 necessary and sufficient for major ventricular muscle defects [PMID: 15109497]).

```
                    NKX2-5 LoF variant (heterozygous)
                                 │
                       Haploinsufficiency
                                 │
             Reduced combinatorial activation of
          chamber/conduction gene programs (GATA4/TBX5)
                                 │
        ┌────────────────────────┼─────────────────────────┐
        ▼                        ▼                          ▼
  [A] Looping/septation    [B] AV-node hypoplasia      [C] Loss of BMP10
      failure                  + cell dropout              repression
        │                        │                          │
  Secundum ASD, VSD,       Progressive AV block        Ectopic BMP10 →
  TOF, DORV, Ebstein       (1°→2°→3°), SCD risk        noncompaction/CMP
```

> "looping morphogenesis, a critical determinant of heart form, was not initiated at the linear heart tube stage" — [PMID: 7628699]

> "At birth, mutant mice display a hypoplastic atrioventricular (AV) node and then develop selective dropout of these conduction cells." — [PMID: 15109497]

> "Transcriptional profiling uncovered the aberrant expression of a unique panel of atrial and conduction system-restricted target genes, as well as the ectopic, high level BMP-10 expression in the adult ventricular myocardium." — [PMID: 15109497]

**Molecular / cellular detail:**
- **Molecular pathways:** NKX2-5 is a homeodomain transcription-factor node in the core cardiac gene-regulatory network; downstream effectors include GJA5/connexin40 (gap junction), BMP10 signaling, and chamber myocyte identity genes. Jay et al. identified connexin40 as a putative Nkx2-5 target [PMID: 15085192].
- **GO biological processes:** cardiac conduction (GO:0061337), heart looping (GO:0001947), cardiac septum morphogenesis (GO:0003279), regulation of transcription by RNA polymerase II (GO:0006357), cardiac muscle tissue development (GO:0048738).
- **Cell types (CL):** nodal/AV-node myocyte (CL:0002087), cardiac Purkinje fiber cell (CL:0000166), ventricular cardiomyocyte (CL:0002131), atrial cardiomyocyte (CL:0002129), precardiac mesoderm.
- **Subcellular (GO CC):** nucleus (GO:0005634, site of transcription-factor action), gap junction / connexin40 (GO:0005922).
- **Protein dysfunction:** predominantly loss of function via impaired DNA binding (homeodomain mutations) or protein truncation; haploinsufficiency is the dominant paradigm [PMID: 9651244].

---

## Section 7 — Anatomical Structures Affected

- **Organ:** Heart (UBERON:0000948) — primary. Secondary systemic effects from heart failure and conduction disease affect the cardiovascular system (UBERON:0004535).
- **Structures:** interatrial/atrial septum (UBERON:0002085) — secundum ASD; interventricular septum (UBERON:0002094) — VSD; atrioventricular node (UBERON:0002351) — conduction disease; cardiac conduction system (UBERON:0004146) and His–Purkinje system; cardiac ventricle (UBERON:0002082) and trabecular myocardium — non-compaction; tricuspid valve — Ebstein anomaly; cardiac outflow tract (UBERON:0004145) — conotruncal defects.
- **Tissue/cell level:** cardiac muscle (myocardium), specialized conduction myocytes, nodal myocytes.
- **Subcellular:** nucleus (transcription-factor action); gap junctions (connexin40).
- **Lateralization:** The heart is a midline organ; conotruncal/looping phenotypes reflect disrupted left–right morphogenesis rather than limb-type lateralization.

---

## Section 8 — Temporal Development

- **Onset:** Congenital for structural defects (present at birth, often detected in infancy/childhood). Conduction disease is congenital-to-progressive — the AV node is hypoplastic from birth, but block severity worsens with age.
- **Progression:** The conduction phenotype is characteristically **progressive**, evolving from first-degree AV block in childhood to higher-grade/complete block in adulthood, reflecting ongoing conduction-cell dropout [PMID: 15085192, 15109497]. Structural defects are static once formed but may require intervention; the myopathic phenotype can emerge or progress over time.
- **Critical period:** Cardiac looping and septation (~embryonic weeks 3–8 in humans; E8–E10.5 in mouse) is the window in which structural defects originate.
- **Course:** Chronic, lifelong, requiring continued surveillance even after structural repair.

---

## Section 9 — Inheritance and Population

- **Inheritance:** Autosomal dominant (OMIM #108900).
- **Penetrance / expressivity:** Incomplete penetrance and markedly variable expressivity — family members with the same variant may have isolated AV block, isolated ASD, complex CHD, or be minimally affected [PMID: 10587520].
- **Epidemiology:** CHD overall affects ~0.8% of live births; NKX2-5 variants account for an estimated ~1–4% of nonsyndromic CHD (established-knowledge estimate). Benson et al.: 7 novel mutations across 26 probands; authors conclude NKX2-5 may account for a clinically significant portion of tetralogy of Fallot and idiopathic AV block [PMID: 10587520].
- **Sex ratio:** No strong sex bias (autosomal).
- **Founder effects / consanguinity:** Not prominent; most variants are family-private. Not a repeat-expansion disorder, so genetic anticipation is not expected. Germline mosaicism is possible but not a documented recurrent feature.

> "Mutations in human NKX2.5 cause a variety of cardiac anomalies and may account for a clinically significant portion of tetralogy of Fallot and idiopathic AV block." — [PMID: 10587520]

> "The coinheritance of NKX2.5 mutations with various congenital heart defects suggests that this transcription factor contributes to diverse cardiac developmental pathways." — [PMID: 10587520]

---

## Section 10 — Diagnostics

- **Electrophysiology:** 12-lead ECG and ambulatory (Holter) monitoring are central for detecting and staging AV block (PR-interval prolongation → higher-grade block); serial surveillance is essential given progression.
- **Imaging:** Transthoracic echocardiography detects secundum ASD, VSD, conotruncal anomalies, Ebstein anomaly, and ventricular non-compaction; cardiac MRI quantifies non-compaction and ventricular function.
- **Genetic testing:** Single-gene NKX2-5 sequencing, multigene congenital-heart/cardiomyopathy/conduction panels, or whole-exome/genome sequencing. Recommended for probands with CHD plus conduction disease and for cascade screening of relatives. Chromosomal microarray detects larger 5q35 structural changes.
- **Clinical criteria / differential diagnosis:** Secundum ASD (or other CHD) with progressive AV block is highly suggestive. Differentials include GATA4-, TBX5- (Holt–Oram, distinguished by radial/upper-limb anomalies), and TBX20-related CHD; isolated idiopathic AV block (Lev–Lenègre); and Lamin A/C conduction disease.
- **Screening:** Cascade genetic and clinical (ECG/echo) screening of at-risk relatives is the key secondary-prevention measure.

---

## Section 11 — Outcome / Prognosis

- **Mortality:** Driven chiefly by high-grade AV block (syncope, sudden cardiac death) and by complications of structural defects and cardiomyopathy. Sudden death has been reported even after structural repair, underscoring the need for conduction surveillance.
- **Morbidity:** Heart failure (from cardiomyopathy/non-compaction or unrepaired shunts), thromboembolic risk, pacemaker dependence.
- **Prognostic factors:** Degree/progression of AV block, presence of ventricular dysfunction/non-compaction, and complexity of the structural lesion. Timely pacemaker/ICD implantation and surgical repair substantially improve outcomes.
- **Recovery:** Structural defects are correctable; conduction disease is managed but not cured and tends to progress.

---

## Section 12 — Treatment

No gene-specific or curative therapy exists; management is phenotype-directed.

| Manifestation | Intervention | NCIT suggestion |
|---|---|---|
| Secundum ASD / VSD | Surgical or transcatheter device closure | Cardiac surgery (NCIT:C51658); septal closure |
| Conotruncal defects (TOF, DORV) | Corrective cardiac surgery | Cardiac surgical procedure |
| Progressive AV block | Permanent pacemaker implantation | Pacemaker (NCIT:C50114) |
| Sudden-death risk / ventricular dysfunction | Implantable cardioverter-defibrillator (ICD) | Implantable defibrillator (NCIT:C62226) |
| Heart failure / cardiomyopathy | Guideline-directed medical therapy (ACE inhibitors/ARBs, beta-blockers, diuretics) | Antihypertensive/cardiac agents |
| Thromboembolism risk (shunts/arrhythmia) | Anticoagulation | Anticoagulant therapy (NCIT:C577) |

- **Pharmacogenomics / advanced therapeutics:** No approved gene, cell, or RNA-based therapy. Gene-replacement/editing remains preclinical. No targeted small molecule exists for NKX2-5 disease.
- **Treatment strategy:** Lifelong multidisciplinary follow-up (congenital cardiology + electrophysiology), serial ECG/Holter and echo, with device therapy timed to conduction progression.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable in the classical sense (congenital genetic disorder); preconception genetic counseling and reproductive options (prenatal/preimplantation genetic testing) can prevent transmission.
- **Secondary prevention:** Cascade genetic and ECG/echocardiographic screening of first-degree relatives enables early detection of silent conduction disease and timely pacemaker placement — the single most impactful preventive measure given the progressive, sudden-death-prone conduction phenotype.
- **Tertiary prevention:** Device therapy (pacemaker/ICD), heart-failure management, and anticoagulation to prevent complications.
- **Counseling:** Autosomal-dominant genetic counseling with 50% transmission risk per pregnancy; emphasis on incomplete penetrance and variable expressivity.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of orthologs:** Mouse (*Mus musculus*, NCBI Taxon 10090; *Nkx2-5*, NCBI Gene 18091); zebrafish (*Danio rerio*, Taxon 7955; *nkx2.5*); *Drosophila melanogaster* (Taxon 7227; *tinman*, the founding ortholog).
- **Evolutionary conservation:** Deep conservation of cardiac selector function — *tinman* mutants in *Drosophila* lack a heart, establishing the ancestral role. NKX2-5 expression in precardiac mesoderm and myocardium is conserved [PMID: 7628699].
- **Natural disease in companion animals/wildlife:** Not a prominently catalogued naturally occurring NKX2-5 disease in veterinary species (OMIA); conservation implies orthologous roles but spontaneous disease is not a documented entity. **Not applicable / not established** for veterinary natural disease.

---

## Section 15 — Model Organisms

- **Mouse (*Mus musculus*; *Nkx2-5*):** The definitive model system with a graded allelic series:
  - Homozygous knockout — embryonic-lethal (E9–10), failed cardiac looping, absent MLC2V [PMID: 7628699].
  - Heterozygotes — model human haploinsufficiency; hypoplastic AV node, ~50% reduction in conduction-system cellularity [PMID: 15085192].
  - Ventricular-restricted conditional knockout — progressive complete heart block, trabecular overgrowth / non-compaction via ectopic BMP10 [PMID: 15109497].
- **Phenotype recapitulation:** Strong and dosage-graded, faithfully reproducing both the conduction and myopathic branches of human disease.
- **Limitations:** Homozygous lethality prevents study of adult null hearts without conditional strategies; mouse–human differences in conduction-system anatomy.
- **Zebrafish (*nkx2.5*):** Useful for developmental and regenerative cardiac studies.
- **Resources:** MGI (mouse), ZFIN (zebrafish), FlyBase (*tinman*), Alliance of Genome Resources.

> "In Nkx2-5 haploinsufficiency, the conduction system has half the normal number of cells." — [PMID: 15085192]

> "The murine homeo box gene Nkx2-5 is expressed in precardiac mesoderm and in the myocardium of embryonic and fetal hearts." — [PMID: 7628699]

---

## Key Findings (consolidated with evidence)

### Finding 1 — NKX2-5 haploinsufficiency causes autosomal-dominant CHD with secundum ASD and progressive AV conduction block
Schott et al. (1998) mapped a dominant locus for cardiac malformations plus AV conduction abnormalities to 5q35 (NKX2-5) and identified 3 mutations, 2 impairing DNA binding → haploinsufficiency [PMID: 9651244]. Benson et al. (2000) found 7 novel mutations in 26 probands; AV block was the primary manifestation in ~25%, alongside ASD and VSD [PMID: 10587520].

> "A dominant disease locus associated with cardiac malformations and atrioventricular conduction abnormalities was mapped to chromosome 5q35, where NKX2-5, a Drosophila tinman homolog, is located." — [PMID: 9651244]
> "Two are predicted to impair binding of NKX2-5 to target DNA, resulting in haploinsufficiency" — [PMID: 9651244]
> "Associated phenotypes included AV block, which was the primary manifestation of cardiac disease in nearly a quarter of affected individuals, as well as atrial septal defect and ventricular septal defect." — [PMID: 10587520]

### Finding 2 — AV block arises from gene-dosage-dependent AV-node hypoplasia and progressive cell dropout
Jay et al. (2004): conduction-system cell number is directly proportional to Nkx2-5 dosage; heterozygotes have ~half the normal cells and lose a connexin40(−)/connexin45(+) AV-node population [PMID: 15085192]. Pashmforoush et al. (2004): hypoplastic AV node at birth followed by selective dropout causes progressive complete heart block [PMID: 15109497].

> "We show in KO mice that the number of cells in the cardiac conduction system is directly related to Nkx2-5 gene dosage." — [PMID: 15085192]
> "Postnatal conduction defects in Nkx2-5 mutation may result at least in part from a defect in the genetic program that governs the recruitment or retention of embryonic cardiac myocytes in the conduction system." — [PMID: 15085192]

### Finding 3 — Nkx2-5 is essential for cardiac looping and ventricular myogenic specification
Lyons et al. (1995): null embryos form a linear tube but fail looping and die E9–10; MLC2V is absent [PMID: 7628699].

> "this gene is a component of a genetic pathway required for myogenic specialization of the ventricles" — [PMID: 7628699]

### Finding 4 — Broad phenotypic spectrum (ASD predominant, progressive AV block, VSD/conotruncal/Ebstein, myopathy)
Documented in Benson et al. and Schott et al. [PMID: 10587520, 9651244] (see Section 3 table).

### Finding 5 — NKX2-5 acts in a combinatorial network; targets include GJA5/connexin40 and BMP10
Jay et al. (connexin40 target) [PMID: 15085192]; Pashmforoush et al. (ectopic BMP10, aberrant conduction/chamber target genes) [PMID: 15109497].

### Finding 6 — Autosomal dominant with incomplete penetrance / variable expressivity
Benson et al.: diverse coinherited CHD phenotypes; clinically significant contribution to TOF and idiopathic AV block [PMID: 10587520].

### Finding 7 — Mouse models recapitulate the disease dosage-dependently; mechanism is deeply conserved
Allelic series across [PMID: 7628699, 15085192, 15109497]; conserved from *Drosophila tinman* through zebrafish *nkx2.5*.

---

## Evidence Base

| PMID | Study (year, journal) | Evidence type | Contribution |
|---|---|---|---|
| [9651244](https://pubmed.ncbi.nlm.nih.gov/9651244/) | Schott et al., 1998, *Science* | Human genetics | Mapped locus to 5q35; identified NKX2-5 mutations; established haploinsufficiency; septation + lifelong AV-node roles |
| [10587520](https://pubmed.ncbi.nlm.nih.gov/10587520/) | Benson et al., 2000, *JCI* | Human genetics/clinical | 7 novel mutations, 26 probands; AV block ~25% primary; ASD/VSD/TOF/DORV/Ebstein spectrum; variable expressivity |
| [15085192](https://pubmed.ncbi.nlm.nih.gov/15085192/) | Jay et al., 2004, *JCI* | Mouse model | Gene-dosage dependence of conduction-system cellularity; connexin40 target; hypoplastic AV node |
| [15109497](https://pubmed.ncbi.nlm.nih.gov/15109497/) | Pashmforoush et al., 2004, *Cell* | Mouse model | Progressive complete heart block (hypoplasia + dropout); ectopic BMP10 drives myopathic/non-compaction branch |
| [7628699](https://pubmed.ncbi.nlm.nih.gov/7628699/) | Lyons et al., 1995, *Genes Dev* | Mouse model | Nkx2-5 required for cardiac looping and ventricular myogenic specification; absent MLC2V in nulls |

The evidence base is internally consistent: human genetic studies define the phenotype and the haploinsufficiency mechanism, and the mouse allelic series supplies the mechanistic causal chain, dosage dependence, and molecular mediators (connexin40, BMP10). The mouse and human data are mutually reinforcing.

---

## Limitations and Knowledge Gaps

1. **Quantitative penetrance/expressivity** for each phenotype across large modern cohorts is incompletely captured; the Benson cohort (26 probands) is foundational but small.
2. **Genotype–phenotype correlation** — whether DNA-binding-missense vs. truncating variants preferentially cause conduction vs. structural vs. myopathic disease — is not fully resolved.
3. **Modifier genes and gene–environment interactions** are undefined despite clear variable expressivity.
4. **Human BMP10 confirmation:** the myopathic/BMP10 mechanism is robustly shown in mouse but direct human ventricular-tissue confirmation is limited.
5. **Disease-specific prevalence** as a standalone epidemiological figure was not individually retrieved; estimates derive from CHD-attributable-fraction literature.
6. **Literature-fetch limitation:** A PubMed esearch outage during the investigation locked the citation base to a verified set of efetch-confirmed landmark papers rather than an exhaustive recent-literature sweep.

---

## Proposed Follow-up Experiments / Actions

1. **Variant-stratified cohort analysis:** Mine ClinVar/HGMD NKX2-5 variants and test genotype–phenotype correlation (truncating vs. homeodomain-missense vs. dominant-negative) against conduction, structural, and myopathic sub-phenotypes.
2. **iPSC-cardiomyocyte modeling:** Patient-derived iPSC-CMs with isogenic correction to quantify dosage effects on conduction (GJA5) and BMP10 expression, bridging mouse mechanism to human cells.
3. **Natural-history registry query:** Extract age-of-onset and progression-rate distributions for AV block to quantify the progressive-conduction model.
4. **Modifier screen:** GWAS/exome analysis within NKX2-5 families to identify modifier loci explaining variable expressivity.
5. **BMP10 human validation:** Examine BMP10 in explanted/biopsied ventricular myocardium from NKX2-5-mutant non-compaction patients.
6. **Prospective pacing study:** Correlate genotype with timing/necessity of pacemaker implantation to inform surveillance intervals.

---

## Consensus Answer

NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease (MONDO:0800441; OMIM #108900, ASD7) is an autosomal-dominant disorder caused by heterozygous, mostly loss-of-function (haploinsufficient) variants in **NKX2-5**, the NK2-class homeodomain cardiac transcription factor at 5q35.1 (vertebrate homolog of *Drosophila tinman*). Reduced NKX2-5 dosage impairs its combinatorial activation (with GATA4/TBX5/GATA6) of chamber- and conduction-specific gene programs, producing three linked manifestations: structural defects (characteristically secundum ASD, plus VSD, tetralogy of Fallot, Ebstein anomaly) from disrupted looping/septation; a dosage-dependent hypoplastic AV node with progressive postnatal conduction-cell dropout causing age-progressive AV block and sudden-death risk; and a myopathic branch (ventricular non-compaction/cardiomyopathy) driven by ectopic BMP10. Management is phenotype-directed (septal closure, pacemaker/ICD, heart-failure therapy) with no gene-specific cure, and the mechanism is faithfully recapitulated dosage-dependently in mouse models.


## Artifacts

- [OpenScientist final report](NKX2-5-Related_Congenital_Conduction_and_Myopathic_Heart_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](NKX2-5-Related_Congenital_Conduction_and_Myopathic_Heart_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 17 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800441` (3 mentions) - the report calls it "MONDO"; MONDO calls it **NKX2.5-related congenital, conduction and myopathic heart disease**
- `HP:0001684` (1 mention) - the report calls it "Physical malformation"; HP calls it **Secundum atrial septal defect**
- `HP:0001678` (1 mention) - the report calls it "Clinical sign (ECG)"; HP calls it **Atrioventricular block**
- `HP:0011705` (1 mention) - the report calls it "Lab/ECG abnormality"; HP calls it **First degree atrioventricular block**
- `HP:0011706` (1 mention) - the report calls it "Lab/ECG abnormality"; HP calls it **Second degree atrioventricular block**
- `HP:0001709` (1 mention) - the report calls it "Lab/ECG abnormality"; HP calls it **Third degree atrioventricular block**
- `HP:0001629` (1 mention) - the report calls it "Physical malformation"; HP calls it **Ventricular septal defect**
- `HP:0001636` (1 mention) - the report calls it "Physical malformation"; HP calls it **Tetralogy of Fallot**
- `HP:0002356` (1 mention) - the report calls it "Physical malformation"; HP calls it **Writer's cramp**
- `HP:0001702` (1 mention) - the report calls it "Physical malformation"; HP calls it **Abnormal tricuspid valve morphology**
- `HP:0030682` (1 mention) - the report calls it "Physical/structural"; HP calls it **Left ventricular noncompaction**
- `HP:0001644` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dilated cardiomyopathy**
- `HP:0001645` (1 mention) - the report calls it "Outcome"; HP calls it **Sudden cardiac death**
- `NCIT:C51658` (1 mention) - the report calls it "Cardiac surgery"; NCIT calls it **Gastric Antrectomy**
- `NCIT:C50114` (1 mention) - the report calls it "Pacemaker"; NCIT calls it **Power Module Device**
- `NCIT:C62226` (1 mention) - the report calls it "Implantable defibrillator"; NCIT calls it **Juvenile Lesion**
- `NCIT:C577` (1 mention) - the report calls it "Anticoagulant therapy"; NCIT calls it **Industrial Waste**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010316` (1 mention) - the report calls it "Physical malformation"; HP calls it **Ebstein anomaly of the tricuspid valve**, and lists "Ebstein's malformation" among its other names
- `GO:0061337` (1 mention) - the report calls it "GO biological processes:** cardiac conduction"; GO calls it **cardiac conduction**
- `UBERON:0000948` (1 mention) - the report calls it "Organ:** Heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names
- `UBERON:0002085` (1 mention) - the report calls it "Structures:** interatrial/atrial septum"; UBERON calls it **interatrial septum**