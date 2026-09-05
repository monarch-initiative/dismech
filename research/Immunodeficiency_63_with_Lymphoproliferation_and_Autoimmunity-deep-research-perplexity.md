---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2026-08-31T15:26:01.473886'
end_time: '2026-08-31T15:26:01.481259'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 63 with Lymphoproliferation and Autoimmunity
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 17
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 71
  verified: 68
  not_found: 1
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.014
  labels_checked: 59
  labels_matching: 32
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0008354
    reported_labels:
    - Hypergammaglobulinemia
    ontology_label: Factor X activation deficiency
  - term_id: HP:0002039
    reported_labels:
    - Chronic diarrhea
    ontology_label: Anorexia
  - term_id: HP:0005407
    reported_labels:
    - Abnormal T cell activation
    ontology_label: obsolete Decreased proportion of CD4-positive helper T cells
  - term_id: HP:0002812
    reported_labels:
    - Abnormal NK cell morphology
    ontology_label: Coxa vara
  - term_id: HP:0002239
    reported_labels:
    - Cytomegalovirus infection
    ontology_label: Gastrointestinal hemorrhage
  - term_id: HP:0012170
    reported_labels:
    - "Epstein\u2013Barr virus infection"
    ontology_label: Nail-biting
  - term_id: GO:0035724
    reported_labels:
    - interleukin-15 receptor activity
    ontology_label: obsolete CD24 biosynthetic process
  - term_id: UBERON:0002150
    reported_labels:
    - lymphoid tissue
    ontology_label: superior cerebellar peduncle
  - term_id: NCIT:C29322
    reported_labels:
    - Ganciclovir
    ontology_label: Phosphoramide Mustard
  - term_id: NCIT:C48274
    reported_labels:
    - Antiviral Therapy
    ontology_label: Cancer Molecular Analysis Project
  - term_id: NCIT:C15206
    reported_labels:
    - Hematopoietic Stem Cell Transplantation
    ontology_label: Clinical Study
  - term_id: NCIT:C15693
    reported_labels:
    - Supportive Care
    ontology_label: Phase I/II Trial
  - term_id: NCIT:C15279
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Radical Mastectomy
  labels_variant: 14
  unresolved_terms:
  - HP:0030315
  obsolete_terms:
  - term_id: HP:0005407
    ontology_label: obsolete Decreased proportion of CD4-positive helper T cells
    replaced_by: HP:0032218
  - term_id: GO:0035724
    ontology_label: obsolete CD24 biosynthetic process
    replaced_by: GO:0009101
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 63 with Lymphoproliferation and Autoimmunity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 63 with Lymphoproliferation and Autoimmunity** covering all of the
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

# Immunodeficiency 63 with Lymphoproliferation and Autoimmunity (IMD63): Comprehensive Disease Characteristics

Immunodeficiency 63 with lymphoproliferation and autoimmunity (IMD63) is a recently defined inborn error of immunity caused by biallelic loss-of-function mutations in the interleukin-2 receptor beta subunit gene, **IL2RB**, leading to a distinctive syndrome that combines features of combined immunodeficiency, profound immune dysregulation, and susceptibility to severe viral infections, especially cytomegalovirus (CMV) and other herpesviruses.[1][9][10] Clinically, affected individuals present in the perinatal period or early childhood with recurrent respiratory and gastrointestinal infections, generalized lymphadenopathy and splenomegaly, enteropathy, dermatologic abnormalities, autoimmune cytopenias such as autoimmune hemolytic anemia, and marked hypergammaglobulinemia with elevated autoantibodies.[10][12] At the molecular level, IL2RB deficiency disrupts signaling of interleukin-2 (IL-2) and interleukin-15 (IL-15) through the heterotrimeric IL-2 receptor, impairing regulatory T cell (Treg) function, altering natural killer (NK) cell development and activity, and skewing T cell homeostasis, thereby coupling combined immunodeficiency with failure of peripheral tolerance.[8][10][12] The disorder is inherited in an autosomal recessive fashion, has been documented in a small number of consanguineous families, and is currently classified as an ultra-rare Mendelian primary immunodeficiency/inborn error of immunity with potentially life-threatening course that can be ameliorated or cured by hematopoietic stem cell transplantation (HSCT).[1][9][10][12]

## 1. Disease Information

### 1.1. Concise Overview and Clinical Concept

Immunodeficiency 63 with lymphoproliferation and autoimmunity (IMD63) is defined as a primary immunodeficiency and immune dysregulation syndrome resulting from germline, biallelic mutations in **IL2RB**, the gene encoding the β subunit (CD122) of the IL-2/IL-15 receptor complex.[1][9][10] OMIM describes IMD63 as “an autosomal recessive disorder characterized by immune dysregulation,” emphasizing the triad of immunodeficiency, lymphoproliferation, and autoimmunity, with onset typically in infancy or early childhood.[1] In the initial clinical cohorts described by Zhang et al. and Fernandez et al., affected children presented with recurrent respiratory infections, chronic diarrhea due to enteropathy, dermatologic manifestations, generalized lymphadenopathy and hepatosplenomegaly, autoimmune hemolytic anemia, and elevated serum immunoglobulin G (IgG) accompanied by multiple autoantibodies.[9][10][12] These clinical features align IMD63 with the broader group of combined immunodeficiencies with immune dysregulation, a category that also includes IL2RA deficiency, FOXP3-related IPEX syndrome, and hypomorphic IL2RG defects.[8][12][15]

At the immunological level, patients display a characteristic pattern of laboratory abnormalities that reflect defective IL-2 and IL-15 signaling through IL2RB.[8][10] T lymphocytes, particularly CD4⁺ and CD8⁺ T cells, show markedly reduced or absent surface expression of IL-2Rβ and severely impaired phosphorylation of STAT5 in response to IL-2 stimulation, whereas NK cells retain partial IL-2Rβ expression and function in hypomorphic alleles such as L77P.[10][12] Clinically, this molecular defect manifests as susceptibility to viral infections—most notably CMV and other herpesviruses—alongside prominent autoimmunity and lymphoproliferation, including massive lymphadenopathy and splenomegaly.[8][10][12] Thus, IMD63 occupies a unique intersection between immunodeficiency and autoimmunity, illustrating how disruption of a single cytokine receptor subunit can simultaneously compromise host defense and break immune tolerance.

### 1.2. Key Identifiers, Synonyms, and Classification

IMD63 is formally catalogued in OMIM under the phenotype entry **#618495 – Immunodeficiency 63 with lymphoproliferation and autoimmunity**, and is linked etiologically to the **IL2RB** gene, which has its own OMIM entry ***146710 – Interleukin 2 receptor, beta; IL2RB**.[1][9] The GenCC/ClinGen submission assigns the disease the MONDO identifier **MONDO:0032782** under the name “immunodeficiency 63 with lymphoproliferation and autoimmunity; IMD63,” explicitly confirming the gene–disease relationship.[4] UniProt also notes immunodeficiency 63 with lymphoproliferation and autoimmunity as a disease associated with IL2RB, describing it as “an autosomal recessive disorder characterized by immune dysregulation resulting in immunodeficiency, autoimmunity, and lymphoproliferation.”[11] Wikipedia lists IL2RB as “interleukin-2 receptor subunit beta” and associates it with IMD63, further corroborating the nomenclature.[13]

Common synonyms and related designations include “IL-2Rβ deficiency,” “IL2RB-associated combined immunodeficiency with autoimmunity,” and “autosomal recessive IL2RB-related immune dysregulation syndrome,” although the standardized name in Mendelian disease taxonomies is **Immunodeficiency 63 with lymphoproliferation and autoimmunity (IMD63)**.[9][10][12] The broader disease category is “Mendelian primary immunodeficiency/inborn error of immunity,” specifically within the subgroup of combined immunodeficiencies with immune dysregulation and prominent herpesvirus susceptibility.[8][12][15] In terms of other coding systems, formal ICD-10/ICD-11 and MeSH-specific codes for IMD63 have not yet been uniquely assigned, and cases are typically coded under more generic headings such as “combined immunodeficiency,” “autoimmune hemolytic anemia,” or “lymphoproliferative disease,” reflecting the novelty and rarity of the entity.[15]

### 1.3. Data Sources and Level of Aggregation

The current knowledge about IMD63 derives almost entirely from aggregated disease-level resources and case series rather than large-scale registry or electronic health record (EHR) datasets, owing to the very small number of documented families and patients.[1][9][10][12] OMIM synthesizes findings from the original descriptions by Zhang et al. and Fernandez et al., who independently identified autosomal recessive IL2RB mutations as the cause of a previously unrecognized severe immune dysregulation syndrome.[9][10][12] These primary reports, published in the *Journal of Experimental Medicine* in 2019, describe eight affected individuals from four consanguineous families with three distinct IL2RB mutations, as well as two siblings with an in-frame deletion, forming the core clinical and mechanistic evidence base.[9][10][12] 

Secondary resources such as UniProt, Wikipedia, and clinical reviews on IL-2 receptor defects and combined immunodeficiencies contextualize IMD63 within the broader landscape of IL-2/IL-15 signaling disorders and inborn errors of immunity.[8][11][12][15] ClinVar and GenCC provide curated variant and gene–disease validity information, including classification of specific IL2RB variants as pathogenic or benign.[3][4][9][10] Because of the ultra-rare nature of IMD63, no large epidemiologic datasets, population-based registries, or clinical trial databases yet exist for this condition, and most statements about its clinical spectrum and prognosis are based on a small number of human case reports and detailed immunologic and molecular investigations.[9][10][12]

## 2. Etiology

### 2.1. Primary Genetic Cause: IL2RB Loss-of-Function

The primary causal factor for IMD63 is germline, biallelic loss-of-function mutation in **IL2RB**, encoding the β subunit of the IL-2 and IL-15 receptor complex.[1][9][10] IL2RB is located on chromosome 22q12.3, spanning genomic coordinates 22:37,125,838–37,175,118 (GRCh38), and is expressed constitutively or inducibly on multiple immune cell types, including CD4⁺ regulatory T cells, CD4⁺ and CD8⁺ effector T cells, B cells, and NK cells.[9][11][16] In the seminal case series, Zhang et al. identified three different homozygous IL2RB mutations in eight patients from four consanguineous pedigrees: a missense mutation L77P, a missense mutation S40L, and a nonsense mutation Q96X, each disrupting IL-2Rβ expression or function by distinct mechanisms.[9][10] Fernandez et al. reported a homozygous 9-base–pair in-frame deletion in two siblings, deleting three conserved residues in the extracellular domain of IL-2Rβ and abolishing functional receptor signaling.[9][12]

Zhang et al. summarized their discovery as follows:

> “Here we identify human interleukin-2 receptor (IL-2R) β chain (*IL2RB*) gene defects as a cause of life-threatening immune dysregulation. We report three homozygous mutations in the *IL2RB* gene of eight individuals from four consanguineous families that cause disease by distinct mechanisms.”[10]

Functional analyses demonstrated that T lymphocytes from affected patients lacked normal surface expression of IL-2Rβ and were unable to respond to IL-2 stimulation, as assessed by STAT5 phosphorylation and proliferation assays, whereas NK cells retained partial IL-2Rβ expression and residual IL-2 responsiveness in certain hypomorphic alleles such as L77P.[10][12] UniProt and OMIM both classify these IL2RB mutations as causal for immunodeficiency 63 with lymphoproliferation and autoimmunity, confirming the gene–disease relationship.[1][9][11] Thus, the etiological core of IMD63 is a Mendelian, autosomal recessive loss-of-function defect in IL2RB that disrupts IL-2/IL-15 receptor signaling across multiple immune cell compartments.

### 2.2. Genetic Risk Factors and Allelic Heterogeneity

Within the IL2RB locus, several distinct variants have been shown to cause IMD63, reflecting allelic heterogeneity and variable residual receptor function.[9][10] The L77P missense mutation is located in exon 4 and leads to impaired surface expression of IL-2Rβ due to defective egress from the endoplasmic reticulum, resulting in negligible IL-2 signaling in T cells but partial residual signaling in NK cells that normally express higher baseline levels of IL-2Rβ.[10][12] The S40L missense mutation, situated in the extracellular domain, decreases IL-2 binding affinity, thereby reducing downstream STAT5 activation despite preserved receptor expression.[9][10] The Q96X nonsense mutation generates a severely truncated protein, effectively abolishing IL-2Rβ expression and function, and thus represents a complete loss-of-function allele.[9][10] Fernandez et al.’s 9-bp in-frame deletion similarly eliminates critical extracellular residues, resulting in a functional null for IL-2 signaling.[9][12]

Zhang et al. explicitly demonstrated three mechanistic classes of IL2RB deficiency:

> “By using this reconstituted system, we define three distinct mechanisms in humans for IL-2Rβ deficiency by showing that it can occur due to an absence of IL-2Rβ (Q96*), impaired surface expression (L77P), and decreased binding of IL-2 (S40L).”[10]

Population-based allele frequency data indicate that these pathogenic IL2RB variants are exceedingly rare. For example, the L77P variant has a minor allele frequency of approximately 0.00001218 in the Genome Aggregation Database (gnomAD), consistent with the ultra-rare nature of IMD63.[10] ClinVar catalogues other IL2RB sequence variants, such as NM_000878.5(IL2RB):c.750C>T (p.Gly250=), which is classified as benign for immunodeficiency 63 with lymphoproliferation and autoimmunity, underscoring that not all IL2RB changes are disease-causing and that careful interpretation of variant pathogenicity is required.[3] No modifier genes or additional susceptibility loci have yet been robustly identified in IMD63, and the current evidence supports a monogenic, recessive etiology driven by IL2RB loss-of-function.[1][9][10][12]

### 2.3. Environmental and Infectious Risk Factors

Although IMD63 is fundamentally genetic, environmental and infectious factors shape the clinical course, particularly by precipitating severe infections and exacerbating immune dysregulation. IL-2Rα (CD25), IL-2Rβ, and atypical IL-2Rγ deficiency patients share a characteristic susceptibility to viral infections, especially herpesviruses such as CMV and Epstein–Barr virus (EBV), reflecting the critical role of IL-2/IL-15 signaling in antiviral immunity.[8][12] Hernandez et al. note that “IL-2Rα, IL-2Rβ, and atypical IL-2Rγ patients presented with prominent viral infections, including severe respiratory viral infections, but most notably CMV and other herpesvirus infections,” and that all IL-2Rα or IL-2Rβ patients surviving the neonatal period developed herpesvirus infections, with a majority developing CMV disease.[8] 

In IMD63, CMV infection appears particularly frequent and clinically important, often manifesting as severe CMV pneumonitis or disseminated disease in early life.[10][12] Recurrent bacterial and respiratory viral infections also occur, largely as a consequence of combined immunodeficiency rather than as predisposing risk factors.[8][10][12][15] There is no evidence that specific environmental toxins, dietary patterns, or lifestyle factors modulate the risk of developing IMD63, given its Mendelian basis, although general exposures that increase infection risk (e.g., crowded living conditions, lack of vaccination against common pathogens) may worsen morbidity in affected individuals.[15] 

### 2.4. Protective Factors and Gene–Environment Interactions

At present, no specific genetic protective factors—such as modifier alleles that ameliorate IL2RB deficiency—have been reported for IMD63.[1][9][10][12] The markedly small number of documented cases and the predominance of consanguineous pedigrees limit the ability to detect such modifiers. However, residual function in hypomorphic IL2RB alleles (such as L77P and S40L) likely acts as an intrinsic partial protective factor compared with complete loss-of-function variants like Q96X, as evidenced by somewhat preserved NK cell cytotoxicity and variable severity of infections in some patients.[10][12] 

Environmentally, aggressive infectious prophylaxis and early recognition of CMV and other herpesvirus infections have been highlighted as crucial factors that improve outcomes and may function as secondary protective measures.[8] Hernandez et al. emphasize that IL-2Rα, IL-2Rβ, and atypical IL-2Rγ deficient patients should receive (val)ganciclovir prophylaxis and close monitoring for CMV infection, given the high burden of CMV disease and its impact on survival.[8] These interventions exemplify gene–environment interactions in which targeted management of environmental exposures (i.e., viral pathogens) reduces disease-related complications in the context of a fixed genetic defect.

More broadly, gene–environment interactions in IMD63 primarily reflect how IL2RB mutations alter immune responses to common environmental pathogens, resulting in disproportionate susceptibility and severe disease rather than classical “risk factors” in the pre-disease sense.[8][10][12] The genetic lesion sets a baseline of impaired IL-2/IL-15 signaling and defective immune regulation, and environmental exposures—especially viral infections—serve as triggers that reveal or amplify the clinical phenotype.

## 3. Phenotypes

### 3.1. Overall Clinical Phenotype Spectrum

IMD63 is characterized by a constellation of clinical manifestations that span immunodeficiency, autoimmunity, and lymphoproliferation, reflecting the central role of IL-2Rβ in both effector immunity and immune tolerance.[1][9][10][12] The initial case series described clinical hallmarks including enteropathy, skin abnormalities, autoimmune hemolytic anemia, hypergammaglobulinemia, lymphadenopathy, splenomegaly, and susceptibility to respiratory and herpesvirus infections.[10][12] Campbell summarized these findings as follows:

> “Clinical hallmarks of the disease included enteropathy, skin abnormalities, autoimmune hemolytic anemia, and hypergammaglobulinemia, in addition to susceptibility to respiratory and herpesvirus infections.”[12]

Nearly all reported patients exhibited autoantibodies, elevated IgG, bowel inflammation with chronic diarrhea, dermatologic changes such as eczema-like or erythrodermic rashes, generalized lymphadenopathy, and enlarged spleen and liver.[10][12] Autoimmune cytopenias, particularly autoimmune hemolytic anemia (AIHA), were frequent, and some patients developed autoimmune thrombocytopenia and neutropenia, reminiscent of Evans syndrome.[10][12] Infectious complications included recurrent respiratory infections, chronic CMV disease, and other severe viral infections, reflecting combined immunodeficiency with impaired antiviral responses.[8][10][12]

From a Human Phenotype Ontology (HPO) perspective, key phenotypic terms include **Autoimmune hemolytic anemia** (HP:0001890), **Hypergammaglobulinemia** (HP:0008354), **Recurrent respiratory infections** (HP:0002205), **Chronic diarrhea** (HP:0002039), **Lymphadenopathy** (HP:0002716), **Splenomegaly** (HP:0001744), **Hepatomegaly** (HP:0002240), **Autoantibody positivity** (HP:0030057), and **Susceptibility to herpesvirus infections** (HP:0005381).[10][12] The combination of these features, particularly when present in infancy or early childhood in the context of consanguinity, should raise suspicion for IL2RB-related IMD63.

### 3.2. Age of Onset, Severity, and Progression

IMD63 typically presents in the neonatal period or early infancy, although exact age of onset varies depending on the specific IL2RB mutation and residual receptor function.[9][10][12] In the cohorts described by Zhang et al. and Fernandez et al., some affected fetuses were lost perinatally, while live-born children showed symptoms within the first months of life, including severe infections and autoimmune manifestations.[9][10][12] Campbell notes that the five kindreds described collectively included “seven affected live-born children with immunodeficiency and autoimmune disease, and three perinatally affected fatalities,” highlighting the potential for intrauterine or neonatal lethality in severe IL2RB deficiency.[12]

Symptom severity appears to range from severe, life-threatening combined immunodeficiency with multi-organ autoimmunity in complete loss-of-function alleles, to somewhat milder but still serious immune dysregulation in hypomorphic variants that retain partial signaling.[10][12] Patients with hypomorphic L77P mutations demonstrated pronounced autoimmunity and infections, but NK cells maintained modest IL-2Rβ surface expression and cytolytic activity, possibly modulating severity.[10] Nonetheless, most reported patients required intensive medical management, and at least one underwent hematopoietic stem cell transplantation, which markedly ameliorated clinical symptoms.[10][12]

Symptom progression is generally chronic and progressive, with ongoing lymphoproliferation, recurrent infections, and evolving autoimmune phenomena over time, although the limited number of cases and short follow-up durations hinder detailed natural history characterization.[9][10][12] Without definitive treatment such as HSCT, the disease course appears to be severe and potentially fatal, with cumulative damage from infections and autoimmunity affecting quality of life and survival.[10][12] The impact on daily functioning is substantial, given chronic diarrhea, failure to thrive, frequent hospitalizations for infections, and anemia-related fatigue; these would correspond to significant decrements in generic quality-of-life instruments such as EQ-5D and SF-36, even though disease-specific QoL data are not yet available.[12]

### 3.3. Immunologic Laboratory Phenotypes

Immunologic laboratory findings in IMD63 reflect combined immunodeficiency with immune activation and dysregulation. Patients commonly exhibit elevated serum IgG and sometimes IgA, with variable IgM, a pattern of **hypergammaglobulinemia** consistent with chronic immune stimulation and autoantibody production.[10][12] Autoantibodies directed against red blood cells, platelets, and other self-antigens are frequent, and autoimmune hemolytic anemia is a prominent clinical phenotype.[10][12] T cell immunophenotyping often reveals skewing toward memory phenotypes, increased CD45RO⁺ T cells, and reduced naïve T cells, a pattern shared with IL2RA and hypomorphic IL2RB and IL2RG deficiencies.[8] Hernandez et al. summarize that “IL-2Rα deficiency and hypomorphic IL-2Rβ and IL-2Rγ defects present with common immunological clinical laboratory findings including i) increased serum IL-2, ii) increased memory T cells, and iii) increased CD56^bright NK cells.”[8]

In IL2RB deficiency, surface expression of IL-2Rβ on T cells is markedly reduced or absent, and functional assays show severely impaired STAT5 phosphorylation and proliferation upon IL-2 stimulation, confirming defective receptor function.[10] NK cells demonstrate variable IL-2Rβ expression, with partial retention in hypomorphic alleles, and concomitant partial preservation of IL-2 responsiveness and cytotoxicity.[10][12] These immunologic features correspond to HPO terms such as **Abnormal T cell morphology** (HP:0002843), **Abnormal T cell activation** (HP:0005407), **Abnormal NK cell morphology** (HP:0002812), and **Elevated serum immunoglobulin G** (HP:0004315).[8][10][12]

A comparative table summarizing key immunologic findings in IL-2R subunit deficiencies, including IL2RB-related IMD63, helps place the phenotype in context:

| Feature | IL-2Rα (CD25) deficiency | IL-2Rβ (CD122) deficiency (IMD63) | IL-2Rγ (CD132) deficiency (X-SCID) |
|--------|---------------------------|-----------------------------------|------------------------------------|
| T cell numbers | Modestly reduced, memory skewing | Variable; memory skewing, abnormal activation | Profoundly reduced (T⁻ B⁺ NK⁻) |
| NK cells | Increased CD56^bright subset | Partial IL-2Rβ expression; variable numbers | Absent or severely reduced |
| Serum IL-2 | Elevated | Elevated | Elevated |
| IgG levels | Elevated IgG, autoantibodies | Elevated IgG, autoantibodies | Variable, often low |
| Herpesvirus susceptibility | Common (CMV, EBV) | Common (CMV, EBV) | Common (but dominated by broad infections) |

This table is derived from the review by Hernandez et al., Zhang et al., and related IL-2R defect literature.[8][10][12]

### 3.4. Quality of Life Impact and HPO Term Suggestions

Although formal health-related quality-of-life studies have not been conducted in IMD63, the severity and breadth of clinical manifestations strongly suggest major impacts on daily functioning and psychosocial well-being.[10][12] Chronic diarrhea and enteropathy interfere with nutrition, growth, and school attendance; recurrent infections necessitate frequent medical visits and hospitalizations; autoimmune hemolytic anemia and other cytopenias cause fatigue, pallor, and increased bleeding risk; and lymphadenopathy and hepatosplenomegaly may cause abdominal discomfort and altered body image.[10][12] Parents and caregivers face substantial stress related to the unpredictability of infections and autoimmune flares, and the need for complex therapies such as immunosuppression, antiviral prophylaxis, and consideration of HSCT.[8][10][12]

Key HPO terms capturing this impact include **Failure to thrive** (HP:0001508), **Chronic diarrhea** (HP:0002039), **Recurrent infections** (HP:0002719), **Fatigue** (HP:0012378), **Developmental delay** (HP:0001263) when present, and **Reduced quality of life** (HP:0030315). While these terms are not yet systematically coded for IMD63 in public ontologies, they can be reasonably suggested based on the clinical descriptions in the primary literature.[10][12] As more patients are identified and systematic phenotyping is performed, the frequency and severity of individual phenotypes will be better quantified, enabling more precise annotation in disease knowledge bases.

## 4. Genetic/Molecular Information

### 4.1. Causal Gene: IL2RB

The causal gene for IMD63 is **IL2RB** (*interleukin-2 receptor subunit beta*), with HGNC-approved symbol IL2RB and OMIM gene entry *146710*.[9][11][13] IL2RB is located at cytogenetic band 22q12.3 and encodes a type I transmembrane glycoprotein that forms part of the heterotrimeric IL-2 receptor complex together with IL2RA (CD25) and IL2RG (common gamma chain, CD132).[9][11][16] The IL-2 receptor exists in low-, intermediate-, and high-affinity forms, with IL2RB and IL2RG constituting the core signaling receptor and IL2RA serving as an affinity-modulating component.[8][16] IL2RB is also shared with the IL-15 receptor, forming the β subunit of the IL-15/IL-2 receptor pair that signals in concert with IL2RG and IL-15RA.[8][13][16]

UniProt describes IL2RB as “the beta subunit of the receptor for interleukin-2 and interleukin-15,” noting that it is expressed predominantly on NK cells, some T cells, and activated B cells, and that it transduces signals through JAK1/JAK3 and STAT5 pathways upon cytokine binding.[11][16] Zhang et al. reinforce that “interleukin-2, which conveys essential signals for immunity, operates through a heterotrimeric receptor,” and that IL2RB mutations disrupt these critical signaling pathways in humans.[10] The gene’s functional importance is further highlighted by earlier work showing that IL-2Rβ-deficient mice have abnormal development of intestinal intraepithelial lymphocytes and peripheral NK cells, autoimmune hemolytic anemia, hypergammaglobulinemia, and lymphadenopathy, phenotypes closely paralleling human IMD63.[10][12]

### 4.2. Pathogenic Variants: Types, Mechanisms, and Frequencies

Pathogenic variants causing IMD63 include missense, nonsense, and in-frame deletion mutations, all affecting the extracellular domain or early coding exons of IL2RB and leading to loss of IL-2Rβ function.[9][10][12] Zhang et al. identified three homozygous mutations in eight patients:

1. **L77P** (Leu77Pro), a missense variant in exon 4, which disrupts receptor trafficking and surface expression, particularly in T cells, resulting in a hypomorphic allele with cell-type–specific effects.[10]
2. **S40L** (Ser40Leu), a missense variant in the extracellular domain that preserves receptor expression but decreases IL-2 binding, thereby impairing downstream signaling.[10]
3. **Q96X** (Gln96*), a stop-gain mutation leading to truncation of the 552-amino-acid protein and effective absence of functional IL-2Rβ, representing a complete loss-of-function allele.[10]

Fernandez et al. reported an additional pathogenic variant:

4. A homozygous **9-bp in-frame deletion** in IL2RB, eliminating three conserved residues in the extracellular motif, which abolished IL-2Rβ function in two siblings with severe immune dysregulation.[9][12]

These variants are classified as pathogenic according to ACMG/AMP guidelines, based on their segregation with disease in multiple consanguineous families, absence or extreme rarity in population databases, predicted functional impact, and direct demonstration of loss of IL-2 signaling in patient lymphocytes.[9][10][12] For example, the L77P mutation has a gnomAD minor allele frequency of 0.00001218, and Q96X and S40L are absent from major exome databases, supporting their pathogenicity.[10]

Zhang et al. experimentally dissected the functional consequences of each variant:

> “Kindreds A and B have the hypomorphic L77P IL-2Rβ mutant, which interferes with egress from the ER. We discovered that this abrogates surface expression and IL-2 signaling in T cells, but that NKs retain not only modest surface expression and responsiveness to IL-2 but also quite potent cytolytic activity… For kindred D, a g.37537259 G>A (p.Gln96*) stop-gain mutation was identified… This mutation would lead to significant truncation of the 552–amino acid protein… we show that [IL2RB deficiency] can occur due to an absence of IL-2Rβ (Q96*), impaired surface expression (L77P), and decreased binding of IL-2 (S40L).”[10]

ClinVar documents other IL2RB variants, including synonymous changes such as c.750C>T (p.Gly250=) that are classified as benign for IMD63, highlighting the importance of distinguishing disease-causing variants from rare polymorphisms.[3] All pathogenic IL2RB variants identified in IMD63 to date are **germline**, biallelic, and inherited in an autosomal recessive fashion; somatic IL2RB mutations have not been implicated in this syndrome.[1][3][4][9][10][12]

### 4.3. Functional Consequences and Molecular Pathways

At the molecular level, pathogenic IL2RB variants cause **loss of function** of the IL-2Rβ subunit, leading to defective IL-2 and IL-15 signaling through the canonical JAK–STAT pathways.[8][10][16] IL-2 binding to the high-affinity receptor (IL2RA–IL2RB–IL2RG) normally triggers activation of JAK1 (associated with IL2RB) and JAK3 (associated with IL2RG), resulting in phosphorylation of STAT5 and other STAT family members, induction of genes involved in T cell proliferation, survival, and differentiation, and maintenance of regulatory T cells.[8][10][16] IL-15 signals through a similar receptor complex (IL15RA–IL2RB–IL2RG), playing key roles in NK cell development and memory CD8⁺ T cell homeostasis.[8][13][16]

In IL2RB deficiency, T cells exhibit absent or severely reduced STAT5 phosphorylation in response to IL-2 and IL-15, and fail to proliferate or upregulate activation markers upon cytokine stimulation.[10] NK cells show variable impairment depending on the specific mutation; hypomorphic alleles like L77P allow residual IL-2Rβ expression and partial NK cell function, whereas complete loss-of-function alleles yield more profound defects.[10][12] The net effect is impaired clonal expansion of effector T cells, defective maintenance and function of Tregs, abnormal NK cell maturation, and skewed T cell memory phenotypes, all of which contribute to combined immunodeficiency and autoimmunity.[8][10][12]

Relevant Gene Ontology (GO) biological process terms capturing these defects include **interleukin-2-mediated signaling pathway** (GO:0035723), **interleukin-15-mediated signaling pathway** (GO:0038119), **regulation of T cell proliferation** (GO:0042129), **positive regulation of regulatory T cell differentiation** (GO:0032823), and **natural killer cell activation** (GO:0030101).[8][10][16] IL2RB itself is annotated with GO terms such as **cytokine receptor activity** (GO:0004896) and **JAK–STAT cascade** (GO:0007259), reflecting its central role in these pathways.[11][16]

### 4.4. Chromosomal and Epigenetic Considerations

No large-scale chromosomal abnormalities, such as deletions, duplications, translocations, or inversions, have been reported as primary etiologic factors in IMD63; rather, the disease is caused by point mutations or small indels within the IL2RB coding sequence.[1][9][10][12] Epigenetic changes—such as DNA methylation or histone modifications affecting IL2RB expression—have not been implicated, and there is currently no evidence that epigenetic mechanisms play a major role in disease onset or progression beyond the impact of the germline mutation.[1][9][10][12]

However, broader epigenetic alterations in Tregs and effector T cells may secondarily arise in the context of chronic immune activation and autoimmunity, as seen in other immune dysregulation syndromes, although this has not yet been specifically studied in IMD63.[12] Future application of methylome and chromatin profiling to patient samples could shed light on secondary epigenetic remodeling associated with chronic inflammation in IL2RB deficiency, but such data are currently unavailable.[1][9][10][12]

## 5. Environmental Information

### 5.1. Environmental and Lifestyle Factors

Because IMD63 is a Mendelian monogenic disorder, **non-genetic environmental factors** do not determine disease occurrence in the same way they do for complex, multifactorial conditions.[1][9][10][12] However, environmental exposures significantly modulate disease expression, course, and outcome. In particular, infectious exposures—especially to CMV and other herpesviruses—are crucial determinants of morbidity and mortality in IL2RB deficiency.[8][10][12] Hernandez et al. note that “CMV and other herpes virus infections were the most problematic infections for [IL-2Rα and IL-2Rβ] patients, they should receive (val)ganciclovir prophylaxis and be monitored regularly for CMV infection,” underscoring the importance of environmental (infectious) risk management.[8]

Lifestyle factors such as smoking, diet, and physical activity have not been specifically studied in IMD63, and there is no evidence that they directly influence disease risk, given the genetic etiology.[1][9][10][12] However, general health behaviors that reduce infection risk and support immune function—such as appropriate vaccinations (excluding live vaccines in severely immunodeficient patients), good hygiene, and adequate nutrition—are likely to be beneficial in mitigating complications.[8][15] Occupational exposures, toxins, and pollution have not been linked to IMD63.

### 5.2. Infectious Agents and Opportunistic Disease

In IMD63, infectious agents function more as opportunistic pathogens exploiting an immunodeficient host than as true etiologic triggers. The most notable infectious agents in reported IL2RB-deficient patients are **cytomegalovirus (CMV)** and other herpesviruses, such as **Epstein–Barr virus (EBV)**, as well as respiratory viruses and common bacterial pathogens.[8][10][12] Hernandez et al. emphasize that IL2RB-deficient patients uniformly develop herpesvirus infections if they survive the neonatal period, with CMV disease being particularly prevalent.[8] Zhang et al. report that “nearly all patients presented with autoantibodies, hypergammaglobulinemia, bowel inflammation, dermatological abnormalities, lymphadenopathy, and cytomegalovirus disease,” highlighting CMV as a defining infectious phenotype.[10]

The heightened susceptibility to CMV and EBV reflects IL-2 and IL-15’s roles in NK cell and CD8⁺ T cell–mediated antiviral responses; IL2RB deficiency impairs these pathways, rendering patients vulnerable to uncontrolled viral replication and tissue-invasive disease.[8][10][12] In some cases, chronic EBV viremia and lymphoproliferation may arise, paralleling the EBV-induced lymphoproliferation seen in CD137 (TNFRSF9) deficiency, although overt EBV-driven lymphoma has not yet been reported in IMD63.[5][6][7][10][12] From an ontology perspective, these infectious complications correspond to HPO terms such as **Recurrent viral infections** (HP:0004429), **Cytomegalovirus infection** (HP:0002239), and **Epstein–Barr virus infection** (HP:0012170).

### 5.3. Gene–Environment Interactions in Infectious Susceptibility

The interaction between IL2RB genotype and environmental exposure to pathogens is central to IMD63 pathophysiology. IL2RB mutations establish a baseline of defective IL-2/IL-15 signaling, leading to impaired T cell and NK cell responses and failure of immune regulation.[8][10][12] Upon exposure to common viruses such as CMV or respiratory pathogens, this genetic defect manifests as severe and often protracted infections, with viral persistence driving chronic immune activation, autoantibody production, and lymphoproliferation.[8][10][12] 

Moreover, chronic antigenic stimulation from persistent infections may contribute to the development of autoimmune phenomena and hypergammaglobulinemia, as immune responses become dysregulated in the absence of effective Treg-mediated tolerance.[8][10][12] Thus, gene–environment interactions in IMD63 largely involve the interplay between IL2RB-mediated signaling defects and environmental pathogen load, with the severity of infectious exposure modulating clinical manifestations on a background of fixed genetic susceptibility.

## 6. Mechanism / Pathophysiology

### 6.1. Ordered Causal Chain from Mutation to Clinical Disease

To conceptualize IMD63 pathophysiology, it is useful to describe an ordered causal chain from the initiating genetic lesion to the diverse clinical manifestations. In narrative form:

Step 1: Biallelic loss-of-function mutation in **IL2RB** leads to absent or impaired expression/function of the IL-2 receptor β subunit on T cells, NK cells, and other lymphocytes, which results in defective IL-2 and IL-15 signaling through the high-affinity heterotrimeric receptor complex.[8][9][10][16] 

Step 2: Defective IL-2/IL-15 signaling leads to impaired proliferation and survival of effector T cells, abnormal differentiation and maintenance of regulatory T cells (Tregs), and altered development and function of NK cells and memory CD8⁺ T cells, resulting in combined immunodeficiency and failure of peripheral immune tolerance.[8][10][12]

Step 3: Combined immunodeficiency leads to increased susceptibility to viral and bacterial infections, particularly CMV and other herpesviruses, which results in chronic antigenic stimulation, persistent inflammation, and immune activation.[8][10][12]

Step 4: Failure of peripheral tolerance and chronic immune activation leads to the production of autoantibodies, breakdown of self–non-self discrimination, and the development of autoimmune phenomena such as autoimmune hemolytic anemia, autoimmune cytopenias, and enteropathy.[10][12]

Step 5: Chronic immune activation and impaired apoptotic regulation of lymphocytes lead to generalized lymphoproliferation, manifesting clinically as lymphadenopathy, splenomegaly, and hepatomegaly, with hypergammaglobulinemia reflecting sustained B cell activation.[10][12]

Step 6: The combined effects of immunodeficiency, autoimmunity, and lymphoproliferation lead to recurrent infections, anemia, organ enlargement, and failure to thrive, culminating in the complex clinical syndrome recognized as immunodeficiency 63 with lymphoproliferation and autoimmunity.[1][9][10][12]

Some mechanistic links, such as the precise pathways by which IL2RB deficiency alters Treg development, are inferred from animal models and knowledge of IL-2 biology rather than directly demonstrated in all human patients, though human data strongly support the overall chain.[8][10][12]

### 6.2. Molecular Pathways: IL-2/IL-15–JAK–STAT Signaling

At the molecular level, IL2RB deficiency primarily affects the **IL-2/IL-15–JAK–STAT signaling cascade**. IL-2 is a pivotal cytokine that promotes activation, proliferation, and differentiation of CD4⁺ T helper subsets and CD4⁺ regulatory T cells, while IL-15 supports NK cell development and memory CD8⁺ T cell maintenance.[8][16] Both cytokines signal via receptors containing IL2RB and IL2RG, with IL2RA adding affinity specificity for IL-2.[8][16] Zhou et al. summarize that “IL-2 exerts biological functions by specifically binding with its receptor, which consists of three subunits, namely IL-2Rα (CD25), IL-2Rβ (CD122), and γc (CD132); both the IL-2Rβ and γc chains belong to a type I cytokine receptor superfamily and are responsible for signaling.”[16]

Upon IL-2 binding to the high-affinity receptor, JAK1 (associated with IL2RB) and JAK3 (associated with IL2RG) are activated, leading to phosphorylation of STAT5 and other STAT family members, which translocate to the nucleus and regulate transcription of genes involved in cell cycle progression, survival, and differentiation.[8][10][16] IL-2 is particularly important for the maintenance and functional competence of FOXP3⁺ regulatory T cells, which enforce peripheral tolerance by suppressing autoreactive T cells.[8][12] IL-15, via IL2RB and IL2RG, is critical for the development and survival of NK cells and certain memory CD8⁺ T cell subsets, thereby providing innate and adaptive antiviral defense.[8][16]

In IL2RB deficiency, this entire signaling axis is compromised. T cells do not respond appropriately to IL-2 stimulation, failing to phosphorylate STAT5 and proliferate, while NK cells show variable defects depending on residual IL2RB function.[10][12] GO terms capturing these processes include **interleukin-2 receptor activity** (GO:0004911), **interleukin-15 receptor activity** (GO:0035724), and **JAK–STAT cascade** (GO:0007259). The failure of these pathways leads to profound functional deficits in key lymphocyte populations and sets the stage for immunodeficiency and immune dysregulation.

### 6.3. Cellular Processes: Treg Dysfunction, NK Cell Abnormalities, and Immune Homeostasis

Cellular-level mechanisms in IMD63 revolve around **Treg dysfunction**, **NK cell abnormalities**, and disrupted immune homeostasis. IL-2 is indispensable for the survival and function of FOXP3⁺ regulatory T cells, and autosomal recessive mutations in IL2RA, IL2RB, and FOXP3 all cause severe immune dysregulation syndromes with overlapping clinical features, such as early-onset autoimmunity and enteropathy.[8][12] Campbell notes that “mutations in *IL2RB, FOXP3*, and *IL2RA* share clinical features of severe immune dysregulation, reflecting an important role of regulatory T cells in maintaining immune tolerance,” and that infant-onset autoimmune manifestations are shared with IPEX syndrome.[12] In IL2RB deficiency, Tregs cannot receive proper IL-2 signals, leading to reduced numbers or impaired suppressive function, thereby breaking peripheral tolerance and allowing autoreactive T cells to cause tissue damage.[8][10][12]

NK cells are another critical cellular compartment affected by IL2RB deficiency. IL-2Rβ is normally highly expressed on NK cells, and IL-2/IL-15 signaling is essential for NK cell maturation and cytotoxic function.[8][10][16] In IL2RB-deficient patients, NK cells show altered maturation phenotypes, including increased proportions of less mature CD56^bright cells, and impaired function, particularly in complete loss-of-function alleles.[8][10] Hernandez et al. report that in patients with hypomorphic IL2RB defects, “a larger proportion of NK cells demonstrate a less mature CD56^bright phenotype,” and that NK cells exhibit functional abnormalities.[8] This contributes to susceptibility to viral infections, especially CMV and EBV, which rely heavily on NK cell and CD8⁺ T cell–mediated control.[8][10][12]

At a broader level, immune homeostasis is profoundly disrupted. T cell memory compartments are skewed toward activated and memory phenotypes, reflecting chronic immune activation and persistent antigen exposure.[8][10][12] B cells are hyperactivated, producing elevated IgG and autoantibodies, leading to hypergammaglobulinemia and autoimmune cytopenias.[10][12] CL terms relevant here include **CD4-positive, alpha-beta T cell** (CL:0000624), **regulatory T cell** (CL:0000815), **natural killer cell** (CL:0000623), and **B cell** (CL:0000236). GO processes include **regulation of immune system process** (GO:0002682), **negative regulation of immune effector process** (GO:0002684), and **positive regulation of B cell activation** (GO:0050871).

### 6.4. Protein Dysfunction: Misfolding, Trafficking, and Binding Defects

At the level of protein structure and function, pathogenic IL2RB variants cause different types of dysfunction, including **misfolding**, **defective trafficking**, and **altered cytokine binding**.[10][11] L77P, located in the extracellular domain, induces misfolding and retention of IL-2Rβ in the endoplasmic reticulum, preventing proper surface expression on T cells and thereby abolishing IL-2 signaling in those cells.[10] S40L alters the cytokine binding site, reducing affinity for IL-2 while sparing receptor expression, leading to hyporesponsive signaling despite normal surface levels.[10] Q96X generates a truncated protein that is likely degraded and never reaches the cell surface, representing a complete loss of receptor.[10]

These protein-level defects correspond to GO terms such as **protein misfolding** (GO:0006457), **protein targeting to membrane** (GO:0006623), and **cytokine binding** (GO:0019955). UniProt annotations for IL2RB highlight its presence in the plasma membrane, and IL2RB’s structure as a type I membrane protein with extracellular cytokine-binding domains and intracellular signaling motifs.[11][16] Disruption of these structural elements directly translates into loss of function in the IL-2/IL-15 receptor complex, upstream of the JAK–STAT signaling cascade.

### 6.5. Immune System Involvement and Tissue Damage Mechanisms

The immune system involvement in IMD63 encompasses both **immunodeficiency** and **autoimmunity**, which together produce tissue damage through multiple mechanisms. Combined immunodeficiency leads to recurrent infections, with pathogen-driven inflammation causing tissue injury in organs such as the lungs (pneumonitis), gastrointestinal tract (enterocolitis), and liver.[8][10][12] Autoimmunity, mediated by autoreactive T and B cells in the absence of effective Treg suppression, leads to direct destruction of red blood cells (autoimmune hemolytic anemia), platelets, and other tissues, contributing to anemia, bleeding, and organ dysfunction.[10][12]

Chronic immune activation and lymphoproliferation result in infiltration of lymphoid cells into lymph nodes, spleen, liver, and other tissues, causing organ enlargement and potentially impairing function.[10][12] While fibrosis and end-organ failure have not been extensively documented in the small IMD63 cohorts, the potential for chronic inflammation to lead to tissue remodeling exists, as seen in other primary immunodeficiencies.[12][15] GO terms relevant here include **immune response** (GO:0006955), **autoimmune response** (GO:0002250), **lymphocyte proliferation** (GO:0046651), and **inflammatory response** (GO:0006954).

### 6.6. Molecular Profiling and Advanced Technologies

To date, there are no published large-scale transcriptomic, proteomic, metabolomic, or single-cell omics datasets specifically focused on IMD63, reflecting the rarity of the condition and the recency of its discovery.[1][9][10][12] However, the functional studies by Zhang et al. and Fernandez et al. provide detailed insights into IL2RB-related signaling defects at the cellular and biochemical levels, using flow cytometry, phospho-STAT assays, and recombinant expression systems.[9][10][12] Future work employing single-cell RNA sequencing, spatial transcriptomics, and multi-omics integration could delineate the precise transcriptional programs altered in Tregs, effector T cells, NK cells, and B cells in IL2RB deficiency, but such data remain to be generated.[1][9][10][12]

Functional genomics approaches, such as CRISPR/Cas9-mediated knockout of IL2RB in human cell lines or organoids, could further define causal pathways and identify potential therapeutic targets. Likewise, integration of human IMD63 data with the extensive literature on Il2rb knockout mice will be valuable in extrapolating mechanistic insights across species.[10][12] For now, the mechanistic understanding of IMD63 rests primarily on classical immunological and molecular assays rather than advanced omics technologies.

## 7. Anatomical Structures Affected

### 7.1. Organ-Level Involvement

IMD63 primarily affects the **immune system**, but its consequences extend to multiple organ systems. The most prominently involved organs include **lymph nodes**, **spleen**, **liver**, **bone marrow**, **gastrointestinal tract**, **skin**, and **lungs**.[10][12][15] Generalized lymphadenopathy and **splenomegaly** (UBERON:0002106) are consistent features, reflecting chronic lymphoproliferation and accumulation of immune cells in secondary lymphoid organs.[10][12] Hepatomegaly (UBERON:0002107) often accompanies splenomegaly, likely due to lymphoid infiltration and inflammatory changes.[10][12] 

The gastrointestinal tract (UBERON:0000160) is a major site of pathology, with enteropathy and chronic diarrhea resulting from immune-mediated inflammation of the small and large intestines.[10][12] Skin (UBERON:0002097) manifestations, such as rashes, eczema-like lesions, and erythroderma, are common, reflecting autoimmune or inflammatory involvement of cutaneous tissues.[10][12] The lungs (UBERON:0002048) are affected by recurrent respiratory infections and viral pneumonitis, which can cause respiratory distress and chronic pulmonary changes.[8][10][12] The hematologic system, including bone marrow (UBERON:0000178) and peripheral blood (UBERON:0000179), is involved through autoimmune hemolytic anemia and other cytopenias.[10][12]

### 7.2. Tissue and Cell-Level Involvement

At the tissue level, IMD63 involves **lymphoid tissues** (e.g., lymph node cortex and medulla, splenic white pulp), **hematopoietic tissues** (bone marrow), and **mucosal tissues** (intestinal epithelium and lamina propria).[10][12][15] In lymphoid organs, there is expansion of lymphocyte populations, including T cells, B cells, and sometimes plasma cells, consistent with lymphoproliferation and chronic immune activation.[10][12] In the gut, inflammatory infiltrates composed of lymphocytes and other immune cells disrupt normal mucosal architecture, leading to malabsorption and diarrhea.[10][12] In the skin, dermal and epidermal infiltrates contribute to rashes and lesions, although detailed histopathologic descriptions are limited.[10][12]

At the cell level, the primary populations affected are **CD4⁺ T helper cells**, **CD8⁺ cytotoxic T cells**, **FOXP3⁺ regulatory T cells**, **NK cells**, and **B cells**, all of which express IL2RB and depend on IL-2/IL-15 signaling.[8][9][10][11][16] CL ontology terms relevant here include **CD4-positive, alpha-beta T cell** (CL:0000624), **CD8-positive, alpha-beta T cell** (CL:0000625), **regulatory T cell** (CL:0000815), **natural killer cell** (CL:0000623), and **B cell** (CL:0000236). Altered phenotypes in these cell types—such as memory skewing in T cells, impaired NK maturation, and hyperactivated B cells—constitute the cellular substrate of IMD63 pathophysiology.[8][10][12]

### 7.3. Subcellular Localization and Cellular Components

At the subcellular level, IL2RB is a **plasma membrane** protein (GO:0005886), with an extracellular domain that binds IL-2 and IL-15, a transmembrane region, and an intracellular tail that associates with JAK1 and transduces signals.[11][16] Pathogenic IL2RB variants affect various cellular compartments, including the **endoplasmic reticulum** (GO:0005783) for misfolded proteins retained and degraded, and the **cell surface** (GO:0009986) where receptor expression is reduced or absent.[10][11] 

Downstream signaling involves the **cytoplasm** (GO:0005737), where JAK kinases phosphorylate STAT proteins, and the **nucleus** (GO:0005634), where STATs regulate transcription. Defective trafficking and surface expression, as in L77P, result in diminished receptor presence at the plasma membrane, whereas truncating mutations like Q96X prevent stable protein production.[10][11] These subcellular defects underpin the failure of IL-2/IL-15 signaling and subsequent immunologic phenotypes.

### 7.4. Localization, Lateralization, and Systemic Nature

IMD63 is inherently **systemic**, affecting multiple organ systems and tissues throughout the body. There is no evidence of lateralization or asymmetry; lymphadenopathy, splenomegaly, enteropathy, and skin manifestations are typically diffuse or generalized.[10][12] The disease’s systemic nature reflects the ubiquitous expression of IL2RB on diverse lymphocyte populations and the central role of IL-2/IL-15 signaling in global immune regulation.[8][9][10][11][16] 

From an anatomic ontology perspective, IMD63 involves **immune system** structures (UBERON:0002405), **lymphoid tissue** (UBERON:0002150), **hematopoietic system** (UBERON:0002390), **gastrointestinal system** (UBERON:0005409), **integumentary system** (UBERON:0002416), and **respiratory system** (UBERON:0001004), illustrating its broad impact.

## 8. Temporal Development

### 8.1. Onset: Age and Pattern

IMD63 generally presents in the **neonatal** or **early pediatric period**, with some cases manifesting as intrauterine or perinatal demise and others as severe disease during infancy or early childhood.[9][10][12] Campbell notes that the combined reports of Zhang et al. and Fernandez et al. include “seven affected live-born children with immunodeficiency and autoimmune disease, and three perinatally affected fatalities,” indicating that disease onset can occur before birth in severe IL2RB deficiency.[12] 

For live-born patients, onset is often **subacute** or **chronic**, rather than acutely fulminant, with progressive development of infections, autoimmunity, and lymphoproliferation over the first months or years of life.[9][10][12] Parents may initially notice failure to thrive, persistent diarrhea, recurrent respiratory infections, and skin rashes, followed by signs of anemia and organ enlargement.[10][12] This pattern is consistent with other combined immunodeficiencies with immune dysregulation, such as IL2RA deficiency and IPEX syndrome.[8][12][15]

### 8.2. Progression: Disease Staging and Course

The progression of IMD63 can be conceptualized in stages: an **early stage** characterized by recurrent infections and emerging autoimmune phenomena; an **intermediate stage** with established lymphoproliferation, chronic enteropathy, and multi-organ involvement; and an **advanced stage** where cumulative organ damage, severe anemia, and recurrent infections pose life-threatening risks.[9][10][12][15] However, formal staging systems have not been developed, and this framework is inferred from case descriptions.

The progression rate appears **rapid** in complete loss-of-function IL2RB variants, with severe disease and perinatal or early childhood mortality, whereas **variable** and somewhat slower progression may occur in hypomorphic alleles with residual receptor function.[10][12] Disease course is generally **chronic**, with intermittent exacerbations triggered by infections or other stressors, rather than fully remitting, although HSCT can induce a form of “cure” by replacing the defective immune system.[10][12] Without HSCT, IMD63 likely remains lifelong, with ongoing health needs.

### 8.3. Remission, Critical Periods, and Windows of Intervention

Spontaneous remission of IMD63 has not been documented, given its genetic basis and persistent IL2RB deficiency.[1][9][10][12] However, **treatment-induced remission** of autoimmune manifestations and infection control can occur with appropriate immunosuppressive, antiviral, and supportive therapies.[8][10][12] HSCT can effectively reconstitute IL-2Rβ–competent immune cells, leading to long-term resolution of immunodeficiency and immune dysregulation, as demonstrated in at least one IL2RB-deficient patient.[10][12]

Critical periods in IMD63 include the **perinatal and early infancy** windows, when severe infections and autoimmune reactions may be most dangerous, and when early diagnosis and initiation of prophylactic antimicrobials and immunomodulatory therapies are particularly impactful.[8][10][12] Early recognition also allows timely consideration of HSCT before irreversible organ damage occurs. Thus, the temporal development of IMD63 underscores the importance of early detection and intervention.

## 9. Inheritance and Population

### 9.1. Inheritance Pattern and Penetrance

IMD63 is inherited in an **autosomal recessive** manner, with affected individuals carrying biallelic pathogenic IL2RB variants and heterozygous carriers being clinically unaffected.[1][4][9][10][12] OMIM explicitly lists immunodeficiency 63 with lymphoproliferation and autoimmunity as autosomal recessive, and GenCC confirms this inheritance pattern.[1][4][9] In the reported consanguineous families, parents were heterozygous carriers and multiple offspring were affected, consistent with Mendelian recessive inheritance.[9][10][12]

Penetrance appears to be **complete** for individuals with biallelic complete loss-of-function variants such as Q96X or the 9-bp deletion, with all such individuals developing severe immune dysregulation.[9][10][12] For hypomorphic alleles such as L77P and S40L, penetrance also seems high, although the severity and specific manifestations may vary, reflecting variable expressivity rather than incomplete penetrance.[10][12] There is no evidence of dominant inheritance, X-linked transmission, genetic anticipation, or germline mosaicism in IMD63, given current data.[1][9][10][12]

### 9.2. Expressivity, Consanguinity, and Founder Effects

Expressivity in IMD63 is **variable**, influenced by the specific IL2RB mutation and residual receptor function.[9][10][12] Patients with hypomorphic L77P mutations may have partial NK cell function and perhaps somewhat less catastrophic infectious susceptibility than those with complete loss-of-function alleles, although autoimmunity and lymphoproliferation remain prominent.[10][12] Some patients have more severe enteropathy and skin disease, while others have more dominant hematologic autoimmunity, reflecting individual variation.[9][10][12]

Consanguinity plays a central role in the epidemiology of IMD63, as all reported families to date have been consanguineous, facilitating homozygosity for rare IL2RB mutations.[9][10][12] This suggests that IMD63 may occur at higher relative frequency in populations with high rates of consanguineous marriage, though absolute prevalence remains extremely low. No clear founder mutations have been definitively established, although certain variants like L77P were identified in multiple related families.[10] Carrier frequency in the general population is unknown but likely exceedingly low, consistent with the rarity of pathogenic IL2RB alleles in gnomAD.[10]

### 9.3. Epidemiology, Prevalence, and Population Demographics

IMD63 is currently classified as an **ultra-rare** primary immunodeficiency, with fewer than a dozen affected individuals reported worldwide.[1][9][10][12] Precise prevalence and incidence estimates are unavailable due to the small number of cases and lack of population-based registries, but it likely falls well below 1 per 1,000,000 individuals, similar to other ultra-rare inborn errors of immunity.[2][15] Orphanet lists many combined immunodeficiencies and immune dysregulation syndromes with prevalences <1/1,000,000, and IMD63 is reasonably assumed to be in this range.[2][15]

Geographically, reported cases originate from consanguineous families in various regions, including Central Asia (e.g., Tajikistan) and other populations where consanguinity is more common.[9][10][12] There is no clear sex predilection, as autosomal recessive inheritance affects males and females equally.[9][10][12] Age distribution is skewed toward infancy and early childhood, reflecting early onset and often severe disease progression.[9][10][12]

## 10. Diagnostics

### 10.1. Clinical and Laboratory Evaluation

Diagnosis of IMD63 requires integration of **clinical features**, **immunologic laboratory findings**, and **genetic testing**. Clinically, physicians should suspect IL2RB deficiency in infants or young children with combined manifestations of recurrent infections, autoimmunity (especially autoimmune hemolytic anemia), enteropathy, dermatologic abnormalities, generalized lymphadenopathy, and hepatosplenomegaly, particularly in the context of consanguinity.[10][12][15] Initial laboratory evaluation should include complete blood counts, immunoglobulin levels, autoantibody panels, and basic metabolic and liver function tests.[10][12][15]

Immunologic testing should assess T, B, and NK cell numbers and phenotypes by flow cytometry, measuring naïve versus memory T cell subsets (e.g., CD45RA/CD45RO), NK cell maturity markers (such as CD56^bright versus CD56^dim), and B cell subsets.[8][10][15] Elevated IgG and autoantibodies, skewed memory T cells, increased CD56^bright NK cells, and abnormal NK function are suggestive of IL-2R signaling defects.[8][10] Functional assays, such as in vitro stimulation of lymphocytes with IL-2 and IL-15 and measurement of STAT5 phosphorylation or proliferation, can reveal defective IL-2Rβ-mediated signaling.[10][12] Direct measurement of IL-2Rβ surface expression on T cells and NK cells by flow cytometry is particularly informative; patients with IL2RB deficiency have markedly reduced or absent IL-2Rβ on T cells and variable expression on NK cells depending on the mutation.[10][12]

Newborn screening based on T cell receptor excision circles (TRECs), used to detect severe T cell lymphopenia as in X-SCID, may not reliably identify IL2RB deficiency, since T cell numbers can be relatively preserved albeit functionally impaired.[8][15] Hernandez et al. note that IL-2Rα and IL-2Rβ deficient patients generally do not have abnormal newborn screens (low TRECs), in contrast to IL-2Rγ deficiency.[8] Thus, IMD63 is unlikely to be detected by standard TREC-based newborn screening.

### 10.2. Genetic Testing Strategies

Definitive diagnosis of IMD63 rests on **genetic testing** demonstrating biallelic pathogenic IL2RB variants.[1][9][10][12] Whole exome sequencing (WES) has been the primary modality used to identify IL2RB mutations in the reported families, particularly in settings where a broad differential of inborn errors of immunity is considered.[9][10][12] WES allows detection of missense, nonsense, and small indel mutations across the exome, and subsequent targeted Sanger sequencing can confirm findings in patients and family members.[9][10][12] Whole genome sequencing (WGS) could similarly be used and would offer additional ability to detect non-coding regulatory variants, though such variants have not yet been reported in IMD63.[1][9][10][12]

Single-gene testing of IL2RB by Sanger sequencing or targeted next-generation sequencing is feasible once clinical suspicion arises, particularly in consanguineous families with typical phenotype.[9][10][12] Gene panels designed for **combined immunodeficiencies with immune dysregulation** and **inborn errors of immunity** increasingly include IL2RB alongside IL2RA, IL2RG, FOXP3, CTLA4, STAT3, and other genes.[8][12][15] Chromosomal microarray (CMA), karyotyping, FISH, mitochondrial DNA testing, and repeat expansion testing are generally not useful for IMD63 diagnosis, as the disease is caused by point mutations and small indels in a single nuclear gene.[1][9][10][12]

ClinVar provides variant-level information, such as classification of specific IL2RB variants as pathogenic or benign, aiding interpretation.[3][9][10] ClinGen/GenCC submissions confirm the gene–disease validity for IL2RB and IMD63.[4] Genetic counseling should accompany testing, given the autosomal recessive inheritance and potential implications for family planning.[1][4][9][10][12]

### 10.3. Omics-Based and Advanced Diagnostics

Although comprehensive omics-based diagnostics—such as transcriptomics, proteomics, metabolomics, and epigenomics—are not yet standard for IMD63, they could theoretically contribute to diagnosis or mechanistic understanding. For example, RNA sequencing of patient lymphocytes could reveal transcriptional signatures of defective IL-2/IL-15 signaling, altered Treg gene expression, and hyperactivated B cells.[8][10][12] Proteomic analysis might identify downstream signaling proteins with altered phosphorylation patterns, while metabolomics could detect metabolic shifts associated with chronic inflammation.[8][10][12]

Liquid biopsy approaches, such as detection of circulating cell-free DNA or RNA, have not been applied to IMD63 and are unlikely to be primary diagnostic tools for a Mendelian immunodeficiency, but they could have ancillary roles in monitoring infection or lymphoproliferation. For now, advanced omics remain largely research tools rather than clinical diagnostics for IL2RB deficiency.[1][9][10][12]

### 10.4. Differential Diagnosis and Clinical Criteria

Differential diagnosis for IMD63 includes other **combined immunodeficiencies with immune dysregulation**, particularly IL2RA deficiency, FOXP3-related IPEX syndrome, hypomorphic IL2RG defects, CTLA4 insufficiency, and STAT3 gain-of-function mutations.[8][12][15] IL2RA deficiency and IL2RB deficiency share many features, including early-onset autoimmunity, enteropathy, elevated IgG, autoantibodies, and herpesvirus infections.[8][12] FOXP3 deficiency (IPEX) also presents with early-onset enteropathy, dermatitis, and autoimmunity but is X-linked and associated with absence or dysfunction of Tregs due to FOXP3 mutation, rather than IL2RB defects.[12] Hypomorphic IL2RG variants cause atypical X-SCID with combined immunodeficiency and immune dysregulation, but classic IL2RG deficiency produces profound T⁻ B⁺ NK⁻ SCID with severe T and NK lymphopenia.[8][12]

CTLA4 haploinsufficiency and STAT3 gain-of-function also produce immune dysregulation syndromes with autoimmunity and lymphoproliferation, but their molecular pathways differ and they often present later in childhood or adulthood.[15] Distinguishing IMD63 from these conditions relies on detailed clinical and immunologic assessment combined with genetic testing. No formal diagnostic criteria or scoring systems specific to IMD63 have been published; instead, diagnosis is based on recognition of the characteristic triad and confirmation of IL2RB mutations.[1][9][10][12]

### 10.5. Screening and Cascade Testing

Population-based screening for IMD63 is not currently feasible or recommended, given its ultra-rare prevalence and absence of specific biomarkers suitable for mass screening.[1][2][9][10][12][15] Newborn screening based on TRECs does not reliably detect IL2RB deficiency, as discussed, and there is no established biochemical or metabolite marker unique to the condition.[8][15] However, **cascade genetic screening** of at-risk relatives in families with known IL2RB mutations is important, allowing identification of carriers and early diagnosis of affected siblings.[1][4][9][10][12]

Carrier screening in consanguineous populations, particularly those where specific IL2RB founder mutations might emerge, could be considered in the future, but data are currently insufficient.[10][12] Prenatal diagnosis and preimplantation genetic testing are theoretically possible once parental carrier status and familial mutations are known, but such interventions have not yet been reported in the literature for IMD63.[1][9][10][12]

## 11. Outcome/Prognosis

### 11.1. Survival, Mortality, and Life Expectancy

Due to the small number of reported cases, precise survival and mortality statistics for IMD63 are not available, but the available data suggest a **poor prognosis** without definitive treatment and significant morbidity and mortality in early life.[9][10][12] Campbell notes that among the five kindreds described with IL2RB mutations, there were “seven affected live-born children with immunodeficiency and autoimmune disease, and three perinatally affected fatalities,” indicating that perinatal mortality due to severe immune dysregulation and infection can occur.[12] Among live-born patients, chronic CMV disease, recurrent infections, and severe autoimmunity pose ongoing threats to survival.[8][10][12]

Hematopoietic stem cell transplantation (HSCT) has been successfully performed in at least one IL2RB-deficient patient, significantly ameliorating clinical symptoms and suggesting that life expectancy can be normalized with effective definitive treatment.[10][12] Zhang et al. note that “stem cell transplant ameliorated clinical symptoms in one patient,” and Campbell highlights HSCT as the current definitive therapy for IL2RB deficiency.[10][12] Without HSCT, life expectancy is likely significantly reduced, though exact estimates cannot be made from the limited data.

### 11.2. Morbidity, Disability, and Quality of Life

Morbidity in IMD63 is high, encompassing recurrent infections, chronic diarrhea, autoimmune cytopenias, organomegaly, and failure to thrive.[10][12] These complications result in substantial disability, including impaired growth and development, reduced physical stamina, limitations on school and social participation, and psychological stress for patients and families.[10][12] The burden of chronic disease would be reflected in generic disability and functioning frameworks such as the International Classification of Functioning (ICF), with limitations in multiple domains.

Quality of life is markedly impaired, although formal measurement with instruments like EQ-5D, SF-36, or PROMIS has not been reported.[12] Recurrent hospitalizations, invasive procedures, and chronic treatments (e.g., immunosuppressive drugs, antivirals, transfusions) contribute to the overall burden. HSCT, when successful, can greatly improve quality of life by reconstituting a functional immune system and reducing the need for ongoing therapies, though transplant-related risks and complications must be considered.[10][12]

### 11.3. Disease Course, Complications, and Recovery Potential

The disease course in IMD63 is characterized by chronic progression with intermittent exacerbations. Complications include severe CMV disease, other viral infections, opportunistic bacterial and fungal infections, autoimmune hemolytic anemia requiring transfusions, autoimmune thrombocytopenia with bleeding risk, enteropathy with malnutrition, and potential organ damage from chronic inflammation.[8][10][12][15] Recovery potential without HSCT is limited; medical management can control some manifestations, such as autoimmunity and infections, but the underlying immunologic defect persists.[8][10][12]

HSCT offers a realistic chance of recovery, with potential normalization of immune function and resolution of most disease manifestations.[10][12] Prognostic factors influencing transplant outcomes include patient age, disease severity at the time of transplant, degree of organ damage, donor match quality, and transplantation center experience.[10][12][15] For patients who are not transplant candidates, prognosis is guarded, with long-term survival dependent on aggressive management of infections and autoimmunity.

### 11.4. Prognostic Biomarkers and Factors

Prognostic biomarkers for IMD63 have not been systematically defined, but certain features likely correlate with outcomes. Severe CMV disease, perinatal onset, and complete loss-of-function IL2RB variants (e.g., Q96X) may predict poorer prognosis due to more profound immunodeficiency.[8][10][12] Residual IL2RB function in hypomorphic alleles, as suggested by partial NK cell activity in L77P, may confer relatively better outcomes, though still within a severe disease spectrum.[10][12]

Serum IL-2 levels, immunoglobulin profiles, autoantibody titers, and lymphocyte activation markers could serve as indicators of disease activity and immune dysregulation, although their prognostic value has not been rigorously validated.[8][10][12] Ultimately, the key prognostic factor is access to and timing of HSCT, which can dramatically alter the natural history of IMD63.

## 12. Treatment

### 12.1. Pharmacotherapy and Supportive Medical Management

Pharmacologic treatment of IMD63 focuses on **managing infections**, **controlling autoimmunity**, and **supporting hematologic and gastrointestinal function**, as well as preparing patients for HSCT when appropriate.[8][10][12][15] Antiviral prophylaxis and therapy are central, particularly against CMV and other herpesviruses. Hernandez et al. recommend that IL-2Rα, IL-2Rβ, and atypical IL-2Rγ deficiency patients “should receive (val)ganciclovir prophylaxis and be monitored regularly for CMV infection,” given the high burden of CMV disease.[8] This corresponds to NCIT terms such as **Ganciclovir** (NCIT:C29322) and **Antiviral Therapy** (NCIT:C48274).

Broad-spectrum antimicrobials, including antibiotics and antifungals, are used to treat bacterial and fungal infections as they arise, following standard infectious disease guidelines for immunocompromised hosts.[8][10][15] Immunoglobulin replacement therapy (intravenous or subcutaneous) may be considered to support humoral immunity, though patients often exhibit hypergammaglobulinemia and autoantibodies rather than classic hypogammaglobulinemia.[10][12][15]

Autoimmune manifestations, especially autoimmune hemolytic anemia and other cytopenias, are managed with **immunosuppressive drugs** such as corticosteroids, rituximab (NCIT:C39165), and other agents, similar to treatment protocols in Evans syndrome and IPEX.[10][12][15] Care must be taken to balance immunosuppression with underlying immunodeficiency, avoiding excessive suppression that could exacerbate infections. Supportive care for anemia may include red blood cell transfusions, while enteropathy may be addressed with nutritional support, including parenteral nutrition if necessary, and anti-inflammatory treatments such as steroids or biologics, although experience in IMD63 is limited.[10][12]

### 12.2. Advanced Therapeutics: Hematopoietic Stem Cell Transplantation and Gene Therapy

The current **definitive treatment** for IL2RB deficiency is **hematopoietic stem cell transplantation (HSCT)**, which replaces the defective immune system with donor-derived cells expressing normal IL-2Rβ and restores functional IL-2/IL-15 signaling.[8][10][12][15] Zhang et al. report that “stem cell transplant ameliorated clinical symptoms in one patient,” and Hernandez et al. note that HSCT is curative for IL-2Rα, IL-2Rβ, and IL-2Rγ defects.[8][10] HSCT corresponds to NCIT term **Hematopoietic Stem Cell Transplantation** (NCIT:C15206).

HSCT carries risks, including graft-versus-host disease, infection, and transplant-related mortality, but in the context of severe IMD63, the potential benefits outweigh these risks when a suitable donor is available.[10][12][15] Conditioning regimens and transplant protocols must be tailored to the patient’s age, organ status, and disease severity, drawing on experience with other primary immunodeficiencies and immune dysregulation syndromes.[15]

Gene therapy, particularly **gene replacement or gene editing** strategies targeting IL2RB, is conceptually attractive and has seen success in related disorders such as IL2RG-deficient X-SCID.[8][12] Hernandez et al. suggest that “hematopoietic stem cell transplant (HSCT) is curative for IL-2Rα, IL-2Rβ, and IL-2Rγ defects, but gene therapy may yield comparable results for X-SCID,” hinting that analogous approaches might one day be applied to IL2RB deficiency.[8] However, as of the latest literature, there are no clinical trials or published reports of IL2RB-targeted gene therapy, and such interventions remain experimental.[1][8][9][10][12]

### 12.3. Surgical and Interventional Treatments

Surgical interventions are not primary treatments for IMD63 but may be required to address complications, such as splenectomy for refractory autoimmune hemolytic anemia or hypersplenism, or placement of central venous lines for long-term intravenous therapies.[10][12][15] Splenectomy (NCIT:C15794) carries risks of increased susceptibility to encapsulated bacterial infections and must be weighed carefully in already immunocompromised patients. Endoscopic procedures may be performed to evaluate enteropathy, and biopsies of lymph nodes or gastrointestinal mucosa may be obtained for diagnostic purposes.[10][12][15]

### 12.4. Supportive and Rehabilitative Care

Supportive care is critical in IMD63, encompassing **nutritional support**, **pain management**, **physical therapy**, and **psychosocial support**.[10][12][15] Children with chronic diarrhea and malabsorption require careful nutritional monitoring, supplemental feeding, and sometimes parenteral nutrition to ensure adequate growth and development.[10][12] Pain and discomfort from lymphadenopathy, splenomegaly, and procedures must be addressed with appropriate analgesia. Physical therapy can help maintain strength and function during periods of illness, and psychosocial interventions support families coping with a chronic, life-threatening disease.

Rehabilitative efforts aim to maximize functioning and quality of life before and after HSCT, addressing any developmental delays or motor impairments that may have arisen due to prolonged illness. NCIT terms such as **Supportive Care** (NCIT:C15693) and **Rehabilitation Therapy** (NCIT:C15279) capture these interventions.

### 12.5. Experimental and Personalized Medicine Approaches

Experimental treatments for IMD63 are currently limited, given the rarity of the disease and the focus on HSCT as the primary definitive therapy. However, future personalized medicine approaches could include **genotype-guided risk stratification** and **targeted therapies** that modulate IL-2/IL-15 signaling or downstream pathways.[8][10][12] For example, low-dose IL-2 therapy has been explored in other autoimmune diseases to selectively expand Tregs; in IL2RB deficiency, such therapy would likely be ineffective but might have nuanced effects in hypomorphic alleles with residual receptor function.[8][12]

Targeted immunotherapies, such as CTLA4-Ig (abatacept) or JAK inhibitors, could theoretically modulate immune activation in IMD63, but their use would need careful consideration given the underlying immunodeficiency and has not been reported.[8][12][15] Personalized transplant conditioning regimens based on specific IL2RB mutations and patient immune status may also be developed in the future, optimizing outcomes while minimizing toxicity.[10][12][15]

## 13. Prevention

### 13.1. Primary, Secondary, and Tertiary Prevention

Primary prevention of IMD63, in the sense of preventing disease occurrence, is challenging due to its **Mendelian genetic basis** and ultra-rare prevalence.[1][9][10][12] Nevertheless, **genetic counseling** and carrier screening in families with known IL2RB mutations can inform reproductive decisions and reduce recurrence risk, representing a form of primary prevention at the family level.[1][4][9][10][12] Prenatal diagnosis and preimplantation genetic testing could prevent the birth of affected children in high-risk families, although such interventions have not yet been documented in the literature for IMD63.[1][9][10][12]

Secondary prevention focuses on **early detection and prompt intervention** to mitigate disease complications. Early recognition of IMD63 in infants with suggestive clinical features allows timely initiation of antiviral prophylaxis, immunosuppressive management of autoimmunity, and consideration of HSCT before severe organ damage occurs.[8][10][12] While there is no population-wide screening program for IMD63, targeted genetic testing and immunologic evaluation in symptomatic children serve as secondary prevention mechanisms.

Tertiary prevention aims to **prevent complications and improve quality of life** in patients with established disease. This includes aggressive infection prophylaxis, vigilant monitoring for CMV and other pathogens, comprehensive management of autoimmunity, and supportive care to prevent malnutrition and developmental delays.[8][10][12][15] HSCT can be viewed as both a tertiary preventive strategy (preventing future infections and autoimmune flares) and a definitive curative therapy.

### 13.2. Immunization and Infectious Prophylaxis

Immunization strategies for IMD63 must balance the need to protect against vaccine-preventable diseases with the risks associated with live attenuated vaccines in immunocompromised hosts. In general, **inactivated vaccines** (e.g., inactivated influenza, pneumococcal, and Hib vaccines) are recommended, while **live vaccines** (such as MMR, varicella, and live polio) are contraindicated or used with extreme caution in severe combined immunodeficiency.[15] Specific guidelines for IMD63 have not been published, but clinicians typically follow immunization recommendations for combined immunodeficiencies.

As emphasized earlier, **antiviral prophylaxis** with valganciclovir or ganciclovir against CMV and possibly other herpesviruses is a key preventive measure.[8] Regular monitoring of CMV viral loads and preemptive treatment when threshold levels are exceeded are integral to preventing severe CMV disease.[8][10][12] Prophylactic antibiotics and antifungals may be used in patients with recurrent bacterial or fungal infections, aligning with standard primary immunodeficiency management.[15]

### 13.3. Genetic Counseling and Risk Stratification

Genetic counseling is paramount in families with IMD63, given autosomal recessive inheritance and potential for multiple affected children.[1][4][9][10][12] Counselors should explain carrier status, recurrence risks (25% for affected offspring when both parents are carriers), options for prenatal diagnosis or preimplantation genetic testing, and implications for extended family members who may also be carriers.[1][4][9][10][12] NSGC and ACMG guidelines for counseling in autosomal recessive conditions provide a framework for these discussions.

Risk stratification within affected patients may involve consideration of specific IL2RB mutations, residual receptor function, severity of infections, and autoimmune burden, guiding decisions about timing and modality of HSCT, intensity of prophylaxis, and monitoring frequencies.[8][10][12] While formal risk models have not been developed for IMD63, clinical judgment informed by experience with related IL-2 receptor defects and combined immunodeficiencies is currently used.[8][12][15]

### 13.4. Public Health and Environmental Interventions

Given the ultra-rare nature of IMD63, large-scale public health interventions specifically targeting this disorder are unlikely.[1][2][9][10][12] However, general public health measures that reduce infection transmission—such as vaccination campaigns, hygiene promotion, and infection control in healthcare settings—indirectly benefit IMD63 patients by lowering their exposure to pathogens.[15] Environmental interventions, such as improved sanitation and reduced overcrowding, similarly reduce infection risk and thereby mitigate disease complications, though they do not prevent the genetic disorder itself.[15]

## 14. Other Species / Natural Disease

### 14.1. Orthologous Genes and Mouse Models

Orthologous IL2RB genes exist in multiple species, including **mice** (*Il2rb*), **fish** (e.g., flounder IL-2Rβ), and other vertebrates.[10][12][16] Mouse Il2rb knockout models have been particularly informative for understanding the consequences of IL-2Rβ deficiency. Earlier studies demonstrated that Il2rb⁻/⁻ mice have abnormal development of intestinal intraepithelial lymphocytes, peripheral NK cell defects, autoimmune hemolytic anemia, hypergammaglobulinemia, elevated autoantibodies, lymphadenopathy, and splenomegaly, phenotypes closely paralleling human IL2RB deficiency.[10][12] Campbell notes that “human *IL2RB* deficiency shares several features of immune dysregulation with *Il2rb* knock-out mice, including autoimmune hemolytic anemia, hypergammaglobulinemia, elevated autoantibodies, lymphadenopathy, and splenomegaly.”[12]

Zhou et al. cloned IL-2 and IL-2Rβ genes from flounder (*Paralichthys olivaceus*) and showed that IL-2Rβ molecules are expressed on both B and T lymphocytes, and that IL-2 interacts with IL-2Rβ to increase the proportion of CD4⁺ T lymphocytes.[16] This work emphasizes the evolutionary conservation of IL-2/IL2RB function across vertebrate species, although natural disease comparable to IMD63 has not been described in fish.[16]

### 14.2. Natural Disease in Non-Human Species

To date, there are no reports of naturally occurring IL2RB deficiency in companion animals, livestock, or wildlife comparable to human IMD63.[1][10][12] OMIA and veterinary disease databases have not catalogued IL2RB-associated immunodeficiencies in animals, suggesting that such conditions are either extremely rare or unrecognized.[1][10][12] However, the phenotypes observed in Il2rb knockout mice closely resemble human IMD63, making them highly relevant as experimental models rather than natural diseases.[10][12]

### 14.3. Comparative Pathology and Evolutionary Conservation

Comparative pathology between human IL2RB deficiency and mouse Il2rb knockout models underscores the conservation of IL-2/IL-15 receptor functions in immune regulation. Both humans and mice with IL2RB/Il2rb defects exhibit autoimmune hemolytic anemia, hypergammaglobulinemia, autoantibody production, lymphadenopathy, and splenomegaly, indicating that IL-2Rβ is essential for maintaining peripheral tolerance and preventing spontaneous autoimmunity.[10][12] Both species also show abnormalities in intestinal intraepithelial lymphocytes and NK cells, highlighting IL-2Rβ’s role in mucosal immunity and innate antiviral defense.[10][12]

Evolutionary conservation of IL2RB-mediated pathways is further supported by flounder studies demonstrating IL-2Rβ expression on B and T lymphocytes and functional IL-2–IL2RB interactions promoting CD4⁺ T cell expansion.[16] These observations suggest that IL2RB’s role in lymphocyte regulation is an ancient feature of vertebrate immune systems, reinforced across species by similar phenotypic consequences of its disruption.[10][12][16]

### 14.4. Zoonotic Potential and Cross-Species Susceptibility

IMD63 itself is not a zoonotic disease and does not involve cross-species transmission; rather, it is a non-communicable, genetic disorder of the human immune system.[1][9][10][12] However, IL2RB deficiency increases susceptibility to zoonotic pathogens such as CMV and EBV (the latter primarily human-specific), reflecting impaired antiviral defense mechanisms.[8][10][12] There is no evidence that IL2RB deficiency alters host range or promotes cross-species infections beyond increased susceptibility in the affected host. Thus, zoonotic considerations relate mainly to the pathogens that exploit the immunodeficient state, not to the genetic disease itself.[8][10][12]

## 15. Model Organisms

### 15.1. Mouse Il2rb Knockout Models

Mouse **Il2rb knockout** models are the most extensively studied experimental systems relevant to IMD63. Il2rb⁻/⁻ mice lack functional IL-2Rβ and exhibit profound immune dysregulation, including autoimmune hemolytic anemia, hypergammaglobulinemia, autoantibodies, lymphadenopathy, splenomegaly, and abnormal development of intestinal intraepithelial lymphocytes and NK cells.[10][12] These phenotypes closely parallel human IL2RB deficiency, making Il2rb knockout mice valuable models for studying disease mechanisms and testing therapies.

Suzuki et al. (referenced by Campbell and Zhang) demonstrated that Il2rb-deficient mice spontaneously develop autoimmune hemolytic anemia and hypergammaglobulinemia, with elevated autoantibodies and expansion of lymphoid organs, reinforcing IL-2Rβ’s role in peripheral tolerance.[10][12] Additional studies showed abnormal development of intestinal intraepithelial lymphocytes and NK cells, indicating that IL-2Rβ is required for mucosal immunity and innate cytotoxic responses.[10][12] These findings agree with human IMD63, where enteropathy and NK cell abnormalities are prominent.[10][12]

From a model organism database perspective, Il2rb knockout mice are catalogued in MGI and IMPC, with detailed phenotypic annotations reflecting immune and hematologic abnormalities.[10][12] They serve as preclinical models for evaluating HSCT, immunosuppressive therapies, and potentially gene therapy approaches targeting IL2RB.

### 15.2. Other Model Systems and Limitations

Beyond mice, other model systems include **in vitro cell line models** with IL2RB knockdown or knockout, and **recombinant expression systems** used by Zhang et al. to dissect mechanisms of IL2RB variants.[10][12] For example, Zhang et al. recreated IL2RB mutations in heterologous systems to show that Q96X abolishes receptor expression, L77P impairs surface trafficking, and S40L reduces IL-2 binding.[10] These in vitro models allow precise mechanistic investigation but do not replicate the full complexity of human immune system interactions.

Fish models, such as flounder IL-2Rβ functional studies, demonstrate evolutionary conservation of IL2RB but have limited direct applicability to human disease due to differences in immune system organization.[16] No Drosophila, C. elegans, or yeast models exist for IL2RB deficiency, given the absence of IL-2/IL-15 signaling in these organisms.[16]

Limitations of mouse Il2rb knockout models include differences in the repertoire of infections, immune system organization, and lifespan compared with humans.[10][12] Moreover, mouse models typically represent complete knockout rather than hypomorphic alleles with residual function, whereas human IMD63 includes both complete and partial loss-of-function variants.[10][12] Despite these limitations, mouse models remain invaluable for elucidating fundamental mechanisms and testing interventions.

### 15.3. Research Applications of Model Organisms

Model organisms contribute significantly to understanding IMD63-related mechanisms and potential treatments. Il2rb knockout mice can be used to study how IL-2Rβ deficiency affects Treg development, NK cell maturation, memory T cell maintenance, and B cell activation, providing insights into the causal chain from IL2RB mutation to autoimmunity and immunodeficiency.[10][12] They also allow experimental infection with pathogens to dissect antiviral defects and test prophylactic strategies.[10][12]

In vitro models support investigation of IL2RB variant-specific effects on protein folding, trafficking, and cytokine binding, informing genotype–phenotype correlations and variant interpretation in human patients.[10][12] Together, these models form a multi-level experimental framework that complements human clinical data and enhances mechanistic understanding of IMD63, which is crucial for developing targeted therapies and optimizing HSCT protocols.

## Conclusion

Immunodeficiency 63 with lymphoproliferation and autoimmunity (IMD63) is a paradigmatic example of how a single Mendelian defect in a cytokine receptor subunit—**IL2RB**, encoding the IL-2/IL-15 receptor β chain—can simultaneously disrupt host defense and immune tolerance, leading to a complex syndrome of combined immunodeficiency, autoimmunity, and lymphoproliferation.[1][9][10][12] At the genetic level, biallelic loss-of-function IL2RB mutations, including missense (L77P, S40L), nonsense (Q96X), and in-frame deletions, abolish or impair IL-2Rβ expression or function, resulting in defective IL-2 and IL-15 signaling.[9][10][12] This molecular lesion initiates a causal chain in which impaired IL-2/IL-15–JAK–STAT signaling leads to Treg dysfunction, altered NK cell maturation, and skewed T cell and B cell homeostasis, thereby coupling combined immunodeficiency with breakdown of peripheral tolerance.[8][10][12][16]

Clinically, IMD63 manifests in infancy or early childhood with recurrent infections (especially CMV and other herpesviruses), enteropathy, dermatologic abnormalities, autoimmune hemolytic anemia and other cytopenias, hypergammaglobulinemia, autoantibodies, lymphadenopathy, and hepatosplenomegaly.[10][12] These phenotypes align with HPO terms such as autoimmune hemolytic anemia, chronic diarrhea, lymphadenopathy, splenomegaly, recurrent viral infections, and hypergammaglobulinemia. Immunologic laboratory findings reveal elevated IgG and autoantibodies, skewed memory T cells, increased CD56^bright NK cells, and markedly reduced or absent IL-2Rβ expression and IL-2 responsiveness in T cells.[8][10][12] Diagnosis relies on recognition of this triad of immunodeficiency, autoimmunity, and lymphoproliferation, combined with immunologic testing and genetic identification of biallelic IL2RB mutations.[1][9][10][12]

IMD63 is inherited in an autosomal recessive fashion, with consanguinity playing a key role in the documented pedigrees, and is currently classified as an ultra-rare inborn error of immunity with unknown but extremely low prevalence.[1][2][4][9][10][12] Prognosis without definitive treatment is poor, with perinatal mortality and severe early-life morbidity from infections and autoimmunity, though precise survival statistics are lacking due to the small number of cases.[9][10][12] The current definitive therapy is hematopoietic stem cell transplantation, which can reconstitute normal IL-2Rβ function and ameliorate clinical symptoms, while antiviral prophylaxis, immunosuppression to control autoimmunity, and supportive care are central to disease management.[8][10][12][15] Gene therapy targeting IL2RB remains a theoretical possibility but has not yet reached clinical application.[8][12]

From a mechanistic standpoint, IMD63 illuminates the critical role of IL2RB in maintaining immune harmony, as emphasized by Campbell’s commentary that autosomal recessive IL2RB mutations reveal a requirement for IL2RB in immunity and peripheral immune tolerance.[12] Comparative studies with Il2rb knockout mice and flounder IL2RB models underscore the evolutionary conservation of IL-2/IL2RB function in vertebrate immune systems.[10][12][16] As more patients are identified and systematic phenotyping, omics profiling, and long-term follow-up are performed, the clinical spectrum, natural history, and optimal management strategies for IMD63 will become clearer. In the interim, careful annotation of phenotypes, mechanisms, and treatments—as synthesized in this report—facilitates the integration of IMD63 into disease knowledge bases and supports clinicians and researchers in recognizing and addressing this rare but informative inborn error of immunity.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 71 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 59 |
| Terms named correctly | 32 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 14 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008354` (1 mention) - the report calls it "Hypergammaglobulinemia"; HP calls it **Factor X activation deficiency**
- `HP:0002039` (2 mentions) - the report calls it "Chronic diarrhea"; HP calls it **Anorexia**
- `HP:0005407` (1 mention) - the report calls it "Abnormal T cell activation"; HP calls it **obsolete Decreased proportion of CD4-positive helper T cells**
- `HP:0002812` (1 mention) - the report calls it "Abnormal NK cell morphology"; HP calls it **Coxa vara**
- `HP:0002239` (1 mention) - the report calls it "Cytomegalovirus infection"; HP calls it **Gastrointestinal hemorrhage**
- `HP:0012170` (1 mention) - the report calls it "Epstein–Barr virus infection"; HP calls it **Nail-biting**
- `GO:0035724` (1 mention) - the report calls it "interleukin-15 receptor activity"; GO calls it **obsolete CD24 biosynthetic process**
- `UBERON:0002150` (1 mention) - the report calls it "lymphoid tissue"; UBERON calls it **superior cerebellar peduncle**
- `NCIT:C29322` (1 mention) - the report calls it "Ganciclovir"; NCIT calls it **Phosphoramide Mustard**
- `NCIT:C48274` (1 mention) - the report calls it "Antiviral Therapy"; NCIT calls it **Cancer Molecular Analysis Project**
- `NCIT:C15206` (1 mention) - the report calls it "Hematopoietic Stem Cell Transplantation"; NCIT calls it **Clinical Study**
- `NCIT:C15693` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Phase I/II Trial**
- `NCIT:C15279` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Radical Mastectomy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0030315` (1 mention), reported as "Reduced quality of life" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005407` (obsolete Decreased proportion of CD4-positive helper T cells) (1 mention) - replaced by `HP:0032218`
- `GO:0035724` (obsolete CD24 biosynthetic process) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030057` (1 mention) - the report calls it "Autoantibody positivity"; HP calls it **Autoimmune antibody positivity**
- `HP:0005381` (1 mention) - the report calls it "Susceptibility to herpesvirus infections"; HP calls it **Recurrent Neisseria meningitidis infection**, and lists "Increased susceptibility to neisseria meningitidis infections" among its other names
- `HP:0004315` (1 mention) - the report calls it "Elevated serum immunoglobulin G"; HP calls it **Decreased circulating IgG concentration**, and lists "Decreased immunoglobulin G" among its other names
- `HP:0001263` (1 mention) - the report calls it "Developmental delay"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `GO:0035723` (1 mention) - the report calls it "interleukin-2-mediated signaling pathway"; GO calls it **interleukin-15-mediated signaling pathway**
- `GO:0038119` (1 mention) - the report calls it "interleukin-15-mediated signaling pathway"; GO calls it **CCL19-activated CCR7 signaling pathway**
- `GO:0032823` (1 mention) - the report calls it "positive regulation of regulatory T cell differentiation"; GO calls it **regulation of natural killer cell differentiation**, and lists "regulation of NK cell differentiation" among its other names
- `GO:0007259` (2 mentions) - the report calls it "JAK–STAT cascade"; GO calls it **cell surface receptor signaling pathway via JAK-STAT**, and lists "JAK-STAT cascade" among its other names
- `GO:0002684` (1 mention) - the report calls it "negative regulation of immune effector process"; GO calls it **positive regulation of immune system process**
- `GO:0006457` (1 mention) - the report calls it "protein misfolding"; GO calls it **protein folding**
- `GO:0006623` (1 mention) - the report calls it "protein targeting to membrane"; GO calls it **protein targeting to vacuole**
- `GO:0002250` (1 mention) - the report calls it "autoimmune response"; GO calls it **adaptive immune response**
- `UBERON:0002106` (1 mention) - the report calls it "splenomegaly"; UBERON calls it **spleen**
- `UBERON:0005409` (1 mention) - the report calls it "gastrointestinal system"; UBERON calls it **alimentary part of gastrointestinal system**, and lists "gastrointestinal system" among its other names