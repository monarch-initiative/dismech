---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-20T07:18:37.261008'
end_time: '2026-08-20T07:46:45.615889'
duration_seconds: 1688.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spondyloepimetaphyseal Dysplasia Faden-Alkuraya Type
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
citation_count: 10
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 14
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:33989636
  needs_review: true
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spondyloepimetaphyseal_Dysplasia_Faden-Alkuraya_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spondyloepimetaphyseal_Dysplasia_Faden-Alkuraya_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spondyloepimetaphyseal Dysplasia Faden-Alkuraya Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spondyloepimetaphyseal Dysplasia Faden-Alkuraya Type** covering all of the
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

# Spondyloepimetaphyseal Dysplasia, Faden-Alkuraya Type (SEMDFA): A Comprehensive Disease Characteristics Report

**Disease:** Spondyloepimetaphyseal Dysplasia, Faden-Alkuraya Type (SEMDFA)
**MONDO ID:** MONDO:0014748 | **OMIM:** #616723 | **Orphanet:** ORPHA:457395
**Causal Gene:** *RSPRY1* (Ring Finger and SPRY Domain Containing 1), 16q13
**Category:** Mendelian (autosomal recessive)

---

## Summary

Spondyloepimetaphyseal dysplasia, Faden-Alkuraya type (SEMDFA) is an ultra-rare, autosomal-recessive skeletal dysplasia first delineated in 2015 and caused by biallelic loss-of-function variants in *RSPRY1*, a gene on chromosome 16q13 encoding a 576-amino-acid secreted protein that contains an N-terminal RING (Really Interesting New Gene) domain and a C-terminal B30.2/SPRY (PRY-SPRY) domain. The disease is defined clinically by a recognizable constellation of **progressive spondyloepimetaphyseal dysplasia, disproportionate short stature, facial dysmorphism, short (fourth) metatarsals and cono-brachydactyly, craniosynostosis, and variable intellectual disability**. Consanguinity is the principal risk factor, and all reported families to date derive from consanguineous or founder backgrounds (Saudi Arabian, Turkish, Peruvian, Indian).

Mechanistically, the most important recent advance is the demonstration that RSPRY1 deficiency causes **constitutive, SMAD3-dependent activation of TGF-β signaling** with dysregulated extracellular-matrix (ECM) dynamics. Transcriptomic profiling of patient fibroblasts showed significant enrichment of TGF-β and ECM pathways; RSPRY1-knockout fibroblasts exhibited enhanced motility that was abolished by concurrent *SMAD3* knockout, and RSPRY1-deficient cells responded poorly to exogenous TGF-β — the signature of a pathway already maximally (constitutively) activated. This places SEMDFA within the broader family of TGF-β–dysregulated skeletal dysplasias and nominates TGF-β/SMAD3 inhibition as a rational, though still entirely experimental, therapeutic hypothesis.

*RSPRY1* is one of the more constrained genes in the human genome (gnomAD pLI ≈ 1.0; LOEUF 0.45; missense Z = 4.05), consistent with strong purifying selection against both loss-of-function and missense variation, and with the severe developmental phenotype produced by complete loss of function. The variant spectrum spans frameshift, nonsense, canonical splice-site, and missense alleles, plus large 16q contiguous-gene deletions that encompass *RSPRY1* and produce overlapping skeletal features. There is currently no disease-specific therapy; management is supportive (orthopedic correction of coxa vara/genu valgum, developmental support, monitoring for craniosynostosis) and prevention relies on genetic counseling with carrier and prenatal/preimplantation testing in at-risk families.

---

## Key Findings

### Finding 1 — SEMDFA is an autosomal-recessive dysplasia caused by biallelic loss-of-function *RSPRY1* variants

SEMDFA was established as a distinct, recognizable Mendelian entity by Faden and colleagues in 2015 using combined autozygome/exome analysis. In a consanguineous Saudi family with four affected siblings, they identified a **homozygous frameshift mutation in *RSPRY1* resulting in nonsense-mediated mRNA decay (NMD)** — i.e., a true null allele — and confirmed the locus in an independent simplex Peruvian case carrying a homozygous missense variant. The original report noted: *"Combined autozygome/exome analysis identified a homozygous frameshift mutation in RSPRY1 with resulting nonsense-mediated decay"* ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

The recessive loss-of-function mechanism has been reproduced across multiple independent families and variant classes:

| Study | Family origin | Variant(s) | Type | Patients |
|-------|--------------|-----------|------|----------|
| Faden et al. 2015 ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)) | Saudi (consanguineous) | Homozygous frameshift → NMD | Frameshift/null | 4 siblings |
| Faden et al. 2015 | Peruvian (simplex) | Homozygous missense | Missense | 1 |
| Simsek-Kiper et al. 2018 ([PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)) | Two families | c.377delT p.Ile126fs\*; c.516+2T>A (splice) | Frameshift; splice | 5 |
| Singh et al. 2024 ([PMID: 38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/)) | Two sisters | c.1652G>A p.(Cys551Tyr) | Missense | 2 |

Simsek-Kiper et al. reported: *"Whole exome sequencing revealed a novel homozygous [c.377delT] [p.Ile126fs\*] frameshift mutation at exon 2 in one family, while Sanger sequencing revealed a novel homozygous splice site mutation [c.516+2T>A] at exon 4/intron 4 border of RSPRY1 in the other family"* ([PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)). The convergence of frameshift, nonsense, splice, and missense variants — all homozygous, all in consanguineous or founder settings — firmly supports a **loss-of-function, autosomal-recessive** disease model. OMIM assigns the disease number **#616723**; *RSPRY1* (HGNC:29420; NCBI Gene 89970) maps to chromosome **16q13**.

### Finding 2 — Core clinical phenotype: progressive spondyloepimetaphyseal dysplasia with short stature, facial dysmorphism, cono-brachydactyly, and intellectual disability

The phenotype is remarkably consistent across all reported cohorts. The original description defined the syndrome as *"comprising progressive spondyloepimetaphyseal dysplasia, short stature, facial dysmorphism, short fourth metatarsals, and intellectual disability"* ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

Simsek-Kiper et al. (n = 5) provided the most detailed radiographic delineation, defining the skeletal hallmarks as: *"(a) mild spondylar dysplasia, (b) epimetaphyseal dysplasia of the long bones associated with coxa vara and genu valgum, (c) brachymesophalangy with cone-shaped epiphyses, and (d) craniosynostosis"* ([PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)). They additionally documented pes planus, prominent heels, pectus deformity, and — notably — a cemento-ossifying fibrous lesion of the maxilla in one patient.

Singh et al. (2024) further expanded the spectrum, reporting **joint dislocation as a novel clinical feature**: *"We observed joint dislocation as a novel clinical feature of this condition"* ([PMID: 38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/)), alongside vertebral defects, small epiphyses, and metaphyseal cupping/fraying.

**Suggested HPO-annotated phenotype profile:**

| Phenotype | HPO term | Onset / character | Frequency |
|-----------|----------|-------------------|-----------|
| Progressive spondyloepimetaphyseal dysplasia | HP:0002762 (SEMD spectrum) | Congenital→childhood, progressive | Universal |
| Short stature (often disproportionate) | HP:0004322 | Childhood, progressive | Universal |
| Facial dysmorphism | HP:0001999 | Congenital | Universal |
| Intellectual disability (variable) | HP:0001249 | Childhood | Most (variable) |
| Short (fourth) metatarsals | HP:0004689 | Childhood | Common |
| Brachydactyly / brachymesophalangy | HP:0001156 / HP:0005831 | Childhood | Common |
| Cone-shaped epiphyses | HP:0010579 | Childhood | Common |
| Craniosynostosis | HP:0001363 | Congenital/early | Reported cohort |
| Coxa vara | HP:0002812 | Progressive | Common |
| Genu valgum | HP:0002857 | Childhood | Common |
| Mild spondylar/vertebral dysplasia | HP:0000925 | Progressive | Common |
| Metaphyseal cupping/fraying | HP:0003023 / HP:0003021 | Childhood | Reported (Singh 2024) |
| Pectus / pes planus | HP:0000766 / HP:0001763 | Childhood | Reported |
| Joint dislocation | HP:0001373 | Childhood | Novel (Singh 2024) |

Severity is best characterized as **moderate-to-severe and progressive** for the skeletal component, with **variable** intellectual disability. Cumulative published patients number ~11 across 5 families, so robust per-phenotype frequency percentages are not available; the features above are qualitatively consistent ("core") versus variable/expanding.

### Finding 3 — RSPRY1 deficiency dysregulates TGF-β/SMAD3 signaling and ECM dynamics (the molecular mechanism)

The pivotal mechanistic study is Imren et al. 2025 (*Int J Mol Sci*), which performed transcriptomic analysis of fibroblasts from patients with homozygous *RSPRY1* mutations. They reported: *"Transcriptome analysis of fibroblasts from patients with homozygous RSPRY1 mutations showed there was significant enrichment of transforming growth factor beta (TGF-β) signaling and ECM-related pathways"* ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)).

Two functional experiments establish the causal, SMAD3-dependent nature of the mechanism:

1. **Epistasis / motility rescue:** *"RSPRY1 knockout fibroblasts exhibited enhanced motility, a phenotype that was abrogated in RSPRY1 + SMAD3 double knockout fibroblasts, highlighting the SMAD3-dependence of RSPRY1's effects"* ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)). The rescue of the cellular phenotype by removing SMAD3 places SMAD3 genetically downstream of RSPRY1 loss.

2. **Constitutive activation:** *"The observed limited response to exogenous TGF-β in RSPRY1-deficient cells indicated that there was constitutive pathway activation"* ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)). A blunted response to added ligand is the hallmark of a pathway already operating near its ceiling.

Together these define the disease as one of **de-repressed / constitutive TGF-β–SMAD3 signaling**, consistent with the well-established role of TGF-β superfamily signaling in chondrocyte proliferation/differentiation and endochondral ossification, and consistent with the observed epimetaphyseal (growth-plate) pathology.

**Suggested GO / pathway terms:** GO:0007179 (transforming growth factor beta receptor signaling pathway); GO:0060395 (SMAD protein signal transduction); GO:0030198 (extracellular matrix organization); GO:0001958 (endochondral ossification); GO:0002062 (chondrocyte differentiation); Reactome R-HSA-170834 (Signaling by TGF-β Receptor Complex).

### Finding 4 — Genomic context (16q12.2–q21), contiguous-gene deletions, and skeletal-muscle expression

*RSPRY1* lies within the 16q12.2–q21 region. Yamamoto et al. (2016) described a patient with a 16q12.2q21 interstitial deletion encompassing *RSPRY1* who presented with developmental delay, epilepsy, short stature, and distinctive features, and proposed: *"Because RSPRY1 was been discovered as the cause of progressive skeletal dysplasia, a loss of this gene might explain the skeletal defects observed in the patient"* ([PMID: 27230627](https://pubmed.ncbi.nlm.nih.gov/27230627/)). This supports a contribution of *RSPRY1* to the skeletal component of larger copy-number syndromes, while the full recessive disease requires biallelic loss.

At the expression level, Waddell et al. (2016) showed that *Rspry1* is expressed in skeletal muscle and is transcriptionally regulated during muscle wasting: *"Nip30 and Rspry1 were transcriptionally induced in response to neurogenic muscle wasting in mice and were also found to be expressed endogenously at the RNA and protein level in C2C12 mouse muscle cells"* ([PMID: 26497270](https://pubmed.ncbi.nlm.nih.gov/26497270/)). These two genes share a regulatory region with a conserved MyoD1-bound E-box enhancer.

The tissue relevance to bone is anchored by the original report's immunolocalization data: *"we detect strong RSPRY1 protein localization in murine embryonic osteoblasts and periosteal cells during primary endochondral ossification, consistent with a role in bone development"* ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

Finally, Jacob et al. (2025), a cohort of 248 Indians with skeletal dysplasia (73.6% diagnostic yield; 60% autosomal recessive; 35% consanguinity), expanded the genotype/phenotype spectrum, listing *RSPRY1* among rarely reported conditions confirmed in their cohort: *"We expand the phenotypic and genotypic spectrum of rarely reported conditions (RAB33B, TRIP11, NEPRO, RPL13, COL27A1, PTHR1, EXOC6B, PRKACA, FUZ and RSPRY1)"* ([PMID: 39706863](https://pubmed.ncbi.nlm.nih.gov/39706863/)).

### Finding 5 — Authoritative identifiers and RSPRY1 protein annotation

Cross-referenced ontology identifiers: **MONDO:0014748** ("progressive spondyloepimetaphyseal dysplasia-short stature-short fourth metatarsals-intellectual disability syndrome"); **OMIM #616723**; **Orphanet ORPHA:457395**; **GARD 0017808**; **UMLS C5568882**; **MedGen 1800305**. Common synonyms: SEMDFA; "spondyloepimetaphyseal dysplasia, Faden-Alkuraya type"; "RSPRY1-associated SEMD with cono-brachydactyly and craniosynostosis."

The RSPRY1 protein corresponds to **UniProt Q96DX4 (RSPRY_HUMAN)**, is **576 amino acids** long, is annotated with a **Secreted** subcellular localization, and contains a **B30.2/SPRY domain (≈ residues 300–483)** and an **N-terminal RING domain**. The original report described it as *"a hypothetical RING and SPRY domain-containing protein of unknown physiological function"* ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)). The RING + PRY/SPRY architecture is shared with the TRIM (tripartite-motif) family of E3 ubiquitin ligases and substrate-recognition proteins, in which PRY-SPRY is the domain "most frequently used for substrate recognition" ([PMID: 33092958](https://pubmed.ncbi.nlm.nih.gov/33092958/)) — a plausible structural basis for RSPRY1 acting as a ubiquitin-ligase/adaptor that normally restrains TGF-β signaling.

### Finding 6 — Expanded pathogenic variant spectrum from ClinVar

ClinVar (reference transcript NM_133368.3) contains ~244 *RSPRY1* variant records, of which ~31 are classified pathogenic/likely pathogenic. Beyond the published case-report alleles, curated pathogenic/likely-pathogenic small variants include:

| Variant (cDNA) | Protein | Class | Classification |
|----------------|---------|-------|----------------|
| c.109del | p.Ala37fs | Frameshift | Pathogenic |
| c.358G>T | p.Glu120Ter | Nonsense | Pathogenic |
| c.1422T>A | p.Cys474Ter | Nonsense | Pathogenic |
| c.1279dup | p.Thr427fs | Frameshift | Pathogenic |
| c.121G>T | p.Gly41Cys | Missense | Pathogenic/LP |
| c.901+3_901+15del / c.901_901+15del | — | Splice-region | Conflicting/uncertain |
| c.1652G>A | p.(Cys551Tyr) | Missense | Pathogenic (Singh 2024) |

The published missense allele was confirmed clinically: *"harbored a homozygous missense variant c.1652G>A;p.(Cys551Tyr) in the RSPRY1 gene"* ([PMID: 38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/)). Many additional pathogenic ClinVar entries are large 16q contiguous-gene copy-number gains/losses (e.g., 16q13-21 deletions) spanning *RSPRY1*. Nearly all point variants are **germline** and homozygous; no somatic disease association is reported.

### Finding 7 — *RSPRY1* is highly constrained in the general population

gnomAD constraint metrics (GRCh38; Ensembl ENSG00000159579) indicate strong purifying selection:

| Metric | Value | Interpretation |
|--------|-------|----------------|
| pLI | 0.9995 | Extremely LoF-intolerant |
| Observed/expected LoF (o/e) | 0.315 (90% CI 0.226–0.446) | ~68% depletion of LoF |
| LOEUF | 0.446 | High constraint |
| LoF Z | 4.97 | Strong LoF depletion |
| Missense Z | 4.05 | Significant missense depletion |
| Synonymous Z | 0.95 | Neutral (as expected) |

The strong depletion of both LoF and missense variation is consistent with a gene whose complete biallelic loss produces a severe developmental disorder, supports the pathogenicity of the reported missense alleles, and explains the near-absence of biallelic LoF in the general population. Heterozygous carriers are clinically unaffected (recessive disease); the constraint reflects gene essentiality/selection at the population level.

---

## Mechanistic Model / Interpretation

The findings assemble into a coherent causal chain from genotype to skeletal phenotype:

```
  Biallelic LoF in RSPRY1 (frameshift / nonsense / splice / missense; or 16q CNV)
                │
                ▼
  Loss of functional RSPRY1 protein (RING + B30.2/SPRY; annotated Secreted;
  expressed in embryonic osteoblasts, periosteal cells, growth-plate region)
                │
                ▼
  De-repression of TGF-β signaling  ──►  Constitutive, SMAD3-dependent
  pathway activation (blunted response to exogenous TGF-β)
                │
                ▼
  Dysregulated ECM organization + enhanced fibroblast motility
  (rescued by SMAD3 knockout → SMAD3 is downstream effector)
                │
                ▼
  Disturbed endochondral ossification & growth-plate biology
                │
                ▼
  Spondylo- (vertebral) + epi- + metaphyseal dysplasia, coxa vara/genu valgum,
  cono-brachydactyly, short metatarsals, craniosynostosis, short stature
  (+ variable intellectual disability, joint dislocation)
```

**Upstream vs downstream:** The upstream trigger is loss of RSPRY1 function. The proximate downstream event is constitutive TGF-β/SMAD3 activation; SMAD3 sits genetically downstream (its removal rescues the RSPRY1-null cellular phenotype). ECM dysregulation and abnormal cell motility are further downstream cellular readouts, and disturbed endochondral ossification is the tissue-level consequence that yields the clinical skeletal dysplasia.

**Cell types and structures involved:** osteoblasts (CL:0000062), chondrocytes (CL:0000138), preosteoblasts (CL:0007010), periosteal/perichondrial cells, and fibroblasts (CL:0000057) — the last being the experimental system in which the mechanism was established. Anatomically the disease targets the **growth plate / metaphysis and epiphysis of long bones (UBERON:0006588 epiphyseal plate; UBERON:0004421 metaphysis; UBERON:0006755 epiphysis), the vertebral column (UBERON:0001130), the cranial sutures (UBERON:0007842) via craniosynostosis, and the hands/feet** (short metatarsals, brachydactyly). Subcellular compartments implicated include the extracellular/secreted space (GO:0005576; GO:0031012 extracellular matrix) and, given the RING/SPRY architecture, potentially the ubiquitin–proteasome machinery (GO:0004842 ubiquitin-protein transferase activity) — the latter unconfirmed for RSPRY1.

**Why the RING/SPRY architecture matters:** RSPRY1 shares its domain layout with TRIM-family E3 ubiquitin ligases, in which the PRY-SPRY (B30.2) domain is the principal substrate-recognition module ([PMID: 33092958](https://pubmed.ncbi.nlm.nih.gov/33092958/)). A parsimonious hypothesis — not yet directly demonstrated for RSPRY1 — is that RSPRY1 normally ubiquitinates or otherwise restrains a component of the TGF-β/SMAD3 cascade; its loss removes that brake, producing constitutive signaling. Note that the UniProt "Secreted" annotation sits in apparent tension with a classic intracellular E3-ligase role; resolving this is a key open question.

---

## Section-by-Section Disease Characteristics

### 1. Disease Information
SEMDFA is an ultra-rare autosomal-recessive skeletal dysplasia characterized by progressive spondyloepimetaphyseal dysplasia, short stature, facial dysmorphism, cono-brachydactyly/short metatarsals, craniosynostosis, and variable intellectual disability. It was first delineated in 2015 in a consanguineous Saudi family and named after the lead investigators Faden and Alkuraya. Identifiers: MONDO:0014748; OMIM #616723; ORPHA:457395; GARD 0017808; UMLS C5568882; MedGen 1800305. ICD-10 maps only to the non-specific Q77.8 (osteochondrodysplasia); no specific MeSH term exists (indexed under "Osteochondrodysplasias"). Synonyms: SEMDFA; spondyloepimetaphyseal dysplasia, Faden-Alkuraya type; "RSPRY1-associated SEMD with cono-brachydactyly and craniosynostosis." Information is derived from **individual patient case reports** (~11 patients aggregated from 5 families), not from population-level EHR or registry resources.

### 2. Etiology
**Primary cause:** biallelic loss-of-function variants in *RSPRY1* (purely genetic; Mendelian recessive). **Genetic risk factors:** homozygous/compound-heterozygous LoF *RSPRY1* alleles; the gene is highly constrained (pLI ≈ 1.0). **Environmental risk factors:** none identified; the dominant non-genetic contributor to risk is **consanguinity** (family structure), which increases homozygosity for founder alleles. **Protective factors / gene-environment interactions:** none established; not applicable to a fully penetrant recessive Mendelian disorder.

### 3. Phenotypes
See Finding 2 table for the full HPO-annotated phenotype list, onset, and severity. Phenotype types span physical/skeletal manifestations (dysplasia, brachydactyly, coxa vara, genu valgum, craniosynostosis), clinical signs (short stature, dysmorphism, joint dislocation), and neurodevelopmental features (intellectual disability). Onset is congenital-to-childhood with a **progressive** skeletal course. Quality-of-life impact is driven by short stature, orthopedic deformity/mobility limitation, and developmental/cognitive impairment; formal QoL instrument data (EQ-5D, SF-36, PROMIS) are not available for this ultra-rare disease.

### 4. Genetic/Molecular Information
**Causal gene:** *RSPRY1* (HGNC:29420; NCBI Gene 89970; Ensembl ENSG00000159579; 16q13; reference transcript NM_133368.3). **Variant classes:** frameshift, nonsense, canonical splice-site, missense, and large 16q CNVs (Findings 1, 4, 6). **Functional consequence:** loss of function (NMD for truncating alleles; splice disruption; SPRY-domain missense likely disrupts substrate binding/folding). **Population frequency:** pathogenic alleles are extremely rare/private to consanguineous families; the gene is strongly depleted of LoF/missense variation in gnomAD (Finding 7). **Origin:** germline, biallelic. **Modifier genes / epigenetics:** none established; no methylation/histone data. **Chromosomal abnormalities:** contiguous-gene 16q12.2–q21 deletions represent the main structural abnormality involving the locus (Finding 4).

### 5. Environmental Information
Not applicable as a cause. No toxic, infectious, lifestyle, or occupational agents are implicated. Consanguinity is a population/social risk factor for homozygosity, not an environmental disease cause.

### 6. Mechanism / Pathophysiology
Constitutive, SMAD3-dependent TGF-β pathway activation with ECM dysregulation, downstream of RSPRY1 loss, disturbing endochondral ossification (Finding 3; Mechanistic Model above). Molecular profiling to date is transcriptomic (patient fibroblasts, bulk RNA-seq) plus functional CRISPR-knockout fibroblast models. Proteomic, metabolomic, single-cell, and spatial data are not yet available. No enzyme deficiency, immune dysregulation, or metabolic derangement is reported. Tissue damage is developmental (abnormal growth-plate/epimetaphyseal ossification) rather than degenerative or inflammatory. Suggested terms: GO:0007179, GO:0060395, GO:0030198, GO:0001958; Reactome R-HSA-170834.

### 7. Anatomical Structures Affected
**Organ/system:** skeletal system (primary) — vertebrae, long-bone epiphyses/metaphyses, cranium (sutures), hands/feet; nervous system (intellectual disability); connective tissue/ECM; joints (dislocation). **Cells:** osteoblasts (CL:0000062), chondrocytes (CL:0000138), fibroblasts (CL:0000057), periosteal cells. **UBERON:** epiphyseal plate (UBERON:0006588), metaphysis (UBERON:0004421), epiphysis (UBERON:0006755), vertebral column (UBERON:0001130), cranial suture (UBERON:0007842). **Subcellular:** extracellular space/ECM (GO:0005576, GO:0031012), consistent with the secreted annotation. **Lateralization:** generalized, bilateral, symmetric.

### 8. Temporal Development
Congenital-to-early-childhood onset; **chronic, insidious** pattern. The skeletal disease is explicitly **progressive** (spondylar changes, coxa vara, deformities worsen during growth), whereas neurocognitive impairment is static/developmental. Lifelong disorder; no spontaneous remission; no genetic anticipation (recessive, non-repeat-expansion). The critical window for orthopedic intervention corresponds to growth-plate–active childhood/adolescence.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive — *"a clinically recognizable autosomal-recessive disorder in four affected siblings from a consanguineous Saudi family"* ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)). **Penetrance:** effectively complete for biallelic LoF. **Expressivity:** variable (intellectual-disability degree; head circumference — microcephaly in the original family vs normocephaly in the 2018 cohort; craniosynostosis). **Epidemiology:** ultra-rare; prevalence/incidence unknown (~11 published patients; Orphanet <1/1,000,000). **Founder/consanguinity:** central — all families consanguineous; homozygosity via autozygosity; reported in Saudi, Turkish, Peruvian, and Indian families. **Carrier frequency:** unknown, expected very low. **Sex ratio:** no sex bias (autosomal recessive). **Recurrence risk:** 25% per pregnancy for two carrier parents.

### 10. Diagnostics
Diagnosis rests on a **characteristic skeletal survey** (mild spondylar dysplasia; epimetaphyseal dysplasia with coxa vara/genu valgum; cone-shaped epiphyses/brachymesophalangy; metaphyseal cupping/fraying; short metatarsals; craniosynostosis) combined with **molecular confirmation of biallelic *RSPRY1* variants**. Genetic testing: **whole-exome sequencing** was the diagnostic modality in all discovery reports; WGS and skeletal-dysplasia gene panels including *RSPRY1* are alternatives; single-gene Sanger sequencing confirms/segregates. Autozygosity mapping is powerful in consanguineous families; GeneMatcher-style matchmaking was pivotal — *"Using a gene-centric 'matchmaking' system, we were able to identify a Peruvian simplex case subject"* ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)). **Chromosomal microarray** detects large 16q contiguous-gene deletions that sequencing panels may miss ([PMID: 27230627](https://pubmed.ncbi.nlm.nih.gov/27230627/)). Karyotype/FISH/mtDNA/repeat-expansion testing are not relevant. No specific biochemical biomarker or newborn-screening test exists. Differential diagnoses include other spondyloepimetaphyseal/spondylometaphyseal dysplasias, Dyggve-Melchior-Clausen dysplasia, and cone-shaped-epiphysis syndromes; *RSPRY1* genotyping is discriminating.

### 11. Outcome / Prognosis
No reports indicate reduced life expectancy; the disorder is a **chronic, non-lethal skeletal dysplasia** compatible with survival to adulthood. Morbidity is dominated by short stature, progressive orthopedic deformity (coxa vara, genu valgum, joint dislocation) and mobility limitation, plus variable cognitive disability; craniosynostosis may require neurosurgical attention. Skeletal changes are structural and not reversible. Prognostic factors are inferred (deformity severity, degree of intellectual disability); no validated prognostic biomarkers exist.

### 12. Treatment
There is **no disease-specific or disease-modifying therapy**. Management is **supportive and multidisciplinary**: orthopedic surgical correction of coxa vara/genu valgum and joint dislocations (NCIT: orthopedic surgical procedure), craniosynostosis repair where indicated, physical/occupational therapy and rehabilitation, and developmental/educational support for intellectual disability. Mechanistically, the constitutive SMAD3-dependent TGF-β activation nominates **TGF-β/SMAD3 pathway inhibition as a candidate therapeutic hypothesis** ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)) — entirely experimental (candidate agents such as ALK5/SMAD3 inhibitors or losartan-type TGF-β modulation used in other connective-tissue disorders), with no preclinical or clinical validation in SEMDFA and no registered trials. No pharmacogenomic considerations are established.

### 13. Prevention
Primary prevention is via **genetic counseling** in consanguineous/at-risk families, **carrier testing**, and reproductive options including **prenatal diagnosis and preimplantation genetic testing (PGT-M)** once the familial *RSPRY1* variant is known. Cascade testing identifies at-risk relatives. Secondary/tertiary prevention focuses on early orthopedic and developmental intervention to limit complications. No population-based screening, immunization, or environmental interventions apply.

### 14. Other Species / Natural Disease
No naturally occurring SEMDFA-equivalent disease is documented in companion animals or wildlife (no OMIA entry identified). Orthologous genes exist across vertebrates (mouse *Rspry1*; NCBI Taxon *Homo sapiens* 9606, *Mus musculus* 10090); the gene is expressed in mouse skeletal muscle and C2C12 cells ([PMID: 26497270](https://pubmed.ncbi.nlm.nih.gov/26497270/)), and murine embryonic bone was used to localize the protein ([PMID: 26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)). No zoonotic or cross-species transmission relevance (Mendelian, non-infectious).

### 15. Model Organisms
No dedicated in vivo *Rspry1* knockout disease model has been reported. Available systems are **cellular/in vitro**: patient-derived dermal fibroblasts with homozygous *RSPRY1* mutations and engineered **RSPRY1-knockout (± SMAD3 double-knockout) fibroblasts** used to establish the TGF-β/SMAD3 mechanism ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)), plus mouse **C2C12 muscle cells** for expression studies ([PMID: 26497270](https://pubmed.ncbi.nlm.nih.gov/26497270/)). Recommended future models: an *Rspry1* knockout/knock-in mouse (IMPC/KOMP), zebrafish *rspry1* CRISPR knockdown for skeletal phenotyping, and patient-derived iPSC → osteoblast/chondrocyte or organoid systems. Phenotype recapitulation is **unknown** — a major research gap.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution | Evidence type |
|------|-----------------|--------------|---------------|
| [26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/) | *Identification of a Recognizable Progressive Skeletal Dysplasia Caused by RSPRY1 Mutations* | Founding report: gene discovery, NMD LoF mechanism, core phenotype, osteoblast localization | Human clinical + in vitro |
| [30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/) | *Further delineation of SEMDFA…* | Radiographic hallmarks; new frameshift + splice alleles; craniosynostosis/cono-brachydactyly | Human clinical |
| [38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/) | *Two sisters with RSPRY1-related SEMD* | Homozygous missense c.1652G>A p.(Cys551Tyr); novel joint dislocation | Human clinical |
| [39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/) | *Unraveling the Role of RSPRY1 in TGF-β Pathway Dysregulation* | Core mechanism: constitutive SMAD3-dependent TGF-β activation; ECM dysregulation | In vitro / patient cells |
| [27230627](https://pubmed.ncbi.nlm.nih.gov/27230627/) | *A 16q12.2q21 deletion…* | Contiguous-gene deletion including *RSPRY1* explains skeletal defects | Human clinical |
| [26497270](https://pubmed.ncbi.nlm.nih.gov/26497270/) | *NIP30 and RSPRY1 in skeletal muscle* | *Rspry1* muscle expression/regulation; MyoD1 E-box enhancer | Model organism / in vitro |
| [39706863](https://pubmed.ncbi.nlm.nih.gov/39706863/) | *Genetic and allelic heterogeneity in 248 Indians with skeletal dysplasia* | Expands *RSPRY1* genotype/phenotype spectrum in a large cohort | Human clinical |
| [33092958](https://pubmed.ncbi.nlm.nih.gov/33092958/) | *Substrate recognition by TRIM/TRIM-like proteins* | Contextualizes PRY-SPRY as a substrate-recognition module (structural analogy) | Review |

Supporting TRIM/SPRY-family literature ([PMID: 36675197](https://pubmed.ncbi.nlm.nih.gov/36675197/), [33989636](https://pubmed.ncbi.nlm.nih.gov/33989636/), [40593126](https://pubmed.ncbi.nlm.nih.gov/40593126/), [38780244](https://pubmed.ncbi.nlm.nih.gov/38780244/), [37139802](https://pubmed.ncbi.nlm.nih.gov/37139802/)) establishes the general biochemistry of RING + PRY/SPRY proteins as E3 ubiquitin ligases/substrate adaptors, providing an analogy-based (not SEMDFA-specific) framework for RSPRY1 function. An endometriosis Mendelian-randomization study ([PMID: 39978332](https://pubmed.ncbi.nlm.nih.gov/39978332/)) lists *RSPRY1* as a candidate eQTL target in an unrelated disease context and is not directly relevant to SEMDFA pathogenesis.

**Supported hypotheses:** biallelic LoF *RSPRY1* causation; autosomal-recessive inheritance with consanguinity; the progressive SEMD + short stature + facial dysmorphism + intellectual disability ± craniosynostosis phenotype; RSPRY1 action in bone-forming cells during endochondral ossification; constitutive SMAD3-dependent TGF-β/ECM dysregulation as the molecular mechanism.

**Refuted / not supported:** dominant inheritance, environmental/infectious causation, and gain-of-function mechanisms are not supported. Universal microcephaly (suggested by the original family) was refuted by the 2018 cohort, in which most patients were normocephalic ([PMID: 30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)).

---

## Limitations and Knowledge Gaps

1. **Very small evidence base.** ~11 patients across 5 consanguineous families underpin the entire clinical picture; per-phenotype frequencies, prognosis, and natural history are not quantifiable with confidence, and there are no epidemiologic, registry, or QoL data.
2. **Mechanism from a single functional study in fibroblasts.** The TGF-β/SMAD3 model rests primarily on one report using patient fibroblasts and knockout cell lines ([PMID: 39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/)); it has not been validated in chondrocytes/osteoblasts or in vivo, the cell types most relevant to the skeletal phenotype.
3. **Molecular link untested.** The direct biochemical connection between RSPRY1 (RING/SPRY, secreted) and TGF-β/SMAD3 restraint — e.g., a specific ubiquitination substrate — is inferred by analogy to TRIM proteins, not demonstrated for RSPRY1.
4. **Discordant localization annotations.** UniProt annotates RSPRY1 as "Secreted," yet a RING/SPRY E3-ligase function and the intracellular constitutive TGF-β phenotype imply intracellular activity; this apparent discrepancy is unresolved.
5. **No animal model of the disease.** No *Rspry1*-null mouse skeletal phenotype has been reported, limiting causal in-vivo confirmation and preclinical therapy testing.
6. **No therapeutics.** TGF-β inhibition is a hypothesis only; efficacy and safety in SEMDFA are untested and no trials are registered.
7. **Epidemiology absent.** No prevalence/incidence estimates, carrier frequencies, or geographic-variant maps beyond consanguineous founder observations.

---

## Proposed Follow-up Experiments / Actions

1. **Generate an *Rspry1* mouse model** (global and cartilage-specific conditional knockout, e.g., *Col2a1-Cre*) and characterize growth-plate architecture, endochondral ossification, and craniofacial sutures to test skeletal recapitulation.
2. **Validate the TGF-β/SMAD3 mechanism in disease-relevant cells** — patient-derived iPSC chondrocytes/osteoblasts and growth-plate organoids — with phospho-SMAD3 quantification and rescue by SMAD3 knockdown or ALK5 (TGFβR1) inhibitors (e.g., SB-431542, galunisertib).
3. **Define the RSPRY1 interactome and substrate(s).** Use affinity purification–mass spectrometry and ubiquitination assays to test whether the RING/SPRY domain targets a TGF-β pathway component for ubiquitination, bridging the structural annotation (Finding 5) and functional mechanism (Finding 3).
4. **Resolve subcellular localization** with endogenous tagging/immunofluorescence and secretome analysis to reconcile the "secreted" annotation with an intracellular E3-ligase function.
5. **Preclinical therapeutic proof-of-concept:** test TGF-β/SMAD3 pathway inhibitors in the mouse model and in patient chondrocyte organoids for correction of ECM and differentiation defects.
6. **Establish an international patient registry** to collect standardized skeletal, developmental, and pediatric HRQoL outcomes and to define natural history, penetrance, and expressivity.
7. **Systematic variant curation** with functional assays (minigene splicing for splice variants; NMD/expression assays for truncating alleles; overexpression rescue for missense) to reclassify VUS and the conflicting splice-region ClinVar entries.
8. **Carrier-frequency and founder-haplotype studies** in consanguineous populations (Saudi, Turkish, Indian, Peruvian) to inform targeted carrier screening and counseling.

---

*Report compiled from an autonomous multi-iteration literature and database investigation (7 confirmed findings; 15 papers reviewed). Evidence types are distinguished as human clinical, in vitro/patient-cell, model organism, and computational throughout.*


## Artifacts

- [OpenScientist final report](Spondyloepimetaphyseal_Dysplasia_Faden-Alkuraya_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spondyloepimetaphyseal_Dysplasia_Faden-Alkuraya_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:33989636` (1 mention) - Crystal structure and mutational analysis of the human TRIM7 B30.2 domain provide insights into the molecular basis of its binding to glycogenin-1.
  - shared terms: mechanism, protein

Weighed against this report's own most characteristic terms: `rspry1`, `disease`, `skeletal`, `dysplasia`, `gene`, `patient`, `tgf`, `craniosynostosis`, `cell`, `phenotype`, `type`, `progressive`, `consanguineous`, `disability`, `familie`, `variant`, `biallelic`, `developmental`, `mechanism`, `protein`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.