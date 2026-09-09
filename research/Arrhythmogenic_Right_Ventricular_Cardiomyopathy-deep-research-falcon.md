---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T10:43:14.289638'
end_time: '2026-09-01T11:04:41.645483'
duration_seconds: 1287.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: arrhythmogenic right ventricular cardiomyopathy
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 32
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-falcon_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-falcon_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** arrhythmogenic right ventricular cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **arrhythmogenic right ventricular cardiomyopathy** covering all of the
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

# Arrhythmogenic Right Ventricular Cardiomyopathy (ARVC): Comprehensive Disease Characteristics Report

**Disease:** Arrhythmogenic right ventricular cardiomyopathy (ARVC / arrhythmogenic cardiomyopathy, ACM)
**MONDO ID:** MONDO:0016587
**Category:** Mendelian (inherited cardiomyopathy)
**Report basis:** 20 confirmed findings, 66 papers reviewed across 5 investigation iterations

---

## Summary

Arrhythmogenic right ventricular cardiomyopathy (ARVC) is an inherited, mostly autosomal-dominant cardiomyopathy of the cardiac desmosome. Pathogenic variants in genes encoding intercalated-disc adhesion proteins impair cardiomyocyte cell–cell adhesion, so that mechanical stress — critically accelerated by endurance exercise — drives progressive myocyte death and fibrofatty replacement of the myocardium. The result is a substrate for life-threatening ventricular arrhythmias, sudden cardiac death (SCD) in the young, and, over time, progressive biventricular heart failure. The most common causal gene is **PKP2** (plakophilin-2, ~40% of cases); other established genes are **DSP, DSG2, DSC2, JUP** (desmosomal) and **TMEM43, PLN, DES, FLNC, LMNA, TTN** (non-desmosomal). A pathogenic variant is identified in only ~50% of probands, and the disease shows incomplete, age-dependent penetrance and striking variable expressivity even within families.

Mechanistically, loss of desmosomal integrity releases plakoglobin, which suppresses canonical Wnt/β-catenin signaling; the Hippo pathway is activated; and PPARγ/TGF-β programs reprogram cardiac cells toward adipogenic and fibrotic fates. In parallel — and often preceding overt structural change — gap-junction (connexin-43) and sodium-channel (NaV1.5) remodeling at the intercalated disc slows conduction and creates the arrhythmic substrate. Modern single-cell, spatial, and proteomic profiling has refined this picture, revealing expanded fibroblast/adipocyte populations, disease-associated cardiomyocyte states, and NLRP3/CCL3-driven inflammation, and nominating circulating biomarkers (CCL3, UCHL1, OCIAD1, desmoyokin, ZBTB11).

Diagnosis relies on the 2010 Revised Task Force Criteria (supplemented by 2020 Padua criteria) integrating ECG, imaging (echocardiography and cardiac MRI with late gadolinium enhancement), tissue characterization, arrhythmia burden, and family/genetic data — and must be distinguished from multiple phenocopies. Management is not curative and rests on exercise restriction, beta-blockers/antiarrhythmic drugs, catheter ablation, and — the only intervention proven to prevent SCD — the implantable cardioverter-defibrillator (ICD), guided by the validated ARVC risk calculator (arrhythmia) and biventricular dysfunction (death/transplant; HR 6.3). Disease-modifying AAV gene therapies (AAV9:PKP2 replacement; mutation-agnostic AAV-Cx43) have been validated in animal models and are entering clinical translation. ARVC also occurs naturally in Boxer dogs (striatin deletion) and is modeled in Jup/Dsp/Pkp2/Tmem43 mice and patient-derived iPSC cardiomyocytes.

---

## Key Findings

### 1. ARVC is primarily a genetic disease of the cardiac desmosome (F001)

ARVC is fundamentally a disease of impaired cardiomyocyte cell–cell adhesion. In the largest ARVC registries, pathogenic variants in desmosomal genes are found in roughly half to two-thirds of probands. The five classic desmosomal genes are **PKP2** (plakophilin-2, the most common), **DSP** (desmoplakin), **DSG2** (desmoglein-2), **DSC2** (desmocollin-2), and **JUP** (plakoglobin/γ-catenin). Non-desmosomal genes contributing to the arrhythmogenic-cardiomyopathy spectrum include **TMEM43, PLN, DES, TTN, FLNC,** and **LMNA**. In a pediatric ARVC cohort, a pathogenic desmosomal mutation was detected in **87%** of patients.

> *"Arrhythmogenic cardiomyopathy (ACM) is a fatal genetic heart disease primarily caused by mutations in desmosomal genes, leading to impaired cell-cell adhesion, ventricular arrhythmias, and progressive heart failure."* — [PMID: 41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/)

> *"Pathogenic mutation in desmosomal genes was detected in 87%."* — [PMID: 41078126](https://pubmed.ncbi.nlm.nih.gov/41078126/)

**Ontology suggestions:** HGNC genes PKP2, DSP, DSG2, DSC2, JUP, TMEM43, PLN, DES, FLNC, LMNA; GO:0007156 (homophilic cell adhesion via plasma-membrane adhesion molecules); GO:0002159 (desmosome assembly); GO:0005911 (cell–cell junction / intercalated disc).

### 2. Suppressed Wnt/β-catenin and activated Hippo signaling drive fibro-adipogenesis (F002)

The central molecular consequence of desmosomal disruption is signaling dysregulation. Loss of desmosomal integrity releases **plakoglobin (γ-catenin)**, which competes with β-catenin and suppresses canonical Wnt signaling. The **Hippo pathway** is activated (phosphorylation of MST1/2, LATS1/2, and YAP). Together these converge to reprogram cardiac progenitors and myocytes toward **adipogenic (PPARγ upregulation) and fibrotic fates**. A common, mutation-agnostic alteration is reduced **connexin-43 (Cx43)** gap-junction expression.

> *"Altered protein constituents of intercalated discs were associated with activation of the upstream Hippo molecules"* — [PMID: 24276085](https://pubmed.ncbi.nlm.nih.gov/24276085/)

> *"The reduction in expression of the ventricular gap junction protein Cx43 (connexin-43) is a common molecular alteration underlying desmosomal junctional deficits and arrhythmias"* — [PMID: 41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/)

**Ontology suggestions:** GO:0060070 (canonical Wnt signaling pathway); GO:0035329 (Hippo signaling); GO:0050873 (brown fat cell differentiation); GO:0005922 (connexin complex).

### 3. ARVC is a leading cause of SCD in young athletes; exercise accelerates the phenotype (F003)

ARVC is one of the most important causes of sudden death in young athletes, and physical activity is a genuine disease accelerator rather than a mere trigger. In a four-decade juvenile SCD registry from north-east Italy, ACM was the cause of SCD in **29% of competitive athletes**. Intense endurance exercise accelerates phenotypic expression and arrhythmic propensity, with the strongest evidence for **PKP2**-mediated ACM, supported by both desmoplakin-transgenic mouse and human data. Preparticipation ECG screening reduced athlete SCD incidence in Italy (from 0.43 to 0.14 per 100,000/year after 2010).

> *"ACM was the cause of SCD in 29% of athletes."* — [PMID: 42305082](https://pubmed.ncbi.nlm.nih.gov/42305082/)

> *"the evidence that exercise is a disease-accelerator is most compelling for PKP2-mediated ACM"* — [PMID: 41954551](https://pubmed.ncbi.nlm.nih.gov/41954551/)

**Ontology suggestions:** HP:0001645 (Sudden cardiac death); HP:0004308 (Ventricular arrhythmia).

### 4. Management: exercise restriction, antiarrhythmics, ablation, and ICD (F004)

No curative therapy exists. Management combines: (1) **exercise restriction**; (2) **beta-blockers and antiarrhythmic drugs**, which reduce arrhythmia burden but not SCD risk; (3) **catheter ablation of VT** — endocardial ablation alone has high recurrence because of the epicardial and patchy substrate, so combined endo-epicardial ablation improves success; and (4) **ICD implantation** for high-risk patients after risk stratification. Bilateral cardiac sympathetic denervation reduced ICD shocks in refractory VT (5 of 8 patients VT-free).

> *"Treatment consists of restriction of physical exercise, antiarrhythmic drugs, catheter ablation and ICD implantation."* — [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)

> *"Antiarrhythmic drugs play an important role in terms of reduction of both the number and the complexity of arrhythmias, but they do not reduce the risk of SD."* — [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)

> *"Endocardial VT ablation in this setting can produce acute success, though recurrence rate is quite high, which may be explained by the more epicardial and patchy nature of the disease."* — [PMID: 28779285](https://pubmed.ncbi.nlm.nih.gov/28779285/)

**Ontology suggestions (NCIT):** ICD implantation, catheter ablation, beta-adrenergic blocker therapy, sotalol, amiodarone.

### 5. Epidemiology: prevalence ~1 in 2,000–5,000, male predominance, 2nd–4th-decade onset (F005)

Estimated prevalence is **1 in 5,000 to 1 in 2,000** in the general population. The disease affects **men more frequently than women** and typically becomes clinically overt from the **second to the fourth decade of life**. In athlete SCD registries, cases are overwhelmingly male (e.g., 50 of 51 in one Italian series).

> *"a genetically determined rare cardiomyopathy (1 in 5000 to 1 in 2000 in the general population)"* — [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)

> *"The disease affects men more frequently than women and becomes clinically overt usually from the second to the fourth decade of life."* — [PMID: 25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/)

### 6. A validated multivariable risk calculator predicts incident ventricular arrhythmia (F006)

A validated calculator (**www.ARVCrisk.com**) estimates individualized risk of first-time sustained ventricular arrhythmia (VA) in definite ARVC patients and performs well (C-statistic ~0.78). Incremental predictors under study include RV free-wall longitudinal strain/regional deformation (raising the C-statistic to ~0.82) and LV late gadolinium enhancement on CMR. Circulating miRNAs (miR-15a-5p, miR-16-5p, miR-92a-3p) show promise for risk stratification.

> *"A risk calculator for individualized prediction of first-time sustained ventricular arrhythmia (VA) in arrhythmogenic right ventricular cardiomyopathy (ARVC) patients has recently been developed and validated (www.ARVCrisk.com)."* — [PMID: 37474315](https://pubmed.ncbi.nlm.nih.gov/37474315/)

> *"The arrhythmogenic right ventricular cardiomyopathy (ARVC) risk calculator estimates the risk of incident sustained ventricular arrhythmia (VA) and performs well..."* — [PMID: 41608798](https://pubmed.ncbi.nlm.nih.gov/41608798/)

### 7. Recessive cardiocutaneous syndromes link ARVC to skin/hair phenotypes (F007)

Two autosomal-recessive cardiocutaneous syndromes anchored the discovery of desmosomal ARVC genetics. **Naxos disease** (OMIM 601214) is recessive ARVC caused by a homozygous **JUP** (plakoglobin) mutation, with woolly hair (from birth), palmoplantar keratoderma (first year), and cardiomyopathy manifesting by adolescence with 100% penetrance. **Carvajal syndrome** (OMIM 605676) is caused by **DSP** mutations with predominantly left-ventricular involvement and childhood-onset heart failure; recessive DSC2 mutations produce an overlapping phenotype.

> *"Naxos disease is a recessively inherited condition with arrhythmogenic right ventricular dysplasia/cardiomyopathy (ARVD/C) and a cutaneous phenotype, characterised by peculiar woolly hair and palmoplantar keratoderma."* — [PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)

> *"Defects in the linking sites of these proteins can interrupt the contiguous chain of cell adhesion, particularly under conditions of increased mechanical stress or stretch, leading to cell death, progressive loss of myocardium and fibro-fatty replacement."* — [PMID: 16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/)

> *"Carvajal syndrome (Online Mendelian Inheritance in Man [OMIM] 605676) is characterized by the association of dilated cardiomyopathy, striate palmoplantar keratoderma, and woolly hair."* — [PMID: 25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/)

**Ontology suggestions:** HP:0007502 (Woolly hair); HP:0000982 (Palmoplantar keratoderma).

### 8. Autosomal-dominant inheritance with incomplete penetrance and variable expressivity (F008)

A familial history is present in **30–50%** of cases. ARVC is usually inherited in an **autosomal-dominant** pattern with variable penetrance and expressivity, plus recessive forms (Naxos, Carvajal). Genetic testing finds a pathogenic mutation in only ~**50%** of patients (gene-elusive in the remainder). Wide intra- and inter-family expressivity remains largely unexplained. The recognized disease spectrum now includes right-dominant (ARVC), left-dominant (ALVC), and biventricular arrhythmogenic cardiomyopathy.

> *"A familial history of ARVC is present in 30% to 50% of cases, and the disease is considered a genetic cardiomyopathy, usually inherited in an autosomal dominant pattern with variable penetrance and expressivity"* — [PMID: 25548613](https://pubmed.ncbi.nlm.nih.gov/25548613/)

> *"Genetic testing is critical in identifying familial mutations and initiating cascade testing, but finds a pathogenic mutation in only ∼50% of patients."* — [PMID: 30446243](https://pubmed.ncbi.nlm.nih.gov/30446243/)

### 9. Naturally occurring ARVC in Boxer dogs (striatin deletion) (F009)

Boxer ARVC is a naturally occurring canine disease causing sudden death or heart failure, associated with a **striatin (STRN) deletion**. In a prospective study of 72 dogs (49 ARVC, 23 controls), ARVC was defined as ≥300 ventricular premature complexes/24h; 33% were syncopal, median age of diagnosis was 6 years, and 36 of 43 genotyped ARVC dogs carried the striatin deletion. It is a disease of middle age. Cats and other species also develop analogous disease.

> *"Boxer arrhythmogenic right ventricular cardiomyopathy (ARVC) is a disease that may result in sudden death or heart failure."* — [PMID: 24962663](https://pubmed.ncbi.nlm.nih.gov/24962663/)

**Ontology suggestions:** NCBITaxon:9615 (*Canis lupus familiaris*); STRN ortholog.

### 10. TMEM43 p.S358L causes the most aggressive subtype (ARVC5) via increased nuclear stiffness (F010)

**ARVC-5** is the most aggressive heterozygous form, caused by the fully penetrant non-desmosomal **TMEM43 p.S358L** mutation, originally endemic to Newfoundland but shown by haplotype analysis to be a European founder mutation ~1,300–1,500 years old. In 62 Spanish carriers, SCD incidence was **38.7%** (higher in men); left-ventricular involvement was common (40% with LVEF <50%). Mechanistically, carrier fibroblast nuclei show increased stiffness versus wild-type by atomic force microscopy.

> *"Arrhythmogenic right ventricular cardiomyopathy type V (ARVC-5) is the most aggressive heterozygous form of ARVC. It is predominantly caused by a fully penetrant mutation (p.S358L) in the nondesmosomal gene TMEM43-endemic to Newfoundland, Canada."* — [PMID: 32062046](https://pubmed.ncbi.nlm.nih.gov/32062046/)

> *"revealed that the cell nuclei exhibit an increased stiffness compared with TMEM43 wild-type controls"* — [PMID: 24598986](https://pubmed.ncbi.nlm.nih.gov/24598986/)

> *"The affected individuals showed a 38.7% incidence of sudden cardiac death, which was higher in men."* — [PMID: 32062046](https://pubmed.ncbi.nlm.nih.gov/32062046/)

### 11. Diagnosis requires distinguishing multiple phenocopies; electrical change precedes structural change (F011)

Diagnosis uses the **2010 Task Force Criteria** (major/minor across ECG depolarization/repolarization, arrhythmias, imaging structural/functional, tissue characterization, and family/genetics). Differential diagnoses include idiopathic RV outflow-tract tachycardia, Brugada syndrome, athlete's heart, dilated cardiomyopathy, myocarditis, cardiac sarcoidosis (a phenocopy that can produce epsilon waves), and congenital RV aneurysms. **Electrical alterations** (PVCs, VT/VF, T-wave inversions V1–V3, epsilon waves) frequently precede detectable structural changes. Three subtypes are recognized: right-dominant (classic ARVC), biventricular, and left-dominant (ALVC).

> *"Idiopathic RV outflow tract tachycardia, Brugada Syndrome, athlete's heart, dilated cardiomyopathy, myocarditis, cardiac sarcoidosis, congenital aneurysms and diverticula may mimic clinical phenotypes of ARVC."* — [PMID: 35268321](https://pubmed.ncbi.nlm.nih.gov/35268321/)

> *"structural findings often become visible after electrical alterations, such as premature ventricular beats, ventricular fibrillation (VF) and ventricular tachycardia (VT)"* — [PMID: 27617087](https://pubmed.ncbi.nlm.nih.gov/27617087/)

**Ontology suggestions:** HP:0011663 (Right ventricular cardiomyopathy); HP:0004756 (Ventricular arrhythmia).

### 12. Desmosomal dysfunction remodels gap junctions and sodium channels, creating the arrhythmic substrate (F012)

Immunohistochemistry of ACM patient hearts shows altered expression and distribution of **connexin-43 (Cx43)**, **plakoglobin**, and the cardiac sodium channel **NaV1.5** at the intercalated disc, secondary to desmosomal dysfunction. Reduced Cx43 and mislocalized/reduced NaV1.5 slow conduction and reduce sodium current, promoting reentry independent of — and preceding — overt fibrofatty structural change. This provides the mechanistic basis for the clinical observation that electrical abnormalities precede structural ones.

> *"a disturbed distribution of gap junction proteins and cardiac sodium channels may also be observed in AC phenotypes, secondary to desmosomal dysfunction"* — [PMID: 23834686](https://pubmed.ncbi.nlm.nih.gov/23834686/)

> *"The altered expression and/or distribution of NaV1.5 channels in AC hearts may play a mechanistic role in the arrhythmias leading to sudden cardiac death in AC patients."* — [PMID: 23834686](https://pubmed.ncbi.nlm.nih.gov/23834686/)

**Ontology suggestions:** genes SCN5A (NaV1.5), GJA1 (Cx43); GO:0086010 (membrane depolarization during action potential).

### 13. Inflammation and innate/autoimmunity contribute to "hot phase" episodes, especially in DSP carriers (F013)

A subset of ARVC patients experience **"hot phases"**: chest pain with troponin release and ECG changes without ischemia, mimicking acute myocarditis. **DSP** (desmoplakin) variants are most frequently associated. Evidence implicates inflammation, autoimmunity, and innate immune activation — myocardial inflammatory infiltrates, circulating anti-desmosomal/anti-intercalated-disc autoantibodies, and NLRP3-inflammasome activation. Immunosuppressive therapy may modulate arrhythmic and heart-failure outcomes in DSP carriers.

> *"Growing data indicate that inflammation, autoimmunity, and innate immune activation play a central role in HP expression and ACM pathobiology, supported by findings of myocardial inflammatory infiltrates, circulating anti-desmosomal and anti-intercalated disc autoantibodies, and activation of NLRP3-inflammasome pathways."* — [PMID: 41448261](https://pubmed.ncbi.nlm.nih.gov/41448261/)

> *"Among ACM-related genes, desmoplakin (DSP) variants are most frequently associated with HP"* — [PMID: 41448261](https://pubmed.ncbi.nlm.nih.gov/41448261/)

**Ontology suggestions:** GO:0072559 (NLRP3 inflammasome complex); HP:0012819 (Myocarditis); CL:0000235 (macrophage).

### 14. DSP arrhythmogenic cardiomyopathy is a distinct left-dominant/biventricular entity (F014)

**DSP-ACM** is associated with more frequent LV involvement, lower LVEF (46±12% vs 56±10% in LV+ right-dominant ACM, P=0.001), LV late gadolinium enhancement, and inflammatory episodes. In families ascertained through acute myocarditis, DSP variants predominated; 39% of carriers had an arrhythmogenic LV phenotype, and 38% of asymptomatic carriers showed isolated LV LGE without meeting RV Task Force Criteria. Such patients often do NOT meet classic (RV-focused) 2010 Task Force Criteria — a key diagnostic pitfall.

> *"Arrhythmogenic cardiomyopathy (ACM) related to Desmoplakin (DSP) mutations is a distinct condition associated with particularly severe outcomes, more frequent left ventricular (LV) involvement, including fibrosis, dysfunction, and inflammatory episodes."* — [PMID: 40021092](https://pubmed.ncbi.nlm.nih.gov/40021092/)

> *"a remarkable phenotype of isolated LV late gadolinium enhancement on contrast-enhanced cardiac magnetic resonance without any other structural abnormality was found in 38% of asymptomatic mutation carriers"* — [PMID: 32356610](https://pubmed.ncbi.nlm.nih.gov/32356610/)

### 15. Biventricular dysfunction is the strongest predictor of death/transplant (F015)

In a 10-year registry of 96 ARVC patients (68% male, 35±15 yr), 21% experienced cardiac death or heart transplantation over 128±92 months. Independent predictors of death/HTx were RV dysfunction (HR 4.12, 95% CI 1.01–18.0, P=0.05), significant tricuspid regurgitation (HR 7.6, 95% CI 2.6–22.0, P<0.001), and amiodarone treatment (HR 3.4). Combined RV+LV ("ordinal") dysfunction was the strongest independent predictor (**HR 6.3, 95% CI 2.17–17.45, P<0.001**). RV systolic dysfunction was present in 65%, LV dysfunction in 24%.

> *"the 'ordinal dysfunction' (Model 2), which considers the presence of both RV and LV dysfunctions, this variable emerged as an independent prognostic predictor (HR: 6.3; 95% CI: 2.17-17.45; P < 0.001)"* — [PMID: 21362707](https://pubmed.ncbi.nlm.nih.gov/21362707/)

> *"During a mean follow-up of 128 ± 92 months, 20 patients (21%) experienced cardiac death or underwent HTx."* — [PMID: 21362707](https://pubmed.ncbi.nlm.nih.gov/21362707/)

### 16. AAV-mediated PKP2 gene replacement prevents and rescues ARVC in mice (F016)

**PKP2** mutations account for ~40% of ARVC and cause reduced gene expression (haploinsufficiency), providing a strong rationale for gene replacement. Three independent groups showed **AAV9:PKP2** gene delivery restores desmosomal/gap-junction structure, prevents or reverses RV dilation, improves LVEF, reduces ventricular arrhythmias and fibrosis, and extends survival (up to 100% survival in treated mice) — both prophylactically (neonatal) and after overt cardiomyopathy (PMID: 39196150; 38499690; 38665939). A mutation-agnostic alternative, **AAV-Cx43**, rescues multiple desmosomal ACM models (PMID: 41582809).

> *"Mutations in Plakophilin-2 (PKP2), encoding a desmosomal protein, account for approximately 40% of ARVC cases and result in reduced gene expression."* — [PMID: 38499690](https://pubmed.ncbi.nlm.nih.gov/38499690/)

> *"Late-stage AAV-PKP2 administration rescued desmosomal protein deficits and reduced pathological deficits including improved cardiac function in adult mice"* — [PMID: 39196150](https://pubmed.ncbi.nlm.nih.gov/39196150/)

> *"a single dose of AAV9:PKP2 gene delivery prevents disease development before the onset of cardiomyopathy and attenuates disease progression after overt cardiomyopathy"* — [PMID: 38499690](https://pubmed.ncbi.nlm.nih.gov/38499690/)

### 17. Single-cell/spatial transcriptomics reveal disease-associated cell states (F017)

- **snRNA-seq** of 5 ACM transplant hearts vs 4 donors showed increased fibroblast and adipocyte proportions and a disease-associated cardiomyocyte subpopulation (CM1) upregulating fibrosis-, metabolism-, and stress-related markers (PMID 40383406).
- **scRNA-seq** of 6 end-stage ARVC hearts + 2 controls identified **NLRP3** as a therapeutic target; pharmacological NLRP3 inhibition prevented RV dilation/dysfunction in ARVC mice; RV was enriched for CCL3 (PMID 38185631).
- **Spatial (Tomo-Seq)** transmural profiling identified **ZBTB11** specifically enriched at sites of active fibro-fatty replacement, inducing autophagy/cell-death programs (PMID 35576477).
- An integrated single-cell/single-nucleus atlas of 45 healthy, 70 DCM, 8 ARVC hearts identified ~1,100 myocardial B cells with disease-specific interaction networks (PMID 38736889).

> *"The snRNA-seq analysis revealed an increased proportion of fibroblasts and adipocytes in the left ventricles of LACM patients, suggesting a cellular basis for the fibrofatty remodeling observed in the disease."* — [PMID: 40383406](https://pubmed.ncbi.nlm.nih.gov/40383406/)

> *"Pharmacological inhibition of NLRP3 could prevent right ventricular dilation and dysfunction of mice with ARVC."* — [PMID: 38185631](https://pubmed.ncbi.nlm.nih.gov/38185631/)

> *"revealed Zinc finger and BTB domain-containing protein 11 (ZBTB11) to be specifically enriched at sites of active fibro-fatty replacement of myocardium"* — [PMID: 35576477](https://pubmed.ncbi.nlm.nih.gov/35576477/)

**Ontology suggestions:** CL:0000057 (fibroblast), CL:0000136 (adipocyte), CL:0000746 (cardiac muscle cell), CL:0000235 (macrophage), CL:0000236 (B cell).

### 18. Multi-omics implicates immune-metabolic dysregulation and nominates circulating biomarkers (F018)

Myocardial RNA-seq + label-free LC-MS/MS proteomics (n=10/group ACM vs DCM vs control) found 3,030 dysregulated mRNAs and 206 differentially expressed proteins in ACM vs control, enriched for immune activation, inflammation, ECM remodeling, and mitochondrial stress; three proteins (**UCHL1, OCIAD1, desmoyokin**) were consistently upregulated at transcript and protein level (PMID 41229088). Lipidomics of ACM fibro-fatty tissue showed increased saturated triglycerides and beige/brown fat markers; scRNA-seq showed pro-inflammatory macrophage accumulation, and plasma **CCL3** predicted adverse heart-failure outcomes (PMID 40223064).

> *"Three novel proteins, UCHL1, OCIAD1 and desmoyokin, were consistently up-regulated at transcript and protein"* — [PMID: 41229088](https://pubmed.ncbi.nlm.nih.gov/41229088/)

> *"The expression of CCL3 in the fibro-fatty tissues was positively correlated with HF progression in patients with ACM."* — [PMID: 40223064](https://pubmed.ncbi.nlm.nih.gov/40223064/)

### 19. ARVC substantially impairs quality of life, with age-, sex-, and shock-dependent burden (F019)

A cross-sectional psychosocial survey of 159 ARVC patients (SF-36, Florida Shock Anxiety Scale, Florida Patient Acceptance Survey) found that ARVC patients reported **lower physical and mental QoL** than a U.S. normative sample. Patients aged 18–35 reported significantly lower mental QoL than older patients; ICD-shock history was associated with higher shock anxiety and lower mental QoL; and female patients reported significantly higher shock anxiety and lower mental QoL than males (PMID 28823501).

> *"ARVC patients reported lower physical and mental QOL compared to a normative U.S sample."* — [PMID: 28823501](https://pubmed.ncbi.nlm.nih.gov/28823501/)

> *"Female ARVC patients reported significantly higher shock anxiety and lower mental QOL compared to male patients."* — [PMID: 28823501](https://pubmed.ncbi.nlm.nih.gov/28823501/)

### 20. Male predominance is gene-specific, with DSP enriched in females (F020)

A SHaRe registry analysis of 3,410 genetically tested DCM/ACM patients found a **61% male predominance** across genotype-positive, genotype-negative, and VUS subgroups (P=0.008), with significant gene-specific variation. TTN-truncating variants were less common in females (OR 0.42, 95% CI 0.33–0.54; P<0.01), whereas **DSP variants** (OR 3.3, 95% CI 2.35–4.78; P<0.01) and grouped non-TTN sarcomeric variants (OR 1.68, 95% CI 1.15–2.47; P<0.001) were more common in females (PMID 42159538).

> *"a 61% male predominance was present across subgroups of genotype positive, genotype negative, and variants of uncertain significance (P = 0.008), with significant gene-specific variation"* — [PMID: 42159538](https://pubmed.ncbi.nlm.nih.gov/42159538/)

> *"DSP (OR: 3.3 [95% CI: 2.35-4.78]; P < 0.01) and grouped non-TTN sarcomeric variants ... were more common (OR: 1.68 [95% CI: 1.15-2.47]; P < 0.001) in females"* — [PMID: 42159538](https://pubmed.ncbi.nlm.nih.gov/42159538/)

---

## Section-by-Section Disease Profile

### 1. Disease Information

ARVC is an inherited cardiomyopathy characterized by fibrofatty replacement of the (predominantly right) ventricular myocardium, ventricular arrhythmias, and risk of sudden cardiac death, with later progression to heart failure. It is now understood as part of a broader **arrhythmogenic cardiomyopathy (ACM)** spectrum encompassing right-dominant (classic ARVC), left-dominant (ALVC), and biventricular forms.

- **Key identifiers:** MONDO:0016587; OMIM phenotype series (Naxos OMIM 601214, Carvajal OMIM 605676, ARVC-5/TMEM43); Orphanet ORPHA:247; ICD-10 I42.8; ICD-11 BC43.3; MeSH D019571 (Arrhythmogenic Right Ventricular Dysplasia).
- **Synonyms:** arrhythmogenic right ventricular dysplasia/cardiomyopathy (ARVD/C); arrhythmogenic cardiomyopathy (ACM); arrhythmogenic ventricular cardiomyopathy (AVC).
- **Information source:** Aggregated disease-level resources (registries, OMIM, Orphanet, cohort studies), supplemented by individual clinical case reports and family-screening cohorts.

### 2. Etiology

**Primary cause:** Germline pathogenic variants in desmosomal genes (PKP2, DSP, DSG2, DSC2, JUP) and non-desmosomal genes (TMEM43, PLN, DES, FLNC, LMNA, TTN) (F001, F010). **Environmental/lifestyle modifier:** intense endurance exercise is the best-established disease accelerator, strongest for PKP2 (F003). **Risk factors:** male sex, family history, gene-elusive multifactorial background (F005, F008, F020). **Protective factors:** exercise restriction reduces phenotypic progression and arrhythmic risk (F003, F004); no well-established protective genetic variant is confirmed here. **Gene–environment interaction:** the "second-hit" model — a desmosomal/genetic predisposition combined with mechanical stress (exercise) or inflammation ("hot phase") triggers phenotypic expression (F003, F013).

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Notes / frequency |
|---|---|---|---|
| Ventricular tachycardia/arrhythmia | Clinical sign | HP:0004756 / HP:0004308 | Hallmark; often precedes structural change (F011) |
| Sudden cardiac death | Outcome | HP:0001645 | Leading cause in young athletes; 29% of athlete SCD (F003) |
| Palpitations | Symptom | HP:0001962 | Common presenting symptom |
| Syncope | Symptom | HP:0001279 | Arrhythmogenic syncope; higher-risk marker |
| Right ventricular dilation/dysfunction | Physical/imaging | HP:0001714 | RV dysfunction in 65% (F015) |
| Left ventricular dysfunction | Physical/imaging | HP:0001644 | 24% overall; prominent in DSP-ACM (F014, F015) |
| Heart failure | Clinical sign | HP:0001635 | Late-phase; ~7% hospitalization in one cohort |
| T-wave inversion V1–V3 / epsilon wave | Lab/ECG | HP:0012231 | Depolarization/repolarization criteria (F011) |
| Woolly hair, palmoplantar keratoderma | Physical (recessive) | HP:0007502 / HP:0000982 | Naxos/Carvajal (F007) |

**Age of onset:** typically 2nd–4th decade; pediatric and recessive childhood-onset forms exist. **Severity/progression:** variable, progressive; episodic "hot phases" in DSP carriers (F013). **QoL impact:** significantly reduced physical and mental QoL, worse in young patients, women, and those with ICD shocks (F019).

### 4. Genetic/Molecular Information

**Causal genes:** PKP2 (~40%, most common), DSP, DSG2, DSC2, JUP (desmosomal); TMEM43, PLN, DES, FLNC, LMNA, TTN (non-desmosomal) (F001, F010). **Variant types:** missense, nonsense, frameshift, splice-site, and structural (e.g., PKP2 splice IVS10-1G>C; TMEM43 p.S358L founder missense; STRN deletion in dogs). **Functional consequences:** PKP2 haploinsufficiency (reduced expression); JUP loss-of-function; TMEM43 altering nuclear mechanics (F016, F010, F009). **Modifier/gene-elusive:** ~50% have no identified variant, implying modifier genes and multifactorial/polygenic contribution (F008). **Epigenetic/chromosomal:** not a principal driver; STRN deletion is the notable structural lesion (canine).

### 5. Environmental Information

The dominant non-genetic factor is **intense/endurance physical exercise**, which accelerates phenotype and arrhythmias (F003). Inflammatory/possibly infectious triggers may initiate "hot phases," clinically mimicking viral myocarditis, particularly in DSP carriers (F013). No specific occupational toxin or confirmed infectious agent is established as causal.

### 6. Mechanism / Pathophysiology — Causal Chain

```
1. Germline pathogenic variant in a desmosomal (PKP2/DSP/DSG2/DSC2/JUP)
   or non-desmosomal (TMEM43/PLN/DES/FLNC/LMNA) gene
        │  leads to
        ▼
2. Structurally/functionally defective desmosome (or nuclear-membrane/
   cytoskeletal defect for TMEM43 → increased nuclear stiffness)
        │  results in
        ▼
3. Impaired cardiomyocyte cell–cell adhesion at the intercalated disc;
   under mechanical stress (accelerated by endurance EXERCISE) →
        ├──► 4a. Cardiomyocyte detachment and DEATH
        │         │ leads to
        │         ▼
        │    5a. Progressive myocyte loss → FIBRO-FATTY REPLACEMENT
        │         (plakoglobin release → suppressed Wnt/β-catenin,
        │          activated Hippo–YAP, PPARγ/TGF-β adipo-fibrogenic programs)
        │
        └──► 4b. Intercalated-disc remodeling:
                  reduced Cx43 gap junctions + mislocalized/reduced NaV1.5
                  │ results in
                  ▼
             5b. Slowed conduction + reduced sodium current →
                  ARRHYTHMIC SUBSTRATE (reentry) — often PRECEDES 5a
        │
        │  (branch) INFLAMMATION / autoimmunity / NLRP3 inflammasome
        │  → "hot phases" (esp. DSP), amplifying injury
        ▼
6. Ventricular arrhythmias (VT/VF) → SUDDEN CARDIAC DEATH
   and, over time, RV → biventricular dysfunction → HEART FAILURE
```

Upstream events are the genetic lesion and adhesion failure; downstream are fibrofatty remodeling, electrical remodeling, arrhythmia, and heart failure. The electrical branch (5b) can dominate early (concealed phase), explaining SCD before overt structural disease (F002, F011, F012, F013).

**Molecular pathways:** Wnt/β-catenin (suppressed), Hippo–YAP (activated), TGF-β, PPARγ adipogenesis (F002). **Cellular processes:** apoptosis/cell death, inflammation, autophagy (ZBTB11), fibro-adipogenic differentiation (F002, F013, F017). **Protein dysfunction:** desmosomal loss-of-function/haploinsufficiency; Cx43/NaV1.5 mislocalization (F012, F016). **Immune involvement:** NLRP3 inflammasome, autoantibodies, macrophage/B-cell infiltration (F013, F017, F018). **Omics:** dysregulated immune-metabolic/mitochondrial pathways; biomarkers UCHL1, OCIAD1, desmoyokin, CCL3, ZBTB11 (F017, F018).

### 7. Anatomical Structures Affected

- **Organ:** heart, principally the **right ventricle** (UBERON:0002080), frequently the **left ventricle** (UBERON:0002084), especially DSP-ACM; body system cardiovascular (F014, F015).
- **Tissue/cell:** ventricular myocardium replaced by fibrous and adipose tissue; involved cells include cardiomyocytes (CL:0000746), fibroblasts (CL:0000057), adipocytes (CL:0000136), macrophages (CL:0000235), B cells (CL:0000236) (F002, F017).
- **Subcellular:** intercalated disc / desmosome / gap junction (GO:0005911, GO:0030057, GO:0005922); nuclear envelope for TMEM43 (GO:0005635) (F010, F012).
- **Localization/lateralization:** predominantly RV free wall / "triangle of dysplasia" and RVOT; often biventricular; DSP shows basal inferolateral LV involvement. Skin/hair in recessive syndromes (F007).

### 8. Temporal Development

**Onset:** typically 2nd–4th decade; concealed → electrical → structural → heart-failure phases. **Progression:** variable and generally progressive; episodic "hot phases" (F013). **Course:** lifelong chronic; arrhythmic risk lifelong; late heart failure. **Critical periods:** adolescence–young adulthood and periods of intense athletic training are windows of heightened vulnerability and intervention opportunity (F003, F005, F008).

### 9. Inheritance and Population

Prevalence ~1 in 2,000–5,000; predominantly autosomal-dominant with incomplete, age-dependent penetrance and variable expressivity; recessive cardiocutaneous forms (Naxos/JUP, Carvajal/DSP) (F005, F007, F008). **Penetrance:** TMEM43 p.S358L is fully penetrant; most desmosomal variants incompletely penetrant (F010, F008). **Founder effects:** TMEM43 p.S358L (Newfoundland/European origin) (F010). **Sex ratio:** overall male predominance (~61% in the DCM/ACM spectrum), but gene-specific — DSP enriched in females (F005, F020). Familial history in 30–50% (F008).

### 10. Diagnostics

- **Clinical criteria:** 2010 Revised Task Force Criteria (2020 Padua criteria add LV/tissue-characterization refinements) (F011).
- **ECG/electrophysiology:** T-wave inversion V1–V3, epsilon waves, late potentials, VT with LBBB morphology (F011).
- **Imaging:** echocardiography and cardiac MRI (RV dilation/dysfunction; late gadolinium enhancement, including isolated LV-LGE in DSP carriers) (F006, F014).
- **Tissue:** endomyocardial biopsy showing patchy, epicardial-predominant fibrofatty replacement.
- **Biomarkers:** troponin release in hot phases; investigational circulating miRNAs (miR-15a-5p/16-5p/92a-3p), plasma CCL3, proteomic candidates UCHL1/OCIAD1/desmoyokin (F006, F013, F018).
- **Genetic testing:** broad cardiomyopathy/arrhythmia gene panels, WES/WGS; single-gene/cascade testing of relatives; yield ~50% (F008).
- **Differential diagnosis:** idiopathic RVOT tachycardia, Brugada syndrome, athlete's heart, DCM, myocarditis, cardiac sarcoidosis, congenital RV aneurysms (F011).

### 11. Outcome/Prognosis

Principal outcomes are SCD (especially young/athletic males) and progressive biventricular heart failure. Combined RV+LV dysfunction is the strongest independent predictor of death/transplant (HR 6.3); tricuspid regurgitation and RV dysfunction are additional predictors (F015). The ARVC risk calculator estimates arrhythmic risk (F006). DSP-ACM carries particularly severe outcomes with LV fibrosis/dysfunction and HF (F014). QoL is substantially impaired (F019).

### 12. Treatment

No curative therapy. Pillars: exercise restriction; beta-blockers/antiarrhythmics (reduce arrhythmia, not SCD); catheter ablation (combined endo-epicardial preferred); ICD (only SCD-preventive intervention); heart transplantation for end-stage HF; bilateral cardiac sympathetic denervation for refractory VT (F004). **Emerging disease-modifying:** AAV9:PKP2 gene replacement and mutation-agnostic AAV-Cx43 (animal-validated, translating); apremilast and NLRP3 inhibition are experimental candidates (F016, F017). Personalized/genotype-guided management is increasingly relevant (DSP → immunomodulation in hot phases; PKP2 → exercise counseling and future gene therapy) (F013, F016).

**NCIT suggestions:** Implantable Cardioverter-Defibrillator; Catheter Ablation; Beta-Blocker Therapy; Amiodarone; Sotalol; Heart Transplantation; Gene Therapy.

### 13. Prevention

- **Primary:** exercise restriction / competitive-sport avoidance in gene carriers; preparticipation ECG screening (reduced athlete SCD in Italy) (F003, F004).
- **Secondary:** cascade family screening (clinical + genetic), regular surveillance of at-risk relatives — including gene-elusive families (F008).
- **Tertiary:** ICD, antiarrhythmics, ablation, HF therapy to prevent complications (F004, F015).
- **Counseling:** genetic counseling for family planning; risk stratification via the ARVC calculator (F006, F008).

### 14. Other Species / Natural Disease

Naturally occurring ARVC is well described in the **Boxer dog** (NCBITaxon:9615), associated with a **striatin (STRN) deletion**, causing SCD/HF with a middle-age onset; cats and other species also develop analogous disease (F009). This provides a spontaneous large-animal comparative model.

### 15. Model Organisms

- **Mouse:** Jup (plakoglobin) cardiomyocyte-restricted knockout recapitulates ventricular dilation, aneurysm, fibrosis, and spontaneous arrhythmias; Dsp-transgenic (R2834H) mice show exercise-accelerated RV disease with perturbed Wnt/β-catenin; Pkp2-deficient and PKP2 patient-splice-mutation mice model the commonest genotype and respond to AAV9:PKP2; TMEM43 models capture nuclear-stiffness mechanisms (F016, F002, F003, F010).
- **iPSC-cardiomyocytes:** patient-derived (e.g., DSP p.Glu952Ter) hiPSC-CMs show loss of cohesion rescued by apremilast — an in vitro human model.
- **Applications:** dissecting adhesion/signaling, arrhythmogenesis, and testing gene/pharmacologic therapies. **Limitations:** murine electrophysiology and RV geometry differ from human; incomplete recapitulation of the human "hot phase"/immune component.

---

## Mechanistic Model / Interpretation

The evidence converges on a unifying model in which **a genetic adhesion defect at the intercalated disc**, unmasked by **mechanical or inflammatory stress**, drives two partially independent downstream arms: (1) an **electrical arm** (Cx43/NaV1.5 remodeling → conduction slowing → reentry), which can produce arrhythmia and SCD *before* overt structural change; and (2) a **structural arm** (myocyte death → plakoglobin/Hippo/Wnt/PPARγ/TGF-β-driven fibrofatty replacement), which produces the imaging hallmark and, ultimately, biventricular heart failure. Inflammation/autoimmunity (NLRP3, autoantibodies, CCL3, macrophage/B-cell infiltration) modulates both arms and dominates "hot phases," especially in DSP genotype. Genotype shapes the clinical face of the disease: PKP2 → classic right-dominant, exercise-sensitive; TMEM43 → most aggressive, fully penetrant; DSP → left-dominant/biventricular, inflammatory, female-enriched.

| Arm | Key molecules | Timing | Clinical readout |
|---|---|---|---|
| Electrical | Cx43↓, NaV1.5 mislocalization | Early (concealed) | VT/VF, SCD |
| Structural | Plakoglobin, Hippo-YAP, PPARγ, TGF-β | Progressive | Fibrofatty scar, RV/LV dysfunction, HF |
| Inflammatory | NLRP3, CCL3, autoantibodies | Episodic "hot phase" | Troponin release, myocarditis-like, DSP |

---

## Evidence Base (selected)

| PMID | Contribution |
|---|---|
| [25894016](https://pubmed.ncbi.nlm.nih.gov/25894016/) | Prevalence, sex, onset, and the four treatment pillars |
| [41582809](https://pubmed.ncbi.nlm.nih.gov/41582809/) | Desmosomal etiology; Cx43 reduction; AAV-Cx43 therapy |
| [24276085](https://pubmed.ncbi.nlm.nih.gov/24276085/) | Hippo pathway activation as causal for adipogenesis |
| [42305082](https://pubmed.ncbi.nlm.nih.gov/42305082/) | ACM = 29% of athlete SCD |
| [41954551](https://pubmed.ncbi.nlm.nih.gov/41954551/) | Exercise as disease-accelerator, strongest for PKP2 |
| [23834686](https://pubmed.ncbi.nlm.nih.gov/23834686/) | Cx43/NaV1.5 remodeling → arrhythmic substrate |
| [16722579](https://pubmed.ncbi.nlm.nih.gov/16722579/) | Naxos disease; mechanochemical cell-death mechanism |
| [25824144](https://pubmed.ncbi.nlm.nih.gov/25824144/) | Carvajal syndrome (DSP) |
| [32062046](https://pubmed.ncbi.nlm.nih.gov/32062046/) / [24598986](https://pubmed.ncbi.nlm.nih.gov/24598986/) | TMEM43 ARVC-5: aggressiveness, SCD, nuclear stiffness |
| [21362707](https://pubmed.ncbi.nlm.nih.gov/21362707/) | Biventricular dysfunction strongest death/HTx predictor (HR 6.3) |
| [37474315](https://pubmed.ncbi.nlm.nih.gov/37474315/) / [41608798](https://pubmed.ncbi.nlm.nih.gov/41608798/) | Validated ARVC risk calculator; LV-LGE |
| [38499690](https://pubmed.ncbi.nlm.nih.gov/38499690/) / [39196150](https://pubmed.ncbi.nlm.nih.gov/39196150/) / [38665939](https://pubmed.ncbi.nlm.nih.gov/38665939/) | AAV9:PKP2 gene therapy prevents/rescues ARVC |
| [40021092](https://pubmed.ncbi.nlm.nih.gov/40021092/) / [32356610](https://pubmed.ncbi.nlm.nih.gov/32356610/) | DSP-ACM: LV-dominant, isolated LV-LGE |
| [41448261](https://pubmed.ncbi.nlm.nih.gov/41448261/) | Inflammation/autoimmunity/NLRP3 in hot phases |
| [40383406](https://pubmed.ncbi.nlm.nih.gov/40383406/) / [38185631](https://pubmed.ncbi.nlm.nih.gov/38185631/) / [35576477](https://pubmed.ncbi.nlm.nih.gov/35576477/) / [38736889](https://pubmed.ncbi.nlm.nih.gov/38736889/) | Single-cell/spatial: fibroblast/adipocyte expansion, NLRP3, ZBTB11, B cells |
| [41229088](https://pubmed.ncbi.nlm.nih.gov/41229088/) / [40223064](https://pubmed.ncbi.nlm.nih.gov/40223064/) | Proteomic/plasma biomarkers (UCHL1/OCIAD1/desmoyokin, CCL3) |
| [28823501](https://pubmed.ncbi.nlm.nih.gov/28823501/) | Quality-of-life burden by age/sex/shock |
| [42159538](https://pubmed.ncbi.nlm.nih.gov/42159538/) | Gene-specific sex predominance (DSP female-enriched) |
| [24962663](https://pubmed.ncbi.nlm.nih.gov/24962663/) | Boxer-dog natural model (STRN deletion) |
| [30446243](https://pubmed.ncbi.nlm.nih.gov/30446243/) / [25548613](https://pubmed.ncbi.nlm.nih.gov/25548613/) | Inheritance, ~50% genetic yield, ARVC/ALVC spectrum |
| [35268321](https://pubmed.ncbi.nlm.nih.gov/35268321/) / [27617087](https://pubmed.ncbi.nlm.nih.gov/27617087/) | Phenocopies; electrical-before-structural |
| [28779285](https://pubmed.ncbi.nlm.nih.gov/28779285/) / [30677492](https://pubmed.ncbi.nlm.nih.gov/30677492/) | Ablation limitations; sympathetic denervation |

---

## Limitations and Knowledge Gaps

1. **Gene-elusive disease (~50%):** the genetic architecture of half of probands remains undefined, limiting variant-directed prevention and therapy (F008).
2. **Penetrance/expressivity unexplained:** the "genotype-phenotype plasticity" — why family members with identical variants diverge widely — lacks a validated modifier/polygenic explanation (F008).
3. **Prognostic tools:** the ARVC risk calculator was developed largely in 2010-Task-Force-Criteria populations and may under-serve DSP/ALVC phenotypes not meeting RV-focused criteria (F006, F014).
4. **Biomarkers investigational:** CCL3, miRNAs, UCHL1/OCIAD1/desmoyokin require prospective validation before clinical use (F006, F018).
5. **Therapy evidence:** no randomized trials of exercise restriction, drug therapy, or screening; gene therapies are pre-clinical/early-phase and untested for long-term human safety/durability (F004, F016).
6. **Model limitations:** murine and iPSC systems incompletely recapitulate human RV geometry, chronic remodeling, and the immune/hot-phase component.

## Proposed Follow-up Experiments / Actions

1. **Genetics of gene-elusive ARVC:** apply large-scale WGS + polygenic risk scoring and rare-variant burden testing in gene-elusive probands and families to define missing heritability (addresses F008).
2. **Prospective biomarker validation:** multi-site cohorts to validate plasma CCL3, miR-15a-5p/16-5p/92a-3p, and UCHL1/OCIAD1/desmoyokin against arrhythmic and HF endpoints; integrate into the risk calculator (F006, F018).
3. **DSP-specific risk model:** develop and validate an ALVC/DSP-oriented risk score incorporating LV-LGE and inflammatory markers, since these patients evade RV-centric criteria (F014).
4. **Clinical translation of gene therapy:** advance AAV9:PKP2 and mutation-agnostic AAV-Cx43 to first-in-human trials with predefined safety, durability, and functional endpoints (F016).
5. **Anti-inflammatory/NLRP3 trials:** test NLRP3 inhibition and immunomodulation (guided by DSP genotype and hot-phase status) in randomized settings (F013, F017).
6. **Exercise-prescription RCTs:** quantify the dose–response of exercise restriction on phenotype progression, genotype-stratified (especially PKP2) (F003).
7. **Single-cell longitudinal atlases:** map the transition from concealed → electrical → structural phases at single-cell/spatial resolution to identify early, reversible intervention points (F017).

---

## Answer to the Research Question

Arrhythmogenic right ventricular cardiomyopathy (ARVC/MONDO:0016587) is an inherited, mostly autosomal-dominant cardiomyopathy with incomplete penetrance in which pathogenic variants in desmosomal genes (PKP2 ~40%, DSP, DSG2, DSC2, JUP) and non-desmosomal genes (TMEM43, PLN, DES, FLNC, LMNA)—identified in ~50% of patients—impair cardiomyocyte adhesion at the intercalated disc, so that mechanical stress (accelerated by endurance exercise) and inflammation drive myocyte death, plakoglobin/Hippo–YAP-mediated Wnt suppression and PPARγ/TGF-β-driven fibrofatty replacement (right-ventricular, frequently biventricular/left-dominant), and Cx43/NaV1.5 remodeling, producing life-threatening ventricular arrhythmias, sudden cardiac death, and later heart failure. Diagnosis uses the 2010 Revised Task Force/2020 Padua criteria (ECG, CMR-LGE, genetics); risk is stratified with the validated ARVC risk calculator (arrhythmia) and biventricular dysfunction (death/transplant, HR 6.3); and management—exercise restriction, beta-blockers/antiarrhythmics, catheter ablation, and the only SCD-preventive intervention, the ICD—is complemented by disease-modifying gene therapies (AAV9:PKP2; mutation-agnostic AAV-Cx43) validated in animal models. The disease occurs naturally in Boxer dogs (STRN deletion) and is modeled in Jup/Dsp/Pkp2/Tmem43 mice and patient iPSC-cardiomyocytes.


## Artifacts

- [OpenScientist final report](Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-falcon_artifacts/final_report.html)
- [OpenScientist final report](Arrhythmogenic_Right_Ventricular_Cardiomyopathy-deep-research-falcon_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 35 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 30 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001645` (2 mentions) - the report calls it "Sudden cardiac death", "Outcome"; HP calls it **Sudden cardiac death**
- `HP:0007502` (2 mentions) - the report calls it "Woolly hair"; HP calls it **Follicular hyperkeratosis**
- `HP:0001962` (1 mention) - the report calls it "Symptom"; HP calls it **Palpitations**
- `HP:0001279` (1 mention) - the report calls it "Symptom"; HP calls it **Syncope**
- `HP:0001714` (1 mention) - the report calls it "Physical/imaging"; HP calls it **Ventricular hypertrophy**
- `HP:0001644` (1 mention) - the report calls it "Physical/imaging"; HP calls it **Dilated cardiomyopathy**
- `HP:0001635` (1 mention) - the report calls it "Clinical sign"; HP calls it **Congestive heart failure**
- `HP:0012231` (1 mention) - the report calls it "Lab/ECG"; HP calls it **Serous retinal detachment**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007156` (1 mention) - the report calls it "homophilic cell adhesion via plasma-membrane adhesion molecules"; GO calls it **homophilic cell-cell adhesion**
- `GO:0005911` (2 mentions) - the report calls it "cell–cell junction / intercalated disc"; GO calls it **cell-cell junction**
- `NCBITaxon:9615` (2 mentions) - the report calls it "Canis lupus familiaris", "Boxer dog"; NCBITaxon calls it **Canis lupus familiaris**, and lists "dog" among its other names
- `HP:0004756` (2 mentions) - the report calls it "Ventricular arrhythmia"; HP calls it **Ventricular tachycardia**
- `UBERON:0002080` (1 mention) - the report calls it "right ventricle", "Organ:** heart, principally the **right ventricle"; UBERON calls it **heart right ventricle**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001645` - called "Sudden cardiac death", "Outcome"
- `NCBITaxon:9615` - called "Canis lupus familiaris", "Boxer dog"
- `UBERON:0002080` - called "right ventricle", "Organ:** heart, principally the **right ventricle"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
