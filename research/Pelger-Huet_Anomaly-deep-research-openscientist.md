---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-10T16:42:57.246538'
end_time: '2026-09-10T17:42:03.094062'
duration_seconds: 3545.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pelger-Huet Anomaly
  mondo_id: MONDO:0008214
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
citation_count: 32
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 21
  relevance_assessed: 33
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0008214
    reported_labels:
    - MONDO
    ontology_label: Pelger-Huet anomaly
  - term_id: HP:0034236
    reported_labels:
    - abnormal neutrophil morphology
    ontology_label: Apnea of prematurity
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pelger-Huet_Anomaly-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pelger-Huet_Anomaly-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pelger-Huet Anomaly
- **MONDO ID:** MONDO:0008214 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pelger-Huet Anomaly** covering all of the
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

# Pelger-Huët Anomaly (MONDO:0008214): A Comprehensive Disease Characteristics Report

## Summary

**Pelger-Huët anomaly (PHA)** is a benign, autosomal-dominant disorder of neutrophil nuclear morphology (incidence ≈ 1 in 6,000) caused by heterozygous loss-of-function variants in **LBR** (lamin B receptor), an inner nuclear membrane protein on chromosome **1q42.12**. In the heterozygous state, PHA produces the pathognomonic hypolobulated "pince-nez" (bilobed/dumbbell) neutrophil nucleus with dense, coarsely clumped chromatin, but neutrophil innate immune function is essentially preserved and affected individuals are clinically well. The principal clinical hazard is **diagnostic**: PHA mimics a "left shift" (increased band forms) and can trigger unnecessary infection work-ups, while an acquired, morphologically identical "pseudo-PHA" signals myelodysplastic syndrome/leukemia, certain drugs, or radiation.

The disease is best understood as a **gene-dosage / dual-function allelic series**. LBR is a chimeric protein with two independent activities: (1) a **structural** N-terminal domain that tethers peripheral heterochromatin and lamin B to the nuclear envelope — this is required for the reciprocal LBR↑/lamin-A/C↓ remodeling that sculpts the lobulated granulocyte nucleus under transcriptional control of **C/EBPε**; and (2) a **C-terminal sterol Δ14-reductase** enzymatic domain that participates in cholesterol biosynthesis. Heterozygous variants perturb only nuclear shape → benign PHA. Biallelic variants that also abolish the sterol-reductase function produce a graded spectrum of **skeletal dysplasia** (PHA with skeletal anomalies, PHASK; LBR-related spondylometaphyseal dysplasia) culminating in perinatal-lethal **Greenberg dysplasia**. Crucially, an enzymatically redundant paralog, **DHCR14/TM7SF2**, compensates for LBR's sterol-reductase activity, which explains why heterozygous PHA carriers have no cholesterol/skeletal phenotype.

This report consolidates 9 confirmed findings across 44 reviewed papers into a mechanistic and clinical account spanning etiology, phenotype, molecular genetics, pathophysiology (as an ordered causal chain), affected anatomy, temporal course, epidemiology/inheritance, diagnostics, prognosis, treatment, prevention, comparative/veterinary biology, and model organisms. The overarching conclusion: **inherited PHA is a benign trait requiring recognition rather than treatment, but it is the mildest expression of an LBR allelic series whose severe biallelic end is lethal, and it must be distinguished from acquired pseudo-PHA and from LBR-independent genetic causes (NBAS/SOPH, TMEM147, LMBR1L).**

---

## Key Findings

### Finding 1 — PHA is caused by LBR mutations, and allelic dosage determines phenotype severity

Pelger-Huët anomaly is caused by variants in the **LBR** gene (lamin B receptor, chromosome 1q42.12). The zygosity of the LBR lesion determines where a patient falls on a phenotypic spectrum. Heterozygous LBR variants cause benign PHA (**OMIM #169400**); homozygous or compound heterozygous variants cause rhizomelic skeletal dysplasia, with or without PHA (**OMIM #618019**), or perinatal-lethal **Greenberg dysplasia** (**OMIM #215140**). This allelic series is grounded in LBR's biology: the protein has a **structural** function (nuclear segmentation of neutrophils) and an **enzymatic** function (sterol Δ14-reductase in cholesterol biosynthesis).

> "Heterozygous variants in the LBR gene have been associated with Pelger-Huët anomaly (PHA, OMIM #169400), while homozygous or compound heterozygous mutations have been associated with rhizomelic skeletal dysplasia, with or without PHA (OMIM #618019) and Greenberg dysplasia (OMIM #215140)." — [PMID: 41059452](https://pubmed.ncbi.nlm.nih.gov/41059452/)

> "The lamin B receptor (LBR) is an inner nuclear membrane protein with a structural function affecting nuclear segmentation in neutrophils and an enzymatic function as a sterol reductase." — [PMID: 42622427](https://pubmed.ncbi.nlm.nih.gov/42622427/)

### Finding 2 — Heterozygous PHA is a benign autosomal-dominant trait that mimics a left shift

PHA is a rare benign autosomal-dominant anomaly with an incidence of approximately **1 in 6,000**. It does **not** cause neutrophilia, but it can produce a **false increase in band forms** (a pseudo-left-shift), risking misdiagnosis of infection. Neutrophil function is preserved, so carriers are clinically healthy; the anomaly is typically an incidental finding on a blood smear or automated differential.

> "Pelger-Huët anomaly (PHA) is a rare benign autosomal-dominant anomaly with an incidence of ∼1 in 6000. It does not cause neutrophilia, but it can cause a false increase in band forms." — [PMID: 26634137](https://pubmed.ncbi.nlm.nih.gov/26634137/)

### Finding 3 — Neutrophil nuclear shape follows an LBR gene-dosage effect; acquired pseudo-PHA arises in MDS, drugs, and radiation

Quantitative image analysis in 26 subjects carrying 0–3 wild-type LBR alleles showed that **~65% of the variance in neutrophil nuclear segmentation** was explained by the number of wild-type LBR alleles, with a **non-additive, hysteresis-like** dose–response (lower and upper plateaus). This confirms LBR gene dosage as the primary quantitative determinant of nuclear lobulation.

An **acquired ("pseudo") PHA** with identical morphology occurs in three well-documented settings: (1) myeloid malignancy — myelodysplastic syndrome and AML, frequently with chromosome 17p abnormalities such as t(5;17) and t(7;17)/monosomy 17; (2) drugs — mycophenolate mofetil, tacrolimus, colchicine, and other immunosuppressants; and (3) ionizing radiation, in a dose-dependent manner (high-dose 2.98–4.61 Gy-Eq group: 13.0 ± 0.85% PH cells vs lower-dose/controls, p = 0.002).

> "Approximately 65% of the observed phenotypic variance was explainable by the number of LBR wild type alleles. The gene-dosage effect followed a non-additive, hysteresis-like characteristic with lower and upper plateaus." — [PMID: 27684937](https://pubmed.ncbi.nlm.nih.gov/27684937/)

> "eight patients had a pseudo-Pelger-Huët anomaly, which correlated significantly with total monosomy 17" — [PMID: 2340488](https://pubmed.ncbi.nlm.nih.gov/2340488/)

> "The high-dose group (n = 5, 2.98-4.61 Gy-Eq) exhibited 13.0 ± 0.85% PH cells (mean ± SEM) in the neutrophil population compared to 6.8 ± 1.6% in the low-dose group" — [PMID: 25627941](https://pubmed.ncbi.nlm.nih.gov/25627941/)

### Finding 4 — Mechanism: LBR tethers peripheral heterochromatin and is upregulated via C/EBPε during granulopoiesis to sculpt the lobulated nucleus

LBR, together with lamins and LAP2, tethers heterochromatin to the nuclear envelope. During neutrophil differentiation, LBR expression **increases** under the transcriptional control of **C/EBPε** (which binds sites in the Lbr promoter). Loss of LBR blocks morphological nuclear lobulation (producing hyposegmentation) but, in human heterozygous PHA, granulocyte innate function is **preserved**. In complete-null mouse models (Lbr-GT/GT and EML-ic/ic), morphological maturation fails while bacterial killing (e.g., of *S. aureus*) can remain intact — though with total LBR loss, promyelocyte proliferation and the respiratory burst can also be deficient.

> "One tether is constituted by the lamin B receptor (LBR) in mammals" — [PMID: 41735607](https://pubmed.ncbi.nlm.nih.gov/41735607/)

> "Lbr is transcriptionally regulated by C/EBPepsilon. Our findings indicate that the Lbr(GT/GT) mice are a model for Pelger-Huët anomaly and that Lbr, under transcriptional regulation of C/EBPepsilon, is necessary for morphological but not necessarily functional granulocyte maturation." — [PMID: 18621876](https://pubmed.ncbi.nlm.nih.gov/18621876/)

### Finding 5 — Model organisms: the mouse ichthyosis (ic) locus IS Lbr; naturally occurring PHA exists in cats, rabbits, and dogs

The mouse **ichthyosis (ic)** alleles (ic, icJ, ic4J) carry nonsense/frameshift Lbr mutations (815ins, 1088insCC, 1884insGGAA); icJ homozygotes show complete loss of LBR protein. Homozygous ic mice recapitulate the PHA-like heterochromatin clumping plus alopecia, variable syndactyly, and hydrocephalus, making them a **single-gene model** of PHA. Naturally occurring autosomal-dominant PHA with granulocyte hyposegmentation is documented in **cats** (and classically in **rabbits** and **dogs**), transmitted as an autosomal-dominant trait.

> "we identified one nonsense (815ins) and two frameshift mutations (1088insCC and 1884insGGAA) within the Lbr gene of mice homozygous for either of three independent mutations (ic, ic(J) and ic(4J), respectively) at the ichthyosis locus" — [PMID: 12490533](https://pubmed.ncbi.nlm.nih.gov/12490533/)

> "Autosomal dominant transmission of this anomaly is suspected based on these findings." — [PMID: 4035941](https://pubmed.ncbi.nlm.nih.gov/4035941/) (cats)

### Finding 6 — Biallelic LBR produces a graded spectrum from PHA-with-skeletal-anomalies to lethal Greenberg dysplasia; the peripheral smear aids prenatal diagnosis

Because LBR is bifunctional, its variants generate a graded allelic spectrum: heterozygous benign PHA → **PHA with mild skeletal anomalies (PHASK, MIM #618019)** → **LBR-related regressive spondylometaphyseal dysplasia (LBR-R-SMD)** (e.g., homozygous c.1534C>T, p.Arg512Trp) → biallelic loss causing **perinatal-lethal Greenberg dysplasia (MIM #215140)** with massive skeletal malformation and fetal hydrops. Greenberg dysplasia, dappled diaphyseal dysplasia, and Astley-Kendall dysplasia are proposed **allelic** disorders. Practically, examining **parental peripheral blood smears** for PHA can guide prenatal genetic counseling in pregnancies with short/bowed tubular bones and a narrow thorax.

> "LBR pathogenic variants cause distinct phenotypes due to the dual function of LBR, including Pelger-Huët anomaly (PHA), PHA with mild skeletal anomalies (PHASK; MIM# 618019), LBR-related regressive type of spondylometaphyseal dysplasia (LBR-R-SMD), Greenberg dysplasia (MIM# 215140)." — [PMID: 34467646](https://pubmed.ncbi.nlm.nih.gov/34467646/)

> "Greenberg dysplasia is a rare, autosomal recessive, prenatal lethal bone dysplasia caused by biallelic pathogenic variants in the lamin B receptor (LBR) gene." — [PMID: 32304187](https://pubmed.ncbi.nlm.nih.gov/32304187/)

### Finding 7 — Genetic heterogeneity: NBAS (SOPH), TMEM147, and LMBR1L cause LBR-independent PHA phenotypes

PHA-type neutrophil hyposegmentation is not exclusive to LBR. It is a defining feature of autosomal-recessive **SOPH syndrome** (Short stature, Optic atrophy, Pelger-Huët anomaly; **OMIM #614800**), caused by the **NBAS** founder mutation c.5741G>A (p.Arg1914His) in Yakuts, with an estimated mutation age of ~804 ± 140 years and a heterozygous carrier frequency of ~13 per 1,000. Syndromic **pseudo-PHA** also arises from biallelic **TMEM147** loss-of-function (TMEM147 anchors LBR to the inner nuclear membrane; ~20% of neutrophils affected, plus intellectual disability). An LBR-independent autosomal-recessive hyposegmentation in Australian Shepherd Dogs is caused by an **LMBR1L** splice variant (c.191+1G>A).

> "SOPH syndrome (Short stature with Optic nerve atrophy and Pelger–Huët anomaly syndrome, OMIM#614800) is an autosomal recessive hereditary disease" — [PMID: 29369590](https://pubmed.ncbi.nlm.nih.gov/29369590/)

> "The frequency of heterozygous carriers of mutation G5741→A (R1914H) in gene NBAS was found, which averaged 13 per 1000 healthy Yakuts." — [PMID: 29369590](https://pubmed.ncbi.nlm.nih.gov/29369590/)

> "Abnormal nuclear segmentation and chromatin compaction were also observed in approximately 20% of neutrophils, indicating the presence of a pseudo-Pelger-Huët anomaly." — [PMID: 36044892](https://pubmed.ncbi.nlm.nih.gov/36044892/)

### Finding 8 — LBR is a chimeric protein: N-terminal Tudor/chromatin domain + C-terminal sterol Δ14-reductase; DHCR14 redundancy explains the absent sterol phenotype in heterozygotes

LBR (**UniProt Q14739**) is an integral inner-nuclear-membrane protein with a hydrophilic N-terminal nucleoplasmic domain (a **Tudor-like fold** that binds chromatin, HP1, and lamin B) and a multi-transmembrane C-terminal **sterol Δ14-reductase (C14SR)** domain that uses NADPH in cholesterol biosynthesis. The crystal structure of the bacterial homolog **MaSR1** (10 transmembrane segments, NADPH-bound catalytic domain) provides molecular insight into disease mutations in LBR and the related **DHCR7**. Critically, LBR shares its Δ14-reductase activity with **DHCR14/TM7SF2** — "twin" enzymes with high sequence/structural homology but divergent regulation — which explains why heterozygous PHA carriers show **no sterol/cholesterol phenotype**. **TMEM147** interacts with LBR to regulate its localization/levels and cholesterol homeostasis.

> "Lamin B receptor (LBR), an integral inner nuclear membrane protein, also contains a functional C14SR domain." — [PMID: 25307054](https://pubmed.ncbi.nlm.nih.gov/25307054/)

> "DHCR14 and LBR uniquely share the same Δ-14 reductase activity in cholesterol biosynthesis" — [PMID: 31911440](https://pubmed.ncbi.nlm.nih.gov/31911440/)

> "TMEM147 interacts with lamin B receptor, regulates its localization and levels, and affects cholesterol homeostasis" — [PMID: 32694168](https://pubmed.ncbi.nlm.nih.gov/32694168/)

### Finding 9 — The lobulated nucleus (high LBR/low lamin A/C) enables deformability for migration; HL-60 LBR-knockdown is an in-vitro PHA model

Neutrophil nuclear lobulation is produced by **elevated LBR together with decreased lamin A/C**; the resulting deformable nucleus facilitates rapid egress from blood vessels and migration through tight tissue spaces to sites of infection, where the nucleus is a **rate-limiting factor** for migration. A single dominant LBR mutation yields hypolobulated nuclei (PHA), while homozygosity produces fully ovoid granulocyte nuclei. A stable **LBR-knockdown HL-60 subline** recapitulates PHA in vitro: on retinoic-acid-induced granulopoiesis the knockdown cells retain an ovoid nucleus with reduced lamin A/C, whereas parental cells develop highly lobulated nuclei; phorbol-ester-induced macrophage differentiation is unaffected.

> "A single dominant mutation in humans leads to neutrophils with hypolobulated nuclei (Pelger-Huet anomaly); homozygosity leads to ovoid granulocyte nuclei." — [PMID: 17245605](https://pubmed.ncbi.nlm.nih.gov/17245605/)

> "a stable LBR knockdown subline of HL-60 cells was established" — [PMID: 21327094](https://pubmed.ncbi.nlm.nih.gov/21327094/)

> "As a rate-limiting factor for cell migration, nuclear morphology and biomechanics are particularly important in the context of neutrophil migration during immune responses." — [PMID: 30564248](https://pubmed.ncbi.nlm.nih.gov/30564248/)

---

## Comprehensive Disease Characteristics

### 1. Disease Information

**Overview.** Pelger-Huët anomaly is an inherited disorder of granulocyte (chiefly neutrophil) nuclear morphology, first described by Pelger (1928) and Huët (1931). Neutrophils fail to develop the normal multilobed (3–5 lobe) nucleus and instead present with **hypolobulated** shapes — round (single lobe), bilobed "pince-nez"/"spectacle," or dumbbell/peanut forms — accompanied by unusually **coarse, dense chromatin clumping**. The heterozygous anomaly is benign; homozygous LBR loss and biallelic LBR sterol-reductase loss cause skeletal dysplasia up to perinatal-lethal disease.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008214 |
| OMIM (benign PHA) | #169400 |
| OMIM (PHA + skeletal anomalies / PHASK) | #618019 |
| OMIM (Greenberg dysplasia, biallelic) | #215140 |
| OMIM (SOPH, NBAS) | #614800 |
| Gene | LBR (HGNC:6518), 1q42.12; UniProt Q14739 |
| ICD-10 | D72.0 (Genetic anomalies of leukocytes) |
| MeSH | Pelger-Huet Anomaly (D010381) |

**Synonyms / alternative names.** Pelger-Huët anomaly; Pelger-Huet nuclear anomaly; Pelger's nuclear anomaly; congenital hyposegmentation of granulocytes; "pince-nez" neutrophils. Homozygous forms overlap with HEM/Greenberg skeletal dysplasia.

**Information source.** Predominantly **aggregated disease-level resources** (OMIM, Orphanet) supplemented by individual case reports and pedigrees (e.g., an eight-generation Icelandic pedigree, [PMID: 35650273](https://pubmed.ncbi.nlm.nih.gov/35650273/)), plus population GWAS of band-neutrophil fraction.

### 2. Etiology

**Causal factors.** The primary cause is **genetic** — heterozygous loss-of-function variants in **LBR** for classic benign PHA (Finding 1). There is a clean **genotype→severity** relationship: one defective allele = benign hypolobulation; two = ovoid nuclei plus (when the sterol-reductase function is lost) skeletal dysplasia/Greenberg dysplasia.

**Genetic risk factors.** LBR pathogenic variants are the causal genetic factor. GWAS of band-neutrophil fraction in 88,101 Icelanders identified **five variants at the LBR locus** and cosegregation of a rare LBR stop-gain with PHA, plus additional inner-nuclear-membrane loci ([PMID: 35650273](https://pubmed.ncbi.nlm.nih.gov/35650273/)). Additional causal genes for PHA-like phenotypes: **NBAS** (SOPH), **TMEM147**, and (canine) **LMBR1L** (Finding 7).

**Environmental risk factors (for acquired pseudo-PHA).** Not risk factors for inherited PHA, but for the *acquired* phenocopy: myeloid malignancy (MDS/AML, esp. 17p abnormalities), drugs (mycophenolate mofetil, tacrolimus, colchicine, immunosuppressants), and ionizing radiation (Finding 3; [PMID: 16390246](https://pubmed.ncbi.nlm.nih.gov/16390246/), [PMID: 25627941](https://pubmed.ncbi.nlm.nih.gov/25627941/)).

**Protective factors.** The enzymatic **redundancy of DHCR14/TM7SF2** is effectively a molecular "protective" buffer that prevents a sterol/skeletal phenotype in LBR heterozygotes (Finding 8). No dietary/lifestyle protective factors are defined.

**Gene–environment interactions.** Not a feature of inherited PHA. The relevant interaction is between drug/radiation exposure and clonal myeloid state producing acquired pseudo-PHA.

### 3. Phenotypes

The defining phenotype is a **laboratory/morphologic abnormality** of the neutrophil, not a symptom. Affected individuals are generally asymptomatic.

| Phenotype | Type | Onset | Severity / progression | Frequency | HPO suggestion |
|---|---|---|---|---|---|
| Bilobed/hypolobulated neutrophil nucleus ("pince-nez") | Laboratory / morphologic | Congenital | Stable, non-progressive | ~100% of neutrophils in heterozygotes | HP:0034236 (abnormal neutrophil morphology); abnormal granulocyte nuclear segmentation |
| Coarse chromatin clumping | Laboratory / morphologic | Congenital | Stable | Characteristic | — |
| Pseudo–left shift (apparent ↑ band forms) | Laboratory artifact | Congenital | Stable | Common on automated differential | — |
| Ovoid (round) granulocyte nuclei (homozygous) | Laboratory / morphologic | Congenital | Stable | Homozygotes | — |
| Skeletal dysplasia — rhizomelic limb shortening, bowing, narrow thorax (biallelic/PHASK/Greenberg) | Physical / radiographic | Prenatal–neonatal | Severe → lethal (Greenberg) | Biallelic only | HP:0008905 (rhizomelia); HP:0000772 (abnormal rib morphology); HP:0001789 (hydrops fetalis) |
| Developmental features (alopecia, syndactyly, hydrocephalus) | Physical | Congenital | Model/syndrome-dependent | Model organisms / syndromic | — |

**Quality-of-life impact.** For heterozygous PHA: **negligible** — no functional impairment; the main "impact" is iatrogenic risk from misdiagnosis. For biallelic skeletal dysplasia/Greenberg dysplasia: profound (perinatal lethality).

### 4. Genetic / Molecular Information

**Causal gene.** **LBR** (lamin B receptor), HGNC:6518, chr 1q42.12, UniProt **Q14739**. Encodes a bifunctional integral inner-nuclear-membrane protein (Finding 8).

**Pathogenic variants.** Variant classes reported include nonsense, frameshift, missense, splice-site, and whole-gene deletion. Illustrative examples from the reviewed literature:
- Novel missense c.561C>G ([PMID: 40980134](https://pubmed.ncbi.nlm.nih.gov/40980134/)).
- Missense c.1011T>G (p.Cys337Trp) and a Chr1q42.12 LBR gene deletion, both associated with impaired sterol reductase function and skeletal dysplasia ([PMID: 40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/)).
- Homozygous c.1534C>T (p.Arg512Trp) → LBR-related regressive spondylometaphyseal dysplasia ([PMID: 34467646](https://pubmed.ncbi.nlm.nih.gov/34467646/)).
- Rare stop-gain LBR variant cosegregating with PHA in a large Icelandic pedigree ([PMID: 35650273](https://pubmed.ncbi.nlm.nih.gov/35650273/)).

**Classification & consequence.** LBR variants act by **loss of function** (haploinsufficiency for the structural nuclear-shape phenotype). Heterozygous LOF → benign PHA; biallelic LOF affecting the sterol-reductase domain → skeletal dysplasia/Greenberg. Variant origin is **germline**. Somatic/acquired pseudo-PHA is not caused by LBR mutation but by clonal myeloid disease (esp. 17p abnormalities) or exposures.

**Modifier genes.** **DHCR14/TM7SF2** (enzymatic redundancy buffering the sterol phenotype) and **TMEM147** (regulates LBR localization/levels) function as molecular modifiers (Finding 8). LBR is also a substrate of the **GSK3β/FBW7** proteasomal pathway; the C337W mutant is preferentially degraded, linking to Wnt signaling ([PMID: 40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/)).

**Epigenetic information.** LBR's core function is **chromatin architectural** — tethering peripheral heterochromatin at the nuclear lamina and organizing HP1-associated silenced chromatin ([PMID: 41735607](https://pubmed.ncbi.nlm.nih.gov/41735607/)). No disease-specific DNA-methylation signature is defined for PHA.

**Chromosomal abnormalities.** Not a cause of inherited PHA. **Acquired** pseudo-PHA correlates with chromosome **17p deletions/monosomy 17** in MDS/AML ([PMID: 2340488](https://pubmed.ncbi.nlm.nih.gov/2340488/)).

### 5. Environmental Information

Environmental factors are irrelevant to **inherited** PHA. For the **acquired phenocopy**: toxins/drugs (mycophenolate, tacrolimus, colchicine, chemotherapy/alkylating agents), **ionizing radiation** (dose-dependent, [PMID: 25627941](https://pubmed.ncbi.nlm.nih.gov/25627941/)), and infections have been reported as triggers ([PMID: 20691170](https://pubmed.ncbi.nlm.nih.gov/20691170/)). No specific infectious agent causes PHA.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (heterozygous, benign PHA — structural axis):**

1. A **heterozygous loss-of-function LBR variant** *reduces* functional LBR protein at the inner nuclear membrane (haploinsufficiency). *[Demonstrated: gene-dosage effect, [PMID: 27684937](https://pubmed.ncbi.nlm.nih.gov/27684937/)].*
2. Reduced LBR *impairs* tethering of peripheral heterochromatin and lamin B to the nuclear envelope. *[Demonstrated in tether biology, [PMID: 41735607](https://pubmed.ncbi.nlm.nih.gov/41735607/)].*
3. During C/EBPε-driven granulopoiesis, the normal **reciprocal remodeling (LBR↑ / lamin-A/C↓)** *fails to complete*, so the nucleus does not acquire multiple lobes. *[Demonstrated: C/EBPε control, [PMID: 18621876](https://pubmed.ncbi.nlm.nih.gov/18621876/); LBR/lamin A-C balance, [PMID: 17245605](https://pubmed.ncbi.nlm.nih.gov/17245605/)].*
4. This *results in* **hypolobulated ("pince-nez"), coarsely clumped neutrophil nuclei** — the diagnostic PHA morphology.
5. Because innate effector programs are largely independent of nuclear shape, neutrophil **function is preserved** in human heterozygotes → **benign phenotype**. *[Demonstrated: morphological-not-functional maturation, [PMID: 18621876](https://pubmed.ncbi.nlm.nih.gov/18621876/)].*

**Branch A — homozygous LBR loss (severe structural):** two null alleles → **ovoid** granulocyte nuclei ([PMID: 17245605](https://pubmed.ncbi.nlm.nih.gov/17245605/)); in complete-null models, additional deficits in promyelocyte proliferation and respiratory burst can appear ([PMID: 18550262](https://pubmed.ncbi.nlm.nih.gov/18550262/)).

**Branch B — biallelic loss of the sterol Δ14-reductase (enzymatic/skeletal axis):**

6b. Biallelic variants that *abolish* LBR's C-terminal sterol Δ14-reductase activity *reduce* LBR-dependent cholesterol synthesis in cells where DHCR14 cannot fully compensate (e.g., osteogenic lineage). *[Demonstrated: [PMID: 31911440](https://pubmed.ncbi.nlm.nih.gov/31911440/), [PMID: 40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/)].*
7b. Impaired cholesterol synthesis *disrupts* **Wnt (WNT3A) pathway** activation and osteogenic differentiation (rescuable by adding cholesterol in MC3T3-E1 cells). *[Demonstrated in vitro, [PMID: 40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/)].*
8b. This *leads to* **skeletal dysplasia** graded from PHASK/LBR-R-SMD to perinatal-lethal **Greenberg dysplasia** with fetal hydrops. *[Demonstrated clinically, [PMID: 32304187](https://pubmed.ncbi.nlm.nih.gov/32304187/), [PMID: 34467646](https://pubmed.ncbi.nlm.nih.gov/34467646/)].*

*Note:* The redundancy of **DHCR14** means that in heterozygotes (and in tissues where DHCR14 is active) no sterol/skeletal phenotype emerges — a key inferred protective mechanism supported by mouse digenic studies ([PMID: 17403717](https://pubmed.ncbi.nlm.nih.gov/17403717/)).

**Functional significance of lobulation (inferred/supported):** the lobulated, deformable nucleus (high LBR/low lamin A/C) is thought to lower nuclear stiffness — the rate-limiting factor — for neutrophil egress and migration through confined tissue ([PMID: 30564248](https://pubmed.ncbi.nlm.nih.gov/30564248/), [PMID: 17245605](https://pubmed.ncbi.nlm.nih.gov/17245605/)). In human PHA this appears clinically inconsequential, though mouse ic/ic neutrophils show abnormal chemotaxis ([PMID: 18550262](https://pubmed.ncbi.nlm.nih.gov/18550262/)).

**Pathways / processes / ontology suggestions:**
- Molecular pathways: cholesterol biosynthesis (KEGG hsa00100), canonical Wnt signaling, GSK3β/FBW7 proteasomal degradation.
- GO biological process: heterochromatin organization (GO:0070828), nuclear envelope organization (GO:0006998), neutrophil differentiation (GO:0030223), sterol biosynthetic process (GO:0016126), cholesterol biosynthetic process (GO:0006695).
- GO molecular function: delta14-sterol reductase activity (GO:0050614).
- GO cellular component: nuclear inner membrane (GO:0005637), nuclear envelope (GO:0005635), nuclear lamina (GO:0005652).
- CL cell types: neutrophil (CL:0000775), band form neutrophil (CL:0000094), promyelocyte (CL:0000836), osteoblast (CL:0000062, skeletal branch).
- CHEBI: cholesterol (CHEBI:16113), NADPH (CHEBI:16474).

### 7. Anatomical Structures Affected

- **Organ / system level (benign PHA):** the **hematopoietic/immune system** — specifically bone marrow granulopoiesis and circulating neutrophils. UBERON: blood (UBERON:0000178), bone marrow (UBERON:0002371).
- **Biallelic disease:** the **skeletal system** — long bones (rhizomelic shortening/bowing), ribs/thorax, vertebrae/metaphyses; plus fetal soft-tissue hydrops in Greenberg dysplasia. UBERON: skeletal system (UBERON:0001434), long bone (UBERON:0002495), rib (UBERON:0002228).
- **Tissue/cell level:** granulocytic lineage cells (neutrophils, band forms, promyelocytes); in skeletal disease, osteogenic mesenchyme/osteoblasts. CL:0000775 (neutrophil), CL:0000836 (promyelocyte).
- **Subcellular level:** the **nuclear inner membrane / nuclear envelope / nuclear lamina** and associated **peripheral heterochromatin** are the primary compartments. GO:0005637 (nuclear inner membrane), GO:0005635 (nuclear envelope), GO:0005652 (nuclear lamina).
- **Localization / lateralization:** systemic (all neutrophils affected); skeletal involvement is bilateral/symmetric.

### 8. Temporal Development

- **Onset:** **congenital** — the morphologic anomaly is present from birth and lifelong. Skeletal dysplasia forms present prenatally/neonatally.
- **Progression:** benign PHA is **stable and non-progressive**; it neither worsens nor resolves. Biallelic Greenberg dysplasia is prenatal-lethal.
- **Course / duration:** benign PHA is a **chronic lifelong** morphologic trait with no clinical evolution. No remission (nor need for it).
- **Critical periods:** the mechanistically relevant window is **terminal granulopoiesis** (C/EBPε-driven LBR upregulation); for skeletal disease, **fetal skeletal development**. For acquired pseudo-PHA, morphology tracks the underlying disease/exposure and can be **reversible** (e.g., after dose reduction of mycophenolate, [PMID: 16390246](https://pubmed.ncbi.nlm.nih.gov/16390246/)).

### 9. Inheritance and Population

- **Epidemiology:** incidence of heterozygous PHA ≈ **1 in 6,000** ([PMID: 26634137](https://pubmed.ncbi.nlm.nih.gov/26634137/)). Prevalence varies by population and reporting; homozygous/biallelic disease is very rare.
- **Inheritance pattern:** **autosomal dominant** (benign PHA); **autosomal recessive** for biallelic skeletal dysplasia/Greenberg dysplasia and for SOPH (NBAS) and TMEM147 forms.
- **Penetrance/expressivity:** high penetrance for the morphologic trait in heterozygotes; **variable expressivity** at the biallelic/skeletal end (PHASK → Greenberg).
- **Founder effects:** the **NBAS c.5741G>A (R1914H)** SOPH founder mutation in **Yakuts** (Sakha), carrier frequency ~13/1,000, mutation age ~804 ± 140 years ([PMID: 29369590](https://pubmed.ncbi.nlm.nih.gov/29369590/)). A large **Icelandic** PHA pedigree traces the trait across eight generations ([PMID: 35650273](https://pubmed.ncbi.nlm.nih.gov/35650273/)).
- **Consanguinity:** relevant to biallelic (recessive) skeletal-dysplasia and SOPH cases.
- **Sex ratio / age distribution:** benign PHA affects sexes equally and is present at all ages (congenital).

### 10. Diagnostics

- **Primary test:** **peripheral blood smear** with morphologic review — recognition of hypolobulated ("pince-nez"/dumbbell), coarsely clumped neutrophil nuclei in a **majority** of neutrophils. Automated hematology analyzers may flag a spurious "left shift" ([PMID: 19021122](https://pubmed.ncbi.nlm.nih.gov/19021122/)).
- **Quantitative morphology:** image analysis of nuclear segmentation reliably discriminates genotypes and can quantify LBR allele dosage ([PMID: 27684937](https://pubmed.ncbi.nlm.nih.gov/27684937/)).
- **Genetic testing:** **LBR single-gene sequencing** confirms diagnosis; **gene panels / WES / WGS** are useful when syndromic features suggest NBAS (SOPH), TMEM147, or skeletal-dysplasia differential. **Karyotype/FISH/CMA** are used chiefly to *exclude* clonal myeloid disease (17p) in suspected acquired pseudo-PHA.
- **Key differential:** **acquired ("pseudo") PHA** — distinguished by clinical context, additional dysplastic features (hypogranular neutrophils, other-lineage dysplasia), abnormal cytogenetics, and reversibility. Family history and a normal parental smear help ([PMID: 20691170](https://pubmed.ncbi.nlm.nih.gov/20691170/), [PMID: 19021122](https://pubmed.ncbi.nlm.nih.gov/19021122/)). Other differentials: true left shift of infection, MDS/AML, drug effect, radiation.
- **Prenatal:** for pregnancies with short/bowed bones and narrow thorax, examine **parental blood smears** for PHA to inform LBR-related dysplasia counseling ([PMID: 34467646](https://pubmed.ncbi.nlm.nih.gov/34467646/), [PMID: 36712868](https://pubmed.ncbi.nlm.nih.gov/36712868/)).
- **Screening:** no population newborn screening; recognition is opportunistic on routine CBC/differential.

### 11. Outcome / Prognosis

- **Benign PHA:** **normal life expectancy**, normal survival, and **no excess morbidity or mortality**. Neutrophil function is preserved; carriers are not immunodeficient. The main adverse outcome is iatrogenic (misdiagnosis → unnecessary work-up/treatment).
- **Biallelic / Greenberg dysplasia:** **perinatal lethal** ([PMID: 32304187](https://pubmed.ncbi.nlm.nih.gov/32304187/)); intermediate PHASK/LBR-R-SMD has variable skeletal morbidity.
- **Prognostic factors:** the single dominant determinant is **LBR zygosity + whether the sterol-reductase function is retained**. Acquired pseudo-PHA carries the prognosis of its underlying cause (e.g., MDS/AML).

### 12. Treatment

- **Inherited PHA requires no treatment.** Management is **recognition and reassurance**, plus documentation to prevent repeated infection work-ups and to avoid misclassification as MDS. No pharmacotherapy, gene therapy, or surgery is indicated for the benign trait.
- **Genetic counseling** is the principal intervention (autosomal-dominant transmission; discuss the rare risk of biallelic skeletal dysplasia if both partners carry LBR variants). NCIT: genetic counseling (NCIT:C15254).
- **Biallelic skeletal dysplasia / Greenberg dysplasia:** no disease-modifying therapy; management is supportive/palliative and reproductive counseling. In-vitro data suggest cholesterol supplementation rescues osteogenic defects in cell models ([PMID: 40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/)), but this is **experimental** and not a clinical therapy.
- **Acquired pseudo-PHA:** treat the **underlying cause** (manage MDS/AML; reduce/withdraw the offending drug — reversibility documented for mycophenolate, [PMID: 16390246](https://pubmed.ncbi.nlm.nih.gov/16390246/)).

### 13. Prevention

- **Primary prevention:** not applicable to a congenital dominant trait; the relevant "prevention" is **genetic counseling** and, for couples both carrying LBR variants, discussion of reproductive options (prenatal testing, PGD) to avoid biallelic lethal disease.
- **Secondary prevention:** ensure PHA is **flagged in the medical record** so a benign smear finding does not precipitate invasive work-up; distinguish from acquired pseudo-PHA to catch underlying myeloid disease early.
- **Tertiary prevention:** not applicable (no complications in benign PHA).
- **Immunization / behavioral / public-health measures:** none applicable.

### 14. Other Species / Natural Disease

- **Taxonomy:** naturally occurring, autosomal-dominant PHA is documented in **domestic cat** (*Felis catus*, NCBI:txid9685; [PMID: 4035941](https://pubmed.ncbi.nlm.nih.gov/4035941/)), **domestic rabbit** (*Oryctolagus cuniculus*, NCBI:txid9986; [PMID: 407754](https://pubmed.ncbi.nlm.nih.gov/407754/)), and **dog** (*Canis lupus familiaris*, NCBI:txid9615). The laboratory **mouse** (*Mus musculus*, NCBI:txid10090) carries the orthologous **ichthyosis (ic)** locus (Finding 5).
- **Breed:** an LBR-**independent** autosomal-recessive granulocyte hyposegmentation is common in **Australian Shepherd Dogs** (39/300 genotyped, 13%), caused by an **LMBR1L** splice variant, and is prenatally lethal in homozygous puppies ([PMID: 37347778](https://pubmed.ncbi.nlm.nih.gov/37347778/)).
- **Orthologous genes:** mouse *Lbr* (the ic locus), and canine *LMBR1L* (distinct gene, distinct mechanism).
- **Comparative pathology / evolutionary conservation:** LBR's dual chromatin-tethering + sterol-reductase function is conserved from a bacterial homolog (MaSR1) through mice to humans ([PMID: 25307054](https://pubmed.ncbi.nlm.nih.gov/25307054/)); the neutrophil hyposegmentation phenotype is broadly conserved across mammals, though not always via LBR (canine LMBR1L). **No zoonotic potential** (non-infectious genetic trait).

### 15. Model Organisms

| Model | Type | Lesion | Recapitulation | Reference |
|---|---|---|---|---|
| Mouse **ichthyosis (ic, icJ, ic4J)** | Mammalian, natural mutant | Nonsense/frameshift *Lbr* (815ins, 1088insCC, 1884insGGAA) | PHA-like heterochromatin clumping + alopecia, variable syndactyly, hydrocephalus | [PMID: 12490533](https://pubmed.ncbi.nlm.nih.gov/12490533/) |
| **Lbr-GT/GT** gene-trap mouse | Mammalian knockout | Lbr null | PHA model; morphological (not functional) granulocyte maturation defect; C/EBPε-regulated | [PMID: 18621876](https://pubmed.ncbi.nlm.nih.gov/18621876/) |
| **EML-ic/ic** progenitor line | In-vitro myeloid model | Lbr-deficient | Nuclear hypolobulation, abnormal chemotaxis, ↓proliferation, deficient respiratory burst; rescued by full-length or C-terminal Lbr | [PMID: 18550262](https://pubmed.ncbi.nlm.nih.gov/18550262/), [PMID: 22140257](https://pubmed.ncbi.nlm.nih.gov/22140257/) |
| **HL-60 LBR-knockdown** subline | Human cell line, in vitro | Stable LBR shRNA knockdown | On RA-induced granulopoiesis, retains ovoid nucleus + ↓lamin A/C (vs lobulated parent); macrophage differentiation unaffected | [PMID: 21327094](https://pubmed.ncbi.nlm.nih.gov/21327094/) |
| **HL-60/S4** (ELCS) | Human cell line | RA differentiation | RA↑LBR drives multilobed nuclei with envelope-limited chromatin sheets; TPA→macrophage lacks lobulation/↓LBR | [PMID: 42124592](https://pubmed.ncbi.nlm.nih.gov/42124592/) |
| **MC3T3-E1** osteoblast | Cell line | Lbr knockdown / cholesterol removal | Reduced Wnt-dependent mineralization, rescued by cholesterol — models skeletal branch | [PMID: 40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/) |
| Digenic **Lbr/Dhcr14** mouse | Mammalian | Combined LOF | Demonstrates DHCR14/LBR sterol-reductase redundancy | [PMID: 17403717](https://pubmed.ncbi.nlm.nih.gov/17403717/) |

**Model strengths/limitations:** the ic mouse and HL-60 knockdown faithfully reproduce the **nuclear-shape** phenotype and the LBR/lamin-A/C molecular logic; complete-null models overstate functional deficits relative to human heterozygous PHA (where function is preserved). Resource databases: **MGI** (mouse *Lbr*/ic), **Cellosaurus/ATCC** (HL-60).

---

## Mechanistic Model / Interpretation

```
              LBR gene (1q42.12) — chimeric bifunctional protein
              ┌───────────────────────────┬───────────────────────────┐
              │ N-terminal (structural)   │ C-terminal (enzymatic)    │
              │ Tudor fold; binds         │ sterol Δ14-reductase      │
              │ heterochromatin, HP1,     │ (C14SR), NADPH-dependent  │
              │ lamin B                   │ cholesterol biosynthesis  │
              └────────────┬──────────────┴──────────────┬────────────┘
                           │                             │
      C/EBPε ↑ LBR during  │                             │  DHCR14/TM7SF2 = redundant
      granulopoiesis;      │                             │  Δ14-reductase (buffers heterozygotes)
      LBR↑ / lamin-A/C↓    │                             │
                           ▼                             ▼
   ── STRUCTURAL AXIS ──────────────         ── ENZYMATIC AXIS ─────────────────
   HET LOF → hypolobulated                   BIALLELIC LOF of C14SR →
   "pince-nez" neutrophils                   ↓cholesterol → Wnt disruption →
   (BENIGN PHA, function intact)             osteogenesis failure
   HOM LOF → ovoid nuclei                    → PHASK → LBR-R-SMD → GREENBERG
   (± proliferation/burst deficits)            dysplasia (perinatal lethal)

   PHENOCOPIES (not LBR mutation):
   • Acquired pseudo-PHA: MDS/AML (17p), drugs (MMF, tacrolimus, colchicine), radiation
   • LBR-independent genetic: NBAS (SOPH), TMEM147, canine LMBR1L
```

The unifying insight is **one gene, two functions, two disease axes, graded by allele dosage**. The structural axis explains the neutrophil morphology and its benign nature in heterozygotes; the enzymatic axis — unmasked only when biallelic loss overwhelms DHCR14 redundancy — explains the skeletal dysplasia spectrum. Acquired pseudo-PHA and LBR-independent genetic causes converge on the same morphologic endpoint through different routes, which is why context and genetics, not morphology alone, drive diagnosis and prognosis.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [41059452](https://pubmed.ncbi.nlm.nih.gov/41059452/) | Allelic series + OMIM IDs (heterozygous PHA vs biallelic dysplasia/Greenberg) | F1 |
| [42622427](https://pubmed.ncbi.nlm.nih.gov/42622427/) | LBR dual structural + sterol-reductase function; homozygous PHA without dysplasia | F1, F8 |
| [26634137](https://pubmed.ncbi.nlm.nih.gov/26634137/) | Incidence ~1/6000; benign AD; band-form pitfall | F2 |
| [27684937](https://pubmed.ncbi.nlm.nih.gov/27684937/) | 65% variance from LBR allele count; hysteresis dose-response | F3 |
| [2340488](https://pubmed.ncbi.nlm.nih.gov/2340488/) | Pseudo-PHA ↔ monosomy 17 in MDS/AML | F3 |
| [25627941](https://pubmed.ncbi.nlm.nih.gov/25627941/) | Radiation dose-dependent pseudo-PHA | F3 |
| [41735607](https://pubmed.ncbi.nlm.nih.gov/41735607/) | LBR (+LAP2) as heterochromatin tether | F4 |
| [18621876](https://pubmed.ncbi.nlm.nih.gov/18621876/) | C/EBPε → Lbr; morphological not functional maturation; Lbr-GT/GT PHA model | F4 |
| [12490533](https://pubmed.ncbi.nlm.nih.gov/12490533/) | Mouse ic locus = Lbr mutations | F5 |
| [4035941](https://pubmed.ncbi.nlm.nih.gov/4035941/) | Autosomal-dominant PHA in cats | F5 |
| [34467646](https://pubmed.ncbi.nlm.nih.gov/34467646/) | Graded LBR phenotype spectrum (PHA→PHASK→LBR-R-SMD→Greenberg) | F6 |
| [32304187](https://pubmed.ncbi.nlm.nih.gov/32304187/) | Biallelic LBR → lethal Greenberg dysplasia; allelic disorders | F6 |
| [29369590](https://pubmed.ncbi.nlm.nih.gov/29369590/) | NBAS/SOPH; Yakut founder carrier frequency | F7 |
| [36044892](https://pubmed.ncbi.nlm.nih.gov/36044892/) | TMEM147 LOF → syndromic pseudo-PHA (~20% neutrophils) | F7 |
| [37347778](https://pubmed.ncbi.nlm.nih.gov/37347778/) | Canine LMBR1L LBR-independent hyposegmentation | F7 |
| [25307054](https://pubmed.ncbi.nlm.nih.gov/25307054/) | MaSR1 structure; LBR C14SR domain | F8 |
| [31911440](https://pubmed.ncbi.nlm.nih.gov/31911440/) | DHCR14/LBR twin-enzyme redundancy | F8 |
| [32694168](https://pubmed.ncbi.nlm.nih.gov/32694168/) | TMEM147 regulates LBR + cholesterol | F8 |
| [17245605](https://pubmed.ncbi.nlm.nih.gov/17245605/) | Dominant→hypolobulated / homozygous→ovoid; LBR/lamin A-C | F9 |
| [21327094](https://pubmed.ncbi.nlm.nih.gov/21327094/) | HL-60 LBR-knockdown in-vitro PHA model | F9 |
| [30564248](https://pubmed.ncbi.nlm.nih.gov/30564248/) | Nucleus as rate-limiting for neutrophil migration | F9 |
| [40355051](https://pubmed.ncbi.nlm.nih.gov/40355051/) | LBR→cholesterol→Wnt in skeletal dysplasia; FBW7 degradation | F6, mechanism |
| [17403717](https://pubmed.ncbi.nlm.nih.gov/17403717/) | Digenic Lbr/Dhcr14 mouse; laminopathy vs sterol error | F8, models |
| [22140257](https://pubmed.ncbi.nlm.nih.gov/22140257/) | Sterol-reductase domain supports myeloid growth/maturation | F4, models |
| [35650273](https://pubmed.ncbi.nlm.nih.gov/35650273/) | GWAS: LBR locus + INM loci; Icelandic PHA pedigree | F1, epidemiology |

---

## Limitations and Knowledge Gaps

1. **Purely literature-based synthesis.** No primary patient-level dataset was analyzed; findings rest on published reports, case series, GWAS, and model-organism studies. Effect sizes are available for a few metrics (LBR allele-dose variance ~65%; radiation PH-cell %) but most claims are qualitative.
2. **Quantitative epidemiology is sparse.** The commonly cited ~1/6,000 incidence lacks robust modern, multi-ethnic prevalence/incidence estimates; geographic and sex-specific data are limited.
3. **Function-vs-morphology uncertainty.** Human heterozygous PHA neutrophils are functionally normal, yet complete-null mouse/EML models show chemotaxis, proliferation, and respiratory-burst deficits. The threshold at which nuclear-shape loss becomes functionally significant in humans is not defined.
4. **DHCR14 redundancy is tissue-dependent** and incompletely mapped; why skeletal (osteogenic) tissue is selectively vulnerable to biallelic LBR sterol-reductase loss while blood is not is inferred, not fully demonstrated in humans.
5. **Acquired pseudo-PHA mechanism** remains unclear at the molecular level ([PMID: 20691170](https://pubmed.ncbi.nlm.nih.gov/20691170/)); the link to 17p is correlative.
6. **Genotype–phenotype granularity** across the PHASK/LBR-R-SMD/Greenberg continuum is limited by small case numbers.

## Proposed Follow-up Experiments / Actions

1. **Modern epidemiology:** leverage large biobanks (e.g., deCODE/UK Biobank-scale CBC + morphology + sequencing) to refine PHA prevalence, penetrance, and LBR variant spectrum across ancestries — building on [PMID: 35650273](https://pubmed.ncbi.nlm.nih.gov/35650273/).
2. **Tissue-resolved DHCR14/LBR redundancy map:** quantify DHCR14 vs LBR sterol-Δ14-reductase contribution across osteoblasts, chondrocytes, and myeloid cells (isoform-specific KO + sterol profiling) to explain skeletal selectivity.
3. **Functional deep-phenotyping of human heterozygous PHA neutrophils:** confined-migration/microfluidic assays and infection-response readouts to definitively test whether reduced nuclear deformability has any subclinical cost.
4. **Structure-guided variant classification:** use the MaSR1 structure ([PMID: 25307054](https://pubmed.ncbi.nlm.nih.gov/25307054/)) and AlphaFold models of LBR to predict which missense variants abolish sterol-reductase activity (skeletal risk) vs only structural function (benign) — improving prenatal counseling.
5. **Standardized diagnostic algorithm** distinguishing inherited PHA from acquired pseudo-PHA (automated image analysis + reflex cytogenetics/LBR sequencing) to reduce misdiagnosis, formalizing [PMID: 27684937](https://pubmed.ncbi.nlm.nih.gov/27684937/) and [PMID: 19021122](https://pubmed.ncbi.nlm.nih.gov/19021122/).
6. **Mechanistic dissection of acquired pseudo-PHA:** test whether 17p-associated genes, drug exposures, or radiation converge on LBR expression/localization (e.g., via TMEM147 or C/EBPε) to phenocopy inherited PHA.

---

*Report compiled from 9 confirmed findings across 44 reviewed papers. Evidence sources span human clinical/genetic studies, population GWAS, model organisms (mouse ic/Lbr, EML, HL-60), in-vitro cell work, and structural biology.*


## Artifacts

- [OpenScientist final report](Pelger-Huet_Anomaly-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pelger-Huet_Anomaly-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 33 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008214` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Pelger-Huet anomaly**
- `HP:0034236` (1 mention) - the report calls it "abnormal neutrophil morphology"; HP calls it **Apnea of prematurity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0070828` (1 mention) - the report calls it "GO biological process: heterochromatin organization"; GO calls it **heterochromatin organization**
- `GO:0050614` (1 mention) - the report calls it "GO molecular function: delta14-sterol reductase activity"; GO calls it **Delta24-sterol reductase activity**
- `GO:0005637` (2 mentions) - the report calls it "GO cellular component: nuclear inner membrane", "nuclear inner membrane"; GO calls it **nuclear inner membrane**
- `CL:0000775` (2 mentions) - the report calls it "CL cell types: neutrophil", "neutrophil"; CL calls it **neutrophil**
- `CHEBI:16113` (1 mention) - the report calls it "CHEBI: cholesterol"; CHEBI calls it **cholesterol**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005637` - called "GO cellular component: nuclear inner membrane", "nuclear inner membrane"
- `CL:0000775` - called "CL cell types: neutrophil", "neutrophil"