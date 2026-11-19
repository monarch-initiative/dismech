---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T11:35:19.039559'
end_time: '2026-10-30T11:50:16.299254'
duration_seconds: 897.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: DGKE-Associated Atypical Hemolytic Uremic Syndrome
  mondo_id: MONDO:0100590
  category: Mendelian
  causal_genes: DGKE
  omim_id: not recorded
  synonyms: aHUS type 7; DGKE nephropathy; DGKE-associated thrombotic microangiopathy
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 17
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:25135762
  relevance_assessed: 18
  on_topic: 14
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 31
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 9
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0100590
    reported_labels:
    - MONDO
    ontology_label: hemolytic uremic syndrome, atypical, susceptibility to, 7
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0001919
    reported_labels:
    - Clinical sign
    ontology_label: Acute kidney injury
  - term_id: HP:0000790
    reported_labels:
    - Lab abnormality
    ontology_label: Hematuria
  - term_id: HP:0000822
    reported_labels:
    - Clinical sign
    ontology_label: Hypertension
  - term_id: HP:0003073
    reported_labels:
    - Lab abnormality
    ontology_label: Hypoalbuminemia
  - term_id: HP:0003124
    reported_labels:
    - Lab abnormality
    ontology_label: Hypercholesterolemia
  - term_id: HP:0005339
    reported_labels:
    - Lab abnormality
    ontology_label: Abnormality of complement system
  - term_id: GO:0007205
    reported_labels:
    - DAG/PKC signaling
    ontology_label: obsolete protein kinase C-activating G protein-coupled receptor
      signaling pathway
  - term_id: CL:1000746
    reported_labels:
    - glomerular capillary endothelial cell
    - Tissue / cell level:** glomerular endothelial cells
    ontology_label: glomerular cell
  - term_id: UBERON:0004638
    reported_labels:
    - renal glomerular capillary
    ontology_label: blood vessel endothelium
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0007205
    ontology_label: obsolete protein kinase C-activating G protein-coupled receptor
      signaling pathway
    replaced_by: GO:0007200
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
  path: DGKE-Associated_Atypical_Hemolytic_Uremic_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DGKE-Associated_Atypical_Hemolytic_Uremic_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DGKE-Associated Atypical Hemolytic Uremic Syndrome
- **MONDO ID:** MONDO:0100590 (if available)
- **Causal gene(s):** DGKE
- **OMIM:** not recorded
- **Synonyms:** aHUS type 7; DGKE nephropathy; DGKE-associated thrombotic microangiopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **DGKE-Associated Atypical Hemolytic Uremic Syndrome** covering all of the
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

# DGKE-Associated Atypical Hemolytic Uremic Syndrome — Comprehensive Disease Report

**MONDO:** MONDO:0100590 · **OMIM:** #615008 (nephrotic syndrome type 7 / aHUS 7) · **Causal gene:** **DGKE** (diacylglycerol kinase epsilon; HGNC:2852) · **Category:** Mendelian (autosomal recessive)

---

## Summary

**DGKE-associated atypical hemolytic uremic syndrome (aHUS) is an autosomal-recessive, complement-independent thrombotic microangiopathy caused by biallelic loss-of-function variants in *DGKE*, the gene encoding diacylglycerol kinase epsilon (DGKε).** This distinguishes it mechanistically from the majority of aHUS cases, which arise from dysregulation of the alternative complement pathway. The causal gene — to state it explicitly in line with the research brief — is **DGKE**, a lipid kinase with *no* role in the complement cascade. The seminal exome-sequencing study of Lemaire and colleagues identified recessive *DGKE* mutations co-segregating with aHUS in nine unrelated kindreds, defining a distinctive Mendelian disease ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)).

DGKε is a small, membrane-bound, constitutively active lipid kinase that is unique among the ten mammalian DGK isoforms in its specificity for 1-stearoyl-2-arachidonoyl-*sn*-glycerol — the diacylglycerol (DAG) backbone of the phosphatidylinositol (PI) cycle. Loss of enzyme function leaves arachidonoyl-DAG elevated, which activates protein kinase C (PKC) and p38-MAPK to generate a **prothrombotic, repair-impaired endothelial state**, and simultaneously starves VEGFR2 signaling of phosphatidylinositol-4,5-bisphosphate (PIP2), collapsing the downstream Akt→COX-2→prostaglandin E2 (PGE2) axis that normally protects the glomerular microvasculature. The net result is microvascular thrombosis and podocyte/endothelial injury in the kidney.

Clinically, the disease presents in infancy (typically before 1–2 years of age) with the classic TMA triad (microangiopathic hemolytic anemia, thrombocytopenia, acute kidney injury) *plus* a distinctive nephropathy — nephrotic-range proteinuria, hematuria, and hypertension — frequently with **normal complement C3**. The course is relapsing and progresses to chronic kidney disease (CKD)/end-stage kidney disease (ESKD) in a substantial fraction of patients. Because the disease is not complement-driven, anti-C5 therapy (eculizumab) is frequently ineffective at preventing relapses, and genetic diagnosis supports de-escalation of complement blockade in favor of supportive, nephroprotective care. Restoration of the PGE2 axis reversed disease in endothelial-specific *Dgke*-knockout mice and represents the most promising mechanism-based therapeutic lead.

---

## Section 1 — Disease Information

**Overview.** DGKE-associated aHUS is an ultra-rare, infantile-onset thrombotic microangiopathy affecting principally the kidney. It belongs to the broader aHUS family but is pathogenically distinct: it is caused by loss of an intracellular lipid kinase rather than by complement dysregulation. The phenotypic spectrum overlaps with membranoproliferative glomerulonephritis (MPGN)-like injury and with isolated steroid-resistant nephrotic syndrome (SRNS), such that the same *DGKE* genotype can present as aHUS, MPGN, or SRNS ([PMID: 32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/); [PMID: 32386968](https://pubmed.ncbi.nlm.nih.gov/32386968/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0100590 |
| OMIM phenotype | #615008 (nephrotic syndrome, type 7; historically "aHUS susceptibility, type 7") |
| Causal gene | *DGKE* (HGNC:2852; NCBI Gene 8526; Ensembl ENSG00000153747) |
| Orphanet | aHUS / rare renal TMA (ORPHA:2134 family) |
| ICD-10 / ICD-11 | D59.3 (hemolytic-uremic syndrome) / 3A21.2 |
| MeSH | Atypical Hemolytic Uremic Syndrome |

**Synonyms / alternative names.** aHUS type 7; DGKE nephropathy; DGKE-associated thrombotic microangiopathy; diacylglycerol kinase epsilon nephropathy.

**Information source type.** Evidence is derived from *aggregated disease-level resources* — primarily small, international case series, national cohorts/registries, and mechanistic model-organism and in vitro studies — rather than from large individual-patient EHR datasets, reflecting the disease's rarity.

---

## Section 2 — Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound-heterozygous) loss-of-function variants in *DGKE*. Lemaire et al. identified recessive *DGKE* mutations in nine unrelated kindreds ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)). This is a monogenic, fully genetic etiology; there is no established infectious or primary environmental cause.

**Genetic risk factors / modifiers.** The disease itself is recessive and Mendelian, but *co-inherited complement variants* can modify onset and severity. In the Spanish aHUS registry, among patients with *DGKE* mutations, several also carried heterozygous variants in thrombomodulin (*THBD*) or *C3*, and complement dysregulation appeared to "influence the onset and disease severity in carriers of diacylglycerol kinase-ε mutations" ([PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)). Thus complement genes act as potential *modifiers* rather than primary causes.

**Environmental / triggering factors.** As in other TMAs, intercurrent infections and, in reported cases, pregnancy can act as triggers or relapse precipitants; one DGKE mutation was identified in a pregnancy-related TMA cohort ([PMID: 40306205](https://pubmed.ncbi.nlm.nih.gov/40306205/)). Age (infancy) is the dominant demographic risk window.

**Protective factors.** No validated genetic or environmental protective factors have been defined for this ultra-rare monogenic disease. *Information not available.*

**Gene–environment interactions.** The principal documented interaction is between the causal *DGKE* genotype and *modifier complement genotype/triggers*, which together shape clinical expressivity ([PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)).

---

## Section 3 — Phenotypes

Core phenotypes, with suggested HPO terms, drawn from Lemaire 2013 and the nationwide DGKε nephropathy cohort (n=12; [PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)):

| Phenotype | Type | HPO term | Frequency (cohort) | Onset / course |
|---|---|---|---|---|
| Microangiopathic hemolytic anemia | Lab abnormality | HP:0001937 (thrombotic microangiopathy); HP:0004809 | 11/12 | Infantile; episodic |
| Thrombocytopenia | Lab abnormality | HP:0001873 | common | Infantile; episodic |
| Acute kidney injury | Clinical sign | HP:0001919 | common | Infantile |
| Nephrotic-range proteinuria | Lab abnormality | HP:0012593 / HP:0000100 | 10/12 | Persistent; relapsing |
| Microscopic hematuria | Lab abnormality | HP:0000790 | 10/12 | Persistent |
| Hypertension | Clinical sign | HP:0000822 | ~40% at follow-up | Persistent |
| Hypoalbuminemia | Lab abnormality | HP:0003073 | 6/12 | — |
| Hypercholesterolemia | Lab abnormality | HP:0003124 | 6/12 | — |
| Hypocomplementemia (low C3) | Lab abnormality | HP:0005339 | 4/12 (minority) | Variable |
| Chronic kidney disease / ESKD | Clinical outcome | HP:0012622 / HP:0003774 | 60% death-or-CKD at 3.3 y | Progressive |

**Characteristics.** Age of onset is **neonatal-to-infantile**: "Patients presented at a median age of 11 (7.5, 12.3) months; all were younger than 2 years" ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)); Lemaire noted affected individuals "present with aHUS before age 1 year" ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)). Severity is moderate-to-severe and variable; progression is **episodic/relapsing on a progressive background** ("relapses (66.7%)... death or progression to CKD (60%)"). A notable feature is that complement C3 is **typically normal**, unlike complement-mediated aHUS, though a minority show low C3.

**Quality-of-life impact.** Disease-specific QoL instruments have not been applied in this ultra-rare population, but the burden is substantial: lifelong CKD/dialysis dependence, growth and developmental impact of infantile kidney disease, relapse surveillance, and transplant considerations. *Formal QoL metrics not available.*

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *DGKE* (chromosome 17q22), encoding diacylglycerol kinase epsilon, a 64-kDa lipid kinase. **Inheritance is autosomal recessive**; disease requires two loss-of-function alleles.

**Pathogenic variant spectrum.** Variants span the gene and include missense, frameshift, nonsense, and splice-site classes. In a 12-patient cohort, 13 homozygous/compound-heterozygous variants were reported (7 pathogenic, 3 likely pathogenic by ACMG/AMP criteria), 11 of which were novel ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)). Recurrent/illustrative alleles include:

- **c.966G>A, p.Trp322Ter** (nonsense) — recurrent; reported homozygous in SRNS and compound-heterozygous in aHUS ([PMID: 32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/)).
- **c.171delG, p.Ser58Alafs\*111** (frameshift) ([PMID: 32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/)).
- **p.His536Qfs\*16** (homozygous frameshift); **p.Trp322\*/p.Pro498Arg** and **p.Gln248His/p.Gly484Glyfs\*10** (compound heterozygous) ([PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)).

**Variant classification & frequency.** Pathogenic alleles are individually ultra-rare in gnomAD, consistent with a recessive, severe pediatric phenotype. **Origin is germline**; no somatic contribution is described.

**Functional consequence.** Variants are **loss-of-function** (enzyme-dead). Lemaire et al. inferred that "loss of DGKE function results in a prothrombotic state" ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)). Mechanistically this is a true loss-of-function (not dominant-negative), consistent with recessive inheritance.

**Modifier genes.** Heterozygous complement variants (*THBD*, *C3*, *CFI*) can co-occur and modify severity/treatment response ([PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/); [PMID: 38374836](https://pubmed.ncbi.nlm.nih.gov/38374836/)).

**Epigenetic information / chromosomal abnormalities.** No disease-specific methylation signature or large-scale cytogenetic abnormality has been described. *Not applicable / not available.*

---

## Section 5 — Environmental Information

- **Environmental toxins/pollution/radiation/occupational exposure:** none established. *Not applicable.*
- **Lifestyle factors:** none established (disease onsets in infancy). *Not applicable.*
- **Infectious agents:** The disease is *not* caused by Shiga-toxin–producing *E. coli* (which causes typical HUS). Infections may act as non-specific relapse triggers, as in other TMAs, but no specific pathogen is causal. The defining distinction from typical HUS is the absence of a Shiga-toxin etiology.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function mutation in *DGKE*** *leads to* absent/non-functional diacylglycerol kinase epsilon protein in cells that normally express it (endothelium, podocytes, platelets). *(Demonstrated: [PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/).)*
2. Loss of the only arachidonoyl-DAG–specific kinase *results in* **accumulation of 1-stearoyl-2-arachidonoyl-DAG** and **failure to regenerate phosphatidylinositol/PIP2** via the PI cycle. *(Demonstrated biochemically: [PMID: 27803897](https://pubmed.ncbi.nlm.nih.gov/27803897/); [PMID: 38008259](https://pubmed.ncbi.nlm.nih.gov/38008259/).)*

   **Branch A — prothrombotic/proinflammatory endothelium:**
3A. Elevated arachidonoyl-DAG *activates* **protein kinase C (PKC)** and **p38-MAPK**. *(Inferred from Lemaire; demonstrated in endothelial cells: [PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/); [PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/).)*
4A. PKC/p38-MAPK signaling *upregulates* **tissue factor and ICAM-1**, promotes endothelial activation, apoptosis, and impaired angiogenesis, *resulting in* a **prothrombotic, proinflammatory endothelial surface** — *without complement deposition*. *(Demonstrated in vitro: [PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/).)*

   **Branch B — loss of endothelial protective signaling:**
3B. PIP2 shortage *impairs* **VEGFR2 signaling** (VEGFA pathway) downstream of the receptor. *(Demonstrated in vivo: [PMID: 33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/).)*
4B. Failed VEGFR2→**Akt** activation *reduces* **COX-2** expression and **PGE2** production. *(Demonstrated: [PMID: 33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/); [PMID: 26887830](https://pubmed.ncbi.nlm.nih.gov/26887830/).)*
5. Branches A and B converge: a prothrombotic, repair-deficient glomerular microvasculature *leads to* **microvascular/capillary thrombosis, endothelial swelling, and podocyte injury** (thrombotic microangiopathy + nephrotic-range proteinuria).
6. Glomerular TMA *results in* the **clinical triad** (hemolytic anemia from mechanical RBC shearing, platelet consumption/thrombocytopenia, acute kidney injury) *plus* proteinuria, hematuria, and hypertension.
7. Recurrent injury *leads to* **chronic kidney disease / ESKD** over time.

### Diagram

```
 DGKE LoF (biallelic)
        │
        ▼
 ↑ arachidonoyl-DAG  +  ↓ PI/PIP2 regeneration (PI cycle broken)
        │                         │
   ┌────┘                         └──────────┐
   ▼ Branch A                                 ▼ Branch B
 PKC / p38-MAPK ↑                     VEGFR2 signaling ↓ (PIP2 shortage)
   │                                          │
 Tissue factor ↑, ICAM-1 ↑             Akt ↓ → COX-2 ↓ → PGE2 ↓
 EC activation/apoptosis                      │
   │                                          │
   └──────────► prothrombotic, repair-impaired glomerular endothelium ◄──┘
                              │
                              ▼
          Microvascular thrombosis + podocyte injury (TMA + proteinuria)
                              │
                              ▼
        MAHA + thrombocytopenia + AKI + hematuria + hypertension
                              │
                              ▼
                        CKD / ESKD (progressive)
```

### Supporting detail
- **Molecular pathways:** PI cycle (lipid resynthesis); DAG–PKC signaling; p38-MAPK; VEGFA–VEGFR2→PI3K–Akt; COX-2/prostaglandin (PGE2) axis.
- **Cellular processes:** endothelial activation, apoptosis, impaired angiogenesis/migration, platelet activation, podocyte dysfunction, microthrombosis.
- **Protein dysfunction:** complete loss of a constitutively active lipid kinase (catalytic/expression loss-of-function, not misfolding-aggregation).
- **Immune involvement:** **complement-independent** — a defining feature. Bruneau et al. showed endothelial activation and death "independently of complement activation": "loss of DGKε expression/activity in EC induces an increase in ICAM-1 and tissue factor expression through the upregulation of p38-MAPK-mediated signals" ([PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/)).
- **GO term suggestions:** GO:0004143 (diacylglycerol kinase activity), GO:0006661 (phosphatidylinositol biosynthetic process), GO:0007205 (DAG/PKC signaling), GO:0038084 (VEGF signaling), GO:0007596 (blood coagulation), GO:0001525 (angiogenesis).
- **CL term suggestions:** CL:0000115 (endothelial cell), CL:1000746 (glomerular capillary endothelial cell), CL:0000653 (podocyte), CL:0000233 (platelet).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** kidney — glomerulus (UBERON:0000074), renal glomerular capillary/endothelium.
- **Secondary / systemic:** microvasculature broadly; hematologic effects (hemolysis, thrombocytopenia). Rare extrarenal TMA features may occur but renal involvement dominates.
- **Body systems:** urinary/renal; hematologic; cardiovascular (microvascular, hypertension).
- **Tissue / cell level:** glomerular endothelial cells (CL:1000746), podocytes (CL:0000653), platelets (CL:0000233). Histology shows TMA and, in a subset, MPGN-like changes ([PMID: 32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/)).
- **Subcellular compartments:** endoplasmic reticulum and Golgi (DGKε is S-palmitoylated at Cys38/40 and localizes to the ER; [PMID: 38008259](https://pubmed.ncbi.nlm.nih.gov/38008259/)); plasma membrane (PI-cycle lipid signaling). GO cellular-component terms: GO:0005789 (ER membrane), GO:0005886 (plasma membrane).
- **UBERON suggestions:** UBERON:0002113 (kidney), UBERON:0000074 (renal glomerulus), UBERON:0004638 (renal glomerular capillary).
- **Lateralization:** bilateral (systemic genetic disease; both kidneys).

---

## Section 8 — Temporal Development

- **Onset:** congenital/infantile — median ~11 months, essentially all before age 2 years ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/); [PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)). Onset pattern is acute (TMA episode) on a chronic genetic background.
- **Progression / course:** relapsing-remitting superimposed on a progressive decline. Relapses occurred in ~66.7% and death/CKD progression in ~60% at median 3.3-year follow-up ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)). A notable natural-history feature is that acute TMA episodes may diminish after early childhood while proteinuria/CKD persists.
- **Disease duration:** chronic, lifelong.
- **Remission patterns:** both spontaneous and treatment-associated remissions are reported, but relapses are common; notably, relapses can occur **as isolated nephrotic-range proteinuria** during or despite C5 blockade ([PMID: 42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/); [PMID: 33879077](https://pubmed.ncbi.nlm.nih.gov/33879077/)).
- **Critical period:** infancy/early childhood is the window of greatest vulnerability and the key period for diagnosis and nephroprotective intervention.

---

## Section 9 — Inheritance and Population

- **Epidemiology / incidence:** ultra-rare. UK registry data defined the incidence of **DGKE aHUS at 0.009/million/year** and **DGKE "MPGN" at 0.006/million/year**, a combined **0.015/million/year** ([PMID: 32386968](https://pubmed.ncbi.nlm.nih.gov/32386968/)). In early-onset (<2 years) aHUS cohorts, *DGKE* mutations account for a meaningful minority — e.g., 4/83 in the Spanish registry ([PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)).
- **Inheritance pattern:** autosomal recessive.
- **Penetrance:** high/complete for the renal phenotype in biallelic carriers (with variable expressivity across aHUS/MPGN/SRNS presentations).
- **Expressivity:** variable — same genotype can yield aHUS, MPGN-like disease, or isolated SRNS ([PMID: 32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/)).
- **Consanguinity:** homozygous cases in consanguineous or founder settings are reported; consanguinity increases recessive risk.
- **Anticipation / mosaicism / founder effects:** no repeat-expansion anticipation; no specific founder mutation established, though recurrent alleles (e.g., p.Trp322Ter) exist. Carrier frequency is low (ultra-rare alleles).
- **Demographics:** reported across multiple ethnicities worldwide; no strong sex bias documented for this monogenic disease. Age distribution is strongly skewed to infancy.

---

## Section 10 — Diagnostics

**Clinical/laboratory signature.** The diagnostic trigger is **infantile aHUS (TMA triad) accompanied by nephrotic-range proteinuria/hematuria and typically normal complement C3**. "For infants and young children with aHUS in conjunct with nephrotic level proteinuria, variants of the DGKE gene should be screened" ([PMID: 37994143](https://pubmed.ncbi.nlm.nih.gov/37994143/)).

**Core labs:** CBC with schistocytes, low haptoglobin, elevated LDH, indirect hyperbilirubinemia (hemolysis); thrombocytopenia; elevated creatinine; urinalysis (proteinuria, hematuria); serum albumin (low), cholesterol (elevated); complement C3/C4 (usually normal); ADAMTS13 activity (to exclude TTP); stool studies/Shiga toxin (to exclude STEC-HUS).

**Biopsy/pathology:** renal biopsy shows thrombotic microangiopathy; a subset shows MPGN-like glomerular changes ([PMID: 32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/)).

**Genetic testing (definitive).** Molecular confirmation requires ***DGKE* sequencing**, best delivered via a **targeted aHUS/TMA gene panel** that includes *DGKE* alongside complement genes (*CFH*, *CFHR1–5*, *CFI*, *CD46/MCP*, *C3*, *CFB*, *THBD*) and, where panels are negative, whole-exome sequencing (as in the original discovery). MLPA of the CFH-CFHR region is useful to characterize co-modifiers. Chromosomal microarray, karyotyping, FISH, mtDNA, and repeat-expansion testing are *not applicable*.

**Clinical criteria / differential diagnosis.** Must distinguish from (1) complement-mediated aHUS (low C3 more typical, complement variants, often eculizumab-responsive), (2) STEC/typical HUS (preceding bloody diarrhea, Shiga toxin), (3) TTP (ADAMTS13 <10%), and (4) secondary TMA. The combination of infantile onset + heavy proteinuria + normal C3 points to *DGKE* ([PMID: 37994143](https://pubmed.ncbi.nlm.nih.gov/37994143/)).

**Screening.** Cascade genetic testing of at-risk siblings and carrier testing of parents (recessive); no population newborn screen exists.

---

## Section 11 — Outcome / Prognosis

- **Renal outcomes:** guarded. ~60% death or progression to CKD and ~67% relapse at median 3.3 years ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)); persistent hypertension/proteinuria in ~40%.
- **Natural history nuance:** acute TMA episodes may attenuate after early childhood, but proteinuria and progressive CKD persist, so long-term prognosis is dominated by nephropathy rather than recurrent hemolytic crises ([PMID: 32386968](https://pubmed.ncbi.nlm.nih.gov/32386968/)).
- **Mortality:** disease-specific mortality is low relative to morbidity; the dominant adverse outcome is ESKD requiring dialysis/transplant.
- **Transplant:** because the defect is intrinsic to kidney cells (endothelium/podocytes) and is **not** circulating-complement-mediated, post-transplant TMA recurrence risk is expected to be lower than in complement-mediated aHUS — an important prognostic/therapeutic distinction (mechanistic inference supported by the cell-intrinsic, complement-independent biology; [PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/)).
- **Prognostic factors:** degree/persistence of proteinuria, hypertension control, baseline GFR, relapse frequency, and co-inherited complement variants (worse with complement modifiers; [PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)).

---

## Section 12 — Treatment

**Overarching principle:** DGKE aHUS is **complement-independent**, so complement blockade is often ineffective at preventing relapses; genotype-guided care emphasizes nephroprotection and de-escalation of unnecessary anti-C5 therapy.

- **Complement inhibition (eculizumab / ravulizumab; NCIT: Eculizumab C88248).** Widely used empirically at presentation before genotype is known. Evidence is mixed: some patients with low C3 appear to respond ([PMID: 33879077](https://pubmed.ncbi.nlm.nih.gov/33879077/); [PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)), but relapses occur **despite** C5 blockade in the absence of complement activation — "eculizumab did not prevent disease relapses, which occurred in the absence of complement activation" ([PMID: 42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/)). Genetic confirmation supports discontinuation/de-escalation to avoid overtreatment: "The lack of genetic testing options has led to overtreatment in this patient" ([PMID: 42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/)).
- **Nephroprotection (first-line for the chronic phase).** RAAS blockade (ACE inhibitors/ARBs) for proteinuria and hypertension; blood-pressure control; supportive care for CKD.
- **Plasma therapy.** Plasma infusion/exchange has controlled recurrences in some patients, particularly those with co-existing complement/THBD variants ([PMID: 25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/)).
- **Antithrombotic strategies.** Given the prothrombotic mechanism (tissue factor/PKC), antiplatelet/anticoagulant approaches are a rational consideration, though not formally validated.
- **Mechanism-based / experimental.** Restoration of the PGE2 axis is the leading targeted concept: a **stable PGE2 analog reversed TMA and proteinuria** in endothelial-specific *Dgke*-knockout mice ([PMID: 33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/)). This is preclinical; no human trial yet.
- **Renal replacement / transplant.** Dialysis and kidney transplantation for ESKD; recurrence risk appears lower than complement-mediated aHUS (see Prognosis).
- **Pharmacogenomics:** none established.

**NCIT term suggestions:** Eculizumab (C88248), ACE Inhibitor (C705)/Angiotensin Receptor Antagonist, Plasmapheresis/Plasma Exchange (C50785), Kidney Transplantation (C15366), Dialysis (C15248).

---

## Section 13 — Prevention

- **Primary prevention:** not possible for a monogenic recessive disease beyond reproductive counseling. **Genetic counseling** for consanguineous/carrier families; options include carrier testing, prenatal testing, and preimplantation genetic diagnosis (recessive, 25% recurrence risk per pregnancy).
- **Secondary prevention:** early recognition of infantile aHUS with heavy proteinuria and prompt *DGKE* sequencing to enable early nephroprotection and to avoid overtreatment with complement inhibitors ([PMID: 37994143](https://pubmed.ncbi.nlm.nih.gov/37994143/); [PMID: 42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/)); cascade testing of siblings.
- **Tertiary prevention:** aggressive BP/proteinuria control to slow CKD; relapse surveillance; **meningococcal vaccination** is required for any patient placed on eculizumab (anti-C5 therapy increases meningococcal risk; [PMID: 27811836](https://pubmed.ncbi.nlm.nih.gov/27811836/)).
- **Public-health / environmental interventions:** not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Orthologous gene:** mouse *Dgke* (NCBI Gene 56077); orthologs conserved across vertebrates. DGKε's arachidonoyl specificity and PI-cycle role are evolutionarily conserved ([PMID: 27803897](https://pubmed.ncbi.nlm.nih.gov/27803897/)).
- **Naturally occurring disease in other species:** no naturally occurring DGKE nephropathy has been documented in companion animals or wildlife (OMIA search not productive). *Not available.*
- **Comparative biology:** engineered mouse models (below) faithfully reproduce the endothelial TMA mechanism, supporting conservation of the pathway.
- **Zoonotic potential / transmission:** none (genetic disease).

---

## Section 15 — Model Organisms

| Model | Type | Key phenotype | Recapitulation | Reference |
|---|---|---|---|---|
| Endothelial-specific *Dgke*-knockout mouse | Mammalian, conditional KO | TMA + proteinuria; impaired VEGFR2→Akt→COX-2→PGE2; **reversed by stable PGE2 analog** | High — reproduces renal TMA and identifies druggable axis | [PMID: 33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/) |
| Global *Dgke*-knockout mouse | Mammalian, constitutive KO | Endothelial distress; impaired glomerular Cox-2 and PGE2 production | Moderate–high (mechanistic) | [PMID: 26887830](https://pubmed.ncbi.nlm.nih.gov/26887830/) |
| DGKε-knockdown human endothelial cells | In vitro cellular | ↑ICAM-1/tissue factor via p38-MAPK; ↑apoptosis; impaired migration/angiogenesis; **no complement deposition** | Mechanism of complement-independent EC injury | [PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/) |
| Recombinant purified DGKε / DGKεΔ40 | In vitro biochemical | Confirms arachidonoyl specificity, constitutive activity | Enzyme-function model | [PMID: 28199087](https://pubmed.ncbi.nlm.nih.gov/28199087/) |

**Model applications:** dissecting the endothelial VEGFR2–PGE2 axis, testing PGE2-based and antithrombotic therapeutics, and validating complement-independence. **Limitations:** mouse models may not fully capture the human proteinuric/podocyte spectrum or the aHUS/MPGN/SRNS phenotypic overlap; in vitro knockdown lacks organ-level hemodynamics. **Resources:** MGI (*Dgke*), standard conditional-KO repositories.

---

## Key Findings (with evidence)

### Finding 1 — Recessive, complement-independent Mendelian disease caused by biallelic *DGKE* loss-of-function
Exome sequencing identified recessive *DGKE* mutations co-segregating with aHUS in nine unrelated kindreds, and the authors stated they "identified recessive mutations in DGKE (encoding diacylglycerol kinase ɛ) that co-segregated with aHUS in nine unrelated kindreds, defining a distinctive Mendelian disease" ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)). DGKε has no role in complement; variants span missense, frameshift, nonsense, and splice classes; a 12-patient cohort reported 13 biallelic variants (7 pathogenic, 3 likely pathogenic, 11 novel) ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)). Lemaire explicitly inferred that "loss of DGKE function results in a prothrombotic state."

### Finding 2 — Mechanism: prothrombotic endothelium via DAG/PKC + collapse of VEGFR2→COX-2→PGE2 signaling
DGKε is arachidonoyl-DAG specific and recycles phosphatidylinositol; its loss elevates arachidonoyl-DAG, activating PKC/p38-MAPK and upregulating tissue factor and ICAM-1 ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/); [PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/)). In endothelial-specific *Dgke*-KO mice, "loss of Dgke in the endothelium results in impaired signaling downstream of VEGFR2 due to cellular shortage of phosphatidylinositol 4,5-biphosphate," and "treating the endothelial specific Dgke-knockout mice with a stable PGE2 analog was sufficient to reverse the clinical manifestations of thrombotic microangiopathy and proteinuria" ([PMID: 33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/)).

### Finding 3 — Infantile-onset nephropathy with proteinuria and progression to CKD
"Patients presented at a median age of 11 (7.5, 12.3) months; all were younger than 2 years," and at median 3.3-year follow-up "significant hypertension and/or proteinuria (40%), relapses (66.7%), and death or progression to CKD (60%) were common" ([PMID: 36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/)). Lemaire: affected individuals "present with aHUS before age 1 year, have persistent hypertension, hematuria and proteinuria (sometimes in the nephrotic range), and develop chronic kidney disease with age" ([PMID: 23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/)).

### Finding 4 — Ultra-rare; eculizumab efficacy controversial
"We defined the incidence of DGKE aHUS as 0.009/million/year and so-called DGKE MPGN as 0.006/million/year, giving a combined incidence of 0.015/million/year" ([PMID: 32386968](https://pubmed.ncbi.nlm.nih.gov/32386968/)). "Eculizumab did not prevent disease relapses, which occurred in the absence of complement activation" ([PMID: 42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/)).

### Finding 5 — Models recapitulate endothelial TMA and are pharmacologically rescuable
Endothelial-specific KO mice develop TMA/proteinuria reversible by a PGE2 analog ([PMID: 33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/)); global KO mice show impaired glomerular Cox-2/PGE2 ([PMID: 26887830](https://pubmed.ncbi.nlm.nih.gov/26887830/)); DGKε-knockdown endothelial cells activate without complement deposition ([PMID: 25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/)).

### Finding 6 — DGKε is a uniquely arachidonoyl-specific, constitutively active PI-cycle lipid kinase
"It is the only DGK isoform with specificity for a particular species of DAG, i.e., 1-stearoyl-2-arachidonoyl glycerol" ([PMID: 27803897](https://pubmed.ncbi.nlm.nih.gov/27803897/)); "DGKε is involved in the PI cycle maintaining the cellular level of phosphorylated PI derivatives of signaling activity" ([PMID: 38008259](https://pubmed.ncbi.nlm.nih.gov/38008259/)). Its substrate selectivity (LOX-like motif) explains the disease's lipid-signaling selectivity ([PMID: 22266092](https://pubmed.ncbi.nlm.nih.gov/22266092/); [PMID: 28199087](https://pubmed.ncbi.nlm.nih.gov/28199087/)).

### Finding 7 — Diagnostic signature + genotype-guided management
Infantile onset + TMA + nephrotic-range proteinuria/hematuria + normal C3 + MPGN-like histology → sequence *DGKE*: "For infants and young children with aHUS in conjunct with nephrotic level proteinuria, variants of the DGKE gene should be screened" ([PMID: 37994143](https://pubmed.ncbi.nlm.nih.gov/37994143/)). Genetic diagnosis prevents overtreatment with complement blockade — "the lack of genetic testing options has led to overtreatment in this patient" ([PMID: 42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/)).

---

## Mechanistic Model / Interpretation

The disease is best understood as a **cell-intrinsic lipid-signaling failure** of the glomerular microvasculature. DGKε sits at a single, non-redundant node in the phosphatidylinositol cycle, uniquely handling the arachidonoyl-DAG that is the PI backbone. When that node fails, two consequences propagate in parallel: (i) a **gain of a prothrombotic/proinflammatory program** (DAG→PKC/p38-MAPK→tissue factor/ICAM-1, with endothelial apoptosis), and (ii) a **loss of a protective program** (PIP2 depletion→VEGFR2→Akt→COX-2→PGE2). The convergence of "more thrombosis, less repair" on the glomerular endothelium and podocyte explains the simultaneous TMA *and* heavy proteinuria that make this entity clinically distinctive. The **absence of complement involvement** is the organizing clinical fact: it explains the typically normal C3, the frequent failure of eculizumab to prevent relapses, and the rationale for genotype-guided de-escalation. The model is strongly supported because the critical protective node (PGE2) is both necessary (lost in KO mice) and sufficient (its pharmacologic restoration reverses disease) — an unusually complete causal demonstration for a rare disease.

---

## Evidence Base

| PMID | Role | How it supports / challenges findings |
|---|---|---|
| [23542698](https://pubmed.ncbi.nlm.nih.gov/23542698/) | Landmark human-genetics [H] | Defines DGKE as recessive causal gene; infers prothrombotic LOF mechanism |
| [36988693](https://pubmed.ncbi.nlm.nih.gov/36988693/) | Nationwide cohort [H] | Quantifies onset (median 11 mo), phenotype frequencies, outcomes |
| [32386968](https://pubmed.ncbi.nlm.nih.gov/32386968/) | UK registry [H] | Incidence 0.015/million/yr; long-term outcomes, treatment response |
| [25135762](https://pubmed.ncbi.nlm.nih.gov/25135762/) | Spanish registry [H] | Complement modifiers influence onset/severity; plasma/complement therapy useful with co-variants |
| [33986189](https://pubmed.ncbi.nlm.nih.gov/33986189/) | Endothelial KO mouse [M] | Establishes VEGFR2→PGE2 mechanism; PGE2 analog reverses disease |
| [26887830](https://pubmed.ncbi.nlm.nih.gov/26887830/) | Global KO mouse [M] | Impaired glomerular Cox-2/PGE2 corroborates mechanism |
| [25498910](https://pubmed.ncbi.nlm.nih.gov/25498910/) | In vitro endothelial [V] | Complement-independent EC activation via p38-MAPK/tissue factor/ICAM-1 |
| [27803897](https://pubmed.ncbi.nlm.nih.gov/27803897/) | Biochemistry review [V/C] | Unique arachidonoyl substrate specificity |
| [38008259](https://pubmed.ncbi.nlm.nih.gov/38008259/) | Biochemistry [V] | S-palmitoylation; ER localization; PI-cycle role |
| [28199087](https://pubmed.ncbi.nlm.nih.gov/28199087/) | Protein purification [V] | Confirms acyl specificity; links LOF to aHUS |
| [22266092](https://pubmed.ncbi.nlm.nih.gov/22266092/) | Mutagenesis [V] | LOX-like motif governs acyl-chain selectivity |
| [42077707](https://pubmed.ncbi.nlm.nih.gov/42077707/) | Case report [H] | Eculizumab fails to prevent relapses; supports de-escalation |
| [33879077](https://pubmed.ncbi.nlm.nih.gov/33879077/) | Case report [H] | Low-C3 patient apparently eculizumab-responsive — nuance/challenge |
| [32413569](https://pubmed.ncbi.nlm.nih.gov/32413569/) | Case series [H] | aHUS/SRNS phenotypic overlap; variable histology |
| [37994143](https://pubmed.ncbi.nlm.nih.gov/37994143/) | Case/guidance [H] | Diagnostic trigger: infantile aHUS + nephrotic proteinuria → sequence DGKE |
| [38374836](https://pubmed.ncbi.nlm.nih.gov/38374836/) | Case report [H] | DGKE + CFI heterozygous variants — modifier concept |

---

## Limitations and Knowledge Gaps

- **Small sample sizes.** All clinical data derive from small case series/registries (largest cohorts ~12 patients); frequencies and outcome percentages carry wide uncertainty.
- **Phenotype–genotype correlation is incomplete.** Why the same *DGKE* genotype produces aHUS vs MPGN vs isolated SRNS is unresolved; modifier contributions (complement variants, triggers) are only partly characterized.
- **Eculizumab evidence is anecdotal and conflicting.** No randomized data exist; apparent responses in low-C3 patients may reflect co-modifiers.
- **PGE2 therapy is preclinical.** The compelling mouse rescue has not been translated to humans; dosing, delivery, and safety in infants are unknown.
- **Transplant recurrence risk** is inferred from mechanism rather than established by large transplant cohorts.
- **QoL, natural history beyond childhood, and adult outcomes** are poorly documented.

---

## Proposed Follow-up Experiments / Actions

1. **International DGKE nephropathy registry** with harmonized genotype, histology, complement status, treatment, and long-term renal outcomes to firm up frequencies and genotype–phenotype correlations.
2. **Prospective / structured evaluation of complement-inhibitor withdrawal** in genetically confirmed DGKE patients, to formalize de-escalation guidance.
3. **Translational development of PGE2-axis therapeutics** (stable PGE2 analogs or EP-receptor agonists) toward first-in-human studies, building on the KO-mouse rescue.
4. **Mechanistic dissection of the aHUS/MPGN/SRNS branch point**, including podocyte-specific *Dgke* models and single-cell profiling of glomerular cell types.
5. **Evaluate antithrombotic/PKC-directed strategies** in model systems given the tissue-factor/PKC arm of the mechanism.
6. **Define post-transplant recurrence risk** through multicenter transplant-cohort analysis.

---

*Evidence source types: human clinical (PMIDs 23542698, 36988693, 32386968, 25135762, 32413569, 42077707, 33879077, 37994143, 38374836); model organism (33986189, 26887830); in vitro cellular (25498910); in vitro biochemical/structural (27803897, 38008259, 28199087, 22266092).*


## Artifacts

- [OpenScientist final report](DGKE-Associated_Atypical_Hemolytic_Uremic_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DGKE-Associated_Atypical_Hemolytic_Uremic_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:25135762` *(abstract only)*: "influence the onset and disease severity in carriers of diacylglycerol kinase-ε mutations"
  - closest text in source: "CONCLUSIONS: Data suggest that complement dysregulation influences the onset and disease severity in carriers of diacylglycerol kinase-ε mutations and that treatments on the basis of plasma infusions and complement inhibition are potentially useful in patients with combined diacylglycerol kinase-ε and complement mutations"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100590` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hemolytic uremic syndrome, atypical, susceptibility to, 7**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0001919` (1 mention) - the report calls it "Clinical sign"; HP calls it **Acute kidney injury**
- `HP:0000790` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hematuria**
- `HP:0000822` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypertension**
- `HP:0003073` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypoalbuminemia**
- `HP:0003124` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypercholesterolemia**
- `HP:0005339` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Abnormality of complement system**
- `GO:0007205` (1 mention) - the report calls it "DAG/PKC signaling"; GO calls it **obsolete protein kinase C-activating G protein-coupled receptor signaling pathway**
- `CL:1000746` (2 mentions) - the report calls it "glomerular capillary endothelial cell", "Tissue / cell level:** glomerular endothelial cells"; CL calls it **glomerular cell**
- `UBERON:0004638` (1 mention) - the report calls it "renal glomerular capillary"; UBERON calls it **blood vessel endothelium**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007205` (obsolete protein kinase C-activating G protein-coupled receptor signaling pathway) (1 mention) - replaced by `GO:0007200`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004143` (1 mention) - the report calls it "diacylglycerol kinase activity"; GO calls it **ATP-dependent diacylglycerol kinase activity**, and lists "diacylglycerol kinase activity" among its other names
- `UBERON:0000074` (2 mentions) - the report calls it "Primary organ:** kidney — glomerulus", "renal glomerulus"; UBERON calls it **renal glomerulus**, and lists "Malphigian glomerulus" among its other names
- `GO:0005789` (1 mention) - the report calls it "ER membrane"; GO calls it **endoplasmic reticulum membrane**, and lists "ER membrane" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:1000746` - called "glomerular capillary endothelial cell", "Tissue / cell level:** glomerular endothelial cells"
- `UBERON:0000074` - called "Primary organ:** kidney — glomerulus", "renal glomerulus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.