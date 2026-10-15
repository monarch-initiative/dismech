---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-07T21:42:40.975140'
end_time: '2026-09-07T21:59:40.840289'
duration_seconds: 1019.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental And Epileptic Encephalopathy 77
  mondo_id: MONDO:0032808
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 39
  verified: 37
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 11
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0032808
    reported_labels:
    - MONDO
    ontology_label: developmental and epileptic encephalopathy, 77
  - term_id: DOID:0112213
    reported_labels:
    - DOID
    ontology_label: multiple congenital anomalies-hypotonia-seizures syndrome 4
  - term_id: CL:0000775
    reported_labels:
    - diagnostic readout
    ontology_label: neutrophil
  - term_id: CL:0000057
    reported_labels:
    - diagnostic readout
    ontology_label: fibroblast
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0031225
    ontology_label: obsolete anchored component of membrane
    replaced_by: GO:0016020
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Developmental_And_Epileptic_Encephalopathy_77-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Developmental_And_Epileptic_Encephalopathy_77-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental And Epileptic Encephalopathy 77
- **MONDO ID:** MONDO:0032808 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental And Epileptic Encephalopathy 77** covering all of the
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

# Developmental and Epileptic Encephalopathy 77 (DEE77): A Comprehensive Disease Characterization

**Disease:** Developmental and Epileptic Encephalopathy 77 (DEE77)
**MONDO ID:** MONDO:0032808 · **OMIM:** #618548 · **Causal gene:** *PIGQ* (16p13.3)
**Category:** Mendelian (autosomal recessive inherited GPI-anchor deficiency)

---

## Summary

Developmental and Epileptic Encephalopathy 77 (DEE77; also indexed as Early Infantile Epileptic Encephalopathy 77 / EIEE77 and as Multiple Congenital Anomalies–Hypotonia–Seizures syndrome 4 / MCAHS4) is an **ultra-rare autosomal-recessive disorder** caused by **biallelic loss-of-function / hypomorphic variants in *PIGQ*** (phosphatidylinositol glycan anchor biosynthesis class Q; HGNC:14135; formerly *GPI1*), located on chromosome 16p13.3. PIGQ is a subunit of the **GPI-N-acetylglucosaminyltransferase (GPI-GnT) complex** that catalyzes the very first, committed step of glycosylphosphatidylinositol (GPI) anchor biosynthesis on the cytoplasmic face of the endoplasmic reticulum. Because GPI anchoring tethers >150 diverse cell-surface proteins (enzymes, adhesion molecules, receptors, complement regulators), PIGQ deficiency produces a systemic **inherited GPI deficiency (IGD)** with a neurodevelopmental core.

The disease was first recognized in 2014, when whole-genome sequencing of severe early-onset epilepsy trios identified a recessive *PIGQ* splice/exon-skipping variant in an Ohtahara-syndrome patient ([PMID: 24463883](https://pubmed.ncbi.nlm.nih.gov/24463883/)). The definitive phenotypic delineation came from Johnstone et al. 2020, who reported seven new biallelic-*PIGQ* subjects with functional confirmation ([PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)). Clinically, DEE77 presents in **early infancy (seizure onset ~2.5–7 months)** with drug-resistant epileptic seizures, axial hypotonia, global developmental delay/intellectual disability, progressive cerebral and cerebellar atrophy, and multisystem (gastrointestinal and cardiac) anomalies. **Premature death occurs in more than half of reported patients.** A milder end of the spectrum — nonprogressive congenital ataxia with intellectual disability and generalized epilepsy — has also been described ([PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)).

There is **no disease-modifying therapy**. Management is supportive and symptomatic, with anti-seizure medications; **high-dose vitamin B6 (pyridoxine / pyridoxal-5′-phosphate)** provides partial seizure benefit in a subset of IGD patients but rarely achieves seizure freedom. Diagnosis rests on **exome/genome sequencing** confirmed functionally by **flow cytometry** showing reduced surface GPI-anchored proteins (e.g., FLAER, CD16, CD14) on granulocytes/leukocytes. Prevention relies on **genetic counseling** with prenatal / preimplantation genetic testing for at-risk (often consanguineous) families. This report synthesizes nine confirmed findings across the full disease-characterization template.

---

## 1. Disease Information

**Overview.** DEE77 is a monogenic, autosomal-recessive developmental and epileptic encephalopathy belonging to the family of **inherited glycosylphosphatidylinositol (GPI) deficiencies (IGDs)** — congenital disorders of glycosylation affecting the biosynthesis or remodeling of the GPI anchor. It is characterized by early-infantile-onset epilepsy that is frequently drug-resistant, together with severe global developmental impairment and congenital multisystem anomalies.

**Key identifiers** (cross-references verified via OLS for MONDO:0032808):

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032808 |
| OMIM (phenotype) | #618548 |
| OMIM (gene *PIGQ*) | 605754 |
| DOID | DOID:0112213 |
| GARD | 0016363 |
| MedGen | C5231405 / CN1684735 |
| UMLS | C5231405 |
| HGNC (gene) | HGNC:14135 |

**Synonyms / alternative names:** Developmental and epileptic encephalopathy 77; DEE77; Early infantile epileptic encephalopathy 77; EIEE77; PIGQ-related GPI deficiency; **Multiple congenital anomalies–hypotonia–seizures syndrome 4 (MCAHS4)**.

**Information source type.** Knowledge is derived almost entirely from **aggregated disease-level resources** (OMIM, MONDO, ClinVar) and from **small published case series / individual case reports** (Martin 2014; Johnstone 2020; Zanni 2022), not from large EHR-based cohorts. The largest quantitative context comes from a pooled IGD cohort (Sidpra et al. 2024; n=83) that includes *PIGQ* among other GPI-pathway genes ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)).

---

## 2. Etiology

**Primary cause — genetic.** DEE77 is caused by **biallelic (autosomal recessive) pathogenic variants in *PIGQ***. There is no environmental, infectious, or acquired etiology; the disorder is fully Mendelian. The first causal link was reported by Martin et al. 2014, who identified a recessive *PIGQ* mutation causing exon skipping and defective GPI biosynthesis in an Ohtahara-syndrome patient among six whole-genome-sequenced severe early-onset epilepsy trios:

> *"The fourth OS patient had a recessive mutation in PIGQ that led to exon skipping and defective glycophosphatidyl inositol biosynthesis."* — [PMID: 24463883](https://pubmed.ncbi.nlm.nih.gov/24463883/)

Johnstone et al. 2020 then confirmed and expanded the etiology with seven new biallelic-*PIGQ* subjects from six families:

> *"We investigated seven children from six families to expand the phenotypic spectrum associated with an early infantile epileptic encephalopathy caused by biallelic pathogenic variants in the phosphatidylinositol glycan anchor biosynthesis class Q (PIGQ) gene."* — [PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)

**Genetic risk factors.** The causal factor is the biallelic *PIGQ* genotype itself. **Consanguinity** is an important risk factor (homozygous variants recur in consanguineous families, e.g., the homozygous c.1631dupA reported by Zanni et al. 2022). Compound heterozygosity accounts for cases in non-consanguineous families. No modifier genes have been formally established for DEE77, although residual enzymatic activity of hypomorphic alleles is the principal determinant of severity (see §4, §9).

**Environmental risk / protective factors and gene–environment interactions.** **None are established.** As a purely Mendelian recessive disorder, environmental exposures do not cause DEE77. The only clinically actionable "environmental" modifier is nutritional/pharmacological — **vitamin B6 (pyridoxine)** partially mitigates seizures in a subset of IGD patients (see §12), representing a gene–treatment rather than a gene–environment interaction. No protective alleles are known.

---

## 3. Phenotypes

The DEE77 phenotype is dominated by a **neurodevelopmental triad (epilepsy + hypotonia + developmental delay)** with frequent multisystem congenital anomalies. Frequencies below combine the *PIGQ*-specific series (Johnstone 2020, n=7; Zanni 2022) with the pooled IGD cohort (Sidpra 2024, n=83) where *PIGQ*-specific numbers are unavailable.

| Phenotype | Type | Onset / severity | Frequency | Suggested HPO |
|---|---|---|---|---|
| Epileptic seizures (incl. status epilepticus, EIMFS, myoclonic) | Clinical sign | Onset 2.5–7 mo; severe, often drug-resistant | 83% (IGD pooled); consistent in *PIGQ* | HP:0001250 (Seizure), HP:0002133 (Status epilepticus) |
| Axial / generalized hypotonia | Clinical sign | Congenital/early; moderate–severe | 72% (IGD pooled) | HP:0008936 (Axial hypotonia), HP:0001252 (Hypotonia) |
| Global developmental delay / intellectual disability | Behavioral/cognitive | Early; severe | 90% (IGD pooled) | HP:0001263 (GDD), HP:0001249 (ID) |
| Cerebral atrophy | Imaging/structural | Progressive | 75% (IGD pooled) | HP:0002059 (Cerebral atrophy) |
| Cerebellar atrophy | Imaging/structural | Progressive | 60% (IGD pooled) | HP:0001272 (Cerebellar atrophy) |
| Corpus callosum anomalies | Imaging/structural | Congenital | 57% (IGD pooled) | HP:0007370 (Aplasia/hypoplasia of the corpus callosum) |
| Gastrointestinal anomalies (incl. midgut volvulus) | Physical | Congenital; can be life-threatening | 66% (IGD pooled); 2/7 volvulus (Johnstone) | HP:0011024 (Abnormality of the GI tract), HP:0002580 (Volvulus) |
| Cardiac anomalies / arrhythmia | Physical | Congenital | 19% (IGD pooled) | HP:0001627 (Abnormal heart morphology), HP:0011675 (Arrhythmia) |
| Renal malformation | Physical | Congenital | 14% (IGD pooled) | HP:0000077 (Abnormality of the kidney) |
| Dysmorphic features | Physical | Congenital; no distinctive gestalt | 82% (any); none >30% | HP:0001999 (Abnormal facial shape) |
| Motor symptoms (ataxia/dyskinesia) | Clinical sign | Variable | 64% (IGD pooled) | HP:0001251 (Ataxia), HP:0100022 (Abnormal movement) |

Key supporting quotes:

> *"Epileptic seizures, axial hypotonia, developmental delay and multiple congenital anomalies were consistently observed. Seizure onset occurred between 2.5 months and 7 months of age and varied from treatable seizures to recurrent episodes of status epilepticus."* — [PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)

> *"Core clinical features were developmental delay or intellectual disability (DD/ID, 90%), seizures (83%), hypotonia (72%) and motor symptoms (64%)."* — [PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)

**Progression and severity.** The severe end shows **progressive** neurodegeneration (progressive atrophy, hypomyelination) and high early mortality; a **milder, nonprogressive** end (congenital ataxia with ID and generalized epilepsy, cerebellar atrophy) is documented ([PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)). Severity correlates with residual PIGQ/GPI-biosynthetic activity.

**Quality-of-life impact.** Not formally measured with EQ-5D/SF-36/PROMIS in this ultra-rare disorder. Qualitatively, the impact is **profound**: affected children have severe cognitive/motor disability, drug-resistant seizures, feeding difficulties, and dependence on full-time caregiving; many do not survive early childhood.

---

## 4. Genetic / Molecular Information

**Causal gene — *PIGQ*.**

| Attribute | Value |
|---|---|
| Gene symbol | *PIGQ* (formerly *GPI1*) |
| HGNC | HGNC:14135 |
| NCBI Gene ID | 9091 |
| OMIM gene | 605754 |
| Ensembl | ENSG00000007541 |
| UniProt | Q9BRB3 |
| Cytoband | 16p13.3 |
| GRCh38 locus | chr16:566,995–584,121 (+ strand) |
| Canonical transcript / RefSeq | ENST00000321878 / NM_004204.5 |

**Pathogenic variant spectrum (ClinVar, 300 records queried).**

| Classification | Count |
|---|---|
| Pathogenic | 24 |
| Likely pathogenic | 4 |
| VUS | 105 |
| Likely benign | 145 |
| Benign | 1 |
| Conflicting | 6 |

By molecular type across the record set: 268 SNVs, 17 deletions, 7 duplications, 2 microsatellite, plus rare CNV gains/losses and 1 inversion. **DEE77 variants are predominantly small-scale** (missense, nonsense, frameshift, splice-site), with occasional copy-number/structural events. Representative variants: the exon-skipping splice variant of Martin 2014 ([PMID: 24463883](https://pubmed.ncbi.nlm.nih.gov/24463883/)) and the homozygous frameshift **NM_004204.5:c.1631dupA (p.Tyr544fs\*79)** of Zanni 2022 ([PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)).

**Population constraint (gnomAD, computed).** *PIGQ* is **heterozygous LoF-tolerant**, consistent with a recessive mechanism: gnomAD v2 pLI ≈ 0 (5.7e-17), LOEUF (oe_lof upper) = 1.12, observed/expected LoF = 0.90 (54 obs vs 60.3 exp), missense Z = −0.08. Heterozygous carriers are unaffected — concordant with the historical observation that heterozygous 16p13.3 deletions removing one *GPI1* allele (in α-thalassemia/mental retardation) do not overtly impair GPI-anchored protein expression ([PMID: 11418246](https://pubmed.ncbi.nlm.nih.gov/11418246/)).

**Functional consequence.** **Loss of function / hypomorphic.** Complete null is presumed embryonic-lethal; viable patients retain residual GPI-biosynthetic activity. Functional proof of causality: transfection of wild-type *PIGQ* cDNA into patient fibroblasts rescued the GPI-anchored-protein deficiency (see §6).

**Modifier genes / epigenetics / large chromosomal abnormalities.** No DEE77-specific modifier genes or epigenetic mechanisms are established. Whole-gene deletions or 16p13.3 CNVs are rare contributors; most disease arises from small biallelic variants.

---

## 5. Environmental Information

**Not applicable.** DEE77 is a monogenic recessive disorder with **no environmental, lifestyle, toxic, radiation, occupational, or infectious cause or trigger**. No dietary, behavioral, or exposure-based risk or protective factors have been identified. The only exogenous factor with clinical relevance is **therapeutic vitamin B6 (pyridoxine/pyridoxal-5′-phosphate)**, which partially reduces seizures in some IGD patients (see §12) — a treatment effect, not a disease cause.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic/LoF *PIGQ* variants** reduce functional PIGQ protein → *leads to*
2. **Impaired GPI-N-acetylglucosaminyltransferase (GPI-GnT) complex** on the cytoplasmic face of the ER, of which PIGQ is a subunit → *results in*
3. **Failure of the first committed step of GPI biosynthesis** (transfer of GlcNAc onto phosphatidylinositol) → *leads to*
4. **Global reduction in GPI anchor synthesis** → *results in*
5. **Reduced cell-surface expression of >150 GPI-anchored proteins** (enzymes, adhesion molecules, receptors, complement regulators) — directly demonstrated in patient granulocytes and fibroblasts → *leads to* (branch point)
   - **5a. Neuronal branch:** loss of GPI-anchored proteins critical to neuronal development, synapse formation, and cortical excitability → *results in* → **epileptogenesis, hypotonia, developmental delay, progressive cerebral/cerebellar atrophy** (inferred from human phenotype + mouse GPI-deficiency models).
   - **5b. Systemic/developmental branch:** loss of GPI-anchored proteins in non-neural tissues during organogenesis → *results in* → **gastrointestinal (volvulus), cardiac, renal congenital anomalies**.
6. Combined CNS and multisystem dysfunction → *results in* → **early-infantile DEE77 with high mortality.**

### Molecular and cellular detail

**PIGQ's molecular role** is defined precisely:

> *"PIGQ encodes the phosphatidylinositol glycan class Q protein and is part of the GPI-N-acetylglucosaminyltransferase complex that initiates GPI biosynthesis from phosphatidylinositol (PI) and N-acetylglucosamine (GlcNAc) on the cytoplasmic side of the endoplasmic reticulum (ER)."* — [PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)

The GPI-GnT ring complex also includes ARV1, which recruits phosphatidylinositol and associates directly with PIGQ:

> *"ARV1 associates with PIGQ, a GPI-GnT component"* — [PMID: 40378954](https://pubmed.ncbi.nlm.nih.gov/40378954/)

**Direct functional proof in human cells** (loss of GPI-anchored proteins is the proximate mechanism, and it is PIGQ-specific):

> *"Flow cytometry using granulocytes and fibroblasts from affected individuals showed reduced expression of glycosylphosphatidylinositol (GPI)-anchored proteins. Transfection of wildtype PIGQ cDNA into patient fibroblasts rescued this phenotype."* — [PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)

**Upstream vs downstream.** The *PIGQ* mutation and GPI-GnT dysfunction are **upstream**; loss of specific GPI-anchored proteins (e.g., complement regulators, folate receptor-α, alkaline phosphatase-related processing, neural adhesion molecules) and the resulting neuronal/organ dysfunction are **downstream**.

**Cellular processes and compartments.** The initiating lesion is in the **endoplasmic reticulum (GO:0005789, ER membrane; cytoplasmic face)**. Affected biological processes: **GPI anchor biosynthetic process (GO:0006506)**, **GPI anchor metabolic process (GO:0006505)**, **protein lipidation / attachment of GPI anchor to protein (GO:0016255)**. Downstream neural processes include **regulation of neuron differentiation** and **regulation of synaptic transmission / neuronal excitability**.

**Biochemical hallmark shared across IGD.** Some IGD subtypes show **hyperphosphatasia** (elevated serum alkaline phosphatase, itself a GPI-anchored enzyme aberrantly shed when anchoring fails); this is variable in *PIGQ* disease. **Folate receptor-α (FOLR1) is a GPI-anchored protein**, providing a mechanistic rationale for cerebral folate involvement and folinic-acid relevance ([PMID: 19732866](https://pubmed.ncbi.nlm.nih.gov/19732866/)).

**Cell types (CL suggestions):** neuron (CL:0000540), GABAergic/inhibitory neuron (CL:0000617), glutamatergic/excitatory neuron (CL:0000679), granulocyte/neutrophil (CL:0000775 — diagnostic readout), fibroblast (CL:0000057 — diagnostic readout).

---

## 7. Anatomical Structures Affected

**Organ level — primary.** The **brain / central nervous system** (UBERON:0000955, brain; UBERON:0001017, CNS) is the primary affected organ. Within the brain, the **cerebral cortex** (UBERON:0000956), **cerebellum** (UBERON:0002037), **corpus callosum** (UBERON:0002336), and white-matter tracts (hypomyelination; symmetric restricted diffusion of the **central tegmental tracts**, 60% in IGD pooled) are involved.

**Secondary / multisystem involvement:**
- **Gastrointestinal tract** (UBERON:0001555) — anomalies in 66%, including life-threatening midgut volvulus.
- **Heart** (UBERON:0000948) — structural anomalies and arrhythmias in ~19%.
- **Kidney** (UBERON:0002113) — malformation in ~14%.

**Body systems:** nervous (primary), digestive, cardiovascular, and renal/urinary (secondary).

**Tissue and cell level.** Primarily **nervous tissue** (excitatory and inhibitory cortical neurons, cerebellar neurons). Because GPI anchoring is ubiquitous, epithelial and other tissues are affected during organogenesis. Diagnostic readouts use **hematopoietic cells** (granulocytes/leukocytes) and **fibroblasts**.

**Subcellular level.** The initiating defect is at the **endoplasmic reticulum membrane, cytoplasmic face** (GO:0005789). The functional deficit manifests at the **plasma membrane** (GO:0005886) as loss of GPI-anchored surface proteins, i.e., in the **anchored component of the plasma membrane** (GO:0031225).

**Localization / lateralization.** CNS involvement is **bilateral and largely symmetric** (symmetric atrophy, symmetric restricted diffusion of central tegmental tracts).

---

## 8. Temporal Development

**Onset.** **Early-infantile / congenital.** Congenital hypotonia and multiple congenital anomalies are present at/near birth; **seizure onset occurs between 2.5 and 7 months** ([PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)). Median age at seizure onset across the IGD family is ~6 months ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)). Onset pattern is **chronic with early emergence**, punctuated by acute events (status epilepticus, volvulus).

**Progression.** At the severe end the course is **progressive**: recurrent/refractory seizures, progressive cerebral and cerebellar atrophy, and hypomyelination, with declining function. At the mild end (Zanni 2022) the course is **nonprogressive** congenital ataxia. Disease is **lifelong (chronic)** when survived.

**Patterns.** Seizures range from treatable to recurrent status epilepticus; **no reliable spontaneous remission** is documented. **Critical period:** the fetal/early-infantile window of neurodevelopment is the period of vulnerability; because the disease "progresses even after birth," early diagnosis and initiation of supportive/pyridoxine therapy is advocated as a potential window of opportunity ([PMID: 26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/)).

---

## 9. Inheritance and Population

**Epidemiology.** DEE77 is **ultra-rare**: only ~15–20 patients reported worldwide since 2014 (Martin 2014 first case; Johnstone 2020 +7; Zanni 2022 +1; scattered others). The case count is **too small for formal prevalence/incidence estimates**, and no Orphanet point-prevalence figure is available.

> *"Pathogenic variants in the PIGQ gene have been previously reported in 10 patients with congenital hypotonia, early-infantile epileptic encephalopathy, and premature death occurring in more than half cases."* — [PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)

**Inheritance.** **Autosomal recessive**, biallelic *PIGQ* — homozygous (often consanguineous) or compound heterozygous.

> *"The fourth OS patient had a recessive mutation in PIGQ"* — [PMID: 24463883](https://pubmed.ncbi.nlm.nih.gov/24463883/)

**Carrier / birth-frequency estimate (gnomAD v4, computed).** Summed high-confidence pLoF allele frequency q ≈ 1.75e-3 → naïve Hardy–Weinberg carrier frequency ≈ 2q ≈ **1/286**, and biallelic-LoF birth frequency q² ≈ **1/327,600**. **This markedly overestimates true disease incidence** because complete PIGQ null is presumed embryonic-lethal, and viable patients require at least one hypomorphic (residual-activity) allele; the true birth prevalence is far lower and unquantified.

**Penetrance / expressivity.** Penetrance of biallelic pathogenic genotypes appears **complete**; **expressivity is variable** — from lethal early-infantile encephalopathy at the severe end to nonprogressive congenital ataxia at the mild end, tracking residual enzyme activity.

**Other genetic features.** **No genetic anticipation** (not a repeat-expansion disorder). **No established founder variant. Consanguinity** increases risk of homozygosity. **No sex predilection** (autosomal); reported cases include both sexes.

---

## 10. Diagnostics

**Genetic testing (primary/definitive).** DEE77 is diagnosed by **exome (WES) or genome (WGS) sequencing**, or by **targeted GPI-biosynthesis / epileptic-encephalopathy gene panels** that include *PIGQ*. Because *PIGQ* is intron-heavy, ES/WGS or panel capture is preferred over single-gene Sanger. Chromosomal microarray can detect rare 16p13.3 CNVs but is low-yield for the typical small biallelic variants. Reference transcript for variant reporting: **NM_004204.5**.

**Functional confirmation.** **Flow cytometry** demonstrating reduced surface GPI-anchored proteins on granulocytes/leukocytes and fibroblasts confirms pathogenicity and functional impact:

> *"Flow cytometry confirmed deficiency of several GPI-anchored proteins on leukocytes (CD14, FLAER)."* — [PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)

FLAER (fluorescent aerolysin, which binds GPI anchors directly), **CD16**, **CD14**, and **CD59/CD55** are standard markers.

**Laboratory / biomarkers.** Serum **alkaline phosphatase** may be elevated (hyperphosphatasia) in some IGD subtypes (variable in *PIGQ*). No specific circulating biomarker is validated for *PIGQ*-DEE77.

**Neuroimaging (diagnostic/prognostic).** Brain MRI is central:

> *"Prognostic and biologically significant neuroimaging features included cerebral atrophy (75%), cerebellar atrophy (60%), callosal anomalies (57%) and symmetric restricted diffusion of the central tegmental tracts (60%)."* — [PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)

**Electrophysiology.** **EEG** documents the epileptic encephalopathy (slow background; multifocal/continuous epileptiform activity; patterns including epilepsy of infancy with migrating focal seizures and myoclonic status).

**Clinical criteria / differential diagnosis.** No disease-specific criteria beyond genotype + GPI-flow-cytometry. Differential diagnosis includes **other inherited GPI deficiencies** (*PIGA, PIGT, PIGV, PIGO, PIGS, PIGW*, etc.), other early-infantile DEEs, congenital disorders of glycosylation, and pyridoxine-dependent epilepsies (ALDH7A1) — distinguished by gene-specific sequencing and GPI-anchored-protein assays.

**Screening.** No population newborn screening exists. **Cascade carrier testing** of relatives and **prenatal/preimplantation testing** are available once the familial biallelic variants are known.

---

## 11. Outcome / Prognosis

**Mortality.** Prognosis is **poor at the severe end**: premature death occurs in **>50%** of reported *PIGQ* patients ([PMID: 34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/)), and biallelic *PIGQ* variants were explicitly associated with increased mortality:

> *"Pathogenic biallelic PIGQ variants were associated with increased mortality."* — [PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)

In the pooled IGD cohort, 15/83 were deceased ([PMID: 38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/)). Deaths are typically from neurologic complications, status epilepticus, or surgical/systemic complications (e.g., midgut volvulus).

**Morbidity / function.** Survivors have **severe, lifelong disability**: profound developmental delay/intellectual disability, drug-resistant epilepsy, motor impairment (hypotonia, ataxia, dyskinesia), feeding difficulties, and sensory involvement (vision/hearing) in some. No validated QoL instruments have been applied.

**Recovery potential.** **Limited.** No disease-modifying therapy exists; the milder (nonprogressive) subgroup has a more stable but still impaired course.

**Prognostic factors.** **Residual GPI-biosynthetic activity / variant severity** is the principal prognostic determinant (severe LoF → early lethality; hypomorphic → milder ataxia). **Neuroimaging** features (cerebral/cerebellar atrophy, callosal anomalies, central-tegmental-tract diffusion restriction) are prognostically significant. **Neonatal onset and refractory seizures** portend worse outcome.

---

## 12. Treatment

**Overview.** There is **no cure and no disease-modifying therapy** for DEE77; management is **supportive and symptomatic** (anti-seizure medications, nutritional/feeding support, surgical correction of anomalies such as volvulus, developmental therapies). Epilepsy is frequently drug-resistant.

**Vitamin B6 (pyridoxine / pyridoxal-5′-phosphate; NCIT: Pyridoxine, C939).** A rational adjunct across IGD. A prospective compassionate-use cohort (Bayat et al. 2022; n=7 IGD, *PIGA/PIGT/PIGV*) using pyridoxine 20–30 mg/kg/day then P5P found partial benefit:

> *"We observed more than 50% seizure frequency reduction in 2 out of 7 and less than 50% reduction in another 3 out of 7 participants. No participants reached seizure freedom."* — [PMID: 35080266](https://pubmed.ncbi.nlm.nih.gov/35080266/)

> *"Early diagnosis and treatment are desirable because the disease progresses even after birth and vitamin B6(pyridoxine) is very effective for some patients with intractable seizures."* — [PMID: 26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/)

**Proof-of-concept targeted therapy (different GPI gene).** Restoring GPI-anchored protein expression can control IGD seizures — an HDAC inhibitor (butyrate) increased *PIGM* transcription and surface GPI expression:

> *"the drug caused complete cessation of intractable seizures in a child with inherited GPI deficiency."* — [PMID: 17442906](https://pubmed.ncbi.nlm.nih.gov/17442906/)

This is a mechanism-anchored strategy but has not been tested in *PIGQ*-DEE77.

**Folinic acid.** Mechanistically relevant because **folate receptor-α (FOLR1) is itself a GPI-anchored protein**; cerebral folate deficiency is treatable with folinic acid ([PMID: 19732866](https://pubmed.ncbi.nlm.nih.gov/19732866/)). Empirical benefit in *PIGQ*-DEE77 is unproven.

**Advanced / experimental therapeutics.** No gene therapy, cell therapy, RNA-based therapy, or *PIGQ*-targeted small molecule exists or is in trials. Highly purified cannabidiol has shown benefit in monogenic epilepsies broadly ([PMID: 40126049](https://pubmed.ncbi.nlm.nih.gov/40126049/)) but is not *PIGQ*-specific.

**Suggested NCIT clinical-intervention terms:** Pyridoxine (C939), Pyridoxal Phosphate (C61970), Anticonvulsant Agent (C264), Folinic Acid/Leucovorin (C576), Supportive Care (C15272).

---

## 13. Prevention

**Primary prevention.** There is **no way to prevent the biallelic genotype**; primary prevention is **reproductive** — **genetic counseling** for at-risk families (especially consanguineous couples) with **carrier testing**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT-M)** once familial *PIGQ* variants are known.

**Secondary prevention.** **Cascade genetic testing** of relatives; early molecular diagnosis to enable prompt supportive care and a trial of pyridoxine/P5P (rationale: the disease progresses postnatally, so early intervention is advocated — [PMID: 26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/)).

**Tertiary prevention.** Prevent complications: aggressive seizure management, surveillance and surgical correction of GI anomalies (volvulus), cardiac monitoring for arrhythmias, nutritional support, and developmental/rehabilitative therapies.

**Immunization / public-health / environmental interventions.** Not applicable (non-infectious, non-environmental Mendelian disorder). Standard childhood immunization for general health.

---

## 14. Other Species / Natural Disease

**Taxonomy.** No naturally occurring *PIGQ*-DEE77 has been described in companion animals or wildlife (no OMIA entry identified). GPI anchoring is universally essential across eukaryotes, so orthologs exist broadly. Human species: *Homo sapiens* (NCBI Taxon 9606); mouse: *Mus musculus* (NCBI Taxon 10090).

**Orthologous genes.** Mouse *Pigq* (ortholog of human *PIGQ*) exists; the pathway ortholog most studied for disease modeling is *Piga* (see §15).

**Comparative biology.** GPI-anchor biosynthesis is **deeply evolutionarily conserved** from yeast to humans; the essentiality of the pathway (embryonic lethality of complete knockout) is conserved, which is why disease modeling relies on conditional/tissue-specific approaches (§15).

**Zoonotic / transmission.** Not applicable — non-transmissible genetic disorder.

---

## 15. Model Organisms

**No *PIGQ*-specific animal model has been published.** Because complete GPI biosynthesis knockout is **embryonic-lethal** (GPI anchoring is essential for embryogenesis), disease modeling uses **conditional / tissue-specific knockouts** of pathway genes.

**Key mouse model (Kandasamy et al. 2021).** Neuron-type-specific GPI-deficiency mice were generated by conditional knockout of ***Piga*** — the gene catalyzing the same first, committed step of GPI biosynthesis in which PIGQ participates as a GPI-GnT subunit — in telencephalon excitatory neurons (Ex-M-cko), inhibitory neurons (In-M-cko), or thalamic neurons (Th-H-cko). These models recapitulate core DEE77 features:

> *"Both Ex-M-cko and In-M-cko mice showed impaired long-term fear memory and were more susceptible to kainic acid-induced seizures."* — [PMID: 33607654](https://pubmed.ncbi.nlm.nih.gov/33607654/)

> *"Phosphatidylinositol glycan biosynthesis class A protein (PIGA) catalyzes the very first step of GPI anchor biosynthesis. Patients carrying a mutation of the PIGA gene usually suffer from inherited glycosylphosphatidylinositol deficiency (IGD) with intractable epilepsy and intellectual developmental disorder."* — [PMID: 33607654](https://pubmed.ncbi.nlm.nih.gov/33607654/)

In-M-cko mice additionally showed a severe **limb-clasping** phenotype and Ex-M-cko mice showed hippocampal synapse changes.

**Model characteristics / recapitulation.** The neuronal GPI-deficiency mouse reproduces **seizure susceptibility and cognitive deficits** — the neurodevelopmental core of DEE77. **Limitations:** these use *Piga* (not its GPI-GnT partner *Pigq*), are conditional (not the constitutive biallelic human genotype), and do not capture the full multisystem congenital-anomaly spectrum (GI/cardiac/renal). In-vitro human models (patient fibroblasts and iPSC-derived systems) complement animal work: patient fibroblasts provided the definitive rescue experiment ([PMID: 32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/)).

**Model databases / resources:** MGI (*Pigq*, *Piga*), IMPC, IMSR.

---

## Mechanistic Model / Interpretation

```
  Biallelic hypomorphic/LoF PIGQ variants (16p13.3)
                │  (autosomal recessive; >=1 residual-activity allele in viable patients)
                v
  Reduced PIGQ subunit  ->  Impaired ER GPI-GnT complex (with PIGA, PIGC, PIGH, PIGP, DPM2, ARV1)
                │            [cytoplasmic face of ER membrane; GO:0005789]
                v
  Failure of 1st committed GPI step: PI + UDP-GlcNAc -> GlcNAc-PI
                │            [GPI anchor biosynthetic process; GO:0006506]
                v
  Global reduction in GPI anchor synthesis
                │
                v
  Deficient surface display of >150 GPI-anchored proteins
  (FLAER-binding anchors, CD16, CD14, CD59, FOLR1, ALPL, adhesion/signaling molecules)
                │
        +-------+--------------------------------+
        v (neuronal branch)                       v (systemic/developmental branch)
  Disrupted neuronal development,           Disrupted organogenesis
  synapse formation, excitability           │
        │                                    v
        v                             GI (volvulus 66%), cardiac (19%),
  Epilepsy (onset 2.5-7 mo, drug-          renal (14%) congenital anomalies
  resistant), hypotonia, GDD/ID,
  progressive cerebral/cerebellar
  atrophy, hypomyelination
        │                                    │
        +------------------+-----------------+
                           v
        DEE77 - early-infantile epileptic encephalopathy
        with multisystem anomalies; >50% premature mortality
                           │
                           v  (partial, non-curative)
        High-dose vitamin B6 (pyridoxine/P5P) -> partial seizure reduction in a subset
```

**Interpretation.** DEE77 is best understood as a **dosage/residual-activity disorder of the GPI-anchor pathway**. The *PIGQ* lesion is upstream and pathway-initiating; the phenotype is the aggregate downstream consequence of losing many functionally diverse GPI-anchored surface proteins simultaneously. Severity is a graded function of how much GPI biosynthesis survives — explaining the continuum from lethal early-infantile encephalopathy to nonprogressive ataxia. The neurodevelopmental prominence reflects the dependence of neuronal differentiation, synaptogenesis, and excitability control on GPI-anchored molecules, validated by conditional neuronal *Piga* knockout mice that reproduce seizure susceptibility and memory deficits. The partial pyridoxine responsiveness — shared across IGD — and the butyrate proof-of-concept in *PIGM* deficiency indicate the pathway is **pharmacologically modifiable in principle**, motivating mechanism-anchored therapy development.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [24463883](https://pubmed.ncbi.nlm.nih.gov/24463883/) | Clinical WGS in severe early-onset epilepsy | First link of recessive *PIGQ* (exon-skipping) to early-onset epileptic encephalopathy |
| [32588908](https://pubmed.ncbi.nlm.nih.gov/32588908/) | EIEE due to biallelic *PIGQ*: 7 new subjects | Defines core phenotype, onset, mortality; functional rescue proving causality |
| [34089469](https://pubmed.ncbi.nlm.nih.gov/34089469/) | *PIGQ*-related GPI deficiency with nonprogressive ataxia | Milder-end spectrum; molecular role of PIGQ; >50% premature death; flow-cytometry diagnosis; c.1631dupA variant |
| [40378954](https://pubmed.ncbi.nlm.nih.gov/40378954/) | ARV1 in GPI-GnT complex | Confirms PIGQ is a GPI-GnT component |
| [38456468](https://pubmed.ncbi.nlm.nih.gov/38456468/) | Clinical/genetic spectrum of IGD (n=83) | Pooled frequencies; neuroimaging prognostic features |
| [33607654](https://pubmed.ncbi.nlm.nih.gov/33607654/) | Neuronal GPI-deficiency mouse models | Model organism recapitulation of seizures + cognitive deficits |
| [11418246](https://pubmed.ncbi.nlm.nih.gov/11418246/) | Human *GPI1* required for efficient GPI biosynthesis | Establishes *GPI1*/*PIGQ* function; heterozygous deletion tolerance (recessive mechanism) |
| [35080266](https://pubmed.ncbi.nlm.nih.gov/35080266/) | Pyridoxine/P5P for GPI-deficiency seizures | Quantifies partial B6 efficacy |
| [26165085](https://pubmed.ncbi.nlm.nih.gov/26165085/) | Inherited GPI deficiency overview | Postnatal progression; B6 effectiveness in a subset |
| [17442906](https://pubmed.ncbi.nlm.nih.gov/17442906/) | Targeted therapy for inherited GPI deficiency | Proof-of-concept: restoring GPI expression controls seizures |
| [19732866](https://pubmed.ncbi.nlm.nih.gov/19732866/) | FOLR1 cerebral folate transport deficiency | FOLR1 is GPI-anchored → folinic-acid rationale |

Evidence source types: **human clinical** (24463883, 32588908, 34089469, 38456468, 35080266, 26165085, 17442906, 19732866), **in vitro** (32588908 fibroblast rescue; 11418246 HEK293 antisense), **model organism** (33607654), **computational** (gnomAD constraint, ClinVar and OLS queries performed during the investigation).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare evidence base.** Fewer than ~20 *PIGQ* patients are reported; most quantitative frequencies (seizures 83%, DD/ID 90%, etc.) come from the **broader IGD cohort** (Sidpra 2024), not *PIGQ*-specific data. *PIGQ*-specific frequencies, penetrance, and natural history are imprecise.
2. **No formal epidemiology.** No validated prevalence/incidence; the gnomAD-derived carrier estimate (~1/286) overestimates disease because it ignores embryonic lethality of complete null and the requirement for a hypomorphic allele.
3. **No *PIGQ*-specific animal model.** Modeling relies on *Piga* conditional knockouts; genotype–phenotype fidelity for *PIGQ* is inferred, not demonstrated.
4. **Therapeutics extrapolated.** Pyridoxine/P5P and butyrate evidence comes from other GPI genes (*PIGA/PIGT/PIGV/PIGM*); no *PIGQ*-specific trial exists. Folinic-acid benefit is mechanistic conjecture.
5. **Genotype–phenotype correlation** (which variants give the severe vs. mild spectrum) is not systematically established; residual-activity assays per variant are lacking.
6. **QoL and long-term outcome** are not measured with standardized instruments.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble a *PIGQ*-specific patient registry** (via GeneMatcher/consortia) to derive gene-specific phenotype frequencies, survival curves, and genotype–phenotype correlations.
2. **Variant-level functional assays.** Quantify residual GPI biosynthesis for each reported *PIGQ* variant (flow cytometry for surface GPI-APs in patient/edited cells) to build a severity-prediction model that would refine prognosis and counseling.
3. **Generate a *Pigq* mouse (or zebrafish) model** — conditional/hypomorphic neuronal knockouts — to directly test *PIGQ* (vs *Piga*) mechanism and the multisystem anomalies (GI/cardiac/renal).
4. **Prospective pyridoxine/P5P trial in *PIGQ*-DEE77**, with EEG/seizure-diary endpoints and GPI-AP flow-cytometry biomarkers, to test whether the subset-benefit seen in other IGDs extends to *PIGQ*.
5. **Test pathway-restoring agents** (HDAC inhibitors as in *PIGM*; substrate/precursor supplementation) in patient iPSC-derived neurons/organoids for *PIGQ*-specific rescue.
6. **Evaluate folinic acid** empirically, given FOLR1's GPI dependence, measuring CSF 5-MTHF where feasible.
7. **Standardize diagnostic workup**: recommend GPI-AP flow cytometry (FLAER/CD16/CD14) as reflex confirmation after ES/WGS identifies biallelic *PIGQ* variants, plus MRI for prognostic atrophy/tract markers.

---

*Report compiled from 9 confirmed findings and 37 reviewed papers across a 5-iteration autonomous investigation. All mechanistic and clinical claims are anchored to primary literature (PMIDs above) with verified abstract quotations.*


## Artifacts

- [OpenScientist final report](Developmental_And_Epileptic_Encephalopathy_77-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Developmental_And_Epileptic_Encephalopathy_77-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032808` (3 mentions) - the report calls it "MONDO"; MONDO calls it **developmental and epileptic encephalopathy, 77**
- `DOID:0112213` (1 mention) - the report calls it "DOID"; DOID calls it **multiple congenital anomalies-hypotonia-seizures syndrome 4**
- `CL:0000775` (1 mention) - the report calls it "diagnostic readout"; CL calls it **neutrophil**
- `CL:0000057` (1 mention) - the report calls it "diagnostic readout"; CL calls it **fibroblast**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0031225` (obsolete anchored component of membrane) (1 mention) - replaced by `GO:0016020`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005789` (3 mentions) - the report calls it "endoplasmic reticulum membrane, cytoplasmic face"; GO calls it **endoplasmic reticulum membrane**
- `UBERON:0001555` (1 mention) - the report calls it "Gastrointestinal tract"; UBERON calls it **digestive tract**
- `GO:0031225` (1 mention) - the report calls it "anchored component of the plasma membrane"; GO calls it **obsolete anchored component of membrane**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:14135` - called "HGNC (gene)", "HGNC"