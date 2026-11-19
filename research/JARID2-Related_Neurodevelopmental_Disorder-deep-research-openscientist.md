---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-07T11:33:18.959509'
end_time: '2026-11-07T11:45:03.036700'
duration_seconds: 704.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: JARID2-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0859306
  category: Mendelian
  causal_genes: JARID2
  omim_id: OMIM:620098
  synonyms: not recorded
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
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 11
  validator_version: 0.5.1
term_validation:
  total_terms: 43
  verified: 36
  not_found: 0
  obsolete: 3
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 10
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: HP:0001249
    reported_labels:
    - high (most)
    ontology_label: Intellectual disability
  - term_id: HP:0000750
    reported_labels:
    - common
    ontology_label: Delayed speech and language development
  - term_id: HP:0001252
    reported_labels:
    - common
    ontology_label: Hypotonia
  - term_id: HP:0000729
    reported_labels:
    - subset
    ontology_label: Autistic behavior
  - term_id: HP:0000336
    reported_labels:
    - characteristic
    ontology_label: Prominent supraorbital ridges
  - term_id: HP:0000490
    reported_labels:
    - characteristic
    ontology_label: Deeply set eye
  - term_id: HP:0000652
    reported_labels:
    - periorbital
    ontology_label: Lower eyelid coloboma
  - term_id: HP:0011800
    reported_labels:
    - characteristic
    ontology_label: Midface retrusion
  - term_id: HP:0001999
    reported_labels:
    - characteristic
    ontology_label: Abnormal facial shape
  - term_id: HP:0000174
    reported_labels:
    - subset
    ontology_label: Abnormal palate morphology
  - term_id: HP:0001627
    reported_labels:
    - subset
    ontology_label: Abnormal heart morphology
  - term_id: GO:0006342
    reported_labels:
    - chromatin silencing
    ontology_label: GO_0006342
  - term_id: UBERON:0005732
    reported_labels:
    - neural plate
    ontology_label: paired limb/fin field
  - term_id: NCIT:C15277
    reported_labels:
    - 'NCIT examples: Supportive Care'
    - supportive care
    ontology_label: Mastectomy
  - term_id: NCIT:C15317
    reported_labels:
    - occupational therapy
    ontology_label: Second-Look Surgery
  - term_id: NCIT:C15312
    reported_labels:
    - speech-language therapy
    - speech therapy
    ontology_label: Radiation Dosimetry
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0006342
    ontology_label: GO_0006342
    replaced_by: GO:0031507
  - term_id: GO:0070734
    ontology_label: obsolete histone H3-K27 methylation
  - term_id: NCIT:C15368
    ontology_label: Treatment
  unresolvable_prefixes:
  - OMIM
  - Gene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: JARID2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: JARID2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** JARID2-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0859306 (if available)
- **Causal gene(s):** JARID2
- **OMIM:** OMIM:620098
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **JARID2-Related Neurodevelopmental Disorder** covering all of the
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

# JARID2-Related Neurodevelopmental Disorder — Comprehensive Disease Characterization

**Causal gene: _JARID2_ (Jumonji And AT-Rich Interaction Domain 2; HGNC:6826; NCBI Gene 3720; UniProt Q92833).**
**MONDO:0859306 · OMIM:620098 (NEURODEVELOPMENTAL DISORDER WITH DELAYED SPEECH AND BEHAVIORAL ABNORMALITIES; gene OMIM:601594) · Category: Mendelian, autosomal dominant.**

> Note on identity: The disease name is generic ("neurodevelopmental disorder"), so this report is anchored to the MONDO/OMIM identifiers and the causal gene **JARID2** given in the brief. JARID2 sits on chromosome **6p22.3** and encodes a Polycomb Repressive Complex 2 (PRC2) accessory subunit. This should not be confused with the many other serially numbered neurodevelopmental disorders (e.g., those caused by SETD5, ANKRD11, KMT2A), which are distinct chromatinopathies.

---

## 1. Disease Information

**Overview.** JARID2-Related Neurodevelopmental Disorder is a rare, recently delineated Mendelian chromatinopathy caused by heterozygous loss-of-function (and, less commonly, gain-of-dosage) alterations of *JARID2*. It is characterized by global developmental delay and/or intellectual/learning disability (ID), speech delay, autism/behavioral-neuropsychiatric abnormalities, hypotonia, and a recognizable facial gestalt (prominent supraorbital ridges, deep-set eyes, dark infraorbital circles, midface hypoplasia); palatal abnormalities and congenital heart defects occur in a subset. Gene–disease validity was formally established by Verberne et al. 2021 in a cohort of 16 individuals from 15 families (PMID 33077894): *"We report that JARID2 haploinsufficiency leads to a clinically distinct neurodevelopmental syndrome, thus establishing gene-disease validity for the purpose of diagnostic reporting."* It was independently confirmed and phenotypically expanded by Cadieux-Dion et al. 2022 (PMID 35533077, 7 individuals/5 families).

**Key identifiers.**
- MONDO: **MONDO:0859306**
- OMIM (phenotype): **620098**; OMIM (gene JARID2): **601594**
- Gene: HGNC:6826 · NCBI Gene:3720 · Ensembl ENSG00000008083 · UniProt Q92833
- Orphanet: JARID2-related disorder is covered under 6p22-p24 deletion / rare chromatinopathies (no unique high-visibility ORPHAcode widely assigned at time of writing — **not definitively recorded**).
- ICD-11: closest mapping **LD2F.1Y / 6A00.Z** style codes for syndromic intellectual developmental disorders (no JARID2-specific code — **not available**).
- MeSH: no JARID2-specific descriptor; indexed under *Intellectual Disability* and *Neurodevelopmental Disorders*.

**Synonyms / alternative names.** "JARID2 haploinsufficiency syndrome"; "JARID2-related intellectual disability"; historically a subset of "6p22-p24 deletion syndrome." Older gene aliases: **JMJ** (jumonji), Jumonji homolog.

**Source of information.** Entirely **disease-level/individual-patient case-series literature** (aggregated published cohorts and single case reports), not EHR-derived population data. Evidence is predominantly human clinical (case series) plus model-organism and in-vitro mechanistic work.

---

## 2. Etiology

**Primary cause — genetic.** The disorder is caused by heterozygous germline alterations of *JARID2*: (i) intragenic/whole-gene **deletions** (including contiguous 6p22-p24 deletions encompassing JARID2), and (ii) **single-nucleotide loss-of-function variants** (nonsense, frameshift, splice) predicted to trigger nonsense-mediated mRNA decay → haploinsufficiency (Verberne 2021, PMID 33077894: *"Several of these variants are likely to result in haploinsufficiency due to nonsense-mediated messenger RNA (mRNA) decay."*). A de novo partial **duplication** (exons 1–7) causing increased expression has also been reported (Viitasalo 2022, PMID 35979655), indicating bidirectional dosage sensitivity.

**Genetic risk factors.** The causal variant *is* the risk factor (monogenic, high-penetrance). Most cases are **de novo**. Candidate **modifier** influences: genetic background strongly modulates penetrance in the mouse ortholog (strain-dependent neural-tube defects; Takeuchi 1999, PMID 10446263), suggesting unidentified human modifier loci. Adjacent 6p22.3 gene **ATXN1** (and DTNBP1, GMPR) contributes to the broader phenotype in large contiguous deletions (Barøy 2013, PMID 23294540).

**Environmental risk factors.** **None established.** No toxin, infection, or lifestyle exposure is implicated. Advanced parental age is a generic contributor to de novo mutation rate but is not specifically documented here.

**Protective factors (genetic or environmental).** **None identified / not applicable.**

**Gene–environment interactions.** **Not documented** in humans. By analogy with the mouse (variable neural-tube-defect penetrance across strains), genetic background likely interacts with the primary lesion, but no specific GxE interaction is proven.

---

## 3. Phenotypes

Frequencies are qualitative/approximate, drawn from small published cohorts (Barøy 2013 n≈5; Verberne 2021 n=16). Onset is **congenital/early childhood**; course is **static (non-progressive) but lifelong**.

| Phenotype | Type | Frequency | HPO term |
|---|---|---|---|
| Global developmental delay | clinical sign | ~100% | HP:0001263 |
| Intellectual disability (mild–moderate, variable) | clinical sign | high (most) | HP:0001249 |
| Delayed speech/language development | clinical sign | common | HP:0000750 |
| Motor delay / gait disturbance | clinical sign | common | HP:0001270 / HP:0001288 |
| Muscular hypotonia | clinical sign | common | HP:0001252 |
| Behavioral/neuropsychiatric abnormality (incl. autistic features, ADHD) | behavioral | common | HP:0000708 / HP:0000729 |
| Prominent supraorbital ridges | physical | characteristic | HP:0000336 |
| Deeply set eyes | physical | characteristic | HP:0000490 |
| Dark infraorbital circles | physical | characteristic | HP:0000652 (periorbital) |
| Midface retrusion/hypoplasia | physical | characteristic | HP:0011800 |
| Abnormal facial gestalt | physical | characteristic | HP:0001999 |
| Autism spectrum / autistic behavior | behavioral | subset | HP:0000729 |
| Palatal abnormality (high-arched/cleft) | physical | subset | HP:0000174 |
| Congenital heart defect | physical | subset | HP:0001627 |

**Severity:** mild to moderate, **variable** between individuals (variable expressivity — some carrier parents are only mildly affected; Cadieux-Dion 2022, PMID 35533077). **Progression:** stable/static developmental disorder; not neurodegenerative. **Seizures, structural brain, growth, and organ anomalies** are reported variably in large contiguous deletions but are **not consistently attributable to JARID2 alone — data incomplete.** Palatal and cardiac anomalies are now recognized as part of the single-gene phenotype in a subset (PMID 35533077).

**Quality-of-life impact.** Lifelong impact on learning, communication, adaptive function, and independence; behavioral comorbidity affects caregiver burden. No disease-specific EQ-5D/SF-36/PROMIS data exist (**not available**); impact inferred from the ID/ASD-spectrum QoL literature.

---

## 4. Genetic / Molecular Information

**Causal gene.** *JARID2* (HGNC:6826; OMIM 601594), 6p22.3, ~28 exons, encoding a ~1246-aa nuclear protein with a **JmjN, JmjC** (enzymatically dead — lacks key Fe(II)/2-OG-coordinating residues), an **ARID/Bright DNA-binding** domain, and a zinc finger. It is a **catalytically inactive Jumonji-family** protein.

**Pathogenic variants.**
- **Types:** whole-gene & intragenic deletions; CNV at 6p22-p24; nonsense/frameshift/splice LoF SNVs (NMD → haploinsufficiency); at least one partial **duplication** (gain). A homozygous **missense** (c.899G>A, p.Arg300Gln) underlies a separate recessive reproductive phenotype (Sun 2025, PMID 40886009).
- **Classification (ACMG/AMP):** truncating LoF variants → Pathogenic/Likely pathogenic (PVS1-supported); many missense remain **VUS**, where DNA-methylation episignature testing can help reclassification (chromatinopathy EpiSign framework, Koparir 2026, PMID 41957673).
- **Allele frequency:** pathogenic alleles are **absent/ultra-rare** in gnomAD; JARID2 is a predicted **loss-of-function-intolerant** gene (consistent with haploinsufficiency; precise pLI/LOEUF to confirm in gnomAD — qualitative).
- **Origin:** predominantly **germline, de novo**. No somatic-disease role in this NDD.
- **Functional consequence:** **loss of function / haploinsufficiency** (dominant); duplication implies **dosage-gain** also pathogenic.

**Modifier genes.** Within 6p22.3: **ATXN1** (independent ID contributor), DTNBP1, GMPR (Barøy 2013). Genetic background acts as modifier in mouse.

**Epigenetic information.** JARID2 is itself an epigenetic regulator (PRC2.2). Loss alters genome-wide **H3K27me3** at developmental targets; a **blood DNA-methylation episignature** is being defined for diagnostic use (van der Laan 2023, PMID 37762546; chromatinopathy EpiSign cohorts, PMID 41957673).

**Chromosomal abnormalities.** Interstitial **6p22-p24 deletions** (0.1–17 Mb) are the historical presentation (Barøy 2013; Verberne 2021). DECIPHER/ClinVar/dbVar are relevant repositories.

---

## 5. Environmental Information

- **Environmental factors:** none implicated — **not applicable** (monogenic disorder).
- **Lifestyle factors:** none — **not applicable**.
- **Infectious agents:** none — **not applicable**.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **LoF variant or deletion in _JARID2_** (or, alternatively, a dosage-increasing duplication) **reduces (or raises) functional JARID2 protein** — *demonstrated* (Verberne 2021; Viitasalo 2022).
2. Altered JARID2 dosage **impairs assembly/targeting of the PRC2.2 variant complex** (JARID2–AEBP2–EZH2–SUZ12–EED–RBBP4/7) to CpG-island nucleation sites — *demonstrated in vitro* (Loh & Veenstra 2022, PMID 35997369; Granat 2026, PMID 41650228).
3. This **reduces initiation/spreading of the PRC2 "read-write" H3K27me3 loop** (JARID2 normally mimics H3K27me3 to seed EZH2 methyltransferase activity) — *demonstrated* (Agius 2026, PMID 41785858).
4. Reduced **H3K27me3 at developmental loci (e.g., HOX and lineage-specifying genes) leads to derepression/mis-timing of gene silencing** — *demonstrated in stem-cell/mouse models*; *inferred* for human neurons.
5. Dysregulated Polycomb target expression **disrupts the normal program of neural progenitor proliferation, differentiation, and neuronal maturation** during a critical embryonic/early-postnatal window — *inferred from mouse neurulation phenotype* (Takeuchi 1999).
6. Aberrant neurodevelopment **results in developmental delay, intellectual disability, speech delay, and behavioral abnormalities**, with concurrent craniofacial patterning changes producing the facial gestalt — *clinical correlation*.
   - **Branch A (canonical, PRC2/epigenetic):** steps 2–4 above.
   - **Branch B (non-canonical signaling):** JARID2 dysfunction **attenuates ERK1/2 (MAPK) pathway activation**, shown for the recessive p.Arg300Gln allele in oocytes/zygotes (Sun 2025, PMID 40886009) — *demonstrated for reproductive phenotype; relevance to NDD inferred.*
   - **Branch C (cardiac, developmental):** in mouse, Jarid2 loss **disrupts outflow-tract morphogenesis and trabecular myocyte proliferation** (Takeuchi 1999) — explains congenital heart involvement seen in some deletion patients.

### Detail by category
- **Molecular pathways:** Polycomb/PRC2 H3K27-methylation axis (primary); **MAPK/ERK1/2** signaling (secondary, Sun 2025). Downstream: HOX and developmental transcription-factor networks. Suggested pathway refs: Reactome *PRC2 methylates histones and DNA*; KEGG not specific.
- **Cellular processes:** chromatin-mediated transcriptional repression; cell-fate commitment; neural progenitor **proliferation/differentiation**; (in mouse) cardiomyocyte proliferation. GO: **GO:0006342** chromatin silencing; **GO:0070734** histone H3-K27 methylation; **GO:0021915** neural tube development; **GO:0030182** neuron differentiation; **GO:0045596** negative regulation of cell differentiation.
- **Protein dysfunction:** haploinsufficiency (reduced scaffold for PRC2 recruitment); missense may act via reduced pathway activation without loss of abundance (Sun 2025). No aggregation. Enzymatically dead JmjC (scaffold, not demethylase).
- **Epigenetic changes:** decreased H3K27me3 at targets; a reproducible **blood DNAm episignature** (diagnostic biomarker).
- **Transcriptomics:** RNA-seq shows dysregulated PRC2 target genes (Viitasalo 2022).
- **Immune/metabolic/tissue-damage categories:** **not applicable / not reported.**
- **Cell types (CL):** neural stem/progenitor cell **CL:0000047**; glutamatergic/GABAergic neurons **CL:0000679 / CL:0000617**; cardiomyocyte **CL:0000746** (mouse). JARID2 "is expressed in human neurons" (Verberne 2021).

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** **brain / central nervous system** (nervous system; UBERON:0000955 brain, UBERON:0001016 nervous system). Secondary/variable: **heart** (congenital defects in some deletion cases; UBERON:0000948), craniofacial skeleton (midface; UBERON:0002104/face).
- **Body systems:** nervous system (primary); cardiovascular and craniofacial (secondary/variable).
- **Tissue/cell level:** nervous tissue; neural progenitors and neurons (CL:0000047, CL:0000540); in mouse also neural plate epithelium (UBERON:0005732) and cardiac trabecular myocytes (CL:0000746).
- **Subcellular level:** **nucleus / nucleoplasm / chromatin** (GO:0005634 nucleus; GO:0000785 chromatin) — JARID2 is a chromatin-bound nuclear factor.
- **Localization / lateralization:** CNS involvement is **bilateral/global**; craniofacial features are symmetric/midline (midface).

---

## 8. Temporal Development

- **Onset:** **congenital / early infancy**; developmental concerns typically recognized in infancy–early childhood. Onset pattern **insidious/chronic** (developmental, not acute).
- **Progression:** **static (non-progressive)** neurodevelopmental disorder; disabilities are **lifelong**. No neurodegeneration or disease "staging." Progression rate: not applicable (stable).
- **Course pattern:** stable/chronic; behavioral features may fluctuate but the underlying disorder does not relapse-remit.
- **Remission:** none spontaneous; developmental gains occur with therapy (treatment-responsive functional improvement, not cure).
- **Critical period:** embryonic–early-postnatal neurodevelopment is the mechanistically vulnerable window (PRC2-dependent fate specification); early intervention (therapy/education) is the clinical window of opportunity.

---

## 9. Inheritance and Population

- **Epidemiology:** **ultra-rare**; precise prevalence/incidence **not established** (only a few dozen published individuals worldwide as of 2025). No Orphanet point-prevalence figure.
- **Inheritance:** **autosomal dominant**; most cases **de novo**, but **inheritance from a mildly affected parent is documented** (Verberne 2021 had one inherited case; Cadieux-Dion 2022, PMID 35533077, reported additional transmitted variants from mildly affected parents). A separate **autosomal recessive** reproductive phenotype arises from biallelic missense (Sun 2025).
- **Penetrance:** high but **not strictly complete** — mildly affected transmitting parents indicate **variable/reduced penetrance** in some families; mouse data show **background-dependent penetrance** for structural defects.
- **Expressivity:** **highly variable** (severity of ID, autism/behavior, palatal and cardiac involvement) even within families (PMID 35533077).
- **Genetic anticipation:** **not applicable** (no repeat expansion).
- **Germline mosaicism:** not documented but theoretically possible for recurrence risk — **not reported**.
- **Founder effects / geographic variant clustering:** **none known**.
- **Consanguinity:** relevant only to the **recessive** reproductive phenotype.
- **Carrier frequency:** pathogenic alleles ultra-rare in gnomAD (**effectively not a carrier-screening target**).
- **Sex ratio:** no strong skew reported for the dominant NDD (**data limited**); the recessive reproductive/infertility phenotype is female-specific (maternal-effect gene).
- **Age distribution:** affected from birth; described across pediatric and into adult life.

---

## 10. Diagnostics

**Genetic testing (diagnostic mainstay).**
- **Chromosomal microarray (CMA)** detects 6p22-p24 deletions/duplications (first-line for the CNV presentation; DECIPHER/ClinVar).
- **Exome (WES) / genome (WGS) sequencing** detects intragenic SNVs/indels and is the primary route to single-gene diagnosis; **GeneMatcher** enabled cohort assembly (Verberne 2021).
- **Exon-level copy-number analysis is essential:** intragenic JARID2 CNVs are highly prevalent and may be missed by standard CMA or SNV-only pipelines (Cadieux-Dion 2022, PMID 35533077: *"the high prevalence of intragenic JARID2 copy number variants, emphasizing the importance of exon-level analysis"*).
- **Single-gene / NDD gene-panel** testing including JARID2.
- **Karyotype/FISH** only for large/visible rearrangements; **mtDNA and repeat-expansion testing not indicated.**

**Omics / epigenomic diagnostics.** **DNA-methylation episignature (EpiSign)** is an emerging clinically validated adjunct that can confirm diagnosis and reclassify VUS in chromatinopathies (Koparir 2026, PMID 41957673: *"methylation profiles supported the pathogenicity of several variants previously classified as VUS"*); JARID2 genomic boundaries/episignature refinement reported by van der Laan 2023 (PMID 37762546). **RNA-seq** can demonstrate NMD/altered PRC2-target expression (Viitasalo 2022).

**Clinical tests / imaging.** No specific biomarker or laboratory abnormality. Brain MRI and echocardiography are used to evaluate variable structural anomalies but are **non-diagnostic**. Developmental/neuropsychological assessment quantifies ID/ASD severity.

**Clinical criteria & differential diagnosis.** No formal consensus diagnostic criteria; diagnosis is **molecular**. Differential diagnosis = other syndromic ID/chromatinopathies (e.g., KMT2A/Wiedemann-Steiner, SETD5-related, ANKRD11/KBG, CHD8, EZH2/Weaver) — distinguished by gene-specific variants, facial gestalt, and episignature. Larger 6p22-p24 deletions must be parsed for ATXN1/DTNBP1 contributions.

**Screening.** No newborn or population carrier screening (ultra-rare, de novo). **Cascade testing** of parents for a proband's variant informs recurrence risk.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** the dominant NDD is **not life-limiting** per se; normal or near-normal life expectancy expected absent severe congenital organ defects. No disease-specific mortality data (**not available**).
- **Morbidity/disability:** lifelong intellectual disability, speech/communication impairment, and behavioral comorbidity are the principal morbidities; variable motor and adaptive impairment.
- **Quality of life:** no disease-specific QoL instrument data (**not available**).
- **Complications:** behavioral/psychiatric comorbidity; in individuals with larger deletions, congenital organ anomalies (cardiac) and associated complications.
- **Recovery potential:** developmental gains with early intervention; disability is chronic (no cure).
- **Prognostic factors:** variant type/size (contiguous deletions with additional genes tend to be more severe), presence of structural organ anomalies, baseline cognitive/adaptive function. No validated molecular prognostic biomarker.

---

## 12. Treatment

**No disease-specific or disease-modifying therapy exists.** Management is **symptomatic, supportive, and multidisciplinary**, as for other syndromic NDDs.

- **Pharmacotherapy (symptomatic):** none targeted at JARID2. Standard agents for comorbidities — e.g., stimulants/alpha-agonists for ADHD, SSRIs for anxiety, antiseizure medication if epilepsy present, antipsychotics for severe behavioral dysregulation. **Pharmacogenomics:** no JARID2-specific guidance.
  - NCIT examples: Supportive Care (NCIT:C15277); Symptomatic Treatment (NCIT:C15632).
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **none available / experimental only.** Haploinsufficiency is in principle a target for future dosage-restoring approaches (ASO upregulation, gene therapy), but **no clinical programs exist** for JARID2. PRC2/EZH2 modulators exist in oncology but are **not applicable** therapeutically here.
- **Surgical/interventional:** only for specific congenital anomalies (e.g., cardiac surgery) when present.
- **Supportive & rehabilitative (core management):** early intervention; **physical therapy** (NCIT:C15368), **occupational therapy** (NCIT:C15317), **speech-language therapy** (NCIT:C15312); special education; behavioral therapy (ABA); nutritional support for feeding/hypotonia.
- **Experimental/clinical trials:** **none registered specifically for JARID2-NDD** (ClinicalTrials.gov — none found).
- **Treatment strategy:** individualized, guided by developmental assessment and comorbidity profile; no genotype-guided algorithm established.

---

## 13. Prevention

- **Primary prevention:** not possible (de novo monogenic). **Genetic counseling** is the principal preventive tool.
- **Secondary prevention:** early developmental screening/surveillance enabling early intervention to optimize function.
- **Tertiary prevention:** management of behavioral comorbidity and surveillance for associated anomalies to prevent secondary complications.
- **Reproductive/genetic prevention:** for families with an identified proband variant, **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** are available; low recurrence risk for de novo cases (counsel for possible germline mosaicism). The recessive reproductive phenotype warrants partner carrier consideration in consanguineous families.
- **Immunization / public-health / environmental interventions:** **not applicable.**

---

## 14. Other Species / Natural Disease

- **Taxonomy:** gene conserved across vertebrates — *Homo sapiens* (NCBI:txid9606); *Mus musculus* (NCBI:txid10090); *Danio rerio* (NCBI:txid7955); *Drosophila melanogaster* (NCBI:txid7227, ortholog *jumonji/Jarid2/dJmj*).
- **Orthologous genes:** mouse **Jarid2** (NCBI Gene 16468; historical name *jmj*); zebrafish **jarid2a/jarid2b**; *Drosophila* **Jarid2/dJmj**.
- **Natural disease in other species:** **no naturally occurring JARID2 disease reported** in companion animals/wildlife (OMIA — none recorded). Phenotypes are experimentally induced.
- **Comparative biology:** the PRC2/H3K27me3 regulatory mechanism is **deeply evolutionarily conserved**; mouse jumonji mutants model the developmental requirement (neurulation, cardiogenesis). *Drosophila* dJmj has partly PRC2-independent roles (Suong 2018, PMID 29102770), indicating some species divergence in function.
- **Transmission / zoonosis:** **not applicable** (genetic disorder).

---

## 15. Model Organisms

- **Mouse (primary model):** gene-trap/knockout **jumonji (jmj/Jarid2)** mice show fully penetrant **neural tube defects and cardiac outflow-tract/trabecular abnormalities** on a C3H/HeJ background, with **strain-dependent penetrance** (Takeuchi 1999, PMID 10446263: *"the jmj gene plays essential roles in the normal development of the neural plate, morphogenesis of bulbus cordis, and proliferation of trabecular myocytes"*). Available model types: constitutive knockout, gene-trap, conditional alleles (MGI). Homozygous null is embryonic/perinatal lethal, so conditional/heterozygous models better mimic human haploinsufficiency.
- **In-vitro / cellular:** **mouse embryonic stem cells (ESCs)** are the workhorse for PRC2.2/JARID2 recruitment and H3K27me3 studies (Loh & Veenstra 2022; Granat 2026; Agius 2026). Reconstituted PRC2 biochemistry defines JARID2's H3K27me3-mimic function. Mouse zygote mRNA-microinjection models the recessive p.Arg300Gln allele (Sun 2025).
- **Invertebrate:** *Drosophila* dJmj (Suong 2018) for stem-cell/differentiation roles (partly PRC2-independent).
- **Phenotype recapitulation:** mouse captures the **developmental CNS and cardiac requirement** and the PRC2/H3K27me3 mechanism well; it does **not** directly model human cognition/behavior or the adult neurodevelopmental phenotype. iPSC-derived neurons/organoids from patients are a logical but **not-yet-prominently-published** resource (**gap**).
- **Resources:** MGI (mouse), ZFIN (zebrafish), FlyBase (Drosophila), IMPC/IMSR for alleles.

---

## Evidence Summary (key PMIDs)

| PMID | Type | Contribution |
|---|---|---|
| 33077894 (Verberne 2021) | Human clinical cohort (n=16) | Establishes JARID2 haploinsufficiency as a distinct NDD; gene–disease validity |
| 35533077 (Cadieux-Dion 2022) | Human clinical (n=7/5 families) | Confirms gene–disease assoc.; adds palatal/cardiac anomalies; variable expressivity; intragenic CNVs |
| 23294540 (Barøy 2013) | Human clinical (6p22.3 deletions) | Defines facial gestalt; implicates JARID2 + ATXN1 |
| 35979655 (Viitasalo 2022) | Human case + RNA-seq | Duplication (gain) also pathogenic; PRC2-target dysregulation |
| 40886009 (Sun 2025) | Human + mouse zygote | Recessive missense; ERK1/2 + H3K27me3 link; maternal-effect |
| 10446263 (Takeuchi 1999) | Mouse model | Neural-tube + cardiac developmental requirement |
| 35997369 (Loh 2022) | Review/in vitro | JARID2 recruits PRC2 (PRC2.2) in ESCs |
| 41785858 (Agius 2026) | Mouse/in vitro | JARID2 mimics H3K27me3 to seed PRC2 read-write loop |
| 41650228 (Granat 2026) | In vitro | MTF2/JARID2 direct PRC2 to chromatin; H3K27me3 deposition |
| 41957673 (Koparir 2026) | Human diagnostic | Episignature/EpiSign for chromatinopathy VUS resolution |
| 37762546 (van der Laan 2023) | Human diagnostic | Refines JARID2 genomic boundaries/episignature |

---

## Limitations and Future Directions

- The disorder is **newly defined with only a few dozen reported individuals**; frequencies, prevalence, sex ratio, penetrance, and prognosis are **preliminary** and from small cohorts.
- **Phenotype frequencies are qualitative**; no large natural-history study exists.
- Human **neuronal/organoid models and a fully validated JARID2 episignature classifier** are still maturing.
- The relationship between **dosage loss vs gain**, and the **ERK1/2 branch**, needs mechanistic clarification in neural tissue.
- **No disease-specific therapy**; dosage-restoration strategies are hypothetical.

---

### Ontology term appendix (suggested)
- **Disease:** MONDO:0859306
- **Gene/protein:** HGNC:6826 (JARID2); UniProt Q92833
- **GO BP:** GO:0070734 (histone H3-K27 methylation), GO:0006342 (chromatin silencing), GO:0021915 (neural tube development), GO:0030182 (neuron differentiation), GO:0045596 (neg. reg. of cell differentiation)
- **GO CC:** GO:0005634 (nucleus), GO:0000785 (chromatin), GO:0035098 (ESC/ATAC-type complex context: PRC2 complex GO:0035098)
- **CL:** CL:0000047 (neural stem cell), CL:0000540 (neuron), CL:0000746 (cardiomyocyte)
- **UBERON:** UBERON:0000955 (brain), UBERON:0001016 (nervous system), UBERON:0000948 (heart), UBERON:0005732 (neural plate)
- **HPO:** HP:0001263, HP:0001249, HP:0000750, HP:0001252, HP:0000708, HP:0000729, HP:0000336, HP:0000490, HP:0011800
- **NCIT (interventions):** NCIT:C15368 (physical therapy), NCIT:C15317 (occupational therapy), NCIT:C15312 (speech therapy), NCIT:C15277 (supportive care)


## Artifacts

- [OpenScientist final report](JARID2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](JARID2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 4 |
| Terms whose name was checked | 29 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (2 mentions) - the report calls it "high (most)"; HP calls it **Intellectual disability**
- `HP:0000750` (2 mentions) - the report calls it "common"; HP calls it **Delayed speech and language development**
- `HP:0001252` (2 mentions) - the report calls it "common"; HP calls it **Hypotonia**
- `HP:0000729` (3 mentions) - the report calls it "subset"; HP calls it **Autistic behavior**
- `HP:0000336` (2 mentions) - the report calls it "characteristic"; HP calls it **Prominent supraorbital ridges**
- `HP:0000490` (2 mentions) - the report calls it "characteristic"; HP calls it **Deeply set eye**
- `HP:0000652` (1 mention) - the report calls it "periorbital"; HP calls it **Lower eyelid coloboma**
- `HP:0011800` (2 mentions) - the report calls it "characteristic"; HP calls it **Midface retrusion**
- `HP:0001999` (1 mention) - the report calls it "characteristic"; HP calls it **Abnormal facial shape**
- `HP:0000174` (1 mention) - the report calls it "subset"; HP calls it **Abnormal palate morphology**
- `HP:0001627` (1 mention) - the report calls it "subset"; HP calls it **Abnormal heart morphology**
- `GO:0006342` (2 mentions) - the report calls it "chromatin silencing"; GO calls it **GO_0006342**
- `UBERON:0005732` (2 mentions) - the report calls it "neural plate"; UBERON calls it **paired limb/fin field**
- `NCIT:C15277` (2 mentions) - the report calls it "NCIT examples: Supportive Care", "supportive care"; NCIT calls it **Mastectomy**
- `NCIT:C15317` (2 mentions) - the report calls it "occupational therapy"; NCIT calls it **Second-Look Surgery**
- `NCIT:C15312` (2 mentions) - the report calls it "speech-language therapy", "speech therapy"; NCIT calls it **Radiation Dosimetry**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006342` (GO_0006342) (2 mentions) - replaced by `GO:0031507`
- `GO:0070734` (obsolete histone H3-K27 methylation) (2 mentions)
- `NCIT:C15368` (Treatment) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0045596` (2 mentions) - the report calls it "neg. reg. of cell differentiation"; GO calls it **negative regulation of cell differentiation**
- `CL:0000746` (3 mentions) - the report calls it "cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `NCIT:C15368` (2 mentions) - the report calls it "physical therapy"; NCIT calls it **Treatment**, and lists "Therapy" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15277` - called "NCIT examples: Supportive Care", "supportive care"
- `NCIT:C15312` - called "speech-language therapy", "speech therapy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`.