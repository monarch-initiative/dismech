---
title: Atrioventricular septal defect pathophysiology for dismech curation
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-27T12:47:17.739977'
end_time: '2026-08-27T13:11:28.115055'
duration_seconds: 1450.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atrioventricular Septal Defect
  mondo_id: MONDO:0859565
  category: Congenital heart defect / endocardial cushion (atrioventricular canal)
    defect
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 10
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 5400
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 66
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Atrioventricular_Septal_Defect-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Atrioventricular_Septal_Defect-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Atrioventricular Septal Defect
- **MONDO ID:** MONDO:0859565 (if available)
- **Category:** Congenital heart defect / endocardial cushion (atrioventricular canal) defect

## Research Objectives

Please provide a comprehensive research report on **Atrioventricular Septal Defect** covering all of the
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

# Atrioventricular Septal Defect (AVSD): A Comprehensive Disease Characteristics Report

**Disease:** Atrioventricular Septal Defect (AVSD) — also atrioventricular canal defect / endocardial cushion defect
**MONDO ID:** MONDO:0859565
**Category:** Congenital heart defect (endocardial cushion / atrioventricular canal defect)
**Evidence base:** 92 primary papers reviewed; 22 findings recorded; 5 hypotheses (all supported). Information derived from aggregated disease-level resources plus clinical cohorts, model-organism studies, and in vitro/computational work.

---

## Summary

Atrioventricular septal defect (AVSD) is a congenital cardiac malformation defined by a **common atrioventricular (AV) junction** resulting from deficient development of the atrioventricular septum. Anatomically it comprises an ostium primum atrial communication and/or an inlet ventricular septal defect together with an abnormal AV valve — either a single common valve (complete AVSD) or two valve orifices with a cleft left AV valve (partial AVSD). The malformation arises from **failed atrioventricular-canal endocardial cushion development**, specifically defective **endothelial-to-mesenchymal transition (EndoMT)** governed by TGF-β, BMP, Notch and Wnt/β-catenin signaling ([PMID: 29549339](https://pubmed.ncbi.nlm.nih.gov/29549339/)). AVSD represents roughly **4–7% of all congenital cardiac malformations** ([PMID: 37612667](https://pubmed.ncbi.nlm.nih.gov/37612667/)).

AVSD has the tightest link of any congenital heart defect to **trisomy 21 (Down syndrome)**: AVSD is the most common heart defect in Down syndrome (~44%), and roughly half of all AVSD cases occur in the context of Down syndrome ([PMID: 39104126](https://pubmed.ncbi.nlm.nih.gov/39104126/); [PMID: 37667895](https://pubmed.ncbi.nlm.nih.gov/37667895/)). Beyond trisomy 21, the genetic architecture is heterogeneous and often **oligogenic**, involving cardiac transcription factors and developmental signaling genes (CRELD1, GATA4/6, NR2F2, NFATC1, GDF1, NOTCH1, BMPR1A, HEY2) plus rare copy-number variants, converging on the **CRELD1–calcineurin/NFATc1–VEGF axis** ([PMID: 15096951](https://pubmed.ncbi.nlm.nih.gov/15096951/); [PMID: 30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/); [PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/)). On chromosome 21, gene-dosage effects (cooperative DSCAM+COL6A2 overexpression; HMGN1-driven myocardial reprogramming) contribute to the trisomy-21 phenotype ([PMID: 22072978](https://pubmed.ncbi.nlm.nih.gov/22072978/); [PMID: 41125893](https://pubmed.ncbi.nlm.nih.gov/41125893/)). Maternal **pregestational diabetes** is a strong modifiable environmental risk factor (adjusted prevalence ratio ~6.7 for non-syndromic AVSD), while folate-rich diet is protective ([PMID: 23061687](https://pubmed.ncbi.nlm.nih.gov/23061687/); [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/)).

Hemodynamically, the defect produces a large **left-to-right shunt** with common-valve regurgitation, causing infantile congestive heart failure and, if left unrepaired, **irreversible pulmonary vascular obstructive disease (Eisenmenger physiology)** ([PMID: 1943197](https://pubmed.ncbi.nlm.nih.gov/1943197/); [PMID: 10812553](https://pubmed.ncbi.nlm.nih.gov/10812553/)). Diagnosis rests on **echocardiography** (AVSD is the most common fetal cardiac diagnosis, with 90–100% fetal-echo sensitivity and the highest genetic-testing yield of any CHD subtype) ([PMID: 37240614](https://pubmed.ncbi.nlm.nih.gov/37240614/); [PMID: 34196822](https://pubmed.ncbi.nlm.nih.gov/34196822/); [PMID: 33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/)). Treatment is **surgical repair in infancy** (single-patch, modified single-patch, or double-patch), with excellent modern long-term survival (~80–88% at 10–25 years) and **left AV valve regurgitation** as the principal residual problem and reoperation driver ([PMID: 40154545](https://pubmed.ncbi.nlm.nih.gov/40154545/); [PMID: 34002204](https://pubmed.ncbi.nlm.nih.gov/34002204/)).

This report synthesizes 22 confirmed findings from 10 iterations across 92 reviewed papers, organized against the 15-section disease-characteristics template.

---

## 1. Disease Information

AVSD (atrioventricular septal defect) is a structural congenital heart malformation characterized by a **common atrioventricular junction** with deficient atrioventricular septation. The core anatomic lesion is an **ostium primum atrial septal defect** and/or an **inlet ventricular septal defect** with an abnormal **common or cleft atrioventricular valve** ([PMID: 8347012](https://pubmed.ncbi.nlm.nih.gov/8347012/)). Forms range from **partial/incomplete** (primum ASD + cleft left AV valve, two valve orifices) through **transitional** to **complete** (single common AV valve, combined atrial and ventricular communications).

**Key identifiers:**
- **MONDO:** MONDO:0859565
- **Common synonyms/alternative names:** atrioventricular canal defect, common atrioventricular canal (CAVC), endocardial cushion defect, AV canal defect, persistent common atrioventricular canal
- **ICD-10:** Q21.2 (atrioventricular septal defect); **MeSH:** "Heart Septal Defects" / "Endocardial Cushion Defects"
- Additional clinical descriptors: complete AVSD (CAVSD), partial AVSD (pAVSD), transitional AVSD

**Source of information:** This report draws primarily on **aggregated disease-level resources** — surgical/echocardiographic cohorts, population-based birth-defect registries (Texas Birth Defects Registry, National Birth Defects Prevention Study, US National Inpatient Sample), genetic studies, and model-organism experiments — rather than individual EHR records.

---

## 2. Etiology

### Disease Causal Factors

AVSD is a **multifactorial, genetically heterogeneous** malformation. The unifying developmental cause is **failed fusion/development of the atrioventricular-canal endocardial cushions** (see Section 6). Causal contributors span:

- **Chromosomal:** trisomy 21 (the single largest contributor), plus other aneuploidies (trisomy 18, trisomy 13) and specific deletions (e.g., 3p25–pter / 3p- syndrome, in which AVSD occurs in ~one-third of patients; [PMID: 19760623](https://pubmed.ncbi.nlm.nih.gov/19760623/)).
- **Single-gene / oligogenic:** CRELD1, GATA4, GATA6, NR2F2, NKX2-5, TBX5, BMP4, NFATC1, GDF1, NOTCH1, BMPR1A, HEY2 (see Section 4).
- **Environmental:** maternal pregestational and gestational diabetes, maternal obesity, poor periconceptional diet.

CRELD1 was the **first identified non-syndromic AVSD susceptibility gene**; critically, "*Mutation of CRELD1 increases susceptibility to AVSD but is not alone sufficient to cause the defect, indicating that AVSD is multigenic*" ([PMID: 15096951](https://pubmed.ncbi.nlm.nih.gov/15096951/)).

### Risk Factors

**Genetic risk factors** — trisomy 21 (dominant), CRELD1 missense variants (~5–10% of simplex AVSD carry a CRELD1 missense mutation; [PMID: 25328912](https://pubmed.ncbi.nlm.nih.gov/25328912/)), and rare damaging variants across ~112 biologically relevant genes enriched in AVSD probands (OR 1.52, 95% CI 1.35–1.71, P = 4.8×10⁻¹¹; [PMID: 25996639](https://pubmed.ncbi.nlm.nih.gov/25996639/)).

**Environmental risk factors** — maternal **pregestational diabetes** is the strongest (adjusted prevalence ratio [aPR] 6.74, 95% CI 3.67–12.37 for non-syndromic complete AV canal), followed by gestational diabetes (aPR 1.69) and obesity (aPR 1.69) ([PMID: 23061687](https://pubmed.ncbi.nlm.nih.gov/23061687/)). Advanced maternal age (via aneuploidy risk), low maternal education, and poor diet are additional contributors ([PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/)).

### Protective Factors

**Environmental protective factors** — frequent consumption of **folate-rich fruits** was protective for CHD (adjusted OR 0.64, 95% CI 0.47–0.89), and consistent periconceptional folic-acid supplementation trended protective for cardiac-inclusive anomalies (aOR 0.5, 95% CI 0.3–1.0) ([PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/); [PMID: 33179873](https://pubmed.ncbi.nlm.nih.gov/33179873/)). **Genetic protective factors** specific to AVSD are not well established.

### Gene–Environment Interactions

The clearest example is a **genetic-threshold/modifier model**: crossing loss-of-function alleles of *Creld1* or *Hey2* onto the trisomic Ts65Dn background "*caused a significant increase in the frequency of CHD*," demonstrating that additional genetic perturbations push a dosage-sensitized background across a defect threshold ([PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/)). On the environmental side, gestational diabetes and obesity show **additive interaction** for AVSD risk (RERI 1.1, 95% CI −0.1 to 2.3; [PMID: 33876578](https://pubmed.ncbi.nlm.nih.gov/33876578/)).

---

## 3. Phenotypes

| Phenotype | Type | Onset | Frequency / Severity | Suggested HPO |
|---|---|---|---|---|
| Atrioventricular septal defect (structural) | Physical/structural malformation | Congenital | Defining feature | HP:0006695 |
| Congestive heart failure | Clinical sign | Neonatal–infantile (mean ~50 days) | 62% (Down) – 84% (non-Down) complete AVSD | HP:0001635 |
| Pulmonary arterial hypertension | Clinical sign | Infantile, earlier in Down syndrome | 38% (Down) vs 16% (non-Down) | HP:0002092 |
| Common AV valve regurgitation | Physical manifestation | Congenital/infantile | Common; drives symptoms | HP:0031652 / HP:0000023 |
| Tachypnea / respiratory distress | Symptom | Infantile | Common | HP:0002789 |
| Failure to thrive / poor weight gain | Sign | Infantile | Common | HP:0001508 |
| Recurrent respiratory infections | Sign | Infantile | Common | HP:0002205 |
| Arrhythmia (AV block, atrial flutter/fibrillation) | ECG abnormality | Variable; high long-term risk | Among highest of all CHDs | HP:0011675 |
| Superior/leftward ("northwest") QRS axis | ECG abnormality | Congenital | Characteristic | HP:0031547 |

**Phenotype characteristics:** Symptoms typically begin in the first weeks-to-months of life (mean symptom onset ~50 ± 75 days in complete AVSD; [PMID: 9532811](https://pubmed.ncbi.nlm.nih.gov/9532811/)). Severity ranges from mild (partial AVSD, sometimes asymptomatic into adulthood) to severe (complete AVSD with heart failure). Progression is **progressive** if unrepaired, driven by pulmonary overcirculation. A key phenotypic contrast: "*There seems to be a pulmonary vascular hyperreactivity predominance in Down's children and cardiac insufficiency signs in the normal genetic group*" ([PMID: 9532811](https://pubmed.ncbi.nlm.nih.gov/9532811/)) — non-Down patients had more severe AV valve morphologic lesions (38% vs 8%).

**Quality of life impact:** After repair, long-term QoL is favorable — self- or caregiver-reported QoL was "*excellent or good in 81%*" of patients up to 40 years after single-patch complete AVSD repair ([PMID: 34953470](https://pubmed.ncbi.nlm.nih.gov/34953470/)).

---

## 4. Genetic / Molecular Information

### Causal and Susceptibility Genes

| Gene (HGNC) | Role / Evidence | Variant examples | Key PMID |
|---|---|---|---|
| **CRELD1** | First non-syndromic AVSD susceptibility gene; regulates calcineurin/NFATc1; ~5–10% of simplex AVSD | p.A286P, p.E325K, c.973G>A (p.Glu325Lys) in cb-EGF calcium-binding domains | [15096951](https://pubmed.ncbi.nlm.nih.gov/15096951/), [21080147](https://pubmed.ncbi.nlm.nih.gov/21080147/), [29054759](https://pubmed.ncbi.nlm.nih.gov/29054759/), [25328912](https://pubmed.ncbi.nlm.nih.gov/25328912/) |
| **NFATC1** | Heterozygous missense; defective nuclear translocation, reduced transactivation | p.Ala367Val (isolated AVSD); p.Val210Met, p.Ala696Thr (+heterotaxy) | [30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/) |
| **GATA6** | Cardiac transcription factor; variants in complex CHD incl. AVSD | A178V (gain of transactivation), L198V | [20581743](https://pubmed.ncbi.nlm.nih.gov/20581743/) |
| **GATA4, NKX2-5, TBX5, BMP4** | Established CHD candidate genes (MLPA CHD panel) | CNVs / point variants | [29952356](https://pubmed.ncbi.nlm.nih.gov/29952356/) |
| **NIPBL, CHD7, CEP152, BMPR1a, ZFPM2, MDM4** | Exome-enriched for rare variants in AVSD vs controls (3 syndrome-associated) | Rare/rare-damaging | [25996639](https://pubmed.ncbi.nlm.nih.gov/25996639/) |
| **GDF1 + NOTCH1** | Co-occurring variants in oligogenic non-syndromic AV canal + coarctation | — | [38975735](https://pubmed.ncbi.nlm.nih.gov/38975735/) |
| **BMPR1A** | Familial CHD (Ebstein + AVSD) co-segregating with chr1 linkage | p.R443H | [30814609](https://pubmed.ncbi.nlm.nih.gov/30814609/) |
| **DNAH11, MKS1** (cilia genes) | ENU mouse recessive AVSD via L/R axis + Hedgehog/second heart field | — | [27340223](https://pubmed.ncbi.nlm.nih.gov/27340223/) |

The genetic etiology remains **unknown in ~40% of cases** ([PMID: 25996639](https://pubmed.ncbi.nlm.nih.gov/25996639/)). Exome sequencing found significant enrichment of rare variants in AVSD vs tetralogy of Fallot (OR 2.25, P = 2.2×10⁻¹⁶), indicating disease-specific genetic burden. Diagnostic yield of exome sequencing in Southern African CHD was 7.9% ([PMID: 42037320](https://pubmed.ncbi.nlm.nih.gov/42037320/)).

### Variant Classification, Type, Origin, and Consequences

- **Classification (ACMG/AMP):** ranges from pathogenic/likely pathogenic (aneuploidy, syndromic-gene LOF) to VUS (many CRELD1/GATA6 missense variants).
- **Variant type:** missense (CRELD1, NFATC1, GATA6, BMPR1A), plus structural/copy-number variants; aneuploidy (trisomy 21) is the dominant chromosomal class.
- **Origin:** predominantly **germline**; somatic origin is not a feature of AVSD.
- **Functional consequences:** loss of function (NFATC1 — "*defective nuclear translocation and decreased transcriptional transactivation activity*"; [PMID: 30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/)), gain of function (GATA6 A178V increased transactivation), and dosage effects (chr21 genes).

### Modifier Genes and Chromosomal Abnormalities

**Modifiers:** VEGFA interacts allelically with CRELD1 as a modifier of AVSD risk ([PMID: 25328912](https://pubmed.ncbi.nlm.nih.gov/25328912/)); *Creld1* and *Hey2* modify trisomy-21 CHD frequency ([PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/)). **Chromosomal abnormalities:** trisomy 21 predominates. Rare CNV burden in 150 AVSD cases concentrated on **chromosomes 19, 22, 21, and 16** and nominated 20 candidate genes ([PMID: 36816019](https://pubmed.ncbi.nlm.nih.gov/36816019/)). In 262 Chinese complete AV canal cases, potentially-causative CNVs were found in 16.4%, of which 90.7% carried 21q11.2–q22.3 duplication (trisomy 21) ([PMID: 34627233](https://pubmed.ncbi.nlm.nih.gov/34627233/)).

**Epigenetic information:** The chr21 chromatin architectural protein **HMGN1** drives trisomy-21 heart defects via **myocardial transcriptional/chromatin reprogramming** ([PMID: 41125893](https://pubmed.ncbi.nlm.nih.gov/41125893/)).

**Suggested ontology terms:** HGNC CRELD1, GATA4, GATA6, NFATC1, NOTCH1, BMPR1A, HMGN1; CHEBI:calcium (calcium-binding EGF domain).

---

## 5. Environmental Information

**Environmental factors:** Maternal metabolic environment dominates. **Pregestational diabetes** is the strongest single non-genetic factor: "*Significant associations were observed between non-syndromic CAVC in offspring and maternal pregestational diabetes (aPR 6.74; 95% CI 3.67, 12.37), gestational diabetes (aPR 1.69) and obesity (aPR 1.69)*" ([PMID: 23061687](https://pubmed.ncbi.nlm.nih.gov/23061687/)). Pregestational diabetes was strongly associated with most birth defects (OR 2.0–75.9) in the National Birth Defects Prevention Study ([PMID: 33876578](https://pubmed.ncbi.nlm.nih.gov/33876578/)).

**Lifestyle factors:** Poor maternal diet low in fruit/vegetables increased CHD risk (aOR 1.56); maternal smoking (~2-fold) and overweight/obesity (aOR 1.8) were risk factors for cardiac-inclusive anomalies ([PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/); [PMID: 33179873](https://pubmed.ncbi.nlm.nih.gov/33179873/)). Folate-rich diet is protective (see Section 2).

**Infectious agents:** Not applicable — AVSD is a developmental malformation, not an infectious disease.

---

## 6. Mechanism / Pathophysiology

### The Central Developmental Mechanism: Failed Endocardial Cushion EndoMT

The AV septum and valves derive from **endocardial cushions**, formed when endocardial cells of the atrioventricular canal (AVC) undergo **endothelial-to-mesenchymal transition (EndoMT/EMT)**, delaminate, and invade the cardiac jelly (extracellular matrix). "*Atrioventricular septal defects often result from impaired endocardial cushion development. Endothelial-to-mesenchymal transition (EndoMT) is a critical event in endocardial cushion development that initiates in the atrioventricular canal (AVC)*" ([PMID: 29549339](https://pubmed.ncbi.nlm.nih.gov/29549339/)).

**Molecular pathways governing EndoMT:**

- **TGF-β signaling** induces EndoMT; MBNL1 negatively regulates TGF-β/EMT, and *Mbnl1*-null mice show precocious EMT, later valve dysmorphia, and ostium secundum septal defects ([PMID: 26472242](https://pubmed.ncbi.nlm.nih.gov/26472242/)).
- **BMP signaling** — "*Bone morphogenetic protein (BMP) signalling plays a key role in regulating the development of the atrioventricular (AV) septum and valves*"; Sema6D acts downstream of BMP to promote AV cushion development ([PMID: 28172500](https://pubmed.ncbi.nlm.nih.gov/28172500/)).
- **Notch signaling** gates the process — endocardial Mib1–Dll4–Notch1 drives EMT and Jag1–Notch1 restrains post-EMT proliferation; "*Mice lacking endocardial Jag1, Notch1, or RBPJ displayed enlarged valve cusps, bicuspid aortic valve, and septal defects*" ([PMID: 27056911](https://pubmed.ncbi.nlm.nih.gov/27056911/)). Manic Fringe (MFNG) promotes Notch-mediated EndMT; "*Aberrant EndMT is a primary cause of congenital valvular malformations*" ([PMID: 39528804](https://pubmed.ncbi.nlm.nih.gov/39528804/)).
- **Wnt/β-catenin signaling** — "*Disruption of these Wnt/β-catenin signaling roles that enable developmental transitions during valvulogenesis could account for common congenital valve defects*" ([PMID: 26893350](https://pubmed.ncbi.nlm.nih.gov/26893350/)).
- **NADPH oxidase NOX2-derived ROS** is critical to EndoMT and heart development ([PMID: 32655758](https://pubmed.ncbi.nlm.nih.gov/32655758/)).

### The CRELD1 → Calcineurin/NFATc1 → VEGF Axis

A specific convergent module operates in AV canal endocardium: "*Multiple lines of evidence support a role of calcineurin/NFAT signaling in AVSD, and mutations in CRELD1, a protein functioning as a regulator of calcineurin/NFAT signaling have been reported*" ([PMID: 30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/)). Murine work established the causal chain: "*Creld1 function is required for the VEGF-dependent proliferation of endocardial cells by promoting the expression of NFATc1 target-genes*" ([PMID: 24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/)); Creld1 promotes NFATc1 dephosphorylation and nuclear translocation via a complex with the calcineurin regulatory subunit CnB at the endoplasmic reticulum. Human pre-valvular endocardial cells from pluripotent stem cells recapitulate BMP2-responsive AVC EndoMT in vitro ([PMID: 31028265](https://pubmed.ncbi.nlm.nih.gov/31028265/)).

### Trisomy 21 Gene-Dosage Mechanisms

- **Cooperative overexpression:** DSCAM and COL6A2 (both chr21) are "*the most strongly interacting pair of genes*"; co-overexpression in mouse heart caused "*≈50% mortality and severe physiological and morphological defects, including atrial septal defects and cardiac hypertrophy*," whereas single-gene overexpression did not ([PMID: 22072978](https://pubmed.ncbi.nlm.nih.gov/22072978/)).
- **HMGN1-mediated reprogramming:** the chromatin architectural gene HMGN1 drives myocardial transcriptional reprogramming underlying trisomy-21 heart defects ([PMID: 41125893](https://pubmed.ncbi.nlm.nih.gov/41125893/)).

### Hemodynamic Pathophysiology (Downstream Clinical Mechanism)

Once the structural defect exists, a large **left-to-right shunt** develops. "*With increasing shunt ratio the pulmonary perfusion raised (r = 0.84), but the systemic output dropped significantly (r = -0.77)*" ([PMID: 10812553](https://pubmed.ncbi.nlm.nih.gov/10812553/)). Untreated, "*The natural history of patients with complete atrioventricular canal defect is one of unrelenting development of pulmonary vascular obstructive disease*" ([PMID: 1943197](https://pubmed.ncbi.nlm.nih.gov/1943197/)), culminating in Eisenmenger physiology.

### Causal Chain Diagram

```
UPSTREAM (developmental)                          DOWNSTREAM (clinical)
─────────────────────────────────────────────────────────────────────────
Trisomy 21 dosage (DSCAM+COL6A2, HMGN1)
   │
Genetic variants (CRELD1, NFATC1, GATA4/6,        Structural defect
   NOTCH1, BMPR1A, GDF1, HEY2)                     (common AV junction,
   │          +                                    primum ASD ± inlet VSD,
Maternal environment (diabetes, obesity)           common/cleft AV valve)
   │                                                      │
   ▼                                                      ▼
Impaired AVC endocardial cushion EndoMT           Large left-to-right shunt
(TGF-β / BMP / Notch / Wnt / NOX2-ROS;              + AV valve regurgitation
 CRELD1→calcineurin/NFATc1→VEGF)                          │
   │                                                      ▼
   ▼                                              Pulmonary overcirculation →
Failed AV septation & valve formation             CHF (infancy) → pulmonary
                                                   vascular obstructive disease
                                                   → Eisenmenger (if untreated)
```

**GO terms:** GO:0003198 (EMT involved in endocardial cushion formation), GO:0003181 (atrioventricular valve morphogenesis), GO:0060411 (cardiac septum morphogenesis). **CL terms:** CL:0002350 (endocardial cell), CL:0000057 (fibroblast/valve interstitial cell), CL:0000746 (cardiac muscle cell).

---

## 7. Anatomical Structures Affected

**Organ level:** The **heart** is the primary affected organ, specifically the **atrioventricular septum** and **atrioventricular valves**. Secondary organ involvement includes the **lungs/pulmonary vasculature** (pulmonary vascular obstructive disease) and, via heart failure, the liver (hepatomegaly). The **cardiovascular** and **respiratory** systems are principally involved.

**Anatomical detail:** AVSD is defined by a common atrioventricular junction with deficient AV septation. The **Rastelli classification** categorizes the anterior (superior) bridging leaflet of the common valve into types A, B, and C, guiding surgical strategy; interventricular communication under the posterior leaflet is surgically decisive ([PMID: 8347012](https://pubmed.ncbi.nlm.nih.gov/8347012/)). In Down syndrome, characteristic **outlet-septum anterior malalignment** occurs — "*Outlet extension of the ventricular component of the defect with outlet septum anterior malalignment was found in 90.6% of Down vs 12.8% of non-Down patients*" ([PMID: 39892564](https://pubmed.ncbi.nlm.nih.gov/39892564/)) — and Rastelli **type A** morphology is an independent risk factor for pulmonary vascular disease in Down syndrome ([PMID: 10946038](https://pubmed.ncbi.nlm.nih.gov/10946038/)).

**Tissue and cell level:** Affected tissues include the **endocardial cushion mesenchyme**, **AV valve leaflet connective tissue**, and adjacent **myocardium**. Key cell populations: **endocardial (endothelial) cells** undergoing EndoMT and their **mesenchymal/valve interstitial cell** derivatives; cardiomyocytes in trisomy-21 reprogramming.

**Subcellular level:** GO cellular components implicated: **nucleus** (NFATc1 translocation; HMGN1 chromatin), **endoplasmic reticulum** (Creld1–calcineurin complex), and extracellular matrix / **cardiac jelly**.

**Localization:** Central heart — the atrioventricular canal region; the lesion is **midline/central** rather than lateralized. **UBERON terms:** UBERON:0002087 (atrioventricular region), UBERON:0002078/0002079 (right/left cardiac atrium), UBERON:0003504 (cardiac atrioventricular valve), UBERON:0002094 (interatrial septum), UBERON:0002099 (interventricular septum), UBERON:0002348 (endocardium).

---

## 8. Temporal Development

**Onset:** **Congenital** — the structural defect forms during embryonic cardiac septation (weeks 4–8 of human development). Clinical symptoms emerge in the **neonatal-to-infantile** period, with mean symptom onset ~50 ± 75 days in complete AVSD ([PMID: 9532811](https://pubmed.ncbi.nlm.nih.gov/9532811/)). Onset pattern is **insidious-to-subacute** as pulmonary vascular resistance falls postnatally and the left-to-right shunt increases.

**Progression:** Without repair, the course is **progressive** — pulmonary overcirculation → congestive heart failure → pulmonary vascular obstructive disease. "*The natural history ... is one of unrelenting development of pulmonary vascular obstructive disease*" ([PMID: 1943197](https://pubmed.ncbi.nlm.nih.gov/1943197/)). Partial AVSD may progress more slowly and occasionally present in adulthood.

**Critical periods / windows of intervention:** Complete AVSD is repaired at **~3–6 months of age** to preempt irreversible pulmonary vascular disease. Late repair (≥6 months) can yield comparable outcomes in resource-limited settings ([PMID: 42079968](https://pubmed.ncbi.nlm.nih.gov/42079968/)), but advanced pulmonary vascular disease may already be established at operation ([PMID: 1943197](https://pubmed.ncbi.nlm.nih.gov/1943197/)). **Remission** is treatment-induced (surgical repair); spontaneous resolution does not occur for complete AVSD. Disease is **lifelong** — repaired patients require ongoing surveillance for LAVV regurgitation, LVOT obstruction, and arrhythmias.

---

## 9. Inheritance and Population

**Epidemiology:** AVSD accounts for **~4–7% of all congenital cardiac malformations** ([PMID: 37612667](https://pubmed.ncbi.nlm.nih.gov/37612667/)) and ~2.6% of pediatric CHD hospitalizations; US prevalence increased over 2016–2020 ([PMID: 38277408](https://pubmed.ncbi.nlm.nih.gov/38277408/)). It is the most common CHD in Down syndrome (44.4%; [PMID: 39104126](https://pubmed.ncbi.nlm.nih.gov/39104126/)) and, conversely, ~54.7% of AVSD cases occur with Down syndrome ([PMID: 37667895](https://pubmed.ncbi.nlm.nih.gov/37667895/)).

**Inheritance pattern:** Predominantly **multifactorial/polygenic** with strong chromosomal (trisomy 21) contribution. Non-syndromic familial cases show **oligogenic** inheritance (e.g., co-occurring GDF1+NOTCH1; BMPR1A co-segregating with a chr1 linkage region) rather than a single Mendelian gene ([PMID: 38975735](https://pubmed.ncbi.nlm.nih.gov/38975735/); [PMID: 30814609](https://pubmed.ncbi.nlm.nih.gov/30814609/)). **Penetrance is incomplete** and **expressivity is variable** — consistent with CRELD1 being susceptibility rather than sufficient ([PMID: 15096951](https://pubmed.ncbi.nlm.nih.gov/15096951/)). Genetic anticipation and repeat-expansion mechanisms are **not applicable**.

**Population demographics:**
- **Down syndrome** is the dominant demographic association.
- **Sex ratio:** slight **female predominance** — girl:boy ratio 1.17:1 in a population-based Bohemian study ([PMID: 7997413](https://pubmed.ncbi.nlm.nih.gov/7997413/)); in Chinese CAVC-with-DS cases the female:male ratio was 1.6:1.0 ([PMID: 34627233](https://pubmed.ncbi.nlm.nih.gov/34627233/)).
- **Age distribution:** presents in infancy; a growing adult congenital population exists (partial AVSD, repaired complete AVSD).
- Consanguinity and founder effects are relevant for rare recessive/syndromic forms but not central to AVSD epidemiology.

---

## 10. Diagnostics

**Echocardiography is the gold standard** — both fetal and postnatal. The diagnostic plane is the **four-chamber view** demonstrating a common AV junction, common AV valve, and the ostium primum and inlet communications: "*the four-chamber views ... showed the atrioventricular septal defect and a common AV valve*" ([PMID: 36766561](https://pubmed.ncbi.nlm.nih.gov/36766561/)).

- **Prenatal detection:** high — antenatal diagnosis of complete AVSD ranges **57–92%** ([PMID: 27981284](https://pubmed.ncbi.nlm.nih.gov/27981284/)); increased detection has made AVSD "*the most common fetal cardiac diagnosis*" ([PMID: 34196822](https://pubmed.ncbi.nlm.nih.gov/34196822/)). Expert fetal echo shows **sensitivity 90–100%**, specificity/NPV 97–100%, PPV 85–100%, with Cohen's kappa >0.9 vs postnatal MRI ([PMID: 37240614](https://pubmed.ncbi.nlm.nih.gov/37240614/)).
- **AI-assisted detection:** the atrial-to-ventricular length ratio (AVLR) via CNN landmark detection is greater in AVSD than controls (P < 0.0001, AUC up to 0.992; [PMID: 38323184](https://pubmed.ncbi.nlm.nih.gov/38323184/)); FINE/STIC 4D identified the common AV valve in 100% of four-chamber volumes with autopsy confirmation ([PMID: 36766561](https://pubmed.ncbi.nlm.nih.gov/36766561/)).
- **ECG:** classically shows a **superior/leftward ("northwest") QRS axis** with AV conduction delay.
- **Cardiac MRI/CT** and **cardiac catheterization** (for pulmonary vascular resistance assessment) are adjuncts.

**Genetic testing** is integral given the aneuploidy link. Among unselected CHD fetuses, positive genetic diagnosis was **highest for AVSD at 36.8%** (chromosomal microarray detecting aneuploidy/pathogenic CNV in 16.7% overall; exome sequencing adding 6.7%; [PMID: 33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/)). Recommended workup: **karyotype/chromosomal microarray (CMA)** first-line (to detect trisomy 21 and pathogenic CNVs), with **exome sequencing** for non-isolated/syndromic or CMA-negative cases; **MLPA CHD panels** (GATA4, NKX2-5, TBX5, BMP4, CRELD1, 22q11.2) offer a cheaper first-tier screen ([PMID: 29952356](https://pubmed.ncbi.nlm.nih.gov/29952356/)).

**Clinical criteria & differential diagnosis:** Diagnosis is anatomic (echo-based). Differentials include isolated ostium primum/secundum ASD, isolated inlet VSD, common atrium (near-complete absence of interatrial septum; [PMID: 34993374](https://pubmed.ncbi.nlm.nih.gov/34993374/)), and heterotaxy-associated AVSD (AVSD is the most common cardiac anomaly in atrial isomerism; [PMID: 28603940](https://pubmed.ncbi.nlm.nih.gov/28603940/)).

**Screening:** Because ~half of children with Down syndrome have CHD (most commonly AVSD), **echocardiographic screening of all newborns/infants with Down syndrome** is standard, though access barriers limit it in resource-poor settings ([PMID: 41877065](https://pubmed.ncbi.nlm.nih.gov/41877065/)).

---

## 11. Outcome / Prognosis

**Survival after repair is excellent and has improved across surgical eras.**

| Cohort / setting | Outcome | PMID |
|---|---|---|
| 27-year single-center (n=248) | Survival 88.3% (10y), 83.8% (15y), 79.6% (25y); prematurity HR 2.43 | [40154545](https://pubmed.ncbi.nlm.nih.gov/40154545/) |
| Australian multi-institutional (n=829) | Operative mortality 3.3%; survival 91.7/90.7/88.7% at 10/15/20y | [34002204](https://pubmed.ncbi.nlm.nih.gov/34002204/) |
| Double-patch series (n=202) | In-hospital mortality 0.5%; freedom from reop 91.8/86.9/86.9% at 5/10/15y | [37612667](https://pubmed.ncbi.nlm.nih.gov/37612667/) |
| Single-patch, up to 40y (n=100) | Hospital mortality 11% (older era); QoL excellent/good 81%; normal LV in all | [34953470](https://pubmed.ncbi.nlm.nih.gov/34953470/) |
| Partial/transitional (n=136) | No deaths; 2.9% reoperation at ~4y | [41659084](https://pubmed.ncbi.nlm.nih.gov/41659084/) |
| US NIS <1yr (n=61,101) | Overall AVSD mortality 6.3% | [37667895](https://pubmed.ncbi.nlm.nih.gov/37667895/) |

**Morbidity / disease course:** The dominant late complication is **left AV valve (LAVV) regurgitation**, the principal reoperation driver, followed by **LVOT obstruction** ([PMID: 41971883](https://pubmed.ncbi.nlm.nih.gov/41971883/); [PMID: 40208292](https://pubmed.ncbi.nlm.nih.gov/40208292/)). AVSD carries **among the highest long-term arrhythmia risk of all CHDs** (advanced AV block, atrial flutter/fibrillation; overall CHD arrhythmia HR 16.4, 95% CI 14.4–18.7; [PMID: 39233212](https://pubmed.ncbi.nlm.nih.gov/39233212/)). Pulmonary hypertension is a key complication, more frequent in Down syndrome (4.3% vs 2.8%, P < 0.001; [PMID: 37667895](https://pubmed.ncbi.nlm.nih.gov/37667895/)).

**Prognostic factors:** prematurity and low birth weight (mortality), pulmonary hypertension, prior pulmonary artery banding, surgical era, non-Down status and moderate postoperative LAVV regurgitation (reoperation risk; [PMID: 34002204](https://pubmed.ncbi.nlm.nih.gov/34002204/)). Interestingly, older age at repair and Down syndrome were associated with **decreased** LAVV reintervention risk ([PMID: 40208292](https://pubmed.ncbi.nlm.nih.gov/40208292/)). A high postoperative leuko-glycemic index predicts prolonged mechanical ventilation and acute kidney injury in Down-syndrome infants ([PMID: 41764019](https://pubmed.ncbi.nlm.nih.gov/41764019/)).

---

## 12. Treatment

**Definitive treatment is surgical biventricular repair** — closure of the atrial (ostium primum) and ventricular components and reconstruction of the left AV valve (including cleft closure). **NCIT concept:** cardiac surgical repair of septal defect.

**Surgical techniques:**
- **Classic single-patch, modified single-patch ("Australian"/Nunn technique), and two-patch (double-patch) repair.** The Nunn-modified single-patch achieves >90% freedom from LAVV reoperation and >97% freedom from LVOT obstruction at 10–15 years ([PMID: 41313357](https://pubmed.ncbi.nlm.nih.gov/41313357/)).
- Complete AVSD is repaired **in infancy (~3–6 months)** to prevent irreversible pulmonary vascular disease. "*Early intervention, in the first 6 months ... gives comparable acceptable results to later repair; Trisomy 21 was not found to be a risk factor for early intervention*" ([PMID: 34350818](https://pubmed.ncbi.nlm.nih.gov/34350818/)). The modified single-patch shortened bypass time (71 vs 99 min, P = 0.001), and adding posterior annuloplasty reduced postoperative LAVV regurgitation (2+ regurgitation 43% → 7%, P = 0.03).
- Complete cleft closure inhibits significant postoperative LAVV regurgitation (OR 0.36, 95% CI 0.14–0.93; [PMID: 39578279](https://pubmed.ncbi.nlm.nih.gov/39578279/)). Refractory cases require **valve replacement**.

**Pharmacotherapy (bridging / supportive):** Anti-heart-failure therapy — **diuretics (furosemide, spironolactone), afterload reduction (ACE inhibitors/enalapril), digoxin** — plus nutritional support. Vasodilators lower vascular resistance but can induce hypotension because systemic output does not rise ([PMID: 10812553](https://pubmed.ncbi.nlm.nih.gov/10812553/)). **Pulmonary artery banding** is an occasional palliative bridge (but prior banding predicts later mortality; [PMID: 34002204](https://pubmed.ncbi.nlm.nih.gov/34002204/)). For established pulmonary hypertension, calcium-channel blockers (nifedipine) and modern PH-targeted therapy are used ([PMID: 2116616](https://pubmed.ncbi.nlm.nih.gov/2116616/); [PMID: 37794522](https://pubmed.ncbi.nlm.nih.gov/37794522/)).

**Advanced/gene/cell therapies:** Not applicable — no gene, RNA, or cell therapies exist for AVSD; treatment is structural/surgical.

**Adult AVSD repair** is safe with low early mortality but notable late arrhythmia and residual LAVV reoperation ([PMID: 40936386](https://pubmed.ncbi.nlm.nih.gov/40936386/)).

---

## 13. Prevention

**Primary prevention** targets modifiable maternal risk factors:
- **Optimize maternal glycemic control** before and during pregnancy (pregestational diabetes aPR ~6.7; [PMID: 23061687](https://pubmed.ncbi.nlm.nih.gov/23061687/)).
- **Periconceptional folic acid / folate-rich diet** — protective for CHD (aOR 0.64; [PMID: 32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/)); provider awareness of folate's cardiac benefits is low and warrants education ([PMID: 41041190](https://pubmed.ncbi.nlm.nih.gov/41041190/)).
- **Weight management** and smoking cessation.

**Secondary prevention (early detection):**
- **Prenatal screening** via the four-chamber view at the mid-trimester anomaly scan; quality of imaging strongly affects detection ([PMID: 31131945](https://pubmed.ncbi.nlm.nih.gov/31131945/)).
- **Prenatal detection of AVSD prompts karyotype/aneuploidy workup** given the strong trisomy-21 association ([PMID: 36766561](https://pubmed.ncbi.nlm.nih.gov/36766561/)).
- **Routine echocardiographic screening of all infants with Down syndrome** ([PMID: 41877065](https://pubmed.ncbi.nlm.nih.gov/41877065/)).

**Tertiary prevention (complication prevention):** timely surgical repair before irreversible pulmonary vascular disease; lifelong surveillance for LAVV regurgitation, LVOT obstruction, arrhythmias, and pulmonary hypertension.

**Genetic counseling:** For families with AVSD/CHD, counseling addresses recurrence risk, oligogenic/multifactorial inheritance, and prenatal diagnostic options (CMA, exome sequencing, fetal echocardiography). **Immunization/public-health/infectious prevention:** not applicable.

---

## 14. Other Species / Natural Disease

AVSD (atrioventricular canal defect) **occurs naturally across mammals**: "*The defect has been described in human beings, dogs, cats, pigs, and horses*," and a 2021 report added the **first documented complete AV canal defect in a pet ferret** (*Mustela putorius furo*) — a 4-year-old male with a loud systolic murmur, dyspnea, cardiomegaly, and pulmonary edema, echocardiographically showing a large ASD, AV valve dysplasia, and VSD, managed palliatively with furosemide, spironolactone, enalapril, and diltiazem ([PMID: 33482816](https://pubmed.ncbi.nlm.nih.gov/33482816/)).

- **Taxonomy / NCBI Taxon:** *Homo sapiens* (9606), *Canis lupus familiaris* (9615), *Felis catus* (9685), *Sus scrofa* (9823), *Equus caballus* (9796), *Mustela putorius furo* (9669).
- **Comparative biology:** The same developmental program — endocardial cushion formation via EndoMT under TGF-β/BMP/Notch/Wnt control — operates across vertebrates, indicating strong **evolutionary conservation** of AV-canal development. Orthologous genes (*Creld1*, *Nfatc1*, *Notch1*, *Gata4*) are conserved across species.
- **Veterinary relevance:** AVSD/AV canal defect is a recognized congenital cardiac malformation in companion animals, typically presenting with murmur and congestive heart failure signs.
- **Zoonotic potential:** none (developmental malformation).

---

## 15. Model Organisms

| Model | Type | Phenotype recapitulation | Key limitation | PMID |
|---|---|---|---|---|
| *Creld1* KO mouse (global/conditional) | Mammalian knockout | Embryonic lethal; essential for septum & valve formation; dissects endocardial calcineurin/NFATc1/VEGF axis | Global KO lethal; requires conditional approach | [33773996](https://pubmed.ncbi.nlm.nih.gov/33773996/), [24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/) |
| *Dnah11*, *Mks1* ENU mutants | Mammalian (cilia genes) | Heritable recessive AVSD via L/R axis + Hedgehog/second heart field | Specific to cilia-pathway subset | [27340223](https://pubmed.ncbi.nlm.nih.gov/27340223/) |
| Ts65Dn (DS model) | Trisomy (>100 Hsa21 orthologs) | Cardiovascular anomalies (right aortic arch + septal defects) in 8.3% of trisomic newborns; sensitized modifier background | Incomplete Hsa21 coverage; low CHD penetrance | [17019652](https://pubmed.ncbi.nlm.nih.gov/17019652/), [22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/) |
| Ts16 (trisomy 16) | Trisomy | Deficient AV septation (primum ASD + VSD) | Atypical conotruncal features (DORV, PTA, TOF) resembling DiGeorge; "*No heart had the typical morphology seen in ... Down's syndrome*" | [9231034](https://pubmed.ncbi.nlm.nih.gov/9231034/), [11066038](https://pubmed.ncbi.nlm.nih.gov/11066038/) |
| Tc1 (transchromosomal) | Human Chr21 in mouse | Models dosage of an intact extra Hsa21 | Mosaicism; partial | [15068235](https://pubmed.ncbi.nlm.nih.gov/15068235/) |
| DSCR1-restored Ts16 | Dosage-rescue | DSCR1 restoration did NOT rescue cardiac anomalies → supports oligogenic model | Single-gene rescue insufficient | [15906378](https://pubmed.ncbi.nlm.nih.gov/15906378/) |
| DSCAM+COL6A2 overexpression mouse | Transgenic | Co-overexpression → ~50% mortality + ASD + hypertrophy | Not a full trisomy model | [22072978](https://pubmed.ncbi.nlm.nih.gov/22072978/) |
| *Mbnl1*-null mouse | Knockout | Precocious TGF-β/EMT; valve dysmorphia + secundum septal defects | Valve phenotype more than classic AVSD | [26472242](https://pubmed.ncbi.nlm.nih.gov/26472242/) |
| Notch pathway mice (*Jag1/Notch1/RBPJ*) | Conditional KO | Enlarged valve cusps, BAV, septal defects | Pathway-specific | [27056911](https://pubmed.ncbi.nlm.nih.gov/27056911/) |
| Zebrafish (NFATC1 mutants; AVC transcriptome; MFNG) | Vertebrate | Cardiac looping/AV canal patterning defects; conserved EMT/TGF-β/Notch/Wnt | Two-chamber heart | [30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/), [34557935](https://pubmed.ncbi.nlm.nih.gov/34557935/), [39528804](https://pubmed.ncbi.nlm.nih.gov/39528804/) |
| Human iPSC-derived pre-valvular endocardial cells | In vitro | BMP2-responsive AVC EndoMT; "valve disease in a dish" | Lacks in vivo hemodynamics/tissue context | [31028265](https://pubmed.ncbi.nlm.nih.gov/31028265/) |
| Syrian hamster; chick cushion explants | Vertebrate/ex vivo | OFT/AV cushion EndoMT; TGF-β regulation | Model-specific | [40074779](https://pubmed.ncbi.nlm.nih.gov/40074779/), [26472242](https://pubmed.ncbi.nlm.nih.gov/26472242/) |

**Overall model interpretation:** Single-gene KOs (*Creld1*, Notch pathway) faithfully model the **mechanistic EndoMT/calcineurin-NFATc1 axis**, while Down-syndrome trisomy models (Ts65Dn, Ts16, Tc1) only **partially** recapitulate the human balanced AVSD morphology — a key limitation. The DSCR1-rescue negative result and *Creld1*/*Hey2* modifier crosses jointly support an **oligogenic, dosage-threshold model** ([PMID: 15906378](https://pubmed.ncbi.nlm.nih.gov/15906378/); [PMID: 22523272](https://pubmed.ncbi.nlm.nih.gov/22523272/)). **Resources:** MGI, IMPC, ZFIN, Cellosaurus.

---

## Mechanistic Model / Interpretation

AVSD is best understood as a **convergent endpoint of failed atrioventricular-canal endocardial cushion development**, reached by multiple upstream routes (chromosomal, oligogenic, environmental) that all impair **endothelial-to-mesenchymal transition** and its downstream valve/septum morphogenesis. The pathway logic:

```
Upstream perturbations              Convergent module                 Structural outcome
──────────────────────  ───────────────────────────────────  ──────────────────────────
Trisomy 21 dosage ──┐
CRELD1 / NFATC1 ─────┤    CRELD1→Calcineurin/NFATc1→VEGF        Deficient AV septation
GATA4/6, NOTCH1 ─────┼──► TGF-β / BMP / Notch / Wnt / NOX2 ──►  + abnormal common/cleft
BMPR1A, GDF1, HEY2 ──┤    driven endocardial EndoMT & valve     AV valve
Maternal diabetes ───┘    remodeling                            (Rastelli A/B/C)
```

Two features make AVSD distinctive among CHDs: (1) its **unusually tight link to trisomy 21**, explained by chr21 gene-dosage effects (DSCAM+COL6A2 cooperativity; HMGN1 chromatin reprogramming) acting on a threshold-sensitized cushion program; and (2) the fact that its **major residual clinical problem (LAVV regurgitation)** is a direct anatomic consequence of the abnormal common-valve leaflet architecture, which surgery can improve but not perfectly normalize.

---

## Evidence Base — Key Literature

| PMID | Contribution |
|---|---|
| [15096951](https://pubmed.ncbi.nlm.nih.gov/15096951/) | CRELD1 as first non-syndromic susceptibility gene; establishes AVSD as multigenic; trisomy-21 link |
| [30007050](https://pubmed.ncbi.nlm.nih.gov/30007050/) | NFATC1 LOF mutations cause AVSD; calcineurin/NFAT axis |
| [24697899](https://pubmed.ncbi.nlm.nih.gov/24697899/) | Mouse Creld1→NFATc1→VEGF endocardial proliferation mechanism |
| [29549339](https://pubmed.ncbi.nlm.nih.gov/29549339/) | AVSD results from impaired cushion EndoMT initiating in the AVC |
| [27056911](https://pubmed.ncbi.nlm.nih.gov/27056911/) / [28172500](https://pubmed.ncbi.nlm.nih.gov/28172500/) / [26893350](https://pubmed.ncbi.nlm.nih.gov/26893350/) | Notch / BMP / Wnt control of cushion EMT and septal/valve defects |
| [22072978](https://pubmed.ncbi.nlm.nih.gov/22072978/) / [41125893](https://pubmed.ncbi.nlm.nih.gov/41125893/) | Chr21 gene-dosage mechanisms (DSCAM+COL6A2; HMGN1) |
| [25996639](https://pubmed.ncbi.nlm.nih.gov/25996639/) | Exome-derived rare-variant enrichment; 6 AVSD genes; 40% unknown etiology |
| [23061687](https://pubmed.ncbi.nlm.nih.gov/23061687/) / [33876578](https://pubmed.ncbi.nlm.nih.gov/33876578/) | Maternal diabetes/obesity as environmental risk factors |
| [32092068](https://pubmed.ncbi.nlm.nih.gov/32092068/) | Folate protective; maternal risk factors for CHD |
| [37240614](https://pubmed.ncbi.nlm.nih.gov/37240614/) / [34196822](https://pubmed.ncbi.nlm.nih.gov/34196822/) / [33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/) | Echocardiographic diagnosis; most common fetal cardiac Dx; highest genetic yield |
| [40154545](https://pubmed.ncbi.nlm.nih.gov/40154545/) / [34002204](https://pubmed.ncbi.nlm.nih.gov/34002204/) / [34953470](https://pubmed.ncbi.nlm.nih.gov/34953470/) | Long-term surgical survival & QoL outcomes |
| [41971883](https://pubmed.ncbi.nlm.nih.gov/41971883/) / [40208292](https://pubmed.ncbi.nlm.nih.gov/40208292/) | LAVV regurgitation as dominant reoperation driver |
| [39892564](https://pubmed.ncbi.nlm.nih.gov/39892564/) / [10946038](https://pubmed.ncbi.nlm.nih.gov/10946038/) / [8347012](https://pubmed.ncbi.nlm.nih.gov/8347012/) | Rastelli anatomy; DS outlet-septum malalignment; type-A PVD risk |
| [39233212](https://pubmed.ncbi.nlm.nih.gov/39233212/) | AVSD among highest arrhythmia-risk CHDs |
| [33482816](https://pubmed.ncbi.nlm.nih.gov/33482816/) | Cross-species natural occurrence (dog, cat, pig, horse, ferret) |
| [1943197](https://pubmed.ncbi.nlm.nih.gov/1943197/) / [10812553](https://pubmed.ncbi.nlm.nih.gov/10812553/) | Left-to-right shunt physiology; unrelenting pulmonary vascular disease |

**Consistency:** Findings were highly consistent across human clinical cohorts, model organisms, and in vitro systems. No hypothesis was refuted; all 5 formal hypotheses (H001–H005) were supported.

---

## Limitations and Knowledge Gaps

1. **~40% of non-syndromic AVSD lacks a molecular diagnosis** ([PMID: 25996639](https://pubmed.ncbi.nlm.nih.gov/25996639/)) — much of the oligogenic/polygenic architecture and regulatory (non-coding) contribution remains uncharacterized.
2. **DS models imperfectly recapitulate human balanced AVSD morphology** ([PMID: 9231034](https://pubmed.ncbi.nlm.nih.gov/9231034/)); the precise chr21 gene(s) and dosage thresholds driving human AVSD are not fully resolved (HMGN1 and DSCAM+COL6A2 are leading but not sole candidates).
3. **Environmental risk estimates derive largely from broad CHD studies**, not AVSD-specific cohorts; folate/diabetes effect sizes for AVSD alone are less precise.
4. **No molecular/epigenetic biomarker** exists for prenatal risk stratification or postoperative LAVV-regurgitation prediction; diagnosis remains imaging-based.
5. **Limited data on adult natural history** of unrepaired/partial AVSD and on long-term neurodevelopmental and phenotype-stratified QoL outcomes.
6. **Penetrance/expressivity quantification** for individual susceptibility variants (e.g., CRELD1) is incomplete.

---

## Proposed Follow-up Experiments / Actions

1. **Large-scale trio whole-genome sequencing** of non-syndromic AVSD to capture regulatory/non-coding and structural variants and resolve the "missing 40%," with statistical modeling of oligogenic burden.
2. **Single-cell / spatial transcriptomics of the developing human AV canal** (and iPSC-derived pre-valvular endocardial cells) to map cell-type-specific EndoMT programs and how CRELD1/NFATC1/HMGN1 perturbations reprogram them.
3. **Dissect chr21 dosage** with combinatorial CRISPR titration of HMGN1, DSCAM, COL6A2 (and modifiers *Creld1*, *Hey2*) on trisomic backgrounds to define the defect threshold and rank causal drivers.
4. **Prospective AVSD-specific gene–environment study** quantifying interaction between maternal glycemic control/folate status and fetal genotype on AVSD risk and severity.
5. **Develop predictive tools for LAVV regurgitation** — integrate 3D-echo valve morphometry (Rastelli type, leaflet geometry) with clinical/genetic data to guide repair technique and surveillance.
6. **Improve prenatal detection** through validation and deployment of AI-assisted four-chamber-view screening (AVLR, FINE/STIC) in general obstetric settings, paired with reflex CMA/exome workflows.
7. **Optimize periconceptional prevention** by testing structured maternal diabetes-control and folate-supplementation programs, and by educating healthcare providers on folate's cardiac benefits.

---

*Report compiled from 22 confirmed findings, 5 supported hypotheses, and 92 reviewed papers across 10 investigation iterations. Evidence sources: human clinical cohorts, population registries, model organisms (mouse, zebrafish, hamster, chick), and in vitro iPSC systems.*


## Artifacts

- [OpenScientist final report](Atrioventricular_Septal_Defect-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Atrioventricular_Septal_Defect-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:29549339
2. PMID:37612667
3. PMID:39104126
4. PMID:37667895
5. PMID:15096951
6. PMID:30007050
7. PMID:24697899
8. PMID:22072978
9. PMID:41125893
10. PMID:23061687
11. PMID:32092068
12. PMID:1943197
13. PMID:10812553
14. PMID:37240614
15. PMID:34196822
16. PMID:33142350
17. PMID:40154545
18. PMID:34002204
19. PMID:8347012
20. PMID:19760623
21. PMID:25328912
22. PMID:25996639
23. PMID:33179873
24. PMID:22523272
25. PMID:33876578
26. PMID:9532811
27. PMID:34953470
28. PMID:42037320
29. PMID:36816019
30. PMID:34627233
31. PMID:26472242
32. PMID:28172500
33. PMID:27056911
34. PMID:39528804
35. PMID:26893350
36. PMID:32655758
37. PMID:31028265
38. PMID:39892564
39. PMID:10946038
40. PMID:42079968
41. PMID:38277408
42. PMID:38975735
43. PMID:30814609
44. PMID:7997413
45. PMID:36766561
46. PMID:27981284
47. PMID:38323184
48. PMID:29952356
49. PMID:34993374
50. PMID:28603940
51. PMID:41877065
52. PMID:41971883
53. PMID:40208292
54. PMID:39233212
55. PMID:41764019
56. PMID:41313357
57. PMID:34350818
58. PMID:39578279
59. PMID:2116616
60. PMID:37794522
61. PMID:40936386
62. PMID:41041190
63. PMID:31131945
64. PMID:33482816
65. PMID:15906378
66. PMID:9231034