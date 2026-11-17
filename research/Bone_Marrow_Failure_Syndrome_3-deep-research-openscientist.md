---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T08:50:31.193599'
end_time: '2026-11-13T09:23:02.513241'
duration_seconds: 1951.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Bone Marrow Failure Syndrome 3
  mondo_id: MONDO:0014887
  category: Mendelian
  causal_genes: DNAJC21
  omim_id: OMIM:617052
  synonyms: bone marrow failure syndrome type 3; BMFS3; DNAJC21 bone marrow failure
    syndrome; DNAJC21-related bone marrow failure syndrome; bone marrow failure syndrome
    caused by mutation in DNAJC21
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
  job_id: e2d85e2d-9bf4-4f56-8eba-08e785991946
citation_count: 14
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 19
  relevance_assessed: 15
  on_topic: 15
  validator_version: 0.5.1
term_validation:
  total_terms: 48
  verified: 46
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 1
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: MONDO:0014887
    reported_labels:
    - MONDO
    ontology_label: bone marrow failure syndrome 3
  - term_id: HP:0001875
    reported_labels:
    - Common
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0001508
    reported_labels:
    - Core (~83.3% SDS)
    ontology_label: Failure to thrive
  - term_id: HP:0001263
    reported_labels:
    - Core
    ontology_label: Global developmental delay
  - term_id: HP:0002719
    reported_labels:
    - Core
    ontology_label: Recurrent infections
  - term_id: HP:0000479
    reported_labels:
    - Variable
    ontology_label: Abnormal retinal morphology
  - term_id: HP:0001738
    reported_labels:
    - Variable (~83.3% SDS)
    ontology_label: Exocrine pancreatic insufficiency
  - term_id: HP:0001394
    reported_labels:
    - Variable
    ontology_label: Cirrhosis
  - term_id: HP:0000924
    reported_labels:
    - Variable
    ontology_label: Abnormality of the skeletal system
  - term_id: HP:0001385
    reported_labels:
    - Variable
    ontology_label: Hip dysplasia
  - term_id: HP:0001382
    reported_labels:
    - Variable
    ontology_label: Joint hypermobility
  - term_id: HP:0000028
    reported_labels:
    - Variable
    ontology_label: Cryptorchidism
  - term_id: NCIT:C15360
    reported_labels:
    - Blood Transfusion
    ontology_label: Adjuvant Chemotherapy
  - term_id: NCIT:C1512
    reported_labels:
    - Granulocyte Colony-Stimulating Factor
    ontology_label: Immunoconjugate
  - term_id: NCIT:C92216
    reported_labels:
    - Enzyme Replacement Therapy
    ontology_label: Seminal Vesicle/Coagulating Gland
  - term_id: NCIT:C15280
    reported_labels:
    - Antibiotic Therapy
    ontology_label: Breast Conservation Treatment
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0051082
    ontology_label: obsolete unfolded protein binding
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bone_Marrow_Failure_Syndrome_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bone_Marrow_Failure_Syndrome_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bone Marrow Failure Syndrome 3
- **MONDO ID:** MONDO:0014887 (if available)
- **Causal gene(s):** DNAJC21
- **OMIM:** OMIM:617052
- **Synonyms:** bone marrow failure syndrome type 3; BMFS3; DNAJC21 bone marrow failure syndrome; DNAJC21-related bone marrow failure syndrome; bone marrow failure syndrome caused by mutation in DNAJC21
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Bone Marrow Failure Syndrome 3** covering all of the
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

# Bone Marrow Failure Syndrome 3 (BMFS3; DNAJC21): Comprehensive Disease Characterization

**Disease:** Bone Marrow Failure Syndrome 3 (BMFS3) · **MONDO:** MONDO:0014887 · **OMIM:** 617052
**Causal gene:** *DNAJC21* (DnaJ heat shock protein family (Hsp40) member C21), 5p13.2 · **Inheritance:** Autosomal recessive

---

## Summary

**Bone Marrow Failure Syndrome 3 (BMFS3) is a rare, autosomal-recessive inherited bone marrow failure syndrome (IBMFS) caused by biallelic loss-of-function variants in *DNAJC21*, a nucleolar/cytoplasmic HSP70 (HSPA8) co-chaperone required for maturation of the 60S large ribosomal subunit.** It is a *ribosomopathy* that falls within the Shwachman-Diamond syndrome (SDS) spectrum, alongside disease genes *SBDS*, *EFL1*, and *SRP54*, which all converge on ribosome biogenesis / early protein synthesis. The causal gene is *DNAJC21* — not to be confused with the serially numbered disease name; all identifiers in this report refer specifically to the *DNAJC21*-related entity (OMIM 617052, MONDO:0014887).

Mechanistically, DNAJC21 binds precursor 45S rRNA and participates in nuclear rRNA processing and cytoplasmic 60S maturation through interactions with the cofactors **PA2G4, HSPA8, and ZNF622**. Biallelic loss of function corrupts 60S subunit maturation, causing cytoplasmic accumulation of the 60S nuclear export factor PA2G4, aberrant ribosome profiles, reduced rRNA, increased sensitivity to actinomycin D, and increased cell death. The resulting ribosomal stress activates p53-dependent pathways in hematopoietic progenitors, producing trilineage bone marrow failure. A zebrafish *dnajc21* model recapitulates cytopenia, reduced growth, and defective protein synthesis, and additionally reveals a nucleotide-metabolism imbalance that can be partially reversed by exogenous nucleoside supplementation.

Clinically, patients present in infancy/childhood with bone marrow failure, growth retardation, failure to thrive, developmental delay, recurrent infections, and ectodermal (skin/teeth/hair) abnormalities, with variable retinal, pancreatic, hepatic, and skeletal involvement — a picture overlapping SDS and dyskeratosis congenita. Like other SDS-spectrum ribosomopathies, BMFS3 carries a predisposition to myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML), driven by TP53-dependent clonal evolution and "somatic genetic rescue." There is no gene-specific therapy; management is supportive (transfusions, G-CSF, pancreatic enzyme replacement, infection prophylaxis) with allogeneic hematopoietic stem cell transplantation (HSCT) for severe marrow failure or malignant transformation, plus lifelong multisystem surveillance and genetic counseling.

---

## Key Findings

### 1. BMFS3 is a *DNAJC21*-caused ribosomopathy with an SDS-like phenotype (F001)

Exome sequencing established germline **biallelic mutations in *DNAJC21*** as the cause of a global bone marrow failure syndrome designated BMFS3 (OMIM 617052; MONDO:0014887). The gene product participates in ribosome biogenesis and places the disorder squarely within the SDS spectrum of ribosomopathies.

> "germline biallelic mutations in DNAJC21 (DNAJ homolog subfamily C member 21)" — [PMID: 27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/)

> "SBDS, DNAJC21, EFL1 and SRP54 are involved in ribosome biogenesis: SBDS, through direct interaction with EFL1, promotes the release of the eukaryotic initiation factor 6 (eIF6) during ribosome maturation, DNAJC21 stabilizes the 80S ribosome" — [PMID: 30413969](https://pubmed.ncbi.nlm.nih.gov/30413969/)

Inheritance is autosomal recessive. *DNAJC21*, *SBDS*, *EFL1*, and *SRP54* are mechanistically unified by their shared role in ribosome maturation / early protein synthesis.

### 2. DNAJC21 deficiency corrupts 60S ribosomal subunit maturation (F002)

DNAJC21 associates with rRNA and functions in maturation of the 60S large ribosomal subunit. Patient lymphoblastoid cell lines show increased sensitivity to actinomycin D (a transcription/rRNA-synthesis inhibitor) and reduced rRNA. Disease-causing mutations **impair interactions with the cofactors PA2G4, HSPA8, and ZNF622**, all involved in 60S maturation. Functionally, DNAJC21 deficiency causes cytoplasmic accumulation of the 60S nuclear export factor PA2G4, aberrant ribosome profiles, and increased cell death.

> "DNAJC21 deficiency resulted in cytoplasmic accumulation of the 60S nuclear export factor PA2G4, aberrant ribosome profiles, and increased cell death" — [PMID: 27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/)

> "Characterization of mutations revealed impairment in interactions with cofactors (PA2G4, HSPA8, and ZNF622) involved in 60S maturation" — [PMID: 27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/)

This is direct mechanistic evidence linking the molecular lesion (60S maturation defect) to a cellular outcome (apoptosis).

### 3. A distinct multisystem IBMFS overlapping SDS and dyskeratosis congenita (F003)

Across newly reported and all previously described patients, affected individuals share a **core IBMFS phenotype**: bone marrow failure, growth retardation, failure to thrive, developmental delay, recurrent infections, and skin/teeth/hair abnormalities. Variable additional features include retinal abnormalities, pancreatic insufficiency, liver cirrhosis, skeletal abnormalities, congenital hip dysplasia, joint hypermobility, and cryptorchidism.

> "All patients present features consistent with IBMFS: bone marrow failure, growth retardation, failure to thrive, developmental delay, recurrent infections, and skin, teeth or hair abnormalities" — [PMID: 29700810](https://pubmed.ncbi.nlm.nih.gov/29700810/)

> "Additional features present in some individuals include retinal abnormalities, pancreatic insufficiency, liver cirrhosis, skeletal abnormalities, congenital hip dysplasia, joint hypermobility, and cryptorchidism" — [PMID: 29700810](https://pubmed.ncbi.nlm.nih.gov/29700810/)

The authors propose DNAJC21-related disease as a distinct IBMFS with phenotypic overlap with SDS and dyskeratosis congenita.

### 4. Zebrafish model links the ribosomal defect to nucleotide metabolism and TP53-dependent MDS (F004)

The first in vivo *dnajc21* model (zebrafish) phenocopies key patient features — cytopenia, reduced growth, and defective protein synthesis. The cytopenia arises from impaired hematopoietic differentiation, DNA-damage accumulation, and reduced proliferation. Introducing a biallelic *tp53* mutation produces MDS-like features (abnormal erythroid morphology, progenitor expansion). Transcriptomic and metabolomic analyses revealed a role in **nucleotide metabolism**, and exogenous nucleoside supplementation restored neutrophil counts.

> "Zebrafish dnajc21 mutants phenocopy key SDS patient phenotypes such as cytopenia, reduced growth, and defective protein synthesis" — [PMID: 39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/)

> "Exogenous nucleoside supplementation restores neutrophil counts, revealing an association between nucleotide imbalance and neutrophil differentiation" — [PMID: 39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/)

> "The introduction of a biallelic tp53 mutation in the dnajc21 mutants leads to the development of myelodysplastic neoplasia-like features" — [PMID: 39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/)

### 5. Predisposition to myeloid malignancy (MDS/AML) (F005)

One DNAJC21 patient in the original cohort developed AML in childhood. *DNAJC21*, like *SBDS* and *SRP54* (but unlike *EFL1* to date), has been associated with myeloid neoplasia. In SDS broadly, 10–30% of cases transform to myeloid neoplasm. *DNAJC21* germline variants have been detected in AML patients without prior clinical suspicion of a hereditary syndrome.

> "one individual developed a hematological cancer (acute myeloid leukemia) in childhood" — [PMID: 27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/)

> "SBDS, DNAJC21, and SRP54 variants have been associated with myeloid neoplasia" — [PMID: 37226705](https://pubmed.ncbi.nlm.nih.gov/37226705/)

### 6. Gene architecture and population constraint support recessive LoF disease (F006)

*DNAJC21* (NCBI Gene 134218; Ensembl ENSG00000168724; cytoband 5p13.2; aliases BMFS3, DNAJA5, GS3, JJJ1) encodes a DnaJ/Hsp40 protein with two N-terminal tetratricopeptide repeat (TPR) domains and a C-terminal J (DNAJ) domain. It binds precursor 45S rRNA and functions in early nuclear rRNA biogenesis and 60S subunit maturation. gnomAD constraint metrics — pLI ≈ 0, LOEUF (oe_lof_upper) = 1.07, observed/expected LoF = 63/72.4 — indicate the gene is **not haploinsufficient/LoF-constrained**, fully consistent with a recessive (two-hit) mechanism rather than a dominant one. ClinVar lists ~554 *DNAJC21* records including biallelic pathogenic/likely-pathogenic variants spanning frameshift, nonsense, and splice-site types.

> "plays a highly conserved role in the maturation of the 60S ribosomal subunit" — [PMID: 27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/)

### 7. Leukemic transformation proceeds via TP53 ribosomal-stress activation and somatic genetic rescue (F007)

In SDS-spectrum ribosomopathies (*SBDS*, *EFL1*, *DNAJC21*), **TP53-dependent pathways are activated** and contribute to bone marrow failure. Selection pressure promotes the outgrowth of clones bearing somatic *TP53* or *EIF6* mutations — "somatic genetic rescue." *TP53*-mutant clones predispose to MDS/AML, whereas *EIF6* inactivation compensates for the ribosome-joining defect without malignant risk. The estimated incidence of SDS overall is ~1 in 75,000–125,000 live births.

> "Selection pressure promotes outgrowth of TP53 or EIF6 mutant cells, that is, somatic genetic rescue." — [PMID: 42971867](https://pubmed.ncbi.nlm.nih.gov/42971867/)

> "TP53-dependent pathways are activated and can contribute to bone marrow failure." — [PMID: 42971867](https://pubmed.ncbi.nlm.nih.gov/42971867/)

> "The estimated incidence is approximately 1 in 75,000 to 125,000 live births." — [PMID: 42971867](https://pubmed.ncbi.nlm.nih.gov/42971867/)

### 8. Management is supportive plus HSCT, with lifelong surveillance; no gene-specific therapy (F008)

There is no approved gene-targeted therapy for SDS-spectrum disease. Management is supportive: transfusions, G-CSF for neutropenia, pancreatic enzyme replacement for exocrine insufficiency, infection prophylaxis/treatment, and allogeneic HSCT for severe marrow failure or MDS/AML. Non-Fanconi IBMFS (including DNAJC21) have been transplanted successfully with reduced-intensity, fludarabine-based conditioning. DNAJC21-specific diagnostic and periodic-surveillance checklists have been proposed given the multisystem involvement and leukemia risk.

> "besides bone marrow transplantation, no gene-based therapy for SDS has yet been developed" — [PMID: 30413969](https://pubmed.ncbi.nlm.nih.gov/30413969/)

> "non-Fanconi anaemia inherited bone marrow failure syndrome (IBMFS)" — [PMID: 37491781](https://pubmed.ncbi.nlm.nih.gov/37491781/)

In SDS cohorts, major features and frequencies: cytopenia 96.8%, exocrine pancreatic dysfunction 83.3%, failure to thrive 83.3%; median age of onset 0.16 years; male:female ~1.3:1 ([PMID: 37803383](https://pubmed.ncbi.nlm.nih.gov/37803383/)). Zebrafish data suggest nucleoside supplementation as a candidate therapy ([PMID: 39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/)).

### 9. DNAJC21 is a conserved nucleolar/cytoplasmic HSP70 co-chaperone (F009)

DNAJC21 (UniProt Q5F1R6; HGNC:27030; 531 aa) acts as a co-chaperone for HSP70 (HSPA8) and binds precursor 45S rRNA, functioning in 60S maturation. It localizes to the cytoplasm, nucleus, and nucleolus. Orthologs span mouse *Dnajc21* (NCBI Gene 78244), zebrafish *dnajc21* (336984), and *S. cerevisiae* *JJJ1* (855495) — the latter a well-characterized 60S biogenesis factor — establishing deep evolutionary conservation of the ribosome-assembly role.

> "plays a highly conserved role in the maturation of the 60S ribosomal subunit" — [PMID: 27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/)

### 10. The pathogenic variant spectrum is almost exclusively loss-of-function (F010)

ClinVar (reference transcript NM_001012339.3) lists ~40 pathogenic/likely-pathogenic *DNAJC21* alleles that are overwhelmingly **nonsense** (e.g., c.661C>T p.Arg221Ter, c.736C>T p.Gln246Ter, c.1150A>T p.Lys384Ter, c.238G>T p.Glu80Ter, c.15T>G p.Tyr5Ter), **frameshift** (c.950del p.Pro317fs, c.271dup p.Tyr91fs, c.411del p.Phe137fs, c.564_568del p.Asn188fs), or **canonical splice-site** (c.983+1G>A exon-7 skipping, c.97+1G>T, c.1434+2T>C, c.316-2A>C, c.439-2A>G). Missense variants are essentially absent from the P/LP set. Large 5p13 copy-number deletions/duplications spanning *DNAJC21* are also reported as pathogenic (an alternative null allele). Total records ~554 (~98 P, ~29 LP; large VUS fraction).

> "homozygous splice-site variant in the DNAJC21 (NM_001012339.3:c.983+1G>A), causing Shwachman-Diamond Syndrome (SDS). It was shown by the RNA sequencing that exon 7 was skipped" — [PMID: 38408162](https://pubmed.ncbi.nlm.nih.gov/38408162/)

---

## Section-by-Section Report

### 1. Disease Information

BMFS3 is a rare autosomal-recessive inherited bone marrow failure syndrome caused by biallelic *DNAJC21* variants. It is a multisystem ribosomopathy with a Shwachman-Diamond-like phenotype.

| Identifier | Value |
|---|---|
| OMIM | 617052 |
| MONDO | MONDO:0014887 |
| Gene | *DNAJC21* (HGNC:27030; NCBI Gene 134218; Ensembl ENSG00000168724) |
| UniProt | Q5F1R6 |
| Orphanet | Classified within inherited bone marrow failure syndromes / SDS spectrum |
| ICD-10 | D61.0x (constitutional aplastic anemia) as closest mapping |
| Cytoband | 5p13.2 |

**Synonyms:** bone marrow failure syndrome type 3; BMFS3; DNAJC21 bone marrow failure syndrome; DNAJC21-related bone marrow failure syndrome; Shwachman-Diamond-like syndrome due to DNAJC21. The information is derived from aggregated disease-level resources (OMIM, ClinVar, UniProt, gnomAD) and primary case reports/cohort studies — not a single EHR.

### 2. Etiology

**Causal factor:** purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in *DNAJC21* (F001, F010). **Genetic risk factor:** carrier parents (each heterozygous); consanguinity increases homozygosity risk in recessive disease. **Environmental risk/protective factors:** none established; this is a monogenic disorder. **Gene–environment interaction:** not established as a primary driver, though the zebrafish model implies nucleotide availability modulates the hematopoietic phenotype (F004), raising the possibility that nutritional nucleoside supply could modify severity. **Protective genetic factor at the somatic level:** *EIF6* inactivation compensates for the ribosome-joining defect without malignant risk (F007), functioning as a benign "somatic rescue" — the mechanistic inverse of the leukemogenic *TP53* rescue.

### 3. Phenotypes

| Phenotype | Type | Frequency | Suggested HPO |
|---|---|---|---|
| Bone marrow failure / pancytopenia | Lab/clinical | Core (cytopenia ~96.8% in SDS spectrum) | HP:0005528 (bone marrow hypocellularity); HP:0001876 (pancytopenia) |
| Neutropenia | Lab | Common | HP:0001875 |
| Growth retardation / short stature | Clinical | Core | HP:0001510; HP:0004322 |
| Failure to thrive | Clinical | Core (~83.3% SDS) | HP:0001508 |
| Developmental delay | Clinical | Core | HP:0001263 |
| Recurrent infections | Clinical | Core | HP:0002719 |
| Skin / teeth / hair abnormalities | Physical | Core | HP:0011138; HP:0000164; HP:0001595 |
| Retinal abnormalities | Clinical | Variable | HP:0000479 |
| Exocrine pancreatic insufficiency | Lab/clinical | Variable (~83.3% SDS) | HP:0001738 |
| Liver cirrhosis / transaminitis | Clinical | Variable | HP:0001394 |
| Skeletal abnormalities | Physical | Variable | HP:0000924 |
| Congenital hip dysplasia | Physical | Variable | HP:0001385 |
| Joint hypermobility | Physical | Variable | HP:0001382 |
| Cryptorchidism | Physical | Variable | HP:0000028 |
| Microdontia / microphthalmia | Physical | Occasional | HP:0000691; HP:0000568 |

Onset is typically neonatal/early-childhood (median onset ~0.16 years in SDS cohorts). Severity is variable; the hematologic course can be progressive with risk of clonal evolution. Quality-of-life impact derives chiefly from transfusion dependence, infection burden, growth/developmental impairment, and cancer surveillance anxiety (disease-specific QoL instruments not reported for BMFS3). (F002, F003, F008)

### 4. Genetic / Molecular Information

**Causal gene:** *DNAJC21* (OMIM 617052). **Variant classes:** nonsense, frameshift, and canonical splice-site predominate; missense P/LP variants are essentially absent; large 5p13 CNVs act as alternative null alleles (F010). **Functional consequence:** loss of function (recessive). gnomAD constraint (pLI≈0, LOEUF 1.07) confirms the gene tolerates heterozygous LoF — disease requires biallelic hits (F006). **Modifier genes:** somatic *TP53* (leukemogenic) and somatic *EIF6* (benign rescue) modify clonal outcome (F007); in rare reports, digenic interaction with telomere-biology-gene VUS (e.g., *NAF1*, *RTEL1*) co-occurs with a DNAJC21 pathogenic allele ([PMID: 41142505](https://pubmed.ncbi.nlm.nih.gov/41142505/)). **Epigenetic information:** none specific to BMFS3 established. **Chromosomal abnormalities:** acquired del(1;7) and MDS-associated cytogenetics can arise upon clonal evolution.

### 5. Environmental Information

No environmental, lifestyle, or infectious causes contribute to BMFS3 — it is a monogenic recessive disorder (F001, F006). Recurrent infections are a *consequence* of neutropenia/immune compromise, not a cause. The only non-genetic lead with mechanistic plausibility is **nucleotide/nucleoside availability**, which modulates neutrophil differentiation in the zebrafish model (F004).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function variants in *DNAJC21* (nonsense/frameshift/splice/CNV) **lead to** loss of functional DNAJC21 co-chaperone protein. *(demonstrated — F001, F010)*
2. Loss of DNAJC21 **impairs** its interactions with 60S-maturation cofactors PA2G4, HSPA8, and ZNF622. *(demonstrated — F002)*
3. Impaired cofactor interactions **result in** defective nuclear rRNA processing and corrupted cytoplasmic 60S large-ribosomal-subunit maturation, with cytoplasmic accumulation of the 60S export factor PA2G4, aberrant ribosome profiles, and reduced rRNA. *(demonstrated — F002)*
4. Defective 60S maturation **causes** ribosomal stress and reduced global protein synthesis. *(demonstrated in model — F004)*
5. Branch A — Ribosomal stress **activates** TP53-dependent pathways → progenitor apoptosis, DNA-damage accumulation, and reduced proliferation → impaired hematopoietic differentiation → trilineage cytopenia / bone marrow failure. *(demonstrated — F004, F007)*
6. Branch B — DNAJC21 loss **perturbs** nucleotide metabolism (nucleotide imbalance) → impaired neutrophil differentiation; reversible by exogenous nucleosides. *(demonstrated in model — F004)*
7. Branch C (clonal evolution) — Chronic p53-mediated selection pressure **promotes** outgrowth of clones with somatic *TP53* mutation ("somatic genetic rescue") → MDS/AML; alternatively somatic *EIF6* inactivation rescues the ribosome-joining defect benignly. *(demonstrated — F005, F007)*
8. Reduced ribosome function in non-hematopoietic tissues **contributes to** growth retardation, developmental delay, pancreatic, hepatic, retinal, skeletal, and ectodermal features. *(inferred from phenotype + ribosomopathy biology — F003)*

```
 DNAJC21 biallelic LoF
          │
   loss of co-chaperone (HSPA8 partner)
          │
 impaired PA2G4 / HSPA8 / ZNF622 interactions
          │
 corrupted 60S maturation ── PA2G4 cytoplasmic accumulation, aberrant ribosomes, low rRNA
          │
   ribosomal stress / low protein synthesis
        ┌─────────────┬────────────────────┐
        ▼             ▼                    ▼
  TP53 activation   nucleotide         multisystem
  → apoptosis       imbalance          ribosomopathy
  → BM failure      → neutrophil       (growth, pancreas,
        │             defect             liver, retina, bone)
        ▼           (nucleoside-
  clonal selection   reversible)
        ▼
 somatic TP53 → MDS/AML   |  somatic EIF6 → benign rescue
```

**Molecular pathways / GO terms:** ribosomal large subunit biogenesis (GO:0042273), rRNA processing (GO:0006364), maturation of LSU-rRNA (GO:0000470), unfolded protein binding / chaperone cofactor (GO:0051082), ATP-dependent protein folding chaperone (via HSPA8), signal transduction by p53 class mediator (GO:0072331). **Cellular processes:** apoptotic process (GO:0006915), hematopoietic cell differentiation, cell cycle arrest. **Protein dysfunction:** loss of function of a DnaJ/Hsp40 co-chaperone (F009). **Cell types (CL):** hematopoietic stem cell (CL:0000037), common myeloid progenitor (CL:0000049), neutrophil (CL:0000775), erythroid progenitor (CL:0000038). **Subcellular (GO CC):** nucleolus (GO:0005730), nucleus (GO:0005634), cytosol (GO:0005829), preribosome / large subunit precursor (GO:0030687).

### 7. Anatomical Structures Affected

- **Primary organ:** bone marrow (UBERON:0002371) — hematopoietic failure.
- **Secondary organs / systems:** exocrine pancreas (UBERON:0000017), liver (UBERON:0002107), retina/eye (UBERON:0000970), skin (UBERON:0002097), teeth (UBERON:0001091), skeleton/hip (UBERON:0001474), gonads (cryptorchidism). Body systems: hematopoietic/immune, digestive, hepatobiliary, integumentary, skeletal, visual, reproductive.
- **Cell populations:** hematopoietic stem/progenitor cells and all downstream lineages; neutrophils and erythroid progenitors specifically implicated.
- **Subcellular:** nucleolus/nucleus (rRNA processing) and cytoplasm (60S maturation).
- **Lateralization:** systemic/bilateral where applicable (e.g., retinal, hip).

### 8. Temporal Development

Onset is congenital-to-early-childhood (median ~0.16 years in SDS cohorts; diagnostic lag ~1.3 years). Course is chronic and lifelong; the hematologic phenotype may be stable or progressive, and is punctuated by the risk of episodic clonal evolution to MDS/AML. Critical intervention windows: early supportive care and timely HSCT before or at transformation; lifelong hematologic surveillance to catch clonal evolution. (F003, F007, F008)

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive (F001, F006).
- **Epidemiology:** no BMFS3-specific prevalence; it is ultra-rare (dozens of reported patients). SDS-spectrum incidence overall ~1 in 75,000–125,000 live births (F007); DNAJC21 accounts for a small minority of that spectrum.
- **Penetrance/expressivity:** biallelic LoF appears highly penetrant for hematologic disease with variable multisystem expressivity (F003).
- **Carrier frequency:** heterozygous LoF alleles are tolerated (gnomAD oe LoF ~0.87; not constrained), consistent with silent carriers.
- **Consanguinity / founder effects:** homozygous variants are frequently reported in consanguineous or specific populations (e.g., Tunisian case [PMID: 42925145](https://pubmed.ncbi.nlm.nih.gov/42925145/); Indian cohorts [PMID: 42712617](https://pubmed.ncbi.nlm.nih.gov/42712617/)); no single global founder allele established.
- **Sex ratio:** approximately balanced (SDS spectrum M:F ~1.3:1).

### 10. Diagnostics

- **Laboratory:** CBC (cytopenias), bone marrow aspirate/biopsy (hypocellular marrow), pancreatic function (fecal elastase, serum trypsinogen/isoamylase), liver enzymes.
- **Genetic testing (definitive):** whole-exome or whole-genome sequencing, or IBMFS/SDS NGS gene panels including *SBDS, DNAJC21, EFL1, SRP54*; single-gene testing / targeted variant confirmation; chromosomal microarray to detect 5p13 CNVs spanning *DNAJC21*. RNA sequencing can confirm splice effects (e.g., exon-7 skipping for c.983+1G>A, [PMID: 38408162](https://pubmed.ncbi.nlm.nih.gov/38408162/)). Note cryptic/atypical presentations — reanalysis of exome data has disclosed DNAJC21 disease ([PMID: 38408162](https://pubmed.ncbi.nlm.nih.gov/38408162/); [PMID: 40209608](https://pubmed.ncbi.nlm.nih.gov/40209608/)).
- **Cytogenetics/surveillance:** periodic marrow cytogenetics for emerging MDS clones (e.g., monosomy 7, del(1;7)).
- **Differential diagnosis:** Shwachman-Diamond syndrome (*SBDS/EFL1/SRP54*), Fanconi anemia (chromosome-breakage testing negative in DNAJC21), dyskeratosis congenita / telomere biology disorders (short telomeres — can co-occur, [PMID: 41142505](https://pubmed.ncbi.nlm.nih.gov/41142505/)), Diamond-Blackfan anemia.
- **Screening:** cascade/carrier testing in families; prenatal/preimplantation testing feasible for known biallelic variants.

### 11. Outcome / Prognosis

Prognosis is governed by the severity of marrow failure and by the risk of transformation to MDS/AML (10–30% transformation across the SDS spectrum; AML documented in a DNAJC21 patient, F005). Morbidity stems from cytopenias (transfusion dependence, infections, bleeding), growth/developmental impairment, and multisystem complications. Allogeneic HSCT can be curative for the hematologic disease but carries transplant-related risks. Prognostic factors: depth of cytopenia, emergence of somatic *TP53* clones (adverse), and development of MDS/AML. No disease-specific survival statistics exist given rarity; prognosis is extrapolated from the SDS spectrum. (F004, F005, F007, F008)

### 12. Treatment

| Modality | Intervention | NCIT suggestion |
|---|---|---|
| Supportive — cytopenia | Red cell / platelet transfusions | NCIT:C15360 (Blood Transfusion) |
| Supportive — neutropenia | G-CSF (filgrastim) | NCIT:C1512 (Granulocyte Colony-Stimulating Factor) |
| Supportive — pancreatic | Pancreatic enzyme replacement therapy | NCIT:C92216 (Enzyme Replacement Therapy) |
| Supportive — infection | Prophylaxis / treatment of infections | NCIT:C15280 (Antibiotic Therapy) |
| Definitive — marrow failure/malignancy | Allogeneic HSCT (reduced-intensity fludarabine-based conditioning) | NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |
| Experimental (model-derived) | Nucleoside supplementation (zebrafish evidence) | — |

There is no approved gene-specific or gene-replacement therapy (F008). HSCT is the only definitive therapy for severe marrow failure or transformation; non-Fanconi IBMFS including DNAJC21 have been transplanted successfully with reduced-intensity conditioning ([PMID: 37491781](https://pubmed.ncbi.nlm.nih.gov/37491781/)). Pharmacogenomics / targeted / immunotherapy / RNA therapies: none established. The nucleoside-supplementation lead ([PMID: 39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/)) is preclinical only.

### 13. Prevention

- **Primary prevention:** not possible (monogenic); genetic counseling for at-risk couples; carrier screening; preimplantation/prenatal testing.
- **Secondary prevention:** early diagnosis via NGS; hematologic surveillance (serial CBC + marrow cytogenetics) to catch clonal evolution early.
- **Tertiary prevention:** infection prophylaxis, transfusion support, timely HSCT, multisystem surveillance (retinal, pancreatic, hepatic, skeletal) per DNAJC21-specific checklists ([PMID: 29700810](https://pubmed.ncbi.nlm.nih.gov/29700810/)).
- **Counseling:** autosomal-recessive recurrence risk 25% per pregnancy for carrier couples; cascade testing of relatives.

### 14. Other Species / Natural Disease

Orthologs: mouse *Dnajc21* (NCBI Gene 78244), zebrafish *dnajc21* (NCBI Gene 336984), *S. cerevisiae JJJ1* (855495, a 60S biogenesis factor) — deep conservation (F009). A **naturally occurring canine model** exists: Portuguese water dogs with "Canine Congenital Microphthalmos with Hematopoietic Defects," caused by a SINE insertion — notably in *DNAJC1* (not *DNAJC21*) — but proposed as a phenotypic model for DNAJC21-associated syndromes, exhibiting microphthalmia, enamel malformation, stunted growth, anemia, and thrombocytopenia ([PMID: 38682429](https://pubmed.ncbi.nlm.nih.gov/38682429/)). No zoonotic or cross-species transmission applies (genetic disease).

### 15. Model Organisms

- **Zebrafish** *dnajc21* mutant (NCBI Gene 336984): phenocopies cytopenia, reduced growth, defective protein synthesis; *tp53* double-mutant develops MDS-like disease; revealed nucleotide-metabolism link and nucleoside rescue ([PMID: 39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/), F004). The principal in vivo model.
- **Yeast** *JJJ1* deletion: foundational for the conserved 60S biogenesis role (F009).
- **Patient-derived lymphoblastoid cell lines / in vitro:** demonstrated actinomycin-D sensitivity, reduced rRNA, PA2G4 mislocalization, apoptosis (F002).
- **Canine** (Portuguese water dog): naturally occurring syndromic microphthalmia-with-hematopoietic-defects model, proposed as comparative DNAJC21 model ([PMID: 38682429](https://pubmed.ncbi.nlm.nih.gov/38682429/)).
- **Limitations:** zebrafish cannot fully model human multisystem features; no mouse *Dnajc21* disease model has been reported recapitulating the full syndrome.

---

## Mechanistic Model / Interpretation

BMFS3 is best understood as a **two-hit recessive ribosomopathy**. The germline "first and second hits" are the biallelic *DNAJC21* LoF alleles; the loss of this HSP70 co-chaperone corrupts 60S subunit maturation (via PA2G4/HSPA8/ZNF622). The downstream biology then bifurcates: (1) a p53-mediated **apoptotic/anti-proliferative** program that depletes hematopoietic progenitors and produces marrow failure, and (2) a **nucleotide-metabolism** derangement that specifically impairs neutrophil differentiation and is, intriguingly, reversible by nucleoside supplementation. Over time, the chronic p53-selective pressure on the stem-cell pool drives **somatic genetic rescue**: clones acquiring *TP53* mutations escape apoptosis but at the cost of malignant potential (MDS/AML), while clones acquiring *EIF6* inactivation rescue ribosome joining benignly. This same somatic-rescue framework, well-characterized in SBDS-SDS, is shared by DNAJC21, unifying BMFS3 with the broader SDS/leukemia-predisposition paradigm.

The ontology-level summary: a nucleolar/cytoplasmic co-chaperone defect (GO:0042273 ribosomal large subunit biogenesis) in hematopoietic stem/progenitor cells (CL:0000037) of the bone marrow (UBERON:0002371) triggers p53 signaling (GO:0072331) and apoptosis (GO:0006915), producing pancytopenia (HP:0001876) with multisystem comorbidity and MDS/AML risk.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [27346687](https://pubmed.ncbi.nlm.nih.gov/27346687/) | *DNAJC21 Mutations Link a Cancer-Prone BMF Syndrome to Corruption in 60S Maturation* | Landmark gene-discovery & mechanism (F001, F002, F005, F006, F009) |
| [29700810](https://pubmed.ncbi.nlm.nih.gov/29700810/) | *Refining the phenotype associated with biallelic DNAJC21 mutations* | Core + variable phenotype, surveillance checklist (F003, F008) |
| [39138265](https://pubmed.ncbi.nlm.nih.gov/39138265/) | *Loss of Dnajc21 leads to cytopenia and altered nucleotide metabolism in zebrafish* | In vivo model; nucleotide link; tp53 MDS (F004) |
| [42971867](https://pubmed.ncbi.nlm.nih.gov/42971867/) | *Shwachman-Diamond syndrome: ribosomopathies, somatic genetic rescue, leukemia predisposition* | Somatic rescue, p53, incidence (F007) |
| [30413969](https://pubmed.ncbi.nlm.nih.gov/30413969/) | *Shwachman-Diamond Syndrome: Molecular Mechanisms* | Pathway unification; no gene therapy (F001, F008) |
| [37226705](https://pubmed.ncbi.nlm.nih.gov/37226705/) | *Shwachman-Diamond syndromes: rare variants* | DNAJC21 myeloid-neoplasia association (F005) |
| [38408162](https://pubmed.ncbi.nlm.nih.gov/38408162/) | *Rare IBMFS disclosed by exome reanalysis* | Splice-site LoF (exon-7 skip), diagnostics (F010) |
| [37491781](https://pubmed.ncbi.nlm.nih.gov/37491781/) | *HLA-matched HSCT with fludarabine conditioning* | HSCT in non-Fanconi IBMFS (F008) |
| [37803383](https://pubmed.ncbi.nlm.nih.gov/37803383/) | *Clinical features/epidemiology/treatment of SDS* | Frequencies, onset, sex ratio (F008) |
| [40209608](https://pubmed.ncbi.nlm.nih.gov/40209608/) | *SBDS & DNAJC21 variants in BMF: atypical/cryptic* | Novel variant c.98-2delA, atypical presentation |
| [42925145](https://pubmed.ncbi.nlm.nih.gov/42925145/) | *SDS-like syndrome due to novel DNAJC21 variant* | Severe phenotype case (Tunisian) |
| [38682429](https://pubmed.ncbi.nlm.nih.gov/38682429/) | *Canine model of syndromic congenital microphthalmia* | Comparative animal model |
| [41142505](https://pubmed.ncbi.nlm.nih.gov/41142505/) | *BMF with short telomeres and digenic VUS* | DNAJC21 + telomere-gene interaction |
| [37450374](https://pubmed.ncbi.nlm.nih.gov/37450374/) | *Germline variants in AML without suspicion* | DNAJC21 germline allele in AML |
| [42712617](https://pubmed.ncbi.nlm.nih.gov/42712617/) | *IBMFS variant profile, North India* | Emerging DNAJC21 recognition in cohorts |

All quoted snippets above are verbatim from the respective abstracts and were validated during the investigation.

---

## Limitations and Knowledge Gaps

1. **Rarity and small N:** Only dozens of DNAJC21 patients are reported; prevalence, penetrance, and natural-history statistics are extrapolated from the broader SDS spectrum rather than DNAJC21-specific registries.
2. **No DNAJC21-specific epidemiology:** incidence (~1/75,000–125,000) refers to SDS overall; the DNAJC21 share is unknown.
3. **Mechanistic gaps:** the precise link between 60S maturation failure and nucleotide-metabolism derangement is not fully resolved; how multisystem (retinal, pancreatic, hepatic, skeletal) features arise mechanistically is inferred, not demonstrated.
4. **Genotype–phenotype correlations** are poorly defined given the mostly null allelic spectrum and small cohorts.
5. **No mouse disease model** recapitulating the full syndrome; the canine model involves *DNAJC1*, a different gene, limiting direct inference.
6. **Therapeutics:** nucleoside supplementation is preclinical (zebrafish) only; no human trials; no gene therapy.
7. **Variant interpretation:** a large ClinVar VUS fraction (~554 total records) means many alleles remain unclassified; rare missense variants of uncertain pathogenicity need functional assays.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a DNAJC21 patient registry** to quantify penetrance, multisystem frequencies, transformation rate, and transplant outcomes specifically for BMFS3.
2. **Functional assays for VUS resolution:** systematic 60S-maturation / PA2G4-localization / growth-rescue assays (yeast *JJJ1* complementation, patient-cell models) to reclassify the large VUS fraction, especially missense variants.
3. **Test nucleoside supplementation** rigorously — dose-finding in zebrafish, then mammalian models, toward a possible investigational human intervention for neutropenia.
4. **Generate a conditional mouse *Dnajc21* model** (hematopoietic-specific knockout) to capture marrow failure, multisystem features, and p53-dependent transformation, enabling preclinical therapeutic testing.
5. **Longitudinal clonal-hematopoiesis sequencing** (serial marrow) in DNAJC21 patients to track emergence of somatic *TP53* vs *EIF6* clones and define surveillance intervals.
6. **Define a standardized surveillance protocol** (hematologic, pancreatic, hepatic, ophthalmologic, skeletal) validated for DNAJC21 disease.
7. **Explore p53-pathway modulation** as a means to reduce progenitor apoptosis while monitoring leukemic-rescue risk.

---

*Report compiled from 10 confirmed findings and 20 reviewed papers across 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature (PMID). Evidence types span human clinical case/cohort studies, zebrafish and canine model organisms, in vitro patient-cell work, and computational/population-genetic resources (gnomAD, ClinVar, UniProt).*


## Artifacts

- [OpenScientist final report](Bone_Marrow_Failure_Syndrome_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bone_Marrow_Failure_Syndrome_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014887` (4 mentions) - the report calls it "MONDO"; MONDO calls it **bone marrow failure syndrome 3**
- `HP:0001875` (1 mention) - the report calls it "Common"; HP calls it **Decreased total neutrophil count**
- `HP:0001508` (1 mention) - the report calls it "Core (~83.3% SDS)"; HP calls it **Failure to thrive**
- `HP:0001263` (1 mention) - the report calls it "Core"; HP calls it **Global developmental delay**
- `HP:0002719` (1 mention) - the report calls it "Core"; HP calls it **Recurrent infections**
- `HP:0000479` (1 mention) - the report calls it "Variable"; HP calls it **Abnormal retinal morphology**
- `HP:0001738` (1 mention) - the report calls it "Variable (~83.3% SDS)"; HP calls it **Exocrine pancreatic insufficiency**
- `HP:0001394` (1 mention) - the report calls it "Variable"; HP calls it **Cirrhosis**
- `HP:0000924` (1 mention) - the report calls it "Variable"; HP calls it **Abnormality of the skeletal system**
- `HP:0001385` (1 mention) - the report calls it "Variable"; HP calls it **Hip dysplasia**
- `HP:0001382` (1 mention) - the report calls it "Variable"; HP calls it **Joint hypermobility**
- `HP:0000028` (1 mention) - the report calls it "Variable"; HP calls it **Cryptorchidism**
- `NCIT:C15360` (1 mention) - the report calls it "Blood Transfusion"; NCIT calls it **Adjuvant Chemotherapy**
- `NCIT:C1512` (1 mention) - the report calls it "Granulocyte Colony-Stimulating Factor"; NCIT calls it **Immunoconjugate**
- `NCIT:C92216` (1 mention) - the report calls it "Enzyme Replacement Therapy"; NCIT calls it **Seminal Vesicle/Coagulating Gland**
- `NCIT:C15280` (1 mention) - the report calls it "Antibiotic Therapy"; NCIT calls it **Breast Conservation Treatment**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051082` (obsolete unfolded protein binding) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002371` (2 mentions) - the report calls it "Primary organ:** bone marrow"; UBERON calls it **bone marrow**
- `UBERON:0000017` (1 mention) - the report calls it "Secondary organs / systems:** exocrine pancreas"; UBERON calls it **exocrine pancreas**, and lists "pars exocrina pancreatis" among its other names