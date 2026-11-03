---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T04:00:04.467514'
end_time: '2026-10-31T04:29:02.433577'
duration_seconds: 1737.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 16
  mondo_id: MONDO:0014961
  category: Mendelian
  causal_genes: SUN5
  omim_id: OMIM:617187
  synonyms: spermatogenic failure 16; SPGF16; spermatogenic failure type 16; SPGF16;
    SUN5 azoospermia; azoospermia caused by mutation in SUN5
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
citation_count: 14
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 13
  quotes_valid: 9
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:27640305
  - PMID:34159570
  - PMID:25775128
  - PMID:34393249
  relevance_assessed: 16
  on_topic: 16
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0014961
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure 16
  - term_id: HP:0012874
    reported_labels:
    - Abnormal sperm morphology
    - Laboratory abnormality
    ontology_label: Abnormal male reproductive system physiology
  - term_id: NCIT:C92531
    reported_labels:
    - Intracytoplasmic Sperm Injection
    ontology_label: ARID1A wt Allele
  - term_id: NCIT:C15417
    reported_labels:
    - Genetic Counseling
    ontology_label: Randomized Clinical Trial
  labels_variant: 3
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spermatogenic_Failure_16-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spermatogenic_Failure_16-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 16
- **MONDO ID:** MONDO:0014961 (if available)
- **Causal gene(s):** SUN5
- **OMIM:** OMIM:617187
- **Synonyms:** spermatogenic failure 16; SPGF16; spermatogenic failure type 16; SPGF16; SUN5 azoospermia; azoospermia caused by mutation in SUN5
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 16** covering all of the
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

# Spermatogenic Failure 16 (SPGF16) — Comprehensive Disease Report

**Disease:** Spermatogenic Failure 16 (SPGF16) · **Causal gene:** *SUN5* (SPAG4L / TSARG4)
**OMIM:** 617187 · **MONDO:** MONDO:0014961 · **HGNC:** HGNC:16252 · **Category:** Mendelian (autosomal recessive)

---

## Summary

**Spermatogenic Failure 16 (SPGF16) is a non-syndromic, autosomal-recessive form of male infertility caused by biallelic loss-of-function variants in *SUN5* (also named SPAG4L or TSARG4), a testis-specific inner-nuclear-membrane LINC-complex protein.** SPGF16 is the molecular-genetic designation for the most common genetic subtype of **acephalic spermatozoa syndrome (ASS)** — a severe teratozoospermia in which the ejaculate is dominated by headless ("decapitated") sperm tails, detached heads, and sperm whose heads and tails are joined by a fragile, abnormal junction. *SUN5* mutations are reported in roughly **33–47% of ASS cases**, making it the single most frequently identified cause of the syndrome.

Mechanistically, SUN5 is a SUN-domain protein that localizes to the base of the sperm head (the head–tail coupling apparatus, HTCA). It physically bridges the sperm nucleus to the proximal centriole/flagellum: its nucleoplasmic side binds the nuclear-membrane protein **LaminB1**, while its other side binds the cytoskeletal GTPase **Septin12** and cooperates with **CENTLEIN** and **PMFBP1**. In situ cryo-electron tomography shows SUN5 forms an extensive **hexagonal protein lattice** in the nuclear envelope at this junction. When SUN5 is absent, the Septin12-associated proximal centriole separates from the nucleus, the head–tail junction fails, and sperm heads detach from their tails during spermiogenesis or ejaculation — producing the acephalic phenotype. *Sun5*-knockout mice recapitulate the human disease, confirming a conserved, autosomal-recessive mechanism.

Clinically, SPGF16 presents as isolated primary male infertility. Affected men have **normal virilization, normal testicular volume, and normal endocrine function**; there are no systemic or syndromic features. Diagnosis rests on semen analysis and sperm morphology (H&E staining, transmission electron microscopy showing head–tail junction defects) confirmed by *SUN5* sequencing (WES/Sanger) and absent SUN5 protein on immunofluorescence/Western blot. Because the defect is purely structural and the detached heads frequently contain intact genetic material, **intracytoplasmic sperm injection (ICSI) is an effective treatment**, with reported fertilization, embryo, and pregnancy rates that are favorable (one cohort: 81.5% fertilization, 81.8% good-quality embryos, 100% pregnancy among SUN5 patients). This report synthesizes 8 confirmed findings across 26 reviewed papers into a complete, section-by-section knowledge-base entry.

---

## 1. Disease Information

**Overview.** SPGF16 is a Mendelian, autosomal-recessive male infertility disorder. It is the genetic-nomenclature label (OMIM phenotype series "Spermatogenic failure") for *SUN5*-related **acephalic spermatozoa syndrome (ASS)**, a rare and severe teratozoospermia defined by a predominance of headless spermatozoa in the ejaculate. ASS is described as "a severe teratospermia with decaudated, decapitated, and malformed sperm, resulting in male infertility" ([PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 617187 (Spermatogenic failure 16) |
| MONDO | MONDO:0014961 |
| Causal gene | *SUN5* (HGNC:16252; NCBI Gene 140732; Ensembl ENSG00000167098; UniProt Q8TC36) |
| Gene OMIM | *SUN5* 613942 |
| ICD-10 | N46 (male infertility) — no SPGF16-specific code |
| ICD-11 | GB04 (male infertility) — no specific code |
| MeSH | Closest: "Infertility, Male"; "Teratozoospermia" |

**Synonyms:** spermatogenic failure 16; SPGF16; spermatogenic failure type 16; SUN5 azoospermia; azoospermia caused by mutation in SUN5; *SUN5*-related acephalic spermatozoa syndrome; acephalic spermatozoa syndrome (ASS, when SUN5-caused); headless spermatozoa.

**Information source.** The knowledge base here is derived from **aggregated disease-level resources** (OMIM, MONDO, gnomAD) plus **individual-patient case reports and small cohort studies** (WES-based gene discovery and ICSI outcome cohorts, predominantly from China). There is no large EHR-derived dataset; the evidence is primarily case-level clinical/genetic literature plus mouse models.

---

## 2. Etiology

**Primary cause — genetic.** SPGF16 is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *SUN5***. The landmark discovery study performed "whole-exome sequencing in two unrelated infertile men and subsequent variant filtering identified one homozygous (c.824C>T [p.Thr275Met]) and one compound heterozygous (c.1006C>T [p.Arg356Cys] and c.485T>A [p.Met162Lys]) SUN5 (also named TSARG4) variants" ([PMID: 27640305](https://pubmed.ncbi.nlm.nih.gov/27640305/)). *SUN5* is the most frequently identified ASS cause: "Mutations in the SUN5 gene have been identified most frequently (33-47%) in ASS cases" ([PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)).

**Genetic risk factors.** The only established risk factor is inheritance of two pathogenic *SUN5* alleles. **Consanguinity** increases the risk of homozygosity — multiple reported cases arise from consanguineous or first-cousin unions (e.g., two infertile brothers of first-cousin parents, [PMID: 40977202](https://pubmed.ncbi.nlm.nih.gov/40977202/)). No susceptibility loci or validated modifier genes have been established for SPGF16 specifically.

**Environmental risk factors.** None established. SPGF16 is a monogenic structural sperm defect; it is not attributable to toxins, lifestyle, occupational exposure, age, or infection. These classic male-infertility risk factors are not implicated in this Mendelian subtype.

**Protective factors.** None identified. Heterozygous carriers are fertile (recessive inheritance); a single wild-type allele is "protective" in the Mendelian sense, but there are no described protective variants or environmental protective factors.

**Gene–environment interactions.** No gene–environment interaction has been documented for SPGF16. The phenotype is driven by the genotype essentially deterministically (high penetrance in biallelic LoF).

---

## 3. Phenotypes

SPGF16 is **non-syndromic**: the phenotype is confined to the reproductive system. Affected men present with primary infertility and otherwise normal health.

| Phenotype | Type | HPO term (suggested) | Characteristics |
|---|---|---|---|
| Male infertility | Clinical sign | HP:0003251 (Male infertility) | Post-pubertal/congenital onset; severe; stable; ~100% of affected men |
| Acephalic/headless spermatozoa | Laboratory (semen) abnormality | HP:0012874 (Abnormal sperm morphology) / teratozoospermia | Predominant finding; severe |
| Abnormal sperm head–tail junction | Laboratory abnormality | HP:0012874 | Fragile junction in the minority of "intact" sperm |
| Asthenozoospermia / abnormal motility | Laboratory abnormality | HP:0008669 (Abnormal spermatogenesis) | Detached tails may retain motility; whole-sperm motility impaired |
| Normal external genitalia / testicular volume | Normal finding (exclusionary) | — | Documented normal exam |
| Normal endocrine/hormonal profile | Normal finding | — | FSH/LH/testosterone typically normal |

Clinical documentation: "Male external genitalia developed normally, bilateral testicles were normal in volume, and bilateral epididymis and spermatic vein were palpated without nodules, cysts, and tenderness. Repeated semen analysis showed that a large number of immature sperm could be seen, and they had the ability to move" ([PMID: 34393249](https://pubmed.ncbi.nlm.nih.gov/34393249/)). The core teratozoospermia is "decaudated, decapitated, and malformed sperm" ([PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)).

**Onset / severity / progression / frequency.** Onset is effectively **congenital** at the cellular level but **manifests post-pubertally** as infertility when reproduction is attempted. Severity is high (near-absolute natural infertility). The condition is **stable and non-progressive** — it does not worsen over time nor cause systemic morbidity. Frequency of the acephalic phenotype among affected men approaches 100% of sperm being abnormal.

**Quality-of-life impact.** The impact is confined to **reproductive function and its psychosocial consequences** (infertility-related distress, family planning burden). There is no physical disability, pain, or reduced life expectancy. No disease-specific QoL instrument (EQ-5D/SF-36) data exist for SPGF16; impact is inferred from the general infertility literature.

---

## 4. Genetic / Molecular Information

**Causal gene.** *SUN5* (Sad1 and UNC84 domain containing 5), aliases **SPAG4L** and **TSARG4**. HGNC:16252; NCBI Gene 140732; Ensembl ENSG00000167098; chromosome **20q11.21** (GRCh38 chr20:32,983,773–33,004,433); **13 exons**; **377-amino-acid** protein (UniProt Q8TC36); reference transcript **NM_080675**. *SUN5* encodes a testis-specific SUN-domain nuclear-envelope protein and a member of the LINC (Linker of Nucleoskeleton and Cytoskeleton) complex.

**Pathogenic variant spectrum.** Variants span **missense, frameshift, nonsense, splice-site, and large structural deletions**. Representative pathogenic alleles and their gnomAD v4 exome allele frequencies:

| Variant (cDNA) | Protein | Class | gnomAD v4 AF |
|---|---|---|---|
| c.381del | p.Val128SerfsTer7 | Frameshift (recurrent, most common) | 3.97×10⁻⁵ (AC 58) |
| c.824C>T | p.Thr275Met | Missense | 1.78×10⁻⁵ |
| c.1066C>T | p.Arg356Cys | Missense | 1.73×10⁻⁵ |
| c.1067G>A | p.Arg356His | Missense | 8.3×10⁻⁶ |
| c.1043A>T | p.Asn348Ile | Missense | 1.87×10⁻⁵ |
| c.775G>A | p.Gly259Ser | Missense | 5.5×10⁻⁶ |
| c.340G>A | p.Gly114Arg | Missense | 2.7×10⁻⁶ |
| c.1072C>T | p.Arg358Ter | Nonsense | 6.9×10⁻⁶ |
| c.485T>A | p.Met162Lys | Missense | — |
| c.1006C>T | p.Arg356Cys | Missense | — |
| c.829C>T | p.Gln277* | Nonsense | — |
| c.211+1insGT | splice | Splice-site | — |
| c.879dupC | p.(fs) | Frameshift | — |
| c.1073G>A | p.Arg358Gln | Missense | — |
| Large deletion (partial *EFCAB8*/*BPIFB2* + complete *SUN5*) | — | Structural (CNV) | — |

The structural deletion was reported alongside a novel missense allele: "one novel homozygous missense mutation (c.775G>A; p.G259S) and one compound heterozygous including one reported missense mutation (c.1043A>T; p.N348I) and a large deletion that contains partial EFCAB8 … and BPIFB2 … and complete SUN5 (NM_080675)" ([PMID: 34159570](https://pubmed.ncbi.nlm.nih.gov/34159570/)). Additional alleles include the homozygous c.879dupC frameshift ([PMID: 40977202](https://pubmed.ncbi.nlm.nih.gov/40977202/)) and homozygous c.1073G>A (p.Arg358Gln) ([PMID: 40740627](https://pubmed.ncbi.nlm.nih.gov/40740627/)).

**Variant classification (ACMG/AMP).** Pathogenic/likely pathogenic for biallelic LoF and recurrent hotspot missense alleles (notably codon 356/358). Classification criteria typically invoked: PVS1 (null variants), PM2_Supporting (rare in gnomAD), PP4 (phenotype match), PM3 (recessive, in trans), and functional evidence (absent sperm SUN5).

**Allele frequency / origin.** All pathogenic alleles are **rare germline** variants at carrier-level frequencies (AF ≤ ~4×10⁻⁵). None are somatic. The recurrent frameshift c.381del is the most common.

**Functional consequence.** **Loss of function** — mutations abolish or destabilize SUN5 protein, eliminating the nucleus-to-flagellum anchor. Patient sperm show absent SUN5 on immunostaining/Western blot.

**Constraint.** gnomAD v4 shows *SUN5* is **LoF-tolerant** (pLI ≈ 0; observed/expected LoF = 0.82; LOEUF = 1.05; mis_z = 0.98; lof_z = 1.13). There is no depletion of heterozygous LoF alleles — exactly as expected for a gene whose only essential function is in recessive male fertility (gnomAD v4; context in [PMID: 34159570](https://pubmed.ncbi.nlm.nih.gov/34159570/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated modifier genes. No disease-specific epigenetic mechanism described (SUN5 participates in nuclear mRNA recruitment/export in spermatogenesis, [PMID: 39108207](https://pubmed.ncbi.nlm.nih.gov/39108207/), but this is a normal function, not an epigenetic disease mechanism). The only "chromosomal abnormality" relevant is the large CNV deletion encompassing *SUN5* noted above.

---

## 5. Environmental Information

**Environmental factors:** None established. SPGF16 is a monogenic disorder; toxins, radiation, and pollution are **not applicable**.
**Lifestyle factors:** None established (smoking, diet, alcohol are not causal for this Mendelian subtype).
**Infectious agents:** **Not applicable** — no infectious trigger.

This section is essentially negative: SPGF16 is a purely genetic, structural sperm defect.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic LoF mutation in *SUN5*** → **leads to** loss or destabilization of the testis-specific SUN-domain protein SUN5 in developing male germ cells (demonstrated: absent SUN5 on patient sperm immunostaining).
2. **Absence of SUN5 at the sperm-head base** → **results in** failure to assemble the nuclear-envelope hexagonal lattice and head–tail coupling apparatus (HTCA) during spermiogenesis (demonstrated by cryo-ET; [PMID: 41855266](https://pubmed.ncbi.nlm.nih.gov/41855266/)).
3. **Loss of the LaminB1–SUN5–Septin12 bridge** → **leads to** separation of the Septin12-associated proximal centriole from the nucleus (demonstrated in *Sun5*-KO mice; [PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)).
4. **Breakage of the head-to-tail junction** → **results in** mechanical uncoupling of the sperm head from the flagellum.
5. **During spermiogenesis/epididymal transit/ejaculation** → the fragile or absent junction **causes** the head and tail to detach → **acephalic (headless) spermatozoa** and detached heads in the ejaculate.
6. **Headless/malformed sperm cannot fertilize an oocyte naturally** → **results in** primary male infertility (the clinical manifestation of SPGF16).

**Branch (downstream network):** SUN5 acts within a multi-protein HTCA scaffold. The adaptor **CENTLEIN** links SUN5 to **PMFBP1**; in its absence "the absence of Centlein sets SUN5 and PMFBP1 apart, the former close to the sperm head and the latter in the decapitated tail" ([PMID: 34389728](https://pubmed.ncbi.nlm.nih.gov/34389728/)). Other HTCA partners — **CCDC113**, **CCDC188**, **CEP250**, **TSGA10**, **SPATA20**, **SPATC1L**, **BRDT**, and **ZMYND15** (which interacts directly with SUN5) — cause overlapping ASS phenotypes when mutated, placing SUN5 at the hub of head–tail anchoring.

### Mechanistic detail

- **Molecular pathways / complex:** LINC complex (SUN–KASH), nuclear-envelope–cytoskeleton coupling. SUN5 "connected the nucleus by interacting with LaminB1 and connected the proximal centriole by interacting with Septin12. The binding between SUN5 and Septin12 promoted their aggregation together in the sperm neck. The disruption of the LaminB1/SUN5/Septin12 complex by Sun5 deficiency caused separation of the Septin12-proximal centriole from the nucleus, leading to the breakage of the head-to-tail junction" ([PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)).
- **Cellular processes:** Spermiogenesis — nuclear-envelope remodeling, implantation-fossa/basal-plate formation, centriole–nucleus tethering. SUN5 dynamically relocates during germ-cell development: "In pachytene spermatocytes, it is located in a membranous compartment… In round spermatids, it progresses to the Golgi and the NE before to be located to the tail/head junction in epididymal sperm… Sun5 is not, as initially reported, facing the acrosome but is in fact excluded from this zone" ([PMID: 25775128](https://pubmed.ncbi.nlm.nih.gov/25775128/)).
- **Protein dysfunction:** Loss of function of a SUN-domain transmembrane protein; truncating and destabilizing missense alleles eliminate the functional anchor. Structural data: "sperm-specific SUN5 localizes to the base of the head in human, mouse, and boar sperm. By applying in situ cryoelectron tomography, we find an extensive hexagonal lattice in the nuclear envelope in this region" ([PMID: 41855266](https://pubmed.ncbi.nlm.nih.gov/41855266/)).
- **Tissue damage mechanism:** Mechanical failure (not inflammatory/ischemic) — the head–tail junction physically fractures.
- **Immune / metabolic involvement:** None.

### Ontology suggestions

- **GO (biological process):** GO:0007283 spermatogenesis; GO:0007286 spermatid development; GO:0048515 spermatid differentiation; GO:0007097 nuclear migration; LINC-complex / nuclear-membrane tethering.
- **GO (cellular component):** GO:0005637 nuclear inner membrane; GO:0005635 nuclear envelope; GO:0034993 (SUN–KASH / LINC); sperm neck / head–tail coupling apparatus.
- **CL (cell type):** CL:0000018 spermatid; CL:0000017 spermatocyte; CL:0000019 sperm; CL:0000015 male germ cell.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Testis (UBERON:0000473) — specifically the seminiferous tubules (UBERON:0001343) where spermiogenesis occurs; and the spermatozoon itself (UBERON:0000408 / CL:0000019). **Secondary:** none — no other organ is affected.
- **Body system:** Male reproductive system (UBERON:0000079) only.
- **Tissue / cell level:** Germinal epithelium of the seminiferous tubule; affected cells are **spermatids and spermatozoa** (CL:0000018 spermatid; CL:0000019 sperm). Somatic Sertoli/Leydig cells and the endocrine axis are unaffected (normal testosterone/testicular volume).
- **Subcellular level:** The lesion is at the **sperm head–tail coupling apparatus / neck**, at the interface of the **nuclear envelope / inner nuclear membrane** (GO:0005637), the **implantation fossa (basal plate)** of the nucleus, and the **proximal centriole**. GO cellular components: nuclear inner membrane (GO:0005637), nuclear envelope (GO:0005635).
- **Localization:** Site = base of the sperm head / sperm neck; systemic to essentially all sperm (not a lateralized anatomical defect). UBERON: sperm (UBERON:0000408); testis (UBERON:0000473).

---

## 8. Temporal Development

- **Onset:** Congenital at the molecular/cellular level (the defect is present from first spermatogenesis at puberty); **clinically recognized in adulthood** when infertility is investigated. Onset pattern is **chronic/insidious** (silent until reproduction attempted).
- **Progression:** **Stable, non-progressive.** There are no disease stages; the sperm defect is constant across the reproductive lifespan. Disease course is a **chronic, lifelong** structural infertility with no spontaneous remission.
- **Critical period:** The vulnerable window is **spermiogenesis** (round-to-elongating spermatid stage) when the HTCA is built. There is no developmental window for correction; the therapeutic "window" is at **assisted reproduction (ICSI)**, which bypasses the defect.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Biallelic pathogenic variants are required; heterozygous carriers are fertile and asymptomatic. Consistent with gnomAD LoF-tolerance (pLI ≈ 0).
- **Penetrance:** Effectively **complete** for the sperm phenotype in biallelic LoF individuals.
- **Expressivity:** Relatively consistent (acephalic spermatozoa), though the proportion of headless vs. fragile-junction vs. malformed sperm varies between individuals.
- **Epidemiology:** ASS overall is **rare** (no precise prevalence/incidence figures; considered a rare form of severe teratozoospermia). Within ASS, *SUN5* accounts for **33–47%** of cases ([PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)). No cases-per-100,000 estimate is available.
- **Consanguinity / founder effects:** Consanguinity elevates homozygosity risk; several reported families are consanguineous. No classical founder haplotype is established, though the recurrent c.381del frameshift is the most common allele in gnomAD.
- **Carrier frequency:** Individual pathogenic alleles are rare (AF ≤ ~4×10⁻⁵); aggregate carrier frequency is low but non-trivial given allelic heterogeneity.
- **Population demographics:** Most reported cohorts are **Han Chinese**, reflecting study ascertainment rather than proven ethnic predilection; cases also reported from Iran and elsewhere. **Sex:** affects males only (a reproductive phenotype); the genotype can be carried by either sex. **Age distribution:** reproductive-age men.

---

## 10. Diagnostics

**Clinical / laboratory workup:**
- **Semen analysis + sperm morphology** (H&E staining): predominance of headless tails, detached heads, and malformed sperm; "a large number of immature sperm… they had the ability to move" ([PMID: 34393249](https://pubmed.ncbi.nlm.nih.gov/34393249/)).
- **Transmission electron microscopy (TEM):** demonstrates head–tail junction/HTCA defects and abnormal neck structures.
- **Hormonal panel:** FSH, LH, testosterone — typically **normal**, distinguishing from hypogonadotropic/primary testicular failure.
- **Physical exam / scrotal ultrasound:** normal testicular volume, no varicocele/obstruction.
- **Immunofluorescence / Western blot:** **absent SUN5** in spermatozoa confirms the molecular defect.

**Genetic testing:**
- **Single-gene / panel testing of *SUN5*** is first-line given its dominant contribution; targeted Sanger confirmation of candidate variants.
- **Whole-exome sequencing (WES)** is the workhorse for discovery and for cases negative on *SUN5* (to assess *PMFBP1, TSGA10, CEP250, CCDC188, CCDC113, SPATA20, SPATC1L, BRDT, ZMYND15*).
- **CMA / CNV analysis** is warranted because large deletions encompassing *SUN5* occur ([PMID: 34159570](https://pubmed.ncbi.nlm.nih.gov/34159570/)).
- Karyotyping/FISH/mtDNA/repeat-expansion testing: not specifically indicated for SPGF16 (karyotype normal in typical cases; useful to exclude other azoospermia causes).

**Clinical criteria / differential diagnosis:** Diagnosis = morphological ASS + biallelic *SUN5*. Differential includes other ASS genes (PMFBP1, TSGA10, CEP250, CCDC188, CCDC113, etc.), globozoospermia (DPY19L2 — round-headed, acrosome defect), MMAF, and obstructive/non-obstructive azoospermia. SUN5 is distinguished by its specific role at the head–tail junction (not the acrosome; [PMID: 25775128](https://pubmed.ncbi.nlm.nih.gov/25775128/)) and its favorable ICSI prognosis.

**Screening:** No population newborn/carrier screening exists. **Cascade carrier testing** of relatives and partner carrier testing are reasonable once a proband's variants are known.

---

## 11. Outcome / Prognosis

- **Survival / mortality / morbidity:** SPGF16 has **no effect on survival, life expectancy, or physical health.** The only "morbidity" is **infertility** and its psychosocial burden.
- **Disease course:** Stable, lifelong infertility; no complications in the conventional medical sense.
- **Recovery / treatment response:** Natural fertility is essentially absent, but **ICSI yields favorable reproductive outcomes** (see Treatment). In a SUN5 cohort: "The rates of fertilization, good-quality embryos and pregnancy for five patients with SUN5 mutations following ICSI were 81.5%, 81.8% and 100%, respectively" ([PMID: 29329387](https://pubmed.ncbi.nlm.nih.gov/29329387/)).
- **Prognostic factors:** The genetic cause predicts ICSI prognosis — *SUN5* and *PMFBP1*/*TSGA10* generally carry **favorable** ICSI outcomes, whereas some genes (e.g., *SPATA20* loss of function, proximal-centriole-deficient *TSGA10*, certain *CEP250*/*CCDC188* cases) may give poorer outcomes. Notably, not all SUN5 ICSI attempts succeed — two ICSI cycles failed to achieve pregnancy in one c.879dupC case ([PMID: 40977202](https://pubmed.ncbi.nlm.nih.gov/40977202/)).

---

## 12. Treatment

**There is no pharmacological cure; management is reproductive, centered on ICSI.**

| Intervention | Role in SPGF16 | NCIT (suggested) | Evidence |
|---|---|---|---|
| **Intracytoplasmic sperm injection (ICSI)** | First-line; bypasses the structural defect by injecting a sperm head (or intact sperm) directly into the oocyte | NCIT:C92531 (Intracytoplasmic Sperm Injection) | Favorable outcomes ([PMID: 29329387](https://pubmed.ncbi.nlm.nih.gov/29329387/)) |
| **IVF with ICSI (ART)** | Framework for ICSI | NCIT:C19829 (In Vitro Fertilization) | — |
| **Genetic counseling** | Inform recurrence risk, carrier/partner testing | NCIT:C15417 (Genetic Counseling) | — |
| **Preimplantation genetic testing (optional)** | Consider when both partners carry risk alleles | — | — |

**Pharmacotherapy / pharmacogenomics:** Not applicable. **Gene/cell/RNA therapies:** None clinical; purely conceptual (the defect is germ-cell structural and not currently a gene-therapy target). **Surgical:** Sperm retrieval is generally unnecessary because sperm are present in the ejaculate (the problem is morphology, not count/azoospermia); standard ejaculate sperm are used for ICSI. **Experimental:** No SPGF16-specific registered trials identified.

**Treatment outcome nuance:** Because the detached head usually retains an intact nucleus, injecting it supports fertilization; however, selecting a sperm/head with an intact centriolar/genetic complement matters — mis-injection of a head plus detached tail produced fertilization failure in a related *CCDC188* case ([PMID: 41004021](https://pubmed.ncbi.nlm.nih.gov/41004021/)), underscoring the importance of gene-specific prognosis.

---

## 13. Prevention

- **Primary prevention:** Not possible (congenital genetic). **Genetic counseling** for consanguineous couples and families with affected relatives is the principal preventive measure.
- **Secondary prevention / screening:** **Carrier screening** of partners and **cascade testing** of relatives once a proband's *SUN5* genotype is defined; **preimplantation genetic testing (PGT)** and **prenatal testing** are options for couples at recurrence risk.
- **Tertiary prevention:** ICSI to achieve pregnancy; counseling that affected/carrier status may be transmitted depending on partner genotype.
- **Immunization / behavioral / public-health / environmental / prophylaxis measures:** Not applicable — no environmental or infectious component.
- **Counseling (ontology):** NCIT:C15417 Genetic Counseling.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *SUN5* has a mouse ortholog **Sun5** (NCBI Gene **76407**; MGI:**1923657**; Ensembl **ENSMUSG00000027480**). SUN5 protein localizes to the sperm-head base in **human, mouse, and boar (pig)** ([PMID: 41855266](https://pubmed.ncbi.nlm.nih.gov/41855266/)), indicating evolutionary conservation of its function across mammals.
- **Natural disease in other species:** No naturally occurring *SUN5* ASS has been catalogued in OMIA for companion animals/livestock; the boar data are experimental/structural, and mouse data are from engineered knockouts.
- **Comparative biology:** The mechanism (head–tail anchoring via a SUN-domain LINC protein) is conserved; mouse knockouts faithfully reproduce the human phenotype (see §15). One caveat: for some *other* ASS genes mouse and human phenotypes diverge (e.g., *CEP250* knock-in mice show azoospermia rather than classic ASS; [PMID: 39726222](https://pubmed.ncbi.nlm.nih.gov/39726222/)), but *SUN5* is concordant across species.
- **Transmission / zoonosis:** Not applicable.

---

## 15. Model Organisms

- **Model type:** Mammalian — **mouse (*Mus musculus*)** is the principal model.
- **Genetic models:** **Sun5-knockout mice** (constitutive null). At least two independent lines:
  - Shang et al., 2017, *eLife* — "Essential role for SUN5 in anchoring sperm head to the tail" ([PMID: 28945193](https://pubmed.ncbi.nlm.nih.gov/28945193/)).
  - Zhang et al., 2024 — "we generated Sun5 knockout mice, which presented the phenotype of ASS," used to map the LaminB1–SUN5–Septin12 bridge ([PMID: 38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/)).
- **Phenotype recapitulation:** **High** — Sun5-null males reproduce human acephalic spermatozoa syndrome (sperm heads detached from tails), validating the causal mechanism.
- **Limitations:** Mice do not model the ICSI-specific clinical outcome variability seen in humans; most lines are constitutive nulls rather than patient-variant knock-ins, so allele-specific (missense) effects are less explored.
- **Applications:** Dissecting HTCA assembly, SUN5 interaction partners (LaminB1, Septin12, CENTLEIN, PMFBP1), and nuclear-envelope lattice architecture.
- **Resources:** MGI (Sun5, MGI:1923657); IMPC/IMSR for availability.

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF in SUN5 (missense/frameshift/nonsense/splice/CNV)
          │  (loss of testis-specific SUN-domain protein)
          ▼
 No SUN5 at sperm-head base  ──►  Hexagonal NE lattice & HTCA fail to assemble
          │                                   (cryo-ET; PMID 41855266)
          ▼
 LaminB1 — SUN5 — Septin12 bridge disrupted
          │                         ├── CENTLEIN/PMFBP1 mis-sorted (PMID 34389728)
          ▼                         └── CCDC113/CCDC188/CEP250/ZMYND15 network destabilized
 Septin12–proximal centriole separates from nucleus  (PMID 38870534)
          ▼
 Head-to-tail junction breaks
          ▼
 Acephalic (headless) spermatozoa + detached heads in ejaculate
          ▼
 Primary male infertility  ──►  rescued by ICSI (favorable outcomes; PMID 29329387)
```

**Upstream vs downstream:** The initiating lesion (upstream) is the *SUN5* mutation; the most proximal molecular consequence is failure of the nuclear-envelope LINC bridge; downstream are the structural head–tail breakage and the clinical infertility. SUN5 is a **hub** — many ASS genes converge on the same HTCA, so SUN5 loss both directly breaks the bridge and indirectly mislocalizes partner proteins.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [27640305](https://pubmed.ncbi.nlm.nih.gov/27640305/) | *Biallelic SUN5 Mutations Cause Autosomal-Recessive Acephalic Spermatozoa Syndrome* | **Landmark** — establishes SUN5 causality; original variants |
| [38870534](https://pubmed.ncbi.nlm.nih.gov/38870534/) | *SUN5 interacts with LaminB1 and Septin12…* | Core mechanism; 33–47% ASS; KO mouse ASS |
| [41855266](https://pubmed.ncbi.nlm.nih.gov/41855266/) | *SUN5 forms a regular protein lattice…* | Cryo-ET hexagonal lattice; cross-species localization |
| [34389728](https://pubmed.ncbi.nlm.nih.gov/34389728/) | *The missing linker between SUN5 and PMFBP1…* | Places SUN5 in HTCA (CENTLEIN/PMFBP1) |
| [25775128](https://pubmed.ncbi.nlm.nih.gov/25775128/) | *Dynamics of Sun5 localization…* | Dynamic relocalization; excluded from acrosome |
| [28945193](https://pubmed.ncbi.nlm.nih.gov/28945193/) | *Essential role for SUN5 in anchoring sperm head to the tail* | Foundational KO mouse |
| [29329387](https://pubmed.ncbi.nlm.nih.gov/29329387/) | *…SUN5 mutations have a favorable pregnancy outcome from ICSI* | Treatment outcome data |
| [34159570](https://pubmed.ncbi.nlm.nih.gov/34159570/) | *Novel Mutation and Deletion in SUN5…* | Structural deletion; LoF-tolerant constraint |
| [34393249](https://pubmed.ncbi.nlm.nih.gov/34393249/) | *Genetic analysis of three ASS cases…* | Clinical exam/semen findings |
| [39108207](https://pubmed.ncbi.nlm.nih.gov/39108207/) | *SUN5… recruitment/export of nuclear mRNA* | Additional SUN5 function |
| [40977202](https://pubmed.ncbi.nlm.nih.gov/40977202/), [40740627](https://pubmed.ncbi.nlm.nih.gov/40740627/) | Novel SUN5 variants (c.879dupC; c.1073G>A) | Expand variant spectrum; variable ICSI outcome |
| [42522282](https://pubmed.ncbi.nlm.nih.gov/42522282/), [39671309](https://pubmed.ncbi.nlm.nih.gov/39671309/), [41004021](https://pubmed.ncbi.nlm.nih.gov/41004021/), [39726222](https://pubmed.ncbi.nlm.nih.gov/39726222/) | ZMYND15/CCDC113/CCDC188/CEP250 ASS genes | Context: SUN5 as HTCA hub; differential genes |

**Consistency:** All primary sources converge — SUN5 is the most common ASS gene, acts at the head–tail junction, is conserved in mouse models, and is ICSI-amenable. The principal nuance is **variable ICSI success** (most cohorts favorable; occasional failures), suggesting additional factors (e.g., centriole/genetic integrity of the injected head) modulate outcome.

---

## Limitations and Knowledge Gaps

1. **Ascertainment bias:** Most cohorts are Han Chinese and small; true population prevalence, ethnic distribution, and carrier frequencies are not precisely quantified.
2. **ICSI outcome heterogeneity:** Reported rates are favorable but based on few patients; occasional failures (e.g., [PMID: 40977202](https://pubmed.ncbi.nlm.nih.gov/40977202/)) indicate incomplete predictability. Prognostic biomarkers for ICSI success are undefined.
3. **Genotype–phenotype correlations:** Whether specific missense vs. truncating alleles predict ICSI prognosis or residual sperm quality is not resolved.
4. **Mechanistic completeness:** The full stoichiometry/architecture of the SUN5–LaminB1–Septin12–CENTLEIN–PMFBP1 complex and the exact developmental timing of junction failure are still being mapped.
5. **No standardized QoL or natural-history data** specific to SPGF16.
6. **Modifier genes/epigenetics:** None established; unexplored.

---

## Proposed Follow-up Experiments / Actions

1. **Multi-center ICSI outcome registry** for *SUN5* ASS, stratified by variant class, to define prognostic predictors and quantify fertilization/live-birth rates with confidence intervals.
2. **Patient-variant knock-in mouse/organoid models** (e.g., p.Thr275Met, p.Arg356Cys) to test allele-specific effects beyond constitutive knockout.
3. **High-resolution structural studies** (cryo-ET/cryo-EM) of the complete HTCA lattice with and without SUN5 partners to refine the assembly model.
4. **Centriole/genome-integrity assessment of detached heads** to explain ICSI failures and develop sperm-selection criteria.
5. **Broaden population screening** (gnomAD-informed carrier panels) across diverse ancestries to estimate true carrier frequency and detect founder alleles.
6. **Functional validation pipeline** for VUS in *SUN5* (expression, localization, interaction assays) to support ACMG classification and clinical reporting.

---

*Report compiled from 8 confirmed findings across 26 reviewed primary and secondary sources. Evidence types: human clinical/genetic (case reports, WES cohorts, ICSI outcome studies), model organism (Sun5-KO mouse), in vitro (co-IP/IF/WB), and structural/computational (cryo-ET, gnomAD constraint).*


## Artifacts

- [OpenScientist final report](Spermatogenic_Failure_16-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spermatogenic_Failure_16-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 13 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 16 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27640305` *(abstract only)*: "whole-exome sequencing in two unrelated infertile men and subsequent variant filtering identified one homozygous (c.824C>T [p.Thr275Met]) and one compound heterozygous (c.1006C>T [p.Arg356Cys] and c.485T>A [p.Met162Lys]) SUN5 (also named TSARG4) variants"
  - closest text in source: "whole-exome sequencing in two unrelated infertile men and subsequent variant filtering identified one homozygous (c.824C>T [p.Thr275Met]) and one compound heterozygous (c.1006C>T [p.Arg356Cys] and c.485T>A [p.Met162Lys]) SUN5 (also named TSARG4) variants"
- `PMID:34159570` *(abstract only)*: "one novel homozygous missense mutation (c.775G>A; p.G259S) and one compound heterozygous including one reported missense mutation (c.1043A>T; p.N348I) and a large deletion that contains partial EFCAB8 … and BPIFB2 … and complete SUN5 (NM_080675)"
  - closest text in source: "We identified one novel homozygous missense mutation (c.775G>A; p.G259S) and one compound heterozygous including one reported missense mutation (c.1043A>T; p.N348I) and a large deletion that contains partial EFCAB8 ( NM_001143967 .1) and BPIFB2 ( NM_025227 ) and complete SUN5 ( NM_080675 ), and one recurrent homozygous splice-site mutation (c.340G>A; p.G114R) in SUN5 in three patients with ASS"
- `PMID:25775128` *(abstract only)*: "In pachytene spermatocytes, it is located in a membranous compartment… In round spermatids, it progresses to the Golgi and the NE before to be located to the tail/head junction in epididymal sperm… Sun5 is not, as initially reported, facing the acrosome but is in fact excluded from this zone"
  - closest text in source: "In round spermatids, it progresses to the Golgi and the NE before to be located to the tail/head junction in epididymal sperm"
- `PMID:34393249` *(abstract only)*: "a large number of immature sperm… they had the ability to move"
  - closest text in source: "Repeated semen analysis showed that a large number of immature sperm could be seen, and they had the ability to move"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014961` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure 16**
- `HP:0012874` (2 mentions) - the report calls it "Abnormal sperm morphology", "Laboratory abnormality"; HP calls it **Abnormal male reproductive system physiology**
- `NCIT:C92531` (1 mention) - the report calls it "Intracytoplasmic Sperm Injection"; NCIT calls it **ARID1A wt Allele**
- `NCIT:C15417` (2 mentions) - the report calls it "Genetic Counseling"; NCIT calls it **Randomized Clinical Trial**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005637` (3 mentions) - the report calls it "nuclear envelope / inner nuclear membrane"; GO calls it **nuclear inner membrane**
- `GO:0034993` (1 mention) - the report calls it "SUN–KASH / LINC"; GO calls it **meiotic nuclear membrane microtubule tethering complex**, and lists "SUN-KASH complex" among its other names
- `UBERON:0000079` (1 mention) - the report calls it "Body system:** Male reproductive system"; UBERON calls it **male reproductive system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012874` - called "Abnormal sperm morphology", "Laboratory abnormality"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.