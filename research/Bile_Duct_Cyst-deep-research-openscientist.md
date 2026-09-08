---
title: Choledochal cyst (bile duct cyst) pathophysiology for dismech curation
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T15:41:15.863802'
end_time: '2026-08-31T16:01:55.920530'
duration_seconds: 1240.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Choledochal Cyst
  mondo_id: MONDO:0018805
  category: Congenital biliary anomaly / cystic dilatation of the bile duct with pancreaticobiliary
    maljunction and malignant potential
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
citation_count: 56
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bile_Duct_Cyst-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bile_Duct_Cyst-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Choledochal Cyst
- **MONDO ID:** MONDO:0018805 (if available)
- **Category:** Congenital biliary anomaly / cystic dilatation of the bile duct with pancreaticobiliary maljunction and malignant potential

## Research Objectives

Please provide a comprehensive research report on **Choledochal Cyst** covering all of the
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

# Choledochal Cyst (Congenital Biliary Dilatation): A Comprehensive Disease Characterization

**Disease:** Choledochal Cyst | **MONDO:** MONDO:0018805 | **Category:** Congenital biliary anomaly with pancreaticobiliary maljunction and malignant potential

**Evidence base:** This report synthesizes 87 primary papers and reviews across a 10-iteration investigation, yielding 20 confirmed findings and 5 supported hypotheses. All content derives from aggregated disease-level clinical/surgical case series, reviews, and animal-model studies — not from a single patient EHR.

---

## Summary

**Choledochal cyst (CC)** — also termed congenital biliary dilatation, choledochal malformation, or bile duct cyst — is a rare congenital cystic or fusiform dilatation of the intra- and/or extrahepatic biliary tree. In the great majority of cases it arises on a background of **pancreaticobiliary maljunction (PBM)**: the pancreatic and common bile ducts fuse *outside* the duodenal wall, forming an abnormally long common channel (≥6 mm) that lies beyond the regulatory control of the sphincter of Oddi. Because hydrostatic pressure in the pancreatic duct exceeds that in the bile duct, activated pancreatic enzymes reflux persistently into the biliary tree ("pancreatobiliary reflux"), chronically injuring the biliary epithelium. This single mechanistic lesion produces both the **cystic dilatation** itself and, over decades, a **hyperplasia–dysplasia–carcinoma sequence** that gives CC its defining clinical importance: a lifelong, elevated risk of cholangiocarcinoma and gallbladder carcinoma (20–30× the general population, mean malignancy age ~32 years).

The disease shows a striking **female predominance (~3–4:1)** and a marked **East-Asian geographic clustering** (~1 in 1,000 live births in Asia versus roughly 1:38,000–1:150,000 in Western populations). Clinically it presents with an age-dependent classic triad — abdominal pain, jaundice, and a palpable right-upper-quadrant mass — that is more complete in children and largely replaced by pain/pancreatitis in adults. Diagnosis is anchored by **magnetic resonance cholangiopancreatography (MRCP)**, now the gold standard, which non-invasively demonstrates both the biliary dilatation and the causal maljunction. Anatomic subtypes follow the **Todani classification (Types I–V)**, with Types I and IV being the most common and carrying the highest malignant risk.

Treatment is **complete excision of the extrahepatic cyst plus cholecystectomy and Roux-en-Y hepaticojejunostomy** — a flow-diversion operation that removes premalignant epithelium and diverts pancreatic juice. Minimally invasive (laparoscopic and robotic) approaches now predominate and reduce complications. Prognosis after complete excision is generally excellent, but a **residual, late-rising biliary-cancer risk persists in retained duct segments** (cumulative incidence ~1.6% at 15 years, 3.9% at 20 years, 11.3% at 25 years), mandating decades-long surveillance with CA19-9 and ultrasound. Because CC is sporadic/multifactorial with no established Mendelian gene, there is no genetic, carrier, or newborn screening; prevention is dominated by prophylactic surgery and lifelong surveillance.

---

## Key Findings

### 1. Disease Information, Identifiers, and the Todani Classification (F015)

Choledochal cysts are rare congenital cystic dilatations of the intra- and/or extrahepatic biliary tree, first described by Vater and Ezler in 1723. Key identifiers are: **MONDO:0018805; MeSH D015529** (Choledochal Cyst); **ICD-10 Q44.4** (congenital); **ICD-11 LB20.2; Orphanet ORPHA:33313**. Common synonyms/alternative names include congenital biliary dilatation, choledochal malformation, bile duct cyst, and cystic dilatation of the bile duct. In 1977, Todani and colleagues modified the original Alonso-Lej (1959) scheme into five types [PMID: 28364277]:

| Todani Type | Description | Notes |
|---|---|---|
| **Type I** | Extrahepatic bile duct dilatation (Ia cystic, Ib focal/segmental, Ic fusiform) | Most common (~50–80%) |
| **Type II** | True supraduodenal diverticulum of the extrahepatic duct | Rare |
| **Type III** | Choledochocele (dilatation of intraduodenal/intramural distal CBD) | Often treated endoscopically |
| **Type IV** | IVa: intrahepatic + extrahepatic; IVb: multiple extrahepatic cysts | Second most common (~33%) |
| **Type V** | Caroli disease (intrahepatic only) | With hepatic fibrosis = Caroli *syndrome* |

A **Type VI** variant (cystic-duct involvement) has been proposed beyond the classical scheme [PMID: 34377608]. As the source review states: *"In 1977, Todani and colleagues modified the original Alonso-Lej classification to include five types of CC. Type I and IV are the most common and most likely to be associated with malignancy"* [PMID: 28364277]. Information for this entry derives from **aggregated disease-level clinical/surgical case series and reviews**, not individual EHR data.

**Ontology anchors:** MONDO:0018805; UBERON:0001174 (common bile duct).

### 2. Etiology — Two Competing Theories; Non-Mendelian Basis (F017)

The exact cause of CC is unknown and likely multifactorial. Two dominant theories persist [PMID: 35741793; PMID: 25588714]:

1. **The pancreaticobiliary maljunction (reflux) theory** (Babbitt, 1969): an anomalous long common channel permits reflux of activated pancreatic juice into the bile duct, causing chronic inflammation, mural weakening, and cystic dilatation.
2. **The congenital stenosis/obstruction theory**: antenatal distal biliary obstruction (or unequal epithelial proliferation during embryologic duct development) produces proximal ductal dilatation.

These are not mutually exclusive, and different Todani subtypes may arise by different mechanisms. Crucially, *"Although family cases or CC associated with other anomalies have been reported, the molecular pathogenesis of CC is still poorly understood"* [PMID: 35741793]. **No single Mendelian gene has been established**; the disorder is regarded as sporadic/multifactorial, so there is no diagnostic genetic test, carrier screening, or defined inheritance pattern. The initiating lesion (PBM) is congenital, forming in embryogenesis when the terminal bile duct joins a ventral pancreatic duct outside the duodenal wall. No specific environmental toxin, lifestyle factor, or infectious agent is established as causal; the primary "environmental" driver is the endogenous mixture of refluxed pancreatic juice and bile acting on the biliary epithelium.

### 3. Epidemiology — Female Predominance and Asian Clustering (F001, F012)

CC shows a strong female predominance and a striking East–West geographic gradient. Incidence is **~1 in 1,000 live births in Asian populations** versus much rarer in the West; a Finnish nationwide series documented a rising estimated incidence from **1:128,000 to 1:38,000 over 37 years (p=0.017)** [PMID: 25123318]. Female:male ratios in surgical cohorts range from ~2.3:1 in adults to ~3.6:1 in children (62 girls/17 boys in a Korean series [PMID: 41368339]; ~71% female in the Finnish series [PMID: 25123318]).

| Parameter | Value | Source |
|---|---|---|
| Asian incidence | ~1 in 1,000 live births | [PMID: 40570483] |
| Western incidence | 1:38,000 – 1:150,000 | [PMID: 25123318] |
| M:F ratio (children) | ~1:3 | [PMID: 19701664] |
| M:F ratio (adults) | ~1:2.3 | [PMID: 19701664] |
| Overall lifetime malignancy risk | ~7.5% | [PMID: 40570483] |
| Cystic vs fusiform onset age | 0.8 y vs 4.6 y (p=0.001) | [PMID: 25123318] |

*"the estimated total incidence rose from 1:128,000 to 1:38,000 (p = 0.017). Cystic CMs (42%) presented at younger age than fusiform CMs (47%) (0.8 vs. 4.6 years, p = 0.001)"* [PMID: 25123318]. Malignancy risk is *"more than 10% after the second decade of life in Asian patients"* [PMID: 31341359]. There is no established Mendelian inheritance, penetrance, founder effect, or consanguinity role — the female/Asian predominance is unexplained at the molecular level.

### 4. Clinical Phenotypes — The Age-Dependent Triad (F006, F014)

The **classic triad** is abdominal pain + jaundice + a palpable right-upper-quadrant mass, but the *complete* triad is uncommon and strongly age-dependent. In a 42-patient series, only 1 child (and no adult) had all three; children were far more likely to have ≥2 of the 3 signs (**82% vs 25%, p<0.05**), whereas adults most commonly presented with abdominal pain misattributed to pancreatitis (23%) [PMID: 7979612]. In a 79-patient series, *"the classic triad of jaundice, abdominal pain, and a mass was 6.7 times more common in group A [children] than in group B [adults]"* [PMID: 19701664].

| Phenotype | HPO term | Frequency / notes |
|---|---|---|
| Abdominal pain | HP:0002027 | ~85% (RUQ); dominant in adults |
| Jaundice | HP:0000952 | ~54%; more common in children |
| Palpable abdominal mass | HP:0032557 | ~38%; more common in children |
| Acute pancreatitis | HP:0001733 | Common in adults (misdiagnosed) |
| Cholangitis | HP:0030151 | Recurrent; episodic |
| Cholelithiasis/choledocholithiasis | HP:0001081 | Adults: gallstones 36.7% |
| Hepatomegaly | HP:0002240 | Variable |
| Conjugated hyperbilirubinemia / acholic stools | HP:0002908 | Neonatal presentation |
| Spontaneous cyst perforation | — | Rare pediatric emergency |

Component frequencies (13-patient series): right-upper-quadrant pain ~85%, jaundice ± cholangitis ~54%, palpable mass ~38% [PMID: 14768318]. Giant cysts (>10 cm) show pain and lump in 100% and the full triad in 60% versus only 14% for smaller cysts [PMID: 23686589]. Antenatally detected cases present as an asymptomatic fetal abdominal/hepatic cyst [PMID: 38582706]. Symptoms are typically **episodic/fluctuating** (recurrent cholangitis, colicky pain); severity ranges from asymptomatic (antenatal/incidental) to severe (perforation, secondary biliary cirrhosis, portal hypertension). Quality-of-life impact is driven by recurrent cholangitis/pancreatitis, the burden of major surgery, and the anxiety of lifelong cancer surveillance.

### 5. Mechanistic Causal Chain — From Maljunction to Carcinoma (F002, F010, F011)

This is the mechanistic heart of the disease. The ordered causal chain from initiating lesion to clinical manifestation:

```
(1) Congenital pancreaticobiliary maljunction (PBM)
    — pancreatic + bile ducts join OUTSIDE duodenal wall,
      long common channel >=6 mm, sphincter of Oddi cannot regulate junction
             |  LEADS TO
             v
(2) Pancreatobiliary reflux
    — pancreatic-duct pressure > bile-duct pressure ->
      persistent reflux of activated pancreatic enzymes into biliary tree
             |  RESULTS IN
             v
(3) Chronic biliary epithelial injury
    — refluxed enzymes + bile stasis + increased intraductal bile-acid concentration
             |
      +------+-----------------------------+
      v (branch A: dilatation)             v (branch B: carcinogenesis)
(5) increased intraductal pressure    (4) injury-repair cycles ->
    + distal obstruction                  epithelial HYPERPLASIA with
    (protein plugs, fatty-acid              early random KRAS mutation
    calcium stones) ->                          |
    CYSTIC/FUSIFORM DILATATION                  v
    = the choledochal cyst            (6) DYSPLASIA -> CARCINOMA sequence
                                          EARLY: KRAS, microsatellite instability,
                                                 COX-2, bcl-2, telomerase, HDAC1, AID, IL-33
                                          LATE:  cyclin D1, beta-catenin, DPC-4/Smad4,
                                                 stepwise TP53 accumulation
                                                   |  CULMINATES IN
                                                   v
                                       (7) Cholangiocarcinoma / gallbladder carcinoma
                                           (20-30x risk; mean age ~32 y)
```

**Supporting evidence.** The pressure-driven reflux step: *"Since hydrostatic pressure within the pancreatic duct is usually higher than that in the common bile duct, pancreatic juice frequently refluxes into the bile duct. As a result, pancreatic enzyme levels are generally very high in the bile and there is a related high incidence of biliary cancer"* [PMID: 19896105]. The histologic sequence: *"Pathological findings strongly suggest a hyperplasia-dysplasia-carcinoma sequence... Reflux of pancreatic enzymes, amylase, bile stasis, and an increased intraductal concentration of bile acids contribute to proliferative activity"* [PMID: 17187167].

**Temporal ordering of molecular events:** *"While microsatellite instability, k-ras mutations, expression of COX-2 and bcl-2, and increased telomerase activity seem to occur early; involvement of cyclin D1, beta-catenin, DPC-4/Smad4 and p53 appear later in carcinogenesis"* [PMID: 17187167].

**The primacy of TP53 over KRAS.** A laser-capture-microdissection NGS study (n=64) documented a **stepwise TP53 accumulation** across the injury-to-cancer field: control epithelium 10% → PBM epithelium without cancer 10% → peritumoral mucosa 38% → tumor tissue **75% (p<0.01)**; *"TP53 alteration more than KRAS mutation was revealed to underlie carci[nogenesis]"* [PMID: 34798839]. In frank cancer, KRAS is *not* PBM-specific: PBM-associated gallbladder cancer 16% (5/32) vs non-associated 8% (4/49), p=0.272 [PMID: 30882917]. Conversely, the inflammatory cytokine **IL-33 mRNA is significantly overexpressed** in PBM-associated gallbladder cancer and its background mucosa (p<0.001) [PMID: 30882917]. Even in childhood, *"The Ki-67 labeling index... and expressions of KRAS, p53, HDAC, and AID in the gallbladder epithelium were significantly higher... BTC may develop later in children with CBD and in adults with PBM, via HDAC and AID expression and through epigenetic and genetic regulation"* [PMID: 34132887].

**Molecular pathways implicated in biliary carcinogenesis:** TGF-β/Smad, IL-6/STAT-3, PI3K/AKT, Wnt, RAF/MEK/MAPK, and Notch [PMID: 24895231].

**Ontology anchors:** GO:0006954 (inflammatory response); GO:0008283 (cell population proliferation); CL:0000069 (biliary epithelial cell/cholangiocyte); CHEBI:3098 (bile acid).

### 6. Genetic / Molecular Information (F011, F017)

CC has **no established causal Mendelian gene**; it is sporadic/multifactorial [PMID: 35741793]. The molecular findings are those of *somatic* carcinogenesis in the injured epithelium, not germline disease-causing variants:

| Gene / marker | Alteration | Frequency | Timing |
|---|---|---|---|
| **TP53** | Somatic mutation/alteration | 10%→38%→75% (field→tumor) | Late, stepwise, dominant driver |
| **KRAS** | Somatic mutation | 13–63% hyperplasia; ~16% PBM cancer | Early, not PBM-specific in cancer |
| **EGFR** | Alteration | 20.6% of PBM-GBC | — |
| **RB1** | Alteration | 17.6% | — |
| **ERBB2** | Alteration | 17.6% | — |
| **IL-33** | mRNA overexpression | Significant (p<0.001) | Inflammatory, background + cancer |
| **HDAC (HDAC1)** | Overexpression | Elevated in CBD/PBM | Early epigenetic driver |
| **AID (AICDA)** | Overexpression | Elevated | Epigenetic/genetic mutator |

The genes involved are **germline-wild-type / somatically altered**; the functional consequence is loss of tumor-suppressor function (TP53, RB1, DPC-4/Smad4) and gain-of-function oncogenic signaling (KRAS, ERBB2/EGFR). **Epigenetic dysregulation (HDAC1, AID) plus microsatellite instability (~60% of dysplasia)** contribute even in childhood [PMID: 34132887; PMID: 14534681]. For **Type V (Caroli disease)**, when part of the ARPKD spectrum, the relevant gene is **PKHD1 (fibrocystin)** — see animal models below. No recurrent chromosomal abnormality (aneuploidy, translocation) is characteristic of CC.

**Ontology anchors:** HGNC:11998 (TP53), HGNC:6407 (KRAS), HGNC:9024 (PKHD1).

### 7. Anatomical Structures and Histopathology (F009)

The primary site is the **extrahepatic/common bile duct** (UBERON:0001174), with secondary involvement of the gallbladder (UBERON:0002110), intrahepatic bile ducts (UBERON:0001172), liver (UBERON:0002107), and pancreatic duct/common channel (UBERON:0009976). The affected body system is the **digestive/hepatobiliary system**. The target cell is the **biliary epithelial cell/cholangiocyte** (CL:0000069); the tissue is glandular/columnar epithelium with associated smooth muscle and connective tissue of the duct wall.

Cyst-wall histology shows *"ulceration, inflammation, fibrosis, and metaplasia"* [PMID: 24604978] — specifically loss of the columnar epithelial lining, absent/attenuated smooth muscle, dense fibrosis, chronic inflammation, and glandular/intestinal metaplasia. Intracholedochal cystic pressure (mean ~15 mmHg) correlates directly with hepatocellular damage and cholestasis and inversely with cyst-wall inflammatory change and bile amylase [PMID: 24604978]. Lateralization is not applicable (midline biliary structure); intrahepatic involvement (Types IVa/V) may be uni- or bilobar.

### 8. Temporal Development (F001, F004, F012, F019)

- **Onset:** Congenital (initiating lesion in embryogenesis); clinical onset ranges from antenatal detection through neonatal, pediatric, and adult presentation. Onset pattern is chronic/insidious, punctuated by acute episodes (cholangitis, pancreatitis). Cystic malformations present younger (median 0.8 y) than fusiform types (median 4.6 y) [PMID: 25123318].
- **Progression:** Chronic, lifelong. Cancer risk is age-dependent — *"The cancer-risk is low in childhood (<1% in the first decade), and shows a clear increase with age"* [PMID: 17187167], rising to 10–30% in adults.
- **Critical window:** Complete excision removes the reflux-injured epithelium; earlier surgery (even before 6 months) improves prognosis regarding intrahepatic-duct stones [PMID: 40097690]. Residual cancer risk rises sharply beyond 15 years post-excision [PMID: 22989043]. Disease course is not self-limiting; without excision it is a chronic, progressive, premalignant condition.

### 9. Diagnostics — MRCP as the Gold Standard (F008, F016)

Diagnosis uses multimodality imaging — ultrasound (first-line, often diagnostic for smaller cysts), CT, MRI/MRCP, ERCP, and PTC. **MRCP has replaced the more invasive ERCP/PTC as the gold standard**: *"MRCP has replaced the more invasive techniques as the gold standard of diagnosis. In addition, MRCP is helpful in detecting an abnormal pancreaticobiliary junction, which is seen in the majority of choledochal cysts"* [PMID: 25682292]. In a giant-cyst series, US/CT were misleading but *"Magnetic resonance cholangiopancreatography correctly achieved the diagnosis in all"* [PMID: 23686589].

**Diagnostic criteria for PBM (Japanese guidelines):** an abnormally long common channel (**≥6 mm**) and/or an abnormal pancreaticobiliary junction outside the duodenal wall on direct cholangiography, MRCP, EUS, or MDCT; an **elevated biliary amylase** supports pancreatobiliary reflux [PMID: 25404143; PMID: 22722902]. Supportive labs show an obstructive/cholestatic pattern (↑ bilirubin, ALP, GGT; LOINC-codable liver panel). There is **no genetic or newborn-screening test** because the disorder is non-Mendelian; CA19-9 serves as a follow-up tumor marker rather than a diagnostic test.

**Key differential diagnoses:** Cystic biliary atresia (CBA) — *"a rare variant of biliary atresia that closely resembles choledochal cyst... complicating diagnosis and potentially delaying critical surgical intervention"* [PMID: 42110123] — plus hepatic cyst, mesenchymal hamartoma, hepatic hemangioma, duplication cyst, and ovarian cyst on prenatal imaging [PMID: 41553982; PMID: 41569008].

### 10. Treatment — Complete Excision + Roux-en-Y Hepaticojejunostomy (F003, F008, F013)

The definitive treatment is **complete excision of the extrahepatic bile duct/cyst plus cholecystectomy and biliary-enteric reconstruction, preferentially Roux-en-Y hepaticojejunostomy** (NCIT: Hepaticojejunostomy; NCIT: Cholecystectomy). Hepaticoduodenostomy carries higher biliary-reflux morbidity. *"Roux-en-Y hepaticojejunostomy should remain the preferred reconstructive option in most children undergoing excision of choledochal malformations"* [PMID: 41927966].

Risk-stratified prophylactic surgery per Japanese guidelines: PBM **with** dilatation → prophylactic flow-diversion (extrahepatic bile duct + gallbladder excision); PBM **without** dilatation → prophylactic cholecystectomy without duct resection: *"in the former group, a prophylactic excision of the common bile duct and gallbladder should be recommended, while in the later group, a prophylactic cholecystectomy without bile duct resection may be the appropriate surgical procedure"* [PMID: 18274840].

**Minimally invasive approaches now predominate.** A meta-analysis of 19 pediatric studies found robotic surgery (RS) superior to laparoscopic surgery (LS):

| Outcome | Robotic vs Laparoscopic (OR, 95% CI) |
|---|---|
| Postoperative biliary stones | 0.10 (0.01–0.89) |
| Bile leakage | 0.28 (0.11–0.70) |
| Anastomotic stricture | 0.27 (0.12–0.65) |
| Overall complications | 0.26 (0.13–0.51) |

*"the RS group had significantly lower incidences of postoperative biliary stones (OR = 0.10...), bile leakage (OR = 0.28...), anastomotic stricture (OR = 0.27...), and overall complications (OR = 0.26...) compared to the LS group"* [PMID: 42130797]. A 201-patient study confirmed lower blood loss, faster oral intake, and shorter hospital stay with RS (all p<0.05) [PMID: 40889549]; a propensity-matched cohort (n=604) confirmed lower anastomotic stricture with RS (1.32%) [PMID: 41104222]. **Chemoprevention (COX-2 inhibitors, vitamin K2) is experimental only** — validated in animal models but not clinical. There is no role for pharmacotherapy, gene therapy, cell therapy, or immunotherapy in the primary disease (aside from oncologic treatment once cancer develops).

### 11. Outcome / Prognosis — Excellent After Excision but Lifelong Residual Cancer Risk (F004, F007, F019)

With complete excision, overall prognosis is generally excellent with low perioperative mortality (5-year overall survival ~95.5% in a 394-patient series [PMID: 25923827]). However, a **residual lifelong cancer risk persists in retained duct segments** — estimated up to ~4% after operation, with pre-operative adult malignancy risk of 6–30% [PMID: 29258149]. A 94-patient cohort quantified the time-dependence:

| Time after excision | Cumulative biliary-cancer incidence |
|---|---|
| 15 years | 1.6% |
| 20 years | 3.9% |
| 25 years | 11.3% |

*"The risk of biliary malignancy in the remnant bile duct increases more than 15 years after cyst excision"* [PMID: 22989043]. Once malignancy develops, prognosis is dismal: *"The overall cumulative survival rates... were 50% at 2 years and 25% at 3 years, with a median survival time of 15 months"* [PMID: 22989043]. Cancer can appear even ~36 years after resection [PMID: 39845966], and regular follow-up has not clearly improved resectability [PMID: 27307284].

**Type I and IV cysts show higher cancer incidence even after excision** [PMID: 17187167]. **Caroli disease/syndrome (Type V)** carries the worst prognosis: in a longitudinal cohort, *"All cases of esophageal varices, hepatic decompensation, cholangiocarcinoma (n=3), and death (n=3) occurred exclusively in the CS [Caroli syndrome] group"* [PMID: 41888235]; cholangiocarcinoma in ~5–19%, and 5-year survival after liver resection ~88.5% but only ~33% at 1 year if cholangiocarcinoma is present [PMID: 24121258; PMID: 29929811]. Prognostic factors include patient age, Todani cyst type, histology, and localization [PMID: 29258149].

**Late complications after excision:** anastomotic stricture/stenosis (diameter <3 mm), intrahepatic duct stones (esp. Todani IVa), remnant intrapancreatic stones, cholangitis, and secondary biliary cirrhosis. Late complications occur in ~36% (8/22) of long-followed pediatric patients at median 12 years [PMID: 41638356].

### 12. Prevention (F008, F020)

Prevention is dominated by surgical and surveillance strategies:

- **Primary/secondary (cancer prevention):** Prophylactic complete excision + cholecystectomy + Roux-en-Y hepaticojejunostomy at diagnosis, removing the reflux-injured premalignant epithelium; for PBM without dilatation, prophylactic cholecystectomy [PMID: 23798483; PMID: 19896105].
- **Surgical refinement:** A Carrel-patch hepaticojejunostomy widening the anastomosis to 10–13 mm reduced stenosis and intrahepatic stones and *"appears to be oncologically safe because of the absence of malignant transformation for at least 20 years"* [PMID: 36574035]. Obsolete internal-drainage procedures (cystenterostomy) leave the cyst in situ and carry high later cancer risk.
- **Tertiary (surveillance):** Lifelong follow-up. *"A postoperative follow-up concept that consists of annual controls of CA19-9 and abdominal ultrasound is introduced"* [PMID: 29258149].
- **Chemoprevention (experimental):** In animal PBM models, COX-2 inhibitors (meloxicam) and vitamin K2 suppress carcinogenesis — not yet clinical [PMID: 15944215; PMID: 21661384].
- **Not applicable:** No vaccine, no genetic/carrier screening, no population newborn screening (sporadic/non-Mendelian); genetic counseling is generally not indicated beyond noting rare familial clustering.

### 13. Other Species / Natural Disease and Model Organisms (F005, F009, F018)

**Natural disease in other species.** Naturally occurring choledochal cysts are documented in **domestic shorthair cats (NCBI Taxon 9685)**: *"Histologically, the cyst wall was expanded by fibroblasts, collagen, and lymphoplasmacytic inflammation"*, with secondary neutrophilic cholangitis, choledochitis, duodenal papillitis, and pancreatitis [PMID: 34027760]. This documents cross-species (comparative) pathology; there is no established zoonotic transmission.

**Model organisms.**

| Model | Species | Method | Recapitulates | Source |
|---|---|---|---|---|
| Surgical APBDU | Dog (mongrel puppy) | Pancreatic-to-bile-duct anastomosis | Progressive dilatation, wall thickening, epithelial hyperplasia | [PMID: 17021737; PMID: 9434012] |
| Surgical APBDU | Minipig | Gallbladder–pancreatoduodenal anastomosis | Intestinal metaplasia (20%), no dilatation | [PMID: 8986984] |
| DBTC chemical | Rat (Lewis) | Single IV dibutyltin dichloride 8 mg/kg | Ductal dilatation, papillary proliferation; HDAC1 early driver | [PMID: 26176076] |
| Surgical PBM + carcinogen | Syrian hamster | CBD ligation + cholecystoduodenostomy + BOP | Atypical epithelium 73–75%, carcinoma 25–36% | [PMID: 21661384; PMID: 15944215] |
| PCK rat | Rat (PKHD1-mutant) | Spontaneous ARPKD mutant | Type V/Caroli: ductal plate malformation, saccular dilatation | [PMID: 11337358; PMID: 20017109] |

The DBTC rat model showed *"the bile duct had been gradually dilated on day 3... the biliary epithelium... was papillary proliferated on day 7... HDAC1 expression increased at the early postoperative period prior to other oncogene"* [PMID: 26176076], implicating **HDAC1 as an upstream driver acting via COX-2**. Chemoprevention is demonstrable: the COX-2 inhibitor meloxicam reduced atypical epithelium from 72.7% to 27.3% with no cancer (PCNA index p=0.045) [PMID: 15944215], and vitamin K2 (menaquinone-4) *"suppressed biliary carcinogenesis by the induction of cell cycle arrest"* [PMID: 21661384]. The PCK rat is the definitive Caroli model — an *"autosomal recessive"* PKHD1/fibrocystin-deficient mutant [PMID: 11337358] showing plasmin/tPA-mediated basement-membrane (laminin, type IV collagen) degradation [PMID: 19025978]. **Model limitations:** surgical APBDU models capture reflux-driven dilatation but not the full decades-long human carcinogenesis timeline; the PCK rat models only Type V (Caroli), not the reflux-driven Types I–IV.

---

## Mechanistic Model / Interpretation

The unifying insight from this investigation is that **a single congenital anatomic lesion (pancreaticobiliary maljunction) drives two clinically distinct outcomes through one shared intermediate (chronic reflux-mediated epithelial injury)**:

```
              CONGENITAL PBM (long common channel >=6 mm)
                            |
              pancreatic-duct pressure > bile-duct pressure
                            |
                  PANCREATOBILIARY REFLUX
             (activated enzymes + bile stasis + high bile acids)
                            |
              CHRONIC BILIARY EPITHELIAL INJURY-REPAIR
                     /                      \
      MECHANICAL branch              MOLECULAR branch
   increased intraductal pressure   hyperplasia (early KRAS/COX-2/
   + protein plugs/stones            HDAC1/AID/IL-33)
          |                              |
   CYSTIC DILATATION            dysplasia -> carcinoma
   (the choledochal cyst)       (late stepwise TP53 10% -> 75%)
          |                              |
   presents as triad,           CHOLANGIOCARCINOMA /
   cholangitis, pancreatitis    GALLBLADDER CARCINOMA
                                (20-30x; mean age ~32 y)
```

This model explains several otherwise puzzling clinical facts. First, why **surgical flow-diversion (excision + Roux-en-Y)** is curative for the cyst yet incompletely protective against cancer: excision removes the bulk of injured epithelium and stops reflux, but any retained duct remnant that has already accumulated somatic mutations (a "field defect") can still progress — hence the late-rising residual risk beyond 15 years. Second, why **cancer risk is age-dependent**: the molecular hits accumulate stepwise over decades (TP53 rising 10%→75% across the field), so childhood risk is <1% but adult risk reaches 10–30%. Third, why **PBM without dilatation still warrants prophylactic cholecystectomy**: the carcinogenic reflux acts on the gallbladder regardless of whether the duct dilates (gallbladder cancer reaches 36–88% in PBM without dilatation). The mechanistic chain from PBM through reflux to the hyperplasia–dysplasia–carcinoma sequence is well demonstrated in human tissue and validated in surgical and chemical animal models; the specific ordering (KRAS early, TP53 late, HDAC1 upstream) is supported but based on cross-sectional tissue-field comparisons rather than longitudinal lineage tracing.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [PMID: 19896105](https://pubmed.ncbi.nlm.nih.gov/19896105/) | Pancreaticobiliary maljunction | Pressure-driven reflux initiates carcinogenesis |
| [PMID: 17187167](https://pubmed.ncbi.nlm.nih.gov/17187167/) | Bile duct cyst as precursor to biliary cancer | Hyperplasia–dysplasia–carcinoma sequence; early/late molecular ordering; age-dependent risk |
| [PMID: 34798839](https://pubmed.ncbi.nlm.nih.gov/34798839/) | Stepwise TP53 mutations in PBM→GBC | TP53 10%→75% field-to-tumor; TP53 > KRAS |
| [PMID: 30882917](https://pubmed.ncbi.nlm.nih.gov/30882917/) | IL-33 overexpression in PBM gallbladder cancers | KRAS not PBM-specific; IL-33 inflammatory driver |
| [PMID: 34132887](https://pubmed.ncbi.nlm.nih.gov/34132887/) | Carcinogenesis via epigenetic/genetic regulation | HDAC/AID + KRAS/p53 elevated even in children |
| [PMID: 18500533](https://pubmed.ncbi.nlm.nih.gov/18500533/) | PBM and carcinogenesis | Multistep injury-repair chain; cancer incidence in PBM |
| [PMID: 25682292](https://pubmed.ncbi.nlm.nih.gov/25682292/) | Imaging of choledochal cysts | MRCP gold standard; detects maljunction |
| [PMID: 28364277](https://pubmed.ncbi.nlm.nih.gov/28364277/) | Pediatric choledochal cysts: management | Todani classification; Types I/IV highest risk |
| [PMID: 42130797](https://pubmed.ncbi.nlm.nih.gov/42130797/) | Robotic vs laparoscopic meta-analysis | RS reduces complications |
| [PMID: 41927966](https://pubmed.ncbi.nlm.nih.gov/41927966/) | Biliary reconstruction in children | Roux-en-Y preferred |
| [PMID: 22989043](https://pubmed.ncbi.nlm.nih.gov/22989043/) | Subsequent biliary malignancy after excision | Residual cancer risk 1.6%→11.3%; poor survival |
| [PMID: 29258149](https://pubmed.ncbi.nlm.nih.gov/29258149/) | Choledochal cyst and malignancy | Lifelong CA19-9 + US surveillance; 6–30% adult risk |
| [PMID: 25123318](https://pubmed.ncbi.nlm.nih.gov/25123318/) | Increasing occurrence in Finland | Western incidence; cystic vs fusiform onset |
| [PMID: 40570483](https://pubmed.ncbi.nlm.nih.gov/40570483/) | Large CBD cyst case report | Asian incidence ~1:1000; ~7.5% malignancy |
| [PMID: 7979612](https://pubmed.ncbi.nlm.nih.gov/7979612/) | Changing pattern of presentation | Age-dependent triad; adult pain/pancreatitis |
| [PMID: 19701664](https://pubmed.ncbi.nlm.nih.gov/19701664/) | Children vs adults, Kashmir | M:F ratios; triad 6.7× more common in children |
| [PMID: 35741793](https://pubmed.ncbi.nlm.nih.gov/35741793/) | Pathogenesis: genomics/transcriptomics | Two theories; non-Mendelian |
| [PMID: 25588714](https://pubmed.ncbi.nlm.nih.gov/25588714/) | Adult CC: pathogenesis/imaging | Reflux vs antenatal-obstruction theories |
| [PMID: 25404143](https://pubmed.ncbi.nlm.nih.gov/25404143/) | PBM and biliary cancer (nationwide) | Cancer 21.6% (with dilatation), 42.4% (without) |
| [PMID: 18274840](https://pubmed.ncbi.nlm.nih.gov/18274840/) | Prophylactic surgery for biliary cancer risk | Risk-stratified prophylactic surgery |
| [PMID: 26176076](https://pubmed.ncbi.nlm.nih.gov/26176076/) | DBTC rat model, HDAC | Rodent cyst model; HDAC1 early driver |
| [PMID: 15944215](https://pubmed.ncbi.nlm.nih.gov/15944215/) | Meloxicam chemoprevention (hamster) | COX-2 inhibition prevents carcinogenesis |
| [PMID: 21661384](https://pubmed.ncbi.nlm.nih.gov/21661384/) | Vitamin K2 chemoprevention (hamster) | Cell-cycle-arrest chemoprevention |
| [PMID: 11337358](https://pubmed.ncbi.nlm.nih.gov/11337358/) | PCK rat / Caroli | Type V animal model (PKHD1) |
| [PMID: 34027760](https://pubmed.ncbi.nlm.nih.gov/34027760/) | Feline choledochal cyst | Natural disease in cats |
| [PMID: 41888235](https://pubmed.ncbi.nlm.nih.gov/41888235/) | Caroli disease vs syndrome cohort | Worse outcomes in Caroli syndrome |
| [PMID: 42110123](https://pubmed.ncbi.nlm.nih.gov/42110123/) | Cystic biliary atresia | Key differential diagnosis |
| [PMID: 24604978](https://pubmed.ncbi.nlm.nih.gov/24604978/) | Intracystic pressure correlations | Cyst-wall histopathology; pressure–damage link |

**Convergent vs challenging evidence.** The reflux/PBM etiology is strongly convergent across human tissue studies, guidelines, and multiple animal models. The main *challenge* to a simple monocausal model comes from the persistence of the "congenital obstruction" theory [PMID: 25588714] and the observation that not all CC (e.g., some Type V/Caroli, which is a ductal-plate/ARPKD disorder) involve PBM at all — indicating **etiologic heterogeneity across Todani subtypes**. A single intracholecystic-papillary-neoplasm case report found neither KRAS nor p53 alteration despite PBM [PMID: 33168026], reminding us that not every PBM-associated tumor follows the canonical pathway.

---

## Limitations and Knowledge Gaps

1. **Non-Mendelian, poorly characterized genetics.** No germline causal gene is established for classic (Types I–IV) CC. The genomics/transcriptomics literature is nascent, and candidate susceptibility loci or modifier genes remain undefined [PMID: 35741793]. The molecular explanation for the female and Asian predominance is unknown.
2. **Cross-sectional molecular ordering.** The KRAS-early/TP53-late sequence and the HDAC1-upstream hypothesis rest on cross-sectional tissue-field comparisons and animal models, not longitudinal human lineage tracing.
3. **Etiologic heterogeneity.** The two-theory debate (reflux vs congenital obstruction) is unresolved; different Todani subtypes likely have distinct mechanisms, and Type V (Caroli) is mechanistically separate (ductal-plate malformation/PKHD1).
4. **Surveillance efficacy uncertain.** Regular post-excision follow-up has not been clearly shown to improve resectability or survival of remnant-duct cancer [PMID: 27307284]; optimal surveillance intervals and modalities are unvalidated.
5. **No clinical chemoprevention.** COX-2 inhibitors and vitamin K2 are validated only in animals; human chemoprevention trials are absent.
6. **Western data are sparse** relative to Asian series; incidence and outcome estimates may not transfer across populations.

---

## Proposed Follow-up Experiments / Actions

1. **Longitudinal molecular field mapping.** Use spatial transcriptomics/multi-region sequencing on excised cyst walls to directly test the proposed KRAS-early → TP53-late → HDAC1-upstream causal ordering and identify a molecular signature predicting remnant-duct cancer risk.
2. **Germline discovery.** Conduct whole-genome/exome sequencing on familial and syndromic CC cohorts (and trio designs) to search for susceptibility variants explaining the female and Asian predominance.
3. **Prospective surveillance trial.** Design a registry-based study testing whether a defined CA19-9 + MRCP surveillance schedule improves early detection and survival of post-excision remnant cancers.
4. **Chemoprevention translation.** Given robust animal data, evaluate COX-2 inhibitors or vitamin K2 in high-risk patients who cannot undergo complete duct clearance (e.g., intrahepatic remnants).
5. **Robotic vs laparoscopic long-term RCT.** Extend current short-term comparative data with a prospective trial powered for long-term anastomotic stricture, intrahepatic stones, and cancer.
6. **Biomarker development for cystic biliary atresia differentiation.** Develop a prenatal/neonatal imaging + biomarker algorithm to reliably distinguish CBA (needs urgent Kasai) from CC.

---

*Report compiled from a 10-iteration autonomous investigation: 20 confirmed findings, 5 supported hypotheses, 87 papers reviewed.*


## Artifacts

- [OpenScientist final report](Bile_Duct_Cyst-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bile_Duct_Cyst-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:28364277
2. PMID:34377608
3. PMID:35741793
4. PMID:25588714
5. PMID:25123318
6. PMID:41368339
7. PMID:40570483
8. PMID:19701664
9. PMID:31341359
10. PMID:7979612
11. PMID:14768318
12. PMID:23686589
13. PMID:38582706
14. PMID:19896105
15. PMID:17187167
16. PMID:34798839
17. PMID:30882917
18. PMID:34132887
19. PMID:24895231
20. PMID:14534681
21. PMID:24604978
22. PMID:40097690
23. PMID:22989043
24. PMID:25682292
25. PMID:25404143
26. PMID:22722902
27. PMID:42110123
28. PMID:41553982
29. PMID:41569008
30. PMID:41927966
31. PMID:18274840
32. PMID:42130797
33. PMID:40889549
34. PMID:41104222
35. PMID:25923827
36. PMID:29258149
37. PMID:39845966
38. PMID:27307284
39. PMID:41888235
40. PMID:24121258
41. PMID:29929811
42. PMID:41638356
43. PMID:23798483
44. PMID:36574035
45. PMID:15944215
46. PMID:21661384
47. PMID:34027760
48. PMID:17021737
49. PMID:9434012
50. PMID:8986984
51. PMID:26176076
52. PMID:11337358
53. PMID:20017109
54. PMID:19025978
55. PMID:18500533
56. PMID:33168026