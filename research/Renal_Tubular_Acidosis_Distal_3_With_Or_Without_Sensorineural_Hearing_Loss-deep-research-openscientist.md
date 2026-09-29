---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T08:25:47.652887'
end_time: '2026-09-06T08:42:32.961413'
duration_seconds: 1005.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Renal Tubular Acidosis, Distal, 3, With or Without Sensorineural Hearing
    Loss
  mondo_id: MONDO:0011268
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
citation_count: 21
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 5
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:23114896
  - PMID:10973252
  relevance_assessed: 25
  on_topic: 18
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 0
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0002900
    reported_labels:
    - Lab abnormality
    ontology_label: Hypokalemia
  - term_id: HP:0000121
    reported_labels:
    - Imaging/clinical
    ontology_label: Nephrocalcinosis
  - term_id: HP:0002150
    reported_labels:
    - Lab abnormality
    ontology_label: Hypercalciuria
  - term_id: HP:0003128
    reported_labels:
    - Lab abnormality
    ontology_label: Lactic acidosis
  - term_id: HP:0000787
    reported_labels:
    - Clinical
    ontology_label: Kidney stone
  - term_id: HP:0002748
    reported_labels:
    - Clinical/imaging
    ontology_label: Rickets
  - term_id: HP:0000103
    reported_labels:
    - Symptom
    ontology_label: Polyuria
  - term_id: HP:0002013
    reported_labels:
    - Symptom
    ontology_label: Vomiting
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0012622
    reported_labels:
    - Lab/clinical
    ontology_label: Chronic kidney disease
  - term_id: CHEBI:15378
    reported_labels:
    - CHEBI:** proton/hydron
    ontology_label: hydron
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
  path: Renal_Tubular_Acidosis_Distal_3_With_Or_Without_Sensorineural_Hearing_Loss-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Renal_Tubular_Acidosis_Distal_3_With_Or_Without_Sensorineural_Hearing_Loss-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Tubular Acidosis, Distal, 3, With or Without Sensorineural Hearing Loss
- **MONDO ID:** MONDO:0011268 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Renal Tubular Acidosis, Distal, 3, With or Without Sensorineural Hearing Loss** covering all of the
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

# Renal Tubular Acidosis, Distal, 3, With or Without Sensorineural Hearing Loss (dRTA-3)

**Disease knowledge-base report**
**MONDO:0011268 · OMIM #602722 · Gene: ATP6V0A4 (HGNC:865) · Category: Mendelian, autosomal recessive**

---

## Summary

Renal tubular acidosis, distal, type 3, with or without sensorineural hearing loss (**dRTA-3**) is a rare Mendelian, autosomal-recessive kidney tubular disorder caused by **biallelic loss-of-function mutations in *ATP6V0A4*** on chromosome 7q34. *ATP6V0A4* encodes the **a4 subunit of the membrane-integral V0 domain of the vacuolar-type H⁺-ATPase (V-ATPase)**, a proton pump concentrated on the apical (luminal) membrane of **α-intercalated cells (type A intercalated cells)** in the renal collecting duct. When this pump fails, the distal nephron can no longer secrete protons into the tubular lumen, so the urine cannot be acidified below pH ~5.5 even during systemic acidosis. The result is a lifelong **hyperchloremic, normal-anion-gap metabolic acidosis** with hypokalemia, hypercalciuria, hypocitraturia, nephrocalcinosis, growth failure, and rickets. Because the identical pump also acidifies the endolymph of the inner ear, affected patients may additionally develop **sensorineural hearing loss (SNHL)** — historically thought to be late-onset (hence "with or without SNHL"), but now known to be able to appear in early childhood as well.

The disease is diagnosed biochemically (inappropriately alkaline urine, pH >5.5, during a normal-anion-gap metabolic acidosis, confirmed by ammonium-chloride acid-loading or furosemide/fludrocortisone testing) and molecularly (next-generation sequencing gene panels or whole-exome sequencing targeting *SLC4A1*, *ATP6V1B1*, *ATP6V0A4*, *WDR72*, *FOXI1*, and *CA2*). Treatment is **lifelong oral alkali** (sodium/potassium bicarbonate and citrate); a prolonged-release potassium citrate/potassium bicarbonate formulation (**ADV7103 / Sibnayal**) improves metabolic control, lowers lithogenic risk, and improves bone density, growth and quality of life relative to standard-of-care alkali. Correcting the acidosis does not reverse established hearing loss, so regular audiological follow-up is essential.

dRTA-3 sits within a genetically heterogeneous family of inherited dRTAs. *ATP6V0A4* accounts for roughly 14–24 % of genetically solved cases in recent multicenter cohorts. Its closest genetic sibling, *ATP6V1B1*-associated dRTA (dRTA type 2 with early deafness, OMIM #267300), encodes the B1 subunit of the same pump and typically produces earlier and more frequent hearing loss; nevertheless, hearing status alone does not reliably distinguish the two genes, which is why molecular testing independent of audiometry is recommended. An *Atp6v0a4* knockout mouse faithfully recapitulates the renal biochemistry and the deafness (with an absent endocochlear potential), and also reveals extrarenal a4 expression in bone, nose, eye and skin.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** dRTA-3 is a primary (genetic) form of **distal (type 1) renal tubular acidosis**, defined by the inability of the distal nephron to maximally acidify the urine during systemic metabolic acidosis, owing to dysfunction of the α-intercalated cells of the collecting duct. It presents in infancy/early childhood with failure to thrive, polyuria, metabolic acidosis, hypokalemia and nephrocalcinosis, and may be accompanied by sensorineural hearing loss.

**Key identifiers.**
- **OMIM:** #602722 (phenotype); gene *ATP6V0A4* OMIM 605239
- **MONDO:** MONDO:0011268
- **Gene / HGNC:** *ATP6V0A4*, HGNC:865; NCBI Gene 50617; Ensembl ENSG00000105929; UniProt Q9HBG4; cytoband 7q34
- **Orphanet:** distal renal tubular acidosis, ORPHA:18 (parent term)
- **ICD-10:** N25.89 (disorders resulting from impaired renal tubular function) — no dedicated dRTA-3 code; **ICD-11:** GB90.4 (renal tubular acidosis)
- **MeSH:** Acidosis, Renal Tubular (D000141)

**Synonyms / alternative names.** Recessive distal renal tubular acidosis (rdRTA2); distal RTA with or without sensorineural hearing loss; RTADR (renal tubular acidosis, distal, with deafness); ATP6V0A4-related dRTA. The gene was originally named **ATP6N1B** and described as causing dRTA "with preserved hearing" ([PMID: 10973252](https://pubmed.ncbi.nlm.nih.gov/10973252/)).

**Source of information.** This report is derived from **aggregated disease-level resources** — OMIM, published cohort studies and case series, functional/model-organism studies, and clinical trials — rather than from individual-patient EHR data.

---

### 2. Etiology

**Primary cause — genetic.** dRTA-3 is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function mutations in *ATP6V0A4***. Smith et al. (2000) identified the gene in dRTA kindreds, finding homozygous truncating (nonsense, deletion, splice-site) mutations in 8 of 9 kindreds with (initially) normal audiometry ([PMID: 10973252](https://pubmed.ncbi.nlm.nih.gov/10973252/)). The gene "encodes an 840 amino acid novel kidney-specific isoform of ATP6N1A, the 116-kD non-catalytic accessory subunit of the proton pump." (Finding F001)

**Genetic risk factors.**
- **Causal variants:** loss-of-function alleles in *ATP6V0A4* (nonsense, frameshift, splice-site, and deleterious missense). See Section 4.
- **Modifier genes:** genetic background modifies the *hearing* phenotype. In V-ATPase-deficient mice, a chromosome-13 modifier locus accounts for ~20 % of hearing-threshold variation (Tian et al. 2017, [PMID: 28934385](https://pubmed.ncbi.nlm.nih.gov/28934385/)); the renal acidification defect, by contrast, is fully penetrant. (Finding F010)

**Environmental / demographic risk factors.**
- **Consanguinity / family history** is the dominant demographic risk factor because the disorder is recessive: 23 of 26 kindreds were consanguineous in Stover et al. 2002 ([PMID: 12414817](https://pubmed.ncbi.nlm.nih.gov/12414817/)), and 18 of 39 in Vargas-Poussou et al. 2006 ([PMID: 16611712](https://pubmed.ncbi.nlm.nih.gov/16611712/)). (Finding F012)
- **Sex:** no strong sex bias (≈52 % female in the European cohort), as expected for autosomal recessive inheritance ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/)).
- There are **no established acquired/toxic causes of dRTA-3 itself**; environmental exposures instead cause *secondary/acquired* dRTA that must be distinguished from the genetic disease (Section 13).

**Protective factors.** No specific genetic or environmental protective alleles are established for dRTA-3. The only "modifiers" documented act on the hearing phenotype (above). Early diagnosis and adequate alkali therapy are protective against complications (growth failure, CKD progression, stone disease) but do not modify disease occurrence.

**Gene–environment interactions.** None specifically documented for dRTA-3. The disease is essentially fully genetically determined; environmental factors (e.g., intercurrent illness, dietary acid load) influence the *severity of decompensation* and the ease of achieving metabolic control rather than causing the disease.

---

### 3. Phenotypes

**Renal / systemic phenotypes** (Findings F006, F005):

| Phenotype | Type | HPO term | Onset | Frequency | Notes |
|---|---|---|---|---|---|
| Renal tubular acidosis (distal) | Lab abnormality | HP:0008341 (distal RTA) | Neonatal/infantile | ~100 % | Defining feature |
| Hyperchloremic metabolic acidosis, normal anion gap | Lab abnormality | HP:0001947 / HP:0000114 | Infantile | ~100 % | Persistent |
| Inability to acidify urine (urine pH >5.5) | Lab abnormality | HP:0500018 (abnormal urine pH) | Infantile | ~100 % | Diagnostic hallmark |
| Hypokalemia | Lab abnormality | HP:0002900 | Infantile | ~74 % | Can cause weakness/paralysis |
| Nephrocalcinosis | Imaging/clinical | HP:0000121 | Childhood | 74–88 % | Medullary |
| Hypercalciuria | Lab abnormality | HP:0002150 | Childhood | Common | Lithogenic |
| Hypocitraturia | Lab abnormality | HP:0003128 | Childhood | Common | Lithogenic |
| Nephrolithiasis | Clinical | HP:0000787 | Childhood/adult | ~21 % (higher in SLC4A1) | |
| Failure to thrive / short stature | Clinical sign | HP:0001508 / HP:0004322 | Infantile | ~74–76 % | Mean adult height SDS −0.57 |
| Rickets / metabolic bone disease | Clinical/imaging | HP:0002748 | Childhood | Common | From acidosis + Ca loss |
| Polyuria | Symptom | HP:0000103 | Infantile | Common | |
| Vomiting | Symptom | HP:0002013 | Infantile | Common | |
| Sensorineural hearing loss | Clinical sign | HP:0000407 | Variable (early–adult) | ~22 % (ATP6V0A4) | See below |
| Chronic kidney disease | Lab/clinical | HP:0012622 | Progressive | 35 % children, 82 % adults | Stage ≥2 |

Watanabe (2018) summarizes: "Common clinical features of dRTA include vomiting, failure to thrive, polyuria, hypercalciuria, hypocitraturia, nephrocalcinosis, nephrolithiasis, growth delay, and rickets." ([PMID: 30588151](https://pubmed.ncbi.nlm.nih.gov/30588151/), Finding F006).

**Sensorineural hearing loss (the defining "with or without" feature).** In *ATP6V0A4* disease, SNHL is **less frequent and usually later-onset** than in *ATP6V1B1* disease. Priyadarshini 2025 reported SNHL in 22.2 % of *ATP6V0A4* vs 61.5 % of *ATP6V1B1* patients ([PMID: 40232499](https://pubmed.ncbi.nlm.nih.gov/40232499/), Finding F006); the Indian registry found SNHL "strongly associated with ATP6V1B1 variants (53.8 %)" ([PMID: 42622870](https://pubmed.ncbi.nlm.nih.gov/42622870/)). However, SNHL can be **congenital, early, or progressive** — 7 *ATP6V0A4* probands developed severe early SNHL between 2 months and 10 years ([PMID: 16611712](https://pubmed.ncbi.nlm.nih.gov/16611712/), Finding F008). The hearing loss is frequently associated with **large vestibular aqueduct syndrome (LVAS/EVA)** on imaging ([PMID: 37121229](https://pubmed.ncbi.nlm.nih.gov/37121229/), Finding F009).

**Progression / severity.** The renal acidification defect is stable and lifelong; CKD is slowly progressive. Hearing loss may be stable or progressive. Symptom severity is variable, driven partly by adequacy of metabolic control and (for hearing) genetic background.

**Quality of life.** dRTA and its treatment significantly impact QoL across education/work, social/family life, and emotional/physical well-being; treatment burden (frequent dosing, palatability) is a major contributor, and switching to twice-daily ADV7103 markedly improved QoL (mean satisfaction 9/10) ([PMID: 35346296](https://pubmed.ncbi.nlm.nih.gov/35346296/); [PMID: 33635379](https://pubmed.ncbi.nlm.nih.gov/33635379/), Finding F011).

---

### 4. Genetic / Molecular Information

**Causal gene.** ***ATP6V0A4*** (a.k.a. ATP6N1B, ATP6N2, RTADR, VPP2), 7q34; gene OMIM 605239; disease OMIM #602722. Encodes the **a4 subunit** — an 840-amino-acid, kidney-enriched isoform of the 116-kD non-catalytic membrane subunit of the V-ATPase (Finding F001, F014).

**Pathogenic variants.**
- **Affected gene / IDs:** *ATP6V0A4*, HGNC:865; UniProt Q9HBG4; Ensembl ENSG00000105929 (Finding F014).
- **Variant classification (ACMG/AMP):** the majority of reported disease alleles are **pathogenic / likely pathogenic** truncating variants; deleterious missense variants also occur.
- **Variant types:** **nonsense, frameshift (deletions/insertions), splice-site, and missense.** Smith 2000 found homozygous truncating mutations in 8/9 kindreds ([PMID: 10973252](https://pubmed.ncbi.nlm.nih.gov/10973252/)). Vargas-Poussou 2006 reported 14 new + 5 recurrent *ATP6V0A4* mutations across 21 families ([PMID: 16611712](https://pubmed.ncbi.nlm.nih.gov/16611712/)).
- **Functional consequence:** **loss of function** of the apical proton pump (Findings F004, F008). Batlle & Haque (2012): *ATP6V1B1* and *ATP6V0A4* mutations "cause loss of function of the apical H⁺-ATPase and autosomal recessive dRTA" ([PMID: 23114896](https://pubmed.ncbi.nlm.nih.gov/23114896/)).
- **Origin:** **germline**, biallelic. Not a somatic disorder.
- **Allele frequency:** individual pathogenic alleles are rare in population databases (gnomAD); no single common founder allele is established for *ATP6V0A4*, although recurrent/founder alleles occur in consanguineous populations.

**Modifier genes.** Genetic background modifies the inner-ear phenotype (Chr-13 modifier locus in mice, ~20 % of hearing-threshold variance; Tian 2017 [PMID: 28934385](https://pubmed.ncbi.nlm.nih.gov/28934385/)) (Finding F010).

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification signatures are established for dRTA-3. Not applicable / not available.

**Chromosomal abnormalities.** None characteristic; dRTA-3 is a single-gene disorder, not a copy-number/structural syndrome.

**Molecular assembly context.** The a4 subunit is part of the **membrane-integral V0 domain**; a functional pump requires reversible assembly of the cytosolic **V1 domain** (ATP-hydrolytic, includes B1/*ATP6V1B1*) with V0 (proton-translocating). Eaton et al. 2024 showed the assembly factor **Dmxl1/Rabconnectin-3A** is required for V1–V0 assembly, and intercalated-cell-specific *Dmxl1* knockout produces high urine pH like B1 knockouts: "the V-ATPase domains, V1 and VO, must assemble to produce a functional holoenzyme" ([PMID: 38984989](https://pubmed.ncbi.nlm.nih.gov/38984989/), Finding F014).

---

### 5. Environmental Information

- **Environmental factors:** none cause dRTA-3 (a monogenic disease). Environmental/toxic/drug exposures instead produce *acquired* dRTA (differential diagnosis, Section 13).
- **Lifestyle factors:** dietary acid load and fluid status influence decompensation and stone risk but do not cause the disease.
- **Infectious agents:** not applicable to genetic dRTA-3. (Note: infections such as visceral leishmaniasis can produce acquired acidification defects — a mimic, not the disease itself.)

---

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function mutation in *ATP6V0A4*** (germline) **results in** loss/dysfunction of the a4 subunit of the V0 domain of the vacuolar H⁺-ATPase.
2. Loss of a4 **leads to** failure of V0 assembly/function at the **apical plasma membrane of renal α-intercalated cells**, so a functional proton pump is not delivered to the luminal membrane (inferred to include impaired trafficking/assembly, by analogy to the Dmxl1 assembly requirement).
3. Loss of apical H⁺-ATPase activity **results in** inability to secrete protons (H⁺) into the collecting-duct lumen; the basolateral anion exchanger AE1 (SLC4A1) and cytosolic carbonic anhydrase II remain intact but are functionally uncoupled from proton export.
4. Impaired distal H⁺ secretion **leads to** failure to lower urinary pH below ~5.5 during systemic acidosis and reduced net acid excretion (impaired titratable acid + ammonium excretion).
5. Retained acid **results in** systemic **hyperchloremic, normal-anion-gap metabolic acidosis**.
6. Metabolic acidosis and impaired distal transport **lead to** secondary consequences: renal potassium wasting → **hypokalemia**; buffering of acid by bone → calcium and citrate mobilization → **hypercalciuria + hypocitraturia**; low urinary citrate and high urinary calcium → **nephrocalcinosis / nephrolithiasis**; chronic acid load in growing children → impaired bone mineralization → **rickets, growth failure**; chronic nephrocalcinosis/tubulointerstitial injury → **progressive CKD**.
7. **Branch (inner ear):** the same a4-containing V-ATPase acidifies **endolymph in the cochlea/endolymphatic sac**; its loss **results in** disrupted endolymph ion/pH homeostasis and **loss of the endocochlear potential**, **leading to** sensorineural hearing loss (often associated with enlarged vestibular aqueduct). Onset is variable (early to adult) and modified by genetic background.

**Molecular pathways / biochemistry.** The core defect is in **acid–base transport**, not a canonical signaling cascade. α-intercalated cells "secrete protons into the tubular lumen through H⁺-ATPases functionally coupled to the basolateral anion exchanger 1 (AE1)"; substrate H⁺ and HCO₃⁻ are generated by cytosolic carbonic anhydrase II ([PMID: 23114896](https://pubmed.ncbi.nlm.nih.gov/23114896/), Finding F004). "Dysfunction of intercalated cells in the collecting tubules accounts for all the known genetic causes of dRTA."

**Cellular processes.** Failure of regulated proton secretion / intracellular and luminal pH regulation; secondary tubulointerstitial injury/nephrocalcinosis. In the inner ear, additional pH-dependent processes are implicated (e.g., autophagic dysregulation of hair cells in a V-ATPase-deficient zebrafish model, [PMID: 38277730](https://pubmed.ncbi.nlm.nih.gov/38277730/)).

**Protein dysfunction.** Loss of function of the a4 subunit; the multisubunit holoenzyme cannot translocate protons across the apical membrane (Finding F014).

**Metabolic changes.** Systemic acidosis; secondary bone mineral mobilization; hypocitraturia reflecting proximal citrate reabsorption driven by intracellular acidosis.

**Biochemical abnormality (defining).** An **ion-transporter/proton-pump defect** — the paradigmatic "biochemical abnormality" category for this disease.

**Immune involvement.** None in the primary genetic disease (immune-mediated α-intercalated-cell injury defines an *acquired* mimic — Sjögren's disease, Section 13).

**Ontology suggestions.**
- **GO (biological process):** proton transmembrane transport (GO:1902600); regulation of intracellular pH (GO:0051453).
- **GO (cellular component):** proton-transporting V-type ATPase, V0 domain (GO:0033179); vacuolar proton-transporting V-type ATPase complex (GO:0016471); apical plasma membrane (GO:0016324).
- **CL (cell types):** renal alpha-intercalated cell (CL:1000715); kidney collecting duct intercalated cell (CL:1001432); cochlear hair cell.
- **UBERON:** kidney collecting duct (UBERON:0001232); cochlea (UBERON:0001844); endolymphatic sac (UBERON:0002400); bone (UBERON:0002481).
- **CHEBI:** proton/hydron (CHEBI:15378); bicarbonate (CHEBI:17544); citrate (CHEBI:16947); potassium (CHEBI:29103).

---

### 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** kidney (collecting duct / distal nephron) — UBERON:0001232, UBERON:0002113.
- **Secondary/other primary target:** inner ear (cochlea, endolymphatic sac) — UBERON:0001844, UBERON:0002400.
- **Secondary involvement:** bone/skeleton (rickets, osteopenia; UBERON:0002481); urinary tract (stones); growth axis (short stature).
- **Body systems:** renal/urinary; auditory/nervous (sensory); musculoskeletal; endocrine-metabolic (acid–base).

**Tissue and cell level.**
- **Tissue:** renal collecting-duct epithelium; cochlear sensory/supporting epithelium.
- **Cells:** **renal α-intercalated (type A intercalated) cells** — CL:1000715 / CL:1001432; cochlear hair cells and endolymph-regulating epithelial cells. The *Atp6v0a4* β-galactosidase reporter also revealed developmental expression in **bone, nose, eye and skin** ([PMID: 22872862](https://pubmed.ncbi.nlm.nih.gov/22872862/), Finding F003).

**Subcellular level.** Apical plasma membrane (GO:0016324); V-ATPase V0 domain (GO:0033179); the a4 subunit "localizes almost exclusively to the apical surface of α-intercalated cells" ([PMID: 10973252](https://pubmed.ncbi.nlm.nih.gov/10973252/), Finding F001).

**Localization / lateralization.** Renal involvement is **bilateral** (both kidneys); nephrocalcinosis is bilateral medullary. Hearing loss is typically **bilateral**, often with bilateral enlarged vestibular aqueducts.

---

### 8. Temporal Development

- **Onset:** typically **congenital/infantile** — median presentation age **0.5 years** (range 0–54) in the European cohort ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/), Finding F012). Children with *ATP6V0A4* (and *ATP6V1B1*) variants present earlier than those with *SLC4A1*/*WDR72* ([PMID: 42622870](https://pubmed.ncbi.nlm.nih.gov/42622870/)).
- **Onset pattern:** chronic, often with acute metabolic decompensation during intercurrent illness in infancy.
- **Progression:** the acidification defect is **stable/lifelong**; complications (nephrocalcinosis, CKD, short stature) are **slowly progressive**. CKD stage ≥2 rises from 35 % in children to 82 % in adults ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/), Finding F005).
- **Hearing loss course:** variable — congenital, early, or later-onset/progressive; regular audiological follow-up is essential ([PMID: 37121229](https://pubmed.ncbi.nlm.nih.gov/37121229/), Finding F009).
- **Remission:** none spontaneously; treatment controls (but does not cure) the biochemistry. Critical window: early diagnosis and alkali therapy protect growth and renal function.

---

### 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** ([PMID: 10973252](https://pubmed.ncbi.nlm.nih.gov/10973252/), Finding F001, F012).
- **Penetrance:** **complete** for the renal acidification defect; **variable expressivity/age of onset** for SNHL.
- **Consanguinity:** major contributor — 23/26 kindreds ([PMID: 12414817](https://pubmed.ncbi.nlm.nih.gov/12414817/)), 18/39 ([PMID: 16611712](https://pubmed.ncbi.nlm.nih.gov/16611712/)) (Finding F012).
- **Founder effects:** recurrent alleles occur in specific/consanguineous populations; no single global founder allele established for *ATP6V0A4*.
- **Carrier frequency / precise prevalence:** not firmly established; dRTA overall is a rare disease (Orphanet ORPHA:18).
- **Gene contribution:** *ATP6V0A4* accounts for ~**14.2 %** of solved dRTA in the Indian registry ([PMID: 42622870](https://pubmed.ncbi.nlm.nih.gov/42622870/)) and ~22 % in another cohort; the overall genetic-diagnosis yield in dRTA is ~83 % ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/)).
- **Sex ratio:** approximately equal (~52 % female), consistent with AR inheritance.
- **Geographic distribution:** worldwide; higher observed frequency in populations with high consanguinity. Genetic variant spectrum differs between Western and Asian cohorts (SLC4A1 dominant in India).

---

### 10. Diagnostics

**Biochemical (core criteria).**
- **Hallmark:** inappropriately alkaline urine (**pH >5.5**) in the presence of a **normal-anion-gap (hyperchloremic) metabolic acidosis** ([PMID: 19158053](https://pubmed.ncbi.nlm.nih.gov/19158053/), Finding F007).
- **Confirmatory provocation tests:** **ammonium chloride (NH₄Cl) acid-loading test** — dRTA patients keep urine pH >5.5 during induced acidosis ([PMID: 21464016](https://pubmed.ncbi.nlm.nih.gov/21464016/)); **furosemide (± fludrocortisone) test** — normal controls lower urine pH <5.5, dRTA patients fail (sensitivity ~1.0, specificity ~0.89 vs NH₄Cl; [PMID: 10862634](https://pubmed.ncbi.nlm.nih.gov/10862634/)).
- Supporting labs: hypokalemia, hyperchloremia, low serum bicarbonate, hypercalciuria, hypocitraturia.

**Imaging.** Renal ultrasound/CT for **nephrocalcinosis** and stones; temporal-bone imaging (CT/MRI) for **enlarged vestibular aqueduct** in patients with hearing loss ([PMID: 37121229](https://pubmed.ncbi.nlm.nih.gov/37121229/)).

**Audiology.** Pure-tone audiometry and auditory brainstem response (ABR); the mouse model shows elevated ABR thresholds and absent endocochlear potential ([PMID: 22872862](https://pubmed.ncbi.nlm.nih.gov/22872862/)).

**Genetic testing.** **NGS gene panels or whole-exome sequencing** targeting *SLC4A1*, *ATP6V1B1*, *ATP6V0A4*, *WDR72*, *FOXI1*, *CA2* confirm the molecular subtype; single-gene *ATP6V0A4* testing where phenotype is suggestive. Mutation yield ~83 % ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/), Finding F007). Genetic testing is recommended **independent of hearing status** because hearing does not distinguish *ATP6V0A4* from *ATP6V1B1* ([PMID: 16611712](https://pubmed.ncbi.nlm.nih.gov/16611712/), Finding F008).

**Clinical criteria / differential diagnosis.** No formal society scoring system; diagnosis rests on the biochemical triad plus genetics. Differential includes acquired dRTA and other RTA subtypes (Section 13).

**Screening.** Cascade genetic testing of relatives once the familial variant is known; carrier testing for reproductive counseling.

---

### 11. Outcome / Prognosis

- **Survival:** generally **normal life expectancy** with treatment; dRTA-3 is not primarily life-limiting. (The knockout mouse dies without alkalinization, underscoring the importance of therapy.)
- **Morbidity:** substantial if untreated/undertreated — **CKD stage ≥2 in 35 % of children and 82 % of adults**; nephrocalcinosis 74–88 %; mean adult height SDS −0.57; stunting up to ~75 % in some cohorts ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/); [PMID: 42622870](https://pubmed.ncbi.nlm.nih.gov/42622870/), Findings F005, F006).
- **Hearing:** SNHL is **irreversible** once established; hence audiological monitoring and early hearing intervention.
- **Prognostic factors:** **adequacy of metabolic control is the key modifiable prognostic factor** — adequate control (normal bicarbonate + normocalciuria) was achieved in 51 %, more often in higher-GDP countries (67 % vs 23 %), and was associated with greater height and eGFR ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/), Finding F005). Genotype influences hearing and stone risk.
- **Recovery:** the renal biochemistry is fully correctable with alkali; complications are largely preventable with early, sustained control.

---

### 12. Treatment

**Pharmacotherapy — mainstay: lifelong oral alkali** (NCIT: alkalinizing agent).
- **Sodium bicarbonate / potassium bicarbonate / potassium citrate / sodium citrate.** Median prescribed dose **1.9 (IQR 1.2–3.3) mEq/kg/day** ([PMID: 30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/), Finding F005). Potassium-based alkali is preferred to correct concomitant hypokalemia; citrate additionally reduces stone risk.
- **Potassium supplementation** as needed for hypokalemia.

**Prolonged-release combination (ADV7103 / Sibnayal — potassium citrate + potassium bicarbonate).** EMA-authorized for dRTA. In an open-label non-inferiority trial (n=37), switching from standard of care raised the response rate from **43 % to 90 %** and reduced urine Ca/citrate below the lithogenic threshold in 56 % of prior non-responders ([PMID: 32712761](https://pubmed.ncbi.nlm.nih.gov/32712761/), Finding F011). Over 24 months, bicarbonate/potassium were normal in 69–86 %/83–93 % of patients, adherence ≥75 % in 79 %, and QoL improved by ~89 % with only mild GI adverse events in 17 % ([PMID: 33635379](https://pubmed.ncbi.nlm.nih.gov/33635379/)). Two years of ADV7103 "improved growth and increased spine BMD" (spine BMD z-score p=0.024) ([PMID: 36529656](https://pubmed.ncbi.nlm.nih.gov/36529656/)).

**Supportive / rehabilitative.**
- **Hearing rehabilitation:** hearing aids; cochlear implantation for severe/profound SNHL. Speech/language support in children.
- **Nutrition and growth monitoring;** stone-prevention measures (hydration, citrate).

**Advanced/experimental therapeutics.** No gene, cell, or RNA-based therapy is approved or in trials for dRTA-3; management is entirely metabolic/supportive. Pharmacogenomics: not applicable.

**Treatment strategy.** Early diagnosis → titrate alkali to normalize plasma bicarbonate and urinary calcium/citrate → monitor growth, renal function, nephrocalcinosis, and hearing → multidisciplinary follow-up (nephrology, audiology, endocrinology/growth). NCIT suggestions: Sodium Bicarbonate (NCIT:C287), Potassium Citrate (NCIT:C47679), Potassium Bicarbonate, Cochlear Implantation.

---

### 13. Prevention

- **Primary prevention:** not possible for a monogenic disease; **genetic counseling** for at-risk (especially consanguineous) families, with carrier/cascade testing and options including prenatal or preimplantation genetic diagnosis once the familial variant is known.
- **Secondary prevention:** early biochemical diagnosis and prompt alkali therapy to prevent nephrocalcinosis, CKD progression, growth failure and bone disease.
- **Tertiary prevention:** sustained metabolic control (ADV7103/alkali) to prevent stones, preserve renal function and bone density; early hearing intervention.
- **Immunization / public-health / environmental interventions:** not applicable.

---

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** mouse *Atp6v0a4* (NCBI Gene 140470); the gene is evolutionarily conserved across vertebrates (zebrafish V-ATPase orthologs used as models).
- **Model relevance:** the *Atp6v0a4* knockout mouse is the principal animal model (below). No well-characterized spontaneous companion-animal or wildlife dRTA-3 is established in OMIA for *ATP6V0A4*.
- **Comparative biology:** the α-intercalated-cell proton-secretion mechanism and V-ATPase subunit composition are conserved between human and mouse; the a4/B1 subunits serve the same kidney and inner-ear functions across species (the d2 subunit co-localizes with a4 in intercalated cells and with a3 in osteoclasts — [PMID: 15800125](https://pubmed.ncbi.nlm.nih.gov/15800125/)).
- **Transmission / zoonosis:** not applicable (non-infectious genetic disease).

---

### 15. Model Organisms

**Mouse — *Atp6v0a4*⁻/⁻ knockout** (mammalian; principal model). Recapitulates the human disease: "Atp6v0a4(-/-) mice demonstrated severe metabolic acidosis, hypokalemia, and early nephrocalcinosis," and were "severely hearing-impaired, as shown by elevated auditory brainstem response thresholds and absent endocochlear potential" ([PMID: 22872862](https://pubmed.ncbi.nlm.nih.gov/22872862/), Finding F003). Mice die rapidly unless alkalinized; heterozygotes are normal until acid-challenged. A β-galactosidase reporter revealed developmental a4 expression in bone, nose, eye and skin in addition to kidney and inner ear.
- **Phenotype recapitulation:** excellent for renal biochemistry and deafness/endocochlear-potential loss.
- **Limitations:** high early lethality without alkali; extrarenal expression sites (bone/eye/nose/skin) not obviously symptomatic in humans; hearing phenotype is strongly strain/background dependent.

**Mouse — *Atp6v1b1* models (sibling gene).** MRL-background *Atp6v1b1* mutants show profound hearing loss with enlarged vestibular aqueducts, whereas B6-background knockouts hear normally; a Chr-13 modifier locus explains ~20 % of hearing-threshold variance — a model for the hearing-loss variability of dRTA ([PMID: 28934385](https://pubmed.ncbi.nlm.nih.gov/28934385/), Finding F010).

**Zebrafish — *atp6v1ba*-deficient.** Links V-ATPase-dependent pH imbalance to autophagic dysregulation of inner-ear hair cells ([PMID: 38277730](https://pubmed.ncbi.nlm.nih.gov/38277730/)) — mechanistic model of the deafness component.

**Mouse — intercalated-cell-specific *Dmxl1* knockout.** Demonstrates that V1–V0 assembly (Rabconnectin-3A/Dmxl1-dependent) is required for intercalated-cell V-ATPase function; KO mice have high urine pH like B1 knockouts ([PMID: 38984989](https://pubmed.ncbi.nlm.nih.gov/38984989/), Finding F014).

**Resources:** MGI (mouse), ZFIN (zebrafish), IMPC/IMSR for mutant strains.

---

## Mechanistic Model (synthesis)

```
   ATP6V0A4 biallelic LOF mutation (germline, chr 7q34)
                     │  results in
                     ▼
   Loss of a4 subunit of V-ATPase V0 domain
                     │  leads to (assembly/trafficking failure; V1–V0 must assemble)
                     ▼
   No functional H+-ATPase at APICAL membrane of renal α-intercalated cells
                     │  results in
                     ▼
   Failure of luminal H+ secretion (AE1 + carbonic anhydrase II intact but uncoupled)
                     │  leads to
                     ▼
   Urine cannot acidify (pH >5.5) + ↓ net acid excretion
                     │  results in
                     ▼
   Hyperchloremic NORMAL-ANION-GAP METABOLIC ACIDOSIS  ──┬─► K+ wasting → HYPOKALEMIA
                     │                                    ├─► bone buffering → HYPERCALCIURIA,
                     │                                    │     HYPOCITRATURIA → NEPHROCALCINOSIS/STONES
                     │                                    ├─► impaired bone mineralization → RICKETS,
                     │                                    │     GROWTH FAILURE / SHORT STATURE
                     │                                    └─► chronic tubulointerstitial injury → CKD
                     │
   BRANCH (same pump, inner ear):
   Loss of a4 V-ATPase in cochlea / endolymphatic sac
                     │  results in
                     ▼
   Disrupted endolymph pH/ion homeostasis → LOSS OF ENDOCOCHLEAR POTENTIAL
   (± enlarged vestibular aqueduct)
                     │  leads to
                     ▼
   SENSORINEURAL HEARING LOSS (variable onset; modified by genetic background)
```

**Upstream vs downstream:** the mutation and pump loss are upstream; acidosis is the pivotal intermediate node; hypokalemia, stone disease, bone disease, CKD and hearing loss are downstream branches. **Alkali therapy acts at the acidosis node** — it corrects the renal/skeletal branches but cannot restore inner-ear proton pumping, explaining why hearing loss is not reversed.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [10973252](https://pubmed.ncbi.nlm.nih.gov/10973252/) | ATP6N1B mutations cause recessive dRTA | Identifies *ATP6V0A4* as causal gene; apical α-intercalated-cell localization (F001) |
| [12414817](https://pubmed.ncbi.nlm.nih.gov/12414817/) | Novel ATP6V1B1/ATP6V0A4 mutations, hearing loss | Later-onset SNHL in *ATP6V0A4*; inner-ear expression; consanguinity (F002, F012) |
| [22872862](https://pubmed.ncbi.nlm.nih.gov/22872862/) | *Atp6v0a4* knockout mouse | Model recapitulates renal + hearing phenotype; absent endocochlear potential; extrarenal expression (F003) |
| [23114896](https://pubmed.ncbi.nlm.nih.gov/23114896/) | Genetic causes/mechanisms of dRTA | α-intercalated-cell mechanism; AE1/CAII coupling; LOF (F004) |
| [30773598](https://pubmed.ncbi.nlm.nih.gov/30773598/) | Treatment & long-term outcome (European cohort, n=340) | Alkali dose, metabolic control, CKD, height; 83 % mutation yield (F005, F007, F012) |
| [30588151](https://pubmed.ncbi.nlm.nih.gov/30588151/) | Improving outcomes in dRTA (review) | Core clinical phenotype list (F006) |
| [40232499](https://pubmed.ncbi.nlm.nih.gov/40232499/) | Etiology & outcomes of primary RTA | Genotype-specific SNHL frequency (22.2 % ATP6V0A4) (F006) |
| [16611712](https://pubmed.ncbi.nlm.nih.gov/16611712/) | Early SNHL with ATP6V0A4 | ATP6V0A4 can cause early deafness; test independent of hearing (F008) |
| [37121229](https://pubmed.ncbi.nlm.nih.gov/37121229/) | Hearing loss & gene mutations in dRTA | LVAS association; congenital + progressive hearing loss (F009) |
| [29242249](https://pubmed.ncbi.nlm.nih.gov/29242249/) | FOXI1 acidosis + deafness | FOXI1 upstream regulator; genetic heterogeneity (F010) |
| [28934385](https://pubmed.ncbi.nlm.nih.gov/28934385/) | ATP6V1B1 MRL mice, EVA | Genetic-background modifier of hearing phenotype (F010) |
| [32712761](https://pubmed.ncbi.nlm.nih.gov/32712761/) | ADV7103 comparative trial | Response 43→90 %; lithogenic-risk reduction (F011) |
| [33635379](https://pubmed.ncbi.nlm.nih.gov/33635379/) | ADV7103 24-month study | Sustained control, adherence, QoL (F011) |
| [36529656](https://pubmed.ncbi.nlm.nih.gov/36529656/) | ADV7103 BMD & growth | Spine BMD z-score ↑ (p=0.024), growth improved (F011) |
| [19158053](https://pubmed.ncbi.nlm.nih.gov/19158053/) | dRTA due to primary hyperparathyroidism | Diagnostic criterion; reversible secondary cause (F007, F013) |
| [21464016](https://pubmed.ncbi.nlm.nih.gov/21464016/) | Primary dRTA case report | NH₄Cl acid-loading confirmation (F007) |
| [10862634](https://pubmed.ncbi.nlm.nih.gov/10862634/) | RTA in osteopenia/osteoporosis | Furosemide test performance vs NH₄Cl (F007) |
| [42694869](https://pubmed.ncbi.nlm.nih.gov/42694869/) | Sjögren's dRTA immuno-tubular model | Acquired mimic targeting α-intercalated cells (F013) |
| [42622870](https://pubmed.ncbi.nlm.nih.gov/42622870/) | Indian dRTA registry | ATP6V0A4 = 14.2 % of solved cases; SNHL genotype pattern (F006, F012) |
| [38984989](https://pubmed.ncbi.nlm.nih.gov/38984989/) | Dmxl1 & V-ATPase assembly | V1–V0 assembly requirement; molecular context (F014) |
| [39150521](https://pubmed.ncbi.nlm.nih.gov/39150521/) | WDR72-dRTA | Differential (amelogenesis imperfecta) (F013) |
| [19232111](https://pubmed.ncbi.nlm.nih.gov/19232111/) | Osteopetrosis | CA2 mixed RTA differential (F013) |
| [15800125](https://pubmed.ncbi.nlm.nih.gov/15800125/) | V-ATPase d2 subunit | Subunit co-localization (a4 in kidney, a3 in osteoclasts) |
| [38277730](https://pubmed.ncbi.nlm.nih.gov/38277730/) | Zebrafish V-ATPase & hair-cell autophagy | Inner-ear mechanistic model |

---

## Limitations and Knowledge Gaps

1. **Epidemiology is imprecise.** No robust population prevalence, incidence, or *ATP6V0A4* carrier frequency exists; cohorts are consanguinity-enriched and geographically skewed, so genotype proportions (14–24 %) are cohort-dependent.
2. **Hearing-loss determinants are incompletely understood.** Why some *ATP6V0A4* patients develop early SNHL and others none is unexplained; modifier evidence is largely from mouse strains, and the human genetic modifiers are unmapped.
3. **No dRTA-3-specific natural-history registry** with long-term renal, auditory and skeletal endpoints stratified by genotype and treatment adequacy.
4. **No omics data specific to dRTA-3** (transcriptomic/proteomic/metabolomic signatures) were identified; molecular-profiling sections are largely not applicable.
5. **No causal/curative therapy.** Gene- and cell-based approaches are absent; alkali corrects biochemistry but not hearing loss.
6. **Genotype–phenotype correlation** for individual *ATP6V0A4* variants (e.g., missense vs truncating) is not well resolved.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an *ATP6V0A4*-specific longitudinal registry** capturing age-stratified audiometry, temporal-bone imaging (EVA), renal function, growth and treatment adequacy to define natural history and genotype–phenotype correlations.
2. **Prospective audiological surveillance protocol** from diagnosis to detect and time SNHL onset in *ATP6V0A4* patients, testing whether early metabolic control alters hearing trajectory.
3. **Functional variant characterization** (in vitro assembly/trafficking/proton-pump assays; AlphaFold-guided structural interpretation) to reclassify VUS and correlate residual function with phenotype severity.
4. **Map human modifiers of the hearing phenotype** by GWAS/whole-genome analysis within dRTA cohorts, building on the murine Chr-13 modifier finding.
5. **Real-world comparative-effectiveness study of ADV7103 vs conventional alkali** on hard endpoints (CKD progression, stone events, final adult height, BMD) across health-economic settings.
6. **Explore inner-ear-directed or gene-based strategies** (e.g., AAV delivery of *ATP6V0A4* to cochlea) using the knockout mouse/zebrafish models to address the currently irreversible hearing loss.

---

### Consensus Answer

Renal tubular acidosis, distal, 3, with or without sensorineural hearing loss (dRTA-3; OMIM #602722, MONDO:0011268) is a rare autosomal-recessive disorder caused by biallelic loss-of-function mutations in *ATP6V0A4* (7q34), encoding the a4 subunit of the apical vacuolar H⁺-ATPase of renal α-intercalated cells; loss of this proton pump abolishes distal urinary acidification, producing hyperchloremic normal-anion-gap metabolic acidosis with hypokalemia, hypercalciuria/hypocitraturia, nephrocalcinosis, growth failure and rickets, plus variable (often later-onset) sensorineural hearing loss because the same pump acidifies inner-ear endolymph. It is diagnosed by inappropriately alkaline urine (pH >5.5) during acidosis (confirmed by acid-loading/furosemide testing) plus NGS gene-panel sequencing, and managed lifelong with oral alkali (bicarbonate/citrate, including prolonged-release ADV7103/Sibnayal), which corrects the biochemistry and improves growth, bone and quality of life but does not reverse established hearing loss.


## Artifacts

- [OpenScientist final report](Renal_Tubular_Acidosis_Distal_3_With_Or_Without_Sensorineural_Hearing_Loss-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Renal_Tubular_Acidosis_Distal_3_With_Or_Without_Sensorineural_Hearing_Loss-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 25 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23114896` *(abstract only)*: "cause loss of function of the apical H⁺-ATPase and autosomal recessive dRTA"
  - closest text in source: "Mutations in ATP6V1B1, encoding the B-subtype unit of the apical H(+) ATPase, and ATP6V0A4, encoding the a-subtype unit, lead to the loss of function of the apical H(+) ATPase and are usually responsible for patients with autosomal recessive dRTA often associated with early or late sensorineural deafness"
- `PMID:10973252` *(abstract only)*: "localizes almost exclusively to the apical surface of α-intercalated cells"
  - closest text in source: "Immunofluorescence studies in human kidney cortex revealed that ATP6N1B localizes almost exclusively to the apical surface of -intercalated cells"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002900` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypokalemia**
- `HP:0000121` (1 mention) - the report calls it "Imaging/clinical"; HP calls it **Nephrocalcinosis**
- `HP:0002150` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypercalciuria**
- `HP:0003128` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Lactic acidosis**
- `HP:0000787` (1 mention) - the report calls it "Clinical"; HP calls it **Kidney stone**
- `HP:0002748` (1 mention) - the report calls it "Clinical/imaging"; HP calls it **Rickets**
- `HP:0000103` (1 mention) - the report calls it "Symptom"; HP calls it **Polyuria**
- `HP:0002013` (1 mention) - the report calls it "Symptom"; HP calls it **Vomiting**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0012622` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Chronic kidney disease**
- `CHEBI:15378` (1 mention) - the report calls it "CHEBI:** proton/hydron"; CHEBI calls it **hydron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008341` (1 mention) - the report calls it "distal RTA"; HP calls it **Distal renal tubular acidosis**
- `HP:0500018` (1 mention) - the report calls it "abnormal urine pH"; HP calls it **Abnormal cardiac exercise stress test**, and lists "Abnormal exercise test" among its other names
- `UBERON:0001232` (2 mentions) - the report calls it "UBERON:** kidney collecting duct"; UBERON calls it **collecting duct of renal tubule**, and lists "kidney collecting duct" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.