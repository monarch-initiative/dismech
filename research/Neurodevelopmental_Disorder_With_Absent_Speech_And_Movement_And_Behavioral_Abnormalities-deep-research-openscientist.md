---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-20T07:13:58.129702'
end_time: '2026-08-20T07:36:30.627772'
duration_seconds: 1352.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral
    Abnormalities
  mondo_id: ''
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 9
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:33182779
  relevance_assessed: 18
  on_topic: 9
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Absent_Speech_And_Movement_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Absent_Speech_And_Movement_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities** covering all of the
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

# Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities (NEDASMB)

*A comprehensive disease-characteristics report for knowledge-base curation*

**Disease:** Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities (NEDASMB)
**MONDO ID:** MONDO:0859519 · **OMIM phenotype:** #620270 · **Gene:** *UBE3C* (MIM 614454)
**Category:** Mendelian (autosomal recessive)

---

## Summary

**Neurodevelopmental Disorder With Absent Speech and Movement and Behavioral Abnormalities (NEDASMB)** is an ultra-rare Mendelian disorder caused by **biallelic (autosomal-recessive) loss-of-function variants in *UBE3C*** (chromosome 7q36.3), and catalogued as **OMIM #620270 / MONDO:0859519 / MedGen C5830319 (UID 1840955)**. It was first delineated in 2023 by Faqeih and colleagues, who used a paralog-directed candidate-gene approach — reasoning that because *UBE3C* is the paralog of the Angelman-syndrome gene *UBE3A*, its loss might produce an Angelman-like phenotype. They identified three patients from two families with an Angelman-like syndrome carrying two loss-of-function *UBE3C* variants; patient RNA studies confirmed the loss-of-function effect [PMID: 36401616].

Clinically, affected individuals present from infancy with a static (non-progressive) encephalopathy comprising **severe global developmental delay/intellectual disability, absent speech, a movement disorder (ataxia, dystonia, tremor), seizures, and neurobehavioral abnormalities** (autistic features, hyperactivity, aggression, sleep disturbance), together with variable brain-imaging findings such as a thin corpus callosum and cerebellar hypoplasia. Mechanistically, *UBE3C* encodes a **proteasome-associated HECT-type E3 ubiquitin ligase** (UniProt Q15386, 1083 aa) that assembles K48- and K29-linked polyubiquitin chains and enhances proteasome processivity. Its loss is predicted to disrupt neuronal protein homeostasis (proteostasis) during cortical circuit assembly — placing NEDASMB conceptually alongside Angelman syndrome (*UBE3A*) and Kaufman oculocerebrofacial syndrome (*UBE3B*) as a "UBE3-family" neurodevelopmental proteostasis disorder.

Because the disorder was described from a single small cohort, most epidemiological, natural-history, prognostic, and disease-specific molecular parameters remain undefined. There is **no disease-specific treatment**; management is entirely supportive/symptomatic, and diagnosis rests on **exome or genome sequencing** after excluding *UBE3A*/15q11–q13 (Angelman) defects. This report consolidates the confirmed identifiers, genetics, mechanism, phenotype, and knowledge gaps to support a curated disease entry, and flags every place where evidence is currently absent.

---

## Key Findings

### Finding 1 — NEDASMB is caused by biallelic loss-of-function variants in *UBE3C*

NEDASMB (MONDO:0859519, OMIM #620270) is caused by **biallelic loss-of-function (LoF) variants in *UBE3C*** (HGNC:16803; NCBI GeneID 9690; ENSG00000009335; chr7q36.3, GRCh38 chr7:157,138,916–157,269,370). The disorder was defined by a **paralog-directed candidate-gene approach**: because *UBE3C* is the paralog of the Angelman-syndrome E3 ligase gene *UBE3A*, the authors screened patients with an Angelman-like clinical picture and detected two LoF *UBE3C* variants in three patients from two families. Patient RNA studies confirmed the loss-of-function consequence, and inheritance is autosomal recessive [PMID: 36401616].

> "In 3 patients from 2 families with Angelman-like syndrome, paralog-directed candidate gene approach detected 2 LoF variants in the other candidate E3 ligase gene, UBE3C, a paralog of the Angelman syndrome E3 ligase gene, UBE3A." [PMID: 36401616]

> "HECTD4 and UBE3C are novel biallelic rare disease genes, expand the association of the other HECT E3 ligase group with neurodevelopmental syndromes, and could explain some of the missing heritability in patients with a suggestive clinical diagnosis of Angelman syndrome." [PMID: 36401616]

The gene is highly constrained in population databases (gnomAD: pLI = 1.0, LOEUF/oe_lof upper = 0.42, missense-z = 3.17), consistent with strong intolerance to loss-of-function — a genomic signature expected for a gene whose complete biallelic loss produces severe neurodevelopmental disease.

### Finding 2 — *UBE3C* is a proteasome-associated HECT E3 ligase essential for neuronal proteostasis and cortical development

*UBE3C* belongs to the **"other" subfamily of HECT-type E3 ubiquitin ligases**. Its catalytic HECT domain (aa 744–1083) adopts an open, L-shaped bilobed conformation and autoubiquitinates (major site Lys903); the last three C-terminal residues are essential for catalysis [PMID: 32039437]. UBE3C assembles **K48- and K29-linked polyubiquitin chains** [PMID: 25752577] and participates in proteasome processivity, innate immunity, and cancer metastasis.

> "The UBE3C E3 ligase is a member of the 'other' subfamily HECT and influences several crucial cellular processes, including innate immunity, proteasome processivity, and cancer metastasis." [PMID: 32039437]

> "the human HECT E3 ligases UBE3C and AREL1 assemble K48/K29- and K11/K33-linked Ub chains" [PMID: 25752577]

Critically, *UBE3C* is a **brain-expressed member of the UBE3 paralog family** (alongside *UBE3A*/Angelman syndrome and *UBE3B*/Kaufman oculocerebrofacial syndrome), and the family's E3-ligase activity is required for cortical circuit assembly and higher cognition [PMID: 33182779]. A separate *UBE3C*-reducing structural variant causes distal hereditary motor neuropathy (DHMN1) with *C. elegans* synaptic-transmission deficits and heat-stress susceptibility, further implicating protein homeostasis (PMID 36380488, from investigation notes).

> "uninterrupted action of UBE3 ligases is a sine qua non for cortical circuit assembly and higher cognitive functions of the neocortex" [PMID: 33182779]

### Finding 3 — Clinical phenotype: severe global developmental delay, absent speech, movement disorder, seizures, behavioral abnormalities (Angelman-like)

Faqeih et al. described patients with "syndromic neurodevelopmental, seizure, and movement disorders and neurobehavioral phenotypes" in an Angelman-like presentation [PMID: 36401616]. HPO annotations for OMIM:620270 (via Monarch, n = 23 features) span developmental, motor, seizure, and behavioral domains.

> "Chromosomal analysis and exome sequencing were used to identify the genetic causes in 10 patients from 7 unrelated families with syndromic neurodevelopmental, seizure, and movement disorders and neurobehavioral phenotypes." [PMID: 36401616]

Onset is congenital/infantile, and the course is chronic and non-progressive (static encephalopathy). The phenotype closely mirrors Angelman syndrome, which is characterized by "severe mental retardation, epilepsy, absent speech, dysmorphic facial features, and a characteristic behavioral phenotype" [PMID: 17848870], supporting the paralog-driven clinical overlap.

| HPO term | Phenotype | Domain |
|----------|-----------|--------|
| HP:0001263 | Global developmental delay | Neurodevelopmental |
| HP:0010864 | Severe intellectual disability | Neurodevelopmental |
| HP:0002300 | Mutism / absent speech | Speech |
| HP:0001270 | Motor delay | Motor |
| HP:0001252 | Hypotonia | Motor |
| HP:0001251 | Ataxia | Movement disorder |
| HP:0002451 | Limb dystonia | Movement disorder |
| HP:0001337 | Tremor | Movement disorder |
| HP:0000729 | Autistic behavior | Behavioral |
| HP:0000752 | Hyperactivity | Behavioral |
| HP:0000718 | Aggressive behavior | Behavioral |
| HP:0002360 | Sleep disturbance | Behavioral |
| HP:0011968 | Feeding difficulties | Systemic |
| HP:0033725 | Thin corpus callosum | Brain imaging |
| HP:0001321 | Cerebellar hypoplasia | Brain imaging |
| HP:0000365 | Hearing impairment | Sensory |

### Finding 4 — UBE3C/Hul5 is a proteasome processivity factor; mouse knockouts show neurobehavioral phenotypes

UBE3C (yeast ortholog **Hul5**) is one of ~5 ubiquitin ligases associated with the mammalian 26S proteasome; it enhances proteasomal processivity and cycles on/off the proteasome with the deubiquitinase Usp14/Ubp6 in response to ubiquitinated-substrate supply [PMID: 28396413].

> "the ubiquitin ligase, Ube3c/Hul5, which enhances proteasomal processivity" [PMID: 28396413]

Under proteotoxic stress (heat shock, arsenite, proteasome inhibition), Ube3c/Hul5 selectively polyubiquitinates the proteasome ubiquitin-receptor subunit **Rpn13**, reducing the proteasome's capacity to degrade ubiquitin conjugates — an autoinhibitory / stress-biomarker mechanism [PMID: 24811749].

> "Rpn13 becomes extensively and selectively poly-ubiquitinated by the proteasome-associated ubiquitin ligase, Ube3c/Hul5" [PMID: 24811749]

**IMPC** mouse *Ube3c*-null lines (mouse gene ID 100763) show neurobehavioral abnormalities — decreased prepulse inhibition, decreased locomotor/vertical activity, decreased exploration in a new environment, and abnormal gait — plus metabolic, cardiac, and immune findings, providing a model that partially recapitulates the human movement/behavioral phenotype.

### Finding 5 — Protein features and variant landscape

**UniProt Q15386** (UBE3C_HUMAN, 1083 aa): an E3 ubiquitin-protein ligase that catalyzes Lys-29- and Lys-48-linked polyubiquitin chains, accepts ubiquitin from the E2 enzyme **UBE2D1** as a thioester, and associates with the 26S proteasome to elongate ubiquitin chains on bound substrates. **ClinVar** contains ~257 *UBE3C* variant records; isolated single-nucleotide variants are predominantly **Uncertain Significance (VUS)** with a few Likely benign, whereas the "Pathogenic" entries at this locus are large 7q36 copy-number changes (contiguous-gene events) rather than isolated *UBE3C* point mutations. The disease-defining biallelic LoF alleles from PMID 36401616 are private/rare and not yet broadly deposited.

### Finding 6 — Pathway context and expression

Reactome maps UBE3C (Q15386) to **R-HSA-983168** "Antigen processing: Ubiquitination & Proteasome degradation" within the Class-I-MHC-mediated antigen-processing superpathway; relevant KEGG pathways are **hsa03050 (Proteasome)** and **hsa04120 (Ubiquitin-mediated proteolysis)**. UBE3C shows **low tissue specificity** (broad/ubiquitous expression, Human Protein Atlas) and is brain-expressed [PMID: 33182779]. No NEDASMB-specific transcriptomic, proteomic, metabolomic, or single-cell datasets exist; the only patient functional data are the RNA studies confirming the LoF effect [PMID: 36401616].

### Finding 7 — OMIM #620270 is the *UBE3C*-specific phenotype entry

NCBI Gene → OMIM linkage for *UBE3C* (GeneID 9690, 7q36.3) returns two records: **phenotype MIM 620270** (Neurodevelopmental disorder with absent speech and movement and behavioral abnormalities) and **gene MIM 614454** (*UBE3C*). MedGen concept **C5830319 (UID 1840955)** corresponds to the same phenotype. This confirms MONDO:0859519 = OMIM:620270 is the *UBE3C*-specific disorder, distinct from the paralog *HECTD4* phenotype reported in the same paper [PMID: 36401616].

---

## Section-by-Section Report

### 1. Disease Information

- **Overview:** NEDASMB is an ultra-rare autosomal-recessive neurodevelopmental disorder in which biallelic loss of the proteasome-associated E3 ubiquitin ligase *UBE3C* produces an Angelman-like syndrome of severe developmental delay, absent speech, movement disorder, seizures, and behavioral abnormalities.
- **Key identifiers:** OMIM phenotype **#620270**; gene MIM **614454**; **MONDO:0859519**; **MedGen C5830319 (UID 1840955)**; **UMLS C5830319**. No dedicated Orphanet or ICD-10/ICD-11 code exists yet. MeSH lacks a specific descriptor; the closest umbrella term is "Neurodevelopmental Disorders" (MeSH D065886).
- **Synonyms / alternative names:** NEDASMB; UBE3C-related neurodevelopmental disorder; Angelman-like syndrome due to UBE3C deficiency (informal).
- **Information source:** Aggregated disease-level resources (OMIM, MONDO, MedGen) built from a single primary clinical/genetic report [PMID: 36401616], i.e., individual-patient data from a small cohort rather than EHR-scale or registry data.

### 2. Etiology

- **Causal factor:** Purely genetic — biallelic (homozygous or compound-heterozygous) loss-of-function variants in *UBE3C* [PMID: 36401616]. No environmental, infectious, or toxic cause is implicated.
- **Genetic risk factors:** The causal variants are the *UBE3C* LoF alleles themselves. No susceptibility loci or modifier genes have been reported. As an autosomal-recessive disorder, **consanguinity** is a demographic risk factor, though this was not quantified.
- **Environmental risk / protective factors:** None identified — not applicable to a monogenic recessive disorder.
- **Gene–environment interactions:** None reported. *In vitro* and model-organism data show UBE3C activity is modulated by **proteotoxic stress** (heat shock, arsenite, proteasome inhibition) [PMID: 24811749], suggesting a theoretical stress-dependent modifier axis, but this has not been demonstrated in patients.

### 3. Phenotypes

The phenotype is Angelman-like and dominated by CNS features (see Finding 3 table for HPO terms). **Phenotype types** include behavioral changes (autistic behavior, hyperactivity, aggression, sleep disturbance), clinical/neurological signs (hypotonia, ataxia, dystonia, tremor, seizures), developmental manifestations (global developmental delay, severe intellectual disability, absent speech, motor delay), and structural brain findings (thin corpus callosum, cerebellar hypoplasia). **Onset** is congenital/infantile; **severity** is severe; **progression** is static (non-progressive encephalopathy); **frequency among affected individuals** cannot be reliably quantified given the tiny cohort (n = 3 for the *UBE3C*-specific phenotype). **Quality-of-life impact** is presumed profound (non-verbal, dependent for activities of daily living), but no formal QoL instrument data (EQ-5D, SF-36, PROMIS) exist for this disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** *UBE3C* (HGNC:16803; NCBI GeneID 9690; MIM 614454; ENSG00000009335; 7q36.3).
- **Pathogenic variants:** Biallelic LoF alleles (e.g., nonsense, frameshift, splice — consistent with the LoF mechanism confirmed by patient RNA studies) [PMID: 36401616]. In ClinVar, isolated *UBE3C* SNVs are mostly VUS; large 7q36 CNVs are catalogued as pathogenic contiguous-gene events. Population allele frequency of the disease alleles is very low/private (gnomAD constraint pLI = 1.0).
- **Origin:** Germline (autosomal recessive). No somatic role in this disease.
- **Functional consequence:** Loss of function (reduced/absent proteasome-associated E3 ligase activity).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None specifically defined for NEDASMB. Note that *UBE3A* (the paralog) is imprinted, but there is no evidence *UBE3C* is imprinted; NEDASMB follows classic biallelic recessive genetics rather than parent-of-origin effects.

### 5. Environmental Information

Not applicable — NEDASMB is a monogenic recessive disorder with **no known environmental, lifestyle, or infectious contributors**. Cellular studies show UBE3C responds to proteotoxic stressors [PMID: 24811749], but no environmental trigger has been linked to disease onset or severity in patients.

### 6. Mechanism / Pathophysiology

**Molecular pathway:** Ubiquitin–proteasome system (UPS). UBE3C is a proteasome-associated HECT E3 ligase that assembles **K48- and K29-linked polyubiquitin chains** [PMID: 25752577] using E2 UBE2D1, and enhances proteasome processivity as substrates are threaded into the 26S proteasome [PMID: 28396413]. Relevant pathways: Reactome R-HSA-983168; KEGG hsa03050 and hsa04120.

**Cellular process:** Regulated protein degradation / protein quality control (proteostasis). Loss of UBE3C is predicted to impair clearance of ubiquitinated neuronal substrates during a period when the neocortex requires "uninterrupted action of UBE3 ligases … for cortical circuit assembly" [PMID: 33182779].

**Protein dysfunction:** Loss-of-function — reduced catalytic output of the HECT domain (catalytic region aa 744–1083; C-terminal residues essential) [PMID: 32039437].

**Proposed causal chain:**

```
Biallelic UBE3C LoF variants
        │
        ▼
Loss of proteasome-associated E3 ligase activity
(reduced K48/K29 polyubiquitination; reduced proteasome processivity)
        │
        ▼
Impaired neuronal protein homeostasis (proteostasis)
during cortical & cerebellar circuit assembly
        │
        ▼
Aberrant neurodevelopment
(thin corpus callosum, cerebellar hypoplasia)
        │
        ▼
Clinical phenotype: severe DD/ID, absent speech,
movement disorder, seizures, behavioral abnormalities
```

Upstream event = loss of UBE3C enzymatic function; downstream events = disrupted proteostasis → aberrant circuit assembly → clinical manifestations. **Cell types involved:** cortical and cerebellar neurons (CL:0000540 neuron; CL:0000121 Purkinje cell — inferred from cerebellar hypoplasia). **GO terms:** GO:0016567 protein ubiquitination; GO:0000209 protein polyubiquitination; GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process; GO:0007420 brain development; GO:0021987 cerebral cortex development. **CHEBI:** ubiquitin conjugate / ATP (cofactors for proteasomal degradation).

**Immune / metabolic / other:** UBE3C also functions in innate immunity (HECT-ligase regulation of type-I IFN) and cancer metastasis [PMID: 32039437; PMID: 21167755], but these are not established components of NEDASMB pathophysiology. No disease-specific metabolomic, proteomic, transcriptomic, or single-cell profiling of patient tissue exists.

### 7. Anatomical Structures Affected

- **Organ / system:** Central nervous system (nervous system; UBERON:0001016). Primary site = brain (UBERON:0000955), with imaging evidence pointing to the **corpus callosum** (UBERON:0002336; thin) and **cerebellum** (UBERON:0002037; hypoplasia). Sensory involvement includes hearing impairment (auditory pathway).
- **Tissue / cell level:** Nervous tissue; cortical and cerebellar neurons (CL:0000540; CL:0000121 Purkinje cell).
- **Subcellular level:** Cytoplasm and 26S proteasome (GO:0000502 proteasome complex; GO:0005829 cytosol); UBE3C associates with the proteasome and cycles on/off it [PMID: 28396413].
- **Lateralization:** Bilateral/symmetric CNS involvement (consistent with a diffuse genetic encephalopathy).

### 8. Temporal Development

- **Onset:** Congenital/infantile; developmental delay evident from early infancy.
- **Onset pattern:** Chronic/insidious (developmental).
- **Progression:** Static (non-progressive) encephalopathy; no evidence of regression in the reported cohort. Seizures and behavioral features persist across childhood.
- **Duration:** Chronic, lifelong.
- **Critical periods:** Prenatal/early-postnatal cortical and cerebellar circuit assembly is the mechanistically implicated vulnerable window [PMID: 33182779]; there is no defined therapeutic window because no disease-modifying therapy exists.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic LoF) [PMID: 36401616].
- **Epidemiology:** Prevalence and incidence are **undefined** (ultra-rare; ~3 patients reported for the *UBE3C*-specific phenotype). Not in Orphanet/GBD with a prevalence estimate.
- **Penetrance / expressivity:** Presumed high penetrance for biallelic LoF, but formal penetrance and the range of expressivity cannot be estimated from n = 3.
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** Recessive inheritance implies consanguinity or shared ancestry may raise risk; no founder allele has been formally established.
- **Carrier frequency:** Not established; expected to be very low given gnomAD constraint.
- **Sex ratio / age / geographic distribution:** Not established.

### 10. Diagnostics

- **Primary diagnostic modality:** **Exome sequencing (WES)** or **genome sequencing (WGS)**, which identified the causal variants; chromosomal analysis was also used in the discovery cohort [PMID: 36401616]. Because the phenotype overlaps Angelman syndrome, the recommended workup first **excludes *UBE3A*/15q11–q13 defects** (methylation analysis, UBE3A sequencing, chromosomal microarray) before attributing disease to *UBE3C*.
- **Confirmatory testing:** Bi-allelic *UBE3C* LoF variants with segregation; patient **RNA studies** confirmed the LoF effect and are a useful functional adjunct [PMID: 36401616].
- **Imaging:** Brain MRI may reveal thin corpus callosum and cerebellar hypoplasia (supportive, not specific).
- **Electrophysiology:** EEG for seizure characterization (as in Angelman-like disorders, though no NEDASMB-specific EEG signature is defined).
- **Biomarkers / omics diagnostics:** No validated blood, CSF, metabolomic, or proteomic biomarker. No newborn-screening test.
- **Clinical criteria / differential diagnosis:** No formal diagnostic criteria. Differential diagnosis includes **Angelman syndrome (*UBE3A*)**, and other severe DD/ID-absent-speech-behavioral syndromes such as *MEF2C* haploinsufficiency [PMID: 27255693], *ACTL6B*-related disorder [PMID: 39275948], *CTNNB1* syndrome [PMID: 36293418], *KMT5B*-related disorder [PMID: 37927187], and *SYT1*-related disorder [PMID: 38058756]. Genetic testing distinguishes these.

### 11. Outcome / Prognosis

- **Survival / mortality:** No mortality or life-expectancy data reported. The disorder appears to be a chronic static encephalopathy compatible with survival into at least adolescence/adulthood, but this is not quantified.
- **Morbidity / disability:** Profound — non-verbal, severe intellectual disability, motor impairment, dependence for daily activities; seizures and behavioral disturbance add morbidity.
- **Recovery / prognostic factors / prognostic biomarkers:** None defined. Given static course and supportive-only management, meaningful recovery is not expected. No QoL instrument data exist.

### 12. Treatment

- **Disease-modifying therapy:** **None exists.** Management is entirely **supportive and symptomatic**.
- **Symptomatic pharmacotherapy (by analogy to Angelman-like disorders):** Anti-seizure medications for epilepsy; agents for sleep disturbance; behavioral/ADHD management as needed. No pharmacogenomic guidance is specific to *UBE3C*. (NCIT: C15607 Anticonvulsant Therapy; C15632 Supportive Care.)
- **Rehabilitative / supportive care:** Physical therapy, occupational therapy, speech/AAC (augmentative and alternative communication) for non-verbal individuals, feeding support for feeding difficulties. AAC design research in intellectual and developmental disabilities is relevant to communication support [PMID: 29710313]. (NCIT: C15315 Physical Therapy; C15258 Rehabilitation Therapy.)
- **Advanced / experimental therapeutics:** None reported; no gene therapy, ASO, or targeted therapy in trials for NEDASMB. No ClinicalTrials.gov entries were identified for this specific disorder.

### 13. Prevention

- **Primary prevention:** Not applicable (genetic disorder). **Genetic counseling** for at-risk families is the principal preventive intervention: recessive recurrence risk of 25% per pregnancy for carrier couples.
- **Screening / early detection:** **Carrier screening** and, where a familial variant is known, **cascade testing**, **prenatal diagnosis**, or **preimplantation genetic testing (PGT-M)** are options. No population-level or newborn screening exists.
- **Public-health / behavioral / immunization measures:** Not applicable.

### 14. Other Species / Natural Disease

- **Orthologs:** Yeast *HUL5* (functional ortholog, processivity factor) [PMID: 28396413]; mouse *Ube3c* (NCBI Gene 100763); *C. elegans* ortholog shows synaptic-transmission phenotypes when UBE3C is reduced (PMID 36380488, investigation notes).
- **Natural disease in other species:** No naturally occurring *UBE3C*-related disease is catalogued in OMIA for companion animals or wildlife.
- **Comparative biology:** UBE3C function (proteasome-associated processivity, K48/K29 chain assembly) is conserved from yeast to human, supporting cross-species mechanistic study.
- **Zoonotic potential:** Not applicable.

### 15. Model Organisms

| Model | System | Phenotype recapitulation | Reference |
|-------|--------|--------------------------|-----------|
| Mouse *Ube3c*-null (IMPC, gene 100763) | Mammalian, knockout | Neurobehavioral: ↓prepulse inhibition, ↓locomotor/vertical activity, ↓exploration, abnormal gait; plus metabolic/cardiac/immune findings | IMPC |
| *C. elegans* (UBE3C reduction) | Invertebrate | Synaptic-transmission deficits; heat-stress susceptibility (proteostasis) | PMID: 36380488 |
| *S. cerevisiae* *hul5Δ* | Yeast | Loss of proteasome processivity; stress-dependent Rpn13 ubiquitination biology | PMID: 28396413; PMID: 24811749 |

- **Genetic model types available:** Knockout mouse (IMPC); worm and yeast loss-of-function.
- **Model limitations:** No published mouse model engineered with a patient-specific biallelic LoF allele or assessed against the full human cognitive/speech/seizure phenotype; behavioral endophenotypes only partially map to human features. No iPSC-derived neuron or organoid model of NEDASMB has been reported.
- **Applications:** Existing models are well suited to dissecting UBE3C's role in proteasome processivity and stress-responsive proteostasis, providing a mechanistic bridge to the human disorder.

---

## Mechanistic Model / Interpretation

NEDASMB is best understood as a **"UBE3-family" neurodevelopmental proteostasis disorder**, sitting alongside its paralogs:

| Gene | Disorder | Inheritance | Shared features |
|------|----------|-------------|-----------------|
| *UBE3A* | Angelman syndrome | Maternal deletion/LoF (imprinted) | Severe ID, absent speech, movement disorder, seizures, behavioral phenotype |
| *UBE3B* | Kaufman oculocerebrofacial syndrome | Autosomal recessive | ID, developmental abnormalities |
| ***UBE3C*** | **NEDASMB (this disorder)** | **Autosomal recessive (biallelic LoF)** | **Severe DD/ID, absent speech, movement disorder, seizures, behavioral abnormalities** |

The unifying biology is that **HECT-type UBE3 E3 ligases are required for cortical circuit assembly and higher cognition** [PMID: 33182779]. UBE3C's specific niche is the **proteasome**: it is a processivity-enhancing ligase [PMID: 28396413] that builds K48/K29 chains [PMID: 25752577] and, under stress, regulates proteasome capacity by ubiquitinating Rpn13 [PMID: 24811749]. Biallelic loss therefore degrades neuronal protein-quality-control capacity precisely when the developing brain is most dependent on it, yielding a static but severe encephalopathy. The paralog-directed discovery strategy — screening Angelman-like patients for *UBE3C* because it is *UBE3A*'s paralog — is itself strong circumstantial evidence for shared pathobiology and "explains some of the missing heritability" in Angelman-negative patients [PMID: 36401616].

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [PMID: 36401616](https://pubmed.ncbi.nlm.nih.gov/36401616/) | *Biallelic variants in HECT E3 paralogs HECTD4 and UBE3C cause NDDs overlapping Angelman syndrome* | **Primary disease-defining paper.** Establishes gene, inheritance, LoF mechanism, phenotype, discovery strategy |
| [PMID: 33182779](https://pubmed.ncbi.nlm.nih.gov/33182779/) | *Molecular evolution, neurodevelopmental roles and clinical significance of HECT-type UBE3 ligases* | Frames UBE3-family requirement for cortical development/cognition |
| [PMID: 32039437](https://pubmed.ncbi.nlm.nih.gov/32039437/) | *Crystal structure of HECT domain of UBE3C E3 ligase* | Enzyme class, catalytic domain, autoubiquitination, cellular roles |
| [PMID: 25752577](https://pubmed.ncbi.nlm.nih.gov/25752577/) | *Assembly and recognition of K29-/K33-linked polyubiquitin* | UBE3C chain-linkage specificity (K48/K29) |
| [PMID: 28396413](https://pubmed.ncbi.nlm.nih.gov/28396413/) | *Ubiquitinated proteins promote proteasome association of Usp14 and Ube3c* | UBE3C/Hul5 as proteasome processivity factor |
| [PMID: 24811749](https://pubmed.ncbi.nlm.nih.gov/24811749/) | *Autoubiquitination of 26S proteasome on Rpn13* | Stress-responsive substrate (Rpn13) and proteostasis regulation |
| [PMID: 17848870](https://pubmed.ncbi.nlm.nih.gov/17848870/) | *Angelman syndrome revisited* | Defines the Angelman phenotype the disorder overlaps |
| [PMID: 25752573](https://pubmed.ncbi.nlm.nih.gov/25752573/) | *K29-selective ubiquitin binding domain* | Confirms UBE3C generates K29 chains |
| [PMID: 28425671](https://pubmed.ncbi.nlm.nih.gov/28425671/) | *Activity-based probes for HECT E3 ligases* | Confirms endogenous UBE3C catalytic activity |
| [PMID: 21167755](https://pubmed.ncbi.nlm.nih.gov/21167755/) | *HECT E3 ligase RAUL regulates type-I IFN* | Context for HECT-ligase immune roles (not disease-specific) |
| [PMID: 27255693](https://pubmed.ncbi.nlm.nih.gov/27255693/) | *MEF2C haploinsufficiency syndrome* | Differential diagnosis |
| [PMID: 39275948](https://pubmed.ncbi.nlm.nih.gov/39275948/) | *ACTL6B-related brain disorders* | Differential diagnosis (severe DD/ID, absent speech) |
| [PMID: 36293418](https://pubmed.ncbi.nlm.nih.gov/36293418/) | *CTNNB1 syndrome* | Differential diagnosis |
| [PMID: 37927187](https://pubmed.ncbi.nlm.nih.gov/37927187/) | *KMT5B-related NDD* | Differential diagnosis |
| [PMID: 38058756](https://pubmed.ncbi.nlm.nih.gov/38058756/) | *SYT1-related disorder* | Differential diagnosis (synaptopathy) |
| [PMID: 31400086](https://pubmed.ncbi.nlm.nih.gov/31400086/) | *Mosaic Angelman syndrome* | Phenotypic spectrum context |
| [PMID: 29710313](https://pubmed.ncbi.nlm.nih.gov/29710313/) | *Gaze/AAC in IDD* | Communication-support relevance |

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** The *UBE3C*-specific phenotype rests on **three patients from two families** in a single 2023 report [PMID: 36401616]. All prevalence, penetrance, expressivity, sex ratio, and natural-history parameters are therefore **undefined**.
2. **No disease-specific omics.** There are no NEDASMB transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial datasets; the only patient functional data are RNA studies confirming the LoF effect.
3. **Variant classification lag.** ClinVar contains mostly VUS for isolated *UBE3C* SNVs; the disease alleles are private and not broadly deposited, complicating clinical interpretation.
4. **Mechanism is inferential.** The proteostasis → cortical-development causal chain is well supported for the UBE3 family and UBE3C biochemistry, but a **direct demonstration in patient-relevant neurons** (e.g., iPSC-derived) is lacking.
5. **No dedicated Orphanet/ICD code**, no formal diagnostic criteria, no QoL data, and no prognostic or treatment data specific to the disorder.
6. **Model gap.** No mouse model carries a patient-specific biallelic LoF allele evaluated against the full human phenotype; no organoid/iPSC model exists.

---

## Proposed Follow-up Experiments / Actions

1. **Cohort expansion via GeneMatcher / Matchmaker Exchange** to identify additional biallelic *UBE3C* families, enabling estimation of penetrance, expressivity, natural history, and genotype–phenotype correlation.
2. **Patient iPSC-derived cortical neurons / cerebral organoids** to test the proteostasis hypothesis directly: measure proteasome processivity, K48/K29 ubiquitin-conjugate accumulation, and neuronal maturation/synaptic phenotypes in UBE3C-null vs. isogenic control.
3. **Deep-phenotype mouse *Ube3c*-null lines** (beyond IMPC screen) — cognition, seizure susceptibility (EEG), motor/cerebellar function, corpus-callosum morphometry — to establish a validated model.
4. **Functional variant classification pipeline** (e.g., ubiquitination assays with activity-based probes [PMID: 28425671]) to reclassify *UBE3C* VUS and support ClinVar submissions.
5. **Standardize the disorder in ontologies:** propose an Orphanet entry and ICD-11 mapping; enrich HPO annotations with frequency data as the cohort grows.
6. **Proteomic/ubiquitinome profiling** of patient-derived cells to define the UBE3C-dependent substrate landscape in neurons and nominate candidate biomarkers.
7. **Genetic-counseling resources** for affected families, including carrier-screening and reproductive-option (PGT-M/prenatal) guidance.

---

*Report compiled from 7 confirmed findings, 17 reviewed papers, and ontology/database cross-mapping (OMIM, MONDO, MedGen, HGNC, UniProt, Reactome, KEGG, ClinVar, gnomAD, IMPC) across 5 investigation iterations.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Absent_Speech_And_Movement_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Absent_Speech_And_Movement_And_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33182779` *(abstract only)*: "uninterrupted action of UBE3 ligases … for cortical circuit assembly"
  - closest text in source: "Particularly, we highlight that uninterrupted action of UBE3 ligases is a sine qua non for cortical circuit assembly and higher cognitive functions of the neocortex."