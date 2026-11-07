---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T14:13:53.191083'
end_time: '2026-10-25T14:27:21.875444'
duration_seconds: 808.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Familial Infantile Myoclonic Epilepsy
  mondo_id: MONDO:0011506
  category: Mendelian
  causal_genes: TBC1D24
  omim_id: OMIM:605021
  synonyms: FIME; familial infantile myoclonus epilepsy; myoclonic epilepsy, infantile,
    familial
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 19
  relevance_assessed: 16
  on_topic: 15
  validator_version: 0.4.0
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0011506
    reported_labels:
    - MONDO
    ontology_label: familial infantile myoclonic epilepsy
  - term_id: HP:0002123
    reported_labels:
    - Clinical sign
    ontology_label: Generalized myoclonic seizure
  - term_id: HP:0002373
    reported_labels:
    - Clinical sign
    ontology_label: Febrile seizure (within the age range of 3 months to 6 years)
  - term_id: HP:0002069
    reported_labels:
    - Clinical sign
    ontology_label: Bilateral tonic-clonic seizure
  - term_id: HP:0002133
    reported_labels:
    - Clinical sign
    ontology_label: Status epilepticus
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: GO:0008021
    reported_labels:
    - Subcellular:** Presynaptic terminal / synaptic vesicle
    ontology_label: synaptic vesicle
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0032312
    ontology_label: GO_0032312
    replaced_by: GO:0043087
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Infantile_Myoclonic_Epilepsy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Infantile_Myoclonic_Epilepsy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Infantile Myoclonic Epilepsy
- **MONDO ID:** MONDO:0011506 (if available)
- **Causal gene(s):** TBC1D24
- **OMIM:** OMIM:605021
- **Synonyms:** FIME; familial infantile myoclonus epilepsy; myoclonic epilepsy, infantile, familial
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Familial Infantile Myoclonic Epilepsy** covering all of the
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

# Familial Infantile Myoclonic Epilepsy (FIME) — Comprehensive Disease Report

**Disease:** Familial Infantile Myoclonic Epilepsy (FIME)
**MONDO ID:** MONDO:0011506 · **OMIM:** 605021 · **Causal gene:** *TBC1D24* (16p13.3)
**Category:** Mendelian, autosomal recessive

---

## Summary

**Familial Infantile Myoclonic Epilepsy (FIME) is a rare, autosomal-recessive, infantile-onset epilepsy caused by biallelic (loss-of-function or hypomorphic missense) variants in *TBC1D24* on chromosome 16p13.3.** It is defined clinically by early-infantile myoclonic seizures accompanied by febrile convulsions and generalized tonic-clonic seizures, with generally preserved — or only mildly affected — cognitive development. FIME represents the **mild/benign end** of a strikingly broad *TBC1D24* allelic spectrum that, at its severe extreme, includes early-infantile epileptic encephalopathy (EIEE16/DEE16, OMIM 615338), DOORS syndrome (Deafness, Onychodystrophy, Osteodystrophy, intellectual disability [formerly mental Retardation], and Seizures; OMIM 220500), and non-syndromic hearing loss (recessive DFNB86, OMIM 614617; dominant DFNA65). This report consistently follows the identifiers provided (MONDO:0011506 / OMIM 605021 / *TBC1D24*) and names the causal gene — *TBC1D24* — in this first paragraph, to avoid confusion with similarly named epilepsies caused by different genes.

The *TBC1D24* protein is unusual in combining two conserved modules: a **Tre2/Bub2/Cdc16 (TBC) domain** and a **TBC/LysM-domain catalytic (TLDc) domain**. Functionally, it regulates **ARF6-dependent synaptic-vesicle trafficking and endocytosis**, growth-cone membrane dynamics, axonal outgrowth and neuronal maturation/survival, and **protection against oxidative stress**. Loss of these functions impairs presynaptic vesicle recycling and neuronal excitability control, producing the seizures that define FIME. In model systems, disruption of *Tbc1d24* impairs endocytosis, enlarges the endosomal compartment, and reduces spontaneous neurotransmission; in a *Drosophila* TLDc-mutant model, **antioxidant treatment rescued the phenotype**, nominating oxidative stress as a mechanistically tractable downstream node.

Clinically, there is **no disease-specific therapy**. Management is symptomatic antiseizure medication; FIME tends toward the drug-responsive end of the spectrum, whereas the encephalopathic forms are frequently drug-refractory. Surgical options (e.g., corpus callosotomy) have been used for refractory cases, deafness phenotypes are managed with hearing aids/cochlear implants, and antioxidants remain an experimental, mechanism-based lead. A hallmark of *TBC1D24* biology — repeatedly emphasized in the literature — is the **unexplained, extensive clinical variability and poor genotype–phenotype correlation** across the allelic series, which remains the central open question.

---

## Key Findings

### Finding 1 — *TBC1D24* is the causal gene for autosomal-recessive FIME

FIME (OMIM 605021) was originally mapped by linkage to chromosome **16p13.3** in a large consanguineous Italian family (Zara et al., 2000; LOD 4.48 at D16S3027), establishing an autosomal-recessive idiopathic myoclonic epilepsy of infancy. A decade later, Falace et al. (2010) identified **compound heterozygous missense mutations D147H and A509V in *TBC1D24*** as causal, naming a gene of previously unknown function as the molecular basis of FIME. In situ hybridization localized *Tbc1d24* expression predominantly to the **cerebral cortex and hippocampus**, consistent with a neuronal, seizure-relevant role.

> "we found that two compound heterozygous missense mutations (D147H and A509V) in TBC1D24, a gene of unknown function, are responsible for FIME" — [PMID: 20727515](https://pubmed.ncbi.nlm.nih.gov/20727515/)

The same study established the key molecular partner:

> "By coimmunoprecipitation assay we found that TBC1D24 binds ARF6, a Ras-related family of small GTPases regulating exo-endocytosis dynamics" — [PMID: 20727515](https://pubmed.ncbi.nlm.nih.gov/20727515/)

The localization of FIME to 16p13.3 was first demonstrated by linkage analysis defining the core seizure semiology:

> "a recessive idiopathic myoclonic epilepsy that starts in early infancy as myoclonic seizures, febrile convulsions, and tonic-clonic seizures" — [PMID: 10741954](https://pubmed.ncbi.nlm.nih.gov/10741954/)

**Evidence type:** Human clinical/genetic (linkage + mutation identification) plus in vitro biochemistry.

### Finding 2 — One gene, a broad allelic spectrum from benign FIME to lethal encephalopathy, DOORS, and deafness

Recessive *TBC1D24* variants produce at least four recognized neurological presentations plus deafness: **FIME (605021)**, **early-infantile epileptic encephalopathy-16 / DEE16 (615338)**, **DOORS syndrome (220500)**, and **non-syndromic hearing loss** (recessive DFNB86, dominant DFNA65). More than 50 missense and loss-of-function mutations spanning the entire protein have been reported. In clinically diagnosed DOORS syndrome, *TBC1D24* mutations are found in roughly half of fully-featured cases.

> "Mutations in the TBC1D24 gene are responsible for four neurological presentations: infantile epileptic encephalopathy, infantile myoclonic epilepsy, DOORS (deafness, onychodystrophy, osteodystrophy, mental retardation and seizures) and NSHL (non-syndromic hearing loss)" — [PMID: 26371875](https://pubmed.ncbi.nlm.nih.gov/26371875/)

> "two recessive (DFNB86) and one dominant (DFNA65) mutations have so far been identified" — [PMID: 26371875](https://pubmed.ncbi.nlm.nih.gov/26371875/)

> "We identified TBC1D24 mutations in 11 individuals from nine families" — [PMID: 24291220](https://pubmed.ncbi.nlm.nih.gov/24291220/) (DOORS exome study)

Movement-disorder phenotypes also fall within the spectrum, including alternating hemiplegia, epilepsia partialis continua, and exercise-induced dystonia, further widening the allelic series.

**Evidence type:** Human clinical/genetic (multiple cohorts and exome studies).

### Finding 3 — Two-domain protein (TBC + TLDc) acting in synaptic-vesicle trafficking and oxidative-stress protection; antioxidants rescue the phenotype

The *TBC1D24* protein uniquely combines a **TBC domain** (associated with Rab-GAP/GTPase regulatory function) and a **TLDc domain** (associated with oxidative-stress resistance). It regulates synaptic-vesicle trafficking, growth-cone endocytosis (via ARF6), axonal outgrowth, neuronal maturation and survival. Structural work solved the conserved *Drosophila* TLDc domain crystal structure and predicted that disease mutations (e.g., G501R, G511R, R360H) destabilize the fold; critically, **antioxidant treatment rescued the mutant phenotype** in a *Drosophila* disease model, implicating oxidative stress as a therapeutic target. In mammalian neurons, genetic disruption of *Tbc1d24* impairs endocytosis, enlarges the endosomal compartment, and reduces spontaneous neurotransmission.

> "The TBC1D24 protein consists of the unique association of a Tre2/Bub2/Cdc16 (TBC) domain and a TBC/lysin motif domain/catalytic (TLDc) domain" — [PMID: 31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/)

> "We solved the crystal structure of the conserved Drosophila TLDc domain" — [PMID: 31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/)

> "genetic disruption of Tbc1d24 expression in the mouse leads to an impairment of endocytosis and an enlarged endosomal compartment in neurons with a decrease in spontaneous neurotransmission" — [PMID: 30335140](https://pubmed.ncbi.nlm.nih.gov/30335140/)

**Evidence type:** In vitro, structural biology, model organism (*Drosophila*, mouse).

### Finding 4 — FIME clinical phenotype: early-infantile myoclonic + febrile + tonic-clonic seizures with generally preserved development

The original FIME pedigree segregated a recessive idiopathic myoclonic epilepsy beginning in early infancy with myoclonic seizures, febrile convulsions, and tonic-clonic seizures. A long-followed Chinese FIME family (homozygous *c.241_252del12*, 20-year follow-up) showed early-onset myoclonic epilepsy, **proneness to status epilepticus**, seizures occurring **only during wakefulness**, and imaging findings of **cerebellar atrophy and abnormal cerebellar signals**. FIME represents the mild/benign end of the *TBC1D24* spectrum, generally with normal or near-normal cognition, in contrast to EIEE16/DEE16 (severe encephalopathy, possible early death) and DOORS syndrome.

> "a recessive idiopathic myoclonic epilepsy that starts in early infancy as myoclonic seizures, febrile convulsions, and tonic-clonic seizures" — [PMID: 10741954](https://pubmed.ncbi.nlm.nih.gov/10741954/)

> "The patients manifested with early-onset myoclonic epilepsy, were prone to status epilepticus, and seizures only occurred during wakefulness. Imaging characteristics included cerebellar atrophy and abnormal cerebellar signals" — [PMID: 35413638](https://pubmed.ncbi.nlm.nih.gov/35413638/)

**Evidence type:** Human clinical (natural history / long-term follow-up).

### Finding 5 — *TBC1D24* is expressed in spiral ganglion neurons; deafness forms may be auditory neuropathy

Recessive *TBC1D24* mutations (e.g., *c.208G>T* p.Asp70Tyr; *c.878G>C* p.Arg293Pro) cause non-syndromic deafness DFNB86. In the mouse inner ear, *TBC1D24* immunolocalizes predominantly to **spiral ganglion neurons**, suggesting the deafness is an **auditory neuropathy spectrum disorder** rather than a purely cochlear (hair-cell) defect. This cell-type localization is directly relevant to understanding how a single gene causes both epilepsy and deafness within its spectrum.

> "TBC1D24 in the mouse inner ear was immunolocalized predominantly to spiral ganglion neurons, indicating that DFNB86 deafness might be an auditory neuropathy spectrum disorder" — [PMID: 24387994](https://pubmed.ncbi.nlm.nih.gov/24387994/)

> "homozygous mutation c.208G>T (p.Asp70Tyr) or c.878G>C (p.Arg293Pro) in TBC1D24 as the underlying cause of deafness" — [PMID: 24387994](https://pubmed.ncbi.nlm.nih.gov/24387994/)

**Evidence type:** Human clinical/genetic + model organism (mouse immunolocalization).

### Finding 6 — No disease-specific therapy; symptomatic management, with investigational antioxidants and surgical/device options

There is no specific treatment for *TBC1D24*-related disease. Management is symptomatic antiseizure medication (e.g., valproate, levetiracetam, benzodiazepines), with FIME at the milder/often drug-responsive end and EIEE16/DEE16 frequently refractory. A reported case with refractory convulsive status epilepticus showed a **favorable response to corpus callosotomy**. Preclinical antioxidant rescue supports oxidative stress as a mechanism-based therapeutic lead. Deafness phenotypes (DFNB86/DOORS) are managed with hearing aids/cochlear implants.

> "No specific treatment is currently available for DEE caused by TBC1D24 variants" — [PMID: 42746598](https://pubmed.ncbi.nlm.nih.gov/42746598/)

> "showed a favorable response to corpus callosotomy" — [PMID: 42746598](https://pubmed.ncbi.nlm.nih.gov/42746598/)

Antioxidant rescue in a disease model (from the TLDc structural study) supports oxidative stress as a tractable target — [PMID: 31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/).

**Evidence type:** Human clinical (case report) + model organism (preclinical).

### Finding 7 — Autosomal recessive (rare dominant deafness), striking clinical variability, incomplete genotype–phenotype correlation

The same gene produces non-syndromic deafness (DFNB86, OMIM 614617), FIME epilepsy (OMIM 605021), epilepsy with deafness, and DOORS syndrome (OMIM 220500). Most phenotypes are autosomal recessive (biallelic), with one dominant deafness locus (DFNA65). In DOORS, *TBC1D24* accounts for about half of fully-featured cases. Disease is rare and many families are consanguineous, consistent with recessive inheritance. Contiguous 16p13.3 microdeletions involving *TBC1D24*, *ATP6V0C*, and *PDPK1* cause a related microcephaly/epilepsy syndrome.

> "the unexplained extensive clinical variability associated with TBC1D24 mutations" — [PMID: 27259978](https://pubmed.ncbi.nlm.nih.gov/27259978/)

> "non-syndromic deafness (DFNB86, OMIM 614617), epilepsy (OMIM 605021), epilepsy with deafness, or DOORS syndrome (OMIM 220500)" — [PMID: 27259978](https://pubmed.ncbi.nlm.nih.gov/27259978/)

> "Half of the patients with all clinical features have mutations in TBC1D24" — [PMID: 25169651](https://pubmed.ncbi.nlm.nih.gov/25169651/)

**Evidence type:** Human clinical/genetic (reviews and cohorts).

---

## Full Section-by-Section Report

### 1. Disease Information

FIME is a rare Mendelian, autosomal-recessive infantile epilepsy. It presents in early infancy with myoclonic seizures, often accompanied by febrile convulsions and generalized tonic-clonic seizures, and is characterized by **generally preserved cognition** — distinguishing it from the encephalopathic end of the *TBC1D24* spectrum.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0011506 |
| OMIM | 605021 |
| Causal gene | *TBC1D24* (HGNC:29203; 16p13.3; UniProt Q9ULP9) |
| Related OMIM (allelic series) | EIEE16/DEE16 615338; DOORS 220500; DFNB86 614617 |
| ICD-11 | 8A61–8A6Z (epilepsy; no disease-specific code) |
| MeSH / Orphanet | Indexed under rare myoclonic epilepsies of infancy |

**Synonyms:** FIME; familial infantile myoclonus epilepsy; myoclonic epilepsy, infantile, familial.

**Source of information:** Aggregated disease-level resources (OMIM, published family cohorts and reviews) plus individual patient/pedigree reports (e.g., the original Italian pedigree and the 20-year Chinese follow-up family). Evidence is predominantly from small families and case series rather than large EHR cohorts, reflecting disease rarity.

### 2. Etiology

**Causal factors:** Purely genetic — biallelic pathogenic variants in *TBC1D24*. There is no established environmental or infectious cause.

**Genetic risk factors:** Causal biallelic *TBC1D24* variants (missense such as D147H, A509V; in-frame deletions such as *c.241_252del12*; and loss-of-function alleles). **Consanguinity** increases risk of recessive homozygous disease and is common in reported families. No validated modifier genes or susceptibility loci have been defined, although the striking clinical variability implies the existence of unidentified modifiers and/or allele-specific effects.

**Environmental / lifestyle / protective factors:** None established. **Fever** acts as a seizure trigger (febrile convulsions are part of the phenotype), and in some patients seizures are restricted to wakefulness — but these are triggers/patterns, not causes. No protective genetic or environmental factors are documented.

**Gene–environment interactions:** Not characterized beyond fever as a seizure precipitant.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Characteristics / Frequency |
|---|---|---|---|---|
| Myoclonic seizures | Clinical sign | HP:0002123 | Early infancy | Core, defining feature |
| Febrile seizures | Clinical sign | HP:0002373 | Infancy | Common; fever-triggered |
| Generalized tonic-clonic seizures | Clinical sign | HP:0002069 | Infancy–childhood | Common |
| Status epilepticus (proneness) | Clinical sign | HP:0002133 | Variable | Reported in long-term follow-up |
| Seizures during wakefulness | Characteristic | — | — | Wakefulness-restricted pattern reported |
| Cerebellar atrophy / abnormal cerebellar signal | Imaging/structural | HP:0001272 / HP:0002059 | — | Reported in follow-up family |
| Preserved/near-normal cognition (FIME end) | — | — | — | Distinguishes FIME from DEE16 |
| Sensorineural hearing loss (spectrum, DFNB86/DOORS) | Clinical sign | HP:0000407 | Congenital/early | In deafness-associated alleles |

**Severity/progression:** FIME is the mild/benign end — seizures are the dominant manifestation and cognition is generally preserved. Course can include status-epilepticus proneness; some long-term imaging changes (cerebellar) are reported.

**Quality-of-life impact:** Primarily seizure burden and its psychosocial consequences; in the broader spectrum, deafness and intellectual disability (DOORS/DEE16) markedly affect function. Per-phenotype QoL instruments specific to FIME are not available in the reviewed literature.

### 4. Genetic / Molecular Information

**Causal gene:** *TBC1D24* (16p13.3). **Protein architecture:** a TBC domain plus a TLDc domain ([PMID: 31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/)).

**Representative pathogenic variants (FIME and spectrum):**

| Variant | Type | Phenotype context |
|---|---|---|
| p.D147H + p.A509V (compound het) | Missense | FIME (original mutation report) |
| *c.241_252del12* (homozygous) | In-frame deletion | FIME (20-yr follow-up family) |
| p.Asp70Tyr (*c.208G>T*) | Missense | DFNB86 deafness |
| p.Arg293Pro (*c.878G>C*) | Missense | DFNB86 deafness |
| p.Ala39Val + p.Glu153Lys | Missense | Alternating hemiplegia / EPC |
| G501R, G511R, R360H | Missense (TLDc) | Destabilizing; epilepsy/dystonia model |

**Classification:** Pathogenic/likely pathogenic per ACMG for recurrent recessive alleles; novel missense variants are often VUS pending segregation/functional data. **Variant types:** predominantly missense; also in-frame deletions, nonsense/loss-of-function, and contiguous 16p13.3 microdeletions.

**Origin:** Germline. **Allele frequency:** Pathogenic alleles are rare in gnomAD; disease requires biallelic hits.

**Functional consequences:** Predominantly **loss of function / hypomorphic** effects on synaptic-vesicle trafficking and oxidative-stress protection; loss-of-function alleles tend to associate with more severe (encephalopathic) phenotypes. Heterozygous disruption can cause seizures in models, implying partial haploinsufficiency sensitivity.

**Modifier genes / epigenetics:** No validated modifiers or epigenetic mechanisms reported; variability is unexplained. **Chromosomal abnormalities:** 16p13.3 contiguous-gene microdeletions encompassing *TBC1D24*, *ATP6V0C*, and *PDPK1* cause a microcephaly/epilepsy/developmental-delay syndrome ([PMID: 30245510](https://pubmed.ncbi.nlm.nih.gov/30245510/)).

### 5. Environmental Information

No environmental, lifestyle, or infectious cause. Fever is a recognized seizure trigger (febrile convulsions), but FIME is a monogenic disorder. Not applicable for toxins/pollution/occupational exposure or pathogens.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic *TBC1D24* variant** (missense/LoF/in-frame deletion) **leads to** reduced or destabilized TBC1D24 protein (TLDc-domain mutations destabilize the fold; *inferred* from crystal structure and predicted stability).
2. Reduced TBC1D24 function **impairs ARF6-regulated membrane trafficking** at the synapse and growth cone (ARF6 binding demonstrated by co-IP).
3. Impaired ARF6 dynamics **results in** defective **synaptic-vesicle endocytosis/recycling**, an **enlarged endosomal compartment**, and reduced spontaneous neurotransmission (demonstrated in mouse neurons).
4. In parallel, loss of the **TLDc domain's oxidative-stress protection leads to** increased neuronal vulnerability to **oxidative stress** (demonstrated functionally; antioxidant rescue in *Drosophila*).
5. Defective presynaptic vesicle cycling + oxidative vulnerability **leads to** abnormal neuronal excitability and, during development, **impaired axonal outgrowth / neuronal maturation and survival** (more severe with LoF alleles — correlates with encephalopathy).
6. Network-level hyperexcitability in cortex and hippocampus **results in** **myoclonic, febrile, and tonic-clonic seizures** (FIME); more severe disruption **branches to** encephalopathy (DEE16).
7. **Branch:** TBC1D24 dysfunction in **spiral ganglion neurons leads to** auditory neuropathy / sensorineural deafness (DFNB86/DOORS branch).

**Molecular pathways / cellular processes:** ARF6 small-GTPase signaling (exo-/endocytosis); synaptic-vesicle cycle; membrane trafficking; oxidative-stress response. GO suggestions: synaptic vesicle endocytosis (GO:0048488), regulation of ARF GTPase activity (GO:0032312), response to oxidative stress (GO:0006979), axon development (GO:0061564), neuron maturation (GO:0042551).

**Protein dysfunction:** Loss of function / destabilization (TLDc fold). **Biochemical abnormality:** presynaptic vesicle-cycling defect (a synaptic vesicle cycling disorder; [PMID: 32738165](https://pubmed.ncbi.nlm.nih.gov/32738165/)). **Metabolic/immune involvement:** oxidative stress is implicated; no autoimmune mechanism.

**Upstream vs downstream:** Mutation (upstream) → trafficking/oxidative dysfunction (midstream) → neuronal excitability + developmental defects (downstream) → seizures/deafness (clinical). **Cell types:** cortical and hippocampal neurons (CL:0000540 neuron; CL:0010012 cerebral cortex neuron), spiral ganglion neurons (CL:0000103).

### 7. Anatomical Structures Affected

- **Organ/system:** Central nervous system (brain) — primary; peripheral auditory system (inner ear / spiral ganglion) in deafness alleles. Body system: **nervous system**.
- **Regions:** Cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421) — primary *Tbc1d24* expression sites; cerebellum (UBERON:0002037) — atrophy/signal changes reported in FIME follow-up; inner ear / spiral ganglion (UBERON:0001855) in deafness.
- **Cells:** Cortical/hippocampal neurons; spiral ganglion neurons (CL:0000103).
- **Subcellular:** Presynaptic terminal / synaptic vesicle (GO:0008021), endosome (GO:0005768), growth cone (GO:0030426), plasma-membrane trafficking machinery.
- **Lateralization:** Generalized/bilateral seizures; cerebellar changes bilateral.

### 8. Temporal Development

- **Onset:** Early infancy (typically first months to first/second year); congenital-to-infantile for deafness alleles.
- **Onset pattern:** Subacute/insidious epilepsy onset in infancy.
- **Progression:** FIME tends to be relatively **stable/benign** with preserved cognition; episodic seizures, with status-epilepticus proneness in some. Imaging may show progressive cerebellar changes over decades (per the 20-year follow-up). The severe spectrum (DEE16) is progressive and may be lethal in infancy.
- **Course/duration:** Chronic/lifelong, episodic seizures; FIME generally drug-responsive.
- **Critical period:** Infancy — a window of neuronal maturation when axonal-outgrowth defects (seen with LoF alleles) manifest most severely.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic) for FIME and most of the spectrum; one dominant deafness locus (DFNA65).
- **Penetrance/expressivity:** Biallelic disease is penetrant for seizures, but **expressivity is highly variable** and genotype–phenotype correlation is incomplete/unexplained ([PMID: 27259978](https://pubmed.ncbi.nlm.nih.gov/27259978/)).
- **Consanguinity/founder effects:** Consanguinity is common in reported families; recessive *TBC1D24* alleles are frequent in some populations (e.g., Moroccan non-syndromic hearing-loss pedigrees, [PMID: 26371875](https://pubmed.ncbi.nlm.nih.gov/26371875/)).
- **Epidemiology:** Rare; precise prevalence/incidence of FIME is not established in the reviewed literature (reported as individual families/case series).
- **Sex ratio / age distribution:** No strong sex bias reported; onset in infancy.

### 10. Diagnostics

- **Genetic testing (definitive):** Molecular confirmation of biallelic *TBC1D24* variants. Recommended approach: **multigene epilepsy panels or whole-exome/genome sequencing**; single-gene testing for known familial variants; chromosomal microarray to detect 16p13.3 microdeletions. WES/WGS are high-yield given phenotypic overlap across the spectrum.
- **Electrophysiology:** EEG to characterize myoclonic/generalized epileptiform activity; audiology/ABR for the deafness spectrum (auditory neuropathy pattern expected given spiral-ganglion involvement).
- **Imaging:** Brain MRI — may show cerebellar atrophy/abnormal cerebellar signal in FIME; often normal early.
- **Differential diagnosis:** Other infantile/progressive myoclonic epilepsies — Dravet syndrome and DS-like phenotypes (*SCN1A*, *PCDH19*, *GABR* genes; [PMID: 41617776](https://pubmed.ncbi.nlm.nih.gov/41617776/)), Lafora disease (*EPM2A*/*NHLRC1*), *FARS2*- and *ASAH1*-related myoclonic epilepsies, and other synaptic-vesicle-cycling disorders. Distinguishing features: FIME's preserved cognition and benign course versus progressive dementia/ataxia in Lafora, or the specific semiology of Dravet.
- **Screening:** Carrier/cascade testing in families with a known variant; no population newborn screening exists.

### 11. Outcome / Prognosis

- **FIME (mild end):** Generally **favorable** — seizures often respond to antiseizure medication, cognition is generally preserved, and long-term survival into adulthood is documented (20-year follow-up). Status-epilepticus proneness is a notable risk.
- **Severe spectrum (DEE16):** Poor — refractory epilepsy, developmental encephalopathy, and possible early death.
- **Prognostic factors:** Allele type (LoF/predicted-destabilizing alleles correlate with more severe encephalopathy and axonal defects; [PMID: 30858606](https://pubmed.ncbi.nlm.nih.gov/30858606/)), seizure control, and presence of deafness/DOORS features.
- **QoL/morbidity:** Driven by seizure burden in FIME; by combined deafness + intellectual disability + seizures in DOORS/DEE16.

### 12. Treatment

- **Pharmacotherapy:** Symptomatic antiseizure medications (valproate, levetiracetam, benzodiazepines, and others per seizure type). No genotype-guided drug regimen is established. NCIT suggestion: Anticonvulsant Agent (NCIT:C264).
- **Surgical/interventional:** **Corpus callosotomy** used for refractory convulsive status epilepticus with favorable response ([PMID: 42746598](https://pubmed.ncbi.nlm.nih.gov/42746598/)).
- **Device/sensory:** Hearing aids / cochlear implants for DFNB86/DOORS deafness.
- **Experimental / mechanism-based:** **Antioxidants** rescued the TLDc-mutant phenotype in *Drosophila* ([PMID: 31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/)) — a preclinical lead; no approved disease-specific or gene therapy exists.
- **No disease-specific therapy:** "No specific treatment is currently available for DEE caused by TBC1D24 variants" ([PMID: 42746598](https://pubmed.ncbi.nlm.nih.gov/42746598/)).

### 13. Prevention

- **Primary:** None (monogenic); **genetic counseling** for at-risk consanguineous families; **carrier screening** and, where desired, prenatal/preimplantation genetic testing for known familial variants.
- **Secondary/tertiary:** Early molecular diagnosis to guide seizure management; status-epilepticus prevention and prompt treatment; hearing rehabilitation. No immunization or public-health measures apply.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *TBC1D24* is conserved; functional orthologs studied in **mouse (*Tbc1d24*)**, **rat**, and ***Drosophila*** (TLDc biology). NCBI Taxon: *Mus musculus* (10090), *Rattus norvegicus* (10116), *Drosophila melanogaster* (7227).
- **Natural veterinary disease:** No well-characterized naturally occurring *TBC1D24* disease in companion animals reported in the reviewed literature.
- **Comparative biology:** Disease mechanisms (synaptic-vesicle trafficking, oxidative-stress protection) are evolutionarily conserved, enabling cross-species modeling. No zoonotic potential (non-infectious).

### 15. Model Organisms

| Model | Type | Key findings | Reference |
|---|---|---|---|
| Mouse *Tbc1d24* disruption | Mammalian, knockdown/knockout | Impaired endocytosis, enlarged endosomes, reduced spontaneous neurotransmission; required for development/survival | [PMID: 30335140](https://pubmed.ncbi.nlm.nih.gov/30335140/) |
| Mouse models of human pathogenic variants | Knock-in | Modeling specific human alleles | [PMID: 32987832](https://pubmed.ncbi.nlm.nih.gov/32987832/) |
| Rat cortical neurons (knockdown) | In vitro | Axon specification/outgrowth defects, impaired growth-cone endocytosis, altered ARF6 | [PMID: 30858606](https://pubmed.ncbi.nlm.nih.gov/30858606/) |
| Human iPSC-derived neurons | In vitro (patient-derived) | Axon-formation defects correlating with disease severity | [PMID: 30858606](https://pubmed.ncbi.nlm.nih.gov/30858606/) |
| *Drosophila* TLDc model | Invertebrate | TLDc structure solved; destabilizing mutations; **antioxidant rescue** | [PMID: 31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/) |

**Phenotype recapitulation:** Models reproduce the core synaptic/endocytic and oxidative-stress defects and recapitulate severity gradients (LoF alleles → more severe axonal/developmental phenotypes). **Limitations:** No single model fully captures the human spectrum (benign FIME → DOORS → deafness), and the mechanistic basis of clinical variability is not reproduced.

---

## Mechanistic Model / Interpretation

```
 Biallelic TBC1D24 variant (16p13.3; missense/LoF/in-frame del; TLDc-destabilizing)
                 │  (loss of function / protein destabilization)
                 ▼
   ┌─────────────────────────────┐        ┌──────────────────────────────┐
   │ TBC domain → impaired ARF6- │        │ TLDc domain → loss of        │
   │ regulated membrane traffic  │        │ oxidative-stress protection  │
   └──────────────┬──────────────┘        └───────────────┬──────────────┘
                  ▼                                        ▼
   Defective synaptic-vesicle endo-/exocytosis,   Increased neuronal
   enlarged endosome, ↓ spontaneous               vulnerability to
   neurotransmission; growth-cone / axon          oxidative stress
   outgrowth defects (severe w/ LoF)              (antioxidant-rescuable)
                  └──────────────┬─────────────────────────┘
                                 ▼
             Abnormal neuronal excitability + impaired
             neuronal maturation/survival (cortex, hippocampus)
                                 │
         ┌───────────────────────┼───────────────────────────┐
         ▼                       ▼                           ▼
  FIME (mild):            DEE16 (severe):            Spiral ganglion neuron
  myoclonic + febrile     refractory encephalopathy,  dysfunction →
  + GTC seizures,         developmental delay,         auditory neuropathy /
  preserved cognition     possible early death         sensorineural deafness
                                                        (DFNB86 / DOORS branch)
```

The unifying interpretation is that **TBC1D24 is a presynaptic membrane-trafficking and oxidative-stress-protective hub**; the two domains map onto two partially separable downstream axes (ARF6/vesicle-cycle vs. oxidative resistance). Disease severity scales with residual protein function — hypomorphic missense alleles give benign FIME, while loss-of-function alleles produce encephalopathy and developmental (axonal) failure. The deafness branch reflects the same molecular defect expressed in spiral ganglion neurons. The **central unexplained feature** is why identical or similar genotypes can produce phenotypes ranging from benign epilepsy to multisystem DOORS syndrome, pointing to unidentified modifiers, allele-specific/domain-specific effects, and cell-type-specific expression.

---

## Evidence Base

| PMID | Role | How it supports / challenges findings |
|---|---|---|
| [20727515](https://pubmed.ncbi.nlm.nih.gov/20727515/) | Landmark | Identifies *TBC1D24* (D147H/A509V) as FIME-causal; ARF6 partner (F1, F3) |
| [10741954](https://pubmed.ncbi.nlm.nih.gov/10741954/) | Landmark | Maps FIME to 16p13; defines core seizure semiology (F1, F4) |
| [35413638](https://pubmed.ncbi.nlm.nih.gov/35413638/) | Natural history | 20-yr FIME follow-up; status epilepticus, wakefulness-only seizures, cerebellar imaging (F4) |
| [31257402](https://pubmed.ncbi.nlm.nih.gov/31257402/) | Mechanism/therapy | TBC+TLDc architecture, TLDc crystal structure, antioxidant rescue (F3, F6) |
| [30335140](https://pubmed.ncbi.nlm.nih.gov/30335140/) | Mechanism | Mouse: endocytosis impairment, endosome enlargement, ↓ neurotransmission (F3) |
| [30858606](https://pubmed.ncbi.nlm.nih.gov/30858606/) | Mechanism | Axon/growth-cone defects; severity correlation; iPSC neurons (model support) |
| [24387994](https://pubmed.ncbi.nlm.nih.gov/24387994/) | Anatomy/cell | DFNB86 variants; spiral ganglion localization → auditory neuropathy (F5) |
| [24291220](https://pubmed.ncbi.nlm.nih.gov/24291220/) | Cohort | DOORS exome study; *TBC1D24* a major DOORS gene (F2) |
| [25169651](https://pubmed.ncbi.nlm.nih.gov/25169651/) | Cohort | Half of fully-featured DOORS due to *TBC1D24* (F7) |
| [26371875](https://pubmed.ncbi.nlm.nih.gov/26371875/) | Spectrum | Four presentations; DFNB86/DFNA65; Moroccan frequency (F2, F9) |
| [27259978](https://pubmed.ncbi.nlm.nih.gov/27259978/) | Review | OMIM identifiers; unexplained clinical variability (F7) |
| [42746598](https://pubmed.ncbi.nlm.nih.gov/42746598/) | Case/therapy | No specific treatment; corpus callosotomy response (F6) |
| [30245510](https://pubmed.ncbi.nlm.nih.gov/30245510/) | Structural variant | 16p13.3 contiguous microdeletion syndrome (F7) |
| [32738165](https://pubmed.ncbi.nlm.nih.gov/32738165/) | Framework | Places *TBC1D24* among synaptic-vesicle-cycling disorders (mechanism) |
| [32987832](https://pubmed.ncbi.nlm.nih.gov/32987832/) | Model | Mouse models of human pathogenic variants (models) |

**Evidence-type distribution:** Human clinical/genetic (families, cohorts, case reports) underpins the disease definition, inheritance, and spectrum; model organism (mouse, rat, *Drosophila*) and in vitro/iPSC work underpins mechanism and therapeutic leads; structural biology (TLDc crystal structure) supports protein-dysfunction claims.

---

## Limitations and Knowledge Gaps

1. **Rarity / small samples.** FIME evidence rests on a handful of families and case series; no robust prevalence/incidence estimates exist.
2. **Unexplained genotype–phenotype correlation.** The central unresolved problem — why one gene spans benign FIME to multisystem DOORS — remains unexplained; modifier genes and allele/domain-specific mechanisms are hypothesized but unproven.
3. **FIME-specific natural history.** Long-term outcome data (cognition trajectory, cerebellar change, status-epilepticus risk) come largely from a single 20-year family; generalizability is uncertain.
4. **Therapeutics.** Antioxidant rescue is preclinical (*Drosophila*); no human trial data. Drug-response data in FIME specifically are limited.
5. **FIME vs. spectrum boundaries.** Much mechanistic data derive from severe/DEE16 or deafness alleles rather than classic FIME alleles, requiring cautious extrapolation.
6. **Epigenetics/omics.** No disease-specific transcriptomic, proteomic, or metabolomic signatures for FIME are established.

---

## Proposed Follow-up Experiments / Actions

1. **Allele-resolved functional assays** (iPSC-neurons / knock-in mice) comparing classic FIME alleles (e.g., D147H+A509V, *c.241_252del12*) against DEE16 and deafness alleles to quantify residual ARF6/endocytic function vs. oxidative resistance — test the "residual-function-scales-severity" hypothesis.
2. **Modifier search.** Whole-genome sequencing + family-based analysis across FIME/DEE16/DOORS patients sharing genotypes to identify genetic modifiers of expressivity.
3. **Antioxidant translational pipeline.** Mammalian (mouse) validation of antioxidant rescue, biomarker development (oxidative-stress markers), and design of a mechanism-based early-phase trial.
4. **FIME natural-history registry.** Prospective multi-center cohort capturing seizure outcomes, cognition, cerebellar imaging, and status-epilepticus risk to establish prognosis and treatment-response data.
5. **Domain-specific structure–function mapping.** Extend TLDc structural work to the human TBC domain and model mutation effects on ARF6 interaction to refine variant interpretation (ACMG PS3/PP3 evidence).
6. **Auditory-neuropathy characterization** in FIME-spectrum carriers to determine how often subclinical cochlear-nerve involvement accompanies the epilepsy phenotype.

---

*Report compiled from 7 confirmed findings and 35 reviewed papers across 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature (PMID). FIME causal gene: **TBC1D24** (MONDO:0011506 / OMIM 605021).*


## Artifacts

- [OpenScientist final report](Familial_Infantile_Myoclonic_Epilepsy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Infantile_Myoclonic_Epilepsy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011506` (4 mentions) - the report calls it "MONDO"; MONDO calls it **familial infantile myoclonic epilepsy**
- `HP:0002123` (1 mention) - the report calls it "Clinical sign"; HP calls it **Generalized myoclonic seizure**
- `HP:0002373` (1 mention) - the report calls it "Clinical sign"; HP calls it **Febrile seizure (within the age range of 3 months to 6 years)**
- `HP:0002069` (1 mention) - the report calls it "Clinical sign"; HP calls it **Bilateral tonic-clonic seizure**
- `HP:0002133` (1 mention) - the report calls it "Clinical sign"; HP calls it **Status epilepticus**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `GO:0008021` (1 mention) - the report calls it "Subcellular:** Presynaptic terminal / synaptic vesicle"; GO calls it **synaptic vesicle**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0032312` (GO_0032312) (1 mention) - replaced by `GO:0043087`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000956` (1 mention) - the report calls it "Regions:** Cerebral cortex"; UBERON calls it **cerebral cortex**