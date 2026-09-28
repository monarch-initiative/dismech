---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-29T10:06:03.947067'
end_time: '2026-08-29T10:18:17.366698'
duration_seconds: 733.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Van Maldergem Syndrome
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
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 4
  relevance_assessed: 21
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 72
  verified: 69
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 8
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0018852
    reported_labels:
    - Van Maldergem syndrome
    - parent
    ontology_label: achromatopsia
  - term_id: UBERON:0001756
    reported_labels:
    - middle ear / ossicles / tympanic cavity
    ontology_label: middle ear
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Van_Maldergem_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Van_Maldergem_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Van Maldergem Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Van Maldergem Syndrome** covering all of the
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

# Van Maldergem Syndrome — Comprehensive Disease Characteristics Report

**Disease:** Van Maldergem Syndrome (VMS)
**Category:** Mendelian (rare autosomal recessive multisystem congenital disorder)
**Suggested MONDO:** MONDO:0018852 (Van Maldergem syndrome). Subtypes: VMLDS1 (MONDO:0010875-class, *DCHS1*), VMLDS2 (*FAT4*).

> **Evidence source note:** VMS is an ultra-rare disorder. Essentially all knowledge is derived from *individual patient case reports and small case series* (aggregated disease-level resources such as OMIM/Orphanet compile these), supplemented by *model-organism* (mouse, zebrafish, Drosophila) and *in vitro* mechanistic studies. There are no EHR-scale cohorts, registries, clinical trials, GWAS, or population omics datasets for this disease. Frequencies below are therefore qualitative/small-denominator estimates, not population statistics.

---

## 1. Disease Information

**Overview.** Van Maldergem syndrome is a rare autosomal recessive multiple-congenital-anomaly/intellectual-disability syndrome first described by Van Maldergem and colleagues in 1992. Its cardinal features are a distinctive craniofacial (blepharo-naso-facial) gestalt, intellectual disability, auditory (external/middle ear) malformations with conductive hearing loss, hand/digit anomalies and skeletal abnormalities, and — characteristically — periventricular and subcortical neuronal heterotopia on brain imaging (PMID 22473091, 27739185). It is caused by biallelic loss-of-function variants in one of two atypical cadherin genes, *DCHS1* (type 1) or *FAT4* (type 2), which act as a receptor–ligand pair in Fat–Dachsous planar cell polarity (PCP)/Hippo signaling (PMID 24056717).

**Key identifiers.**
- **OMIM:** #601390 — Van Maldergem syndrome 1 (VMLDS1; *DCHS1*); #615546 — Van Maldergem syndrome 2 (VMLDS2; *FAT4*). MIM#601390 explicitly cited in PMID 25930014 and PMID 40797481.
- **Orphanet:** ORPHA:314679 (Van Maldergem syndrome).
- **ICD-10:** Q87.8 (other specified congenital malformation syndromes, not elsewhere classified); **ICD-11:** LD2F.1Y / LD2F.0Y class (multiple developmental anomalies). No VMS-specific ICD code.
- **MeSH:** No dedicated MeSH heading; indexed under "Abnormalities, Multiple" / "Intellectual Disability" and gene terms *DCHS1*, *FAT4*.
- **MONDO:** MONDO:0018852 (parent), with type-1/type-2 children.

**Synonyms / alternative names.** Van Maldergem syndrome 1 and 2 (VMLDS1/VMLDS2); "blepharo-naso-facial malformation with intellectual disability" (descriptive); historically overlapping with, and now recognized as allelic to, **Hennekam lymphangiectasia–lymphedema syndrome** when caused by *FAT4* (PMID 24913602, 29681106).

---

## 2. Etiology

**Primary cause — genetic.** VMS is monogenic and recessive. It is caused by **biallelic (homozygous or compound heterozygous) pathogenic variants** in:
- ***DCHS1*** (Dachsous cadherin-related 1; HGNC:13681; NCBI Gene 8642; chromosome **11p15.4**; OMIM *603057) → VMLDS1.
- ***FAT4*** (FAT atypical cadherin 4; HGNC:23109; NCBI Gene 79633; chromosome **4q28.1**; OMIM *612411) → VMLDS2.

> "Here we show that mutations in genes encoding the receptor-ligand cadherin pair DCHS1 and FAT4 lead to a recessive syndrome in humans that includes periventricular neuronal heterotopia." (PMID 24056717)

**Risk factors.**
- *Genetic:* The two causal genes are the only established risk determinants. **Consanguinity** is a major risk amplifier — parental consanguinity was present in 3/5 families in the defining cohort, and homozygous variants predominate in consanguineous pedigrees (PMID 22473091). No susceptibility loci or GWAS signals exist (disease is monogenic). Potential modifier effects (e.g., *FAT4* vs *DCHS1* genotype, allelic *CCBE1/ADAMTS3* interactions in the lymphatic-overlap phenotype) are hypothesized but unproven.
- *Environmental / lifestyle / infectious:* **None identified.** VMS is fully genetically determined; no toxin, teratogen, dietary, occupational, or infectious contributor is known or expected. (Not applicable.)

**Protective factors.** None described. In principle, inheriting only one variant allele (heterozygous carrier) is "protective" in the Mendelian sense — carriers are unaffected — but no protective modifier alleles are known.

**Gene–environment interactions.** Not applicable/none reported; the phenotype is determined by biallelic genotype independent of environment.

---

## 3. Phenotypes

VMS is a **congenital, multisystem, generally non-progressive** disorder; most features are present at birth or emerge in infancy, with intellectual disability apparent in childhood. Severity is **variable** (mild-to-moderate ID is typical). Frequencies are qualitative given the tiny reported population (~dozens of patients worldwide).

**Craniofacial (physical manifestations — near-universal / "typical facial gestalt"):**
- Blepharophimosis (HP:0000581); telecanthus (HP:0000506); maxillary/midface hypoplasia (HP:0000327/HP:0011800); microtia (HP:0008551); atresia of external auditory canal (HP:0000413); blepharo-naso-facial malformation. (PMID 22473091, 27739185)

**Auditory (clinical sign — near-universal):**
- Conductive hearing impairment (HP:0000405), bilateral, from microtia + aural atresia ± middle-ear/ossicular and tympanic-cavity malformations. "Almost all nine described patients have been shown to be affected by conductive hearing impairment attributed to microtia, and atresia of the outer ear canal." (PMID 27739185)

**Neurological / neurodevelopmental (near-universal):**
- Intellectual disability, mild-to-moderate (HP:0001249); neonatal hypotonia (HP:0001319); periventricular nodular heterotopia (HP:0032388) and subcortical/subependymal neuronal heterotopia (HP:0002518); altered functional cerebral asymmetry (PMID 25930014); poor coordination/clumsiness (HP:0002317). (PMID 22473091, 24056717)

**Skeletal / limb (common):**
- Digital contractures/camptodactyly (HP:0100490/HP:0012385); brachydactyly / short 4th metacarpal (HP:0001156); scoliosis (HP:0002650); osteopenia (HP:0000938); general skeletal anomalies. (PMID 22473091, 28878612, 40797481, 29681106)

**Neonatal / feeding / respiratory (common):**
- Feeding difficulties (HP:0011968); respiratory problems and **tracheal anomalies** (HP:0002778); failure to thrive (HP:0001508). (PMID 22473091, 29681106)

**Endocrine (rare/variable):**
- Hypogonadotropic hypogonadism (HP:0000044); breast aplasia/hypoplasia/amazia with normal nipples (HP:0100783/HP:0003187) (PMID 29046692); central precocious puberty (HP:0000826) (PMID 40797481).

**Genitourinary (rare/variable):**
- Unilateral renal agenesis (HP:0000122/HP:0000104); ureterovesical junction obstruction/urinary tract obstruction (HP:0000073); duplex/duplicated collecting system (HP:0000081). (PMID 28878612, 30853441)

**Gastrointestinal / lymphatic (rare):**
- Intestinal lymphangiectasia (HP:0002593) — reported in VMS and blurring the boundary with Hennekam syndrome (PMID 31063239).

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist. Inferred burden: lifelong intellectual disability and hearing loss impair communication, learning, and independence; feeding/respiratory issues and multiple surgeries burden infancy; craniofacial differences carry psychosocial impact. Hearing rehabilitation measurably improves social skills and language (PMID 26491591).

---

## 4. Genetic / Molecular Information

**Causal genes.**
| Gene | Locus | OMIM | Protein | Disease |
|---|---|---|---|---|
| *DCHS1* (HGNC:13681, Gene 8642) | 11p15.4 | *603057 | Dachsous 1 (protocadherin, PCP ligand) | VMLDS1 (#601390) |
| *FAT4* (HGNC:23109, Gene 79633) | 4q28.1 | *612411 | FAT4 (protocadherin, PCP receptor) | VMLDS2 (#615546) |

DCHS1 and FAT4 form a **receptor–ligand pair**; FAT4 is a very large single-pass transmembrane protein with 34 extracellular cadherin repeats, EGF-like domains, and laminin-G–like domains; DCHS1 is its Dachsous-family cadherin ligand (PMID 28488382).

**Pathogenic variants.**
- *Type/class:* predominantly **loss-of-function** — nonsense, frameshift, and canonical splice-site variants (e.g., *FAT4* NM_024582.6:c.7018+1G>A, loss of the intron-6 donor site, ACMG **pathogenic**; PMID 37551355), as well as missense variants. Compound heterozygous and homozygous configurations both occur (PMID 29046692, 28878612).
- *Classification:* Reported variants are curated as **pathogenic / likely pathogenic** by ACMG/AMP criteria; novel variants continue to be reported, some initially VUS pending segregation/functional data (PMID 31384091, 40797481).
- *Allele frequency:* Individually **rare/private**; consistent with a recessive ultra-rare disease, biallelic pathogenic genotypes are essentially absent from gnomAD, though single heterozygous LoF alleles exist at very low frequency.
- *Origin:* **Germline**, biallelic. (Somatically, *FAT4* is a tumor-suppressor mutated in cancers, but that is unrelated to the germline VMS phenotype; PMID 28488382 notes FAT4's tumor-suppressor role.)
- *Functional consequence:* **Loss of function** of the Dchs1–Fat4 PCP/Hippo module. A 2026 study shows the **DCHS1 intracellular domain** is functionally critical — its loss expands neurogenic proliferation and generates VMS-like defects (PMID 41972678).

**Modifier genes.** None validated. Phenotype-modifying candidates include the specific gene affected (*FAT4* vs *DCHS1*) and, for the lymphatic-overlap phenotype, the allelic lymphangiogenesis genes *CCBE1* and *ADAMTS3* (which also cause Hennekam syndrome) (PMID 29681106).

**Epigenetics.** No DNA-methylation, histone-modification, or episignature data specific to VMS are available (not applicable at present).

**Chromosomal abnormalities.** VMS is a single-gene disorder; no recurrent aneuploidy, translocation, or copy-number syndrome. Chromosomal microarray is typically normal (useful mainly to exclude CNV mimics).

---

## 5. Environmental Information

- **Environmental factors:** None. No toxin, radiation, pollutant, or occupational exposure is implicated.
- **Lifestyle factors:** None (congenital genetic disease).
- **Infectious agents:** None. VMS is not infectious or triggered by pathogens.

*(All "Not applicable" — VMS is entirely genetically determined.)*

---

## 6. Mechanism / Pathophysiology

**Core molecular pathway — Fat–Dachsous PCP and Hippo/YAP signaling.** DCHS1 (Dachsous) and FAT4 are the vertebrate orthologs of the *Drosophila* Dachsous–Fat PCP system. They bind heterophilically across cell membranes and are expressed in **complementary gradients** that provide directional (planar polarity) information to tissues, feeding into the **Hippo kinase cascade** to restrain the transcriptional co-activator **YAP** (PMID 24056717, 24998526). GO/pathway terms: planar cell polarity pathway (GO:0090175), Hippo signaling (GO:0035329), homophilic cell–cell adhesion via plasma-membrane adhesion molecules (GO:0007156), Reactome "Signaling by Hippo."

**Causal chain (neurodevelopment — best-characterized):**
1. **Trigger (upstream):** Biallelic LoF of *DCHS1* or *FAT4* → loss of Fat–Dachsous PCP signaling in the embryonic neuroepithelium.
2. **De-repression of YAP:** Hippo signaling is disrupted → YAP (Hippo effector) is inappropriately active.
   > "These effects were countered by concurrent knockdown of Yap, a transcriptional effector of the Hippo signaling pathway. These findings implicate Dchs1 and Fat4 upstream of Yap as key regulators of mammalian neurogenesis." (PMID 24056717)
3. **Cellular consequence:** **Expanded neural progenitor proliferation** with **reduced neuronal differentiation** → excess progenitors. Confirmed by DCHS1-intracellular-domain loss expanding neurogenic proliferation (PMID 41972678).
4. **Migration failure:** Loss of Dchs1/Fat4 expression gradients disrupts collective tangential neuronal migration and planar polarity (PMID 24998526).
5. **Clinical manifestation (downstream):** Neurons fail to reach the cortical plate → **periventricular/subcortical neuronal heterotopia**, intellectual disability, and altered functional cerebral asymmetry (PMID 24056717, 25930014).

**Parallel causal chains in other organs (same module, tissue-specific outputs):**
- **Bone/craniofacial:** Dchs1–Fat4 regulates **osteoblast differentiation**; its disruption produces the craniofacial abnormalities of VMS (PMID 31358536). → maxillary hypoplasia, skeletal anomalies, osteopenia.
- **Kidney:** FAT4 fine-tunes kidney development by **regulating RET receptor-tyrosine-kinase signaling**; Fat4 deletion causes duplex-kidney phenotypes (PMID 30853441). → renal agenesis/duplex kidney/urinary obstruction.
- **Cytoskeleton (early embryo):** Dchs1 influences **actin and microtubule** organization, partly independent of Fat, via its intracellular domain (zebrafish; PMID 26160902).
- **Neuronal maintenance:** *Drosophila* fat loss in neurons impairs neuromuscular-junction structure and axonal targeting (PMID 28488382).

**Cellular processes:** cell proliferation/cell-cycle control (GO:0008283), neuron differentiation (GO:0030182), neuron migration (GO:0001764), osteoblast differentiation (GO:0001649), establishment of planar polarity (GO:0001736). **Cell types (CL):** radial glial/neural progenitor cells (CL:0000047 / CL:0000031), migrating neurons (CL:0000540), osteoblasts (CL:0000062), ureteric-bud/renal epithelial cells (CL:1000454). **Subcellular (GO CC):** plasma membrane (GO:0005886), cell–cell junction (GO:0005911), actin cytoskeleton (GO:0015629), microtubule (GO:0005874); YAP acts in the nucleus (GO:0005634).

**Protein dysfunction:** loss of function of large transmembrane protocadherins (adhesion/signaling), not misfolding/aggregation. **Metabolic changes:** none characteristic. **Immune involvement:** none (not an immune disease). **Tissue-damage mechanism:** developmental **malformation/dysplasia** (failed morphogenesis) rather than degeneration, ischemia, or fibrosis. **Molecular profiling (transcriptomics/proteomics/metabolomics/lipidomics):** no patient-derived omics datasets available. **Functional genomics:** mechanistic knockdown/knockout screens in mouse/zebrafish/fly and YAP-epistasis (above) constitute the functional evidence.

---

## 7. Anatomical Structures Affected

**Organ / system level (primary):**
- **Nervous system** (UBERON:0001016): cerebral cortex (UBERON:0000956), periventricular white matter/lateral ventricle margins (UBERON:0002289) — heterotopia; brainstem branchiomotor nuclei (migration). Body system: **nervous**.
- **Ear** (UBERON:0001690): external ear/auricle (UBERON:0001757) — microtia; external auditory canal (UBERON:0001352) — atresia; **middle ear / ossicles / tympanic cavity** (UBERON:0001756) — malformation (PMID 27739185). Body system: **special sensory/auditory**.
- **Craniofacial skeleton & face** (UBERON:0001456 face; UBERON:0001684 mandible/maxilla UBERON:0002397): midface/maxillary hypoplasia.
- **Skeleton / limbs** (UBERON:0002091): hands/digits (UBERON:0002389), vertebral column (UBERON:0002415) — contractures, brachydactyly, scoliosis, osteopenia.

**Secondary / variable organ involvement:**
- **Kidney/urinary tract** (UBERON:0002113 kidney; UBERON:0000056 ureter): agenesis, duplex kidney, ureterovesical obstruction (PMID 28878612, 30853441).
- **Endocrine/reproductive** (UBERON:0000990 reproductive system; hypothalamic–pituitary–gonadal axis): hypogonadotropic hypogonadism, precocious puberty; **breast** (UBERON:0000310) aplasia (PMID 29046692, 40797481).
- **Respiratory tract / trachea** (UBERON:0003126): tracheal anomalies, respiratory problems (PMID 29681106).
- **Gastrointestinal/lymphatic** (UBERON:0002108 small intestine; lymphatic vessels UBERON:0001473): intestinal lymphangiectasia (PMID 31063239).

**Tissue level:** neuroepithelium/neural tissue, connective/skeletal tissue (bone), epithelial tissues (renal, otic). **Cell level (CL):** neural progenitors/radial glia, migrating neurons, osteoblasts, renal epithelial cells (see §6). **Subcellular (GO CC):** plasma membrane, cell–cell junctions, cytoskeleton; nuclear YAP.

**Localization / lateralization:** brain heterotopia typically **bilateral**; ear/hearing involvement **bilateral**; renal malformations may be **unilateral** (e.g., unilateral renal agenesis, PMID 28878612). Notably, functional cerebral asymmetry is *increased* (PMID 25930014).

---

## 8. Temporal Development

- **Onset:** **Congenital / prenatal–neonatal.** Craniofacial, ear, and brain malformations are established in utero; neonatal hypotonia, feeding, and respiratory problems present at birth (PMID 22473091). Intellectual disability manifests through infancy/childhood. Endocrine features (precocious or hypogonadotropic puberty) emerge in childhood/adolescence (PMID 40797481, 29046692).
- **Onset pattern:** **Chronic/static (congenital malformation)** rather than acute.
- **Progression:** Generally **non-progressive/stable** — the structural malformations are fixed; neurodevelopmental deficits remain stable rather than degenerating. In the 2025 case, "the neurodevelopmental deficits remained stable without progression" over 2-year follow-up (PMID 40797481). No defined disease "stages."
- **Progression rate / course:** Static congenital course; lifelong (chronic). Not episodic or relapsing–remitting.
- **Remission:** Not applicable (structural congenital disorder; no spontaneous remission). Specific manifestations are **treatment-modifiable** (e.g., precocious puberty controlled with GnRH analog; hearing improved with implants).
- **Critical periods:** Embryonic corticogenesis and organogenesis are the windows during which the pathology is set; there is no post-natal window to reverse the heterotopia. Intervention windows exist for *managing* sequelae (early hearing amplification for language development; timely endocrine therapy).

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** Orphanet prevalence class **<1/1,000,000**; fewer than ~50 patients reported worldwide since 1992 (only ~9 described by 2016–2017; PMID 27739185). Incidence not quantifiable. No registry/GBD data.

**Inheritance & genetics.**
- **Pattern:** **Autosomal recessive** for both *DCHS1* and *FAT4* forms (PMID 22473091, 24056717).
- **Penetrance:** Essentially **complete** in biallelic individuals (all reported biallelic patients are affected), though **expressivity is variable** (organ involvement and severity differ between patients, even within the same gene).
- **Anticipation:** None (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Consanguinity:** **Important risk factor** — parental consanguinity in 3/5 defining families; homozygous variants common in consanguineous unions (PMID 22473091).
- **Founder effects:** None established; variants are largely private.
- **Carrier frequency:** Not formally estimated; expected very low. Heterozygous carriers are asymptomatic.

**Population demographics.**
- **Affected populations:** Reported across diverse ancestries (European, Middle Eastern, Chinese, Macedonian, etc.; PMIDs 22473091, 40797481, 28878612) — no ethnic predilection beyond enrichment where consanguinity is common.
- **Geographic distribution:** Worldwide, non-endemic.
- **Sex ratio:** No clear sex bias; both sexes affected (autosomal). Some sex-specific manifestations reported (breast aplasia/hypogonadism in a female, PMID 29046692).
- **Age distribution:** Diagnosed from newborn period (PMID 29505454) through adulthood (retrospective WES at age 37, PMID 29046692).

---

## 10. Diagnostics

**Genetic testing (definitive).**
- **Approach:** Molecular confirmation of **biallelic pathogenic variants in *DCHS1* or *FAT4***. **Whole-exome sequencing (WES)** is the principal diagnostic modality and has repeatedly established the diagnosis, including via **reverse phenotyping** and **expanded carrier screening** of parents (PMID 37551355, 29046692, 28878612, 31384091). **WGS** is an alternative that also detects deep-intronic/structural variants. **Multigene panels** for intellectual disability / periventricular heterotopia / malformation syndromes should include *DCHS1*, *FAT4*, and — given phenotypic overlap — *CCBE1* and *ADAMTS3* (Hennekam). **Single-gene testing** is reasonable when the gestalt is classic. **Chromosomal microarray/karyotype/FISH** are typically normal and serve to exclude CNV/aneuploidy mimics. Mitochondrial and repeat-expansion testing are not indicated.

**Imaging & clinical tests.**
- **Brain MRI:** periventricular nodular and subcortical heterotopia — a **recognizable pattern** that, in the right clinical context, should prompt targeted testing (PMID 39462795, 24056717).
- **Temporal-bone high-resolution CT:** external/middle-ear and tympanic-cavity malformations (PMID 27739185).
- **Audiology:** confirms conductive hearing loss; **EEG** documented altered functional cerebral asymmetry in a research setting (PMID 25930014).
- **Renal ultrasound/urography:** for renal agenesis/duplex kidney/obstruction (PMID 28878612).
- **Endocrine labs:** gonadotropins/sex steroids for hypogonadotropic hypogonadism or precocious puberty (PMID 29046692, 40797481).

**Biomarkers / omics diagnostics:** No specific biochemical biomarker; **DNA sequence variants are the diagnostic marker.** No validated RNA/proteomic/metabolomic/epigenomic test; no liquid biopsy role.

**Clinical criteria & differential diagnosis.** No formal consensus criteria; diagnosis rests on the **characteristic facial gestalt + hearing loss + intellectual disability + neuronal heterotopia**, confirmed genetically. **Differential diagnoses:** Hennekam syndrome (allelic *FAT4*; distinguished classically by lymphedema — though intestinal lymphangiectasia can overlap; PMID 31063239, 29681106); other periventricular-heterotopia disorders (*FLNA*-related; ARFGEF2-related; EML1-associated) (PMID 39462795); blepharophimosis-ptosis-epicanthus-inversus syndrome (BPES, *FOXL2*); other multiple-congenital-anomaly/ID syndromes.

**Screening.** Not part of newborn screening. **Cascade/carrier screening** of relatives once the familial variants are known; **expanded carrier screening** can identify at-risk couples (PMID 37551355). Prenatal/preimplantation testing feasible for known familial variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics. Prognosis ranges from **early death in severely affected infants** (two siblings died undiagnosed with multiple congenital anomalies; PMID 37551355) to **survival into adulthood** with stable disability (diagnosis at age 37; PMID 29046692). Mortality is driven by severe neonatal respiratory/feeding complications and major malformations rather than by a degenerative process.
- **Morbidity/function:** Chief long-term morbidities are **intellectual disability** and **conductive hearing loss**, with variable skeletal, renal, endocrine, and respiratory contributions. Disability is lifelong but **non-progressive**.
- **Quality-of-life measures:** No EQ-5D/SF-36/PROMIS data; hearing rehabilitation improves communication/social outcomes (PMID 26491591).
- **Complications:** recurrent respiratory issues (tracheal anomalies), feeding failure/failure-to-thrive, hearing-loss–related language delay, urinary-tract obstruction/renal impairment, endocrine dysfunction; psychosocial impact of craniofacial differences.
- **Recovery potential:** Structural malformations do not resolve, but sequelae are **manageable** (hearing devices, hormone therapy, surgery). Neurodevelopmental deficits are stable.
- **Prognostic factors:** severity/extent of neonatal respiratory and feeding compromise and of CNS involvement predict early outcome; no molecular prognostic biomarker validated (possible gene-specific/genotype effects unproven).

---

## 12. Treatment

**No disease-modifying or curative therapy exists.** Management is **multidisciplinary, supportive, and symptom-directed** (NCIT: Supportive Care, C15277).

- **Pharmacotherapy (symptom-specific):**
  - **GnRH analog (leuprorelin/leuprolide acetate, e.g., Enantone®)** for central precocious puberty — successfully controlled pubertal progression over 2 years (PMID 40797481). NCIT: Leuprolide (C1300); ATC L02AE02.
  - Endocrine replacement/management for hypogonadotropic hypogonadism as clinically indicated (PMID 29046692).
  - No pharmacogenomic considerations specific to VMS.
- **Surgical / interventional:**
  - **Hearing rehabilitation:** bone-conduction hearing device (bone-anchored), or, when tympanic-cavity hypoplasia precludes ossiculoplasty, an **active middle-ear implant (Vibrant Soundbridge)** — improved hearing, social skills, and language (PMID 27739185, 26491591). NCIT: Cochlear/Middle Ear Implant; Hearing Aid.
  - Orthopedic/craniofacial and urological surgery as needed (e.g., for obstruction, scoliosis).
- **Supportive & rehabilitative:** nutritional support/feeding management for infantile feeding difficulties; respiratory care for tracheal anomalies; **physical, occupational, and speech therapy**; special education for intellectual disability. (NCIT: Physical Therapy C15327; Occupational Therapy; Speech Therapy.)
- **Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** **None** developed or in trials; not applicable.
- **Experimental treatments / clinical trials:** **None registered** for VMS (no NCT identifiers).
- **Treatment strategy:** individualized, organ-system–based (audiology, neurodevelopment, endocrinology, nephrology, orthopedics, genetics). No standardized algorithm exists; "Neurodevelopmental deficits were managed with regular follow-ups due to the lack of established therapeutic protocols" (PMID 40797481).

---

## 13. Prevention

- **Primary prevention:** Not preventable at the individual level (congenital genetic disease). **Genetic counseling** is the cornerstone: for consanguineous couples and families with an affected child, recurrence risk is **25%** per pregnancy (autosomal recessive).
- **Secondary prevention (early detection):** early brain MRI/audiology/renal imaging in suspected cases; early hearing amplification to protect language development; endocrine surveillance.
- **Tertiary prevention:** manage complications (hearing devices, hormone therapy, respiratory/feeding support, surgery) to limit disability.
- **Genetic/reproductive prevention:** **carrier/cascade screening**, **expanded carrier screening** for at-risk couples (PMID 37551355), and **prenatal or preimplantation genetic diagnosis** for known familial *DCHS1*/*FAT4* variants.
- **Immunization / behavioral / public-health / environmental / prophylaxis:** Not applicable (no infectious or environmental component).

---

## 14. Other Species / Natural Disease

- **Taxonomy of orthologs studied:** *Mus musculus* (NCBI Taxon 10090), *Danio rerio* (7955), *Drosophila melanogaster* (7227).
- **Orthologous genes:** mouse **Dchs1** (Gene 94176) / **Fat4** (Gene 329628); zebrafish **dchs1b**, **dchs2**, **fat** orthologs; *Drosophila* **ds** (dachsous) and **ft** (fat). The pathway is **deeply evolutionarily conserved** (Fat–Dachsous PCP originally defined in *Drosophila*; PMID 24998526, 28488382).
- **Natural disease in animals:** **No naturally occurring VMS-equivalent** is documented in companion animals or wildlife (OMIA: none specific). Veterinary relevance is limited to experimental models, not spontaneous disease.
- **Comparative biology / conservation:** The neuronal, PCP, cytoskeletal, and growth-control functions of Fat–Dachsous are conserved from flies to mammals; loss produces analogous polarity/migration/proliferation defects across species (PMID 24998526, 26160902, 28488382).
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

VMS mechanism has been dissected chiefly in **animal models** (mammalian and invertebrate); no established patient-derived organoid/iPSC model is prominent in the literature to date.

- **Mouse (mammalian):**
  - *Dchs1* and *Fat4* knockdown/knockout/conditional models. **Phenotype recapitulation:** periventricular/subcortical heterotopia with expanded progenitors and reduced differentiation, reversed by *Yap* knockdown (PMID 24056717); disrupted facial branchiomotor neuron migration/PCP (PMID 24998526); osteoblast-differentiation and craniofacial defects (PMID 31358536); duplex-kidney/RET phenotypes (PMID 30853441). **Genetic model types:** knockout, conditional/tissue-specific knockdown. **Limitation:** individual studies capture single organ systems; no single mouse fully reproduces the whole human syndrome. Resource: **MGI**.
  - A **2026** model targeting the **DCHS1 intracellular domain** reproduced expanded neurogenic proliferation and VMS-like neurodevelopmental defects (PMID 41972678), dissecting domain-specific function.
- **Zebrafish (*Danio rerio*):** maternal-zygotic **dchs1b** (and *dchs2*) mutants — egg-activation, cortical-granule-exocytosis, gastrulation, dorsal-organizer, and actin/microtubule cytoskeleton defects; the Dchs1b intracellular domain rescues microtubule bundling, revealing Fat-independent roles (PMID 26160902). Resource: **ZFIN**. **Use:** early morphogenesis, cytoskeletal biology, PCP.
- **Drosophila melanogaster:** neuron-specific knockdown of **fat** — shortened lifespan, impaired locomotion, neuromuscular-junction and axonal-targeting defects, supporting a neuronal-autonomous contribution of FAT4 loss to the human neuronal phenotype (PMID 28488382). Resource: **FlyBase**. **Use:** conserved Fat/Dachsous PCP, neuronal function.

**Applications:** these models establish the Dchs1–Fat4 → Hippo/YAP axis in neurogenesis, PCP-driven neuronal migration, osteogenesis, and nephrogenesis, and provide platforms for testing pathway-directed interventions (e.g., YAP modulation). **Limitations:** partial phenotype coverage per model; species differences in ear/craniofacial anatomy; absence of a comprehensive humanized model.

---

## Summary of Supported vs. Refuted Hypotheses

**Supported (evidence-based):**
- VMS is autosomal recessive, caused by biallelic *DCHS1* (VMLDS1) or *FAT4* (VMLDS2) LoF variants (PMID 24056717, 22473091).
- Periventricular heterotopia arises from loss of Dchs1/Fat4 → YAP de-repression → excess progenitor proliferation/failed differentiation and migration (PMID 24056717, 24998526, 41972678).
- The same module drives craniofacial/skeletal (osteoblast) and renal (FAT4–RET) phenotypes (PMID 31358536, 30853441).
- VMS and Hennekam syndrome are allelic *FAT4* disorders on a phenotypic spectrum (PMID 24913602, 29681106, 31063239).
- Conductive hearing loss from ear malformation is near-constant and implant-treatable (PMID 27739185, 26491591).

**Refuted / not supported:** No environmental, infectious, or lifestyle etiology; no anticipation; no evidence for a progressive/degenerative course (features are static, PMID 40797481).

## Limitations & Future Directions
- Evidence rests on **case reports/series** (n in the dozens) → frequencies and prognosis are imprecise; no registries, trials, or patient omics.
- **Genotype–phenotype correlations** (*DCHS1* vs *FAT4*; specific domains) and **modifiers** need larger cohorts.
- No **targeted therapy**; the well-defined Hippo/YAP axis is a rational (untested) therapeutic target.
- **Patient-derived iPSC/organoid** models and standardized natural-history studies are priorities.

---

### Key References (PMID)
41972678, 40797481, 39462795, 37551355, 31384091, 31358536, 31063239, 30853441, 29681106, 29505454, 29046692, 28878612, 28488382, 27739185, 26491591, 26160902, 25930014, 24998526, 24913602, 24056717, 22473091.


## Artifacts

- [OpenScientist final report](Van_Maldergem_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Van_Maldergem_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 72 |
| Resolved | 69 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018852` (2 mentions) - the report calls it "Van Maldergem syndrome", "parent"; MONDO calls it **achromatopsia**
- `UBERON:0001756` (1 mention) - the report calls it "middle ear / ossicles / tympanic cavity"; UBERON calls it **middle ear**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001249` (1 mention) - the report calls it "Intellectual disability, mild-to-moderate"; HP calls it **Intellectual disability**
- `HP:0002778` (1 mention) - the report calls it "tracheal anomalies"; HP calls it **Abnormal tracheal morphology**, and lists "Tracheal disease" among its other names
- `UBERON:0002091` (1 mention) - the report calls it "Skeleton / limbs"; UBERON calls it **appendicular skeleton**, and lists "skeleton appendiculare" among its other names
- `UBERON:0003126` (1 mention) - the report calls it "Respiratory tract / trachea"; UBERON calls it **trachea**, and lists "vertebrate trachea" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0018852` - called "Van Maldergem syndrome", "parent"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.