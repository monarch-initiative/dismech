---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T01:27:04.152980'
end_time: '2026-10-24T01:41:18.588539'
duration_seconds: 854.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Blepharocheilodontic Syndrome 1
  mondo_id: MONDO:0054740
  category: Mendelian
  causal_genes: CDH1
  omim_id: not recorded
  synonyms: BCDS1; blepharo-cheilo-dontic syndrome 1; CDH1-related blepharocheilodontic
    syndrome; Elschnig syndrome
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 19
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:11476703
  - PMID:26123647
  relevance_assessed: 27
  on_topic: 14
  off_topic: 2
  off_topic_references:
  - PMID:38132417
  - PMID:25010141
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0000656
    reported_labels:
    - Clinical sign
    ontology_label: Ectropion
  - term_id: HP:0100660
    reported_labels:
    - Physical malformation
    ontology_label: Dyskinesia
  - term_id: HP:0100698
    reported_labels:
    - Clinical sign
    ontology_label: Subcutaneous neurofibroma
  - term_id: HP:0002225
    reported_labels:
    - Physical malformation
    ontology_label: Sparse pubic hair
  - term_id: HP:0000677
    reported_labels:
    - Dental abnormality
    ontology_label: Oligodontia
  - term_id: HP:0000698
    reported_labels:
    - Dental abnormality
    ontology_label: Conical tooth
  - term_id: HP:0000679
    reported_labels:
    - Dental abnormality
    ontology_label: Taurodontia
  - term_id: HP:0000689
    reported_labels:
    - Physical
    ontology_label: Dental malocclusion
  - term_id: HP:0000968
    reported_labels:
    - Physical
    ontology_label: Ectodermal dysplasia
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
  path: Blepharocheilodontic_Syndrome_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Blepharocheilodontic_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blepharocheilodontic Syndrome 1
- **MONDO ID:** MONDO:0054740 (if available)
- **Causal gene(s):** CDH1
- **OMIM:** not recorded
- **Synonyms:** BCDS1; blepharo-cheilo-dontic syndrome 1; CDH1-related blepharocheilodontic syndrome; Elschnig syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Blepharocheilodontic Syndrome 1** covering all of the
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

# Blepharocheilodontic Syndrome 1 (BCDS1): A Comprehensive Disease Characteristics Report

**Disease:** Blepharocheilodontic Syndrome 1 (BCDS1)
**MONDO ID:** MONDO:0054740
**OMIM:** #119580
**Orphanet:** ORPHA:1997
**Causal gene:** **CDH1** (E-cadherin; HGNC:1748; NCBI Gene 999)
**Synonyms:** BCDS1; blepharo-cheilo-dontic syndrome 1; CDH1-related blepharocheilodontic syndrome; Elschnig syndrome
**Category:** Mendelian, autosomal dominant

---

## Summary

Blepharocheilodontic syndrome 1 (BCDS1) is an ultra-rare, congenital, autosomal dominant malformation syndrome caused by **heterozygous pathogenic variants in CDH1**, the gene encoding the epithelial cell–adhesion molecule **E-cadherin**. The syndrome is defined by a clinical triad of (1) eyelid malformations (lagophthalmos, ectropion of the lower eyelids, euryblepharon, distichiasis), (2) cleft lip and/or cleft palate, and (3) dental anomalies, most notably oligodontia with conical teeth and incisal notching. BCDS1 is the CDH1-related form of the disorder; a closely related second type, BCDS2, is caused by truncating variants in CTNND1 (encoding p120-catenin), the direct binding partner of E-cadherin, and together the two genes define a single "cadherin–catenin complex" developmental disorder.

The core mechanism is dysfunction of the **E-cadherin–p120-catenin adherens-junction complex**. Unlike the loss-of-function CDH1 variants that drive hereditary diffuse gastric cancer (HDGC), the missense CDH1 variants found in BCDS1 act largely in a **dominant-negative** manner, impairing the adhesion function of the cadherin–catenin complex during the morphogenesis of the eyelids, lip/palate, and teeth. Functional studies in zebrafish, mouse (conditional Cdh1/Ctnnd1 deletion; Ctnnd1 knockout), and Xenopus recapitulate features of the syndrome and confirm the central role of E-cadherin–p120-catenin interaction in craniofacial development. Because E-cadherin sequesters β-catenin at the cell membrane, its dysfunction also links the disorder to Wnt signaling and epithelial-to-mesenchymal transition (EMT) control, though the precise downstream developmental cascade in human tissue is largely inferred.

Clinically, BCDS1 features are **structural, congenital, and non-progressive**, with normal life expectancy; management is entirely **symptomatic and multidisciplinary** — eyelid reconstructive surgery, cleft lip/palate repair, and prosthodontic/orthodontic dental rehabilitation. A clinically important and still-contested nuance is a **variant-dependent cancer risk**: at least one BCDS family developed diffuse gastric cancer from a germline CDH1 variant, while the recurrent c.760G>A (p.Asp254Asn) orofacial-cleft allele has been shown NOT to predispose to hereditary cancer. This mandates variant-specific genetic counseling, with consideration of International Gastric Cancer Linkage Consortium (IGCLC) surveillance protocols for families carrying HDGC-class alleles.

---

## Key Findings

### Finding 1 — BCDS1 is caused by heterozygous, dominant-negative CDH1 variants

BCDS1 results from heterozygous pathogenic variants in **CDH1 (E-cadherin)**. In the defining molecular cohorts, heterozygous CDH1/CTNND1 variants were identified in 15 of 17 BCDS index patients ([PMID: 29348693](https://pubmed.ncbi.nlm.nih.gov/29348693/)), and an earlier study found five CDH1 heterozygous missense mutations plus three CTNND1 truncating mutations across 11 patients from 8 families ([PMID: 28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/)). Critically, functional experiments established that the CDH1 variants in BCDS do not behave like classic cancer-associated loss-of-function alleles:

> "Functional experiments in zebrafish and human cells showed that the CDH1 variants impair the cell adhesion function of the cadherin-catenin complex in a dominant-negative manner. Variants in CDH1 have been linked to familial hereditary diffuse gastric cancer and invasive lobular breast cancer; however, no cases of gastric or breast cancer have been reported in our BCDS cases." ([PMID: 29348693](https://pubmed.ncbi.nlm.nih.gov/29348693/))

The two distinct variant classes — **CDH1 missense** (dominant-negative) and **CTNND1 truncating** (loss-of-function/haploinsufficiency) — both converge on the same adhesion complex:

> "We identified five CDH1 heterozygous missense mutations and three CTNND1 heterozygous truncating mutations leading to loss-of-function or haploinsufficiency." ([PMID: 28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/))

Additional pathogenic CDH1 missense alleles have since broadened the spectrum, e.g., c.1198G>A (p.Asp400Asn) located in the extracellular cadherin-type repeats, co-segregating in a Chinese BCD family and classified likely pathogenic under ACMG criteria ([PMID: 36552944](https://pubmed.ncbi.nlm.nih.gov/36552944/)).

### Finding 2 — The clinical triad: eyelid malformations, cleft lip/palate, and dental anomalies

BCDS is defined by a recognizable triad:

> "Blepharocheilodontic syndrome (BCDS) consists of lagophthalmia, ectropion of the lower eyelids, distichiasis, euryblepharon, cleft lip/palate and dental anomalies and has autosomal dominant inheritance with variable expression." ([PMID: 29348693](https://pubmed.ncbi.nlm.nih.gov/29348693/))

The **dental phenotype** is severe and quantified: in a dedicated craniofacial/dental study, all patients exhibited oligodontia with a mean of 13.7 missing permanent teeth (range 7–17), severe skeletal Class III malocclusion (vs controls, P = 0.001), reduced anterior lower face height (P = 0.027), taurodontism, conical teeth, and incisal notching ([PMID: 28181393](https://pubmed.ncbi.nlm.nih.gov/28181393/)):

> "All patients exhibited oligodontia (mean number of missing permanent teeth 13.7, range 7-17)" ([PMID: 28181393](https://pubmed.ncbi.nlm.nih.gov/28181393/))

The **periocular phenotype** (lower lid ectropion, euryblepharon, lagophthalmos) is often functionally significant and surgically demanding ([PMID: 39442179](https://pubmed.ncbi.nlm.nih.gov/39442179/)). BCDS overlaps clinically with isolated lagophthalmos syndrome, supporting a phenotypic continuum ([PMID: 15930907](https://pubmed.ncbi.nlm.nih.gov/15930907/)). Oligodontia also places BCDS within a broader differential of oligodontia-associated syndromes alongside hypohidrotic ectodermal dysplasia, Axenfeld-Rieger, Witkop, Ellis-van Creveld, and oculofaciocardiodental syndromes ([PMID: 38132417](https://pubmed.ncbi.nlm.nih.gov/38132417/)).

### Finding 3 — Gastric cancer risk is variant-dependent and remains contested

The initial BCDS reports argued that BCD CDH1 variants are a distinct, non-oncogenic class, having observed no gastric or breast cancer among patients ([PMID: 29348693](https://pubmed.ncbi.nlm.nih.gov/29348693/); [PMID: 28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/)). This picture was complicated by subsequent reports:

> "We report the first case of diffuse gastric cancer in an individual with familial blepharocheilodontic syndrome (BCD) due to a germline CDH1 likely pathogenic variant." ([PMID: 32302040](https://pubmed.ncbi.nlm.nih.gov/32302040/))

This cancer risk was reinforced in a confirmatory follow-up ([PMID: 32483297](https://pubmed.ncbi.nlm.nih.gov/32483297/)). Conversely, a focused study of the recurrent cleft allele found no cancer predisposition:

> "The Recurrent E-Cadherin (CDH1) Mutation c.760G>A Causes Orofacial Clefts but Does Not Predispose to Hereditary Cancer" ([PMID: 39596675](https://pubmed.ncbi.nlm.nih.gov/39596675/))

**Interpretation:** cancer risk in CDH1-BCDS is not uniform and must be assessed at the level of the specific variant, not the syndrome label.

### Finding 4 — E-cadherin–p120-catenin adhesion dysfunction underlies BCDS; animal models recapitulate features

The mechanistic centerpiece is the physical interaction between E-cadherin and p120-catenin (CTNND1). Conditional genetic ablation of either partner reproduces the phenotype:

> "Conditional deletion of Cdh1 and Ctnnd1 in various animal models induces features reminiscent of BCD syndrome and underlines critical role of the E-cadherin-p120ctn interaction in eyelid, craniofacial, and tooth development." ([PMID: 28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/))

CDH1 missense mutations caused accelerated E-cadherin degradation, and Ctnnd1 knockout mice recapitulate the cleft lip/palate (CL/P) spectrum, with the genes enriched in embryonic oro-palatal epithelia ([PMID: 29805042](https://pubmed.ncbi.nlm.nih.gov/29805042/)):

> "recapitulation of the CL/P spectrum in Ctnnd1 knockout mice support a causative role in CL/P pathogenesis" ([PMID: 29805042](https://pubmed.ncbi.nlm.nih.gov/29805042/))

Complementary work linked p120-catenin to epithelial integrity/turnover and mesenchymal roles via conditional Ctnnd1 deletion in mice and CRISPR/Cas9 targeting in Xenopus ([PMID: 32196547](https://pubmed.ncbi.nlm.nih.gov/32196547/)).

### Finding 5 — The CTNND1 (BCDS2) phenotype is expanding beyond the classic triad

While BCDS1 (CDH1) typically presents the classic triad, the CTNND1-related form (BCDS2) carries a broader, multi-system phenotype:

> "presenting with craniofacial dysmorphisms including cleft palate and hypodontia, as well as congenital cardiac anomalies, limb dysmorphologies and neurodevelopmental disorders" ([PMID: 32196547](https://pubmed.ncbi.nlm.nih.gov/32196547/))

Eight novel protein-truncating CTNND1 variants (6 de novo) were found in 13 participants from 9 families, prompting the proposal of a "broader velocardiofacial-like syndrome." Newer reports add genitourinary anomalies:

> "the patient exhibited a duplex kidney, ureterocele, and a bicornuate uterus-phenotypic traits not previously associated with BCD syndrome" ([PMID: 40028877](https://pubmed.ncbi.nlm.nih.gov/40028877/))

Prenatal CTNND1 cases have described hydrocephalus and major fetal cardiac malformations ([PMID: 39487033](https://pubmed.ncbi.nlm.nih.gov/39487033/); [PMID: 37274823](https://pubmed.ncbi.nlm.nih.gov/37274823/)), and a Chinese pedigree documented a novel c.83delG (p.A29Rfs*55) CTNND1 variant in non-simplex BCDS ([PMID: 36584998](https://pubmed.ncbi.nlm.nih.gov/36584998/)).

### Finding 6 — E-cadherin, β-catenin sequestration, Wnt signaling, and EMT

E-cadherin is a transmembrane glycoprotein forming adherens junctions; its best-characterized downstream link is sequestration of β-catenin, connecting the BCDS lesion to Wnt signaling and EMT:

> "In normal cells, E-cadherin exerts its tumour suppressing role mainly by sequestering β-catenin from its binding to LEF (Lymphoid enhancer factor)/TCF (T cell factor) which serves the function of transcribing genes of the proliferative Wnt signaling pathway." ([PMID: 29279096](https://pubmed.ncbi.nlm.nih.gov/29279096/))

> "loss of E-cadherin releases β-catenin from the cell membrane and leads to its degradation" ([PMID: 31804558](https://pubmed.ncbi.nlm.nih.gov/31804558/))

In developmental morphogenesis, regulated downregulation of E-cadherin at adherens junctions is required for epithelial placode budding (e.g., hair follicle), mechanistically analogous to the epithelial remodeling needed in facial/eyelid/tooth morphogenesis ([PMID: 25010141](https://pubmed.ncbi.nlm.nih.gov/25010141/)). Note: in BCDS, the β-catenin/Wnt connection is **mechanistically plausible and inferred** from E-cadherin biology rather than directly demonstrated in affected craniofacial tissue.

### Finding 7 — Management is symptomatic and multidisciplinary

There is no disease-modifying therapy; care targets the structural manifestations:

> "Lateral tarsal strips, lower eyelid retractor disinsertion, myocutaneous advancement of the cheek and eyelids, and lateral tarsorrhaphy were performed. Correction of the ectropion, eyelid retraction, euryblepharon, and marked improvement in his lagophthalmos were achieved postoperatively." ([PMID: 11476703](https://pubmed.ncbi.nlm.nih.gov/11476703/))

> "Multiple surgical procedures including lateral canthoplasty, tarsorrhaphy, and midface augmentation may be necessary for correction of eyelid malposition and achieving cosmetic and functional improvements." ([PMID: 39442179](https://pubmed.ncbi.nlm.nih.gov/39442179/))

Dental rehabilitation of oligodontia uses prosthodontic/orthodontic approaches including overdentures in skeletal Class III patients ([PMID: 20073547](https://pubmed.ncbi.nlm.nih.gov/20073547/)), and euryblepharon with nocturnal eyelid eversion may require surgical correction ([PMID: 15220581](https://pubmed.ncbi.nlm.nih.gov/15220581/)).

### Finding 8 — CDH1 allelic series with incomplete penetrance

CDH1 displays an allelic series spanning BCDS, nonsyndromic orofacial clefting, and HDGC. In nonsyndromic cleft lip/palate:

> "three probably pathogenic variants (c.760G>A [p.Asp254Asn], c.1023T>G [p.Tyr341*], and c.2351G>A [p.Arg784His]) segregated according to autosomal dominant inheritance in four nonsyndromic cleft lip with or without cleft palate (NSCL/P) families (Lod score: 5.8 at θ = 0; 47% penetrance)" ([PMID: 26123647](https://pubmed.ncbi.nlm.nih.gov/26123647/))

> "CDH1 contributes to NSCL/P with mainly rare, moderately penetrant variants, and CDH1 haploinsufficiency is the likely etiological mechanism" ([PMID: 26123647](https://pubmed.ncbi.nlm.nih.gov/26123647/))

Inheritance is autosomal dominant with variable expression, and many BCDS cases are de novo. The recurrent c.760G>A/p.Asp254Asn allele appears across both nonsyndromic cleft families and the BCDS spectrum and is the one shown not to predispose to cancer.

### Finding 9 — Epidemiology, onset, and course

BCDS is described consistently as a "rare autosomal dominant condition" ([PMID: 28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/)), with fewer than ~100 reported cases, the largest molecular cohorts comprising 17 and 11 index patients. Orphanet (ORPHA:1997) assigns a prevalence of <1/1,000,000. Malformations are congenital/present at birth and detectable prenatally:

> "This case report describes the prenatal diagnosis of the extremely rare Blepharo-Cheilo-Dontic syndrome." ([PMID: 41563506](https://pubmed.ncbi.nlm.nih.gov/41563506/))

Features are structural and static rather than progressive, and life expectancy is normal (absent HDGC-class cancer risk).

### Finding 10 — Comparative biology and conservation

CDH1 (human; NCBI Gene 999; HGNC:1748) has deeply conserved orthologs: mouse Cdh1 (NCBI Gene 12550), zebrafish cdh1, and Xenopus. BCDS modeling has used zebrafish (dominant-negative CDH1), mouse conditional Cdh1/Ctnnd1 deletions, Ctnnd1 knockout mice (CL/P), and Xenopus CRISPR/Cas9 CTNND1 targeting. In veterinary genetics, CTNND1 was investigated as a positional candidate for congenital entropion in Swiss White Alpine sheep, but the identified variant was deemed unlikely causal:

> "Pathogenic variants in human CTNND1 cause blepharocheilodontic syndrome 2, a rare disorder including eyelid anomalies" ([PMID: 31945208](https://pubmed.ncbi.nlm.nih.gov/31945208/))

### Finding 11 — CDH1 cancer-risk management (IGCLC) for HDGC-class variants

For germline CDH1 pathogenic variants in the HDGC context, cumulative diffuse gastric cancer incidence is ~40% by age 80 and lobular breast cancer ~55% in women ([PMID: 36700973](https://pubmed.ncbi.nlm.nih.gov/36700973/)):

> "Those affected show an incidence of gastric cancer of around 40% up to the age of 80 years and affected women show an incidence of 55% for the occurrence of lobular breast cancer." ([PMID: 36700973](https://pubmed.ncbi.nlm.nih.gov/36700973/))

The 2020 IGCLC guidelines provide management options directly applicable to BCDS families carrying HDGC-class CDH1 alleles:

> "Prophylactic total gastrectomy remains the recommended option for gastric cancer risk management in pathogenic CDH1 variant carriers. However, there is increasing confidence from the IGCLC that endoscopic surveillance in expert centres can be safely offered to patients who wish to postpone surgery" ([PMID: 32758476](https://pubmed.ncbi.nlm.nih.gov/32758476/))

---

## Report by Template Section

### 1. Disease Information
BCDS1 is an ultra-rare autosomal dominant congenital malformation syndrome affecting eyelid, lip/palate, and dental development, caused by CDH1 variants. **Identifiers:** MONDO:0054740; OMIM #119580; Orphanet ORPHA:1997; related type BCDS2 (CTNND1). **Synonyms:** BCDS1, blepharo-cheilo-dontic syndrome 1, CDH1-related blepharocheilodontic syndrome, Elschnig syndrome. Information is derived from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual patient case reports/series** (the condition is too rare for registry-scale EHR data).

### 2. Etiology
**Primary cause:** genetic — heterozygous pathogenic CDH1 variants (BCDS1); CTNND1 truncating variants (BCDS2). **Genetic risk factors:** the causal variant itself (dominant); modifier background explains variable expression. **Environmental risk/protective factors:** none established — this is a Mendelian structural malformation syndrome. **Gene–environment interactions:** none documented. No infectious, toxic, or lifestyle contributors are known.

### 3. Phenotypes
Core phenotypes (congenital; physical manifestations/clinical signs; mostly stable/non-progressive):

| Phenotype | Type | Suggested HPO | Frequency |
|---|---|---|---|
| Lower eyelid ectropion | Clinical sign | HP:0000656 | Common/defining |
| Euryblepharon | Physical malformation | HP:0100660 | Common |
| Lagophthalmos | Clinical sign | HP:0100698 | Common |
| Distichiasis | Physical malformation | HP:0002225 | Frequent |
| Cleft lip / cleft palate | Physical malformation | HP:0410030 / HP:0000175 | Defining |
| Oligodontia | Dental abnormality | HP:0000677 | Near-universal (mean 13.7 missing teeth) |
| Conical/tapered teeth | Dental abnormality | HP:0000698 | Frequent |
| Taurodontism | Dental abnormality | HP:0000679 | Reported |
| Dental malocclusion (Class III) | Physical | HP:0000689 | P=0.001 vs controls |
| Ectodermal dysplasia features | Physical | HP:0000968 | Reported |

**Quality-of-life impact:** functional (ocular surface exposure/keratopathy risk from lagophthalmos; feeding/speech from cleft; mastication/esthetics from oligodontia) and psychosocial (facial dysmorphism). CTNND1/BCDS2 may add cardiac, limb, neurodevelopmental, and genitourinary burden.

### 4. Genetic/Molecular Information
**Causal gene:** CDH1 (16q22.1; HGNC:1748; NCBI Gene 999; OMIM *192090). **Variant types:** predominantly **missense** in the extracellular cadherin repeats (e.g., p.Asp254Asn/c.760G>A; p.Asp400Asn/c.1198G>A), acting **dominant-negatively**; CTNND1 variants are **truncating** (LoF/haploinsufficiency). **Classification:** pathogenic/likely pathogenic per ACMG/AMP. **Allele frequency:** BCDS alleles are rare/absent in gnomAD. **Origin:** germline; frequently de novo. **Functional consequence:** dominant-negative destabilization of the cadherin–catenin adhesion complex and accelerated E-cadherin degradation (for some missense alleles). **Modifier genes:** CTNND1 and the shared complex explain genetic heterogeneity; specific modifiers of expressivity are undefined. **Epigenetics / chromosomal abnormalities:** not a feature of CDH1-BCDS (incidental 17q12 microdeletion in one complex pedigree is unrelated to BCDS causation).

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established or expected for this Mendelian disorder.

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous **CDH1 missense variant** (germline) produces a mutant E-cadherin that **leads to** a dominant-negative protein incorporated into adherens junctions (and, for some alleles, accelerated E-cadherin degradation). *(Demonstrated in zebrafish/human cells.)*
2. This **results in** destabilization of the **E-cadherin–p120-catenin (CTNND1) adhesion complex** and impaired epithelial cell–cell adhesion. *(Demonstrated.)*
3. Impaired adhesion in cranial epithelia **leads to** defective epithelial integrity, turnover, and morphogenetic remodeling (budding/fusion) in the developing **eyelid, lip/palatal shelves, and dental lamina**. *(Supported by conditional Cdh1/Ctnnd1 deletion and Ctnnd1-KO animal models.)*
4. In parallel/branch, loss of membrane E-cadherin **releases β-catenin**, perturbing Wnt signaling and EMT balance required for epithelial placode budding and fusion. *(Inferred from E-cadherin biology; not directly shown in affected human craniofacial tissue.)*
5. These developmental failures **result in** the clinical triad: eyelid malformations (failed lid morphogenesis), cleft lip/palate (failed shelf fusion), and oligodontia/tooth-shape anomalies (disrupted odontogenesis). *(Observed clinically.)*

```
CDH1 missense variant (dominant-negative)
        │
        ▼
Destabilized E-cadherin–p120-catenin adherens junction ──► accelerated E-cadherin degradation
        │
        ▼
Impaired epithelial adhesion / remodeling in cranial epithelia
        │                         │
        ▼                         ▼
β-catenin release →          Failed morphogenesis of
Wnt/EMT dysregulation        eyelid / lip-palate / dental lamina
(inferred)                        │
        └──────────┬──────────────┘
                   ▼
   Eyelid malformations · Cleft lip/palate · Oligodontia (BCDS triad)
```

**Pathways/processes (GO):** cell–cell adhesion (GO:0098609), adherens junction organization (GO:0034332), canonical Wnt signaling (GO:0060070), EMT (GO:0001837), odontogenesis (GO:0042476), palate development (GO:0060021), eyelid development in camera-type eye (GO:0061029). **Cell types (CL):** epithelial cell (CL:0000066), odontogenic/oral epithelial cell, periderm. **Subcellular (GO CC):** adherens junction (GO:0005912), plasma membrane (GO:0005886), catenin complex (GO:0016342).

### 7. Anatomical Structures Affected
**Organ level:** eyelids (UBERON:0000158), lip (UBERON:0001833), palate (UBERON:0001716), teeth (UBERON:0001091). **Body systems:** integumentary/ectodermal, craniofacial skeleton, visual adnexa. BCDS2 (CTNND1) secondarily involves heart (UBERON:0000948), limbs, kidney/urinary tract (duplex kidney; ureterocele), uterus, and CNS. **Tissue/cell:** epithelial tissue (adherens-junction-dependent), oro-palatal and dental-lamina epithelium. **Laterality:** clefts and eyelid anomalies may be unilateral or bilateral/asymmetric.

### 8. Temporal Development
**Onset:** congenital; prenatally detectable. **Pattern:** static structural malformation — non-progressive. **Critical period:** embryonic craniofacial morphogenesis (facial-shelf fusion, eyelid formation, odontogenesis). **Duration:** lifelong structural features; no spontaneous remission; outcomes depend on surgical/dental correction. HDGC-class cancer risk, when present, has adult-onset age-dependent penetrance.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant, variable expressivity, frequently de novo. **Penetrance:** incomplete (~47% for CDH1-related clefting in NSCL/P families; nonpenetrant carriers reported). **Prevalence:** <1/1,000,000 (Orphanet); <~100 published cases. **Sex ratio:** no strong skew reported. **Founder/consanguinity:** not prominent; recurrent c.760G>A allele noted across families. **Carrier frequency:** not applicable (dominant).

### 10. Diagnostics
**Clinical:** recognition of the triad on physical/ophthalmologic/dental exam; dental panoramic radiography quantifies oligodontia and taurodontism. **Genetic testing (confirmatory):** single-gene CDH1 testing, multigene cleft/ectodermal panels, or WES/WGS; CTNND1 testing for BCDS2; Sanger confirmation and segregation analysis. Prenatal diagnosis is feasible via molecular testing and reverse phenotyping on fetal ultrasound. **Differential diagnosis:** isolated lagophthalmos syndrome (continuum), other oligodontia syndromes (hypohidrotic ectodermal dysplasia, Axenfeld-Rieger, Witkop, Ellis-van Creveld, oculofaciocardiodental), nonsyndromic CL/P. **Screening:** cascade genetic testing of at-risk relatives; for HDGC-class CDH1 alleles, consider upper-GI endoscopic surveillance and breast MRI (see §12).

### 11. Outcome/Prognosis
**Survival/life expectancy:** normal in the absence of HDGC-class cancer risk. **Morbidity:** functional (ocular exposure/keratopathy; feeding/speech from cleft; mastication/esthetics from oligodontia) and psychosocial. **Complications:** corneal exposure from lagophthalmos; cleft-related feeding/speech/ENT sequelae; in BCDS2, cardiac/neurodevelopmental morbidity. **Prognostic factors:** specific CDH1 variant (cancer risk), severity/extent of malformation, access to multidisciplinary surgical/dental care.

### 12. Treatment
No disease-modifying therapy exists; care is **symptomatic and multidisciplinary** (NCIT concepts: surgical procedure; oculoplastic/eyelid reconstruction; cleft lip/palate repair; dental prosthesis/overdenture; orthodontic therapy; supportive care).
- **Eyelid:** lateral tarsal strips, lower-lid retractor disinsertion, myocutaneous cheek/eyelid advancement, lateral tarsorrhaphy, lateral canthoplasty, midface augmentation; lubrication for lagophthalmos.
- **Cleft:** staged surgical repair; speech therapy; ENT/audiology.
- **Dental:** prosthodontic rehabilitation (overdentures, implants when appropriate); orthodontics for Class III malocclusion.
- **Cancer-risk management (variant-specific, HDGC-class alleles only):** per IGCLC — prophylactic total gastrectomy or expert-center endoscopic surveillance; annual breast MRI from age 30 in women.
No pharmacotherapy, gene therapy, RNA therapy, or immunotherapy is indicated for the malformation syndrome itself.

### 13. Prevention
**Primary prevention:** not possible (Mendelian). **Genetic counseling** is central: autosomal dominant 50% transmission risk, de novo possibility, incomplete penetrance/variable expressivity, and variant-specific cancer counseling. **Reproductive options:** prenatal diagnosis and preimplantation genetic testing for known familial variants. **Secondary/tertiary prevention:** early surgical/dental intervention to limit functional complications; for HDGC-class alleles, cancer surveillance/prophylaxis. **Cascade screening** of relatives.

### 14. Other Species / Natural Disease
Human CDH1 (NCBI Gene 999) is orthologous to mouse Cdh1 (NCBI Gene 12550), zebrafish cdh1, and Xenopus cadherin. CTNND1 was explored as a candidate for **congenital entropion in Swiss White Alpine sheep**, though the specific variant was judged unlikely causal ([PMID: 31945208](https://pubmed.ncbi.nlm.nih.gov/31945208/)). The cadherin–catenin complex is deeply evolutionarily conserved, underpinning cross-species modeling. No established naturally occurring BCDS-equivalent companion-animal disease is catalogued; no zoonotic relevance.

### 15. Model Organisms
- **Zebrafish:** dominant-negative CDH1 expression reproduces adhesion defects ([PMID: 29348693](https://pubmed.ncbi.nlm.nih.gov/29348693/)).
- **Mouse:** conditional Cdh1 and Ctnnd1 deletions induce BCD-reminiscent features ([PMID: 28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/)); Ctnnd1 knockout recapitulates the CL/P spectrum ([PMID: 29805042](https://pubmed.ncbi.nlm.nih.gov/29805042/)).
- **Xenopus:** CRISPR/Cas9 CTNND1 targeting links p120-catenin to epithelial/mesenchymal craniofacial roles ([PMID: 32196547](https://pubmed.ncbi.nlm.nih.gov/32196547/)).
- **In vitro:** human cell adhesion assays demonstrate dominant-negative effects.

**Phenotype recapitulation:** cleft lip/palate and craniofacial features are well-reproduced in Ctnnd1-KO mice; adhesion-complex dysfunction is reproduced in zebrafish/cells. **Limitations:** the full human triad (particularly the eyelid and oligodontia spectrum) is not completely recapitulated in any single model; most models use conditional/complete LoF rather than the human dominant-negative missense mechanism.

---

## Mechanistic Model / Interpretation

BCDS1 is best understood as a **disorder of the epithelial adherens junction** during craniofacial morphogenesis. The unifying lesion is destabilization of the **E-cadherin–p120-catenin complex**, reachable by two genetic routes: dominant-negative CDH1 missense alleles (BCDS1) or truncating CTNND1 alleles (BCDS2). The convergence of two genes encoding direct binding partners onto one clinical phenotype is the strongest evidence that adhesion-complex integrity — not a single gene's dose — is the critical variable. The downstream β-catenin/Wnt/EMT arm is biologically coherent and supported by cancer and developmental literature, but in BCDS it remains an **inference** rather than a tissue-level demonstration.

| Feature | CDH1 (BCDS1) | CTNND1 (BCDS2) | HDGC (CDH1) |
|---|---|---|---|
| Typical variant type | Missense (extracellular repeats) | Truncating | LoF (truncating/splice/deletion) |
| Mechanism | Dominant-negative | Haploinsufficiency/LoF | Loss of function (+ 2nd hit) |
| Core phenotype | Eyelid/cleft/dental triad | Triad + cardiac/limb/NDD/GU | Diffuse gastric + lobular breast cancer |
| Cancer risk | Variant-dependent, contested | Not established | High (GC ~40%, LBC ~55%) |
| Penetrance | Incomplete (~47% clefting) | Variable | Incomplete, age-dependent |

---

## Evidence Base

| PMID | Role in report | Support / Challenge |
|---|---|---|
| [29348693](https://pubmed.ncbi.nlm.nih.gov/29348693/) | Dominant-negative CDH1/CTNND1; triad definition | Core support |
| [28301459](https://pubmed.ncbi.nlm.nih.gov/28301459/) | CDH1 missense + CTNND1 truncating; animal models | Core support |
| [28181393](https://pubmed.ncbi.nlm.nih.gov/28181393/) | Quantified dental/craniofacial phenotype | Support |
| [32302040](https://pubmed.ncbi.nlm.nih.gov/32302040/) | First DGC in BCDS | Support (cancer risk) |
| [39596675](https://pubmed.ncbi.nlm.nih.gov/39596675/) | c.760G>A cleft without cancer | Challenge (variant-dependent) |
| [32483297](https://pubmed.ncbi.nlm.nih.gov/32483297/) | Confirmation of cancer risk | Support |
| [29805042](https://pubmed.ncbi.nlm.nih.gov/29805042/) | Ctnnd1-KO CL/P model | Support (mechanism) |
| [32196547](https://pubmed.ncbi.nlm.nih.gov/32196547/) | Expanded CTNND1 phenotype; Xenopus | Support (BCDS2) |
| [40028877](https://pubmed.ncbi.nlm.nih.gov/40028877/) | Novel genitourinary findings | Support (BCDS2 expansion) |
| [29279096](https://pubmed.ncbi.nlm.nih.gov/29279096/) | E-cadherin/β-catenin/Wnt biology | Support (mechanism) |
| [31804558](https://pubmed.ncbi.nlm.nih.gov/31804558/) | E-cadherin loss → β-catenin/EMT | Support (mechanism) |
| [26123647](https://pubmed.ncbi.nlm.nih.gov/26123647/) | AD inheritance, 47% penetrance, haploinsufficiency | Support (genetics) |
| [11476703](https://pubmed.ncbi.nlm.nih.gov/11476703/) | Eyelid reconstructive surgery | Support (treatment) |
| [39442179](https://pubmed.ncbi.nlm.nih.gov/39442179/) | Periocular surgical management | Support (treatment) |
| [20073547](https://pubmed.ncbi.nlm.nih.gov/20073547/) | Dental/overdenture management | Support (treatment) |
| [41563506](https://pubmed.ncbi.nlm.nih.gov/41563506/) | Prenatal diagnosis, rarity | Support (epidemiology) |
| [31945208](https://pubmed.ncbi.nlm.nih.gov/31945208/) | Comparative (sheep CTNND1) | Support (comparative) |
| [32758476](https://pubmed.ncbi.nlm.nih.gov/32758476/) | IGCLC HDGC guidelines | Support (management) |
| [36700973](https://pubmed.ncbi.nlm.nih.gov/36700973/) | HDGC lifetime cancer risks | Support (risk quantification) |
| [36552944](https://pubmed.ncbi.nlm.nih.gov/36552944/) | Novel CDH1 p.Asp400Asn | Support (variant spectrum) |
| [15930907](https://pubmed.ncbi.nlm.nih.gov/15930907/) | BCDS/lagophthalmos continuum | Support (differential) |
| [38132417](https://pubmed.ncbi.nlm.nih.gov/38132417/) | Oligodontia syndrome differential | Support (differential) |

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** With <~100 reported cases and largest cohorts of 11–17 index patients, phenotype frequencies and genotype–phenotype correlations are imprecise; "frequencies" are qualitative.
2. **Cancer risk unresolved.** Whether, and which, CDH1-BCDS variants confer HDGC-class risk is genuinely contested. The field lacks a validated rule linking a BCDS variant to cancer penetrance; management defaults to variant-specific counseling.
3. **β-catenin/Wnt/EMT arm is inferred.** The downstream Wnt/EMT dysregulation in affected human craniofacial tissue has not been directly demonstrated; it is extrapolated from cancer and developmental models.
4. **Mechanistic mismatch in models.** Most animal models use conditional/complete loss of function rather than the human dominant-negative missense mechanism, limiting fidelity. No single model recapitulates the complete human triad.
5. **Penetrance/expressivity modifiers unknown.** Incomplete (~47%) penetrance and nonpenetrant carriers imply uncharacterized modifiers.
6. **Quality-of-life and outcome data are anecdotal**, drawn from case reports rather than systematic patient-reported-outcome instruments.

---

## Proposed Follow-up Experiments / Actions

1. **Variant-resolved cancer-risk registry.** Pool international BCDS cases by exact CDH1 variant and prospectively track gastric/breast cancer to define per-allele penetrance and settle the surveillance question.
2. **Functional triage assay.** Develop a standardized cell-based assay (adhesion, E-cadherin degradation kinetics, β-catenin localization) to classify each BCDS CDH1 variant as "HDGC-like LoF" vs "dominant-negative, cancer-neutral," informing counseling.
3. **Faithful disease model.** Generate knock-in mice/zebrafish carrying patient-specific dominant-negative CDH1 missense alleles (not conditional KO) to test whether they reproduce the full eyelid–cleft–dental triad.
4. **Direct test of the Wnt/EMT branch.** Use patient-derived iPSC craniofacial/dental organoids to measure β-catenin/Wnt and EMT activity, confirming or refuting step 4 of the causal chain in human tissue.
5. **Genotype–phenotype and modifier study.** WGS of BCDS families with discordant expressivity to identify modifier loci explaining incomplete penetrance.
6. **Standardized multidisciplinary outcome measures.** Apply validated ophthalmic, speech, dental, and PRO instruments across a multi-center cohort to quantify functional/QoL burden and benchmark surgical outcomes.

---

*Evidence source legend: human clinical (case series/reports, cohorts), model organism (zebrafish, mouse, Xenopus), in vitro (human cell adhesion assays), computational (ACMG/bioinformatic variant classification). Ontology suggestions (HPO/GO/CL/UBERON/NCIT/MONDO) are provided inline for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Blepharocheilodontic_Syndrome_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Blepharocheilodontic_Syndrome_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 27 |
| On topic | 14 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11476703` *(abstract only)*: "Lateral tarsal strips, lower eyelid retractor disinsertion, myocutaneous advancement of the cheek and eyelids, and lateral tarsorrhaphy were performed. Correction of the ectropion, eyelid retraction, euryblepharon, and marked improvement in his lagophthalmos were achieved postoperatively."
  - closest text in source: "Lateral tarsal strips, lower eyelid retractor disinsertion, myocutaneous advancement of the cheek and eyelids, and lateral tarsorrhaphy were performed"
- `PMID:26123647` *(abstract only)*: "three probably pathogenic variants (c.760G>A [p.Asp254Asn], c.1023T>G [p.Tyr341*], and c.2351G>A [p.Arg784His]) segregated according to autosomal dominant inheritance in four nonsyndromic cleft lip with or without cleft palate (NSCL/P) families (Lod score: 5.8 at θ = 0; 47% penetrance)"
  - closest text in source: "three probably pathogenic variants (c.760G>A [p.Asp254Asn], c.1023T>G [p.Tyr341*], and c.2351G>A [p.Arg784His]) segregated according to autosomal dominant inheritance in four nonsyndromic cleft lip with or without cleft palate (NSCL/P) families (Lod score: 5.8 at θ = 0; 47% penetrance)"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:38132417` (4 mentions) - Oligodontia in the Clinical Spectrum of Syndromes: A Systematic Review.
  - shared terms: syndrome
- `PMID:25010141` (3 mentions) - CD133 expression correlates with membrane beta-catenin and E-cadherin loss from human hair follicle placodes during morphogenesis.
  - shared terms: e-cadherin, gene

Weighed against this report's own most characteristic terms: `cdh1`, `variant`, `ctnnd1`, `eyelid`, `bcds`, `cleft`, `dental`, `cancer`, `syndrome`, `allele`, `craniofacial`, `risk`, `e-cadherin`, `palate`, `malformation`, `gene`, `dominant-negative`, `lip`, `missense`, `bcds2`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000656` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ectropion**
- `HP:0100660` (1 mention) - the report calls it "Physical malformation"; HP calls it **Dyskinesia**
- `HP:0100698` (1 mention) - the report calls it "Clinical sign"; HP calls it **Subcutaneous neurofibroma**
- `HP:0002225` (1 mention) - the report calls it "Physical malformation"; HP calls it **Sparse pubic hair**
- `HP:0000677` (1 mention) - the report calls it "Dental abnormality"; HP calls it **Oligodontia**
- `HP:0000698` (1 mention) - the report calls it "Dental abnormality"; HP calls it **Conical tooth**
- `HP:0000679` (1 mention) - the report calls it "Dental abnormality"; HP calls it **Taurodontia**
- `HP:0000689` (1 mention) - the report calls it "Physical"; HP calls it **Dental malocclusion**
- `HP:0000968` (1 mention) - the report calls it "Physical"; HP calls it **Ectodermal dysplasia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.