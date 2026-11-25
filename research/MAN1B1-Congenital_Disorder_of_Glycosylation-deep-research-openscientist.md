---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T23:11:56.291154'
end_time: '2026-11-12T23:25:11.172260'
duration_seconds: 794.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MAN1B1-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0018349
  category: Mendelian
  causal_genes: MAN1B1
  omim_id: not recorded
  synonyms: MAN1B1-CDG; carbohydrate deficient glycoprotein syndrome type II due to
    MAN1B1 deficiency; congenital disorder of glycosylation type 2 due to MAN1B1 deficiency;
    congenital disorder of glycosylation type II due to MAN1B1 deficiency; intellectual
    disability-truncal obesity syndrome
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: baab8c03-aa7e-4422-bbdb-9c651e51e030
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 13
  off_topic: 1
  off_topic_references:
  - PMID:27856750
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 23
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 1
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0001249
    reported_labels:
    - Near-universal
    ontology_label: Intellectual disability
  - term_id: HP:0001263
    reported_labels:
    - Near-universal
    ontology_label: Global developmental delay
  - term_id: HP:0001999
    reported_labels:
    - Near-universal
    ontology_label: Abnormal facial shape
  - term_id: HP:0001252
    reported_labels:
    - Frequent
    ontology_label: Hypotonia
  - term_id: HP:0000750
    reported_labels:
    - Frequent
    ontology_label: Delayed speech and language development
  - term_id: HP:0000708
    reported_labels:
    - Frequent
    ontology_label: Atypical behavior
  - term_id: HP:0001956
    reported_labels:
    - Variable / least consistent
    ontology_label: Truncal obesity
  - term_id: HP:0001250
    reported_labels:
    - Subset
    ontology_label: Seizure
  - term_id: HP:0002910
    reported_labels:
    - Subset
    ontology_label: Elevated circulating hepatic transaminase concentration
  - term_id: HP:0000028
    reported_labels:
    - Subset
    ontology_label: Cryptorchidism
  - term_id: HP:0011968
    reported_labels:
    - Subset
    ontology_label: Feeding difficulties
  - term_id: HP:0002267
    reported_labels:
    - Rare/novel
    ontology_label: Exaggerated startle response
  - term_id: UBERON:0002107
    reported_labels:
    - Secondary involvement:** liver
    ontology_label: liver
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0030433
    ontology_label: obsolete ubiquitin-dependent ERAD pathway
    replaced_by: GO:0036503
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MAN1B1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MAN1B1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MAN1B1-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0018349 (if available)
- **Causal gene(s):** MAN1B1
- **OMIM:** not recorded
- **Synonyms:** MAN1B1-CDG; carbohydrate deficient glycoprotein syndrome type II due to MAN1B1 deficiency; congenital disorder of glycosylation type 2 due to MAN1B1 deficiency; congenital disorder of glycosylation type II due to MAN1B1 deficiency; intellectual disability-truncal obesity syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MAN1B1-Congenital Disorder of Glycosylation** covering all of the
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

# MAN1B1-Congenital Disorder of Glycosylation (Rafiq Syndrome): Comprehensive Disease Report

**Disease:** MAN1B1-Congenital Disorder of Glycosylation (MAN1B1-CDG; Rafiq syndrome, RAFQS)
**MONDO ID:** MONDO:0018349
**Causal gene:** **MAN1B1** (mannosidase alpha class 1B member 1), chromosome 9q34.3
**Category:** Mendelian, autosomal recessive

---

## Summary

MAN1B1-Congenital Disorder of Glycosylation is a rare, autosomal-recessive, Golgi-type (type II) congenital disorder of glycosylation caused by **biallelic loss-of-function variants in the MAN1B1 gene** on chromosome 9q34.3. MAN1B1 encodes a glycoside-hydrolase family 47 (GH47) α-1,2-mannosidase that trims terminal α1,2-linked mannose residues from N-linked glycans and participates in endoplasmic reticulum (ER)/Golgi glycoprotein quality control. Loss of MAN1B1 function impairs N-glycan maturation, disrupts Golgi morphology, and produces a characteristic serum transferrin hybrid-type N-glycan "CDG-II" signature that is diagnostically useful. The disorder was first described clinically in 2010 and linked to MAN1B1 in 2011 by Rafiq and colleagues, giving rise to the eponym **Rafiq syndrome**.

Clinically, MAN1B1-CDG is dominated by a neurodevelopmental core: near-universal **intellectual disability/developmental delay** and **distinctive facial dysmorphism**, accompanied by **muscular hypotonia**, speech delay or absent speech, and behavioral problems (impulsivity, aggression). **Truncal obesity** — once highlighted in the alternative name "intellectual disability–truncal obesity syndrome" — is in fact one of the *least consistent* features across the ~45 patients reported worldwide. Additional, more variable features include epilepsy, cryptorchidism, feeding difficulties, hyperekplexia, and hypertransaminasemia (elevated liver transaminases). A recurrent missense allele, **c.1000C>T (p.Arg334Cys)**, appears repeatedly across unrelated populations.

No disease-modifying therapy exists. Management is entirely supportive and symptomatic, centered on developmental and behavioral support, monitoring of liver transaminases, and management of individual complications such as epilepsy. A pharmacologic "translational balancing" trial with disulfiram failed to alter glycosylation, reinforcing the absence of established targeted treatment. Despite the small absolute number of patients, MAN1B1-CDG is one of the more frequently encountered CDG-II subtypes in diagnostic cohorts — second only to PMM2 in some recent referral series — making accurate recognition of its biochemical and clinical signature clinically valuable.

---

## Key Findings

### Finding 1 — MAN1B1-CDG (Rafiq syndrome) is an autosomal-recessive CDG type II caused by biallelic MAN1B1 mutations

Exome sequencing identified **MAN1B1** as the causal gene in a previously unsolved CDG-II patient, and six additional cases were subsequently confirmed; all presented with slight facial dysmorphism, psychomotor retardation, and truncal obesity ([PMID: 24348268](https://pubmed.ncbi.nlm.nih.gov/24348268/)). As the authors wrote: *"exome sequencing was used to identify MAN1B1 as the culprit gene in an unsolved CDG-II patient. Subsequently, 6 additional cases with MAN1B1-CDG were found. All individuals presented slight facial dysmorphism, psychomotor retardation and truncal obesity."*

The disorder was first described clinically in 2010 and genetically linked to MAN1B1 in 2011, and is now classified as **Rafiq syndrome (RAFQS)**, an autosomal-recessive CDG-II. A 2025 review of 44 cases confirmed the synonymy and inheritance pattern: *"Rafiq syndrome, MAN1B1-CDG, was described in 2010 and associated with genetic mutation in MAN1B1 gene in 2011. The disorder follows an autosomal recessive pattern of inheritance and typically presents with specific facial dysmorphism, intellectual disability, developmental delay, obesity, and hypotonia"* ([PMID: 39840888](https://pubmed.ncbi.nlm.nih.gov/39840888/)). *(Evidence source: human clinical / exome sequencing.)*

### Finding 2 — MAN1B1 encodes a Golgi-localized α-1,2-mannosidase; deficiency disrupts Golgi morphology and glycoprotein quality control

MAN1B1 was historically regarded as an ER-resident α-1,2-mannosidase initiating ER-associated degradation (ERAD). However, the index CDG study demonstrated that **endogenous MAN1B1 localizes to the Golgi complex**, and that patient cells show markedly abnormal Golgi architecture: *"We were able to confirm that MAN1B1 is indeed localized to the Golgi complex instead of the ER. Furthermore, we observed an altered Golgi morphology in all patients' cells, with marked dilatation and fragmentation"* ([PMID: 24348268](https://pubmed.ncbi.nlm.nih.gov/24348268/)).

Beyond its catalytic activity, MAN1B1 plays a **non-enzymatic "gatekeeper" role** in protein biosynthetic quality control. A conserved, vertebrate-specific non-enzymatic decapeptide in the luminal stem domain governs the fate of misfolded ERAD substrates: *"a highly conserved, vertebrate-specific non-enzymatic decapeptide sequence in the luminal stem domain plays a significant role in controlling the fate of overexpressed Null Hong Kong"* ([PMID: 24627495](https://pubmed.ncbi.nlm.nih.gov/24627495/)). Mechanistically, MAN1B1 belongs to the **GH47 family**, which trims terminal α1,2-linked mannose residues during N-glycan maturation in the secretory pathway, producing the uniquely trimmed oligomannose isomers required for glycoprotein quality control and glycan maturation ([PMID: 27856750](https://pubmed.ncbi.nlm.nih.gov/27856750/)). *(Evidence source: in vitro / cell biology / structural enzymology.)*

### Finding 3 — MAN1B1-CDG produces a characteristic CDG-II serum transferrin glycoprofile with hybrid-type N-glycans, enabling diagnosis

High-resolution mass spectrometry of intact plasma transferrin reveals a highly characteristic glycosylation signature consisting of **hybrid-type N-glycans**, consistent with deficient mannosidase activity. Screening a cohort of 100 CDG-II patients with this method identified 11 additional MAN1B1-CDG cases, all confirmed by Sanger sequencing: *"A highly characteristic glycosylation signature was observed with hybrid type N-glycans, in agreement with deficient mannosidase activity. The speed and robustness of the method allowed subsequent screening in a cohort of 100 patients with congenital disorder of glycosylation type II, which revealed the characteristic glycosylation profile of MAN1B1-congenital disorder of glycosylation in 11 additional patients"* ([PMID: 24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/)).

In routine practice, serum transferrin isoelectric focusing shows a **type 2 CDG pattern**, and MALDI-TOF mass spectrometry of transferrin glycans aids diagnosis because the defective glycans accumulate only at trace levels ([PMID: 34141584](https://pubmed.ncbi.nlm.nih.gov/34141584/)). A case series confirmed both the biochemical pattern and an associated laboratory abnormality: *"All patients had presented due to dysmorphic and neurological findings and hypertransaminasemia was remarkable. A type 2 pattern was found on serum transferrin isoelectrofocusing analysis"* ([PMID: 34162022](https://pubmed.ncbi.nlm.nih.gov/34162022/)). *(Evidence source: human clinical / mass spectrometry diagnostics.)*

### Finding 4 — Variant spectrum: biallelic loss-of-function with a recurrent p.Arg334Cys allele at locus 9q34.3

MAN1B1 maps to **chromosome 9q34.3** (the MRT15 intellectual-disability locus). The original gene-discovery study identified multiple loss-of-function variants (RefSeq NM_016219), including a nonsense variant **c.1418G>A (p.Trp473\*)** segregating with intellectual disability in a Pakistani family, and demonstrated that disease-associated missense variants act through loss of function: *"we have identified mutations in the gene MAN1B1, encoding a mannosyl oligosaccharide, alpha 1,2-mannosidase. In one Pakistani family, MR43, a homozygous nonsense mutation (RefSeq number NM_016219.3: c.1418G>A [p.Trp473\*]), segregated with intellectual disability"* ([PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/)).

The recurrent missense allele **c.1000C>T (p.Arg334Cys)** has been reported repeatedly across unrelated populations and is functionally damaging: it either *"reduce[s] k(cat) by ∼1300-fold or disrupt[s] stable protein expression in mammalian cells"* ([PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/)). The expanding allelic spectrum now includes:

| Variant (NM_016219) | Protein | Type | Population / note | Reference |
|---|---|---|---|---|
| c.1000C>T | p.Arg334Cys | Missense (recurrent) | Multiple populations; ~1300-fold ↓ kcat | [PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/), [PMID: 39896699](https://pubmed.ncbi.nlm.nih.gov/39896699/), [PMID: 36142510](https://pubmed.ncbi.nlm.nih.gov/36142510/) |
| c.1418G>A | p.Trp473* | Nonsense | Pakistani family MR43 | [PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/) |
| c.1189G>A | p.Glu397Lys | Missense (founder) | Village founder allele | [PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/) |
| c.1118C>G | p.Pro373Arg | Missense | Saudi | [PMID: 41246981](https://pubmed.ncbi.nlm.nih.gov/41246981/) |
| c.1976T>G | p.Phe659Cys | Missense | Palestinian | [PMID: 39840888](https://pubmed.ncbi.nlm.nih.gov/39840888/) |
| c.2011C>T + 23-bp deletion | — | Compound het (nonsense + del) | Chinese | [PMID: 41393301](https://pubmed.ncbi.nlm.nih.gov/41393301/) |
| c.1065+1G>C | — | Splice-site | Russian (compound het with p.Arg334Cys) | [PMID: 36142510](https://pubmed.ncbi.nlm.nih.gov/36142510/) |

Both recurrent missense residues are conserved across the animal kingdom, and MAN1B1 has been cited as one of the few non-syndromic autosomal-recessive intellectual-disability (NS-ARID) genes with an elevated mutation frequency across populations. *(Evidence source: human genetics / in vitro functional assays.)*

### Finding 5 — Clinical phenotype: neurodevelopmental core with variable truncal obesity; no disease-modifying therapy

Across the ~45 reported patients, the most frequent features are **intellectual disability / developmental delay** and **distinctive facial dysmorphism** (near-universal), while **truncal obesity is among the least consistent** features — a notable correction to the older syndrome name. The 44-case review stated plainly: *"the 2 most frequent features among them are intellectual disability and facial dysmorphism, whereas the least frequent one is truncal obesity"* ([PMID: 39840888](https://pubmed.ncbi.nlm.nih.gov/39840888/)).

Additional recurrent features include muscular hypotonia, speech delay/absent speech, behavioral problems (impulsivity, aggression), and in subsets epilepsy, cryptorchidism, feeding difficulties, hyperekplexia, and hypertransaminasemia ([PMID: 24348268](https://pubmed.ncbi.nlm.nih.gov/24348268/); [PMID: 39896699](https://pubmed.ncbi.nlm.nih.gov/39896699/); [PMID: 34162022](https://pubmed.ncbi.nlm.nih.gov/34162022/)). Novel phenotypic expansions reported include persistent hyperekplexia and feeding difficulty ([PMID: 39896699](https://pubmed.ncbi.nlm.nih.gov/39896699/)) and co-occurring thyroid dyshormonogenesis in a case with a second-gene (DUOX2) variant ([PMID: 41393301](https://pubmed.ncbi.nlm.nih.gov/41393301/)).

No targeted therapy exists. A trial of **disulfiram**, based on a translational-balancing hypothesis, left glycosylation unaltered — i.e., no biochemical benefit: *"Unaltered glycosylation during disulfiram treatment in mannosyl-oligosaccharide alpha-1,2-mannnosidase-congenital disorders of glycosylation (MAN1B1-CDG)"* ([PMID: 34258140](https://pubmed.ncbi.nlm.nih.gov/34258140/)). Management therefore remains supportive and symptomatic. *(Evidence source: human clinical / interventional trial.)*

### Finding 6 — MAN1B1-CDG is one of the more frequently encountered CDG type II subtypes among diagnostic referrals

Although rare in absolute terms, MAN1B1-CDG is relatively common within CDG-II diagnostic populations. In the index diagnostic screen, 12 of 100 CDG-II patients (the index case plus 11 identified by transferrin glycoprofiling) carried MAN1B1 mutations ([PMID: 24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/)). In a 2022–2025 retrospective of biochemical genetic testing performed after equivocal molecular results, MAN1B1 was the **second most frequently implicated CDG gene after PMM2**: *"Molecular findings were reported for 52 different genes, of which PMM2 (n = 13), MAN1B1 (n = 6), and ALG13 (n = 6) were the most frequent"* ([PMID: 41905312](https://pubmed.ncbi.nlm.nih.gov/41905312/)). Despite this relative frequency, the absolute number of reported patients remains small (~45 worldwide as of 2025). *(Evidence source: human clinical / diagnostic cohorts.)*

---

## Section-by-Section Report

### 1. Disease Information

MAN1B1-CDG (Rafiq syndrome) is a rare autosomal-recessive inborn error of metabolism belonging to the **congenital disorders of glycosylation, type II (CDG-II)** — disorders characterized by defective processing of protein-bound N-glycans in the ER/Golgi. The disease arises from deficiency of the GH47 α-1,2-mannosidase encoded by MAN1B1, impairing N-glycan maturation and glycoprotein quality control.

**Key identifiers:**
- **MONDO:** MONDO:0018349
- **Gene (HGNC):** MAN1B1
- **Locus:** 9q34.3
- **Synonyms:** MAN1B1-CDG; Rafiq syndrome (RAFQS); carbohydrate-deficient glycoprotein syndrome type II due to MAN1B1 deficiency; congenital disorder of glycosylation type 2/II due to MAN1B1 deficiency; intellectual disability–truncal obesity syndrome.

Information is derived from **aggregated disease-level resources and published case reports/series** (OMIM, Orphanet, primary literature), not from individual EHR records. The evidence base is a small, globally distributed set of ~45 reported patients.

### 2. Etiology

**Primary cause — genetic.** The disease is monogenic: biallelic (homozygous or compound heterozygous) **loss-of-function variants in MAN1B1** cause the disorder ([PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/)). There are no established environmental or infectious causes.

**Genetic risk factors.** The sole causal factor is biallelic MAN1B1 pathogenic variation. **Consanguinity** is a strong contributor — many reported families are consanguineous (e.g., Pakistani, Saudi, Palestinian, and other populations), consistent with autosomal-recessive inheritance and homozygous founder/recurrent alleles.

**Environmental risk / protective / gene–environment factors.** No environmental risk factors, protective factors, or gene–environment interactions have been established for this Mendelian disorder. The only "protective" consideration is at the population-genetics level — avoidance of consanguineous unions reduces recessive-disease risk generally.

### 3. Phenotypes

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Intellectual disability | Cognitive/behavioral | Near-universal | HP:0001249 |
| Global developmental delay | Developmental | Near-universal | HP:0001263 |
| Distinctive facial dysmorphism | Physical | Near-universal | HP:0001999 |
| Muscular hypotonia | Clinical sign | Frequent | HP:0001252 |
| Speech delay / absent speech | Developmental | Frequent | HP:0000750 |
| Behavioral problems (impulsivity, aggression) | Behavioral | Frequent | HP:0000708 |
| Truncal obesity | Physical | Variable / least consistent | HP:0001956 |
| Epilepsy / seizures | Neurological | Subset | HP:0001250 |
| Hypertransaminasemia | Laboratory abnormality | Subset | HP:0002910 |
| Cryptorchidism | Physical | Subset | HP:0000028 |
| Feeding difficulties | Clinical sign | Subset | HP:0011968 |
| Hyperekplexia (exaggerated startle) | Neurological | Rare/novel | HP:0002267 |

**Characteristics.** Onset is **congenital/neonatal to early childhood** (hypotonia, developmental delay recognized in infancy). Severity is **variable**, dominated by stable (non-degenerative) intellectual disability. The course is generally **static/non-progressive** neurologically, though behavioral issues and obesity may evolve. Frequency data derive from the 44-case review ([PMID: 39840888](https://pubmed.ncbi.nlm.nih.gov/39840888/)), which ranked intellectual disability and facial dysmorphism as most frequent and truncal obesity as least frequent.

**Quality of life.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder. Impact is driven by lifelong intellectual disability, communication limitations, and behavioral challenges, all of which substantially affect daily functioning and caregiver burden.

### 4. Genetic / Molecular Information

**Causal gene:** MAN1B1 (mannosidase alpha class 1B member 1), 9q34.3; RefSeq NM_016219. Encodes a GH47-family α-1,2-mannosidase.

**Pathogenic variants.** Reported variants are predominantly **loss-of-function missense, nonsense, splice-site, and small deletion** alleles (see table under Finding 4). The recurrent **c.1000C>T (p.Arg334Cys)** reduces catalytic rate ~1300-fold or abolishes stable protein expression ([PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/)). Variant classification follows ACMG/AMP; truncating variants are pathogenic, and recurrent missense alleles are supported by functional data. Population allele frequencies (gnomAD) are low, consistent with rarity; MAN1B1 is nonetheless noted as having elevated mutation frequency among NS-ARID genes.

**Functional consequence:** loss of function (reduced/abolished mannosidase activity and/or loss of the non-enzymatic gatekeeper function). **Somatic vs germline:** germline. **Modifier genes / epigenetics / chromosomal abnormalities:** none established specific to MAN1B1-CDG. (One Chinese case carried a coexisting DUOX2 variant causing independent thyroid dyshormonogenesis — a second disease rather than a modifier; [PMID: 41393301](https://pubmed.ncbi.nlm.nih.gov/41393301/).)

**Gene/GO annotations:** molecular function GO:0004571 (mannosyl-oligosaccharide 1,2-α-mannosidase activity); process GO:0006491 (N-glycan processing); GO:0036508 (protein α-1,2-demannosylation).

### 5. Environmental Information

Not applicable. No environmental factors, lifestyle factors, or infectious agents are implicated in this monogenic recessive disorder. Consanguinity (a demographic/social factor) increases the probability of homozygous affected offspring but is not an environmental disease cause per se.

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in MAN1B1** (e.g., p.Arg334Cys, p.Trp473*) **result in** loss of GH47 α-1,2-mannosidase activity and/or loss of stable MAN1B1 protein. *(Demonstrated — functional assays, [PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/).)*
2. Loss of MAN1B1 **leads to** failure to trim terminal α1,2-linked mannose residues during N-glycan maturation in the Golgi/ER. *(Demonstrated — enzymology, [PMID: 27856750](https://pubmed.ncbi.nlm.nih.gov/27856750/).)*
3. Impaired mannose trimming **results in** accumulation of aberrant **hybrid-type N-glycans** on secreted glycoproteins (e.g., serum transferrin). *(Demonstrated — mass spectrometry, [PMID: 24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/).)*
4. In parallel, loss of the **non-enzymatic gatekeeper decapeptide function leads to** defective ERAD substrate retention/retrieval and disturbed glycoprotein quality control. *(Demonstrated in overexpression models — [PMID: 24627495](https://pubmed.ncbi.nlm.nih.gov/24627495/).)*
5. These defects **lead to** altered Golgi morphology — marked dilatation and fragmentation — in patient cells. *(Demonstrated — [PMID: 24348268](https://pubmed.ncbi.nlm.nih.gov/24348268/).)*
6. Global hypoglycosylation/aberrant glycosylation of many client proteins **is inferred to** disrupt neuronal development and function. *(Inferred — mechanism linking glycosylation defect to neurodevelopment not directly demonstrated.)*
7. This **results in** the clinical phenotype: intellectual disability, developmental delay, facial dysmorphism, hypotonia, behavioral problems, and variable truncal obesity; a branch to the **liver** produces hypertransaminasemia. *(Observed clinically.)*

**Detail by category:**
- **Molecular pathway:** N-linked glycan biosynthesis/maturation in the secretory pathway (KEGG "N-Glycan biosynthesis"; Reactome "Asparagine N-linked glycosylation"). GH47 mannosidases produce trimmed oligomannose isomers needed for quality control.
- **Cellular processes:** ER-associated degradation (ERAD), glycoprotein quality control, Golgi-based glycan processing. GO:0030433 (ubiquitin-dependent ERAD pathway), GO:0006491.
- **Protein dysfunction:** loss of catalytic activity (missense reducing kcat ~1300-fold) and/or loss of stable protein expression; also loss of a non-enzymatic chaperone-like gatekeeper function.
- **Subcellular compartments:** Golgi apparatus (GO:0005794) — primary site of endogenous MAN1B1; ER (GO:0005789) involvement via ERAD.
- **Biochemical abnormality:** mannosyl-oligosaccharide α-1,2-mannosidase deficiency; accumulation of hybrid-type N-glycans.
- **Molecular profiling:** diagnostic transferrin glycoprofile (hybrid-type N-glycans). Albumin, newly recognized as N-glycosylated, also shows site-specific alterations in MAN1B1-CDG, a potential diagnostic biomarker ([PMID: 41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/)).

**Suggested terms:** GO:0004571, GO:0006491, GO:0030433; cell types affected are broad (neurons CL:0000540, hepatocytes CL:0000182) given multisystem glycoprotein involvement.

### 7. Anatomical Structures Affected

- **Primary organ/system:** central nervous system (brain; UBERON:0000955) — intellectual disability, developmental delay, hypotonia, behavioral problems.
- **Secondary involvement:** liver (UBERON:0002107) — hypertransaminasemia; adipose/metabolic (truncal obesity); craniofacial structures (dysmorphism); gonads (cryptorchidism).
- **Body systems:** nervous, hepatic/digestive, endocrine/metabolic, musculoskeletal (hypotonia).
- **Tissue/cell level:** broadly affected secretory-pathway–dependent cells; neurons and hepatocytes clinically prominent.
- **Subcellular:** **Golgi apparatus** (GO:0005794) is the key compartment (dilatation and fragmentation in patient cells); ER (GO:0005789) via ERAD.
- **Localization/lateralization:** systemic and bilateral/symmetric (a metabolic disorder, not a focal lesion).

### 8. Temporal Development

- **Onset:** congenital/neonatal to early childhood; typically recognized in infancy via hypotonia and developmental delay.
- **Onset pattern:** chronic/insidious.
- **Progression:** neurologically **static/stable** (non-degenerative) intellectual disability; this contrasts with some other CDGs (e.g., PMM2-CDG with progressive cerebellar atrophy). Behavioral features and obesity may fluctuate or evolve.
- **Duration:** chronic, lifelong.
- **Remission:** none (no spontaneous or treatment-induced remission).
- **Critical periods:** early developmental window relevant for supportive/rehabilitative intervention, though no disease-modifying therapy exists.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive ([PMID: 39840888](https://pubmed.ncbi.nlm.nih.gov/39840888/)).
- **Penetrance:** complete (biallelic LoF produces disease); **expressivity:** variable (notably for truncal obesity and seizures).
- **Epidemiology:** no formal prevalence/incidence figures; ~45 patients reported worldwide as of 2025 (ultra-rare). Relatively common *within* CDG-II diagnostic cohorts — 12/100 in the index screen ([PMID: 24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/)) and the second most frequent CDG gene (n=6) after PMM2 (n=13) in a recent referral series ([PMID: 41905312](https://pubmed.ncbi.nlm.nih.gov/41905312/)).
- **Founder effects/consanguinity:** recurrent/founder alleles (e.g., p.Glu397Lys village founder; recurrent p.Arg334Cys) reported; consanguinity frequent in affected families.
- **Populations:** reported across Pakistani, Saudi, Palestinian, Russian, Chinese, Korean, Portuguese, Turkish, and other populations — broad geographic distribution.
- **Sex ratio / age distribution:** no established sex bias (autosomal); affected individuals span pediatric through adult ages.
- **Carrier frequency / anticipation / mosaicism:** no specific data; anticipation not expected (not a repeat-expansion disorder).

### 10. Diagnostics

- **Screening biochemistry:** serum transferrin isoelectric focusing shows a **CDG type 2 pattern** ([PMID: 34162022](https://pubmed.ncbi.nlm.nih.gov/34162022/)).
- **Confirmatory glycomics:** intact-transferrin high-resolution MS and MALDI-TOF MS of transferrin N-glycans reveal the characteristic **hybrid-type N-glycan** signature ([PMID: 24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/); [PMID: 34141584](https://pubmed.ncbi.nlm.nih.gov/34141584/)). Because defective glycans accumulate only at trace levels, a tiered decision tree (exome → gel electrophoresis → MS) improves diagnostic yield.
- **Emerging biomarker:** site-specific N-glycosylation changes in **albumin** ([PMID: 41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/)).
- **Laboratory clue:** hypertransaminasemia is a recurrent, supportive finding.
- **Genetic testing (definitive):** whole-exome sequencing has been the principal route to diagnosis (many cases are biochemically subtle); targeted/single-gene MAN1B1 sequencing and hereditary-metabolic gene panels also used. Chromosomal microarray/karyotype are not primary tools.
- **Differential diagnosis:** other CDG-II subtypes and non-specific syndromic intellectual disability; the hybrid-type glycan signature distinguishes MAN1B1-CDG. Caution: transferrin protein variants at glycosylation sites can mimic CDG patterns ([PMID: 21431619](https://pubmed.ncbi.nlm.nih.gov/21431619/)).

### 11. Outcome / Prognosis

- **Survival/life expectancy:** no evidence of markedly reduced lifespan; the disorder is chronic and non-neurodegenerative, so prognosis is driven by the fixed intellectual disability and manageable complications rather than mortality. No formal survival data.
- **Morbidity/disability:** substantial lifelong disability from intellectual disability, communication limitation, and behavioral problems; obesity and epilepsy add morbidity in subsets.
- **Complications:** epilepsy, hypertransaminasemia/liver involvement, feeding difficulties, behavioral crises.
- **Prognostic factors:** severity of intellectual disability and presence of epilepsy/behavioral problems; no validated molecular prognostic biomarkers. Genotype–phenotype correlation is limited given the small cohort.

### 12. Treatment

- **No disease-modifying therapy exists.** A **disulfiram** trial based on a translational-balancing hypothesis did not alter glycosylation ([PMID: 34258140](https://pubmed.ncbi.nlm.nih.gov/34258140/)).
- **Supportive/symptomatic management (standard of care):** early developmental intervention; physical, occupational, and speech therapy (NCIT rehabilitation interventions); behavioral support for impulsivity/aggression; **antiseizure medication** for epilepsy; nutritional/weight management for truncal obesity; and periodic monitoring of liver transaminases.
- **Advanced/experimental therapeutics:** none approved; no gene therapy, cell therapy, or RNA-based therapy in trials for MAN1B1-CDG.
- **Pharmacogenomics / targeted / immunotherapy:** not applicable.

*(NCIT suggestions: Supportive Care; Physical Therapy; Occupational Therapy; Speech Therapy; Anticonvulsant Therapy.)*

### 13. Prevention

- **Primary prevention:** not possible for a monogenic recessive disorder beyond reproductive risk reduction.
- **Genetic counseling:** central — carrier parents have a 25% recurrence risk per pregnancy; counseling on consanguinity-associated recessive risk is relevant.
- **Reproductive options:** carrier testing of at-risk relatives (cascade screening), prenatal diagnosis, and preimplantation genetic testing where a familial variant is known.
- **Newborn/population screening:** not currently part of standard newborn screening panels.
- **Secondary/tertiary prevention:** early diagnosis enables timely developmental support; monitoring and managing epilepsy, liver function, and obesity prevents complications.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** MAN1B1 is conserved across vertebrates; the disease-relevant missense residues are conserved across the animal kingdom ([PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/)), and the non-enzymatic gatekeeper decapeptide is vertebrate-specific ([PMID: 24627495](https://pubmed.ncbi.nlm.nih.gov/24627495/)). Mouse ortholog: *Man1b1* (NCBI Gene ID 227619).
- **Natural disease in other species:** no naturally occurring MAN1B1-CDG analog documented in companion animals or wildlife (no OMIA entry identified).
- **Comparative biology:** high evolutionary conservation of the GH47 mannosidase mechanism supports cross-species functional relevance.
- **Transmission/zoonosis:** not applicable (genetic disorder).

### 15. Model Organisms

- **Direct MAN1B1-CDG animal models:** no well-characterized, published mammalian knockout model specifically recapitulating the human MAN1B1-CDG phenotype was identified in this investigation.
- **In vitro models:** patient-derived fibroblasts demonstrate altered Golgi morphology (dilatation/fragmentation) and the hybrid-type glycan defect, serving as the principal disease model ([PMID: 24348268](https://pubmed.ncbi.nlm.nih.gov/24348268/)); mammalian cell overexpression systems established the loss-of-function mechanism of missense alleles and the gatekeeper role ([PMID: 21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/); [PMID: 24627495](https://pubmed.ncbi.nlm.nih.gov/24627495/)).
- **Related CDG models (context only):** other CDGs have animal models (e.g., Ngly1-deficient rats for NGLY1 deficiency, [PMID: 41721346](https://pubmed.ncbi.nlm.nih.gov/41721346/)), but these model distinct genes, not MAN1B1.
- **Gap:** a conditional/knockout mammalian model would be a valuable resource (see Follow-up).

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF variants in MAN1B1 (9q34.3)
   e.g., p.Arg334Cys (down kcat ~1300x), p.Trp473* (nonsense)
                     |
                     v
 Loss of GH47 alpha-1,2-mannosidase activity  --+
                     |                           | (parallel branch)
                     v                           v
 Failure to trim terminal alpha1,2-mannose   Loss of non-enzymatic
 on N-glycans (Golgi)                        "gatekeeper" decapeptide
                     |                           |
                     v                           v
 Accumulation of hybrid-type N-glycans       Defective ERAD substrate
 on secreted glycoproteins                   retention / QC
   (diagnostic transferrin signature)           |
                     |___________________________|
                                 |
                                 v
          Altered Golgi morphology (dilatation, fragmentation)
                                 |
                                 v
        Aberrant glycosylation of many client proteins (inferred)
                                 |
            _____________________|____________________
           |                     |                    |
           v                     v                    v
   Neurodevelopmental      Hepatic branch        Metabolic/other
   impairment              (hypertransaminasemia) (truncal obesity,
   (ID, DD, hypotonia,                             cryptorchidism,
   dysmorphism, behavior)                          epilepsy - variable)
```

MAN1B1-CDG illustrates two linked but distinct mechanisms converging on disease: a **catalytic defect** (impaired N-glycan mannose trimming) and a **non-catalytic quality-control defect** (loss of the gatekeeper function controlling misfolded-protein disposal). Upstream, the mutation and enzyme loss are well demonstrated; the biochemical consequence (hybrid-type glycans, abnormal Golgi) is directly observed in patient cells; the downstream link from generalized glycosylation disturbance to specific neurodevelopmental outcomes is plausible but remains **inferred** rather than mechanistically proven. The non-progressive clinical course and relatively mild biochemical signature (trace-level defective glycans) distinguish MAN1B1-CDG from more severe CDGs such as PMM2-CDG.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [24348268](https://pubmed.ncbi.nlm.nih.gov/24348268/) | *MAN1B1 deficiency: an unexpected CDG-II* | Gene discovery via exome; core triad; Golgi localization + abnormal Golgi morphology |
| [21763484](https://pubmed.ncbi.nlm.nih.gov/21763484/) | *Mutations in MAN1B1 cause AR intellectual disability* | 9q34.3 locus; LoF variants; p.Arg334Cys down kcat ~1300x |
| [24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/) | *Diagnostic serum glycosylation profile (MAN1B1)* | Hybrid-type N-glycan transferrin signature; 12/100 CDG-II frequency |
| [24627495](https://pubmed.ncbi.nlm.nih.gov/24627495/) | *Golgi-localized MAN1B1 non-enzymatic gatekeeper* | Non-enzymatic decapeptide gatekeeper role in ERAD/QC |
| [27856750](https://pubmed.ncbi.nlm.nih.gov/27856750/) | *GH47 alpha-mannosidases and glycan maturation* | Enzymatic mechanism of GH47 mannose trimming |
| [39840888](https://pubmed.ncbi.nlm.nih.gov/39840888/) | *Rafiq syndrome, Palestinian child, 44-case review* | AR inheritance; frequency ranking (ID/dysmorphism > obesity) |
| [34162022](https://pubmed.ncbi.nlm.nih.gov/34162022/) | *MAN1B1-CDG: novel patients and variant* | CDG type 2 IEF pattern; hypertransaminasemia |
| [34141584](https://pubmed.ncbi.nlm.nih.gov/34141584/) | *MAN1B1-CDG: three new individuals, biochemical profiles* | MALDI-TOF diagnostic decision tree; trace-level glycans |
| [34258140](https://pubmed.ncbi.nlm.nih.gov/34258140/) | *Disulfiram translational balancing* | Failed pharmacologic trial — no disease-modifying therapy |
| [39896699](https://pubmed.ncbi.nlm.nih.gov/39896699/) | *Rafiq syndrome, new phenotypic features* | p.Arg334Cys; feeding difficulty + hyperekplexia (novel) |
| [41905312](https://pubmed.ncbi.nlm.nih.gov/41905312/) | *Biochemical genetic testing after equivocal sequencing* | MAN1B1 2nd most frequent CDG gene (n=6) after PMM2 |
| [41246981](https://pubmed.ncbi.nlm.nih.gov/41246981/) | *Saudi patient, p.Pro373Arg* | Novel variant; expanded phenotype |
| [41393301](https://pubmed.ncbi.nlm.nih.gov/41393301/) | *Chinese patient + thyroid dyshormonogenesis* | Compound het variants; coexisting DUOX2 disease |
| [36142510](https://pubmed.ncbi.nlm.nih.gov/36142510/) | *Russian patient, compound het* | c.1065+1G>C splice variant with p.Arg334Cys |
| [41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/) | *Albumin as CDG glycoprotein biomarker* | Albumin N-glycosylation altered in MAN1B1-CDG |

Evidence quality is predominantly **human clinical case reports/series** (small n) plus **in vitro cell biology and enzymology**. The gene-disease relationship, loss-of-function mechanism, Golgi pathology, and diagnostic glycoprofile are well supported; genotype–phenotype correlations and the precise neurodevelopmental mechanism are not.

---

## Limitations and Knowledge Gaps

1. **Small cohort (~45 patients):** prevents robust prevalence estimates, genotype–phenotype correlation, and natural-history/prognosis data.
2. **Inferred downstream mechanism:** the causal link from generalized glycosylation disturbance to specific neurodevelopmental and metabolic outcomes is plausible but not directly demonstrated.
3. **No animal model:** no published mammalian knockout model recapitulating MAN1B1-CDG limits mechanistic and preclinical therapeutic study.
4. **No quantitative QoL/outcome data:** no EQ-5D/SF-36/PROMIS or standardized disability metrics.
5. **No therapy:** only one pharmacologic trial (disulfiram), which was negative; no targeted therapeutic strategy.
6. **Diagnostic subtlety:** trace-level defective glycans make biochemical diagnosis difficult; exome sequencing is often required.
7. **Variant interpretation:** several alleles are recent/novel; functional validation is incomplete for some missense variants.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a conditional/knockout mammalian (mouse) model** of *Man1b1* deficiency to test phenotype recapitulation (neurodevelopment, obesity, liver), and a cellular iPSC-derived neuronal model to probe the neurodevelopmental mechanism.
2. **Build an international MAN1B1-CDG registry/natural-history study** to quantify phenotype frequencies, QoL, and longitudinal course across the ~45+ patients.
3. **Systematic genotype–phenotype analysis** correlating variant class (truncating vs missense; residual activity) with severity, especially for the recurrent p.Arg334Cys.
4. **Validate albumin-derived glycopeptides** and refine transferrin MS workflows as sensitive, specific diagnostic biomarkers to shorten the diagnostic odyssey ([PMID: 41713138](https://pubmed.ncbi.nlm.nih.gov/41713138/); [PMID: 24566669](https://pubmed.ncbi.nlm.nih.gov/24566669/)).
5. **Functional characterization** of newly reported variants (p.Pro373Arg, p.Phe659Cys, splice-site alleles) in mammalian expression systems to confirm pathogenicity and ACMG classification.
6. **Preclinical therapeutic exploration:** given the dual catalytic + gatekeeper mechanism, test proteostasis-modulating and glycan-targeted strategies in cellular models; reassess any residual-function rescue approaches now that disulfiram has failed.
7. **Incorporate MAN1B1 into CDG gene panels and reflex glycomics** given its relative frequency among CDG-II referrals.


## Artifacts

- [OpenScientist final report](MAN1B1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MAN1B1-Congenital_Disorder_of_Glycosylation-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 13 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:27856750` (6 mentions) - Substrate recognition and catalysis by GH47 α-mannosidases involved in Asn-linked glycan maturation in the mammalian secretory pathway.
  - shared terms: mannosidase, glycan

Weighed against this report's own most characteristic terms: `man1b1-cdg`, `man1b1`, `gene`, `patient`, `disorder`, `obesity`, `disability`, `intellectual`, `variant`, `glycosylation`, `type`, `disease`, `n-glycan`, `diagnostic`, `mannosidase`, `cdg-ii`, `developmental`, `glycan`, `truncal`, `cdg`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 18 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (1 mention) - the report calls it "Near-universal"; HP calls it **Intellectual disability**
- `HP:0001263` (1 mention) - the report calls it "Near-universal"; HP calls it **Global developmental delay**
- `HP:0001999` (1 mention) - the report calls it "Near-universal"; HP calls it **Abnormal facial shape**
- `HP:0001252` (1 mention) - the report calls it "Frequent"; HP calls it **Hypotonia**
- `HP:0000750` (1 mention) - the report calls it "Frequent"; HP calls it **Delayed speech and language development**
- `HP:0000708` (1 mention) - the report calls it "Frequent"; HP calls it **Atypical behavior**
- `HP:0001956` (1 mention) - the report calls it "Variable / least consistent"; HP calls it **Truncal obesity**
- `HP:0001250` (1 mention) - the report calls it "Subset"; HP calls it **Seizure**
- `HP:0002910` (1 mention) - the report calls it "Subset"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0000028` (1 mention) - the report calls it "Subset"; HP calls it **Cryptorchidism**
- `HP:0011968` (1 mention) - the report calls it "Subset"; HP calls it **Feeding difficulties**
- `HP:0002267` (1 mention) - the report calls it "Rare/novel"; HP calls it **Exaggerated startle response**
- `UBERON:0002107` (1 mention) - the report calls it "Secondary involvement:** liver"; UBERON calls it **liver**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030433` (obsolete ubiquitin-dependent ERAD pathway) (2 mentions) - replaced by `GO:0036503`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004571` (2 mentions) - the report calls it "mannosyl-oligosaccharide 1,2-α-mannosidase activity"; GO calls it **mannosyl-oligosaccharide 1,2-alpha-mannosidase activity**
- `GO:0036508` (1 mention) - the report calls it "protein α-1,2-demannosylation"; GO calls it **protein alpha-1,2-demannosylation**
- `GO:0030433` (2 mentions) - the report calls it "ubiquitin-dependent ERAD pathway"; GO calls it **obsolete ubiquitin-dependent ERAD pathway**
- `GO:0005794` (2 mentions) - the report calls it "Subcellular compartments:** Golgi apparatus", "Golgi apparatus", "Subcellular:** **Golgi apparatus"; GO calls it **Golgi apparatus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005794` - called "Subcellular compartments:** Golgi apparatus", "Golgi apparatus", "Subcellular:** **Golgi apparatus"