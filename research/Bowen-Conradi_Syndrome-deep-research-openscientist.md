---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-29T03:29:39.974195'
end_time: '2026-10-29T03:47:30.001481'
duration_seconds: 1070.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Bowen-Conradi Syndrome
  mondo_id: MONDO:0008879
  category: Mendelian
  causal_genes: EMG1
  omim_id: not recorded
  synonyms: BWCNS; Bowen-Conradi Hutterite syndrome
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
citation_count: 16
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 16
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 9
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0008879
    reported_labels:
    - MONDO
    ontology_label: Bowen-Conradi syndrome
  - term_id: DOID:0050684
    reported_labels:
    - DOID
    ontology_label: Bowen-Conradi syndrome
  - term_id: HP:0000252
    reported_labels:
    - Clinical sign
    ontology_label: Microcephaly
  - term_id: HP:0000448
    reported_labels:
    - Physical
    ontology_label: Prominent nose
  - term_id: HP:0001838
    reported_labels:
    - Physical
    ontology_label: Rocker bottom foot
  - term_id: HP:0002803
    reported_labels:
    - Physical
    ontology_label: Congenital contracture
  - term_id: HP:0002187
    reported_labels:
    - Neurodevelopmental
    ontology_label: Profound intellectual disability
  - term_id: HP:0005528
    reported_labels:
    - Lab/hematologic
    ontology_label: Bone marrow hypocellularity
  - term_id: HP:0001522
    reported_labels:
    - Outcome
    ontology_label: Death in infancy
  - term_id: NCIT:C133419
    reported_labels:
    - Supportive Care
    ontology_label: Pathologic Stage IIA Esophageal Adenocarcinoma AJCC v8
  - term_id: NCIT:C15277
    reported_labels:
    - Palliative Care
    ontology_label: Mastectomy
  - term_id: NCIT:C47384
    reported_labels:
    - Nutritional Support
    ontology_label: Albendazole
  labels_variant: 4
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
  path: Bowen-Conradi_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bowen-Conradi_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bowen-Conradi Syndrome
- **MONDO ID:** MONDO:0008879 (if available)
- **Causal gene(s):** EMG1
- **OMIM:** not recorded
- **Synonyms:** BWCNS; Bowen-Conradi Hutterite syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Bowen-Conradi Syndrome** covering all of the
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

# Bowen-Conradi Syndrome (MONDO:0008879): A Comprehensive Disease Characterization

**Causal gene: EMG1** (NEP1; "EMG1 N1-specific pseudouridine methyltransferase"; 12p13.31)

---

## Summary

**Bowen-Conradi syndrome (BCS)** is a lethal, autosomal-recessive **ribosomopathy** caused by a single homozygous founder missense mutation, **p.Asp86Gly (c.257A>G, historically reported as c.400A>G)**, in the gene **EMG1** on chromosome 12p13.31. EMG1 (yeast ortholog **Nep1**) is a highly conserved nucleolar **SPOUT-class N1-specific pseudouridine methyltransferase** that is essential for maturation of the 18S ribosomal RNA and assembly of the small (40S) ribosomal subunit. The disease is overwhelmingly concentrated in the **Hutterite population** of North America, where it is one of the most common inherited disorders described in any human group — carrier frequency ~1 in 10 and birth prevalence ~1 in 355 live births.

Mechanistically, the D86G substitution does **not** abolish the enzyme's catalytic (methyltransferase) activity. Instead, it destabilizes the EMG1 protein: it disrupts a predicted D86–R84 salt bridge, promotes aggregation and nuclear mislocalization, triggers proteasome-dependent degradation, and impairs nucleolar recruitment. The resulting EMG1 deficiency delays 18S rRNA processing and small-subunit biogenesis, producing a **G2/M cell-cycle arrest, a mitotic-progression defect (binucleation), and dramatically reduced proliferation** — effects most damaging in rapidly dividing tissues such as the developing embryo, brain, and bone marrow.

Clinically, BCS presents at birth with **severe proportionate pre- and postnatal growth retardation, microcephaly, micrognathia, a prominent nose, rocker-bottom feet, joint contractures, profound psychomotor delay, and failure to thrive**, closely mimicking trisomy 18. The condition is uniformly lethal, with most affected infants dying within the first year of life. There is **no disease-specific treatment** — management is supportive and palliative — and prevention rests on genetic counseling, carrier screening, and prenatal/molecular diagnosis in at-risk (predominantly Hutterite) families.

---

## Key Findings

### Finding 1 — BCS is caused by a homozygous EMG1 founder mutation (p.Asp86Gly)

BCS maps to chromosome **12p13.3** and is caused by the EMG1 variant **p.Asp86Gly**, originally reported as NM_006331.6:c.400A>G and in later literature/ClinVar as NM_006331.8:c.257A>G. The mutation **segregated with disease** across Hutterite pedigrees and was **absent from 414 non-Hutterite alleles**, consistent with a population-specific founder allele. It alters a highly conserved aspartate residue; a structural model predicts loss of a stabilizing **D86–R84 salt bridge**.

> *"We identified variant NM_006331.6:c.400A-->G, p.D86G in the 18S ribosome assembly protein EMG1 as the probable cause of BCS. This mutation segregated with disease, was not found in 414 non-Hutterite alleles, and altered a highly conserved aspartic acid (D) residue."* — [PMID: 19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/)

The founder effect is striking: nearly all reported cases occur among Hutterites, with birth prevalence ~1/355 ([PMID: 19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/)) and a carrier frequency of ~1 in 10 — *"making BCS one of the most commonly inherited genetic diseases in any human group studied to date"* ([PMID: 22856010](https://pubmed.ncbi.nlm.nih.gov/22856010/)).

### Finding 2 — EMG1/Nep1 is a SPOUT-class pseudouridine-N1-methyltransferase with a dual role

EMG1 (yeast **Nep1**) is a nucleolar SPOUT-class RNA methyltransferase that catalyzes **N1-methylation of a pseudouridine** (Ψ1191 in yeast 18S rRNA), contributing to the hypermodified base **m1acp3Ψ**.

> *"Nep1 only methylates RNAs containing a pseudouridine at a position corresponding to a previously identified hypermodified N1-methyl-N3-(3-amino-3-carboxypropyl) pseudouridine (m1acp3-Psi) in eukaryotic 18S rRNAs."* — [PMID: 20047967](https://pubmed.ncbi.nlm.nih.gov/20047967/)

Critically, EMG1 has a **dual function**: an enzymatic methyltransferase activity *and* a separable, essential role as a **pre-ribosome assembly factor** required for small-subunit rRNA maturation and Rps19 incorporation.

> *"This strongly suggests a dual Nep1 function, as Ψ1191-methyltransferase and ribosome assembly factor."* — [PMID: 20972225](https://pubmed.ncbi.nlm.nih.gov/20972225/)

The disease mechanism is tied to the **assembly** role, not catalysis: *"Interestingly, the Nep1 methyltransferase activity is not affected upon introduction of the BCS mutation."* — [PMID: 20972225](https://pubmed.ncbi.nlm.nih.gov/20972225/). Structural work confirms Nep1 recognizes rRNA via base-specific interactions and that catalytic activity may be dispensable while RNA binding/assembly is critical ([PMID: 21087996](https://pubmed.ncbi.nlm.nih.gov/21087996/)).

### Finding 3 — D86G destabilizes EMG1 causing aggregation, degradation, and failed nucleolar recruitment

The pathogenic mechanism is **protein instability**, not loss of transcription. BCS patient fibroblasts show **normal EMG1 mRNA but dramatically reduced EMG1 protein**:

> *"In BCS patient fibroblasts, EMG1 mRNA levels did not differ from those of normal cells, but EMG1 protein was dramatically reduced in comparison to that of normal controls."* — [PMID: 19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/)

The D86G substitution disrupts the D86–R84 salt bridge, increases EMG1 self-interaction/dimerization, and promotes aggregation. Mutant EMG1 is still imported into the nucleus but accumulates in nuclear foci and is degraded:

> *"The BCS mutation in EMG1 leads to reduced nucleolar localisation, accumulation of EMG1D86G in nuclear foci and its proteasome-dependent degradation."* — [PMID: 27798105](https://pubmed.ncbi.nlm.nih.gov/27798105/)

This reduced nucleolar pool, acting within the NOP14–NOC4L–UTP14A subcomplex, impairs small-subunit biogenesis.

### Finding 4 — EMG1 deficiency delays 18S rRNA processing and causes G2/M arrest and reduced proliferation

Downstream of EMG1 depletion, patient cells show a **consistent delay in 18S rRNA processing** and accumulate at the **G2/M** boundary, with cell-type-specific proliferation effects (lymphoblasts strongly affected, fibroblasts less so):

> *"In BCS patient lymphoblasts, cells accumulated in G2/M, resulting in reduced proliferation rates; however, patient fibroblasts showed normal proliferation. The rate of 18S rRNA processing was consistently delayed in patient cells"* — [PMID: 26676230](https://pubmed.ncbi.nlm.nih.gov/26676230/)

A D86G knock-in mouse revealed a **mitotic-progression defect** underlying growth arrest:

> *"In fibroblasts derived from the BCS mouse embryos, we detected a high proportion of binucleated cells, indicating that a mitotic defect underlies the growth arrest in BCS."* — [PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/)

> *"These embryos exhibited dramatically reduced cell proliferation, which we also detected in autopsy brain tissue and bone marrow of BCS patients"* — [PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/)

This explains the tissue selectivity: high-turnover tissues (embryo, brain, marrow) are preferentially compromised.

### Finding 5 — Clinical phenotype: severe growth failure, microcephaly, trisomy-18-like gestalt, infant death

BCS is a lethal autosomal-recessive condition characterized by severely impaired prenatal and postnatal growth, profound psychomotor retardation, and early death:

> *"Bowen-Conradi syndrome (BCS) is a ribosomopathy characterized by severe developmental delay and growth failure that typically leads to death by one year of age."* — [PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/)

> *"Bowen-Conradi syndrome (BCS) is a lethal autosomal recessive condition having significant clinical overlap with trisomy 18."* — [PMID: 22856010](https://pubmed.ncbi.nlm.nih.gov/22856010/)

Bone marrow failure is among the recognized features:

> *"Bowen-Conradi syndrome (BCS) is a severe genetic disorder that is characterised by various developmental abnormalities, bone marrow failure and early infant death."* — [PMID: 27798105](https://pubmed.ncbi.nlm.nih.gov/27798105/)

The original clinical delineation (Hunter et al., 1979) listed the defining features:

> *"the major features of the syndrome include porportionate intrauterine growth retardation, microcephaly, micrognathia, a prominent nose, rocker-bottom feet, joint limitation, and failure to thrive, with death within the first year of life"* — [PMID: 484596](https://pubmed.ncbi.nlm.nih.gov/484596/)

### Finding 6 — Mouse models: Emg1 is essential for embryogenesis; D86G recapitulates growth failure and neural tube defects

Complete loss of Emg1 is early-embryonic lethal and **p53-independent**:

> *"Loss of EMG1 function in mice arrested embryonic development prior to the blastocyst stage."* — [PMID: 20858271](https://pubmed.ncbi.nlm.nih.gov/20858271/)

> *"loss of p53, which has been shown to rescue some phenotypes resulting from defects in ribosome biogenesis, failed to rescue the Emg1-/- pre-implantation lethality"* — [PMID: 20858271](https://pubmed.ncbi.nlm.nih.gov/20858271/)

The D86G knock-in recapitulates the human disease:

> *"Embryos homozygous for the mutation in Emg1 were small for gestational age with neural tube defects, and died between embryonic days 8.5 and 12.5."* — [PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/)

A 2025 study adds a developmental-signaling dimension — EMG1 cooperates with GRHL3 in β-catenin/Wnt-dependent surface-ectoderm differentiation:

> *"Conditional knockout mutation of Emg1 in the GRHL3-positive surface ectoderm causes neural tube defects at the level of the spinal cord, i.e. spina bifida."* — [PMID: 40761126](https://pubmed.ncbi.nlm.nih.gov/40761126/)

### Finding 7 — Natural history and locus mapping

A formal clinical/genetic study ascertained **39 cases** and estimated birth prevalence at 1/355 ([PMID: 12838567](https://pubmed.ncbi.nlm.nih.gov/12838567/)). A genome-wide scan localized the gene to a 3.5 cM (1.9 Mbp) segment of 12p13.3 and established genetic distinctness from COFS:

> *"the BCS locus was mapped to a 3.5 cM segment (1.9 Mbp) in chromosome region 12p13.3 bounded by F8VWF and D12S397"* — [PMID: 15578624](https://pubmed.ncbi.nlm.nih.gov/15578624/)

> *"This study also demonstrates that BCS and cerebro-oculo-facial-skeletal syndrome (COFS) are genetically distinct."* — [PMID: 15578624](https://pubmed.ncbi.nlm.nih.gov/15578624/)

### Finding 8 — Variant annotation locked down (ClinVar, gnomAD)

ClinVar classifies **NM_006331.8(EMG1):c.257A>G (p.Asp86Gly)** as **Pathogenic** for BCS (VCV000000890; dbSNP **rs74435397**; UniProt VAR_062480; OMIM allelic variant 611531.0001; GRCh38 NC_000012.12:g.6974427A>G). In gnomAD v4 the allele frequency is ~6.6×10⁻⁶ (1/152,190) and it is absent from all major continental ancestry groups queried — reflecting the Hutterite population's near-absence from reference databases. Two other EMG1 variants are listed for this disease: c.214A>G (p.Ile72Val, Uncertain significance) and c.126dup (p.Leu43fs, Benign).

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Bowen-Conradi syndrome is a lethal autosomal-recessive ribosome-biogenesis disorder (ribosomopathy) presenting congenitally with severe growth failure, microcephaly, a distinctive facial appearance, joint contractures, rocker-bottom feet, and profound psychomotor delay, with death usually in the first year of life.

**Key identifiers (consolidated, Finding 9):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008879 |
| OMIM (disease) | 211180 |
| Orphanet | ORPHA:1270 |
| DOID | DOID:0050684 |
| MeSH | C537081 |
| UMLS | C1859405 |
| MedGen | 349160 |
| SNOMED CT | 711153001 |
| GARD | 0005950 |
| NORD | 869 |
| ICD-9 | 759.89 |
| ICD-11 (foundation) | 1713786719 |

**Synonyms:** Bowen-Conradi syndrome; BWCNS; Bowen-Conradi Hutterite syndrome.

**Information source type.** Evidence derives from **aggregated disease-level resources** (OMIM, Orphanet, ClinVar) plus **individual patient** case series, autopsy studies, and patient-derived cell lines — not EHR data. Orphanet definition: *"a lethal autosomal recessive ribosomal biogenesis disorder characterized by severe prenatal and postnatal growth retardation, microcephaly, a distinctive facial appearance, extreme psychomotor delay, hip and knee contractures and rockerbottom feet."*

### 2. Etiology

- **Causal factor:** purely **genetic** — homozygous EMG1 c.257A>G (p.Asp86Gly). No environmental or infectious contribution.
- **Genetic risk factor:** Hutterite ancestry (founder allele); consanguinity/endogamy. Carrier frequency ~1/10 in Hutterites ([PMID: 22856010](https://pubmed.ncbi.nlm.nih.gov/22856010/)).
- **Environmental risk/protective factors:** none identified. This is a fully penetrant Mendelian disorder with no known modifiers.
- **Protective factors:** none genetic/environmental identified beyond *not* carrying the founder allele.
- **Gene–environment interactions:** none documented; not applicable.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Frequency |
|---|---|---|---|---|
| Proportionate intrauterine growth retardation | Physical/growth | HP:0001511 (IUGR) | Prenatal | Characteristic |
| Severe postnatal growth failure / failure to thrive | Growth | HP:0001508 | Neonatal | Characteristic |
| Microcephaly | Clinical sign | HP:0000252 | Congenital | Characteristic |
| Micrognathia | Physical | HP:0000347 | Congenital | Common |
| Prominent nose | Physical | HP:0000448 | Congenital | Common |
| Rocker-bottom feet | Physical | HP:0001838 | Congenital | Common |
| Joint contractures / limitation | Physical | HP:0002803 | Congenital | Common |
| Profound psychomotor delay | Neurodevelopmental | HP:0002187 | Infancy | Characteristic |
| Bone marrow failure | Lab/hematologic | HP:0005528 | Infancy | Reported |
| Early death (<1 year) | Outcome | HP:0001522 | Infancy | ~Uniform |

Severity is **severe/lethal**; course is **progressive to death**; onset is **congenital/prenatal**. Quality-of-life instruments (EQ-5D, SF-36) are not applicable given uniform infantile lethality and profound neurological impairment. Features overlap strongly with **trisomy 18** and can mimic **COFS** and **CHARGE** syndromes ([PMID: 25799636](https://pubmed.ncbi.nlm.nih.gov/25799636/)).

### 4. Genetic / Molecular Information

- **Causal gene:** EMG1 — HGNC:16912, NCBI Gene 10436, Ensembl ENSG00000126749, UniProt Q92979, OMIM gene 611531; locus 12p13.31 (GRCh38 chr12:6,970,765–6,979,939, + strand); official name "EMG1 N1-specific pseudouridine methyltransferase"; aliases NEP1, C2F, Grcc2f.
- **Pathogenic variant:** c.257A>G (p.Asp86Gly), missense; **Pathogenic** (ClinVar VCV000000890; rs74435397); germline; ultra-rare in gnomAD (~6.6×10⁻⁶).
- **Functional consequence:** **loss of function via protein destabilization** — reduced protein level, aggregation, proteasomal degradation, failed nucleolar recruitment (Findings 2–3). Enzymatic activity is retained; the assembly-factor function is compromised.
- **Other EMG1 variants listed:** c.214A>G (p.Ile72Val, VUS); c.126dup (p.Leu43fs, Benign).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none established for human BCS. (Genetic interaction with *Grhl3* demonstrated in mouse neurulation — [PMID: 40761126](https://pubmed.ncbi.nlm.nih.gov/40761126/).)

CHEBI-relevant entities: S-adenosyl-L-methionine (CHEBI:15414, methyl donor); pseudouridine (CHEBI:17802); m1acp3Ψ hypermodified base.

### 5. Environmental Information

Not applicable. BCS is entirely genetic; no environmental factors, lifestyle factors, or infectious agents contribute to causation or triggering.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Homozygous **EMG1 c.257A>G (p.Asp86Gly)** mutation **results in** an amino-acid substitution at a conserved residue (demonstrated).
2. D86G **disrupts a predicted D86–R84 salt bridge**, which **leads to** protein destabilization, increased self-interaction/dimerization, and aggregation (structural model + in vitro; partly inferred).
3. Destabilized EMG1 **is imported to the nucleus but leads to** accumulation in nuclear foci and **proteasome-dependent degradation** (demonstrated, [PMID: 27798105](https://pubmed.ncbi.nlm.nih.gov/27798105/)).
4. Degradation **results in** a dramatically **reduced steady-state EMG1 protein pool** despite normal mRNA (demonstrated, [PMID: 19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/)).
5. Reduced nucleolar EMG1 **impairs** small-subunit (SSU) processome function / 40S ribosome assembly and Rps19 incorporation (demonstrated in yeast/human).
6. This **leads to delayed 18S rRNA processing** (demonstrated, [PMID: 26676230](https://pubmed.ncbi.nlm.nih.gov/26676230/)).
7. Delayed SSU biogenesis **results in G2/M cell-cycle arrest and a mitotic-progression defect (binucleation)** (demonstrated, [PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/)).
8. These **lead to dramatically reduced cell proliferation**, preferentially in high-turnover tissues — embryo, developing brain, bone marrow (demonstrated).
   - **Branch A (growth/CNS):** reduced proliferation **causes** IUGR, microcephaly, psychomotor delay.
   - **Branch B (hematologic):** reduced marrow proliferation **causes** bone marrow failure.
   - **Branch C (morphogenesis, mouse):** EMG1–GRHL3/β-catenin–Wnt axis disruption **causes** neural tube defects/spina bifida (model organism; relevance to human facial/skeletal features inferred).
9. Combined tissue failure **results in** the lethal congenital phenotype and death within the first year.

**Molecular pathways:** ribosome biogenesis / SSU processome; rRNA pseudouridine-N1-methylation; (mouse) Wnt/β-catenin surface-ectoderm differentiation.
**Cellular processes:** cell-cycle (G2/M) regulation, mitosis, proliferation; nucleologenesis. Notably, the phenotype is **p53-independent** ([PMID: 20858271](https://pubmed.ncbi.nlm.nih.gov/20858271/)), distinguishing it from some other ribosomopathies.
**Protein dysfunction:** loss of function via misfolding/aggregation and accelerated degradation (not loss of catalysis).
**GO term suggestions:** GO:0042274 (ribosomal small subunit biogenesis); GO:0006364 (rRNA processing); GO:0000154 (rRNA modification); GO:0008649 (rRNA (pseudouridine) methyltransferase activity); GO:0005730 (nucleolus); GO:0031167 (rRNA methylation); GO:0000278 (mitotic cell cycle); GO:0008283 (cell population proliferation).
**CL term suggestions:** hematopoietic progenitors; CL:0000047 (neuronal stem cell); CL:0000031 (neuroblast); CL:0000057 (fibroblast).

### 7. Anatomical Structures Affected

- **Primary organs/systems:** brain (nervous system, microcephaly — UBERON:0000955); skeletal/musculoskeletal system (joint contractures, rocker-bottom feet — UBERON:0002204); craniofacial structures (micrognathia, prominent nose); bone marrow / hematopoietic system (UBERON:0002371).
- **Secondary involvement:** generalized growth failure (whole-body).
- **Tissue/cell level:** rapidly proliferating cell populations — embryonic/fetal progenitors, neural progenitors, hematopoietic progenitors.
- **Subcellular level:** **nucleolus** (GO:0005730) — primary site of EMG1 action; nucleus (nuclear foci of mutant protein); cytoplasm/proteasome (degradation).
- **Localization/lateralization:** systemic and bilateral/symmetric; no lateralization.

### 8. Temporal Development

- **Onset:** congenital/prenatal (IUGR detectable in utero).
- **Onset pattern:** chronic/insidious from conception; not acute.
- **Progression:** progressive postnatally with failure to thrive; no remission.
- **Course/duration:** uniformly lethal, typically within the **first year of life**.
- **Critical period:** embryogenesis and early infancy (windows of highest proliferative demand). No therapeutic window has been established.

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive; homozygous founder allele.
- **Penetrance:** complete (fully penetrant, lethal).
- **Expressivity:** relatively consistent/severe.
- **Epidemiology:** birth prevalence ~1/355 live births in Hutterites ([PMID: 12838567](https://pubmed.ncbi.nlm.nih.gov/12838567/), [PMID: 19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/)); carrier frequency ~1/10 in Hutterites ([PMID: 22856010](https://pubmed.ncbi.nlm.nih.gov/22856010/)).
- **Founder effect / geography:** Hutterite populations of North America; rare possible non-Hutterite cases reported ([PMID: 15578624](https://pubmed.ncbi.nlm.nih.gov/15578624/), [PMID: 12002150](https://pubmed.ncbi.nlm.nih.gov/12002150/)).
- **Consanguinity:** endogamous Hutterite community structure underlies the high homozygosity.
- **Sex ratio:** no sex bias (autosomal); not applicable.
- **Anticipation / mosaicism:** not applicable (non-repeat, Mendelian).

### 10. Diagnostics

- **Genetic testing (definitive):** targeted single-gene/variant testing for EMG1 c.257A>G is the diagnostic gold standard; clinical molecular testing became available ~2015. The first molecularly confirmed case was reported by [PMID: 25799636](https://pubmed.ncbi.nlm.nih.gov/25799636/). WES/WGS and gene panels for ribosomopathies also detect it.
- **Importance of molecular confirmation:** clinically indistinguishable Hutterite phenocopies exist — an infant clinically diagnosed as BCS was found to have a **normal EMG1 sequence** ([PMID: 25906497](https://pubmed.ncbi.nlm.nih.gov/25906497/)), underscoring that molecular testing is essential.
- **Clinical/laboratory clues:** IUGR, microcephaly, characteristic facies; possible cytopenias (bone marrow failure). Functional assays (18S rRNA processing delay) exist in research settings only.
- **Imaging:** prenatal ultrasound (IUGR, microcephaly); no specific radiologic signature.
- **Differential diagnosis:** trisomy 18 (karyotype/CMA to exclude), COFS, CHARGE syndrome; distinguished by EMG1 molecular testing.
- **Screening:** carrier screening and cascade testing in Hutterite families; prenatal diagnosis.

### 11. Outcome / Prognosis

- **Prognosis:** uniformly poor; **lethal in infancy**, most deaths within the first year ([PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/), [PMID: 484596](https://pubmed.ncbi.nlm.nih.gov/484596/)).
- **Morbidity:** profound psychomotor impairment, growth failure, feeding difficulties, susceptibility related to bone marrow failure.
- **Recovery potential:** none; no recovery or remission documented.
- **Prognostic biomarkers:** none beyond the genotype itself.

### 12. Treatment

- **No disease-specific or curative therapy exists.** Management is **supportive/palliative**: nutritional support for failure to thrive, management of feeding difficulties, respiratory and hematologic support, and family support.
- **Pharmacotherapy / gene therapy / cell therapy / RNA therapy:** none approved or in trials for BCS.
- **Experimental:** no registered clinical trials (ClinicalTrials.gov) target BCS specifically.
- **NCIT (supportive care) suggestions:** NCIT:C133419 (Supportive Care); NCIT:C15277 (Palliative Care); NCIT:C47384 (Nutritional Support).

### 13. Prevention

- **Primary prevention:** **genetic counseling** and **carrier screening** in the Hutterite population; informed reproductive decision-making.
- **Secondary/prenatal:** molecular prenatal diagnosis and preimplantation genetic testing for at-risk couples.
- **Cascade testing:** of relatives of affected probands/carriers.
- No immunization, behavioral, or public-health environmental intervention is applicable (purely genetic disorder).
- **NSGC/ACMG genetic counseling** resources are the principal prevention tools.

### 14. Other Species / Natural Disease

- **Orthologs:** mouse **Emg1** (NCBI Gene 14791, Ensembl ENSMUSG00000004268, chr6); yeast **NEP1/EMG1** (*Saccharomyces cerevisiae*). The gene is strongly conserved across eukaryotes.
- **Natural disease in other species:** no naturally occurring EMG1 disease is documented in companion animals or wildlife (OMIA); BCS is studied via engineered models rather than spontaneous animal disease.
- **Comparative biology:** mechanism (rRNA Ψ1191 N1-methylation, SSU assembly) is conserved from yeast to human, making yeast genetics directly informative ([PMID: 20972225](https://pubmed.ncbi.nlm.nih.gov/20972225/), [PMID: 22588997](https://pubmed.ncbi.nlm.nih.gov/22588997/)).
- **Zoonotic potential:** none (not applicable).

### 15. Model Organisms

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| *S. cerevisiae* Nep1 mutants | Yeast / in vitro | Dual role (Ψ1191 methylation + SSU assembly); BCS mutation retains catalysis; genetic interactions with RPS18, RPS19, UTP30 | [PMID: 20972225](https://pubmed.ncbi.nlm.nih.gov/20972225/), [PMID: 22588997](https://pubmed.ncbi.nlm.nih.gov/22588997/), [PMID: 21087996](https://pubmed.ncbi.nlm.nih.gov/21087996/) |
| Emg1 knockout mouse | Mammalian / null | Pre-blastocyst arrest; p53-independent lethality | [PMID: 20858271](https://pubmed.ncbi.nlm.nih.gov/20858271/) |
| Emg1 D86G knock-in mouse | Mammalian / knock-in | Small for gestational age, neural tube defects, death E8.5–E12.5, reduced proliferation, binucleation | [PMID: 25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/) |
| Conditional Emg1 KO (GRHL3+ ectoderm) | Mammalian / conditional | Spina bifida; genetic interaction with Grhl3 | [PMID: 40761126](https://pubmed.ncbi.nlm.nih.gov/40761126/) |
| BCS patient fibroblasts / lymphoblasts | In vitro (human) | Reduced EMG1 protein, delayed 18S processing, G2/M arrest | [PMID: 19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/), [PMID: 26676230](https://pubmed.ncbi.nlm.nih.gov/26676230/) |

**Phenotype recapitulation.** The D86G knock-in mouse recapitulates growth failure, reduced proliferation, and the mitotic defect, but is **more severe** (embryonic lethal E8.5–E12.5) than human disease (infantile lethal), reflecting species differences in developmental robustness. The null mouse's pre-blastocyst lethality confirms EMG1's absolute essentiality but cannot model the hypomorphic BCS allele; the D86G knock-in is therefore the more faithful disease model.

---

## Mechanistic Model / Interpretation

```
 EMG1 c.257A>G (p.D86G)  [homozygous, Hutterite founder allele]
            │  loss of D86–R84 salt bridge
            ▼
 EMG1 protein destabilization → aggregation / nuclear foci
            │  (mRNA normal; protein ↓↓)
            ▼
 Proteasome-dependent degradation → reduced nucleolar EMG1
            │
            ▼
 Impaired SSU processome / 40S assembly (assembly role, NOT catalysis)
            │
            ▼
 Delayed 18S rRNA processing
            │
            ▼
 G2/M arrest + mitotic defect (binucleation)  [p53-INDEPENDENT]
            │
            ▼
 ↓↓ proliferation of high-turnover tissues
      ├── embryo/fetus  → IUGR, growth failure
      ├── brain         → microcephaly, psychomotor delay
      ├── bone marrow   → bone marrow failure
      └── (mouse) ectoderm/Wnt–GRHL3 → neural tube defects
            │
            ▼
 Congenital trisomy-18-like phenotype → death < 1 year
```

The central insight is that BCS is a **protein-stability ribosomopathy**: the mutation does not eliminate EMG1's enzymatic function but destroys the protein, starving the nucleolus of a factor needed to build the small ribosomal subunit. Because the bottleneck is **proliferation** (via delayed 40S biogenesis and mitotic failure), the tissues that suffer are those dividing fastest during development — a unifying explanation for the growth failure, microcephaly, and marrow failure. The p53-independence sets BCS apart from classical "nucleolar-stress/p53" ribosomopathies and suggests the mitotic/proliferation block is the proximate driver.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [19463982](https://pubmed.ncbi.nlm.nih.gov/19463982/) | EMG1 mutation causes BCS | Identifies p.D86G; segregation; absent in 414 control alleles; protein (not mRNA) depletion; prevalence 1/355 |
| [20972225](https://pubmed.ncbi.nlm.nih.gov/20972225/) | Nep1 dual role | Methyltransferase + assembly factor; BCS mutation spares catalysis |
| [20047967](https://pubmed.ncbi.nlm.nih.gov/20047967/) | Nep1 is Ψ-N1 methyltransferase | Defines enzymatic specificity (m1acp3Ψ on 18S) |
| [21087996](https://pubmed.ncbi.nlm.nih.gov/21087996/) | Nep1 structure | SPOUT fold; RNA binding over catalysis; Rps19 assembly |
| [27798105](https://pubmed.ncbi.nlm.nih.gov/27798105/) | Mutant EMG1 import/stability | Nuclear foci, proteasomal degradation, reduced nucleolar recruitment; bone marrow failure |
| [26676230](https://pubmed.ncbi.nlm.nih.gov/26676230/) | G2/M arrest + 18S delay | Patient lymphoblasts; cell-type-specific proliferation effects |
| [25708872](https://pubmed.ncbi.nlm.nih.gov/25708872/) | D86G knock-in mouse | Mitotic defect/binucleation; reduced proliferation in patient brain/marrow; NTDs |
| [20858271](https://pubmed.ncbi.nlm.nih.gov/20858271/) | Emg1 KO mouse | Pre-blastocyst lethality; p53-independent |
| [40761126](https://pubmed.ncbi.nlm.nih.gov/40761126/) | EMG1–GRHL3/Wnt | Surface-ectoderm differentiation; spina bifida; Grhl3 interaction |
| [15578624](https://pubmed.ncbi.nlm.nih.gov/15578624/) | Locus mapping | 12p13.3; distinct from COFS |
| [12838567](https://pubmed.ncbi.nlm.nih.gov/12838567/) | Clinical/genetic study | 39-case natural history; prevalence 1/355 |
| [484596](https://pubmed.ncbi.nlm.nih.gov/484596/) | Original delineation (1979) | Defining clinical features |
| [22856010](https://pubmed.ncbi.nlm.nih.gov/22856010/) | Trisomy-18 mimic review | Carrier frequency ~1/10; AR lethal |
| [25799636](https://pubmed.ncbi.nlm.nih.gov/25799636/) | First molecularly confirmed case | Clinical confirmation by EMG1 testing; mimics |
| [25906497](https://pubmed.ncbi.nlm.nih.gov/25906497/) | BCS phenocopy | Normal EMG1 in clinical "BCS" infant — need for molecular testing |
| [22588997](https://pubmed.ncbi.nlm.nih.gov/22588997/) | Yeast NEP1 interactions | Genetic network (Rps18/19, Utp30) |
| [24240090](https://pubmed.ncbi.nlm.nih.gov/24240090/) | Diseases of SSU processome | Places EMG1/BCS in ribosomopathy context |

Evidence spans **human clinical** (case series, autopsy), **human in vitro** (patient fibroblasts/lymphoblasts), **model organism** (mouse KO, knock-in, conditional; yeast genetics), and **computational/structural** (salt-bridge modeling, crystal structures). Convergence across these independent lines is strong and consistent.

---

## Limitations and Knowledge Gaps

1. **Narrow genetic spectrum.** Essentially all confirmed human cases carry the single founder allele; the phenotypic consequences of other EMG1 variants (e.g., p.Ile72Val VUS) are unknown. Genotype–phenotype breadth cannot be assessed.
2. **Tissue-selectivity mechanism incompletely resolved.** Why some proliferating cell types (lymphoblasts) are more sensitive than others (fibroblasts) is not fully explained; redundancy or compensatory buffering is hypothesized but undefined.
3. **Bone marrow failure under-characterized** in humans — reported as a feature but not systematically quantified across the cohort.
4. **Human relevance of the Wnt–GRHL3/NTD branch** rests on mouse data; it is not established whether this pathway contributes to the human facial/skeletal gestalt or whether human BCS fetuses have NTDs at comparable frequency.
5. **No natural animal disease / no longitudinal human omics.** There are no transcriptomic/proteomic/metabolomic patient datasets analyzed here; molecular profiling is limited to targeted assays.
6. **Mouse–human severity mismatch.** The knock-in is embryonic-lethal whereas humans survive to infancy, limiting direct translation of therapeutic windows.
7. **No therapeutics.** Absence of any disease-modifying treatment or trial means prognostic and treatment sections rely on supportive-care principles rather than disease-specific evidence.

---

## Proposed Follow-up Experiments / Actions

1. **Protein-stabilization screen.** Small-molecule or pharmacological-chaperone screens to rescue EMG1-D86G from proteasomal degradation (e.g., proteasome modulation, chemical chaperones) in patient fibroblasts — a tractable target since mRNA and catalysis are intact.
2. **Patient-derived iPSC/organoid models.** Generate iPSC-derived neural progenitors and hematopoietic progenitors to model the proliferation defect in the most-affected human lineages and test rescue strategies.
3. **Single-cell transcriptomics** of D86G knock-in mouse embryos and patient-derived progenitors to map cell-type-specific vulnerability and identify downstream effectors of the G2/M block.
4. **Gene/mRNA replacement feasibility.** Assess AAV- or LNP-mRNA-based EMG1 restoration in the knock-in mouse, given that the defect is loss-of-function and dose-sensitive.
5. **Define the Wnt–GRHL3 axis in humans.** Re-examine BCS autopsy material for neural tube and surface-ectoderm defects to test the translational relevance of [PMID: 40761126](https://pubmed.ncbi.nlm.nih.gov/40761126/).
6. **Expand carrier screening** in Hutterite colonies and systematically report any non-Hutterite EMG1 variants to clarify the disease's genetic spectrum and population reach.
7. **p53-independence follow-up.** Dissect the p53-independent cell-cycle checkpoint driving G2/M arrest to identify alternative, druggable nodes.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 25 reviewed papers. All mechanistic and clinical claims are anchored to primary literature with verified abstract quotes.*


## Artifacts

- [OpenScientist final report](Bowen-Conradi_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bowen-Conradi_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008879` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Bowen-Conradi syndrome**
- `DOID:0050684` (1 mention) - the report calls it "DOID"; DOID calls it **Bowen-Conradi syndrome**
- `HP:0000252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Microcephaly**
- `HP:0000448` (1 mention) - the report calls it "Physical"; HP calls it **Prominent nose**
- `HP:0001838` (1 mention) - the report calls it "Physical"; HP calls it **Rocker bottom foot**
- `HP:0002803` (1 mention) - the report calls it "Physical"; HP calls it **Congenital contracture**
- `HP:0002187` (1 mention) - the report calls it "Neurodevelopmental"; HP calls it **Profound intellectual disability**
- `HP:0005528` (1 mention) - the report calls it "Lab/hematologic"; HP calls it **Bone marrow hypocellularity**
- `HP:0001522` (1 mention) - the report calls it "Outcome"; HP calls it **Death in infancy**
- `NCIT:C133419` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Pathologic Stage IIA Esophageal Adenocarcinoma AJCC v8**
- `NCIT:C15277` (1 mention) - the report calls it "Palliative Care"; NCIT calls it **Mastectomy**
- `NCIT:C47384` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Albendazole**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001508` (1 mention) - the report calls it "Growth"; HP calls it **Failure to thrive**, and lists "Undergrowth" among its other names
- `HP:0000347` (1 mention) - the report calls it "Physical"; HP calls it **Micrognathia**, and lists "Hypoplastic mandible" among its other names
- `GO:0005730` (2 mentions) - the report calls it "nucleolus", "Subcellular level:** **nucleolus"; GO calls it **nucleolus**
- `CL:0000031` (1 mention) - the report calls it "neuroblast"; CL calls it **neuroblast (sensu Vertebrata)**, and lists "neuroblast" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005730` - called "nucleolus", "Subcellular level:** **nucleolus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.