---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T21:31:41.355859'
end_time: '2026-08-28T21:45:26.958053'
duration_seconds: 825.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paget Disease of Bone
  mondo_id: ''
  category: Metabolic Bone Disorder
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
citation_count: 33
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 9
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:38963497
  - PMID:33768371
  - PMID:21515589
  relevance_assessed: 34
  on_topic: 24
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0002750
    reported_labels:
    - Abnormal long bone morphology
    ontology_label: Delayed skeletal maturation
  labels_variant: 3
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
  path: Paget_Disease_of_Bone-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Paget_Disease_of_Bone-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paget Disease of Bone
- **MONDO ID:**  (if available)
- **Category:** Metabolic Bone Disorder

## Research Objectives

Please provide a comprehensive research report on **Paget Disease of Bone** covering all of the
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

# Paget Disease of Bone — Comprehensive Disease Characteristics Report

**Disease:** Paget Disease of Bone (PDB; osteitis deformans)
**Category:** Metabolic Bone Disorder
**Primary identifiers:** MONDO:0005479 · OMIM #167250 (PDB2, SQSTM1) / #602080 (PDB3) / #616833 (PDB6, ZNF687) · Orphanet ORPHA:2801 · ICD-10 M88 · ICD-11 FB80.0 · MeSH D010001 (Osteitis Deformans)
**Evidence base:** 9 confirmed findings, 39 primary papers reviewed across 5 iterations. Evidence is drawn from aggregated disease-level resources (OMIM, Orphanet, GWAS meta-analyses, guideline statements), human clinical cohorts and registries, knock-in mouse models, and in-vitro osteoclast studies.

---

## Summary

Paget disease of bone (PDB) is a chronic, focal, adult-onset metabolic bone disorder in which giant, hyperactive, hypernucleated osteoclasts drive intense localized bone resorption. This is followed by a disorganized compensatory increase in osteoblastic bone formation, producing expanded, structurally weak, hypervascular "mosaic" bone (mixed woven and lamellar). Clinically this manifests as bone pain, deformity, secondary osteoarthritis, pathological fracture, deafness (when the skull is involved), and — rarely (~0.7–1%) — malignant transformation to osteosarcoma. Many patients are asymptomatic and are detected incidentally through an elevated serum alkaline phosphatase (ALP) or an X-ray taken for another reason.

PDB is best understood as a **complex gene–environment disorder that converges on the osteoclast RANK–RANKL–OPG signaling axis and p62/autophagy machinery**. Mutations affecting the ubiquitin-associated (UBA) domain of **SQSTM1** (which encodes p62), especially the recurrent **p.P392L** variant, are the single most common genetic cause. Beyond SQSTM1, rarer causal genes (ZNF687, PFN1, VCP) and at least seven common susceptibility loci (CSF1, OPTN, TNFRSF11A/RANK, TM7SF4/DCSTAMP, PML, RIN3, NUP205) shape polygenic risk. A parallel, distinct recessive childhood disorder — **juvenile Paget's disease** — is caused chiefly by loss of osteoprotegerin (TNFRSF11B/OPG), directly confirming the centrality of the RANK–RANKL–OPG axis. The steadily declining incidence and severity of PDB across multiple countries strongly implicates a diminishing environmental trigger whose identity remains unresolved.

Diagnosis rests on the combination of characteristic plain radiographs, an elevated serum ALP (the standard marker of disease activity), and a technetium-99m radionuclide bone scan to map disease extent. A **single 5-mg intravenous infusion of zoledronic acid** is first-line therapy and produces durable biochemical remission in ~90–97% of patients — far superior to older bisphosphonates — although a large randomized trial (PRISM-EZ) showed that intensively normalizing bone turnover does not improve fractures, pain, or quality of life versus symptomatic management. This report details all requested disease characteristics with primary-literature citations.

---

## Section 1 — Disease Information

PDB is a chronic focal disorder of bone remodeling, the **second most common metabolic bone disease after osteoporosis** ([PMID: 28690091](https://pubmed.ncbi.nlm.nih.gov/28690091/)). It is characterized by "increased osteoclast-mediated bone resorption and a subsequent compensatory increase in bone formation, resulting in a disorganized mosaic of woven and lamellar bone at one or more affected skeletal sites" ([PMID: 30671590](https://pubmed.ncbi.nlm.nih.gov/30671590/)).

**Key identifiers:** MONDO:0005479; OMIM #167250 (classic SQSTM1-related PDB2), with additional loci PDB3 (#602080) and PDB6/ZNF687 (#616833); Orphanet ORPHA:2801; ICD-10 M88 (with subsite codes M88.0 skull, M88.8 other bones, M88.9 unspecified); ICD-11 FB80.0; MeSH D010001 (Osteitis Deformans).

**Synonyms / alternative names:** Osteitis deformans; Paget's disease of bone; Paget disease, bone; osteitis deformans of Paget. (Note: distinct from Paget disease of the breast/nipple and extramammary Paget disease, which are unrelated epithelial neoplasms.)

**Information source type:** Predominantly aggregated disease-level resources (OMIM, Orphanet, GWAS meta-analyses, guideline statements) supplemented by clinical cohorts, health-administrative databases (e.g., Quebec, UK), and disease registries. Some findings derive from individual-patient EHR/registry data (e.g., contemporary vs historical cohort comparisons; VCP CoRDS registry).

---

## Section 2 — Etiology

**Primary causal factors.** PDB is a genetically heterogeneous disorder with a strong hereditary component overlaid on one or more environmental triggers. As reviewed, "PDB is a genetically heterogeneous disorder, with mutations in at least two different genes (SQSTM1, ZNF687) and more common predisposing variants," while "the focal nature of lesions, the decline in prevalence rates, and the incomplete penetrance of the disease among family members suggest that one or more environmental triggers may play a role" ([PMID: 30671590](https://pubmed.ncbi.nlm.nih.gov/30671590/)).

**Genetic risk factors.**
- **Causal:** SQSTM1 UBA-domain mutations (p.P392L most common) — present in ~10–40% of familial and ~5–10% of sporadic cases (Finding F001). Rarer causal genes: ZNF687 and PFN1 (severe, early-onset, polyostotic, giant-cell-tumor–prone forms) and VCP (syndromic PDB).
- **Susceptibility loci:** Seven common GWAS loci — CSF1 (1p13), OPTN (10p13), TNFRSF11A/RANK (18q21), TM7SF4/DCSTAMP (rs2458413), PML (rs5742915), RIN3 (rs10498635), NUP205 (rs4294134) — together explaining ~13% of familial risk (Finding F006; [PMID: 21623375](https://pubmed.ncbi.nlm.nih.gov/21623375/)).

**Environmental risk factors.** Age (incidence rises sharply after ~55 y), male sex, and family history are the principal established risk factors. Geographic and rural clustering suggests an environmental/zoonotic contribution: a Spanish study of 2,342 new cases found a moderate positive correlation between PDB incidence and density of female breeding cattle (R²=0.236) ([PMID: 40408225](https://pubmed.ncbi.nlm.nih.gov/40408225/)). A separate hypothesis links historical PDB prevalence to domestic bituminous coal burning ([PMID: 38902530](https://pubmed.ncbi.nlm.nih.gov/38902530/)). The long-postulated chronic **paramyxovirus (measles) infection** of osteoclasts remains unconfirmed and contested (see Section 5).

**Protective factors.** No validated genetic protective variants or dietary/lifestyle protective factors are established. The declining incidence implies that **reduced exposure to the (unidentified) environmental trigger** is effectively protective at the population level (Finding F002).

**Gene–environment interactions.** The prevailing model holds that a genetic predisposition (e.g., SQSTM1/p62 UBA mutation or risk alleles at RANK/OPTN/CSF1/DCSTAMP) sensitizes osteoclast precursors, which then require an environmental "second hit" to produce focal lesions — explaining incomplete penetrance and the focal, localized nature of disease despite a germline mutation present in every cell (Findings F001, F009).

---

## Section 3 — Phenotypes

| Phenotype | Type | HPO term | Characteristics / frequency |
|---|---|---|---|
| Bone pain | Symptom | HP:0002653 (Bone pain) | Most common symptom; ~52% of symptomatic patients report pagetic bone pain in both historical and contemporary cohorts ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)); progressive/fluctuating |
| Bone deformity (bowing of long bones, skull enlargement) | Physical manifestation | HP:0002750 (Abnormal long bone morphology) | 13% contemporary vs 54% historical cohort — declining severity ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)) |
| Pathological fracture | Clinical sign | HP:0002659 (Increased susceptibility to fractures) | 6.7% contemporary vs 36.7% historical ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)) |
| Secondary osteoarthritis | Clinical sign | HP:0002758 (Osteoarthritis) | ~43–52% of patients ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)) |
| Hearing impairment (skull involvement) | Clinical sign | HP:0000365 (Hearing impairment) | ~52–61% when skull affected ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)) |
| Elevated serum alkaline phosphatase | Laboratory abnormality | HP:0003155 (Elevated circulating ALP) | Core biochemical hallmark; reflects disease activity/extent |
| Skull enlargement / cranial nerve compression | Physical manifestation | HP:0000256 (Macrocephaly); HP:0000365 | Variable |
| Osteosarcoma (malignant transformation) | Clinical sign | HP:0002669 (Osteosarcoma) | Rare, ~0.7–1% (see Section 11) |

**Age of onset:** adult/late-onset; typically diagnosed after age 55, mean age at diagnosis ~68.7 y in a contemporary cohort ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)). **Progression:** slowly progressive but focally stable; individual lesions expand over years. **Severity:** highly variable, ranging from asymptomatic incidental findings (~85% at diagnosis in contemporary series) to disabling deformity. **Quality-of-life impact:** driven mainly by chronic pain, deformity, secondary arthritis, and deafness; notably, the PRISM-EZ RCT found no QoL benefit from intensive bone-turnover suppression ([PMID: 28176386](https://pubmed.ncbi.nlm.nih.gov/28176386/)).

Contemporary disease is milder: patients are older at diagnosis, more often monostotic (60.5%), with lower ALP, fewer pagetic bones, fewer fractures and deformities than historical cohorts ([PMID: 36858336](https://pubmed.ncbi.nlm.nih.gov/36858336/)).

---

## Section 4 — Genetic / Molecular Information

**Causal genes.**
- **SQSTM1** (HGNC:11280; encodes p62/sequestosome-1; OMIM *601530) — the major gene. UBA-domain mutations, recurrent **p.P392L (c.1175C>T)**, occur in ~10–40% of familial and ~5–10% of sporadic PDB and associate with more severe/extensive disease ([PMID: 37180975](https://pubmed.ncbi.nlm.nih.gov/37180975/); Finding F001). Functional consequence: impaired ubiquitin binding → dysregulated NF-κB signaling and autophagy → osteoclast hyperactivity.
- **ZNF687** (HGNC:13809) — causes severe, early-onset, polyostotic PDB with giant-cell tumor predisposition; variants cluster in the nuclear localization signal (e.g., p.Pro937Arg, p.Pro937His, p.Arg939Cys) ([PMID: 37728743](https://pubmed.ncbi.nlm.nih.gov/37728743/)).
- **PFN1** (profilin-1) — very rare cause of severe PDB; essentially absent in most cohorts ([PMID: 37728743](https://pubmed.ncbi.nlm.nih.gov/37728743/)).
- **VCP** (p97; HGNC:12666) — autosomal-dominant missense mutations cause syndromic PDB within multisystem proteinopathy (see Section 6 & Finding F005).
- **TNFRSF11B/OPG, TNFRSF11A/RANK, SP7/osterix** — cause the distinct recessive juvenile Paget's disease (Finding F008).

**Variant classification (ACMG/AMP):** SQSTM1 p.P392L and other recurrent UBA-domain variants are classified pathogenic/likely pathogenic; ZNF687 NLS variants are supported as disease-associated ([PMID: 37728743](https://pubmed.ncbi.nlm.nih.gov/37728743/)). Variant types are predominantly **missense**, with some truncating UBA-domain variants; large deletions dominate the most severe JPD phenotypes.

**Somatic vs germline:** Causal variants are **germline**. Somatic changes are relevant to the osteosarcomas that arise in pagetic bone (COSMIC-type analysis beyond present scope).

**Modifier genes:** The seven GWAS loci act as susceptibility/severity modifiers on top of SQSTM1; DCSTAMP, OPTN and CSF1 modulate osteoclast fusion and differentiation.

**Epigenetic / chromosomal:** No recurrent large-scale chromosomal abnormality defines classic PDB (JPD can involve large TNFRSF11B deletions). Systematic disease-specific methylation/histone data were not identified in the reviewed literature — a knowledge gap.

---

## Section 5 — Environmental Information

**Environmental / occupational factors.** Rural residence and proximity to livestock correlate with higher incidence (breeding-cattle density R²=0.236) ([PMID: 40408225](https://pubmed.ncbi.nlm.nih.gov/40408225/)). Historical domestic coal combustion has been proposed as a candidate exposure whose decline parallels falling PDB prevalence ([PMID: 38902530](https://pubmed.ncbi.nlm.nih.gov/38902530/)).

**Lifestyle factors.** No robust smoking/diet/alcohol association is established; age and male sex remain the dominant demographic risk factors.

**Infectious agents (contested).** A chronic **paramyxovirus** infection of osteoclasts — variously measles virus (MV), respiratory syncytial virus (RSV), or canine distemper virus (CDV) — has been hypothesized for decades. Supporting: measles virus RNA was detected by in-situ hybridization in pagetic osteoclasts and other bone cells but not controls ([PMID: 3701300](https://pubmed.ncbi.nlm.nih.gov/3701300/)). Refuting: PCR failed to detect paramyxovirus sequences in pagetic bone from 10 consecutive patients ([PMID: 1805546](https://pubmed.ncbi.nlm.nih.gov/1805546/)); prior dog/cat ownership was not a risk factor in 433 US cases ([PMID: 2376461](https://pubmed.ncbi.nlm.nih.gov/2376461/)); and a serological study of 463 patients found no elevation of MV/CDV/RSV antibodies (only a modest increase in mumps antibody) ([PMID: 28361207](https://pubmed.ncbi.nlm.nih.gov/28361207/)). **Net assessment: the viral hypothesis remains unproven and is not currently supported by the weight of evidence.**

---

## Section 6 — Mechanism / Pathophysiology

**Central causal chain (Finding F009).** Genetic predisposition (SQSTM1/p62 UBA mutation; risk alleles at TNFRSF11A/RANK, OPTN, CSF1, TM7SF4/DCSTAMP) + a putative environmental trigger → **osteoclast precursor hypersensitivity to RANKL** → dysregulated **NF-κB signaling** and **autophagy** (increased SQSTM1, ATG5, LC3-II) → formation of **giant, hypernucleated, hyperactive osteoclasts** with nuclear inclusions → focal intense **bone resorption** → compensatory **disorganized osteoblastic bone formation** (mixed woven + lamellar "mosaic" bone) → **expanded, weak, hypervascular** bone → pain, deformity, fracture, deafness, and rare osteosarcoma.

The osteoclast is the central effector: "the osteoclast, a myeloid-derived cell responsible for bone resorption, contributes to the disease" ([PMID: 33768371](https://pubmed.ncbi.nlm.nih.gov/33768371/)). The P394L knock-in mouse confirms autophagy dysregulation downstream of the UBA mutation, with "increased expression of sqstm1, autophagy-related gene 5 (atg5) and light chain 3 gene (lc3) in osteoclast precursors" ([PMID: 21515589](https://pubmed.ncbi.nlm.nih.gov/21515589/)).

**Molecular pathways.** RANK–RANKL–OPG (TNFRSF11A–TNFSF11–TNFRSF11B) axis; NF-κB signaling; ubiquitin–proteasome system and autophagy/lysosomal degradation (p62, VCP). GO suggestions: GO:0045672 (positive regulation of osteoclast differentiation), GO:0006914 (autophagy), GO:0043123 (positive regulation of canonical NF-κB signal transduction), GO:0045453 (bone resorption), GO:0002446 (neutrophil/myeloid-lineage regulation).

**Protein dysfunction.** p62 UBA-domain mutations impair ubiquitin binding, disrupting selective autophagy and NF-κB regulation. VCP/p97 is an AAA+ ATPase; "pathogenic mutations frequently found at the interface between the NTD domain and D1 ATPase domain … cause malfunction of VCP" ([PMID: 38963497](https://pubmed.ncbi.nlm.nih.gov/38963497/)). MSP genes "share disruption of RNA stress granule function and autophagic degradation" ([PMID: 33145792](https://pubmed.ncbi.nlm.nih.gov/33145792/)).

**Cell types (CL):** osteoclast (CL:0000092), osteoblast (CL:0000062), osteocyte (CL:0000137), osteoclast precursor / myeloid monocyte lineage. **Subcellular (GO CC):** autophagosome (GO:0005776), lysosome (GO:0005764), nucleus/nuclear inclusion bodies, cytoplasmic ubiquitin-rich inclusions.

**Immune/inflammatory involvement.** Osteoimmunology is central: RANKL-driven osteoclastogenesis is regulated by immune signaling; PDB is framed as an osteoclast-centric immunoskeletal disorder in "Osteoimmunology and Osteoclast Pathology" ([PMID: 33768371](https://pubmed.ncbi.nlm.nih.gov/33768371/)).

**Metabolic changes.** High local bone turnover markedly elevates serum ALP and collagen breakdown products; systemic metabolic derangement is uncommon except high-output cardiac states in extensive polyostotic disease.

---

## Section 7 — Anatomical Structures Affected

**Organ/skeletal-site level.** PDB is focal and can be monostotic or polyostotic. Commonly affected sites (UBERON): pelvis (UBERON:0001270), spine/vertebral column especially lumbar (UBERON:0001130), femur (UBERON:0000981), skull (UBERON:0000033), tibia (UBERON:0000979). Skull involvement causes cranial nerve compression and hearing loss; spinal involvement can cause radiculopathy/myelopathy. The spine — particularly the lumbar spine — is a common site and a frequent location of malignant transformation ([PMID: 42359209](https://pubmed.ncbi.nlm.nih.gov/42359209/)).

**Secondary/system involvement.** Cardiovascular (high-output state in extensive disease), nervous system (nerve/cord compression, deafness), joints (secondary osteoarthritis). **Tissue level:** bone/connective tissue; hypervascular marrow fibrosis. **Cell populations (CL):** osteoclasts (primary), osteoblasts, osteocytes.

**Localization/laterality.** Lesions are typically **asymmetric and focal**, may be unilateral or bilateral, and characteristically do not cross joint spaces; disease begins at one end of a long bone and advances along it (the radiographic "blade of grass"/flame-shaped front).

---

## Section 8 — Temporal Development

**Onset.** Adult/late-onset, chronic, insidious; rarely diagnosed before age 40. Classic PDB is essentially never congenital (contrast juvenile Paget's disease, which presents in infancy/childhood — Section 9).

**Progression.** Individual lesions advance slowly and locally; overall the disease is chronic and lifelong but not systemically progressive in most patients. Stages within a lesion: an early **osteolytic/resorptive** phase → a **mixed** phase → a late **sclerotic/burnt-out** phase.

**Patterns.** Biochemical remission is **treatment-induced** (bisphosphonates); spontaneous remission of established lesions does not occur. The main "critical period" for intervention is symptomatic active disease with elevated ALP, where a single zoledronic acid infusion yields prolonged suppression ([PMID: 31574000](https://pubmed.ncbi.nlm.nih.gov/31574000/)).

---

## Section 9 — Inheritance and Population

**Epidemiology.** PDB is common in older adults of European descent but is **declining**. UK standardized incidence fell from 0.75/10,000 person-years (1999) to 0.20/10,000 (2015) ([PMID: 33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/)). In Quebec, standardized incidence fell from 0.77/1,000 (2000/01) to 0.28/1,000 (2019/20) while standardized prevalence stayed stable (~0.44% → 0.43%) ([PMID: 37683713](https://pubmed.ncbi.nlm.nih.gov/37683713/)). Incidence rises steeply with age (UK crude incidence ≥85 y: 6.3/10,000 men, 3.7/10,000 women) and is higher in men.

**Inheritance.** Classic PDB is **complex/polygenic** with autosomal-dominant familial clustering in SQSTM1-linked families showing **incomplete, age-dependent penetrance** and **variable expressivity**. About 15–40% of patients have a family history. Seven common loci explain ~13% of familial risk ([PMID: 21623375](https://pubmed.ncbi.nlm.nih.gov/21623375/)).

**Juvenile Paget's disease (JPD; OMIM 239000)** is a distinct **autosomal-recessive** disorder, most often from biallelic loss-of-function of **TNFRSF11B/OPG** — first shown as a homozygous deletion in Navajos ([PMID: 32298837](https://pubmed.ncbi.nlm.nih.gov/32298837/)); the most severe phenotypes arise from "major gene deletions or mutations affecting cysteine residues in the ligand-binding domain" ([PMID: 25108083](https://pubmed.ncbi.nlm.nih.gov/25108083/)). Heterozygous TNFRSF11A/RANK duplication and heterozygous SP7 mutation are rarer causes.

**Population demographics.** Highest prevalence historically in Britain and in populations of British descent (North America, Australia, New Zealand); largely absent in indigenous populations of those regions and low in Asia/Africa ([PMID: 38902530](https://pubmed.ncbi.nlm.nih.gov/38902530/)). Male predominance (male:female ≈ 1.2–1.4:1). Founder effects operate in JPD (Navajo TNFRSF11B deletion).

---

## Section 10 — Diagnostics

**Recommended workup (Finding F007).** Guidelines (Endocrine Society 2014; IOF/ASBMR/ECTS/UK Bone Research Society 2019) recommend **plain radiography + serum total alkaline phosphatase** for initial diagnosis and **technetium-99m radionuclide bone scintigraphy** to delineate extent ([PMID: 32803929](https://pubmed.ncbi.nlm.nih.gov/32803929/); [PMID: 31574000](https://pubmed.ncbi.nlm.nih.gov/31574000/)).

- **Laboratory:** Elevated serum total ALP (bone-specific ALP if hepatic/pregnancy confounding); markers of bone turnover (P1NP, serum/urinary CTX, NTX) to assess activity and treatment response, typically remeasured at 3–6 months. Serum calcium usually normal.
- **Imaging:** X-ray shows cortical thickening, coarse trabeculation, bone expansion, osteoporosis circumscripta (skull), and the flame-shaped advancing lytic front in long bones. Bone scan identifies all active sites. CT/MRI is reserved for complications and suspected malignant transformation ([PMID: 42359209](https://pubmed.ncbi.nlm.nih.gov/42359209/)).
- **Biopsy:** Not routinely required; reserved for atypical lesions or to exclude sarcoma. Histology shows the pathognomonic "mosaic" pattern with giant multinucleated osteoclasts.
- **Genetic testing:** SQSTM1 sequencing (single-gene / small panels including ZNF687, VCP, PFN1) is available but **not routine** — used mainly in early-onset, severe, or strongly familial disease and for research/cascade evaluation. WES/WGS have research utility for gene discovery.

**Clinical criteria & differential diagnosis.** Diagnosis is radiographic + biochemical. Differentials: osteoblastic metastases (esp. prostate/breast), primary bone tumors, sclerotic/lytic metabolic bone disease, fibrous dysplasia, and hyperparathyroidism.

**Screening.** No population screening is recommended. Because ALP elevation is often incidental, biochemical detection is common. Cascade genetic screening of relatives in SQSTM1 families is possible but not standard given incomplete penetrance and lack of proven benefit from early asymptomatic treatment.

---

## Section 11 — Outcome / Prognosis

**Overall prognosis** is good for most patients; PDB is usually not life-limiting, and modern disease is milder. Prognosis "mainly depends on the occurrence of complications involving bones and joints, neurological, cardiovascular or metabolic systems" ([PMID: 28690091](https://pubmed.ncbi.nlm.nih.gov/28690091/)).

**Complications.** Bone pain, deformity, secondary osteoarthritis, pathological fracture, deafness/cranial neuropathy, spinal stenosis, high-output cardiac failure (extensive disease), and — rarely — sarcomatous transformation.

**Malignant transformation (Finding F004).** Osteosarcoma occurs in ~0.7–1% of patients (historically up to ~5.5%). Contemporary incidence: "The incidence of malignant transformation was 0.7%, and the most frequent histologic type was osteogenic sarcoma" ([PMID: 1451058](https://pubmed.ncbi.nlm.nih.gov/1451058/)). Tumors are mostly high-grade osteosarcomas (~88%), arise in older men (mean ~66 y), predominate in axial skeleton/pelvis and femur, and carry a dismal **~10% 5-year survival** ([PMID: 17550323](https://pubmed.ncbi.nlm.nih.gov/17550323/)). Surgery ± chemotherapy offers the only realistic survival benefit but outcomes remain poor ([PMID: 20652460](https://pubmed.ncbi.nlm.nih.gov/20652460/); [PMID: 42359209](https://pubmed.ncbi.nlm.nih.gov/42359209/)).

**Prognostic factors.** Extent/number of bones involved and baseline ALP correlate with disease burden; notably, sarcoma risk did **not** significantly correlate with number of bones involved or disease duration ([PMID: 17550323](https://pubmed.ncbi.nlm.nih.gov/17550323/)). New/worsening pain, a soft-tissue mass, or a lytic lesion in known pagetic bone should prompt urgent evaluation for malignancy.

---

## Section 12 — Treatment

**First-line pharmacotherapy: intravenous bisphosphonates (NCIT: Zoledronic Acid; Bisphosphonate).**
A **single 5-mg IV zoledronic acid infusion** is standard first-line therapy and produces durable biochemical remission (Finding F003). It normalizes bone-turnover markers in the majority for ≥2 years independent of prior therapy ([PMID: 17032148](https://pubmed.ncbi.nlm.nih.gov/17032148/)), and in head-to-head trials achieved therapeutic response in ~90–97% of patients versus ~45% for pamidronate ([PMID: 17605632](https://pubmed.ncbi.nlm.nih.gov/17605632/)). Long-term durability: over 6.5 years without retreatment, relapse occurred in only 1/152 (0.7%) zoledronate vs 23/115 (20%) risedronate patients (p<0.001) ([PMID: 21638319](https://pubmed.ncbi.nlm.nih.gov/21638319/)).

| Regimen | Therapeutic response | Durability |
|---|---|---|
| Zoledronic acid 5 mg IV (single) | ~90–97% | 1/152 relapse at 6.5 y ([PMID: 21638319](https://pubmed.ncbi.nlm.nih.gov/21638319/)) |
| Neridronate 200 mg (IV or IM) | 92.6% (IV), 96.5% (IM) at 6 mo | Response declines by 24–36 mo ([PMID: 20814970](https://pubmed.ncbi.nlm.nih.gov/20814970/)) |
| Pamidronate 30 mg IV | ~45% | Inferior ([PMID: 17605632](https://pubmed.ncbi.nlm.nih.gov/17605632/)) |
| Risedronate 30 mg PO | Lower | 20% relapse at 6.5 y ([PMID: 21638319](https://pubmed.ncbi.nlm.nih.gov/21638319/)) |

**Treatment goal — an important caveat.** Despite superb biochemical control, the PRISM-EZ RCT (n=502) found that intensively normalizing bone turnover did **not** reduce fractures, orthopedic procedures, or bone pain, nor improve quality of life versus symptomatic treatment: "There were no clinically important differences in quality of life measures or bone pain between the treatment groups" ([PMID: 28176386](https://pubmed.ncbi.nlm.nih.gov/28176386/)). Treatment is therefore aimed mainly at **symptom (pain) relief and protection of complication-prone sites**, not universal biochemical normalization.

**Supportive care.** Analgesics/NSAIDs for pain; calcium and vitamin D repletion before bisphosphonate dosing (response correlates with 25(OH)D — [PMID: 20814970](https://pubmed.ncbi.nlm.nih.gov/20814970/)); physical therapy, hearing aids. **Surgery:** joint replacement for pagetic osteoarthritis, fracture fixation, osteotomy for deformity, decompression for neural compression; pre-operative bisphosphonate reduces hypervascular bleeding. **Experimental/advanced:** no gene, cell, or RNA therapy is approved for PDB. Adverse events of IV bisphosphonates: acute-phase reaction (~14%), hypocalcemia, and rare osteonecrosis of the jaw and atypical femoral fractures.

---

## Section 13 — Prevention

- **Primary prevention:** None established, because the environmental trigger is unidentified. The natural population-level decline in incidence suggests reduced trigger exposure is effectively preventive ([PMID: 33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/); [PMID: 38902530](https://pubmed.ncbi.nlm.nih.gov/38902530/)).
- **Secondary prevention:** Detection via incidental ALP elevation or radiographs; no formal population screening program.
- **Tertiary prevention:** Bisphosphonates and vitamin D/calcium repletion to control active disease; orthopedic surveillance; prompt imaging + biopsy for suspected sarcoma.
- **Genetic counseling:** Appropriate for early-onset/familial (SQSTM1) disease and for autosomal-recessive JPD families; incomplete penetrance limits predictive value in classic PDB.
- **Immunization / prophylaxis:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** Human disease (*Homo sapiens*, NCBI:txid9606). Engineered mouse models exist (*Mus musculus*, NCBI:txid10090).
- **Orthologous genes:** mouse *Sqstm1*, *Vcp*, *Tnfrsf11b* (Opg), *Tnfrsf11a* (Rank), *Csf1*, *Optn*.
- **Natural disease in other species:** No well-established spontaneous PDB analog in companion animals in the reviewed literature; the epidemiologic association with cattle density ([PMID: 40408225](https://pubmed.ncbi.nlm.nih.gov/40408225/)) is ecological, not evidence of a natural animal disease. Prior pet ownership (dogs/cats) was exonerated as a risk factor ([PMID: 2376461](https://pubmed.ncbi.nlm.nih.gov/2376461/)).
- **Comparative biology:** The RANK–RANKL–OPG axis and p62/autophagy machinery are evolutionarily conserved, underpinning the translational validity of mouse models.
- **Zoonotic potential:** None demonstrated; the paramyxovirus/zoonosis hypotheses remain unproven (Section 5).

---

## Section 15 — Model Organisms

- **P394L SQSTM1 knock-in mouse** (mammalian; equivalent to human p.P392L) — the key model. Heterozygotes develop focal pagetic-like lesions in 77% and homozygotes in 95% by 12 months vs 0% in wild-type (P<0.001), with enlarged multinucleated osteoclasts containing nuclear inclusions and increased RANKL sensitivity: "mice with a proline to leucine mutation at codon 394 of mouse sqstm1 (P394L) … develop a bone disorder with remarkable similarity to PDB" ([PMID: 21515589](https://pubmed.ncbi.nlm.nih.gov/21515589/)). This model also demonstrated that zoledronic acid prevents pagetic-like lesions and accelerated bone loss ([PMID: 30154079](https://pubmed.ncbi.nlm.nih.gov/30154079/)).
- **Phenotype recapitulation:** Excellent for the focal osteolytic/mixed lesions, giant osteoclasts, RANKL hypersensitivity, and autophagy dysregulation.
- **Limitations:** Requires the germline mutation plus aging; incomplete recapitulation of the human environmental trigger and of extensive polyostotic deforming disease; does not model osteosarcoma.
- **In-vitro systems:** Patient-derived and mutant osteoclast precursor cultures show increased RANKL sensitivity, giant osteoclast formation, and elevated SQSTM1/ATG5/LC3 ([PMID: 21515589](https://pubmed.ncbi.nlm.nih.gov/21515589/)).
- **Resources:** MGI (mouse), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
   GENETIC PREDISPOSITION                         ENVIRONMENTAL TRIGGER
  ┌──────────────────────────┐                   ┌──────────────────────┐
  │ SQSTM1/p62 UBA mut(P392L) │                   │ Unknown, declining    │
  │ ZNF687, PFN1, VCP         │   +               │ (?paramyxovirus, coal │
  │ Risk loci: RANK, OPTN,    │                   │  smoke, rural/cattle) │
  │ CSF1, DCSTAMP, PML, RIN3, │                   └──────────┬───────────┘
  │ NUP205                    │                              │
  └───────────┬──────────────┘                              │
              └──────────────┬───────────────────────────────┘
                             ▼
        Osteoclast precursor HYPERSENSITIVITY to RANKL
        + dysregulated NF-κB signaling + autophagy (↑SQSTM1/ATG5/LC3)
                             ▼
        GIANT, hypernucleated, hyperactive OSTEOCLASTS (nuclear inclusions)
                             ▼
        Focal intense BONE RESORPTION (osteolytic phase)
                             ▼
        Compensatory DISORGANIZED OSTEOBLASTIC bone formation
                             ▼
        Expanded, weak, hypervascular "MOSAIC" bone (woven + lamellar)
                             ▼
   ┌─────────────┬───────────────┬────────────┬─────────────┬────────────┐
  Pain        Deformity       Fracture      Deafness     2° Osteoarthritis
                                                    └── Rare: OSTEOSARCOMA (~0.7–1%)
```

**Upstream vs downstream:** SQSTM1/p62 dysfunction and RANK–RANKL–OPG imbalance are the most upstream molecular events; the osteoclast is the central effector; osteoblastic overactivity and mosaic bone are downstream consequences. Juvenile Paget's disease (OPG loss → unopposed RANKL) is a "natural experiment" that isolates the RANK–RANKL–OPG limb and confirms its centrality (Finding F008).

---

## Evidence Base

| PMID | How it supports / challenges findings |
|---|---|
| [21515589](https://pubmed.ncbi.nlm.nih.gov/21515589/) | P394L knock-in mouse recapitulates PDB; establishes causal role of UBA mutation and autophagy dysregulation (F001, F009) |
| [37180975](https://pubmed.ncbi.nlm.nih.gov/37180975/) | SQSTM1 as most frequent genetic cause; UBA mutations linked to severity (F001) |
| [33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/) | Declining UK incidence → changing environmental trigger (F002) |
| [40408225](https://pubmed.ncbi.nlm.nih.gov/40408225/) | Rural livestock (cattle) association; environmental contribution (F002) |
| [21638319](https://pubmed.ncbi.nlm.nih.gov/21638319/) | Durable remission from single zoledronic acid infusion (F003) |
| [28176386](https://pubmed.ncbi.nlm.nih.gov/28176386/) | PRISM-EZ: intensive therapy gives no QoL/pain/fracture benefit (F003) |
| [17550323](https://pubmed.ncbi.nlm.nih.gov/17550323/) | Paget sarcoma histology (88% osteosarcoma) and 10% 5-yr survival (F004) |
| [1451058](https://pubmed.ncbi.nlm.nih.gov/1451058/) | 0.7% malignant transformation incidence (F004) |
| [40037468](https://pubmed.ncbi.nlm.nih.gov/40037468/) | VCP-MSP/IBMPFD — syndromic PDB (F005) |
| [33145792](https://pubmed.ncbi.nlm.nih.gov/33145792/) | Shared stress-granule/autophagy defect across MSP genes (F005) |
| [21623375](https://pubmed.ncbi.nlm.nih.gov/21623375/) | Seven GWAS loci; ~13% familial risk (F006) |
| [31574000](https://pubmed.ncbi.nlm.nih.gov/31574000/) | Diagnostic workup + zoledronic acid first-line (F007) |
| [32803929](https://pubmed.ncbi.nlm.nih.gov/32803929/) | Radiography + ALP + bone scan algorithm (F007) |
| [32298837](https://pubmed.ncbi.nlm.nih.gov/32298837/) | OPG (TNFRSF11B) loss causes JPD; SP7 mutation (F008) |
| [25108083](https://pubmed.ncbi.nlm.nih.gov/25108083/) | OPG genotype–phenotype correlation in JPD (F008) |
| [33768371](https://pubmed.ncbi.nlm.nih.gov/33768371/) | Osteoclast as central effector cell (F009) |
| [3701300](https://pubmed.ncbi.nlm.nih.gov/3701300/) / [1805546](https://pubmed.ncbi.nlm.nih.gov/1805546/) / [28361207](https://pubmed.ncbi.nlm.nih.gov/28361207/) / [2376461](https://pubmed.ncbi.nlm.nih.gov/2376461/) | Conflicting/negative evidence on the paramyxovirus hypothesis |

---

## Limitations and Knowledge Gaps

1. **The environmental trigger is unidentified.** Declining incidence strongly implies one, but coal-smoke, paramyxovirus, and cattle-exposure hypotheses are unconfirmed and partly contradicted.
2. **Genotype–phenotype gaps.** SQSTM1 and the seven GWAS loci explain only a minority of heritability; many familial cases are unexplained ([PMID: 41024681](https://pubmed.ncbi.nlm.nih.gov/41024681/)).
3. **Epigenetics.** No robust disease-specific DNA-methylation/histone dataset was identified.
4. **Treatment paradox.** Excellent biochemical control does not translate into fewer fractures or better QoL (PRISM-EZ), leaving the optimal treatment goal (biochemical vs symptomatic) unresolved.
5. **Sarcoma risk stratification.** No reliable biomarker predicts which patients will undergo malignant transformation; surveillance guidelines are underdeveloped ([PMID: 42359209](https://pubmed.ncbi.nlm.nih.gov/42359209/)).
6. **Modern data are cohort/registry-based**, subject to referral and ascertainment bias; SEER-type survival data for classic PDB are limited.

---

## Proposed Follow-up Experiments / Actions

1. **Trigger identification:** Metagenomic/16S and viral-capture sequencing of active pagetic bone vs controls, paired with geospatial exposure analysis (cattle density, historical coal use) to test environmental hypotheses definitively.
2. **Heritability completion:** Large multi-ancestry GWAS + WGS/burden testing in SQSTM1-negative families to find the missing causal genes.
3. **Epigenomic profiling:** ATAC-seq/WGBS/ChIP-seq of pagetic vs normal osteoclasts to map disease-specific regulatory changes.
4. **Randomized trial of a symptom-guided vs biochemical-target treatment strategy** with fracture, deformity progression, deafness, and validated QoL endpoints (extending PRISM-EZ).
5. **Sarcoma biomarker discovery:** Longitudinal imaging + circulating tumor DNA/somatic mutation surveillance in high-burden pagetic bone to enable early detection.
6. **Mechanistic dissection in models:** Cross P394L-Sqstm1 mice onto RANK/OPG-modified backgrounds and test autophagy modulators to define the causal hierarchy and identify targeted (non-bisphosphonate) therapies.

---

*Report compiled from 9 confirmed findings and 39 primary papers over 5 investigation iterations. Evidence source types are indicated throughout: human clinical/registry, model organism (P394L mouse), in-vitro osteoclast, and computational/GWAS.*


## Artifacts

- [OpenScientist final report](Paget_Disease_of_Bone-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Paget_Disease_of_Bone-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 34 |
| On topic | 24 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:38963497` *(abstract only)*: "pathogenic mutations frequently found at the interface between the NTD domain and D1 ATPase domain … cause malfunction of VCP"
  - closest text in source: "Pathogenic mutations frequently found at the interface between the NTD domain and D1 ATPase domain have been shown to cause malfunction of VCP, leading to degenerative disorders including the inclusion body myopathy associated with Paget disease of bone and frontotemporal dementia (IBMPFD), amyotrophic lateral sclerosis (ALS), and cancers"
- `PMID:33768371` *(abstract only)*: "Osteoimmunology and Osteoclast Pathology"
  - Text part not found as substring: 'Osteoimmunology and Osteoclast Pathology' (note: only abstract available for PMID:33768371, full text may contain this excerpt)
- `PMID:21515589` *(abstract only)*: "mice with a proline to leucine mutation at codon 394 of mouse sqstm1 (P394L) … develop a bone disorder with remarkable similarity to PDB"
  - closest text in source: "Here we show that mice with a proline to leucine mutation at codon 394 of mouse sqstm1 (P394L), equivalent to the P392L SQSTM1 mutation in humans, develop a bone disorder with remarkable similarity to PDB"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 12 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002750` (1 mention) - the report calls it "Abnormal long bone morphology"; HP calls it **Delayed skeletal maturation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003155` (1 mention) - the report calls it "Elevated circulating ALP"; HP calls it **Elevated circulating alkaline phosphatase concentration**, and lists "Elevated ALP" among its other names
- `GO:0043123` (1 mention) - the report calls it "positive regulation of canonical NF-κB signal transduction"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**
- `GO:0002446` (1 mention) - the report calls it "neutrophil/myeloid-lineage regulation"; GO calls it **neutrophil mediated immunity**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.