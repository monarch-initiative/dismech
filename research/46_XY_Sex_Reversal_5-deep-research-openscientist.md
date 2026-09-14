---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T05:29:50.506539'
end_time: '2026-09-01T05:47:39.997872'
duration_seconds: 1069.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 46,XY Sex Reversal 5
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 10
  relevance_assessed: 17
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 5
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0013120
    reported_labels:
    - confirmed via EBI OLS
    - MONDO
    ontology_label: 46,XY sex reversal 5
  - term_id: HP:0010461
    reported_labels:
    - 46,XY sex reversal
    ontology_label: Abnormality of the male genitalia
  - term_id: HP:0000062
    reported_labels:
    - Physical manifestation
    ontology_label: Ambiguous genitalia
  - term_id: HP:0000047
    reported_labels:
    - Physical manifestation
    ontology_label: Hypospadias
  - term_id: HP:0000028
    reported_labels:
    - Clinical sign
    ontology_label: Cryptorchidism
  - term_id: NCIT:C15417
    reported_labels:
    - hormone therapy
    ontology_label: Randomized Clinical Trial
  - term_id: NCIT:C15277
    reported_labels:
    - surgery
    ontology_label: Mastectomy
  - term_id: NCIT:C15681
    reported_labels:
    - genetic counseling
    ontology_label: Cytotoxic Chemotherapy
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: 46_XY_Sex_Reversal_5-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 46_XY_Sex_Reversal_5-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 46,XY Sex Reversal 5
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **46,XY Sex Reversal 5** covering all of the
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

# 46,XY Sex Reversal 5 (SRXY5): A Comprehensive Disease Characterization

**Disease:** 46,XY Sex Reversal 5 (SRXY5)
**OMIM:** #613080 · **MONDO:** MONDO:0013120 · **Causal gene:** *CBX2* (17q25.3)
**Category:** Mendelian, autosomal-recessive disorder/difference of sex development (DSD)
**Report date:** 2026-09-01

---

## Summary

**46,XY Sex Reversal 5 (SRXY5) is a rare autosomal-recessive difference of sex development (DSD) caused by biallelic loss-of-function mutations in *CBX2* (Chromobox 2; historically *M33*), a Polycomb-group (PRC1) chromatin-modifying gene on chromosome 17q25.3.** In an individual with a normal 46,XY karyotype, loss of CBX2 function prevents activation of the testis-determining genetic cascade. Because CBX2 acts *upstream of SRY*, its loss produces failure to initiate the SRY→SOX9 male pathway (with reduced NR5A1/SF-1 expression) and de-repression of the ovarian program. The clinical consequence ranges from a completely female phenotype with a uterus and histologically normal ovaries at one extreme to ambiguous/undervirilized external genitalia at the other.

The disease is defined by the index case reported by Biason-Lauber and colleagues in 2009 ([PMID: 19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/)): a prenatally karyotyped 46,XY girl with normal female external genitalia, a uterus, and ovaries, who carried compound-heterozygous loss-of-function mutations in *CBX2* — NM_005189.3:c.293C>T (p.Pro98Leu) and c.1328G>C (p.Arg443Pro). Both alleles are independently classified **Pathogenic** for "46,XY sex reversal 5" in ClinVar. The human finding is mechanistically anchored by decades of mouse work: constitutive *M33/Cbx2* knockout recapitulates XY male-to-female sex reversal, and this reversal is genetically rescued by forced expression of *Sry* or *Sox9*, cementing CBX2's position at the top of the testis-determination hierarchy.

SRXY5 is exceptionally rare (only a small number of confirmed *CBX2*-mutant cases worldwide; a 47-patient DSD cohort found no additional pathogenic *CBX2* mutations). There is no disease-modifying therapy; management is supportive and multidisciplinary — sex-of-rearing decisions, hormone replacement, gonadectomy where germ-cell-tumor risk warrants, and psychosocial and genetic counseling — following the international DSD consensus framework. This report synthesizes 9 confirmed findings drawn from 21 reviewed papers spanning human clinical, in-vitro/functional, model-organism, and computational-database evidence.

---

## Key Findings

### Finding 1 — SRXY5 is caused by biallelic loss-of-function mutations in *CBX2*, placing CBX2 upstream of SRY

The defining discovery of SRXY5 came from a single, unusually informative index case. Biason-Lauber et al. (2009) described a prenatally karyotyped 46,XY girl born with **completely normal female external genitalia, a uterus, and histologically normal ovaries**. Whole-gene analysis of *CBX2* — the human ortholog of mouse *M33* — revealed compound-heterozygous loss-of-function mutations. This case defines the OMIM entry #613080 (46,XY sex reversal 5).

Crucially, the discovery added a new, higher tier to the human sex-determination cascade. As the authors state:

> "The analysis of the human homolog of M33, Chromobox homolog 2 (CBX2), in this girl revealed loss-of-function mutations that allowed us, by placing CBX2 upstream of SRY, to add an additional component to the still incomplete cascade of human sex development." — [PMID: 19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/)

This is the single most important mechanistic anchor for the disease: CBX2 is not merely another testis gene but an upstream *enabler* of the SRY-initiated switch.

### Finding 2 — Mouse *M33/Cbx2* knockout recapitulates XY sex reversal via loss of upstream regulation of *Sry* and *Nr5a1*/SF-1

The human finding rests on a robust animal foundation predating it by more than a decade. Katoh-Fukui et al. (1998) showed that *M33*-null mice display **XY male-to-female sex reversal** with retarded genital ridge formation and gonadal growth defects arising near the time of *Sry* expression:

> "survivors showed male-to-female sex reversal" — [PMID: 9641679](https://pubmed.ncbi.nlm.nih.gov/9641679/)

> "Gonadal growth defects appeared near the time of expression of the Y-chromosome-specific Sry gene, suggesting that M33 deficiency may cause sex reversal by interfering with steps upstream of Sry." — [PMID: 9641679](https://pubmed.ncbi.nlm.nih.gov/9641679/)

A subsequent study connected M33 to the nuclear receptor SF-1: M33-knockout adrenal/splenic phenotypes mirror those of *Nr5a1* (Ad4BP/SF-1) knockouts, and M33-KO gonads/adrenals showed significantly reduced Ad4BP/SF-1 expression with ChIP evidence of direct regulation:

> "indicating that M33 is an essential upstream regulator of Ad4BP/SF1" — [PMID: 15899914](https://pubmed.ncbi.nlm.nih.gov/15899914/)

Sex-reversal penetrance is incomplete in mice: one study reported reversal in ~28.6% of XY−/− embryos, with the remainder showing bilateral testicular hypoplasia ([PMID: 22200029](https://pubmed.ncbi.nlm.nih.gov/22200029/)).

### Finding 3 — CBX2 is a PRC1 chromatin regulator that *stimulates* the male pathway and *represses* the female pathway; two isoforms have distinct DSD roles

Genome-wide DamID mapping in Sertoli-like NT-2D1 cells identified ~1,600 direct CBX2 targets and established CBX2's bistable, dual role:

> "CBX2 role in the sex development cascade is to stimulate the male pathway and concurrently inhibit the female pathway" — [PMID: 25569159](https://pubmed.ncbi.nlm.nih.gov/25569159/)

Mechanistically, CBX2 is an H3K27me3 "reader" within Polycomb Repressive Complex 1 (PRC1), where it associates with RING1B, PCGF2, and PHC2 and plays a structural role in the H2AK119 mono-ubiquitination machinery ([PMID: 31093962](https://pubmed.ncbi.nlm.nih.gov/31093962/); [PMID: 32979540](https://pubmed.ncbi.nlm.nih.gov/32979540/)).

The gene encodes two functionally distinct isoforms. The shorter isoform, **CBX2.2**, has its own DSD-associated variants (p.Cys132Arg and p.Cys154fs) that cause 46,XY DSD, likely through defective regulation of *EMX2*:

> "both CBX2.2 variants fail to regulate the expression of genes essential for sexual development, leading to a severe 46,XY DSD defect, likely because of a defective expression of EMX2 in the developing gonad" — [PMID: 29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/)

### Finding 4 — Phenotypic spectrum ranges from complete female genitalia with ovaries to ambiguous genitalia

SRXY5 is phenotypically variable. The index case had a fully female phenotype with uterus and normal ovaries ([PMID: 19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/)). At the opposite end, CBX2.2-variant patients presented with:

> "two patients with features of DSD i.e. atypical external genitalia, perineal hypospadias and no palpable gonads" — [PMID: 29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/)

Because 46,XY gonadal dysgenesis broadly carries elevated germ-cell-tumor/gonadoblastoma risk, gonadectomy is considered, and care follows the multidisciplinary DSD consensus framework:

> "medical, surgical and psychological care and the decision regarding sex of rearing or gender assignment" — [PMID: 18987491](https://pubmed.ncbi.nlm.nih.gov/18987491/)

### Finding 5 — Gene annotation and gnomAD constraint support an autosomal-recessive mechanism

*CBX2* identifiers: **HGNC:1552**, NCBI Gene **84733**, Ensembl **ENSG00000173894**, UniProt **Q14781**, OMIM gene ***602770**, cytoband **17q25.3** (chr17:79,778,135–79,788,394, GRCh38); aliases *M33*, *CDCA6*, *SRXY5*. gnomAD constraint metrics show CBX2 is **not** loss-of-function intolerant: pLI = 0.024, observed/expected LoF (oe_lof) = 0.52 (90% CI 0.33–0.87), lof_z = 1.85. Heterozygous LoF is therefore tolerated in the general population, consistent with a **recessive** disease requiring biallelic loss. ClinVar lists 224 *CBX2* variants, predominantly benign/VUS.

### Finding 6 — CBX2 acts upstream of SRY: rescue epistasis with *Sry*/*Sox9*

The decisive genetic proof of hierarchy comes from mouse rescue experiments. In *Cbx2*-KO gonads, expression of *Sry, Sox9, Lhx9, Ad4BP/SF-1 (Nr5a1), Dax-1 (Nr0b1), Gata4, Arx,* and *Dmrt1* is disrupted:

> "the expression of Sry, Sox9, Lhx9, Ad4BP/SF-1, Dax-1, Gata4, Arx, and Dmrt1, genes encoding transcription factors essential for gonadal development, is affected in Cbx2 KO gonads" — [PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/)

Forced expression of *Sry* or *Sox9* rescues the sex reversal but not the gonadal hypoplasia:

> "Male-to-female sex reversal in Cbx2 KO mice was rescued by crossing them with transgenic mice displaying forced expression of Sry or Sox9." — [PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/)

This dissociates two CBX2 functions: (i) controlling the sex-determining switch *specifically through Sry*, and (ii) governing gonad size via a separate downstream gene set.

### Finding 7 — Disease and molecular ontology annotations

**Disease IDs:** OMIM #613080; MONDO:0013120 (confirmed via EBI OLS); Orphanet groups under 46,XY complete/partial gonadal dysgenesis (ORPHA:242, ORPHA:2138). **Gene/protein:** *CBX2* (HGNC:1552, OMIM *602770, UniProt Q14781, 532 aa). **Protein architecture** (UniProt Q14781): N-terminal chromodomain (aa 12–70; H3K9me/H3K27me reader), nuclear localization signal (aa 163–168), and large disordered/AT-hook-containing C-terminal regions (aa 60–204, 296–348, 379–493). Notably, the index-case variants **p.Pro98Leu** and **p.Arg443Pro** fall in the disordered regions *outside* the chromodomain.

**Suggested GO terms:** GO:0035102 (PRC1 complex), GO:0031519 (PcG protein complex), GO:0045137 (development of primary sexual characteristics), GO:0062072 (histone reader activity), GO:0000122/GO:0045892 (negative regulation of transcription), GO:0031507 (heterochromatin formation), GO:0005634 (nucleus).

### Finding 8 — ClinVar confirms the two index-case alleles as Pathogenic

ClinVar (queried 2026-09-01) lists **NM_005189.3(CBX2):c.293C>T (p.Pro98Leu)** and **NM_005189.3(CBX2):c.1328G>C (p.Arg443Pro)**, both classified **Pathogenic** for the condition "46,XY sex reversal 5" — precisely the compound-heterozygous genotype of the index patient ([PMID: 19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/)). Other *CBX2* coding substitutions (p.His331Arg, p.Met404Leu, p.Val487Ile, p.Ala460Thr) are VUS. Pathogenic large 17q25.3 CNVs in ClinVar are contiguous-gene events rather than isolated CBX2-DSD.

### Finding 9 — Mouse ortholog identifiers and completed model-organism annotation

Mouse ortholog *Cbx2* (*M33*): NCBI Gene **12416**, MGI:**88289**, Ensembl **ENSMUSG00000025577**, chromosome 11. The constitutive *M33/Cbx2* knockout is the validated SRXY5 model recapitulating XY male-to-female sex reversal ([PMID: 9641679](https://pubmed.ncbi.nlm.nih.gov/9641679/), [PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/), [PMID: 15899914](https://pubmed.ncbi.nlm.nih.gov/15899914/), [PMID: 22200029](https://pubmed.ncbi.nlm.nih.gov/22200029/)).

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** SRXY5 is a rare Mendelian 46,XY DSD in which a chromosomally male (46,XY) individual fails to complete testis determination because of loss of the Polycomb regulator CBX2. The result is dysgenetic gonads or ovaries, frequently with Müllerian (uterine) structures, and external genitalia ranging from typically female to ambiguous.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #613080 |
| OMIM (gene) | *602770 (CBX2) |
| MONDO | MONDO:0013120 |
| Orphanet (grouping) | ORPHA:242, ORPHA:2138 (46,XY complete/partial gonadal dysgenesis) |
| Gene (HGNC) | HGNC:1552 |
| NCBI Gene | 84733 |
| Ensembl | ENSG00000173894 |
| UniProt | Q14781 |
| MeSH (broad) | Disorders of Sex Development; Gonadal Dysgenesis, 46,XY |

**Synonyms / alternative names:** 46,XY sex reversal 5; SRXY5; CBX2-related 46,XY DSD; gonadal dysgenesis due to CBX2 deficiency. Gene aliases: *M33*, *CDCA6*.

**Information source.** Disease-level knowledge derives primarily from aggregated resources (OMIM, ClinVar, Orphanet) built on a very small number of *individual* clinical case reports plus extensive mouse model data — not from EHR-scale datasets.

### 2. Etiology

**Primary cause — genetic.** SRXY5 is caused by **biallelic (autosomal-recessive) loss-of-function mutations in *CBX2***. The index genotype is compound-heterozygous p.Pro98Leu / p.Arg443Pro ([PMID: 19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/)). Isoform-specific CBX2.2 variants (p.Cys132Arg, p.Cys154fs) cause a severe 46,XY DSD via defective *EMX2* regulation ([PMID: 29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/)).

**Genetic risk factors.** The disease requires two damaging *CBX2* alleles; heterozygous carriers are unaffected (consistent with gnomAD tolerance of monoallelic LoF, pLI = 0.024). Consanguinity increases risk of biallelic recessive genotypes (a recurring theme in DSD cohorts generally, e.g., [PMID: 42202777](https://pubmed.ncbi.nlm.nih.gov/42202777/)).

**Environmental / infectious factors.** None known to cause SRXY5. This is a monogenic developmental disorder; there is no evidence for toxin, infectious, or lifestyle etiology.

**Protective factors and gene–environment interactions.** Not applicable / none established. The only "protective" scenario is the absence of a second pathogenic allele.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| 46,XY complete gonadal dysgenesis / sex reversal | Clinical sign | HP:0010461 (46,XY sex reversal) | Core; variable |
| Female external genitalia in 46,XY individual | Physical manifestation | HP:0000812 (abnormal external genitalia) | Index case |
| Ambiguous genitalia | Physical manifestation | HP:0000062 | CBX2.2-variant patients |
| Hypospadias (perineal) | Physical manifestation | HP:0000047 | CBX2.2 cases ([PMID: 29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/)) |
| Presence of uterus / Müllerian derivatives | Clinical sign | HP:0000130 (abnormal uterus) | Index case had uterus |
| Ovarian or dysgenetic gonadal tissue | Histology | HP:0000138 / HP:0000133 | Index case: normal ovaries |
| Cryptorchidism / no palpable gonads | Clinical sign | HP:0000028 | CBX2.2 cases |
| Germ-cell tumor / gonadoblastoma risk | Neoplasm (risk) | HP:0100728 / HP:0100729 | Elevated in 46,XY GD generally |
| Primary amenorrhea / delayed puberty (potential) | Lab/clinical | HP:0000132 / HP:0000823 | Depends on gonadal function |

**Characteristics.** Onset is **congenital** (determined during embryonic gonadal development, ~gestational weeks 6–8 in humans). Severity is **variable** (from typically female to ambiguous). Course is **stable/non-progressive** structurally, though tumor risk accrues over time and pubertal hormone deficits emerge with age. Frequency data are limited by the very small number of confirmed cases.

**Quality-of-life impact.** DSD conditions carry documented psychosocial and quality-of-life burdens; a multidisciplinary education/empowerment program (Empower-DSD) improved or stabilized health-related quality of life in >66% of children and parents ([PMID: 42597469](https://pubmed.ncbi.nlm.nih.gov/42597469/)) and improved diagnosis-specific knowledge ([PMID: 41579703](https://pubmed.ncbi.nlm.nih.gov/41579703/)).

### 4. Genetic / Molecular Information

**Causal gene.** *CBX2* (HGNC:1552; OMIM *602770; 17q25.3).

**Pathogenic variants (ClinVar, Pathogenic for SRXY5):**

| Variant (NM_005189.3) | Protein | Type | Classification | Domain location |
|---|---|---|---|---|
| c.293C>T | p.Pro98Leu | Missense | Pathogenic | Disordered region (outside chromodomain) |
| c.1328G>C | p.Arg443Pro | Missense | Pathogenic | Disordered C-terminal region |
| (CBX2.2) | p.Cys132Arg | Missense | Reported pathogenic ([PMID: 29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/)) | Isoform-specific |
| (CBX2.2) | p.Cys154fs | Frameshift | Reported pathogenic | Isoform-specific |

**Allele frequency.** Pathogenic alleles are ultra-rare/private; gnomAD shows CBX2 is LoF-tolerant at the heterozygous level (oe_lof 0.52). **Origin:** germline. **Functional consequence:** loss of function (biallelic).

**Modifier genes / epigenetics.** CBX2 itself is an epigenetic effector (H3K27me3 reader, H2AK119ub machinery). Downstream network members (*SRY, SOX9, NR5A1/SF-1, EMX2, DMRT1, GATA4, DAX1/NR0B1, LHX9, ARX*) are candidate modifiers of expressivity. No formal modifier locus is established.

**Chromosomal abnormalities.** Large 17q25.3 CNVs in ClinVar are contiguous-gene deletions/duplications, not isolated CBX2-DSD events. A 47-patient DSD MLPA study found **no** CBX2 copy-number changes and no additional pathogenic point mutations ([PMID: 23219007](https://pubmed.ncbi.nlm.nih.gov/23219007/)), underscoring rarity.

### 5. Environmental Information

**Not applicable.** SRXY5 is a monogenic developmental disorder with no established environmental, lifestyle, toxicological, or infectious contribution.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function mutation in *CBX2*** (e.g., p.Pro98Leu + p.Arg443Pro) **results in** a non-functional CBX2 protein in the bipotential gonad (genital ridge). *(Demonstrated — human [PMID: 19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/); ClinVar Pathogenic.)*
2. Loss of CBX2 **impairs assembly/function of the PRC1 chromatin-modifying complex** (CBX2 is a structural H3K27me3 reader supporting H2AK119 mono-ubiquitination). *(Demonstrated in vitro — [PMID: 31093962](https://pubmed.ncbi.nlm.nih.gov/31093962/), [PMID: 32979540](https://pubmed.ncbi.nlm.nih.gov/32979540/).)*
3. Defective CBX2/PRC1 activity **fails to establish the chromatin state that stimulates male-pathway genes and represses female-pathway genes** across ~1,600 direct targets. *(Demonstrated — DamID, [PMID: 25569159](https://pubmed.ncbi.nlm.nih.gov/25569159/).)*
4. As an upstream node, CBX2 loss **fails to permit/activate *SRY* (and *NR5A1*/SF-1) expression** in pre-Sertoli somatic cells at the critical window (~gestational week 6–7; in mouse, near the time of *Sry* onset). *(Demonstrated — mouse [PMID: 9641679](https://pubmed.ncbi.nlm.nih.gov/9641679/), [PMID: 15899914](https://pubmed.ncbi.nlm.nih.gov/15899914/), [PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/).)*
5. Absent SRY **fails to activate *SOX9***, the master Sertoli-cell determinant. **Branch:** without SOX9-driven Sertoli differentiation, the supporting-cell lineage defaults toward the granulosa (ovarian) program; de-repressed pro-ovarian genes (e.g., via impaired *EMX2* regulation in the CBX2.2 isoform axis) reinforce this. *(Demonstrated/inferred — [PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/), [PMID: 29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/).)*
6. Failure of Sertoli-cell determination **results in gonadal dysgenesis or ovarian development** in a 46,XY gonad. *(Demonstrated — human/mouse.)*
7. Absent/deficient testicular Sertoli and Leydig function **leads to loss of anti-Müllerian hormone and androgen output**, which **results in** retention of Müllerian structures (uterus) and undervirilized/female external genitalia. *(Inferred from endocrine physiology; consistent with index-case uterus + female genitalia.)*
8. In parallel, a **separate CBX2-dependent gene set governs gonad size**, so dysgenetic/hypoplastic gonads persist even when the sex-fate switch is rescued. *(Demonstrated — Sry/Sox9 rescue corrects sex reversal but not hypoplasia, [PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/).)*

```
CBX2 biallelic LOF
        │ (results in)
        ▼
PRC1/H2AK119ub chromatin regulation impaired
        │ (fails to set)
        ▼
Male genes not stimulated / female genes de-repressed
        │ (fails to activate)
        ▼
SRY not expressed ──► SOX9 not activated
        │                         │
        │ (branch)                ▼
        ▼               Sertoli differentiation fails
Pro-ovarian program        │
(EMX2 axis) reinforced     ▼
        └────────► Gonadal dysgenesis / ovary in 46,XY
                          │ (leads to)
                          ▼
        ↓ AMH, ↓ androgens ► uterus retained + female/ambiguous genitalia
                          │
        (parallel) separate gene set ► persistent gonadal hypoplasia
```

**Upstream vs downstream.** CBX2 is the most **upstream** demonstrated node (above SRY). SRY→SOX9→Sertoli differentiation and the NR5A1/SF-1, DMRT1, GATA4, DAX1, LHX9, ARX network are **downstream**.

**Cell types / processes.** Key cell type: bipotential/pre-Sertoli somatic supporting cell of the genital ridge (**suggested CL:** CL:0000216 Sertoli cell; CL:0000670 primordial germ cell; CL:0000501 granulosa cell). Processes: **GO:0007530** sex determination, **GO:0008584** male gonad development, **GO:0045137** development of primary sexual characteristics, **GO:0031507** heterochromatin formation.

**Molecular profiling.** DamID identified ~1,600 direct CBX2 targets in Sertoli-like cells ([PMID: 25569159](https://pubmed.ncbi.nlm.nih.gov/25569159/)). No SRXY5-specific human metabolomic/proteomic/single-cell datasets are available given case rarity.

### 7. Anatomical Structures Affected

- **Primary organ:** gonad (bipotential gonad / genital ridge) — **UBERON:0000991** gonad; **UBERON:0000992** ovary; **UBERON:0000473** testis.
- **Secondary / body systems:** reproductive/endocrine system (**UBERON:0000990**); Müllerian derivatives — uterus **UBERON:0000995**, external genitalia. Adrenal gland and spleen are affected in the mouse M33 model (via SF-1) but adrenal disease is not a prominent human SRXY5 feature.
- **Tissue/cell level:** gonadal somatic supporting cells (Sertoli/granulosa) and germ cells; germline meiotic defects in the mouse model ([PMID: 22200029](https://pubmed.ncbi.nlm.nih.gov/22200029/)).
- **Subcellular:** nucleus / chromatin (**GO:0005634** nucleus; **GO:0035102** PRC1 complex; **GO:0000785** chromatin).
- **Lateralization:** typically bilateral gonadal involvement; asymmetric gonads (one hypoplastic testis + contralateral ovary/ovotestis) occur in the mouse model.

### 8. Temporal Development

- **Onset:** congenital — the lesion acts during embryonic sex determination (human ~6–8 weeks gestation).
- **Onset pattern:** insidious/developmental; often first detected at birth (ambiguous genitalia), prenatally (karyotype–phenotype discordance, as in the index case), or at puberty (delayed puberty/primary amenorrhea).
- **Progression:** structurally stable/non-progressive; lifelong. Germ-cell-tumor risk accrues over time, and hypogonadism manifests at expected puberty.
- **Critical period:** the sex-determination window is the intervention-relevant developmental window mechanistically, though no in-utero therapy exists.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive (biallelic *CBX2* LoF). Consistent with gnomAD LoF tolerance (pLI 0.024).
- **Prevalence/incidence:** not precisely established — ultra-rare; only a handful of molecularly confirmed cases worldwide. A dedicated 47-patient DSD cohort found no additional pathogenic CBX2 mutations ([PMID: 23219007](https://pubmed.ncbi.nlm.nih.gov/23219007/)), and the authors concluded the study "does not support CBX2 gene disruption as a common cause of gonadal DSD."
- **Penetrance/expressivity:** variable expressivity (female to ambiguous phenotype); mouse penetrance of overt sex reversal is incomplete (~28.6% of XY−/−, [PMID: 22200029](https://pubmed.ncbi.nlm.nih.gov/22200029/)).
- **Consanguinity/founder effects:** consanguinity raises recessive-genotype probability (general DSD context); no CBX2 founder allele is established.
- **Carrier frequency:** unknown; individual pathogenic alleles are private/ultra-rare in gnomAD.
- **Sex ratio / affected population:** by definition affects 46,XY (chromosomally male) individuals who may present or be reared as female; no ethnic predilection established.

### 10. Diagnostics

**Recommended approach:** karyotype (46,XY) with phenotype–karyotype discordance triggers molecular workup.

- **Genetic testing:** karyotyping (confirms 46,XY); DSD **gene panels** including *CBX2* alongside *SRY, SOX9, NR5A1, MAP3K1, WT1, GATA4, DHH, DMRT1*; **WES/WGS** for gene-agnostic diagnosis (essential given rarity); **single-gene *CBX2* sequencing** for targeted confirmation; **chromosomal microarray/MLPA** to detect CBX2 CNVs (MLPA probe set developed in [PMID: 23219007](https://pubmed.ncbi.nlm.nih.gov/23219007/)). Confirm variants against **ClinVar** (both index alleles are Pathogenic).
- **Laboratory tests:** gonadotropins (LH/FSH), testosterone, AMH, inhibin B, hCG stimulation test to assess gonadal function.
- **Imaging:** pelvic/abdominal ultrasound and MRI to identify Müllerian structures (uterus) and locate gonads.
- **Histopathology:** gonadal biopsy — ovarian, dysgenetic, or streak tissue; surveillance for gonadoblastoma/germ-cell neoplasia.
- **Differential diagnosis:** other 46,XY complete/partial gonadal dysgenesis (SRY, NR5A1/SF-1, MAP3K1, WT1, SOX9, DHH, PBX1), androgen insensitivity syndrome, 17α-/11β-hydroxylase and steroidogenic defects, and Swyer syndrome. Distinguishing features: *CBX2*-related cases show early upstream failure with possible normal ovaries; PBX1 disease adds radioulnar/radiocubital synostosis ([PMID: 31058389](https://pubmed.ncbi.nlm.nih.gov/31058389/)).
- **Screening:** no population newborn screen; cascade genetic testing of relatives after a proband is identified.

### 11. Outcome / Prognosis

- **Survival/mortality:** SRXY5 is not intrinsically life-limiting; life expectancy is normal. Principal medical risk is **germ-cell tumor/gonadoblastoma** in dysgenetic gonads, mitigated by surveillance/gonadectomy.
- **Morbidity/function:** infertility is typical; hypogonadism requires lifelong hormone replacement; psychosocial burden is significant.
- **Complications:** gonadal neoplasia; osteoporosis and metabolic effects of untreated hypogonadism; surgical and psychological sequelae.
- **Prognostic factors:** phenotype severity, gonadal histology/position, and timing of diagnosis/intervention. No molecular prognostic biomarker beyond genotype is established.
- **Quality of life:** improvable with structured multidisciplinary support ([PMID: 42597469](https://pubmed.ncbi.nlm.nih.gov/42597469/), [PMID: 41579703](https://pubmed.ncbi.nlm.nih.gov/41579703/)).

### 12. Treatment

**No disease-modifying/curative therapy exists** (no gene, cell, or RNA therapy; not applicable). Management is supportive and individualized within the international DSD consensus framework ([PMID: 16882788](https://pubmed.ncbi.nlm.nih.gov/16882788/), [PMID: 18987491](https://pubmed.ncbi.nlm.nih.gov/18987491/), [PMID: 17885459](https://pubmed.ncbi.nlm.nih.gov/17885459/)):

| Modality | Detail | Suggested NCIT |
|---|---|---|
| Hormone replacement | Estrogen (± progestin) or testosterone per sex of rearing/gonadal status | NCIT:C15417 (hormone therapy) |
| Gonadectomy | For germ-cell-tumor risk in dysgenetic gonads | NCIT:C15277 (surgery) / gonadectomy |
| Genital / reconstructive surgery | Individualized; deferred until autonomous consent where legally required (e.g., Germany) | NCIT:C15329 (reconstructive surgery) |
| Psychological support | DSD-specialized counseling; peer/empowerment programs | supportive care |
| Genetic counseling | Recurrence-risk (25% for AR), cascade testing | NCIT:C15681 (genetic counseling) |

Sex-of-rearing decisions should be based on the most likely adult gender identity, diagnosis, genital appearance, fertility potential, and psychosocial context ([PMID: 17885459](https://pubmed.ncbi.nlm.nih.gov/17885459/)). No pharmacogenomic or experimental targeted therapy is specific to SRXY5.

### 13. Prevention

- **Primary prevention:** not possible for a congenital monogenic disorder; **genetic counseling** and reproductive options (PGT/prenatal testing) for at-risk (carrier) couples.
- **Secondary prevention:** early molecular diagnosis; gonadal tumor **surveillance** and timely gonadectomy where indicated.
- **Tertiary prevention:** hormone replacement to prevent osteoporosis/metabolic complications; psychosocial support to reduce stigma-related morbidity.
- **Counseling:** autosomal-recessive recurrence risk 25% per pregnancy for carrier couples; cascade carrier testing. Immunization/public-health/environmental measures: not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / ortholog:** mouse *Cbx2* (NCBI Gene 12416, MGI:88289, Ensembl ENSMUSG00000025577, chromosome 11); NCBI Taxon 10090 (*Mus musculus*).
- **Natural disease:** no well-documented naturally occurring CBX2 sex-reversal disease in companion animals/wildlife is recorded here; the phenotype is known from engineered knockouts. (OMIA not confirmed for a spontaneous CBX2 DSD in this investigation.)
- **Comparative biology:** the CBX2→Sry/SF-1 hierarchy is conserved between mouse and human, validating cross-species inference; mouse recapitulates XY male-to-female sex reversal and gonadal hypoplasia.
- **Zoonotic potential:** not applicable.

### 15. Model Organisms

- **Primary model:** constitutive *M33/Cbx2*-knockout mouse (mammalian; Alliance/MGI:88289).
- **Model types available:** knockout (constitutive); the field also uses transgenic rescue lines (forced *Sry* or *Sox9* expression) demonstrating epistasis ([PMID: 22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/)). In-vitro human models: NT-2D1 Sertoli-like cells (DamID target mapping, [PMID: 25569159](https://pubmed.ncbi.nlm.nih.gov/25569159/)); gonadal fibroblasts and EBV-transformed lymphocytes express both CBX2 isoforms ([PMID: 23219007](https://pubmed.ncbi.nlm.nih.gov/23219007/)).
- **Phenotype recapitulation:** high — XY male-to-female sex reversal, gonadal hypoplasia, reduced SF-1, disrupted downstream TF network; additional homeotic skeletal transformations and germline/meiotic defects (broader Polycomb roles).
- **Limitations:** incomplete penetrance (~28.6%); pleiotropic phenotypes (skeletal, splenic, adrenal) beyond the human DSD focus; isoform biology (CBX2.1 vs CBX2.2) is human-relevant and less fully modeled in mouse.
- **Resources:** MGI, IMPC/IMSR for allele availability.

---

## Mechanistic Model / Interpretation

SRXY5 is best understood as a **failure of the upstream "permissive" chromatin switch** that normally licenses the male genetic program. CBX2, as a PRC1 reader of H3K27me3, sets the chromatin landscape that (a) *permits/activates SRY and NR5A1/SF-1* and (b) *represses the ovarian program*. Because CBX2 sits above SRY, its biallelic loss is functionally equivalent — at the level of outcome — to SRY loss, but it acts one tier higher and simultaneously de-represses female genes. The mouse rescue experiments provide the cleanest logic: restoring *Sry* or *Sox9* downstream corrects the sex-fate decision, proving CBX2's role in that decision is transmitted *through* SRY/SOX9; yet gonad size remains hypoplastic, revealing a second, parallel CBX2 output. This two-arm model (fate switch vs. growth) explains the clinical spectrum: patients can have ovaries with a uterus (fate fully flipped) or dysgenetic/ambiguous gonads (partial), depending on residual function and isoform involvement (CBX2.2→EMX2).

| Node | Role | Direction | Evidence |
|---|---|---|---|
| CBX2 (PRC1) | Chromatin permissive switch | Most upstream | Human [19361780]; mouse [9641679] |
| SRY | Testis-determining trigger | Downstream of CBX2 | Rescue [22186409] |
| SOX9 | Master Sertoli determinant | Downstream of SRY | Rescue [22186409] |
| NR5A1/SF-1 | Steroidogenic/gonadal TF | Downstream target | [15899914] |
| EMX2 (via CBX2.2) | Ovarian/gonadal regulator | Branch | [29998616] |

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [19361780](https://pubmed.ncbi.nlm.nih.gov/19361780/) | Ovaries/female phenotype in 46,XY girl with CBX2 mutations | Human clinical (index case) | Defines SRXY5; CBX2 upstream of SRY |
| [22186409](https://pubmed.ncbi.nlm.nih.gov/22186409/) | *Cbx2* required for *Sry* expression | Mouse genetic | Epistasis: Sry/Sox9 rescue |
| [9641679](https://pubmed.ncbi.nlm.nih.gov/9641679/) | Male-to-female sex reversal in M33 mutants | Mouse | Founding model; upstream of Sry |
| [15899914](https://pubmed.ncbi.nlm.nih.gov/15899914/) | M33 regulates Ad4BP/SF1 | Mouse/ChIP | SF-1 link |
| [25569159](https://pubmed.ncbi.nlm.nih.gov/25569159/) | Genome-wide CBX2 targets | In vitro (DamID) | Dual stimulate/repress role |
| [29998616](https://pubmed.ncbi.nlm.nih.gov/29998616/) | CBX2 isoform 2 targets in DSD | Human/functional | CBX2.2 variants; EMX2 |
| [31093962](https://pubmed.ncbi.nlm.nih.gov/31093962/) | PRC1 topology/enzymology | In vitro biochemistry | CBX2 structural role in PRC1 |
| [32979540](https://pubmed.ncbi.nlm.nih.gov/32979540/) | CBX protein functions review | Review | CBX2 as H3K27me3 reader in PRC1 |
| [22200029](https://pubmed.ncbi.nlm.nih.gov/22200029/) | Cbx2 in meiosis/germline | Mouse | Penetrance ~28.6%; germline role |
| [23219007](https://pubmed.ncbi.nlm.nih.gov/23219007/) | CBX2 in 46,XY/46,XX DSD cohort | Human cohort (n=47) | CBX2 not a common DSD cause; rarity |
| [31058389](https://pubmed.ncbi.nlm.nih.gov/31058389/) | PBX1 in testis-determination | Human | CBX2 protein-interaction partner; DDx |
| [18987491](https://pubmed.ncbi.nlm.nih.gov/18987491/) / [16882788](https://pubmed.ncbi.nlm.nih.gov/16882788/) / [17885459](https://pubmed.ncbi.nlm.nih.gov/17885459/) | DSD consensus statements | Clinical guideline | Management framework |
| [42597469](https://pubmed.ncbi.nlm.nih.gov/42597469/) / [41579703](https://pubmed.ncbi.nlm.nih.gov/41579703/) | Empower-DSD program | Clinical (QoL/education) | Quality-of-life/support evidence |

**Challenging/tempering evidence:** [PMID: 23219007](https://pubmed.ncbi.nlm.nih.gov/23219007/) explicitly found no pathogenic *CBX2* mutations in 47 DSD patients — a key check on over-attribution: CBX2 is a *rare* cause, not a common one.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity / small N.** The human disease is defined by very few molecularly confirmed cases; genotype–phenotype correlations, penetrance, and prevalence are consequently imprecise.
2. **Mechanistic gaps in humans.** The full downstream target set and the precise chromatin logic (which male genes are directly activated vs. which female genes de-repressed) are best characterized in cell lines and mouse, not patient gonads.
3. **Isoform biology.** The distinct contributions of CBX2.1 vs CBX2.2 (and the EMX2 axis) are incompletely resolved and may explain phenotypic variability.
4. **No prevalence/epidemiology data**, no natural-history cohort, and no SRXY5-specific omics datasets.
5. **No SRXY5-specific therapy or biomarker**; management is generic to 46,XY gonadal dysgenesis.
6. **Domain location paradox.** The pathogenic index missense variants (p.Pro98Leu, p.Arg443Pro) lie outside the chromodomain in disordered regions — the structural basis of their loss of function is not fully explained.

## Proposed Follow-up Experiments / Actions

1. **Establish an SRXY5 patient registry** and pursue GeneMatcher/international case aggregation to define penetrance, expressivity, and gonadal-tumor risk quantitatively.
2. **Functional characterization of p.Pro98Leu and p.Arg443Pro** (and CBX2.2 variants) in isogenic gonadal-somatic iPSC-derived models to map how disordered-region substitutions disrupt PRC1 assembly and target regulation.
3. **Single-cell / spatial transcriptomics of patient or knockout gonadal ridge** to resolve the Sertoli-vs-granulosa fate branch and validate the CBX2→SRY→SOX9 and CBX2.2→EMX2 arms in situ.
4. **Systematic reclassification of the many CBX2 VUS** in ClinVar using calibrated functional assays to improve diagnostic yield.
5. **Comparative-genomics / OMIA search** for spontaneous CBX2-related DSD in domestic species to add natural-disease models.
6. **Formalize a DSD-panel diagnostic algorithm** ensuring CBX2 (with CNV/MLPA coverage) is included and cross-referenced to ClinVar, and integrate multidisciplinary psychosocial support (Empower-DSD-type programs) into standard care.

---

*Report compiled from 9 confirmed findings and 21 reviewed papers, integrating human clinical, in-vitro/functional, model-organism, and computational-database evidence. Ontology suggestions (MONDO:0013120, HGNC:1552, GO:0007530/0008584/0035102, UBERON:0000991/0000992, CL:0000216, NCIT clinical-intervention terms) are provided for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](46_XY_Sex_Reversal_5-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](46_XY_Sex_Reversal_5-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 18 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013120` (4 mentions) - the report calls it "confirmed via EBI OLS", "MONDO"; MONDO calls it **46,XY sex reversal 5**
- `HP:0010461` (1 mention) - the report calls it "46,XY sex reversal"; HP calls it **Abnormality of the male genitalia**
- `HP:0000062` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Ambiguous genitalia**
- `HP:0000047` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Hypospadias**
- `HP:0000028` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cryptorchidism**
- `NCIT:C15417` (1 mention) - the report calls it "hormone therapy"; NCIT calls it **Randomized Clinical Trial**
- `NCIT:C15277` (1 mention) - the report calls it "surgery"; NCIT calls it **Mastectomy**
- `NCIT:C15681` (1 mention) - the report calls it "genetic counseling"; NCIT calls it **Cytotoxic Chemotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0062072` (1 mention) - the report calls it "histone reader activity"; GO calls it **histone H3K9me2/3 reader activity**, and lists "histone H3K9me2 reader activity" among its other names
- `GO:0045892` (1 mention) - the report calls it "negative regulation of transcription"; GO calls it **negative regulation of DNA-templated transcription**
- `HP:0000812` (1 mention) - the report calls it "abnormal external genitalia"; HP calls it **Abnormal internal genitalia**
- `HP:0000130` (1 mention) - the report calls it "abnormal uterus"; HP calls it **Abnormality of the uterus**
- `NCIT:C15329` (1 mention) - the report calls it "reconstructive surgery"; NCIT calls it **Surgical Procedure**, and lists "Type of Surgery" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013120` - called "confirmed via EBI OLS", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.