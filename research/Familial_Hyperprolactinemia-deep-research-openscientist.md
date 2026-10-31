---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T05:37:45.042061'
end_time: '2026-10-25T05:53:12.129728'
duration_seconds: 927.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Familial Hyperprolactinemia
  mondo_id: MONDO:0014250
  category: Genetic
  causal_genes: PRLR
  omim_id: not recorded
  synonyms: familial isolated prolactin receptor deficiency; hereditary hyperprolactinemia;
    familial idiopathic hyperprolactinemia; prolactin insensitivity
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 22
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 5
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014250
    reported_labels:
    - MONDO
    ontology_label: familial hyperprolactinemia
  - term_id: HP:0000789
    reported_labels:
    - Clinical sign
    ontology_label: Infertility
  - term_id: HP:0100783
    reported_labels:
    - Lactation difficulties
    ontology_label: Breast aplasia
  - term_id: CL:0002313
    reported_labels:
    - lactotroph / prolactin-secreting cell of pituitary
    ontology_label: endocrine-paracrine cell of prostate gland
  - term_id: UBERON:0001885
    reported_labels:
    - Anterior pituitary / adenohypophysis
    ontology_label: dentate gyrus of hippocampal formation
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Hyperprolactinemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Hyperprolactinemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Hyperprolactinemia
- **MONDO ID:** MONDO:0014250 (if available)
- **Causal gene(s):** PRLR
- **OMIM:** not recorded
- **Synonyms:** familial isolated prolactin receptor deficiency; hereditary hyperprolactinemia; familial idiopathic hyperprolactinemia; prolactin insensitivity
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Familial Hyperprolactinemia** covering all of the
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

# Familial Hyperprolactinemia (PRLR): Comprehensive Disease Characteristics Report

**Disease:** Familial Hyperprolactinemia · **MONDO:** MONDO:0014250 · **OMIM:** #615555 · **Causal gene:** **PRLR** (prolactin receptor, HGNC:9446, chromosome 5p13-p12) · **Category:** Genetic (Mendelian endocrine disorder)

---

## Summary

**Familial hyperprolactinemia is a rare Mendelian endocrine disorder caused by germline loss-of-function variants in *PRLR*, the gene encoding the prolactin receptor.** The prototypical lesion is the autosomal-dominant heterozygous missense variant **p.His188Arg (c.563A>G)**, which disrupts the high-affinity ligand-binding interface of the receptor and abolishes downstream JAK2–STAT5 signaling, producing a state of **prolactin insensitivity (resistance)**. Biallelic inactivating genotypes (e.g., compound-heterozygous Pro269Leu/Arg171*) extend the spectrum to patients with hyperprolactinemia accompanied by **agalactia** (failure of lactation). Critically, this disorder is **tumor-negative**: patients have elevated serum prolactin but a **normal pituitary MRI**, distinguishing it from the far more common prolactinoma. This report concerns the PRLR (prolactin receptor) form specifically — not the prolactin ligand gene (PRL), nor pituitary-tumor genes (AIP, MEN1).

The mechanistic core is a broken negative-feedback loop. Under normal physiology, prolactin signals through PRLR on hypothalamic tuberoinfundibular dopaminergic (TIDA) neurons, which release dopamine to inhibit pituitary lactotroph prolactin secretion — a short-loop feedback circuit. When PRLR is inactivated, this feedback is lost: dopaminergic inhibitory tone on lactotrophs falls, lactotrophs are disinhibited, and prolactin secretion rises **without any tumor**. Simultaneously, peripheral tissues (breast, gonads, decidua) become resistant to the elevated prolactin, producing the clinical phenotype of oligomenorrhea/amenorrhea, infertility, and agalactia. *PRLR* knockout and heterozygous mouse models strongly corroborate this biology, recapitulating sterility, implantation failure, and gene-dosage-dependent lactation failure.

A striking feature of *PRLR* biology is **bidirectionality**: loss-of-function variants cause familial hyperprolactinemia, whereas **gain-of-function variants** (constitutively active receptors, e.g., p.Ile146Leu, p.Ile76Val) cause the opposite phenotype — benign breast tumors (multiple fibroadenomas) through ligand-independent STAT5 activation and proliferation. This report synthesizes genetics, mechanism, diagnosis, management, epidemiology, and model-organism evidence for the loss-of-function disease, with explicit ontology term suggestions and primary-literature citations throughout. Because the disorder is ultra-rare (only a handful of kindreds described worldwide since 2013), several template sections are necessarily sparse, and those gaps are flagged explicitly.

---

## 1. Disease Information

**Overview.** Familial hyperprolactinemia is a hereditary form of non-physiological hyperprolactinemia in which serum prolactin is persistently elevated due to inherited inactivation of the prolactin receptor, *not* due to a prolactin-secreting pituitary adenoma, drug exposure, hypothyroidism, renal failure, or other secondary cause. It is a **diagnosis of exclusion** confirmed by identifying a pathogenic germline *PRLR* variant. Clinically, affected individuals (predominantly women identified to date) present with menstrual irregularity, infertility, and — in biallelic/strongly inactivating genotypes — failure of lactation (agalactia).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014250 |
| OMIM (phenotype) | #615555 (Hyperprolactinemia) |
| Gene | *PRLR*, HGNC:9446; NCBI Gene 5618; Ensembl ENSG00000113494; UniProt P16471; OMIM gene *176761 |
| ICD-10 | E22.1 (Hyperprolactinemia) |
| ICD-11 | 5A60.1 (Hyperprolactinaemia) |
| MeSH | D006966 (Hyperprolactinemia) |
| Orphanet | Rare hyperprolactinemia (no dedicated PRLR-specific ORPHA code at time of writing) |

**Synonyms / alternative names:** familial isolated prolactin receptor deficiency; hereditary hyperprolactinemia; familial idiopathic hyperprolactinemia; prolactin insensitivity; prolactin resistance.

**Data provenance:** Information is derived from **aggregated disease-level resources** (OMIM, PubMed case reports and kindred studies) and functional in-vitro/model-organism work, rather than large EHR cohorts. The disease is defined by a small number of published families; there is no population registry specific to the *PRLR* form.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by germline **loss-of-function variants in *PRLR***. Two inheritance architectures are documented:

- **Autosomal dominant** via a heterozygous inactivating missense variant (**p.His188Arg**), which behaves dominantly (haploinsufficiency and/or dominant-negative effect on receptor dimers). This was the founding observation in three affected sisters [PMID: 24195502](https://pubmed.ncbi.nlm.nih.gov/24195502/).
- **Autosomal recessive / biallelic** via compound-heterozygous inactivating variants (**Pro269Leu / Arg171\***), associated with hyperprolactinemia plus agalactia [PMID: 36445946](https://pubmed.ncbi.nlm.nih.gov/36445946/).

**Genetic risk factors.** The causal variants themselves are the risk factors; no separate susceptibility loci or GWAS signals are established for this Mendelian condition. Modifier genes are unknown.

**Environmental risk factors.** None established for the *PRLR* form. (For hyperprolactinemia in general, drugs — especially dopamine-antagonist antipsychotics such as paliperidone/risperidone — hypothyroidism, chest-wall stimulation, stress, and renal failure are classic secondary causes, but these are *differentials* to be excluded, not causes of the familial disease.)

**Protective factors.** None established. No protective *PRLR* alleles are described for this phenotype.

**Gene–environment interactions.** Not characterized. Physiological states that elevate prolactin (pregnancy, lactation, estrogen exposure) may interact with reduced receptor signaling, but this is inferred rather than demonstrated.

---

## 3. Phenotypes

Phenotypes reflect both **central disinhibition** (elevated prolactin) and **peripheral prolactin resistance** (end-organ non-response). Because reported kindreds are tiny, frequencies are qualitative.

| Phenotype | Type | HPO suggestion | Onset | Severity / frequency | Evidence |
|---|---|---|---|---|---|
| Elevated serum prolactin / hyperprolactinemia | Laboratory abnormality | HP:0000870 (Hyperprolactinemia) | Adult (reproductive age) | Defining feature; all affected | [PMID: 24195502](https://pubmed.ncbi.nlm.nih.gov/24195502/) |
| Oligomenorrhea / amenorrhea | Clinical sign | HP:0000876 / HP:0000141 | Adolescence–adulthood | Common in affected women | [PMID: 24195502](https://pubmed.ncbi.nlm.nih.gov/24195502/) |
| Infertility / subfertility | Clinical sign | HP:0000789 | Reproductive age | Variable | Human + model [PMID: 9009200](https://pubmed.ncbi.nlm.nih.gov/9009200/) |
| Agalactia / failure of lactation | Clinical sign | HP:0100783 (Lactation difficulties) | Postpartum | Seen with biallelic/strong LOF | [PMID: 36445946](https://pubmed.ncbi.nlm.nih.gov/36445946/) |
| Absence of galactorrhea | Distinguishing feature | — | — | Contrasts with prolactinoma | Inferred from resistance |

**Quality-of-life impact.** Chiefly reproductive and psychosocial: infertility, menstrual disturbance, and inability to breastfeed. The condition is **not life-threatening** and does not itself cause mass effect, visual loss, or hypopituitarism (those belong to prolactinoma). No disease-specific EQ-5D/SF-36 data exist for the *PRLR* form.

**Note on peripheral resistance paradox:** Because end-organs are prolactin-resistant, classic high-prolactin signs that depend on prolactin *action* (e.g., galactorrhea) may be **absent or muted**, even though circulating prolactin is high — a clinically important distinction from prolactinoma.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PRLR* (prolactin receptor), a class-1 cytokine-receptor-superfamily single-pass transmembrane receptor. OMIM gene *176761; HGNC:9446.

**Pathogenic variants (documented):**

| Variant (protein) | cDNA | Zygosity | Classification | Type | Consequence | Phenotype | Evidence |
|---|---|---|---|---|---|---|---|
| p.His188Arg | c.563A>G | Heterozygous | Pathogenic | Missense | Loss of function (disrupts ligand binding; abolishes JAK2-STAT5) | Familial hyperprolactinemia (AD) | [PMID: 24195502](https://pubmed.ncbi.nlm.nih.gov/24195502/), confirmed [PMID: 36445946](https://pubmed.ncbi.nlm.nih.gov/36445946/) |
| p.Pro269Leu + p.Arg171* | — | Compound het | Pathogenic | Missense + nonsense | Biallelic inactivation | Hyperprolactinemia + agalactia | [PMID: 36445946](https://pubmed.ncbi.nlm.nih.gov/36445946/) |
| p.Ser434Phe | c.1301C>T | Heterozygous | Candidate (missense) | Missense | Proposed hyperprolactinemia association | Familial idiopathic hyperprolactinemia | [PMID: 39355173](https://pubmed.ncbi.nlm.nih.gov/39355173/) |

**Gain-of-function counterparts (opposite disease pole — benign breast tumors, NOT hyperprolactinemia):** p.Ile146Leu and p.Ile76Val confer constitutive, ligand-independent activity [PMID: 18779591](https://pubmed.ncbi.nlm.nih.gov/18779591/), [PMID: 19897676](https://pubmed.ncbi.nlm.nih.gov/19897676/). A rare activating p.Asn492Ile has been linked to increased prolactinoma incidence [PMID: 36445946](https://pubmed.ncbi.nlm.nih.gov/36445946/).

**Allele frequency.** The pathogenic loss-of-function variants are extremely rare / private to the described kindreds; they are not common polymorphisms in gnomAD. By contrast, p.Ile76Val and p.Ile146Leu are relatively common in the general population and, in a separate study, had no effect on signaling after prolactin stimulation and were **not** associated with sporadic prolactinoma [PMID: 26641246](https://pubmed.ncbi.nlm.nih.gov/26641246/) — underscoring that variant interpretation must be functional, not frequency-only.

**Origin.** Germline (constitutional); no somatic involvement in this disease.

**Functional consequence.** Loss of function (His188Arg, Arg171*, Pro269Leu). His188Arg disrupts the high-affinity ligand-binding interface, so prolactin cannot productively engage the receptor, abolishing JAK2–STAT5 phosphorylation.

**Modifier genes / epigenetics / chromosomal abnormalities.** None established for this disorder. No methylation, histone, or large structural lesions are implicated; this is a single-gene coding-variant disease.

---

## 5. Environmental Information

No **environmental, lifestyle, or infectious** agents cause the familial *PRLR* disease — it is monogenic. These categories are relevant only to the **secondary hyperprolactinemias** that must be excluded during workup: dopamine-antagonist drugs (antipsychotics, metoclopramide), estrogens, primary hypothyroidism, chronic kidney disease, chest-wall trauma/stimulation, and stress. (Example drug signal: paliperidone palmitate strongly associated with increased blood prolactin and galactorrhea in pharmacovigilance data, [PMID: 39833706](https://pubmed.ncbi.nlm.nih.gov/39833706/).) CHEBI entities relevant to differentials/therapy: dopamine (CHEBI:18243), cabergoline (CHEBI:3286), bromocriptine (CHEBI:3181).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Germline inactivating *PRLR* variant** (e.g., His188Arg) **results in** a prolactin receptor that cannot bind ligand at its high-affinity interface (demonstrated in vitro) [PMID: 24195502].
2. Defective ligand binding **leads to** failure of receptor dimerization/activation and **abolishes** JAK2 autophosphorylation and STAT5 phosphorylation — i.e., **prolactin insensitivity / resistance** (demonstrated in vitro) [PMID: 24195502].
3. **Branch A — Central disinhibition (drives the hyperprolactinemia):** Loss of functional PRLR on hypothalamic **tuberoinfundibular dopaminergic (TIDA) neurons results in** failure of prolactin's short-loop negative feedback. Normally prolactin activates TIDA neurons, which release dopamine to inhibit lactotrophs (demonstrated in mouse) [PMID: 30759390]. Without feedback, **dopaminergic inhibitory tone on pituitary lactotrophs falls** (inferred in humans; demonstrated feedback circuit in mouse).
4. Reduced dopamine **leads to disinhibition of anterior-pituitary lactotrophs**, which **results in increased prolactin secretion** → **tumor-negative hyperprolactinemia** (inferred for humans, consistent with normal MRI) [PMID: 24195502; 30759390].
5. **Branch B — Peripheral resistance (drives the clinical signs):** Inactive PRLR in **gonadal axis, mammary epithelium, and decidua results in** end-organ non-response to the (now elevated) prolactin → **oligomenorrhea/amenorrhea, infertility, and agalactia** (human phenotype; corroborated by *Prlr*-null/heterozygous mice) [PMID: 9009200; 10935023; 36445946].

```
 PRLR LOF variant (His188Arg)
          │ abolishes ligand binding
          ▼
 No JAK2–STAT5 signaling  = PROLACTIN RESISTANCE
          │
   ┌──────┴───────────────────────────┐
   ▼ (central)                          ▼ (peripheral)
 TIDA neurons lose PRL feedback     Breast / gonad / decidua
   │ ↓ dopamine release               unresponsive to PRL
   ▼                                   │
 Lactotrophs disinhibited             ▼
   │ ↑ PRL secretion               Amenorrhea, infertility,
   ▼                                agalactia
 HYPERPROLACTINEMIA (no tumor)
```

### Detail by category

- **Molecular pathways:** JAK2–STAT5 is the canonical prolactin pathway (Reactome "Prolactin receptor signaling"; also PI3K-AKT and MAPK contributions). Its loss is the central defect [PMID: 24195502; 10596761].
- **Cellular processes:** Failure of prolactin-driven mammary alveologenesis/differentiation and corpus-luteum support; decidual regulation disrupted (prolactin normally silences IL-6 and 20α-HSD in decidua via JAK2-STAT5) [PMID: 17255200].
- **Protein dysfunction:** Loss of function via disrupted extracellular ligand-binding interface (His188Arg); truncation (Arg171*). No aggregation/misfolding described.
- **Immune/inflammatory, metabolic, oxidative:** Not primary features of the *PRLR* disease.
- **GO term suggestions:** GO:0038161 (prolactin signaling pathway), GO:0007565 (female pregnancy), GO:0007595 (lactation), GO:0046543 (development of secondary female sexual characteristics), GO:0007259 (JAK-STAT cascade).
- **CL term suggestions:** CL:0002313 (lactotroph / prolactin-secreting cell of pituitary), CL:0000700 (dopaminergic neuron / TIDA neuron), CL:0002326 (luminal epithelial cell of mammary gland).

---

## 7. Anatomical Structures Affected

**Organ level (endocrine system, UBERON:0000949):**
- **Hypothalamus** (UBERON:0001898) — TIDA neurons; site of feedback failure.
- **Anterior pituitary / adenohypophysis** (UBERON:0001885) — disinhibited lactotrophs; the source of excess prolactin, yet **structurally normal (no adenoma)**.
- **Mammary gland / breast** (UBERON:0001911) — prolactin-resistant; agalactia.
- **Ovary / gonads** (UBERON:0000992) and **uterus/decidua** (UBERON:0000995) — reproductive dysfunction, implantation failure (model).

**Tissue/cell level:** pituitary lactotrophs (CL:0002313); hypothalamic dopaminergic neurons (CL:0000700); mammary luminal epithelium (CL:0002326); granulosa/corpus luteum cells.

**Subcellular level (GO Cellular Component):** plasma membrane receptor (GO:0005886); downstream cytoplasmic JAK2 and nuclear STAT5 (GO:0005634 nucleus for STAT5 transcriptional action).

**Localization/lateralization:** Bilateral/systemic (endocrine); no lateralization.

---

## 8. Temporal Development

- **Onset:** Insidious, typically recognized in **adult reproductive age**, when menstrual disturbance, infertility, or postpartum lactation failure prompts evaluation.
- **Progression:** **Stable/chronic**, non-progressive. There is no mass lesion to grow and no evidence of neurodegeneration. Prolactin elevation is persistent.
- **Course:** Lifelong (germline). The heterozygous-mouse lactation phenotype is notably **age- and parity-dependent** — near-complete lactation failure after a first pregnancy when mated young (6–8 wk), attenuated when mated at 20 wk, and absent after a second pregnancy [PMID: 10935023] — suggesting biological windows (parity/age) can modulate expressivity.
- **Remission/critical periods:** No spontaneous remission of the genetic defect; reproductive windows are the main intervention periods.

---

## 9. Inheritance and Population

**Epidemiology.** No reliable prevalence/incidence figures exist for the *PRLR*-specific disease — it is **ultra-rare**, described in only a few kindreds since 2013. (Hyperprolactinemia overall is common, but the genetic *PRLR* subset is a tiny fraction.) Germline *PRLR* mutation is **not** a major cause of sporadic prolactinoma [PMID: 26641246](https://pubmed.ncbi.nlm.nih.gov/26641246/).

**Inheritance pattern.** Both documented: **autosomal dominant** (heterozygous His188Arg) and **autosomal recessive/biallelic** (compound-het Pro269Leu/Arg171*).

**Penetrance / expressivity.** Appears high for the biochemical trait (hyperprolactinemia) in reported dominant kindreds but with **variable clinical expressivity** (menstrual/fertility/lactation phenotypes vary). Model data imply **gene-dosage and age/parity-dependent** expressivity.

**Anticipation, mosaicism, founder effects, consanguinity, carrier frequency:** Not established / insufficient data. Variants appear private to families.

**Demographics.** Reported patients are predominantly **female** (ascertainment via reproductive phenotypes); male carriers may be underrecognized given subtler phenotypes. No defined ethnic/geographic clustering.

---

## 10. Diagnostics

**Diagnostic strategy (diagnosis of exclusion → genetic confirmation):**

1. **Confirm true hyperprolactinemia** — repeat serum prolactin; prolactin threshold >20 ng/mL (men) / >25 ng/mL (women) for non-physiological elevation [PMID: 39355173].
2. **Exclude macroprolactinemia** by PEG precipitation (big-big prolactin/anti-PRL IgG complexes). Macroprolactinemia accounts for **10–25%** of hyperprolactinemic patients and ~**3.7%** of the general population [PMID: 23304187](https://pubmed.ncbi.nlm.nih.gov/23304187/); in one Chinese cohort it was **22.9%** of hyperprolactinemic patients [PMID: 34620143](https://pubmed.ncbi.nlm.nih.gov/34620143/). Clinical features alone cannot reliably distinguish it [PMID: 22313536; 21527183].
3. **Exclude secondary causes** — drugs (dopamine antagonists), hypothyroidism, renal failure, pregnancy, chest-wall stimulation — per the Endocrine Society guideline [PMID: 21296991](https://pubmed.ncbi.nlm.nih.gov/21296991/).
4. **Pituitary MRI** — must be **NORMAL** (no micro-/macroadenoma). MRI is essential because prolactin level correlates imperfectly with adenoma presence (optimal cutoff ~38.7 ng/mL in one series) [PMID: 39792709].
5. **Genetic testing** — single-gene *PRLR* sequencing or **whole-exome sequencing (WES)** to identify the pathogenic variant [PMID: 24195502; 39355173]. WES has been the discovery modality in reported families.

**Clinical lab/ontology:** serum prolactin (LOINC 15081-0). Differential diagnosis includes prolactinoma, macroprolactinemia, drug-induced hyperprolactinemia, hypothyroidism, PCOS (where hyperprolactinemia may coexist or mask PCOS — PCOS is itself a diagnosis of exclusion) [PMID: 21388855].

**Omics/biopsy/screening:** No specific omics diagnostic; no biopsy; no population newborn screening. **Cascade genetic testing** of relatives is appropriate once a familial variant is identified.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Not reduced** by the disease itself; it is non-malignant and non-life-threatening. No disease-specific mortality.
- **Morbidity/function:** Reproductive morbidity (infertility, menstrual disturbance, agalactia) and associated psychosocial burden.
- **Complications:** Chronic hyperprolactinemia generally (across causes) has been associated with sequelae such as hypogonadism and, in dopamine-agonist-treated cohorts, a modestly increased ischemic-stroke signal [PMID: 39924868] — but these data are not specific to the *PRLR* form and treatment context differs.
- **Recovery/prognostic factors:** Prognosis is favorable; the condition is stable. Because peripheral tissues are resistant, standard dopamine-agonist lowering of prolactin may not reverse end-organ symptoms the way it does in prolactinoma — a key prognostic/therapeutic distinction (inferred from resistance mechanism).

---

## 12. Treatment

**There is no cure; management is supportive and reproductive-endocrine, not tumor-directed.** Because the defect is receptor *resistance*, lowering prolactin pharmacologically does not restore prolactin signaling at resistant end-organs.

- **Dopamine agonists** (cabergoline — NCIT:C1868; bromocriptine — NCIT:C372) are first-line for hyperprolactinemia generally and may normalize prolactin levels [PMID: 21296991; 40966237], but their benefit in a *resistance* disorder is limited to lowering the circulating level rather than correcting end-organ non-response. Cabergoline is generally preferred for efficacy/tolerability; intolerance occurs in 3–12% [PMID: 37027090]. Dopamine agonists carry impulse-control-disorder risk (7.5–46% in prolactinoma/hyperprolactinemia cohorts) [PMID: 40316139].
- **Reproductive management:** assisted reproduction/fertility support for infertility; counseling regarding inability to breastfeed (agalactia).
- **Gene/cell/RNA/targeted/immuno-therapies:** None approved or in trials for this indication. No surgical role (no tumor).
- **Pharmacogenomics:** None specific.

**Guideline anchor:** Endocrine Society clinical practice guideline on hyperprolactinemia [PMID: 21296991](https://pubmed.ncbi.nlm.nih.gov/21296991/); Pituitary Society prolactinoma guidelines for differential context [PMID: 16886971].

---

## 13. Prevention

- **Primary prevention:** Not applicable (germline).
- **Secondary prevention:** **Cascade genetic screening** of at-risk relatives after a familial *PRLR* variant is identified; early recognition avoids misdiagnosis as prolactinoma and unnecessary imaging/pharmacotherapy.
- **Genetic counseling:** Essential — discuss autosomal dominant vs biallelic transmission, variable expressivity, and reproductive planning (NSGC/ACMG frameworks; preimplantation/prenatal options could be discussed though rarely indicated given benign course).
- **Immunization / public health / environmental:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Prlr* is conserved in mouse (NCBI Gene 19116; *Mus musculus*, NCBI:txid10090) and rat (*Rattus norvegicus*, NCBI:txid10116). High evolutionary conservation of the prolactin–PRLR–JAK2–STAT5 axis.
- **Natural disease:** No well-characterized spontaneous *PRLR*-deficiency hyperprolactinemia syndrome is catalogued in companion animals/wildlife (OMIA search not definitive). Prolactin/PRLR variation in livestock affects reproduction/lactation traits but is not framed as this disease.
- **Comparative biology:** Engineered mouse knockouts (below) are the main cross-species evidence; mechanisms (lactation, implantation, feedback) are strongly conserved.
- **Zoonotic potential:** None (genetic disease).

---

## 15. Model Organisms

**Mouse (*Mus musculus*) — the principal model.**

| Model | Key phenotype | Relevance to human disease | Evidence |
|---|---|---|---|
| *Prlr*-null (homozygous KO) | Female **sterility** from complete implantation failure; irregular cycles, reduced fertilization, defective preimplantation development, no pseudopregnancy; ~50% of males infertile/subfertile | Establishes PRLR as essential reproductive/lactation regulator; models peripheral-resistance phenotype | [PMID: 9009200](https://pubmed.ncbi.nlm.nih.gov/9009200/) |
| *Prlr* heterozygous (+/−) | Near-complete **lactation failure after first pregnancy** (young dams), rescued at 20 wk or second pregnancy; smaller, less-branched mammary glands | Models autosomal-dominant, **gene-dosage- and age-dependent** human phenotype | [PMID: 10935023](https://pubmed.ncbi.nlm.nih.gov/10935023/) |
| Conditional neuronal *Prlr* deletion | Prolactin drives TIDA dopaminergic neuron signaling (short-loop feedback) | Mechanistic basis for central disinhibition → hyperprolactinemia | [PMID: 30759390](https://pubmed.ncbi.nlm.nih.gov/30759390/) |
| Neutralizing anti-PRLR antibody (pharmacologic) | Reversible infertility, mammary involution, impaired lactation — phenocopies KO | Validates PRLR blockade = disease phenotype | [PMID: 26284426](https://pubmed.ncbi.nlm.nih.gov/26284426/) |

**Phenotype recapitulation:** Excellent for reproductive/lactation features and for the central-feedback mechanism. **Limitations:** Mouse models were engineered knockouts rather than the human point mutation; homozygous sterility prevents some multigenerational study; human dominant hyperprolactinemia biochemistry is better captured mechanistically than quantitatively. Resources: MGI, IMPC, IMSR.

---

## Mechanistic Model / Interpretation

The unifying model is a **two-compartment consequence of one molecular lesion**. A loss-of-function *PRLR* allele simultaneously (1) disables the hypothalamic brake on prolactin secretion and (2) deafens peripheral tissues to the hormone. Compartment 1 explains the paradox at the heart of the disease — **high prolactin with no tumor** — because the elevation is driven by lost dopaminergic feedback rather than autonomous adenoma secretion. Compartment 2 explains why the clinical signs (amenorrhea, infertility, agalactia) are those of prolactin *deficiency of action* despite prolactin *excess in blood*. This resolves what would otherwise look contradictory and is the single most important interpretive point for a clinician: in familial *PRLR* hyperprolactinemia, the number is high but the hormone "isn't working."

The **bidirectionality** of *PRLR* reinforces the model's logic. If loss of signaling disinhibits prolactin and deafens tissues, then **gain** of signaling (constitutive receptors: I146L, I76V) should produce ligand-independent proliferation in prolactin-responsive epithelium — and indeed these variants cause benign breast fibroadenomas [PMID: 18779591; 19897676]. The same receptor, read in opposite directions, yields opposite diseases.

```
      LOSS of function            GAIN of function
   (His188Arg, Arg171*)          (Ile146Leu, Ile76Val)
            │                             │
   prolactin resistance          constitutive STAT5 activation
            │                             │
   ▼ feedback / ▼ action          ▲ proliferation
            │                             │
  FAMILIAL HYPERPROLACTINEMIA     BENIGN BREAST FIBROADENOMAS
     (tumor-negative)
```

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [24195502](https://pubmed.ncbi.nlm.nih.gov/24195502/) | *Mutant prolactin receptor and familial hyperprolactinemia* | **Founding evidence**: His188Arg LOF disrupts ligand binding, abolishes JAK2-STAT5; segregates in 3 sisters; no tumor/MEN |
| [36445946](https://pubmed.ncbi.nlm.nih.gov/36445946/) | *PRLR variants with diverse effects on signalling* | Confirms His188Arg inactivating; biallelic Pro269Leu/Arg171* with agalactia; notes activating Asn492Ile/prolactinoma |
| [30759390](https://pubmed.ncbi.nlm.nih.gov/30759390/) | *Elevated prolactin drives TIDA neuron switch* | Mechanism: PRL short-loop feedback on dopaminergic neurons |
| [9009200](https://pubmed.ncbi.nlm.nih.gov/9009200/) | *Null mutation of Prlr — reproductive defects* | KO mouse: sterility, implantation failure |
| [10935023](https://pubmed.ncbi.nlm.nih.gov/10935023/) | *Mammary gland development in Prlr KO* | Dominant, dosage/age-dependent lactation failure in het mice |
| [18779591](https://pubmed.ncbi.nlm.nih.gov/18779591/) | *Gain-of-function PRLR mutation in benign breast tumors* | Opposite pole: constitutive activity, fibroadenomas |
| [19897676](https://pubmed.ncbi.nlm.nih.gov/19897676/) | *Two constitutively active PRLR variants (95 women)* | Confirms I146L and I76V constitutive activity |
| [26641246](https://pubmed.ncbi.nlm.nih.gov/26641246/) | *Germline PRLR not major cause of sporadic prolactinoma* | Boundary: common PRLR variants functionally neutral |
| [21296991](https://pubmed.ncbi.nlm.nih.gov/21296991/) | *Endocrine Society hyperprolactinemia guideline* | Diagnostic/therapeutic framework |
| [23304187](https://pubmed.ncbi.nlm.nih.gov/23304187/) | *Macroprolactinemia significance* | Quantifies key differential (10–25%) |
| [39355173](https://pubmed.ncbi.nlm.nih.gov/39355173/) | *Ser434Phe PRLR* | Additional candidate variant; WES approach |

**Key verified quotes:**
- "This substitution disrupted the high-affinity ligand-binding interface of the prolactin receptor, resulting in a loss of downstream signaling by Janus kinase 2 (JAK2) and signal transducer and activator of transcription 5 (STAT5)" — [PMID: 24195502].
- "an inactivating germline heterozygous PRLR variant (His188Arg) was reported in a kindred with hyperprolactinaemia, while an inactivating compound heterozygous PRLR variant (Pro269Leu/Arg171Stop) was identified in an individual with hyperprolactinaemia and agalactia" — [PMID: 36445946].
- "Homozygous females were sterile owing to a complete failure of embryonic implantation... Half of the homozygous males were infertile or showed reduced fertility." — [PMID: 9009200].
- "Heterozygous females showed almost complete failure of lactation following their first pregnancy when mated at 6-8 weeks of age." — [PMID: 10935023].
- "These neurons normally release dopamine to inhibit prolactin secretion and are activated by prolactin in a short-loop feedback manner." — [PMID: 30759390].
- "This sole substitution was sufficient to confer constitutive activity to the receptor variant" — [PMID: 18779591].
- "The prevalence of macroprolactinemia is 10-25% in patients with hyperprolactinemia and 3.7% in general population." — [PMID: 23304187].

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity:** Only a handful of kindreds/variants are published. Prevalence, incidence, penetrance estimates, sex ratio, and geographic/founder data are essentially unknown.
2. **Human central mechanism is inferred:** The TIDA-feedback disinhibition step is demonstrated in mouse; direct human hypothalamic evidence is lacking. Labeled as inference throughout.
3. **Variant interpretation:** Several *PRLR* missense variants are common and functionally neutral [PMID: 26641246]; candidate variants (e.g., Ser434Phe) need functional confirmation. Not all reported variants are ACMG-classified pathogenic.
4. **Therapeutics:** No disease-specific trials. Whether dopamine agonists meaningfully help a resistance disorder is untested; end-organ resistance predicts limited symptomatic benefit.
5. **Male and multigenerational phenotype** underdescribed due to ascertainment bias toward reproductive-age women.
6. **No omics/epigenetic/structural data** specific to the human disease.

---

## Proposed Follow-up Experiments / Actions

1. **Functional assays** (JAK2/STAT5 reporter, ligand-binding) for all newly reported *PRLR* variants (e.g., Ser434Phe) to resolve pathogenicity per ACMG PS3.
2. **International kindred registry / GeneMatcher outreach** to aggregate cases, estimate penetrance/expressivity, and define male phenotype.
3. **Knock-in mouse (His188Arg)** modeling the exact human dominant allele to test whether it reproduces hyperprolactinemia (not just reproductive phenotypes) and to directly measure TIDA dopaminergic tone.
4. **Human hypothalamic-pituitary feedback testing** (dynamic prolactin/dopamine axis studies) in affected carriers to confirm the central-disinhibition mechanism.
5. **Therapeutic evaluation**: prospective assessment of whether prolactin-lowering alters reproductive outcomes in confirmed carriers, versus assisted-reproduction-first strategies.
6. **Structural modeling (AlphaFold/cryo-EM)** of His188Arg/Pro269Leu to map how each disrupts the ligand interface and dimerization.

---

*Report compiled from 5 discovery iterations, 5 confirmed findings, and 39 reviewed papers. Evidence types: human clinical/genetic (kindreds, guidelines), model organism (mouse KO/het, antibody), in vitro functional (signaling assays), and computational/inferential (central-feedback extrapolation).*


## Artifacts

- [OpenScientist final report](Familial_Hyperprolactinemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Hyperprolactinemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014250` (2 mentions) - the report calls it "MONDO"; MONDO calls it **familial hyperprolactinemia**
- `HP:0000789` (1 mention) - the report calls it "Clinical sign"; HP calls it **Infertility**
- `HP:0100783` (1 mention) - the report calls it "Lactation difficulties"; HP calls it **Breast aplasia**
- `CL:0002313` (2 mentions) - the report calls it "lactotroph / prolactin-secreting cell of pituitary"; CL calls it **endocrine-paracrine cell of prostate gland**
- `UBERON:0001885` (1 mention) - the report calls it "Anterior pituitary / adenohypophysis"; UBERON calls it **dentate gyrus of hippocampal formation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000870` (1 mention) - the report calls it "Hyperprolactinemia"; HP calls it **Increased circulating prolactin concentration**, and lists "Hyperprolactinemia" among its other names
- `GO:0046543` (1 mention) - the report calls it "development of secondary female sexual characteristics"; GO calls it **development of animal secondary female sexual characteristics**, and lists "development of secondary female sexual characteristics" among its other names
- `GO:0007259` (1 mention) - the report calls it "JAK-STAT cascade"; GO calls it **cell surface receptor signaling pathway via JAK-STAT**, and lists "JAK-STAT cascade" among its other names
- `CL:0000700` (2 mentions) - the report calls it "dopaminergic neuron / TIDA neuron"; CL calls it **dopaminergic neuron**
- `UBERON:0001911` (1 mention) - the report calls it "Mammary gland / breast"; UBERON calls it **mammary gland**
- `UBERON:0000992` (1 mention) - the report calls it "Ovary / gonads"; UBERON calls it **ovary**
- `UBERON:0000995` (1 mention) - the report calls it "uterus/decidua"; UBERON calls it **uterus**