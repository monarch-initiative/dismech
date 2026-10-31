---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T19:31:27.509866'
end_time: '2026-10-31T19:57:01.043367'
duration_seconds: 1533.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Combined Factor V and Factor VIII Deficiency
  mondo_id: MONDO:0018175
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: F5F8D; FV and FVIII combined deficiency; combined deficiency of factor
    V and factor type VIII; familial multiple coagulation factor deficiency
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
citation_count: 39
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 12
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:17010120
  - PMID:14718532
  - PMID:40296097
  relevance_assessed: 39
  on_topic: 20
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 10
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0018175
    reported_labels:
    - MONDO
    ontology_label: combined deficiency of factor V and factor VIII
  - term_id: HP:0000421
    reported_labels:
    - Sign
    ontology_label: Epistaxis
  - term_id: HP:0000225
    reported_labels:
    - Sign
    ontology_label: Gingival bleeding
  - term_id: HP:0000132
    reported_labels:
    - Sign
    ontology_label: Menorrhagia
  - term_id: HP:0011891
    reported_labels:
    - Sign
    ontology_label: Post-partum hemorrhage
  - term_id: HP:0005261
    reported_labels:
    - abnormal bleeding
    ontology_label: Joint hemorrhage
  - term_id: NCIT:C681
    reported_labels:
    - plasma
    ontology_label: Opiate Antagonist
  - term_id: NCIT:C1947
    reported_labels:
    - Coagulation Factor VIII
    ontology_label: Organic Oxoacids
  - term_id: NCIT:C29066
    reported_labels:
    - Desmopressin
    ontology_label: Gamma Interferon-SCH
  - term_id: NCIT:C47720
    reported_labels:
    - Tranexamic Acid
    ontology_label: Sodium Acetate
  labels_variant: 9
  obsolete_terms:
  - term_id: NCIT:C29066
    ontology_label: Gamma Interferon-SCH
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
  path: Combined_Factor_V_And_Factor_VIII_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Factor_V_And_Factor_VIII_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Factor V and Factor VIII Deficiency
- **MONDO ID:** MONDO:0018175 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** F5F8D; FV and FVIII combined deficiency; combined deficiency of factor V and factor type VIII; familial multiple coagulation factor deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Combined Factor V and Factor VIII Deficiency** covering all of the
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

# Combined Factor V and Factor VIII Deficiency (F5F8D): Comprehensive Disease Characterization

**MONDO:** MONDO:0018175 · **OMIM:** 227300 · **Causal genes:** *LMAN1* (ERGIC-53) and *MCFD2* · **Category:** Mendelian, autosomal recessive

---

## Summary

**Combined Factor V and Factor VIII Deficiency (F5F8D) is not a disease of the clotting-factor genes it is named after.** It is caused by biallelic loss-of-function mutations in either ***LMAN1*** (lectin, mannose-binding 1; also called ERGIC-53; HGNC:6631; chromosome 18q21) or ***MCFD2*** (multiple coagulation factor deficiency 2; HGNC:18451; chromosome 2p21). These two proteins assemble into a calcium-dependent cargo-receptor complex that ferries coagulation factors V (FV) and VIII (FVIII) from the endoplasmic reticulum (ER) to the Golgi through the early secretory pathway. When the receptor fails, FV and FVIII cannot be efficiently secreted, and their plasma activities fall **concordantly to roughly 5–20% of normal**. This is the crucial conceptual point for a knowledge base: the *F5* and *F8* structural genes are entirely normal in F5F8D; the lesion is in the intracellular transport machinery shared by their protein products, which is why a *single* genetic lesion lowers *two* coagulation factors simultaneously.

Clinically, F5F8D is a **mild-to-moderate, lifelong, non-progressive bleeding disorder** dominated by mucocutaneous bleeding (epistaxis, gum bleeding, easy bruising, menorrhagia) and excessive bleeding provoked by surgery, circumcision, dental extraction, trauma, and childbirth. Life-threatening central-nervous-system or gastrointestinal bleeds and hemarthroses are uncommon, distinguishing F5F8D from the more severe rare bleeding disorders (FXIII, FX, FVII). Many patients are minimally symptomatic and are discovered incidentally when routine preoperative screening reveals simultaneously prolonged prothrombin time (PT) and activated partial thromboplastin time (aPTT). Prognosis and life expectancy are excellent.

Diagnosis rests on the combination of concurrently prolonged PT and aPTT (both correcting on 1:1 mixing), concordantly reduced FV:C and FVIII:C with normal von Willebrand factor and normal other clotting factors, confirmed by targeted *LMAN1*/*MCFD2* sequencing. Treatment requires replacing **both** factors — fresh frozen plasma (the only practical FV source, since no FV concentrate exists) plus FVIII raised by desmopressin or FVIII concentrate — supplemented by antifibrinolytics for minor mucosal bleeding and planned peripartum cover during pregnancy. The disorder is enriched in consanguineous Middle-Eastern and South-Asian populations, where founder alleles are documented, and has an estimated general-population prevalence of ~1 in 1,000,000.

---

## 1. Disease Information

F5F8D is a rare autosomal-recessive coagulopathy characterized by the simultaneous, coordinate reduction of two clotting factors — FV and FVIII — that are otherwise genetically and structurally normal. The defect lies in a shared intracellular transport receptor, making F5F8D a paradigm of a "secretory-pathway cargo-receptor disease" rather than a classic single-factor deficiency.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0018175 |
| OMIM | 227300 (F5F8D1, *LMAN1*); 613625 (F5F8D2, *MCFD2*) |
| Orphanet | ORPHA:35909 |
| ICD-10 | D68.2 (hereditary deficiency of other clotting factors) |
| ICD-11 | 3B12 (hereditary deficiency of other coagulation factors) |
| MeSH | Factor V deficiency / Factor VIII deficiency (combined) |
| Genes (HGNC) | *LMAN1* (HGNC:6631; OMIM 601567); *MCFD2* (HGNC:18451; OMIM 607788) |

**Synonyms:** F5F8D; FV and FVIII combined deficiency; combined deficiency of factor V and factor VIII; familial multiple coagulation factor deficiency; DF5F8.

**Source of information:** The knowledge base entry is derived from **aggregated disease-level resources** (OMIM, Orphanet, review literature) combined with **individual-patient case reports and small case series** (e.g., Saudi, Turkish, Tunisian, Iranian, Pakistani, Indian cohorts). There is no large EHR-derived dataset; because of rarity, the evidence base is dominated by case reports, founder-population series, and molecular/structural studies.

---

## 2. Etiology

**Primary cause — genetic.** F5F8D is caused by **biallelic (homozygous or compound heterozygous) loss-of-function mutations** in *LMAN1* or *MCFD2*. Positional cloning first mapped the locus to chromosome 18q21 and identified ERGIC-53/*LMAN1* as the causal gene, with two mutations "accounting for all affected individuals in nine families studied" ([PMID: 9546392](https://pubmed.ncbi.nlm.nih.gov/9546392/)). A second gene, *MCFD2* on 2p21, accounts for *LMAN1*-negative families.

- **~70%** of families carry *LMAN1* mutations; **~15–30%** carry *MCFD2* mutations.
- Essentially all *LMAN1* alleles are **null**: in a survey of 35 families, 13 distinct mutations comprised "3 splice site mutations, 6 insertions and deletions resulting in translational frameshifts, 3 nonsense codons, and elimination of the translation initiation codon" ([PMID: 10090934](https://pubmed.ncbi.nlm.nih.gov/10090934/)).
- **Inheritance is autosomal recessive**; heterozygous carriers are asymptomatic.

**Genetic risk factors:** The only established risk factor is inheritance of two pathogenic *LMAN1* or *MCFD2* alleles. **Consanguinity** sharply increases risk in endogamous populations. **Founder alleles** (see §9) elevate carrier frequency regionally.

**Environmental risk factors:** None established as causal. Because the phenotype is provoked, environmental/situational *triggers of bleeding* (surgery, trauma, dental procedures, childbirth, antiplatelet/anticoagulant drugs) convert a latent defect into a clinical event, but they do not cause the disease.

**Protective factors:** No genetic or environmental protective modifiers are established. Mechanistically, **residual LMAN1 expression** acts in a dose-dependent protective manner — hypomorphic alleles retaining partial function predict milder phenotypes (mouse data, §6).

**Gene–environment interactions:** Not formally characterized. The practical interaction is between the genetic secretion defect and hemostatic challenges (surgery, parturition), which determine when bleeding manifests.

---

## 3. Phenotypes

F5F8D produces a **mild-to-moderate bleeding diathesis**. Phenotypes are both **laboratory abnormalities** (the defining concordant FV/FVIII reduction with dual PT/aPTT prolongation) and **clinical bleeding signs/symptoms**.

| Phenotype | Type | HPO term | Frequency / characteristics |
|---|---|---|---|
| Prolonged PT and aPTT | Lab abnormality | HP:0008151 (prolonged PT), HP:0003645 (prolonged aPTT) | Universal; both correct on mixing |
| Reduced factor V activity | Lab abnormality | HP:0003225 (reduced factor V activity) | ~5–20% in most patients |
| Reduced factor VIII activity | Lab abnormality | HP:0003125 (reduced factor VIII activity) | ~5–20%, concordant with FV |
| Epistaxis | Sign | HP:0000421 | Common |
| Gingival/oral bleeding | Sign | HP:0000225 | Common |
| Easy bruising / ecchymoses | Sign | HP:0000978 (bruising susceptibility) | Common |
| Menorrhagia | Sign | HP:0000132 | Common in affected women |
| Prolonged bleeding after surgery/procedure | Sign | HP:0004846 (post-surgical bleeding) | Characteristic; circumcision, dental extraction |
| Postpartum hemorrhage | Sign | HP:0011891 | Risk during delivery |
| Prolonged bleeding after trauma | Sign | HP:0005261 (abnormal bleeding) | Characteristic |

**Onset:** Congenital (defect present from birth), but recognition is frequently delayed to childhood or adulthood because symptoms are mild; many cases surface at the first hemostatic challenge or incidentally. **Severity:** mild-to-moderate, variable. **Progression:** stable, non-progressive, lifelong. **Frequency among affected individuals:** mucocutaneous bleeding predominates; hemarthrosis and life-threatening CNS/GI bleeds are uncommon.

Characteristic factor levels and severity are summarized in the literature: F5F8D "is characterized by concomitantly low levels (usually between 5% and 20%) of both FV and FVIII, and is associated with a mild to moderate bleeding tendency" ([PMID: 19141160](https://pubmed.ncbi.nlm.nih.gov/19141160/)). A pediatric case documented gum bleeding leading to diagnosis ([PMID: 38912355](https://pubmed.ncbi.nlm.nih.gov/38912355/)), and multiple reports describe incidental detection in asymptomatic individuals on preoperative screening ([PMID: 38659545](https://pubmed.ncbi.nlm.nih.gov/38659545/); [PMID: 41040772](https://pubmed.ncbi.nlm.nih.gov/41040772/)).

**Quality-of-life impact:** Generally modest given the mild phenotype, but women bear a disproportionate burden through menorrhagia and reproductive-tract bleeding, which can affect quality of life and employment (rare-bleeding-disorder cohort, [PMID: 39958127](https://pubmed.ncbi.nlm.nih.gov/39958127/)). Bleeding severity can be quantified with standardized tools (ISTH-BAT; EN-RBD bleeding score), with bleeding score inversely correlated with factor activity ([PMID: 27855295](https://pubmed.ncbi.nlm.nih.gov/27855295/)).

---

## 4. Genetic / Molecular Information

**Causal genes:**

| Gene | Locus | Protein | OMIM (disease) | Share of families |
|---|---|---|---|---|
| *LMAN1* (ERGIC-53) | 18q21.3-q22 | Hexameric type-1 transmembrane mannose-specific lectin | 227300 | ~70% |
| *MCFD2* | 2p21 | Soluble EF-hand protein | 613625 | ~15–30% |

**Pathogenic variants:**
- ***LMAN1*** alleles are **overwhelmingly null** — splice-site, frameshift insertions/deletions, nonsense, and start-codon loss ([PMID: 10090934](https://pubmed.ncbi.nlm.nih.gov/10090934/)). Reported examples include a nonsense C→T transition in exon 9 and a frameshift deletion in a Turkish family ([PMID: 20460353](https://pubmed.ncbi.nlm.nih.gov/20460353/)); a homozygous c.604C>T in a Saudi child ([PMID: 38659545](https://pubmed.ncbi.nlm.nih.gov/38659545/)); and a homozygous c.822G>A in Saudi siblings ([PMID: 36116005](https://pubmed.ncbi.nlm.nih.gov/36116005/)).
- ***MCFD2*** harbors both null and **missense** variants; most reported missense substitutions cluster at the LMAN1-binding interface (see §6), which explains their pathogenicity ([PMID: 20142513](https://pubmed.ncbi.nlm.nih.gov/20142513/)).
- **Structural variants matter:** a heterozygous large deletion in *MCFD2* can mimic a homozygous substitution and requires dosage analysis to resolve ([PMID: 38764219](https://pubmed.ncbi.nlm.nih.gov/38764219/)).

**Variant classification:** Reported disease alleles are predominantly **pathogenic/likely pathogenic** under ACMG/AMP criteria (null variants = PVS1-supported; recurrent founder alleles with segregation).

**Allele frequency:** Pathogenic alleles are extremely rare in gnomAD generally, but founder alleles reach appreciable carrier frequencies regionally (e.g., ~0.011 for the Djerba Tunisian *LMAN1* intron-9 allele; §9).

**Origin:** **Germline**, biallelic. No somatic contribution.

**Functional consequence:** **Loss of function** of the cargo receptor → failure of efficient ER-to-Golgi export of FV and FVIII. The defect is in transport, not synthesis.

**Modifier genes:** The two causal genes modify each other's phenotype — *MCFD2* mutations generally yield lower FV/FVIII than *LMAN1* mutations: "Though clinically indistinguishable, MCFD2 mutations generally exhibit lower levels of FV and FVIII than LMAN1 mutations" ([PMID: 19183188](https://pubmed.ncbi.nlm.nih.gov/19183188/)). Residual LMAN1 dose is itself a quantitative modifier (§6). No external modifier loci are established.

**Epigenetic information / chromosomal abnormalities:** None described as relevant to F5F8D.

---

## 5. Environmental Information

F5F8D is a **purely monogenic disorder with no environmental, lifestyle, or infectious etiology.** No toxins, radiation, occupational exposures, dietary factors, or pathogens cause or trigger the disease. Environmental factors only matter as **bleeding precipitants** (surgery, trauma, parturition) and through drugs that impair hemostasis (antiplatelets, anticoagulants, NSAIDs), which should be used cautiously. **Infectious agents:** not applicable.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in *LMAN1* or *MCFD2*** → **results in** absence or dysfunction of the corresponding protein.
2. Loss of functional LMAN1 and/or MCFD2 → **leads to** failure to assemble a functional **LMAN1–MCFD2 cargo-receptor complex** in the ER.
3. Absent cargo receptor → **results in** failure to capture newly synthesized FV and FVIII in the ER and package them into **COPII-coated vesicles** for ER-to-Golgi transport.
4. Impaired ER exit → **leads to** reduced secretion of FV and FVIII into plasma (and reduced platelet FV).
5. Reduced circulating FV and FVIII (~5–20% of normal) → **results in** impaired generation of both the **tenase** (FVIIIa-dependent) and **prothrombinase** (FVa-dependent) complexes.
6. Impaired thrombin generation on both the intrinsic/common-pathway axes → **leads to** prolonged aPTT (FVIII) *and* prolonged PT (FV), i.e., the signature **dual coagulation-screen abnormality**.
7. Deficient hemostasis → **manifests as** mild-to-moderate mucocutaneous and procedure/trauma-provoked bleeding.

*(Branch: whether the lesion is in LMAN1 or MCFD2 converges on the same complex failure; MCFD2 defects tend to lower factor levels more. Inferred step: the exact quantitative link between residual LMAN1 and human phenotype severity is extrapolated from mouse dose-response data.)*

### Molecular and cellular detail

**The cargo-receptor complex.** LMAN1 (ERGIC-53) is a **hexameric type-1 transmembrane mannose-specific lectin** that cycles between the ER and the ER-Golgi intermediate compartment (ERGIC). Its luminal **carbohydrate-recognition domain (CRD)** contains *separable* binding sites: one for its partner MCFD2 (on the N-terminal β-sheet) and one for mannose/cargo. "The CRD of LMAN1 contains distinct, separable binding sites for both its partner protein (MCFD2) and the cargo proteins (FV/FVIII)," and LMAN1 oligomerization is necessary for receptor function ([PMID: 20817851](https://pubmed.ncbi.nlm.nih.gov/20817851/)). Structural work pinpointed **His178 and Gly251/252** as critical cargo-binding residues ([PMID: 23709226](https://pubmed.ncbi.nlm.nih.gov/23709226/)).

**MCFD2 is the FV/FVIII-specific adaptor.** MCFD2 is a soluble EF-hand (calcium-binding) protein. Crystallography shows a **1:1 ERGIC-53-CRD : MCFD2 complex**, and "the interaction is independent of sugar-binding of ERGIC-53 and involves most of the missense mutation sites of MCFD2 so far reported in F5F8D" ([PMID: 20142513](https://pubmed.ncbi.nlm.nih.gov/20142513/)). Critically, MCFD2 is **not** required for transport of the receptor's other cargoes: "ERGIC-53 can bind cargo glycoproteins in an MCFD2-independent fashion and … MCFD2 is a recruitment factor for blood coagulation factors V and VIII" ([PMID: 17010120](https://pubmed.ncbi.nlm.nih.gov/17010120/)). This is why F5F8D patients lack lysosomal or other cargo phenotypes — only the FV/FVIII arm is affected. MCFD2 binds a **10-amino-acid segment of the FVIII B-domain** ([PMID: 32170195](https://pubmed.ncbi.nlm.nih.gov/32170195/)).

**Division of labor.** Cell-line studies indicate that **MCFD2 performs cargo binding/transport while LMAN1 acts as a shuttle carrier of MCFD2**: overexpression of MCFD2 alone rescues FV/FVIII secretion in LMAN1-deficient cells, and N-glycan binding by LMAN1 is not strictly essential for transport ([PMID: 36490287](https://pubmed.ncbi.nlm.nih.gov/36490287/)).

**pH/Ca²⁺-triggered cargo cycle.** Cargo capture in the ER is **Ca²⁺-dependent at neutral pH**; a conserved CRD histidine acts as a pH/Ca²⁺ sensor so that mild acidification and lower Ca²⁺ in the ERGIC trigger glycoprotein release: "Acidification of cells inhibited the association of ERGIC-53 with the known cargo … and dissociation of this glycoprotein in the ERGIC was impaired by organelle neutralization" ([PMID: 14718532](https://pubmed.ncbi.nlm.nih.gov/14718532/)).

**Broader cargo repertoire.** The LMAN1–MCFD2 receptor also exports **cathepsin C and cathepsin Z** ([PMID: 15849265](https://pubmed.ncbi.nlm.nih.gov/15849265/); [PMID: 17010120](https://pubmed.ncbi.nlm.nih.gov/17010120/)), **alpha-1-antitrypsin** ([PMID: 18283111](https://pubmed.ncbi.nlm.nih.gov/18283111/)), and **Mac-2BP/LGALS3BP** ([PMID: 23550150](https://pubmed.ncbi.nlm.nih.gov/23550150/)). Because MCFD2 is dedicated to FV/FVIII, humans with MCFD2 mutations lose only FV/FVIII transport; the other cargoes are handled MCFD2-independently.

**Cell types and tissues.** FVIII is synthesized primarily by **endothelial cells**, not hepatocytes — conditional-knockout mouse studies "demonstrate that endothelial cells are the primary biosynthetic source of murine FVIII and that hepatocytes make no significant contribution to the plasma FVIII pool" ([PMID: 24719406](https://pubmed.ncbi.nlm.nih.gov/24719406/)). FV is produced by hepatocytes and megakaryocytes (platelet FV).

### ASCII mechanistic model

```
 LMAN1 or MCFD2 biallelic null mutation
             │ (loss of function)
             ▼
 No functional LMAN1–MCFD2 cargo receptor in ER
             │
             ▼
 FV & FVIII not captured → not loaded into COPII vesicles
             │ (ER→Golgi export fails; Ca2+/pH-gated cycle broken)
             ▼
 ↓ Secretion of FV (hepatocytes/megakaryocytes) & FVIII (endothelium)
             │
             ▼
 Plasma FV ≈ FVIII ≈ 5–20% of normal
        ┌────────────┴────────────┐
        ▼                         ▼
 ↓ Prothrombinase (FVa)    ↓ Tenase (FVIIIa)
        │                         │
        ▼                         ▼
   Prolonged PT              Prolonged aPTT
        └────────────┬────────────┘
                     ▼
       Mild–moderate mucocutaneous / provoked bleeding
```

**Suggested GO / CL terms:** GO:0006888 (ER-to-Golgi vesicle-mediated transport); GO:0030134 (COPII-coated ER-to-Golgi transport vesicle); GO:0005537 (mannose binding); GO:0007596 (blood coagulation); GO:0005509 (calcium ion binding). CL:0000182 (hepatocyte); CL:0000115 (endothelial cell); CL:0000556 (megakaryocyte). UBERON:0002107 (liver); UBERON:0001981 (blood vessel). CHEBI:29108 (calcium(2+)); CHEBI:4208 (D-mannose).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** The **hematologic/coagulation system** and the **cardiovascular (blood/vasculature)** system are primarily affected. There is no primary organ pathology; bleeding manifests at mucosal surfaces, skin, joints (rarely), and the reproductive tract.
- **Primary biosynthetic sites:** **Liver (hepatocytes)** for FV; **vascular endothelium** for FVIII ([PMID: 24719406](https://pubmed.ncbi.nlm.nih.gov/24719406/)); **megakaryocytes/platelets** carry a FV pool.
- **Tissue/cell level:** hepatocytes (CL:0000182), endothelial cells (CL:0000115), megakaryocytes (CL:0000556).
- **Subcellular level:** The molecular lesion resides in the **early secretory pathway** — endoplasmic reticulum (GO:0005783), **ER-Golgi intermediate compartment/ERGIC** (GO:0005793), and **COPII vesicles** (GO:0030134).
- **Localization of bleeding:** Mucocutaneous surfaces (nasal mucosa, oral/gingival mucosa, skin), gastrointestinal and intracranial sites (rare), and the uterus/reproductive tract (menorrhagia, postpartum). Bleeding is **systemic/multifocal**, not lateralized.

**UBERON terms:** UBERON:0002107 (liver); UBERON:0001981 (blood vessel/vasculature); UBERON:0000178 (blood); UBERON:0000344 (mucosa); UBERON:0002097 (skin of body).

---

## 8. Temporal Development

- **Onset:** Congenital — the secretion defect is present from birth. Clinical recognition is often **delayed** to childhood or adulthood because bleeding is mild; many cases surface at the first hemostatic challenge (circumcision, dental extraction, surgery, menarche, childbirth) or incidentally on preoperative screening.
- **Onset pattern:** Insidious/chronic baseline with **episodic, provoked** bleeding events.
- **Progression:** **Stable and non-progressive.** Factor levels remain constant over life.
- **Course:** Lifelong (chronic), with excellent prognosis. No disease "stages."
- **Remission:** Not applicable — the genetic defect is permanent; bleeding is managed, not cured. Replacement therapy produces transient correction.
- **Critical periods:** Hemostatic challenges — **surgery, dental procedures, trauma, menstruation, and especially pregnancy/delivery** — are the windows requiring intervention. In pregnancy the physiologic FVIII rise is blunted because secretion (not synthesis) is limiting, so the defect persists and postpartum-hemorrhage risk remains ([PMID: 19298378](https://pubmed.ncbi.nlm.nih.gov/19298378/)).

---

## 9. Inheritance and Population

**Epidemiology:** Estimated prevalence **~1 in 1,000,000** in the general population; F5F8D constitutes roughly **3% of rare coagulation disorders**. "The prevalence of this disease in the general population is estimated to be 1:1,000,000 and is significantly higher in regions where consanguineous marriages are permitted, such as the Mideast and South Asia" ([PMID: 39209292](https://pubmed.ncbi.nlm.nih.gov/39209292/)).

**Inheritance:** **Autosomal recessive.** Heterozygotes are asymptomatic. Equal sex incidence (though women are more often symptomatic due to menstrual/reproductive bleeding).

**Penetrance/expressivity:** High penetrance of the biochemical phenotype (low FV/FVIII) in biallelic carriers; **variable expressivity** of bleeding severity. No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism not a recognized feature.

**Founder effects and consanguinity:** Strong. Documented founder alleles include an **LMAN1 intron-9 donor-splice mutation prevalent among Tunisian Djerba Jews** (carrier allele frequency ~0.011) and an **exon-1 G insertion among Middle Eastern/Iraqi Jews**: "a thymidine (T) to cytosine (C) transition in intron 9 at a donor splice site among Tunisian families. For each mutation, haplotype analysis revealed a founder effect" ([PMID: 15166951](https://pubmed.ncbi.nlm.nih.gov/15166951/)). High prevalence is reported in consanguineous cohorts in Iran ([PMID: 27894217](https://pubmed.ncbi.nlm.nih.gov/27894217/); [PMID: 23632381](https://pubmed.ncbi.nlm.nih.gov/23632381/)) and Pakistan ([PMID: 28388959](https://pubmed.ncbi.nlm.nih.gov/28388959/)).

**Population demographics:** Enriched in Mediterranean, Middle-Eastern, and South-Asian populations where endogamy is common. Geographic distribution of variants tracks founder haplotypes. Sex ratio ~1:1.

---

## 10. Diagnostics

**Diagnostic algorithm:**
1. **Screening coagulation tests:** simultaneously **prolonged PT and aPTT**, both **fully corrected by 1:1 mixing** (indicates factor deficiency, not an inhibitor).
2. **Specific factor assays:** concordant reduction of **FV:C and FVIII:C to ~5–20%**, with **normal levels of other coagulation factors** and **normal von Willebrand factor antigen/activity**. This pattern distinguishes F5F8D from isolated hemophilia A (normal PT), isolated FV deficiency (normal FVIII), and type 2N/3 von Willebrand disease. Illustrative case: "a combined deficiency of factors V and VIII at 12.4% … and 9.1%, respectively, whereas other coagulation factor levels remained within the normal range, including the antigenic activity of von Willebrand" ([PMID: 40296097](https://pubmed.ncbi.nlm.nih.gov/40296097/)).
3. **Molecular confirmation:** targeted **LMAN1/MCFD2 sequencing**, a rare-bleeding-disorder gene panel, or **whole-exome sequencing** (which identified a novel homozygous *LMAN1* c.604C>T, [PMID: 38659545](https://pubmed.ncbi.nlm.nih.gov/38659545/)). **Dosage/copy-number analysis** is needed because a heterozygous large *MCFD2* deletion can masquerade as a homozygous substitution ([PMID: 38764219](https://pubmed.ncbi.nlm.nih.gov/38764219/)).

**Biomarkers:** FV:C and FVIII:C are the defining biomarkers; reduced **platelet FV** supports the diagnosis. vWF is normal (key discriminator).

**Clinical/bleeding assessment:** Standardized bleeding-assessment tools (ISTH-BAT; EN-RBD bleeding score) quantify symptom burden, with bleeding score inversely correlated with factor activity ([PMID: 27855295](https://pubmed.ncbi.nlm.nih.gov/27855295/)).

**Differential diagnosis:** hemophilia A (isolated FVIII, normal PT); isolated FV deficiency (normal FVIII); combined vitamin-K-dependent factor deficiency; von Willebrand disease types 2N/3; rare **digenic** coincidental *F5* + *F8* mutations ([PMID: 41040772](https://pubmed.ncbi.nlm.nih.gov/41040772/)).

**Screening:** Carrier and cascade testing within affected consanguineous families; no population newborn screening exists given rarity and mild phenotype. Imaging/electrophysiology/biopsy are not diagnostic for this disorder.

**LOINC concepts:** PT (5902-2), aPTT (3173-2/14979-9), Factor V activity (3192-2), Factor VIII activity (3209-4), von Willebrand factor antigen (5088-1).

---

## 11. Outcome / Prognosis

**Prognosis is excellent with normal life expectancy.** F5F8D is a **milder** rare bleeding disorder than FXIII, FX, or FVII deficiencies: "patients with factor XIII, factor X and factor VII more commonly presented severe life-threatening bleeding, while patients with combined factor V and factor VIII presented a milder phenotype" ([PMID: 27894217](https://pubmed.ncbi.nlm.nih.gov/27894217/)).

- **Mortality:** Low; disease-specific mortality is uncommon with appropriate peri-procedural and obstetric management.
- **Morbidity:** Mucocutaneous bleeding, menorrhagia, and procedure/trauma-provoked bleeding; hemarthrosis and life-threatening CNS/GI bleeds are uncommon. A 37-case single-center India series documents the clinical spectrum ([PMID: 20575023](https://pubmed.ncbi.nlm.nih.gov/20575023/)).
- **Disease course:** Stable, lifelong, non-progressive. Many patients remain asymptomatic until a hemostatic challenge ([PMID: 38912355](https://pubmed.ncbi.nlm.nih.gov/38912355/); [PMID: 38659545](https://pubmed.ncbi.nlm.nih.gov/38659545/)).
- **Prognostic factors:** Baseline FV/FVIII activity broadly tracks bleeding tendency (MCFD2 genotype → lower levels), but factor levels correlate **inconsistently** with bleeding outcomes, particularly in pregnancy ([PMID: 41789952](https://pubmed.ncbi.nlm.nih.gov/41789952/)), so clinical history and bleeding scores remain essential.

---

## 12. Treatment

**Core principle: replace BOTH factors.** Because no clotting-factor gene is defective but two factor proteins are low, therapy must raise both FV and FVIII. "Treatment of bleeding episodes requires a source of both FV and FVIII; replacement of FV is achieved through the use of fresh frozen plasma, and that of FVIII by desmopressin or specific FVIII concentrates, plasma-derived or recombinant FVIII products" ([PMID: 19141160](https://pubmed.ncbi.nlm.nih.gov/19141160/)).

| Modality | Purpose | Notes / NCIT |
|---|---|---|
| **Fresh frozen plasma** (or SD/virus-inactivated plasma) | Sole practical **FV** source | No FV concentrate exists: "only prothrombin and FV deficiencies still remain without a specific product" ([PMID: 27913544](https://pubmed.ncbi.nlm.nih.gov/27913544/)). NCIT:C681 (plasma) |
| **FVIII concentrate** (plasma-derived or recombinant) | Raise **FVIII** | NCIT:C1947 (Coagulation Factor VIII) |
| **Desmopressin (DDAVP)** | Transiently raise **FVIII** for minor bleeds/procedures | NCIT:C29066 (Desmopressin) |
| **Antifibrinolytics (tranexamic acid)** | Mucosal/minor bleeds, menorrhagia, dental work | NCIT:C47720 (Tranexamic Acid) |
| **Local hemostatic measures** | Epistaxis, dental | Adjunctive |

Management is tailored to the setting — surgery, spontaneous bleeding, pregnancy/delivery, and the neonate — per UKHCDO guidelines ([PMID: 15357789](https://pubmed.ncbi.nlm.nih.gov/15357789/)). Broader reviews confirm the dual-replacement strategy and the absence of a dedicated FV product ([PMID: 19141160](https://pubmed.ncbi.nlm.nih.gov/19141160/); [PMID: 27913544](https://pubmed.ncbi.nlm.nih.gov/27913544/)).

**Pregnancy/peripartum:** A documented F5F8D pregnancy (FV 29%, FVIII 21%; aPTT 78s) was managed with a protocol-based multidisciplinary plan: **2000 IU FVIII at onset of labor** raising FVIII to 36% and FV to 38%, then 12-hourly tapering doses keeping FVIII >50% for 5 days — delivery with no bleeding: "An infusion of 2000IU of FVIII was implemented over 5 minutes; soon thereafter, PT was 17 seconds, aPTT patient/control ratio had decreased to 1.9 and FV and FVIII reached 38% and 36% respectively" ([PMID: 24161289](https://pubmed.ncbi.nlm.nih.gov/24161289/)). Because the defect persists through pregnancy, planned cover prevents postpartum hemorrhage ([PMID: 19298378](https://pubmed.ncbi.nlm.nih.gov/19298378/)).

**Pharmacogenomics / gene / cell / targeted therapies:** None approved or required; F5F8D is managed with replacement and antifibrinolytics. (Of note, the LMAN1–MCFD2 axis is being explored in the *opposite* direction as an **anticoagulant target** — GalNAc-siRNA knockdown of LMAN1/MCFD2 lowers FVIII and prolongs aPTT in mice, [PMID: 39222205](https://pubmed.ncbi.nlm.nih.gov/39222205/) — which conceptually validates the pathway but is not a treatment for the deficiency.)

**Treatment strategy:** On-demand replacement for bleeds/procedures; prophylaxis is rarely needed given the mild phenotype; antifibrinolytics first-line for menorrhagia and mucosal bleeding.

---

## 13. Prevention

- **Primary prevention:** Not possible (monogenic, congenital). **Genetic counseling** and **carrier/cascade screening** in affected families — especially in consanguineous communities and founder populations — reduce recurrence; **prenatal/preimplantation genetic testing** is available where a familial mutation is known.
- **Secondary prevention:** Early diagnosis via recognition of the dual PT/aPTT pattern on preoperative screening; confirm before elective surgery to plan hemostatic cover.
- **Tertiary prevention (preventing bleeding complications):** Pre-procedure factor replacement, peripartum protocols, antifibrinolytics, avoidance of antiplatelet/anticoagulant drugs and intramuscular injections, routine dental care, and iron supplementation for menorrhagia-related anemia.
- **Counseling:** Autosomal-recessive recurrence risk (25% for carrier couples); emphasize in consanguineous families. NSGC/ACMG genetic-counseling frameworks apply.
- **Immunization / public-health / environmental interventions:** Not applicable (non-infectious, non-environmental).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *LMAN1* and *MCFD2* are conserved in mammals. Mouse orthologs *Lman1* and *Mcfd2* have been functionally studied (see §15).
- **Natural disease in other species:** No well-characterized spontaneous F5F8D-equivalent is established in companion animals or wildlife in the reviewed literature; the disease is primarily described in humans and in engineered mouse models.
- **Comparative biology:** The LMAN1–MCFD2 cargo-receptor mechanism is evolutionarily conserved, making mouse models directly informative. A notable species difference: in mice the ER-exit defect is partial (FV/FVIII ~50% vs ~5–20% in humans), implying additional redundancy.
- **Zoonotic potential:** None (non-infectious).

---

## 15. Model Organisms

**Mouse is the principal model.**

| Model | Phenotype | Key insight | PMID |
|---|---|---|---|
| *Lman1⁻/⁻* knockout | Plasma/platelet FV and FVIII ~50% (milder than human ~5–30%); distended hepatocyte ER with accumulation of **α1-antitrypsin** and GRP78; partially penetrant, strain-dependent perinatal lethality | Confirms LMAN1 as cargo receptor; implicates additional unidentified cargoes; identifies A1AT as a co-cargo | [PMID: 21795745](https://pubmed.ncbi.nlm.nih.gov/21795745/) |
| *Lman1^cgt/cgt* hypomorph (~6–8% mRNA) | Intermediate FV/FVIII ~70% | **Dose-dependent** effect of residual LMAN1: "these results show a dose-dependent effect of residual LMAN1 on the secretion of its cargo proteins … human subjects with hypomorphic LMAN1 mutations might present with mild bleeding phenotypes" | [PMID: 33196840](https://pubmed.ncbi.nlm.nih.gov/33196840/) |
| *Lman1* conditional (tissue-specific) KO | Endothelial, not hepatocyte, FVIII loss | "Endothelial cells are the primary biosynthetic source of murine FVIII … hepatocytes make no significant contribution to the plasma FVIII pool" | [PMID: 24719406](https://pubmed.ncbi.nlm.nih.gov/24719406/) |
| *Mcfd2⁻/⁻* vs *Lman1⁻/⁻* | Distinct in vivo functions | Dissects separable roles of the two subunits | [PMID: 29735583](https://pubmed.ncbi.nlm.nih.gov/29735583/) |

**Cellular / in-vitro models:** HEK293T, HepG2, and HCT116 LMAN1- and MCFD2-deficient lines reveal cell-type-dependent secretion requirements and allow functional pathogenicity assays for candidate variants; MCFD2 overexpression rescues FV/FVIII secretion in LMAN1-null cells, establishing MCFD2 as the cargo-engaging subunit and LMAN1 as its shuttle ([PMID: 36490287](https://pubmed.ncbi.nlm.nih.gov/36490287/)). Structural models (crystallography, NMR) defined the CRD–MCFD2 interface and the FVIII B-domain binding peptide ([PMID: 20142513](https://pubmed.ncbi.nlm.nih.gov/20142513/); [PMID: 23709226](https://pubmed.ncbi.nlm.nih.gov/23709226/); [PMID: 32170195](https://pubmed.ncbi.nlm.nih.gov/32170195/)).

**Model limitations:** Mouse knockouts underrecapitulate human factor-level reduction (≈50% vs ≈5–20%), likely due to species redundancy; partially penetrant lethality and additional cargoes complicate interpretation. Cell lines capture transport biology but not whole-organism bleeding phenotypes.

---

## Mechanistic Model / Interpretation

F5F8D is best understood as a **trafficking disease masquerading as a coagulation-factor deficiency.** The single unifying lesion — loss of the LMAN1–MCFD2 cargo receptor — explains every clinical observation: (1) *why two unrelated factors fall together* (they share a transporter); (2) *why the factors are structurally normal* (synthesis is intact, export is not); (3) *why levels sit near 5–20% rather than zero* (bulk-flow and residual secretion provide a floor, and residual-LMAN1 dose modulates it); (4) *why the phenotype is mild and non-progressive* (partial, stable secretion defect); and (5) *why MCFD2 defects tend to be slightly more severe* (MCFD2 is the dedicated FV/FVIII adaptor, so its loss more directly cripples their recruitment while sparing other cargoes). The **MCFD2-is-a-recruitment-factor** finding is the linchpin that reconciles the broad cargo repertoire of LMAN1 (cathepsins, α1-antitrypsin, Mac-2BP) with the narrow, FV/FVIII-only clinical picture of F5F8D.

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [9546392](https://pubmed.ncbi.nlm.nih.gov/9546392/) | Identified ERGIC-53/*LMAN1* as first causal gene | F001 |
| [10090934](https://pubmed.ncbi.nlm.nih.gov/10090934/) | *LMAN1* mutation spectrum uniformly null (35 families) | F001 |
| [20817851](https://pubmed.ncbi.nlm.nih.gov/20817851/) | Separable MCFD2 vs cargo binding sites; oligomerization required | F002 |
| [23709226](https://pubmed.ncbi.nlm.nih.gov/23709226/) | His178, Gly251/252 cargo-binding residues | F002 |
| [20142513](https://pubmed.ncbi.nlm.nih.gov/20142513/) | 1:1 CRD–MCFD2 crystal structure; missense sites at interface | F002, F004 |
| [17010120](https://pubmed.ncbi.nlm.nih.gov/17010120/) | MCFD2 = FV/FVIII recruitment factor; MCFD2-independent cargo binding | F009 |
| [14718532](https://pubmed.ncbi.nlm.nih.gov/14718532/) | pH/Ca²⁺-triggered cargo release in ERGIC | F009 |
| [36490287](https://pubmed.ncbi.nlm.nih.gov/36490287/) | MCFD2 carries cargo; LMAN1 shuttles MCFD2 | F002 |
| [19183188](https://pubmed.ncbi.nlm.nih.gov/19183188/) | MCFD2 mutations give lower FV/FVIII than LMAN1 | F003 |
| [19141160](https://pubmed.ncbi.nlm.nih.gov/19141160/) | Factor levels 5–20%, mild-moderate bleeding; dual replacement | F003, F005 |
| [39209292](https://pubmed.ncbi.nlm.nih.gov/39209292/) | Prevalence 1:1,000,000; consanguinity enrichment | F004 |
| [15166951](https://pubmed.ncbi.nlm.nih.gov/15166951/) | Founder mutations in Jewish populations | F004 |
| [27913544](https://pubmed.ncbi.nlm.nih.gov/27913544/) | No specific FV concentrate exists | F005 |
| [33196840](https://pubmed.ncbi.nlm.nih.gov/33196840/) | Dose-dependent residual LMAN1 effect (mouse) | F006 |
| [21795745](https://pubmed.ncbi.nlm.nih.gov/21795745/) | *Lman1⁻/⁻* ~50% factors; A1AT accumulation | F006 |
| [24719406](https://pubmed.ncbi.nlm.nih.gov/24719406/) | Endothelium is FVIII source | F006 |
| [29735583](https://pubmed.ncbi.nlm.nih.gov/29735583/) | Distinct MCFD2 vs LMAN1 in-vivo roles | F006 |
| [24161289](https://pubmed.ncbi.nlm.nih.gov/24161289/) | Peripartum FVIII protocol | F007 |
| [19298378](https://pubmed.ncbi.nlm.nih.gov/19298378/) | Defect persists in pregnancy; PPH risk | F007 |
| [40296097](https://pubmed.ncbi.nlm.nih.gov/40296097/) | Defining lab pattern with normal vWF | F008 |
| [38764219](https://pubmed.ncbi.nlm.nih.gov/38764219/) | Large deletion mimics homozygous substitution | F008 |
| [27855295](https://pubmed.ncbi.nlm.nih.gov/27855295/) | EN-RBD bleeding score; inverse correlation with factor activity | F008 |
| [27894217](https://pubmed.ncbi.nlm.nih.gov/27894217/) | F5F8D milder than FXIII/FX/FVII | F010 |
| [38912355](https://pubmed.ncbi.nlm.nih.gov/38912355/) | Pediatric gum-bleeding presentation | F010 |
| [39222205](https://pubmed.ncbi.nlm.nih.gov/39222205/) | LMAN1/MCFD2 knockdown as anticoagulant — pathway validation | Context |

All findings are supported by multiple independent lines of evidence (human clinical case series, structural/biochemical studies, and mouse and cell-line genetics). No contradictory findings were identified; the main tension is the quantitative mismatch between mouse (~50%) and human (~5–20%) factor levels, attributed to species redundancy.

---

## Limitations and Knowledge Gaps

1. **Rarity-limited epidemiology.** Prevalence (~1:1,000,000) is an estimate; true incidence, age distribution, and population-specific carrier frequencies outside founder groups are poorly quantified.
2. **Genotype–phenotype resolution is coarse.** Although MCFD2 mutations trend toward lower factor levels, individual bleeding severity correlates imperfectly with factor activity, especially in pregnancy — predictive models are lacking.
3. **Incomplete cargo census.** Mouse data (perinatal lethality, A1AT accumulation) imply additional unidentified LMAN1 cargoes whose loss could contribute to subtle, under-recognized human phenotypes.
4. **Model mismatch.** Mouse knockouts do not reproduce the human factor-level depth, limiting their use for severity modeling.
5. **No disease-specific therapeutics.** FV replacement still depends on FFP; no recombinant FV product and no gene/cell therapy exist for F5F8D.
6. **QoL data are sparse.** Patient-reported outcomes, particularly the menstrual/reproductive burden in women, are under-studied.
7. **Digenic cases.** Rare coincidental *F5* + *F8* defects can phenocopy F5F8D and complicate molecular diagnosis.

---

## Proposed Follow-up Experiments / Actions

1. **Variant functional classification pipeline:** Use the established LMAN1/MCFD2-deficient cell lines ([PMID: 36490287](https://pubmed.ncbi.nlm.nih.gov/36490287/)) as a standardized rescue assay to reclassify VUS and resolve digenic vs monogenic cases.
2. **Copy-number-aware molecular testing:** Adopt routine dosage/CNV analysis of *MCFD2* and *LMAN1* to avoid misclassifying heterozygous large deletions as homozygous substitutions ([PMID: 38764219](https://pubmed.ncbi.nlm.nih.gov/38764219/)).
3. **Natural-history registry:** Pool founder-population cohorts (Tunisian, Iranian, Pakistani, Indian, Saudi) into a harmonized registry linking genotype, factor levels, ISTH-BAT/EN-RBD scores, and bleeding outcomes to build a severity-prediction model.
4. **Cargo discovery:** Proteomic profiling of LMAN1/MCFD2-null cells and conditional mouse tissues to complete the cargo census and test whether additional cargoes produce subclinical human phenotypes.
5. **Therapeutic development:** Evaluate recombinant FV products and the "passport-sequence" secretion-enhancement concept ([PMID: 32170195](https://pubmed.ncbi.nlm.nih.gov/32170195/)) as routes to a dedicated FV replacement, reducing FFP dependence.
6. **Reproductive-health protocols:** Prospectively validate individualized peripartum dual-factor protocols ([PMID: 24161289](https://pubmed.ncbi.nlm.nih.gov/24161289/)) and quantify menorrhagia-related QoL and anemia burden in affected women.
7. **Carrier screening in endogamous communities:** Offer targeted founder-allele carrier and cascade screening with genetic counseling to reduce recurrence.

---

*Report compiled from a 5-iteration autonomous investigation: 10 confirmed findings across 45 reviewed papers. Evidence spans human clinical case series, structural/biochemical studies, and mouse and cell-line genetics.*


## Artifacts

- [OpenScientist final report](Combined_Factor_V_And_Factor_VIII_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Factor_V_And_Factor_VIII_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 39 |
| On topic | 20 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:17010120` *(abstract only)*: "ERGIC-53 can bind cargo glycoproteins in an MCFD2-independent fashion and … MCFD2 is a recruitment factor for blood coagulation factors V and VIII"
  - closest text in source: "The results indicate that ERGIC-53 can bind cargo glycoproteins in an MCFD2-independent fashion and suggest that MCFD2 is a recruitment factor for blood coagulation factors V and VIII."
- `PMID:14718532` *(abstract only)*: "Acidification of cells inhibited the association of ERGIC-53 with the known cargo … and dissociation of this glycoprotein in the ERGIC was impaired by organelle neutralization"
  - closest text in source: "Acidification of cells inhibited the association of ERGIC-53 with the known cargo cathepsin Z-related protein and dissociation of this glycoprotein in the ERGIC was impaired by organelle neutralization that did not impair the transport of a control protein"
- `PMID:40296097` *(abstract only)*: "a combined deficiency of factors V and VIII at 12.4% … and 9.1%, respectively, whereas other coagulation factor levels remained within the normal range, including the antigenic activity of von Willebrand"
  - closest text in source: "Specific coagulation factor assays demonstrated a combined deficiency of factors V and VIII at 12.4% (normal range: 55-150) and 9.1% (normal range: 50-145), respectively, whereas other coagulation factor levels remained within the normal range, including the antigenic activity of von Willebrand at 71.7% (normal range: 50-150)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 29 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018175` (2 mentions) - the report calls it "MONDO"; MONDO calls it **combined deficiency of factor V and factor VIII**
- `HP:0000421` (1 mention) - the report calls it "Sign"; HP calls it **Epistaxis**
- `HP:0000225` (1 mention) - the report calls it "Sign"; HP calls it **Gingival bleeding**
- `HP:0000132` (1 mention) - the report calls it "Sign"; HP calls it **Menorrhagia**
- `HP:0011891` (1 mention) - the report calls it "Sign"; HP calls it **Post-partum hemorrhage**
- `HP:0005261` (1 mention) - the report calls it "abnormal bleeding"; HP calls it **Joint hemorrhage**
- `NCIT:C681` (1 mention) - the report calls it "plasma"; NCIT calls it **Opiate Antagonist**
- `NCIT:C1947` (1 mention) - the report calls it "Coagulation Factor VIII"; NCIT calls it **Organic Oxoacids**
- `NCIT:C29066` (1 mention) - the report calls it "Desmopressin"; NCIT calls it **Gamma Interferon-SCH**
- `NCIT:C47720` (1 mention) - the report calls it "Tranexamic Acid"; NCIT calls it **Sodium Acetate**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C29066` (Gamma Interferon-SCH) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003225` (1 mention) - the report calls it "reduced factor V activity"; HP calls it **Reduced coagulation factor V activity**, and lists "Reduced factor V activity" among its other names
- `HP:0004846` (1 mention) - the report calls it "post-surgical bleeding"; HP calls it **Prolonged bleeding after surgery**, and lists "Protracted bleeding after surgery" among its other names
- `GO:0006888` (1 mention) - the report calls it "ER-to-Golgi vesicle-mediated transport"; GO calls it **endoplasmic reticulum to Golgi vesicle-mediated transport**, and lists "ER to Golgi vesicle-mediated transport" among its other names
- `GO:0030134` (2 mentions) - the report calls it "COPII-coated ER-to-Golgi transport vesicle", "COPII vesicles"; GO calls it **COPII-coated ER to Golgi transport vesicle**, and lists "COPII vesicle" among its other names
- `GO:0005537` (1 mention) - the report calls it "mannose binding"; GO calls it **D-mannose binding**, and lists "mannose binding" among its other names
- `CL:0000182` (2 mentions) - the report calls it "hepatocyte", "Tissue/cell level:** hepatocytes"; CL calls it **hepatocyte**
- `UBERON:0001981` (2 mentions) - the report calls it "blood vessel", "blood vessel/vasculature"; UBERON calls it **blood vessel**
- `CHEBI:4208` (1 mention) - the report calls it "D-mannose"; CHEBI calls it **D-mannopyranose**, and lists "D-Mannose" among its other names
- `GO:0005793` (1 mention) - the report calls it "ER-Golgi intermediate compartment/ERGIC"; GO calls it **endoplasmic reticulum-Golgi intermediate compartment**, and lists "ER-Golgi intermediate compartment" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0030134` - called "COPII-coated ER-to-Golgi transport vesicle", "COPII vesicles"
- `CL:0000182` - called "hepatocyte", "Tissue/cell level:** hepatocytes"
- `UBERON:0001981` - called "blood vessel", "blood vessel/vasculature"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.