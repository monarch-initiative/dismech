---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T02:12:40.775748'
end_time: '2026-09-28T02:27:53.551139'
duration_seconds: 912.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rickettsia Helvetica Spotted Fever
  mondo_id: MONDO:0000331
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 21
  relevance_assessed: 27
  on_topic: 25
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 5
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0000331
    reported_labels:
    - spotted fever group rickettsiosis parent
    - spotted fever
    - spotted fever group parent term
    ontology_label: Rickettsia helvetica spotted fever
  - term_id: HP:0001945
    reported_labels:
    - Common; warm season; mild
    ontology_label: Fever
  - term_id: HP:0002315
    reported_labels:
    - Common
    ontology_label: Headache
  - term_id: HP:0003326
    reported_labels:
    - Common
    ontology_label: Myalgia
  - term_id: GO:0006928
    reported_labels:
    - movement of cell / actin-based motility
    ontology_label: obsolete movement of cell or subcellular component
  - term_id: NCIT:C557
    reported_labels:
    - Doxycycline
    - First-line:** **Doxycycline
    ontology_label: Hydroxychloroquine
  - term_id: HP:0002716
    reported_labels:
    - TIBOLA/SENLAT-like cases
    ontology_label: Lymphadenopathy
  - term_id: HP:0100785
    reported_labels:
    - Rare
    ontology_label: Insomnia
  - term_id: HP:0001657
    reported_labels:
    - pericarditis
    ontology_label: Prolonged QT interval
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0006928
    ontology_label: obsolete movement of cell or subcellular component
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Rickettsia_Helvetica_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Rickettsia_Helvetica_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rickettsia Helvetica Spotted Fever
- **MONDO ID:** MONDO:0000331 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rickettsia Helvetica Spotted Fever** covering all of the
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

# Rickettsia helvetica Spotted Fever — Comprehensive Disease Characteristics Report

**Disease:** Rickettsia helvetica Spotted Fever
**MONDO ID:** MONDO:0000331 (spotted fever group rickettsiosis parent)
**Category:** Infectious Disease (tick-borne bacterial zoonosis)
**Causative organism:** *Rickettsia helvetica* (NCBI:txid35789), spotted fever group (SFG) Rickettsiaceae

---

## Summary

*Rickettsia helvetica* spotted fever is an emerging, generally mild tick-borne rickettsiosis caused by the obligate intracellular gram-negative bacterium *Rickettsia helvetica*, a member of the spotted fever group (SFG) of the genus *Rickettsia*. It is transmitted principally by the European sheep tick *Ixodes ricinus* and is the only non-imported rickettsia known to circulate in Scandinavia. The disease is best characterized clinically by an **aneruptive (rashless) febrile illness** accompanied by headache and myalgia during the warm season — a presentation that distinguishes it from most other SFG rickettsioses, which typically produce a rash and/or an inoculation eschar. A recognized but rare severe end of the spectrum includes lymphocytic meningitis, neuritis (facial palsy/sudden deafness associations), and chronic perimyocarditis linked to sudden cardiac death. Localized skin lesions, eschar, and regional lymphadenopathy (a TIBOLA/SENLAT-like picture) have also been documented at tick-bite sites, broadening the clinical spectrum beyond the classical "rashless fever."

Mechanistically, the organism is inoculated by a feeding tick, replicates within human monocytes/macrophages (an early cellular target), and disseminates to its ultimate target — the vascular endothelium — producing the perivascular and vasculitic lesions seen in skin capillaries and cardiac tissue. In vitro, *R. helvetica* exhibits actin-based intracellular motility, expresses the surface cell antigen Sca4, invades neurons, and can grow within the host-cell nucleus, features relevant to cell-to-cell spread and central nervous system involvement. Because the disease is purely infectious/environmental in origin, there is **no heritable genetic cause, no causal human gene, and no inheritance pattern**; sections of the research template dealing with germline genetics, chromosomal abnormalities, and Mendelian inheritance are not applicable.

Diagnosis rests on serology (indirect immunofluorescence assay, IFA, requiring a four-fold IgG titre rise) and molecular detection (PCR/sequencing of rickettsial genes such as *16S rRNA*, *17-kDa* protein, *gltA*, *ompA*, *ompB*, and *sca4*), with lesion capillary blood and cerebrospinal fluid outperforming whole blood. **Doxycycline is the treatment of choice for patients of all ages**, and the prognosis is generally excellent, with the great majority of infections being asymptomatic seroconversions or self-limited flu-like illness. No vaccine exists; prevention relies on tick-bite avoidance and prompt tick removal. An early hypothesis linking *R. helvetica* to sarcoidosis pathogenesis has been repeatedly refuted.

---

## Key Findings

### 1. Definition, taxonomy, vector, and clinical triad (F001)

*Rickettsia helvetica* is an emerging human pathogen within the spotted fever group of rickettsiae, transmitted by *Ixodes ricinus*, and associated with three recognized human manifestations: aneruptive (rashless) febrile illness, meningitis, and sudden death in chronic perimyocarditis. It holds the distinction of being **the only non-imported rickettsia found in Scandinavia**, first detected in *I. ricinus* ticks before any human disease link was established.

> "Rickettsia helvetica is an emerging human pathogen, belonging to the spotted fever group (SFG) rickettsiae, associated with generally aneruptive fever, meningitis, and sudden death in chronic perimyocarditis." — [PMID: 29664700](https://pubmed.ncbi.nlm.nih.gov/29664700/)

> "Rickettsia helvetica is the only non-imported rickettsia found in Scandinavia. It was first detected in Ixodes ricinus ticks, but has never been linked to human disease." — [PMID: 10513711](https://pubmed.ncbi.nlm.nih.gov/10513711/) (statement predates the perimyocarditis link established in that same landmark paper)

**Ontology suggestions:** MONDO:0000331 (spotted fever); NCBITaxon:35789 (*Rickettsia helvetica*); NCBITaxon:34613 (*Ixodes ricinus*).

### 2. Typical presentation — mild aneruptive febrile illness (F002)

In a landmark case series of eight patients from France, Italy, and Thailand with serological evidence of infection (Fournier et al. 2004), the disease presented as a **mild, warm-season illness with fever, headache, and myalgia but without a cutaneous rash** — hence "aneruptive fever." This is a key differentiator from other SFG rickettsioses (e.g., Mediterranean spotted fever, Rocky Mountain spotted fever), which characteristically produce rash and/or eschar.

> "The infection presented as a mild disease in the warm season and was associated with fever, headache, and myalgia but not with a cutaneous rash." — [PMID: 14766859](https://pubmed.ncbi.nlm.nih.gov/14766859/)

> "R. helvetica should be suspected in patients with unexplained fever, especially following a bite from an Ixodes sp. tick." — [PMID: 14766859](https://pubmed.ncbi.nlm.nih.gov/14766859/)

**HPO suggestions:** Fever (HP:0001945); Headache (HP:0002315); Myalgia (HP:0003326).

### 3. The refuted sarcoidosis hypothesis (F003)

An initial hypothesis (Nilsson et al.) proposed *R. helvetica* as an aetiological agent in **sarcoidosis**. This has not withstood independent scrutiny. Multiple Scandinavian/Danish studies using serology, real-time PCR, and fluorescence in situ hybridization (FISH) on sarcoidosis patient tissues and sera failed to detect *Rickettsia* and found no serological difference versus controls. In one archival study of sarcoidosis versus control mediastinal lymph node biopsies, no rickettsial DNA was found by PCR/FISH; a serosurvey found antibodies in 1/49 (2%) sarcoidosis patients versus 4/51 (8%) controls (not significant). A subsequent large meta-analysis likewise did not associate *R. helvetica* with sarcoidosis.

> "Our results do not support the hypothesis that Rickettsia is involved in the pathogenesis of sarcoidosis." — [PMID: 21284566](https://pubmed.ncbi.nlm.nih.gov/21284566/)

> "the current study does not support an association between rickettsia and sarcoidosis" — [PMID: 15516677](https://pubmed.ncbi.nlm.nih.gov/15516677/)

Supporting negative evidence: [PMID: 20298335](https://pubmed.ncbi.nlm.nih.gov/20298335/) (2% vs 8%, NS), [PMID: 19685374](https://pubmed.ncbi.nlm.nih.gov/19685374/) (prospective, negative), [PMID: 21299929](https://pubmed.ncbi.nlm.nih.gov/21299929/) (thesis, negative), [PMID: 27894280](https://pubmed.ncbi.nlm.nih.gov/27894280/) (meta-analysis: *R. helvetica* not associated).

### 4. Pathogenesis — cellular targets and intracellular mechanisms (F004)

In vitro studies establish the cellular mechanics of infection. *R. helvetica* survives and propagates in human THP-1 monocytes — an early target after tick inoculation — and induces TNF-α. In mouse NSC-34 neurons it forms **short polar actin tails** enabling intracellular movement and cell-to-cell spread, expresses **Sca4** (which, with vinculin, facilitates passage across the cell membrane), and can **invade and grow within the host-cell nucleus**. As with other SFG rickettsiae, the ultimate target is the vascular endothelium, producing the perivascular/vasculitic lesions observed in skin capillaries and cardiac tissue.

> "Our results show that R. helvetica survives and propagates in the THP-1 cells." — [PMID: 33276122](https://pubmed.ncbi.nlm.nih.gov/33276122/)

> "Short actin tails were shown at the polar end of the bacteria, which makes it likely that they can move intracellularly, and even spread between cells." — [PMID: 37085774](https://pubmed.ncbi.nlm.nih.gov/37085774/)

> "The bacteria were also shown to invade and grow in the cell nucleus of the neuron." — [PMID: 37085774](https://pubmed.ncbi.nlm.nih.gov/37085774/)

**Ontology suggestions:** GO:0006928 (movement of cell / actin-based motility); CL:0000576 (monocyte); CL:0000235 (macrophage); CL:0000115 (endothelial cell); CL:0000540 (neuron); UBERON:0001981 (blood vasculature); GO:0005634 (nucleus) as invaded compartment.

### 5. Epidemiology and vector ecology (F005)

*R. helvetica* is among the most common tick-borne organisms in European *I. ricinus*, with prevalences of **4.7–13% in Danish ticks** and ~7.7% in Serbian *I. ricinus*. It frequently co-occurs with *Borrelia burgdorferi* sensu lato because they share the *I. ricinus* vector: **25% of B. burgdorferi-positive ticks in the Netherlands were co-infected with rickettsiae**, predominantly *R. helvetica*. Small mammals — especially *Apodemus* mice — act as reservoirs; *R. helvetica* was the dominant species (90.9%) among rickettsia-positive German rodents/shrews. Human exposure is often asymptomatic seroconversion or mild self-limiting illness. SFG seroprevalence reached 32% among patients tested for neuroborreliosis and 31.1% among tick-exposed workers versus 13.3% controls (Poland).

> "With a prevalence of 4.7-13% in Danish Ixodes ricinus ticks, Rickettsia helvetica is one of the most frequently detected tick-borne organisms in Denmark." — [PMID: 29996782](https://pubmed.ncbi.nlm.nih.gov/29996782/)

> "of all the Borrelia burgdorferi s.l.-positive ticks, 25% were co-infected with rickettsiae" — [PMID: 26739030](https://pubmed.ncbi.nlm.nih.gov/26739030/)

> "Rickettsia helvetica (90.9%) was found as the dominantly occurring species in the four investigated federal states" — [PMID: 29398604](https://pubmed.ncbi.nlm.nih.gov/29398604/)

Risk factors (from [PMID: 27631765](https://pubmed.ncbi.nlm.nih.gov/27631765/)): occupational exposure to ticks (p = 0.002), frequency of tick bites (p = 0.02), and male gender (p = 0.005).

### 6. Treatment — doxycycline is first-line (F006)

As for all SFG rickettsioses, **doxycycline is the recommended first-line therapy** for *R. helvetica* infection, for patients of all ages, with early empirical treatment based on clinical suspicion being critical to prevent severe outcomes. In recent tick-bite-associated cases (Serbia, 2025), clinical signs resolved after doxycycline. No vaccine exists.

> "Doxycycline is the treatment of choice for patients of all ages; early treatment based on clinical diagnosis is critical to prevent severe outcomes." — [PMID: 34526545](https://pubmed.ncbi.nlm.nih.gov/34526545/)

> "Clinical signs resolved after doxycycline." — [PMID: 42520541](https://pubmed.ncbi.nlm.nih.gov/42520541/)

**NCIT suggestion:** Doxycycline (NCIT:C557).

### 7. Diagnostics — serology plus molecular detection (F007)

Diagnosis uses: (1) **IFA** with *R. helvetica* antigen, requiring a four-fold IgG titre rise for confirmation (cut-offs 1/64–1/128; endpoint titres up to 1/320 in a cardiac case); (2) **PCR/sequencing** of rickettsial genes — *16S rRNA* and the *17-kDa* outer-membrane protein gene (original 1999 cases), and *gltA*, *ompA*, *ompB*, *sca4* for genotyping — performed on skin lesion biopsy, capillary/lesion blood, whole blood, or CSF. Critically, lesion capillary blood outperformed whole blood (which was PCR-negative) in recent cases. Immunohistochemistry/electron microscopy of skin biopsies shows rickettsia-like organisms in the walls of skin capillaries and veins. Serology **cannot reliably distinguish species within SFG** owing to strong cross-reactivity.

> "All patients showed a four-fold increase in antibody titer to the spotted fever rickettsia, R. helvetica, and immunohistochemical examination revealed rickettsia-like organisms in the walls of skin capillaries and veins." — [PMID: 15723687](https://pubmed.ncbi.nlm.nih.gov/15723687/)

> "Rickettsia spp. DNA was detected in capillary blood from both lesions, and sequencing of the PCR amplicons identified R. helvetica, while whole blood was PCR-negative" — [PMID: 42520541](https://pubmed.ncbi.nlm.nih.gov/42520541/)

> "Owing to a known occurrence of immunological cross-reactivites, however, the results must be cautiously interpreted with regard to species of Rickettsia involved" — [PMID: 17852905](https://pubmed.ncbi.nlm.nih.gov/17852905/)

### 8. Local skin lesions, eschar, and lymphadenopathy — a broadened spectrum (F008)

Although classically "aneruptive," tick-bite-associated cases show **local dermatologic signs**: pruritic erythematous lesions, eschar, and non-specific bite-site lesions. An 8-year-old girl developed a pruritic scalp papule/crust with occipital/cervical lymphadenopathy after a *Haemaphysalis punctata* bite (R. helvetica confirmed by sequencing of lesion and whole-blood PCR), resembling a mild **TIBOLA/SENLAT-like** localized presentation. This implicates *H. punctata* as an alternative vector alongside *I. ricinus*.

> "An 8-year-old girl (Case 2) developed a pruritic scalp papule/crust and occipital/cervical lymphadenopathy after an adult female Haemaphysalis punctata attachment" — [PMID: 42520541](https://pubmed.ncbi.nlm.nih.gov/42520541/)

> "Eight patients developed local skin lesions at the site of the tick bite including non-specific lesions, itching sensation at the lesion site, and eschar." — [PMID: 36435213](https://pubmed.ncbi.nlm.nih.gov/36435213/)

**HPO suggestions:** Skin ulcer / eschar (HP:0200042); Lymphadenopathy (HP:0002716); Pruritus (HP:0000989).

### 9. Emerging pathogen status and prognosis (F009)

Review-level evidence places *R. helvetica* among the emerging European SFG rickettsioses transmitted by *I. ricinus* (alongside *R. monacensis*; *R. slovaca*/*raoultii* causing TIBOLA; *R. conorii* causing Mediterranean spotted fever). It is described as a human pathogen "in cases of fever with and without rash and in patients with meningitis and carditis." The great majority of infections are asymptomatic seroconversions or mild, self-limiting flu-like illness with full recovery on doxycycline; **severe outcomes (fatal chronic perimyocarditis/sudden cardiac death, meningitis, possible endocarditis) are rare**. No confirmed genetic host-susceptibility loci, chromosomal abnormalities, or inheritance patterns apply — the etiology is purely infectious/environmental.

> "Rickettsia helvetica has also been involved as a human pathogen in cases of fever with and without rash and in patients with meningitis and carditis." — [PMID: 23177355](https://pubmed.ncbi.nlm.nih.gov/23177355/)

> "Emerging pathogens, including bacteria of the order Rickettsiales (Anaplasma phagocytophilum, 'Candidatus Neoehrlichia mikurensis,' Rickettsia helvetica, and R. monacensis)" — [PMID: 25520947](https://pubmed.ncbi.nlm.nih.gov/25520947/)

---

## Section-by-Section Report

### 1. Disease Information

*Rickettsia helvetica* spotted fever is a tick-borne bacterial zoonosis caused by the obligate intracellular SFG rickettsia *R. helvetica*. It typically manifests as a mild, self-limiting, often rashless febrile illness, with rare severe cardiac and neurological complications.

**Key identifiers:**
- **MONDO:** MONDO:0000331 (spotted fever group parent term)
- **Organism NCBI Taxon:** 35789 (*Rickettsia helvetica*)
- **OMIM:** Not applicable (non-genetic infectious disease)
- **Orphanet:** No dedicated rare-disease entry specific to *R. helvetica*
- **ICD-10:** A77.8 (Other spotted fevers) / **ICD-11:** 1C30.Z (Spotted fever, unspecified)
- **MeSH:** *Rickettsia helvetica*; Spotted Fever Group; Rickettsia Infections

**Synonyms:** *R. helvetica* infection; *R. helvetica* rickettsiosis; aneruptive fever associated with *R. helvetica*. Historically the organism was designated the "Swiss agent."

**Information source:** Evidence is derived predominantly from **aggregated disease-level resources** — case series, serosurveys, tick surveillance studies, and in vitro experiments — rather than large EHR patient cohorts, reflecting the rarity of confirmed symptomatic human cases.

### 2. Etiology

**Causal factor:** Purely **infectious** — the obligate intracellular gram-negative bacterium *R. helvetica*. There is no genetic or heritable etiology.

**Risk factors (environmental/behavioral):** Tick exposure is the dominant risk. Occupational exposure to ticks (p = 0.002), frequency of tick bites (p = 0.02), and male gender (p = 0.005) were significant risk factors for SFG seropositivity ([PMID: 27631765](https://pubmed.ncbi.nlm.nih.gov/27631765/)). Warm-season outdoor activity in endemic European regions increases exposure. No genetic risk/susceptibility loci or protective alleles have been identified. **Gene–environment interactions are not applicable.**

### 3. Phenotypes

| Phenotype | Type | Frequency/Severity | HPO suggestion |
|---|---|---|---|
| Fever | Symptom | Common; warm season; mild | HP:0001945 |
| Headache | Symptom | Common | HP:0002315 |
| Myalgia | Symptom | Common | HP:0003326 |
| Absence of rash (aneruptive) | Distinguishing sign | Typical | — |
| Local skin lesion / eschar | Clinical sign | In tick-bite-associated cases | HP:0200042 |
| Regional lymphadenopathy | Clinical sign | TIBOLA/SENLAT-like cases | HP:0002716 |
| Meningitis (lymphocytic) | Severe manifestation | Rare | HP:0100785 |
| Perimyocarditis / sudden cardiac death | Severe manifestation | Rare, potentially fatal | HP:0001657 (pericarditis) |
| Facial palsy / sudden deafness (association) | Neurological | Uncommon, association | HP:0010628 / HP:0008527 |

**Onset:** Adult-onset most common (also pediatric, e.g., the 8-year-old case); **acute/subacute** onset. **Severity:** Predominantly mild; rarely severe. **Progression:** Usually self-limited; chronic perimyocarditis is the exception. **QoL impact:** Minimal in typical mild disease; severe/fatal only in rare cardiac cases.

### 4. Genetic/Molecular Information

**Not applicable to the human host.** *R. helvetica* spotted fever is an infectious disease with no causal human gene, no pathogenic germline/somatic variants, no modifier genes, no relevant human epigenetic changes, and no chromosomal abnormalities. Molecular characterization pertains to the **pathogen genome** — genes used for diagnosis/genotyping include *16S rRNA*, *17-kDa* protein gene, *gltA* (citrate synthase), *ompA*, *ompB*, and *sca4* ([PMID: 32723640](https://pubmed.ncbi.nlm.nih.gov/32723640/), [PMID: 21142961](https://pubmed.ncbi.nlm.nih.gov/21142961/)).

### 5. Environmental Information

**Environmental factors:** Exposure to questing *I. ricinus* (and, less commonly, *Haemaphysalis punctata*) ticks in European woodland, peri-urban, and urban green areas ([PMID: 25520947](https://pubmed.ncbi.nlm.nih.gov/25520947/), [PMID: 29664700](https://pubmed.ncbi.nlm.nih.gov/29664700/)). **Lifestyle factors:** Outdoor occupation/recreation during warm months. **Infectious agent:** *R. helvetica* (NCBITaxon:35789); reservoirs are small mammals, especially *Apodemus* mice ([PMID: 29398604](https://pubmed.ncbi.nlm.nih.gov/29398604/)). Co-infection with *Borrelia burgdorferi* s.l. is common ([PMID: 26739030](https://pubmed.ncbi.nlm.nih.gov/26739030/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating exposure → clinical manifestation):**

1. An infected *Ixodes ricinus* (or *Haemaphysalis punctata*) tick attaches and feeds, **inoculating** *R. helvetica* into the dermis. *(vector demonstrated; inoculation route inferred from SFG biology)*
2. Inoculated bacteria **infect and replicate within human monocytes/macrophages** at/near the bite site — an early cellular target — and **induce TNF-α**, initiating a proinflammatory response. *(demonstrated in vitro, THP-1 cells, [PMID: 33276122](https://pubmed.ncbi.nlm.nih.gov/33276122/))*
3. Intracellular bacteria **polymerize host actin into short polar tails**, driving intracellular movement and **cell-to-cell spread**; Sca4 with vinculin **enables passage across the cell membrane**. *(demonstrated in vitro, [PMID: 37085774](https://pubmed.ncbi.nlm.nih.gov/37085774/))*
4. Dissemination **leads to infection of the vascular endothelium** (the ultimate SFG target), **resulting in** perivascular inflammation and **vasculitis** in small vessels. *(inferred from SFG biology + IHC of skin capillary/vein walls, [PMID: 15723687](https://pubmed.ncbi.nlm.nih.gov/15723687/))*
5. Endothelial/vascular injury **produces** the clinical manifestations:
   - **Branch A (typical):** systemic cytokine response **results in** fever, headache, myalgia (aneruptive febrile illness).
   - **Branch B (cutaneous):** local vasculitis **results in** bite-site skin lesion, eschar, and regional lymphadenopathy.
   - **Branch C (cardiac, rare):** chronic vascular/myocardial involvement **leads to** perimyocarditis and, rarely, sudden cardiac death. *(inferred from post-mortem association, [PMID: 10513711](https://pubmed.ncbi.nlm.nih.gov/10513711/))*
   - **Branch D (neurological, rare):** neuronal/CNS invasion (including nuclear growth) **leads to** meningitis and neuritis. *(neuronal invasion demonstrated in vitro, [PMID: 37085774](https://pubmed.ncbi.nlm.nih.gov/37085774/); clinical association [PMID: 23790098](https://pubmed.ncbi.nlm.nih.gov/23790098/))*

```
 Tick bite ──▶ Monocyte/macrophage infection (+TNF-α)
                     │  actin tails, Sca4/vinculin
                     ▼
             Cell-to-cell spread ──▶ Endothelial infection ──▶ Vasculitis
                                                                │
        ┌───────────────┬───────────────┬────────────────┬─────┘
        ▼               ▼               ▼                ▼
   Fever/HA/myalgia  Eschar +         Perimyocarditis   Meningitis /
   (aneruptive)      lymphadenopathy  → sudden death    neuritis
   [typical]         [TIBOLA-like]    [rare, fatal]     [rare]
```

**Cell types (CL):** monocyte (CL:0000576), macrophage (CL:0000235), endothelial cell (CL:0000115), neuron (CL:0000540). **Biological processes (GO):** actin-based movement (GO:0006928), inflammatory response (GO:0006954), TNF production (GO:0032640). **Subcellular:** host-cell nucleus (GO:0005634) invaded.

### 7. Anatomical Structures Affected

- **Primary:** Vascular endothelium / small blood vessels (UBERON:0001981 blood vasculature). Skin (UBERON:0002097) at bite site.
- **Secondary:** Heart — pericardium/myocardium (UBERON:0002348 / UBERON:0001133) in perimyocarditis; meninges (UBERON:0002360) and CNS in neurological cases; lymph nodes (UBERON:0000029) in lymphadenopathy.
- **Body systems:** Cardiovascular, integumentary, nervous, lymphatic.
- **Tissue/cell level:** Vascular endothelial cells; monocytes/macrophages; neurons (experimental).
- **Lateralization:** Local lesions/lymphadenopathy correspond to bite site (may be unilateral/regional); systemic disease is not lateralized.

### 8. Temporal Development

- **Onset:** Acute/subacute, during the warm tick-activity season, days after a tick bite. Affects adults predominantly; pediatric cases occur.
- **Progression:** Most cases are **self-limited** and resolve (spontaneously or rapidly with doxycycline). Rare **chronic perimyocarditis** represents a progressive/fatal course.
- **Course pattern:** Typically monophasic and self-limiting; chronic in the rare cardiac form.
- **Critical period:** Early doxycycline (as for SFG rickettsioses generally) is the key window to prevent severe outcomes ([PMID: 34526545](https://pubmed.ncbi.nlm.nih.gov/34526545/)).

### 9. Inheritance and Population

- **Inheritance:** Not applicable (infectious disease; no heritable component).
- **Epidemiology:** Human symptomatic incidence is not well quantified (likely under-recognized). Tick infection prevalence: 4.7–13% (Denmark), ~7.7% (Serbia). SFG seroprevalence: up to 31–32% in exposed groups vs 13% controls. Reservoirs: *Apodemus* mice.
- **Geographic distribution:** Europe-wide (Scandinavia, Denmark, Netherlands, Germany, Serbia, Italy, Hungary, Poland, France), with detections in Asia (*I. persulcatus*, Japan). Distribution tracks *I. ricinus*.
- **Sex ratio:** Male predominance in seropositivity (occupational exposure-driven).
- **Age distribution:** Predominantly working-age adults; pediatric cases documented.

### 10. Diagnostics

- **Serology:** IFA with *R. helvetica* antigen; four-fold IgG rise confirmatory (cut-offs 1/64–1/128). Limited by SFG cross-reactivity — cannot reliably resolve species.
- **Molecular:** PCR + sequencing of *16S rRNA*, *17-kDa*, *gltA*, *ompA*, *ompB*, *sca4*. **Lesion capillary blood and CSF outperform whole blood.**
- **Histology/IHC/EM:** Rickettsia-like organisms in walls of skin capillaries and veins.
- **Differential diagnosis:** Lyme borreliosis (co-infection common), other SFG rickettsioses (*R. monacensis*, *R. slovaca*/TIBOLA, *R. conorii*/MSF), anaplasmosis, *Candidatus* Neoehrlichia mikurensis, tick-borne encephalitis, and — where fever + thrombocytopenia — SFTS-like illnesses.
- **Screening:** No asymptomatic-population screening; no newborn/carrier screening (non-genetic).

### 11. Outcome / Prognosis

- **Prognosis is generally excellent.** Most infections are asymptomatic seroconversions or mild, self-limiting flu-like illness with full recovery on doxycycline.
- **Mortality:** Very rare, confined to chronic perimyocarditis/sudden cardiac death; possible endocarditis role under investigation. (For SFG rickettsioses broadly, delayed doxycycline markedly worsens outcomes — RMSF data show mortality rising from ~4% to ~35% when treatment is delayed beyond day 5 [PMID: 34290155](https://pubmed.ncbi.nlm.nih.gov/34290155/); illustrative of the treatment-timing principle, not *R. helvetica*-specific mortality.)
- **Prognostic factors:** Timeliness of doxycycline; presence of cardiac/CNS involvement.

### 12. Treatment

- **First-line:** **Doxycycline** (NCIT:C557), for patients of all ages; early empirical treatment based on clinical suspicion. Clinical signs resolved after doxycycline in documented cases.
- **Pharmacogenomics / advanced therapeutics / surgery:** Not applicable.
- **Supportive care:** Antipyretics/analgesics as needed.
- **No vaccine** and no combination-therapy requirement for typical disease.

### 13. Prevention

- **Primary prevention:** Tick-bite avoidance (protective clothing, repellents), prompt tick removal, avoiding tick habitat during peak season; **no vaccine** exists.
- **Public health / environmental:** Vector awareness, tick surveillance, education for occupationally exposed groups.
- **Secondary/tertiary:** Early recognition and doxycycline to prevent progression; no population screening programs.
- **Genetic counseling:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy of hosts/vectors:** *Ixodes ricinus* (NCBITaxon:34613), *Ixodes persulcatus*, *Haemaphysalis punctata*; reservoir small mammals (*Apodemus* spp.).
- **Natural disease / veterinary relevance:** *R. helvetica* is widespread in ticks feeding on wildlife and companion animals; dogs serve as sentinels — 93.9% SFG-seropositive in a German study, with 66.0% attributable to *R. helvetica* ([PMID: 25889200](https://pubmed.ncbi.nlm.nih.gov/25889200/)). Overt natural disease in animals is not well characterized.
- **Zoonotic potential / cross-species susceptibility:** Zoonotic (tick-transmitted); "One Health" framing emphasized in recent case reports ([PMID: 42520541](https://pubmed.ncbi.nlm.nih.gov/42520541/)).

### 15. Model Organisms

- **In vitro / cellular models:** Human **THP-1 monocytes** (infection/propagation, TNF-α induction; [PMID: 33276122](https://pubmed.ncbi.nlm.nih.gov/33276122/)); mouse **NSC-34 motor-neuron-like cells** (actin tails, Sca4 expression, nuclear invasion; [PMID: 37085774](https://pubmed.ncbi.nlm.nih.gov/37085774/)).
- **Recapitulation:** These cellular models reproduce key mechanistic features (monocyte tropism, actin-based motility, neuronal/nuclear invasion) but not the whole-organism vascular/cardiac disease.
- **Limitations:** No established, widely used mammalian in vivo (mouse/rat) disease model specific to *R. helvetica* was identified; endothelial and cardiac pathogenesis remain to be modeled in vivo.

---

## Mechanistic Model / Interpretation

The coherent narrative that emerges is of a **low-virulence, endothelium-tropic SFG rickettsia** whose typical clinical footprint is deliberately understated: unlike its more aggressive relatives (*R. rickettsii*, *R. conorii*), *R. helvetica* usually causes an **aneruptive** febrile illness. The in vitro evidence explains both the mildness and the occasional severity. Early replication in monocytes/macrophages with TNF-α induction accounts for the systemic flu-like syndrome, while actin-based motility and Sca4-mediated membrane traversal provide the machinery for dissemination to endothelium — the shared final common pathway of SFG rickettsioses — yielding the vasculitis documented histologically in skin capillaries and, rarely, in cardiac tissue (perimyocarditis). Demonstrated neuronal invasion and intranuclear growth provide a plausible cellular basis for the rare meningitis/neuritis associations. The disease is therefore best conceptualized as a **spectrum** from asymptomatic seroconversion → mild aneruptive fever (most common) → localized TIBOLA/SENLAT-like eschar + lymphadenopathy → rare severe cardiac or neurological disease, all converging on endothelial infection and vasculitis, and all responsive to timely doxycycline.

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [29664700](https://pubmed.ncbi.nlm.nih.gov/29664700/) | Supports F001 | Taxonomy (SFG) + clinical triad |
| [10513711](https://pubmed.ncbi.nlm.nih.gov/10513711/) | Supports F001 | Vector (*I. ricinus*); perimyocarditis/sudden death |
| [14766859](https://pubmed.ncbi.nlm.nih.gov/14766859/) | Supports F002 | Aneruptive febrile presentation |
| [21284566](https://pubmed.ncbi.nlm.nih.gov/21284566/) | Refutes sarcoidosis link (F003) | Archival PCR/FISH negative |
| [15516677](https://pubmed.ncbi.nlm.nih.gov/15516677/) | Refutes sarcoidosis link (F003) | Serology negative |
| [27894280](https://pubmed.ncbi.nlm.nih.gov/27894280/) | Refutes sarcoidosis link (F003) | Meta-analysis: not associated |
| [33276122](https://pubmed.ncbi.nlm.nih.gov/33276122/) | Supports F004 | Monocyte infection/propagation |
| [37085774](https://pubmed.ncbi.nlm.nih.gov/37085774/) | Supports F004 | Actin tails, Sca4, nuclear invasion |
| [29996782](https://pubmed.ncbi.nlm.nih.gov/29996782/) | Supports F005 | Tick prevalence (Denmark) |
| [26739030](https://pubmed.ncbi.nlm.nih.gov/26739030/) | Supports F005 | Borrelia co-infection |
| [29398604](https://pubmed.ncbi.nlm.nih.gov/29398604/) | Supports F005 | Small-mammal reservoirs |
| [27631765](https://pubmed.ncbi.nlm.nih.gov/27631765/) | Supports F005 | Risk factors + seroprevalence |
| [34526545](https://pubmed.ncbi.nlm.nih.gov/34526545/) | Supports F006 | Doxycycline first-line |
| [42520541](https://pubmed.ncbi.nlm.nih.gov/42520541/) | Supports F006/F007/F008 | Doxycycline response; lesion-blood PCR; pediatric eschar case |
| [15723687](https://pubmed.ncbi.nlm.nih.gov/15723687/) | Supports F007 | Four-fold titre; IHC of vessel walls |
| [17852905](https://pubmed.ncbi.nlm.nih.gov/17852905/) | Supports F007 | SFG serological cross-reactivity |
| [36435213](https://pubmed.ncbi.nlm.nih.gov/36435213/) | Supports F008 | Local lesions/eschar |
| [23177355](https://pubmed.ncbi.nlm.nih.gov/23177355/) | Supports F009 | European review; clinical spectrum |
| [25520947](https://pubmed.ncbi.nlm.nih.gov/25520947/) | Supports F009 | Emerging Rickettsiales classification |

---

## Limitations and Knowledge Gaps

- **Sparse confirmed human cases.** Diagnosis is complicated by SFG serological cross-reactivity, so many "R. helvetica" attributions rest on serology that cannot resolve species; molecular confirmation is available only in a minority of cases.
- **Incidence unknown.** True symptomatic human incidence/prevalence is not quantified; most epidemiological data describe tick/animal prevalence and seroprevalence, not disease burden.
- **Causality of severe outcomes.** The perimyocarditis/sudden-death and meningitis/neuritis associations are based on case reports and serology; direct causal proof (isolation from affected tissue in life) is limited.
- **No in vivo disease model.** Mechanistic insight derives from cell-culture systems; endothelial/cardiac pathogenesis lacks a validated animal model.
- **Treatment evidence extrapolated.** Doxycycline efficacy is inferred from SFG-wide guidance and small case reports, not *R. helvetica*-specific trials.

---

## Proposed Follow-up Experiments / Actions

1. **Standardized molecular case definition.** Promote species-specific PCR (*gltA*/*ompA*/*ompB*/*sca4*) on lesion capillary blood, CSF, and biopsy over serology alone to build a reliable confirmed-case registry.
2. **Prospective clinical cohort.** Enroll febrile tick-bitten patients in endemic European regions with paired sera + molecular testing to estimate symptomatic incidence and the true frequency of cardiac/neurological complications.
3. **In vivo model development.** Establish an immunocompetent/immunodeficient mouse model to test endothelial tropism and cardiac pathology, closing the gap between cell-culture mechanisms and organ-level disease.
4. **Endothelial and cardiac mechanism studies.** Extend the THP-1/NSC-34 work to primary human endothelial and cardiac cells to directly test the vasculitis/perimyocarditis pathway.
5. **Co-infection interaction studies.** Given frequent *Borrelia* co-infection, evaluate whether co-infection alters clinical severity or diagnostic performance.
6. **Definitively close the sarcoidosis question** in the literature/knowledge base as *refuted*, citing the concordant negative serology/PCR/FISH studies and meta-analysis.

---

*Evidence source types: human clinical (case series, serosurveys, registries), in vitro/cellular (THP-1, NSC-34), tick/animal surveillance, and review/meta-analysis. This report synthesizes 9 confirmed findings across 41 reviewed papers over 5 investigation iterations.*


## Artifacts

- [OpenScientist final report](Rickettsia_Helvetica_Spotted_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Rickettsia_Helvetica_Spotted_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000331` (3 mentions) - the report calls it "spotted fever group rickettsiosis parent", "spotted fever", "spotted fever group parent term"; MONDO calls it **Rickettsia helvetica spotted fever**
- `HP:0001945` (2 mentions) - the report calls it "Common; warm season; mild"; HP calls it **Fever**
- `HP:0002315` (2 mentions) - the report calls it "Common"; HP calls it **Headache**
- `HP:0003326` (2 mentions) - the report calls it "Common"; HP calls it **Myalgia**
- `GO:0006928` (2 mentions) - the report calls it "movement of cell / actin-based motility"; GO calls it **obsolete movement of cell or subcellular component**
- `NCIT:C557` (2 mentions) - the report calls it "Doxycycline", "First-line:** **Doxycycline"; NCIT calls it **Hydroxychloroquine**
- `HP:0002716` (2 mentions) - the report calls it "TIBOLA/SENLAT-like cases"; HP calls it **Lymphadenopathy**
- `HP:0100785` (1 mention) - the report calls it "Rare"; HP calls it **Insomnia**
- `HP:0001657` (1 mention) - the report calls it "pericarditis"; HP calls it **Prolonged QT interval**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006928` (obsolete movement of cell or subcellular component) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:35789` (2 mentions) - the report calls it "Rickettsia helvetica", "R. helvetica"; NCBITaxon calls it **Rickettsia helvetica**
- `NCBITaxon:34613` (2 mentions) - the report calls it "Ixodes ricinus", "Taxonomy of hosts/vectors:** *Ixodes ricinus"; NCBITaxon calls it **Ixodes ricinus**
- `UBERON:0001981` (2 mentions) - the report calls it "blood vasculature"; UBERON calls it **blood vessel**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0000331` - called "spotted fever group rickettsiosis parent", "spotted fever", "spotted fever group parent term"
- `NCBITaxon:35789` - called "Rickettsia helvetica", "R. helvetica"
- `NCBITaxon:34613` - called "Ixodes ricinus", "Taxonomy of hosts/vectors:** *Ixodes ricinus"
- `NCIT:C557` - called "Doxycycline", "First-line:** **Doxycycline"