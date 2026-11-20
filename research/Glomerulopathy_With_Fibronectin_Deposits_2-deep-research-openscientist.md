---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T18:12:07.719784'
end_time: '2026-11-12T18:52:50.092191'
duration_seconds: 2442.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Glomerulopathy With Fibronectin Deposits 2
  mondo_id: MONDO:0011165
  category: Mendelian
  causal_genes: FN1
  omim_id: OMIM:601894
  synonyms: glomerulopathy with fibronectin deposits type 2; FN1 fibronectin glomerulopathy;
    fibronectin glomerulopathy caused by mutation in FN1
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 16
  relevance_assessed: 18
  on_topic: 17
  validator_version: 0.5.1
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 10
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0000093
    reported_labels:
    - Proteinuria
    - Lab/clinical
    ontology_label: Proteinuria
  - term_id: HP:0000790
    reported_labels:
    - Hematuria
    - Lab/clinical
    ontology_label: Hematuria
  - term_id: HP:0000822
    reported_labels:
    - Hypertension
    - Clinical sign
    ontology_label: Hypertension
  - term_id: HP:0000100
    reported_labels:
    - Nephrotic syndrome
    - Clinical
    ontology_label: Nephrotic syndrome
  - term_id: NCIT:C61602
    reported_labels:
    - ACE Inhibitor
    ontology_label: Atypia Confined to the Basal and Parabasal Epithelial Layers
  - term_id: NCIT:C98079
    reported_labels:
    - Angiotensin Receptor Blocker
    ontology_label: Meglitinide Antidiabetic Agent
  - term_id: NCIT:C1551
    reported_labels:
    - glucocorticoid
    ontology_label: Water-Soluble Vitamin
  - term_id: NCIT:C2367
    reported_labels:
    - Kidney Transplantation
    ontology_label: Triazene Derivative CB10-277
  - term_id: HP:0003077
    reported_labels:
    - Lab
    ontology_label: Hyperlipidemia
  - term_id: HP:0008341
    reported_labels:
    - Lab
    ontology_label: Distal renal tubular acidosis
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Glomerulopathy_With_Fibronectin_Deposits_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Glomerulopathy_With_Fibronectin_Deposits_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glomerulopathy With Fibronectin Deposits 2
- **MONDO ID:** MONDO:0011165 (if available)
- **Causal gene(s):** FN1
- **OMIM:** OMIM:601894
- **Synonyms:** glomerulopathy with fibronectin deposits type 2; FN1 fibronectin glomerulopathy; fibronectin glomerulopathy caused by mutation in FN1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Glomerulopathy With Fibronectin Deposits 2** covering all of the
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

# Glomerulopathy With Fibronectin Deposits 2 (GFND2): Comprehensive Disease Characterization Report

**Disease:** Glomerulopathy With Fibronectin Deposits 2 (GFND2)
**MONDO ID:** MONDO:0011165 | **OMIM:** 601894 | **Causal gene:** **FN1 (fibronectin 1, 2q35; HGNC:3778)**
**Category:** Mendelian (autosomal dominant)

---

## Summary

Glomerulopathy with fibronectin deposits 2 (GFND2; OMIM 601894, MONDO:0011165) is a rare autosomal dominant hereditary glomerular disease caused by heterozygous variants in **FN1**, the gene encoding **fibronectin 1**, located at chromosome 2q35. The disease is defined histopathologically by the pathognomonic feature of massive glomerular deposits of fibronectin in the mesangium and subendothelial space, producing a membranoproliferative glomerulonephritis (MPGN) type III-like architecture. Clinically, patients present with proteinuria (frequently in the nephrotic range), microscopic hematuria, hypertension, and slow but relentless progression to end-stage renal disease (ESRD), with terminal renal failure occurring at a median age of approximately 47 years in a large kindred.

Across the largest aggregated series of 72 genetically confirmed patients, the **fibronectin heparin-binding domain was identified as the mutational hotspot** [PMID: 42068364]. The recurrent, canonical variant is **NM_212482.4 c.2918A>G (p.Tyr973Cys / Y973C)**, reported across multiple unrelated patients and populations. Functional studies indicate a **gain/alteration-of-function mechanism**: at least one variant (c.3415G>A) increases fibronectin binding to integrin while decreasing binding to collagen type IV, driving glomerular-specific fibronectin deposition [PMID: 36774238]. A key pathogenic insight is that GFND2 **recurs in kidney allografts**, implicating circulating (plasma-derived) mutant fibronectin as the deposit source rather than a purely local kidney defect [PMID: 35774511, 22747478].

There is no disease-specific or curative therapy. Management is supportive nephroprotection—RAAS blockade (ACE inhibitors/ARBs), the angiotensin receptor-neprilysin inhibitor sacubitril/valsartan, and SGLT2 inhibitors as adjuncts—with inconsistent responses to immunosuppression. ESRD is managed by dialysis and kidney transplantation, though allograft recurrence is well documented. Research models are limited to patient-derived induced pluripotent stem cells (iPSCs); no established GFND2-specific animal model exists, partly because constitutive Fn1 knockout is embryonic lethal in mice. The disease is frequently misdiagnosed as MPGN type I/III, thrombotic microangiopathy (TMA), lupus, or IgA nephritis until fibronectin immunohistochemistry and FN1 genetic testing establish the correct diagnosis.

> **Evidence note:** GFND2 is an ultra-rare disease known from <100 genetically confirmed patients worldwide. Most evidence is Level IV/V (case reports, small families, mechanistic in vitro work). Quantitative epidemiology, controlled trials, and formal penetrance estimates are **not available**.

---

## Key Findings

### Finding 1 — GFND2 is an autosomal dominant glomerulopathy caused by FN1 mutations

GFND2 is a Mendelian, autosomal dominant kidney disease caused by heterozygous pathogenic variants in **FN1 (fibronectin 1)**, located at chromosome **2q35**. Multiple independent human cohorts and case reports have linked heterozygous FN1 variants to glomerulopathy with fibronectin deposits (GFND2, OMIM 601894). A comprehensive literature review of **72 genetically confirmed patients** established that the **fibronectin heparin-binding domain is a mutational hotspot** [PMID: 42068364]:

> "The comprehensive literature review of 72 patients revealed that the heparin-binding domain is a mutational hotspot" [PMID: 42068364]

The classic recurrent variant is **NM_212482.4 c.2918A>G (p.Tyr973Cys / Y973C)**, reported across multiple unrelated patients and distinct populations [PMID: 41642109, 39285372, 42675453]:

> "the FN1 gene was heterozygous for NM_212482.4 (c.2918A>G), that is, Y973C mutation" [PMID: 41642109]

This establishes both the gene–disease relationship and the recurrent hotspot that anchors molecular diagnosis. **Suggested ontology terms:** HGNC:3778 (FN1); MONDO:0011165; UBERON:0002113 (kidney).

### Finding 2 — Clinical phenotype: proteinuria, hematuria, hypertension, slow progression to ESRD (MPGN-like)

The clinical syndrome is consistent across case series: the main manifestations are **proteinuria** (often nephrotic-range), **microscopic hematuria**, **hypertension**, and **progressive decline in renal function** culminating in **end-stage renal disease** [PMID: 41656823]:

> "Proteinuria, hematuria, hypertension and progressive deterioration of renal function are the main clinical manifestations, which eventually develop into end-stage renal disease (ESRD)" [PMID: 41656823]

Histology shows an **MPGN type III-like pattern** with massive glomerular fibronectin deposits. The natural history is one of slow progression: in a large kindred, the **median age to terminal renal failure was ~47 years** [PMID: 10964510]:

> "an autosomal dominant kidney disease that leads to terminal renal failure at a median age of 47 years" [PMID: 10964510]

Onset is typically in the 2nd–5th decade (ages ~10–50 years) but the reported range is wide, from age 4 to 75 [PMID: 38254040, 39859354, 39285372]. **Suggested HPO terms:** HP:0000093 (Proteinuria), HP:0000790 (Hematuria), HP:0000822 (Hypertension), HP:0000083 (Renal insufficiency), HP:0003774 (Stage 5 chronic kidney disease), HP:0000100 (Nephrotic syndrome).

### Finding 3 — Mechanism: gain/alteration of matrix-binding function causing glomerular fibronectin deposition

Functional characterization supports a **gain-of-function / altered-binding** mechanism rather than simple loss of function. The FN1 variant c.3415G>A was shown to cause glomerular fibronectin-specific deposition in a gain-of-function manner, **increasing** fibronectin binding to integrin (maintaining podocyte adhesion) while **decreasing** binding to collagen type IV (COL4A3/4) [PMID: 36774238]:

> "a novel mutation (c.3415G>A) in FN1 that causes glomerular fibronectin-specific deposition in a gain-of-function manner" [PMID: 36774238]

> "this variant increased fibronectin's ability to bind to integrin, thereby maintaining podocyte adhesion" [PMID: 36774238]

The disease-defining histology is **massive mesangial and subendothelial fibronectin deposits** that are **PAS-positive, Jones silver-negative, and Congo red-negative**, with MPGN type III-like architecture [PMID: 10964510, 40529320]. Systemic (extra-renal) fibronectin deposition has been demonstrated in gastric mucosal extracellular matrix, indicating the defect is not confined to the kidney [PMID: 42068364]. **Suggested GO terms:** GO:0005178 (integrin binding), GO:0005518 (collagen binding), GO:0007160 (cell-matrix adhesion), GO:0030198 (extracellular matrix organization). **Suggested CL terms:** CL:0000653 (podocyte), CL:1000742 (glomerular mesangial cell). **Suggested UBERON:** UBERON:0001229 (renal glomerulus).

### Finding 4 — Allograft recurrence implicates circulating (plasma) fibronectin

A pivotal pathophysiological insight is that GFND2 **recurs in kidney allografts**, strongly implicating **circulating/plasma-derived mutant fibronectin** in the pathogenesis rather than a kidney-intrinsic defect alone. Multiple post-transplant recurrence cases are documented, including the first Japanese case [PMID: 22747478] and subsequent reports [PMID: 35774511, 37852577, 38053039], with recurrence occurring from weeks–months to ~27 months post-transplant:

> "Given the persistence of abnormal circulating fibronectin levels, FNG can relapse following renal transplantation. The circulating fibronectin deposits on grafts, and renal function progressively deteriorates after recurrence" [PMID: 35774511]

In one case, the mutant FN1 missense variant **reduced** fibronectin binding to heparin, endothelial cells, and podocytes and **impaired stress-fiber formation**, with persistent abnormal circulating fibronectin depositing on the graft [PMID: 35774511]:

> "a missense mutation in the fibronectin 1 (FN1) gene caused reduced binding to heparin, endothelial cells, and podocytes and impaired stress fiber formation" [PMID: 35774511]

Native disease typically progresses to kidney failure over 15–20 years. **This finding is clinically important:** because the pathogenic protein circulates, transplantation does not cure the underlying disease, and graft recurrence must be anticipated. **Suggested GO terms:** GO:0008201 (heparin binding), GO:0032956 (regulation of actin cytoskeleton organization).

### Finding 5 — Variant spectrum: dominant missense hotspots plus splice/in-frame deletions; frequent misdiagnosis

By 2025, approximately **ten exonic and one intronic pathogenic FN1 variants** had been catalogued, but **genotype–phenotype correlation data remain lacking** [PMID: 40120032]:

> "Currently, ten exonic and one intronic pathogenic variants in the fibronectin 1 gene have been identified; however, genotype-phenotype correlation data are lacking" [PMID: 40120032]

Variant types include:
- **Recurrent missense:** Y973C (c.2918A>G); W1925R; G417V [PMID: 39859354]
- **In-frame deletion:** c.5749_5751delACT (p.Thr1917del), de novo [PMID: 42068364]
- **Splice-site variants:** intron 36 c.5888-2A>G (familial) [PMID: 40120032]; c.5888-1G>C [PMID: 37801747]

De novo occurrence is documented [PMID: 38254040, 42068364]. Additional reported features include **hyperkalemic distal renal tubular acidosis** [PMID: 41642109] and **marked hyperlipidemia with intracapillary lipid deposition** [PMID: 42967636]. The disease is **frequently misdiagnosed** as MPGN type I/III, thrombotic microangiopathy, lupus nephritis, or IgA nephritis before fibronectin immunohistochemistry and FN1 genetics clarify it [PMID: 41642109, 35774511, 37852577]. Pathologic-genomic correlation—including glomerular proteomics detecting mutant-allele fibronectin peptides—has been used to reclassify variants of unknown significance (VUS) [PMID: 37852577]:

> "genetic studies showed a variant of unknown significance in the fibronectin 1 gene. Proteomic analyses of the glomeruli ... demonstrated large amount of fibronectin with abundant accumulation of the peptide synthesized by the detected variant" [PMID: 37852577]

### Finding 6 — Management is supportive/nephroprotective; no disease-specific therapy

No targeted or curative therapy exists. Management centers on **RAAS blockade** (ACE inhibitors/ARBs) to lower proteinuria and preserve function; in one elderly patient, conservative ARB therapy preserved function and reduced proteinuria over 2 years [PMID: 39285372]. The angiotensin receptor-neprilysin inhibitor **sacubitril/valsartan** has been used [PMID: 41642109; PMID: 42967636, where it was combined with simvastatin with stable renal function and lipids over 17 months]. **SGLT2 inhibitors** are employed as adjuncts [PMID: 42675453]:

> "prednisolone and cyclosporine A were initiated for management of nephrotic syndrome. The patient subsequently achieved partial remission" [PMID: 42675453]

> "a sodium-glucose cotransporter 2 (SGLT2) inhibitor was added as adjunct therapy" [PMID: 42675453]

Immunosuppression (glucocorticoids ± cyclosporine, tacrolimus, mizoribine, azathioprine) gives **variable/incomplete responses**: partial remission with prednisolone + cyclosporine + SGLT2i [PMID: 42675453], incomplete remission with glucocorticoid + mizoribine + ARB [PMID: 40120032], and no clear response to RASi + steroids + tacrolimus in another case [PMID: 40529320]. End-stage disease is managed by dialysis and kidney transplantation, but FNG can recur in the allograft [PMID: 22747478, 35774511]. **Suggested NCIT terms:** NCIT:C61602 (ACE Inhibitor), NCIT:C98079 (Angiotensin Receptor Blocker), NCIT:C1551 (glucocorticoid), NCIT:C2367 (Kidney Transplantation).

### Finding 7 — Research models limited to patient-derived iPSCs; systemic deposition documented

A patient-derived **induced pluripotent stem cell line (XJHi001-A)** was generated from an FNG patient carrying heterozygous FN1 c.5888-1G>C to study pathogenesis and test therapies [PMID: 37801747]:

> "we generated an induced pluripotent stem cell (iPSC) line from peripheral blood mononuclear cells (PBMCs) of a 32-years-old female patient who carried a heterozygous NM_212482.2(C.5888-1G > C) mutation in the FN1 gene" [PMID: 37801747]

Otherwise, variant effects have been studied **in vitro** via binding assays (integrin up, COL4 down [PMID: 36774238]; heparin/endothelial/podocyte binding down, impaired stress fibers [PMID: 35774511]) and by **glomerular proteomics** [PMID: 37852577]. Systemic involvement is shown by fibronectin deposition in gastric mucosal extracellular matrix [PMID: 42068364]:

> "Gastric mucosal immunohistochemistry revealed specific fibronectin deposition within the extracellular matrix, indicating systemic involvement" [PMID: 42068364]

**No GFND2-specific knockout/knock-in mouse disease model** is reported in this literature set; notably, constitutive Fn1 knockout is embryonic lethal in mice, limiting simple loss-of-function modeling.

### Finding 8 — Disease identity, locus heterogeneity, and diagnostic gold standard

GFND (MIM 601894) is an autosomal dominant kidney disease representing a **distinct entity of MPGN type III** characterized by the unique feature of massive glomerular fibronectin deposits [PMID: 10964510]:

> "It represents a distinct entity of membranoproliferative glomerulonephritis (MPGN) type III and is characterized by the unique feature of massive glomerular deposits of fibronectin" [PMID: 10964510]

An earlier GFND locus mapped to **chromosome 1q32 (GFND1)** in a large kindred with no causal gene identified [PMID: 10964510]; the gene-defined form is **FN1 at 2q35 = GFND2**. This represents **locus heterogeneity** within the GFND phenotype. Definitive diagnosis rests on biopsy showing **PAS-positive, silver-negative, Congo red-negative** mesangial/subendothelial deposits that **stain strongly for fibronectin by immunohistochemistry (IST-4 positive / IST-9 negative pattern)**, with confirmatory FN1 sequencing and, in ambiguous cases, glomerular mass-spectrometry proteomics detecting mutant-allele fibronectin peptides [PMID: 40529320, 22747478, 37852577]:

> "extensive periodic acid Schiff-positive but Jones' methenamine silver-negative and Congo red-negative mesangial and capillary wall deposits, which stained strongly for fibronectin on immunohistochemistry" [PMID: 40529320]

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous germline (occasionally de novo) variant in FN1** (hotspot in the heparin-binding domain; e.g., Y973C / c.2918A>G) **leads to** production of a structurally altered fibronectin protein.
2. The mutant fibronectin **alters its matrix-binding profile** — demonstrated for c.3415G>A as *increased* integrin binding and *decreased* collagen type IV binding [PMID: 36774238], and for another variant as *decreased* heparin/endothelial/podocyte binding with impaired stress-fiber formation [PMID: 35774511]. (Mechanism is variant-specific; a unifying biochemical theme is dysregulated ECM assembly rather than loss of fibronectin per se — *inferred*.)
3. Altered binding **results in** failure of normal fibronectin incorporation into the glomerular extracellular matrix and **aberrant accumulation/deposition** of fibronectin in the mesangium and subendothelial space.
4. Because mutant fibronectin **circulates in plasma** (*inferred* from allograft recurrence), deposition is continuously fed from the circulation — **this is why transplantation does not cure the disease and grafts recur** [PMID: 35774511, 22747478].
5. Massive fibronectin deposits **lead to** expansion of the mesangium, thickening/duplication of capillary walls, and an **MPGN type III-like architecture** that distorts the glomerular filtration barrier.
6. Disruption of the filtration barrier **results in** proteinuria (often nephrotic-range) and hematuria; glomerular/vascular involvement **contributes to** hypertension.
7. Progressive glomerular injury and secondary tubulointerstitial fibrosis **lead to** slow decline in GFR and, over ~15–20 years (median terminal failure ~47 years), **end-stage renal disease** [PMID: 10964510, 35774511].
8. **Branch — systemic involvement:** the same circulating mutant fibronectin **deposits in extra-renal extracellular matrix** (e.g., gastric mucosa), indicating GFND2 is a systemic ECM disorder with a predominantly renal phenotype [PMID: 42068364].

### Upstream vs downstream

| Tier | Event | Evidence type |
|------|-------|---------------|
| Upstream (initiating) | FN1 heterozygous variant (hotspot: heparin-binding domain) | Human genetics [PMID: 42068364, 41642109] |
| Upstream (molecular) | Altered fibronectin matrix-binding (integrin↑/COL4↓; heparin↓) | In vitro functional [PMID: 36774238, 35774511] |
| Intermediate | Circulating mutant fibronectin → glomerular deposition | Human (allograft recurrence) [PMID: 35774511, 22747478] |
| Downstream (tissue) | MPGN III-like remodeling, filtration-barrier disruption | Histopathology [PMID: 10964510, 40529320] |
| Downstream (clinical) | Proteinuria, hematuria, hypertension → ESRD | Human clinical [PMID: 41656823, 10964510] |

### Cell types and compartments

- **Cell types:** podocytes (CL:0000653), glomerular endothelial cells (CL:1001005), glomerular mesangial cells (CL:1000742); hepatocytes/plasma as the likely source of circulating fibronectin.
- **Anatomical sites (UBERON):** renal glomerulus (UBERON:0001229), glomerular basement membrane (UBERON:0002188), mesangium (UBERON:0005750), kidney (UBERON:0002113); extra-renal: stomach/gastric mucosa (UBERON:0001199).
- **Subcellular (GO CC):** extracellular matrix (GO:0031012), extracellular region (GO:0005576), actin cytoskeleton/stress fibers (GO:0001725).
- **Biological processes (GO BP):** extracellular matrix organization (GO:0030198), cell-matrix adhesion (GO:0007160), integrin-mediated signaling (GO:0007229).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Evidence type |
|------|-----------------|--------------|---------------|
| [10964510](https://pubmed.ncbi.nlm.nih.gov/10964510/) | Molecular cloning of critical region for GFND | Defines GFND as distinct MPGN III entity; 1q32 (GFND1) locus; median terminal failure ~47 y | Human genetics/clinical |
| [36774238](https://pubmed.ncbi.nlm.nih.gov/36774238/) | High-impact FN1 variant & decreased COL4 binding | Gain-of-function mechanism; integrin↑/COL4↓ | In vitro functional |
| [35774511](https://pubmed.ncbi.nlm.nih.gov/35774511/) | Recurrent deposition in renal allografts | Circulating fibronectin drives recurrence; heparin/podocyte binding↓ | Human + in vitro |
| [22747478](https://pubmed.ncbi.nlm.nih.gov/22747478/) | Recurrent FNG in renal transplant (first Japan) | Allograft recurrence; IST4+/IST9− diagnostic signature | Human clinical |
| [37852577](https://pubmed.ncbi.nlm.nih.gov/37852577/) | Pathologic-genomic correlation | VUS reclassification via glomerular proteomics | Human clinical/proteomics |
| [42068364](https://pubmed.ncbi.nlm.nih.gov/42068364/) | Pediatric FNG, p.Thr1917del, systemic involvement | 72-patient review: heparin-binding hotspot; gastric ECM deposition | Human review/clinical |
| [40120032](https://pubmed.ncbi.nlm.nih.gov/40120032/) | Familial FNG, splice-site variant | Catalogs ~10 exonic + 1 intronic variants; no genotype-phenotype data | Human genetics/clinical |
| [41656823](https://pubmed.ncbi.nlm.nih.gov/41656823/) | Glomerulopathy with fibronectin deposits | Canonical clinical quartet → ESRD | Human clinical |
| [41642109](https://pubmed.ncbi.nlm.nih.gov/41642109/) | FNG case + literature review | Documents recurrent Y973C; hyperkalemic distal RTA | Human clinical |
| [39285372](https://pubmed.ncbi.nlm.nih.gov/39285372/) | FNG in elderly patient | Y973C; ARB preserved function over 2 y | Human clinical |
| [42675453](https://pubmed.ncbi.nlm.nih.gov/42675453/) | Late-onset NS, 17-y course | Immunosuppression partial remission; SGLT2i adjunct | Human clinical |
| [42967636](https://pubmed.ncbi.nlm.nih.gov/42967636/) | FNG with intracapillary lipid deposition | Hyperlipidemia; sacubitril/valsartan + simvastatin | Human clinical |
| [37801747](https://pubmed.ncbi.nlm.nih.gov/37801747/) | iPSC line XJHi001-A | Patient-derived disease model; c.5888-1G>C | In vitro model |
| [38254040](https://pubmed.ncbi.nlm.nih.gov/38254040/) | FNG with MPGN features | De novo variant; IST-4 confirmation | Human clinical |
| [39859354](https://pubmed.ncbi.nlm.nih.gov/39859354/) | FNG without typical features, G417V | Atypical/early presentation (4-y-old) | Human clinical |
| [40529320](https://pubmed.ncbi.nlm.nih.gov/40529320/) | First African case report | Diagnostic histochemical signature | Human clinical |
| [38053039](https://pubmed.ncbi.nlm.nih.gov/38053039/) | FNG in allograft biopsy | Allograft recurrence; prior MPGN misdiagnosis | Human clinical |
| [42150947](https://pubmed.ncbi.nlm.nih.gov/42150947/) | FNG + chronic active ABMR in allograft | Allograft complexity; treatment-refractory | Human clinical |

**Overall evidence quality:** The evidence base is composed almost entirely of **case reports, small case series, and one 72-patient aggregated literature review**, reflecting the rarity of the disease. There are no randomized trials, no prospective cohorts, and no formal prevalence/incidence estimates. Mechanistic evidence rests on a handful of in vitro binding studies and one patient-derived iPSC line. This evidence tier is appropriate for an ultra-rare Mendelian disorder but limits the strength of quantitative and therapeutic conclusions.

---

## Section-by-Section Synthesis (Template Coverage)

### 1. Disease Information
GFND2 is a rare autosomal dominant hereditary glomerulopathy defined by massive glomerular fibronectin deposits. **Identifiers:** OMIM 601894; MONDO:0011165; causal gene FN1 (HGNC:3778, 2q35). **Synonyms:** glomerulopathy with fibronectin deposits type 2; FN1 fibronectin glomerulopathy; fibronectin glomerulopathy (FNG/FG). Information is derived from **aggregated disease-level resources and individual published patient case reports**, not EHR mining.

### 2. Etiology
**Primary cause is genetic:** heterozygous pathogenic FN1 variants (autosomal dominant). No environmental, infectious, or lifestyle cause is established. **Genetic risk:** causal FN1 variants (hotspot = heparin-binding domain; recurrent Y973C). No susceptibility loci, modifier genes, protective variants, or gene-environment interactions are documented for this ultra-rare monogenic disease. Note **locus heterogeneity**: a gene-unidentified GFND1 locus maps to 1q32 [PMID: 10964510].

### 3. Phenotypes
| Phenotype | Type | HPO | Onset/severity/frequency |
|-----------|------|-----|--------------------------|
| Proteinuria (often nephrotic) | Lab/clinical | HP:0000093 | Presenting sign; frequent/near-universal |
| Hematuria (microscopic) | Lab/clinical | HP:0000790 | Common |
| Hypertension | Clinical sign | HP:0000822 | Common |
| Progressive renal failure → ESRD | Clinical | HP:0000083 / HP:0003774 | Progressive; median terminal ~47 y |
| Nephrotic syndrome/edema | Clinical | HP:0000100 | Subset |
| Hyperlipidemia (reported) | Lab | HP:0003077 | Case-level [PMID: 42967636] |
| Distal renal tubular acidosis (hyperkalemic) | Lab | HP:0008341 | Case-level [PMID: 41642109] |

Onset ranges from age 4 to 75, typically 2nd–5th decade; progression is slow and chronic. Quality-of-life data are not formally reported, but the trajectory toward dialysis/transplant implies substantial long-term morbidity.

### 4. Genetic/Molecular Information
**Causal gene:** FN1 (disease OMIM 601894; gene OMIM 135600). **Variant types:** missense (Y973C/c.2918A>G, W1925R, G417V), in-frame deletion (p.Thr1917del), splice-site (c.5888-2A>G, c.5888-1G>C). ~10 exonic + 1 intronic pathogenic variants catalogued [PMID: 40120032]. **Origin:** germline (autosomal dominant), with de novo occurrences [PMID: 38254040, 42068364]. **Functional consequence:** gain/alteration-of-function (altered matrix binding) [PMID: 36774238], not classic loss of function. No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are established. Population allele frequencies are consistent with a very rare pathogenic variant set.

### 5. Environmental Information
No environmental factors, lifestyle factors, or infectious agents are implicated. GFND2 is a monogenic disorder; environmental contribution is **not applicable**.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain. Key pathway nodes: integrin binding (GO:0005178), collagen binding (GO:0005518), heparin binding (GO:0008201), ECM organization (GO:0030198). Upstream = FN1 variant + altered binding; downstream = glomerular deposition → filtration-barrier failure → ESRD. Circulating fibronectin is the inferred vehicle for continuous deposition.

### 7. Anatomical Structures Affected
**Primary organ:** kidney (UBERON:0002113), specifically the glomerulus (UBERON:0001229) — mesangium (UBERON:0005750) and subendothelial/capillary wall. **Cells:** podocytes (CL:0000653), mesangial cells (CL:1000742), glomerular endothelial cells. **Subcellular:** extracellular matrix (GO:0031012). **Extra-renal/systemic:** gastric mucosal ECM (UBERON:0001199) [PMID: 42068364]. Involvement is **bilateral** (systemic genetic disease).

### 8. Temporal Development
**Onset:** typically adult (2nd–5th decade); range age 4–75; **insidious/chronic**. **Progression:** slow and progressive to end-stage over ~15–20 years; median terminal renal failure ~47 years [PMID: 10964510, 35774511]. **Course:** chronic, progressive, lifelong; no spontaneous remission reported. Partial, treatment-associated proteinuria reduction is possible with nephroprotection/immunosuppression.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant. **Penetrance:** appears high but not formally quantified; variable expressivity and wide age-of-onset range noted. De novo variants occur. **Epidemiology:** no formal prevalence/incidence estimates exist — an ultra-rare disease with cases reported across Asian (Japanese, Korean, Chinese), European, and now African [PMID: 40529320] populations. No established founder effect, consanguinity role (AD disease), or sex predilection is documented. Genotype–phenotype correlation data are lacking [PMID: 40120032].

### 10. Diagnostics
**Gold standard:** kidney biopsy showing PAS-positive, Jones silver-negative, Congo red-negative mesangial/subendothelial deposits that stain strongly for **fibronectin by IHC (IST-4 positive / IST-9 negative)** [PMID: 40529320, 22747478], confirmed by **FN1 sequencing** (single-gene or panel/WES). Electron microscopy shows fibrillary/granular dense deposits. **Glomerular mass-spectrometry proteomics** can detect mutant-allele fibronectin peptides and reclassify VUS [PMID: 37852577]. **Differential diagnosis:** MPGN type I/III, thrombotic microangiopathy, lupus nephritis, IgA nephropathy, amyloidosis (excluded by Congo red negativity) — frequent misdiagnosis before fibronectin IHC/genetics [PMID: 41642109, 35774511, 37852577]. **Genetic testing** (single-gene FN1, renal gene panels, WES) is diagnostic and enables cascade family screening/counseling.

### 11. Outcome/Prognosis
Prognosis is **poor over the long term**: progressive decline to ESRD requiring dialysis/transplantation, median terminal renal failure ~47 years [PMID: 10964510]. No formal survival statistics beyond renal outcomes. **Prognostic factors** are not formally established (no genotype-phenotype correlation [PMID: 40120032]). Key complication is **allograft recurrence** after transplantation [PMID: 22747478, 35774511, 38053039], and concomitant antibody-mediated rejection can further threaten graft survival [PMID: 42150947].

### 12. Treatment
No disease-specific/curative therapy. **Supportive nephroprotection:** RAAS blockade (ACEi/ARB; NCIT:C61602/C98079) [PMID: 39285372]; sacubitril/valsartan [PMID: 41642109, 42967636]; SGLT2 inhibitors as adjuncts [PMID: 42675453]; statins for hyperlipidemia [PMID: 42967636]. **Immunosuppression** (glucocorticoids, cyclosporine, tacrolimus, mizoribine) yields variable/incomplete responses [PMID: 42675453, 40120032, 40529320]. **Renal replacement:** dialysis and kidney transplantation (NCIT:C2367) for ESRD, with recurrence risk. No approved gene, cell, or RNA-based therapy exists.

### 13. Prevention
No primary prevention (monogenic disease). **Secondary/tertiary prevention:** early diagnosis via biopsy + genetics, blood-pressure and proteinuria control to slow progression. **Genetic counseling** is central: autosomal dominant 50% transmission risk; cascade screening of relatives (e.g., retrospective recognition of affected deceased relatives previously labeled "type 1 MPGN" [PMID: 38053039]). Prenatal/preimplantation testing is theoretically possible once a familial variant is known.

### 14. Other Species / Natural Disease
FN1 is highly evolutionarily conserved (orthologs in mouse *Fn1*, etc.). No naturally occurring GFND2-equivalent disease in companion animals or wildlife is documented in this literature set. Veterinary/zoonotic relevance: **not applicable**.

### 15. Model Organisms
The principal model is a **patient-derived iPSC line (XJHi001-A)** carrying FN1 c.5888-1G>C [PMID: 37801747]. Mechanism is otherwise studied via **in vitro binding assays** and **glomerular proteomics**. **No GFND2-specific knockout/knock-in mouse model** is reported; constitutive *Fn1* knockout is embryonic lethal, so conditional or knock-in humanized approaches would be required. This is a major gap in the modeling toolkit.

---

## Limitations and Knowledge Gaps

1. **Evidence tier is low:** the literature is almost entirely case reports/series plus one 72-patient aggregated review. No prevalence/incidence, no controlled trials, no prospective natural-history cohorts.
2. **No genotype–phenotype correlation:** explicitly noted as lacking [PMID: 40120032]; it is unknown why some variants cause pediatric/rapidly progressive disease and others late-onset disease.
3. **Mechanistic heterogeneity unresolved:** different variants show opposite binding changes (integrin↑ in one [PMID: 36774238] vs. endothelial/podocyte/heparin binding↓ in another [PMID: 35774511]). A unifying biochemical model of how diverse binding defects all cause fibronectin deposition is not established.
4. **Source of circulating fibronectin not definitively localized:** allograft recurrence implicates a circulating (likely hepatic/plasma) mutant protein, but the tissue origin and whether lowering circulating mutant fibronectin would help are untested.
5. **No animal model:** absence of an in vivo GFND2 model limits preclinical therapeutic testing.
6. **No targeted therapy:** all management is nephroprotective/supportive; response to immunosuppression is inconsistent and likely reflects non-specific effects.
7. **Penetrance and expressivity not quantified.**

---

## Proposed Follow-up Experiments / Actions

1. **Build a FN1 variant–function map:** systematically express the ~10+ catalogued pathogenic variants and measure binding to integrin, collagen IV, heparin, endothelial cells, and podocytes, plus fibril assembly, to test whether a common downstream assembly defect unifies the gain/alteration-of-function mechanism.
2. **Establish an in vivo model:** generate a knock-in mouse (e.g., Fn1 Y973C) or liver-specific conditional humanized FN1 model to overcome embryonic lethality and recapitulate glomerular deposition; evaluate whether circulating mutant fibronectin is necessary and sufficient.
3. **Test the circulating-protein hypothesis therapeutically:** in iPSC-derived kidney organoids and animal models, assess whether reducing circulating mutant fibronectin (e.g., ASO/siRNA knockdown of the mutant allele, or plasma clearance strategies) prevents/reverses deposition — directly relevant to allograft recurrence.
4. **Create a GFND2 registry and natural-history study** to derive prevalence, penetrance, genotype–phenotype correlations, and prognostic biomarkers.
5. **Standardize diagnostic workflow:** promote fibronectin IHC (IST-4/IST-9) + FN1 genetics + glomerular proteomics as a reflex pathway for MPGN/TMA-like biopsies of unknown cause, to reduce the frequent misdiagnosis.
6. **Transplant management protocol:** prospectively characterize allograft recurrence rates, timing, and whether pre/peri-transplant interventions (e.g., mutant-protein lowering) reduce recurrence.
7. **Explore sacubitril/valsartan and SGLT2 inhibitors prospectively** as nephroprotective agents given encouraging anecdotal reports.

---

*Report compiled from 8 confirmed findings and 20 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are attributed to primary literature by PMID; direct quotes are drawn verbatim from the cited abstracts.*


## Artifacts

- [OpenScientist final report](Glomerulopathy_With_Fibronectin_Deposits_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Glomerulopathy_With_Fibronectin_Deposits_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000093` (2 mentions) - the report calls it "Proteinuria", "Lab/clinical"; HP calls it **Proteinuria**
- `HP:0000790` (2 mentions) - the report calls it "Hematuria", "Lab/clinical"; HP calls it **Hematuria**
- `HP:0000822` (2 mentions) - the report calls it "Hypertension", "Clinical sign"; HP calls it **Hypertension**
- `HP:0000100` (2 mentions) - the report calls it "Nephrotic syndrome", "Clinical"; HP calls it **Nephrotic syndrome**
- `NCIT:C61602` (2 mentions) - the report calls it "ACE Inhibitor"; NCIT calls it **Atypia Confined to the Basal and Parabasal Epithelial Layers**
- `NCIT:C98079` (1 mention) - the report calls it "Angiotensin Receptor Blocker"; NCIT calls it **Meglitinide Antidiabetic Agent**
- `NCIT:C1551` (1 mention) - the report calls it "glucocorticoid"; NCIT calls it **Water-Soluble Vitamin**
- `NCIT:C2367` (2 mentions) - the report calls it "Kidney Transplantation"; NCIT calls it **Triazene Derivative CB10-277**
- `HP:0003077` (1 mention) - the report calls it "Lab"; HP calls it **Hyperlipidemia**
- `HP:0008341` (1 mention) - the report calls it "Lab"; HP calls it **Distal renal tubular acidosis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000653` (3 mentions) - the report calls it "podocyte", "Cell types:** podocytes"; CL calls it **podocyte**, and lists "renal podocyte" among its other names
- `UBERON:0001229` (3 mentions) - the report calls it "renal glomerulus"; UBERON calls it **renal corpuscle**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000093` - called "Proteinuria", "Lab/clinical"
- `HP:0000790` - called "Hematuria", "Lab/clinical"
- `HP:0000822` - called "Hypertension", "Clinical sign"
- `HP:0000100` - called "Nephrotic syndrome", "Clinical"
- `CL:0000653` - called "podocyte", "Cell types:** podocytes"