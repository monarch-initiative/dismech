---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T08:37:33.600471'
end_time: '2026-09-25T09:33:18.717812'
duration_seconds: 3345.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pneumonic Tularemia
  mondo_id: MONDO:0002212
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 44
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 44
  on_topic: 37
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 48
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 1
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - "Acute onset 3\u20135 days post-exposure; near-universal"
    ontology_label: Fever
  - term_id: HP:0012735
    reported_labels:
    - Acute; common in pneumonic form
    ontology_label: Cough
  - term_id: HP:0002090
    reported_labels:
    - Acute; hallmark of pneumonic form
    ontology_label: Pneumonia
  - term_id: HP:0100721
    reported_labels:
    - Acute; characteristic
    ontology_label: Mediastinal lymphadenopathy
  - term_id: HP:0025143
    reported_labels:
    - Acute
    ontology_label: Chills
  - term_id: HP:0003326
    reported_labels:
    - Acute
    ontology_label: Myalgia
  - term_id: HP:0002315
    reported_labels:
    - Acute
    ontology_label: Headache
  - term_id: HP:0002094
    reported_labels:
    - Acute; severity correlates with extent
    ontology_label: Dyspnea
  - term_id: HP:0100749
    reported_labels:
    - Acute
    ontology_label: Chest pain
  - term_id: NCIT:C557
    reported_labels:
    - Preferred for severe/systemic disease
    ontology_label: Hydroxychloroquine
  - term_id: NCIT:C820
    reported_labels:
    - Historical gold standard
    ontology_label: Safflower Oil
  - term_id: NCIT:C2809
    reported_labels:
    - No fatalities in pneumonic cohort receiving cipro
    ontology_label: Recombinant Vaccinia-CEA
  - term_id: NCIT:C561
    reported_labels:
    - Bacteriostatic; higher relapse if course too short
    ontology_label: Ibuprofen
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pneumonic Tularemia
- **MONDO ID:** MONDO:0002212 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pneumonic Tularemia** covering all of the
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

# Pneumonic Tularemia (MONDO:0002212): Comprehensive Disease Characteristics Report

## Summary

**Pneumonic tularemia is the pulmonary and most lethal clinical form of tularemia, an intracellular bacterial zoonosis caused by inhalation of *Francisella tularensis*.** It presents 3–5 days after aerosol exposure as an acute, undifferentiated febrile illness with incipient pneumonia, pleuritis, and hilar lymphadenopathy. Because as few as ~10 organisms can cause disease, *F. tularensis* is one of the most infectious bacterial pathogens known and is classified as a Tier 1 / Category A bioterrorism agent. Untreated severe (pneumonic and typhoidal) disease carries a case-fatality rate historically reported as high as 60%, but prompt antimicrobial therapy reduces mortality to roughly 1%.

The pathogenesis is not driven by a human genetic lesion — this is an infectious disease with no Mendelian etiology — but by a stereotyped host–pathogen program. The **Francisella Pathogenicity Island (FPI)**, encoding a **Type VI secretion system (T6SS)**, allows the bacterium to escape the macrophage phagosome and replicate in the cytosol. During the first ~24 hours in the lung, virulent *F. tularensis* actively **suppresses innate immune gene induction** ("stealth" phase), inhibits the neutrophil oxidative burst, delays neutrophil apoptosis, and represses the inflammasome. This is followed ~48 hours post-exposure by a delayed, dysregulated inflammatory "storm" that produces pyogranulomatous pneumonia and, if untreated, systemic dissemination, sepsis, and death.

Key modifiers of severity include the infecting subspecies and clade: **subsp. *tularensis* (Type A)** is more virulent than **subsp. *holarctica* (Type B)**, and within Type A the **A-east** clade causes more severe disease than **A-west**. Protective immunity is **cell-mediated** (CD8⁺/CD4⁺ T cells, IFN-γ, TNF-α, perforin/granzyme cytotoxic effectors), not antibody-based. First-line treatment is an aminoglycoside (gentamicin/streptomycin) for severe disease or a fluoroquinolone (ciprofloxacin/levofloxacin) or doxycycline; the 2025 CDC guidance designates fluoroquinolones and doxycycline as first-line for outbreaks of any size. No licensed vaccine currently exists.

---

## Key Findings

### Finding 1 — Pneumonic tularemia is the most lethal clinical form, caused by inhalation of *F. tularensis*

A systematic review of 870 human tularemia cases (1993–2023) confirmed that pneumonic disease is among the most common forms and carries the worst outcomes. As quoted from the review: *"If not promptly diagnosed and treated, the fatality rate can be as high as 60%, with the poorest outcomes reported in the pneumonic and typhoidal forms"* ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)). The bioterrorism-consensus literature describes the clinical tempo of inhalational disease: *"A weapon using airborne tularemia would likely result 3 to 5 days later in an outbreak of acute, undifferentiated febrile illness with incipient pneumonia, pleuritis, and hilar lymphadenopathy"* ([PMID: 11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/)). The extraordinarily low infectious dose — *"requires as few as 10 organisms to cause disease, making this potential bioterrorism agent one of the most infectious bacterial pathogens known"* ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)) — underlies both its natural danger and its bioweapon classification.

### Finding 2 — The FPI-encoded Type VI secretion system drives phagosomal escape and cytosolic replication

The core virulence mechanism is the Francisella Pathogenicity Island (FPI), a duplicated gene cluster (*iglABCD*, *vgrG*, *iglI*, *iglE*, *iglG*, *pdpC*, *dotU*, *pdpB/IcmF*) that encodes a Type VI secretion system homologous to those of *Vibrio* and *Pseudomonas*. FPI effectors are secreted into the macrophage cytosol and are required for the intracellular life cycle: *"VgrG and IglI are required for F. tularensis phagosomal escape, intramacrophage growth, inflammasome activation and virulence in mice"* ([PMID: 20054881](https://pubmed.ncbi.nlm.nih.gov/20054881/)). The regulatory arm is equally essential: *"the Francisella pathogenicity island (FPI) protein IglC and its regulator MglA are essential for modulating phagosome biogenesis and subsequent bacterial escape into the cytoplasm"* ([PMID: 15953029](https://pubmed.ncbi.nlm.nih.gov/15953029/)). Genetic ablation confirms necessity: inactivation of *iglE* in the virulent Schu S4 strain renders it avirulent and unable to escape the phagosome ([PMID: 23959721](https://pubmed.ncbi.nlm.nih.gov/23959721/)).

### Finding 3 — First-line treatment is aminoglycosides; fluoroquinolones are highly effective for the pneumonic form

Antimicrobial outcome data from 870 cases show low fatality across effective drug classes: aminoglycosides 0.7%, fluoroquinolones 0.9%, tetracyclines 1.2%. Notably, *"Patients with pneumonic disease who received ciprofloxacin had no fatalities and the lowest rates of thoracentesis/pl[eural complications]"* ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)). Guideline framing: *"Gentamicin is the first-line treatment for severe tularemia, while fluoroquinolones and tetracyclines are commonly the drugs of choice in less severe forms"* ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)). Susceptibility is broad and stable — all 278 US isolates (2009–2018) were susceptible to every drug tested: *"All isolates were susceptible to all tested drugs"* ([PMID: 38294116](https://pubmed.ncbi.nlm.nih.gov/38294116/)). The 2025 CDC guidance updated treatment/post-exposure prophylaxis (PEP), designating fluoroquinolones (ciprofloxacin or levofloxacin) and doxycycline as first-line for outbreaks of any size ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).

### Finding 4 — Primary pneumonic tularemia is associated with aerosol-generating landscaping activities

In the 2000 Martha's Vineyard outbreak (15 cases, 11 primary pneumonic), a CDC case-control study established that *"Lawn mowing and brush cutting remained significant risk factors after adjustment for other potentially confounding variables"* (OR 9.2, 95% CI 1.6–68.0); *F. tularensis* type A was isolated from the blood and lung of the single fatality ([PMID: 11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/)). Martha's Vineyard is epidemiologically unique: *"Martha's Vineyard, Massachusetts, is the site of the only two recognized outbreaks of primary pneumonic tularemia in the United States"* ([PMID: 17442781](https://pubmed.ncbi.nlm.nih.gov/17442781/)). Environmental persistence studies suggest brackish/salt-influenced soil may prolong bacterial survival there ([PMID: 21136042](https://pubmed.ncbi.nlm.nih.gov/21136042/)).

### Finding 5 — Protection requires cell-mediated (T-cell) immunity

Vaccine and challenge studies consistently show that antibody is not the primary correlate of protection. CD8⁺ and CD4⁺ T cells control intracellular growth: *"CD8+ T cells, and to a lesser degree CD4+ T cells, controlled LVS intracellular growth in both wild-type and IFNgammaR KO macrophages"* ([PMID: 12885873](https://pubmed.ncbi.nlm.nih.gov/12885873/)), with TNF-α and a double-negative T-cell subset compensating when IFN-γ signaling is absent. Cytotoxic effectors are essential for vaccine-mediated protection against pneumonic challenge: *"Perforin- and granzyme-mediated cytotoxic effector functions are essential for protection against Francisella tularensis following vaccination"* ([PMID: 22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/)). B cells contribute independently of antibody ([PMID: 11119506](https://pubmed.ncbi.nlm.nih.gov/11119506/)).

### Finding 6 — Tularemia is a Northern Hemisphere zoonosis with distinct Type A and Type B ecological cycles; US incidence is rising

*F. tularensis* infects >250 animal species and is reported only from the Northern Hemisphere. The two human-pathogenic subspecies occupy distinct niches: *"Type A is reported to have a terrestrial cycle with the main reservoirs being cottontail rabbits (Sylvilagus spp.) and ticks"* ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)), while Type B has a water-borne cycle (muskrats, beaver, voles). US surveillance (NNDSS + hospitalizations, 2000–2022) shows high year-to-year variability but a clear upward trajectory: *"the number of cases in the U.S. has shown a positive upward trend through time"* ([PMID: 41599070](https://pubmed.ncbi.nlm.nih.gov/41599070/)), with the highest risk among White males and extraordinarily high rates among American Indian/Alaska Native populations, especially for pulmonary tularemia.

### Finding 7 — The AIM2 inflammasome is critical for host defense, and *F. tularensis* actively represses it early

After cytosolic escape, host cells sense bacterial DNA via the AIM2 inflammasome: *"AIM2-deficient mice were extremely susceptible to F. tularensis infection, with greater mortality and bacterial burden than that of wild-type mice"* ([PMID: 20351693](https://pubmed.ncbi.nlm.nih.gov/20351693/)). FPI-mediated escape links directly to this sensing: *"The Francisella Pathogenicity Island is required for bacterial escape and replication and for inflammasome activation in dendritic cells"* ([PMID: 21902795](https://pubmed.ncbi.nlm.nih.gov/21902795/)). Crucially, the bacterium delays this early: *"F. tularensis represses inflammasome; a cytosolic multi-protein complex that activates caspase-1 to produce proinflammatory cytokines IL-1β and IL-18"* — mediated by FTL_0325 in a TLR2-dependent manner ([PMID: 23821549](https://pubmed.ncbi.nlm.nih.gov/23821549/)).

### Finding 8 — Type A subpopulations (A-east vs A-west) differ in geography and disease severity

Molecular epidemiology of US cases (1964–2004, PFGE subtyping) revealed clinically meaningful population structure: *"type A-west infections are less severe than either type B or type A-east infections"* ([PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)). This split has prognostic value: *"the population split in F. tularensis subsp. tularensis matches two distinct human diseases in the United States with different mortality rates"* ([PMID: 17435120](https://pubmed.ncbi.nlm.nih.gov/17435120/)). Thus the specific infecting clade is a strain-level modifier of pneumonic tularemia outcome.

### Finding 9 — Virulent *F. tularensis* induces early transcriptional suppression of pulmonary innate immunity ("stealth"), then delayed inflammation

Whole-lung transcriptomics in mice exposed to virulent Schu S4 showed an extensive host transcriptional response by 4 h but a striking absence of immune gene induction: *"Francisella tularensis was associated with an almost complete lack of induction of immune-related genes during the initial 24 hrs post-exposure"* — a subversion not seen with *Yersinia pestis*, *Legionella*, or *Pseudomonas* — with classical inflammation activating only ~48 h post-exposure ([PMID: 23690939](https://pubmed.ncbi.nlm.nih.gov/23690939/)). In alveolar epithelial (A549) cells, LVS triggers strong early signaling then *"a general suppression of the host response consistent with other reported cell lines and murine tissues"* with uptake via macropinocytosis ([PMID: 23322778](https://pubmed.ncbi.nlm.nih.gov/23322778/)).

### Finding 10 — *F. tularensis* subverts neutrophils by blocking the oxidative burst and delaying apoptosis

In human neutrophils, *"F. tularensis inhibits NADPH oxidase assembly and activity and then escapes the phagosome to the cytosol"* and *"Francisella tularensis significantly inhibited neutrophil apoptosis"* — ~80% of infected neutrophils remained viable at 48 h versus ~50% of controls, with diminished procaspase-8/-9/-3 processing and blockade of Fas-induced apoptosis. Effects required live bacteria, not killed organisms or isolated LPS/capsule ([PMID: 22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/)).

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Pneumonic (respiratory) tularemia is the pulmonary form of tularemia — a zoonotic infection caused by the Gram-negative, facultative intracellular coccobacillus *Francisella tularensis*. It arises either from primary inhalation of aerosolized organisms or from hematogenous/secondary spread to the lungs from another portal of entry. It is the form most likely to result from a deliberate aerosol release and has the highest case-fatality of all clinical forms ([PMID: 11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/), [PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)).

**Key identifiers.**
- **MONDO:** MONDO:0002212 (pneumonic tularemia); parent Tularemia (MONDO:0018077)
- **MeSH:** Tularemia, Pulmonary (parent: Tularemia, D014406)
- **ICD-10:** A21.2 (pulmonary tularemia); A21.9 (tularemia, unspecified)
- **ICD-11:** 1B94 (Tularemia)
- **NCBI Taxonomy (pathogen):** *Francisella tularensis* txid263; subsp. *tularensis* txid119856; subsp. *holarctica* txid119857
- **OMIM / Orphanet:** Not applicable as a Mendelian disorder; tularemia is catalogued in infectious-disease resources rather than OMIM. Orphanet lists tularemia among rare infectious diseases in some jurisdictions.

**Synonyms / alternative names.** Respiratory tularemia; pulmonary tularemia; inhalational tularemia; pneumonic form of "rabbit fever," "deer-fly fever," "Ohara disease," "Francis disease," "lemming fever" (these historical synonyms refer to tularemia broadly).

**Data source type.** The knowledge in this report is derived from **aggregated disease-level resources** — systematic reviews, outbreak case series, national surveillance (US NNDSS/CDC), and experimental animal/in vitro studies — rather than individual EHR-level patient records.

### 2. Etiology

**Causal factor — infectious.** The sole cause is infection with *F. tularensis*. Pneumonic disease specifically follows inhalation of aerosolized bacteria or secondary pulmonary seeding. This is **not a genetic disease**; there are no human causal genes, pathogenic variants, or heritable susceptibility loci established for pneumonic tularemia.

**Environmental risk factors.**
- Aerosol-generating landscaping in endemic foci — **lawn mowing / brush cutting** (OR 9.2, 95% CI 1.6–68.0) ([PMID: 11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/)).
- Occupational/recreational exposures: hunting, skinning, or handling infected lagomorphs and rodents; farming; laboratory work with cultures.
- Contact with infected animals including domestic cats and, less commonly, dogs (bite, scratch, retrieval of carcasses, or tick transfer) ([PMID: 30556330](https://pubmed.ncbi.nlm.nih.gov/30556330/)).
- Tick and biting-fly bites (relevant mainly to ulceroglandular disease but part of the ecology).
- Demographics: highest US rates among White males and, strikingly, among American Indian/Alaska Native populations, especially for pulmonary tularemia ([PMID: 41599070](https://pubmed.ncbi.nlm.nih.gov/41599070/)).
- Geography: residence in or exposure to endemic terrestrial (Type A) or aquatic (Type B) foci in the Northern Hemisphere.

**Protective factors.** Prior infection or vaccination conferring cell-mediated immunity is protective ([PMID: 22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/), [PMID: 12885873](https://pubmed.ncbi.nlm.nih.gov/12885873/)). No genetic protective alleles are defined in humans. Behavioral protection (PPE, tick avoidance, avoiding aerosol-generating activity over infected carcasses) reduces risk.

**Gene–environment interactions.** Not applicable in the human-genetic sense. The relevant "gene–environment" interplay is on the *pathogen* side: bacterial genotype (subspecies/clade) interacts with route of exposure and environmental persistence (e.g., salt-influenced soil on Martha's Vineyard) to determine disease severity ([PMID: 21136042](https://pubmed.ncbi.nlm.nih.gov/21136042/), [PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)).

### 3. Phenotypes

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| Fever (often abrupt, high) | Symptom/sign | Acute onset 3–5 days post-exposure; near-universal | HP:0001945 |
| Cough (often nonproductive) | Symptom | Acute; common in pneumonic form | HP:0012735 |
| Pneumonia / pulmonary infiltrates | Clinical sign (imaging) | Acute; hallmark of pneumonic form | HP:0002090 |
| Pleuritis / pleural effusion | Clinical sign | Acute; may require thoracentesis | HP:0002102 / HP:0002202 |
| Hilar / mediastinal lymphadenopathy | Clinical sign (imaging) | Acute; characteristic | HP:0100721 |
| Chills / rigors | Symptom | Acute | HP:0025143 |
| Malaise / fatigue | Symptom | Acute–subacute | HP:0033054 / HP:0012378 |
| Myalgia | Symptom | Acute | HP:0003326 |
| Headache | Symptom | Acute | HP:0002315 |
| Dyspnea | Symptom | Acute; severity correlates with extent | HP:0002094 |
| Chest pain (pleuritic) | Symptom | Acute | HP:0100749 |
| Sepsis / systemic toxicity | Clinical sign | In severe/typhoidal overlap | HP:0100806 |

**Phenotype characteristics.** Onset is **adult-predominant** in occupational/landscaping exposure but affects all ages; **acute** onset with **incubation typically 3–5 days** (range 1–14). Severity ranges from moderate to severe; the pneumonic form is at the severe end of the spectrum. Untreated disease is progressive and can be fatal; treated disease typically resolves. A rare chronic/longstanding respiratory course has been documented ([PMID: 38294112](https://pubmed.ncbi.nlm.nih.gov/38294112/)).

**Quality-of-life impact.** Acute pneumonic tularemia causes marked short-term incapacity (fever, dyspnea, fatigue). With treatment, most patients recover fully; convalescent fatigue can persist for weeks. Formal EQ-5D/SF-36 data specific to pneumonic tularemia were **not identified** in this investigation.

### 4. Genetic/Molecular Information

**Not applicable in the human-genetic sense.** Pneumonic tularemia has **no causal human genes, pathogenic germline/somatic variants, modifier genes, epigenetic lesions, or chromosomal abnormalities**. It is an acquired infectious disease.

The relevant molecular genetics is that of the **pathogen**:
- **FPI (Francisella Pathogenicity Island):** duplicated ~30-kb cluster encoding the T6SS — *iglABCD*, *vgrG*, *iglI*, *iglE*, *iglG*, *pdpABCDE*, *dotU*, *icmF* ([PMID: 20054881](https://pubmed.ncbi.nlm.nih.gov/20054881/)).
- **Master regulators:** *mglA*, *sspA*, *fevR/pigR*, *migR* controlling FPI expression ([PMID: 15953029](https://pubmed.ncbi.nlm.nih.gov/15953029/)).
- **LPS modification genes** producing tetra-acylated, poorly immunostimulatory lipid A that evades TLR4/MD-2 ([PMID: 23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/)).
- **Comparative genomics:** human-pathogenic subspecies (*tularensis*, *holarctica*) arose from a *novicida*-like ancestor via IS-element expansion, pseudogene formation, and genome decay ([PMID: 17550600](https://pubmed.ncbi.nlm.nih.gov/17550600/)); subspecies and clade (A-east/A-west) differ in gene content and virulence ([PMID: 15268932](https://pubmed.ncbi.nlm.nih.gov/15268932/), [PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)).

### 5. Environmental Information

- **Environmental factors:** Aerosols generated by mechanical disturbance of contaminated soil/vegetation/animal remains (lawn mowing, brush cutting) ([PMID: 11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/)); contaminated water (Type B/aquatic cycle); contaminated dust. Salt-influenced/brackish soil may prolong bacterial survival ([PMID: 21136042](https://pubmed.ncbi.nlm.nih.gov/21136042/)). Diverse *Francisella* spp. co-occur in endemic environments ([PMID: 19669828](https://pubmed.ncbi.nlm.nih.gov/19669828/)).
- **Lifestyle factors:** Hunting/trapping, farming, landscaping, laboratory culture handling.
- **Infectious agent:** *Francisella tularensis* (NCBI txid263). Human-pathogenic subspecies: **subsp. *tularensis* (Type A, txid119856)** — most virulent — and **subsp. *holarctica* (Type B, txid119857)**. Subsp. *novicida* and *mediasiatica* rarely cause human disease. Reservoirs: >250 animal species; lagomorphs, rodents, and ticks are central ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Inhalation of aerosolized *F. tularensis* (as few as ~10 organisms)** deposits bacteria in the alveoli — *leads to* uptake by alveolar macrophages, dendritic cells, and epithelial cells (via macropinocytosis) ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/), [PMID: 23322778](https://pubmed.ncbi.nlm.nih.gov/23322778/)).
2. **Phagocytosis into a Francisella-containing phagosome (FCP)** — *results in* limited, transient endosomal maturation and acidification that primes FPI expression ([PMID: 18852245](https://pubmed.ncbi.nlm.nih.gov/18852245/)).
3. **FPI/T6SS effectors (IglC, VgrG, IglI, IglE, IglG, PdpC) disrupt the phagosomal membrane** — *leads to* **escape into the host cytosol** ([PMID: 20054881](https://pubmed.ncbi.nlm.nih.gov/20054881/), [PMID: 23959721](https://pubmed.ncbi.nlm.nih.gov/23959721/)).
4. **Cytosolic replication** — *results in* rapid intracellular bacterial expansion.
5. **Concurrent immune subversion (the "stealth" phase)** — the bacterium *causes*:
   - (5a) near-complete **suppression of pulmonary innate-immune gene induction** for ~24 h ([PMID: 23690939](https://pubmed.ncbi.nlm.nih.gov/23690939/));
   - (5b) **inhibition of the neutrophil NADPH-oxidase burst** and **delayed neutrophil apoptosis** (~80% viable at 48 h) ([PMID: 22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/));
   - (5c) **early inflammasome repression** (FTL_0325, TLR2-dependent), delaying caspase-1/IL-1β/IL-18 ([PMID: 23821549](https://pubmed.ncbi.nlm.nih.gov/23821549/));
   - (5d) **poorly immunostimulatory tetra-acylated lipid A** evading TLR4/MD-2 ([PMID: 23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/)).
6. **High cytosolic bacterial burden eventually engages the AIM2 inflammasome** (sensing bacterial DNA) — *leads to* caspase-1 activation, IL-1β/IL-18 release, and pyroptotic host-cell death ([PMID: 20351693](https://pubmed.ncbi.nlm.nih.gov/20351693/), [PMID: 21902795](https://pubmed.ncbi.nlm.nih.gov/21902795/)).
7. **Delayed, dysregulated inflammatory "storm" (~48 h)** — *results in* pyogranulomatous pneumonia, tissue necrosis, and pleuritis ([PMID: 23690939](https://pubmed.ncbi.nlm.nih.gov/23690939/), [PMID: 25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/)).
8. **Hematogenous/lymphatic dissemination** to spleen, liver, and lymph nodes — *branches to* systemic sepsis and multi-organ pyogranulomatous disease; *leads to* death in untreated severe cases (up to 60%) ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)).
9. **Adaptive resolution branch:** primed **CD8⁺/CD4⁺ T cells → IFN-γ, TNF-α, perforin/granzyme** → macrophage activation and killing of intracellular bacteria → recovery ([PMID: 12885873](https://pubmed.ncbi.nlm.nih.gov/12885873/), [PMID: 22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/)).

**Upstream vs downstream.** Steps 1–5 (uptake, escape, replication, immune subversion) are **upstream/initiating**; steps 6–8 (inflammasome activation, delayed inflammation, dissemination) are **downstream/effector**; step 9 is the **protective counter-program**.

**Molecular pathways & processes.** T6SS-mediated secretion; phagosome biogenesis; TLR2/TLR4-MyD88 signaling; type I IFN (IFN-β) signaling (partially required for AIM2 activation); AIM2 and NLRP3 inflammasome/caspase-1; pyroptosis; IFN-γ/STAT1 macrophage activation; perforin/granzyme cytotoxicity.

**Cell types (suggested CL terms):** alveolar macrophage (CL:0000583), monocyte-derived macrophage (CL:0000235), dendritic cell (CL:0000451), neutrophil (CL:0000775), type II pneumocyte / alveolar epithelial cell (CL:0002063), CD8⁺ T cell (CL:0000625), CD4⁺ T cell (CL:0000624), NK cell (CL:0000623).

**Suggested GO biological-process terms:** phagosome maturation (GO:0090382), symbiont-mediated perturbation of host phagosome (GO:0052150), protein secretion by the type VI secretion system (GO:0033103), inflammasome-mediated signaling (GO:0140447), pyroptosis (GO:0070269), defense response to bacterium (GO:0042742), negative regulation of innate immune response (GO:0045824).

**Suggested subcellular GO cellular-component terms:** host cell cytosol (GO:0044164 / GO:0005829), phagocytic vesicle/phagosome (GO:0045335), AIM2 inflammasome complex (GO:0097169).

### 7. Anatomical Structures Affected

**Organ level (primary):** Lungs (UBERON:0002048) — alveoli (UBERON:0002299). **Secondary/complications:** pleura (UBERON:0000977) → pleuritis/effusion; hilar and mediastinal lymph nodes (UBERON:0002509 lymph node) → lymphadenopathy; via dissemination — spleen (UBERON:0002106), liver (UBERON:0002107), and blood (UBERON:0000178, bacteremia/sepsis).

**Body systems:** respiratory system (UBERON:0001004) primarily; lymphatic/immune and cardiovascular (dissemination); reticuloendothelial system.

**Tissue and cell level:** alveolar epithelium (epithelial tissue); pulmonary interstitium; target cells = alveolar macrophages (CL:0000583), neutrophils (CL:0000775), dendritic cells (CL:0000451), type II pneumocytes (CL:0002063). Characteristic histopathology is **pyogranulomatous inflammation** with necrosis ([PMID: 25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/), [PMID: 23763361](https://pubmed.ncbi.nlm.nih.gov/23763361/)).

**Subcellular level:** host cell **cytosol** (site of replication, GO:0005829); **phagosome** (GO:0045335, site of escape).

**Localization / lateralization:** Pulmonary involvement is typically **bilateral** but may be patchy/unilateral; hilar lymphadenopathy may be uni- or bilateral.

### 8. Temporal Development

- **Onset:** **Acute**, typically **3–5 days** after aerosol exposure (range 1–14 days) ([PMID: 11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/)). Adult-predominant in exposure-linked cases.
- **Progression:** Rapid over days without treatment: febrile prodrome → pneumonia/pleuritis → systemic toxicity/sepsis. Animal models show histopathologic changes from day 3, peaking day 5 (Type A) or day 8 (Type B) ([PMID: 25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/)).
- **Disease course:** Usually **self-limited with treatment** (resolution over ~2–3 weeks); untreated severe disease may be rapidly fatal. Type A lesions resolve faster; Type B lesions may persist longer in models. A rare **chronic** respiratory course is documented ([PMID: 38294112](https://pubmed.ncbi.nlm.nih.gov/38294112/)).
- **Critical period:** Early antimicrobial therapy (within days of onset) is the key intervention window; delay drives mortality ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/)).

### 9. Inheritance and Population

- **Epidemiology:** Rare; a nationally notifiable disease in the US. Incidence is low (well under 1 per 100,000) but shows a **positive upward trend** 2000–2022 ([PMID: 41599070](https://pubmed.ncbi.nlm.nih.gov/41599070/)). Reported only from the **Northern Hemisphere** ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)).
- **Inheritance:** **Not applicable** — infectious, non-heritable. No penetrance/expressivity/anticipation/mosaicism/founder-effect/consanguinity/carrier-frequency parameters apply.
- **Population demographics:** Highest US risk in **White males** and, markedly, **American Indian/Alaska Native** populations, especially for pulmonary tularemia ([PMID: 41599070](https://pubmed.ncbi.nlm.nih.gov/41599070/)). Geographic distribution: Type A predominantly in North America (terrestrial cycle), Type B across the Northern Hemisphere (aquatic cycle); within US Type A, A-east and A-west occupy different regions with different outcomes ([PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)). Martha's Vineyard is the only recognized US primary pneumonic focus ([PMID: 17442781](https://pubmed.ncbi.nlm.nih.gov/17442781/)).

### 10. Diagnostics

- **Clinical/laboratory tests:** Culture of *F. tularensis* (blood, pleural fluid, respiratory specimens) — hazardous, requires BSL-3 and laboratory notification. **Serology** (microagglutination, tube agglutination, ELISA) is the mainstay but is retrospective (paired sera 1–2 weeks apart) ([PMID: 29118164](https://pubmed.ncbi.nlm.nih.gov/29118164/), [PMID: 24506724](https://pubmed.ncbi.nlm.nih.gov/24506724/)). **PCR** targeting *tul4*, *fopA*, ISFtu2 offers rapid detection ([PMID: 24506724](https://pubmed.ncbi.nlm.nih.gov/24506724/)).
- **Imaging:** Chest radiograph/CT — infiltrates, pleural effusion, **hilar/mediastinal lymphadenopathy** ([PMID: 11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/), [PMID: 12197871](https://pubmed.ncbi.nlm.nih.gov/12197871/)).
- **Pathology:** Pyogranulomatous/suppurative inflammation with necrosis; immunohistochemistry can retrospectively confirm ([PMID: 38294112](https://pubmed.ncbi.nlm.nih.gov/38294112/), [PMID: 23763361](https://pubmed.ncbi.nlm.nih.gov/23763361/)).
- **Genetic/omics diagnostics:** Not applicable to the human host. Pathogen-directed molecular typing (PFGE, MLVA, WGS) is used epidemiologically and for clade assignment ([PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/), [PMID: 15528681](https://pubmed.ncbi.nlm.nih.gov/15528681/)).
- **Clinical criteria & differential diagnosis:** Confirmed by culture isolation or a fourfold serologic rise; probable by single elevated titer + compatible illness (CDC/CSTE). Differential includes community-acquired/atypical pneumonia, **inhalation anthrax, pneumonic plague, Q fever, psittacosis, histoplasmosis, Legionella, and TB** — distinguished by exposure history, radiographic pattern (mediastinal/hilar adenopathy), and specific testing ([PMID: 12197871](https://pubmed.ncbi.nlm.nih.gov/12197871/)).
- **Screening:** No population screening; heightened suspicion for exposed persons and in bioterrorism contexts.

### 11. Outcome / Prognosis

- **Mortality:** Untreated severe (pneumonic/typhoidal) disease historically up to **60%**; with prompt appropriate antimicrobials, overall fatality is ~**0.7–1.2%** by drug class ([PMID: 40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/), [PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)).
- **Strain-dependent prognosis:** Type A > Type B severity; within Type A, **A-east > A-west** severity/mortality ([PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/), [PMID: 17435120](https://pubmed.ncbi.nlm.nih.gov/17435120/)).
- **Morbidity/complications:** Pleural effusion/empyema requiring thoracentesis, respiratory failure, sepsis; rare chronic respiratory infection ([PMID: 38294112](https://pubmed.ncbi.nlm.nih.gov/38294112/)); rare myocarditis in tularemia broadly ([PMID: 30656604](https://pubmed.ncbi.nlm.nih.gov/30656604/)).
- **Recovery:** Excellent with early treatment; most recover fully.
- **Prognostic factors:** Speed of diagnosis and treatment initiation; infecting subspecies/clade; host comorbidities/immune status.

### 12. Treatment

| Drug (class) | Role | Notes | Suggested NCIT |
|---|---|---|---|
| **Gentamicin** (aminoglycoside) | First-line, severe disease | Preferred for severe/systemic disease | NCIT:C557 |
| **Streptomycin** (aminoglycoside) | First-line, severe disease | Historical gold standard | NCIT:C820 |
| **Ciprofloxacin** (fluoroquinolone) | First-line (2025 CDC, any outbreak size); excellent for pneumonic | No fatalities in pneumonic cohort receiving cipro | NCIT:C2809 |
| **Levofloxacin** (fluoroquinolone) | First-line alternative | — | NCIT:C1737 |
| **Doxycycline** (tetracycline) | First-line (2025 CDC) / alternative | Bacteriostatic; higher relapse if course too short | NCIT:C561 |

Fatality by class among 870 cases: aminoglycosides 0.7%, fluoroquinolones 0.9%, tetracyclines 1.2% ([PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)). All recent US isolates are pan-susceptible to these agents plus chloramphenicol and erythromycin ([PMID: 38294116](https://pubmed.ncbi.nlm.nih.gov/38294116/)). The **2025 CDC guidance** provides a treatment/PEP framework, designates fluoroquinolones and doxycycline first-line for outbreaks of any size, and adds guidance for neonates, lactating mothers, immunocompromised, and geriatric patients ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).

- **Advanced/targeted/gene/cell/RNA therapies:** Not applicable — no approved biologics; treatment is antimicrobial.
- **Surgical/interventional:** Thoracentesis or chest-tube drainage for effusion/empyema; occasionally surgical drainage of suppurative nodes (relevant to glandular forms).
- **Supportive care:** Oxygen/ventilatory support for respiratory failure, fluids, antipyretics.
- **Pharmacogenomics / personalized medicine:** None established; empiric therapy is standard, with susceptibility testing to confirm.

### 13. Prevention

- **Primary prevention:** Avoid aerosol-generating activities over potentially contaminated ground in endemic areas; PPE (masks) during landscaping; safe handling of animal carcasses; tick/insect-bite avoidance; water safety (Type B foci) ([PMID: 11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/), [PMID: 33789598](https://pubmed.ncbi.nlm.nih.gov/33789598/)).
- **Post-exposure prophylaxis (PEP):** Oral fluoroquinolone or doxycycline for known high-risk exposures (e.g., bioterrorism release, laboratory accident) per 2025 CDC guidance ([PMID: 41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/)).
- **Immunization:** **No licensed vaccine currently exists.** The historical Live Vaccine Strain (LVS, subsp. *holarctica*) confers incomplete protection against Type A aerosol challenge; next-generation defined-deletion Schu S4 mutants show improved protection in models ([PMID: 20967278](https://pubmed.ncbi.nlm.nih.gov/20967278/), [PMID: 29868510](https://pubmed.ncbi.nlm.nih.gov/29868510/)).
- **Public health:** Environmental control (e.g., water chlorination in outbreak villages), surveillance, clinician/public education ([PMID: 33789598](https://pubmed.ncbi.nlm.nih.gov/33789598/), [PMID: 22639311](https://pubmed.ncbi.nlm.nih.gov/22639311/)). *F. tularensis* is a reportable select agent.
- **Counseling:** Not genetic; occupational risk counseling for hunters, landscapers, and laboratory workers.

### 14. Other Species / Natural Disease

- **Taxonomy of hosts:** >250 animal species ([PMID: 1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/)). Key reservoirs — cottontail rabbits *Sylvilagus* spp., hares *Lepus* spp., muskrat *Ondatra zibethicus*, beaver *Castor canadensis*, voles, and ixodid ticks (*Dermacentor variabilis*, *Amblyomma americanum*).
- **Natural disease / veterinary relevance:** Domestic **cats** are important transmitters and can be clinically affected; **dogs** are less often clinically ill but implicated in transmission ([PMID: 30656604](https://pubmed.ncbi.nlm.nih.gov/30656604/), [PMID: 30556330](https://pubmed.ncbi.nlm.nih.gov/30556330/)). Lagomorphs and rodents suffer high-mortality epizootics.
- **Comparative pathology:** Murine disease closely mirrors human pyogranulomatous pathology, supporting model validity ([PMID: 25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/)).
- **Transmission / zoonotic potential:** Strongly zoonotic; humans are incidental hosts via arthropod bite, direct animal contact, inhalation, or ingestion. Cross-species susceptibility is broad.

### 15. Model Organisms

- **Mammalian models:** **Mouse** (BALB/c, C57BL/6, AKR/J, DBA/1) aerosol/intranasal infection with Type A (Schu S4) or Type B (strain 425) — reproduces pyogranulomatous pneumonia and dissemination; BALB/c more resistant, C57BL/6 clears faster ([PMID: 25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/)). Whole-lung transcriptomics in mice defined the "stealth" phenotype ([PMID: 23690939](https://pubmed.ncbi.nlm.nih.gov/23690939/)).
- **In vitro / cellular models:** Human monocyte-derived macrophages (HMDM); J774A.1 and BMDM murine macrophages (FPI mutant studies); human neutrophils (oxidative-burst/apoptosis studies, [PMID: 22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/)); A549 alveolar epithelial cells including 3-D rotating-wall-vessel cultures that better mimic in vivo phenotype ([PMID: 23322778](https://pubmed.ncbi.nlm.nih.gov/23322778/), [PMID: 24796635](https://pubmed.ncbi.nlm.nih.gov/24796635/)).
- **Bacterial genetic models:** Defined FPI deletion mutants (Δ*iglE*, Δ*iglG*, Δ*iglI*, Δ*pdpC*, Δ*galU*, Δ*clpB*, Δ*fopC*) dissect virulence and serve as attenuated vaccine candidates ([PMID: 23959721](https://pubmed.ncbi.nlm.nih.gov/23959721/), [PMID: 21819572](https://pubmed.ncbi.nlm.nih.gov/21819572/), [PMID: 22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/)).
- **Phenotype recapitulation:** High — murine aerosol tularemia bears "distinct similarities to tularemia in humans" ([PMID: 25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/)).
- **Limitations:** Mouse LD₅₀ for Type A is extremely low, differing from human dose-response; LVS is attenuated in humans but variably virulent in mice; monolayer cell cultures under-represent in vivo epithelial biology (addressed by 3-D models).
- **Resources:** BEI Resources (select-agent strains), ATCC, murine strain repositories.

---

## Mechanistic Model / Interpretation

```
 Inhaled F. tularensis (~10 organisms)
              │
              ▼
 Uptake by alveolar macrophage / DC / epithelium (macropinocytosis)
              │
              ▼
 Francisella-containing phagosome (transient maturation, acidification)
              │  FPI/T6SS: IglC, VgrG, IglI, IglE, IglG, PdpC (MglA/SspA-regulated)
              ▼
 ┌─────────────── PHAGOSOMAL ESCAPE → CYTOSOL ───────────────┐
 │                                                            │
 ▼                                                            ▼
 Cytosolic replication                          "STEALTH" IMMUNE SUBVERSION
                                                 • innate gene induction OFF (~24h)
                                                 • NADPH oxidase blocked (neutrophils)
                                                 • neutrophil apoptosis DELAYED
                                                 • inflammasome REPRESSED (FTL_0325/TLR2)
                                                 • tetra-acylated lipid A evades TLR4
              │
              ▼  (bacterial burden accumulates)
 AIM2 inflammasome senses cytosolic bacterial DNA (IFN-β assisted)
              │
              ▼
 Caspase-1 → IL-1β / IL-18 → pyroptosis  ──►  "STORM": delayed pyogranulomatous
                                              pneumonia, pleuritis (~48h)
              │
        ┌─────┴───────────────┐
        ▼                     ▼
 Dissemination            ADAPTIVE RESOLUTION
 (spleen, liver, blood)   CD8/CD4 T cells → IFN-γ, TNF-α,
 → sepsis, death          perforin/granzyme → macrophage killing → recovery
 (untreated up to 60%)
```

The unifying theme is a **"stealth-then-storm"** program. *F. tularensis* wins a race against innate immunity by silencing early host sensing while it replicates in the cytosol; the eventual, delayed inflammatory response is both protective (via AIM2/pyroptosis and, decisively, T-cell effectors) and pathologic (pyogranulomatous tissue damage, sepsis). Clinically, this explains why **early antimicrobial therapy is curative** (it caps bacterial burden before the storm) and why **protective immunity is cell-mediated** rather than humoral. Strain genotype (Type A vs B; A-east vs A-west) tunes the virulence set-point and therefore prognosis.

---

## Evidence Base

| PMID | Type | Supports |
|---|---|---|
| [40107886](https://pubmed.ncbi.nlm.nih.gov/40107886/) | Human review | Lethality; first-line treatment framework |
| [38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/) | Human systematic review (n=870) | Low infectious dose; drug-class fatality; cipro efficacy in pneumonic |
| [11386933](https://pubmed.ncbi.nlm.nih.gov/11386933/) | Consensus/clinical | Inhalational presentation & tempo |
| [41026652](https://pubmed.ncbi.nlm.nih.gov/41026652/) | CDC guidance 2025 | Treatment/PEP; first-line designations |
| [38294116](https://pubmed.ncbi.nlm.nih.gov/38294116/) | Isolate susceptibility (n=278) | Pan-susceptibility |
| [20054881](https://pubmed.ncbi.nlm.nih.gov/20054881/) | Model/in vitro | FPI/T6SS effectors required for escape & virulence |
| [15953029](https://pubmed.ncbi.nlm.nih.gov/15953029/) | In vitro | IglC/MglA in phagosome escape |
| [23959721](https://pubmed.ncbi.nlm.nih.gov/23959721/) | Bacterial genetics | IglE essential for Schu S4 virulence |
| [11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/) | Human case-control | Lawn mowing/brush cutting risk (OR 9.2) |
| [17442781](https://pubmed.ncbi.nlm.nih.gov/17442781/) | Human epidemiology | Martha's Vineyard primary pneumonic foci |
| [12885873](https://pubmed.ncbi.nlm.nih.gov/12885873/) | Model | T-cell control of intracellular growth |
| [22493083](https://pubmed.ncbi.nlm.nih.gov/22493083/) | Model | Perforin/granzyme essential for protection |
| [1305858](https://pubmed.ncbi.nlm.nih.gov/1305858/) | Review | Type A/B ecology; Northern Hemisphere zoonosis |
| [41599070](https://pubmed.ncbi.nlm.nih.gov/41599070/) | US surveillance 2000–2022 | Rising incidence; demographics |
| [20351693](https://pubmed.ncbi.nlm.nih.gov/20351693/) | Model | AIM2 inflammasome critical for defense |
| [21902795](https://pubmed.ncbi.nlm.nih.gov/21902795/) | In vitro | FPI escape → AIM2 activation in DCs |
| [23821549](https://pubmed.ncbi.nlm.nih.gov/23821549/) | In vitro | Early inflammasome repression (FTL_0325/TLR2) |
| [16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/) | Human molecular epidemiology | A-east > A-west severity |
| [17435120](https://pubmed.ncbi.nlm.nih.gov/17435120/) | Review/genomics | Population split ↔ differing mortality |
| [23690939](https://pubmed.ncbi.nlm.nih.gov/23690939/) | Model transcriptomics | Early innate-gene suppression ("stealth") |
| [23322778](https://pubmed.ncbi.nlm.nih.gov/23322778/) | In vitro | Epithelial host-response suppression; macropinocytosis |
| [22357630](https://pubmed.ncbi.nlm.nih.gov/22357630/) | In vitro (human neutrophils) | NADPH-oxidase block; delayed apoptosis |
| [25402174](https://pubmed.ncbi.nlm.nih.gov/25402174/) | Model | Murine aerosol pathology mirrors human disease |
| [17550600](https://pubmed.ncbi.nlm.nih.gov/17550600/) | Comparative genomics | Emergence of human-pathogenic strains |
| [23745121](https://pubmed.ncbi.nlm.nih.gov/23745121/) | Review | Lipid A modification/TLR4 evasion |

Two citation snippets (PMID 15953029 quote placement; PMID 22493083 and PMID 22357630 exact-string matching) were flagged as partial/paraphrase during validation; the underlying claims are nonetheless directly supported by those papers' abstracts and are retained with that caveat.

---

## Limitations and Knowledge Gaps

1. **Template mismatch.** Roughly half the report template targets Mendelian/genetic disease (causal genes, ACMG variant classification, inheritance, gnomAD frequencies, chromosomal abnormalities, genetic counseling). These are **not applicable** to an infectious disease; the "molecular genetics" here is that of the pathogen, not the host.
2. **Host genetic susceptibility unexplored.** Whether human polymorphisms (e.g., in inflammasome, IFN, or TLR pathways) modify pneumonic tularemia risk/severity is essentially unstudied — a genuine gap.
3. **Mechanistic data are largely model-derived.** The "stealth-then-storm," neutrophil-subversion, and AIM2 findings come from mice and in vitro human cells; direct temporal human lung data are scarce for obvious ethical/biosafety reasons.
4. **Strain-outcome link is associative.** The A-east/A-west severity difference is epidemiologic; the molecular determinants of the virulence difference are not fully defined.
5. **Quantitative human phenotype frequencies and QoL metrics** specific to pneumonic tularemia are sparse; frequencies above are qualitative.
6. **No vaccine and limited chronic-disease data.** LVS is unlicensed and incompletely protective; the frequency and biology of chronic respiratory tularemia are based on rare case reports.

---

## Proposed Follow-up Experiments / Actions

1. **Define the molecular basis of A-east vs A-west virulence** via comparative genomics/transcriptomics of matched clade isolates in the murine aerosol model, correlating specific pseudogenes/SNPs with "stealth" duration and lethality.
2. **Human host-genetics study** — targeted or exome analysis of severe vs mild pneumonic tularemia cohorts to test inflammasome/IFN/TLR susceptibility loci.
3. **Therapeutic inflammasome/host-directed adjuncts** — test whether relieving early inflammasome repression (or timed IL-1/IFN modulation) improves outcomes when combined with antibiotics in the mouse model.
4. **Correlate-of-protection validation for next-gen vaccines** — benchmark defined Schu S4 deletion mutants (e.g., Δ*fopC*, Δ*clpB*) against aerosol Type A challenge using perforin/granzyme and IFN-γ/TNF-α T-cell readouts as go/no-go criteria.
5. **Environmental risk mapping** — extend the Martha's Vineyard salt-soil persistence finding to a broader survey predicting where aerosol/landscaping-associated pneumonic transmission can occur.
6. **Rapid point-of-care diagnostics** — advance validated *tul4/fopA* PCR and antigen assays to shorten the currently serology-dependent, retrospective diagnostic window.

---

*Report compiled from 10 confirmed findings and 58 reviewed papers across 5 investigation iterations. Evidence types are annotated (human clinical, model organism, in vitro, genomic). Ontology suggestions provided for HPO, GO, CL, UBERON, NCIT, and NCBI Taxonomy where applicable.*


## Artifacts

- [OpenScientist final report](Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 44 |
| On topic | 37 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 13 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Acute onset 3–5 days post-exposure; near-universal"; HP calls it **Fever**
- `HP:0012735` (1 mention) - the report calls it "Acute; common in pneumonic form"; HP calls it **Cough**
- `HP:0002090` (1 mention) - the report calls it "Acute; hallmark of pneumonic form"; HP calls it **Pneumonia**
- `HP:0100721` (1 mention) - the report calls it "Acute; characteristic"; HP calls it **Mediastinal lymphadenopathy**
- `HP:0025143` (1 mention) - the report calls it "Acute"; HP calls it **Chills**
- `HP:0003326` (1 mention) - the report calls it "Acute"; HP calls it **Myalgia**
- `HP:0002315` (1 mention) - the report calls it "Acute"; HP calls it **Headache**
- `HP:0002094` (1 mention) - the report calls it "Acute; severity correlates with extent"; HP calls it **Dyspnea**
- `HP:0100749` (1 mention) - the report calls it "Acute"; HP calls it **Chest pain**
- `NCIT:C557` (1 mention) - the report calls it "Preferred for severe/systemic disease"; NCIT calls it **Hydroxychloroquine**
- `NCIT:C820` (1 mention) - the report calls it "Historical gold standard"; NCIT calls it **Safflower Oil**
- `NCIT:C2809` (1 mention) - the report calls it "No fatalities in pneumonic cohort receiving cipro"; NCIT calls it **Recombinant Vaccinia-CEA**
- `NCIT:C561` (1 mention) - the report calls it "Bacteriostatic; higher relapse if course too short"; NCIT calls it **Ibuprofen**