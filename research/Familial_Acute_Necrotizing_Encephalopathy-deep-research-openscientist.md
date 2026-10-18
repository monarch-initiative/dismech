---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T01:39:33.177546'
end_time: '2026-10-15T02:03:59.741822'
duration_seconds: 1466.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Acute Necrotizing Encephalopathy
  mondo_id: MONDO:0011953
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
citation_count: 19
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000955
    reported_labels:
    - Primary organ:** brain
    ontology_label: brain
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Acute_Necrotizing_Encephalopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Acute_Necrotizing_Encephalopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Acute Necrotizing Encephalopathy
- **MONDO ID:** MONDO:0011953 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Acute Necrotizing Encephalopathy** covering all of the
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

# Familial Acute Necrotizing Encephalopathy (ANE1): A Comprehensive Disease Report

**Disease:** Familial Acute Necrotizing Encephalopathy
**MONDO ID:** MONDO:0011953 | **OMIM:** 608033 | **Category:** Mendelian (autosomal-dominant, incompletely penetrant)
**Causal gene:** *RANBP2* (Nup358), HGNC:9848, NCBI Gene 5903, chromosome 2q13

---

## Summary

Familial acute necrotizing encephalopathy (ANE1) is a rare, autosomal-dominant, incompletely penetrant predisposition to a fulminant post-infectious brain injury. It is caused by heterozygous missense variants in *RANBP2* (RAN-binding protein 2 / Nup358), the largest nucleoporin of the nuclear pore complex, with a recurrent mutational hotspot at p.Thr585Met (c.1880C>T). The disorder is unmasked when an affected individual — typically a previously healthy young child (median onset ~24 months) — contracts a common febrile viral infection such as influenza A/B, human herpesvirus-6 (HHV-6), parainfluenza, respiratory syncytial virus (RSV), or SARS-CoV-2. The infection triggers a systemic hyperinflammatory ("cytokine storm") response that drives blood–brain-barrier breakdown and produces the disease's hallmark: multiple bilaterally **symmetric** necrotic lesions, most characteristically in the thalami, plus the brainstem tegmentum, external capsules, insular cortices, periventricular white matter, and cerebellum.

The mechanistic model connects two arms of *RANBP2* biology: (1) its canonical roles in nucleocytoplasmic transport and SUMOylation, and (2) its non-canonical role in central nervous system (CNS) energy metabolism, where RanBP2 binds hexokinase I ("the pacemaker of glycolysis") and the mitochondrial metallochaperone Cox11. A mouse model demonstrated that *RanBP2* haploinsufficiency selectively lowers hexokinase I and ATP levels in the CNS, providing a biological rationale for the brain's vulnerability. On top of this metabolic predisposition, the infection-driven cytokine storm (IL-6, TNF-α, hyperferritinemia) produces endothelial activation and vasogenic/cytotoxic edema with petechial hemorrhage ("dysoria"), culminating in symmetric thalamic necrosis.

ANE1 carries high morbidity and mortality (~30–40% mortality in some cohorts; frequent severe neurologic sequelae in survivors). Diagnosis rests on the characteristic symmetric thalamic MRI signature combined with *RANBP2* sequencing and a supportive laboratory profile (elevated CSF protein without pleocytosis, elevated transaminases/CPK, thrombocytopenia, hyperferritinemia, no hyperammonemia). There is no approved disease-specific therapy; management combines intensive supportive care with early immunomodulation (high-dose corticosteroids, IVIG, and IL-6 blockade with tocilizumab). Prophylactic pulse steroids during febrile infections in known carriers, and influenza vaccination, are emerging preventive strategies. Notably, ~19% of familial/recurrent cases lack a *RANBP2* variant, indicating locus heterogeneity and additional susceptibility loci still to be discovered.

---

## Key Findings

### Finding 1 — ANE1 is caused by dominant *RANBP2* missense mutations, most commonly p.Thr585Met

The landmark study by Neilson et al. (2009) mapped a 7-Mb ANE1 susceptibility locus in a family segregating recurrent ANE as an incompletely penetrant, autosomal-dominant trait, and found that all affected individuals and obligate carriers were heterozygous for the missense variant c.1880C>T, p.Thr585Met in *RANBP2*. As the authors state: *"We now report that all affected individuals and obligate carriers in this family are heterozygous for a missense mutation (c.1880C-->T, p.Thr585Met) in the gene encoding the nuclear pore protein Ran Binding Protein 2 (RANBP2)"* ([PMID: 19118815](https://pubmed.ncbi.nlm.nih.gov/19118815/)). The same mutation recurred widely: *"Patients from 9 of 15 additional kindreds with familial or recurrent ANE had the identical mutation. It arose de novo in two families"* — establishing p.Thr585Met as a true mutational hotspot that can also arise de novo.

Allelic heterogeneity exists. Reported pathogenic variants beyond the p.Thr585Met hotspot include **p.Trp681Cys** (a de novo variant causing recurrent ANE), **p.Glu3014Gly** (c.9041A>G, identified in a four-generation Chinese family: *"A novel missense variation, c.9041A > G, p.(Glu3014Gly) in RANBP2 was identified in this family"* — [PMID: 35348941](https://pubmed.ncbi.nlm.nih.gov/35348941/)), and p.Thr585Met reported co-occurring with a *CPT2* thermolabile modifier in the first Japanese case.

- **Variant type:** missense (point mutations)
- **Classification (ACMG/AMP):** pathogenic / likely pathogenic for the recurrent variants
- **Origin:** germline (inherited or de novo)
- **HGNC:** RANBP2 (HGNC:9848); **OMIM gene:** 601181; **OMIM phenotype (ANE1):** 608033

### Finding 2 — ANE1 is triggered by common viral febrile infections and presents with bilateral symmetric thalamic lesions

ANE is a rapidly progressive encephalopathy in previously healthy children following common viral infections. Neilson et al. frame it precisely: *"Acute necrotizing encephalopathy (ANE) is a rapidly progressive encephalopathy that can occur in otherwise healthy children after common viral infections such as influenza and parainfluenza"* ([PMID: 19118815](https://pubmed.ncbi.nlm.nih.gov/19118815/)). The clinical episode follows a stereotyped sequence: a viral prodrome with fever → rapid deterioration of consciousness, seizures, and focal deficits → coma. In the familial (ANE1) form, episodes can **recur** with each new infection.

The neuroimaging signature is diagnostic. In an ANE1 case: *"Brain magnetic resonance imaging (MRI) showed a characteristic involvement of the bilateral thalami, external capsules, insular cortices, and brainstem, suggesting ANE"* ([PMID: 34059398](https://pubmed.ncbi.nlm.nih.gov/34059398/)). The lesions are symmetric and multifocal, affecting both gray and white matter: *"symmetric multifocal brain lesions are seen in the bilateral thalami as well as other characteristic regions, involving both gray and white matter"* ([PMID: 32426208](https://pubmed.ncbi.nlm.nih.gov/32426208/)). Documented viral triggers across case reports include influenza A (including H1N1), influenza B, HHV-6/HHV-7, parainfluenza, RSV, varicella zoster, dengue, and SARS-CoV-2.

### Finding 3 — Prognosis is predicted by the ANE Severity Score, brainstem involvement, and hyperferritinemia; early steroids improve outcome

The **ANE Severity Score (ANE-SS)** stratifies risk on a 0–9 scale: 3 points for shock, 2 for brainstem lesions, 2 for age >48 months, 1 for platelet count <100,000/μL, and 1 for CSF protein >60 mg/dL, yielding low (0–1), medium (2–4), and high (5–9) risk strata ([PMID: 24931733](https://pubmed.ncbi.nlm.nih.gov/24931733/)).

Hyperferritinemia — a marker of the underlying cytokine storm — is a key outcome predictor. Lee et al. (2024, n=29) found that *"ferritin, aspartate aminotransferase (AST), and ANE severity score (ANE-SS) were the predictors associated with outcomes"* ([PMID: 38295717](https://pubmed.ncbi.nlm.nih.gov/38295717/)), with 69% of patients having poor neurological outcomes; thresholds of ferritin >1823 ng/mL, AST >78 U/L, and ANE-SS >4.5 predicted poor outcome, and higher ferritin/ANE-SS correlated with brainstem involvement. A Malaysian cohort (n=13) reported 38.5% mortality with 5 brainstem deaths, and all survivors in a vegetative state or with severe disability at discharge ([PMID: 33358123](https://pubmed.ncbi.nlm.nih.gov/33358123/)). Critically, *"Early treatment with high dose steroids is associated with a more favorable outcome"* ([PMID: 32426208](https://pubmed.ncbi.nlm.nih.gov/32426208/)), especially in patients without brainstem involvement.

| ANE-SS component | Points |
|---|---|
| Shock | 3 |
| Brainstem lesions | 2 |
| Age >48 months | 2 |
| Platelets <100,000/μL | 1 |
| CSF protein >60 mg/dL | 1 |
| **Risk strata** | Low 0–1 · Medium 2–4 · High 5–9 |

### Finding 4 — Pathophysiology: *RANBP2* variant + viral fever → cytokine storm → BBB breakdown → symmetric thalamic necrosis

The proposed causal chain integrates genetics, immunology, and tissue pathology. The original neuropathologic description of ANE emphasized blood–brain-barrier failure: *"Both the gray and white matter are involved, with neuropathological evidence of local breakdown of the blood-brain barrier (dysoria)"* ([PMID: 9105653](https://pubmed.ncbi.nlm.nih.gov/9105653/)). The RANBP2-specific mechanisms remain only partially demonstrated; Levine et al. enumerate several non-mutually-exclusive hypotheses: *"There are several non-mutually exclusive hypotheses suggesting possible etiologies for this phenotype based on the many functions of RANBP2 within the cell. These include dysfunctions in nucleocytoplasmic trafficking and intracellular metabolic regulation, as well as cytokine storm, and abnormal distribution of mitochondria"* ([PMID: 32426208](https://pubmed.ncbi.nlm.nih.gov/32426208/)).

Evidence for the cytokine-storm step comes from severe pediatric viral encephalopathy, where *"Serum concentrations of cytokines/chemokines including interleukin 6 and tumor necrosis factor-α were significantly higher within 24 hours of onset than for controls"* ([PMID: 41714597](https://pubmed.ncbi.nlm.nih.gov/41714597/)).

### Finding 5 — Epidemiology: rare pediatric disorder; sporadic form predominant in East Asia; familial ANE1 very rare

ANE of childhood was first established as a disease entity predominantly affecting infants and young children in Japan and Taiwan: *"This disease predominantly affects infants and young children living in Japan and Taiwan, and manifests itself as acute encephalopathy following viral infections"* ([PMID: 9105653](https://pubmed.ncbi.nlm.nih.gov/9105653/)). Importantly, the geographic distribution of the familial (RANBP2-associated) form differs from the sporadic form: *"Although sporadic ANE predominantly affects Asian children, ANE1 is very rare in east Asia"* ([PMID: 34059398](https://pubmed.ncbi.nlm.nih.gov/34059398/)). The familial form has been reported across European, North American, Chinese, and (first in 2021) Japanese kindreds. No precise prevalence/incidence figures exist; ANE is classified as a rare disease (Orphanet).

### Finding 6 — RANBP2/Nup358 is a multidomain nucleoporin that binds hexokinase I and Cox11; haploinsufficiency lowers CNS ATP (mouse model)

RANBP2 (Nup358, ~358 kDa) is the largest nucleoporin, forming the cytoplasmic filaments of the nuclear pore complex and regulating nucleocytoplasmic transport: *"RANBP2 (also known as Nup358) is the largest nucleoporin of the nuclear pore complex (NPC), where it constitutes the main component of the cytoplasmic filaments and regulates nucleocytoplasmic transport"* ([PMID: 40976348](https://pubmed.ncbi.nlm.nih.gov/40976348/)). Its domains include a zinc finger, four Ran-binding domains, an E3 SUMO ligase domain, and a cyclophilin-like domain; it localizes to the nuclear envelope, annulate lamellae, mitochondria–ER junctions, and kinetochores.

The metabolic link is decisive for understanding CNS vulnerability. Aslanukov et al. showed that *"RanBP2 associates in vitro and in vivo and colocalizes with the mitochondrial metallochaperone, Cox11, and the pacemaker of glycolysis, hexokinase type I (HKI) via its leucine-rich domain"* and, critically, that *"haploinsufficiency of RanBP2 in an inbred strain causes a pronounced decrease of HKI and ATP levels selectively in the central nervous system"* ([PMID: 17069463](https://pubmed.ncbi.nlm.nih.gov/17069463/)). This provides a mechanistic basis for why the brain — and energy-demanding structures such as the thalamus — are selectively vulnerable.

### Finding 7 — Marked intrafamilial phenotypic variability; prophylactic pulse steroids may prevent recurrences

Alrifai et al. (2026) reported three siblings sharing the identical pathogenic *RANBP2* variant but with markedly divergent courses — one progressed to brain death with influenza A, one responded to corticosteroids with mild residual cognitive dysfunction, and a third remained neurologically intact despite recurrent infections: *"Despite sharing the same genotype, the clinical spectrum was markedly variable"* ([PMID: 42407393](https://pubmed.ncbi.nlm.nih.gov/42407393/)). This illustrates **variable expressivity** and **incomplete penetrance**. Importantly, the surviving siblings received a preventive strategy: *"The surviving cases were given a preventive treatment plan with pulse steroids during influenza infections. At 2 years of follow-up, they still have no new episodes of encephalopathy"* ([PMID: 42407393](https://pubmed.ncbi.nlm.nih.gov/42407393/)) — proof-of-concept for anti-inflammatory prophylaxis during febrile illness.

### Finding 8 — Systematic review (n=92): demographics and vaccine safety

Cavaliere et al. (2026) conducted a PRISMA systematic review of familial/recurrent/genetic ANE: *"Ninety-two patients were analysed (91 literature cases and 1 novel case) (median onset age 24 months; 62% male; RANBP2 mutations in 81% of tested individuals)"* ([PMID: 42385467](https://pubmed.ncbi.nlm.nih.gov/42385467/)). Of 142 clinical events, 108 were definite/probable ANE and 34 were atypical (25 infection-triggered encephalopathy without bithalamic involvement; 9 other acute neurological events); in 13% of patients, atypical episodes preceded a subsequent ANE event. Regarding vaccination safety: *"5/20 resumed vaccination post-ANE (no vaccine-related relapses over a median follow-up of 19 months)"* ([PMID: 42385467](https://pubmed.ncbi.nlm.nih.gov/42385467/)).

### Finding 9 — Diagnosis rests on characteristic MRI plus *RANBP2* sequencing; key labs distinguish from Reye syndrome

The diagnosis is clinical-radiological, supported by a characteristic laboratory profile. A classic case description notes: *"His serum CPK was markedly elevated, but there was no hyperammonaemia or hypoglycaemia. His CSF showed an increased protein level, but the cell count and glucose level were normal"* ([PMID: 10834515](https://pubmed.ncbi.nlm.nih.gov/10834515/)) — the elevated CSF protein without pleocytosis and the absence of hyperammonemia/hypoglycemia distinguish ANE from Reye syndrome. The para-infectious (non-neuroinvasive) nature is supported by PCR-negative CSF: *"Antibody production without detectable levels of influenza virus in cerebrospinal fluid suggests that virus infection occurred, but the virus did not replicate in sufficient numbers in his central nervous system"* ([PMID: 10834515](https://pubmed.ncbi.nlm.nih.gov/10834515/)). Molecular confirmation of ANE1 is by *RANBP2* single-gene sequencing or multigene panel/WES. A rapid bedside functional assay for RANBP2-ANE1 has been proposed ([PMID: 38046586](https://pubmed.ncbi.nlm.nih.gov/38046586/)).

### Finding 10 — ANE1 is a gene–environment disorder with modifiers and locus heterogeneity

ANE1 is a paradigmatic gene–environment interaction: it requires both a genetic predisposition (*RANBP2* variant) and an environmental trigger (febrile viral infection), with incomplete penetrance. Ohashi et al. reported a modifier: a patient carrying both *RANBP2* p.Thr585Met and a thermolabile *CPT2* polymorphism — *"The patient also harbored a CPT2 polymorphism that is linked to acute encephalopathy in Japanese patients. Thus, he had a genetic background with two susceptibility variants for acute encephalopathy, RANBP2 (frequent in the Caucasians), and CPT2 (frequent in the Japa[nese])"* ([PMID: 34059398](https://pubmed.ncbi.nlm.nih.gov/34059398/)). Locus heterogeneity is established by López-Laso et al., who described a familial/recurrent ANE family **without** *RANBP2* mutations: *"Mutations in RANBP2 are not the sole susceptibility alleles for familial or recurrent ANE"* ([PMID: 19643689](https://pubmed.ncbi.nlm.nih.gov/19643689/)) — consistent with the systematic review's finding of RANBP2 variants in only 81% of tested cases.

### Finding 11 — Management is supportive plus early immunomodulation; prophylactic steroids in carriers are emerging prevention

No RANBP2-targeted or disease-specific approved therapy exists. Acute management combines ICU-level supportive care with immunomodulation. For SARS-CoV-2-related ANE: *"Treatment with a combination of early steroid therapy, intravenous immunoglobulin therapy, and targeted interleukin 6 (IL-6) blockade yielded good neurological improvements"* ([PMID: 36529001](https://pubmed.ncbi.nlm.nih.gov/36529001/)). Preventive strategies include prophylactic pulse steroids during infections in carriers ([PMID: 42407393](https://pubmed.ncbi.nlm.nih.gov/42407393/)) and influenza vaccination, which did not provoke relapses ([PMID: 42385467](https://pubmed.ncbi.nlm.nih.gov/42385467/)).

---

## Report by Template Section

### 1. Disease Information
ANE1 is a rare, autosomal-dominant, incompletely penetrant Mendelian predisposition to infection-triggered acute necrotizing encephalopathy. **Identifiers:** MONDO:0011953; OMIM 608033 (phenotype); *RANBP2* gene OMIM 601181; Orphanet (rare disease). **Synonyms:** acute necrotizing encephalopathy type 1; familial/recurrent/genetic acute necrotizing encephalopathy; RANBP2-associated ANE; infection-induced acute encephalopathy 3 (IIAE3). Information is derived from **aggregated disease-level resources** (case reports, kindred studies, and systematic reviews) rather than EHR.

### 2. Etiology
**Primary cause:** heterozygous germline missense variants in *RANBP2* (recurrent p.Thr585Met). **Genetic risk factors:** the causal *RANBP2* variants; modifier/co-susceptibility alleles such as the thermolabile *CPT2* p.Phe352Cys polymorphism ([PMID: 34059398](https://pubmed.ncbi.nlm.nih.gov/34059398/)). **Environmental risk factors:** common febrile viral infections (influenza A/B, HHV-6/7, parainfluenza, RSV, varicella zoster, dengue, SARS-CoV-2); fever/hyperthermia is a key trigger. **Protective factors:** avoidance/mitigation of febrile viral illness (vaccination, antipyresis, antivirals) reduces trigger exposure; no genetic protective alleles are established. **Gene–environment interaction:** disease requires BOTH the genetic predisposition AND an infectious trigger — a canonical GxE disorder with incomplete penetrance ([PMID: 19643689](https://pubmed.ncbi.nlm.nih.gov/19643689/)).

### 3. Phenotypes
Core phenotypes and suggested HPO terms:
- **Acute/recurrent encephalopathy** (HP:0006846 Acute encephalopathy) — rapid deterioration of consciousness; severe; episodic/recurrent with infections.
- **Seizures** (HP:0001250) — common in acute episodes.
- **Fever** (HP:0001945) — prodromal trigger.
- **Coma / reduced consciousness** (HP:0001259) — severe episodes.
- **Ataxia** (HP:0001251), **dysarthria** (HP:0001260), **developmental regression/delay** (HP:0002376) — sequelae.
- **Elevated CSF protein** (HP:0002922), **elevated hepatic transaminases** (HP:0002910), **hyperferritinemia** (HP:0003281), **thrombocytopenia** (HP:0001873), **elevated CPK** (HP:0003236) — laboratory abnormalities.
- **Age of onset:** infancy–early childhood (median 24 months). **Severity:** severe/variable. **Progression:** episodic/relapsing with infections, often with cumulative deficits. **Frequency:** RANBP2 variant in ~81% of tested familial cases. **QoL impact:** survivors frequently have severe disability or vegetative state.

### 4. Genetic/Molecular Information
**Causal gene:** *RANBP2* (HGNC:9848; OMIM 601181; NCBI Gene 5903). **Pathogenic variants:** p.Thr585Met (c.1880C>T, recurrent hotspot, pathogenic); p.Trp681Cys (de novo); p.Glu3014Gly (c.9041A>G). **Variant type:** missense. **Classification:** pathogenic/likely pathogenic (ACMG/AMP). **Allele frequency:** extremely rare in gnomAD (private/ultra-rare). **Origin:** germline (inherited or de novo). **Functional consequence:** altered function of a multidomain nucleoporin affecting nucleocytoplasmic transport, SUMOylation, and CNS energy metabolism (HKI/ATP). **Modifier genes:** *CPT2* thermolabile polymorphism. **Chromosomal abnormalities:** none characteristic; the 2q12-13 region harboring *RANBP2* is structurally dynamic with RGPD paralogs ([PMID: 37795679](https://pubmed.ncbi.nlm.nih.gov/37795679/)).

### 5. Environmental Information
**Environmental/infectious factors:** viral febrile infections are the essential trigger — influenza A/B (including H1N1), HHV-6/HHV-7, parainfluenza, RSV, varicella zoster, dengue, and SARS-CoV-2. **Lifestyle factors:** not established; fever itself is the operative exposure. The para-infectious nature (PCR-negative CSF) indicates the brain injury is immune/inflammatory rather than directly virus-invasive.

### 6. Mechanism / Pathophysiology — Ordered Causal Chain

```
1. Germline heterozygous RANBP2 missense variant (e.g., p.Thr585Met)
      → creates an incompletely penetrant predisposition [demonstrated: genetics]
2. Baseline reduced RANBP2 function
      → lowers hexokinase I and ATP selectively in the CNS
        [demonstrated in RanBP2+/- mouse; inferred for human variants]
3. A common febrile viral infection (influenza, HHV-6, SARS-CoV-2)
      → triggers a systemic hyperinflammatory response [demonstrated: clinical]
4. Excessive pro-inflammatory cytokines (IL-6, TNF-α; hyperferritinemia)
      → "cytokine storm" [demonstrated: serum cytokines elevated <24h]
5. Cytokines cause endothelial activation + local BBB breakdown ("dysoria")
      → vasogenic/cytotoxic edema + petechial hemorrhage [demonstrated: neuropathology]
                         │
                         ├─(branch A: metabolic) energy failure in
                         │   high-demand gray matter (thalamus, brainstem)
                         │
                         └─(branch B: inflammatory) direct cytokine-mediated
                             endothelial/parenchymal injury
6. Multifocal SYMMETRIC necrosis → bilateral thalami, brainstem tegmentum,
   external capsules, insular cortex, periventricular white matter, cerebellum
      → coma, seizures, focal deficits; recurrence with each infection
```

- **Molecular pathways:** cytokine signaling (IL-6/JAK-STAT, TNF-α); nucleocytoplasmic transport; SUMOylation (RANBP2 E3 SUMO ligase); glycolysis (hexokinase I).
- **Cellular processes:** inflammation (GO:0006954), necrosis (GO:0070265), blood–brain-barrier disruption, apoptosis (GO:0006915).
- **Protein dysfunction:** altered function of the Nup358 cytoplasmic-filament nucleoporin.
- **Metabolic changes:** reduced CNS hexokinase I and ATP (GO:0006006 glucose metabolic process; GO:0006754 ATP biosynthetic process).
- **Immune involvement:** hyperinflammatory cytokine storm (not autoimmune, not immunodeficiency).
- **Tissue damage:** BBB breakdown (dysoria), vasogenic/cytotoxic edema, petechial hemorrhage, necrosis.
- **Cell types (CL):** vascular endothelial cells (CL:0000115), neurons (CL:0000540), astrocytes (CL:0000127), microglia (CL:0000129).
- **Subcellular (GO CC):** nuclear pore (GO:0005643), cytoplasmic filaments, mitochondrion (GO:0005739), mitochondria–ER junction.

### 7. Anatomical Structures Affected
- **Primary organ:** brain (UBERON:0000955); **body system:** central nervous system.
- **Specific sites (UBERON):** thalamus (UBERON:0001897) — bilateral and symmetric; brainstem/midbrain tegmentum (UBERON:0002298 brainstem); external capsule; insular cortex (UBERON:0002022); periventricular white matter; cerebellum (UBERON:0002037); mammillary bodies, periaqueductal gray, hippocampus (reported in some cases).
- **Lateralization:** bilateral, symmetric — a diagnostic hallmark.
- **Secondary involvement:** rare multiorgan involvement (e.g., acute fulminant myocarditis reported concomitantly).
- **Tissue level:** both gray and white matter; nervous tissue and cerebral vasculature.

### 8. Temporal Development
- **Onset:** pediatric, typically infancy–early childhood (median ~24 months); **pattern:** acute/fulminant, following a viral prodrome by days.
- **Progression:** episodic/relapsing — acute episodes recur with each new febrile infection; within an episode, rapid (hours–days) deterioration to coma.
- **Disease course:** lifelong predisposition; between episodes patients may be stable, but cumulative deficits can accrue.
- **Remission:** acute episodes may partially resolve (imaging shows resolution of swelling with residual cytotoxic edema); prophylactic steroids during infections may prevent new episodes.
- **Critical period:** the first 24–72 hours of a febrile illness is the window for intervention (early steroids/immunomodulation).

### 9. Inheritance and Population
- **Inheritance:** autosomal dominant, **incomplete penetrance**, **variable expressivity** ([PMID: 19118815](https://pubmed.ncbi.nlm.nih.gov/19118815/); [PMID: 42407393](https://pubmed.ncbi.nlm.nih.gov/42407393/)).
- **Penetrance:** incomplete; some carriers never develop ANE despite recurrent infections.
- **De novo / mosaicism:** de novo occurrence documented in ≥2 families; germline mosaicism not specifically reported.
- **Epidemiology:** no precise prevalence/incidence; ultra-rare. Sporadic ANE predominates in East Asian children; familial ANE1 is rare worldwide and very rare in East Asia.
- **Demographics (systematic review, n=92):** median onset 24 months; 62% male; RANBP2 variant in 81% of tested.
- **Founder effect/consanguinity:** no founder effect established; reported in non-consanguineous families.

### 10. Diagnostics
- **Imaging (definitive):** brain MRI showing bilateral **symmetric** lesions of thalami, brainstem tegmentum, external capsules, insular cortex, periventricular white matter, cerebellum; thalamic "tricolour"/laminar/concentric pattern on ADC maps.
- **Laboratory:** CSF elevated protein **without** pleocytosis; elevated serum transaminases (AST/ALT) and CPK; thrombocytopenia; hyperferritinemia; **no** hyperammonemia or hypoglycemia (distinguishes from Reye syndrome); CSF typically virus-PCR-negative.
- **Genetic testing:** *RANBP2* single-gene sequencing, multigene encephalopathy panels, or WES/WGS; a rapid bedside functional assay has been proposed ([PMID: 38046586](https://pubmed.ncbi.nlm.nih.gov/38046586/)).
- **Differential diagnosis:** sporadic ANE; acute disseminated encephalomyelitis (ADEM); Leigh/MELAS mitochondrial disease; Wernicke encephalopathy; acute bilateral striatal necrosis; Reye syndrome; acute encephalopathy with biphasic seizures and late reduced diffusion (AESD); dengue necrotizing encephalopathy-like encephalitis.
- **Screening:** cascade genetic testing of at-risk relatives in known kindreds; prenatal/pre-symptomatic testing feasible once a familial variant is identified.

### 11. Outcome / Prognosis
- **Mortality:** high — ~38.5% in the Malaysian cohort (5 brainstem deaths); ~30–40% range reported; 69% poor neurological outcome in a 29-patient series.
- **Morbidity:** survivors frequently have severe disability or vegetative state at discharge, with variable later recovery.
- **Prognostic factors:** ANE-SS (>4.5), brainstem involvement, shock, hyperferritinemia (>1823 ng/mL), AST (>78 U/L), low GCS at presentation, higher MRI scores.
- **Recovery:** partial recovery possible with early immunomodulation, particularly when the brainstem is spared; ≥12-month follow-up recommended for accurate prognostication.

### 12. Treatment
No disease-specific approved therapy. **Acute:** intensive supportive/ICU care + immunomodulation:
- High-dose IV corticosteroids (earliest treatment associated with better outcome) — NCIT: Corticosteroid Therapy.
- IVIG (intravenous immunoglobulin).
- IL-6 blockade (tocilizumab) — effective in SARS-CoV-2-related ANE ([PMID: 36529001](https://pubmed.ncbi.nlm.nih.gov/36529001/)).
- Trigger-directed therapy: oseltamivir + antipyresis for influenza.
- Severe multiorgan cases: ECMO support reported.
**Prevention in carriers:** prophylactic pulse steroids during febrile infections ([PMID: 42407393](https://pubmed.ncbi.nlm.nih.gov/42407393/)); influenza vaccination.
**Pharmacogenomics / targeted / gene / cell / RNA therapies:** none established.

### 13. Prevention
- **Primary:** influenza vaccination (safe with respect to ANE relapse — [PMID: 42385467](https://pubmed.ncbi.nlm.nih.gov/42385467/)); avoidance/early treatment of febrile viral illness.
- **Secondary:** early recognition and prompt immunomodulation during febrile illness in known carriers; prophylactic pulse steroids.
- **Tertiary:** rehabilitation; management of neurologic sequelae.
- **Genetic counseling:** autosomal-dominant transmission with incomplete penetrance and variable expressivity must be conveyed; cascade testing in kindreds.

### 14. Other Species / Natural Disease
- **Taxonomy / orthologs:** *Ranbp2* mouse ortholog (*Mus musculus*, NCBI:txid10090). No naturally occurring companion-animal/wildlife equivalent of ANE1 is established (not reported in OMIA).
- **Comparative biology:** RANBP2 is conserved across metazoans; the primate-specific RGPD paralog family arose via duplication during ape evolution ([PMID: 37795679](https://pubmed.ncbi.nlm.nih.gov/37795679/)).
- **Zoonotic potential:** not applicable (the human disorder is a host genetic predisposition, not a transmissible disease).

### 15. Model Organisms
- **Mouse (*Mus musculus*):** *RanBP2*-null mice are embryonic lethal; inbred *RanBP2*(+/-) haploinsufficient mice show selectively decreased CNS hexokinase I and ATP, growth deficits, and impaired glucose catabolism ([PMID: 17069463](https://pubmed.ncbi.nlm.nih.gov/17069463/)) — recapitulating the **metabolic** arm of ANE1.
- **Additional mouse phenotype:** *RanBP2* haploinsufficiency is neuroprotective against light-elicited, age-dependent photoreceptor degeneration and alters retinal free-fatty-acid metabolism ([PMID: 18949001](https://pubmed.ncbi.nlm.nih.gov/18949001/)).
- **Model types available:** knockout (lethal), haploinsufficient/heterozygous. **Limitation:** no mouse model fully reproduces the infection-triggered symmetric thalamic necrosis of human ANE1; the gene–environment (viral-trigger) dimension is not captured.
- **Resources:** MGI (mouse), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

ANE1 is best understood as a **two-hit, gene–environment disorder** superimposed on an underlying **metabolic vulnerability**:

| Layer | Element | Evidence strength |
|---|---|---|
| Predisposition | Germline *RANBP2* variant (p.Thr585Met) | Demonstrated (genetics, [PMID: 19118815](https://pubmed.ncbi.nlm.nih.gov/19118815/)) |
| Baseline vulnerability | Reduced CNS hexokinase I / ATP | Demonstrated in mouse ([PMID: 17069463](https://pubmed.ncbi.nlm.nih.gov/17069463/)); inferred in humans |
| Trigger | Febrile viral infection | Demonstrated (clinical, [PMID: 19118815](https://pubmed.ncbi.nlm.nih.gov/19118815/)) |
| Amplifier | Cytokine storm (IL-6, TNF-α, ferritin) | Demonstrated (serum cytokines, [PMID: 41714597](https://pubmed.ncbi.nlm.nih.gov/41714597/)) |
| Effector | BBB breakdown ("dysoria") | Demonstrated (neuropathology, [PMID: 9105653](https://pubmed.ncbi.nlm.nih.gov/9105653/)) |
| Lesion | Symmetric thalamic/brainstem necrosis | Demonstrated (MRI/pathology) |

The convergence of a metabolic predisposition (why the brain, and specifically energy-hungry deep gray structures) with an inflammatory trigger (why infections, why symmetric and fulminant) explains both the anatomical selectivity and the episodic, infection-linked course. The therapeutic implication follows directly: interrupting the cytokine-storm amplifier early (steroids, IVIG, tocilizumab) and pre-empting it in carriers (prophylactic steroids during fevers) are the rational interventions, and both have preliminary clinical support.

The ~19% of familial cases without a *RANBP2* variant ([PMID: 42385467](https://pubmed.ncbi.nlm.nih.gov/42385467/); [PMID: 19643689](https://pubmed.ncbi.nlm.nih.gov/19643689/)) indicate genetic locus heterogeneity — additional susceptibility genes in the same mechanistic pathway remain to be identified.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [19118815](https://pubmed.ncbi.nlm.nih.gov/19118815/) | Landmark | Identifies *RANBP2* p.Thr585Met as causal; AD, incomplete penetrance; viral trigger |
| [35348941](https://pubmed.ncbi.nlm.nih.gov/35348941/) | Support | Novel p.Glu3014Gly variant — allelic heterogeneity |
| [34059398](https://pubmed.ncbi.nlm.nih.gov/34059398/) | Support | First Japanese ANE1; *CPT2* modifier; MRI signature; geographic contrast |
| [32426208](https://pubmed.ncbi.nlm.nih.gov/32426208/) | Review | Mechanistic hypotheses; symmetric lesions; early steroids beneficial |
| [24931733](https://pubmed.ncbi.nlm.nih.gov/24931733/) | Tool | Defines ANE Severity Score |
| [38295717](https://pubmed.ncbi.nlm.nih.gov/38295717/) | Support | Ferritin/AST/ANE-SS as outcome predictors |
| [9105653](https://pubmed.ncbi.nlm.nih.gov/9105653/) | Foundational | Defines ANE entity; BBB breakdown (dysoria); East Asian predominance |
| [41714597](https://pubmed.ncbi.nlm.nih.gov/41714597/) | Support | IL-6/TNF-α elevated <24h — cytokine storm evidence |
| [17069463](https://pubmed.ncbi.nlm.nih.gov/17069463/) | Mechanism | RanBP2–HKI–Cox11; haploinsufficiency lowers CNS ATP (mouse) |
| [40976348](https://pubmed.ncbi.nlm.nih.gov/40976348/) | Background | RANBP2 identity, domains, localization |
| [42407393](https://pubmed.ncbi.nlm.nih.gov/42407393/) | Support | Variable expressivity in 3 siblings; prophylactic steroids |
| [42385467](https://pubmed.ncbi.nlm.nih.gov/42385467/) | Review | n=92 demographics; RANBP2 in 81%; vaccine safety |
| [10834515](https://pubmed.ncbi.nlm.nih.gov/10834515/) | Support | Lab profile; para-infectious (PCR-negative CSF) |
| [38046586](https://pubmed.ncbi.nlm.nih.gov/38046586/) | Support | Proposed rapid bedside RANBP2-ANE1 diagnostic |
| [19643689](https://pubmed.ncbi.nlm.nih.gov/19643689/) | Support | Locus heterogeneity — RANBP2 not the sole susceptibility allele |
| [36529001](https://pubmed.ncbi.nlm.nih.gov/36529001/) | Support | Steroids + IVIG + tocilizumab effective (SARS-CoV-2 ANE) |
| [33358123](https://pubmed.ncbi.nlm.nih.gov/33358123/) | Support | Malaysian cohort: 38.5% mortality; severe sequelae |
| [37795679](https://pubmed.ncbi.nlm.nih.gov/37795679/) | Background | RANBP2 evolution, RGPD paralogs, disease associations |
| [18949001](https://pubmed.ncbi.nlm.nih.gov/18949001/) | Model | RanBP2 haploinsufficiency effects in mouse retina/metabolism |
| [26923722](https://pubmed.ncbi.nlm.nih.gov/26923722/) | Support | Variable course; novel p.Trp681Cys de novo variant |

---

## Limitations and Knowledge Gaps

1. **No precise epidemiology.** Prevalence and incidence of ANE1 are unknown; evidence is from case reports, kindreds, and a single systematic review (n=92).
2. **Mechanism partly inferred.** The link from human *RANBP2* variants to the metabolic (HKI/ATP) deficit is demonstrated only in mice; direct human tissue evidence is lacking. The exact molecular pathway from variant to cytokine storm remains "elusive."
3. **Locus heterogeneity unresolved.** ~19% of familial/recurrent cases lack a *RANBP2* variant; the additional gene(s) are unidentified.
4. **Treatment evidence is low-grade.** Steroids, IVIG, and tocilizumab are supported by case reports/small series, not randomized trials; one cohort found early immunomodulation did not change outcome, highlighting inconsistency.
5. **Penetrance/expressivity modifiers poorly characterized.** Beyond *CPT2*, genetic and environmental modifiers that determine whether a carrier develops ANE are largely unknown.
6. **No faithful animal model** reproduces the infection-triggered symmetric thalamic necrosis.
7. **Some citation snippets were normalized/approximate** (e.g., PMID 24931733, 35348941, 38046586 flagged during verification), so exact wording should be re-verified against source abstracts.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an infection-challenge model** in *RanBP2* mutant (knock-in p.Thr585Met) mice, challenged with influenza/poly(I:C), to test whether the symmetric thalamic lesion and cytokine storm can be recapitulated and pharmacologically prevented.
2. **Identify the non-RANBP2 loci** in the ~19% of familial cases via WGS/trio sequencing and GeneMatcher collaboration.
3. **Prospective registry + natural history study** to generate true prevalence/incidence, penetrance estimates, and standardized outcomes.
4. **Biomarker study** correlating serial serum IL-6, TNF-α, and ferritin trajectories with ANE-SS and MRI severity to define treatment-response thresholds.
5. **Randomized/adaptive trial** (or structured prospective cohort) of early high-dose steroids ± tocilizumab ± IVIG, stratified by brainstem involvement.
6. **Carrier prophylaxis protocol** formally evaluating prophylactic pulse steroids and influenza vaccination during febrile illness in genotyped carriers.
7. **Functional validation** of the proposed rapid bedside RANBP2-ANE1 assay against genetic gold standard across multiple variants.

---

*Report compiled from 11 confirmed findings and 42 reviewed papers across 5 investigation iterations. Evidence source types span human clinical case reports/cohorts, systematic review, mouse model organism, and in vitro biochemistry.*


## Artifacts

- [OpenScientist final report](Familial_Acute_Necrotizing_Encephalopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Acute_Necrotizing_Encephalopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** brain"; UBERON calls it **brain**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001259` (1 mention) - the report calls it "Coma / reduced consciousness"; HP calls it **Coma**, and lists "Unconsciousness" among its other names
- `HP:0002376` (1 mention) - the report calls it "developmental regression/delay"; HP calls it **Developmental regression**
- `HP:0002922` (1 mention) - the report calls it "Elevated CSF protein"; HP calls it **Increased CSF protein concentration**, and lists "Elevated csf protein" among its other names
- `HP:0002910` (1 mention) - the report calls it "elevated hepatic transaminases"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0003281` (1 mention) - the report calls it "hyperferritinemia"; HP calls it **Increased circulating ferritin concentration**, and lists "Hyperferritinemia" among its other names
- `HP:0003236` (1 mention) - the report calls it "elevated CPK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names
- `GO:0006954` (1 mention) - the report calls it "Cellular processes:** inflammation"; GO calls it **inflammatory response**, and lists "inflammation" among its other names