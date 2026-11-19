---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T14:00:17.204401'
end_time: '2026-10-31T14:20:37.451443'
duration_seconds: 1220.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Megalencephalic Leukoencephalopathy With Subcortical Cysts 2B
  mondo_id: MONDO:0013491
  category: Mendelian
  causal_genes: HEPACAM
  omim_id: OMIM:613926
  synonyms: megalencephalic leukoencephalopathy with subcortical cysts 2B, remitting,
    with or without mental retardation
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
citation_count: 19
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 18
  off_topic: 1
  off_topic_references:
  - PMID:42586097
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0000256
    reported_labels:
    - Physical sign
    ontology_label: Macrocephaly
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: HP:0001249
    reported_labels:
    - Cognitive
    ontology_label: Intellectual disability
  - term_id: HP:0000717
    reported_labels:
    - Behavioral
    ontology_label: Autism
  - term_id: HP:0001270
    reported_labels:
    - Clinical
    ontology_label: Motor delay
  labels_variant: 1
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
  path: Megalencephalic_Leukoencephalopathy_With_Subcortical_Cysts_2B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Megalencephalic_Leukoencephalopathy_With_Subcortical_Cysts_2B-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Megalencephalic Leukoencephalopathy With Subcortical Cysts 2B
- **MONDO ID:** MONDO:0013491 (if available)
- **Causal gene(s):** HEPACAM
- **OMIM:** OMIM:613926
- **Synonyms:** megalencephalic leukoencephalopathy with subcortical cysts 2B, remitting, with or without mental retardation
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Megalencephalic Leukoencephalopathy With Subcortical Cysts 2B** covering all of the
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

# Megalencephalic Leukoencephalopathy With Subcortical Cysts 2B (MLC2B)

**Disease:** Megalencephalic Leukoencephalopathy With Subcortical Cysts, type 2B (remitting, with or without intellectual disability)
**MONDO:** MONDO:0013491 · **OMIM:** 613926 · **Causal gene:** **HEPACAM** (encoding **GlialCAM / hepaCAM**, HGNC:17027) · **Category:** Mendelian (autosomal **dominant**)

---

## Summary

Megalencephalic leukoencephalopathy with subcortical cysts type 2B (**MLC2B**) is a rare, autosomal **dominant**, **remitting** leukoencephalopathy caused by a single heterozygous (usually missense) variant in **HEPACAM**, the gene encoding the astrocyte-enriched immunoglobulin-superfamily cell-adhesion molecule **GlialCAM** (also called hepaCAM). It sits within the "megalencephalic leukoencephalopathy with subcortical cysts" (MLC) disease family, which also comprises classic recessive **MLC1** (MLC1 gene) and recessive **MLC2A** (biallelic HEPACAM). HEPACAM variants account for roughly **25% of all MLC cases**; the dosage/zygosity of the HEPACAM lesion determines whether the course is the deteriorating classic phenotype (two mutations → MLC2A) or the improving/remitting phenotype (one dominant mutation → MLC2B) ([PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/)).

Mechanistically, GlialCAM is the obligatory trafficking partner of the astrocytic membrane protein **MLC1** and an **auxiliary (β) subunit of the ClC-2 chloride channel**, targeting the MLC1–ClC-2 complex to cell–cell junctions at perivascular astrocyte endfeet of the **gliovascular unit**. Dominant MLC2B mutations cluster in the first immunoglobulin (Ig) domain and perturb GlialCAM–GlialCAM self-interactions (cis/trans), acting in a **dominant-negative** manner to mislocalize the complex, disrupt astrocytic **volume-regulated anion channel (VRAC)** activity and ion/water homeostasis, and thereby produce chronic white-matter edema with intramyelinic vacuolation ([PMID: 22405205](https://pubmed.ncbi.nlm.nih.gov/22405205/); [PMID: 31960914](https://pubmed.ncbi.nlm.nih.gov/31960914/)). Because a single dominant allele causes only a partial, developmentally timed disturbance, the edema and MRI abnormalities characteristically **improve or normalize over time**, distinguishing MLC2B from the progressive recessive forms.

Clinically, MLC2B presents in infancy with **macrocephaly** and MRI white-matter edema ± subcortical cysts, but—unlike classic MLC—motor and cognitive function are typically preserved or only mildly affected, and imaging improves. The phenotypic spectrum ranges from **benign familial macrocephaly** (full normalization) to **macrocephaly with intellectual disability ± autism** ([PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/)). There is **no disease-modifying therapy**; management is supportive. This report synthesizes seven confirmed findings and 23 reviewed papers into a comprehensive, section-by-section knowledge-base entry.

---

## Key Findings

### Finding 1 — MLC2B is caused by a single dominant HEPACAM (GlialCAM) mutation and follows a remitting course

López-Hernández et al. (2011) identified HEPACAM/GlialCAM as a direct MLC1-binding partner and screened 40 MLC patients who lacked MLC1 mutations. Of these, **10 patients with the classical, deteriorating phenotype carried two HEPACAM mutations** (recessive **MLC2A**), whereas **18 patients with an improving phenotype carried a single mutation** (dominant **MLC2B**). Most parents carrying a single mutation themselves had macrocephaly, confirming **dominant inheritance with a milder, self-improving expression**. Overall, approximately **25% of MLC cases carry HEPACAM variants**.

> *"Ten patients with the classical, deteriorating phenotype had two mutations, and 18 patients with the improving phenotype had one mutation. Most parents with a single mutation had macrocephaly, indicating dominant inheritance."* — [PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/)

The OMIM designation, autosomal dominant inheritance, and remitting character are reaffirmed in the recent literature:

> *"megalencephalic leukoencephalopathy with subcortical cysts 2B (MLC2B, MIM# 613,926, autosomal dominant)"* — [PMID: 38280046](https://pubmed.ncbi.nlm.nih.gov/38280046/)

This establishes the central genotype–phenotype rule of the HEPACAM-linked MLC family: **allele dosage dictates course** — one dominant allele → remitting MLC2B; two alleles → progressive MLC2A.

### Finding 2 — GlialCAM is an auxiliary subunit of the ClC-2 chloride channel and of MLC1; mutations mislocalize the complex

Jeworutzki et al. (2012) demonstrated that GlialCAM physically binds the **ClC-2 chloride channel**, co-localizes with it in **Bergmann glia and perivascular astrocyte endfeet**, and **targets ClC-2 to cell–cell junctions**, where it increases ClC-2-mediated currents and alters the channel's gating. Crucially, disease-causing GLIALCAM mutations **abolish this junctional targeting**, which is the core molecular lesion shared across MLC2A and MLC2B.

> *"GlialCAM targets ClC-2 to cell junctions, increases ClC-2 mediated currents, and changes its functional properties. Disease-causing GLIALCAM mutations abolish the targeting of the channel to cell junctions."* — [PMID: 22405205](https://pubmed.ncbi.nlm.nih.gov/22405205/)

> *"the disruption of the Cl(-) channel ClC-2 causes fluid accumulation leading to myelin vacuolation"* — [PMID: 22405205](https://pubmed.ncbi.nlm.nih.gov/22405205/)

Arnedo et al. (2014) independently confirmed that GlialCAM acts as the auxiliary (β) subunit of **both MLC1 and ClC-2**. This defines GlialCAM as a molecular hub whose job is to assemble and correctly localize an astrocytic ion-homeostasis module; mislocalization of that module produces the fluid accumulation and myelin vacuolation that are the histopathological hallmarks of MLC.

### Finding 3 — Structural basis distinguishing dominant (MLC2B) from recessive (MLC2A) GLIALCAM mutations

Elorza-Vidal et al. (2020) built a structural model of GlialCAM homo-interactions and proposed a mechanistic explanation for why some HEPACAM mutations are dominant. **Dominant (MLC2B) mutations affect GlialCAM–GlialCAM interacting surfaces in the first immunoglobulin (Ig) domain**, which mediate self-association **in cis** (between GlialCAM molecules in the same cell) and **in trans** (between GlialCAM on neighbouring cells). Because GlialCAM self-associates, a mutant monomer can poison wild-type partners — the molecular definition of a **dominant-negative** effect — explaining dominant inheritance even though most pathogenic mutations (dominant or recessive) ultimately disrupt junctional targeting.

> *"we suggest that dominant mutations affect different GlialCAM-GlialCAM interacting surfaces in the first Ig domain, which can occur between GlialCAM molecules present in the same cell (cis) or present in neighbouring cells (trans)"* — [PMID: 31960914](https://pubmed.ncbi.nlm.nih.gov/31960914/)

This is directly supported by functional case data: a novel MLC2B mutation **p.Q56P** mislocalized GlialCAM and its partners yet still **activated ClC-2 like wild-type**, whereas a recessive MLC2A allele (p.R73W) showed no trafficking defect and no functional change — illustrating that the dominant/recessive distinction is encoded in *which* molecular surface is disturbed rather than simply the presence of a mutation ([PMID: 24202401](https://pubmed.ncbi.nlm.nih.gov/24202401/)).

### Finding 4 — Clinical phenotype: infantile macrocephaly with transient white-matter edema that improves over time

The defining clinical feature of MLC2B is **clinical and MRI improvement/normalization over time**, contrasting with the deterioration of classic/recessive MLC. The multi-institutional cross-sectional study by Hamilton et al. (2018; 204 classic MLC patients) established that clinical and MRI features alone do not distinguish subtypes at a single time point, but **course over time** does ([PMID: 29661901](https://pubmed.ncbi.nlm.nih.gov/29661901/)). López-Hernández (2011) delineated the MLC2B spectrum:

> *"In some families with dominant HEPACAM mutations, the clinical picture and magnetic resonance imaging normalized, indicating that HEPACAM mutations can cause benign familial macrocephaly. In other families with dominant HEPACAM mutations, patients had macrocephaly and mental retardation with or without autism."* — [PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/)

The remitting/improving white-matter course has been documented serially on MRI, including in HEPACAM-region deletion (Jacobsen syndrome) cases that mimic MLC2B remission:

> *"the WMA in the present patient improved over time. As with some of MLC2B patients, the WMA in the present patient improved over time."* — [PMID: 32507665](https://pubmed.ncbi.nlm.nih.gov/32507665/)

Resolution of MRI abnormalities over childhood has also been captured in teaching neuroimaging reports of MLC ([PMID: 24821940](https://pubmed.ncbi.nlm.nih.gov/24821940/)).

### Finding 5 — MLC converges on astrocytic VRAC dysfunction, with an emerging GPRC5B signaling node

Recent work places HEPACAM/GlialCAM within an astrocytic **volume-regulated anion channel (VRAC)** module. Kerst et al. (2026) state that genetic defects in astrocytic VRAC-modulating proteins (**MLC1, GlialCAM, Aquaporin-4, GPRC5B**) cause MLC, and disrupted VRAC activity in MLC-patient lymphoblasts and primary astrocytes supports this pathogenic link. Importantly, however, astrocyte-specific **Lrrc8a** (the pore-forming VRAC subunit) knockout **alone did not reproduce chronic edema**, refining — rather than contradicting — the model: VRAC loss is part of, but not sufficient for, the full MLC phenotype.

> *"Genetic defects in astrocytic VRAC modulating proteins (MLC1, GlialCAM, Aquaporin-4, GPRC5B) cause the leukodystrophy Megalencephalic leukoencephalopathy with subcortical cysts (MLC), characterized by chronic white matter edema and myelin vacuolization."* — [PMID: 41654199](https://pubmed.ncbi.nlm.nih.gov/41654199/)

> *"astrocyte specific Lrrc8a knockout mice had normal brain water content, no myelin vacuolization, and preserved expression of MLC-related proteins"* — [PMID: 41654199](https://pubmed.ncbi.nlm.nih.gov/41654199/)

A parallel biochemical line of evidence identifies the orphan G-protein-coupled receptor **GPRC5B** as a signaling node regulated by GlialCAM/MLC1, with dominant GPRC5B mutations found in MLC patients — introducing a **gain-of-function signaling** dimension downstream of the adhesion complex:

> *"GlialCAM and MLC1 may regulate cell signaling via GPRC5B"* — [PMID: 41314544](https://pubmed.ncbi.nlm.nih.gov/41314544/)

### Finding 6 — MLC is a developmental disorder of the gliovascular unit; dominant hepaCAM mutants mislocalize and rewire the astrocyte interactome

Gilbert et al. (2021) established that during postnatal development, MLC1 forms a membrane complex with GlialCAM at the **junctions between perivascular astrocytic processes**, which together with blood vessels constitute the **gliovascular unit** — framing MLC as a **developmental disorder of this unit**.

> *"MLC1 forms a membrane complex with GlialCAM (another astrocytic transmembrane protein) at the junctions between perivascular astrocytic processes. Perivascular astrocytic processes along with blood vessels form the gliovascular unit."* — [PMID: 34723793](https://pubmed.ncbi.nlm.nih.gov/34723793/)

Lewis et al. (2025/2026), studying three **dominant** pathogenic hepaCAM variants in the developing mouse cortex *in vivo*, found that mutant hepaCAM is **dramatically redistributed** throughout cortical astrocytes and **significantly rewires the protein interactome** — with **decreased association with Connexin 43 and ClC-2** (coupling/ion-handling partners) and a **novel interaction with the epilepsy-associated potassium channel KCNQ2**:

> *"We also observed significant changes in protein interactome between wild type and mutant hepaCAM, including decreased association with previously described hepaCAM-interacting proteins Connexin 43 and CLC-2. Moreover, we identified the epilepsy-associate potassium channel KCNQ2 as a novel hepaCAM interaction partner"* — [PMID: 42649352](https://pubmed.ncbi.nlm.nih.gov/42649352/)

This mechanistically links dominant hepaCAM mutations to both **gap-junctional coupling defects** (Connexin 43) and **seizure susceptibility** (KCNQ2), and emphasizes a cell-biological, developmentally timed mechanism consistent with the remitting course.

### Finding 7 — GlialCAM operates in an adhesion/signaling axis with MLC1 and aquaporin-4 controlling astrocyte state and water handling

De et al. (2023), using human glioblastoma specimens and single-cell transcriptomics, independently validated functional links among **GlialCAM, Mlc1, and aquaporin-4 (AQP4)**. High GlialCAM promotes cell–cell adhesion, while its loss activates pro-invasive extracellular-matrix adhesion/signaling. Although this was a cancer-biology study, it independently confirms GlialCAM's normal astrocyte adhesion role and its partnership with the **water channel AQP4** — the same axis disrupted in MLC2B.

> *"Profiling GlialCAM-regulated genes combined with cross-referencing to single-cell transcriptomic datasets validates functional links among GlialCAM, Mlc1, and aquaporin-4 in the invasive cell state."* — [PMID: 37722850](https://pubmed.ncbi.nlm.nih.gov/37722850/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous dominant missense variant in HEPACAM** (clustering in the first Ig domain) **leads to** production of a mutant GlialCAM monomer alongside wild-type protein. *(Demonstrated — López-Hernández 2011; Elorza-Vidal 2020.)*
2. The mutant monomer **disrupts GlialCAM–GlialCAM self-association** (cis within a cell and trans between neighbouring astrocytes), **resulting in** a **dominant-negative** impairment of GlialCAM assembly. *(Inferred from structural modelling — Elorza-Vidal 2020.)*
3. Impaired GlialCAM self-assembly **results in** failed **targeting of the GlialCAM–MLC1–ClC-2 complex to cell–cell junctions** at perivascular astrocyte endfeet. *(Demonstrated — Jeworutzki 2012; case p.Q56P, Arnedo 2014.)*
4. Mislocalization **leads to** rewiring of the astrocyte interactome: **decreased association with Connexin 43 (gap-junction coupling) and ClC-2**, and **aberrant interaction with KCNQ2**. *(Demonstrated in mouse cortex in vivo — Lewis 2025/2026.)*
5. These coupling/channel defects **result in** disturbed astrocytic **ion (Cl⁻, K⁺) and water handling**, including impaired **volume-regulated anion channel (VRAC)** activity and dysregulated **AQP4**-mediated water flux. *(Demonstrated/supported — Kerst 2026; De 2023; Mlc1-null mice.)*
6. Impaired astrocyte **regulatory volume decrease** **leads to** **astrocytic swelling** at fluid–brain barriers (the earliest change in model mice). *(Demonstrated — Mlc1-null mice, PMID 25382142.)*
7. Astrocyte swelling and fluid dysregulation **result in** **chronic white-matter edema with intramyelinic (myelin) vacuolation** and, in classic forms, **subcortical cysts**. *(Demonstrated histopathology.)*
8. Edema **manifests clinically** as **infantile macrocephaly**, ± seizures, ± mild motor/cognitive involvement. *(Demonstrated clinically.)*
9. **Branch (MLC2B-specific):** Because only **one** dominant allele is affected, the homeostatic disturbance is **partial and developmentally timed** — as MLC1/GlialCAM expression peaks in infancy and then declines, the defect **leads to spontaneous improvement/normalization** of edema and MRI, producing the **remitting** MLC2B phenotype (benign familial macrocephaly ↔ macrocephaly with ID/autism). *(Inferred from genotype–phenotype and developmental expression data — López-Hernández 2011; PMID 25382142.)*
10. **Branch (MLC2A / classic MLC):** **Two** HEPACAM alleles (or biallelic MLC1 loss) **lead to** a more complete, **persistent** homeostatic failure → **progressive** deterioration rather than remission. *(Demonstrated.)*
11. **Emerging parallel node:** GlialCAM/MLC1 regulate the orphan GPCR **GPRC5B**; dominant GPRC5B mutations can themselves cause MLC, suggesting a **gain-of-function signaling** contribution acting alongside the adhesion/ion-homeostasis defect. *(Emerging — Kerst 2026.)*

### Schematic

```
HEPACAM dominant missense (1st Ig domain)
        │ dominant-negative
        ▼
GlialCAM cis/trans self-association disrupted
        │
        ▼
MLC1-GlialCAM-ClC-2 complex NOT targeted to astrocyte junctions
        │
        ├─► down Connexin 43 coupling ─► gap-junction network defect
        ├─► down ClC-2 Cl- current ────► anion/osmotic dysregulation
        ├─► aberrant KCNQ2 binding ─────► seizure susceptibility
        └─► impaired VRAC / AQP4 ───────► water flux dysregulation
                                 │
                                 ▼
             impaired astrocyte Regulatory Volume Decrease
                                 │
                                 ▼
                 perivascular astrocyte swelling
                                 │
                                 ▼
          chronic white-matter edema + intramyelinic vacuolation
                                 │
                                 ▼
              MACROCEPHALY (± seizures, ± mild ID/autism)
                                 │
            ┌────────────────────┴────────────────────┐
     1 allele (MLC2B)                          2 alleles (MLC2A/classic)
     developmentally timed → IMPROVES          persistent → PROGRESSIVE
```

### Upstream vs downstream

- **Upstream (initiating):** HEPACAM dominant mutation → GlialCAM self-assembly/trafficking failure.
- **Midstream (effector):** mislocalization of MLC1–ClC-2; loss of Connexin 43 coupling; VRAC/AQP4 dysregulation.
- **Downstream (tissue/clinical):** astrocyte swelling → myelin vacuolation/edema → macrocephaly, seizures, variable cognition.

### Cell types and biological processes (ontology suggestions)

- **Cell types (CL):** astrocyte (**CL:0000127**); perivascular astrocyte / astrocyte endfoot; Bergmann glia (**CL:0000644**); oligodendrocyte (secondarily, via myelin vacuolation, **CL:0000128**).
- **Biological processes (GO):** cell volume homeostasis (**GO:0006884**); regulation of regulatory volume decrease; chloride transmembrane transport (**GO:1902476**); water transport (**GO:0006833**); cell–cell adhesion (**GO:0098609**); gliogenesis / astrocyte development (**GO:0014002**).
- **Cellular components (GO CC):** plasma membrane (**GO:0005886**); cell junction (**GO:0030054**); anchoring junction; astrocyte endfoot plasma membrane; myelin sheath (**GO:0043209**).

---

## Section-by-Section Knowledge Base Entry

### 1. Disease Information
MLC2B is a rare genetic vacuolating leukoencephalopathy — the **dominant, remitting** HEPACAM form of the MLC family. **Identifiers:** OMIM **613926**; MONDO **MONDO:0013491**; gene **HEPACAM** (HGNC:17027, GlialCAM). Orphanet classifies MLC under ORPHA:2478 (MLC) with gene-defined subtypes. **Synonyms:** "megalencephalic leukoencephalopathy with subcortical cysts 2B, remitting, with or without mental retardation"; "MLC2B"; dominant-HEPACAM MLC. Information is derived from **aggregated disease-level resources** (OMIM, Orphanet) and **published patient cohorts/case series** (e.g., López-Hernández 2011; Hamilton 2018), not EHR.

### 2. Etiology
**Primary cause:** a single heterozygous (dominant) pathogenic variant in **HEPACAM**, predominantly **missense** variants affecting the first Ig domain, acting **dominant-negatively** ([PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/); [PMID: 31960914](https://pubmed.ncbi.nlm.nih.gov/31960914/)). **Genetic risk factors:** the HEPACAM variant itself is causal; **MLC1** and **GPRC5B** are related genes within the same disease family / pathway. **Modifier/allele-dosage effect:** zygosity is the principal modifier of course (1 allele → remitting MLC2B; 2 alleles → progressive MLC2A). **Environmental risk/protective factors and gene–environment interactions:** none established — MLC2B is a monogenic Mendelian disorder with no known environmental contribution. **No infectious etiology.**

### 3. Phenotypes
| Phenotype | Type | HPO suggestion | Onset | Course | Frequency |
|---|---|---|---|---|---|
| Macrocephaly | Physical sign | HP:0000256 | Infantile | Persistent (even after MRI improves) | Nearly all |
| White-matter edema / abnormal MRI signal | Imaging/lab | HP:0002500 / HP:0040146 | Infantile | **Improving/remitting** in MLC2B | Characteristic |
| Subcortical cysts | Imaging | HP:0002416 / HP:0006891 | Infantile | May regress | Variable (less than classic) |
| Seizures / epilepsy | Clinical sign | HP:0001250 | Childhood | Variable | Subset |
| Intellectual disability | Cognitive | HP:0001249 | Childhood | Mild/variable | Subset ("with or without") |
| Autism / autistic features | Behavioral | HP:0000717 | Childhood | Variable | Subset |
| Motor delay / mild motor deterioration | Clinical | HP:0001270 | Childhood | Usually mild in MLC2B | Subset |

**Quality-of-life impact:** at the **benign end**, essentially normal functioning (benign familial macrocephaly); at the **more affected end**, impact is driven by intellectual disability, autism, and/or seizures rather than by progressive motor decline, which distinguishes MLC2B from classic MLC.

### 4. Genetic / Molecular Information
**Causal gene:** HEPACAM / GlialCAM (chromosome 11q24.2; OMIM gene 611642). **Variant classes:** predominantly **missense** (dominant MLC2B); nonsense/frameshift and compound-heterozygous combinations, and an intragenic duplication, are seen in recessive MLC2A ([PMID: 24202401](https://pubmed.ncbi.nlm.nih.gov/24202401/); [PMID: 38280046](https://pubmed.ncbi.nlm.nih.gov/38280046/)). **Representative dominant allele:** p.Q56P (MLC2B; mislocalizes GlialCAM yet preserves ClC-2 activation) ([PMID: 24202401](https://pubmed.ncbi.nlm.nih.gov/24202401/)). **Classification:** per ACMG/AMP, recurrent MLC-associated missense variants are typically pathogenic/likely pathogenic (ClinVar). **Allele frequency:** pathogenic variants are rare/absent in gnomAD. **Origin:** germline; dominant variants are frequently **de novo** or inherited from a mildly affected/macrocephalic parent. **Functional consequence:** **dominant-negative** disruption of GlialCAM self-assembly and complex trafficking (MLC2B); **loss of function** in biallelic MLC2A. **Modifier genes:** allele dosage; pathway partners MLC1, GPRC5B, AQP4. **Chromosomal:** large deletions encompassing HEPACAM (11q terminal deletion / Jacobsen syndrome) can produce an MLC2B-like remitting white-matter picture ([PMID: 32507665](https://pubmed.ncbi.nlm.nih.gov/32507665/)).

### 5. Environmental Information
**Not applicable** — no environmental, lifestyle, or infectious factors are known to cause or modify MLC2B. It is a purely monogenic disorder.

### 6. Mechanism / Pathophysiology
Presented in full above (see **Mechanistic Model**). Summary: dominant HEPACAM mutation → GlialCAM self-assembly/trafficking failure → mislocalized MLC1–ClC-2 complex, reduced Connexin 43 coupling, aberrant KCNQ2 binding, impaired VRAC/AQP4 water handling → astrocyte swelling → white-matter edema/vacuolation → macrocephaly ± seizures ± mild cognitive involvement; partial single-allele defect and developmental timing yield the remitting course. **Molecular pathway:** astrocytic ion/water homeostasis (ClC-2 chloride transport, VRAC/LRRC8A, AQP4 water channel), GlialCAM/MLC1 adhesion, GPRC5B signaling. **Cellular processes:** regulatory volume decrease, gap-junctional coupling, cell adhesion. **Protein dysfunction:** dominant-negative mislocalization (not aggregation). **Immune involvement:** none causal, though anti-GlialCAM autoantibodies appear in multiple sclerosis (separate context, [PMID: 35628339](https://pubmed.ncbi.nlm.nih.gov/35628339/)). **Tissue damage mechanism:** osmotic/fluid accumulation → intramyelinic vacuolation.

### 7. Anatomical Structures Affected
- **Organ/system:** central nervous system (**UBERON:0001017**); cerebral **white matter** (**UBERON:0002316**) is the primary target; brain (**UBERON:0000955**).
- **Preferential sites:** cerebral hemispheric white matter with **anterior-temporal and frontoparietal subcortical cysts**; perivascular astrocyte endfeet (gliovascular unit).
- **Tissue/cell level:** nervous tissue; **astrocytes** (CL:0000127), especially perivascular astrocytes and **Bergmann glia** (CL:0000644); secondary **myelin/oligodendrocyte** involvement.
- **Subcellular (GO CC):** plasma membrane, **cell junctions** (GO:0030054), astrocyte endfoot membrane, myelin sheath (GO:0043209).
- **Lateralization:** **bilateral and symmetric** white-matter involvement.

### 8. Temporal Development
- **Onset:** infantile (macrocephaly often noted in first year); **insidious/chronic** onset.
- **Course (MLC2B hallmark):** **remitting/improving** — clinical and MRI abnormalities frequently stabilize, improve, or normalize over childhood, in contrast to the slowly progressive deterioration of classic/recessive MLC ([PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/); [PMID: 29661901](https://pubmed.ncbi.nlm.nih.gov/29661901/); [PMID: 32507665](https://pubmed.ncbi.nlm.nih.gov/32507665/)).
- **Remission pattern:** spontaneous (developmentally timed), not treatment-induced.
- **Critical period:** infancy/early childhood, coinciding with peak astrocytic MLC1/GlialCAM expression and myelination.

### 9. Inheritance and Population
- **Inheritance:** autosomal **dominant** (MLC2B); contrast recessive MLC1/MLC2A.
- **Penetrance/expressivity:** **incomplete penetrance and highly variable expressivity** — ranges from asymptomatic/benign familial macrocephaly to macrocephaly with intellectual disability ± autism within the same family ([PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/)).
- **De novo vs inherited:** both; mildly affected macrocephalic parents may transmit.
- **Epidemiology:** MLC overall is very rare (orphan disease); HEPACAM accounts for ~25% of MLC, of which MLC2B is the dominant subset. Precise prevalence/incidence of MLC2B specifically is not established; higher MLC frequency is reported in consanguineous and certain founder populations — these largely reflect **recessive** forms.
- **Sex ratio:** no strong sex bias reported. **Consanguinity:** relevant to recessive forms, not dominant MLC2B.

### 10. Diagnostics
- **Imaging (primary):** brain **MRI** showing diffuse, bilaterally symmetric white-matter signal abnormality/edema with anterior-temporal (± frontoparietal) subcortical cysts; **serial MRI showing improvement** supports MLC2B ([PMID: 24821940](https://pubmed.ncbi.nlm.nih.gov/24821940/); [PMID: 32507665](https://pubmed.ncbi.nlm.nih.gov/32507665/)).
- **Clinical clue:** infantile macrocephaly (serial head-circumference).
- **Genetic testing (confirmatory):** **single-gene HEPACAM sequencing** or a **leukodystrophy/MLC gene panel** (HEPACAM + MLC1); **WES/WGS** when panels are negative; **CMA** can detect 11q deletions mimicking MLC2B. Zygosity determination (one vs two HEPACAM alleles) distinguishes MLC2B from MLC2A.
- **Biopsy/pathology (historical/research):** myelin and perivascular astrocyte **vacuolation** — rarely needed clinically.
- **No specific blood/urine biomarker or enzyme assay** exists; diagnosis is imaging + genetic.
- **Differential diagnosis:** classic MLC (MLC1, recessive), Canavan disease, vanishing white matter disease, Alexander disease, Jacobsen syndrome (11q deletion), other megalencephalic/vacuolating leukodystrophies — distinguished by causal gene, cyst distribution, and especially **course** (remitting vs progressive).

### 11. Outcome / Prognosis
- **Prognosis is comparatively favourable** for MLC2B: motor and cognitive function are typically preserved or only mildly affected, and imaging/clinical features improve ([PMID: 21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/)).
- **Life expectancy:** not reported to be reduced in the benign end of the spectrum; no disease-specific mortality data.
- **Morbidity:** driven by residual macrocephaly, variable intellectual disability/autism, and seizures (subset), rather than progressive disability.
- **Prognostic factors:** allele dosage (dominant single allele → better), presence/absence of seizures and cognitive involvement.

### 12. Treatment
- **No disease-modifying therapy exists;** management is **supportive/symptomatic** ([PMID: 38487253](https://pubmed.ncbi.nlm.nih.gov/38487253/); [PMID: 33551753](https://pubmed.ncbi.nlm.nih.gov/33551753/)).
- **Supportive care (NCIT suggestions):** antiepileptic/anticonvulsant drugs for seizures; developmental/educational support, physical/occupational/speech therapy for those with motor or cognitive involvement; behavioral support for autism features.
- **No approved gene, cell, RNA, or targeted therapy** for MLC2B. Experimental directions target the shared MLC pathway (e.g., VRAC/ion-homeostasis modulation); none is MLC2B-specific. (Note: guanabenz in the [PMID: 42586097](https://pubmed.ncbi.nlm.nih.gov/42586097/) trial is for **vanishing white matter**, a different leukodystrophy — not MLC2B.)

### 13. Prevention
- **No primary prevention** (monogenic disease). **Genetic counseling** is the principal intervention: autosomal dominant with ~50% transmission risk per child from an affected parent, but with **incomplete penetrance/variable expressivity** complicating prediction.
- **Prenatal / preimplantation genetic testing** is possible once the familial HEPACAM variant is known. **Cascade testing** of relatives (noting many carriers have only macrocephaly) is appropriate.
- No immunization, behavioral, or public-health prevention applies.

### 14. Other Species / Natural Disease
- **Orthologs:** mouse *Hepacam* / *Mlc1* (NCBI Gene; model species *Mus musculus*, NCBI:txid10090). GlialCAM/MLC1 biology is evolutionarily conserved across mammals.
- **Natural disease:** no well-characterized naturally occurring HEPACAM-MLC2B equivalent in companion animals is established in the reviewed literature (OMIA not confirmed here).
- **No zoonotic or cross-species transmission** (genetic disease).

### 15. Model Organisms
- **Mouse — Mlc1-null:** recapitulates early human disease (early-onset megalencephaly, increased brain water content, abnormal perivascular astrocytes from ~3 weeks, widespread white-matter vacuolization/intramyelinic edema from ~3 months); astrocytes show **slowed regulatory volume decrease and reduced volume-regulated anion currents**, rescued by MLC1 re-expression, and **reduced GlialCAM and ClC-2 expression** — confirming the astrocyte volume-regulation defect as the primary lesion ([PMID: 25382142](https://pubmed.ncbi.nlm.nih.gov/25382142/)).
- **Mouse — GlialCAM / hepaCAM models:** developmental in-vivo studies of dominant hepaCAM variants show redistribution and interactome rewiring in cortical astrocytes ([PMID: 42649352](https://pubmed.ncbi.nlm.nih.gov/42649352/), [PMID: 40894676](https://pubmed.ncbi.nlm.nih.gov/40894676/)).
- **Mouse — Lrrc8a (VRAC) conditional KO:** astrocyte-specific deletion causes neurological dysfunction but **not** chronic white-matter edema — a useful negative/refining model ([PMID: 41654199](https://pubmed.ncbi.nlm.nih.gov/41654199/)).
- **In vitro:** patient lymphoblasts and primary astrocytes (VRAC assays); heterologous expression systems (Xenopus oocytes / HEK/HeLa) for ClC-2 trafficking and current studies ([PMID: 22405205](https://pubmed.ncbi.nlm.nih.gov/22405205/)).
- **Model limitation:** most genetic models address MLC1 loss (recessive) rather than the **dominant-negative** MLC2B mechanism, and models do not fully capture the **remitting** human course.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [21419380](https://pubmed.ncbi.nlm.nih.gov/21419380/) | Mutant GlialCAM causes MLC, benign familial macrocephaly, macrocephaly+retardation/autism | Human clinical/genetic | F1, F4 — dominant 1-allele → remitting MLC2B; phenotype spectrum |
| [22405205](https://pubmed.ncbi.nlm.nih.gov/22405205/) | GlialCAM is a ClC-2 auxiliary subunit | In vitro / molecular | F2 — ClC-2 β-subunit, junctional targeting, mutations abolish it |
| [31960914](https://pubmed.ncbi.nlm.nih.gov/31960914/) | Structural basis of dominant vs recessive GLIALCAM mutations | Computational/structural | F3 — dominant = 1st Ig domain self-interaction surfaces |
| [24202401](https://pubmed.ncbi.nlm.nih.gov/24202401/) | Expanding spectrum: two GLIALCAM patients (MLC2B p.Q56P; MLC2A) | Human + in vitro | F3 — dominant vs recessive allele functional contrast |
| [29661901](https://pubmed.ncbi.nlm.nih.gov/29661901/) | MLC disease variant characterization (204 patients) | Human cross-sectional | F4 — course distinguishes subtypes |
| [32507665](https://pubmed.ncbi.nlm.nih.gov/32507665/) | Serial MRI in Jacobsen syndrome (HEPACAM deletion) | Human imaging | F4 — remitting white-matter course |
| [24821940](https://pubmed.ncbi.nlm.nih.gov/24821940/) | Resolution of MRI abnormalities in MLC | Human imaging | F4 — MRI improvement |
| [38280046](https://pubmed.ncbi.nlm.nih.gov/38280046/) | Intragenic HEPACAM duplication → MLC2A | Human genetic | F1 — OMIM 613926, AD; HEPACAM allelic series |
| [41654199](https://pubmed.ncbi.nlm.nih.gov/41654199/) | Astrocyte-specific Lrrc8a KO | Mouse model | F5 — VRAC module; LRRC8A loss insufficient |
| [41314544](https://pubmed.ncbi.nlm.nih.gov/41314544/) | GPRC5B regulated by MLC1/GlialCAM | In vitro/biochem | F5 — GPRC5B signaling node |
| [34723793](https://pubmed.ncbi.nlm.nih.gov/34723793/) | MLC as developmental disorder of the gliovascular unit | Review/model | F6 — gliovascular-unit localization |
| [42649352](https://pubmed.ncbi.nlm.nih.gov/42649352/) | Dominant hepaCAM variants alter localization & interactome | Mouse in vivo | F6 — interactome rewiring (Cx43, ClC-2, KCNQ2) |
| [40894676](https://pubmed.ncbi.nlm.nih.gov/40894676/) | Dominant MLC hepaCAM mutations alter localization/interactome | Mouse in vivo | F6 — ~25% MLC from hepaCAM; dominant mechanism |
| [37722850](https://pubmed.ncbi.nlm.nih.gov/37722850/) | GlialCAM in glioblastoma cell state | Human/scRNA-seq | F7 — GlialCAM–MLC1–AQP4 axis |
| [25382142](https://pubmed.ncbi.nlm.nih.gov/25382142/) | Mlc1-null mice: developmental angle | Mouse model | Mechanism — astrocyte RVD/VRAC defect, ↓GlialCAM/ClC-2 |
| [38487253](https://pubmed.ncbi.nlm.nih.gov/38487253/) | MLC variant update & review | Review | Treatment — "No treatment is available" |
| [33551753](https://pubmed.ncbi.nlm.nih.gov/33551753/) | MLC pathophysiology & therapy perspectives | Review | Mechanism, treatment |
| [25883547](https://pubmed.ncbi.nlm.nih.gov/25883547/) | MLC1 links leukodystrophies & channelopathies | Review | Mechanism — ion/water homeostasis |
| [35628339](https://pubmed.ncbi.nlm.nih.gov/35628339/) | GPR37 & MLC; anti-GlialCAM in MS | Review | Immune context (separate) |

**Consistency:** All seven confirmed findings are mutually reinforcing. The dominant-negative structural model (F3) explains the dominant inheritance established clinically (F1); the ClC-2/MLC1 trafficking role (F2) and gliovascular-unit localization/interactome data (F6) explain the ion-water homeostasis defect; the VRAC and AQP4 convergence (F5, F7) and Mlc1-null mouse data unify MLC-family genes onto one astrocytic volume-regulation module. No reviewed paper contradicts the core model; the Lrrc8a-KO negative result (F5) refines rather than refutes it.

---

## Limitations and Knowledge Gaps

1. **MLC2B-specific epidemiology is absent.** Prevalence, incidence, and sex distribution of the dominant subtype specifically are not quantified; most cohort data pool recessive MLC.
2. **Dominant-negative mechanism is partly inferred.** The cis/trans self-interaction model (F3) rests on structural modelling; direct structural (cryo-EM/crystallographic) confirmation of mutant GlialCAM self-association defects is still needed.
3. **No MLC2B-specific animal model fully captures remission.** Most genetic models are MLC1-null (recessive); dominant hepaCAM in-vivo work is recent and does not yet reproduce the human improving course.
4. **Molecular basis of remission is unexplained.** Why single-allele defects resolve developmentally (compensation? declining MLC1/GlialCAM expression? myelination maturation?) is hypothesized but not demonstrated.
5. **GPRC5B node is emerging.** Its weight relative to the ion-homeostasis defect, and whether it contributes to MLC2B specifically, is unresolved.
6. **No biomarkers or therapies.** No fluid biomarker, no disease-modifying treatment, and no natural-history registry data specific to MLC2B.
7. **Penetrance quantification is lacking.** "Incomplete penetrance/variable expressivity" is qualitative; no numeric penetrance estimates exist for specific dominant alleles.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history / genotype–phenotype registry for HEPACAM-dominant MLC2B**, with serial head circumference, MRI (quantitative white-matter water content), and neurocognitive outcomes to quantify remission timing, penetrance, and expressivity per allele.
2. **Knock-in mouse (or iPSC-astrocyte/organoid) carrying a bona fide dominant MLC2B allele** (e.g., p.Q56P) to test whether it reproduces the **remitting** course and to dissect developmental compensation.
3. **Structural validation** (cryo-EM/AlphaFold-Multimer + biophysics) of GlialCAM Ig1 cis/trans self-association, comparing dominant vs recessive mutants, to confirm the dominant-negative surface model (F3).
4. **Interactome time-course** in developing astrocytes to test whether loss of Connexin 43/ClC-2 association and gain of KCNQ2 binding (F6) normalize as edema remits — linking molecular rewiring to clinical remission.
5. **VRAC/AQP4 functional assays** in MLC2B patient-derived astrocytes vs MLC2A, to determine whether the dominant single-allele defect produces a *partial* (recoverable) versus *complete* homeostatic failure, testing the allele-dosage model.
6. **Evaluate GPRC5B signaling** (gain-of-function) in HEPACAM-dominant backgrounds to define its contribution and druggability within the MLC pathway.
7. **Biomarker discovery** (CSF/plasma proteomics, imaging quantitation) to track and predict the remitting course and support any future trials.

---

*Report compiled from 7 confirmed findings and 23 reviewed papers over 5 completed investigation iterations. Evidence types are annotated (human clinical, mouse model, in vitro, computational/structural). Causal gene throughout: **HEPACAM/GlialCAM**; disease: **MLC2B (OMIM 613926, MONDO:0013491)**.*


## Artifacts

- [OpenScientist final report](Megalencephalic_Leukoencephalopathy_With_Subcortical_Cysts_2B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Megalencephalic_Leukoencephalopathy_With_Subcortical_Cysts_2B-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 18 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42586097` (3 mentions) - Safety and efficacy of guanabenz in early-childhood onset vanishing white matter: primary analysis of a single-arm, phase 1/2 trial.
  - shared terms: disease, model

Weighed against this report's own most characteristic terms: `mlc2b`, `hepacam`, `dominant`, `glialcam`, `mlc1`, `mlc`, `remitting`, `astrocyte`, `macrocephaly`, `course`, `recessive`, `mutation`, `cell`, `clc-2`, `allele`, `gene`, `mlc2a`, `disease`, `model`, `white-matter`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000256` (1 mention) - the report calls it "Physical sign"; HP calls it **Macrocephaly**
- `HP:0001250` (1 mention) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `HP:0001249` (1 mention) - the report calls it "Cognitive"; HP calls it **Intellectual disability**
- `HP:0000717` (1 mention) - the report calls it "Behavioral"; HP calls it **Autism**
- `HP:0001270` (1 mention) - the report calls it "Clinical"; HP calls it **Motor delay**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000644` (2 mentions) - the report calls it "Bergmann glia"; CL calls it **Bergmann glial cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.