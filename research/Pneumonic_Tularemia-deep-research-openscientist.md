---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T15:55:59.312038'
end_time: '2026-09-29T16:11:19.498852'
duration_seconds: 920.19
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Pneumonic Tularemia
  mondo_id: MONDO:0002212
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
citation_count: 44
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 8
  relevance_assessed: 44
  on_topic: 31
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 45
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 18
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0002212
    reported_labels:
    - if available
    - tularemia; pneumonic subtype
    ontology_label: pneumonic tularemia
  - term_id: GO:0070269
    reported_labels:
    - pyroptosis
    - Cellular processes:** phagocytosis, phagosomal escape, intracellular replication,
      **pyroptosis
    ontology_label: pyroptotic inflammatory response
  - term_id: NCIT:C839
    reported_labels:
    - "Aminoglycosides \u2014 streptomycin"
    ontology_label: Spiramycin
  - term_id: NCIT:C405
    reported_labels:
    - "Fluoroquinolones \u2014 ciprofloxacin"
    ontology_label: Cyclophosphamide
  - term_id: NCIT:C692
    reported_labels:
    - "Tetracyclines \u2014 doxycycline"
    ontology_label: Nimodipine
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  - NCBI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pneumonic Tularemia
- **MONDO ID:** MONDO:0002212 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pneumonic Tularemia** covering all of the
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

# Pneumonic Tularemia — Comprehensive Disease Characteristics Report

**Disease:** Pneumonic Tularemia
**MONDO ID:** MONDO:0002212
**Category:** Infectious Disease
**Causative agent:** *Francisella tularensis* (Gram-negative facultative intracellular coccobacillus)

---

## Summary

Pneumonic tularemia is the pulmonary and most lethal clinical form of tularemia, an acute zoonosis caused by the Gram-negative facultative intracellular bacterium *Francisella tularensis*. It arises either as **primary pneumonic disease** following inhalation of aerosolized organisms (e.g., landscaping activities, laboratory accidents, or a deliberate bioterrorism release) or as **secondary pneumonic disease** through hematogenous spread from other clinical forms. Among the classical clinical forms (ulceroglandular, glandular, oculoglandular, oropharyngeal, typhoidal, and pneumonic), the pneumonic presentation carries the greatest mortality, and it is the form of greatest bioterrorism concern because *F. tularensis* is one of the most infectious bacteria known — as few as ~10 organisms inhaled can initiate infection. The organism is a **CDC Category A (Tier 1) select agent**.

Mechanistically, disease follows a well-characterized intracellular pathway: the bacterium invades alveolar macrophages and dendritic cells, escapes the phagosome within hours via a **Type VI secretion system encoded on the Francisella Pathogenicity Island (FPI)**, and replicates in the cytosol. Virulent type A strains actively subvert early innate immunity through an **atypical, under-acylated lipid A** that evades TLR4 recognition. Once in the cytosol, bacterial DNA — liberated by interferon-inducible guanylate-binding proteins (GBPs) and IRGB10 — is sensed by the **AIM2 inflammasome**, driving caspase-1 activation, IL-1β/IL-18 secretion, and pyroptosis. Protective adaptive immunity is Th1-polarized and depends on **IFN-γ, TNF-α, iNOS, and CD4⁺ T cells (T-bet)**.

Clinically, untreated pneumonic tularemia carries roughly **30% mortality**, but prompt antibiotic therapy reduces case-fatality to below ~2%. Aminoglycosides (streptomycin, gentamicin) are the historical treatment of choice; fluoroquinolones (ciprofloxacin) and doxycycline are effective alternatives, and the **2025 CDC guidelines list fluoroquinolones and doxycycline as first-line options**. Diagnosis relies chiefly on serology (microagglutination) and PCR because culture is insensitive and biohazardous. **No licensed human vaccine exists.** Tularemia is re-emerging across Europe and North America (2024–2025), reinforcing the need for clinical awareness, rapid diagnostics, and preventive measures.

---

## Section 1 — Disease Information

**Overview.** Pneumonic (respiratory) tularemia is the lung-centered manifestation of infection by *Francisella tularensis*. It presents with fever, cough, dyspnea, pleuritic chest pain, and radiographic infiltrates, often with hilar lymphadenopathy and pleural effusion. Primary pneumonic disease results from inhalation of infectious aerosols; secondary pneumonic disease develops when bacteria seed the lungs from bloodstream dissemination of ulceroglandular, typhoidal, or other forms.

**Key identifiers:**
- **MONDO:** MONDO:0002212 (tularemia; pneumonic subtype)
- **MeSH:** Tularemia (D014406); "Tularemia, Pulmonary" as a subheading concept
- **ICD-10:** A21.2 (pulmonary tularemia); A21.9 (tularemia, unspecified)
- **ICD-11:** 1B94 (Tularaemia)
- **SNOMED CT:** Pulmonary tularemia (disorder)
- **Orphanet:** Tularemia is catalogued as a rare bacterial infectious disease (ORPHA:855 for the parent entity)
- **NCBI Taxonomy (pathogen):** *Francisella tularensis* — txid263

**Synonyms / alternative names:** Pulmonary tularemia; respiratory tularemia; pneumonic form of tularemia; "rabbit fever" (lung form); "deer-fly fever" (lung form); Ohara disease / Francis disease (historical, whole-disease synonyms).

**Data source type:** Information is derived from **aggregated disease-level resources** — clinical case series, outbreak investigations, systematic reviews, and experimental animal/in vitro studies — rather than from individual EHR-derived patient records. A 2024 systematic review aggregated 870 cases spanning 1993–2023.

---

## Section 2 — Etiology

**Primary cause (infectious).** Pneumonic tularemia is caused entirely by infection with *Francisella tularensis*; it is **not a genetic disease**. Human infection is initiated by inhalation of aerosolized bacteria. *F. tularensis* is among the most infectious bacteria known — inoculation or inhalation of **as few as 10 organisms** initiates infection (Finding F002; [PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/); [PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/)).

> "requires as few as 10 organisms to cause disease, making this potential bioterrorism agent one of the most infectious bacterial pathogens known" — [PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)

**Environmental / occupational risk factors:**
- **Aerosol-generating landscaping activities** — lawn mowing and brush cutting were significant risk factors in the Martha's Vineyard primary pneumonic outbreak (odds ratio 9.2, 95% CI 1.6–68.0) (Finding F008; [PMID: 11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/)).
- **Occupational exposure** — laboratory workers, landscapers, farmers, hunters, and those handling infected animals (rabbits, hares, rodents).
- **Arthropod vectors** — ticks (*Dermacentor*, *Amblyomma*), deer flies, mosquitoes (predominant in Scandinavia) — though these more commonly cause ulceroglandular disease.
- **Animal contact** — lagomorphs, rodents, and domestic cats/dogs. Dog-related exposures accounted for 3.3% of U.S. cases, of which 13% were pneumonic ([PMID: 30556330](https://pubmed.ncbi.nlm.nih.gov/30556330/)).
- **Deliberate aerosol release** — the pneumonic form is the most likely presentation after intentional release ([PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/)).
- **Sex/age** — systemic disease occurs more commonly in older patients ([PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)).

**Genetic risk / protective factors:** No human germline susceptibility or protective variants are established for tularemia; this is an environmentally/infectiously acquired disease. Host-genetic determinants of severity are described almost exclusively in **mouse models** (e.g., inflammasome genes *Aim2*, *Nlrp3*), not in humans. **Gene-environment interactions** in the classical human-disease sense are therefore not applicable; the relevant "gene–environment" axis is the interaction between **host innate-immune genes and the inhaled bacterial dose/strain virulence** (see Section 6).

---

## Section 3 — Phenotypes

Pneumonic tularemia is an acute, adult-predominant (though all ages affected) febrile respiratory illness with an incubation period typically of **3–5 days (range 1–14 days)**.

| Phenotype | Type | HPO suggestion | Frequency / notes |
|---|---|---|---|
| Fever | Symptom/sign | HP:0001945 (Fever) | Near-universal; abrupt onset |
| Cough (often nonproductive) | Symptom | HP:0012735 (Cough) | Common |
| Dyspnea | Symptom | HP:0002094 (Dyspnea) | Common in severe disease |
| Pleuritic chest pain | Symptom | HP:0033771 (Pleuritic chest pain) | Frequent |
| Pneumonia / pulmonary infiltrate | Clinical sign / imaging | HP:0002090 (Pneumonia) | Defining feature |
| Pleural effusion | Clinical sign | HP:0002202 (Pleural effusion) | Common; may require drainage |
| Hilar lymphadenopathy | Clinical sign | HP:0100721 (Hilar lymphadenopathy) | Characteristic radiographic finding |
| Chills / rigors | Symptom | HP:0025143 (Chills) | Common |
| Malaise / fatigue | Symptom | HP:0003394 / HP:0012378 | Common |
| Headache | Symptom | HP:0002315 (Headache) | Frequent |
| Myalgia | Symptom | HP:0003326 (Myalgia) | Frequent |
| Cavitary pneumonia / empyema | Complication | HP:0006528 / HP:0002101 | Reported; e.g., pulmonary empyema cases ([PMID: 24655540](https://pubmed.ncbi.nlm.nih.gov/24655540/)) |
| Elevated inflammatory markers (ESR, CRP) | Lab abnormality | HP:0003565 (Elevated ESR) | Common |

**Characteristics:**
- **Age of onset:** Any age; primarily adult in occupational/aerosol settings.
- **Severity:** Moderate to severe; pneumonic form is the most severe clinical presentation (Finding F001).
- **Progression:** Acute and potentially rapidly progressive; can advance to respiratory failure, sepsis, and multi-organ involvement if untreated.
- **Frequency among affected individuals:** In U.S. case series, pneumonic disease constituted ~12% of all tularemia cases ([PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)); in dedicated aerosol outbreaks it predominates (11 of 15 cases primary pneumonic on Martha's Vineyard; [PMID: 11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/)).

**Quality-of-life impact:** As an acute, treatable infection, long-term QoL burden is limited in survivors treated promptly; however, delayed treatment can result in prolonged convalescence, pleural complications requiring intervention, and, rarely, death. No disease-specific EQ-5D/SF-36 datasets exist for pneumonic tularemia.

---

## Section 4 — Genetic / Molecular Information

**Not applicable in the human-host genetic sense.** Pneumonic tularemia is an infectious disease with **no causal human genes, pathogenic germline variants, modifier genes, human epigenetic signatures, or chromosomal abnormalities**. There is no OMIM Mendelian entry, no ClinVar variant set, and no inheritance pattern.

The relevant molecular determinants are **bacterial**:
- **Francisella Pathogenicity Island (FPI):** a ~16–19 gene cluster including the *iglABCD* operon encoding a **Type VI secretion system (T6SS)** required for phagosomal escape and intramacrophage growth; FPI mutants are highly attenuated (Finding F003; [PMID: 17395722](https://pubmed.ncbi.nlm.nih.gov/17395722/), [PMID: 17233889](https://pubmed.ncbi.nlm.nih.gov/17233889/)).
- **Regulators:** *mglA/mglB* control FPI expression.
- **Effector *opiA*** (a bacterial PI3-kinase) modifies phagosomal PI(3)P to promote escape ([PMID: 30057173](https://pubmed.ncbi.nlm.nih.gov/30057173/)).
- **LPS/lipid A biosynthesis genes** (*lpxD1/lpxD2*, *galU*) shape immune evasion ([PMID: 28478203](https://pubmed.ncbi.nlm.nih.gov/28478203/), [PMID: 21819572](https://pubmed.ncbi.nlm.nih.gov/21819572/)).

**Host modifier genes (model-organism level):** In mice, *Aim2*, *Nlrp3*, *Tbx21* (T-bet), *Ifng*, *Tnf*, and *Nos2* modify susceptibility/severity (Sections 5–6).

---

## Section 5 — Environmental Information

**Infectious agent (taxon):** *Francisella tularensis*, NCBI Taxon 263. Two clinically important subspecies:
- **subsp. *tularensis* (Type A)** — North America; highly virulent. Subdivided into **type A-west** and the more severe **type A-east** (Finding F009; [PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)).
- **subsp. *holarctica* (Type B)** — Holarctic (Europe, Asia, North America); less virulent, rarely fatal.

> "type A-west infections are less severe than either type B or type A-east infections" — [PMID: 16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/)

**Environmental persistence:** *F. tularensis* Type A survives in brackish water and salt-influenced soil similarly to Type B, which may explain why Martha's Vineyard sustains pneumonic transmission ([PMID: 21136042](https://pubmed.ncbi.nlm.nih.gov/21136042/)). Diverse *Francisella* species are detectable in environmental water/sediment/soil at active foci ([PMID: 19669828](https://pubmed.ncbi.nlm.nih.gov/19669828/)).

**Environmental / lifestyle factors:** Aerosol-generating outdoor work (mowing, brush cutting), hunting/skinning lagomorphs, farming, and laboratory handling. Waterborne outbreaks (contaminated drinking water) are common in Turkey and drive oropharyngeal rather than pneumonic disease ([PMID: 42343287](https://pubmed.ncbi.nlm.nih.gov/42343287/)). No specific dietary or smoking association is established for the pneumonic form.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (inhalation → clinical pneumonia)

1. **Inhalation of aerosolized *F. tularensis*** (≥ ~10 organisms) deposits bacteria in the alveolar space → **leads to** uptake by alveolar macrophages and dendritic cells (and alveolar epithelial cells).
2. **Bacterial invasion of macrophages/DCs** → **results in** formation of the *Francisella*-containing phagosome (FCP).
3. **FPI/Type VI secretion system activity** (IglABCD; effector OpiA remodels phagosomal PI(3)P) → **causes** disruption of the phagosomal membrane and **phagosomal escape within a few hours** (demonstrated in vitro and in macrophages) ([PMID: 32694562](https://pubmed.ncbi.nlm.nih.gov/32694562/), [PMID: 30057173](https://pubmed.ncbi.nlm.nih.gov/30057173/)).
4. **Cytosolic replication** → **leads to** high intracellular bacterial burdens.
5. *In parallel,* **atypical tetra-acylated lipid A** on the bacterial surface **precludes** efficient TLR4 recognition and cationic antimicrobial peptide binding → **results in** blunted/delayed early innate signaling (chemokines, neutrophil recruitment) — an active immune-evasion branch (demonstrated: prior type A aerosol exposure antagonizes pulmonary LPS response; *galU* mutant reverses this) ([PMID: 28807561](https://pubmed.ncbi.nlm.nih.gov/28807561/), [PMID: 26510639](https://pubmed.ncbi.nlm.nih.gov/26510639/), [PMID: 21819572](https://pubmed.ncbi.nlm.nih.gov/21819572/)).
6. **Cytosolic bacterial DNA is liberated** by interferon-inducible GBP2/GBP5 and IRGB10, which attack the bacterial membrane causing bacteriolysis → **leads to** DNA release ([PMID: 25774716](https://pubmed.ncbi.nlm.nih.gov/25774716/), [PMID: 27693356](https://pubmed.ncbi.nlm.nih.gov/27693356/)).
7. **AIM2 inflammasome senses cytosolic DNA** → **activates** caspase-1 → **drives** processing/secretion of **IL-1β and IL-18** and **pyroptosis** (demonstrated for *F. novicida*/LVS) ([PMID: 21883803](https://pubmed.ncbi.nlm.nih.gov/21883803/)).
   - *Branch:* An **ASC-dependent, caspase-1-independent (caspase-8) pathway** also generates IL-18, boosting NK-cell IFN-γ ([PMID: 23975862](https://pubmed.ncbi.nlm.nih.gov/23975862/)).
8. **IL-18 + IL-12 → NK/T-cell IFN-γ**; with TNF-α these **activate iNOS (NOS2)** in macrophages → **results in** nitric-oxide-mediated bacterial killing (demonstrated in LVS aerosol model) ([PMID: 19237526](https://pubmed.ncbi.nlm.nih.gov/19237526/)).
9. **Th1 adaptive response (T-bet–dependent CD4⁺ T cells, plus antibody including IgA)** → **mediates** control and clearance; loss of T-bet or CD4⁺ T cells → **results in** overwhelming infection ([PMID: 24421047](https://pubmed.ncbi.nlm.nih.gov/24421047/), [PMID: 19211773](https://pubmed.ncbi.nlm.nih.gov/19211773/)).
10. **Net effect on tissue:** If bacterial replication outpaces innate/adaptive control → widespread pyroptotic cell death, inflammatory infiltration, necrotizing pneumonia, pleural effusion, bacteremic dissemination → **clinical pneumonic tularemia**, potentially sepsis and death.

### Detail by category

- **Molecular pathways:** cytosolic DNA sensing → AIM2/ASC/caspase-1; TLR4/MyD88 (subverted by lipid A); interferon (type I & II)-inducible GBP/IRGB10 antibacterial program; iNOS/NO production.
- **Cellular processes:** phagocytosis, phagosomal escape, intracellular replication, **pyroptosis** (GO:0070269), inflammasome assembly, inflammation (GO:0006954), autophagy/xenophagy (ATG5 modulates immunity, [PMID: 42514097](https://pubmed.ncbi.nlm.nih.gov/42514097/)).
- **Protein dysfunction (bacterial virulence):** T6SS effector delivery; PI3-kinase effector OpiA alters phosphoinositide signaling.
- **Immune involvement:** Th1/IFN-γ-dominant protective immunity; excessive early NLRP3 signaling can be host-detrimental ([PMID: 34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/)); antibody (IgG2a, IgA) contributes but requires host IFN-γ/T cells to protect ([PMID: 8039881](https://pubmed.ncbi.nlm.nih.gov/8039881/)).
- **Metabolic:** macrophage selenoproteins restrict intracellular replication ([PMID: 34777335](https://pubmed.ncbi.nlm.nih.gov/34777335/)); acidic-pH lipid A remodeling ([PMID: 28807561](https://pubmed.ncbi.nlm.nih.gov/28807561/)).
- **Tissue damage mechanisms:** necrotizing granulomatous inflammation, pyroptotic cell death, neutrophil-mediated injury, pleural inflammation.

**GO term suggestions:** GO:0070269 (pyroptosis), GO:0006954 (inflammatory response), GO:0032731 (positive regulation of IL-1β production), GO:0045087 (innate immune response), GO:0042742 (defense response to bacterium), GO:0071222 (cellular response to LPS).
**CL term suggestions:** CL:0000235 (macrophage), CL:0000583 (alveolar macrophage), CL:0000451 (dendritic cell), CL:0000623 (natural killer cell), CL:0000624 (CD4⁺ T cell), CL:0000775 (neutrophil).

---

## Section 7 — Anatomical Structures Affected

**Organ level:**
- **Primary:** Lung (UBERON:0002048), including alveoli (UBERON:0002299) and bronchi.
- **Secondary:** Pleura/pleural cavity (UBERON:0002402) — effusion/empyema; hilar/mediastinal lymph nodes (UBERON:0002509); with dissemination: spleen (UBERON:0002106), liver (UBERON:0002107), bone marrow, and rarely heart (myocarditis reported, [PMID: 30656604](https://pubmed.ncbi.nlm.nih.gov/30656604/)).
- **Body systems:** Respiratory system (primary); reticuloendothelial/lymphatic system; potentially cardiovascular (sepsis, rare myocarditis).

**Tissue and cell level:**
- Alveolar epithelium; pulmonary interstitium.
- **Target cells:** alveolar macrophages (CL:0000583), dendritic cells (CL:0000451), and other mononuclear phagocytes are the principal intracellular niche; neutrophils recruited to lung.

**Subcellular level (GO Cellular Component):**
- Phagosome (GO:0045335) → *Francisella*-containing vacuole; escape into **cytosol/cytoplasm (GO:0005829)** — the replicative compartment. AIM2 inflammasome assembles in the cytosol.

**Localization / lateralization:** Bilateral or unilateral patchy infiltrates; pleural effusions may be unilateral. Hilar adenopathy commonly bilateral.

---

## Section 8 — Temporal Development

- **Onset:** **Acute**, after an incubation of **3–5 days (range 1–14)**. Median incubation ~3 days in Missouri case review ([PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)).
- **Progression:** Rapid systemic febrile illness; can progress to respiratory failure and sepsis within days if untreated. Not staged like cancer; described as early (febrile, cough) → established pneumonia (infiltrates, effusion) → severe/complicated (empyema, respiratory failure, bacteremia).
- **Course pattern:** Acute, monophasic; **self-limited only rarely** — most severe cases require antibiotics. With treatment, recovery is the rule; convalescence over 1–4 weeks.
- **Duration:** Days to weeks (acute); not a chronic lifelong disease.
- **Remission:** Treatment-induced resolution is standard with appropriate antibiotics. Relapse can occur with bacteriostatic agents (tetracyclines) or short courses.
- **Critical periods:** **Early antibiotic initiation is the key intervention window**; delayed therapy increases complication and mortality risk ([PMID: 42601640](https://pubmed.ncbi.nlm.nih.gov/42601640/), [PMID: 22652404](https://pubmed.ncbi.nlm.nih.gov/22652404/)).

---

## Section 9 — Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable.

**Epidemiology:**
- Tularemia is a **rare, reportable** zoonosis. The pneumonic form is a minority of cases except in aerosol outbreaks.
- **Geographic distribution:** Northern hemisphere — North America (esp. south-central USA: Arkansas, Missouri, Oklahoma; and Martha's Vineyard for pneumonic), Scandinavia, Central/Eastern Europe, Turkey, Russia, Japan.
- **Re-emergence (2024–2025):** rising incidence — Austria 117, Slovenia 38, France 150, Spain/Castile-León 206, and **United States 220 cases in 2024** (Finding F012; [PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)). Germany reached a peak incidence in 2024 ([PMID: 42601640](https://pubmed.ncbi.nlm.nih.gov/42601640/)).
- **Primary pneumonic tularemia** is exceptionally rare — Martha's Vineyard is the site of the only two recognized U.S. primary pneumonic outbreaks (1978, 2000) (Finding F008; [PMID: 17442781](https://pubmed.ncbi.nlm.nih.gov/17442781/)).

> "Martha's Vineyard, Massachusetts, is the site of the only two recognized outbreaks of primary pneumonic tularemia in the United States" — [PMID: 17442781](https://pubmed.ncbi.nlm.nih.gov/17442781/)

**Demographics:**
- **Sex ratio:** Male predominance in many series (e.g., 65% male in Missouri, [PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)), reflecting occupational/recreational exposure; varies by outbreak.
- **Age:** All ages; systemic/severe disease more common in older adults.
- **Population-specific variants:** Type A (North America) vs. Type B (Eurasia) geographic segregation; type A-east most virulent.

---

## Section 10 — Diagnostics

**Serology (cornerstone):**
- **Microagglutination test (MAT):** titer **≥ 1/160** considered positive; seroconversion (≥4-fold rise) in paired sera is confirmatory (Finding F006; [PMID: 22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/)). Antibodies may take 2+ weeks to develop, limiting early diagnosis.
- Serology is preferred because **culture has low sensitivity and biosafety risk**, and PCR lacks standardization ([PMID: 20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/)).

> "Serology is still considered to be a cornerstone in tularemia diagnosis due to the low sensitivity of bacterial culture and the lack of standardization in PCR methodology" — [PMID: 20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/)

- **Rapid immunochromatographic test:** 98.3% sensitivity, 96.5% specificity vs. MAT ([PMID: 20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/)).

**Molecular (PCR):**
- Validated targets: **ISFtu2 insertion element, tul4 (17-kDa), fopA (43-kDa), 23-kDa gene** ([PMID: 14662930](https://pubmed.ncbi.nlm.nih.gov/14662930/)). Multitarget real-time TaqMan assays improve detection in complex specimens.
- PCR positive in ~91% of lymph node aspirates where cultures were negative (Finding F006).

**Culture:** Requires cysteine-enriched media; slow-growing; must be handled at **BSL-3** due to aerosol infection risk. Low clinical sensitivity.

**Imaging:** Chest X-ray/CT show patchy infiltrates, hilar/mediastinal lymphadenopathy, pleural effusion, and occasionally cavitation ([PMID: 24655540](https://pubmed.ncbi.nlm.nih.gov/24655540/)).

**Laboratory:** Nonspecific — elevated ESR/CRP; leukocytosis variable (more frequent in pediatric cases, [PMID: 42343287](https://pubmed.ncbi.nlm.nih.gov/42343287/)).

**Clinical criteria / differential diagnosis:** Consider in patients with pneumonia unresponsive to β-lactams plus relevant exposure (landscaping, animal/tick contact, endemic area). **Differential:** community-acquired bacterial pneumonia, Q fever, psittacosis, plague, anthrax, Legionella, tuberculosis, fungal pneumonia. Tularemia is frequently initially misdiagnosed ([PMID: 22911645](https://pubmed.ncbi.nlm.nih.gov/22911645/)).

**Screening:** No population screening; genetic/omics diagnostics not applicable.

---

## Section 11 — Outcome / Prognosis

- **Untreated mortality:** ~**30%** (Finding F012; [PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)); pneumonic form has the highest mortality of all clinical forms (Finding F001; [PMID: 38461051](https://pubmed.ncbi.nlm.nih.gov/38461051/)).

> "with the pneumonic presentation resulting in the greatest mortality" — [PMID: 38461051](https://pubmed.ncbi.nlm.nih.gov/38461051/)

- **Treated case-fatality (all forms, 870-case systematic review):** 0.7% (aminoglycosides), 0.9% (fluoroquinolones), 1.2% (tetracyclines) — overall low with prompt therapy (Finding F004; [PMID: 38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/)).
- **Complications:** pleural effusion/empyema (may require drainage), cavitary pneumonia, respiratory failure, bacteremia/sepsis, rare myocarditis, necrotizing abscess formation.
- **Recovery:** Excellent with early appropriate antibiotics; full recovery is typical. Prognosis worsens with delayed diagnosis, older age, type A-east strain, and high inhaled dose.
- **Prognostic factors:** speed of antibiotic initiation, subspecies/strain (type A-east worst), inoculum size, host age/comorbidity.

| Treatment class | Case-fatality (all forms) | Notes |
|---|---|---|
| Aminoglycosides (streptomycin, gentamicin) | 0.7% | Treatment of choice historically |
| Fluoroquinolones (ciprofloxacin) | 0.9% | No fatalities & lowest pleural intervention in pneumonic subset |
| Tetracyclines (doxycycline) | 1.2% | Bacteriostatic; higher relapse |

---

## Section 12 — Treatment

**Pharmacotherapy (NCIT term suggestions in parentheses):**
- **Aminoglycosides — streptomycin (NCIT:C839), gentamicin (NCIT:C575):** historical treatment of choice; bactericidal (Finding F004; [PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/)).

> "Streptomycin and gentamicin are currently considered the treatment of choice for tularemia. Quinolone is an effective alternative drug." — [PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/)

- **Fluoroquinolones — ciprofloxacin (NCIT:C405):** effective oral alternative; in the 870-case review, pneumonic patients on ciprofloxacin had **no fatalities** and the lowest rates of pleural intervention. Oral ciprofloxacin successfully treated cavitary pneumonic disease after drainage ([PMID: 24655540](https://pubmed.ncbi.nlm.nih.gov/24655540/)).
- **Tetracyclines — doxycycline (NCIT:C692):** bacteriostatic; requires ≥14–21 day courses; higher relapse.
- **2025 CDC guidelines** now establish **fluoroquinolones and doxycycline as first-line options** (Finding F012; [PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)).

> "The 2025 CDC guidelines establish fluoroquinolones and doxycycline as first-line therapeutic options" — [PMID: 42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/)

**Post-exposure prophylaxis:** streptomycin, gentamicin, doxycycline, or ciprofloxacin ([PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/)).

**Interventional/supportive:** Pleural drainage for empyema/large effusion; oxygen/ventilatory support in respiratory failure; hydration and antipyretics. **No patient isolation required** for pneumonic tularemia (no person-to-person transmission) ([PMID: 29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/)).

**Experimental/adjunctive:** Post-exposure immunization with *F. tularensis* membrane protein fraction (MPF) augmented gentamicin efficacy (100% survival in a mouse pneumonic model) — proof of concept for immunotherapy adjuncts ([PMID: 22652404](https://pubmed.ncbi.nlm.nih.gov/22652404/)).

**Pharmacogenomics / targeted / gene / cell / RNA therapies:** Not applicable.

---

## Section 13 — Prevention

- **Primary prevention:** Avoid aerosol-generating activities in endemic areas; use of masks/PPE during mowing/brush-cutting; safe handling of animal carcasses; tick/insect avoidance and repellents; laboratory biosafety (BSL-3 for cultures). Vector control and public health education.
- **Immunization:** **No licensed human vaccine** (Finding F007; [PMID: 38461051](https://pubmed.ncbi.nlm.nih.gov/38461051/)).

> "there are no approved vaccines against F. tularensis in the United States" — [PMID: 38461051](https://pubmed.ncbi.nlm.nih.gov/38461051/)

  - The **unlicensed Live Vaccine Strain (LVS)** protects mice against lethal intranasal/aerosol SCHU S4 challenge (CD4⁺ T-cell– and antibody/IgA-mediated) ([PMID: 19211773](https://pubmed.ncbi.nlm.nih.gov/19211773/)).
  - **Subunit/glycoconjugate candidates:** glucan-particle LPS + FTT0814 subunit vaccine (partial protection, T-cell immunity in a rat aerosol model, [PMID: 38713688](https://pubmed.ncbi.nlm.nih.gov/38713688/)); O-antigen glycoconjugate ([PMID: 30872471](https://pubmed.ncbi.nlm.nih.gov/30872471/)); MPL-adjuvanted catanionic nanoparticle vaccine ([PMID: 28077440](https://pubmed.ncbi.nlm.nih.gov/28077440/)). All remain experimental.
- **Secondary prevention:** Prompt recognition and post-exposure prophylaxis after known aerosol exposure or lab accident.
- **Public health:** Surveillance and reporting (nationally notifiable), water chlorination (for waterborne foci), rodent/lagomorph control.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of hosts (naturally infected):** Lagomorphs — rabbits/hares (*Sylvilagus*, *Lepus*); rodents (voles, mice, muskrats, beavers); domestic cats (*Felis catus*, NCBI:9685) and dogs (*Canis lupus familiaris*, NCBI:9615). Ticks and deer flies are vectors/reservoirs.
- **Natural disease & veterinary relevance:** Tularemia is an important zoonosis; cats can transmit to humans via bite/scratch ([PMID: 30556330](https://pubmed.ncbi.nlm.nih.gov/30556330/)); domestic dogs facilitate transmission via retrieved carcasses and ticks. Lagomorphs suffer high mortality (epizootics).
- **Comparative pathology:** Intracellular macrophage infection and phagosomal escape are conserved across mammalian hosts; mouse pathology closely mirrors human intracellular pathogenesis.
- **Zoonotic potential:** High — a prototypical zoonosis. **No human-to-human transmission**, so pneumonic cases need no isolation.
- **Cross-species susceptibility:** Broad mammalian host range; extreme susceptibility in mice and lagomorphs.

---

## Section 15 — Model Organisms

- **Mouse (*Mus musculus*, NCBI:10090) — principal model.** Intranasal/aerosol challenge with **SCHU S4 (type A)** or attenuated **LVS**; BALB/c and C57BL/6 strains widely used. Recapitulates pneumonic pathogenesis, intracellular replication, inflammasome activation, Th1 immunity, and treatment/vaccine responses (Findings F003, F005, F007, F010, F011).
  - Knockout models: *Aim2⁻/⁻*, *Nlrp3⁻/⁻*, *Asc⁻/⁻*, *Casp1⁻/⁻*, *Tbx21⁻/⁻* (T-bet), *Ifng⁻/⁻*, *Nos2⁻/⁻* — dissect inflammasome and Th1 pathways ([PMID: 24421047](https://pubmed.ncbi.nlm.nih.gov/24421047/), [PMID: 21883803](https://pubmed.ncbi.nlm.nih.gov/21883803/), [PMID: 33875472](https://pubmed.ncbi.nlm.nih.gov/33875472/), [PMID: 34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/)).
- **Rat (*Rattus norvegicus*, NCBI:10116):** Fischer 344 inhalation model used for vaccine efficacy testing ([PMID: 38713688](https://pubmed.ncbi.nlm.nih.gov/38713688/)).
- **In vitro / cellular:** Bone-marrow-derived and cell-line macrophages (J774) to study phagosomal escape, cytosolic replication, and inflammasome activation ([PMID: 32694562](https://pubmed.ncbi.nlm.nih.gov/32694562/), [PMID: 29482417](https://pubmed.ncbi.nlm.nih.gov/29482417/)).
- ***F. novicida* and *F. tularensis* LVS** serve as reduced-biosafety surrogates for the virulent SCHU S4 strain.
- **Model limitations:** *F. novicida* is attenuated in humans but hypervirulent in mice; LVS is attenuated relative to SCHU S4; mouse inflammasome biology and lipid A responses differ somewhat from humans, so protective correlates do not always translate ([PMID: 41410566](https://pubmed.ncbi.nlm.nih.gov/41410566/)).

---

## Mechanistic Model / Interpretation

```
 Inhaled F. tularensis (~10 organisms, type A)
              |
              v
   Alveolar macrophage / DC uptake ---> Francisella-containing phagosome
              |                                   |
              |  FPI / T6SS (IglABCD),            |  Atypical tetra-acylated
              |  effector OpiA (PI3K)             |  lipid A --> evades TLR4
              v                                   v  (blunted early innate signal)
     PHAGOSOMAL ESCAPE (hours) ----------> CYTOSOLIC REPLICATION
              |
              v
   GBP2/GBP5 + IRGB10 attack bacteria --> bacteriolysis --> DNA release
              |
              v
        AIM2 inflammasome --> caspase-1 --> IL-1b / IL-18 + PYROPTOSIS
              |                                   |
              |  (ASC/caspase-8 branch also        |
              |   makes IL-18, caspase-1-indep.)   v
              v                          NK/T cells --> IFN-gamma
   IFN-gamma + TNF-a --> iNOS/NO in macrophages --> bacterial killing
              |
              v
   T-bet+ CD4+ Th1 cells + antibody (IgG2a, IgA) --> CLEARANCE
              |
   (If replication outpaces control) --> necrotizing pneumonia,
        pleural effusion, bacteremia, sepsis --> CLINICAL PNEUMONIC TULAREMIA
```

**Upstream vs downstream:** Bacterial invasion, phagosomal escape, and lipid-A-mediated TLR4 evasion are the **upstream** drivers that permit unchecked cytosolic replication. The AIM2 inflammasome, GBP/IRGB10 bacteriolysis, IFN-γ/iNOS, and Th1/CD4⁺ responses are **downstream host-protective** mechanisms; when they are outpaced (high dose, virulent type A-east, delayed antibiotics), tissue injury and death follow. This model integrates 12 confirmed findings and is consistent across in vitro, mouse, rat, and human clinical/outbreak data.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding | Contribution |
|---|---|---|---|
| [38461051](https://pubmed.ncbi.nlm.nih.gov/38461051/) | Vaccine strategies vs *Francisella* | F001, F007 | Pneumonic = greatest mortality; no approved vaccine |
| [38294108](https://pubmed.ncbi.nlm.nih.gov/38294108/) | Systematic review 1993–2023 | F002, F004 | ~10-organism dose; comparative fatality by drug class |
| [29183485](https://pubmed.ncbi.nlm.nih.gov/29183485/) | Bichat guidelines | F001, F002, F004 | Pneumonic = bioterrorism form; aminoglycoside first-line |
| [32694562](https://pubmed.ncbi.nlm.nih.gov/32694562/) | Immune lymphocytes halt LVS | F003 | Phagosomal escape & cytosolic replication |
| [17395722](https://pubmed.ncbi.nlm.nih.gov/17395722/) | Francisella Pathogenicity Island | F003 | FPI encodes T6SS |
| [30057173](https://pubmed.ncbi.nlm.nih.gov/30057173/) | PI3K effector OpiA | F003 | Effector promotes phagosomal escape |
| [19237526](https://pubmed.ncbi.nlm.nih.gov/19237526/) | Immune-mouse T cells | F005 | IFN-γ/TNF-α/iNOS dependence |
| [19211773](https://pubmed.ncbi.nlm.nih.gov/19211773/) | Oral LVS protection | F005, F007 | CD4⁺ T cells/IgA mediate pulmonary protection |
| [24421047](https://pubmed.ncbi.nlm.nih.gov/24421047/) | T-bet & lung immunity | F005 | T-bet critical for pulmonary immunity |
| [20220165](https://pubmed.ncbi.nlm.nih.gov/20220165/) | Immunochromatographic test | F006 | Serology cornerstone; rapid test performance |
| [22090310](https://pubmed.ncbi.nlm.nih.gov/22090310/) | Central Anatolia cases | F006 | MAT ≥1/160 threshold |
| [14662930](https://pubmed.ncbi.nlm.nih.gov/14662930/) | Multitarget TaqMan PCR | F006 | Validated PCR gene targets |
| [11757506](https://pubmed.ncbi.nlm.nih.gov/11757506/) | Martha's Vineyard outbreak | F008 | Landscaping OR 9.2 risk factor |
| [17442781](https://pubmed.ncbi.nlm.nih.gov/17442781/) | Martha's Vineyard review | F008 | Only 2 US primary pneumonic outbreaks |
| [16836829](https://pubmed.ncbi.nlm.nih.gov/16836829/) | US molecular epidemiology | F009 | Type A-east most severe |
| [28807561](https://pubmed.ncbi.nlm.nih.gov/28807561/) | Lipid A remodeling | F010 | Atypical lipid A evades TLR4 |
| [26510639](https://pubmed.ncbi.nlm.nih.gov/26510639/) | Type A antagonizes TLR4 response | F010 | Active innate-immune suppression |
| [21819572](https://pubmed.ncbi.nlm.nih.gov/21819572/) | galU mutant | F010 | WT FT suppresses early innate immunity |
| [21883803](https://pubmed.ncbi.nlm.nih.gov/21883803/) | AIM2 & bacteriolysis | F011 | AIM2→caspase-1/IL-1β/IL-18/pyroptosis |
| [25774716](https://pubmed.ncbi.nlm.nih.gov/25774716/) | GBP2/GBP5 & AIM2 | F011 | GBPs liberate DNA for AIM2 |
| [27693356](https://pubmed.ncbi.nlm.nih.gov/27693356/) | IRGB10 | F011 | IRGB10 liberates bacterial ligands |
| [23975862](https://pubmed.ncbi.nlm.nih.gov/23975862/) | ASC/caspase-8 IL-18 | F011 | Caspase-1-independent IL-18/IFN-γ branch |
| [42641375](https://pubmed.ncbi.nlm.nih.gov/42641375/) | Re-emerging zoonosis | F012 | 30% untreated mortality; 2025 CDC first-line |

**Challenging/nuancing evidence:** *Aim2*/*Nlrp3* are dispensable for *vaccine-induced* adaptive immunity ([PMID: 33875472](https://pubmed.ncbi.nlm.nih.gov/33875472/)), and NLRP3 can increase host susceptibility ([PMID: 34690967](https://pubmed.ncbi.nlm.nih.gov/34690967/)) — indicating inflammasome roles are context-dependent (innate control vs. immunopathology).

---

## Limitations and Knowledge Gaps

1. **Mechanistic data are largely from mouse/in vitro models** using LVS or *F. novicida* surrogates, not virulent human type A SCHU S4 in humans. Translation to human pneumonic disease is inferred.
2. **Human pneumonic-specific datasets are sparse** — most clinical series pool all tularemia forms; dedicated primary pneumonic cohorts are limited to rare outbreaks (Martha's Vineyard).
3. **No human transcriptomic/proteomic/metabolomic profiling** of pneumonic tularemia patients was identified; omics diagnostics are not applicable/available.
4. **Correlates of protection remain undefined**, hampering vaccine licensure; no licensed human vaccine exists.
5. **Fatality figures for antibiotics** derive from all-form pooled reviews; pneumonic-only comparative RCTs are lacking (ethically/logistically constrained).
6. **Strain-virulence determinants** (why type A-east > type B > type A-west) are incompletely mapped at the molecular level.
7. **PMID 42641375** provides key re-emergence and 2025-guideline figures but is a single review source; primary CDC guideline documents should be cross-checked.

---

## Proposed Follow-up Experiments / Actions

1. **Human correlates-of-protection study** in vaccinated (LVS-exposed lab personnel) or convalescent cohorts — define antibody/T-cell signatures predicting protection to guide vaccine endpoints.
2. **Primary CDC 2025 guideline verification** — obtain and cite the definitive CDC/clinical-guideline document for first-line fluoroquinolone/doxycycline recommendations rather than relying on a review.
3. **Comparative-effectiveness analysis** of ciprofloxacin vs. gentamicin specifically in pneumonic cases, leveraging pooled outbreak registries, to formalize the observed lower pleural-intervention rate.
4. **Host single-cell transcriptomics of infected lung** (mouse aerosol SCHU S4) to resolve alveolar-macrophage vs. DC vs. neutrophil trajectories and map AIM2/IFN-γ programs spatially.
5. **Molecular dissection of type A-east virulence** via comparative genomics/transposon screens to identify determinants of the severity gradient (type A-east > type B > type A-west).
6. **Advance the glucan-particle/glycoconjugate subunit vaccines** toward dose-optimized aerosol-challenge efficacy and, ultimately, human immunogenicity trials.
7. **Adjunct immunotherapy translation** — evaluate membrane-protein-fraction post-exposure immunization plus antibiotics ([PMID: 22652404](https://pubmed.ncbi.nlm.nih.gov/22652404/)) in higher-order models toward a therapeutic-adjunct strategy.

---

*Report compiled from 12 confirmed findings and ~60 reviewed papers across 5 investigative iterations. Evidence source types span human clinical/outbreak studies, mouse and rat model-organism experiments, and in vitro cellular assays, as annotated throughout.*


## Artifacts

- [OpenScientist final report](Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pneumonic_Tularemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 44 |
| On topic | 31 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 30 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0002212` (3 mentions) - the report calls it "if available", "tularemia; pneumonic subtype"; MONDO calls it **pneumonic tularemia**
- `GO:0070269` (2 mentions) - the report calls it "pyroptosis", "Cellular processes:** phagocytosis, phagosomal escape, intracellular replication, **pyroptosis"; GO calls it **pyroptotic inflammatory response**
- `NCIT:C839` (1 mention) - the report calls it "Aminoglycosides — streptomycin"; NCIT calls it **Spiramycin**
- `NCIT:C405` (1 mention) - the report calls it "Fluoroquinolones — ciprofloxacin"; NCIT calls it **Cyclophosphamide**
- `NCIT:C692` (1 mention) - the report calls it "Tetracyclines — doxycycline"; NCIT calls it **Nimodipine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100721` (1 mention) - the report calls it "Hilar lymphadenopathy"; HP calls it **Mediastinal lymphadenopathy**
- `GO:0032731` (1 mention) - the report calls it "positive regulation of IL-1β production"; GO calls it **positive regulation of interleukin-1 beta production**, and lists "positive regulation of IL-1 beta production" among its other names
- `CL:0000583` (2 mentions) - the report calls it "alveolar macrophage", "Target cells:** alveolar macrophages"; CL calls it **alveolar macrophage**
- `CL:0000624` (1 mention) - the report calls it "CD4⁺ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `UBERON:0002048` (1 mention) - the report calls it "Primary:** Lung"; UBERON calls it **lung**
- `UBERON:0002402` (1 mention) - the report calls it "Secondary:** Pleura/pleural cavity"; UBERON calls it **pleural cavity**
- `GO:0045335` (1 mention) - the report calls it "Phagosome"; GO calls it **phagocytic vesicle**, and lists "phagosome" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0002212` - called "if available", "tularemia; pneumonic subtype"
- `GO:0070269` - called "pyroptosis", "Cellular processes:** phagocytosis, phagosomal escape, intracellular replication, **pyroptosis"
- `CL:0000583` - called "alveolar macrophage", "Target cells:** alveolar macrophages"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `NCBI`.
