---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T03:14:53.801684'
end_time: '2026-09-30T03:51:08.519339'
duration_seconds: 2174.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Septic Peritonitis
  mondo_id: MONDO:0005195
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
  quotes_checked: 15
  quotes_valid: 15
  relevance_assessed: 39
  on_topic: 27
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 49
  verified: 49
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 16
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0025380
    reported_labels:
    - Abdominal guarding
    ontology_label: Increased circulating androstenedione concentration
  - term_id: CL:0000771
    reported_labels:
    - B-1a cell
    ontology_label: eosinophil
  - term_id: NCIT:C51674
    reported_labels:
    - Drainage Procedure
    ontology_label: Endomyocardial Biopsy
  - term_id: NCIT:C157715
    reported_labels:
    - Debridement
    ontology_label: Total Gut Decontamination
  - term_id: NCIT:C1878
    reported_labels:
    - Imipenem
    ontology_label: Darbepoetin Alfa
  - term_id: NCIT:C1737
    reported_labels:
    - Cefotaxime
    ontology_label: Organic Solvents
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Septic_Peritonitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Septic_Peritonitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Septic Peritonitis
- **MONDO ID:** MONDO:0005195 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Septic Peritonitis** covering all of the
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

# Septic Peritonitis (MONDO:0005195): A Comprehensive Disease Characterization Report

## Summary

**Septic peritonitis is a life-threatening bacterial infection of the peritoneal cavity, most commonly arising as *secondary* peritonitis from disruption of the gastrointestinal tract (perforation, ischemia, dehiscence, or penetrating trauma).** Contamination of the normally sterile peritoneum with polymicrobial gut flora triggers a dysregulated innate-immune response—pathogen-associated molecular patterns (PAMPs) such as lipopolysaccharide (LPS) activating resident peritoneal macrophages and mesothelium via Toll-like receptor/NF-κB signaling, releasing a cytokine cascade (TNF-α, IL-1β, IL-6, HMGB1) with massive neutrophil recruitment. When this response becomes systemic and dysregulated, it produces **sepsis**—defined by Sepsis-3 as "life-threatening organ dysfunction caused by a dysregulated host response to infection"—and can progress to septic shock and multiple organ dysfunction syndrome (MODS). The **abdomen is the second most common source of sepsis**, and intra-abdominal infections carry hospital mortality of 23–38%, rising above 80% in severe complicated intra-abdominal sepsis (SCIAS).

This report is derived from **aggregated disease-level resources** (clinical guidelines, cohort studies, systematic reviews, and experimental model literature)—not individual patient EHR records. Importantly, septic peritonitis is an **infectious/mechanical disease, not a Mendelian genetic disorder**: it has no causal gene, no inheritance pattern, no pathogenic variant class, and no vaccine. Genetic contributions are limited to polygenic host-susceptibility modifiers of the sepsis response. Consequently, several sections of the standard disease template (causal genes, pathogenic variants, chromosomal abnormalities, repeat-expansion testing, genetic counseling) are **not applicable** and are marked as such.

The two therapeutic pillars are **source control** (surgical debridement, drainage, removal of infected devices, decompression) and **early broad-spectrum empiric antibiotics with resuscitation**. Source control is the dominant determinant of survival: in postoperative intra-abdominal infection, eliminating the infection source reduced mortality from 100% to 19%. The landmark STOP-IT trial showed that ~4 days of antibiotics suffice after adequate source control. Septic peritonitis is also a **common, high-mortality naturally occurring disease in dogs and cats** (overall mortality ~64% in GI-perforation cases), where it is elegantly diagnosed by a **blood-to-peritoneal-fluid glucose difference >20 mg/dL** (100% sensitive/specific in dogs). The gold-standard experimental model is **cecal ligation and puncture (CLP)** in mice.

---

## 1. Disease Information

**Overview.** Septic peritonitis is inflammation of the peritoneum (the serous membrane lining the abdominal cavity and viscera) caused by bacterial infection, most often following breach of a hollow viscus. It is a form of **intra-abdominal infection (IAI)** and, when the host response becomes dysregulated, of **abdominal sepsis**. Intra-abdominal infections "account for a major cause of morbidity and mortality, representing the second most common sepsis-related death with a hospital mortality of 23-38%" ([PMID: 39200076](https://pubmed.ncbi.nlm.nih.gov/39200076/)).

**Key identifiers.**
- **MONDO:** MONDO:0005195
- **MeSH:** Peritonitis (D010538)
- **ICD-10:** K65 (Peritonitis); K65.0 (Generalized/acute peritonitis); K65.1 (Peritoneal abscess); K65.9 (Peritonitis, unspecified)
- **ICD-11:** DC50 (Peritonitis)
- **SNOMED CT:** 48661000 (Peritonitis); 65119005 (Bacterial peritonitis)
- **OMIM / Orphanet:** Not applicable — septic peritonitis is an acquired infectious/surgical condition, not a Mendelian or rare genetic disease, so it has no OMIM phenotype number and no Orphanet ORPHA code.

**Synonyms / alternative names.** Bacterial peritonitis; suppurative peritonitis; secondary peritonitis (most relevant subtype); acute bacterial peritonitis; purulent peritonitis; abdominal sepsis / intra-abdominal sepsis (when systemic); surgical peritonitis. Related but distinct: spontaneous bacterial peritonitis (SBP, the *primary* form), tertiary peritonitis.

**Source of information.** Aggregated disease-level resources — clinical guidelines (WSES, Surviving Sepsis), retrospective and prospective cohort studies, systematic reviews, and experimental animal-model literature.

---

## 2. Etiology

**Primary causal factors — infectious and mechanical.** The proximate cause is **microbial contamination of the sterile peritoneal cavity**, overwhelmingly from a breach of the gastrointestinal tract. "Secondary peritonitis is a life-threatening intra-abdominal condition arising from gastrointestinal perforation, chemical injury, or catheter-related infections" ([PMID: 41227298](https://pubmed.ncbi.nlm.nih.gov/41227298/)). Common precipitating lesions include perforated peptic ulcer, perforated appendicitis, perforated diverticulitis, bowel ischemia/necrosis, anastomotic dehiscence after GI surgery, penetrating/blunt abdominal trauma, and perforated malignancy. The infection is typically **polymicrobial**, reflecting gut flora (*Escherichia coli* and other Enterobacterales, *Bacteroides fragilis* and anaerobes, enterococci; *Candida* in upper-GI perforation).

**Genetic risk factors.** There are **no causal Mendelian variants or established susceptibility loci** specific to septic peritonitis. As an acquired infection, risk is governed by the anatomical lesion and by polygenic host modifiers of the innate-immune/sepsis response (e.g., variants in TLR4, TNF, IL-6 pathways have been studied in sepsis generally, but none are diagnostic or actionable for peritonitis). This section is largely **not applicable**.

**Environmental / clinical risk factors.**
- **Medications:** Non-steroidal anti-inflammatory drugs (NSAIDs) and corticosteroids promote GI ulceration/perforation. In companion animals, "administration of anti-inflammatory drugs in dogs and cats is a significant risk factor for pyloric perforation" ([PMID: 24283417](https://pubmed.ncbi.nlm.nih.gov/24283417/)).
- **Comorbidities:** diabetes mellitus, immunosuppression, malignancy, diverticular disease, peptic ulcer disease, cirrhosis (predisposes to the primary/SBP form).
- **Procedural:** recent abdominal surgery, peritoneal dialysis catheters, foreign-body migration (e.g., grass awns in animals; [PMID: 36874536](https://pubmed.ncbi.nlm.nih.gov/36874536/)).
- **Demographic:** advancing age (higher perforation and mortality risk).

**Protective factors.** No genetic protective variants are established. Protective/beneficial factors are effectively **preventive and therapeutic**: prompt surgical source control, early appropriate antibiotics, and management of predisposing GI disease. There is no dietary or vaccine-based primary prevention.

**Gene–environment interactions.** Not established as clinically meaningful. Host genetic modulation of the cytokine response may interact with pathogen burden to influence sepsis severity, but this is speculative for peritonitis specifically and not actionable.

---

## 3. Phenotypes

Septic peritonitis presents acutely with a constellation of peritoneal signs and systemic sepsis features. In a comparative study of acute abdomen, "common signs were tenderness, rebound tenderness, guarding/rigidity, tachycardia, and abdominal distention" ([PMID: 42583660](https://pubmed.ncbi.nlm.nih.gov/42583660/)).

| Phenotype | Type | HPO suggestion | Frequency/severity | Onset/progression |
|---|---|---|---|---|
| Abdominal pain | Symptom | HP:0002027 (Abdominal pain) | Near-universal; severe | Acute; progressive |
| Rebound tenderness / peritoneal signs | Clinical sign | HP:0002027 | Very common | Acute |
| Abdominal guarding/rigidity | Clinical sign | HP:0025380 (Abdominal guarding) | Common | Acute |
| Fever | Sign | HP:0001945 (Fever) | Common | Acute; may be absent/hypothermia in severe sepsis |
| Nausea and vomiting | Symptom | HP:0002018 / HP:0002013 | Common | Acute |
| Anorexia | Symptom | HP:0002039 (Anorexia) | Common | Acute |
| Tachycardia | Sign | HP:0001649 (Tachycardia) | Common | Acute |
| Abdominal distension | Sign | HP:0003270 (Abdominal distention) | Common | Acute/subacute |
| Hypotension / septic shock | Sign | HP:0002615 (Hypotension) | In severe disease | Acute; life-threatening |
| Leukocytosis (or leukopenia) | Lab abnormality | HP:0001974 / HP:0001882 | Common | Acute |
| Elevated CRP / procalcitonin | Lab abnormality | HP:0011227 (Elevated CRP) | Common | Acute |
| Lactic acidosis | Lab abnormality | HP:0003128 (Lactic acidosis) | Severe disease; prognostic | Acute |
| Multi-organ dysfunction | Complication | HP:0011024 (GI), HP:0000083 (Renal insufficiency) | Severe/tertiary | Progressive |

**Age of onset.** Any age; predominantly adult and geriatric (matching perforation risk). Neonatal forms occur secondary to necrotizing enterocolitis-associated intestinal perforation.

**Severity/progression.** Acute onset, rapidly progressive; if untreated, escalates to septic shock and MODS within hours to days. **Quality-of-life impact** in the acute phase is severe (ICU-level illness); survivors of abdominal sepsis may experience prolonged recovery, post-intensive-care syndrome, and long hospital stays. Disease-specific QoL instruments are not standard; generic ICU/sepsis outcome measures apply.

---

## 4. Genetic/Molecular Information

**This section is largely NOT APPLICABLE.** Septic peritonitis is an acquired infectious disease with:
- **No causal genes** (no OMIM gene entries).
- **No pathogenic variants** (no ClinVar classifications, no ACMG/AMP-relevant germline or somatic variants, no allele-frequency considerations).
- **No chromosomal abnormalities.**
- **No disease-specific epigenetic signature** established as diagnostic.

**Modifier genes (host susceptibility, research-level only).** Polygenic variation in innate-immune signaling (TLR4/CD14/LBP–LPS recognition, TNF, IL6, IL1B, NLR-family inflammasome genes) modulates the intensity of the sepsis response but is neither diagnostic nor actionable. Experimental work implicates inflammasome and receptor genes in host defense—e.g., **NLRC4** deficiency improved survival and bacterial clearance in CLP-induced polymicrobial sepsis ([PMID: 41071588](https://pubmed.ncbi.nlm.nih.gov/41071588/)), and **CD300ld** modulates neutrophil bacterial phagocytosis ([PMID: 40376837](https://pubmed.ncbi.nlm.nih.gov/40376837/))—but these are mechanistic/model findings, not human germline disease genes.

---

## 5. Environmental Information

**Environmental / iatrogenic factors.** NSAIDs and corticosteroids (GI ulceration), abdominal surgery, peritoneal dialysis catheters, and intra-abdominal foreign bodies. No environmental toxin, radiation, or pollutant is a recognized cause.

**Lifestyle factors.** Alcohol use (pancreatitis, cirrhosis/SBP risk), smoking (peptic ulcer disease). Diet-related diverticular disease contributes to perforated diverticulitis.

**Infectious agents (the direct cause of secondary septic peritonitis).** Typically **polymicrobial enteric flora**:
- **Gram-negative bacteria (NCBI Taxonomy):** *Escherichia coli* (NCBI:txid562) — most common; *Klebsiella*, *Enterobacter*, *Proteus*, *Pseudomonas aeruginosa*.
- **Anaerobes:** *Bacteroides fragilis*, *Clostridium* spp.
- **Gram-positive:** *Enterococcus* spp., streptococci, *Staphylococcus aureus* (esp. PD-associated).
- **Fungi:** *Candida* spp., particularly in upper-GI (gastric/duodenal) perforation and tertiary peritonitis.

In companion-animal septic peritonitis, microbial growth occurred in the large majority of peritoneal cultures, with agents effectively covered by cefotaxime, ceftazidime, and imipenem ([PMID: 30040445](https://pubmed.ncbi.nlm.nih.gov/30040445/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **GI-tract lesion** (perforated ulcer, ruptured appendix/diverticulum, ischemic/necrotic bowel, anastomotic dehiscence, penetrating trauma) **leads to** spillage of luminal contents and gut flora into the sterile peritoneal cavity. *(demonstrated)*
2. **Bacterial contamination + PAMPs (e.g., LPS)** *results in* recognition by resident peritoneal macrophages and mesothelial cells via pattern-recognition receptors (TLR4/CD14) **→** NF-κB activation. *(inferred from sepsis biology; supported by biomarker data)*
3. NF-κB activation *leads to* release of **pro-inflammatory cytokines (TNF-α, IL-1β, IL-6) and alarmins (HMGB1)** and chemokines, *causing* massive **neutrophil recruitment** into the peritoneum. *(supported — biomarkers PCT, IL-6, HMGB1, CRP, LPS, NLR, NGAL elevated; [PMID: 41227298](https://pubmed.ncbi.nlm.nih.gov/41227298/))*
4. **Branch A (local):** Inflammation shifts the peritoneal **coagulation–fibrinolysis balance toward coagulation**; "both surgery and peritonitis disturb the equilibrium between coagulation and fibrinolysis in the abdominal cavity in favour of the coagulation system," and "diminished fibrin degradation is a common pathway for the formation of adhesions and abscesses" ([PMID: 12734857](https://pubmed.ncbi.nlm.nih.gov/12734857/)). *This results in* fibrin deposition, loculation, **abscess and adhesion formation** — walling off infection but also creating protected bacterial niches. *(demonstrated)*
5. **Branch B (systemic):** Unchecked, cytokines spill into the circulation, *causing* a **dysregulated systemic host response = sepsis** ("life-threatening organ dysfunction caused by a dysregulated host response to infection"; [PMID: 30685836](https://pubmed.ncbi.nlm.nih.gov/30685836/)). *(demonstrated)*
6. Systemic inflammation *leads to* **vasodilation, capillary leak, microvascular thrombosis, and hypoperfusion** → **septic shock** and **tissue ischemia/oxidative injury**. *(inferred/demonstrated in sepsis)*
7. Hypoperfusion + direct cytokine injury *result in* **multiple organ dysfunction syndrome (MODS)** — acute kidney injury, ARDS, septic cardiomyopathy, hepatic dysfunction, DIC. Septic cardiomyopathy is a documented complication of small-intestinal perforation with peritonitis ([PMID: 42260799](https://pubmed.ncbi.nlm.nih.gov/42260799/)). *(demonstrated)*
8. **Immune trajectory:** After the hyperinflammatory phase, "most patients survive the hyperinflammatory phase but progress to an immunosuppressive phase, which increases the emergence of secondary infections" ([PMID: 31259890](https://pubmed.ncbi.nlm.nih.gov/31259890/)), *leading to* tertiary peritonitis and late mortality. *(demonstrated)*
9. Endpoint: **death from refractory shock, MODS, or secondary infection** unless the causal chain is interrupted by source control + antibiotics. "Mortality typically results from disruption of the gastrointestinal tract, progressive and self-perpetuating bio-mediator generation, systemic inflammation, and multiple organ failure" ([PMID: 37170123](https://pubmed.ncbi.nlm.nih.gov/37170123/)). *(demonstrated)*

### Category detail

- **Molecular pathways:** TLR4/CD14–LPS → MyD88 → NF-κB; downstream MAPK signaling; inflammasome (NLRC4, NLRP3) → caspase-1 → IL-1β/IL-18 maturation. TNF can switch homeostatic efferocytosis to lytic caspase-8–dependent pyroptosis with IL-1β maturation ([PMID: 40540586](https://pubmed.ncbi.nlm.nih.gov/40540586/)).
- **Cellular processes:** acute inflammation, phagocytosis, neutrophil extracellular trap formation, pyroptosis/apoptosis, efferocytosis, later immunosuppression.
- **Immune involvement:** central — innate immunity (macrophages, neutrophils, mesothelium) drives both protection and pathology; adaptive dysfunction (T-cell exhaustion, B-1a cell depletion via neutrophil trogocytosis; [PMID: 40568588](https://pubmed.ncbi.nlm.nih.gov/40568588/)) characterizes the immunosuppressive phase.
- **Tissue damage mechanisms:** oxidative stress, ischemia/hypoperfusion, microvascular thrombosis, fibrin-driven abscess/adhesion, necrosis.
- **GO term suggestions:** GO:0006954 (inflammatory response), GO:0032496 (response to lipopolysaccharide), GO:0007249 (NF-κB signaling), GO:0006909 (phagocytosis), GO:0070269 (pyroptosis), GO:0007596 (blood coagulation), GO:0042060 (wound healing/adhesion).
- **CL term suggestions:** CL:0000864 (tissue-resident macrophage), CL:0000775 (neutrophil), CL:0000077 (mesothelial cell), CL:0000771 (B-1a cell), CL:0000084 (T cell).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** peritoneum (UBERON:0002358, parietal peritoneum; UBERON:0002357, serosa) and the perforated hollow viscus (stomach UBERON:0000945, small intestine UBERON:0002108, large intestine/colon UBERON:0001155, appendix UBERON:0001154).
- **Secondary (complications):** kidney (UBERON:0002113, AKI), lung (UBERON:0002048, ARDS), heart (UBERON:0000948, septic cardiomyopathy), liver (UBERON:0002107), spleen (UBERON:0002106), systemic vasculature.
- **Body systems:** digestive (primary), immune/hematologic, cardiovascular, respiratory, renal/urinary — reflecting multi-system sepsis.

**Tissue and cell level.** Mesothelial lining (epithelial-like serosa), submesothelial connective tissue and vasculature; infiltrating **neutrophils (CL:0000775)** and **peritoneal macrophages (CL:0000864)**; **B-1a cells (CL:0000771)** in serosal cavities.

**Subcellular level.** Mitochondrial dysfunction (bioenergetic failure in sepsis; GO:0005739), nucleus (NF-κB translocation; GO:0005634), inflammasome assembly in cytosol (GO:0005829), plasma-membrane receptor complexes (TLR4; GO:0005886).

**Localization / lateralization.** Peritonitis is typically **diffuse/generalized (bilateral, non-lateralized)** when spillage is widespread, or **localized** (e.g., abscess) when contained. Free intra-abdominal air and diffuse fluid indicate generalized perforation peritonitis.

---

## 8. Temporal Development

- **Onset:** acute or subacute (hours to a few days). Insidious onset can occur in immunosuppressed or postoperative patients.
- **Stages:** (1) contamination/local peritonitis → (2) systemic inflammatory/hyperinflammatory sepsis → (3) septic shock/MODS → (4) either resolution (with treatment) or immunosuppressive/tertiary phase with secondary infection.
- **Progression rate:** rapid; can be fulminant, particularly with delayed source control.
- **Course pattern:** acute, potentially self-limited *only* with definitive intervention; otherwise progressive and fatal.
- **Remission:** treatment-induced (source control + antibiotics); no spontaneous remission for established secondary septic peritonitis.
- **Critical periods:** the **early window for source control and antibiotics is decisive** — delay markedly worsens outcome; the transition from hyperinflammatory to immunosuppressive phase is a second window of vulnerability to secondary infection.

---

## 9. Inheritance and Population

**Epidemiology.** Septic peritonitis/abdominal sepsis is common and globally important. The **abdomen is the second most common source of sepsis** ([PMID: 30685836](https://pubmed.ncbi.nlm.nih.gov/30685836/)), and sepsis overall is a leading cause of death: GBD 2017 estimated ~**48.9 million incident sepsis cases and 11 million sepsis-related deaths** worldwide, "a major cause of health loss" ([PMID: 31954465](https://pubmed.ncbi.nlm.nih.gov/31954465/)). IAIs carry hospital mortality of 23–38% ([PMID: 39200076](https://pubmed.ncbi.nlm.nih.gov/39200076/)), and SCIAS mortality can exceed 80% ([PMID: 37170123](https://pubmed.ncbi.nlm.nih.gov/37170123/)).

**Genetic etiology — NOT APPLICABLE.** No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency. Septic peritonitis is acquired.

**Population demographics.** Risk rises with age and with predisposing GI disease. No strong ethnic predisposition to the infection itself (although access to timely surgery/critical care strongly affects outcomes and drives geographic mortality variation). Sex distribution roughly reflects the underlying etiology (e.g., perforated ulcer, diverticulitis, appendicitis). Geographic variation in outcome is driven by healthcare access rather than by genetic epidemiology.

---

## 10. Diagnostics

**Clinical examination.** Acute abdomen with tenderness, rebound tenderness, guarding/rigidity, distension, tachycardia, and often fever ([PMID: 42583660](https://pubmed.ncbi.nlm.nih.gov/42583660/)).

**Laboratory tests / biomarkers.** Leukocytosis or leukopenia, elevated CRP and **procalcitonin (PCT)**, IL-6, HMGB1, LPS, elevated **neutrophil-to-lymphocyte ratio (NLR)**, NGAL, and lactate. "Biomarkers such as procalcitonin (PCT), interleukin-6 (IL-6), high mobility group box 1 (HMGB1), C-reactive protein (CRP), lipopolysaccharide (LPS), neutrophil-to-lymphocyte ratio (NLR), and neutrophil gelatinase-associated lipocalin (NGAL) have emerged as tools for early diagnosis, subtype stratification, and monitoring of therapeutic response" ([PMID: 41227298](https://pubmed.ncbi.nlm.nih.gov/41227298/)). LOINC-codable: WBC, CRP, PCT, lactate.

**Imaging.** **CT is the imaging modality of choice** — more sensitive than plain radiography for pneumoperitoneum. "Free intra-abdominal air in combination with diffuse fluid is a reliable indication for surgery as it is strongly associated with perforated diverticulitis with generalized peritonitis" ([PMID: 22752330](https://pubmed.ncbi.nlm.nih.gov/22752330/)). In gastroduodenal perforation, free intraperitoneal air is a direct sign ([PMID: 15093233](https://pubmed.ncbi.nlm.nih.gov/15093233/)); CT is more sensitive than plain films for detecting free air even in peritoneal-dialysis patients ([PMID: 8188913](https://pubmed.ncbi.nlm.nih.gov/8188913/)).

**Peritoneal fluid analysis (diagnostic cornerstone).** Neutrophilic exudate; **cytologic identification of intracellular bacteria is confirmatory**. In veterinary medicine, a **blood-to-fluid glucose difference >20 mg/dL was 100% sensitive and 100% specific** for septic peritoneal effusion in dogs, and a **blood-to-fluid lactate difference < −2.0 mmol/L was also 100% sensitive/specific** ([PMID: 12692761](https://pubmed.ncbi.nlm.nih.gov/12692761/)). Point-of-care peritoneal culture has ~80% sensitivity/100% specificity ([PMID: 34331824](https://pubmed.ncbi.nlm.nih.gov/34331824/)). For the *primary* (SBP) form, diagnosis is an ascitic-fluid neutrophil count **>250 cells/mm³** ([PMID: 42488876](https://pubmed.ncbi.nlm.nih.gov/42488876/), [PMID: 42565189](https://pubmed.ncbi.nlm.nih.gov/42565189/)).

**Genetic / omics diagnostics — NOT APPLICABLE** for diagnosis of the infection (no WGS/WES/panel/karyotype/FISH/mtDNA/repeat-expansion role). Microbiologic culture and, increasingly, metagenomic next-generation sequencing (mNGS) of fluid can identify pathogens (mNGS sensitivity 65.8% vs culture 36.8% in PD-related peritonitis; [PMID: 39611142](https://pubmed.ncbi.nlm.nih.gov/39611142/)).

**Clinical criteria / scoring.** Diagnosis is clinical + imaging + fluid analysis. Severity/prognosis are graded by **APACHE II** and **Mannheim Peritonitis Index (MPI)**, plus Sepsis-3/SOFA. **Differential diagnosis:** non-septic causes of acute abdomen (pancreatitis, ischemia without perforation, epiploic appendagitis, primary SBP, chemical peritonitis).

---

## 11. Outcome / Prognosis

**Mortality.** High and driven by source-control success and physiologic derangement. In severe secondary peritonitis, mortality was ~38%; **APACHE II (19.6 vs 14.3; p=0.0015) and MPI (35.5 vs 27.8; p=0.001) were significantly higher in non-survivors**, and MPI was the only independent multivariate risk factor ([PMID: 21988045](https://pubmed.ncbi.nlm.nih.gov/21988045/)). Multivariate analysis of 604 IAI patients confirmed the prognostic dominance of host-related factors and the value of APACHE II and MPI ([PMID: 8645072](https://pubmed.ncbi.nlm.nih.gov/8645072/)).

**Source control is the dominant prognostic factor.** In postoperative IAI, "in 37 of the patients the source of infection was eliminated resulting in 7 deaths (19%); all 11 of those in whom it was not eliminated died" ([PMID: 8891619](https://pubmed.ncbi.nlm.nih.gov/8891619/)).

**Prognostic factors:** age, physiologic severity (APACHE II, SOFA), MPI, adequacy/timeliness of source control, organ dysfunction, fungal involvement (worse outcomes; [PMID: 38691220](https://pubmed.ncbi.nlm.nih.gov/38691220/)), and serial peritoneal-fluid variables (in dogs, lower abdominal-fluid WBC and higher blood-to-fluid WBC/neutrophil ratios predicted recurrent septic peritonitis; [PMID: 27556266](https://pubmed.ncbi.nlm.nih.gov/27556266/)).

**Complications:** septic shock, MODS (AKI, ARDS, septic cardiomyopathy, DIC, hepatic dysfunction), intra-abdominal abscess/adhesions, tertiary peritonitis, secondary/nosocomial infection, and long-term post-sepsis morbidity.

---

## 12. Treatment

**Two pillars: source control + early antibiotics/resuscitation.**

**Surgical / interventional source control (the therapeutic gold standard).** "The 'old' surgical source control consisting of debridement, removal of infected devices, drainage of purulent cavities, and decompression of the abdominal cavity is the gold standard of surgical care" ([PMID: 30685836](https://pubmed.ncbi.nlm.nih.gov/30685836/)). Modalities include exploratory laparotomy with repair/resection of the perforated viscus, peritoneal lavage, percutaneous abscess drainage, and open-abdomen management. **Vacuum-assisted closure (VAC)** is a feasible open-abdomen technique in veterinary septic peritonitis ([PMID: 22474052](https://pubmed.ncbi.nlm.nih.gov/22474052/)). NCIT suggestions: NCIT:C15329 (Surgery), NCIT:C51674 (Drainage Procedure), NCIT:C157715 (Debridement). Note: rapid source-control laparotomy is not universally beneficial and should be applied selectively ([PMID: 28846501](https://pubmed.ncbi.nlm.nih.gov/28846501/)).

**Pharmacotherapy — empiric broad-spectrum antibiotics.** Cover Gram-negative enterics and anaerobes (± enterococci/fungi by risk). Agents shown effective against peritoneal isolates include **cefotaxime, ceftazidime, and imipenem** ([PMID: 30040445](https://pubmed.ncbi.nlm.nih.gov/30040445/)); typical human regimens include beta-lactam/beta-lactamase inhibitors, carbapenems, or cephalosporin+metronidazole, with antifungals for upper-GI/tertiary disease. **Duration:** the landmark **STOP-IT** RCT found "four days of antibiotics for source-controlled complicated intra-abdominal infection resulted in similar outcomes when compared with a longer duration," including in high-risk patients ([PMID: 27670577](https://pubmed.ncbi.nlm.nih.gov/27670577/)). NCIT: NCIT:C258 (Antibiotic), NCIT:C1878 (Imipenem), NCIT:C1737 (Cefotaxime).

**Supportive/critical care.** Fluid resuscitation, vasopressors, source-directed antibiotics, organ support (renal replacement therapy, mechanical ventilation, inotropes/mechanical support for septic cardiomyopathy — as in the multimodal rescue described in [PMID: 42260799](https://pubmed.ncbi.nlm.nih.gov/42260799/)), and nutritional support, per Surviving Sepsis principles.

**Experimental / adjunctive therapeutics (model-stage).** Immunomodulation strategies tested in CLP and other models include soluble CD6 receptor ([PMID: 27895015](https://pubmed.ncbi.nlm.nih.gov/27895015/)), the hCG-related peptide LQGV ([PMID: 20890188](https://pubmed.ncbi.nlm.nih.gov/20890188/)), trophoblast stem cells ([PMID: 40691621](https://pubmed.ncbi.nlm.nih.gov/40691621/)), CD300ld-based neutrophil enhancement ([PMID: 40376837](https://pubmed.ncbi.nlm.nih.gov/40376837/)), and trained-immunity neutrophil reprogramming ([PMID: 41980372](https://pubmed.ncbi.nlm.nih.gov/41980372/)). None are yet standard human therapy. For PD-associated recurrent peritonitis, taurolidine-urokinase lock therapy shows promise ([PMID: 40988813](https://pubmed.ncbi.nlm.nih.gov/40988813/)).

**Pharmacogenomics / gene / cell / RNA / targeted / immunotherapy:** NOT APPLICABLE as approved disease-specific therapies.

---

## 13. Prevention

- **Primary prevention:** treat/prevent predisposing GI disease (peptic ulcer prophylaxis, judicious NSAID/steroid use, timely management of appendicitis/diverticulitis), aseptic technique for PD catheters, and prompt surgery for at-risk lesions. There is **no vaccine**.
- **Secondary prevention:** early recognition and treatment of GI perforation/ischemia before diffuse peritonitis develops; sepsis screening protocols.
- **Tertiary prevention:** meticulous source control, appropriate antibiotic stewardship (STOP-IT short-course), prevention of secondary/nosocomial infection during the immunosuppressive phase, and monitoring for abscess/adhesion complications.
- **Public health:** access to timely surgical and critical care is the key determinant of survival and the main lever for reducing geographic mortality disparities.
- **Genetic screening / counseling / immunization:** NOT APPLICABLE.

---

## 14. Other Species / Natural Disease

Septic peritonitis is a **common, high-mortality naturally occurring disease in companion animals**, making veterinary data unusually informative.

- **Taxonomy:** dog (*Canis lupus familiaris*, NCBI:txid9615), cat (*Felis catus*, NCBI:txid9685); mouse (*Mus musculus*, NCBI:txid10090) and rat as experimental hosts; zebrafish (*Danio rerio*, NCBI:txid7955) as a peritonitis model host.
- **Natural disease:** "Septic peritonitis is a common, life-threatening condition encountered in dogs and cats" ([PMID: 30040445](https://pubmed.ncbi.nlm.nih.gov/30040445/)). In GI-perforation cases, "the overall mortality was 63.6%" across 44 dogs and 11 cats ([PMID: 24283417](https://pubmed.ncbi.nlm.nih.gov/24283417/)). Etiologies mirror humans: GI perforation (foreign bodies, NSAID-induced pyloric ulcer, dehiscence), with uncommon causes such as **grass-awn foreign-body migration** (good-to-excellent prognosis after surgery; [PMID: 36874536](https://pubmed.ncbi.nlm.nih.gov/36874536/)).
- **Comparative biology:** the pathophysiology (GI disruption → polymicrobial contamination → sepsis), diagnostics (blood-to-fluid glucose/lactate gradients, intracellular bacteria on cytology), and treatment (source control + antibiotics, open-abdomen/VAC) are strongly conserved between humans and companion animals — a key rationale for cross-species translational study.
- **Zoonotic potential:** the enteric pathogens involved can be zoonotic, but septic peritonitis itself is **not a transmissible disease**.

---

## 15. Model Organisms

**Gold-standard model — Cecal Ligation and Puncture (CLP).** "Cecal ligation and puncture (CLP)... is often considered the 'gold standard' to induce polymicrobial sepsis in laboratory animals. CLP is a well-described model involving a simple surgical procedure that closely mimics the clinical course of intra-abdominal sepsis" ([PMID: 34048005](https://pubmed.ncbi.nlm.nih.gov/34048005/)). Severity is **tunable**: e.g., 40% cecal ligation with double puncture yields ~80% mortality within 5 days, and 80% ligation ~100% mortality ([PMID: 20890188](https://pubmed.ncbi.nlm.nih.gov/20890188/)).

**Other models.**
- **Cecal slurry (CS) intraperitoneal injection** — the gold standard for *neonatal* mice ([PMID: 34048005](https://pubmed.ncbi.nlm.nih.gov/34048005/)).
- **Zebrafish bacterial peritonitis** — used to study neutrophil trained immunity ([PMID: 41980372](https://pubmed.ncbi.nlm.nih.gov/41980372/)).
- **Genetic knockout/transgenic mice** on the CLP background dissect mechanism (e.g., *Nlrc4−/−*, [PMID: 41071588](https://pubmed.ncbi.nlm.nih.gov/41071588/); CD300ld, [PMID: 40376837](https://pubmed.ncbi.nlm.nih.gov/40376837/)).

**Phenotype recapitulation & applications.** CLP reproduces the polymicrobial source, the biphasic hyper- then immuno-suppressive host response ([PMID: 31259890](https://pubmed.ncbi.nlm.nih.gov/31259890/)), cytokine kinetics, bacterial dissemination, and organ injury, enabling study of immunopathology and candidate therapeutics.

**Limitations.** Model outcomes are highly sensitive to technical variables — notably **housing temperature**: thermoneutral (30°C) housing improved CLP survival from 40% to 78% versus standard 22°C, altering IL-6 and phagocytosis ([PMID: 32433210](https://pubmed.ncbi.nlm.nih.gov/32433210/)). Mouse models incompletely capture human comorbidity, age, and the effect of source control/antibiotics — a recognized reason for translational failure of sepsis immunotherapies.

---

## Mechanistic Model / Interpretation

```
   GI-tract lesion (perforation / ischemia / dehiscence / trauma)
                 │  spillage of luminal gut flora
                 ▼
   Contamination of sterile peritoneum (polymicrobial: E. coli, anaerobes, Candida)
                 │  PAMPs (LPS) → TLR4/CD14 → NF-κB (resident macrophages, mesothelium)
                 ▼
   Cytokine storm: TNF-α, IL-1β, IL-6, HMGB1  +  neutrophil recruitment
             ┌────────────┴─────────────┐
   BRANCH A (local)               BRANCH B (systemic)
   coagulation > fibrinolysis     dysregulated host response = SEPSIS
   → fibrin, adhesions,           → vasodilation, capillary leak,
     abscess (walled-off             microthrombosis, hypoperfusion
     protected niche)             → septic shock
             │                          │
             └──────────► MULTIPLE ORGAN DYSFUNCTION (AKI, ARDS,
                          septic cardiomyopathy, DIC, hepatic) ◄──────┐
                                        │                              │
                          hyperinflammatory → IMMUNOSUPPRESSIVE phase  │
                                        │  secondary/tertiary infection┘
                                        ▼
                          DEATH  ◄── interrupted by ──►  SOURCE CONTROL + ANTIBIOTICS → recovery
```

The unifying theme is that **septic peritonitis is a source-control disease**: every downstream mechanistic step is fueled by ongoing contamination from the GI lesion, so physically eliminating the source (with antibiotic and physiologic support) is both the most upstream and the most effective intervention — explaining why source-control success dominates every prognostic model.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [39200076](https://pubmed.ncbi.nlm.nih.gov/39200076/) | Supports | IAI mortality 23–38%; 2nd most common sepsis death |
| [37170123](https://pubmed.ncbi.nlm.nih.gov/37170123/) | Supports | SCIAS mortality >80%; GI-disruption→MODS causal chain |
| [30685836](https://pubmed.ncbi.nlm.nih.gov/30685836/) | Supports | Sepsis-3 definition; abdomen 2nd source; source-control gold standard |
| [31954465](https://pubmed.ncbi.nlm.nih.gov/31954465/) | Supports | Global sepsis burden (48.9M cases, 11M deaths, GBD 2017) |
| [41227298](https://pubmed.ncbi.nlm.nih.gov/41227298/) | Supports | Secondary peritonitis subtypes; biomarker panel |
| [8891619](https://pubmed.ncbi.nlm.nih.gov/8891619/) | Supports | Source control determines survival (19% vs 100% mortality) |
| [21988045](https://pubmed.ncbi.nlm.nih.gov/21988045/) | Supports | APACHE II & MPI discriminate survivors; MPI independent |
| [8645072](https://pubmed.ncbi.nlm.nih.gov/8645072/) | Supports | 604-patient multivariate validation of scoring systems |
| [27670577](https://pubmed.ncbi.nlm.nih.gov/27670577/) | Supports | STOP-IT: 4-day antibiotics suffice after source control |
| [22752330](https://pubmed.ncbi.nlm.nih.gov/22752330/) | Supports | CT free air+fluid → surgery for generalized peritonitis |
| [15093233](https://pubmed.ncbi.nlm.nih.gov/15093233/) | Supports | Free intraperitoneal air = direct perforation sign |
| [42583660](https://pubmed.ncbi.nlm.nih.gov/42583660/) | Supports | Classic peritoneal signs of acute abdomen |
| [12692761](https://pubmed.ncbi.nlm.nih.gov/12692761/) | Supports | Blood-to-fluid glucose/lactate gradients 100% Se/Sp (dogs) |
| [12734857](https://pubmed.ncbi.nlm.nih.gov/12734857/) | Supports | Coagulation shift → abscess/adhesion mechanism |
| [34048005](https://pubmed.ncbi.nlm.nih.gov/34048005/) | Supports | CLP as gold-standard polymicrobial sepsis model |
| [31259890](https://pubmed.ncbi.nlm.nih.gov/31259890/) | Supports | Biphasic immune course; immunosuppressive phase |
| [24283417](https://pubmed.ncbi.nlm.nih.gov/24283417/) | Supports | Companion-animal mortality 63.6%; NSAID risk factor |
| [30040445](https://pubmed.ncbi.nlm.nih.gov/30040445/) | Supports | Veterinary microbiology; effective antibiotics |
| [32433210](https://pubmed.ncbi.nlm.nih.gov/32433210/) | Qualifies | Housing temperature drastically alters CLP outcomes (model limitation) |
| [28846501](https://pubmed.ncbi.nlm.nih.gov/28846501/) | Qualifies | Rapid source-control laparotomy not universally beneficial |

---

## Limitations and Knowledge Gaps

1. **Template mismatch.** Roughly half the standard disease template (causal genes, pathogenic variants, inheritance, penetrance, chromosomal/epigenetic diagnostics, genetic counseling, vaccination) is **not applicable** to an acquired infectious/surgical condition. These are documented as N/A rather than forced.
2. **Human vs veterinary diagnostic evidence.** The most striking quantitative diagnostic data (blood-to-fluid glucose/lactate 100% Se/Sp) come from **canine/feline** cohorts; the exact human cutoffs differ and human peritoneal-fluid gradient thresholds are less standardized.
3. **Heterogeneity.** "Septic peritonitis" spans primary (SBP), secondary (the main entity here), and tertiary forms, and multiple GI source lesions with different microbiology and prognosis — pooling can obscure subtype-specific detail.
4. **Immunotherapy translation.** Numerous adjunctive immunomodulators succeed in CLP but none is approved for human peritonitis; model artifacts (e.g., housing temperature) contribute to this translational gap.
5. **Host-genetic modifiers** of the sepsis response are biologically plausible but not yet clinically actionable for peritonitis.

## Proposed Follow-up Experiments / Actions

1. **Standardize human peritoneal-fluid biochemical gradients** (glucose, lactate, pH) prospectively to replicate the high-performing veterinary diagnostics in people.
2. **Subtype-stratified prognostic modeling** integrating MPI/APACHE II with the biomarker panel (PCT, IL-6, HMGB1, NLR, NGAL) to individualize source-control urgency and antibiotic duration.
3. **Validate short-course/biomarker-guided antibiotic stopping** (building on STOP-IT) across the fungal-peritonitis and immunosuppressed subgroups.
4. **Cross-species translational studies** leveraging naturally occurring canine/feline septic peritonitis as a bridge between CLP and human trials for candidate immunotherapies (e.g., neutrophil-directed CD300ld, trained immunity).
5. **Standardize CLP reporting** (housing temperature, ligation length, resuscitation/antibiotic co-treatment) to improve reproducibility and translational fidelity.
6. **Investigate host-genetic and mNGS-guided personalization** — combine rapid pathogen metagenomics with host inflammatory profiling to tailor antimicrobial and immunomodulatory therapy.

---

*Report compiled from 13 confirmed findings and 58 reviewed papers across a 5-iteration autonomous investigation. Evidence sources: human clinical cohorts and guidelines, veterinary clinical cohorts (naturally occurring disease), and experimental animal models (CLP, cecal slurry, zebrafish).*


## Artifacts

- [OpenScientist final report](Septic_Peritonitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Septic_Peritonitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 39 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 27 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025380` (1 mention) - the report calls it "Abdominal guarding"; HP calls it **Increased circulating androstenedione concentration**
- `CL:0000771` (2 mentions) - the report calls it "B-1a cell"; CL calls it **eosinophil**
- `NCIT:C51674` (1 mention) - the report calls it "Drainage Procedure"; NCIT calls it **Endomyocardial Biopsy**
- `NCIT:C157715` (1 mention) - the report calls it "Debridement"; NCIT calls it **Total Gut Decontamination**
- `NCIT:C1878` (1 mention) - the report calls it "Imipenem"; NCIT calls it **Darbepoetin Alfa**
- `NCIT:C1737` (1 mention) - the report calls it "Cefotaxime"; NCIT calls it **Organic Solvents**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002027` (2 mentions) - the report calls it "Abdominal pain", "Clinical sign"; HP calls it **Abdominal pain**
- `HP:0011227` (1 mention) - the report calls it "Elevated CRP"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated CRP" among its other names
- `GO:0007249` (1 mention) - the report calls it "NF-κB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "p50-dependent NF-kappaB signaling" among its other names
- `GO:0070269` (1 mention) - the report calls it "pyroptosis"; GO calls it **pyroptotic inflammatory response**, and lists "pyroptosis" among its other names
- `GO:0042060` (1 mention) - the report calls it "wound healing/adhesion"; GO calls it **wound healing**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002027` - called "Abdominal pain", "Clinical sign"