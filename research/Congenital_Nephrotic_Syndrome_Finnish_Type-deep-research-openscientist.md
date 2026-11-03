---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T15:10:57.300298'
end_time: '2026-10-31T15:22:51.746790'
duration_seconds: 714.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Nephrotic Syndrome, Finnish Type
  mondo_id: MONDO:0009732
  category: Mendelian
  causal_genes: NPHS1
  omim_id: OMIM:256300
  synonyms: Finnish congenital nephrosis; congenital nephrotic syndrome - Finnish
    type; nephrotic syndrome - NPHS1 associated
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 36
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 21
  validator_version: 0.4.0
term_validation:
  total_terms: 21
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 3
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0009732
    reported_labels:
    - MONDO
    ontology_label: congenital nephrotic syndrome, Finnish type
  - term_id: HP:0003073
    reported_labels:
    - Lab abnormality
    ontology_label: Hypoalbuminemia
  - term_id: HP:0003124
    reported_labels:
    - Lab abnormality
    ontology_label: Hypercholesterolemia
  - term_id: HP:0000100
    reported_labels:
    - Composite
    ontology_label: Nephrotic syndrome
  - term_id: HP:0001622
    reported_labels:
    - Perinatal
    ontology_label: Premature birth
  - term_id: HP:0001518
    reported_labels:
    - Perinatal
    ontology_label: Small for gestational age
  - term_id: HP:0002719
    reported_labels:
    - Clinical
    ontology_label: Recurrent infections
  - term_id: HP:0001977
    reported_labels:
    - Clinical
    ontology_label: Abnormal thrombosis
  - term_id: HP:0001789
    reported_labels:
    - Prenatal
    ontology_label: Hydrops fetalis
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Nephrotic_Syndrome_Finnish_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Nephrotic_Syndrome_Finnish_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Nephrotic Syndrome, Finnish Type
- **MONDO ID:** MONDO:0009732 (if available)
- **Causal gene(s):** NPHS1
- **OMIM:** OMIM:256300
- **Synonyms:** Finnish congenital nephrosis; congenital nephrotic syndrome - Finnish type; nephrotic syndrome - NPHS1 associated
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Nephrotic Syndrome, Finnish Type** covering all of the
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

# Congenital Nephrotic Syndrome, Finnish Type (CNF) — Comprehensive Disease Characterization

**Disease:** Congenital Nephrotic Syndrome, Finnish Type (CNF / CNS-FT)
**MONDO:** MONDO:0009732 · **OMIM:** 256300 · **Causal gene:** **NPHS1** (nephrin) · **Category:** Mendelian (autosomal recessive)

---

## Summary

Congenital Nephrotic Syndrome, Finnish Type (CNF) is a severe autosomal-recessive glomerular disease caused by biallelic loss-of-function variants in **NPHS1**, the gene encoding **nephrin**. Nephrin is a 1,241-residue, immunoglobulin-superfamily transmembrane cell-adhesion protein expressed specifically in kidney glomerular podocytes, where it is the central structural and signaling component of the **slit diaphragm** — the final size- and charge-selective barrier of the glomerular filter ([PMID: 9660941](https://pubmed.ncbi.nlm.nih.gov/9660941/)). When nephrin is absent or non-functional, the slit diaphragm fails to form, the glomerular filtration barrier becomes freely permeable to protein, and the fetus/newborn develops massive, predominantly albumin, proteinuria that begins *in utero*. The resulting nephrotic syndrome — hypoalbuminemia, hypercholesterolemia, and severe edema — is clinically apparent within days of birth and progresses to end-stage kidney disease (ESKD).

The disease is defined by a striking population genetics story: in Finland two founder mutations — **Fin-major** (c.121delCT, p.Leu41fs, a 2-bp deletion in exon 2) and **Fin-minor** (p.Arg1109*, a nonsense mutation in exon 26) — account for more than 90% of disease alleles, with a Fin-major carrier frequency of roughly 1 in 59 ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/); [PMID: 10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/)). Outside Finland the disease occurs in all populations but is caused by a broad spectrum of private truncating and missense variants. Truncating/null alleles produce classic congenital disease with total nephrin loss, whereas certain "mild" missense alleles that still traffic to the membrane shift the phenotype toward later-onset, milder childhood steroid-resistant nephrotic syndrome ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).

Historically CNF was uniformly fatal within the first 6 months of life. The modern Finnish management paradigm — aggressive intravenous albumin replacement, intensive nutrition, infection/thrombosis prophylaxis, bilateral nephrectomy, peritoneal dialysis, and early kidney transplantation — has transformed CNF into a survivable condition with favorable long-term outcomes and near-normal growth and neurodevelopment ([PMID: 7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/); [PMID: 29185126](https://pubmed.ncbi.nlm.nih.gov/29185126/)). A distinctive post-transplant complication — recurrent nephrotic-range proteinuria driven by **anti-nephrin autoantibodies** arising almost exclusively in Fin-major homozygotes who have never expressed nephrin (nephrin is a neoantigen to their immune system) — is managed by plasma exchange plus B-cell/plasma-cell–directed immunotherapy ([PMID: 11549850](https://pubmed.ncbi.nlm.nih.gov/11549850/); [PMID: 24682440](https://pubmed.ncbi.nlm.nih.gov/24682440/)). Kidney transplantation remains the only cure, but AAV-mediated podocyte gene replacement and pharmacological-chaperone rescue of trafficking-defective missense mutants are in preclinical development.

---

## Section 1 — Disease Information

CNF is a rare Mendelian **congenital nephrotic syndrome** — nephrotic syndrome with onset in the first 3 months of life (congenital by definition if ≤3 months) — caused by biallelic NPHS1/nephrin defects. It is the prototypical and most common genetic cause of congenital nephrotic syndrome.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009732 |
| OMIM | 256300 |
| Gene / OMIM gene | NPHS1 (OMIM *602716); HGNC:7908 |
| UniProt (nephrin) | O60500 |
| Orphanet | ORPHA:839 (Congenital nephrotic syndrome, Finnish type) |
| ICD-10 | N04 (nephrotic syndrome); congenital subtype P96.8 contexts |
| ICD-11 | GB41 (nephrotic syndrome) |
| MeSH | Nephrotic Syndrome; Congenital |

**Synonyms:** Congenital nephrotic syndrome of the Finnish type (CNF / CNS-FT); Finnish congenital nephrosis; nephrosis 1, congenital, Finnish type; NPHS1-associated nephrotic syndrome.

**Information source:** The knowledge base here is derived from aggregated disease-level resources (OMIM, Orphanet) combined with primary clinical literature — national/registry cohorts (e.g., the Finnish and French CNS cohorts), case series, and molecular/functional studies — rather than individual EHR data.

---

## Section 2 — Etiology

**Primary cause (genetic):** Biallelic (homozygous or compound-heterozygous) loss-of-function variants in **NPHS1** (chromosome 19q13.1, 29 exons), encoding nephrin. CNF is a monogenic, autosomal-recessive disease; there is no environmental or infectious cause of true CNF. Nephrin loss abolishes the slit diaphragm ([PMID: 9660941](https://pubmed.ncbi.nlm.nih.gov/9660941/); [PMID: 10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/)).

**Genetic risk factors:** The only "risk factor" is inheritance of two pathogenic NPHS1 alleles. In Finland the dominant risk allele is the Fin-major founder mutation (carrier frequency ~1:59) ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/)). Consanguinity and founder-population membership increase carrier-to-carrier mating probability. Modifier context: a single "mild" missense allele in a compound-heterozygous genotype shifts disease toward a later/milder phenotype ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).

**Environmental / lifestyle risk factors:** None established for causation. CNF is fully genetically determined. (Note: congenital infections — the TORCH group, congenital syphilis, CMV, toxoplasmosis — cause a *secondary* congenital nephrotic *phenocopy* that must be distinguished from genetic CNF; these are mimics, not causes of NPHS1 disease.)

**Protective factors:** No genetic or environmental protective factors are established. Within the disease, retained partial nephrin function (hypomorphic missense alleles that still traffic to the membrane and retain homo-/heterodimerization) confers a milder, later-onset course — the closest analog to a protective modifier ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).

**Gene–environment interactions:** Not applicable in the classic sense. The clinically most important "gene×environment/immune" interaction is iatrogenic: in Fin-major homozygotes who have never expressed nephrin, transplantation of a nephrin-expressing kidney introduces nephrin as a **neoantigen**, triggering anti-nephrin autoantibodies and recurrent disease ([PMID: 11549850](https://pubmed.ncbi.nlm.nih.gov/11549850/)).

---

## Section 3 — Phenotypes

CNF presents with the full nephrotic tetrad of **intrauterine onset**, detectable within days of birth regardless of genotype, plus characteristic perinatal features ([PMID: 35260424](https://pubmed.ncbi.nlm.nih.gov/35260424/); [PMID: 11910513](https://pubmed.ncbi.nlm.nih.gov/11910513/)).

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Massive proteinuria (≈90% albumin) | Lab abnormality | HP:0000093 (Proteinuria) | Intrauterine onset; severe; ~100% |
| Hypoalbuminemia / hypoproteinemia | Lab abnormality | HP:0003073 | Neonatal; severe; ~100% |
| Hypercholesterolemia / dyslipidemia | Lab abnormality | HP:0003124 | Neonatal; moderate–severe; frequent |
| Generalized edema / anasarca | Clinical sign | HP:0000969 (Edema) | Neonatal; severe; very frequent |
| Nephrotic syndrome | Composite | HP:0000100 | Congenital (≤days of life); ~100% |
| Prematurity | Perinatal | HP:0001622 | Common |
| Low birth weight / small-for-gestational-age | Perinatal | HP:0001518 | Common |
| Large edematous placenta (>25% of birth weight), hydropic villi | Perinatal/placental | — | Characteristic; frequent |
| Progression to end-stage kidney disease | Clinical course | HP:0003774 (Stage 5 CKD) | Infancy–early childhood; ~universal untreated |
| Increased susceptibility to infection (urinary Ig loss) | Clinical | HP:0002719 | Severe; frequent complication |
| Thrombosis / thromboembolism (antithrombin loss) | Clinical | HP:0001977 | Severe; frequent complication |
| Fetal hydrops | Prenatal | HP:0001789 | Occasional in utero presentation |
| Elevated maternal/amniotic alpha-fetoprotein | Prenatal lab | — | Characteristic prenatal marker |

**Progression:** Proteinuria is present and massive from birth, severe and progressive; without replacement therapy the nephrotic state is relentless. **Quality-of-life impact:** Profound in infancy — chronic edema, feeding/nutrition burden, repeated hospitalizations, infection and thrombosis risk, dialysis, and transplantation. Post-transplant, QoL and development improve substantially, with favorable neurodevelopment and catch-up growth reported in transplanted cohorts ([PMID: 29185126](https://pubmed.ncbi.nlm.nih.gov/29185126/)).

---

## Section 4 — Genetic / Molecular Information

**Causal gene:** **NPHS1** (19q13.1; HGNC:7908; OMIM *602716), 29 exons, encoding **nephrin** (UniProt O60500; 1,241 aa). Nephrin was identified by positional cloning as the first slit-diaphragm protein and is specifically expressed in glomerular podocytes ([PMID: 9660941](https://pubmed.ncbi.nlm.nih.gov/9660941/)).

**Variant spectrum and classification:**

| Allele | Variant type | Nomenclature | Notes |
|---|---|---|---|
| **Fin-major** | Frameshift (2-bp deletion, exon 2) | c.121delCT, p.Leu41fs | Pathogenic; null; >90% of Finnish alleles; total nephrin absence |
| **Fin-minor** | Nonsense (exon 26) | p.Arg1109* (R1109X) | Pathogenic; null; second Finnish founder allele |
| Non-Finnish truncating | Nonsense/frameshift/splice | e.g., c.2335-1G>A (splice) | Pathogenic; classic congenital disease |
| "Mild" missense | Missense | e.g., E725D and others | Hypomorphic; trafficking-competent variants cause later-onset milder disease |

- **ClinVar/ACMG classification:** Fin-major and Fin-minor and other truncating alleles are classified **pathogenic**; many missense alleles are pathogenic/likely-pathogenic, with a subset of VUS requiring functional validation.
- **Allele frequency:** Pathogenic NPHS1 alleles are rare in gnomAD globally; Fin-major is enriched in Finland (founder effect, carrier ~1:59) ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/)).
- **Origin:** Germline only. No somatic contribution.
- **Functional consequence:** Predominantly **loss of function**. Truncating alleles → no nephrin protein → no slit diaphragm ([PMID: 10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/)). Many missense alleles cause **ER retention / trafficking defects**; but some missense variants traffic normally and retain nephrin homodimerization and NEPH1 (KIRREL1) heterodimerization, explaining a milder course ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).

**Genotype–phenotype correlation:** Compound-heterozygous NPHS1 genotypes were associated with more severe proteinuria in a congenital/infantile cohort ([PMID: 41339767](https://pubmed.ncbi.nlm.nih.gov/41339767/)); presence of at least one "mild" allele predicts later onset and milder disease ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).

**Modifier genes:** Other slit-diaphragm genes (NPHS2/podocin, KIRREL1/NEPH1, CD2AP, TRPC6) can modify podocyte function and cause overlapping phenotypes; formal digenic modifier effects for CNF are not firmly established. **Epigenetic / chromosomal:** No recurrent epigenetic mechanism or large chromosomal abnormality is characteristic; rare copy-number deletions affect related SRNS genes (PLCE1, NPHS2) but are uncommon in NPHS1 disease ([PMID: 37670083](https://pubmed.ncbi.nlm.nih.gov/37670083/)).

---

## Section 5 — Environmental Information

CNF is a purely genetic Mendelian disease with **no established environmental, lifestyle, toxic, or infectious cause**.

- **Environmental / lifestyle factors:** None causal.
- **Infectious agents:** Not causal of NPHS1 CNF. Importantly, **congenital infections (TORCH: toxoplasma, rubella, CMV, HSV; congenital syphilis)** produce a *secondary* congenital nephrotic syndrome that phenocopies CNF and must be excluded diagnostically. Co-occurrence of TORCH seropositivity with a genuine NPHS1 variant has been reported, underscoring the need for genetic confirmation.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic NPHS1 loss-of-function mutation** (e.g., Fin-major frameshift / Fin-minor nonsense) → **leads to** absent or non-functional nephrin protein in podocytes (demonstrated: nephrin not expressed in Fin-major/Fin-minor kidneys; ZO-1 preserved) ([PMID: 10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/)).
2. Absent/non-functional nephrin → **results in** failure to assemble the **slit diaphragm**, the zipper-like interpodocyte junction that nephrin ectodomains form (demonstrated: slit diaphragms missing).
3. Loss of the slit diaphragm → **leads to** loss of nephrin→Fyn→Nck→actin signaling and consequent **podocyte foot-process effacement** and cytoskeletal disorganization (mechanism demonstrated in vitro and in podocyte models; inferred in human CNF) ([PMID: 16543952](https://pubmed.ncbi.nlm.nih.gov/16543952/); [PMID: 23188823](https://pubmed.ncbi.nlm.nih.gov/23188823/)).
4. Breached filtration barrier → **results in** massive, predominantly **albumin**, proteinuria beginning *in utero* (~90% of urinary protein is albumin) ([PMID: 7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/)).
5. Urinary protein loss → **leads to** **hypoalbuminemia** → reduced plasma oncotic pressure → **edema/anasarca**; and compensatory hepatic lipoprotein synthesis → **hypercholesterolemia** ([PMID: 35260424](https://pubmed.ncbi.nlm.nih.gov/35260424/)).
6. Branch — urinary loss of specific proteins:
   - Loss of immunoglobulins → **leads to** increased **infection/sepsis** risk;
   - Loss of antithrombin + hemoconcentration → **leads to** **thrombosis** ([PMID: 29185126](https://pubmed.ncbi.nlm.nih.gov/29185126/)).
7. Ongoing glomerular injury → **results in** progressive nephron loss and **end-stage kidney disease** in infancy/early childhood ([PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/)).
8. Iatrogenic branch — in Fin-major homozygotes (lifelong nephrin-null), kidney transplantation reintroduces nephrin → **immune system recognizes nephrin as a neoantigen** → **anti-nephrin autoantibodies** → recurrent nephrotic-range proteinuria in ~20–25% ([PMID: 11549850](https://pubmed.ncbi.nlm.nih.gov/11549850/); [PMID: 24682440](https://pubmed.ncbi.nlm.nih.gov/24682440/)).

### Mechanistic detail

**Molecular pathway (nephrin signaling hub):** Nephrin is not merely structural. Engagement of the nephrin ectodomain induces transient **Fyn** (Src-family kinase) activity that phosphorylates specific cytoplasmic-tail tyrosines, recruiting the **Nck** (SH2/SH3) adaptor and driving **Nck-dependent actin polymerization**; Nck in turn promotes further Fyn-dependent nephrin phosphorylation ([PMID: 16543952](https://pubmed.ncbi.nlm.nih.gov/16543952/); [PMID: 23188823](https://pubmed.ncbi.nlm.nih.gov/23188823/)). Phosphorylation of the Nck-binding sites falls during podocyte injury, linking nephrin signaling loss to cytoskeletal collapse. Relevant GO/pathway terms: regulation of actin cytoskeleton, Src/Fyn tyrosine kinase signaling.

**Protein dysfunction:** Nephrin has eight **Ig-like C2 domains** + one **fibronectin type-III domain** extracellularly, a single transmembrane segment, and an intrinsically unstructured, conserved cytoplasmic signaling tail; it partners with KIRREL1/NEPH1, podocin (NPHS2), CD2AP and TRPC6 at the slit diaphragm ([PMID: 34288970](https://pubmed.ncbi.nlm.nih.gov/34288970/)). Truncating alleles → null protein; many missense → misfolding and ER retention; some missense retain folding/dimerization and traffic normally ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).

**Cell type / biological process:** Primary injured cell is the **glomerular visceral epithelial cell (podocyte)** — CL:0000653. Core biological processes (GO): glomerular filtration (GO:0003094), slit diaphragm assembly, actin cytoskeleton organization (GO:0030036), cell–cell adhesion.

**Immune involvement:** No primary autoimmunity in genetic CNF. Secondary humoral immunity is central only to post-transplant recurrence via anti-nephrin autoantibodies. This mechanism mirrors the broader, newly recognized role of **anti-nephrin autoantibodies** in acquired podocytopathies (minimal change disease, FSGS), where antibody binding induces nephrin phosphorylation, endocytosis, and cytoskeletal change ([PMID: 42959077](https://pubmed.ncbi.nlm.nih.gov/42959077/); [PMID: 41746488](https://pubmed.ncbi.nlm.nih.gov/41746488/)).

**Subcellular compartments (GO CC):** plasma membrane / slit diaphragm (GO:0036056, filtration diaphragm), cell–cell junction; for trafficking-defective mutants, endoplasmic reticulum retention.

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** Kidney (UBERON:0002113), specifically the **renal glomerulus** (UBERON:0000074) and its **glomerular filtration barrier**.
- **Primary cell:** **Podocyte** / glomerular visceral epithelial cell (CL:0000653), and its specialized **slit diaphragm** between foot processes.
- **Tissue type:** Glomerular epithelium (visceral epithelial cells); proximal tubular epithelium secondarily, showing microcystic dilatation ("microcysts") on histology.
- **Secondary/systemic involvement (body systems):** Cardiovascular/hematologic (edema, thrombosis, hemoconcentration), immune (hypogammaglobulinemia → infection), metabolic/endocrine (hyperlipidemia, growth failure, hypothyroidism from urinary thyroxine-binding globulin loss), and nutritional. The **placenta** is characteristically enlarged (>25% of birth weight) with hydropic villi ([PMID: 11910513](https://pubmed.ncbi.nlm.nih.gov/11910513/)).
- **Subcellular (GO CC):** slit diaphragm / plasma membrane (GO:0036056); ER (trafficking-defective mutants).
- **Lateralization:** Bilateral and diffuse (both kidneys, all glomeruli).

---

## Section 8 — Temporal Development

- **Onset:** **Congenital** — proteinuria begins *in utero*; clinically detectable within the first days of life regardless of genotype; may present prenatally as fetal hydrops and raised maternal/amniotic AFP ([PMID: 35260424](https://pubmed.ncbi.nlm.nih.gov/35260424/)).
- **Onset pattern:** Chronic, congenital, relentlessly progressive from birth.
- **Progression / stages:** Nephrotic from birth → progressive renal insufficiency → **ESKD**. In the French cohort, 39 patients reached ESKD at a **median age of 11 months**; renal survival was 64% at 1 year and 45% at 2 years ([PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/)).
- **Course:** Progressive, lifelong, not self-limiting. No spontaneous remission of genetic CNF (rare milder missense cases may run a slower course).
- **Critical intervention windows:** Prenatal diagnosis window (AFP + NPHS1 molecular testing); neonatal period for albumin/nutrition support; infancy/early childhood for nephrectomy–dialysis–transplant sequencing.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal recessive**; complete penetrance for biallelic null genotypes ([PMID: 9660941](https://pubmed.ncbi.nlm.nih.gov/9660941/)).
- **Penetrance / expressivity:** Essentially complete penetrance; expressivity variable depending on allele severity (null vs mild missense) ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/)).
- **Founder effect:** Classic Finnish founder population — Fin-major and Fin-minor account for >90% of Finnish disease alleles ([PMID: 10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/)).
- **Carrier frequency:** Fin-major **1:59** (95% CI 1:89–1:44); Fin-minor **1:2004** in Finland ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/)).
- **Consanguinity:** Increases risk in non-founder populations (homozygosity for private alleles).
- **Epidemiology:** Historically ~1 in 8,000–10,000 births in Finland. Outside Finland the estimated **cumulative incidence was 0.5/100,000 live births** (French nationwide cohort) ([PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/)).
- **Geographic distribution:** Highest in Finland; occurs worldwide in all populations, caused by diverse non-founder variants (e.g., no Finnish mutations in Italian CNF patients, who carried 13 distinct mutations) ([PMID: 12495287](https://pubmed.ncbi.nlm.nih.gov/12495287/)).
- **Sex ratio:** Approximately equal (autosomal recessive). **Age distribution:** Neonates/infants.
- **Genetic anticipation / germline mosaicism:** Not features of this non-repeat, recessive disease.

---

## Section 10 — Diagnostics

**Clinical/laboratory:** Heavy proteinuria and hypoalbuminemia detectable at/near birth; hypercholesterolemia; low IgG; low antithrombin. Prenatally, elevated **maternal serum and amniotic-fluid alpha-fetoprotein (AFP)** with normal ultrasound and karyotype is suggestive but **not specific** — affected homozygotes and heterozygous carriers can both show raised AFP and proteinuric fetal kidneys, so **NPHS1 mutation analysis is required for confirmation** ([PMID: 12047969](https://pubmed.ncbi.nlm.nih.gov/12047969/); [PMID: 9172059](https://pubmed.ncbi.nlm.nih.gov/9172059/)).

**Biopsy / pathology:** Light microscopy shows minimal-change-like glomeruli with characteristic **proximal tubular microcystic dilatation**; electron microscopy shows podocyte **foot-process effacement** and absent slit diaphragms; **immunohistochemistry shows absent nephrin with preserved ZO-1** ([PMID: 10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/)). Placental examination shows a large placenta with hydropic villi ([PMID: 11910513](https://pubmed.ncbi.nlm.nih.gov/11910513/)).

**Genetic testing (confirmatory and definitive):** Targeted NPHS1 single-gene testing (including founder-allele assays — RFLP/dual-color oligonucleotide ligation for Fin-major/Fin-minor) in Finnish-ancestry patients ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/)); otherwise a **congenital/steroid-resistant nephrotic syndrome gene panel** or **whole-exome sequencing** covering NPHS1, NPHS2, WT1, LAMB2, PLCE1. In the French cohort, biallelic NPHS1 explained 65% of non-infectious CNS ([PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/)); pooled NPHS1 mutation prevalence in CNS/SRNS is ~15% ([PMID: 39596340](https://pubmed.ncbi.nlm.nih.gov/39596340/)). CMA/CNV analysis is a second-line adjunct (rare deletions) ([PMID: 37670083](https://pubmed.ncbi.nlm.nih.gov/37670083/)).

**Differential diagnosis:** Other genetic CNS — **NPHS2** (podocin, later SRNS), **WT1** (Denys-Drash/Frasier), **LAMB2** (Pierson), **PLCE1**; and **secondary CNS** from congenital infections (TORCH, syphilis). Key distinguishers: onset timing, extrarenal features (WT1 → genital/Wilms; LAMB2 → ocular), and absent-nephrin IHC in NPHS1 ([PMID: 18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/); [PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/)).

**Screening:** Prenatal AFP + NPHS1 molecular testing in at-risk pregnancies; carrier/cascade screening in founder populations; haplotype/mutation-based prenatal diagnosis is well established ([PMID: 9067923](https://pubmed.ncbi.nlm.nih.gov/9067923/)).

---

## Section 11 — Outcome / Prognosis

- **Untreated natural history:** Historically **uniformly fatal, usually within the first 6 months of life** ([PMID: 7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/)).
- **With modern management:** Survivable with favorable outcomes. ESKD reached at median 11 months; renal survival 64% (1 yr) / 45% (2 yr) in the French cohort ([PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/)).
- **Post-transplant (Japanese cohort, n=14):** Dialysis started at 2.4 ± 1.3 yr, transplant at 5.2 ± 2.0 yr, mean follow-up 14.3 ± 8.9 yr; **satisfactory graft survival, improved height SD score, favorable neurodevelopment**, mean eGFR 57.3 ± 16.5 mL/min/1.73 m² at last observation; 2/14 had recurrent proteinuria ([PMID: 29185126](https://pubmed.ncbi.nlm.nih.gov/29185126/)).
- **Morbidity / complications:** Severe edema, **sepsis**, and **thrombosis** before transplant (urinary loss of immunoglobulins and antithrombin, hemoconcentration); invasive infection rate **2.41/patient/year** in the French cohort ([PMID: 29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/); [PMID: 29185126](https://pubmed.ncbi.nlm.nih.gov/29185126/)).
- **Prognostic factors:** Genotype (NPHS1 biallelic associated with longer renal and patient survival than other genotypes); allele severity (null vs mild missense); Fin-major homozygosity predicts post-transplant recurrence risk; rising anti-nephrin antibody titer predicts/accompanies recurrence ([PMID: 24682440](https://pubmed.ncbi.nlm.nih.gov/24682440/)).

---

## Section 12 — Treatment

CNF has **no causal cure except kidney transplantation**; management is supportive until transplant.

**Supportive medical management (the Finnish protocol):** Early **intravenous albumin** replacement (NCIT: Albumin), intensive **nutritional support**, aggressive treatment of infections and thrombosis, and correction of protein/lipid/thyroid deficits ([PMID: 7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/)). ACE inhibitors/indomethacin are sometimes used to reduce proteinuria. Thyroxine supplementation and anticoagulation as needed.

**Surgical / interventional:** **Bilateral nephrectomy** followed by **peritoneal dialysis**, then **kidney transplantation** — the standard of care when medical management fails ([PMID: 9510361](https://pubmed.ncbi.nlm.nih.gov/9510361/); [PMID: 7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/)). NCIT: Nephrectomy; Kidney Transplantation; Peritoneal Dialysis.

**Treatment of post-transplant recurrence:** In Fin-major homozygotes developing anti-nephrin-mediated recurrence, **plasma exchange** combined with **cyclophosphamide** and **anti-CD20 (rituximab)** B-cell depletion is effective ([PMID: 17519780](https://pubmed.ncbi.nlm.nih.gov/17519780/); [PMID: 21672106](https://pubmed.ncbi.nlm.nih.gov/21672106/); [PMID: 24682440](https://pubmed.ncbi.nlm.nih.gov/24682440/)). Emerging combined B-cell (CD20) + plasma-cell (CD38) targeting (e.g., obinutuzumab + daratumumab; "New Gaslini protocol") is proposed for refractory humoral podocytopathy ([PMID: 42959077](https://pubmed.ncbi.nlm.nih.gov/42959077/)). NCIT: Rituximab; Cyclophosphamide; Plasmapheresis.

**Experimental / curative pipeline:** (1) **AAV-mediated podocyte-targeted gene replacement** — capsid engineering plus podocyte-specific promoters; constitutive/conditional Nphs1-knockout mice established as substrates ([PMID: 38987283](https://pubmed.ncbi.nlm.nih.gov/38987283/); [PMID: 41788620](https://pubmed.ncbi.nlm.nih.gov/41788620/)). (2) **Pharmacological chaperones** for trafficking-defective missense mutants — a nanoluciferase (HiBiT) high-throughput screen identified 10 compounds that promote cell-surface expression of the nephrin E725D mutant ([PMID: 41241432](https://pubmed.ncbi.nlm.nih.gov/41241432/)). Challenges: vector immunogenicity, biodistribution, and genetic heterogeneity.

**Pharmacogenomics:** Not a defining feature; standard transplant immunosuppression pharmacogenetics apply.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible for a Mendelian recessive disease; genetic risk reduction only via reproductive counseling.
- **Genetic counseling:** 25% recurrence risk for carrier couples; counseling essential, especially in founder populations and consanguineous families ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/)).
- **Carrier / cascade screening:** Feasible in Finland via founder-allele assays (Fin-major/Fin-minor) ([PMID: 10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/)).
- **Prenatal diagnosis:** AFP (maternal serum/amniotic) plus definitive **NPHS1 mutation/haplotype analysis**; in utero fetal kidney biopsy has been used historically ([PMID: 9067923](https://pubmed.ncbi.nlm.nih.gov/9067923/); [PMID: 12047969](https://pubmed.ncbi.nlm.nih.gov/12047969/); [PMID: 11288113](https://pubmed.ncbi.nlm.nih.gov/11288113/)). Preimplantation genetic diagnosis is an option for known-mutation families.
- **Secondary/tertiary prevention:** Early albumin/nutrition support, infection and thrombosis prophylaxis, and timely nephrectomy–dialysis–transplant to prevent complications ([PMID: 7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/)).
- **Immunization / public-health / environmental interventions:** Not applicable to disease causation (routine vaccination is standard supportive care given infection risk).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** Nephrin is evolutionarily conserved from nematodes to higher vertebrates. Orthologs: mouse *Nphs1* (NCBI Gene 54631), and functional orthologs in *Drosophila* (**Sns**, with NEPH1 ortholog **Kirre/Duf**), *Xenopus*, and zebrafish ([PMID: 34288970](https://pubmed.ncbi.nlm.nih.gov/34288970/); [PMID: 19515699](https://pubmed.ncbi.nlm.nih.gov/19515699/); [PMID: 15895368](https://pubmed.ncbi.nlm.nih.gov/15895368/)).
- **Comparative biology:** Invertebrate orthologs are Ig-3-domain-rich, whereas vertebrates acquired CD80-like C2-set domains; intrinsically unstructured cytoplasmic regions are conserved and functionally important ([PMID: 34288970](https://pubmed.ncbi.nlm.nih.gov/34288970/)). In *Drosophila*, Sns/Kirre direct formation of a slit-diaphragm-like **nephrocyte diaphragm** essential for size-selective hemolymph filtration ([PMID: 19515699](https://pubmed.ncbi.nlm.nih.gov/19515699/)).
- **Natural disease in companion animals / zoonosis:** No major naturally occurring NPHS1 CNF analog is prominently documented; not zoonotic.

---

## Section 15 — Model Organisms

| Model | Type | Key phenotype / use | Reference |
|---|---|---|---|
| **Nphs1-knockout mouse** (129/Sv-Nphs1) | Mammalian, constitutive KO | Median survival to postnatal day **P5** (vs 90–100% in het/WT at P50); proteinuria (↑ albumin/creatinine); renal-tubular **microcysts** (P<0.0022); reduced foot-process density by TEM (P<0.0001) | [PMID: 39003671](https://pubmed.ncbi.nlm.nih.gov/39003671/); [PMID: 38987283](https://pubmed.ncbi.nlm.nih.gov/38987283/) |
| Conditional/constitutive Nphs1-KO mice | Mammalian | Substrate for **NPHS1 gene-replacement therapy** development | [PMID: 38987283](https://pubmed.ncbi.nlm.nih.gov/38987283/); [PMID: 41788620](https://pubmed.ncbi.nlm.nih.gov/41788620/) |
| **Drosophila nephrocyte** (Sns/Kirre) | Invertebrate | Slit-diaphragm-like nephrocyte diaphragm; knockdown reduces diaphragms and impairs size-selective uptake; **humanized assay** (transgenic human nephrin) validates NPHS1 variant pathogenicity | [PMID: 19515699](https://pubmed.ncbi.nlm.nih.gov/19515699/); [PMID: 40543925](https://pubmed.ncbi.nlm.nih.gov/40543925/) |
| **Xenopus** / zebrafish | Lower vertebrate | Nephrin ortholog expressed specifically in pronephric glomus/glomerulus; developmental/filtration studies | [PMID: 15895368](https://pubmed.ncbi.nlm.nih.gov/15895368/) |
| Patient iPSCs / podocyte organoids | Cellular/in vitro | Variant functional validation, trafficking assays, drug screening | [PMID: 41241432](https://pubmed.ncbi.nlm.nih.gov/41241432/) |

**Phenotype recapitulation:** The mouse KO faithfully reproduces massive proteinuria, foot-process effacement, tubular microcysts, and perinatal lethality — closely mirroring human CNF. **Limitations:** Perinatal lethality constrains long-term and therapeutic studies; mouse does not model the Fin-major-specific human post-transplant anti-nephrin autoimmunity; invertebrate nephrocytes model the filtration structure but not whole-organ disease.

---

## Mechanistic Model / Interpretation

```
 NPHS1 biallelic LOF (Fin-major c.121delCT / Fin-minor R1109X / other null/missense)
            │
            ▼
 Absent or non-functional NEPHRIN protein in podocytes  ──(missense)──► ER retention / mistrafficking
            │                                                           (some "mild" missense traffic OK → milder/later disease)
            ▼
 Failure of SLIT DIAPHRAGM assembly (nephrin zipper missing; ZO-1 preserved)
            │
            ├──► Loss of nephrin→Fyn→Nck→actin signaling → foot-process effacement
            ▼
 Breached glomerular filtration barrier
            │
            ▼
 Massive proteinuria (~90% albumin), intrauterine onset  ──► large hydropic placenta; ↑ AFP
            │
            ├──► Hypoalbuminemia → ↓ oncotic pressure → EDEMA / ANASARCA
            ├──► Compensatory hepatic lipoprotein synthesis → HYPERCHOLESTEROLEMIA
            ├──► Urinary IgG loss → INFECTION / SEPSIS
            ├──► Urinary antithrombin loss + hemoconcentration → THROMBOSIS
            ▼
 Progressive nephron loss → END-STAGE KIDNEY DISEASE (median ~11 months)
            │
            ▼  [management: albumin + nutrition → bilateral nephrectomy → PD → transplant]
 Kidney transplant (CURE)
            │
            └──(Fin-major homozygotes only; nephrin = neoantigen)──►
                 ANTI-NEPHRIN AUTOANTIBODIES → recurrent proteinuria (~20–25%)
                 → Rx: plasma exchange + cyclophosphamide + rituximab (anti-CD20)
```

**Upstream vs downstream:** The mutation and nephrin loss are the apical cause; slit-diaphragm failure and signaling loss are proximate mechanisms; proteinuria and its systemic sequelae are downstream; ESKD is terminal; anti-nephrin autoimmunity is a distinct iatrogenic downstream branch unique to nephrin-null patients.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [9660941](https://pubmed.ncbi.nlm.nih.gov/9660941/) | Landmark positional cloning: NPHS1 → nephrin, 1241-aa Ig-family adhesion protein, glomerulus-specific (F001, F012) |
| [10972661](https://pubmed.ncbi.nlm.nih.gov/10972661/) | Founder mutations >90% of Finnish cases; nephrin absent in patient kidneys, ZO-1 preserved (F001, F002) |
| [10839769](https://pubmed.ncbi.nlm.nih.gov/10839769/) | Carrier frequencies: Fin-major 1:59, Fin-minor 1:2004 (F002) |
| [11549850](https://pubmed.ncbi.nlm.nih.gov/11549850/) | Transplantation introduces nephrin neoantigen → pathogenic autoantibodies (F003) |
| [24682440](https://pubmed.ncbi.nlm.nih.gov/24682440/) | Anti-nephrin antibodies cause recurrence; PE + cyclophosphamide + anti-CD20 therapy (F003) |
| [17519780](https://pubmed.ncbi.nlm.nih.gov/17519780/); [21672106](https://pubmed.ncbi.nlm.nih.gov/21672106/) | Plasma exchange and rituximab in recurrent NS (Section 12) |
| [29474669](https://pubmed.ncbi.nlm.nih.gov/29474669/) | French cohort: incidence 0.5/100,000; NPHS1 65%; ESKD median 11 mo; infection rate 2.41/pt/yr (F004, F011) |
| [16543952](https://pubmed.ncbi.nlm.nih.gov/16543952/); [23188823](https://pubmed.ncbi.nlm.nih.gov/23188823/) | Nephrin–Fyn–Nck–actin signaling axis; phosphorylation falls during injury (F005) |
| [39003671](https://pubmed.ncbi.nlm.nih.gov/39003671/); [38987283](https://pubmed.ncbi.nlm.nih.gov/38987283/) | Nphs1-KO mouse quantitative phenotype; GRT substrate (F006) |
| [7742232](https://pubmed.ncbi.nlm.nih.gov/7742232/) | Historical fatality + modern Finnish management paradigm (F007) |
| [35260424](https://pubmed.ncbi.nlm.nih.gov/35260424/); [11910513](https://pubmed.ncbi.nlm.nih.gov/11910513/) | Cardinal clinical features; placental hydropic villi (F008) |
| [18614772](https://pubmed.ncbi.nlm.nih.gov/18614772/) | Mild missense alleles traffic normally → later-onset milder disease; NPHS1 vs NPHS2 differential (F009, F011) |
| [41339767](https://pubmed.ncbi.nlm.nih.gov/41339767/) | Compound-het NPHS1 → more severe proteinuria (F009) |
| [41241432](https://pubmed.ncbi.nlm.nih.gov/41241432/); [41788620](https://pubmed.ncbi.nlm.nih.gov/41788620/) | Pharmacological chaperone screen; AAV/CRISPR gene therapy strategies (F010) |
| [34288970](https://pubmed.ncbi.nlm.nih.gov/34288970/) | Nephrin Ig-domain architecture and evolutionary conservation (F012) |
| [19515699](https://pubmed.ncbi.nlm.nih.gov/19515699/); [40543925](https://pubmed.ncbi.nlm.nih.gov/40543925/) | Drosophila Sns/Kirre nephrocyte model; humanized variant assay (F013) |
| [29185126](https://pubmed.ncbi.nlm.nih.gov/29185126/) | Japanese transplant cohort: complications + favorable long-term outcome (F014) |
| [12047969](https://pubmed.ncbi.nlm.nih.gov/12047969/); [9172059](https://pubmed.ncbi.nlm.nih.gov/9172059/); [9067923](https://pubmed.ncbi.nlm.nih.gov/9067923/) | Prenatal AFP non-specificity → need for NPHS1 molecular diagnosis (Section 10/13) |
| [12495287](https://pubmed.ncbi.nlm.nih.gov/12495287/) | Non-Finnish (Italian) patients carry diverse private mutations (Section 9) |
| [39596340](https://pubmed.ncbi.nlm.nih.gov/39596340/); [37670083](https://pubmed.ncbi.nlm.nih.gov/37670083/) | NPHS1/NPHS2 mutation prevalence; rare CNVs in SRNS genes (Section 4/10) |
| [42959077](https://pubmed.ncbi.nlm.nih.gov/42959077/); [41746488](https://pubmed.ncbi.nlm.nih.gov/41746488/) | Anti-nephrin autoantibodies in podocytopathies; B/plasma-cell targeting (Section 6/12) |

**Evidence source types:** Human clinical (national/registry cohorts, case series, prenatal studies), molecular/functional in vitro (signaling, trafficking, chaperone screens), and model organism (mouse KO, Drosophila, Xenopus/zebrafish).

---

## Limitations and Knowledge Gaps

- **No disease-specific omics in hand:** This report synthesizes literature; no primary transcriptomic/proteomic/metabolomic dataset for CNF was analyzed. Patient-level single-cell/spatial podocyte profiling of CNF kidneys remains sparse.
- **Modifier genetics underdetermined:** Formal modifier loci explaining expressivity (beyond allele severity) are not established.
- **Post-transplant autoimmunity mechanism incomplete:** Why only Fin-major homozygotes (total nephrin absence) reliably mount pathogenic anti-nephrin responses — and the precise epitopes — is not fully resolved; Palb (permeability) factors may also contribute ([PMID: 16518627](https://pubmed.ncbi.nlm.nih.gov/16518627/)).
- **Therapeutics preclinical:** Gene replacement and pharmacological chaperones remain preclinical; no human efficacy data; vector immunogenicity, biodistribution, and genotype heterogeneity are unsolved.
- **Quantitative natural-history outside registries:** Life-expectancy and QoL metrics derive from limited cohorts (France, Japan, Finland); global generalizability is uncertain.

---

## Proposed Follow-up Experiments / Actions

1. **Variant-function pipeline:** Systematically classify NPHS1 VUS using the humanized *Drosophila* nephrocyte assay ([PMID: 40543925](https://pubmed.ncbi.nlm.nih.gov/40543925/)) and nanoluciferase trafficking screens ([PMID: 41241432](https://pubmed.ncbi.nlm.nih.gov/41241432/)) to separate null, trafficking-defective, and functional-but-mild alleles — directly informing prognosis and chaperone candidacy.
2. **AAV gene-replacement proof-of-concept in Nphs1-KO mice:** Deliver podocyte-promoter-driven NPHS1 to the established 129/Sv-Nphs1 KO ([PMID: 38987283](https://pubmed.ncbi.nlm.nih.gov/38987283/)) and quantify rescue of proteinuria, foot-process density, and survival; optimize capsid to overcome glomerular biodistribution limits.
3. **Pharmacological-chaperone validation:** Advance the 10 hit compounds rescuing nephrin E725D ([PMID: 41241432](https://pubmed.ncbi.nlm.nih.gov/41241432/)) through podocyte and iPSC-organoid secondary assays and in vivo testing in a knock-in missense mouse.
4. **Predictive biomarker for recurrence:** Prospectively validate standardized quantitative **anti-nephrin IgG** assays (CLIA/ELISA) to stratify Fin-major homozygotes before transplant and monitor recurrence risk ([PMID: 42767610](https://pubmed.ncbi.nlm.nih.gov/42767610/)).
5. **Deep podocyte profiling of CNF kidneys:** Apply single-cell/single-nucleus RNA-seq and spatial transcriptomics to nephrectomy specimens to define the downstream podocyte injury program and candidate adjunct targets.
6. **Prospective international natural-history and QoL registry:** Standardize outcome capture (growth, neurodevelopment, infection, thrombosis, graft survival, EQ-5D/PedsQL) across centers to refine prognosis.

---

*Report compiled from 14 confirmed findings and 56 reviewed papers over a 5-iteration investigation. Causal gene: **NPHS1** (nephrin). MONDO:0009732 · OMIM:256300.*


## Artifacts

- [OpenScientist final report](Congenital_Nephrotic_Syndrome_Finnish_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Nephrotic_Syndrome_Finnish_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 15 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009732` (3 mentions) - the report calls it "MONDO"; MONDO calls it **congenital nephrotic syndrome, Finnish type**
- `HP:0003073` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypoalbuminemia**
- `HP:0003124` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypercholesterolemia**
- `HP:0000100` (1 mention) - the report calls it "Composite"; HP calls it **Nephrotic syndrome**
- `HP:0001622` (1 mention) - the report calls it "Perinatal"; HP calls it **Premature birth**
- `HP:0001518` (1 mention) - the report calls it "Perinatal"; HP calls it **Small for gestational age**
- `HP:0002719` (1 mention) - the report calls it "Clinical"; HP calls it **Recurrent infections**
- `HP:0001977` (1 mention) - the report calls it "Clinical"; HP calls it **Abnormal thrombosis**
- `HP:0001789` (1 mention) - the report calls it "Prenatal"; HP calls it **Hydrops fetalis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003774` (1 mention) - the report calls it "Stage 5 CKD"; HP calls it **Stage 5 chronic kidney disease**
- `CL:0000653` (2 mentions) - the report calls it "Primary cell:** **Podocyte** / glomerular visceral epithelial cell"; CL calls it **podocyte**, and lists "glomerular visceral epithelial cell" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** Kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.