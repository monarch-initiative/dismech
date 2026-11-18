---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T08:50:25.026921'
end_time: '2026-11-13T09:47:53.155357'
duration_seconds: 3448.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital High-molecular-weight Kininogen Deficiency
  mondo_id: MONDO:0009234
  category: Mendelian
  causal_genes: KNG1
  omim_id: OMIM:228960
  synonyms: kininogen deficiency; high molecular weight kininogen deficiency
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 0ed64834-48d4-49b0-9971-3bcaba9be869
citation_count: 15
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 8
  validator_version: 0.5.1
term_validation:
  total_terms: 21
  verified: 19
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 7
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0009234
    reported_labels:
    - MONDO
    ontology_label: congenital high-molecular-weight kininogen deficiency
  - term_id: HP:0011897
    reported_labels:
    - Abnormal prekallikrein
    ontology_label: Increased total neutrophil count
  - term_id: HP:0004863
    reported_labels:
    - Abnormality of coagulation factor XI
    ontology_label: Compensated hemolytic anemia
  - term_id: GO:0002542
    reported_labels:
    - bradykinin biosynthetic process
    ontology_label: Factor XII activation
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Congenital_High-molecular-weight_Kininogen_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_High-molecular-weight_Kininogen_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital High-molecular-weight Kininogen Deficiency
- **MONDO ID:** MONDO:0009234 (if available)
- **Causal gene(s):** KNG1
- **OMIM:** OMIM:228960
- **Synonyms:** kininogen deficiency; high molecular weight kininogen deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital High-molecular-weight Kininogen Deficiency** covering all of the
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

# Congenital High-Molecular-Weight Kininogen Deficiency (KNG1) — Comprehensive Disease Report

**Disease:** Congenital High-molecular-weight Kininogen Deficiency
**MONDO ID:** MONDO:0009234 · **OMIM:** 228960 · **Causal gene:** **KNG1** (kininogen-1; HGNC:6383; chromosome 3q27; UniProt P01042)
**Historical eponym:** Fitzgerald factor deficiency (also Williams, Flaujeac, Fujiwara traits) · **Category:** Mendelian, autosomal recessive

---

## Summary

Congenital high-molecular-weight kininogen (HK) deficiency is an ultra-rare, autosomal recessive defect of the plasma **contact (kallikrein–kinin) system** caused by **biallelic truncating loss-of-function (LOF) variants in the KNG1 gene**. KNG1 produces, by alternative splicing, both high-molecular-weight kininogen (HK) and low-molecular-weight kininogen (LK). HK is a non-enzymatic cofactor that scaffolds prekallikrein (PK) and factor XI (FXI) onto anionic surfaces and endothelial receptors, enabling factor XII (FXII)–driven contact activation. Because this contact pathway is dispensable for physiologic hemostasis, the complete absence of HK produces a **striking laboratory abnormality — an isolated, markedly prolonged activated partial thromboplastin time (aPTT) — but no clinical disease**. Affected individuals are asymptomatic, have normal life expectancy, and require no treatment; the principal clinical risk is *misdiagnosis* leading to unnecessary intervention.

The investigation confirmed nine core findings. Severe HK deficiency is defined by <1% HK procoagulant activity, isolated prolonged aPTT (that corrects on 1:1 mixing with normal plasma), and secondary reductions in PK and FXI. A 2023 systematic review catalogued **48 cases across 41 families**, identified **10 distinct deficiency-causing KNG1 variants — all truncating (nonsense/frameshift)** — and estimated a prevalence of **~1 case per 8 million**, modestly higher in individuals of African ancestry ([PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)). The benign nature of the human phenotype is mirrored and mechanistically explained by mouse models: *Kng1*-knockout mice are **protected** from ischemic stroke and experimental cerebral malaria without any bleeding penalty, establishing HK as pathogenic in thromboinflammation yet dispensable for hemostasis.

A crucial nuance is KNG1's **dual, variant-type-dependent phenotype**: truncating LOF alleles cause benign HK *deficiency*, whereas a specific missense substitution causes **bradykinin-mediated hereditary angioedema (HAE-KNG1)** — a gain-of-pathway, not loss-of-function, disorder. Diagnostically, HK deficiency must be distinguished from the two other benign contact-factor deficiencies (FXII and prekallikrein) using mixing studies and specific factor assays, and conceptually from HAE-KNG1. The entire picture validates the contact system as a *safe antithrombotic drug target* — the therapeutic rationale behind contemporary agents such as the anti-FXIIa antibody garadacimab.

---

## Disease Information (Section 1)

**Overview.** Congenital HK deficiency is a hereditary, autosomal recessive coagulation-factor deficiency in which the plasma concentration/activity of high-molecular-weight kininogen is severely reduced (typically <1% in homozygotes/compound heterozygotes). HK is a central cofactor of the contact activation system that bridges the intrinsic coagulation pathway and the inflammatory kallikrein–kinin (bradykinin) axis. Because the contact system is not required for normal hemostasis, the deficiency is clinically silent and is almost always discovered incidentally during work-up of an unexplained, isolated prolonged aPTT.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009234 |
| OMIM | 228960 |
| Gene | KNG1 (HGNC:6383; NCBI Gene 3827; Ensembl ENSG00000113889; UniProt P01042) |
| Cytoband | 3q27.3 |
| Inheritance | Autosomal recessive |

**Synonyms / alternative names.** Kininogen deficiency; high-molecular-weight kininogen deficiency; HMWK deficiency; **Fitzgerald factor deficiency** (classic eponym); Williams trait; Flaujeac trait; Fujiwara trait; total kininogen deficiency (when both HK and LK are affected by variants in the common heavy chain).

**Source of information.** Evidence is derived almost entirely from **aggregated disease-level resources and individual published case reports** (coagulation laboratories, hematology case series, and a 2023 systematic review), not from large EHR cohorts — reflecting the condition's extreme rarity and asymptomatic nature.

---

## Etiology (Section 2)

**Primary cause — genetic.** The disease is monogenic: **biallelic truncating loss-of-function variants in KNG1**. All ten deficiency-causing variants catalogued to date are nonsense or frameshift mutations ([PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)). Representative reported variants include p.Gln486* (c.1456C>T) in a large Chinese family ([PMID: 32185598](https://pubmed.ncbi.nlm.nih.gov/32185598/)), an exon-4 frameshift (c.523_524insTC) in a patient with splenic infarction ([PMID: 24492696](https://pubmed.ncbi.nlm.nih.gov/24492696/)), and c.488delG in the first Korean case ([PMID: 31858768](https://pubmed.ncbi.nlm.nih.gov/31858768/)).

> *"All of them were truncating mutations, whereas the only known HK amino acid substitution with a relevant phenotype instead causes hereditary angioedema."* — [PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)

**Genetic risk factors.** The only risk factor is inheritance of two LOF KNG1 alleles. Heterozygous carriers (~50% HK activity) are asymptomatic with normal or near-normal aPTT. Consanguinity increases the likelihood of homozygosity, consistent with reports of affected individuals in isolated or endogamous populations (e.g., the first Australian case in an Aboriginal individual, [PMID: 3574180](https://pubmed.ncbi.nlm.nih.gov/3574180/)).

**Environmental risk / protective / gene–environment factors.** **Not applicable.** There are no established environmental, lifestyle, infectious, dietary, or occupational risk or protective factors, and no gene–environment interactions. The condition is fully determined by genotype. Notably, in model systems the *loss* of HK is itself *protective* against thrombosis and thromboinflammation (see Mechanism), but this is a consequence of the genotype, not an external modifier.

---

## Phenotypes (Section 3)

The defining feature is the **near-total absence of a clinical phenotype** despite a dramatic laboratory abnormality.

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency | QoL impact |
|---|---|---|---|---|---|---|
| Prolonged aPTT (isolated) | Laboratory abnormality | HP:0003645 (Prolonged partial thromboplastin time) | Congenital (present from birth; detected at any age) | Marked (aPTT often 2–3× ULN) | ~100% of homozygotes | None |
| Reduced HK activity/antigen (<1%) | Laboratory abnormality | — (abnormal coagulation factor activity) | Congenital | Severe | ~100% | None |
| Secondary low prekallikrein | Laboratory abnormality | HP:0011897 (Abnormal prekallikrein) | Congenital | Mild–moderate | Common | None |
| Secondary low factor XI | Laboratory abnormality | HP:0004863 (Abnormality of coagulation factor XI) | Congenital | Mild–moderate | Common | None |
| Bleeding tendency | Symptom | HP:0001892 (Abnormal bleeding) | — | **Absent** | ~0% | None |

> *"Individuals with HK deficiency appeared asymptomatic and had decreased levels of prekallikrein and factor XI, which could lead to misdiagnosis."* — [PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)

**Important interpretive note.** Isolated reports describe thrombotic/ischemic events in deficient individuals — e.g., splenic infarction ([PMID: 24492696](https://pubmed.ncbi.nlm.nih.gov/24492696/)) and an association with acute granulocytic leukaemia ([PMID: 6573994](https://pubmed.ncbi.nlm.nih.gov/6573994/)). These are anecdotal co-occurrences in a tiny population and are **not established as caused by the deficiency**; the systematic review's overall conclusion remains that the condition is asymptomatic. **Quality-of-life impact is negligible** because the condition does not cause symptoms; the chief hazard is iatrogenic (unnecessary blood products or delayed surgery from misinterpreting the aPTT).

---

## Genetic / Molecular Information (Section 4)

**Causal gene.** KNG1 (OMIM gene 612358), chromosome 3q27.3. By alternative splicing of a shared heavy-chain-encoding region, KNG1 produces **HK** (120–160 kDa) and **LK**. Truncating variants in the common exons abolish both; variants in HK-specific regions selectively affect HK.

**Protein architecture (HK).** HK is a **multidomain protein of the cystatin superfamily**:
- **Heavy chain — domains D1–D3** (cystatin-like folds; D2/D3 inhibit cysteine proteases);
- **D4** — the **bradykinin** segment, released by kallikrein cleavage;
- **Light chain — D5** (histidine/glycine/Zn²⁺-rich; binds anionic surfaces and the endothelial receptor gC1qR/C1QBP) and **D6** (binds prekallikrein and factor XI).

> *"Analysis of the binding of HK domain 5 (HKD5) to gC1qR shows only 1 high-affinity binding site per trimer."* — [PMID: 32559765](https://pubmed.ncbi.nlm.nih.gov/32559765/)

**Variant classification & type.** Deficiency-causing variants are **pathogenic/likely pathogenic (ACMG)**, uniformly **truncating** (nonsense, frameshift, splice), predicted **loss-of-function** — they remove the C-terminal light-chain domains (D5/D6) required for surface binding and PK/FXI delivery, abolishing cofactor function. **Allele frequency:** truncating KNG1 alleles are very rare in gnomAD, with modest enrichment in African-ancestry populations (basis for the ~1/8,000,000 prevalence estimate). **Origin:** germline. **Functional consequence:** loss of function.

**Dual phenotype.** A single **missense** KNG1 substitution causes **HAE-KNG1** (bradykinin-mediated angioedema) — the opposite, gain-of-pathway direction ([PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/); [PMID: 39773511](https://pubmed.ncbi.nlm.nih.gov/39773511/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** None established. Secondary reductions in PK (KLKB1) and FXI (F11) reflect loss of the HK-dependent circulating complexes rather than independent genetic lesions. No epigenetic mechanism or large structural/chromosomal abnormality is implicated.

---

## Environmental Information (Section 5)

**Not applicable.** No environmental toxins, radiation, pollutants, occupational exposures, lifestyle factors (smoking, diet, alcohol, exercise), or infectious agents cause or trigger congenital HK deficiency. It is a purely Mendelian trait.

---

## Mechanism / Pathophysiology (Section 6)

### Causal chain (initiating lesion → laboratory manifestation)

1. **Biallelic truncating KNG1 variant** → premature stop codon / frameshift → **loss of full-length HK protein** (and often LK), with removal of light-chain domains D5/D6. *(Demonstrated.)*
2. Loss of D5 → **failure to bind anionic surfaces and the endothelial receptor gC1qR/C1QBP (Zn²⁺-dependent)**; loss of D6 → **failure to carry prekallikrein and factor XI** to the activating surface. *(Demonstrated structurally.)*
3. Absent HK cofactor → **prekallikrein and factor XI are no longer scaffolded into their circulating complexes** → secondary decrease in plasma PK and FXI. *(Demonstrated — observed as secondary low PK/FXI.)*
4. No surface assembly → **FXII-driven reciprocal (contact) activation cannot proceed efficiently in vitro** → the contact-initiated intrinsic pathway (FXIIa→FXIa→FIXa) fails to generate thrombin in the aPTT assay → **markedly prolonged aPTT**, correcting on mixing with normal plasma. *(Demonstrated.)*
5. **Branch A — Hemostasis:** because physiologic clotting is driven by tissue factor/FVIIa (extrinsic) and thrombin feedback, loss of the contact arm leaves **hemostasis intact → no bleeding**. *(Demonstrated in humans and animal models.)*
6. **Branch B — Thromboinflammation:** absent HK → **reduced bradykinin generation** and reduced contact-driven thrombosis → in disease-challenge settings this is **protective** (smaller infarcts, less edema). *(Demonstrated in mice; inferred to underlie the benign human course.)*

### Detail by category

**Molecular pathways.** The **contact / kallikrein–kinin system**. HK forms a ternary complex with FXII on gC1qR: *"Gel filtration experiments reveal that gC1qR clusters FXII and HK into a higher-order 500-kDa ternary complex"* ([PMID: 32559765](https://pubmed.ncbi.nlm.nih.gov/32559765/)). The system *"activates 2 distinct pathways, the intrinsic pathway of coagulation via cleavage of FIX, and inflammation via HK cleavage resulting in bradykinin (BK) generation"* ([PMID: 40638675](https://pubmed.ncbi.nlm.nih.gov/40638675/)). An FXII-*independent* route exists in which **prolylcarboxypeptidase (PRCP)** activates the PK–HK complex to generate bradykinin.

**Protein dysfunction.** Loss of function via truncation; the D5 surface-binding and D6 PK/FXI-binding activities are eliminated. HK is *"central to the function of both arms of the system as a substrate for plasma kallikrein and critical cofactor, which forms interactions with cell receptors and activators"* ([PMID: 40638675](https://pubmed.ncbi.nlm.nih.gov/40638675/)).

**Cellular / immune / tissue processes.** In the normal state, HK-derived bradykinin acts on endothelial **B1/B2 receptors** to drive vasodilation, increased vascular permeability, edema, and inflammation. In deficiency these are blunted. Mouse data: *"BK-induced vasogenic edema contributes to human and murine CM"* ([PMID: 42446942](https://pubmed.ncbi.nlm.nih.gov/42446942/)) — the very process absent when HK is lost.

**Suggested ontology terms.** GO:0002542 (bradykinin biosynthetic process); GO:0007596 (blood coagulation); GO:0002353 (plasma kallikrein-kinin cascade); GO:0006954 (inflammatory response). Cell types (CL): endothelial cell (CL:0000115), platelet (CL:0000233), hepatocyte (CL:0000182; site of synthesis). CHEBI: bradykinin (CHEBI:3165), Zn²⁺ (CHEBI:29105).

---

## Anatomical Structures Affected (Section 7)

- **Organ/system (functional, not structural).** The **cardiovascular/hematologic system** (plasma coagulation; UBERON:0000178 blood) and the **endothelium** (UBERON:0001986) are where the contact system operates. HK is synthesized primarily by the **liver** (hepatocytes; UBERON:0002107).
- **Tissue/cell level.** No tissue is structurally damaged by the deficiency. Functionally relevant cells: hepatocytes (synthesis), vascular endothelial cells (gC1qR-mediated assembly surface), platelets.
- **Subcellular level.** HK is a secreted plasma protein; relevant GO cellular components: GO:0005615 (extracellular space), GO:0072562 (blood microparticle), GO:0009897 (external side of plasma membrane, via gC1qR).
- **Localization / lateralization.** Not applicable — this is a systemic plasma-protein deficiency with no anatomical focus or lateralization.

---

## Temporal Development (Section 8)

- **Onset.** Congenital (present from birth), but the trait is **asymptomatic and insidious** — typically detected incidentally in childhood through late adulthood (reported probands span childhood to age 67).
- **Progression.** **Stable and non-progressive.** There are no disease stages, no progression rate, and no relapsing/remitting course. It is a **lifelong, chronic, incidental laboratory trait**.
- **Patterns.** No remission or critical-period concepts apply. The only clinically relevant "time window" is any situation requiring aPTT interpretation (e.g., pre-operative screening), where misreading the result could prompt unnecessary intervention.

---

## Inheritance and Population (Section 9)

- **Inheritance pattern.** Autosomal recessive. Heterozygotes (~50% HK) are asymptomatic with normal/near-normal aPTT.
- **Penetrance / expressivity.** The *laboratory* phenotype (prolonged aPTT, low HK) is essentially fully penetrant in biallelic individuals; the *clinical* phenotype is effectively null (no symptoms).
- **Epidemiology.** Estimated prevalence **~1 case per 8,000,000**, modestly higher in African-ancestry populations.

> *"Conservative estimates suggest an overall prevalence of severe HK deficiency of approximately one case per 8 million population, slightly higher in Africans."* — [PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)

> *"We identified 48 cases of severe HK deficiency (41 families), of these 47 have been previously published."* — [PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)

- **Founder effects / consanguinity.** Consanguinity and population isolation raise homozygosity risk (e.g., [PMID: 3574180](https://pubmed.ncbi.nlm.nih.gov/3574180/)). No strong single founder allele is established; the modest African enrichment derives from gnomAD truncating-allele frequencies.
- **Carrier frequency.** Very low, consistent with the ~1/8,000,000 homozygote prevalence.
- **Sex ratio.** ~1:1 (autosomal). **Age distribution.** Any age, reflecting incidental detection. No genetic anticipation (not a repeat-expansion disorder); germline mosaicism not reported.

---

## Diagnostics (Section 10)

**Core pattern.** **Isolated, markedly prolonged aPTT with a normal prothrombin time (PT) and no bleeding.** The aPTT **corrects on 1:1 mixing with normal pooled plasma** (indicating factor deficiency, not an inhibitor) but **not** when mixed with plasma deficient in the same factor.

**Confirmatory testing.** Low **HK procoagulant activity (<1%)** and/or antigen; **KNG1 sequencing** confirms biallelic truncating variants. Expect **secondary reductions in PK and FXI** — a recognized misdiagnosis trap.

**Distinguishing from other benign contact-factor deficiencies.** HK, prekallikrein (PK), and factor XII deficiencies all give a prolonged aPTT without bleeding. They are separated by **specific factor assays and mixing with factor-specific depleted plasmas**. Supporting evidence from the analogous PK deficiency literature:

> *"Prekallikrein (PK) deficiency is a rare contact factor deficiency that can markedly prolong the activated partial thromboplastin time (aPTT) without a bleeding phenotype."* — [PMID: 42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/)

> *"The aPTT corrected on mixing with normal pooled plasma but not with PK-deficient plasma."* — [PMID: 42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/)

**Viscoelastic testing.** Thromboelastography (TEG) remains **normal** because physiologic hemostasis is intact — useful for perioperative reassurance ([PMID: 42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/)).

**Genetic testing.** Single-gene **KNG1 sequencing** is definitive; coagulation/thrombophilia gene panels, WES, or WGS will also detect it. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable**. **LOINC:** aPTT (LOINC 14979-9).

**Differential diagnosis.** PK deficiency, FXII deficiency (both benign), lupus anticoagulant (does *not* fully correct on mixing), and true intrinsic-factor deficiencies (FVIII/IX/XI — which *do* bleed, except FXI which bleeds variably).

**Screening.** No population newborn or carrier screening is indicated given the benign nature. Cascade testing within a family is optional for counseling clarity.

---

## Outcome / Prognosis (Section 11)

**Benign with normal life expectancy.** There is no disease-specific mortality, no progressive course, no organ failure, and no disability attributable to the deficiency itself.

> *"Inherited deficiency in contact system proteins is not associated with increased bleeding in humans and animal models."* — [PMID: 35196732](https://pubmed.ncbi.nlm.nih.gov/35196732/)

> *"...high-molecular-weight kininogen, and plasma kallikrein specifically contribute to thrombosis, however, have minor, if any, role in hemostatic coagulation mechanisms."* — [PMID: 35196732](https://pubmed.ncbi.nlm.nih.gov/35196732/)

Morbidity, QoL measures, and prognostic biomarkers are **not applicable**. The main avoidable harm is **iatrogenic** (unnecessary plasma products, surgical delay) from misinterpreting the aPTT. Some mechanistic reasoning and sparse case reports raise the theoretical possibility of a mildly *reduced* thrombotic risk (consistent with the protective mouse data), but this is not an established clinical outcome.

---

## Treatment (Section 12)

**No treatment is required.** The condition is asymptomatic and hemostasis is normal.

- **Pharmacotherapy / advanced therapeutics / surgery:** none indicated for the deficiency.
- **Perioperative management:** reassurance; **routine prophylactic blood products are not indicated.**

> *"...routine prophylactic administration of blood products for pre-operative management of this condition is not indicated."* — [PMID: 40125216](https://pubmed.ncbi.nlm.nih.gov/40125216/)

- **Conceptual relevance (not treatment *of* this disease):** the hemostasis-sparing nature of HK/contact-system loss is the **therapeutic rationale** for drugs that *inhibit* the contact system in other diseases — e.g., the anti-FXIIa monoclonal antibody **garadacimab** and kallikrein inhibitors for hereditary angioedema ([PMID: 42057602](https://pubmed.ncbi.nlm.nih.gov/42057602/)). These are relevant to HAE-KNG1 and HAE-C1INH, **not** to HK deficiency.

**NCIT (contextual):** NCIT therapeutic-procedure concepts are not applicable to an untreated benign trait.

---

## Prevention (Section 13)

- **Primary/secondary/tertiary prevention, immunization, prophylaxis, behavioral/public-health interventions:** **not applicable** — the condition is benign, congenital, and non-preventable.
- **Genetic counseling.** The only meaningful preventive action. Counsel that the trait is autosomal recessive, benign, and does not cause bleeding; clarify the distinction from HAE-KNG1 and from true bleeding disorders; offer cascade testing for diagnostic clarity and to prevent future misinterpretation of aPTT results. Prenatal/preimplantation testing is generally unwarranted given the benign phenotype.

---

## Other Species / Natural Disease (Section 14)

- **Taxonomy / orthologs.** *Homo sapiens* (NCBI Taxon 9606), KNG1. Mouse ortholog **Kng1** (*Mus musculus*, NCBI Taxon 10090) is the principal experimental model. Rat *Kng1* also exists.
- **Natural disease in animals.** No well-characterized naturally occurring HK-deficiency disease of veterinary importance is established in the reviewed literature. The relevant animal data are **engineered knockouts**, not natural disease.
- **Comparative biology / evolutionary conservation.** The contact system and HK's cofactor role are conserved across mammals, and the hemostasis-sparing, thrombosis-promoting role of HK is reproduced in mouse knockouts (see Model Organisms). No zoonotic/transmission relevance (non-infectious Mendelian trait).

---

## Model Organisms (Section 15)

**Mouse (*Kng1*-knockout) is the key model**, and it faithfully recapitulates the human paradox — **no bleeding, but protection from thromboinflammatory disease**:

- **Ischemic stroke (tMCAO).** *"Kng(-/-) mice of either sex subjected to transient middle cerebral artery occlusion developed dramatically smaller brain infarctions and less severe neurologic deficits without an increase in infarct-associated hemorrhage."* ([PMID: 22936662](https://pubmed.ncbi.nlm.nih.gov/22936662/)). The authors conclude HK *"appears to be instrumental in pathologic thrombus formation and inflammation but dispensable for hemostasis."* Reconstitution with human KNG or bradykinin restored clot deposition and infarct susceptibility.

- **Experimental cerebral malaria (ECM).** *"HK-null (Kng1-/-), combined BK B1- and B2 receptor-null (Bdkrb1-/-Bdkrb2-/-), BK B2 receptor-null (Bdkrb2-/-), or BK B1 receptor-null (Bdkrb1-/-) mice were protected significantly from neurologic deterioration and brain edema compared with wild-type mice."* ([PMID: 42446942](https://pubmed.ncbi.nlm.nih.gov/42446942/)). Notably, *F12-/-* mice were **not** protected, implicating an **FXII-independent, PRCP-driven bradykinin pathway**; cleaved HK was elevated in children with CNS malaria (40%) vs uncomplicated malaria (18%).

**Model types available.** Constitutive knockout (*Kng1-/-*), plus pathway-adjacent knockouts (*Klkb1-/-* prekallikrein, *F12-/-*, bradykinin-receptor nulls, PRCP-deficient). **Recapitulation:** excellent for the hemostasis-sparing phenotype and the thromboinflammatory/bradykinin biology. **Limitations:** mice model disease *challenge* phenotypes (stroke, malaria) rather than the human "incidental lab finding"; human truncating alleles are modeled as full knockouts. **Resources:** MGI (Kng1), IMPC/IMSR.

---

## Mechanistic Model / Interpretation

```
 Biallelic truncating KNG1 variant (nonsense/frameshift)
            │  (loss of full-length HK; D5/D6 removed)
            ▼
 No HK cofactor in plasma
            │
   ┌────────┴─────────────────────────────┐
   ▼                                        ▼
 Cannot scaffold PK & FXI            Cannot bind anionic surface /
 on surface (D6 lost)                gC1qR endothelial receptor (D5 lost)
   │                                        │
   ▼                                        ▼
 Secondary ↓PK, ↓FXI             FXII contact activation fails (in vitro)
   │                                        │
   └──────────────┬─────────────────────────┘
                  ▼
        Intrinsic pathway not initiated in aPTT assay
                  │
                  ▼
        ►► ISOLATED PROLONGED aPTT (normal PT, corrects on mixing)
                  │
     ┌────────────┴───────────────┐
     ▼                             ▼
 BRANCH A: Hemostasis          BRANCH B: Thromboinflammation
 unaffected (TF/FVIIa          ↓bradykinin, ↓contact thrombosis
 extrinsic intact)             → PROTECTIVE in stroke / ECM (mouse)
     │                             │
     ▼                             ▼
 NO BLEEDING                   Benign (even favorable) course
```

**Synthesis.** The entire clinical picture flows from one fact: the **contact system is a thrombo-*inflammatory* amplifier, not a hemostatic necessity**. Removing its central cofactor (HK) therefore scrambles a laboratory test (aPTT) that *reports on* contact activation, while leaving the patient entirely well. The same lesion that abolishes the aPTT's intrinsic trigger also removes a driver of pathological thrombosis and bradykinin-mediated edema — which is why knockout mice are protected. KNG1's dual phenotype crystallizes the logic: **lose the protein (truncation) → benign deficiency; dysregulate the pathway toward excess bradykinin (missense) → hereditary angioedema.**

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/) | *Severe HMW kininogen deficiency: clinical characteristics, KNG1 variants, prevalence* | **Keystone**: 48 cases/41 families, 10 truncating variants, ~1/8M prevalence, asymptomatic, truncating-vs-missense dichotomy |
| [32185598](https://pubmed.ncbi.nlm.nih.gov/32185598/) | *Homozygous c.1456C>T nonsense in a Chinese family* | Confirms <1% HK activity, asymptomatic proband, nonsense variant |
| [24492696](https://pubmed.ncbi.nlm.nih.gov/24492696/) | *Novel exon-4 frameshift; splenic infarction* | Novel truncating variant; anecdotal thrombotic co-occurrence |
| [31858768](https://pubmed.ncbi.nlm.nih.gov/31858768/) | *First Korean case, c.488delG* | Additional truncating variant |
| [3574180](https://pubmed.ncbi.nlm.nih.gov/3574180/) | *Fitzgerald factor deficiency in an Australian Aboriginal* | Population/consanguinity context |
| [40638675](https://pubmed.ncbi.nlm.nih.gov/40638675/) | *Structure and interactions of contact-system proteins* | HK as dual cofactor/substrate; two downstream arms |
| [32559765](https://pubmed.ncbi.nlm.nih.gov/32559765/) | *FXII/kininogen assembly with gC1qR* | HKD5–gC1qR binding; 500-kDa ternary complex; domain architecture |
| [22936662](https://pubmed.ncbi.nlm.nih.gov/22936662/) | *Kininogen deficiency protects from ischemic neurodegeneration* | Mouse stroke protection, hemostasis-sparing |
| [42446942](https://pubmed.ncbi.nlm.nih.gov/42446942/) | *Bradykinin in murine cerebral malaria* | Second model of Kng1-/- protection; FXII-independent PRCP route |
| [35196732](https://pubmed.ncbi.nlm.nih.gov/35196732/) | *An update on safe anticoagulation* | Contact-system loss not associated with bleeding → benign prognosis + drug-target rationale |
| [42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/) | *Normal TEG with prolonged aPTT in PK deficiency* | Diagnostic analogue: mixing studies, normal viscoelastic testing |
| [40125216](https://pubmed.ncbi.nlm.nih.gov/40125216/) | *Severe PK deficiency as isolated aPTT prolongation* | No prophylactic blood products needed |
| [39773511](https://pubmed.ncbi.nlm.nih.gov/39773511/) | *Advances in HAE pathogenesis* | KNG1 as an HAE gene (missense) — the opposite phenotype |
| [36609679](https://pubmed.ncbi.nlm.nih.gov/36609679/) | *HAE diagnosis & pathophysiology* | Context for HAE-KNG1 classification |
| [42057602](https://pubmed.ncbi.nlm.nih.gov/42057602/) | *Garadacimab for HAE prophylaxis* | Contact-system inhibition as safe antithrombotic/anti-angioedema strategy |

**Source types:** human clinical (case reports, systematic review, diagnostic series), model organism (mouse knockouts), and structural/in-vitro (gC1qR assembly). The findings are concordant across all three.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** Only ~48 reported cases worldwide; prevalence (~1/8M) is a gnomAD-derived estimate, not a measured incidence. Rare phenotypes could be under-ascertained because the condition is asymptomatic.
2. **Anecdotal event reports.** Thrombosis (splenic infarction) and a leukaemia association appear in single case reports; causality is unestablished and likely coincidental.
3. **Protective effect is model-derived.** The antithrombotic/anti-inflammatory benefit of HK loss is robust in mice but **not quantified in humans**; whether HK-deficient people have measurably lower stroke/thrombosis risk is unknown.
4. **No human natural-history cohort, QoL data, or registry.** Longitudinal human data are absent.
5. **Genotype–phenotype granularity.** All deficiency alleles are truncating, but position-specific effects (e.g., HK-selective vs total kininogen deficiency) are incompletely mapped.
6. **No veterinary natural disease** characterized; animal evidence is engineered.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international HK-deficiency registry** to capture natural history, thrombotic/bleeding events, pregnancy outcomes, and surgical experiences across more than the current 48 cases.
2. **Quantify thrombotic risk in carriers/homozygotes** via case–control or Mendelian-randomization analyses using KNG1 LOF alleles in large biobanks (UK Biobank, gnomAD-linked cohorts) to test whether the murine protection translates to humans.
3. **Standardize the diagnostic algorithm** distinguishing HK, PK, and FXII deficiencies (reflex specific-factor assays + mixing with factor-depleted plasmas + normal TEG) and disseminate to coagulation laboratories to prevent iatrogenic harm.
4. **Map genotype–phenotype** for HK-selective vs total kininogen deficiency by correlating variant position (shared heavy chain vs HK-specific light chain) with residual LK and clinical features.
5. **Mechanistic dissection of the FXII-independent (PRCP) bradykinin route** suggested by the ECM model, to clarify which contact-system node is the safest therapeutic target.
6. **Counseling materials** emphasizing benign prognosis and the KNG1 truncation-vs-missense (deficiency vs HAE) distinction, for hematologists and genetic counselors.

---

*Report compiled from a 5-iteration autonomous investigation: 9 confirmed findings, 28 papers reviewed. All quoted abstract text is verbatim from the cited PMIDs.*


## Artifacts

- [OpenScientist final report](Congenital_High-molecular-weight_Kininogen_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_High-molecular-weight_Kininogen_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009234` (2 mentions) - the report calls it "MONDO"; MONDO calls it **congenital high-molecular-weight kininogen deficiency**
- `HP:0011897` (1 mention) - the report calls it "Abnormal prekallikrein"; HP calls it **Increased total neutrophil count**
- `HP:0004863` (1 mention) - the report calls it "Abnormality of coagulation factor XI"; HP calls it **Compensated hemolytic anemia**
- `GO:0002542` (1 mention) - the report calls it "bradykinin biosynthetic process"; GO calls it **Factor XII activation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names
- `GO:0009897` (1 mention) - the report calls it "external side of plasma membrane, via gC1qR"; GO calls it **external side of plasma membrane**