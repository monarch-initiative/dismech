---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T23:54:27.754715'
end_time: '2026-11-05T00:29:00.558754'
duration_seconds: 2072.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SIN3A-Related Intellectual Disability Syndrome
  mondo_id: MONDO:0044699
  category: Mendelian
  causal_genes: SIN3A
  omim_id: not recorded
  synonyms: Witteveen-Kolk syndrome; WITKOS
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
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 20
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:39576496
  relevance_assessed: 21
  on_topic: 13
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 41
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 9
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - Common
    ontology_label: Global developmental delay
  - term_id: HP:0000729
    reported_labels:
    - Minority
    ontology_label: Autistic behavior
  - term_id: HP:0007018
    reported_labels:
    - Minority
    ontology_label: Attention deficit hyperactivity disorder
  - term_id: HP:0000252
    reported_labels:
    - Characteristic
    ontology_label: Microcephaly
  - term_id: HP:0004322
    reported_labels:
    - Characteristic
    ontology_label: Short stature
  - term_id: HP:0001999
    reported_labels:
    - Characteristic/recognizable
    ontology_label: Abnormal facial shape
  - term_id: HP:0011968
    reported_labels:
    - Common
    ontology_label: Feeding difficulties
  - term_id: HP:0001627
    reported_labels:
    - Not uncommon
    ontology_label: Abnormal heart morphology
  - term_id: HP:0000175
    reported_labels:
    - Rare
    ontology_label: Cleft palate
  - term_id: UBERON:0000956
    reported_labels:
    - "Primary organ/system:** Central nervous system \u2014 cerebral cortex"
    ontology_label: cerebral cortex
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0016575
    ontology_label: obsolete histone deacetylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SIN3A-Related_Intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SIN3A-Related_Intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SIN3A-Related Intellectual Disability Syndrome
- **MONDO ID:** MONDO:0044699 (if available)
- **Causal gene(s):** SIN3A
- **OMIM:** not recorded
- **Synonyms:** Witteveen-Kolk syndrome; WITKOS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SIN3A-Related Intellectual Disability Syndrome** covering all of the
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

# SIN3A-Related Intellectual Disability Syndrome (Witteveen-Kolk Syndrome, WITKOS): Comprehensive Disease Characterization

**Disease:** SIN3A-Related Intellectual Disability Syndrome / Witteveen-Kolk syndrome (WITKOS)
**Causal gene:** **SIN3A** (SIN3 transcription regulator family member A; HGNC:19353; NCBI Gene 25942; chromosome 15q24.2)
**MONDO ID:** MONDO:0044699 · **OMIM:** 613406 · **Synonyms:** Witteveen-Kolk syndrome, WITKOS, SIN3A-related intellectual disability
**Category:** Mendelian, autosomal dominant

---

## Summary

Witteveen-Kolk syndrome (WITKOS) is a rare autosomal dominant neurodevelopmental disorder caused by **haploinsufficiency of *SIN3A***, the gene encoding the eponymous scaffold protein of the SIN3-HDAC transcriptional corepressor complex on chromosome **15q24.2**. The disease was defined by Witteveen and colleagues in 2016, who identified dominant heterozygous loss-of-function mutations in *SIN3A* in individuals with mild intellectual disability (ID) and autism spectrum disorder (ASD) who also shared facial dysmorphism, microcephaly, and short stature. Because the same phenotype arises from atypical 15q24 microdeletions that span *SIN3A*, the gene is recognized as the critical driver of that contiguous-gene microdeletion syndrome ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)).

Mechanistically, SIN3A is a ~2 MDa corepressor hub that uses four paired-amphipathic-helix (PAH1–4) domains to dock sequence-specific transcription factors — including the neuronal factor Myt1L and the DNA demethylase TET1 — and link them to the histone deacetylase activity of HDAC1/2. Reducing SIN3A dosage by half degrades this chromatin-repression machinery. In the developing mouse brain, Sin3a knockdown reduces cortical neurogenesis, alters neuronal identity, and produces aberrant corticocortical projections, providing a direct developmental explanation for the human phenotype. Complete loss of Sin3a is embryonic lethal, confirming the gene is essential and consistent with a strict haploinsufficiency (loss-of-function) disease mechanism. Patient missense variants (e.g., A126V, K155E) have been shown biophysically to destabilize the PAH1 αα-hub domain, confirming that even non-truncating variants act by loss of function.

Clinically, WITKOS is mild and multisystem but variable. In the largest cohort (28 patients), cognitive impairment ranged from absent (25%) to mild (50%), moderate (22%), or severe (6%); hypotonia (43%) and seizures (14%) were common, and the phenotype has since expanded to include hypogonadotropic hypogonadism, cardiac defects, gastroesophageal reflux/motility disorder, cleft palate, movement disorders (dystonia, ataxia), and, in one family, ectodermal dysplasia with progeroid features and early-onset diabetes. The disorder is ultra-rare (a few cases per million; fewer than ~100 reported), mostly de novo, diagnosed by trio exome/genome sequencing or chromosomal microarray, and managed supportively through a multidisciplinary team. There is no disease-modifying or gene-targeted therapy.

---

## Key Findings

### Finding 1 — SIN3A haploinsufficiency causes Witteveen-Kolk syndrome

Witteveen et al. (2016) established the disease by identifying **dominant heterozygous loss-of-function mutations in *SIN3A*** (chromosome 15q24.2) in individuals with mild ID and ASD who shared a recognizable constellation of facial dysmorphism, microcephaly, and short stature. Critically, this phenotype is "highly related to that of individuals with atypical 15q24 microdeletions," establishing SIN3A as the critical gene in the 15q24 microdeletion region (OMIM 613406).

> "we identified dominant mutations in the gene encoding the transcriptional repressor and MeCP2 interactor switch-insensitive 3 family member A (SIN3A; chromosome 15q24.2) in individuals who, in addition to mild intellectual disability and ASD, share striking features, including facial dysmorphisms, microcephaly and short stature" — [PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)

> "This phenotype is highly related to that of individuals with atypical 15q24 microdeletions, linking SIN3A to this microdeletion syndrome" — [PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)

This dual origin — single-gene point mutations and whole-gene deletions producing the same disorder — is the clearest genetic signature of a haploinsufficiency mechanism.

### Finding 2 — Core clinical phenotype: mild ID, distinctive facies, growth/feeding difficulties

Balasubramanian et al. (2021) comprehensively characterized **28 patients** (17 male / 11 female; mean age 8.2 years). Among the 16 patients aged ≥8 years, cognitive severity broke down as 50% mild ID, 22% moderate ID, 6% severe ID, and 25% with **no cognitive impairment** — underscoring both the overall mildness and the marked variability of the syndrome. Other neurological features were common: hypotonia in 12/28 (43%) and seizures in 4/28 (14%); ASD and ADHD were each present in a minority of patients. The molecular spectrum comprised 24 truncating variants, 3 missense variants, and one large in-frame gain (exons 10–12); 27 of 28 were novel, indicating that nearly all variants are private.

> "Out of 16 patients ≥ 8 years old assessed, eight (50%) had mild intellectual disability (ID), four had moderate ID (22%), and one had severe ID (6%). Four (25%) did not have any cognitive impairment." — [PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)

> "Other neurological symptoms such as seizures (4/28) and hypotonia (12/28) were common." — [PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)

### Finding 3 — Mechanism: SIN3A is a corepressor scaffold regulating cortical neurogenesis

SIN3A is the eponymous scaffold of the **SIN3-HDAC corepressor complex** (with HDAC1/2, RBBP4/7, SAP30, SDS3), which deacetylates histones to repress transcription ([PMID: 33130996](https://pubmed.ncbi.nlm.nih.gov/33130996/)). SIN3 is an essential gene in metazoans; its loss impairs cell proliferation, and in *Drosophila* it downregulates the cell-cycle gene *String/CDC25* ([PMID: 19825413](https://pubmed.ncbi.nlm.nih.gov/19825413/)). Most directly relevant to the human disease, in vivo knockdown of Sin3a in the developing mouse brain reduced cortical neurogenesis, altered neuronal identity, and produced aberrant corticocortical projections ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)).

> "in vivo functional knockdown of Sin3a led to reduced cortical neurogenesis, altered neuronal identity and aberrant corticocortical projections in the developing mouse brain" — [PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)

> "The transcriptional corepressor SIN3 is an essential gene in metazoans. In cell culture experiments, loss of SIN3 leads to defects in cell proliferation." — [PMID: 19825413](https://pubmed.ncbi.nlm.nih.gov/19825413/)

**Suggested ontology terms:** GO:0006355 (regulation of DNA-templated transcription), GO:0016575 (histone deacetylation), GO:0021895 (cerebral cortex neuron differentiation), GO:0021987 (cerebral cortex development); CL:0000540 (neuron), CL:0000047 (neural progenitor cell), CL:0000679 (glutamatergic neuron).

### Finding 4 — Sin3a is essential for genome integrity and viability; constitutive knockout is embryonic lethal

McDonel et al. (2012) showed that **Sin3a-null mouse embryos die peri-implantation**: they suffer unresolved DNA damage and acute p53-independent apoptosis specifically in the E3.5–4.5 epiblast. Sin3a-deleted ES cells mount a DNA damage response with double-strand breaks, arrest at G2, and undergo apoptosis; Myc and E2F targets are downregulated in Sin3a-null inner cell masses. This confirms that SIN3A is an essential, dosage-sensitive gene — the biological basis for why only heterozygous loss (haploinsufficiency), not biallelic loss, is compatible with human life.

> "embryos lacking Sin3a suffer unresolved DNA damage and acute p53-independent apoptosis specifically in the E3.5-4.5 epiblast" — [PMID: 22206758](https://pubmed.ncbi.nlm.nih.gov/22206758/)

> "The Sin3a/HDAC co-repressor complex is a critical regulator of transcription networks that govern cell cycle control and apoptosis throughout development." — [PMID: 22206758](https://pubmed.ncbi.nlm.nih.gov/22206758/)

### Finding 5 — Expanding phenotype: hypogonadotropic hypogonadism / pubertal delay

Correa Brito et al. (2024) reported a novel SIN3A loss-of-function variant causative for **hypogonadotropic hypogonadism (HH)** in a WITKOS patient, extending the phenotype into the neuroendocrine/reproductive axis. HH overlaps with WITKOS (OMIM 613406) and with 15q24 microdeletions, paralleling Kallmann-type presentations (pubertal delay with or without anosmia/hyposmia).

> "hypogonadotropic hypogonadism has been suggested to overlap with Witteveen-Kolk syndrome (WITKOS, OMIM #613406) associated with 15q24 microdeletions" — [PMID: 38528912](https://pubmed.ncbi.nlm.nih.gov/38528912/)

**Suggested HPO terms:** HP:0000044 (hypogonadotropic hypogonadism), HP:0000823 (delayed puberty).

### Finding 6 — Molecular architecture: four PAH domains serve as a transcription-factor docking hub

SIN3A sits at the center of the ~2 MDa Sin3L/Rpd3L HDAC complex, mediating simultaneous protein–protein interactions via four **paired-amphipathic-helix (PAH1–4) domains**, each a four-helix bundle with a hydrophobic cleft binding a single-helix Sin3-interaction domain (SID) with high affinity ([PMID: 30279502](https://pubmed.ncbi.nlm.nih.gov/30279502/), [PMID: 21676866](https://pubmed.ncbi.nlm.nih.gov/21676866/)). PAH1 recruits the neuronal transcription factor **Myt1L** (neuronal differentiation/identity maintenance; [PMID: 32391601](https://pubmed.ncbi.nlm.nih.gov/32391601/)) and the DNA demethylase **TET1** ([PMID: 30279502](https://pubmed.ncbi.nlm.nih.gov/30279502/)); PAH2 binds Mad1/Mxd1 and HBP1; PAH3 binds SAP30 ([PMID: 21676866](https://pubmed.ncbi.nlm.nih.gov/21676866/)). SIN3A thereby couples sequence-specific DNA-binding factors to HDAC1/2 enzymatic activity.

> "The Sin3A protein sits at the centre of the complex, mediating multiple simultaneous protein-protein interactions via its four paired-amphipathic helix (PAH) domains (PAH1-4)." — [PMID: 30279502](https://pubmed.ncbi.nlm.nih.gov/30279502/)

> "Myt1L, through a highly conserved segment shared with its paralogs, interacts directly and specifically with the Sin3 PAH1 domain" — [PMID: 32391601](https://pubmed.ncbi.nlm.nih.gov/32391601/)

The recruitment of a neuronal identity transcription factor (Myt1L) specifically by PAH1 provides a mechanistic bridge between SIN3A dosage and neurodevelopmental consequences.

### Finding 7 — Epidemiology: ultra-rare, autosomal dominant, mostly de novo loss-of-function

Tang et al. (2025) state WITKOS incidence is extremely low — **only a few cases per million** population reported globally, with most presenting in childhood/adolescence. The disorder is autosomal dominant, caused by heterozygous loss-of-function SIN3A variants or 15q24.1–q24.2 microdeletions encompassing SIN3A. Fewer than ~100 patients have been reported in the literature (Witteveen 2016; Balasubramanian 2021 28-patient cohort). No formal Orphanet prevalence estimate exists.

> "Its incidence rate is extremely low. According to the current limited global data statistics, only a few cases occur per million population." — [PMID: 40336075](https://pubmed.ncbi.nlm.nih.gov/40336075/)

> "WITKOS is a rare neurodevelopmental disorder caused by heterozygous loss-of-function variants in the 15q24.1 - q24.2 region, includeing switch-insensitive 3 transcription regulator family member A (SIN3 A)." — [PMID: 40336075](https://pubmed.ncbi.nlm.nih.gov/40336075/)

### Finding 8 — WITKOS is a multisystem disorder beyond core neurodevelopmental features

Case reports have broadened the spectrum well beyond ID/facies/microcephaly/short stature:
- **Cardiac defects** with gastroesophageal reflux and esophageal motility disorder (Uctepe et al. 2024, [PMID: 38841330](https://pubmed.ncbi.nlm.nih.gov/38841330/));
- **Cleft palate** (Boynuyogun et al., [PMID: 39828923](https://pubmed.ncbi.nlm.nih.gov/39828923/));
- Progressive generalized **dystonia and cerebellar ataxia** (Mustafa et al. 2025, [PMID: 39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/); variant c.1051C>T p.Pro351Ser);
- A familial form with **ectodermal dysplasia, progeroid appearance, and early-onset diabetes mellitus** (Chan et al. 2025, [PMID: 40586236](https://pubmed.ncbi.nlm.nih.gov/40586236/)).

> "Our findings showed that cardiac defects are not uncommon findings in WITKOS. Physicians should also be aware of reflux disease and motility disorder in patients with feeding difficulty" — [PMID: 38841330](https://pubmed.ncbi.nlm.nih.gov/38841330/)

> "a chronic, progressively worsening symmetric cerebellar ataxia, along with generalized dystonia. Notably, dystonia has not been previously associated with this syndrome." — [PMID: 39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/)

### Finding 9 — Management is supportive/multidisciplinary; first personalized behavioral treatment reported

There is **no disease-modifying or gene-targeted therapy** for WITKOS; management is supportive and multidisciplinary (geneticist, pediatrician, neurologist), addressing developmental delay, feeding/growth, seizures, cardiac and GI issues, and behavior (Balasubramanian 2021). Janssen et al. (2026) reported the first documented treatment of behavioral problems in WITKOS — a personalized 12-session psychological intervention in a 27-year-old woman that reduced anxiety, fatigue, and cognitive overload with positive short-term functional gains but limited maintenance at 3-month follow-up.

> "we present a case study of the first documented treatment of behavioral problems in WITKOS" — [PMID: 41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/)

> "Involvement of a multidisciplinary team including a geneticist, paediatrician and neurologist should be considered in managing these patients." — [PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)

### Finding 10 — Missense variants destabilize the SIN3A PAH1 αα-hub, confirming loss-of-function

Due et al. (2026) performed structural/thermodynamic studies of the Sin3A **PAH1 αα-hub domain** and two WITKOS patient missense variants (**A126V and K155E**), demonstrating stability and interaction defects. This provides molecular-level confirmation that pathogenic SIN3A missense variants act by destabilizing PAH domains and disrupting recruitment of interacting transcription factors — a loss-of-function mechanism consistent with haploinsufficiency.

> "we relate αα-hub stability to function by structural and thermodynamic studies of the Sin3A-paired amphipathic helix 1 (PAH1) wt hub domain and two predicted loss-of-function variants (A126V and K155E) found in patients with the neurodevelopmental Witteveen-Kolk syndrome" — [PMID: 41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/)

### Finding 11 — The SIN3/HDAC corepressor is conserved from yeast to humans; multiple model organisms exist

The SIN3-RPD3 histone deacetylase corepressor is conserved from *Saccharomyces cerevisiae* (Sin3/Rpd3/Ume6; [PMID: 25957495](https://pubmed.ncbi.nlm.nih.gov/25957495/)) through *Drosophila* (SIN3 essential for proliferation and wing development via String/CDC25; [PMID: 19825413](https://pubmed.ncbi.nlm.nih.gov/19825413/)) to mouse (Sin3a essential, embryonic-lethal knockout; [PMID: 22206758](https://pubmed.ncbi.nlm.nih.gov/22206758/)) and human SIN3A.

> "Ume6 interacts with the upstream repressor site 1 (URS1) and represses transcription by recruiting both the conserved histone deacetylase Rpd3 (through the co-repressor Sin3) and the chromatin-remodeling factor Isw2." — [PMID: 25957495](https://pubmed.ncbi.nlm.nih.gov/25957495/)

**Orthologs:** *S. cerevisiae* SIN3 (NCBI Gene YOL004W); *Drosophila* Sin3A; *Mus musculus* Sin3a (NCBI Gene 20466); *Homo sapiens* SIN3A (NCBI Gene 25942; HGNC:19353). No naturally occurring companion-animal disease is catalogued in OMIA for SIN3A.

### Finding 12 — Diagnosis relies on molecular genetics; SIN3A is LOF-constrained with an emerging chromatinopathy episignature

WITKOS has **no pathognomonic biochemical biomarker**; diagnosis requires detecting a heterozygous pathogenic SIN3A variant (trio WES/WGS — most variants are private/novel, 27/28 novel in Balasubramanian 2021) or a 15q24.1–q24.2 microdeletion by chromosomal microarray (e.g., a de novo 1.6 Mb deletion, [PMID: 38841330](https://pubmed.ncbi.nlm.nih.gov/38841330/)). SIN3A is strongly constrained against loss of function in gnomAD. As a chromatin/HDAC-complex ("chromatinopathy") gene, SIN3A is a candidate for DNA-methylation **episignature**-based variant classification increasingly used for these disorders ([PMID: 41957673](https://pubmed.ncbi.nlm.nih.gov/41957673/), [PMID: 41952182](https://pubmed.ncbi.nlm.nih.gov/41952182/)).

> "We report 27 novel variants and one previously reported variant." — [PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)

> "Affymetrix CytoScan 750K microarray showed a de novo 1.6-Mb deletion at 15q24.1q24.2" — [PMID: 38841330](https://pubmed.ncbi.nlm.nih.gov/38841330/)

---

## Full Section-by-Section Report

### 1. Disease Information

WITKOS is a rare autosomal dominant neurodevelopmental disorder caused by haploinsufficiency of **SIN3A**. Core features are mild intellectual disability, developmental delay, distinctive craniofacial dysmorphism, microcephaly, and short stature, with variable multisystem involvement.

**Key identifiers:** MONDO:0044699 · OMIM 613406 · Gene: SIN3A (HGNC:19353; NCBI Gene 25942; Ensembl ENSG00000169375; UniProt Q96ST3) · Chromosome 15q24.2. Orphanet lists the SIN3A-related intellectual disability/Witteveen-Kolk entity but without a formal prevalence estimate. No specific ICD-10/ICD-11 code is dedicated to WITKOS; it maps to generic categories for intellectual disability/congenital malformation syndromes.

**Synonyms:** Witteveen-Kolk syndrome, WITKOS, SIN3A-related intellectual disability syndrome, SIN3A haploinsufficiency.

**Information source:** The knowledge base is derived primarily from aggregated disease-level resources (OMIM, published case series, and cohort studies) rather than individual EHR records. The largest evidence source is a 28-patient international cohort ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)) plus the defining discovery paper ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)) and numerous single-case reports.

### 2. Etiology

**Primary cause:** Genetic — heterozygous loss-of-function of SIN3A, by (a) intragenic point/indel variants (nonsense, frameshift, splice-site, and destabilizing missense) or (b) 15q24.1–q24.2 microdeletions encompassing SIN3A. There is no infectious, environmental, or metabolic cause.

**Genetic risk factors:** The only established causal factor is the SIN3A variant itself. Most cases are de novo; there is no known susceptibility locus or polygenic contribution. Modifier genes are not defined, though a contiguous-gene deletion (removing neighboring 15q24 genes) may modify expressivity.

**Environmental risk / protective factors:** None identified. There are no documented dietary, lifestyle, occupational, or toxic exposures that cause, raise, or lower the risk; because the disorder is Mendelian and usually de novo, environmental contributions are not expected. **Gene-environment interactions:** None documented.

### 3. Phenotypes

| Phenotype | Type | Frequency | HPO term |
|---|---|---|---|
| Intellectual disability (mild predominant) | Cognitive/behavioral | ~75% impaired (50% mild, 22% mod, 6% severe); 25% unaffected | HP:0001249 / HP:0001256 |
| Global developmental delay | Cognitive | Common | HP:0001263 |
| Autism spectrum disorder | Behavioral | Minority | HP:0000729 |
| ADHD | Behavioral | Minority | HP:0007018 |
| Muscular hypotonia | Clinical sign | 12/28 (43%) | HP:0001252 |
| Seizures | Clinical sign | 4/28 (14%) | HP:0001250 |
| Microcephaly | Physical | Characteristic | HP:0000252 |
| Short stature | Physical | Characteristic | HP:0004322 |
| Facial dysmorphism | Physical | Characteristic/recognizable | HP:0001999 |
| Feeding difficulties / growth failure | Clinical | Common | HP:0011968 |
| Hypogonadotropic hypogonadism / delayed puberty | Endocrine | Reported | HP:0000044 / HP:0000823 |
| Congenital heart defects | Clinical | "Not uncommon" | HP:0001627 |
| GERD / esophageal motility disorder | Clinical | Reported | HP:0002020 |
| Cleft palate | Physical | Rare | HP:0000175 |
| Dystonia / cerebellar ataxia | Neurological | Rare (expanding) | HP:0001332 / HP:0001251 |
| Ectodermal dysplasia / progeroid / early diabetes | Multisystem | Single family | HP:0000968 / HP:0000006 |

**Characteristics:** Onset is congenital/neonatal to early childhood (developmental features). Severity is predominantly mild but variable (mild→severe ID; 25% cognitively normal). Most features are stable rather than progressive, though a reported movement disorder was progressive. **Quality-of-life impact** is driven by cognitive/behavioral impairment, feeding/growth issues, and comorbidities requiring lifelong support; one documented behavioral intervention produced short-term gains ([PMID: 41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/)).

### 4. Genetic / Molecular Information

**Causal gene:** SIN3A (OMIM *607776; HGNC:19353; NCBI Gene 25942). **Disease OMIM:** 613406.

**Pathogenic variants:** Predominantly truncating (nonsense, frameshift, splice-site) consistent with loss of function; a minority are missense that destabilize PAH domains, plus whole-gene 15q24 deletions. In the 28-patient cohort: 24 truncating, 3 missense, 1 large in-frame gain; 27/28 novel/private ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)). Specific examples: c.1051C>T (p.Pro351Ser) with dystonia/ataxia ([PMID: 39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/)); p.A126V and p.K155E destabilizing PAH1 ([PMID: 41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/)).

**Classification & allele frequency:** Variants are classified pathogenic/likely pathogenic per ACMG; they are private and absent from population databases. SIN3A is strongly LOF-constrained in gnomAD (high pLI), supporting haploinsufficiency intolerance. **Origin:** germline, usually de novo. **Functional consequence:** loss of function / haploinsufficiency; missense variants act via protein destabilization (also loss of function). No gain-of-function or dominant-negative mechanism is established.

**Modifier genes:** Not formally defined; deletion size in 15q24 CNVs may modulate severity. **Epigenetic information:** As a chromatinopathy gene, SIN3A disruption is expected to alter genome-wide histone acetylation/DNA methylation; a specific DNA-methylation episignature is an active area of development ([PMID: 41957673](https://pubmed.ncbi.nlm.nih.gov/41957673/)). **Chromosomal abnormalities:** 15q24.1–q24.2 microdeletions (e.g., de novo 1.6 Mb; [PMID: 38841330](https://pubmed.ncbi.nlm.nih.gov/38841330/)); the region's segmental-duplication architecture mediates recurrent rearrangements ([PMID: 22180641](https://pubmed.ncbi.nlm.nih.gov/22180641/), [PMID: 19557438](https://pubmed.ncbi.nlm.nih.gov/19557438/)).

### 5. Environmental Information

No environmental, lifestyle, or infectious factors contribute to WITKOS. It is a monogenic disorder; **not applicable** across toxins, radiation, occupational exposure, diet, smoking/alcohol, and pathogens.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous loss-of-function lesion in SIN3A** (truncating variant, destabilizing missense, or 15q24 microdeletion) **reduces functional SIN3A protein to ~50%** (haploinsufficiency). *Demonstrated genetically.*
2. Reduced SIN3A **results in a deficit of the scaffold** at the center of the ~2 MDa SIN3-HDAC corepressor complex, because SIN3A docks transcription factors and HDAC1/2 via its four PAH domains. *Demonstrated biochemically/structurally (PMID 30279502, 21676866).*
3. For missense variants, the lesion specifically **destabilizes the PAH1 αα-hub, which leads to impaired binding** of SID-containing partners (e.g., Myt1L, TET1). *Demonstrated thermodynamically (PMID 41759735).*
4. Loss of scaffold **results in failure to recruit HDAC1/2 to target promoters**, leading to inappropriate histone hyperacetylation and **derepression/dysregulation of SIN3-controlled gene networks** (cell-cycle, Myc/E2F targets). *Inferred from complex biology + Sin3a-null ICM data (PMID 22206758).*
5. In neural progenitors, dysregulation **impairs the balance of proliferation vs differentiation**, which in the developing cortex **results in reduced cortical neurogenesis, altered neuronal identity, and aberrant corticocortical projections**. *Demonstrated in mouse knockdown (PMID 27399968).*
   - **Branch A (brain):** altered cortical wiring **leads to** intellectual disability, ASD, microcephaly, seizures, hypotonia.
   - **Branch B (growth/endocrine):** dysregulated developmental programs **lead to** short stature and, via hypothalamic-pituitary effects, hypogonadotropic hypogonadism (PMID 38528912). *Inferred.*
   - **Branch C (other systems):** disrupted transcriptional programs in cardiac, craniofacial, GI, and ectodermal tissues **contribute to** heart defects, cleft palate, reflux/motility disorder, and ectodermal/progeroid features (PMID 38841330, 39828923, 40586236). *Inferred from case reports.*

**Molecular pathways:** Chromatin-mediated transcriptional repression (SIN3-HDAC/Rpd3L); downstream Myc and E2F target networks; Myt1L/TET1-dependent neuronal gene regulation. **Cellular processes:** cell-cycle control, neural progenitor proliferation/differentiation, apoptosis, DNA-damage response (GO:0006974). **Protein dysfunction:** loss of scaffold function via truncation or PAH-domain destabilization. **Metabolic/immune/biochemical:** no specific enzyme deficiency, immune involvement, or metabolic defect is characteristic. **Epigenetic:** global histone-acetylation/DNA-methylation dysregulation (chromatinopathy).

**Suggested ontology terms:** GO:0016575 (histone deacetylation), GO:0000122 (negative regulation of transcription by RNA Pol II), GO:0021987 (cerebral cortex development), GO:0007399 (nervous system development); CL:0000540 (neuron), CL:0000047 (neural progenitor cell); GO:0005634 (nucleus).

### 7. Anatomical Structures Affected

- **Primary organ/system:** Central nervous system — cerebral cortex (UBERON:0000956), brain (UBERON:0000955); nervous system (UBERON:0001016). Neurodevelopmental impact is the defining feature.
- **Secondary involvement:** Craniofacial skeleton (dysmorphism, cleft palate — UBERON:0001716 secondary palate); heart (UBERON:0000948); gastrointestinal/esophagus (UBERON:0001043); endocrine axis (hypothalamic-pituitary-gonadal; UBERON:0000007 pituitary); skin/ectodermal derivatives (UBERON:0000014) in the familial progeroid form; musculoskeletal (short stature, hypotonia).
- **Tissue/cell level:** Nervous tissue; cortical neurons and neural progenitors (CL:0000540, CL:0000047). **Subcellular:** nucleus (GO:0005634) — SIN3A is a nuclear corepressor.
- **Lateralization:** Bilateral/symmetric (microcephaly, cortical involvement, symmetric movement features).

### 8. Temporal Development

- **Onset:** Congenital/neonatal to early childhood; most present in childhood or adolescence (PMID 40336075). Pattern is chronic/developmental rather than acute.
- **Progression:** Generally stable, non-progressive developmental disorder; cognitive and physical features are lifelong. Exceptions include a progressive movement disorder (dystonia/ataxia) in one report ([PMID: 39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/)).
- **Duration:** Chronic/lifelong. **Remission:** None (not a remitting condition). **Critical periods:** Cortical neurogenesis in fetal development is the mechanistically critical window; there is no established postnatal intervention window.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare — a few cases per million population; <~100 reported patients; no formal Orphanet prevalence/incidence estimate ([PMID: 40336075](https://pubmed.ncbi.nlm.nih.gov/40336075/)).
- **Inheritance:** Autosomal dominant; mostly de novo heterozygous LOF (or 15q24 CNV). **Penetrance:** Appears high but expressivity is highly variable (25% of cohort members ≥8 y had no cognitive impairment). **Expressivity:** Variable, including within families. **Anticipation:** Not applicable (not a repeat-expansion disorder). **Germline mosaicism:** Possible in principle (not specifically documented). **Founder effects/consanguinity:** None (variants are private, de novo). **Carrier frequency:** Not applicable to a dominant de novo disorder.
- **Demographics:** No ethnic predilection, geographic clustering, or strong sex bias established (cohort 17M/11F). Age distribution skews pediatric due to recent recognition.

### 10. Diagnostics

- **No biochemical biomarker** exists; diagnosis is molecular.
- **Genetic testing (primary):** Trio whole-exome (WES) or whole-genome sequencing (WGS) detects intragenic SIN3A variants (most are private/novel). **Chromosomal microarray (CMA)** detects 15q24.1–q24.2 microdeletions. Gene panels for ID/ASD that include SIN3A are also used. Single-gene testing is low-yield given phenotype nonspecificity; karyotype is insufficient for microdeletions. Mitochondrial and repeat-expansion testing are not indicated.
- **Emerging:** DNA-methylation **episignature** classification (EpiSign) for chromatinopathies may aid reclassification of SIN3A VUS ([PMID: 41957673](https://pubmed.ncbi.nlm.nih.gov/41957673/), [PMID: 41952182](https://pubmed.ncbi.nlm.nih.gov/41952182/)).
- **Imaging:** Brain MRI may show nonspecific findings; used to evaluate microcephaly/seizures. **Clinical criteria:** No formal diagnostic criteria; diagnosis rests on a compatible phenotype plus a pathogenic SIN3A variant/deletion. **Differential diagnosis:** 15q24 microdeletion syndrome (same spectrum), other chromatinopathies/ID syndromes (ANKRD11/KBG, SETD5, KMT2A, CHD3/CHD8, ADNP), and other causes of mild syndromic ID with microcephaly and short stature. **Screening:** Not amenable to population/newborn screening; cascade testing is generally unnecessary given de novo origin, but parental testing informs recurrence risk.

### 11. Outcome / Prognosis

- **Survival/mortality:** No evidence of reduced life expectancy or disease-specific mortality; WITKOS is not life-limiting in itself. The disorder is compatible with adult life (behavioral treatment reported in a 27-year-old; [PMID: 41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/)).
- **Morbidity/function:** Driven by (usually mild) intellectual disability, behavioral issues, feeding/growth difficulties, and variable multisystem complications. Functional outcomes range widely given variable expressivity.
- **Complications:** Seizures, cardiac defects, GERD/motility disorder, cleft palate, movement disorder, endocrine (hypogonadism, early diabetes in one family). **Recovery potential:** Developmental features are stable; supportive therapy improves function.
- **Prognostic factors:** Severity of ID and presence of multisystem complications; no validated molecular prognostic biomarker, though deletion vs point-variant and variant location/type may influence phenotype.

### 12. Treatment

- **No disease-modifying or gene-targeted therapy** exists. Management is **supportive and multidisciplinary** (NCIT: Supportive Care; Multidisciplinary Care) — geneticist, pediatrician, neurologist ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)).
- **Symptom-directed:** Antiseizure medication for epilepsy; nutritional support/anti-reflux management for feeding difficulties and GERD; cardiology management and surgical repair for cardiac defects; surgical cleft palate repair after neurodevelopmental maturation ([PMID: 39828923](https://pubmed.ncbi.nlm.nih.gov/39828923/)); endocrine therapy for hypogonadism; movement-disorder management for dystonia/ataxia.
- **Rehabilitative/behavioral:** Physical, occupational, and speech therapy; special education; a first personalized 12-session psychological intervention reduced anxiety/fatigue/cognitive overload with short-term gains ([PMID: 41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/)).
- **Pharmacogenomics, gene/cell/RNA therapy, targeted/immunotherapy, experimental trials:** None specific to WITKOS at this time. No NCT-registered disease-specific trials identified.

### 13. Prevention

- **Primary prevention:** Not applicable (de novo genetic origin). **Secondary prevention:** Early developmental assessment and intervention improve functional outcomes; screening for known complications (cardiac, GI/reflux, cleft palate, endocrine) is recommended once diagnosed (PMID 38841330, 39828923).
- **Genetic counseling:** Essential — recurrence risk for parents of a de novo case is low (germline mosaicism caveat); an affected individual has a 50% transmission risk. Prenatal/preimplantation genetic testing is feasible for a known familial variant. **Public health/immunization/environmental:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** SIN3A/Sin3 is deeply conserved. *Homo sapiens* SIN3A (NCBI Gene 25942); *Mus musculus* Sin3a (NCBI Gene 20466); *Drosophila melanogaster* Sin3A; *Saccharomyces cerevisiae* SIN3 (YOL004W). Function conserved from yeast through metazoans ([PMID: 25957495](https://pubmed.ncbi.nlm.nih.gov/25957495/), [PMID: 19825413](https://pubmed.ncbi.nlm.nih.gov/19825413/), [PMID: 22206758](https://pubmed.ncbi.nlm.nih.gov/22206758/)).
- **Natural disease:** No naturally occurring companion-animal or wildlife SIN3A disease is catalogued in OMIA. **Comparative biology:** The corepressor mechanism and its essentiality are evolutionarily conserved, supporting cross-species mechanistic inference. **Zoonotic potential:** Not applicable.

### 15. Model Organisms

| Model | Type | Key finding | Reference |
|---|---|---|---|
| Mouse (Sin3a knockout) | Mammalian, constitutive KO | Embryonic lethal (peri-implantation); DNA damage + p53-independent apoptosis in epiblast | [PMID: 22206758](https://pubmed.ncbi.nlm.nih.gov/22206758/) |
| Mouse (in vivo Sin3a knockdown, developing brain) | Mammalian, focal knockdown | Reduced cortical neurogenesis, altered neuronal identity, aberrant corticocortical projections — recapitulates core human neurodevelopmental mechanism | [PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/) |
| *Drosophila* SIN3 | Invertebrate | Essential gene; regulates proliferation/wing development via String/CDC25 | [PMID: 19825413](https://pubmed.ncbi.nlm.nih.gov/19825413/) |
| *S. cerevisiae* Sin3/Rpd3/Ume6 | Yeast | Conserved corepressor mechanism; transcriptional repression | [PMID: 25957495](https://pubmed.ncbi.nlm.nih.gov/25957495/) |

**Phenotype recapitulation:** The mouse brain knockdown is the most disease-relevant model, directly reproducing the neurogenesis defect proposed to underlie human ID. **Limitations:** Constitutive KO is embryonic lethal, so the human haploinsufficiency state requires heterozygous/conditional models; no published heterozygous mouse phenotype fully modeling WITKOS is in the knowledge base. Invertebrate/yeast models illuminate conserved molecular function but not the syndromic phenotype. **Resources:** MGI (Sin3a), FlyBase (Sin3A), SGD (SIN3).

---

## Mechanistic Model / Interpretation

```
 SIN3A heterozygous LOF            (truncating / destabilizing missense / 15q24 deletion)
        │  reduces functional SIN3A protein to ~50% (haploinsufficiency)
        ▼
 Deficient SIN3-HDAC corepressor scaffold
   (4 PAH domains can no longer dock TFs + HDAC1/2 at full capacity)
   • missense A126V/K155E → PAH1 αα-hub destabilized → lost Myt1L/TET1 binding (PMID 41759735, 32391601, 30279502)
        │  leads to
        ▼
 Failure to recruit HDAC1/2 → histone hyperacetylation → derepression/dysregulation
   of SIN3-controlled gene networks (Myc, E2F, cell-cycle)  (PMID 22206758)
        │  results in
        ▼
 Imbalanced neural progenitor proliferation vs differentiation
        │  in developing cortex → reduced neurogenesis, altered identity,
        │  aberrant corticocortical projections (PMID 27399968)
        ▼
 ┌────────────── BRANCH A (brain) ──────────────┐  ┌─ BRANCH B (growth/endocrine) ─┐  ┌─ BRANCH C (other) ─┐
 │ ID, ASD, microcephaly, seizures, hypotonia   │  │ short stature; HH / pubertal   │  │ heart defects,     │
 │                                              │  │ delay (PMID 38528912)          │  │ cleft palate, GERD,│
 │                                              │  │                                │  │ ectodermal/progeroid│
 └──────────────────────────────────────────────┘  └────────────────────────────────┘  └────────────────────┘
```

**Upstream vs downstream:** The mutation and corepressor-scaffold deficit are upstream (demonstrated genetically/structurally); gene-network dysregulation is intermediate (demonstrated in cells/embryos); the cortical neurogenesis defect is the proximal cause of the neurodevelopmental phenotype (demonstrated in mouse); multisystem branches are largely inferred from case reports. The essentiality of SIN3A (embryonic-lethal null) explains why only partial (50%) loss is compatible with life and produces a comparatively mild, dosage-dependent syndrome.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/) | *SIN3A haploinsufficiency causes mild ID…* | **Defining paper**; establishes gene, phenotype, mouse neurogenesis mechanism |
| [33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/) | *28-individual SIN3A cohort* | Largest cohort; severity frequencies, variant spectrum, management |
| [22206758](https://pubmed.ncbi.nlm.nih.gov/22206758/) | *Sin3a essential for genome integrity* | Embryonic lethality; essentiality supporting haploinsufficiency |
| [30279502](https://pubmed.ncbi.nlm.nih.gov/30279502/) | *Sin3A recruits Tet1 via PAH1* | PAH-domain scaffold architecture |
| [32391601](https://pubmed.ncbi.nlm.nih.gov/32391601/) | *Myt1L–Sin3 PAH1 interaction* | Links PAH1 to neuronal identity TF |
| [21676866](https://pubmed.ncbi.nlm.nih.gov/21676866/) | *SAP30–Sin3A structure* | ~2 MDa complex; PAH3 interaction |
| [41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/) | *PAH1 αα-hub stability/variants* | Functional proof missense = LOF |
| [40336075](https://pubmed.ncbi.nlm.nih.gov/40336075/) | *15q24 deletion WITKOS review* | Epidemiology; AD/CNV etiology |
| [38528912](https://pubmed.ncbi.nlm.nih.gov/38528912/) | *SIN3A + hypogonadotropic hypogonadism* | Endocrine phenotype expansion |
| [38841330](https://pubmed.ncbi.nlm.nih.gov/38841330/) | *WITKOS reflux + SIN3A deletion* | Cardiac/GI involvement; CMA diagnosis |
| [39828923](https://pubmed.ncbi.nlm.nih.gov/39828923/) | *WITKOS with cleft palate* | Craniofacial expansion |
| [39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/) | *WITKOS dystonia/ataxia* | Movement-disorder expansion |
| [40586236](https://pubmed.ncbi.nlm.nih.gov/40586236/) | *Familial WITKOS progeroid/diabetes* | Familial multisystem expansion |
| [41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/) | *Personalized treatment case* | First behavioral intervention |
| [19825413](https://pubmed.ncbi.nlm.nih.gov/19825413/) | *Drosophila SIN3/String* | Conservation, essentiality, proliferation |
| [25957495](https://pubmed.ncbi.nlm.nih.gov/25957495/) | *Yeast Sin3/Rpd3/Ume6* | Yeast conservation |
| [33130996](https://pubmed.ncbi.nlm.nih.gov/33130996/) | *REST/NRSF–SIN3 complex* | Complex composition |
| [41957673](https://pubmed.ncbi.nlm.nih.gov/41957673/), [41952182](https://pubmed.ncbi.nlm.nih.gov/41952182/) | *Chromatinopathy episignatures* | Diagnostic context for VUS |

All mechanistic and clinical claims above are tied to cited abstracts/snippets; titles alone were not used to infer content.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** With <~100 reported patients and one substantial cohort (n=28), frequency estimates (e.g., 43% hypotonia, 14% seizures) are imprecise and likely subject to ascertainment bias toward more severely affected individuals.
2. **No formal prevalence/incidence.** Epidemiology rests on qualitative "few per million" statements; no registry-based figures exist.
3. **Inferred multisystem mechanism.** Cardiac, GI, craniofacial, endocrine, and ectodermal features derive from single case reports; their frequency and the causal link to SIN3A dosage (versus contiguous-gene effects in CNV cases) are not firmly established.
4. **No validated episignature yet** specifically for SIN3A; its chromatinopathy methylation signature is anticipated but not confirmed in the cited sources.
5. **No haploinsufficiency animal model phenotype** fully recapitulating WITKOS is documented in the knowledge base (the null is embryonic lethal; the relevant mouse data are focal knockdowns).
6. **No therapeutics.** There is no disease-modifying treatment and no WITKOS-specific clinical trial.
7. **Genotype–phenotype correlations** (truncating vs missense vs deletion; variant position relative to PAH domains) remain unresolved, limiting prognostic counseling.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a WITKOS natural-history registry** to generate real prevalence/incidence and robust phenotype frequencies across age, and to track complication rates (cardiac, GI, endocrine, movement disorder).
2. **Generate and phenotype a *Sin3a* heterozygous (and brain-conditional) mouse** to test whether 50% dosage reproduces microcephaly, short stature, behavioral and multisystem features, and to define critical developmental windows.
3. **Develop and validate a SIN3A DNA-methylation episignature** (EpiSign-style) to reclassify VUS and confirm atypical/dual-diagnosis cases, leveraging the chromatinopathy framework (PMID 41957673, 41952182).
4. **Systematic genotype–phenotype analysis** correlating variant class and PAH-domain location with cognitive severity and organ involvement, building on PAH1 thermodynamic data (PMID 41759735).
5. **Functional dissection of the Myt1L/TET1–SIN3A axis** in human iPSC-derived cortical neurons/organoids carrying patient variants, to connect specific PAH-domain interaction losses to transcriptomic and neurodevelopmental phenotypes.
6. **Screen for pharmacologic modulation** — e.g., whether HDAC-pathway or targeted epigenetic agents can partially normalize transcriptional dysregulation in patient-derived models (hypothesis-generating, given the HDAC-complex mechanism).
7. **Standardize clinical surveillance guidelines** (cardiac echo, feeding/GI evaluation, endocrine/pubertal monitoring, developmental and behavioral support) and disseminate a multidisciplinary care pathway.

---

*Report compiled from 12 confirmed findings and 47 reviewed papers across five discovery iterations. Causal gene: **SIN3A** (15q24.2). Evidence sources span human clinical cohorts/case reports, mouse in vivo models, invertebrate and yeast genetics, and in vitro structural/biophysical studies, as annotated above.*


## Artifacts

- [OpenScientist final report](SIN3A-Related_Intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SIN3A-Related_Intellectual_Disability_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 21 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:39576496` *(abstract only)*: "a chronic, progressively worsening symmetric cerebellar ataxia, along with generalized dystonia. Notably, dystonia has not been previously associated with this syndrome."
  - closest text in source: "Herein, we present a 21-year-old woman with dysmorphic facial features, short stature, and a chronic, progressively worsening symmetric cerebellar ataxia, along with generalized dystonia"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "Common"; HP calls it **Global developmental delay**
- `HP:0000729` (1 mention) - the report calls it "Minority"; HP calls it **Autistic behavior**
- `HP:0007018` (1 mention) - the report calls it "Minority"; HP calls it **Attention deficit hyperactivity disorder**
- `HP:0000252` (1 mention) - the report calls it "Characteristic"; HP calls it **Microcephaly**
- `HP:0004322` (1 mention) - the report calls it "Characteristic"; HP calls it **Short stature**
- `HP:0001999` (1 mention) - the report calls it "Characteristic/recognizable"; HP calls it **Abnormal facial shape**
- `HP:0011968` (1 mention) - the report calls it "Common"; HP calls it **Feeding difficulties**
- `HP:0001627` (1 mention) - the report calls it "Not uncommon"; HP calls it **Abnormal heart morphology**
- `HP:0000175` (1 mention) - the report calls it "Rare"; HP calls it **Cleft palate**
- `UBERON:0000956` (1 mention) - the report calls it "Primary organ/system:** Central nervous system — cerebral cortex"; UBERON calls it **cerebral cortex**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016575` (2 mentions) - the report calls it "histone deacetylation"; GO calls it **obsolete histone deacetylation**
- `CL:0000047` (3 mentions) - the report calls it "neural progenitor cell"; CL calls it **neural stem cell**
- `GO:0000122` (1 mention) - the report calls it "negative regulation of transcription by RNA Pol II"; GO calls it **negative regulation of transcription by RNA polymerase II**