---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T16:55:47.908353'
end_time: '2026-11-09T17:26:53.458117'
duration_seconds: 1865.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: RAB28-Related Retinopathy
  mondo_id: MONDO:0100448
  category: Mendelian
  causal_genes: RAB28
  omim_id: not recorded
  synonyms: RAB28 retinopathy
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
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 0
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0100448
    reported_labels:
    - MONDO
    ontology_label: RAB28-related retinopathy
  - term_id: HP:0000548
    reported_labels:
    - Clinical sign (ERG)
    ontology_label: Cone/cone-rod dystrophy
  - term_id: HP:0008061
    reported_labels:
    - Physical sign
    ontology_label: Aplasia/Hypoplasia of the retina
  - term_id: HP:0007894
    reported_labels:
    - Clinical sign
    ontology_label: Fundus hypopigmentation
  - term_id: HP:0000551
    reported_labels:
    - Symptom
    ontology_label: Color vision defect
  - term_id: HP:0000613
    reported_labels:
    - Symptom
    ontology_label: Photophobia
  - term_id: CL:0000573
    reported_labels:
    - "Tissue/cell:** Neural retina photoreceptors \u2014 cones"
    ontology_label: retinal cone cell
  - term_id: NCIT:C15431
    reported_labels:
    - NCIT suggestions:** Gene Therapy
    ontology_label: Hematopoietic Cell Transplantation
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: RAB28-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RAB28-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RAB28-Related Retinopathy
- **MONDO ID:** MONDO:0100448 (if available)
- **Causal gene(s):** RAB28
- **OMIM:** not recorded
- **Synonyms:** RAB28 retinopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **RAB28-Related Retinopathy** covering all of the
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

# RAB28-Related Retinopathy (Cone-Rod Dystrophy 18): A Comprehensive Disease Characterization

**Disease:** RAB28-Related Retinopathy | **Causal gene:** **RAB28** | **MONDO:** [MONDO:0100448](https://monarchinitiative.org/MONDO:0100448) | **OMIM disease:** 615374 (CORD18) | **OMIM gene:** *612994 | **Category:** Mendelian, non-syndromic inherited retinal dystrophy

---

## Summary

**RAB28-Related Retinopathy** is a rare, non-syndromic, autosomal-recessive **cone-rod dystrophy (CORD18)** caused by biallelic loss-of-function variants in **RAB28**, a gene encoding a farnesylated small Ras-related GTPase of the Rab family that is highly expressed in photoreceptors and functions at the ciliary apparatus. The disease is cataloged as OMIM 615374, MONDO:0100448, and the causal gene as OMIM *612994 / HGNC:9764 (chromosome 4p15.33). This report focuses on the disease defined by these identifiers and its causal gene **RAB28** — not the neighboring **PROM1** locus, which maps to the same homozygous interval and has caused diagnostic confusion in at least one consanguineous family.

The clinical phenotype is a progressive, childhood-to-early-adult-onset deterioration of central and color vision, with macular hyperpigmentation, retinal pigment epithelium (RPE) and macular atrophy, photoreceptor-layer thinning on optical coherence tomography (OCT), and a full-field electroretinogram (ERG) signature of severely reduced **cone** responses with milder **rod** reduction (the cone-predominant "cone-rod" pattern). Disease was first established in 2013 through two consanguineous/isolated families (German and Moroccan-Jewish) harboring homozygous nonsense mutations, and has since been reported across European, North-African/Middle-Eastern, Italian, and Korean backgrounds, remaining genetically homogeneous.

Mechanistically, RAB28 localizes to the photoreceptor basal body, connecting cilium and ciliary rootlet, and associates with intraflagellar transport (IFT) trains and the BBSome. Loss of RAB28 function impairs **RPE phagocytosis of (cone) outer segments**, blunts the circadian dawn/dusk peaks of outer-segment phagocytosis (OSP), disrupts **visual-cycle retinoid recycling** (reduced 11-cRAL, 11cRP, atRP), and dysregulates **ciliary extracellular-vesicle (EV) shedding** via the BBSome. These converging defects culminate in progressive cone-then-rod photoreceptor dysfunction and degeneration. There is currently **no approved therapy**; management is supportive/low-vision rehabilitation plus genetic counseling. Cone-targeted gene replacement rescues the OSP defect in zebrafish, making AAV-based gene supplementation the leading experimental therapeutic strategy.

---

## Key Findings

### Finding 1 — RAB28 loss-of-function causes autosomal-recessive cone-rod dystrophy (CORD18)

RAB28-related retinopathy was defined by a combined homozygosity-mapping and exome-sequencing study that identified recessive nonsense mutations segregating with arCRD in two unrelated families. In a German family with three affected siblings, a homozygous **c.565C>T (p.Glu189\*)** variant was found; in a family of Moroccan-Jewish descent with two affected siblings, a homozygous **c.409C>T (p.Arg137\*)** variant was found. As the original report states: *"A combined approach of homozygosity mapping and exome sequencing revealed a homozygous nonsense mutation (c.565C>T [p.Glu189\*]) in RAB28 in a German family with three siblings with arCRD. Another homozygous nonsense mutation (c.409C>T [p.Arg137\*]) was identified in a family of Moroccan Jewish descent with two siblings affected by arCRD"* ([PMID: 23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/)).

All five affected individuals shared a consistent clinical picture: *"All five affected individuals presented with hyperpigmentation in the macula, progressive loss of the visual acuity, atrophy of the retinal pigment epithelium, and severely reduced cone and rod responses on the electroretinogram"* ([PMID: 23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/)). The recessive inheritance, the nonsense nature of the variants (predicted null alleles), and the shared phenotype together establish RAB28 loss-of-function as the disease cause. Disease OMIM is 615374 (CORD18); gene OMIM is *612994; MONDO:0100448.

**Phenotype (HPO) annotations:** Cone-rod dystrophy (HP:0000548), abnormal electroretinogram (HP:0000512), abnormality of macular pigmentation (HP:0008061), retinal pigment epithelial atrophy (HP:0007894), reduced visual acuity (decreased), progressive visual loss (HP:0000529), dyschromatopsia (HP:0000551), photophobia (HP:0000613).

### Finding 2 — RAB28 is a farnesylated ciliary GTPase at the basal body / connecting cilium, associated with IFT and the BBSome

Unlike most Rab GTPases, RAB28 carries an atypical prenylation signal: *"Opposed to other Rab GTPases that are generally geranylgeranylated, RAB28 is predicted to be farnesylated. Staining of rat retina showed localization of RAB28 to the basal body and the ciliary rootlet of the photoreceptors"* ([PMID: 23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/)). This farnesyl (C15) lipid anchor is mechanistically relevant because it governs membrane association and trafficking of the GTPase.

Developmental expression profiling in *C. elegans* confirmed a dedicated ciliary role: *"this small GTPase is exclusively expressed in ciliated neurons where it dynamically associates with IFT trains"* ([PMID: 27930654](https://pubmed.ncbi.nlm.nih.gov/27930654/)). RAB28's distribution along the cilium depends on its GTP/GDP nucleotide state and on BBSome association, placing it within the ciliary intraflagellar transport machinery that is essential for photoreceptor outer-segment maintenance.

**Ontology annotations:** GTPase activity (GO:0003924), small GTPase mediated signal transduction (GO:0007264), protein farnesylation (GO:0018343), ciliary basal body (GO:0036064), photoreceptor connecting cilium (GO:0032391), intraflagellar transport (GO:0042073), BBSome (GO:0034464). Cell types: retinal cone cell (CL:0000573), retinal rod cell (CL:0000604), ciliated sensory neuron.

### Finding 3 — RAB28 is required for RPE phagocytosis of (cone) outer segments and for visual-cycle retinoid recycling

The downstream cellular consequence of RAB28 loss is a defect in the daily renewal of photoreceptor outer segments. In rodent and zebrafish models, *"the absence of Rab28 results in diminished dawn, photoreceptor, outer segment phagocytosis (OSP)"* ([PMID: 35471581](https://pubmed.ncbi.nlm.nih.gov/35471581/)). The circadian peaks of OSP (dawn for rods, with dusk contributions) are selectively blunted, while basal phagocytosis is preserved — implicating RAB28 in the regulated, high-throughput component of outer-segment turnover rather than constitutive clearance.

This OSP defect is coupled to a measurable disruption of the retinoid (visual) cycle: *"retinoid levels of 11-cRAL, 11cRP, and atRP are significantly reduced in larval and adult rab28 KO retinae (p < .05)"* ([PMID: 35471581](https://pubmed.ncbi.nlm.nih.gov/35471581/)). Reduced 11-cis-retinal (11-cRAL, the chromophore of opsin) directly compromises phototransduction capacity.

The requirement is especially pronounced for cones. In mouse, *"The small GTPase RAB28 is required for phagocytosis of cone outer segments by the murine retinal pigmented epithelium"* ([PMID: 30228185](https://pubmed.ncbi.nlm.nih.gov/30228185/)), consistent with the cone-predominant ERG deficit seen in patients. In zebrafish, *"Genetic Deletion of Zebrafish Rab28 Causes Defective Outer Segment Shedding, but Not Retinal Degeneration"* ([PMID: 32258030](https://pubmed.ncbi.nlm.nih.gov/32258030/)) — a key model limitation indicating that the primary molecular lesion (defective OS shedding/phagocytosis) can be dissociated from overt degeneration in the fish, highlighting species differences in disease tempo.

**Ontology annotations:** photoreceptor outer segment (GO:0001750), retina homeostasis (GO:0001895), photoreceptor cell maintenance (GO:0045494), visual perception (GO:0007601), retinoid metabolic process (GO:0001523), phagocytosis (GO:0006909). Cell types: retinal pigment epithelial cell (CL:0002586). CHEBI: 11-cis-retinal (CHEBI:16066), retinoid.

### Finding 4 — Ciliary Rab28 and the BBSome negatively regulate extracellular-vesicle (EV) shedding

A parallel mechanistic branch emerged from *C. elegans* sensory cilia: *"the ciliary G-protein Rab28, associated with human autosomal recessive cone-rod dystrophy, negatively regulates EV levels in the sensory organs"* ([PMID: 32101165](https://pubmed.ncbi.nlm.nih.gov/32101165/)). Working with the BBSome, Rab28 restrains the production/shedding of ciliary extracellular vesicles. Because photoreceptor outer-segment disc morphogenesis and shedding share machinery with ciliary EV biogenesis, dysregulated EV shedding offers a complementary explanation for how RAB28 loss perturbs outer-segment homeostasis. This is an inferred bridge between the invertebrate EV finding and the vertebrate OSP defect rather than a directly demonstrated pathway in human retina.

**Ontology annotations:** extracellular vesicle biogenesis (GO:0140112), ciliary membrane (GO:0060170), negative regulation of extracellular exosome assembly.

### Finding 5 — An ultra-rare, non-syndromic, childhood-onset, progressive condition with no approved therapy

RAB28-CRD is genetically homogeneous: *"RAB28-associated CRD is genetically homogeneous and results from pathogenic variants in the RAB28 gene, which is essential for photoreceptor function"* ([PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)). The characteristic electrophysiology is cone-predominant: *"Full-field ERG revealed severely diminished cone responses, while rod responses were mildly reduced"* ([PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)). Reported patients span European, North-African/Middle-Eastern (Moroccan-Jewish), Italian, and Korean backgrounds, with childhood-to-early-adult onset, progressive central/color-vision loss, macular hyperpigmentation, RPE/macular atrophy, and photoreceptor-layer thinning on OCT ([PMID: 23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/), [PMID: 33396523](https://pubmed.ncbi.nlm.nih.gov/33396523/), [PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)). The condition is non-syndromic with normal life expectancy. No formal prevalence, incidence, penetrance, or natural-history figures are established, owing to the disease's rarity (fewer than ~20 reported families worldwide).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in RAB28** (nonsense/frameshift predominantly; rare missense) **leads to** absent or non-functional RAB28 GTPase protein (predicted null alleles such as p.Glu189\* and p.Arg137\*). *[Demonstrated in human families, PMID 23746546.]*
2. Loss of the **farnesylated ciliary RAB28 GTPase** **results in** disrupted RAB28 function at the photoreceptor basal body, connecting cilium and ciliary rootlet, and loss of its nucleotide-state-dependent association with IFT trains and the BBSome. *[Demonstrated: localization PMID 23746546; IFT/BBSome PMID 27930654.]*
3. Impaired ciliary RAB28/BBSome function **branches** into two coupled consequences:
   - **Branch A:** **leads to** diminished circadian (dawn/dusk) peaks of RPE phagocytosis of photoreceptor — especially **cone** — outer segments (OSP), with basal OSP preserved. *[Demonstrated: PMID 35471581, 30228185.]*
   - **Branch B:** **leads to** dysregulated (increased) ciliary extracellular-vesicle shedding, since Rab28/BBSome normally negatively regulate EV levels. *[Demonstrated in C. elegans; PMID 32101165. Link to vertebrate photoreceptor is inferred.]*
4. Defective OSP **results in** failure to recycle outer-segment retinoids, **leading to** significantly reduced 11-cis-retinal (11-cRAL), 11-cis-retinyl palmitate (11cRP) and all-trans-retinyl palmitate (atRP) — i.e., **visual-cycle disruption**. *[Demonstrated: PMID 35471581.]*
5. Reduced chromophore availability plus accumulating/unrenewed outer-segment material **results in** progressive cone (then rod) photoreceptor dysfunction, **leading to** macular RPE stress and hyperpigmentation, RPE atrophy, and photoreceptor-layer thinning. *[Demonstrated clinically: PMID 23746546, 42231409.]*
6. Photoreceptor and RPE degeneration **results in** the clinical phenotype: progressive loss of visual acuity and color vision, macular atrophy, and a cone-predominant ERG deficit. *[Demonstrated: PMID 23746546, 42231409.]*

### Schematic

```
 RAB28 biallelic LoF (p.Glu189*, p.Arg137*, ...)
             │
             ▼
 Loss of farnesylated ciliary RAB28 GTPase
 (basal body / connecting cilium / rootlet; IFT + BBSome)
             │
     ┌───────┴────────────────────────┐
     ▼                                 ▼
 Branch A                         Branch B
 ↓ dawn/dusk RPE OSP of           dysregulated ciliary
 (cone) outer segments            EV shedding (BBSome)
     │                                 │
     ▼                                 │
 Visual-cycle disruption              │ (inferred link to
 (↓11-cRAL, 11cRP, atRP)             │  OS disc homeostasis)
     │                                 │
     └───────────────┬─────────────────┘
                     ▼
     Progressive cone→rod photoreceptor dysfunction
     + macular hyperpigmentation, RPE atrophy, OCT thinning
                     ▼
     Cone-rod dystrophy: ↓acuity, ↓color vision,
     cone>>rod ERG reduction (CORD18)
```

### Upstream vs downstream

- **Upstream / initiating:** RAB28 LoF variant → loss of ciliary GTPase function (molecular).
- **Midstream:** OSP failure and EV dysregulation (cellular, RPE-photoreceptor interface).
- **Downstream:** visual-cycle depletion → photoreceptor degeneration → clinical cone-rod dystrophy.

**Cell types involved:** retinal cone cell (CL:0000573, primary), retinal rod cell (CL:0000604), retinal pigment epithelial cell (CL:0002586). **Anatomy:** retina (UBERON:0000966), macula lutea (UBERON:0005388), photoreceptor outer segment, retinal pigment epithelium (UBERON:0001782). **Subcellular:** connecting cilium / basal body (GO:0032391, GO:0036064), ciliary rootlet, ciliary membrane.

---

## Section-by-Section Reference Content

### 1. Disease Information
- **Overview:** Non-syndromic autosomal-recessive cone-rod dystrophy with childhood/early-adult onset, progressive central and color vision loss, macular pigmentary changes and RPE atrophy.
- **Identifiers:** OMIM disease 615374 (Cone-Rod Dystrophy 18, CORD18); OMIM gene RAB28 *612994; MONDO:0100448; HGNC:9764 (RAB28). ICD-11: 9B70.0 (cone and cone-rod dystrophies) / ICD-10 H35.5 (hereditary retinal dystrophy). Orphanet: within the inherited cone-rod dystrophy group. MeSH: Cone-Rod Dystrophies / Retinal Dystrophies.
- **Synonyms:** RAB28 retinopathy; RAB28-related cone-rod dystrophy; CORD18; arCRD due to RAB28.
- **Data source:** Aggregated from individual-patient case reports/series and model-organism functional studies — not EHR-derived population data.

### 2. Etiology
- **Causal factor:** Purely genetic — biallelic (homozygous or compound-heterozygous) loss-of-function variants in RAB28. No environmental or infectious etiology.
- **Genetic risk factors:** The RAB28 pathogenic variants themselves are causal (not susceptibility loci). Consanguinity increases homozygous-variant risk (families reported from consanguineous/isolated populations).
- **Protective factors:** None identified. No modifier alleles or protective variants reported.
- **Gene-environment interactions:** None documented. The circadian light cycle is biologically relevant (OSP peaks are light/dark-entrained) but not established as a modifiable disease modifier.

### 3. Phenotypes
| Phenotype | Type | HPO | Onset | Severity | Progression | Frequency |
|---|---|---|---|---|---|---|
| Cone-rod dystrophy | Clinical sign (ERG) | HP:0000548 | Childhood–early adult | Severe (cone) | Progressive | ~All |
| Reduced visual acuity | Symptom | decreased acuity | Childhood on | Moderate–severe | Progressive | ~All |
| Macular hyperpigmentation | Physical sign | HP:0008061 | Variable | Variable | Progressive | High |
| RPE atrophy / macular atrophy | Clinical sign | HP:0007894 | Childhood on | Variable | Progressive | High |
| Photoreceptor-layer thinning (OCT) | Imaging sign | abnormal OCT | Childhood on | Variable | Progressive | High |
| Dyschromatopsia (color-vision loss) | Symptom | HP:0000551 | Early | Variable | Progressive | Common |
| Photophobia | Symptom | HP:0000613 | Variable | Mild–moderate | Stable/progressive | Variable |

- **Quality-of-life impact:** Progressive central and color-vision loss impairs reading, driving, and fine visual tasks; low-vision aids and rehabilitation partially mitigate. No disease-specific QOL instrument data (EQ-5D/SF-36) published.

### 4. Genetic / Molecular Information
- **Causal gene:** RAB28 (HGNC:9764; OMIM *612994), chromosome 4p15.33; encodes a farnesylated Rab-family small GTPase.
- **Pathogenic variants:** Predominantly **nonsense/null** — c.565C>T (p.Glu189\*), c.409C>T (p.Arg137\*) ([PMID: 23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/)); additional alleles expanded the spectrum ([PMID: 33396523](https://pubmed.ncbi.nlm.nih.gov/33396523/)). A rare **missense** p.Ser23Phe was reported in a sporadic case alongside a de novo 4p16.1p15.33 deletion ([PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)).
- **Classification:** Null variants are pathogenic (ACMG PVS1 + segregation). Missense/VUS require functional support.
- **Allele frequency:** Pathogenic alleles are ultra-rare/absent-to-very-rare in gnomAD.
- **Origin:** Germline. **Functional consequence:** loss of function (null alleles; hypomorphic for some).
- **Chromosomal abnormalities:** A de novo **4p16.1p15.33 deletion** unmasking a RAB28 variant was reported ([PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)) — relevant because RAB28 lies on 4p.
- **Diagnostic caveat:** RAB28 and **PROM1** sit in the same homozygous 4p interval; a deep-intronic PROM1 pseudoexon mutation caused CRD in a family initially suspected of RAB28 involvement ([PMID: 26153215](https://pubmed.ncbi.nlm.nih.gov/26153215/)). Both must be sequenced (including deep intronic regions) when this interval maps.
- **Modifier genes / epigenetics:** None identified.

### 5. Environmental Information
Not applicable. No environmental, lifestyle, or infectious contributors; disease is monogenic recessive.

### 6. Mechanism / Pathophysiology
See **Mechanistic Model** above. Pathways/processes: ciliary trafficking (IFT/BBSome), RPE phagocytosis (GO:0006909), retinoid/visual cycle (GO:0001523), extracellular-vesicle biogenesis (GO:0140112). No canonical Wnt/MAPK/mTOR involvement reported. Protein dysfunction = loss of GTPase function at the cilium. No immune or metabolic-systemic involvement.

### 7. Anatomical Structures Affected
- **Organ:** Eye/retina (UBERON:0000966); macula (UBERON:0005388) predominantly affected; RPE (UBERON:0001782).
- **Tissue/cell:** Neural retina photoreceptors — cones (CL:0000573) > rods (CL:0000604); RPE cells (CL:0002586).
- **Subcellular:** Connecting cilium/basal body (GO:0032391/GO:0036064), ciliary rootlet, outer-segment membranes.
- **Localization:** Bilateral, macula-predominant (central), symmetric.

### 8. Temporal Development
- **Onset:** Childhood to early adulthood; insidious, chronic.
- **Progression:** Slowly progressive; cone dysfunction precedes/exceeds rod. Lifelong, no remission.
- **Critical period:** Therapeutic window exists while photoreceptors survive (pre-end-stage atrophy) — relevant to gene-replacement timing.

### 9. Inheritance and Population
- **Inheritance:** Autosomal recessive; biallelic. Penetrance appears complete in reported homozygotes; expressivity variable.
- **Epidemiology:** Ultra-rare; no formal prevalence/incidence. <~20 families reported.
- **Populations:** European, North-African/Middle-Eastern (Moroccan-Jewish), Italian, Korean. **Consanguinity** contributes. No established founder variant. Sex ratio ~1:1 (autosomal recessive).

### 10. Diagnostics
- **Clinical/functional:** Full-field ERG (cone >> rod reduction), color-vision testing, visual-field testing. OCT (photoreceptor/ONL thinning, RPE changes), fundus autofluorescence, fundus photography (macular hyperpigmentation/atrophy).
- **Genetic testing (definitive):** IRD gene panels including RAB28, whole-exome (WES) or whole-genome sequencing (WGS). WGS adds value because deep-intronic variants (e.g., the PROM1 pseudoexon in the same interval, [PMID: 26153215](https://pubmed.ncbi.nlm.nih.gov/26153215/)) and CNVs (4p deletion, [PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)) are missed by exon-focused assays. Chromosomal microarray detects 4p deletions. Homozygosity mapping aids consanguineous families.
- **Differential diagnosis:** Other autosomal-recessive cone-rod dystrophies (ABCA4, PROM1, CDHR1, ADAM9, C8orf37, etc.), Stargardt disease, achromatopsia. Distinguished by gene testing; the shared 4p RAB28/PROM1 interval is the key pitfall.

### 11. Outcome / Prognosis
- **Survival/mortality:** Normal life expectancy; non-lethal, non-systemic.
- **Morbidity:** Progressive low vision / visual disability; central and color vision most affected.
- **Disease course:** Chronic, progressive, no spontaneous remission. Legal blindness possible in advanced disease.
- **Prognostic factors:** Residual photoreceptor survival and macular integrity; earlier/larger atrophy portends worse function. No validated molecular prognostic biomarkers.

### 12. Treatment
- **Current standard:** No approved disease-modifying therapy. Supportive **low-vision rehabilitation**, optical aids, UV/glare protection, and **genetic counseling**.
- **Experimental — gene therapy:** AAV-mediated RAB28 gene supplementation is the leading strategy. Cone-specific wild-type Rab28 re-expression rescued the OSP defect in zebrafish rab28 mutants ([PMID: 37321111](https://pubmed.ncbi.nlm.nih.gov/37321111/)). Small gene size and cone-targeting feasibility are favorable for AAV.
- **Gene-agnostic option:** Optogenetic therapy is a universal approach for late-stage degeneration regardless of causal gene ([PMID: 33262683](https://pubmed.ncbi.nlm.nih.gov/33262683/)), potentially applicable once photoreceptors are lost.
- **NCIT suggestions:** Gene Therapy (NCIT:C15431), AAV Vector-based therapy, Supportive Care (NCIT:C15277), Low Vision Rehabilitation. No pharmacotherapy or pharmacogenomics established.

### 13. Prevention
- **Primary:** Not preventable (monogenic). **Genetic counseling**, carrier testing in at-risk families, and reproductive options (preimplantation/prenatal genetic diagnosis) for known familial variants.
- **Secondary:** Cascade testing of relatives; early ophthalmologic surveillance in at-risk children.
- **Tertiary:** Low-vision rehabilitation to limit disability. No immunization or public-health measures apply.

### 14. Other Species / Natural Disease
- **Orthologs:** Mouse *Rab28* (NCBI Gene 211548), zebrafish *rab28*, *C. elegans* *rab-28*. Highly conserved ciliary GTPase.
- **Natural disease:** No naturally occurring RAB28 retinopathy documented in companion animals/wildlife (OMIA search negative). All animal data are engineered models.
- **Comparative biology:** Mechanism (ciliary GTPase, OSP) conserved; zebrafish shows OSP defect **without** overt degeneration ([PMID: 32258030](https://pubmed.ncbi.nlm.nih.gov/32258030/)), a notable cross-species difference. No zoonotic/transmission relevance.

### 15. Model Organisms
| Model | Type | Key phenotype | Recapitulation | Reference |
|---|---|---|---|---|
| Mouse Rab28 KO | Mammalian, knockout | Loss of cone outer-segment phagocytosis by RPE; blunted dawn/dusk OSP; ↓retinoids | Recapitulates OSP/visual-cycle defect | [PMID: 30228185](https://pubmed.ncbi.nlm.nih.gov/30228185/), [PMID: 35471581](https://pubmed.ncbi.nlm.nih.gov/35471581/) |
| Zebrafish rab28 KO | Teleost, genetic deletion | Defective OS shedding; **no** overt retinal degeneration | Partial — molecular defect without degeneration | [PMID: 32258030](https://pubmed.ncbi.nlm.nih.gov/32258030/) |
| Zebrafish rab28 + cone transgene | Rescue model | Cone-specific WT Rab28 rescues OSP | Proof-of-concept for gene therapy | [PMID: 37321111](https://pubmed.ncbi.nlm.nih.gov/37321111/) |
| C. elegans rab-28 | Invertebrate | Dysregulated ciliary EV shedding; IFT/BBSome association | Models ciliary/EV mechanism | [PMID: 27930654](https://pubmed.ncbi.nlm.nih.gov/27930654/), [PMID: 32101165](https://pubmed.ncbi.nlm.nih.gov/32101165/) |

- **Limitations:** Zebrafish lacks overt degeneration (tempo/species difference); no model fully reproduces human progressive macular atrophy. **Resources:** MGI, ZFIN, WormBase.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/) | *Mutations in RAB28 … cause arCRD* | Human clinical + IHC | F1 (causal variants, phenotype), F2 (farnesylation, localization) |
| [33396523](https://pubmed.ncbi.nlm.nih.gov/33396523/) | *Expanding the clinical/genetic spectrum* | Human clinical | F5 (variant/phenotype spectrum) |
| [42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/) | *Sporadic CRD: RAB28 p.Ser23Phe + 4p deletion* | Human clinical | F5 (homogeneity, cone>rod ERG), missense + CNV |
| [30228185](https://pubmed.ncbi.nlm.nih.gov/30228185/) | *RAB28 required for cone OS phagocytosis (mouse)* | Mouse model | F3 (RPE phagocytosis) |
| [35471581](https://pubmed.ncbi.nlm.nih.gov/35471581/) | *Dawn/dusk OSP & visual cycle require Rab28* | Mouse + zebrafish | F3 (OSP, retinoids) |
| [32258030](https://pubmed.ncbi.nlm.nih.gov/32258030/) | *Zebrafish Rab28 KO: OS shedding defect, no degeneration* | Zebrafish model | F3 (model limitation) |
| [27930654](https://pubmed.ncbi.nlm.nih.gov/27930654/) | *RAB-28 ciliary GTPase, BBSome/IFT* | C. elegans | F2 (IFT/BBSome) |
| [32101165](https://pubmed.ncbi.nlm.nih.gov/32101165/) | *Ciliary Rab28 & BBSome regulate EV shedding* | C. elegans | F4 (EV shedding) |
| [37321111](https://pubmed.ncbi.nlm.nih.gov/37321111/) | *Gene therapy for RAB28: zebrafish* | Zebrafish rescue | Treatment (gene therapy) |
| [26153215](https://pubmed.ncbi.nlm.nih.gov/26153215/) | *Deep-intronic PROM1 pseudoexon mimics RAB28 CRD* | Human clinical | Diagnostic caveat (RAB28/PROM1 interval) |
| [33262683](https://pubmed.ncbi.nlm.nih.gov/33262683/) | *Optogenetic gene therapy for degenerate retina* | Review | Gene-agnostic therapy option |
| [40869487](https://pubmed.ncbi.nlm.nih.gov/40869487/) | *Genetic therapies for retinitis pigmentosa* | Review | IRD gene-therapy landscape |

**How papers challenge findings:** [PMID: 32258030](https://pubmed.ncbi.nlm.nih.gov/32258030/) is the main internal tension — zebrafish Rab28 loss produces the molecular OS-shedding defect but **not** degeneration, indicating the OSP lesion is necessary but perhaps not sufficient for rapid photoreceptor death, or that species differ in resilience/tempo. [PMID: 26153215](https://pubmed.ncbi.nlm.nih.gov/26153215/) does not challenge RAB28 causation but warns that the co-localized PROM1 gene can masquerade as RAB28 disease.

---

## Limitations and Knowledge Gaps

- **Epidemiology unquantified:** No formal prevalence, incidence, penetrance, or natural-history figures — disease too rare; estimates rely on <~20 reported families.
- **Human mechanism inferred from models:** OSP/visual-cycle and EV-shedding mechanisms are demonstrated in mouse, zebrafish, and *C. elegans*; direct human retinal mechanistic data are absent.
- **Model-human discordance:** Zebrafish lacks degeneration, so disease tempo and the sufficiency of the OSP defect for human photoreceptor loss remain uncertain.
- **EV branch under-validated:** The EV-shedding pathway (Finding 4) is established only in *C. elegans*; its contribution to vertebrate photoreceptor pathology is an inference.
- **Genotype-phenotype correlations:** With so few patients and a mix of null and rare missense alleles, severity/progression correlations are not established.
- **No therapy in humans:** Gene-replacement efficacy is shown only in zebrafish; no human trials, dosing, or safety data.
- **No validated biomarkers** for progression or treatment response.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a RAB28-CRD patient registry** to capture natural history, age-of-onset distribution, progression rate, and genotype-phenotype correlations across the reported populations.
2. **Generate a mammalian degeneration model** (e.g., aged/stressed Rab28-KO mouse, or cone-rich model) to test whether the OSP/visual-cycle defect is sufficient for progressive macular-type degeneration, resolving the zebrafish discordance.
3. **Patient iPSC-derived retinal organoids / RPE** to directly test the OSP, visual-cycle, and EV-shedding mechanisms in human cells and validate cross-species inferences.
4. **Preclinical AAV-RAB28 gene-supplementation study** in the mouse model with functional (ERG) and structural (OCT/histology) endpoints, defining the therapeutic window relative to photoreceptor survival.
5. **Dissect the EV-shedding branch in vertebrates** — test whether RAB28/BBSome-dependent EV dysregulation occurs in mammalian photoreceptor cilia and contributes to outer-segment disc defects.
6. **Deep-sequencing diagnostic protocol** for the 4p RAB28/PROM1 interval (WGS + CNV analysis) to avoid misattribution and capture deep-intronic and structural variants.
7. **Biomarker discovery** — longitudinal OCT/autofluorescence and retinoid-related measures as progression/treatment-response surrogates.

---

## References

1. Roosing S, et al. *Mutations in RAB28, encoding a farnesylated small GTPase, are associated with autosomal-recessive cone-rod dystrophy.* [PMID: 23746546](https://pubmed.ncbi.nlm.nih.gov/23746546/)
2. *Expanding the Clinical and Genetic Spectrum of RAB28-related retinopathy.* [PMID: 33396523](https://pubmed.ncbi.nlm.nih.gov/33396523/)
3. *Sporadic cone-rod dystrophy caused by a heterozygous RAB28 p.Ser23Phe pathogenic variant and a de novo 4p16.1p15.33 deletion.* [PMID: 42231409](https://pubmed.ncbi.nlm.nih.gov/42231409/)
4. *The small GTPase RAB28 is required for phagocytosis of cone outer segments by the murine retinal pigmented epithelium.* [PMID: 30228185](https://pubmed.ncbi.nlm.nih.gov/30228185/)
5. *Dawn and dusk peaks of outer segment phagocytosis, and visual cycle function require Rab28.* [PMID: 35471581](https://pubmed.ncbi.nlm.nih.gov/35471581/)
6. *Genetic Deletion of Zebrafish Rab28 Causes Defective Outer Segment Shedding, but Not Retinal Degeneration.* [PMID: 32258030](https://pubmed.ncbi.nlm.nih.gov/32258030/)
7. *Whole-Organism Developmental Expression Profiling Identifies RAB-28 as a Novel Ciliary GTPase Associated with the BBSome and Intraflagellar Transport.* [PMID: 27930654](https://pubmed.ncbi.nlm.nih.gov/27930654/)
8. *Ciliary Rab28 and the BBSome negatively regulate extracellular vesicle shedding.* [PMID: 32101165](https://pubmed.ncbi.nlm.nih.gov/32101165/)
9. *Gene therapy for RAB28: What can we learn from zebrafish?* [PMID: 37321111](https://pubmed.ncbi.nlm.nih.gov/37321111/)
10. *Homozygosity mapping and whole-genome sequencing reveals a deep intronic PROM1 mutation causing cone-rod dystrophy by pseudoexon activation.* [PMID: 26153215](https://pubmed.ncbi.nlm.nih.gov/26153215/)
11. *Optogenetic Gene Therapy for the Degenerate Retina: Recent Advances.* [PMID: 33262683](https://pubmed.ncbi.nlm.nih.gov/33262683/)
12. *Genetic Therapies for Retinitis Pigmentosa: Current Breakthroughs and Future Directions.* [PMID: 40869487](https://pubmed.ncbi.nlm.nih.gov/40869487/)

---

*Evidence source legend: Human clinical (PMIDs 23746546, 33396523, 42231409, 26153215); Mouse model (30228185, 35471581); Zebrafish model (32258030, 35471581, 37321111); C. elegans (27930654, 32101165); Review (33262683, 40869487).*


## Artifacts

- [OpenScientist final report](RAB28-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RAB28-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 9 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100448` (5 mentions) - the report calls it "MONDO"; MONDO calls it **RAB28-related retinopathy**
- `HP:0000548` (2 mentions) - the report calls it "Clinical sign (ERG)"; HP calls it **Cone/cone-rod dystrophy**
- `HP:0008061` (2 mentions) - the report calls it "Physical sign"; HP calls it **Aplasia/Hypoplasia of the retina**
- `HP:0007894` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Fundus hypopigmentation**
- `HP:0000551` (2 mentions) - the report calls it "Symptom"; HP calls it **Color vision defect**
- `HP:0000613` (2 mentions) - the report calls it "Symptom"; HP calls it **Photophobia**
- `CL:0000573` (3 mentions) - the report calls it "Tissue/cell:** Neural retina photoreceptors — cones"; CL calls it **retinal cone cell**
- `NCIT:C15431` (1 mention) - the report calls it "NCIT suggestions:** Gene Therapy"; NCIT calls it **Hematopoietic Cell Transplantation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000966` (2 mentions) - the report calls it "Organ:** Eye/retina"; UBERON calls it **retina**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:9764` - called "chromosome 4p15.33", "RAB28"