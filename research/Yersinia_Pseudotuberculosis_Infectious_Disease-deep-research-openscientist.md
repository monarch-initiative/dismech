---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T15:09:25.230713'
end_time: '2026-09-27T15:24:40.394133'
duration_seconds: 915.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Yersinia Pseudotuberculosis Infectious Disease
  mondo_id: MONDO:0007024
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
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 10
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 37
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 7
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Very common
    ontology_label: Fever
  - term_id: HP:0002014
    reported_labels:
    - Common
    ontology_label: Diarrhea
  - term_id: HP:0004299
    reported_labels:
    - Common (children)
    ontology_label: Hernia of the abdominal wall
  - term_id: HP:0000988
    reported_labels:
    - Far Eastern strains
    ontology_label: Skin rash
  - term_id: HP:0012219
    reported_labels:
    - ~3% (Yersinia sequela est.)
    ontology_label: Erythema nodosum
  - term_id: HP:0000083
    reported_labels:
    - Systemic cases
    ontology_label: Renal insufficiency
  - term_id: UBERON:0003454
    reported_labels:
    - Peyer's patches / gut-associated lymphoid tissue
    ontology_label: small intestine Peyer's patch
  - term_id: NCIT:C540
    reported_labels:
    - ciprofloxacin
    ontology_label: Heparan Sulfate
  - term_id: NCIT:C1737
    reported_labels:
    - ceftriaxone, cefotaxime
    ontology_label: Organic Solvents
  - term_id: NCIT:C61796
    reported_labels:
    - gentamicin, enrofloxacin (vet)
    ontology_label: Ivermectin
  - term_id: NCIT:C692
    reported_labels:
    - doxycycline, oxytetracycline
    ontology_label: Nimodipine
  - term_id: NCIT:C287
    reported_labels:
    - trimethoprim-sulfamethoxazole
    ontology_label: Aspirin
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Yersinia_Pseudotuberculosis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Yersinia_Pseudotuberculosis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Yersinia Pseudotuberculosis Infectious Disease
- **MONDO ID:** MONDO:0007024 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Yersinia Pseudotuberculosis Infectious Disease** covering all of the
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

# Yersinia pseudotuberculosis Infectious Disease — Comprehensive Disease-Characteristics Report

**MONDO ID:** MONDO:0007024 | **Category:** Infectious Disease | **Causative agent:** *Yersinia pseudotuberculosis* (NCBI:txid633)

**Evidence base:** Aggregated disease-level literature (PubMed reviews, primary microbiology/immunology studies, human clinical case series, model-organism experiments). No individual patient/EHR data or omics files were provided; all statements are literature-derived and cited by PMID.

---

## Summary

*Yersinia pseudotuberculosis* infectious disease is an acute, zoonotic, foodborne enteric infection caused by the cold-tolerant (psychrotrophic) Gram-negative coccobacillus *Y. pseudotuberculosis*. The pathogen is acquired fecal-orally from contaminated water, produce, or meat, and it uniquely proliferates under refrigeration, which shapes both its epidemiology and its prevention. The disease shows a striking **geographic dichotomy**: in Europe and most of the world it manifests as a self-limiting gastroenteritis or, in children, as fever with mesenteric lymphadenitis and terminal ileitis that mimics acute appendicitis ("pseudoappendicitis"). In Russia and Japan, by contrast, epidemic strains cause a severe systemic inflammatory disease historically called **Far East scarlet-like fever (FESLF)**, characterized by scarlatiniform rash, arthralgia, and toxic-shock-like features.

The pathophysiology is bacterial-effector driven, not host-genetic. The organism enters through M cells over the Peyer's patches using the chromosomal adhesin **invasin** (a high-affinity β1-integrin ligand), replicates in the intestine, and then disseminates to mesenteric lymph nodes, liver, and spleen. A **temperature-regulated type III secretion system (T3SS)** encoded on the pYV virulence plasmid — switched on at 37 °C by the master regulator **LcrF** — injects **Yop effector proteins** that paralyze phagocytes and disable innate immune signaling (NF-κB, MAPK, IRF3). The severe FESLF phenotype is additionally determined by strain plasmid/superantigen content: the **pVM82 plasmid** and the superantigen **YPMa (Y. pseudotuberculosis-derived mitogen A)**, which overstimulates CD4⁺ Vβ3/Vβ7/Vβ8 T cells to release a TNF-α/IFN-γ cytokine storm.

The disease is generally self-limiting with an excellent prognosis, and the organism is broadly antibiotic-susceptible (fluoroquinolones, third-generation cephalosporins, aminoglycosides, tetracyclines). Severe systemic and septicemic disease is concentrated in hosts with **iron overload, desferrioxamine therapy, or immunosuppression**. Post-infectious immune sequelae — reactive arthritis and erythema nodosum — occur in a minority. Notably, *Y. pseudotuberculosis* is the recent enteric evolutionary ancestor of *Y. pestis* (plague). Prevention rests on food and water hygiene; no human vaccine exists. This report synthesizes 12 confirmed findings from 46 reviewed papers across all 15 requested disease-characteristic domains.

---

## 1. Disease Information

**Overview.** *Yersinia pseudotuberculosis* infectious disease (yersiniosis due to *Y. pseudotuberculosis*) is an acute enteric zoonosis. Clinically it presents along a spectrum from self-limiting gastroenteritis to pseudoappendicitis (mesenteric adenitis/terminal ileitis) to, in the Far East, a severe systemic scarlet-fever-like illness. It is caused by a Gram-negative, facultatively anaerobic, motile (at ≤30 °C), psychrotrophic member of the family *Yersiniaceae*.

**Key identifiers:**
- **MONDO:** MONDO:0007024
- **MeSH:** *Yersinia pseudotuberculosis Infections*
- **ICD-10:** A28.2 (Extraintestinal yersiniosis) / A04.8 (other bacterial intestinal infections)
- **Pathogen taxonomy:** NCBI:txid633 (*Yersinia pseudotuberculosis*)
- OMIM/Orphanet: not a Mendelian disorder; no OMIM entry (infectious, not genetic). Orphanet lists Far East scarlet-like fever as a rare condition.

**Synonyms / alternative names:** Far East scarlet-like fever (FESLF); Izumi fever (historical Japanese name); pseudotuberculosis; Pasteurella pseudotuberculosis infection (historical bacterial name); scarlatinoid fever.

**Information source type.** The evidence base is **aggregated disease-level literature** (case series, outbreak investigations, microbiology and animal-model studies, and serosurveys) rather than individual EHR-derived cohorts. Much quantitative sequelae data are extrapolated from the closely related *Y. enterocolitica*.

The two-faced clinical identity is the anchoring finding (**F001**):

> *"Far East scarlet-like fever is caused by Yersinia pseudotubuclosis infection, an organism that typically causes self-limiting gastroenteritis in Europe."* — Amphlett 2016, [PMID: 26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/)

> *"Geographical heterogeneity exists between virulence factors produced by European and Far Eastern Y pseudotuberculosis strains, implicating superantigen Y pseudotuberculosis-derived mitogen A (YPMa) in the pathogenesis of FESLF."* — [PMID: 26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/)

---

## 2. Etiology

**Primary cause.** The disease is **infectious**, caused entirely by *Y. pseudotuberculosis*. There is no genetic (Mendelian) etiology in the human host. Disease severity is governed by **pathogen genotype** (plasmid and superantigen content) interacting with **host iron status and immune competence**.

**Environmental / exposure risk factors:**
- **Foodborne/waterborne transmission** via contaminated refrigerated food, raw vegetables (lettuce, carrots), untreated water, and meat (**F012**).
- **Animal contact** — broad wildlife and domestic-animal reservoirs (**F008**).
- **Age** — children are disproportionately affected by the pseudoappendicitis form.
- **Cold storage** — the organism's psychrotrophic growth increases the infectious dose reachable in refrigerated foods.

**Host risk factors for severe/systemic disease (F010):**
- **Iron overload** (e.g., β-thalassemia, hemochromatosis).
- **Desferrioxamine (DFO) iron-chelation therapy** — DFO acts as a xenosiderophore delivering iron to the bacterium.
- **Immunosuppression and splenectomy.**

> *"Patients undergoing DFO therapy are at risk for Y. enterocolitica infection which may be localized to mesenteric nodes and tonsils or occur as a generalized form such as septicemia."* — Wanachiwanawin 2000, [PMID: 11132234](https://pubmed.ncbi.nlm.nih.gov/11132234/)

**Genetic protective / risk factors:** None established in humans. Susceptibility is essentially universal; outcome modulation is by iron availability and immune status rather than host germline variants.

**Gene–environment interaction.** The key "interaction" is **host iron availability × bacterial iron acquisition**: excess free iron (from overload or DFO chelation therapy) supports rapid bacterial growth and systemic dissemination, converting a normally contained enteric infection into septicemia.

---

## 3. Phenotypes

| Phenotype | Type | Characteristics | Frequency | Suggested HPO |
|---|---|---|---|---|
| Fever | Symptom | Acute onset; prominent in FESLF | Very common | HP:0001945 |
| Abdominal pain (RLQ) / pseudoappendicitis | Sign/symptom | Mesenteric adenitis, terminal ileitis; children 5–14 y | Common in children | HP:0002027, HP:0002605 |
| Diarrhea / gastroenteritis | Symptom | Self-limiting (Europe) | Common | HP:0002014 |
| Mesenteric lymphadenitis | Clinical sign | Mimics appendicitis | Common (children) | HP:0004299 |
| Scarlatiniform rash | Physical manifestation | FESLF hallmark | Far Eastern strains | HP:0000988 |
| Arthralgia / reactive arthritis | Sign; post-infectious | Weeks after infection | ~12% (Yersinia sequela est.) | HP:0002829, HP:0001369 |
| Erythema nodosum | Physical; post-infectious | Panniculitis, self-limiting | ~3% (Yersinia sequela est.) | HP:0012219 |
| Transient renal dysfunction | Lab/clinical | Systemic FESLF; correlates with anti-YPM | Systemic cases | HP:0000083 |
| Toxic-shock-like features | Clinical | Superantigen-driven | Severe FESLF | HP:0032169 |

Phenotype spectrum evidence (**F006**):

> *"responsible for scarlatinoid fever, food poisoning, post-infectious complications like erythema nodosum/reactive arthritis as well as pseudoappendicitis in children"* — Basharat 2021, [PMID: 33321204](https://pubmed.ncbi.nlm.nih.gov/33321204/)

Reactive-arthritis frequency (extrapolated from *Y. enterocolitica* population study, **F006**):

> *"Self-reported symptoms consistent with ReA were reported by 12% of yersiniosis patients compared to 5% in a reference group not exposed to yersiniosis."* — Rosner 2013, [PMID: 23701958](https://pubmed.ncbi.nlm.nih.gov/23701958/)

**Onset/severity/progression:** acute onset; self-limiting in most; systemic FESLF is more severe and correlates with higher anti-YPM titers. **Quality of life:** acute illness is generally short-lived; the main QoL burden falls on the minority with reactive arthritis (weeks–months of joint pain).

---

## 4. Genetic/Molecular Information

**This is an infectious disease; there are no human causal genes, pathogenic germline variants, chromosomal abnormalities, or Mendelian inheritance.** The "genetics" of the disease are the genetics of the **pathogen**.

**Key bacterial virulence loci:**
- **pYV / pCD1 virulence plasmid (~70 kb):** encodes the **Ysc T3SS** and **Yop effectors** (YopH, YopE, YopT, YopJ/YopP, YopM, YopO/YpkA) plus the master regulator **LcrF (VirF)**.
- **Chromosomal *inv* gene:** invasin, the β1-integrin adhesin for M-cell entry.
- ***ail*, *yadA*** (plasmid): adhesion/serum resistance.
- **YPMa gene (*ypmA*):** superantigen; hallmark of Far Eastern strains.
- **pVM82 plasmid (~82 MDa):** present only in FESLF-causing strains (**F011**).

Strain plasmid genotype determines clinical severity (**F011**):

> *"effects of pathogenicity of an understudied pVM82 plasmid present only in Y pseudotuberculosis sttains causing clinical-epidemic manifestation of the infections as Far East scarlet-like fever (FESLF)"* — Somova 2016, [PMID: 30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/)

> *"Variability of damage of innate immunity cells and target-organs caused by various plasmid types of Y pseudotuberculosis by virulence could determine polymorphism of clinical-morphological manifestations of this infection."* — [PMID: 30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/)

**Serotypes:** ≥21 O-serotypes exist; *Y. pestis* evolved from serotype **O:1b** (**F005**).

---

## 5. Environmental Information

**Infectious agent (NCBI Taxon):** *Yersinia pseudotuberculosis*, NCBI:txid633.

**Environmental/transmission factors:**
- **Cold tolerance (psychrotrophy):** enables growth in refrigerated foods (**F012**).

> *"Yersinia enterocolitica and Yersinia pseudotuberculosis are important foodborne pathogens that cause infections through contaminated refrigerated food."* — Palonen 2010, [PMID: 20088683](https://pubmed.ncbi.nlm.nih.gov/20088683/)

- **Food vehicles:** raw vegetables, lettuce, carrots, untreated water, meat.
- **Animal reservoirs:** pigs, sheep, wild birds, rodents, deer, and many others; food/livestock strains are molecularly indistinguishable from human isolates (**F008**).

> *"All human Y. pseudotuberculosis 1/O:1 strains were indistinguishable from pig, sheep or food strains."* — Okwori 2009, [PMID: 19835774](https://pubmed.ncbi.nlm.nih.gov/19835774/)

**Lifestyle factors:** consumption of raw/undercooked produce and unpasteurized/untreated water; exposure to farm and wild animals.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

```
1.  Ingestion of contaminated refrigerated food/water
        → delivers viable Y. pseudotuberculosis to the small intestine
2.  Chromosomal invasin binds host β1-integrins on M cells (Peyer's patches)
        → results in translocation across the follicle-associated epithelium
3.  Invasin–β1-integrin engagement activates Rac1, MAP kinases, NF-κB
        → drives local chemokine production and bacterial uptake
4.  Bacteria replicate in the intestinal lumen/lamina propria
        → establishes a replicating pool (required for later dissemination)
5.  Host body temperature (37 °C) is sensed by an RNA thermometer + YmoA
        → de-represses the master regulator LcrF
6.  LcrF activates the pYV-encoded Ysc T3SS and yop genes
        → injects Yop effectors into phagocytes on contact
7a. YopH/YopE/YopT/YopO disrupt phagocyte cytoskeleton/Rho GTPases
        → results in resistance to phagocytosis (antiphagocytic defense)
7b. YopJ acetylates/deubiquitinates TAK1 and reduces K63-ubiquitination
    of TRAF3/TRAF6
        → blocks NF-κB, MAPK, and IRF3 signaling
        → suppresses innate cytokine and interferon responses
8.  Surviving extracellular bacteria disseminate to mesenteric lymph
    nodes, liver, spleen
        → mesenteric lymphadenitis / pseudoappendicitis / abscessation

        ┌──────────────── BRANCH: strain genotype ────────────────┐
        │ European strains          │ Far Eastern strains          │
        │ (YPMa-/pVM82-)             │ (YPMa+, pVM82+)              │
        │  → localized, self-limiting│  → superantigen released     │
        │    gastroenteritis /       │                              │
        │    pseudoappendicitis      │                              │
        └────────────────────────────┴──────────────────────────────┘
9.  (Far East) YPMa superantigen cross-links MHC-II to TCR Vβ3/Vβ7/Vβ8
        → massive polyclonal CD4+ T-cell activation
10. Activated T cells release TNF-α and IFN-γ
        → systemic inflammation, rash, renal dysfunction, toxic shock (FESLF)
11. (Post-infectious, in a minority) molecular mimicry / immune complexes
        → reactive arthritis and erythema nodosum weeks after infection
```

### Detail by category

**Molecular pathways.** Host invasin signaling engages **Rac1 → MAPK → NF-κB**. Bacterial YopJ targets the **NF-κB, MAPK, and IRF3** pathways (**F009**):

> *"YopJ inhibited TLR-mediated NF-kappaB and MAP kinase activation, as suggested by previous studies. In addition, induction of the TLR-mediated interferon response was blocked by YopJ, indicating that YopJ also inhibits IRF3 signalling."* — Sweet 2007, [PMID: 17608743](https://pubmed.ncbi.nlm.nih.gov/17608743/)

**Cellular processes.** Inflammation (GO:0006954), inhibition of phagocytosis (GO:0006909), suppression of innate immune signaling, superantigen-driven T-cell proliferation (GO:0042110).

**Protein dysfunction (bacterial effectors as toxins):** YopH (tyrosine phosphatase), YopE/YopT (Rho GAP/protease), YopJ (acetyltransferase/deubiquitinase), YopO/YpkA (kinase), YopM (leukocyte-modulating). LcrF is the thermo-activated transcriptional master switch.

**Temperature control is the master mechanism (F003):**

> *"two different Y. pseudotuberculosis patient isolates expressing a stabilized thermometer variant were strongly reduced in their ability to disseminate into the Peyer's patches, liver and spleen and have fully lost their lethality"* — Böhme 2012, [PMID: 22359501](https://pubmed.ncbi.nlm.nih.gov/22359501/)

> *"Ysc-T3SS-mediated Yop secretion leads to global reprogramming of the Yersinia transcriptome with a massive shift of the expression from chromosomal to virulence plasmid-encoded genes"* — Meyer 2024, [PMID: 39159284](https://pubmed.ncbi.nlm.nih.gov/39159284/)

**Intestinal entry mechanism (F004):**

> *"Invasin protein is a high-affinity ligand for beta1 integrins and especially important in the early phase of intestinal infection for efficient translocation through the M cells located in the follicle-associated epithelium overlying the Peyer's patches."* — Grassl 2003, [PMID: 12755365](https://pubmed.ncbi.nlm.nih.gov/12755365/)

> *"Replication of bacteria in the intestine before translocation appeared critical for dissemination"* — Barnes 2006, [PMID: 16754724](https://pubmed.ncbi.nlm.nih.gov/16754724/)

**Superantigen mechanism (F002):**

> *"Patients with systemic symptoms such as lymphadenopathy, transient renal dysfunction, and arthritis had significantly higher titers of anti-YPM than patients with gastrointestinal tract symptoms alone."* — Abe 1997, [PMID: 9109426](https://pubmed.ncbi.nlm.nih.gov/9109426/)

> *"This shock was blocked by the injection of monoclonal antibodies (mAbs) to CD4, TCR Vbeta7 plus Vbeta8, tumor necrosis factor-alpha (TNF-alpha) and interferon-gamma (IFN-gamma)"* — Miyoshi-Akiyama 1997, [PMID: 9159409](https://pubmed.ncbi.nlm.nih.gov/9159409/)

Quantitatively (**F002**): 20/33 (61%) of acutely infected patients had elevated anti-YPM IgG vs controls (P=0.0001); Vβ3⁺ T cells were significantly increased in the acute phase (P=0.009).

**Immune involvement:** the disease is a contest between bacterial innate-immune evasion (Yop-mediated) and, in FESLF, pathological adaptive over-activation (superantigen-mediated). **Cell types (CL):** M cells, macrophages/neutrophils (CL:0000235, CL:0000775), CD4⁺ T cells (CL:0000624), dendritic cells (CL:0000451). **GO biological processes:** GO:0006909 (phagocytosis), GO:0042110 (T-cell activation), GO:0006954 (inflammatory response), GO:0043123 (positive regulation of NF-κB), GO:0009266 (response to temperature stimulus).

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- Terminal ileum and cecum (UBERON:0002116; UBERON:0001153)
- Mesenteric lymph nodes (UBERON:0002509)
- Peyer's patches / gut-associated lymphoid tissue (UBERON:0003454)

**Secondary organ involvement (dissemination/complications):**
- Liver (UBERON:0002107) and spleen (UBERON:0002106) — hepatosplenic abscessation
- Skin (UBERON:0002097) — rash, erythema nodosum
- Joints (UBERON:0000467 articular system) — reactive arthritis
- Kidney (UBERON:0002113) — transient renal dysfunction in FESLF
- Rarely muscle (myositis) and heart (myocarditis)

**Body systems:** digestive, lymphatic/immune, integumentary, musculoskeletal, and (in systemic disease) renal.

**Tissue/cell level:** intestinal follicle-associated epithelium (M cells), lymphoid tissue, professional phagocytes (macrophages, neutrophils), CD4⁺ T lymphocytes.

**Subcellular (GO Cellular Component):** host plasma membrane (GO:0005886, invasin–integrin contact and T3SS translocon), cytosol (GO:0005829, Yop effector site of action), and the bacterial T3SS injectisome.

**Localization/lateralization:** RLQ abdominal involvement (ileocecal) is characteristic; disease is systemic rather than lateralized.

---

## 8. Temporal Development

- **Onset:** acute to subacute after a short incubation (typically days). Predominantly affects **children and young adults** for the pseudoappendicitis form.
- **Course:** most cases are **self-limiting** over 1–3 weeks. FESLF is a more severe acute systemic illness.
- **Stages:** (1) intestinal colonization/replication → (2) lymphatic dissemination (mesenteric adenitis) → (3) possible systemic spread (hepatosplenic; FESLF) → (4) post-infectious immune sequelae (reactive arthritis, erythema nodosum) weeks later.
- **Progression rate:** generally self-limited; severe/septicemic progression is concentrated in iron-overloaded/immunosuppressed hosts.
- **Remission:** spontaneous in most; antibiotic-responsive in systemic disease.
- **Critical period:** the **37 °C temperature shift** on host entry is the decisive window that activates the T3SS virulence program (**F003**).

---

## 9. Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, founder effects, or carrier frequency.

**Epidemiology:**
- Sporadic worldwide; **epidemic FESLF** clusters in the Russian Far East and Japan (**F011**).

> *"Pseudotuberculosis in humans until the 1950s was found in different countries of the world as a rare sporadic disease that occurred in the form of acute appendicitis and mesenteric lymphadenitis."* — Somova 2020, [PMID: 32498317](https://pubmed.ncbi.nlm.nih.gov/32498317/)

- **Geographic distribution:** European strains cause mild disease; Far Eastern strains (YPMa⁺, pVM82⁺) cause severe systemic disease — a genotype-driven geographic virulence gradient (**F001**).
- **Age distribution:** skewed toward children/young adults for pseudoappendicitis.
- **Sex ratio:** no strong, well-established skew for the enteric form.
- **Serotype geography:** ≥21 O-serotypes; distinct serotype/plasmid profiles by region.

---

## 10. Diagnostics

**Two-tier diagnostic strategy (F007):**

**Acute disease — direct detection:**
- **Stool culture** (cold enrichment exploits psychrotrophy), tissue/mesenteric node culture.
- PCR for species/virulence genes (*inv*, *ypmA*, O-antigen gene clusters).
- Imaging (CT/ultrasound): mesenteric lymphadenopathy, terminal ileitis — helps distinguish from surgical appendicitis.

**Post-infectious / chronic disease — serology:**

> *"Whereas early infections can be diagnosed by direct detection of bacteria, chronic infections can only be identified by serological tests."* — Wielkoszynski 2018, [PMID: 30238343](https://pubmed.ncbi.nlm.nih.gov/30238343/)

**Species-discriminating serology** uses recombinant antigens (**F007**):

> *"discrimination between the two types of infection is based on two recombinant bacterial proteins, MyfA and PsaA (specific for Y. enterocolitica and Y. pseudotuberculosis, respectively)"* — [PMID: 30238343](https://pubmed.ncbi.nlm.nih.gov/30238343/)

**O-genotyping** by multiplex PCR of O-antigen gene clusters replaces classical serotyping and distinguishes *Y. pseudotuberculosis* from *Y. pestis* (Bogdanovich 2003, [PMID: 14605146](https://pubmed.ncbi.nlm.nih.gov/14605146/)).

**Differential diagnosis:** acute appendicitis, *Y. enterocolitica* infection, Crohn's terminal ileitis, Kawasaki disease (notably — several case reports link *Y. pseudotuberculosis* to KD-like presentations, e.g., [PMID: 9202805](https://pubmed.ncbi.nlm.nih.gov/9202805/)), streptococcal scarlet fever, and other causes of reactive arthritis/erythema nodosum.

**Omics diagnostics:** not routine; PCR-based genotyping is the molecular standard.

---

## 11. Outcome / Prognosis

- **Overall prognosis: excellent.** Most infections are self-limiting with full recovery.
- **Mortality:** low in immunocompetent hosts; significant risk of fatal **septicemia** in iron-overloaded, DFO-treated, splenectomized, or immunosuppressed patients (**F010**).
- **Morbidity:** driven by post-infectious **reactive arthritis** (~12% of yersiniosis, weeks–months of disability) and **erythema nodosum** (~3%) (**F006**); rare myositis/myocarditis.
- **Recovery:** high; antibiotics accelerate resolution of systemic disease.
- **Prognostic factors:** host iron status, immune competence, and infecting-strain genotype (YPMa/pVM82 → severe FESLF). High **anti-YPM titers** correlate with systemic rather than purely GI disease (a prognostic serologic marker) (**F002**).

---

## 12. Treatment

**Pharmacotherapy.** The organism is broadly antibiotic-susceptible (**F005**):

> *"None of the 58 Y. pseudotuber-culosis isolates was resistant to any tested antimicrobial."* — Kim 2017, [PMID: 28222842](https://pubmed.ncbi.nlm.nih.gov/28222842/)

| Drug class | Examples | Suggested NCIT | Notes |
|---|---|---|---|
| Fluoroquinolones | ciprofloxacin | NCIT:C540 | First-line for systemic disease |
| 3rd-gen cephalosporins | ceftriaxone, cefotaxime | NCIT:C1737 | Used in systemic/severe cases (incl. KD-associated case) |
| Aminoglycosides | gentamicin, enrofloxacin (vet) | NCIT:C61796 | Effective; note T3SS-associated tolerance in vitro |
| Tetracyclines | doxycycline, oxytetracycline | NCIT:C692 | Effective; oxytetracycline used in livestock outbreaks |
| TMP-SMX | trimethoprim-sulfamethoxazole | NCIT:C287 | Alternative (note sulfonamide resistance in some animal strains) |

- **Mild self-limiting gastroenteritis** typically needs only supportive care (rehydration).
- **Systemic/FESLF/septicemia** and high-risk hosts warrant antibiotics.
- **Caveat — antibiotic tolerance:** T3SS-induced growth arrest can reduce susceptibility to gentamicin and doxycycline in subpopulations within host tissues ([PMID: 40623067](https://pubmed.ncbi.nlm.nih.gov/40623067/); [PMID: 32753491](https://pubmed.ncbi.nlm.nih.gov/32753491/)).

**Supportive care:** hydration; NSAIDs for reactive arthritis/erythema nodosum. **Surgical:** occasionally unnecessary appendectomy is performed before diagnosis is clarified. **No gene, cell, or RNA-based therapies** are relevant.

---

## 13. Prevention

**No licensed human vaccine exists.** Prevention is centered on interrupting foodborne transmission (**F012**):

- **Primary prevention (food/water hygiene):** wash raw produce; treat/boil water; safe meat handling; recognize that **refrigeration does not stop this psychrotroph**, so cold storage is not protective.
- **Secondary prevention:** early culture-based diagnosis to avoid unnecessary appendectomy and to guide antibiotics in high-risk hosts.
- **Tertiary prevention:** prompt antibiotics and iron-management vigilance in β-thalassemia/hemochromatosis/DFO patients to prevent septicemia (**F010**).
- **Public health / veterinary:** reservoir control in livestock and food-processing hygiene; molecular surveillance links animal/food strains to human cases (**F008**, [PMID: 19835774](https://pubmed.ncbi.nlm.nih.gov/19835774/)).

---

## 14. Other Species / Natural Disease

**Zoonotic pathogen with broad reservoirs (F008):**

> *"Yersinia pseudotuberculosis and Yersinia enterocolitica are ubiquitous pathogens with wildlife and domestic animal reservoirs."* — Walker 2018, [PMID: 30360909](https://pubmed.ncbi.nlm.nih.gov/30360909/)

- **Natural disease in animals:** systemic *Y. pseudotuberculosis* O:1 causing multi-organ abscessation and osteomyelitis in a ring-tailed lemur (*Lemur catta*); outbreaks in zoological/research primate colonies (enteritis, mesenteric lymphadenitis, organ abscessation) (Walker 2018, [PMID: 30360909](https://pubmed.ncbi.nlm.nih.gov/30360909/)).
- **Livestock:** serotype III causes "winter scours" diarrhea outbreaks in weaned Merino sheep, seasonally in winter (Stanger 2018, [PMID: 29691860](https://pubmed.ncbi.nlm.nih.gov/29691860/)).
- **Wildlife surveillance:** beech marten and Alpine ibex identified as reservoirs, carrying mobilizable virulence plasmids (Carella 2022, [PMID: 35892105](https://pubmed.ncbi.nlm.nih.gov/35892105/)).
- **Species affected (NCBI Taxonomy):** pigs (txid9823), sheep (txid9940), primates including *Lemur catta* (txid9447), deer, rodents, birds, humans (txid9606).

**Comparative / evolutionary biology (F005):** *Y. pseudotuberculosis* is the recent enteric ancestor of *Y. pestis*:

> *"Conventional microbiology, bacterial population genetics, and genome sequence data, all suggest that Y pestis is a recently evolved clone of the enteric pathogen Yersinia pseudotuberculosis."* — Prentice & Rahalison 2007, [PMID: 17416264](https://pubmed.ncbi.nlm.nih.gov/17416264/)

**Zoonotic transmission:** fecal–oral via contaminated food/water; strain identity between human, pig, sheep, and food isolates confirms cross-species/food-chain transmission (**F008**).

---

## 15. Model Organisms

- **Mouse (oral infection model)** — the principal model. Recapitulates M-cell/Peyer's-patch entry, intestinal replication, and hepatosplenic dissemination; used to prove the temperature/T3SS and superantigen mechanisms.
  - Böhme 2012 ([PMID: 22359501](https://pubmed.ncbi.nlm.nih.gov/22359501/)): oral mouse infection demonstrated that a locked thermometer variant loses dissemination and lethality.
  - Barnes 2006 ([PMID: 16754724](https://pubmed.ncbi.nlm.nih.gov/16754724/)): oral mouse model showed intestinal replication precedes dissemination.
  - Miyoshi-Akiyama 1997 ([PMID: 9159409](https://pubmed.ncbi.nlm.nih.gov/9159409/)): murine YPM model established MHC-II-dependent Vβ7/Vβ8 expansion and TNF-α/IFN-γ-mediated lethal shock.
- ***Galleria mellonella*** (invertebrate infection model) — used for virulence/regulation studies (e.g., Fis regulator, [PMID: 41880349](https://pubmed.ncbi.nlm.nih.gov/41880349/)).
- **Cell-culture / in vitro** — epithelial cell invasion assays (invasin–β1-integrin), phagocyte intoxication assays (YopE/YopB-D), RNAi screens for host T3SS cofactors (e.g., CCR5, [PMID: 25691588](https://pubmed.ncbi.nlm.nih.gov/25691588/)).
- **Phenotype recapitulation:** the mouse oral model reproduces the enteric-to-systemic axis very well; it does **not** fully reproduce human FESLF because human-specific superantigen (YPMa) effects and the pVM82-linked epidemic phenotype are strain- and host-context dependent.

---

## Mechanistic Model / Interpretation

The disease is best understood as a **two-stage, genotype-branched infection**:

```
                       Y. pseudotuberculosis (ingested, cold-tolerant)
                                        |
                          invasin -> β1-integrin -> M cells
                                        |
                        intestinal replication (Peyer's patches)
                                        |
       37°C -> RNA thermometer/YmoA -> LcrF -> Ysc T3SS -> Yop effectors
              (YopH/E/T/O paralyze phagocytes; YopJ silences NF-κB/MAPK/IRF3)
                                        |
                    dissemination -> mesenteric nodes, liver, spleen
                                        |
        +-------------------------------+-------------------------------+
   European genotype                                        Far Eastern genotype
   (YPMa-, pVM82-)                                          (YPMa+, pVM82+)
        |                                                            |
  self-limiting gastroenteritis /                     YPMa superantigen ->
  pseudoappendicitis                                  Vβ3/7/8 CD4+ T-cell storm ->
        |                                             TNF-α/IFN-γ -> FESLF
        +---------------- post-infectious immune sequelae -----------+
                     (reactive arthritis ~12%, erythema nodosum ~3%)

  Host modifier: iron overload / DFO / immunosuppression -> septicemia
```

**Upstream vs downstream:** temperature sensing → LcrF → T3SS is the upstream master switch; Yop-mediated immune paralysis and (in FESLF) superantigen T-cell activation are downstream effectors; post-infectious arthritis/erythema nodosum are terminal immune sequelae. The pathogen genotype (plasmid/superantigen content) is the single strongest determinant of whether the outcome is mild or severe.

---

## Evidence Base

| PMID | Paper (abbreviated) | Supports | Contribution |
|---|---|---|---|
| [26819960](https://pubmed.ncbi.nlm.nih.gov/26819960/) | Far East scarlet-like fever review (Amphlett 2016) | F001 | Two clinical faces; YPMa in FESLF |
| [9109426](https://pubmed.ncbi.nlm.nih.gov/9109426/) | Clinical role of superantigen (Abe 1997) | F002 | Anti-YPM correlates with systemic disease |
| [9159409](https://pubmed.ncbi.nlm.nih.gov/9159409/) | Murine YPM toxicity (Miyoshi-Akiyama 1997) | F002 | Vβ/CD4, TNF-α/IFN-γ shock mechanism |
| [22359501](https://pubmed.ncbi.nlm.nih.gov/22359501/) | RNA thermometer/LcrF (Böhme 2012) | F003 | Temperature-gated virulence; in vivo proof |
| [39159284](https://pubmed.ncbi.nlm.nih.gov/39159284/) | RNase reprogramming (Meyer 2024) | F003 | T3SS-driven transcriptomic shift |
| [12755365](https://pubmed.ncbi.nlm.nih.gov/12755365/) | Invasin/β1-integrin (Grassl 2003) | F004 | M-cell entry mechanism |
| [16754724](https://pubmed.ncbi.nlm.nih.gov/16754724/) | Intestinal dissemination (Barnes 2006) | F004 | Replication precedes dissemination |
| [17416264](https://pubmed.ncbi.nlm.nih.gov/17416264/) | Plague (Prentice 2007) | F005 | Ancestor of Y. pestis |
| [14605146](https://pubmed.ncbi.nlm.nih.gov/14605146/) | O-genotyping PCR (Bogdanovich 2003) | F005 | ≥21 serotypes; O:1b origin of Y. pestis |
| [28222842](https://pubmed.ncbi.nlm.nih.gov/28222842/) | AMR in primates (Kim 2017) | F005 | Broad antibiotic susceptibility |
| [33321204](https://pubmed.ncbi.nlm.nih.gov/33321204/) | Pan-genomics/drug mining (Basharat 2021) | F006 | Phenotype spectrum enumeration |
| [23701958](https://pubmed.ncbi.nlm.nih.gov/23701958/) | Yersinia sequelae (Rosner 2013) | F006 | ReA ~12%, EN ~3% frequencies |
| [30238343](https://pubmed.ncbi.nlm.nih.gov/30238343/) | Diagnostic ELISA (Wielkoszynski 2018) | F007 | Culture vs serology; PsaA marker |
| [30360909](https://pubmed.ncbi.nlm.nih.gov/30360909/) | Lemur osteomyelitis (Walker 2018) | F008 | Zoonotic reservoir; animal disease |
| [19835774](https://pubmed.ncbi.nlm.nih.gov/19835774/) | Nigeria human/animal strains (Okwori 2009) | F008 | Food/animal-to-human strain identity |
| [29691860](https://pubmed.ncbi.nlm.nih.gov/29691860/) | Winter scours in sheep (Stanger 2018) | F008 | Livestock natural disease |
| [17608743](https://pubmed.ncbi.nlm.nih.gov/17608743/) | YopJ/TRAF (Sweet 2007) | F009 | NF-κB/MAPK/IRF3 inhibition |
| [11132234](https://pubmed.ncbi.nlm.nih.gov/11132234/) | Infections in E-β thalassemia (Wanachiwanawin 2000) | F010 | Iron/DFO risk factor |
| [30695393](https://pubmed.ncbi.nlm.nih.gov/30695393/) | Plasmid-associated virulence (Somova 2016) | F011 | pVM82 + YPMa → FESLF |
| [32498317](https://pubmed.ncbi.nlm.nih.gov/32498317/) | FESLF as special manifestation (Somova 2020) | F011 | Epidemiologic geographic pattern |
| [20088683](https://pubmed.ncbi.nlm.nih.gov/20088683/) | Cold adaptation (Palonen 2010) | F012 | Psychrotrophic foodborne transmission |

---

## Limitations and Knowledge Gaps

1. **Quantitative human epidemiology is sparse.** Precise incidence/prevalence (per 100,000) for *Y. pseudotuberculosis* specifically are not well established; many sequelae frequencies (reactive arthritis ~12%, erythema nodosum ~3%) are **extrapolated from *Y. enterocolitica*** population studies rather than measured for *Y. pseudotuberculosis* directly.
2. **FESLF molecular detail is understudied.** The pVM82 plasmid's gene content and the precise mechanistic link between pVM82 and the FESLF phenotype remain incompletely defined; YPMa's role is strongly implicated but the causal chain to renal dysfunction is partly inferred.
3. **No human host-genetic risk data.** Because this is infectious, no GWAS/germline susceptibility data exist; iron availability is the dominant, well-supported host modifier.
4. **Kawasaki-disease association is unresolved.** Several case reports link *Y. pseudotuberculosis* to KD-like illness, but causation vs. coincidence/molecular mimicry is not established.
5. **Antibiotic tolerance in tissue** (T3SS-induced growth arrest reducing aminoglycoside/tetracycline killing) is demonstrated in mouse models but its clinical treatment-failure significance in humans is unquantified.
6. **No original data analysis** was performed in this investigation; findings are literature-derived syntheses, so confidence rests on the quality of the cited primary studies.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify *Y. pseudotuberculosis*-specific sequelae** in a prospective human cohort (rather than extrapolating from *Y. enterocolitica*), stratified by infecting serotype and YPMa/pVM82 status.
2. **Complete pVM82 functional genomics:** sequence and mutate pVM82 loci to define which genes are necessary/sufficient for FESLF-associated renal and vascular pathology.
3. **Structure-guided anti-superantigen therapeutics:** build on the YPM point-mutant work ([PMID: 10087177](https://pubmed.ncbi.nlm.nih.gov/10087177/)) to develop TCR-Vβ-blocking or attenuated-toxoid immunotherapeutics for severe FESLF.
4. **Clinical tolerance study:** test whether T3SS-induced antibiotic tolerance drives relapse in systemic human disease and whether combination regimens or T3SS inhibitors improve clearance.
5. **Iron-management guideline evaluation:** assess whether temporary DFO cessation and prompt empirical antibiotics reduce septicemia mortality in iron-overloaded patients presenting with fever.
6. **Integrated One-Health surveillance:** expand PFGE/WGS matching of food, livestock, wildlife, and human isolates to map transmission chains and identify high-risk food vehicles for targeted prevention.


## Artifacts

- [OpenScientist final report](Yersinia_Pseudotuberculosis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Yersinia_Pseudotuberculosis_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 22 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Very common"; HP calls it **Fever**
- `HP:0002014` (1 mention) - the report calls it "Common"; HP calls it **Diarrhea**
- `HP:0004299` (1 mention) - the report calls it "Common (children)"; HP calls it **Hernia of the abdominal wall**
- `HP:0000988` (1 mention) - the report calls it "Far Eastern strains"; HP calls it **Skin rash**
- `HP:0012219` (1 mention) - the report calls it "~3% (Yersinia sequela est.)"; HP calls it **Erythema nodosum**
- `HP:0000083` (1 mention) - the report calls it "Systemic cases"; HP calls it **Renal insufficiency**
- `UBERON:0003454` (1 mention) - the report calls it "Peyer's patches / gut-associated lymphoid tissue"; UBERON calls it **small intestine Peyer's patch**
- `NCIT:C540` (1 mention) - the report calls it "ciprofloxacin"; NCIT calls it **Heparan Sulfate**
- `NCIT:C1737` (1 mention) - the report calls it "ceftriaxone, cefotaxime"; NCIT calls it **Organic Solvents**
- `NCIT:C61796` (1 mention) - the report calls it "gentamicin, enrofloxacin (vet)"; NCIT calls it **Ivermectin**
- `NCIT:C692` (1 mention) - the report calls it "doxycycline, oxytetracycline"; NCIT calls it **Nimodipine**
- `NCIT:C287` (1 mention) - the report calls it "trimethoprim-sulfamethoxazole"; NCIT calls it **Aspirin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0032169` (1 mention) - the report calls it "Severe FESLF"; HP calls it **Severe infection**
- `GO:0043123` (1 mention) - the report calls it "positive regulation of NF-κB"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**, and lists "positive regulation of I-kappaB kinase/NF-kappaB cascade" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names