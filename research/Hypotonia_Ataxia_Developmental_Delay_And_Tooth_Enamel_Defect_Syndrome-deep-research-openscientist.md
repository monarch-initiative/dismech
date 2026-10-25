---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T01:27:59.591002'
end_time: '2026-10-24T02:05:04.675613'
duration_seconds: 2225.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypotonia, Ataxia, Developmental Delay, and Tooth Enamel Defect Syndrome
  mondo_id: MONDO:0060666
  category: Mendelian
  causal_genes: CTBP1
  omim_id: not recorded
  synonyms: HADDTS; CTBP1-related neurodevelopmental disorder
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
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 9
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 3
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001251
    reported_labels:
    - high (most)
    ontology_label: Ataxia
  - term_id: GO:0001764
    reported_labels:
    - Cellular processes:** neural progenitor proliferation & migration
    ontology_label: neuron migration
  - term_id: NCIT:C15917
    reported_labels:
    - physical therapy
    ontology_label: Arterial Embolization
  - term_id: NCIT:C15224
    reported_labels:
    - occupational therapy
    ontology_label: Nutrition Research, Fats
  - term_id: NCIT:C15348
    reported_labels:
    - speech-language therapy
    ontology_label: Vasectomy
  - term_id: NCIT:C15491
    reported_labels:
    - nutritional support/feeding management
    ontology_label: Premenopausal
  - term_id: NCIT:C15587
    reported_labels:
    - genetic counseling
    - Counseling:** **genetic counseling
    ontology_label: Bone Marrow Ablation with Stem Cell Support
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypotonia_Ataxia_Developmental_Delay_And_Tooth_Enamel_Defect_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypotonia_Ataxia_Developmental_Delay_And_Tooth_Enamel_Defect_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypotonia, Ataxia, Developmental Delay, and Tooth Enamel Defect Syndrome
- **MONDO ID:** MONDO:0060666 (if available)
- **Causal gene(s):** CTBP1
- **OMIM:** not recorded
- **Synonyms:** HADDTS; CTBP1-related neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypotonia, Ataxia, Developmental Delay, and Tooth Enamel Defect Syndrome** covering all of the
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

# Hypotonia, Ataxia, Developmental Delay, and Tooth Enamel Defect Syndrome (HADDTS)
### A CTBP1-related neurodevelopmental disorder — comprehensive disease characterization

---

## Summary (Answer to the Research Question)

**Hypotonia, Ataxia, Developmental Delay, and Tooth Enamel Defect Syndrome (HADDTS)** is an ultra-rare, autosomal dominant neurodevelopmental disorder caused by **de novo heterozygous pathogenic variants in *CTBP1*** (C-terminal binding protein 1; HGNC:2494), a NAD(H)-dependent transcriptional corepressor that also acts as a cytoplasmic membrane-fission factor (BARS). The overwhelming majority of patients (~90%) carry a single recurrent missense hotspot, **c.991C>T / c.1024C>T, p.Arg342Trp** (transcript-dependent numbering; originally reported as p.R331W), located in the C-terminal **PLDLS-binding cleft** through which CtBP1 recruits chromatin-modifying corepressor partners. The mutation acts as a **dominant-negative / interfering allele** (not simple haploinsufficiency), impairing assembly of CtBP–HDAC1/2–LSD1 repressor complexes that guide corticogenesis, deregulating transcription, sensitizing cells to metabolic-stress apoptosis, and — via the BARS branch — disturbing Golgi-dependent neuronal polarization and migration. The clinical core is the eponymous tetrad: **muscular hypotonia, ataxia, global developmental delay/intellectual disability, and tooth enamel defects**, with **cerebellar atrophy** on MRI. Fewer than ~20 patients have been reported worldwide. There is no disease-specific therapy; management is supportive.

> ⚠️ **Gene disambiguation note:** This report concerns **MONDO:0060666 / OMIM #617915**, the ***CTBP1*-related** disorder HADDTS. It is distinct from *CTBP2*-related phenotypes; the systematic review found no confirmed neurodevelopmental disorder from heterozygous *CTBP2* variants (PMID 36331689).

---

## 1. Disease Information

**Overview.** HADDTS is a monogenic (Mendelian) pediatric neurodevelopmental syndrome. It was first delineated in 2016 when four unrelated patients with developmental delay, intellectual disability, failure to thrive, hypotonia, ataxia and tooth-enamel defects were each found to carry the same de novo *CTBP1* missense variant (PMID 27094857): *"we have identified four patients with similar phenotypes of developmental delay, intellectual disability, failure to thrive, hypotonia, ataxia, and tooth enamel defects who all have the same de novo R331W missense variant in C-terminal binding protein 1 (CTBP1)"* (PMID 27094857).

**Key identifiers.**
- **MONDO:** MONDO:0060666
- **OMIM:** #617915 (Hypotonia, ataxia, developmental delay, and tooth enamel defect syndrome; HADDTS)
- **Gene:** *CTBP1*, HGNC:2494, NCBI Gene 1487, Ensembl ENSG00000159692, UniProt Q13363; cytoband 4p16.3
- **Orphanet:** CTBP1-related neurodevelopmental disorder (ultra-rare; ORPHA designation under CTBP1-related conditions)
- **ICD-10:** no specific code (mapped generically, e.g., Q87.8 / F79); **ICD-11:** no specific code (e.g., LD2F.1Y / 6A00.Z used generically)
- **MeSH:** no dedicated descriptor; indexed under Neurodevelopmental Disorders / Intellectual Disability
- **Data source type:** **Disease-level aggregation of individual published patient case reports/series** (not EHR registry data); evidence is predominantly human clinical case reports supplemented by in vitro and model-organism functional studies.

**Synonyms / alternative names:** HADDTS; CTBP1-related neurodevelopmental disorder; CTBP1-related intellectual disability; (historical) "R331W/R342W CTBP1 syndrome."

---

## 2. Etiology

**Primary cause — genetic.** HADDTS is caused by **heterozygous pathogenic variants in *CTBP1***, almost always arising **de novo** (PMID 42589715, PMID 27094857). There is no environmental, infectious, or multifactorial etiology; it is a classic de novo dominant Mendelian disorder.

**Genetic risk factors.**
- **Causal variant (recurrent hotspot):** *CTBP1* **p.Arg342Trp** (c.991C>T or c.1024C>T depending on transcript; = legacy p.R331W). 13/14 individuals in the systematic review carried this variant (PMID 36331689).
- **Second reported variant:** **c.1315_1316delCA, p.Gln439ValfsTer84** (frameshift) in one individual (PMID 36331689).
- **Expanded allelic spectrum:** a novel **c.107G>C, p.Arg36Pro** variant, also in the PLDLS cleft, produced a *distinct* neurodevelopmental disorder not fully meeting HADDTS criteria (PMID 41674141).
- **Modifier genes:** none established. *CTBP2* is a paralog with overlapping function and is a plausible genetic modifier (redundancy), but no human modifier data exist.
- **Primary risk factor for occurrence:** advanced parental age is the generic correlate of de novo mutation burden (not specifically demonstrated for *CTBP1*).

**Environmental risk factors / lifestyle / infectious agents:** **None known / not applicable.** No toxin, exposure, diet, or pathogen is implicated. (CTD: no curated environmental interaction causing HADDTS.)

**Protective factors (genetic or environmental):** **None identified / not applicable.**

**Gene–environment interactions.** Not established clinically. Mechanistically, CtBP1 is a **metabolic/redox sensor** (NAD(H)-dependent), and patient fibroblasts show heightened sensitivity to **glucose deprivation** (PMID 31041561) — a cell-level gene×metabolic-state interaction, but no organism-level GxE is documented.

---

## 3. Phenotypes

Evidence base: human clinical case reports/series (PMID 27094857, 31041561, 36331689, 42704868). Frequencies are approximate given the very small cohort (<20 patients).

**Core tetrad (present in most/all; "consistent CtBP1-related phenotypes of intellectual disability, ataxia, hypotonia, and tooth enamel defects present in most patients," PMID 31041561):**

| Phenotype | Type | Onset | Severity | Course | Freq. | HPO |
|---|---|---|---|---|---|---|
| Intellectual disability / global developmental delay | cognitive/behavioral | neonatal–infancy | moderate–severe | stable/non-progressive | ~100% | HP:0001249; HP:0001263 |
| Muscular hypotonia ("floppy infant") | clinical sign (neuromuscular) | neonatal | moderate–severe | often improves to spasticity/stable | ~100% | HP:0001252; HP:0001319 |
| Ataxia (gait/truncal) | clinical sign (cerebellar) | childhood | moderate | stable | high (most) | HP:0001251 |
| Tooth enamel defect (enamel hypoplasia/amelogenesis imperfecta-like) | physical/dental | childhood (as teeth erupt) | variable | stable | high (defining) | HP:0000682; HP:0006297 |

**Additional/variable features reported:**
- Cerebellar atrophy / volume loss on MRI (HP:0001272; cerebellar vermis atrophy HP:0006855) — *"cerebellar volume loss"* (PMID 36331689); *"cerebellar atrophy on brain imaging"* (PMID 42704868).
- Delayed/absent speech, speech disorder (HP:0000750; HP:0001344).
- Failure to thrive / feeding difficulties (HP:0001508; HP:0011968) (PMID 27094857).
- Facial dysmorphism (HP:0001999) (PMID 42704868).
- Constipation (HP:0002019) (PMID 42704868).
- Congenital heart disease — atrial septal defect (HP:0001631) reported in the p.R36P case (PMID 41674141).
- Behavioral features of severe NDD (variable).

**Quality-of-life impact.** High burden: nonverbal or limited speech, dependence for daily activities, mobility limited by hypotonia/ataxia, and dental morbidity (pain, caries susceptibility from defective enamel). No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder; QoL inferred from severe-NDD phenotype.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***CTBP1*** (HGNC:2494; OMIM gene *602618*; disease OMIM #617915). Encodes a 440-aa NAD(H)-dependent d-isomer–specific 2-hydroxyacid dehydrogenase-family transcriptional corepressor (UniProt Q13363).

**Pathogenic variants.**
- **p.Arg342Trp (recurrent hotspot):** c.991C>T / c.1024C>T; **missense**; **Pathogenic (ACMG)**; recurrent de novo; in the PLDLS-binding cleft. ~90% of cases (PMID 36331689, 27094857, 31041561, 42704868).
- **p.Gln439ValfsTer84:** c.1315_1316delCA; **frameshift**; **Pathogenic**; single case (PMID 36331689).
- **p.Arg36Pro:** c.107G>C; **missense**; PLDLS cleft; distinct/atypical NDD (PMID 41674141).
- **Allele frequency:** all are **absent from population databases** (gnomAD) — consistent with de novo pathogenic variants in an essential, highly constrained gene (*CTBP1* is loss-of-function intolerant). **Not found as common polymorphisms.**
- **Somatic vs germline:** **germline** (constitutional de novo); one case of **maternal germline mosaicism** (PMID 36331689). (Note: somatic *CTBP1* dysregulation/overexpression is separately implicated in cancer — not relevant to HADDTS germline disease.)
- **Functional consequence:** **Dominant-negative / interfering gain-of-abnormal-function** at the PLDLS cleft rather than simple loss of function. Supported by (i) viability of *Ctbp1*-null mice (PMID 12101226); (ii) reduced partner binding by the mutant plus transcriptional deregulation (PMID 31041561). The variant retains dimerization/NAD-binding but loses high-affinity partner recruitment, enabling it to poison shared CtBP1/CtBP2 complexes.

**Modifier genes.** None proven; *CTBP2* redundancy is the leading candidate buffer (PMID 12101226, 12508276).

**Epigenetic information.** CtBP1 is itself an **epigenetic effector** — it scaffolds HDAC1/HDAC2 and LSD1/KDM1A to deacetylate and demethylate histones at target enhancers (PMID 41105133). No disease-specific DNA-methylation "episignature" has yet been published for HADDTS (a plausible future diagnostic avenue, not applicable currently).

**Chromosomal abnormalities.** None; HADDTS is a single-nucleotide/small-indel disorder. Chromosomal microarray is typically normal.

---

## 5. Environmental Information

**Environmental factors, lifestyle factors, infectious agents:** **None / not applicable.** HADDTS is a purely genetic de novo dominant disorder with no established environmental contribution. The only environment-adjacent biology is cellular **metabolic/redox state** (glucose/NAD(H)), which modulates CtBP1 activity and patient-cell apoptosis sensitivity (PMID 31041561, PMID 38626254) — relevant mechanistically, not as a population exposure.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **de novo heterozygous *CTBP1* variant** (predominantly p.Arg342Trp) arises in the germline → an altered CtBP1 protein with a defective **PLDLS-binding cleft**.
2. The mutant **leads to** reduced recruitment of PLDLS-motif corepressor partners and chromatin-modifying enzymes (HDAC1/2, LSD1) to CtBP1 (*demonstrated*: reduced interaction with chromatin-modifying factors, PMID 31041561; complex identity, PMID 41105133).
3. Because CtBP1 dimerizes with/shares partners with CtBP2, the mutant **acts as a dominant-negative**, poisoning the combined CtBP1/CtBP2–HDAC–LSD1 repressor activity (*inferred* from *Ctbp1*-null mouse viability + dosage sensitivity, PMID 12101226/12508276).
4. This **results in** genome-wide **transcriptional deregulation** of genes controlling multiple cellular processes (*demonstrated* by transcriptomics, PMID 31041561).

   **Branch A (nuclear / chromatin):** Deregulated neurogenic enhancer programs (PRDM16–CtBP–HDAC1/2–LSD1) **lead to** impaired neural progenitor proliferation and **delayed migration/positioning of cortical neurons** (PMID 41105133, 32169478).

   **Branch B (cytoplasmic / BARS):** Impaired CtBP1-S/**BARS**-mediated **Golgi membrane fission** **leads to** defective post-Golgi trafficking, disturbing neuronal polarization, axon/dendrite elongation and the multipolar-to-bipolar transition (*BARS requirement demonstrated by RNAi*, PMID 35455998; dual function, PMID 41674141; whether HADDTS alleles impair BARS fission specifically is *inferred*).

   **Branch C (metabolic / apoptotic):** As an NAD(H) sensor, mutant CtBP1 **results in** heightened sensitivity to metabolic stress — glucose deprivation strongly activates the BH3-only gene **NOXA/PMAIP1**, enhancing apoptosis (PMID 31041561); a functional case links the disorder to **impaired mitochondrial bioenergetics** (PMID 42123581).
5. Branches A–C **converge** to **reduce dendritic number/length, disrupt dendritic arborization and spine formation, and lower excitatory synaptic transmission** (*demonstrated in vitro and in vivo*, PMID 41674141).
6. These cellular defects **result in** maldevelopment of **cerebral cortex and cerebellum** → **cerebellar atrophy**, and clinically **hypotonia, ataxia, developmental delay/intellectual disability** (PMID 36331689, 42704868).
7. In parallel, CtBP1 corepressor dysfunction in **enamel-forming epithelium (ameloblasts)** **leads to** the **tooth enamel defect** (*mechanism inferred*; ameloblast-specific data not yet published).

### Detail by category
- **Molecular pathways:** CtBP corepressor axis (PLDLS-partner → HDAC1/2 + LSD1/KDM1A, recruited via PRDM16, ZEB1/δEF1, CTCF) (PMID 10567582, 41105133); NAD(H)/redox-glycolysis signaling controlling CtBP oligomerization (PMID 38626254, 41972124); intersections with Wnt-regulated repression (CtBP is a Wnt-pathway corepressor). GO: negative regulation of transcription by RNA Pol II (GO:0000122); transcription corepressor activity (GO:0003714).
- **Cellular processes:** neural progenitor proliferation & migration (GO:0001764), dendrite development (GO:0016358), dendritic spine morphogenesis (GO:0060997), synaptic transmission (GO:0007268), apoptosis (GO:0006915), Golgi vesicle budding/fission (GO:0048194).
- **Protein dysfunction:** loss of high-affinity PLDLS partner binding with retained scaffold → **dominant-negative**; two functional modules = NAD(H)-binding Rossmann fold (intact) + PLDLS cleft (disrupted) (PMID 38711119).
- **Metabolic changes:** NAD(H)/glucose sensitivity; impaired mitochondrial bioenergetics (PMID 42123581, 31041561).
- **Immune involvement:** not a feature of HADDTS (CtBP1's inflammasome-transrepression role is a separate vascular context, PMID 38626254).
- **Tissue damage mechanism:** developmental (maldevelopment) rather than degenerative, though "cerebellar atrophy" implies some neuronal loss/under-growth.
- **Molecular profiling available:** transcriptomics in glioblastoma lines expressing wt vs W342 CtBP1 (PMID 31041561); unbiased proteomics of mutant interactome (PMID 31041561); isogenic iPSC-derived neuronal models (PMID 41459558); no HADDTS metabolomics/lipidomics/spatial datasets yet.
- **Cell types (CL):** glutamatergic/excitatory cortical neuron (CL:0000679), pyramidal neuron, neural progenitor cell (CL:0011020), cerebellar neurons (Purkinje/granule), ameloblast (CL:0000059, enamel).
- **Subcellular compartments (GO CC):** nucleus (GO:0005634), Golgi apparatus (GO:0005794), mitochondrion (GO:0005739).

---

## 7. Anatomical Structures Affected

- **Organ/system level — primary:** **central nervous system** (UBERON:0001017) — **cerebral cortex** (UBERON:0000956) and **cerebellum** (UBERON:0002037, with cerebellar atrophy/vermis involvement); **teeth/dental enamel** (UBERON:0001752 tooth; UBERON:0001751 enamel). Body systems: **nervous**, **musculoskeletal/neuromuscular** (hypotonia), **stomatognathic/dental**.
- **Secondary involvement:** **digestive** (feeding difficulty, constipation), **cardiovascular** (atrial septal defect in one case), growth (failure to thrive).
- **Tissue/cell level:** **nervous tissue** (cortical & cerebellar neurons, neural progenitors); **dental epithelium** (ameloblasts → enamel matrix); skeletal **muscle** secondarily (central hypotonia, not primary myopathy).
- **Subcellular:** nucleus (chromatin regulation), Golgi apparatus (BARS fission), mitochondria (bioenergetics).
- **Localization / lateralization:** **bilateral, symmetric** CNS involvement; cerebellar atrophy is typically diffuse/midline (vermian).

---

## 8. Temporal Development

- **Onset:** **congenital/neonatal** — hypotonia and feeding problems present from birth ("floppy baby," PMID 42704868); developmental delay evident in infancy. Pattern: **chronic, insidious** (developmental, not acute).
- **Progression:** **largely static/non-progressive neurodevelopmental** course; disability is lifelong. Enamel defects manifest as dentition erupts. Cerebellar atrophy documented on imaging; whether it is static or slowly progressive across the small cohort is **not firmly established** (natural-history data limited).
- **Disease course pattern:** stable/chronic lifelong; not relapsing-remitting or episodic.
- **Critical period / window of opportunity:** **corticogenesis (prenatal) and early postnatal synaptic maturation** — the mechanistic steps (neuron migration, dendrite/spine formation) occur developmentally, so the therapeutic window is early; postnatal reversal is likely limited.
- **Remission:** none (no spontaneous or treatment-induced remission reported).

---

## 9. Inheritance and Population

- **Epidemiology:** **ultra-rare**; **<20 patients reported worldwide** as of 2026 — *"This is the 18th reported case of this ultra-rare disorder"* (PMID 42704868); *"only 20 published cases"* (PMID 42123581). **Prevalence/incidence not quantifiable** (no population estimate; effectively <1/1,000,000).
- **Inheritance pattern:** **autosomal dominant** (OMIM #617915), essentially all cases **de novo** (PMID 42589715, 27094857).
- **Penetrance:** presumed **complete** in heterozygous carriers of the pathogenic variant (all reported carriers affected).
- **Expressivity:** **variable** (core tetrad consistent; additional features e.g., cardiac, dysmorphism vary; distinct allele p.R36P gives an atypical presentation).
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** **documented** (one maternal germline mosaicism case, PMID 36331689) → **non-zero recurrence risk** for apparently unaffected parents.
- **Founder effects / consanguinity / carrier frequency:** **not applicable** (recurrent de novo dominant; the recurrence reflects a mutational **hotspot**, not a founder haplotype; consanguinity irrelevant; no carrier screening relevance).
- **Population demographics:** reported across diverse populations (US, Iran [PMID 34608870], Poland [PMID 42704868], others) → **no ethnic predilection**; recurrence is hotspot-driven, not geographic. **Sex ratio:** apparent male excess (10/14 males, PMID 36331689) but likely ascertainment artifact given tiny N. **Age distribution:** children and young adults (diagnosed in childhood; oldest reported ~20 years).

---

## 10. Diagnostics

- **Primary diagnostic modality — genomic sequencing.** Diagnosis is molecular: **trio whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** identifies the de novo *CTBP1* variant — *"Exome sequencing is an effective way to identify genetic causes of etiologically heterogeneous conditions such as developmental delay and intellectual disabilities"* (PMID 27094857); subsequent cases diagnosed by WES (PMID 34608870) and genotype-to-phenotype large-scale testing (PMID 42704868). **Single-gene/targeted *CTBP1* testing** or **NDD gene panels** including *CTBP1* are appropriate when clinically suspected. Confirmation by Sanger; parental testing to establish de novo status.
- **Low-yield / normal tests:** **chromosomal microarray (CMA)** and **karyotype** are typically normal (no structural lesion); FISH, mtDNA testing, and repeat-expansion testing are **not indicated**.
- **Supportive clinical tests:**
  - **Brain MRI:** cerebellar atrophy/volume loss (HP:0001272) (PMID 36331689, 42704868).
  - **Dental examination/radiographs:** enamel hypoplasia/defects.
  - **Echocardiography:** to evaluate congenital heart defect when present.
  - **Metabolic workup:** generally non-diagnostic but excludes mimics; patient fibroblasts show glucose-deprivation apoptosis sensitivity (research finding, PMID 31041561), and one report notes mitochondrial bioenergetic impairment (PMID 42123581) — not yet a clinical biomarker.
- **Biomarkers:** no validated circulating/biochemical biomarker; the **genetic variant itself is the diagnostic marker**. A DNA-methylation episignature is a plausible future tool (not available).
- **Clinical/diagnostic criteria:** no formal consensus criteria; diagnosis = compatible phenotype (hypotonia + ataxia + DD/ID + enamel defect ± cerebellar atrophy) **plus a pathogenic *CTBP1* variant**. Note: the atypical p.R36P patient did **not** fulfill HADDTS criteria despite a pathogenic *CTBP1* variant (PMID 41674141), underscoring phenotype–genotype nuance.
- **Differential diagnosis:** other causes of the hypotonia–ataxia–ID–enamel constellation, e.g., **Kohlschütter–Tönz syndrome** (*ROGDI*; epilepsy + amelogenesis imperfecta), other **amelogenesis imperfecta** syndromes, **congenital disorders of glycosylation**, **cerebellar hypoplasia/atrophy syndromes**, and other monogenic NDDs — distinguished by gene-level testing.
- **Screening (asymptomatic):** not applicable (de novo; no carrier/newborn screening); **cascade testing** only relevant for recurrence counseling given mosaicism.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **No disease-specific mortality data**; HADDTS is **not reported as life-limiting per se**. Life expectancy is presumably determined by severity of disability and complications (feeding, aspiration, cardiac anomaly when present) rather than by a defined lethal course. Oldest reported patient ~20 years (PMID 41674141).
- **Morbidity/disability:** **high, lifelong** — intellectual disability (often moderate–severe), motor disability from hypotonia and ataxia, speech impairment, and dental morbidity. Most patients require lifelong caregiving support.
- **Disease course:** chronic, static neurodevelopmental disability; complications include feeding difficulty/failure to thrive, constipation, dental caries/pain from enamel defects, and cardiac issues in a minority.
- **Recovery potential:** developmental gains with early intervention/therapy are possible, but **the underlying neurodevelopmental deficit is not reversible**.
- **Prognostic factors:** genotype (classic p.R342W vs atypical alleles), severity of cerebellar atrophy, presence of cardiac/other systemic anomalies, and feeding status. **No validated prognostic biomarkers.** QoL/ICF-coded disability instruments not formally applied.

---

## 12. Treatment

**There is no disease-specific or disease-modifying therapy for HADDTS. Management is entirely supportive and multidisciplinary** (evidence: absence of any reported pharmacologic/gene/cell/RNA therapy or HADDTS-specific trial; standard severe-NDD care).

- **Pharmacotherapy:** **none specific.** Symptomatic agents as needed (e.g., for constipation; anti-epileptics only if seizures occur). **Pharmacogenomics:** not applicable.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **none approved or in trials.** Note a conceptual mismatch: existing **CtBP dehydrogenase inhibitors** (MTOB, JW-98, Comp.11) were developed to *reduce* CtBP oncogenic activity in cancer (PMID 41353240, 38711119) — the **opposite** of what a loss-of-corepression developmental disorder would require; they are **not** HADDTS therapeutics. Because the mechanism is dominant-negative, **allele-selective knockdown (ASO/siRNA against the mutant allele)** is a theoretically rational but **unproven/experimental** future direction (NCIT: Antisense Oligonucleotide Therapy C1516; Gene Therapy C15262).
- **Surgical/interventional:** as indicated for complications (e.g., congenital heart defect repair; dental restorative procedures/crowns for enamel defects).
- **Supportive & rehabilitative (mainstay):** **physical therapy** (NCIT:C15917) for hypotonia/ataxia/mobility; **occupational therapy** (NCIT:C15224); **speech-language therapy** (NCIT:C15348) and AAC; **nutritional support/feeding management** (NCIT:C15491) for failure to thrive; **restorative/preventive dental care** for enamel defects; management of constipation; early-intervention/special-education programs. NCIT: Supportive Care (C15277).
- **Treatment outcomes / adverse events:** supportive measures improve function/comfort; no curative outcome. **Treatment strategy:** individualized, symptom-directed multidisciplinary care; genotype-guided therapy not yet available (**personalized medicine = experimental allele-specific approaches only**).

---

## 13. Prevention

- **Primary prevention:** **none possible** for the de novo event itself (no modifiable risk factor).
- **Secondary prevention:** early developmental surveillance and early-intervention therapy to optimize function; early dental and cardiac evaluation to pre-empt complications (tertiary prevention of complications).
- **Genetic screening / reproductive options:** once a familial/proband variant is identified, **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** are available for future pregnancies; recurrence risk is low but **non-zero due to documented germline mosaicism** (PMID 36331689).
- **Counseling:** **genetic counseling** (NCIT:C15587) is central — explaining de novo dominant inheritance, low-but-nonzero recurrence risk (mosaicism), and reproductive options.
- **Immunization / behavioral / public-health / environmental / prophylaxis:** **not applicable** (no infectious or environmental component).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *CTBP1* is deeply conserved. Orthologs: **mouse *Ctbp1*** (NCBI Gene 13016; *Mus musculus*, NCBI:txid10090), **rat *Ctbp1*** (*Rattus norvegicus*, NCBI:txid10116), zebrafish *ctbp1* (*Danio rerio*, NCBI:txid7955), *Drosophila* **CtBP** (NCBI:txid7227), and a plant homolog **Angustifolia** (PMID 12508276). The paralog **CTBP2/*Ctbp2*** (NCBI Gene 13017 mouse) is partially redundant.
- **Natural disease in other species / breeds / VBO / zoonosis:** **None reported.** No naturally occurring HADDTS-equivalent disease, no breed predisposition (VBO: not applicable), and **no zoonotic/transmission** relevance — it is a non-communicable germline disorder.
- **Comparative biology / conservation:** disease mechanisms are evolutionarily conserved — CtBP corepressor function and PLDLS-partner recruitment are conserved from flies to humans (PMID 10567582, 12508276), and CtBP controls neurodevelopment across vertebrates, enabling model-organism study.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBI:txid10090) — knockouts:** ***Ctbp1*-null mice are small but viable and fertile**, whereas ***Ctbp2*-null mice are embryonic lethal (~E10.5)** with axial-patterning, heart-morphogenesis and neural-development defects; compound alleles show **dosage-sensitive** phenotypes (PMID 12101226, 12508276). **Interpretation:** *Ctbp1* loss alone is well tolerated → argues the human p.R342W is **dominant-negative**, not haploinsufficient. (Available via MGI/IMSR.)
- **Mouse — in vivo corticogenesis models:** **in utero electroporation** of CtBP2 siRNA perturbs neural stem/progenitor proliferation and migration (PMID 32169478); the **PRDM16–CtBP1/2–HDAC1/2–LSD1** complex guides upper-layer neuron migration (PMID 41105133); acute in vivo expression of human **p.R342W and p.R36P** causes excitatory-neuron migration delay and disrupted dendritic arborization/spine formation (PMID 41674141). **Strong recapitulation** of the human neuromigration/dendritic phenotype.
- **Primary neurons / in vitro:** hippocampal neuron cultures show reduced dendrite number/length with mutant CtBP1 (PMID 41674141) and impaired axon/dendrite growth with BARS knockdown (PMID 35455998).
- **Patient-derived & iPSC models:** patient **dermal fibroblasts** (glucose-deprivation apoptosis, NOXA induction; PMID 31041561); **isogenic iPSC-derived neurons** modeling the heterozygous mutation (PMID 41459558); **glioblastoma lines** expressing wt vs W342 CtBP1 for transcriptomics (PMID 31041561).
- **Model limitations:** no single model reproduces the **full human tetrad** (especially the **tooth enamel defect**, which lacks a dedicated published model); mouse knockouts model *loss* rather than the *dominant-negative* allele; cerebellar/ataxia phenotype not fully characterized in a germline knock-in mouse (a **p.R342W knock-in mouse is a key gap**).
- **Resources:** MGI (mouse), IMSR/IMPC (alleles), ZFIN (zebrafish), FlyBase (Drosophila), Cellosaurus (iPSC/cell lines).

---

## Supported vs Refuted Hypotheses

**Supported:**
1. HADDTS is caused by de novo heterozygous *CTBP1* variants, dominated by the recurrent PLDLS-cleft hotspot p.Arg342Trp (PMID 27094857, 36331689).
2. The variant acts via a **dominant-negative** mechanism (Ctbp1-null mice viable; mutant loses partner binding but retains scaffold) (PMID 12101226, 31041561).
3. Pathogenesis converges on **corticogenesis**: impaired neuron migration, dendrite/spine maturation, and excitatory transmission (PMID 41674141, 41105133, 32169478).
4. CtBP1 couples **metabolic/redox state** to transcription, explaining glucose-stress apoptosis (PMID 31041561, 38626254, 41972124).
5. A **second (BARS/Golgi-fission) branch** contributes to neuronal maldevelopment (PMID 35455998, 41674141).

**Refuted / not supported:**
- Simple **haploinsufficiency** as the mechanism (refuted by viable *Ctbp1*-null mice).
- A confirmed ***CTBP2***-related equivalent neurodevelopmental disorder (not identified; PMID 36331689).
- Any environmental/infectious etiology or population risk factor (none exist).

---

## Limitations and Future Directions

- **Tiny evidence base** (<20 patients) → frequencies, sex ratio, prognosis and natural history are imprecise.
- **Enamel-defect mechanism is inferred**, not experimentally demonstrated (no ameloblast model).
- **No germline p.R342W knock-in animal** to model the dominant-negative allele and the full tetrad (key gap).
- **No disease-specific therapy**; allele-selective silencing is a rational but untested avenue given the dominant-negative mechanism.
- **No HADDTS-specific omics atlas** (metabolomics, single-cell/spatial of patient brain) and **no methylation episignature** yet.
- Genotype–phenotype expansion (e.g., p.R36P atypical disorder) suggests the *CTBP1* phenotypic spectrum is broader than the classic tetrad and warrants systematic re-delineation.

---

### Key references (PMID)
27094857 (original 4-patient delineation) · 31041561 (7-patient cohort + mechanism/NOXA) · 36331689 (systematic review, 14 cases) · 42589715 (variant spectrum review) · 41674141 (R36P; in vivo corticogenesis; dual function) · 42704868 (18th case; floppy baby; dominant-negative) · 42123581 (mitochondrial bioenergetics) · 41459558 (isogenic iPSC model) · 34608870 (Iranian WES case) · 12101226 & 12508276 (Ctbp1/2 mouse genetics) · 32169478 & 41105133 (CtBP in cortical neurogenesis/migration) · 35455998 (BARS neuronal trafficking) · 10567582 (PLDLS corepressor mechanism) · 38626254, 41972124, 38711119, 41353240 (NAD(H)-sensing, structure, inhibitors).


## Artifacts

- [OpenScientist final report](Hypotonia_Ataxia_Developmental_Delay_And_Tooth_Enamel_Defect_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypotonia_Ataxia_Developmental_Delay_And_Tooth_Enamel_Defect_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001251` (1 mention) - the report calls it "high (most)"; HP calls it **Ataxia**
- `GO:0001764` (1 mention) - the report calls it "Cellular processes:** neural progenitor proliferation & migration"; GO calls it **neuron migration**
- `NCIT:C15917` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Arterial Embolization**
- `NCIT:C15224` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Nutrition Research, Fats**
- `NCIT:C15348` (1 mention) - the report calls it "speech-language therapy"; NCIT calls it **Vasectomy**
- `NCIT:C15491` (1 mention) - the report calls it "nutritional support/feeding management"; NCIT calls it **Premenopausal**
- `NCIT:C15587` (1 mention) - the report calls it "genetic counseling", "Counseling:** **genetic counseling"; NCIT calls it **Bone Marrow Ablation with Stem Cell Support**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001272` (2 mentions) - the report calls it "Brain MRI:** cerebellar atrophy/volume loss"; HP calls it **Cerebellar atrophy**
- `HP:0001631` (1 mention) - the report calls it "Congenital heart disease — atrial septal defect"; HP calls it **Atrial septal defect**
- `UBERON:0001017` (1 mention) - the report calls it "central nervous system", "Organ/system level — primary:** **central nervous system"; UBERON calls it **central nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0001017` - called "central nervous system", "Organ/system level — primary:** **central nervous system"
- `NCIT:C15587` - called "genetic counseling", "Counseling:** **genetic counseling"