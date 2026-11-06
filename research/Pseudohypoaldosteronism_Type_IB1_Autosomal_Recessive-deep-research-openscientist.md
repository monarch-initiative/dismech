---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-03T04:33:21.114757'
end_time: '2026-11-03T04:49:41.082482'
duration_seconds: 979.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pseudohypoaldosteronism Type IB1 Autosomal Recessive
  mondo_id: MONDO:0009917
  category: Mendelian
  causal_genes: SCNN1A
  omim_id: OMIM:264350
  synonyms: autosomal recessive PHA 1; PHA1B; autosomal recessive pseudohypoaldosteronism
    type 1; generalised PHA1; generalised pseudohypoaldosteronism type 1; generalized
    PHA1; generalized pseudohypoaldosteronism type 1
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
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 18
  validator_version: 0.4.0
term_validation:
  total_terms: 44
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 2
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0002902
    reported_labels:
    - ~Universal
    ontology_label: Hyponatremia
  - term_id: HP:0002153
    reported_labels:
    - ~Universal
    ontology_label: Hyperkalemia
  - term_id: HP:0001942
    reported_labels:
    - ~Universal
    ontology_label: Metabolic acidosis
  - term_id: HP:0000859
    reported_labels:
    - ~Universal
    ontology_label: Increased circulating aldosterone concentration
  - term_id: HP:0001508
    reported_labels:
    - Common
    ontology_label: Failure to thrive
  - term_id: HP:0001944
    reported_labels:
    - Common
    ontology_label: Dehydration
  - term_id: HP:0002013
    reported_labels:
    - Common
    ontology_label: Vomiting
  - term_id: HP:0012236
    reported_labels:
    - Characteristic of systemic form
    ontology_label: Elevated sweat chloride
  - term_id: HP:0011675
    reported_labels:
    - Minority but life-threatening
    ontology_label: Arrhythmia
  - term_id: HP:0012759
    reported_labels:
    - ~16% in one cohort
    ontology_label: Neurodevelopmental abnormality
  labels_variant: 1
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
  path: Pseudohypoaldosteronism_Type_IB1_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pseudohypoaldosteronism_Type_IB1_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudohypoaldosteronism Type IB1 Autosomal Recessive
- **MONDO ID:** MONDO:0009917 (if available)
- **Causal gene(s):** SCNN1A
- **OMIM:** OMIM:264350
- **Synonyms:** autosomal recessive PHA 1; PHA1B; autosomal recessive pseudohypoaldosteronism type 1; generalised PHA1; generalised pseudohypoaldosteronism type 1; generalized PHA1; generalized pseudohypoaldosteronism type 1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pseudohypoaldosteronism Type IB1 Autosomal Recessive** covering all of the
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

# Autosomal Recessive Pseudohypoaldosteronism Type IB1 (PHA1B1, SCNN1A): Comprehensive Disease Characterization

**Disease:** Pseudohypoaldosteronism Type IB1, Autosomal Recessive (PHA1B1)
**Causal gene:** **SCNN1A** (encoding the α-subunit of the epithelial sodium channel, ENaC)
**Identifiers:** OMIM 264350 · MONDO:0009917 · Orphanet ORPHA:171876 (systemic PHA1) · ICD-10 E27.4 · MeSH D011546 (Pseudohypoaldosteronism)
**Category:** Mendelian, autosomal recessive

---

## Summary

Autosomal recessive **Pseudohypoaldosteronism type 1B1 (PHA1B1)** is a rare, neonatal-onset, **multisystem salt-wasting disorder** caused by biallelic loss-of-function mutations in **SCNN1A**, the gene on chromosome 12p13 that encodes the obligatory **α-subunit of the amiloride-sensitive epithelial sodium channel (ENaC)**. ENaC is a heterotrimeric (α:β:γ, 1:1:1) channel that serves as the terminal effector of aldosterone signaling in sodium-reabsorbing epithelia. When the α-subunit is lost, the channel cannot assemble or conduct Na⁺, so target tissues become **resistant to aldosterone** despite grossly elevated hormone levels. The systemic (generalized) form contrasts with the milder, kidney-restricted autosomal dominant form (PHA1A) caused by heterozygous *NR3C2* (mineralocorticoid receptor) mutations.

Clinically, affected neonates present within the **first two weeks of life** with life-threatening **hyponatremia, hyperkalemia, and metabolic acidosis**, accompanied by **markedly elevated plasma renin and aldosterone** that are unresponsive to mineralocorticoid therapy. Because ENaC operates not only in the distal nephron and colon but also in **sweat glands, salivary glands, and the airway epithelium**, PHA1B1 produces extrarenal features that distinguish it from renal PHA1: **elevated sweat and saliva electrolytes** (overlapping with cystic fibrosis) and **cystic-fibrosis-like respiratory disease** driven by excess airway surface liquid and impaired fluid absorption. The disorder is **lifelong**, strongly **associated with consanguinity**, and carries substantial neonatal mortality (~25% in one long cohort) and neurological morbidity from hyperkalemia-induced cardiac arrest.

There is no disease-modifying or curative therapy. Management is lifelong and supportive: **high-dose oral sodium supplementation**, **potassium removal** (cation-exchange resins/binders), and **correction of acidosis**, titrated to electrolytes. Severity tracks **residual channel activity** — truncating/null variants give the most severe, persistent disease, whereas hypomorphic missense or partially active variants can produce milder or even transient phenotypes that improve with age (partly through compensatory upregulation of the thiazide-sensitive Na-Cl cotransporter, NCC). This report compiles the genetics, mechanism, phenotype spectrum, diagnostics, prognosis, treatment, and model-organism evidence for PHA1B1, with primary-literature citations and ontology-term suggestions for knowledge-base curation.

---

## 1. Disease Information

PHA1B1 is the autosomal recessive, **generalized (systemic / multisystem) form of pseudohypoaldosteronism type 1**, a condition of **end-organ resistance to aldosterone**. "Pseudo" denotes that the biochemical picture mimics aldosterone deficiency (salt wasting, hyperkalemia, acidosis) while aldosterone is in fact high — the defect lies downstream of the hormone, in the ENaC effector channel itself.

**Key identifiers:**
- **OMIM:** 264350 (Pseudohypoaldosteronism type I, autosomal recessive)
- **MONDO:** MONDO:0009917
- **Orphanet:** systemic/generalized PHA1 (ORPHA:171876); PHA1 parent ORPHA:79168
- **ICD-10:** E27.4 (other and unspecified adrenocortical insufficiency); **ICD-11:** mineralocorticoid-resistance endocrine disorders
- **MeSH:** D011546 (Pseudohypoaldosteronism)
- **Gene:** SCNN1A, HGNC:10599, NCBI Gene 6337, Ensembl ENSG00000111319, UniProt P37088 (SCNNA_HUMAN), locus 12p13.31

**Synonyms:** autosomal recessive PHA 1; PHA1B; autosomal recessive pseudohypoaldosteronism type 1; generalized/generalised PHA1; generalized/generalised pseudohypoaldosteronism type 1; multisystem/systemic PHA1.

**Nomenclature note:** "PHA1B" is used in OMIM for the recessive ENaC-subunit form as a whole. More granular subtyping assigns **PHA1B1 to SCNN1A**, **PHA1B2 to SCNN1B**, and **PHA1B3 to SCNN1G**. This report concerns the SCNN1A-driven subtype but necessarily draws on the shared ENaC biology, because most mechanistic and clinical literature treats the three subunit genes together.

**Source of information:** Derived almost entirely from **aggregated disease-level resources** (OMIM, Orphanet, reviews) and **published case reports / small single-center cohorts** rather than large EHR datasets, reflecting the disorder's rarity.

---

## 2. Etiology

**Primary cause — genetic.** PHA1B1 is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function mutations in SCNN1A**. Of the three ENaC subunit genes, **SCNN1A-related cases are the most frequent** cause of systemic PHA1.

> [PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/): "The autosomal recessive systemic form (PHA1B), caused by mutations in SCNN1A, SCNN1B, or SCNN1G, is particularly severe and typically manifests in the neonatal period. Among these, SCNN1B-related cases occur less frequently than SCNN1A-related cases."

**Genetic risk factors.**
- **Causal variants:** biallelic LoF variants in SCNN1A (frameshift, nonsense/premature-termination, splice-site; also hypomorphic missense).
- **Consanguinity** is the dominant risk amplifier: it raises the chance of homozygosity for a recessive allele. A 37-year single-center cohort found **all affected children had consanguineous parents** (South Asian, Middle Eastern, or African origin) ([PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/)).
- **Founder effects** exist for specific alleles (e.g., a SCNN1G splice variant shared on a common haplotype across Indian-subcontinent families) ([PMID: 8640238](https://pubmed.ncbi.nlm.nih.gov/8640238/)).

**Environmental risk factors:** None are causal. The disease is fully genetically determined. However, environmental/physiologic **stressors** (intercurrent illness, gastroenteritis, heat, salt restriction, dehydration) precipitate **acute salt-wasting crises** in already-affected individuals.

**Protective factors.**
- **Genetic:** *residual channel activity* is protective in the sense of attenuating severity — missense/hypomorphic alleles that retain partial ENaC function yield milder or transient disease ([PMID: 31301676](https://pubmed.ncbi.nlm.nih.gov/31301676/); [PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/)). Compensatory **NCC (SLC12A3) upregulation** mitigates renal salt loss over time ([PMID: 20376516](https://pubmed.ncbi.nlm.nih.gov/20376516/)).
- **Environmental:** generous dietary **sodium** supplementation functionally rescues the salt-losing phenotype; this is therapeutic rather than preventive of the underlying disorder.

**Gene–environment interaction:** The principal interaction is between the **fixed genetic defect** and **sodium/potassium intake and physiologic stress** — a high-sodium, potassium-managing diet counteracts the channel defect, whereas salt restriction or illness unmasks crises.

---

## 3. Phenotypes

PHA1B1 phenotypes fall into **laboratory abnormalities**, **clinical signs/symptoms**, and **extrarenal manifestations**. Onset is overwhelmingly **neonatal** (first days–weeks of life). Severity in systemic disease is **severe and persistent** (lifelong), contrasting with renal PHA1.

| Phenotype | Type | Onset | Frequency | HPO term |
|---|---|---|---|---|
| Hyponatremia | Lab abnormality | Neonatal | ~Universal | HP:0002902 |
| Hyperkalemia | Lab abnormality | Neonatal | ~Universal | HP:0002153 |
| Metabolic acidosis | Lab abnormality | Neonatal | ~Universal | HP:0001942 |
| Elevated plasma renin | Lab abnormality | Neonatal | ~Universal | HP:0000848 (hyperreninemia) |
| Elevated aldosterone (hyperaldosteronism) | Lab abnormality | Neonatal | ~Universal | HP:0000859 |
| Renal salt wasting | Clinical sign | Neonatal | ~Universal | HP:0000127 (renal salt wasting) |
| Failure to thrive | Clinical sign | Neonatal/infancy | Common | HP:0001508 |
| Dehydration / volume depletion | Clinical sign | Neonatal (crises) | Common | HP:0001944 |
| Vomiting / feeding difficulty | Symptom | Neonatal/infancy | Common | HP:0002013 |
| Recurrent respiratory infection / CF-like lung disease | Clinical sign | Infancy/childhood | Common in systemic form | HP:0002783 / HP:0006532 |
| Cough / wheeze / chest congestion | Symptom | Early childhood (≤5 y) | Frequent in young systemic patients | HP:0012735 / HP:0030828 |
| Elevated sweat chloride / sweat electrolytes | Lab abnormality | Congenital | Characteristic of systemic form | HP:0012236 |
| Skin lesions / eczematous dermatitis / miliaria | Physical manifestation | Infancy | Reported (salt deposition) | HP:0000964 (eczema) |
| Cardiac arrhythmia / arrest (hyperkalemia) | Clinical sign | Neonatal crises | Minority but life-threatening | HP:0011675 |
| Neurodevelopmental impairment (post-arrest) | Clinical sign | After crisis | ~16% in one cohort | HP:0012759 |

**Severity and progression:** Systemic PHA1B1 is typically **severe and lifelong**, with **episodic** salt-wasting crises superimposed on a chronic course. Hypomorphic variants produce **milder, sometimes transient** disease that can improve with age.

**Quality-of-life impact:** Substantial. Affected children require lifelong oral salt and potassium-lowering medication, frequent electrolyte monitoring, and hospital admissions for crises; respiratory involvement adds CF-like morbidity. Survivors of hyperkalemic cardiac arrest may have permanent neurological disability. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist for this rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene.** **SCNN1A** (sodium channel epithelial 1 subunit alpha), 12p13.31; HGNC:10599; OMIM gene 600228; disease OMIM 264350. The gene encodes the **α-ENaC subunit**, which is **obligatory** for channel assembly, trafficking, and Na⁺ conduction. ENaC is a **heterotrimer of α (SCNN1A), β (SCNN1B, 16p12), and γ (SCNN1G, 16p12) subunits** in 1:1:1 stoichiometry.

> [PMID: 38963175](https://pubmed.ncbi.nlm.nih.gov/38963175/): "Systemic PHA type I (PHA1B) has varying degrees of clinical presentation and results from mutations in genes encoding subunits of the epithelial sodium channel (ENaC) including the alpha, beta, and gamma subunits. To date, about 45 variants of PHA1B have been identified."

**Pathogenic variants.**
- **Variant types:** frameshift (including gross deletions, insertions/deletions), nonsense/premature termination, canonical splice-site, and missense. Truncating/null variants predominate in severe systemic disease; a **gross deletion of SCNN1A** has also been reported ([PMID: 41275343](https://pubmed.ncbi.nlm.nih.gov/41275343/)).
- **Classification (ACMG/AMP):** most reported SCNN1A LoF variants are **pathogenic/likely pathogenic**; novel missense variants are sometimes initially **VUS** pending functional testing.
- **Allele frequency:** causal alleles are **very rare** in gnomAD (private/family-specific or founder); LoF constraint on SCNN1A means null alleles are uncommon in the general population.
- **Origin:** **germline**; no somatic involvement.
- **Functional consequence:** **loss of function** — abolished or markedly reduced amiloride-sensitive Na⁺ current. Truncating variants remove pore/gating elements; missense variants reduce open probability (e.g., a γ-ENaC A635V example reduced amiloride-sensitive current by ~30%, illustrating the residual-activity principle) ([PMID: 40153144](https://pubmed.ncbi.nlm.nih.gov/40153144/)).

> [PMID: 8589714](https://pubmed.ncbi.nlm.nih.gov/8589714/): "Investigation of affected offspring of consanguineous union reveals mutations in either the alpha or beta subunits of the amiloride-sensitive epithelial sodium channel in five kindreds. These mutations are homozygous in affected subjects, co-segregate with the disease, and introduce frameshift, premature termination or missense mutations that result in loss of channel activity."

**Modifier genes.** **NCC/SLC12A3** (thiazide-sensitive Na-Cl cotransporter) acts as a physiologic modifier — its upregulation partially compensates for ENaC loss. Broader aldosterone-pathway regulators (WNK kinases, Nedd4L/NEDD4L ubiquitin ligase, channel-activating proteases such as CAP1/Prss8, CAP3/St14, kallikrein-1) influence ENaC abundance/activity and are candidate modulators but are not established clinical modifiers in PHA1B1.

**Epigenetic information:** No disease-specific DNA-methylation or histone-modification findings are established for PHA1B1.

**Chromosomal abnormalities:** Point mutations and small indels dominate; **gross intragenic deletions** of SCNN1A occur but large cytogenetic rearrangements are not characteristic.

---

## 5. Environmental Information

PHA1B1 is a **monogenic disorder with no environmental cause**. There are **no toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents** that cause the disease.

Environmental factors are relevant only as **modulators of the established disease:**
- **Dietary sodium/potassium** — the key modifiable factor (therapeutic high-salt intake; potassium restriction).
- **Heat/sweating** — excess sodium loss through defective sweat glands can worsen salt depletion.
- **Intercurrent infection/gastroenteritis** — precipitates acute crises.

**Infectious agents:** none cause PHA1B1. Notably, recurrent lower-respiratory infections occur as a *consequence* of airway ENaC dysfunction, but — unlike cystic fibrosis — typically **without** characteristic *S. aureus* / *P. aeruginosa* colonization early on ([PMID: 10403853](https://pubmed.ncbi.nlm.nih.gov/10403853/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function mutation in SCNN1A** (frameshift/nonsense/splice/missense) → **leads to** absent or non-functional α-ENaC protein.
2. Loss of the obligatory α-subunit → **results in** failure of ENaC heterotrimer assembly/trafficking and/or absent pore conduction → **abolished amiloride-sensitive Na⁺ current** at the apical membrane of sodium-absorbing epithelia. *(Demonstrated in Xenopus oocyte expression studies.)*
3. In the **distal nephron (connecting tubule/collecting duct)**: loss of apical Na⁺ entry → **leads to** reduced electrogenic Na⁺ reabsorption → **impaired lumen-negative transepithelial voltage** → **reduced driving force for K⁺ and H⁺ secretion**.
4. Branch → **renal salt wasting** (natriuresis, volume depletion) and **impaired K⁺/H⁺ excretion** → **hyponatremia + hyperkalemia + metabolic acidosis**.
5. Volume depletion and hyperkalemia → **stimulate renin and aldosterone** → **very high plasma renin activity and aldosterone**, but because the effector (ENaC) is defective → **target-organ resistance** → biochemical picture *mimics* aldosterone deficiency ("pseudo").
6. Extrarenal branch — ENaC loss in **colon** (fecal Na⁺ loss), **sweat glands** (→ **high sweat Na⁺/Cl⁻**), **salivary glands** (→ **high saliva electrolytes**), and **airway** → multisystem phenotype.
7. Airway branch: loss of ENaC-mediated Na⁺ (and fluid) absorption from airway surfaces → **excess airway surface liquid (>2× normal)** → altered mucociliary clearance and **recurrent chest congestion/cough/wheeze (CF-like)**. *(Demonstrated by in vivo airway measurements.)*
8. Severe hyperkalemia → **can cause cardiac arrhythmia/arrest** → in survivors, hypoxic-ischemic injury → **neurodevelopmental impairment**. *(Observed clinically.)*
9. Compensatory branch (partial): over time, **NCC (SLC12A3) upregulation** in the distal nephron → **partially restores Na⁺ reabsorption** → clinical improvement in some patients. *(Inferred from human urinary NCC protein and mouse models.)*

### Mechanistic detail

**Molecular pathway:** the **aldosterone–mineralocorticoid receptor (MR)–ENaC axis** (renin-angiotensin-aldosterone system, RAAS). Aldosterone normally binds MR (NR3C2), inducing transcription/activity of ENaC and Na⁺/K⁺-ATPase in principal cells. PHA1B1 disables the **terminal effector** (ENaC) rather than the receptor, so RAAS output is high but ineffective ([PMID: 24840884](https://pubmed.ncbi.nlm.nih.gov/24840884/)).

**Protein dysfunction:** Cryo-EM established ENaC as a **heterotrimeric α:β:γ channel** with large extracellular "hand"-like domains (PDB 6BQN), with defined principles of assembly, proteolytic activation, and inhibition ([PMID: 30251954](https://pubmed.ncbi.nlm.nih.gov/30251954/); [PMID: 32729833](https://pubmed.ncbi.nlm.nih.gov/32729833/)). Loss-of-function truncations remove pore/gating elements and abolish current; missense variants lower open probability. Truncated β-ENaC subunits can still support **partial** channel activity, explaining milder phenotypes ([PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/)).

**Cellular processes:** defective transepithelial **ion transport** (sodium reabsorption, potassium/proton secretion) in **epithelial principal cells**; secondary **fluid homeostasis** dysregulation at airway surfaces.

**Biochemical abnormality:** an **ion-channel defect** (amiloride-sensitive Na⁺ channel) — the defining lesion.

**Suggested GO terms:** sodium ion transmembrane transport (GO:0035725); regulation of sodium ion transport (GO:0002028); sodium channel activity (GO:0005272); cellular response to aldosterone (GO:1904045); potassium ion homeostasis (GO:0055075); renal sodium ion absorption (GO:0070294).
**Suggested CL terms:** kidney collecting duct principal cell (CL:1000714); kidney connecting tubule epithelial cell (CL:1000768); eccrine sweat gland cell; respiratory multiciliated epithelial cell (CL:0002145); colonic epithelial cell (CL:0011108).
**Suggested CHEBI terms:** sodium(1+) (CHEBI:29101); potassium(1+) (CHEBI:29103); aldosterone (CHEBI:27584); amiloride (CHEBI:2639).

**Molecular profiling:** No large transcriptomic/proteomic/metabolomic datasets exist for human PHA1B1; mechanistic evidence comes from targeted electrophysiology (oocyte expression) and mouse knockouts.

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Kidney** (distal nephron: connecting tubule, cortical collecting duct) — UBERON:0002113; primary site of salt wasting.
- **Colon / distal large intestine** — UBERON:0001155; fecal sodium loss.
- **Sweat glands (eccrine)** — UBERON:0001820; elevated sweat electrolytes.
- **Salivary glands** — UBERON:0001044; elevated saliva electrolytes.
- **Lung / airway epithelium** — UBERON:0002048; excess airway surface liquid, CF-like disease.

**Secondary/organ systems:** endocrine (RAAS activation), cardiovascular (hyperkalemic arrhythmia), nervous system (post-arrest injury), skin (salt-related dermatitis/eczema).

**Body systems:** renal/urinary, gastrointestinal, integumentary, respiratory, cardiovascular, endocrine.

**Tissue and cell level:** **epithelial tissue** throughout; specifically Na⁺-absorbing **principal cells** of the collecting duct, surface colonocytes, eccrine gland ductal cells, and **airway multiciliated epithelial cells** (ENaC localizes to cilia and regulates surface-liquid volume) ([PMID: 26772908](https://pubmed.ncbi.nlm.nih.gov/26772908/)). ENaC (with CFTR) is expressed in human **epidermis and epidermal appendages including eccrine sweat glands** ([PMID: 28130590](https://pubmed.ncbi.nlm.nih.gov/28130590/)).

**Subcellular level:** **apical plasma membrane** of epithelial cells (GO:0016324, apical plasma membrane); the channel traffics through ER/Golgi and is regulated at the membrane by proteases and Nedd4L-mediated ubiquitination.

**Localization / lateralization:** **bilateral / systemic** — all paired and unpaired target organs are affected symmetrically; this is not a focal or lateralized disorder.

---

## 8. Temporal Development

**Onset:** **Congenital/neonatal**. Essentially all systemic (SCNN1A) cases present within the **first days to two weeks of life**.

> [PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/): "All children were presented within the first 2 weeks of life with life-threatening, severe hyperkalaemia and hyponatraemia. All parents were consanguineous and of South Asian, Middle Eastern or African ethnic origin."

**Onset pattern:** **acute** presentation (salt-wasting crisis / adrenal-crisis-like picture: dehydration, failure to thrive, shock) superimposed on a congenital defect.

**Progression:**
- **Course:** chronic, **lifelong** for severe (truncating) systemic disease, punctuated by **episodic crises** triggered by illness, heat, or salt restriction.
- **Rate:** variable; crises are acute, baseline disease is persistent.
- **Milder variants:** some hypomorphic SCNN1A/SCNN1B cases show **transient** disease that improves/remits with age, partly via NCC compensation and reduced dependence on ENaC for salt homeostasis with growth ([PMID: 23426840](https://pubmed.ncbi.nlm.nih.gov/23426840/); [PMID: 37134141](https://pubmed.ncbi.nlm.nih.gov/37134141/)).

**Remission patterns:** No spontaneous cure for severe disease; **treatment-controlled** stability is achievable. Partial, age-related improvement occurs with hypomorphic alleles.

**Critical period:** The **neonatal period** is the window of maximal vulnerability (hyperkalemic cardiac arrest) and the critical window for diagnosis and electrolyte stabilization to prevent death and neurological injury.

---

## 9. Inheritance and Population

**Inheritance:** **Autosomal recessive**. Both *SCNN1A* alleles must be non-functional (homozygous or compound heterozygous).

**Epidemiology:** Very rare; systemic PHA1 prevalence is not precisely established (orders of magnitude rarer than the autosomal dominant renal form). Overall PHA1 is estimated at roughly **1 in 80,000 newborns** (all forms), with the recessive systemic form being a minority.

**Penetrance:** **Complete** for biallelic LoF genotypes (all homozygotes manifest).
**Expressivity:** **Variable**, driven chiefly by **residual channel activity** (genotype–phenotype correlation).

> [PMID: 31301676](https://pubmed.ncbi.nlm.nih.gov/31301676/): "Patients presenting with missense mutations of SCNN1A and SCNN1B had a less marked rise in serum aldosterone suggesting preservation in sodium epithelial channel function."

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
**Germline mosaicism:** Not a described feature.
**Consanguinity:** **Major contributing factor** — nearly all recessive systemic cases arise in consanguineous unions.
**Founder effects:** Documented for specific ENaC alleles (e.g., shared SCNN1G splice haplotype in Indian-subcontinent families; clustered SCNN1A variants in defined geographic populations such as a Sicilian town) ([PMID: 8640238](https://pubmed.ncbi.nlm.nih.gov/8640238/); [PMID: 34134742](https://pubmed.ncbi.nlm.nih.gov/34134742/)).
**Carrier frequency:** Low; not precisely quantified for SCNN1A; heterozygous carriers are asymptomatic.

**Population demographics:** Reported disproportionately in populations with **high consanguinity** — South Asian, Middle Eastern, North/Sub-Saharan African, and certain Mediterranean communities ([PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/)).
**Sex ratio:** ~1:1 (autosomal recessive; no sex predilection).
**Age distribution:** Diagnosed in neonates; affected individuals survive into childhood/adulthood with treatment.

---

## 10. Diagnostics

**Laboratory tests (core):**
- Serum electrolytes: **hyponatremia, hyperkalemia** (LOINC 2951-2 sodium; 2823-3 potassium).
- **Metabolic acidosis** (low bicarbonate; LOINC 1963-8).
- **Plasma renin activity — markedly elevated** (LOINC 2915-7).
- **Plasma/serum aldosterone — markedly elevated**; elevated **aldosterone:renin ratio** (LOINC 1763-2).
- Urinary electrolytes: **high urine sodium**, inappropriately low urine K⁺ excretion for the degree of hyperkalemia.
- **Normal cortisol and normal 17-hydroxyprogesterone** — essential to exclude salt-wasting congenital adrenal hyperplasia (21-hydroxylase deficiency).

**Extrarenal / differentiating tests:**
- **Sweat chloride test** — elevated in systemic PHA1, overlapping with cystic fibrosis.
- **Saliva electrolytes** — elevated.

> [PMID: 7965429](https://pubmed.ncbi.nlm.nih.gov/7965429/): "Four patients with severe pseudohypoaldosteronism caused by multiple end-organ resistance to aldosterone had frequently recurring lower respiratory tract infections and persistently elevated sweat and saliva electrolyte values."

**Genetic testing (confirmatory):**
- **Single-gene / gene-panel sequencing** of *SCNN1A, SCNN1B, SCNN1G* (systemic form) and *NR3C2* (renal form) is the definitive approach.
- **Whole-exome sequencing (WES)** is widely used and has identified novel SCNN1A variants; **whole-genome sequencing (WGS)** or deletion/duplication analysis (MLPA/CMA) is needed to detect **gross deletions** missed by standard sequencing ([PMID: 41275343](https://pubmed.ncbi.nlm.nih.gov/41275343/)).
- Functional confirmation (Xenopus oocyte amiloride-sensitive current) resolves VUS, especially missense variants.

**Clinical diagnostic criteria:** Neonatal salt-wasting (hyponatremia + hyperkalemia + metabolic acidosis) **with high renin and aldosterone** and **poor/absent response to mineralocorticoid (fludrocortisone)**, after excluding adrenal insufficiency/CAH, plus confirmatory genetics.

**Differential diagnosis:**
- **Salt-wasting congenital adrenal hyperplasia (21-OH deficiency)** — distinguished by elevated 17-OHP, low aldosterone, response to steroid.
- **Primary adrenal insufficiency / aldosterone synthase deficiency** — low aldosterone (vs high in PHA).
- **Autosomal dominant renal PHA1 (NR3C2)** — milder, kidney-restricted, normal sweat electrolytes, often improves with age ([PMID: 26817011](https://pubmed.ncbi.nlm.nih.gov/26817011/)).
- **Secondary (transient) PHA** — e.g., urinary tract infection/obstructive uropathy in infants.
- **Cystic fibrosis** — overlapping high sweat chloride and respiratory disease; PHA1 may be clinically indistinguishable until hormonal/genetic testing.

> [PMID: 22208790](https://pubmed.ncbi.nlm.nih.gov/22208790/): "Pseudohypoaldosteronism type 1 may be indistinguishable from cystic fibrosis (CF) unless serum aldosterone, plasma renin activity, and urinary electrolytes are measured and mutation analysis rules out CF."

Notably, PHA1 and CF can rarely **coexist** ([PMID: 38914525](https://pubmed.ncbi.nlm.nih.gov/38914525/)).

**Screening:** No routine newborn screen for PHA1B1; **cascade/carrier testing** and **prenatal/preimplantation diagnosis** are available for families with a known SCNN1A variant.

---

## 11. Outcome / Prognosis

**Mortality:** Significant in severe systemic disease, driven by **hyperkalemic cardiac arrest** in the neonatal/infant period.

> [PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/): "Three children died (25%) and two (16%) had severe neurological impairment post-cardiac arrest secondary to hyperkalaemia."

**Morbidity / disability:** Neurological impairment in survivors of cardiac arrest (~16% in the cited cohort); chronic burden of electrolyte management; CF-like respiratory morbidity in systemic cases.

**Life expectancy:** With **intensive lifelong electrolyte management**, survival with **normal neurodevelopment is achievable**. Growth is often normal with adequate salt replacement ([PMID: 8865238](https://pubmed.ncbi.nlm.nih.gov/8865238/)).

**Disease course / complications:** Recurrent dehydration/crises, failure to thrive, recurrent respiratory infections, and (in a minority) cardiac/neurological catastrophe. Systemic (SCNN1A) disease has a **poorer prognosis than renal (NR3C2) disease** and generally does **not** remit with age when the variant is a true null.

**Prognostic factors:**
- **Genotype / residual channel activity** — the dominant prognostic determinant (truncating = severe/persistent; missense/hypomorphic = milder/transient).
- **Severity of initial hyperkalemia** and timeliness of neonatal stabilization (predicts arrest/neurological outcome).

---

## 12. Treatment

There is **no curative or disease-modifying therapy**. Management is **lifelong, supportive, and electrolyte-directed**.

**Pharmacotherapy / supportive care (NCIT suggestions in parentheses):**
- **Oral sodium chloride supplementation**, high-dose (often up to ~10–45 mmol/kg/day), the cornerstone of therapy (NCIT:C692 Sodium Chloride).
- **Sodium bicarbonate** to correct metabolic acidosis (NCIT:C29141 Sodium Bicarbonate).
- **Potassium-lowering measures:** cation-exchange resins — **sodium polystyrene sulfonate (Kayexalate)** — and newer potassium binders (patiromer, sodium zirconium cyclosilicate) (NCIT:C47704 Polystyrene Sulfonate). Dietary potassium restriction.
- **Acute hyperkalemia management:** insulin/glucose, beta-agonists, calcium gluconate (cardioprotection), and dialysis in refractory cases.
- **Mineralocorticoids (fludrocortisone) are INEFFECTIVE** — the defect is downstream of the receptor — and do **not** form part of definitive therapy (useful diagnostically by their lack of effect).
- **Indomethacin** has been used empirically in some historical cases to reduce salt loss, with reported benefit, but is not standard ([PMID: 6395746](https://pubmed.ncbi.nlm.nih.gov/6395746/)).

**Respiratory care:** For systemic patients with CF-like airway disease, **CF-style airway clearance and infection management** may be required.

> [PMID: 7965429](https://pubmed.ncbi.nlm.nih.gov/7965429/): "Patients with pseudohypoaldosteronism may require treatment similar to that for cystic fibrosis to prevent long-term respiratory complications."

**Advanced/experimental therapeutics:** No approved gene, cell, RNA-based, or targeted therapy exists. Proof-of-concept laboratory work shows **pharmacological rescue of channel function** — e.g., the **TNF lectin-like domain (AP301/solnatide)** restored ENaC function in PHA1B frameshift mutants in vitro ([PMID: 28611771](https://pubmed.ncbi.nlm.nih.gov/28611771/)) — but this is not a clinical therapy for PHA1B1.

**Treatment strategy:** Individualized titration of sodium supplementation, acidosis correction, and potassium control to normalize electrolytes and support growth; multidisciplinary follow-up (endocrinology, nephrology, pulmonology, genetics). Personalized intensity is guided by **genotype/residual activity** — milder variants may need less and may be weaned as the child grows.

**Treatment outcomes:** With adherence, electrolytes and renin/aldosterone can normalize and growth proceeds normally; however, severe cases demand large daily supplement doses and remain at risk of crises.

---

## 13. Prevention

The disease itself cannot be prevented (congenital genetic cause); prevention focuses on **avoiding complications** and **reproductive risk reduction**.

- **Primary prevention:** Not applicable for disease occurrence. **Genetic counseling** for consanguineous couples and families with a known variant; **carrier testing**, **prenatal diagnosis**, and **preimplantation genetic diagnosis** allow informed reproductive choices and early preparedness ([PMID: 34134742](https://pubmed.ncbi.nlm.nih.gov/34134742/)).
- **Secondary prevention:** Early recognition of neonatal salt-wasting and prompt genetic confirmation to start therapy before a catastrophic hyperkalemic event; cascade screening of at-risk siblings.
- **Tertiary prevention:** Rigorous electrolyte management, sick-day rules (increased salt, early medical review during illness/heat), and respiratory surveillance to prevent crises, cardiac arrest, neurological injury, and chronic lung disease.
- **Immunization / public health / environmental interventions:** Not applicable to the genetic cause; routine childhood immunization and respiratory-infection precautions are prudent given airway involvement.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (*Homo sapiens*, NCBI Taxon 9606). Naturally occurring PHA1B1 is not a recognized spontaneous disease in companion animals or wildlife (no OMIA entry for a natural SCNN1A-PHA phenotype of veterinary importance).
- **Orthologous genes:** *Scnn1a* in mouse (NCBI Gene 20276, chr 6) and rat (*Scnn1a*, NCBI Gene 25122). ENaC subunit genes are **deeply conserved** across vertebrates — orthologs appear from jawless fish onward, and most tetrapods carry four ENaC paralogs ([PMID: 26772908](https://pubmed.ncbi.nlm.nih.gov/26772908/)).
- **Comparative biology:** The aldosterone–ENaC axis is evolutionarily conserved, making rodent models highly informative. Complete α-ENaC knockout in mice is **neonatally lethal from defective lung fluid clearance**, underscoring the channel's conserved role in airway as well as renal sodium/fluid handling.
- **Transmission:** None — non-infectious, non-zoonotic genetic disorder.

---

## 15. Model Organisms

**Mouse (Mus musculus) — the principal model.**
- **Constitutive α-ENaC (*Scnn1a*) knockout:** dies within ~40 h of birth from failure to clear lung fluid — demonstrating ENaC's essential role in perinatal airway fluid absorption and modeling the respiratory dimension of systemic PHA1.
- **Inducible, nephron-specific α-ENaC knockout (Scnn1a^Pax8/LC1):** recapitulates renal PHA-1 in adults — **hyperkalemia and body-weight loss on a regular diet**, rescued by a high-Na⁺/low-K⁺ diet.

> [PMID: 26701978](https://pubmed.ncbi.nlm.nih.gov/26701978/): "We generated adult inducible nephron-specific αENaC-knockout mice (Scnn1a(Pax8/LC1)) that exhibit hyperkalemia and body weight loss when kept on a regular-salt diet, thus mimicking PHA-1."

- Importantly, these mice reveal a **compensatory mechanism**: on a regular diet NCC is paradoxically downregulated despite high aldosterone, and a rescue diet normalizes electrolytes and restores NCC — dovetailing with the human finding of NCC-mediated compensation ([PMID: 20376516](https://pubmed.ncbi.nlm.nih.gov/20376516/)).
- **Conditional (floxed) alleles for Scnn1b and Scnn1g** exist to dissect β- and γ-subunit roles, since their constitutive knockouts are also perinatally lethal ([PMID: 19036848](https://pubmed.ncbi.nlm.nih.gov/19036848/)).

**In vitro / cellular models:**
- **Xenopus laevis oocyte expression** of mutant ENaC subunits is the standard functional assay for pathogenicity and residual activity (e.g., truncated β-ENaC retains partial activity; γ-A635V reduces current ~30%) ([PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/); [PMID: 40153144](https://pubmed.ncbi.nlm.nih.gov/40153144/)).

**Model characteristics:** Inducible nephron-specific knockouts **faithfully reproduce the renal electrolyte phenotype** and the diet-dependent compensation; constitutive knockouts capture the **lethal pulmonary** phenotype. **Limitations:** no single mouse fully reproduces the complete human multisystem spectrum simultaneously (renal + sweat/saliva + chronic survivable lung disease), and perinatal lethality of global knockouts necessitates conditional/inducible strategies.

**Resources:** MGI (*Scnn1a*, *Scnn1b*, *Scnn1g*), IMPC/KOMP conditional alleles, IMSR.

---

## Mechanistic Model (Synthesis)

```
   Biallelic LoF mutation in SCNN1A (12p13)
                 │
                 ▼
   Absent / non-functional α-ENaC subunit
                 │   (α is obligatory for assembly + conduction)
                 ▼
   No functional α:β:γ ENaC heterotrimer at apical membrane
                 │
     ┌───────────┼─────────────┬──────────────┬───────────────┐
     ▼           ▼             ▼              ▼               ▼
  Kidney      Colon        Sweat gland    Saliva gland      Airway
 (CD/CNT)   (Na⁺ loss)   (↑sweat Na/Cl)  (↑saliva e-lytes) (↓Na⁺+fluid
     │                                                      absorption)
     ▼                                                         ▼
 ↓Na⁺ reabsorption → ↓lumen-negative voltage            Airway surface
 → ↓K⁺/H⁺ secretion                                     liquid >2× normal
     │                                                         ▼
     ▼                                                 CF-like cough/
 HYPONATREMIA + HYPERKALEMIA + METABOLIC ACIDOSIS      wheeze/infection
     │                               │
     ▼                               ▼
 RAAS activation →            Severe hyperkalemia →
 ↑↑renin, ↑↑aldosterone       cardiac arrhythmia/arrest →
 (ineffective = "pseudo")     neurological injury (survivors)
     │
     ▼
 Partial compensation over time: ↑NCC (SLC12A3) → mild/transient improvement
```

**Upstream vs downstream:** The mutation and loss of ENaC conduction are **upstream**; renal/colonic salt wasting and the electrolyte triad are **proximal downstream** effects; RAAS activation, crises, cardiac/neurological events, and respiratory disease are **distal downstream** consequences. NCC upregulation is a **compensatory feedback branch**.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [8589714](https://pubmed.ncbi.nlm.nih.gov/8589714/) | ENaC subunit mutations cause PHA1 | Human genetics (landmark) | Causal LoF in α/β ENaC; recessive inheritance |
| [8640238](https://pubmed.ncbi.nlm.nih.gov/8640238/) | Homozygosity mapping of PHA1 | Human genetics (landmark) | Loci at 12p (SCNN1A) & 16p; founder haplotype |
| [38963175](https://pubmed.ncbi.nlm.nih.gov/38963175/) | Novel SCNN1A mutation, PHA1B | Human case / review | PHA1B from ENaC subunits; ~45 variants |
| [41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/) | PHA1B2 twins (SCNN1B) | Human case | Gene triad; severity; SCNN1A most common |
| [33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/) | AR-PHA1 clinical cohort | Human cohort (12 pts, 37 y) | Neonatal onset, consanguinity, 25% mortality |
| [31301676](https://pubmed.ncbi.nlm.nih.gov/31301676/) | Genotype–phenotype in PHA1 | Human cohort | Missense → residual activity, milder disease |
| [10403853](https://pubmed.ncbi.nlm.nih.gov/10403853/) | Airway ENaC dysfunction in PHA1 | Human physiology | Abolished airway Na⁺ absorption; 2× ASL |
| [22208790](https://pubmed.ncbi.nlm.nih.gov/22208790/) | Pulmonary complications review | Review | PHA1 vs CF differentiation |
| [7965429](https://pubmed.ncbi.nlm.nih.gov/7965429/) | Sweat/saliva electrolytes in PHA | Human case series | Elevated sweat/saliva; CF-like respiratory care |
| [28130590](https://pubmed.ncbi.nlm.nih.gov/28130590/) | ENaC/CFTR in epidermis | Human expression | Molecular basis of sweat phenotype |
| [20376516](https://pubmed.ncbi.nlm.nih.gov/20376516/) | NCC upregulation in AR-PHA1 | Human | Compensatory NCC mechanism |
| [26701978](https://pubmed.ncbi.nlm.nih.gov/26701978/) | Nephron-specific αENaC KO mouse | Mouse model | Recapitulates renal PHA-1 |
| [19036848](https://pubmed.ncbi.nlm.nih.gov/19036848/) | Conditional Scnn1b/Scnn1g | Mouse model | Tools for subunit dissection |
| [20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/) | Truncated β-ENaC partial activity | In vitro (oocyte) | Residual-activity genotype–phenotype |
| [40153144](https://pubmed.ncbi.nlm.nih.gov/40153144/) | γ-ENaC A635V function | In vitro + human | Missense reduces current ~30% |
| [30251954](https://pubmed.ncbi.nlm.nih.gov/30251954/) | Cryo-EM ENaC structure | Structural | Heterotrimeric architecture |
| [32729833](https://pubmed.ncbi.nlm.nih.gov/32729833/) | ENaC assembly/activation | Structural | Assembly, proteolytic activation |
| [26772908](https://pubmed.ncbi.nlm.nih.gov/26772908/) | ENaC family review | Review | Tissue distribution, phylogeny, disease |
| [24840884](https://pubmed.ncbi.nlm.nih.gov/24840884/) | Aldosterone function disorders | Review | RAAS–ENaC axis, PHA genetics |
| [28611771](https://pubmed.ncbi.nlm.nih.gov/28611771/) | TNF lectin-like domain rescue | In vitro | Experimental channel rescue |
| [41275343](https://pubmed.ncbi.nlm.nih.gov/41275343/) | Gross deletion in SCNN1A | Human case | Deletion-detection diagnostic gap |
| [34134742](https://pubmed.ncbi.nlm.nih.gov/34134742/) | SCNN1A splice mutation, Sicily | Human case | Founder clustering; prevention via NGS |
| [37134141](https://pubmed.ncbi.nlm.nih.gov/37134141/) | Mild/transient AR-PHA1 | Human cohort | Milder phenotype spectrum |
| [23426840](https://pubmed.ncbi.nlm.nih.gov/23426840/) | SCNN1B splice mutation, Turkey | Human case | Age-related improvement mechanism |
| [8865238](https://pubmed.ncbi.nlm.nih.gov/8865238/) | Severe PHA twins | Human case | Lifelong management; normal growth achievable |
| [6395746](https://pubmed.ncbi.nlm.nih.gov/6395746/) | PHA review / indomethacin | Human case | Historical salt/indomethacin therapy |
| [26817011](https://pubmed.ncbi.nlm.nih.gov/26817011/) | Renal PHA1 (NR3C2) | Human case | Distinguishes renal vs systemic PHA1 |
| [38914525](https://pubmed.ncbi.nlm.nih.gov/38914525/) | PHA1 coexisting with CF | Human case | PHA1/CF overlap and coexistence |

---

## Limitations and Knowledge Gaps

1. **SCNN1A-specific vs pooled data.** Much of the clinical and mechanistic literature pools the three ENaC subunit genes under "PHA1B." Pure SCNN1A-only cohorts are small, and some cited cohorts include SCNN1G/SCNN1B patients.
2. **No large-scale omics.** No transcriptomic, proteomic, metabolomic, or single-cell datasets exist specifically for human PHA1B1; mechanism rests on targeted electrophysiology and mouse genetics.
3. **Epidemiology imprecise.** True prevalence/incidence and carrier frequency of SCNN1A-PHA1B1 are not well quantified; estimates are extrapolated from all-PHA1 figures.
4. **Structure–function for specific variants.** Only a minority of reported SCNN1A variants have functional characterization; many remain inferred LoF.
5. **No disease-modifying therapy.** Promising in vitro channel-rescue approaches (e.g., solnatide/AP301) have not been translated to PHA1B1 clinical trials.
6. **Quality-of-life data absent.** No validated QoL instrument data for this rare disorder.
7. **Deletion detection gap.** Standard sequencing can miss gross SCNN1A deletions, risking under-diagnosis.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble an SCNN1A-only genotype–phenotype registry** correlating variant class (null vs hypomorphic) and functional residual activity with mortality, salt-requirement, and respiratory outcomes.
2. **Systematic functional assays** (oocyte/mammalian electrophysiology + cryo-EM-guided modeling) for all reported SCNN1A VUS to firm up ACMG classification and residual-activity predictions.
3. **Ensure deletion/duplication analysis (MLPA/CMA/WGS)** in genetically unconfirmed clinically typical cases to close the gross-deletion diagnostic gap.
4. **Translate channel-rescue pharmacology** (e.g., solnatide/AP301, small-molecule ENaC potentiators) toward preclinical PHA1B1 models and, if promising, early-phase trials.
5. **Characterize the extrarenal burden** (longitudinal sweat/saliva electrolytes, pulmonary function, airway microbiome) to define when CF-style respiratory care improves outcomes.
6. **Investigate NCC-targeted or dietary strategies** that exploit the compensatory NCC branch to reduce salt-supplement burden.
7. **Develop a humanized/hypomorphic knock-in mouse** reproducing the survivable multisystem phenotype for therapeutic testing.

---

*Report compiled from 7 confirmed findings and 36 reviewed papers across a 5-iteration autonomous investigation. Evidence source types are indicated throughout (human clinical, model organism, in vitro, structural/computational).*


## Artifacts

- [OpenScientist final report](Pseudohypoaldosteronism_Type_IB1_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pseudohypoaldosteronism_Type_IB1_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 13 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002902` (1 mention) - the report calls it "~Universal"; HP calls it **Hyponatremia**
- `HP:0002153` (1 mention) - the report calls it "~Universal"; HP calls it **Hyperkalemia**
- `HP:0001942` (1 mention) - the report calls it "~Universal"; HP calls it **Metabolic acidosis**
- `HP:0000859` (1 mention) - the report calls it "~Universal"; HP calls it **Increased circulating aldosterone concentration**
- `HP:0001508` (1 mention) - the report calls it "Common"; HP calls it **Failure to thrive**
- `HP:0001944` (1 mention) - the report calls it "Common"; HP calls it **Dehydration**
- `HP:0002013` (1 mention) - the report calls it "Common"; HP calls it **Vomiting**
- `HP:0012236` (1 mention) - the report calls it "Characteristic of systemic form"; HP calls it **Elevated sweat chloride**
- `HP:0011675` (1 mention) - the report calls it "Minority but life-threatening"; HP calls it **Arrhythmia**
- `HP:0012759` (1 mention) - the report calls it "~16% in one cohort"; HP calls it **Neurodevelopmental abnormality**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000848` (1 mention) - the report calls it "hyperreninemia"; HP calls it **Increased circulating renin concentration**, and lists "Hyperreninemia" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:171876` - called "systemic PHA1", "Orphanet:** systemic/generalized PHA1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.