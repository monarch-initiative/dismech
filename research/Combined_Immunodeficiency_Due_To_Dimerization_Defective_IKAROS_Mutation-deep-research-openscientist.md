---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T17:35:38.853622'
end_time: '2026-10-15T18:03:42.219957'
duration_seconds: 1683.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Immunodeficiency Due To Dimerization Defective IKAROS Mutation
  mondo_id: MONDO:0979288
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
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 16
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:24297995
  - PMID:34920454
  relevance_assessed: 28
  on_topic: 16
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 10
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0979288
    reported_labels:
    - Mondo
    ontology_label: combined immunodeficiency due to dimerization defective IKAROS
      mutation
  - term_id: HP:0001873
    reported_labels:
    - Lab/clinical sign
    ontology_label: Thrombocytopenia
  - term_id: HP:0001875
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0002719
    reported_labels:
    - Symptom
    ontology_label: Recurrent infections
  - term_id: HP:0006727
    reported_labels:
    - Neoplasm
    ontology_label: T-cell acute lymphoblastic leukemias
  - term_id: HP:0004812
    reported_labels:
    - Neoplasm
    ontology_label: B Acute Lymphoblastic Leukemia
  - term_id: HP:0002960
    reported_labels:
    - Clinical sign
    ontology_label: Autoimmunity
  - term_id: HP:0005415
    reported_labels:
    - abnormal T-cell count
    ontology_label: Decreased total CD8+ T cell proportion
  - term_id: HP:0010976
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total B cell count
  - term_id: NCIT:C564
    reported_labels:
    - Immunoglobulin Therapy
    ontology_label: Ifosfamide
  - term_id: NCIT:C15431
    reported_labels:
    - Immunotherapy
    ontology_label: Hematopoietic Cell Transplantation
  - term_id: NCIT:C105558
    reported_labels:
    - Allogeneic HSCT
    ontology_label: TPI1 wt Allele
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Immunodeficiency_Due_To_Dimerization_Defective_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Immunodeficiency_Due_To_Dimerization_Defective_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due To Dimerization Defective IKAROS Mutation
- **MONDO ID:** MONDO:0979288 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due To Dimerization Defective IKAROS Mutation** covering all of the
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

# Combined Immunodeficiency Due To Dimerization-Defective IKAROS Mutation — Comprehensive Disease Report

**MONDO ID:** MONDO:0979288 | **Category:** Mendelian (autosomal dominant inborn error of immunity)
**Causal gene:** *IKZF1* (IKAROS), 7p12.2 | **Report compiled from 5 discovery iterations, 9 confirmed findings, 35 reviewed papers**

---

## Summary

**Combined Immunodeficiency due to Dimerization-Defective IKAROS Mutation** is a rare, autosomal-dominant inborn error of immunity (IEI) caused by germline heterozygous variants in the **C-terminal dimerization domain (zinc fingers 5–6)** of the transcription factor **IKAROS**, encoded by *IKZF1* on chromosome 7p12.2. These "dimerization-defective" (DD) variants disrupt the ability of IKAROS to form homodimers and heterodimers (with family members AIOLOS/IKZF3 and HELIOS/IKZF2). Because the functional unit of IKAROS is a dimer and the mutant protein does not sequester the wild-type allele, the dominant consequence is **haploinsufficiency** — roughly a halving of functional IKAROS dosage — rather than a dominant-negative effect ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)).

IKAROS is a master regulator of lymphoid and myeloid development and a potent tumor suppressor. Loss of its dimerization function impairs several downstream mechanisms that all depend on an intact C-terminal domain: **pericentromeric heterochromatin targeting, protein stability, sumoylation, and recruitment of the NuRD chromatin-remodeling/deacetylase complex**. The net effect is defective B- and T-lymphopoiesis that branches into a characteristic **three-axis disorder**: (1) **combined immunodeficiency / hypogammaglobulinemia** with recurrent and opportunistic infections (including *Pneumocystis jirovecii*); (2) **immune dysregulation / autoimmunity** with autoimmune cytopenias and Evans syndrome; and (3) **predisposition to lymphoid malignancy** (T-cell acute lymphoblastic leukemia, B-ALL, Burkitt lymphoma). The condition shows **incomplete penetrance and variable expressivity** — some variant carriers remain asymptomatic or recover spontaneously ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/), [PMID: 36433803](https://pubmed.ncbi.nlm.nih.gov/36433803/)).

Knowledge of this entity derives almost entirely from **aggregated small case series and mechanistic functional studies**, not from large registries or EHR cohorts. The landmark description (Kuehn et al., *Blood* 2021) reported 4 unrelated families. Management ranges from supportive immunoglobulin replacement and anti-infective prophylaxis to **curative allogeneic hematopoietic stem cell transplantation (HSCT)** for severe or malignant disease. Below, each of the template's 15 sections is addressed in full, with primary-literature citations and suggested ontology terms for knowledge-base population.

---

## Key Findings (with evidence)

### Finding 1 — The disease is defined by germline heterozygous C-terminal dimerization-domain *IKZF1* variants acting via haploinsufficiency

Kuehn et al. (*Germline IKAROS dimerization haploinsufficiency causes hematologic cytopenias and malignancies*, *Blood* 2021) described **4 germline heterozygous IKAROS variants affecting the C-terminal dimerization domain (zinc fingers 5–6) in 4 unrelated families**. The key mechanistic distinction from other *IKZF1* disease classes is that these variants act by **dimerization haploinsufficiency** — they disrupt homo-/heterodimerization (completely or partially) but **do not affect wild-type allele function**, ruling out a classic dominant-negative mechanism.

> "Herein, we describe 4 germline heterozygous IKAROS variants affecting its C-terminal dimerization domain, via haploinsufficiency, in 4 unrelated families." — [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)

IKAROS-associated disease is now formally classified into **four mechanistic classes depending on protein expression and functional defect: haploinsufficiency, dimerization-defective, dominant-negative, and gain-of-function** ([PMID: 36433803](https://pubmed.ncbi.nlm.nih.gov/36433803/)). The dimerization-defective class is the subject of this report.

> "can be classified through four different mechanisms of action depending on the protein expression and its functional defects: haploinsufficiency, dimerization defective, dominant negative, and gain of function" — [PMID: 36433803](https://pubmed.ncbi.nlm.nih.gov/36433803/)

### Finding 2 — Characteristic presentation: hematologic cytopenias/Evans syndrome and lymphoid malignancy, with incomplete penetrance

In the Kuehn cohort, index patients presented with **cytopenias (thrombocytopenia, anemia, neutropenia)/Evans syndrome** and **malignancies (T-ALL, Burkitt lymphoma)**.

> "Index patients presented with hematologic disease consisting of cytopenias (thrombocytopenia, anemia, neutropenia)/Evans syndrome and malignancies (T-cell acute lymphoblastic leukemia, Burkitt lymphoma)." — [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)

> "display dimerization haploinsufficiency and incomplete clinical penetrance" — [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)

The broader IKAROS-associated disease spectrum spans **susceptibility to infection, autoimmunity/immune dysregulation, allergy, and malignancy** ([PMID: 36433803](https://pubmed.ncbi.nlm.nih.gov/36433803/), [PMID: 33392855](https://pubmed.ncbi.nlm.nih.gov/33392855/)).

### Finding 3 — The dimerization defect disrupts four downstream regulatory mechanisms

DD mutants disrupt IKAROS homo- and heterodimerization and secondarily impair **sumoylation, protein stability, and recruitment of the NuRD (nucleosome remodeling and deacetylase) complex** — mechanisms that are *not* affected by N-terminal DNA-binding defects.

> "they alter key mechanisms of IKAROS gene regulation, including sumoylation, protein stability, and the recruitment of the nucleosome remodeling and deacetylase complex" — [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)

Pericentromeric heterochromatin targeting of IKAROS requires **both** the N-terminal DNA-binding zinc-finger domain **and** the C-terminal dimerization domain:

> "targeting was dependent on the amino-terminal DNA-binding zinc finger domain and carboxy-terminal dimerization domain of Ikaros" — [PMID: 10970879](https://pubmed.ncbi.nlm.nih.gov/10970879/)

IKAROS protein stability is independently regulated by its C-terminal dimerization domain and an N-terminal stability-associated region ([PMID: 40024461](https://pubmed.ncbi.nlm.nih.gov/40024461/)).

### Finding 4 — Mouse models establish IKAROS as an essential lymphoid regulator and potent tumor suppressor

Mouse *Ikzf1* (NCBI Gene 22778) models show IKAROS is "a potent tumor suppressor and hematopoietic regulator" ([PMID: 26314708](https://pubmed.ncbi.nlm.nih.gov/26314708/)); loss in developing lymphoid cells causes leukemia and IKAROS is required for normal thymic T-cell development ([PMID: 30635395](https://pubmed.ncbi.nlm.nih.gov/30635395/)). Individual zinc fingers have **separable functions** — mice lacking finger 1 or finger 4 show distinct subsets of null defects, and **finger 4 is selectively required for tumor suppression**:

> "finger 4 was selectively required for tumor suppression" — [PMID: 24013668](https://pubmed.ncbi.nlm.nih.gov/24013668/)

IKAROS is "absolutely required for pre-B cell differentiation by attenuating IL-7 signals" ([PMID: 24297995](https://pubmed.ncbi.nlm.nih.gov/24297995/)) and is a negative regulator of B1-cell development ([PMID: 26841869](https://pubmed.ncbi.nlm.nih.gov/26841869/)). Targeted deletion of *Ikzf1* is sufficient to transform Lmo2-dependent T-ALL to oncogene independence ([PMID: 33483615](https://pubmed.ncbi.nlm.nih.gov/33483615/)).

### Finding 5 — Allogeneic HSCT is a curative option for severe disease

> "HCT was well-tolerated achieving full engraftment in both patients receiving reduced intensity, matched unrelated donor grafts, with no severe acute or chronic graft-vs-host-disease, and in remission from their diseases 2.5 and 4 years post-HCT" — [PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/)

A patient with *IKZF1*-associated CVID, autoimmune hemolytic anemia, and pancytopenia also underwent HSCT ([PMID: 33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/)). Otherwise, standard management includes **immunoglobulin replacement and anti-infective (including *Pneumocystis jirovecii*) prophylaxis** ([PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/), [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/)).

### Finding 6 — DD variants skew T cells toward reduced naïve / increased memory — distinct from DN variants

> "Patients with IKZF1 haploinsufficiency (HI) or dimerization-defective (DD) variants show reduced naive and increased memory T cells, while dominant-negative (DN) mutations result in the opposite phenotype." — [PMID: 41424385](https://pubmed.ncbi.nlm.nih.gov/41424385/)

IKAROS regulates **HNRNPLL**, the master regulator of CD45 isoform splicing that defines CD45RA+/naïve vs CD45RO+/memory phenotypes, acting at both thymic and post-thymic levels ([PMID: 41424385](https://pubmed.ncbi.nlm.nih.gov/41424385/)). By contrast, DN variants produce mostly naïve T cells unable to evolve into effector memory cells ([PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/)).

### Finding 7 — IKAROS is a six-zinc-finger transcription factor: ZF1–4 bind DNA, ZF5–6 mediate dimerization

> "IKAROS, encoded by IKZF1, is a six zinc-finger (ZF) transcription factor integral to lymphocyte development and function. IKZF1 mutations affecting DNA-binding (ZF1-4) and dimerization (ZF5-6) have been extensively reported and result in human disease." — [PMID: 40024461](https://pubmed.ncbi.nlm.nih.gov/40024461/)

Key identifiers: **HGNC:13176; gene OMIM \*603023; UniProt Q13422; chromosome 7p12.2.** Haploinsufficient DNA-binding-domain disease maps to OMIM *Common variable immunodeficiency 13* (CVID13, #616873); the dimerization-defective combined immunodeficiency entity is catalogued as **MONDO:0979288**.

### Finding 8 — >70 germline variants reported; critical dimerization residues mapped; somatic deletions cause dominant-negative Ik6 in leukemia

> "To date, >70 IKAROS germ line heterozygous variants have been reported in patients with primary immunodeficiency (PID)/inborn errors of immunity (IEI) and leukemia" — [PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)

> "We also conducted an in-depth examination of the C-terminal dimerization domain using alanine-scanning mutagenesis to identify amino acids critical for dimerization and other functions." — [PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)

Systematic in-vitro testing of 81 variants (33 patient-detected germline VUS + 48 laboratory dimerization-domain mutations) identified residues critical for dimerization; 15 patient variants and ≥21 laboratory mutations impaired IKAROS function ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)). Separately, **somatic** focal 7p12 *IKZF1* deletions are the most frequent copy-number alteration in BCR-ABL1-positive ALL (80/106, 75%), and the Δ4-7 deletion produces a dominant-negative cytoplasmic isoform (Ik6):

> "The most frequent somatic copy number alteration was a focal deletion on 7p12 of IKZF1, which encodes the transcription factor Ikaros and was identified in 80 (75%) of 106 patients." — [PMID: 19589926](https://pubmed.ncbi.nlm.nih.gov/19589926/)

### Finding 9 — Integrated three-axis disease model

Germline heterozygous C-terminal (ZF5–6) *IKZF1* variants → loss of dimerization → ~50% functional IKAROS loss → impaired pericentromeric targeting, reduced protein stability, disrupted sumoylation and NuRD recruitment → defective B/T lymphopoiesis, branching into (A) combined immunodeficiency, (B) autoimmunity/cytopenias, and (C) tumor-suppressor loss driving malignancy.

> "These dimerization defective mutants disrupt homo- and heterodimerization in a complete or partial manner, but they do not affect the wild-type allele function." — [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Combined Immunodeficiency due to Dimerization-Defective IKAROS Mutation is a monogenic (Mendelian) inborn error of immunity caused by germline heterozygous variants in the C-terminal dimerization domain (zinc fingers 5–6) of *IKZF1*/IKAROS. It belongs to the family of **IKAROS-associated diseases**, which span common variable immunodeficiency (CVID), combined immunodeficiency (CID), autoimmunity/immune dysregulation, and hematologic malignancy. The DD subtype is mechanistically a **haploinsufficiency** disorder ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/), [PMID: 36433803](https://pubmed.ncbi.nlm.nih.gov/36433803/)).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| Mondo | MONDO:0979288 |
| Gene | *IKZF1* (IKAROS); HGNC:13176; NCBI Gene 10320; UniProt Q13422 |
| Gene OMIM | \*603023 |
| Related phenotype OMIM | CVID13 #616873 (DNA-binding haploinsufficiency class) |
| Cytoband | 7p12.2 |
| MeSH | IKZF1 protein, human; Primary Immunodeficiency Diseases |
| ICD-11 | 4A00 (Primary immunodeficiencies, class) |

**Synonyms / alternative names.** Germline IKAROS dimerization haploinsufficiency; dimerization-defective IKAROS/IKZF1 deficiency; IKZF1-related combined immunodeficiency (dimerization-defective class); IKAROS-associated disease, dimerization-defective subtype.

**Information source.** Derived from **aggregated disease-level resources and small case series/functional studies** (e.g., 4 families in [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)), not from EHR/registry-scale individual-patient data.

### 2. Etiology

**Primary cause — genetic.** Germline heterozygous missense (and occasionally truncating) variants in the C-terminal dimerization domain (ZF5–6) of *IKZF1*. These disrupt homo-/heterodimerization and act by **haploinsufficiency** (no dominant-negative sequestration of the wild-type allele) ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)).

**Genetic risk factors.** The causal variant itself is the risk factor. Over 70 germline *IKZF1* variants are reported across IEI/leukemia; a subset in ZF5–6 cause the DD phenotype ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)). Modifier genes are not formally defined, but functional partners **AIOLOS/IKZF3** and **HELIOS/IKZF2** (dimerization partners) and **PAX5, RUNX1, ETV6** (co-regulated transcription-factor network in lymphoid leukemia) are mechanistically relevant ([PMID: 34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/), [PMID: 34920454](https://pubmed.ncbi.nlm.nih.gov/34920454/), [PMID: 31381561](https://pubmed.ncbi.nlm.nih.gov/31381561/), [PMID: 36764385](https://pubmed.ncbi.nlm.nih.gov/36764385/)).

**Environmental risk / protective factors.** No established environmental risk or protective factors; the disease is monogenic. Infection exposure determines clinical expression (infection susceptibility) but is not causal of the genotype. No protective dietary or lifestyle factors are documented.

**Gene–environment interactions.** Not formally characterized. The incomplete penetrance implies unidentified genetic and/or environmental modifiers; infectious burden and immune challenge likely influence which carriers manifest and which axis (infection, autoimmunity, malignancy) predominates. This is **inferred**, not demonstrated.

### 3. Phenotypes

Phenotypes are drawn from the Kuehn cohort and the broader IKAROS-disease literature. Frequencies are qualitative given small cohorts.

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Thrombocytopenia | Lab/clinical sign | HP:0001873 | Childhood | Variable–severe | Common (index cases) |
| Anemia / autoimmune hemolytic anemia | Lab/clinical sign | HP:0001903 / HP:0004870 | Childhood | Variable | Common |
| Neutropenia | Lab abnormality | HP:0001875 | Childhood | Variable | Reported |
| Evans syndrome (combined AIHA + ITP) | Clinical syndrome | HP:0004870 + HP:0001873 | Childhood | Moderate–severe | Characteristic |
| Hypogammaglobulinemia / CVID-like | Lab abnormality | HP:0002720 / HP:0005387 | Childhood–adult | Variable | Common |
| Recurrent bacterial/viral infections | Symptom | HP:0002719 | Childhood | Variable | Common |
| Opportunistic infection (*Pneumocystis jirovecii* pneumonia) | Clinical sign | HP:0002090 (pneumonia) | Childhood | Severe | Prominent in DN; reported in CID |
| T-ALL | Neoplasm | HP:0006727 | Childhood | Severe | Index cases |
| B-ALL | Neoplasm | HP:0004812 | Childhood | Severe | Reported |
| Burkitt lymphoma | Neoplasm | HP:0012190 (non-Hodgkin lymphoma) | Childhood | Severe | Index case |
| Autoimmunity / immune dysregulation (SLE-like, neutrophilic dermatosis) | Clinical sign | HP:0002960 | Childhood | Variable | Reported ([PMID: 38413050](https://pubmed.ncbi.nlm.nih.gov/38413050/)) |
| Reduced naïve / increased memory T cells | Lab (immunophenotype) | HP:0005415 (abnormal T-cell count) | Congenital/childhood | — | DD-characteristic ([PMID: 41424385](https://pubmed.ncbi.nlm.nih.gov/41424385/)) |
| Reduced B cells | Lab abnormality | HP:0010976 | Congenital–childhood | Variable | Common |
| Low TREC on newborn screening (SCID-like) | Lab abnormality | — | Neonatal | Variable (may recover) | Reported ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)) |

**Severity/progression.** Highly **variable** with **incomplete penetrance**; some carriers are asymptomatic, and spontaneous recovery of T-cell output has been documented in a haploinsufficiency case ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)). Malignancy risk is lifelong, warranting surveillance ([PMID: 38413050](https://pubmed.ncbi.nlm.nih.gov/38413050/)).

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36 data exist. QoL is impaired by chronic infection burden, need for lifelong immunoglobulin replacement/prophylaxis, autoimmune cytopenia management, and the morbidity/mortality of malignancy and HSCT.

### 4. Genetic / Molecular Information

**Causal gene.** *IKZF1* (IKAROS), 7p12.2; six C2H2 zinc-finger transcription factor. ZF1–4 (N-terminal) bind DNA; ZF5–6 (C-terminal) mediate dimerization ([PMID: 40024461](https://pubmed.ncbi.nlm.nih.gov/40024461/)).

**Pathogenic variants.**
- **Affected gene/IDs:** IKZF1, HGNC:13176, UniProt Q13422.
- **Classification:** Pathogenic / likely pathogenic for functionally validated DD variants; many remain **VUS** pending functional testing. Systematic functional assays (dimerization, DNA-binding, pericentromeric localization, protein stability) are used to reclassify VUS ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)).
- **Variant type:** Predominantly **missense** within ZF5–6; truncating/nonsense variants (e.g., p.C182\* in the haploinsufficiency class) also occur ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)).
- **Allele frequency:** Ultra-rare / absent in gnomAD (consistent with high-penetrance disease variants, though penetrance is incomplete).
- **Origin:** **Germline** (de novo or inherited). Distinct from **somatic** *IKZF1* deletions in leukemia ([PMID: 19589926](https://pubmed.ncbi.nlm.nih.gov/19589926/)).
- **Functional consequence:** **Loss of function via haploinsufficiency** (DD class) — in contrast to dominant-negative (e.g., N159 DNA-binding variants, [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/)) and gain-of-function classes.

**Modifier genes.** *IKZF3* (AIOLOS) and *IKZF2* (HELIOS) as dimerization partners; aberrant partner variants (e.g., *IKZF3* G159R) cause overlapping disease by "heterodimeric interference" ([PMID: 34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/), [PMID: 34920454](https://pubmed.ncbi.nlm.nih.gov/34920454/)).

**Epigenetic information.** IKAROS itself is an epigenetic regulator (NuRD/HDAC1 recruitment, H3K27me3 heterochromatin formation, enhancer/super-enhancer regulation, pioneering activity) — see Section 6. Disease-specific DNA-methylation signatures are not established.

**Chromosomal abnormalities.** Large-scale germline cytogenetic abnormalities are not characteristic of this entity; the relevant copy-number event (focal 7p12 *IKZF1* deletion) is **somatic** and leukemia-associated ([PMID: 19589926](https://pubmed.ncbi.nlm.nih.gov/19589926/)).

### 5. Environmental Information

No established environmental, toxic, lifestyle, or infectious **causes**. The disease is genetic. Infectious agents (bacteria, viruses, *Pneumocystis jirovecii*, fungi) act as **consequences/triggers of clinical manifestation** given the underlying immunodeficiency, not as etiologic agents ([PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/), [PMID: 33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/)). NCBI Taxonomy: *Pneumocystis jirovecii* (txid42068).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **germline heterozygous variant** arises in the C-terminal dimerization domain (ZF5–6) of *IKZF1* → **leads to** a mutant IKAROS protein that cannot form stable homodimers or heterodimers (with AIOLOS/HELIOS) ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)).
2. Loss of dimerization → **results in** ~50% reduction of functional IKAROS (haploinsufficiency); the wild-type allele is unaffected (not dominant-negative) ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)).
3. Reduced functional IKAROS → **impairs** pericentromeric heterochromatin targeting (which requires both ZF1–4 and ZF5–6), **reduces** protein stability, and **disrupts** sumoylation and NuRD/HDAC1 complex recruitment ([PMID: 10970879](https://pubmed.ncbi.nlm.nih.gov/10970879/), [PMID: 40024461](https://pubmed.ncbi.nlm.nih.gov/40024461/), [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)).
4. Disrupted chromatin regulation → **deregulates** IKAROS target-gene programs, including enhancer/super-enhancer activation, heterochromatin (H3K27me3) formation, and attenuation of IL-7 and type-I-IFN signaling ([PMID: 31073152](https://pubmed.ncbi.nlm.nih.gov/31073152/), [PMID: 40555735](https://pubmed.ncbi.nlm.nih.gov/40555735/), [PMID: 24297995](https://pubmed.ncbi.nlm.nih.gov/24297995/), [PMID: 30635395](https://pubmed.ncbi.nlm.nih.gov/30635395/)).
5. Deregulated programs → **impair** B- and T-lymphopoiesis and skew T cells toward reduced naïve / increased memory (via HNRNPLL/CD45 splicing) ([PMID: 41424385](https://pubmed.ncbi.nlm.nih.gov/41424385/)).
6. The lymphopoiesis defect **branches** into three clinical axes:
   - **(A) Immunodeficiency** → hypogammaglobulinemia, low B cells, recurrent + opportunistic (*Pneumocystis*) infection ([PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/), [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/)).
   - **(B) Immune dysregulation** → derepressed proinflammatory/type-I-IFN programs → autoimmune cytopenias/Evans syndrome, neutrophilic dermatosis ([PMID: 30635395](https://pubmed.ncbi.nlm.nih.gov/30635395/), [PMID: 38413050](https://pubmed.ncbi.nlm.nih.gov/38413050/)).
   - **(C) Tumor-suppressor loss** → failure of heterochromatin/enhancer control (EZH2/HDAC1/H3K27me3) → T-ALL, B-ALL, Burkitt lymphoma ([PMID: 24013668](https://pubmed.ncbi.nlm.nih.gov/24013668/), [PMID: 40555735](https://pubmed.ncbi.nlm.nih.gov/40555735/), [PMID: 33483615](https://pubmed.ncbi.nlm.nih.gov/33483615/)).

**Molecular pathways.** NuRD/Mi-2 chromatin remodeling + HDAC1 deacetylation; EZH2/PRC2 H3K27me3 facultative heterochromatin; IL-7 receptor signaling (attenuated by IKAROS during pre-B differentiation); type-I-IFN response (repressed by IKAROS); enhancer/super-enhancer landscape with IKAROS pioneering activity.

**Cellular processes.** Lymphocyte differentiation, pericentromeric heterochromatin organization (GO:0070828), chromatin remodeling (GO:0006338), negative regulation of cell proliferation, tumor suppression.

**Protein dysfunction.** Loss of dimerization (protein–protein interaction failure), reduced stability (increased turnover), mislocalization (cytoplasmic retention of some mutants, e.g., p.C182\*), loss of DNA-target binding in combination variants ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)).

**Immune system involvement.** Combined immunodeficiency + autoimmunity + lymphoid neoplasia — a classic "immune dysregulation with immunodeficiency and malignancy" triad.

**GO/CL term suggestions.** Biological process: GO:0030098 (lymphocyte differentiation), GO:0070828 (heterochromatin organization), GO:0006338 (chromatin remodeling). Cell types (CL): CL:0000236 (B cell), CL:0000084 (T cell), CL:0000624 (CD4+ αβ T cell), CL:0000625 (CD8+ αβ T cell), CL:0000037 (hematopoietic stem cell), CL:0000813 (memory T cell), CL:0000775 (neutrophil).

### 7. Anatomical Structures Affected

- **Organ/system level (primary):** Immune/hematopoietic system — bone marrow (UBERON:0002371), thymus (UBERON:0002370), spleen (UBERON:0002106), lymph nodes (UBERON:0000029), peripheral blood (UBERON:0000178).
- **Secondary involvement:** Lungs (opportunistic/*Pneumocystis* pneumonia; UBERON:0002048); skin (neutrophilic dermatosis; UBERON:0002097); any organ targeted by autoimmunity or infiltrated by malignancy.
- **Tissue/cell level:** Lymphoid tissue; affected cell populations — B lymphocytes (CL:0000236), T lymphocytes (CL:0000084; naïve CL:0000898 / memory CL:0000813), hematopoietic stem/progenitor cells (CL:0000037), neutrophils (CL:0000775), myeloid dendritic cells, eosinophils.
- **Subcellular level:** Nucleus (GO:0005634) — pericentromeric heterochromatin (GO:0005721); the mislocalization defect involves aberrant cytoplasm (GO:0005737) retention of some mutants.
- **Localization / lateralization:** Systemic / bilateral; no lateralization.

### 8. Temporal Development

- **Onset:** Typically **congenital to pediatric/childhood**; some present neonatally via abnormal SCID newborn screening (low TREC) ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)); CVID-like presentations may extend into adulthood.
- **Onset pattern:** Insidious/chronic for immunodeficiency; may be acute at times of infection, autoimmune cytopenia crisis, or malignancy diagnosis.
- **Progression:** Variable. Chronic lifelong immunodeficiency; episodic autoimmune cytopenias; malignancy is a discrete, potentially fatal event. Spontaneous recovery of T-cell output is documented in at least one haploinsufficiency case ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)).
- **Remission patterns:** Treatment-induced (HSCT can be curative; [PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/)); spontaneous partial recovery possible.
- **Critical periods:** Early childhood (infection vulnerability, HSCT timing); lifelong window of malignancy surveillance.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; no formal prevalence/incidence estimates. Known from <10 families for the DD subtype specifically and >70 germline *IKZF1* variant carriers across all IKAROS-disease classes ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)).
- **Inheritance pattern:** **Autosomal dominant** (germline heterozygous).
- **Penetrance:** **Incomplete** ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/), [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/)).
- **Expressivity:** **Variable** — different carriers manifest different axes (infection, autoimmunity, malignancy) and severities.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** Not characterized; de novo variants reported. No founder effects documented.
- **Carrier frequency:** Not established (dominant disease; carriers are affected individuals with incomplete penetrance).
- **Demographics:** No ethnic predilection reported; both sexes affected. Age distribution skews pediatric.

### 10. Diagnostics

- **Laboratory tests:** CBC (cytopenias), immunoglobulin levels (hypogammaglobulinemia), lymphocyte subset immunophenotyping (low B cells; reduced naïve/increased memory T cells — DD signature), vaccine-response antibody titers, Coombs/DAT (AIHA).
- **Newborn screening:** May show **low TREC (SCID-like)**; important to add *IKZF1* to the low-TREC differential (spontaneous recovery possible) ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)).
- **Biomarkers:** No specific circulating biomarker; the **immunophenotypic signature** (naïve/memory skew) and functional assays are the practical markers.
- **Genetic testing (definitive):** **WES/WGS or targeted IEI gene panels** including *IKZF1*; single-gene *IKZF1* sequencing confirms the variant. Functional validation (dimerization, DNA-binding, pericentromeric localization, protein stability, alanine scanning) reclassifies VUS ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/), [PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).
- **Imaging / functional / electrophysiology / biopsy:** Non-specific; used for complications (infection imaging, malignancy staging biopsies, bone-marrow examination for cytopenias/leukemia).
- **Clinical criteria:** Diagnosis rests on a compatible clinical phenotype + a functionally validated germline ZF5–6 *IKZF1* variant.
- **Differential diagnosis:** CVID and other IEIs; SCID (on newborn screening); other IKAROS-disease classes (haploinsufficiency DNA-binding, dominant-negative, gain-of-function); *IKZF3*/AIOLOS and *IKZF2*/HELIOS disorders; ALPS/Evans syndrome of other causes; somatic *IKZF1*-deleted leukemia.
- **Screening:** Cascade family genetic testing once a variant is identified; SCID newborn screening may flag affected neonates.

### 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics; prognosis is driven by the **three axes** — infection severity, autoimmune cytopenia control, and (most critically) malignancy. Lymphoid malignancy (T-ALL/B-ALL/Burkitt) carries the highest mortality risk.
- **Morbidity:** Chronic infection burden, transfusion-dependent cytopenias, lifelong immunoglobulin replacement, and the morbidity of malignancy therapy/HSCT.
- **Disease course:** Chronic lifelong, punctuated by acute episodes; incomplete penetrance means some carriers have minimal morbidity.
- **Recovery potential:** HSCT can be curative for severe/malignant disease ([PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/), [PMID: 33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/)); spontaneous partial immune recovery is possible ([PMID: 33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/)).
- **Prognostic factors:** Variant mechanism/severity (complete vs partial dimerization loss), penetrance, presence of malignancy, and transplant eligibility/donor availability.

### 12. Treatment

| Modality | Intervention | NCIT suggestion | Evidence |
|---|---|---|---|
| Supportive/immune | Immunoglobulin replacement (IVIG/SCIG) | NCIT:C564 (Immunoglobulin Therapy) | [PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/) |
| Anti-infective prophylaxis | *Pneumocystis jirovecii* prophylaxis (e.g., TMP-SMX); antibacterial/antiviral/antifungal as needed | NCIT:C15843 (Antimicrobial Prophylaxis) | [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/) |
| Immunomodulation | Treatment of autoimmune cytopenias (corticosteroids, rituximab, etc.) | NCIT:C15431 (Immunotherapy) | general IEI practice |
| Curative | **Allogeneic HSCT** (reduced-intensity, matched unrelated donor shown tolerable) | NCIT:C105558 (Allogeneic HSCT) | [PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/), [PMID: 33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/) |
| Malignancy-directed | Standard ALL/lymphoma chemotherapy; investigational CK2 inhibition (CX-4945) to restore IKAROS function in B-ALL | NCIT:C15632 (Chemotherapy) | [PMID: 32396934](https://pubmed.ncbi.nlm.nih.gov/32396934/) |

- **Pharmacogenomics:** No disease-specific PGx guidance; experimental CK2 inhibition (CX-4945) restores IKAROS-mediated repression and chemosensitivity in high-risk B-ALL (preclinical) ([PMID: 32396934](https://pubmed.ncbi.nlm.nih.gov/32396934/)).
- **Gene/cell/RNA therapy:** No approved gene therapy; HSCT is the current cellular therapy. Gene correction is conceptually attractive but not clinically established.
- **Treatment strategy:** Risk-adapted — supportive care for mild/CVID-like disease; HSCT for severe combined immunodeficiency, refractory autoimmunity, or malignancy. Lifelong malignancy surveillance ([PMID: 38413050](https://pubmed.ncbi.nlm.nih.gov/38413050/)).

### 13. Prevention

- **Primary prevention:** Not possible (germline genetic). **Genetic counseling** and reproductive options (prenatal testing, preimplantation genetic diagnosis) for known-variant families.
- **Secondary prevention:** **Cascade genetic testing** of relatives; SCID newborn screening may enable early detection; proactive immunoglobulin replacement and infection prophylaxis.
- **Tertiary prevention:** Anti-infective prophylaxis, immunization (note: live vaccines may be contraindicated in CID), surveillance for autoimmunity and hematologic malignancy, timely HSCT.
- **Counseling:** Autosomal-dominant inheritance with incomplete penetrance should be communicated; a positive family history and susceptibility to infection/immune dysregulation are red flags for genomic testing ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *IKZF1* (NCBI Gene 10320); mouse *Ikzf1* (NCBI Gene 22778). Highly conserved across mammals.
- **Natural disease in other species:** No well-characterized naturally occurring companion-animal/wildlife equivalent documented; disease knowledge comes from engineered mouse models (Section 15), not spontaneous veterinary disease.
- **Comparative biology:** Mouse models faithfully reproduce the tumor-suppressor and lymphoid-developmental roles of IKAROS, validating the human mechanism; zinc-finger-specific functions are conserved ([PMID: 24013668](https://pubmed.ncbi.nlm.nih.gov/24013668/), [PMID: 26314708](https://pubmed.ncbi.nlm.nih.gov/26314708/)).
- **Transmission / zoonosis:** Not applicable (non-infectious genetic disease).

### 15. Model Organisms

- **Model type:** Mammalian — **mouse (*Mus musculus*)** is the principal model; plus in-vitro cell systems (HeLa/293/NIH3T3 transfection for localization/dimerization; T-ALL/B-ALL cell lines; thymoma line JE131).
- **Genetic models:** *Ikzf1* germline knockouts; **individual zinc-finger deletions (ZF1, ZF4)** showing separable phenotypes ([PMID: 24013668](https://pubmed.ncbi.nlm.nih.gov/24013668/)); conditional/T-cell-specific knockouts ([PMID: 30635395](https://pubmed.ncbi.nlm.nih.gov/30635395/)); tetracycline-regulated Lmo2 T-ALL model demonstrating *Ikzf1*-loss-driven oncogene independence ([PMID: 33483615](https://pubmed.ncbi.nlm.nih.gov/33483615/)).
- **Phenotype recapitulation:** Strong for the **tumor-suppressor and lymphoid-developmental** axes — loss causes leukemia, impaired thymic T-cell and pre-B development ([PMID: 26314708](https://pubmed.ncbi.nlm.nih.gov/26314708/), [PMID: 24297995](https://pubmed.ncbi.nlm.nih.gov/24297995/), [PMID: 30635395](https://pubmed.ncbi.nlm.nih.gov/30635395/)). AIOLOS/IKZF3 variant knock-in mice recapitulate B/T phenotypes of human disease ([PMID: 34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/)).
- **Limitations:** Mouse germline nulls do not model the human **heterozygous haploinsufficient** dosage precisely; human-specific immunophenotypic features (e.g., HNRNPLL/CD45 naïve-memory skew) and the three-axis clinical spectrum are only partially captured. No published mouse knock-in of a specific human ZF5–6 DD variant is noted in the reviewed literature.
- **Resources:** MGI (*Ikzf1*), IMPC/IMSR for knockout alleles.

---

## Mechanistic Model (Integrated Diagram)

```
 Germline heterozygous IKZF1 variant in C-terminal dimerization domain (ZF5-6)
                              │
                              ▼
        Mutant IKAROS cannot homo-/heterodimerize (AIOLOS, HELIOS)
                              │  (wild-type allele unaffected → HAPLOINSUFFICIENCY, not dominant-negative)
                              ▼
            ~50% functional IKAROS; reduced protein stability
                              │
                              ▼
   Impaired pericentromeric targeting + disrupted sumoylation + loss of NuRD/HDAC1 recruitment
                              │
                              ▼
   Deregulated chromatin/enhancer programs; altered IL-7 & type-I-IFN signaling
                              │
                              ▼
            Defective B- & T-lymphopoiesis (naive->memory T-cell skew)
             ┌────────────────┼─────────────────────┐
             ▼                ▼                     ▼
   (A) IMMUNODEFICIENCY   (B) IMMUNE DYSREG.    (C) TUMOR-SUPPRESSOR LOSS
   hypogamma, low B,      autoimmune cytopenias  T-ALL / B-ALL /
   recurrent + PJP        / Evans syndrome,      Burkitt lymphoma
   infections             neutrophilic dermatosis
             └────────────────┴─────────────────────┘
                              │
                              ▼
          Incomplete penetrance, variable expressivity
          Severe disease -> curative allogeneic HSCT
```

| IKZF1 disease class | Mechanism | Domain | T-cell phenotype | Key reference |
|---|---|---|---|---|
| Haploinsufficiency (DNA-binding) | ~50% LOF | ZF1–4 | Reduced naïve / ↑ memory | [PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/) |
| **Dimerization-defective (this disease)** | **Haploinsufficiency via lost dimerization** | **ZF5–6** | **Reduced naïve / ↑ memory** | [PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/), [PMID: 41424385](https://pubmed.ncbi.nlm.nih.gov/41424385/) |
| Dominant-negative | Sequesters WT | DNA-binding (e.g., N159) | Mostly naïve, no effector memory | [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/) |
| Gain-of-function | Hyperactive | — | — | [PMID: 38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/) |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in report |
|---|---|---|
| [32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/) | *Germline IKAROS dimerization haploinsufficiency...* | **Landmark**: defines the disease, mechanism (haploinsufficiency), phenotype, incomplete penetrance |
| [36433803](https://pubmed.ncbi.nlm.nih.gov/36433803/) | *Inborn errors of human IKAROS: LOF/GOF...* | Four-class mechanistic framework incl. dimerization-defective |
| [33392855](https://pubmed.ncbi.nlm.nih.gov/33392855/) | *IKAROS-Associated Diseases in 2020...* | Genotype/phenotype/outcome overview |
| [10970879](https://pubmed.ncbi.nlm.nih.gov/10970879/) | *Targeting of Ikaros to pericentromeric heterochromatin...* | Dimerization domain required for pericentromeric targeting |
| [40024461](https://pubmed.ncbi.nlm.nih.gov/40024461/) | *IKAROS protein stability...* | Six-ZF architecture; C-terminal domain regulates stability |
| [41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/) | *Systematic functional validation of IKAROS variants* | >70 germline variants; alanine scanning maps critical residues |
| [41424385](https://pubmed.ncbi.nlm.nih.gov/41424385/) | *IKAROS regulates human T cell phenotype...* | DD-specific naïve/memory T-cell skew |
| [29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/) | *Dominant-negative IKZF1 mutations...* | Contrasting DN class; PJP; T-cell maturation block |
| [24013668](https://pubmed.ncbi.nlm.nih.gov/24013668/) | *Selective regulation... by individual zinc fingers* | ZF4 selectively required for tumor suppression |
| [24297995](https://pubmed.ncbi.nlm.nih.gov/24297995/) | *Ikaros required for pre-B differentiation...* | B-lineage requirement via IL-7 attenuation |
| [26314708](https://pubmed.ncbi.nlm.nih.gov/26314708/) | *Regulation of gene expression dynamics...* | Potent tumor suppressor / hematopoietic regulator |
| [30635395](https://pubmed.ncbi.nlm.nih.gov/30635395/) | *Lack of Ikaros Deregulates Inflammatory Gene Programs...* | Autoimmunity axis; type-I-IFN repression |
| [33483615](https://pubmed.ncbi.nlm.nih.gov/33483615/) | *T-ALL can evolve to oncogene independence* | Ikzf1 loss sufficient to transform T-ALL |
| [40555735](https://pubmed.ncbi.nlm.nih.gov/40555735/) | *Critical roles of IKAROS and HDAC1...* | Heterochromatin/EZH2/H3K27me3 tumor-suppression mechanism |
| [31073152](https://pubmed.ncbi.nlm.nih.gov/31073152/) | *Ikaros tumor suppressor... enhancers/super-enhancers* | Enhancer/pioneering mechanism |
| [38320737](https://pubmed.ncbi.nlm.nih.gov/38320737/) | *IKAROS GOF disease: HCT experience...* | HSCT curative and well-tolerated |
| [33122583](https://pubmed.ncbi.nlm.nih.gov/33122583/) | *CVID, AIHA, pancytopenia... IKAROS defect* | HSCT in IKZF1-CVID; DNA-binding/PC localization assays |
| [33855675](https://pubmed.ncbi.nlm.nih.gov/33855675/) | *Abnormal SCID newborn screening...* | Low TREC; spontaneous recovery; haploinsufficiency |
| [19589926](https://pubmed.ncbi.nlm.nih.gov/19589926/) | *Recurrent 7p12 IKZF1 deletions in BCR-ABL1 ALL* | Somatic deletions; dominant-negative Ik6 isoform |
| [34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/) | *AIOLOS variant impairs immunity by interfering with IKAROS* | Heterodimeric interference; partner-gene relevance |
| [34920454](https://pubmed.ncbi.nlm.nih.gov/34920454/) | *Germline IKZF2 (Helios) mutations...* | Family-member dimerization/NuRD biology |
| [32396934](https://pubmed.ncbi.nlm.nih.gov/32396934/) | *IKAROS and CK2... chemosensitivity in B-ALL* | Experimental CK2 inhibition therapy |
| [38413050](https://pubmed.ncbi.nlm.nih.gov/38413050/) | *Neutrophilic dermatosis in IKZF1 variant...* | Autoinflammatory manifestation; surveillance |
| [32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/) | *IKZF1-Associated Diseases in PID...* | Supportive management; infection susceptibility |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | *Rapid identification of primary atopic disorders...* | Genomic sequencing / diagnostic approach |

**Evidence-source types:** Human clinical (case series) — 32845957, 29889099, 33122583, 33855675, 38320737, 38413050; mechanistic/in-vitro — 10970879, 40024461, 41380100, 32396934; model organism (mouse) — 24013668, 26314708, 30635395, 33483615, 24297995; reviews/frameworks — 36433803, 33392855, 32654692.

---

## Limitations and Knowledge Gaps

1. **Small sample size.** The defining DD cohort comprised only 4 families ([PMID: 32845957](https://pubmed.ncbi.nlm.nih.gov/32845957/)); no prevalence, incidence, survival, or QoL statistics exist. All frequency statements are qualitative.
2. **Penetrance quantification.** Incomplete penetrance is established qualitatively; the actual penetrance fraction and its genetic/environmental modifiers are unknown.
3. **No DD-specific animal model.** Mouse data derive from nulls/zinc-finger deletions, not knock-ins of human ZF5–6 variants; they model dosage imperfectly.
4. **Mechanistic branch weighting.** Why a given carrier develops immunodeficiency vs autoimmunity vs malignancy (and the role of variant-specific partial vs complete dimerization loss) is not resolved.
5. **Therapeutics.** HSCT evidence is strongest from GOF/other IKAROS-disease cases; DD-specific transplant outcomes are sparse. CK2 inhibition is preclinical only.
6. **Variant interpretation.** Many *IKZF1* ZF5–6 variants remain VUS; functional assays, while advancing ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)), are not yet standardized for clinical reporting.
7. **Epidemiology and population genetics.** No founder effects, carrier frequencies, geographic/ethnic distributions, or sex ratios are established.

---

## Proposed Follow-up Experiments / Actions

1. **Build an international DD-IKZF1 registry** to quantify penetrance, axis-specific frequencies, malignancy risk, and natural history across larger numbers.
2. **Generate knock-in mouse (or iPSC) models of specific human ZF5–6 DD variants** to directly test haploinsufficiency dosage effects and the naïve/memory T-cell skew (HNRNPLL/CD45 axis).
3. **Standardize and clinically validate the functional assay battery** (dimerization, DNA-binding, pericentromeric localization, protein stability, alanine scanning) for ACMG-grade VUS reclassification ([PMID: 41380100](https://pubmed.ncbi.nlm.nih.gov/41380100/)).
4. **Define the DD immunophenotypic signature** (naïve/memory ratios, B-cell subsets) prospectively as a clinical biomarker to distinguish DD from DN disease.
5. **Prospective HSCT outcome study** specific to DD-IKZF1 patients, including reduced-intensity conditioning regimens.
6. **Evaluate IKAROS-restoring pharmacology (e.g., CK2 inhibitor CX-4945)** in IKZF1-driven leukemia arising on a germline DD background ([PMID: 32396934](https://pubmed.ncbi.nlm.nih.gov/32396934/)).
7. **Systematic malignancy surveillance protocol** for asymptomatic variant carriers, given lifelong leukemia/lymphoma risk ([PMID: 38413050](https://pubmed.ncbi.nlm.nih.gov/38413050/)).

---

*Report compiled from 5 discovery iterations, 9 confirmed findings, and 35 reviewed primary and review papers. Ontology term suggestions (MONDO, HPO, GO, CL, UBERON, NCIT, HGNC) are provided inline for knowledge-base population.*


## Artifacts

- [OpenScientist final report](Combined_Immunodeficiency_Due_To_Dimerization_Defective_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Immunodeficiency_Due_To_Dimerization_Defective_IKAROS_Mutation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 28 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24297995` *(abstract only)*: "absolutely required for pre-B cell differentiation by attenuating IL-7 signals"
  - closest text in source: "Pre-B cell receptor (pre-BCR) signaling and migration from IL-7-rich environments cooperate to drive pre-B cell differentiation via transcriptional programs that remain unclear"
- `PMID:34920454`: "heterodimeric interference"
  - Text part not found as substring: 'heterodimeric interference'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0979288` (3 mentions) - the report calls it "Mondo"; MONDO calls it **combined immunodeficiency due to dimerization defective IKAROS mutation**
- `HP:0001873` (2 mentions) - the report calls it "Lab/clinical sign"; HP calls it **Thrombocytopenia**
- `HP:0001875` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total neutrophil count**
- `HP:0002719` (1 mention) - the report calls it "Symptom"; HP calls it **Recurrent infections**
- `HP:0006727` (1 mention) - the report calls it "Neoplasm"; HP calls it **T-cell acute lymphoblastic leukemias**
- `HP:0004812` (1 mention) - the report calls it "Neoplasm"; HP calls it **B Acute Lymphoblastic Leukemia**
- `HP:0002960` (1 mention) - the report calls it "Clinical sign"; HP calls it **Autoimmunity**
- `HP:0005415` (1 mention) - the report calls it "abnormal T-cell count"; HP calls it **Decreased total CD8+ T cell proportion**
- `HP:0010976` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total B cell count**
- `NCIT:C564` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **Ifosfamide**
- `NCIT:C15431` (1 mention) - the report calls it "Immunotherapy"; NCIT calls it **Hematopoietic Cell Transplantation**
- `NCIT:C105558` (1 mention) - the report calls it "Allogeneic HSCT"; NCIT calls it **TPI1 wt Allele**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012190` (1 mention) - the report calls it "non-Hodgkin lymphoma"; HP calls it **T-cell lymphoma**
- `CL:0000624` (1 mention) - the report calls it "CD4+ αβ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000625` (1 mention) - the report calls it "CD8+ αβ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `GO:0005634` (1 mention) - the report calls it "Subcellular level:** Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `NCIT:C15843` (1 mention) - the report calls it "Antimicrobial Prophylaxis"; NCIT calls it **Preventive Intervention**, and lists "Prophylaxis" among its other names