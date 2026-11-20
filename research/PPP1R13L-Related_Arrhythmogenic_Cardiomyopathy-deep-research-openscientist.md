---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T21:48:32.840517'
end_time: '2026-11-11T22:02:21.185566'
duration_seconds: 828.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PPP1R13L-Related Arrhythmogenic Cardiomyopathy
  mondo_id: MONDO:0957795
  category: Mendelian
  causal_genes: PPP1R13L
  omim_id: OMIM:620519
  synonyms: PPP1R13L cardiocutaneous syndrome; PPP1R13L-associated cardiocutaneous
    syndrome; PPP1R13L-related cardiomyopathy
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
citation_count: 18
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 19
  on_topic: 14
  validator_version: 0.5.1
term_validation:
  total_terms: 19
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0957795
    reported_labels:
    - MONDO
    ontology_label: arrhythmogenic cardiomyopathy with variable ectodermal abnormalities
  - term_id: HP:0002216
    reported_labels:
    - Woolly hair
    ontology_label: Premature graying of hair
  labels_variant: 1
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
  path: PPP1R13L-Related_Arrhythmogenic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PPP1R13L-Related_Arrhythmogenic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PPP1R13L-Related Arrhythmogenic Cardiomyopathy
- **MONDO ID:** MONDO:0957795 (if available)
- **Causal gene(s):** PPP1R13L
- **OMIM:** OMIM:620519
- **Synonyms:** PPP1R13L cardiocutaneous syndrome; PPP1R13L-associated cardiocutaneous syndrome; PPP1R13L-related cardiomyopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PPP1R13L-Related Arrhythmogenic Cardiomyopathy** covering all of the
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

# PPP1R13L-Related Arrhythmogenic Cardiomyopathy: A Comprehensive Disease Characterization

**Disease:** PPP1R13L-Related Arrhythmogenic Cardiomyopathy (PPP1R13L cardiocutaneous syndrome)
**Causal gene:** **PPP1R13L** (protein phosphatase 1 regulatory subunit 13 like; encodes **iASPP**, the inhibitor of apoptosis-stimulating protein of p53; also known as RAI, NKIP1)
**Key identifiers:** OMIM:620519 · MONDO:0957795 · HGNC gene PPP1R13L · Chromosome 19q13.2–q13.32
**Category:** Mendelian, autosomal-recessive

---

## Summary

PPP1R13L-related arrhythmogenic cardiomyopathy is an **ultra-rare, autosomal-recessive cardiocutaneous syndrome** caused by **biallelic loss-of-function variants in PPP1R13L**, the gene encoding **iASPP** (inhibitor of apoptosis-stimulating protein of p53, also historically called NKIP1/RAI). The disease is distinct from the many serially numbered cardiomyopathies: the causal gene here is unambiguously **PPP1R13L**, not a desmosomal plakin or a sarcomeric gene, although the downstream lesion converges on the cardiac desmosome. To date only approximately **15–20 affected children** have been reported worldwide, typically from consanguineous or founder pedigrees. The cardinal manifestation is **severe, early-onset, rapidly progressive dilated/arrhythmogenic cardiomyopathy** (mean onset ~2 years 10 months; range 3 months–9 years) with ventricular arrhythmias and high early-childhood mortality, accompanied by a **variably expressed ectodermal phenotype** (woolly/sparse hair, abnormal/pointed teeth, skin abnormalities) and, in some families, orofacial clefting and ocular disease (glaucoma, keratitis).

The **central disease mechanism** is loss of iASPP from the cardiomyocyte **intercalated disc**, where iASPP normally binds **desmoplakin and desmin** and maintains the integrity of the **desmosome–intermediate-filament network**. Its loss destabilizes desmin anchoring at the intercalated disc, producing an arrhythmogenic right-ventricular cardiomyopathy (ARVC)-like phenotype with sudden cardiac death — demonstrated concordantly in **human explanted hearts**, **Ppp1r13l-mutant mice**, and naturally occurring **Poll Hereford cattle** cardiomyopathy and woolly-haircoat syndrome. Two additional mechanistic arms amplify disease: dysregulated **NF-κB / IL-1 inflammation** (iASPP is a common inhibitor of RelA/p65 and p53) and loss of **Keap1–Nrf2 antioxidant protection**, which sensitizes cardiomyocytes to oxidative/hypoxic injury. The ectodermal features are attributable to iASPP's regulation of **p63**, which is required for epithelial stratification.

**Diagnosis** rests on exome or genome sequencing (biallelic-variant filtering) combined with ACM/DCM cardiac workup (echocardiography, cardiac MRI with late gadolinium enhancement, ECG/Holter, and explant/autopsy histopathology). **Management** is supportive: heart-failure pharmacotherapy, antiarrhythmics, implantable cardioverter-defibrillator (ICD), and definitive **heart transplantation** for end-stage disease. **Investigational IL-1 blockade** reduces ventricular ectopy and normalizes serum cytokines but has not restored contractile function. Prognosis is poor without transplantation, with multiple deaths before age three in reported cohorts.

---

## Section 1 — Disease Information

**Overview.** PPP1R13L-related arrhythmogenic cardiomyopathy (also termed **PPP1R13L cardiocutaneous syndrome** or **PPP1R13L-associated cardiocutaneous syndrome**) is a Mendelian, autosomal-recessive disorder in which biallelic loss of function of PPP1R13L produces a syndromic combination of **life-threatening childhood cardiomyopathy** (dilated and/or arrhythmogenic) plus **ectodermal abnormalities** of hair, skin, and teeth. The cardiomyopathy may show features of inflammation on histology. First described in humans in 2017 as a lethal infantile dilated cardiomyopathy in Arab Christian infants, the condition has since been expanded through international gene-matching efforts and single case reports.

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM | **620519** (phenotype); PPP1R13L gene 607463 |
| MONDO | **MONDO:0957795** |
| Gene (HGNC) | **PPP1R13L** |
| Protein (UniProt) | iASPP (Q8WUF5) |
| Cytogenetic locus | 19q13.2–q13.32 |

**Synonyms / alternative names:** PPP1R13L cardiocutaneous syndrome; PPP1R13L-associated cardiocutaneous syndrome; PPP1R13L-related cardiomyopathy; iASPP-related cardiomyopathy. The gene carries legacy aliases **NKIP1** (NF-κB interacting protein 1) and **RAI** (RelA-associated inhibitor).

**Information source.** Knowledge is derived almost exclusively from **individual-patient clinical reports and small family cohorts** (case reports, GeneMatcher-facilitated case series, and explant/autopsy studies), supplemented by **model-organism** (mouse, cattle) and **in vitro** mechanistic work. There are no aggregated registry- or EHR-scale datasets because of the disease's rarity.

---

## Section 2 — Etiology

**Primary cause — genetic.** The disease is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in PPP1R13L**. There is no infectious, toxic, or environmental primary cause. The GeneMatcher-facilitated international study identified biallelic PPP1R13L variants in **seven children from five unrelated families** with severe dilated cardiomyopathy following exome or genome sequencing, establishing a robust gene–disease association: *"biallelic variants in PPP1R13L were identified in seven children with severe DCM from five unrelated families following exome or genome sequencing"* ([PMID: 32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/)). The ClinGen DCM gene-curation expert panel's 2024–2025 reassessment of 68 genes includes PPP1R13L among curated DCM genes ([PMID: 42708185](https://pubmed.ncbi.nlm.nih.gov/42708185/)).

**Genetic risk factors.** The disease is monogenic and recessive; the sole genetic requirement is two defective PPP1R13L alleles. **Consanguinity** and **founder alleles** are major contributors (see Section 9). Reported disease variants are predominantly **nonsense and frameshift** (loss-of-function) alleles.

**Environmental risk factors.** None established as causal. As with other arrhythmogenic cardiomyopathies, **physical exertion** and **sympathetic/adrenergic stress** are plausible arrhythmia triggers, and inflammatory flares may contribute, but no PPP1R13L-specific environmental risk factor has been demonstrated. Sex does not appear to modify primary risk (recessive, both sexes affected).

**Protective factors.** No genetic or environmental protective factors have been identified. Heterozygous carriers are generally unaffected, consistent with recessive inheritance and the absence of a dominant-negative effect for most LoF alleles.

**Gene–environment interactions.** Not formally characterized. The mechanistic convergence on **inflammation (NF-κB/IL-1)** and **oxidative stress (Nrf2/Keap1)** suggests that inflammatory or ischemic/hypoxic stressors could plausibly worsen myocardial injury in genetically susceptible individuals, but this remains **inferred, not demonstrated**.

---

## Section 3 — Phenotypes

The phenotype is **syndromic and variably expressed**, even within families. Approximately 15 patients were tabulated in one 2024 review, which summarized that *"PPP1R13L is associated with a recessive syndrome leading to cardiac anomalies with skin, teeth, and hair abnormalities. Fifteen patients have been described so far"* ([PMID: 39579152](https://pubmed.ncbi.nlm.nih.gov/39579152/)).

### Cardiac (core, high penetrance)
- **Severe early-onset dilated cardiomyopathy / arrhythmogenic cardiomyopathy** — ventricular dilatation and systolic dysfunction; the dominant and most lethal feature.
- **Ventricular arrhythmias / premature ventricular contractions / ventricular tachycardia** — arrhythmogenic substrate, risk of sudden cardiac death.
- **Heart failure** — progressive, leading to death or transplant.
- Suggested HPO: **HP:0001644** (Dilated cardiomyopathy), **HP:0011663** (Right ventricular cardiomyopathy / arrhythmogenic), **HP:0004308** (Ventricular arrhythmia), **HP:0001635** (Congestive heart failure), **HP:0001645** (Sudden cardiac death).

### Ectodermal (variably expressed)
- **Woolly / sparse / dry hair**, **high anterior hairline** — HP:0002216 (Woolly hair), HP:0008070 (Sparse hair).
- **Abnormal / pointed teeth** — dental anomalies.
- **Skin abnormalities** — abnormal epidermal morphology.
- **Broad nasal bridge**, dysmorphic features.

### Orofacial and ocular (subset of families)
- **Cleft lip and palate** — HP:0000202.
- **Glaucoma** — HP:0000501; **keratitis** / ocular surface disease (neonatal keratitis also seen in the bovine model).

### Other / expanded phenotype
- **Anorectal anomaly** reported in an extended-phenotype case ([PMID: 39579152](https://pubmed.ncbi.nlm.nih.gov/39579152/)).
- **Global developmental delay** in one child ([PMID: 37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/)).

**Characteristics.** Age of onset: **neonatal to childhood** (cardiac mean ~2 y 10 m). Severity: **severe** for cardiac features; **mild–moderate and variable** for ectodermal features. Progression: cardiac disease is **progressive**; arrhythmias are **episodic**. Frequency: cardiomyopathy is near-universal in affected individuals; ectodermal features are present in most but **variably expressed**, so a given patient may have DCM without obvious skin/hair findings, which can obscure the syndromic diagnosis.

Intrafamilial variability is well illustrated in a consanguineous family where *"The index case had DCM and wooly hair, two of his siblings had DCM and CLP while three cousins had, in addition, glaucoma"* ([PMID: 37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/)).

**Quality-of-life impact.** Severe. Affected children face recurrent heart failure, arrhythmia, hospitalization, transplant evaluation, and frequently death in early childhood. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare condition.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** **PPP1R13L** (OMIM gene 607463), chromosome **19q13.2–q13.32**, 13 exons, encoding **iASPP**. iASPP contains ankyrin repeats and an SH3 domain mediating its protein–protein interactions with p53-family proteins and with desmosomal proteins ([PMID: 18275817](https://pubmed.ncbi.nlm.nih.gov/18275817/)).

**Pathogenic variants (representative).**
| Variant (protein / cDNA) | Type | Zygosity | Phenotype / note | PMID |
|---|---|---|---|---|
| Homozygous premature stop codon | Nonsense | Homozygous | 5 Arab Christian infants, 4 families; lethal infantile DCM (founder) | [28069640](https://pubmed.ncbi.nlm.nih.gov/28069640/) |
| p.Arg330ProfsTer76 | Frameshift | Homozygous | Consanguineous family, 6 affected children | [37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/) |
| p.Gln194Ter (c.580C>T) | Nonsense | Homozygous | Arrhythmogenic cardiomyopathy | [35933355](https://pubmed.ncbi.nlm.nih.gov/35933355/) |
| Novel frameshift | Frameshift | Homozygous | 4-year-old, DCM + ectodermal features | [41919412](https://pubmed.ncbi.nlm.nih.gov/41919412/) |
| Multiple biallelic LoF (5 families) | Nonsense/frameshift | Biallelic | GeneMatcher cohort, 7 children | [32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/) |
| Bovine c.956_962dup7, p.Ser322GlnfsX4 | Frameshift | Homozygous | Poll Hereford cattle CWH model | [19016676](https://pubmed.ncbi.nlm.nih.gov/19016676/) |

**Variant classification.** Reported disease alleles are overwhelmingly **pathogenic/likely pathogenic loss-of-function** (nonsense, frameshift) per ACMG/AMP criteria. The nonsense example was described as *"a novel homozygous stop-gain pathogenic variant, c.580C > T: p.Gln194Ter, in the PPP1R13L gene"* ([PMID: 35933355](https://pubmed.ncbi.nlm.nih.gov/35933355/)). A heterozygous missense variant p.A620P was scored only as a **VUS** in an ACM screen where a co-occurring TP63 nonsense variant was likely pathogenic, and the authors concluded PPP1R13L involvement in that case "remains to be determined" ([PMID: 30453078](https://pubmed.ncbi.nlm.nih.gov/30453078/)) — underscoring that the established disease mechanism is **biallelic LoF**, not monoallelic missense.

**Allele frequency.** Causal alleles are extremely rare/private in population databases (gnomAD), consistent with an ultra-rare recessive disorder; some alleles are population-enriched founder variants.

**Somatic vs germline.** **Germline** exclusively.

**Functional consequence.** **Loss of function** (biallelic). Loss of iASPP protein removes its stabilizing role at the intercalated disc and its regulatory inhibition of p53/p63/NF-κB.

**Modifier genes.** None formally established. Given iASPP's binding partners, **desmoplakin, desmin, TP63, and NF-κB-pathway genes** are mechanistically plausible modifiers but unproven in humans.

**Epigenetic information.** No PPP1R13L-specific disease methylation/chromatin data available.

**Chromosomal abnormalities.** None; disease is caused by small sequence variants, not large structural rearrangements.

---

## Section 5 — Environmental Information

No environmental, lifestyle, or infectious agent is a **cause** of this monogenic disease. Of note, PPP1R13L-related cardiomyopathy can **present as or mimic myocarditis** (inflammatory histology), which is relevant to differential diagnosis rather than etiology; some reports describe inflammation on cardiac histology ([PMID: 35924320](https://pubmed.ncbi.nlm.nih.gov/35924320/)). Standard arrhythmia precautions (avoidance of extreme exertion) are advisable as for other arrhythmogenic cardiomyopathies, but this is extrapolated rather than PPP1R13L-specific.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variant in PPP1R13L** → **leads to** absence/severe reduction of iASPP protein.
2. Loss of iASPP **at the cardiomyocyte intercalated disc** → **results in** failure to bind and stabilize **desmoplakin and desmin** (*"iASPP interacts with desmoplakin and desmin in cardiomyocytes to maintain the integrity of desmosomes and intermediate filament networks in vitro and in vivo"*, [PMID: 25691752](https://pubmed.ncbi.nlm.nih.gov/25691752/)).
3. Destabilized desmosome–intermediate-filament network → **leads to** **loss of desmin anchoring at the intercalated disc** — the central lesion seen in human explants (*"loss of desmin-desmosome anchoring in cardiomyocytes appears to be the central mechanism of PPP1R13L cardiomyopathy"*, [PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)).
4. Weakened cell–cell adhesion under mechanical load → **results in** cardiomyocyte injury, an **ARVC-like structural phenotype** (RV dilatation; demonstrated at E16.5 in mice) and progressive ventricular dysfunction.
5. **Branch A (inflammation):** Loss of iASPP's inhibition of **RelA/p65 NF-κB** → **leads to** increased NF-κB signaling and **IL-1/cytokine-driven inflammation** (increased nuclear NF-κB in non-cardiomyocytes of human explants) → amplifies myocardial damage and arrhythmogenic remodeling.
6. **Branch B (oxidative stress):** Loss of iASPP → **results in** impaired **Keap1–Nrf2** antioxidant activation → cardiomyocytes become sensitized to hypoxia/reoxygenation injury, with **increased apoptosis and ROS** (*inferred* for human disease; demonstrated in rodent cardiomyocytes).
7. **Branch C (ectodermal):** Loss of iASPP's regulation of **p63** → **leads to** defective epithelial stratification → **hair, skin, dental, and orofacial** abnormalities.
8. Convergence → **severe early-onset dilated/arrhythmogenic cardiomyopathy**, **ventricular arrhythmias**, **heart failure**, and **sudden cardiac death**.

### Detail by category

**Molecular pathways.** Three interlocking axes: (1) **desmosomal / cytoskeletal** structural pathway (desmoplakin–desmin at the intercalated disc); (2) **NF-κB inflammatory** signaling — *"inhibitor of Apoptosis Stimulating p53 Protein (iASPP) is one such common regulator of both RelA/p65 and p53"* ([PMID: 26646590](https://pubmed.ncbi.nlm.nih.gov/26646590/)); (3) **Keap1–Nrf2 (NFE2L2)** antioxidant signaling ([PMID: 33332723](https://pubmed.ncbi.nlm.nih.gov/33332723/)). A fourth, **p53/p63** transcriptional regulation, underlies the ectodermal phenotype — *"iASPP is likely to control epithelial stratification by regulating p63's transcriptional activity"* ([PMID: 21930934](https://pubmed.ncbi.nlm.nih.gov/21930934/)).

**Cellular processes.** Cell–cell adhesion/desmosome assembly, apoptosis regulation, inflammation, oxidative-stress response, and epithelial stratification/differentiation.

**Protein dysfunction.** **Loss of function** of iASPP — a shuttling multifunctional protein that in the nucleus inhibits p53/p63 and in the cytoplasm/intercalated disc regulates desmosome integrity. iASPP's ankyrin-repeat + SH3 architecture mediates differential binding to p53, p63, and p73 ([PMID: 18275817](https://pubmed.ncbi.nlm.nih.gov/18275817/)).

**Metabolic / oxidative changes.** Impaired Nrf2-dependent antioxidant defense elevates ROS and apoptosis under hypoxia/reoxygenation: *"The upregulation of iASPP repressed H/R-induced injury by decreasing levels of apoptosis and reactive oxygen species production"* and *"iASPP ameliorates H/R-induced apoptosis and oxidative stress in cardiomyocytes via potentiating Nrf2 signaling via modulation of Keap1"* ([PMID: 33332723](https://pubmed.ncbi.nlm.nih.gov/33332723/)).

**Immune involvement.** Dysregulated NF-κB → IL-1-driven inflammation; human explants show increased NF-κB nuclear signaling in non-cardiomyocytes ([PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)).

**Tissue-damage mechanisms.** Mechanical disruption of intercalated discs, fibrosis/fibrofatty remodeling (ACM-type substrate), inflammatory injury, and oxidative/apoptotic cardiomyocyte loss.

**Molecular profiling.** Human explant immunofluorescence demonstrates **loss of desmin at the intercalated disk** as the central feature distinguishing PPP1R13L hearts from non-PPP1R13L DCM controls, plus increased NF-κB in non-cardiomyocytes ([PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)).

**Suggested ontology terms.** GO: desmosome organization, cell–cell junction assembly, apoptotic process (**GO:0006915**), NF-κB signaling (**GO:0038061**), cellular response to oxidative stress (**GO:0034599**), regulation of transcription (**GO:0006355**). CL: cardiac muscle cell / cardiomyocyte (**CL:0000746**), keratinocyte (**CL:0000312**).

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary: **heart** (UBERON:0000948), especially the **ventricular myocardium** with right- and both-ventricular involvement. Secondary systems: **integument** (skin, hair follicles), **teeth / oral cavity**, **eye** (glaucoma, cornea). Body systems: **cardiovascular** (primary), **integumentary/ectodermal**, **orofacial/craniofacial**, **ocular/visual**.

**Tissue and cell level.** **Cardiac muscle tissue** and **cardiomyocytes** (CL:0000746), specifically at the **intercalated disc** where iASPP, desmoplakin, and desmin co-localize. Ectodermally derived **epithelial/keratinocyte** lineages (CL:0000312) account for hair/skin/tooth features.

**Subcellular level.** **Intercalated disc / desmosome** (GO:0030057 desmosome), **intermediate-filament cytoskeleton** (desmin network), **nucleus** (p53/p63/NF-κB transcriptional regulation), **cytoplasm** (iASPP shuttling).

**Localization & lateralization.** Cardiac involvement is **biventricular** with frequent **right-ventricular** structural change (ARVC-like). Ectodermal features are generally **bilateral/symmetric**.

---

## Section 8 — Temporal Development

**Onset.** **Congenital to early-childhood.** Cardiac presentation is early: mean **2 years 10 months** (range **3 months–9 years**) ([PMID: 32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/)); the original cohort presented at **4–30 months** — *"Five Arab Christian infants, aged 4-30 months from four families, were diagnosed with DCM associated with mild skin, teeth, and hair abnormalities. All passed away before age 3"* ([PMID: 28069640](https://pubmed.ncbi.nlm.nih.gov/28069640/)). Onset pattern is typically **subacute to chronic-progressive**, sometimes with an acute decompensated heart-failure presentation.

**Progression.** **Rapidly progressive.** DCM *"presented early (mean: 2 years 10 months; range: 3 months-9 years) and was progressive, resulting in death (n = 3) or transplant (n = 3), with one child currently awaiting transplant"* among 7 children ([PMID: 32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/)). Disease course is **progressive** for pump failure with **episodic** arrhythmic events.

**Patterns.** No spontaneous remission. The only "remission" is **treatment/transplant-induced** replacement of the diseased organ. The **critical intervention window** is early childhood — before irreversible pump failure — arguing for early genetic diagnosis, arrhythmia surveillance, and timely transplant evaluation.

---

## Section 9 — Inheritance and Population

**Inheritance.** **Autosomal recessive.** Both biallelic homozygous (consanguineous/founder) and compound-heterozygous genotypes are reported.

**Epidemiology.** **Ultra-rare**; only ~15–20 patients reported worldwide. No formal prevalence/incidence estimates exist. The disease is likely **underdiagnosed** because its cardiac phenotype overlaps non-syndromic DCM and PPP1R13L is a recent addition to gene panels.

**Penetrance / expressivity.** Cardiomyopathy penetrance appears **high** in biallelic-LoF individuals; **ectodermal features are variably expressed** even among affected siblings/cousins ([PMID: 37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/)). Expressivity is therefore **variable**.

**Founder effects / consanguinity.** Strong role. The first human cohort — homozygous premature stop codon in **5 Arab Christian infants from 4 families** — is consistent with a **regional founder allele** ([PMID: 28069640](https://pubmed.ncbi.nlm.nih.gov/28069640/)). A recurrent homozygous frameshift **p.Arg330ProfsTer76** segregated in a **consanguineous family with 6 affected children** ([PMID: 37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/)). Consanguinity is a recurring feature across pedigrees.

**Genetic anticipation / germline mosaicism.** No evidence (not a repeat-expansion disorder; recessive).

**Carrier frequency.** Not formally established; expected to be very low in general populations but potentially elevated in specific founder/consanguineous communities.

**Demographics.** Reported across Middle Eastern (Arab Christian), consanguineous, and other populations. **Both sexes affected** (recessive; no sex predilection). **Age distribution** skews to infancy/early childhood owing to high early mortality. The gene maps to chromosome **19q13.2–q13.32** (bovine orthologue on BTA18, [PMID: 19016676](https://pubmed.ncbi.nlm.nih.gov/19016676/)).

---

## Section 10 — Diagnostics

**Genetic testing is the diagnostic cornerstone.** All reported PPP1R13L cases were identified by **whole-exome or whole-genome sequencing** with biallelic-variant filtering ([PMID: 32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/), [PMID: 37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/)). Single-gene testing rarely suffices because the presentation overlaps non-syndromic DCM and PPP1R13L is a newer panel addition; authors recommend that *"PPP1R13L should be included in ACM genetic testing to improve the identification of at-risk family members and the diagnostic yield"* ([PMID: 35933355](https://pubmed.ncbi.nlm.nih.gov/35933355/)). WES/WGS with biallelic filtering and gene panels covering cardiomyopathy/ACM genes are the preferred approaches; CMA/karyotype/FISH/mitochondrial/repeat-expansion testing are **not applicable** (small sequence variants, nuclear recessive).

**Cardiac workup (parallels ACM/DCM).**
- **Echocardiography** — ventricular dilatation and systolic dysfunction.
- **Cardiac MRI with late gadolinium enhancement (LGE)** — the gold standard for ventricular structure/function, edema, and fibrosis: *"Cardiac magnetic resonance imaging (CMR) with late gadolinium enhancement (LGE) is the gold standard for evaluating left and right ventricular structure and function, edema, and fibrosis"* ([PMID: 34970070](https://pubmed.ncbi.nlm.nih.gov/34970070/)); detects fibrofatty/RV substrate.
- **ECG / Holter monitoring** — ventricular arrhythmia burden, PVCs, VT.
- **Histopathology** on explant/autopsy — **loss of desmin at the intercalated disk** and increased NF-κB in non-cardiomyocytes are characteristic ([PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)).
- **Postmortem genetic testing** confirms concealed arrhythmogenic cardiomyopathy in sudden death, including PPP1R13L ([PMID: 42098522](https://pubmed.ncbi.nlm.nih.gov/42098522/)).

**Biomarkers.** No specific circulating biomarker; serum **IL-1/IL-10** can be elevated and track with the inflammatory arm (and normalize with IL-1 blockade) ([PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)). Standard heart-failure biomarkers (BNP/NT-proBNP, troponin) apply generically.

**Clinical criteria & differential diagnosis.** Diagnosis integrates ACM/DCM imaging-electrophysiology criteria with **confirmatory biallelic PPP1R13L genotype**. Differentials: desmosomal ACM (DSP, PKP2, DSG2), other childhood DCM (sarcomeric, metabolic, mitochondrial), **myocarditis** (which PPP1R13L disease can mimic), and syndromic ectodermal disorders. The presence of **ectodermal features (woolly hair, dental/skin anomalies)** alongside early DCM should prompt PPP1R13L testing.

**Screening.** **Cascade genetic testing** of at-risk relatives and **carrier testing** in consanguineous families; prenatal/preimplantation testing is feasible when the familial variant is known.

---

## Section 11 — Outcome / Prognosis

**Poor, with high early-childhood mortality.** In the 7-child cohort, outcomes were **3 deaths, 3 transplants, and 1 awaiting transplant** ([PMID: 32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/)). In the original cohort, all **5 infants died before age 3** ([PMID: 28069640](https://pubmed.ncbi.nlm.nih.gov/28069640/)). In a consanguineous family with p.Arg330ProfsTer76, **all but one of 6 affected children died in early childhood** ([PMID: 37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/)).

**Mortality mechanisms.** Progressive **heart failure** and **sudden cardiac death** from ventricular arrhythmia (ARVC-like substrate).

**Morbidity / QoL.** Severe cardiac disability, recurrent hospitalization, transplant dependency; ectodermal and ocular comorbidity in subsets. No validated QoL instruments reported.

**Recovery potential.** No spontaneous recovery; **heart transplantation is definitive** for end-stage disease. IL-1 blockade reduced arrhythmia *"without contractile recovery"* ([PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)).

**Prognostic factors.** Early age at cardiac onset, rapid progression to heart failure, high ventricular-arrhythmia burden, and extent of LGE/fibrosis portend worse outcome (extrapolated from ACM literature; [PMID: 39486037](https://pubmed.ncbi.nlm.nih.gov/39486037/), [PMID: 34970070](https://pubmed.ncbi.nlm.nih.gov/34970070/)).

---

## Section 12 — Treatment

**No disease-specific or curative pharmacotherapy exists.** Management is supportive and mirrors ACM/DCM care.

**Pharmacotherapy (supportive).** Standard **heart-failure therapy** (as age-appropriate: ACE inhibitors/ARBs, beta-blockers, diuretics, aldosterone antagonists) and **antiarrhythmics** for ventricular arrhythmia control. NCIT concepts: heart-failure pharmacotherapy, antiarrhythmic agents.

**Device / interventional.** **Implantable cardioverter-defibrillator (ICD)** for sudden-death prevention given the arrhythmogenic substrate (NCIT: Implantable Cardioverter Defibrillator).

**Definitive therapy.** **Heart transplantation** — the definitive treatment for end-stage disease ([PMID: 32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/)). NCIT: Heart Transplantation.

**Investigational / emerging — IL-1 blockade.** Two pediatric patients (47 and 32 months) with refractory ventricular arrhythmias/heart failure received **anti-IL-1 immunomodulatory therapy**: *"IL-1 blockade was associated with reduced ventricular ectopy and normalized serum cytokine levels (IL-1, IL-10) but without contractile recovery"* ([PMID: 41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/)). This targets the NF-κB/IL-1 inflammatory arm and is the most promising mechanism-informed adjunct to date, though it does not reverse pump failure.

**Pharmacogenomics / gene / cell / RNA therapy.** None established. Gene-replacement is conceptually attractive (recessive LoF) but not developed.

---

## Section 13 — Prevention

- **Primary prevention:** For a recessive Mendelian disease, prevention is reproductive/genetic — **genetic counseling, carrier screening in consanguineous/founder families, and prenatal or preimplantation genetic testing** when the familial variant is known.
- **Secondary prevention:** **Cascade genetic testing** of relatives, with early cardiac surveillance (echo/CMR/Holter) of genotype-positive children to enable timely heart-failure therapy, ICD, and transplant listing.
- **Tertiary prevention:** Arrhythmia management, ICD for sudden-death prevention, heart-failure optimization, and investigational IL-1 blockade to reduce arrhythmic burden.
- **Counseling:** Autosomal-recessive recurrence risk is **25%** per pregnancy for carrier couples; discuss consanguinity.
- **No immunization or public-health/environmental prevention applies** (monogenic disease).

---

## Section 14 — Other Species / Natural Disease

PPP1R13L-related disease is notable for a **naturally occurring large-animal model**. **Poll Hereford cattle** develop **cardiomyopathy and woolly-haircoat syndrome (CWH)** caused by a PPP1R13L (NKIP1/RAI) frameshift — *"a 7-bp duplication (c.956_962dup7) in exon 6 of this 13-exon gene"*, p.Ser322GlnfsX4, on BTA18 ([PMID: 19016676](https://pubmed.ncbi.nlm.nih.gov/19016676/)). The bovine phenotype strikingly parallels the human syndrome: **cardiomyopathy + woolly haircoat**, plus neonatal keratitis — making it a strong comparative-pathology model and one of the earliest clues linking PPP1R13L to a cardiocutaneous syndrome.

- **Taxonomy:** *Bos taurus* (NCBI Taxon 9913); *Mus musculus* (NCBI Taxon 10090).
- **Orthologous gene:** bovine/murine **Ppp1r13l**.
- **Comparative biology:** The cardiac desmosomal mechanism and the hair/skin phenotype are **evolutionarily conserved** across human, mouse, and cattle, supporting mechanistic generalizability.
- **Zoonotic potential:** None (genetic disease).

---

## Section 15 — Model Organisms

**Mouse.** The **Ppp1r13l(Δ8/Δ8)** (exon-8 deletion) mouse — *"iASPP-deficient mice with exon 8 deletion (Ppp1r13l(Δ8/Δ8)) die of sudden cardiac death, displaying features of ARVC"* ([PMID: 25691752](https://pubmed.ncbi.nlm.nih.gov/25691752/)). iASPP deficiency induces **right-ventricular dilatation at E16.5**, and iASPP interacts with desmoplakin and desmin to maintain desmosome/intermediate-filament integrity *in vitro* and *in vivo*. The **Wa3** mouse is an additional allele. These models **recapitulate** arrhythmogenic cardiomyopathy and sudden death well, validating the desmosomal mechanism.

**Cattle (natural model).** Poll Hereford CWH (above) — excellent recapitulation of the combined **cardiac + cutaneous** phenotype ([PMID: 19016676](https://pubmed.ncbi.nlm.nih.gov/19016676/)).

**In vitro / cellular.** Rodent cardiomyocyte hypoxia/reoxygenation systems demonstrate the **Nrf2/Keap1 cardioprotective** arm ([PMID: 33332723](https://pubmed.ncbi.nlm.nih.gov/33332723/)); cancer-cell and epithelial systems established iASPP's **p53/p63/NF-κB** regulatory roles ([PMID: 21930934](https://pubmed.ncbi.nlm.nih.gov/21930934/), [PMID: 26646590](https://pubmed.ncbi.nlm.nih.gov/26646590/)).

**Model limitations.** Mouse embryonic lethality/early death complicates longitudinal study; cellular systems address single pathways in isolation; no patient-derived iPSC-cardiomyocyte model is yet prominent in the literature reviewed. **Research applications:** mechanism of intercalated-disc/desmosome maintenance, arrhythmogenesis, inflammatory and oxidative-stress contributions, and preclinical testing of anti-inflammatory/antioxidant interventions.

**Model resources:** MGI (mouse), OMIA (cattle, natural disease).

---

## Mechanistic Model / Interpretation

```
          Biallelic LoF PPP1R13L  →  loss of iASPP protein
                                  |
        ┌─────────────────────────┼──────────────────────────────┐
        │                         │                              │
  STRUCTURAL (central)      INFLAMMATORY (Branch A)      OXIDATIVE (Branch B)
  loss of iASPP at           loss of NF-κB (RelA/p65)     loss of Keap1–Nrf2
  intercalated disc          inhibition                  activation
        │                         │                              │
  desmoplakin–desmin         ↑ NF-κB / IL-1 cytokines      ↑ ROS, ↑ apoptosis
  desmosome destabilized     (seen in human explants)      under hypoxia/reox
        │                         │                              │
  loss of desmin anchoring   inflammatory myocardial       cardiomyocyte
  (human explant hallmark)   injury & remodeling           sensitization
        └───────────┬─────────────┴──────────────────────────────┘
                    ▼
     Severe early-onset DILATED / ARRHYTHMOGENIC cardiomyopathy
     → ventricular arrhythmias → heart failure → sudden cardiac death

  Branch C (ectodermal):  loss of iASPP → dysregulated p63 →
     defective epithelial stratification → woolly/sparse hair,
     dental, skin, orofacial (cleft), ocular features
```

The **structural desmosomal lesion is the dominant, directly demonstrated driver** (human explants, mouse, cattle). The **inflammatory and oxidative branches are amplifiers**: the inflammatory arm is supported by human explant NF-κB data and the clinical response of arrhythmia to IL-1 blockade, while the oxidative arm is currently **inferred from rodent cardiomyocytes**. The **p63 branch** cleanly explains the non-cardiac ectodermal phenotype, unifying the "cardiocutaneous" syndrome under a single gene.

---

## Evidence Base

| PMID | Study type | Contribution |
|---|---|---|
| [32666529](https://pubmed.ncbi.nlm.nih.gov/32666529/) | Human case series (GeneMatcher) | Gene–disease validation; 7 children/5 families; natural history & poor prognosis |
| [28069640](https://pubmed.ncbi.nlm.nih.gov/28069640/) | Human cohort | First human description; founder nonsense allele; lethal infantile DCM |
| [25691752](https://pubmed.ncbi.nlm.nih.gov/25691752/) | Mouse + in vitro | Core desmosomal mechanism; iASPP–desmoplakin–desmin; ARVC & sudden death |
| [41928611](https://pubmed.ncbi.nlm.nih.gov/41928611/) | Human explant + therapy | Desmin-loss central mechanism; NF-κB in non-cardiomyocytes; IL-1 blockade |
| [19016676](https://pubmed.ncbi.nlm.nih.gov/19016676/) | Cattle (natural model) | PPP1R13L frameshift causes bovine cardiomyopathy + woolly haircoat |
| [21930934](https://pubmed.ncbi.nlm.nih.gov/21930934/) | In vitro | iASPP controls epithelial stratification via p63 (ectodermal features) |
| [26646590](https://pubmed.ncbi.nlm.nih.gov/26646590/) | In vitro | iASPP is a common inhibitor of RelA/p65 NF-κB and p53 |
| [33332723](https://pubmed.ncbi.nlm.nih.gov/33332723/) | Rodent cardiomyocytes | iASPP cardioprotection via Keap1–Nrf2; ↓ ROS/apoptosis |
| [37698259](https://pubmed.ncbi.nlm.nih.gov/37698259/) | Human family | Null allele p.Arg330ProfsTer76; intrafamilial variability; early deaths |
| [35933355](https://pubmed.ncbi.nlm.nih.gov/35933355/) | Human case | p.Gln194Ter nonsense → ACM; recommends PPP1R13L on ACM panels |
| [39579152](https://pubmed.ncbi.nlm.nih.gov/39579152/) | Review/case | Core triad; ~15 patients; extended phenotype (anorectal anomaly) |
| [34970070](https://pubmed.ncbi.nlm.nih.gov/34970070/) | Review | CMR-LGE as imaging gold standard for ACM/DCM |
| [42708185](https://pubmed.ncbi.nlm.nih.gov/42708185/) | ClinGen curation | PPP1R13L among curated DCM genes (2024–2025 reassessment) |
| [30453078](https://pubmed.ncbi.nlm.nih.gov/30453078/) | Human panel screen | Monoallelic missense = VUS; underscores biallelic-LoF mechanism; TP63 link |
| [42098522](https://pubmed.ncbi.nlm.nih.gov/42098522/) | Forensic | Postmortem genetic testing detects PPP1R13L in sudden death |
| [18275817](https://pubmed.ncbi.nlm.nih.gov/18275817/) | Structural | iASPP ankyrin-repeat/SH3 architecture; differential p53/p63/p73 binding |
| [35924320](https://pubmed.ncbi.nlm.nih.gov/35924320/) | Human case | Expands phenotype; inflammation on histology; variably expressed ectodermal features |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity.** Conclusions rest on ~15–20 patients and a handful of families; no registry, prevalence, incidence, penetrance, or carrier-frequency estimates exist.
2. **Oxidative-stress arm is extrapolated.** The Keap1–Nrf2 cardioprotective mechanism is shown in rodent cardiomyocytes, not directly in human PPP1R13L hearts.
3. **Genotype–phenotype correlation is unresolved.** Why ectodermal features vary so widely, and what modifies cardiac severity, is unknown.
4. **No validated QoL/natural-history instruments** and limited long-term post-transplant outcome data.
5. **Therapeutics.** IL-1 blockade reduces arrhythmia but not pump failure; no gene/cell/RNA therapy exists. No controlled trials are feasible at current patient numbers.
6. **Human cellular models** (e.g., patient iPSC-cardiomyocytes) are not yet prominent, limiting mechanistic dissection in a human genetic background.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international PPP1R13L registry** to aggregate genotype, phenotype, natural history, and transplant/mortality outcomes across centers.
2. **Patient-derived iPSC-cardiomyocyte models** to test, in human background, the relative contributions of the desmosomal, NF-κB/IL-1, and Nrf2/Keap1 arms and to screen candidate drugs.
3. **Prospective evaluation of IL-1 blockade** (and other anti-inflammatory/antioxidant agents, e.g., Nrf2 activators) with standardized arrhythmia and contractile endpoints.
4. **Deep phenotyping of ectodermal/ocular/orofacial features** with p63-pathway biomarkers to understand variable expressivity.
5. **Carrier-frequency and founder-allele mapping** in consanguineous/founder populations (e.g., Arab Christian communities) to inform screening.
6. **Preclinical gene-replacement or base-editing proof-of-concept** in Ppp1r13l-mutant mice, leveraging the recessive LoF mechanism.
7. **Advocate inclusion of PPP1R13L on all pediatric DCM/ACM gene panels** and promote postmortem genetic testing in unexplained pediatric sudden death.

---

*Evidence source legend: Human clinical (case reports/series, explants, forensic), Model organism (mouse, cattle), In vitro (cardiomyocyte, epithelial, cancer cell), Computational/structural. This report synthesizes 8 confirmed findings and 27 reviewed papers from a 5-iteration autonomous investigation.*


## Artifacts

- [OpenScientist final report](PPP1R13L-Related_Arrhythmogenic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PPP1R13L-Related_Arrhythmogenic_Cardiomyopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957795` (2 mentions) - the report calls it "MONDO"; MONDO calls it **arrhythmogenic cardiomyopathy with variable ectodermal abnormalities**
- `HP:0002216` (1 mention) - the report calls it "Woolly hair"; HP calls it **Premature graying of hair**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000746` (2 mentions) - the report calls it "cardiomyocytes"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.