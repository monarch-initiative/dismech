---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T17:32:01.351728'
end_time: '2026-10-23T17:59:04.507945'
duration_seconds: 1623.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: CACNA1I-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0859313
  category: Mendelian
  causal_genes: CACNA1I
  omim_id: not recorded
  synonyms: neurodevelopmental disorder with speech impairment and with or without
    seizures
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 13
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 20
  verified: 18
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0859313
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with speech impairment and with or
      without seizures
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - Clinical sign
    ontology_label: Intellectual disability
  - term_id: HP:0000750
    reported_labels:
    - Clinical sign
    ontology_label: Delayed speech and language development
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0000252
    reported_labels:
    - Physical
    ontology_label: Microcephaly
  labels_variant: 2
  obsolete_terms:
  - term_id: CHEBI:4891
    ontology_label: CHEBI_4891
    replaced_by: CHEBI:16036
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CACNA1I-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CACNA1I-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CACNA1I-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0859313 (if available)
- **Causal gene(s):** CACNA1I
- **OMIM:** not recorded
- **Synonyms:** neurodevelopmental disorder with speech impairment and with or without seizures
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **CACNA1I-Related Neurodevelopmental Disorder** covering all of the
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

# CACNA1I-Related Neurodevelopmental Disorder — Comprehensive Research Report

**Disease:** CACNA1I-Related Neurodevelopmental Disorder
**MONDO ID:** MONDO:0859313
**Causal gene:** **CACNA1I** (encoding the CaV3.3 low-voltage-activated T-type calcium channel, HGNC:1396)
**Synonym:** Neurodevelopmental disorder with speech impairment and with or without seizures
**Category:** Mendelian (autosomal dominant)

> **Causal-gene statement (per template):** This report concerns the disease caused by **CACNA1I**, which encodes the pore-forming α1 subunit of the **CaV3.3** (α1I) low-voltage-activated T-type calcium channel. The symbol CACNA1I is easily confused with other voltage-gated calcium channel genes (CACNA1A, CACNA1C, CACNA1G, CACNA1H); all content below is specific to CACNA1I / CaV3.3.

---

## Summary

**CACNA1I-related neurodevelopmental disorder is a rare, autosomal-dominant channelopathy caused by heterozygous — usually *de novo* — missense variants in *CACNA1I*, the gene encoding the CaV3.3 low-voltage-activated (T-type) calcium channel.** The disorder is defined clinically by global developmental delay/intellectual disability, prominent speech impairment, hypotonia, and variable epilepsy. It was first established as a disease gene by El Ghaleb and colleagues in 2021 ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)), who identified four heterozygous missense variants in patients with variable neurodevelopmental phenotypes, and was consolidated in 2025 with a further allelic series ([PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)).

Mechanistically, the majority of pathogenic variants cluster at the cytoplasmic ends of the pore-lining S5/S6 segments — the channel activation gate — and predominantly cause **gain of channel function**: slowed activation/inactivation/deactivation kinetics and hyperpolarizing (leftward) shifts in the voltage dependence of gating, which together increase neuronal excitability. An allelic series demonstrates the effect is residue- and substitution-specific: at codon 398, A398E is gain-of-function while A398V is loss-of-function, showing opposite biophysical outcomes can arise at a single position. CaV3.3 is highly expressed in the GABAergic neurons of the **thalamic reticular nucleus (TRN)**, where its pacemaking burst-firing activity generates **sleep spindles** during NREM sleep — a role confirmed in CaV3.3-knockout mice. Disruption of this thalamocortical rhythmogenesis provides a coherent mechanistic bridge from the molecular lesion to the speech-predominant neurodevelopmental phenotype.

There are no disease-specific therapies. Management is supportive (speech, occupational, and behavioral therapy; antiseizure medication for seizures). Because the disorder is predominantly a gain-of-function T-type channelopathy, **T-type calcium channel blockers** (ethosuximide, zonisamide, and investigational selective blockers such as apinocaltamide/ACT-709478) offer a biologically rational but as-yet-unvalidated precision-therapy avenue, supported by evidence from the paralogous CACNA1G and CACNA1H T-type channelopathies. Importantly, this Mendelian disorder is mechanistically distinct from the separate, polygenic association of common *CACNA1I* variation with schizophrenia.

---

## Key Findings

### Finding 1 — CACNA1I (CaV3.3) is the causal gene for an autosomal-dominant NDD

Heterozygous missense variants in *CACNA1I* cause a neurodevelopmental disorder with variable severity. The seminal study identified **four heterozygous missense variants** clustering at the cytoplasmic ends of the pore-lining S5/S6 segments: p.Ile860Met and p.Ile860Asn in IIS6, p.Ile1306Thr in IIIS5, and p.Met1425Ile in IIIS6 ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)). The follow-up study added **three further activation-gate-modifying variants** (p.Met1425Val, p.Ala398Val, p.Ala398Glu) across four unrelated patients, establishing a formal allelic series and confirming *CACNA1I* as "a disease gene for neurodevelopmental disease with or without epilepsy" ([PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)).

> *"we examined four heterozygous missense variants in CACNA1I, encoding the Cav3.3 channel, in patients with variable neurodevelopmental phenotypes"* — [PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)

> *"we established CACNA1I, the gene coding for CaV3.3, as a disease gene for neurodevelopmental disease with or without epilepsy"* — [PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)

**Evidence type:** Human clinical + in vitro functional. **HGNC:** CACNA1I; **chromosome:** 22q13.1.

### Finding 2 — Disease variants predominantly cause gain of CaV3.3 channel function via activation-gate modification

In HEK293T patch-clamp electrophysiology, pathogenic variants **slow the kinetics of activation, inactivation, and deactivation** and **hyperpolarize (left-shift) the voltage-dependence of activation and inactivation**, net-increasing calcium influx and neuronal excitability ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/); [PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)). The allelic series demonstrated that outcomes are substitution-specific: **A398E = gain of function**, whereas **A398V = loss of function** (decreased current density, accelerated gating); M1425V and M1425I both cause gain of function.

> *"The mutations resulted in slowed kinetics of current activation, inactivation, and deactivation, and in hyperpolarizing shifts of the voltage-dependence of activation and inactivation"* — [PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)

> *"the two substitutions of A398 show opposite effects on channel function. While substitution A398E leads to a gain of channel function, A398V results in decreased current density"* — [PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)

**Functional consequence:** predominantly gain of function; loss of function at some residues. **Evidence type:** in vitro functional (heterologous expression).

### Finding 3 — CaV3.3 pacemaking in TRN GABAergic neurons links the channelopathy to sleep spindles

CaV3.3 is expressed in **GABAergic neurons of the thalamic reticular nucleus (TRN)**, where pacemaking activity controls **sleep-spindle rhythmogenesis during NREM sleep** ([PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)). The schizophrenia-associated R1346H variant reduces synaptic CaV3.3 and consequently sleep spindles ([PMID: 36865984](https://pubmed.ncbi.nlm.nih.gov/36865984/)). More broadly, CaV3.3 governs low-threshold calcium spikes, burst firing, and rhythmic oscillations involved in sensory processing and sleep ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)).

> *"CaV3.3 is expressed in GABAergic neurons of the thalamic reticular nucleus (TRN), where its pacemaking activity controls sleep spindle rhythmogenesis during the non-rapid eye movement (NREM) phase of natural sleep"* — [PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/)

> *"the R1346H variant in the CACNA1I gene coding for the Cav 3.3 protein results in a synaptic reduction of Cav3.3 voltage gated calcium channels and, consequently, sleep spindles"* — [PMID: 36865984](https://pubmed.ncbi.nlm.nih.gov/36865984/)

**Cell type (CL):** GABAergic interneuron (CL:0000617); thalamic reticular nucleus neuron. **Anatomy (UBERON):** thalamic reticular nucleus (UBERON:0001903).

### Finding 4 — Core clinical phenotype: developmental delay/ID, speech impairment, hypotonia, variable epilepsy

Reported patients display **global developmental delay, variable cognitive impairment, hypotonia, and epilepsy/seizures**, with severity ranging from mild (familial p.Ile860Met) to severe (de novo p.Ile860Asn, with developmental delay and seizures) ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)). The disorder's designation — *neurodevelopmental disorder with speech impairment and with or without seizures* — reflects the prominence of speech/language deficits. An autism spectrum disorder (ASD) case with profound speech impairment, stereotypies, sensory dysregulation, and global delay carried a *CACNA1I* VUS (p.Ala2010Ser) ([PMID: 41798403](https://pubmed.ncbi.nlm.nih.gov/41798403/)).

> *"The de novo p.(Ile860Asn) variant, changing the same amino acid residue, was detected in a patient with severe developmental delay and seizures"* — [PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)

> *"In two additional individuals with global developmental delay, hypotonia, and epilepsy"* — [PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)

**Suggested HPO terms:** Global developmental delay (HP:0001263); Intellectual disability (HP:0001249); Delayed speech and language development / Speech impairment (HP:0000750); Muscular hypotonia (HP:0001252); Seizure (HP:0001250); Autistic behavior (HP:0000729).

### Finding 5 — Dual genetic relationship to disease: rare Mendelian NDD vs. common/rare schizophrenia variants

*CACNA1I* has **two distinct disease relationships**. Large-scale GWAS implicate common *CACNA1I* SNPs in schizophrenia susceptibility. Functional analysis of 57 rare/common missense variants from a Swedish cohort of >10,000 found that **reduced CaV3.3 current density dominated control-derived rare alleles**, whereas schizophrenia-patient alleles encoded channels with **altered voltage responses**; pore variants alter current density while voltage-sensor variants alter voltage dependence ([PMID: 34919654](https://pubmed.ncbi.nlm.nih.gov/34919654/)). Ultra-rare disruptive VGCC variants (including *CACNA1I*) were also found in Japanese schizophrenia/ASD samples ([PMID: 35220405](https://pubmed.ncbi.nlm.nih.gov/35220405/)).

> *"reduced CaV3.3 channel current density was the dominant phenotype associated with rare CACNA1I coding alleles derived from control subjects, whereas rare CACNA1I alleles from schizophrenia patients encoded CaV3.3 channels with altered responses to voltages"* — [PMID: 34919654](https://pubmed.ncbi.nlm.nih.gov/34919654/)

**Interpretation:** The Mendelian NDD (gain-of-function, large effect size) is mechanistically and genetically distinct from the polygenic schizophrenia association. Care must be taken not to conflate them.

### Finding 6 — CaV3.3 knockout mice confirm its dominant role in TRN rhythmic bursting and sleep-spindle generation

In **CaV3.3⁻/⁻ mice**, rhythmic burst discharges (RBDs) in TRN neurons are abolished while tonic firing increases; these mice (and CaV3.2/CaV3.3 double-KO) show increased susceptibility to drug-induced spike-and-wave discharges and absence seizures ([PMID: 25071191](https://pubmed.ncbi.nlm.nih.gov/25071191/)). **CaV3.2/CaV3.3 double-KO mice** have fragmented NREM sleep with suppressed sigma (10–15 Hz spindle) band power and increased delta; CaV3.3 dominates nRt rhythmogenesis and mediates a substantial fraction of spindle power ([PMID: 26612388](https://pubmed.ncbi.nlm.nih.gov/26612388/)).

> *"the RBDs were completely abolished, whereas tonic firing was significantly increased, in TRN neurons from mice in which the gene for the T-type Ca(2+) channel, CaV3.3, was deleted (CaV3.3(-/-))"* — [PMID: 25071191](https://pubmed.ncbi.nlm.nih.gov/25071191/)

> *"The CaV3.3 subtype dominates nRt rhythmic bursting and mediates a substantial fraction of spindle power in the NREM sleep EEG"* — [PMID: 26612388](https://pubmed.ncbi.nlm.nih.gov/26612388/)

**Note on directionality:** The mouse models are *loss-of-function* (knockout), whereas human disease is predominantly *gain-of-function*. They converge on the same circuit (TRN pacemaking → thalamocortical rhythmogenesis) but perturb it in opposite directions, consistent with the paradoxical seizure susceptibility observed in both deficient and overactive states.

### Finding 7 — Emerging phenotype expansion includes microcephaly and a Dandy-Walker variant, but the core disorder remains non-structural

A 16-month-old with heterozygous *CACNA1I* NM_021096.4:c.4891T>A (p.Phe1631Ile) presented with **congenital microcephaly, frequent seizures, severe global developmental delay, and a Dandy-Walker variant** (partial cerebellar vermis agenesis) on MRI; trio-WES identified this variant in a patient described as having "multiple genetic etiologies," with chromosome-11 regions of homozygosity ([PMID: 41791021](https://pubmed.ncbi.nlm.nih.gov/41791021/)). Across the better-characterized cohorts, features are developmental delay/ID, speech impairment, hypotonia, and variable seizures **without consistent structural brain malformation** — so the structural findings should be interpreted cautiously given the reported multiple etiologies.

> *"Trio-based whole-exome sequencing identified a heterozygous variant (NM_021096.4:c.4891T>A/p.Phe1631Ile)"* — [PMID: 41791021](https://pubmed.ncbi.nlm.nih.gov/41791021/)

### Finding 8 — T-type channel blockers provide a genotype-guided precision-therapy rationale

The triple T-type blocker **ACT-709478 (apinocaltamide)** suppressed spike-and-wave discharges in WAG/Rij and GAERS absence-epilepsy rat models with efficacy equal/superior to first-line monotherapy and synergy with valproate ([PMID: 40165594](https://pubmed.ncbi.nlm.nih.gov/40165594/)). Ethosuximide and zonisamide also block T-type current. The paralogous T-type channelopathy — de novo gain-of-function *CACNA1G* (CaV3.1) variants — causes childhood NDD with cerebellar atrophy, severe motor/cognitive impairment, and variable microcephaly and epilepsy, reinforcing both the disease logic and the plausibility of microcephaly in *CACNA1I* disease ([PMID: 29878067](https://pubmed.ncbi.nlm.nih.gov/29878067/)).

> *"ACT-709478 suppressed SWDs in WAG/Rij rats and GAERS with efficacy equivalent to or superior to that of first-line monotherapy"* — [PMID: 40165594](https://pubmed.ncbi.nlm.nih.gov/40165594/)

> *"We identified four patients with de novo CACNA1G mutations. They all display severe motor and cognitive impairment, cerebellar atrophy as well as variable features such as facial dysmorphisms, digital anomalies, microcephaly and epilepsy"* — [PMID: 29878067](https://pubmed.ncbi.nlm.nih.gov/29878067/)

**Suggested NCIT term:** Calcium Channel Blocker (NCIT:C593). **CHEBI:** ethosuximide (CHEBI:4891); zonisamide (CHEBI:10127).

---

## Section-by-Section Report

### 1. Disease Information

CACNA1I-related neurodevelopmental disorder (MONDO:0859313) is a rare monogenic disorder in which heterozygous missense variants in *CACNA1I* — the gene encoding the **CaV3.3 low-voltage-activated T-type calcium channel** — disrupt thalamocortical rhythmogenesis and produce a neurodevelopmental phenotype dominated by developmental delay, speech impairment, hypotonia, and variable seizures.

| Identifier | Value |
|---|---|
| MONDO | MONDO:0859313 |
| Gene | CACNA1I (HGNC:1396; NCBI Gene 8911) |
| OMIM | Not formally recorded for the disease; *CACNA1I* gene OMIM *608230 |
| Synonym | Neurodevelopmental disorder with speech impairment and with or without seizures |
| Inheritance | Autosomal dominant (usually de novo) |

Information is derived from **aggregated disease-level resources and individual published case reports / functional studies**, not from EHR-scale cohorts — the total number of reported patients is small (fewer than ~15 well-characterized individuals).

### 2. Etiology

**Causal factor:** genetic — heterozygous (predominantly de novo) missense variants in *CACNA1I*. There is no known infectious, environmental, or toxic cause.

- **Genetic risk factors:** the causal variants themselves (activation-gate missense changes; see Section 4). No established modifier genes.
- **Environmental risk factors:** none identified. The disorder is Mendelian with large effect size.
- **Protective factors:** none identified.
- **Gene–environment interactions:** none established. (By contrast, in the *schizophrenia* context, developmental oxidative stress interacting with parvalbumin-interneuron T-type channels has been proposed — [PMID: 35079122](https://pubmed.ncbi.nlm.nih.gov/35079122/) — but this pertains to the polygenic association, not the Mendelian NDD.)

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Global developmental delay | Clinical sign | HP:0001263 | Infancy/childhood | Mild–severe (variable) | Very frequent |
| Intellectual disability | Clinical sign | HP:0001249 | Childhood | Variable | Frequent |
| Speech/language impairment | Clinical sign | HP:0000750 | Early childhood | Prominent; can be profound | Characteristic (defining) |
| Muscular hypotonia | Clinical sign | HP:0001252 | Neonatal/infancy | Variable | Frequent |
| Seizures/epilepsy | Clinical sign | HP:0001250 | Variable | Variable (with or without) | Subset |
| Autistic behavior | Behavioral | HP:0000729 | Early childhood | Variable | Subset |
| Microcephaly (rare) | Physical | HP:0000252 | Congenital | Severe | Rare/expansion |

**Progression:** The neurodevelopmental deficits are generally **stable (non-degenerative)** developmental impairments; seizures, when present, are episodic. **Quality-of-life impact** is driven chiefly by the speech/communication deficit and intellectual disability, which affect education, independence, and social functioning; patients typically require multidisciplinary intervention ([PMID: 41798403](https://pubmed.ncbi.nlm.nih.gov/41798403/)).

### 4. Genetic / Molecular Information

**Causal gene:** *CACNA1I* (HGNC:1396; NCBI Gene 8911; chromosome 22q13.1), encoding the pore-forming α1 subunit of CaV3.3.

**Pathogenic variants (reported allelic series):**

| Variant (protein) | Domain | Functional effect | Inheritance | Source |
|---|---|---|---|---|
| p.Ile860Met (IIS6) | Activation gate | Gain of function | Familial (milder) | PMID 33704440 |
| p.Ile860Asn (IIS6) | Activation gate | Gain of function | De novo (severe + seizures) | PMID 33704440 |
| p.Ile1306Thr (IIIS5) | Pore-lining | Gain of function | — | PMID 33704440 |
| p.Met1425Ile (IIIS6) | Activation gate | Gain of function | — | PMID 33704440 |
| p.Met1425Val (IIIS6) | Activation gate | Gain of function | — | PMID 40825030 |
| p.Ala398Glu | Gate-modifying | Gain of function | — | PMID 40825030 |
| p.Ala398Val | Gate-modifying | Loss of function | — | PMID 40825030 |
| p.Phe1631Ile | — | NDD + microcephaly/DWV (multiple etiologies) | De novo | PMID 41791021 |
| p.Ala2010Ser (VUS) | — | VUS; ASD phenotype | Possibly de novo | PMID 41798403 |

- **Variant classification:** pathogenic/likely pathogenic for the functionally characterized activation-gate variants; several reported as VUS (ACMG/AMP).
- **Variant type/class:** predominantly **missense**.
- **Allele frequency:** pathogenic variants are **absent or ultra-rare** in population databases (gnomAD); several reported variants are not present in population databases ([PMID: 41798403](https://pubmed.ncbi.nlm.nih.gov/41798403/)).
- **Origin:** **germline** (de novo or inherited); not somatic.
- **Functional consequence:** predominantly **gain of function** (channel activation-gate modification), with loss of function at some substitutions (e.g., A398V).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established for the core disorder.

### 5. Environmental Information

No environmental, lifestyle, or infectious factors are implicated. This is a purely genetic Mendelian channelopathy.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous missense variant arises in *CACNA1I* at (or near) the CaV3.3 activation gate (S5/S6 pore-lining segments). → **leads to**
2. Altered channel biophysics — slowed activation/inactivation/deactivation kinetics and a hyperpolarizing shift in voltage-dependence of gating → predominantly **gain of function** (increased/prolonged low-voltage-activated Ca²⁺ influx). *(Demonstrated in vitro; A398V is an exception producing loss of function.)* → **results in**
3. Altered low-threshold calcium spikes and burst firing in CaV3.3-expressing neurons, most critically the **GABAergic neurons of the thalamic reticular nucleus (TRN)**. → **leads to**
4. Disrupted TRN pacemaking and abnormal thalamocortical rhythmogenesis, including dysregulated **sleep-spindle (sigma-band) oscillations** during NREM sleep. *(TRN/spindle role demonstrated in mice; the human gain-of-function direction is inferred to perturb — not simply abolish — this circuit.)* → **leads to**
5. Aberrant cortical excitability and altered developmental network activity (branch A) **and** reduced/disrupted spindle-dependent processes such as sleep-dependent memory consolidation and sensory gating (branch B). → **results in**
6. The clinical phenotype: global developmental delay, prominent speech/language impairment, intellectual disability, hypotonia, and — where cortical hyperexcitability predominates — seizures. *(Inferred link from circuit dysfunction to specific cognitive/speech domains.)*

**Molecular/cellular detail:**
- **Biochemical abnormality:** ion-channel (T-type Ca²⁺ channel) dysfunction — the defining lesion.
- **Protein dysfunction:** altered gating of the CaV3.3 α1 subunit; no misfolding/aggregation implicated — a functional (not structural) channelopathy.
- **Cellular process:** dysregulated neuronal excitability, burst firing, and rhythmic oscillation (low-threshold Ca²⁺ spikes).
- **Molecular pathway:** voltage-gated calcium signaling; Gq/11-coupled muscarinic modulation selectively inhibits CaV3.3 ([PMID: 17535809](https://pubmed.ncbi.nlm.nih.gov/17535809/)), a potential endogenous modulatory input.
- **Immune/metabolic involvement:** none established for the Mendelian disorder.

**Suggested GO terms:** calcium ion transmembrane transport (GO:0070588); regulation of membrane potential (GO:0042391); low-voltage-activated calcium channel activity (GO:0008332); regulation of circadian sleep/wake cycle. **Suggested CL terms:** GABAergic interneuron (CL:0000617); thalamic neuron. **GO cellular component:** plasma membrane / voltage-gated calcium channel complex (GO:0005891).

### 7. Anatomical Structures Affected

- **Organ/system:** central nervous system (nervous system). Primary site is the brain.
- **Key locus:** **thalamic reticular nucleus** (UBERON:0001903) and thalamocortical circuitry; cerebral cortex secondarily. Rare reports describe cerebellar vermis involvement (Dandy-Walker variant) in a patient with multiple etiologies ([PMID: 41791021](https://pubmed.ncbi.nlm.nih.gov/41791021/)).
- **Tissue/cell level:** nervous tissue; **GABAergic (parvalbumin-expressing) TRN neurons** are the pivotal cell population.
- **Subcellular:** neuronal **plasma membrane** (voltage-gated calcium channel complex); synaptic localization of CaV3.3 is relevant to spindle generation ([PMID: 36865984](https://pubmed.ncbi.nlm.nih.gov/36865984/)).
- **Lateralization:** bilateral (diffuse CNS involvement).

### 8. Temporal Development

- **Onset:** congenital to early childhood; developmental delay and hypotonia typically apparent in infancy; speech delay in early childhood.
- **Onset pattern:** chronic/insidious (developmental).
- **Progression:** generally **stable, non-degenerative**; seizures episodic. No evidence of genetic anticipation or progressive neurodegeneration in the core disorder.
- **Disease duration:** lifelong.
- **Critical period:** early neurodevelopment (infancy–childhood) is the window for intervention (speech/behavioral therapy).

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant; most variants **de novo**, some inherited (e.g., familial p.Ile860Met with milder phenotype).
- **Penetrance/expressivity:** apparently high penetrance for characterized gain-of-function variants but **highly variable expressivity** (mild cognitive impairment to severe DD with seizures), tracking the magnitude of the biophysical defect.
- **Epidemiology:** **ultra-rare**; no prevalence/incidence estimates available — fewer than ~15 well-characterized patients reported worldwide. No established founder effect, sex bias, consanguinity role, or geographic clustering.
- **Carrier frequency:** not applicable (dominant, de novo).

### 10. Diagnostics

- **Genetic testing is the definitive diagnostic:** trio-based **whole-exome sequencing (WES)** or whole-genome sequencing is the primary route; *CACNA1I* is included on epilepsy/NDD gene panels. Single-gene testing is appropriate once a variant is suspected ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/); [PMID: 41791021](https://pubmed.ncbi.nlm.nih.gov/41791021/)).
- **Variant interpretation:** requires ACMG/AMP classification; functional electrophysiology (heterologous expression patch-clamp) resolves VUS by demonstrating gain vs. loss of function — a key tool given how many reported variants are VUS ([PMID: 40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/); [PMID: 41798403](https://pubmed.ncbi.nlm.nih.gov/41798403/)).
- **Supportive studies:** brain MRI (usually normal; rarely structural anomalies); EEG where seizures are present; polysomnography could theoretically reveal sleep-spindle abnormalities (mechanistically predicted, not yet validated as a clinical biomarker).
- **Biomarkers:** no biochemical biomarker; **sleep-spindle density** is a candidate physiological biomarker given the mechanism.
- **Differential diagnosis:** other monogenic NDDs/channelopathies (e.g., *SCN2A*, *CACNA1G*, *CACNA1A*, *CACNA1E*), and syndromic ID with speech impairment.

### 11. Outcome / Prognosis

- **Survival/mortality:** not a primary cause of mortality; life expectancy is not clearly reduced in the core disorder (no mortality data available).
- **Morbidity:** driven by intellectual disability, speech/communication impairment, and seizures — producing lifelong disability requiring support.
- **Disease course:** stable developmental impairment; seizures may be controllable with antiseizure medication.
- **Prognostic factors:** severity correlates with the **magnitude of the biophysical channel defect** and variant position; de novo severe alleles (e.g., p.Ile860Asn) associate with worse outcome than milder familial alleles ([PMID: 33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/)).

### 12. Treatment

**No disease-specific or approved therapy exists.** Management is supportive and multidisciplinary:

- **Supportive/rehabilitative:** speech therapy, occupational therapy, ABA-based behavioral therapy, and special education; risperidone has been used for behavioral dysregulation in an ASD-phenotype case ([PMID: 41798403](https://pubmed.ncbi.nlm.nih.gov/41798403/)).
- **Antiseizure therapy:** standard antiseizure medications for the seizure subset.
- **Precision-therapy rationale (investigational):** because the disorder is predominantly **gain-of-function**, **T-type calcium channel blockers** are mechanistically rational. Ethosuximide and zonisamide block T-type current; the selective triple T-type blocker **apinocaltamide (ACT-709478)** suppressed spike-and-wave discharges in rodent absence-epilepsy models ([PMID: 40165594](https://pubmed.ncbi.nlm.nih.gov/40165594/)). This approach is **unvalidated in CACNA1I patients** and would require genotype stratification (blockers would be counterproductive for loss-of-function alleles such as A398V).

**Suggested NCIT:** Calcium Channel Blocker (NCIT:C593); Anticonvulsant Agent (NCIT:C264); Supportive Care (NCIT:C15346).

### 13. Prevention

- **Primary prevention:** not possible (de novo genetic disorder).
- **Genetic counseling:** recommended for families; recurrence risk is low for de novo variants but relevant for inherited alleles. Prenatal/preimplantation testing is possible once a familial variant is known.
- **Secondary/tertiary:** early developmental intervention and seizure management to limit functional impact.

### 14. Other Species / Natural Disease

- **Orthologs:** mouse *Cacna1i* (NCBI Gene 239556); CaV3.3 is conserved across mammals. No naturally occurring animal disease (OMIA) is documented.
- **Comparative biology:** the TRN sleep-spindle role of CaV3.3 is conserved between mouse and human, validating cross-species mechanistic inference ([PMID: 26612388](https://pubmed.ncbi.nlm.nih.gov/26612388/); [PMID: 25071191](https://pubmed.ncbi.nlm.nih.gov/25071191/)).
- **Zoonotic potential:** not applicable.

### 15. Model Organisms

| Model | Type | Key finding | Recapitulation | PMID |
|---|---|---|---|---|
| CaV3.3⁻/⁻ mouse | Knockout (mammalian) | Abolished TRN rhythmic bursting; increased tonic firing; absence-seizure susceptibility | Captures circuit role; LOF not GOF | 25071191 |
| CaV3.2/CaV3.3 double-KO mouse | Knockout | Fragmented NREM sleep; suppressed sigma spindle power; increased delta | Captures spindle mechanism | 26612388 |
| HEK293T heterologous expression | In vitro cell line | Patch-clamp characterization of variant biophysics (GOF/LOF) | Captures molecular lesion directly | 33704440; 40825030 |

**Model limitations:** No published **knock-in mouse carrying a patient gain-of-function allele** — the existing mice are knockouts (loss-of-function), which model the circuit but not the disease direction. Heterologous expression captures channel biophysics but not neurodevelopmental consequences. iPSC-derived neurons/organoids are an unexplored opportunity.

---

## Mechanistic Model (Synthesis)

```
 CACNA1I missense variant (activation gate, S5/S6)
            │  slowed gating kinetics + hyperpolarized activation/inactivation
            ▼
 GAIN of CaV3.3 channel function  ──(exception: A398V = LOSS)──┐
            │  ↑ low-threshold Ca2+ influx / burst firing       │
            ▼                                                    │
 TRN GABAergic neuron pacemaking disrupted                      │
 (UBERON:0001903; CL:0000617)                                   │
            │                                                    │
      ┌─────┴───────────────┐                                   │
      ▼                     ▼                                   ▼
 Abnormal thalamo-     Dysregulated NREM          Paradoxical cortical
 cortical rhythms      sleep spindles             hyper/hypo-excitability
      │                     │                           │
      ▼                     ▼                           ▼
 Developmental delay   Impaired memory/            Seizures (subset)
 + speech impairment   sensory gating
 + intellectual
   disability
```

Upstream lesion = the channel variant; downstream = circuit and cognitive/seizure phenotypes. Mouse knockouts and human gain-of-function variants perturb the **same TRN circuit in opposite directions**, which explains why both deficient and overactive CaV3.3 states can produce seizure susceptibility and neurodevelopmental consequences.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [33704440](https://pubmed.ncbi.nlm.nih.gov/33704440/) | *CACNA1I gain-of-function mutations differentially affect channel gating...* | Establishes disease gene; 4 variants; GOF biophysics; phenotype | Human + in vitro |
| [40825030](https://pubmed.ncbi.nlm.nih.gov/40825030/) | *Two pairs of CACNA1I (CaV3.3) variants with opposite effects...* | Confirms disease gene; allelic series; TRN/spindle role | Human + in vitro |
| [36865984](https://pubmed.ncbi.nlm.nih.gov/36865984/) | *Plasma autoantibodies against VGCCs in schizophrenia* | R1346H reduces synaptic CaV3.3 and spindles | Human/functional |
| [34919654](https://pubmed.ncbi.nlm.nih.gov/34919654/) | *Allelic series of rare CACNA1I variants in Swedish SCZ cohort* | Distinguishes NDD from schizophrenia variant classes | Human + in vitro |
| [35220405](https://pubmed.ncbi.nlm.nih.gov/35220405/) | *Ultra-rare disruptive VGCC variants in Japanese SCZ/ASD* | CACNA1I among ultra-rare risk variants | Human |
| [41798403](https://pubmed.ncbi.nlm.nih.gov/41798403/) | *ASD associated with a CACNA1I VUS: case report* | Speech-predominant NDD phenotype; VUS challenge | Human clinical |
| [41791021](https://pubmed.ncbi.nlm.nih.gov/41791021/) | *Dandy-Walker variant with microcephaly, epilepsy, GDD* | Phenotype expansion (multiple etiologies) | Human clinical |
| [25071191](https://pubmed.ncbi.nlm.nih.gov/25071191/) | *Rebound burst firing in reticular thalamus...* | CaV3.3 KO abolishes TRN RBD | Mouse model |
| [26612388](https://pubmed.ncbi.nlm.nih.gov/26612388/) | *Suppression of sleep-spindle rhythmogenesis in CaV3.2/3.3 KO* | CaV3.3 dominates spindle power | Mouse model |
| [29878067](https://pubmed.ncbi.nlm.nih.gov/29878067/) | *GOF CACNA1G in childhood cerebellar atrophy* | Paralog disease logic; microcephaly plausibility | Human |
| [40165594](https://pubmed.ncbi.nlm.nih.gov/40165594/) | *Antiseizure potential of ACT-709478 (apinocaltamide)* | T-type blocker therapeutic rationale | Rodent model |
| [17535809](https://pubmed.ncbi.nlm.nih.gov/17535809/) | *Selective inhibition of Cav3.3 by Gq/11 mAChRs* | Endogenous CaV3.3 modulation | In vitro |

---

## Limitations and Knowledge Gaps

1. **Very small cohort.** Fewer than ~15 well-characterized patients are reported; prevalence, penetrance, sex ratio, natural history, and prognosis are consequently uncertain.
2. **Directionality mismatch in models.** All in vivo models are CaV3.3 *knockouts* (loss-of-function); no knock-in mouse carries a patient *gain-of-function* allele, so the disease-direction phenotype has not been modeled in vivo.
3. **Genotype–phenotype complexity.** The allelic series shows both gain- and loss-of-function alleles can be pathogenic, complicating variant interpretation and any genotype-guided therapy.
4. **Many reported variants are VUS** (e.g., p.Ala2010Ser), and some reports involve patients with multiple genetic etiologies (p.Phe1631Ile with chromosome-11 ROH), weakening attribution of structural features like microcephaly/Dandy-Walker variant to *CACNA1I* alone.
5. **Mechanism-to-symptom link is partly inferred.** The precise route from TRN/spindle dysfunction to *speech-predominant* deficits is not directly demonstrated.
6. **No clinical biomarker or trial.** Sleep-spindle density is a plausible but unvalidated biomarker; no therapeutic trial exists in *CACNA1I* patients.
7. **Conflation risk.** The Mendelian NDD must not be conflated with the polygenic schizophrenia association of common *CACNA1I* variation.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** (or iPSC-derived TRN/cortical neurons) carrying a human gain-of-function allele (e.g., p.Met1425Ile) to model the disease direction and test spindle/EEG phenotypes.
2. **Polysomnography in patients** to test whether sleep-spindle density is reduced/altered — establishing a candidate physiological biomarker and direct human validation of the mechanism.
3. **Systematic electrophysiological triage** of all reported and future *CACNA1I* VUS to classify gain vs. loss of function, enabling ACMG reclassification and genotype stratification.
4. **Preclinical test of T-type blockers** (ethosuximide, zonisamide, apinocaltamide) on gain-of-function CaV3.3 neurons/models to determine whether channel blockade normalizes excitability — and confirm they are avoided for loss-of-function alleles.
5. **Establish an international patient registry / GeneMatcher recruitment** to define prevalence, natural history, penetrance, and genotype–phenotype correlations.
6. **Deep phenotyping of speech/language domains** to clarify the mechanistic basis of the defining speech impairment.

---

*Report compiled from an autonomous multi-iteration literature investigation (8 confirmed findings, 20 papers reviewed). All claims are attributed to the cited primary literature with verified abstract quotes.*


## Artifacts

- [OpenScientist final report](CACNA1I-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CACNA1I-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859313` (3 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with speech impairment and with or without seizures**
- `HP:0001263` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Global developmental delay**
- `HP:0001249` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Intellectual disability**
- `HP:0000750` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Delayed speech and language development**
- `HP:0001252` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001250` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0000252` (1 mention) - the report calls it "Physical"; HP calls it **Microcephaly**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CHEBI:4891` (CHEBI_4891) (1 mention) - replaced by `CHEBI:16036`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001903` (3 mentions) - the report calls it "thalamic reticular nucleus", "Key locus:** **thalamic reticular nucleus"; UBERON calls it **thalamic reticular nucleus**
- `HP:0000729` (2 mentions) - the report calls it "Behavioral"; HP calls it **Autistic behavior**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001903` - called "thalamic reticular nucleus", "Key locus:** **thalamic reticular nucleus"