---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T11:28:52.212075'
end_time: '2026-09-25T11:44:09.585317'
duration_seconds: 917.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Gas Gangrene
  mondo_id: MONDO:0005767
  category: Infectious Disease
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
citation_count: 37
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 23
  quotes_valid: 16
  quotes_unsupported: 7
  unsupported_quote_references:
  - PMID:26633512
  - PMID:32828915
  - PMID:8557365
  - PMID:162815
  - PMID:8373904
  - PMID:10456947
  - PMID:10621873
  relevance_assessed: 38
  on_topic: 23
  off_topic: 2
  off_topic_references:
  - PMID:42743700
  - PMID:41133194
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 39
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 17
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0012531
    reported_labels:
    - Early, near-universal
    ontology_label: Pain
  - term_id: HP:0003202
    reported_labels:
    - proxy
    ontology_label: Skeletal muscle atrophy
  - term_id: HP:0025439
    reported_labels:
    - "Variable \u2014 **not universal** (PMID: 10621873)"
    ontology_label: Pharyngitis
  - term_id: HP:0000969
    reported_labels:
    - 'Severe, progressive (PMID: 11111933)'
    ontology_label: Edema
  - term_id: HP:0011121
    reported_labels:
    - Progressive
    ontology_label: Abnormal skin morphology
  - term_id: HP:0001945
    reported_labels:
    - Common
    ontology_label: Fever
  - term_id: HP:0031273
    reported_labels:
    - Late/systemic
    ontology_label: Shock
  - term_id: HP:0001878
    reported_labels:
    - 'Rare (~3%), often fatal (PMID: 27049736)'
    ontology_label: Hemolytic anemia
  - term_id: HP:0005521
    reported_labels:
    - 'Severe complication (PMID: 9163265)'
    ontology_label: Disseminated intravascular coagulation
  - term_id: UBERON:0007844
    reported_labels:
    - fascia
    ontology_label: cartilage element
  - term_id: CHEBI:16040
    reported_labels:
    - ceramide
    ontology_label: cytosine
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Gas_Gangrene-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Gas_Gangrene-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gas Gangrene
- **MONDO ID:** MONDO:0005767 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Gas Gangrene** covering all of the
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

# Gas Gangrene (Clostridial Myonecrosis): A Comprehensive Disease Dossier

**Disease:** Gas Gangrene · **MONDO:** MONDO:0005767 · **ICD-10:** A48.0 · **Category:** Infectious Disease
**Evidence base:** 11 confirmed findings · 46 papers reviewed · 5 investigation iterations
**Evidence tiers labeled throughout:** *human clinical*, *model organism* (mouse), *in vitro*, *structural/computational*, *veterinary*.

---

## Summary

Gas gangrene, also termed **clostridial myonecrosis**, is a rapidly progressive, life-threatening necrotizing infection of skeletal muscle caused by toxin-producing anaerobic *Clostridium* species. It is **not a genetic disease** — its etiology is entirely infectious and environmental. The dominant pathogen in **traumatic and post-surgical** cases is *Clostridium perfringens* type A, while **spontaneous (atraumatic)** cases are characteristically caused by *Clostridium septicum* and act as a red flag for occult gastrointestinal malignancy and immunosuppression. The disease belongs to the broader family of necrotizing soft tissue infections (NSTIs), alongside necrotizing fasciitis and Fournier's gangrene.

The pathophysiology is fundamentally **toxin-driven**. Genetic knockout studies provide definitive proof that **alpha-toxin (phospholipase C, encoded by the *plc* gene)** is essential for disease, and that it acts **synergistically with perfringolysin O (theta-toxin, encoded by *pfoA*)**. Together these toxins destroy vascular endothelium and myocytes, provoke a paradoxical **vascular leukostasis** (leukocytes adhere to and plug capillaries rather than entering tissue), cause regional ischemia and spreading edema, and — when the infection becomes systemic — produce **massive intravascular hemolysis** that can kill within hours. Alpha-toxin is a 370-residue zinc metalloenzyme with a catalytic N-terminal domain and a novel prokaryotic C2-like membrane-binding C-terminal domain.

Gas gangrene is a **surgical emergency**. Survival depends on urgent radical excisional debridement combined with antibiotics — specifically **penicillin plus clindamycin**, the latter added because protein-synthesis inhibitors suppress ongoing toxin production whereas penicillin does not. Hyperbaric oxygen is adjunctive. Mortality ranges from roughly **5–30%** for localized clostridial disease confined to an extremity, rising steeply with truncal involvement, delayed diagnosis, advanced age, and comorbidity, and approaches **~100%** for spontaneous *C. septicum* myonecrosis.

---

## Key Findings

### F1 — Alpha-toxin (phospholipase C) is the principal virulence factor

The single most important molecular determinant of *C. perfringens* gas gangrene is **alpha-toxin (CPA/PLC)**, a phospholipase C / sphingomyelinase. Its N-terminal domain (residues 1–250) is catalytic and its C-terminal domain (251–370) is the membrane-binding site; immunization with the C-domain prevents gas gangrene in mice while N-domain immunization does not. Mechanistically, the toxin binds lipid rafts via a GM1a/TrkA complex, generates diacylglycerol, and activates endogenous PLCγ-1 through TrkA, triggering endocytosis and cell death. *Clostridium perfringens* alpha-toxin "is a key mediator of gas gangrene… manifest[ing] as fever, pain, edema, myonecrosis, and gas production. Alpha-toxin possesses phospholipase C and sphingomyelinase activities" ([PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/)). Downstream, the toxin "specifically induces endothelial cell death by promoting ceramide-mediated apoptosis" ([PMID: 32828915](https://pubmed.ncbi.nlm.nih.gov/32828915/)) and impairs muscle regeneration by dose-dependently decreasing MyoD and myogenin in C2C12 myoblasts ([PMID: 32860931](https://pubmed.ncbi.nlm.nih.gov/32860931/)). *(in vitro / model organism)*

### F2 — Vascular/endothelial injury and leukostasis drive the causal chain

Both PLC (alpha-toxin) and perfringolysin O (theta-toxin) act on venous capillary endothelium: PLC strongly induces ELAM-1 (E-selectin), ICAM-1, and IL-8 and converts endothelial cells to a fibroblastoid morphology; PFO induces early ICAM-1 and causes direct endothelial death. "The toxin-induced expression of proadhesive and activational proteins and direct cytopathic effects may contribute to the leukostasis, vascular compromise, and capillary leak characteristic of C. perfringens gas gangrene" ([PMID: 8557365](https://pubmed.ncbi.nlm.nih.gov/8557365/)). The disease is "initiated by direct toxin effects upon venous capillary endothelial cell function, leading to expression of pro-inflammatory mediators and adhesion molecules, and initiation of platelet aggregation" ([PMID: 11111933](https://pubmed.ncbi.nlm.nih.gov/11111933/)). This produces leukocyte hyperadhesion with impaired chemotaxis, leukostasis, capillary leak, regional ischemia, and progressive edema. *(in vitro / review)*

### F3 — Spontaneous (atraumatic) gas gangrene is caused by *C. septicum* and signals occult malignancy

"Spontaneous Clostridium septicum myonecrosis, or gas gangrene, is an extremely rare soft tissue infection associated with malignancy and immunosuppression. Even with appropriate treatment the mortality rate approaches 100%" ([PMID: 18555761](https://pubmed.ncbi.nlm.nih.gov/18555761/)). "Atraumatic infections due to Clostridium septicum are known to be associated with immunosuppression or even malignancy" ([PMID: 16021394](https://pubmed.ncbi.nlm.nih.gov/16021394/)). Multiple case reports document *C. septicum* bacteremia/myonecrosis revealing occult colon or rectal cancer ([PMID: 10901913](https://pubmed.ncbi.nlm.nih.gov/10901913/); [PMID: 18019648](https://pubmed.ncbi.nlm.nih.gov/18019648/)), mandating GI malignancy workup. By contrast, traumatic/post-surgical disease is predominantly *C. perfringens* type A ([PMID: 18034207](https://pubmed.ncbi.nlm.nih.gov/18034207/)). *(human clinical)*

### F4 — Treatment requires urgent surgical debridement plus antibiotics; HBO is adjunctive

"Treatment of choice is surgical debridement of the infectious focus with radical removal of all necrotic tissue, resection of the corresponding lymphatics in addition to antibiotic therapy with penicillin G, aminoglycosides, or clindamycin or hyperbaric oxygenation" ([PMID: 18034207](https://pubmed.ncbi.nlm.nih.gov/18034207/)). In a Duke HBO series of 49 patients: "Survival in patients with involvement confined to the extremities was 92.3 percent… combined involvement of extremity and trunk was 53.3 percent, and with primary trunk involvement half… survived. Survival for the entire series was 73.5 percent" ([PMID: 162815](https://pubmed.ncbi.nlm.nih.gov/162815/)). Nonclostridial gas gangrene carries ~43% mortality, worsened by delay ([PMID: 11782626](https://pubmed.ncbi.nlm.nih.gov/11782626/)). *(human clinical)*

### F5 — Alpha-toxin is a 370-residue two-domain zinc metalloenzyme with a novel prokaryotic C2 domain

"The toxin is a 370-residue, zinc metalloenzyme that has phospholipase C activity, and can bind to membranes in the presence of calcium. The crystal structure of the enzyme reveals a two-domain protein" ([PMID: 9699639](https://pubmed.ncbi.nlm.nih.gov/9699639/)). The N-terminal catalytic domain resembles *Bacillus cereus* PC-PLC; "The C-terminal domain shows a strong structural analogy to eukaryotic calcium-binding C2 domains. We believe this is the first example of such a domain in prokaryotes" ([PMID: 9699639](https://pubmed.ncbi.nlm.nih.gov/9699639/)). C2 domains bind phospholipid/calcium in intracellular second-messenger proteins — pathways the toxin perturbs. *(structural)*

### F6 — Gas gangrene sits within NSTIs with age- and comorbidity-dependent mortality

In a Medicare NSTI cohort of adults ≥65 (n=1427), 97% required emergency surgery and "The overall mortality was 5.3%. Several underlying comorbidities were associated with higher rates of mortality including cancer (OR: 3.50, P = 0.0009), liver disease (OR: 2.97, P = 0.03), and kidney disease (OR: 2.15, P = 0.01)" ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/)). A validated NSQIP calculator (n=1392) reported 13% 30-day mortality with independent predictors including "age older than 60 years (odds ratio [OR] = 2.5; 95% CI 1.7–3.6)" plus dialysis (1.9), ASA ≥4 (3.6), septic shock (2.4), and platelets <50K (3.5) ([PMID: 23628224](https://pubmed.ncbi.nlm.nih.gov/23628224/)). Pediatric NSTI is rare (355 US cases, 2016–2020) ([PMID: 38518580](https://pubmed.ncbi.nlm.nih.gov/38518580/)). *(human clinical)*

### F7 — Naturally occurring clostridial myonecrosis in animals: blackleg (*C. chauvoei*)

"Blackleg is an infectious disease that mainly affects cattle and rarely affects other ruminants. It is characterized by hemorrhagic blackleg myositis" ([PMID: 40989646](https://pubmed.ncbi.nlm.nih.gov/40989646/)) and "is a soil-borne disease primarily affecting cattle and is caused by Clostridium chauvoei" ([PMID: 42743700](https://pubmed.ncbi.nlm.nih.gov/42743700/)). It is endemic in regions such as Ethiopia and Kazakhstan with strong seasonal (post-rainy/November) peaks ([PMID: 41133194](https://pubmed.ncbi.nlm.nih.gov/41133194/)), with novel presentations including intestinal necrosis in calves ([PMID: 42545146](https://pubmed.ncbi.nlm.nih.gov/42545146/)). Unlike traumatic human disease, blackleg is typically **endogenous** — latent muscle spores activated by hypoxia. Controlled by multivalent clostridial vaccines. *(veterinary)*

### F8 — Alpha-toxin-mediated massive intravascular hemolysis is a rare, rapidly fatal complication

"C. perfringens sepsis is uncommon, [but] it is often rapidly fatal because the alpha toxin of this bacterium induces massive intravascular hemolysis by disrupting red blood cell membranes" ([PMID: 27049736](https://pubmed.ncbi.nlm.nih.gov/27049736/)); characteristic labs are severe hemolytic anemia with very low MCV, spherocytes, hemolyzed sample, and negative Coombs. Fulminant *C. perfringens* bacteremia is "severe and fatal in fifty per cent of cases" ([PMID: 37110247](https://pubmed.ncbi.nlm.nih.gov/37110247/)). In a 13-year series, fatal intravascular hemolysis occurred in ~3.0% (1/33) of *C. perfringens* infections ([PMID: 25755747](https://pubmed.ncbi.nlm.nih.gov/25755747/)). "Serum PLC activity… showed a nearly fivefold increase (6.0 to 27.3 U/l), which is consistent with the hypothesized dominant role of this enzyme" ([PMID: 8373904](https://pubmed.ncbi.nlm.nih.gov/8373904/)); death can occur within 4–8 hours of admission ([PMID: 1776111](https://pubmed.ncbi.nlm.nih.gov/1776111/)). *(human clinical)*

### F9 — Clindamycin outperforms penicillin by suppressing toxin synthesis

"Clindamycin is more efficacious than penicillin in experimental gas gangrene caused by Clostridium perfringens in animals" ([PMID: 7548539](https://pubmed.ncbi.nlm.nih.gov/7548539/)). Efficacy tracks toxin suppression, not bactericidal activity: "complete suppression of alpha-toxin activity by tetracycline, metronidazole, rifampin, clindamycin, and chloramphenicol at concentrations equal to the MIC. In contrast, alpha-toxin activity persisted at concentrations of penicillin equal to and above the MIC" ([PMID: 2882731](https://pubmed.ncbi.nlm.nih.gov/2882731/)). This underpins the guideline-recommended **penicillin + clindamycin** combination. *(model organism)*

### F10 — Genetic proof: alpha-toxin (*plc*) is essential and synergizes with theta-toxin (*pfoA*)

Allelic-exchange inactivation of the chromosomal *plc* gene showed "the plc mutants had demonstrably reduced virulence and therefore provided definitive genetic evidence for the essential role of alpha-toxin in gas gangrene" ([PMID: 7746141](https://pubmed.ncbi.nlm.nih.gov/7746141/)). Alpha-toxin and PFO act synergistically: "the isogenic strain that was reconstituted for both toxins produced a pathology that was clearly more severe than when alpha-toxin alone was reconstituted" ([PMID: 11705975](https://pubmed.ncbi.nlm.nih.gov/11705975/)). Both are required for leukostasis: "significantly reduced leukocyte aggregation when alpha-toxin was absent and complete abrogation… when theta-toxin was absent. Thus, both alpha-toxin and theta-toxin are necessary for the characteristic vascular leukostasis" ([PMID: 10456947](https://pubmed.ncbi.nlm.nih.gov/10456947/)). By contrast, alpha-clostripain (*ccp*) is dispensable ([PMID: 21829506](https://pubmed.ncbi.nlm.nih.gov/21829506/)). *(model organism)*

### F11 — Diagnosis is clinical/surgical; tissue gas is not universal and delay is the chief pitfall

"Tissue gas is not a universal finding in necrotizing soft tissue infections. This misconception… contributes to diagnostic errors. Incision and drainage is an inappropriate surgical strategy… excisional debridement is needed" ([PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)). "The two commonest pitfalls in management are failure of early diagnosis and inadequate surgical debridement" (same source). For severe SSTIs, "intensive care, source control, and broad-spectrum antimicrobials are required for the initial phase of illness," with growing use of rapid diagnostics and ongoing IVIG debate ([PMID: 29278528](https://pubmed.ncbi.nlm.nih.gov/29278528/)). *(review)*

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Spore inoculation** into devitalized/hypoxic tissue (trauma, surgery) **or** hematogenous seeding from a GI lesion (spontaneous *C. septicum*) → germination of vegetative clostridia in an anaerobic niche. *(demonstrated)*
2. Local hypoxia/low redox potential → **permits anaerobic proliferation** and toxin-gene expression. *(inferred/demonstrated)*
3. Vegetative growth → secretion of **alpha-toxin (PLC)** and **perfringolysin O (theta-toxin)**. *(demonstrated genetically; PMID: 7746141, 11705975)*
4. Alpha-toxin's PLC/sphingomyelinase activity hydrolyzes membrane phospholipids → **DAG + ceramide**; via GM1a/TrkA raft binding, activates PLCγ-1 → **endothelial and myocyte apoptosis/death** and **blocked myogenesis** (↓MyoD/myogenin). *(in vitro; PMID: 26633512, 32828915, 32860931)*
5. Toxins on venous capillary endothelium → **↑E-selectin/ICAM-1/IL-8** and platelet aggregation. *(in vitro; PMID: 8557365, 11111933)*
6. **Branch — both toxins required:** leukocyte hyperadhesion + impaired chemotaxis → **vascular leukostasis** (neutrophils plug capillaries instead of clearing bacteria). *(mouse; PMID: 10456947)*
7. Leukostasis + endothelial injury → **capillary leak, ischemia, progressive edema** → feed-forward extension of the anaerobic zone. *(inferred/demonstrated)*
8. Anaerobic fermentation of muscle → **tissue gas** (variable) + spreading **coagulative myonecrosis** → clinical gas gangrene. *(demonstrated; gas not universal, PMID: 10621873)*
9. **Systemic branch:** toxin in bloodstream → alpha-toxin lyses RBC membranes → **massive intravascular hemolysis** → hemolytic anemia, DIC, multi-organ failure, death within hours. *(human; PMID: 27049736, 8373904)*

```
  TRAUMA/SURGERY (C. perfringens)          GI LESION/MALIGNANCY (C. septicum)
        │                                            │
        └───────────────┬────────────────────────────┘
                        ▼
          Anaerobic niche → clostridial growth
                        ▼
     ALPHA-TOXIN (plc, PLC)  +  THETA-TOXIN (pfoA, PFO)
        │                 │                    │
        ▼                 ▼                    ▼
  membrane hydrolysis   endothelial injury   RBC lysis (systemic)
  → DAG/ceramide        + E-sel/ICAM-1/IL-8         │
  → endothelial +             │                     ▼
  myocyte apoptosis;          ▼            MASSIVE INTRAVASCULAR
  ↓MyoD/myogenin       leukocyte hyperadhesion  HEMOLYSIS → DIC,
        │              (BOTH toxins required)   MOF, death (hrs)
        │                     ▼
        │            VASCULAR LEUKOSTASIS → capillary leak,
        │            ischemia, spreading EDEMA
        └──────────────┬───────────────┘
                       ▼
      SPREADING MYONECROSIS + TISSUE GAS → SEPTIC SHOCK
                       ▼
   ── Interrupted only by: EMERGENCY EXCISIONAL DEBRIDEMENT
      + PENICILLIN/CLINDAMYCIN (toxin suppression) + HBO ──
```

The unifying theme is **exotoxin-driven vascular and myofiber destruction with a self-amplifying ischemic loop**: toxins kill endothelium and jam neutrophils in capillaries, which starves tissue of oxygen and immune defense, which further favors clostridial growth. Because the damage is enzymatic and toxin-mediated rather than dependent on bacterial burden alone, therapy must both **remove the substrate (surgery)** and **silence the toxin (protein-synthesis-inhibiting antibiotics)** — the direct rationale for the penicillin + clindamycin combination.

---

## Detailed Section-by-Section Report

### 1. Disease Information

**Overview.** A rapidly progressive, life-threatening necrotizing infection of skeletal muscle caused by toxin-producing *Clostridium* species, most often *C. perfringens* type A, characterized by "fever, pain, edema, myonecrosis, and gas production" ([PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/)). It is one member of the broader **necrotizing soft tissue infections (NSTIs)** ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/); [PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)).

**Key identifiers.** MONDO:0005767 · ICD-10 A48.0 · ICD-11 (gas gangrene) · MeSH D005738 · SNOMED CT 372070002. **OMIM/Orphanet: not applicable** — acquired infection, not a Mendelian disorder.

**Synonyms.** Clostridial myonecrosis; clostridial gas gangrene; myonecrosis; emphysematous gangrene. In animals: blackleg (*C. chauvoei*), malignant edema (*C. septicum/C. perfringens*).

**Information source.** Disease-level aggregated resources (reviews, case series, mouse pathogenesis studies); population burden from administrative/registry datasets coded at the NSTI level ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/); [PMID: 23628224](https://pubmed.ncbi.nlm.nih.gov/23628224/); [PMID: 38518580](https://pubmed.ncbi.nlm.nih.gov/38518580/)).

### 2. Etiology

**Primary cause — infectious.** Anaerobic, spore-forming *Clostridium* bacilli via two routes: (1) **traumatic/post-surgical** — predominantly *C. perfringens* type A (NCBITaxon:1502) in devitalized muscle ([PMID: 18034207](https://pubmed.ncbi.nlm.nih.gov/18034207/)); (2) **spontaneous/hematogenous** — predominantly *C. septicum* (NCBITaxon:1504), associated with occult GI malignancy, neutropenia, immunosuppression ([PMID: 18555761](https://pubmed.ncbi.nlm.nih.gov/18555761/); [PMID: 16021394](https://pubmed.ncbi.nlm.nih.gov/16021394/)). Other agents: *C. novyi*, *C. histolyticum*, *C. sordellii*.

**Risk factors (host/environmental).** Penetrating/crush trauma, open fractures, contaminated wounds, GI/biliary surgery, septic abortion; **diabetes mellitus** ([PMID: 11782626](https://pubmed.ncbi.nlm.nih.gov/11782626/)); **malignancy (OR 3.50), liver disease (OR 2.97), renal disease (OR 2.15)** ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/)); chemotherapy/neutropenia/cirrhosis ([PMID: 25755747](https://pubmed.ncbi.nlm.nih.gov/25755747/)); age >60, male sex (~59%) ([PMID: 23628224](https://pubmed.ncbi.nlm.nih.gov/23628224/)).

**Genetic risk factors (human host): none established — not applicable.** **Protective factors:** prompt wound debridement, tissue oxygenation, veterinary toxoid vaccination; no human genetic protective variants. **Gene–environment interaction:** operates as **pathogen-genotype × host-microenvironment** (toxin genes expressed under anaerobic necrotic conditions).

### 3. Phenotypes

| Phenotype | Type | Characteristics | HPO |
|---|---|---|---|
| Severe pain out of proportion | Symptom | Early, near-universal | HP:0012531 |
| Myonecrosis | Pathological sign | Severe, progressive; defining | HP:0003202 (proxy) |
| Soft-tissue gas/crepitus | Sign | Variable — **not universal** ([PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)) | HP:0025439 |
| Tense edema | Sign | Severe, progressive ([PMID: 11111933](https://pubmed.ncbi.nlm.nih.gov/11111933/)) | HP:0000969 |
| Skin discoloration/hemorrhagic bullae | Physical | Progressive | HP:0011121 |
| Fever | Symptom | Common | HP:0001945 |
| Septic shock/hypotension | Sign | Late/systemic | HP:0031273 |
| Hemolytic anemia | Lab | Rare (~3%), often fatal ([PMID: 27049736](https://pubmed.ncbi.nlm.nih.gov/27049736/)) | HP:0001878 |
| DIC | Lab/clinical | Severe complication ([PMID: 9163265](https://pubmed.ncbi.nlm.nih.gov/9163265/)) | HP:0005521 |
| Rhabdomyolysis/↑CK/acute renal failure | Lab | Severe ([PMID: 9163265](https://pubmed.ncbi.nlm.nih.gov/9163265/)) | HP:0003236; HP:0000083 |

**Onset:** acute (hours–days); adult predominance. **Progression:** fulminant. **Quality of life:** survivors often undergo amputation/extensive debridement with lasting disability; disease-specific EQ-5D/SF-36 data not available.

### 4. Genetic / Molecular Information

**Human causal genes: none — not applicable.** No human causal genes, pathogenic variants, modifier genes, epigenetic marks, or chromosomal abnormalities.

**Pathogen virulence genes (operative molecular determinants):**
- ***plc*** → alpha-toxin (CPA), 370-aa zinc-metalloenzyme PLC/sphingomyelinase, UniProt **P0C216**; **essential** ([PMID: 7746141](https://pubmed.ncbi.nlm.nih.gov/7746141/)).
- ***pfoA*** → perfringolysin O (theta-toxin), cholesterol-dependent cytolysin, UniProt **P0C2E9**; synergistic, required for leukostasis ([PMID: 11705975](https://pubmed.ncbi.nlm.nih.gov/11705975/); [PMID: 10456947](https://pubmed.ncbi.nlm.nih.gov/10456947/)).
- ***ccp*** → alpha-clostripain; **dispensable** ([PMID: 21829506](https://pubmed.ncbi.nlm.nih.gov/21829506/)).
- ***cpe*/*ccpA*** → enterotoxin/regulator; CcpA does **not** regulate PLC ([PMID: 15292123](https://pubmed.ncbi.nlm.nih.gov/15292123/)).

**Toxinotyping:** *C. perfringens* **type A** (cpa/plc+) is the principal agent; cpa/type A confirmed in fatal hemolysis ([PMID: 25755747](https://pubmed.ncbi.nlm.nih.gov/25755747/)).

### 5. Environmental Information

Clostridial spores reside in **soil, dust, and mammalian GI tracts**; wound contamination with soil/foreign bodies is the classic exposure. Blackleg is explicitly soil-borne with seasonal peaks ([PMID: 42743700](https://pubmed.ncbi.nlm.nih.gov/42743700/)). Lifestyle: injection drug use, smoking/diabetes (impaired perfusion). Infectious agents (NCBI Taxonomy): *C. perfringens* (1502), *C. septicum* (1504), *C. novyi* (1522), *C. histolyticum* (1498), *C. sordellii* (1505), *C. chauvoei* (1494). Nonclostridial gas gangrene (mixed aerobic/anaerobic) has ~43% mortality ([PMID: 11782626](https://pubmed.ncbi.nlm.nih.gov/11782626/)).

### 6. Mechanism / Pathophysiology

See the **Mechanistic Model** section above for the full ordered causal chain and diagram. Key category detail:
- **Molecular pathways:** phospholipid/sphingolipid hydrolysis → DAG/ceramide; TrkA/PLCγ-1 activation; ceramide→apoptosis (GO:0004629 phospholipase C activity; GO:0006672 ceramide metabolic process) ([PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/); [PMID: 32828915](https://pubmed.ncbi.nlm.nih.gov/32828915/)).
- **Cellular processes:** apoptosis (GO:0006915), inflammation, blocked myogenesis (GO:0042692), platelet aggregation (GO:0070527) ([PMID: 32860931](https://pubmed.ncbi.nlm.nih.gov/32860931/)).
- **Protein dysfunction:** bacterial gain-of-toxic-function; two-domain zinc metalloenzyme ([PMID: 9699639](https://pubmed.ncbi.nlm.nih.gov/9699639/)).
- **Immune involvement:** paradoxical leukostasis with failure of neutrophil tissue entry; IL-8 induction ([PMID: 8557365](https://pubmed.ncbi.nlm.nih.gov/8557365/)).
- **Tissue damage:** ischemia, direct cytolysis, coagulative necrosis, hemolysis.
- **Omics:** no large-scale human transcriptomic/proteomic/metabolomic disease atlases identified — data are targeted in vitro/mouse. *Omics largely not available.*
- **Cell types (CL):** endothelial cell (CL:0000115), skeletal muscle cell (CL:0000188), myoblast (CL:0000056), erythrocyte (CL:0000232), neutrophil (CL:0000775), platelet (CL:0000233).

### 7. Anatomical Structures Affected

Primary: **skeletal muscle** (UBERON:0001134) and its microvasculature; secondarily subcutaneous tissue/fascia (UBERON:0007844). Body systems: musculoskeletal (primary), cardiovascular/microvascular (UBERON:0001982 capillary; UBERON:0001986 endothelium), hematologic (RBC hemolysis), with systemic sepsis affecting kidneys, lungs, coagulation ([PMID: 9163265](https://pubmed.ncbi.nlm.nih.gov/9163265/)). Subcellular (GO CC): plasma membrane (GO:0005886), membrane raft (GO:0045121), extracellular region (GO:0005576). Localization: typically **unilateral/focal** at the wound, spreading proximally; spontaneous *C. septicum* can be multifocal/distant.

### 8. Temporal Development

Onset: **acute**, incubation <24 h to a few days (traumatic); adult/geriatric. Progression: **fulminant, monophasic** (early local pain/edema → intermediate discoloration/bullae/crepitus/toxicity → advanced myonecrosis/shock/hemolysis). Not relapsing/chronic. Remission is treatment-induced via surgical source control ([PMID: 18555761](https://pubmed.ncbi.nlm.nih.gov/18555761/)). **Critical period: the first hours** — time-to-debridement is the dominant modifiable survival determinant ([PMID: 11782626](https://pubmed.ncbi.nlm.nih.gov/11782626/); [PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)).

### 9. Inheritance and Population

Epidemiology: **rare**; invasive *C. perfringens* ~0.017% of samples in one series ([PMID: 25755747](https://pubmed.ncbi.nlm.nih.gov/25755747/)); pediatric NSTI very rare (355 US cases 2016–2020) ([PMID: 38518580](https://pubmed.ncbi.nlm.nih.gov/38518580/)). Inheritance: **not applicable** (all genetic-etiology sub-items — penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, carrier frequency — N/A). Demographics: male predominance (~59%) ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/)); older/comorbid populations over-represented. Geographic: worldwide, historically battlefield-associated; veterinary blackleg endemic to specific soils ([PMID: 42743700](https://pubmed.ncbi.nlm.nih.gov/42743700/); [PMID: 41133194](https://pubmed.ncbi.nlm.nih.gov/41133194/)).

### 10. Diagnostics

Clinical diagnosis paramount ([PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)). Labs: leukocytosis, markedly elevated CK, lactic acidosis; in hemolysis — severe anemia, low MCV, spherocytes, negative Coombs ([PMID: 27049736](https://pubmed.ncbi.nlm.nih.gov/27049736/)); DIC panel. Microbiology: Gram stain (large Gram-positive bacilli, few leukocytes), anaerobic culture, PCR toxin-gene typing on tissue ([PMID: 25755747](https://pubmed.ncbi.nlm.nih.gov/25755747/)); intragranulocytic bacilli on blood smear in sepsis ([PMID: 1776111](https://pubmed.ncbi.nlm.nih.gov/1776111/)). Imaging: CT/MRI show soft-tissue gas dissecting fascial planes — but **gas not universal** ([PMID: 42348105](https://pubmed.ncbi.nlm.nih.gov/42348105/); [PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)). Definitive: surgical exploration (necrotic, non-contractile muscle). Differential: necrotizing fasciitis, crepitant cellulitis, pyomyositis. Spontaneous *C. septicum* → **occult GI malignancy workup** ([PMID: 16021394](https://pubmed.ncbi.nlm.nih.gov/16021394/)). Genetic/omics/screening: **not applicable**.

### 11. Outcome / Prognosis

Mortality high and extent-dependent: 73.5% overall survival, 92.3% extremity-only, ~53% extremity+trunk, 50% trunk (HBO series) ([PMID: 162815](https://pubmed.ncbi.nlm.nih.gov/162815/)); 5.3% in-hospital (older adults) to 13% 30-day (NSQIP) ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/); [PMID: 23628224](https://pubmed.ncbi.nlm.nih.gov/23628224/)); nonclostridial ~43% ([PMID: 11782626](https://pubmed.ncbi.nlm.nih.gov/11782626/)); spontaneous *C. septicum* ~100% ([PMID: 18555761](https://pubmed.ncbi.nlm.nih.gov/18555761/)); bacteremia with hemolysis ~50% ([PMID: 37110247](https://pubmed.ncbi.nlm.nih.gov/37110247/)). Prognostic factors: anatomic extent, time-to-debridement, age >60, septic shock, ASA ≥4, dialysis, thrombocytopenia ([PMID: 23628224](https://pubmed.ncbi.nlm.nih.gov/23628224/)), comorbidity ([PMID: 32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/)). Morbidity: amputation, tissue loss, long-term disability. Recovery possible with early radical surgery.

### 12. Treatment

**Triad (urgent, simultaneous):** (1) **Surgical** — radical excisional debridement, fasciotomy, amputation as needed, repeat debridement ([PMID: 18034207](https://pubmed.ncbi.nlm.nih.gov/18034207/); [PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)); NCIT: Surgical Debridement (C15329), Amputation (C15275). (2) **Antibiotics** — **penicillin G + clindamycin** (clindamycin suppresses toxin synthesis) ([PMID: 2882731](https://pubmed.ncbi.nlm.nih.gov/2882731/); [PMID: 7548539](https://pubmed.ncbi.nlm.nih.gov/7548539/)); alternatives metronidazole/tetracycline/aminoglycosides; NCIT: Penicillin G (C716), Clindamycin (C376), Metronidazole (C639). (3) **HBO, adjunctive** ([PMID: 162815](https://pubmed.ncbi.nlm.nih.gov/162815/)); NCIT: Hyperbaric Oxygen Therapy (C15683) — secondary to surgery ([PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/)). Supportive ICU care, resuscitation, shock/DIC/renal management ([PMID: 29278528](https://pubmed.ncbi.nlm.nih.gov/29278528/)). Experimental: IVIG (debated); anti-alpha-toxin C-domain immunotherapy protective in mice ([PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/)). Pharmacogenomics: not applicable.

### 13. Prevention

Primary: meticulous wound care, early debridement, avoiding tight closure of contaminated wounds ([PMID: 10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/); [PMID: 162815](https://pubmed.ncbi.nlm.nih.gov/162815/)). Secondary: early recognition + rapid surgery; occult GI malignancy workup in *C. septicum* ([PMID: 16021394](https://pubmed.ncbi.nlm.nih.gov/16021394/)). Tertiary: aggressive source control + ICU support. **Immunization (humans): no licensed vaccine** (C-domain alpha-toxoid protective experimentally only, [PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/)). **Veterinary: multivalent clostridial toxoids** prevent blackleg/malignant edema ([PMID: 40989646](https://pubmed.ncbi.nlm.nih.gov/40989646/)). Genetic counseling/carrier screening: not applicable.

### 14. Other Species / Natural Disease

Hosts: cattle *Bos taurus* (NCBITaxon:9913), sheep *Ovis aries* (9940), other ruminants. **Blackleg** (*C. chauvoei*, NCBITaxon:1494) — soil-borne, highly lethal hemorrhagic emphysematous myositis, typically **endogenous** ([PMID: 40989646](https://pubmed.ncbi.nlm.nih.gov/40989646/); [PMID: 42743700](https://pubmed.ncbi.nlm.nih.gov/42743700/)); novel intestinal-necrosis presentation ([PMID: 42545146](https://pubmed.ncbi.nlm.nih.gov/42545146/)); atypical prolonged courses ([PMID: 42651908](https://pubmed.ncbi.nlm.nih.gov/42651908/)). **Malignant edema** (*C. septicum/C. perfringens/C. novyi*) from wound contamination. Veterinary importance: major cause of sudden death/economic loss, managed by vaccination ([PMID: 41133194](https://pubmed.ncbi.nlm.nih.gov/41133194/)). Comparative pathology: shared core mechanism, differing route (endogenous latency vs traumatic contamination). Alpha-toxin also implicated in animal sudden-death syndrome ([PMID: 9699639](https://pubmed.ncbi.nlm.nih.gov/9699639/)). Zoonotic potential: minimal — environmental/endogenous acquisition, not animal-to-human transmission.

### 15. Model Organisms

**Primary — mouse myonecrosis model** (i.m./footpad *C. perfringens* inoculation): workhorse for pathogenesis, high fidelity to human histopathology ([PMID: 7746141](https://pubmed.ncbi.nlm.nih.gov/7746141/); [PMID: 11705975](https://pubmed.ncbi.nlm.nih.gov/11705975/); [PMID: 10456947](https://pubmed.ncbi.nlm.nih.gov/10456947/); [PMID: 2882731](https://pubmed.ncbi.nlm.nih.gov/2882731/)). **Genetic models (bacterial):** isogenic allelic-exchange/TargeTron knockouts of *plc*, *pfoA*, *ccp* with complementation ([PMID: 7746141](https://pubmed.ncbi.nlm.nih.gov/7746141/); [PMID: 21829506](https://pubmed.ncbi.nlm.nih.gov/21829506/)). **In vitro:** C2C12 myoblasts ([PMID: 32860931](https://pubmed.ncbi.nlm.nih.gov/32860931/)), HUVEC ([PMID: 8557365](https://pubmed.ncbi.nlm.nih.gov/8557365/)), CD31+ endothelial cells ([PMID: 32828915](https://pubmed.ncbi.nlm.nih.gov/32828915/)), erythrocyte hemolysis ([PMID: 24349173](https://pubmed.ncbi.nlm.nih.gov/24349173/)). **Structural/computational:** alpha-toxin crystal structure ([PMID: 9699639](https://pubmed.ncbi.nlm.nih.gov/9699639/)); in silico N–C domain docking ([PMID: 24349173](https://pubmed.ncbi.nlm.nih.gov/24349173/)). **Limitations:** mouse models emphasize local toxin-driven process; less capture of human comorbidity context and the spontaneous *C. septicum*/malignancy axis. No host-genetic disease lines (host is not predisposed). **Resources:** *C. perfringens* strain 13; ATCC 13124.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [7746141](https://pubmed.ncbi.nlm.nih.gov/7746141/) | Genetic proof alpha-toxin (*plc*) essential | Model organism |
| [11705975](https://pubmed.ncbi.nlm.nih.gov/11705975/) | Alpha-toxin × PFO synergy | Model organism |
| [10456947](https://pubmed.ncbi.nlm.nih.gov/10456947/) | Both toxins required for leukostasis | Model organism |
| [26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/) | Alpha-toxin mechanism; clinical features; C-domain vaccine | In vitro/review |
| [9699639](https://pubmed.ncbi.nlm.nih.gov/9699639/) | Crystal structure; novel prokaryotic C2 domain | Structural |
| [32828915](https://pubmed.ncbi.nlm.nih.gov/32828915/) | Ceramide-mediated endothelial apoptosis | In vitro |
| [32860931](https://pubmed.ncbi.nlm.nih.gov/32860931/) | Impaired myogenesis (↓MyoD/myogenin) | In vitro |
| [8557365](https://pubmed.ncbi.nlm.nih.gov/8557365/) | Adhesion molecule/IL-8 upregulation | In vitro |
| [11111933](https://pubmed.ncbi.nlm.nih.gov/11111933/) | Pathogenesis causal chain | Review |
| [18555761](https://pubmed.ncbi.nlm.nih.gov/18555761/) | Spontaneous *C. septicum*, ~100% mortality | Human |
| [16021394](https://pubmed.ncbi.nlm.nih.gov/16021394/) | Atraumatic *C. septicum* ↔ malignancy | Human |
| [27049736](https://pubmed.ncbi.nlm.nih.gov/27049736/) | Alpha-toxin → massive hemolysis | Human |
| [8373904](https://pubmed.ncbi.nlm.nih.gov/8373904/) | Rising PLC drives hemolysis | Human |
| [162815](https://pubmed.ncbi.nlm.nih.gov/162815/) | HBO survival by anatomic extent | Human |
| [18034207](https://pubmed.ncbi.nlm.nih.gov/18034207/) | Standard treatment triad | Review |
| [2882731](https://pubmed.ncbi.nlm.nih.gov/2882731/) | Clindamycin > penicillin (toxin suppression) | Model organism |
| [10621873](https://pubmed.ncbi.nlm.nih.gov/10621873/) | Gas not universal; excisional debridement | Review |
| [32818779](https://pubmed.ncbi.nlm.nih.gov/32818779/) | NSTI comorbidity mortality ORs | Human |
| [23628224](https://pubmed.ncbi.nlm.nih.gov/23628224/) | Validated NSTI mortality predictors | Human |
| [40989646](https://pubmed.ncbi.nlm.nih.gov/40989646/) / [42743700](https://pubmed.ncbi.nlm.nih.gov/42743700/) | Blackleg (*C. chauvoei*) | Veterinary |

---

## Ontology Term Appendix (for KB population)

- **Disease:** MONDO:0005767; MeSH D005738; ICD-10 A48.0; SNOMED 372070002.
- **Pathogen genes/proteins:** *plc*/alpha-toxin (UniProt P0C216); *pfoA*/perfringolysin O (UniProt P0C2E9).
- **GO (process):** GO:0004629 (phospholipase C activity), GO:0006672 (ceramide metabolic process), GO:0006915 (apoptosis), GO:0070527 (platelet aggregation), GO:0006954 (inflammatory response), GO:0042692 (muscle cell differentiation).
- **GO (component):** GO:0005886 (plasma membrane), GO:0045121 (membrane raft), GO:0005576 (extracellular region).
- **CL:** CL:0000115 (endothelial cell), CL:0000188 (skeletal muscle cell), CL:0000056 (myoblast), CL:0000232 (erythrocyte), CL:0000775 (neutrophil), CL:0000233 (platelet).
- **UBERON:** UBERON:0001134 (skeletal muscle), UBERON:0007844 (fascia), UBERON:0001982 (capillary), UBERON:0001986 (endothelium).
- **CHEBI:** CHEBI:29105 (zinc 2+), CHEBI:29108 (calcium 2+), CHEBI:17636 (sphingomyelin), CHEBI:16040 (ceramide).
- **NCIT (treatment):** C15329 (Surgical Debridement), C15275 (Amputation), C15683 (Hyperbaric Oxygen Therapy), C716 (Penicillin G), C376 (Clindamycin), C639 (Metronidazole).

---

## Limitations and Knowledge Gaps

1. **No human genetic architecture** — as an acquired infection, many template sections (causal genes, variants, inheritance, omics diagnostics, genetic screening) are intrinsically not applicable.
2. **Rarity limits epidemiology** — precise incidence/prevalence for gas gangrene specifically is ill-defined; cohort data pool it within NSTIs.
3. **Human host-susceptibility mechanisms underexplored** — why some patients develop fulminant hemolysis vs localized disease is unresolved; the malignancy–*C. septicum* link is epidemiologic, not mechanistically dissected.
4. **Adjunctive therapy uncertainty** — HBO and IVIG benefit rests on observational/experimental (non-randomized) evidence.
5. **Model gaps** — mouse models do not recapitulate the comorbid spontaneous *C. septicum* setting or the full systemic hemolysis/DIC syndrome.
6. **Citation currency** — several foundational mechanistic papers are decades old; contemporary human molecular-profiling datasets of gas-gangrene tissue are essentially absent.

---

## Proposed Follow-up Experiments / Actions

1. **Time-to-debridement quantification** — model mortality as a continuous function of hours-to-first-debridement, controlling for anatomic extent and comorbidity, to formalize the "surgical clock."
2. **Anti-toxin adjunct trials** — evaluate C-domain-directed antibodies or small-molecule PLC inhibitors as surgical adjuncts, building on protective C-domain immunization data ([PMID: 26633512](https://pubmed.ncbi.nlm.nih.gov/26633512/)).
3. **Host-susceptibility profiling** — transcriptomic/single-cell analysis of human gas-gangrene surgical specimens to map endothelial and neutrophil states in situ and validate the leukostasis model in humans.
4. **Systematic *C. septicum*–malignancy pathway** — prospectively characterize the GI mucosal breach permitting hematogenous seeding, to define a screening/prevention protocol.
5. **HBO and IVIG RCTs** — adequately powered randomized or emulated-trial analyses to resolve adjunct benefit.
6. **Improved rapid diagnostics** — validate point-of-care PCR toxinotyping ([PMID: 25755747](https://pubmed.ncbi.nlm.nih.gov/25755747/)) and bedside biomarkers (serum PLC activity) to shorten time-to-diagnosis.

---

### Evidence source key
**Human clinical:** PMID 18034207, 18555761, 16021394, 10901913, 18019648, 11782626, 9163265, 162815, 27049736, 25755747, 8373904, 1776111, 37110247, 32818779, 23628224, 38518580, 10621873, 29278528, 42348105.
**Model organism (mouse):** PMID 7746141, 11705975, 10456947, 2882731, 7548539, 21829506.
**In vitro:** PMID 26633512, 32828915, 32860931, 8557365, 24349173.
**Structural/computational:** PMID 9699639, 24349173.
**Veterinary:** PMID 40989646, 42743700, 41133194, 42545146, 42651908.

*Report compiled from 11 confirmed findings and 46 reviewed papers over 5 investigation iterations.*


## Artifacts

- [OpenScientist final report](Gas_Gangrene-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Gas_Gangrene-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 23 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 7 |
| References weighed for topical relevance | 38 |
| On topic | 23 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26633512` *(abstract only)*: "is a key mediator of gas gangrene… manifest[ing] as fever, pain, edema, myonecrosis, and gas production. Alpha-toxin possesses phospholipase C and sphingomyelinase activities"
  - closest text in source: "Alpha-toxin possesses phospholipase C and sphingomyelinase activities"
- `PMID:32828915` *(abstract only)*: "specifically induces endothelial cell death by promoting ceramide-mediated apoptosis"
  - closest text in source: "Together, our results suggest that α-toxin-induced endothelial cell death promotes severe myonecrosis and is involved in the pathogenesis of C"
- `PMID:8557365` *(abstract only)*: "The toxin-induced expression of proadhesive and activational proteins and direct cytopathic effects may contribute to the leukostasis, vascular compromise, and capillary leak characteristic of C. perfringens gas gangrene"
  - closest text in source: "The toxin-induced expression of proadhesive and activational proteins and direct cytopathic effects may contribute to the leukostasis, vascular compromise, and capillary leak characteristics of C"
- `PMID:162815` *(abstract only)*: "Survival in patients with involvement confined to the extremities was 92.3 percent… combined involvement of extremity and trunk was 53.3 percent, and with primary trunk involvement half… survived. Survival for the entire series was 73.5 percent"
  - closest text in source: "Survival in patients with involvement confined to the extremities was 92.3 percent"
- `PMID:8373904` *(abstract only)*: "Serum PLC activity… showed a nearly fivefold increase (6.0 to 27.3 U/l), which is consistent with the hypothesized dominant role of this enzyme"
  - closest text in source: "Serum PLC activity, on the other hand, showed a nearly fivefold increase (6.0 to 27.3 U/l), which is consistent with the hypothesized dominant role of this enzyme."
- `PMID:10456947` *(abstract only)*: "significantly reduced leukocyte aggregation when alpha-toxin was absent and complete abrogation… when theta-toxin was absent. Thus, both alpha-toxin and theta-toxin are necessary for the characteristic vascular leukostasis"
  - closest text in source: "Thus, both alpha-toxin and theta-toxin are necessary for the characteristic vascular leukostasis observed in clostridial myonecrosis."
- `PMID:10621873` *(abstract only)*: "Tissue gas is not a universal finding in necrotizing soft tissue infections. This misconception… contributes to diagnostic errors. Incision and drainage is an inappropriate surgical strategy… excisional debridement is needed"
  - closest text in source: "Incision and drainage is an inappropriate surgical strategy for necrotizing soft tissue infections; excisional debridement is needed"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42743700` (10 mentions) - Spatiotemporal patterns and ecological niche modeling of Blackleg in cattle in the Western Amhara region, Ethiopia, 2018-2023.
  - shared terms: disease
- `PMID:41133194` (7 mentions) - Blackleg in cattle in Kazakhstan: regional epizootology, seasonal patterns, and molecular identification of the pathogen.
  - shared terms: clinical, genetic

Weighed against this report's own most characteristic terms: `gas`, `human`, `septicum`, `disease`, `gangrene`, `perfringen`, `alpha-toxin`, `plc`, `tissue`, `hemolysis`, `toxin`, `model`, `clinical`, `myonecrosis`, `muscle`, `spontaneous`, `debridement`, `genetic`, `malignancy`, `edema`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 34 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012531` (1 mention) - the report calls it "Early, near-universal"; HP calls it **Pain**
- `HP:0003202` (1 mention) - the report calls it "proxy"; HP calls it **Skeletal muscle atrophy**
- `HP:0025439` (1 mention) - the report calls it "Variable — **not universal** (PMID: 10621873)"; HP calls it **Pharyngitis**
- `HP:0000969` (1 mention) - the report calls it "Severe, progressive (PMID: 11111933)"; HP calls it **Edema**
- `HP:0011121` (1 mention) - the report calls it "Progressive"; HP calls it **Abnormal skin morphology**
- `HP:0001945` (1 mention) - the report calls it "Common"; HP calls it **Fever**
- `HP:0031273` (1 mention) - the report calls it "Late/systemic"; HP calls it **Shock**
- `HP:0001878` (1 mention) - the report calls it "Rare (~3%), often fatal (PMID: 27049736)"; HP calls it **Hemolytic anemia**
- `HP:0005521` (1 mention) - the report calls it "Severe complication (PMID: 9163265)"; HP calls it **Disseminated intravascular coagulation**
- `UBERON:0007844` (2 mentions) - the report calls it "fascia"; UBERON calls it **cartilage element**
- `CHEBI:16040` (1 mention) - the report calls it "ceramide"; CHEBI calls it **cytosine**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1504` (1 mention) - the report calls it "C. septicum"; NCBITaxon calls it **Clostridium septicum**
- `GO:0004629` (2 mentions) - the report calls it "phospholipase C activity"; GO calls it **C-type glycerophospholipase activity**, and lists "phospholipase C activity" among its other names
- `GO:0006915` (2 mentions) - the report calls it "Cellular processes:** apoptosis", "apoptosis"; GO calls it **apoptotic process**, and lists "activation of apoptosis" among its other names
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0001134` (2 mentions) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `CHEBI:17636` (1 mention) - the report calls it "sphingomyelin"; CHEBI calls it **sphingomyelin d18:1**, and lists "Sphingomyelin" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006915` - called "Cellular processes:** apoptosis", "apoptosis"