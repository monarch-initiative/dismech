---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-14T20:46:30.658461'
end_time: '2026-09-14T21:20:11.837948'
duration_seconds: 2021.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bone Fragility With Contractures Arterial Rupture And Deafness
  mondo_id: MONDO:0012892
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 41
  not_found: 0
  obsolete: 3
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 3
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0012892
    reported_labels:
    - MONDO
    ontology_label: bone fragility with contractures, arterial rupture, and deafness
  - term_id: HP:0002650
    reported_labels:
    - Skeletal sign
    ontology_label: Scoliosis
  - term_id: HP:0002815
    reported_labels:
    - knee-related
    ontology_label: Abnormality of the knee
  - term_id: HP:0000518
    reported_labels:
    - Ocular sign
    ontology_label: Cataract
  - term_id: HP:0011003
    reported_labels:
    - Ocular
    ontology_label: High myopia
  - term_id: HP:0000541
    reported_labels:
    - Ocular
    ontology_label: Retinal detachment
  - term_id: HP:0000407
    reported_labels:
    - Auditory
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0010490
    reported_labels:
    - Physical
    ontology_label: Abnormal palmar crease morphology
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0000076
    reported_labels:
    - Renal
    ontology_label: Vesicoureteral reflux
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  - term_id: CHEBI:24544
    ontology_label: CHEBI_24544
    replaced_by: CHEBI:15525
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bone_Fragility_With_Contractures_Arterial_Rupture_And_Deafness-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bone_Fragility_With_Contractures_Arterial_Rupture_And_Deafness-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bone Fragility With Contractures Arterial Rupture And Deafness
- **MONDO ID:** MONDO:0012892 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bone Fragility With Contractures Arterial Rupture And Deafness** covering all of the
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

# Bone Fragility With Contractures, Arterial Rupture and Deafness (BCARD Syndrome): A Comprehensive Disease Report

**Disease:** Bone Fragility With Contractures, Arterial Rupture and Deafness (BCARD)
**MONDO ID:** MONDO:0012892 · **OMIM:** #612394 · **Gene:** *PLOD3* (LH3)
**Category:** Mendelian (autosomal recessive connective-tissue disorder)

---

## Summary

**Bone fragility with contractures, arterial rupture and deafness (BCARD)** is an ultra-rare, autosomal recessive, multisystem connective-tissue disorder caused by **biallelic loss-of-function variants in *PLOD3***, the gene encoding the multifunctional collagen-modifying enzyme **lysyl hydroxylase 3 (LH3)**. First described in a human patient in 2008, the disease remains exceptionally rare, with only approximately **11 patients across roughly seven reports** documented as of 2025. It is catalogued as OMIM #612394 and MONDO:0012892, and its clinical description is derived almost entirely from aggregated case reports of individual patients rather than large registries.

The central molecular lesion is loss of LH3 enzymatic activity. LH3 is unusual among collagen-modifying enzymes because it is bifunctional: it performs **lysyl hydroxylation** of collagen lysine residues and the subsequent **O-glycosylation** (galactosylation and glucosylation) of the resulting hydroxylysines. Mouse genetics have established that the **glucosyltransferase (GGT/Glc-T) activity — not the lysyl hydroxylase activity — is the function essential for basement-membrane formation**, and that embryonic survival correlates directly with residual GGT activity. Loss of hydroxylysine glycosylation prevents the intracellular assembly and secretion of network and beaded-filament collagens (types IV and VI), producing widespread failure of basement membranes and extracellular matrix. This matrix failure explains the pleiotropic clinical picture: low bone mineral density and bone fragility, joint/finger contractures, cataract with retinal-detachment risk, sensorineural deafness, and life-threatening arterial aneurysm/dissection, together with variable skin fragility (an epidermolysis-bullosa-like phenotype), muscle ultrastructural changes overlapping Ullrich congenital muscular dystrophy, and — in the most severe cases — a devastating neurovascular phenotype (cerebral small-vessel disease, cortical malformations, epilepsy).

Diagnosis rests on exome/genome sequencing plus a supportive biochemical biomarker — **markedly reduced glycosylated hydroxylysine** (galactosyl-hydroxylysine and glucosyl-galactosyl-hydroxylysine) in tissue/fibroblasts, and reduced LH3 protein in skin. There is **no disease-modifying therapy**; management is symptomatic and multidisciplinary, with particular vigilance for vascular catastrophe. This report synthesizes nine confirmed findings and 25 reviewed papers to populate the disease knowledge-base entry across all requested domains, and flags where evidence is absent or extrapolated.

---

## Key Findings

### F001 — BCARD is an autosomal recessive connective-tissue disorder caused by biallelic *PLOD3* (LH3) variants

BCARD (OMIM #612394; MONDO:0012892) is caused by **biallelic pathogenic variants in *PLOD3*** (encoding lysyl hydroxylase 3, LH3; gene OMIM 603066; HGNC:9083; located on chromosome **7q22.1**). The first patient, reported in 2008, was a **compound heterozygote**, establishing recessive inheritance. As of 2025 the literature describes only ~11 patients across ~7 reports, confirming ultra-rarity.

A 2025 review states plainly: *"BCARD syndrome is a rare autosomal recessive connective tissue disorder characterized by bone abnormalities, cataract, risk of arterial rupture due to vascular aneurisms or dissections, and sensorineural deafness"* and that *"BCARD, linked to biallelic pathogenic variants in the PLOD3 gene, was characterized in 10 cases across six reports"* ([PMID: 40289369](https://pubmed.ncbi.nlm.nih.gov/40289369/)). The original human report describes *"a human disorder of LH3 presenting as a compound heterozygote with recessive inheritance"* ([PMID: 18834968](https://pubmed.ncbi.nlm.nih.gov/18834968/)).

### F002 — LH3/PLOD3 is a multifunctional collagen-modifying enzyme whose glycosyltransferase activity is essential for basement-membrane collagen secretion

LH3 catalyzes lysyl hydroxylation and the subsequent O-glycosylation of hydroxylysines (galactosyl- and glucosylgalactosyl-hydroxylysine) on collagens. Critically, mouse genetics demonstrate that the **glucosyltransferase (GGT) activity, not the lysyl hydroxylase activity, is the function essential for basement-membrane formation**: LH3-knockout and GGT-null hypomorphic embryos die at E9.5–E14.5 from failed basement-membrane formation, and **embryonic survival correlates directly with the level of GGT activity**. Loss of glycosylated hydroxylysines prevents the intracellular tetramerization of type VI collagen and impairs secretion of types IV and VI collagen. Recent enzymology (2023) refines the division of labor, showing LH3 carries the Glc-T activity while GLT25D1 provides the Gal-T activity.

Key evidence: *"the GGT activity, not the LH activity of LH3, is essential for the formation of the basement membrane"* and *"survival of hypomorphic embryos and the formation of the basement membrane were directly correlated with the level of GGT activity"* ([PMID: 16467571](https://pubmed.ncbi.nlm.nih.gov/16467571/)); *"loss of glycosylated hydroxylysines prevents the intracellular tetramerization of type VI collagen and leads to impaired secretion of type IV and VI collagens"* ([PMID: 17873278](https://pubmed.ncbi.nlm.nih.gov/17873278/)); and *"LH3/PLOD3 only has Glc-T activity and that GLT25D1 only has Gal-T activity"* ([PMID: 37446392](https://pubmed.ncbi.nlm.nih.gov/37446392/)).

### F003 — BCARD presents as a multisystem phenotype overlapping Stickler, Ehlers-Danlos and epidermolysis bullosa

Cardinal features span multiple organ systems: **skeletal** (low bone mineral density/bone fragility, scoliosis, prominent knees, finger/joint contractures), **ocular** (cataract, high myopia, retinal-detachment risk), **auditory** (sensorineural hearing loss), **vascular** (aneurysms/dissection, risk of arterial rupture), plus craniofacial dysmorphism, reduced palmar creases, and developmental delay. Some patients show a **recessive dystrophic epidermolysis bullosa (RDEB)-like** sub-lamina-densa skin blistering with abnormal anchoring fibrils and reduced type VII collagen. The 2025 expansion added vesico-ureteral reflux, intestinal and cardiac anomalies, focal epilepsy, and brain malformations (polymicrogyria, heterotopia). The overall phenotype overlaps **most with Stickler syndrome**, with variable EDS and EB features.

Supporting quotes: *"Key clinical features included ocular abnormalities with risk for retinal detachment, sensorineural hearing loss, reduced palmar creases, finger contractures, prominent knees, scoliosis, low bone mineral density, recognisable craniofacial dysmorphisms, developmental delay and risk for vascular dissection"* and *"Collated clinical features showed most overlap with Stickler syndrome with variable features of Ehlers-Danlos syndrome (EDS) and epidermolysis bullosa (EB)"* ([PMID: 31129566](https://pubmed.ncbi.nlm.nih.gov/31129566/)); *"The blistering in the skin occurred below the lamina densa and was associated with variable density and morphology of anchoring fibrils. The level of type VII collagen expression in the skin was markedly reduced"* ([PMID: 30463024](https://pubmed.ncbi.nlm.nih.gov/30463024/)); *"also exhibited vesico-ureteral reflux, intestinal anomaly, minor cardiac anomalies, focal epilepsy, and brain abnormalities, including polymicrogyria and heterotopia"* ([PMID: 40289369](https://pubmed.ncbi.nlm.nih.gov/40289369/)).

### F004 — LH3/PLOD3 molecular structure maps disease mutations near catalytic sites

Full-length human LH3 crystal structures reveal an **elongated homodimer** with two distinct catalytic sites — an **N-terminal glycosyltransferase domain** and a **C-terminal lysyl hydroxylase/dioxygenase domain** — separated by an accessory domain. Known disease-related mutations map in close proximity to the catalytic sites, and specific variants selectively abolish either the lysyl hydroxylase or the glycosyltransferase activity, accompanied by reduced LH3 protein levels in patient cells.

Evidence: *"The elongated homodimeric LH3 architecture shows two distinct catalytic sites at the N- and C-terminal boundaries of each monomer, separated by an accessory domain"* and *"Known disease-related mutations map in close proximity to the catalytic sites"* ([PMID: 30089812](https://pubmed.ncbi.nlm.nih.gov/30089812/)); *"One mutation dramatically reduced the sugar-transfer activity of LH3, whereas another abrogated lysyl hydroxylase activity; these changes were accompanied by reduced LH3 protein levels in cells"* ([PMID: 18834968](https://pubmed.ncbi.nlm.nih.gov/18834968/)).

### F005 — Post-Golgi trafficking of LH3 is required for collagen glycosylation homeostasis, linking BCARD to ARC syndrome biology

LH3 acts partly extracellularly / post-Golgi. **VIPAR (VIPAS39) together with VPS33B sorts LH3 into newly identified post-Golgi collagen-IV carriers**, and this sorting is essential for lysine modification of multiple collagen types. Loss of VIPAR/VPS33B — which causes **Arthrogryposis–Renal dysfunction–Cholestasis (ARC) syndrome** — produces collagen abnormalities mirroring those of primary LH3 deficiency, connecting the two disorders mechanistically.

Evidence: *"VIPAR, with its partner proteins, regulate sorting of lysyl hydroxylase 3 (LH3, also known as PLOD3) into newly identified post-Golgi collagen IV carriers and that VIPAR-dependent sorting is essential for modification of lysines in multiple collagen types"* and *"regulation of post-Golgi LH3 trafficking is essential for collagen homeostasis and for the development and function of multiple organs and tissues"* ([PMID: 27435297](https://pubmed.ncbi.nlm.nih.gov/27435297/)).

### F006 — Reduced glycosylated hydroxylysine is the biochemical hallmark and candidate diagnostic biomarker

Patient tissue/fibroblast analyses show **markedly reduced glycosylated hydroxylysine** — specifically galactosyl-hydroxylysine and glucosyl-galactosyl-hydroxylysine — together with dramatically reduced LH3 protein in skin and fibroblast cultures. LH3 normally localizes to the epidermal basement membrane and is severely depleted there in patients, making immunostaining a complementary diagnostic modality.

Evidence: *"Analysis of hydroxylysine and its glycosylated derivatives (galactosyl-hydroxylysine and glucosyl-galactosyl-hydroxylysine) revealed marked reduction in glycosylated hydroxylysine"* and *"The level of LH3 was dramatically reduced in the skin and fibroblast cultures from the patient"* ([PMID: 30463024](https://pubmed.ncbi.nlm.nih.gov/30463024/)); *"We show abundant LH3 localising to the basement membrane in normal skin which is severely depleted in RDEB patient skin"* ([PMID: 26380979](https://pubmed.ncbi.nlm.nih.gov/26380979/)).

### F007 — PLOD3/LH3 deficiency includes a severe neurovascular phenotype

A homozygous in-frame variant **c.1216_1218delCTC (p.Leu406del)** caused an infantile-onset (10 months) severe phenotype: developmental delay, clustered epileptic spasms with hypsarrhythmia (**West syndrome**), and MRI showing multiple intracranial malacias, bleeding foci, extensive white-matter abnormalities and brain atrophy consistent with **cerebral small-vessel disease (SVD)**, plus flattened vertebrae and metacarpal abnormalities. The 2025 case added polymicrogyria, heterotopia and focal epilepsy. Craniofacial dysmorphism (hypertelorism, upturned nose, low-set ears) was noted.

Evidence: *"Cerebral magnetic resonance imaging showed multiple intracranial malacias and bleeding foci, extensive abnormal signals in the white matter, and obvious brain atrophy, which was consistent with cerebral small vessel disease (SVD)"* and *"Whole-exome sequencing revealed a novel homozygous variant of c.1216_1218delCTC (p.L406del)"* ([PMID: 36203519](https://pubmed.ncbi.nlm.nih.gov/36203519/)); *"brain abnormalities, including polymicrogyria and heterotopia"* ([PMID: 40289369](https://pubmed.ncbi.nlm.nih.gov/40289369/)).

### F008 — gnomAD constraint metrics confirm *PLOD3* is not haploinsufficient, consistent with recessive disease

gnomAD (GRCh38) constraint for *PLOD3* (ENSG00000106397; chr7:101,205,977–101,218,420; 7q22.1) shows **pLI ≈ 0** (6.4e-19), **LoF observed/expected = 0.75** (73 observed vs 96.9 expected LoF variants), **LOEUF = 0.92**, and missense Z ≈ 0.004 (oe_mis ≈ 1.0). Heterozygous loss-of-function is therefore tolerated in the general population, matching the observed autosomal recessive (biallelic) inheritance. This is consistent with the human report of *"a human disorder of LH3 presenting as a compound heterozygote with recessive inheritance"* ([PMID: 18834968](https://pubmed.ncbi.nlm.nih.gov/18834968/)).

### F009 — LH3 deficiency produces collagen VI muscle ultrastructural changes overlapping Ullrich congenital muscular dystrophy

In LH3-manipulated mice, altered distribution and aggregation of type VI collagen produced muscle ultrastructural alterations **similar to those in collagen VI knockout mice and some Ullrich congenital muscular dystrophy patients**. Underglycosylated types IV and VI collagen showed abnormal distribution. Evidence: *"The altered distribution and aggregation of type VI collagen led to similar ultrastructural alterations in muscle to those detected in collagen VI knockout and some Ullrich congenital muscular dystrophy patients"* ([PMID: 17873278](https://pubmed.ncbi.nlm.nih.gov/17873278/)).

---

## Section-by-Section Disease Characterization

### 1. Disease Information

BCARD is a **rare autosomal recessive connective-tissue disorder** defined by the combination of bone abnormalities/fragility, joint contractures, cataract, risk of arterial rupture (aneurysm/dissection), and sensorineural deafness ([PMID: 40289369](https://pubmed.ncbi.nlm.nih.gov/40289369/)).

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM (disease) | #612394 |
| OMIM (gene *PLOD3*) | 603066 |
| MONDO | MONDO:0012892 |
| HGNC | HGNC:9083 (*PLOD3*) |
| Ensembl gene | ENSG00000106397 |
| Cytoband | 7q22.1 |

**Synonyms / alternative names:** "Bone fragility with contractures, arterial rupture, and deafness"; "BCARD syndrome"; "PLOD3-related connective tissue disorder"; "Lysyl hydroxylase 3 (LH3) deficiency." Orphanet, ICD-10/ICD-11, and MeSH do not maintain a dedicated, widely-cited term distinct from the OMIM/MONDO entries; the condition is best indexed via OMIM #612394 and the gene *PLOD3*.

**Source of information:** Derived almost exclusively from **aggregated individual case reports** (~11 patients / ~7 reports), not EHR-scale or registry data.

### 2. Etiology

**Primary cause:** Purely **genetic** — biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in *PLOD3* (F001, F004). No environmental or infectious cause exists.

**Genetic risk factors:** The disease-causing variants are the only known genetic determinant. Because *PLOD3* is **not haploinsufficient** (pLI ≈ 0, LOEUF 0.92; F008), carriers (heterozygotes) are unaffected, and disease requires two damaging alleles. **Consanguinity** is a relevant contributor because homozygous variants (e.g., p.Leu406del) have been reported (F007).

**Environmental / lifestyle / infectious factors, protective factors, gene-environment interactions:** No environmental risk or protective factors, and no gene–environment interactions, are established for this Mendelian disorder. Clinically, avoidance of vascular stressors is prudent given arterial fragility, but this is inferred, not evidence-based.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / severity / frequency notes |
|---|---|---|---|
| Low bone mineral density / bone fragility | Skeletal sign | HP:0004349 / HP:0002659 | Congenital-early; core feature |
| Joint / finger contractures | Physical manifestation | HP:0002803 / HP:0009473 | Early; core |
| Scoliosis | Skeletal sign | HP:0002650 | Childhood |
| Prominent knees | Physical | HP:0002815 (knee-related) | Core |
| Cataract | Ocular sign | HP:0000518 | Congenital/early; core |
| High myopia | Ocular | HP:0011003 | Variable |
| Retinal detachment (risk) | Ocular | HP:0000541 | Risk feature |
| Sensorineural hearing loss | Auditory | HP:0000407 | Core |
| Arterial aneurysm / dissection / rupture | Vascular | HP:0002616 / HP:0004942 | Life-threatening; variable onset |
| Reduced palmar creases | Physical | HP:0010490 | Recognizable sign |
| Craniofacial dysmorphism | Physical | HP:0001999 | Core |
| Developmental delay | Neurodevelopmental | HP:0001263 | Variable |
| Skin blistering (EB-like) | Skin | HP:0008066 | Variable subphenotype |
| Vesico-ureteral reflux | Renal | HP:0000076 | Expanded (2025) |
| Focal epilepsy / epileptic spasms | Neurological | HP:0007359 / HP:0011097 | Severe cases |
| Polymicrogyria / heterotopia | CNS malformation | HP:0002126 / HP:0002282 | Severe cases |

Frequencies cannot be quantified precisely given ~11 patients. Severity is **variable**, ranging from a Stickler-like presentation to lethal infantile neurovascular disease (F003, F007). Progression is generally **stable-to-progressive** with episodic vascular risk. Quality-of-life impact is substantial: sensory (vision, hearing), mobility (contractures, bone fragility), neurodevelopmental disability, and the constant threat of vascular catastrophe. No disease-specific QoL instruments (EQ-5D/SF-36) have been applied to this ultra-rare cohort.

### 4. Genetic / Molecular Information

**Causal gene:** *PLOD3* (LH3), OMIM 603066, HGNC:9083, chr 7q22.1 (F001). **Inheritance:** autosomal recessive.

**Pathogenic variants:** Reported variants include compound-heterozygous missense/functional variants in the founding case (one abrogating glycosyltransferase activity, another abrogating lysyl hydroxylase activity; F004), and the homozygous in-frame deletion **c.1216_1218delCTC (p.Leu406del)** in the severe neurovascular case (F007). Variant types span **missense, in-frame deletion, and loss-of-function** alleles. Functionally, variants cause **loss of function** — either selectively ablating one of LH3's two catalytic activities or reducing overall protein level (F004). Disease-related mutations cluster **near the catalytic sites** in the LH3 structure (F004).

**Allele frequency / population data:** Consistent with recessive disease, gnomAD shows LoF is tolerated (73 observed vs 96.9 expected; LOEUF 0.92); no common pathogenic allele reaches appreciable frequency (F008). **Origin:** germline. **Modifier genes / epigenetics / chromosomal abnormalities:** none established; trafficking partners **VPS33B/VIPAR** functionally modulate LH3 activity and, when mutated, cause the related ARC syndrome (F005).

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents contribute to BCARD. It is a monogenic disorder (F001, F002). This section is **not applicable** beyond noting that mechanical/vascular stress may precipitate complications (rupture) in already-fragile tissue (inferred).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic *PLOD3* loss-of-function variants** *lead to* reduced/absent functional LH3 enzyme (and reduced LH3 protein levels) (F001, F004).
2. Loss of LH3 *results in* deficient **lysyl hydroxylation** and, critically, deficient **glucosyltransferase (GGT/Glc-T)-mediated O-glycosylation** of collagen hydroxylysines (F002).
3. Loss of glycosylated hydroxylysines *prevents* the **intracellular tetramerization of type VI collagen** and *impairs* **secretion of type IV and type VI collagens** (F002).
4. Impaired secretion/assembly *leads to* **failure of basement-membrane formation** and defective extracellular matrix (demonstrated in mouse: BM formation and embryo survival scale with residual GGT activity) (F002).
5. **[Branch — trafficking]** LH3 must be sorted into post-Golgi collagen-IV carriers by **VPS33B/VIPAR**; if this axis fails, the same collagen-modification defect ensues (links BCARD to ARC syndrome) (F005).
6. Matrix failure *manifests* in a tissue-specific manner:
   - Bone/connective tissue → **bone fragility, contractures, scoliosis** (inferred from collagen/matrix defect).
   - Basement-membrane-dependent structures (lens, cochlea, vessel wall) → **cataract, sensorineural deafness, arterial aneurysm/rupture** (inferred from BM collagen IV failure).
   - Skin (anchoring fibrils, type VII collagen reduced) → **EB-like sub-lamina-densa blistering** (F003, F006).
   - Muscle (collagen VI mis-aggregation) → **Ullrich-CMD-like ultrastructural change** (F009).
   - CNS microvasculature → **cerebral small-vessel disease, hemorrhage, cortical malformation, epilepsy** in severe cases (F007).

**Upstream vs downstream:** The mutation and enzymatic loss are upstream; collagen underglycosylation and secretion failure are the pivotal intermediate node; organ-specific matrix failure is downstream. **Molecular pathway:** collagen biosynthesis / post-translational modification (hydroxylysine formation and O-glycosylation). **GO term suggestions:** *peptidyl-lysine hydroxylation* (GO:0017185), *collagen fibril organization* (GO:0030199), *basement membrane organization* (GO:0071711), *collagen-containing extracellular matrix* (GO:0062023, cellular component), *protein glycosylation* (GO:0006486). **CL/cell types:** fibroblast (CL:0000057), osteoblast (CL:0000062), vascular smooth muscle cell (CL:0000359), keratinocyte (CL:0000312). **CHEBI entities:** hydroxylysine (CHEBI:24544-class), galactosylhydroxylysine, glucosylgalactosylhydroxylysine, UDP-glucose (CHEBI:46229), UDP-galactose, 2-oxoglutarate (CHEBI:16810). **Subcellular compartments:** endoplasmic reticulum and Golgi (GO:0005783, GO:0005794) for collagen modification/secretion; post-Golgi carriers/extracellular space for LH3 trafficking (F005).

### 7. Anatomical Structures Affected

**Primary organs / systems:** skeleton (UBERON:0002481 bone tissue), eye/lens (UBERON:0000965 lens), inner ear/cochlea (UBERON:0001844), arteries/vascular system (UBERON:0001637; cardiovascular system UBERON:0004535), skin (UBERON:0002097), skeletal muscle (UBERON:0001134), and — in severe cases — brain (UBERON:0000955) and cerebral small vessels. **Secondary:** kidney/urinary tract (vesico-ureteral reflux), gastrointestinal tract, and heart (minor anomalies) (F003).

**Tissue/cell level:** connective tissue and basement membranes are the unifying target; affected cell populations include fibroblasts, osteoblasts, vascular smooth-muscle cells, keratinocytes, and CNS vascular cells (F002, F003, F007, F009). **Subcellular:** ER/Golgi secretory pathway and post-Golgi trafficking (F005). **Lateralization:** systemic/bilateral.

### 8. Temporal Development

**Onset:** congenital-to-infantile; the severe neurovascular form presented at **10 months** (F007). **Pattern:** chronic with a superimposed **episodic** risk of acute vascular events (dissection/rupture) and, in severe cases, epileptic spasms. **Progression:** variable — from a relatively stable Stickler-like course to rapidly progressive infantile encephalopathy with brain atrophy (F007). **Critical periods:** early development (basement-membrane formation is embryonically essential in mouse models; F002) and any period of vascular stress. **Duration:** lifelong.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive (F001, F008). **Epidemiology:** ultra-rare; no formal prevalence/incidence estimate exists — only ~11 patients reported worldwide (F001). **Penetrance:** appears complete in biallelic carriers, though **expressivity is highly variable** (F003, F007). **Consanguinity** contributes (homozygous variants reported). **Carrier frequency:** not formally established; gnomAD LoF tolerance indicates carriers are asymptomatic and present in the general population (F008). **Founder effects, anticipation, germline mosaicism:** none reported. **Sex ratio / ethnicity / geography:** no demonstrated bias; cases are geographically scattered.

### 10. Diagnostics

**Genetic testing is the definitive diagnostic modality.** Given the multisystem, Stickler/EDS/EB-overlapping phenotype, **whole-exome or whole-genome sequencing** (or a connective-tissue/collagenopathy gene panel including *PLOD3*) is the recommended approach; single-gene testing is appropriate when the phenotype is recognized (F003).

**Biochemical biomarker:** **reduced glycosylated hydroxylysine** (galactosyl-hydroxylysine and glucosyl-galactosyl-hydroxylysine) in tissue/fibroblasts, with reduced LH3 protein — a supportive, mechanism-specific assay (F006). **Immunohistochemistry** of skin shows severe basement-membrane LH3 depletion (F006). **Imaging:** DXA (low BMD), skeletal radiographs (flattened vertebrae, metacarpal changes), vascular imaging (CT/MR angiography for aneurysm/dissection surveillance), ophthalmologic exam (cataract, myopia, retinal detachment), audiometry (sensorineural loss), and brain MRI in neurological cases (SVD, malformations) (F003, F007). **Skin biopsy/EM** in blistering cases shows sub-lamina-densa cleavage, abnormal anchoring fibrils, reduced type VII collagen (F003, F006).

**Differential diagnosis:** Stickler syndrome (closest overlap), Ehlers-Danlos syndromes, epidermolysis bullosa, Ullrich congenital muscular dystrophy, and ARC syndrome (VPS33B/VIPAR) (F003, F005, F009).

### 11. Outcome / Prognosis

Prognosis is **guarded and variable**. The most serious threat is **arterial rupture/dissection**, a potentially fatal complication (F001, F003). The severe infantile neurovascular form carries a poor prognosis with cerebral small-vessel disease, hemorrhage, brain atrophy, and refractory epileptic spasms (F007). Morbidity is high across sensory (vision, hearing), musculoskeletal (fragility, contractures), and neurodevelopmental domains. No formal survival statistics exist due to rarity. **Prognostic factors** (inferred): earlier onset and neurovascular involvement predict worse outcomes. No validated prognostic biomarkers exist beyond the mechanistic biochemical markers.

### 12. Treatment

**No disease-modifying therapy exists.** Management is **symptomatic and multidisciplinary** (NCIT suggestions: *Supportive Care Intervention*, *Physical Therapy*, *Surgical Procedure*, *Genetic Counseling*):
- **Vascular:** surveillance imaging and prophylactic/emergency vascular surgery for aneurysm/dissection; avoidance of vascular stress (inferred best practice given rupture risk).
- **Skeletal:** management of low BMD and fractures; orthopedic care for scoliosis/contractures; physical and occupational therapy.
- **Ophthalmologic:** cataract surgery, myopia correction, retinal-detachment monitoring/repair.
- **Auditory:** hearing aids / cochlear implantation for sensorineural loss.
- **Neurological:** anti-seizure medication for epileptic spasms/focal epilepsy; developmental support.
- **Dermatologic:** wound care for EB-like blistering.

**Pharmacogenomics, gene/cell/RNA therapy, targeted/immunotherapy:** none established or in trials for BCARD specifically. **Experimental therapeutics:** no registered clinical trials identified for this disease.

### 13. Prevention

There is no primary prevention for this Mendelian disorder beyond **reproductive genetic counseling**. Given autosomal recessive inheritance and a role for consanguinity, **carrier testing** of at-risk relatives, **cascade testing**, and options such as **prenatal diagnosis** or **preimplantation genetic testing** are appropriate for families with a known variant (F001, F008). **Secondary/tertiary prevention** focuses on surveillance (vascular imaging, ophthalmology, audiology, DXA) and prompt intervention to prevent catastrophic complications, especially arterial rupture (F003). NCIT suggestion: *Genetic Counseling*, *Prenatal Diagnosis*.

### 14. Other Species / Natural Disease

*PLOD3* is evolutionarily conserved; the mouse ortholog **Plod3** provides the key mechanistic models (F002, F009). No naturally occurring companion-animal or wildlife BCARD-equivalent disease is documented in OMIA. There is no zoonotic or transmission relevance (monogenic disorder). Orthologs exist across vertebrates (human *PLOD3* NCBI Gene 8985; mouse *Plod3*), supporting cross-species mechanistic study.

### 15. Model Organisms

The principal model is the **mouse (*Mus musculus*)**:
- **LH3/Plod3 knockout** embryos die at **E9.5** from failed basement-membrane formation (F002).
- **GGT-null hypomorphic** embryos die E9.5–E14.5, with survival scaling to residual GGT activity — establishing the glucosyltransferase activity as the essential function (F002).
- LH3-manipulated mice reproduce **collagen VI muscle ultrastructural pathology** overlapping Ullrich CMD (F009).

**Phenotype recapitulation:** mouse models faithfully capture the core molecular lesion (collagen underglycosylation, BM failure) and muscle pathology; **limitation:** complete knockouts are embryonic-lethal, so hypomorphic/conditional models are required to study postnatal, organ-specific human features (bone, ear, vessel, brain). Cellular models — **patient fibroblasts** — recapitulate reduced glycosylated hydroxylysine and reduced LH3 protein (F006), and the **VPS33B/VIPAR (ARC syndrome)** system provides complementary in vitro/murine models of the trafficking arm (F005). No zebrafish, Drosophila, or iPSC/organoid BCARD models are documented in the reviewed literature.

---

## Mechanistic Model / Interpretation

```
 Biallelic PLOD3 (LH3) LoF variants
              │  (F001, F004; variants cluster near catalytic sites)
              ▼
 Loss of LH3 lysyl-hydroxylase AND glucosyltransferase (GGT) activity
              │  (F002; GGT activity is the essential one)
              ▼
 Deficient O-glycosylation of collagen hydroxylysines
   (↓ galactosyl-Hyl, ↓ glucosyl-galactosyl-Hyl)  ◄── DIAGNOSTIC BIOMARKER (F006)
              │
              ▼
 Failed intracellular assembly (Col VI tetramerization) +
 impaired secretion of type IV & VI collagens              (F002)
              │
      ┌───────┴─────────────────────────────┐
      ▼                                       ▼
 Basement-membrane failure            Post-Golgi trafficking dependency
 (embryonically essential in mouse)   via VPS33B/VIPAR — shared with
      │                               ARC syndrome                (F005)
      ▼
 ORGAN-SPECIFIC MATRIX FAILURE
  ├─ Bone/joint → fragility, contractures, scoliosis
  ├─ Lens → cataract; retina → detachment risk
  ├─ Cochlea → sensorineural deafness
  ├─ Artery wall → aneurysm / dissection / RUPTURE  ◄── lethal risk
  ├─ Skin → EB-like sub-lamina-densa blistering (↓ Col VII)   (F003, F006)
  ├─ Muscle → Ullrich-CMD-like ultrastructure (Col VI)        (F009)
  └─ CNS microvessels → small-vessel disease, hemorrhage,
     cortical malformation, epilepsy (severe cases)           (F007)
```

The unifying interpretation is that **BCARD is a "collagen post-translational modification disease."** A single enzyme's bifunctional loss cripples the glycosylation step required to fold, assemble and secrete the network (type IV) and beaded-filament (type VI) collagens that build basement membranes and connective-tissue scaffolds throughout the body. Because these collagens are ubiquitous, the phenotype is pleiotropic and overlaps several better-known collagenopathies (Stickler, EDS, EB, Ullrich CMD) — a diagnostic pitfall that makes sequencing essential. The glucosyltransferase activity is the mechanistic linchpin, and the trafficking arm (VPS33B/VIPAR) explains the phenotypic kinship with ARC syndrome.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [40289369](https://pubmed.ncbi.nlm.nih.gov/40289369/) | *Expanding the Clinical Spectrum of BCARD Syndrome…* | Defines disease, AR inheritance, biallelic *PLOD3*, ultra-rarity; expands phenotype to renal/GI/cardiac/CNS (F001, F003, F007) |
| [18834968](https://pubmed.ncbi.nlm.nih.gov/18834968/) | *A connective tissue disorder caused by mutations of the LH3 gene* | First human case; recessive/compound-het; variant-specific loss of each enzymatic activity (F001, F004, F008) |
| [16467571](https://pubmed.ncbi.nlm.nih.gov/16467571/) | *Glycosylation catalyzed by LH3 is essential for basement membranes* | GGT activity is the essential function; dose-dependent embryo survival (F002) |
| [17873278](https://pubmed.ncbi.nlm.nih.gov/17873278/) | *Secretion and assembly of type IV and VI collagens depend on glycosylation…* | Mechanism: loss of Hyl-glycosylation blocks Col VI tetramerization / Col IV,VI secretion; Ullrich CMD muscle overlap (F002, F009) |
| [37446392](https://pubmed.ncbi.nlm.nih.gov/37446392/) | *Regulatory "Hot Spots" for LH/PLOD glycosyltransferase activity* | Enzymatic division of labor: LH3=Glc-T, GLT25D1=Gal-T (F002) |
| [30089812](https://pubmed.ncbi.nlm.nih.gov/30089812/) | *Molecular architecture of LH3* | Homodimer, two catalytic sites; disease mutations near active sites (F004) |
| [31129566](https://pubmed.ncbi.nlm.nih.gov/31129566/) | *Pathogenic variants in PLOD3…* | Clinical feature catalogue; Stickler/EDS/EB overlap (F003) |
| [30463024](https://pubmed.ncbi.nlm.nih.gov/30463024/) | *PLOD3 mutations cause RDEB-like blistering…* | Skin phenotype; reduced glycosylated Hyl biomarker; reduced LH3 protein (F003, F006) |
| [26380979](https://pubmed.ncbi.nlm.nih.gov/26380979/) | *LH3 localizes to epidermal basement membrane…* | LH3 BM localization/depletion; IHC diagnostic modality (F006) |
| [36203519](https://pubmed.ncbi.nlm.nih.gov/36203519/) | *Cerebral small vessel disease caused by PLOD3…* | Severe neurovascular phenotype; homozygous p.Leu406del (F007) |
| [27435297](https://pubmed.ncbi.nlm.nih.gov/27435297/) | *Regulation of post-Golgi LH3 trafficking…* | VPS33B/VIPAR sorting of LH3; ARC syndrome link (F005) |

The remaining reviewed papers (e.g., PLOD3 in colorectal, lung, liver, bladder, esophageal cancers; PMIDs 39948137, 35265665, 35116582, 36872941, 41491166, 39659928, 34646265) concern PLOD3's oncologic/ECM-remodeling role and do **not** bear directly on BCARD pathophysiology; they are noted here only to document that LH3 also functions in tumor ECM stiffening — a context distinct from the germline loss-of-function disease.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity (n ≈ 11):** All clinical conclusions rest on a handful of case reports. Frequencies, penetrance, expressivity, and prognosis cannot be quantified with confidence.
2. **No epidemiological data:** Prevalence, incidence, carrier frequency, sex/ethnic distribution are unknown.
3. **Genotype–phenotype correlation is immature:** Only a few variants are functionally characterized; whether specific alleles (e.g., GGT-selective vs LH-selective) predict organ-specific severity is unresolved.
4. **Mechanistic inference for organ-specific features:** The link from collagen underglycosylation to bone, ear, and vessel phenotypes is strongly plausible but largely **inferred** from collagen biology rather than directly demonstrated in BCARD tissue.
5. **No therapeutics or trials:** No disease-modifying therapy, no registered clinical trials, no validated QoL or prognostic instruments.
6. **Model gaps:** Complete-knockout embryonic lethality limits study of postnatal features; conditional/hypomorphic, zebrafish, and iPSC/organoid models are underdeveloped or absent.
7. **Biomarker validation:** Reduced glycosylated hydroxylysine is promising but not standardized as a clinical diagnostic assay across laboratories.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international BCARD/PLOD3 patient registry** to aggregate the scattered cases and generate the first real prevalence, penetrance, natural-history, and mortality data — with structured vascular-event and neurodevelopmental outcomes.
2. **Systematic genotype–phenotype study:** functionally classify each reported *PLOD3* variant for residual LH vs GGT activity (in vitro assays) and correlate with organ involvement and severity, testing the hypothesis that residual GGT activity predicts survival/severity (extending F002).
3. **Standardize the biochemical diagnostic:** validate a quantitative urinary/tissue glycosylated-hydroxylysine assay (ratio of glucosyl-galactosyl-Hyl to total Hyl) as a rapid, orthogonal confirmatory test alongside sequencing (F006).
4. **Develop conditional/hypomorphic mouse and human iPSC-derived models** (osteoblast, vascular smooth muscle, cochlear, cortical) to interrogate postnatal, tissue-specific mechanisms not accessible in embryonic-lethal knockouts (addressing F002/F007/F009 gaps).
5. **Vascular surveillance protocol:** define evidence-based imaging intervals and intervention thresholds for aneurysm/dissection, given rupture is the leading lethal risk (F003).
6. **Explore trafficking-based therapeutic hypotheses:** given the VPS33B/VIPAR–LH3 axis (F005), test whether enhancing LH3 stability/trafficking or supplying residual GGT activity rescues collagen glycosylation in patient fibroblasts — a first step toward any disease-modifying strategy.
7. **Cross-collagenopathy differential-diagnosis panel:** ensure *PLOD3* is included in Stickler/EDS/EB/Ullrich-CMD gene panels so that BCARD is not missed in patients presenting with overlapping features (F003, F009).

---

*Report compiled from 9 confirmed findings and 25 reviewed papers over 5 investigation iterations. Evidence types: human clinical case reports (PMIDs 40289369, 31129566, 30463024, 36203519, 18834968, 26380979); in vitro/structural (30089812, 37446392, 26380979); mouse model (16467571, 17873278); trafficking/cell biology (27435297); population genomics (gnomAD, supporting F008).*


## Artifacts

- [OpenScientist final report](Bone_Fragility_With_Contractures_Arterial_Rupture_And_Deafness-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bone_Fragility_With_Contractures_Arterial_Rupture_And_Deafness-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012892` (4 mentions) - the report calls it "MONDO"; MONDO calls it **bone fragility with contractures, arterial rupture, and deafness**
- `HP:0002650` (1 mention) - the report calls it "Skeletal sign"; HP calls it **Scoliosis**
- `HP:0002815` (1 mention) - the report calls it "knee-related"; HP calls it **Abnormality of the knee**
- `HP:0000518` (1 mention) - the report calls it "Ocular sign"; HP calls it **Cataract**
- `HP:0011003` (1 mention) - the report calls it "Ocular"; HP calls it **High myopia**
- `HP:0000541` (1 mention) - the report calls it "Ocular"; HP calls it **Retinal detachment**
- `HP:0000407` (1 mention) - the report calls it "Auditory"; HP calls it **Sensorineural hearing impairment**
- `HP:0010490` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal palmar crease morphology**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0000076` (1 mention) - the report calls it "Renal"; HP calls it **Vesicoureteral reflux**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`
- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`
- `CHEBI:24544` (CHEBI_24544) (1 mention) - replaced by `CHEBI:15525`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Neurodevelopmental"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `HP:0008066` (1 mention) - the report calls it "Skin"; HP calls it **Abnormal blistering of the skin**, and lists "Skin bullae" among its other names
- `GO:0006486` (1 mention) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**