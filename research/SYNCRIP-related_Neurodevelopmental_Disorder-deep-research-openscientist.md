---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T17:48:21.205670'
end_time: '2026-10-24T18:11:22.795316'
duration_seconds: 1381.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SYNCRIP-related Neurodevelopmental Disorder
  mondo_id: MONDO:0800456
  category: Mendelian
  causal_genes: SYNCRIP
  omim_id: not recorded
  synonyms: SYNCRIP-related intellectual disability; hnRNP-Q-related neurodevelopmental
    disorder
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
citation_count: 14
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 40
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 8
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0800456
    reported_labels:
    - MONDO
    ontology_label: SYNCRIP-related neurodevelopmental disorder
  - term_id: HP:0011283
    reported_labels:
    - Neuroradiological
    ontology_label: Abnormal metencephalon morphology
  - term_id: HP:0000750
    reported_labels:
    - Cognitive/communicative
    ontology_label: Delayed speech and language development
  - term_id: CL:0000129
    reported_labels:
    - radial glial cell / apical radial glia
    - radial glial cells / apical progenitors
    ontology_label: microglial cell
  labels_variant: 7
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SYNCRIP-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SYNCRIP-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SYNCRIP-related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0800456 (if available)
- **Causal gene(s):** SYNCRIP
- **OMIM:** not recorded
- **Synonyms:** SYNCRIP-related intellectual disability; hnRNP-Q-related neurodevelopmental disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SYNCRIP-related Neurodevelopmental Disorder** covering all of the
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

# SYNCRIP-related Neurodevelopmental Disorder: A Comprehensive Research Report

**Target disease:** SYNCRIP-related Neurodevelopmental Disorder
**MONDO ID:** MONDO:0800456
**Causal gene:** **SYNCRIP** (Synaptotagmin-binding Cytoplasmic RNA-Interacting Protein; also known as **hnRNP-Q**; HGNC:16918; NCBI Gene 10492; Ensembl ENSG00000135316; UniProt O60506; chromosome 6q14.3)

---

## Summary

**SYNCRIP-related Neurodevelopmental Disorder (SYNCRIP-NDD) is a rare, autosomal-dominant Mendelian condition caused by heterozygous, typically *de novo*, variants in the gene SYNCRIP, which encodes the RNA-binding protein hnRNP-Q.** The disorder was established when a large-scale intellectual-disability trio meta-analysis flagged SYNCRIP as a statistically supported candidate gene, and was confirmed by subsequent case reports describing additional individuals with *de novo* loss-of-function and RNA-recognition-motif (RRM) missense variants. The core clinical picture comprises intellectual disability/developmental delay, frequently with autism spectrum features, and variable epilepsy (including myoclonic-atonic seizures) and structural brain malformations such as periventricular nodular heterotopia and widened subarachnoid spaces.

The molecular mechanism is **haploinsufficiency of hnRNP-Q**. SYNCRIP is one of the most loss-of-function-intolerant genes in the human genome (gnomAD pLI = 1.00, LOEUF = 0.228), and pathogenic variants are predominantly truncating (frameshift/nonsense) alleles that reduce functional protein dosage, alongside rarer missense variants in the conserved RRM2 domain that impair RNA binding. Although SYNCRIP is ubiquitously expressed across tissues, the disease is CNS-selective, implying a neuron-specific dependence on precise hnRNP-Q dosage rather than tissue-restricted expression. Mechanistically, hnRNP-Q controls cortical neurogenesis by maintaining the temporal transcription-factor program of radial glial cells through a **phase-separation-dependent** recruitment of mRNA-stabilization complexes that regulates Notch signaling. Pathogenic human mutations weaken this phase-separation capacity, stalling the transcriptional progression of neural progenitors and producing cortical layering defects and learning/memory impairment in mouse models.

SYNCRIP-NDD belongs to the broader family of **"hnRNPopathies"** — neurodevelopmental disorders caused by haploinsufficiency of heterogeneous nuclear ribonucleoprotein genes (e.g., *HNRNPU*, *HNRNPK*) — which converge on dysregulation of post-transcriptional RNA metabolism (splicing, mRNA stability, transport, and local translation) in neurons. The disorder is managed symptomatically; there is no disease-modifying therapy. This report synthesizes evidence from human clinical genetics, population constraint databases, model-organism studies (mouse and *Drosophila*), and in vitro molecular biology.

---

## 1. Disease Information

**Overview.** SYNCRIP-related Neurodevelopmental Disorder is a monogenic neurodevelopmental disorder characterized primarily by intellectual disability/global developmental delay, with a high frequency of autism spectrum disorder features and a variable occurrence of epilepsy and brain malformations. It results from heterozygous pathogenic variants in *SYNCRIP*, a gene encoding the RNA-binding protein hnRNP-Q, a member of the heterogeneous nuclear ribonucleoprotein (hnRNP) family that regulates mRNA splicing, stability, transport, and translation.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0800456 |
| Gene (HGNC) | SYNCRIP, HGNC:16918 |
| NCBI Gene | 10492 |
| Ensembl | ENSG00000135316 |
| UniProt | O60506 (HNRPQ_HUMAN) |
| Cytogenetic locus | 6q14.3 (GRCh38 chr6:85,607,779–85,644,063) |
| OMIM | Not recorded for the disease (no dedicated phenotype MIM at time of research) |
| ICD-10/ICD-11 | No disease-specific code; coded under generic neurodevelopmental/intellectual-disability categories |
| MeSH | No disease-specific MeSH; indexed under Intellectual Disability / Neurodevelopmental Disorders |

**Synonyms / alternative names:** SYNCRIP-related intellectual disability; hnRNP-Q-related neurodevelopmental disorder; (protein-based) Synaptotagmin-binding cytoplasmic RNA-interacting protein-related disorder.

**Source of information.** The entry is derived from **aggregated disease-level resources and small published case series**, not EHR/individual-patient data. The evidence base is small — a handful of published individuals plus a de novo mutation meta-analysis — supplemented by extensive functional data from model organisms and in vitro studies. Monarch Initiative confirms the MONDO definition but shows sparse phenotype annotation, consistent with an ultra-rare, recently delineated disorder.

---

## 2. Etiology

**Primary cause — genetic.** SYNCRIP-NDD is caused by heterozygous pathogenic variants in *SYNCRIP*. These arise **predominantly *de novo***, consistent with a dominant mechanism acting through haploinsufficiency. Two mutational classes are documented:

1. **Loss-of-function (truncating) variants** — frameshift and nonsense variants producing prematurely terminated/unstable transcript, reducing functional hnRNP-Q dosage (haploinsufficiency).
2. **Missense variants in the RNA-recognition-motif (RRM) domains** — notably in the conserved RRM2 domain — impairing RNA binding.

Semino et al. (2021) reported three individuals: two with frameshift variants (the more severely affected) and one with an RRM2 missense variant: *"Two frameshift variants in the more severely affected individuals, likely result in haploinsufficiency. The third missense variant lies in the conserved RNA recognition motif (RRM) 2 domain likely affecting RNA-binding"* [PMID: 34157790](https://pubmed.ncbi.nlm.nih.gov/34157790/).

SYNCRIP was first nominated as an intellectual-disability gene by a meta-analysis of 2,104 trios: *"Statistical analyses identified 10 new candidate ID genes: DLG4, PPM1D, RAC1, SMAD6, SON, SOX5, SYNCRIP, TCF20, TLK2 and TRIP12"* [PMID: 27479843](https://pubmed.ncbi.nlm.nih.gov/27479843/).

**Genetic risk factors.** The causal variants themselves are the risk factors. There are no reported susceptibility loci or validated modifier genes. The gene's extreme constraint (Section 4) means any functional haploinsufficient lesion carries high disease risk.

**Environmental risk factors.** None established. As a monogenic *de novo* disorder, advanced parental age is a general (non-specific) risk factor for *de novo* mutation burden, not specifically quantified for SYNCRIP.

**Protective factors.** None identified (genetic or environmental).

**Gene–environment interactions.** None documented.

---

## 3. Phenotypes

The phenotypic spectrum is derived from a small published cohort (principally the 3 individuals of Semino et al. plus the meta-analysis probands). Reported features, with suggested HPO terms:

| Phenotype | Type | HPO term | Frequency (small cohort) | Onset | Severity/course |
|---|---|---|---|---|---|
| Intellectual disability / global developmental delay | Cognitive | HP:0001249 / HP:0001263 | ~100% | Infancy/childhood | Variable (mild–severe); stable, lifelong |
| Autism spectrum disorder / autistic features | Behavioral | HP:0000729 | ~2/3 | Early childhood | Variable |
| Epilepsy (incl. myoclonic-atonic seizures) | Neurological sign | HP:0001250 / HP:0002123 | ~1/3 | Childhood | Variable; episodic seizures |
| Periventricular nodular heterotopia | Neuroradiological/structural | HP:0032388 / HP:0007165 | Reported | Congenital | Static malformation |
| Widened subarachnoid space | Neuroradiological | HP:0011283 | Reported | Congenital/infancy | Static |
| Speech/language delay | Cognitive/communicative | HP:0000750 | Common | Childhood | Lifelong |

**Phenotype characteristics.** Onset is in the **neonatal-to-childhood** window (developmental). Severity is **variable**, correlating loosely with variant class — frameshift/truncating (haploinsufficiency) variants were seen in the more severely affected individuals, whereas the RRM2 missense case was reportedly milder. The disorder is **non-progressive/static** (a developmental encephalopathy with fixed deficits rather than neurodegeneration), though epilepsy introduces an episodic component.

**Quality-of-life impact.** Intellectual disability and ASD features substantially impair adaptive functioning, communication, and independence, typically requiring lifelong educational and caregiver support. Epilepsy adds seizure-related morbidity and treatment burden. Formal QoL instrument data (EQ-5D, SF-36, PROMIS) are not available for this ultra-rare disorder.

> **Note on uncertainty:** Frequencies are based on <10 published individuals and are provisional. Larger cohorts (e.g., via GeneMatcher) are needed for robust penetrance/frequency figures.

---

## 4. Genetic / Molecular Information

**Causal gene.** *SYNCRIP* (HGNC:16918; NCBI Gene 10492; Ensembl ENSG00000135316), chromosome 6q14.3. Encodes hnRNP-Q / Synaptotagmin-binding cytoplasmic RNA-interacting protein (UniProt O60506).

**Protein architecture.** hnRNP-Q contains **three RNA-recognition-motif (RRM) domains**, a **unique N-terminal acidic domain (AcD)**, and a **C-terminal RGG box**. The acidic domain is a non-canonical, structurally distinct nucleic-acid-binding region: *"The acid-rich sequence segment is unique to SYNCRIP and the closely related protein hnRNP R"* [PMID: 27081926](https://pubmed.ncbi.nlm.nih.gov/27081926/). The AcD binds ATP at physiological concentrations despite lacking an RRM fold [PMID: 31791586](https://pubmed.ncbi.nlm.nih.gov/31791586/).

**Pathogenic variants (ClinVar, transcript NM_006372.5).** NCBI ClinVar returns 193 SYNCRIP records: 121 Uncertain significance, 19 Pathogenic, 4 Likely pathogenic, 1 Pathogenic/Likely pathogenic, 17 Likely benign, 1 Benign. Pathogenic small variants are **predominantly truncating**:

| Variant (NM_006372.5) | Protein | Class | Classification |
|---|---|---|---|
| c.1473dup | p.Gln492fs | Frameshift | Pathogenic |
| c.700_701del | p.Ile234fs | Frameshift | Pathogenic |
| c.1336C>T | p.Arg446Ter | Nonsense | Pathogenic |
| c.438dup | p.Pro147fs | Frameshift | Likely pathogenic |
| c.858_859del | p.Gly287fs | Frameshift | Pathogenic |

Additional pathogenic entries are **large 6q14 copy-number deletions/duplications** spanning *SYNCRIP* (e.g., GRCh38 6q14.3-15 chr6:85,370,716–90,669,793 ×1). Most missense SNVs remain **variants of uncertain significance (VUS)**.

**Variant classification (ACMG/AMP).** Truncating variants in a highly LoF-constrained gene meet strong pathogenicity criteria (e.g., PVS1 + de novo PS2/PM6). RRM-domain missense variants require functional evidence (RNA-binding/phase-separation assays) to be upgraded from VUS.

**Allele frequency.** Pathogenic variants are absent/vanishingly rare in population databases (gnomAD), consistent with *de novo*, highly penetrant disease alleles.

**Somatic vs germline.** Germline (constitutional); *de novo* in affected probands.

**Functional consequences.** **Loss of function / haploinsufficiency** is the dominant mechanism. Frameshift/nonsense alleles reduce functional dosage; RRM2 missense alleles impair RNA binding, with a demonstrated phase-separation-weakening effect (Section 6).

**gnomAD constraint (v2.1.1).** SYNCRIP is among the most LoF-intolerant genes:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 1.00 (0.99999999986) | Extreme LoF intolerance |
| LOEUF (oe_lof upper) | 0.228 | Most-constrained decile (<0.35) |
| observed/expected LoF | 0.131 (9 obs vs 68.9 exp) | ~87% depletion of LoF variants |
| LoF Z | 6.12 | Strong constraint |
| Missense Z | 5.48 (oe_mis 0.537) | Significant missense constraint |
| Synonymous Z | −0.15 | Neutral (validates model) |

These support a **haploinsufficiency** disease mechanism (dosage sensitivity).

**Expression (GTEx v8).** SYNCRIP is **ubiquitously expressed** (median 33.9 TPM across 54 tissues; range 6.2–89.9 TPM), highest in cultured fibroblasts (89.9), EBV-transformed lymphocytes (88.8), and thyroid (63.6); brain regions 11–28 TPM (cerebellar hemisphere 27.5, frontal cortex BA9 16.2, hippocampus 13.0, cortex 12.7); lowest in whole blood (6.2). Ubiquitous expression contrasted with CNS-selective disease implies **neuron-specific dosage dependence**.

**Modifier genes / epigenetics.** None established. The paralog *HNRNPR* (hnRNP-R) shares high sequence homology and partially overlapping functions; in *Drosophila* both correspond to the single ortholog *Syncrip* (Syp) [PMID: 30214903](https://pubmed.ncbi.nlm.nih.gov/30214903/). Whether hnRNP-R dosage modifies disease severity is untested. No episignature/methylation marker is known.

**Chromosomal abnormalities.** 6q14.3 deletions/duplications encompassing *SYNCRIP* are documented as pathogenic CNVs in ClinVar.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributors are known for SYNCRIP-NDD. It is a monogenic *de novo* genetic disorder. Environmental factors (e.g., parental-age effects on *de novo* mutation rate) are generic to all *de novo* disorders and not specific to this condition. **Not applicable / none documented.**

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **de novo variant in *SYNCRIP*** arises — either a frameshift/nonsense allele or an RRM-domain missense allele.
2. **Truncating alleles lead to** reduced functional hnRNP-Q protein (haploinsufficiency); **missense RRM2 alleles lead to** impaired RNA binding; **both branches converge** on insufficient functional hnRNP-Q activity in neural cells.
3. Reduced/impaired hnRNP-Q **results in weakened liquid-liquid phase-separation (LLPS) capacity** — pathogenic human mutations fail to form stable biomolecular condensates (demonstrated in vitro and in mouse) [PMID: 39776340](https://pubmed.ncbi.nlm.nih.gov/39776340/).
4. Weakened phase separation **leads to** failure to recruit mRNA-stabilization complexes that maintain transcription of **temporal transcription factors** in radial glial cells (RGCs).
5. Loss of temporal-transcription-factor maintenance **dysregulates Notch signaling** governing RGC fate, which **stalls the transcriptional progression** of neural progenitors through their temporal identity program (inferred causal linkage from mouse knockout data).
6. Stalled progenitor temporal dynamics **result in** disrupted late-stage neurogenesis, abnormal neuronal migration/localization, and **superficial cortical-layer defects**.
7. Abnormal cortical architecture and connectivity **lead to** the clinical phenotypes: intellectual disability, autism spectrum features, epilepsy, and structural malformations (periventricular nodular heterotopia) — plus learning/memory impairment demonstrated in mouse models.

**Branch note:** In addition to the neurogenesis branch (steps 3–6), hnRNP-Q has **post-mitotic neuronal roles** (synaptic plasticity, neurite morphogenesis, local translation) that likely contribute to the cognitive/behavioral phenotype independently of cortical layering, though their specific contribution in patients is **inferred, not demonstrated**.

### Supporting detail

**Molecular pathways.** The central pathway is **Notch signaling** regulating RGC temporal identity, downstream of hnRNP-Q-mediated mRNA stabilization. Wu et al. (2025) showed: *"Syncrip knockout in RGCs disrupts differentiation and abnormal neuronal localization, ultimately resulting in superficial cortical layer defects as well as learning and memory impairments in mice"* and *"pathogenic human mutations in Syncrip weaken its phase-separation capability, failing to form stable complexes normally"* [PMID: 39776340](https://pubmed.ncbi.nlm.nih.gov/39776340/).

**Cellular processes.** Regulation of neural-progenitor temporal identity; neuronal differentiation and migration; synaptic plasticity; neurite/dendrite morphogenesis. In mammalian neurons, hnRNP-Q1 binds mRNAs encoding the actin-nucleation machinery: *"hnRNP Q1 bound to a set of identified mRNAs encoding the components of the actin nucleation-promoting Cdc42/N-WASP/Arp2/3 complex"* [PMID: 22493061](https://pubmed.ncbi.nlm.nih.gov/22493061/).

**Protein dysfunction.** Loss of function via haploinsufficiency (truncating) or impaired RNA binding (RRM2 missense), both reducing functional ribonucleoprotein condensates (weakened LLPS). The unique acidic domain mediates non-canonical nucleic-acid/ATP binding relevant to condensate behavior [PMID: 27081926](https://pubmed.ncbi.nlm.nih.gov/27081926/); [PMID: 31791586](https://pubmed.ncbi.nlm.nih.gov/31791586/).

**Molecular functions (QuickGO; UniProt O60506, 62 annotations).**
- *Molecular function:* RNA binding (GO:0003723), mRNA 5′-UTR binding (GO:0048027), nucleic acid binding (GO:0003676), protein binding (GO:0005515).
- *Biological process:* negative regulation of translation (GO:0017148), positive regulation of cytoplasmic translation (GO:2000767), CRD-mediated mRNA stabilization (GO:0070934), negative regulation of deadenylation-dependent mRNA decay (GO:1900152), mRNA splicing via spliceosome (GO:0000398), RNA processing (GO:0006396).
- *Cellular component:* nucleus (GO:0005634), cytoplasm/cytosol (GO:0005737/GO:0005829), ribonucleoprotein complex (GO:1990904), CRD-mediated mRNA stability complex (GO:0070937/GO:0106002), GAIT complex (GO:0097452), catalytic step 2 spliceosome (GO:0071013).

**Evolutionary conservation (Drosophila).** The single fly ortholog *Syncrip/Syp* controls neuroblast temporal identity via the **Imp→Syp switch** [PMID: 28394252](https://pubmed.ncbi.nlm.nih.gov/28394252/); [PMID: 38031099](https://pubmed.ncbi.nlm.nih.gov/38031099/), and is required for activity-dependent synaptic growth: *"activity-dependent accumulation of Msp300 in the postsynaptic compartment of the Drosophila larval neuromuscular junction is regulated by the conserved RNA binding protein Syncrip/hnRNP Q"* [PMID: 32040548](https://pubmed.ncbi.nlm.nih.gov/32040548/).

**Suggested GO/CL terms.** Biological processes: GO:0021895 (cerebral cortex neuron differentiation), GO:0007219 (Notch signaling pathway), GO:0070934 (CRD-mediated mRNA stabilization), GO:0017148 (negative regulation of translation). Cell types: CL:0000679 (glutamatergic neuron), CL:0000047 (neural stem cell), CL:0000031 (neuroblast), CL:0000129 (radial glial cell / apical radial glia).

### Mechanistic diagram

```
 de novo SYNCRIP variant
   ├─ frameshift/nonsense ── haploinsufficiency ─┐
   └─ RRM2 missense ──────── impaired RNA binding ┤
                                                  ▼
                            insufficient functional hnRNP-Q
                                                  ▼
                        weakened phase separation (LLPS)
                                                  ▼
             failure to recruit mRNA-stabilization complexes
                                                  ▼
     loss of temporal-TF maintenance in radial glial cells
                                                  ▼
                 dysregulated Notch signaling / stalled
                     progenitor temporal progression
                                                  ▼
           disrupted neurogenesis, abnormal migration,
                 superficial cortical-layer defects
                                                  ▼
   Intellectual disability · ASD features · epilepsy · PNH
   (+ post-mitotic synaptic/neurite roles, inferred)
```

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ: the **brain** (central nervous system). The disorder is CNS-selective despite ubiquitous SYNCRIP expression. No consistent primary involvement of other organ systems.

**Body systems.** Nervous system (UBERON:0001016). Specifically, the **cerebral cortex** (UBERON:0000956) and its developing germinal zones; the **periventricular region** (site of nodular heterotopia); and the **subarachnoid space** (UBERON:0002360, widened).

**Tissue and cell level.** Nervous tissue. Key cell populations: **radial glial cells / apical progenitors** (CL:0000129), **neuroblasts/intermediate progenitors** (CL:0000031), and **cortical projection neurons** (CL:0000679, glutamatergic neurons). Post-mitotic neurons (including hippocampal neurons implicated in learning/memory in mouse models) are also affected through synaptic/morphogenic roles.

**Subcellular level.** hnRNP-Q localizes to the **nucleus** (GO:0005634) and **cytoplasm/cytosol** (GO:0005737/GO:0005829), functioning within **ribonucleoprotein complexes/granules** (GO:1990904), the **CRD-mediated mRNA stability complex** (GO:0070937), the **GAIT complex** (GO:0097452), and the **spliceosome** (GO:0071013). Biomolecular condensates (phase-separated granules) are the critical subcellular structures whose assembly is impaired.

**Localization / lateralization.** Cortical malformations (periventricular nodular heterotopia, widened subarachnoid spaces) are typically **bilateral**, consistent with a diffuse developmental mechanism.

---

## 8. Temporal Development

**Onset.** **Congenital/developmental.** Cortical malformations originate during fetal corticogenesis; developmental delay manifests in infancy/early childhood. Onset pattern is **insidious/chronic** (a static developmental encephalopathy), not acute.

**Progression.** Cognitive/structural deficits are **static** (fixed developmental deficits) rather than neurodegenerative. There are no defined disease "stages." Epilepsy, when present, introduces an **episodic** seizure course. Overall, a **chronic, lifelong** condition.

**Patterns / critical periods.** The **critical period of vulnerability** is prenatal/perinatal corticogenesis, when radial-glial temporal programming and neuronal migration occur — the window in which SYNCRIP haploinsufficiency exerts its developmental effect. There is no spontaneous remission of the core neurodevelopmental phenotype; seizures may respond to anti-seizure medication.

---

## 9. Inheritance and Population

**Epidemiology.** **Prevalence and incidence are unknown/unestablished** — the disorder is ultra-rare, with fewer than ~10 published individuals. No registry-based prevalence estimates exist. It contributes to the broad category of monogenic intellectual disability (collectively ~1% of the population, but each individual gene is rare).

**Inheritance pattern.** **Autosomal dominant**, essentially always **de novo** (sporadic). No confirmed vertical transmission reported.

**Penetrance.** Presumed **high/complete** for reported pathogenic truncating variants, though formal penetrance cannot be estimated from the tiny cohort.

**Expressivity.** **Variable** — severity correlates loosely with variant class (truncating/haploinsufficiency more severe than RRM2 missense).

**Genetic anticipation.** Not applicable (not a repeat-expansion disorder).

**Germline mosaicism.** Not specifically reported; theoretically possible as for other *de novo* dominant disorders (relevant to recurrence-risk counseling).

**Founder effects / consanguinity.** Not applicable — *de novo* dominant mechanism; no founder alleles; consanguinity not relevant.

**Carrier frequency.** Not applicable (dominant *de novo*). gnomAD shows depletion of LoF variants (9 observed vs 68.9 expected) — pathogenic alleles are not carried in the general population.

**Population demographics.** No ethnic/geographic predilection reported. Sex ratio not established (cohort too small). Age distribution: affected from birth/infancy; lifelong.

---

## 10. Diagnostics

**Recommended approach.** Diagnosis is **molecular**, via broad genomic sequencing in a child with unexplained developmental delay/intellectual disability ± ASD ± epilepsy ± brain malformation.

**Genetic testing (primary diagnostic modality).**
- **Trio whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** is the highest-yield approach, enabling *de novo* variant detection and classification. GeneMatcher-type data sharing is essential for ultra-rare genes.
- **Intellectual disability / epilepsy / ASD gene panels** that include *SYNCRIP* can detect SNVs/indels.
- **Chromosomal microarray (CMA)** detects 6q14.3 deletions/duplications encompassing *SYNCRIP*.
- Single-gene testing has limited utility given phenotypic nonspecificity.
- Karyotyping/FISH only for suspected large structural rearrangements; mtDNA and repeat-expansion testing are **not applicable**.

**Variant interpretation.** Apply ACMG/AMP criteria: truncating variants in this LoF-constrained gene (PVS1) plus *de novo* status (PS2/PM6) support pathogenicity; RRM-domain missense variants typically remain VUS pending functional assays (RNA binding, phase-separation).

**Clinical tests / imaging.** **Brain MRI** is informative — may reveal **periventricular nodular heterotopia** and **widened subarachnoid spaces**. **EEG** is indicated when seizures are suspected (may show epileptiform activity, including patterns consistent with myoclonic-atonic epilepsy). Routine labs, metabolic workup, and biopsies are typically normal/noncontributory (no specific biomarker exists).

**Biomarkers / omics diagnostics.** No validated protein, metabolite, or methylation biomarker (episignature) is established. RNA-sequencing for aberrant splicing is a research tool, not a clinical test.

**Clinical criteria / differential diagnosis.** No disorder-specific diagnostic criteria. Differential diagnosis includes other **hnRNPopathies** and monogenic ID/ASD/epilepsy syndromes — e.g., *HNRNPU*-related disorder (early-onset epilepsy, severe ID; [PMID: 28393272](https://pubmed.ncbi.nlm.nih.gov/28393272/)), *HNRNPK*-related Au-Kline syndrome (distinctive facial gestalt; [PMID: 29904177](https://pubmed.ncbi.nlm.nih.gov/29904177/)), *MED13L* haploinsufficiency ([PMID: 28645799](https://pubmed.ncbi.nlm.nih.gov/28645799/)), and other heterotopia-associated genes (e.g., *FLNA*). Molecular testing distinguishes these.

**Screening.** No population newborn or carrier screening (ultra-rare, *de novo*). Cascade testing is generally unnecessary given *de novo* origin, but parental testing confirms de novo status for recurrence-risk counseling.

---

## 11. Outcome / Prognosis

**Survival / mortality.** No evidence of reduced life expectancy from the core disorder; it is **not directly life-limiting**. Mortality risk, if any, relates to seizure complications in severe epilepsy. No formal survival statistics exist.

**Morbidity and function.** The principal burden is **neurodevelopmental disability** — intellectual disability, communication/speech impairment, and ASD-related adaptive deficits — producing lifelong dependence of varying degree. Epilepsy adds morbidity in a subset.

**Disease course.** Chronic and **static** (non-degenerative). Core deficits persist; developmental gains occur with intervention but intellectual disability remains. Complications: seizures, feeding/behavioral issues, and those secondary to cortical malformation.

**Recovery potential.** No cure; **symptomatic improvement** with early intervention (therapies, special education) is possible but core cognitive impairment is permanent.

**Prognostic factors.** **Variant class** is the main apparent prognostic factor — truncating/haploinsufficiency variants were associated with more severe phenotypes than the RRM2 missense variant in the published series [PMID: 34157790](https://pubmed.ncbi.nlm.nih.gov/34157790/). Seizure control and severity of cortical malformation also influence outcome. No validated prognostic biomarkers.

---

## 12. Treatment

**There is no disease-modifying or targeted therapy.** Management is **symptomatic and supportive**, following general neurodevelopmental-disorder best practice.

**Pharmacotherapy.** **Anti-seizure medications** for epilepsy, selected per seizure type (myoclonic-atonic epilepsy may respond to valproate, levetiracetam, lamotrigine, or specific regimens; choice individualized). Behavioral/ASD-associated symptoms managed per standard practice. No pharmacogenomic guidance specific to SYNCRIP. (NCIT: C15215 Anticonvulsant Therapy.)

**Advanced therapeutics.** None available. Gene, RNA-based, cell, targeted, or immunotherapies are **not applicable/not developed**. Haploinsufficiency is conceptually amenable to future dosage-restoring strategies (e.g., ASO-mediated upregulation or gene supplementation), but none exist for SYNCRIP.

**Surgical/interventional.** Epilepsy surgery only in rare refractory cases with a resectable focus; generally not applicable given diffuse malformation.

**Supportive and rehabilitative (mainstay).**
- **Physical therapy** (NCIT: C15415) for hypotonia/motor delay.
- **Occupational therapy** (NCIT: C15321).
- **Speech-language therapy** (NCIT: C15402) for communication delay.
- Special education, behavioral therapy for ASD features, and family/caregiver support.

**Experimental treatments.** No disease-specific clinical trials (no NCT identifiers) exist for SYNCRIP-NDD.

**Treatment strategy.** Multidisciplinary developmental-pediatrics/neurology care: seizure management, developmental therapies, educational support, and genetic counseling. **Personalized medicine** is currently limited to variant-informed prognosis and counseling.

---

## 13. Prevention

**Primary prevention.** Not possible for *de novo* mutations. General preconception health applies but does not specifically prevent this disorder.

**Secondary prevention / early detection.** Early genetic diagnosis via WES/WGS enables **early intervention** (developmental therapies, seizure monitoring), improving functional outcomes though not altering the underlying genetic lesion.

**Genetic screening / reproductive options.** For families with an affected child (de novo), recurrence risk is low but non-zero (germline mosaicism). **Prenatal diagnosis** or **preimplantation genetic testing (PGT-M)** for the specific familial variant can be offered in subsequent pregnancies.

**Counseling.** **Genetic counseling** is central: explaining *de novo* dominant inheritance, low recurrence risk (with caveat of possible germline mosaicism), and reproductive options. Parental testing confirms de novo status.

**Immunization / public health / environmental / prophylaxis.** Not applicable.

---

## 14. Other Species / Natural Disease

**Taxonomy and orthologs.** SYNCRIP is evolutionarily conserved. Orthologs include:
- *Mus musculus* (NCBI Taxon:10090): *Syncrip* (used in the definitive mouse knockout study).
- *Drosophila melanogaster* (NCBI Taxon:7227): single ortholog *Syncrip* (*Syp*), corresponding to both human paralogs hnRNP-Q and hnRNP-R [PMID: 30214903](https://pubmed.ncbi.nlm.nih.gov/30214903/).

**Natural disease in other species.** No naturally occurring SYNCRIP-related disease is documented in companion animals or wildlife (no OMIA entry noted). The animal involvement is **experimental** (model organisms), not natural disease.

**Comparative biology.** The temporal-identity function of Syp/hnRNP-Q is deeply conserved from flies to mammals: *Drosophila* uses the Imp→Syp gradient switch to program neuroblast temporal identity [PMID: 28394252](https://pubmed.ncbi.nlm.nih.gov/28394252/); [PMID: 38031099](https://pubmed.ncbi.nlm.nih.gov/38031099/), paralleling the mammalian radial-glial temporal program disrupted in disease. This conservation strengthens causal inference.

**Transmission / zoonosis.** Not applicable (genetic disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*, MGI).** The key model is a **conditional *Syncrip* knockout in radial glial cells**. Wu et al. (2025) showed this disrupts late-stage neurogenesis, stalls transcriptional progression, causes abnormal neuronal localization, superficial cortical-layer defects, and **learning/memory impairments** — recapitulating core features of the human disorder — and demonstrated that **human pathogenic mutations weaken phase separation** [PMID: 39776340](https://pubmed.ncbi.nlm.nih.gov/39776340/). This is the strongest model linking genotype to mechanism to phenotype.

**Drosophila (*D. melanogaster*, FlyBase).** The single ortholog *Syp* is a workhorse for dissecting neuroblast temporal identity (Imp→Syp switch) and activity-dependent synaptic plasticity (Msp300/Nesprin-1) [PMID: 28394252](https://pubmed.ncbi.nlm.nih.gov/28394252/); [PMID: 32040548](https://pubmed.ncbi.nlm.nih.gov/32040548/). It models progenitor-timing and synaptic functions but, as a single gene standing for two human paralogs, does not distinguish hnRNP-Q from hnRNP-R.

**Cellular / in vitro models.** Human neuroblastoma (SH-SY5Y) knockdown of hnRNP-Q/hnRNP-R revealed distinct downstream gene programs affecting neurodegeneration and inflammation pathways [PMID: 30214903](https://pubmed.ncbi.nlm.nih.gov/30214903/). Rodent hippocampal neurons demonstrated hnRNP-Q control of cytoskeletal (Cdc42/N-WASP/Arp2/3) mRNAs and neurite morphogenesis [PMID: 22493061](https://pubmed.ncbi.nlm.nih.gov/22493061/) and translational regulation under stress [PMID: 34944075](https://pubmed.ncbi.nlm.nih.gov/34944075/). In vitro biophysics characterized the unique acidic domain and its ATP/nucleic-acid binding relevant to phase separation [PMID: 27081926](https://pubmed.ncbi.nlm.nih.gov/27081926/); [PMID: 31791586](https://pubmed.ncbi.nlm.nih.gov/31791586/).

**Model characteristics.** The mouse conditional knockout **recapitulates** cortical layering defects and cognitive impairment. **Limitations:** models use complete loss (knockout) rather than the human heterozygous haploinsufficient state; the *Drosophila* single ortholog conflates paralog-specific functions; patient-derived iPSC/organoid models of specific variants are not yet reported. iPSC-derived cortical organoids carrying patient RRM2 missense or truncating variants would be a valuable next-generation model.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | How it supports findings |
|---|---|---|---|
| [27479843](https://pubmed.ncbi.nlm.nih.gov/27479843/) | *Meta-analysis of 2,104 trios... 10 new ID genes* | Human genetics | Statistically nominates SYNCRIP as an ID gene (F001) |
| [34157790](https://pubmed.ncbi.nlm.nih.gov/34157790/) | *Further evidence for de novo SYNCRIP variants* | Human clinical | Defines two variant classes; core phenotypes (F001) |
| [39776340](https://pubmed.ncbi.nlm.nih.gov/39776340/) | *Posttranscriptional control of neural progenitors by Syncrip* | Mouse / in vitro | Phase-separation mechanism; Notch/temporal-TF program; human mutations weaken LLPS (F002) |
| [27081926](https://pubmed.ncbi.nlm.nih.gov/27081926/) | *Acidic domain is a unique feature of SYNCRIP* | In vitro / structural | Protein architecture; unique acidic domain (F003) |
| [32040548](https://pubmed.ncbi.nlm.nih.gov/32040548/) | *Syncrip required for activity-induced Msp300* | Drosophila | Conserved synaptic-plasticity role (F003) |
| [22493061](https://pubmed.ncbi.nlm.nih.gov/22493061/) | *hnRNP Q regulates Cdc42-mediated morphogenesis* | Neuronal in vitro | Cytoskeletal mRNA regulation; neurite morphogenesis (F003) |
| [28394252](https://pubmed.ncbi.nlm.nih.gov/28394252/) | *Steroid-hormone induction of temporal gene expression* | Drosophila | Imp→Syp temporal switch (F003) |
| [38031099](https://pubmed.ncbi.nlm.nih.gov/38031099/) | *Imp in INPs and newborn neurons* | Drosophila | Imp/Syp gradients in progenitor timing (F003) |
| [30214903](https://pubmed.ncbi.nlm.nih.gov/30214903/) | *Gene expression profiles controlled by hnRNP Q and R* | In vitro | Paralog relationship; distinct downstream programs (F003, F008) |
| [31791586](https://pubmed.ncbi.nlm.nih.gov/31791586/) | *ATP binds nucleic-acid domains beyond RRM* | Biophysics | Acidic-domain ATP binding relevant to LLPS (F003) |
| [28393272](https://pubmed.ncbi.nlm.nih.gov/28393272/) | *Heterozygous HNRNPU variants cause epilepsy + ID* | Human clinical | Comparator hnRNPopathy (F008) |
| [39976380](https://pubmed.ncbi.nlm.nih.gov/39976380/) | *Expanding HNRNPU-related disorder spectrum* | Human clinical | Comparator hnRNPopathy phenotype (F008) |
| [29904177](https://pubmed.ncbi.nlm.nih.gov/29904177/) | *Au-Kline syndrome (HNRNPK)* | Human clinical | Comparator hnRNPopathy (F008) |
| [41325101](https://pubmed.ncbi.nlm.nih.gov/41325101/) | *RNArchitects: how hnRNPs shape neuronal landscapes* | Review | hnRNP dysfunction as convergent NDD mechanism (F008) |
| [32865115](https://pubmed.ncbi.nlm.nih.gov/32865115/) | *RNA-binding proteins in neurological disease* | Review | RBP dysregulation in NDD (F008) |

**Supporting database evidence (non-PMID):** gnomAD v2.1.1 constraint (pLI=1.00, LOEUF=0.228) for haploinsufficiency (F004); NCBI ClinVar (193 records; truncating-variant predominance) for variant spectrum (F005); GTEx v8 for ubiquitous expression vs CNS-selective disease (F006); QuickGO/UniProt O60506 for molecular functions (F007); Monarch Initiative for MONDO definition and sparse annotation.

---

## Limitations and Knowledge Gaps

1. **Tiny clinical cohort.** Fewer than ~10 published individuals; phenotype frequencies, penetrance, expressivity, and prognosis are provisional. No natural-history or registry data.
2. **No OMIM/ICD/Orphanet-specific identifiers** at the time of research, reflecting recent delineation and under-annotation (confirmed sparse in Monarch).
3. **Genotype–phenotype correlation is preliminary** — the truncating-more-severe-than-missense pattern rests on 3 individuals.
4. **Variant interpretation gap.** Most SYNCRIP missense variants are VUS (121/193 ClinVar records); functional assays are not routinely available clinically.
5. **Mechanistic models use complete knockout**, not the human heterozygous state; paralog redundancy (hnRNP-R) and its possible modifier role are untested in the disease context.
6. **No biomarkers, no episignature, no targeted therapy, and no disease-specific clinical trials.**
7. **No patient-derived iPSC/organoid models** of specific variants reported.

---

## Proposed Follow-up Experiments / Actions

1. **Cohort expansion via GeneMatcher/matchmaking** to assemble ≥20–30 individuals, enabling robust phenotype-frequency, penetrance, and genotype–phenotype analyses, and to seek an OMIM phenotype entry.
2. **Functional assays for VUS reclassification** — systematic RNA-binding (CLIP/EMSA) and phase-separation (in vitro droplet, cellular condensate) assays for recurrent missense variants.
3. **Patient-specific iPSC-derived cortical organoids** carrying truncating vs RRM2 missense variants, to test whether human heterozygous dosage reproduces the temporal-TF/Notch/layering defects seen in mouse knockouts and to quantify condensate deficits.
4. **Heterozygous (Syncrip⁺/⁻) and knock-in missense mouse models** to better mimic the human haploinsufficient state and to test paralog (hnRNP-R) modifier effects.
5. **Transcriptome/splicing profiling (RNA-seq)** of patient cells to search for a diagnostic aberrant-splicing or expression signature (potential biomarker/episignature analog).
6. **Mechanism-guided therapeutic exploration** — because the mechanism is haploinsufficiency, evaluate dosage-restoring strategies (e.g., ASO-mediated upregulation of the wild-type allele) in cellular/mouse models.
7. **Standardized natural-history data collection** (development, seizures, neuroimaging) to define prognosis and critical intervention windows.

---

## Consensus Answer

SYNCRIP-related neurodevelopmental disorder (MONDO:0800456) is a rare, autosomal-dominant, typically *de novo* Mendelian condition caused by heterozygous loss-of-function (frameshift/nonsense → haploinsufficiency) or RNA-recognition-motif missense variants in **SYNCRIP** (hnRNP-Q), presenting with intellectual disability, frequent autism spectrum features, and variable epilepsy and cortical malformation (e.g., periventricular nodular heterotopia). Mechanistically, insufficient hnRNP-Q impairs RNA binding and phase separation, disrupting the Notch-dependent temporal transcription-factor program by which radial glial cells build the cortex, yielding cortical layering defects and lifelong cognitive impairment; management is symptomatic with no disease-modifying therapy.


## Artifacts

- [OpenScientist final report](SYNCRIP-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SYNCRIP-related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 19 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800456` (3 mentions) - the report calls it "MONDO"; MONDO calls it **SYNCRIP-related neurodevelopmental disorder**
- `HP:0011283` (1 mention) - the report calls it "Neuroradiological"; HP calls it **Abnormal metencephalon morphology**
- `HP:0000750` (1 mention) - the report calls it "Cognitive/communicative"; HP calls it **Delayed speech and language development**
- `CL:0000129` (2 mentions) - the report calls it "radial glial cell / apical radial glia", "radial glial cells / apical progenitors"; CL calls it **microglial cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000729` (1 mention) - the report calls it "Behavioral"; HP calls it **Autistic behavior**
- `GO:0003723` (1 mention) - the report calls it "Molecular function:* RNA binding"; GO calls it **RNA binding**, and lists "poly(A) RNA binding" among its other names
- `GO:0017148` (2 mentions) - the report calls it "Biological process:* negative regulation of translation", "negative regulation of translation"; GO calls it **negative regulation of translation**
- `GO:0005634` (2 mentions) - the report calls it "Cellular component:* nucleus", "nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `GO:1990904` (2 mentions) - the report calls it "ribonucleoprotein complexes/granules"; GO calls it **ribonucleoprotein complex**
- `GO:0071013` (2 mentions) - the report calls it "spliceosome"; GO calls it **catalytic step 2 spliceosome**
- `CL:0000031` (2 mentions) - the report calls it "neuroblast", "neuroblasts/intermediate progenitors"; CL calls it **neuroblast (sensu Vertebrata)**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0017148` - called "Biological process:* negative regulation of translation", "negative regulation of translation"
- `GO:0005634` - called "Cellular component:* nucleus", "nucleus"
- `CL:0000031` - called "neuroblast", "neuroblasts/intermediate progenitors"
- `CL:0000129` - called "radial glial cell / apical radial glia", "radial glial cells / apical progenitors"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.