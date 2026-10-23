---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-11T21:40:10.946582'
end_time: '2026-09-11T22:31:44.245400'
duration_seconds: 3093.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 70
  mondo_id: MONDO:0033542
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
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_70-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_70-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 70
- **MONDO ID:** MONDO:0033542 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 70** covering all of the
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

# Immunodeficiency 70 (IMD70): A Comprehensive Disease Characteristics Report

**Disease:** Immunodeficiency 70 (IMD70)
**Primary identifiers:** OMIM #618969 · MONDO:0033542 · DOID:0112005 · UMLS C5436501 · MedGen 1740270
**Causal gene:** *IVNS1ABP* (KLHL39 / NS1-BP), chromosome 1q25.3, HGNC:16951
**Category:** Mendelian, autosomal dominant (haploinsufficiency)

---

## Summary

Immunodeficiency 70 (IMD70) is an **ultra-rare, autosomal-dominant inborn error of immunity** caused by **heterozygous loss-of-function (haploinsufficiency) of *IVNS1ABP***, a gene at chromosome 1q25.3 that encodes a BTB-BACK-Kelch protein (also called KLHL39 or NS1-BP). The disorder was first defined by Thaventhiran and colleagues in 2020 within the NIHR BioResource whole-genome sequencing primary-immunodeficiency cohort ([PMID: 32499645](https://pubmed.ncbi.nlm.nih.gov/32499645/)), in **three unrelated probands** carrying loss-of-function alleles. It is catalogued in OMIM as #618969 and mapped to MONDO:0033542. No dedicated Orphanet, ICD-10/ICD-11, or MeSH entry exists for IMD70 as a distinct entity; clinically it falls within the common variable immunodeficiency (CVID) / combined immunodeficiency spectrum.

Clinically, IMD70 presents as a **combined immunodeficiency with immune dysregulation**. The hallmark features are **cutaneous HPV-driven warts** (verrucae, palmar and plantar warts), **recurrent bacterial sinopulmonary infections** and furuncles, **hypogammaglobulinemia**, and reduced circulating **CD4⁺ T cells and CD19⁺ B cells**. Superimposed autoinflammatory/autoimmune manifestations include colitis, celiac disease, achalasia and retinal vasculitis. Inheritance is autosomal dominant with **incomplete penetrance and variable expressivity** — a transmitting mother in the original cohort carried the mutation without an infection history yet still displayed a subclinical immunophenotype (reduced CD4⁺ T and CD19⁺ B cells).

Mechanistically, *IVNS1ABP* is a multifunctional protein that **stabilizes the F-actin cytoskeleton** through its Kelch repeats, acts as a **CUL3 E3-ubiquitin-ligase substrate adaptor**, and participates in **pre-mRNA splicing and nuclear mRNA export**. The gene is extremely intolerant to loss-of-function (gnomAD pLI ≈ 1.0), so a single inactivating allele reduces functional protein by roughly half and produces disease through haploinsufficiency. Diagnosis is essentially genomic (WGS/WES or a broad inborn-errors-of-immunity panel), and management is standard-of-care primary immunodeficiency support (immunoglobulin replacement, antimicrobial prophylaxis, dermatologic HPV treatment, immunomodulation, and consideration of HSCT in severe cases). No disease-specific therapy or clinical trial exists.

---

## 1. Disease Information

IMD70 is a Mendelian inborn error of immunity — a primary immunodeficiency with prominent immune dysregulation. It corresponds to **OMIM #618969**, **MONDO:0033542**, **DOID:0112005**, **UMLS C5436501** and **MedGen 1740270**. The causal gene was resolved through NCBI elink (OMIM 618969 → Gene ID 10625) as ***IVNS1ABP*** — Influenza Virus NS1A-Binding Protein — located at chromosome **1q25.3**. Gene synonyms/aliases include **KLHL39, NS1-BP, NS1BP, ARA3, FLARA3, HSPC068, ND1**, and — tellingly — **"IMD70"** itself. The NCBI RefSeq gene summary explicitly states the gene is "Implicated in immunodeficiency 70."

There is **no distinct Orphanet, ICD-10/ICD-11 or MeSH identifier** for IMD70; MONDO cross-references list only OMIM:618969, DOID:0112005, UMLS:C5436501 and MedGen:1740270. Clinically the entity is coded under the CVID / combined-immunodeficiency umbrella (ICD-10 D83/D81; ICD-11 4A00.x).

**Source of information:** the disease-level knowledge is derived from an **aggregated disease-level cohort** rather than individual EHR — specifically the whole-genome sequencing PID cohort of Thaventhiran et al., which is the source of all HPO annotations for OMIM:618969.

> *"Primary immunodeficiency (PID) is characterized by recurrent and often life-threatening infections, autoimmunity and cancer, and it poses major diagnostic and therapeutic challenges."* — [PMID: 32499645](https://pubmed.ncbi.nlm.nih.gov/32499645/)

**Suggested ontology term:** MONDO:0033542.

---

## 2. Etiology

**Disease causal factor:** IMD70 is **monogenic and genetic** — heterozygous loss-of-function of *IVNS1ABP* acting through **haploinsufficiency**. There is no infectious or environmental cause of the disorder itself (though HPV and other infections are downstream clinical consequences).

**Genetic risk factors:** The causal variants are germline heterozygous LoF alleles in *IVNS1ABP* (see Section 4). Because the gene is extremely LoF-constrained (gnomAD pLI ≈ 0.9997), essentially any inactivating allele is a strong candidate driver. No separate susceptibility loci or modifier genes have been established for IMD70.

**Environmental risk factors / protective factors / gene–environment interactions:** **Not established.** No environmental risk factors, protective alleles, protective exposures, or documented gene–environment interactions specific to IMD70 have been reported — consistent with a highly penetrant (though incompletely penetrant) monogenic disorder defined in only three families. This is a genuine knowledge gap rather than a negative finding.

---

## 3. Phenotypes

The HPO annotation set for OMIM:618969 comprises **18 terms**, all derived from the founding cohort (~4 patients). They cluster into four coherent domains. Onset in the described probands was **adult** (ages 19–56 at report), though a childhood contribution cannot be excluded given warts.

| Phenotype (type) | HPO term | Frequency in cohort | Notes |
|---|---|---|---|
| Verrucae — cutaneous sign | HP:0200043 | Characteristic | HPV-driven |
| Palmar warts — cutaneous sign | HP:0033004 | Characteristic | HPV-driven |
| Plantar warts — cutaneous sign | HP:0033005 | Characteristic | HPV-driven |
| Recurrent sinusitis — clinical | HP:0011108 | Characteristic | Bacterial |
| Furuncle — cutaneous sign | HP:0020083 | Variable | Bacterial |
| Immunodeficiency — clinical | HP:0002721 | Characteristic | Combined |
| Colitis — clinical | HP:0002583 | Variable | Immune dysregulation |
| Celiac disease — clinical | HP:0002608 | Variable | Autoimmune |
| Achalasia — clinical | HP:0002571 | Variable | Autoimmune/dysmotility |
| Retinal vasculitis — clinical | HP:0025188 | Variable | Autoimmune |
| ↓CD4⁺ T-cell proportion — lab | HP:0032218 | 1/4 | Immunophenotype |
| ↓Total B-cell count — lab | HP:0010976 | 1/4 | Immunophenotype |
| ↓Circulating IgA — lab | HP:0003460 | 1/3 | Hypogammaglobulinemia |
| ↓Circulating IgM — lab | HP:0002850 | 1/3 | Hypogammaglobulinemia |
| ↓Total IgG — lab | HP:0032132 | 1/3 | Hypogammaglobulinemia |
| ↓Circulating immunoglobulin — lab | HP:0004313 | — | Hypogammaglobulinemia |
| Chronic fatigue — constitutional | HP:0012432 | Variable | — |
| Autosomal dominant inheritance | HP:0000006 | — | Mode |

**Severity/progression:** variable and chronic; the immunodeficiency is lifelong. **Quality-of-life impact:** not formally measured with EQ-5D/SF-36/PROMIS instruments for IMD70; qualitatively, recurrent infections, persistent warts, chronic fatigue and gastrointestinal/ocular autoimmune complications would be expected to impair daily functioning.

> *"about 25% of patients have autoimmune disease, allergy is prevalent and up to 10% develop lymphoid malignancies"* — [PMID: 32499645](https://pubmed.ncbi.nlm.nih.gov/32499645/)

This documents the immune-dysregulation and malignancy susceptibility of the broader PID cohort in which IMD70 was described, consistent with the colitis, celiac disease and retinal vasculitis annotated to IMD70.

---

## 4. Genetic / Molecular Information

**Causal gene:** *IVNS1ABP* (Gene ID 10625; HGNC:16951; OMIM gene 609209), chromosome 1q25.3, reference transcript **NM_006469.5**, protein UniProt **Q9Y6Y0**.

**gnomAD constraint** (ENSG00000116679; GRCh38 chr1:185,296,388–185,317,273):

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 0.9997 | Near-certain haploinsufficient |
| LOEUF (oe_lof upper) | 0.442 | Strong LoF constraint |
| Observed/Expected LoF | 0.317 (25 obs / 78.9 exp) | ~68% depletion of LoF variants |
| LoF Z | 5.15 | Highly significant constraint |
| Missense Z | 4.23 | Missense-constrained |

**Pathogenic variants** — ClinVar lists **three Pathogenic variants** classified to IMD70, all loss-of-function, all germline:

| Variant (cDNA) | Protein | Type | Consequence |
|---|---|---|---|
| c.1899G>A | p.Trp633Ter | Nonsense | Loss of function |
| c.1072C>T | p.Arg358Ter | Nonsense | Loss of function |
| NC_000001.10:g.185276239_185287961del (~11.7 kb) | — | Intragenic/partial-gene deletion | Loss of function |

No "likely pathogenic" entries exist. IMD70-linked missense alleles (p.Arg204Cys, p.Gln504Pro, p.Asp580Ala, p.Val529Gly) remain **VUS** per ACMG/AMP; p.Cys508Gly is likely benign. Allele frequencies of the pathogenic variants are effectively absent from population databases (consistent with the LoF depletion above). **Functional consequence: loss of function / haploinsufficiency** (~50% reduction in functional protein).

**Modifier genes / epigenetic information / chromosomal abnormalities:** No IMD70-specific modifier genes or epigenetic mechanisms are established. Of interest, *IVNS1ABP* protein levels are indirectly regulated epigenetically in other contexts — in liver cancer, promoter hypermethylation-driven silencing of the RNA methyltransferase NSUN7 destabilizes the CCDC9B transcript and reduces IVNS1ABP protein ([PMID: 37173708](https://pubmed.ncbi.nlm.nih.gov/37173708/)) — but this is not shown to operate in IMD70. No recurrent chromosomal abnormality beyond the intragenic partial-gene deletion is reported.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious **causes** of IMD70 have been identified — the disorder is monogenic. Infectious agents are relevant only as **downstream opportunistic consequences**: cutaneous **human papillomavirus (HPV)** driving warts, pyogenic bacteria causing recurrent sinusitis/pneumonia/furuncles, and (in the broader PID context) EBV-associated disease. There are no reported toxin, radiation, occupational, dietary, smoking, or alcohol associations specific to IMD70.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (D = demonstrated, I = inferred)

```
(1) Heterozygous LoF IVNS1ABP variant
    (p.Trp633Ter | p.Arg358Ter | ~11.7 kb partial deletion)
              │  [D: LoF alleles + gnomAD pLI 0.9997]
              ▼
(2) ~50% loss of functional NS1-BP  →  HAPLOINSUFFICIENCY
              │
      ┌───────┴──────────────────────────────┐
      ▼                                        ▼
(3a) Impaired F-actin stabilization      (3b) Disturbed CUL3 ubiquitin-ligase
     via Kelch repeats;                        adaptor activity + pre-mRNA
     dysregulated actin dynamics               alternative splicing / mRNA export
     [D macrophages PMID:32943673;             [D biochemically; disease-link I]
      fibroblasts/iPSC/NPC PMID:41857046;
      I in lymphocytes]
      └───────┬──────────────────────────────┘
              ▼
   ┌──────────┼───────────────────────────┐
   ▼          ▼                            ▼
(4) BRANCH A            (5) BRANCH B                 (6) BRANCH C
 Impaired immune-cell    Defective antiviral          Loss of immune tolerance
 homeostasis →           control (GO:0009615) →        (?via altered AHR/Th17) →
 ↓CD4+ T, ↓CD19+ B →      HPV-driven cutaneous          autoinflammation:
 ↓immunoglobulin →        warts; EBV glandular          colitis, celiac disease,
 hypogammaglobulinemia →  disease                       achalasia, retinal vasculitis
 recurrent bacterial     [phenotype D;                  [phenotype D;
 sinusitis/pneumonia/     mechanism I]                   mechanism I]
 furuncles [D]
              │
              ▼
(7) Chronic immune dysregulation → increased malignancy/
    lymphoproliferation risk [I, general PID]
```

**Interpretation.** One inactivated *IVNS1ABP* allele reduces functional NS1-BP by ~50%. Because the gene is exquisitely dosage-sensitive (pLI ≈ 1.0), this haploinsufficiency simultaneously perturbs three cellular systems that immune cells depend on for development, migration, antigen handling and antiviral defense:

- **Molecular pathways / cellular processes:** F-actin cytoskeleton organization (GO:0007015), the CUL3-RING ubiquitin-ligase pathway (GO:0031463), RNA splicing (GO:0008380) and nuclear mRNA export, plus modulation of the aryl-hydrocarbon-receptor (AHR) pathway and ERK signalling. NS1-BP is a Kelch-family stabilizer of F-actin that "protects against actin derangement."
- **Protein dysfunction:** Truncating alleles/partial deletion abolish protein output from one allele; the retained protein is structurally normal but present at reduced dose (loss-of-function, not dominant-negative — although a dominant-negative contribution cannot be formally excluded).
- **Immune system involvement:** Combined immunodeficiency (reduced CD4⁺ T and CD19⁺ B cells, hypogammaglobulinemia) plus immune dysregulation/autoimmunity.
- **Antiviral defense:** Intrinsic "response to virus" role (GO:0009615) plausibly underlies the HPV-driven wart susceptibility.

> *"Influenza virus NS1A-binding protein (Ivns1abp) belongs to the Kelch family of proteins that play a central role in actin cytoskeleton dynamics by directly associating with F-actin and by protecting against actin derangement."* — [PMID: 32943673](https://pubmed.ncbi.nlm.nih.gov/32943673/)

> *"the cellular Non-Structural protein 1 (NS1)-binding protein (NS1-BP) interacts with the viral NS1 and M1 mRNA to promote M1 to M2 splicing"* — [PMID: 39384042](https://pubmed.ncbi.nlm.nih.gov/39384042/)

**Molecular profiling context.** Single-cell splicing-QTL analysis of PBMCs shows *IVNS1ABP* acts as a *trans*-regulator of splicing (distal effect on RPS24 splicing, interacting with the splicing factor HNRNPK), reinforcing that its dosage shapes immune-cell splicing programs ([PMID: 41672992](https://pubmed.ncbi.nlm.nih.gov/41672992/)).

**Upstream vs downstream.** Steps 1–3 are upstream molecular lesions; steps 4–7 are downstream clinical branches. The branches are not mutually exclusive — one patient can show infection susceptibility, warts and autoinflammation together because they share the same upstream defects.

**Cell types (CL):** CD4⁺ T cell (CL:0000624), B cell (CL:0000236), macrophage (CL:0000235), keratinocyte (CL:0000312).
**Biological processes (GO BP):** actin filament organization (GO:0007015), RNA splicing (GO:0008380), defense response to virus (GO:0051607), protein ubiquitination.

---

## 7. Anatomical Structures Affected

**Organ / system level:** immune system (primary); skin (warts, furuncles); upper and lower respiratory tract (sinuses, lungs); gastrointestinal tract (colon, esophagus, small bowel in celiac disease); eye (retina).

**Tissue / cell level:** lymphoid cells (CD4⁺ T cells, CD19⁺ B cells), macrophages, and epithelial keratinocytes are the key affected populations. Actin-dependent processes in these cells are central.

**Subcellular level (GO CC):** cytoskeleton (GO:0005856), Cul3-RING ligase complex (GO:0031463), spliceosomal complex (GO:0005681), nucleoplasm (GO:0005654), cytoplasm/cytosol.

**Localization (UBERON):** epidermis (UBERON:0001003), paranasal sinus (UBERON:0002100), lung (UBERON:0002048), colon (UBERON:0001155), esophagus (UBERON:0001043), retina (UBERON:0000966). Manifestations (e.g., warts, retinal vasculitis) are generally bilateral/multifocal rather than lateralized.

---

## 8. Temporal Development

**Onset:** In the defining cohort, probands presented in **adulthood** (ages 19–56 at report), consistent with the general PID observation that most patients present in adulthood without an apparent family history. Warts may begin earlier. Onset is **insidious/chronic** rather than acute.

**Progression:** chronic and lifelong, with a fluctuating course driven by recurrent infections and episodic autoinflammatory flares (colitis, retinal vasculitis). No defined staging system exists.

**Critical periods / remission:** No spontaneous remission is described; the underlying immunodeficiency is permanent. The relevant intervention window is essentially from diagnosis onward (immunoglobulin replacement, prophylaxis).

> *"Although the most severe forms of PID are identified in early childhood, most patients present in adulthood, typically with no apparent family history and a variable clinical phenotype of widespread immune dysregulation"* — [PMID: 32499645](https://pubmed.ncbi.nlm.nih.gov/32499645/)

---

## 9. Inheritance and Population

**Epidemiology:** **Ultra-rare** — defined in only **three unrelated probands** worldwide; prevalence unknown and unquantified (**< 1 per 1,000,000**). No incidence, sex-ratio or geographic-distribution data exist.

**Inheritance:** **Autosomal dominant** (HP:0000006) via haploinsufficiency.

**Penetrance/expressivity:** **Incomplete penetrance, variable expressivity.** The transmitting mother in kindred A carried the mutation and lacked an infection history yet still showed reduced CD4⁺ T and CD19⁺ B cells (subclinical immunophenotype).

**Other genetic-etiology parameters:** No genetic anticipation, germline mosaicism, founder effect, consanguinity association, or defined carrier frequency is established (unsurprising for a dominant disorder with only three families). No population enrichment is known.

---

## 10. Diagnostics

**Diagnostic approach: genomic.** IMD70 was discoverable only through unbiased genome-wide sequencing (it was found within a whole-genome sequencing PID cohort) and is diagnosed by identifying a heterozygous LoF *IVNS1ABP* variant via **WGS, WES, or a broad primary-immunodeficiency / inborn-errors-of-immunity gene panel** (reference transcript NM_006469.5; NIH GTR condition C5436501). Chromosomal microarray may detect the ~11.7 kb partial-gene deletion.

**Supportive laboratory work-up:** serum immunoglobulins (IgG/IgA/IgM — may show hypogammaglobulinemia, HP:0004313); lymphocyte immunophenotyping (reduced CD4⁺ T cells HP:0032218, reduced CD19⁺ B cells HP:0010976); vaccine-response/antibody-function testing; HPV/EBV assessment.

**Clinical criteria / differential diagnosis:** No standalone diagnostic criteria exist; IMD70 is diagnosed genotype-first within the CVID/CID framework. Differential diagnoses include CVID, combined immunodeficiency, WHIM syndrome (CXCR4), other "wart" PIDs (EVER1/2/TMC6-8 epidermodysplasia verruciformis, GATA2, DOCK8, WILD/CIB1), and actin-related PIDs (WAS, ARPC1B, DOCK8).

**Screening:** No newborn/carrier screening program exists; cascade genetic testing of relatives is appropriate once a familial variant is identified.

> *"The implementation of whole-genomic analyses in the routine diagnostics has led to a paradigm shift. Upfront genome-wide analysis by whole genome sequencing (WGS) will shorten the time to diagnosis…"* — [PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)

---

## 11. Outcome / Prognosis

No formal survival, mortality, or quality-of-life data specific to IMD70 exist given the tiny cohort. Prognosis is inferred from the CVID/combined-immunodeficiency framework: **chronic lifelong disease** with morbidity from recurrent infections, persistent HPV warts, autoinflammatory complications (colitis, retinal vasculitis, achalasia), and an elevated **long-term risk of lymphoproliferation/malignancy** typical of dysregulated PID. With immunoglobulin replacement and infection prophylaxis, life expectancy is likely substantially improved, though unquantified. Prognostic biomarkers specific to IMD70 have not been defined; degree of hypogammaglobulinemia and T/B-cell cytopenia are plausible severity indicators.

> *"about 25% of patients have autoimmune disease, allergy is prevalent and up to 10% develop lymphoid malignancies"* — [PMID: 32499645](https://pubmed.ncbi.nlm.nih.gov/32499645/)

---

## 12. Treatment

There is **no disease-specific therapy and no IMD70 clinical trial** (ClinicalTrials.gov). Management is **inferred standard-of-care PID care**:

| Intervention | Rationale | NCIT suggestion |
|---|---|---|
| Immunoglobulin replacement therapy | For hypogammaglobulinemia (HP:0004313) | Immunoglobulin Therapy |
| Antimicrobial prophylaxis | Recurrent bacterial infections | Antibiotic Therapy |
| Dermatologic/ablative HPV treatment + HPV vaccination | Cutaneous warts | Human Papillomavirus Vaccine |
| Immunomodulation | Autoinflammatory features (colitis, retinal vasculitis) | Immunomodulatory Therapy |
| Malignancy/lymphoproliferation surveillance | Elevated PID malignancy risk | — |
| Allogeneic HSCT (consideration) | Severe combined immune dysregulation | Hematopoietic Stem Cell Transplantation |

No approved **gene or cell therapy** exists. No pharmacogenomic guidance specific to IMD70 is established.

---

## 13. Prevention

There is no primary prevention for this monogenic disorder. Relevant measures are:

- **Secondary/tertiary prevention:** early genomic diagnosis, immunoglobulin replacement, infection prophylaxis, HPV vaccination, and surveillance for autoimmune complications and malignancy.
- **Genetic counseling:** autosomal-dominant recurrence risk (50% to offspring of an affected carrier), with counseling on **incomplete penetrance and variable expressivity**; cascade testing of at-risk relatives; options for prenatal/preimplantation genetic testing once a familial variant is confirmed.
- **Public-health/environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

*IVNS1ABP* is deeply conserved across mammals, with one-to-one orthologs in **mouse (*Ivns1abp*, NCBI GeneID 117198)** and **rat (*Ivns1abp*, GeneID 289089)**; the Kelch β-propeller is conserved broadly (orthologs and functional homologs extend to fish, where *ivns1abp* is studied as an egg-quality/ageing marker — [PMID: 41270604](https://pubmed.ncbi.nlm.nih.gov/41270604/)). **No naturally occurring animal disease (OMIA) corresponding to IMD70** and no zoonotic/cross-species transmission are applicable — the disorder is a germline human Mendelian condition.

---

## 15. Model Organisms

Disease-relevant experimental systems reported to date are **cellular/in vitro, not whole-animal IMD70 models**:

1. **Patient-derived fibroblasts, isogenic iPSCs, neural progenitor cells and cerebral organoids** carrying a homozygous *IVNS1ABP* mutation (progeroid-neuropathy context) show defective cytokinesis, increased DNA damage, premature cellular senescence and dysregulated actin polymerization ([PMID: 41857046](https://pubmed.ncbi.nlm.nih.gov/41857046/)).
2. **Macrophage models** showing *Ivns1abp* controls actin-dependent phagocytosis and a c-Myc–regulated reparative phenotype ([PMID: 32943673](https://pubmed.ncbi.nlm.nih.gov/32943673/)).
3. A **crystal structure** of the human Kelch domain (residues 330–642) solved at 1.98 Å as a six-bladed β-propeller ([PMID: 29497022](https://pubmed.ncbi.nlm.nih.gov/29497022/)).

> *"Exome sequencing revealed a homozygous mutation in the IVNS1ABP gene, which encodes IVNS1ABP, an influenza virus non-structural protein-1 binding protein."* — [PMID: 41857046](https://pubmed.ncbi.nlm.nih.gov/41857046/)

**No published *Ivns1abp*-knockout mouse specifically modeling the human immunodeficiency was identified**, and no natural animal model exists — a significant resource gap. Available models are best suited to studying the actin, cytokinesis, senescence and splicing arms of the mechanism rather than the intact immune phenotype.

---

## Mechanistic Model / Interpretation (Synthesis)

The unifying model is that **a single inactivating *IVNS1ABP* allele halves NS1-BP dosage in a gene that cannot tolerate loss-of-function**, and this dosage insufficiency degrades three cellular systems at once — the F-actin cytoskeleton, the CUL3-ubiquitin proteostasis machinery, and the mRNA-splicing/export program. Immune cells are unusually dependent on all three (for immune-synapse formation, migration, phagocytosis, antigen processing and antibody production), which is why the clinical picture is a **combined immunodeficiency with immune dysregulation** rather than an isolated defect. The three downstream branches (infection susceptibility, HPV-driven warts, autoinflammation) coexist because they emanate from the same upstream lesion.

The strongest mechanistic evidence is in the **actin arm** — NS1-BP is a Kelch-family F-actin stabilizer ([PMID: 32943673](https://pubmed.ncbi.nlm.nih.gov/32943673/)), and defects in other actin regulators (WASP, ARPC1B) are established causes of immunodeficiency ([PMID: 29127144](https://pubmed.ncbi.nlm.nih.gov/29127144/)). The **splicing/export arm** is well established biochemically ([PMID: 39384042](https://pubmed.ncbi.nlm.nih.gov/39384042/)), and immune-cell splicing-QTL data confirm *IVNS1ABP* dosage regulates splicing programs *in trans* ([PMID: 41672992](https://pubmed.ncbi.nlm.nih.gov/41672992/)). The connection from these molecular defects to the specific human lymphocyte phenotype remains **inferred rather than directly demonstrated in patient T/B cells**.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [32499645](https://pubmed.ncbi.nlm.nih.gov/32499645/) | *Whole-genome sequencing of a sporadic primary immunodeficiency cohort* | **Foundational.** Defines IMD70; source of all HPO annotations; establishes AD inheritance, adult presentation, variable dysregulation, malignancy risk |
| [32943673](https://pubmed.ncbi.nlm.nih.gov/32943673/) | *The influenza virus NS1A binding protein gene modulates macrophage response…* | NS1-BP as Kelch-family F-actin stabilizer; actin/phagocytosis mechanism |
| [39384042](https://pubmed.ncbi.nlm.nih.gov/39384042/) | *Cellular NS1-BP interacts with mRNA export receptor NXF1…* | Splicing (M1→M2) and NXF1-mediated mRNA-export functions |
| [41857046](https://pubmed.ncbi.nlm.nih.gov/41857046/) | *IVNS1ABP mutation drives cellular senescence in newly identified progeroid neuropathy* | Biallelic (recessive) phenotype; zygosity-dependent disease; senescence/DNA-damage cellular models |
| [29497022](https://pubmed.ncbi.nlm.nih.gov/29497022/) | *Crystal structure of the Kelch domain of human NS1-binding protein at 1.98 Å* | Protein architecture — six-bladed β-propeller Kelch domain |
| [41672992](https://pubmed.ncbi.nlm.nih.gov/41672992/) | *Single-cell resolution of splicing regulation in PBMCs…* | *IVNS1ABP* is a *trans*-sQTL regulator of splicing in immune cells (dosage sensitivity) |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | *Rapid identification of primary atopic disorders by upfront genomic sequencing* | Supports genome-first diagnostic paradigm for ultra-rare monogenic immune disease |
| [29127144](https://pubmed.ncbi.nlm.nih.gov/29127144/) | *Disruption of thrombocyte and T-lymphocyte development by ARPC1B mutation* | Comparator: actin-regulator (Arp2/3) deficiency causing PID; supports actin-immunodeficiency axis |
| [37173708](https://pubmed.ncbi.nlm.nih.gov/37173708/) | *Epigenetic inactivation of NSUN7… in liver cancer* | Shows IVNS1ABP protein can be indirectly downregulated via epigenetic/RNA-modification pathways (non-IMD70 context) |

Additional papers describe *IVNS1ABP* in cardiovascular/oncologic contexts ([PMID: 40782973](https://pubmed.ncbi.nlm.nih.gov/40782973/), [PMID: 41613752](https://pubmed.ncbi.nlm.nih.gov/41613752/), [PMID: 38956669](https://pubmed.ncbi.nlm.nih.gov/38956669/)) and non-mammalian biology ([PMID: 41270604](https://pubmed.ncbi.nlm.nih.gov/41270604/), [PMID: 39664389](https://pubmed.ncbi.nlm.nih.gov/39664389/)); they corroborate the gene's broad roles in actin dynamics, MYC regulation and cell-death/senescence programs but do not bear directly on IMD70 pathogenesis.

---

## Limitations and Knowledge Gaps

1. **Extremely small evidence base.** The disease definition rests on **three unrelated probands** from a single 2020 study; all HPO annotations trace to one publication. Prevalence, incidence, sex ratio, penetrance estimates and genotype-phenotype correlations are effectively unquantifiable.
2. **Mechanism inferred in lymphocytes.** NS1-BP's actin and splicing functions are demonstrated in macrophages, fibroblasts, iPSCs and biochemical systems — not in patient T or B cells. Branches A–C are inferred.
3. **No animal model of the immunodeficiency.** No *Ivns1abp* heterozygous/conditional-knockout mouse modeling IMD70 exists; no OMIA natural-disease counterpart.
4. **VUS burden.** Beyond three LoF alleles, IMD70-associated missense variants remain VUS, limiting diagnostic certainty for non-truncating variants.
5. **No IMD70-specific therapeutics or trials.** Management is extrapolated from general PID/CVID practice; no efficacy data specific to this disorder.
6. **Ontology/coding gaps.** No Orphanet, ICD-10/11, or MeSH identifier — a barrier to registry-based epidemiology.
7. **Zygosity-dependent phenotypes.** Biallelic *IVNS1ABP* loss causes a distinct progeroid neuropathy; the relationship (if any) to the heterozygous immunodeficiency spectrum is unexplored.

---

## Proposed Follow-up Experiments / Actions

1. **International case ascertainment** via GeneMatcher/matchmaker exchanges and inborn-errors-of-immunity consortia to refine penetrance, expressivity and the phenotypic spectrum.
2. **Patient-derived immune-cell functional studies** — profile CD4⁺ T, CD19⁺ B and keratinocyte lines for F-actin content, immune-synapse formation, migration, phagocytosis and antibody class-switching to test branches A and B directly.
3. **Isogenic haploinsufficiency models** — heterozygous *IVNS1ABP* iPSC lines differentiated to lymphoid/myeloid lineages and skin organoids to quantify dosage-dependent effects on actin, splicing and ubiquitination.
4. **Conditional mouse model** — lymphocyte-specific *Ivns1abp* heterozygous/knockout mouse to test whether haploinsufficiency recapitulates cytopenias, hypogammaglobulinemia and infection susceptibility.
5. **Single-cell RNA-seq of patient PBMCs** to map mis-splicing events (e.g., RPS24) driven by reduced *IVNS1ABP* dosage, building on [PMID: 41672992](https://pubmed.ncbi.nlm.nih.gov/41672992/).
6. **HPV/keratinocyte antiviral assays** to test whether NS1-BP–haploinsufficient keratinocytes have impaired intrinsic antiviral control explaining the wart phenotype.
7. **Registry and ontology curation** — advocate for an Orphanet entry and ICD-11 extension code to enable systematic epidemiology.
8. **Standardized management guidance** — draft a consensus care pathway (Ig-replacement thresholds, HPV surveillance, malignancy screening, HSCT criteria) tailored to IMD70 within the CVID/CID framework.

---

*Report compiled from a 5-iteration autonomous investigation: 9 confirmed findings, 14 papers reviewed. Evidence source types span human clinical cohort (PMID:32499645), in vitro/cellular (PMID:32943673, 41857046, 39384042, 29497022), computational/constraint (gnomAD, ClinVar, UniProt), and comparator human disease (PMID:29127144).*


## Artifacts

- [OpenScientist final report](Immunodeficiency_70-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_70-deep-research-openscientist_artifacts/final_report.pdf)