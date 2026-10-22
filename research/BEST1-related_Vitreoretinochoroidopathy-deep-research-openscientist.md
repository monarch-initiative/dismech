---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T12:15:12.649931'
end_time: '2026-10-22T12:30:44.793393'
duration_seconds: 932.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: BEST1-related Vitreoretinochoroidopathy
  mondo_id: MONDO:0700240
  category: Mendelian
  causal_genes: BEST1
  omim_id: not recorded
  synonyms: ADVRIC
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
citation_count: 24
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 19
  validator_version: 0.3.0
term_validation:
  total_terms: 49
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 0
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: MONDO:0700240
    reported_labels:
    - MONDO
    ontology_label: BEST1-related vitreoretinochoroidopathy
  - term_id: HP:0004327
    reported_labels:
    - Common
    ontology_label: Abnormal vitreous humor morphology
  - term_id: HP:0000533
    reported_labels:
    - Common
    ontology_label: Chorioretinal atrophy
  - term_id: HP:0012808
    reported_labels:
    - Subset
    ontology_label: Abnormal nasal base norphology
  - term_id: HP:0012109
    reported_labels:
    - Subset
    ontology_label: Angle closure glaucoma
  - term_id: HP:0000526
    reported_labels:
    - Subset
    ontology_label: Aniridia
  - term_id: HP:0000518
    reported_labels:
    - Frequent (4/6 in V86M family)
    ontology_label: Cataract
  - term_id: HP:0001093
    reported_labels:
    - Rare
    ontology_label: Optic nerve dysplasia
  - term_id: HP:0000545
    reported_labels:
    - Increased vs BVMD
    ontology_label: Myopia
  - term_id: HP:0000608
    reported_labels:
    - Common
    ontology_label: Macular degeneration
  - term_id: HP:0011505
    reported_labels:
    - Subset
    ontology_label: Cystoid macular edema
  - term_id: UBERON:0000970
    reported_labels:
    - Primary organ:** eye
    ontology_label: eye
  - term_id: UBERON:0000964
    reported_labels:
    - "Secondary involvement:** anterior segment \u2014 cornea"
    ontology_label: cornea
  - term_id: NCIT:C15262
    reported_labels:
    - NCIT term suggestions:** Anti-VEGF Therapy, Laser Therapy
    ontology_label: Immunotherapy
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: BEST1-related_Vitreoretinochoroidopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: BEST1-related_Vitreoretinochoroidopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BEST1-related Vitreoretinochoroidopathy
- **MONDO ID:** MONDO:0700240 (if available)
- **Causal gene(s):** BEST1
- **OMIM:** not recorded
- **Synonyms:** ADVRIC
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **BEST1-related Vitreoretinochoroidopathy** covering all of the
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

# BEST1-related Vitreoretinochoroidopathy (ADVIRC): A Comprehensive Disease Characterization

**Disease:** BEST1-related Vitreoretinochoroidopathy (Autosomal Dominant Vitreoretinochoroidopathy, ADVIRC)
**MONDO ID:** MONDO:0700240 · **OMIM:** 193220 · **Causal gene:** **BEST1** (bestrophin-1; VMD2)
**Category:** Mendelian, autosomal dominant inherited retinal dystrophy

---

## Summary

**Autosomal dominant vitreoretinochoroidopathy (ADVIRC) is a rare Mendelian inherited retinal dystrophy caused by heterozygous mutations in the *BEST1* gene (also called *VMD2*), which encodes bestrophin-1 — a ~580-amino-acid, ~66 kDa pentameric calcium-activated chloride channel located in the basolateral plasma membrane of the retinal pigment epithelium (RPE).** It is one of the three classic "bestrophinopathies," alongside Best vitelliform macular dystrophy (BVMD) and autosomal recessive bestrophinopathy (ARB), and it is the rarest of the three. ADVIRC is defined clinically by a pathognomonic 360-degree circumferential band of peripheral retinal hyperpigmentation with a discrete posterior (equatorial) boundary, together with fibrillar vitreous condensation, retinal vascular leakage and neovascularization, choroidal atrophy, and a spectrum of developmental ocular anomalies including nanophthalmos/microcornea, iris dysgenesis, cataract, and angle-closure glaucoma.

What mechanistically distinguishes ADVIRC from the other bestrophinopathies is its molecular origin. The causative *BEST1* variants cluster at exonic splice-regulatory elements and simultaneously produce a missense substitution **and** exon skipping, generating three bestrophin-1 isoforms per heterozygous individual (wild-type, missense, and in-frame deletion). These aberrant isoforms co-assemble into the homopentameric channel and confer a **gain-of-function** effect, in contrast to the loss-of-function or dominant-negative mechanisms that drive BVMD and ARB. The downstream consequences branch into a developmental arm (ocular malformations arising during eye development) and a degenerative arm (progressive RPE dysfunction, photoreceptor loss, blood-retinal barrier breakdown, and choroidal atrophy).

Clinically, ADVIRC is slowly progressive with markedly variable expressivity — even within a single family carrying the same variant — ranging from mild peripheral changes with preserved acuity to severe pan-ocular disease with no light perception. There is no disease-specific or curative therapy; management is supportive, addressing macular edema, neovascularization, glaucoma, cataract, and retinal detachment. Because the mechanism is gain-of-function, conventional gene-supplementation strategies are expected to fail, and allele-specific suppression (e.g., CRISPR/Cas9 editing of the mutant allele) is the leading experimental therapeutic avenue. This report consolidates seven confirmed findings and 52 reviewed papers into a structured characterization across all requested domains.

---

## Key Findings

### Finding 1 — ADVIRC is caused by *BEST1* (VMD2) mutations acting through aberrant pre-mRNA splicing

The landmark study establishing the molecular basis of ADVIRC was Yardley et al. (2004). Using genetic linkage followed by sequencing in five ADVIRC families, the authors identified three pathogenic *VMD2*/*BEST1* sequence alterations (reported variants include V86M, Y227N, and V235A), each affecting exonic splice enhancer/silencer sites. A minigene splicing assay demonstrated that each mutation simultaneously produces a missense substitution **and** exon skipping. The verbatim conclusion was that *"All sequences showed simultaneous missense substitutions and exon skipping"* [PMID: 15452077](https://pubmed.ncbi.nlm.nih.gov/15452077/). The consequence is that each heterozygous individual expresses three distinct bestrophin isoforms: the wild-type protein, a full-length protein carrying the missense substitution, and an in-frame deletion product from skipping the affected exon.

This paper also pinpointed the gene product and its localization: *"VMD2 encodes bestrophin, a transmembrane protein located at the basolateral membrane of the RPE, that is also mutated in Best macular dystrophy"* [PMID: 15452077](https://pubmed.ncbi.nlm.nih.gov/15452077/). The study additionally linked ADVIRC-associated splice mutations to nanophthalmos, connecting the splicing defect to a developmental ocular phenotype. This establishes the **initiating molecular lesion** of ADVIRC.

- **Gene annotation:** HGNC:1114 (*BEST1*), OMIM gene 607854.
- **Evidence type:** Human clinical/genetic + in vitro minigene assay.

### Finding 2 — ADVIRC is associated with gain-of-function in bestrophin-1, unlike other bestrophinopathies

A recent retrospective case series by Ni et al. (2026) compared 8 ADVIRC, 10 BVMD, and 10 control eyes using quantitative imaging. The ADVIRC outer-segment layer was significantly thinner than in BVMD at all foveal locations, and the ADVIRC photoreceptor layer was thinner than in both BVMD and controls perifoveally (Kruskal–Wallis / Mann–Whitney tests). A companion systematic review documented increased myopia prevalence in ADVIRC (median axial length 24.7 mm, spherical refraction −0.63 D) relative to BVMD and controls. The authors framed the mechanism explicitly: *"Autosomal dominant vitreoretinochoroidopathy (ADVIRC) is associated with gain-of-function in bestrophin-1 instead of loss-of-function or dominant-negative mechanisms in other bestrophinopathies"* [PMID: 41991505](https://pubmed.ncbi.nlm.nih.gov/41991505/), and connected that mechanism to phenotype: *"This study found that gain-of-function in ADVIRC may cause increased prevalence of myopia, PR layer thinning, and outer segment shortening"* [PMID: 41991505](https://pubmed.ncbi.nlm.nih.gov/41991505/).

This gain-of-function framing is mechanistically pivotal: it explains why ADVIRC presents with developmental anomalies and a distinct degenerative profile, and it has direct therapeutic implications (gene supplementation would not overcome a toxic gain-of-function allele).

- **Evidence type:** Human clinical imaging cohort + systematic review.

### Finding 3 — Pathognomonic 360-degree circumferential peripheral pigmentary band with a discrete posterior boundary

Multiple independent case series describe the defining ophthalmoscopic sign of ADVIRC. Blair et al. (1984) described *"peripheral, coarse pigmentary degeneration of the fundus for 360 degrees, with a relatively discrete posterior border in the equatorial region (this finding may be pathognomonic)"* [PMID: 6689931](https://pubmed.ncbi.nlm.nih.gov/6689931/), together with punctate yellow-white retinal opacities, vascular abnormalities, blood-retinal barrier breakdown, retinal neovascularization, vitreous abnormalities, and choroidal atrophy.

Roider et al. (1997), studying an independent pedigree (7/15 family members affected), confirmed: *"The main clinical findings were peripheral pigmentary changes for 360 degrees, with a discrete boundary near the equator"* [PMID: 9279944](https://pubmed.ncbi.nlm.nih.gov/9279944/), and documented marked reduction of the EOG light rise (reduced Arden ratio), implicating RPE dysfunction.

Goldberg et al. (1989) provided histopathologic correlation, describing ADVIRC as *"clinically characterized by a slowly progressive or stationary circumferential peripheral pigmentary retinopathy with fibrillar condensation of the vitreous"* [PMID: 2516300](https://pubmed.ncbi.nlm.nih.gov/2516300/), with disorganized peripheral retina, focally atrophic RPE, perivascular pigment migration, equatorial multifocal photoreceptor loss, and a preretinal membrane of condensed vitreous and Müller cells.

- **HPO suggestions:** Abnormal retinal pigmentation (HP:0007703), Retinal pigment epithelial atrophy (HP:0007894), Peripheral retinal degeneration (HP:0007769), Vitreous floaters / abnormal vitreous morphology (HP:0004327), Chorioretinal atrophy (HP:0000533), Retinal neovascularization (HP:0012808).
- **Evidence type:** Human clinical case series + histopathology.

### Finding 4 — BEST1 encodes bestrophin-1, a Ca²⁺-activated Cl⁻ channel at the RPE basolateral membrane

*BEST1* (*VMD2*) encodes bestrophin-1, a ~580-amino-acid, ~66 kDa transmembrane protein. Guziewicz et al. (2007) defined the protein as one that *"encodes bestrophin, a 580-amino acid protein of 66 kDa"* [PMID: 17460247](https://pubmed.ncbi.nlm.nih.gov/17460247/) and localized it via immunocytochemistry: *"immunocytochemistry of normal canine retina demonstrated specific localization of protein to the RPE basolateral plasma membranes"* [PMID: 17460247](https://pubmed.ncbi.nlm.nih.gov/17460247/).

Functionally, Wang et al. (2026) described bestrophin-1 as *"a calcium-activated chloride channel predominantly expressed in the RPE, where it plays essential roles in ionic homeostasis, transepithelial transport, and regulation of the visual cycle"* [PMID: 42222334](https://pubmed.ncbi.nlm.nih.gov/42222334/). Cryo-EM studies confirm that bestrophin-1 assembles as a homopentameric channel with resolved closed and partially open conformations (Owji et al. 2022, [PMID: 35789156](https://pubmed.ncbi.nlm.nih.gov/35789156/); Kim et al. 2025, [PMID: 40043778](https://pubmed.ncbi.nlm.nih.gov/40043778/)). The pentameric architecture is mechanistically important for ADVIRC, because it allows mutant and wild-type subunits to co-assemble.

- **GO suggestions:** chloride channel activity (GO:0005254), calcium-activated chloride channel activity (GO:0005229), chloride transmembrane transport (GO:1902476), basolateral plasma membrane (GO:0016323).
- **CHEBI:** chloride (CHEBI:17996), calcium(2+) (CHEBI:29108).
- **Evidence type:** Model organism (canine) immunocytochemistry + human/structural biology + review.

### Finding 5 — ADVIRC causes developmental anterior-segment/ocular anomalies with marked variable expressivity

Vincent et al. (2011) studied a family with the heterozygous *BEST1* variant p.V86M (c.256G>A). Among six subjects, the phenotype spanned: *"angle closure glaucoma (n = 2), microcornea with shallow anterior chamber (n = 1), iris dysgenesis (n = 2), cataracts (n = 4), classical peripheral concentric band of retinal hyperpigmentation (n = 5), and optic nerve dysplasia (n = 1)"* [PMID: 21072067](https://pubmed.ncbi.nlm.nih.gov/21072067/). Visual acuity ranged from ≥20/25 to no light perception, and full-field ERG from low-normal to non-recordable with age. The authors characterized the disorder as *"a slowly progressive vitreoretinal degeneration that demonstrates marked intra-familial phenotypic variability"* [PMID: 21072067](https://pubmed.ncbi.nlm.nih.gov/21072067/).

Variable expressivity within families carrying the same variant is a recurring theme: da Palma et al. (2021) documented it in a three-generation pedigree with c.715G>A/p.V239M [PMID: 34746433](https://pubmed.ncbi.nlm.nih.gov/34746433/), and Mainguy et al. (2024) reported the splice variant c.1101-1G>T with a distinctive ADVIRC phenotype [PMID: 38957071](https://pubmed.ncbi.nlm.nih.gov/38957071/). This finding supports the view that ADVIRC is a **pan-ocular developmental and degenerative** condition, not merely a peripheral retinopathy.

- **HPO suggestions:** Glaucoma / Angle-closure glaucoma (HP:0000501 / HP:0012109), Microcornea (HP:0000482), Shallow anterior chamber (HP:0000594), Iris hypoplasia / coloboma (HP:0000526), Cataract (HP:0000518), Optic nerve dysplasia (HP:0001093), Myopia (HP:0000545), Nanophthalmos / Microphthalmia (HP:0000568).
- **Evidence type:** Human clinical/genetic family studies.

### Finding 6 — ADVIRC is a rare autosomal dominant bestrophinopathy and a minority of BEST1-related retinal dystrophy

A population registry study by Sæther et al. (2026) of 60 *BEST1*-related retinal dystrophy (BEST1-RD) patients in Southern and Eastern Norway found: *"Forty-one patients were diagnosed with Best's vitelliform macular dystrophy (BVMD), 15 with autosomal recessive bestrophinopathy (ARB) and 4 with autosomal dominant vitreoretinochoroidopathy (ADVIRC)"* [PMID: 41627933](https://pubmed.ncbi.nlm.nih.gov/41627933/). ADVIRC was thus the rarest of the three classic bestrophinopathies (4/60; ~6.7%). The same study estimated overall BEST1-RD prevalence: *"The prevalence of BEST1-RD in Southern and Eastern Norway was between 1:64 600 and 1:43 700"* [PMID: 41627933](https://pubmed.ncbi.nlm.nih.gov/41627933/), noting *BEST1* as the third leading cause of inherited retinal dystrophy in Norway.

Inheritance is autosomal dominant (Blair 1984 [PMID: 6689931](https://pubmed.ncbi.nlm.nih.gov/6689931/); Yardley 2004 [PMID: 15452077](https://pubmed.ncbi.nlm.nih.gov/15452077/)), contrasting with the autosomal recessive inheritance of ARB.

- **Evidence type:** Population registry / epidemiology.

### Finding 7 — Integrated mechanism: splice-altering *BEST1* mutations produce a gain-of-function RPE channel that drives both developmental anomalies and progressive retinopathy

Synthesizing the above, the causal chain runs: (1) a heterozygous *BEST1* exonic splice-site variant (e.g., c.256G>A/p.V86M) causes simultaneous missense substitution and exon skipping, generating three bestrophin-1 isoforms (Yardley 2004 minigene assay, [PMID: 15452077](https://pubmed.ncbi.nlm.nih.gov/15452077/)); (2) the aberrant isoforms co-assemble into the homopentameric Ca²⁺-activated Cl⁻ channel (cryo-EM pentamer, Owji 2022 [PMID: 35789156](https://pubmed.ncbi.nlm.nih.gov/35789156/)); (3) conferring a gain-of-function effect (Ni 2026, [PMID: 41991505](https://pubmed.ncbi.nlm.nih.gov/41991505/)); which (4) branches into a **developmental arm** (nanophthalmos/myopia, microcornea, iris dysgenesis, cataract, angle-closure glaucoma — Vincent 2011 [PMID: 21072067](https://pubmed.ncbi.nlm.nih.gov/21072067/)) and a **degenerative arm** (RPE anion/Ca²⁺/fluid-transport dysfunction — iPSC-RPE models Singh 2013 [PMID: 23139242](https://pubmed.ncbi.nlm.nih.gov/23139242/), Li 2017 [PMID: 29063836](https://pubmed.ncbi.nlm.nih.gov/29063836/)) producing a reduced EOG Arden ratio (Roider 1997 [PMID: 9279944](https://pubmed.ncbi.nlm.nih.gov/9279944/)), the 360-degree peripheral pigmentary band with equatorial photoreceptor loss (Goldberg 1989 [PMID: 2516300](https://pubmed.ncbi.nlm.nih.gov/2516300/)), blood-retinal barrier breakdown, neovascularization, macular edema, and choroidal atrophy (Blair 1984 [PMID: 6689931](https://pubmed.ncbi.nlm.nih.gov/6689931/)). There is no environmental or infectious trigger; disease is germline and autosomal dominant.

---

## Section-by-Section Report

### 1. Disease Information

ADVIRC is a rare, slowly progressive, autosomal dominant inherited retinal dystrophy affecting the full thickness of the eye — vitreous, retina, RPE, and choroid — hence "vitreoretinochoroidopathy." Its causal gene is **BEST1** (bestrophin-1). The clinical hallmark is a circumferential 360-degree peripheral band of pigmentary retinopathy with a sharply demarcated posterior (equatorial) boundary, accompanied by fibrillar vitreous condensation, retinal vascular leakage, neovascularization, cystoid macular edema, choroidal atrophy, and developmental ocular anomalies.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0700240 |
| OMIM | 193220 (Vitreoretinochoroidopathy, VRCP / ADVIRC) |
| Gene (OMIM) | *BEST1* 607854 |
| HGNC | HGNC:1114 (*BEST1*) |
| Synonyms | ADVIRC; VRCP; vitreoretinochoroidopathy, autosomal dominant; BEST1-related vitreoretinochoroidopathy |
| ICD-11 | 9B70–9B71 range (hereditary retinal dystrophy, closest match) |
| MeSH | Closest: Retinal Dystrophies / Eye Diseases, Hereditary |

Information is derived from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual-patient** case series and family studies in the primary literature; there is no large EHR-derived dataset for this ultra-rare disease.

### 2. Etiology

**Causal factor:** Monogenic — heterozygous germline mutations in *BEST1* that disrupt exonic splice-regulatory elements, producing simultaneous missense substitution and exon skipping (Yardley 2004, [PMID: 15452077](https://pubmed.ncbi.nlm.nih.gov/15452077/)). No environmental or infectious cause is known.

**Genetic risk factors:** The causal variants themselves are the risk factor. Reported ADVIRC variants include V86M (c.256G>A), Y227N, V235A, p.V239M (c.715G>A), p.T277M (c.830C>T), and the splice variant c.1101-1G>T. These affect exonic splice enhancer/silencer sites.

**Environmental risk / protective factors:** None established. Because the disease is highly penetrant Mendelian with no known modifiers, environmental contributions are not a described feature. No protective alleles or lifestyle protective factors are documented.

**Gene–environment interactions:** None documented. The variable expressivity seen within families (same variant, different severity) suggests the influence of stochastic developmental factors or unidentified genetic modifiers rather than environment.

### 3. Phenotypes

| Phenotype | Type | Onset | Severity / Progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| 360° circumferential peripheral pigmentary band, discrete equatorial border | Clinical sign (pathognomonic) | Congenital/early, progressive | Slowly progressive–stationary | Near-universal | HP:0007703, HP:0007769 |
| Fibrillar vitreous condensation | Clinical sign | Early | Stable–progressive | Common | HP:0004327 |
| Reduced visual acuity / night blindness | Symptom | Childhood–adult | Variable (20/25 to NLP) | Variable | HP:0000572, HP:0000662 |
| Retinal vascular leakage / blood-retinal barrier breakdown | Clinical sign | Variable | Progressive | Common | HP:0000608 |
| Retinal neovascularization | Clinical sign | Later | Progressive | Subset | HP:0012808 |
| Cystoid macular edema | Clinical sign | Variable | Episodic/progressive | Subset | HP:0011505 |
| Choroidal atrophy | Clinical sign | Progressive | Progressive | Common | HP:0000533 |
| Myopia / increased axial length | Clinical sign | Early | Stable | Increased vs BVMD | HP:0000545 |
| Nanophthalmos / microcornea | Developmental | Congenital | Stable | Subset | HP:0000568, HP:0000482 |
| Iris dysgenesis | Developmental | Congenital | Stable | Subset | HP:0000526 |
| Cataract | Clinical sign | Variable | Progressive | Frequent (4/6 in V86M family) | HP:0000518 |
| Angle-closure glaucoma | Clinical sign | Adult | Progressive, vision-threatening | Subset | HP:0012109 |
| Optic nerve dysplasia | Developmental | Congenital | Stable | Rare | HP:0001093 |
| Reduced EOG Arden ratio | Laboratory/electrophysiology | Any | Stable | Characteristic | — |

**Quality of life impact:** ADVIRC causes progressive peripheral and (variably) central visual field loss, night blindness, and in severe cases blindness (no light perception), with substantial impact on mobility, driving, and independent daily functioning. Angle-closure glaucoma and cataract add acute vision-threatening and surgical burdens. No disease-specific EQ-5D/SF-36 data exist; impact is inferred from documented visual acuity ranges and progression (Vincent 2011, [PMID: 21072067](https://pubmed.ncbi.nlm.nih.gov/21072067/)).

### 4. Genetic / Molecular Information

**Causal gene:** *BEST1* (HGNC:1114; OMIM 607854; chromosome 11q12.3), encoding bestrophin-1.

**Pathogenic variants (ADVIRC-specific):**

| Variant (cDNA) | Protein | Type | Mechanism note |
|---|---|---|---|
| c.256G>A | p.V86M | Missense + splice | Classic ADVIRC; exonic splice element (Yardley 2004, Vincent 2011) |
| — | p.Y227N | Missense + splice | Yardley 2004 |
| — | p.V235A | Missense + splice | Yardley 2004 |
| c.715G>A | p.V239M | Missense + splice | da Palma 2021 |
| c.830C>T | p.T277M | Missense | Atypical/posterior ADVIRC (PMID 36712704) |
| c.1101-1G>T | splice acceptor | Splice | Mainguy 2024 |

**Variant classification:** Pathogenic / likely pathogenic per ACMG/AMP (co-segregation, functional splicing assay, recurrence). **Variant type:** predominantly missense variants that also disrupt splicing (dual consequence), plus canonical splice-site variants. **Functional consequence:** gain-of-function (Ni 2026, [PMID: 41991505](https://pubmed.ncbi.nlm.nih.gov/41991505/)) — distinct from the loss-of-function (ARB) and dominant-negative (BVMD) mechanisms of other bestrophinopathies. **Origin:** germline. **Allele frequency:** these are private/rare disease variants, essentially absent or ultra-rare in gnomAD.

**Modifier genes:** None confirmed; variable expressivity suggests undiscovered modifiers or stochastic factors.

**Epigenetic information / chromosomal abnormalities:** None reported; ADVIRC is a point-mutation/splice disorder without large structural rearrangements.

### 5. Environmental Information

No environmental, lifestyle, toxic, or infectious factors are implicated in ADVIRC. It is a purely Mendelian germline disorder. This section is **not applicable** beyond noting the absence of such contributions.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous *BEST1* exonic splice-regulatory variant** (e.g., c.256G>A/p.V86M) **results in** disruption of an exonic splice enhancer/silencer (Yardley 2004 — *demonstrated*).
2. This **leads to** simultaneous missense substitution **and** exon skipping during pre-mRNA splicing, **producing** three bestrophin-1 isoforms per cell: wild-type, missense, and in-frame-deletion (Yardley 2004 minigene assay — *demonstrated in vitro*).
3. The aberrant isoforms **co-assemble** into the **homopentameric** Ca²⁺-activated Cl⁻ channel (cryo-EM pentamer; Owji 2022 — *structural inference applied to ADVIRC*).
4. The mixed-subunit channel **confers a gain-of-function** effect on RPE anion/ion handling (Ni 2026 — *inferred from phenotype and comparative imaging*).
5. **Branch A — developmental arm:** altered RPE/ocular ion and fluid handling during eye development **leads to** nanophthalmos/myopia, microcornea, shallow anterior chamber, iris dysgenesis, cataract, optic nerve dysplasia, and predisposition to **angle-closure glaucoma** (Vincent 2011).
6. **Branch B — degenerative arm:** chronic RPE dysfunction (impaired Ca²⁺ signaling, anion transport, and fluid flux; impaired photoreceptor-outer-segment handling) **results in** RPE atrophy, equatorial photoreceptor loss, a reduced EOG light rise (lowered Arden ratio), the pathognomonic 360° pigmentary band, blood-retinal barrier breakdown, retinal neovascularization, cystoid macular edema, and choroidal atrophy (Goldberg 1989; Roider 1997; Blair 1984).

**Molecular pathways / biochemical defect:** The primary defect is in a **calcium-activated chloride channel** (bestrophin-1) governing RPE ionic homeostasis, transepithelial fluid transport, and the visual cycle (Wang 2026, [PMID: 42222334](https://pubmed.ncbi.nlm.nih.gov/42222334/)). iPSC-RPE models of *BEST1* disease demonstrate disrupted fluid flux, delayed rhodopsin/outer-segment degradation, altered calcium responses, and increased oxidative stress (Singh 2013, [PMID: 23139242](https://pubmed.ncbi.nlm.nih.gov/23139242/); Li 2017, [PMID: 29063836](https://pubmed.ncbi.nlm.nih.gov/29063836/)). Note: these functional models are largely of BVMD/ARB-type mutations; direct ADVIRC-isoform functional assays remain limited.

**Cellular processes:** RPE dysfunction, impaired phagocytosis/outer-segment turnover, oxidative stress, and secondary photoreceptor degeneration.

**Tissue damage mechanisms:** RPE atrophy, blood-retinal barrier breakdown with vascular leakage and neovascularization, choroidal atrophy, and vitreous fibrillar condensation.

- **GO (biological process) suggestions:** chloride transmembrane transport (GO:1902476), regulation of intracellular pH/ion homeostasis (GO:0006885), visual perception (GO:0007601), retinal pigment epithelium development (GO:0003406), response to oxidative stress (GO:0006979).
- **GO (cellular component):** basolateral plasma membrane (GO:0016323), endoplasmic reticulum (GO:0005783).
- **CL (cell type) suggestions:** retinal pigment epithelial cell (CL:0002586), retinal photoreceptor cell (rod CL:0000604, cone CL:0000573), Müller cell (CL:0000636).

### 7. Anatomical Structures Affected

- **Primary organ:** eye (UBERON:0000970), specifically the retina (UBERON:0000966), RPE (UBERON:0001782), choroid (UBERON:0001776), and vitreous body (UBERON:0001796).
- **Secondary involvement:** anterior segment — cornea (UBERON:0000964), iris (UBERON:0001769), lens (UBERON:0000965), anterior chamber/trabecular meshwork (angle-closure glaucoma); optic nerve (UBERON:0000941).
- **Body system:** visual/sensory system (nervous system, special sense organ).
- **Tissue/cell level:** epithelial (RPE), neural (photoreceptors, Müller glia), vascular endothelium (retinal vessels).
- **Subcellular level:** basolateral plasma membrane of RPE (GO:0016323); endoplasmic reticulum calcium stores implicated in *BEST1* function (Singh 2013).
- **Lateralization:** **bilateral**, generally symmetric; the peripheral band is circumferential (360°).

### 8. Temporal Development

- **Onset:** Congenital developmental anomalies (nanophthalmos, microcornea, iris dysgenesis) are present from birth; the pigmentary retinopathy and degenerative features are early-onset and progressive, often recognized in childhood to adulthood.
- **Onset pattern:** chronic, insidious.
- **Progression:** slowly progressive to stationary (Goldberg 1989, [PMID: 2516300](https://pubmed.ncbi.nlm.nih.gov/2516300/)); electrophysiology (ffERG) may decline from low-normal to non-recordable with age (Vincent 2011). Course is progressive but slow; disease is **chronic and lifelong**.
- **Variable expressivity:** marked, even within families carrying the same variant (da Palma 2021; Mainguy 2024).
- **Remission:** none; no spontaneous remission. **Critical periods:** eye development (for the congenital anomalies) and ongoing adult life for degenerative progression and glaucoma risk.

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant (contrast with autosomal recessive ARB).
- **Penetrance:** high/complete for genotype, but **highly variable expressivity**.
- **Epidemiology:** ultra-rare. In a Norwegian registry, ADVIRC accounted for only 4/60 BEST1-RD patients; overall BEST1-RD prevalence was estimated at **1:64,600 to 1:43,700** (Sæther 2026, [PMID: 41627933](https://pubmed.ncbi.nlm.nih.gov/41627933/)), making ADVIRC a small fraction of that — on the order of 1 in several hundred thousand to low millions.
- **Sex ratio:** no sex predilection reported (autosomal dominant).
- **Founder effects / consanguinity / anticipation / mosaicism:** none established; variants are typically private. No repeat-expansion mechanism, so genetic anticipation is not expected.
- **Carrier frequency:** not applicable (dominant; affected = carriers).

### 10. Diagnostics

- **Clinical examination:** dilated fundoscopy revealing the pathognomonic 360° peripheral pigmentary band with discrete equatorial boundary; fibrillar vitreous.
- **Imaging:** ultra-widefield fundus photography, fluorescein angiography (vascular leakage, neovascularization, barrier breakdown), OCT (photoreceptor/outer-segment thinning, macular edema), fundus autofluorescence.
- **Electrophysiology:** **Electrooculography (EOG)** showing reduced Arden ratio (reduced light rise) reflecting RPE dysfunction (Roider 1997, [PMID: 9279944](https://pubmed.ncbi.nlm.nih.gov/9279944/)); full-field ERG ranging from low-normal to non-recordable with age (note: EOG can occasionally be normal in bestrophinopathies — [PMID: 28590961](https://pubmed.ncbi.nlm.nih.gov/28590961/)).
- **Genetic testing (confirmatory):** targeted single-gene *BEST1* sequencing, inherited-retinal-dystrophy gene panels, or WES/WGS. Because pathogenic ADVIRC variants act on splicing, functional/minigene confirmation or in silico splice prediction strengthens classification.
- **Histopathology (research/autopsy):** disorganized peripheral retina, focal RPE atrophy, perivascular pigment migration, equatorial photoreceptor loss, preretinal Müller/vitreous membrane (Goldberg 1989).
- **Differential diagnosis:** familial exudative vitreoretinopathy, retinitis pigmentosa, other bestrophinopathies (BVMD, ARB), Wagner syndrome, and retinal vasculopathies. Distinguishing feature: the discrete 360° equatorial pigmentary band and *BEST1* genotype.

### 11. Outcome / Prognosis

- **Survival/mortality:** ADVIRC is **not life-limiting**; it is an ocular disorder. No disease-specific mortality.
- **Morbidity:** significant visual morbidity — progressive field loss, variable central vision loss (20/25 to no light perception), night blindness, and risk of blindness; secondary complications include angle-closure glaucoma, cataract, cystoid macular edema, neovascularization, and (rarely) retinal detachment.
- **Prognostic factors:** severity of developmental anomalies, presence of glaucoma/neovascularization, age (ffERG declines with age), and specific variant — though expressivity is highly variable.
- **Disease course:** slowly progressive, lifelong; bestrophinopathies generally show slow BCVA decline in the absence of CNV/glaucoma complications (natural-history data for the broader bestrophinopathy group, [PMID: 42559932](https://pubmed.ncbi.nlm.nih.gov/42559932/)).

### 12. Treatment

There is **no curative or disease-specific therapy**. Management is supportive and complication-directed:

- **Pharmacotherapy / interventional:** anti-VEGF intravitreal injections for choroidal neovascularization/macular edema; IOP-lowering medications and laser peripheral iridotomy/trabeculectomy for angle-closure glaucoma (as applied in bestrophinopathy cohorts, e.g., [PMID: 39048936](https://pubmed.ncbi.nlm.nih.gov/39048936/)).
- **Surgical:** cataract extraction; glaucoma surgery; vitrectomy/retinal detachment repair as needed.
- **Supportive/rehabilitative:** low-vision aids, occupational support, and genetic counseling.
- **Experimental / advanced therapeutics:** Because ADVIRC is **gain-of-function**, simple gene-supplementation (adding wild-type *BEST1*) is unlikely to help. The rational strategy is **allele-specific suppression** of the mutant transcript. Proof-of-concept exists: allele-specific CRISPR/Cas9 editing in hiPSC-RPE restored BEST1 localization, protein stability, and anion transport for selected dominant *BEST1* mutations ([PMID: 42010707](https://pubmed.ncbi.nlm.nih.gov/42010707/)). AAV-mediated *BEST1* delivery to RPE has been demonstrated in canine models (serotype-dependent; rAAV2/2 safe and RPE-specific, [PMID: 24143172](https://pubmed.ncbi.nlm.nih.gov/24143172/)), and broader gene-therapy strategies for bestrophinopathies are under review ([PMID: 41096689](https://pubmed.ncbi.nlm.nih.gov/41096689/)).
- **NCIT term suggestions:** Anti-VEGF Therapy, Laser Therapy (NCIT:C15262), Cataract Surgery, Gene Therapy (NCIT:C15431), Genetic Counseling (NCIT:C15417), Supportive Care (NCIT:C15227).

### 13. Prevention

- **Primary prevention:** not possible (germline Mendelian). **Genetic counseling** is central: autosomal dominant inheritance confers 50% transmission risk to offspring. **Preimplantation genetic diagnosis (PGD)** and **prenatal testing** are options once the family variant is known.
- **Secondary prevention:** early ophthalmologic surveillance in at-risk family members (cascade testing) to detect and treat angle-closure glaucoma, cataract, macular edema, and neovascularization early.
- **Tertiary prevention:** regular monitoring and timely intervention to preserve remaining vision (IOP control, anti-VEGF, surgery).
- **Immunization / public health / environmental interventions:** not applicable.

### 14. Other Species / Natural Disease

- **Orthologous gene / natural models:** *BEST1* has a canine ortholog, and naturally occurring **canine multifocal retinopathy (cmr)** is caused by *BEST1* mutations — a validated large-animal model of human bestrophinopathy (Guziewicz 2007, [PMID: 17460247](https://pubmed.ncbi.nlm.nih.gov/17460247/); cmr3, [PMID: 21197113](https://pubmed.ncbi.nlm.nih.gov/21197113/)). Canine bestrophinopathy recapitulates the focal/multifocal retina–RPE separations and underdeveloped RPE apical domain seen in human disease ([PMID: 29721958](https://pubmed.ncbi.nlm.nih.gov/29721958/)).
- **Taxonomy:** *Canis lupus familiaris* (NCBI:txid9615); affected breeds include mastiff-related breeds (cmr1), Coton de Tulear (cmr2), and Lapponian herder (cmr3).
- **Comparative biology:** cmr shares clinical and molecular features with human bestrophinopathies but reflects loss-of-function/mislocalization mechanisms — ADVIRC's specific gain-of-function splicing mechanism is **not** directly modeled by existing cmr dogs.
- **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms

| Model | Type | Use / Recapitulation | Reference |
|---|---|---|---|
| hiPSC-derived RPE (patient-specific) | In vitro / cellular | Disrupted fluid flux, delayed POS/rhodopsin degradation, altered Ca²⁺ responses, oxidative stress | [PMID: 23139242](https://pubmed.ncbi.nlm.nih.gov/23139242/), [PMID: 29063836](https://pubmed.ncbi.nlm.nih.gov/29063836/) |
| Canine multifocal retinopathy (cmr) | Mammalian (dog) | Natural *BEST1* model; retina–RPE separation, underdeveloped RPE apical domain | [PMID: 17460247](https://pubmed.ncbi.nlm.nih.gov/17460247/), [PMID: 29721958](https://pubmed.ncbi.nlm.nih.gov/29721958/) |
| Zebrafish *best1* | Vertebrate | Mutant mislocalization and retinal-integrity effects | [PMID: 41456629](https://pubmed.ncbi.nlm.nih.gov/41456629/) |
| MDCK II polarized epithelial cells | In vitro | Channel localization/function assays for *BEST1* mutants | [PMID: 41456629](https://pubmed.ncbi.nlm.nih.gov/41456629/) |

**Limitation of models:** No existing animal model carries an ADVIRC splicing/gain-of-function variant; most functional and animal work models BVMD/ARB (loss-of-function/dominant-negative) mechanisms. This is a key gap for ADVIRC-specific preclinical therapeutic testing.

---

## Mechanistic Model / Interpretation

```
 Heterozygous BEST1 exonic splice-regulatory variant (e.g. c.256G>A / p.V86M)
                               │  (demonstrated: minigene assay, Yardley 2004)
                               ▼
 Simultaneous MISSENSE substitution + EXON SKIPPING
   → 3 bestrophin-1 isoforms: wild-type | missense | in-frame deletion
                               │  (structural inference: pentamer, Owji 2022)
                               ▼
 Mixed-subunit co-assembly into homopentameric Ca²⁺-activated Cl⁻ channel
                               │  (inferred: Ni 2026)
                               ▼
              GAIN-OF-FUNCTION at the RPE basolateral membrane
                               │
          ┌────────────────────┴─────────────────────┐
          ▼ (Branch A: DEVELOPMENTAL)                 ▼ (Branch B: DEGENERATIVE)
  Nanophthalmos / myopia, microcornea,       RPE anion/Ca²⁺/fluid-transport
  shallow AC, iris dysgenesis, cataract,      dysfunction → RPE atrophy,
  optic nerve dysplasia                        ↓ EOG Arden ratio, equatorial
          │                                     photoreceptor loss
          ▼                                            │
  ANGLE-CLOSURE GLAUCOMA                               ▼
  (Vincent 2011)                             360° peripheral pigmentary band,
                                             blood-retinal barrier breakdown,
                                             neovascularization, macular edema,
                                             choroidal atrophy (Blair/Goldberg/Roider)
```

The defining conceptual point is that ADVIRC sits apart from the other two bestrophinopathies not by which gene is mutated but by **how** the channel is altered. BVMD arises from dominant-negative mutant subunits poisoning the pentamer; ARB arises from biallelic loss-of-function; ADVIRC arises from splice-altering variants that create a **gain-of-function** channel. This single mechanistic distinction accounts for ADVIRC's unique combination of **congenital developmental anomalies** (which the degenerative-only bestrophinopathies largely lack) plus a **progressive peripheral degeneration** with its signature circumferential band.

### Comparison of the three classic bestrophinopathies

| Feature | BVMD | ARB | **ADVIRC** |
|---|---|---|---|
| Inheritance | Autosomal dominant | Autosomal recessive | **Autosomal dominant** |
| Mechanism | Dominant-negative | Loss-of-function (biallelic) | **Gain-of-function (splice-altering)** |
| EOG Arden ratio | Reduced | Reduced | **Reduced** |
| Hallmark lesion | Central vitelliform ("egg-yolk") | Multifocal subretinal deposits | **360° peripheral pigmentary band** |
| Developmental anomalies | Rare | Angle-closure, hyperopia | **Prominent (nanophthalmos, iris dysgenesis, etc.)** |
| Relative frequency (Norway) | 41/60 | 15/60 | **4/60 (rarest)** |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [15452077](https://pubmed.ncbi.nlm.nih.gov/15452077/) | Mutations of VMD2 splicing regulators cause nanophthalmos and ADVIRC | **Foundational:** establishes splicing mechanism and causal gene |
| [41991505](https://pubmed.ncbi.nlm.nih.gov/41991505/) | Gain of function in BEST1: photoreceptor changes and myopia in ADVIRC | **Foundational:** gain-of-function mechanism + PR/refractive phenotype |
| [21072067](https://pubmed.ncbi.nlm.nih.gov/21072067/) | BEST1-related ADVIRC: developmental ocular anomalies | Developmental-arm phenotype; variable expressivity (p.V86M) |
| [6689931](https://pubmed.ncbi.nlm.nih.gov/6689931/) | ADVIRC (Blair 1984) | Pathognomonic 360° band; vascular/vitreous/choroidal features |
| [2516300](https://pubmed.ncbi.nlm.nih.gov/2516300/) | Histopathologic study of ADVIRC | Histopathology; circumferential pigmentary retinopathy |
| [9279944](https://pubmed.ncbi.nlm.nih.gov/9279944/) | ADVIRC (Roider 1997) | Independent family; reduced EOG Arden ratio |
| [17460247](https://pubmed.ncbi.nlm.nih.gov/17460247/) | Bestrophin mutations cause canine multifocal retinopathy | Protein size/localization; canine natural model |
| [42222334](https://pubmed.ncbi.nlm.nih.gov/42222334/) | From BEST1 mutations to retinal regeneration | Bestrophin-1 molecular function (CaCC, visual cycle) |
| [35789156](https://pubmed.ncbi.nlm.nih.gov/35789156/) | Structures and gating of human bestrophin channels | Homopentameric architecture (co-assembly basis) |
| [40043778](https://pubmed.ncbi.nlm.nih.gov/40043778/) | Cryo-EM of mouse BEST1 closed/partially open | Conformational states of the channel |
| [41627933](https://pubmed.ncbi.nlm.nih.gov/41627933/) | BEST1-associated dystrophies in Norway | Epidemiology; ADVIRC rarest (4/60); prevalence estimate |
| [34746433](https://pubmed.ncbi.nlm.nih.gov/34746433/) | Variable expressivity of ADVIRC (p.V239M) | Intra-familial variability with identical variant |
| [38957071](https://pubmed.ncbi.nlm.nih.gov/38957071/) | Variable expressivity, c.1101-1G>T | Novel splice variant; variable phenotype |
| [23139242](https://pubmed.ncbi.nlm.nih.gov/23139242/) | iPSC modeling of Best disease | RPE fluid flux, Ca²⁺, POS handling (degenerative arm) |
| [29063836](https://pubmed.ncbi.nlm.nih.gov/29063836/) | BEST1 mediates Ca²⁺-dependent function | Channel function in patient RPE |
| [42010707](https://pubmed.ncbi.nlm.nih.gov/42010707/) | Allele-specific CRISPR suppression of BEST1 | Rational therapy for dominant/GoF mutations |
| [24143172](https://pubmed.ncbi.nlm.nih.gov/24143172/) | rAAV-mediated BEST1 transfer to RPE | Gene-delivery feasibility (canine) |
| [42559932](https://pubmed.ncbi.nlm.nih.gov/42559932/) | Bestrophinopathies: natural history | Slow BCVA decline context (broader group) |

**Evidence source types used:** human clinical/genetic (family and case series, registry), in vitro (minigene splicing, iPSC-RPE, MDCK), structural biology (cryo-EM), and model organism (canine, zebrafish).

---

## Limitations and Knowledge Gaps

1. **No ADVIRC-specific functional/animal model.** Functional data (iPSC-RPE, canine cmr, zebrafish) overwhelmingly model BVMD/ARB loss-of-function or dominant-negative mutations. The ADVIRC gain-of-function splicing isoform mixture has **not** been directly characterized in a physiological channel-function assay, so "gain-of-function" is partly inferred from phenotype/imaging (Ni 2026) rather than from direct electrophysiology of the three co-assembled isoforms.
2. **Ultra-rarity limits epidemiology.** Prevalence is extrapolated from a single regional registry (Norway); global prevalence, geographic/ethnic distribution, and sex-specific data are essentially unknown.
3. **Variable expressivity is unexplained.** The same variant produces widely different severity within families, implying modifier genes or stochastic developmental factors that have not been identified.
4. **No disease-specific QoL instruments or natural-history cohort.** Prognostic estimates borrow from broader bestrophinopathy natural-history data.
5. **Mechanistic branch assignment partly inferred.** The precise reason splice-altering variants cause both developmental anomalies and degeneration (vs. degeneration alone) is not experimentally dissected.
6. **Variant spectrum is small.** Only a handful of ADVIRC variants are confirmed; genotype–phenotype correlation is underpowered.

---

## Proposed Follow-up Experiments / Actions

1. **Direct functional characterization of ADVIRC isoform mixtures.** Express the three bestrophin-1 isoforms (wild-type + missense + in-frame deletion) at physiological stoichiometry in iPSC-RPE or heterologous pentameric reconstitution and perform patch-clamp + anion-flux assays to confirm gain-of-function at the channel level and define the biophysical change (e.g., altered Ca²⁺ sensitivity, altered Cl⁻ conductance).
2. **Generate an ADVIRC-specific model.** Create a knock-in mouse or zebrafish carrying an exonic splice variant (e.g., p.V86M-equivalent) to test whether both the developmental (nanophthalmos/anterior-segment) and degenerative (peripheral band) arms are recapitulated — currently a major gap.
3. **Allele-specific knockdown as therapy.** Extend allele-specific CRISPR/Cas9 or ASO suppression ([PMID: 42010707](https://pubmed.ncbi.nlm.nih.gov/42010707/)) to ADVIRC splice variants in patient-derived iPSC-RPE and assess rescue of fluid flux, outer-segment handling, and channel function.
4. **Splice-correction approach.** Because the lesion is a splicing defect, test splice-switching ASOs or small molecules that restore normal exon inclusion, potentially eliminating the aberrant in-frame-deletion isoform.
5. **Modifier discovery.** Perform WGS + transcriptomics across multiple affected individuals sharing a variant but differing in severity to identify genetic/epigenetic modifiers of expressivity.
6. **Prospective natural-history registry.** Assemble a multicenter ADVIRC cohort with standardized ultra-widefield imaging, OCT, EOG/ffERG, and QoL instruments to define progression rates, prognostic biomarkers, and clinical-trial endpoints.
7. **Developmental-arm investigation.** Use ADVIRC iPSC-derived optic-vesicle/organoid systems to interrogate how the gain-of-function channel perturbs anterior-segment and axial-length development, linking the molecular defect to nanophthalmos and angle-closure glaucoma.

---

*Report compiled from 7 confirmed findings and 52 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature (PMID) with verbatim abstract quotes where available.*


## Artifacts

- [OpenScientist final report](BEST1-related_Vitreoretinochoroidopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](BEST1-related_Vitreoretinochoroidopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700240` (2 mentions) - the report calls it "MONDO"; MONDO calls it **BEST1-related vitreoretinochoroidopathy**
- `HP:0004327` (2 mentions) - the report calls it "Common"; HP calls it **Abnormal vitreous humor morphology**
- `HP:0000533` (2 mentions) - the report calls it "Common"; HP calls it **Chorioretinal atrophy**
- `HP:0012808` (2 mentions) - the report calls it "Subset"; HP calls it **Abnormal nasal base norphology**
- `HP:0012109` (2 mentions) - the report calls it "Subset"; HP calls it **Angle closure glaucoma**
- `HP:0000526` (2 mentions) - the report calls it "Subset"; HP calls it **Aniridia**
- `HP:0000518` (2 mentions) - the report calls it "Frequent (4/6 in V86M family)"; HP calls it **Cataract**
- `HP:0001093` (2 mentions) - the report calls it "Rare"; HP calls it **Optic nerve dysplasia**
- `HP:0000545` (2 mentions) - the report calls it "Increased vs BVMD"; HP calls it **Myopia**
- `HP:0000608` (1 mention) - the report calls it "Common"; HP calls it **Macular degeneration**
- `HP:0011505` (1 mention) - the report calls it "Subset"; HP calls it **Cystoid macular edema**
- `UBERON:0000970` (1 mention) - the report calls it "Primary organ:** eye"; UBERON calls it **eye**
- `UBERON:0000964` (1 mention) - the report calls it "Secondary involvement:** anterior segment — cornea"; UBERON calls it **cornea**
- `NCIT:C15262` (1 mention) - the report calls it "NCIT term suggestions:** Anti-VEGF Therapy, Laser Therapy"; NCIT calls it **Immunotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007703` (2 mentions) - the report calls it "HPO suggestions:** Abnormal retinal pigmentation"; HP calls it **Abnormal retinal pigmentation**
- `GO:0005254` (1 mention) - the report calls it "GO suggestions:** chloride channel activity"; GO calls it **chloride channel activity**
- `GO:0016323` (3 mentions) - the report calls it "Subcellular level:** basolateral plasma membrane of RPE"; GO calls it **basolateral plasma membrane**
- `CHEBI:17996` (1 mention) - the report calls it "CHEBI:** chloride"; CHEBI calls it **chloride**