---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T17:19:07.695234'
end_time: '2026-10-28T17:37:30.056822'
duration_seconds: 1102.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Amegakaryocytic Thrombocytopenia 1
  mondo_id: MONDO:0800452
  category: Mendelian
  causal_genes: MPL
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 27
  on_topic: 23
  validator_version: 0.4.0
term_validation:
  total_terms: 30
  verified: 27
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.036
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0001873
    reported_labels:
    - Laboratory / clinical
    ontology_label: Thrombocytopenia
  - term_id: HP:0001876
    reported_labels:
    - Laboratory
    ontology_label: Pancytopenia
  - term_id: HP:0002170
    reported_labels:
    - Clinical sign
    ontology_label: Intracranial hemorrhage
  - term_id: HP:0001627
    reported_labels:
    - Physical malformation
    ontology_label: Abnormal heart morphology
  - term_id: HP:0001507
    reported_labels:
    - Physical
    ontology_label: Growth abnormality
  - term_id: HP:0001263
    reported_labels:
    - Behavioral/neuro
    ontology_label: Global developmental delay
  labels_variant: 1
  unresolved_terms:
  - HP:0004811
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
  path: Congenital_Amegakaryocytic_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Amegakaryocytic_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Amegakaryocytic Thrombocytopenia 1
- **MONDO ID:** MONDO:0800452 (if available)
- **Causal gene(s):** MPL
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

Please provide a comprehensive research report on **Congenital Amegakaryocytic Thrombocytopenia 1** covering all of the
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

# Congenital Amegakaryocytic Thrombocytopenia 1 (CAMT1): A Comprehensive Disease Characteristics Report

**Disease:** Congenital Amegakaryocytic Thrombocytopenia type 1 (CAMT1)
**MONDO ID:** MONDO:0800452 · **OMIM:** #604498 · **Causal gene:** **MPL** (thrombopoietin receptor, c-MPL / TpoR; HGNC:7217)
**Category:** Mendelian, autosomal recessive

---

## Summary

**Congenital Amegakaryocytic Thrombocytopenia type 1 (CAMT1) is a rare, autosomal-recessive inherited bone marrow failure syndrome caused by biallelic loss-of-function mutations in *MPL*, the gene encoding the thrombopoietin (TPO) receptor, c-MPL/TpoR.** The name is a serial descriptor; the defining molecular lesion is MPL deficiency, and this report follows the MONDO ID (MONDO:0800452) and the designated causal gene throughout. CAMT caused by MPL mutation is frequently written "CAMT-MPL" to distinguish it from phenocopies caused by other genes (e.g., MECOM/RUSAT-2, RBM8A/TAR, THPO).

Clinically, CAMT1 presents at or shortly after birth as **severe isolated thrombocytopenia with reduced or absent bone marrow megakaryocytes**, classically without the limb or skeletal anomalies that mark its differential diagnoses. Over the first years of life (mean ~4 years), the isolated thrombocytopenia **progresses to trilineage pancytopenia / aplastic anemia** because MPL signaling is required not only for megakaryopoiesis but also for the survival and quiescence of hematopoietic stem cells (HSCs). The pathophysiology is a clean causal chain: loss of TPO→MPL→JAK2/STAT5/MAPK/PI3K signaling abolishes megakaryocyte production (→ thrombocytopenia) and removes the anti-apoptotic, quiescence-enforcing maintenance of HSCs (→ progressive stem-cell exhaustion and marrow aplasia). Because the receptor that normally clears TPO is absent, serum TPO is markedly elevated — a key diagnostic clue.

**Allogeneic hematopoietic stem cell transplantation (HSCT) is the only curative therapy**, with roughly 86% six-year overall survival in the largest registry series, though graft failure remains a challenge. TPO-receptor agonists (eltrombopag, romiplostim) are generally ineffective in MPL-null disease because the drug target itself is absent; responses across inherited thrombocytopenias are genotype-unpredictable. Genotype-phenotype correlation exists at the level of allele class — null "type I" mutations generally cause earlier, more severe disease than hypomorphic "type II" missense mutations — but this correlation is imperfect and should not delay transplant planning. A notable biological lesson is that *Mpl*-knockout mice reproduce the thrombocytopenia but **not** the aplastic anemia, so patient-derived induced pluripotent stem cells (iPSCs) have become the key human model, implicating FLI1-dependent transcriptional control of megakaryocyte/erythroid fate.

This report integrates 10 confirmed findings and 40 reviewed papers into a full disease-knowledge-base entry across all 15 requested domains.

---

## Key Findings

### Finding 1 — CAMT1 is caused by biallelic loss-of-function *MPL* mutations

CAMT (MIM #604498) is an autosomal-recessive inherited bone marrow failure syndrome caused by **homozygous or compound heterozygous mutations in *MPL***, the gene encoding the thrombopoietin receptor (c-MPL/TpoR). The comprehensive CAMT-MPL cohort of 56 patients ([PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)) defined genotype-phenotype correlations and added 17 novel mutations. The disorder is characterized diagnostically by **elevated serum TPO** and **reduced platelet c-MPL and bone marrow colonies** ([PMID: 17666371](https://pubmed.ncbi.nlm.nih.gov/17666371/)).

> *"Congenital amegakaryocytic thrombocytopenia caused by deleterious homozygous or compound heterozygous mutations in MPL (CAMT-MPL) is a rare inherited bone marrow failure syndrome presenting as an isolated thrombocytopenia at birth progressing to pancytopenia due to exhaustion of hematopoietic progenitors."* — [PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)

> *"Most of the cases of congenital amegakaryocytic thrombocytopenia are caused by defective expression or function of the thrombopoietin receptor due to homozygous or compound heterozygous mutations in the gene MPL."* — [PMID: 19388932](https://pubmed.ncbi.nlm.nih.gov/19388932/)

### Finding 2 — Mutation type predicts clinical course: "type I" (null) vs "type II" (hypomorphic)

In the founding cohort (Ballmaier et al., [PMID: 11133753](https://pubmed.ncbi.nlm.nih.gov/11133753/)), all 8 CAMT patients carried c-mpl mutations that segregated into two mechanistic classes. **Type I** — nonsense/frameshift mutations predicting complete loss of c-Mpl function — was associated with earlier, more persistent severe thrombocytopenia and earlier progression to pancytopenia. **Type II** — missense mutations in the extracellular domain predicting partial residual receptor function — was associated with a transient early platelet increase and later marrow failure. The 56-patient cohort ([PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)) confirmed reliable genotype-phenotype correlations.

> *"We found frameshift or nonsense mutations that are predicted to result in a complete loss of c-Mpl function in 5 patients. Heterozygous or homozygous missense mutations predicted to lead to amino acid exchanges in the extracellular domain of the receptor were found in 3 other patients. The type of mutations correlated with the clinical course of the disease."* — [PMID: 11133753](https://pubmed.ncbi.nlm.nih.gov/11133753/)

**Caveat:** Savoia et al. ([PMID: 17666371](https://pubmed.ncbi.nlm.nih.gov/17666371/)) found no strict correlation and cautioned against delaying HSCT based on predicted residual receptor activity. The correlation is therefore real at the population level but not deterministic for the individual patient.

### Finding 3 — Allogeneic HSCT is the only curative therapy (~86% 6-year survival)

The EBMT registry study of 66 CAMT patients undergoing allo-HSCT (Aldebert et al., 2024, [PMID: 39289521](https://pubmed.ncbi.nlm.nih.gov/39289521/)) reported **6-year overall survival of 85.6%**, disease-free survival 66.9%, and transplant-related mortality 8.0%, but a cumulative graft failure of 25% and second transplant in 17%. Bone marrow was the most common stem cell source (61%), and myeloablative busulfan-based conditioning was used most frequently. A myeloablative umbilical cord blood transplant series ([PMID: 26369627](https://pubmed.ncbi.nlm.nih.gov/26369627/)) showed durable engraftment in 5/5 patients at a median 14-year follow-up.

> *"The 6-year disease-free survival (DFS) and overall survival (OS) were 66.9% and 85.6%, respectively. The 6-year transplant-related mortality (TRM) was 8.0%. In conclusion, most patients with CAMT benefit from allo-HSCT, but with many graft failures."* — [PMID: 39289521](https://pubmed.ncbi.nlm.nih.gov/39289521/)

### Finding 4 — TPO-MPL signals via JAK2/STAT5 and MAPK/PI3K; loss abolishes megakaryopoiesis and HSC maintenance

TPO is constitutively produced by liver and kidney. It binds MPL — a cytokine-receptor-superfamily protein lacking intrinsic kinase activity — inducing receptor homodimerization. The major proliferative signal proceeds through **JAK2/STAT5**, with differentiation driven by **sustained MAPK** activation; **PI3K/AKT** is also engaged ([PMID: 9831170](https://pubmed.ncbi.nlm.nih.gov/9831170/)). Cryo-EM structures of the TPO-MPL complex ([PMID: 37633268](https://pubmed.ncbi.nlm.nih.gov/37633268/); [PMID: 40766813](https://pubmed.ncbi.nlm.nih.gov/40766813/)) reveal homodimeric activation and rationalize loss-of-function thrombocytopenia mutations at the TPO-MPL binding interface and JAK2 dimerization via the pseudokinase domain. Plasma TPO is regulated by platelet/megakaryocyte mass through MPL binding, internalization, and degradation — explaining why serum TPO is elevated in CAMT (there is no receptor to clear it).

> *"Upon ligand-induced Mpl homodimerization, the major signaling events for proliferation are mediated through the JAK2/STAT5 pathway, while differentiation might occur through a prolonged activation of the MAPK pathway."* — [PMID: 9831170](https://pubmed.ncbi.nlm.nih.gov/9831170/)

> *"revealing the basis for homodimeric MPL activation and providing a structural rationalization for genetic loss-of-function thrombocytopenia mutations"* — [PMID: 37633268](https://pubmed.ncbi.nlm.nih.gov/37633268/)

### Finding 5 — *Mpl*-/- mice recapitulate thrombocytopenia but not aplastic anemia

*c-mpl*-/- and *Tpo*-/- mice have near-identical phenotypes: severe thrombocytopenia (~10–15% of normal platelet count) with reduced megakaryocytes and reduced committed progenitors of all lineages; residual platelets are morphologically and functionally normal and prevent bleeding ([PMID: 10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/)). **Critically, unlike human CAMT, these mice maintain normal marrow cellularity and do NOT progress to aplastic anemia** ([PMID: 12799278](https://pubmed.ncbi.nlm.nih.gov/12799278/); [PMID: 10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/)). This confirms TPO is the sole c-Mpl ligand and the primary physiologic regulator of platelet production.

> *"TPO-/- and mpl-/- mice are severely thrombocytopenic indicating that TPO is the primary physiological regulator of platelet production in vivo."* — [PMID: 10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/)

> *"The platelets that are produced in the absence of TPO signalling are morphologically and functionally normal and residual production is sufficient to prevent bleeding and allow a normal lifespan."* — [PMID: 10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/)

### Finding 6 — Presentation as isolated neonatal thrombocytopenia progressing to pancytopenia; diagnosis uses elevated TPO and marrow findings

CAMT presents as severe isolated hypomegakaryocytic thrombocytopenia at birth (HP:0001873 Thrombocytopenia), classically without characteristic physical anomalies, progressing to trilineage pancytopenia/aplastic anemia usually within the first years of life (mean ~4 years; earliest <6 months). In a 20-patient series ([PMID: 16351641](https://pubmed.ncbi.nlm.nih.gov/16351641/)), 14/20 developed pancytopenia and one died of bleeding; some patients had cardiac defects (2), growth abnormalities (6), and psychomotor retardation (4). The 56-patient cohort ([PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)) found thrombocytopenia was NOT detected at birth in ~25% of patients, and highlighted head-region anomalies (brain, ocular/orbital) and intracranial hemorrhage as severe complications. Diagnostic hallmarks: **markedly elevated serum TPO, absent/reduced bone marrow megakaryocytes, reduced platelet c-MPL, confirmed by MPL sequencing**.

> *"Development of pancytopenia was observed in 14 of the patients, only one patient presented with an isolated thrombocytopenia over a period of over 14 years. One boy died from bleeding complications."* — [PMID: 16351641](https://pubmed.ncbi.nlm.nih.gov/16351641/)

> *"An important and new finding was that thrombocytopenia was not detected at birth in a quarter of the patients."* — [PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)

> *"Patients affected by other IBMFS - especially Fanconi anemia or dyskeratosis congenita - may be misdiagnosed as having CAMT"* — [PMID: 34404532](https://pubmed.ncbi.nlm.nih.gov/34404532/)

### Finding 7 — Autosomal recessive, ultra-rare, with risk of clonal progression to MDS/AML

Inheritance is autosomal recessive (biallelic MPL). Orphanet prevalence is **<1/1,000,000**, with only hundreds of cases reported worldwide (96 reviewed in [PMID: 22102270](https://pubmed.ncbi.nlm.nih.gov/22102270/)). As an inherited bone marrow failure syndrome with germline predisposition, CAMT carries a recognized risk of clonal evolution to **myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML)** ([PMID: 30573048](https://pubmed.ncbi.nlm.nih.gov/30573048/)), underscoring the need for hematologic surveillance and timely allogeneic HSCT.

> *"given differences in the risk of disease progression to myelodysplastic syndrome, acute myeloid leukemia, and other malignancies"* — [PMID: 30573048](https://pubmed.ncbi.nlm.nih.gov/30573048/)

> *"The present review summarizes clinical and laboratory data for 96 patients with CAMT, reported since 1990."* — [PMID: 22102270](https://pubmed.ncbi.nlm.nih.gov/22102270/)

### Finding 8 — CAMT1 sits within a broad monogenic inherited-thrombocytopenia differential; TPO-agonist response is genotype-unpredictable

Inherited thrombocytopenias are caused by defects in **more than 50 genes** affecting platelet production ([PMID: 41766040](https://pubmed.ncbi.nlm.nih.gov/41766040/)). Beyond MPL-CAMT, the neonatal/severe differential includes **THPO** (ligand side), **MECOM/HOXA11** (RUSAT), **RBM8A** (TAR), Fanconi anemia and dyskeratosis congenita genes, **GFI1B** (autosomal dominant, α-granule deficiency, persistent CD34), **GNE** (autosomal recessive), and the leukemia-predisposition familial platelet disorders **ANKRD26/ETV6/RUNX1**. TPO-receptor agonists give variable, genotype-unpredictable responses — even siblings with the same variant can differ ([PMID: 41359897](https://pubmed.ncbi.nlm.nih.gov/41359897/)) — and are ineffective in MPL-null CAMT because the receptor target is absent ([PMID: 20188141](https://pubmed.ncbi.nlm.nih.gov/20188141/)).

> *"Inherited thrombocytopenias (ITs) constitute a heterogeneous group of congenital bleeding disorders caused by defects in over 50 genes that predominantly affect platelet production."* — [PMID: 41766040](https://pubmed.ncbi.nlm.nih.gov/41766040/)

> *"the observed responses may differ even in siblings carrying the same mutation"* — [PMID: 41359897](https://pubmed.ncbi.nlm.nih.gov/41359897/)

### Finding 9 — TPO/MPL maintains HSC numbers by inhibiting apoptosis and enforcing quiescence — the mechanistic basis for marrow failure

THPO promotes both self-renewal and cell-cycle quiescence of adult bone-marrow HSCs, which express MPL on HSCs and multipotent progenitors (MPPs). In adult inducible *Thpo*-knockout mice, THPO "primarily maintains adult BM HSC numbers by inhibiting apoptosis," and THPO is "critical during neonatal development to establish a structured HSC and MPP hierarchy" ([PMID: 41895275](https://pubmed.ncbi.nlm.nih.gov/41895275/)). THPO also stimulates HSC mitochondrial homeostasis/metabolism ([PMID: 34248130](https://pubmed.ncbi.nlm.nih.gov/34248130/)), and MPL activation upregulates Galectin-3 to enforce quiescence via p21 ([PMID: 33837181](https://pubmed.ncbi.nlm.nih.gov/33837181/)). This provides the demonstrated (mouse) mechanistic basis for the previously inferred branch of CAMT pathophysiology: loss of MPL signaling removes anti-apoptotic/quiescence maintenance of HSCs, driving progressive stem-cell attrition and trilineage aplastic anemia.

> *"THPO primarily maintains adult BM HSC numbers by inhibiting apoptosis"* — [PMID: 41895275](https://pubmed.ncbi.nlm.nih.gov/41895275/)

> *"THPO function is thus limited during adult hematopoiesis but is critical during neonatal development to establish a structured HSC and MPP hierarchy."* — [PMID: 41895275](https://pubmed.ncbi.nlm.nih.gov/41895275/)

### Finding 10 — Patient-derived iPSCs model the human disease where mice fail, implicating FLI1-dependent fate control

Patient-derived CAMT iPSCs recapitulate defective MPL-mediated signaling in vitro (Hirata et al., 2013, [PMID: 23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/)). Because *Mpl*-/- mice do not exhibit the human disease phenotype, iPSCs were used as a human disease-tracing system. MPL signaling proved essential for maintenance of the CD34+ multipotent progenitor (MPP) population and development of the CD41+GPA+ megakaryocyte-erythrocyte progenitor (MEP) population. MPL overexpression impaired erythropoiesis and increased aberrant megakaryocyte production specifically in CAMT iPSC-derived CD34+ cells, reflecting differential expression of the transcription factor **FLI1**.

> *"Because Mpl(-/-) mice do not exhibit the human disease phenotype, we used an in vitro disease tracing system with induced pluripotent stem cells (iPSCs) derived from a CAMT patient"* — [PMID: 23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/)

> *"MPL signaling is essential for maintenance of the CD34+ multipotent hematopoietic progenitor (MPP) population and development of the CD41+GPA+ megakaryocyte-erythrocyte progenitor (MEP) population"* — [PMID: 23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/)

> *"impaired transcriptional regulation of the MPL signaling that normally governs megakaryopoiesis and erythropoiesis underlies CAMT"* — [PMID: 23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/)

---

## Report by Section

### 1. Disease Information

CAMT1 is a rare, inherited (congenital) bone marrow failure syndrome defined molecularly by biallelic loss-of-function mutations in **MPL**, the thrombopoietin receptor gene. It presents in the neonatal period as severe amegakaryocytic (hypomegakaryocytic) thrombocytopenia and progresses to aplastic anemia / pancytopenia.

**Key identifiers:**
- **OMIM:** #604498
- **MONDO:** MONDO:0800452
- **Orphanet:** ORPHA:3319 (Congenital amegakaryocytic thrombocytopenia)
- **ICD-10:** D69.4 (other primary thrombocytopenia) / D61.0 (constitutional aplastic anemia) as the disease evolves
- **ICD-11:** 3B64.1 region (congenital thrombocytopenia); bone marrow failure codes apply on progression
- **MeSH:** Thrombocytopenia, Congenital; Bone Marrow Failure Disorders
- **Gene:** MPL (HGNC:7217; NCBI Gene 4352; UniProt P40238; chromosome 1p34.2)

**Synonyms / alternative names:** CAMT; CAMT-MPL; congenital amegakaryocytic thrombocytopenia type 1; amegakaryocytic thrombocytopenia, congenital; thrombocytopenia with absent/reduced megakaryocytes (non-TAR).

**Information source:** Primarily **aggregated disease-level resources** (OMIM, Orphanet) and small-to-moderate published patient cohorts/case series (largest: 56 clinical and 66 transplant patients), rather than large EHR datasets, reflecting the disease's rarity.

### 2. Etiology

**Causal factor:** Entirely **genetic** — biallelic (homozygous or compound heterozygous) loss-of-function mutations in MPL (Findings 1, 2). There is no environmental or infectious cause.

**Genetic risk factors:** The causal variants are the MPL mutations themselves. Being a heterozygous carrier confers no disease (recessive). No validated modifier genes are established in humans, though differential FLI1 expression modulates the cellular phenotype (Finding 10).

**Environmental / lifestyle / protective factors:** None established — CAMT1 is a monogenic Mendelian disorder; environmental exposures, diet, and lifestyle are not etiologic. No protective alleles or exposures are described. Consanguinity increases the likelihood of homozygous presentation (recessive inheritance).

**Gene-environment interactions:** Not applicable as a disease-causing mechanism. The main "interaction" of clinical relevance is iatrogenic: response (or lack thereof) to TPO-receptor agonists depends on which MPL allele is present (Finding 8; [PMID: 20188141](https://pubmed.ncbi.nlm.nih.gov/20188141/)).

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Thrombocytopenia (severe) | Laboratory / clinical | HP:0001873 | Neonatal (not detected at birth in ~25%) | Severe | ~100% (defining) |
| Reduced/absent marrow megakaryocytes | Laboratory/pathology | HP:0004811 (reduced megakaryocytes) | Neonatal | Severe | ~100% |
| Pancytopenia / aplastic anemia | Laboratory | HP:0001876 | Childhood (mean ~4 yr; earliest <6 mo) | Severe | ~70% (14/20, [PMID: 16351641](https://pubmed.ncbi.nlm.nih.gov/16351641/)) |
| Petechiae / bruising / bleeding | Clinical sign | HP:0000967 / HP:0001892 | Neonatal | Moderate–severe | Common |
| Intracranial hemorrhage | Clinical sign | HP:0002170 | Neonatal/infancy | Severe (can be fatal) | Subset ([PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)) |
| Elevated serum thrombopoietin | Laboratory biomarker | — | Congenital | — | ~100% |
| Cardiac defects | Physical malformation | HP:0001627 | Congenital | Variable | Minority (2/20) |
| Growth abnormalities | Physical | HP:0001507 | Childhood | Variable | Minority (6/20) |
| Psychomotor/developmental delay | Behavioral/neuro | HP:0001263 | Childhood | Variable | Minority (4/20) |
| Head-region (brain, ocular/orbital) anomalies | Physical | HP:0000240 / HP:0000478 | Congenital | Variable | Subset (56-pt cohort) |

**Progression:** Isolated thrombocytopenia → progressive, often severe, trilineage pancytopenia (progressive course). **Quality-of-life impact:** Dominated by bleeding risk in infancy (including life-threatening intracranial hemorrhage) and, later, by transfusion dependence, infection risk from marrow failure, and the morbidity of HSCT. Classically CAMT lacks the limb anomalies of TAR/RUSAT, which is a diagnostically useful negative.

### 4. Genetic / Molecular Information

**Causal gene:** **MPL** (OMIM *159530; chromosome 1p34.2). Encodes the thrombopoietin receptor (c-MPL/TpoR), a type I single-pass transmembrane cytokine-receptor-superfamily protein.

**Pathogenic variants:**
- **Variant types:** Nonsense, frameshift, splice-site (e.g., intron 11 splice variant, [PMID: 23625800](https://pubmed.ncbi.nlm.nih.gov/23625800/)), and missense. Representative reported alleles include nonsense mutations such as p.Tyr63* (c.189C>A) and p.Arg357* (c.1069C>T), the latter a novel mutation ([PMID: 21162090](https://pubmed.ncbi.nlm.nih.gov/21162090/)).
- **Classification (ACMG/AMP):** Pathogenic / likely pathogenic for null and well-characterized missense alleles.
- **Variant class / functional consequence:** **Loss of function** — complete (type I null) or partial (type II hypomorphic), the latter affecting the extracellular ligand-binding domain and leaving some residual signaling (Finding 2). All are **germline**.
- **Allele frequency:** Individually rare/absent in gnomAD, consistent with ultra-rare recessive disease.
- **Somatic vs germline:** Germline. (Note: *somatic* gain-of-function MPL mutations, e.g. MPL W515, cause myeloproliferative neoplasms — a separate disease class and not CAMT.)

**Modifier genes:** No established human modifiers; **FLI1** transcriptional output modulates the megakaryocyte-vs-erythroid cellular phenotype in patient iPSCs (Finding 10).

**Epigenetic / chromosomal abnormalities:** None are primary causes. On clonal evolution to MDS/AML, secondary cytogenetic abnormalities (e.g., monosomy 7) may be acquired (Finding 7).

### 5. Environmental Information

Not applicable to disease causation. CAMT1 is a monogenic germline disorder with no toxic, radiation, lifestyle, or infectious etiology. Infectious agents are relevant only as *complications* of the marrow failure / post-transplant immunosuppression, not as causes.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function mutation in *MPL*** (germline) **leads to** absent or defective thrombopoietin receptor (c-MPL) on hematopoietic stem cells, progenitors, and megakaryocytes. *(Demonstrated.)*
2. Absent/defective MPL **results in** failure of TPO-induced receptor homodimerization and loss of downstream **JAK2/STAT5** (proliferation), **MAPK** (differentiation), and **PI3K/AKT** signaling. *(Demonstrated — structural + biochemical, [PMID: 9831170](https://pubmed.ncbi.nlm.nih.gov/9831170/), [PMID: 37633268](https://pubmed.ncbi.nlm.nih.gov/37633268/).)*
3. **Branch A (megakaryocyte lineage):** Loss of MPL signaling **abolishes** CFU-megakaryocyte proliferation and megakaryocyte maturation **→** absent/reduced marrow megakaryocytes **→ severe thrombocytopenia from birth**. *(Demonstrated.)*
4. **Branch B (stem-cell compartment):** Loss of MPL signaling **removes** the anti-apoptotic and quiescence-enforcing maintenance of HSCs/MPPs (mediated via STAT5, Galectin-3/p21, and mitochondrial homeostasis) **→** progressive HSC apoptosis and exhaustion **→ trilineage pancytopenia / aplastic anemia** over the first years of life. *(Mechanism demonstrated in mouse; progression demonstrated in human; [PMID: 41895275](https://pubmed.ncbi.nlm.nih.gov/41895275/), [PMID: 12799278](https://pubmed.ncbi.nlm.nih.gov/12799278/).)*
5. Impaired **FLI1-dependent transcriptional regulation** in MPL-deficient progenitors **skews** megakaryocyte/erythroid fate decisions **→** defective MEP development (human iPSC model). *(Demonstrated in vitro, [PMID: 23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/).)*
6. Absence of MPL **prevents** TPO clearance (normally via receptor binding/internalization/degradation) **→ markedly elevated serum TPO** (diagnostic biomarker). *(Inferred from MPL biology; consistent with observed elevated TPO.)*
7. Germline bone-marrow-failure predisposition **leads to** selective pressure for clonal escape **→ risk of MDS/AML**. *(Demonstrated as a class risk for IBMFS, [PMID: 30573048](https://pubmed.ncbi.nlm.nih.gov/30573048/).)*

```
         MPL biallelic LOF mutation
                    │
         no/defective TPO receptor
                    │
     loss of JAK2/STAT5 + MAPK + PI3K/AKT
            ┌───────┴────────┐
    Branch A              Branch B
 megakaryopoiesis      HSC maintenance
    abolished          (anti-apoptosis,
        │               quiescence) lost
  absent megakaryocytes      │
        │              HSC exhaustion
  THROMBOCYTOPENIA           │
  (neonatal)          PANCYTOPENIA / APLASTIC
        │             ANEMIA (~mean 4 yr)
        └──────┬──────────┘
          germline IBMFS → MDS/AML risk
```

**Molecular pathways:** JAK-STAT (JAK2→STAT5), RAS/MAPK, PI3K-AKT (KEGG hsa04630 Jak-STAT; Reactome "Signaling by Thrombopoietin").
**Cellular processes & GO terms:** Negative regulation of apoptosis (GO:0043066, TPO is anti-apoptotic), stem-cell population maintenance (GO:0019827), megakaryocyte differentiation (GO:0030219), thrombopoietin-mediated signaling pathway (GO:0038163), mitochondrial homeostasis.
**Cell types (CL):** Hematopoietic stem cell (CL:0000037), megakaryocyte (CL:0000556), megakaryocyte-erythroid progenitor (CL:0000050), common myeloid progenitor (CL:0000049).
**Immune involvement:** Secondary — inhibitory cytokines (TNF-α, IFN-γ) are increased in marrow during the pancytopenic phase, possibly amplifying aplasia ([PMID: 17666371](https://pubmed.ncbi.nlm.nih.gov/17666371/)).
**Protein dysfunction (CHEBI/ontology):** MPL is a plasma-membrane receptor (GO:0005886); LOF mutations impair ligand binding or surface expression (structural rationale in [PMID: 37633268](https://pubmed.ncbi.nlm.nih.gov/37633268/)).

### 7. Anatomical Structures Affected

- **Primary organ:** Bone marrow (UBERON:0002371), specifically the hematopoietic compartment.
- **Body system:** Hematopoietic/immune system (UBERON:0002390 bone marrow; UBERON:0000178 blood).
- **Secondary involvement:** Central nervous system (intracranial hemorrhage from thrombocytopenia); occasional congenital anomalies of heart (UBERON:0000948), eye/orbit (UBERON:0000970), and brain (UBERON:0000955) reported in a subset.
- **Tissue/cell level:** Myeloid tissue; megakaryocytes (reduced/absent) and HSCs/MPPs (progressively depleted); all three hematopoietic lineages ultimately affected.
- **Subcellular (GO Cellular Component):** Plasma membrane receptor complex (GO:0005886); mitochondrion (GO:0005739, TPO-regulated HSC mitochondrial homeostasis).
- **Localization/lateralization:** Systemic marrow involvement (bilateral/diffuse); bleeding manifestations are site-dependent.

### 8. Temporal Development

- **Onset:** Congenital — thrombocytopenia usually detectable at or shortly after birth, though ~25% are not identified at birth ([PMID: 32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/)).
- **Progression:** Chronic, progressive. Isolated thrombocytopenia → pancytopenia/aplastic anemia at a **mean of ~4 years** (earliest <6 months; one report of severe pancytopenia within the first month, [PMID: 23625800](https://pubmed.ncbi.nlm.nih.gov/23625800/)).
- **Course pattern:** Progressive marrow failure; type I (null) alleles tend to progress earlier and more severely than type II (hypomorphic) (Finding 2).
- **Remission:** No spontaneous remission; durable correction only via HSCT (treatment-induced, Finding 3).
- **Critical period / window of opportunity:** Early childhood, before irreversible marrow exhaustion and before clonal evolution — the rationale for not delaying transplant ([PMID: 17666371](https://pubmed.ncbi.nlm.nih.gov/17666371/)).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic MPL).
- **Penetrance:** Effectively complete in individuals with two LOF alleles; **expressivity is variable**, influenced by allele class (type I vs II) and modifiers.
- **Epidemiology:** Ultra-rare; Orphanet prevalence **<1/1,000,000**; ~96 patients reviewed in one survey ([PMID: 22102270](https://pubmed.ncbi.nlm.nih.gov/22102270/)), hundreds reported worldwide.
- **Carrier frequency:** Very low; carriers are asymptomatic.
- **Consanguinity / founder effects:** Consanguinity increases homozygous presentation; no single dominant founder allele established — the mutational spectrum is heterogeneous across populations.
- **Sex ratio:** Approximately equal (autosomal). **Age distribution:** Essentially all pediatric onset.
- **Anticipation / mosaicism:** Not features of this recessive single-gene disorder.

### 10. Diagnostics

**Laboratory / clinical tests:**
- CBC: severe **isolated thrombocytopenia** (later pancytopenia).
- **Markedly elevated serum TPO** (hallmark) — due to absent receptor-mediated clearance.
- **Reduced platelet surface c-MPL** and reduced megakaryocyte colony formation ([PMID: 17666371](https://pubmed.ncbi.nlm.nih.gov/17666371/)).
- **Bone marrow:** reduced/absent megakaryocytes with initially preserved then declining overall cellularity (biopsy/aspirate histopathology).

**Genetic testing (confirmatory):** **Single-gene MPL sequencing** or inherited-thrombocytopenia / bone-marrow-failure **gene panels** (including MPL, THPO, MECOM, RBM8A, HOXA11, GFI1B, GNE, RUNX1, ANKRD26, ETV6, Fanconi and dyskeratosis-congenita genes). **WES/WGS** are useful when panels are non-diagnostic or the phenotype is atypical. Chromosomal microarray/karyotype help exclude TAR (RBM8A/1q21.1 deletion) and monitor for clonal cytogenetic evolution (e.g., monosomy 7).

**Clinical criteria / differential diagnosis:** Diagnosis rests on the triad of congenital hypomegakaryocytic thrombocytopenia + elevated TPO + biallelic MPL mutation. Differential includes **TAR (RBM8A)**, **RUSAT-2 (MECOM)** ([PMID: 41635268](https://pubmed.ncbi.nlm.nih.gov/41635268/)), **Fanconi anemia**, **dyskeratosis congenita**, **THPO deficiency**, **GFI1B** and **GNE** thrombocytopenias, and **SAMD9/SAMD9L** syndromes ([PMID: 31306780](https://pubmed.ncbi.nlm.nih.gov/31306780/)); patients with other IBMFS "may be misdiagnosed as having CAMT" ([PMID: 34404532](https://pubmed.ncbi.nlm.nih.gov/34404532/)).

**Screening:** No population newborn screen exists; **cascade/carrier testing** of relatives and prenatal/preimplantation testing are available once the familial variants are known.

### 11. Outcome / Prognosis

- **Natural history (untreated):** Progressive marrow failure with high risk of fatal bleeding (including intracranial hemorrhage) in infancy and death from aplastic anemia/infection in childhood; recognized risk of MDS/AML transformation (Finding 7).
- **With HSCT:** ~**85.6% 6-year overall survival**, 66.9% disease-free survival, 8.0% transplant-related mortality (EBMT, [PMID: 39289521](https://pubmed.ncbi.nlm.nih.gov/39289521/)); durable multi-decade engraftment achievable ([PMID: 26369627](https://pubmed.ncbi.nlm.nih.gov/26369627/)).
- **Complications:** Bleeding, transfusion dependence/iron overload, infections, graft failure (~25%) and need for second transplant (~17%), GvHD, and clonal/malignant evolution.
- **Prognostic factors:** Allele class (type I vs II), age at transplant, pre-transplant marrow cellularity, donor type/HLA match, and conditioning intensity.

### 12. Treatment

| Modality | Detail | Role | Suggested NCIT |
|---|---|---|---|
| **Allogeneic HSCT** | BM (most common, 61%), UCB, or PBSC; myeloablative busulfan-based conditioning | **Only curative therapy** (Finding 3) | Allogeneic Hematopoietic Stem Cell Transplantation (C15431) |
| **Supportive care** | Platelet transfusions, red-cell transfusions, infection prophylaxis | Bridge to transplant; symptom control | Supportive Care (C15277) |
| **TPO-receptor agonists** | Eltrombopag, romiplostim — generally **ineffective in MPL-null disease**; rare type-II alleles (e.g., F104S) may respond to specific transmembrane-targeting agonists in vitro | Mostly not applicable ([PMID: 20188141](https://pubmed.ncbi.nlm.nih.gov/20188141/)) | Eltrombopag (C62528); Romiplostim (C66952) |
| **Gene therapy (experimental)** | Retroviral/lentiviral MPL replacement; physiologic (Mpl-promoter) expression needed to avoid myeloproliferation/leukemia seen with overexpression | Investigational ([PMID: 19844195](https://pubmed.ncbi.nlm.nih.gov/19844195/)) | Gene Therapy (C15254) |

**Pharmacogenomics / personalized medicine:** Treatment is genotype-aware — MPL-null patients should proceed to HSCT rather than trial TPO-agonists; rare residual-function alleles may rarely respond to selected agonists. **Treatment algorithm:** diagnose early → supportive care + surveillance → HSCT when a suitable donor is available, ideally before marrow exhaustion or clonal evolution.

### 13. Prevention

- **Primary prevention:** Not possible for a germline monogenic disorder. **Genetic counseling** for couples with an affected child or known carrier status is central (25% recurrence risk per pregnancy).
- **Reproductive options (genetic screening):** **Prenatal diagnosis** and **preimplantation genetic testing** once familial MPL variants are identified; **cascade testing** of at-risk relatives.
- **Secondary prevention:** Early diagnosis (elevated TPO + marrow + MPL sequencing), hematologic surveillance for pancytopenia and clonal/cytogenetic evolution.
- **Tertiary prevention:** Bleeding-risk management, infection prophylaxis, timely HSCT to prevent irreversible marrow failure and malignant transformation.
- **Immunization / public health:** Not applicable to disease causation; standard immunization and infection-prevention measures apply peri-transplant.

### 14. Other Species / Natural Disease

- **Taxonomy:** Human (NCBI:txid9606). Experimental disease modeled in *Mus musculus* (NCBI:txid10090).
- **Orthologous gene:** mouse *Mpl* (NCBI Gene 17480). MPL/TPO signaling is evolutionarily conserved across mammals.
- **Natural disease in other species:** No well-characterized spontaneous animal homolog of CAMT is established in OMIA; the disease is understood primarily through engineered mouse knockouts (Finding 5) and human iPSC models (Finding 10).
- **Comparative pathology:** *Mpl*-/- mice reproduce thrombocytopenia but **not** the aplastic-anemia progression — a key species difference limiting the mouse as a full model and implying greater human HSC dependence on MPL.
- **Zoonotic potential:** None (genetic disease).

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Limitation | Reference |
|---|---|---|---|---|
| ***Mpl*-/- mouse** | Mammalian knockout | Severe thrombocytopenia (~10–15% platelets), reduced megakaryocytes and multilineage progenitors | **Does NOT progress to aplastic anemia**; normal marrow cellularity maintained | [PMID: 10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/), [PMID: 12799278](https://pubmed.ncbi.nlm.nih.gov/12799278/) |
| ***Tpo*-/- mouse** | Mammalian knockout | Near-identical to *Mpl*-/- (confirms TPO is sole MPL ligand) | Same as above | [PMID: 10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/) |
| **CAMT patient iPSCs** | Human in vitro / cellular | Defective MPL signaling; loss of CD34+ MPP maintenance and CD41+GPA+ MEP development; FLI1 dysregulation | In vitro only; lacks marrow niche/in vivo progression | [PMID: 23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/) |
| **BaF3 / cell-line MPL mutants** | In vitro cell line | Models specific type-II alleles (e.g., F104S) and agonist responsiveness | Reductionist; single-lineage | [PMID: 20188141](https://pubmed.ncbi.nlm.nih.gov/20188141/) |
| **Retroviral Mpl BMT mouse** | Gene-therapy model | Tests MPL gene replacement; reveals leukemia/pancytopenia balance | Overexpression toxicity | [PMID: 19844195](https://pubmed.ncbi.nlm.nih.gov/19844195/) |

**Resources:** MGI (mouse *Mpl*), Cellosaurus (patient iPSC lines), ATCC/BaF3 (cell lines). The central lesson: **patient-derived iPSCs are the model of choice for the human-specific marrow-failure phenotype that mice do not reproduce.**

---

## Mechanistic Model / Interpretation

CAMT1 is, at its core, a **single-receptor-deficiency disease with a two-branch consequence**. The elegance of the mechanism is that MPL sits at the junction of two biological programs:

1. **Lineage program (megakaryopoiesis):** MPL is the dominant driver of megakaryocyte production. Its loss immediately and near-completely abolishes platelet production, explaining the congenital, severe, *isolated* thrombocytopenia — the first clinical act.

2. **Stewardship program (HSC maintenance):** MPL is also a survival/quiescence receptor for the entire stem-cell pool. Its loss is tolerated at birth (the HSC pool is still intact) but, over years, the absence of anti-apoptotic and quiescence-enforcing signaling causes **progressive stem-cell attrition**, converting isolated thrombocytopenia into **trilineage aplastic anemia** — the second clinical act. This temporal separation explains why CAMT is not simply "congenital thrombocytopenia" but a progressive bone-marrow-failure syndrome.

The **elevated serum TPO** is the fingerprint of the lesion: with no receptor to bind, internalize, and degrade TPO, the ligand accumulates. The **genotype-phenotype axis** (type I null vs type II hypomorphic) maps directly onto how much residual signaling survives, tuning the speed of both acts — though stochastic and modifier effects blur the correlation enough that it must not dictate transplant timing.

The **mouse-vs-human discordance** (thrombocytopenia yes, aplasia no in *Mpl*-/- mice) is itself mechanistically informative: it implies human HSCs are more dependent on MPL for long-term maintenance than mouse HSCs, or that compensatory pathways differ. Patient iPSCs bridge this gap and add the **FLI1 transcriptional node** as the lineage-fate switch downstream of MPL.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Evidence type |
|---|---|---|---|
| [32703794](https://pubmed.ncbi.nlm.nih.gov/32703794/) | CAMT-MPL: 56 patients | Causal gene, genotype-phenotype, onset | Human cohort |
| [11133753](https://pubmed.ncbi.nlm.nih.gov/11133753/) | c-mpl mutations cause CAMT | Causal gene; type I vs II | Human cohort |
| [19388932](https://pubmed.ncbi.nlm.nih.gov/19388932/) | Advances in CAMT | MPL LOF cause | Review |
| [17666371](https://pubmed.ncbi.nlm.nih.gov/17666371/) | 5 novel mutations | Elevated TPO, TNF-α/IFN-γ; no strict genotype correlation | Human series |
| [16351641](https://pubmed.ncbi.nlm.nih.gov/16351641/) | 20-patient series | Progression to pancytopenia, bleeding death | Human series |
| [39289521](https://pubmed.ncbi.nlm.nih.gov/39289521/) | EBMT HSCT outcomes | 85.6% 6-yr OS; graft failure | Human registry |
| [26369627](https://pubmed.ncbi.nlm.nih.gov/26369627/) | UCB transplant | Durable engraftment | Human series |
| [9831170](https://pubmed.ncbi.nlm.nih.gov/9831170/) | TPO and its receptor | JAK2/STAT5, MAPK | Review |
| [37633268](https://pubmed.ncbi.nlm.nih.gov/37633268/) | TPO-MPL structure | LOF structural rationale | Structural |
| [40766813](https://pubmed.ncbi.nlm.nih.gov/40766813/) | MPL activation structure | JAK2 dimerization, LOF mutations | Structural |
| [10582337](https://pubmed.ncbi.nlm.nih.gov/10582337/) | Mpl gene targeting | Mouse thrombocytopenia, no aplasia | Mouse |
| [12799278](https://pubmed.ncbi.nlm.nih.gov/12799278/) | TPO essential for hematopoiesis | Human aplasia vs mouse | Human/mouse |
| [41895275](https://pubmed.ncbi.nlm.nih.gov/41895275/) | THPO neonatal hierarchy | HSC anti-apoptosis/quiescence | Mouse |
| [34248130](https://pubmed.ncbi.nlm.nih.gov/34248130/) | THPO mitochondria | HSC metabolism/quiescence | Mouse/review |
| [33837181](https://pubmed.ncbi.nlm.nih.gov/33837181/) | Galectin-3 quiescence | MPL→Gal-3→quiescence | Mouse |
| [23908116](https://pubmed.ncbi.nlm.nih.gov/23908116/) | CAMT iPSCs | Human model; FLI1 | Human iPSC |
| [30573048](https://pubmed.ncbi.nlm.nih.gov/30573048/) | BMF predisposition | MDS/AML risk | Review |
| [22102270](https://pubmed.ncbi.nlm.nih.gov/22102270/) | CAMT clinical review | Rarity (96 patients) | Review |
| [34404532](https://pubmed.ncbi.nlm.nih.gov/34404532/) | CAMT not a single disease | Differential diagnosis | Review |
| [41766040](https://pubmed.ncbi.nlm.nih.gov/41766040/) | GFI1B / IT review | >50-gene differential | Review |
| [41359897](https://pubmed.ncbi.nlm.nih.gov/41359897/) | GNE thrombocytopenia | Genotype-unpredictable agonist response | Case/review |
| [20188141](https://pubmed.ncbi.nlm.nih.gov/20188141/) | F104S c-Mpl agonist | Agonist mostly ineffective; rare exceptions | In vitro |
| [19844195](https://pubmed.ncbi.nlm.nih.gov/19844195/) | Gene therapy of MPL | Leukemia/pancytopenia balance | Mouse |
| [41635268](https://pubmed.ncbi.nlm.nih.gov/41635268/) | RUSAT-2 (MECOM) | Differential diagnosis | Review |
| [21162090](https://pubmed.ncbi.nlm.nih.gov/21162090/) | Novel nonsense mutation | Variant nomenclature examples | Case report |
| [23625800](https://pubmed.ncbi.nlm.nih.gov/23625800/) | Pancytopenia in first month | Early progression, splice variant | Case report |
| [31306780](https://pubmed.ncbi.nlm.nih.gov/31306780/) | SAMD9/SAMD9L HCT | Differential diagnosis | Human series |

---

## Limitations and Knowledge Gaps

1. **Small cohorts.** The largest studies are 56 (clinical) and 66 (transplant) patients; epidemiology, penetrance, and expressivity estimates carry wide uncertainty.
2. **Imperfect genotype-phenotype correlation.** Type I vs II predicts trend but not individual course; no validated human modifier genes explain residual variability.
3. **Species discordance.** Mouse knockouts do not model the human aplastic-anemia progression, so mechanistic claims for Branch B (HSC exhaustion) rest largely on mouse THPO biology plus human iPSC inference rather than in vivo human proof.
4. **TPO-clearance step partly inferred.** The elevated-TPO mechanism is consistent with MPL biology but is inferred rather than directly demonstrated in CAMT patients in the reviewed literature.
5. **Therapeutic gap.** No approved pharmacologic alternative to HSCT; gene therapy remains experimental and constrained by the narrow therapeutic window between correction and myeloproliferation.
6. **MDS/AML risk unquantified.** Transformation risk is recognized as a class property of IBMFS but is not precisely quantified for MPL-CAMT specifically.

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry** with systematic serum-TPO, marrow-cellularity, and clonal-cytogenetic data to quantify progression timing by allele class and MDS/AML incidence.
2. **iPSC-based FLI1 mechanistic dissection** — rescue/overexpression experiments to test whether restoring FLI1 balance corrects the MEP defect, and whether this is tractable pharmacologically.
3. **Optimized MPL gene/base-editing therapy** using endogenous-promoter or safe-harbor strategies to achieve physiologic receptor levels and avoid the leukemogenesis seen with retroviral overexpression ([PMID: 19844195](https://pubmed.ncbi.nlm.nih.gov/19844195/)).
4. **Allele-specific agonist screening** to systematically identify which rare type-II MPL alleles can be rescued by transmembrane- vs extracellular-domain-targeting agonists (extending [PMID: 20188141](https://pubmed.ncbi.nlm.nih.gov/20188141/)).
5. **Humanized / xenograft models** (CAMT iPSC-derived HSPCs engrafted into immunodeficient mice) to recreate the human aplastic-anemia progression that conventional knockouts miss.
6. **Prospective transplant-timing study** to define the optimal window balancing marrow exhaustion/clonal evolution against transplant-related mortality and graft failure.

---

*Report compiled from 10 confirmed findings and 40 reviewed papers over 5 investigation iterations. Evidence types are labeled throughout as human clinical, human registry, mouse, in vitro/iPSC, structural, or review. All mechanistic and clinical claims are cited to primary literature (PMID); causal-chain steps are explicitly marked as demonstrated or inferred.*


## Artifacts

- [OpenScientist final report](Congenital_Amegakaryocytic_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Amegakaryocytic_Thrombocytopenia_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001873` (2 mentions) - the report calls it "Laboratory / clinical"; HP calls it **Thrombocytopenia**
- `HP:0001876` (1 mention) - the report calls it "Laboratory"; HP calls it **Pancytopenia**
- `HP:0002170` (1 mention) - the report calls it "Clinical sign"; HP calls it **Intracranial hemorrhage**
- `HP:0001627` (1 mention) - the report calls it "Physical malformation"; HP calls it **Abnormal heart morphology**
- `HP:0001507` (1 mention) - the report calls it "Physical"; HP calls it **Growth abnormality**
- `HP:0001263` (1 mention) - the report calls it "Behavioral/neuro"; HP calls it **Global developmental delay**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004811` (1 mention), reported as "reduced megakaryocytes" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002371` (1 mention) - the report calls it "Primary organ:** Bone marrow"; UBERON calls it **bone marrow**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.