---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T18:52:51.429302'
end_time: '2026-09-03T19:21:56.396277'
duration_seconds: 1744.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Dominant Intermediate E
  mondo_id: MONDO:0013758
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:23014460
  relevance_assessed: 22
  on_topic: 19
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 24
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.04
  labels_checked: 21
  labels_matching: 9
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0013758
    reported_labels:
    - MONDO
    ontology_label: Charcot-Marie-Tooth disease dominant intermediate E
  - term_id: HP:0001761
    reported_labels:
    - Physical manifestation
    - pes cavus
    ontology_label: Pes cavus
  - term_id: HP:0003693
    reported_labels:
    - Clinical sign
    ontology_label: Distal amyotrophy
  - term_id: HP:0002751
    reported_labels:
    - Physical manifestation
    ontology_label: Kyphoscoliosis
  - term_id: HP:0030181
    reported_labels:
    - variable NCV
    ontology_label: Gordon reflex
  - term_id: HP:0000097
    reported_labels:
    - Pathology/lab
    - FSGS
    ontology_label: Focal segmental glomerulosclerosis
  - term_id: HP:0000093
    reported_labels:
    - Laboratory abnormality
    - proteinuria
    ontology_label: Proteinuria
  - term_id: HP:0000100
    reported_labels:
    - Clinical
    ontology_label: Nephrotic syndrome
  - term_id: HP:0003774
    reported_labels:
    - Clinical
    - ESRD
    ontology_label: Stage 5 chronic kidney disease
  - term_id: CL:0002573
    reported_labels:
    - Schwann cells
    - Nervous tissue:** myelinating **Schwann cells
    - Schwann cell
    ontology_label: Schwann cell
  - term_id: UBERON:0000044
    reported_labels:
    - peripheral nerve
    ontology_label: dorsal root ganglion
  labels_variant: 1
  unresolved_terms:
  - HP:0106487
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Charcot-Marie-Tooth_Disease_Dominant_Intermediate_E-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Charcot-Marie-Tooth_Disease_Dominant_Intermediate_E-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Dominant Intermediate E
- **MONDO ID:** MONDO:0013758 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Dominant Intermediate E** covering all of the
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

# Charcot-Marie-Tooth Disease Dominant Intermediate E (CMTDIE): A Comprehensive Disease Characteristics Report

**Disease:** Charcot-Marie-Tooth Disease Dominant Intermediate E
**MONDO ID:** MONDO:0013758 | **OMIM:** #614455 | **Category:** Mendelian (autosomal dominant)
**Causal gene:** *INF2* (Inverted Formin 2), 14q32.33, HGNC:23791

---

## Summary

Charcot-Marie-Tooth disease Dominant Intermediate E (CMTDIE) is a rare autosomal-dominant Mendelian disorder that uniquely couples an **intermediate-type peripheral neuropathy** with **focal segmental glomerulosclerosis (FSGS)** of the kidney. It is caused by heterozygous mutations in *INF2*, a gene encoding an endoplasmic-reticulum–anchored, actin-nucleating formin. Pathogenic variants cluster tightly in the **diaphanous-inhibitory domain (DID)** encoded by exons 2–4. In a landmark cohort, 12 of 16 (75%) patients with CMT plus glomerulopathy carried DID mutations, establishing *INF2* as the dominant cause of the dual phenotype ([PMID: 22187985](https://pubmed.ncbi.nlm.nih.gov/22187985/)).

The mechanism is a **gain-of-function actinopathy**, not haploinsufficiency: point-mutant *Inf2* knock-in mice develop glomerular disease while *Inf2* knockouts do not ([PMID: 39536114](https://pubmed.ncbi.nlm.nih.gov/39536114/)). Loss of the DID-mediated autoinhibition produces **excessive/dysregulated actin polymerization** that injures two highly polarized cell types simultaneously: **Schwann cells**, producing a "Schwann-cell actinopathy" with demyelinating-plus-axonal features and intermediate nerve conduction velocities ([PMID: 24487800](https://pubmed.ncbi.nlm.nih.gov/24487800/)), and **podocytes**, producing FSGS via dysregulated dynein-mediated trafficking of nephrin to the proteasome, abnormal mitochondrial dynamics, and terminal MRTF/SRF- and p53-driven cell death ([PMID: 39621430](https://pubmed.ncbi.nlm.nih.gov/39621430/), [PMID: 39586895](https://pubmed.ncbi.nlm.nih.gov/39586895/)).

There is a **positional genotype-phenotype gradient** along the DID: N-terminal residues (57–184) produce the dual CMT/FSGS phenotype, whereas more C-terminal residues (184–245) tend to produce isolated FSGS ([PMID: 37491439](https://pubmed.ncbi.nlm.nih.gov/37491439/)). Renal disease is progressive, frequently reaching end-stage renal disease (ESRD) in the third-to-fourth decade, but—importantly for counseling—**genetic (INF2) FSGS does not recur after kidney transplantation**, unlike idiopathic FSGS ([PMID: 27733133](https://pubmed.ncbi.nlm.nih.gov/27733133/)). No disease-specific therapy exists; management is supportive, though proteasome inhibition and allele-selective silencing are promising experimental strategies.

---

## Section 1: Disease Information

**Overview.** CMTDIE is a hereditary neurologic-renal syndrome in which an intermediate form of Charcot-Marie-Tooth peripheral neuropathy co-occurs with steroid-resistant FSGS. "Intermediate" refers to nerve conduction velocities that fall between the demyelinating (CMT1, <38 m/s) and axonal (CMT2, >45 m/s) ranges, reflecting mixed demyelinating and axonal pathology. The disease is distinctive among the CMTs because the same mutation damages both the peripheral nervous system and the kidney glomerulus.

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0013758 |
| OMIM | #614455 (Charcot-Marie-Tooth disease, dominant intermediate E) |
| Gene | *INF2*, OMIM *610982, HGNC:23791, 14q32.33 |
| ICD-10 | G60.0 (Hereditary motor and sensory neuropathy) |
| MeSH | Charcot-Marie-Tooth Disease (D002607) |
| Orphanet | Related entry: Charcot-Marie-Tooth disease with glomerulopathy |

**Synonyms / alternative names.** CMTDIE; Dominant intermediate Charcot-Marie-Tooth disease type E (DI-CMTE); CMT–FSGS; INF2-related CMT with glomerulopathy; hereditary neuropathy with glomerulopathy.

**Information source.** The knowledge base is derived from **aggregated disease-level resources** (OMIM, ClinVar) plus **individual-patient case series and family pedigrees** reported in the primary literature. There is no large EHR-derived cohort; the disease is rare, and knowledge rests on multi-generation families and small case series.

---

## Section 2: Etiology

**Primary cause — genetic.** CMTDIE is a monogenic disorder caused by **heterozygous mutations in *INF2***. In the defining cohort, Boyer et al. genotyped 16 index patients with CMT plus FSGS who lacked *PMP22*/*MPZ* mutations and identified nine novel heterozygous *INF2* mutations in 12/16 (75%), all in exons 2–3 encoding the DID ([PMID: 22187985](https://pubmed.ncbi.nlm.nih.gov/22187985/)). Inheritance is autosomal dominant; *de novo* mutations also occur and may be relatively common in the dual phenotype ([PMID: 24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/)).

**Genetic risk factors.** The causal variants are the DID missense/in-frame variants themselves. The *position* of the variant is the principal modifier of the phenotype (see Section 4). No independent susceptibility loci or GWAS signals are described—this is a Mendelian, not complex, disease.

**Environmental risk factors.** None established as causative. CMTDIE is fully determined by the germline *INF2* variant. However, experimental models show that a "second hit" of glomerular stress unmasks the renal phenotype: R218Q knock-in mice are normal at baseline but develop proteinuria/FSGS after puromycin aminonucleoside (PAN) or protamine sulfate injury ([PMID: 38915495](https://pubmed.ncbi.nlm.nih.gov/38915495/), [PMID: 27350175](https://pubmed.ncbi.nlm.nih.gov/27350175/)). This implies that mutant INF2 confers a susceptibility to injury rather than causing spontaneous glomerular destruction, and that podocyte stressors could plausibly modulate human disease onset—though this is inferred from models, not demonstrated clinically.

**Protective factors.** No genetic or environmental protective factors are established. The observation that *INF2* knockout does not cause disease implies that reducing mutant allele expression (allele-selective silencing) would be protective—a therapeutic hypothesis, not a natural protective factor.

**Gene-environment interactions.** Not characterized in humans. The model data (mutation + injury synergy) are the closest analog.

---

## Section 3: Phenotypes

CMTDIE has two organ-system phenotype clusters: **neurologic** and **renal**, plus occasional additional features.

### Neurologic phenotypes

| Phenotype | Type | HPO term | Onset | Severity/Progression |
|-----------|------|----------|-------|----------------------|
| Distal muscle weakness (legs > arms) | Clinical sign | HP:0009053 (distal lower limb amyotrophy) | Childhood–adolescence (mean onset ~11.5 y) | Slowly progressive |
| Peripheral sensory loss | Symptom | HP:0106487 | Childhood–adult | Progressive |
| Pes cavus | Physical manifestation | HP:0001761 | Childhood | Stable/progressive |
| Distal muscle atrophy | Clinical sign | HP:0003693 | Adolescence | Progressive |
| Kyphoscoliosis | Physical manifestation | HP:0002751 | Variable | Variable |
| Intermediate nerve conduction velocity | Laboratory/electrophysiology | HP:0030181 (variable NCV) | Detectable at diagnosis | Stable trait |

Case reports document mean CMT onset ~11.5 years (range 3–17) with slowly progressive sensorimotor polyneuropathy, pes cavus, and kyphoscoliosis ([PMID: 30680856](https://pubmed.ncbi.nlm.nih.gov/30680856/)). Rare families show additional CNS features (intellectual disability, more severe sensorineural hearing loss) ([PMID: 24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/)) or transient speech difficulty ([PMID: 25943269](https://pubmed.ncbi.nlm.nih.gov/25943269/)).

### Renal phenotypes

| Phenotype | Type | HPO term | Onset | Severity/Progression |
|-----------|------|----------|-------|----------------------|
| Focal segmental glomerulosclerosis | Pathology/lab | HP:0000097 | Childhood–adulthood | Progressive to ESRD |
| Proteinuria | Laboratory abnormality | HP:0000093 | Childhood–adult | Progressive |
| Nephrotic syndrome | Clinical | HP:0000100 | Variable | Steroid-resistant |
| End-stage renal disease | Clinical | HP:0003774 | 3rd–4th decade typically | Terminal renal outcome |

Renal involvement ranges from minimal proteinuria to steroid-resistant nephrotic syndrome progressing to ESRD. Some *INF2* mutations produce **isolated CMT with minimal/absent kidney involvement** ([PMID: 30680856](https://pubmed.ncbi.nlm.nih.gov/30680856/)), and *INF2* can present with **non-FSGS histology** (minimal-change glomerulopathy, IgA nephropathy) within the same family ([PMID: 29038887](https://pubmed.ncbi.nlm.nih.gov/29038887/)).

**Quality-of-life impact.** The combination is doubly disabling: progressive distal weakness impairs gait and manual dexterity (requiring orthoses), while progression to ESRD imposes dialysis dependence or transplantation. No formal EQ-5D/SF-36 data specific to CMTDIE are published.

**Frequency note.** Within *INF2*-mutation carriers, both variable penetrance and intrafamilial variability are documented—the same variant can produce isolated FSGS in one relative and the full dual phenotype in another ([PMID: 25943269](https://pubmed.ncbi.nlm.nih.gov/25943269/)).

---

## Section 4: Genetic / Molecular Information

**Causal gene.** *INF2* (Inverted Formin 2), 14q32.33, HGNC:23791, OMIM *610982. INF2 is a member of the diaphanous-related formin family that nucleates and elongates actin filaments and also regulates microtubule dynamics.

**Pathogenic variants.**
- **Domain clustering:** Nearly all CMTDIE variants localize to the **diaphanous-inhibitory domain (DID)** encoded by exons 2–4. Boyer et al. found all nine mutations in exons 2–3 ([PMID: 22187985](https://pubmed.ncbi.nlm.nih.gov/22187985/)).
- **Variant type:** Predominantly **missense** (e.g., p.L77P, p.L128P, p.G114D, p.L132P, p.G73D, p.V108D), with some **in-frame deletions** (p.Leu69_Ser72del) and **cryptic splice** variants (c.271C>G producing p.Arg91_Gln130del) ([PMID: 22961558](https://pubmed.ncbi.nlm.nih.gov/22961558/), [PMID: 24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/), [PMID: 24750328](https://pubmed.ncbi.nlm.nih.gov/24750328/), [PMID: 30680856](https://pubmed.ncbi.nlm.nih.gov/30680856/)).
- **Classification:** Pathogenic/likely pathogenic per ACMG (segregation with disease, absence in controls, functional data). Variants are typically **germline**; *de novo* events documented.
- **Allele frequency:** Essentially absent from population databases (gnomAD)—consistent with a rare, penetrant, dominant disorder.
- **Functional consequence:** **Gain-of-function / dominant-negative** on actin regulation (see below), NOT loss-of-function.

**Positional genotype-phenotype correlation.** Ueda et al. showed that **variants between residues 184 and 245 produce isolated (monogenic) FSGS**, while **variants between residues 57 and 184 cause the dual CMT/FSGS phenotype** ([PMID: 37491439](https://pubmed.ncbi.nlm.nih.gov/37491439/)). The paper states: *"Variants between residues 184 and 245 of INF2, an actin assembly factor, produce the monogenic FSGS phenotype. Meanwhile, variants between residues 57 and 184 cause a dual-faceted disease involving peripheral neurons and podocytes."* Mechanistically, CMT/FSGS variants (G73D, V108D) caused more severe cytoskeletal disruption and mitochondrial fragmentation than FSGS-only variants (T161N, N202S), providing a molecular basis for why the more N-terminal variants add the neuropathy.

**Gain-of-function evidence.** Subramanian et al. demonstrated that the R218Q point mutation, but not the knockout allele, confers susceptibility to glomerular disease in mice — *"R218Q INF2 mice are susceptible to glomerular disease, in contrast to INF2 knockout mice"* — and cellular assays showed the mutation alters the actin cytoskeleton via a gain-of-function effect ([PMID: 39536114](https://pubmed.ncbi.nlm.nih.gov/39536114/), [PMID: 38915495](https://pubmed.ncbi.nlm.nih.gov/38915495/)). Labat-de-Hoz et al. summarize: *"These mutations disrupt INF2 regulation, leading to excessive actin polymerization"* ([PMID: 39586895](https://pubmed.ncbi.nlm.nih.gov/39586895/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** The variant *position* is the dominant modifier. No specific modifier genes, disease-specific epigenetic marks, or chromosomal abnormalities are established for CMTDIE.

**Gene/GO annotations.** *INF2* — GO:0007015 (actin filament organization), GO:0051017 (actin filament bundle assembly), GO:0000266 (mitochondrial fission), GO:0032956 (regulation of actin cytoskeleton organization). Cellular component: GO:0005783 (endoplasmic reticulum), GO:0005884 (actin filament).

---

## Section 5: Environmental Information

CMTDIE is a **monogenic disease with no established environmental cause**. There are no implicated toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents. The only environmental dimension is experimental: in mouse models, superimposed glomerular injury (PAN, protamine sulfate) is required to unmask the renal phenotype in R218Q knock-in animals ([PMID: 38915495](https://pubmed.ncbi.nlm.nih.gov/38915495/), [PMID: 27350175](https://pubmed.ncbi.nlm.nih.gov/27350175/)), suggesting—by inference—that podocyte stressors may modulate onset in humans. Standard nephroprotective avoidance of nephrotoxins is prudent but not disease-specific.

---

## Section 6: Mechanism / Pathophysiology

### Ordered causal chain

```
1. Heterozygous missense/in-frame mutation in INF2 DID (exons 2–4)
      │  leads to
2. Loss of DID-mediated autoinhibition of INF2 (normally held inactive by a
   CAP1 / lysine-acetylated-actin complex bound to the DID)
      │  results in
3. Constitutive / dysregulated INF2 activity → EXCESSIVE ACTIN POLYMERIZATION
   (gain-of-function; NOT haploinsufficiency)
      │
      ├──────────── BRANCH A: SCHWANN CELL (peripheral nerve) ────────────┐
      │  4a. Perturbation of the INF2–MAL–CDC42 myelination pathway         │
      │        leads to                                                      │
      │  5a. Global disruption of the Schwann-cell actin cytoskeleton;       │
      │      abnormal β-actin accumulation in Schwann cell cytoplasm         │
      │        results in                                                    │
      │  6a. Chronic demyelination/remyelination + progressive axonal loss   │
      │        → intermediate nerve conduction velocities                    │
      │        → CMT phenotype (distal weakness, atrophy, pes cavus)         │
      │                                                                      │
      └──────────── BRANCH B: PODOCYTE (kidney glomerulus) ────────────────┘
         4b. Disrupted INF2 sequestration of Dynll1 → Dynll1 captured by PI31
               leads to
         5b. Dynein-mediated transport of nephrin to the proteasome →
             proteasome-mediated nephrin degradation → slit-diaphragm loss
               (in parallel) abnormal mitochondrial fission/adhesion defects
               results in
         6b. Foot-process effacement, proteinuria → FSGS → ESRD (3rd–4th decade)

7. CONVERGENT TERMINAL STEP (both cell types): excess F-actin drives MRTF/SRF
   transcriptional reprogramming + abnormal mitochondrial dynamics →
   mitotic abnormalities → p53-mediated cell death → cell loss
```

Steps 1–3 and the podocyte branch (4b–6b) are experimentally demonstrated; the Schwann-cell branch (4a–6a) is supported by human nerve pathology and INF2–MAL interaction data but the in-vivo chain in nerve is partly inferred. Step 7 is drawn from cell-biology/review synthesis.

### Detail by category

**Molecular pathways.** The central lesion is dysregulated **actin polymerization** by an ER-anchored formin. In Schwann cells, INF2 acts through the **INF2–MAL–CDC42** pathway; Boyer et al. showed *"INF2 colocalizes and interacts with MAL in Schwann cells. The INF2 mutants perturbed the INF2-MAL-CDC42 pathway"* ([PMID: 22187985](https://pubmed.ncbi.nlm.nih.gov/22187985/)). Downstream, excess G-/F-actin signaling engages the **MRTF/SRF** transcriptional axis ([PMID: 39586895](https://pubmed.ncbi.nlm.nih.gov/39586895/)). INF2 is normally activated physiologically through *"calmodulin binding, KAc-actin deacetylation, G-actin binding, or association with the Cdc42 GTPase"* — regulatory inputs bypassed by DID mutations.

**Cellular processes.** Dysregulated actin dynamics, defective **intracellular/vesicular trafficking**, abnormal **mitochondrial fission and fusion** (INF2 nucleates actin at ER–mitochondria contact sites to drive DRP1-mediated fission), impaired cell adhesion, and ultimately **p53-mediated cell death** ([PMID: 39586895](https://pubmed.ncbi.nlm.nih.gov/39586895/), [PMID: 39184068](https://pubmed.ncbi.nlm.nih.gov/39184068/), [PMID: 39774009](https://pubmed.ncbi.nlm.nih.gov/39774009/)).

**Protein dysfunction.** DID mutations abolish the DID–DAD (diaphanous autoregulatory domain) autoinhibitory clamp, releasing the FH2 domain to over-nucleate actin. This is a **gain-of-function**/dominant mechanism, definitively shown because point mutants but not knockouts cause disease ([PMID: 39536114](https://pubmed.ncbi.nlm.nih.gov/39536114/)).

**Metabolic / mitochondrial changes.** Mutant INF2 causes abnormal mitochondrial dynamics and fragmentation; CMT/FSGS variants produce more severe mitochondrial fragmentation than FSGS-only variants ([PMID: 37491439](https://pubmed.ncbi.nlm.nih.gov/37491439/)). Mitochondrial-associated ER membrane (MAM) actin dynamics are implicated in podocyte injury ([PMID: 41864363](https://pubmed.ncbi.nlm.nih.gov/41864363/)).

**Tissue damage mechanisms.** Schwann cell: Mathis et al. examined six CMTDIE nerve biopsies and reported that *"these lesions reflect a global disorder of the actin cytoskeleton in Schwann cells and that CMTDIE is the first peripheral nerve disorder associated with a Schwann cell actinopathy,"* including *"abnormal accumulation of β-actin in the cytoplasm of Schwann cells"* ([PMID: 24487800](https://pubmed.ncbi.nlm.nih.gov/24487800/)). Podocyte: nephrin proteostasis failure and foot-process effacement.

**Biochemical abnormality (podocyte, druggable node).** Sun et al. and Williquett et al. defined the mechanism: *"The R218Q mutation in INF2 disrupted sequestration of Dynll1 by INF2, allowing Dynll1 to be captured by PI31 and promoting dynein-mediated transport of nephrin to the proteasome"* ([PMID: 33443052](https://pubmed.ncbi.nlm.nih.gov/33443052/), [PMID: 39621430](https://pubmed.ncbi.nlm.nih.gov/39621430/)). Proteasome inhibition (bortezomib) or knockdown of PI31/Dynll1 restored nephrin proteostasis and protected R218Q mice against PAN-induced FSGS.

**Terminal transcriptional / cell-death cascade.** Labat-de-Hoz et al. describe how excess actin causes *"altered intracellular trafficking, abnormal mitochondrial dynamics, and profound transcriptional reprogramming via the MRTF/SRF complex, resulting in mitotic abnormalities and p53-mediated cell death"* ([PMID: 39586895](https://pubmed.ncbi.nlm.nih.gov/39586895/)).

**Cell types (CL terms):** Schwann cell (CL:0002573), podocyte (CL:0000653). **Anatomy (UBERON):** peripheral nerve (UBERON:0000044), renal glomerulus (UBERON:0000074). **GO biological processes:** GO:0007015 (actin filament organization), GO:0000266 (mitochondrial fission), GO:0006511 (ubiquitin-dependent protein catabolic process).

---

## Section 7: Anatomical Structures Affected

**Organ level.**
- **Primary:** Peripheral nervous system (peripheral nerves; UBERON:0000044) and kidney (renal glomerulus; UBERON:0000074).
- **Body systems:** Nervous system (peripheral) and urinary/renal system.
- **Secondary:** Skeletal deformities secondary to neuropathy (pes cavus, kyphoscoliosis); ESRD complications (cardiovascular, anemia, mineral-bone disease).

**Tissue and cell level.**
- **Nervous tissue:** myelinating **Schwann cells** (CL:0002573) — the principal cellular target in nerve; secondary axonal loss.
- **Renal tissue:** glomerular visceral epithelial cells (**podocytes**, CL:0000653) — the principal renal target; the slit diaphragm (nephrin/podocin) is the molecular casualty.

**Subcellular level (GO cellular component).** Endoplasmic reticulum (GO:0005783, where ER-anchored INF2 resides), actin cytoskeleton (GO:0015629), mitochondrion (GO:0005739, abnormal fission/fusion), proteasome complex (GO:0000502, nephrin degradation), ER–mitochondria contact site / MAM.

**Localization / lateralization.** Neuropathy is **bilateral, symmetric, length-dependent** (distal legs first). Renal involvement is bilateral (systemic glomerular disease).

---

## Section 8: Temporal Development

**Onset.** Neuropathy typically begins in **childhood to adolescence** (mean CMT onset ~11.5 years, range 3–17) with insidious, slowly progressive distal weakness ([PMID: 30680856](https://pubmed.ncbi.nlm.nih.gov/30680856/)). Renal onset is variable, ranging from childhood to adulthood ([PMID: 23014460](https://pubmed.ncbi.nlm.nih.gov/23014460/)).

**Progression.** Both components are **chronic and progressive**. Neuropathy progresses slowly over decades. Renal disease progresses from proteinuria to nephrotic syndrome to FSGS: Barua et al. report that *"INF2-related disease showed variable penetrance, with onset of disease ranging widely from childhood to adulthood, and commonly leading to end-stage renal disease in the third and fourth decade of life"* ([PMID: 23014460](https://pubmed.ncbi.nlm.nih.gov/23014460/)). Renal dysfunction is more severe and earlier-onset when neuropathy coexists ([PMID: 24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/)).

**Patterns.** No spontaneous remission. Disease is lifelong. The window for renal intervention is before advanced glomerulosclerosis; the theoretical critical period for any future INF2-directed therapy would be prior to irreversible podocyte loss.

---

## Section 9: Inheritance and Population

**Epidemiology.** CMTDIE is **rare** (no precise prevalence; part of the broader CMT spectrum affecting ~1 in 2,500). Among **autosomal-dominant familial FSGS**, *INF2* mutations explain ~9%: Barua et al. found *"Mutations in INF2 were found in a total of 20 of the 215 families... thereby explaining disease in 9%"* versus only 2/281 sporadic cases ([PMID: 23014460](https://pubmed.ncbi.nlm.nih.gov/23014460/)). By comparison, *ACTN4* accounted for ~3% and *TRPC6* ~2%.

**Inheritance genetics.**
- **Pattern:** Autosomal dominant; *de novo* mutations documented ([PMID: 24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/)).
- **Penetrance:** Variable/incomplete — "variable penetrance, with onset ranging widely from childhood to adulthood" ([PMID: 23014460](https://pubmed.ncbi.nlm.nih.gov/23014460/)).
- **Expressivity:** Variable, including intrafamilial variability where the same variant causes isolated FSGS in one relative and dual CMT/FSGS in another ([PMID: 25943269](https://pubmed.ncbi.nlm.nih.gov/25943269/)).
- **Anticipation, mosaicism, founder effects, consanguinity:** Not established (dominant, non-repeat-expansion disease; consanguinity not relevant).

**Population demographics.** Reported across diverse populations—European, Korean ([PMID: 24750328](https://pubmed.ncbi.nlm.nih.gov/24750328/)), Chinese ([PMID: 25943269](https://pubmed.ncbi.nlm.nih.gov/25943269/), [PMID: 31515790](https://pubmed.ncbi.nlm.nih.gov/31515790/))—with no ethnic predilection. No strong sex bias reported for the Mendelian disease.

---

## Section 10: Diagnostics

**Clinical tests.**
- **Electrophysiology (key):** Nerve conduction studies show **intermediate motor NCV** with both demyelinating and axonal features—the diagnostic signature ([PMID: 24750328](https://pubmed.ncbi.nlm.nih.gov/24750328/)).
- **Urinalysis / renal labs:** Proteinuria screening is essential in every CMT patient — *"we strongly suggest to screen for proteinuria in CMT patients, in order to identify patients with this renal-neurologic phenotype in an early stage"* ([PMID: 25439738](https://pubmed.ncbi.nlm.nih.gov/25439738/)). Serum albumin, creatinine, eGFR track renal function.
- **Nerve biopsy (sural):** Chronic demyelination/remyelination, progressive axonal loss, whorl-like Schwann-cell proliferations, abnormal β-actin accumulation — a Schwann-cell actinopathy ([PMID: 24487800](https://pubmed.ncbi.nlm.nih.gov/24487800/)).
- **Renal biopsy:** FSGS (or occasionally minimal-change/IgA histology) ([PMID: 29038887](https://pubmed.ncbi.nlm.nih.gov/29038887/)).

**Genetic testing (definitive).** Targeted **single-gene *INF2* sequencing (exons 2–4)** or CMT/FSGS **gene panels**; **whole-exome sequencing** has identified novel variants (e.g., p.L132P) ([PMID: 24750328](https://pubmed.ncbi.nlm.nih.gov/24750328/)). Screening should not be restricted to patients with combined neuro-renal disease, since *INF2* variants can cause isolated CMT ([PMID: 30680856](https://pubmed.ncbi.nlm.nih.gov/30680856/)) or isolated FSGS. *INF2* testing is strongly recommended in any patient with CMT plus early nephropathy ([PMID: 24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/)). Diagnosis via genetics can sometimes obviate renal biopsy ([PMID: 27733133](https://pubmed.ncbi.nlm.nih.gov/27733133/)).

**Clinical criteria / differential diagnosis.** Differentiate from other intermediate CMTs (CMT1X/*GJB1*, DI-CMT from *DNM2*, *YARS*), CMT1A (*PMP22* duplication), and isolated genetic FSGS (*NPHS2*, *TRPC6*, *ACTN4*, *WT1*). The combination of intermediate NCV **plus** proteinuria/FSGS strongly points to *INF2*.

**Screening.** Cascade genetic testing of at-risk relatives; urine protein screening in known carriers. No newborn screening exists.

---

## Section 11: Outcome / Prognosis

**Renal outcome.** Progressive to ESRD, "commonly leading to end-stage renal disease in the third and fourth decade of life" ([PMID: 23014460](https://pubmed.ncbi.nlm.nih.gov/23014460/)). Renal disease is generally steroid-resistant.

**Key transplant prognostic distinction.** Genetic (*INF2*) FSGS **does not recur** after kidney transplantation, in sharp contrast to idiopathic FSGS: *"Whilst patients with FSGS without a confirmed genetic cause have a high recurrence rate in the transplanted organ, patients with a mutation generally exhibit no recurrence and have a good prognosis"* ([PMID: 27733133](https://pubmed.ncbi.nlm.nih.gov/27733133/)). Direct clinical confirmation: in an *INF2* family with 14 affected members, *"Four members received a kidney transplant without disease recurrence"* ([PMID: 29038887](https://pubmed.ncbi.nlm.nih.gov/29038887/)). This is a **major counseling anchor**—transplantation offers durable renal replacement.

**Neurologic outcome.** Slowly progressive disability from distal weakness, atrophy, and foot deformity; not typically life-limiting on its own. Life expectancy is governed largely by renal outcome and transplant success.

**Prognostic factors.** Variant position (dual vs isolated phenotype), age at renal onset, degree of proteinuria/glomerulosclerosis at diagnosis.

---

## Section 12: Treatment

**No disease-specific/curative therapy currently exists.** Management is supportive and organ-directed.

**Neurologic / supportive-rehabilitative.**
- Physical therapy, occupational therapy, ankle-foot orthoses, orthopedic management of pes cavus/kyphoscoliosis (NCIT: Physical Therapy, Orthotic Device). Symptomatic pain management as needed.

**Renal.**
- RAAS blockade (ACE inhibitors/ARBs) for proteinuria (antiproteinuric, nephroprotective; NCIT: ACE Inhibitor, Angiotensin Receptor Antagonist). FSGS here is generally steroid-resistant, so immunosuppression is of limited value.
- **Renal replacement:** dialysis and **kidney transplantation** (NCIT: Kidney Transplantation)—the latter with excellent, non-recurring outcomes ([PMID: 27733133](https://pubmed.ncbi.nlm.nih.gov/27733133/)).

**Experimental / emerging (mechanism-directed).**
- **Proteasome inhibition:** Bortezomib restored nephrin proteostasis and protected R218Q mice — *"Suppression of proteasome-mediated proteolysis with proteasome inhibitors is a new therapeutic strategy for inverted formin 2-mediated FSGS"* ([PMID: 39621430](https://pubmed.ncbi.nlm.nih.gov/39621430/)). Targeting the PI31–Dynll1 interaction is a proposed node.
- **Allele-selective silencing (ASO/siRNA):** Because knockout is non-pathogenic while the point mutant is, selectively silencing the mutant allele is a rational (untested-in-human) strategy.
- No pharmacogenomic, gene-therapy, cell-therapy, or immunotherapy protocols are established for CMTDIE.

**Treatment strategy.** Genotype-guided: confirm *INF2* variant, monitor proteinuria and nerve function, initiate RAAS blockade early, plan for transplantation, and counsel on non-recurrence.

---

## Section 13: Prevention

**Primary prevention.** Not possible for a germline Mendelian disorder. **Genetic counseling** is central: autosomal dominant inheritance means 50% transmission risk; prenatal diagnosis and **preimplantation genetic diagnosis (PGD)** are options for known family variants.

**Secondary prevention.** **Cascade genetic testing** of at-risk relatives and **proteinuria screening** in carriers enables early detection and early RAAS blockade to slow renal progression ([PMID: 25439738](https://pubmed.ncbi.nlm.nih.gov/25439738/)).

**Tertiary prevention.** Nephroprotection (blood-pressure control, avoidance of nephrotoxins), management of ESRD complications, orthopedic/rehabilitative care to preserve mobility, and timely transplantation.

**Immunization / public health / environmental interventions.** Not applicable (non-infectious, non-environmental).

---

## Section 14: Other Species / Natural Disease

- **Taxonomy:** *INF2* orthologs exist in mammals; disease modeling is chiefly in **mouse (*Mus musculus*, NCBI Taxon 10090)**.
- **Orthologous gene:** mouse *Inf2* (NCBI Gene ID 79600).
- **Natural disease:** No well-characterized naturally occurring CMTDIE in companion animals or wildlife is documented (OMIA). The disease is essentially known from humans and engineered models.
- **Comparative biology:** INF2's actin-regulatory and mitochondrial-fission functions are evolutionarily conserved, supporting cross-species mechanistic relevance.
- **Transmission:** Not applicable (non-communicable, germline genetic).

---

## Section 15: Model Organisms

**Mouse models (principal).**

| Model | Type | Key finding | PMID |
|-------|------|-------------|------|
| *Inf2* R218Q knock-in | Point-mutant knock-in | Susceptible to PAN-induced proteinuria/FSGS; demonstrates gain-of-function | [39536114](https://pubmed.ncbi.nlm.nih.gov/39536114/), [38915495](https://pubmed.ncbi.nlm.nih.gov/38915495/) |
| *Inf2* knockout | Null allele | Minimal renal phenotype — does NOT recapitulate disease | [39536114](https://pubmed.ncbi.nlm.nih.gov/39536114/) |
| *Inf2* R218Q knock-in (protamine) | Injury model | Impaired podocyte/slit-diaphragm recovery; nephrin/podocin mislocalization | [27350175](https://pubmed.ncbi.nlm.nih.gov/27350175/) |
| Patient iPSC kidney organoid (S186P) | In vitro human | Recapitulates defective adhesion and mitochondrial phenotypes | [38915495](https://pubmed.ncbi.nlm.nih.gov/38915495/) |

**Phenotype recapitulation.** The R218Q knock-in reproduces the **renal** phenotype (only after a second-hit injury) and demonstrates the gain-of-function mechanism and the therapeutic tractability of proteasome inhibition. Human iPSC-derived podocyte organoids recapitulate the adhesion/mitochondrial defects.

**Model limitations.** (1) The **neuropathy** component is poorly modeled—published mouse work focuses on kidney, not Schwann-cell disease. (2) Baseline mice are near-normal; a stressor is required to unmask renal disease, so the models capture *susceptibility* rather than spontaneous progressive FSGS. (3) The positional genotype-phenotype gradient (why some variants add neuropathy) is not fully reconstructed in vivo.

**Resources:** MGI (mouse *Inf2*), patient-derived iPSC/organoid lines.

---

## Mechanistic Model / Interpretation

CMTDIE is best understood as a **single molecular lesion producing a two-organ actinopathy**. A DID mutation releases INF2 from autoinhibition, and the resulting excess/dysregulated actin polymerization is simultaneously toxic to the two most architecturally demanding cell types in the body—myelinating Schwann cells and podocytes—both of which depend on exquisitely controlled actin cytoskeletons for their elaborate membrane processes (myelin wraps; foot processes/slit diaphragm).

```
        INF2 DID mutation (gain-of-function)
                     │
        excess/dysregulated actin polymerization
                     │
      ┌──────────────┴───────────────┐
   SCHWANN CELL                    PODOCYTE
  (INF2–MAL–CDC42            (Dynll1→PI31→dynein→
   pathway perturbed;         proteasomal nephrin loss;
   β-actin accumulation)      mitochondrial/adhesion defects)
      │                            │
 demyelination +               foot-process effacement
 axonal loss                   → FSGS
      │                            │
 intermediate-NCV               proteinuria → ESRD
 neuropathy                     (3rd–4th decade)
      └──────────┬────────────────┘
        MRTF/SRF reprogramming + abnormal
        mitochondrial dynamics + p53 cell death
        (convergent terminal cell-loss step)
```

The **positional gradient** (residues 57–184 → dual; 184–245 → renal-only) implies that the N-terminal DID region governs an interaction (plausibly the Schwann-cell INF2–MAL–CDC42 axis) whose disruption is required to add neuropathy, whereas podocyte injury is triggered across a broader mutational span. The **gain-of-function** nature reframes therapy: rather than replacing lost function, the goal is to *reduce* aberrant activity—hence the appeal of allele-selective silencing (mimicking the benign knockout) and downstream proteasome inhibition (rescuing nephrin).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|------|-----------------|--------------|
| [22187985](https://pubmed.ncbi.nlm.nih.gov/22187985/) | *INF2 mutations in CMT with glomerulopathy* | Establishes INF2 DID as cause in 75% of CMT+FSGS; INF2–MAL–CDC42 in Schwann cells |
| [37491439](https://pubmed.ncbi.nlm.nih.gov/37491439/) | *Cytoskeletal/structural effects of INF2 variants* | Positional genotype-phenotype gradient (57–184 dual; 184–245 renal-only) |
| [39536114](https://pubmed.ncbi.nlm.nih.gov/39536114/) | *INF2 causes kidney disease through gain-of-function* | Point-mutant but not knockout causes disease → gain-of-function |
| [38915495](https://pubmed.ncbi.nlm.nih.gov/38915495/) | *Missense mutant gain-of-function INF2-FSGS* | R218Q knock-in + organoid recapitulate adhesion/mitochondrial defects |
| [24487800](https://pubmed.ncbi.nlm.nih.gov/24487800/) | *Neuropathology: Schwann cell actinopathy* | Defines nerve pathology as Schwann-cell actinopathy; β-actin accumulation |
| [23014460](https://pubmed.ncbi.nlm.nih.gov/23014460/) | *INF2 in familial vs sporadic FSGS* | INF2 = 9% of AD familial FSGS; variable penetrance; ESRD in 3rd–4th decade |
| [33443052](https://pubmed.ncbi.nlm.nih.gov/33443052/) | *Dysregulated dynein trafficking of nephrin* | Podocyte mechanism: nephrin mistrafficking |
| [39621430](https://pubmed.ncbi.nlm.nih.gov/39621430/) | *Dynll1-PI31 / proteasome target* | Dynll1→PI31→proteasomal nephrin loss; proteasome inhibition therapeutic |
| [39586895](https://pubmed.ncbi.nlm.nih.gov/39586895/) | *Regulation of INF2 in inherited disorders* | Excess actin → MRTF/SRF + p53 cell death; physiological activators |
| [27733133](https://pubmed.ncbi.nlm.nih.gov/27733133/) | *Diagnosing FSGS without biopsy* | Genetic FSGS does not recur post-transplant |
| [29038887](https://pubmed.ncbi.nlm.nih.gov/29038887/) | *INF2 with non-FSGS histology* | 4 transplants without recurrence; histologic heterogeneity |
| [30680856](https://pubmed.ncbi.nlm.nih.gov/30680856/) | *Cryptic splice INF2, minimal renal* | INF2 can cause isolated CMT; expands testing indications |
| [24174593](https://pubmed.ncbi.nlm.nih.gov/24174593/) | *De novo INF2 mutations* | De novo events; broader phenotype (ID, hearing loss) |
| [25439738](https://pubmed.ncbi.nlm.nih.gov/25439738/) | *CMT: are you testing for proteinuria?* | Clinical mandate to screen CMT patients for proteinuria |

**Evidence source types:** Human clinical/genetic (case series, pedigrees, cohort genotyping); model organism (R218Q knock-in and knockout mice); in vitro (patient iPSC organoids, cultured podocytes); computational/structural (variant modeling).

---

## Limitations and Knowledge Gaps

1. **Neuropathy mechanism underexplored in vivo.** Mouse work centers on kidney; no robust mouse model reproduces the Schwann-cell neuropathy, leaving the INF2–MAL–CDC42 chain partly inferential.
2. **Positional gradient not mechanistically closed.** Why residues 57–184 add neuropathy while 184–245 spare nerve is correlative; the specific N-terminal interaction responsible is not proven.
3. **Epidemiology imprecise.** No population-level prevalence/incidence for CMTDIE specifically; frequency is anchored to familial-FSGS cohorts.
4. **Penetrance/expressivity unexplained.** Variable and intrafamilial variability lack identified modifiers (genetic or environmental).
5. **No human therapeutic data.** Proteasome inhibition and allele-selective silencing are preclinical; efficacy/safety in patients is unknown.
6. **Second-hit requirement in models** complicates translation—human triggers of renal onset are not defined.
7. **QoL data absent.** No formal EQ-5D/SF-36/PROMIS metrics for the dual disability.

---

## Proposed Follow-up Experiments / Actions

1. **Develop a neuropathy-competent model** — Schwann-cell-specific R218Q/G73D knock-in mice or patient iPSC-derived Schwann cells/organoids to test the INF2–MAL–CDC42 hypothesis and screen neuroprotective compounds.
2. **Test allele-selective silencing** (ASO/siRNA against the mutant *INF2* allele) in R218Q knock-in mice for both renal and (once modeled) neural readouts, leveraging the benign-knockout rationale.
3. **Advance proteasome-axis therapeutics** — dose-ranging bortezomib and PI31–Dynll1 interaction inhibitors in knock-in models with proteinuria and nephrin proteostasis endpoints.
4. **Structure-function mapping** of DID residues 57–245 to explain the phenotype gradient (co-IP/proximity assays for MAL/CDC42/Dynll1 binding across variants).
5. **Build a CMTDIE patient registry** capturing genotype, NCV, renal trajectory, transplant outcomes, and QoL to quantify penetrance, ESRD timing, and non-recurrence rates prospectively.
6. **Modifier discovery** — WGS + expression profiling in variable-expressivity families to find genetic/environmental modifiers of neural vs renal severity.
7. **Clinical guideline** — codify universal proteinuria screening in CMT and *INF2* testing in isolated CMT or FSGS, plus counseling on transplant non-recurrence.

---

*Report compiled from 8 confirmed findings and 27 reviewed papers across 5 investigation iterations. Ontology suggestions: MONDO:0013758; genes/GO: INF2 (GO:0007015, GO:0000266, GO:0005783); cells CL:0002573 (Schwann cell), CL:0000653 (podocyte); anatomy UBERON:0000044 (peripheral nerve), UBERON:0000074 (renal glomerulus); phenotypes HP:0000097 (FSGS), HP:0000093 (proteinuria), HP:0001761 (pes cavus), HP:0003774 (ESRD).*


## Artifacts

- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Dominant_Intermediate_E-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Charcot-Marie-Tooth_Disease_Dominant_Intermediate_E-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 22 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23014460` *(abstract only)*: "variable penetrance, with onset ranging widely from childhood to adulthood"
  - closest text in source: "INF2-related disease showed variable penetrance, with onset of disease ranging widely from childhood to adulthood, and commonly leading to end-stage renal disease in the third and fourth decade of life"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013758` (3 mentions) - the report calls it "MONDO"; MONDO calls it **Charcot-Marie-Tooth disease dominant intermediate E**
- `HP:0001761` (2 mentions) - the report calls it "Physical manifestation", "pes cavus"; HP calls it **Pes cavus**
- `HP:0003693` (1 mention) - the report calls it "Clinical sign"; HP calls it **Distal amyotrophy**
- `HP:0002751` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Kyphoscoliosis**
- `HP:0030181` (1 mention) - the report calls it "variable NCV"; HP calls it **Gordon reflex**
- `HP:0000097` (2 mentions) - the report calls it "Pathology/lab", "FSGS"; HP calls it **Focal segmental glomerulosclerosis**
- `HP:0000093` (2 mentions) - the report calls it "Laboratory abnormality", "proteinuria"; HP calls it **Proteinuria**
- `HP:0000100` (1 mention) - the report calls it "Clinical"; HP calls it **Nephrotic syndrome**
- `HP:0003774` (2 mentions) - the report calls it "Clinical", "ESRD"; HP calls it **Stage 5 chronic kidney disease**
- `CL:0002573` (3 mentions) - the report calls it "Schwann cells", "Nervous tissue:** myelinating **Schwann cells", "Schwann cell"; CL calls it **Schwann cell**
- `UBERON:0000044` (3 mentions) - the report calls it "peripheral nerve"; UBERON calls it **dorsal root ganglion**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0106487` (1 mention), reported as "Symptom" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0009053` (1 mention) - the report calls it "distal lower limb amyotrophy"; HP calls it **Distal lower limb muscle weakness**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001761` - called "Physical manifestation", "pes cavus"
- `HP:0000097` - called "Pathology/lab", "FSGS"
- `HP:0000093` - called "Laboratory abnormality", "proteinuria"
- `HP:0003774` - called "Clinical", "ESRD"
- `CL:0002573` - called "Schwann cells", "Nervous tissue:** myelinating **Schwann cells", "Schwann cell"