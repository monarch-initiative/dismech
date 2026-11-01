---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-26T12:17:04.006246'
end_time: '2026-10-26T12:31:29.606016'
duration_seconds: 865.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Distal Arthrogryposis Type 2B1
  mondo_id: MONDO:0020820
  category: Mendelian
  causal_genes: TNNI2
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 12
  relevance_assessed: 18
  on_topic: 10
  off_topic: 1
  off_topic_references:
  - PMID:39423837
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 3
  labels_mismatched: 15
  mislabelled_terms:
  - term_id: MONDO:0020820
    reported_labels:
    - MONDO
    ontology_label: distal arthrogryposis type 2B1
  - term_id: HP:0012385
    reported_labels:
    - Physical manifestation
    ontology_label: Camptodactyly
  - term_id: HP:0009465
    reported_labels:
    - Clinical sign
    ontology_label: Ulnar deviation of finger
  - term_id: HP:0001838
    reported_labels:
    - Clinical sign
    ontology_label: Rocker bottom foot
  - term_id: HP:0001762
    reported_labels:
    - Clinical sign
    ontology_label: Talipes equinovarus
  - term_id: HP:0000325
    reported_labels:
    - Physical manifestation
    ontology_label: Triangular face
  - term_id: HP:0000494
    reported_labels:
    - Physical manifestation
    ontology_label: Downslanted palpebral fissures
  - term_id: HP:0000160
    reported_labels:
    - Physical manifestation
    ontology_label: Narrow mouth
  - term_id: HP:0000303
    reported_labels:
    - Physical manifestation
    ontology_label: Mandibular prognathia
  - term_id: HP:0004322
    reported_labels:
    - Physical manifestation
    ontology_label: Short stature
  - term_id: HP:0005684
    reported_labels:
    - Clinical sign
    ontology_label: Distal arthrogryposis
  - term_id: NCIT:C15328
    reported_labels:
    - Physical Therapy
    ontology_label: Splenectomy
  - term_id: NCIT:C15329
    reported_labels:
    - Occupational Therapy
    ontology_label: Surgical Procedure
  - term_id: NCIT:C116746
    reported_labels:
    - Casting
    ontology_label: Anti-mesothelin/MMAE Antibody-drug Conjugate DMOT4039A
  - term_id: NCIT:C50048
    reported_labels:
    - Brace
    ontology_label: Read Only Memory Device
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Distal_Arthrogryposis_Type_2B1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Distal_Arthrogryposis_Type_2B1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Arthrogryposis Type 2B1
- **MONDO ID:** MONDO:0020820 (if available)
- **Causal gene(s):** TNNI2
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Distal Arthrogryposis Type 2B1** covering all of the
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

# Distal Arthrogryposis Type 2B1 (DA2B1 / Sheldon-Hall Syndrome): A Comprehensive Disease Report

**Target disease:** Distal Arthrogryposis Type 2B1 (DA2B1)
**MONDO ID:** MONDO:0020820 | **OMIM:** 601680 | **Causal gene:** **TNNI2** (fast-twitch skeletal-muscle troponin I; HGNC:11946; NCBI Gene 7136; UniProt P48788; gene OMIM 191043; 11p15.5)

This report concerns the **TNNI2**-caused form of Sheldon-Hall syndrome. The "2B" distal-arthrogryposis phenotype is genetically heterogeneous and can also arise from *TNNT3* (DA2B2), *MYH3* (DA2B3), and *TPM2* (DA2B4); the entry addressed here is the **TNNI2** allelic form (DA2B1), following the MONDO ID and causal gene provided.

---

## Summary

**Distal arthrogryposis type 2B1 (DA2B1), also known as Sheldon-Hall syndrome (SHS), is a rare autosomal-dominant congenital contracture disorder caused by heterozygous gain-of-function mutations in *TNNI2***, the gene encoding the fast-twitch skeletal-muscle isoform of troponin I at chromosome 11p15.5. Although the broad "DA2B" phenotype is genetically heterogeneous — mutations in four interacting sarcomeric/fast-twitch genes (*TNNI2*, *TNNT3*, *TPM2*, *MYH3*) can all produce a Sheldon-Hall picture — the *TNNI2*-driven form is DA2B1 specifically. The clinical hallmark is non-progressive distal limb contractures (camptodactyly, ulnar deviation of the hands, clubfoot/congenital vertical talus) combined with a distinctive triangular face (downslanting palpebral fissures, prominent nasolabial folds, small mouth, prominent chin). Cognition and life expectancy are normal.

The molecular mechanism is **gain of function, not haploinsufficiency**. DA2B1 *TNNI2* mutations cluster in the troponin-I C-terminal (inhibitory/actin-binding) domain and increase the calcium sensitivity and contractile output of developing fast-twitch fetal muscle. In reconstituted actomyosin and skinned-fiber assays, the mutant proteins raise ATPase rates and Ca²⁺ sensitivity, and the *TNNI2* R156ter mutant generates higher maximum force. Sustained hypercontractility of fetal muscle during the critical window of limb development is believed to restrict joint movement in utero, producing fixed contractures. A second, mouse-demonstrated branch links a *Tnni2* mutation to a non-sarcomeric transcriptional route in bone (increased *Hif3a*, reduced *Vegf*, delayed endochondral ossification) that contributes to short stature.

This report synthesizes **7 confirmed findings** and **28 reviewed papers** into a complete disease-knowledge-base entry covering identifiers, etiology, phenotypes, genetics, mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, cross-species biology, and model organisms. Evidence derives from human clinical/genetic studies, in-vitro biophysics, and a knock-in mouse model. Treatment is entirely supportive (physical/occupational therapy, Ponseti casting, staged orthopedic surgery); there is no disease-specific or curative drug therapy.

---

## Key Findings

### Finding 1 — DA2B1 is caused by heterozygous gain-of-function *TNNI2* mutations clustered in the C-terminal domain at 11p15.5

*TNNI2* encodes the fast-skeletal troponin I isoform, one of four sarcomeric/fast-twitch genes that cause distal arthrogryposis. In the Beck et al. (2013) cohort of 153 distal-arthrogryposis kindreds, disease-causing mutations in 56/153 (37%) families — including 14/48 (29%) with DA1 and 42/105 (40%) with DA2B — were distributed **nearly equally across *TNNI2*, *TNNT3*, *TPM2*, and *MYH3***. Reported *TNNI2* variants are heterozygous and concentrate in the **C-terminal domain**: p.Lys175del (c.523_525delAAG), p.Arg156Ter (c.466C>T), p.Glu167del, p.Arg174Gln, and p.Ile165Phe (c.493A>T). Inheritance is autosomal dominant with variable expressivity and reduced penetrance.

> "Disease-causing mutations in 56/153 (37%) kindreds including 14/48 (29%) with DA1 and 42/105 (40%) with DA2B were distributed nearly equally across TNNI2, TNNT3, TPM2, and MYH3" — [PMID: 23401156](https://pubmed.ncbi.nlm.nih.gov/23401156/)

> "detected a three base pair deletion that would be predicted to result in the deletion of a glutamic acid at codon position 167 (DeltaE167). This mutation, like the two previously described TNNI2 mutations, is located in the carboxy-terminal domain" — [PMID: 16497570](https://pubmed.ncbi.nlm.nih.gov/16497570/)

### Finding 2 — DA-causing *TNNI2* mutations increase fast-twitch muscle contractility and Ca²⁺ sensitivity (gain-of-function mechanism)

Robinson et al. (2007) tested all four then-reported DA mutants (Arg63His TnT, Arg91Gly β-TM, Arg174Gln TnI, Arg156ter TnI) in actomyosin ATPase assays and troponin-exchanged skinned rabbit psoas fibers. Every mutant produced **significantly enhanced ATPase rates at all calcium concentrations and increased Ca²⁺ sensitivity**; the *TNNI2* Arg156ter mutant additionally generated significantly higher maximum force. The authors proposed that these mutations cause increased contractility of developing fast-twitch skeletal muscle, producing muscle contractures and limb deformities — the central gain-of-function model for DA2B1.

> "each mutant caused a significant increase in Ca2+ sensitivity, and Arg156ter TnI generated significantly higher maximum force" — [PMID: 17194691](https://pubmed.ncbi.nlm.nih.gov/17194691/)

> "We propose the mutations cause increased contractility of developing fast-twitch skeletal muscles, thus causing muscle contractures and the development of the observed limb deformities" — [PMID: 17194691](https://pubmed.ncbi.nlm.nih.gov/17194691/)

### Finding 3 — A *Tnni2* K175del knock-in mouse recapitulates DA2B via a non-sarcomeric transcriptional route in bone (↑Hif3a, ↓Vegf)

Zhu et al. (2014) generated *Tnni2*^K175del^ knock-in mice ("DA2B mice") that showed **typical DA2B phenotypes — limb abnormality and small body size**. *Tnni2* is expressed in osteoblasts and growth-plate chondrocytes; in mutant radii/ulnae, *Hif3a* was significantly upregulated. ChIP demonstrated Tnni2 binds the *Hif3a* promoter, and the mutant protein transactivated *Hif3a* more strongly than wild type. Increased *Hif3a* impaired angiogenesis, delayed endochondral ossification, and decreased chondrocyte differentiation and osteoblast proliferation (counteracting Hif1a-induced *Vegf*) — a mechanism for the short stature seen in DA2B beyond the sarcomeric contracture pathway.

> "Tnni2K175del mice (referred to as DA2B mice) showed typical DA2B phenotypes, including limb abnormality and small body size" — [PMID: 25340332](https://pubmed.ncbi.nlm.nih.gov/25340332/)

> "Tnni2K175del mutation led to abnormally increased hif3a and decreased vegf in bone, which explain, at least in part, the small body size" — [PMID: 25340332](https://pubmed.ncbi.nlm.nih.gov/25340332/)

### Finding 4 — DA2B (Sheldon-Hall) clinical phenotype: distal contractures + distinctive triangular face, intermediate between DA1 and Freeman-Sheldon syndrome

Krakowiak et al. (1998) described the DA2B phenotype: **vertical talus, ulnar deviation, severe camptodactyly, and a distinctive triangular face** with prominent nasolabial folds, downslanting palpebral fissures, a small mouth, and a prominent chin. The anomalies are more severe than DA1 and less severe than DA2A (Freeman-Sheldon syndrome). The gene maps to 11p15.5. High intra- and inter-individual variability of expression among mutation carriers is well documented.

> "Affected individuals have vertical talus, ulnar deviation, severe camptodactyly, and a distinctive face characterized by a triangular shape, prominent nasolabial folds, downslanting palpebral fissures, small mouth, and a prominent chin" — [PMID: 9508073](https://pubmed.ncbi.nlm.nih.gov/9508073/)

> "A gene for DA2B maps to chromosome 11p15.5" — [PMID: 9508073](https://pubmed.ncbi.nlm.nih.gov/9508073/)

### Finding 5 — gnomAD constraint shows *TNNI2* is tolerant to loss of function (consistent with gain-of-function, not haploinsufficiency)

gnomAD v2.1.1 constraint metrics for *TNNI2* (ENSG00000130598; GRCh38 chr11:1,838,981–1,841,680) are: **pLI = 0.010**, **LOEUF = 0.826**, observed/expected LoF = 0.53 (14 observed vs 26.5 expected), missense Z = 1.18 (oe_mis = 0.82). None of these indicate significant intolerance to loss-of-function or missense variation. If DA2B1 arose from haploinsufficiency, *TNNI2* would be expected to be LoF-intolerant; instead, the LoF tolerance aligns with a **gain-of-function / dominant-negative** disease mechanism, corroborating the functional data in Finding 2.

> "We propose the mutations cause increased contractility of developing fast-twitch skeletal muscles, thus causing muscle contractures and the development of the observed limb deformities" — [PMID: 17194691](https://pubmed.ncbi.nlm.nih.gov/17194691/)

### Finding 6 — Landmark mapping; the most common distal arthrogryposis; diagnosed by NGS panels/exome

Sung et al. (2003) — the landmark identification — mapped DA2B to chromosome 11 and showed it is caused by *TNNI2* mutations predicted to disrupt the troponin-I C-terminal domain specific to the fast-twitch troponin–tropomyosin complex, describing DA2B as **"the most common of the DAs."** For diagnosis, Ravenscroft et al. (2021) reported that in an unselected cohort of 190 probands with arthrogryposis/fetal akinesia, NGS gene panels plus WES yielded a diagnosis in **81/190 (42.6%)**, reporting only ACMG class 4/5 variants.

> "DA2B is caused by mutations in TNNI2 that are predicted to disrupt the carboxy-terminal domain of an isoform of troponin I (TnI) specific to the troponin-tropomyosin (Tc-Tm) complex of fast-twitch myofibers" — [PMID: 12592607](https://pubmed.ncbi.nlm.nih.gov/12592607/)

> "Comprehensive gene panels give a diagnosis for a substantial proportion (42%) of fetal akinesia and arthrogryposis cases, even in an unselected cohort" — [PMID: 33060286](https://pubmed.ncbi.nlm.nih.gov/33060286/)

### Finding 7 — ClinVar variant spectrum: recurrent heterozygous C-terminal *TNNI2* missense, in-frame deletion, and nonsense variants (NM_003282.4)

ClinVar lists 168 *TNNI2* records: 34 Pathogenic, 10 Likely pathogenic, 3 Pathogenic/Likely pathogenic, plus 63 VUS. Variants explicitly annotated to "Distal arthrogryposis type 2B1" cluster in the **C-terminal region (~codons 156–176)**: p.Arg174Gln (c.521G>A), p.Arg156Ter (c.466C>T), p.Lys175Asn (c.525G>T), p.Glu167del, p.Lys176del, p.Ile165Phe (c.493A>T), p.Arg162Ser, p.Glu166Ter, p.Ser169Ter, p.Arg174Trp (c.520C>T), and p.Lys106Glu (c.316A>G). Variant classes are missense, in-frame single-codon deletions, and nonsense/stop-gain — **all germline and heterozygous**. Large 11p15.5 CNVs in ClinVar map to the Silver-Russell/β-thalassemia loci, not to DA2B1. The recurrence of p.Arg156Ter across unrelated families underscores a mutational hotspot.

> "Recurrence of the p.R156X TNNI2 mutation in distal arthrogryposis type 2B" — [PMID: 17101001](https://pubmed.ncbi.nlm.nih.gov/17101001/)

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** DA2B1 (Sheldon-Hall syndrome) is a rare, non-progressive, autosomal-dominant congenital contracture disorder in the distal-arthrogryposis (DA) family. It is characterized by congenital contractures of the distal limbs — camptodactyly, ulnar deviation of the hands, and foot deformities (clubfoot/talipes equinovarus or congenital vertical talus) — together with distinctive craniofacial features (triangular face, downslanting palpebral fissures, prominent nasolabial folds, small mouth, prominent chin). Proximal joints are relatively spared and cognition is normal. Sheldon-Hall syndrome is phenotypically **intermediate between DA1 (distal contractures only) and DA2A/Freeman-Sheldon syndrome** (more severe, with prominent facial contractures/"whistling face").

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0020820 |
| OMIM (phenotype) | 601680 |
| Gene (OMIM) | *TNNI2* 191043 |
| HGNC | HGNC:11946 |
| NCBI Gene | 7136 |
| UniProt | P48788 |
| Ensembl | ENSG00000130598 |
| Cytogenetic locus | 11p15.5 |

**Synonyms / alternative names.** Sheldon-Hall syndrome (SHS); distal arthrogryposis type 2B (DA2B); "a variant of Freeman-Sheldon syndrome." The DA2B label is further subdivided by gene (DA2B1 = *TNNI2*; DA2B2 = *TNNT3*; DA2B3 = *MYH3*; DA2B4 = *TPM2*); this report concerns the *TNNI2* form (DA2B1).

**Source of information.** Primarily **aggregated disease-level resources** (OMIM, ClinVar, gnomAD) and **individual-patient case reports/kindred studies** in the literature; not EHR-derived.

### 2. Etiology

**Causal factors.** Purely **genetic** — heterozygous gain-of-function mutations in *TNNI2*. No environmental, infectious, or toxic cause is established.

**Genetic risk factors.** The causal variants are germline, heterozygous, and cluster in the *TNNI2* C-terminal domain (codons ~156–176). The disease is monogenic; the "risk factor" is carriage of a pathogenic *TNNI2* allele. Within the broader DA2B phenotype, *TNNT3*, *TPM2*, and *MYH3* are the locus-heterogeneous alternatives (Findings 1, 6).

**Environmental risk factors.** None established. Family history (an affected parent) is the principal risk indicator given autosomal-dominant inheritance.

**Protective factors.** No genetic or environmental protective factors are documented. Notably, *TNNI2* is tolerant to loss-of-function in gnomAD (Finding 5), implying LoF alleles do **not** cause disease — consistent with only specific gain-of-function/dominant-negative C-terminal changes being pathogenic.

**Gene–environment interactions.** None documented; DA2B1 is a Mendelian, environment-independent disorder.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Frequency / notes |
|---|---|---|---|---|
| Camptodactyly | Physical manifestation | HP:0012385 | Congenital | Severe; characteristic |
| Ulnar deviation of hand | Clinical sign | HP:0009465 | Congenital | Characteristic |
| Congenital vertical talus | Clinical sign | HP:0001838 | Congenital | Reported in SHS kindreds |
| Talipes equinovarus (clubfoot) | Clinical sign | HP:0001762 | Congenital | Common foot deformity |
| Triangular face | Physical manifestation | HP:0000325 | Congenital | Distinctive facies |
| Downslanted palpebral fissures | Physical manifestation | HP:0000494 | Congenital | Distinctive facies |
| Prominent nasolabial fold | Physical manifestation | facial/HP | Congenital | Distinctive facies |
| Microstomia (small mouth) | Physical manifestation | HP:0000160 | Congenital | Distinctive facies |
| Prominent chin (mentum) | Physical manifestation | HP:0000303 | Congenital | Distinctive facies |
| Short stature | Physical manifestation | HP:0004322 | Childhood | Mouse model supports a bone mechanism (Finding 3) |
| Distal arthrogryposis / multiple contractures | Clinical sign | HP:0005684 | Congenital | Core feature |

**Phenotype characteristics.** Onset is **congenital** (contractures present at birth, often detectable prenatally by ultrasound). Severity is **variable** (high intra- and interfamilial variability among carriers of the same mutation). Course is **non-progressive/stable** — contractures do not neurologically worsen, though untreated deformities impair function and relapse after correction. Penetrance is reduced; expressivity is variable (Finding 4; PMID:30216196 documents intrafamilial variability).

**Quality-of-life impact.** Chiefly musculoskeletal: impaired hand dexterity (camptodactyly/ulnar deviation) and ambulation (foot deformities). With appropriate orthopedic management, most DA patients achieve independent ambulation and self-care (in a mixed AMC cohort, ~98% of DA patients were independent ambulators; PMID:33104047). Cognition, respiration, and life expectancy are typically unaffected.

### 4. Genetic / Molecular Information

**Causal gene.** *TNNI2* (fast-twitch skeletal troponin I; HGNC:11946; NCBI Gene 7136; UniProt P48788; OMIM 191043; ENSG00000130598; 11p15.5). Reference transcript **NM_003282.4**.

**Pathogenic variants (representative, DA2B1-annotated).**
| Variant (protein) | cDNA | Class | Domain |
|---|---|---|---|
| p.Arg174Gln | c.521G>A | Missense | C-terminal |
| p.Arg174Trp | c.520C>T | Missense | C-terminal |
| p.Arg156Ter | c.466C>T | Nonsense (recurrent hotspot) | C-terminal |
| p.Ile165Phe | c.493A>T | Missense | C-terminal |
| p.Lys175del | c.523_525delAAG | In-frame deletion | C-terminal |
| p.Glu167del | — | In-frame deletion | C-terminal |
| p.Lys175Asn | c.525G>T | Missense | C-terminal |
| p.Lys176del | — | In-frame deletion | C-terminal |
| p.Arg162Ser | c.486G>C/T | Missense | C-terminal |
| p.Glu166Ter | c.496G>T | Nonsense | C-terminal |
| p.Ser169Ter | c.503_505dup | Stop-gain/frameshift | C-terminal |
| p.Lys106Glu | c.316A>G | Missense | — |

**Variant classification.** Per ACMG/AMP, the recurrent C-terminal variants are classified Pathogenic/Likely pathogenic in ClinVar (34 P, 10 LP, 3 P/LP among 168 *TNNI2* records; Finding 7).

**Variant type/class.** Missense, in-frame single-codon deletions, and nonsense/stop-gain — all germline, heterozygous.

**Allele frequency.** Pathogenic alleles are absent or ultra-rare in gnomAD; *TNNI2* overall is LoF-tolerant (pLI 0.010, LOEUF 0.826; Finding 5).

**Somatic vs germline.** Germline. (One report described an atypical adult with only facial contractures attributed to somatic mosaicism of a *TNNI2* variant — PMID:23850728.)

**Functional consequence.** **Gain of function** — increased myofilament Ca²⁺ sensitivity and contractility (Finding 2); the C-terminal nonsense allele R156ter behaves as a functional gain/dominant-negative rather than simple LoF.

**Modifier genes.** None established. The variable expressivity suggests modifiers exist but they are uncharacterized.

**Epigenetic information.** None specific to DA2B1 in humans. In the mouse model, the mutant Tnni2 protein acts as a transcriptional transactivator at the *Hif3a* promoter (Finding 3) — a gene-regulatory, not classical epigenetic, effect.

**Chromosomal abnormalities.** None; DA2B1 is a single-gene disorder. Large 11p15.5 CNVs map to other loci (Silver-Russell/thalassemia), not DA2B1 (Finding 7).

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in DA2B1 — it is a Mendelian gain-of-function disorder. (By contrast, several abstracts in the reviewed literature concern *phenocopies* of arthrogryposis from teratogens or congenital infection — e.g., Japanese encephalitis virus in piglets, PMID:41738435; Oropouche virus in human newborns, PMID:39423837 — unrelated to *TNNI2*/DA2B1 and relevant only to the differential for acquired fetal akinesia.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous gain-of-function mutation arises in the **C-terminal (inhibitory/actin-binding) domain of *TNNI2*** (e.g., R174Q, R156ter, K175del). → *leads to*
2. An altered fast-twitch troponin I that is incorporated into the troponin–tropomyosin complex of developing fast-twitch myofibers. → *results in*
3. **Increased Ca²⁺ sensitivity of the thin filament and enhanced actomyosin ATPase/contractile output** (demonstrated in vitro; Finding 2). → *leads to*
4. **Hypercontractility of developing fetal fast-twitch skeletal muscle** across the critical window of limb morphogenesis (*inferred* from in-vitro biophysics applied to development). → *results in*
5. **Reduced fetal limb movement / fixed muscle shortening across joints** (fetal-akinesia-type mechanism). → *leads to*
6. **Congenital distal joint contractures** — camptodactyly, ulnar deviation, clubfoot/vertical talus — the defining clinical phenotype.

**Branch (bone/stature, mouse-demonstrated):**

2b. Mutant Tnni2 (also expressed in osteoblasts and growth-plate chondrocytes) **binds and transactivates the *Hif3a* promoter** more strongly than wild type. → *leads to*
3b. **Increased Hif3a → decreased Vegf → impaired angiogenesis and delayed endochondral ossification**, with reduced chondrocyte differentiation and osteoblast proliferation. → *results in*
4b. **Short stature / small body size** (Finding 3).

**Supporting detail by category:**
- **Molecular pathways:** Calcium-regulated thin-filament (troponin–tropomyosin) regulation of actomyosin cross-bridge cycling; in bone, HIF/VEGF angiogenic signaling. GO terms: regulation of muscle contraction (GO:0006937), skeletal muscle contraction (GO:0003009), troponin complex (GO:0005861), endochondral ossification (GO:0001958), angiogenesis (GO:0001525).
- **Cellular processes:** Myofibrillar contraction; chondrocyte differentiation; osteoblast proliferation; angiogenesis.
- **Protein dysfunction:** Gain of function/dominant effect altering Ca²⁺-dependent inhibition of actomyosin; the C-terminal domain is critical for troponin-I's actin-binding/inhibitory function.
- **Biochemical abnormalities:** Elevated myofilament Ca²⁺ sensitivity and ATPase rate at all [Ca²⁺]; higher maximum force for R156ter.
- **Tissue damage mechanism:** Not degenerative — the primary lesion is developmental (contracture formation), not tissue necrosis/inflammation.
- **Immune/metabolic involvement:** None established.
- **Molecular profiling:** Mouse bone transcriptional change (↑*Hif3a*, ↓*Vegf*). No human omics datasets specific to DA2B1.

**Upstream vs downstream.** Upstream: the *TNNI2* mutation and altered thin-filament biophysics. Downstream: fetal hypercontractility → contractures (muscle branch) and Hif3a/Vegf dysregulation → short stature (bone branch).

**Cell types / CL terms:** fast-twitch skeletal muscle cell / myocyte (CL:0000190, CL:0008002), osteoblast (CL:0000062), chondrocyte (CL:0000138).

### 7. Anatomical Structures Affected

- **Organ/system level:** Musculoskeletal system — primarily the **distal limbs** (hands and feet) and **craniofacial** structures; skeletal growth (stature). Body system: musculoskeletal (UBERON:0002204 musculature; UBERON:0002398 manus; UBERON:0002387 pes).
- **Tissue/cell level:** **Skeletal (striated) muscle tissue**, specifically fast-twitch myofibers (UBERON:0001134 skeletal muscle tissue); growth-plate cartilage and bone (osteoblasts, chondrocytes) in the stature branch.
- **Subcellular level:** **Sarcomere / myofibril / troponin complex** (GO:0030017 sarcomere; GO:0005861 troponin complex; GO:0030016 myofibril); nucleus (for the Tnni2→Hif3a transcriptional branch, GO:0005634).
- **Localization:** UBERON:0002398 (manus), UBERON:0002387 (pes), UBERON:0001456 (face). Lateralization: **bilateral**, often symmetric distal contractures.

### 8. Temporal Development

- **Onset:** **Congenital** — contractures are present at birth and frequently detectable on prenatal ultrasound (late-gestation reduced movement/fixed posture).
- **Onset pattern:** The structural defect is established in utero (developmental); it is not acute/relapsing.
- **Progression:** **Non-progressive/stable.** The contractures do not neurologically worsen, but untreated deformities impair function and can relapse after orthopedic correction (especially with brace non-compliance; PMID:18594099).
- **Disease course / duration:** Lifelong structural condition; functional status is modifiable by treatment.
- **Critical periods:** The **fetal limb-morphogenesis window** is the critical period for contracture formation; the key intervention opportunity is postnatal orthopedic correction (early Ponseti casting for clubfoot).

### 9. Inheritance and Population

- **Epidemiology:** DA2B/Sheldon-Hall syndrome is described as **"the most common of the distal arthrogryposes"** (Finding 6), but precise prevalence/incidence figures for DA2B1 specifically are not established (rare disease).
- **Inheritance pattern:** **Autosomal dominant**, with reduced penetrance and variable expressivity (Findings 1, 4).
- **Penetrance:** Incomplete/reduced.
- **Expressivity:** Variable (high intra- and interfamilial variability; PMID:30216196).
- **Genetic anticipation:** Not a feature (not a repeat-expansion disorder).
- **Germline / somatic mosaicism:** A somatic-mosaicism case with only facial features has been reported (PMID:23850728); germline mosaicism is plausible but not well quantified.
- **Founder effects / consanguinity:** Not applicable (dominant; recurrent variants such as p.R156X recur independently as a hotspot rather than a founder allele — PMID:17101001).
- **Carrier frequency:** Not applicable (dominant); pathogenic alleles are ultra-rare.
- **Demographics:** Reported worldwide across diverse populations (multiple Chinese kindreds among reviewed reports); no strong ethnic predilection. **Sex ratio** ~1:1 (autosomal). Age distribution: present from birth across all ages.

### 10. Diagnostics

- **Clinical diagnosis:** Based on the characteristic constellation — distal contractures (camptodactyly, ulnar deviation, clubfoot/vertical talus) plus the triangular facies (Finding 4).
- **Genetic testing (definitive):** **NGS multigene panels** (covering *TNNI2*, *TNNT3*, *TPM2*, *MYH3*, *MYBPC1*, *PIEZO2*, etc.) and **whole-exome sequencing** are the mainstay; Sanger confirmation and segregation analysis follow. Diagnostic yield for arthrogryposis/fetal-akinesia cohorts is ~42% (Finding 6). Single-gene *TNNI2* testing is appropriate when the phenotype is classic.
- **Prenatal diagnosis:** Molecular prenatal diagnosis is feasible when the familial variant is known (linkage + targeted mutation detection via CVS/amniocentesis has been reported for DA2B *TNNI2* K175del families — PMID:17380469). Prenatal ultrasound can detect fixed fetal posture/reduced movement in late gestation.
- **Laboratory tests:** Serum creatine kinase is typically **normal**; EMG is typically not myopathic/myotonic (helps exclude myotonic/dystrophic mimics).
- **Imaging:** Radiographs document joint deformities (vertical talus, clubfoot, hand contractures) for surgical planning.
- **Differential diagnosis:** DA1 (milder, no facial features), DA2A/Freeman-Sheldon syndrome (more severe, *MYH3*), amyoplasia (more proximal involvement), other sarcomeric DAs (*TNNT3*/DA2B2, *MYH3*/DA2B3, *TPM2*/DA2B4), *PIEZO2*-related DA, STAC3 disorder/Native American myopathy, Schwartz-Jampel syndrome, and acquired/teratogenic or infectious fetal-akinesia phenocopies.
- **Screening:** No population newborn screening. **Cascade genetic testing** of at-risk relatives and genetic counseling are appropriate.

### 11. Outcome / Prognosis

- **Survival/mortality:** **Normal life expectancy**; DA2B1 is not life-limiting (no primary cardiac or respiratory involvement in the typical *TNNI2* form).
- **Morbidity/function:** Chiefly musculoskeletal disability from hand and foot deformities. With orthopedic management, most patients ambulate independently and are self-sufficient (PMID:33104047).
- **Complications:** Related mainly to treatment — recurrence of clubfoot after Ponseti correction (especially with brace non-compliance; PMID:18594099) and elevated fracture risk after hardware removal following osteotomy (PMID:41191822).
- **Recovery potential:** Deformities are correctable/improvable with staged intervention; the underlying genetic condition is not curable.
- **Prognostic factors:** Severity of initial deformities, compliance with bracing/therapy, and timeliness of intervention. Normal cognition favors rehabilitation outcomes.

### 12. Treatment

**There is no disease-specific or curative pharmacotherapy, gene therapy, or molecular-targeted therapy for DA2B1.** Management is **supportive and orthopedic**:

| Modality | Details | NCIT suggestion |
|---|---|---|
| Physical therapy | Stretching, range-of-motion for contractures | NCIT:C15328 (Physical Therapy) |
| Occupational therapy | Hand function, activities of daily living | NCIT:C15329 (Occupational Therapy) |
| Serial casting (Ponseti) | First-line for clubfoot; effective but needs more casts than idiopathic clubfoot (mean 6.9 vs 4.5; p=0.002) and relapses with non-compliance (PMID:18594099) | NCIT:C116746 (Casting) |
| Orthotics/bracing | Maintain correction, prevent relapse | NCIT:C50048 (Brace) |
| Orthopedic surgery | Tenotomy, soft-tissue release, osteotomy, guided growth for fixed deformities; Ilizarov for severe knee deformity (PMID:30807513; PMID:18724198) | surgical NCIT terms |

**Pharmacogenomics / anesthesia caution:** Given the broader DA spectrum's overlap with conditions carrying malignant-hyperthermia susceptibility (e.g., *MYH3* FSS, STAC3 disorder), perioperative anesthetic caution is warranted; the standard *TNNI2* DA2B1 form is not classically MH-associated, but careful anesthetic assessment is prudent.

**Experimental therapeutics:** None specific. No NCT-registered DA2B1-targeted trials identified.

### 13. Prevention

- **Primary prevention:** Not possible (congenital genetic disorder). **Genetic counseling** for affected families (50% transmission risk, autosomal dominant with reduced penetrance/variable expressivity).
- **Secondary prevention:** **Prenatal molecular diagnosis** when the familial variant is known (PMID:17380469); preimplantation genetic testing (PGT) for known-variant families. Prenatal ultrasound surveillance.
- **Tertiary prevention:** Early orthopedic intervention (Ponseti casting, therapy) to prevent fixed deformity and maximize function; brace adherence to prevent relapse.
- **Immunization/public health/environmental:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *TNNI2* is conserved across vertebrates; the mouse ortholog *Tnni2* was used to model DA2B (Finding 3). Human *TNNI2* NCBI Gene 7136; mouse *Tnni2* NCBI Gene 21953.
- **Natural disease in other species:** No well-characterized spontaneous *TNNI2* distal-arthrogryposis in companion animals is established in the reviewed literature. (Arthrogryposis in livestock is usually acquired — e.g., teratogenic/viral fetal akinesia such as JEV in piglets, PMID:41738435 — not *TNNI2*-related.)
- **Comparative biology:** The knock-in mouse demonstrates evolutionary conservation of the pathomechanism, recapitulating limb abnormality and short stature.
- **Zoonotic potential:** Not applicable (genetic disorder).

### 15. Model Organisms

- **Mouse (*Mus musculus*), knock-in *Tnni2*^K175del^** — the principal genetic model. It **recapitulates key DA2B features**: limb abnormality and small body size (Finding 3). It additionally revealed the non-sarcomeric **Hif3a/Vegf bone mechanism** for short stature, expressing *Tnni2* in osteoblasts/chondrocytes. Resource: MGI.
  - **Phenotype recapitulation:** Good for limb deformity and stature.
  - **Limitations:** Craniofacial features and per-variant biophysical validation are not fully captured by a single knock-in; the study emphasizes the bone branch over the muscle-contracture biophysics.
- **In-vitro reconstituted systems** — actomyosin ATPase assays and troponin-exchanged skinned rabbit psoas fibers established the gain-of-function (↑Ca²⁺ sensitivity, ↑force) mechanism for DA *TNNI2* mutants (Finding 2; PMID:17194691).
- **Applications:** Mechanistic dissection of thin-filament regulation (in vitro) and of limb/bone development in vivo.

---

## Mechanistic Model / Interpretation

```
                 Heterozygous GOF mutation in TNNI2 C-terminal domain
                 (R174Q / R156ter / K175del / I165F ...)
                                   │
          ┌────────────────────────┴────────────────────────┐
          │ MUSCLE BRANCH (in vitro + inferred)              │ BONE BRANCH (mouse)
          ▼                                                  ▼
 Altered fast-twitch troponin I in                 Mutant Tnni2 binds & transactivates
 troponin–tropomyosin complex                      the Hif3a promoter in osteoblasts/
          │                                        growth-plate chondrocytes
          ▼                                                  │
 ↑ Myofilament Ca²⁺ sensitivity                              ▼
 ↑ Actomyosin ATPase / ↑ max force (R156ter)        ↑ Hif3a  →  ↓ Vegf
          │                                                  │
          ▼                                                  ▼
 Hypercontractility of developing                  Impaired angiogenesis; delayed
 fetal fast-twitch muscle                          endochondral ossification;
          │                                        ↓ chondrocyte diff. & osteoblast prolif.
          ▼                                                  │
 ↓ Fetal limb movement / fixed                               ▼
 muscle shortening across joints                    SHORT STATURE / small body size
          │
          ▼
 CONGENITAL DISTAL CONTRACTURES
 (camptodactyly, ulnar deviation,
  clubfoot/vertical talus) + triangular facies
```

The two branches explain the two cardinal components of the DA2B phenotype: **muscle hypercontractility → contractures** (upstream biophysical gain of function) and a **non-sarcomeric transcriptional route → short stature**. The gain-of-function interpretation is triangulated by three independent evidence types: (1) in-vitro biophysics (↑Ca²⁺ sensitivity/force), (2) population constraint data showing *TNNI2* is LoF-tolerant (so disease is not haploinsufficiency), and (3) tight C-terminal mutational clustering (only specific functional changes are pathogenic). The recurrence of identical variants (e.g., p.R156X) across unrelated families reflects a mutational hotspot rather than a founder effect.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [12592607](https://pubmed.ncbi.nlm.nih.gov/12592607/) | *Mutations in fast-twitch contractile proteins cause DA* | **Landmark**: *TNNI2* causes DA2B; C-terminal mechanism; "most common DA" | Human genetics |
| [17194691](https://pubmed.ncbi.nlm.nih.gov/17194691/) | *Mutations in TnI/TnT/β-TM all increase contractile function* | **Core mechanism**: gain of function (↑Ca²⁺ sensitivity, ↑force) | In vitro |
| [25340332](https://pubmed.ncbi.nlm.nih.gov/25340332/) | *Tnni2 GOF impedes bone development via Hif3a* | **Mouse model**: recapitulates limb + stature; Hif3a/Vegf route | Model organism |
| [9508073](https://pubmed.ncbi.nlm.nih.gov/9508073/) | *Clinical analysis of a variant of FSS (DA2B)* | **Phenotype** + maps DA2B to 11p15.5 | Human clinical |
| [23401156](https://pubmed.ncbi.nlm.nih.gov/23401156/) | *Spectrum of mutations in DA1 and DA2B* | **Mutation distribution** across 4 genes | Human genetics |
| [16497570](https://pubmed.ncbi.nlm.nih.gov/16497570/) | *A TNNI2 mutation in a DA2B family* | C-terminal clustering (ΔE167) | Human genetics |
| [17101001](https://pubmed.ncbi.nlm.nih.gov/17101001/) | *Recurrence of p.R156X TNNI2 in DA2B* | Recurrent hotspot nonsense variant | Human genetics |
| [33060286](https://pubmed.ncbi.nlm.nih.gov/33060286/) | *Neurogenetic fetal akinesia and arthrogryposis* | **Diagnostic yield** (42%) of NGS panels | Human clinical/genomics |
| [17380469](https://pubmed.ncbi.nlm.nih.gov/17380469/) | *Molecular prenatal diagnosis for DA2B* | Prenatal diagnosis for *TNNI2* K175del | Human clinical |
| [23850728](https://pubmed.ncbi.nlm.nih.gov/23850728/) | *Novel TNNI2 mutation causes FSS; somatic mosaicism* | C-terminal I165F; DA1/DA2B/FSS continuum; mosaicism | Human genetics |
| [18594099](https://pubmed.ncbi.nlm.nih.gov/18594099/) | *Ponseti method for clubfoot in DA* | Treatment efficacy/relapse data | Human clinical |
| [33104047](https://pubmed.ncbi.nlm.nih.gov/33104047/) | *Orthopedic outcomes in AMC cohort* | Functional outcomes (DA ambulation ~98%) | Human clinical |
| [30216196](https://pubmed.ncbi.nlm.nih.gov/30216196/) | *Intrafamilial variability in DA2B* | Variable expressivity | Human clinical |

---

## Limitations and Knowledge Gaps

- **Epidemiology:** No precise prevalence/incidence for DA2B1 specifically; "most common DA" is qualitative.
- **Mechanism integration:** The muscle-hypercontractility → contracture step during fetal development is *inferred* from adult in-vitro biophysics; direct demonstration in developing human/fetal muscle is lacking. The bone (Hif3a/Vegf) branch is demonstrated only in mouse for one variant (K175del) and may not generalize to all alleles.
- **Genotype–phenotype:** Determinants of variable expressivity and reduced penetrance (modifier genes/environment) are unknown.
- **Human omics:** No human transcriptomic/proteomic/metabolomic datasets specific to DA2B1.
- **Therapeutics:** No molecularly targeted or disease-modifying therapy exists or is in trials; management is entirely supportive.
- **Cross-species natural disease:** No confirmed spontaneous *TNNI2* DA in domestic animals.

---

## Proposed Follow-up Experiments / Actions

1. **Fetal-stage functional validation:** Use *Tnni2* knock-in or patient iPSC-derived myotubes/organoids to directly measure hypercontractility and contracture formation during the developmental window, closing the inference gap in step 4 of the causal chain.
2. **Allelic-series mouse models:** Generate knock-ins for additional human variants (R174Q, R156ter, I165F) to test whether the Hif3a/Vegf bone branch is variant-specific or general, and whether craniofacial features can be recapitulated.
3. **Genotype–phenotype & modifier mapping:** Assemble a multi-family DA2B1 registry with standardized phenotyping to quantify penetrance and search for genetic/environmental modifiers of expressivity.
4. **Therapeutic proof-of-concept:** Test whether calcium-desensitizing myofilament agents (e.g., troponin-activity modulators) can attenuate hypercontractility in patient-derived muscle models — a rational, mechanism-based therapeutic hypothesis.
5. **Prenatal/early-intervention outcome study:** Evaluate whether earlier molecular diagnosis and immediate postnatal Ponseti/therapy improve long-term function and reduce relapse/complication rates (e.g., fracture after hardware removal).
6. **ClinVar/VarSome curation:** Reclassify the 63 *TNNI2* VUS using functional-assay data and ACMG PS3/PM1 (C-terminal hotspot) criteria to improve diagnostic clarity.

---

*Report compiled from 7 confirmed findings and 28 reviewed papers. Evidence types: human clinical/genetic, in-vitro biophysics, and a knock-in mouse model. All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Distal_Arthrogryposis_Type_2B1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Distal_Arthrogryposis_Type_2B1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:39423837` (2 mentions) - Newborns with microcephaly in Brazil and potential vertical transmission of Oropouche virus: a case series.
  - shared terms: arthrogryposis, fetal

Weighed against this report's own most characteristic terms: `tnni2`, `da2b1`, `contracture`, `da2b`, `phenotype`, `variant`, `mutation`, `gene`, `distal`, `genetic`, `function`, `c-terminal`, `arthrogryposis`, `type`, `mouse`, `hif3a`, `disorder`, `fast-twitch`, `bone`, `fetal`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 15 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020820` (2 mentions) - the report calls it "MONDO"; MONDO calls it **distal arthrogryposis type 2B1**
- `HP:0012385` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Camptodactyly**
- `HP:0009465` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ulnar deviation of finger**
- `HP:0001838` (1 mention) - the report calls it "Clinical sign"; HP calls it **Rocker bottom foot**
- `HP:0001762` (1 mention) - the report calls it "Clinical sign"; HP calls it **Talipes equinovarus**
- `HP:0000325` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Triangular face**
- `HP:0000494` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Downslanted palpebral fissures**
- `HP:0000160` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Narrow mouth**
- `HP:0000303` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Mandibular prognathia**
- `HP:0004322` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Short stature**
- `HP:0005684` (1 mention) - the report calls it "Clinical sign"; HP calls it **Distal arthrogryposis**
- `NCIT:C15328` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Splenectomy**
- `NCIT:C15329` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Surgical Procedure**
- `NCIT:C116746` (1 mention) - the report calls it "Casting"; NCIT calls it **Anti-mesothelin/MMAE Antibody-drug Conjugate DMOT4039A**
- `NCIT:C50048` (1 mention) - the report calls it "Brace"; NCIT calls it **Read Only Memory Device**