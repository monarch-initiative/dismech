---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T17:28:26.302248'
end_time: '2026-10-27T18:05:10.368025'
duration_seconds: 2204.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Trichohepatoneurodevelopmental Syndrome
  mondo_id: MONDO:0032645
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: THNS
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 42
  verified: 40
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 10
  labels_mismatched: 18
  mislabelled_terms:
  - term_id: MONDO:0032645
    reported_labels:
    - MONDO
    ontology_label: trichohepatoneurodevelopmental syndrome
  - term_id: HP:0001263
    reported_labels:
    - Nearly universal
    ontology_label: Global developmental delay
  - term_id: HP:0010864
    reported_labels:
    - Common
    ontology_label: Severe intellectual disability
  - term_id: HP:0001290
    reported_labels:
    - Common
    ontology_label: Generalized hypotonia
  - term_id: HP:0001392
    reported_labels:
    - Common
    ontology_label: Abnormality of the liver
  - term_id: HP:0030845
    reported_labels:
    - 5/6 in paralog cohort
    ontology_label: Heliotrope rash of eyelid
  - term_id: HP:0000989
    reported_labels:
    - Frequent (9/14 in paralog)
    ontology_label: Pruritus
  - term_id: HP:0001999
    reported_labels:
    - 13/14 (paralog)
    ontology_label: Abnormal facial shape
  - term_id: HP:0000252
    reported_labels:
    - Common
    ontology_label: Microcephaly
  - term_id: HP:0001508
    reported_labels:
    - Pronounced
    ontology_label: Failure to thrive
  - term_id: HP:0001627
    reported_labels:
    - Variable
    ontology_label: Abnormal heart morphology
  - term_id: HP:0000924
    reported_labels:
    - Variable
    ontology_label: Abnormality of the skeletal system
  - term_id: HP:0002795
    reported_labels:
    - Variable
    ontology_label: Abnormal respiratory system physiology
  - term_id: HP:0000504
    reported_labels:
    - Variable
    ontology_label: Abnormality of vision
  - term_id: HP:0011024
    reported_labels:
    - Variable
    ontology_label: Abnormality of the gastrointestinal tract
  - term_id: CL:0000763
    reported_labels:
    - hair follicle cell
    ontology_label: myeloid cell
  - term_id: UBERON:0000970
    reported_labels:
    - Eye / visual system
    ontology_label: eye
  - term_id: UBERON:0004288
    reported_labels:
    - Skeleton / limbs (hip, chest, feet)
    ontology_label: skeleton
  labels_variant: 6
  obsolete_terms:
  - term_id: GO:0061077
    ontology_label: obsolete chaperone-mediated protein folding
    replaced_by: GO:0006457
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Trichohepatoneurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Trichohepatoneurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trichohepatoneurodevelopmental Syndrome
- **MONDO ID:** MONDO:0032645 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** THNS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Trichohepatoneurodevelopmental Syndrome** covering all of the
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

# Trichohepatoneurodevelopmental Syndrome (THNS): A Comprehensive Disease Characteristics Report

**Disease:** Trichohepatoneurodevelopmental Syndrome (THNS)
**MONDO ID:** MONDO:0032645 | **OMIM:** #618268 | **Causal gene:** *CCDC47* (HGNC:24856; gene OMIM *618260)
**Report date:** 2026-10-27

---

## Summary

**Trichohepatoneurodevelopmental syndrome (THNS; MONDO:0032645, OMIM #618268) is an ultra-rare, autosomal-recessive multisystem Mendelian disorder caused by biallelic loss-of-function variants in *CCDC47* (coiled-coil domain containing 47; HGNC:24856; protein alias "calumin"; UniProt Q96A33).** Despite the name's "tricho-hepato-neuro" construction pointing to three organ systems, the unifying lesion is molecular: *CCDC47* encodes an endoplasmic-reticulum (ER) membrane protein that performs two essential jobs — it is a subunit of the **PAT (Protein Associated with the ER Translocon) intramembrane chaperone complex** (together with Asterix, encoded by *WDR83OS*) that folds multipass transmembrane proteins during their biogenesis, and it independently supports **ER calcium storage and signaling**. When both *CCDC47* alleles are truncated, these functions fail, producing the characteristic combination of woolly/coarse hair, liver dysfunction (elevated bile acids, pruritus), and global developmental delay with hypotonia, plus facial dysmorphism and a range of skeletal, cardiac, sensory, and immune features.

The disorder is ultra-rare: fewer than ~10 patients have been reported worldwide as of 2025 (the original four unrelated families reported by Morimoto et al. in 2018, additional cases from Saudi Arabia and China). The gene–disease association has been curated as **STRONG** by ClinGen. All disease-causing alleles described to date are **biallelic truncating (frameshift/nonsense) variants** — e.g., p.(Glu190Profs*7), p.(Arg443*), p.(Leu141Phefs*19), p.(Arg212*) — consistent with a complete loss-of-function recessive mechanism. Mouse *Ccdc47* knockout is embryonic lethal, indicating the gene is essential for early development.

Diagnosis is molecular, established by whole-exome or whole-genome sequencing with confirmation of the *trans* phase of variants by parental testing. There is **no disease-specific or targeted therapy**; management is entirely supportive and multidisciplinary (nutritional support, developmental/physical/occupational/speech therapies, anti-pruritic and cholestasis management, and surveillance for cardiac, skeletal, auditory, and visual complications). Inheritance is autosomal recessive with a 25% sibling recurrence risk; consanguinity is common among reported families, and carrier/cascade/prenatal/preimplantation testing is appropriate for at-risk families.

---

## Section 1 — Disease Information

**Overview.** THNS is a Mendelian, autosomal-recessive, multisystem disorder of childhood onset. It was first delineated in 2018 by Morimoto et al. under the descriptive title *"a Disorder Characterized by Woolly Hair, Liver Dysfunction, Dysmorphic Features, and Global Developmental Delay"* ([PMID: 30401460](https://pubmed.ncbi.nlm.nih.gov/30401460/)). The name "trichohepatoneurodevelopmental" encodes the three defining organ domains: **tricho-** (hair — coarse/woolly hair), **hepato-** (liver — dysfunction with elevated bile acids), and **neurodevelopmental** (global developmental delay, hypotonia, intellectual disability). A later case series summarizes it directly: *"It is characterized by liver dysfunction, hypotonia, global developmental delay, coarse hair, and dysmorphic features."* ([PMID: 39171352](https://pubmed.ncbi.nlm.nih.gov/39171352/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0032645 |
| OMIM (disease) | #618268 (TRICHOHEPATONEURODEVELOPMENTAL SYNDROME; THNS) |
| OMIM (gene) | *618260 (*CCDC47*) |
| MedGen | CN/UID 1648322 |
| UMLS | C4748898 |
| HGNC (gene) | HGNC:24856 |
| NCBI Gene | 57003 |
| Ensembl | ENSG00000108588 |
| UniProt (protein) | Q96A33 |
| Orphanet | No dedicated ORPHAcode found (ultra-rare) |
| ICD-10/ICD-11 | No dedicated code; maps to broad categories |

**Synonyms / alternative names.** THNS; "bi-allelic CCDC47 disorder"; the descriptive 2018 designation (woolly hair, liver dysfunction, dysmorphic features, global developmental delay). The gene *CCDC47* carries aliases GK001, MSTP041, and **calumin**.

**Information source.** The disease-level knowledge is derived from **aggregated case reports and gene-disease curation** (OMIM, ClinGen, ClinVar) rather than EHR-scale cohorts — reflecting the small number (~6–10) of individually reported patients.

---

## Section 2 — Etiology

**Primary cause (genetic).** THNS is caused exclusively by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *CCDC47***. There is no known environmental, infectious, or multifactorial contribution. The gene–disease association reached a **STRONG** ClinGen classification: *"we evaluated the gene-disease association as per ClinGen guidelines and reached a strong level of association"* ([PMID: 39171352](https://pubmed.ncbi.nlm.nih.gov/39171352/)). Independent confirmation comes from the PAT-partner study: *"biallelic variants in CCDC47 were identified in four unrelated families with trichohepatoneurodevelopmental syndrome"* ([PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)).

**Genetic risk factors.** The only established risk factor is carriage of two pathogenic *CCDC47* alleles. **Consanguinity** is a major demographic risk factor, since homozygous truncating variants predominate among reported families (notably the Saudi and Chinese cases). No susceptibility loci or validated modifier genes outside *CCDC47* have been identified, though the paralogous PAT-complex gene *WDR83OS* causes an overlapping phenotype (see Section 6).

**Environmental / lifestyle / protective factors.** None are applicable or documented for this purely monogenic condition. No protective variants or modifier alleles have been reported. Because the disorder is recessive and penetrant in biallelic LoF carriers, heterozygous carriers are unaffected (consistent with the gnomAD constraint profile in Section 4).

**Gene–environment interactions.** Not applicable — no environmental interaction has been described.

---

## Section 3 — Phenotypes

THNS is a multisystem disorder. The cardinal triad is **hair / liver / neurodevelopment**, expanded by dysmorphism and multiple additional system involvements. Phenotype frequencies below are drawn primarily from the expanded case series (Yang et al. 2024, [PMID: 38524542](https://pubmed.ncbi.nlm.nih.gov/38524542/)) and the overlapping PAT-complex disorder (Barish et al. 2024, [PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)).

| Phenotype | Type | Onset / course | Frequency (reported cases) | Suggested HPO term |
|---|---|---|---|---|
| Global developmental delay | Clinical | Infancy; often severe/profound | Nearly universal | HP:0001263 |
| Intellectual disability (profound) | Clinical | Childhood | Common | HP:0010864 |
| Hypotonia (generalized) | Clinical sign | Neonatal/infancy | Common | HP:0001290 |
| Coarse / woolly hair ("tricho-") | Physical | Congenital | Defining feature | HP:0002212 / HP:0002216 |
| Liver dysfunction | Laboratory | Infancy/childhood | Common | HP:0001392 |
| Elevated serum bile acids | Laboratory | Childhood | 5/6 in paralog cohort | HP:0030845 |
| Pruritus / intractable itching | Symptom | Childhood | Frequent (9/14 in paralog) | HP:0000989 |
| Facial dysmorphism | Physical | Congenital | 13/14 (paralog) | HP:0001999 |
| Microcephaly | Physical | Congenital/progressive | Common | HP:0000252 |
| Growth restriction / failure to thrive | Clinical | Infancy | Pronounced | HP:0001508 |
| Congenital heart defects | Clinical | Congenital | Variable | HP:0001627 |
| Skeletal / limb anomalies (hip dislocation/dysplasia, overlapping toes, pectus excavatum, scoliosis, narrow chest, small feet) | Physical | Congenital | Variable | HP:0000924 |
| Respiratory abnormalities | Clinical | Variable | Variable | HP:0002795 |
| Visual abnormalities | Clinical | Variable | Variable | HP:0000504 |
| Hearing impairment | Clinical/sensory | Childhood | Reported (novel, Chinese case) | HP:0000365 |
| Immunodeficiency | Clinical/lab | Variable | Reported | HP:0002721 |
| Gastrointestinal abnormalities | Clinical | Variable | Variable | HP:0011024 |

**Severity and variability.** Severity ranges from severe to profound for the neurodevelopmental component. The expanded series enumerates the full spectrum: *"the most common phenotypes observed in these patients include microcephaly, profound intellectual disability, severe global development delay, pronounced growth restriction, hypotonia, woolly hair, facial dysmorphism, respiratory and visual abnormalities, gastrointestinal abnormalities, liver dysfunction, pruritus, skeletal and limb abnormalities, congenital heart defects and immunodeficiency."* ([PMID: 38524542](https://pubmed.ncbi.nlm.nih.gov/38524542/)). Marked **variable expressivity** is evident: the Chinese patient with homozygous p.Arg212* had hearing impairment (a novel feature — *"our patients showed a novel complication of hearing impairment"*, [PMID: 38524542](https://pubmed.ncbi.nlm.nih.gov/38524542/)) but *lacked* brain abnormalities, hip dislocation, overlapping toes, pectus excavatum, scoliosis, and narrow chest.

**Liver phenotype note.** A distinctive pattern — elevated **bile acids** with **normal bilirubin and normal-to-mildly-elevated liver enzymes** — characterizes the overlapping *WDR83OS* (PAT complex partner) disorder and informs the THNS cholestasis/pruritus picture: *"bile acids were significantly elevated in 5/6 of individuals tested, bilirubin was normal and liver enzymes were normal to mildly elevated"* ([PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)).

**Quality of life impact.** Given profound developmental delay, growth restriction, pruritus, and multisystem involvement, QoL and daily functioning are severely affected, with high caregiver dependence. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *CCDC47* (coiled-coil domain containing 47), HGNC:24856, NCBI Gene 57003, Ensembl ENSG00000108588, located at **chr17q23.1** (GRCh38: chr17:63,745,255–63,776,351). Gene OMIM *618260. Aliases: GK001, MSTP041, calumin.

**Protein.** UniProt **Q96A33**, "PAT complex subunit CCDC47," **483 amino acids**, a type I single-pass ER transmembrane protein localized to the ER / rough ER membrane; it binds Ca²⁺ with low affinity and high capacity ("calumin"): *"CCDC47, also known as calumin, has been shown to bind Ca²⁺ with low affinity and high capacity."* ([PMID: 30401460](https://pubmed.ncbi.nlm.nih.gov/30401460/)).

**Pathogenic variants (all biallelic, truncating LoF):**

| Variant (NM_020198.2) | Protein | Type | Zygosity context |
|---|---|---|---|
| c.567_570del | p.(Glu190Profs*7) | Frameshift | Homozygous (Case 1, Saudi) |
| c.1327C>T | p.(Arg443*) | Nonsense | Compound het (Case 2, Saudi) |
| c.422dup | p.(Leu141Phefs*19) | Frameshift | Compound het (Case 2, Saudi) |
| c.634C>T | p.(Arg212*) | Nonsense | Homozygous (Chinese case) |

Source quote: *"Exome sequencing of Case 1 identified a pathogenic homozygous variant within the CCDC47: NM_020198.2:c.567_570del, p.(Glu190Profs*7). Genome sequencing of Case 2 identified two likely pathogenic heterozygous variants within the CCDC47: NM_020198.2:c.1327C>T, p.(Arg443*) and NM_020198.2:c.422dup, p.(Leu141Phefs*19)."* ([PMID: 39171352](https://pubmed.ncbi.nlm.nih.gov/39171352/))

**Variant classification (ACMG/AMP).** All reported disease alleles are classified **Pathogenic / Likely Pathogenic**. ClinVar (queried Oct 2026) contains ~100 total *CCDC47* variant records, of which **17 are Pathogenic/Likely pathogenic** and **11 are specifically annotated to THNS** — consistent with a predominantly truncating spectrum and with the ClinGen STRONG classification.

**Allele frequency / constraint.** gnomAD constraint for *CCDC47*: **pLI ≈ 0** (9.4e-10), observed/expected LoF ratio = 0.68 (LOEUF 0.88). This indicates tolerance of **heterozygous** loss — consistent with a recessive disease model in which only biallelic loss is pathogenic. Pathogenic alleles are vanishingly rare / absent in population databases.

**Somatic vs germline.** All variants are **germline**. No somatic/cancer association is described (no COSMIC relevance).

**Functional consequence.** **Loss of function** (complete, via truncation/NMD). No gain-of-function or dominant-negative mechanism is implicated.

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated modifier genes, epigenetic signatures, or large-scale chromosomal abnormalities are associated with THNS. The functionally related gene *WDR83OS* (PAT complex partner) causes a phenotypically overlapping but distinct disorder.

---

## Section 5 — Environmental Information

No environmental factors, lifestyle factors, or infectious agents contribute to THNS. It is a purely monogenic, autosomal-recessive disorder. This section is **not applicable**.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic truncating variant in *CCDC47*** (e.g., p.Glu190Profs*7, p.Arg443*) **leads to** nonsense-mediated decay and loss of CCDC47 protein (decreased mRNA and protein observed in patient cells). *[Demonstrated]*
2. Loss of CCDC47 **results in** failure of the **PAT intramembrane chaperone complex** (CCDC47 + Asterix/WDR83OS), which normally folds multipass transmembrane proteins during their biogenesis at the ER. *[Demonstrated structurally/biochemically]*
3. **Branch A (proteostasis):** PAT-complex failure **leads to** impaired biogenesis/folding of large multipass membrane proteins → **ER proteostasis stress** and reduced functional membrane proteins across tissues. *[Inferred from PAT structural biology + paralog genetics]*
4. **Branch B (calcium):** Loss of CCDC47 ("calumin," an ER Ca²⁺-binding protein) **results in** (i) decreased total ER Ca²⁺ storage, (ii) impaired IP3R-mediated Ca²⁺ release, and (iii) reduced ER Ca²⁺ refilling via store-operated Ca²⁺ entry (SOCE). *[Demonstrated in patient-derived cells]*
5. Convergent **ER dysfunction (proteostasis + Ca²⁺ dysregulation)** **leads to** cell-type-specific defects in high-demand tissues — hepatocytes (bile acid handling → cholestasis/pruritus), neurons and neural progenitors (developmental delay, hypotonia, microcephaly), hair follicle keratinocytes (coarse/woolly hair), and developing skeletal/cardiac/sensory tissues. *[Inferred]*
6. Tissue-level defects **result in** the clinical THNS phenotype: woolly hair + liver dysfunction (elevated bile acids, pruritus) + global developmental delay/hypotonia + dysmorphism + multisystem anomalies. *[Demonstrated clinically]*

Where the chain branches (steps 3 and 4), both arms converge on generalized ER dysfunction (step 5). Complete ablation is embryonic lethal in mouse, placing CCDC47 upstream as an essential developmental gene.

### Molecular detail

**Molecular pathways / protein function.** CCDC47 heterodimerizes with **Asterix** (106-aa protein encoded by *WDR83OS*) to form the **PAT complex**: *"WDR83OS) encodes the 106-aa (amino acid) protein Asterix, which heterodimerizes with CCDC47 to form the PAT (protein associated with ER translocon) complex. This complex functions as a chaperone for large proteins containing transmembrane domains to ensure proper folding."* ([PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)). Structural work defines its mechanism precisely: *"The PAT complex, an intramembrane chaperone comprising Asterix and CCDC47, engages early TMDs of multipass proteins to promote their biogenesis"* and *"the nascent chain is not engaged with Sec61, which is occluded and latched closed by CCDC47"* ([PMID: 36261528](https://pubmed.ncbi.nlm.nih.gov/36261528/)). Mechanistically, CCDC47 **latches Sec61 closed** while Asterix redirects the substrate behind Sec61 into a semi-enclosed, lipid-filled cavity where transmembrane domains insert and fold — a **multipass translocon**.

**Calcium handling.** CCDC47/calumin was independently identified as *"a unique calcium regulating protein"* whose *"overexpression of CCDC47 resulted in increase in ionomycin-induced calcium release and reuptake"* ([PMID: 30140426](https://pubmed.ncbi.nlm.nih.gov/30140426/)). Loss-of-function patient cells show *"decreased total ER Ca2+ storage, impaired Ca2+ signaling mediated by the IP3R Ca2+ release channel, and reduced ER Ca2+ refilling via store-operated Ca2+ entry."* ([PMID: 30401460](https://pubmed.ncbi.nlm.nih.gov/30401460/)).

**Genetic validation of the complex.** Biallelic truncating *WDR83OS* (Asterix) variants cause an overlapping neurodevelopmental disorder with hypercholanemia ([PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)), **genetically validating the PAT complex as the disease-relevant module** and reinforcing a shared cholestasis-with-pruritus mechanism.

**Suggested ontology terms.**
- GO biological process: GO:0045047 (protein targeting to ER), GO:0072318 / membrane-protein insertion into ER membrane, GO:0051209 (release of sequestered Ca²⁺ into cytosol), GO:0006983 (ER overload response), GO:0061077 (chaperone-mediated protein folding).
- GO cellular component: GO:0005789 (endoplasmic reticulum membrane), GO:0005791 (rough ER), GO:0071256 (translocon complex).
- CL cell types: CL:0000182 (hepatocyte), CL:0000540 (neuron), CL:0011020 (neural progenitor), CL:0000312 (keratinocyte), CL:0000763 (hair follicle cell).

```
  CCDC47 biallelic LoF
          │
          ▼
  Loss of CCDC47 protein (NMD)
          │
   ┌──────┴───────────────┐
   ▼                      ▼
PAT complex failure     Calcium dysregulation
(multipass MP folding)  (↓ER Ca²⁺ store, ↓IP3R, ↓SOCE)
   │                      │
   └──────┬───────────────┘
          ▼
  Generalized ER dysfunction
          │
   ┌──────┼──────┬───────┬────────┐
   ▼      ▼      ▼       ▼        ▼
 Liver  Brain  Hair   Skeletal  Cardiac/
(bile  (GDD,  (woolly) /sensory  immune
 acids, hypotonia)
pruritus)
```

---

## Section 7 — Anatomical Structures Affected

| Level | Structure | Suggested ontology term |
|---|---|---|
| Organ (primary) | Liver | UBERON:0002107 |
| Organ (primary) | Brain / CNS | UBERON:0000955 |
| Organ (primary) | Hair / skin | UBERON:0001037 (strand of hair), UBERON:0002097 (skin) |
| Organ (secondary) | Heart | UBERON:0000948 |
| Organ (secondary) | Ear / auditory system | UBERON:0001690 |
| Organ (secondary) | Eye / visual system | UBERON:0000970 |
| Organ (secondary) | Skeleton / limbs (hip, chest, feet) | UBERON:0004288 |
| Organ (secondary) | Immune system | UBERON:0002405 |
| Body systems | Nervous, digestive/hepatobiliary, integumentary, musculoskeletal, cardiovascular, sensory, immune | — |
| Tissue/cell | Hepatocytes, neurons/neural progenitors, keratinocytes/hair follicle cells | CL:0000182, CL:0000540, CL:0000312 |
| Subcellular | Endoplasmic reticulum membrane (rough ER); ER translocon | GO:0005789, GO:0005791 |
| Localization | Bilateral/generalized (systemic ER defect); hip dislocation/dysplasia may be bilateral | — |

The subcellular epicenter is the **ER membrane**, where CCDC47 resides and where both the PAT-complex chaperone function and Ca²⁺ handling occur.

---

## Section 8 — Temporal Development

**Onset.** Congenital to early infancy. Hair and dysmorphic features are present at birth; hypotonia and developmental delay manifest in infancy; liver dysfunction and bile acid elevation present in infancy/childhood.

**Progression.** Insidious and chronic. The neurodevelopmental impairment is static-to-progressive; growth restriction is pronounced. By analogy to the paralogous *WDR83OS* disorder, a **progressive reduction in relative head circumference (progressive microcephaly)** is plausible — *"we observed a progressive reduction in relative head circumference"* ([PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)) (inferred for THNS).

**Disease course / duration.** Chronic, lifelong. No remission patterns are described. Critical windows likely coincide with early neurodevelopment (prenatal–early postnatal), given the embryonic lethality of complete murine ablation and the developmental nature of the phenotype.

---

## Section 9 — Inheritance and Population

**Epidemiology.** Ultra-rare. Only **~6 reported cases** across the literature as of 2025 (the original 4 unrelated families from Morimoto 2018, plus Saudi cases 5 and 6, plus the Chinese case). No prevalence/incidence estimates are available; it is below the threshold for Orphanet point-prevalence reporting.

**Inheritance.** **Autosomal recessive.** Biallelic (homozygous or compound-heterozygous) truncating variants required. Sibling recurrence risk = **25%**.

**Penetrance / expressivity.** Penetrance appears complete in biallelic LoF carriers; **expressivity is variable** (e.g., presence/absence of brain, skeletal, and auditory features across patients).

**Consanguinity / founder effects.** Consanguinity is prominent; homozygous variants predominate (Saudi and Chinese cases). No defined founder mutation has been established, though recurrence of specific alleles in consanguineous populations is plausible.

**Carrier frequency.** Not formally estimated; heterozygous LoF alleles are tolerated (gnomAD LOEUF 0.88, pLI ≈ 0) and present at very low frequency.

**Demographics.** Reported in Middle Eastern (Saudi) and East Asian (Chinese) populations, likely reflecting consanguinity and ascertainment rather than true geographic restriction. No established sex bias.

---

## Section 10 — Diagnostics

**Molecular diagnosis is definitive.** All reported cases were diagnosed by **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** identifying biallelic *CCDC47* variants, with Sanger segregation confirming the *trans* phase: *"The trans phase of the detected variants has been confirmed by the parental testing."* ([PMID: 39171352](https://pubmed.ncbi.nlm.nih.gov/39171352/)).

**Recommended genetic testing approach.**
- First-line: **WES or WGS** (the diagnosis was made by exome/genome sequencing in every published case).
- Confirmation: **Sanger sequencing** of parents to confirm biallelic *trans* configuration.
- Alternatives: multigene neurodevelopmental/hepatopathy panels including *CCDC47*; single-gene testing where the phenotype is recognized.
- Karyotype/CMA/FISH/mtDNA/repeat-expansion testing are **not** indicated as primary tests (no chromosomal or repeat mechanism).

**Supportive laboratory / clinical findings.**
- Elevated serum **bile acids** (key biochemical clue), with typically **normal bilirubin** and normal-to-mildly-elevated liver enzymes.
- Brain and skeletal imaging (microcephaly, hip dysplasia/dislocation, scoliosis, pectus).
- Audiology, ophthalmology, and cardiac (echocardiography) evaluation given multisystem involvement.
- Immunologic workup where immunodeficiency is suspected.

**Clinical criteria / differential diagnosis.** No formal consensus diagnostic criteria exist. Differential diagnoses include other **woolly-hair syndromes** (e.g., Naxos disease, cardiofaciocutaneous/Noonan-spectrum RASopathies), **syndromic cholestasis/bile-acid disorders** (PFIC, ARC syndrome), and **ER/trafficking disorders** with neurodevelopmental delay. The combination of woolly hair + elevated bile acids + global developmental delay + confirmed biallelic *CCDC47* variants distinguishes THNS. The paralogous *WDR83OS* disorder is the closest molecular mimic.

**Screening.** Carrier screening and cascade testing in consanguineous/at-risk families; prenatal and preimplantation genetic testing are feasible once a familial biallelic genotype is known. No population newborn screening exists.

---

## Section 11 — Outcome / Prognosis

**Survival / mortality.** No formal survival statistics exist for this ultra-rare disorder. The embryonic lethality of complete murine *Ccdc47* knockout underscores that residual function is required for viability; surviving patients have severe multisystem morbidity.

**Morbidity / function.** High morbidity: profound developmental delay/intellectual disability, hypotonia, growth restriction, pruritus, and variable cardiac, skeletal, auditory, and visual impairment produce substantial, lifelong disability and caregiver dependence.

**Disease course.** Chronic and progressive in some features (e.g., inferred progressive microcephaly). Complications include failure to thrive, cholestatic pruritus, orthopedic complications (hip dislocation/scoliosis), hearing/vision loss, and possible immunodeficiency-related infections.

**Prognostic factors.** No validated prognostic biomarkers. Severity likely correlates with the degree of residual CCDC47 function and the breadth of organ involvement. Elevated bile acids may serve as a biochemical disease marker.

---

## Section 12 — Treatment

**No disease-specific or targeted therapy exists.** Management is **supportive and multidisciplinary** (NCIT: Supportive Care):

- **Nutritional support** for failure to thrive / growth restriction.
- **Developmental therapies** — physical, occupational, and speech therapy for delay and hypotonia.
- **Cholestasis / pruritus management** — anti-pruritic agents and bile-acid–directed supportive care (e.g., ursodeoxycholic acid considered in cholestasis; cholestyramine/rifampin/antihistamines for itch) — symptomatic, not curative.
- **Surveillance and management** of cardiac defects, skeletal anomalies (orthopedic care for hip dysplasia/scoliosis), hearing (audiologic rehabilitation/hearing aids), and visual impairment.
- **Immunologic management** if immunodeficiency is present.

**Advanced / experimental therapeutics.** None in clinical trials; no gene therapy, cell therapy, RNA therapy, or small-molecule program is reported. The recessive LoF mechanism and the essential, broadly expressed nature of the gene make gene-replacement conceptually relevant but entirely preclinical.

**Pharmacogenomics / personalized medicine.** Not applicable beyond genotype-based diagnosis and counseling.

Suggested NCIT terms: Supportive Care (C15277), Physical Therapy (C15855), Nutritional Support (C15329), Genetic Counseling (C15338).

---

## Section 13 — Prevention

**Primary prevention** is through **genetic counseling and reproductive options** in families with a known biallelic genotype: carrier screening of relatives, prenatal diagnosis, and preimplantation genetic testing. There is no way to prevent disease onset in an affected biallelic fetus; prevention is reproductive.

- **Secondary prevention:** early molecular diagnosis enabling early supportive intervention (developmental therapies, cholestasis management).
- **Tertiary prevention:** surveillance to prevent complications (orthopedic, cardiac, auditory, nutritional).
- **Counseling:** autosomal-recessive counseling with 25% sibling recurrence risk; emphasize consanguinity-related risk.
- Immunization, public-health, and environmental interventions are **not applicable**.

---

## Section 14 — Other Species / Natural Disease

*CCDC47* is **deeply evolutionarily conserved** (HomoloGene 41351). Orthologs (NCBI Gene IDs):

| Species | Gene | NCBI Gene ID |
|---|---|---|
| Mouse (*Mus musculus*) | *Ccdc47* | 67163 |
| Rat (*Rattus norvegicus*) | *Ccdc47* | 303606 |
| Zebrafish (*Danio rerio*) | *ccdc47* | 447812 |
| Dog (*Canis familiaris*) | *CCDC47* | 480480 |
| Cow (*Bos taurus*) | *CCDC47* | 540167 |
| Chicken (*Gallus gallus*) | *CCDC47* | 419958 |
| Fruit fly (*Drosophila melanogaster*) | — | 33573 |
| Roundworm (*C. elegans*) | — | 175505 |

No **naturally occurring** THNS-equivalent disease has been documented in companion animals or wildlife (no OMIA entry). The deep conservation of the PAT-complex machinery implies conserved mechanisms, making animal models highly relevant. No zoonotic or cross-species transmission applies (monogenic disorder).

---

## Section 15 — Model Organisms

**Mouse (*Mus musculus*).** The most informative model to date: **constitutive *Ccdc47* knockout is embryonic lethal**, establishing the gene as essential for early development — *"In mice, loss of Ccdc47 leads to embryonic lethality, suggesting that Ccdc47 is essential for early development."* ([PMID: 30401460](https://pubmed.ncbi.nlm.nih.gov/30401460/)). This limits the utility of complete knockouts for modeling the viable human phenotype; **conditional/tissue-specific or hypomorphic alleles** would be required to recapitulate organ-specific disease. (MGI: *Ccdc47* 67163.)

**Zebrafish (*Danio rerio*).** For the paralogous PAT-complex gene *WDR83OS*, a zebrafish model implicated **lipid absorption, craniofacial, and nervous-system development** ([PMID: 39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/)), providing a tractable system to probe PAT-complex biology relevant to THNS (cholestasis, neurodevelopment, dysmorphism). (ZFIN: *ccdc47* 447812.)

**Cellular / in vitro models.** **Patient-derived cells** carrying biallelic damaging alleles are the primary functional system, demonstrating decreased CCDC47 mRNA/protein and the ER Ca²⁺ defects (↓ ER Ca²⁺ store, impaired IP3R release, reduced SOCE) ([PMID: 30401460](https://pubmed.ncbi.nlm.nih.gov/30401460/)). Cardiomyocyte overexpression studies established the calcium-regulatory role ([PMID: 30140426](https://pubmed.ncbi.nlm.nih.gov/30140426/)). iPSC-derived hepatocytes/neurons and organoids are logical future models (not yet reported).

**Phenotype recapitulation.** Partial: calcium and proteostasis phenotypes are captured in cells; whole-organism multisystem recapitulation awaits conditional mammalian models. **Databases:** MGI, RGD, ZFIN, FlyBase, WormBase.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [30401460](https://pubmed.ncbi.nlm.nih.gov/30401460/) | *Bi-allelic CCDC47 Variants Cause a Disorder Characterized by Woolly Hair, Liver Dysfunction, Dysmorphic Features, and Global Developmental Delay* | **Landmark delineation.** First description of THNS; establishes core phenotype, ER Ca²⁺ functional defects, calumin/Ca²⁺-binding identity, and mouse embryonic lethality. |
| [39171352](https://pubmed.ncbi.nlm.nih.gov/39171352/) | *CCDC47 gene and THNS: fifth and sixth cases from Saudi Arabia* | Documents specific pathogenic variants, biallelic inheritance, parental *trans*-phase confirmation, and **ClinGen STRONG** gene-disease validity. |
| [38524542](https://pubmed.ncbi.nlm.nih.gov/38524542/) | *Clinical and genetic analysis of THNS* | Expands phenotype spectrum (microcephaly, immunodeficiency, heart defects) and documents **variable expressivity** (novel hearing impairment; absent features in p.Arg212* case). |
| [39471804](https://pubmed.ncbi.nlm.nih.gov/39471804/) | *Homozygous variants in WDR83OS lead to a neurodevelopmental disorder with hypercholanemia* | **Validates the PAT complex** as disease-relevant; defines Asterix–CCDC47 heterodimer, cholestasis-with-normal-bilirubin pattern, phenotype frequencies, progressive microcephaly, zebrafish model. |
| [36261528](https://pubmed.ncbi.nlm.nih.gov/36261528/) | *Mechanism of an intramembrane chaperone for multipass membrane proteins* | **Structural mechanism.** Defines PAT complex as intramembrane chaperone; CCDC47 latches Sec61 closed; Asterix redirects substrate into multipass translocon. |
| [30140426](https://pubmed.ncbi.nlm.nih.gov/30140426/) | *Dysregulation of the calcium handling protein CCDC47 in diabetic cardiomyopathy* | Independent evidence that CCDC47/calumin regulates Ca²⁺ flux (release and reuptake). |

**Evidence source types:** human clinical/genetic (30401460, 39171352, 38524542, 39471804), structural/biochemical in vitro (36261528), cellular/model-organism (30140426, 30401460 mouse). The gene–disease relationship is corroborated by ClinGen (STRONG) and ClinVar (17 P/LP records; 11 THNS-annotated).

---

## Mechanistic Model / Interpretation

THNS is best understood as an **ER membrane-biogenesis and calcium-homeostasis disorder** with a convergent causal architecture. A single molecular lesion — complete loss of CCDC47 — disables two ER functions simultaneously: (1) the **PAT intramembrane chaperone** that folds multipass transmembrane proteins (CCDC47 latching Sec61 closed while Asterix redirects substrates into a lipid-filled multipass translocon), and (2) **ER calcium buffering and signaling** (calumin's low-affinity/high-capacity Ca²⁺ binding supporting ER Ca²⁺ stores, IP3R release, and store-operated refilling). Both arms converge on generalized ER dysfunction, which in turn impairs the most biosynthetically demanding tissues — liver (bile acid handling), developing brain, hair follicle, and skeletal/cardiac/sensory systems — producing the tricho-hepato-neurodevelopmental triad plus its multisystem extensions.

The **strongest independent corroboration** is genetic: biallelic truncating variants in the obligate PAT partner *WDR83OS* (Asterix) cause a phenotypically overlapping neurodevelopmental disorder with hypercholanemia. Two genes, one complex, one overlapping disease — a textbook demonstration that the **PAT complex** is the disease-relevant module. The cholestatic signature (elevated bile acids with normal bilirubin) is shared, pointing to a specific vulnerability in hepatocyte bile-acid transport, consistent with multipass bile-acid transporters requiring PAT-assisted folding.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity (~6 cases).** All phenotype frequencies are from tiny cohorts; several frequencies are borrowed from the paralogous *WDR83OS* disorder and are **inferred** for THNS.
2. **No natural history study.** Progression rate, survival, and long-term outcomes are undefined; progressive microcephaly is inferred, not demonstrated, for THNS.
3. **Genotype–phenotype relationships** are unresolved — all alleles are truncating, so the basis of variable expressivity (e.g., presence/absence of brain or skeletal features) is unknown and may reflect genetic background or modifiers.
4. **Tissue-specific mechanism unproven.** The link from generalized ER dysfunction to specific organ phenotypes (why liver/hair/brain) is hypothesized; the identity of the critical multipass client proteins per tissue is unknown.
5. **No faithful whole-organism model.** Complete murine knockout is embryonic lethal; conditional/hypomorphic mammalian models have not been reported.
6. **No therapeutics.** No targeted or disease-modifying treatment exists or is in trials.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a patient registry / GeneMatcher recruitment** to expand the cohort, define natural history, and firm up phenotype frequencies specific to *CCDC47* (rather than borrowed from *WDR83OS*).
2. **Conditional/tissue-specific mouse models** (hepatocyte-, neuron-, keratinocyte-specific *Ccdc47* deletion) to bypass embryonic lethality and test the tissue-vulnerability hypothesis.
3. **iPSC-derived hepatocytes, neurons, and organoids** from patients to dissect the proteostasis vs calcium arms and identify the critical multipass membrane-protein clients (e.g., bile-acid transporters) by comparative membrane proteomics.
4. **Define the PAT-complex "clientome"** via proximity labeling / selective ribosome profiling in CCDC47-null cells to pinpoint which multipass proteins fail to fold in liver, brain, and hair tissues.
5. **Functional rescue assays** (wild-type *CCDC47* re-expression; small-molecule ER Ca²⁺ or proteostasis modulators) in patient cells to nominate therapeutic strategies.
6. **Structure-guided variant interpretation**: map all ClinVar *CCDC47* variants onto the PAT-complex structure ([PMID: 36261528](https://pubmed.ncbi.nlm.nih.gov/36261528/)) to refine classification of VUS and predict residual function.
7. **Standardize diagnostic workup** — propose a biochemical-plus-molecular criterion (elevated bile acids + biallelic *CCDC47* LoF) and seek an Orphanet/ICD-11 code to improve ascertainment.

---

*Report compiled from 9 confirmed findings across 5 investigation iterations, grounded in 6 primary papers and ClinGen/ClinVar/gnomAD annotations.*


## Artifacts

- [OpenScientist final report](Trichohepatoneurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Trichohepatoneurodevelopmental_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 34 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 18 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032645` (3 mentions) - the report calls it "MONDO"; MONDO calls it **trichohepatoneurodevelopmental syndrome**
- `HP:0001263` (1 mention) - the report calls it "Nearly universal"; HP calls it **Global developmental delay**
- `HP:0010864` (1 mention) - the report calls it "Common"; HP calls it **Severe intellectual disability**
- `HP:0001290` (1 mention) - the report calls it "Common"; HP calls it **Generalized hypotonia**
- `HP:0001392` (1 mention) - the report calls it "Common"; HP calls it **Abnormality of the liver**
- `HP:0030845` (1 mention) - the report calls it "5/6 in paralog cohort"; HP calls it **Heliotrope rash of eyelid**
- `HP:0000989` (1 mention) - the report calls it "Frequent (9/14 in paralog)"; HP calls it **Pruritus**
- `HP:0001999` (1 mention) - the report calls it "13/14 (paralog)"; HP calls it **Abnormal facial shape**
- `HP:0000252` (1 mention) - the report calls it "Common"; HP calls it **Microcephaly**
- `HP:0001508` (1 mention) - the report calls it "Pronounced"; HP calls it **Failure to thrive**
- `HP:0001627` (1 mention) - the report calls it "Variable"; HP calls it **Abnormal heart morphology**
- `HP:0000924` (1 mention) - the report calls it "Variable"; HP calls it **Abnormality of the skeletal system**
- `HP:0002795` (1 mention) - the report calls it "Variable"; HP calls it **Abnormal respiratory system physiology**
- `HP:0000504` (1 mention) - the report calls it "Variable"; HP calls it **Abnormality of vision**
- `HP:0011024` (1 mention) - the report calls it "Variable"; HP calls it **Abnormality of the gastrointestinal tract**
- `CL:0000763` (1 mention) - the report calls it "hair follicle cell"; CL calls it **myeloid cell**
- `UBERON:0000970` (1 mention) - the report calls it "Eye / visual system"; UBERON calls it **eye**
- `UBERON:0004288` (1 mention) - the report calls it "Skeleton / limbs (hip, chest, feet)"; UBERON calls it **skeleton**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0061077` (obsolete chaperone-mediated protein folding) (1 mention) - replaced by `GO:0006457`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0051209` (1 mention) - the report calls it "release of sequestered Ca²⁺ into cytosol"; GO calls it **release of sequestered calcium ion into cytosol**
- `GO:0061077` (1 mention) - the report calls it "chaperone-mediated protein folding"; GO calls it **obsolete chaperone-mediated protein folding**
- `GO:0005791` (2 mentions) - the report calls it "rough ER"; GO calls it **rough endoplasmic reticulum**, and lists "rough ER" among its other names
- `CL:0011020` (1 mention) - the report calls it "neural progenitor"; CL calls it **neural progenitor cell**
- `UBERON:0000955` (1 mention) - the report calls it "Brain / CNS"; UBERON calls it **brain**
- `UBERON:0001690` (1 mention) - the report calls it "Ear / auditory system"; UBERON calls it **ear**, and lists "auditory apparatus" among its other names