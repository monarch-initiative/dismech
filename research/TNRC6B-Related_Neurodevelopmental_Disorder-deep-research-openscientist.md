---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T23:35:09.290341'
end_time: '2026-10-20T23:47:53.360932'
duration_seconds: 764.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TNRC6B-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0030995
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
citation_count: 16
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:34847178
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 6
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0000750
    reported_labels:
    - Static
    ontology_label: Delayed speech and language development
  - term_id: HP:0010862
    reported_labels:
    - Static
    ontology_label: Delayed fine motor development
  - term_id: HP:0002194
    reported_labels:
    - Static
    ontology_label: Delayed gross motor development
  - term_id: HP:0007018
    reported_labels:
    - Static
    ontology_label: Attention deficit hyperactivity disorder
  - term_id: HP:0000708
    reported_labels:
    - Variable
    ontology_label: Atypical behavior
  - term_id: HP:0033127
    reported_labels:
    - Static
    ontology_label: Abnormality of the musculoskeletal system
  - term_id: HP:0001999
    reported_labels:
    - Static
    ontology_label: Abnormal facial shape
  - term_id: HP:0000252
    reported_labels:
    - Static
    ontology_label: Microcephaly
  - term_id: HP:0000957
    reported_labels:
    - Stable
    ontology_label: Cafe-au-lait spot
  - term_id: HP:0001250
    reported_labels:
    - Variable/episodic
    ontology_label: Seizure
  - term_id: HP:0001939
    reported_labels:
    - Variable
    ontology_label: Abnormality of metabolism/homeostasis
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TNRC6B-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TNRC6B-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TNRC6B-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0030995 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TNRC6B-Related Neurodevelopmental Disorder** covering all of the
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

# TNRC6B-Related Neurodevelopmental Disorder — Comprehensive Disease Report

**Disease:** TNRC6B-Related Neurodevelopmental Disorder
**Synonym (OMIM):** Global developmental delay with speech and behavioral abnormalities (GDSBA)
**OMIM:** 619243 (phenotype) · 610740 (gene) · **MONDO:** MONDO:0030995 · **Gene:** *TNRC6B* (HGNC:28368; NCBI Gene 23112; 22q13.1)
**Category:** Mendelian, autosomal dominant

---

## Summary

TNRC6B-related neurodevelopmental disorder (NDD) is an **ultra-rare, autosomal dominant Mendelian condition** caused by heterozygous, predominantly loss-of-function variants in *TNRC6B*, a gene encoding a GW182-family scaffold protein essential for microRNA (miRNA)-mediated gene silencing. The disorder was first systematically delineated in 2020 in a cohort of 17 patients ([PMID: 32152250](https://pubmed.ncbi.nlm.nih.gov/32152250/)), in which developmental delay/intellectual disability (DD/ID) was present in 100% of subjects, accompanied by speech delay (94%), motor delay (71–82%), autism or autistic traits (76%), ADHD (65%), and variable musculoskeletal and dysmorphic features. It carries the OMIM designation **619243 "Global developmental delay with speech and behavioral abnormalities"** and is formally described as an autosomal dominant disease caused by *TNRC6B* variants ([PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)).

Mechanistically, *TNRC6B* encodes one of three human GW182 paralogs (TNRC6A/B/C). The protein scaffolds the miRNA-induced silencing complex (miRISC): its glycine-tryptophan (GW/WG)-rich N-terminus binds Argonaute (AGO2), while its C-terminal silencing domain recruits poly(A)-binding protein (PABP) and the CCR4-NOT deadenylation machinery to execute target-mRNA repression. Pathogenic variants are heterozygous and reduce functional dosage (haploinsufficiency); the gene is highly loss-of-function intolerant in population databases (pLI ≈ 1.0). Because the same miRNA machinery (AGO2/TNRC6B/FMRP/MOV10) governs neural stem-cell differentiation, dendritic maturation, and DICER-dependent miRNA production, reduced TNRC6B dosage is proposed to dysregulate the post-transcriptional programs required for normal neuronal differentiation and cortical development, producing the neurodevelopmental phenotype.

Clinically, the disorder presents congenitally or in early childhood with a **static (non-progressive)** picture. Diagnosis is molecular — via trio whole-exome (WES) or whole-genome sequencing (WGS), supplemented by chromosomal microarray for 22q13.1 deletions, and by minigene/RNA assays to resolve splice-altering or synonymous variants of uncertain significance. There is **no disease-specific or targeted therapy**; management is entirely supportive (early intervention; speech, physical, and occupational therapy; special education; and symptomatic treatment of seizures, ADHD, and behavioral comorbidities). Life expectancy is expected to be normal or near-normal. The remainder of this report expands each disease-characteristic section with the available evidence and flags where information is absent from the primary literature.

---

## Key Findings

### Finding 1 — TNRC6B-related NDD is an autosomal dominant disorder caused by heterozygous *TNRC6B* variants (OMIM 619243)

The foundational clinical delineation comes from Granadillo et al. (2020), who characterized **17 patients** with heterozygous *TNRC6B* variants. The core phenotype was DD/ID in **17/17 (100%)**, with speech delay in **16/17 (94%)**, fine motor delay in **14/17 (82%)**, gross motor delay in **12/17 (71%)**, autism or autistic traits in **13/17 (76%)**, ADHD in **11/17 (65%)**, other behavioral problems in **7/17**, and musculoskeletal findings in **12/17 (71%)**. As stated in the abstract: *"Clinical findings included DD/ID (17/17) (speech delay in 94% (16/17), fine motor delay in 82% (14/17) and gross motor delay in 71% (12/17) of subjects), autism or autistic traits (13/17), attention deficit and hyperactivity disorder (ADHD) (11/17), other behavioural problems (7/17) and musculoskeletal findings (12/17)"* ([PMID: 32152250](https://pubmed.ncbi.nlm.nih.gov/32152250/)). The disorder carries OMIM 619243 and is described as *"an autosomal dominant disease caused by variants in TNRC6B gene"* ([PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)). This establishes both the inheritance pattern and the quantitative phenotype frequencies used throughout this report.

### Finding 2 — TNRC6B encodes a GW182-family scaffold essential for miRNA-mediated gene silencing

*TNRC6B* is one of three human GW182 paralogs (TNRC6A/B/C). Its GW/WG-rich N-terminus contains multiple Argonaute (AGO2)-binding sites that engage tryptophan-binding pockets in the AGO2 PIWI domain, while the C-terminal RRM/silencing domain recruits PABP and the CCR4-NOT deadenylation machinery. Functionally, TNRC6B is a core component of miRISC: *"two core protein components of human miRISC, Argonaute2 (Ago2) and TNRC6B, condense into phase-separated droplets in vitro and in live cells"* ([PMID: 29576456](https://pubmed.ncbi.nlm.nih.gov/29576456/)), and *"the multivalent binding of TNRC6 enables cooperative binding of miRNA-AGO complexes to target RNAs, thereby explaining the basis of cooperative action"* ([PMID: 32661162](https://pubmed.ncbi.nlm.nih.gov/32661162/)). GW182/TNRC6 proteins are required for miRNA activity: *"GW182 is required for transcriptional activation and for the activity of miRNAs"* ([PMID: 30086238](https://pubmed.ncbi.nlm.nih.gov/30086238/)). These data define the molecular role that is compromised in disease.

### Finding 3 — Pathogenic variants are predominantly loss-of-function, including a pathogenic synonymous splicing variant

Reported disease-causing variants span the full loss-of-function spectrum: nonsense, frameshift (e.g., c.1632delC p.Leu546fs*63), missense (e.g., c.335C>T p.Pro112Leu; c.1409A>G p.Asp470Ser), splice-altering, and whole/partial-gene deletions at 22q13.1. Notably, a **synonymous** variant c.3141G>A was proven pathogenic by minigene assay through induction of exon 7 skipping: *"we demonstrated that c.3141G > A variant induced exon 7 skipping and the synonymous variant was pathogenic"* ([PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)). Yang et al. reported *"novel de novo likely pathogenic or pathogenic TNRC6B variants c.335C>T (p.Pro112Leu) and c.1632delC (p.Leu546fs*63)"* ([PMID: 38404251](https://pubmed.ncbi.nlm.nih.gov/38404251/)). The gene is highly loss-of-function intolerant in gnomAD (pLI ≈ 1.0), consistent with **haploinsufficiency** as the disease mechanism.

### Finding 4 — Expanded phenotype includes dysmorphism, growth abnormalities, café-au-lait spots, seizures, and metabolic abnormalities

Beyond the core NDD features, the phenotypic spectrum has broadened. Yang et al. (2024) reported *"DD/ID, delayed speech, ADHD, behavioral abnormalities, short stature, low body weight, café-au-lait spots, metabolic abnormalities, and facial dysmorphism including coarse facial features, sparse hair, frontal bossing, hypertelorism, amblyopia, strabismus, and downslanted palpebral fissures"* ([PMID: 38404251](https://pubmed.ncbi.nlm.nih.gov/38404251/)). Importantly, there is no recognizable facial gestalt: *"The majority of patients exhibited some dysmorphic features but no recognisable gestalt was identified"* ([PMID: 32152250](https://pubmed.ncbi.nlm.nih.gov/32152250/)). Epilepsy co-occurring with ASD has been reported as a presenting feature ([PMID: 37348364](https://pubmed.ncbi.nlm.nih.gov/37348364/)).

### Finding 5 — The miRNA/miRISC machinery regulates neuronal differentiation and dendrite development, linking TNRC6B loss to neurodevelopmental phenotypes

TNRC6B operates within the neural miRNA machinery in a developmental-stage-specific manner: *"Developmental regulation of the processing pathway correlates with differential localization of the proteins Argonaute, FMRP, MOV10, and TNRC6B in self-renewing stem cells and neurons"* ([PMID: 17167072](https://pubmed.ncbi.nlm.nih.gov/17167072/)). The same AGO2-cofactor module controls DICER and dendrite formation: *"the MOV10-FMRP-AGO2 complex regulates DICER expression, revealing a novel mechanism for regulation of miRNA production required for normal neuronal morphology"* ([PMID: 34847178](https://pubmed.ncbi.nlm.nih.gov/34847178/)). This provides the mechanistic bridge between TNRC6B haploinsufficiency and impaired neurodevelopment.

### Finding 6 — Mouse Tnrc6 knockouts show paralog-specific essentiality, but no established Tnrc6b neurodevelopmental model exists

Guo et al. (2017) generated Tnrc6a/b/c knockout mice: *"TNRC6a mutants die at mid-gestation, while b- and c- deleted mice are born at a Mendelian ratio. However, the majority of TNRC6b and all TNRC6c mutants die within 24h after birth"* ([PMID: 28811219](https://pubmed.ncbi.nlm.nih.gov/28811219/)). Homozygous loss is largely perinatal-lethal and the paralogs are not fully redundant in vivo. The mouse ortholog is *Tnrc6b* (NCBI Gene 213988); the human gene is *TNRC6B* (NCBI Gene 23112, HGNC:28368). No heterozygous mouse model recapitulating the human neurodevelopmental phenotype has yet been reported.

### Finding 7 — Diagnosis relies on exome/genome sequencing; management is supportive with no disease-specific therapy

TNRC6B-related NDD is a molecular diagnosis made by WES/WGS and chromosomal microarray (for 22q13.1 deletions). Professional guidance supports broad genetic testing: *"professional medical organizations recommend genetic testing for all individuals with a NDD"* ([PMID: 41274961](https://pubmed.ncbi.nlm.nih.gov/41274961/)). Functional assays resolve ambiguous variants: *"WES combined with minigene assay establishes a robust basis for genetic counseling and diagnosing diseases"* ([PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)). No approved disease-specific therapy exists; management is supportive.

### Finding 8 — Autosomal dominant inheritance with both de novo and inherited variants, variable expressivity, and ultra-rare prevalence

Most pathogenic variants arise de novo (*"novel de novo likely pathogenic or pathogenic TNRC6B variants"* — [PMID: 38404251](https://pubmed.ncbi.nlm.nih.gov/38404251/)), confirming autosomal dominant inheritance (*"autosomal dominant disease caused by variants in TNRC6B gene"* — [PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)). However, inherited transmission occurs: a three-generation family segregating a 22q13.1 deletion involving *TNRC6B* has been reported ([PMID: 42074582](https://pubmed.ncbi.nlm.nih.gov/42074582/)), demonstrating vertical transmission with variable expressivity and probable incomplete penetrance. Fewer than ~50–100 molecularly confirmed cases exist; no formal prevalence/incidence has been established.

### Finding 9 — The central nervous system is the primary affected organ, with multisystem secondary involvement

The brain/CNS is the primary target (DD/ID, speech/language delay, ASD, ADHD, seizures). Secondary systems include musculoskeletal (12/17 in Granadillo 2020), craniofacial/skeletal, ophthalmologic (strabismus, amblyopia), growth/endocrine-metabolic, and integumentary (café-au-lait macules) systems — *"autism or autistic traits (13/17), attention deficit and hyperactivity disorder (ADHD) (11/17), other behavioural problems (7/17) and musculoskeletal findings (12/17)"* ([PMID: 32152250](https://pubmed.ncbi.nlm.nih.gov/32152250/)).

---

## Section-by-Section Report

### 1. Disease Information

TNRC6B-related neurodevelopmental disorder is a **monogenic, autosomal dominant NDD** caused by heterozygous variants in *TNRC6B*. It is characterized by developmental delay / intellectual disability, prominent speech and language delay, autism spectrum features, ADHD, and variable dysmorphic, growth, and behavioral abnormalities.

**Key identifiers:**
- **OMIM:** 619243 ("Global developmental delay with speech and behavioral abnormalities"; phenotype) / 610740 (*TNRC6B* gene)
- **MONDO:** MONDO:0030995
- **Gene:** *TNRC6B* — HGNC:28368; NCBI Gene 23112; chromosome 22q13.1
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No dedicated disease-specific code identified in the primary literature reviewed; the condition is captured under broad NDD/intellectual-disability categories.

**Synonyms / alternative names:** Global developmental delay with speech and behavioral abnormalities (GDSBA); TNRC6B deficiency syndrome; TNRC6B-related developmental delay.

**Information source type:** The disease-level knowledge is **aggregated from individual-patient case series and case reports** (notably the 17-patient Granadillo cohort and subsequent single/multi-patient reports), not from EHR-scale or registry-level datasets.

### 2. Etiology

**Causal factors:** Purely genetic — heterozygous, predominantly loss-of-function variants in *TNRC6B*. There is no evidence for environmental, infectious, or multifactorial causation.

**Genetic risk factors:** The causal variants themselves (nonsense, frameshift, splice-site, missense, synonymous splice-altering, and 22q13.1 deletions). No susceptibility loci or validated modifier genes have been established. In one case, co-occurrence of a *TNRC6B* variant with an Xq28/*MECP2* microdeletion was associated with a more severe phenotype, suggesting that a second genomic lesion can act as a modifier ([PMID: 41147347](https://pubmed.ncbi.nlm.nih.gov/41147347/)).

**Environmental risk factors / protective factors / gene-environment interactions:** None identified. As a Mendelian dominant disorder, environmental and lifestyle factors are not established contributors, and no protective alleles or gene-environment interactions are reported. *Not applicable / not available for this disease.*

### 3. Phenotypes

| Phenotype | Type | Frequency | Onset | Course | Suggested HPO |
|---|---|---|---|---|---|
| Developmental delay / intellectual disability | Cognitive/behavioral | 17/17 (100%) | Infancy/early childhood | Static | HP:0001263 / HP:0001249 |
| Speech / language delay | Cognitive/behavioral | 16/17 (94%) | Early childhood | Static | HP:0000750 |
| Fine motor delay | Motor | 14/17 (82%) | Infancy | Static | HP:0010862 |
| Gross motor delay | Motor | 12/17 (71%) | Infancy | Static | HP:0002194 |
| Autism / autistic traits | Behavioral | 13/17 (76%) | Early childhood | Static | HP:0000717 |
| ADHD | Behavioral | 11/17 (65%) | Childhood | Static | HP:0007018 |
| Other behavioral problems | Behavioral | 7/17 (41%) | Childhood | Variable | HP:0000708 |
| Musculoskeletal findings | Physical | 12/17 (71%) | Congenital/childhood | Static | HP:0033127 |
| Facial dysmorphism (no gestalt) | Physical | Majority | Congenital | Static | HP:0001999 |
| Short stature / low body weight | Growth | Variable | Childhood | Variable | HP:0004322 / HP:0004325 |
| Microcephaly | Physical | Occasional | Congenital/childhood | Static | HP:0000252 |
| Café-au-lait macules | Physical | Occasional | Childhood | Stable | HP:0000957 |
| Strabismus / amblyopia | Ophthalmologic | Occasional | Childhood | Variable | HP:0000486 / HP:0000646 |
| Seizures / epilepsy | Neurological | Occasional | Childhood | Variable/episodic | HP:0001250 |
| Metabolic abnormalities | Laboratory | Occasional | Childhood | Variable | HP:0001939 |

**Severity and quality-of-life impact:** Severity is variable but generally moderate; the dominant burden is cognitive, communicative, and behavioral, substantially affecting education, communication, and independent daily functioning. Formal QoL instrument data (EQ-5D, SF-36, PROMIS) are *not available* for this disorder.

### 4. Genetic/Molecular Information

**Causal gene:** *TNRC6B* (trinucleotide repeat containing 6B), 22q13.1; HGNC:28368; NCBI Gene 23112; OMIM gene 610740; disorder OMIM 619243.

**Pathogenic variants (representative):**

| Variant (cDNA) | Protein | Type | Classification | Origin |
|---|---|---|---|---|
| c.3141G>A | (synonymous) → exon 7 skipping | Splice-altering synonymous | Pathogenic (minigene-proven) | — |
| c.335C>T | p.Pro112Leu | Missense | Likely pathogenic/pathogenic | De novo |
| c.1632delC | p.Leu546fs*63 | Frameshift | Pathogenic | De novo |
| c.1409A>G | p.Asp470Ser | Missense | VUS/likely pathogenic | — |
| 22q13.1 deletion | whole/partial gene loss | Structural/CNV | Pathogenic | Inherited (3-gen family) |

**Allele frequency:** Pathogenic variants are absent or ultra-rare in gnomAD; *TNRC6B* is highly loss-of-function intolerant (pLI ≈ 1.0). **Origin:** Germline (de novo most common; inherited in deletion families). **Functional consequence:** Loss of function / haploinsufficiency.

**Modifier genes:** No validated modifiers; a second-site *MECP2* deletion worsened phenotype in one case ([PMID: 41147347](https://pubmed.ncbi.nlm.nih.gov/41147347/)). **Epigenetic information:** No disorder-specific DNA-methylation signature ("episignature") has been reported — *knowledge gap*. **Chromosomal abnormalities:** 22q13.1 deletions involving *TNRC6B* ([PMID: 42074582](https://pubmed.ncbi.nlm.nih.gov/42074582/)).

### 5. Environmental Information

No environmental, lifestyle, or infectious contributors are implicated. This is a monogenic disorder. *Not applicable.*

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous loss-of-function *TNRC6B* variant (nonsense/frameshift/splice/missense/deletion) **leads to** reduced production of functional TNRC6B protein (haploinsufficiency; demonstrated by LoF-intolerance and minigene-proven exon skipping).
2. Reduced TNRC6B **results in** diminished GW182-scaffold availability for assembly of the miRNA-induced silencing complex (miRISC) — TNRC6B normally bridges AGO2 to PABP and the CCR4-NOT deadenylase (demonstrated biochemically).
3. Impaired miRISC scaffolding **leads to** less efficient cooperative/multivalent binding of miRNA-AGO complexes to target mRNAs and reduced phase-separated condensate formation (demonstrated in vitro/in cells; [PMID: 29576456](https://pubmed.ncbi.nlm.nih.gov/29576456/), [PMID: 32661162](https://pubmed.ncbi.nlm.nih.gov/32661162/)).
4. Weakened miRNA-mediated silencing **results in** derepression of miRNA target transcripts and broadly dysregulated post-transcriptional gene expression (inferred from loss of miRNA activity; [PMID: 30086238](https://pubmed.ncbi.nlm.nih.gov/30086238/)).
5. Because this machinery (AGO2/TNRC6B/FMRP/MOV10) is developmentally deployed in neural stem cells and neurons and regulates DICER-dependent miRNA production, its disruption **leads to** impaired neural differentiation and dendritic maturation (demonstrated for the AGO2-cofactor module; [PMID: 17167072](https://pubmed.ncbi.nlm.nih.gov/17167072/), [PMID: 34847178](https://pubmed.ncbi.nlm.nih.gov/34847178/)).
6. Abnormal neuronal differentiation and connectivity during critical developmental windows **results in** the clinical neurodevelopmental phenotype — DD/ID, speech delay, ASD, ADHD, and seizures (inferred; the cell-biological-to-clinical link is not directly demonstrated in patients).

**Branch:** Beyond the CNS, TNRC6B-dependent miRNA regulation operates in multiple tissues, plausibly explaining the secondary musculoskeletal, craniofacial, growth, skin (café-au-lait), and metabolic features (inferred, pleiotropic).

```
TNRC6B LoF variant
      │ (haploinsufficiency)
      ▼
↓ functional TNRC6B (GW182 scaffold)
      │
      ▼
Defective miRISC assembly (AGO2–TNRC6B–PABP–CCR4/NOT)
      │
      ▼
↓ miRNA-mediated silencing / condensate formation
      │
      ├──► CNS branch: impaired neural differentiation & dendrite maturation ──► DD/ID, speech delay, ASD, ADHD, seizures
      └──► Systemic branch: pleiotropic miRNA dysregulation ──► dysmorphism, growth/metabolic, skeletal, skin findings
```

**Molecular pathway:** miRNA-mediated post-transcriptional gene silencing (RNA interference). **Cellular processes:** neural stem-cell differentiation, dendritic/neuronal morphogenesis, mRNA deadenylation/decay. **Protein dysfunction:** loss of function of a scaffolding protein. **Subcellular localization:** cytoplasmic P-bodies / ribonucleoprotein granules (GO:0000932 P-body; GO:0036464 cytoplasmic ribonucleoprotein granule). **Suggested GO BP terms:** GO:0035195 (miRNA-mediated gene silencing), GO:0031047 (regulation of gene silencing by RNA), GO:0021954 (CNS neuron development), GO:0016358 (dendrite development). **Suggested CL terms:** CL:0000540 (neuron), CL:0000047 (neuronal stem cell). No disorder-specific transcriptomic, proteomic, metabolomic, or CRISPR-screen data in patients are available — *knowledge gap*.

### 7. Anatomical Structures Affected

- **Primary organ:** Brain / central nervous system — UBERON:0000955 (brain), UBERON:0001017 (CNS), UBERON:0000956 (cerebral cortex).
- **Secondary involvement:** Musculoskeletal system (UBERON:0002204), craniofacial skeleton, eye (UBERON:0000970), skin (UBERON:0002097; café-au-lait macules), and growth/endocrine-metabolic axes.
- **Tissue/cell level:** Nervous tissue; neurons (CL:0000540) and neural progenitors (CL:0000047).
- **Subcellular:** Cytoplasmic P-bodies / RNP granules (GO:0000932, GO:0036464).
- **Localization/lateralization:** CNS involvement is bilateral/diffuse; no consistent lateralization.

### 8. Temporal Development

- **Onset:** Congenital to early childhood; delays typically recognized in infancy/toddlerhood.
- **Onset pattern:** Insidious/chronic (developmental).
- **Progression:** **Static (non-progressive)** neurodevelopmental course; behavioral problems may fluctuate, and seizures are episodic when present.
- **Duration:** Chronic, lifelong.
- **Remission:** No spontaneous remission; developmental gains occur with intervention.
- **Critical period:** Early childhood is the key window for developmental/therapeutic intervention.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant ([PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)).
- **Variant origin:** Predominantly de novo ([PMID: 38404251](https://pubmed.ncbi.nlm.nih.gov/38404251/)); inherited transmission documented in a three-generation 22q13.1-deletion family ([PMID: 42074582](https://pubmed.ncbi.nlm.nih.gov/42074582/)).
- **Penetrance/expressivity:** Variable expressivity; likely incomplete penetrance (inferred from familial segregation). Precise penetrance not quantified.
- **Anticipation / germline mosaicism / founder effects / consanguinity:** Not established (not a repeat-expansion disorder; dominant mechanism does not require consanguinity).
- **Epidemiology:** Ultra-rare; fewer than ~50–100 molecularly confirmed cases reported. No formal prevalence or incidence; no Orphanet prevalence estimate.
- **Population/sex distribution:** Reported across diverse populations (European, Chinese, others). No established founder effect or strong sex bias.

### 10. Diagnostics

- **Primary approach:** Molecular genetic testing. Trio **WES/WGS** is the first-tier test for NDD and identifies de novo *TNRC6B* variants; **chromosomal microarray (CMA)** detects 22q13.1 deletions. *"Professional medical organizations recommend genetic testing for all individuals with a NDD"* ([PMID: 41274961](https://pubmed.ncbi.nlm.nih.gov/41274961/)).
- **Variant interpretation:** Minigene / RNA splicing assays resolve synonymous and splice-region VUS — *"WES combined with minigene assay establishes a robust basis for genetic counseling and diagnosing diseases"* ([PMID: 39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/)).
- **Gene panels:** Broad intellectual-disability/autism/epilepsy NGS panels that include *TNRC6B*.
- **Imaging / EEG:** Brain MRI and EEG are used for phenotyping (seizures), not diagnostic of the gene.
- **Biomarkers:** No specific biochemical biomarker. **Karyotyping/FISH/mtDNA/repeat testing:** generally not indicated (CMA preferred for the deletion subtype).
- **Clinical criteria:** No standalone diagnostic criteria; diagnosis = compatible NDD phenotype + pathogenic *TNRC6B* variant.
- **Differential diagnosis:** Other monogenic NDD/ASD genes, 22q13 (Phelan-McDermid/*SHANK3*) region disorders, Rett syndrome (*MECP2*), and syndromic ID with café-au-lait (e.g., neurofibromatosis type 1, RASopathies, constitutional mismatch-repair deficiency) when pigmentary findings are present.
- **Screening:** No newborn/population screening; cascade testing for at-risk relatives in inherited cases.

### 11. Outcome/Prognosis

- **Survival/mortality:** Life expectancy is expected to be **normal or near-normal**; the disorder is not known to be life-limiting. No disease-specific mortality data.
- **Morbidity/disability:** Lifelong cognitive, communicative, and behavioral disability is the main burden; degree varies.
- **Complications:** Seizures, behavioral/psychiatric comorbidities (ASD, ADHD), feeding/growth issues in a subset.
- **Recovery potential:** Developmental gains achievable with early intervention; underlying deficits are static and persistent.
- **Prognostic factors:** Severity of baseline ID, presence of epilepsy, and co-occurring genomic lesions (e.g., concurrent *MECP2* deletion associated with more severe delay and malnutrition — [PMID: 41147347](https://pubmed.ncbi.nlm.nih.gov/41147347/)).

### 12. Treatment

- **Disease-specific/targeted therapy:** **None approved or available.** Management is supportive.
- **Pharmacotherapy (symptomatic):** Antiepileptic drugs for seizures; stimulant/non-stimulant ADHD medications; agents for behavioral/psychiatric comorbidities as clinically indicated (NCIT: anticonvulsant therapy; CNS stimulant therapy).
- **Rehabilitative/supportive:** Early intervention programs; speech-language therapy; physical and occupational therapy; special education; behavioral therapy for ASD; nutritional/feeding support where needed (NCIT: speech therapy; physical therapy; occupational therapy; supportive care).
- **Advanced/experimental therapeutics:** Gene-directed and ASO approaches for rare NDDs remain investigational; none specific to *TNRC6B*. No NCT-registered disorder-specific trials identified.
- **Pharmacogenomics / personalized medicine:** Not established for this disorder.
- **Treatment strategy:** Individualized, multidisciplinary, symptom-directed care.

### 13. Prevention

- **Primary prevention:** Not possible for de novo variants. **Genetic counseling** for families, especially where a variant is inherited (e.g., 22q13.1-deletion kindreds), informs recurrence risk (up to 50% for a transmitting dominant carrier).
- **Secondary prevention:** Early developmental surveillance and intervention to optimize outcomes.
- **Tertiary prevention:** Proactive management of seizures, behavioral comorbidities, and growth/nutrition to limit complications.
- **Reproductive options:** Prenatal diagnosis and preimplantation genetic testing are available for families with a known pathogenic variant.
- **Immunization / public-health / environmental measures:** Not applicable.

### 14. Other Species / Natural Disease

- **Orthologs:** Mouse *Tnrc6b* (NCBI Gene 213988) is orthologous to human *TNRC6B* (NCBI Gene 23112). The GW182/TNRC6 family is evolutionarily conserved across metazoans.
- **Natural disease / veterinary relevance:** No naturally occurring *TNRC6B* disease reported in companion animals or wildlife (OMIA search negative). *Not applicable.*
- **Zoonotic potential / cross-species transmission:** Not applicable (genetic disorder).

### 15. Model Organisms

- **Mouse (Mus musculus, NCBI Taxon 10090):** Constitutive knockouts of *Tnrc6a/b/c* established paralog-specific essentiality. *"TNRC6a mutants die at mid-gestation, while b- and c- deleted mice are born at a Mendelian ratio. However, the majority of TNRC6b and all TNRC6c mutants die within 24h after birth"* ([PMID: 28811219](https://pubmed.ncbi.nlm.nih.gov/28811219/)). Homozygous *Tnrc6b* loss is largely perinatal-lethal.
- **Phenotype recapitulation:** Current knockouts model gene essentiality and miRNA biology but **do not model the human heterozygous neurodevelopmental phenotype**; no heterozygous or conditional CNS *Tnrc6b* model of the NDD has been reported.
- **Other systems:** In vitro biochemical and cell-based systems (HEK293/HeLa; tethering and phase-separation assays) have defined TNRC6B's silencing and condensate functions ([PMID: 29576456](https://pubmed.ncbi.nlm.nih.gov/29576456/), [PMID: 19470757](https://pubmed.ncbi.nlm.nih.gov/19470757/)). Patient-derived iPSC/neuronal or organoid models are a logical but currently unreported resource.

---

## Mechanistic Model / Interpretation

The unifying model is **dosage-sensitive disruption of microRNA-mediated post-transcriptional gene regulation during neurodevelopment.** TNRC6B is a GW182-family scaffold that is one of the three structural pillars of miRISC. Its N-terminal GW/WG repeats tether multiple Argonaute molecules, enabling cooperative, multivalent engagement of miRNA-AGO complexes with target mRNAs and driving liquid-liquid phase separation into P-body-like condensates; its C-terminal silencing domain couples the complex to PABP and the CCR4-NOT deadenylase to effect repression. Losing one functional allele reduces scaffold concentration below the threshold required for robust silencing. Because neural stem-cell specification, neuronal differentiation, DICER-dependent miRNA production, and dendritic maturation all depend on this AGO2/TNRC6B/FMRP/MOV10 module in a stage-specific manner, haploinsufficiency plausibly perturbs the fine post-transcriptional tuning that cortical and neuronal development require — yielding the clinical NDD. The multisystem (craniofacial, skeletal, growth, skin, metabolic) features reflect the pleiotropy of miRNA regulation across tissues.

Two caveats temper this model. First, the patient-level link (steps 5→6 in the causal chain) is **inferred**: no patient neurons, transcriptomes, or methylation signatures have been profiled to show derepressed miRNA targets in vivo. Second, mouse genetics show the paralogs are **not redundant** and that homozygous loss is lethal, so the heterozygous, viable human disorder occupies a dosage window not yet modeled experimentally.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [32152250](https://pubmed.ncbi.nlm.nih.gov/32152250/) | *Pathogenic variants in TNRC6B…* (Granadillo 2020) | Foundational 17-patient cohort; core phenotype frequencies |
| [39115759](https://pubmed.ncbi.nlm.nih.gov/39115759/) | *Synonymous variant c.3141G>A altering splicing* | AD inheritance, OMIM 619243, LoF via exon skipping, diagnostic approach |
| [38404251](https://pubmed.ncbi.nlm.nih.gov/38404251/) | *Novel variants…café-au-lait, metabolic* (Yang 2024) | Expanded phenotype; de novo missense/frameshift variants |
| [29576456](https://pubmed.ncbi.nlm.nih.gov/29576456/) | *Phase transitions in human miRISC* | TNRC6B as core miRISC condensate component |
| [32661162](https://pubmed.ncbi.nlm.nih.gov/32661162/) | *Biochemical basis for cooperative miRNA action* | Multivalent TNRC6B scaffolding |
| [30086238](https://pubmed.ncbi.nlm.nih.gov/30086238/) | *GW182 scaffolding requirement* | GW182/TNRC6 required for miRNA activity |
| [17167072](https://pubmed.ncbi.nlm.nih.gov/17167072/) | *let-7 during neural specification* | TNRC6B in neural differentiation machinery |
| [34847178](https://pubmed.ncbi.nlm.nih.gov/34847178/) | *FMRP/MOV10 regulate Dicer1 & dendrites* | AGO2-module → dendrite development link |
| [28811219](https://pubmed.ncbi.nlm.nih.gov/28811219/) | *Tnrc6c essential in lung; Tnrc6 KO mice* | Paralog-specific mouse lethality |
| [41274961](https://pubmed.ncbi.nlm.nih.gov/41274961/) | *Precision diagnostics in rare NDDs* | Genetic testing recommended for all NDD |
| [42074582](https://pubmed.ncbi.nlm.nih.gov/42074582/) | *3-generation 22q13.1 deletion family* | Inherited transmission; variable expressivity |
| [37348364](https://pubmed.ncbi.nlm.nih.gov/37348364/) | *Epilepsy and ASD from TNRC6B variant* | Seizure/ASD presentation |
| [41147347](https://pubmed.ncbi.nlm.nih.gov/41147347/) | *TNRC6B + Xq28/MECP2 microdeletion* | Modifier effect; more severe phenotype |
| [19470757](https://pubmed.ncbi.nlm.nih.gov/19470757/) | *Functional dissection of human TNRC6* | Domain architecture; RRM/silencing domain |
| [19398495](https://pubmed.ncbi.nlm.nih.gov/19398495/) | *Mammalian GW182 Ago-binding sites* | Multiple AGO2-binding sites in N-terminus |
| [38300321](https://pubmed.ncbi.nlm.nih.gov/38300321/) | *WES in severe DLD (Swedish cohort)* | TNRC6B among diagnostic yield in language disorder |
| [42607197](https://pubmed.ncbi.nlm.nih.gov/42607197/) | *Craniosynostosis genetics* | TNRC6B among NDD-associated variants |

**Challenging/qualifying evidence:** [PMID: 25228304](https://pubmed.ncbi.nlm.nih.gov/25228304/) (TCF20/TNRC6B at a chr22 breakpoint) found **no significant association of TNRC6B mutations with ASD** in a screened family set, attributing the phenotype to TCF20 — an early signal that individual TNRC6B variants required careful causal validation, later provided by the Granadillo cohort and functional studies. [PMID: 31670606](https://pubmed.ncbi.nlm.nih.gov/31670606/) shows TNRC6 is **not required for silencing by fully complementary duplexes**, clarifying that the disease-relevant function is specifically **miRNA** (partial-complementarity) regulation, not all RNAi.

---

## Limitations and Knowledge Gaps

1. **Small evidence base:** Fewer than ~50–100 confirmed cases; phenotype frequencies rest heavily on one 17-patient cohort, limiting precision and generalizability.
2. **No patient-level molecular profiling:** No transcriptomic, proteomic, metabolomic, or DNA-methylation ("episignature") data from patients; the miRNA-derepression mechanism in human neurons is inferred, not demonstrated.
3. **No disease-specific animal model:** Existing *Tnrc6b* knockout mice are perinatal-lethal when homozygous and do not model the human heterozygous NDD; no conditional/heterozygous CNS model exists.
4. **Quantitative genetics unknown:** Penetrance and expressivity are not quantified; genotype-phenotype correlations (missense vs. truncating vs. deletion) are not established.
5. **Epidemiology absent:** No prevalence/incidence, no formal Orphanet estimate, no registry.
6. **Ontology/coding gaps:** No dedicated Orphanet/ICD/MeSH code identified; captured under broad NDD categories.
7. **No targeted therapy or trials:** Management is entirely supportive; no NCT-registered disease-specific interventions.

---

## Proposed Follow-up Experiments / Actions

1. **Build a patient registry / GeneMatcher cohort** to expand case numbers, refine phenotype frequencies, and quantify penetrance and expressivity.
2. **Generate patient-derived iPSC neurons/organoids** carrying LoF *TNRC6B* variants and perform RNA-seq/small-RNA-seq to test for predicted miRNA-target derepression and dendritic/differentiation defects.
3. **Create a conditional/heterozygous Tnrc6b mouse (or neuronal-specific knockdown)** to establish an NDD-relevant model and test behavioral, electrophysiological, and dendritic-morphology endpoints.
4. **Define a DNA-methylation episignature** across confirmed cases to aid VUS reclassification and clinical diagnosis.
5. **Systematic genotype-phenotype analysis** separating truncating, missense, splice, and 22q13.1-deletion subgroups, including assessment of second-site modifiers (e.g., concurrent *MECP2* loss).
6. **Functional validation pipeline** (minigene/RNA assays and tethering/silencing reporters) as a standard for reclassifying splice and synonymous VUS.
7. **Natural-history study** to document developmental trajectories, seizure risk, and growth/metabolic outcomes, informing anticipatory guidance and counseling.

---

*Report compiled from 25 reviewed papers and 9 confirmed findings across 5 investigation iterations. Evidence types span human clinical case series/reports, in vitro biochemistry and cell biology, and model-organism (mouse) genetics; mechanistic links between molecular dysfunction and clinical phenotype are explicitly flagged as inferred where direct patient-level data are lacking.*


## Artifacts

- [OpenScientist final report](TNRC6B-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TNRC6B-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:34847178` (6 mentions) - FMRP and MOV10 regulate Dicer1 expression and dendrite development.
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `tnrc6b`, `phenotype`, `gene`, `disorder`, `variant`, `deletion`, `q13`, `behavioral`, `seizure`, `disease`, `genetic`, `developmental`, `ndd`, `heterozygous`, `delay`, `growth`, `dominant`, `speech`, `human`, `adhd`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000750` (1 mention) - the report calls it "Static"; HP calls it **Delayed speech and language development**
- `HP:0010862` (1 mention) - the report calls it "Static"; HP calls it **Delayed fine motor development**
- `HP:0002194` (1 mention) - the report calls it "Static"; HP calls it **Delayed gross motor development**
- `HP:0007018` (1 mention) - the report calls it "Static"; HP calls it **Attention deficit hyperactivity disorder**
- `HP:0000708` (1 mention) - the report calls it "Variable"; HP calls it **Atypical behavior**
- `HP:0033127` (1 mention) - the report calls it "Static"; HP calls it **Abnormality of the musculoskeletal system**
- `HP:0001999` (1 mention) - the report calls it "Static"; HP calls it **Abnormal facial shape**
- `HP:0000252` (1 mention) - the report calls it "Static"; HP calls it **Microcephaly**
- `HP:0000957` (1 mention) - the report calls it "Stable"; HP calls it **Cafe-au-lait spot**
- `HP:0001250` (1 mention) - the report calls it "Variable/episodic"; HP calls it **Seizure**
- `HP:0001939` (1 mention) - the report calls it "Variable"; HP calls it **Abnormality of metabolism/homeostasis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000717` (1 mention) - the report calls it "Static"; HP calls it **Autism**
- `GO:0035195` (1 mention) - the report calls it "miRNA-mediated gene silencing"; GO calls it **miRNA-mediated post-transcriptional gene silencing**, and lists "miRNA-mediated gene silencing" among its other names
- `GO:0031047` (1 mention) - the report calls it "regulation of gene silencing by RNA"; GO calls it **regulatory ncRNA-mediated gene silencing**, and lists "gene silencing by RNA" among its other names
- `GO:0021954` (1 mention) - the report calls it "CNS neuron development"; GO calls it **central nervous system neuron development**
- `UBERON:0002204` (1 mention) - the report calls it "Secondary involvement:** Musculoskeletal system"; UBERON calls it **musculoskeletal system**