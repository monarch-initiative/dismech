---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-20T01:00:42.209031'
end_time: '2026-08-20T01:13:52.384587'
duration_seconds: 790.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glioblastoma, IDH-Wildtype
  mondo_id: ''
  category: ''
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 28
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 10
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Glioblastoma_IDH_Wildtype-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Glioblastoma_IDH_Wildtype-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glioblastoma, IDH-Wildtype
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Glioblastoma, IDH-Wildtype** covering all of the
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

# Glioblastoma, IDH-Wildtype — Comprehensive Disease Characteristics Report

*Autonomous discovery investigation • WHO CNS5 (2021) framework • Evidence base: 30 papers reviewed, 2 confirmed findings, 3 supported hypotheses*

---

## Summary

**Glioblastoma, IDH-wildtype (GBM)** is the most common and most aggressive malignant primary brain tumor in adults. Under the 2021 WHO Classification of CNS Tumors (WHO CNS5), it is defined as a WHO grade-4 **diffuse astrocytic glioma** that is **wild-type for *IDH1/IDH2*** and carries at least one of three molecular hallmarks — **TERT promoter mutation**, **EGFR amplification**, or **combined whole-chromosome gain of 7 and loss of 10 (+7/−10)** — even in the absence of the classic grade-4 histological features of microvascular proliferation or necrosis (so-called "molecular GBM") ([PMID: 42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/)). This molecular definition marked a fundamental shift away from purely histological diagnosis.

Mechanistically, GBM is a **sporadic, somatic-genetic disease**. Its driver alterations converge on three core signaling axes — the **RTK/PI3K (growth factor)**, **TP53**, and **RB** pathways — with *EGFR* and *CDKN2A/B* aberrations found in essentially all tumors, and single-copy *PTEN* loss plus *TERT* promoter point mutation acting as the earliest founder events ([PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)). Downstream, the tumor establishes a profoundly **immunosuppressive microenvironment** dominated by M2-like tumor-associated macrophages, regulatory T cells, myeloid-derived suppressor cells, and hypoxia-driven tryptophan–kynurenine metabolism that drives T-cell exhaustion — the principal reason immunotherapy has largely failed in GBM.

Clinically, GBM presents in older adults (median age ~64 years, male predominance) with progressive neurological deficits, headache, and seizures. Despite maximal safe surgical resection, radiotherapy, and temozolomide (the **Stupp protocol**), median overall survival is only **~14.6 months**, rising to **~21.7 months** when the ***MGMT* promoter is methylated** — the single most important predictive/prognostic biomarker ([PMID: 41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/)). The addition of **Tumor Treating Fields (TTFields)** to maintenance temozolomide significantly improves survival (pooled HR 0.68 for both OS and PFS) ([PMID: 41741710](https://pubmed.ncbi.nlm.nih.gov/41741710/)). Five-year survival remains under ~7%. This report synthesizes disease information, etiology, phenotypes, molecular biology, mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and model systems for this entity.

---

## Section 1 — Disease Information

**Overview.** Glioblastoma, IDH-wildtype is a WHO grade-4 diffuse astrocytic tumor of the central nervous system arising from glial or glial-precursor lineage cells. It is characterized histologically (when features are present) by dense cellularity, nuclear atypia, brisk mitotic activity, **microvascular/endothelial proliferation**, and **palisading necrosis**, and biologically by diffuse infiltration of surrounding brain parenchyma that renders the tumor surgically incurable. In WHO CNS5 (2021), diagnosis no longer requires these histological features: an IDH-wildtype diffuse astrocytoma with any of the three molecular signatures (TERT promoter mutation, EGFR amplification, +7/−10) is classified as GBM ([PMID: 42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/)).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0018177 (glioblastoma); IDH-wildtype subtype under adult diffuse glioma |
| ICD-O-3 morphology | 9440/3 (glioblastoma, NOS) |
| ICD-11 | 2A00.00 (Glioblastoma of brain) |
| ICD-10 | C71.x (malignant neoplasm of brain) |
| MeSH | D005909 (Glioblastoma) |
| OMIM | 137800 (Glioma susceptibility 1) |
| SNOMED CT | 63634009 (Glioblastoma multiforme) |
| ICD-O-3 (IDH-mutant grade 4, for contrast) | 9445/3 (Astrocytoma, IDH-mutant, grade 4) ([PMID: 42581490](https://pubmed.ncbi.nlm.nih.gov/42581490/)) |

**Synonyms / alternative names.** Glioblastoma multiforme (GBM, historical), grade IV astrocytoma, "molecular GBM" (mGBM) when diagnosed by molecular criteria, "histological GBM" (hGBM) when diagnosed by classic morphology, giant cell glioblastoma and gliosarcoma (morphologic patterns). Note the 2021 reclassification **removed** "IDH-mutant glioblastoma," which is now "Astrocytoma, IDH-mutant, grade 4" — a clinically distinct, better-prognosis entity ([PMID: 42581490](https://pubmed.ncbi.nlm.nih.gov/42581490/)).

**Data source type.** The information in this report is drawn from **aggregated disease-level resources** — WHO classifications, population-based registries (SEER, Spanish and Colombian registries), multicenter cohorts (e.g., the international Histo-Mol GBM Collaborative of 1,857 patients), and mechanistic/omics studies — rather than individual EHR records.

---

## Section 2 — Etiology

**Primary causal factors.** GBM IDH-wildtype is overwhelmingly a **sporadic somatic disease**; the vast majority of tumors have no identifiable germline cause. Tumorigenesis is driven by accumulated **somatic genomic alterations** in glial/precursor cells that activate growth-factor signaling and inactivate tumor-suppressor and cell-cycle control. In multifocal GBM, comprehensive profiling proved **monoclonal origin** with early founder events (single-copy *PTEN* loss, *TERT* promoter mutation) followed by divergent clonal evolution ([PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)).

**Genetic risk factors.**
- **Somatic drivers (not inherited):** *TERT* promoter mutations, *EGFR* amplification/mutation (incl. EGFRvIII), *PTEN* loss, *CDKN2A/B* deletion, *TP53* mutation, *NF1* loss, *PIK3CA/PIK3R1*, *RB1*, *PDGFRA*, *MDM2/4* amplification.
- **Germline susceptibility (rare):** Low-penetrance GWAS loci (e.g., near *TERT*, *EGFR*, *CDKN2A/B*, *RTEL1*, *TP53*). Hereditary cancer syndromes predispose to gliomas: **Li-Fraumeni** (*TP53*), **Lynch/constitutional mismatch-repair deficiency**, **neurofibromatosis type 1** (*NF1*), and **Turcot syndrome**. OMIM 137800 catalogs glioma susceptibility.

**Environmental risk factors.**
- **Ionizing radiation** to the head (e.g., prior therapeutic cranial irradiation) is the only firmly established exogenous risk factor.
- **Age** (rising incidence with age, peak 65–75), **male sex** (male predominance; male sex an independent adverse survival factor, HR ~1.37 in one registry) ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)), and **European/White ancestry** (higher incidence) are demographic risk factors.
- No consistent causal role has been established for mobile-phone radiofrequency exposure, occupational chemicals, diet, or head trauma.

**Protective factors.** Epidemiological studies have repeatedly noted an **inverse association with atopic/allergic disease and elevated IgE**, suggesting immune surveillance may be protective, though this is correlative. No validated genetic protective allele is established. No dietary or lifestyle factor has robust protective evidence.

**Gene–environment interactions.** The clearest example is prior **therapeutic ionizing radiation** interacting with germline DNA-repair deficiency (e.g., mismatch-repair or *TP53* pathway defects) to accelerate secondary glioma formation. Otherwise GxE data are sparse for this tumor.

---

## Section 3 — Phenotypes

GBM phenotypes are **neurological signs and symptoms** produced by mass effect, infiltration, edema, and disruption of eloquent brain regions. Onset is **adult/geriatric**, course is **progressive** and typically **subacute** (symptoms often < 3 months), and severity is **moderate-to-severe** with major quality-of-life impact.

| Phenotype | Type | HPO term | Frequency / notes |
|---|---|---|---|
| Headache | Symptom | HP:0002315 | Very common; often progressive, worse in morning |
| Seizures | Sign/symptom | HP:0001250 | Seizure at onset in ~25–60%; ~28% (49/177) in one IDH-WT cohort ([PMID: 34794192](https://pubmed.ncbi.nlm.nih.gov/34794192/)) |
| Focal motor weakness / hemiparesis | Sign | HP:0001269 / HP:0002061 | Common; slowly progressive neurological deficit ([PMID: 29248175](https://pubmed.ncbi.nlm.nih.gov/29248175/)) |
| Aphasia / speech disturbance (dysphasia) | Sign | HP:0002381 | With dominant temporoparietal lesions ([PMID: 29062690](https://pubmed.ncbi.nlm.nih.gov/29062690/)) |
| Cognitive/behavioral change | Behavioral | HP:0000708 | Personality change, confusion ([PMID: 42607912](https://pubmed.ncbi.nlm.nih.gov/42607912/)) |
| Nausea/vomiting, papilledema (raised ICP) | Sign | HP:0002017 / HP:0001085 | From mass effect and edema |
| Cognitive decline | Symptom | HP:0100543 | Progressive with tumor growth/treatment |

**Phenotype–anatomy correlation.** In IDH-WT GBM presenting with seizures, lesions are disproportionately located in the **parietal lobe**, **left/dominant hemisphere**, and involve the **subventricular zone (SVZ)**; seizure-onset tumors are typically smaller at diagnosis, and generalized seizure at onset associated with longer overall survival ([PMID: 34794192](https://pubmed.ncbi.nlm.nih.gov/34794192/)). Speech arrest / paroxysmal dysphasia can localize to the dominant temporal lobe ([PMID: 29062690](https://pubmed.ncbi.nlm.nih.gov/29062690/)).

**Quality of life.** GBM severely impairs daily functioning through neurological deficits, seizures, fatigue, corticosteroid side effects, and cognitive decline; performance status (KPS) is both a QoL indicator and a strong prognostic factor. Higher intratumoral serotonin was associated with better patient-reported general health in one biobank cohort ([PMID: 42377764](https://pubmed.ncbi.nlm.nih.gov/42377764/)).

---

## Section 4 — Genetic / Molecular Information

**Defining and causal genes (somatic).** GBM IDH-wildtype is *diagnosed by molecular criteria*. Per WHO CNS5, any IDH-wildtype diffuse astrocytoma with **TERT promoter mutation**, **EGFR amplification**, or **+7/−10** is GBM ([PMID: 42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/)). The confirmed molecular architecture (Finding F001) is that all tumors harbor alterations across three core pathways:

> *"All tumors harbored alterations in the 3 GBM core pathways: RTK/PI3K, p53, and RB regulatory pathways with aberrations of EGFR and CDKN2A/B in all (100%) patients."* — [PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)

> *"Only 2 events were found to be early in all patients: single copy loss of PTEN and TERT promoter point mutations."* — [PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)

| Gene (HGNC) | Alteration | Pathway | Consequence |
|---|---|---|---|
| *TERT* | Promoter point mutation (C228T/C250T) | Telomere maintenance | GoF — telomerase reactivation (early founder) |
| *EGFR* | Amplification, EGFRvIII, mutation | RTK/PI3K | GoF — constitutive growth signaling |
| *PTEN* | Single-copy loss / mutation | RTK/PI3K–AKT | LoF (early founder) |
| *CDKN2A/B* | Homozygous deletion | RB / cell cycle | LoF — loss of p16/p14ARF |
| *TP53* | Mutation / *MDM2/4* amplification | p53 | LoF — apoptosis/senescence escape |
| *NF1* | Mutation / deletion | RTK/RAS | LoF — RAS activation |
| *RB1* | Deletion / mutation | RB | LoF — cell-cycle deregulation |
| *PDGFRA*, *PIK3CA/R1*, *MET* | Amplification/mutation | RTK/PI3K | GoF |
| Chr 7 gain / Chr 10 loss (+7/−10) | Aneuploidy | Multiple | Diagnostic hallmark |

**Variant classification / origin.** These are **somatic** alterations (COSMIC/TCGA), not germline; standard ACMG germline pathogenicity classification does not apply. Population allele frequencies (gnomAD) are irrelevant since these arise somatically. Functional consequences are a mix of **gain-of-function** (EGFR, TERT, PDGFRA amplifications) and **loss-of-function** (PTEN, CDKN2A/B, TP53, NF1, RB1). EGFR pathway alterations are also prognostically adverse, correlating with rapid early progression ([PMID: 41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/)).

**Epigenetic information.** The most clinically important epigenetic mark is ***MGMT* promoter methylation**, which silences the DNA-repair enzyme O6-methylguanine-DNA methyltransferase, sensitizing tumors to alkylating chemotherapy (see Sections 10–12). DNA-methylation profiling (methylation-class subgrouping) is increasingly used for diagnosis. GBM lacks the **G-CIMP** hypermethylator phenotype that characterizes IDH-mutant gliomas.

**Modifier genes.** MGMT methylation status modifies both chemosensitivity and the survival benefit of surgical cytoreduction ([PMID: 41680847](https://pubmed.ncbi.nlm.nih.gov/41680847/)). An 11-gene malignant–myeloid interaction signature (incl. *TPST1*, *CHI3L1*, *NNMT*) modifies prognosis and immunotherapy response ([PMID: 41838327](https://pubmed.ncbi.nlm.nih.gov/41838327/)).

**Chromosomal abnormalities.** Whole-chromosome **+7 gain and −10 loss** is near-universal and diagnostic; focal amplifications (EGFR, PDGFRA, MDM2, CDK4/6) and homozygous deletions (CDKN2A/B, PTEN) are frequent. GBM genomes are highly aneuploid.

---

## Section 5 — Environmental Information

- **Environmental factors (CTD/EPA domain):** **Ionizing radiation** is the only established environmental cause. No consistent evidence implicates pesticides, industrial solvents, formaldehyde, or air pollution as causal, though these remain under study.
- **Lifestyle factors:** No robust causal lifestyle factor. Smoking, alcohol, and diet have not shown consistent associations. Antidepressant (SSRI) use is common among patients; fluoxetine/sertraline were associated with better survival than other SSRIs (HR 0.62, 95% CI 0.44–0.88) in an observational cohort — hypothesis-generating, not causal ([PMID: 42377764](https://pubmed.ncbi.nlm.nih.gov/42377764/)).
- **Infectious agents:** No pathogen is an established cause. **CMV** nucleic acids/antigens have been detected in GBM tissue by some groups, but a causal role is unproven and contested. Importantly, **cerebral cryptococcoma** and other infectious masses can radiologically *mimic* GBM, a diagnostic pitfall ([PMID: 42607912](https://pubmed.ncbi.nlm.nih.gov/42607912/)).

---

## Section 6 — Mechanism / Pathophysiology

**Molecular pathways.** GBM biology is organized around three convergent core pathways ([PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)):
1. **RTK/PI3K–AKT–mTOR** growth signaling (EGFR/PDGFRA/MET amplification, PTEN loss, PIK3CA) — GO:0038083, KEGG hsa05214.
2. **TP53** apoptosis/senescence axis (TP53 mutation, MDM2/4, CDKN2A/*p14ARF*) — GO:0072331.
3. **RB / cell-cycle control** (CDKN2A/B deletion, RB1 loss, CDK4/6, CCND2) — GO:0007049, GO:0000082.
Plus **telomere maintenance** via TERT reactivation — GO:0007004.

**Causal chain (upstream → downstream).**
```
Somatic founder events                 Core-pathway convergence            Malignant phenotype
(PTEN loss, TERT promoter mut.)  ─►  RTK/PI3K↑ + p53↓ + RB↓ + TERT↑  ─►  uncontrolled proliferation,
                                                                          apoptosis evasion, immortalization
        │                                                                         │
        ▼                                                                         ▼
  Clonal evolution / intratumoral        Angiogenesis (VEGF), hypoxia/           Diffuse infiltration,
  heterogeneity (monoclonal origin) ─►   necrosis, glioma stem cells        ─►   necrosis, microvascular
                                                                                 proliferation
                                                     │
                                                     ▼
                            Immunosuppressive tumor microenvironment (TAMs/MDSCs/Treg,
                            IDO1–kynurenine, T-cell exhaustion) ─► immune escape, treatment resistance
                                                     │
                                                     ▼
                            Progressive neurological deficits, seizures, death (~14.6 mo)
```

**Cellular processes.** Sustained proliferation, evasion of apoptosis, replicative immortality, angiogenesis, invasion/infiltration, and maintenance of a **glioma stem-cell** compartment. Hypoxia drives pseudopalisading necrosis and VEGF-mediated neovascularization.

**Immune system involvement — a defining feature.** GBM builds an intensely **immunosuppressive TME**. Tumor-associated macrophages (M2-like), regulatory T cells, MDSCs, dysfunctional NK and dendritic cells, and exhausted CD8+ T cells cooperate to enforce immune escape; low neoantigen burden, antigenic heterogeneity, and poor immune infiltration further blunt immunity ([PMID: 42383800](https://pubmed.ncbi.nlm.nih.gov/42383800/)). A **hypoxia-driven tryptophan–kynurenine metabolic circuit** is central:

> *"the axis of hypoxia-driven tryptophan degradation … IDO1/TDO2-mediated breakdown of tryptophan and the consequent accumulation of kynurenine, a metabolite that triggers GCN2- and AHR-mediated CD8+ T-cell exhaustion and supports regulatory T-cell differentiation and expansion."* — [PMID: 41893336](https://pubmed.ncbi.nlm.nih.gov/41893336/)

Glial cells (astrocytes, microglia, oligodendrocyte-lineage) spatially organize immune cells into **immunosuppressive niches / spatial microdomains** that foster local T-cell exhaustion and coordinated immune escape ([PMID: 42613643](https://pubmed.ncbi.nlm.nih.gov/42613643/)). Malignant–myeloid crosstalk (e.g., an 11-gene signature including *TPST1*, via PTN–NCL and EREG/AREG–EGFR signaling) shapes the immunosuppressive milieu and predicts poor prognosis/immunotherapy resistance ([PMID: 41838327](https://pubmed.ncbi.nlm.nih.gov/41838327/)).

**Metabolic changes.** Aerobic glycolysis (Warburg effect), hypoxia-inducible metabolism, and tryptophan catabolism (IDO1/TDO2 → kynurenine, driving VEGFA via the Trp–GCN2–ATF4 axis, linking immunosuppression to angiogenesis) ([PMID: 41893336](https://pubmed.ncbi.nlm.nih.gov/41893336/)). Intratumoral serotonin/5-HIAA metabolism is measurable and linked to patient-reported wellbeing ([PMID: 42377764](https://pubmed.ncbi.nlm.nih.gov/42377764/)).

**Tissue damage mechanisms.** Oxidative stress, hypoxia/ischemia, pseudopalisading necrosis, blood–brain-barrier breakdown with vasogenic edema, and destruction of eloquent neural tissue.

**Molecular profiling & advanced technologies.** Multi-omics/single-cell/spatial-transcriptomic studies reveal profound **intratumoral heterogeneity** and immune spatial architecture ([PMID: 41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/), [PMID: 42613643](https://pubmed.ncbi.nlm.nih.gov/42613643/)). Integrative multi-omics defined the malignant–myeloid interaction signature that outperformed standard clinicopathological factors ([PMID: 41838327](https://pubmed.ncbi.nlm.nih.gov/41838327/)).

**Suggested GO/CL terms.** GO:0006954 (inflammatory response), GO:0001525 (angiogenesis), GO:0006979 (response to oxidative stress), GO:0002829/GO:0002534 (immunosuppression); CL:0000878 (CNS macrophage/microglia), CL:0000129 (glial cell), CL:0000784/CL:0000815 (dendritic/regulatory T cell), CL:0000127 (astrocyte), glioma stem cell.

---

## Section 7 — Anatomical Structures Affected

**Organ level.** Primary organ: the **brain** (UBERON:0000955), a nervous-system malignancy. Most common site: **cerebral hemispheres / supratentorial white matter**, especially the **frontal** and **temporal lobes**; spread along white-matter tracts and across the **corpus callosum** ("butterfly glioma") is characteristic ([PMID: 29248175](https://pubmed.ncbi.nlm.nih.gov/29248175/)). Rare extension to dura, galea, and calvarium ([PMID: 29248175](https://pubmed.ncbi.nlm.nih.gov/29248175/)). Body system: **central nervous system** (UBERON:0001017).

| Structure | UBERON | Note |
|---|---|---|
| Brain | UBERON:0000955 | Primary organ |
| Cerebral hemisphere / cerebrum | UBERON:0001869 | Most common location |
| Frontal lobe | UBERON:0016525 | Frequent |
| Temporal lobe | UBERON:0001871 | Frequent; dominant-lobe speech deficits |
| Parietal lobe | UBERON:0001872 | Enriched in seizure-onset tumors ([PMID: 34794192](https://pubmed.ncbi.nlm.nih.gov/34794192/)) |
| Corpus callosum | UBERON:0002336 | Butterfly spread |
| Subventricular zone | UBERON:0004024 | Putative origin; SVZ involvement in seizure-onset GBM ([PMID: 34794192](https://pubmed.ncbi.nlm.nih.gov/34794192/)) |

**Tissue / cell level.** Nervous tissue; malignant **astrocyte/glial-lineage** cells and **glioma stem cells**; heavy infiltration by tumor-associated macrophages/microglia and other immune cells. CL terms: CL:0000127 (astrocyte), CL:0000129 (glial cell), CL:0000878 (CNS macrophage/microglia).

**Subcellular level.** Nucleus (GO:0005634 — genomic instability, TP53/RB dysregulation), plasma membrane/cytoplasm (GO:0005886 — EGFR/RTK signaling), mitochondria (GO:0005739 — altered metabolism), telomeres (GO:0000781 — TERT reactivation).

**Localization / lateralization.** Typically **unilateral** but diffusely infiltrative and often **multilobar** (multilobar involvement ~65% on MRI in molecular GBM) ([PMID: 41619575](https://pubmed.ncbi.nlm.nih.gov/41619575/)); can be multifocal/multicentric (monoclonal) ([PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)). Left/dominant hemisphere predominance in seizure-onset cases ([PMID: 34794192](https://pubmed.ncbi.nlm.nih.gov/34794192/)).

---

## Section 8 — Temporal Development

- **Onset:** Adult/geriatric; median age ~61–64 years; ~46.5% of patients are ≥65 years ([PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)). Onset is **subacute/insidious**, with symptoms typically < 3 months.
- **Progression:** **Rapid and progressive.** GBM is WHO **grade 4** (highest grade); there is no formal TNM staging for primary brain tumors. **Rapid early progression (REP)** — MRI progression after resection but before adjuvant therapy — occurs in ~45–50% and correlates with **EGFR pathway alterations** (multivariate p=0.006) ([PMID: 41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/)).
- **Course pattern:** Relentlessly **progressive**; near-universal recurrence after initial therapy. Disease is effectively **chronic-lethal** over months.
- **Remission / critical periods:** True remission is rare; treatment-induced responses are temporary. Timing of chemoradiation initiation matters — starting chemoradiotherapy 32–49 days post-surgery independently improved outcome in MGMT-methylated patients ([PMID: 42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/)). Prognosis is dynamic — conditional survival improves markedly with time survived (in giant-cell GBM, projected 5-yr survival rose from a 14% baseline to 69–83% among 3–4-year survivors) ([PMID: 42189411](https://pubmed.ncbi.nlm.nih.gov/42189411/)).

---

## Section 9 — Inheritance and Population

**Epidemiology.** GBM is the **most common malignant primary brain tumor in adults** — ~27.9% of malignant CNS tumors in one registry ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)); ~50.1% of high-grade gliomas were IDH-wildtype GBM in a Spanish cohort ([PMID: 41133515](https://pubmed.ncbi.nlm.nih.gov/41133515/)). Incidence is roughly **3–5 per 100,000 per year** and rising in recent series ([PMID: 41133515](https://pubmed.ncbi.nlm.nih.gov/41133515/)).

**Inheritance.** Essentially **sporadic/somatic**; not Mendelian. Susceptibility is **multifactorial/polygenic** (low-penetrance GWAS loci) with rare high-penetrance familial cancer syndromes (Li-Fraumeni, Lynch/CMMRD, NF1, Turcot). Concepts of penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are **generally not applicable** to this somatic tumor except within the rare inherited syndromes.

**Population demographics.**
- **Sex:** **Male predominance** (~1.4–1.6:1); male sex an independent adverse prognostic factor (HR ~1.37) ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)).
- **Age:** Peak incidence 65–75; older age strongly worsens survival, with steepest decline ≥70 years ([PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)).
- **Ancestry/geography:** Higher incidence in White/European-ancestry populations; global data limited, particularly in Latin America ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)).

---

## Section 10 — Diagnostics

**Imaging (first-line).** Contrast-enhanced **MRI** is the primary modality: a heterogeneously **ring-enhancing** mass with central necrosis, surrounding FLAIR-hyperintense vasogenic edema, mass effect, and midline shift. However, **molecular GBM often mimics low-grade glioma** — enhancement absent in ~39% or faint; infiltrative FLAIR abnormality nearly constant, multilobar in ~65%, diffusion restriction in ~64%, and elevated rCBV (>1.75) in ~88% — so infiltrative FLAIR, multilobar spread, diffusion restriction, or high perfusion should raise suspicion, especially in older patients ([PMID: 41619575](https://pubmed.ncbi.nlm.nih.gov/41619575/)). Advanced **18F-FDG PET/MRI** discriminates high-grade/IDH-wildtype status (SUVmax AUC 0.938; CBF AUC 0.875/0.825) ([PMID: 41913661](https://pubmed.ncbi.nlm.nih.gov/41913661/)).

**Histopathology / IHC (gold standard).** Tissue diagnosis via resection or **biopsy** (biopsy more common in molecular GBM, ~69% vs 30%, and in older/frailer patients) ([PMID: 41504931](https://pubmed.ncbi.nlm.nih.gov/41504931/), [PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)). Histology: pleomorphic astrocytic tumor with mitoses, microvascular proliferation, necrosis. IHC: **GFAP+, S-100+, OLIG2+, CD68+ (macrophages), p53** ([PMID: 29248175](https://pubmed.ncbi.nlm.nih.gov/29248175/)); IDH1 R132H immunonegativity supports IDH-wildtype status.

**Molecular/genetic testing (now diagnostic).** Required per WHO CNS5:
- **IDH1/IDH2** status (IHC + sequencing) — must be wild-type.
- **TERT promoter** mutation, **EGFR** amplification (FISH/NGS), **chromosome +7/−10** (CMA/NGS) — any one defines GBM ([PMID: 42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/)).
- ***MGMT* promoter methylation** — predictive/prognostic (methylation-specific PCR/pyrosequencing).
- **CDKN2A/B, PTEN, TP53, NF1, PIK3CA, MTAP** via **NGS panels** — prognostic/therapeutic ([PMID: 41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/)).
- **DNA-methylation array classification** for difficult cases.
Molecular testing is applied less comprehensively in older patients, a care disparity ([PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)).

**Clinical criteria.** 2021 **WHO CNS5** classification; cIMPACT-NOW updates 8–11 refine the framework ([PMID: 42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/)).

**Differential diagnosis.** Brain metastasis, primary CNS lymphoma, IDH-mutant astrocytoma grade 4, oligodendroglioma, abscess, demyelination, and — critically — **infectious mass lesions such as cerebral cryptococcoma**, which can radiologically mimic high-grade glioma even in immunocompetent hosts (serum/CSF cryptococcal antigen aids differentiation) ([PMID: 42607912](https://pubmed.ncbi.nlm.nih.gov/42607912/)).

**Screening.** No population-level screening exists or is recommended; the disease is sporadic, rapidly progressive, and lacks an asymptomatic detectable window.

---

## Section 11 — Outcome / Prognosis

**Survival — dismal.** Median overall survival with standard care is **~14.6 months** overall (Finding F002):

> *"The standard Stupp protocol (60 Gy/30 fractions with temozolomide [TMZ]) improves overall survival (OS) to 14.6 months, with greater benefits in O6-methylguanine-DNA methyltransferase (MGMT)-methylated tumors (21.7 months)."* — [PMID: 41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/)

5-year survival is ~7% or lower. Real-world median OS was ~12.9 months in a population-based surgical cohort ([PMID: 41733819](https://pubmed.ncbi.nlm.nih.gov/41733819/)); glioblastoma carried the worst prognosis among CNS tumors in a registry (~20.9% survival in mixed cohorts; HR 9.64) ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)).

**Prognostic factors (multiple validated):**
| Factor | Direction | Evidence |
|---|---|---|
| ***MGMT* promoter methylation** | Favorable (predictive + prognostic) | 21.7 vs 14.6 mo ([PMID: 41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/)); EF-14 methylated OS 31.6 mo ([PMID: 41741710](https://pubmed.ncbi.nlm.nih.gov/41741710/)) |
| **Extent of resection** | Favorable | RANO class 1 (supramaximal) OS 21.0 vs 4.5 mo for class 4 ([PMID: 41733819](https://pubmed.ncbi.nlm.nih.gov/41733819/)) |
| **Younger age** | Favorable | mOS 19.2 (<65) vs 15.0 (≥65) mo ([PMID: 40971171](https://pubmed.ncbi.nlm.nih.gov/40971171/)) |
| **Good performance status (KPS/NANO)** | Favorable | Preoperatively intact = longer OS ([PMID: 41733819](https://pubmed.ncbi.nlm.nih.gov/41733819/)) |
| **Treatment intensity / adjuvant completion** | Favorable | Independent predictor ([PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)) |
| **EGFR pathway alteration** | Adverse (rapid early progression) | REP multivariate p=0.006 ([PMID: 41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/)) |
| **Male sex, higher grade** | Adverse | HR 1.37 / 7.46 ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)) |
| **11-gene malignant–myeloid signature** | Adverse; outperforms standard factors | ([PMID: 41838327](https://pubmed.ncbi.nlm.nih.gov/41838327/)) |

**Morbidity/QoL.** Progressive neurological disability, seizures, cognitive decline, and dependency; performance status is central to both prognosis and QoL. Prognosis is **dynamic** — conditional survival improves substantially for those surviving the high-risk early years ([PMID: 42189411](https://pubmed.ncbi.nlm.nih.gov/42189411/)).

---

## Section 12 — Treatment

**Standard of care — the Stupp protocol.** Maximal safe surgical resection → **concurrent radiotherapy (60 Gy/30 fractions) + temozolomide** → adjuvant temozolomide (NCIT: C62554 Temozolomide; C15313 Radiation Therapy; C15329 Surgery). Protocol completion significantly improves OS in both MGMT-methylated and unmethylated patients (p<0.0001) ([PMID: 42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/)). Optimizations: initiate chemoradiation ~32–49 days post-surgery, add stereotactic sequential boost in methylated patients, minimize dexamethasone (≥1.2 mg/m² worsens outcomes), and avoid age bias ([PMID: 42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/)).

**Tumor Treating Fields (TTFields)** (NCIT: C118835). Alternating electric fields added to maintenance TMZ significantly prolong survival (Finding F002, Hypothesis H003):

> *"Pooled analysis showed that TTFields significantly improved OS, HR = 0.68, 95% CI 0.60–0.78, p < 0.0001"* — [PMID: 41741710](https://pubmed.ncbi.nlm.nih.gov/41741710/)

(also PFS HR 0.68; EF-14 MGMT-methylated median OS 31.6 months).

**Pharmacotherapy / pharmacogenomics.** Temozolomide is the backbone alkylator; its efficacy depends on **MGMT** methylation — a pharmacogenomic biomarker where the unmethylated (active) enzyme repairs O6-methylguanine and confers resistance ([PMID: 41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/)). Bevacizumab (anti-VEGF; NCIT: C2039) is used for recurrence/edema (improves PFS, not OS). Lomustine and other nitrosoureas at recurrence.

**Immunotherapy — largely unsuccessful to date.** Checkpoint inhibitors, CAR-T, and vaccines have shown limited efficacy owing to the immunosuppressive TME, low neoantigen burden, and antigenic heterogeneity ([PMID: 42383800](https://pubmed.ncbi.nlm.nih.gov/42383800/)). Emerging strategies combine checkpoint blockade with metabolic reprogramming, myeloid modulation, and interferon reactivation, guided by spatial/single-cell biomarkers ([PMID: 41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/)). Metabolic-immune targeting (IDO1 inhibitor BMS-986205 + nivolumab + RT) was safe in a phase I trial (RP2D 50 mg; NCT04047706) ([PMID: 42189896](https://pubmed.ncbi.nlm.nih.gov/42189896/)).

**Surgical.** Maximal safe / **supramaximal resection** is a strong independent survival predictor; mild-to-moderate new postoperative deficits did not reduce survival, supporting aggressive resection ([PMID: 41733819](https://pubmed.ncbi.nlm.nih.gov/41733819/)). Re-resection at recurrence benefits patients, with benefit modulated by MGMT status (greater residual-volume effect in unmethylated tumors) ([PMID: 41680847](https://pubmed.ncbi.nlm.nih.gov/41680847/)).

**Elderly-specific strategy.** Fit patients <70 benefit from conventionally fractionated chemoradiation; **hypofractionated** regimens are appropriate ≥70 ([PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)). Age alone should not dictate therapy — fit elderly with good KPS and MGMT methylation achieve outcomes similar to younger patients on standard protocols ([PMID: 40971171](https://pubmed.ncbi.nlm.nih.gov/40971171/)).

**Supportive care.** Antiepileptics for seizures, corticosteroids (minimized) for edema, rehabilitation, and palliative care.

**Personalized medicine.** MGMT-stratified surgical and radiotherapy decision-making ([PMID: 41680847](https://pubmed.ncbi.nlm.nih.gov/41680847/), [PMID: 42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/)); NGS-guided identification of EGFR-driven rapid progressors for expedited adjuvant therapy ([PMID: 41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/)).

---

## Section 13 — Prevention

- **Primary prevention:** No established modifiable strategy exists, as GBM lacks proven controllable causes. Avoiding unnecessary therapeutic cranial ionizing radiation is the only rational measure.
- **Secondary prevention / screening:** No population screening — rapid progression and lack of an asymptomatic detectable phase make screening impractical.
- **Tertiary prevention:** Optimizing treatment (complete resection, protocol completion, TTFields, seizure/edema control, minimizing dexamethasone) to delay progression and preserve function ([PMID: 42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/)).
- **Immunization / behavioral / public-health / prophylaxis:** Not applicable — no vaccine, no validated lifestyle prevention, no infectious cause to interrupt.
- **Genetic counseling:** Relevant only for the rare hereditary cancer syndromes (Li-Fraumeni, Lynch/CMMRD, NF1) that predispose to gliomas.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** Primarily **Homo sapiens** (NCBI:txid9606). Naturally occurring glioma is well recognized in **dogs** (*Canis lupus familiaris*, NCBI:txid9615), especially brachycephalic breeds (Boxer, Boston Terrier, Bulldog), making canine glioma a valued spontaneous comparative model. Gliomas also occur in cats and other mammals.
- **Breed:** Brachycephalic dog breeds are over-represented (VBO breed identifiers apply to canine breeds such as Boxer, Boston Terrier).
- **Orthologous genes:** Core drivers are conserved — *Egfr*, *Pten*, *Tp53*, *Cdkn2a*, *Nf1*, *Rb1*, *Tert* have clear mouse/rat/dog orthologs (NCBI Gene).
- **Comparative biology:** Canine gliomas share histological features and some pathway alterations (RTK/PI3K, cell cycle) with human GBM, though molecular concordance is incomplete; they are used to study invasion, imaging, and therapy. Evolutionary conservation of the RTK/PI3K, p53, and RB pathways underlies cross-species relevance.
- **Transmission:** Not applicable — GBM is a non-transmissible somatic neoplasm with **no zoonotic potential**.

---

## Section 15 — Model Organisms

- **Model types:** Mammalian in vivo (mouse, rat), cell lines, patient-derived xenografts (PDX), organoids, and iPSC/neural-stem-cell–derived systems.
- **Mouse genetic models:** **Genetically engineered mouse models (GEMMs)** combining core-pathway lesions recapitulate GBM: *Nf1/Trp53/Pten* conditional knockouts, *EGFRvIII* transgenics, and RCAS/tv-a and Cre-lox conditional systems targeting glial/neural progenitors. These reproduce diffuse infiltration, necrosis, and the three-pathway (RTK/PI3K, p53, RB) architecture confirmed in human tumors ([PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)).
- **Xenograft / PDX / organoid models:** Human GBM lines (e.g., U87, U251) and glioma-stem-cell–enriched PDX/organoids preserve intratumoral heterogeneity and are used for drug testing; single-cell and spatial platforms increasingly interrogate the immune microenvironment ([PMID: 41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/)).
- **Phenotype recapitulation:** GEMMs and orthotopic models reproduce invasion, angiogenesis, necrosis, and immunosuppressive myeloid infiltration; syngeneic models (GL261, CT-2A) are standard for immunotherapy studies.
- **Limitations:** Mouse models incompletely capture human intratumoral/spatial heterogeneity, the mature human immune microenvironment, TERT-promoter biology, and blood–brain-barrier pharmacology — a key reason therapies effective in mice often fail clinically ([PMID: 42383800](https://pubmed.ncbi.nlm.nih.gov/42383800/), [PMID: 41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/)).
- **Resources:** MGI, IMPC/KOMP (mouse alleles), Cellosaurus/ATCC (cell lines), and spontaneous canine glioma cohorts (comparative oncology).

---

## Mechanistic Model / Integrated Interpretation

GBM IDH-wildtype is best understood as a **convergent somatic-genetic disease with an immunosuppressive systems-level phenotype**. Two early founder events (single-copy *PTEN* loss, *TERT* promoter mutation) initiate a monoclonal tumor that universally acquires lesions across three core pathways — **RTK/PI3K** (proliferation/survival), **p53** (apoptosis/senescence escape), and **RB** (cell-cycle deregulation) — with EGFR and CDKN2A/B involved in essentially all tumors ([PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/)). This genomic program yields diffuse infiltration, angiogenesis, hypoxia-driven necrosis, and a glioma-stem-cell reservoir. Downstream, glial cells organize a spatially structured, **immunosuppressive microenvironment** (M2 TAMs, MDSCs, Treg, IDO1–kynurenine-driven T-cell exhaustion) that enforces immune escape and treatment resistance ([PMID: 42613643](https://pubmed.ncbi.nlm.nih.gov/42613643/), [PMID: 41893336](https://pubmed.ncbi.nlm.nih.gov/41893336/), [PMID: 42383800](https://pubmed.ncbi.nlm.nih.gov/42383800/)). Clinically this manifests as older adults with progressive deficits/seizures and a ~14.6-month median survival despite trimodal therapy, with **MGMT methylation** the dominant lever on chemosensitivity and **extent of resection** the dominant surgical lever ([PMID: 41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/), [PMID: 41733819](https://pubmed.ncbi.nlm.nih.gov/41733819/)).

---

## Evidence Base — Key Literature

| PMID | Contribution | Support / challenge |
|---|---|---|
| [42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/) | WHO CNS5 molecular definition of GBM | Supports F001 / H001 |
| [28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/) | Three core pathways; EGFR/CDKN2A/B in 100%; PTEN/TERT founders; monoclonal origin | Supports F001 / H001 |
| [41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/) | Stupp OS 14.6 mo; MGMT-methylated 21.7 mo | Supports F002 / H002 |
| [41741710](https://pubmed.ncbi.nlm.nih.gov/41741710/) | TTFields meta-analysis OS/PFS HR 0.68 | Supports F002 / H003 |
| [42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/) | Stupp optimization; timing, dexamethasone, boost | Supports treatment section |
| [41733819](https://pubmed.ncbi.nlm.nih.gov/41733819/) | Extent of resection & neurological status prognostic | Supports prognosis/surgery |
| [41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/) | EGFR alterations → rapid early progression | Supports temporal/prognosis |
| [42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/) | Age, treatment intensity, MGMT predict survival; elderly care | Epidemiology/treatment |
| [41504931](https://pubmed.ncbi.nlm.nih.gov/41504931/) | mGBM vs hGBM outcomes (WHO CNS5) | Disease info/diagnostics |
| [41619575](https://pubmed.ncbi.nlm.nih.gov/41619575/) | MRI features of molecular GBM | Diagnostics |
| [41913661](https://pubmed.ncbi.nlm.nih.gov/41913661/) | FDG-PET/MRI for grade/IDH status | Diagnostics |
| [42613643](https://pubmed.ncbi.nlm.nih.gov/42613643/) | Glial-organized immune niches | Mechanism/immunity |
| [41893336](https://pubmed.ncbi.nlm.nih.gov/41893336/) | IDO1–kynurenine → T-cell exhaustion | Mechanism/immunity |
| [42383800](https://pubmed.ncbi.nlm.nih.gov/42383800/) | Immunosuppressive TME; immunotherapy barriers | Mechanism/treatment |
| [41838327](https://pubmed.ncbi.nlm.nih.gov/41838327/) | 11-gene malignant–myeloid signature; TPST1 | Mechanism/prognosis |
| [34794192](https://pubmed.ncbi.nlm.nih.gov/34794192/) | Seizure phenotype localization | Phenotypes |
| [41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/) | Registry epidemiology/prognosis | Epidemiology |
| [41133515](https://pubmed.ncbi.nlm.nih.gov/41133515/) | Incidence IDH-WT GBM vs IDH-mutant | Epidemiology |
| [42607912](https://pubmed.ncbi.nlm.nih.gov/42607912/) | Cryptococcoma mimicking GBM | Differential dx |
| [42189896](https://pubmed.ncbi.nlm.nih.gov/42189896/) | Phase I RT+nivolumab+IDO1 inhibitor | Experimental treatment |
| [42581490](https://pubmed.ncbi.nlm.nih.gov/42581490/) | WHO 2021 reclassification of IDH-mutant GBM | Disease info |
| [42377764](https://pubmed.ncbi.nlm.nih.gov/42377764/) | Serotonin/antidepressants, QoL | Environmental/QoL |
| [42189411](https://pubmed.ncbi.nlm.nih.gov/42189411/) | Conditional survival dynamics | Temporal/prognosis |
| [40971171](https://pubmed.ncbi.nlm.nih.gov/40971171/) | Elderly on standard protocol | Treatment |
| [41680847](https://pubmed.ncbi.nlm.nih.gov/41680847/) | MGMT modifies re-resection benefit | Treatment |
| [41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/) | Precision immunotherapy framework | Treatment/mechanism |
| [29248175](https://pubmed.ncbi.nlm.nih.gov/29248175/) | Calvarial GBM, IHC markers | Anatomy/diagnostics |
| [29062690](https://pubmed.ncbi.nlm.nih.gov/29062690/) | Temporal-lobe epilepsy presentation | Phenotypes |
| [27893285](https://pubmed.ncbi.nlm.nih.gov/27893285/) | Molecular subtyping of CNS tumors | Disease info |

---

## Limitations and Knowledge Gaps

1. **No primary data analysis.** This report is a literature/knowledge synthesis under WHO CNS5; no patient-level dataset was analyzed in the investigation.
2. **Retrospective/observational bias.** Much survival and prognostic evidence comes from registries and retrospective cohorts subject to selection and indication bias (e.g., resection favoring fitter patients) ([PMID: 41504931](https://pubmed.ncbi.nlm.nih.gov/41504931/)).
3. **Immunotherapy mechanisms outpace clinical benefit.** Elegant TME biology has not yet translated to survival gains; predictive biomarkers remain unvalidated prospectively ([PMID: 42383800](https://pubmed.ncbi.nlm.nih.gov/42383800/), [PMID: 41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/)).
4. **Etiology largely unexplained.** Beyond ionizing radiation and rare syndromes, the causes of sporadic GBM are unknown; no actionable prevention exists.
5. **Underdiagnosis of molecular GBM.** mGBM mimics low-grade glioma radiologically, risking treatment delays ([PMID: 41619575](https://pubmed.ncbi.nlm.nih.gov/41619575/)); molecular testing is applied unevenly, especially in older patients ([PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)).
6. **Sparse global/LMIC data**, particularly outside North America/Europe ([PMID: 41247425](https://pubmed.ncbi.nlm.nih.gov/41247425/)).

---

## Proposed Follow-up Experiments / Actions

1. **Prospective biomarker-stratified immunotherapy trials** integrating spatial/single-cell profiling to select interferon-competent, myeloid-defined subgroups ([PMID: 41892350](https://pubmed.ncbi.nlm.nih.gov/41892350/)).
2. **Target the hypoxia–tryptophan–kynurenine axis** in rational combinations (IDO1/TDO2 + checkpoint + anti-angiogenic), building on the phase I RT+nivolumab+BMS-986205 safety signal ([PMID: 42189896](https://pubmed.ncbi.nlm.nih.gov/42189896/), [PMID: 41893336](https://pubmed.ncbi.nlm.nih.gov/41893336/)).
3. **Validate the 11-gene malignant–myeloid signature (incl. TPST1)** prospectively as a prognostic/predictive tool and evaluate TPST1 as a therapeutic target ([PMID: 41838327](https://pubmed.ncbi.nlm.nih.gov/41838327/)).
4. **EGFR-guided adjuvant acceleration:** test whether expediting chemoradiation in EGFR-altered (REP-prone) tumors improves outcomes ([PMID: 41212363](https://pubmed.ncbi.nlm.nih.gov/41212363/)).
5. **MGMT-stratified surgical/RT algorithms** at diagnosis and recurrence in prospective cohorts ([PMID: 41680847](https://pubmed.ncbi.nlm.nih.gov/41680847/), [PMID: 42397615](https://pubmed.ncbi.nlm.nih.gov/42397615/)).
6. **Improve molecular-GBM recognition** through radiomic/imaging criteria and universal molecular testing regardless of age ([PMID: 41619575](https://pubmed.ncbi.nlm.nih.gov/41619575/), [PMID: 42240773](https://pubmed.ncbi.nlm.nih.gov/42240773/)).

---

## Confirmed Findings and Hypotheses (from investigation)

**Findings**
- **F001:** GBM IDH-wildtype is defined molecularly by TERT/EGFR/+7-10 and converges on RTK/PI3K, p53, and RB core pathways (EGFR & CDKN2A/B in 100%; PTEN loss and TERT promoter mutation as early founders) — [PMID: 42159911](https://pubmed.ncbi.nlm.nih.gov/42159911/), [PMID: 28201779](https://pubmed.ncbi.nlm.nih.gov/28201779/).
- **F002:** Standard therapy yields ~14.6-month median survival; MGMT methylation (21.7 mo) and TTFields (OS/PFS HR 0.68) improve outcomes — [PMID: 41007699](https://pubmed.ncbi.nlm.nih.gov/41007699/), [PMID: 41741710](https://pubmed.ncbi.nlm.nih.gov/41741710/).

**Hypotheses**
- **H001 [supported]:** GBM IDH-wildtype defined by core molecular alterations converging on RTK/PI3K, p53, RB pathways.
- **H002 [supported]:** MGMT promoter methylation is a predictive/prognostic biomarker; methylated tumors benefit more from temozolomide.
- **H003 [supported]:** Adding TTFields to maintenance temozolomide improves OS and PFS.

*Ontology quick-reference:* MONDO:0018177 • MeSH D005909 • ICD-O 9440/3 • ICD-11 2A00.00 • UBERON:0000955 (brain) • CL:0000127 (astrocyte), CL:0000878 (microglia) • GO:0001525 (angiogenesis), GO:0007049 (cell cycle) • CHEBI temozolomide, kynurenine • NCIT C62554 (temozolomide), C118835 (TTFields).


## Artifacts

- [OpenScientist final report](Glioblastoma_IDH_Wildtype-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Glioblastoma_IDH_Wildtype-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.
