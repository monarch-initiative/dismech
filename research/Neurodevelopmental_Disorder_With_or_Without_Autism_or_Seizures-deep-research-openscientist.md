---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-18T15:13:39.245657'
end_time: '2026-08-18T15:32:06.454925'
duration_seconds: 1107.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder With or Without Autism or Seizures
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
citation_count: 14
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 16
  on_topic: 6
  off_topic: 2
  off_topic_references:
  - PMID:42609138
  - PMID:42446772
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_or_Without_Autism_or_Seizures-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_or_Without_Autism_or_Seizures-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With or Without Autism or Seizures
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With or Without Autism or Seizures** covering all of the
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

# Neurodevelopmental Disorder With or Without Autism or Seizures (NEDAUS): A Comprehensive Disease Characteristics Report

**Disease:** Neurodevelopmental Disorder With or Without Autism or Seizures (NEDAUS)
**MONDO ID:** MONDO:0030994 · **OMIM:** #619239 · **Causal gene:** *CUL3* (HGNC:2553)
**Category:** Mendelian (autosomal dominant, syndromic neurodevelopmental disorder)

---

## Summary

Neurodevelopmental disorder with or without autism or seizures (NEDAUS) is a rare, autosomal-dominant, syndromic neurodevelopmental disorder caused by heterozygous — and predominantly *de novo* — loss-of-function (LoF) variants in **CUL3**, the gene encoding Cullin-3, the scaffold subunit of the Cullin-3 RING E3 ubiquitin-ligase (CRL3) complexes. The disorder maps to **MONDO:0030994 / OMIM #619239** and is classified as a Mendelian neurodevelopmental disorder. Its clinical hallmark is global developmental delay and intellectual disability (nearly constant), accompanied by variable autism spectrum features and epilepsy — frequently infantile spasms with hypsarrhythmia — hence the descriptive name "with or without autism or seizures."

The mechanistic basis is **haploinsufficiency**. A single functional *CUL3* allele produces roughly half the normal amount of Cullin-3 scaffold, reducing the ubiquitin-ligase activity of the ~180 CRL3 complexes that depend on it. This was demonstrated directly in patient-derived cells: reduced ubiquitin–protein conjugates and failure to degrade the canonical CRL3 substrate **4E-BP1 (EIF4EBP1)**, a regulator of mTOR–eIF4E cap-dependent translation ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)). A parallel substrate axis — **RhoA**, controlled via KCTD13/BACURD adaptors — governs actin cytoskeletal dynamics, neuronal migration, and dendritic growth; a *Cul3*-haploinsufficient mouse recapitulates social/cognitive deficits and reduced cortical volume, and pharmacologic RhoA inhibition rescues the dendritic and network-activity phenotypes ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/)). *CUL3* is one of the most loss-of-function-intolerant genes in the human genome (gnomAD pLI ≈ 1.0, LOEUF 0.31), fully consistent with a haploinsufficiency disease model.

There is currently **no disease-specific therapy**; management is symptomatic and supportive (antiseizure medication, developmental/behavioral therapies, and management of feeding and structural anomalies). The mechanistic work does, however, nominate **RhoA and the mTOR–eIF4E translational axis** as rational future therapeutic targets. Notably, a mechanistically distinct allelic disorder — pseudohypoaldosteronism type IIE / familial hyperkalemic hypertension (OMIM #614496) — is caused by *CUL3* exon-9-skipping variants acting through a dominant-negative mechanism, and must be distinguished from the LoF-driven neurodevelopmental disorder.

---

## Key Findings

### Finding 1 — Disease identity and identifiers (F001)

NEDAUS is a *CUL3*-related autosomal-dominant neurodevelopmental disorder. The Monarch/MONDO graph maps **MONDO:0030994** (synonym NEDAUS) to **OMIM:619239**, **DOID:0061147**, **GARD:0018540**, **UMLS:C5543225**, and **MedGen:1784023**. The disease is associated causally with **HGNC:2553 (CUL3)** and mode of inheritance **HP:0000006 (autosomal dominant)**, and is a subclass of MONDO:0100500 (Mendelian disease). Core HPO annotations returned for the disease include:

| Phenotype | HPO term |
|---|---|
| Seizure | HP:0001250 |
| Autistic behavior | HP:0000729 |
| Delayed speech and language development | HP:0000750 |
| Motor delay | HP:0001270 |
| Intellectual disability, mild → severe | HP:0001256 / HP:0010864 |
| Infantile spasms | HP:0012469 |
| Hypsarrhythmia | HP:0002521 |
| Microcephaly | HP:0000252 |
| Failure to thrive | HP:0001508 |

**Synonyms / alternative names:** Neurodevelopmental disorder with or without autism or seizures; NEDAUS; CUL3-related neurodevelopmental disorder; CUL3 haploinsufficiency syndrome. Information is derived from **aggregated, disease-level resources** (OMIM, MONDO, HPO curation) plus published multi-center patient cohorts — not from a single EHR system.

### Finding 2 — CUL3 loss-of-function causes syndromic NDD via haploinsufficiency; 4E-BP1 accumulates (F002)

The largest cohort assembled to date comprised **37 individuals with heterozygous *CUL3* variants** — 35 with LoF variants and 2 with missense variants — presenting a syndromic NDD characterized by intellectual disability with or without autistic features ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)). The authors verified the mechanism in patient-derived T-cells:

> "We assembled a cohort of 37 individuals with heterozygous CUL3 variants presenting a syndromic NDD characterized by intellectual disability with or without autistic features. Of these, 35 have loss-of-function (LoF) and 2 have missense variants." ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/))

> "Notably, we show that 4E-BP1 (EIF4EBP1), a prominent substrate of CUL3, fails to be targeted for proteasomal degradation in patient-derived cells." ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/))

Patient cells showed **decreased ubiquitin–protein conjugates**, confirming that reduced CUL3 dosage translates into reduced global CRL3 E3-ligase output, with the substrate 4E-BP1 accumulating rather than being degraded. Haploinsufficiency via LoF is therefore the predominant pathogenic mechanism.

### Finding 3 — Mouse model: RhoA/cytoskeletal signaling and cortical neurogenesis (F003)

A CRISPR-engineered *Cul3*-haploinsufficient mouse recapitulates the human phenotype and pinpoints a causal substrate ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/)):

> "Cul3 mutant mice exhibited social and cognitive deficits and hyperactive behavior. Brain MRI found decreased volume of cortical regions." ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/))

Multi-omic profiling implicated neurogenesis and cytoskeletal defects; dendritic growth, filamentous-actin puncta, and spontaneous network activity were all reduced. Critically, the phenotype was pharmacologically reversible:

> "Inhibition of small GTPase RhoA, a molecular substrate of Cul3 ligase, rescued dendrite length and network activity phenotypes." ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/))

This establishes **RhoA** as a mechanistically causal, druggable node downstream of *CUL3* loss.

### Finding 4 — Extreme LoF intolerance and the distinct allelic hypertension disorder (F004)

gnomAD constraint metrics for *CUL3* (ENSG00000036257, chromosome 2) place it among the most intolerant genes in the genome: **pLI = 1.0**, observed/expected LoF (oe_lof) = 0.213 (95% CI 0.149–0.313; **LOEUF = 0.31**), observed LoF 19 vs expected 89.1, LoF Z = 6.30, and strong missense constraint (missense Z = 6.58). This severe intolerance is exactly what a haploinsufficiency model predicts and provides the population-genetic underpinning for ACMG PVS1-level pathogenicity of null variants.

Importantly, a **mechanistically distinct allelic disorder** exists: pseudohypoaldosteronism type IIE / familial hyperkalemic hypertension (OMIM #614496) is caused by *CUL3* **exon-9-skipping** variants producing an internal deletion of residues 403–459 (CUL3-Δ9):

> "Cul3 mutations cause skipping of exon 9, which results in an internal deletion of 57 amino acids from the CUL3 protein (CUL3-∆9)." ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/))

CUL3-Δ9 acts by a **dominant-negative** mechanism on the renal KLHL3–WNK-kinase degradation axis — **not** haploinsufficiency — and produces hypertension/hyperkalemia rather than neurodevelopmental disease. This dichotomy is essential for correct variant interpretation.

### Finding 5 — Phenotype spectrum and HPO frequencies (F005)

Curated HPO annotations for OMIM:619239 (source PMIDs 30311385, 32341456, 31696658) plus the Blackburn 2024 cohort (n = 37) yield a frequency-stratified phenotype profile:

| Frequency tier | Phenotype (HPO) |
|---|---|
| **Constant / near-constant** | Global developmental delay incl. delayed speech/language (HP:0000750, 5/5); delayed sitting (HP:0025336, 3/3) and walking (HP:0031936, 3/3); motor delay (HP:0001270); intellectual disability, mild→severe (HP:0001256 / HP:0010864); infantile onset (HP:0003593, 3/3) |
| **Frequent** | Autistic behavior (HP:0000729); seizures (HP:0001250, 2/3) incl. infantile spasms (HP:0012469, 2/3) with hypsarrhythmia (HP:0002521) and EEG burst suppression (HP:0010851); tonic seizures (HP:0032792); hyperactivity/ADHD (HP:0000752); delayed CNS myelination (HP:0002188); feeding difficulties (HP:0011968); failure to thrive (HP:0001508) |
| **Variable / less common** | Microcephaly (HP:0000252); dysmorphic facial features (GestaltMatcher-analyzed); submucous cleft palate (HP:0000176); bifid uvula (HP:0000193); atrial septal defect (HP:0001631); pulmonic stenosis (HP:0001642); absent thumb (HP:0009777) |

The **quality-of-life impact** is substantial and lifelong, driven principally by intellectual disability, communication impairment, epilepsy, and feeding difficulty — features that require multidisciplinary developmental, educational, and medical support. Autism-associated motor and feeding difficulties (well documented in the broader ASD literature, e.g. [PMID: 42608985](https://pubmed.ncbi.nlm.nih.gov/42608985/), [PMID: 42609138](https://pubmed.ncbi.nlm.nih.gov/42609138/)) compound daily-functioning burden.

### Finding 6 — CUL3/CRL3 substrate-adaptor network links NEDAUS to multiple neuronal pathways (F006)

CUL3 is the scaffold of Cullin-3 RING E3 ligases (CRL3s), which use ~180 BTB/Kelch (KLHL/KCTD) substrate adaptors to recognize hundreds of substrates. The brain-relevant CRL3 axes documented in the literature are:

1. **RhoA** (via BACURD/KCTD13/TNFAIP1 adaptors) — actin cytoskeleton, neuronal migration, dendrite growth ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/); [PMID: 26969432](https://pubmed.ncbi.nlm.nih.gov/26969432/)).
2. **4E-BP1/EIF4EBP1** — cap-dependent translation / mTOR–eIF4E ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)).
3. **KEAP1–NRF2 (NFE2L2)** — antioxidant / oxidative-stress response ([PMID: 42446772](https://pubmed.ncbi.nlm.nih.gov/42446772/); [PMID: 37328017](https://pubmed.ncbi.nlm.nih.gov/37328017/)).
4. **KLHL3–WNK kinase** — renal ion homeostasis, relevant to the allelic hypertension disorder ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/)).

The 16p11.2 CNV adaptor **KCTD13** converges on the CUL3–RhoA axis ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/)), tying NEDAUS mechanistically to one of the most common autism-associated copy-number syndromes.

### Finding 7 — ClinVar variant landscape (F007)

ClinVar returns **727 total *CUL3* variant records**, of which **226 are classified pathogenic or likely-pathogenic**. These P/LP records encompass both (a) the NDD-associated whole-gene loss-of-function alleles (nonsense, frameshift, splice-site, and larger deletions; germline, typically *de novo*) and (b) the mechanistically distinct exon-9-skipping alleles causing familial hyperkalemic hypertension (OMIM #614496). Variant interpretation follows ACMG/AMP guidelines; null variants readily meet **PVS1** given CUL3's strong LoF intolerance.

### Finding 8 — Cross-species conservation of the CUL3/KCTD13 social-behavior axis (F008)

Outbred rat models of the 16p11.2 deletion and duplication (Sprague-Dawley and Long-Evans backgrounds) display convergent social-behavior and novel-object deficits, with altered MAPK1 and CUL3 pathways and male-biased sexual dimorphism ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/)):

> "Altogether, the consequences of the 16p11.2 genetic region dosage on social behavior are now found in three different species: humans, mice and rats." ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/))

> "Interestingly major pathways affecting MAPK1 and CUL3 were found altered in the rat 16p11.2 models with additional changes in males compared to females." ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/))

Together with the *Cul3*-haploinsufficient mouse ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/)) and the human cohort ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)), this demonstrates conservation of the CUL3/KCTD13–RhoA social-behavior circuit across humans, mice, and rats.

### Finding 9 — Consolidated causal chain (F009)

Integrating all findings, the causal chain runs from a single germline variant to the clinical syndrome (detailed in the Mechanistic Model below): heterozygous *de novo* *CUL3* LoF → ~50% reduced CUL3 → decreased CRL3 activity → accumulation of substrates 4E-BP1 and RhoA → impaired neurogenesis, migration, dendritic growth, and network activity → reduced cortical volume and delayed myelination → developmental delay/intellectual disability with variable autism and epilepsy. Inheritance is autosomal dominant with essentially complete penetrance but **highly variable expressivity**; the disorder is ultra-rare, and management is symptomatic only.

---

## Mechanistic Model / Interpretation

```
   Heterozygous de novo CUL3 loss-of-function variant
   (nonsense / frameshift / splice / deletion; 35/37 LoF)
   gnomAD pLI ≈ 1.0, LOEUF 0.31  →  no tolerance for haploinsufficiency
                     │
                     ▼
        ~50% reduction in CUL3 scaffold protein
                     │
                     ▼
   Reduced Cullin-3 RING E3 ligase (CRL3) activity
   (↓ ubiquitin–protein conjugates in patient T-cells)
                     │
        ┌────────────┴─────────────┐
        ▼                          ▼
  4E-BP1 (EIF4EBP1)            RhoA  (via KCTD13/
  fails to be degraded         BACURD/TNFAIP1 adaptors)
        │                          │
        ▼                          ▼
  Dysregulated mTOR–eIF4E      Disrupted actin cytoskeleton,
  cap-dependent translation    neuronal migration, dendrite growth
        └────────────┬─────────────┘
                     ▼
   Impaired cortical neurogenesis & neuronal network activity
                     ▼
   ↓ Cortical volume · delayed CNS myelination (mouse MRI + human)
                     ▼
   Global developmental delay / intellectual disability
   + variable autism (HP:0000729) + epilepsy / infantile spasms (HP:0012469)
```

**Upstream vs downstream.** The initiating (upstream) event is CUL3 dosage reduction and consequent global loss of CRL3 ubiquitination capacity. The substrate-accumulation steps (4E-BP1, RhoA) are proximate downstream effectors; cytoskeletal/translational dysregulation and impaired neurogenesis are intermediate; reduced cortical volume and the clinical neurodevelopmental phenotype are the most distal outputs.

**Cell types and processes.** Affected cell types include cortical projection neurons (CL:0000598), neural progenitor/radial-glia populations (CL:0000047), and layer II/III pyramidal neurons whose positioning and dendritic maturation depend on KCTD13/TNFAIP1–Rnd signaling ([PMID: 26969432](https://pubmed.ncbi.nlm.nih.gov/26969432/)). Relevant GO biological processes: **protein polyubiquitination (GO:0000209)**, **proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161)**, **neuron migration (GO:0001764)**, **dendrite development (GO:0016358)**, **cerebral cortex development (GO:0021987)**, and **regulation of Rho protein signal transduction (GO:0035023)**. Subcellular compartments: **cytosol (GO:0005829)**, **Cul3-RING ubiquitin ligase complex (GO:0031463)**, and the actin cytoskeleton. Primary anatomy: cerebral cortex (**UBERON:0000956**), with brain (**UBERON:0000955**) and the nervous system broadly affected.

---

## Section-by-Section Report

### 1. Disease Information
NEDAUS is a rare Mendelian syndromic neurodevelopmental disorder defined by developmental delay/intellectual disability with variable autism and seizures. **Identifiers:** MONDO:0030994; OMIM #619239; DOID:0061147; GARD:0018540; UMLS:C5543225; MedGen:1784023. No dedicated Orphanet code or ICD-10/11 code is specific to NEDAUS; it is captured under broad NDD/intellectual-disability categories. **Synonyms:** CUL3-related NDD; CUL3 haploinsufficiency syndrome. Data are from disease-level curation and published cohorts.

### 2. Etiology
**Primary cause:** genetic — heterozygous, mostly *de novo* loss-of-function variants in *CUL3*. **Genetic risk:** the causal LoF variant itself; *CUL3* is a defined haploinsufficient gene (pLI ≈ 1.0). No confirmed environmental risk, protective, or gene–environment-interaction factors are established for this Mendelian disorder; disease is essentially fully determined by the causal variant with variable expressivity. Sex may modulate expression (male-biased effects seen in rat 16p11.2/CUL3-pathway models, [PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/)), but this is not established in humans for NEDAUS specifically.

### 3. Phenotypes
See Finding 5 for the full frequency-stratified table and HPO terms. Phenotype types span **behavioral changes** (autism HP:0000729, hyperactivity HP:0000752), **neurological signs** (seizures HP:0001250, infantile spasms HP:0012469, hypotonia), **cognitive/developmental** (intellectual disability HP:0001256/HP:0010864, delayed speech HP:0000750), **structural/physical** (microcephaly HP:0000252, palatal anomalies HP:0000176/HP:0000193, congenital heart defects HP:0001631/HP:0001642), and **EEG laboratory abnormalities** (hypsarrhythmia HP:0002521, burst suppression HP:0010851). Onset is infantile/congenital; severity is variable (mild to severe); course is generally stable/non-progressive (a static encephalopathy) with epilepsy that may be episodic.

### 4. Genetic / Molecular Information
**Causal gene:** *CUL3* (HGNC:2553; OMIM *603136; Ensembl ENSG00000036257; chromosome 2q36.2). **Variant classes:** predominantly nonsense, frameshift, canonical splice-site, and gene/exon deletions (LoF); rare missense. In the largest cohort, 35/37 were LoF ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)). **ClinVar:** 226 P/LP of 727 records (Finding 7). **Allele frequency:** causal alleles are absent/ultra-rare in gnomAD, consistent with strong constraint. **Origin:** germline, typically *de novo*. **Functional consequence:** loss of function → haploinsufficiency. **Distinct allelic mechanism:** exon-9-skipping CUL3-Δ9 → dominant-negative → hypertension disorder ([PMID: 29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/), [PMID: 32619053](https://pubmed.ncbi.nlm.nih.gov/32619053/), [PMID: 35563538](https://pubmed.ncbi.nlm.nih.gov/35563538/)). **Modifier genes / epigenetics:** not specifically defined for NEDAUS; substrate-adaptor genes (KCTD13, KLHL family) are mechanistic partners. **Chromosomal abnormalities:** 16p11.2 CNVs (containing KCTD13) converge on the same CUL3–RhoA pathway ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/)).

### 5. Environmental Information
No environmental, lifestyle, or infectious agents are established as causes or triggers. This is a monogenic disorder.

### 6. Mechanism / Pathophysiology
Detailed in the Mechanistic Model section and Findings 2, 3, 6, 9. **Molecular pathways:** ubiquitin–proteasome system (CRL3), mTOR–eIF4E cap-dependent translation (via 4E-BP1), Rho-GTPase/actin signaling (via RhoA/KCTD13), and KEAP1–NRF2 oxidative-stress response. **Cellular processes:** cortical neurogenesis, neuronal migration, dendritic maturation, network-activity formation. **Protein dysfunction:** loss of scaffold function → reduced substrate ubiquitination → substrate accumulation. **Transcriptomic/multi-omic** dysregulation of neurogenesis and cytoskeletal programs is documented in the mouse model ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/)).

### 7. Anatomical Structures Affected
**Primary organ:** brain (UBERON:0000955), specifically cerebral cortex (UBERON:0000956) with reduced volume and delayed myelination (HP:0002188). **Body system:** central nervous system (nervous). **Secondary involvement:** cardiovascular (septal defects), craniofacial/palate, and occasionally limb. **Cell types (CL):** cortical projection neurons (CL:0000598), neural progenitors (CL:0000047), pyramidal neurons. **Subcellular (GO CC):** cytosol (GO:0005829), Cul3-RING ligase complex (GO:0031463). **Lateralization:** bilateral/generalized CNS involvement.

### 8. Temporal Development
**Onset:** congenital/infantile (HP:0003593). **Course:** static (non-progressive) neurodevelopmental encephalopathy; epilepsy may be episodic and infantile spasms have a characteristic early-infancy window. **Critical period:** early cortical development (fetal/early postnatal neurogenesis and migration) is the mechanistically vulnerable window, consistent with the mouse MRI finding of decreased cortical volume from early postnatal development. **Duration:** chronic, lifelong.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant (HP:0000006), predominantly *de novo*. **Penetrance:** essentially complete for the neurodevelopmental phenotype; **expressivity highly variable**. **Epidemiology:** ultra-rare; precise prevalence/incidence not established (fewer than ~50 published patients). **Sex ratio:** not firmly established; model organisms suggest possible male-biased severity. **Founder effects/consanguinity:** not applicable (dominant, *de novo*). Recurrence risk to siblings is low (germline mosaicism possible but not quantified); risk to offspring of an affected individual is 50%.

### 10. Diagnostics
**Genetic testing is definitive.** Recommended approach: trio **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, or a broad intellectual-disability/autism/epilepsy **gene panel** that includes *CUL3*; **chromosomal microarray (CMA)** detects gene/exon-level and 16p11.2 CNVs. Variant interpretation by ACMG/AMP (PVS1 for null variants). **Supportive tests:** EEG (may show hypsarrhythmia/burst suppression), brain MRI (reduced cortical volume, delayed myelination). No specific biochemical biomarker exists, though patient cells show reduced ubiquitin conjugates and elevated 4E-BP1 (research assays). **Differential diagnosis:** other monogenic syndromic NDD/DEE genes (e.g., STXBP1 [PMID: 42609058](https://pubmed.ncbi.nlm.nih.gov/42609058/), SCN2A, MED13L, SHANK3, KCNB1, PTEN, CDKL5 — several co-identified in ASD/NDD cohorts, [PMID: 25969726](https://pubmed.ncbi.nlm.nih.gov/25969726/), [PMID: 31696658](https://pubmed.ncbi.nlm.nih.gov/31696658/)) and 16p11.2 deletion/duplication syndrome.

### 11. Outcome / Prognosis
NEDAUS is a chronic, lifelong disorder. It is not typically life-limiting on its own, but severe epilepsy (infantile spasms/DEE), feeding difficulty/failure to thrive, and structural anomalies contribute morbidity. **Prognostic factors:** severity of intellectual disability, presence and control of epilepsy, and structural comorbidities. Long-term outcomes reflect the degree of developmental impairment; recovery is limited (static encephalopathy) but developmental gains occur with intervention.

### 12. Treatment
**No disease-specific therapy exists — management is symptomatic and supportive:**
- **Antiseizure medications** for epilepsy/infantile spasms (standard infantile-spasms therapy: ACTH, vigabatrin, corticosteroids as clinically indicated).
- **Developmental/behavioral therapies:** early intervention, special education, applied behavioral therapy for autism, speech and occupational therapy.
- **Feeding support** for feeding difficulty/failure to thrive; surgical repair of palatal/cardiac anomalies as needed.
- **Emerging mechanistic targets (preclinical):** **RhoA inhibition** rescued dendritic and network phenotypes in the mouse model ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/)); the **mTOR–eIF4E/4E-BP1 translational axis** is a rational second target ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)). Neither is an approved therapy for NEDAUS. No pharmacogenomic or gene/RNA-based therapy is established.

### 13. Prevention
No primary prevention exists for a *de novo* dominant disorder. **Genetic counseling** is central: an affected individual has a 50% transmission risk; sibling recurrence risk is low but germline mosaicism cannot be excluded. **Prenatal/preimplantation genetic testing** is available for families with a known pathogenic variant. Secondary/tertiary prevention focuses on early epilepsy control and developmental intervention to limit complications.

### 14. Other Species / Natural Disease
*Cul3* orthologs are conserved: mouse *Cul3* (NCBI Gene 26554) and rat *Cul3* (NCBI Gene 292630). **Model species:** *Mus musculus* (NCBI:txid10090), *Rattus norvegicus* (NCBI:txid10116). No naturally occurring companion-animal disease is catalogued in OMIA for *CUL3*, but the pathway is evolutionarily conserved and disease mechanisms recapitulate across humans, mice, and rats ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/)). No zoonotic relevance (non-infectious genetic disease).

### 15. Model Organisms
- **Mouse (*Cul3* germline haploinsufficient, CRISPR):** recapitulates social/cognitive deficits, hyperactivity, reduced cortical volume, and dendritic/network deficits; RhoA inhibition rescues key phenotypes — strong construct and face validity ([PMID: 33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/)). Databases: MGI, IMPC.
- **Rat (16p11.2 deletion/duplication, outbred SD & LE):** altered MAPK1/CUL3 pathways, social-behavior deficits, sexual dimorphism ([PMID: 37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/)). Database: RGD.
- **In vitro / patient-derived cells:** patient T-cells demonstrate reduced ubiquitin conjugates and 4E-BP1 accumulation, providing a cellular readout of the mechanism ([PMID: 39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/)).
- **In utero electroporation (mouse):** KCTD13/TNFAIP1 manipulation alters cortical neuron positioning and dendritic maturation ([PMID: 26969432](https://pubmed.ncbi.nlm.nih.gov/26969432/)).
- **Limitations:** models capture cytoskeletal/neurogenesis phenotypes but incompletely model the full human cognitive/autistic/epileptic spectrum; iPSC-derived neuron/organoid models of NEDAUS are not yet established in the reviewed literature.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [39301775](https://pubmed.ncbi.nlm.nih.gov/39301775/) | *Loss-of-function variants in CUL3 cause a syndromic NDD* | **Landmark human cohort** (n=37, 35 LoF); defines phenotype + 4E-BP1 mechanism (F002, F009) |
| [33727673](https://pubmed.ncbi.nlm.nih.gov/33727673/) | *Autism-linked Cullin3 germline haploinsufficiency…RhoA signaling* | **Key mouse model**; cortical volume ↓, RhoA rescue (F003) |
| [37465586](https://pubmed.ncbi.nlm.nih.gov/37465586/) | *…16p11.2 rat models…MAPK2 and KCTD13/CUL3* | Cross-species conservation; CUL3-pathway alteration (F008) |
| [29361671](https://pubmed.ncbi.nlm.nih.gov/29361671/) | *Mutant Cul3-mediated familial hyperkalemic hypertension* | Defines distinct CUL3-Δ9 dominant-negative allelic disorder (F004) |
| [26969432](https://pubmed.ncbi.nlm.nih.gov/26969432/) | *Bacurd1/Kctd13 and Bacurd2/Tnfaip1…Rnd proteins* | Adaptor→RhoA/cortical positioning mechanism (F006) |
| [32619053](https://pubmed.ncbi.nlm.nih.gov/32619053/), [35563538](https://pubmed.ncbi.nlm.nih.gov/35563538/), [27378813](https://pubmed.ncbi.nlm.nih.gov/27378813/) | PHA II / CUL3-Δ9 papers | Support the distinct hypertension mechanism |
| [42446772](https://pubmed.ncbi.nlm.nih.gov/42446772/), [37328017](https://pubmed.ncbi.nlm.nih.gov/37328017/) | KEAP1–NRF2 / Cul3 antioxidant papers | Supporting CRL3 substrate network (F006) |
| [31696658](https://pubmed.ncbi.nlm.nih.gov/31696658/), [25969726](https://pubmed.ncbi.nlm.nih.gov/25969726/) | ASD/NDD WES cohorts | Independent identification of *de novo CUL3* LoF in ASD; differential-diagnosis context |
| [31279627](https://pubmed.ncbi.nlm.nih.gov/31279627/) | *Structural basis…KLHL20 E3 ligase* | Structural context for BTB-Kelch CRL3 substrate recruitment |

**Evidence-source types:** human clinical cohorts (39301775, 31696658, 25969726); model organism (33727673, 37465586, 26969432, 27378813); in vitro/patient-derived cells (39301775, 35563538, 37328017); population genetics/computational (gnomAD constraint, ClinVar).

---

## Limitations and Knowledge Gaps

1. **Small case numbers.** The largest cohort is n=37; precise prevalence, incidence, sex ratio, and natural-history milestones are not established. Phenotype frequencies for several HPO terms rest on small denominators (e.g., 2/3, 3/3).
2. **Genotype–phenotype correlation is underpowered.** The basis for highly variable expressivity (why some individuals have autism, others seizures, others neither) is unexplained; no confirmed human modifier genes or epigenetic modifiers.
3. **Two missense variants** in the cohort are not fully mechanistically resolved versus LoF — the contribution of non-null alleles to NEDAUS remains uncertain.
4. **No human neuronal disease models** (iPSC-derived neurons/organoids) were identified in the reviewed literature; mechanistic inferences rest on mouse/rat and patient blood cells.
5. **No therapeutic trials.** RhoA and mTOR–eIF4E rescue data are preclinical only; translational safety/efficacy in humans is unknown.
6. **Biomarkers** (4E-BP1 accumulation, ubiquitin-conjugate levels) are research assays, not validated clinical diagnostics.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international NEDAUS registry** to define prevalence, natural history, epilepsy trajectories, sex ratio, and genotype–phenotype correlations at scale.
2. **Generate patient iPSC-derived cortical neurons/organoids** to test whether 4E-BP1 accumulation and RhoA-dependent cytoskeletal/network phenotypes reproduce in human neurons, and to screen rescue compounds.
3. **Preclinical target validation:** test RhoA inhibitors (e.g., ROCK-pathway or direct RhoA modulators) and mTOR–eIF4E/4E-BP1-axis modulators in the *Cul3⁺/⁻* mouse for behavioral/cognitive rescue and therapeutic window.
4. **Deep phenotyping of the CRL3 substrate/adaptor network** (KCTD13, KLHL family, NRF2/KEAP1) in patient cells to identify secondary biomarkers and additional therapeutic nodes.
5. **Systematic reclassification of ClinVar VUS** (of the 727 records, ~500 non-P/LP) using functional 4E-BP1/ubiquitin-conjugate assays to improve diagnostic yield.
6. **Distinguish allelic disorders diagnostically:** ensure clinical pipelines flag exon-9-skipping CUL3-Δ9 variants (hypertension) separately from whole-gene LoF (NEDAUS), given opposite mechanisms and management.

---

*Report compiled from 9 confirmed findings and 27 reviewed papers over 5 iterations. Evidence is strongest for the core identity (F001), haploinsufficiency mechanism with 4E-BP1 accumulation (F002), and RhoA-dependent cortical/behavioral phenotypes with pharmacologic rescue in mouse (F003).*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_or_Without_Autism_or_Seizures-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_or_Without_Autism_or_Seizures-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 6 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42609138` (3 mentions) - Feeding Behaviours in Families With Children or Young People With Autism: A Systematic Review.
  - shared terms: reduced, autism
- `PMID:42446772` (4 mentions) - Neuroprotective Potential of Nardostachys jatamansi Extract via Keap1-Nrf2 Pathway Regulation in Parkinson's Disease.
  - shared terms: mechanism

Weighed against this report's own most characteristic terms: `cul3`, `disorder`, `model`, `rhoa`, `variant`, `phenotype`, `nedaus`, `e-bp1`, `cortical`, `mouse`, `lof`, `epilepsy`, `gene`, `human`, `reduced`, `cohort`, `kctd13`, `mechanism`, `autism`, `cell`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.