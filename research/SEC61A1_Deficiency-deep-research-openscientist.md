---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T20:30:56.456504'
end_time: '2026-10-22T20:49:46.884837'
duration_seconds: 1130.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SEC61A1 Deficiency
  mondo_id: MONDO:0100337
  category: Mendelian
  causal_genes: SEC61A1
  omim_id: not recorded
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
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:21499241
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 45
  verified: 36
  not_found: 0
  obsolete: 0
  unverifiable: 9
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0100337
    reported_labels:
    - SEC61A1 deficiency
    - umbrella
    ontology_label: SEC61A1 deficiency
  - term_id: HP:0002149
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperuricemia
  - term_id: HP:0000107
    reported_labels:
    - Physical manifestation
    ontology_label: Renal cyst
  - term_id: HP:0001903
    reported_labels:
    - Lab abnormality
    ontology_label: Anemia
  - term_id: HP:0001875
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0001510
    reported_labels:
    - Physical
    ontology_label: Growth delay
  - term_id: HP:0100543
    reported_labels:
    - Behavioral/neuro
    ontology_label: Cognitive impairment
  - term_id: HP:0002917
    reported_labels:
    - Lab abnormality
    ontology_label: Hypomagnesemia
  - term_id: HP:0000846
    reported_labels:
    - Lab abnormality
    ontology_label: Adrenal insufficiency
  unresolvable_prefixes:
  - Orphanet
  - HomoloGene
  - NCBIGene
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SEC61A1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SEC61A1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SEC61A1 Deficiency
- **MONDO ID:** MONDO:0100337 (if available)
- **Causal gene(s):** SEC61A1
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SEC61A1 Deficiency** covering all of the
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

# SEC61A1 Deficiency (MONDO:0100337): A Comprehensive Disease Characterization

## Summary

**SEC61A1 deficiency** is a rare autosomal-dominant multisystem disorder caused by heterozygous pathogenic variants in **SEC61A1** (HGNC:18276; OMIM gene 609213; chr3q21.3; ENSG00000058262), the gene encoding the pore-forming **α-subunit of the Sec61 protein-translocation channel (translocon)** in the endoplasmic reticulum (ER). Sec61α is a dual-function membrane protein: it forms the central aqueous conduit through which secretory and membrane proteins are co-translationally translocated across/into the ER membrane (GO:0008320 transmembrane protein transporter activity), and it simultaneously functions as a passive ER calcium-leak channel (GO:0005262 calcium channel activity). Because the protein sits at the hub of the secretory pathway, dominant mutations produce a pleiotropic "translocopathy" that strikes the most highly secretory and proliferative cell lineages — renal tubular/juxtaglomerular cells, antibody-secreting plasma cells, and maturing granulocytes.

Under the umbrella concept MONDO:0100337 ("SEC61A1 deficiency"), the disease resolves into **three distinct dominant OMIM phenotypes**: (1) **ADTKD-SEC61A1 / familial juvenile hyperuricemic nephropathy 4 (HNFJ4, OMIM 617056)** — early-onset progressive chronic kidney disease (CKD) with hyperuricemia, congenital anemia, growth retardation and renal cysts; (2) **common variable immunodeficiency 15 (CVID15, OMIM 620670)** — a plasma-cell differentiation block producing hypogammaglobulinemia; and (3) **severe congenital neutropenia 11 (SCN11, OMIM 620674)** — a granulocytic maturation arrest. Additional reported features expand the spectrum to hypomagnesemia, hypoaldosteronism with salt-wasting, cognitive impairment, microcephaly and epilepsy.

The unifying mechanism is impaired co-translational protein translocation combined with dysregulated ER calcium homeostasis, which together trigger a terminal (apoptotic) unfolded-protein response (UPR) in secretory lineages. SEC61A1's extreme population-genetic constraint (gnomAD pLI = 0.9998; missense Z = 5.53) confirms strong dosage sensitivity and supports a haploinsufficiency/dominant-negative model. There is currently no curative therapy; management is organ-specific and supportive (dialysis/transplant, immunoglobulin replacement, G-CSF, fludrocortisone). The chemical chaperone **4-phenylbutyrate**, which rescues the mutant translocon's renin-transport defect in vitro, is the leading mechanism-based experimental avenue.

---

## Key Findings

### Finding 1 — SEC61A1 is the causal gene; heterozygous loss-of-function causes ADTKD

The founding disease association was established by Bolar et al. 2016 ([PMID: 27392076](https://pubmed.ncbi.nlm.nih.gov/27392076/)), who identified heterozygous missense variants **c.553A>G (p.Thr185Ala)** and **c.200T>G (p.Val67Gly)** in two families with autosomal-dominant tubulointerstitial kidney disease (ADTKD) plus congenital anemia. Both variants affect *"functionally important and conserved residues in SEC61."* Critically, the study provided direct tissue-level mechanistic evidence: *"Both transiently expressed SEC6A1A variants are delocalized to the Golgi, a finding confirmed in a renal biopsy from an affected individual."* Functional confirmation came from a zebrafish model: suppression or CRISPR deletion of the ortholog *sec61al2* induced pronephric tubule convolution defects that were rescued by wild-type human mRNA but **not** by the patient/mutant mRNA — establishing loss of function as the disease mechanism. This finding anchors the causal gene and the two founding ADTKD-SEC61A1 variants.

### Finding 2 — SEC61A1 mutations also cause primary antibody deficiency (CVID) via a plasma-cell differentiation block

Schubert et al. 2018 ([PMID: 28782633](https://pubmed.ncbi.nlm.nih.gov/28782633/)) extended the phenotype to humoral immunodeficiency. They *"identified novel heterozygous missense (c.254T>A, p.V85D) and nonsense (c.1325G>T, p.E381*) mutations in SEC61A1, segregating with the disease phenotype"* across 11 patients from two families presenting with hypogammaglobulinemia and recurrent respiratory infections. B cells from patients failed to differentiate into plasma cells in vitro. Mechanistically, *"SEC61A1-V85D was deficient in cotranslational protein translocation, and it disturbed the cellular calcium homeostasis in HeLa cells,"* and triggered the terminal unfolded-protein response. This connects the translocation defect and calcium dysregulation directly to the failure of the most secretory immune lineage (the plasma cell), and defines the immune arm later catalogued as CVID15.

### Finding 3 — A druggable molecular defect: phenylbutyrate rescues mutant renin transport

Sicking et al. 2022 ([PMID: 35064074](https://pubmed.ncbi.nlm.nih.gov/35064074/)) dissected the biochemical consequence of the ADTKD mutations. The V67G and T185A Sec61α mutants impair translocation/transport of **preprorenin** into the ER lumen, offering a plausible explanation for the renal/juxtaglomerular phenotype. Importantly, *"Phenylbutyrate rescues the transport defect of the Sec61α mutations V67G and T185A for renin,"* establishing a pharmacological rescue of the molecular lesion and a concrete therapeutic hypothesis. The study also reinforced the channel's dual role, moving both protein substrates and calcium ions across the ER membrane.

### Finding 4 — An expanding multisystem phenotype beyond the kidney

Across the ~15 reported patients (reviewed by Zhong et al. 2026, [PMID: 41850665](https://pubmed.ncbi.nlm.nih.gov/41850665/)), the renal presentation comprises early-onset CKD with hyperuricemia, bland urinary sediment, absence of significant proteinuria, and renal cysts. Extrarenal features are prominent: *"The extrarenal features included growth retardation, hematological abnormalities, cognitive impairment, and immunological abnormalities."* Hematological abnormalities span normocytic normochromic anemia and neutropenia/agranulocytosis. Newer case reports continue to broaden the spectrum: a pediatric case from Oman (p.Thr185Ser, c.554C>G) presented with **hypomagnesemia, epilepsy, and microcephaly** — epilepsy being a previously unreported ADTKD-SEC61A1 feature ([PMID: 42730770](https://pubmed.ncbi.nlm.nih.gov/42730770/)) — and Karpman et al. 2024 documented **hypoaldosteronism with salt-wasting** that was *"successfully treated with fludrocortisone"* ([PMID: 39135939](https://pubmed.ncbi.nlm.nih.gov/39135939/)).

### Finding 5 — Extreme intolerance to variation supports dominant haploinsufficiency

Population-genetic constraint data from gnomAD v2.1.1 strongly support a dosage-sensitive mechanism. For SEC61A1 (ENSG00000058262; HGNC:18276; chr3:128,051,641–128,071,683 GRCh38; 3q21.3):

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 0.9998 | Near-certain intolerance to loss of function |
| LOEUF (oe_lof upper) | 0.418 | Constrained |
| observed/expected LoF | 0.272 (obs 15 / exp 55.2) | ~73% depletion of LoF alleles |
| LoF Z | 4.59 | Strong LoF constraint |
| missense Z | 5.53 (oe_mis 0.471) | Strong missense constraint |

This profile is characteristic of a haploinsufficient, dominant-acting gene, consistent with the autosomal-dominant inheritance observed clinically.

### Finding 6 — The severe congenital neutropenia arm (SCN11) unifies three phenotypes

The official disease concept MONDO:0100337 ("SEC61A1 deficiency") is defined as any Mendelian disease caused by SEC61A1 mutation, *"characterized by variable presentation of phenotypes... including autosomal dominant tubulointerstitial kidney disease, primary antibody deficiency, and severe congenital neutropenia."* Van Nieuwenhove et al. 2020 ([PMID: 32325141](https://pubmed.ncbi.nlm.nih.gov/32325141/)) established the myeloid arm: *"We identified a novel de novo missense mutation in SEC61A1 (c.A275G;p.Q92R) in a patient with SCN"* (designated SCN11). The shared mechanism was confirmed — *"The mutation results in diminished protein expression, disturbed protein translocation, and an increase in calcium leakage from the endoplasmic reticulum"* — along with UPR dysregulation. Wang et al. 2026 ([PMID: 42056350](https://pubmed.ncbi.nlm.nih.gov/42056350/)) reported a second SCN variant, c.1135T>C (p.Trp379Arg), noting *"This is the second reported SEC61A1 variant associated with SCN11, expanding the genetic and phenotypic spectrum of SCN."* ClinVar (Oct 2025) lists 393 SEC61A1 records, including 25 pathogenic and 6 likely pathogenic, with the large majority (~360) classified as variants of uncertain significance.

### Finding 7 — Three resolved OMIM entities under one MONDO umbrella

Gene–disease association resolution (Monarch/OLS/MONDO) catalogues three distinct entities caused by SEC61A1:

| Arm | Disease | OMIM | MONDO | Other IDs |
|---|---|---|---|---|
| Kidney | Hyperuricemic nephropathy, familial juvenile, 4 (HNFJ4) / ADTKD-SEC61A1 | 617056 | MONDO:0014891 | DOID:0061120 |
| Immune | Immunodeficiency, common variable, 15 (CVID15) | 620670 | MONDO:0958013 | Orphanet:697417 |
| Myeloid | Neutropenia, severe congenital, 11, autosomal dominant (SCN11) | 620674 | MONDO:0958017 | — |

All three are umbrella'd by **MONDO:0100337** ("SEC61A1 deficiency"). GO molecular-function annotation confirms the dual activity: **GO:0008320** (transmembrane protein transporter activity) and **GO:0005262** (calcium channel activity), with cellular component **GO:0005784** (Sec61 translocon complex). Note: an earlier label "CVID13" was corrected to **CVID15** during the investigation.

### Finding 8 — Deep evolutionary conservation supports model-organism transferability

SEC61A1 is deeply conserved (HomoloGene:55537), with verified orthologs: human SEC61A1 (NCBIGene:29927), mouse *Sec61a1* (NCBIGene:53421), rat *Sec61a1* (NCBIGene:80843), zebrafish *sec61al1* (NCBIGene:192298) and *sec61al2* (NCBIGene:266796), and yeast *SEC61* (NCBIGene:851095), plus orthologs across Xenopus, chicken, dog, cow, and primates. Complete loss of translocon function is expected to be lethal, consistent with the dominant, heterozygous nature of human disease. Disease-relevant modeling has succeeded in zebrafish for the renal phenotype (*"Suppression or CRISPR-mediated deletions of sec61al2 in zebrafish embryos induced convolution defects of the pronephric tubules but not the pronephric ducts"*; [PMID: 27392076](https://pubmed.ncbi.nlm.nih.gov/27392076/)) and via CD34+ granulocytic differentiation assays for the SCN arm ([PMID: 32325141](https://pubmed.ncbi.nlm.nih.gov/32325141/)).

---

## Report by Template Section

### 1. Disease Information
SEC61A1 deficiency is a rare autosomal-dominant Mendelian translocopathy caused by heterozygous variants in **SEC61A1**, the Sec61 translocon α-subunit gene. **Key identifiers:** MONDO:0100337 (umbrella); constituent entities HNFJ4/ADTKD-SEC61A1 (OMIM 617056, MONDO:0014891, DOID:0061120), CVID15 (OMIM 620670, MONDO:0958013, Orphanet:697417), SCN11 (OMIM 620674, MONDO:0958017); gene OMIM 609213; HGNC:18276. **Synonyms/alternative names:** ADTKD-SEC61A1; familial juvenile hyperuricemic nephropathy type 4; Sec61-alphopathy/translocopathy. Information is derived from **aggregated disease-level resources** (OMIM, MONDO, Orphanet, ClinVar, gnomAD) combined with **individual-patient reports/case series** (the primary literature cited throughout).

### 2. Etiology
**Causal factor:** monogenic — heterozygous pathogenic variants in SEC61A1. **Genetic risk:** the causal variant itself is sufficient; no susceptibility loci or modifier genes are established. The extreme gnomAD constraint (pLI 0.9998, missense Z 5.53) indicates strong purifying selection. **Environmental risk/protective factors and gene–environment interactions:** none established; this is a Mendelian disorder with no documented environmental contribution. A single founding de novo variant (p.Q92R, SCN11) indicates that disease can arise sporadically.

### 3. Phenotypes
Representative phenotypes with suggested HPO terms:

| Phenotype | Type | HPO suggestion | Characteristics |
|---|---|---|---|
| Chronic kidney disease / tubulointerstitial nephropathy | Clinical sign | HP:0012622 / HP:0000112 | Early-onset, progressive to ESRD in adulthood |
| Hyperuricemia / gout | Lab abnormality | HP:0002149 | Juvenile onset |
| Bland urinary sediment / absent proteinuria | Lab abnormality (negative finding) | — | Characteristic for ADTKD |
| Renal cysts / glomerulocystic disease | Physical manifestation | HP:0000107 | Variable |
| Congenital/normocytic anemia | Lab abnormality | HP:0001903 | Neonatal/congenital |
| Neutropenia / agranulocytosis | Lab abnormality | HP:0001875 | SCN11 arm; severe |
| Hypogammaglobulinemia / recurrent infections | Lab abnormality / symptom | HP:0004313 / HP:0002719 | CVID15 arm; plasma-cell block |
| Growth retardation | Physical | HP:0001510 | Variable |
| Cognitive impairment | Behavioral/neuro | HP:0100543 | Reported subset |
| Hypomagnesemia | Lab abnormality | HP:0002917 | Newer feature |
| Hypoaldosteronism / salt-wasting | Lab abnormality | HP:0000846 | Fludrocortisone-responsive |
| Epilepsy, microcephaly | Clinical sign | HP:0001250 / HP:0000252 | Rare, pediatric (p.Thr185Ser) |

Onset ranges from congenital/neonatal (anemia, neutropenia) to childhood/adolescence (CKD). Severity is variable; the renal course is progressive. Quality-of-life impact is substantial owing to lifelong CKD/dialysis dependence, infection susceptibility, and transfusion/growth issues; no disease-specific QoL instruments have been applied.

### 4. Genetic / Molecular Information
**Causal gene:** SEC61A1 (OMIM 609213; HGNC:18276; 3q21.3). **Pathogenic variants** (all germline, mostly heterozygous dominant): missense p.Thr185Ala (c.553A>G), p.Val67Gly (c.200T>G), p.Thr185Ser (c.554C>G) — ADTKD; p.Val85Asp (c.254T>A) and nonsense p.Glu381* (c.1325G>T) — CVID; p.Gln92Arg (c.A275G, de novo) and p.Trp379Arg (c.1135T>C) — SCN11. **Variant classes:** predominantly missense, with a disease-relevant nonsense allele. **ClinVar (Oct 2025):** 393 records (25 pathogenic, 6 likely pathogenic, ~360 VUS). **Allele frequency:** pathogenic alleles are absent/ultra-rare in gnomAD; the gene is strongly LoF- and missense-constrained. **Functional consequence:** loss of function with likely dominant-negative contribution (mutant subunit incorporated into the heterotrimeric channel). **Modifier genes/epigenetics/chromosomal abnormalities:** none established.

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors are known. Recurrent infections are a *consequence* of the immunodeficiency/neutropenia arms, not a cause.

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**
1. A heterozygous SEC61A1 variant (missense or nonsense) **leads to** a defective or reduced Sec61α subunit incorporated into the ER translocon.
2. This **results in** impaired co-translational translocation of secretory/membrane precursor proteins into the ER (demonstrated for preprorenin) **and**, in parallel (branch), increased passive Ca²⁺ leak from the ER lumen through the defective channel (demonstrated in HeLa cells and CD34+ cells).
3. Reduced protein import **leads to** mislocalization of Sec61α to the Golgi (shown in patient renal biopsy) and accumulation of untranslocated/misfolded client proteins.
4. Protein-folding stress plus disturbed ER Ca²⁺ homeostasis **results in** activation of ER stress and the **terminal (apoptotic) unfolded-protein response**.
5. In the most secretory/proliferative lineages this **results in** cell dysfunction/death — branching into: (a) renal tubular + juxtaglomerular cells → tubulointerstitial fibrosis, impaired renin/renal function → CKD, hyperuricemia, anemia, hypoaldosteronism; (b) plasma cells → differentiation block → hypogammaglobulinemia (CVID15); (c) granulocyte precursors → maturation arrest → severe congenital neutropenia (SCN11).

**Upstream:** the translocation defect and Ca²⁺ dysregulation. **Downstream:** UPR-driven apoptosis and lineage-specific functional failure. **Molecular pathways/processes:** protein targeting to ER (GO:0045047), SRP-dependent co-translational translocation (GO:0006614), response to ER stress/UPR (GO:0030968), ER calcium ion homeostasis (GO:0032469), apoptotic process (GO:0006915). **Cell types (CL):** kidney tubule epithelial cell, juxtaglomerular cell, plasma cell (CL:0000786), neutrophil/granulocyte precursor (CL:0000775). **Subcellular compartment:** ER membrane / Sec61 translocon complex (GO:0005784), ER (GO:0005783). **Protein dysfunction:** loss of channel conductance for protein substrates + aberrant Ca²⁺ leak; mislocalization to Golgi; likely dominant-negative assembly into the heterotrimeric Sec61 complex (structural context from cryo-EM studies [PMID: 33398175](https://pubmed.ncbi.nlm.nih.gov/33398175/), [PMID: 21499241](https://pubmed.ncbi.nlm.nih.gov/21499241/)).

### 7. Anatomical Structures Affected
**Primary organs:** kidney (UBERON:0002113) — tubulointerstitium, juxtaglomerular apparatus; bone marrow (UBERON:0002371) — myeloid compartment; secondary lymphoid organs / plasma-cell niches. **Secondary involvement:** systemic (anemia, growth retardation), adrenal/renin-angiotensin-aldosterone axis (hypoaldosteronism), CNS (cognitive impairment, epilepsy, microcephaly). **Body systems:** urinary, hematopoietic/immune, endocrine, nervous. **Tissues/cells:** renal epithelial cells, plasma cells (CL:0000786), neutrophils (CL:0000775). **Subcellular:** ER membrane (GO:0005789), Sec61 translocon (GO:0005784). **Localization:** bilateral kidney involvement; systemic hematologic/immune involvement.

### 8. Temporal Development
**Onset:** congenital/neonatal for anemia and neutropenia; childhood-to-adolescent for CKD/hyperuricemia; insidious and chronic. **Progression:** renal disease is slowly progressive, advancing to end-stage kidney disease in adulthood (ESRD present at diagnosis in a substantial fraction of ADTKD cohorts). **Course:** chronic, lifelong, progressive; no spontaneous remission. **Critical windows:** early diagnosis enables renal-protective management, infection prophylaxis, and G-CSF initiation for neutropenia.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant; de novo occurrence documented (SCN11 p.Q92R). **Penetrance/expressivity:** appears high-penetrance but with highly variable expressivity (which organ arm predominates differs among families/variants). **Epidemiology:** ultra-rare; SEC61A1 accounts for a very small minority of ADTKD cases (ADTKD overall ~5% of monogenic CKD; SEC61A1 is among the rarest subtypes, with single-family yields in large cohorts such as the Japanese cohort of [PMID: 39976632](https://pubmed.ncbi.nlm.nih.gov/39976632/)). No formal prevalence/incidence estimates exist. **Founder effects/consanguinity:** none established; gnomAD shows pathogenic alleles are essentially absent. **Carrier frequency:** not applicable (dominant, de novo or inherited heterozygous). **Sex ratio/geographic distribution:** no established skew; cases reported across multiple populations (Europe, Japan, Middle East).

### 10. Diagnostics
**Genetic testing is the diagnostic cornerstone.** ADTKD is defined by identification of a pathogenic variant in one of UMOD, MUC1, REN, HNF1B, or SEC61A1. Recommended approaches: targeted single-gene/panel testing (ADTKD gene panels), whole-exome or whole-genome sequencing for unexplained CKD; long-read sequencing is especially useful to resolve MUC1 but exome/genome suffices for SEC61A1. **Supportive clinical/lab findings:** elevated creatinine with **bland urinary sediment and minimal proteinuria**, hyperuricemia/gout, normocytic anemia, neutropenia, hypogammaglobulinemia, hypomagnesemia, low aldosterone. **Imaging:** normal-to-small kidneys ± cysts. **Biopsy:** nonspecific tubulointerstitial fibrosis/tubular atrophy; immunostaining can show Sec61α Golgi mislocalization (research setting). **Differential diagnosis:** other ADTKD subtypes (UMOD, MUC1, REN, HNF1B), and newly described ADTKD-JAG1 ([PMID: 41061854](https://pubmed.ncbi.nlm.nih.gov/41061854/)); for the immune/myeloid arms, other causes of CVID and congenital neutropenia (e.g., ELANE). **Screening:** cascade genetic testing of at-risk relatives.

### 11. Outcome / Prognosis
The renal arm carries a guarded prognosis, progressing to ESRD requiring dialysis or transplantation in adulthood; transplantation is effective as the defect is intrinsic to kidney tissue but systemic. The immune arm risks recurrent/chronic infection and bronchiectasis if untreated; the myeloid arm risks severe bacterial infection and, as with other SCN, potential long-term leukemia surveillance considerations. Overall morbidity is high (lifelong CKD, infection susceptibility, growth impairment). No formal survival statistics exist given rarity. **Prognostic factors:** specific variant/predominant organ arm, age at CKD onset, and severity of cytopenias.

### 12. Treatment
No curative, mechanism-targeted therapy is approved; management is **organ-specific and supportive**:
- **Renal:** CKD management, uric-acid lowering (e.g., allopurinol), renal replacement therapy — dialysis and kidney transplantation (NCIT:C157763 kidney transplantation).
- **Immune (CVID15):** immunoglobulin replacement therapy (IVIG/SCIG; NCIT:C29071 immunoglobulin therapy), infection prophylaxis.
- **Myeloid (SCN11):** granulocyte colony-stimulating factor / G-CSF (filgrastim; NCIT:C1583).
- **Endocrine:** fludrocortisone for hypoaldosteronism/salt-wasting (demonstrated effective, [PMID: 39135939](https://pubmed.ncbi.nlm.nih.gov/39135939/)).
- **Hematologic:** transfusion support for anemia; magnesium supplementation for hypomagnesemia.
- **Experimental / mechanism-based:** the chemical chaperone **4-phenylbutyrate** rescues the mutant translocon's renin-transport defect in vitro ([PMID: 35064074](https://pubmed.ncbi.nlm.nih.gov/35064074/)) and is the leading candidate for molecular correction; not yet trialed clinically for this disease.
**Pharmacogenomics, gene/cell/RNA therapies:** none established.

### 13. Prevention
No primary prevention (Mendelian). **Secondary prevention:** early genetic diagnosis enables renal-protective care, infection prophylaxis/immunoglobulin, and timely G-CSF. **Genetic counseling** is central: 50% transmission risk for an affected heterozygous parent; de novo cases possible. Prenatal/preimplantation genetic testing is feasible when a familial variant is known. Cascade testing identifies at-risk relatives for surveillance.

### 14. Other Species / Natural Disease
SEC61A1 is deeply conserved across eukaryotes (HomoloGene:55537), with orthologs in mouse, rat, zebrafish, Xenopus, chicken, dog, cow, primates, and yeast (see Finding 8 for NCBI Gene IDs; NCBI Taxon IDs: human 9606, mouse 10090, rat 10116, zebrafish 7955, *S. cerevisiae* 559292). No naturally occurring SEC61A1 disease has been catalogued in companion animals or wildlife (no OMIA entry identified); complete translocon loss is presumed embryonic-lethal. No zoonotic relevance (non-infectious disease).

### 15. Model Organisms
- **Zebrafish (*Danio rerio*):** morpholino knockdown and CRISPR deletion of *sec61al2* reproduce pronephric tubule convolution defects; human wild-type mRNA rescues but mutant mRNA does not — a validated model of the renal phenotype ([PMID: 27392076](https://pubmed.ncbi.nlm.nih.gov/27392076/)). Resource: ZFIN.
- **Cellular/in vitro:** HeLa cells expressing SEC61A1-V85D show translocation and calcium-homeostasis defects and UPR induction ([PMID: 28782633](https://pubmed.ncbi.nlm.nih.gov/28782633/)); patient CD34+ cells modeling granulocytic differentiation recapitulate the SCN maturation arrest ([PMID: 32325141](https://pubmed.ncbi.nlm.nih.gov/32325141/)). Biochemical reconstitution of preprorenin transport assessed the renin defect and phenylbutyrate rescue ([PMID: 35064074](https://pubmed.ncbi.nlm.nih.gov/35064074/)).
- **Yeast and structural systems:** *S. cerevisiae* and thermophilic fungal Sec61–Sec62–Sec63 complexes provided the cryo-EM structural framework for channel gating ([PMID: 33398175](https://pubmed.ncbi.nlm.nih.gov/33398175/)).
- **Mammalian knockout:** no published mouse model specific to the human disease variants was identified; complete Sec61a1 knockout is expected lethal. Resources: MGI, RGD, ZFIN, IMPC.
**Phenotype recapitulation:** strong for the renal (zebrafish) and cellular/immune/myeloid (in vitro) arms. **Limitation:** no whole-mammal model captures the full multisystem human phenotype.

---

## Mechanistic Model / Interpretation

```
            Heterozygous SEC61A1 variant (missense / nonsense)
                               |
            defective Sec61a subunit in ER translocon
                               |
        +----------------------+----------------------+
        |                                             |
 impaired co-translational                   increased passive ER
 protein translocation                       Ca2+ leak through channel
 (e.g. preprorenin;                          (shown in HeLa, CD34+ cells)
  Golgi mislocalization)                                |
        |                                             |
        +----------------------+----------------------+
                               |
             ER stress --> terminal (apoptotic) UPR
                               |
   +---------------+-----------+-----------+---------------+
 renal tubular/   plasma cells   granulocyte    CNS / endocrine
 JG cells         (block)        precursors     (variable)
   |                  |              |                |
 CKD, hyperuric.,  hypogamma-     severe          cognitive impair.,
 anemia, cysts,    globulinemia   congenital      epilepsy, hypo-
 hypoaldosteron.   (CVID15)       neutropenia     magnesemia
 (HNFJ4/ADTKD)                    (SCN11)
```

The central insight is **lineage selectivity through shared biochemistry**: a single ubiquitously expressed translocon defect manifests preferentially in cells with the heaviest secretory/folding load and highest proliferative demand, where the combined protein-translocation deficit and ER-calcium dysregulation most readily tip cells into apoptotic UPR. The same molecular lesion thus produces three nosologically distinct dominant diseases that share one mechanism — a paradigm of a monogenic "translocopathy."

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [27392076](https://pubmed.ncbi.nlm.nih.gov/27392076/) | *Heterozygous LoF SEC61A1 mutations cause ADTKD with anemia* | Founding ADTKD variants; Golgi mislocalization in biopsy; zebrafish rescue | Human clinical + model organism |
| [28782633](https://pubmed.ncbi.nlm.nih.gov/28782633/) | *Plasma cell deficiency with heterozygous SEC61A1 mutations* | CVID arm; V85D translocation + Ca²⁺ defect; terminal UPR | Human clinical + in vitro |
| [35064074](https://pubmed.ncbi.nlm.nih.gov/35064074/) | *Phenylbutyrate rescues Sec61α V67G/T185A renin transport* | Druggable mechanism; preprorenin defect | In vitro / biochemical |
| [41850665](https://pubmed.ncbi.nlm.nih.gov/41850665/) | *De novo SEC61A1 in congenital anemia + early kidney disease* | Multisystem phenotype review | Human clinical review |
| [39135939](https://pubmed.ncbi.nlm.nih.gov/39135939/) | *Hypoaldosteronism from novel SEC61A1 variant* | Hypoaldosteronism; fludrocortisone treatment | Human clinical |
| [32325141](https://pubmed.ncbi.nlm.nih.gov/32325141/) | *Defective Sec61α1 underlies autosomal dominant SCN* | SCN11 arm; Q92R; translocation + Ca²⁺ leak + UPR | Human clinical + in vitro |
| [42056350](https://pubmed.ncbi.nlm.nih.gov/42056350/) | *Novel de novo SEC61A1 variant in SCN* | Second SCN11 variant (W379R) | Human clinical |
| [42730770](https://pubmed.ncbi.nlm.nih.gov/42730770/) | *Rare ADTKD in children (Oman)* | p.Thr185Ser; epilepsy, microcephaly, hypomagnesemia | Human clinical |
| [33398175](https://pubmed.ncbi.nlm.nih.gov/33398175/) | *Stepwise gating of Sec61 by Sec63/Sec62* | Structural basis of channel gating | Structural/cryo-EM |
| [21499241](https://pubmed.ncbi.nlm.nih.gov/21499241/) | *Cryo-EM of ribosome–SecYE in membrane* | Translocon architecture | Structural/cryo-EM |
| [34519781](https://pubmed.ncbi.nlm.nih.gov/34519781/) | *Clinical and genetic spectra of ADTKD* | Places SEC61A1 among ADTKD genes | Review |
| [36531871](https://pubmed.ncbi.nlm.nih.gov/36531871/) | *ADTKD: emerging cause of genetic CKD* | Gene-based ADTKD classification | Review |
| [39976632](https://pubmed.ncbi.nlm.nih.gov/39976632/) | *ADTKD phenotype/genotype in a Japanese cohort* | Rarity of SEC61A1 (1 of 40 families) | Human clinical cohort |
| [41061854](https://pubmed.ncbi.nlm.nih.gov/41061854/) | *ADTKD-JAG1* | Differential diagnosis; haploinsufficiency parallel | Human clinical |

All three mechanistic studies ([27392076], [28782633], [32325141]) converge on the same molecular defect (impaired translocation + ER Ca²⁺ dysregulation + UPR), lending strong internal consistency. The constraint data (gnomAD) and conservation data (HomoloGene) are independent, non-literature lines of support for the dosage-sensitive dominant model.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** Fewer than ~20 patients are reported across all three arms; prevalence/incidence, penetrance, expressivity, and sex/geographic distribution remain poorly quantified.
2. **Genotype–phenotype correlation unresolved.** It is unclear why some variants predominantly cause renal disease, others immunodeficiency, and others neutropenia; no systematic structure–function map of variant position vs. organ arm exists.
3. **Dominant-negative vs. haploinsufficiency.** The relative contributions are inferred; the nonsense allele (E381*) suggests haploinsufficiency, while missense Golgi-mislocalization suggests a dominant-negative/toxic component — these may differ by variant.
4. **No whole-mammal disease model** captures the full multisystem phenotype; mechanistic work relies on zebrafish (renal) and cell lines.
5. **Therapeutics unproven in vivo.** Phenylbutyrate rescue is purely in vitro; no clinical trial data exist for any mechanism-targeted therapy.
6. **VUS burden.** ~360 of 393 ClinVar entries are VUS, complicating clinical interpretation of novel variants.
7. **Rare features** (epilepsy, microcephaly, cognitive impairment) are reported in single cases and their causal link to SEC61A1 requires replication.

---

## Proposed Follow-up Experiments / Actions

1. **Build an international SEC61A1 patient registry** to quantify prevalence, penetrance, organ-arm frequencies, and natural history across all three OMIM entities.
2. **Systematic variant functional mapping:** assay a panel of patient and ClinVar VUS variants in parallel for (a) protein translocation, (b) ER Ca²⁺ leak, (c) UPR induction, and (d) lineage-specific differentiation (plasma-cell and granulocyte in vitro assays), to resolve genotype–phenotype correlation and reclassify VUS.
3. **Generate a conditional/knock-in mouse** carrying a recurrent human variant (e.g., p.Thr185Ala) to test multisystem recapitulation and serve as a preclinical therapeutic platform.
4. **Preclinical test of 4-phenylbutyrate and other chemical chaperones / UPR modulators** (e.g., ISRIB, TUDCA) in zebrafish and patient-derived cells/organoids across renal, plasma-cell, and myeloid readouts.
5. **iPSC-derived organoid models** (kidney organoids, plasma-cell differentiation, granulopoiesis) from patient cells to dissect lineage selectivity and screen candidate drugs.
6. **Structural studies** of mutant Sec61α within the heterotrimeric channel (cryo-EM) to clarify dominant-negative assembly and channel gating/Ca²⁺-leak defects.
7. **Prospective surveillance protocols** combining renal, immune, and hematologic monitoring for genetically diagnosed individuals, and evaluation of early G-CSF/immunoglobulin/renal-protective intervention outcomes.

---

*Evidence source legend: human clinical, model organism (zebrafish), in vitro/biochemical, structural (cryo-EM), computational (gnomAD constraint, HomoloGene conservation).*


## Artifacts

- [OpenScientist final report](SEC61A1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SEC61A1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:21499241` (4 mentions) - Cryo-EM structure of the ribosome-SecYE complex in the membrane environment.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `sec61a1`, `disease`, `variant`, `renal`, `kidney`, `sec61`, `defect`, `phenotype`, `gene`, `cell`, `scn11`, `heterozygous`, `neutropenia`, `anemia`, `ckd`, `translocon`, `arm`, `congenital`, `dominant`, `missense`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 9 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100337` (5 mentions) - the report calls it "SEC61A1 deficiency", "umbrella"; MONDO calls it **SEC61A1 deficiency**
- `HP:0002149` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperuricemia**
- `HP:0000107` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Renal cyst**
- `HP:0001903` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Anemia**
- `HP:0001875` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total neutrophil count**
- `HP:0001510` (1 mention) - the report calls it "Physical"; HP calls it **Growth delay**
- `HP:0100543` (1 mention) - the report calls it "Behavioral/neuro"; HP calls it **Cognitive impairment**
- `HP:0002917` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypomagnesemia**
- `HP:0000846` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Adrenal insufficiency**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0100337` - called "SEC61A1 deficiency", "umbrella"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`, `HomoloGene`, `NCBIGene`.