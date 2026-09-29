---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T14:13:16.623671'
end_time: '2026-09-04T14:26:51.054376'
duration_seconds: 814.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: "Peroxisome biogenesis disorder 2B, PBD2B, OMIM 202370 \u2014 the\
    \ non-classic, milder end of the PEX5-related Zellweger spectrum, historically\
    \ called neonatal adrenoleukodystrophy or infantile Refsum disease. Caused by\
    \ biallelic hypomorphic variants in PEX5, which encodes the cytosolic PTS1 peroxisomal\
    \ matrix protein import receptor. This is complementation group 2, gene PEX5 -\
    \ not PEX1, not PEX2."
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 62
  verified: 58
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - Sign; congenital/infantile; variable, sometimes followed by spasticity; impairs
      feeding and motor milestones
    ontology_label: Hypotonia
  - term_id: HP:0001263
    reported_labels:
    - Sign; infancy/childhood; mild to severe and variably progressive
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - Neurobehavioral; variable; cognition can be relatively preserved in mild disease
    ontology_label: Intellectual disability
  - term_id: HP:0000407
    reported_labels:
    - Sign; often infancy/early childhood; usually bilateral and slowly progressive/stable
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0002415
    reported_labels:
    - MRI/pathology; childhood to adult; stable or progressive/regressive
    ontology_label: Leukodystrophy
  - term_id: HP:0000824
    reported_labels:
    - Endocrine/laboratory; may emerge progressively
    ontology_label: Decreased response to growth hormone stimulation test
  - term_id: HP:0006297
    reported_labels:
    - Dental sign; secondary dentition
    ontology_label: Enamel hypoplasia
  - term_id: HP:0001999
    reported_labels:
    - Physical manifestation; congenital, generally mild in PBD2B
    ontology_label: Abnormal facial shape
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0061912
    ontology_label: obsolete selective autophagy
  unresolvable_prefixes:
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peroxisome_Biogenesis_Disorder_2B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome biogenesis disorder 2B, PBD2B, OMIM 202370 — the non-classic, milder end of the PEX5-related Zellweger spectrum, historically called neonatal adrenoleukodystrophy or infantile Refsum disease. Caused by biallelic hypomorphic variants in PEX5, which encodes the cytosolic PTS1 peroxisomal matrix protein import receptor. This is complementation group 2, gene PEX5 - not PEX1, not PEX2.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome biogenesis disorder 2B, PBD2B, OMIM 202370 — the non-classic, milder end of the PEX5-related Zellweger spectrum, historically called neonatal adrenoleukodystrophy or infantile Refsum disease. Caused by biallelic hypomorphic variants in PEX5, which encodes the cytosolic PTS1 peroxisomal matrix protein import receptor. This is complementation group 2, gene PEX5 - not PEX1, not PEX2.** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome biogenesis disorder 2B, PBD2B, OMIM 202370 — the non-classic, milder end of the PEX5-related Zellweger spectrum, historically called neonatal adrenoleukodystrophy or infantile Refsum disease. Caused by biallelic hypomorphic variants in PEX5, which encodes the cytosolic PTS1 peroxisomal matrix protein import receptor. This is complementation group 2, gene PEX5 - not PEX1, not PEX2.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome biogenesis disorder 2B, PBD2B, OMIM 202370 — the non-classic, milder end of the PEX5-related Zellweger spectrum, historically called neonatal adrenoleukodystrophy or infantile Refsum disease. Caused by biallelic hypomorphic variants in PEX5, which encodes the cytosolic PTS1 peroxisomal matrix protein import receptor. This is complementation group 2, gene PEX5 - not PEX1, not PEX2.** covering all of the
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


# Peroxisome biogenesis disorder 2B (PBD2B; OMIM 202370)

## Scope and evidence standard

This report concerns **biallelic PEX5-related, non-classic Zellweger spectrum disorder (ZSD), complementation group 2**—not PEX1- or PEX2-related disease. The historical labels *neonatal adrenoleukodystrophy* (NALD) and *infantile Refsum disease* (IRD) describe intermediate and milder portions of a continuous phenotype and are no longer regarded as cleanly separable diseases. A major limitation is that PEX5 disease is exceptionally rare: most modern natural-history studies combine all ZSD genes or predominantly study PEX1. Accordingly, claims below are labeled **PEX5-specific human**, **general ZSD**, or **model/in-vitro inference**.

The following table summarizes the principal conclusions.

| Domain | PEX5/PBD2B-specific conclusion | Evidence scope/caveat |
|---|---|---|
| Identity | **Peroxisome biogenesis disorder 2B (PBD2B; OMIM 202370)** denotes the non-classic, milder end of **PEX5-related Zellweger spectrum disorder (ZSD)**; historical labels include neonatal adrenoleukodystrophy and infantile Refsum disease. It belongs to **complementation group 2** (Japanese group F), not PEX1- or PEX2-related disease. (moser1998moleculargeneticsof pages 2-4, rosewich2015clinicalutilitygene pages 1-2) | Historical phenotype labels overlap and are now generally treated as a severity continuum rather than discrete disorders. A dedicated MONDO term for PBD2B was not verified; broader ZSD is MONDO:0019609. (OpenTargets Search: Zellweger spectrum disorder-PEX5) |
| Gene/protein | **PEX5** (12p13.31; OMIM *600414; ENSG00000139197) encodes the cytosolic receptor/chaperone for proteins bearing a C-terminal peroxisomal targeting signal type 1 (PTS1). PEX5L also supports PTS2 import through PEX7. (OpenTargets Search: Zellweger spectrum disorder-PEX5, rosewich2015clinicalutilitygene pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 5-7) | This is specifically a PEX5 disorder; PEX1 and PEX2 encode different components of peroxisome biogenesis. |
| Inheritance | Autosomal recessive: disease results from **biallelic germline PEX5 variants**; PBD2B is expected to reflect hypomorphic alleles retaining partial receptor/import activity. (moser1998moleculargeneticsof pages 2-4, rosewich2015clinicalutilitygene pages 1-2) | Penetrance is expected to be high for pathogenic biallelic genotypes, but PEX5-specific estimates, modifier genes, founder effects, and carrier frequencies are unavailable. A reported 2025 homozygous stop-loss/frameshift allele remained an ACMG VUS without functional validation. (bernalbonilla2025detectionofa pages 2-4) |
| Core mechanism | Reduced PEX5 function impairs PTS1-cargo recognition, docking at PEX13/PEX14, matrix translocation, or receptor recycling after Cys11 monoubiquitination and PEX1–PEX6–PEX26-mediated extraction; this reduces peroxisomal matrix-enzyme activity and perturbs lipid and redox metabolism. (constantin2024theroleof pages 10-16, fujiki2020recentinsightsinto pages 2-3, argyriou2016peroxisomebiogenesisdisorders pages 5-7, pandey2024molecularinteractionsof pages 16-20) | Import failure is well established; the relative contribution of individual metabolites, mitochondrial dysfunction, oxidative stress, inflammation, and pexophagy to each human phenotype remains partly inferred from cells and models. |
| Biochemical signature | Expected ZSD profile: elevated plasma C26:0/C26:1 and C24:0/C22:0 or C26:0/C22:0 ratios, phytanic/pristanic acids, pipecolic acid, and C27 bile-acid intermediates (DHCA/THCA), with reduced erythrocyte plasmalogens; fibroblasts show impaired matrix-protein import. (rosewich2015clinicalutilitygene pages 1-2, braverman2016peroxisomebiogenesisdisorders pages 3-4, klouwer2015zellwegerspectrumdisorders pages 8-9) | Results vary with age, diet, residual function, and tissue; mild disease may yield borderline or normal plasma results. These are general ZSD biomarkers, not validated PEX5-specific prognostic surrogates. |
| Mild-spectrum phenotypes | Typical features include infantile/childhood hypotonia and developmental delay, sensorineural hearing loss, progressive retinal dystrophy or visual loss, liver dysfunction, enamel hypoplasia, ataxia, peripheral neuropathy, spasticity, and stable or progressive leukodystrophy; renal stones/hyperoxaluria and adrenal insufficiency may emerge. (rosewich2015clinicalutilitygene pages 1-2, klouwer2015zellwegerspectrumdisorders pages 8-9, argyriou2016peroxisomebiogenesisdisorders pages 9-10) | PEX5-isolated frequencies are unavailable. General ZSD ophthalmic cohorts found abnormal ERGs in about 93%, macular cysts/schisis in 16/21 milder patients, and slow visual-acuity decline of approximately 0.01 LogMAR/year, but these cohorts were not PEX5-specific. (yergeau2022peroxisomebiogenesisdisorders pages 1-4) |
| Diagnosis | Confirm a compatible phenotype with a **multianalyte peroxisomal biochemical profile**, followed by a PEX/ZSD gene panel, exome, or genome sequencing demonstrating two clinically significant **PEX5** alleles in trans. Use fibroblast PTS1-import/localization and metabolic assays when biochemical or variant findings are equivocal. (rosewich2015clinicalutilitygene pages 1-2, braverman2016peroxisomebiogenesisdisorders pages 3-4) | Single-marker VLCFA testing can miss mild PEX disorders. CMA, karyotyping, FISH, mitochondrial-DNA, and repeat-expansion testing are not first-line unless another diagnosis is suspected. |
| Treatment | No approved curative or **PEX5-targeted disease-modifying therapy** exists. Management is multidisciplinary and supportive: nutrition/gastrostomy when needed, antiseizure medication, hearing aids or cochlear implants, visual aids, physical/occupational/speech therapy, fat-soluble vitamins when deficient, adrenal replacement, vitamin K for coagulopathy, and renal-stone prevention. (klouwer2015zellwegerspectrumdisorders pages 8-9, braverman2016peroxisomebiogenesisdisorders pages 20-20) | Evidence is based mainly on expert guidance and general ZSD practice; controlled PEX5-specific response rates and pharmacogenomic guidance are absent. |
| Prognosis | Hypomorphic PEX5 disease is expected to permit survival through childhood and potentially adulthood, with chronic sensory, neurologic, hepatic, and renal morbidity; leukodystrophy may remain stable or progress. (yergeau2022peroxisomebiogenesisdisorders pages 1-4, argyriou2016peroxisomebiogenesisdisorders pages 9-10) | No PEX5/PBD2B survival curve, median life expectancy, or validated prognostic biomarker exists. Severe-ZSD mortality within 1–2 years should not be directly applied to PBD2B. |
| Epidemiology | PBD2B is ultra-rare; no reliable PEX5-specific incidence, prevalence, sex ratio, ethnic distribution, or carrier-frequency estimate was identified. Both sexes should be affected equally under autosomal-recessive inheritance. | Published ZSD-wide or PEX1-specific estimates cannot be assigned to PEX5. Historical evidence identified only very small numbers of complementation-group-2 patients. (moser1998moleculargeneticsof pages 2-4, malone2025estimationofpex1mediated pages 1-2) |
| Models/trials | Pex5-null and conditional mice reproduce absent matrix import, mitochondrial/ER abnormalities, neuronal-migration delay, dysmyelination, axonal degeneration, neuroinflammation, motor/cognitive impairment, and early death; CRISPR pex5 zebrafish show reduced import, hepatic lipid accumulation, demyelination, edema, impaired movement, and reduced survival. (jiang2025modellingperoxisomaldisorders pages 8-9) | Null models resemble severe ZSD more than hypomorphic PBD2B. General ZSD studies include natural-history and retinal cohorts, while betaine and hydroxychloroquine trials targeted PEX1 or PEX1/PEX6/PEX26—not PEX5—and have not established disease-modifying efficacy. (NCT01668186 chunk 1, NCT01838941 chunk 1, NCT06190626 chunk 1, NCT03856866 chunk 1) |


*Table: Compact evidence summary distinguishing PEX5-specific conclusions from broader Zellweger-spectrum extrapolation. It highlights the scarcity of PEX5-isolated quantitative data and absence of a PEX5-targeted disease-modifying therapy.*

## 1. Disease information

### Definition

PBD2B is an autosomal-recessive Mendelian disorder caused by biallelic, usually hypomorphic, variants in **PEX5**, encoding the cytosolic receptor for peroxisomal targeting signal type 1 (PTS1)-bearing matrix proteins. Residual PEX5-dependent import distinguishes the non-classic phenotype from severe PEX5-related Zellweger syndrome, although the boundary is biological rather than categorical. Historical complementation analysis assigned PEX5 deficiency to US **complementation group 2**; an early review reported only two group-2 patients, illustrating the evidence scarcity. ZS, NALD, and IRD were already recognized as a severity continuum, with IRD least severe and NALD intermediate. (moser1998moleculargeneticsof pages 2-4, rosewich2015clinicalutilitygene pages 1-2)

### Identifiers and synonyms

- **Disease OMIM:** 202370, *Peroxisome biogenesis disorder 2B*.
- **Gene:** PEX5; **OMIM gene:** *600414; chromosome **12p13.31**; Ensembl **ENSG00000139197**; approved name *peroxisomal biogenesis factor 5*. (OpenTargets Search: Zellweger spectrum disorder-PEX5, rosewich2015clinicalutilitygene pages 1-2)
- **MONDO:** no PBD2B-specific MONDO identifier was verified in the retrieved evidence. Use broader **MONDO:0019609, Zellweger spectrum disorders**, with PEX5/genotype qualification; **MONDO:0019234** denotes peroxisome biogenesis disorder. (OpenTargets Search: Zellweger spectrum disorder-PEX5)
- **Orphanet:** broader PBD-ZSD is **Orphanet:79189**; Zellweger syndrome is Orphanet:912. A PEX5/PBD2B-specific Orphanet code was not verified. (OpenTargets Search: Zellweger spectrum disorder-PEX5)
- **Common names:** PBD2B; PEX5-related ZSD; PEX5 deficiency; peroxisome biogenesis disorder, complementation group 2; historically NALD and IRD.
- **ICD/MeSH:** ICD systems generally classify this under broader peroxisomal disorders/Zellweger syndrome rather than a unique PEX5 code. A specific ICD-10/11 or MeSH identifier for PBD2B was not established by the retrieved literature.

The evidence is principally aggregated disease-level literature, small case series, cultured fibroblasts, and model organisms—not EHR-derived individual-level population data.

## 2. Etiology, risk, and protective factors

### Causal factor

The necessary cause is **biallelic germline PEX5 dysfunction**. Hypomorphic alleles retain enough PTS1 import to produce the milder PBD2B phenotype; two severe loss-of-function alleles would be expected to move the phenotype toward classic neonatal Zellweger syndrome. This is a receptor/import defect, not an isolated enzyme deficiency. PEX5’s causal association with ZSD is supported by human genetic evidence and curated disease-target resources. (OpenTargets Search: Zellweger spectrum disorder-PEX5, rosewich2015clinicalutilitygene pages 1-2)

### Genetic risk

Risk is highest for offspring of two heterozygous carriers: for each conception, the theoretical risks are 25% affected, 50% carrier, and 25% unaffected/non-carrier. Consanguinity or endogamy increases the probability that both parents carry the same rare allele. No validated susceptibility loci, modifier genes, protective alleles, polygenic score, or PEX5-specific founder allele were identified.

A 1999 primary report described functional heterogeneity in PEX5-defective patients and identified **p.Asn489Lys (N489K)** in an IRD patient (PMID **10462504**, published August 1999; DOI: https://doi.org/10.1006/bbrc.1999.1232). The available excerpt did not provide a complete modern transcript-level genotype, population frequency, or ACMG classification; it should therefore not be entered as a fully resolved pathogenic genotype without checking the original sequence table.

A 2025 report identified homozygous **NM_001131025.2:c.1897_1900dupACTA, p.(Met634Asnfs*16)** in two affected siblings from an endogamous family. Both parents were heterozygous; the variant was absent from reviewed population/literature resources, but remained an **ACMG VUS** (PM4, PM2, PP1) and lacked a PTS1-import functional assay. It should not be represented as definitively pathogenic. (bernalbonilla2025detectionofa pages 2-4)

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, smoking behavior, alcohol exposure, occupation, sex, or lifestyle factor causes PBD2B. Diet can modify measured phytanic/pristanic acid and may modify metabolite burden, but does not prevent the genetic disorder. Age and diet also influence biochemical test sensitivity. No proven environmental or genetic protective factor prevents disease in a person with a pathogenic biallelic genotype. (braverman2016peroxisomebiogenesisdisorders pages 3-4, klouwer2015zellwegerspectrumdisorders pages 8-9)

**Gene–environment interaction:** residual import capacity is primary; dietary phytanic-acid exposure and physiologic stress may alter downstream metabolite burden or complications. This is clinically plausible/general ZSD evidence, not a quantified PEX5-specific interaction.

## 3. Phenotypes

PEX5-isolated frequencies do not exist. The following phenotype annotations represent the expected non-classic ZSD phenotype, supported by historical PEX5 cases and broader ZSD cohorts.

| Phenotype | Type, onset, course, impact | Suggested HPO term |
|---|---|---|
| Hypotonia | Sign; congenital/infantile; variable, sometimes followed by spasticity; impairs feeding and motor milestones | HP:0001252 |
| Global developmental delay | Sign; infancy/childhood; mild to severe and variably progressive | HP:0001263 |
| Intellectual disability | Neurobehavioral; variable; cognition can be relatively preserved in mild disease | HP:0001249 |
| Seizures/epilepsy | Symptom/sign; neonatal through childhood; episodic, variable severity | HP:0001250 / HP:0001251 |
| Sensorineural hearing loss | Sign; often infancy/early childhood; usually bilateral and slowly progressive/stable | HP:0000407 |
| Retinal dystrophy/retinitis-pigmentosa-like disease | Sign; infancy onward; progressive night blindness, field and acuity loss | HP:0000556 / HP:0000510 |
| Nystagmus/visual impairment | Sign; infancy; persistent | HP:0000639 / HP:0000505 |
| Leukodystrophy/demyelination | MRI/pathology; childhood to adult; stable or progressive/regressive | HP:0002415 |
| Ataxia, spasticity, neuropathy | Neurologic signs; commonly later childhood/adulthood; progressive | HP:0001251, HP:0001257, HP:0009830 |
| Hepatomegaly/liver dysfunction | Sign/laboratory; infancy onward; may improve, persist, or progress to fibrosis/cirrhosis | HP:0002240 / HP:0002910 |
| Failure to thrive/feeding difficulty | Symptom/sign; infancy; variable | HP:0001508 / HP:0011968 |
| Renal cortical cysts, hyperoxaluria/nephrolithiasis | Imaging/laboratory; variable, sometimes later | HP:0000107 / HP:0003073 / HP:0000787 |
| Adrenal insufficiency | Endocrine/laboratory; may emerge progressively | HP:0000824 |
| Enamel hypoplasia | Dental sign; secondary dentition | HP:0006297 |
| Dysmorphic facial features | Physical manifestation; congenital, generally mild in PBD2B | HP:0001999 |

Historical severe-ZSD figures—hypotonia 99%, hearing impairment 100%, hepatomegaly 100%, retinopathy 71%, seizures 80%, renal cysts 93%, and neuronal-migration defects 67%—must **not** be assigned as PBD2B frequencies; they came from predominantly severe, mixed-gene disease. (moser1998moleculargeneticsof pages 2-4)

More relevant but still non-PEX5-specific intermediate/mild ophthalmic data show mean visual-acuity decline of approximately **+0.01 LogMAR/year**, legal blindness beginning at mean age **7.8 years**, abnormal ERGs in **93%**, and macular cysts/schisis in **16/21** milder patients. Another analysis estimated median blindness at 3.8 years in intermediate disease and 7.3 years in mild disease. These data support a substantial effect on mobility, communication, education, and independence, but no PEX5-specific EQ-5D, SF-36, PROMIS, or validated patient-reported outcome has been published. (yergeau2022peroxisomebiogenesisdisorders pages 1-4, yergeau2022peroxisomebiogenesisdisorders pages 22-24)

A 42-patient mixed PBD-ZSD/D-bifunctional-protein cohort, comprising 300 audiograms, found that most hearing loss was moderately severe to severe, usually changed slowly, and improved functionally with amplification; again, it was not a PEX5 subgroup.

## 4. Genetic and molecular information

### Gene and protein

**PEX5** encodes two principal splice isoforms, PEX5S and PEX5L. The C-terminal tetratricopeptide-repeat domain recognizes the C-terminal PTS1 motif, commonly **-Ser-Lys-Leu (-SKL)** or a conservative variant. The N-terminal region acts as a cargo chaperone/holdase and contains interaction motifs for the docking and export machinery. PEX5L additionally acts with PEX7 in PTS2 import. (argyriou2016peroxisomebiogenesisdisorders pages 5-7, pandey2024molecularinteractionsof pages 16-20)

Suggested annotations include HGNC **HGNC:9719**; GO molecular functions **peroxisomal targeting sequence binding** and **protein transporter/chaperone activity**; GO biological processes **protein import into peroxisome matrix (GO:0016558)** and **peroxisome organization (GO:0007031)**.

### Variant spectrum and interpretation

Disease alleles may be missense, nonsense, frameshift, splice-altering, stop-loss, or larger copy-number variants. PBD2B specifically requires enough residual PEX5 function to avoid complete neonatal disease; therefore, at least one hypomorphic allele is biologically expected, but a validated allele-by-allele PEX5 severity catalogue was not recovered. Variants are germline, not somatic. The mechanism is partial loss of function, not gain of function or dominant negative action.

Population frequencies must be checked in the current gnomAD release by exact transcript/HGVS. No reliable PEX5 carrier-frequency estimate was found. Neither chromosomal rearrangements nor recurrent aneuploidy characterize PBD2B. No disease-specific methylation, histone, or chromatin signature and no validated epigenetic modifier are known.

## 5. Environmental information

Environmental toxins, ionizing radiation, pollution, occupational exposure, infectious agents, smoking, and alcohol are not established etiologies or triggers. Nutritional state affects clinical resilience and some biomarker concentrations. Phytanic acid derives largely from dietary ruminant fat/dairy and can be restricted if elevated, but evidence that restriction changes long-term PBD2B neurologic outcome is weak. Infection and fasting can precipitate decompensation in many metabolic diseases, but a PEX5-specific risk estimate is unavailable. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic PEX5 variants lead to** reduced amount or function of cytosolic PEX5 receptor.
2. **Reduced PEX5 function leads to** impaired binding/chaperoning of PTS1 cargo, impaired docking to PEX13/PEX14, impaired transient-pore translocation, and/or defective receptor recycling.
3. **Import-cycle failure leads to** cytosolic mislocalization and reduced matrix activity of multiple PTS1 enzymes; the exact step affected is allele dependent and often not demonstrated clinically. (constantin2024theroleof pages 10-16, fujiki2020recentinsightsinto pages 2-3, argyriou2016peroxisomebiogenesisdisorders pages 5-7, pandey2024molecularinteractionsof pages 16-20)
4. **Multienzyme deficiency leads to** impaired VLCFA and dicarboxylic-fatty-acid β-oxidation, disturbed branched-chain fatty-acid and bile-acid metabolism, impaired ether-lipid/plasmalogen synthesis indirectly through organelle dysfunction, and altered peroxide/redox handling. (argyriou2016peroxisomebiogenesisdisorders pages 3-5)
5. **These metabolic defects lead to** accumulation of VLCFAs, phytanic/pristanic acids and C27 bile-acid intermediates, reduced plasmalogens, and altered pipecolate/glyoxylate handling.
6. **Lipid and redox disequilibrium leads to** membrane/myelin abnormalities, hepatocellular and retinal stress, mitochondrial/ER dysfunction, and altered inter-organelle signaling; the relative contribution of each metabolite is incompletely resolved.
7. **Branch A—developing nervous system:** abnormal lipid supply and cellular homeostasis **lead to** impaired neuronal migration and neurodevelopment, producing hypotonia, developmental delay, epilepsy, and cortical abnormalities.
8. **Branch B—white matter:** oligodendrocyte/myelin and axonal dysfunction, with early innate immune activation **leads to** dysmyelination, leukodystrophy, axonal degeneration, ataxia, neuropathy, and spasticity; much of this chain is model-derived.
9. **Branch C—retina/cochlea:** long-lived sensory-cell membrane and metabolic stress **leads to** retinal dystrophy and sensorineural hearing loss.
10. **Branch D—liver/kidney/adrenal:** toxic bile-acid/lipid and oxalate disturbances **lead to** hepatopathy, nephrolithiasis/cysts, and adrenal dysfunction.
11. **Residual import in hypomorphic disease leads to** slower, organ-selective, chronic progression rather than uniformly lethal neonatal multisystem failure.

### Import-cycle detail and recent research

Cargo-bound PEX5 docks at the PEX13/PEX14 translocation module. After cargo release, PEX5 is monoubiquitinated at **Cys11** by the PEX2/PEX10/PEX12 RING complex and extracted by the ATP-dependent PEX1–PEX6 AAA complex anchored by PEX26. A 2024 mechanistic study stated: **“PEX5, the peroxisomal protein shuttling receptor, binds newly synthesized proteins in the cytosol and transports them to the organelle.”** It showed that reversible cysteine ubiquitination prevents inappropriate PEX5 polyubiquitination and translocon obstruction (published March 2024; DOI: https://doi.org/10.1371/journal.pbio.3002567). This clarifies receptor quality control but is not a PBD2B treatment study. (constantin2024theroleof pages 10-16, fujiki2020recentinsightsinto pages 2-3, pandey2024molecularinteractionsof pages 16-20)

A 2024 Nature Communications study showed that PEX13’s SH3 domain dynamically recognizes PEX5 WxxxF/Y motifs, refining the docking mechanism (published April 2024; DOI: https://doi.org/10.1038/s41467-024-47605-w). A 2024 genome-wide CRISPRi study linked RNF146/tankyrase-dependent PARylation at PEX14 to import efficiency and Wnt/β-catenin signaling (published July 2024; DOI: https://doi.org/10.1083/jcb.202312069). These results suggest developmental signaling consequences of peroxisome dysfunction, but a direct causal role in human PEX5-PBD2B remains unproven.

Pexophagy may amplify loss of functional organelles when ubiquitinated PEX5 accumulates. However, this mechanism is strongest for receptor-export defects such as PEX1/PEX6/PEX26, not necessarily primary hypomorphic PEX5 deficiency. A 2023 study found that loss of PEX13 caused ubiquitinated PEX5 and ROS to cooperate in inducing pexophagy (published January 2023; DOI: https://doi.org/10.1080/15548627.2022.2160566). It is mechanistically relevant but should not be treated as direct PEX5 patient evidence.

### Cells, pathways, and ontology suggestions

- **Cells:** neuron (CL:0000540), oligodendrocyte (CL:0000128), astrocyte (CL:0000127), microglial cell (CL:0000129), hepatocyte (CL:0000182), retinal photoreceptor cell (CL:0000210), retinal pigment epithelial cell (CL:0002586), inner-ear sensory hair cell (CL:0000202), adrenal cortical cell, and renal tubular epithelial cell.
- **Processes:** GO:0016558 protein import into peroxisome matrix; GO:0007031 peroxisome organization; GO:0006635 fatty-acid β-oxidation; GO:0035336 long-chain-fatty-acid metabolism; GO:0046485 ether-lipid metabolism; GO:0006979 response to oxidative stress; GO:0061912 selective autophagy; GO:0042552 myelination; GO:0008366 axon ensheathment.
- **Compartments:** peroxisome GO:0005777; peroxisomal matrix GO:0005782; peroxisomal membrane GO:0005778; cytosol GO:0005829; mitochondrion GO:0005739; endoplasmic reticulum GO:0005783.

No PEX5-specific single-cell, spatial-transcriptomic, patient proteomic, or integrated multi-omic disease atlas was identified. Cell-type-specific lipid abnormalities have been demonstrated in mixed-gene ZSD iPSC derivatives, so fibroblast biomarkers cannot be assumed to reflect neural or hepatic metabolism.

## 7. Anatomical structures affected

Primary systems are nervous, sensory, hepatic, renal, endocrine, skeletal, and dental. Suggested UBERON annotations include brain **UBERON:0000955**, cerebral cortex **UBERON:0000956**, cerebral white matter **UBERON:0002437**, cerebellum **UBERON:0002037**, retina **UBERON:0000966**, cochlea **UBERON:0001844**, liver **UBERON:0002107**, kidney **UBERON:0002113**, adrenal gland **UBERON:0002369**, peripheral nerve **UBERON:0001021**, and tooth **UBERON:0001091**. Disease is usually bilateral/systemic rather than lateralized. Asymmetric cortical malformation has been reported in an individual PEX5 family, but it is not a defining pattern. (bernalbonilla2025detectionofa pages 2-4)

At the tissue level, white-matter myelin and axons, cortical developmental zones, photoreceptor/RPE layers, cochlear sensory pathways, hepatocytes, renal tubules, and adrenal cortex are implicated. At the subcellular level, the initiating compartment is the peroxisomal matrix-import apparatus; secondary mitochondrial, ER, lysosomal/autophagic, and cytosolic abnormalities may follow.

## 8. Temporal development

Non-classic disease usually begins congenitally or in infancy with hypotonia, feeding/growth difficulty, hearing loss, nystagmus/visual dysfunction, or developmental delay. Ataxia, neuropathy, spasticity, retinal degeneration, leukodystrophy, adrenal insufficiency, and nephrolithiasis may become prominent later. Leukodystrophy can be stable for years or progress at any age. (argyriou2016peroxisomebiogenesisdisorders pages 9-10)

The course is chronic and lifelong, not relapsing-remitting. Residual PEX5 function can permit survival into childhood or adulthood, but no PEX5-specific staging system, progression rate, median survival, remission pattern, or critical therapeutic window has been validated. Developmental periods and the interval before irreversible retinal/white-matter injury are rational intervention windows, but this remains inferential.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Both sexes are expected to be affected equally. Penetrance should be high for genuinely pathogenic biallelic genotypes, while expressivity is variable and related largely to residual import. Anticipation is not expected. Germline mosaicism has not been established as a characteristic feature, although a small residual recurrence risk can never be excluded after an apparently de novo event.

No reliable PEX5/PBD2B prevalence, incidence, carrier frequency, geographic distribution, sex ratio, or population-specific variant distribution is available. Historical identification of only two complementation-group-2 patients confirms extreme rarity but is not an epidemiologic denominator. PEX1-specific modeling and general ZSD birth estimates must not be assigned to PEX5. (moser1998moleculargeneticsof pages 2-4, malone2025estimationofpex1mediated pages 1-2)

## 10. Diagnostics

### Recommended workflow

1. **Clinical suspicion:** infantile hearing/visual impairment, hypotonia or developmental delay with liver disease, leukodystrophy, neuropathy/ataxia, adrenal dysfunction, renal stones, or enamel hypoplasia.
2. **First-line biochemical panel:** fasting plasma VLCFAs—C26:0, C26:1, C24:0/C22:0, C26:0/C22:0—plus phytanic and pristanic acids; erythrocyte plasmalogens; plasma/urine pipecolic acid; and C27 bile-acid intermediates DHCA and THCA. Multiple assays are preferred because VLCFA alone can miss mild PEX disease. (rosewich2015clinicalutilitygene pages 1-2, braverman2016peroxisomebiogenesisdisorders pages 3-4)
3. **Molecular confirmation:** a comprehensive PEX/ZSD/peroxisomal-disorder panel with deletion/duplication calling, or exome/genome sequencing, demonstrating two clinically significant PEX5 variants in trans.
4. **Functional clarification:** cultured fibroblast PTS1-reporter/catalase localization, anti-catalase immunofluorescence, VLCFA oxidation, plasmalogen synthesis, and complementation studies when biochemical results or variants are equivocal. (rosewich2015clinicalutilitygene pages 1-2)
5. **Baseline organ assessment:** liver enzymes, bilirubin, coagulation and fat-soluble vitamins; ACTH/cortisol; renal function and urine oxalate; ophthalmology including OCT/ERG where useful; audiology; neurologic/developmental assessment; brain MRI; dental and bone assessment. (braverman2016peroxisomebiogenesisdisorders pages 20-20)

**Interpretive caution:** biomarker concentrations may diminish with age and correlate poorly with clinical severity, so they are diagnostic/supportive markers rather than validated prognostic or treatment surrogate endpoints. (klouwer2015zellwegerspectrumdisorders pages 8-9)

### Imaging and functional tests

Brain MRI may show leukodystrophy, cortical malformation, perisylvian/polymicrogyric change, or cerebellar-region white-matter disease; mild patients may have normal MRI. OCT can detect intraretinal schisis/cysts and atrophy. ERG is commonly abnormal or extinguished, but may be too insensitive to longitudinal functional change; visual acuity, fields, mobility, and functional-vision questionnaires are complementary. EEG is indicated for seizures; nerve-conduction studies for neuropathy; ABR/audiometry for hearing loss. (yergeau2022peroxisomebiogenesisdisorders pages 22-24, yergeau2022peroxisomebiogenesisdisorders pages 4-6)

### Differential diagnosis

Important alternatives are severe PEX5-Zellweger syndrome; other PEX-gene ZSDs; D-bifunctional protein deficiency (**HSD17B4**); acyl-CoA oxidase-1 deficiency (**ACOX1**); X-linked adrenoleukodystrophy (**ABCD1**); adult Refsum disease (**PHYH/PEX7**); rhizomelic chondrodysplasia punctata; isolated hereditary retinal/hearing disorders; mitochondrial disease; and other leukodystrophies. Approximately 10–15% of patients evaluated for elevated VLCFAs may have a single-enzyme defect rather than ZSD. (braverman2016peroxisomebiogenesisdisorders pages 3-4)

CMA may detect an unusual exon/gene deletion but is not first-line for sequence-level PEX5 disease. Karyotype, FISH, mtDNA analysis, and repeat-expansion assays are not routinely indicated. RNA sequencing can clarify suspected splice variants; untargeted metabolomics/proteomics remain adjunct research methods.

### Screening

Population newborn screening is not uniformly established for ZSD; C26:0-lysophosphatidylcholine-based screening used for X-ALD may identify some ZSD cases but can miss mild disease. Cascade testing of relatives and targeted carrier testing are appropriate after familial variants are known. Prenatal diagnosis and PGT-M are technically available.

## 11. Outcome and prognosis

PBD2B generally has a better prognosis than classic neonatal Zellweger syndrome, with survival into later childhood and potentially adulthood. Nevertheless, morbidity may be substantial from deafness, progressive retinal degeneration, motor disability, epilepsy, leukodystrophy, neuropathy, liver disease, adrenal insufficiency, and renal stones. Recovery of established neurodevelopmental or retinal injury is unlikely under current supportive care.

No PEX5-specific 5- or 10-year survival rate, median life expectancy, mortality rate, or validated prognostic model exists. Severe-ZSD survival of only 1–2 years should not be applied directly to PBD2B. General mild-ZSD evidence supports slow visual deterioration and possible adult survival, but much of it comes from PEX1 p.Gly843Asp cohorts. (yergeau2022peroxisomebiogenesisdisorders pages 1-4, yergeau2022peroxisomebiogenesisdisorders pages 12-15)

Likely prognostic factors are residual import activity, genotype class, congenital brain malformation, early liver/coagulation disease, feeding/respiratory compromise, and onset/progression of leukodystrophy. Plasma VLCFA concentration alone is not a reliable severity predictor. Quality-of-life burden extends to caregivers: a completed 2018 survey enrolled **92** caregivers and measured symptoms, parental stress, and family quality of life, but no PEX5 subgroup result was available. (klouwer2015zellwegerspectrumdisorders pages 8-9, NCT03440905 chunk 1)

## 12. Treatment and current applications

### Current standard of care

There is no approved curative or PEX5-directed disease-modifying therapy. Real-world management is multidisciplinary and complication-directed:

- nutritional assessment, feeding therapy, calorie supplementation, and gastrostomy where required;
- antiseizure medication selected by seizure type;
- hearing aids or cochlear implantation, communication support, and annual audiology;
- glasses, low-vision services, cataract management where indicated, and annual ophthalmology/OCT;
- physical, occupational, and speech therapy; mobility/orthotic support;
- vitamin K for deficiency/coagulopathy and replacement of deficient fat-soluble vitamins;
- glucocorticoid replacement for confirmed adrenal insufficiency and emergency stress-dose planning;
- fluids and citrate for hyperoxaluria/nephrolithiasis as clinically indicated;
- surveillance and specialist management of liver disease, bone health, and enamel hypoplasia. (klouwer2015zellwegerspectrumdisorders pages 8-9, braverman2016peroxisomebiogenesisdisorders pages 20-20)

Suggested NCIt intervention concepts include **Supportive Care (C15747)**, physical therapy, occupational therapy, speech therapy, gastrostomy, hearing aid, cochlear implant, anticonvulsant therapy, glucocorticoid replacement, vitamin supplementation, and genetic counseling. Exact NCIt identifiers should be verified against the current release before database ingestion.

### Dietary and pharmacologic approaches

Phytanic-acid restriction may lower substrate exposure when phytanic acid is elevated, but it is not curative and has no demonstrated PEX5-specific neurologic response rate. Cholic acid and other bile-acid strategies have been investigated in ZSD, but effectiveness and hepatotoxicity require specialist oversight; no PEX5-specific efficacy evidence was recovered. Liver transplantation has been reported in only two general-ZSD children with biochemical improvement and uncertain long-term multisystem benefit. (klouwer2015zellwegerspectrumdisorders pages 8-9)

### Trials and experimental therapy

- **NCT01838941**, oral betaine: completed open-label single-group pilot, 12 children, March 2013–June 2015. It targeted misfolded **PEX1-p.Gly843Asp**, not PEX5; primary endpoint was six-month plasma C26/C22 change. No PEX5 subgroup or usable efficacy/adverse-event result was found. https://clinicaltrials.gov/study/NCT01838941 (NCT01838941 chunk 1)
- **NCT03856866 (HARP)**, hydroxychloroquine 4 mg/kg/day: completed randomized quadruple-masked N-of-1 crossover series, **3** participants, 2019–2020; eligibility was restricted to PEX1, PEX6, or PEX26 disease. No PEX5 participant was specified. https://clinicaltrials.gov/study/NCT03856866 (NCT03856866 chunk 1)
- Subsequent cell work found that chloroquine/hydroxychloroquine worsened rather than restored PEX1-G843D peroxisomal functions, arguing against routine autophagy inhibition; this is not direct PEX5 evidence.
- **NCT01668186**, recruiting longitudinal PBD natural history: target **244**, annual follow-up for up to 10 years, estimated completion 2031; no PEX5 subgroup results yet. https://clinicaltrials.gov/study/NCT01668186 (NCT01668186 chunk 1)
- **NCT06190626**, recruiting prospective retinal natural history: target **30**, begun December 18, 2023, five-year ophthalmic follow-up; no PEX5 subgroup specified. https://clinicaltrials.gov/study/NCT06190626 (NCT06190626 chunk 1)

Gene replacement/editing, RNA therapy, and cell therapy remain preclinical concepts. Multisystem expression, developmental onset, and the need to reach brain, retina, liver, and other tissues make delivery difficult. Retinal gene therapy may be the most anatomically tractable application, but no PEX5 clinical efficacy data exist.

## 13. Prevention

Primary lifestyle prevention is impossible because PBD2B is inherited. Effective reproductive prevention options are genetic counseling, partner/carrier testing in an identified family, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and PGT-M. Secondary prevention consists of early biochemical/genetic diagnosis, cascade testing, and prompt surveillance for treatable complications. Tertiary prevention includes seizure control, hearing amplification, low-vision intervention, nutrition support, adrenal-crisis prevention, vitamin/coagulation management, renal-stone prevention, rehabilitation, and vaccination according to routine schedules. No disease-specific vaccine, antimicrobial prophylaxis, or environmental public-health measure applies.

## 14. Other species and natural disease

No well-established naturally occurring companion-animal PEX5/PBD2B syndrome, breed predisposition, or veterinary prevalence was identified. PEX5 is evolutionarily conserved across eukaryotes, and orthologous import-cycle function is studied in yeast, flies, fish, and mice. This is inherited cellular disease, not infection; there is no zoonotic transmission or cross-species contagion.

Suggested taxa are **Homo sapiens** NCBI Taxon 9606, **Mus musculus** 10090, **Danio rerio** 7955, **Drosophila melanogaster** 7227, and **Saccharomyces cerevisiae** 4932. Current NCBI ortholog Gene IDs and any VBO breed terms should be verified programmatically before ingestion.

## 15. Model organisms

### Mouse

Global **Pex5-null mice** model severe Zellweger syndrome rather than PBD2B: they exhibit absent matrix import, neuronal-migration abnormalities, hepatic disease, secondary mitochondrial changes, hypotonia, and early death. Conditional Nestin-Pex5 deletion isolates neural peroxisome deficiency and produces progressive motor/coordination and cognitive impairment, dysmyelination, axonal degeneration, lipid accumulation, astrogliosis/microgliosis, and death before six months. Neural innate-immune activation occurs early and precedes overt demyelination, supporting inflammation as a downstream amplifier rather than the initiating lesion. These null models overstate the severity expected from hypomorphic PBD2B.

### Zebrafish

CRISPR/Cas9 **pex5 knockout zebrafish** show reduced matrix-protein import and peroxisome abundance, altered motor activity, hepatic lipid accumulation, demyelination, edema, deflated swim bladder, small liver, and reduced survival. They are useful for developmental imaging and drug screening but again represent near-complete deficiency, not a validated human PBD2B allele. (jiang2025modellingperoxisomaldisorders pages 8-9)

### Cellular systems

Patient fibroblasts remain the most directly useful functional system for PTS1 import, catalase localization, VLCFA oxidation, plasmalogen synthesis, complementation, temperature sensitivity, and variant rescue. GFP-PTS1 reporters permit live/high-content screening. ZSD iPSCs differentiated into neurons, neural progenitors, oligodendrocyte precursors, and hepatocyte-like cells demonstrate cell-type-dependent lipid abnormalities and impaired assembly, but retrieved lines carried PEX1, PEX10, PEX12, or PEX26—not PEX5—so their relevance is pathway-level.

Drosophila and yeast are valuable for conserved import machinery and genetic interaction screens, but they incompletely model human brain, retina, hearing, bile-acid metabolism, and chronic multisystem natural history.

## Evidence-weighted conclusions

1. **High confidence:** PBD2B is autosomal-recessive PEX5/complementation-group-2 disease; PEX5 is the PTS1 receptor, and reduced matrix import is the initiating defect. (OpenTargets Search: Zellweger spectrum disorder-PEX5, rosewich2015clinicalutilitygene pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 5-7)
2. **Moderate confidence:** residual import explains the milder, chronic phenotype involving hearing, retina, nervous system, liver, kidney, adrenal gland, and dentition; direct PEX5 cohorts remain too small for reliable frequencies.
3. **High confidence:** diagnosis should combine a multianalyte peroxisomal biochemical profile with biallelic PEX5 molecular confirmation and fibroblast functional testing when needed. (rosewich2015clinicalutilitygene pages 1-2, braverman2016peroxisomebiogenesisdisorders pages 3-4)
4. **High confidence:** current care is supportive; no PEX5-specific disease-modifying therapy or clinical trial has established efficacy. (klouwer2015zellwegerspectrumdisorders pages 8-9, NCT01838941 chunk 1, NCT03856866 chunk 1)
5. **Major knowledge gaps:** PEX5-specific prevalence, carrier frequency, penetrance estimates, validated genotype–phenotype map, prospective natural history, patient-reported quality of life, biomarkers of progression, hypomorphic knock-in models, and PEX5-targeted therapeutic studies.

### Selected authoritative references

- Shimozawa N, et al. *Functional heterogeneity of C-terminal peroxisome targeting signal 1 in PEX5-defective patients.* **Biochem Biophys Res Commun.** Published August 1999. PMID: **10462504**. https://doi.org/10.1006/bbrc.1999.1232
- Klouwer FCC, et al. *Zellweger spectrum disorders: clinical overview and management approach.* **Orphanet J Rare Dis.** Published December 2015. https://doi.org/10.1186/s13023-015-0368-9 (klouwer2015zellwegerspectrumdisorders pages 8-9)
- Braverman NE, et al. *Peroxisome biogenesis disorders in the Zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines.* **Mol Genet Metab.** Published March 2016. https://doi.org/10.1016/j.ymgme.2015.12.009 (braverman2016peroxisomebiogenesisdisorders pages 3-4)
- Yergeau C, et al. *Peroxisome Biogenesis Disorders in the Zellweger Spectrum: Ophthalmic Findings…* Preprint posted November 7, 2022. https://doi.org/10.1101/2022.11.06.22279732 (yergeau2022peroxisomebiogenesisdisorders pages 1-4)
- Francisco T, et al. *Noncanonical and reversible cysteine ubiquitination prevents the overubiquitination of PEX5 at the peroxisomal membrane.* **PLoS Biol.** Published March 2024. https://doi.org/10.1371/journal.pbio.3002567
- Gaussmann S, et al. *Modulation of peroxisomal import by the PEX13 SH3 domain and a proximal FxxxF binding motif.* **Nat Commun.** Published April 2024. https://doi.org/10.1038/s41467-024-47605-w
- Jiang CS, Schrader M. *Modelling Peroxisomal Disorders in Zebrafish.* **Cells.** Published January 2025. https://doi.org/10.3390/cells14020147 (jiang2025modellingperoxisomaldisorders pages 8-9)

**Abstract-supported quotations:** the 2015 clinical review states, **“There is currently no curative therapy, but supportive care is available.”** The 2024 peroxisome review describes peroxisomes as organelles with key functions in fatty-acid β-oxidation, myelin-lipid synthesis, and cellular redox balance. These authoritative summaries accurately frame current care and mechanism, but neither supplies PEX5-specific treatment-response statistics.

References

1. (moser1998moleculargeneticsof pages 2-4): Hugo W. Moser. Molecular genetics of peroxisomal disorders. Frontiers in bioscience : a journal and virtual library, 5:D298-306, Nov 1998. URL: https://doi.org/10.1080/15513819809168801, doi:10.1080/15513819809168801. This article has 52 citations.

2. (rosewich2015clinicalutilitygene pages 1-2): Hendrik Rosewich, Hans Waterham, Bwee Tien Poll-The, Andreas Ohlenbusch, and Jutta Gärtner. Clinical utility gene card for: zellweger syndrome spectrum. European Journal of Human Genetics, 23(8):1111-1111, Nov 2015. URL: https://doi.org/10.1038/ejhg.2014.250, doi:10.1038/ejhg.2014.250. This article has 10 citations and is from a domain leading peer-reviewed journal.

3. (OpenTargets Search: Zellweger spectrum disorder-PEX5): Open Targets Query (Zellweger spectrum disorder-PEX5, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (argyriou2016peroxisomebiogenesisdisorders pages 5-7): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

5. (bernalbonilla2025detectionofa pages 2-4): Ingrid Bernal-Bonilla, Juan Arias-Florez, Sandra Ximena Ramírez, Bibiana Bayona-Gomez, Lina Castro-Castillo, Valeria Correa-Martinez, Yasmín Sánchez-Gómez, Natalia Santiago-Tovar, C. Gaviria-Sabogal, Nora Constanza Contreras Bravo, R. Cabrera, Adrien Morel, D. Fonseca-Mendoza, and C. Restrepo. Detection of a novel homozygous pex5 stop-loss variant associated with zellweger syndrome in a highly endogamic family. Sep 2025. URL: https://doi.org/10.2147/tacg.s518636, doi:10.2147/tacg.s518636. This article has 1 citations.

6. (constantin2024theroleof pages 10-16): Constantin Mouzaaber. The role of peroxins 1 and 6 in the retinal pigment epithelium. Text, 2024. URL: https://doi.org/10.7939/r3-v6ev-1s49, doi:10.7939/r3-v6ev-1s49. This article has 0 citations and is from a peer-reviewed journal.

7. (fujiki2020recentinsightsinto pages 2-3): Yukio Fujiki, Yuichi Abe, Yuuta Imoto, Akemi J. Tanaka, Kanji Okumoto, Masanori Honsho, Shigehiko Tamura, Non Miyata, Toshihide Yamashita, Wendy K. Chung, and Tsuneyoshi Kuroiwa. Recent insights into peroxisome biogenesis and associated diseases. Journal of Cell Science, May 2020. URL: https://doi.org/10.1242/jcs.236943, doi:10.1242/jcs.236943. This article has 95 citations and is from a domain leading peer-reviewed journal.

8. (pandey2024molecularinteractionsof pages 16-20): Saroj Pandey. Molecular interactions of the human pex1/pex6 aaa+ atpase complex and in vivo mrna editing of the pex1-g843d mutation. May 2024. URL: https://doi.org/10.15496/publikation-94953, doi:10.15496/publikation-94953. This article has 0 citations.

9. (braverman2016peroxisomebiogenesisdisorders pages 3-4): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 352 citations and is from a peer-reviewed journal.

10. (klouwer2015zellwegerspectrumdisorders pages 8-9): Femke C. C. Klouwer, Kevin Berendse, Sacha Ferdinandusse, Ronald J. A. Wanders, Marc Engelen, and Bwee Tien Poll-The. Zellweger spectrum disorders: clinical overview and management approach. Orphanet Journal of Rare Diseases, Dec 2015. URL: https://doi.org/10.1186/s13023-015-0368-9, doi:10.1186/s13023-015-0368-9. This article has 300 citations and is from a peer-reviewed journal.

11. (argyriou2016peroxisomebiogenesisdisorders pages 9-10): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

12. (yergeau2022peroxisomebiogenesisdisorders pages 1-4): Christine Yergeau, Razek Georges Coussa, Fares Antaki, Catherine Argyriou, Robert K. Koenekoop, and Nancy E. Braverman. Peroxisome biogenesis disorders in the zellweger spectrum: ophthalmic findings from a new natural history study cohort and scoping literature review. MedRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.06.22279732, doi:10.1101/2022.11.06.22279732. This article has 2 citations.

13. (braverman2016peroxisomebiogenesisdisorders pages 20-20): Nancy E. Braverman, Gerald V. Raymond, William B. Rizzo, Ann B. Moser, Mark E. Wilkinson, Edwin M. Stone, Steven J. Steinberg, Michael F. Wangler, Eric T. Rush, Joseph G. Hacia, and Mousumi Bose. Peroxisome biogenesis disorders in the zellweger spectrum: an overview of current diagnosis, clinical manifestations, and treatment guidelines. Molecular genetics and metabolism, 117 3:313-21, Mar 2016. URL: https://doi.org/10.1016/j.ymgme.2015.12.009, doi:10.1016/j.ymgme.2015.12.009. This article has 352 citations and is from a peer-reviewed journal.

14. (malone2025estimationofpex1mediated pages 1-2): Karen E. Malone, Catherine Argyriou, Evelyn Zavacky, and Nancy Braverman. Estimation of pex1-mediated zellweger spectrum disorder births and population prevalence by population genetics modeling. Genetics in Medicine Open, 3:103431, Apr 2025. URL: https://doi.org/10.1016/j.gimo.2025.103431, doi:10.1016/j.gimo.2025.103431. This article has 4 citations and is from a peer-reviewed journal.

15. (jiang2025modellingperoxisomaldisorders pages 8-9): Chenxing S. Jiang and Michael Schrader. Modelling peroxisomal disorders in zebrafish. Jan 2025. URL: https://doi.org/10.3390/cells14020147, doi:10.3390/cells14020147. This article has 4 citations.

16. (NCT01668186 chunk 1): Nancy Braverman. Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD). McGill University Health Centre/Research Institute of the McGill University Health Centre. 2012. ClinicalTrials.gov Identifier: NCT01668186

17. (NCT01838941 chunk 1): Nancy Braverman. Betaine and Peroxisome Biogenesis Disorders. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2013. ClinicalTrials.gov Identifier: NCT01838941

18. (NCT06190626 chunk 1): Nancy Braverman. Longitudinal Prospective Natural History Study of Retinopathy in Zellweger Spectrum Disorder. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2023. ClinicalTrials.gov Identifier: NCT06190626

19. (NCT03856866 chunk 1): Neal Sondheimer. Hydroxychloroquine Administration for Reduction of Pexophagy. The Hospital for Sick Children. 2019. ClinicalTrials.gov Identifier: NCT03856866

20. (yergeau2022peroxisomebiogenesisdisorders pages 22-24): Christine Yergeau, Razek Georges Coussa, Fares Antaki, Catherine Argyriou, Robert K. Koenekoop, and Nancy E. Braverman. Peroxisome biogenesis disorders in the zellweger spectrum: ophthalmic findings from a new natural history study cohort and scoping literature review. MedRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.06.22279732, doi:10.1101/2022.11.06.22279732. This article has 2 citations.

21. (argyriou2016peroxisomebiogenesisdisorders pages 3-5): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

22. (yergeau2022peroxisomebiogenesisdisorders pages 4-6): Christine Yergeau, Razek Georges Coussa, Fares Antaki, Catherine Argyriou, Robert K. Koenekoop, and Nancy E. Braverman. Peroxisome biogenesis disorders in the zellweger spectrum: ophthalmic findings from a new natural history study cohort and scoping literature review. MedRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.06.22279732, doi:10.1101/2022.11.06.22279732. This article has 2 citations.

23. (yergeau2022peroxisomebiogenesisdisorders pages 12-15): Christine Yergeau, Razek Georges Coussa, Fares Antaki, Catherine Argyriou, Robert K. Koenekoop, and Nancy E. Braverman. Peroxisome biogenesis disorders in the zellweger spectrum: ophthalmic findings from a new natural history study cohort and scoping literature review. MedRxiv, Nov 2022. URL: https://doi.org/10.1101/2022.11.06.22279732, doi:10.1101/2022.11.06.22279732. This article has 2 citations.

24. (NCT03440905 chunk 1):  Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders. University of South Florida. 2018. ClinicalTrials.gov Identifier: NCT03440905

## Artifacts

- [Edison artifact artifact-00](Peroxisome_Biogenesis_Disorder_2B-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 62 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (1 mention) - the report calls it "Sign; congenital/infantile; variable, sometimes followed by spasticity; impairs feeding and motor milestones"; HP calls it **Hypotonia**
- `HP:0001263` (1 mention) - the report calls it "Sign; infancy/childhood; mild to severe and variably progressive"; HP calls it **Global developmental delay**
- `HP:0001249` (1 mention) - the report calls it "Neurobehavioral; variable; cognition can be relatively preserved in mild disease"; HP calls it **Intellectual disability**
- `HP:0000407` (1 mention) - the report calls it "Sign; often infancy/early childhood; usually bilateral and slowly progressive/stable"; HP calls it **Sensorineural hearing impairment**
- `HP:0002415` (1 mention) - the report calls it "MRI/pathology; childhood to adult; stable or progressive/regressive"; HP calls it **Leukodystrophy**
- `HP:0000824` (1 mention) - the report calls it "Endocrine/laboratory; may emerge progressively"; HP calls it **Decreased response to growth hormone stimulation test**
- `HP:0006297` (1 mention) - the report calls it "Dental sign; secondary dentition"; HP calls it **Enamel hypoplasia**
- `HP:0001999` (1 mention) - the report calls it "Physical manifestation; congenital, generally mild in PBD2B"; HP calls it **Abnormal facial shape**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0061912` (obsolete selective autophagy) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000540` (1 mention) - the report calls it "Cells:** neuron"; CL calls it **neuron**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`.