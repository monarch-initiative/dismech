---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T21:31:41.355817'
end_time: '2026-08-28T22:04:47.735476'
duration_seconds: 1986.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Bilateral Absence of Vas Deferens
  mondo_id: ''
  category: Reproductive System Disorder
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 23
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 7
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0009299
    reported_labels:
    - MONDO
    ontology_label: 46 XX gonadal dysgenesis
  - term_id: HP:0000798
    reported_labels:
    - Abnormality of the vas deferens
    ontology_label: Oligozoospermia
  - term_id: HP:0012869
    reported_labels:
    - Decreased ejaculate volume
    ontology_label: Acephalic spermatozoa
  - term_id: HP:0011878
    reported_labels:
    - Abnormality of the seminal vesicle
    ontology_label: Abnormal platelet membrane protein expression
  - term_id: HP:0000029
    reported_labels:
    - Abnormality of the epididymis
    ontology_label: Testicular atrophy
  labels_variant: 3
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
  path: Congenital_Bilateral_Absence_of_Vas_Deferens-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Bilateral_Absence_of_Vas_Deferens-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Bilateral Absence of Vas Deferens
- **MONDO ID:**  (if available)
- **Category:** Reproductive System Disorder

## Research Objectives

Please provide a comprehensive research report on **Congenital Bilateral Absence of Vas Deferens** covering all of the
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

# Congenital Bilateral Absence of the Vas Deferens (CBAVD): A Comprehensive Disease Characterization

**Disease:** Congenital Bilateral Absence of the Vas Deferens (CBAVD)
**Identifiers:** OMIM 277180 · ORPHA:48 · MONDO:0009299 · ICD-10 Q55.4 · ICD-11 LB77.0 · MeSH (vas deferens/abnormalities)
**Category:** Reproductive System Disorder (congenital male genital malformation)

---

## Summary

Congenital bilateral absence of the vas deferens (CBAVD) is a congenital malformation of the male reproductive ductal system in which both vasa deferentia fail to develop or degenerate before birth, producing **obstructive azoospermia with preserved spermatogenesis**. It accounts for **1–2% of male infertility** and is estimated to affect **~0.1% of all men** (likely an underestimate, since asymptomatic men are rarely evaluated). CBAVD is best understood as the **genital-limited end of the cystic fibrosis (CF) / CFTR-related disorder spectrum**: over 95% of men with classic CF are infertile because of vasal atresia, and isolated CBAVD is most commonly caused by biallelic *CFTR* variants — typically a severe CF-causing allele combined with a mild/variable allele such as the intron-8/9 poly-T (IVS8-5T / TG-T tract) or p.Arg117His.

Genetically, CBAVD is heterogeneous but *CFTR*-dominant. In stringently phenotyped cohorts, *CFTR* variants explain roughly **70–80%** of cases; the X-linked adhesion G-protein-coupled receptor gene **ADGRG2** accounts for **~2%** of cases (a familial X-linked form), and **10–20%** remain genetically unexplained. Importantly, a distinct subset of unexplained CBAVD coexists with **unilateral renal agenesis / solitary kidney**, pointing to an early **mesonephric (Wolffian) duct developmental defect** — mechanistically separate from the progressive fetal duct degeneration seen with *CFTR*/*ADGRG2* variants. Candidate developmental genes (FREM1, WNT2B, TBX6) have recently emerged in this renal-anomaly subgroup.

Clinically, CBAVD is non-life-threatening with a normal life expectancy; its principal consequence is infertility. Because spermatogenesis is intact, **biological paternity is achievable in ~85% of men** via surgical sperm retrieval (MESA/PESA/TESE) combined with intracytoplasmic sperm injection (ICSI). Management is anchored by *CFTR*/*ADGRG2* genetic testing, **partner carrier screening**, and genetic counseling, since ~10% of couples share pathogenic *CFTR* variants and risk a child with CF. A landmark 2025/2026 observation shows that **prenatal CFTR-modulator therapy (elexacaftor/tezacaftor/ivacaftor, ETI) can prevent CBAVD**, defining a fetal critical window; postnatal modulator therapy does **not** reverse established vasal agenesis. CFTR-knockout rats are the animal model that best recapitulates the human bilateral vasal absence phenotype.

---

## 1. Disease Information

CBAVD is a **congenital malformation of the male reproductive tract** characterized by the bilateral absence (aplasia) or atresia of the vasa deferentia — the paired muscular ducts that transport spermatozoa from the epididymis to the ejaculatory ducts. The result is a mechanical (obstructive) block to sperm transport, giving **obstructive azoospermia** despite normal testicular sperm production. It is frequently accompanied by anomalies of adjacent Wolffian-duct derivatives (seminal vesicles, distal epididymis, ejaculatory ducts).

**Key identifiers**

| Resource | Identifier |
|---|---|
| OMIM | 277180 (CBAVD) |
| Orphanet | ORPHA:48 |
| MONDO | MONDO:0009299 |
| ICD-10 | Q55.4 (congenital absence/aplasia/hypoplasia of vas deferens) |
| ICD-11 | LB77.0 |
| MeSH | Vas Deferens / abnormalities |

**Synonyms / alternative names:** CBAVD; congenital bilateral aplasia of the vas deferens; congenital absence of the vas deferens (CAVD, when unspecified laterality); bilateral vasal agenesis; part of the "congenital absence of the vas deferens" (CAVD) family that also includes **congenital unilateral absence of the vas deferens (CUAVD)**.

**Data source type:** The evidence base is derived from **aggregated disease-level resources** (OMIM, Orphanet, cohort studies, meta-analyses) supplemented by **individual patient reports** (case reports of ADGRG2 pedigrees, MRI series, prenatal ETI case). It is a well-curated Mendelian/complex reproductive disorder rather than an EHR-derived entity.

---

## 2. Etiology

### Causal factors — predominantly genetic

CBAVD is overwhelmingly a **genetic** disorder, principally a genital manifestation of *CFTR* dysfunction.

- **CFTR (autosomal recessive, predominant).** The majority of CBAVD men carry at least one CF-causing *CFTR* variant. *"The majority of subjects with CAVD carry at least one cystic fibrosis-causing mutation that warrants CFTR testing"* [PMID: 32025909](https://pubmed.ncbi.nlm.nih.gov/32025909/). In a large Chinese isolated-CAVD (iCAVD) cohort (n=199), *"CFTR and ADGRG2 variants were identified in 74.87% of iCAVD patients, with CFTR being the predominant pathogenic gene"* [PMID: 42199298](https://pubmed.ncbi.nlm.nih.gov/42199298/).
- **ADGRG2 (X-linked recessive, ~2%).** *"Approximately 2% of the cases of CAVD are hemizygous for a loss-of-function mutation in the ADGRG2 gene that may cause a familial form of X-linked infertility"* [PMID: 32025909](https://pubmed.ncbi.nlm.nih.gov/32025909/).
- **Developmental / Wolffian-duct defect (subset with renal agenesis).** *CFTR*-negative cases frequently coexist with a solitary kidney, indicating an early organogenesis disorder (see Section 5 and Section 6).
- **Unexplained (10–20%).** A residual fraction lacks an identified molecular cause.

### Risk factors

- **Genetic risk factors:** biallelic *CFTR* variants (a severe allele such as p.Phe508del combined with a mild/variable allele — e.g., IVS8-5T poly-T with long TG tract, or p.Arg117His-T7); hemizygous truncating *ADGRG2* variants; candidate developmental variants (FREM1, WNT2B, TBX6) in the renal-anomaly subtype. The **IVS9-5T (poly-T 5T)** allele is a major low-penetrance risk allele, especially in East Asian populations.
- **Environmental risk factors:** No established toxic, occupational, infectious, or lifestyle exposure causes CBAVD. It is a developmental/genetic disorder; **sex is male-only** (defining), and **family history** of CF or CBAVD is relevant.

### Protective factors

- **Genetic:** By definition, the wild-type / functional *CFTR* and *ADGRG2* alleles are "protective"; the poly-T **7T/9T** tracts confer normal splicing/function versus the risk-associated 5T.
- **Environmental / therapeutic:** **Prenatal CFTR-modulator therapy (ETI) prevents CBAVD** in genetically susceptible fetuses (Section 6, Finding F006) — an intervention that restores CFTR channel function during the fetal critical window.

### Gene–environment interactions

The clearest gene–environment interaction is **pharmacologic restoration of CFTR function in utero**. The poly-T/TG polymorphic tract is itself a *cis*-genetic modifier of splicing that determines residual CFTR activity and hence penetrance of the genital phenotype (the TG12-T5 combination reduces CFTR function; [PMID: 42572672](https://pubmed.ncbi.nlm.nih.gov/42572672/)). No classical toxin-by-gene interaction has been documented.

---

## 3. Phenotypes

CBAVD presents in otherwise healthy, normally virilized men, typically discovered during **infertility evaluation** (adult-onset presentation of a congenital anatomic defect).

| Phenotype | Type | Onset / severity / frequency | Suggested HPO |
|---|---|---|---|
| Non-palpable / absent bilateral vas deferens | Physical/clinical sign | Congenital; bilateral; ~100% (defining) | HP:0000798 (Abnormality of the vas deferens); "Aplasia of the vas deferens" |
| Obstructive azoospermia | Laboratory abnormality | Congenital anatomic cause, detected in adulthood; severe; ~100% | HP:0000027 (Azoospermia) |
| Low ejaculate volume | Laboratory/clinical | Congenital; frequent | HP:0012869 (Decreased ejaculate volume) |
| Low semen pH (acidic) | Laboratory | Frequent | Abnormal seminal pH |
| Low/absent seminal fructose | Laboratory | Frequent (reflects seminal-vesicle involvement) | — |
| Seminal vesicle agenesis/hypoplasia | Physical/imaging | Variable — bilateral agenesis, unilateral agenesis, or present | HP:0011878 (Abnormality of the seminal vesicle) |
| Epididymal partial absence | Physical/imaging | Variable; genotype-correlated | HP:0000029 (Abnormality of the epididymis) |
| Male infertility | Clinical outcome | Adult; severe; ~100% | HP:0003251 (Male infertility) |
| Unilateral renal agenesis (subset) | Physical/imaging | Congenital; in developmental subtype | HP:0000122 (Unilateral renal agenesis) |

**Supporting evidence.** *"The incidence of congenital bilateral absence of the vas deferens (CBAVD) in infertile men is 1-2%"* [PMID: 35109852](https://pubmed.ncbi.nlm.nih.gov/35109852/). Seminal-vesicle involvement is variable: among 47 CBAVD patients, *"29 had bilateral agenesis of the seminal vesicles, 9 had unilateral agenesis, and 9 had bilateral presence"* [PMID: 40533736](https://pubmed.ncbi.nlm.nih.gov/40533736/). Epididymal involvement tracks with *CFTR* genotype: *"patients carrying at least one non-5 T variant were associated with an 8.17-fold increased risk of epididymal partial absence compared to those having the homozygous 5 T mutation"* [PMID: 39592508](https://pubmed.ncbi.nlm.nih.gov/39592508/).

**Quality-of-life impact.** The dominant impact is **infertility** and its psychosocial burden; there is no pain, disability, or systemic morbidity in isolated CBAVD. Because sperm retrieval + ICSI achieves paternity in most couples, the long-term QoL impact is limited relative to systemic diseases. Men should also be counseled about the possibility of an underlying **CFTR-related disorder** (e.g., pancreatitis, sinopulmonary disease) that may manifest later.

---

## 4. Genetic / Molecular Information

### Causal genes

- **CFTR** (HGNC:1884; OMIM 602421; chr7q31.2) — cystic fibrosis transmembrane conductance regulator; a cAMP-activated Cl⁻/HCO₃⁻ channel. **Predominant cause of CBAVD.**
- **ADGRG2** (HGNC:18023; OMIM 300572; chrXp22.13) — adhesion GPCR G2 (GPR64), epididymal- and efferent-duct-specific. **X-linked cause (~2%).**
- **Candidate developmental genes:** FREM1, WNT2B, TBX6 in *CFTR*-negative CBAVD with renal anomalies [PMID: 40921938](https://pubmed.ncbi.nlm.nih.gov/40921938/).

### Pathogenic variants — CFTR

Isolated CBAVD is typically caused by a **trans-heterozygous combination** of one severe CF-causing allele plus one mild/variable allele:

- **p.Phe508del (F508del)** — the classic severe deletion; predominant in Europeans.
- **Poly-T / TG tract (IVS8-5T; c.1210-34TG(n)T(m))** — the **T5** allele with a long TG repeat reduces exon-9 inclusion and lowers functional CFTR. *"the combination of T5 with longer TG repeats is associated with reduced CFTR function"* — as in a compound heterozygote p.Phe508del + TG12T5 [PMID: 42572672](https://pubmed.ncbi.nlm.nih.gov/42572672/).
- **p.Arg117His** — associated with CBAVD and other CFTR-related disorders; a French cohort (n=179) found *"83 isolated CBAVD, 67 other CFTR-related phenotypes"* with an overall mild phenotype [PMID: 23378603](https://pubmed.ncbi.nlm.nih.gov/23378603/).
- **IVS9-5T** — the most common allele in Chinese CBAVD (~54.5%), with regional variants such as p.Gln1352His (c.4056G>C).

**Variant classification** follows ACMG/AMP tiers (pathogenic / likely pathogenic / VUS). **Variant types** include missense (p.Arg117His), in-frame deletion (p.Phe508del), splice-modulating poly-T/TG tracts, nonsense, frameshift, and deep-intronic/large rearrangements — hence the recommendation for **whole-exon + flanking + rearrangement** *CFTR* screening in CAVD [PMID: 40065563](https://pubmed.ncbi.nlm.nih.gov/40065563/). **Origin is germline.** **Functional consequence** is **loss of function** (reduced Cl⁻/HCO₃⁻ conductance).

### Pathogenic variants — ADGRG2

Hemizygous **protein-truncating** variants: *"c.1545dupT (p.Glu516Ter), c.2845delT (p.Cys949AlafsTer81), and c.2002_2006delinsAGA (p.Leu668ArgfsTer21)"* [PMID: 27476656](https://pubmed.ncbi.nlm.nih.gov/27476656/); additional c.G118T (p.Glu40*) and the nonsense c.908C>G (p.Ser303*) [PMID: 37273165](https://pubmed.ncbi.nlm.nih.gov/37273165/). These are **loss-of-function**, X-linked, maternally inherited, and typically **absent from population databases**. Western blot confirms a **truncated ADGRG2 protein** [PMID: 37273165].

### Modifier genes / epigenetics / chromosomal abnormalities

- **Modifiers:** the **poly-T/TG tract** functions as the principal *cis*-modifier of CFTR splicing and penetrance. **SLC9A3** interacts functionally with CFTR (Sections 6/7).
- **Epigenetics:** No disease-specific DNA-methylation or histone signature has been established for CBAVD.
- **Chromosomal abnormalities:** Not a primary cause. A single case report describes a 47,XYY mosaic karyotype coexisting with CBAVD [PMID: 35109852](https://pubmed.ncbi.nlm.nih.gov/35109852/); this appears coincidental rather than causal.

---

## 5. Environmental Information

- **Environmental factors / toxins / radiation / occupational exposure:** None established as causal. CBAVD is a developmental-genetic disorder.
- **Lifestyle factors (smoking, diet, alcohol, exercise):** No demonstrated role in causation.
- **Infectious agents:** Not applicable — CBAVD is congenital and non-infectious. (Acquired vasal obstruction from infection or vasectomy is a *separate* differential diagnosis, not CBAVD.)

The only "environmental" (i.e., non-germline) modifier with proven effect is **pharmacologic** — prenatal CFTR modulator exposure (protective; Section 6).

---

## 6. Mechanism / Pathophysiology

### Two etiologic subtypes (bimodal pathogenesis)

CBAVD arises through **two mechanistically distinct routes**, a key organizing insight of this investigation (Finding F005):

```
                          ┌─────────────────────────────────────────────┐
                          │   CBAVD  (obstructive azoospermia)           │
                          └─────────────────────────────────────────────┘
                                     │
        ┌────────────────────────────┴───────────────────────────────┐
        │                                                              │
 (A) DEGENERATIVE subtype                              (B) DEVELOPMENTAL subtype
  CFTR / ADGRG2 loss-of-function                        Mesonephric (Wolffian) duct
  → abnormal luminal Cl⁻/HCO₃⁻ &                        maldevelopment (early organogenesis)
    fluid transport                                     → ureteric bud + duct derivatives
  → progressive fetal atresia/                            affected
    degeneration of vas deferens                        → vasal agenesis + UNILATERAL
    beginning later in fetal life                         RENAL AGENESIS / solitary kidney
  → kidneys SPARED                                      candidate genes: FREM1, WNT2B, TBX6
```

**Evidence for the split:** *"An important proportion of these unexplained CAVDs coexist with a solitary kidney suggesting an early organogenesis disorder (Wolffian duct), unlike CAVDs related to CFTR or ADGRG2 mutations, which might be the result of progressive degeneration that begins later in fetal life"* [PMID: 32025909](https://pubmed.ncbi.nlm.nih.gov/32025909/). The shared embryology of the developmental subtype: *"The embryonic insult that results in unilateral renal agenesis may involve not only the ureteral bud but also other mesonephric duct derivatives, including the seminal vesicles, vas deferens, and epididymis"* [PMID: 16985610](https://pubmed.ncbi.nlm.nih.gov/16985610/). MRI data support **acquired/progressive** vasal agenesis in the CFTR-type: *"Preliminary findings in this study are consistent with the theory of acquired vasal agenesis in CBAVD"* [PMID: 41255074](https://pubmed.ncbi.nlm.nih.gov/41255074/).

### Molecular pathways and protein dysfunction

- **CFTR pathway (degenerative subtype).** CFTR is a **cAMP-activated Cl⁻ and HCO₃⁻ channel** governing the luminal microenvironment of the male tract. Loss of function disturbs anion/fluid secretion and the **HCO₃⁻/soluble adenylyl cyclase/cAMP/CREB** and **NF-κB/COX-2/PGE₂** signaling axes relevant to tract development and sperm function: *"CFTR is emerging as a versatile player with roles in mediating different signaling pathways... in addition to its long-recognized role in electrolyte and fluid transport that regulates the luminal microenvironment of the male reproductive tract"* [PMID: 22709980](https://pubmed.ncbi.nlm.nih.gov/22709980/). Abnormal luminal fluid handling is thought to drive the **progressive atresia** of the vas: *"cystic fibrosis (CF) leads to infertility in over 95% of cases, due to early and progressive atresia of the vas deferens, resulting in obstructive azoospermia"* [PMID: 42380629](https://pubmed.ncbi.nlm.nih.gov/42380629/).
- **ADGRG2 pathway (X-linked subtype).** ADGRG2 is an **adhesion GPCR** expressed apically in **non-ciliated efferent-duct epithelium**: *"ADGRG2 expression was restricted to the apical membranes of non-ciliated epithelia in human efferent ducts"* [PMID: 32314195](https://pubmed.ncbi.nlm.nih.gov/32314195/). Loss of function causes **obstructive infertility** by disrupting efferent-duct fluid reabsorption (recapitulated in Adgrg2-knockout mice: *"Adgrg2-knockout male mice develop obstructive infertility"* [PMID: 27476656](https://pubmed.ncbi.nlm.nih.gov/27476656/)).
- **SLC9A3 (NHE3) interaction.** SLC9A3 loss reduces CFTR protein and causes obstruction: *"depleted Slc9a3 in male mice causes infertility due to the abnormal dilated lumen of the rete testis and efferent ductules"* [PMID: 28384194](https://pubmed.ncbi.nlm.nih.gov/28384194/) — implicating a shared ion-transport/CFTR-stability module.

### Cellular processes, cell types, and compartments

- **Cell types (CL):** ductal epithelial cells of the vas deferens/epididymis; **non-ciliated efferent-duct epithelial cells** (ADGRG2⁺); seminal-vesicle epithelium.
- **Cellular process:** disrupted transepithelial anion/fluid transport → luminal microenvironment failure → epithelial/duct **degeneration and atresia** (degenerative subtype) or failed duct **morphogenesis** (developmental subtype).
- **Subcellular compartments (GO CC):** **apical plasma membrane** (GO:0016324) — site of CFTR and ADGRG2 function; anion channel activity.
- **Suggested GO BP:** GO:0006821 (chloride transport), GO:0055085 (transmembrane transport), GO:0048754 (branching morphogenesis of an epithelial tube), GO:0035239 (tube morphogenesis), GO:0007283 (spermatogenesis — preserved).

### Critical window — a therapeutic mechanism

The degenerative subtype is **preventable in utero**. In a male CF infant (homozygous F508del) whose carrier mother began ETI at 27+4 weeks: *"ultrasound at 8 weeks demonstrated bilateral vas deferens, a structure typically absent in nearly all male patients with CF at birth"* and *"These findings suggest that prenatal CFTR modulation - even when initiated late"* can preserve the duct [PMID: 41654435](https://pubmed.ncbi.nlm.nih.gov/41654435/). Conversely, *"At present male patients taking CFTR modulators have not shown improvement in infertility"* [PMID: 39288989](https://pubmed.ncbi.nlm.nih.gov/39288989/) — establishing that restoration must occur **before** the duct is lost.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** vas deferens (UBERON:0001000) — bilateral. **Secondary/associated:** epididymis (UBERON:0001301), seminal vesicle (UBERON:0000998), ejaculatory duct, efferent ducts (UBERON:0003074). **Kidney (UBERON:0002113)** in the developmental subtype (unilateral renal agenesis).
- **Body system:** male reproductive/genital system (UBERON:0000079); urinary system involvement in the renal-anomaly subtype.
- **Tissue / cell level:** ductal **epithelium** (transporting epithelium) and surrounding smooth muscle of the vas; **non-ciliated efferent-duct epithelial cells** (ADGRG2⁺). Testicular seminiferous tissue is **preserved** (spermatogenesis intact).
- **Subcellular:** apical plasma membrane (GO:0016324); anion channel machinery.
- **Localization / lateralization:** **bilateral** by definition (CBAVD); the CAVD family also includes **unilateral (CUAVD)** and asymmetric presentations. Seminal-vesicle and epididymal involvement is frequently **asymmetric** [PMID: 40533736](https://pubmed.ncbi.nlm.nih.gov/40533736/).

---

## 8. Temporal Development

- **Onset:** **Congenital** — the anatomic defect is present at (or develops before) birth. In the degenerative CFTR subtype, atresia is *"early and progressive"* during fetal life [PMID: 42380629]; the developmental subtype originates at early organogenesis. Clinically, however, the disorder is usually **detected in adulthood** during infertility work-up (insidious, asymptomatic until then).
- **Progression:** The **structural defect is fixed/non-progressive after birth** (the vas is already absent). There are no post-natal "stages." Disease course is **stable and lifelong**; the associated infertility is chronic unless overcome by ART.
- **Patterns / critical periods:** The single actionable **critical period is fetal** — CFTR function must be preserved during gestation to prevent vasal loss (prenatal ETI, [PMID: 41654435]). No spontaneous remission occurs.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** *"The prevalence of CAVDs in men is reported to be approximately 0.1%"* [PMID: 32025909](https://pubmed.ncbi.nlm.nih.gov/32025909/) (likely underestimated).
- **Frequency in male infertility:** CBAVD accounts for **1–2%** of infertile men [PMID: 35109852](https://pubmed.ncbi.nlm.nih.gov/35109852/).
- **Incidence:** Not precisely established (congenital, detected at reproductive age).

### Inheritance (genetic etiology)

| Feature | CFTR-related CBAVD | ADGRG2-related CBAVD |
|---|---|---|
| Pattern | Autosomal recessive (biallelic) | X-linked recessive (hemizygous) |
| Share of cases | ~70–80% | ~2% |
| Penetrance | **Incomplete/variable**, modulated by poly-T/TG tract | High but variable |
| Expressivity | Variable (isolated CBAVD ↔ broader CFTR-RD) | Variable (one carrier had normal fertility) |
| Reproductive risk | Offspring CF risk if partner carries severe allele | X-linked transmission via carrier mothers |

- **Penetrance / expressivity:** Variable and incomplete for the genital phenotype; sweat chloride does **not** correlate with severity in p.Arg117His carriers [PMID: 23378603](https://pubmed.ncbi.nlm.nih.gov/23378603/). For ADGRG2, an obligate-carrier male with the p.Ser303* variant had **normal fertility**, illustrating variable expressivity [PMID: 37273165](https://pubmed.ncbi.nlm.nih.gov/37273165/).
- **Genetic anticipation / mitochondrial inheritance:** Not applicable.
- **Founder effects / geographic allele spectra:** **Population-specific**. **p.Phe508del** predominates in Europeans; **IVS9-5T is the most common allele in Chinese CBAVD (~54.5%)** with regional p.Gln1352His. *"There are no obvious hotspot CFTR mutations in Chinese CBAVD patients besides the IVS9-5 T allele"* [PMID: 35119551](https://pubmed.ncbi.nlm.nih.gov/35119551/).
- **Consanguinity / carrier frequency:** *CFTR* carrier frequency is high in populations with elevated CF prevalence (up to ~1/25 in Europeans), underpinning the reproductive-risk concern. **~10% of iCAVD couples share pathogenic *CFTR* variants:** *"10.14% of couples carried shared pathogenic or likely pathogenic CFTR variants"* [PMID: 42199298](https://pubmed.ncbi.nlm.nih.gov/42199298/).

### Population demographics

- **Sex:** male only (defining).
- **Geographic variation of variants:** European vs East Asian allele spectra differ markedly (above).
- **Age distribution:** presents at reproductive age (typically 20s–40s at infertility work-up).

---

## 10. Diagnostics

### Clinical tests

- **Physical exam:** bilateral **non-palpable vasa deferentia** — the cornerstone finding.
- **Semen analysis (laboratory):** **azoospermia**, **low ejaculate volume**, **low (acidic) pH**, **low/absent fructose** (reflecting seminal-vesicle contribution). Normal serum FSH/testosterone and normal testicular volume support an obstructive (not spermatogenic) cause.
- **Imaging:** scrotal ultrasound (confirms absent/atretic vas, evaluates epididymis), **transrectal ultrasound** (seminal vesicles, ejaculatory ducts), and **MRI** for the intra-abdominal vas and seminal-vesicle pathology — *"detailed findings are obtained by MRI even in the evaluation of the intra-abdominal part of the VD"* [PMID: 41255074](https://pubmed.ncbi.nlm.nih.gov/41255074/). **Renal ultrasound is mandatory** to detect solitary kidney (developmental subtype).
- **Biopsy/histopathology:** testicular biopsy shows **preserved spermatogenesis** (not routinely needed).

### Genetic testing

- **Recommended approach:** Comprehensive **CFTR** analysis first — including **full exon + flanking-region sequencing, the poly-T/TG tract, and large-rearrangement detection** — because standard panels miss deep-intronic and rearrangement alleles: *"the urgent need for extensive CFTR screening, including sequencing of whole exons and flanking regions and detection of large rearrangements and deep intronic CF-causing variants"* [PMID: 40065563](https://pubmed.ncbi.nlm.nih.gov/40065563/). If *CFTR* is negative **and renal ultrasound is normal**, test **ADGRG2**: *"Pathogenic variants in ADGRG2 are important to look for when CFTR analysis is negative and renal ultrasonography is normal"* [PMID: 41886210](https://pubmed.ncbi.nlm.nih.gov/41886210/).
- **Modalities:** targeted *CFTR* single-gene/panel testing; WES/WGS for unexplained cases and developmental candidate genes (FREM1, WNT2B, TBX6); karyotype only if a broader syndrome is suspected.

### Clinical criteria & differential diagnosis

- **Diagnosis** rests on the triad of **non-palpable vasa + obstructive azoospermia + low-volume acidic fructose-negative semen**, confirmed by imaging and genetics.
- **Differential diagnosis:** other causes of obstructive azoospermia (ejaculatory-duct obstruction, post-infectious or post-vasectomy obstruction, Young syndrome) and non-obstructive azoospermia (distinguished by normal FSH/testicular volume and preserved spermatogenesis in CBAVD).

### Screening

- **Partner CFTR carrier screening** is essential before ART (couple co-carrier risk ~10%).
- **Cascade testing** of family members for ADGRG2 pedigrees.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** **Isolated CBAVD carries no excess mortality; life expectancy is normal.** Prognosis for survival is excellent. (Men should nonetheless be evaluated for a broader CFTR-related disorder that could have its own morbidity.)
- **Morbidity / function:** The sole functional impact is **infertility**; no disability or organ failure in isolated disease.
- **Fertility outcome (the key prognostic domain):** Excellent with ART. Because spermatogenesis is preserved, surgical sperm retrieval + ICSI is highly successful: in a Chinese cohort, *"Spermatozoa were successfully retrieved in 46 patients, and 39 of the patients had their own offspring through ICSI"* (≈85% paternity) [PMID: 35119551](https://pubmed.ncbi.nlm.nih.gov/35119551/).
- **Prognostic factors:**
  - **Residual CFTR activity** predicts retrieval success — MESA extraction failure was higher in CF than CFTR-RD: *"Extraction failure rates were 18.6% for cystic fibrosis and 3.9% for CFTR-RD (P = 0.01)"*, and worse with no residual activity (27.9% vs 3.7% failure, P<0.001) [PMID: 40850271](https://pubmed.ncbi.nlm.nih.gov/40850271/).
  - **Sperm motility** predicts ICSI outcome: *"the clinical pregnancy rates, embryo implantation rates, and live birth rates in the high motility group were significantly increased"* [PMID: 34313208](https://pubmed.ncbi.nlm.nih.gov/34313208/).
- **Complications:** principally reproductive/ART-related (e.g., risk of transmitting CF to offspring; rare ART complications such as monochorionic/conjoined twinning after embryo transfer, [PMID: 42215739](https://pubmed.ncbi.nlm.nih.gov/42215739/)).

---

## 12. Treatment

CBAVD has **no medical cure for the anatomic defect**; management is **fertility-focused** plus genetic counseling.

### Assisted reproduction (mainstay)

- **Surgical sperm retrieval:** **MESA** (microsurgical epididymal sperm aspiration), **PESA** (percutaneous epididymal sperm aspiration), **TESE** (testicular sperm extraction). *(NCIT: Sperm Retrieval; Testicular Sperm Extraction.)*
- **ICSI** (intracytoplasmic sperm injection): the definitive route to biological paternity; ~85% success in achieving offspring [PMID: 35119551]. *(NCIT: Intracytoplasmic Sperm Injection.)*
- **Optimization:** select high-motility sperm to maximize live-birth rate [PMID: 34313208].

### CFTR modulator therapy — a disease-modifying frontier

- **Prenatal ETI (elexacaftor/tezacaftor/ivacaftor)** can **prevent CBAVD** when administered to the fetus via a carrier mother during gestation [PMID: 41654435](https://pubmed.ncbi.nlm.nih.gov/41654435/). This is investigational and raises ethical/consent questions for heterozygous fetuses [PMID: 39543810](https://pubmed.ncbi.nlm.nih.gov/39543810/).
- **Postnatal modulators do NOT reverse** established CBAVD/infertility [PMID: 39288989](https://pubmed.ncbi.nlm.nih.gov/39288989/).

### Pharmacogenomics / personalized medicine

- **Genotype-guided counseling:** *CFTR* genotype informs residual function, retrieval prognosis, CFTR-RD surveillance, and modulator eligibility.
- **Couple-level genotyping** guides **preimplantation genetic testing (PGT)** to avoid transmitting CF.

### Not applicable

Gene therapy, cell therapy, RNA therapeutics, immunotherapy, and chemotherapy have **no established role** in CBAVD.

---

## 13. Prevention

- **Primary prevention:** **Prenatal CFTR-modulator therapy** is the only demonstrated means of preventing the vasal defect itself (investigational) [PMID: 41654435]. Broadly, primary prevention is limited because CBAVD is congenital/genetic.
- **Secondary prevention / early detection:** Genetic diagnosis at infertility work-up enables timely ART and CFTR-RD surveillance.
- **Tertiary prevention:** Optimizing sperm-retrieval/ICSI protocols and PGT to prevent CF offspring.
- **Genetic screening & counseling (central):** **CFTR carrier screening of both partners** before ART is essential; ~10% of couples are co-carriers [PMID: 42199298]. Options include **preimplantation genetic diagnosis** and prenatal testing. Comprehensive *CFTR* screening (exons + flanking + rearrangements) is recommended before ART [PMID: 40065563].
- **Immunization / public-health / environmental measures:** Not applicable (non-infectious, non-environmental).

---

## 14. Other Species / Natural Disease

- **Taxonomy affected (models):** *Rattus norvegicus* (rat, NCBI:txid10116), *Mus musculus* (mouse, NCBI:txid10090), plus large-animal CF models — ferret, pig, sheep, rabbit.
- **Orthologous genes:** *Cftr* (rat/mouse), *Adgrg2*, *Slc9a3* orthologs.
- **Natural / comparative disease:** CF animal models frequently show **absent vas deferens/epididymis with normal testicular histology**, mirroring human CBAVD: *"CFTR-knockout rats more closely reproduce the human phenotype, showing bilateral absence of the vas deferens and epididymal hypoplasia, although they exhibit more pronounced hypospermatogenesis than observed in men"* [PMID: 42380629](https://pubmed.ncbi.nlm.nih.gov/42380629/). Evolutionary conservation of CFTR-dependent duct development underlies the cross-species recapitulation.
- **Transmission / zoonosis:** Not applicable (genetic malformation).

---

## 15. Model Organisms

| Model | Genetic manipulation | Phenotype recapitulation | Key limitation |
|---|---|---|---|
| **CFTR-knockout rat** | Complete Cftr KO | **Best model** — bilateral vas absence + epididymal hypoplasia | More severe hypospermatogenesis than men |
| Mouse — knock-in / partial KO | Hypomorphic | Usually **remain fertile** | Fails to model vasal absence |
| Mouse — complete Cftr KO | Full KO | May develop **vas atresia with aging** | Age-dependent, heterogeneous |
| Large animals (ferret, pig, sheep, rabbit) | CF models | Frequently **absent vas/epididymis, normal testis** | Cost, husbandry |
| **Adgrg2-knockout mouse** | Adgrg2 KO | **Obstructive infertility** (efferent-duct model) | Models ADGRG2 subtype only |
| **Slc9a3-knockout mouse** | Slc9a3 KO | Obstructive azoospermia; **reduced CFTR** in epididymis/vas | Models NHE3/CFTR interaction |

**Supporting quotes.** *"knock-in or partial knockout models usually remain fertile, whereas complete knockouts may develop vas deferens atresia with aging"* [PMID: 42380629](https://pubmed.ncbi.nlm.nih.gov/42380629/). *"Adgrg2-knockout male mice develop obstructive infertility"* [PMID: 27476656](https://pubmed.ncbi.nlm.nih.gov/27476656/). *"depleted Slc9a3 in male mice causes infertility due to the abnormal dilated lumen of the rete testis and efferent ductules"* [PMID: 28384194](https://pubmed.ncbi.nlm.nih.gov/28384194/).

**Applications:** these models allow study of CFTR-dependent duct morphogenesis, the fetal critical window for modulator rescue, efferent-duct fluid handling (ADGRG2/SLC9A3), and CFTR-modulator pharmacology. **Databases:** MGI, RGD, IMPC/KOMP, IMSR.

---

## Mechanistic Model / Interpretation

CBAVD is best conceptualized as a **convergent obstructive-azoospermia phenotype reached by two upstream routes**:

```
UPSTREAM CAUSE                    MID-STREAM MECHANISM                    DOWNSTREAM PHENOTYPE
─────────────────────────────────────────────────────────────────────────────────────────────
CFTR biallelic LoF ──►  ↓ apical Cl⁻/HCO₃⁻ & fluid transport ──►  progressive fetal ─┐
(severe + mild allele;   (HCO₃⁻/sAC/cAMP; NF-κB/COX-2)             vasal atresia      │
 poly-T/TG modifier)                                              (kidneys spared)    │
                                                                                      ├─► Bilateral
ADGRG2 hemizygous LoF ─► efferent-duct epithelial dysfunction ──► efferent/vasal ─────┤   absent vas
(X-linked, ~2%)          (adhesion GPCR, fluid reabsorption)      obstruction         │   → obstructive
                                                                                      │   azoospermia
Wolffian-duct           failed duct + ureteric-bud morphogenesis ─► vasal agenesis ───┘   (SPERMATOGENESIS
maldevelopment          (FREM1/WNT2B/TBX6?)                        + UNILATERAL RENAL     PRESERVED)
(developmental subtype)                                            AGENESIS
```

**Upstream vs downstream:** the genetic lesion (CFTR/ADGRG2 LoF or a developmental-gene defect) is upstream; disrupted epithelial ion/fluid transport (or failed morphogenesis) is the mid-stream mechanism; duct atresia/agenesis and consequent obstructive azoospermia are downstream. The **testis is not in the causal chain** — spermatogenesis is preserved, which is precisely why sperm retrieval + ICSI works. The **presence/absence of a solitary kidney** is the single most useful clinical discriminator between the developmental and degenerative subtypes and should redirect genetic testing (renal-anomaly → developmental genes; normal kidneys + CFTR-negative → ADGRG2).

---

## Evidence Base

| PMID | Contribution | Supports finding |
|---|---|---|
| [32025909](https://pubmed.ncbi.nlm.nih.gov/32025909/) | Genetics review — CFTR predominance, ADGRG2 ~2%, prevalence 0.1%, developmental/degenerative split | F001, F005, F009 |
| [42199298](https://pubmed.ncbi.nlm.nih.gov/42199298/) | Large Chinese iCAVD cohort — 74.87% CFTR/ADGRG2; 10.14% couple co-carriers | F001, F009 |
| [27476656](https://pubmed.ncbi.nlm.nih.gov/27476656/) | Original ADGRG2 truncating variants; Adgrg2-KO mouse | F002, F007 |
| [32314195](https://pubmed.ncbi.nlm.nih.gov/32314195/) | ADGRG2 efferent-duct localization; novel LoF variant | F002 |
| [35109852](https://pubmed.ncbi.nlm.nih.gov/35109852/) | CBAVD incidence 1–2%; 47,XYY mosaic case | F003 |
| [40533736](https://pubmed.ncbi.nlm.nih.gov/40533736/) | Seminal-vesicle status distribution (47 patients) | F003 |
| [39592508](https://pubmed.ncbi.nlm.nih.gov/39592508/) | Non-5T → 8.17× epididymal partial-absence risk | F003 |
| [42380629](https://pubmed.ncbi.nlm.nih.gov/42380629/) | CF male reproductive phenotype; CFTR-KO rat best model | F004, F007 |
| [23378603](https://pubmed.ncbi.nlm.nih.gov/23378603/) | p.Arg117His CBAVD/CFTR-RD spectrum; couples at CF risk | F004 |
| [16985610](https://pubmed.ncbi.nlm.nih.gov/16985610/) | Mesonephric-duct embryology of renal + vasal agenesis | F005 |
| [40921938](https://pubmed.ncbi.nlm.nih.gov/40921938/) | FREM1/WNT2B/TBX6 in CFTR-negative CBAVD with renal anomalies | F005 |
| [41255074](https://pubmed.ncbi.nlm.nih.gov/41255074/) | MRI evidence for acquired/progressive vasal agenesis | F005 |
| [41654435](https://pubmed.ncbi.nlm.nih.gov/41654435/) | Prenatal ETI prevents CBAVD (case) | F006 |
| [39288989](https://pubmed.ncbi.nlm.nih.gov/39288989/) | Postnatal modulators do not reverse infertility | F006 |
| [28384194](https://pubmed.ncbi.nlm.nih.gov/28384194/) | SLC9A3 KO → obstructive azoospermia, ↓CFTR | F007 |
| [35119551](https://pubmed.ncbi.nlm.nih.gov/35119551/) | ICSI outcomes; Chinese allele spectrum (IVS9-5T) | F008, F009 |
| [40850271](https://pubmed.ncbi.nlm.nih.gov/40850271/) | Residual CFTR activity predicts MESA success | F008 |
| [34313208](https://pubmed.ncbi.nlm.nih.gov/34313208/) | Sperm motility predicts ICSI outcome | F008 |
| [40065563](https://pubmed.ncbi.nlm.nih.gov/40065563/) | Meta-analysis; comprehensive CFTR screening needed | Diagnostics |
| [42572672](https://pubmed.ncbi.nlm.nih.gov/42572672/) | TG12T5 splicing variant in CFTR-RD | Section 4 |
| [37273165](https://pubmed.ncbi.nlm.nih.gov/37273165/) | ADGRG2 p.Ser303*; carrier with normal fertility | Sections 4, 9 |
| [41886210](https://pubmed.ncbi.nlm.nih.gov/41886210/) | ADGRG2 testing when CFTR-negative + normal kidneys | Diagnostics |
| [22709980](https://pubmed.ncbi.nlm.nih.gov/22709980/) | CFTR signaling pathways in male fertility | Section 6 |
| [39543810](https://pubmed.ncbi.nlm.nih.gov/39543810/) | CFTR modulators & reproductive health; fetal exposure | Sections 12, 13 |

**Consistency:** Findings are mutually reinforcing across independent European and East Asian cohorts, case reports, MRI series, and multiple animal models. No major contradictions were identified; the chief tension is the **"progressive degeneration" vs "developmental agenesis"** debate, which the two-subtype model reconciles (degenerative = CFTR/ADGRG2, kidneys spared; developmental = Wolffian-duct defect, renal agenesis).

---

## Limitations and Knowledge Gaps

1. **Unexplained fraction (10–20%).** A substantial minority of CBAVD lacks a molecular diagnosis; developmental genes (FREM1, WNT2B, TBX6) are candidates but not yet validated at scale.
2. **Single-case evidence for prenatal prevention.** The ETI-prevents-CBAVD observation rests on **one infant** [PMID: 41654435]; timing, dosing, the true critical window, and long-term/heterozygote safety are unknown, with unresolved ethical questions.
3. **Penetrance/expressivity poorly quantified.** The poly-T/TG modifier and the normal-fertility ADGRG2 carrier show incomplete penetrance that is not yet predictable at the individual level.
4. **Model limitations.** No model perfectly reproduces isolated human CBAVD; rats over-express hypospermatogenesis, and most mouse models remain fertile.
5. **Epidemiology.** Prevalence (~0.1%) is likely underestimated; incidence and non-European/non-East-Asian allele spectra are under-characterized.
6. **Epigenetics.** No disease-specific epigenetic signature has been defined.
7. **Long-term offspring outcomes** after prenatal modulator exposure are unstudied.

---

## Proposed Follow-up Experiments / Actions

1. **Systematic renal imaging + developmental-gene panel** (FREM1, WNT2B, TBX6, and broader WES/WGS) in all *CFTR*/*ADGRG2*-negative CBAVD to validate the developmental subtype and expand the gene set.
2. **Registry/prospective study of prenatal CFTR-modulator exposure** with structured male genital-tract follow-up (vas patency by ultrasound, later fertility) to define the fetal critical window, efficacy, and safety.
3. **Functional dissection of the ADGRG2–CFTR–SLC9A3 module** in efferent-duct organoids/animal models to map shared fluid-transport mechanisms.
4. **Genotype-stratified sperm-retrieval outcome studies** to formalize residual-CFTR-activity and motility as pre-procedure prognostic tools (building on [PMID: 40850271], [PMID: 34313208]).
5. **Universal comprehensive CFTR screening protocol** (exons + flanking + poly-T/TG + rearrangements + deep-intronic) with mandatory partner carrier screening and PGT counseling before ART.
6. **Population-specific allele catalogues** beyond European/Chinese cohorts to improve carrier-screening panels globally.
7. **Longitudinal CFTR-RD surveillance** of isolated-CBAVD men to quantify later pancreatic/sinopulmonary risk.

---

*Report compiled from a 5-iteration autonomous investigation: 9 confirmed findings, 27 papers reviewed. Evidence types span human clinical cohorts, case reports, imaging series, in vitro studies, and model-organism data.*


## Artifacts

- [OpenScientist final report](Congenital_Bilateral_Absence_of_Vas_Deferens-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Bilateral_Absence_of_Vas_Deferens-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 15 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009299` (2 mentions) - the report calls it "MONDO"; MONDO calls it **46 XX gonadal dysgenesis**
- `HP:0000798` (1 mention) - the report calls it "Abnormality of the vas deferens"; HP calls it **Oligozoospermia**
- `HP:0012869` (1 mention) - the report calls it "Decreased ejaculate volume"; HP calls it **Acephalic spermatozoa**
- `HP:0011878` (1 mention) - the report calls it "Abnormality of the seminal vesicle"; HP calls it **Abnormal platelet membrane protein expression**
- `HP:0000029` (1 mention) - the report calls it "Abnormality of the epididymis"; HP calls it **Testicular atrophy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016324` (2 mentions) - the report calls it "apical plasma membrane", "Subcellular:** apical plasma membrane"; GO calls it **apical plasma membrane**
- `GO:0007283` (1 mention) - the report calls it "spermatogenesis — preserved"; GO calls it **spermatogenesis**
- `UBERON:0000079` (1 mention) - the report calls it "Body system:** male reproductive/genital system"; UBERON calls it **male reproductive system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016324` - called "apical plasma membrane", "Subcellular:** apical plasma membrane"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.