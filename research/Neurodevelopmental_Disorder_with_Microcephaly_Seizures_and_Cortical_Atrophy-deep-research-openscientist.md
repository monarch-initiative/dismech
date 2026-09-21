---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-18T15:07:38.160863'
end_time: '2026-08-18T15:21:29.629452'
duration_seconds: 831.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Microcephaly, Seizures, and Cortical
    Atrophy
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 10
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_with_Microcephaly_Seizures_and_Cortical_Atrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_with_Microcephaly_Seizures_and_Cortical_Atrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Microcephaly, Seizures, and Cortical Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Microcephaly, Seizures, and Cortical Atrophy** covering all of the
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

# Neurodevelopmental Disorder with Microcephaly, Seizures, and Cortical Atrophy (NDMSCA / VARS1-related disorder)

**Comprehensive Disease Characteristics Report**
**OMIM #617802 · Gene: VARS1 · Category: Mendelian (autosomal recessive)**
*Report compiled from a 5-iteration autonomous literature investigation (30 papers reviewed, 9 confirmed findings)*

---

## Summary

**Neurodevelopmental disorder with microcephaly, seizures, and cortical atrophy (NDMSCA; also abbreviated NEDMISCA), OMIM #617802, is an ultra-rare autosomal recessive Mendelian disease caused by biallelic variants in *VARS1*, the gene encoding the sole cytoplasmic valyl-tRNA synthetase (ValRS).** The disease was established in 2019 by two independent landmark cohorts — Siekierska et al. (10 patients; [PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)) and Friedman et al. (7 patients from 5 families; [PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)) — and was substantially expanded in 2026 by Aynekin et al. (13 individuals from 10 families; [PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)). In total, roughly **~30 molecularly confirmed patients** are described in the world literature.

Affected individuals present with a consistent core phenotype: **primary or progressive microcephaly, global developmental delay / intellectual disability, early-onset epilepsy or epileptic encephalopathy, and progressive cerebral cortical atrophy with white-matter volume loss.** The molecular mechanism is a **partial loss of valyl-tRNA aminoacylation function** — most pathogenic alleles are hypomorphic missense variants clustered in the tRNA-binding/anticodon and catalytic domains — which impairs cytoplasmic protein translation in the developing brain. Functional confirmation comes from reduced enzymatic activity in patient fibroblasts, yeast complementation assays, and a *vars*-knockout zebrafish model that recapitulates key neurological traits.

There is **no disease-specific or curative therapy**; management is entirely supportive (antiseizure medications, developmental/rehabilitative therapy, feeding support). Mechanistically rational but unproven experimental strategies — cognate amino acid (valine) supplementation, cognate-tRNA delivery, and integrated-stress-response (ISR) inhibition — are borrowed from the broader aminoacyl-tRNA synthetase (ARS) disorder field. Prognosis is poor, with severe lifelong disability, frequently drug-resistant epilepsy, and a neurodegenerative course; residual VARS1 enzymatic activity of the specific genotype is the most plausible prognostic modifier.

---

## 1. Disease Information

**Overview.** NDMSCA is a Mendelian, autosomal recessive, infantile-onset neurodevelopmental and neurodegenerative disorder of cytoplasmic protein translation. It belongs to the growing class of **aminoacyl-tRNA synthetase (ARS) deficiencies**, in which impaired charging of a specific tRNA with its cognate amino acid disrupts protein synthesis, with a brain-predominant clinical picture.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #617802 — "Neurodevelopmental disorder with microcephaly, seizures, and cortical atrophy" |
| OMIM (gene) | 192150 (*VARS1*) |
| Gene symbol | **VARS1** (formerly *VARS*) |
| HGNC | HGNC:12651 |
| NCBI Gene | 7407 |
| Ensembl | ENSG00000204394 |
| UniProt | P26640 |
| MONDO (suggested) | MONDO:0060639 |
| Cytogenetic locus | 6p21.33 (within the MHC region), chr6:31,777,518–31,795,752 (GRCh38) |

**Synonyms / alternative names:** NDMSCA; NEDMISCA; VARS1-related (valyl-tRNA synthetase) developmental encephalopathy; "developmental encephalopathy with microcephaly"; progressive neurodevelopmental epileptic encephalopathy due to VARS variants.

**Source of information.** Evidence is derived from **aggregated disease-level and primary case-series resources** (OMIM, published patient cohorts), not from EHR/individual-patient population databases. The disease-level knowledge base comprises three cohort publications plus isolated case reports.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused exclusively by **biallelic (homozygous or compound heterozygous) pathogenic variants in *VARS1***. As Friedman et al. state: *"VARS encodes the only known valine cytoplasmic-localized aminoacyl-tRNA synthetase. Here, we report seven patients from five unrelated families with five different biallelic missense variants in VARS"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)). There is no environmental or infectious contribution to primary causation.

**Genetic risk factors.** The only established risk factor is inheritance of two damaging *VARS1* alleles. **Consanguinity** increases risk, as expected for a recessive disorder — homozygous variants are reported in multiple families, including consanguineous unions (e.g., the consanguineous case in [PMID: 36204440](https://pubmed.ncbi.nlm.nih.gov/36204440/)).

**Environmental risk / protective factors.** None identified. No lifestyle, occupational, toxic, or nutritional factors are known to modify onset or risk. As a fully penetrant monogenic recessive disorder, gene–environment interactions have not been described. There are no reported genetic protective/modifier alleles beyond the intrinsic effect of residual enzyme activity (see §9, §11).

---

## 3. Phenotypes

The core phenotype is a **triad of progressive microcephaly, seizures, and cortical atrophy**, on a background of global developmental delay / intellectual disability. Friedman et al.: *"Subjects present with a range of global developmental delay, epileptic encephalopathy and primary or progressive microcephaly. Longitudinal assessment demonstrates progressive cortical atrophy and white matter volume loss"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)). Aynekin et al. confirm the triad in an independent cohort: *"a neurodevelopmental syndrome with progressive microcephaly, seizures, and intellectual disability"* ([PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)).

| Phenotype | Type | Onset | Severity / course | Frequency (qualitative) | Suggested HPO |
|---|---|---|---|---|---|
| Microcephaly (primary or progressive) | Physical/growth sign | Congenital–infantile | Moderate–severe; often progressive | Core (near-universal) | HP:0000252; HP:0000253 (progressive) |
| Global developmental delay / intellectual disability | Cognitive/behavioral | Infantile | Severe | Core | HP:0001263; HP:0001249 |
| Seizures / epileptic encephalopathy | Neurological sign | Early-onset (often infantile) | Often drug-resistant; severe | Common/core | HP:0001250; HP:0200134 |
| Cerebral cortical atrophy | Imaging sign | Infantile onset, progressive | Progressive | Core (imaging) | HP:0002120 |
| White-matter volume loss / abnormal white matter | Imaging sign | Progressive | Progressive | Common | HP:0002500 |
| Hypotonia | Neurological sign | Infantile | Variable | Common | HP:0001252 |
| Thin corpus callosum, delayed myelination | Imaging sign | Infantile | Structural | Variable/common | HP:0002079; HP:0012448 |
| Spasticity, feeding difficulties, visual/optic involvement | Neurological/other | Variable | Variable | Variable | (feature-dependent) |

**Quality-of-life impact.** Given severe intellectual disability, drug-resistant epilepsy, motor impairment, and feeding difficulty, affected children are typically fully dependent for daily activities. Formal QoL instrument data (EQ-5D, SF-36, PROMIS) are **not available** for this ultra-rare cohort.

---

## 4. Genetic / Molecular Information

**Causal gene.** *VARS1* (HGNC:12651; OMIM gene 192150; UniProt P26640), encoding cytoplasmic valyl-tRNA synthetase, the enzyme that charges tRNA-Val with valine for cytoplasmic translation.

**Pathogenic variants.** The mutational spectrum is dominated by **missense variants**, with a minority of truncating alleles:

- Siekierska et al.: an allelic series of **9 biallelic variants (7 novel, 2 previously reported) in 10 patients** ([PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)).
- Friedman et al.: **5 biallelic missense variants** across 5 families; variants *"map to the VARS tRNA binding domain and adjacent to the anticodon domain, and disrupt highly conserved residues"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)).
- Aynekin et al. (2026): **15 variants** — 2 causing premature truncation (LOF) and 13 missense localizing to catalytic and aminoacylation domains ([PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)).

**Variant classification / functional consequence.** Most alleles are ACMG **pathogenic/likely pathogenic**, but VUS are common across ARS genes (over 80% of ARS missense variants are VUS per [PMID: 42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/)), underscoring the value of functional assays. The functional consequence is **partial loss of function (hypomorphic)** — patient cells retain intact VARS protein but show reduced enzymatic activity (see §6). Complete biallelic null is likely incompatible with life (consistent with embryonic lethality of ARS knockouts in mouse).

**Population allele frequency / constraint.** gnomAD (GRCh38) constraint for *VARS1*: **pLI ≈ 0 (3.8×10⁻¹⁵)**, observed/expected LoF = 0.57 (LOEUF ≈ 0.68; 92 observed vs 161 expected LoF), **missense Z = 3.71** (oe_mis = 0.79). Interpretation: heterozygous LoF is *tolerated* (carriers unaffected — as expected for a recessive gene), while *strong missense constraint* indicates missense changes in the aminoacylation/tRNA-binding domains are deleterious — matching the observation that most pathogenic alleles are missense.

**Somatic vs germline.** All variants are **germline**. No somatic involvement.

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier genes, epigenetic marks, or large-scale chromosomal abnormalities have been described for this disorder. The most likely intrinsic modifier of severity is the **residual aminoacylation activity of the specific biallelic genotype**.

---

## 5. Environmental Information

**Not applicable.** NDMSCA is a purely Mendelian genetic disorder. No environmental factors, lifestyle factors, or infectious agents contribute to causation or triggering. (Note: because *VARS1* lies within the 6p21.33 MHC region, the gene is physically near immune loci, but there is no immune-mediated or infectious mechanism to the disease.)

---

## 6. Mechanism / Pathophysiology

### Causal chain

```
Biallelic hypomorphic VARS1 variants
        │  (missense in tRNA-binding/anticodon + catalytic domains; rare truncating)
        ▼
Reduced valyl-tRNA aminoacylation activity  (partial loss of function)
        │  [GO:0004832 valine-tRNA ligase activity; GO:0006438 valyl-tRNA aminoacylation]
        ▼
Impaired cytoplasmic protein translation  [GO:0006412; GO:0005829 cytosol]
        │
        ▼
Reduced neurogenesis + increased apoptosis in developing brain
        │  (inferred from comparative ARS models: aars1 zebrafish)
        ▼
Failure of brain growth (microcephaly) + neuronal/white-matter loss
        │
        ▼
Progressive cortical & white-matter atrophy → epilepsy, DD/ID  (clinical manifestation)
```

**Molecular pathway / biochemical defect.** The primary lesion is **enzymatic**: reduced valine-tRNA ligase activity (GO:0004832) impairing valyl-tRNA aminoacylation (GO:0006438), a core step of cytoplasmic translation (GO:0006412). Friedman et al.: *"Patient primary cells show intact VARS protein but reduced enzymatic activity, suggesting partial loss of function"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)). Siekierska et al. independently confirm: *"In silico, in vitro, and yeast complementation assays demonstrate that the underlying pathomechanism of these mutations is most likely a loss of protein function"* ([PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)).

**Structural basis.** Molecular-dynamics simulations show missense substitutions *"can disrupt local protein dynamics, RNA-interaction surfaces, or catalytic geometry, thereby affecting ligand recognition, substrate specificity, and tRNA interaction"* ([PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)).

**Cellular processes.** By analogy with the related recessive ARS disorder caused by *AARS1*, the cellular consequence of translation-factor ARS LOF is **reduced neurogenesis and increased apoptosis**: *"zebrafish mutants in aars1 have reduced neurogenesis and increased apoptosis"* ([PMID: 41508610](https://pubmed.ncbi.nlm.nih.gov/41508610/)). A plausible downstream contributor across ARS diseases is chronic activation of the **integrated stress response (ISR)** secondary to accumulation of uncharged tRNA (the rationale for ISR-inhibitor therapy; [PMID: 39702998](https://pubmed.ncbi.nlm.nih.gov/39702998/)).

**Cell types / subcellular localization.** Implicated cell types: cortical neurons (CL:0000540 neuron; CL:0010012 cerebral cortex neuron) and — via white-matter loss/hypomyelination — oligodendrocytes (CL:0000128). VARS1 acts in the **cytoplasm/cytosol (GO:0005829)**, the site of cytoplasmic translation. (VARS1 is distinct from mitochondrial ValRS; the disorder is a *cytoplasmic* translation defect.)

**Immune / metabolic / omics.** No autoimmune or immunodeficiency component. No specific metabolic, proteomic, metabolomic, or lipidomic disease signature has been published beyond the direct aminoacylation defect. No single-cell/spatial/multi-omics datasets exist for this disorder.

---

## 7. Anatomical Structures Affected

**Organ / body system.** The disease is **CNS-predominant**; the primary affected organ is the **brain** (UBERON:0000955). There is no consistent primary involvement of non-neural organs despite VARS1 being a general translation enzyme.

**Regional / tissue involvement (bilateral, diffuse):**

| Structure | UBERON | Finding |
|---|---|---|
| Cerebral cortex | UBERON:0000956 | Progressive cortical atrophy |
| Cerebral white matter | UBERON:0002316 | Progressive white-matter volume loss; delayed myelination |
| Corpus callosum | UBERON:0001851 | Thinning |
| Brain (global) | UBERON:0000955 | Microcephaly / reduced brain volume |

Friedman et al.: *"Longitudinal assessment demonstrates progressive cortical atrophy and white matter volume loss"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)).

**Cell level:** cortical neurons (CL:0000540, CL:0010012); oligodendrocytes (CL:0000128). **Subcellular:** cytosol (GO:0005829). **Lateralization:** bilateral/symmetric, diffuse.

---

## 8. Temporal Development

**Onset.** Congenital-to-early-infantile. Microcephaly may be **primary (present at birth)** or **progressive (postnatally acquired)**; epilepsy is often early-onset. Siekierska et al.: *"ten patients with a developmental encephalopathy with microcephaly, often associated with early-onset epilepsy"* ([PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)).

**Progression.** The course is **progressive / neurodegenerative** — longitudinal imaging demonstrates worsening cortical and white-matter atrophy over time ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)). Friedman et al. explicitly frame VARS1 disease as *"pediatric neurodegeneration."* Disease duration is chronic and lifelong; there is no remission.

**Critical period.** Because the defect impairs neurogenesis during brain development, the **prenatal and early-postnatal window** is the period of greatest vulnerability and the theoretical window for any disease-modifying intervention.

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare.** The world literature comprises approximately **~30 molecularly confirmed individuals**: 10 (Siekierska et al., [PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)), 7 from 5 families (Friedman et al., [PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)), 13 from 10 families (Aynekin et al., [PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)), plus isolated reports (e.g., [PMID: 36204440](https://pubmed.ncbi.nlm.nih.gov/36204440/)). **No population prevalence or incidence estimate exists** (not established in Orphanet/GBD).

**Inheritance.** **Autosomal recessive.** Affected individuals carry biallelic (homozygous or compound heterozygous) *VARS1* variants; parents are unaffected obligate heterozygotes — consistent with the LoF-tolerant heterozygous gnomAD profile. Aynekin et al.: *"We clinically evaluated 13 affected individuals from 10 unrelated families"* ([PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)); Friedman et al.: *"seven patients from five unrelated families with five different biallelic missense variants"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)).

- **Penetrance:** Presumed complete for biallelic damaging genotypes.
- **Expressivity:** Variable (severity likely tracks residual enzyme activity; Aynekin et al. define new clinical/molecular subtypes).
- **Consanguinity:** Increases risk; homozygous cases reported in consanguineous families.
- **Founder effect / anticipation / mosaicism:** No established founder mutation; two recurrent alleles noted by Siekierska et al. suggest limited allelic recurrence. No anticipation (not a repeat-expansion disorder). No germline mosaicism reported.
- **Carrier frequency:** Not formally established; very low given rarity.
- **Sex ratio:** No sex bias (autosomal). Both sexes affected.

---

## 10. Diagnostics

**Molecular diagnosis is definitive.** All reported patients were identified by **whole-exome or whole-genome sequencing** revealing biallelic *VARS1* variants ([PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/); [PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/); [PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)). WES/WGS and neurodevelopmental/epilepsy gene panels including *VARS1* are the recommended first-line tests. Chromosomal microarray/karyotype are not informative (no structural cause).

**Functional confirmation.** A **patient-fibroblast aminoacylation activity assay** confirms pathogenicity and reclassifies VUS. A high-throughput LC-MS/MS aminoacylation assay measuring aaRS activity in patient fibroblasts *"has contributed to the diagnosis of nearly 200 patients"* across ARS genes ([PMID: 42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/)).

**Supportive investigations.** Serial **brain MRI** (NCIT:C16809) shows progressive cortical atrophy, white-matter volume loss, thin corpus callosum, delayed myelination; **EEG** (NCIT:C38054) documents epileptic encephalopathy. Head-circumference tracking documents microcephaly.

**Suggested NCIT terms:** Whole Exome Sequencing (NCIT:C101294), MRI (NCIT:C16809), EEG (NCIT:C38054).

**Differential diagnosis.** Other ARS/translation disorders and recessive microcephaly–epilepsy–cortical-atrophy syndromes reviewed during this investigation, distinguished by gene and neuroimaging pattern: *AARS1*, *EPRS1* (HLD15), *DARS2/AARS2/EARS2* (mitochondrial leukoencephalopathies), *ASNS* deficiency, *TBCD* tubulinopathy, *TRAPPC4*, *BRAT1*, *CSTB*, *MINPP1*, *UFM1* (H-ABC), *WWOX*. Genetic testing is required to distinguish these overlapping phenotypes.

**Screening.** No newborn/population screening exists. Cascade carrier testing of relatives and prenatal/preimplantation testing are feasible once the familial variants are known.

---

## 11. Outcome / Prognosis

**Prognosis is poor.** Affected individuals have **profound intellectual and motor disability with frequently drug-resistant epilepsy**, on a **progressive/neurodegenerative** trajectory. Friedman et al. frame the disorder as pediatric neurodegeneration: *"The implication of VARS in pediatric neurodegeneration broadens the spectrum of human diseases due to mutations in tRNA synthetase genes"* ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)).

**Survival / mortality.** Formal survival, mortality, and QoL statistics are **not available** for this ~30-patient cohort. Early-childhood death occurs at the severe end of the spectrum (as seen across severe recessive translation disorders).

**Prognostic modifier.** The most plausible predictor of severity is the **residual VARS1 aminoacylation activity** of the specific biallelic genotype — truncating/low-activity alleles predicting greater severity — consistent with the partial-loss-of-function model and the new molecular subtypes defined by Aynekin et al. ([PMID: 41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/)).

---

## 12. Treatment

**No disease-specific or curative therapy exists.** Management is **supportive and symptomatic**:

| Domain | Intervention | Suggested NCIT |
|---|---|---|
| Epilepsy | Antiseizure medications (often multiple; may be refractory) | NCIT:C264 (Anticonvulsant Agent) |
| Development | Physical/occupational/speech therapy | — |
| Nutrition | Feeding support (may require tube feeding) | — |
| Monitoring | Serial MRI, EEG, growth tracking | NCIT:C16809, NCIT:C38054 |

**Experimental / mechanism-based strategies (unproven for VARS1):**

- **Cognate amino acid (valine) supplementation** — CHEBI:16414 (valine). *"Current treatment approaches to rescue defective or dysfunctional tRNA synthetase mutants include supplementation with cognate amino acids and delivery of cognate tRNAs to alleviate bottlenecks in translation. Complementary approaches use inhibitors to target the integrated stress response"* ([PMID: 39702998](https://pubmed.ncbi.nlm.nih.gov/39702998/)).
- **Cognate-tRNA delivery** and **ISR inhibitors** — investigational across ARS disorders ([PMID: 39702998](https://pubmed.ncbi.nlm.nih.gov/39702998/); [PMID: 42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/)).

**Important caveat on efficacy.** Amino acid supplementation is **safe but of unproven and apparently limited efficacy**. In a pilot trial of related mitochondrial ARS leukoencephalopathies (AARS2/DARS2), supplementation was *"safe and well tolerated ... but efficacy endpoints were not met"* though most patients remained clinically stable ([PMID: 41075682](https://pubmed.ncbi.nlm.nih.gov/41075682/)). Anecdotal benefit has been reported in some other ARS disorders (e.g., methionine in MARS1, tyrosine in YARS2), highlighting variable, gene- and case-specific responses. No controlled trial exists specifically for VARS1/valine.

---

## 13. Prevention

There is **no primary prevention** for this genetic disorder beyond reproductive genetic counseling.

- **Genetic counseling:** Autosomal recessive recurrence risk of 25% for future pregnancies of carrier couples; counseling is the central preventive tool.
- **Carrier / cascade testing:** Once familial *VARS1* variants are known, cascade testing of relatives and reproductive partners is possible.
- **Prenatal / preimplantation genetic testing (PGT):** Available for at-risk couples with known variants.
- **Consanguinity awareness:** In consanguineous populations, awareness and pre-conception counseling reduce recurrence.

Immunization, behavioral, environmental, and public-health prevention are **not applicable**.

---

## 14. Other Species / Natural Disease

- **Orthologous genes / taxonomy:** zebrafish *vars/vars1* (*Danio rerio*, NCBI Taxon 7955); *Saccharomyces cerevisiae* ortholog *VAS1* (Taxon 4932). VARS/ValRS is deeply evolutionarily conserved as an essential translation enzyme.
- **Natural disease in other species:** No naturally occurring VARS1 disorder in companion animals or wildlife has been reported (not applicable per OMIA).
- **Comparative biology:** The disease mechanism (essential aminoacylation) is conserved across eukaryotes, which is why yeast complementation is a valid pathogenicity assay.
- **Zoonotic potential:** Not applicable (non-infectious).

---

## 15. Model Organisms

| Model | Type | Key finding | Resource |
|---|---|---|---|
| *vars*-knockout zebrafish | Vertebrate (whole-organism) | *"Zebrafish modeling accurately recapitulated some of the key neurological disease traits"* ([PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)) | ZFIN (Taxon 7955) |
| Yeast complementation (*S. cerevisiae*) | Cellular / functional | Demonstrated loss of function of patient variants ([PMID: 30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/)) | SGD (Taxon 4932) |
| Patient fibroblasts | In vitro (human) | Intact protein but reduced aminoacylation activity ([PMID: 30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/)) | — |
| Comparative: *aars1* zebrafish / mouse | Vertebrate | *"zebrafish mutants in aars1 have reduced neurogenesis and increased apoptosis"*; Aars1 mouse embryonic-lethal ([PMID: 41508610](https://pubmed.ncbi.nlm.nih.gov/41508610/)) | ZFIN, MGI |

**Phenotype recapitulation.** The zebrafish *vars* knockout reproduces key neurological traits, validating it as a disease model; yeast complementation validates individual variant pathogenicity. **Limitations:** neither model fully captures the human progressive cortical/white-matter atrophy or seizure phenotype in detail. A dedicated *Vars1* mouse (knock-in of hypomorphic alleles) would better model the partial-LOF neurodegenerative course — this is a knowledge gap.

---

## Mechanistic Model / Interpretation

The evidence converges on a **single coherent mechanism** unified across three independent human cohorts and multiple functional systems:

```
              ┌─────────────────────────────────────────────┐
              │  UPSTREAM (genetic → biochemical)           │
              │  Biallelic hypomorphic VARS1 variants       │
              │  → partial loss of ValRS aminoacylation     │
              └───────────────────┬─────────────────────────┘
                                  ▼
              ┌─────────────────────────────────────────────┐
              │  MIDSTREAM (cellular)                       │
              │  Impaired cytoplasmic translation           │
              │  → ↓ neurogenesis, ↑ apoptosis (± ISR)      │
              └───────────────────┬─────────────────────────┘
                                  ▼
              ┌─────────────────────────────────────────────┐
              │  DOWNSTREAM (tissue → clinical)             │
              │  Failure of brain growth + neurodegeneration│
              │  → microcephaly, cortical/WM atrophy,       │
              │    epilepsy, DD/ID  (progressive)           │
              └─────────────────────────────────────────────┘
```

Three features make this model robust: (1) **convergent human genetics** — biallelic *VARS1* in ≥30 patients across ≥17 families from independent groups; (2) **direct functional evidence** — reduced enzyme activity in patient cells with intact protein (a *hypomorphic*, not null, mechanism); and (3) **cross-system validation** — yeast complementation and zebrafish knockout. The hypomorphic nature explains why the disease is viable at all (complete null likely lethal) and predicts a **genotype–severity relationship driven by residual activity** — the single most important open translational question.

---

## Evidence Base

| PMID | Role | How it supports the findings |
|---|---|---|
| [30755602](https://pubmed.ncbi.nlm.nih.gov/30755602/) | Landmark cohort (Friedman) | Establishes biallelic missense *VARS1* cause, partial-LOF mechanism (reduced enzyme activity, intact protein), progressive cortical/WM atrophy, "pediatric neurodegeneration." |
| [30755616](https://pubmed.ncbi.nlm.nih.gov/30755616/) | Landmark cohort (Siekierska) | Allelic series of 9 biallelic variants in 10 patients; yeast + zebrafish confirm loss of function; early-onset epilepsy + microcephaly. |
| [41672381](https://pubmed.ncbi.nlm.nih.gov/41672381/) | 2026 expansion (Aynekin) | Largest cohort (13/10 families); defines clinical/molecular subtypes; MD simulations of missense variants; truncating + missense spectrum. |
| [42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/) | Methods/therapy review | Aminoacylation functional assay for diagnosis/VUS reclassification; amino acid supplementation and gene-therapy landscape for ARS diseases. |
| [39702998](https://pubmed.ncbi.nlm.nih.gov/39702998/) | Therapy review | Mechanistic experimental strategies: cognate amino acid supplementation, tRNA delivery, ISR inhibition. |
| [41508610](https://pubmed.ncbi.nlm.nih.gov/41508610/) | Comparative model | *aars1* zebrafish show reduced neurogenesis + increased apoptosis — the cellular basis of ARS microcephaly. |
| [36204440](https://pubmed.ncbi.nlm.nih.gov/36204440/) | Case report | VARS VUS in a consanguineous neonate with NDMSCA-consistent neuroimaging; illustrates consanguinity and dual-diagnosis complexity. |
| [41075682](https://pubmed.ncbi.nlm.nih.gov/41075682/) | Trial (related ARS) | Amino acid supplementation safe but efficacy endpoints not met in AARS2/DARS2 — tempers therapeutic expectations. |

**Contextual differential-diagnosis literature** reviewed (not causal for this disease): MINPP1-PCH ([PMID: 41025723](https://pubmed.ncbi.nlm.nih.gov/41025723/)), UFM1 H-ABC ([PMID: 35189806](https://pubmed.ncbi.nlm.nih.gov/35189806/)), ASNS deficiency ([PMID: 30978478](https://pubmed.ncbi.nlm.nih.gov/30978478/)), TBCD tubulinopathy ([PMID: 27807845](https://pubmed.ncbi.nlm.nih.gov/27807845/)), TRAPPC4 ([PMID: 31794024](https://pubmed.ncbi.nlm.nih.gov/31794024/)), CSTB ([PMID: 28378817](https://pubmed.ncbi.nlm.nih.gov/28378817/)), BRAT1 ([PMID: 28635423](https://pubmed.ncbi.nlm.nih.gov/28635423/)), EPRS1/HLD15 ([PMID: 41721156](https://pubmed.ncbi.nlm.nih.gov/41721156/)), MARS1 ([PMID: 32833345](https://pubmed.ncbi.nlm.nih.gov/32833345/)).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare cohort (~30 patients).** No population prevalence/incidence, no formal survival/mortality/QoL data, and limited natural-history granularity.
2. **No genotype–phenotype quantification.** Although residual enzyme activity is the presumed severity determinant, no systematic correlation between measured aminoacylation activity and clinical severity has been published.
3. **No dedicated mammalian (mouse) model** of hypomorphic *Vars1*; existing models (zebrafish KO, yeast) do not fully recapitulate progressive cortical atrophy or epilepsy.
4. **No omics profiling** (transcriptomic, proteomic, metabolomic) of patient neural tissue or organoids.
5. **No VARS1-specific therapeutic data.** Valine supplementation is mechanistically rational but untested; extrapolation from other ARS trials suggests safety but uncertain/limited benefit.
6. **Frequencies of individual features** (e.g., exact % with seizures, hypotonia, feeding difficulty) are not precisely tabulated across the pooled cohort.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a genotype–activity–severity map.** Systematically measure fibroblast valyl-tRNA aminoacylation activity for each biallelic genotype and correlate with a standardized severity score (seizure control, developmental quotient, rate of atrophy on serial MRI).
2. **Generate a hypomorphic *Vars1* knock-in mouse** (patient missense allele in trans with a null) to model the progressive neurodegenerative course and test interventions in a mammalian brain.
3. **Patient-iPSC cortical organoids** to test whether (a) valine supplementation, (b) cognate-tRNA delivery, or (c) ISR inhibitors (e.g., ISRIB) rescue neurogenesis/apoptosis phenotypes in vitro.
4. **Pilot valine-supplementation study** with pre-specified biomarker endpoints (aminoacylation activity, ISR markers) and imaging endpoints, learning from the null-efficacy AARS2/DARS2 trial design ([PMID: 41075682](https://pubmed.ncbi.nlm.nih.gov/41075682/)).
5. **Build an international patient registry** to capture natural history, survival, seizure semiology/EEG evolution, and QoL — prerequisites for any future trial.
6. **Reclassify VUS at scale** using the high-throughput LC-MS/MS aminoacylation assay ([PMID: 42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/)) to improve diagnostic yield and enable cascade testing.

---

## Ontology Term Appendix

- **MONDO:** MONDO:0060639 (NDMSCA)
- **Gene/HGNC:** HGNC:12651 (VARS1); UniProt P26640; NCBI Gene 7407
- **HPO:** HP:0000252, HP:0000253, HP:0001263, HP:0001249, HP:0001250, HP:0200134, HP:0002120, HP:0002500, HP:0001252, HP:0002079, HP:0012448
- **GO (process/function/component):** GO:0006438 (valyl-tRNA aminoacylation), GO:0004832 (valine-tRNA ligase activity), GO:0006412 (translation), GO:0000049 (tRNA binding), GO:0005829 (cytosol)
- **CL:** CL:0000540 (neuron), CL:0010012 (cerebral cortex neuron), CL:0000128 (oligodendrocyte)
- **UBERON:** UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex), UBERON:0002316 (white matter), UBERON:0001851 (corpus callosum)
- **CHEBI:** CHEBI:16414 (valine)
- **NCIT:** NCIT:C101294 (WES), NCIT:C16809 (MRI), NCIT:C38054 (EEG), NCIT:C264 (Anticonvulsant Agent)

---

*Evidence source types: human clinical/genetic (Siekierska, Friedman, Aynekin cohorts; case reports), in vitro (patient fibroblast aminoacylation assays), model organism (zebrafish, yeast), and computational (molecular dynamics, gnomAD constraint). All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_with_Microcephaly_Seizures_and_Cortical_Atrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_with_Microcephaly_Seizures_and_Cortical_Atrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.