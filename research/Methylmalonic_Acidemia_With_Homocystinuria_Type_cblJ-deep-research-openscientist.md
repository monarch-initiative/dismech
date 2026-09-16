---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T08:42:28.288274'
end_time: '2026-09-06T09:20:04.402580'
duration_seconds: 2256.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Methylmalonic Acidemia With Homocystinuria, Type cblJ
  mondo_id: MONDO:0013925
  category: Mendelian
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
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 2
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0013925
    reported_labels:
    - MONDO
    ontology_label: methylmalonic acidemia with homocystinuria, type cblJ
  - term_id: GO:0005764
    reported_labels:
    - Subcellular compartments:** lysosome
    ontology_label: lysosome
  - term_id: HP:0011968
    reported_labels:
    - Clinical sign
    ontology_label: Feeding difficulties
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    ontology_label: Global developmental delay
  - term_id: HP:0025406
    reported_labels:
    - Symptom
    ontology_label: Asthenia
  - term_id: HP:0012120
    reported_labels:
    - Lab abnormality
    ontology_label: Methylmalonic aciduria
  - term_id: HP:0002160
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperhomocystinemia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methylmalonic Acidemia With Homocystinuria, Type cblJ
- **MONDO ID:** MONDO:0013925 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Methylmalonic Acidemia With Homocystinuria, Type cblJ** covering all of the
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

# Methylmalonic Acidemia With Homocystinuria, Type cblJ (MAHCJ)

**Disease:** Methylmalonic Acidemia With Homocystinuria, Type cblJ
**MONDO ID:** MONDO:0013925 · **OMIM:** #614857 · **Gene:** *ABCD4* (14q24.3)
**Category:** Mendelian (autosomal recessive inborn error of intracellular cobalamin metabolism)

---

## Summary

Methylmalonic acidemia with homocystinuria type cblJ (**MAHCJ**, "cobalamin J disease") is an **ultra-rare autosomal recessive inborn error of intracellular vitamin B12 (cobalamin) metabolism**. It is caused by **biallelic loss-of-function or missense variants in *ABCD4***, a gene on chromosome 14q24.3 encoding an ATP-binding cassette (ABC) transporter. Unlike its ABCD-family relatives, which are peroxisomal, ABCD4 acts at the **lysosome**, where — together with its chaperone LMBD1 (the protein deficient in cblF disease) — it **exports cobalamin from the lysosomal lumen into the cytosol**. When ABCD4 fails, free cobalamin is trapped in the lysosome and cannot reach the two downstream enzymes that require it. The result is a **combined biochemical phenotype**: methylmalonic acidemia plus homocystinuria, characteristically with **normal serum vitamin B12**.

Cobalamin is a cofactor for only two human reactions, and cblJ disrupts **both** because the defect sits at the shared upstream export step. Cytosolic **methylcobalamin** is required by **methionine synthase (MTR)** to remethylate homocysteine to methionine; mitochondrial **adenosylcobalamin** is required by **methylmalonyl-CoA mutase (MMUT)** to convert methylmalonyl-CoA to succinyl-CoA. Loss of both cofactors causes accumulation of homocysteine and methylmalonic acid, low/normal methionine, and downstream neurologic, hematologic, gastrointestinal, and metabolic disease. The disorder was first defined in 2012, and as of 2025 only about **eight patients** have been documented worldwide, giving a clinical spectrum that runs from **severe neonatal multisystem disease** to a **presymptomatically screen-detected infant who remained neurotypical**.

Management is **lifelong metabolic therapy**: parenteral (IM/SC) **hydroxocobalamin** is the mainstay, supplemented by **betaine**, **L-carnitine**, **folate/folinic acid**, and a **protein-modified diet**, with the therapeutic goal of normalizing plasma total homocysteine, methionine, and methylmalonic acid. There is no cure and no approved gene, cell, or RNA therapy. Prognosis hinges chiefly on **how early treatment begins** — newborn-screening detection with presymptomatic treatment is associated with markedly better neurodevelopmental outcomes. This report synthesizes 11 confirmed findings across 26 reviewed papers into a complete disease-characteristics entry.

---

## Key Findings

### F001 — cblJ is an ultra-rare autosomal recessive lysosomal cobalamin-export disorder caused by biallelic *ABCD4* variants

Cobalamin J disease (MAHCJ, OMIM #614857) is an autosomal recessive disorder of intracellular cobalamin metabolism caused by **biallelic pathogenic variants in *ABCD4*** (14q24.3), which encodes an ATP-binding cassette transporter. It was first described by Coelho and colleagues in 2012 (*Nature Genetics*). It is **ultra-rare** — only about eight documented patients as of 2025 — and both clinically and biochemically it **mimics the cblF defect** (caused by *LMBRD1* mutations): both produce a failure to release cobalamin from lysosomes, generating combined methylmalonic acidemia plus homocystinuria.

> *"We describe a new disease that results in failure to release vitamin B12 from lysosomes, which mimics the cblF defect caused by LMBRD1 mutations"* — [PMID: 22922874](https://pubmed.ncbi.nlm.nih.gov/22922874/)

> *"It is caused by pathogenic variants in ABCD4, which encodes an ATP-binding cassette (ABC) transporter that affects the lysosomal release of cobalamin (Cbl) into the cytoplasm."* — [PMID: 33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/)

> *"Cobalamin J disease (CblJ) is an ultrarare autosomal recessive disorder of intracellular cobalamin metabolism associated with combined methylmalonic academia and homocystinuria (MAHCJ; 614857)."* — [PMID: 41378236](https://pubmed.ncbi.nlm.nih.gov/41378236/)

### F002 — ABCD4 is a lysosomal ABC transporter exported by the LMBD1 chaperone and requiring its ATPase domain and transmembrane helix 6

ABCD4 colocalizes with the lysosomal proteins **LAMP1** and **LMBD1**, the latter being deficient in cblF disease. ABCD4 relies on **LMBD1 as a dedicated chaperone** for correct trafficking to the lysosome. Structural (cryo-EM) work shows LMBD1 has nine transmembrane helices plus a cytosolic domain that engages ABCD4; disrupting this interaction impairs ABCD4 trafficking. Function additionally depends on the **ATPase domain**, and **transmembrane helix 6 (residues D329, T332)** is indispensable for cobalamin substrate recognition and transport without reducing ATPase activity.

> *"ABCD4 colocalizes with the lysosomal proteins LAMP1 and LMBD1, the latter of which is deficient in the cblF defect"* — [PMID: 22922874](https://pubmed.ncbi.nlm.nih.gov/22922874/)

> *"the cobalamin exporter ABCD4 is distinct, instead relying on LMBD1 as a dedicated chaperone for its trafficking"* — [PMID: 42303638](https://pubmed.ncbi.nlm.nih.gov/42303638/)

> *"TM helix 6 contributes to substrate recognition"* — [PMID: 38069516](https://pubmed.ncbi.nlm.nih.gov/38069516/)

### F003 — Clinical spectrum ranges from severe neonatal multisystem disease to asymptomatic screen-detected cases

Across the ~8 known cases, reported features include **feeding difficulties, failure to thrive, hypotonia, seizures, developmental delay, and hematological abnormalities** (macrocytic/megaloblastic anemia). The phenotype is highly **variable**: one patient detected by newborn screening and treated presymptomatically remained **asymptomatic with normal growth and neurodevelopment** (the first neurotypical case, Pillai 2021); another (Aslan 2025, the 8th documented case, novel homozygous *ABCD4* c.1591C>T p.Arg531Trp) presented with **recurrent abdominal pain attacks** and is the oldest, longest-followed patient. A 2013 case presented atypically as **diabetic ketoacidosis** (hyperglycemia, high anion gap metabolic acidosis).

> *"Described clinical features include feeding difficulties, failure to thrive, hypotonia, seizures, developmental delay, and hematological abnormalities."* — [PMID: 33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/)

> *"With early detection and initiation of treatment, this patient has remained asymptomatic with normal growth parameters and neurodevelopmental function."* — [PMID: 33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/)

> *"A novel homozygous missense variant c.1591C>T (p.Arg531Trp) in exon 17 of"* — [PMID: 41378236](https://pubmed.ncbi.nlm.nih.gov/41378236/)

### F004 — Treatment centers on parenteral hydroxocobalamin, with betaine and carnitine, per remethylation-disorder guidelines

The **2026 First Revision of the Guidelines for Diagnosis and Management of Remethylation Disorders** recommends **parenteral hydroxocobalamin** for cobalamin-related defects together with **betaine**, aiming to keep total homocysteine, methionine (and methylmalonic acid) as close to normal as achievable. Early detection through newborn screening is associated with improved outcomes. In cblJ specifically, the newborn-screening-detected patient treated early (Pillai 2021) remained asymptomatic. Standard adjuncts across combined MMA+HC disorders include **folate/folinic acid, L-carnitine, and a low-protein/protein-modified diet**.

> *"Betaine as first-line therapy for methylenetetrahydrofolate reductase deficiency and parenteral hydroxocobalamin for cobalamin-related defects have reduced mortality and morbidity."* — [PMID: 42231716](https://pubmed.ncbi.nlm.nih.gov/42231716/)

> *"Early detection through newborn screening is associated with improved clinical outcomes."* — [PMID: 42231716](https://pubmed.ncbi.nlm.nih.gov/42231716/)

### F005 — Causal chain: ABCD4 loss traps cobalamin in lysosomes, depleting BOTH mitochondrial adenosylcobalamin and cytosolic methylcobalamin

Cobalamin derivatives serve **only two reactions in humans**: (1) **methylcobalamin** as cofactor for cytosolic **methionine synthase** (remethylation of homocysteine to methionine), and (2) **adenosylcobalamin** as cofactor for mitochondrial **methylmalonyl-CoA mutase** (conversion of methylmalonyl-CoA to succinyl-CoA). Because cblJ (and cblF) defects sit at the **shared lysosomal-export step**, they impair synthesis of **both** cofactors, producing combined methylmalonic acidemia + homocystinuria with **normal serum B12**.

> *"Cobalamin derivatives are needed for only two reactions in man; remethylation of homocysteine to methionine, with methylcobalamin as a cofactor for methionine synthase, and the conversion of methylmalonyl-coenzyme A to succinyl coenzyme A by methylmalonyl-CoA mutase, with adenosylcobalamin as a cofactor."* — [PMID: 22422209](https://pubmed.ncbi.nlm.nih.gov/22422209/)

> *"a new disease that results in failure to release vitamin B12 from lysosomes"* — [PMID: 22922874](https://pubmed.ncbi.nlm.nih.gov/22922874/)

### F006 — Diagnosis relies on a biochemical triad, confirmed by *ABCD4* sequencing and cellular complementation

Biochemical hallmarks (shared across combined MMA+HC / remethylation disorders): **elevated plasma total homocysteine, elevated methylmalonic acid (blood/urine), low or low-normal methionine, and normal circulating vitamin B12 and folate**. Guidelines recommend assessing plasma total homocysteine, methionine, methylmalonic acid, and serum vitamin B12 in suspected cases. Newborn screening detects the disorder via **elevated C3 (propionylcarnitine)**. Definitive diagnosis of cblJ specifically requires distinguishing it from cblC/cblD/cblF and cblX-like disorders — achieved by **molecular genetic testing (*ABCD4* sequencing)** and confirmed by biochemical and **cellular complementation** studies.

> *"Plasma total homocysteine, methionine, methylmalonic acid, serum vitamin B12 (and folates) should be assessed in suspected cases."* — [PMID: 42231716](https://pubmed.ncbi.nlm.nih.gov/42231716/)

> *"detected by newborn screening and confirmed by biochemical, molecular, and complementation studies"* — [PMID: 33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/)

> *"caused by biallelic variants in one of the following genes: MMACHC (cblC), MMADHC (cblD), LMBRD1 (cblF), ABCD4 (cblJ), THAP11 (cblX-like), and ZNF143 (cblX-like), or a hemizygous variant in HCFC1 (cblX)"* — [PMID: 34655177](https://pubmed.ncbi.nlm.nih.gov/34655177/)

### F007 — *ABCD4* gene identity, protein family, and genetic-counseling context

*ABCD4* (ATP-binding cassette subfamily D member 4; **HGNC:68; NCBI Gene 5826; OMIM \*603214**) maps to **14q24.3** and encodes a **half-transporter of the peroxisomal ABC (ABCD) subfamily** that also includes ABCD1 (X-linked adrenoleukodystrophy), ABCD2, and ABCD3. Although historically annotated as peroxisomal, in cobalamin metabolism ABCD4 localizes to the **lysosome**. Inheritance is autosomal recessive; both parents are obligate carriers, giving a **25% recurrence risk per pregnancy**. Prenatal diagnosis for combined MMA+HC disorders is feasible via targeted variant testing / clinical exome sequencing once familial variants are known, and is considered crucial for high-risk couples. Reported pathogenic variants include loss-of-function (ATPase-domain-disrupting) and missense alleles (e.g., c.1591C>T p.Arg531Trp, homozygous); consanguinity/homozygosity is documented in some families.

> *"we identified causal mutations in ABCD4, a gene that codes for an ABC transporter, which was previously thought to have peroxisomal localization and function"* — [PMID: 22922874](https://pubmed.ncbi.nlm.nih.gov/22922874/)

> *"Prenatal diagnosis of combined methylmalonic acidemia with homocystinuria is crucial for high-risk couples since the disorder can be life-threatening for offspring."* — [PMID: 34655177](https://pubmed.ncbi.nlm.nih.gov/34655177/)

### F008 — No dedicated ABCD4/cblJ animal model; modeling relies on patient fibroblasts, complementation, and related-gene models

As of 2026, **no published knockout/knock-in animal model specific to *ABCD4* (cblJ) exists**. Functional studies use **patient-derived fibroblasts**, **cellular complementation** (microcell-mediated chromosome transfer), and **in vitro reconstitution / proteoliposome transport assays** (e.g., TM6 chimera studies). Related genes in the combined-MMA+HC group have validated models: a viable **zebrafish *mmachc* (cblC) mutant** recapitulates methylmalonic acidemia, growth retardation, lethality, and retinopathy, and improves with hydroxocobalamin/methylcobalamin/methionine/betaine; **mouse models of *Hcfc1*/*Thap11* (cblX-like)** reproduce loss of Mmachc, metabolic perturbations, and developmental defects. Mouse *Mmachc* knockouts show early embryonic lethality. ABCD4 orthologs include mouse *Abcd4* (NCBI Gene 192287), conserved across vertebrates including zebrafish.

> *"we used genome editing to study the loss of mmachc function and to develop the first viable animal model of cblC deficiency"* — [PMID: 32186706](https://pubmed.ncbi.nlm.nih.gov/32186706/)

> *"we have generated mouse models of this disease"* — [PMID: 35013307](https://pubmed.ncbi.nlm.nih.gov/35013307/)

> *"six proteoliposomes were prepared, each containing a different chimeric ABCD4 protein"* — [PMID: 38069516](https://pubmed.ncbi.nlm.nih.gov/38069516/)

### F009 — cblJ primarily affects the nervous and hematopoietic systems, with GI and metabolic involvement; remethylation defects carry leukoencephalopathy and vascular risk

Organ/system involvement in cblJ: **central nervous system** (developmental delay, seizures, hypotonia; brain, UBERON:0000955); **hematopoietic/bone marrow** (megaloblastic/macrocytic anemia, cytopenias; bone marrow UBERON:0002371); **digestive system** (feeding difficulties, failure to thrive, recurrent abdominal pain; UBERON:0001555). The primary lesion is subcellular — the **lysosome (GO:0005764)** and lysosomal membrane (GO:0005765) — with downstream failure in **mitochondria (GO:0005739)** and **cytosol (GO:0005829)**. Because cblJ impairs remethylation, it belongs to the disorder class associated with **leukoencephalopathy/leukodystrophy**, and elevated homocysteine confers **thromboembolic/vascular risk** (inferred for cblJ from the disorder class).

> *"Disorders of cobalamin and folate intracellular metabolism that result in defective remethylation of homocysteine to methionine are associated with leukodystrophy"* — [PMID: 22422209](https://pubmed.ncbi.nlm.nih.gov/22422209/)

> *"Described clinical features include feeding difficulties, failure to thrive, hypotonia, seizures, developmental delay, and hematological abnormalities."* — [PMID: 33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/)

### F010 — Epidemiology: ~8 reported cases worldwide, congenital/pediatric onset, no sex predilection; prognosis hinges on early treatment

cblJ is an **ultrarare** disorder; the 2025 report by Aslan et al. represents only the **eighth documented patient worldwide**, so no reliable prevalence/incidence estimate exists (well below the <1/1,000,000 threshold). Onset is typically **congenital to early infancy**, though a late/attenuated presentation with recurrent abdominal pain into the teens is documented. Inheritance is autosomal recessive; **both sexes are affected**; consanguinity underlies homozygous cases. Prognosis is highly dependent on **timing of therapy**: the only presymptomatically (newborn-screening) diagnosed and early-treated patient remained asymptomatic with normal growth and neurodevelopment, whereas late-diagnosed patients in the broader combined-MMA+HC group frequently have residual developmental delay/intellectual disability. Disease course is chronic/lifelong requiring continuous treatment.

> *"A new patient with MAHCJ, representing the eighth documented instance, is reported here."* — [PMID: 41378236](https://pubmed.ncbi.nlm.nih.gov/41378236/)

> *"parenteral hydroxocobalamin for cobalamin-related defects have reduced mortality and morbidity"* — [PMID: 42231716](https://pubmed.ncbi.nlm.nih.gov/42231716/)

### F011 — Management and prevention: lifelong hydroxocobalamin-based therapy plus newborn screening, cascade/prenatal testing, and genetic counseling

There is **no cure and no approved gene/cell/RNA therapy** for cblJ; management is lifelong metabolic therapy. The core regimen (extrapolated from remethylation-disorder guidelines and combined-MMA+HC cohorts): **parenteral hydroxocobalamin** (mainstay; partially bypasses the export block by mass action / cofactor provision), **betaine** (activates betaine-homocysteine methyltransferase to lower homocysteine), **L-carnitine** (conjugates toxic organic acids), **folinic/folic acid**, and a **protein-modified diet**, targeting normalization of plasma total homocysteine, methionine, and methylmalonic acid. Cyanocobalamin is inferior to hydroxocobalamin. Prevention operates at three levels: **primary/secondary** — newborn screening (elevated C3 → confirmatory homocysteine/MMA/organic acids) enables presymptomatic treatment; **secondary** — carrier/cascade testing and prenatal/preimplantation testing once familial variants are known; **tertiary** — continuous metabolite monitoring and early sick-day management. Genetic counseling communicates the 25% AR recurrence risk.

> *"Betaine as first-line therapy for methylenetetrahydrofolate reductase deficiency and parenteral hydroxocobalamin for cobalamin-related defects have reduced mortality and morbidity."* — [PMID: 42231716](https://pubmed.ncbi.nlm.nih.gov/42231716/)

> *"no cases of presymptomatic diagnosis have been reported"* — [PMID: 33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/)

> *"treatment with low-protein diet, vitamin B12, folic acid, and L-carnitine"* — [PMID: 23546813](https://pubmed.ncbi.nlm.nih.gov/23546813/)

---

## Section-by-Section Disease Characteristics

### 1. Disease Information

**Overview.** Cobalamin J disease (MAHCJ) is an ultra-rare autosomal recessive inborn error of intracellular cobalamin metabolism. Biallelic *ABCD4* variants block the export of cobalamin from lysosomes to the cytosol, depriving cells of the two active cobalamin cofactors and producing **combined methylmalonic acidemia and homocystinuria**, classically with **normal serum B12** (F001, F005).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #614857 (MAHCJ) |
| OMIM (gene) | *603214 (*ABCD4*) |
| MONDO | MONDO:0013925 |
| Gene / HGNC | *ABCD4* / HGNC:68 |
| NCBI Gene | 5826 |
| Cytogenetic locus | 14q24.3 |
| Cobalamin complementation class | cblJ |

**Synonyms / alternative names:** Methylmalonic acidemia with homocystinuria, cblJ type; MAHCJ; Cobalamin J disease; cblJ; combined methylmalonic acidemia and homocystinuria, cblJ type.

**Information source.** Because of ultra-rarity (~8 patients), knowledge derives almost entirely from **aggregated disease-level resources** (OMIM, guidelines) and **individual case reports / small case series**, not large EHR datasets (F001, F010).

### 2. Etiology

- **Causal factor:** Purely **genetic** — biallelic pathogenic variants in *ABCD4* (F001, F007). No environmental or infectious cause.
- **Genetic risk factors:** The disease *is* the genotype (biallelic *ABCD4*). Reported alleles include ATPase-domain-disrupting LoF and missense variants (e.g., homozygous c.1591C>T p.Arg531Trp) (F003, F007). **Consanguinity** is a risk factor for homozygous disease.
- **Environmental risk / trigger factors:** Not causal, but **catabolic stress** (intercurrent illness, fasting, high protein load) can precipitate acute metabolic decompensation (F011).
- **Protective factors:** No genetic protective alleles described. The strongest **modifiable protective factor** is **early (presymptomatic) treatment** following newborn screening (F004, F010).
- **Gene–environment interaction:** Fixed genotype interacts with **dietary protein and catabolic state**; adequate cobalamin/betaine therapy plus protein modification mitigates biochemical toxicity (F011).

### 3. Phenotypes

| Phenotype | Type | HPO term (suggested) | Onset / frequency |
|---|---|---|---|
| Feeding difficulties | Clinical sign | HP:0011968 | Neonatal/infantile; common |
| Failure to thrive | Clinical sign | HP:0001508 | Infantile; common |
| Hypotonia | Clinical sign | HP:0001252 | Infantile; common |
| Seizures | Clinical sign | HP:0001250 | Variable |
| Developmental delay | Clinical sign | HP:0001263 | Variable; frequent if late-treated |
| Megaloblastic/macrocytic anemia | Lab/hematologic | HP:0001889 / HP:0001972 | Common |
| Recurrent abdominal pain | Symptom | HP:0025406 | Late/attenuated presentation |
| Elevated methylmalonic acid | Lab abnormality | HP:0012120 | Constant |
| Hyperhomocysteinemia | Lab abnormality | HP:0002160 | Constant |
| Low/low-normal methionine | Lab abnormality | HP:0500152 (hypomethioninemia) | Constant |

Severity is **variable** (severe neonatal multisystem → asymptomatic screen-detected). Progression is **chronic** with risk of **episodic decompensation** during catabolic stress (F003, F009). Quality-of-life impact is greatest in late-diagnosed patients with neurodevelopmental sequelae; presymptomatically treated patients can have normal function (F003, F010).

### 4. Genetic / Molecular Information

- **Causal gene:** *ABCD4* (14q24.3; HGNC:68; NCBI Gene 5826; OMIM *603214) (F007).
- **Protein:** ABCD4, a half-ABC transporter of the ABCD subfamily (relatives ABCD1/2/3); functions at the lysosome despite historic peroxisomal annotation (F002, F007).
- **Variant classes:** Loss-of-function (ATPase-domain-disrupting) and missense (e.g., c.1591C>T, p.Arg531Trp, homozygous). Functional consequence is **loss of function** (impaired lysosomal cobalamin export) (F002, F003, F007).
- **Functional determinants:** ATPase domain and **transmembrane helix 6 (D329, T332)** required for substrate recognition; trafficking requires the **LMBD1 chaperone** (F002).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established for cblJ specifically. *LMBRD1* (cblF) is a functional partner but a separate disease gene (F002).

### 5. Environmental Information

No causal environmental factor, toxin, radiation exposure, or infectious agent. The relevant **environmental/lifestyle modifiers** are **dietary protein load** and **catabolic states** (illness, fasting) that can trigger metabolic decompensation (F011). Not applicable: infectious agents, occupational exposures.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic *ABCD4* loss-of-function variants** → produce an ABCD4 transporter that either mis-traffics or cannot transport substrate (loss of function). *(demonstrated: F001, F002, F007)*
2. **Loss of ABCD4 lysosomal export function** (compounded when LMBD1 chaperoning or TM6/ATPase function is lost) → **leads to** failure to move free cobalamin out of the lysosomal lumen. *(demonstrated: F002, F005)*
3. **Cobalamin trapped in lysosomes** → **results in** starvation of the cytosolic cobalamin-processing machinery (MMACHC/MMADHC). *(inferred from shared-step logic + cblF mimicry: F005)*
4. **Deficient synthesis of both active cofactors** → **branches** into two arms:
   - **4a. Low methylcobalamin** → **impairs methionine synthase (MTR)** in cytosol → **leads to** ↑homocysteine, ↓methionine (homocystinuria; hypomethioninemia). *(demonstrated: F005)*
   - **4b. Low adenosylcobalamin** → **impairs methylmalonyl-CoA mutase (MMUT)** in mitochondria → **leads to** ↑methylmalonyl-CoA → ↑methylmalonic acid (methylmalonic acidemia). *(demonstrated: F005)*
5. **Metabolite accumulation + methionine/SAM deficiency** → **results in** cellular toxicity affecting rapidly dividing and metabolically demanding tissues → **leads to** megaloblastic anemia (hematopoietic), leukoencephalopathy/neurologic injury (CNS), failure to thrive/feeding difficulty (GI/metabolic). *(phenotype demonstrated F003, F009; leukoencephalopathy inferred from disorder class F009)*
6. **Elevated homocysteine** → **confers** thromboembolic/vascular risk. *(inferred from disorder class: F009)*

**Mechanistic categories:**
- **Molecular pathways:** cobalamin (B12) intracellular processing/trafficking; one-carbon/methionine cycle; propionate/methylmalonate catabolism (KEGG cobalamin metabolism) (F005).
- **Protein dysfunction:** ABCD4 loss of transport function / mistrafficking; downstream loss of MTR and MMUT holoenzyme activity from cofactor starvation (F002, F005).
- **Metabolic changes:** amino acid (homocysteine/methionine) and organic acid (methylmalonate) dysregulation (F005).
- **Subcellular compartments:** lysosome (GO:0005764), mitochondrion (GO:0005739), cytosol (GO:0005829) (F009).
- **Suggested GO/CL terms:** GO:0009235 (cobalamin metabolic process), GO:0032259 (methylation), GO:0006555 (methionine metabolic process); cell types — neuron (CL:0000540), oligodendrocyte (CL:0000128), erythroid progenitor (CL:0000038), hepatocyte (CL:0000182) (F009).

### 7. Anatomical Structures Affected

- **Primary organs / systems:** central nervous system / brain (UBERON:0000955) — nervous system; hematopoietic / bone marrow (UBERON:0002371); digestive system (UBERON:0001555) (F009).
- **Secondary / class-level:** cerebral white matter (leukoencephalopathy) and vasculature (homocysteine-related thromboembolic risk) (F009).
- **Tissue/cell level:** nervous tissue (neurons, oligodendrocytes), hematopoietic/erythroid lineage, hepatocytes (F009).
- **Subcellular:** lysosome (site of lesion), mitochondrion and cytosol (downstream enzyme failure) (GO:0005764/0005739/0005829) (F009).
- **Lateralization:** systemic/bilateral (metabolic disease); not lateralized.

### 8. Temporal Development

- **Onset:** typically **congenital to early infancy**; a **late/attenuated** teenage presentation (recurrent abdominal pain) is documented (F003, F010).
- **Onset pattern:** subacute-to-chronic, with acute decompensation possible under catabolic stress (F011).
- **Progression / course:** **chronic, lifelong**; neurodevelopmental damage, once established in late-treated patients, is largely irreversible; biochemical abnormalities are treatment-responsive (F004, F010).
- **Critical period:** the **neonatal/early-infancy window** is the key opportunity for intervention — presymptomatic treatment can prevent morbidity (F003, F010).

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive; 25% recurrence risk per pregnancy; both parents obligate carriers (F001, F007).
- **Epidemiology:** ultra-rare — ~8 documented patients worldwide; no reliable prevalence/incidence estimate (below <1/1,000,000) (F010).
- **Penetrance / expressivity:** essentially complete penetrance for the biochemical phenotype; **variable expressivity** clinically (severe neonatal → asymptomatic screen-detected) (F003, F010).
- **Sex ratio:** no sex predilection; both sexes affected (F010).
- **Consanguinity / founder effects:** consanguinity underlies homozygous cases (e.g., p.Arg531Trp homozygote); no established founder mutation given case scarcity (F007, F010).
- **Anticipation / mosaicism:** not applicable / not reported.

### 10. Diagnostics

- **Biochemical triad:** ↑plasma total homocysteine, ↑methylmalonic acid (blood/urine), low/low-normal methionine, with **normal serum B12 and folate** (F006).
- **Newborn screening:** elevated **C3 (propionylcarnitine)** acylcarnitine on tandem MS, with confirmatory homocysteine/MMA/organic acid testing (F006, F011).
- **Confirmatory testing:** **molecular genetic testing (*ABCD4* sequencing)** plus **cellular complementation** studies to assign the cblJ class and distinguish from cblC/cblD/cblF/cblX-like (F006).
- **Recommended genetic approach:** targeted *ABCD4* single-gene testing or a combined-MMA+HC gene panel (MMACHC, MMADHC, LMBRD1, ABCD4, HCFC1, THAP11, ZNF143); WES/WGS for undifferentiated cases (F006).
- **Differential diagnosis:** cblC (MMACHC), cblD (MMADHC), cblF (LMBRD1), cblX/cblX-like (HCFC1/THAP11/ZNF143) — biochemically overlapping, distinguished by genetics/complementation (F006).
- **Representative labs (LOINC-type):** plasma total homocysteine, plasma methionine, methylmalonic acid, serum B12, acylcarnitine profile.

### 11. Outcome / Prognosis

- **Prognostic driver:** **timing of treatment.** Presymptomatic (screen-detected) early treatment → normal growth and neurodevelopment; late diagnosis → frequent residual developmental delay/intellectual disability (extrapolated from combined-MMA+HC cohorts) (F003, F010).
- **Mortality/morbidity:** hydroxocobalamin-based therapy reduces mortality and morbidity; untreated/late-treated severe neonatal disease is life-threatening (F004, F010, F011).
- **Complications:** neurologic injury/leukoencephalopathy, cytopenias, vascular/thromboembolic risk from hyperhomocysteinemia, metabolic decompensation (F009).
- **Prognostic biomarkers:** degree of control of plasma total homocysteine, MMA, and methionine on therapy (F004, F011).

### 12. Treatment

| Intervention | Role / mechanism | NCIT (suggested) |
|---|---|---|
| Parenteral hydroxocobalamin (IM/SC) | Mainstay; partial bypass of export block, cofactor provision | C74569 |
| Betaine | Activates betaine-homocysteine methyltransferase → lowers homocysteine | C61763 |
| L-carnitine (levocarnitine) | Conjugates/clears toxic organic acids | C61825 |
| Folinic / folic acid | One-carbon support | C61915 |
| Protein-modified / low-protein diet | Reduces methylmalonate/homocysteine precursor load | — |
| Sick-day management (hydration, anti-catabolic) | Prevents/treats acute decompensation | — |

- **Goal:** normalize plasma total homocysteine, methionine, and methylmalonic acid (F004, F011).
- **Cyanocobalamin is inferior** to hydroxocobalamin (F011).
- **Advanced therapeutics:** no approved gene, cell, RNA, or targeted therapy; none in cblJ-specific trials (F008, F011).
- **Pharmacogenomics:** not applicable.

### 13. Prevention

- **Primary/secondary:** newborn screening (C3 elevation) enabling **presymptomatic treatment** — the key advance associated with near-normal outcomes (F010, F011).
- **Genetic prevention:** carrier/cascade testing of relatives; **prenatal/preimplantation genetic testing** for at-risk couples once familial *ABCD4* variants are known (F007, F011).
- **Tertiary:** continuous metabolite monitoring, early sick-day management to prevent neurologic/hematologic complications (F011).
- **Genetic counseling:** communicate 25% AR recurrence risk (F007, F011). NCIT: Newborn Screening (C93073), Genetic Counseling (C15366).
- **Immunization / public-health / vector control:** not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *ABCD4* is conserved across vertebrates; mouse *Abcd4* (NCBI Gene 192287); zebrafish ortholog present (F008).
- **Natural disease in other species:** no naturally occurring ABCD4/cblJ animal disease documented (OMIA); no zoonotic potential (not applicable) (F008).
- **Comparative biology:** cobalamin-processing pathway conserved; related genes modeled in zebrafish (*mmachc*) and mouse (*Hcfc1*/*Thap11*) (F008).

### 15. Model Organisms

- **No dedicated ABCD4/cblJ animal model exists** (F008).
- **In vitro / cellular models:** patient-derived fibroblasts; cellular complementation (microcell-mediated chromosome transfer); proteoliposome/chimera transport assays for TM6/ATPase function (F002, F008).
- **Related-gene models:** viable zebrafish *mmachc* (cblC) mutant recapitulating MMA, growth retardation, lethality, retinopathy (rescued by hydroxocobalamin/methylcobalamin/methionine/betaine); mouse *Hcfc1*/*Thap11* (cblX-like) models; mouse *Mmachc* knockouts (embryonic lethal) (F008).
- **Databases:** MGI (mouse *Abcd4*), ZFIN (zebrafish), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
  Biallelic ABCD4 LoF/missense variants (14q24.3)
                |  (loss of function; TM6/ATPase/LMBD1-trafficking failure)
                v
  ABCD4 fails to export cobalamin from lysosome  <-- LMBD1 chaperone required
                |
                v
  Free cobalamin TRAPPED in lysosomal lumen  (shared step, mimics cblF)
                |
                v
  Cytosolic cobalamin processing (MMACHC/MMADHC) starved
                |
        +-------+-------------------------+
        v                                 v
  Low METHYLcobalamin               Low ADENOSYLcobalamin
        |                                 |
        v                                 v
  Methionine synthase (MTR)         Methylmalonyl-CoA mutase (MMUT)
  fails (cytosol)                   fails (mitochondrion)
        |                                 |
        v                                 v
  ^ Homocysteine, v Methionine       ^ Methylmalonic acid
  (HOMOCYSTINURIA)                   (METHYLMALONIC ACIDEMIA)
        \_________________  __________________/
                          \/
   Tissue toxicity: CNS (delay, seizures, leukoencephalopathy),
   hematopoietic (megaloblastic anemia), GI (FTT, feeding difficulty),
   vascular (homocysteine-driven thrombotic risk)
                |
                v
   NORMAL serum B12 (defect is intracellular/trafficking, not uptake)
```

The unifying insight is that cblJ is a **single upstream lysosomal-export lesion producing a dual downstream cofactor failure**. This explains its two most characteristic features: the **combined** MMA + homocystinuria biochemistry, and the **normal serum B12** (the block is intracellular trafficking, not absorption). Therapeutically, high-dose parenteral hydroxocobalamin can partially overcome the export block by mass action, which — together with betaine and carnitine — rationalizes the guideline regimen. The dominant prognostic lever is **time-to-treatment**, making newborn screening the single most impactful intervention.

---

## Evidence Base

| PMID | Paper (abbrev.) | Supports |
|---|---|---|
| [22922874](https://pubmed.ncbi.nlm.nih.gov/22922874/) | *Mutations in ABCD4 cause a new inborn error of B12 metabolism* | F001, F002, F005, F007 — gene discovery, lysosomal localization, cblF mimicry |
| [33729671](https://pubmed.ncbi.nlm.nih.gov/33729671/) | *Cobalamin J disease detected on newborn screening* | F001, F003, F006, F009, F010, F011 — phenotype, first neurotypical case, diagnosis |
| [41378236](https://pubmed.ncbi.nlm.nih.gov/41378236/) | *Cobalamin J in a teenager with abdominal pain* | F001, F003, F007, F010 — 8th case, novel p.Arg531Trp, ultra-rarity |
| [42303638](https://pubmed.ncbi.nlm.nih.gov/42303638/) | *LMBD1-dependent trafficking of ABCD4* | F002 — LMBD1 chaperone requirement |
| [38069516](https://pubmed.ncbi.nlm.nih.gov/38069516/) | *TM helix 6 of ABCD4 indispensable for transport* | F002, F008 — substrate recognition; in vitro modeling |
| [22422209](https://pubmed.ncbi.nlm.nih.gov/22422209/) | *Leukoencephalopathies of cobalamin/folate metabolism* | F005, F009 — two-reaction cofactor logic; leukodystrophy |
| [42231716](https://pubmed.ncbi.nlm.nih.gov/42231716/) | *Guidelines for Remethylation Disorders (2026 revision)* | F004, F006, F010, F011 — treatment & diagnostic standards |
| [34655177](https://pubmed.ncbi.nlm.nih.gov/34655177/) | *Prenatal diagnosis of combined MMA+HC* | F006, F007 — differential gene list, prenatal diagnosis |
| [32186706](https://pubmed.ncbi.nlm.nih.gov/32186706/) | *mmachc zebrafish model* | F008 — related-gene animal model |
| [35013307](https://pubmed.ncbi.nlm.nih.gov/35013307/) | *Hcfc1/Ronin mouse models* | F008 — related cblX-like mouse models |
| [23546813](https://pubmed.ncbi.nlm.nih.gov/23546813/) | *Cobalamin defect presenting as DKA* | F003, F011 — atypical presentation; supportive regimen |
| [23751581](https://pubmed.ncbi.nlm.nih.gov/23751581/) | *Outcomes of combined MMA+HC after treatment* | Prognosis context (49/55 with neurological impairment) |

**Supporting vs challenging:** All confirmed findings are mutually reinforcing; no paper directly challenges the core mechanism. The principal *tension* is between the guideline/cohort evidence (largely from cblC and broader combined-MMA+HC populations) and the very small cblJ-specific dataset — meaning some treatment and prognosis statements are **extrapolated** rather than cblJ-specific.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity (~8 patients)** precludes reliable estimates of prevalence, incidence, penetrance quantification, robust genotype–phenotype correlation, and formal survival statistics.
2. **Treatment and prognosis data are largely extrapolated** from cblC/cblF and broader combined-MMA+HC cohorts; no cblJ-specific randomized or large observational data exist.
3. **No dedicated ABCD4/cblJ animal model** — mechanistic inferences at the tissue/organ level rely on cellular assays and related-gene models.
4. **Steps 3–4 of the causal chain** (lysosomal trapping → cytosolic MMACHC/MMADHC starvation) are inferred from shared-pathway logic and cblF mimicry rather than direct cblJ demonstration.
5. **Vascular/thromboembolic and leukoencephalopathy risks** are inferred from the remethylation-disorder class, not directly quantified in cblJ patients.
6. **No epigenetic, modifier-gene, or population-frequency data** specific to cblJ.

## Proposed Follow-up Experiments / Actions

1. **Establish an international cblJ registry** to pool the handful of cases for natural-history, genotype–phenotype, and long-term outcome data.
2. **Generate a validated ABCD4 animal model** (zebrafish *abcd4* knockout by analogy to *mmachc*; conditional mouse *Abcd4*) to test tissue-level pathophysiology and therapy response.
3. **Directly test the trapping→starvation step** in patient fibroblasts using compartment-resolved cobalamin cofactor assays (AdoCbl/MeCbl quantification) before/after hydroxocobalamin.
4. **Systematically genotype–phenotype map** reported *ABCD4* variants against ATPase-domain vs TM6 vs trafficking effects using the proteoliposome/chimera platform.
5. **Prospectively evaluate high-dose parenteral hydroxocobalamin dosing** and betaine in screen-detected cblJ neonates, with total homocysteine/MMA/methionine as biomarkers.
6. **Assess vascular/thrombotic and white-matter outcomes** longitudinally with MRI and homocysteine monitoring in the small treated cohort.
7. **Advocate for inclusion of the combined-MMA+HC C3 marker** in newborn screening panels where absent, given the demonstrated prognostic benefit of presymptomatic treatment.

---

*Report compiled from 11 confirmed findings and 26 reviewed papers across a 5-iteration autonomous investigation. Evidence source types: human clinical case reports/series, in vitro/cellular functional studies, structural biology (cryo-EM / proteoliposome reconstitution), and related-gene model-organism studies.*


## Artifacts

- [OpenScientist final report](Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Methylmalonic_Acidemia_With_Homocystinuria_Type_cblJ-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

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
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013925` (2 mentions) - the report calls it "MONDO"; MONDO calls it **methylmalonic acidemia with homocystinuria, type cblJ**
- `GO:0005764` (3 mentions) - the report calls it "Subcellular compartments:** lysosome"; GO calls it **lysosome**
- `HP:0011968` (1 mention) - the report calls it "Clinical sign"; HP calls it **Feeding difficulties**
- `HP:0001508` (1 mention) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0001263` (1 mention) - the report calls it "Clinical sign"; HP calls it **Global developmental delay**
- `HP:0025406` (1 mention) - the report calls it "Symptom"; HP calls it **Asthenia**
- `HP:0012120` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Methylmalonic aciduria**
- `HP:0002160` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperhomocystinemia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0500152` (1 mention) - the report calls it "hypomethioninemia"; HP calls it **Hypocystinemia**
- `GO:0006555` (1 mention) - the report calls it "methionine metabolic process"; GO calls it **L-methionine metabolic process**