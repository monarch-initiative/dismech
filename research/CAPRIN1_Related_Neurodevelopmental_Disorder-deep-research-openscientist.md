---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T20:59:10.811071'
end_time: '2026-08-28T21:11:25.690362'
duration_seconds: 734.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CAPRIN1 Related Neurodevelopmental Disorder
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
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 19
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35979925
  relevance_assessed: 13
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:36279435
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 1
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001251
    reported_labels:
    - Variable (later reports)
    ontology_label: Ataxia
  - term_id: HP:0000365
    reported_labels:
    - Variable (later reports)
    ontology_label: Hearing impairment
  - term_id: HP:0001999
    reported_labels:
    - Variable (later reports)
    ontology_label: Abnormal facial shape
  - term_id: UBERON:0000955
    reported_labels:
    - primary organ is the brain/CNS
    ontology_label: brain
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CAPRIN1_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CAPRIN1_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CAPRIN1 Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CAPRIN1 Related Neurodevelopmental Disorder** covering all of the
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

# CAPRIN1-Related Neurodevelopmental Disorder: Comprehensive Disease Characterization

## Summary

**CAPRIN1-related neurodevelopmental disorder (CAPRIN1-NDD)** is a rare, autosomal dominant Mendelian condition caused by heterozygous **loss-of-function (LoF) variants in the *CAPRIN1* gene** (Cell cycle-Associated PRotein 1; MIM \*601178; chromosome 11p13), producing disease through **haploinsufficiency**. The gene encodes **Caprin-1** (also called RNG105, "RNA Granule protein 105 kDa"), a ubiquitously expressed, evolutionarily conserved cytoplasmic RNA-binding phosphoprotein that is a core structural and regulatory component of neuronal **RNA transport granules** and cytoplasmic **stress granules**. In neurons, Caprin-1 controls the somatodendritic transport and local translation of a specific subset of synaptic mRNAs — a process essential for synaptic plasticity, homeostatic AMPA-receptor scaling, and long-term memory. Reducing Caprin-1 to roughly half its normal dose disrupts these processes, yielding a neurodevelopmental phenotype.

The disorder was formally defined in 2022–2023 (Pavinato et al., *Brain*) from a founding cohort of 12 unrelated individuals and independently corroborated by a "stress-granule regulator gene" cohort (Jia et al., 2022). The **core clinical phenotype** is dominated by language impairment/speech delay (≈100%), intellectual disability (≈83%), attention-deficit/hyperactivity disorder (≈82%), and autism spectrum disorder (≈67%), with a variable multisystem tail including respiratory problems, limb/skeletal anomalies, developmental delay, feeding difficulties, seizures (≈33%), ophthalmologic problems, and — in later reports — cerebellar ataxia, dysmorphic features, and hearing loss. Both **de novo** and **inherited** variants occur, implying incomplete penetrance and/or variable expressivity.

Mechanistically, the disorder is anchored by strong convergent evidence: patient-derived cells show monoallelic (wild-type) expression and half-dose protein; *CAPRIN1⁺/⁻* human iPSC-derived cortical neurons show reduced neuronal processes, disorganization, and degeneration; and mouse models (constitutive knockout, dosage-matched heterozygotes, and inner-ear conditional knockouts) recapitulate memory deficits, ASD-like behavior, and progressive hearing loss respectively. There is **no disease-modifying therapy**; management is entirely supportive and multidisciplinary. Because the mechanism is haploinsufficiency, dosage-restoration strategies are rational future therapeutics, and patient iPSC platforms have been generated explicitly toward this goal. This report synthesizes 12 confirmed findings across all 15 template sections, grounded in 13 primary papers.

---

## Key Findings

### Finding 1 — CAPRIN1-NDD is an autosomal dominant disorder caused by CAPRIN1 haploinsufficiency

Pavinato et al. (*Brain*, 2023) described "*an autosomal dominant disorder associated with loss-of-function variants in the Cell cycle associated protein 1 (CAPRIN1; MIM\*601178)*" [PMID: 35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/). The founding study identified 12 unrelated cases carrying heterozygous LoF variants at 11p13. The mechanism is **haploinsufficiency**: in patient-derived lymphoblasts and fibroblasts, the authors "*showed a monoallelic expression of the wild-type allele, and a reduction of the transcript and protein compatible with a half dose*." Both de novo and inherited (parent-to-child) LoF variants were reported, establishing dominant inheritance with a dosage-sensitive mechanism rather than a dominant-negative or gain-of-function effect. This finding is the molecular foundation of the entire disease entity.

### Finding 2 — Core phenotype spectrum and frequencies

In the founding cohort of 12 cases, the neurobehavioral core comprised "*language impairment/speech delay (100%), intellectual disability (83%), attention deficit hyperactivity disorder (82%) and autism spectrum disorder (67%)*" [PMID: 35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/). A multisystem tail was also documented: "*Affected individuals also had respiratory problems (50%), limb/skeletal anomalies (50%), developmental delay (42%) feeding difficulties (33%), seizures (33%) and ophthalmologic problems (33%).*" A later case report expanded the recognized spectrum, noting "*respiratory problems, limb and skeletal anomalies, developmental delay, feeding difficulties, seizures, ophthalmologic problems, cerebellar ataxia, dysmorphic features, and hearing loss*" [PMID: 41859620](https://pubmed.ncbi.nlm.nih.gov/41859620/), adding **ataxia, dysmorphism, and hearing loss** to the phenotype.

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Language impairment / speech delay | ~100% | HP:0000750 (Delayed speech and language development) |
| Intellectual disability | ~83% | HP:0001249 |
| ADHD | ~82% | HP:0007018 |
| Autism spectrum disorder | ~67% | HP:0000717 |
| Respiratory problems | ~50% | HP:0002087 |
| Limb/skeletal anomalies | ~50% | HP:0011844 |
| Developmental delay | ~42% | HP:0001263 |
| Feeding difficulties | ~33% | HP:0011968 |
| Seizures | ~33% | HP:0001250 |
| Ophthalmologic problems | ~33% | HP:0000478 |
| Cerebellar ataxia | Variable (later reports) | HP:0001251 |
| Hearing loss | Variable (later reports) | HP:0000365 |
| Dysmorphic features | Variable (later reports) | HP:0001999 |

### Finding 3 — Caprin-1 regulates dendritic mRNA localization and local translation essential for synaptic plasticity and long-term memory

Caprin-1/RNG105 is a core RNA-binding component of neuronal RNA granules and cytoplasmic stress granules; it binds a subset of mRNAs via its RGG motifs and partners with G3BP1. Knockout mouse work established its physiological role: "*RNG105-deficient mice displayed unprecedentedly severe defects in long-term memory formation in spatial and contextual learning tasks*" [PMID: 29157358](https://pubmed.ncbi.nlm.nih.gov/29157358/). The synaptic mechanism was defined: "*RNG105 deficiency reduced the dendritic localization of mRNAs encoding regulators of AMPAR surface expression, which was consistent with attenuated homeostatic AMPAR scaling in dendrites and reduced synaptic strength.*" A distinct cargo class was identified in earlier work: "*RNG105 knock-out in mice reduces the dendritic localization of mRNAs for Na+/K+ ATPase (NKA) subunit isoforms*" [PMID: 20861386](https://pubmed.ncbi.nlm.nih.gov/20861386/), with consequent neuronal network degeneration. Crucially, the human cellular phenotype mirrors the mouse: in *CAPRIN1⁺/⁻* iPSC-derived cortical neurons, "*CAPRIN1 loss caused reduced neuronal processes, overall disruption of the neuronal organization and an increased neuronal degeneration*" [PMID: 35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/). This finding provides the causal chain from gene dosage to synaptic and network dysfunction.

### Finding 4 — Mouse models recapitulate ASD-like behavior, memory deficits, and sensory phenotypes

Dosage-matched heterozygous mice model the human haploinsufficiency: "*Rng105(+/-) mice exhibited a reduced sociality in a home cage and a weak preference for social novelty*" [PMID: 26865403](https://pubmed.ncbi.nlm.nih.gov/26865403/), together with reduced behavioral flexibility — an ASD-relevant profile at the matched gene dosage. Homozygous knockouts show severe long-term memory impairment and network degeneration (Finding 3). An inner-ear conditional knockout links Caprin-1 to the patient hearing-loss phenotype: "*targeted inner ear-deletion of Caprin1 in mice leads to an early onset, progressive hearing loss*" [PMID: 35165318](https://pubmed.ncbi.nlm.nih.gov/35165318/), with abnormal inner-hair-cell–spiral-ganglion-neuron synapses and failed recovery from noise exposure. Together these models recapitulate the behavioral, cognitive, and sensory dimensions of the human disorder.

### Finding 5 — Molecular identifiers and pathogenic variant spectrum

**Gene:** *CAPRIN1* (HGNC:6743; NCBI Gene 4076; OMIM \*601178; Ensembl ENSG00000135387), chromosome **11p13**. **Protein:** Caprin-1 (UniProt Q14444), 709 amino acids, organized into two homology regions (HR1 — a coiled-coil containing the G3BP-binding motif; HR2), an RGG-rich RNA-binding region, and a C-terminal low-complexity/prion-like domain. Reported pathogenic/likely-pathogenic variants are predominantly **heterozygous loss-of-function**: nonsense (e.g., "*c. 1045 C > T, p. (Q349\*)... a nonsense mutation, de novo and heterozygous, likely resulting in loss of function of the CAPRIN1 protein*" [PMID: 41859620](https://pubmed.ncbi.nlm.nih.gov/41859620/)), frameshift, and splice-site variants. A second specific pathogenic allele, "*c.1744C>T CAPRIN1 variant*," was used to derive a patient iPSC line [PMID: 40112765](https://pubmed.ncbi.nlm.nih.gov/40112765/). Summarizing evidence indicates "*The majority of reported pathogenic mutations in the CAPRIN1 gene result in decreased protein levels and haploinsufficiency*" [PMID: 35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/). *CAPRIN1* is strongly constrained against LoF in gnomAD (high pLI / very low LOEUF), consistent with haploinsufficiency; pathogenic alleles are absent or ultra-rare in population databases.

| Attribute | Value |
|---|---|
| Gene symbol | *CAPRIN1* |
| HGNC | HGNC:6743 |
| NCBI Gene | 4076 |
| OMIM (gene) | \*601178 |
| Ensembl | ENSG00000135387 |
| Locus | 11p13 |
| UniProt (protein) | Q14444 (709 aa) |
| Dominant variant class | LoF (nonsense, frameshift, splice) |
| Mechanism | Haploinsufficiency |

### Finding 6 — Independent replication: CAPRIN1 among stress-granule regulator genes causing NDD

Jia et al. (2022) independently reported "*a new neurodevelopmental disorder (NDD) with common features of language problems, intellectual disability, and behavioral issues caused by de novo likely gene-disruptive variants in*" genes regulating stress-granule assembly (including *CAPRIN1* and its partners) [PMID: 35977029](https://pubmed.ncbi.nlm.nih.gov/35977029/). This convergent cohort places CAPRIN1-NDD within a broader class of **"stress-granulopathy"/RNA-granule NDDs** that share impaired mRNA regulation, strengthening causal attribution and situating the disorder mechanistically among related conditions.

### Finding 7 — Inheritance, penetrance, epidemiology, and onset

Inheritance is **autosomal dominant**. Both de novo (e.g., p.Q349\*, "*de novo and heterozygous*" [PMID: 41859620](https://pubmed.ncbi.nlm.nih.gov/41859620/)) and inherited variants occur; in the founding cohort several variants were transmitted from a parent, implying **incomplete penetrance and/or variable expressivity**, with some carrier parents mildly or subclinically affected. Onset is early — developmental/speech delay is apparent in infancy to early childhood (congenital-to-pediatric onset) — and the course is **chronic and lifelong**, best characterized as a static-to-slowly-evolving developmental encephalopathy rather than a rapidly progressive neurodegeneration in patients. The disorder is **ultra-rare**: only a few dozen cases have been reported worldwide since 2022 ("*We identified 12 cases with loss-of-function CAPRIN1 variants*" [PMID: 35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/)), with no formal prevalence estimate (Orphanet-level "unknown/<1:1,000,000"). No established sex bias, ethnic predilection, founder effect, or consanguinity requirement (dominant, not recessive). No phenotype-specific OMIM/MONDO/ICD code is yet firmly assigned; ICD-11 would map under the 6A00 (disorders of intellectual development) range.

### Finding 8 — Diagnosis, management, and anatomical/subcellular involvement

Diagnosis is **molecular**: exome/genome sequencing (or NDD/epilepsy/autism gene panels) detecting a heterozygous LoF variant; chromosomal microarray may detect 11p13 deletions encompassing *CAPRIN1*. There is no specific biochemical biomarker; supportive tests reflect complications (EEG for seizures ~33%, audiometry/ABR for hearing loss, ophthalmologic exam, brain MRI). Anatomically the **primary organ is the brain/CNS** (UBERON:0000955), especially cerebral cortex and hippocampus (dendritic compartments) and cerebellum (ataxia); secondary systems include auditory (cochlea, IHC–SGN synapse), respiratory, musculoskeletal, and visual. Subcellularly, pathology centers on **cytoplasmic RNA/stress granules and neuronal dendrites** (GO:0010494 cytoplasmic stress granule; GO:0036477 somatodendritic compartment; GO:0030425 dendrite). Relevant cell types: cortical/hippocampal glutamatergic neurons (CL:0000679) and spiral ganglion neurons. Management is entirely supportive/symptomatic — early intervention, speech/language therapy, special education, ADHD pharmacotherapy, anti-seizure medication when indicated ("*seizures (33%)*" [PMID: 35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/)), hearing aids, and physical/occupational therapy. No disease-modifying or gene-targeted therapy exists, though patient iPSC lines have been generated toward future therapeutic development: "*To understand the pathogenesis of this disorder and in view of future treatment, we generated human induced pluripotent stem cells (iPSCs) from a patient*" [PMID: 40112765](https://pubmed.ncbi.nlm.nih.gov/40112765/).

### Finding 9 — Protein-level mechanism: Caprin-1 domains bidirectionally regulate stress-granule phase separation and select mRNA cargo

Caprin-1 binds the NTF2-like domain of G3BP1 via a conserved motif: "*Caprin-1 exhibits a highly conserved motif, F(M/I/L)Q(D/E)Sx(I/L)D that binds to the NTF-2-like domain of G3BP-1*" [PMID: 17210633](https://pubmed.ncbi.nlm.nih.gov/17210633/). Its C-terminal RGG-rich region selectively binds target mRNAs: "*The carboxy-terminal region of Caprin-1 selectively bound mRNA for c-Myc or cyclin D2, this binding being diminished by mutation of the three RGG motifs and abolished by deletion of the RGG-rich region.*" Structurally, phase-separation behavior is bidirectional: "*The C-terminal domain of Caprin-1 underwent spontaneous LLPS, whereas the N-terminal domain and GIM of Caprin-1 suppressed LLPS of G3BP1*" [PMID: 36279435](https://pubmed.ncbi.nlm.nih.gov/36279435/) — a "yin-yang" control of reversible stress-granule assembly. Caprin-1 also enhances mRNA recruitment into condensates: "*Caprin1 triggers the formation of large G3BP1-mRNA condensates in vitro and improves both the mRNA and G3BP1 recruitment in SGs*" [PMID: 41131140](https://pubmed.ncbi.nlm.nih.gov/41131140/). Overexpression induces eIF2α phosphorylation and selective (not global) translational repression, tying Caprin-1 dosage directly to the regulation of specific mRNAs.

### Finding 10 — Caprin-1 stress-granule dynamics link to broader neurodegeneration (BPAN/WDR45, ALS)

WDR45 (mutated in β-propeller protein-associated neurodegeneration, BPAN) regulates stress-granule disassembly through Caprin-1: "*WDR45 forms gel-like condensates via its WD5 domain, which competitively displaces G3BP1 from Caprin-1 to promote SG disassembly*" [PMID: 40473629](https://pubmed.ncbi.nlm.nih.gov/40473629/). BPAN mutations impair Caprin-1 interaction, delaying SG disassembly and correlating with earlier disease onset; moreover "*WDR45 depletion also exacerbates amyotrophic lateral sclerosis-associated pathological SGs, highlighting its broader relevance to neurodegenerative diseases.*" This positions Caprin-1 as a hub within the stress-granule dysregulation axis of neurodegeneration, complementing (but distinct from) its neurodevelopmental role via haploinsufficiency.

### Finding 11 — Evolutionary conservation and model-organism resources

Caprin-1 is "*a ubiquitously expressed, well-conserved cytoplasmic phosphoprotein*" [PMID: 17210633](https://pubmed.ncbi.nlm.nih.gov/17210633/), with orthologs across vertebrates and invertebrates (human *CAPRIN1* Gene 4076; mouse *Caprin1/Rng105* Gene 53872, NCBI Taxon:10090; conserved orthologs in rat, zebrafish *Danio rerio* Taxon:7955, and *Drosophila*). Available disease models include constitutive *Rng105/Caprin1* knockout mice (severe LTM/network phenotypes), dosage-matched heterozygous mice (ASD-like behavioral model), inner-ear conditional knockouts (hearing-loss model), and human patient-derived iPSC lines plus CRISPR-engineered *CAPRIN1⁺/⁻* iPSC-derived cortical neurons/NPCs ("*we generated human induced pluripotent stem cells (iPSCs) from a patient carrying the c.1744C>T CAPRIN1 variant*" [PMID: 40112765](https://pubmed.ncbi.nlm.nih.gov/40112765/)). No naturally occurring animal disease (OMIA entry) is established for *CAPRIN1*.

### Finding 12 — Prognosis, natural history, and therapeutic outlook

CAPRIN1-NDD is a **chronic, lifelong, predominantly static developmental encephalopathy** with no established reduction in life expectancy and no reported disease-specific mortality. Morbidity is driven by intellectual disability, ASD, ADHD, and communication impairment, with variable seizures (~33%), hearing loss, and cerebellar ataxia adding burden. Onset in infancy/early childhood defines a **critical early-intervention window**. No disease-modifying therapy exists; care is supportive/multidisciplinary. Because pathogenesis is haploinsufficiency, dosage-restoration strategies (e.g., ASOs targeting the wild-type allele, upregulation approaches, gene supplementation) are rational future therapies, and patient iPSC lines were generated explicitly "*in view of future treatment*" [PMID: 40112765](https://pubmed.ncbi.nlm.nih.gov/40112765/).

---

## Section-by-Section Report

### 1. Disease Information
CAPRIN1-NDD is a rare autosomal dominant neurodevelopmental disorder caused by heterozygous LoF variants in *CAPRIN1*. **Key identifiers:** causal gene OMIM \*601178; locus 11p13; HGNC:6743; NCBI Gene 4076; Ensembl ENSG00000135387; protein UniProt Q14444. A dedicated OMIM phenotype/MONDO/ICD entry is not yet firmly established (the entity was defined in 2022–2023). **Synonyms:** CAPRIN1 haploinsufficiency disorder; RNG105-related NDD; CAPRIN1-related neurodevelopmental disorder with language impairment, ADHD and ASD. Information is derived from **aggregated disease-level resources and small published case series** (12-case founding cohort plus subsequent case reports), not EHR-scale data.

### 2. Etiology
The **primary cause is genetic** — heterozygous LoF variants in *CAPRIN1* producing haploinsufficiency (Findings 1, 5). The principal genetic risk factor is the pathogenic LoF allele itself (de novo or inherited). No environmental risk factors, protective factors, or gene–environment interactions are established; the condition is monogenic and Mendelian, not multifactorial. Modifier genes are not defined, though partners in the stress-granule network (G3BP1/2, UBAP2L) are plausible candidates given the shared "stress-granulopathy" class (Finding 6).

### 3. Phenotypes
See Finding 2 table. Phenotype types span **behavioral** (ASD, ADHD), **cognitive** (intellectual disability, language impairment), **neurological** (seizures, cerebellar ataxia), **sensory** (hearing loss, ophthalmologic problems), and **physical/multisystem** (limb/skeletal anomalies, respiratory problems, feeding difficulties, dysmorphism). Onset is neonatal-to-childhood; severity is variable; course is generally static/lifelong. Quality-of-life impact is substantial via communication, learning, and behavioral domains, though no formal EQ-5D/SF-36 data exist for this ultra-rare disorder.

### 4. Genetic/Molecular Information
Causal gene *CAPRIN1* (Finding 5). Variant classes: nonsense, frameshift, splice-site (predominant), rare structural/deletion (11p13). Functional consequence: loss of function → haploinsufficiency (not dominant-negative/gain-of-function). Population frequency: pathogenic alleles absent/ultra-rare; the gene is strongly LoF-constrained (high pLI). Origin: germline (de novo or inherited). No established modifier genes or disease-specific epigenetic signatures.

### 5. Environmental Information
Not applicable — CAPRIN1-NDD is a monogenic disorder with no known environmental, lifestyle, or infectious contributors.

### 6. Mechanism / Pathophysiology
The causal chain (Findings 1, 3, 9): heterozygous LoF variant → ~50% reduction in Caprin-1 protein → impaired assembly/function of neuronal RNA transport granules and altered stress-granule dynamics (Caprin-1–G3BP1 LLPS control; RGG-mediated mRNA selection) → reduced somatodendritic localization and local translation of synaptic mRNAs (AMPAR regulators, Na⁺/K⁺-ATPase subunits) → attenuated homeostatic AMPAR scaling and reduced synaptic strength → impaired synaptic/structural plasticity, reduced neuronal processes, disrupted network organization, and increased neuronal degeneration → intellectual disability, language impairment, ASD, ADHD, seizures. **GO biological processes:** mRNA transport (GO:0051028), regulation of translation (GO:0006417), stress granule assembly (GO:0034063), synaptic plasticity (GO:0048167). **GO cellular components:** cytoplasmic stress granule (GO:0010494), dendrite (GO:0030425), somatodendritic compartment (GO:0036477). **CL cell types:** glutamatergic neuron (CL:0000679).

```
LoF variant → ↓50% Caprin-1 → impaired RNA granule / SG dynamics
     → ↓ dendritic mRNA localization + local translation (AMPAR, NKA)
        → ↓ synaptic strength / plasticity → network disorganization + degeneration
           → ID · language impairment · ASD · ADHD · seizures
```

### 7. Anatomical Structures Affected
Primary: brain/CNS (UBERON:0000955) — cerebral cortex, hippocampus, cerebellum. Secondary: cochlea/inner ear, respiratory system, musculoskeletal system, eye. Subcellular: cytoplasmic stress granules, dendrites (Finding 8). Lateralization: bilateral/generalized.

### 8. Temporal Development
Onset in infancy/early childhood (congenital-to-pediatric); insidious developmental presentation; chronic lifelong course; predominantly static developmental encephalopathy. Critical intervention window is early childhood (Findings 7, 12).

### 9. Inheritance and Population
Autosomal dominant; incomplete penetrance/variable expressivity; de novo and inherited variants; ultra-rare (few dozen cases worldwide; no formal prevalence); no established sex bias, founder effect, or consanguinity role (Finding 7).

### 10. Diagnostics
Molecular diagnosis via WES/WGS or NDD gene panels detecting heterozygous LoF *CAPRIN1* variants; CMA for 11p13 deletions. No specific biomarker. Supportive tests: EEG, audiometry/ABR, ophthalmologic exam, brain MRI. Differential diagnosis includes other RNA-granule/stress-granule NDDs (G3BP-family, UBAP2L) and broad syndromic ID/ASD (Finding 8).

### 11. Outcome/Prognosis
Lifelong static developmental encephalopathy; no established mortality reduction; morbidity from ID/ASD/ADHD/communication impairment plus variable seizures, hearing loss, ataxia. Prognostic heterogeneity likely reflects variable expressivity (Finding 12).

### 12. Treatment
Entirely supportive/symptomatic: early intervention, speech/language therapy, special education, ADHD pharmacotherapy (stimulants/atomoxetine; NCIT clinical-intervention terms apply), anti-seizure medication, hearing aids, physical/occupational therapy. No disease-modifying therapy; iPSC platforms generated toward future dosage-restoration approaches (Findings 8, 12).

### 13. Prevention
No primary prevention (monogenic). Genetic counseling for recurrence risk (de novo vs inherited), prenatal/preimplantation testing where a familial variant is known, and cascade testing of at-risk relatives constitute the applicable secondary measures.

### 14. Other Species / Natural Disease
No naturally occurring animal disease (no OMIA entry). Orthologs: mouse *Caprin1/Rng105* (Gene 53872, Taxon:10090), rat, zebrafish (Taxon:7955), *Drosophila* — highly conserved (Finding 11).

### 15. Model Organisms
Constitutive *Rng105/Caprin1* KO mice (memory/network phenotypes), dosage-matched heterozygous mice (ASD-like behavior), inner-ear conditional KO (hearing loss), and human patient-derived and CRISPR-engineered *CAPRIN1⁺/⁻* iPSC cortical neurons/NPCs. Models recapitulate cognitive, behavioral, and sensory dimensions but a fully faithful multisystem model of the human syndrome is lacking (Findings 4, 11).

---

## Mechanistic Model / Interpretation

CAPRIN1-NDD is best understood as an **RNA-granule / local-translation disorder of dosage sensitivity**. Caprin-1 sits at the intersection of two condensate systems — constitutive neuronal RNA transport granules that deliver specific mRNAs to dendrites, and inducible cytoplasmic stress granules that transiently sequester mRNAs during cellular stress. Its modular architecture (G3BP1-interacting motif, RGG mRNA-binding region, C-terminal LLPS-prone low-complexity domain) enables it to select mRNA cargo and to bidirectionally tune phase separation ("yin-yang" control). A 50% reduction in Caprin-1 is sufficient to degrade the fidelity of dendritic mRNA delivery and local translation, undermining homeostatic AMPAR scaling and synaptic strength — the biophysical substrate of learning and memory. Because these processes are most demanding during the intense synaptic remodeling of early brain development, a partial deficit manifests as a neurodevelopmental rather than a purely neurodegenerative phenotype, though degenerative features appear in cellular models and connect Caprin-1 to broader neurodegeneration (BPAN/WDR45, ALS).

The convergence of evidence is unusually strong for an ultra-rare disorder: patient genetics (monoallelic wild-type expression, half-dose protein), human iPSC cellular phenotypes, three complementary mouse models, an independent replication cohort, and detailed biophysical dissection of the protein all point to the same haploinsufficiency mechanism. This coherence makes CAPRIN1-NDD an attractive candidate for **dosage-restoration therapeutics**.

| Evidence layer | System | Key observation |
|---|---|---|
| Human genetics | Patient lymphoblasts/fibroblasts | Monoallelic WT expression; half-dose transcript/protein |
| Human cellular | *CAPRIN1⁺/⁻* iPSC cortical neurons | Reduced processes, disorganization, degeneration |
| Mouse (heterozygous) | *Rng105⁺/⁻* | ASD-like reduced sociality/novelty preference |
| Mouse (homozygous KO) | *Rng105⁻/⁻* | Severe LTM deficit; network degeneration; ↓ dendritic AMPAR/NKA mRNA |
| Mouse (conditional) | Inner-ear *Caprin1* KO | Progressive hearing loss; abnormal IHC–SGN synapse |
| In vitro biophysics | Recombinant Caprin-1/G3BP1 | Bidirectional LLPS control; RGG mRNA selection; ↑ mRNA recruitment |

---

## Evidence Base

| PMID | Title (abbrev.) | Role / support |
|---|---|---|
| [35979925](https://pubmed.ncbi.nlm.nih.gov/35979925/) | *CAPRIN1 haploinsufficiency causes NDD…* | Founding cohort; AD inheritance, haploinsufficiency, phenotype frequencies, iPSC cellular phenotype |
| [41859620](https://pubmed.ncbi.nlm.nih.gov/41859620/) | *CAPRIN1-Related NDD: novel mutation with ataxia* | Expands phenotype (ataxia, hearing loss); de novo p.Q349\* nonsense variant |
| [35977029](https://pubmed.ncbi.nlm.nih.gov/35977029/) | *De novo variants in stress-granule assembly genes…* | Independent replication; situates CAPRIN1 in stress-granulopathy class |
| [40112765](https://pubmed.ncbi.nlm.nih.gov/40112765/) | *iPSC line from CAPRIN1 haploinsufficiency patient* | c.1744C>T variant; iPSC model toward future treatment |
| [29157358](https://pubmed.ncbi.nlm.nih.gov/29157358/) | *RNG105/Caprin1 essential for long-term memory* | KO mouse: severe LTM defects, AMPAR mechanism |
| [20861386](https://pubmed.ncbi.nlm.nih.gov/20861386/) | *RNG105 deficiency impairs NKA mRNA localization* | Specific dendritic mRNA cargoes; network degeneration |
| [26865403](https://pubmed.ncbi.nlm.nih.gov/26865403/) | *Rng105 heterozygous mice behavior* | Dosage-matched ASD-like social deficits |
| [35165318](https://pubmed.ncbi.nlm.nih.gov/35165318/) | *Caprin1 inner-ear deletion → hearing loss* | Model for patient hearing-loss phenotype |
| [17210633](https://pubmed.ncbi.nlm.nih.gov/17210633/) | *Caprin-1 structural features / G3BP-1 / eIF2α* | RGG mRNA selection; G3BP1-interacting motif; conservation |
| [36279435](https://pubmed.ncbi.nlm.nih.gov/36279435/) | *Yin-yang regulation of stress granules by Caprin-1* | Bidirectional LLPS control of SG assembly |
| [41131140](https://pubmed.ncbi.nlm.nih.gov/41131140/) | *mRNA recruitment by G3BP1 condensates via Caprin1* | Caprin-1 enhances mRNA recruitment into SGs |
| [40473629](https://pubmed.ncbi.nlm.nih.gov/40473629/) | *WDR45 regulates SG disassembly via Caprin-1* | Links Caprin-1 to BPAN/ALS neurodegeneration |
| [31978946](https://pubmed.ncbi.nlm.nih.gov/31978946/) | *Cataloguing dendritic mRNAs regulated by RBPs* | Review of Caprin1/RNG105 dendritic mRNA regulation |

---

## Limitations and Knowledge Gaps

- **Small case numbers.** The disorder rests on ~12 founding cases plus scattered reports; phenotype frequencies have wide confidence intervals and may shift as cohorts grow.
- **No formal epidemiology.** Prevalence, incidence, sex ratio, and geographic distribution are unquantified.
- **Penetrance/expressivity poorly defined.** Inherited variants and mildly affected carrier parents imply incomplete penetrance, but genotype–phenotype correlations (variant type, position) are not yet established.
- **No dedicated OMIM phenotype/MONDO/ICD identifier** was confirmed during this investigation.
- **No natural-history study.** Long-term trajectory, life expectancy, and complication rates are inferred, not measured.
- **No disease-modifying therapy or clinical trials.** Management is supportive; dosage-restoration approaches remain preclinical concepts.
- **Model gaps.** No single animal model captures the full multisystem human syndrome; the connection between stress-granule biophysics and specific clinical features is mechanistically plausible but not fully proven in patients.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a patient registry / natural-history study** to refine phenotype frequencies, penetrance, expressivity, and long-term outcomes; formally request OMIM phenotype and MONDO/ICD-11 assignments.
2. **Genotype–phenotype analysis** across accumulating variants (nonsense vs frameshift vs splice vs whole-gene deletion) to test whether variant class or position modifies severity.
3. **Deep phenotyping of *CAPRIN1⁺/⁻* iPSC cortical organoids** with transcriptomics/translatomics (Ribo-seq) to define the dysregulated dendritic mRNA program in human neurons and identify candidate biomarkers.
4. **Dosage-restoration proof-of-concept:** test allele-specific or gene-supplementation strategies (e.g., ASO upregulation of the wild-type allele, AAV gene supplementation) in *CAPRIN1⁺/⁻* neurons and heterozygous mice, using AMPAR scaling and network organization as functional readouts.
5. **Cross-disorder comparison** with other stress-granule NDD genes (G3BP1/2, UBAP2L) to define shared and gene-specific pathways and potential convergent therapeutic targets.
6. **Sensory-phenotype workup** (systematic audiometry/ophthalmology) in patient cohorts to quantify hearing loss and eye involvement suggested by the inner-ear model and case reports.


## Artifacts

- [OpenScientist final report](CAPRIN1_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CAPRIN1_Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 5 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35979925` *(abstract only)*: "*The majority of reported pathogenic mutations in the CAPRIN1 gene result in decreased protein levels and haploinsufficiency*"
  - closest text in source: "We describe an autosomal dominant disorder associated with loss-of-function variants in the Cell cycle associated protein 1 (CAPRIN1; MIM*601178)"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:36279435` (4 mentions) - Yin and yang regulation of stress granules by Caprin-1.
  - shared terms: caprin-1

Weighed against this report's own most characteristic terms: `caprin1`, `variant`, `gene`, `heterozygous`, `loss`, `disorder`, `phenotype`, `hearing`, `caprin-1`, `haploinsufficiency`, `patient`, `ipsc`, `stress-granule`, `novo`, `established`, `human`, `model`, `cohort`, `network`, `rng105`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 5 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001251` (1 mention) - the report calls it "Variable (later reports)"; HP calls it **Ataxia**
- `HP:0000365` (1 mention) - the report calls it "Variable (later reports)"; HP calls it **Hearing impairment**
- `HP:0001999` (1 mention) - the report calls it "Variable (later reports)"; HP calls it **Abnormal facial shape**
- `UBERON:0000955` (2 mentions) - the report calls it "primary organ is the brain/CNS"; UBERON calls it **brain**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.