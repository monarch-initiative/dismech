---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T10:12:34.913222'
end_time: '2026-08-28T10:33:25.182993'
duration_seconds: 1250.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Calvarial Doughnut Lesions-Bone Fragility Syndrome
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
citation_count: 8
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Calvarial_Doughnut_Lesions-bone_Fragility_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Calvarial_Doughnut_Lesions-bone_Fragility_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Calvarial Doughnut Lesions-Bone Fragility Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Calvarial Doughnut Lesions-Bone Fragility Syndrome** covering all of the
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

# Calvarial Doughnut Lesions–Bone Fragility Syndrome (CDL/CDL-SMD): Comprehensive Disease Report

**Disease:** Calvarial Doughnut Lesions with Bone Fragility, with or without Spondylometaphyseal Dysplasia
**OMIM:** #126550 · **Gene:** *SGMS2* (SMS2) · **MONDO:** MONDO:0007470 / MONDO:0007926 · **ORPHA:** 85192
**Category:** Mendelian (autosomal dominant)

---

## Summary

Calvarial Doughnut Lesions–Bone Fragility Syndrome (CDL; OMIM #126550) is an **ultra-rare autosomal-dominant skeletal dysplasia** caused by heterozygous pathogenic variants in *SGMS2*, the gene encoding the plasma-membrane–resident enzyme **sphingomyelin synthase 2 (SMS2)** on chromosome 4q25. The disease is defined clinically by childhood-onset low bone mineral density, recurrent spinal and peripheral fragility fractures, and its pathognomonic radiographic hallmark: multiple ring-like ("doughnut-shaped") sclerotic/hyperostotic lesions of the calvarium, often palpable as cranial lumps. A subset of patients also has spondylometaphyseal dysplasia (CDL-SMD), representing the severe end of the disease spectrum.

The central mechanistic insight is that CDL results from **two distinct molecular mechanisms operating along a genotype–phenotype gradient**. The recurrent nonsense variant **c.148C>T (p.Arg50\*)** produces a catalytically inactive enzyme (loss of function) and is associated with the milder, childhood-onset osteoporosis end of the spectrum. In contrast, the N-terminal missense variants **c.185T>G (p.Ile62Ser)** and **c.191T>G (p.Met64Arg)** produce a **fully active but ER-retained enzyme** — a "toxic gain-of-mislocalization" mechanism — and cause the severe CDL-SMD phenotype with neonatal fractures, severe short stature, and long-bone deformities. Because SMS2 normally acts at the plasma membrane and trans-Golgi to establish a sphingomyelin/sterol gradient along the secretory pathway, mislocalized enzyme disrupts membrane lipid organization in osteogenic cells and impairs the matrix mineralization that osteoblasts and osteocytes carry out. Osteoclast formation and function remain normal, distinguishing CDL from high-turnover bone disease and from osteogenesis imperfecta.

All three canonical pathogenic variants are **absent from gnomAD** (~1.6M alleles surveyed), and *SGMS2* shows only moderate loss-of-function constraint (pLI ≈ 0.01, LOEUF ≈ 0.69). This population-genetic signature supports the interpretation that the severe phenotype depends on the mislocalization/gain mechanism rather than on simple gene-dosage loss. Management is currently **symptomatic**, centered on bisphosphonates plus calcium and vitamin D, which improve bone mineral density and reduce fractures; no curative therapy exists. This report synthesizes 13 confirmed findings across all 15 requested disease-characteristic domains.

---

## Key Findings

### 1. Disease Information

CDL is a rare autosomal-dominant skeletal disorder characterized by low bone mineral density, spinal and peripheral fractures, and specific sclerotic lesions of the cranial bones (Merkuryeva et al. 2023). As stated verbatim: *"Calvarial doughnut lesions (CDL) with bone fragility with or without spondylometaphyseal dysplasia (MIM: #126550) is a rare autosomal dominant skeletal disorder characterized by low bone mineral density, spinal and peripheral fractures, and specific sclerotic lesions of the cranial bones"* ([PMID: 37175737](https://pubmed.ncbi.nlm.nih.gov/37175737/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (disease) | #126550 |
| OMIM (gene *SGMS2*) | 611574 |
| Chromosomal locus | 4q25 |
| Orphanet | ORPHA:85192 |
| MONDO | MONDO:0007470 (also mapped MONDO:0007926) |
| SNOMED CT | 720598005 |
| Disease Ontology | DOID:0080721 |
| UMLS / GTR | C1852022 |
| HGNC gene | SGMS2 |

**Synonyms / alternative names:** familial calvarial doughnut lesions; CDL; CDL with bone fragility; CDL with spondylometaphyseal dysplasia (CDLSMD/CDL-SMD).

The information is derived from **aggregated disease-level resources** and small clinical case series/family studies (the entire literature comprises roughly 8–11 families), rather than from EHR-scale patient datasets.

### 2. Etiology

The **primary cause is genetic**: heterozygous pathogenic variants in *SGMS2*. There is no known environmental, infectious, or acquired etiology. Pekkinen et al. 2019 evaluated six families with rare skeletal phenotypes and osteoporosis by next-generation sequencing and identified in all families a heterozygous *SGMS2* variant: *"we identified a heterozygous variant in SGMS2, a gene prominently expressed in cortical bone and encoding the plasma membrane-resident sphingomyelin synthase SMS2"* ([PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)).

- **Genetic risk factors:** The causal alleles are the disease-defining variants themselves (p.Arg50\*, p.Ile62Ser, p.Met64Arg). No independent susceptibility loci or modifier genes have been established.
- **Environmental / lifestyle risk factors:** None identified; the disease is monogenic and highly penetrant for the genetic lesion, though clinical expressivity is variable.
- **Protective factors / gene–environment interactions:** No genetic or environmental protective factors have been reported. Supportive measures (calcium, vitamin D, bisphosphonates) mitigate the phenotype but are treatments rather than etiologic protective factors.

### 3. Phenotypes

CDL is a multi-system skeletal phenotype with variable severity. The following table consolidates the reported features with suggested HPO terms.

| Phenotype | Type | Onset / severity | Suggested HPO |
|---|---|---|---|
| Doughnut-shaped sclerotic calvarial lesions (palpable cranial lumps) | Physical manifestation / imaging | Childhood; pathognomonic | HP:0002683 (Abnormal skull morphology); HP:0002684 (Thickened calvaria) |
| Low bone mineral density / osteoporosis | Laboratory / imaging | Childhood-onset | HP:0000939 (Osteoporosis); HP:0004349 (Reduced bone mineral density) |
| Recurrent fragility fractures (spinal + peripheral) | Clinical sign | Childhood; severe in CDL-SMD (neonatal) | HP:0002659 (Increased susceptibility to fractures); HP:0002757 (Recurrent fractures) |
| Vertebral compression fractures / "bone-in-bone" vertebrae | Imaging | Childhood–adult | HP:0002953 (Vertebral compression fractures) |
| Spondylometaphyseal dysplasia (severe subset) | Physical manifestation | Neonatal/infantile | HP:0002656 (Metaphyseal dysplasia); HP:0002655 (Spondylometaphyseal dysplasia) |
| Severe short stature (severe subset) | Physical manifestation | Congenital/infantile | HP:0004322 (Short stature) |
| Long-bone deformity / undermodeling of tubular bones | Imaging | Childhood | HP:0000924 (Abnormal skeletal morphology) |
| Peripheral facial nerve palsy | Neurological sign | Variable | HP:0010628 (Facial palsy) |
| Elevated serum alkaline phosphatase | Laboratory abnormality | Variable | HP:0003155 (Elevated alkaline phosphatase) |
| Dental caries / tooth hypoplasia | Physical manifestation | Childhood | HP:0000670 (Carious teeth); HP:0006297 (Hypoplasia of teeth) |
| Glaucoma (occasional) | Clinical sign | Variable | HP:0000501 (Glaucoma) |
| Scoliosis | Physical manifestation | Childhood | HP:0002650 (Scoliosis) |

**Severity gradient:** Subjects with p.Arg50\* present at the milder end — *"childhood-onset osteoporosis with or without cranial sclerosis"* — whereas patients with p.Ile62Ser or p.Met64Arg have *"a more severe presentation, with neonatal fractures, severe short stature, and spondylometaphyseal dysplasia"* ([PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)). Progression is chronic and lifelong, with fracture susceptibility being the dominant morbidity. There is **wide interfamilial and intrafamilial phenotypic variability**, even among individuals sharing the identical p.Arg50\* variant (Merkuryeva 2023; Basalom 2021).

**Neurological involvement:** *"Several subjects had experienced peripheral facial nerve palsy or other neurological manifestations"* ([PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)), attributed to the role of sphingomyelin in neural tissue. A dedicated 2023 review (Pihlström et al., PMID 37886644) specifically links *SGMS2* primary osteoporosis with facial nerve palsy.

**Quality-of-life impact:** Recurrent fractures, chronic back pain from vertebral compressions, scoliosis, short stature, and facial nerve palsy collectively impair mobility, cause chronic pain, and reduce daily functioning. No formal EQ-5D/SF-36/PROMIS studies exist for this ultra-rare disease.

### 4. Genetic / Molecular Information

**Causal gene:** *SGMS2* (sphingomyelin synthase 2 / SMS2), OMIM 611574, chromosome 4q25. The three canonical pathogenic variants (RefSeq NM_001375905.1) are:

| Variant (cDNA) | Protein | Type | ClinVar classification | ClinVar VCV | gnomAD |
|---|---|---|---|---|---|
| c.148C>T | p.Arg50\* (Arg50Ter) | Nonsense | Pathogenic/Likely pathogenic | VCV000635285 | Absent (AC=0) |
| c.185T>G | p.Ile62Ser | Missense | Pathogenic | VCV000635286 | Absent (AC=0) |
| c.191T>G | p.Met64Arg | Missense | Pathogenic | VCV000635287 | Absent (AC=0) |

*"Four unrelated families shared the same nonsense variant, c.148C>T (p.Arg50\*), whereas the other families had a missense variant, c.185T>G (p.Ile62Ser) or c.191T>G (p.Met64Arg)"* ([PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)).

**Functional consequences:** *"While the p.Arg50\* mutation yielded a catalytically inactive enzyme, p.Ile62Ser and p.Met64Arg each enhanced the rate of de novo sphingomyelin production by blocking export of a functional enzyme from the endoplasmic reticulum"* ([PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)). Thus p.Arg50\* = **loss of function**; the missense alleles = **ER-retention / toxic gain-of-mislocalization**.

**Population genetics and constraint:** In gnomAD v4 (GRCh38, ~1.61M alleles), all three canonical variants are absent (exome AC=0, genome AC=0; 95% upper-bound AF ≈ 1.9×10⁻⁶). By contrast, the adjacent benign-leaning VUS c.149G>A/p.Arg50Gln is observed (AC=15, AF≈9.3×10⁻⁶), reinforcing the specificity of the causal alleles. *SGMS2* gene-level constraint is only moderate — **pLI = 0.010, LOEUF (oe_lof_upper) = 0.69, observed/expected LOF = 21/43.8 = 0.48, mis_z = 1.20** — meaning the gene tolerates heterozygous LOF reasonably well. This is a key clue that the **severe phenotype is not driven by simple haploinsufficiency/dosage but by the gain-of-mislocalization mechanism** of the missense alleles.

**Modifier genes / epigenetics / chromosomal abnormalities:** No disease modifiers have been established. Some "pathogenic" *SGMS2*-region ClinVar entries are large chromosome-4q copy-number gains unrelated to CDL and should not be confused with the point-variant allelic series. Of ~200 *SGMS2* ClinVar submissions, the vast majority are VUS from population/panel screening; only the three point variants above are disease-causing for CDL.

### 5. Environmental Information

No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents are implicated in CDL. It is a purely Mendelian, monogenic disorder. (Sphingomyelin biology is relevant to other membrane-stress and infection contexts — e.g. SMPDL3B in cGAS-STING signaling, PMID 41175872 — but these are unrelated to CDL pathogenesis.)

### 6. Mechanism / Pathophysiology

**Molecular pathway — sphingolipid metabolism.** SMS2 catalyzes the transfer reaction **phosphatidylcholine + ceramide → sphingomyelin + diacylglycerol** at the plasma membrane and trans-Golgi. Sphingomyelin is the *"main lipid component of the plasma membrane essential for bone mineralization"* ([PMID: 37175737](https://pubmed.ncbi.nlm.nih.gov/37175737/)). Normally, sphingomyelin production in the trans-Golgi traps ER cholesterol to build a **sphingomyelin/sterol gradient along the secretory pathway**.

**Core pathomechanism (severe missense alleles).** Sokoya et al. 2022 showed that *"SMS2 variants linked to the most severe bone phenotypes retain full enzymatic activity but fail to leave the ER owing to a defective autonomous ER export signal. Cells harboring pathogenic SMS2 variants accumulate sphingomyelin in the ER and display a disrupted transbilayer sphingomyelin asymmetry"* ([PMID: 36102623](https://pubmed.ncbi.nlm.nih.gov/36102623/)). This ectopic ER sphingomyelin production produces imbalances in cholesterol organization, glycerophospholipid profiles, and membrane lipid order along the secretory pathway (also observed in patient-derived fibroblasts). The authors conclude: *"We postulate that pathogenic SMS2 variants undermine the capacity of osteogenic cells to uphold nonrandom lipid distributions that are critical for their bone forming activity"* ([PMID: 36102623](https://pubmed.ncbi.nlm.nih.gov/36102623/)).

**Causal chain (severe CDL-SMD):**

```
Missense SGMS2 (p.Ile62Ser / p.Met64Arg)
   │  (disrupts N-terminal autonomous ER-export signal)
   ▼
Active SMS2 retained in the ER  ──► ectopic SM synthesis in ER
   ▼
Disrupted transbilayer SM asymmetry + altered cholesterol/
glycerophospholipid distribution + abnormal membrane lipid order
   ▼
Loss of nonrandom secretory-pathway lipid landscape in osteoblasts/osteocytes
   ▼
Defective bone-matrix mineralization (normal osteoclasts)
   ▼
Low BMD, fragile bone, doughnut calvarial lesions, SMD
```

**Bone tissue-level pathology.** Mäkitie et al. 2021 analyzed transiliac biopsies from two adult males with p.Arg50\*. Histomorphometry showed reduced osteoid thickness and mineralizing surface, increased osteoid surface, and markedly elevated **mineralization lag time (+8.16 SD, +4.10 SD)**. Quantitative backscattered electron imaging (qBEI) showed **low, heterogeneous matrix mineralization (CaPeak −2.41/−3.72 SD; CaWidth +7.47/+4.41 SD)** with chaotic collagen fibril arrangement under polarized light; osteocyte lacunae were abnormally large/round and the **canalicular network severely disturbed** ([PMID: 34761145](https://pubmed.ncbi.nlm.nih.gov/34761145/)). Independent biopsy data: *"Bone biopsies showed markedly altered bone material characteristics, including defective bone mineralization. Osteoclast formation and function in vitro was normal"* ([PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)).

**Upstream vs downstream:** The upstream trigger is the mislocalized/inactive SMS2 enzyme; the downstream endpoint is impaired osteoblast/osteocyte matrix mineralization. Osteoclasts are not the effectors — resorption is normal — so the disease is a **bone-formation/mineralization defect, not a resorption defect**.

**Ontology suggestions:** GO:0006686 (sphingomyelin biosynthetic process); GO:0006665 (sphingolipid metabolic process); GO:0030282 (bone mineralization); GO:0001503 (ossification); GO:0006888 (ER-to-Golgi vesicle-mediated transport). Cell types: CL:0000062 (osteoblast); CL:0000137 (osteocyte). CHEBI:17636 (sphingomyelin); CHEBI:16113 (cholesterol); CHEBI:17761 (ceramide).

### 7. Anatomical Structures Affected

- **Primary organ/system:** Skeletal system (UBERON:0001474 bone element; UBERON:0002481 bone tissue). Directly affected sites include the **calvaria/skull (UBERON:0011618 calvaria; UBERON:0000209 cranial bone)**, **vertebral column (UBERON:0001130)**, and **long/tubular bones of the limbs (UBERON:0002495 long bone)** with metaphyseal involvement in the severe subset.
- **Secondary involvement:** Peripheral **nervous system** — facial nerve (UBERON:0001647), causing facial palsy; **eye** (glaucoma, UBERON:0000970); **teeth/dentition** (UBERON:0001091), with caries and hypoplasia.
- **Tissue/cell level:** Connective tissue (bone). Target cells are **osteoblasts (CL:0000062)** and **osteocytes (CL:0000137)**; osteoclasts (CL:0000092) are spared functionally. *SGMS2* is *"prominently expressed in cortical bone."*
- **Subcellular level:** **Endoplasmic reticulum (GO:0005783)** — site of pathogenic SMS2 retention and ectopic sphingomyelin accumulation; **Golgi apparatus/trans-Golgi network (GO:0005802)**; **plasma membrane (GO:0005886)** — the normal SMS2 site of action; the **osteocyte lacunocanalicular network** is structurally disrupted.
- **Localization / lateralization:** Calvarial lesions are typically **multiple and bilateral**; skeletal fragility is generalized/systemic.

### 8. Temporal Development

- **Onset:** Childhood-onset in the milder (p.Arg50\*) form; **neonatal/congenital** onset (neonatal fractures) in the severe CDL-SMD (missense) form. Onset pattern is insidious/chronic.
- **Progression:** Chronic and lifelong. Fracture burden accrues over childhood and adulthood; vertebral compression fractures and scoliosis can progress. Progression rate is variable and correlates with genotype (severe in missense alleles).
- **Disease course:** Progressive/stable skeletal fragility rather than episodic or relapsing–remitting; not self-limited.
- **Critical periods / intervention windows:** Childhood/adolescence, during peak bone accrual, is the key window for anti-osteoporotic intervention (bisphosphonates) to prevent fractures and permit vertebral remodeling — as demonstrated in a pediatric case where compressed vertebrae partially recovered after 2 years of therapy (Zhang 2025).

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (heterozygous *SGMS2* variants).
- **Epidemiology:** Ultra-rare. By 2023, ~15 patients from 8 families had been described in the literature; Merkuryeva et al. added 11 more patients from three families (all p.Arg50\*), for a total of only a few dozen reported cases worldwide. No population prevalence/incidence estimates are available due to rarity.
- **Penetrance / expressivity:** *"These reports further confirm the genetic basis of CDL, the recurrence of the same variant (p.Arg50\*) in individuals of the same ancestry, and the variable penetrance of some of the clinical findings"* ([PMID: 34504906](https://pubmed.ncbi.nlm.nih.gov/34504906/)). Expressivity is **highly variable**, both between and within families.
- **Founder effects:** The recurrent c.148C>T (p.Arg50\*) variant appears in **French-Canadian and French families of shared ancestry**, consistent with a founder allele; the French-Canadian pedigree spans six generations (Basalom 2021).
- **Carrier frequency / consanguinity:** As a dominant disorder, carrier-frequency and consanguinity concepts do not apply in the recessive sense; the three causal alleles are **absent from gnomAD**, indicating they are not present at appreciable frequency in the general population.
- **Population demographics / sex ratio:** No sex predilection has been established (both sexes affected); the best-documented cluster is of French/French-Canadian ancestry, but the disorder is otherwise pan-ethnic.

### 10. Diagnostics

- **Imaging (cornerstone):** Skeletal radiography reveals the pathognomonic **multiple doughnut-shaped (ring-like) sclerotic/hyperostotic calvarial lesions**, generalized osteopenia/low BMD, vertebral compression fractures, "bone-in-bone" vertebrae, metaphyseal undermodeling, and squaring of metacarpals/metatarsals. **DXA** quantifies low BMD (e.g., whole-body BMD Z-score −2.8 in a pediatric case; Zhang 2025).
- **Laboratory:** Serum **alkaline phosphatase may be elevated**. Bone-turnover markers and calcium/phosphate are generally used to exclude other metabolic bone disease.
- **Bone biopsy / histomorphometry:** Transiliac biopsy shows defective mineralization (increased osteoid, prolonged mineralization lag time), low/heterogeneous matrix mineralization on qBEI, chaotic collagen, and disrupted osteocyte lacunocanalicular network — with **normal osteoclast function** ([PMID: 34761145](https://pubmed.ncbi.nlm.nih.gov/34761145/); [PMID: 30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/)).
- **Genetic testing (definitive):** Targeted *SGMS2* single-gene testing or osteoporosis/skeletal-dysplasia gene panels; **whole-exome sequencing (WES)** was the discovery method (Pekkinen 2019). Because the allelic series is very small and clustered, sequencing the exon encoding the N-terminal region of *SGMS2* is high-yield. ClinVar (NM_001375905.1) confirms the three canonical variants as Pathogenic.
- **Clinical criteria / differential diagnosis:** Diagnosis rests on the combination of characteristic calvarial doughnut lesions + bone fragility + *SGMS2* variant. Key differentials: **osteogenesis imperfecta** (CDL is distinct — see below), other early-onset osteoporoses (e.g., *LRP5*, *WNT1*, *PLS3*), and sclerosing bone dysplasias. Nishimura et al. concluded such patients *"may represent a group of fragile bone syndromes which differ from osteogenesis imperfecta"* ([PMID: 8958616](https://pubmed.ncbi.nlm.nih.gov/8958616/)).
- **Screening:** Cascade genetic testing of at-risk relatives is appropriate given autosomal-dominant inheritance and the recurrent founder allele.

### 11. Outcome / Prognosis

- **Survival/mortality:** CDL is **not life-limiting**; no disease-specific mortality is reported. Morbidity, not mortality, dominates the prognosis.
- **Morbidity/disability:** Recurrent fractures, chronic back pain, vertebral compression and scoliosis, short stature (severe subset), facial nerve palsy, and dental problems drive long-term disability and reduced mobility/quality of life.
- **Disease course/complications:** Chronic, lifelong skeletal fragility; complications include vertebral deformity, long-bone deformity requiring surgery in severe cases, and glaucoma/facial palsy requiring specialist care.
- **Recovery potential / prognostic factors:** Genotype is the principal prognostic factor — **missense (ER-retention) alleles predict severe CDL-SMD**, whereas p.Arg50\* predicts milder disease. With bisphosphonate therapy, BMD improves and fractures decrease; vertebral remodeling can occur in growing children (Zhang 2025).

### 12. Treatment

There is **no curative/pathogenetic therapy**; management is symptomatic and aimed at preventing osteoporosis progression and fractures.

| Modality | Details | Suggested NCIT |
|---|---|---|
| Bisphosphonates (first-line) | Pamidronate/other bisphosphonates to increase BMD and reduce fractures | NCIT:C1876 (Bisphosphonate); NCIT:C1350 (Pamidronate) |
| Calcium supplementation | Adjunct to bisphosphonate | NCIT:C376 (Calcium) |
| Vitamin D | Adjunct to support mineralization | NCIT:C904 (Vitamin D) |
| Orthopedic surgery | Management of fractures/deformities in severe cases | NCIT:C15329 (Surgery) |
| Specialist care | Ophthalmology (glaucoma), neurology/ENT (facial palsy), dentistry | — |

**Representative outcome (pediatric case, Zhang 2025, [PMID: 40393762](https://pubmed.ncbi.nlm.nih.gov/40393762/)):** A 7.4-year-old boy with *SGMS2* c.148C>T (p.Arg50\*), scoliosis, multiple vertebral compressions, and whole-body BMD 0.664 g/cm² (Z-score −2.8) was treated with **pamidronate disodium + calcium + vitamin D for 2 years**. Outcome: back pain improved, **no new fractures**, BMD Z-score rose from −2.8 to **+1.3**, and compressed vertebrae partially recovered/remodeled.

**Advanced/experimental therapeutics:** No gene, cell, RNA, targeted, or immunotherapies are approved or in trials for CDL. The gain-of-mislocalization mechanism of the missense alleles suggests that, in principle, allele-specific silencing or strategies to restore ER export could be rational future targets — but none exist today. No pharmacogenomic guidance is established.

### 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (monogenic disease). **Genetic counseling** for affected families is central, given autosomal-dominant inheritance (50% transmission risk) and the recurrent founder allele.
- **Secondary prevention:** Early diagnosis (radiographic + genetic) and early anti-osteoporotic therapy to prevent fractures during the childhood bone-accrual window.
- **Tertiary prevention:** Fracture prevention (bisphosphonates, fall precautions), management of scoliosis/vertebral deformity, and monitoring/treatment of glaucoma and facial nerve palsy.
- **Genetic screening:** Cascade testing of relatives; prenatal/preimplantation genetic testing is theoretically possible for known familial variants. No population newborn/carrier screening is warranted for this ultra-rare dominant disorder.

### 14. Other Species / Natural Disease

No naturally occurring CDL analog has been documented in companion animals or wildlife (no OMIA entry identified). *SGMS2* is evolutionarily conserved; the mouse ortholog is **Sgms2** (see model-organism section). No zoonotic or cross-species transmission applies (this is a genetic, non-communicable disorder). Comparative biology is informative chiefly through mouse genetics of the sphingomyelin-synthase family.

### 15. Model Organisms

The most relevant models are **mouse (Mus musculus, NCBI Taxon:10090)** knockouts of the sphingomyelin-synthase family. A key study revealed an important **isoform-specificity caveat**: Matsumoto et al. 2019 showed that **osteoblast-specific *Sms1* deletion on an *Sms2*-null background** (Sp7-Cre;SMS1^f/f;SMS2^−/−) reduced trabecular and cortical bone mass, lowered BMD, and slowed mineral apposition, and impaired BMP2-induced Smad1/5/8 and p38 signaling during osteoblast differentiation, whereas plain *Sms2*-deficient mice did **not** show this bone-formation deficit ([PMID: 31847800](https://pubmed.ncbi.nlm.nih.gov/31847800/)).

**Model limitation / interpretation:** This means simple *Sms2* knockout mice do **not** faithfully recapitulate human CDL. The discrepancy is mechanistically consistent with the human genetics: human CDL is caused by *SGMS2* (SMS2), and the severe alleles act by **ER-retention (gain of mislocalized activity)**, not by loss of SMS2 function. A faithful mouse model would therefore likely require **knock-in of the missense alleles (e.g., Ile62Ser/Met64Arg)** rather than simple gene deletion. Cellular models exist — **patient-derived fibroblasts** reproduce the disrupted secretory-pathway lipid landscape (Sokoya 2022). Model resources: MGI (mouse *Sgms2*), IMPC/IMSR for knockout lines.

---

## Mechanistic Model / Interpretation

CDL is best understood as a **sphingolipid-membrane–organization disorder of bone-forming cells**, with two mechanistic arms converging on defective mineralization:

```
                    SGMS2 / SMS2 (sphingomyelin synthase 2, chr4q25)
                                   │
        ┌──────────────────────────┴───────────────────────────┐
        │                                                        │
  p.Arg50*  (nonsense)                              p.Ile62Ser / p.Met64Arg (missense)
  Loss of function                                  ER-export signal disrupted
  → catalytically inactive enzyme                   → ACTIVE enzyme trapped in ER
        │                                                        │
  Reduced SM synthesis                              Ectopic SM synthesis in ER;
  (dosage effect; gene is                           disrupted transbilayer SM asymmetry,
   only moderately LOF-constrained,                 altered cholesterol/glycerophospholipid
   pLI≈0.01)                                        distribution & membrane lipid order
        │                                                        │
   MILDER end:                                       SEVERE end (CDL-SMD):
   childhood osteoporosis                            neonatal fractures, severe
   ± cranial sclerosis                               short stature, SMD
        └──────────────────────────┬───────────────────────────┘
                                    ▼
        Loss of the nonrandom secretory-pathway lipid landscape
        that osteoblasts/osteocytes require for bone formation
                                    ▼
        Defective matrix mineralization + chaotic collagen +
        disrupted osteocyte lacunocanalicular network
        (osteoclasts NORMAL)
                                    ▼
        Low BMD · fragile bone · doughnut calvarial lesions
```

The **population-genetic evidence ties the model together**: because *SGMS2* tolerates heterozygous LOF fairly well (pLI≈0.01, LOEUF≈0.69), pure haploinsufficiency produces the milder end, while the **severe phenotype requires the toxic, active-but-mislocalized enzyme**. The absence of all three causal alleles from ~1.6M gnomAD alleles confirms their pathogenic, non-polymorphic nature and distinguishes them from nearby tolerated variants (e.g., p.Arg50Gln, present at AF≈9×10⁻⁶). This model explains the genotype–phenotype gradient, the normal osteoclast biology, and why simple *Sms2*-knockout mice fail to reproduce the disease.

---

## Evidence Base

| PMID | Paper (abbrev.) | Role / support |
|---|---|---|
| [30779713](https://pubmed.ncbi.nlm.nih.gov/30779713/) | Pekkinen 2019 — *Osteoporosis and skeletal dysplasia caused by pathogenic variants in SGMS2* | **Landmark discovery.** Establishes *SGMS2* as causal gene, the three canonical variants, the LOF-vs-ER-retention dichotomy, genotype–phenotype gradient, normal osteoclasts, and facial-nerve palsy. Supports F001, F002, F003, F004. |
| [36102623](https://pubmed.ncbi.nlm.nih.gov/36102623/) | Sokoya 2022 (eLife) — *Pathogenic variants of SMS2 disrupt lipid landscapes in the secretory pathway* | **Core mechanism.** Shows severe alleles retain activity but are ER-retained; disrupted SM asymmetry and secretory-pathway lipid landscape; links to impaired osteogenic bone formation. Supports F005. |
| [34761145](https://pubmed.ncbi.nlm.nih.gov/34761145/) | Mäkitie 2021 (JBMR Plus) — bone tissue organization/osteocyte network | **Tissue-level pathology.** Quantitative histomorphometry/qBEI documenting the mineralization defect, chaotic collagen, disrupted lacunocanalicular network in p.Arg50\* patients. Supports F006. |
| [37175737](https://pubmed.ncbi.nlm.nih.gov/37175737/) | Merkuryeva 2023 — three families with recurrent variant | **Disease definition & recurrence.** Provides disease definition, MIM number, inheritance, phenotypic variability, and SM's role in mineralization. Supports F007, F006. |
| [34504906](https://pubmed.ncbi.nlm.nih.gov/34504906/) | Basalom 2021 — French-Canadian family | **Founder allele & penetrance.** Documents recurrence of p.Arg50\* in shared ancestry and variable penetrance. Supports F007. |
| [8958616](https://pubmed.ncbi.nlm.nih.gov/8958616/) | Nishimura 1996 — original clinical description | **Historical/differential.** Establishes CDL as distinct from osteogenesis imperfecta. Supports F003. |
| [40393762](https://pubmed.ncbi.nlm.nih.gov/40393762/) | Zhang 2025 — pamidronate pediatric case | **Treatment outcome.** Documents bisphosphonate efficacy (BMD Z-score −2.8→+1.3, no new fractures, vertebral remodeling). Supports F008. |
| [31847800](https://pubmed.ncbi.nlm.nih.gov/31847800/) | Matsumoto 2019 (Mol Med) — mouse Sms1/Sms2 | **Model organism caveat.** SMS1 (not SMS2) loss impairs osteoblast differentiation via BMP2–Smad/p38; explains why Sms2-KO mice don't model CDL. Supports F009. |
| 38388831 | Hu 2024 (Nat Struct Mol Biol) — SMSr cryo-EM | **Protein structure.** Multi-TM fold with catalytic pentad; contextualizes clustering of disease residues near N-terminal ER-export region. Supports F011. |

The evidence base is internally consistent: independent human genetic, cellular (patient fibroblast/heterologous expression), and bone-histology studies all converge on a mineralization defect driven by mislocalized/lost sphingomyelin-synthase activity, with population-genetic constraint data corroborating the mechanistic interpretation.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity limits epidemiology.** Only a few dozen patients from ~8–11 families are reported; there are no reliable prevalence/incidence figures, no sex-ratio data, and no formal quality-of-life (EQ-5D/SF-36/PROMIS) studies.
2. **Small allelic series.** Essentially three pathogenic variants define the disease; genotype–phenotype conclusions rest on limited numbers, and the ~200 *SGMS2* ClinVar entries are dominated by VUS.
3. **No faithful animal model.** *Sms2*-knockout mice do not recapitulate CDL; the required knock-in missense models (Ile62Ser/Met64Arg) have not been reported, limiting mechanistic and preclinical therapeutic work.
4. **Mechanistic granularity.** How disrupted secretory-pathway lipid distribution mechanistically produces both osteopenia (fragility) and focal calvarial hyperostosis (doughnut lesions) in the same patient remains incompletely explained.
5. **Treatment evidence is anecdotal.** Bisphosphonate efficacy is supported by case reports, not controlled trials; long-term outcomes and optimal regimens are undefined. No disease-modifying therapy exists.
6. **Neurological and ocular features** (facial palsy, glaucoma) are described but their frequency, natural history, and mechanistic link to sphingomyelin biology are not quantified.

---

## Proposed Follow-up Experiments / Actions

1. **Generate knock-in mouse models** of p.Ile62Ser and p.Met64Arg (and a p.Arg50\* LOF line) to test the ER-retention/gain-of-mislocalization hypothesis in vivo and provide a preclinical platform. Compare to conditional osteoblast/osteocyte-specific lines.
2. **Osteoblast/osteocyte-specific lipidomics and imaging** (patient iPSC-derived osteogenic cells and organoids) to map how ER-retained SMS2 remodels the secretory-pathway lipid gradient and to identify the mineralization step that fails.
3. **Establish an international CDL registry** to aggregate genotype, radiographic phenotype, fracture history, treatment response, and neurological/ocular features — enabling proper penetrance/expressivity and natural-history quantification.
4. **Controlled/observational treatment studies** of bisphosphonates (± other anti-osteoporotics) in CDL to define efficacy, dosing, and long-term skeletal outcomes.
5. **Allele-specific therapeutic exploration** for the toxic missense alleles (e.g., allele-selective ASO/siRNA silencing, or chemical chaperones/ER-export modulators to relieve mislocalization).
6. **Functional reclassification of *SGMS2* VUS** using the ER-export/enzymatic assays established by Sokoya 2022, to triage the many VUS in ClinVar and refine diagnostic yield.
7. **Deep phenotyping of facial nerve palsy and glaucoma** across the cohort to determine frequency, onset, and whether these track with genotype or sphingomyelin dysregulation in neural/ocular tissue.

---

*Report compiled from 13 confirmed findings across 5 investigation iterations; 10 primary papers reviewed. Evidence types span human clinical genetics, patient-derived cellular assays, bone histomorphometry, mouse genetics, and population-genomic constraint analysis.*


## Artifacts

- [OpenScientist final report](Calvarial_Doughnut_Lesions-bone_Fragility_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Calvarial_Doughnut_Lesions-bone_Fragility_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.