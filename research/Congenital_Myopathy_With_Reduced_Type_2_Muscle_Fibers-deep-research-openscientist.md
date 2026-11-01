---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T19:51:57.007075'
end_time: '2026-10-31T20:08:44.882142'
duration_seconds: 1007.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Myopathy With Reduced Type 2 Muscle Fibers
  mondo_id: MONDO:0034109
  category: Mendelian
  causal_genes: MYL1
  omim_id: OMIM:618414
  synonyms: myopathy, congenital, with fast-twitch (type II) fiber atrophy; myopathy,
    congenital, with fast-twitch (type II) fibre atrophy
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
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 7
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:41568526
  relevance_assessed: 8
  on_topic: 5
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 5
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0003324
    reported_labels:
    - clinical sign
    ontology_label: Generalized muscle weakness
  - term_id: HP:0011968
    reported_labels:
    - symptom
    ontology_label: Feeding difficulties
  - term_id: HP:0001999
    reported_labels:
    - physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0001558
    reported_labels:
    - symptom
    ontology_label: Decreased fetal movement
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_Myopathy_With_Reduced_Type_2_Muscle_Fibers-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Myopathy_With_Reduced_Type_2_Muscle_Fibers-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myopathy With Reduced Type 2 Muscle Fibers
- **MONDO ID:** MONDO:0034109 (if available)
- **Causal gene(s):** MYL1
- **OMIM:** OMIM:618414
- **Synonyms:** myopathy, congenital, with fast-twitch (type II) fiber atrophy; myopathy, congenital, with fast-twitch (type II) fibre atrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Myopathy With Reduced Type 2 Muscle Fibers** covering all of the
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

# Congenital Myopathy With Reduced Type 2 Muscle Fibers (CMYO14 / MYL1-related congenital myopathy)

**MONDO:0034109 · OMIM:618414 · Causal gene: _MYL1_ (HGNC:7582)**

---

## Summary (Answer to the Research Question)

Congenital myopathy with reduced type 2 muscle fibers — formally **congenital myopathy‑14 (CMYO14)** — is an **ultra‑rare, autosomal‑recessive, severe neonatal‑onset skeletal muscle disease caused by biallelic loss‑of‑function variants in _MYL1_**, the gene encoding the **fast‑twitch (type II) skeletal‑muscle myosin essential/alkali light chain (ELC; isoforms MLC1F/MLC3F)**. Loss of functional fast ELC destabilizes the myosin motor specifically in type II fibers, producing arrested fast‑fiber development/maturation with marked **type II fiber hypotrophy or absence** on muscle biopsy, while type I (slow) fibers — which use a different ELC, MYL3 — are relatively spared. Clinically this manifests as profound **congenital hypotonia, generalized weakness, respiratory insufficiency, and feeding difficulty**, and the disorder has a severe prognosis. Fewer than ~6 patients have been reported worldwide (first described by Ravenscroft et al. 2018, PMID 30215711).

This report was assembled from **disease‑level aggregated resources (OMIM, gnomAD, NCBI Gene/HomoloGene, HGNC/UniProt/Ensembl)** and from the **small set of primary case reports** that constitute the entire human literature; it is not derived from EHR cohorts (no registry exists for such a rare disease).

---

## 1. Disease Information

- **What it is:** A congenital myopathy defined molecularly by MYL1 deficiency and histologically by selective smallness/atrophy or absence of fast‑twitch (type II) myofibres. "Congenital myopathies are typically characterised by early onset hypotonia, weakness and hallmark features on biopsy" (Ravenscroft 2018, PMID 30215711).
- **Key identifiers:**
  - **MONDO:** MONDO:0034109
  - **OMIM phenotype:** 618414 (Myopathy, congenital, 14; CMYO14)
  - **OMIM gene:** _MYL1_ 160780
  - **Mondo synonyms / OMIM title:** "Myopathy, congenital, with fast‑twitch (type II) fiber atrophy" / "…fibre atrophy"
  - **Orphanet:** Listed under congenital myopathies; no separate large epidemiology entry (ultra‑rare).
  - **ICD‑11:** 8C70 (Primary disorders of muscles / congenital myopathy) — approximate mapping; **ICD‑10:** G71.2 (congenital myopathies).
  - **MeSH:** "Myopathies, Structural, Congenital" (D020914); gene MeSH "Myosin Light Chains."
  - **Gene identifiers:** HGNC:7582; NCBI Gene 4632; Ensembl ENSG00000168530; UniProt **P05976**; locus **2q34**.
- **Synonyms/aliases:** CMYO14, CMYP14, MYL1‑related congenital myopathy, myopathy with fast‑twitch type II fiber atrophy; gene aliases MLC1F, MLC3F, MLC1/3, MYOFTA.
- **Source type:** Disease‑level/aggregated + individual case reports (not EHR).

*Ontology:* MONDO:0034109.

---

## 2. Etiology

- **Primary cause — genetic:** Biallelic (homozygous or compound‑heterozygous) **loss‑of‑function variants in _MYL1_**. "We identified variants in the gene (MYL1) encoding the skeletal muscle fast‑twitch specific myosin essential light chain (ELC) in both probands" (Ravenscroft 2018, PMID 30215711). It is a monogenic Mendelian disorder; no environmental or infectious cause.
- **Genetic risk factors:** The only risk factor is inheriting two pathogenic _MYL1_ alleles. **Consanguinity** is a major contributor (multiple reported families are consanguineous; homozygous variants). No susceptibility loci or GWAS associations (too rare).
- **Environmental risk factors:** None known. Not toxin/lifestyle/occupation‑related.
- **Protective factors:** A **single functional _MYL1_ allele is fully protective** — carriers are asymptomatic (see gnomAD constraint, §9). No dietary/lifestyle protective factors are relevant.
- **Gene–environment interactions:** None documented; disease is fully genetically determined.

---

## 3. Phenotypes

All features have **congenital/neonatal onset** and are **severe**; course is early and often life‑threatening. Frequencies are qualitative given ≤6 patients.

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Severe generalized hypotonia ("floppy infant") | clinical sign | HP:0001290 (neonatal hypotonia HP:0001319) | Congenital; severe; ~all patients |
| Generalized muscle weakness | clinical sign | HP:0003324 | Congenital; severe; ~all |
| Respiratory insufficiency / ventilator dependence | clinical sign | HP:0002093 / HP:0004887 | Neonatal; severe; most patients |
| Feeding difficulties / need for nutritional support | symptom | HP:0011968 | Neonatal; severe; most |
| Facial weakness / myopathic facies | clinical sign | HP:0010628 / HP:0000338 | Congenital; variable |
| Skeletal anomalies / contractures (incl. arthrogryposis‑like) | physical | HP:0002804 / HP:0001371 | Congenital; variable |
| Craniofacial/dysmorphic anomalies | physical | HP:0001999 | Reported in newest case (Barington 2026, PMID 41568526) |
| Reduced fetal movement / antenatal onset | symptom | HP:0001558 | Prenatal in some |
| Type II (fast) fiber hypotrophy/atrophy/absence on biopsy | laboratory/pathology | HP:0003554 (type II muscle fiber atrophy) | Universal defining feature |

Key quotes: "Both individuals showed a very severe congenital myopathy, characterised by congenital hypotonia and weakness, requiring ventilatory and nutritional assistance" (Madrigal/Natera‑de Benito 2025, PMID 40488356); "a neonate with severe hypotonia, respiratory insufficiency, and skeletal anomalies… the patient presented with craniofacial anomalies not previously described" (Barington 2026, PMID 41568526).

**Quality of life:** Profound — affected neonates typically require respiratory support (invasive/non‑invasive ventilation) and tube feeding, with major impairment of all gross motor function. Formal QoL instruments (EQ‑5D/PROMIS) have not been applied given rarity and age.

---

## 4. Genetic / Molecular Information

- **Causal gene:** _MYL1_ (myosin light chain 1), OMIM 160780, HGNC:7582, locus **2q34**, Ensembl ENSG00000168530, UniProt **P05976**. Encodes the **non‑phosphorylatable alkali/essential light chain of fast skeletal muscle myosin**; "This gene encodes a myosin alkali light chain expressed in fast skeletal muscle. Two transcript variants have been identified" (NCBI RefSeq). The two isoforms **MLC1F and MLC3F** arise by alternative promoter/splicing and are **type II–fiber specific**.
- **Pathogenic variants reported (all germline, biallelic):**
  - **c.479‑2A>G** — essential splice‑acceptor, predicted exon‑5 skipping (homozygous, Proband 1; Ravenscroft 2018, PMID 30215711) — **Pathogenic**.
  - **c.488T>G, p.(Met163Arg)** — missense, predicted to impair binding to the IQ domain of myosin heavy chain and to destabilize the protein (homozygous, Proband 2; PMID 30215711) — **Pathogenic/Likely pathogenic**.
  - **Three further novel variants** across two individuals (Madrigal/Natera‑de Benito 2025, PMID 40488356).
  - **c.479‑25T>C** — deep‑intronic splice variant; RNA from patient muscle showed inclusion of 19 bp of intron 4 → frameshift/premature stop in most transcripts, plus in‑frame exon 4–5 skipping in a minority (homozygous; Barington 2026, PMID 41568526).
  - **Variant classes:** splice‑site, missense, and deep‑intronic splice‑altering. No recurrent/founder allele; all private.
  - **Allele frequency:** All pathogenic alleles are absent/ultra‑rare in gnomAD. General MYL1 LoF is **tolerated** in population (obs 16 vs exp 21.8 LoF; see §9).
  - **Functional consequence:** **Loss of function** (null/unstable protein) — "MYL1 was markedly reduced in skeletal muscle from both probands, suggesting that the missense substitution likely results in an unstable protein" (PMID 30215711). Not gain‑of‑function or dominant‑negative.
- **Modifier genes:** None identified. (Hypothetically, expression of other fast ELC/regulatory light chains could modulate severity, but this is unproven.)
- **Epigenetics:** No disease‑specific DNA‑methylation/histone findings reported.
- **Chromosomal abnormalities:** None — point/splice variants only; no CNV/structural etiology reported.

*Ontology/annotation:* HGNC:7582; UniProt P05976; GO molecular function "structural constituent of muscle" (GO:0008307), "myosin light chain binding."

---

## 5. Environmental Information

- **Environmental factors:** None. Purely genetic Mendelian disorder.
- **Lifestyle factors:** Not applicable.
- **Infectious agents:** None (not infectious or immune‑mediated).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic _MYL1_ loss‑of‑function variant** (splice/missense/deep‑intronic) **results in** aberrant/absent _MYL1_ mRNA (e.g., exon skipping, frameshift + premature stop) — *demonstrated by patient RNA studies* (PMID 41568526).
2. This **leads to** absent or unstable **fast‑skeletal essential/alkali light chain (MLC1F/MLC3F)** protein — *demonstrated by markedly reduced MYL1 on Western blot of patient muscle* (PMID 30215711).
3. Loss of ELC **results in** a **destabilized myosin lever arm/neck** and impaired heavy‑chain–light‑chain coupling in **type II (fast) fibers** — *inferred from in‑vitro motility: removing myosin light chains reduces actin sliding velocity ~11‑fold (8.8→0.8 µm/s) without reducing ATPase* (Lowey 1993, PMID 8413589).
4. This **leads to** **impaired force transduction and defective fast‑twitch myofibre development/maturation** (type II fibers remain small and retain **developmental myosin**) — *demonstrated histologically* (PMID 40488356).
5. The branch point: **type I (slow) fibers are relatively spared** because they use a **different ELC gene (MYL3)**; they remain normal‑to‑hypertrophic, producing the **"floret" pattern** (small type II fibers clustered around larger type I fibers) (PMID 40488356).
6. Fiber‑level dysfunction **results in** **generalized weakness and hypotonia**, affecting respiratory and bulbar musculature → **respiratory insufficiency and feeding difficulty** — *the clinical endpoint* (PMID 30215711, 40488356, 41568526).
7. In vivo validation: **zebrafish myl1 knockdown results in** disrupted muscle structure and impaired touch‑evoked (fast‑twitch–dependent) escape responses, confirming the chain (PMID 30215711).

### Mechanistic detail by category

- **Molecular pathways / biochemical process:** Actin–myosin cross‑bridge cycling and the sarcomeric contractile apparatus (Reactome "Striated Muscle Contraction," R‑HSA‑390522). The defect is structural‑contractile, **not** a classic signaling cascade (no Wnt/MAPK/mTOR involvement implicated).
- **Protein dysfunction:** Loss of function via protein instability/absence; the missense p.Met163Arg is predicted to "impede intermolecular interactions that facilitate binding to the IQ domain of myosin heavy chain, thus likely impacting on the structure and functioning of the myosin motor" (PMID 30215711).
- **Cellular processes:** Arrested fast‑fiber differentiation/maturation (persistent developmental/neonatal myosin); dystrophic‑like/myopathic changes on biopsy, but **not** a primary apoptotic/inflammatory/autophagic disease.
- **Metabolic changes:** None primary (not a metabolic myopathy).
- **Immune involvement:** None.
- **Tissue damage:** Secondary dystrophic‑like change without primary necrosis/fibrosis as the driver.
- **Molecular profiling:** Patient‑muscle **RNA analysis** (splicing), **Western blot** (protein loss), **immunohistochemistry/immunofluorescence/EM** (fiber typing, developmental myosin, ultrastructure) (PMID 40488356, 41568526). No large transcriptomic/proteomic/metabolomic datasets exist.

*Ontology:* GO biological process — skeletal muscle contraction (GO:0003009), myofibril assembly (GO:0030239), muscle filament sliding (GO:0030049), skeletal muscle fiber development (GO:0048741); GO cellular component — myosin complex (GO:0016459), myofibril (GO:0030016), sarcomere/A band. CL — fast muscle cell (CL:0000190), skeletal muscle fiber (CL:0008002).

---

## 7. Anatomical Structures Affected

- **Organ level:** **Skeletal muscle** is the primary affected organ (UBERON:0001134). Secondary/system involvement: **respiratory system** (ventilatory failure from weak respiratory/diaphragmatic muscles, UBERON:0001004), **digestive/feeding** (bulbar weakness → dysphagia), **skeletal system** (contractures, craniofacial/skeletal anomalies). **No primary cardiac involvement** is characteristic (cardiac myosin uses MYL3/MYL4, not MYL1), and brain/CNS structure is intrinsically normal (weakness is myopathic, not neurogenic).
- **Tissue/cell level:** **Striated (skeletal) muscle tissue**; the targeted population is the **fast‑twitch type II skeletal muscle fiber** (CL:0000190 fast muscle cell). Type I/slow fibers (CL:0000189) are relatively spared.
- **Subcellular level:** **Sarcomere/myofibril** — specifically the **myosin thick filament / myosin complex** (GO:0016459) at the head–neck (lever‑arm) region; **A‑band**. No primary mitochondrial, nuclear, ER, or lysosomal pathology.
- **Localization / lateralization:** **Generalized and bilateral/symmetric**, affecting axial, limb, respiratory, facial and bulbar muscles.

*Ontology:* UBERON:0001134 (skeletal muscle tissue), UBERON:0001103 (diaphragm), UBERON:0001004 (respiratory system).

---

## 8. Temporal Development

- **Onset:** **Congenital** — antenatal (reduced fetal movements in some) to **neonatal**; onset pattern is **present‑at‑birth/early**, not acute‑episodic.
- **Progression:** The myopathy itself is best characterized as **early‑severe and largely static‑to‑slowly‑evolving** (a congenital myopathy rather than a relentlessly degenerative dystrophy), but the **clinical course is dominated by severe early respiratory/feeding compromise**; too few long‑surviving patients exist to define a late natural history. Duration: **chronic/lifelong**.
- **Patterns:** No remission. **Critical period = neonatal/infantile**, where respiratory and nutritional support is decisive for survival.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** "CMYO14… an ultrarare autosomal recessive disorder caused by biallelic variants in MYL1" (Barington 2026, PMID 41568526).
- **Penetrance:** Complete in biallelic carriers (all reported biallelic individuals affected); **heterozygotes unaffected**.
- **Expressivity:** Uniformly severe to date, with some phenotypic expansion (craniofacial anomalies).
- **Anticipation:** Not applicable (not a repeat‑expansion disorder).
- **Germline mosaicism / founder effect:** None reported; all variants private; several **consanguineous** pedigrees → homozygosity.
- **gnomAD constraint (computational):** pLI = 7.2×10⁻⁵; **oe_lof = 0.735 (90% CI 0.498–1.117)**; obs_lof = 16 vs exp 21.8 → **MYL1 is NOT loss‑of‑function‑intolerant / not haploinsufficient**, consistent with recessive inheritance and asymptomatic carriers.
- **Carrier frequency:** Not formally established; expected low given private alleles (higher within consanguineous communities).
- **Epidemiology:** **Ultra‑rare — ≤6 patients reported worldwide (2018–2026).** True prevalence/incidence are unknown (likely <1 per million). No sex predilection; reported in consanguineous families of varied ancestry.

*Ontology/inheritance:* HP:0000007 (autosomal recessive inheritance).

---

## 10. Diagnostics

- **Laboratory:** Serum **creatine kinase** may be normal or mildly elevated (as in most congenital myopathies); no specific blood biomarker. No specific metabolite/enzyme assay.
- **Electrophysiology:** EMG typically shows a **myopathic pattern**; nerve conduction normal (distinguishes from neurogenic floppy infant, e.g., SMA).
- **Imaging:** Muscle MRI/ultrasound can show myopathic change (nonspecific); no pathognomonic pattern reported for this ultra‑rare entity.
- **Muscle biopsy (key):** Dystrophic‑like/myopathic changes with **hypotrophy/atrophy or absence of type II (fast) fibers**; small fibers arranged around larger type I fibers in a **"floret" pattern**; **persistent developmental myosin** expression; EM shows aberrant myofibrillar features. ATPase/myosin‑isoform immunohistochemistry demonstrates the fiber‑type disproportion; **Western blot shows markedly reduced MYL1 protein** (PMID 30215711, 40488356).
- **Genetic testing (confirmatory):** **WES or WGS**, or a **congenital myopathy next‑generation‑sequencing gene panel** that includes _MYL1_, is the diagnostic approach of choice — "massive parallel sequencing" underlies modern diagnosis (PMID 40488356). **WGS and RNA/functional studies are specifically valuable for deep‑intronic/splice variants** that WES or panels may miss — "underscores the diagnostic importance of intron variants, highlighting the value of combining in silico splice prediction with functional RNA analyses" (PMID 41568526). Single‑gene _MYL1_ testing is appropriate once biopsy points to type II fiber deficiency. CMA/karyotype/FISH/mtDNA/repeat testing are **not** indicated.
- **Clinical criteria / differential diagnosis:** No formal diagnostic criteria; diagnosis = clinical congenital myopathy + type II fiber deficiency on biopsy + biallelic _MYL1_ variants. **Differential diagnosis:** other causes of the floppy infant — **SMA (SMN1)**; other congenital myopathies (nemaline/_ACTA1_, core/_RYR1_, centronuclear/_MTM1,DNM2,BIN1_); **congenital fiber‑type disproportion** (classically **type I** fiber smallness — the mirror image of MYL1's type II smallness; PMID 26526626); congenital muscular dystrophies; metabolic/mitochondrial myopathies; congenital myasthenic syndromes. Biopsy fiber‑typing plus genetics distinguish these (floppy‑infant work‑up: PMID 23743156).
- **Screening:** Not on newborn‑screening panels; **cascade carrier testing** of relatives and **carrier screening** in consanguineous families once a familial variant is known.

*Ontology/LOINC:* CK (LOINC 2157‑6); genetic testing NCIT.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Severe prognosis.** Reported patients have profound neonatal weakness with **ventilator and nutritional dependence**; given the very small, recent cohort, formal survival statistics are unavailable, but the phenotype is life‑threatening in infancy. No 5‑/10‑year figures exist.
- **Morbidity/function:** Severe motor disability; dependence on respiratory and feeding support; major impact on all developmental milestones.
- **Complications:** **Respiratory failure and respiratory infections**, aspiration, failure to thrive, orthopedic complications (contractures, scoliosis) — typical of severe congenital myopathy.
- **Recovery potential:** No cure; supportive care can stabilize but not reverse. Congenital myopathies in general are static‑to‑slowly‑progressive, so some patients who survive the neonatal period may achieve relative stability, but evidence is limited for MYL1.
- **Prognostic factors:** Degree of respiratory involvement and severity of the null genotype are the main determinants; no validated prognostic biomarker.

---

## 12. Treatment

**No disease‑specific or curative therapy exists.** Management is **supportive/multidisciplinary**, as for severe congenital myopathies:

- **Pharmacotherapy:** None disease‑specific. No approved drug; no pharmacogenomic guidance. (General congenital‑myopathy care avoids depolarizing agents where malignant‑hyperthermia risk is a concern, but MH is a _RYR1_ issue, not established for MYL1.)
- **Respiratory support (cornerstone):** Non‑invasive or invasive **mechanical ventilation**, airway clearance (NCIT: Mechanical Ventilation C70909).
- **Nutritional support:** **Nasogastric/gastrostomy feeding** for bulbar weakness/failure to thrive (NCIT: Enteral Nutrition/Gastrostomy).
- **Rehabilitation:** **Physical therapy, occupational therapy, speech therapy**; contracture prevention (stretching/orthoses) (NCIT: Physical Therapy C15327, Occupational Therapy, Speech Therapy).
- **Surgical/orthopedic:** Management of contractures and **scoliosis** as needed.
- **Advanced therapeutics (experimental/none approved):** No gene therapy, ASO, cell therapy, or targeted therapy exists or is in trial for MYL1 specifically. Conceptually, because the mechanism is **recessive loss‑of‑function**, **gene replacement/augmentation** (e.g., AAV‑delivered MYL1) or **splice‑modulating ASOs** (for the intronic splice alleles) are rational future directions, but remain hypothetical. The zebrafish model provides a platform for preclinical testing (PMID 30215711).
- **Treatment outcomes:** Supportive care improves survival/comfort but does not alter the underlying deficit; no response‑rate data.
- **Strategy:** Genotype‑guided counseling; multidisciplinary neuromuscular care pathway.

---

## 13. Prevention

- **Primary prevention:** Not applicable to disease occurrence beyond reproductive genetics. **Genetic counseling** for carrier couples (25% recurrence risk per pregnancy).
- **Secondary prevention:** Early recognition of the floppy infant and prompt respiratory/nutritional support; no population screening.
- **Tertiary prevention:** Prevent complications — respiratory surveillance/immunizations against respiratory pathogens (e.g., influenza, RSV prophylaxis, pneumococcus) in the medically fragile infant; aspiration precautions; contracture/scoliosis prevention.
- **Genetic/reproductive options:** **Carrier (cascade) testing**, **prenatal diagnosis**, and **preimplantation genetic testing (PGT‑M)** are available for families with a known biallelic genotype. Especially relevant in **consanguineous** families.
- **Immunization/public‑health/environmental:** No disease‑specific vaccine or environmental intervention (not infectious/environmental).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (HomoloGene group 23194):** _MYL1_ is highly conserved — **mouse _Myl1_** (NCBI Gene 17901; NCBITaxon:10090), **rat _Myl1_** (56781), **zebrafish _myl1_** (58143; NCBITaxon:7955), **chicken** (396470), **cattle** (317657), **dog** (478896), **frog** (394551). In mouse, _Myl1_ is a canonical **fast‑fiber marker** (expressed alongside Myh3/Myh8/Mylpf; Amann 2014, PMID 25172430).
- **Natural disease in animals:** **None documented** — no entry in OMIA for naturally occurring MYL1 myopathy; no companion‑animal/wildlife counterpart or specific affected breed (no VBO breed). **No zoonotic potential / cross‑species transmission** (genetic disorder).
- **Comparative biology:** Strong evolutionary conservation of fast‑fiber ELC function supports translational validity of models; fiber‑type specificity (fast ELC = MYL1; slow/cardiac ELC = MYL3) is conserved across vertebrates.

---

## 15. Model Organisms

- **Validated model — zebrafish (_Danio rerio_, NCBITaxon:7955):** Morpholino **_myl1_ knockdown** produced "abnormal morphology, disrupted muscle structure and impaired touch‑evoked escape responses, thus confirming that skeletal muscle fast‑twitch specific myosin ELC is critical for myofibre development and function" (Ravenscroft 2018, PMID 30215711). The touch‑evoked escape readout is **fast‑twitch dependent**, directly mirroring the human type II deficit — **good phenotype recapitulation** of the muscle‑structural and fast‑fiber‑function phenotype. (Resource: ZFIN.)
- **Mammalian models:** **No dedicated _Myl1_‑knockout mouse myopathy model** has been reported for this disease (gap); mouse _Myl1_ is used mainly as a fast‑fiber expression marker. IMPC/MGI (Gene MGI for _Myl1_) could host future alleles. **Limitation:** absence of a mammalian model limits preclinical therapeutic testing; morpholino knockdown has known transient/off‑target caveats.
- **In vitro / cellular:** No established patient iPSC‑myotube or immortalized line is reported specifically, though patient muscle (histology, Western blot, EM, RNA) has been studied directly (PMID 40488356, 41568526).
- **Applications:** Models are suited to studying fast‑fiber myofibrillogenesis, ELC–myosin lever‑arm mechanics, and (prospectively) gene‑replacement or splice‑correction therapy.

---

## Supported vs Refuted Hypotheses

**Supported:**
- Biallelic _MYL1_ LoF causes CMYO14 (human genetics + zebrafish; PMID 30215711).
- The disease selectively affects **type II/fast fibers** because MYL1 is the fast‑fiber‑specific ELC, while type I fibers use MYL3 (histology + gene biology; PMID 40488356).
- Mechanism is **loss of function** (unstable/absent protein), with ELC required for normal myosin shortening velocity (PMID 8413589, 30215711).
- Strictly **autosomal recessive** with asymptomatic carriers (gnomAD constraint; PMID 41568526).
- Deep‑intronic splice variants expand the mutational spectrum and require RNA/WGS diagnostics (PMID 41568526).

**Refuted / not supported:**
- Not haploinsufficient/dominant (gnomAD pLI≈0; carriers unaffected).
- Not a metabolic, inflammatory, mitochondrial, or primary cardiac disease.
- No environmental/infectious etiology; no founder effect established.

---

## Limitations and Future Directions

- **Tiny evidence base:** ≤6 patients; frequencies, natural history, and survival are estimates, not statistics.
- **No mammalian genetic model** and **no clinical trials/therapies** — gene‑replacement and splice‑modulating ASO strategies are rational but untested.
- **Unknowns:** long‑term prognosis in survivors; existence of milder/later‑onset phenotypes; modifier genes; precise fraction of cardiac/respiratory muscle MYL1 dependence.
- **Priorities:** generate a conditional/null mouse or stable zebrafish mutant; patient iPSC‑myotube models; registry/natural‑history collection; evaluate AAV‑MYL1 and ASO splice correction.

---

### Key references
- Ravenscroft G, et al. *Bi‑allelic mutations in MYL1 cause a severe congenital myopathy.* Hum Mol Genet / J Med Genet 2018. **PMID 30215711**.
- Madrigal/Natera‑de Benito D, et al. *MYL1‑Related Congenital Myopathy: Clinical, Genetic and Pathological Insights.* 2025. **PMID 40488356**.
- Barington M, et al. *Novel MYL1 Intron Variant With Expanded Phenotype.* 2026. **PMID 41568526**.
- Lowey S, Waller GS, Trybus KM. *Skeletal muscle myosin light chains are essential for physiological speeds of shortening.* Nature 1993. **PMID 8413589**.
- Sitbon YH, et al. *Insights into myosin regulatory and essential light chains…* 2020 (review). **PMID 31131433**.
- Amann R, et al. (fast‑fiber marker _Myl1_ in mouse) 2014. **PMID 25172430**.
- Kissiedu J, Prayson RA. *Congenital fiber type disproportion.* 2016 (differential). **PMID 26526626**.
- Gene/constraint resources: NCBI Gene 4632; gnomAD (MYL1 constraint); HGNC:7582; UniProt P05976.


## Artifacts

- [OpenScientist final report](Congenital_Myopathy_With_Reduced_Type_2_Muscle_Fibers-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Myopathy_With_Reduced_Type_2_Muscle_Fibers-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41568526` *(abstract only)*: "a neonate with severe hypotonia, respiratory insufficiency, and skeletal anomalies… the patient presented with craniofacial anomalies not previously described"
  - closest text in source: "We describe what is likely the fifth reported patient, a neonate with severe hypotonia, respiratory insufficiency, and skeletal anomalies showing distinct histological changes of skeletal muscle consistent with all previously described patients"
- `PMID:41568526` *(abstract only)*: "CMYO14… an ultrarare autosomal recessive disorder caused by biallelic variants in MYL1"
  - closest text in source: "Congenital myopathy-14 (CMYO14) is an ultrarare autosomal recessive disorder caused by biallelic variants in MYL1, with only four patients reported to date"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003324` (1 mention) - the report calls it "clinical sign"; HP calls it **Generalized muscle weakness**
- `HP:0011968` (1 mention) - the report calls it "symptom"; HP calls it **Feeding difficulties**
- `HP:0001999` (1 mention) - the report calls it "physical"; HP calls it **Abnormal facial shape**
- `HP:0001558` (1 mention) - the report calls it "symptom"; HP calls it **Decreased fetal movement**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003554` (1 mention) - the report calls it "type II muscle fiber atrophy"; HP calls it **Type 2 muscle fiber atrophy**
- `GO:0016459` (2 mentions) - the report calls it "myosin thick filament / myosin complex"; GO calls it **myosin complex**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.