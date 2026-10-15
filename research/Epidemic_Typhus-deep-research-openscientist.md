---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T00:14:22.335014'
end_time: '2026-09-25T00:30:13.574693'
duration_seconds: 951.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Epidemic Typhus
  mondo_id: MONDO:0019362
  category: Infectious Disease
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
citation_count: 32
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 22
  relevance_assessed: 32
  on_topic: 21
  off_topic: 2
  off_topic_references:
  - PMID:35082036
  - PMID:36406066
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 44
  verified: 43
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 38
  labels_matching: 23
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0002383
    reported_labels:
    - Severe/CNS cases
    ontology_label: Infectious encephalitis
  - term_id: HP:0012819
    reported_labels:
    - Severe cases
    ontology_label: Myocarditis
  - term_id: HP:0006515
    reported_labels:
    - Severe cases
    ontology_label: Interstitial pneumonitis
  - term_id: HP:0001919
    reported_labels:
    - Severe cases
    ontology_label: Acute kidney injury
  - term_id: HP:0002615
    reported_labels:
    - Severe/terminal
    ontology_label: Hypotension
  - term_id: NCIT:C692
    reported_labels:
    - Doxycycline
    ontology_label: Nimodipine
  - term_id: NCIT:C376
    reported_labels:
    - Chloramphenicol
    ontology_label: Cisplatin
  - term_id: NCIT:C15844
    reported_labels:
    - Antibiotic Therapy
    ontology_label: Protein/Amino Acid Nutrition Research, Animal
  - term_id: NCIT:C15311
    reported_labels:
    - Vaccination
    ontology_label: Quality Control
  - term_id: NCIT:C16781
    reported_labels:
    - Sanitation
    ontology_label: Laryngoscopy
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Epidemic_Typhus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Epidemic_Typhus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epidemic Typhus
- **MONDO ID:** MONDO:0019362 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Epidemic Typhus** covering all of the
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

# Epidemic Typhus (MONDO:0019362): A Comprehensive Disease Characteristics Report

## Summary

**Epidemic typhus** is an acute, severe, potentially fatal febrile illness caused by *Rickettsia prowazekii*, an obligate intracellular Gram-negative bacterium of the typhus group of *Rickettsia*. Its defining epidemiological feature is human-to-human transmission mediated by the human body louse, *Pediculus humanus corporis*: humans acquire infection not from the louse bite itself, but when louse feces laden with *R. prowazekii* are inoculated into skin abrasions, scratch wounds, or mucosal surfaces. Because the vector thrives under conditions of poverty, cold climate, crowding, poor hygiene, war, famine, and mass displacement, epidemic typhus is historically a disease of social collapse and remains a threat wherever these conditions recur. Humans are the principal reservoir, and the organism can persist latently for years before reactivating as **Brill–Zinsser disease**, a milder recrudescent form that can reseed epidemics where lice are present. A sylvatic (zoonotic) cycle exists in the eastern United States involving the southern flying squirrel *Glaucomys volans*.

Mechanistically, the disease is unified by a single pathological process: **rickettsial vasculitis**. After inoculation, *R. prowazekii* disseminates hematogenously and preferentially invades vascular **endothelial cells** (and, secondarily, macrophages), replicating free in the host cytoplasm. To survive, it parasitizes host energy directly through an ATP/ADP translocase (Tlc1) because its reductive genome lacks glycolysis. Endothelial infection triggers vascular inflammation, loss of vascular integrity, and increased permeability, producing widespread small-vessel vasculitis with perivascular mononuclear "typhus nodules," microthrombi, and vascular leak. The downstream consequence is multiorgan injury — rash, headache/encephalitis, myocarditis, pneumonitis, acute kidney injury, and hypotension/shock. Protective immunity is cell-mediated, dominated by IFN-γ and CD8+ cytotoxic T lymphocytes; humoral antibody alone is insufficient once infection is established.

Clinically, epidemic typhus presents after a ~1–2 week incubation as an acute monophasic illness with high fever, severe headache, and myalgia, classically accompanied by a centrifugal maculopapular/petechial rash — though the rash is frequently absent (e.g., only ~25% of cases in a Burundi outbreak). Diagnosis rests primarily on serology (indirect immunofluorescence assay is the reference test), with the important caveat that antibodies are absent early. **Doxycycline** is the treatment of choice, producing rapid defervescence, and delayed empiric therapy risks severe sequelae and death. There is **no currently licensed rickettsial vaccine**; prevention depends on louse control and sanitation. *R. prowazekii* is classified as a **CDC Category B bioterrorism agent** because it is stable in dried louse feces and transmissible by aerosol. This report synthesizes 10 confirmed findings drawn from 39 reviewed papers across all requested disease-characteristic domains.

---

## 1. Disease Information

Epidemic typhus (also called **louse-borne typhus**, **classic typhus**, **jail fever**, **camp fever**, **war fever**, and **exanthematic typhus**) is one of the oldest recorded pestilential diseases of humankind [PMID: 27726780](https://pubmed.ncbi.nlm.nih.gov/27726780/). It is an acute systemic infection caused by *Rickettsia prowazekii*. The recrudescent form is termed **Brill–Zinsser disease**.

**Key identifiers:**
- **MONDO:** MONDO:0019362
- **MeSH:** Typhus, Epidemic Louse-Borne
- **ICD-10:** A75.0 (Epidemic louse-borne typhus due to *Rickettsia prowazekii*); A75.1 (recrudescent typhus / Brill–Zinsser disease)
- **ICD-11:** 1C30.0 (Typhus fever due to *Rickettsia prowazekii*)
- **Disease category:** Infectious disease (vector-borne bacterial zoonosis/anthroponosis)

**Information source type:** The knowledge base entry is derived predominantly from **aggregated disease-level resources** — reviews, outbreak investigations, case series, and experimental animal/in-vitro studies — rather than from individual EHR-derived patient records. Contemporary surveillance is limited; in the United States the disease is not nationally notifiable [PMID: 31984654](https://pubmed.ncbi.nlm.nih.gov/31984654/).

---

## 2. Etiology

### Causal factors

Epidemic typhus is an **infectious disease** with no primary genetic etiology in the human host. The sole causative agent is *Rickettsia prowazekii*. As summarized in the finding on etiology and transmission (F001):

> "Epidemic typhus is transmitted to human beings by the body louse *Pediculus humanus corporis*. The disease is still considered a major threat by public-health authorities, despite the efficacy of antibiotics, because poor sanitary conditions are conducive to louse proliferation." — [PMID: 18582834](https://pubmed.ncbi.nlm.nih.gov/18582834/)

> "Epidemic typhus caused by *Rickettsia prowazekii* is one of the oldest pestilential diseases of humankind. The disease is transmitted to human beings by the body louse *Pediculus humanus corporis*." — [PMID: 27726780](https://pubmed.ncbi.nlm.nih.gov/27726780/)

The louse acquires *R. prowazekii* by feeding on a bacteremic human; the bacteria multiply in the louse gut epithelium and are shed in feces. Humans are infected when contaminated feces are rubbed into bite/scratch abrasions or contact mucous membranes — **not** by the bite itself. The louse dies of the infection, which distinguishes this vector relationship from most arthropod-borne diseases.

### Risk factors

- **Environmental / social:** Poor sanitation, cold climate (which promotes wearing of unwashed layered clothing that harbors body lice), overcrowding, war, famine, refugee/displacement camps, homelessness, and incarceration are the dominant risk factors [PMID: 18582834](https://pubmed.ncbi.nlm.nih.gov/18582834/); [PMID: 17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/). Homeless populations in developed countries are an increasingly recognized at-risk group.
- **Occupational/exposure:** In the U.S. sylvatic cycle, contact with southern flying squirrels and their ectoparasites is a risk factor [PMID: 18582834](https://pubmed.ncbi.nlm.nih.gov/18582834/).
- **Genetic risk factors (human host):** None established. Epidemic typhus is not a heritable condition; there are no known human causal variants, susceptibility loci, or modifier genes. (See Sections 4 and 9.)

### Protective factors

- **Environmental protective factors:** Good hygiene, regular laundering/heat treatment of clothing, access to bathing, and reduced crowding interrupt the louse cycle and are protective.
- **Immunological:** Prior infection confers cell-mediated immunity (IFN-γ/CD8+ T-cell memory), although latent organisms may persist and reactivate (Brill–Zinsser). No human **genetic** protective variants are documented.

### Gene–environment interactions

No documented human gene–environment interactions. Disease risk is governed by socio-environmental exposure to infected lice, not by host genotype. On the **pathogen** side, however, virulence is genetically encoded and environmentally modulated (see Section 4).

---

## 3. Phenotypes

Epidemic typhus is an **acute monophasic febrile illness** with an incubation period of approximately 1–2 weeks (F010). Onset is typically abrupt.

| Phenotype | Type | Frequency / severity | HPO suggestion |
|---|---|---|---|
| High fever | Symptom/sign | Near-universal; high, sustained | HP:0001945 (Fever) |
| Severe headache | Symptom | Very common, severe | HP:0002315 (Headache) |
| Myalgia | Symptom | Common | HP:0003326 (Myalgia) |
| Malaise/prostration | Symptom | Common | HP:0033834 (Malaise) |
| Maculopapular/petechial rash (centrifugal) | Physical sign | Classic but **frequently absent** (~25% in Burundi) | HP:0000988 (Skin rash); HP:0000979 (Petechiae) |
| Stupor / delirium ("typhos") / encephalitis | Neurologic sign | In severe cases | HP:0002329 (Drowsiness); HP:0002383 (Encephalitis); HP:0031258 (Delirium) |
| Meningoencephalitis | Clinical sign | Severe/CNS cases | HP:0002383 |
| Myocarditis | Clinical sign | Severe cases | HP:0012819 |
| Pneumonitis / interstitial pneumonia | Clinical sign | Severe cases | HP:0006515 |
| Acute kidney injury | Lab/clinical | Severe cases | HP:0001919 |
| Hypotension / shock | Clinical sign | Severe/terminal | HP:0002615 |

Supporting evidence (F004):

> "Serology is the mainstay of diagnosis... Doxycycline is the treatment of choice." — [PMID: 30712763](https://pubmed.ncbi.nlm.nih.gov/30712763/)

The term "typhus" derives from the Greek *typhos* ("smoke/stupor"), reflecting the characteristic neurologic clouding. On rash frequency (F010), the Burundi outbreak study reported skin eruptions in only ~25% of cases [PMID: 9717922](https://pubmed.ncbi.nlm.nih.gov/9717922/), underscoring that absence of rash does not exclude the diagnosis.

**Quality of life impact:** During acute illness, patients are typically prostrate and incapacitated. Because the disease is acute and monophasic (self-limited with treatment, or fatal), there is no chronic QoL instrument literature (EQ-5D/SF-36) specific to epidemic typhus; survivors who receive timely doxycycline generally recover fully, whereas untreated severe disease causes death or neurologic sequelae.

---

## 4. Genetic/Molecular Information

**No human causal genes, pathogenic variants, modifier genes, chromosomal abnormalities, or epigenetic disease mechanisms exist** — epidemic typhus is an acquired infection, not a Mendelian or complex genetic disorder. This section therefore addresses the genetics of the **pathogen**, which are central to virulence and vaccine biology.

### Pathogen genome and bioenergetics (F003)

*R. prowazekii* has a small, reductive genome reflecting its obligate intracytoplasmic lifestyle. It retains TCA-cycle and electron-transport genes but **lacks glycolysis**, forcing dependence on host metabolites:

> "the *R. prowazekii* genome contains genes encoding components of the tricarboxylic acid cycle as well as of the electron transport system, but lacks genes to support glycolysis." — [PMID: 9693729](https://pubmed.ncbi.nlm.nih.gov/9693729/)

The organism steals host ATP via the ATP/ADP translocase **Tlc1**:

> "The paradigm for the study of rickettsial transport systems is the ATP/ADP translocase Tlc1, which exchanges bacterial ADP for host cell ATP as a source of energy." — [PMID: 16923893](https://pubmed.ncbi.nlm.nih.gov/16923893/)

Of five annotated Tlc paralogues, **only Tlc1 transports ATP/ADP**; Tlc4 and Tlc5 import other ribonucleotides (CTP, UTP, GDP), underscoring extensive host dependence for nucleotides [PMID: 16923893](https://pubmed.ncbi.nlm.nih.gov/16923893/). The ADP/ATP translocator was among the first rickettsial transporters cloned and expressed in *E. coli* [PMID: 2986146](https://pubmed.ncbi.nlm.nih.gov/2986146/), and its transcription is coordinately regulated with citrate synthase (*gltA*) in response to host energy state [PMID: 9607082](https://pubmed.ncbi.nlm.nih.gov/9607082/).

### Pathogen virulence genetics (F005)

Strain virulence maps to an **area of genomic plasticity**, with inactivating frameshifts in homopolymeric poly(A)/poly(T) tracts (in *recO*, a methyltransferase, and an exported protein) in the avirulent **Madrid E** vaccine strain, and cascade gene reactivation restoring virulence on passage — an example of adaptive mutation:

> "An area of genomic plasticity appears to determine virulence in *R. prowazekii* and represents an example of adaptive mutation for this pathogen." — [PMID: 20368341](https://pubmed.ncbi.nlm.nih.gov/20368341/)

Key virulence genes include **pld** (phospholipase D) and **tlyC** (hemolysin C), both implicated in phagosomal escape (see Section 6). Directed knockout of *pld* in strain Madrid Evir attenuated virulence in guinea pigs while retaining protective immunogenicity [PMID: 19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/).

---

## 5. Environmental Information

### Environmental and lifestyle factors

The disease is fundamentally driven by **socio-environmental conditions** that promote body-louse proliferation: cold climate, unwashed clothing, crowding, and poor sanitation (F001). Lifestyle factors are those associated with poverty and displacement rather than individual behaviors like smoking or diet.

### Infectious agents (F001, F005)

- **Etiologic agent:** *Rickettsia prowazekii* (NCBI Taxonomy: txid782), an obligate intracellular Gram-negative alphaproteobacterium (family Rickettsiaceae, typhus group).
- **Vector:** *Pediculus humanus corporis* (human body louse; NCBI Taxonomy: txid121224). Body lice may co-transmit other pathogens (*Bartonella quintana* — trench fever; *Borrelia recurrentis* — relapsing fever), and co-circulation is documented in outbreaks [PMID: 9717922](https://pubmed.ncbi.nlm.nih.gov/9717922/); [PMID: 37567429](https://pubmed.ncbi.nlm.nih.gov/37567429/).
- **Sylvatic reservoir/vector:** Southern flying squirrel *Glaucomys volans* and its ectoparasites in the eastern USA (F002).
- **Biothreat:** Stable in dried louse feces and aerosol-transmissible — CDC Category B agent (F005).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Infected body-louse feces are deposited on the skin during feeding; scratching **inoculates** *R. prowazekii* through abrasions or onto mucosae →
2. Bacteria enter the bloodstream and **disseminate hematogenously** to distant vascular beds →
3. *R. prowazekii* **invades vascular endothelial cells** (primary target) and, secondarily, macrophages; it escapes the phagosome into the cytosol (**phospholipase D [pld]** and **hemolysin C/TlyC** contribute to membrane damage/phagosomal escape) →
4. In the cytoplasm the bacterium **parasitizes host ATP** via the ATP/ADP translocase **Tlc1** (it cannot glycolyse) and replicates freely →
5. Endothelial infection **activates host-cell signaling**, triggering vascular inflammation, loss of vascular integrity, and increased permeability — collectively **"rickettsial vasculitis"** (inferred host signaling differs between typhus and spotted-fever groups) →
6. Widespread small-vessel vasculitis produces **perivascular mononuclear infiltrates ("typhus nodules")**, microthrombi, and vascular leak →
7. **End-organ hypoperfusion and edema** result in rash (skin microvasculature), headache/encephalitis (brain), myocarditis (heart), pneumonitis (lung), acute kidney injury (kidney), and hypotension/shock →
8. If untreated → **multiorgan failure and death**. *(Branch A: cell-mediated immunity — IFN-γ + CD8+ T cells — clears the organism and drives recovery. Branch B: latent survival in adipose tissue leads years later to Brill–Zinsser reactivation.)*

### Detail and supporting evidence (F006, F009)

Endothelial tropism is the mechanistic origin of the disease:

> "a majority of sequelae associated with human rickettsioses are the outcome of the pathogen's affinity for endothelium lining the blood vessels, the consequences of which are vascular inflammation, insult to vascular integrity and compromised vascular permeability, collectively termed 'Rickettsial vasculitis'." — [PMID: 19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/)

> "Rickettsiosis is a vector-borne disease that causes systemic and potentially fatal vasculitis if not diagnosed promptly and treated with antibiotics." — [PMID: 40793754](https://pubmed.ncbi.nlm.nih.gov/40793754/)

Human autopsy evidence confirms the cellular targets (F009):

> "*Rickettsia prowazekii* organisms were identified in endothelium and macrophages in sections of the brains of three Egyptian men who died of epidemic louse-borne typhus in Cairo during World War II and in the brain from a recent case of typhus fever acquired in Burundi." — [PMID: 9346184](https://pubmed.ncbi.nlm.nih.gov/9346184/)

**Molecular/cellular processes:** obligate intracellular replication in cytoplasm; phagosomal escape (PLD, TlyC); host energy parasitism (Tlc1); endothelial activation → vascular inflammation and permeability; Th1 cell-mediated immunity for clearance. LPS/lipid A proinflammatory signaling contributes to inflammation, and O-antigen immunogenicity differs between typhus and spotted-fever groups [PMID: 38259062](https://pubmed.ncbi.nlm.nih.gov/38259062/).

**Suggested ontology terms:**
- GO biological processes: GO:0006954 (inflammatory response), GO:0009405 (pathogenesis), GO:0015867 (ATP transport), GO:0051701 (biological process involved in interaction with host), GO:0006955 (immune response), GO:0032609 (interferon-gamma production).
- CL cell types: CL:0000115 (endothelial cell), CL:0002138 (blood vessel endothelial cell), CL:0000235 (macrophage), CL:0000625 (CD8-positive, alpha-beta T cell).
- CHEBI: CHEBI:15422 (ATP), CHEBI:16761 (ADP), CHEBI:16412 (lipopolysaccharide).

---

## 7. Anatomical Structures Affected

**Organ level (F009):** The primary target is the **vascular endothelium** systemically. Target organs of hematogenous dissemination are **brain, lungs, heart, and kidneys**, plus **skin, liver, and spleen**:

> "reproduces the hematogenous dissemination to the critical target organs, including brain, lungs, heart, and kidneys, primary endothelial and, to a lesser degree, macrophage intracellular rickettsial infection." — [PMID: 11005205](https://pubmed.ncbi.nlm.nih.gov/11005205/)

**Body systems involved:** cardiovascular (vasculitis, myocarditis), nervous (encephalitis, meningoencephalitis), respiratory (interstitial pneumonia), renal (AKI), integumentary (rash), and reticuloendothelial (liver/spleen).

**Tissue and cell level:** vascular endothelial cells (primary) and macrophages (secondary). **Adipose tissue** is a latency reservoir (F002).

**Subcellular level:** *R. prowazekii* resides free in the **host cytoplasm** (GO:0005737, cytoplasm) after escaping the **phagosome** (GO:0045335). It exploits the host cytosolic nucleotide pools via Tlc1.

**Localization/lateralization:** Lesions are **bilateral and systemic/diffuse** (widespread small-vessel involvement), not lateralized.

**Suggested UBERON terms:** UBERON:0001981 (blood vessel), UBERON:0001986 (endothelium), UBERON:0000955 (brain), UBERON:0002048 (lung), UBERON:0000948 (heart), UBERON:0002113 (kidney), UBERON:0002097 (skin of body), UBERON:0001013 (adipose tissue).

---

## 8. Temporal Development

- **Onset:** Adult and any age with exposure; **acute** onset after an incubation of ~1–2 weeks (F010). Not congenital or age-restricted.
- **Course:** **Acute, monophasic** febrile illness. With effective treatment, defervescence occurs rapidly (~48 h on doxycycline; F004). Untreated disease progresses over ~2 weeks to severe multiorgan involvement.
- **Stages:** early (nonspecific fever/headache/myalgia) → established (rash, neurologic signs) → severe (encephalitis, myocarditis, pneumonitis, AKI, shock) → death or convalescence.
- **Progression rate:** rapid if untreated; can be fatal within days to ~2 weeks.
- **Remission/relapse:** Treatment-induced remission is prompt. **Latent persistence** enables recrudescence years-to-decades later as **Brill–Zinsser disease**, typically milder (F002):

> "Brill-Zinsser disease, a relapsed form of epidemic typhus that appears as sporadic cases many years after the initial infection, is unrelated to louse infestation. Stress or a waning immune system are likely to reactivate this earlier persistent infection." — [PMID: 18582834](https://pubmed.ncbi.nlm.nih.gov/18582834/)

A murine model localizes the latency reservoir to adipose tissue, reactivatable with dexamethasone (F002):

> "*Rickettsia prowazekii* (the etiologic agent of epidemic typhus) was detected... in murine adipose tissue, but not in liver, spleen, lung, or central nervous system tissues of mice 4 months after recovery from the primary infection... these data suggest a role for adipose tissue as a potential reservoir for dormant infections with *R. prowazekii*." — [PMID: 20049326](https://pubmed.ncbi.nlm.nih.gov/20049326/)

- **Critical period for intervention:** early empiric doxycycline before serologic confirmation is decisive; delay increases mortality and sequelae (F004).

---

## 9. Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, founder effect, consanguinity, or carrier frequency applies.

### Epidemiology (F010)

Epidemic typhus is now **rare and sporadic globally**, persisting in cold, impoverished, crowded settings (highland Africa, the Andes, parts of Asia) and via the North American sylvatic flying-squirrel cycle. It is **not nationally notifiable** in the USA, so true burden is uncertain; U.S. insurance-claim coding suggests substantial misclassification:

> "Epidemic typhus (n = 931/1,799; 51.8%) was the most common TGRs, followed by murine typhus." — [PMID: 31984654](https://pubmed.ncbi.nlm.nih.gov/31984654/)

This coding pattern is notable because true epidemic typhus requires louse or flying-squirrel exposure and should be rare, indicating diagnostic misclassification. Explosive epidemics still occur in humanitarian crises. The Burundi outbreak (1995–1997) affected displaced/imprisoned populations after a 12-year absence, with co-circulating trench fever (F005, F010):

> "After a 12-year absence, epidemic typhus has re-emerged among the displaced population of Burundi." — [PMID: 9717922](https://pubmed.ncbi.nlm.nih.gov/9717922/)

Historical typhus-group distribution spanned Andean/Caribbean South America (e.g., Colombia) [PMID: 36628901](https://pubmed.ncbi.nlm.nih.gov/36628901/), and epidemiologic patterns of typhus-group rickettsioses continue to shift in regions such as China [PMID: 38163619](https://pubmed.ncbi.nlm.nih.gov/38163619/).

- **Geographic distribution:** endemic foci in highland/cold impoverished regions; sylvatic cycle in eastern USA.
- **Demographics:** affects those exposed to body lice — refugees, prisoners, homeless, war-affected populations; no ethnic genetic predisposition.
- **Sex ratio:** driven by exposure, not biology; no established intrinsic sex difference.

---

## 10. Diagnostics

### Clinical tests and biomarkers (F004)

- **Serology (reference standard):** Indirect immunofluorescence assay (IFA) for anti–*R. prowazekii* antibodies.

> "Serology is the mainstay of diagnosis, and the indirect immunofluorescence assay is the test of choice. Reactive antibodies are seldom present during early illness, so testing should be performed on both acute-phase and convalescent-phase sera. Doxycycline is the treatment of choice." — [PMID: 30712763](https://pubmed.ncbi.nlm.nih.gov/30712763/)

- **Timing caveat:** antibodies are typically absent in early illness → paired acute and convalescent sera are required; treatment should not await serology.
- **Molecular:** PCR of blood/tissue; immunohistochemistry using anti-LPS monoclonal antibodies can identify organisms in endothelium/tissue [PMID: 9346184](https://pubmed.ncbi.nlm.nih.gov/9346184/).
- **Laboratory abnormalities:** commonly thrombocytopenia, elevated transaminases, and inflammatory markers (as seen across typhus-group rickettsioses).
- **Genetic/omics diagnostics:** not applicable for host diagnosis; pathogen detection increasingly uses PCR and targeted next-generation sequencing (tNGS) in difficult cases.

### Clinical criteria and differential diagnosis (F004, F010)

- No formal DSM/consensus scoring; diagnosis is clinical-epidemiologic (louse exposure + acute febrile syndrome) confirmed serologically.
- **Differential diagnosis:** typhoid fever (imported epidemic typhus is readily misdiagnosed as typhoid — [PMID: 10511530](https://pubmed.ncbi.nlm.nih.gov/10511530/)), murine (flea-borne) typhus, scrub typhus, meningococcemia, other rickettsioses, viral hemorrhagic and arboviral encephalitides. Typhus-group *Rickettsia* can cause community-acquired CNS infection (meningoencephalitis) that must be considered "outside the box" [PMID: 39447222](https://pubmed.ncbi.nlm.nih.gov/39447222/).

**Screening:** No asymptomatic-population screening exists; outbreak response uses active case-finding plus louse surveillance.

---

## 11. Outcome/Prognosis

- **Mortality:** Untreated epidemic typhus historically carries high case-fatality (reported up to ~10–60% depending on host condition, age, and epidemic context). With prompt doxycycline, mortality falls dramatically.
- **Recovery:** Doxycycline produces rapid clinical resolution (defervescence within ~48 h) and, in CNS disease, prompt symptom resolution (F004):

> "Treatment with doxycycline leads to prompt resolution of symptoms. Failure to initiate early empiric treatment can lead to serious consequences." — [PMID: 39447222](https://pubmed.ncbi.nlm.nih.gov/39447222/)

- **Complications:** encephalitis with neurologic sequelae, myocarditis, pneumonitis, acute kidney injury, gangrene of extremities (from vasculitis/microthrombi), shock, and death.
- **Prognostic factors:** timeliness of therapy is the dominant modifiable determinant; older age, comorbidity, malnutrition, and delayed diagnosis worsen outcome. Delayed diagnosis is associated with fatal outcomes in typhus-group rickettsioses [PMID: 38163619](https://pubmed.ncbi.nlm.nih.gov/38163619/).
- **Recrudescence:** survivors carry lifelong risk of Brill–Zinsser reactivation, generally milder (F002).

---

## 12. Treatment

### Pharmacotherapy (F004)

- **Doxycycline** (tetracycline-class; inhibits bacterial 30S ribosome/protein synthesis) is the **drug of choice** for all ages, producing rapid defervescence. Even short courses are effective given the organism's susceptibility.
- **Alternatives:** chloramphenicol (historically used, e.g., in pregnancy or tetracycline intolerance); some fluoroquinolones and macrolides have activity but doxycycline remains first-line.
- **Post-exposure prophylaxis:** single-dose doxycycline can be used in outbreak settings (F007).
- **Pharmacogenomics:** none clinically relevant to therapy.

> "Doxycycline is the treatment of choice." — [PMID: 30712763](https://pubmed.ncbi.nlm.nih.gov/30712763/)

### Supportive care

Fluid resuscitation for vascular leak/shock, management of encephalitis, respiratory support for pneumonitis, and organ-specific supportive measures for severe multiorgan disease.

### Advanced/experimental therapeutics

No gene, cell, RNA-based, or immunotherapy is used or required — this is a treatable acute bacterial infection. Research on attenuated vaccine strains (e.g., *pld* knockout) is directed at prevention rather than treatment [PMID: 19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/).

**Suggested NCIT terms:** NCIT:C692 (Doxycycline), NCIT:C376 (Chloramphenicol), NCIT:C15844 (Antibiotic Therapy).

---

## 13. Prevention

### Primary prevention — louse control (F007)

Interrupting the body-louse cycle is the decisive intervention: improved hygiene/sanitation, laundering and heat treatment of clothing, and pediculicides. Topical **permethrin** and oral **ivermectin** (which targets invertebrate glutamate-gated chloride channels) are effective, and mass ivermectin administration reduces louse prevalence:

> "Ivermectin is efficacious against headlice, and is also being evaluated as a malaria vector control tool." — [PMID: 40140904](https://pubmed.ncbi.nlm.nih.gov/40140904/)

However, **pediculicide resistance** is an emerging threat — permethrin treatment failures are documented [PMID: 41258179](https://pubmed.ncbi.nlm.nih.gov/41258179/), and novel glutamate-gated chloride channel (GluCl) mutations threaten ivermectin efficacy:

> "resistance to this insecticide threatens the effectiveness of head louse control programs." — [PMID: 40102974](https://pubmed.ncbi.nlm.nih.gov/40102974/)

New pediculicide chemistries with alternative modes of action are under development to manage resistance [PMID: 35082036](https://pubmed.ncbi.nlm.nih.gov/35082036/).

### Secondary prevention

Early empiric doxycycline; single-dose doxycycline post-exposure prophylaxis during outbreaks (F007).

### Immunization

The historic live attenuated **Madrid E** vaccine and killed vaccines were used in the mid-20th century, but **no rickettsial vaccine is currently licensed or available**; vector control and antibiotics remain the mainstays (F007). Candidate non-reverting attenuated strains (e.g., *pld* knockout) protect in animal models [PMID: 19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/).

### Public health

Sanitation, mass delousing in refugee/prison settings, outbreak surveillance, and health education. Preparedness planning must address vulnerable groups such as pregnant women given biothreat potential [PMID: 28398677](https://pubmed.ncbi.nlm.nih.gov/28398677/).

**Suggested NCIT/CHEBI terms:** NCIT:C29744 (Permethrin), CHEBI:6078 (ivermectin), NCIT:C15311 (Vaccination), NCIT:C16781 (Sanitation).

---

## 14. Other Species / Natural Disease

- **Taxonomy of agent and vectors:** *Rickettsia prowazekii* (NCBI:txid782); *Pediculus humanus corporis* (NCBI:txid121224).
- **Reservoir hosts:** Humans are the principal reservoir. A **sylvatic zoonotic cycle** involves the **southern flying squirrel *Glaucomys volans*** and its ectoparasites in the eastern USA (F002):

> "Since 1975, R prowazekii infection in human beings has been related to contact with the flying squirrel *Glaucomys volans* in the USA." — [PMID: 18582834](https://pubmed.ncbi.nlm.nih.gov/18582834/)

- **Zoonotic potential/transmission:** established (sylvatic squirrel cycle → humans). Body/head louse clades (including a described Clade D) may carry additional pathogens, illustrating broad vector competence [PMID: 26392158](https://pubmed.ncbi.nlm.nih.gov/26392158/).
- **Comparative pathology:** experimental infection reproduces human-like disease in mice and guinea pigs (Section 15). Louse infestations of veterinary importance (e.g., sheep lice) are managed with similar acaricides/ivermectin, informing vector-control science [PMID: 36406066](https://pubmed.ncbi.nlm.nih.gov/36406066/).

---

## 15. Model Organisms (F008)

Historically, murine models were of limited value because infection was often inapparent or erratically lethal [PMID: 18366341](https://pubmed.ncbi.nlm.nih.gov/18366341/). Modern models, tuned by host genetic background, rickettsial species, and inoculation route, now recapitulate human disease.

| Model | System | Recapitulation | Key finding | PMID |
|---|---|---|---|---|
| BALB/c mouse, IV *R. prowazekii* (Breinl) | Mammalian | Dissemination to blood/liver/lung/brain within 1 day, persisting ≥9 days; interstitial pneumonia, pulmonary & cerebral hemorrhages, hepatic granulomas | Lesions independent of humoral response; associated with IFN-γ, TNF, RANTES/CCL5 | [17537665](https://pubmed.ncbi.nlm.nih.gov/17537665/) |
| C3H/HeN mouse, *R. typhi* (typhus-group endothelial-target model) | Mammalian | Endothelial vascular lesions in brain, lung, heart, kidney | IFN-γ and CD8+ T cells crucial for clearance; IL-12 marks effective immunity | [11005205](https://pubmed.ncbi.nlm.nih.gov/11005205/) |
| Guinea pig | Mammalian | Virulence/attenuation assessment | *pld* knockout of Madrid Evir attenuated and protective | [19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/) |
| BALB/c adipose reservoir | Mammalian | Latency/recrudescence | *R. prowazekii* persists in adipose tissue; reactivates with dexamethasone | [20049326](https://pubmed.ncbi.nlm.nih.gov/20049326/) |

Supporting quotes (F008):

> "infected mice developed interstitial pneumonia, with consolidation of the alveoli, hemorrhages in lungs, multifocal granulomas in liver, and hemorrhages in brain, as seen in humans." — [PMID: 17537665](https://pubmed.ncbi.nlm.nih.gov/17537665/)

> "Gamma interferon and CD8 T lymphocytes were demonstrated to be crucial to clearance of the rickettsiae and recovery from infection." — [PMID: 11005205](https://pubmed.ncbi.nlm.nih.gov/11005205/)

**Model limitations:** susceptibility is strongly genotype-, species-, and route-dependent; no single rodent model fully reproduces louse-borne natural transmission or the full human vasculitic spectrum. **Applications:** pathogenesis of endothelial infection, protective immunity mechanisms, vaccine candidate evaluation, and latency/recrudescence biology.

---

## Mechanistic Model / Interpretation

```
   Infected louse feces (R. prowazekii)
              │  inoculation via skin abrasion / mucosa
              ▼
     Bloodstream (bacteremia) ──────────────► hematogenous dissemination
              │
              ▼
   ENDOTHELIAL CELL INVASION  ◄── (macrophages, secondary)
              │  phagosomal escape: PLD, TlyC
              ▼
   Cytoplasmic replication  ──── energy theft via Tlc1 (ATP/ADP), no glycolysis
              │
              ▼
   Endothelial activation → VASCULAR INFLAMMATION
   (loss of integrity + increased permeability = "RICKETTSIAL VASCULITIS")
              │
              ├── typhus nodules (perivascular mononuclear infiltrate)
              ├── microthrombi
              └── vascular leak / edema
              │
              ▼
   MULTIORGAN INJURY:
   skin(rash) · brain(encephalitis) · heart(myocarditis)
   lung(pneumonitis) · kidney(AKI) · shock
              │
       ┌──────┴───────────────┐
       ▼                       ▼
  Cell-mediated immunity   Untreated → death
  (IFN-γ, CD8+ T cells)         │
       │                        │  OR early doxycycline → rapid recovery
       ▼
  Clearance + latent survival in adipose tissue
       │  years later (stress / waning immunity)
       ▼
  BRILL–ZINSSER DISEASE (recrudescence, can reseed epidemics)
```

The unifying interpretation is that **a single cellular tropism — for vascular endothelium — accounts for the entire clinical syndrome**. Every major manifestation (rash, encephalitis, myocarditis, pneumonitis, renal failure, shock) is the local expression of the same diffuse small-vessel vasculitis. This explains why a narrow-spectrum, inexpensive antibiotic (doxycycline) that halts intracellular replication produces such rapid, near-complete recovery, and why the disease is simultaneously a biological curiosity (energy-parasitic reductive genome), a public-health disease of poverty and displacement, and a recognized biothreat.

---

## Evidence Base

| PMID | Role | Supports |
|---|---|---|
| [18582834](https://pubmed.ncbi.nlm.nih.gov/18582834/) | Landmark review (*Epidemic typhus*) | Vector, transmission, flying-squirrel cycle, Brill–Zinsser, biothreat (F001, F002, F005) |
| [27726780](https://pubmed.ncbi.nlm.nih.gov/27726780/) | Review (*History of Epidemic Typhus*) | Agent and body-louse transmission (F001) |
| [20049326](https://pubmed.ncbi.nlm.nih.gov/20049326/) | Model organism study | Adipose latency reservoir/recrudescence (F002) |
| [9693729](https://pubmed.ncbi.nlm.nih.gov/9693729/) | Bioenergetics study | No glycolysis; TCA/ETS present (F003) |
| [16923893](https://pubmed.ncbi.nlm.nih.gov/16923893/) | Transporter study | Tlc1 ATP/ADP translocase; host energy parasitism (F003) |
| [30712763](https://pubmed.ncbi.nlm.nih.gov/30712763/) | Practical review | IFA serology; doxycycline first-line (F004) |
| [39447222](https://pubmed.ncbi.nlm.nih.gov/39447222/) | CNS case discussion | Doxycycline resolves CNS disease; danger of delay (F004) |
| [20368341](https://pubmed.ncbi.nlm.nih.gov/20368341/) | Multi-omics study | Genomic plasticity/adaptive mutation, virulence (F005) |
| [9717922](https://pubmed.ncbi.nlm.nih.gov/9717922/) | Outbreak report | Burundi re-emergence; low rash frequency (F005, F010) |
| [19327117](https://pubmed.ncbi.nlm.nih.gov/19327117/) | Mechanistic review | Endothelial tropism → rickettsial vasculitis (F006) |
| [40793754](https://pubmed.ncbi.nlm.nih.gov/40793754/) | TlyC hemolysin study | Systemic fatal vasculitis; phagosomal escape (F006) |
| [40140904](https://pubmed.ncbi.nlm.nih.gov/40140904/) | Cluster RCT | Ivermectin efficacy against lice (F007) |
| [40102974](https://pubmed.ncbi.nlm.nih.gov/40102974/) | Resistance study | GluCl mutations → ivermectin resistance (F007) |
| [17537665](https://pubmed.ncbi.nlm.nih.gov/17537665/) | Model organism study | BALB/c model recapitulates multiorgan pathology (F008) |
| [11005205](https://pubmed.ncbi.nlm.nih.gov/11005205/) | Model organism study | Endothelial target model; IFN-γ/CD8 clearance (F008, F009) |
| [9346184](https://pubmed.ncbi.nlm.nih.gov/9346184/) | Human autopsy IHC | Endothelium/macrophage targeting in fatal CNS typhus (F009) |
| [31984654](https://pubmed.ncbi.nlm.nih.gov/31984654/) | Claims analysis | Contemporary US coding/misclassification (F010) |
| [10511530](https://pubmed.ncbi.nlm.nih.gov/10511530/) | Case report | Misdiagnosis as typhoid (F010) |
| [19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/) | Mutagenesis study | *pld* knockout attenuated, protective vaccine candidate |
| [18366341](https://pubmed.ncbi.nlm.nih.gov/18366341/) | Review | Animal-model context and historical limitations |

Supporting context papers: [37567429](https://pubmed.ncbi.nlm.nih.gov/37567429/) (louse-borne pathogens), [17114713](https://pubmed.ncbi.nlm.nih.gov/17114713/) (homeless/ectoparasites), [26392158](https://pubmed.ncbi.nlm.nih.gov/26392158/) (louse clades), [38259062](https://pubmed.ncbi.nlm.nih.gov/38259062/) (LPS/lipid A), [36628901](https://pubmed.ncbi.nlm.nih.gov/36628901/) & [38163619](https://pubmed.ncbi.nlm.nih.gov/38163619/) (regional epidemiology), [28398677](https://pubmed.ncbi.nlm.nih.gov/28398677/) (biothreat/pregnancy), [41258179](https://pubmed.ncbi.nlm.nih.gov/41258179/) & [35082036](https://pubmed.ncbi.nlm.nih.gov/35082036/) (pediculicide resistance/new chemistries).

---

## Limitations and Knowledge Gaps

1. **Contemporary burden is poorly quantified.** Epidemic typhus is not nationally notifiable in the USA, and coding data indicate substantial misclassification, so incidence/prevalence estimates are uncertain [PMID: 31984654](https://pubmed.ncbi.nlm.nih.gov/31984654/).
2. **Human mechanistic data are sparse.** Much pathogenesis detail derives from animal models (some using *R. typhi* as a typhus-group surrogate) and in-vitro work rather than human tissue; autopsy series are historical and small [PMID: 9346184](https://pubmed.ncbi.nlm.nih.gov/9346184/).
3. **Latency biology is incompletely defined in humans.** The adipose reservoir is demonstrated in mice; the precise cellular/molecular basis of Brill–Zinsser latency and reactivation in humans remains inferred [PMID: 20049326](https://pubmed.ncbi.nlm.nih.gov/20049326/).
4. **No modern host-response omics** (transcriptomics/proteomics/metabolomics) datasets specific to human epidemic typhus were identified, limiting biomarker and prognostic-model development.
5. **Vaccine gap.** No licensed vaccine exists; attenuated candidates remain experimental [PMID: 19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/).
6. **Vector-control fragility.** Growing pediculicide resistance (permethrin, ivermectin/GluCl) threatens the primary prevention strategy [PMID: 41258179](https://pubmed.ncbi.nlm.nih.gov/41258179/); [PMID: 40102974](https://pubmed.ncbi.nlm.nih.gov/40102974/).

---

## Proposed Follow-up Experiments / Actions

1. **Strengthen surveillance:** advocate for standardized case definitions and (re)consideration of notifiable status; pair clinical reporting with **body-louse infestation surveys** in high-risk settings (refugee camps, prisons, homeless populations).
2. **Human host-response omics:** collect acute/convalescent blood for RNA-seq, proteomics, and cytokine profiling to define IFN-γ/CD8 signatures and candidate **prognostic biomarkers** (e.g., markers distinguishing severe vasculitic disease), building on the murine IFN-γ/TNF/CCL5 associations [PMID: 17537665](https://pubmed.ncbi.nlm.nih.gov/17537665/).
3. **Define the human latency reservoir:** test whether adipose tissue harbors *R. prowazekii* in Brill–Zinsser patients, translating the murine finding [PMID: 20049326](https://pubmed.ncbi.nlm.nih.gov/20049326/).
4. **Advance vaccine development:** further evaluate non-reverting attenuated strains (e.g., *pld*, and additional virulence-locus knockouts) for durable cell-mediated protection [PMID: 19506016](https://pubmed.ncbi.nlm.nih.gov/19506016/); [PMID: 20368341](https://pubmed.ncbi.nlm.nih.gov/20368341/).
5. **Resistance-proof vector control:** deploy rotation of pediculicides with distinct modes of action and monitor GluCl/kdr resistance markers; evaluate mass ivermectin administration co-benefits and limits [PMID: 40140904](https://pubmed.ncbi.nlm.nih.gov/40140904/); [PMID: 35082036](https://pubmed.ncbi.nlm.nih.gov/35082036/).
6. **Diagnostic acceleration:** validate rapid molecular (PCR/tNGS) and point-of-care assays to overcome the early-serology gap and reduce misdiagnosis as typhoid or other febrile illnesses [PMID: 30712763](https://pubmed.ncbi.nlm.nih.gov/30712763/); [PMID: 10511530](https://pubmed.ncbi.nlm.nih.gov/10511530/).

---

*Report compiled from 10 confirmed findings and 39 reviewed papers. Evidence types span human clinical/autopsy studies, animal models (mouse, guinea pig), in-vitro/molecular biology, and epidemiological/outbreak investigations, as annotated per finding.*


## Artifacts

- [OpenScientist final report](Epidemic_Typhus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Epidemic_Typhus-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 21 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35082036` (6 mentions) - New chemistries for the control of human head lice, Pediculus humanus capitis: A mini-review.
  - shared terms: human
- `PMID:36406066` (3 mentions) - Epidemiological and therapeutic studies on sheep lice in Sayint district, South Wollo Zone, Northeast Ethiopia.
  - shared terms: treatment

Weighed against this report's own most characteristic terms: `disease`, `typhus`, `epidemic`, `prowazekii`, `human`, `host`, `infection`, `louse`, `doxycycline`, `outbreak`, `acute`, `treatment`, `vaccine`, `organism`, `reservoir`, `brill`, `pathogen`, `zinsser`, `fever`, `rickettsia`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 38 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002383` (2 mentions) - the report calls it "Severe/CNS cases"; HP calls it **Infectious encephalitis**
- `HP:0012819` (1 mention) - the report calls it "Severe cases"; HP calls it **Myocarditis**
- `HP:0006515` (1 mention) - the report calls it "Severe cases"; HP calls it **Interstitial pneumonitis**
- `HP:0001919` (1 mention) - the report calls it "Severe cases"; HP calls it **Acute kidney injury**
- `HP:0002615` (1 mention) - the report calls it "Severe/terminal"; HP calls it **Hypotension**
- `NCIT:C692` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Nimodipine**
- `NCIT:C376` (1 mention) - the report calls it "Chloramphenicol"; NCIT calls it **Cisplatin**
- `NCIT:C15844` (1 mention) - the report calls it "Antibiotic Therapy"; NCIT calls it **Protein/Amino Acid Nutrition Research, Animal**
- `NCIT:C15311` (1 mention) - the report calls it "Vaccination"; NCIT calls it **Quality Control**
- `NCIT:C16781` (1 mention) - the report calls it "Sanitation"; NCIT calls it **Laryngoscopy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `GO:0032609` (1 mention) - the report calls it "interferon-gamma production"; GO calls it **type II interferon production**, and lists "interferon-gamma production" among its other names
- `CL:0002138` (1 mention) - the report calls it "blood vessel endothelial cell"; CL calls it **endothelial cell of lymphatic vessel**, and lists "lymphatic endothelial cell" among its other names
- `GO:0045335` (1 mention) - the report calls it "phagosome"; GO calls it **phagocytic vesicle**, and lists "phagosome" among its other names
- `NCIT:C29744` (1 mention) - the report calls it "Permethrin"; NCIT calls it **Formaldehyde**, and lists "Methanal" among its other names