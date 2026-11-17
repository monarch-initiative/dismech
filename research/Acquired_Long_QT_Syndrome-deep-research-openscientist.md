---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:42:30.331738'
end_time: '2026-11-04T18:58:17.861644'
duration_seconds: 947.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Acquired Long QT Syndrome
  mondo_id: MONDO:1060292
  category: Complex
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: aLQTS; drug-induced long QT syndrome; secondary long QT syndrome; acquired
    QT prolongation
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
citation_count: 37
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 37
  on_topic: 12
  validator_version: 0.5.1
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 6
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001657
    reported_labels:
    - Laboratory/ECG sign
    ontology_label: Prolonged QT interval
  - term_id: HP:0004755
    reported_labels:
    - Clinical sign (polymorphic VT)
    ontology_label: Supraventricular tachycardia
  - term_id: HP:0001279
    reported_labels:
    - Symptom
    ontology_label: Syncope
  - term_id: HP:0001250
    reported_labels:
    - Symptom (can mimic epilepsy)
    ontology_label: Seizure
  - term_id: HP:0001663
    reported_labels:
    - Clinical sign
    ontology_label: Ventricular fibrillation
  - term_id: HP:0001645
    reported_labels:
    - Outcome
    ontology_label: Sudden cardiac death
  - term_id: HP:0011675
    reported_labels:
    - Symptom/sign
    ontology_label: Arrhythmia
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acquired_Long_QT_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acquired_Long_QT_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acquired Long QT Syndrome
- **MONDO ID:** MONDO:1060292 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** aLQTS; drug-induced long QT syndrome; secondary long QT syndrome; acquired QT prolongation
- **Category:** Complex

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Acquired Long QT Syndrome** covering all of the
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

# Acquired Long QT Syndrome (aLQTS): A Comprehensive Disease Characterization

**MONDO:** MONDO:1060292 · **Category:** Complex (non-Mendelian) · **Principal molecular target:** *KCNH2*/hERG (Kv11.1), the IKr potassium channel

---

## Summary

**Acquired Long QT Syndrome (aLQTS)** is a complex, non-Mendelian disorder of ventricular repolarization in which a reversible external insult—most commonly a QT-prolonging drug, but also hypokalemia, bradycardia, hypomagnesemia, hypocalcemia, or metabolic/structural cardiac stress—prolongs the heart-rate-corrected QT interval (QTc) and predisposes to the polymorphic ventricular tachycardia **torsades de pointes (TdP)**, which can degenerate into ventricular fibrillation and sudden cardiac death. Unlike congenital LQTS, aLQTS has **no single causal gene**; the dominant molecular lesion is **pharmacological blockade of the rapidly activating delayed rectifier potassium current (IKr)**, carried by the channel encoded by **KCNH2 (hERG, Kv11.1; HGNC:6251)**. More than 100 structurally diverse drugs block hERG, and essentially every drug ever withdrawn for TdP liability is a hERG blocker ([PMID: 16253929](https://pubmed.ncbi.nlm.nih.gov/16253929/)).

The central organizing principle of aLQTS is **"reduced repolarization reserve"** (Roden): normal repolarization is buffered by multiple redundant potassium currents, so subclinical lesions—latent congenital mutations, common modifier alleles, electrolyte disturbance, bradycardia, structural heart disease—do not prolong QT at baseline but unmask marked QT prolongation and TdP when an IKr-blocking drug is added ([PMID: 16336514](https://pubmed.ncbi.nlm.nih.gov/16336514/)). This framework explains the idiosyncratic, patient-specific nature of the disease and frames aLQTS as a prototypical **gene–environment interaction**. Roughly **25–30% of aLQTS patients carry latent congenital LQTS mutations**, enriched in *KCNH2* ([PMID: 26715165](https://pubmed.ncbi.nlm.nih.gov/26715165/)), and common variants such as **KCNE1 D85N** confer an odds ratio of ~9 for drug-induced LQTS ([PMID: 22100668](https://pubmed.ncbi.nlm.nih.gov/22100668/)). Female sex and electrolyte abnormalities are the leading clinical risk factors.

Because the trigger is largely external and the ion-channel block is reversible, aLQTS is **highly preventable and treatable**: remove the culprit drug, correct electrolytes (keep potassium high-normal), give IV magnesium for TdP, and provide rate support (isoproterenol/pacing) for bradycardia-dependent episodes ([PMID: 26183037](https://pubmed.ncbi.nlm.nih.gov/26183037/)). Validated risk scores (Tisdale), clinical decision support, and curated drug lists (CredibleMeds/AZCERT) support prevention in hospital settings ([PMID: 36527915](https://pubmed.ncbi.nlm.nih.gov/36527915/); [PMID: 22549576](https://pubmed.ncbi.nlm.nih.gov/22549576/)).

---

## Section 1 — Disease Information

**Overview.** Acquired Long QT Syndrome is a secondary (non-inherited) prolongation of ventricular repolarization, measured on the surface ECG as a prolonged QTc, that carries a risk of TdP. It is distinct from congenital LQTS in that it is precipitated by identifiable, usually reversible, external factors—predominantly medications. The core causal target is the **KCNH2/hERG (Kv11.1)** channel conducting IKr ([PMID: 16253929](https://pubmed.ncbi.nlm.nih.gov/16253929/)).

**Key identifiers.**
- **Mondo:** MONDO:1060292
- **Synonyms:** acquired LQTS (aLQTS); drug-induced long QT syndrome (diLQTS); secondary long QT syndrome; acquired QT prolongation
- **MeSH:** Long QT Syndrome (D008133); related: Torsades de Pointes (D016171)
- **ICD-10:** I45.81 (Long QT syndrome); drug-induced forms often coded with the offending agent (T-codes) plus I45.81
- **OMIM / Orphanet / causal gene:** Not applicable in the Mendelian sense — aLQTS has no single OMIM gene entry; the congenital counterparts (LQT1 *KCNQ1*, LQT2 *KCNH2*, LQT3 *SCN5A*) are the genetic reservoir from which susceptibility is drawn.

**Data provenance.** Evidence is drawn from both **aggregated disease-level resources** (systematic reviews, pharmacovigilance databases such as FDA FAERS, curated drug lists) and **individual-patient data** (EHR cohorts, case-control genetic studies, case reports). Both sources are heavily represented in the literature reviewed.

---

## Section 2 — Etiology

**Disease causal factors.** The primary cause is **pharmacological**: drugs that block the hERG/IKr channel. Beyond direct pore block, some drugs act by **disrupting hERG trafficking** to the plasma membrane or accelerating its degradation (pentamidine, arsenic trioxide, probucol, geldanamycin) ([PMID: 24998878](https://pubmed.ncbi.nlm.nih.gov/24998878/)). Non-pharmacologic acquired causes include electrolyte derangements, bradyarrhythmias, hypothyroidism, hypothermia, starvation/anorexia, CNS injury (subarachnoid hemorrhage), Takotsubo cardiomyopathy, and myocardial ischemia/heart failure.

**Genetic risk factors.** aLQTS is polygenic/multifactorial on top of an environmental trigger:
- **Latent congenital mutations** in *KCNH2*, *KCNQ1*, *SCN5A* (and minor genes) — present in ~28% of aLQTS patients ([PMID: 26715165](https://pubmed.ncbi.nlm.nih.gov/26715165/)).
- **Common susceptibility alleles**, most robustly **KCNE1 D85N (rs1805128)**, OR 9.0 (95% CI 3.5–22.9) ([PMID: 22100668](https://pubmed.ncbi.nlm.nih.gov/22100668/)); additional candidate polymorphisms include NOS1AP variants and ethnic-specific alleles (e.g., *KCNH2* P448R/A915V in Asians; *SCN5A* S1102Y in African Americans) ([PMID: 16540748](https://pubmed.ncbi.nlm.nih.gov/16540748/)).

**Environmental/clinical risk factors.** QTc >500 ms or ΔQTc ≥60 ms from baseline, advanced age, **female sex**, acute myocardial infarction, heart failure with reduced ejection fraction, hypokalemia, hypomagnesemia, hypocalcemia, bradycardia, diuretic use, elevated drug levels from drug–drug interactions (CYP inhibition), inadequate renal dose adjustment, and rapid IV administration ([PMID: 27212965](https://pubmed.ncbi.nlm.nih.gov/27212965/)).

**Protective factors.** The inverse of the risk factors: maintaining potassium in the high-normal range, avoiding culprit drugs and QT-drug combinations, and androgenic hormonal milieu (dihydrotestosterone/androgens shorten repolarization, which may underlie lower male risk) ([PMID: 27595633](https://pubmed.ncbi.nlm.nih.gov/27595633/)). No validated protective genetic variant is established.

**Gene–environment interaction.** aLQTS is the canonical cardiac GxE disorder: a subclinical genetic/electrolyte lesion reduces repolarization reserve, and only the combination with an IKr-blocking drug exceeds the threshold for clinical QT prolongation and TdP ([PMID: 16336514](https://pubmed.ncbi.nlm.nih.gov/16336514/)).

---

## Section 3 — Phenotypes

The core phenotype is **prolonged QTc on 12-lead ECG**; QTc >500 ms strongly supports pathology and ΔQTc ≥60 ms from baseline is significant ([PMID: 41266879](https://pubmed.ncbi.nlm.nih.gov/41266879/)). Downstream phenotypes derive from the arrhythmia.

| Phenotype | Type | HPO term | Onset / course | Frequency |
|---|---|---|---|---|
| Prolonged QT interval | Laboratory/ECG sign | HP:0001657 | Acute, drug-triggered | Defining feature |
| Torsades de pointes | Clinical sign (polymorphic VT) | HP:0004755 | Episodic | Rare but serious; up to ~3.6% for methadone |
| Syncope / presyncope | Symptom | HP:0001279 | Episodic, arrhythmogenic | Variable |
| Seizure / seizure-like episodes | Symptom (can mimic epilepsy) | HP:0001250 | Episodic | Can be misdiagnosed as epilepsy |
| Ventricular fibrillation / cardiac arrest | Clinical sign | HP:0001663 | Acute | Rare |
| Sudden cardiac death | Outcome | HP:0001645 | Acute | Rare |
| Arrhythmia / palpitations | Symptom/sign | HP:0011675 | Episodic | Variable |

Many patients are **asymptomatic until a trigger** is introduced. Seizure-like episodes are a notable mimic that can delay correct diagnosis ([PMID: 23412014](https://pubmed.ncbi.nlm.nih.gov/23412014/); [PMID: 41266879](https://pubmed.ncbi.nlm.nih.gov/41266879/)). **Quality of life** is generally unaffected once the trigger is removed, as the condition is usually reversible; the burden is dominated by the acute arrhythmic risk rather than chronic disability.

---

## Section 4 — Genetic / Molecular Information

**Causal gene (molecular target).** **KCNH2** (hERG, Kv11.1; HGNC:6251; chromosome 7q36.1; NCBI Gene 3757) encodes the pore-forming subunit of the IKr channel — the dominant drug target in aLQTS ([PMID: 16253929](https://pubmed.ncbi.nlm.nih.gov/16253929/)). Secondary contributing genes: *KCNQ1* (IKs), *SCN5A* (late INa), *KCNE1*/*KCNE2* (β-subunits).

**Latent pathogenic variants.** In an international cohort of 188 aLQTS probands screened across the five major LQTS genes, **53 (28%) carried 47 disease-causing mutations**. In "true aLQTS" (normal baseline QTc off triggers), **KCNH2 mutations were much more frequent than KCNQ1 (64% [95% CI 43–82%] vs 20% [95% CI 7–41%], P < 0.01)**. The control QTc of aLQTS patients (453±39 ms) was intermediate between congenital LQTS (478±46 ms) and non-carriers (406±26 ms) ([PMID: 26715165](https://pubmed.ncbi.nlm.nih.gov/26715165/)). Variant classes are predominantly **missense** loss-of-function (K-channel) or gain-of-function (Na-channel), classified per ACMG/AMP.

**Common modifier variant.** **KCNE1 D85N (rs1805128)** predicted diLQTS with **OR 9.0 (95% CI 3.5–22.9)**; variant allele present in 8.6% of cases, 2.9% of drug-exposed controls, 1.8% of population controls, replicated in a validation cohort (3.5% cases vs 1.4% controls) ([PMID: 22100668](https://pubmed.ncbi.nlm.nih.gov/22100668/)). KCNE1 encodes the MinK β-subunit modulating IKs.

**Functional consequences.** Potassium-channel variants → **loss of function** of repolarizing current; sodium-channel variants (*SCN5A*) → **gain of function** (sustained late inward sodium current). Trafficking-disrupting drugs reduce **membrane hERG expression** independent of pore block ([PMID: 24998878](https://pubmed.ncbi.nlm.nih.gov/24998878/)).

**Origin.** Germline (inherited susceptibility variants); the disease itself is **not somatic**. **Epigenetic and chromosomal abnormalities** are not established contributors to aLQTS.

---

## Section 5 — Environmental Information

**Pharmacological (dominant environmental factor).** See Section 12 culprit-drug table. Over 100 structurally diverse drugs block hERG; chemical-motif analysis of >300,000 compounds shows why structurally unrelated agents share this liability ([PMID: 16253929](https://pubmed.ncbi.nlm.nih.gov/16253929/); [PMID: 25700001](https://pubmed.ncbi.nlm.nih.gov/25700001/)).

**Electrolyte/metabolic.** Hypokalemia (graded dose-response with severe QT prolongation, P-trend <0.001), hypomagnesemia, and hypocalcemia ([PMID: 41397500](https://pubmed.ncbi.nlm.nih.gov/41397500/); [PMID: 35103080](https://pubmed.ncbi.nlm.nih.gov/35103080/)).

**Lifestyle / physiologic.** Bradycardia, starvation/anorexia nervosa, liquid protein diets, hypothermia. **Infectious agents:** not a direct cause, though infection-associated QT prolongation occurs via drugs, fever, and electrolyte shifts (e.g., COVID-19 treatment cohorts) ([PMID: 33963634](https://pubmed.ncbi.nlm.nih.gov/33963634/)).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

```
1. External trigger (IKr/hERG-blocking drug, OR trafficking-disrupting drug,
   OR hypokalemia/hypomagnesemia/bradycardia)
        │  leads to
2. Reduction of net repolarizing K+ current (IKr), ± reduced membrane hERG
   (trafficking block) — INFERRED to summate with any latent genetic lesion
        │  results in  (branch: amplified where repolarization reserve is already reduced —
        │               latent KCNH2/KCNQ1/SCN5A variant, KCNE1 D85N, female sex, structural disease)
3. Prolongation of ventricular action potential duration (APD) and QT interval
        │  permits
4. Reactivation of L-type Ca2+ current (ICaL) and/or enhanced late INa during phase 2/3
        │  generates
5. Early afterdepolarizations (EADs) in mid-myocardial (M) cells
        │  triggers
6. Triggered activity → focal premature ventricular excitation
        │  propagates into (requires)
7. A substrate of inhomogeneous/dispersed repolarization (transmural dispersion;
   M-cells vs epi/endocardium) with a concave repolarization-boundary geometry
        │  produces
8. Functional reentry → TORSADES DE POINTES (polymorphic VT)
        │  may degenerate to
9. Ventricular fibrillation → syncope / cardiac arrest / SUDDEN CARDIAC DEATH
```

### Detail

**Molecular/biochemical defect.** The upstream lesion is a **cardiac ion-channel defect**: reduced IKr through hERG/Kv11.1. Drugs bind promiscuously within the hERG inner cavity; chemical-motif analysis of >300,000 compounds identified many scaffolds enriched for hERG inhibition, explaining why structurally unrelated agents share this liability ([PMID: 25700001](https://pubmed.ncbi.nlm.nih.gov/25700001/)). A parallel branch is **trafficking disruption**, reducing surface channel density ([PMID: 24998878](https://pubmed.ncbi.nlm.nih.gov/24998878/)).

**Cellular process.** Prolonged APD allows **ICaL reactivation / late-INa persistence**, generating EADs. EADs are the *trigger*; a *substrate* of dispersed repolarization is required for reentry. "TdP is initiated by triggered activity due to early afterdepolarization (EAD) and maintained by reentry within a substrate of inhomogeneous repolarization" ([PMID: 38504714](https://pubmed.ncbi.nlm.nih.gov/38504714/)). Computational tissue models show reentry forms only when EAD clusters create a **concave repolarization-boundary geometry** ([PMID: 37515880](https://pubmed.ncbi.nlm.nih.gov/37515880/); [PMID: 39837062](https://pubmed.ncbi.nlm.nih.gov/39837062/)).

**Experimental recapitulation.** Human engineered heart tissues reproduce the mechanism: hERG blockade (E-4031) prolongs APD, and combining hERG inhibition with **hypokalemia + hypomagnesemia** produces VT with marked beat-to-beat instability ([PMID: 41727060](https://pubmed.ncbi.nlm.nih.gov/41727060/)).

**Upstream vs downstream.** Upstream = channel block / reduced reserve → APD prolongation (ionic/cellular). Downstream = EAD → triggered activity → reentry → TdP (tissue-level). **Cell types:** ventricular cardiomyocytes, especially **mid-myocardial M-cells** (CL:0000746, cardiac muscle cell; CL:0002129, regular ventricular cardiac myocyte). **GO terms:** GO:0086009 (membrane repolarization), GO:0098915 (membrane repolarization during ventricular cardiac muscle cell action potential), GO:0086091 (regulation of heart rate by cardiac conduction), GO:0005251 (delayed rectifier potassium channel activity). **CHEBI:** potassium(1+) (CHEBI:29103), magnesium(2+) (CHEBI:18420).

---

## Section 7 — Anatomical Structures Affected

- **Organ:** Heart (UBERON:0000948), specifically the **cardiac ventricles** (UBERON:0002082) and ventricular myocardium (UBERON:0002349). Body system: **cardiovascular** (UBERON:0004535). Secondary: brain (hypoxic injury from arrhythmia/syncope).
- **Tissue/cell:** Ventricular **cardiac muscle** (striated); affected cells are **ventricular cardiomyocytes**, with **mid-myocardial M-cells** central to transmural dispersion of repolarization (CL:0000746, CL:0002129).
- **Subcellular:** Plasma membrane ion channels (GO:0005886), sarcolemmal **voltage-gated potassium channel complex** (GO:0008076); endoplasmic reticulum/Golgi relevant to the hERG trafficking branch (GO:0005783, GO:0005794).
- **Localization:** Bilateral/diffuse ventricular involvement; no lateralization.

---

## Section 8 — Temporal Development

- **Onset:** Acute to subacute, tied to drug exposure or metabolic insult. Can occur at **any age**; older adults are over-represented (median age ~72 in a Swedish TdP cohort) ([PMID: 41553550](https://pubmed.ncbi.nlm.nih.gov/41553550/)), but cases span neonates/infants to the elderly ([PMID: 41896159](https://pubmed.ncbi.nlm.nih.gov/41896159/)).
- **Progression/course:** **Episodic and reversible.** QT prolongation develops over hours to days after drug initiation/dose increase; TdP is typically self-limited or terminated by intervention. The condition is **not chronic** once the trigger is removed.
- **Remission:** Treatment-induced remission is the norm — QTc normalizes after drug withdrawal and electrolyte correction.
- **Critical period:** The vulnerable window is during active drug exposure, especially with concurrent electrolyte disturbance, bradycardia, or multiple QT drugs — the key opportunity for monitoring and intervention.

---

## Section 9 — Inheritance and Population

**Epidemiology.** Incidence of QTc >500 ms varies widely by drug and setting (0–16.2% for methadone; TdP prevalence up to 3.6%) ([PMID: 42735272](https://pubmed.ncbi.nlm.nih.gov/42735272/)). In a prolonged-QTc inpatient cohort (n=2,735), **89 (3%) developed TdP** ([PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/)). In a Swedish population cohort of 762 TdP patients (50% female, median age 72), 59% had been dispensed ≥1 risk drug and 73% had a risk drug and/or risk diagnosis ([PMID: 41553550](https://pubmed.ncbi.nlm.nih.gov/41553550/)).

**Inheritance.** aLQTS is **multifactorial/complex**, not Mendelian. Susceptibility is **polygenic** (latent rare variants + common modifiers) interacting with environment. Penetrance of latent variants is **incomplete and trigger-dependent**.

**Sex ratio.** Strong **female predominance** of TdP risk (140/188 probands female; ~50–55% of cohorts female but higher per-exposure risk) ([PMID: 26715165](https://pubmed.ncbi.nlm.nih.gov/26715165/); [PMID: 27595633](https://pubmed.ncbi.nlm.nih.gov/27595633/)). Notably, controlled crossover studies (dofetilide, quinidine, ranolazine, verapamil) found **no sex difference in concentration-adjusted QTc prolongation**, implying the excess female risk reflects lower baseline repolarization reserve/hormonal state rather than greater drug-induced QT lengthening per exposure ([PMID: 26324176](https://pubmed.ncbi.nlm.nih.gov/26324176/)).

**Population demographics.** Older adults, patients with heart failure/MI, and those on polypharmacy are over-represented. Ethnic-specific modifier alleles exist (*KCNH2* P448R/A915V in Asians; *SCN5A* S1102Y in African Americans) ([PMID: 16540748](https://pubmed.ncbi.nlm.nih.gov/16540748/)).

---

## Section 10 — Diagnostics

**Principal test:** **12-lead ECG** with QTc measurement (Bazett/Fridericia/Framingham). Diagnostic support: **QTc >500 ms on ≥2 ECGs** and/or **ΔQTc ≥60 ms from baseline** ([PMID: 41266879](https://pubmed.ncbi.nlm.nih.gov/41266879/); [PMID: 38982033](https://pubmed.ncbi.nlm.nih.gov/38982033/)). Continuous telemetry for at-risk inpatients.

**Laboratory:** serum potassium, magnesium, calcium; renal/hepatic function; thyroid function; drug levels where applicable. Correct hypokalemia/hypomagnesemia.

**Risk stratification tools.**

| Tool | Variables | Output | Evidence |
|---|---|---|---|
| **Tisdale score** (0–23) | Age >68, female, loop diuretic, K+ ≤3.5, admission QTc ≥450, acute MI, sepsis, HF, ≥1/≥2 QT drugs | Low ≤6 / Mod 7–10 / High ≥11 | Mortality OR 4.80 (7–10) and 11.51 (≥11) vs <7 in 92,383 inpatients ([PMID: 36527915](https://pubmed.ncbi.nlm.nih.gov/36527915/)) |
| **RISQ-PATH** | EHR-derived clinical factors | Risk probability | Outperformed by ML in head-to-head ([PMID: 41139036](https://pubmed.ncbi.nlm.nih.gov/41139036/)) |
| **Machine-learning (XGBoost/DNN)** | EHR + ECG traces | AUROC 0.86–0.87 | Superior to Tisdale/RISQ-PATH ([PMID: 41139036](https://pubmed.ncbi.nlm.nih.gov/41139036/); [PMID: 42951254](https://pubmed.ncbi.nlm.nih.gov/42951254/)) |

**Genetic testing.** Not routine for isolated drug-induced events, but **targeted LQTS gene panel (KCNQ1, KCNH2, SCN5A, KCNE1, KCNE2)** is warranted when baseline QTc is prolonged off triggers, there is a family history, or TdP occurred with minimal provocation — ~28% yield of latent mutations ([PMID: 26715165](https://pubmed.ncbi.nlm.nih.gov/26715165/)). KCNE1 D85N genotyping is a research/risk-modifier tool ([PMID: 22100668](https://pubmed.ncbi.nlm.nih.gov/22100668/)).

**Differential diagnosis.** Congenital LQTS (persistent QTc off triggers; family history), electrolyte-only QT prolongation, epilepsy (seizure-like syncope mimics), structural VT, Takotsubo. Distinguish by reversibility after trigger removal.

---

## Section 11 — Outcome / Prognosis

**Prognosis is generally excellent once the trigger is removed** — QTc normalizes and arrhythmic risk resolves. The acute danger is TdP progressing to VF and sudden death. Mortality and length-of-stay track the Tisdale score: vs QTc-RS <7, mortality **OR 4.80 (95% CI 4.42–5.21) for score 7–10** and **11.51 (95% CI 10.23–12.94) for ≥11**, with length of stay rising ~0.7 day per point ([PMID: 36527915](https://pubmed.ncbi.nlm.nih.gov/36527915/)). Severe QTc prolongation is associated with ~3-fold higher ventricular arrhythmia risk and ~2-fold SCD risk among antipsychotic/antidepressant users ([PMID: 41397500](https://pubmed.ncbi.nlm.nih.gov/41397500/)). Prognostic factors: magnitude of QTc, number of risk factors/QT drugs, electrolyte status, structural heart disease, and presence of latent genetic susceptibility.

---

## Section 12 — Treatment

**Acute management of TdP** ([PMID: 26183037](https://pubmed.ncbi.nlm.nih.gov/26183037/)):
1. **Discontinue the culprit QT-prolonging drug(s)**.
2. **IV magnesium sulfate** — first-line for TdP, even if serum Mg is normal.
3. **Correct electrolytes** — keep potassium in the high-normal range; replete magnesium/calcium.
4. **Electrical cardioversion/defibrillation** for sustained/hemodynamically unstable episodes.
5. **Rate acceleration** — isoproterenol or transvenous pacing for recurrent/bradycardia-dependent (pause-dependent) TdP.
6. **Avoid** repolarization-prolonging antiarrhythmics (Class IA/III).

Direct quote: *"Immediate treatment of TdP is by intravenous administration of magnesium sulphate, terminating prolonged episodes using electrical cardioversion. In refractory cases of recurrent TdP, the arrhythmia can be suppressed by increasing the underlying heart rate using isoproterenol (isoprenaline) or transvenous pacing"* ([PMID: 26183037](https://pubmed.ncbi.nlm.nih.gov/26183037/)). NCIT intervention concepts: Magnesium Sulfate Therapy, Electrical Cardioversion, Cardiac Pacing, Isoproterenol.

**Pharmacogenomics / drug–drug interactions.** CYP3A4/CYP2D6/CYP1A2 inhibition raises culprit-drug plasma levels and TdP risk (e.g., ritonavir increasing hydroxychloroquine/lopinavir exposure) ([PMID: 36437717](https://pubmed.ncbi.nlm.nih.gov/36437717/)). Genotype-aware prescribing and KCNE1/latent-variant status inform personalized risk.

**Culprit drug classes (all hERG/IKr blockers unless noted):** Class IA/III antiarrhythmics (quinidine, disopyramide, sotalol, dofetilide, ibutilide, amiodarone); macrolides/fluoroquinolones (erythromycin, clarithromycin, azithromycin, moxifloxacin, ciprofloxacin); azole antifungals; antimalarials (hydroxychloroquine, chloroquine, halofantrine); antipsychotics (haloperidol, thioridazine, quetiapine, ziprasidone); antidepressants (citalopram/escitalopram, TCAs); antiemetics (ondansetron, domperidone); methadone; ranolazine; oncology agents (arsenic trioxide, anthracyclines, TKIs) ([PMID: 26926294](https://pubmed.ncbi.nlm.nih.gov/26926294/)). **Trafficking inhibitors:** pentamidine, arsenic trioxide, probucol.

| Drug | Association metric | Source |
|---|---|---|
| Ranolazine | TdP OR 53.6 (95% CI 5.4–524) | [PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) |
| Dofetilide | TdP OR ~25 | [PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) |
| Furosemide (via hypokalemia) | 39.3% of TdP cases | [PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) |
| Methadone | 27% of TdP cases | [PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) |
| SSRIs | 19.1% of TdP cases | [PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) |
| Amiodarone | 18% of TdP cases | [PMID: 26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) |

---

## Section 13 — Prevention

aLQTS is **largely preventable**. The AHA/ACCF scientific statement *"Prevention of Torsade de Pointes in Hospital Settings"* (Drew et al., 2010) codifies the approach: identify at-risk patients (proarrhythmic drugs, electrolyte disturbances, bradyarrhythmias) for QT-interval monitoring, avoid/limit concurrent QT-prolonging drugs, and correct hypokalemia/hypomagnesemia ([PMID: 20142454](https://pubmed.ncbi.nlm.nih.gov/20142454/); [PMID: 22549576](https://pubmed.ncbi.nlm.nih.gov/22549576/)).

- **Primary prevention:** curated avoidance lists (**CredibleMeds/AZCERT** known/possible/conditional TdP risk), preclinical hERG screening (ICH S7B/E14, CiPA), electrolyte stewardship, dose adjustment in renal impairment, and avoiding QT-drug combinations ([PMID: 20047143](https://pubmed.ncbi.nlm.nih.gov/20047143/)).
- **Secondary prevention:** baseline and on-treatment ECG monitoring, telemetry for high-risk patients, **clinical decision support alerts**, and risk scores (Tisdale/RISQ-PATH/ML) ([PMID: 41139036](https://pubmed.ncbi.nlm.nih.gov/41139036/); [PMID: 41208201](https://pubmed.ncbi.nlm.nih.gov/41208201/)).
- **Tertiary prevention / counseling:** when a latent congenital variant is unmasked, **genetic counseling and cascade screening** of relatives.

---

## Section 14 — Other Species / Natural Disease

aLQTS is fundamentally an **induced** phenotype rather than a naturally occurring heritable disease, so there is limited "natural disease" literature in other species. The hERG channel and IKr are **evolutionarily conserved** across mammals, and drug-induced QT prolongation is well documented in **dog** (canine, NCBI Taxon 9615) and **rabbit** (Oryctolagus cuniculus, Taxon 9986) models used for preclinical cardiac safety. Orthologous gene: *KCNH2* (human NCBI Gene 3757) with orthologs in mouse (*Kcnh2*), rat, dog, and zebrafish (*kcnh2/zERG*). Zoonotic/transmission considerations do not apply.

---

## Section 15 — Model Organisms

| Model | Type | Use | Evidence |
|---|---|---|---|
| **Heterologous hERG cells** (HEK293/CHO) | In vitro | Patch-clamp hERG screening; ICH S7B/E14 standard | [PMID: 20047143](https://pubmed.ncbi.nlm.nih.gov/20047143/), [PMID: 25700001](https://pubmed.ncbi.nlm.nih.gov/25700001/) |
| **Human iPSC-CMs** | In vitro / cellular | CiPA initiative; sex-specific repolarization-reserve studies | [PMID: 30247688](https://pubmed.ncbi.nlm.nih.gov/30247688/) |
| **Human engineered heart tissue (EHT)** | 3D in vitro | Recapitulates hERG-block + electrolyte-driven VT | [PMID: 41727060](https://pubmed.ncbi.nlm.nih.gov/41727060/) |
| **Zebrafish** (Danio rerio) | Whole-organism | Acquired & inherited LQT2; delayed repolarization | [PMID: 33519527](https://pubmed.ncbi.nlm.nih.gov/33519527/) |
| **Rabbit/canine wedge, transgenic** | Mammalian | Transmural dispersion, EAD/TdP | [PMID: 38504714](https://pubmed.ncbi.nlm.nih.gov/38504714/) |
| **In silico virtual populations** | Computational | Sex-aware proarrhythmia prediction | [PMID: 42216678](https://pubmed.ncbi.nlm.nih.gov/42216678/) |

**Phenotype recapitulation:** sex-specific hiPSC-CMs reproduce the female repolarization-reserve deficit ("differential expression of KCNE1 gene and reduced repolarization reserve in female-derived hiPSC-CMs," [PMID: 30247688](https://pubmed.ncbi.nlm.nih.gov/30247688/)); EHTs reproduce the EAD→VT cascade under combined hERG block + hypokalemia/hypomagnesemia; zebrafish reproduce whole-organ delayed repolarization ("Drug block of hERG channels or dysfunctional channel variants can result in acquired or inherited LQTS2," [PMID: 33519527](https://pubmed.ncbi.nlm.nih.gov/33519527/)). **Limitation:** no model fully captures the polygenic human susceptibility background, and small-animal repolarization currents differ from human.

---

## Mechanistic Model / Interpretation

The entire disease collapses onto a single quantitative idea — **repolarization reserve** — pushed past a threshold:

```
            NET REPOLARIZING CURRENT (reserve)
   high │█████████████████████  ← healthy: drug tolerated, QT normal
        │███████████████▓▓▓▓▓▓  ← latent KCNH2 variant / KCNE1 D85N / female /
        │                          hypokalemia: still normal QT at baseline
threshold├─────────────────────── ← TdP risk threshold
        │████████▓▓▓░░░░░░░░░░░  ← + IKr-blocking drug: QT prolongs, EADs form
   low  │███░░░░░░░░░░░░░░░░░░░  ← + 2nd QT drug / bradycardia: TdP
```

Two independent "hits" are needed: a **substrate** (reduced reserve, often silent) and a **trigger** (drug/electrolyte). Upstream events are ionic (reduced IKr → longer APD); the pivotal cellular event is the **EAD**; the tissue-level requirement for lethality is **dispersed repolarization** enabling reentry. This explains why population-level QT prolongation is common but TdP is rare, why risk is idiosyncratic, and why prevention (removing the trigger) is so effective.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [16253929](https://pubmed.ncbi.nlm.nih.gov/16253929/) | Establishes KCNH2/hERG block as dominant mechanism; drugs withdrawn for TdP are hERG blockers |
| [24998878](https://pubmed.ncbi.nlm.nih.gov/24998878/) | hERG trafficking-disruption branch of mechanism |
| [26715165](https://pubmed.ncbi.nlm.nih.gov/26715165/) | 28% latent congenital mutations; KCNH2 > KCNQ1 enrichment |
| [22100668](https://pubmed.ncbi.nlm.nih.gov/22100668/) | KCNE1 D85N OR 9.0 — validated common susceptibility allele |
| [16336514](https://pubmed.ncbi.nlm.nih.gov/16336514/) | Reduced repolarization reserve framework |
| [27212965](https://pubmed.ncbi.nlm.nih.gov/27212965/) | Consolidated TdP risk-factor list |
| [27595633](https://pubmed.ncbi.nlm.nih.gov/27595633/) / [30247688](https://pubmed.ncbi.nlm.nih.gov/30247688/) | Female sex as independent risk factor; mechanistic basis |
| [26324176](https://pubmed.ncbi.nlm.nih.gov/26324176/) | No sex difference in concentration-adjusted QTc — reserve, not drug-handling |
| [36527915](https://pubmed.ncbi.nlm.nih.gov/36527915/) / [38982033](https://pubmed.ncbi.nlm.nih.gov/38982033/) | Tisdale score and mortality gradient |
| [38504714](https://pubmed.ncbi.nlm.nih.gov/38504714/) | EAD-trigger + reentry-substrate mechanism of TdP |
| [41727060](https://pubmed.ncbi.nlm.nih.gov/41727060/) | Human EHT recapitulating hERG-block + electrolyte VT |
| [26183037](https://pubmed.ncbi.nlm.nih.gov/26183037/) | Acute TdP management algorithm |
| [26589717](https://pubmed.ncbi.nlm.nih.gov/26589717/) / [26926294](https://pubmed.ncbi.nlm.nih.gov/26926294/) | Culprit-drug rankings and classes |
| [20142454](https://pubmed.ncbi.nlm.nih.gov/20142454/) / [22549576](https://pubmed.ncbi.nlm.nih.gov/22549576/) | AHA/ACCF prevention statement |
| [25700001](https://pubmed.ncbi.nlm.nih.gov/25700001/) / [33519527](https://pubmed.ncbi.nlm.nih.gov/33519527/) | hERG promiscuity; zebrafish model |
| [16540748](https://pubmed.ncbi.nlm.nih.gov/16540748/) | Ethnic-specific modifier alleles; LQTS channelopathy review |

---

## Limitations and Knowledge Gaps

- **No single causal gene:** aLQTS is defined by an external trigger acting on a polygenic/environmental background; conventional OMIM-style gene annotation does not apply and the genetic architecture beyond KCNE1 D85N and latent LQTS variants is incompletely mapped.
- **TdP is rare and idiosyncratic**, making prospective quantification of absolute risk difficult; most data are from case-control, pharmacovigilance (reporting bias), and EHR cohorts rather than randomized designs.
- **Sex-difference mechanism** remains partly unresolved — crossover studies show no per-exposure QTc difference, pointing to baseline reserve/hormonal effects that are hard to quantify clinically.
- **Risk scores (Tisdale/RISQ-PATH)** have modest discrimination; ML models improve AUROC but need prospective validation and lack generalizability guarantees.
- **Trafficking-disruption pathway** is less well characterized than direct pore block and may be under-recognized in safety screening.
- **No validated protective genetic variant** is established.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective validation of ML risk models** (XGBoost + ECG-DNN) against Tisdale in multi-center inpatient cohorts, with calibration and net-benefit analysis.
2. **Polygenic risk score** combining KCNE1 D85N, NOS1AP, and latent rare LQTS variants to predict diLQTS, tested in drug-exposed EHR biobanks.
3. **Sex-aware iPSC-CM / EHT panels** to dissect the hormonal and KCNE1-expression basis of female susceptibility and to test whether androgen supplementation raises reserve.
4. **Systematic trafficking-liability screening** (surface-hERG assays) added to CiPA-style preclinical pipelines to capture non-pore-block mechanisms.
5. **Quality-improvement trials** of CDS alerts + electrolyte stewardship bundles to measure reduction in QTc >500 ms and TdP incidence.
6. **Cascade genetic screening protocols** for relatives of patients in whom a latent congenital variant is unmasked by aLQTS.

---

*Report compiled from 14 confirmed findings and 51 reviewed papers across a 5-iteration autonomous investigation. Evidence types span human clinical cohorts, pharmacovigilance databases, in vitro/iPSC and engineered-tissue models, zebrafish, and computational simulation.*


## Artifacts

- [OpenScientist final report](Acquired_Long_QT_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acquired_Long_QT_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 37 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001657` (1 mention) - the report calls it "Laboratory/ECG sign"; HP calls it **Prolonged QT interval**
- `HP:0004755` (1 mention) - the report calls it "Clinical sign (polymorphic VT)"; HP calls it **Supraventricular tachycardia**
- `HP:0001279` (1 mention) - the report calls it "Symptom"; HP calls it **Syncope**
- `HP:0001250` (1 mention) - the report calls it "Symptom (can mimic epilepsy)"; HP calls it **Seizure**
- `HP:0001663` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ventricular fibrillation**
- `HP:0001645` (1 mention) - the report calls it "Outcome"; HP calls it **Sudden cardiac death**
- `HP:0011675` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Arrhythmia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000948` (1 mention) - the report calls it "Organ:** Heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names
- `UBERON:0004535` (1 mention) - the report calls it "cardiovascular"; UBERON calls it **cardiovascular system**
- `GO:0005886` (1 mention) - the report calls it "Subcellular:** Plasma membrane ion channels"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names