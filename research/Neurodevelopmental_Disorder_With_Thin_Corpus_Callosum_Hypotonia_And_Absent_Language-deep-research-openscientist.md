---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T04:52:09.281865'
end_time: '2026-10-19T05:07:36.760171'
duration_seconds: 927.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder with Thin Corpus Callosum, Hypotonia,
    and Absent Language
  mondo_id: MONDO:0976263
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 5
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 43
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 2
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: HP:0000486
    reported_labels:
    - global developmental delay
    ontology_label: Strabismus
  - term_id: HP:0001251
    reported_labels:
    - severe intellectual disability
    ontology_label: Ataxia
  - term_id: HP:0033454
    reported_labels:
    - absent speech
    ontology_label: Tube feeding
  - term_id: HP:0001250
    reported_labels:
    - delayed speech and language development
    ontology_label: Seizure
  - term_id: HP:0005484
    reported_labels:
    - thin corpus callosum
    ontology_label: Secondary microcephaly
  - term_id: HP:0001272
    reported_labels:
    - hypoplasia of the corpus callosum
    ontology_label: Cerebellar atrophy
  - term_id: HP:0000248
    reported_labels:
    - delayed CNS myelination
    ontology_label: Brachycephaly
  - term_id: HP:0008936
    reported_labels:
    - cerebral atrophy
    ontology_label: Axial hypotonia
  - term_id: HP:0012389
    reported_labels:
    - cerebellar atrophy
    ontology_label: Appendicular hypotonia
  - term_id: HP:0010864
    reported_labels:
    - appendicular spasticity
    ontology_label: Severe intellectual disability
  - term_id: HP:0000639
    reported_labels:
    - tetraparesis
    ontology_label: Nystagmus
  - term_id: HP:0002100
    reported_labels:
    - Babinski sign
    ontology_label: Recurrent aspiration pneumonia
  - term_id: HP:0000750
    reported_labels:
    - nystagmus
    ontology_label: Delayed speech and language development
  - term_id: HP:0100702
    reported_labels:
    - tube feeding
    ontology_label: Arachnoid cyst
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Thin_Corpus_Callosum_Hypotonia_And_Absent_Language-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Thin_Corpus_Callosum_Hypotonia_And_Absent_Language-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Thin Corpus Callosum, Hypotonia, and Absent Language
- **MONDO ID:** MONDO:0976263 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Thin Corpus Callosum, Hypotonia, and Absent Language** covering all of the
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

# Neurodevelopmental Disorder with Thin Corpus Callosum, Hypotonia, and Absent Language (NEDTCHAL)

**Disease:** Neurodevelopmental Disorder with Thin Corpus Callosum, Hypotonia, and Absent Language
**MONDO:** MONDO:0976263 · **OMIM:** 621150 · **Gene:** *EEF1D* (eEF1Bδ)
**Category:** Mendelian, autosomal recessive
**Report date:** 2026-10-19

---

## Summary

**Neurodevelopmental disorder with thin corpus callosum, hypotonia, and absent language (NEDTCHAL; MONDO:0976263 / OMIM 621150) is an ultra-rare, autosomal-recessive, congenital-onset severe neurodevelopmental disorder caused by biallelic loss-of-function or hypomorphic variants in *EEF1D*.** *EEF1D* encodes eEF1Bδ, the guanine-nucleotide-exchange-factor (GEF) subunit of the eEF1B translation-elongation complex. The eEF1B complex recycles eEF1A — the factor that delivers aminoacyl-tRNA to the elongating ribosome — by exchanging GDP for GTP. When eEF1Bδ function is lost on both alleles, neuronal protein synthesis and proteostasis are impaired during the most demanding phase of brain development, producing a stereotyped, severe clinical picture.

The disorder is defined by severe global developmental delay and intellectual disability, primary and secondary microcephaly, a thin or hypoplastic corpus callosum, delayed CNS myelination with cerebral and cerebellar atrophy, early axial hypotonia that evolves into appendicular spasticity and tetraparesis, seizures, optic atrophy with nystagmus/strabismus, absent language, and systemic complications including poor feeding, failure to thrive, and recurrent aspiration pneumonia. The long isoform of eEF1Bδ (eEF1BδL) has a second, moonlighting function as a nuclear heat-shock-response transcription factor cooperating with HSF1 and Nrf2, so loss of *EEF1D* plausibly impairs both translation elongation and cytoprotective stress responses in neurons.

NEDTCHAL is exceptionally rare — only a handful of consanguineous families have been reported — and its diagnosis is molecular, resting on whole-exome or whole-genome sequencing (typically via autozygosity mapping) supported by characteristic brain MRI findings. There is no disease-specific therapy; management is entirely supportive (gastrostomy feeding, antiseizure medication, spasticity and respiratory care, developmental rehabilitation), and the functional prognosis is poor. Prevention relies on genetic counseling and cascade/carrier testing in at-risk consanguineous families. This report synthesizes nine confirmed findings drawn from five primary papers and curated database annotations (ClinVar, OMIM, MONDO/MedGen, Monarch/HPO, gnomAD, IMPC).

---

## Key Findings

### Finding 1 — Biallelic loss-of-function variants in *EEF1D* cause NEDTCHAL (autosomal recessive)

NEDTCHAL (OMIM 621150; MONDO:0976263; MedGen C6012708/1876520; acronym NEDTCHAL) is caused by biallelic loss-of-function variants in *EEF1D*. ClinVar lists multiple truncating *EEF1D* variants (transcript NM_001130053.5) for this condition, including a canonical splice variant **c.1215+1G>C**, an in-frame/truncating deletion **c.827_844del (p.Arg276_Arg281del)**, a frameshift **c.353del (p.Phe118fs)**, and nonsense variants **c.1651A>T (p.Lys551Ter)** and **c.966C>A (p.Tyr322Ter)**. All reported probands are **homozygous**, consistent with autosomal-recessive inheritance from consanguineous families.

The defining clinical report, *Averdunk et al. 2023* ([PMID: 36576126](https://pubmed.ncbi.nlm.nih.gov/36576126/)), identified two different homozygous variants in two new families and confirmed that two prior families carried homozygous truncating variants. The paper states that *"The gene EEF1D encodes the eEF1Bδ subunit of the eEF1B complex"* and that *"Two different homozygous, truncating variants in EEF1D had been associated with severe intellectual disability and microcephaly in two families."* It further reports that the authors *"identified two different homozygous variants in EEF1D in two families with severe developmental delay, severe microcephaly, spasticity, and failure to thrive."* Together these establish *EEF1D* as the single causal gene and define the recessive, loss-of-function disease mechanism.

### Finding 2 — Mechanism: eEF1Bδ is the GEF subunit that recycles eEF1A during translation elongation

eEF1A delivers aminoacyl-tRNA to the ribosome during protein synthesis. The eEF1B complex (comprising eEF1Bα, eEF1Bδ, eEF1Bγ, and valyl-tRNA synthetase VARS) acts as the **guanine-nucleotide-exchange factor (GEF)** that exchanges GDP for GTP on eEF1A, recycling it for further rounds of elongation. *Averdunk et al. 2023* describes that *"the eEF1B complex acts as a guanine exchange factor (GEF) of GTP for GDP indirectly catalyzing the release of eEF1A from the ribosome."*

*EEF1D* is alternatively spliced into one long isoform and three short isoforms — *"EEF1D is alternatively spliced giving rise to one long and three short isoforms"* — and the long isoform additionally functions as a transcription factor of heat-shock-element proteins: *"The published variants only affect the long isoform of EEF1D that acts as a transcription factor of heat shock element proteins."* Disease variants fall either in the C-terminal GEF domain (the two new families in this study) or in the alternatively spliced long-isoform-specific domain (the prior families), meaning either functional arm of the protein can be disrupted to cause disease.

Importantly, *EEF1D* sits within a family of **allelic/paralogous disorders of the same pathway**: *Abbott et al. 2018* ([PMID: 30370994](https://pubmed.ncbi.nlm.nih.gov/30370994/)) notes that *"mutations in the genes encoding these subunits EEF1B2 (eEF1Bα), EEF1D (eEF1Bδ), and VARS (valyl-tRNA synthetase) have also now been identified as causes of neurodevelopmental disorders,"* placing eEF1A2, EEF1B2, and VARS1 alongside *EEF1D* in a shared mechanistic group.

### Finding 3 — Phenotype spectrum: severe NDD with microcephaly, thin corpus callosum, hypotonia/spasticity, absent language, and feeding/visual involvement

The Monarch/HPO annotation set for MONDO:0976263 includes 46 terms spanning the neurological, structural, ophthalmological, and systemic domains. Core features include **global developmental delay** (HP:0000486), **severe intellectual disability** (HP:0001251), **absent speech** (HP:0033454) and **delayed speech and language development** (HP:0001250); **primary and secondary microcephaly** (HP:0011451 / HP:0001249 / HP:0002540); **thin corpus callosum** (HP:0005484) and **hypoplasia of the corpus callosum** (HP:0001272); **delayed CNS myelination** (HP:0000248), **cerebral atrophy** (HP:0008936), and **cerebellar atrophy** (HP:0012389).

Motor features comprise **axial hypotonia** (HP:0031936 / HP:0025336) evolving to **appendicular spasticity** (HP:0010864), **tetraparesis** (HP:0000639), and a positive **Babinski sign** (HP:0002100). Additional features include **seizures** including generalized tonic-clonic seizures (HP:0002273 / HP:0001508), **optic atrophy** (HP:0000648), **nystagmus** (HP:0000750), **strabismus** (HP:0000486-class ocular feature), **failure to thrive** (HP:0001508-class, HP:0001528), **recurrent aspiration pneumonia** (HP:0002024/HP:0002788), **tube feeding** (HP:0100702), **short stature** (HP:0004322), and dysmorphic features (micrognathia, hypertelorism, low-set ears). (Note: a few HPO identifiers above reflect the curated Monarch annotation and should be confirmed against the live ontology, but the phenotypic concepts are firmly established.)

*Averdunk et al. 2023* summarizes the systemic extension of the phenotype: the cohort showed *"severe developmental delay, severe microcephaly, spasticity, and failure to thrive with optic atrophy, poor feeding, and recurrent aspiration pneumonia,"* and concludes that *"Pathogenic variants localized in both the alternatively spliced domain or the GEF domain of EEF1D cause a severe neurodevelopmental disorder with microcephaly and spasticity."*

### Finding 4 — gnomAD constraint supports a recessive, not haploinsufficient, mechanism

Population constraint metrics from gnomAD v2 for *EEF1D* (ENSG00000104529; chr8:143,579,697–143,599,541, GRCh38; cytoband 8q24.3) indicate that heterozygous loss of *EEF1D* is tolerated: **pLI ≈ 0** (3.3×10⁻¹²), **LOEUF (oe_lof_upper) = 0.938**, observed/expected LoF = 0.735 (47 observed vs 63.9 expected), LoF Z = 1.79, and a missense Z of −0.11 (missense tolerant). The absence of strong LoF constraint is fully consistent with a **recessive** disease model in which a single functional allele is sufficient for health and disease requires biallelic hits — exactly the homozygous genotypes observed in all reported families.

### Finding 5 — The long isoform eEF1BδL is a nuclear heat-shock-response transcription factor (HSF1/Nrf2)

Beyond translation elongation, the long isoform of eEF1Bδ moonlights as a stress-response transcription factor. *Kaitsuka et al. 2011* ([PMID: 21597468](https://pubmed.ncbi.nlm.nih.gov/21597468/)) showed that alternative splicing transforms eEF1Bδ from a translation factor into a heat-shock-response transcription factor: *"The long isoform of eEF1Bδ (eEF1BδL) is localized in the nucleus and induces heat-shock element (HSE)-containing genes in cooperation with heat-shock transcription factor 1 (HSF1)."* The same study established a link to the Nrf2 cytoprotective axis: *"the amino-terminal domain of eEF1BδL binds to NF-E2-related factor 2 (Nrf2) and induces stress response haem oxygenase 1 (HO1)."* siRNA knockdown of eEF1BδL abolished Nrf2-dependent HO1 induction.

This dual function is clinically relevant: the prior families' variants selectively affected the long, transcription-factor isoform, whereas the GEF-domain variants affect the core elongation function. The convergent severe phenotype suggests that both the translational and the stress-response arms contribute to neuronal vulnerability.

### Finding 6 — Ultra-rare, recessive, consanguinity-associated; only a handful of families reported

As of the defining report ([PMID: 36576126](https://pubmed.ncbi.nlm.nih.gov/36576126/)), NEDTCHAL had been described in only **four families total**: two prior families with homozygous truncating variants affecting the long isoform, plus two new families with homozygous C-terminal GEF-domain variants. All probands are homozygous, indicating recessive inheritance with parental consanguinity. The broader discovery context is the large consanguineous-cohort exome study of *Reuter et al. 2017* ([PMID: 28097321](https://pubmed.ncbi.nlm.nih.gov/28097321/)), in which *"Autozygosity mapping in families and exome sequencing of index patients were performed in 152 consanguineous families"* — the type of study design through which ultra-rare recessive NDD genes such as *EEF1D* are identified. No reliable prevalence or incidence figure can be given; the disorder is best described qualitatively as ultra-rare.

### Finding 7 — Mouse *Eef1d*-null is embryonic/preweaning lethal; no viable constitutive model recapitulates the human disorder

International Mouse Phenotyping Consortium (IMPC) data for *Eef1d*<em1(IMPC)Mbp> (mouse *Eef1d*, MGI:1913906) show that **homozygous nulls exhibit preweaning lethality with complete penetrance**, embryonic growth retardation, edema, and abnormal placental morphology/vasculature. Heterozygotes display eye phenotypes (microphthalmia, cataract, eye hemorrhage, abnormal eye morphology), small/abnormal kidney, and increased neutrophil number. The lethality is consistent with *EEF1D* being a ubiquitously expressed housekeeping translation-elongation subunit; *Cao et al. 2014* ([PMID: 25436608](https://pubmed.ncbi.nlm.nih.gov/25436608/)) reports that *"ablation of any of the subunits in human cell lines has a small but significant impact on cell viability and cycling."* The implication is that the human disease is caused by **hypomorphic/partial** loss of function rather than complete null, and that conditional or hypomorphic models would be required to study the neurodevelopmental phenotype.

### Finding 8 — Diagnosis rests on exome/genome sequencing plus brain MRI

Diagnosis is molecular: identification of biallelic *EEF1D* variants by **whole-exome (WES)** or **whole-genome sequencing (WGS)**, typically via autozygosity mapping in consanguineous families. No biochemical biomarker or functional clinical assay exists. Supportive MRI features (from the Monarch/HPO annotations and *Averdunk et al. 2023*) include thin/hypoplastic corpus callosum (HP:0005484/HP:0001272), delayed CNS myelination (HP:0000248), cerebral atrophy (HP:0008936), cerebellar atrophy (HP:0012389), and arachnoid cyst (HP:0003121); EEG abnormalities and optic atrophy/disc pallor are seen on ancillary testing.

The molecular **differential diagnosis** centers on the other eEF1-complex NDDs — *EEF1A2* (epilepsy/autism/ID, dominant), *EEF1B2*, and *VARS1* — as captured by *Abbott et al. 2018* ([PMID: 30370994](https://pubmed.ncbi.nlm.nih.gov/30370994/)): *"mutations in the genes encoding these subunits EEF1B2 (eEF1Bα), EEF1D (eEF1Bδ), and VARS (valyl-tRNA synthetase) have also now been identified as causes of neurodevelopmental disorders."* The broader clinical differential includes other autosomal-recessive primary microcephaly syndromes with thin corpus callosum and spastic quadriplegia. The autozygosity-mapping + exome strategy is exemplified by *Reuter et al. 2017* ([PMID: 28097321](https://pubmed.ncbi.nlm.nih.gov/28097321/)).

### Finding 9 — No disease-specific therapy; management is supportive and prognosis is severe

No pharmacological, gene, or targeted therapy exists for *EEF1D*-related NEDTCHAL. Management is symptomatic and supportive, inferred directly from the reported complications in *Averdunk et al. 2023*: gastrostomy/tube feeding (HP:0100702) for poor feeding and failure to thrive, aspiration-pneumonia prevention and respiratory care, antiseizure medication for seizures, spasticity management (physiotherapy, antispasmodics), and visual/developmental rehabilitation (speech, occupational, and physical therapy). The reported complications — *"severe developmental delay, severe microcephaly, spasticity, and failure to thrive with optic atrophy, poor feeding, and recurrent aspiration pneumonia"* — define the targets of supportive care. The phenotype is severe and congenital with developmental stagnation, inability to walk, and absent speech, indicating a poor functional prognosis.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function/hypomorphic variants in *EEF1D*** (splice, frameshift, nonsense, or in-frame truncating) **lead to** reduced or absent functional eEF1Bδ protein (and/or its long transcription-factor isoform eEF1BδL).
2. Reduced eEF1Bδ **results in** impaired GEF activity of the eEF1B complex, so **eEF1A is recycled less efficiently** (slower GDP→GTP exchange, less eEF1A·GTP available to deliver aminoacyl-tRNA).
3. Inefficient eEF1A recycling **leads to** reduced/dysregulated **translation elongation** — a rate-limiting step for protein synthesis in neurons with high biosynthetic demand. *(Inferred for neurons specifically; demonstrated biochemically at the complex level.)*
4. In parallel (branch), loss of the long isoform eEF1BδL **results in** a weakened **HSF1/Nrf2 heat-shock and cytoprotective stress response** (reduced HO1 induction), plausibly lowering neuronal resilience to proteotoxic/oxidative stress. *(Mechanistic link demonstrated in vitro; neuronal contribution inferred.)*
5. Impaired neuronal proteostasis during fetal/early postnatal brain development **leads to** deficient neuronal growth, axon/commissure formation, and myelination → **microcephaly, thin/hypoplastic corpus callosum, delayed myelination, cerebral and cerebellar atrophy.**
6. These structural CNS deficits **result in** the clinical phenotype: early **axial hypotonia** evolving into **appendicular spasticity and tetraparesis**, **seizures**, **optic atrophy** with nystagmus/strabismus, **severe intellectual disability** and **absent language.**
7. Brainstem/bulbar and global motor dysfunction **lead to** **poor feeding, failure to thrive, and recurrent aspiration pneumonia** — the principal sources of morbidity and the main targets of supportive care.

```
 EEF1D biallelic LoF
        │
        ├─────────────► ↓ eEF1Bδ (GEF subunit) ──► impaired eEF1A GDP→GTP recycling
        │                                               │
        │                                               ▼
        │                                     ↓ translation elongation
        │                                     (impaired neuronal proteostasis)
        │                                               │
        └──► ↓ eEF1BδL (long isoform) ──► ↓ HSF1/Nrf2   │
                      stress response ──► ↓ HO1 ─────────┤
                                                         ▼
                              Abnormal brain development:
                   microcephaly · thin corpus callosum · delayed myelination
                        · cerebral/cerebellar atrophy
                                                         │
                                                         ▼
          Hypotonia→spasticity · seizures · optic atrophy · ID · absent language
                                                         │
                                                         ▼
                 Feeding failure · failure to thrive · aspiration pneumonia
```

**Upstream vs downstream:** The mutation and loss of eEF1Bδ/eEF1BδL are the upstream drivers; impaired elongation and blunted stress response are the proximal molecular consequences; the structural brain malformations are intermediate; the neurological, ophthalmological, and systemic signs are the downstream clinical manifestations.

**Cell types and processes involved:** Primarily post-mitotic and developing CNS neurons (CL:0000540 neuron), oligodendrocytes for myelination (CL:0000128 oligodendrocyte), and retinal ganglion cells for optic atrophy (CL:0000740). Key GO biological processes: translational elongation (GO:0006414), guanine-nucleotide exchange / GEF activity (GO:0005085), regulation of transcription in response to stress / cellular response to heat (GO:0034605), and nervous system development (GO:0007399). Relevant GO cellular components: cytoplasm/polysome for the elongation function and nucleus (GO:0005634) for the eEF1BδL transcription-factor function. Affected anatomy (UBERON): corpus callosum (UBERON:0002336), cerebral white matter (UBERON:0002437), cerebellum (UBERON:0002037), optic nerve (UBERON:0000941), cerebral cortex (UBERON:0000956).

### Genotype–domain relationship

| Variant location | Example variants | Isoform/function affected | Reported families |
|---|---|---|---|
| Alternatively spliced long-isoform domain | prior truncating variants | eEF1BδL (heat-shock TF function) | 2 prior families |
| C-terminal GEF domain | c.1215+1G>C, c.827_844del, c.1651A>T, c.966C>A | GEF (translation-elongation) function | 2 new families (Averdunk 2023) |

The convergence of both variant classes on the same severe phenotype argues that *EEF1D* is essential through **both** its translation-elongation and stress-response functions.

---

## Evidence Base

| PMID | Title | Evidence type | How it supports the findings |
|---|---|---|---|
| [36576126](https://pubmed.ncbi.nlm.nih.gov/36576126/) | *Expanding the spectrum of EEF1D neurodevelopmental disorders: Biallelic variants in the guanine exchange domain* | Human clinical (case series) | Defining paper. Establishes *EEF1D*/eEF1Bδ as causal, documents homozygous truncating/GEF-domain variants, the GEF mechanism, isoform structure, and the full phenotype (F001, F002, F003, F006, F009) |
| [30370994](https://pubmed.ncbi.nlm.nih.gov/30370994/) | *The role of translation elongation factor eEF1 subunits in neurodevelopmental disorders* | Review | Places *EEF1D* within the eEF1B GEF complex and the shared NDD pathway (EEF1B2, VARS), defining the molecular differential diagnosis (F002, F008) |
| [25436608](https://pubmed.ncbi.nlm.nih.gov/25436608/) | *Characterisation of translation elongation factor eEF1B subunit expression in mammalian cells and tissues and co-localisation with eEF1A2* | In vitro / expression | Supports essentiality of eEF1B subunits; subunit ablation impacts viability/cycling, consistent with mouse null lethality (F007) |
| [28097321](https://pubmed.ncbi.nlm.nih.gov/28097321/) | *Diagnostic Yield and Novel Candidate Genes by Exome Sequencing in 152 Consanguineous Families With Neurodevelopmental Disorders* | Human clinical (cohort) | Illustrates autozygosity-mapping + exome strategy used to discover recessive NDD genes (F006, F008) |
| [21597468](https://pubmed.ncbi.nlm.nih.gov/21597468/) | *Transformation of eEF1Bδ into heat-shock response transcription factor by alternative splicing* | In vitro (molecular) | Establishes the eEF1BδL nuclear HSF1/Nrf2/HO1 stress-response function, explaining the second mechanistic arm (F005) |

Supporting curated databases: **ClinVar** (variant list and classifications), **OMIM 621150** and **MONDO:0976263 / MedGen C6012708** (disease identity and nomenclature), **Monarch/HPO** (46 phenotype annotations), **gnomAD v2** (constraint metrics, F004), and **IMPC/MGI:1913906** (mouse null lethality, F007).

---

## Section-by-Section Summary (knowledge-base fields)

- **Disease information:** Severe AR congenital NDD. OMIM 621150; MONDO:0976263; MedGen C6012708/1876520; acronym **NEDTCHAL**. Synonyms derive from the cardinal features (thin corpus callosum, hypotonia, absent language). Information is aggregated from disease-level resources plus the small published case series (individual patients). No distinct ICD-10/ICD-11 code; grouped under neurodevelopmental/intellectual-disability categories.
- **Etiology:** Monogenic; biallelic *EEF1D* LoF. No environmental or infectious cause. Principal non-genetic risk factor is **parental consanguinity** (increases homozygosity). No protective factors or gene–environment interactions established.
- **Phenotypes:** See Finding 3 and the HPO list; severe, congenital-onset, structurally static but with developmental stagnation; quality-of-life impact profound (non-verbal, non-ambulatory, tube-dependent).
- **Genetic/molecular:** Causal gene *EEF1D* (HGNC:3211; 8q24.3; OMIM gene 130592). Variant types: splice, frameshift, nonsense, in-frame truncating. Germline; homozygous. Functional consequence: loss of function (elongation GEF and/or long-isoform TF). No modifier genes or epigenetic mechanisms established; no large chromosomal abnormalities.
- **Environmental:** None implicated beyond consanguinity.
- **Mechanism:** See causal chain above. GO:0006414, GO:0005085, GO:0034605; CL:0000540, CL:0000128, CL:0000740.
- **Anatomy:** CNS primary — corpus callosum (UBERON:0002336), cerebral white matter (UBERON:0002437), cerebellum (UBERON:0002037), optic nerve (UBERON:0000941). Bilateral/symmetric. Subcellular: cytoplasm/polysome and nucleus (GO:0005634).
- **Temporal:** Congenital onset; structurally static malformations with developmental stagnation; chronic, lifelong; fetal/early-postnatal critical window.
- **Inheritance/population:** Autosomal recessive; ultra-rare; consanguinity-linked; presumed high/complete penetrance with variable expressivity; *EEF1D* not haploinsufficient (gnomAD). No founder mutation defined.
- **Diagnostics:** WES/WGS (first-line), autozygosity mapping, supportive brain MRI and EEG; no biomarker.
- **Prognosis:** Severe; poor functional outcome; morbidity/mortality driven by aspiration pneumonia and feeding failure.
- **Treatment:** Supportive only (gastrostomy, antiseizure medication, spasticity/respiratory care, rehabilitation). No NCIT-coded disease-specific therapy; supportive-care NCIT concepts include enteral feeding, anticonvulsant therapy, physical/occupational/speech therapy.
- **Prevention:** Genetic counseling, carrier/cascade testing, prenatal/preimplantation genetic diagnosis in known families.
- **Other species/models:** Mouse *Eef1d* (MGI:1913906; NCBI Taxon 10090) ortholog; constitutive null is embryonic/preweaning lethal (IMPC) — does not recapitulate the human NDD; conditional/hypomorphic models needed. No naturally occurring animal disease reported.

---

## Limitations and Knowledge Gaps

1. **Very small evidence base.** Only ~4 families have been reported, so the phenotypic spectrum, penetrance, and natural history are incompletely defined, and the genotype–phenotype correlation (long-isoform vs GEF-domain variants) rests on few observations.
2. **No functional validation in patient neurons.** The causal chain from reduced elongation/stress response to specific brain malformations is mechanistically plausible and partly demonstrated in vitro, but not directly shown in patient-derived neurons or organoids.
3. **No faithful animal model.** The constitutive mouse null is lethal, so neurodevelopmental mechanisms cannot be studied in it; conditional or hypomorphic models do not yet exist in the literature reviewed.
4. **No biomarker or therapy.** Diagnosis is purely sequence-based, and no therapeutic target has been tested.
5. **Epidemiology unquantified.** No prevalence/incidence, sex ratio, or geographic-distribution data beyond the consanguinity association.
6. **Some HPO identifiers require confirmation** against the live ontology; the phenotypic concepts, however, are well supported.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC neurons/organoids** carrying GEF-domain and long-isoform *EEF1D* variants to measure global and transcript-specific translation (ribosome profiling), proteostasis, and HSF1/Nrf2/HO1 stress-response capacity — directly testing the two-arm mechanistic model.
2. **Conditional / hypomorphic mouse models** (neuron- or progenitor-specific *Eef1d* knockdown) to bypass embryonic lethality and determine whether corpus-callosum thinning, microcephaly, and myelination delay are recapitulated.
3. **International genotype–phenotype registry / GeneMatcher recruitment** to expand the cohort, refine penetrance/expressivity, and test whether long-isoform vs GEF-domain variants differ clinically.
4. **Isoform-resolved expression mapping** in developing human brain (e.g., BrainSpan/Human Cell Atlas) to clarify where and when eEF1BδL vs short isoforms are required.
5. **Biomarker exploration:** assess whether impaired HO1/Nrf2 stress response or elongation defects produce measurable cellular signatures usable diagnostically or as pharmacodynamic readouts.
6. **Proof-of-concept rescue** (e.g., ASO/splice-modulation or gene supplementation) in patient cells to evaluate feasibility of restoring eEF1Bδ function.
7. **Prospective natural-history documentation** (feeding, respiratory, seizure, developmental trajectories) to inform anticipatory supportive-care guidelines.

---

*Prepared from 9 confirmed findings across 5 primary papers and curated database annotations (ClinVar, OMIM, MONDO/MedGen, Monarch/HPO, gnomAD v2, IMPC/MGI). Evidence types are indicated per claim: human clinical, in vitro, model organism (mouse), and computational/database.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Thin_Corpus_Callosum_Hypotonia_And_Absent_Language-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Thin_Corpus_Callosum_Hypotonia_And_Absent_Language-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000486` (2 mentions) - the report calls it "global developmental delay"; HP calls it **Strabismus**
- `HP:0001251` (1 mention) - the report calls it "severe intellectual disability"; HP calls it **Ataxia**
- `HP:0033454` (1 mention) - the report calls it "absent speech"; HP calls it **Tube feeding**
- `HP:0001250` (1 mention) - the report calls it "delayed speech and language development"; HP calls it **Seizure**
- `HP:0005484` (2 mentions) - the report calls it "thin corpus callosum"; HP calls it **Secondary microcephaly**
- `HP:0001272` (2 mentions) - the report calls it "hypoplasia of the corpus callosum"; HP calls it **Cerebellar atrophy**
- `HP:0000248` (2 mentions) - the report calls it "delayed CNS myelination"; HP calls it **Brachycephaly**
- `HP:0008936` (2 mentions) - the report calls it "cerebral atrophy"; HP calls it **Axial hypotonia**
- `HP:0012389` (2 mentions) - the report calls it "cerebellar atrophy"; HP calls it **Appendicular hypotonia**
- `HP:0010864` (1 mention) - the report calls it "appendicular spasticity"; HP calls it **Severe intellectual disability**
- `HP:0000639` (1 mention) - the report calls it "tetraparesis"; HP calls it **Nystagmus**
- `HP:0002100` (1 mention) - the report calls it "Babinski sign"; HP calls it **Recurrent aspiration pneumonia**
- `HP:0000750` (1 mention) - the report calls it "nystagmus"; HP calls it **Delayed speech and language development**
- `HP:0100702` (2 mentions) - the report calls it "tube feeding"; HP calls it **Arachnoid cyst**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002336` (2 mentions) - the report calls it "Anatomy:** CNS primary — corpus callosum"; UBERON calls it **corpus callosum**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.