---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T02:23:14.494885'
end_time: '2026-09-04T02:42:05.755191'
duration_seconds: 1131.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental And Epileptic Encephalopathy 80
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
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 24
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 15
  relevance_assessed: 26
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - 72% (IGD cohort)
    ontology_label: Hypotonia
  - term_id: HP:0100022
    reported_labels:
    - 64% (IGD cohort)
    ontology_label: Abnormality of movement
  - term_id: HP:0002126
    reported_labels:
    - 2/~16 (PIGB)
    ontology_label: Polymicrogyria
  - term_id: HP:0003155
    reported_labels:
    - Most
    ontology_label: Elevated circulating alkaline phosphatase concentration
  - term_id: HP:0001999
    reported_labels:
    - 82% (IGD cohort), variable
    ontology_label: Abnormal facial shape
  - term_id: UBERON:0002298
    reported_labels:
    - brainstem tegmentum, central tegmental tract region
    ontology_label: brainstem
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Developmental_And_Epileptic_Encephalopathy_80-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Developmental_And_Epileptic_Encephalopathy_80-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental And Epileptic Encephalopathy 80
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental And Epileptic Encephalopathy 80** covering all of the
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

# Developmental and Epileptic Encephalopathy 80 (DEE80 / PIGB-related GPI Deficiency): A Comprehensive Disease Report

## Summary

**Developmental and Epileptic Encephalopathy 80 (DEE80; OMIM #618580; also EIEE80, GPI biosynthesis defect 21)** is an ultra-rare, autosomal-recessive **inherited glycosylphosphatidylinositol (GPI) deficiency disorder (IGD)** caused by biallelic loss-of-function variants in **PIGB** (phosphatidylinositol glycan anchor biosynthesis class B; HGNC:8959; chromosome 15q21.3). PIGB encodes the endoplasmic-reticulum mannosyltransferase that transfers the **third mannose** to the growing GPI core glycan. Because roughly 150 human cell-surface proteins are attached to the plasma membrane through a GPI anchor — many of them adhesion, guidance and signaling molecules essential for brain development — the loss of PIGB function reduces surface presentation of all of them simultaneously. The clinical consequence is a severe neurodevelopmental disorder combining **early-onset, often intractable epilepsy**, **global developmental delay/intellectual disability**, **hypotonia**, **axonal peripheral neuropathy**, variable **brain malformations** (polymicrogyria, hypomyelination) and, in most patients, **elevated serum alkaline phosphatase (hyperphosphatasia)**, with high mortality in early childhood in severe cases.

The disease was first delineated by Murakami et al. in 2019, who described 10 unrelated families with biallelic PIGB mutations; all affected individuals had seizures, most had developmental/intellectual delay, and eight children died before four years of age. Subsequent case reports (e.g., Schiavoni 2021) and large cross-gene IGD cohorts (Bellai-Dussault 2019; Sidpra 2024) have broadened the phenotypic spectrum from lethal neonatal encephalopathy to milder presentations with survival into later childhood, and have defined a shared neuroimaging signature including cerebral/cerebellar atrophy and symmetric restricted diffusion of the **central tegmental tracts**.

This report synthesizes eight confirmed findings and 29 reviewed papers into a coherent mechanistic and clinical picture. The two most mechanistically satisfying insights are: (1) **why serum alkaline phosphatase is elevated** — PIGB deficiency accumulates an *incomplete but mannose-bearing* GPI that the transamidase still attaches to, resulting in secretion (shedding) rather than membrane anchoring of tissue-nonspecific alkaline phosphatase (TNAP); and (2) **why vitamin B6 partially helps seizures** — TNAP is the ectoenzyme that dephosphorylates circulating pyridoxal-5′-phosphate (PLP), so perturbed surface TNAP disturbs vitamin B6 handling, providing a biochemical rationale for supraphysiologic pyridoxine/PLP supplementation. There is no cure; management is supportive with mechanism-based, partially effective high-dose pyridoxine/pyridoxal-5′-phosphate for seizures.

---

## 1. Disease Information

**Overview.** DEE80 is a Mendelian, autosomal-recessive congenital disorder of glycosylation belonging to the inherited GPI deficiency (IGD) subgroup. It is a developmental and epileptic encephalopathy — meaning both the underlying developmental disturbance and the recurrent epileptic activity contribute to the encephalopathy — of prenatal/early-infantile onset.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #618580 (Developmental and epileptic encephalopathy 80) |
| Gene | PIGB — OMIM *604122; HGNC:8959; NCBI Gene 9488; Ensembl ENSG00000069943; UniProt Q92521 |
| Locus | 15q21.3 |
| Suggested MONDO | Inherited GPI deficiency / DEE80 (MONDO term for EIEE80) |
| ICD-11 | 8A61 (Developmental and epileptic encephalopathies) — closest applicable code |
| Inheritance | Autosomal recessive |

**Synonyms / alternative names:** EIEE80 (Epileptic encephalopathy, early infantile, 80); Developmental and epileptic encephalopathy 80; PIGB-related GPI biosynthesis defect; GPI biosynthesis defect 21 (GPIBD21); PIGB-CDG. Note that a broader allelic spectrum exists: biallelic *PIGB* variants have also been linked to **Acrofrontofacionasal dysostosis type 1 (AFFND1)** ([PMID: 34400385](https://pubmed.ncbi.nlm.nih.gov/34400385/)), and a distinct constitutional *PIGB* mechanism can predispose to **paroxysmal nocturnal hemoglobinuria (PNH)** via somatic copy-number-neutral loss of heterozygosity ([PMID: 33216889](https://pubmed.ncbi.nlm.nih.gov/33216889/)).

**Source of information.** Disease-level aggregated resources (OMIM, Orphanet) combined with individual-patient primary literature (case series and cohort studies). The founding evidence is individual-patient data from ~16 affected individuals across 10 families ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)), augmented by cross-gene IGD cohorts of 202 ([PMID: 30054924](https://pubmed.ncbi.nlm.nih.gov/30054924/)) and 83 individuals ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)).

---

## 2. Etiology

**Primary cause — genetic (Finding F001).** DEE80 is caused exclusively by **biallelic (homozygous or compound heterozygous) pathogenic variants in PIGB**. Murakami et al. (2019) described ten unrelated families each carrying different PIGB mutations (10 distinct variants), and demonstrated by flow cytometry that blood cells and fibroblasts had **decreased cell-surface GPI-anchored proteins**, confirming causality.

> "We describe ten unrelated families with bi-allelic mutations in PIGB, a gene that encodes phosphatidylinositol glycan class B, which transfers the third mannose to the GPI." — [PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)

> "Flow cytometric analysis of blood cells and fibroblasts from the affected individuals showed decreased cell surface presence of GPI-anchored proteins." — [PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)

**Genetic risk factors.** The only established risk factor is inheritance of two damaging PIGB alleles. Consanguinity increases risk of homozygosity (several reported families are consanguineous). No common susceptibility loci or GWAS signals apply — this is a monogenic disorder.

**Environmental / infectious factors.** No environmental, toxic, infectious, or lifestyle cause contributes to disease onset. As with other IGDs, **fever and intercurrent infection can worsen seizures** and precipitate status epilepticus (documented in the related PIGW disorder, [PMID: 38055078](https://pubmed.ncbi.nlm.nih.gov/38055078/)), but these are triggers of symptoms, not causes of disease.

**Protective factors.** None genetically defined. Supraphysiologic vitamin B6 (pyridoxine/pyridoxal-5′-phosphate) mitigates seizures in a subset (see Treatment).

**Gene–environment interactions.** Limited; the principal clinically relevant interaction is fever/infection as a seizure-provoking factor superimposed on the genetic lesion.

---

## 3. Phenotypes

DEE80 phenotypes span neurological, metabolic and multisystem domains. Frequencies below combine the founding PIGB cohort ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)), a milder single case ([PMID: 34161862](https://pubmed.ncbi.nlm.nih.gov/34161862/)), and cross-gene IGD cohorts ([PMID: 30054924](https://pubmed.ncbi.nlm.nih.gov/30054924/); [PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)).

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Seizures / epilepsy | Clinical sign | Early infantile (median ~6 mo in IGDs) | ~100% (PIGB cohort); 83% (IGD cohort) | HP:0001250 (Seizure); HP:0011097 (Epileptic spasms) |
| Global developmental delay / intellectual disability | Clinical sign | Congenital/infantile | Most; 90% (IGD cohort) | HP:0001263; HP:0001249 |
| Hypotonia | Clinical sign | Infantile | 72% (IGD cohort) | HP:0001252 |
| Motor symptoms | Clinical sign | Infantile | 64% (IGD cohort) | HP:0100022 |
| Peripheral (axonal) neuropathy | Clinical sign | Childhood | 4/~16 (PIGB) | HP:0000762; HP:0003477 |
| Polymicrogyria | Physical/imaging | Congenital | 2/~16 (PIGB) | HP:0002126 |
| Hypomyelination | Imaging | Congenital/infantile | Reported (milder case) | HP:0006808 |
| Elevated alkaline phosphatase (hyperphosphatasia) | Laboratory | Congenital | Most | HP:0003155 |
| 2-oxoglutaric aciduria | Laboratory | — | 2 severe cases (PIGB) | HP:0003355 (Organic aciduria) |
| Scoliosis | Physical | Childhood | Reported (milder case) | HP:0002650 |
| Foot deformity (equino-varo-cavus) | Physical | Childhood | Reported (milder case) | HP:0001760 |
| Dysmorphic features | Physical | Congenital | 82% (IGD cohort), variable | HP:0001999 |
| Early mortality | Outcome | <4 years | 8 children (PIGB); 15/83 (IGD) | — |

**Phenotype characteristics (Finding F002).** In the founding cohort, "most of the affected individuals have global developmental and/or intellectual delay, all had seizures, two had polymicrogyria, and four had a peripheral neuropathy. Eight children passed away before four years old" ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)). Two severely affected individuals showed **2-oxoglutaric aciduria**, indicating a metabolic derangement in the most severe end of the spectrum. Two individuals carried a clinical diagnosis of **DOORS syndrome** (Deafness, Onycho-Osteodystrophy, mental Retardation, Seizures) before the molecular cause was known.

Severity is **variable**. Schiavoni et al. (2021) reported the milder end: "severe global developmental delay with absent speech, mixed peripheral polyneuropathy, hypotonia, bilateral equino-varo-supinated-cavus foot, early-onset scoliosis, elevated serum alkaline phosphatase and a single episode of febrile status epilepticus. Hypomyelination was documented on brain MRI" ([PMID: 34161862](https://pubmed.ncbi.nlm.nih.gov/34161862/)). Progression is generally **static-to-progressive**; Murakami & Kinoshita note the disease "progresses even after birth" ([PMID: 26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/)).

**Quality-of-life impact.** Profound. Affected children typically have absent or minimal speech, are non-ambulatory or motor-impaired, require anticonvulsant therapy, and depend on full caregiving. No disease-specific EQ-5D/SF-36 data exist given rarity.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PIGB* — phosphatidylinositol glycan anchor biosynthesis, class B (HGNC:8959; NCBI Gene 9488; OMIM *604122; UniProt Q92521; 15q21.3). PIGB is a **GT-C superfamily mannosyltransferase** (GPI mannosyltransferase III / GPI-MT-III) that transfers the third mannose (Man3) onto the GPI intermediate in the ER membrane ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/); topology reviewed in [PMID: 31569500](https://pubmed.ncbi.nlm.nih.gov/31569500/)). It shares a conserved membrane-embedded "BindGPILA" domain with PIG-M, PIG-V, PIG-Z, PIG-U and PIG-W ([PMID: 29764287](https://pubmed.ncbi.nlm.nih.gov/29764287/)).

**Pathogenic variants.** At least 10 distinct biallelic variants were reported in the founding families, including missense and predicted loss-of-function alleles; an intronic splice variant causing exon skipping (a null allele) was found in AFFND1 families ([PMID: 34400385](https://pubmed.ncbi.nlm.nih.gov/34400385/)). Variant classification follows ACMG/AMP; most are classified pathogenic/likely pathogenic in ClinVar. Functional consequence is **loss of function** — reduced or absent third-mannose transfer, leading to reduced GPI-anchored protein surface expression ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)). Transfection rescue assays confirm variant PIGB fails to restore GPI-anchored protein surface expression in PIGB-deficient CHO cells ([PMID: 33216889](https://pubmed.ncbi.nlm.nih.gov/33216889/)).

**Allele frequency.** Pathogenic alleles are individually ultra-rare in gnomAD (consistent with a recessive, severe disorder). **Origin:** germline (constitutional). Notably, a constitutional heterozygous PIGB variant rendered homozygous by somatic copy-number-neutral loss of heterozygosity can produce a PNH clone ([PMID: 33216889](https://pubmed.ncbi.nlm.nih.gov/33216889/)) — a distinct, non-DEE80 phenomenon.

**Modifier genes / epigenetics.** No specific modifier genes or epigenetic mechanisms are established for DEE80. Phenotypic variability (lethal vs milder) likely reflects residual PIGB enzymatic activity (hypomorphic vs null alleles), analogous to other IGDs.

**Chromosomal abnormalities.** Not a feature of DEE80 itself; the associated 70-kbp 15q microdeletion in the PNH report involves TM2D3/TARSL2, unrelated to the encephalopathy ([PMID: 33216889](https://pubmed.ncbi.nlm.nih.gov/33216889/)).

**Subcellular localization note.** PIGB is normally an ER/nuclear-envelope membrane enzyme; work in fungal systems shows nuclear-envelope localization can be essential for its activity ([PMID: 30266758](https://pubmed.ncbi.nlm.nih.gov/30266758/); [PMID: 32051283](https://pubmed.ncbi.nlm.nih.gov/32051283/)).

---

## 5. Environmental Information

DEE80 is a purely genetic disorder. **No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents cause it.** The only clinically relevant environmental modifiers are **fever and infection**, which can lower seizure threshold and precipitate status epilepticus. Dietary vitamin B6 status is relevant only as a therapeutic lever (see Treatment).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function PIGB variants** → **loss of GPI mannosyltransferase-III activity** in the ER (fails to add the third mannose to the GPI glycan core). *(Demonstrated — enzyme function and rescue assays.)*
2. Loss of Man3 addition → **accumulation of an incomplete, mannose-bearing GPI intermediate** and **globally reduced surface presentation of GPI-anchored proteins (GPI-APs)** on all cell types (shown by flow cytometry). *(Demonstrated.)*
3a. **Branch A (neurodevelopment):** Reduced surface GPI-APs → loss of GPI-anchored adhesion/guidance/signaling molecules (glypicans, contactins, RGMa, and ~150 others) → **impaired cortical progenitor proliferation, neuronal migration, axon guidance and myelination** → polymicrogyria, hypomyelination, axonal neuropathy, developmental delay. *(Mechanistically inferred from the established roles of individual GPI-APs.)*
3b. **Branch B (network excitability):** Developmental disorganization + altered GPI-anchored receptor signaling → **cortical hyperexcitability** → **early-onset, often intractable seizures** → epileptic encephalopathy compounding the developmental deficit. *(Inferred.)*
3c. **Branch C (alkaline phosphatase / vitamin B6):** Because the accumulated GPI still bears mannose, the transamidase attaches TNAP to it, but the incomplete anchor causes **TNAP to be secreted/shed rather than membrane-retained** → **serum hyperphosphatasia** and **reduced surface TNAP** → **perturbed dephosphorylation of pyridoxal-5′-phosphate (PLP)** → disturbed vitamin B6 homeostasis contributing to seizures. *(Branch C "secretion" step demonstrated in CHO cells; the PLP-handling link is biochemically inferred.)*
4. Net result: **developmental and epileptic encephalopathy with multisystem involvement and high early mortality.**

### Molecular detail

**Loss of GPI-anchored guidance/adhesion proteins drives cortical maldevelopment (Finding F005).** Many GPI-APs are master regulators of corticogenesis. Glypicans: **GPC4** (expressed in cortical progenitors) "promotes their proliferation and the generation of intermediate progenitors, whereas neuronal GPC2 acts as a brake on radial neuronal migration" ([PMID: 42275470](https://pubmed.ncbi.nlm.nih.gov/42275470/)); the GPI-anchored morphogen receptor **GPC3** forms a complex with Unc5 to "guide migrating pyramidal neurons in the mouse cortex" ([PMID: 36240740](https://pubmed.ncbi.nlm.nih.gov/36240740/)). Contactins (**CNTN2/TAG-1**, **CNTN4**) mark and modulate migrating neurons and neurite elongation ([PMID: 40580015](https://pubmed.ncbi.nlm.nih.gov/40580015/); [PMID: 38745463](https://pubmed.ncbi.nlm.nih.gov/38745463/); [PMID: 30629639](https://pubmed.ncbi.nlm.nih.gov/30629639/)), and **RGMa** is a GPI-anchored guidance molecule regulating neuronal differentiation and survival ([PMID: 36089003](https://pubmed.ncbi.nlm.nih.gov/36089003/)). Because PIGB loss reduces surface presentation of *all* GPI-APs simultaneously ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)), these pathways are impaired in parallel — explaining polymicrogyria, migration defects, hypomyelination and neuropathy.

**Hyperphosphatasia mechanism (Finding F006).** Murakami et al. (2012) directly demonstrated the molecular basis in CHO mutants: "The GPI-anchored protein was secreted substantially into medium from PIGV-, PIGB-, and PIGF-deficient CHO cells, in which incomplete GPI bearing mannose was accumulated. In contrast, ALP was degraded in PIGL-, DPM2-, or PIGX-deficient CHO cells, in which incomplete shorter GPIs that lacked mannose were accumulated" ([PMID: 22228761](https://pubmed.ncbi.nlm.nih.gov/22228761/)). Thus PIGB deficiency accumulates a *mannose-bearing* (but incomplete) GPI that the transamidase still uses, releasing TNAP into serum — the direct molecular cause of hyperphosphatasia in DEE80.

**Vitamin B6 rationale (Finding F007).** TNAP is itself a GPI-anchored ectoenzyme that dephosphorylates **pyridoxal-5′-phosphate (PLP)** — the predominant circulating form of vitamin B6 — to pyridoxal, which alone can cross the neuronal membrane to be re-phosphorylated intracellularly. Buchet, Millán & Magne (2013): TNAP deficiency (hypophosphatasia) "leads to ... epileptic seizures in the most severe cases, caused by abnormal metabolism of pyridoxal-5'-phosphate (the predominant form of vitamin B6)" ([PMID: 23860646](https://pubmed.ncbi.nlm.nih.gov/23860646/)); TNAP's broad substrate range including PLP is confirmed by Imam et al. (2024) ([PMID: 39728440](https://pubmed.ncbi.nlm.nih.gov/39728440/)). In GPI deficiencies the surface TNAP pool is reduced/shed, perturbing B6 handling — providing the biochemical rationale for supraphysiologic pyridoxine/PLP supplementation, which partially reduces seizures ([PMID: 35080266](https://pubmed.ncbi.nlm.nih.gov/35080266/)).

### Upstream vs downstream, cell types, GO/CL terms

- **Upstream (initiating):** ER GPI biosynthesis defect (GO:0006506 GPI anchor biosynthetic process; GO:0000030 mannosyltransferase activity). Compartment: endoplasmic reticulum (GO:0005783); nuclear envelope (GO:0005635).
- **Downstream (effector):** neuronal migration (GO:0001764), axon guidance (GO:0007411), central nervous system myelination (GO:0022010), regulation of neuron differentiation (GO:0045664); dephosphorylation of PLP (GO:0016791 phosphatase activity).
- **Cell types (CL):** neural progenitor/radial glia (CL:0000031 neuroblast; CL:0000681 radial glial cell), pyramidal neuron (CL:0000598), oligodendrocyte (CL:0000128), peripheral neuron/Schwann-associated axons (CL:0002573).

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary organ: **brain** (central nervous system) — cerebral cortex, white matter, cerebellum, brainstem. Secondary: **peripheral nervous system** (axonal neuropathy). Multisystem involvement is common in IGDs — Sidpra et al. found systemic involvement in 61/83, with gastrointestinal 66%, cardiac 19%, renal 14% ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)). Musculoskeletal features (scoliosis, foot deformity) reflect neuromuscular and connective-tissue involvement.

**Neuroimaging signature (Finding F008).** In the largest IGD cohort, prognostically significant features were "cerebral atrophy (75%), cerebellar atrophy (60%), callosal anomalies (57%) and **symmetric restricted diffusion of the central tegmental tracts (60%)**" ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)). Polymicrogyria and hypomyelination are specifically documented in PIGB patients.

**Tissue / cell level.** Nervous tissue predominantly: cortical neurons, radial glia/progenitors, oligodendrocytes (hypomyelination), peripheral axons. **Subcellular:** the initiating defect is in the **endoplasmic reticulum** (GPI assembly) and **plasma membrane** (GPI-AP presentation).

**UBERON terms:** UBERON:0000955 (brain); UBERON:0000956 (cerebral cortex); UBERON:0002037 (cerebellum); UBERON:0002316 (white matter); UBERON:0002298 (brainstem tegmentum, central tegmental tract region); UBERON:0000044 (peripheral nerve / dorsal root ganglion). **Lateralization:** bilateral/symmetric (e.g., symmetric central tegmental tract diffusion restriction; bilateral foot deformity).

---

## 8. Temporal Development

**Onset.** Congenital to early-infantile. In IGDs the **median age at seizure onset is 6 months** ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)); developmental delay is apparent from infancy. Onset pattern is chronic/insidious for developmental features and can be acute for seizures.

**Progression.** The disorder is **progressive after birth** — "the disease progresses even after birth" ([PMID: 26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/)) — arguing for early diagnosis and treatment. Course ranges from rapidly fatal (8 children dead before age 4 in the founding cohort; 15/83 deceased in the IGD cohort) to a more static but severely disabled trajectory in milder cases.

**Patterns.** Seizures are often intractable; no spontaneous remission is described. **Critical periods:** the prenatal/early-infantile window of corticogenesis and myelination is when the irreversible structural damage occurs, and the early-infantile period is the therapeutic window for seizure control (pyridoxine). Fever/infection are episodic aggravators.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare; exact prevalence/incidence are not established. Fewer than ~20 PIGB-specific patients are reported in the literature; DEE80 sits within the broader IGD group (>200 individuals reported across all GPI-pathway genes). No population-level prevalence figure exists.

**Inheritance.** **Autosomal recessive.** Requires two pathogenic PIGB alleles. **Penetrance** appears complete for biallelic loss-of-function. **Expressivity is variable** (lethal neonatal to milder childhood phenotypes), likely reflecting residual enzyme activity. **Genetic anticipation:** not applicable (no repeat expansion). **Germline mosaicism:** not specifically reported. **Consanguinity** contributes (homozygous cases in consanguineous families). **Carrier frequency:** not established; individually rare alleles.

**Population demographics.** Reported families are geographically and ethnically diverse (no established founder population for PIGB). **Sex ratio:** autosomal — no sex bias expected. **Age distribution:** affected individuals are infants and young children; survival beyond childhood occurs in milder cases.

---

## 10. Diagnostics

**Biochemical clues (Finding F003).** **Elevated serum alkaline phosphatase (hyperphosphatasia)** is a hallmark and a strong pointer to IGD: "The presence of hyperphosphatasia is strong evidence of IGD. Flow cytometric analysis of GPI-APs on granulocytes is also useful for the detection of IGD" ([PMID: 25803904](https://pubmed.ncbi.nlm.nih.gov/25803904/)). Clinical-clue combinations — "Certain combinations, such as seizures with aplastic/hypoplastic nails or abnormal alkaline phosphatase levels suggest an inherited GPI deficiency" ([PMID: 30054924](https://pubmed.ncbi.nlm.nih.gov/30054924/)). Note: not all IGDs show hyperphosphatasia; some show normal/low ALP depending on where the biosynthetic block lies.

**Flow cytometry.** Reduced surface GPI-anchored proteins (e.g., CD16, CD24, FLAER, CD59) on granulocytes/blood cells is a functional confirmatory assay ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/); [PMID: 25803904](https://pubmed.ncbi.nlm.nih.gov/25803904/)).

**Genetic testing (definitive).** Diagnosis is confirmed by **whole-exome (WES) or whole-genome (WGS) sequencing** identifying biallelic PIGB variants; WGS/RNA analysis is valuable for detecting deep-intronic/splice variants (e.g., the exon-skipping intronic allele in AFFND1, [PMID: 34400385](https://pubmed.ncbi.nlm.nih.gov/34400385/)). Targeted gene panels for epileptic encephalopathy / congenital disorders of glycosylation that include the PIG genes are appropriate first-line. Segregation studies confirm biallelic inheritance.

**Imaging.** Brain MRI may show polymicrogyria, hypomyelination, cerebral/cerebellar atrophy, callosal anomalies, and **symmetric restricted diffusion of the central tegmental tracts** ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)).

**Electrophysiology.** EEG documents epileptiform activity; nerve conduction studies confirm axonal peripheral neuropathy.

**Metabolic.** Urine organic acids may reveal **2-oxoglutaric aciduria** in severe cases ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)).

**Differential diagnosis.** Other IGDs (PIGA, PIGV, PIGN, PIGO, PIGT, PIGS, PIGW, PIGG, etc.), DOORS syndrome, hyperphosphatasia-mental retardation syndrome (Mabry syndrome, PIGV/PIGO), pyridoxine-dependent epilepsy (ALDH7A1), and other early-infantile epileptic encephalopathies. Two DEE80 patients were initially diagnosed clinically as DOORS syndrome.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Guarded, particularly in severe forms: **eight of ~16 affected children in the founding cohort died before age four** ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)); **15 of 83** individuals in the broad IGD cohort were deceased at reporting ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)). Milder patients survive into later childhood.

**Morbidity / function.** Severe lifelong disability — intellectual disability, absent/minimal speech, motor impairment, epilepsy, neuropathy, orthopedic complications (scoliosis, foot deformity). Full caregiver dependence is typical.

**Prognostic factors.** Severity of the underlying allele (null vs hypomorphic), presence of cortical malformation, seizure intractability, and neuroimaging burden (cerebral/cerebellar atrophy and central tegmental tract diffusion restriction are described as prognostically significant, [PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)). 2-oxoglutaric aciduria marks the most severe metabolic end.

---

## 12. Treatment

There is **no cure**; management is symptomatic and supportive, with one mechanism-based pharmacologic lever.

**Vitamin B6 (pyridoxine / pyridoxal-5′-phosphate) — mechanism-based, partial (Finding F004).** In a cohort of 7 GPI-deficiency patients treated with high-dose pyridoxine (20–30 mg/kg/day) or pyridoxal-5′-phosphate: "We observed more than 50% seizure frequency reduction in 2 out of 7 and less than 50% reduction in another 3 out of 7 participants. No participants reached seizure freedom" ([PMID: 35080266](https://pubmed.ncbi.nlm.nih.gov/35080266/)); no significant EEG change was seen in 6/7. Murakami & Kinoshita emphasize early treatment: "Early diagnosis and treatment are desirable because the disease progresses even after birth and vitamin B6(pyridoxine) is very effective for some patients with intractable seizures" ([PMID: 26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/)). The biochemical rationale is the TNAP–PLP link (Findings F006, F007). NCIT: Pyridoxine (C793); Pyridoxal Phosphate (C88250).

**Antiseizure medications.** Standard antiepileptic drugs are used for seizure control, though seizures are frequently intractable. Choice is empirical/supportive; no genotype-specific ASM is validated.

**Supportive / rehabilitative care.** Physical, occupational and speech therapy; nutritional support; orthopedic management of scoliosis/foot deformity; management of intercurrent infections that provoke seizures; multidisciplinary developmental support. NCIT: Supportive Care (C15277); Physical Therapy (C15359).

**Advanced / experimental therapeutics.** No approved gene, cell, or RNA therapy exists for DEE80. Gene replacement is a conceptually attractive future avenue (recessive loss-of-function of a single enzyme), but none is in clinical trials for PIGB. **Pharmacogenomics:** not established.

---

## 13. Prevention

**Primary prevention.** Not possible for a spontaneously arising recessive disorder except through reproductive genetic counseling. **Genetic counseling** for at-risk families (25% recurrence risk for carrier couples) is central. **Carrier screening** and, where an affected proband's variants are known, **prenatal diagnosis or preimplantation genetic testing (PGT-M)** can prevent recurrence.

**Secondary prevention.** Early molecular diagnosis (rapid WES/WGS in neonates with epileptic encephalopathy plus hyperphosphatasia) enables early initiation of pyridoxine and multidisciplinary support during the progressive early period. There is no population newborn-screening test for PIGB deficiency, though hyperphosphatasia on routine chemistry can be an incidental flag.

**Tertiary prevention.** Prevention of complications — aspiration, infection-triggered status epilepticus, orthopedic deterioration — through proactive management.

---

## 14. Other Species / Natural Disease

PIGB is evolutionarily conserved; orthologs and GPI-pathway homologs exist across eukaryotes (mammals, fungi, protozoa). Functional studies of PIG-B localization/activity have been performed in fungal systems ([PMID: 30266758](https://pubmed.ncbi.nlm.nih.gov/30266758/); [PMID: 32051283](https://pubmed.ncbi.nlm.nih.gov/32051283/)), and the shared BindGPILA membrane domain is conserved across PIG-B/M/V/W/U/Z ([PMID: 29764287](https://pubmed.ncbi.nlm.nih.gov/29764287/)). **Orthologs:** mouse *Pigb* (NCBI Gene 55981). No naturally occurring PIGB-deficiency disease in companion animals or wildlife is catalogued (no OMIA entry identified). GPI biosynthesis is essential and broadly conserved, so complete loss is generally embryonic-lethal in model organisms. No zoonotic relevance.

---

## 15. Model Organisms

**Cellular models (principal experimental system).** **PIGB-deficient Chinese hamster ovary (CHO) cells** are the workhorse for GPI biology and were pivotal in establishing DEE80 mechanism: they show loss of surface GPI-anchored proteins and the diagnostic **secretion of ALP** ([PMID: 22228761](https://pubmed.ncbi.nlm.nih.gov/22228761/)); transfection rescue confirms variant pathogenicity ([PMID: 33216889](https://pubmed.ncbi.nlm.nih.gov/33216889/)). PIGB-knockout human cell lines were used to show altered EthN-P bridge usage on GPI anchors ([PMID: 35603428](https://pubmed.ncbi.nlm.nih.gov/35603428/)). Patient fibroblasts and blood cells serve as primary-cell models for flow-cytometric GPI-AP quantitation ([PMID: 31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/)).

**Genetic model types.** Knockout/knock-down cell lines are the primary genetic models. A dedicated mouse model of PIGB deficiency recapitulating DEE80 is not prominently reported (complete GPI-pathway knockouts are typically embryonic lethal; conditional/hypomorphic strategies would be required). MGI lists *Pigb* (mouse), enabling future targeted or conditional models.

**Phenotype recapitulation & limitations.** Cellular models faithfully reproduce the *biochemical* phenotype (reduced surface GPI-APs; ALP shedding) and are excellent for variant functional testing, but **cannot recapitulate the neurodevelopmental phenotype** (cortical migration, epilepsy, neuropathy). Patient-derived iPSC neurons/organoids would be the logical next step to model corticogenesis defects.

---

## Mechanistic Model / Interpretation

```
   PIGB biallelic loss-of-function (15q21.3)
                 │  (loss of GPI mannosyltransferase-III; no 3rd mannose)
                 ▼
   Incomplete, mannose-bearing GPI accumulates in ER
                 │
   ┌─────────────┼───────────────────────────────┐
   ▼             ▼                                 ▼
 Global loss   Transamidase still attaches      Reduced surface
 of surface    TNAP to incomplete anchor        TNAP pool
 GPI-APs       → TNAP SECRETED (shed)                │
   │                │                                 ▼
   ▼                ▼                     Impaired PLP (vit B6)
 Loss of        Serum hyperphosphatasia   dephosphorylation
 glypicans,     (diagnostic clue)              │
 contactins,                                    ▼
 RGMa, etc.                          Contributes to seizures →
   │                                 partial response to pyridoxine/PLP
   ▼
 Impaired cortical progenitor proliferation,
 neuronal migration, axon guidance, myelination
   │
   ├──► Polymicrogyria, hypomyelination, cerebral/cerebellar atrophy
   ├──► Axonal peripheral neuropathy
   └──► Cortical hyperexcitability ──► early-onset intractable epilepsy
                                 │
                                 ▼
        DEVELOPMENTAL & EPILEPTIC ENCEPHALOPATHY 80
        (DD/ID, seizures, hypotonia, high early mortality)
```

The unifying concept is that **one enzymatic lesion removes an entire class of ~150 cell-surface proteins**, producing a pleiotropic, multi-branch phenotype. Two branches are biochemically demonstrated (GPI-AP loss by flow cytometry; TNAP shedding in CHO cells); the neurodevelopmental branch is inferred from the well-established individual functions of GPI-anchored guidance/adhesion molecules; and the vitamin-B6 branch is a biochemically grounded therapeutic hypothesis supported by partial clinical efficacy.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [31256876](https://pubmed.ncbi.nlm.nih.gov/31256876/) | *Mutations in PIGB Cause an Inherited GPI Biosynthesis Defect...* | Human clinical + in vitro | **Founding paper**; defines gene, phenotype, mortality, flow-cytometry defect (F001, F002) |
| [34161862](https://pubmed.ncbi.nlm.nih.gov/34161862/) | *Further delineation of PIGB-related early infantile EE* | Human case | Milder-end phenotype (F002) |
| [22228761](https://pubmed.ncbi.nlm.nih.gov/22228761/) | *Mechanism for release of alkaline phosphatase in GPI deficiency* | In vitro (CHO) | Explains hyperphosphatasia (F006) |
| [23860646](https://pubmed.ncbi.nlm.nih.gov/23860646/) | *Multisystemic functions of alkaline phosphatases* | Review | TNAP–PLP–seizure link (F007) |
| [39728440](https://pubmed.ncbi.nlm.nih.gov/39728440/) | *Structural/functional integration of TNAP* | Review | Confirms TNAP dephosphorylates PLP (F007) |
| [35080266](https://pubmed.ncbi.nlm.nih.gov/35080266/) | *Pyridoxine or PLP for seizures in GPI deficiency* | Human cohort (n=7) | Partial efficacy of B6 (F004) |
| [26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/) | *[Inherited GPI deficiency...]* | Review | B6 effective in some; progressive disease (F004) |
| [25803904](https://pubmed.ncbi.nlm.nih.gov/25803904/) | *[Inherited GPI deficiencies...]* | Review | Hyperphosphatasia + flow cytometry diagnostics (F003) |
| [30054924](https://pubmed.ncbi.nlm.nih.gov/30054924/) | *Clinical variability in IGDs* | Human cohort (n=202) | Diagnostic clues (F003) |
| [38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/) | *Clinical and genetic spectrum of IGDs* | Human cohort (n=83) | Natural history, imaging signature (F008) |
| [42275470](https://pubmed.ncbi.nlm.nih.gov/42275470/) | *Glypican core proteins in corticogenesis* | Model/in vitro | GPC4/GPC2 in migration (F005) |
| [36240740](https://pubmed.ncbi.nlm.nih.gov/36240740/) | *GPC3-Unc5 receptor complex in migration* | Model/structural | GPC3 guides cortical neurons (F005) |
| [40580015](https://pubmed.ncbi.nlm.nih.gov/40580015/), [38745463](https://pubmed.ncbi.nlm.nih.gov/38745463/), [30629639](https://pubmed.ncbi.nlm.nih.gov/30629639/) | Contactins CNTN2/CNTN4/CNTN1 | Model | Migrating-neuron / neurite roles (F005) |
| [36089003](https://pubmed.ncbi.nlm.nih.gov/36089003/) | *RGMa...* | Model | GPI-anchored guidance/survival molecule (F005) |
| [34400385](https://pubmed.ncbi.nlm.nih.gov/34400385/) | *Intronic PIGB variant in AFFND1* | Human + in vitro | Allelic spectrum; null via exon skipping |
| [33216889](https://pubmed.ncbi.nlm.nih.gov/33216889/) | *PNH from CN-LOH of constitutional PIGB* | Human + in vitro | Rescue assay; distinct PNH mechanism |
| [29764287](https://pubmed.ncbi.nlm.nih.gov/29764287/), [31569500](https://pubmed.ncbi.nlm.nih.gov/31569500/), [30266758](https://pubmed.ncbi.nlm.nih.gov/30266758/), [32051283](https://pubmed.ncbi.nlm.nih.gov/32051283/) | PIG-B structure/topology/localization | Computational/model | Enzyme biology context |
| [35603428](https://pubmed.ncbi.nlm.nih.gov/35603428/) | *EthN-P on second mannose...* | In vitro | PIGB-KO GPI biology |
| [30269814](https://pubmed.ncbi.nlm.nih.gov/30269814/), [32198969](https://pubmed.ncbi.nlm.nih.gov/32198969/), [38055078](https://pubmed.ncbi.nlm.nih.gov/38055078/) | PIGS/PIGW IGDs | Human | Related IGDs; differential diagnosis, B6-responsive seizures |

---

## Limitations and Knowledge Gaps

1. **Small n.** Fewer than ~20 molecularly confirmed PIGB/DEE80 patients are reported; frequency estimates and genotype–phenotype correlations are provisional. Many cohort-level statistics (imaging, seizure onset, mortality) derive from **cross-gene IGD cohorts**, not PIGB-specific data — an extrapolation caveat.
2. **Neurodevelopmental branch is inferred.** The link from GPI-AP loss to cortical malformation and epilepsy rests on the established biology of individual GPI-APs (glypicans, contactins, RGMa) rather than direct demonstration in PIGB-deficient neurons.
3. **No faithful whole-animal or iPSC-neuronal model** of DEE80 is established; the neurodevelopmental phenotype has not been experimentally reconstituted.
4. **Vitamin B6 mechanism is partly hypothetical.** The TNAP–PLP rationale is biochemically sound, but efficacy is partial and no participant achieved seizure freedom; the precise contribution of disturbed B6 metabolism to PIGB-related seizures is not fully proven.
5. **No prevalence/incidence, QoL, or long-term natural-history data** specific to DEE80.
6. **Epigenetic, metabolomic, and multi-omic** profiling of DEE80 tissues is essentially absent (2-oxoglutaric aciduria in severe cases is unexplained mechanistically).

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived iPSC cortical organoids / neurons** carrying PIGB variants to directly test whether reduced surface glypicans/contactins/RGMa cause migration and myelination defects — closing the inference gap in the neurodevelopmental branch.
2. **PIGB conditional/hypomorphic mouse model** (neural-specific) to recapitulate cortical malformation, epilepsy and neuropathy, and to test pyridoxine/PLP and GPI-pathway-directed therapies in vivo.
3. **Quantitative PLP/pyridoxal metabolomics** (serum and, where possible, CSF) in PIGB patients before/after high-dose B6, correlated with surface TNAP activity, to test the F007 mechanism directly and identify B6 responders.
4. **Genotype–phenotype registry** aggregating all PIGB cases with standardized phenotyping, MRI (including central tegmental tract diffusion), ALP levels, and residual enzyme activity to build predictive prognostic models.
5. **Systematic ClinVar/gnomAD curation** of PIGB variants with functional (CHO rescue / flow-cytometry) classification to improve ACMG interpretation and diagnostic yield.
6. **Explore GPI-pathway or substrate-supplementation therapeutics** (e.g., strategies used in other CDGs) as candidate disease-modifying approaches, given the recessive single-enzyme etiology.

---

*Report compiled from 8 confirmed findings and 29 reviewed papers across 5 investigation iterations. Evidence types are labeled human clinical, model organism, in vitro, computational, or review throughout.*


## Artifacts

- [OpenScientist final report](Developmental_And_Epileptic_Encephalopathy_80-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Developmental_And_Epileptic_Encephalopathy_80-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 26 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (1 mention) - the report calls it "72% (IGD cohort)"; HP calls it **Hypotonia**
- `HP:0100022` (1 mention) - the report calls it "64% (IGD cohort)"; HP calls it **Abnormality of movement**
- `HP:0002126` (1 mention) - the report calls it "2/~16 (PIGB)"; HP calls it **Polymicrogyria**
- `HP:0003155` (1 mention) - the report calls it "Most"; HP calls it **Elevated circulating alkaline phosphatase concentration**
- `HP:0001999` (1 mention) - the report calls it "82% (IGD cohort), variable"; HP calls it **Abnormal facial shape**
- `UBERON:0002298` (1 mention) - the report calls it "brainstem tegmentum, central tegmental tract region"; UBERON calls it **brainstem**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003355` (1 mention) - the report calls it "Organic aciduria"; HP calls it **Aminoaciduria**
- `UBERON:0000044` (1 mention) - the report calls it "peripheral nerve / dorsal root ganglion"; UBERON calls it **dorsal root ganglion**