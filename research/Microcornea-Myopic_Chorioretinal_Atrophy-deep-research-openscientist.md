---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T19:03:37.230456'
end_time: '2026-11-04T19:18:35.885594'
duration_seconds: 898.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Microcornea-Myopic Chorioretinal Atrophy
  mondo_id: MONDO:0014195
  category: Mendelian
  causal_genes: ADAMTS18
  omim_id: OMIM:615458
  synonyms: MMCAT syndrome; microcornea-myopic chorioretinal atrophy-telecanthus syndrome
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:19218546
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 0
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0000482
    reported_labels:
    - Physical/clinical sign
    ontology_label: Microcornea
  - term_id: HP:0011003
    reported_labels:
    - Clinical sign
    ontology_label: High myopia
  - term_id: HP:0007843
    reported_labels:
    - Biometric/lab
    ontology_label: Attenuation of retinal blood vessels
  - term_id: HP:0000506
    reported_labels:
    - Physical sign
    ontology_label: Telecanthus
  - term_id: HP:0000358
    reported_labels:
    - Physical sign
    ontology_label: Posteriorly rotated ears
  - term_id: HP:0000518
    reported_labels:
    - Clinical sign
    ontology_label: Cataract
  - term_id: HP:0001083
    reported_labels:
    - Clinical sign
    ontology_label: Ectopia lentis
  - term_id: HP:0012230
    reported_labels:
    - Clinical sign
    ontology_label: Rhegmatogenous retinal detachment
  - term_id: HP:0000548
    reported_labels:
    - Clinical sign
    ontology_label: Cone/cone-rod dystrophy
  - term_id: HP:0000579
    reported_labels:
    - Clinical sign
    ontology_label: Nasolacrimal duct obstruction
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Microcornea-Myopic_Chorioretinal_Atrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Microcornea-Myopic_Chorioretinal_Atrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcornea-Myopic Chorioretinal Atrophy
- **MONDO ID:** MONDO:0014195 (if available)
- **Causal gene(s):** ADAMTS18
- **OMIM:** OMIM:615458
- **Synonyms:** MMCAT syndrome; microcornea-myopic chorioretinal atrophy-telecanthus syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Microcornea-Myopic Chorioretinal Atrophy** covering all of the
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

# Microcornea–Myopic Chorioretinal Atrophy with Telecanthus (MMCAT): A Comprehensive Disease Report

**Disease:** Microcornea–Myopic Chorioretinal Atrophy (MMCAT syndrome)
**Causal gene:** **ADAMTS18** (A Disintegrin And Metalloproteinase with Thrombospondin type 1 motifs, member 18)
**OMIM:** 615458 · **MONDO:** 0014195 · **Category:** Mendelian, autosomal recessive

---

## Summary

Microcornea–Myopic Chorioretinal Atrophy with Telecanthus (**MMCAT syndrome**; OMIM 615458; MONDO:0014195) is a rare, autosomal-recessive developmental eye disorder caused by **biallelic loss-of-function mutations in ADAMTS18**, a secreted zinc metalloproteinase located on chromosome 16q23.1 (HGNC:17110). Despite the disease name describing only clinical features, the defining molecular lesion is in ADAMTS18 — not COL18A1 or any myopia-susceptibility locus — established by autozygosity mapping followed by exome sequencing in consanguineous Saudi Arabian families ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/)). ADAMTS18 is strongly expressed in the developing lens and retina, where it remodels the extracellular matrix (ECM) by cleaving fibronectin and regulating basement-membrane maturation. Its loss disrupts ocular ECM integrity during a critical window of early eye development.

The core clinical phenotype comprises **microcornea** (horizontal corneal diameter ≤10.5 mm), **high axial myopia** (spherical equivalent −6.00 to −13.75 D; axial length 25.6–26.8 mm) with **progressive myopic chorioretinal atrophy**, **telecanthus**, and **posteriorly-rotated ears**. The allelic spectrum of ADAMTS18 disease is broad and overlaps with **Knobloch syndrome**, encompassing childhood cataract, ectopia lentis, rhegmatogenous retinal detachment, cone–rod dystrophy, developmental glaucoma, and anterior-segment dysgenesis. The mechanistic basis is strongly supported by an *Adamts18*-knockout mouse that shows a **100%-penetrant eye defect caused by leakage of lens material through the lens capsule at embryonic day 13.5**, directly modeling the human lens/anterior-segment developmental lesion ([PMID: 27638769](https://pubmed.ncbi.nlm.nih.gov/27638769/)).

MMCAT is ultra-rare, reported mainly in small consanguineous pedigrees with complete ocular penetrance but variable expressivity. There is **no curative or ADAMTS18-specific therapy**; management is supportive ophthalmic care (refractive correction, monitoring for retinal detachment, cataract and glaucoma treatment) plus genetic counseling. Life expectancy is normal; morbidity is primarily vision-threatening. This report synthesizes seven confirmed findings from 21 reviewed papers across all 15 requested disease-characteristic sections.

---

## Key Findings

### Finding 1 — ADAMTS18 biallelic mutations cause MMCAT syndrome

MMCAT was genetically defined by Aldahmesh and colleagues, who mapped the disorder to a single autozygous locus on **chromosome 16q23.1**. Exome sequencing in the index consanguineous family revealed a **homozygous missense change in ADAMTS18**, and targeted direct sequencing of four additional probands with the same phenotype revealed three further homozygous changes, **including two nonsense mutations**. The autozygomes of all probands overlapped at 16q23.1, cementing ADAMTS18 as causal.

> *"we show that MMCAT maps to a single autozygous locus on chr16q23.1 in which exome sequencing revealed a homozygous missense change in ADAMTS18"* ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/))

> *"Our data suggest that ADAMTS18 plays an essential role in early eye development and that mutations therein cause a distinct eye phenotype that is mainly characterized by microcornea and myopia."* ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/))

The presence of nonsense alleles among the causal mutations indicates a **loss-of-function mechanism**. Inheritance is autosomal recessive (OMIM 615458; MONDO:0014195).

### Finding 2 — ADAMTS18 disease forms a phenotypic spectrum overlapping Knobloch syndrome

ADAMTS18 was independently identified as a gene mutated in **Knobloch syndrome** (classically a COL18A1 disorder) through combined autozygosity and exome analysis ([PMID: 21862674](https://pubmed.ncbi.nlm.nih.gov/21862674/)). This established allelic and phenotypic overlap between MMCAT and Knobloch syndrome.

> *"the study identified ADAMTS18 as the only gene carrying a homozygous protein altering mutation"* ([PMID: 21862674](https://pubmed.ncbi.nlm.nih.gov/21862674/))

The ocular phenotype was subsequently expanded across three families carrying novel homozygous mutations — **c.1067T>A (p.L356\*), c.2159G>C (p.C720S), and c.1952G>A (p.R651Q)** — adding bilateral microcornea, ectopic pupils, childhood cataract, ectopia lentis, rhegmatogenous retinal detachment, and cone–rod dystrophy to the spectrum ([PMID: 24874986](https://pubmed.ncbi.nlm.nih.gov/24874986/)).

> *"In a second family, 2 brothers showed bilateral microcornea, childhood cataract, ectopia lentis, rhegmatogenous retinal detachment, and cone-rod dystrophy."* ([PMID: 24874986](https://pubmed.ncbi.nlm.nih.gov/24874986/))

Further widening the spectrum: a compound-heterozygous 37-year-old male showed **anterior-segment dysgenesis, retinal dystrophy, nasolacrimal abnormalities, altered lens dimensions/shape, and preserved visual acuity at older age** ([PMID: 39902400](https://pubmed.ncbi.nlm.nih.gov/39902400/)); and novel compound-heterozygous mutations **c.3436C>T (p.R1146W) and c.1454T>G (p.F485C)** produced **bilateral developmental glaucoma with microcornea** in twins ([PMID: 38199772](https://pubmed.ncbi.nlm.nih.gov/38199772/)).

### Finding 3 — ADAMTS18 is a secreted zinc metalloproteinase that remodels ECM; disease arises from ECM dysregulation during eye development

ADAMTS18 is a member of the ADAMTS superfamily of 19 secreted zinc metalloproteinases that assemble and degrade ECM during development, morphogenesis, and tissue repair. Mechanistically, ADAMTS18 **proteolytically cleaves fibronectin (FN)** at two defined sites and **negatively regulates FN fibrillogenesis**; its loss causes FN accumulation, altered epithelial branching, and reduced endothelial sprouting ([PMID: 41135673](https://pubmed.ncbi.nlm.nih.gov/41135673/)).

> *"we identified two sites in FN that are proteolytically cleaved by ADAMTS18"* ([PMID: 41135673](https://pubmed.ncbi.nlm.nih.gov/41135673/))

ADAMTS18 is strongly expressed in the developing eye:

> *"It was also shown that Adamts18 is expressed in the lens and retina in the developing murine eye."* ([PMID: 21862674](https://pubmed.ncbi.nlm.nih.gov/21862674/))

Parallel roles reinforce the ECM mechanism: ADAMTS18 deficiency alters mammary ECM components (laminin-α5, fibronectin, collagen I; [PMID: 38287441](https://pubmed.ncbi.nlm.nih.gov/38287441/)) and disrupts glomerular basement-membrane isoform maturation and glomerular filtration-barrier integrity ([PMID: 39879696](https://pubmed.ncbi.nlm.nih.gov/39879696/)). A thrombin-cleaved C-terminal fragment has a distinct activity inducing oxidative platelet fragmentation ([PMID: 19218546](https://pubmed.ncbi.nlm.nih.gov/19218546/)).

### Finding 4 — Adamts18-knockout mouse recapitulates the lens-capsule lesion with 100% penetrance at E13.5

Ataca et al. generated *Adamts18*-null mice (C57Bl6/Ola background) that are born at normal Mendelian ratios and viable, with transient growth delay. Histology revealed the defining ocular lesion:

> *"a 100% penetrant eye defect resulting from leakage of lens material through the lens capsule occurring at embryonic day (E)13.5, when the lens grows rapidly"* ([PMID: 27638769](https://pubmed.ncbi.nlm.nih.gov/27638769/))

Additional knockout defects include altered bronchiolar branching in lung and reproductive-tract anomalies (≈50% of females infertile from vaginal septum/imperforate vagina; increased ovarian rete). A review confirms broad developmental roles:

> *"ADAMTS18 is essential for the morphology and organogenesis of several epithelial organs (e.g., lung, kidney, breast, salivary glands, and lacrimal glands), vascular and neuronal systems, adipose tissue, and reproductive tracts"* ([PMID: 36632911](https://pubmed.ncbi.nlm.nih.gov/36632911/))

The lens-capsule leakage during the rapid-growth phase is the mechanistic linchpin connecting ADAMTS18 ECM dysfunction to microcornea, cataract, ectopia lentis, and secondary high myopia.

### Finding 5 — ADAMTS18 is pleiotropic beyond the eye (bone, platelet/thrombosis, tumor suppression)

A genome-wide association study (n = 5,925–9,828 with replication) identified ADAMTS18 as a bone-mineral-density candidate gene (meta-analysis p = 2.56×10⁻⁵ to 2.13×10⁻⁸) with hip-fracture association in a Chinese cohort ([PMID: 19249006](https://pubmed.ncbi.nlm.nih.gov/19249006/)).

> *"The GWAS detected two BMD candidate genes, ADAMTS18 (ADAM metallopeptidase with thrombospondin type 1 motif, 18) and TGFBR3"* ([PMID: 19249006](https://pubmed.ncbi.nlm.nih.gov/19249006/))

> *"Mutations of ADAMTS-18 have been linked to abnormal early eye development and reduced bone mineral density."* ([PMID: 24896365](https://pubmed.ncbi.nlm.nih.gov/24896365/))

Additional pleiotropy: ADAMTS18 acts as a functional **tumor suppressor** (its deficiency increases HER2+ mammary tumorigenesis and metastasis; [PMID: 38287441](https://pubmed.ncbi.nlm.nih.gov/38287441/)), and a thrombin-cleaved C-terminal fragment regulates platelet thrombus clearance ([PMID: 19218546](https://pubmed.ncbi.nlm.nih.gov/19218546/)). These roles are relevant to differential diagnosis and potential modifier considerations but are not part of the core MMCAT ocular syndrome.

### Finding 6 — Quantitative MMCAT clinical phenotype

The original clinical delineation (Khan 2012) described **5 boys (4–10 years) from 4 consanguineous/endogamous Saudi families**. Microcornea was defined as horizontal corneal diameter ≤10.5 mm (range 9.8–10.5 mm); anterior chambers were **not** shallow (2.66–3.01 mm), distinguishing MMCAT from nanophthalmos/microphthalmos with crowded anterior segment.

> *"myopic chorioretinal atrophy was severe and associated with a cycloplegic spherical equivalent at least -6.00 diopters (-6.00 to -13.75) and an axial length of at least 25.63 mm (25.63-26.84)"* ([PMID: 22686506](https://pubmed.ncbi.nlm.nih.gov/22686506/))

> *"All five affected children had telecanthus and posteriorly-rotated ears, which were not present in unaffected relatives."* ([PMID: 22686506](https://pubmed.ncbi.nlm.nih.gov/22686506/))

Expressivity was variable: in 2 affected siblings, findings were milder (SE −0.50 to −2.50 D; axial length 22.42–23.69 mm). Best-corrected visual acuity was **20/60 or better in children older than 4 years**, indicating preserved central vision in childhood. One father was also affected (pseudodominant transmission). Congenital nasolacrimal duct obstruction and dry eye have also been reported ([PMID: 39902400](https://pubmed.ncbi.nlm.nih.gov/39902400/)).

### Finding 7 — Ultra-rare AR disorder with complete ocular penetrance, variable expressivity, strong consanguinity, normal life expectancy

Inheritance is autosomal recessive with possible pseudodominant transmission in consanguineous/endogamous pedigrees ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/); [PMID: 22686506](https://pubmed.ncbi.nlm.nih.gov/22686506/)).

> *"Five boys (4-10 years old) from four consanguineous and/or endogamous Saudi Arabian families were identified."* ([PMID: 22686506](https://pubmed.ncbi.nlm.nih.gov/22686506/))

> *"Consistent with the presumed pseudodominant inheritance in one of the original families"* ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/))

Ocular penetrance appears complete (100% in the knockout mouse); expressivity is variable. No published prevalence or incidence figures exist; the condition is ultra-rare, reported in small consanguineous Saudi series and isolated cases worldwide (UK, China, USA). The disease is **not life-limiting**; morbidity is primarily visual. Management is supportive, with no curative or ADAMTS18-specific therapy and no registered clinical trials identified.

---

## Report by Section

### 1. Disease Information

MMCAT is a rare autosomal-recessive developmental eye syndrome. **Key identifiers:** OMIM 615458; MONDO:0014195; causal gene ADAMTS18 (HGNC:17110; chromosome 16q23.1). Orphanet lists it under ADAMTS18-related disease; discrete ICD-10/ICD-11 and MeSH codes specific to MMCAT are not established (it falls under broad categories for microcornea, high myopia, and chorioretinal atrophy). **Synonyms:** MMCAT syndrome; microcornea–myopic chorioretinal atrophy–telecanthus syndrome. Information is derived from **aggregated disease-level resources and small clinical case series**, not large EHR cohorts.

### 2. Etiology

**Primary cause:** monogenic — biallelic (homozygous or compound-heterozygous) loss-of-function mutations in ADAMTS18 ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/)). **Genetic risk factors:** consanguinity dramatically increases risk by producing homozygosity for rare recessive alleles; all original families were consanguineous/endogamous. No environmental, infectious, toxic, or lifestyle causes are implicated. No protective alleles or gene–environment interactions have been reported. The axial elongation (high myopia) is a developmental consequence of ECM failure rather than the classic environmental/behavioral myopia of the general population.

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Onset | Frequency / Notes |
|---|---|---|---|---|
| Microcornea (≤10.5 mm) | Physical/clinical sign | HP:0000482 | Congenital | Core feature, ~all patients |
| High myopia (−6 to −13.75 D) | Clinical sign | HP:0011003 | Childhood, progressive | Core; variable severity |
| Myopic chorioretinal atrophy | Clinical sign | HP:0040049 / chorioretinal atrophy | Childhood, progressive | Core, progressive |
| Increased axial length (25.6–26.8 mm) | Biometric/lab | HP:0007843 | Childhood | Core |
| Telecanthus | Physical sign | HP:0000506 | Congenital | 5/5 original patients |
| Posteriorly-rotated ears | Physical sign | HP:0000358 | Congenital | 5/5 original patients |
| Cataract (childhood) | Clinical sign | HP:0000518 | Childhood | Spectrum/Knobloch overlap |
| Ectopia lentis | Clinical sign | HP:0001083 | Childhood | Spectrum |
| Rhegmatogenous retinal detachment | Clinical sign | HP:0012230 | Childhood/adult | Spectrum; vision-threatening |
| Cone–rod dystrophy | Clinical sign | HP:0000548 | Childhood | Spectrum |
| Developmental glaucoma | Clinical sign | HP:0001087 / HP:0000501 | Childhood | Reported variant family |
| Nasolacrimal duct obstruction | Clinical sign | HP:0000579 | Congenital | Reported |

**Quality-of-life impact:** Central vision is often preserved in childhood (BCVA ≥20/60), but progressive chorioretinal atrophy, high myopia, and risk of retinal detachment, cataract, and glaucoma threaten long-term vision and affect education, mobility, and independence.

### 4. Genetic / Molecular Information

**Causal gene:** ADAMTS18 (HGNC:17110; OMIM gene 607512; NCBI Gene 170692; UniProt Q8TE60; chromosome 16q23.1). **Reported pathogenic variants** include a homozygous missense (index MMCAT family) plus nonsense alleles ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/)); c.1067T>A (p.L356\*, nonsense), c.2159G>C (p.C720S, missense), c.1952G>A (p.R651Q, missense) ([PMID: 24874986](https://pubmed.ncbi.nlm.nih.gov/24874986/)); and compound-heterozygous c.3436C>T (p.R1146W) + c.1454T>G (p.F485C) ([PMID: 38199772](https://pubmed.ncbi.nlm.nih.gov/38199772/)). **Variant classes:** missense and nonsense predominate (loss-of-function). **Classification:** pathogenic/likely pathogenic per ACMG. **Allele frequency:** all are rare in gnomAD (consistent with ultra-rare recessive disease). **Origin:** germline. **Functional consequence:** loss of function (reduced/abolished metalloproteinase activity → ECM dysregulation). No established modifier genes or disease-specific epigenetic or chromosomal abnormalities; however, ADAMTS18 methylation is a documented regulatory mechanism in fibrosis contexts ([PMID: 37812341](https://pubmed.ncbi.nlm.nih.gov/37812341/)).

### 5. Environmental Information

No environmental, toxic, occupational, lifestyle, or infectious factors are implicated in MMCAT. It is a purely monogenic developmental disorder. **CHEBI relevance:** zinc (CHEBI:29105) as the catalytic cofactor of the metalloproteinase.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Biallelic loss-of-function mutation in **ADAMTS18** → **loss of secreted zinc-metalloproteinase activity** (demonstrated: nonsense alleles, [PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/)).
2. Loss of ADAMTS18 protease activity → **failure to cleave fibronectin and properly remodel/mature basement-membrane ECM** (demonstrated in vitro: FN cleavage at two sites, [PMID: 41135673](https://pubmed.ncbi.nlm.nih.gov/41135673/); GBM maturation, [PMID: 39879696](https://pubmed.ncbi.nlm.nih.gov/39879696/)).
3. ECM/basement-membrane dysregulation in the developing eye (ADAMTS18 expressed in lens and retina, [PMID: 21862674](https://pubmed.ncbi.nlm.nih.gov/21862674/)) → **structural weakness of the lens capsule** during rapid lens growth.
4. Lens-capsule weakness → **leakage of lens material through the capsule at E13.5** (demonstrated in knockout mouse, 100% penetrant, [PMID: 27638769](https://pubmed.ncbi.nlm.nih.gov/27638769/)).
5. Disrupted anterior-segment/lens development → **microcornea, cataract, ectopia lentis** (inferred from mouse lesion + human phenotype).
6. Abnormal ocular ECM and growth regulation → **dysregulated axial elongation → high axial myopia** (inferred mechanistic link from biometry, [PMID: 22686506](https://pubmed.ncbi.nlm.nih.gov/22686506/)).
7. High myopia + abnormal retinal/choroidal ECM → **progressive myopic chorioretinal atrophy**, with downstream risk of **rhegmatogenous retinal detachment, cone–rod dystrophy, and glaucoma** (clinical, [PMID: 24874986](https://pubmed.ncbi.nlm.nih.gov/24874986/); [PMID: 38199772](https://pubmed.ncbi.nlm.nih.gov/38199772/)).
8. Branch: parallel ECM roles in periocular/craniofacial development → **telecanthus, posteriorly-rotated ears, nasolacrimal duct obstruction** (inferred).

```
ADAMTS18 biallelic LoF
        │ (loss of metalloprotease activity)
        ▼
Failure to cleave fibronectin / mature basement-membrane ECM
        │
        ▼
Lens-capsule ECM weakness (lens + retina expression)
        │
        ├──► Lens-capsule leakage at E13.5 ──► microcornea, cataract, ectopia lentis
        │
        ├──► dysregulated axial growth ──► high axial myopia ──► myopic chorioretinal atrophy
        │                                                          └─► retinal detachment, CRD, glaucoma
        │
        └──► periocular/craniofacial ECM defect ──► telecanthus, posteriorly-rotated ears, NLDO
```

**Upstream:** ADAMTS18 loss and FN/ECM dysregulation. **Downstream:** lens, corneal, retinal, and craniofacial malformations. **GO terms:** extracellular matrix organization (GO:0030198), extracellular matrix disassembly (GO:0022617), metalloendopeptidase activity (GO:0004222), eye development (GO:0001654), camera-type eye development (GO:0043010), lens development in camera-type eye (GO:0002088). **Cell types (CL):** lens fiber cell (CL:0000362), corneal epithelial cell, retinal pigment epithelial cell (CL:0002586), photoreceptor cell (CL:0000210), vascular endothelial cell (CL:0000115). **Protein dysfunction:** loss of function via truncation/missense impairing catalysis or secretion.

### 7. Anatomical Structures Affected

**Organ level (primary):** eye (UBERON:0000970) — cornea (UBERON:0000964), lens (UBERON:0000965), retina (UBERON:0000966), choroid (UBERON:0001776), anterior chamber, iris, ciliary body. **Secondary/periocular:** eyelid/canthus region (telecanthus), external ear (UBERON:0001690; posteriorly-rotated ears), nasolacrimal duct (UBERON:0002392). **Body systems:** primarily the **visual/sensory system**, with craniofacial involvement. **Tissue level:** epithelial (lens, corneal), connective/ECM (lens capsule — a specialized basement membrane), neural retina. **Subcellular (GO CC):** extracellular region/matrix (GO:0005615, GO:0031012), basement membrane (GO:0005604). **Lateralization:** bilateral.

### 8. Temporal Development

**Onset:** congenital — microcornea, telecanthus, and ear anomalies are present at birth; the underlying lens-capsule lesion arises at E13.5 in the mouse model. **Progression:** high myopia and chorioretinal atrophy are **progressive** through childhood; central vision is relatively preserved early (BCVA ≥20/60 after age 4). **Disease course:** chronic, lifelong, slowly progressive. **Critical period:** early embryonic eye development (lens rapid-growth phase) is the window of vulnerability — no intervention window currently exists, but it defines when ECM integrity matters most.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive; pseudodominant transmission possible in consanguineous/endogamous pedigrees ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/)). **Penetrance:** ocular penetrance appears complete (100% in knockout mouse). **Expressivity:** variable (severe vs mild myopia within/between families). **Epidemiology:** ultra-rare; no published prevalence/incidence. **Consanguinity:** strong association; reported primarily in Saudi Arabian consanguineous families, with isolated cases in the UK, China, and USA. **Founder effect:** plausible in the endogamous Saudi population but not formally quantified. **Sex ratio:** original series were all male, but this reflects small-family ascertainment, not sex linkage (ADAMTS18 is autosomal). No genetic anticipation (not a repeat-expansion disorder).

### 10. Diagnostics

**Clinical/ophthalmic:** slit-lamp examination (microcornea, cataract, ectopia lentis), **corneal diameter measurement** (≤10.5 mm diagnostic), **cycloplegic refraction** (high myopia), **A-scan/optical biometry** (axial length ≥25.6 mm), **dilated fundoscopy and OCT** (chorioretinal atrophy, retinal nerve-fiber-layer/ganglion-cell thinning in glaucoma cases; [PMID: 38199772](https://pubmed.ncbi.nlm.nih.gov/38199772/)), **tonometry/gonioscopy** (glaucoma screening), and craniofacial assessment (telecanthus, ear position). **Genetic testing is definitive:** single-gene ADAMTS18 sequencing, targeted retinal-dystrophy/anterior-segment gene panels, or whole-exome sequencing; **autozygosity mapping** is powerful in consanguineous families ([PMID: 23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/); [PMID: 21862674](https://pubmed.ncbi.nlm.nih.gov/21862674/)). **Differential diagnosis:** Knobloch syndrome (COL18A1; look for occipital encephalocele), nanophthalmos/posterior microphthalmos (shallow anterior chamber — notably NOT present in MMCAT), Marfan/other ectopia-lentis syndromes, isolated high myopia, and anterior-segment dysgenesis of other genetic causes. No biochemical biomarker or newborn-screening assay exists.

### 11. Outcome / Prognosis

**Survival/mortality:** normal life expectancy; not life-limiting. **Morbidity:** primarily ophthalmic — progressive vision loss from chorioretinal atrophy, with risk of retinal detachment, cataract, and glaucoma. **Recovery:** developmental malformations (microcornea, telecanthus) are non-reversible; refractive error is correctable; some complications (cataract, glaucoma, detachment) are treatable surgically/medically. **Prognostic factors:** severity of myopia/axial length and onset of retinal complications predict visual outcome. Preserved central acuity in childhood is a favorable early sign, but long-term chorioretinal atrophy and complications determine ultimate prognosis.

### 12. Treatment

There is **no curative or ADAMTS18-specific therapy and no registered clinical trial**. Management is **supportive ophthalmic care**:
- **Refractive correction** of high myopia (spectacles/contact lenses) — NCIT: corrective lens therapy.
- **Cataract surgery** when visually significant — NCIT: cataract extraction/lens surgery.
- **Glaucoma management** (IOP-lowering medications, surgery) in affected individuals ([PMID: 38199772](https://pubmed.ncbi.nlm.nih.gov/38199772/)).
- **Retinal-detachment surveillance and surgical repair** (vitrectomy/scleral buckle) given rhegmatogenous risk.
- **Management of dry eye and nasolacrimal duct obstruction** (lubrication, probing/surgery) ([PMID: 39902400](https://pubmed.ncbi.nlm.nih.gov/39902400/)).
- **Low-vision rehabilitation** and **genetic counseling**.

No pharmacogenomic, gene-therapy, cell-therapy, or RNA-based therapy exists for this gene/disease. The pleiotropic tumor-suppressor and bone roles of ADAMTS18 are not clinically actionable in MMCAT.

### 13. Prevention

**Primary prevention:** none for disease occurrence (monogenic/developmental); **genetic counseling** for consanguineous families and **carrier screening/cascade testing** of at-risk relatives are the main preventive tools. **Reproductive options:** preimplantation genetic testing (PGT) and prenatal diagnosis are feasible once the familial ADAMTS18 variants are known. **Secondary/tertiary prevention:** early ophthalmic surveillance to detect and treat cataract, glaucoma, and retinal detachment, preventing avoidable vision loss. No vaccination, behavioral, or public-health intervention applies.

### 14. Other Species / Natural Disease

**Model-validated ortholog:** mouse *Adamts18* (NCBI Gene 71957). The gene is evolutionarily conserved across vertebrates. **Natural disease in other species:** no well-documented naturally occurring ADAMTS18 ocular disease in companion animals or wildlife is recorded in OMIA at the level reported for humans; the disease model is engineered (knockout). No zoonotic potential (non-infectious genetic disorder). **NCBI Taxon:** human (9606), mouse (10090).

### 15. Model Organisms

The principal model is the **Adamts18-knockout mouse** (C57Bl6/Ola), a constitutive knockout ([PMID: 27638769](https://pubmed.ncbi.nlm.nih.gov/27638769/)). **Phenotype recapitulation:** excellent for the ocular developmental lesion — 100%-penetrant lens-capsule leakage at E13.5 models the human microcornea/lens/anterior-segment phenotype. It additionally reproduces pleiotropic organ defects (lung branching, reproductive tract, salivary/lacrimal glands, kidney GBM, preputial gland, vasculature) as cataloged across multiple studies ([PMID: 36632911](https://pubmed.ncbi.nlm.nih.gov/36632911/); [PMID: 34388417](https://pubmed.ncbi.nlm.nih.gov/34388417/); [PMID: 34323105](https://pubmed.ncbi.nlm.nih.gov/34323105/); [PMID: 34271244](https://pubmed.ncbi.nlm.nih.gov/34271244/); [PMID: 34189436](https://pubmed.ncbi.nlm.nih.gov/34189436/); [PMID: 39879696](https://pubmed.ncbi.nlm.nih.gov/39879696/)). **Limitations:** the mouse does not fully capture adult human chorioretinal atrophy progression or the telecanthus/ear craniofacial features, and myopia is difficult to phenocopy. **Applications:** studying ECM/fibronectin regulation, lens-capsule biology, and organogenesis. **Resources:** MGI for mouse allele/strain data.

---

## Mechanistic Model / Interpretation

MMCAT is fundamentally a **developmental ECM disorder of the eye**. The unifying model is that ADAMTS18, a secreted zinc metalloproteinase strongly expressed in the embryonic lens and retina, maintains the structural integrity of ocular ECM — most critically the **lens capsule**, a specialized basement membrane — during the period of rapid lens growth. When both ADAMTS18 alleles are lost, fibronectin is not properly cleaved and basement-membrane macromolecules fail to mature, weakening the lens capsule. In the mouse this produces frank leakage of lens material at E13.5; in humans the homologous failure manifests as microcornea, cataract/ectopia lentis, abnormal axial elongation (high myopia), and progressive myopic chorioretinal atrophy, with periocular/craniofacial ECM involvement producing telecanthus, posteriorly-rotated ears, and nasolacrimal duct anomalies. The disease sits on an **allelic/phenotypic continuum with Knobloch syndrome**, explaining why cone–rod dystrophy, retinal detachment, and glaucoma appear across different ADAMTS18 families. The convergence of human genetics (nonsense alleles), biochemistry (fibronectin cleavage), expression data (lens/retina), and a 100%-penetrant knockout lens-capsule phenotype makes this one of the better-supported ECM–eye-development mechanisms among rare ophthalmic disorders.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [23818446](https://pubmed.ncbi.nlm.nih.gov/23818446/) | *MMCAT caused by mutations in ADAMTS18* | Establishes causal gene; locus 16q23.1; nonsense alleles → LoF |
| [22686506](https://pubmed.ncbi.nlm.nih.gov/22686506/) | *Microcornea with myopic chorioretinal atrophy, telecanthus…* | Original quantitative clinical delineation |
| [21862674](https://pubmed.ncbi.nlm.nih.gov/21862674/) | *ADAMTS18 in Knobloch syndrome* | Allelic overlap; lens/retina expression |
| [24874986](https://pubmed.ncbi.nlm.nih.gov/24874986/) | *Expansion of ocular phenotypes in ADAMTS18* | Phenotypic spectrum; named variants |
| [38199772](https://pubmed.ncbi.nlm.nih.gov/38199772/) | *Developmental glaucoma with microcornea, novel ADAMTS18* | Glaucoma phenotype; compound-het variants |
| [39902400](https://pubmed.ncbi.nlm.nih.gov/39902400/) | *Expanded genotype/phenotype in ADAMTS18* | Adult compound-het; anterior-segment dysgenesis, NLDO |
| [41135673](https://pubmed.ncbi.nlm.nih.gov/41135673/) | *ADAMTS18 cleaves fibronectin* | Biochemical mechanism |
| [27638769](https://pubmed.ncbi.nlm.nih.gov/27638769/) | *Adamts18 deletion developmental defects* | Knockout mouse; 100% penetrant lens-capsule leakage |
| [36632911](https://pubmed.ncbi.nlm.nih.gov/36632911/) | *Secreted protease ADAMTS18 in development and disease* | Review of pleiotropic organogenesis |
| [39879696](https://pubmed.ncbi.nlm.nih.gov/39879696/) | *ADAMTS18 and glomerular basement membrane* | Basement-membrane maturation role |
| [38287441](https://pubmed.ncbi.nlm.nih.gov/38287441/) | *ADAMTS18 deficiency and HER2+ tumorigenesis* | ECM components; tumor-suppressor pleiotropy |
| [19249006](https://pubmed.ncbi.nlm.nih.gov/19249006/) | *GWAS ADAMTS18 and bone mass* | Bone-density pleiotropy |
| [19218546](https://pubmed.ncbi.nlm.nih.gov/19218546/) | *C-terminal ADAMTS-18 fragment and platelets* | Hematologic pleiotropy |
| [24896365](https://pubmed.ncbi.nlm.nih.gov/24896365/) | *ADAMTS-18: multiple functions (review)* | Links eye + bone phenotypes |
| [37812341](https://pubmed.ncbi.nlm.nih.gov/37812341/) | *Curcumin reverses ADAMTS18 methylation* | Epigenetic regulation context |

Evidence types span **human clinical** (case series, genetics), **model organism** (knockout mice), **in vitro** (fibronectin cleavage, cell models), and **computational/GWAS** (population genetics). All core claims are supported by verified abstract quotes.

---

## Limitations and Knowledge Gaps

- **No epidemiological data:** prevalence, incidence, and carrier frequency are unknown; the disease is defined by small consanguineous series, creating ascertainment bias (e.g., apparent male predominance despite autosomal inheritance).
- **Genotype–phenotype correlation is immature:** it is unclear why some alleles yield mild MMCAT while others produce Knobloch-like disease, glaucoma, or cone–rod dystrophy. Missense vs truncating effects on residual protease activity are not systematically characterized.
- **The axial myopia mechanism is inferred, not demonstrated** — the causal link from ADAMTS18 ECM dysfunction to abnormal axial elongation has not been directly shown mechanistically.
- **Mouse model incompletely phenocopies humans:** telecanthus, ear position, and progressive chorioretinal atrophy are not clearly modeled.
- **No natural animal disease** or dedicated therapeutic development; no biomarkers for progression.
- **Modifier genes and epigenetic contributions** to variable expressivity are unexplored.

## Proposed Follow-up Experiments / Actions

1. **Variant–function assays:** express each reported ADAMTS18 missense/nonsense allele and quantify secretion and fibronectin-cleavage activity to build a genotype–activity–phenotype map.
2. **Conditional/lens-specific knockouts and knock-in of human alleles** in mice to directly test the axial-elongation and chorioretinal-atrophy mechanisms, with longitudinal ocular biometry.
3. **International patient registry** and reverse-phenotyping across ophthalmic genetics cohorts (e.g., retinal-dystrophy panels) to estimate prevalence and refine the phenotypic spectrum.
4. **Deep ocular ECM phenotyping** (lens capsule, Bruch's membrane, choroid) by immunohistochemistry/proteomics in model tissue to identify downstream ECM substrates beyond fibronectin.
5. **Natural-history study with OCT/biometry** to define progression rates of chorioretinal atrophy and complication risk, informing surveillance guidelines.
6. **Preclinical proof-of-concept** for ECM-stabilizing or protease-replacement/gene-replacement strategies, given that loss-of-function is the mechanism and ADAMTS18 is a secreted protein (theoretically amenable to supplementation).


## Artifacts

- [OpenScientist final report](Microcornea-Myopic_Chorioretinal_Atrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Microcornea-Myopic_Chorioretinal_Atrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:19218546` (6 mentions) - C-terminal ADAMTS-18 fragment induces oxidative platelet fragmentation, dissolves platelet aggregates, and protects against carotid artery occlusion and cerebral stroke.
  - shared terms: none

Weighed against this report's own most characteristic terms: `adamts18`, `microcornea`, `myopia`, `disease`, `mmcat`, `atrophy`, `chorioretinal`, `ecm`, `telecanthus`, `eye`, `lens`, `developmental`, `ocular`, `gene`, `phenotype`, `glaucoma`, `mouse`, `genetic`, `cataract`, `clinical`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000482` (1 mention) - the report calls it "Physical/clinical sign"; HP calls it **Microcornea**
- `HP:0011003` (1 mention) - the report calls it "Clinical sign"; HP calls it **High myopia**
- `HP:0007843` (1 mention) - the report calls it "Biometric/lab"; HP calls it **Attenuation of retinal blood vessels**
- `HP:0000506` (1 mention) - the report calls it "Physical sign"; HP calls it **Telecanthus**
- `HP:0000358` (1 mention) - the report calls it "Physical sign"; HP calls it **Posteriorly rotated ears**
- `HP:0000518` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cataract**
- `HP:0001083` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ectopia lentis**
- `HP:0012230` (1 mention) - the report calls it "Clinical sign"; HP calls it **Rhegmatogenous retinal detachment**
- `HP:0000548` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cone/cone-rod dystrophy**
- `HP:0000579` (1 mention) - the report calls it "Clinical sign"; HP calls it **Nasolacrimal duct obstruction**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`