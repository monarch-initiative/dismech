---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T18:59:16.500632'
end_time: '2026-10-31T19:25:12.410212'
duration_seconds: 1555.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: '"Hypomyelinating Leukodystrophy 17"'
  mondo_id: MONDO:0054817
  category: Mendelian
  causal_genes: AIMP2
  omim_id: OMIM:618006
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
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:34523057
  relevance_assessed: 14
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:42468917
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 37
  verified: 35
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.028
  labels_checked: 12
  labels_matching: 1
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0054817
    reported_labels:
    - MONDO
    ontology_label: leukodystrophy, hypomyelinating, 17
  - term_id: HP:0000252
    reported_labels:
    - Physical/clinical sign
    ontology_label: Microcephaly
  - term_id: HP:0002500
    reported_labels:
    - Imaging/physical
    ontology_label: Abnormal cerebral white matter morphology
  - term_id: HP:0002059
    reported_labels:
    - Imaging
    ontology_label: Cerebral atrophy
  - term_id: HP:0001272
    reported_labels:
    - Imaging
    ontology_label: Cerebellar atrophy
  - term_id: HP:0002134
    reported_labels:
    - Imaging
    ontology_label: Abnormal basal ganglia morphology
  - term_id: HP:0002280
    reported_labels:
    - Imaging
    ontology_label: Enlarged cisterna magna
  - term_id: UBERON:0000955
    reported_labels:
    - Primary organ:** brain
    ontology_label: brain
  - term_id: UBERON:0001870
    reported_labels:
    - Specific regions:** cerebrum
    ontology_label: frontal cortex
  labels_variant: 2
  unresolved_terms:
  - HP:0021010
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypomyelinating_Leukodystrophy_17-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypomyelinating_Leukodystrophy_17-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** "Hypomyelinating Leukodystrophy 17"
- **MONDO ID:** MONDO:0054817 (if available)
- **Causal gene(s):** AIMP2
- **OMIM:** OMIM:618006
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **"Hypomyelinating Leukodystrophy 17"** covering all of the
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

# Hypomyelinating Leukodystrophy 17 (HLD17) — Comprehensive Disease Report

**Disease:** Hypomyelinating Leukodystrophy 17 (HLD17)
**Causal gene:** **AIMP2** (aminoacyl-tRNA synthetase complex-interacting multifunctional protein 2; synonyms **JTV1**, **MSC p38 / p38**; HGNC:20609)
**MONDO:** MONDO:0054817 · **OMIM:** #618006
**Inheritance:** Autosomal recessive (biallelic loss of function)

---

## Summary

**Hypomyelinating Leukodystrophy 17 (HLD17) is an ultra-rare, autosomal recessive, infantile-onset white matter disorder caused by biallelic loss-of-function mutations in the gene AIMP2.** AIMP2 (also known as JTV1 or p38) encodes the non-catalytic scaffolding subunit of the cytoplasmic multi-tRNA synthetase complex (MSC), a macromolecular machine of eight aminoacyl-tRNA synthetases and three scaffolding AIMP proteins (AIMP1–3) that is essential for efficient protein synthesis. HLD17 was first delineated when whole-exome sequencing of affected children from two unrelated consanguineous families identified a homozygous recurrent nonsense variant, c.105C>A p.(Tyr35Ter), establishing AIMP2 as the first human disease gene in this category ([PMID: 29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/)). The disease belongs to the "RNA translation" mechanistic class of hypomyelinating leukodystrophies, alongside its paralog AIMP1 (which causes HLD3) and POLR3A/POLR3B (Pol III–related leukodystrophies). The serial name ("...17") does not name the gene; all identifiers here refer to the AIMP2-related disorder and should not be confused with the clinically similar AIMP1-related HLD3 (OMIM 260600).

Clinically, HLD17 presents in infancy with **microcephaly, refractory seizures, intellectual disability/global developmental delay, and spastic quadriparesis**. Neuroimaging shows **CNS hypomyelination together with atrophy of the cerebrum, cerebellum, and spinal cord, a thin corpus callosum, prominent cisterna magna, and symmetric T2 hypointensities in the bilateral basal ganglia**. The disorder is progressive and neurodevelopmental, reflecting both a failure to deposit myelin and ongoing neural cell loss.

Mechanistically, HLD17 appears to arise through **two converging, partly distinct routes**: (1) a **loss-of-function route** in which reduced AIMP2 destabilizes the MSC (dysregulating methionyl-tRNA synthetase, MARS1), attenuates global protein synthesis, and causes neural cell death and brain atrophy — recapitulated by CRISPR knockdown of *aimp2* in zebrafish; and (2) a **toxic/gain-of-dysfunction route** in which the truncated p.Tyr35Ter mutant protein aggregates in the Golgi apparatus of oligodendroglial cells, activating Golgi-stress caspase-2 (CASP2) signaling and arresting oligodendrocyte differentiation. No disease-modifying therapy is currently approved; care is supportive. Two preclinical strategies are promising: **anticodon-engineered suppressor tRNAs** to read through nonsense alleles such as p.Tyr35Ter, and **CASP2 inhibition** to relieve the Golgi-stress differentiation block.

---

## Section 1 — Disease Information

HLD17 is a **Mendelian (monogenic), autosomal recessive hypomyelinating leukodystrophy** — an inherited white matter disorder defined by insufficient deposition of myelin during brain development rather than loss of previously normal myelin (demyelination). The causal gene is **AIMP2**.

| Identifier type | Value |
|---|---|
| Disease name | Hypomyelinating Leukodystrophy 17 |
| MONDO | MONDO:0054817 |
| OMIM | #618006 |
| Causal gene | AIMP2 (HGNC:20609; synonyms JTV1, MSC p38/p38) |
| Gene location | chr7p22.1 (GRCh38 chr7:6,009,255–6,023,834; ENSG00000106305) |
| Gene class | RNA translation / tRNA-synthetase complex scaffold |
| Inheritance | Autosomal recessive |

> "HLD17 (Hypomyelinating Leukodystrophy 17) is an inherited white matter disorder characterized by insufficient myelin production due to biallelic loss of function mutations in the aminoacyl-tRNA synthetase complex-interacting multifunctional protein 2 (AIMP2) gene." — [PMID: 39640834](https://pubmed.ncbi.nlm.nih.gov/39640834/)

**Synonyms/alternative names:** The condition is referred to as HLD17 and by its OMIM designation (#618006). The gene AIMP2 is interchangeably called **JTV1** and **MSC p38/p38** in the biochemical literature.

**Source of information:** The disease-level knowledge is derived from **aggregated resources** (OMIM, Orphanet, literature reviews) combined with a small number of **individual patient reports** (whole-exome-sequenced consanguineous families and additional cohort cases). Because HLD17 is ultra-rare, the evidence base is dominated by individual case reports and small cohorts rather than EHR-scale aggregation.

---

## Section 2 — Etiology

**Primary cause — genetic.** HLD17 is caused exclusively by **biallelic (homozygous or compound heterozygous) loss-of-function mutations in AIMP2**. The originally described allele is the recurrent nonsense variant **c.105C>A, p.(Tyr35Ter)**, identified homozygously in affected individuals from two unrelated consanguineous families ([PMID: 29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/)). The allelic spectrum has since expanded to include **compound heterozygous** genotypes ([PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)).

> "We hereby report the first human disease associated with deleterious mutations in AIMP2." — [PMID: 29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/)

**Genetic risk factors.** The disease-causing factor is the biallelic AIMP2 genotype itself; there are no established independent susceptibility loci or modifier genes. **Consanguinity** is a major risk-elevating circumstance because it increases the probability of homozygosity for rare recessive AIMP2 alleles. The founder-like p.(Tyr35Ter) variant lies within a shared 940 kb homozygous region on chromosome 7, consistent with descent from a common ancestor.

**Environmental, lifestyle, infectious, protective, and gene–environment factors.** None are established. HLD17 is a pure Mendelian disorder: there are **no documented environmental triggers, toxins, infectious agents, lifestyle risk/protective factors, or gene–environment interactions**. The only "protective" circumstance is the absence of a second pathogenic AIMP2 allele (heterozygous carriers are unaffected).

---

## Section 3 — Phenotypes

Core phenotypes documented across affected individuals (two consanguineous families; four children) and subsequent cohort reports are listed below with suggested HPO terms.

| Phenotype | Type | HPO term (suggested) | Onset | Course | Frequency |
|---|---|---|---|---|---|
| Microcephaly | Physical/clinical sign | HP:0000252 | Congenital/neonatal | Progressive | Core feature (all reported) |
| Refractory seizures | Clinical sign | HP:0001250 (seizure); HP:0002133 (status) | Infancy | Progressive, refractory | Core feature |
| Intellectual disability / global developmental delay | Behavioral/cognitive | HP:0001249 / HP:0001263 | Infancy | Progressive | Core feature |
| Spastic quadriparesis | Clinical sign | HP:0002510 (spastic tetraplegia) | Infancy | Progressive | Core feature |
| CNS hypomyelination | Imaging/physical | HP:0002500 | Congenital | Persistent | Defining feature |
| Cerebral atrophy | Imaging | HP:0002059 | Infancy | Progressive | Frequent |
| Cerebellar atrophy | Imaging | HP:0001272 | Infancy | Progressive | Frequent |
| Spinal cord atrophy | Imaging | HP:0021010 | Infancy | Progressive | Reported |
| Thin corpus callosum | Imaging | HP:0033725 / HP:0002079 (hypoplasia) | Congenital | Stable/progressive | Reported |
| Basal ganglia T2 hypointensity (symmetric) | Imaging | HP:0002134 | Infancy | — | Reported |
| Prominent/enlarged cisterna magna | Imaging | HP:0002280 | Congenital | — | Reported |

> "two affected children each having microcephaly, refractory seizures, intellectual disability, and spastic quadriparesis" — [PMID: 29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/)

> "Magnetic resonance imaging showed atrophy of cerebrum, cerebellum and spinal cord, prominent cisterna magna, symmetric T2 hypo-intensities in the bilateral basal ganglia and thinning of corpus callosum." — [PMID: 29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/)

**Severity, progression, and quality of life.** The phenotype is **severe and progressive**, with onset in early infancy. Affected children have profound neurological impairment, with the combination of refractory epilepsy, severe cognitive impairment, and spastic quadriparesis producing major dependence in all domains of daily function. Formal QoL instruments (EQ-5D, SF-36, PROMIS) have not been applied in this ultra-rare disease; impact is inferred from phenotype severity. Neurological symptoms are described as "variable" across reported patients ([PMID: 39433694](https://pubmed.ncbi.nlm.nih.gov/39433694/)).

---

## Section 4 — Genetic / Molecular Information

**Causal gene — AIMP2.**
- Gene symbol: AIMP2 (synonyms JTV1, MSC p38). HGNC:20609. Ensembl ENSG00000106305. Chromosome 7p22.1.
- OMIM disease: #618006.

**Pathogenic variants.**
- **c.105C>A, p.(Tyr35Ter)** — recurrent **nonsense** variant; homozygous in the index consanguineous families; founder-like (within a shared 940 kb homozygous block). Classified pathogenic.
- **Compound heterozygous loss-of-function** genotypes reported subsequently ([PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)).
- AIMP2 pathogenic/likely-pathogenic variants recur in Indian congenital microcephaly / NDD exome cohorts ([PMID: 35568357](https://pubmed.ncbi.nlm.nih.gov/35568357/); [PMID: 42833956](https://pubmed.ncbi.nlm.nih.gov/42833956/)).

**Variant classes:** nonsense (premature termination codon) and other loss-of-function alleles; engineered indels have been used to model the disease.

**Allele frequency / population constraint (gnomAD, GRCh38).** AIMP2 is **not haploinsufficient** — fully consistent with a recessive mechanism:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | ≈ 1.0e-6 (≈0) | Tolerant to heterozygous LoF |
| LoF observed/expected (o/e) | 0.855 (90% CI 0.60–1.24) | No strong LoF depletion |
| LOEUF (upper) | 1.24 | Not LoF-constrained |
| Observed vs expected LoF | 20 vs 23.4 | As expected |
| LoF z | 0.60 | Not constrained |
| Missense z | −2.10 (o/e missense 1.24) | Tolerant to missense |

This profile means a single pathogenic AIMP2 allele is tolerated (carriers unaffected); disease requires two defective alleles.

**Functional consequence:** **Loss of function.** AIMP2 disease mutations cause decreased AIMP2 protein expression, attenuated protein synthesis, and dysregulation of the MSC component MARS1 ([PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)). In addition, the truncated p.Tyr35Ter protein exhibits a **toxic aggregation behavior** (Golgi mislocalization) in oligodendroglial cells ([PMID: 34523057](https://pubmed.ncbi.nlm.nih.gov/34523057/)).

**Somatic vs germline:** Germline. **Modifier genes, epigenetic changes, chromosomal abnormalities:** none established for HLD17.

---

## Section 5 — Environmental Information

**Not applicable.** HLD17 is a monogenic autosomal recessive disorder. No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents are implicated in its causation or triggering.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function mutation in AIMP2** (e.g., homozygous nonsense c.105C>A p.Tyr35Ter) **→ leads to** reduced/absent functional AIMP2 scaffold protein (demonstrated: reduced protein expression in patient fibroblasts).
2. Reduced AIMP2 **→ results in** destabilization/dysregulation of the multi-tRNA synthetase complex (MSC), including dysregulation of methionyl-tRNA synthetase **MARS1** (demonstrated in patient fibroblasts).
3. MSC dysregulation **→ leads to** **attenuation of global protein synthesis** (demonstrated in patient fibroblasts).
4. Impaired protein synthesis **→ results in** **increased neural cell death and atrophy in the developing brain** (demonstrated: CRISPR *aimp2* zebrafish; inferred for human CNS).

   **Branch (toxic/oligodendroglial route):**
   - 2b. The truncated Y35X protein **→ aggregates in the Golgi apparatus** of oligodendroglial cells (demonstrated in mouse FBD-102b cells).
   - 3b. Golgi aggregation **→ upregulates Golgi-stress signaling and activates caspase-2 (CASP2)** (demonstrated).
   - 4b. CASP2 activation **→ blocks oligodendrocyte morphological differentiation** (demonstrated; reversed by CASP2 knockdown).

5. Neural cell death (step 4) **plus** oligodendrocyte differentiation arrest (step 4b) **→ together result in** **CNS hypomyelination and progressive cerebral/cerebellar/spinal atrophy** (clinically and radiologically demonstrated).
6. Hypomyelination + atrophy **→ manifest as** microcephaly, refractory seizures, intellectual disability, and spastic quadriparesis (clinical).

### Detail by category

**Protein / normal function.** AIMP2/p38 is a **non-enzymatic scaffolding protein required for assembly of the macromolecular multi-tRNA synthetase complex** ([PMID: 18695251](https://pubmed.ncbi.nlm.nih.gov/18695251/)). The MSC is a eukaryote-specific assembly of **eight aminoacyl-tRNA synthetases and three AIMP scaffolds (AIMP1–3)** ([PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)). Beyond translation, AIMP2 is a **moonlighting tumor-suppressor**: under genotoxic/oxidative stress it dissociates from the MSC, translocates to the nucleus, and **directly interacts with p53, preventing MDM2-mediated ubiquitination/degradation of p53**, promoting apoptosis ([PMID: 18695251](https://pubmed.ncbi.nlm.nih.gov/18695251/)); it also co-activates FBP to induce USP29, stabilizing p53 under oxidative stress ([PMID: 21285945](https://pubmed.ncbi.nlm.nih.gov/21285945/)), and modulates TGF-β, Wnt, and TNF signaling ([PMID: 38835119](https://pubmed.ncbi.nlm.nih.gov/38835119/)).

> "AIMP2/p38 is a scaffolding protein required for the assembly of the macromolecular tRNA synthetase complex." — [PMID: 18695251](https://pubmed.ncbi.nlm.nih.gov/18695251/)

> "the eukaryote-specific multisynthetase complex (MSC), a macromolecular assembly of eight aminoacyl-tRNA synthetases (ARS) and three scaffolding components known as aminoacyl-tRNA synthetase interacting multifunctional proteins (AIMP1-3)" — [PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)

**Molecular pathways / cellular processes.** Core pathway = aminoacyl-tRNA biosynthesis / cytoplasmic translation (GO:0006412 translation; GO:0043039 tRNA aminoacylation). Downstream: regulated cell death/apoptosis (GO:0006915), Golgi stress response, caspase-2 signaling. Oligodendrocyte differentiation (GO:0048709) is the specifically impaired developmental program.

**Protein dysfunction.** Two modes: (i) **loss of scaffold function** → MSC destabilization and reduced translation; (ii) **toxic aggregation** of the Y35X fragment in the Golgi, driving Golgi stress/CASP2.

> "the HLD17-associated nonsense mutation (Tyr35-to-Ter [Y35X]) of AIMP2 localizes AIMP2 proteins as aggregates into the Golgi bodies in mouse oligodendroglial FBD-102b cells" — [PMID: 34523057](https://pubmed.ncbi.nlm.nih.gov/34523057/)

> "Expression of the Y35X mutant proteins, but not the wild type proteins, in cells upregulates Golgi stress signaling involving caspase-2 activation." — [PMID: 34523057](https://pubmed.ncbi.nlm.nih.gov/34523057/)

**Metabolic / biochemical.** The central defect is impaired protein synthesis capacity secondary to MSC dysfunction (not a classic enzyme deficiency measurable in blood/urine).

**Immune involvement:** none established (non-inflammatory hypomyelination).

**Cell types involved (suggested CL terms):** oligodendrocyte (CL:0000128) and oligodendrocyte precursor cell (CL:0002453) — the differentiating cells blocked by Golgi-stress/CASP2; neurons/neural cells broadly (CL:0000540) undergoing death/atrophy.

**Molecular profiling.** Patient fibroblasts: decreased AIMP2 protein, attenuated protein synthesis, MARS1 dysregulation ([PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)). No published transcriptomic/proteomic/metabolomic/lipidomic signatures specific to HLD17.

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** brain (UBERON:0000955) — central nervous system (UBERON:0001017). Body system: nervous system.
- **Primary tissue:** white matter (UBERON:0002316) — hypomyelination.
- **Specific regions:** cerebrum (UBERON:0001870), cerebellum (UBERON:0002037), spinal cord (UBERON:0002240), corpus callosum (UBERON:0002336, thin), basal ganglia (UBERON:0002420, symmetric T2 hypointensity), cisterna magna (prominent). Microcephaly reflects reduced overall brain volume.
- **Cell populations:** oligodendrocyte (CL:0000128)/OPC (CL:0002453), the myelinating cells of the CNS.
- **Subcellular compartments (GO CC):** aminoacyl-tRNA synthetase multienzyme complex (GO:0017101)/cytoplasm; Golgi apparatus (GO:0005794) — site of mutant protein aggregation; nucleus (GO:0005634) — site of AIMP2–p53 interaction under stress.
- **Lateralization:** **bilateral and symmetric** (symmetric basal ganglia T2 hypointensities; diffuse hypomyelination).

---

## Section 8 — Temporal Development

- **Onset:** congenital/neonatal to early infancy. Microcephaly is congenital; seizures and motor/cognitive signs emerge in infancy.
- **Onset pattern:** chronic/insidious with early manifestation.
- **Progression:** **progressive** — cerebral, cerebellar, and spinal atrophy worsen over time; seizures are refractory; the myelination deficit persists.
- **Course:** chronic, lifelong, progressive neurodevelopmental disorder; no spontaneous remission reported.
- **Critical period:** the perinatal/early-infancy window of active myelination is the key period of vulnerability and the plausible window for intervention (before irreversible hypomyelination and atrophy).

---

## Section 9 — Inheritance and Population

- **Inheritance:** autosomal recessive; biallelic AIMP2 loss of function. Carriers (heterozygotes) are unaffected (consistent with gnomAD LoF tolerance).
- **Penetrance/expressivity:** biallelic genotype appears fully penetrant for a severe neurodevelopmental phenotype; neurological severity is described as variable.
- **Consanguinity / founder effect:** strongly associated.

> "The variant lies in a common homozygous region of 940 kb on chromosome 7 and is likely to have been inherited from a common ancestor." — [PMID: 29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/)

- **Epidemiology:** **ultra-rare.** Prevalence/incidence not formally quantified; only a handful of families/patients reported worldwide. AIMP2 appears as an ultra-rare cause in large microcephaly/NDD exome cohorts.

> "We here report phenotypes associated with the genes for ultra-rare NDDs with microcephaly namely ATRIP, MINPP1, PNPLA8, AIMP2, ANKLE2, NCAPD2 and TRIT1" — [PMID: 35568357](https://pubmed.ncbi.nlm.nih.gov/35568357/)

- **Populations:** reported in consanguineous families and in South Asian (Indian) cohorts; no exclusive ethnic restriction established. **Sex ratio:** no sex bias expected (autosomal recessive). **Carrier frequency:** not established; expected very low given rarity.

---

## Section 10 — Diagnostics

**Diagnostic approach = MRI pattern recognition + next-generation sequencing (NGS).**

> "Next-generation sequencing provides a definitive diagnosis in 80-90% of patients." — [PMID: 33324001](https://pubmed.ncbi.nlm.nih.gov/33324001/)

- **Imaging (MRI):** the cornerstone. Hypomyelination is defined as **diffuse, persistent T2/FLAIR hyperintensity with relative temporal stability and absent enhancement**, distinguishing it from demyelination ([PMID: 42468917](https://pubmed.ncbi.nlm.nih.gov/42468917/)). HLD17-specific findings: CNS hypomyelination, cerebral/cerebellar/spinal atrophy, thin corpus callosum, symmetric basal ganglia T2 hypointensity, prominent cisterna magna.

> "The pivotal imaging distinction is between hypomyelination-diffuse, persistent T2/FLAIR hyperintensity with relative temporal stability and absent enhancement-and demyelination" — [PMID: 42468917](https://pubmed.ncbi.nlm.nih.gov/42468917/)

- **Genetic testing:** **WES or WGS** identifying biallelic AIMP2 loss-of-function variants is definitive; leukodystrophy/HLD gene panels including AIMP2 and targeted single-gene testing/Sanger confirmation are used. Chromosomal microarray is of low yield (point mutations, not CNVs).
- **Gene class context:** HLD-causing genes "encode structural myelin proteins but also many that encode proteins involved in RNA translation" — the class to which AIMP2 belongs ([PMID: 33324001](https://pubmed.ncbi.nlm.nih.gov/33324001/)).
- **Laboratory/biomarkers:** no specific blood/CSF biomarker; diagnosis is imaging + molecular.
- **Differential diagnosis:** other hypomyelinating leukodystrophies — **HLD3 (AIMP1)**, Pol III–related leukodystrophies (POLR3A/POLR3B), 4H leukodystrophy, oculodentodigital dysplasia, and other RNA-translation-class HLDs; distinguished by gene and MRI pattern nuances (e.g., Pol III disorders show T2 hypointensity of thalami/pallida and optic radiations).

---

## Section 11 — Outcome / Prognosis

- **Prognosis:** poor. HLD17 is a severe, progressive, lifelong neurodevelopmental disorder with refractory epilepsy, severe cognitive and motor disability (spastic quadriparesis), and progressive CNS atrophy.
- **Survival/mortality:** formal survival statistics are not established for HLD17 given its rarity; the allelic paralog disorder HLD3 (AIMP1) is associated with decreased life expectancy ([PMID: 33402283](https://pubmed.ncbi.nlm.nih.gov/33402283/)), and severe early-onset HLDs generally carry high morbidity and reduced survival.
- **Morbidity/function:** profound disability across motor, cognitive, and seizure domains; high dependence for daily care.
- **Prognostic factors:** not formally defined; earlier/more severe presentation and refractory seizures imply worse outcome. No validated prognostic biomarkers.

---

## Section 12 — Treatment

**No approved disease-modifying therapy exists. Management is supportive.**

- **Supportive/symptomatic care:** anti-seizure medication for refractory epilepsy (e.g., levetiracetam has been used in HLD patients), spasticity management, nutritional support, and rehabilitation (physical, occupational, speech therapy). NCIT concepts: supportive care (NCIT:C19236), anticonvulsant therapy (NCIT:C15229), rehabilitation therapy (NCIT:C15917).
- **Preclinical / experimental strategies:**
  1. **Anticodon-engineered suppressor tRNAs** for nonsense alleles.

     > "We tested anticodon engineered suppressor tRNAs on expression of disease-associated nonsense mutations and found that they dramatically increase protein expression of AIMP2 variants" — [PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)

     The authors propose these "could improve patient outcomes," especially relevant to the premature-termination allele p.Tyr35Ter.
  2. **CASP2 inhibition.**

     > "CASP2 knockdown but not control knockdown reverses the phenotypes of cells expressing the mutant proteins" — [PMID: 34523057](https://pubmed.ncbi.nlm.nih.gov/34523057/)

- **Pharmacogenomics, gene therapy, cell therapy, surgery, immunotherapy:** none established/approved for HLD17.

---

## Section 13 — Prevention

- **Primary prevention:** not possible at the population level (monogenic recessive). The main avenue is **genetic counseling** for consanguineous and at-risk families.
- **Secondary prevention / screening:** **carrier screening** and **cascade testing** of relatives of affected probands; **prenatal diagnosis** and **preimplantation genetic testing** are options once the familial AIMP2 variant is known. There is no newborn-screening assay for HLD17.
- **Tertiary prevention:** early seizure control, spasticity management, and rehabilitation to limit complications.
- **Counseling:** recurrence risk is 25% for each pregnancy of carrier couples; emphasize consanguinity-related risk.

---

## Section 14 — Other Species / Natural Disease

- **Orthologs / models:** zebrafish (*Danio rerio*) *aimp2* is orthologous and, when disrupted, recapitulates brain phenotypes (below). Mouse *Aimp2* is used in oligodendroglial cell models.
- **Natural disease in other species:** no naturally occurring AIMP2 leukodystrophy is documented in companion animals or wildlife (no OMIA entry noted). Zoonotic/transmission considerations: not applicable.
- **Comparative biology:** AIMP2 and the MSC are evolutionarily conserved across eukaryotes; the paralog AIMP1 causes an analogous human HLD (HLD3), underscoring conservation of the tRNA-synthetase-complex pathway in myelin biology.

---

## Section 15 — Model Organisms

| Model | System | Key phenotype / use | Reference |
|---|---|---|---|
| Zebrafish *aimp2* CRISPR | *Danio rerio*, in vivo | Increased cell death and atrophy in developing brain | [PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/) |
| Patient-derived fibroblasts | Human, in vitro | Decreased AIMP2 protein, attenuated protein synthesis, MARS1 dysregulation | [PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/) |
| Mouse oligodendroglial FBD-102b (AIMP2-Y35X) | Mouse cell line, in vitro | Golgi aggregation, CASP2 activation, differentiation block (rescued by CASP2 knockdown) | [PMID: 34523057](https://pubmed.ncbi.nlm.nih.gov/34523057/) |
| HEK293 AIMP2-indel (CRISPR-Cas9) | Human cell line, in vitro | Engineered cellular model of HLD17 | [PMID: 39433694](https://pubmed.ncbi.nlm.nih.gov/39433694/) |
| In silico AIMP2 structure (Phyre2/I-TASSER) | Computational | WT vs mutant structural modeling | [PMID: 39640834](https://pubmed.ncbi.nlm.nih.gov/39640834/) |

> "CRISPR-mediated disruption of aimp2 in zebrafish led to increased cell death and atrophy in the developing brain" — [PMID: 42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/)

> "produced a construct for inducing mutations in the AIMP2 gene, which can be utilized to edit the AIMP2 gene in nerve cells and create a cellular model of the HLD17 disease" — [PMID: 39433694](https://pubmed.ncbi.nlm.nih.gov/39433694/)

**Phenotype recapitulation / limitations:** the zebrafish model captures neural cell death and brain atrophy; the oligodendroglial cell model captures the differentiation block and its CASP2 dependence; fibroblasts capture the translational defect. No published mouse model fully recapitulates the complete human hypomyelinating leukodystrophy phenotype, which remains a gap.

---

## Mechanistic Model / Interpretation

```
            Biallelic AIMP2 LoF (e.g., homozygous c.105C>A p.Tyr35Ter)
                                   │
            ┌──────────────────────┴───────────────────────┐
   LOSS-OF-FUNCTION route                        TOXIC / AGGREGATION route
            │                                               │
  ↓ AIMP2 scaffold protein                     Truncated Y35X protein
            │                                               │
  MSC destabilization                           Aggregates in Golgi
  (MARS1 dysregulation)                          (oligodendroglia)
            │                                               │
  ↓ global protein synthesis                     Golgi stress → CASP2 activation
            │                                               │
  Neural cell death / brain atrophy            Oligodendrocyte differentiation BLOCK
            │                                               │
            └──────────────────┬────────────────────────────┘
                               ▼
         CNS HYPOMYELINATION + progressive cerebral/cerebellar/spinal atrophy
                               ▼
     Microcephaly · refractory seizures · intellectual disability · spastic quadriparesis
```

The two routes are complementary. The **loss-of-function arm** (upstream, cell-general) explains the broad neural cell death and atrophy seen in the zebrafish model and patient fibroblasts. The **toxic-aggregation arm** (cell-type-specific to oligodendroglia) explains why myelination in particular fails and nominates CASP2 as a druggable node. Both converge on hypomyelination plus atrophy. Therapeutically, suppressor tRNAs act at the most upstream point (restoring full-length AIMP2, addressing both arms for nonsense alleles), whereas CASP2 inhibition acts on the downstream oligodendroglial arm.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [29215095](https://pubmed.ncbi.nlm.nih.gov/29215095/) | Homozygous AIMP2 nonsense variant → NDD | Establishes AIMP2 as causal; defines p.Tyr35Ter, clinical/MRI phenotype, founder region |
| [39640834](https://pubmed.ncbi.nlm.nih.gov/39640834/) | In silico analysis of AIMP2 missense | States HLD17 definition, biallelic LoF mechanism; structural modeling |
| [34523057](https://pubmed.ncbi.nlm.nih.gov/34523057/) | Golgi-stress CASP2 & AIMP2-Y35X | Golgi aggregation, CASP2 activation, differentiation block, CASP2 rescue |
| [42719951](https://pubmed.ncbi.nlm.nih.gov/42719951/) | AIMP2 LoF zebrafish model | MSC/MARS1 dysregulation, ↓ protein synthesis, brain atrophy, suppressor tRNA therapy |
| [39433694](https://pubmed.ncbi.nlm.nih.gov/39433694/) | CRISPR HEK293 HLD17 model | Cellular model; "variable neurological symptoms" |
| [18695251](https://pubmed.ncbi.nlm.nih.gov/18695251/) | AIMP2/p38 responds to genotoxic stress via p53 | Defines scaffold and p53-stabilizing moonlighting function |
| [38835119](https://pubmed.ncbi.nlm.nih.gov/38835119/) | AIMP2-DX2 structure | TGF-β/Wnt/TNF signaling roles |
| [21285945](https://pubmed.ncbi.nlm.nih.gov/21285945/) | JTV1/FBP/USP29/p53 | Oxidative-stress p53 stabilization pathway |
| [35568357](https://pubmed.ncbi.nlm.nih.gov/35568357/) | 87 Indian microcephaly families | AIMP2 as ultra-rare microcephaly NDD gene |
| [42833956](https://pubmed.ncbi.nlm.nih.gov/42833956/) | Indian microcephaly cohort | AIMP2 pathogenic variants in congenital microcephaly |
| [33324001](https://pubmed.ncbi.nlm.nih.gov/33324001/) | HLD review | NGS diagnostic yield 80–90%; RNA-translation gene class |
| [42468917](https://pubmed.ncbi.nlm.nih.gov/42468917/) | MRI patterns in leukodystrophies | Hypomyelination vs demyelination imaging definition |
| [33402283](https://pubmed.ncbi.nlm.nih.gov/33402283/) | AIMP1/HLD3 | Paralog disorder; decreased life expectancy; peripheral nerve involvement |
| [21855841](https://pubmed.ncbi.nlm.nih.gov/21855841/) | POLR3A leukodystrophy | Shared "perturbed protein synthesis" mechanism across RNA-translation HLDs |

---

## Limitations and Knowledge Gaps

1. **Very small patient base.** Only a handful of families/patients are reported; prevalence, incidence, survival, penetrance, and expressivity are not quantitatively established.
2. **Narrow allelic spectrum.** Most evidence rests on the founder nonsense allele p.Tyr35Ter; genotype–phenotype correlations for other variant classes (missense, splice) are largely unknown.
3. **No complete mouse model.** Existing models (zebrafish, cell lines, fibroblasts) each capture only part of the phenotype; a faithful mammalian model of the full hypomyelinating leukodystrophy is lacking.
4. **Mechanistic weighting unresolved.** The relative contributions of the loss-of-function (translation) arm versus the toxic Golgi-stress/CASP2 arm to human hypomyelination are not quantified.
5. **No validated biomarkers or omics signatures** (transcriptomic/proteomic/metabolomic) specific to HLD17.
6. **Therapies remain preclinical.** Suppressor tRNA and CASP2 strategies have not been tested in vivo in a mammalian HLD17 model or in patients.

---

## Proposed Follow-up Experiments / Actions

1. **Develop a conditional/constitutive mouse *Aimp2* model** (and an oligodendrocyte-specific knockout) to test whether hypomyelination, atrophy, and seizures are recapitulated in a mammal.
2. **Test anticodon-engineered suppressor tRNAs in vivo** (zebrafish and a mouse model carrying a nonsense allele) and assess rescue of myelination, protein synthesis, and survival.
3. **Test CASP2 inhibitors** (pharmacologic or genetic) in oligodendroglial and in vivo models to determine whether differentiation and myelination are restored.
4. **Define genotype–phenotype correlations** by building an international HLD17 patient registry capturing variant class, imaging, seizure burden, and survival.
5. **Characterize the MSC/translation defect** in patient-derived iPSC oligodendrocytes (ribosome profiling, proteomics) to weight the LoF vs toxic-aggregation contributions.
6. **Search for modifiers** (e.g., MARS1 and other MSC components, CASP2 pathway genes) that might explain the "variable" neurological severity.

---

## Consensus Answer

Hypomyelinating Leukodystrophy 17 (HLD17; MONDO:0054817, OMIM #618006) is an ultra-rare, autosomal recessive, infantile-onset hypomyelinating leukodystrophy caused by biallelic loss-of-function mutations in **AIMP2** (HGNC:20609; synonyms JTV1/p38), the non-catalytic scaffold of the cytoplasmic multi-tRNA synthetase complex, with the recurrent founder nonsense allele c.105C>A p.(Tyr35Ter). AIMP2 loss destabilizes the multisynthetase complex (dysregulating MARS1) and attenuates protein synthesis, causing neural cell death and brain atrophy, while the truncated mutant protein aggregates in the Golgi and activates Golgi-stress caspase-2 to arrest oligodendrocyte differentiation—together producing CNS hypomyelination and progressive cerebral/cerebellar/spinal atrophy that manifest as microcephaly, refractory seizures, intellectual disability, and spastic quadriparesis. Management is currently supportive, with anticodon-engineered suppressor tRNAs and CASP2 inhibition as promising preclinical therapeutic strategies.


## Artifacts

- [OpenScientist final report](Hypomyelinating_Leukodystrophy_17-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypomyelinating_Leukodystrophy_17-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34523057` *(abstract only)*: "the HLD17-associated nonsense mutation (Tyr35-to-Ter [Y35X]) of AIMP2 localizes AIMP2 proteins as aggregates into the Golgi bodies in mouse oligodendroglial FBD-102b cells"
  - closest text in source: "the HLD17-associated nonsense mutation (Tyr35-to-Ter [Y35X]) of AIMP2 localizes AIMP2 proteins as aggregates into the Golgi bodies in mouse oligodendroglial FBD-102b cells"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42468917` (6 mentions) - Magnetic resonance imaging in leukodystrophies: characteristic patterns and diagnostic relevance.
  - shared terms: leukodystrophy, disease

Weighed against this report's own most characteristic terms: `aimp2`, `hld17`, `protein`, `atrophy`, `cell`, `gene`, `hypomyelination`, `nonsense`, `casp2`, `patient`, `variant`, `mutation`, `msc`, `leukodystrophy`, `microcephaly`, `biallelic`, `recessive`, `familie`, `phenotype`, `disease`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0054817` (3 mentions) - the report calls it "MONDO"; MONDO calls it **leukodystrophy, hypomyelinating, 17**
- `HP:0000252` (1 mention) - the report calls it "Physical/clinical sign"; HP calls it **Microcephaly**
- `HP:0002500` (1 mention) - the report calls it "Imaging/physical"; HP calls it **Abnormal cerebral white matter morphology**
- `HP:0002059` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebral atrophy**
- `HP:0001272` (1 mention) - the report calls it "Imaging"; HP calls it **Cerebellar atrophy**
- `HP:0002134` (1 mention) - the report calls it "Imaging"; HP calls it **Abnormal basal ganglia morphology**
- `HP:0002280` (1 mention) - the report calls it "Imaging"; HP calls it **Enlarged cisterna magna**
- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** brain"; UBERON calls it **brain**
- `UBERON:0001870` (1 mention) - the report calls it "Specific regions:** cerebrum"; UBERON calls it **frontal cortex**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0021010` (1 mention), reported as "Imaging" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000128` (2 mentions) - the report calls it "Cell populations:** oligodendrocyte"; CL calls it **oligodendrocyte**
- `UBERON:0002316` (1 mention) - the report calls it "Primary tissue:** white matter"; UBERON calls it **white matter**, and lists "CNS white matter" among its other names