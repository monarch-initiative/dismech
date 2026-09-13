---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-13T20:52:48.072689'
end_time: '2026-09-13T21:25:50.721532'
duration_seconds: 1982.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Sensory and Autonomic Neuropathy Type 1E
  mondo_id: MONDO:0013584
  category: Mendelian
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 32
  not_found: 0
  obsolete: 4
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 0
  labels_mismatched: 21
  mislabelled_terms:
  - term_id: MONDO:0013584
    reported_labels:
    - MONDO
    ontology_label: hereditary sensory neuropathy-deafness-dementia syndrome
  - term_id: DOID:0070158
    reported_labels:
    - Disease Ontology (DOID)
    ontology_label: hereditary sensory neuropathy type 1E
  - term_id: HP:0007328
    reported_labels:
    - Clinical sign
    ontology_label: Impaired pain sensation
  - term_id: HP:0010829
    reported_labels:
    - Clinical sign
    ontology_label: Impaired temperature sensation
  - term_id: HP:0002495
    reported_labels:
    - Clinical sign
    ontology_label: Impaired vibratory sensation
  - term_id: HP:0000763
    reported_labels:
    - Clinical sign
    ontology_label: Sensory neuropathy
  - term_id: HP:0003477
    reported_labels:
    - Clinical sign
    ontology_label: Peripheral axonal neuropathy
  - term_id: HP:0200042
    reported_labels:
    - Physical manifestation
    ontology_label: Skin ulcer
  - term_id: HP:0002754
    reported_labels:
    - Physical manifestation
    ontology_label: Osteomyelitis
  - term_id: HP:0002828
    reported_labels:
    - Physical manifestation
    ontology_label: Multiple joint contractures
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000726
    reported_labels:
    - Clinical sign
    ontology_label: Dementia
  - term_id: HP:0002145
    reported_labels:
    - Clinical sign
    ontology_label: Frontotemporal dementia
  - term_id: HP:0000751
    reported_labels:
    - Behavioral
    ontology_label: Personality changes
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0002459
    reported_labels:
    - Clinical sign
    ontology_label: obsolete Dysautonomia
  - term_id: HP:0030050
    reported_labels:
    - Clinical sign
    ontology_label: obsolete Narcolepsy
  - term_id: HP:0002524
    reported_labels:
    - Clinical sign
    ontology_label: Cataplexy
  - term_id: HP:0002059
    reported_labels:
    - Imaging
    ontology_label: Cerebral atrophy
  - term_id: HP:0001272
    reported_labels:
    - Imaging
    ontology_label: Cerebellar atrophy
  - term_id: HP:0001251
    reported_labels:
    - Clinical sign
    ontology_label: Ataxia
  obsolete_terms:
  - term_id: HP:0002459
    ontology_label: obsolete Dysautonomia
    replaced_by: HP:0012332
  - term_id: HP:0030050
    ontology_label: obsolete Narcolepsy
    replaced_by: HP:0002524
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: GO:0010216
    ontology_label: obsolete negative regulation of gene expression via chromosomal
      DNA cytosine methylation
    replaced_by: GO:0044027
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1E-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1E-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Sensory and Autonomic Neuropathy Type 1E
- **MONDO ID:** MONDO:0013584 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Sensory and Autonomic Neuropathy Type 1E** covering all of the
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

# Hereditary Sensory and Autonomic Neuropathy Type 1E (HSAN1E)
## Comprehensive Disease Characteristics Report

**Disease:** Hereditary Sensory and Autonomic Neuropathy Type 1E
**MONDO ID:** MONDO:0013584 · **OMIM:** #614116 · **Orphanet:** 456318 · **Category:** Mendelian (autosomal dominant)
**Causal gene:** *DNMT1* (DNA methyltransferase 1), 19p13.2

---

## Summary

Hereditary Sensory and Autonomic Neuropathy Type 1E (HSAN1E) is a rare, autosomal-dominant, adult-onset neurodegenerative disorder affecting **both the central and peripheral nervous systems**. It is caused by heterozygous mutations clustered in the **targeting-sequence (TS) / replication focus targeting sequence (RFTS) domain of *DNMT1*** (encoded by exons 20–21). Patients are clinically normal until young adulthood and then develop a characteristic clinical triad: a **sensory-predominant peripheral (and autonomic) neuropathy**, **sensorineural hearing loss**, and **progressive dementia**. Narcolepsy with or without cataplexy, autonomic dysfunction, psychiatric/personality change, and seizures are additional features. HSAN1E lies at one pole of a *DNMT1* disease spectrum whose other pole is autosomal-dominant cerebellar ataxia, deafness and narcolepsy (ADCA-DN, OMIM 604121); the two are allelic and can overlap.

Mechanistically, disease mutations destabilize the RFTS domain of DNMT1. In the wild-type enzyme this domain autoinhibits the catalytic methyltransferase domain and directs the protein to replication foci/heterochromatin via interaction with UHRF1. Mutant DNMT1 undergoes **premature degradation**, has **reduced methyltransferase activity**, and **loses heterochromatin binding during G2**, producing a signature methylome of **global hypomethylation with focal site-specific hypermethylation**. Whole-genome bisulfite sequencing of patient DNA confirmed genome-wide methylation loss (X chromosome and chromosome 18 most affected) alongside hundreds of thousands of differentially methylated CpG sites. In cellular models, cells expressing mutant DNMT1 are prone to apoptosis and fail to differentiate into the neuronal lineage — connecting the epigenetic lesion to neurodegeneration.

There is currently **no disease-modifying therapy**; management is supportive and multidisciplinary (wound/foot care, treatment of osteomyelitis and Charcot joints, hearing aids/cochlear implants, wake-promoting agents and sodium oxybate for narcolepsy, and management of psychiatric symptoms and seizures). Natural-history data from a nine-kinship cohort report a **mean age of onset ≈38 years and mean survival ≈54 years**. Because the underlying lesion is epigenetic and therefore in principle reversible, the DNMT1/methylome defect is regarded as a rational future therapeutic target.

---

## Section 1 — Disease Information

HSAN1E is a hereditary sensory and autonomic neuropathy distinguished from other HSAN subtypes by the co-occurrence of **central** features (dementia, hearing loss, sometimes narcolepsy) with the **peripheral** sensory/autonomic neuropathy. The MONDO ontology (MONDO:0013584) labels it *"hereditary sensory neuropathy-deafness-dementia syndrome"* and defines it as *"A hereditary sensory neuropathy characterized by adult onset of progressive peripheral sensory loss, progressive hearing impairment, and early-onset dementia that has material basis in heterozygous mutation in the DNMT1 gene on chromosome 19p13"* (Finding F012).

**Key identifiers (verified via EBI OLS4 / MONDO):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013584 |
| OMIM | 614116 |
| Orphanet | 456318 |
| MeSH | C580162 |
| Disease Ontology (DOID) | DOID:0070158 |
| UMLS | C3279885 |
| MedGen | 481515 |
| GARD | 0011927 |
| NORD | 1903 |

**Synonyms / alternative names (verified):** HSAN1E, HSN1E, HSNIE; "Neuropathy, hereditary sensory, type IE"; "DNMT1-related dementia, deafness, and sensory neuropathy"; "hereditary sensory neuropathy with hearing loss and dementia."

**Source of information:** Aggregated disease-level resources (OMIM, Orphanet, MONDO) supplemented by primary case-series/kindred reports from the peer-reviewed literature. Individual-patient (EHR) datasets were not used; findings derive from published kindreds and functional studies.

---

## Section 2 — Etiology

**Primary cause (genetic).** HSAN1E is a monogenic Mendelian disorder caused by **heterozygous, autosomal-dominant mutations in *DNMT1***, specifically within the targeting-sequence/RFTS domain (exons 20–21). Exome sequencing first identified *DNMT1* c.1484A>G (p.Tyr495Cys) in two American and one Japanese kindred and c.1470-1472TCC>ATA (p.Asp490Glu-Pro491Tyr) in a European kindred, all within the TS domain (Klein et al. 2011, [PMID: 21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/); Finding F001). *"Here we show that mutations in DNMT1 cause both central and peripheral neurodegeneration in one form of hereditary sensory and autonomic neuropathy with dementia and hearing loss"* and *"All mutations are within the targeting-sequence domain of DNMT1."*

**Genetic risk factors.** The disease-causing variants are themselves the risk factor; no additional susceptibility loci are established. Because inheritance is autosomal dominant with a single pathogenic allele sufficient for disease, first-degree relatives carry a 50% transmission risk. **De novo** mutations occur (e.g., p.T481P and p.P491L arose de novo in a natural-history cohort; Baets et al. 2015, [PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/); Finding F005), so a negative family history does not exclude the diagnosis.

**Environmental risk factors / protective factors / gene–environment interactions.** No environmental, lifestyle, infectious, or dietary risk or protective factors are established for HSAN1E, and no gene–environment interactions have been demonstrated. This is expected for a fully penetrant monogenic disorder. (Not applicable / no data.)

---

## Section 3 — Phenotypes

The phenotype is an adult-onset (mean ≈38 y) multisystem neurodegeneration. Core and additional features with suggested HPO terms and qualifiers are tabulated below (Findings F003, F010).

| Phenotype | Type | HPO term | Onset / severity / progression | Frequency |
|---|---|---|---|---|
| Loss of pain sensation | Clinical sign | HP:0007328 | Adult-onset; progressive | Core |
| Impaired temperature sensation | Clinical sign | HP:0010829 | Adult-onset; progressive | Core |
| Impaired vibratory sensation | Clinical sign | HP:0002495 | Adult-onset; progressive | Core |
| Sensory neuropathy | Clinical sign | HP:0000763 | Adult-onset; progressive | Core |
| Peripheral axonal neuropathy | Clinical sign | HP:0003477 | Adult-onset; progressive | Core |
| Skin ulcer (neuropathic) | Physical manifestation | HP:0200042 | Secondary complication | Common |
| Osteomyelitis (chronic) | Physical manifestation | HP:0002754 | Secondary complication | Common |
| Charcot arthropathy | Physical manifestation | HP:0002828 | Secondary complication | Common |
| Sensorineural hearing loss | Clinical sign | HP:0000407 | Adult-onset; progressive | Core |
| Dementia / cognitive decline | Clinical sign | HP:0000726 | Adult-onset; progressive | Core |
| Frontal lobe dementia (executive) | Clinical sign | HP:0002145 | Early feature; progressive | Common |
| Personality change | Behavioral | HP:0000751 | Variable | Subset |
| Seizure | Clinical sign | HP:0001250 | Variable | Subset |
| Autonomic dysregulation | Clinical sign | HP:0002459 | Adult-onset | Common |
| Narcolepsy | Clinical sign | HP:0030050 | Variable | Subset (shared with ADCA-DN) |
| Cataplexy | Clinical sign | HP:0002524 | Variable | Subset |
| Cerebral atrophy | Imaging | HP:0002059 | Progressive | Common |
| Cerebellar atrophy | Imaging | HP:0001272 | Progressive | Common |
| Cerebellar ataxia | Clinical sign | HP:0001251 | Characteristic of ADCA-DN pole | Spectrum-dependent |

Enumerating the core, Yuan et al. describe *"loss of pain and vibration sense, chronic osteomyelitis, autonomic system dysfunctions, hearing loss, and mild dementia"* ([PMID: 23521649](https://pubmed.ncbi.nlm.nih.gov/23521649/)). Psychiatric burden is notable: *"The symptoms of these patients include prominent personality, psychiatric manifestations, and seizures in one"* (Klein et al. 2013, [PMID: 23365052](https://pubmed.ncbi.nlm.nih.gov/23365052/)). Narcolepsy is shared across the spectrum — *"narcolepsy with or without cataplexy with low/intermediate or normal cerebrospinal fluid hypocretin-1 is present in both diseases"* ([PMID: 24727570](https://pubmed.ncbi.nlm.nih.gov/24727570/)).

**Quality-of-life impact.** Disease combines chronic neuropathic complications requiring wound/limb care (risk of amputation from ulcers/osteomyelitis/Charcot joints), sensory disability, progressive deafness impairing communication, and progressive dementia with loss of independence — a severe, cumulative disability trajectory. Disease-specific QoL instrument data (EQ-5D/SF-36) were not identified in the literature.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *DNMT1* (DNA (cytosine-5)-methyltransferase 1), HGNC:2976, located at **19p13.2**; disease OMIM #614116. DNMT1 is the maintenance methyltransferase that copies CpG methylation onto the newly synthesized DNA strand during replication.

**Pathogenic variants.** All reported HSAN1E variants localize to the TS/RFTS domain encoded by exons 20–21, described as a *"mutation hot spot"*: *"all reported mutations of DNMT1 are concentrated in exons 20 and 21, which encode the replication focus targeting sequence (RFTS) domain of Dnmt1"* ([PMID: 23521649](https://pubmed.ncbi.nlm.nih.gov/23521649/); Finding F001).

| Variant (protein) | cDNA / note | Source (PMID) |
|---|---|---|
| p.Tyr495Cys | c.1484A>G — recurrent hot spot | 21532572 |
| p.Asp490Glu–Pro491Tyr | c.1470-1472TCC>ATA (in-cis di-substitution) | 21532572 |
| p.Tyr495His | — | 23365052 |
| p.His569Arg | exon 21 | 23521649 |
| p.Pro496Tyr | functionally characterized | 28334952 |
| p.Tyr500Cys | functionally characterized | 28334952 |
| p.Cys353Phe, p.Thr481Pro, p.Pro491Leu, p.Tyr524Asp, p.Ile531Asn | 5 novel TS-domain variants; T481P & P491L de novo | 25678562 |

**Variant classification & type.** Reported variants are pathogenic missense (and in-cis multi-nucleotide) substitutions consistent with ACMG criteria (segregation with disease, functional impact, absence from controls, de novo occurrence). No truncating/frameshift or structural variants are characteristic — the mechanism is a conformational/stability defect of a specific domain rather than gene deletion.

**Allele frequency / origin.** These are rare, essentially private familial variants; they are **germline** in origin (with documented de novo events). No somatic association exists. Population-database (gnomAD) frequencies are effectively absent, consistent with a severe dominant disorder.

**Functional consequence.** The variants act by **protein destabilization / partial loss of maintenance-methylation function with a dominant, misfolding/degradation-driven effect** (Finding F002), rather than simple haploinsufficiency — the mutant allele produces an unstable protein and perturbs the methylome.

**Genotype–phenotype gradient (intra-domain).** A key insight is spatial ordering within the TS domain: *"all the mutations causal for HSAN1E are located in the middle part or N-terminus end of the TS domain, whereas all the mutations causal for autosomal dominant cerebellar ataxia, deafness and narcolepsy are located in the C-terminus end of the TS domain"* (Baets et al. 2015, [PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/); Finding F005).

**Modifier genes / epigenetic modifiers / chromosomal abnormalities.** No established modifier genes. The disease itself is fundamentally epigenetic (see Section 6). No chromosomal/structural abnormalities are implicated.

---

## Section 5 — Environmental Information

No environmental factors, toxins, occupational exposures, lifestyle factors, or infectious agents are implicated in the causation of HSAN1E. It is a purely genetic (Mendelian, monogenic) disorder. **Not applicable / no data.** (Note: infections such as osteomyelitis and *S. aureus* wound infections are downstream *complications* of sensory loss, not etiologic agents — the parallel to neuropathic infection biology is illustrated by studies of other insensate neuropathies such as CIPA, [PMID: 39455857](https://pubmed.ncbi.nlm.nih.gov/39455857/).)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous missense mutation in the TS/RFTS domain of *DNMT1*** (exons 20–21) *leads to* a conformationally destabilized DNMT1 protein.
2. Destabilization *results in* **premature degradation of the mutant protein** and **reduced methyltransferase activity** (demonstrated).
3. The mutation *impairs* the RFTS domain's normal functions — **binding to UHRF1** and **association with heterochromatin/replication foci** — with defective binding especially during the **late-S/G2 phase** of the cell cycle (demonstrated).
4. Loss of proper targeting during replication *leads to* a **signature methylome: global hypomethylation with focal site-specific hypermethylation** (demonstrated by whole-genome bisulfite sequencing of patient DNA).
5. The aberrant methylome *results in* **dysregulated gene expression and genomic instability** in affected cells (inferred from methylome data).
6. In neural precursors this *leads to* a **propensity to apoptosis and a failure to differentiate into the neuronal lineage** (demonstrated in mESC complementation/rescue assays).
7. The cumulative cellular loss *results in* **progressive degeneration of dorsal-root-ganglion sensory neurons, cochlear/auditory pathways, cerebral and cerebellar cortex, and the hypothalamic hypocretin (orexin) system** (inferred from the anatomic distribution of clinical deficits).
8. This anatomic degeneration *manifests clinically* as **sensory/autonomic neuropathy, sensorineural hearing loss, progressive dementia, and narcolepsy**.

Branch point: the **position of the mutation within the TS domain** biases the phenotype — N-terminal/middle TS mutations toward the **HSAN1E** pole (peripheral neuropathy prominent), C-terminal TS mutations toward the **ADCA-DN** pole (cerebellar ataxia/narcolepsy prominent).

### Detail by category

**Molecular pathway — DNA-methylation maintenance.** DNMT1 is the maintenance DNA methyltransferase. Its N-terminal regulatory region contains the **RFTS domain, a CXXC zinc finger, and paired BAH domains**; the crystal structure (residues 351–1600 with S-adenosyl-L-homocysteine, 2.62 Å) shows that *"The RFTS domain directly associates with the methyltransferase domain, thereby inhibiting the substrate binding of hDNMT1"* (Zhang et al. 2015, [PMID: 26070743](https://pubmed.ncbi.nlm.nih.gov/26070743/); Finding F004). The authors note the structure *"provides a framework for understanding the functional consequence of disease-related hDNMT1 mutations."* Disease mutations sit in this autoinhibitory/targeting module.

**Protein dysfunction.** Klein et al. showed the core lesion: *"These mutations cause premature degradation of mutant proteins, reduced methyltransferase activity and impaired heterochromatin binding during the G2 cell cycle phase leading to global hypomethylation and site-specific hypermethylation"* ([PMID: 21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/); Finding F002). Smets et al. added that the HSAN1E variants P496Y and Y500C *"not only impair DNMT1 heterochromatin association, but also UHRF1 interaction resulting in hypomethylation,"* and decrease protein stability in late S/G2 ([PMID: 28334952](https://pubmed.ncbi.nlm.nih.gov/28334952/); Finding F009).

**Epigenetic change (the defining lesion).** Whole-genome bisulfite sequencing of three affected/sibling pairs demonstrated the "signature methylome": *"overall methylation loss was consistently found in all chromosomes with X and 18 being most affected"* — with **564,218 differentially methylated CpG sites, 300,134 of them hypermethylated** (Sun et al. 2014, [PMID: 25033457](https://pubmed.ncbi.nlm.nih.gov/25033457/); Finding F008). The disorder is thus *"directly caused by methylomic changes"* ([PMID: 23098078](https://pubmed.ncbi.nlm.nih.gov/23098078/)).

**Cellular process — apoptosis & failed neurogenesis.** In mESC DNMT1-rescue assays, *"cells expressing mutated DNMT1 were prone to apoptosis and failed to differentiate into neuronal lineage"* ([PMID: 28334952](https://pubmed.ncbi.nlm.nih.gov/28334952/)). This links the methylation defect directly to neuronal loss and impaired neurogenesis.

**Cross-disease supporting paradigm.** DNMT/5-methylcytosine dysregulation drives neuronal apoptosis in other neurodegenerations too: in ALS, *"motor neurons in human ALS show significant abnormalities in Dnmt1, Dnmt3a, and 5-methylcytosine,"* and *"During apoptosis of cultured motor neuron-like cells, Dnmt1 and Dnmt3a protein levels increase, and 5-methylcytosine accumulates"* (Martin & Wong 2013, [PMID: 23900692](https://pubmed.ncbi.nlm.nih.gov/23900692/); Finding F011). This is *supporting* context, not direct HSAN1E data.

**Suggested ontology terms.** GO biological process: DNA methylation (GO:0006306), maintenance of DNA methylation (GO:0010216), regulation of gene expression by genetic imprinting (GO:0006346), neuron apoptotic process (GO:0051402), neuron differentiation (GO:0030182). GO cellular component: heterochromatin (GO:0000792), replication fork / nuclear replication focus (GO:0043596), nucleus (GO:0005634). CL cell types: sensory neuron (CL:0000101), neuron (CL:0000540), cochlear hair cell (CL:0000855).

### Mechanism schematic

```
DNMT1 TS/RFTS missense mutation (exons 20-21)
        │ destabilizes domain
        ▼
Premature protein degradation + reduced MTase activity
        │ loses UHRF1 binding / heterochromatin targeting (late S/G2)
        ▼
Aberrant "signature" methylome
  (global hypomethylation + focal hypermethylation; X & chr18 worst)
        │ dysregulated gene expression
        ▼
Neural precursors: apoptosis + failed neuronal differentiation
        ▼
Degeneration of:  DRG sensory neurons ─► sensory/autonomic neuropathy
                  cochlea/auditory ────► sensorineural hearing loss
                  cerebral+cerebellar ─► dementia (+ ataxia at ADCA-DN pole)
                  hypothalamic hypocretin ─► narcolepsy
```

---

## Section 7 — Anatomical Structures Affected

HSAN1E is a **combined central and peripheral neurodegeneration** — *"mutations in DNMT1 cause both central and peripheral neurodegeneration"* ([PMID: 21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/); Finding F008).

**Peripheral (organ/tissue/cell):** Dorsal root ganglia and their **sensory neurons** (UBERON:0000044 dorsal root ganglion; CL:0000101 sensory neuron) with sensory-predominant axonal loss (absent sensory nerve action potentials, abnormal sural-nerve biopsy) and involvement of **autonomic fibers**; motor conduction is relatively spared ([PMID: 23521649](https://pubmed.ncbi.nlm.nih.gov/23521649/); [PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)).

**Central:** Diffuse **cerebral and cerebellar cortex** (UBERON:0000956 cerebral cortex; UBERON:0002037 cerebellum) with atrophy and frontal-lobe hypometabolism; the **cochlea / auditory pathway** (sensorineural hearing loss); and the **hypothalamic hypocretin (orexin) system** (UBERON:0001898 hypothalamus), underlying narcolepsy with reduced CSF hypocretin-1 ([PMID: 24727570](https://pubmed.ncbi.nlm.nih.gov/24727570/); [PMID: 23365052](https://pubmed.ncbi.nlm.nih.gov/23365052/)).

**Body systems:** central nervous, peripheral nervous, and autonomic nervous systems; sensory (auditory) system. **Subcellular:** nucleus, heterochromatin, and DNA replication foci (GO cellular-component terms above). **Lateralization:** bilateral / symmetric, as expected for a length-dependent/genetic neurodegeneration.

---

## Section 8 — Temporal Development

**Onset.** Patients are *"clinically normal until young adulthood, then begin developing the characteristic symptoms involving central and peripheral nervous systems"* ([PMID: 25033457](https://pubmed.ncbi.nlm.nih.gov/25033457/); Finding F003). Onset is typically in the **20s–40s**, with a cohort **mean of 37.7 years** ([PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/); Finding F005). Pattern is **insidious and chronic**.

**Progression.** The course is **progressive and neurodegenerative**, evolving from isolated executive dysfunction to global dementia in parallel with worsening neuropathy, deafness, and (in some) narcolepsy. In ADCA-DN kindreds cognition declines *"in parallel with neurological deterioration"* ([PMID: 27869457](https://pubmed.ncbi.nlm.nih.gov/27869457/)). Disease is **chronic lifelong**; there are **no remissions**.

**Duration / survival.** Mean survival in the nine-kinship cohort was **53.6 years (SD 7.7; range 43–75)** — *"The average survival of HSAN1E was 53.6 years"* ([PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)). Given a ~38-year mean onset, typical symptomatic duration is on the order of **~15 years**.

---

## Section 9 — Inheritance and Population

**Inheritance.** **Autosomal dominant**, heterozygous. **De novo** mutations occur (p.T481P, p.P491L; [PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)), so sporadic presentations are possible. Penetrance appears high/complete in reported kindreds; expressivity is **variable** (age of onset and feature mix differ within and between families, and along the HSAN1E↔ADCA-DN spectrum).

**Epidemiology.** HSAN1E is **ultra-rare**, described in a limited number of kindreds worldwide (American, Japanese, European, Brazilian). Precise prevalence/incidence figures are not established (Orphanet lists it among rare diseases without a firm prevalence estimate). No founder effect, defined consanguinity role, or population enrichment is established — variants are largely private/familial. **Sex ratio:** no sex predilection reported (autosomal). **Geographic distribution:** worldwide, no endemic region.

**Genetic counseling implications.** 50% transmission risk to offspring of an affected heterozygote; de novo cases mean absence of family history does not exclude the diagnosis; predictive/cascade testing and reproductive options (PGT, prenatal testing) are feasible once the familial variant is known.

---

## Section 10 — Diagnostics

**Molecular diagnosis (definitive).** Sequencing of ***DNMT1* exons 20–21 (TS/RFTS domain)**; identifying a pathogenic TS-domain variant is confirmatory ([PMID: 21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/); [PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/); Finding F006). Single-gene testing, targeted hereditary-neuropathy/dementia gene panels including *DNMT1*, or exome/genome sequencing are all appropriate routes.

**Supporting multimodal workup** (as used in reported cohorts):

| Modality | Typical finding |
|---|---|
| Nerve conduction / EMG | Absent sensory nerve action potentials; near-normal motor conduction |
| Sural nerve / skin / muscle biopsy | Sensory axonal loss |
| Brain MRI | Diffuse cerebral and cerebellar atrophy |
| FDG-PET | Frontal-lobe hypometabolism ([PMID: 23365052](https://pubmed.ncbi.nlm.nih.gov/23365052/)) |
| EEG | May show abnormalities; seizures in some |
| Audiometry | Sensorineural hearing loss |
| Polysomnography / MSLT | Narcolepsy pattern |
| CSF | Low/intermediate hypocretin-1; total tau, phospho-tau, amyloid-β1-42, 14-3-3 measured ([PMID: 24727570](https://pubmed.ncbi.nlm.nih.gov/24727570/)) |
| Optical coherence tomography, lymphoscintigraphy | Adjunct assessments |

*"Frontal lobe hypometabolism has been documented in an HSAN1E family"* ([PMID: 23365052](https://pubmed.ncbi.nlm.nih.gov/23365052/)).

**Omics/epigenomic diagnostics (research).** Whole-genome bisulfite sequencing reveals the disease-specific "signature methylome," a potential future molecular biomarker ([PMID: 25033457](https://pubmed.ncbi.nlm.nih.gov/25033457/)).

**Diagnostic pitfalls.** *"Diagnosing the syndrome can be difficult, as all clinical features may not be present at onset, HLA-DQB1*06:02 is often negative, and sporadic cases occur"* (Pedroso et al. 2013, [PMID: 23904686](https://pubmed.ncbi.nlm.nih.gov/23904686/); Finding F006). Unlike idiopathic/autoimmune narcolepsy, the HLA-DQB1*06:02 allele is frequently absent in DNMT1-related narcolepsy.

**Differential diagnosis.** Other HSAN subtypes (e.g., HSAN1 due to *SPTLC1*), CMT with sensory features, diabetic/amyloid/paraneoplastic sensory neuropathies, other insensate neuropathies such as CIPA (*NTRK1*), and neurodegenerative dementias with hearing loss. The combination of adult-onset sensory neuropathy + deafness + dementia (± narcolepsy) with a *DNMT1* TS-domain variant is distinctive.

---

## Section 11 — Outcome / Prognosis

**Survival/mortality.** Progressive and ultimately life-limiting; **mean survival ≈53.6 years** in the reported cohort ([PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)). No formal 5-/10-year survival statistics exist for this ultra-rare disease.

**Morbidity.** High and cumulative: neuropathic ulcers, chronic osteomyelitis, Charcot arthropathy (amputation risk), progressive deafness, and dementia leading to loss of independence; autonomic dysfunction and narcolepsy add further disability. Recovery potential is essentially nil — the process is neurodegenerative with no disease-modifying therapy.

**Prognostic factors.** Position of the mutation within the TS domain influences the phenotypic pole (HSAN1E vs ADCA-DN) and thus the dominant morbidity ([PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)). No validated molecular prognostic biomarkers are established beyond genotype.

---

## Section 12 — Treatment

**There is no approved disease-modifying therapy.** Management is **symptomatic and multidisciplinary** (Finding F007):

- **Neuropathic/foot care:** protective footwear, wound care, aggressive treatment of ulcers, osteomyelitis, and Charcot joints to prevent amputation.
- **Hearing:** hearing aids or cochlear implants for sensorineural hearing loss (NCIT: cochlear implantation).
- **Narcolepsy/cataplexy:** wake-promoting agents (e.g., **modafinil**, stimulants) and **sodium oxybate** ([PMID: 24727570](https://pubmed.ncbi.nlm.nih.gov/24727570/)).
- **Neuropsychiatric:** management of psychiatric/behavioral symptoms and seizures ([PMID: 23365052](https://pubmed.ncbi.nlm.nih.gov/23365052/)).
- **Rehabilitative/supportive:** physical and occupational therapy; autonomic symptom management; neuropathic pain control as needed.

**Rational future target.** Because the defect is epigenetic, it is in principle reversible: *"Epigenetic modifications, however, are reversible and are therefore a prime target for therapeutic intervention,"* and *"Some diseases, such as a hereditary form of sensory neuropathy accompanied by dementia, are directly caused by methylomic changes"* (Johnson et al. 2012, [PMID: 23098078](https://pubmed.ncbi.nlm.nih.gov/23098078/); Finding F007). This frames methylome-modulating or DNMT1-stabilizing/allele-specific strategies as logical (currently experimental) directions. No HSAN1E-specific clinical trials (NCT identifiers) were identified.

---

## Section 13 — Prevention

No primary prevention exists for this genetic disorder. Preventive activity is therefore **genetic and tertiary**:

- **Genetic counseling** for at-risk families (50% offspring risk; predictive/cascade testing once the familial variant is known).
- **Reproductive options:** preimplantation genetic testing (PGT) and prenatal diagnosis where desired.
- **Tertiary prevention (complication avoidance):** meticulous foot/skin surveillance and podiatric care to prevent ulcers/osteomyelitis/amputation; fall-risk and sleep-safety management for narcolepsy; hearing rehabilitation; seizure and psychiatric management.

No immunization, behavioral, environmental, or public-health prevention applies. **Not applicable** for population screening beyond family-based cascade testing.

---

## Section 14 — Other Species / Natural Disease

*DNMT1* is deeply conserved across vertebrates, and orthologs exist in mouse (*Dnmt1*), rat, zebrafish, and other model species (Section 15). However, **no naturally occurring HSAN1E-equivalent disease has been reported in companion animals or wildlife** (no OMIA entry corresponding to the human TS-domain DNMT1 neuropathy was identified). There is no zoonotic or cross-species transmission dimension (the disease is genetic). Comparative relevance is chiefly through **engineered/experimental models** rather than natural disease. **Largely not applicable / no data** for natural animal disease.

---

## Section 15 — Model Organisms

Functional modeling of HSAN1E has relied primarily on **cell-based systems** rather than dedicated whole-animal models (Finding F009):

- **Mouse embryonic stem cell (mESC) DNMT1 complementation / rescue assays** are the principal model. *"With functional complementation assays in mouse embryonic stem cells, we showed that DNMT1 mutations P496Y and Y500C identified in HSANIE patients not only impair DNMT1 heterochromatin association, but also UHRF1 interaction resulting in hypomethylation"* and, in rescue assays, *"cells expressing mutated DNMT1 were prone to apoptosis and failed to differentiate into neuronal lineage"* (Smets et al. 2017, [PMID: 28334952](https://pubmed.ncbi.nlm.nih.gov/28334952/)).
- **Patient-derived material:** germline DNA for whole-genome bisulfite sequencing ([PMID: 25033457](https://pubmed.ncbi.nlm.nih.gov/25033457/)); cellular localization/binding-efficiency experiments at replication foci and heterochromatin ([PMID: 21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/); [PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)).

**Recapitulation & limitations.** The cellular models faithfully reproduce the **molecular hallmarks** (protein instability, lost UHRF1/heterochromatin binding, hypomethylation, apoptosis, failed neuronal differentiation) but do **not reproduce the whole-organism, adult-onset, multi-system neurodegenerative phenotype** (sensory neuropathy, deafness, dementia, narcolepsy). A validated knock-in animal model carrying a TS-domain mutation and recapitulating the clinical syndrome was not identified — a clear resource gap. **Model resources:** MGI (mouse *Dnmt1*), plus patient-derived iPSC/mESC approaches.

---

## Mechanistic Model / Interpretation

The evidence assembles into a single coherent, largely demonstrated causal narrative. A **specific structural lesion** — a missense change in the autoinhibitory/targeting RFTS domain of DNMT1 — is the root cause (Sections 4, 6; [PMID: 21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/), [PMID: 26070743](https://pubmed.ncbi.nlm.nih.gov/26070743/)). Because this domain both **autoinhibits the catalytic domain** and **targets DNMT1 to replication foci via UHRF1/heterochromatin**, its destabilization produces two coupled failures: the protein is **degraded prematurely**, and what remains is **mistargeted during late S/G2**. The result is not random but a **reproducible "signature methylome"** — genome-wide hypomethylation with focal hypermethylation ([PMID: 25033457](https://pubmed.ncbi.nlm.nih.gov/25033457/)). Downstream, this epigenetic derangement makes cells — critically, neural precursors — **apoptosis-prone and unable to complete neuronal differentiation** ([PMID: 28334952](https://pubmed.ncbi.nlm.nih.gov/28334952/)), which is the most direct available bridge from "methylation defect" to "neurodegeneration." The specific anatomical targets (DRG sensory neurons, cochlea, cerebral/cerebellar cortex, hypothalamic hypocretin neurons) explain the clinical triad plus narcolepsy.

The **intra-domain genotype–phenotype gradient** is the most elegant structural insight: N-terminal/middle TS mutations → HSAN1E; C-terminal TS mutations → ADCA-DN ([PMID: 25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/)). HSAN1E and ADCA-DN are therefore *"two discrete clinical entities belonging to the same disease spectrum, with variable degree of overlap"* ([PMID: 24727570](https://pubmed.ncbi.nlm.nih.gov/24727570/)) — one gene, one domain, a continuum of phenotypes set by mutation position.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [21532572](https://pubmed.ncbi.nlm.nih.gov/21532572/) | Mutations in DNMT1 cause hereditary sensory neuropathy with dementia and hearing loss | Landmark: identifies DNMT1 TS-domain as causal; defines core molecular mechanism |
| [26070743](https://pubmed.ncbi.nlm.nih.gov/26070743/) | Crystal Structure of Human DNA Methyltransferase 1 | Structural basis: RFTS autoinhibition; framework for mutation interpretation |
| [25033457](https://pubmed.ncbi.nlm.nih.gov/25033457/) | Aberrant signature methylome by DNMT1 hot spot mutation in HSAN1E | Genome-wide methylome in patients: global hypomethylation + focal hypermethylation |
| [28334952](https://pubmed.ncbi.nlm.nih.gov/28334952/) | DNMT1 mutations affect UHRF1 interaction and neuronal differentiation | Cellular mechanism: UHRF1/heterochromatin loss → apoptosis + failed neurogenesis |
| [25678562](https://pubmed.ncbi.nlm.nih.gov/25678562/) | Defects of mutant DNMT1 linked to a spectrum of neurological disorders | Natural history (onset ~38 y, survival ~54 y); intra-TS genotype–phenotype gradient; de novo variants |
| [23521649](https://pubmed.ncbi.nlm.nih.gov/23521649/) | Novel RFTS-domain DNMT1 mutation causes HSAN1E | Exon 20–21 hot spot; core phenotype enumeration |
| [23365052](https://pubmed.ncbi.nlm.nih.gov/23365052/) | DNMT1 mutation hot spot causes varied phenotypes | Psychiatric/seizure features; FDG-PET frontal hypometabolism |
| [24727570](https://pubmed.ncbi.nlm.nih.gov/24727570/) | Narcolepsy is a common phenotype in HSAN IE and ADCA-DN | Narcolepsy/hypocretin; HLA-DQB1*06:02 negativity; disease spectrum |
| [23904686](https://pubmed.ncbi.nlm.nih.gov/23904686/) | Novel de novo exon 21 DNMT1 mutation (Brazilian patient) | Diagnostic pitfalls; sporadic/de novo cases |
| [27869457](https://pubmed.ncbi.nlm.nih.gov/27869457/) | Cognitive/behavioral deterioration in ADCA-DN | Cognitive trajectory parallels neurodegeneration (allelic condition) |
| [23098078](https://pubmed.ncbi.nlm.nih.gov/23098078/) | DNA methylation in aging and disease | Reversibility of methylomic defect → epigenetic therapy rationale |
| [23900692](https://pubmed.ncbi.nlm.nih.gov/23900692/) | Aberrant DNA methylation in ALS | Cross-disease support for DNMT/5mC → neuronal apoptosis paradigm |

---

## Limitations and Knowledge Gaps

- **Ultra-rare, small cohorts.** Findings derive from a limited number of kindreds; prevalence/incidence, precise penetrance, and formal survival curves are not firmly established.
- **No validated animal model.** Mechanistic evidence rests on cell-based (mESC/patient-cell) assays; a knock-in organism reproducing the adult-onset multisystem phenotype is lacking, limiting study of tissue-specific vulnerability and preclinical therapeutics.
- **Gap from methylome to neuron loss.** Which specific hyper-/hypomethylated loci and dysregulated genes actually drive DRG, cochlear, cortical, and hypocretin-neuron degeneration is not resolved; causality between individual DMRs and clinical features is inferred.
- **No disease-modifying therapy or trials.** The epigenetic-reversibility rationale is conceptual; no HSAN1E-specific therapeutic has been tested clinically.
- **QoL/prognostic biomarkers.** No disease-specific quality-of-life data or validated molecular prognostic markers (beyond mutation position) exist.
- **Cross-disease evidence flagged.** The ALS/DNMT paradigm ([PMID: 23900692](https://pubmed.ncbi.nlm.nih.gov/23900692/)) is supporting context, not direct HSAN1E data.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a TS-domain knock-in mouse** (e.g., *Dnmt1* p.Tyr495Cys equivalent) and characterize age-dependent DRG/cochlear/cortical/hypocretin-neuron degeneration to establish an in-vivo model and test recapitulation.
2. **Integrate patient methylome with transcriptome** (paired WGBS + RNA-seq in patient iPSC-derived sensory neurons and cortical/hypocretin neurons) to identify the DMR→gene→phenotype links driving each clinical domain.
3. **iPSC disease modeling with isogenic controls:** derive sensory neurons, cochlear-like and hypothalamic neurons from patient iPSCs (CRISPR-corrected isogenic pairs) to map cell-type-specific vulnerability and apoptosis.
4. **Therapeutic screening on the epigenetic axis:** test protein-stabilizing chaperones, UHRF1-interaction modulators, and demethylation/re-methylation balancing agents in the cellular models; explore allele-selective ASO/RNAi knockdown of the mutant allele.
5. **Natural-history registry & biomarker validation:** prospectively collect standardized neurophysiology, imaging, CSF (hypocretin-1, tau/pTau/Aβ42, 14-3-3), and methylome data across kindreds to define progression rates, QoL, and candidate prognostic biomarkers.
6. **Structure-guided variant interpretation:** use the DNMT1 crystal structure ([PMID: 26070743](https://pubmed.ncbi.nlm.nih.gov/26070743/)) plus deep mutational scanning of the TS domain to build a predictive HSAN1E↔ADCA-DN genotype–phenotype map for clinical variant classification.

---

*Report compiled from 12 confirmed findings across 15 reviewed papers. Evidence source types: human clinical (kindred case series, natural history), in vitro/cellular (mESC complementation, WGBS), computational/structural (crystal structure), and cross-disease supporting literature (ALS).*


## Artifacts

- [OpenScientist final report](Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1E-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1E-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 4 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 21 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013584` (3 mentions) - the report calls it "MONDO"; MONDO calls it **hereditary sensory neuropathy-deafness-dementia syndrome**
- `DOID:0070158` (1 mention) - the report calls it "Disease Ontology (DOID)"; DOID calls it **hereditary sensory neuropathy type 1E**
- `HP:0007328` (1 mention) - the report calls it "Clinical sign"; HP calls it **Impaired pain sensation**
- `HP:0010829` (1 mention) - the report calls it "Clinical sign"; HP calls it **Impaired temperature sensation**
- `HP:0002495` (1 mention) - the report calls it "Clinical sign"; HP calls it **Impaired vibratory sensation**
- `HP:0000763` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensory neuropathy**
- `HP:0003477` (1 mention) - the report calls it "Clinical sign"; HP calls it **Peripheral axonal neuropathy**
- `HP:0200042` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Skin ulcer**
- `HP:0002754` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Osteomyelitis**
- `HP:0002828` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Multiple joint contractures**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0000726` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dementia**
- `HP:0002145` (1 mention) - the report calls it "Clinical sign"; HP calls it **Frontotemporal dementia**
- `HP:0000751` (1 mention) - the report calls it "Behavioral"; HP calls it **Personality changes**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0002459` (1 mention) - the report calls it "Clinical sign"; HP calls it **obsolete Dysautonomia**
- `HP:0030050` (1 mention) - the report calls it "Clinical sign"; HP calls it **obsolete Narcolepsy**
- `HP:0002524` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cataplexy**
- `HP:0002059` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebral atrophy**
- `HP:0001272` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebellar atrophy**
- `HP:0001251` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ataxia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002459` (obsolete Dysautonomia) (1 mention) - replaced by `HP:0012332`
- `HP:0030050` (obsolete Narcolepsy) (1 mention) - replaced by `HP:0002524`
- `GO:0006306` (obsolete DNA methylation) (1 mention)
- `GO:0010216` (obsolete negative regulation of gene expression via chromosomal DNA cytosine methylation) (1 mention) - replaced by `GO:0044027`