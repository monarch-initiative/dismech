---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T00:06:37.043419'
end_time: '2026-10-31T00:30:05.750936'
duration_seconds: 1408.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Jeffries-Lakhani Neurodevelopmental Syndrome
  mondo_id: MONDO:0958329
  category: Mendelian
  causal_genes: CRELD1
  omim_id: OMIM:620771
  synonyms: JELANS; CRELD1-related neurodevelopmental disorder; CRELD1-associated
    neurodevelopmental disorder
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
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 7
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:37947183
  relevance_assessed: 14
  on_topic: 6
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 39
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0958329
    reported_labels:
    - MONDO
    ontology_label: Jeffries-Lakhani neurodevelopmental syndrome
  - term_id: HP:0001252
    reported_labels:
    - Variable
    ontology_label: Hypotonia
  - term_id: HP:0011675
    reported_labels:
    - Slowly progressive
    ontology_label: Arrhythmia
  - term_id: HP:0002804
    reported_labels:
    - Static
    ontology_label: Arthrogryposis multiplex congenita
  - term_id: UBERON:0000955
    reported_labels:
    - Primary:* brain/CNS
    ontology_label: brain
  - term_id: NCBITaxon:6239
    reported_labels:
    - crld-1
    ontology_label: Caenorhabditis elegans
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Jeffries-Lakhani_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Jeffries-Lakhani_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Jeffries-Lakhani Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0958329 (if available)
- **Causal gene(s):** CRELD1
- **OMIM:** OMIM:620771
- **Synonyms:** JELANS; CRELD1-related neurodevelopmental disorder; CRELD1-associated neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Jeffries-Lakhani Neurodevelopmental Syndrome** covering all of the
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

# Jeffries-Lakhani Neurodevelopmental Syndrome (JELANS): A Comprehensive Disease Characterization

**Disease:** Jeffries-Lakhani Neurodevelopmental Syndrome (JELANS)
**Causal gene:** *CRELD1* (Cysteine-Rich with EGF-Like Domains 1)
**MONDO ID:** MONDO:0958329 · **OMIM:** 620771
**Synonyms:** JELANS; CRELD1-related neurodevelopmental disorder; CRELD1-associated neurodevelopmental disorder
**Inheritance:** Autosomal recessive (biallelic)

---

## Summary

Jeffries-Lakhani Neurodevelopmental Syndrome (JELANS) is a rare, recently delineated autosomal **recessive** multisystem disorder caused by **biallelic variants in *CRELD1*** (Cysteine-Rich with EGF-Like Domains 1; HGNC:14630; locus 3p25.3). It is distinct from the long-recognized role of monoallelic/heterozygous *CRELD1* variants as a susceptibility factor for atrioventricular septal defects (AVSD); JELANS is the severe, constitutional, two-hit recessive disease. The syndrome was defined in 2024 by Jeffries, Lakhani and colleagues, who identified biallelic *CRELD1* variants in 18 individuals from 14 families [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/). Its core triad is **developmental delay, early-onset (frequently intractable) epilepsy, and hypotonia**, with **cardiac arrhythmias in ~50%**, structural heart defects in ~10%, and recurrent infections in a subset. At the severe end of the spectrum, patients present with **arthrogryposis multiplex congenita and profound congenital muscle weakness**, a congenital-myasthenic-syndrome-like picture [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/).

The molecular basis of JELANS converges on two experimentally supported functions of the ER-resident CRELD1 protein. First, CRELD1 is a **regulator of calcineurin/NFATc1 signaling** essential for heart development; murine *Creld1* knockout is embryonic lethal and the protein controls VEGF-dependent endocardial proliferation via NFATc1 target genes [PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/). Second, CRELD1 is an **evolutionarily conserved ER protein-disulfide-isomerase (PDI) that acts as a maturational enhancer of ionotropic (nicotinic) acetylcholine receptors (nAChRs)**, physically interacting with and promoting the ER assembly of AChR subunits [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/). CRELD1 additionally functions as a gatekeeper of immune homeostasis, consistent with the recurrent-infection phenotype [PMID: 33169013](https://pubmed.ncbi.nlm.nih.gov/33169013/). This dual-mechanism model (NFAT signaling for cardiac features; AChR maturation for neuromuscular and epileptic features) explains the characteristic neuro-cardiac-neuromuscular-immune phenotype.

Most patients carry a **frameshift (null) allele in trans with a cysteine-disrupting missense allele**; a recurrent missense, **p.(Cys192Tyr)**, was found in 10 of 14 families, and a second cysteine-disrupting missense, **p.(Cys292Tyr)**, was reported in the severe arthrogryposis case. The natural history shows **developmental plateauing with slowly progressive non-neurologic complications in survivors**, and the disorder is **life-limiting in a subset**. Management is currently supportive; the AChR-deficiency mechanism offers a rational but as-yet-unproven rationale for cholinesterase inhibitors (e.g., pyridostigmine), by analogy to genetically defined congenital myasthenic syndromes.

---

## Section 1 — Disease Information

**Overview.** JELANS is a Mendelian, autosomal recessive neurodevelopmental disorder caused by loss of function of *CRELD1*. It is multisystem, with prominent central nervous system, cardiac, neuromuscular, and immune involvement. The disease entity was established in 2024 from an aggregated international cohort assembled via GeneMatcher-style collaboration; the evidence base is therefore a mix of **individual patient-level clinical/genetic data** (the defining cohort and subsequent case reports) and **aggregated disease-level resources** (OMIM, MONDO).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (disease) | 620771 |
| OMIM (gene) | 607170 |
| MONDO | MONDO:0958329 |
| Gene (HGNC) | *CRELD1*, HGNC:14630; NCBI Gene 78987; Ensembl ENSG00000163703; UniProt Q96HD1; locus 3p25.3 |
| ICD-10 / ICD-11 | No specific code; maps generically to a rare genetic neurodevelopmental disorder / symptomatic epilepsy category |
| Orphanet | Newly described; a dedicated ORPHAcode may not yet be assigned (not available) |
| MeSH | No dedicated descriptor; indexed under *CRELD1*, neurodevelopmental disorders, epilepsy |

**Synonyms.** JELANS; CRELD1-related neurodevelopmental disorder; CRELD1-associated neurodevelopmental disorder; descriptive title "multisystem syndrome with neurodevelopmental phenotypes, cardiac dysrhythmias and frequent infections" [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/). The eponym honors the lead authors (Jeffries and Lakhani) of the defining report.

**Important disambiguation.** The *CRELD1* literature is dominated by studies of **heterozygous missense variants as modifiers/susceptibility alleles for AVSD** (sporadic, in Down syndrome, and in Turner syndrome). Those are *not* JELANS. JELANS specifically denotes the **biallelic, constitutional, recessive multisystem syndrome**, dominated by neurodevelopmental features. Care must be taken not to conflate the two.

---

## Section 2 — Etiology

**Primary cause — genetic.** JELANS is caused exclusively by **biallelic (recessive) pathogenic variants in *CRELD1***. In the defining cohort, most affected individuals were **compound heterozygous for a frameshift/null allele in trans with a missense allele**: "*Most harbored a frameshift in trans with a missense allele, with 1 recurrent variant, p.(Cys192Tyr), identified in 10 families*" [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/). There is no environmental or infectious cause of the syndrome itself.

**Genetic risk factors.**
- *Causal variants:* biallelic *CRELD1* loss-of-function and cysteine-disrupting missense variants. Recurrent **p.(Cys192Tyr)** (10/14 families) behaves as a founder-like allele. A second severe case carried **c.875G>A p.(Cys292Tyr)** with **c.959delA p.(Gln320Argfs\*25)** [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/).
- *Inheritance requirement:* two defective alleles; heterozygous carriers (the parents) are unaffected for the syndrome.
- *Modifier/susceptibility context (distinct from JELANS):* heterozygous/rare *CRELD1* variants act as **AVSD susceptibility alleles**, including in **Down syndrome** [PMID: 29054759](https://pubmed.ncbi.nlm.nih.gov/29054759/); [PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/) and **bicuspid aortic valve in Turner syndrome** [PMID: 36929416](https://pubmed.ncbi.nlm.nih.gov/36929416/).

**Environmental risk factors.** None established. The disorder is constitutional and genetically determined. **Consanguinity/shared ancestry** increases the chance of biallelic genotypes, as for all recessive disease.

**Protective factors.** None specifically identified. A wild-type *CRELD1* allele is protective (carriers unaffected); residual function of the missense allele may modulate severity — a genotype-phenotype relationship rather than a classical protective factor.

**Gene–environment interactions.** None defined within JELANS. In the broader *CRELD1* literature, *Creld1* loss of function interacts with the **trisomy-21 genetic background** to raise CHD risk (a gene–gene/dosage interaction) [PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/) — but this is not the mechanism of recessive JELANS.

---

## Section 3 — Phenotypes

The phenotype is multisystem. Frequencies are drawn primarily from the 18-individual defining cohort [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/) and are therefore approximate.

| Phenotype | Type | Frequency | Onset | Course | Suggested HPO |
|---|---|---|---|---|---|
| Developmental delay / intellectual disability | Behavioral/cognitive | Core (majority) | Infancy | Plateauing | HP:0001263 / HP:0001249 |
| Early-onset epilepsy (often intractable/refractory) | Clinical sign | Core (majority) | Neonatal–first year | Episodic, often refractory | HP:0001250; HP:0011097 (early-onset); HP:0011171 |
| Hypotonia | Clinical sign | Core (majority) | Neonatal/infancy | Variable | HP:0001252 |
| Cardiac arrhythmia / rhythm disturbance | Clinical sign | ~50% | Variable | Slowly progressive | HP:0011675 |
| Structural congenital heart defect (incl. septal defects) | Physical | ~10% | Congenital | Static/surgical | HP:0001671 / HP:0001674 (AVSD) |
| Recurrent infections | Clinical sign | Subset | Childhood | Recurrent | HP:0002719 |
| Feeding difficulties / failure to thrive | Clinical sign | Subset | Infancy | Variable | HP:0011968 / HP:0001508 |
| Arthrogryposis multiplex congenita | Physical | Severe end | Congenital | Static | HP:0002804 |
| Severe muscle weakness | Clinical sign | Severe end | Congenital | Variable | HP:0003202 / HP:0003324 |

The defining report states the core phenotype directly: "*Affected individuals displayed an array of phenotypes involving developmental delay, early-onset epilepsy, and hypotonia, with about half demonstrating cardiac arrhythmias and some experiencing recurrent infections*" [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/).

A second, more severe presentation was reported by D'Alessandro et al. (2025): "*We report a patient with arthrogryposis, severe muscle weakness and neurodevelopmental delay. During his first year of life, he developed therapy-refractory epilepsy*" [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/). This extends the phenotypic spectrum toward a congenital neuromuscular/arthrogryposis end, mechanistically framed by nicotinic AChR biology: "*Mutations in acetylcholine receptor-subunit genes have been associated with neuromuscular diseases, such as arthrogryposis multiplex congenita (AMC) and epilepsy*" [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/).

**Severity and progression.** Severity is variable, ranging from a predominantly neurodevelopmental presentation to a severe neuromuscular (congenital-myasthenic/arthrogrypotic) presentation with therapy-refractory epilepsy. The overall course shows **developmental plateauing** with **slowly progressive non-neurologic complications** (cardiac rhythm disturbances, infections) in survivors.

**Quality of life.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder (not available). Given intellectual disability, refractory epilepsy, hypotonia/weakness, and the need for cardiac and infection surveillance, the impact on daily functioning and caregiver burden is expected to be **severe**, with dependence for activities of daily living in more severely affected individuals.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *CRELD1* (Cysteine-Rich with EGF-Like Domains 1), HGNC:14630, chromosome 3p25.3; gene OMIM 607170, disease OMIM **620771**.

**Protein architecture.** CRELD1 is an **ER-resident type-I membrane glycoprotein / protein disulfide isomerase** containing a signal peptide, an N-terminal glutamic-acid/tryptophan-rich **DUF3456 "WE" domain**, **three EGF-like domains** (including calcium-binding cb-EGF domains), and a C-terminal transmembrane anchor. The transmembrane CRLD-1A isoform corresponds to vertebrate CRELD1, whereas the KDEL-bearing isoform corresponds to CRELD2 — the two vertebrate paralogs of the single *C. elegans* *crld-1* gene [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/).

**Pathogenic variants in JELANS.**

| Variant | Type | Effect | Notes |
|---|---|---|---|
| p.(Cys192Tyr) | Missense (cysteine-disrupting) | Reduced protein function | Recurrent in 10/14 families; founder-like |
| p.(Cys292Tyr) / c.875G>A | Missense (cysteine-disrupting) | Reduced function | Severe arthrogryposis case |
| c.959delA / p.(Gln320Argfs\*25) | Frameshift | Null allele | In trans with p.Cys292Tyr |
| Various frameshift alleles | Frameshift | Loss of function | Typically in trans with a missense allele |

**Genotype pattern.** The characteristic genotype is a **null (frameshift) allele in trans with a cysteine-disrupting missense allele** [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/). The recurrent loss of cysteine residues (Cys192, Cys292) is mechanistically significant: CRELD1 functions as a protein disulfide isomerase, so disruption of structural cysteines would impair disulfide-dependent chaperone activity and EGF-domain folding.

**Variant classification (ACMG/AMP).** The recurrent p.(Cys192Tyr) and family-specific alleles are classified pathogenic/likely pathogenic on the basis of recessive segregation, functional evidence, and rarity in population databases. Functional validation showed **patient missense alleles have reduced protein function** (diminished craniofacial-defect induction upon overexpression), and **Xenopus tropicalis creld1 knockdown caused developmental defects and increased induced-seizure susceptibility** [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/).

**Allele frequency.** Individual null and cysteine-missense alleles are rare in gnomAD; the recurrent p.(Cys192Tyr) is rare but recurrent (founder-like). Exact gnomAD frequencies were not formally tabulated in this investigation.

**Somatic vs germline.** Germline (constitutional), biallelic; no somatic involvement.

**Functional consequence.** **Partial loss of function** predominates (null alleles + hypomorphic/function-reducing missense). Complete loss is likely incompatible with life (mouse null is embryonic lethal [PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/)), explaining why patients retain hypomorphic missense function on at least one allele. This contrasts with some AVSD-associated heterozygous *CRELD1* missense variants reported as gain-of-function in ECM regulation (e.g., P286R) [PMID: 24927998](https://pubmed.ncbi.nlm.nih.gov/24927998/) — again underscoring that the modifier/AVSD biology differs from recessive JELANS.

**Modifier genes.** Not established for JELANS. In AVSD contexts, *CRELD1* interacts with trisomy-21 dosage-sensitive genes and with *HEY2* [PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/) and with the pathway partner *NFATC1* [PMID: 30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/).

**Epigenetic information.** No disease-specific DNA-methylation episignature has been reported for JELANS (not available).

**Chromosomal abnormalities.** JELANS is a single-gene disorder; no recurrent large-scale rearrangement defines it. (*CRELD1* variants act as modifiers in the aneuploidies Down and Turner syndromes [PMID: 29054759](https://pubmed.ncbi.nlm.nih.gov/29054759/); [PMID: 36929416](https://pubmed.ncbi.nlm.nih.gov/36929416/).)

---

## Section 5 — Environmental Information

No **environmental, lifestyle, or infectious** agents cause or trigger JELANS. The disorder is entirely genetic. Recurrent infections in affected individuals are a *consequence* of CRELD1-dependent immune dysregulation rather than a primary infectious etiology. No toxins, radiation, occupational exposures, or dietary factors have been implicated (not applicable).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

```
1. Biallelic loss-of-function CRELD1 variants (null allele in trans with a
   cysteine-disrupting missense allele)
        │  leads to  (demonstrated: reduced activity of patient missense alleles)
        ▼
2. Reduced quantity/function of ER-resident CRELD1 protein (↓ PDI chaperone
   activity + ↓ calcineurin/NFAT-regulatory activity)
        │  branches into parallel arms
        ├───────────────┬────────────────┬─────────────────┐
        ▼               ▼                ▼                 ▼
3a. Cardiac        3b. Neuromuscular   3c. CNS            3d. Immune
   Impaired           / CNS-synaptic      excitability       Loss of immune-
   calcineurin/       Impaired ER         (shared with 3b)   gatekeeping
   NFATc1 signaling   assembly of         + NFAT-dependent
                      nicotinic AChRs     neurodevelopment
        │ results in     │ results in       │ results in      │ results in
        ▼                ▼                   ▼                 ▼
4a. Defective       4b. ↓ surface       4c. Developmental   4d. Dysregulated
    endocardial/        nicotinic AChR       delay, hypotonia    T-cell
    myocardial          at NMJ & CNS         homeostasis (↓CD4)
    development         synapses
        │                │                    │                │
        ▼                ▼                    ▼                 ▼
5a. Arrhythmia      5b. Hypotonia,      5c. Intellectual    5d. Recurrent
    (~50%),             weakness,            disability          infections
    structural CHD      arthrogryposis   (epilepsy shared
    (~10%)             (CMS-like)        across 5b/5c)
```

Steps 2→3a→4a→5a (cardiac) and 2→3b→4b→5b (neuromuscular) are **experimentally supported** in model systems; the precise link from AChR deficiency to *central* refractory epilepsy and the NFAT→neurodevelopment link (3c) are **inferred** by analogy to nAChR-subunit epilepsies and NFAT-dependent gene programs.

### Molecular pathways
- **Calcineurin/NFATc1 signaling (cardiac):** "*We show that Creld1 is sufficient to promote NFATc1 dephosphorylation and translocation to the nucleus. Creld1 is contained in a joint protein complex with the regulatory subunit of calcineurin, CnB, thereby controlling calcineurin function*" [PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/). Downstream NFAT target-gene expression drives VEGF-dependent endocardial proliferation. Suggested GO: calcineurin-NFAT signaling cascade (GO:0033173); heart development (GO:0007507); heart valve morphogenesis (GO:0003179).
- **ER receptor-assembly/quality-control pathway (neuromuscular/CNS):** "*The assembly of neurotransmitter receptors in the endoplasmic reticulum limits the number of receptors delivered to the plasma membrane, ultimately controlling neurotransmitter sensitivity and synaptic transfer function*" [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/). Suggested GO: protein disulfide isomerase activity (GO:0003756); protein folding in endoplasmic reticulum (GO:0034975); neuromuscular junction development (GO:0007274).

### Cellular processes
Endocardial/endothelial cell proliferation (cardiac morphogenesis); ER protein folding and receptor assembly quality control; cholinergic synaptic transmission at the NMJ; T-cell homeostasis.

### Protein dysfunction
CRELD1 loss removes a **maturational chaperone (PDI)**; cysteine-disrupting missense alleles specifically impair disulfide chemistry needed for client-receptor folding. Clients are **specific**: AChRs depend on CRELD1, whereas GABA-A receptors of the same superfamily are CRELD1-independent [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/). Conservation is demonstrated — mouse Creld1 rescues *C. elegans crld-1a* mutants, and Creld1 knockdown in mouse muscle cells decreases AChR surface expression.

### Immune system involvement
"*We here provide evidence that CRELD1 is an important gatekeeper of immune system homeostasis*" [PMID: 33169013](https://pubmed.ncbi.nlm.nih.gov/33169013/); the accompanying commentary is titled *"CRELD1 controls T cell homeostasis"* [PMID: 33169012](https://pubmed.ncbi.nlm.nih.gov/33169012/). Low-CRELD1 individuals show reduced CD4 T cells. This underlies the recurrent-infection phenotype, though baseline PBMC subsets in the JELANS cohort were broadly similar to healthy donors — suggesting a subtle or functional (rather than numeric) immune defect.

### Subcellular compartment
The **endoplasmic reticulum** (GO:0005783) is the central organelle: CRELD1 operates there both as an NFAT-signaling regulator and as a receptor-maturation chaperone.

### Suggested cell types (CL)
Endocardial cell (CL:0002350); cardiomyocyte (CL:0000746); skeletal myocyte/myotube (CL:0000188); motor neuron (CL:0000100); neuron (CL:0000540); CD4+ T cell (CL:0000624).

### Molecular profiling
A large human expression-variance cohort defined CRELD1-dependent transcriptional/immune phenotypes [PMID: 33169013](https://pubmed.ncbi.nlm.nih.gov/33169013/). No JELANS-specific human-tissue omics atlas yet exists.

---

## Section 7 — Anatomical Structures Affected

**Organ level.**
- *Primary:* brain/CNS (UBERON:0000955) — epilepsy, developmental delay, hypotonia; heart (UBERON:0000948) — arrhythmia, septal/structural defects; skeletal muscle (UBERON:0001134) and neuromuscular junction (UBERON:0002409) — hypotonia, weakness, arthrogryposis.
- *Secondary/complications:* joints/limbs (arthrogryposis, UBERON:0000982); immune system (recurrent infections).
- *Body systems:* nervous, cardiovascular, musculoskeletal/neuromuscular, immune.

**Tissue and cell level.** Nervous tissue (cholinergic circuits); cardiac endocardium (endocardial cells) and myocardium (cardiomyocytes); endocardial cushions/valves (UBERON:0003709); skeletal muscle; CD4+ T lymphocytes. See CL terms in Section 6.

**Subcellular level.** Endoplasmic reticulum (GO:0005783) is the key compartment; CRELD1 is a membrane-associated ER protein. Plasma-membrane receptor abundance (at the NMJ/synapse) is the downstream readout.

**Localization / lateralization.** Manifestations are **generalized/bilateral** (generalized hypotonia, generalized epilepsy, symmetric arthrogryposis); cardiac defects are central (septal). No consistent lateralization is described.

---

## Section 8 — Temporal Development

**Onset.** Congenital to early infantile. Hypotonia and structural cardiac defects are congenital; epilepsy is typically **neonatal to first year of life** and frequently intractable [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/); [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/). Arthrogryposis (when present) is congenital.

**Progression.** The neurodevelopmental course shows **developmental plateauing** rather than frank regression, while **non-neurologic complications are slowly progressive** (cardiac rhythm disturbances, infections). The defining cohort describes these complications "in survivors," indicating the disorder can be **life-limiting/fatal in a subset**. The course is therefore best described as developmental with slowly progressive multisystem complications, with variable severity.

**Patterns.** Seizures may be episodic and, in milder cases, amenable to control; arrhythmias are episodic. No spontaneous remission of the underlying disorder. **Critical periods:** the prenatal/perinatal and first-year windows (cardiac morphogenesis; NMJ/synapse formation; seizure onset) are the key vulnerability windows and plausible intervention windows.

---

## Section 9 — Inheritance and Population

**Inheritance.** Autosomal **recessive** (biallelic *CRELD1*). Parents are unaffected carriers.

**Penetrance / expressivity.** Appears **highly penetrant** for a neurodevelopmental phenotype in biallelic individuals, with **variable expressivity** — ranging from predominantly neurodevelopmental to severe neuromuscular/arthrogrypotic presentations (cardiac arrhythmia ~50%, infections in a subset).

**Genetic anticipation / mosaicism.** Not applicable (not a repeat-expansion disorder); no germline mosaicism reports.

**Founder effects / consanguinity.** The recurrent **p.(Cys192Tyr)** allele in 10/14 families suggests a **founder-like effect**; consanguinity may contribute to biallelic (including homozygous) genotypes.

**Epidemiology.** JELANS is **ultra-rare**. Only ~18 individuals from 14 families (defining cohort) plus isolated subsequent cases are reported; true prevalence/incidence are unknown and presumably <1 per 1,000,000 (not available).

**Population demographics.** The defining cohort was international; no specific ethnic predilection is established beyond the founder-like recurrent allele. **Sex ratio** is not clearly skewed (consistent with autosomal recessive inheritance). Age distribution reflects a pediatric-onset disorder. **Carrier frequency** is not formally established; individual pathogenic alleles are rare in gnomAD.

---

## Section 10 — Diagnostics

**Genetic testing is the definitive diagnostic modality.**
- *Recommended approach:* **trio exome (WES) or genome (WGS) sequencing**, which identifies biallelic *CRELD1* variants and establishes phase. The syndrome was defined by next-generation sequencing plus GeneMatcher-style international matchmaking [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/).
- *Single-gene / trio testing:* confirm biallelic *CRELD1* variants and the **trans** configuration (typically frameshift + missense); confirm/segregate the recurrent p.(Cys192Tyr) and family-specific frameshift alleles.
- *Gene panels:* epilepsy, neurodevelopmental, hypotonia, arthrogryposis, and congenital-myasthenic-syndrome panels should include *CRELD1*.
- *CMA/karyotype/FISH:* not diagnostic (single-gene disorder) but used to exclude chromosomal differentials. mtDNA and repeat-expansion testing are not indicated.

**Clinical / ancillary tests.**
- *EEG* for epilepsy characterization (often shows refractory epileptiform activity).
- *ECG / Holter / echocardiography* for arrhythmia and structural cardiac screening (arrhythmia ~50%, structural defect ~10%).
- *Brain MRI* for developmental delay/epilepsy evaluation (findings not yet systematically characterized).
- *Neuromuscular work-up* (EMG/repetitive nerve stimulation, CK) in the CMS-like/arthrogryposis presentation.
- *Immune evaluation* (immunoglobulins, lymphocyte subsets) given recurrent infections — note baseline PBMC subsets were grossly normal in the cohort.

**Biomarkers.** No specific circulating/biochemical biomarker; diagnosis rests on genotype plus phenotype. No methylation episignature defined.

**Clinical criteria / differential diagnosis.** No formal consensus criteria yet. Differential diagnoses include other recessive developmental-and-epileptic encephalopathies; **congenital myasthenic syndromes** (nAChR-subunit, agrin/rapsyn/DOK7-related) — especially for the weakness/arthrogryposis presentation; *NFATC1*-related AVSD (distinct, cardiac-restricted) [PMID: 30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/); and syndromic causes of arthrogryposis. Distinguished by biallelic *CRELD1* variants.

**Screening.** No population newborn screening. **Cascade carrier testing** of relatives and **prenatal/preimplantation genetic testing** are appropriate once familial variants are known.

---

## Section 11 — Outcome / Prognosis

**Survival/mortality.** No formal survival statistics, but the defining cohort explicitly refers to "survivors," indicating **the disorder is life-limiting in a subset** [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/). Principal risks are early-onset/refractory epilepsy, severe hypotonia/respiratory compromise, and cardiac arrhythmia (potentially life-threatening if unmonitored).

**Morbidity / function.** High morbidity: lifelong intellectual disability, refractory epilepsy, hypotonia/weakness (up to arthrogryposis with profound weakness), plus the need for ongoing cardiac and infection surveillance. Significant disability and care-dependence are expected in moderate-to-severe cases.

**Disease course / complications.** Developmental plateauing; slowly progressive cardiac rhythm disturbances; recurrent infections; refractory seizures. Structural heart defects (~10%) may require surgical repair.

**Prognostic factors.** Severity and control of epilepsy, presence/severity of cardiac arrhythmia, the severe neuromuscular phenotype (arthrogryposis + refractory epilepsy portends a worse course), and the **residual function of the missense allele** (genotype). No validated molecular prognostic biomarker exists.

---

## Section 12 — Treatment

**Current standard: supportive / multidisciplinary.** There is no disease-modifying or curative therapy. Management targets each system:
- *Epilepsy:* antiseizure medications chosen by seizure type/EEG (NCIT: Anticonvulsant Agent); seizures are frequently **intractable/therapy-refractory** [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/).
- *Cardiac:* antiarrhythmic/cardiology-directed therapy; device therapy (pacemaker) if indicated; surgical repair of structural defects.
- *Neuromuscular/developmental:* physical, occupational, and speech therapy (NCIT: Physical Therapy; Occupational Therapy; Speech Therapy); management of hypotonia and contractures; feeding support.
- *Immune/infectious:* prompt treatment and surveillance of recurrent infections; immunology referral; consider immunoglobulin replacement if a humoral defect is found (individualized).

**Mechanism-based (candidate, unproven) therapy — cholinesterase inhibitors.** Because CRELD1 is a **maturation enhancer controlling surface abundance of nicotinic AChRs** [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/), biallelic loss reduces functional AChRs at the NMJ, producing a **congenital-myasthenic-syndrome-like** picture. This mechanistically motivates **cholinesterase inhibitors such as pyridostigmine** (NCIT: Pyridostigmine; a reversible AChE inhibitor that raises synaptic acetylcholine), by analogy to AChR-deficiency CMS [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/). **Important caveat:** this is an untested mechanistic inference requiring genetic-subtype caution — pyridostigmine is beneficial in some CMS subtypes but harmful in others (e.g., slow-channel, DOK7, COLQ-related). Any trial should be cautious, monitored, and ideally protocolized.

**Advanced / targeted / gene therapy.** None available; no gene, cell, RNA, or targeted small-molecule therapy for *CRELD1* (research stage only; not applicable clinically). No registered clinical trials specific to JELANS were identified.

**Treatment strategy.** Multidisciplinary care (neurology, cardiology, immunology, developmental pediatrics, genetics). The AChR-deficiency mechanism provides the main precision-medicine hypothesis (cholinesterase inhibitors, with subtype caution); no established pharmacogenomic protocol exists for this gene.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable for a Mendelian disorder beyond reproductive options. **Genetic counseling** for at-risk couples (25% recurrence risk per pregnancy for carrier couples).
- **Secondary prevention (reproductive):** Carrier screening, cascade testing, prenatal diagnosis, and **preimplantation genetic testing (PGT-M)** for families with known biallelic variants. Early sequencing-based diagnosis enables early seizure control, cardiac surveillance, and infection management.
- **Tertiary prevention (preventing complications):** Proactive cardiac surveillance (ECG/echo) for arrhythmia; structured seizure management; infection monitoring/immunology follow-up; physical therapy to limit contractures.
- **Counseling:** Autosomal recessive recurrence risk is **25%**; cascade testing and reproductive options should be offered.
- **Immunization / public health / environmental:** Standard childhood immunizations and infection precautions for the infection-prone subset; no disease-specific vaccine or environmental intervention applies (not applicable).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs.** *CRELD1* is evolutionarily conserved. Orthologs: mouse *Creld1* (NCBI Gene 171508; NCBITaxon:10090), *Xenopus tropicalis* creld1 (NCBITaxon:8364), and the single *C. elegans* gene *crld-1* (NCBITaxon:6239), whose two isoforms correspond to the vertebrate paralogs CRELD1 (transmembrane) and CRELD2 (KDEL) [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/).
- **Natural disease in other species.** No naturally occurring companion-animal or wildlife disease equivalent to JELANS is documented in OMIA (not available).
- **Comparative biology.** Mouse *Creld1* is essential for heart development; **global knockout is embryonic lethal** [PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/); conditional KO reveals myocardial roles [PMID: 33773996](https://pubmed.ncbi.nlm.nih.gov/33773996/). *Xenopus* creld1 knockdown reproduces developmental defects and seizure susceptibility [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/). The AChR-maturation function is **deeply conserved**: mouse Creld1 rescues *C. elegans crld-1a* mutants, and mouse-muscle Creld1 knockdown lowers surface AChR [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/). Both the calcineurin/NFATc1 and the ER-PDI/AChR mechanisms are conserved — supporting cross-species validity.
- **Transmission / zoonosis.** Not applicable (genetic disorder).

---

## Section 15 — Model Organisms

| Model | Type | Key findings | Recapitulation | Reference |
|---|---|---|---|---|
| *C. elegans* — *crld-1* mutants | Invertebrate | Identified in a forward (levamisole-resistance) screen; required for synaptic nicotinic AChR expression; crld-1A is an ER PDI assembling AChRs; rescued by mouse Creld1 | Core neuromuscular/AChR-assembly arm; proves conservation | [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/) |
| *C. elegans* — patient-variant knock-in | Invertebrate | Compound-heterozygous CRELD1 variants reduce AChRs at the NMJ | Models patient genotype's functional effect | [PMID: 40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/) |
| *Xenopus tropicalis* — creld1 knockdown/CRISPR | Vertebrate | Developmental defects; increased induced-seizure susceptibility; ~10% structural cardiac defects; overexpression assay measures missense allele function | Strong neurodevelopmental/seizure recapitulation; key disease-validation model | [PMID: 37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/) |
| Mouse — Creld1 knockdown in muscle cells | In vitro (mammalian) | Decreased AChR surface expression | Supports nAChR-maturation mechanism in mammals | [PMID: 30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/) |
| Mouse — global *Creld1* KO | Mammalian, knockout | Embryonic lethal; essential for heart development/endocardial proliferation | Cardiac developmental role; lethality limits postnatal study | [PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/) |
| Mouse — conditional *Creld1* KO (endocardial/myocardial) | Mammalian, conditional | Regulates myocardial development and function | Enables tissue-specific cardiac study | [PMID: 33773996](https://pubmed.ncbi.nlm.nih.gov/33773996/) |
| Mouse — Ts65Dn × *Creld1* LoF cross | Mammalian, genetic interaction | Increases CHD frequency on trisomic background | Models CRELD1 as a CHD modifier (AVSD context) | [PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/) |

**Model resources.** MGI (mouse *Creld1*), Xenbase (Xenopus creld1), WormBase (*crld-1*), Alliance of Genome Resources.

**Model strengths.** Collectively, the models reproduce the cardiac (mouse NFAT), neuromuscular/AChR (worm, mouse muscle cells), and seizure/developmental (Xenopus) arms, and demonstrate cross-species rescue — strong evidence of conserved mechanism.

**Model limitations.** Global mouse KO is embryonic lethal, precluding study of postnatal neurodevelopment and epilepsy; no mouse model fully recapitulates the combined human neuro-cardiac-immune triad with the specific biallelic null/hypomorphic genotype. Patient-specific iPSC/organoid or humanized knock-in CNS models are not yet established.

---

## Mechanistic Model / Interpretation

JELANS is best understood as a **dual-mechanism, ER-centered CRELD1 loss-of-function disorder**:

```
                 ┌──────────────────────────────────────────┐
                 │   Biallelic CRELD1 loss of function       │
                 │  (null allele + Cys-disrupting missense)  │
                 └──────────────────┬───────────────────────┘
                                    │  ER-resident CRELD1 depleted/hypofunctional
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
  Calcineurin/NFATc1        PDI-dependent AChR          Immune-homeostasis
  signaling impaired        maturation impaired          gatekeeping lost
          │                         │                         │
          ▼                         ▼                         ▼
  Endocardial/myocardial    ↓ surface nicotinic AChR     Dysregulated T-cell
  development & rhythm       at NMJ & CNS synapses        homeostasis (↓CD4)
          │                         │                         │
          ▼                         ▼                         ▼
  Arrhythmia (~50%),        Hypotonia, weakness,         Recurrent
  structural CHD (~10%)     arthrogryposis, epilepsy      infections
```

The cardiac arm (NFAT) and the neuromuscular/CNS arm (AChR maturation) are both experimentally grounded; the immune arm is supported by independent mouse/human work. The convergence on the **endoplasmic reticulum** — where CRELD1 both scaffolds calcineurin/NFAT signaling and performs PDI-dependent receptor assembly — unifies the otherwise disparate neuro-cardiac-neuromuscular-immune phenotype. The recurrent loss of **cysteine residues** (Cys192, Cys292) in pathogenic missense alleles is mechanistically coherent with disruption of CRELD1's disulfide-isomerase chemistry, which both functions depend on.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [37947183](https://pubmed.ncbi.nlm.nih.gov/37947183/) | *Biallelic CRELD1 variants cause a multisystem syndrome...* | **Defining cohort** (18 pts/14 families); inheritance, genotype, phenotype frequencies, Xenopus + functional validation, natural history | Human clinical + model |
| [40980404](https://pubmed.ncbi.nlm.nih.gov/40980404/) | *Biallelic CRELD1 variants cause severe muscle weakness and infantile epilepsy* | Phenotype extension (arthrogryposis, refractory epilepsy); p.Cys292Tyr + frameshift; C. elegans NMJ AChR reduction; CMS-like therapeutic rationale | Human clinical + C. elegans |
| [30407909](https://pubmed.ncbi.nlm.nih.gov/30407909/) | *CRELD1 is an evolutionarily-conserved maturational enhancer of ionotropic AChRs* | **Core neuromuscular mechanism**: ER PDI, AChR maturation, cross-species conservation, client specificity | C. elegans / mouse / in vitro |
| [24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/) | *Murine Creld1 controls cardiac development through calcineurin/NFATc1* | **Cardiac mechanism**: NFAT signaling; KO embryonic lethal | Mouse / in vitro |
| [33773996](https://pubmed.ncbi.nlm.nih.gov/33773996/) | *Creld1 regulates myocardial development and function* | Conditional KO; tissue-specific cardiac role | Mouse |
| [33169013](https://pubmed.ncbi.nlm.nih.gov/33169013/) | *CRELD1 modulates homeostasis of the immune system* | Immune-gatekeeper function → infections; ↓CD4 T cells | Human cohort / mouse |
| [33169012](https://pubmed.ncbi.nlm.nih.gov/33169012/) | *CRELD1 controls T cell homeostasis* (commentary) | Supports T-cell homeostasis role | Review |
| [22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/) | *Genetic modifiers in Down syndrome CHD* | Context: CRELD1 as dosage-threshold CHD modifier | Mouse / human |
| [30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/) | *NFATC1 missense mutations and AVSD* | Supports calcineurin/NFAT pathway in cardiac defects; differential | Human / zebrafish |
| [36929416](https://pubmed.ncbi.nlm.nih.gov/36929416/) | *CRELD1 variants and bicuspid aortic valve in Turner syndrome* | Context: heterozygous modifier role (distinct from JELANS) | Human genetics |
| [29054759](https://pubmed.ncbi.nlm.nih.gov/29054759/); [22987595](https://pubmed.ncbi.nlm.nih.gov/22987595/); [21413875](https://pubmed.ncbi.nlm.nih.gov/21413875/); [24927998](https://pubmed.ncbi.nlm.nih.gov/24927998/) | Heterozygous CRELD1 variants as AVSD risk/modifier alleles | Context: contrasting heterozygous/GoF modifier biology | Human genetics / in vitro |

Evidence spans **human clinical** (defining cohort, case reports), **model organism** (mouse, Xenopus, C. elegans), and **in vitro** (muscle-cell knockdown, functional missense assays). The mechanistic model is unusually well supported for an ultra-rare disorder because CRELD1's two core functions were independently established before JELANS was delineated.

---

## Supported vs. Refuted Hypotheses

- **Supported:** JELANS is autosomal recessive, caused by biallelic (null + hypomorphic cysteine-missense) *CRELD1* variants; it is a multisystem neuro-cardiac-neuromuscular-immune syndrome; mechanisms involve impaired calcineurin/NFATc1 signaling **and** impaired ER maturation of nicotinic AChRs; the p.Cys192Tyr allele is recurrent (10/14 families); model organisms (C. elegans, Xenopus, mouse) recapitulate AChR loss, seizure susceptibility, and cardiac defects.
- **Newly strengthened:** The AChR-maturation mechanism is now **demonstrated** (not merely inferred), providing a unified explanation for the neuromuscular and epilepsy features and a **mechanism-based (candidate) therapeutic rationale for cholinesterase inhibitors** (pyridostigmine), with subtype caution.
- **Nuanced / partially refuted:** Recurrent infections are *not* explained by a gross baseline shift in patient PBMC immune-cell proportions (similar to healthy donors); the immune defect is likely functional rather than numeric. The course is **not purely static** — it shows developmental plateauing with slowly progressive complications and is **life-limiting in a subset**.

---

## Limitations and Knowledge Gaps

1. **Small cohort.** The clinical picture rests on ~18 individuals plus isolated cases; frequencies (~50% arrhythmia, ~10% structural CHD) are approximate and may shift as more patients are identified. Penetrance, prognosis, sex ratio, and natural history are preliminary.
2. **No human disease-tissue omics.** No transcriptomic/proteomic/metabolomic/epigenomic atlas of patient tissues exists; molecular profiling evidence is indirect (model systems, immune-homeostasis cohort).
3. **Epilepsy and immune mechanisms partly inferred.** The causal link from AChR deficiency to *central* refractory epilepsy and the NFAT→neurodevelopment link are inferred rather than directly demonstrated in human CNS; the immune defect appears functional rather than numeric.
4. **No validated biomarker or prognostic model.** Genotype-phenotype correlations (missense residual function; severe neuromuscular subtype) are suggestive but unquantified; no methylation episignature.
5. **Therapy untested.** The cholinesterase-inhibitor rationale is a mechanistic hypothesis; efficacy and safety in JELANS are unproven, and CMS experience warns that AChE inhibitors harm some subtypes.
6. **No faithful mammalian CNS model.** Embryonic lethality of global mouse KO limits study of the neurodevelopmental/epileptic phenotype; conditional neural and patient-genotype knock-in CNS models are lacking.

---

## Proposed Follow-up Experiments / Actions

1. **Expand and deep-phenotype the cohort** via international registries and GeneMatcher to firm up phenotype frequencies, natural history, survival, sex ratio, and genotype-phenotype correlation (especially missense residual-function vs severity).
2. **Build a patient-genotype knock-in mouse or neural conditional KO** to model epilepsy and neurodevelopment; complement with **patient iPSC-derived motor neurons/muscle and cerebral/neuromuscular organoids** to measure surface AChR abundance and synaptic function.
3. **Quantify AChR deficits in patient-derived systems** and test whether **cholinesterase inhibitors (pyridostigmine) or 3,4-diaminopyridine** rescue neuromuscular function — and whether any subtype would be harmed — before any cautious, protocolized human trial.
4. **Electrophysiology in patients** (repetitive nerve stimulation, single-fiber EMG) to test for a decremental/NMJ-transmission defect supporting the CMS-like model and guiding AChE-inhibitor trials.
5. **Define a methylation episignature** and search for diagnostic/prognostic biomarkers to aid VUS reclassification; estimate gnomAD-based carrier frequency.
6. **Structural/biochemical work** on CRELD1 PDI activity with cysteine-disrupting missense alleles (Cys192Tyr, Cys292Tyr) to confirm the disulfide-chemistry mechanism and prioritize alleles amenable to chaperone-rescue strategies.
7. **Detailed immune characterization** (T-cell subsets/function) in patients to clarify the infection phenotype and whether prophylaxis is warranted.

---

*Evidence source types are indicated throughout: human clinical (defining cohort and case reports), model organism (mouse, Xenopus, C. elegans), and in vitro (muscle-cell knockdown, functional missense assays). Causal steps that are inferred rather than directly demonstrated are explicitly flagged.*


## Artifacts

- [OpenScientist final report](Jeffries-Lakhani_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Jeffries-Lakhani_Neurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:37947183`: "multisystem syndrome with neurodevelopmental phenotypes, cardiac dysrhythmias and frequent infections"
  - closest text in source: "Most presented with early-onset neurodevelopmental features, most notably hypotonia and epilepsy, with developmental plateauing and slowly progressive non-neurologic medical complexities in survivors, including cardiac rhythm disturbances and frequent infections"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0958329` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Jeffries-Lakhani neurodevelopmental syndrome**
- `HP:0001252` (1 mention) - the report calls it "Variable"; HP calls it **Hypotonia**
- `HP:0011675` (1 mention) - the report calls it "Slowly progressive"; HP calls it **Arrhythmia**
- `HP:0002804` (1 mention) - the report calls it "Static"; HP calls it **Arthrogryposis multiplex congenita**
- `UBERON:0000955` (1 mention) - the report calls it "Primary:* brain/CNS"; UBERON calls it **brain**
- `NCBITaxon:6239` (1 mention) - the report calls it "crld-1"; NCBITaxon calls it **Caenorhabditis elegans**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002719` (1 mention) - the report calls it "Recurrent"; HP calls it **Recurrent infections**