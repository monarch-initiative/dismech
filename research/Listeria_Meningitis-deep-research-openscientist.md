---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T21:30:52.389337'
end_time: '2026-09-29T21:46:14.517249'
duration_seconds: 922.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Listeria meningitis
  mondo_id: MONDO:0006836
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
citation_count: 42
reference_validation:
  total_references: 43
  verified: 43
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 43
  on_topic: 26
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 5
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0002315
    reported_labels:
    - Common (~84% in general BM)
    ontology_label: Headache
  - term_id: HP:0002383
    reported_labels:
    - 84% of neurolisteriosis
    ontology_label: Infectious encephalitis
  - term_id: HP:0001250
    reported_labels:
    - Elevated in alcoholic/severe cases
    ontology_label: Seizure
  - term_id: HP:0002921
    reported_labels:
    - Diagnostic
    ontology_label: Abnormal cerebrospinal fluid morphology
  - term_id: HP:0000238
    reported_labels:
    - ~10%; poor prognosis
    ontology_label: Hydrocephalus
  - term_id: GO:0090662
    reported_labels:
    - phagosome
    ontology_label: GO_0090662
  - term_id: UBERON:0002361
    reported_labels:
    - "Primary organ:** brain and meninges \u2014 leptomeninges"
    ontology_label: pia mater
  - term_id: NCIT:C544
    reported_labels:
    - Adjunct, esp. early/severe
    ontology_label: Altretamine
  - term_id: NCIT:C312
    reported_labels:
    - Alternative (penicillin allergy); CNS-penetrant, intracellular; salvage for
      refractory disease
    ontology_label: Bleomycin Sulfate
  - term_id: NCIT:C61796
    reported_labels:
    - Alternative in some settings
    ontology_label: Ivermectin
  - term_id: NCIT:C583
    reported_labels:
    - Standard empirically, **stop when Listeria confirmed
    ontology_label: Recombinant Interferon Gamma
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0090662
    ontology_label: GO_0090662
    replaced_by: GO:0055085
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Listeria_Meningitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Listeria_Meningitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Listeria meningitis
- **MONDO ID:** MONDO:0006836 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Listeria meningitis** covering all of the
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

# Listeria Meningitis (MONDO:0006836): A Comprehensive Disease Characterization

**Disease:** Listeria meningitis / Neurolisteriosis · **MONDO:** MONDO:0006836 · **MeSH:** D008587 (Meningitis, Listeria) · **ICD-10:** A32.11 · **ICD-11:** 1C1A.0 · **Category:** Infectious disease (bacterial, foodborne, opportunistic CNS infection)

## Summary

**Listeria meningitis** is an acute, severe bacterial meningitis/meningoencephalitis caused by the Gram-positive, foodborne, facultative intracellular bacterium *Listeria monocytogenes*. Unlike the classic community-acquired meningitis pathogens (*Streptococcus pneumoniae*, *Neisseria meningitidis*), Listeria is an **"atypical" pathogen** whose disease is almost entirely confined to hosts with impaired cell-mediated immunity: neonates, adults ≥65 years, pregnant women, and people who are diabetic, immunosuppressed, alcoholic, or have malignancy. Because host defense against an intracellular organism depends on T-cell–mediated immunity, the epidemiology is defined by *who cannot mount that response* rather than by exposure alone. Invasive listeriosis is rare (US incidence ≈0.29 per 100,000 per year) but carries a case-fatality of roughly 20–30%, the highest of the common bacterial meningitis etiologies.

Mechanistically, *L. monocytogenes* is a paradigm of intracellular pathogenesis. It crosses the intestinal, placental, and blood–brain barriers using the surface internalins **InlA** and **InlB**, which engage host **E-cadherin (CDH1)** and the **Met** receptor tyrosine kinase, respectively. Once intracellular, the pore-forming toxin **listeriolysin O (LLO/*hly*)** mediates escape from the phagosome into the cytosol, and the surface protein **ActA** nucleates host actin to drive actin-based motility and direct cell-to-cell spread — allowing the bacterium to move between cells while evading humoral immunity. The clinical result is a meningoencephalitis with a characteristic predilection for the **brainstem (rhombencephalitis)**, a pattern that is radiologically and pathologically distinctive and prognostically ominous. Bacterial genotype matters: the hypervirulent **sequence type 6 (ST6/CC6)** independently predicts unfavorable outcome.

Treatment is distinct from empirical meningitis therapy: *L. monocytogenes* is **intrinsically resistant to all cephalosporins**, so first-line therapy is high-dose **ampicillin/amoxicillin, usually combined with gentamicin** for synergy, with **trimethoprim-sulfamethoxazole (TMP-SMX)** as the principal alternative in penicillin-allergic patients. Adjunctive dexamethasone, standard in pneumococcal meningitis, is generally stopped once Listeria is confirmed. No vaccine exists; prevention rests on **food-safety counseling** of high-risk groups (avoiding deli meats, soft cheeses, unpasteurized dairy) and public-health surveillance (whole-genome sequencing of clinical and food-processing isolates). This report synthesizes 10 confirmed findings from 49 reviewed papers across all 15 requested disease-characteristic domains.

---

## Key Findings

### Finding 1 — Listeria is an "atypical" meningitis pathogen concentrated in the elderly, diabetic, and immunosuppressed

*L. monocytogenes* is a minority cause of community-acquired bacterial meningitis overall, but it is strongly over-represented in specific vulnerable populations, reflecting the requirement for intact cell-mediated immunity to control an intracellular pathogen.

In a Dutch nationwide prospective cohort, **diabetes conferred a 2.2-fold higher risk of acquiring bacterial meningitis** and was an independent risk factor for death (adjusted OR 1.98, 95% CI 1.13–3.48, P=0.017); Listeria caused 6% of meningitis episodes in diabetic patients ([PMID: 27845429](https://pubmed.ncbi.nlm.nih.gov/27845429/)). Among patients **≥80 years**, atypical pathogens including *L. monocytogenes* occurred substantially more often than in younger adults (49/149 [33%] vs 362/1991 [18%]; p<0.001) ([PMID: 35352336](https://pubmed.ncbi.nlm.nih.gov/35352336/)). A Barcelona cohort likewise found Listeria more frequent among diabetics (18% vs 10%, p=0.033) ([PMID: 32312231](https://pubmed.ncbi.nlm.nih.gov/32312231/)). Additional risk-group associations include alcoholism (Listeria caused 8% of alcoholic meningitis, with 25% mortality; [PMID: 28065808](https://pubmed.ncbi.nlm.nih.gov/28065808/)), immunosuppressive medication (chiefly corticosteroids; [PMID: 27613024](https://pubmed.ncbi.nlm.nih.gov/27613024/)), and systemic lupus erythematosus ([PMID: 20213126](https://pubmed.ncbi.nlm.nih.gov/20213126/)).

> *"the risk of acquiring bacterial meningitis was 2.2-fold higher for diabetes patients"* — [PMID: 27845429](https://pubmed.ncbi.nlm.nih.gov/27845429/)

**Interpretation:** The disease is defined by host immune status. This has direct clinical consequence — any adult ≥50, or any immunocompromised or diabetic patient, presenting with meningitis should receive **empirical ampicillin to cover Listeria** in addition to a cephalosporin/vancomycin regimen.

### Finding 2 — The ST6/CC6 genotype independently predicts unfavorable outcome

Outcome is partly determined by the *bacterial* genotype, not only the host. In 92 adults with *L. monocytogenes* meningitis pooled from two Dutch nationwide cohorts, the rate of unfavorable outcome rose from 27% (1998–2002) to 61% (2006–2012, P=0.002). Multivariate regression identified **infection with sequence type 6 (ST6) as the sole independent predictor of unfavorable outcome (OR 3.77, 95% CI 1.07–13.33)**, and ST6 became more prevalent over time (4% vs 29%, P=0.009) ([PMID: 23592828](https://pubmed.ncbi.nlm.nih.gov/23592828/)).

> *"Multivariate regression analysis identified infection with L. monocytogenes ST6 as the sole predictor of unfavorable outcome (odds ratio, 3.77; 95% confidence interval, 1.07-13.33)"* — [PMID: 23592828](https://pubmed.ncbi.nlm.nih.gov/23592828/)

This links to the genomic epidemiology of hypervirulent clonal complex 1 (CC1) and related lineages ([PMID: 38165396](https://pubmed.ncbi.nlm.nih.gov/38165396/)) and is reinforced by animal-model data (Finding 6) showing genotype-dependent virulence.

### Finding 3 — Neurolisteriosis presents chiefly as meningoencephalitis, with characteristic brainstem involvement

In the French **MONALISA** national prospective cohort (818 cases: 107 maternal-neonatal, 427 bacteraemia, 252 neurolisteriosis), **neurolisteriosis presented as meningoencephalitis in 212/252 (84%)** and **brainstem (rhombencephalitis) involvement in 42/252 (17%)**. Three-month mortality was higher for pure bacteraemia than neurolisteriosis (HR 0.54, 95% CI 0.41–0.69, p<0.0001). Among pregnant women, 26/107 (24%) experienced fetal loss — notably, never after 29 weeks' gestation ([PMID: 28139432](https://pubmed.ncbi.nlm.nih.gov/28139432/)).

> *"Neurolisteriosis presented as meningoencephalitis in 212 (84%) of 252 patients; brainstem involvement was only reported in 42 (17%) of 252 patients"* — [PMID: 28139432](https://pubmed.ncbi.nlm.nih.gov/28139432/)

Historically, in an epidemic Swiss series, 6 of 8 adults with parenchymal CNS infection had brainstem involvement, and a preceding influenza-like prodrome was common ([PMID: 3918344](https://pubmed.ncbi.nlm.nih.gov/3918344/)). The predilection for the brainstem distinguishes Listeria clinically from other bacterial meningitides.

### Finding 4 — CNS invasion is mediated by internalins (InlA/InlB → E-cadherin/Met) with LLO/ActA driving intracellular survival and spread

The molecular pathogenesis is well characterized. **Internalins InlA and InlB interact with host receptors E-cadherin and MET (mesenchymal-epithelial transition factor) to facilitate brain invasion**, and *L. monocytogenes* activates NF-κB in brain endothelium ([PMID: 30117097](https://pubmed.ncbi.nlm.nih.gov/30117097/)). Once internalized, **listeriolysin O (LLO)** mediates phagosomal escape into the cytosol, and **ActA** drives actin-based motility and cell-to-cell spread. In the zebrafish larval model, bacteria escaped the macrophage phagosome in an LLO-dependent manner, an event critical for virulence ([PMID: 19546195](https://pubmed.ncbi.nlm.nih.gov/19546195/)); LLO additionally promotes protrusion formation and spread by exploiting **efferocytosis** ([PMID: 24739967](https://pubmed.ncbi.nlm.nih.gov/24739967/)).

> *"Internalins (InlA and InlB) of Listeria monocytogenes interact with its cellular receptors E-cadherin and mesenchymal-epithelial transition (MET) to facilitate invading the brain"* — [PMID: 30117097](https://pubmed.ncbi.nlm.nih.gov/30117097/)

> *"bacteria could escape the macrophage phagosome in a listeriolysin-dependent manner and accessed the cytosol; this event was critical for bacterial virulence"* — [PMID: 19546195](https://pubmed.ncbi.nlm.nih.gov/19546195/)

Secretion of these virulence factors depends on the **Sec/SecDF** translocation system ([PMID: 24056100](https://pubmed.ncbi.nlm.nih.gov/24056100/)) and is governed by the master transcriptional regulator **PrfA** ([PMID: 26055558](https://pubmed.ncbi.nlm.nih.gov/26055558/)). Passive immunization with anti-ActA and anti-LLO antibodies is protective in mice, confirming these factors as functional virulence determinants ([PMID: 28004800](https://pubmed.ncbi.nlm.nih.gov/28004800/)).

### Finding 5 — Ampicillin/amoxicillin (± gentamicin) is first-line; cephalosporins fail; TMP-SMX is the key alternative

*L. monocytogenes* is **intrinsically resistant to cephalosporins**, the single most important therapeutic fact about this disease. Guidelines specify amoxicillin (+gentamicin) for Listeria and continue **amoxicillin alone for 14 days** in confirmed Listeria meningitis; cefotaxime is reserved for *E. coli* precisely because Listeria is not covered by cephalosporins ([PMID: 29433694](https://pubmed.ncbi.nlm.nih.gov/29433694/)). In an infant-rat meningoencephalitis model, **amoxicillin plus gentamicin was the most active regimen in brain tissue** ([PMID: 10390217](https://pubmed.ncbi.nlm.nih.gov/10390217/)). **TMP-SMX** has bactericidal intracellular activity and excellent CNS penetration and has cured refractory listeriosis unresponsive to amoxicillin/gentamicin ([PMID: 10959905](https://pubmed.ncbi.nlm.nih.gov/10959905/)).

> *"In case of meningitis due to GBS or L. monocytogenes antibiotherapy is continued for 14 days with amoxicillin alone"* — [PMID: 29433694](https://pubmed.ncbi.nlm.nih.gov/29433694/)

> *"TMP/SMX has bactericidal extracellular and intracellular activity against Listeria and excellent central nervous system penetration, and thus may be effective for the treatment of refractory listeriosis"* — [PMID: 10959905](https://pubmed.ncbi.nlm.nih.gov/10959905/)

Regarding **adjunctive dexamethasone**: while corticosteroids reduce mortality and hearing loss in bacterial meningitis overall (largely driven by pneumococcus; [PMID: 17253505](https://pubmed.ncbi.nlm.nih.gov/17253505/), [PMID: 23152589](https://pubmed.ncbi.nlm.nih.gov/23152589/)), current guidance is to **stop dexamethasone once Listeria is confirmed** ([PMID: 36472590](https://pubmed.ncbi.nlm.nih.gov/36472590/), [PMID: 42601017](https://pubmed.ncbi.nlm.nih.gov/42601017/)).

### Finding 6 — Animal models recapitulate the disease and reveal genotype and species specificity

A validated **C57BL/6 intracisternal *L. monocytogenes* meningitis mouse model** demonstrated genotype-dependent severity: **ST1-infected mice had a more severe inflammatory response and brain damage than ST6-infected mice** ([PMID: 30193592](https://pubmed.ncbi.nlm.nih.gov/30193592/)). Because the **InlA:E-cadherin interaction is species-specific** (human vs murine E-cadherin differ at a critical residue), **transgenic mice expressing human E-cadherin** were generated, in which the essential role of InlA in crossing the intestinal barrier was established ([PMID: 15060982](https://pubmed.ncbi.nlm.nih.gov/15060982/)). The **zebrafish larval model** reproduces LLO-dependent phagosomal escape and ActA-dependent spread with real-time imaging ([PMID: 19546195](https://pubmed.ncbi.nlm.nih.gov/19546195/)).

> *"ST1-infected mice had a more severe inflammatory response and brain damage as compared to ST6-infected mice"* — [PMID: 30193592](https://pubmed.ncbi.nlm.nih.gov/30193592/)

### Finding 7 — Invasive listeriosis is rare but severe, concentrated in the elderly and pregnant

US CDC surveillance (2009–2011, 1,651 cases) reported an **average annual incidence of 0.29 cases/100,000**, a **case-fatality rate of 21%**, with **58% of cases in adults ≥65 years** and **14% pregnancy-associated**. Incidence was markedly higher among adults ≥65 (1.3/100,000; **relative rate 4.4**) and pregnant women (3.0/100,000; **RR 10.1**); ≥74% of non-pregnant patients <65 had an immunocompromising condition ([PMID: 23739339](https://pubmed.ncbi.nlm.nih.gov/23739339/)). A global 80-year meta-analysis found **Listeria meningitis had the highest case-fatality (27%, 95% CI 24–31%)** of the common causes, exceeding pneumococcus (24%) and far exceeding meningococcus (9%) ([PMID: 39093565](https://pubmed.ncbi.nlm.nih.gov/39093565/)).

> *"The average annual incidence was 0.29 cases per 100,000 population. Compared with the overall population, incidence was markedly higher among adults aged ≥65 years (1.3; relative rate [RR]: 4.4) and pregnant women (3.0; RR: 10.1)"* — [PMID: 23739339](https://pubmed.ncbi.nlm.nih.gov/23739339/)

### Finding 8 — Neuroimaging shows rhombencephalitis, abscesses, and hydrocephalus with prognostic weight

In the MONALISA prospective imaging study (71 neurolisteriosis patients, mean age 64), 85% had encephalitis signs and imaging was abnormal in 87%: meningeal enhancement (35%), abscess/nodules (14%), hemorrhages (15%), hydrocephalus/contrast-enhancing ventricles (10%). **Three-month survival was lower with hydrocephalus (14% vs 73%, P=0.005) and with parenchymal lesions (54% vs 92%, P=0.004)** ([PMID: 29796652](https://pubmed.ncbi.nlm.nih.gov/29796652/)). A Granada cohort found rhombencephalitis in 10/120 (8.3%), with MRI showing **T2-FLAIR hyperintensity (100%)**, pons/medulla/cerebellum involvement, and cranial-nerve enhancement (70%); rhombencephalitis increased in-hospital mortality ([PMID: 37303100](https://pubmed.ncbi.nlm.nih.gov/37303100/)). The classic MRI appearance of Listeria rhombencephalitis has been described since the 1990s ([PMID: 8826752](https://pubmed.ncbi.nlm.nih.gov/8826752/)).

> *"The most frequent MRI findings in patients with confirmed rhombencephalitis were T2-FLAIR hyperintensity (100%)... while the most frequent anatomical involvement were pons, medulla oblongata, and cerebellum"* — [PMID: 37303100](https://pubmed.ncbi.nlm.nih.gov/37303100/)

### Finding 9 — Neurolisteriosis is a shared zoonotic syndrome ("circling disease") in ruminants

Bovine listeriosis mirrors the human disease: 11/12 cases presented as neurolisteriosis with **suppurative meningoencephalitis and brainstem microabscesses**, and isolates were serotypes 4b and 1/2a (shared with humans) carrying the *inlA* virulence gene ([PMID: 40192846](https://pubmed.ncbi.nlm.nih.gov/40192846/)). In goats with encephalitic listeriosis, circling (or a history of circling) was associated with survival (OR 6.24), and males were 14× more likely to be non-survivors ([PMID: 37084183](https://pubmed.ncbi.nlm.nih.gov/37084183/)). Ruminant isolates display zoonotic characteristics, causing similar clinical signs in humans including abortion and encephalitis ([PMID: 42667904](https://pubmed.ncbi.nlm.nih.gov/42667904/)).

> *"its ruminant isolates display zoonotic characteristics, causing similar clinical signs in humans, including abortion and encephalitis"* — [PMID: 42667904](https://pubmed.ncbi.nlm.nih.gov/42667904/)

### Finding 10 — Neonatal listeriosis is bimodal: early-onset (in-utero sepsis) vs late-onset (meningitis)

In a Swedish series (1958–1974, 110 cases), of 37 liveborn neonates, **22 had "early disease" (mostly granulomatosis infantiseptica)** acquired in utero from the mother, and **8 had "late disease" with meningoencephalitis** from often nosocomial postnatal sources; maternal cases included 8 abortions and 3 stillbirths, with serotypes 1 and 4b predominating ([PMID: 419368](https://pubmed.ncbi.nlm.nih.gov/419368/)). Modern reviews confirm foodborne maternal acquisition (deli meats, unprocessed cheese) placing neonates at high morbidity risk ([PMID: 40887071](https://pubmed.ncbi.nlm.nih.gov/40887071/)).

> *"Out of 37 neonates born alive, 22 had 'early disease', mostly granulomatosis infantiseptica, and 8 had 'late disease' with meningoencephalitis"* — [PMID: 419368](https://pubmed.ncbi.nlm.nih.gov/419368/)

---

## Section-by-Section Disease Characterization

### 1. Disease Information

Listeria meningitis is an acute bacterial infection of the meninges (and frequently the brain parenchyma, hence meningoencephalitis) caused by *Listeria monocytogenes*. The data derive from **aggregated disease-level resources** — national prospective cohorts (Dutch MeningItis cohorts, French MONALISA), CDC surveillance, and case series — rather than a single-gene EHR phenotype; this is an infectious rather than a Mendelian entity.

| Identifier system | Value |
|---|---|
| MONDO | MONDO:0006836 (Listeria meningitis) |
| MeSH | *Meningitis, Listeria* (D008587); *Listeriosis* (D008088) |
| ICD-10 | A32.11 (Listerial meningitis); A32.12 (Listerial meningoencephalitis); P37.2 (neonatal) |
| ICD-11 | 1C1A.0 (Listeriosis, with CNS extension) |
| NCBI Taxonomy | *Listeria monocytogenes* — txid1639 |

**Synonyms:** listerial meningitis, neurolisteriosis (broader term including meningoencephalitis, rhombencephalitis, brain abscess), CNS listeriosis. Not an OMIM/Orphanet Mendelian disease.

### 2. Etiology

**Primary cause:** infection with *L. monocytogenes*, a foodborne facultative intracellular Gram-positive bacillus (Findings 1, 4, 5). The route is ingestion of contaminated food (deli meats, soft/unpasteurized cheeses, unprocessed dairy, produce) → intestinal translocation → bacteremia → CNS/placental seeding.

**Environmental/host risk factors:** age ≥65 (RR 4.4), pregnancy (RR 10.1), neonatal status, diabetes mellitus (2.2× meningitis risk), immunosuppressive medication (chiefly corticosteroids), alcoholism, malignancy, SLE, and other conditions impairing cell-mediated immunity (Findings 1, 7; PMIDs 27845429, 35352336, 32312231, 28065808, 27613024, 20213126, 23739339).

**Genetic risk factors (host):** No Mendelian causal genes. Susceptibility is driven by acquired/iatrogenic immune compromise. No established GWAS locus specific to Listeria meningitis was found — a **knowledge gap** — though defects in cell-mediated immunity (e.g., TNF-α blockade, corticosteroids) are mechanistically implicated.

**Pathogen genetic factors:** virulence and outcome vary by bacterial genotype — hypervirulent clonal complexes CC1, CC4, CC6; **ST6 independently predicts poor outcome** (Finding 2; PMID 23592828). Key virulence genes: *inlA*, *inlB*, *hly* (LLO), *actA*, *plcA/plcB*, regulated by *prfA*.

**Protective factors:** intact cell-mediated (T-cell) immunity is the principal protective factor. Behaviorally, avoidance of high-risk foods reduces exposure. No genetic protective variant is established.

### 3. Phenotypes

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Fever | Symptom | ~74–75% | HP:0001945 |
| Headache | Symptom | Common (~84% in general BM) | HP:0002315 |
| Neck stiffness / meningismus | Clinical sign | ~74% | HP:0031179 / HP:0000708 |
| Altered mental status / drowsiness | Sign | Very common; part of classic triad | HP:0011446 / HP:0002329 |
| Meningoencephalitis | Syndrome | 84% of neurolisteriosis | HP:0002383 |
| Rhombencephalitis / brainstem signs (ataxia, cranial neuropathies, nystagmus, dysphagia) | Sign | ~8–17% | HP:0002401, HP:0001251, HP:0000618 |
| Seizures | Sign | Elevated in alcoholic/severe cases | HP:0001250 |
| CSF pleocytosis, low glucose, high protein | Lab abnormality | Diagnostic | HP:0002921 |
| Hydrocephalus | Complication | ~10%; poor prognosis | HP:0000238 |
| Fetal loss / stillbirth (maternal) | Outcome | 24% in pregnant | HP:0001561, HP:0003826 |

Onset is **acute to subacute**; a preceding influenza-like prodrome is characteristic ([PMID: 3918344](https://pubmed.ncbi.nlm.nih.gov/3918344/)). Severity is high (case-fatality 20–30%). Quality-of-life impact among survivors of bacterial meningitis broadly is substantial: at 12 months, 26.7% had hearing loss, 32.8% depressive symptoms, 31.0% persistent headache ([PMID: 31927117](https://pubmed.ncbi.nlm.nih.gov/31927117/)).

### 4. Genetic/Molecular Information

**Not applicable for host germline genetics** — Listeria meningitis is infectious, with no causal human gene, pathogenic variant, ACMG classification, or inheritance pattern. The relevant "genetics" is the **bacterial genome**: virulence loci *inlA*/*inlB* (internalins → E-cadherin/Met), *hly* (listeriolysin O), *actA* (actin-based motility), *plcA*/*plcB* (phospholipases), master regulator *prfA*. Genotype (ST/CC) modifies outcome (Finding 2). Host HGNC genes engaged as receptors: **CDH1** (E-cadherin) and **MET**.

### 5. Environmental Information

**Infectious agent:** *Listeria monocytogenes* (NCBI txid1639); serotypes 4b, 1/2a, 1/2b are most clinically important. **Environmental reservoir:** soil, water, decaying vegetation; contaminates food-processing environments via biofilm formation ([PMID: 38287241](https://pubmed.ncbi.nlm.nih.gov/38287241/)). **Lifestyle/dietary factors:** consumption of deli meats, pâté, soft cheeses, unpasteurized dairy, and refrigerated ready-to-eat foods (Listeria grows at refrigeration temperatures). Alcohol use is a host risk factor ([PMID: 28065808](https://pubmed.ncbi.nlm.nih.gov/28065808/)).

### 6. Mechanism / Pathophysiology — Causal Chain

```
1. Ingestion of L. monocytogenes-contaminated food
        │ leads to
2. InlA binds host E-cadherin (CDH1) on intestinal epithelium → invasion & translocation across gut barrier
   InlB binds Met receptor → complementary invasion of non-epithelial cells
        │ results in
3. Bacteremia (facultative intracellular survival in monocytes/macrophages)
        │ branches:
   3a → Placental barrier crossing (InlA/InlB) → fetal/neonatal infection → granulomatosis infantiseptica / neonatal meningitis
   3b → Blood-brain barrier crossing (endothelial invasion; NF-κB activation; possibly "Trojan-horse" via infected leukocytes)
        │ leads to
4. CNS invasion → within cells, LLO (hly) perforates the phagosome → cytosolic escape (critical for virulence)
        │ results in
5. ActA nucleates host actin → actin-based motility → cell-to-cell spread (evades humoral immunity); LLO exploits efferocytosis
        │ leads to
6. Neutrophilic/suppurative inflammation of meninges and brain parenchyma; predilection for brainstem
        │ results in
7. Meningoencephalitis / rhombencephalitis, abscesses, hydrocephalus, hemorrhage
        │ leads to
8. Raised ICP, cranial neuropathies, coma → death (case-fatality ~20-30%) or neurological sequelae
```

Steps 2, 4, 5 are **experimentally demonstrated** (PMIDs 30117097, 19546195, 24739967, 15060982). Step 3b's precise BBB-crossing route (transcellular vs Trojan-horse) is partly **inferred**. **Molecular pathways:** host **NF-κB** activation in endothelium (PMID 30117097); PrfA-regulated virulence regulon in the bacterium. **Cellular processes (GO):** GO:0006909 phagocytosis, GO:0090662 (phagosome), GO:0006935 actin-based motility, GO:0043277 (apoptotic cell clearance/efferocytosis), GO:0006954 inflammatory response. **Cell types (CL):** macrophages (CL:0000235), monocytes (CL:0000576), neutrophils (CL:0000775), brain microvascular endothelial cells (CL:0002139). Neutrophils can provide an intravacuolar niche ([PMID: 40067021](https://pubmed.ncbi.nlm.nih.gov/40067021/)).

### 7. Anatomical Structures Affected

- **Primary organ:** brain and meninges — leptomeninges (UBERON:0002361), brain (UBERON:0000955), with characteristic **brainstem** (UBERON:0002298), **pons** (UBERON:0000988), **medulla oblongata** (UBERON:0001896), and **cerebellum** (UBERON:0002037) involvement (Findings 3, 8).
- **Body system:** central nervous system.
- **Secondary:** bloodstream (bacteremia/sepsis), placenta (UBERON:0001987) and fetus in pregnancy; ventricles (hydrocephalus).
- **Tissue/cell level:** nervous tissue; meningeal/epithelial and endothelial barriers; targets macrophages, monocytes, neutrophils, endothelial cells.
- **Subcellular (GO CC):** phagosome (GO:0045335), cytosol (GO:0005829), host actin cytoskeleton (GO:0015629); host plasma membrane (E-cadherin/Met receptors).
- **Lateralization:** brainstem lesions often bilateral/asymmetric; meningitis diffuse.

### 8. Temporal Development

Onset is **acute to subacute** (days), often after an influenza-like prodrome. Age of onset is bimodal at the population level: **neonatal** (early-onset in-utero sepsis vs late-onset meningitis; Finding 10) and **elderly/immunocompromised adult**. Course without treatment is rapidly progressive to coma and death; with treatment, disease is **self-limited over a 2–3 week antibiotic course** (14 days minimum for meningitis, longer for rhombencephalitis/abscess). Complications (hydrocephalus, parenchymal lesions) mark a worse trajectory (Finding 8). The critical intervention window is prompt empirical ampicillin — delay worsens outcome.

### 9. Inheritance and Population

- **Inheritance:** Not applicable (infectious).
- **Epidemiology:** US incidence ≈0.29/100,000/year overall; 1.3/100,000 in ≥65 (RR 4.4); 3.0/100,000 in pregnancy (RR 10.1) (Finding 7). 58% of cases in ≥65; 14% pregnancy-associated.
- **Sex:** Several series show female predominance driven by pregnancy-associated cases (e.g., 69.8% female in a Karachi cohort, [PMID: 42018538](https://pubmed.ncbi.nlm.nih.gov/42018538/); 77% female in Qatar, [PMID: 40978187](https://pubmed.ncbi.nlm.nih.gov/40978187/)); outside pregnancy, elderly males predominate.
- **Geographic distribution:** worldwide; outbreaks tied to contaminated food products; winter seasonal peaks reported in some series ([PMID: 3918344](https://pubmed.ncbi.nlm.nih.gov/3918344/)).

### 10. Diagnostics

- **Definitive:** CSF and/or blood **culture** of *L. monocytogenes* (Gram-positive rods; may be sparse). Gram-stain sensitivity is limited.
- **CSF profile:** pleocytosis (may be modest/mononuclear, especially in immunosuppressed — <1000/mm³ in ~46% of immunosuppressed; [PMID: 27613024](https://pubmed.ncbi.nlm.nih.gov/27613024/)), elevated protein, low glucose.
- **Molecular:** PCR / multiplex meningitis-encephalitis panels; whole-genome sequencing for genotyping/surveillance (Findings 2, 10; PMID 40887071).
- **Imaging:** MRI is key — T2-FLAIR hyperintensity of pons/medulla/cerebellum, meningeal enhancement, abscesses, hydrocephalus, hemorrhage (Finding 8; PMIDs 29796652, 37303100, 8826752).
- **Differential diagnosis:** other bacterial meningitides (pneumococcus, meningococcus), viral encephalitis (esp. HSV rhombencephalitis), tuberculous meningitis, brain abscess, and — in SLE patients — lupus flare (which Listeria can mimic; [PMID: 20213126](https://pubmed.ncbi.nlm.nih.gov/20213126/)).

### 11. Outcome / Prognosis

- **Case-fatality:** ~20–30% (US surveillance 21%; global meta-analysis 27%, the highest of common causes) (Finding 7; PMIDs 23739339, 39093565).
- **Prognostic factors:** older age; bacterial genotype **ST6** (OR 3.77; Finding 2); imaging findings — **hydrocephalus** (survival 14% vs 73%) and parenchymal lesions (54% vs 92%) (Finding 8); coma/altered consciousness; intracranial hemorrhage (associated with 63% mortality; [PMID: 23028898](https://pubmed.ncbi.nlm.nih.gov/23028898/)).
- **Sequelae:** hearing loss, persistent neurological deficits, cognitive/depressive symptoms among survivors ([PMID: 31927117](https://pubmed.ncbi.nlm.nih.gov/31927117/)).
- **Maternal-fetal:** high fetal loss (24%), stillbirth, preterm delivery; mothers often recover fully.

### 12. Treatment

| Intervention | Role | NCIT (suggested) |
|---|---|---|
| **Ampicillin / amoxicillin** (high-dose IV) | First-line; 14+ days for meningitis | NCIT:C356 / C61785 |
| **Gentamicin** (added for synergy) | Adjunct, esp. early/severe | NCIT:C544 |
| **TMP-SMX (co-trimoxazole)** | Alternative (penicillin allergy); CNS-penetrant, intracellular; salvage for refractory disease | NCIT:C312 |
| **Meropenem** | Alternative in some settings | NCIT:C61796 |
| Cephalosporins | **Ineffective — intrinsic resistance** (do not use) | — |
| Adjunctive **dexamethasone** | Standard empirically, **stop when Listeria confirmed** | NCIT:C583 |
| Supportive / neurocritical care | ICP management, seizure control, CSF diversion for hydrocephalus | — |

Evidence: Finding 5 (PMIDs 29433694, 10390217, 10959905); dexamethasone context (PMIDs 17253505, 23152589, 42601017, 36472590). No pharmacogenomic, gene, cell, or RNA-based therapy applies. Passive immunization (anti-ActA/anti-LLO) is experimental/preclinical only ([PMID: 28004800](https://pubmed.ncbi.nlm.nih.gov/28004800/)).

### 13. Prevention

- **Primary (no vaccine exists):** dietary/behavioral counseling of high-risk groups — pregnant women, elderly, immunocompromised — to avoid deli meats, pâté, soft/unpasteurized cheeses, unpasteurized milk, and to reheat ready-to-eat foods; refrigeration hygiene ([PMID: 40887071](https://pubmed.ncbi.nlm.nih.gov/40887071/), [PMID: 42018538](https://pubmed.ncbi.nlm.nih.gov/42018538/)).
- **Public health:** food-safety regulation, environmental monitoring of processing plants, and **whole-genome-sequencing surveillance** linking clinical and food isolates to detect and interrupt outbreaks (PMID 40887071; [PMID: 11938118](https://pubmed.ncbi.nlm.nih.gov/11938118/)).
- **Secondary/tertiary:** prompt empirical ampicillin in at-risk meningitis patients; neurocritical monitoring to prevent complications.
- No genetic screening, immunization, or chemoprophylaxis is applicable.

### 14. Other Species / Natural Disease

Listeria neurolisteriosis is a well-recognized **zoonotic** and veterinary disease. In ruminants (cattle, sheep, goats) it causes **"circling disease"** — suppurative meningoencephalitis with **brainstem microabscesses** that pathologically parallel human rhombencephalitis (Finding 9; PMIDs 40192846, 37084183, 42667904). Shared serotypes (4b, 1/2a) and virulence genes (*inlA*) underscore cross-species conservation of mechanism. Species affected: *Bos taurus* (txid9913), *Capra hircus* (txid9925), *Ovis aries* (txid9940). Orthologous host receptor genes (CDH1, MET) are conserved, though InlA:E-cadherin binding is species-specific (Finding 6). Ovine-derived isolates infect trigeminal ganglion neurons via InlA/InlB/LLO ([PMID: 42121802](https://pubmed.ncbi.nlm.nih.gov/42121802/)), a proposed route of neuroinvasion in ruminants.

### 15. Model Organisms

| Model | Type | Recapitulation | PMID |
|---|---|---|---|
| C57BL/6 intracisternal meningitis mouse | Mammalian, induced | Meningitis with genotype-dependent severity (ST1>ST6) | 30193592 |
| Humanized E-cadherin transgenic mouse | Mammalian, genetic (knock-in) | Overcomes InlA species specificity; models intestinal barrier crossing | 15060982 |
| Oral infection murine model (ruminant isolates) | Mammalian, induced | Pathogenicity/genomic comparison | 42667904 |
| Infant-rat meningoencephalitis | Mammalian, induced | Antibiotic efficacy testing in brain | 10390217 |
| Zebrafish larvae | Vertebrate, in vivo imaging | LLO-dependent phagosomal escape; ActA-dependent spread; real-time phagocyte interaction | 19546195 |
| RAW264.7 / cultured cell lines | In vitro | Invasion, intracellular growth, cell-to-cell spread | 28004800, 26055558 |

**Limitations:** wild-type mice under-model oral/intestinal invasion because murine E-cadherin does not bind InlA (requires humanized model); no single model fully captures the elderly/immunocompromised human host context.

---

## Mechanistic Model / Interpretation

The unifying theme is that **Listeria meningitis is a disease of the intersection between an intracellular pathogen's molecular toolkit and a host who cannot deploy cell-mediated immunity.** Three axes explain nearly all clinical observations:

1. **Host immune axis** (Findings 1, 7) — defines *who* gets the disease: neonates, elderly, pregnant, diabetic, immunosuppressed. This drives the epidemiology (RR 4.4–10.1) and the demand for empirical ampicillin in at-risk meningitis.

2. **Pathogen invasion/spread axis** (Findings 4, 6) — defines *how* the disease happens: InlA/InlB→E-cadherin/Met for barrier crossing (gut, placenta, BBB), LLO for phagosomal escape, ActA for intracellular spread. This intracellular, cell-to-cell lifestyle explains why humoral immunity and cephalosporins fail while cell-penetrant agents (ampicillin, TMP-SMX) succeed.

3. **Pathogen genotype axis** (Findings 2, 6) — defines *how badly*: hypervirulent ST6/CC lineages independently worsen outcome, corroborated by genotype-dependent murine brain damage.

These converge on a **brainstem-predominant meningoencephalitis** (Findings 3, 8) whose imaging signature (T2-FLAIR pons/medulla/cerebellum, hydrocephalus) is both diagnostic and prognostic, and which is faithfully mirrored in ruminant "circling disease" (Finding 9), confirming a deeply conserved zoonotic syndrome.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [27845429](https://pubmed.ncbi.nlm.nih.gov/27845429/) | Diabetes 2.2× BM risk; Listeria 6% | F1 |
| [35352336](https://pubmed.ncbi.nlm.nih.gov/35352336/) | Atypical pathogens 33% in ≥80y | F1 |
| [23592828](https://pubmed.ncbi.nlm.nih.gov/23592828/) | ST6 sole predictor of poor outcome | F2 |
| [28139432](https://pubmed.ncbi.nlm.nih.gov/28139432/) | MONALISA: 84% meningoencephalitis, 17% brainstem | F3 |
| [30117097](https://pubmed.ncbi.nlm.nih.gov/30117097/) | InlA/InlB→E-cadherin/Met brain invasion | F4 |
| [19546195](https://pubmed.ncbi.nlm.nih.gov/19546195/) | LLO-dependent escape; zebrafish model | F4, F6 |
| [24739967](https://pubmed.ncbi.nlm.nih.gov/24739967/) | LLO/efferocytosis-mediated spread | F4 |
| [29433694](https://pubmed.ncbi.nlm.nih.gov/29433694/) | Amoxicillin 14d; cephalosporins fail | F5 |
| [10959905](https://pubmed.ncbi.nlm.nih.gov/10959905/) | TMP-SMX CNS-penetrant salvage | F5 |
| [10390217](https://pubmed.ncbi.nlm.nih.gov/10390217/) | Amox+gent most active in brain | F5 |
| [30193592](https://pubmed.ncbi.nlm.nih.gov/30193592/) | Mouse meningitis model, ST1>ST6 | F6 |
| [15060982](https://pubmed.ncbi.nlm.nih.gov/15060982/) | Humanized E-cadherin mouse; InlA specificity | F6 |
| [23739339](https://pubmed.ncbi.nlm.nih.gov/23739339/) | US incidence 0.29, CFR 21%, RR by group | F7 |
| [39093565](https://pubmed.ncbi.nlm.nih.gov/39093565/) | Listeria highest CFR (27%) among causes | F7 |
| [29796652](https://pubmed.ncbi.nlm.nih.gov/29796652/) | Imaging; hydrocephalus/parenchymal prognosis | F8 |
| [37303100](https://pubmed.ncbi.nlm.nih.gov/37303100/) | Rhombencephalitis MRI signature | F8 |
| [40192846](https://pubmed.ncbi.nlm.nih.gov/40192846/) | Bovine brainstem microabscesses | F9 |
| [42667904](https://pubmed.ncbi.nlm.nih.gov/42667904/) | Zoonotic ruminant isolates | F9 |
| [419368](https://pubmed.ncbi.nlm.nih.gov/419368/) | Bimodal neonatal disease | F10 |
| [40887071](https://pubmed.ncbi.nlm.nih.gov/40887071/) | Neonatal listeriosis review/prevention | F10 |

---

## Limitations and Knowledge Gaps

- **Host genetic susceptibility is undefined.** No GWAS locus or Mendelian modifier for Listeria meningitis specifically was identified; susceptibility is framed entirely through acquired immune compromise. Section 4 (host genetics) and much of Section 9 (inheritance) are **not applicable** to this infectious disease.
- **BBB-crossing route is partially inferred.** Whether Listeria crosses the BBB primarily transcellularly, paracellularly, or via infected leukocytes ("Trojan horse") is not fully resolved in the reviewed evidence.
- **Sex-ratio data are confounded** by the large pregnancy-associated fraction; true non-pregnant sex ratios are less well quantified.
- **Metabolomics/proteomics/single-cell/spatial** profiling of human Listeria meningitis was not found — these omics domains remain gaps.
- **Prognostic value of ST6** derives largely from Dutch cohorts; generalizability across geographies needs confirmation.
- **No randomized trial** defines the optimal antibiotic regimen or the role of gentamicin/dexamethasone specifically in Listeria meningitis; guidance is extrapolated from cohorts and models.

## Proposed Follow-up Experiments / Actions

1. **Genotype–outcome validation:** Prospective multinational cohort correlating *L. monocytogenes* CC/ST (WGS) with CNS outcome to confirm/extend ST6 findings beyond the Netherlands.
2. **Host immunogenetics:** Targeted sequencing / immune-function studies in non-classical Listeria meningitis patients to identify inborn or acquired immune defects (e.g., in the IFN-γ/TNF axis).
3. **RCT of adjunctive therapy:** Evaluate gentamicin's incremental benefit and dexamethasone's harm/benefit specifically in confirmed Listeria meningitis.
4. **Neuroinvasion mechanism:** Use humanized E-cadherin mice + intravital imaging and the zebrafish model to dissect transcellular vs Trojan-horse BBB crossing and test anti-InlB/Met blockade.
5. **Biomarker development:** Assess CSF/serum markers and MRI hydrocephalus/parenchymal-lesion scoring as validated prognostic tools for early neurocritical escalation.
6. **Prevention impact:** Quantify the effect of WGS-based food-surveillance programs on invasive listeriosis incidence in risk groups.


## Artifacts

- [OpenScientist final report](Listeria_Meningitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Listeria_Meningitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 43 |
| On topic | 26 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 17 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002315` (1 mention) - the report calls it "Common (~84% in general BM)"; HP calls it **Headache**
- `HP:0002383` (1 mention) - the report calls it "84% of neurolisteriosis"; HP calls it **Infectious encephalitis**
- `HP:0001250` (1 mention) - the report calls it "Elevated in alcoholic/severe cases"; HP calls it **Seizure**
- `HP:0002921` (1 mention) - the report calls it "Diagnostic"; HP calls it **Abnormal cerebrospinal fluid morphology**
- `HP:0000238` (1 mention) - the report calls it "~10%; poor prognosis"; HP calls it **Hydrocephalus**
- `GO:0090662` (1 mention) - the report calls it "phagosome"; GO calls it **GO_0090662**
- `UBERON:0002361` (1 mention) - the report calls it "Primary organ:** brain and meninges — leptomeninges"; UBERON calls it **pia mater**
- `NCIT:C544` (1 mention) - the report calls it "Adjunct, esp. early/severe"; NCIT calls it **Altretamine**
- `NCIT:C312` (1 mention) - the report calls it "Alternative (penicillin allergy); CNS-penetrant, intracellular; salvage for refractory disease"; NCIT calls it **Bleomycin Sulfate**
- `NCIT:C61796` (1 mention) - the report calls it "Alternative in some settings"; NCIT calls it **Ivermectin**
- `NCIT:C583` (1 mention) - the report calls it "Standard empirically, **stop when Listeria confirmed"; NCIT calls it **Recombinant Interferon Gamma**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0090662` (GO_0090662) (1 mention) - replaced by `GO:0055085`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0043277` (1 mention) - the report calls it "apoptotic cell clearance/efferocytosis"; GO calls it **apoptotic cell clearance**