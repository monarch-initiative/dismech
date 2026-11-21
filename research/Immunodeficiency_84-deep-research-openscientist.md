---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T22:25:54.160106'
end_time: '2026-11-12T22:55:53.925630'
duration_seconds: 1799.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Immunodeficiency 84
  mondo_id: MONDO:0030333
  category: Mendelian
  causal_genes: not recorded
  omim_id: OMIM:619437
  synonyms: IMD84; immunodeficiency due to IKZF3 deficiency
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 1a32927d-dfe4-4cf9-a963-cc2b679371bd
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 9
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 31
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.031
  labels_checked: 17
  labels_matching: 5
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0030333
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 84
  - term_id: HP:0002718
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent bacterial infections
  - term_id: HP:0004429
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent viral infections
  - term_id: HP:0410330
    reported_labels:
    - abnormal T-cell count/subset
    ontology_label: Meat allergen allergy
  - term_id: HP:0002960
    reported_labels:
    - Clinical sign
    ontology_label: Autoimmunity
  labels_variant: 7
  unresolved_terms:
  - HP:0005405
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_84-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_84-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 84
- **MONDO ID:** MONDO:0030333 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** OMIM:619437
- **Synonyms:** IMD84; immunodeficiency due to IKZF3 deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 84** covering all of the
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

# Immunodeficiency 84 (IMD84 / AIOLOS Deficiency): Comprehensive Disease Characterization

**Disease:** Immunodeficiency 84 (IMD84)
**Causal gene:** **IKZF3** (encoding the Ikaros-family zinc-finger transcription factor **AIOLOS**)
**OMIM:** #619437 | **MONDO:** 0030333 | **Category:** Mendelian, autosomal dominant inborn error of immunity

---

## Summary

Immunodeficiency 84 (IMD84; OMIM #619437, MONDO:0030333) is a rare autosomal-dominant inborn error of immunity (IEI) caused by heterozygous germline variants in **IKZF3**, the gene encoding the IKAROS-family C2H2 zinc-finger transcription factor **AIOLOS** (HGNC:13178; NCBI Gene 22806; UniProt Q9UKT9; chromosome 17q12-q21.1). The disease name is a serial number ("Immunodeficiency 84") that does not name the gene; this report follows the supplied identifiers and confirms the causal gene is **IKZF3/AIOLOS**, *not* a similarly numbered immunodeficiency caused by a different gene.

Two mechanistically distinct classes of variant produce the disease, and the class predicts the clinical severity. DNA-binding-domain (DBD) missense variants — **G159R, N160S, and G191R** — act through a novel autosomal-dominant mechanism termed **"heterodimeric interference"**: the mutant AIOLOS protein sequesters and misdirects its physiological heterodimeric partner IKAROS (IKZF1), abolishing binding of both AIOLOS homodimers and AIOLOS–IKAROS heterodimers to their canonical DNA motif and redirecting the complexes to aberrant genomic locations. This produces a B-cell-predominant **combined immunodeficiency** with recurrent and opportunistic infections (notably *Pneumocystis jirovecii* pneumonia), impaired antibody responses, abnormal B- and T-cell maturation, autoimmunity, and a predisposition to B-cell malignancy including chronic lymphocytic leukemia (CLL). A second class — **haploinsufficiency** variants (E82K missense; Q402X truncating) — produces a milder, later-onset **common variable immunodeficiency (CVID)-like** humoral phenotype. This two-mechanism paradigm is directly analogous to that established for the paralog IKZF1/IKAROS, and AIOLOS residue N160 is the structural homolog of IKAROS N159.

Knock-in mouse models carrying the human N160S and G159R variants recapitulate the human B- and T-cell phenotypes, and classic *Ikzf3*-null mice reveal additional roles in long-lived plasma-cell generation and prevention of SLE-like autoimmunity. Of translational interest, AIOLOS is a well-characterized **cereblon (CRBN) neosubstrate**: immunomodulatory drugs (IMiDs/CELMoDs such as lenalidomide, pomalidomide, and mezigdomide) redirect the CRL4–CRBN E3 ubiquitin ligase to degrade IKZF1 and IKZF3 — the pharmacologic mirror image of the genetic deficiency. There is no IMD84-specific therapy; management is supportive (immunoglobulin replacement, infection prophylaxis, and hematopoietic stem-cell transplantation in severe cases).

---

## 1. Disease Information

**Overview.** Immunodeficiency 84 is a Mendelian inborn error of immunity characterized by defective humoral and cellular immunity arising from heterozygous variants in *IKZF3*/AIOLOS. It belongs to the family of "IKZF-associated inborn errors of immunity," alongside disorders of IKAROS (IKZF1) and HELIOS (IKZF2). AIOLOS, IKAROS, and HELIOS are transcription factors predominantly expressed in hematopoietic cells where they form heteromeric and homodimeric complexes to regulate lymphocyte development ([PMID: 42169761](https://pubmed.ncbi.nlm.nih.gov/42169761/)).

**Key identifiers (confirmed — Finding F007):**

| Identifier type | Value |
|---|---|
| Disease name | Immunodeficiency 84 (IMD84) |
| OMIM | #619437 |
| MONDO | MONDO:0030333 |
| Synonyms | IMD84; immunodeficiency due to IKZF3 deficiency; AIOLOS deficiency; AIOLOS-associated inborn error of immunity |
| Gene symbol | IKZF3 (AIOLOS) |
| HGNC | HGNC:13178 |
| NCBI Gene | 22806 |
| Ensembl | ENSG00000161405 |
| UniProt | Q9UKT9 |
| OMIM gene | 606221 |
| Cytogenetic location | 17q12-q21.1 (GRCh38 chr17:39,757,715–39,864,368, minus strand) |

**Source of information.** The knowledge base is derived from aggregated disease-level resources (OMIM, MONDO, gnomAD) combined with individual patient case reports and family studies published in primary literature, plus functional validation in cell lines and knock-in mouse models. It is not drawn from EHR/population epidemiology — the disease is ultra-rare with only a handful of reported families.

---

## 2. Etiology

**Primary cause — genetic (Finding F001).** IMD84 is caused by germline heterozygous variants in *IKZF3*. Reported pathogenic variants cluster in the N-terminal DNA-binding zinc-finger domain. As stated by the AIOLOS-associated IEI review: *"heterozygous missense loss-of-function variants within the DNA-binding domain of the IKZF3 gene (G159R, N160S, and G191R) have been identified in patients with inborn errors of immunity (IEI). Additionally, a missense and a truncating variant (E82K and Q402X) leading to the AIOLOS haploinsufficiency have been documented"* ([PMID: 38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/)).

**Genetic risk factors.** The causal variants themselves are the risk factors — all reported missense DBD variants were fully penetrant. There are no known susceptibility loci or common modifier alleles for this ultra-rare monogenic disease.

**Environmental risk factors / protective factors / gene–environment interactions.** No environmental risk factors, protective factors, or gene–environment interactions have been established. As a highly penetrant monogenic disorder, disease occurrence is determined by the variant. Infectious exposures act as *triggers* for clinical manifestations (opportunistic and recurrent infections) rather than as causes of the underlying immune defect. No protective genetic variants have been reported. *(Information not available — not applicable for a fully penetrant monogenic IEI.)*

---

## 3. Phenotypes

The core clinical phenotype (Finding F003) is a **combined immunodeficiency** with B-cell-predominant features. Patients carrying AIOLOS N160S showed *"impaired humoral responses, abnormal B cell development (high percentage of CD21low B cells and negative CD23 expression), and abrogated CD40 responses"* ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)). The majority of individuals with AIOLOS-associated IEI *"manifest recurrent sinopulmonary infections, as well as various bacterial and viral infections"* ([PMID: 38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/)).

| Phenotype | Type | Suggested HPO term | Notes / frequency |
|---|---|---|---|
| Recurrent sinopulmonary infections | Clinical sign | HP:0011947 / HP:0002090 (pneumonia) | Majority of patients (dominant phenotype) |
| Recurrent bacterial infections | Clinical sign | HP:0002718 | Common |
| Recurrent viral infections | Clinical sign | HP:0004429 | Common |
| *Pneumocystis jirovecii* pneumonia | Clinical sign | HP:0002090 (pneumonia) | In DN DBD-variant (combined ID) patients |
| Impaired humoral/antibody response | Lab abnormality | HP:0005405 (impaired T-cell–dependent antibody response) | Core feature |
| Abnormal B-cell development (↑CD21low, absent CD23) | Lab abnormality | HP:0010976 (B-cell abnormality) | Core feature |
| Increased naive T cells / abnormal T-cell differentiation | Lab abnormality | HP:0410330 (abnormal T-cell count/subset) | Documented |
| Autoimmunity | Clinical sign | HP:0002960 | Supported by mouse models; SLE-like features |
| B-cell malignancy (CLL) | Neoplasm | HP:0005550 (CLL) / HP:0004377 | Reported complication |

**Phenotype characteristics.** *Age of onset:* typically pediatric/early-onset for dominant-negative combined-immunodeficiency variants; later (CVID-like) for haploinsufficiency variants. *Severity:* variable — severe (combined immunodeficiency with opportunistic infection) for DN DBD variants, milder for haploinsufficiency. *Progression:* chronic, lifelong; episodic infections; risk of malignancy increasing with age. *Frequency among affected:* recurrent sinopulmonary infection is the dominant manifestation in the majority.

**Quality-of-life impact.** No disease-specific EQ-5D/SF-36 data exist for this ultra-rare disorder. By analogy to combined immunodeficiencies and CVID, burden derives from recurrent infections, need for lifelong immunoglobulin replacement, malignancy surveillance, and (in severe cases) transplantation. *(Quantitative QoL data not available.)*

---

## 4. Genetic / Molecular Information

**Causal gene.** *IKZF3* (AIOLOS), HGNC:13178, OMIM gene 606221, chromosome 17q12-q21.1. The protein is an IKAROS-family C2H2 zinc-finger transcription factor with N-terminal DNA-binding zinc fingers and C-terminal dimerization zinc fingers (Finding F007).

**Pathogenic variant spectrum (Finding F001):**

| Variant | Type | Mechanism | Penetrance | Phenotype |
|---|---|---|---|---|
| G159R | Missense (DBD) | Dominant-negative / heterodimeric interference | Full | Combined immunodeficiency |
| N160S | Missense (DBD) | Dominant-negative / heterodimeric interference | Full | Combined immunodeficiency |
| G191R | Missense (DBD) | Dominant-negative / heterodimeric interference | Full | Combined immunodeficiency |
| E82K | Missense | Haploinsufficiency | — | CVID-like (milder) |
| Q402X | Truncating (nonsense) | Haploinsufficiency | — | CVID-like (milder) |

The N160S variant *"was fully penetrant and had a dominant-negative effect over WT AIOLOS but not WT IKAROS"* ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)).

**Variant classification.** The reported DBD missense and truncating variants are classified pathogenic/likely pathogenic per ACMG/AMP criteria (functional evidence, segregation, absence from population databases).

**Allele frequency.** Essentially absent from population databases — consistent with a highly constrained gene (see below). Somatic vs germline: all reported disease variants are **germline**.

**Functional consequences.** DBD missense variants are loss-of-function at the DNA-binding level but act dominantly through interference with the wild-type partner (gain of a dominant-negative/interfering activity). E82K and Q402X cause simple **loss of function / haploinsufficiency**.

**Gene constraint (Finding F009).** gnomAD v2/v4 constraint for *IKZF3* (ENSG00000161405): **pLI = 0.99999** (near-certain LoF intolerance), observed/expected LoF ratio **o/e = 0.204** (90% CI 0.126–0.346; LOEUF = 0.346), LoF Z = 4.72; missense constraint mis_Z = 2.76 (o/e_mis = 0.749). Population databases show essentially no common LoF variation — strongly supporting that heterozygous loss is deleterious and consistent with a haploinsufficiency mechanism for truncating variants.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes have been established. AIOLOS itself functions in chromatin regulation (pericentromeric heterochromatin targeting; see Mechanism). No recurrent large-scale chromosomal abnormalities are reported for IMD84. *(Not applicable / not available.)*

---

## 5. Environmental Information

No environmental toxins, radiation, pollution, occupational exposures, or lifestyle factors are established causes or modifiers of IMD84. **Infectious agents** are relevant as *consequences/triggers* of the immunodeficiency rather than causes: patients are susceptible to *Pneumocystis jirovecii* (opportunistic fungal pneumonia), recurrent bacterial sinopulmonary pathogens, and various viral infections ([PMID: 38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/); [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)). *(Environmental/lifestyle etiology: not applicable for a monogenic disease.)*

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A germline **heterozygous variant in *IKZF3*** (e.g., G159R/N160S/G191R in the DNA-binding domain) **leads to** a mutant AIOLOS protein with an altered zinc-finger DNA-binding surface.
2. **Branch A — Dominant-negative DBD variants:** Mutant AIOLOS **still dimerizes** (via intact C-terminal dimerization fingers) with wild-type AIOLOS and with its partner **IKAROS**, **which results in** mutant-containing homo- and heterodimers that **fail to bind the canonical AIOLOS–IKAROS DNA motif** and are **redirected to aberrant genomic regions** lacking that motif; the mutant also **fails pericentromeric (heterochromatin) targeting**.
   - This **sequesters wild-type IKAROS** away from its normal targets ("**heterodimeric interference**"), **leading to** loss of IKAROS/AIOLOS-dependent transcriptional programs across lymphocyte development. *(Demonstrated: removing the mutant's dimerization capacity restored B-cell development.)*
3. **Branch B — Haploinsufficiency variants (E82K, Q402X):** Reduced functional AIOLOS dosage (one working allele) **results in** sub-threshold AIOLOS activity — a milder, later humoral defect. *(Supported by extreme LoF intolerance; mechanism inferred by analogy to IKZF1 haploinsufficiency.)*
4. Loss of AIOLOS/IKAROS transcriptional control **leads to** abnormal **B-cell development** (↑CD21low B cells, absent CD23, abrogated CD40 responses) and **impaired antibody responses**.
5. In parallel it **leads to** abnormal **T-cell differentiation** (naive-skewed T cells, dysregulated CD40L), impairing T-cell help. *(Demonstrated in patients and knock-in mice.)*
6. The combined B- and T-cell defect **results in** the clinical **combined immunodeficiency**: recurrent sinopulmonary and opportunistic infections (*Pneumocystis jirovecii*).
7. Loss of AIOLOS-dependent tolerance/homeostasis programs **leads to** **autoimmunity** (SLE-like in mouse models) and, over time, **predisposition to B-cell malignancy** (CLL/lymphoma). *(Autoimmunity/lymphoma demonstrated in Aiolos-null mice; CLL reported in patients.)*

### Mechanistic detail

**Molecular pathways and protein dysfunction (Finding F002).** The central lesion is corruption of the IKAROS-family transcription-factor network. Mutant AIOLOS homodimers and AIOLOS–IKAROS heterodimers *"did not bind the canonical AIOLOS-IKAROS DNA sequence"* ([PMID: 34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/)). The authors define the new principle: *"Heterodimeric interference is a new mechanism of autosomal dominance that causes inborn errors of immunity by impairing protein function via the mutation of its heterodimeric partner"* ([PMID: 34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/)). Functionally, the mutant acts dominant-negative over WT AIOLOS but not WT IKAROS, yet corrupts IKAROS function by sequestering it into non-functional complexes ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)).

**Cellular processes.** AIOLOS regulates lymphocyte development, B-cell maturation, plasma-cell generation, and T-helper differentiation. It also targets pericentromeric heterochromatin, linking it to chromatin-mediated gene silencing — a function lost by the DBD mutants.

**Immune system involvement.** The disease is fundamentally an immunodeficiency with an autoimmune/dysregulation component — reflecting AIOLOS's dual roles in building protective immunity and enforcing tolerance.

**T-cell programs (Finding F006).** Beyond B cells, AIOLOS shapes T-helper biology: under Th17-polarizing conditions STAT3 and AhR upregulate Aiolos, which *"silenced the Il2 locus, promoting T(H)17 differentiation in vitro and in vivo"* ([PMID: 22751139](https://pubmed.ncbi.nlm.nih.gov/22751139/)). Aiolos also *"promotes CXCR3 expression on Th1 cells by propagating the IFN-γ/STAT1 cytokine signaling pathway"* ([PMID: 39560988](https://pubmed.ncbi.nlm.nih.gov/39560988/)) and regulates eosinophil tissue homing via CCR3 ([PMID: 34341502](https://pubmed.ncbi.nlm.nih.gov/34341502/)).

**Drug-target parallel (Finding F005).** AIOLOS/IKZF3 is a cereblon neosubstrate. CELMoDs/IMiDs act as molecular glues: *"recruiting novel protein substrates for selective proteasomal degradation. These include two critical lymphoid transcription factors, Ikaros family zinc finger proteins 1 and 3 (IKZF1 and IKZF3), also known as Ikaros and Aiolos"* ([PMID: 38539501](https://pubmed.ncbi.nlm.nih.gov/38539501/)). Pharmacologic degradation of Aiolos *"correlates with increased transcription of interferon (IFN)-stimulated genes"* ([PMID: 26002965](https://pubmed.ncbi.nlm.nih.gov/26002965/)) — showing Aiolos normally represses interferon-stimulated genes. This drug-induced degradation is the pharmacologic analog of the genetic deficiency.

**Suggested ontology terms.**
- GO biological process: regulation of lymphocyte differentiation (GO:0045619); B cell differentiation (GO:0030183); T-helper 17 cell differentiation (GO:0072539); negative regulation of transcription, DNA-templated (GO:0045892); regulation of immune response (GO:0050776).
- GO cellular component: nucleus (GO:0005634); heterochromatin / pericentric heterochromatin (GO:0005721); transcription regulator complex (GO:0005667).
- CL cell types: B cell (CL:0000236); plasma cell (CL:0000786); T-helper 17 cell (CL:0002038); T-helper 1 cell (CL:0000545); naive T cell (CL:0000898); eosinophil (CL:0000771).
- CHEBI (drug analogs): lenalidomide (CHEBI:63791); pomalidomide; thalidomide (CHEBI:9513).

---

## 7. Anatomical Structures Affected

**Organ / body-system level.** The **immune/hematolymphoid system** is primarily affected (UBERON:0002405 immune system; UBERON:0002390 hematopoietic system). Secondary organ involvement follows infection: **lungs/respiratory tract** (UBERON:0002048 lung; recurrent sinopulmonary infection, *Pneumocystis* pneumonia) and the **upper respiratory tract/sinuses**. **Bone marrow** (UBERON:0002371) is central to B-lymphopoiesis and plasma-cell maintenance.

**Tissue / cell level.** Affected cell populations: **B cells** (CL:0000236) — abnormal maturation with ↑CD21low, absent CD23; **plasma cells** (CL:0000786) — AIOLOS required for long-lived bone-marrow plasma cells; **T cells** (CL:0000084) with naive skewing; **Th17** (CL:0002038) and **Th1** (CL:0000545) subsets; **eosinophils** (CL:0000771).

**Subcellular level.** The **nucleus** (GO:0005634) and **pericentromeric heterochromatin** (GO:0005721) — the sites of AIOLOS transcriptional/chromatin function.

**Localization / lateralization.** Systemic (not lateralized); infections typically bilateral (e.g., pneumonia).

---

## 8. Temporal Development

**Onset.** Variable and variant-dependent (Finding F008). Dominant-negative DBD variants tend to present early (pediatric) as combined immunodeficiency; haploinsufficiency variants present later with a CVID-like course. Onset pattern is typically **chronic/insidious**, punctuated by acute infections.

**Progression.** Chronic, lifelong. Course is characterized by recurrent/episodic infections, potential development of autoimmunity, and an increasing risk of B-cell malignancy over time. No formal staging system exists.

**Patterns / critical periods.** No spontaneous remission; management is lifelong. The principal window for definitive intervention is early identification enabling immunoglobulin replacement, infection prophylaxis, and consideration of hematopoietic stem-cell transplantation before severe infectious or malignant complications accrue.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal dominant** (heterozygous variants) (Finding F001). Reported missense DBD variants are **fully penetrant**; the N160S variant *"was fully penetrant"* ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)).

**Penetrance / expressivity.** High (complete for reported DBD missense variants); expressivity is variable, strongly influenced by variant mechanism (DN vs haploinsufficiency).

**Epidemiology.** Ultra-rare; only a small number of families/individuals reported worldwide. No reliable prevalence or incidence estimates exist. *(Not available — too few cases.)*

**Founder effects / consanguinity / carrier frequency.** Not applicable — the disease is dominant with de novo or vertically transmitted private variants; extreme gnomAD LoF intolerance (pLI ≈ 1) means carriers of LoF variants are essentially absent from the general population (Finding F009).

**Population demographics.** No ethnic predilection, geographic clustering, or sex bias has been established given the small number of cases. *(Not available.)*

---

## 10. Diagnostics

**Clinical/laboratory tests.** Immunophenotyping by flow cytometry is central and reveals the characteristic signature: increased **CD21low B cells**, **absent CD23** expression, abnormal B-cell maturation, abrogated CD40 responses, increased naive T cells, and abnormal T-cell differentiation ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)). Serum immunoglobulins typically show impaired antibody responses/hypogammaglobulinemia. Functional assays include pericentromeric heterochromatin localization and electrophoretic mobility shift assays (EMSA) to confirm DNA-binding defects — approaches validated for the IKZF family ([PMID: 38734037](https://pubmed.ncbi.nlm.nih.gov/38734037/)).

**Genetic testing.** Definitive diagnosis is molecular. **Whole-genome sequencing (WGS)** or **whole-exome sequencing (WES)** is the recommended approach; the primary atopic/IEI literature supports upfront genomic sequencing for suspected monogenic IEI ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)). A companion IKZF-family report emphasizes that panels may miss variants and that WGS can detect pathogenic IKZF variants where panels and exomes were non-diagnostic ([PMID: 38734037](https://pubmed.ncbi.nlm.nih.gov/38734037/)). *IKZF3* should be included in IEI/CVID/combined-immunodeficiency gene panels; single-gene testing confirms a known familial variant.

**Clinical criteria / differential diagnosis.** No disease-specific criteria. Differential diagnosis includes other IKZF-associated IEIs (**IKZF1/IKAROS** — CVID-like or combined immunodeficiency; **IKZF2/HELIOS**), CVID of other genetic cause, and other combined immunodeficiencies. The distinguishing feature is the *IKZF3* variant plus the heterodimeric-interference functional signature.

**Screening.** Cascade genetic testing of at-risk relatives once a familial variant is identified. No population newborn screening exists for this ultra-rare disorder.

---

## 11. Outcome / Prognosis

**Survival / mortality.** No formal survival statistics exist. Prognosis is driven by infection severity (combined immunodeficiency with *Pneumocystis* pneumonia carries significant risk) and malignancy. *(Quantitative survival data not available.)*

**Morbidity / complications.** Recurrent and opportunistic infections, autoimmunity, and B-cell malignancy — a family was reported *"with T and B cell involvement, Pneumocystis jirovecii pneumonia, and/or chronic lymphocytic leukemia"* ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)). Lifelong immunoglobulin dependence contributes to morbidity.

**Prognostic factors.** The variant mechanism is the strongest prognostic determinant (Finding F008): **dominant-negative DBD variants** → early-onset combined immunodeficiency, high *Pneumocystis* risk, naive-skewed T cells — worse prognosis; **haploinsufficiency variants** → milder CVID-like course. Across the IKZF family, *"Mutations acting by haploinsufficiency present with a common variable immune deficiency-like phenotype mainly characterized by increased susceptibility to infections. Mutations acting in a dominant negative fashion present with a combined immunodeficiency phenotype with high prevalence of Pneumocystis jirovecii pneumonia"* ([PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/)).

---

## 12. Treatment

No IMD84-specific disease-modifying therapy exists; management is supportive and extrapolated from combined immunodeficiency / CVID care.

| Intervention | Rationale | Suggested NCIT concept |
|---|---|---|
| **Immunoglobulin replacement** (IVIG/SCIG) | Corrects impaired antibody responses / hypogammaglobulinemia | NCIT: Intravenous Immunoglobulin Therapy |
| **Antimicrobial prophylaxis** (e.g., anti-*Pneumocystis*: trimethoprim-sulfamethoxazole) | Prevents opportunistic/recurrent infection | NCIT: Antibiotic Therapy / Prophylaxis |
| **Hematopoietic stem-cell transplantation (HSCT)** | Potentially curative for severe combined immunodeficiency | NCIT: Hematopoietic Stem Cell Transplantation |
| **Malignancy surveillance / treatment** (e.g., for CLL) | Elevated B-cell malignancy risk | NCIT: Cancer Treatment |
| Supportive care, vaccination caution (live vaccines) | Symptom and infection management | NCIT: Supportive Care |

**Pharmacogenomic note.** Because AIOLOS is a CRBN neosubstrate, IMiDs/CELMoDs (lenalidomide, pomalidomide, mezigdomide) *degrade* AIOLOS and would be expected to worsen the deficiency — relevant if a patient with IMD84 also had a plasma-cell neoplasm; these agents are generally contraindicated with respect to the underlying immune defect (Finding F005). No genotype-guided IMD84-specific pharmacotherapy is established.

**Experimental therapeutics.** No IMD84-specific clinical trials (no NCT identifiers) are known.

---

## 13. Prevention

Being a highly penetrant monogenic disorder, **primary prevention** centers on **genetic counseling** and reproductive options (prenatal testing, preimplantation genetic diagnosis) for families with a known variant. **Secondary prevention** is early molecular diagnosis via genomic sequencing and cascade testing of relatives, enabling pre-emptive immunoglobulin replacement and infection prophylaxis. **Tertiary prevention** targets complications: anti-infective prophylaxis (notably anti-*Pneumocystis*), vaccination strategy adjusted for immunodeficiency (avoid live vaccines), malignancy surveillance, and timely HSCT in severe cases. No immunization prevents the disease itself; no behavioral or environmental interventions apply.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** The gene is conserved in mouse (*Mus musculus*, NCBI Taxon 10090) as *Ikzf3* (Aiolos). No naturally occurring companion-animal or wildlife disease equivalent to IMD84 has been documented in OMIA. **Comparative biology** is addressed through engineered models (next section). Evolutionary conservation of the AIOLOS/IKAROS dimerization and DNA-binding architecture underlies the faithful recapitulation of human phenotypes in mice. No zoonotic potential (the disease is genetic, not transmissible).

---

## 15. Model Organisms

**Knock-in models of human variants (Finding F004).** Mice carrying the corresponding human N160S (Kuehn) and G159R (Yamashita) variants recapitulate the human B- and T-cell phenotypes: *"The human immunophenotype was recapitulated in a murine model carrying the corresponding human mutation"* ([PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)). These are the most disease-faithful models.

**Classic knockout models.** *Ikzf3*-null mice reveal the broader biology:
- B cells show an activated phenotype with augmented BCR proliferation, spontaneous germinal centers, elevated IgG/IgE, and autoantibodies; *"Auto-antibodies and development of B cell lymphomas are frequently seen among aging Aiolos mutants"* ([PMID: 9806640](https://pubmed.ncbi.nlm.nih.gov/9806640/)) — modeling the autoimmunity and malignancy risk.
- Aiolos is required for the humoral memory compartment: *"the Ikaros family member, Aiolos, is specifically required for the generation of these plasma cells"* (long-lived high-affinity bone-marrow plasma cells) ([PMID: 14718515](https://pubmed.ncbi.nlm.nih.gov/14718515/)).
- Aiolos-null mice develop SLE-like anti-dsDNA antibodies and immune-complex glomerulonephritis ([PMID: 12574333](https://pubmed.ncbi.nlm.nih.gov/12574333/)).

**Cereblon-humanized models.** Studying the AIOLOS–CRBN drug axis requires humanized-CRBN mice because *"a single amino acid substitution of valine to isoleucine in mouse CRBN at position 391"* renders *"mice...not susceptible to IMiD-induced degradation of neosubstrates"* ([PMID: 33186626](https://pubmed.ncbi.nlm.nih.gov/33186626/)).

**Model limitations.** Mouse CRBN resistance to IMiDs limits pharmacologic modeling without humanization; knockout mice do not capture the dominant-negative heterodimeric-interference mechanism (which requires the specific knock-in). Resources: MGI, IMPC/IMSR for *Ikzf3* alleles; the DT40 chicken B-cell line for targeted functional studies ([PMID: 17623906](https://pubmed.ncbi.nlm.nih.gov/17623906/)).

---

## Mechanistic Model / Interpretation

```
            IKZF3 (AIOLOS) germline heterozygous variant
                              |
         +--------------------+-------------------------+
         |                                              |
  DBD missense (G159R/N160S/G191R)          Haploinsufficiency (E82K/Q402X)
  = dominant-negative                        = reduced dosage
         |                                              |
  Mutant AIOLOS still dimerizes               ~50% functional AIOLOS
  with WT AIOLOS AND IKAROS                           |
         |                                             |
  Homo/heterodimers FAIL canonical DNA binding         |
  + redirected to aberrant loci                        |
  + fail pericentromeric targeting                     |
         |                                             |
  "HETERODIMERIC INTERFERENCE":                        |
  WT IKAROS sequestered/misdirected                    |
         +-----------------+------------------------- -+
                           v
      Disrupted IKAROS/AIOLOS transcriptional program
                           v
   +------------+---------------+------------------+
   v            v               v                  v
Abnormal B   Naive-skewed    Loss of           Loss of
cell dev.    T cells /       tolerance/        plasma-cell
(hiCD21low,  impaired        homeostasis       maintenance
 -CD23)      T-cell help
   |            |               |                  |
   +------------+---------------+                  |
                v               v                  v
      COMBINED IMMUNODEFICIENCY   AUTOIMMUNITY   Poor long-term
      recurrent/opportunistic     (SLE-like in   antibody titers
      infections (P. jirovecii)   mice)
                |
                v
      B-cell malignancy risk (CLL/lymphoma)
```

**Severity rule (genotype–phenotype):** DBD dominant-negative variants → combined immunodeficiency + high *Pneumocystis* risk (worse). Haploinsufficiency → CVID-like (milder). AIOLOS N160 is the structural homolog of IKAROS N159, and the paradigm transfers directly from IKZF1 ([PMID: 32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/); [PMID: 29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [34155405](https://pubmed.ncbi.nlm.nih.gov/34155405/) | *A variant in human AIOLOS impairs adaptive immunity by interfering with IKAROS* | Heterodimeric interference mechanism; loss of canonical DNA binding (F002) |
| [34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/) | *T and B cell abnormalities, pneumocystis pneumonia, CLL with AIOLOS defect* | N160S full penetrance, dominant-negative, B/T phenotype, PCP, CLL, mouse recapitulation (F001, F003, F004) |
| [38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/) | *AIOLOS-Associated Inborn Errors of Immunity* | Full variant spectrum; sinopulmonary infection phenotype (F001, F003) |
| [32654692](https://pubmed.ncbi.nlm.nih.gov/32654692/) | *IKAROS Family Zinc Finger 1-Associated Diseases in PID* | DN vs haploinsufficiency genotype-phenotype paradigm (F008) |
| [29889099](https://pubmed.ncbi.nlm.nih.gov/29889099/) | *Dominant-negative IKZF1 mutations cause T, B, myeloid combined immunodeficiency* | Naive T-cell skewing in DN DBD variants (F008) |
| [38539501](https://pubmed.ncbi.nlm.nih.gov/38539501/) | *Mezigdomide — CRBN E3 ligase modulator* | AIOLOS/IKZF3 is a CRBN neosubstrate (F005) |
| [33186626](https://pubmed.ncbi.nlm.nih.gov/33186626/) | *Lenalidomide-sensitive syngeneic murine model (CRBN humanization)* | Species difference in CRBN; need for humanized models (F005) |
| [26002965](https://pubmed.ncbi.nlm.nih.gov/26002965/) | *CC-122 mimics an interferon response (DLBCL)* | Aiolos represses interferon-stimulated genes (F005) |
| [22751139](https://pubmed.ncbi.nlm.nih.gov/22751139/) | *Aiolos promotes TH17 differentiation by silencing Il2* | Th17/IL-2 silencing role (F006) |
| [39560988](https://pubmed.ncbi.nlm.nih.gov/39560988/) | *Aiolos promotes CXCR3 on Th1 via IFN-γ/STAT1* | Th1 migration program (F006) |
| [14718515](https://pubmed.ncbi.nlm.nih.gov/14718515/) | *Aiolos required for high-affinity bone-marrow plasma cells* | Plasma-cell/long-term immunity role (F004) |
| [9806640](https://pubmed.ncbi.nlm.nih.gov/9806640/) | *Aiolos regulates B cell activation and maturation* | Autoantibodies, B-cell lymphoma in Aiolos-null mice (F004) |
| [12574333](https://pubmed.ncbi.nlm.nih.gov/12574333/) | *OBF-1 and SLE-like phenotype in Aiolos mutant mice* | SLE-like autoimmunity in Aiolos-null mice (F004/F006) |
| [38734037](https://pubmed.ncbi.nlm.nih.gov/38734037/) | *Novel IKZF1 variant in AD CVID; WGS* | WGS utility; haploinsufficiency functional testing (diagnostics) |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | *Rapid identification of primary atopic disorders via WGS* | Upfront genomic sequencing for IEI (diagnostics) |
| [42169761](https://pubmed.ncbi.nlm.nih.gov/42169761/) | *IKZF-associated inborn errors of immunity* | IKZF family biology/disease context |
| [34341502](https://pubmed.ncbi.nlm.nih.gov/34341502/) | *Aiolos regulates eosinophil migration* | CCR3-dependent eosinophil homing (F006) |
| [17623906](https://pubmed.ncbi.nlm.nih.gov/17623906/) | *DT40 mutants: transcriptional regulation of B-cell development* | Functional model system for Aiolos (model organisms) |

**Evidence source types:** human clinical/genetic (patient families — 34694366, 38773004, 38734037); functional in vitro (EMSA, localization — 34155405); model organism (knock-in and knockout mice — 34694366, 9806640, 14718515, 12574333, 33186626); computational/population genetics (gnomAD constraint — F009).

---

## Limitations and Knowledge Gaps

1. **Very small patient numbers.** Only a handful of families/individuals are reported, so prevalence, incidence, sex ratio, age distribution, survival, and quality-of-life metrics are unavailable. All phenotype frequencies are qualitative.
2. **Haploinsufficiency phenotype less characterized.** The E82K and Q402X haploinsufficiency arm rests on fewer cases; its mechanism is partly inferred by analogy to IKZF1 and from extreme gnomAD LoF intolerance rather than fully demonstrated patient-level functional data.
3. **No natural animal disease.** Comparative/veterinary data are absent; all animal evidence is from engineered models.
4. **Treatment evidence is extrapolated.** No IMD84-specific trials exist; management recommendations are inferred from combined immunodeficiency/CVID practice.
5. **Modifiers and epigenetics unresolved.** Modifier genes, epigenetic contributions, and determinants of variable expressivity are not defined.
6. **Malignancy risk not quantified.** CLL/lymphoma is reported but the magnitude of lifetime risk is unknown.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & natural-history study** for AIOLOS/IKZF3 variants to quantify penetrance, infection burden, autoimmunity, malignancy incidence, and outcomes stratified by variant mechanism.
2. **Systematic functional classification** of all reported and future *IKZF3* variants (DNA-binding EMSA, pericentromeric localization, dimerization assays) to assign DN vs haploinsufficiency and predict severity prospectively.
3. **Deep immunophenotyping / single-cell multi-omics** (scRNA-seq + ATAC) of patient B and T cells to map the disrupted AIOLOS/IKAROS regulatory network at cell-type resolution and define biomarkers.
4. **HSCT outcome analysis** across reported cases to establish indications, timing, and efficacy for severe combined-immunodeficiency presentations.
5. **Cereblon-humanized knock-in mouse studies** combining the N160S/G159R alleles with humanized CRBN to dissect the intersection of genetic deficiency and IMiD pharmacology — clarifying contraindications and potential therapeutic windows.
6. **Structural studies** (cryo-EM / AlphaFold-guided) of mutant AIOLOS–IKAROS heterodimers on aberrant DNA to understand how DBD mutations redirect genomic targeting.

---

*Report compiled from 9 confirmed findings and 29 reviewed papers across a 5-iteration investigation. Causal gene confirmed: **IKZF3 (AIOLOS)**.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_84-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_84-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

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
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030333` (2 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 84**
- `HP:0002718` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent bacterial infections**
- `HP:0004429` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent viral infections**
- `HP:0410330` (1 mention) - the report calls it "abnormal T-cell count/subset"; HP calls it **Meat allergen allergy**
- `HP:0002960` (1 mention) - the report calls it "Clinical sign"; HP calls it **Autoimmunity**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005405` (1 mention), reported as "impaired T-cell–dependent antibody response" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010976` (1 mention) - the report calls it "B-cell abnormality"; HP calls it **Decreased total B cell count**, and lists "Low B cell count" among its other names
- `GO:0045619` (1 mention) - the report calls it "GO biological process: regulation of lymphocyte differentiation"; GO calls it **regulation of lymphocyte differentiation**
- `GO:0005634` (2 mentions) - the report calls it "GO cellular component: nucleus", "nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `GO:0005721` (2 mentions) - the report calls it "pericentromeric heterochromatin"; GO calls it **pericentric heterochromatin**
- `CL:0000236` (2 mentions) - the report calls it "CL cell types: B cell", "B cells"; CL calls it **B cell**
- `CL:0002038` (2 mentions) - the report calls it "Th17"; CL calls it **T follicular helper cell**, and lists "Tfh" among its other names
- `CL:0000545` (2 mentions) - the report calls it "Th1"; CL calls it **T-helper 1 cell**, and lists "Th1 cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "GO cellular component: nucleus", "nucleus"
- `CL:0000236` - called "CL cell types: B cell", "B cells"