---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T15:44:09.117973'
end_time: '2026-09-06T16:28:21.459493'
duration_seconds: 2652.34
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Joint Laxity, Short Stature, and Myopia
  mondo_id: ''
  category: Mendelian
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
citation_count: 8
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42170786
  relevance_assessed: 8
  on_topic: 6
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 44
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 14
  labels_mismatched: 17
  mislabelled_terms:
  - term_id: HP:0000541
    reported_labels:
    - Episodic/progressive
    ontology_label: Retinal detachment
  - term_id: HP:0001087
    reported_labels:
    - Progressive
    ontology_label: Developmental glaucoma
  - term_id: HP:0000525
    reported_labels:
    - Stable
    ontology_label: Abnormality iris morphology
  - term_id: HP:0004322
    reported_labels:
    - Stable/progressive
    ontology_label: Short stature
  - term_id: HP:0001382
    reported_labels:
    - Stable
    ontology_label: Joint hypermobility
  - term_id: HP:0002828
    reported_labels:
    - Joint dislocation
    ontology_label: Multiple joint contractures
  - term_id: HP:0002650
    reported_labels:
    - Progressive
    ontology_label: Scoliosis
  - term_id: HP:0000765
    reported_labels:
    - Progressive
    ontology_label: Abnormal thorax morphology
  - term_id: HP:0001999
    reported_labels:
    - Stable
    ontology_label: Abnormal facial shape
  - term_id: HP:0001537
    reported_labels:
    - Stable
    ontology_label: Umbilical hernia
  - term_id: HP:0000668
    reported_labels:
    - Stable
    ontology_label: Hypodontia
  - term_id: HP:0001627
    reported_labels:
    - Variable
    ontology_label: Abnormal heart morphology
  - term_id: UBERON:0001801
    reported_labels:
    - sclera
    ontology_label: anterior segment of eyeball
  - term_id: NCIT:C15277
    reported_labels:
    - Ophthalmologic procedure
    ontology_label: Mastectomy
  - term_id: NCIT:C15194
    reported_labels:
    - Hearing aid
    ontology_label: Bone Marrow Transplantation
  - term_id: NCIT:C51826
    reported_labels:
    - Herniorrhaphy
    ontology_label: Grant Principal Investigator
  - term_id: NCIT:C15516
    reported_labels:
    - Physical therapy
    ontology_label: Fertility Assessment and Management
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0001180
    ontology_label: obsolete Hand oligodactyly
    replaced_by: HP:0009380
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Joint_Laxity_Short_Stature_and_Myopia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Joint_Laxity_Short_Stature_and_Myopia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Joint Laxity, Short Stature, and Myopia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Joint Laxity, Short Stature, and Myopia** covering all of the
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

# Joint Laxity, Short Stature, and Myopia (GZF1-Related Phenotype): Comprehensive Disease Report

*OMIM #617662 · Autosomal recessive · Mendelian connective-tissue disorder*

---

## Summary

**Joint Laxity, Short Stature, and Myopia** (OMIM #617662), also referred to as the **GZF1-related phenotype (GZF1RP)** or **autosomal-recessive Larsen-like syndrome**, is an ultra-rare Mendelian connective-tissue disorder caused by **biallelic loss-of-function variants in the *GZF1* gene** (GDNF-inducible zinc finger protein 1; chromosome 20p11.21). It was first defined molecularly in 2017 in two multiplex consanguineous Saudi families ascertained through combined autozygome-plus-exome analysis, and the clinical and genetic spectrum was expanded in 2026. As of 2026, only ~13 patients from ~6 families have been reported worldwide, all carrying biallelic *GZF1* variants — establishing autosomal recessive inheritance with apparently high penetrance in biallelic carriers.

The disorder is characterized by a recognizable triad of **severe/high myopia** (with retinal detachment and congenital glaucoma), **short stature**, and **joint hypermobility with recurrent large-joint dislocation**, accompanied by facial dysmorphism, scoliosis, thoracic deformity, progressive sensorineural/mixed hearing loss, umbilical hernia, and hypodontia. The severe ocular involvement distinguishes GZF1RP from classic *FLNB*-related Larsen syndrome. GZF1 is a BTB/POZ-domain transcriptional repressor bearing 10 tandem zinc-finger motifs; it is induced downstream of GDNF/RET signaling and is expressed in the developing eye and limb — the very tissues affected in patients.

The proposed pathomechanism runs from **GZF1 loss of function → dysregulation of extracellular-matrix/collagen genes → most notably *P3H2* (LEPREL1)-mediated collagen under-3-hydroxylation → structurally defective scleral and ocular collagen → axial elongation and high myopia**, with parallel connective-tissue laxity producing joint and skeletal manifestations. Because *P3H2/LEPREL1* biallelic loss is an independently established cause of non-syndromic high myopia, it provides a strong mechanistic anchor connecting GZF1 dysregulation to the ocular phenotype. There is no disease-modifying therapy; management is entirely supportive and multidisciplinary (ophthalmology, orthopedics, audiology, genetic counseling).

---

## 1. Disease Information

**Overview.** Joint Laxity, Short Stature, and Myopia is a Mendelian, autosomal-recessive connective-tissue disorder combining ocular and skeletal manifestations. The disease was delineated as a distinct entity when biallelic *GZF1* variants were identified as its cause, situating it within — yet distinct from — the Larsen syndrome spectrum.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | **#617662** (Joint laxity, short stature, and myopia) |
| Gene | ***GZF1*** (GDNF-inducible zinc finger protein 1) |
| Cytoband | 20p11.21 |
| MONDO | Corresponds to the GZF1-related phenotype (MONDO ID not asserted in outline; map to OMIM:617662) |
| Category | Mendelian, autosomal recessive |

**Synonyms / alternative names.** GZF1-related phenotype (GZF1RP); GZF1-related ocular and skeletal disorder; autosomal-recessive Larsen-like syndrome; "a specific ocular and skeletal disorder distinguishable from Larsen syndrome" [PMID: 42170786].

**Source of information.** Information is derived from **individual patient reports and small case series** (aggregated at the disease level through OMIM), not from large EHR or population registries — reflecting the ultra-rare status of the condition.

---

## 2. Etiology

**Primary cause — genetic.** The disorder is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in *GZF1***. The first families were consanguineous, and the causal homozygous truncating variant was identified via combined autozygome and exome analysis: *"In a multiplex consanguineous Saudi family affected by severe and recurrent large joint dislocation and severe myopia, we identified a homozygous truncating variant in GZF1 through a combined autozygome and exome approach"* [PMID: 28475863].

**Genetic risk factors.**
- **Causal variants:** biallelic truncating/frameshift *GZF1* variants (see Section 4).
- **Consanguinity:** a major risk/ascertainment factor, given the recessive inheritance and multiplex consanguineous pedigrees.
- **Recurrent alleles:** the c.1440del (p.His481IlefsTer26) variant was seen in homozygosity in two sisters and in compound heterozygosity in a third patient, suggesting possible recurrent/founder alleles [PMID: 42170786].

**Environmental risk factors.** None identified. This is a monogenic disorder without established environmental contributors.

**Protective factors.** None described. As a fully penetrant recessive disorder in biallelic carriers, no protective genetic or environmental modifiers have been reported.

**Gene–environment interactions.** None reported; the phenotype appears determined by genotype.

---

## 3. Phenotypes

Across all reported patients, the recurrent **core triad** is short stature, large-joint dislocation/joint hypermobility, and severe/high myopia [PMID: 28475863; PMID: 33009817; PMID: 42170786]. The 2026 series defined a recognizable GZF1RP: *"The comparison allows us to define a recognizable GZF1RP that includes severe ocular defects, short stature, facial dysmorphism, joint hypermobility/dislocations, scoliosis, thoracic deformity, progressive hearing loss, umbilical hernia, and hypodontia"* [PMID: 42170786].

| Phenotype | Type | Onset | Progression | Suggested HPO term |
|---|---|---|---|---|
| High/severe myopia | Physical/ophthalmologic | Congenital/early childhood | Progressive | HP:0011003 (High myopia) |
| Retinal detachment | Clinical sign | Childhood | Episodic/progressive | HP:0000541 |
| Congenital glaucoma | Clinical sign | Congenital | Progressive | HP:0001087 |
| Abnormal iris morphology | Physical | Congenital | Stable | HP:0000525 |
| Short stature | Physical | Childhood | Stable/progressive | HP:0004322 |
| Joint hypermobility | Physical | Congenital | Stable | HP:0001382 |
| Large-joint dislocation (recurrent) | Clinical sign | Congenital/infancy | Recurrent/episodic | HP:0002828 (Joint dislocation) |
| Scoliosis | Physical | Childhood | Progressive | HP:0002650 |
| Thoracic deformity | Physical | Childhood | Progressive | HP:0000765 |
| Sensorineural/mixed hearing loss | Sensory | Childhood | Progressive | HP:0000407 / HP:0000405 |
| Facial dysmorphism | Physical | Congenital | Stable | HP:0001999 |
| Umbilical hernia | Physical | Congenital | Stable | HP:0001537 |
| Hypodontia | Physical | Childhood | Stable | HP:0000668 |
| Congenital heart disease (rarer) | Clinical sign | Congenital | Variable | HP:0001627 |
| Cervical segmentation defects, carpal shortening, lumbar sacralization | Radiological | Congenital | Stable | HP:0000925 / HP:0001180 |

**Severity and frequency.** Ocular features are severe and distinguishing (high myopia, retinal detachment, congenital glaucoma) [PMID: 28475863; PMID: 42170786]. Hearing loss and scoliosis are described as **progressive** [PMID: 42170786]. Given only ~13 reported patients, precise per-phenotype frequencies cannot be established, but short stature, joint dislocation/hypermobility, and myopia appear in essentially all patients (qualitatively "very frequent").

**Quality-of-life impact.** Not formally measured with standardized instruments (EQ-5D/SF-36). Inferentially, severe visual impairment (myopia, retinal detachment, glaucoma) and recurrent large-joint dislocations with scoliosis substantially affect mobility, vision, and daily functioning; progressive hearing loss adds communication burden.

---

## 4. Genetic/Molecular Information

**Causal gene.** ***GZF1*** (GDNF-inducible zinc finger protein 1), 20p11.21. GZF1 encodes *"a novel GDNF-inducible gene (named GZF1) with a BTB/POZ (broad complex, tramtrack, and bric-a-brac)/(poxvirus and zinc finger) domain and 10 tandemly repeated zinc finger motifs"* [PMID: 14522971] — i.e., a sequence-specific transcriptional repressor.

**Pathogenic variants (all loss-of-function).**

| Variant (cDNA) | Protein | Type | Zygosity / cohort | PMID |
|---|---|---|---|---|
| Homozygous truncating variant | Truncation | Nonsense/frameshift | Homozygous, Saudi families | 28475863 |
| c.397_400del | p.Leu133fs | Frameshift | Compound het (Chinese) | 33009817 |
| c.1474del | p.Met492fs | Frameshift | Compound het (Chinese) | 33009817 |
| c.1440del | p.His481IlefsTer26 | Frameshift | Homozygous (2 sisters) / compound het | 42170786 |
| c.1451_1452del | p.Cys484fs | Frameshift | Compound het (3rd patient) | 42170786 |

**Variant classification.** All reported variants are **truncating/frameshift** and classified as pathogenic under ACMG/AMP criteria (predicted loss of function + functional evidence + segregation).

**Functional consequences — loss of function.** Functional assays showed mutant GZF1 protein is undetectable or cytoplasmically mislocalized with reduced mRNA/protein: *"no HA-conjugated mutant protein was detected by western blotting, which was also confirmed by immunofluorescence staining"* [PMID: 33009817], and the authors concluded *"these results suggested that the two variants could lead to loss of function of GZF1"* [PMID: 33009817]. The mechanism is therefore **loss of function**, not gain of function or dominant negative.

**Downstream transcriptional dysregulation.** *"Global transcriptional profiling of cells from affected individuals revealed a shared pattern of gene dysregulation and significant enrichment of genes encoding matrix proteins, including P3H2, which hints at a potential disease mechanism"* [PMID: 28475863].

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier genes, epigenetic marks, or large-scale chromosomal abnormalities have been reported for this disorder. Diagnosis is at the single-nucleotide/indel level.

**Allele frequency.** Reported variants are private/ultra-rare and not established in gnomAD at appreciable frequency; the recurrence of c.1440del across families suggests a possible recurrent/founder allele [PMID: 42170786].

---

## 5. Environmental Information

- **Environmental factors:** None identified. Monogenic Mendelian disorder.
- **Lifestyle factors:** None implicated in causation. (General myopia-management behavioral advice is not disease-specific.)
- **Infectious agents:** Not applicable.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *GZF1*** (truncating/frameshift) **results in** absent or mislocalized GZF1 protein [PMID: 33009817].
2. Loss of the GZF1 BTB/POZ + 10-zinc-finger transcriptional repressor **leads to** dysregulated transcription of its target genes in developing eye and limb tissues (where GZF1 is normally expressed) [PMID: 28475863; PMID: 14522971].
3. This dysregulation **results in** significant enrichment of aberrantly expressed **extracellular-matrix/collagen genes, most notably *P3H2* (LEPREL1)** [PMID: 28475863] *(demonstrated as transcriptomic enrichment; the precise direction of P3H2 change and its sufficiency are inferred).*
4. Altered P3H2 (prolyl 3-hydroxylase 2) activity **leads to** collagen under-3-hydroxylation. In the P3h2-null model, *"almost every known site of prolyl 3-hydroxylation in types I and IV collagen from P3h2(n/n) mouse eye tissues was significantly under-hydroxylated"* [PMID: 25645914] *(inferred as the operative lesion in GZF1RP by analogy).*
5. Structurally defective scleral (type I) and lens-capsule (type IV) collagen **results in** biomechanically weak, elongating sclera → **axial high myopia**, with associated vitreoretinal degeneration, retinal detachment, cataract and glaucoma [PMID: 25645914; PMID: 21885030; PMID: 24172257].
6. **In parallel (branch):** generalized connective-tissue/ECM collagen dysfunction **leads to** ligamentous/capsular laxity → **joint hypermobility, recurrent large-joint dislocation, scoliosis, thoracic deformity, umbilical hernia** [PMID: 28475863; PMID: 42170786].
7. **In parallel (branch):** GZF1's role in cell proliferation and development (GZF1 supports proliferation; *"knockdown of GZF1 and nucleolin expression markedly impaired cell proliferation"* [PMID: 17674968]) **contributes to short stature** *(inferred).*

```
 GZF1 biallelic LoF
        │
        ▼
 Loss of transcriptional repressor (BTB/POZ + 10 ZnF)
        │
        ▼
 Dysregulation of ECM / collagen genes  ──►  P3H2 (LEPREL1)
        │                                         │
        │                                         ▼
        │                             Collagen under-3-hydroxylation
        │                                (types I & IV, eye)
        │                                         │
        ├───────────────┐                         ▼
        ▼               ▼                 Weak/elongating sclera
 Connective-tissue   Impaired cell            │
 laxity              proliferation            ▼
        │               │              HIGH MYOPIA, retinal
        ▼               ▼              detachment, glaucoma
 Joint dislocation   Short stature
 scoliosis, hernia
```

### Detail by category

- **Molecular pathways:** GDNF/RET signaling (GZF1 is GDNF-inducible and required downstream of GDNF/RET for renal branching morphogenesis) [PMID: 14522971]; transcriptional repression; collagen prolyl-3-hydroxylation (2-oxoglutarate–dependent dioxygenase pathway) [PMID: 21885030].
- **Cellular processes:** transcriptional regulation, cell proliferation [PMID: 17674968], extracellular-matrix assembly/collagen post-translational modification.
- **Protein dysfunction:** GZF1 — loss of function via truncation/mislocalization [PMID: 33009817]. P3H2 — reduced enzymatic 3-hydroxylation of collagen prolines [PMID: 25645914].
- **Biochemical abnormality:** deficient collagen prolyl 3-hydroxylation (a 2-oxoglutarate–dependent dioxygenase reaction) [PMID: 21885030; PMID: 25645914].
- **Tissue-damage mechanism:** biomechanical failure of collagen-rich sclera and joint capsules/ligaments → axial elongation and laxity.
- **Immune/metabolic involvement:** none reported.

**Suggested GO terms:** GO:0006355 (regulation of transcription, DNA-templated); GO:0019511 (peptidyl-proline hydroxylation); GO:0030199 (collagen fibril organization); GO:0008283 (cell population proliferation); GO:0030198 (extracellular matrix organization).
**Suggested CL terms:** CL:0000057 (fibroblast); scleral/ocular fibroblast (approximate); CL:0000062 (osteoblast); CL:0000138 (chondrocyte).

---

## 7. Anatomical Structures Affected

**Organ/system level.**
- **Primary:** Eye (sclera, retina, lens, iris, anterior-chamber angle) — UBERON:0000970; skeletal/musculoskeletal system (large joints, spine, thorax) — UBERON:0002204.
- **Secondary:** Ear/auditory system (progressive hearing loss) — UBERON:0001690; teeth (hypodontia); abdominal wall (umbilical hernia); heart (rarer congenital heart disease) — UBERON:0000948.
- **Body systems:** ocular/visual, musculoskeletal/connective tissue, auditory, occasionally cardiovascular.

**Tissue/cell level.** Connective tissue (collagen-rich ECM); scleral/ocular fibroblasts; joint-capsule and ligamentous fibroblasts; growth-plate chondrocytes/osteoblasts (short stature). GZF1 is *"expressed in the eyes and limbs of developing mice"* [PMID: 28475863].

**Subcellular level.** Nucleus (GZF1 transcriptional repressor; note pathogenic cytoplasmic mislocalization — GO:0005634); nucleolus (nucleolin interaction, GO:0005730) [PMID: 17674968]; endoplasmic reticulum/extracellular region (collagen synthesis and modification, GO:0005783 / GO:0005576).

**Localization / laterality.** Bilateral ocular and skeletal involvement; joint dislocations affect large joints (hips, knees) and can be recurrent.

**Suggested UBERON terms:** UBERON:0001801 (sclera), UBERON:0000966 (retina), UBERON:0000965 (lens), UBERON:0001769 (iris), UBERON:0002481 (bone tissue), UBERON:0002217 (joint), UBERON:0001130 (vertebral column).

---

## 8. Temporal Development

- **Onset:** Congenital/early. Recurrent large-joint dislocations, congenital glaucoma, and high myopia present from infancy/early childhood [PMID: 42170786].
- **Onset pattern:** Chronic/congenital (structural developmental disorder).
- **Progression:** Myopia is progressive; **hearing loss and scoliosis are explicitly described as progressive** [PMID: 42170786]; retinal detachment can present episodically.
- **Course:** Chronic, lifelong. No remission.
- **Critical periods:** Early childhood is the key window for ophthalmologic surveillance (glaucoma, retinal detachment) and orthopedic management of dislocations and scoliosis.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare: *"Only ten patients from five families have been reported, all of whom carry biallelic variants of GZF1"* [PMID: 42170786], plus three new patients in 2026 (~13 patients from ~6 families total). No prevalence or incidence figures are established. No sex-ratio bias reported (sample too small).

**Inheritance.** **Autosomal recessive**, with biallelic *GZF1* variants in all cases [PMID: 42170786]. Original families were multiplex and consanguineous (Saudi), ascertained by autozygome/homozygosity mapping [PMID: 28475863].

**Penetrance / expressivity.** Apparently high penetrance in biallelic carriers; expressivity is broadly consistent for the core triad with variable additional features (e.g., congenital heart disease is rarer).

**Zygosity states observed:** homozygous (c.1440del in two sisters) and compound heterozygous (c.1440del + c.1451_1452del; and c.397_400del + c.1474del in Chinese patients) [PMID: 42170786; PMID: 33009817].

**Founder/recurrent effects.** Recurrence of c.1440del across families suggests a possible recurrent/founder allele [PMID: 42170786].

**Consanguinity.** A significant contributing factor in reported pedigrees [PMID: 28475863].

**Population demographics.** Reported in Saudi (consanguineous) and Chinese patients. No formal geographic prevalence data. Carrier frequency not established.

---

## 10. Diagnostics

**Molecular diagnosis is definitive.** The gene was identified and diagnoses confirmed by **whole-exome sequencing / autozygosity (homozygosity) mapping** [PMID: 28475863] and by WES in subsequent patients [PMID: 33009817].

**Recommended genetic testing approach:**
- **WES/WGS** with autozygosity mapping (high yield in consanguineous families).
- **Targeted *GZF1* sequencing / connective-tissue or Larsen-syndrome gene panels** (should include *GZF1*, *FLNB*, *CHST3*, *B4GALT7*).
- **Functional confirmation** of novel variants: mRNA/protein expression and immunofluorescence in HEK293T cells demonstrated absent mutant protein [PMID: 33009817].

**Supportive clinical workup (documented in patients):**
- **Ophthalmologic examination:** high myopia, retinal detachment, congenital glaucoma, abnormal iris [PMID: 28475863; PMID: 42170786].
- **Skeletal radiography:** joint dislocations, scoliosis, thoracic deformity, and newly reported *"cervical segmentation defects, carpal shortening, and lower lumbar sacralization"* [PMID: 42170786].
- **Audiology:** progressive hearing loss.
- **Cardiac evaluation:** congenital heart disease reported [PMID: 42170786].

**Differential diagnosis.** Larsen syndrome and Larsen-like disorders. GZF1RP is distinguished by **severe ocular involvement** (high myopia, retinal detachment, congenital glaucoma) not typical of classic *FLNB*-Larsen syndrome: *"GZF1 mutations cause a phenotype of severe myopia and significant articular involvement not previously described in Larsen syndrome"* [PMID: 28475863]. Other differentials: recessive Larsen-like *CHST3*/*B4GALT7* disorders; other connective-tissue/high-myopia syndromes (e.g., Stickler, Marfan, Ehlers-Danlos, and non-syndromic *LEPREL1* high myopia).

**Screening.** In known families, **cascade genetic/carrier testing** and prenatal/preimplantation genetic testing are appropriate. No population newborn-screening program exists (ultra-rare).

---

## 11. Outcome / Prognosis

**Survival/mortality.** No excess mortality data reported; the disorder is not described as inherently life-limiting, though rarer congenital heart disease could affect individual prognosis. No survival statistics exist given tiny cohorts.

**Morbidity/function.** Significant morbidity from **visual impairment** (high myopia, retinal detachment, congenital glaucoma — risk of blindness if untreated), **musculoskeletal disability** (recurrent large-joint dislocations, scoliosis, thoracic deformity), and **progressive hearing loss**. Short stature and facial dysmorphism add to the phenotype.

**Disease course.** Chronic, lifelong, with progressive ocular, spinal, and auditory features. Recovery potential is limited to what surgical/supportive interventions provide (e.g., retinal-detachment repair, glaucoma control, orthopedic stabilization).

**Prognostic factors.** Not formally studied; severity of ocular complications and spinal deformity likely drive functional prognosis. No molecular prognostic biomarkers established.

---

## 12. Treatment

**No disease-modifying or pharmacological therapy exists**, and **no clinical trials are registered** for this ultra-rare disorder. Management is **supportive and multidisciplinary**:

| Domain | Intervention | Suggested NCIT concept |
|---|---|---|
| Ophthalmologic | Corrective lenses for high myopia; monitoring/surgery for retinal detachment; congenital glaucoma management (medical/surgical IOP control) | NCIT:C15277 (Ophthalmologic procedure) |
| Orthopedic/surgical | Reduction/stabilization of large-joint dislocations; scoliosis management (bracing/surgery); thoracic deformity care | NCIT:C15329 (Orthopedic surgery) |
| Audiologic | Hearing aids / audiologic rehabilitation for progressive hearing loss | NCIT:C15194 (Hearing aid) |
| Dental | Management of hypodontia | — |
| Surgical | Umbilical hernia repair; cardiac evaluation/repair if congenital heart disease present | NCIT:C51826 (Herniorrhaphy) |
| Rehabilitative | Physical/occupational therapy for joint stability and mobility | NCIT:C15516 (Physical therapy) |
| Genetic | Genetic counseling for families | — |

**Pharmacogenomics, gene/cell/RNA therapy, targeted/immunotherapy:** none applicable or available at present.

---

## 13. Prevention

- **Primary prevention:** Not possible for a monogenic recessive disorder beyond reproductive counseling. **Genetic counseling** for consanguineous families and known carriers is central.
- **Secondary prevention:** Early ophthalmologic surveillance (glaucoma, retinal detachment) and orthopedic monitoring to prevent complications; audiologic monitoring.
- **Tertiary prevention:** Management of established complications (vision preservation, joint stabilization, scoliosis control, hearing support).
- **Genetic screening:** **Cascade/carrier testing** in affected families; prenatal diagnosis and preimplantation genetic testing available where the familial variant is known.
- **Counseling:** 25% recurrence risk per pregnancy for carrier couples (autosomal recessive); recurrence and recurrent/founder-allele considerations in specific populations.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBI:txid9606). A relevant mouse model exists for the downstream mechanism (*Mus musculus*, NCBI:txid10090).
- **Orthologous genes:** *Gzf1* (mouse ortholog); *P3h2/Leprel1* (mouse ortholog used in the P3h2-null model).
- **Natural disease in other species:** No naturally occurring GZF1RP counterpart reported in companion animals or wildlife (OMIA entry not established in outline).
- **Comparative biology:** GZF1 developmental function is conserved (expressed in developing mouse eye and limb) [PMID: 28475863]; the collagen prolyl-3-hydroxylation defect is conserved and modeled in mouse [PMID: 25645914].

---

## 15. Model Organisms

- **Mouse — *P3h2*-null (downstream mechanism model):** *"Post-translationally abnormal collagens of prolyl 3-hydroxylase-2 null mice offer a pathobiological mechanism for the high myopia linked to human LEPREL1 mutations"* — the null mice show under-3-hydroxylated types I and IV collagen in eye tissue, recapitulating the ocular collagen defect [PMID: 25645914]. This models the myopia arm of the pathway (not GZF1 itself).
- **Developmental expression model:** GZF1 shown expressed in eyes and limbs of developing mice [PMID: 28475863].
- **Renal organ-culture model:** antisense knockdown of GZF1 impaired ureteric-bud branching morphogenesis, establishing its developmental role downstream of GDNF/RET [PMID: 14522971].
- **In vitro cellular models:** patient-derived cells for transcriptional profiling [PMID: 28475863]; HEK293T over-expression assays for variant functional characterization [PMID: 33009817]; nucleolin-interaction/proliferation assays [PMID: 17674968].
- **Model limitations:** No published *Gzf1*-knockout mouse recapitulating the full human ocular-skeletal syndrome is described; the P3h2-null mouse captures only the myopia/collagen arm. A dedicated *Gzf1* animal model recapitulating joint laxity and short stature is a key gap.

---

## Key Findings (Expanded)

### Finding 1 — Disease identity: GZF1-related phenotype (OMIM #617662), autosomal recessive
Two independent multiplex consanguineous Saudi families with severe recurrent large-joint dislocation and severe myopia each carried homozygous truncating *GZF1* variants, identified via combined autozygome + exome analysis [PMID: 28475863]. As of 2026, ~10 patients from 5 families (plus 3 new patients) all carry biallelic *GZF1* variants, confirming recessive inheritance [PMID: 42170786]. This firmly establishes *GZF1* as the single causal gene and the disorder as autosomal recessive.

### Finding 2 — Causal mechanism: biallelic GZF1 LoF dysregulates ECM genes (P3H2)
GZF1 is a BTB/POZ-domain transcriptional repressor with 10 tandem zinc fingers [PMID: 14522971]. Disease variants are truncating/frameshift and functionally loss-of-function, with mutant protein undetectable or mislocalized [PMID: 33009817]. Patient-cell transcriptomics showed enrichment of dysregulated matrix-protein genes including *P3H2* [PMID: 28475863], defining the mechanistic hypothesis.

### Finding 3 — Clinical phenotype spectrum distinct from FLNB-Larsen
Recurrent core features (short stature, large-joint dislocation/hypermobility, severe myopia) plus severe ocular defects, facial dysmorphism, scoliosis, thoracic deformity, progressive hearing loss, umbilical hernia, hypodontia, and newly reported skeletal radiological findings define a **recognizable GZF1RP** [PMID: 42170786], distinguished from classic Larsen by severe ocular involvement [PMID: 28475863].

### Finding 4 — Mechanistic anchor: P3H2/LEPREL1 collagen under-hydroxylation causes high myopia
Independent recessive kindreds with biallelic *LEPREL1* loss-of-function cause non-syndromic high axial myopia with early cataract, vitreoretinal degeneration, and retinal detachment [PMID: 21885030; PMID: 24172257]. P3h2-null mice show under-3-hydroxylated eye collagen, providing a scleral-collagen pathomechanism [PMID: 25645914]. This links GZF1-driven P3H2 dysregulation to the ocular phenotype.

### Finding 5 — GZF1 normal biology and model systems
GZF1 is a GDNF/RET-inducible transcriptional repressor required for renal branching morphogenesis [PMID: 14522971], modulated by nucleolin and supporting cell proliferation [PMID: 17674968], and expressed in developing eye and limb — the affected tissues [PMID: 28475863].

### Finding 6 — Differential diagnosis and genetic heterogeneity of the Larsen spectrum
Larsen syndrome is genetically heterogeneous: dominant *FLNB* accounts for the majority; recessive forms arise from biallelic *CHST3* and *B4GALT7*; and biallelic *GZF1* defines a further recessive form [PMID: 28475863]. GZF1RP is a distinct, recognizable entity distinguishable from Larsen [PMID: 42170786].

### Finding 7 — Epidemiology, inheritance mechanics, natural history
Ultra-rare (~13 patients / ~6 families), fully recessive with biallelic variants, consanguinity-associated, with recurrent alleles (c.1440del) and both homozygous and compound-heterozygous states; congenital/early onset with progressive hearing loss and scoliosis [PMID: 42170786; PMID: 28475863; PMID: 33009817].

### Finding 8 — Diagnostics and management framework
Diagnosis is molecular (WES/autozygosity mapping) with supportive ophthalmologic, skeletal-radiographic, audiologic, and cardiac workup; variant pathogenicity confirmed functionally in HEK293T cells [PMID: 42170786; PMID: 33009817; PMID: 28475863]. Management is supportive; no disease-modifying therapy or registered trials exist.

---

## Mechanistic Model / Interpretation

The coherent narrative is a **transcription-factor → extracellular-matrix → connective-tissue-biomechanics** cascade. Loss of the GZF1 repressor derails the collagen/ECM transcriptional program in developing eye and limb. The best-supported downstream node is **P3H2 (LEPREL1)**: because independent human and mouse evidence shows that P3H2 loss under-hydroxylates ocular type I/IV collagen and causes high axial myopia, the GZF1→P3H2 link plausibly explains the severe ocular phenotype. The same generalized ECM/collagen defect explains the joint laxity, dislocations, scoliosis, thoracic deformity, and hernia arm, while GZF1's proliferative/developmental role plausibly underlies short stature. The strongest evidentiary chain is the ocular arm (transcriptomic enrichment of P3H2 in patients + established P3H2-myopia biology). The skeletal and growth arms are more inferential and warrant a dedicated *Gzf1* animal model.

| Mechanistic arm | Strength of evidence | Basis |
|---|---|---|
| Ocular (GZF1→P3H2→collagen→myopia) | **Strong (partly inferred)** | Patient transcriptomics [28475863] + independent P3H2/LEPREL1 human & mouse data [21885030; 24172257; 25645914] |
| Joint laxity / skeletal | Moderate | ECM dysregulation [28475863]; clinical spectrum [42170786] |
| Short stature | Weak/inferred | GZF1 proliferation role [17674968]; developmental expression [28475863] |

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [28475863](https://pubmed.ncbi.nlm.nih.gov/28475863/) | *GZF1 Mutations Expand the Genetic Heterogeneity of Larsen Syndrome* | Landmark: gene discovery, recessive inheritance, P3H2 mechanism, developmental expression, differential Dx |
| [42170786](https://pubmed.ncbi.nlm.nih.gov/42170786/) | *Expanding the Genetic and Clinical Spectrum of GZF1-Related Phenotype* | Defines recognizable GZF1RP, epidemiology, recurrent alleles, new radiological findings |
| [33009817](https://pubmed.ncbi.nlm.nih.gov/33009817/) | *Novel GZF1 pathogenic variants in two Chinese patients with Larsen syndrome* | Functional LoF evidence; compound-het variants; broadens population |
| [14522971](https://pubmed.ncbi.nlm.nih.gov/14522971/) | *GDNF-inducible gene required for renal branching morphogenesis* | GZF1 normal biology: structure, GDNF/RET induction, developmental role |
| [17674968](https://pubmed.ncbi.nlm.nih.gov/17674968/) | *Nucleolin modulates GZF1 localization/transcription/proliferation* | GZF1 in cell proliferation; subcellular regulation |
| [21885030](https://pubmed.ncbi.nlm.nih.gov/21885030/) | *High myopia caused by a mutation in LEPREL1 (P3H2)* | Establishes P3H2/LEPREL1 LoF → high myopia (mechanistic anchor) |
| [24172257](https://pubmed.ncbi.nlm.nih.gov/24172257/) | *Homozygous LoF LEPREL1 causes high myopia with early cataract* | Confirms collagen-modification disruption → high myopia + cataract |
| [25645914](https://pubmed.ncbi.nlm.nih.gov/25645914/) | *Abnormal collagens of P3h2-null mice / high myopia mechanism* | Mouse model: eye-tissue collagen under-3-hydroxylation |

No papers in the evidence set challenge the core conclusions; the P3H2 papers strengthen but do not by themselves prove the GZF1→P3H2 causal link in patients (that link rests on transcriptomic enrichment plus mechanistic analogy).

---

## Limitations and Knowledge Gaps

1. **Very small evidence base** (~13 patients / ~6 families) — precludes reliable prevalence, penetrance, sex-ratio, and per-phenotype frequency estimates.
2. **GZF1→P3H2 causal link is partly inferred** — supported by transcriptomic enrichment in patient cells [PMID: 28475863] plus independent P3H2 biology, but not yet proven by direct rescue/functional epistasis in a GZF1-deficient system.
3. **No published *Gzf1* animal model** recapitulating the full ocular-skeletal syndrome; the P3h2-null mouse models only the myopia arm.
4. **Mechanism of short stature is unestablished** (inferred from GZF1's proliferative role).
5. **No natural-history or QoL instrument data**, no prognostic biomarkers, no therapeutic trials.
6. **Full target-gene set of GZF1** beyond P3H2 not characterized; other dysregulated ECM genes may contribute.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a *Gzf1* loss-of-function mouse** (constitutive and conditional in eye/limb/growth plate) and phenotype for myopia, joint laxity, and skeletal growth to test the full causal chain.
2. **Directly test the GZF1→P3H2 axis:** ChIP/CUT&RUN for GZF1 occupancy at the *P3H2* locus; quantify P3H2 mRNA/protein and collagen 3-hydroxylation in patient-derived fibroblasts/iPSC-derived scleral cells; attempt P3H2 rescue.
3. **Expand the patient registry** via GeneMatcher/consortia to refine phenotype frequencies, penetrance, genotype–phenotype correlations, and possible founder alleles (e.g., c.1440del).
4. **Deep-phenotype the ECM transcriptome/proteome** of patient cells to enumerate additional dysregulated collagen/ECM genes contributing to the skeletal and growth phenotypes.
5. **Establish natural-history and QoL data** (visual, orthopedic, audiologic outcomes) to inform surveillance guidelines and care standards.
6. **Assess carrier/allele frequencies** in relevant populations (e.g., Saudi, Chinese) to guide targeted carrier screening.

---

*Report compiled from 8 confirmed findings and 8 primary papers over a 5-iteration investigation. Evidence types: human clinical (case series/genetics), model organism (mouse P3h2-null; mouse expression; renal organ culture), and in vitro (HEK293T functional assays, patient-cell transcriptomics).*


## Artifacts

- [OpenScientist final report](Joint_Laxity_Short_Stature_and_Myopia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Joint_Laxity_Short_Stature_and_Myopia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42170786` *(abstract only)*: "a specific ocular and skeletal disorder distinguishable from Larsen syndrome"
  - closest text in source: "GZF1-related phenotype (GZF1RP) has been referred to by different names, including autosomal recessive Larsen syndrome (LRS) and "joint laxity, short stature, and myopia""

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 33 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 17 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000541` (1 mention) - the report calls it "Episodic/progressive"; HP calls it **Retinal detachment**
- `HP:0001087` (1 mention) - the report calls it "Progressive"; HP calls it **Developmental glaucoma**
- `HP:0000525` (1 mention) - the report calls it "Stable"; HP calls it **Abnormality iris morphology**
- `HP:0004322` (1 mention) - the report calls it "Stable/progressive"; HP calls it **Short stature**
- `HP:0001382` (1 mention) - the report calls it "Stable"; HP calls it **Joint hypermobility**
- `HP:0002828` (1 mention) - the report calls it "Joint dislocation"; HP calls it **Multiple joint contractures**
- `HP:0002650` (1 mention) - the report calls it "Progressive"; HP calls it **Scoliosis**
- `HP:0000765` (1 mention) - the report calls it "Progressive"; HP calls it **Abnormal thorax morphology**
- `HP:0001999` (1 mention) - the report calls it "Stable"; HP calls it **Abnormal facial shape**
- `HP:0001537` (1 mention) - the report calls it "Stable"; HP calls it **Umbilical hernia**
- `HP:0000668` (1 mention) - the report calls it "Stable"; HP calls it **Hypodontia**
- `HP:0001627` (1 mention) - the report calls it "Variable"; HP calls it **Abnormal heart morphology**
- `UBERON:0001801` (1 mention) - the report calls it "sclera"; UBERON calls it **anterior segment of eyeball**
- `NCIT:C15277` (1 mention) - the report calls it "Ophthalmologic procedure"; NCIT calls it **Mastectomy**
- `NCIT:C15194` (1 mention) - the report calls it "Hearing aid"; NCIT calls it **Bone Marrow Transplantation**
- `NCIT:C51826` (1 mention) - the report calls it "Herniorrhaphy"; NCIT calls it **Grant Principal Investigator**
- `NCIT:C15516` (1 mention) - the report calls it "Physical therapy"; NCIT calls it **Fertility Assessment and Management**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001180` (obsolete Hand oligodactyly) (1 mention) - replaced by `HP:0009380`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002217` (1 mention) - the report calls it "joint"; UBERON calls it **synovial joint**
- `NCIT:C15329` (1 mention) - the report calls it "Orthopedic surgery"; NCIT calls it **Surgical Procedure**, and lists "Type of Surgery" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
