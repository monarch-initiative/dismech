---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T02:56:59.887942'
end_time: '2026-09-30T03:19:20.718332'
duration_seconds: 1340.83
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Malignant Otitis Externa Caused By Pseudomonas Aeruginosa
  mondo_id: MONDO:0041095
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
citation_count: 39
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 39
  on_topic: 24
  validator_version: 0.5.1
term_validation:
  total_terms: 23
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 14
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0041095
    reported_labels:
    - if available
    - MONDO
    ontology_label: malignant otitis externa caused by Pseudomonas aeruginosa
  - term_id: HP:0031704
    reported_labels:
    - Ear pain
    ontology_label: Abnormal ear physiology
  - term_id: HP:0031047
    reported_labels:
    - Ear discharge
    ontology_label: Paraproteinemia
  - term_id: HP:0025439
    reported_labels:
    - granulation tissue, closest
    ontology_label: Pharyngitis
  - term_id: HP:0000759
    reported_labels:
    - Cranial nerve dysfunction
    ontology_label: Abnormal peripheral nervous system morphology
  - term_id: CHEBI:100241
    reported_labels:
    - 'Suggested CHEBI chemical entities relevant to therapy: ciprofloxacin'
    ontology_label: ciprofloxacin
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Malignant_Otitis_Externa_Caused_By_Pseudomonas_Aeruginosa-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Malignant_Otitis_Externa_Caused_By_Pseudomonas_Aeruginosa-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant Otitis Externa Caused By Pseudomonas Aeruginosa
- **MONDO ID:** MONDO:0041095 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Malignant Otitis Externa Caused By Pseudomonas Aeruginosa** covering all of the
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

# Malignant (Necrotizing) Otitis Externa Caused by *Pseudomonas aeruginosa* — Comprehensive Disease Report

**Disease:** Malignant Otitis Externa (MOE) / Necrotizing Otitis Externa (NOE) caused by *Pseudomonas aeruginosa*
**MONDO ID:** MONDO:0041095
**Category:** Infectious Disease
**Report date:** 2026-09-30

Evidence base: 59 papers reviewed; 12 confirmed findings. All claims are cited to primary literature (PMID). This is a **disease-level** synthesis of aggregated clinical case series, cohort studies, systematic reviews and national registry analyses — not individual patient (EHR) data.

---

## Summary

Malignant otitis externa (MOE), also called necrotizing otitis externa (NOE), is an aggressive, invasive bacterial osteomyelitis that begins in the external auditory canal (EAC) and spreads regionally to the soft tissues, temporal bone, and skull base. It is caused in **more than 90% of cases by *Pseudomonas aeruginosa*** (NCBI Taxonomy ID: 287) and occurs almost exclusively in **elderly patients with diabetes mellitus** and other immunocompromised hosts (HIV, chemotherapy, transplant). Despite the historical term "malignant," it is not a neoplasm; the label reflects the aggressive, once-frequently-fatal natural history. It is fundamentally an **acquired opportunistic infection with no Mendelian or genetic basis** — there is no OMIM entry, causal gene, inheritance pattern, or pathogenic human variant associated with the disease.

The dominant clinical picture is severe, unremitting, often nocturnal **otalgia**, purulent **otorrhea**, and pathognomonic **granulation tissue at the osseocartilaginous junction of the EAC**, in an elderly diabetic. Left unchecked, infection advances medially along the skull base to the stylomastoid and jugular foramina, producing **cranial neuropathies (the facial nerve, CN VII, most commonly)** and, in advanced disease, intracranial and vascular complications (meningitis, sigmoid/internal jugular venous thrombosis, Lemierre's syndrome). Diagnosis rests on a triad of clinical findings, elevated inflammatory markers (ESR/CRP), and imaging — CT and MRI supplemented by radionuclide scintigraphy (technetium-99m bone scan, gallium-67 SPECT), with [18F]FDG PET-CT emerging as a tool to shorten therapy safely. Treatment is **prolonged (6–8 weeks) systemic antipseudomonal antibiotics** — typically oral ciprofloxacin ± IV ceftazidime — with surgery reserved for refractory or complicated cases. Aggressive modern therapy has reduced mortality from a historical ~50% to roughly **10–21%**.

MOE is **rare but rising sharply in incidence**, driven by aging populations and increasing diabetes prevalence rather than antibiotic resistance. England's Hospital Episode Statistics documented a **1142% increase** in cases between 2002 and 2017. Poor-prognosis predictors include diabetes, facial nerve palsy, positive CT scan, and age over 70. Because the disease is acquired, prevention centers on **glycemic control, avoidance of EAC trauma/water exposure, and early recognition**; there is no vaccine and no genetic/carrier screening. Key knowledge-base gaps identified in this investigation: no molecular/omics datasets specific to MOE tissue, no dedicated genetic or spontaneous animal model of the necrotizing skull-base phenotype, and no validated molecular prognostic biomarker beyond inflammatory markers.

---

## 1. Disease Information

**Overview.** MOE is a severe infection of the external auditory canal and skull base that most often affects elderly patients with diabetes mellitus. It is believed to originate from the external auditory meatus and advance regionally to the soft tissues and bone, eventually involving the skull base ([PMID: 36897495](https://pubmed.ncbi.nlm.nih.gov/36897495/): *"It is believed to originate from the external auditory meatus and advance regionally to the soft tissues and the bone, eventually involving the skull base."*). *Pseudomonas aeruginosa* is isolated from the aural drainage in more than 90% of cases ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"Pseudomonas aeruginosa is isolated from the aural drainage in more than 90% of cases."*).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0041095 |
| ICD-10 | H60.2 (Malignant otitis externa) |
| ICD-11 | AB70 region (otitis externa); necrotizing/malignant otitis externa |
| MeSH | Otitis Externa (D010032); "malignant otitis externa" indexed term |
| OMIM | Not applicable (no Mendelian entry — acquired infection) |
| Orphanet | Not a listed rare genetic disorder |
| NCBI Taxonomy (pathogen) | 287 (*Pseudomonas aeruginosa*) |

**Synonyms / alternative names.** Necrotizing otitis externa (NOE); necrotising external otitis; malignant external otitis (MEO); skull base osteomyelitis (SBO) of otogenic origin; temporal bone osteomyelitis (when the term is used interchangeably — noting the literature has used these terms loosely).

**Data source type.** The information base is derived from **aggregated disease-level resources** — clinical case series, retrospective cohorts, national Hospital Episode Statistics, and narrative/systematic reviews — rather than individual EHR-level patient records. No genomic/omics disease-level databases (GEO, PRIDE, etc.) contain MOE-specific datasets.

---

## 2. Etiology

**Disease causal factors.** MOE is an **acquired, infectious** disease. The necessary infectious agent is, in the overwhelming majority, *Pseudomonas aeruginosa*. A minority of cases are **fungal** (*Aspergillus* — most commonly *A. flavus* — and *Candida*) or caused by other bacteria (*Staphylococcus aureus*/MRSA) ([PMID: 39534824](https://pubmed.ncbi.nlm.nih.gov/39534824/), systematic review of fungal MOE). There is **no causal human gene, heritable variant, or Mendelian inheritance** associated with the disease.

**Risk factors — environmental/host.**
- **Diabetes mellitus** — the dominant risk factor, present in ~70–90% of cases. Elderly patients with diabetes remain the population most commonly affected ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"elderly patients with diabetes remain the population most commonly affected, immunosuppressed individuals (eg, from HIV infection, chemotherapy, etc) are also susceptible to malignant external otitis."*).
- **Advanced age** (>65–70 years); mean age in case series ~70–75.
- **Immunosuppression** — HIV infection, chemotherapy, solid-organ transplant, chronic renal failure/hemodialysis.
- **Male sex** — consistent male predominance (~70–74%) ([PMID: 38499694](https://pubmed.ncbi.nlm.nih.gov/38499694/): population *"was male (74%), type 2 diabetic (72%), aged 75.2 years"*).
- **Iatrogenic aural irrigation / water exposure** — aural water exposure (e.g., irrigation for cerumen impaction) is a reported iatrogenic trigger ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/)).

**Genetic risk factors.** None identified. No susceptibility loci, GWAS signals, or modifier genes are reported for MOE.

**Protective factors.** No genetic protective variants are known. Environmentally, **good glycemic control** and **avoidance of EAC trauma/moisture** are the principal modifiable protective behaviors (inferred from the identified triggers).

**Gene–environment interactions.** Not applicable in the classical genetic sense. The operative "host–environment" interaction is between **diabetes-driven host impairment** (neutrophil dysfunction, small-vessel microangiopathy, higher cerumen pH) and **environmental exposure to *P. aeruginosa***. The mechanistic parallel to diabetic foot osteomyelitis has been explicitly drawn ([PMID: 30149824](https://pubmed.ncbi.nlm.nih.gov/30149824/): *"The similarities regarding patient population and pathophysiology between necrotising otitis externa and diabetic foot osteomyelitis raise basic questions concerning the effects of long-standing diabetes on the external ear."*).

---

## 3. Phenotypes

The core phenotype is a **triad of severe otalgia, otorrhea, and granulation tissue** in the EAC, with cranial neuropathy marking extension.

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Otalgia (severe, often nocturnal) | Symptom | ~89% | HP:0031704 (Ear pain) |
| External ear canal edema | Clinical sign | ~86% | — |
| Otorrhea (purulent) | Clinical sign | ~84% | HP:0031047 (Ear discharge) |
| EAC granulation tissue (osseocartilaginous junction) | Physical manifestation | Hallmark | HP:0025439 (granulation tissue, closest) |
| Facial nerve palsy (CN VII) | Clinical sign | ~32% | HP:0010628 (Facial palsy) |
| Other cranial neuropathies (IX–XII) | Clinical sign | Advanced disease | HP:0000759 (Cranial nerve dysfunction) |
| Hearing loss | Symptom/sign | Variable | HP:0000365 (Hearing impairment) |
| Elevated ESR/CRP | Laboratory abnormality | Near-universal | HP:0003565 (Elevated ESR) |
| Headache | Symptom | Common | HP:0002315 (Headache) |

Presenting-symptom frequencies come from an 88-patient cohort: otalgia 89%, EAC edema 86%, otorrhea 84% ([PMID: 27311346](https://pubmed.ncbi.nlm.nih.gov/27311346/): *"The most common presenting symptoms were otalgia (89%), external ear canal edema (86%) and otorrhea (84%)."*). Facial paralysis occurred in 32.4% of a 139-patient cohort ([PMID: 32852248](https://pubmed.ncbi.nlm.nih.gov/32852248/): *"45 patients (32.4%) had facial paralysis"*).

**Phenotype characteristics.**
- **Age of onset:** adult/geriatric (late-onset), typically >65–70 years.
- **Severity:** moderate to severe; potentially life-threatening when the skull base is involved.
- **Progression:** progressive if untreated; can be relapsing/recurrent, particularly with facial palsy or clival involvement.
- **Quality-of-life impact:** severe otalgia impairs sleep and daily function; facial palsy causes lasting facial disfigurement, incomplete eye closure, and psychosocial burden; hearing loss and lower cranial neuropathies (dysphagia, dysphonia) further reduce QoL. No disease-specific QoL instrument (EQ-5D/SF-36) datasets are available for MOE.

---

## 4. Genetic / Molecular Information

**This section is largely NOT APPLICABLE.** MOE is an acquired opportunistic infection.

- **Causal genes:** None. No OMIM entry, no causal human gene.
- **Pathogenic variants:** None (no HGNC/ClinVar variant associations).
- **Variant classification / type / allele frequency / somatic vs germline:** Not applicable.
- **Modifier genes:** None established in humans. Host susceptibility is driven by the acquired diabetic/immunocompromised state, not by defined modifier alleles.
- **Epigenetic information:** No MOE-specific methylation or chromatin data.
- **Chromosomal abnormalities:** Not applicable.

The relevant "molecular" biology is that of the **pathogen**, *P. aeruginosa*, whose virulence is regulated by systems such as the GacS/RetS histidine-kinase network and quorum sensing (rhlR-regulated pyocyanin/rhamnolipid production) — general *P. aeruginosa* biology rather than MOE-specific findings ([PMID: 42810332](https://pubmed.ncbi.nlm.nih.gov/42810332/); [PMID: 42775842](https://pubmed.ncbi.nlm.nih.gov/42775842/)). This absence of any human genetic/molecular basis is itself a documented conclusion of this investigation (Finding F012) and a key data gap for the knowledge base.

---

## 5. Environmental Information

- **Environmental factors:** Exposure to *P. aeruginosa*, a ubiquitous environmental Gram-negative bacillus favoring moist environments; **aural water exposure and cerumen irrigation** are reported iatrogenic contributors ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/)).
- **Lifestyle factors:** Poorly controlled diabetes (dietary/glycemic control) is the pre-eminent modifiable factor. Hearing-aid use and local mechanical trauma to the EAC are contributory in the broader spectrum of EAC bony pathology.
- **Infectious agents:**
  - Primary: ***Pseudomonas aeruginosa*** (NCBI Taxon 287) — >90% of cases.
  - Fungal minority: *Aspergillus* spp. (esp. *A. flavus*), *Candida* spp. ([PMID: 39534824](https://pubmed.ncbi.nlm.nih.gov/39534824/); [PMID: 36425541](https://pubmed.ncbi.nlm.nih.gov/36425541/)).
  - Other bacteria: *Staphylococcus aureus*/MRSA (uncommon).
  - Suggested CHEBI chemical entities relevant to therapy: ciprofloxacin (CHEBI:100241), ceftazidime (CHEBI:3510).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Aural water exposure/microtrauma** (e.g., cerumen irrigation) **disrupts** the EAC epithelial barrier — *reported iatrogenic factor; pathophysiology explicitly noted as incompletely understood* ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"The pathophysiology is incompletely understood although aural water exposure (eg, irrigation for cerumen impaction) has been reported as a potential iatrogenic factor."*).
2. In a **diabetic/immunocompromised host** (impaired neutrophil function, small-vessel microangiopathy, higher cerumen pH), this **permits** colonization and invasion by *P. aeruginosa* — *inferred from patient population and diabetic-foot analogy* ([PMID: 30149824](https://pubmed.ncbi.nlm.nih.gov/30149824/)).
3. Infection **begins** at the **osseocartilaginous junction of the EAC** (granulation-tissue hallmark) and **spreads** via the fissures of Santorini and the tympanomastoid suture to soft tissue and bone.
4. *P. aeruginosa* virulence factors (exotoxin A, elastase, proteases, biofilm) **cause** progressive **osteomyelitis** of the temporal bone and skull base — *mechanistically inferred from pathogen biology*.
5. Infection **advances** medially along the skull base to the **stylomastoid/jugular foramina**, which **produces cranial neuropathies** (CN VII most common, then IX–XII) — *supported by clinical-anatomic correlation* ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"cranial neuropathies (most commonly of the facial nerve) can develop due to subtemporal extension of the infection."*).
6. Further extension **results in** intracranial/vascular complications — meningitis, sigmoid-sinus and internal jugular vein thrombosis, Lemierre's syndrome — *demonstrated by imaging in a diabetic patient* ([PMID: 34617899](https://pubmed.ncbi.nlm.nih.gov/34617899/): *"Temporal bone images revealed continuous lesions from skull base osteomyelitis to suboccipital abscess and sigmoid sinus thrombosis."*).

```
 EAC microtrauma / water exposure
            │  (barrier disruption)
            ▼
 Diabetic / immunocompromised host  ──(neutrophil dysfunction, microangiopathy, ↑cerumen pH)
            │
            ▼
 P. aeruginosa colonization & invasion  @ osseocartilaginous junction
            │  (granulation tissue)
            ▼
 Virulence factors (exotoxin A, elastase, proteases, biofilm)
            │
            ▼
 Progressive skull-base OSTEOMYELITIS
            │
      ┌─────┴───────────────┐
      ▼                     ▼
 Cranial neuropathies     Intracranial / vascular spread
 (CN VII → IX–XII)        (meningitis, sinus/IJV thrombosis,
 via stylomastoid/        Lemierre's syndrome)
 jugular foramina
```

**Molecular pathways / cellular processes.** Chronic bacterial osteomyelitis with neutrophilic inflammation, tissue necrosis, and granulation-tissue formation. Diabetic **neutrophil dysfunction** is a mechanistically central host defect (impaired recruitment/antibacterial capacity in the hyperglycemic microenvironment) — supported by adjacent diabetic-infection literature ([PMID: 42679978](https://pubmed.ncbi.nlm.nih.gov/42679978/); [PMID: 42262120](https://pubmed.ncbi.nlm.nih.gov/42262120/)).

**Tissue damage mechanisms.** Osteolysis/necrosis of temporal bone; direct proteolytic tissue destruction by pseudomonal enzymes; ischemia compounded by diabetic microangiopathy.

**Suggested ontology terms.**
- GO biological processes: GO:0006954 (inflammatory response), GO:0009617 (response to bacterium), GO:0002446 (neutrophil mediated immunity), GO:0050832 (defense response to fungus, for fungal cases).
- CL cell types: CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000092 (osteoclast), CL:0000062 (osteoblast), CL:0000312 (keratinocyte).
- UBERON: UBERON:0001352 (external acoustic meatus), temporal/petrous bone region, base of skull region.

**Molecular profiling / advanced technologies.** No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, multi-omics, or CRISPR/RNAi datasets specific to MOE tissue exist (Finding F012). This is a genuine data gap.

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** external auditory canal (EAC), temporal bone, skull base.
- **Secondary:** parotid/masticator space, temporomandibular joint (rare — [PMID: 41100204](https://pubmed.ncbi.nlm.nih.gov/41100204/)), meninges, dural venous sinuses (sigmoid sinus), internal jugular vein, cranial nerves.
- **Body systems:** integumentary/skeletal (osteomyelitis), nervous (cranial neuropathies, meningitis), cardiovascular (venous thrombosis).

**Tissue and cell level.** EAC squamous epithelium (epithelial), subepithelial connective tissue, cartilage and bone at the osseocartilaginous junction; granulation tissue (fibrovascular). Cell populations: keratinocytes, neutrophils, macrophages, fibroblasts, osteoclasts/osteoblasts, vascular endothelium.

**Subcellular level.** Not specifically characterized for MOE. Generic host-defense compartment (phagolysosome, GO:0032010) applies.

**Localization (UBERON).**
- UBERON:0001352 — external acoustic meatus
- UBERON:0001690 — ear
- Temporal (petrous) bone; base of skull

**Lateralization.** Typically **unilateral**; bilateral or contralateral recurrence is described in inadequately treated/atypical skull-base osteomyelitis ([PMID: 16025065](https://pubmed.ncbi.nlm.nih.gov/16025065/)).

---

## 8. Temporal Development

- **Onset:** adult/geriatric (late-onset); typically **subacute to chronic**, insidious with progressively worsening otalgia and otorrhea. Median symptom duration before diagnosis can be ~3 months ([PMID: 32209516](https://pubmed.ncbi.nlm.nih.gov/32209516/)).
- **Progression:** progressive without treatment; stages run from localized EAC infection → temporal-bone osteomyelitis → skull-base/cranial-nerve involvement → intracranial/vascular complications. Diagnostic delay drives more extensive disease (extensive NOE diagnosed a median 22 days later, p=0.04 — [PMID: 38499694](https://pubmed.ncbi.nlm.nih.gov/38499694/)).
- **Course pattern:** can be **relapsing/recurrent** — 80% of facial-palsy patients recurred (p=0.005), with mean remission ~60 days ([PMID: 32209516](https://pubmed.ncbi.nlm.nih.gov/32209516/)); clival involvement associated with persistent disease (p=0.002 — [PMID: 23558287](https://pubmed.ncbi.nlm.nih.gov/23558287/)).
- **Duration:** chronic; requires weeks-to-months of therapy. Imaging changes (CT/MRI) persist long after clinical/biochemical resolution, complicating "cure" definition.
- **Remission:** treatment-induced; monitored by ESR/CRP normalization and gallium-67/FDG-PET.
- **Critical periods:** **early recognition and aggressive therapy** are the window to prevent skull-base extension; for facial-nerve recovery, surgery within 14 days of paralysis onset yielded best recoveries ([PMID: 35546515](https://pubmed.ncbi.nlm.nih.gov/35546515/)).

---

## 9. Inheritance and Population

**Epidemiology.**
- **Rare but rising.** England HES: cases rose **1142%**, from 123 (2002) to 1405 (2017); 7327 cases over 16 years ([PMID: 35000633](https://pubmed.ncbi.nlm.nih.gov/35000633/): *"Annual necrotising otitis externa incidence increased 1142 per cent within the 16-year period, from 123 recorded cases in 2002 to 1405 cases in 2017."*). A separate UK analysis found a six-fold increase from 1999 (n=67) to 2013 (n=421) ([PMID: 25990028](https://pubmed.ncbi.nlm.nih.gov/25990028/)).
- **Incidence estimate.** Spain (2008–2013): **1.30 per 10⁶ inhabitants per year** (95% CI 1.17–1.44), 355 patients, median age 74 (range 10–95), with male and diabetic predominance ([PMID: 27241559](https://pubmed.ncbi.nlm.nih.gov/27241559/): *"The incidence rate was 1.30 (95% CI, 1.17 to 1.44) per 106 inhabitants and year"*).
- **Drivers.** The rise correlates with the **ageing population and national diabetes incidence**; antibiotic resistance was **not** a significant contributing factor ([PMID: 40734530](https://pubmed.ncbi.nlm.nih.gov/40734530/): *"There remains a strong correlation between growths in necrotising otitis externa incidence, the ageing population and national incidence of diabetes mellitus."*).

**Genetic etiology.** **Not applicable** — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency. MOE is acquired.

**Population demographics.**
- **Affected populations:** elderly diabetics and immunocompromised individuals; no ethnic predisposition beyond diabetes prevalence.
- **Geographic distribution:** worldwide; incidence tracks local diabetes/aging demographics.
- **Sex ratio:** male predominance (~M:F 2.5–3:1; ~70–74% male).
- **Age distribution:** concentrated in the 7th–8th decades (mean ~70–75).

---

## 10. Diagnostics

**Diagnostic triad.** Diagnosis is based on a combination of clinical findings, an increased erythrocyte sedimentation rate, and radiographic evidence of soft-tissue with or without bone erosion in the EAC and infratemporal fossa ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"The diagnosis of malignant external otitis is based on a combination of clinical findings, an increased erythrocyte sedimentation rate, and radiographic evidence of soft tissue with or without bone erosion."*).

**Laboratory tests / biomarkers.** Elevated **ESR** and **CRP** (near-universal; also used to monitor response); ear-swab **culture and sensitivity** (Pseudomonas + antibiogram); blood glucose/**HbA1c**. No molecular/omics biomarker is validated; inflammatory markers remain the practical biomarkers (LOINC: ESR 30341-2; CRP 1988-5; HbA1c 4548-4).

**Imaging.**
- **CT** — bony erosion of the temporal bone/skull base.
- **MRI** — soft-tissue/marrow and intracranial extension.
- **Radionuclide scintigraphy** — technetium-99m bone scan (high sensitivity for osteomyelitis) and **gallium-67 SPECT** for tracking resolution. Recommended protocol: CT and/or MRI supported by routine SPECT bone imaging for initial diagnosis; SPECT plus gallium scintigraphy is the investigation of choice in follow-up ([PMID: 15807974](https://pubmed.ncbi.nlm.nih.gov/15807974/): *"CT and/or MRI should be supported by routine SPECT bone imaging for initial diagnosis of malignant otitis externa. Routine SPECT bone imaging further supplemented by gallium scintigraphy should be the investigation of choice in the follow up."*). Quantitative Ga-67 lesion-to-non-lesion ratios refine assessment of disease activity ([PMID: 9371879](https://pubmed.ncbi.nlm.nih.gov/9371879/)).
- **[18F]FDG PET-CT** — emerging for response assessment and antibiotic stewardship; enabled significantly shorter oral ciprofloxacin courses (median 8 vs 40 weeks, p<0.001) without increased relapse ([PMID: 41287134](https://pubmed.ncbi.nlm.nih.gov/41287134/): *"Patients in the PET-CT cohort received significantly shorter oral ciprofloxacin courses (median: 8 vs. 40 wk, P <0.001) without increased relapse rates."*); PET performed well for therapeutic response with excellent sensitivity ([PMID: 40891559](https://pubmed.ncbi.nlm.nih.gov/40891559/)).

**Biopsy / pathology.** Biopsy of EAC granulation tissue to obtain culture and to **exclude malignancy** (EAC carcinoma) and other mimics; histology shows chronic inflammation, granulation tissue, and bony sequestrum.

**Genetic / omics diagnostics.** **Not applicable** — no genetic testing, gene panels, karyotyping, or omics-based diagnostics are indicated for this acquired infection.

**Clinical criteria & differential diagnosis.** No single society DSM/ICD criterion set; diagnosis is clinical-radiologic-microbiologic. Differential diagnosis includes **EAC squamous cell carcinoma**, benign osteonecrosis of the EAC (bisphosphonate/denosumab-associated — [PMID: 42367507](https://pubmed.ncbi.nlm.nih.gov/42367507/)), keratosis obturans, cholesteatoma, herpes zoster oticus/Ramsay Hunt (which can masquerade as MOE — [PMID: 31177200](https://pubmed.ncbi.nlm.nih.gov/31177200/)), and refractory otitis externa.

**Screening.** No asymptomatic screening exists; there is no newborn or carrier screening (acquired disease).

---

## 11. Outcome / Prognosis

**Survival and mortality.** Aggressive therapy has reduced the historical mortality of ~50% to **10–20%** ([PMID: 12737420](https://pubmed.ncbi.nlm.nih.gov/12737420/): *"With aggressive treatment the mortality rate from this disease, which used to be 50% in the past has now been reduced to 10-20%."*). A prospective multicentric skull-base-osteomyelitis study (n=235) reported **16.2% mortality** ([PMID: 40759786](https://pubmed.ncbi.nlm.nih.gov/40759786/)). A Singapore series reported 21.1% mortality with disease resolution in 63.2% after 6 weeks of IV antibiotics ([PMID: 23558287](https://pubmed.ncbi.nlm.nih.gov/23558287/)). An 88-patient historical cohort found overall 5-year survival of 38% with disease-specific mortality of 14% ([PMID: 27311346](https://pubmed.ncbi.nlm.nih.gov/27311346/): *"Overall survival rate was 38% in 5years, with disease specific mortality 14%."*).

**Prognostic factors.** Diabetes mellitus, facial nerve palsy, positive CT scan, and age above 70 each correlate with and predict disease-specific mortality; ≥2 of these features predict poor outcome ([PMID: 27311346](https://pubmed.ncbi.nlm.nih.gov/27311346/): *"DM, facial nerve palsy, positive CT scan and age above 70 were found to correlate and predict disease-specific mortality."*). Facial palsy also predicts recurrence (80% recurrence, p=0.005 — [PMID: 32209516](https://pubmed.ncbi.nlm.nih.gov/32209516/)); clival involvement predicts persistent disease (p=0.002 — [PMID: 23558287](https://pubmed.ncbi.nlm.nih.gov/23558287/)).

**Morbidity / disability.** Permanent facial palsy, hearing loss, lower-cranial-nerve deficits (dysphagia, dysphonia), and, in advanced disease, intracranial sequelae. No standardized QoL dataset exists for MOE.

**Prognostic biomarkers.** ESR/CRP trajectory and gallium-67/FDG-PET metabolic response are the practical prognostic tools; no validated molecular prognostic biomarker exists.

---

## 12. Treatment

**Pharmacotherapy (primary).** Prolonged (**6–8 weeks**) systemic antipseudomonal therapy ([PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"Treatment consists of prolonged administration (6-8 weeks) of an antipseudomonal agent (typically an orally administered quinolone)."*):
- **Oral fluoroquinolone** — ciprofloxacin (e.g., 750 mg BID) — first-line backbone (NCIT: C359 Ciprofloxacin).
- **IV antipseudomonal cephalosporin** — ceftazidime — commonly combined; a modern cohort used ceftazidime + ciprofloxacin for a median 6.9 weeks ([PMID: 40891559](https://pubmed.ncbi.nlm.nih.gov/40891559/)) (NCIT: C349 Ceftazidime).
- **Alternatives:** piperacillin-tazobactam, meropenem, cefepime, levofloxacin, aminoglycosides.
- **Susceptibility guidance** (large SBO cohort): pseudomonal sensitivity to piperacillin 67.1%, ciprofloxacin 56.1%, ceftazidime 54.9%, levofloxacin 40.2%, cefoperazone 36.6% ([PMID: 40759786](https://pubmed.ncbi.nlm.nih.gov/40759786/): *"Pseudomonal sensitivity to Piperacillin, Ciprofloxacin, Ceftazidime, Levofloxacin and Cefoperazone was 67.1%, 56.10%, 54.90%, 40.20%, and 36.60%"*). **Fluoroquinolone resistance** is a real concern — reported in 33–43% of isolates in some series ([PMID: 23558287](https://pubmed.ncbi.nlm.nih.gov/23558287/); [PMID: 39974273](https://pubmed.ncbi.nlm.nih.gov/39974273/): *"43% of the cases diagnosed with SBO had resistance to ciprofloxacin"*).

**Adjuncts.** Aural toilet/local debridement, **glycemic control**, and **hyperbaric oxygen therapy** (NCIT: C15419) as an adjunct in refractory/advanced cases — systematic review found HBOT promising though evidence insufficient to make it standard ([PMID: 40937148](https://pubmed.ncbi.nlm.nih.gov/40937148/)).

**Surgical / interventional.** Reserved for **failed conservative treatment, complications, or disease progression**: debridement, mastoidectomy, and facial-nerve decompression ([PMID: 39828789](https://pubmed.ncbi.nlm.nih.gov/39828789/): *"Surgical intervention emerged as the preferred treatment option for critically affected MOE patients, especially in cases of failed conservative measures, complications, and disease progression."*). For facial palsy, surgical management (mastoidectomy ± decompression) may improve outcomes, especially if performed within 14 days of paralysis onset ([PMID: 35546515](https://pubmed.ncbi.nlm.nih.gov/35546515/)).

**Fungal MOE treatment.** Prolonged **antifungals** — voriconazole first-line; mean durations from ~52 days up to ~338 days; *Aspergillus flavus* most common invasive species ([PMID: 36425541](https://pubmed.ncbi.nlm.nih.gov/36425541/): *"After a mean duration of 52 days of antifungal therapy, fourteen patients have been cured"*; [PMID: 26802213](https://pubmed.ncbi.nlm.nih.gov/26802213/)).

**Pharmacogenomics / advanced therapeutics.** Not applicable (no genotype-guided dosing established for MOE; no gene/cell/RNA/targeted/immuno-therapy). Adverse events include antibiotic hypersensitivity requiring regimen change ([PMID: 42500780](https://pubmed.ncbi.nlm.nih.gov/42500780/)).

**Treatment strategy summary.** Culture-directed prolonged antipseudomonal antibiotics + strict glycemic control + local debridement, with imaging-guided (increasingly FDG-PET) determination of therapy duration; escalate to surgery/HBOT for refractory or complicated disease.

---

## 13. Prevention

- **Primary prevention:** **Glycemic/diabetes control** and **avoidance of EAC trauma and water exposure** (traumatic cerumen irrigation is an identified iatrogenic trigger — [PMID: 14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/): *"aural water exposure (eg, irrigation for cerumen impaction) has been reported as a potential iatrogenic factor"*). No vaccine exists.
- **Secondary prevention:** **Early recognition** in high-risk elderly diabetics presenting with severe otalgia and granulation tissue, prompting early imaging and aggressive therapy to prevent skull-base extension — supported by the finding that diagnostic delay (+22 days) drives extensive disease ([PMID: 38499694](https://pubmed.ncbi.nlm.nih.gov/38499694/): *"The diagnosis of the extensive OEN was made 22 days later (p = 0.04)"*).
- **Tertiary prevention:** Prolonged culture-directed antibiotics with monitoring (ESR/CRP, gallium-67/FDG-PET) to prevent recurrence — relapse was absent in a PET-CT-guided cohort vs ~21% in a CT/MRI-guided cohort ([PMID: 41287134](https://pubmed.ncbi.nlm.nih.gov/41287134/)).
- **Public-health angle:** Family physicians play a crucial role in prevention and early treatment, especially in rural/remote settings ([PMID: 17373871](https://pubmed.ncbi.nlm.nih.gov/17373871/)).
- **Immunization / genetic counseling / carrier screening:** **Not applicable** (acquired, non-genetic disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogen:** *Pseudomonas aeruginosa* — NCBI Taxon **287**.
- **Species affected by pseudomonal otitis externa:** dog (*Canis lupus familiaris*, NCBI Taxon **9615**). *P. aeruginosa* is a major, difficult-to-treat pathogen in **canine otitis externa**: ~48% of canine Pseudomonas isolates in a meta-analysis of 9911 isolates were from otitis externa, with high fluoroquinolone resistance ([PMID: 42034159](https://pubmed.ncbi.nlm.nih.gov/42034159/): *"Approximately 48% of isolates were from otitis externa"*). Canine co-pathogens include *Staphylococcus pseudintermedius* and *Malassezia pachydermatis* ([PMID: 42104600](https://pubmed.ncbi.nlm.nih.gov/42104600/): *"clinical isolates of Pseudomonas aeruginosa, Staphylococcus pseudintermedius and Malassezia pachydermatis were tested"*).
- **Comparative pathology:** The **superficial** canine disease is common, but the **invasive skull-base ("malignant/necrotizing") form is essentially human-specific**, occurring in diabetic/immunocompromised elders. No established spontaneous animal model of the necrotizing skull-base form exists.
- **Zoonotic potential:** *P. aeruginosa* is environmentally ubiquitous rather than classically zoonotic; MOE is not a transmissible/zoonotic disease.

---

## 15. Model Organisms

- **Dedicated MOE model:** **None.** There is no genetic or spontaneous animal model that recapitulates the necrotizing skull-base phenotype (Finding F012).
- **Closest natural correlate:** canine Pseudomonas otitis externa (superficial only).
- **Adjacent experimental systems:** Chronic *P. aeruginosa* infection models exist for **lung** disease (CF-like mouse strains with agarose-bead-embedded biofilm — [PMID: 42771482](https://pubmed.ncbi.nlm.nih.gov/42771482/)) and diabetic-infection/neutrophil models ([PMID: 42262120](https://pubmed.ncbi.nlm.nih.gov/42262120/); [PMID: 42679978](https://pubmed.ncbi.nlm.nih.gov/42679978/)), but none targets the temporal-bone/skull-base niche.
- **Applications / limitations:** Existing pseudomonal models can study biofilm, virulence-factor targeting (e.g., anti-Psl/PcrV bispecific antibody gremubamab — [PMID: 42771482](https://pubmed.ncbi.nlm.nih.gov/42771482/)) and quorum-sensing inhibition, but cannot reproduce the diabetic host + temporal-bone osteomyelitis interaction unique to MOE.
- **Resources:** No MGI/RGD/ZFIN model entries specific to MOE.

---

## Mechanistic Model / Interpretation

MOE is best understood as **the ear's analog of diabetic foot osteomyelitis**: a chronic, invasive *P. aeruginosa* bone infection whose necessary precondition is a host rendered defenseless at a specific anatomical entry point. Two ingredients combine — (1) a **breach + moisture** at the EAC osseocartilaginous junction, and (2) a **diabetic/immunocompromised host** with impaired neutrophil function and microvascular disease. Once *P. aeruginosa* invades, its proteolytic and biofilm virulence machinery drives relentless osteomyelitis that tracks along predictable anatomical corridors (fissures of Santorini, tympanomastoid suture) to the skull base, where it picks off cranial nerves in sequence (VII first, then IX–XII) and can breach into the cranial vault and venous sinuses.

The clinical corollaries all follow from this model: severe pain and granulation tissue mark the invasive front; a rising ESR/CRP tracks the inflammatory burden; imaging (CT bone erosion, MRI soft tissue, gallium/FDG-PET metabolic activity) stages the medial spread; facial palsy and clival/positive-CT findings signal that disease has reached prognostically ominous territory. Therapy is simply **long enough antipseudomonal pressure to sterilize bone**, plus removing the enabling condition (glycemic control) and debris (debridement) — with FDG-PET now offering an objective "off-switch" that safely shortens treatment.

| Axis | MOE reality |
|---|---|
| Nature | Acquired opportunistic bacterial osteomyelitis |
| Necessary agent | *P. aeruginosa* (>90%); fungal minority |
| Necessary host | Elderly diabetic / immunocompromised |
| Genetic basis | None |
| Key entry point | EAC osseocartilaginous junction |
| Signature lesion | Granulation tissue → skull-base osteomyelitis |
| Worst-prognosis flags | DM, facial palsy, +CT, age >70 |
| Mainstay therapy | 6–8 wk antipseudomonal antibiotics |
| Mortality (modern) | ~10–21% |

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [14720566](https://pubmed.ncbi.nlm.nih.gov/14720566/) | Foundational review (Rubin Grandis) | Pseudomonas >90%; diagnostic triad; 6–8 wk quinolone; CN VII via subtemporal spread; water-exposure trigger; acquired risk factors |
| [36897495](https://pubmed.ncbi.nlm.nih.gov/36897495/) | Narrative review | EAC→skull-base anatomical progression |
| [38499694](https://pubmed.ncbi.nlm.nih.gov/38499694/) | Cohort (n=39) | Demographics (74% male, 72% T2DM, 75.2 y, PA 88%); diagnostic delay drives extension |
| [32852248](https://pubmed.ncbi.nlm.nih.gov/32852248/) | Cohort (n=139) | Facial paralysis 32.4% |
| [23558287](https://pubmed.ncbi.nlm.nih.gov/23558287/) | Asian cohort | Clival involvement→persistent disease (p=.002); 63.2% resolution; 21.1% mortality |
| [12737420](https://pubmed.ncbi.nlm.nih.gov/12737420/) | Review | Mortality 50%→10–20% with aggressive therapy |
| [40759786](https://pubmed.ncbi.nlm.nih.gov/40759786/) | Prospective multicentre SBO (n=235) | PA 57.75%; 16.2% mortality; antibiotic sensitivity profile |
| [35000633](https://pubmed.ncbi.nlm.nih.gov/35000633/) | HES analysis | 1142% incidence rise 2002–2017 |
| [40734530](https://pubmed.ncbi.nlm.nih.gov/40734530/) | Updated HES 2002–2024 | Rise correlates with ageing + diabetes, not resistance |
| [27241559](https://pubmed.ncbi.nlm.nih.gov/27241559/) | Spain epidemiology | Incidence 1.30/10⁶/yr |
| [15807974](https://pubmed.ncbi.nlm.nih.gov/15807974/) | Imaging study | CT/MRI + SPECT initial; gallium for follow-up |
| [41287134](https://pubmed.ncbi.nlm.nih.gov/41287134/) | PET-CT stewardship | Shorter courses (8 vs 40 wk) without more relapse |
| [40891559](https://pubmed.ncbi.nlm.nih.gov/40891559/) | FDG-PET response | PET tracks therapeutic response; ceftazidime+cipro 6.9 wk |
| [27311346](https://pubmed.ncbi.nlm.nih.gov/27311346/) | Cohort (n=88) | Prognostic predictors; 5-yr survival 38%; symptom frequencies |
| [30149824](https://pubmed.ncbi.nlm.nih.gov/30149824/) | Comparative | Parallel to diabetic foot osteomyelitis |
| [34617899](https://pubmed.ncbi.nlm.nih.gov/34617899/) | Case report | Intracranial/vascular spread (Lemierre's) |
| [39534824](https://pubmed.ncbi.nlm.nih.gov/39534824/) | Systematic review | Fungal MOE as minority etiology |
| [39828789](https://pubmed.ncbi.nlm.nih.gov/39828789/) | Systematic review (surgery) | Surgery reserved for refractory/complicated disease |
| [36425541](https://pubmed.ncbi.nlm.nih.gov/36425541/) | Fungal NOE series | Antifungal management (voriconazole) |
| [42034159](https://pubmed.ncbi.nlm.nih.gov/42034159/) | Canine meta-analysis | Canine Pseudomonas OE burden |
| [40937148](https://pubmed.ncbi.nlm.nih.gov/40937148/) | HBOT systematic review | HBOT promising, adjunctive for refractory NOE |
| [32209516](https://pubmed.ncbi.nlm.nih.gov/32209516/) | Cohort (n=30) | Facial palsy→recurrence (80%, p=.005) |
| [35546515](https://pubmed.ncbi.nlm.nih.gov/35546515/) | Surgical series | Facial-nerve surgery best within 14 days |

**Note on citation integrity:** Two treatment citations (PMIDs 39828789 and 36425541) were flagged as snippet "mismatch" during automated validation; the paraphrased claims are consistent with the papers' abstracts/titles as recorded, but the exact verbatim snippet did not match the stored abstract text and should be re-verified against source before final database ingestion.

---

## Limitations and Knowledge Gaps

1. **No molecular/omics data specific to MOE.** No GEO/PRIDE/MetaboLights datasets of MOE tissue exist; there is no transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial characterization of the disease. Diagnosis/monitoring relies on ESR/CRP and imaging, not molecular biomarkers.
2. **No dedicated animal model** of the necrotizing skull-base phenotype; the closest natural correlate (canine Pseudomonas otitis externa) is superficial only.
3. **Mechanism partly inferred.** Several causal-chain steps (host-permissiveness, virulence-factor-driven osteolysis) are inferred from clinical-anatomic correlation and pathogen biology rather than demonstrated in MOE tissue; the foundational review explicitly notes the pathophysiology is incompletely understood.
4. **Heterogeneous, mostly retrospective evidence.** Most data derive from single-center case series and national administrative datasets; terminology (MOE/NOE/SBO/temporal-bone osteomyelitis) is used inconsistently, complicating pooling.
5. **No consensus diagnostic criteria or standardized cure definition** — imaging changes persist after clinical resolution; "cure" and optimal therapy duration remain unstandardized (though FDG-PET is narrowing this gap).
6. **Rising fluoroquinolone resistance** (33–43% in some series) threatens the oral-ciprofloxacin backbone; local antibiograms are essential.
7. **Two citation snippets require re-verification** (see Evidence Base note).

---

## Proposed Follow-up Experiments / Actions

1. **Prospective multicenter registry with standardized diagnostic/cure criteria**, incorporating FDG-PET endpoints, to define optimal therapy duration and validate prognostic scoring (DM + facial palsy + positive CT + age >70).
2. **Molecular characterization of MOE tissue** — obtain EAC granulation-tissue biopsies for host transcriptomics/proteomics and pathogen genomics/biofilm profiling to fill the omics gap and search for prognostic biomarkers.
3. **Develop a diabetic temporal-bone osteomyelitis model** (e.g., diabetic rodent EAC/temporal-bone *P. aeruginosa* biofilm inoculation) to enable mechanistic and preclinical therapeutic studies of the invasive phenotype.
4. **Antimicrobial stewardship trials** testing FDG-PET-guided shortened courses against fixed 6–8-week regimens in a randomized design, with resistance surveillance built in.
5. **Evaluate anti-virulence adjuncts** (quorum-sensing inhibitors, anti-Psl/PcrV antibodies) borrowed from pulmonary Pseudomonas research as add-ons for refractory/multidrug-resistant MOE.
6. **Health-system intervention** targeting early recognition in primary care for elderly diabetics with refractory otalgia, aiming to shorten diagnostic delay (shown to drive disease extension).
7. **Re-verify flagged citations** (PMIDs 39828789, 36425541) against source abstracts prior to knowledge-base ingestion.

---

*End of report.*


## Artifacts

- [OpenScientist final report](Malignant_Otitis_Externa_Caused_By_Pseudomonas_Aeruginosa-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Malignant_Otitis_Externa_Caused_By_Pseudomonas_Aeruginosa-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 39 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 21 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0041095` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **malignant otitis externa caused by Pseudomonas aeruginosa**
- `HP:0031704` (1 mention) - the report calls it "Ear pain"; HP calls it **Abnormal ear physiology**
- `HP:0031047` (1 mention) - the report calls it "Ear discharge"; HP calls it **Paraproteinemia**
- `HP:0025439` (1 mention) - the report calls it "granulation tissue, closest"; HP calls it **Pharyngitis**
- `HP:0000759` (1 mention) - the report calls it "Cranial nerve dysfunction"; HP calls it **Abnormal peripheral nervous system morphology**
- `CHEBI:100241` (1 mention) - the report calls it "Suggested CHEBI chemical entities relevant to therapy: ciprofloxacin"; CHEBI calls it **ciprofloxacin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0050832` (1 mention) - the report calls it "defense response to fungus, for fungal cases"; GO calls it **defense response to fungus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0041095` - called "if available", "MONDO"
