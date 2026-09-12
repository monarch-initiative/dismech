---
provider: perplexity
model: sonar-deep-research
cached: true
start_time: '2026-08-29T19:51:26.132574'
end_time: '2026-08-29T19:51:26.137113'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Shashi-Pena Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 96
  verified: 87
  not_found: 2
  obsolete: 5
  unverifiable: 2
  confabulation_rate: 0.021
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: UBERON:0004288
    reported_labels:
    - vertebral column
    ontology_label: skeleton
  - term_id: UBERON:0008896
    reported_labels:
    - skeleton
    ontology_label: post-hyoid pharyngeal arch
  - term_id: NCIT:C48920
    reported_labels:
    - Cardiac Surgery
    ontology_label: Quantile
  - term_id: NCIT:C49997
    reported_labels:
    - Cardiac Catheterization
    ontology_label: Imager Device
  - term_id: NCIT:C17956
    reported_labels:
    - Prenatal Genetic Testing
    ontology_label: Cytochrome P450 19A1
  - term_id: NCIT:C18189
    reported_labels:
    - Preimplantation Genetic Diagnosis
    ontology_label: Pathology
  labels_variant: 1
  unresolved_terms:
  - HP:0000724
  - NCIT:C47233
  obsolete_terms:
  - term_id: GO:0016585
    ontology_label: obsolete chromatin remodeling complex
  - term_id: GO:0031060
    ontology_label: obsolete regulation of histone methylation
  - term_id: CL:0000664
    ontology_label: obsolete closable valve cell
    replaced_by: CL:1000147
  - term_id: CL:0000672
    ontology_label: obsolete tracheary element
    replaced_by: PO:0000290
  - term_id: NCIT:C17956
    ontology_label: Cytochrome P450 19A1
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Shashi-Pena Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Shashi-Pena Syndrome** covering all of the
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

# Shashi-Pena Syndrome: Comprehensive Disease Characteristics and Mechanistic Overview

Shashi-Pena syndrome (SHAPNS) is an ultra-rare, autosomal dominant neurodevelopmental and multiple malformation syndrome caused by heterozygous disruption of the *ASXL2* gene, an epigenetic regulator belonging to the additional sex combs-like family of Polycomb/Trithorax-related proteins.[1][9][13] Clinically, SHAPNS is characterized by a recognizable pattern of craniofacial dysmorphism, congenital macrocephaly, hypotonia, global developmental delay or intellectual disability, seizures, episodic hypoglycemia, congenital heart disease, and a distinctive glabellar nevus flammeus, alongside highly variable involvement of growth, behavior, endocrinologic and dental features.[1][9][11] At the molecular level, the disorder is almost invariably associated with germline de novo truncating variants in *ASXL2* and, more rarely, structural rearrangements that disrupt *ASXL2* expression; functional evidence from human genetics and murine models indicates that these lesions result in loss of function of ASXL2, altered recruitment of Polycomb repressive complex 2, perturbation of histone H3K27 methylation, and widespread dysregulation of developmental gene expression.[13][14][15] As of 2023, approximately 23 individuals have been described in the medical literature, with patient-advocacy estimates of 50–60 diagnosed cases worldwide, underscoring the extreme rarity of this condition and the early stage of natural history and mechanistic characterization.[1][10] This report synthesizes the current knowledge on SHAPNS across clinical, genetic, molecular, anatomical, temporal, epidemiologic, diagnostic, prognostic, therapeutic, preventive, and model organism domains, with explicit mapping to key biomedical ontologies (MONDO, HPO, GO, CL, UBERON, CHEBI, NCIT) and integration of primary literature from human case series, mechanistic in vitro studies, and *Asxl2* animal models.[1][9][11][13][14][15]  

## 1. Disease Information

### 1.1. Definition and Concise Overview

Shashi-Pena syndrome is a Mendelian neurodevelopmental disorder defined by a constellation of congenital craniofacial, neurologic, metabolic, and cardiac manifestations attributable to heterozygous pathogenic variants in *ASXL2*.[1][9][13] The clinical phenotype was first formally delineated in 2016 by Shashi, Peña and colleagues, who identified six unrelated individuals with de novo truncating variants in *ASXL2* through the Undiagnosed Diseases Network and recognized a consistent pattern of macrocephaly, arched eyebrows, hypertelorism, prominent eyes, feeding difficulties, hypotonia, developmental delay, and episodic hypoglycemia.[13][8] Subsequent reports have expanded the spectrum to include cerebral atrophy, minor congenital heart disease, neonatal hypoglycemia, seizures, and, in some individuals, postnatal overgrowth, dental anomalies, and atypically mild neurodevelopmental impairment.[9][11] Clinically, SHAPNS is often suspected on the basis of macrocephaly, developmental delay, hypotonia, seizures, and a distinctive facial gestalt with glabellar nevus flammeus, and is confirmed by identification of a pathogenic *ASXL2* variant via exome sequencing or targeted gene analysis.[1][9][11][13] In contemporary classification, SHAPNS is recognized as a rare autosomal dominant multiple malformation and neurodevelopmental syndrome within the broader group of ASXL-related disorders, which also includes Bohring-Opitz syndrome (*ASXL1*) and Bainbridge-Ropers syndrome (*ASXL3*).[8][13][15]

From a nosologic standpoint, Shashi-Pena syndrome is catalogued among rare congenital disorders and neurodevelopmental syndromes, often grouped with overgrowth conditions with macrocephaly and epigenetic regulator disorders.[9][13] GeneReviews describes SHAPNS as a clinically recognizable neurodevelopmental syndrome characterized by macrocephaly, developmental delay, seizures, hypotonia, hypoglycemia, distinctive facial features, and a glabellar nevus flammeus, succinctly capturing its core phenotype.[16][1][9] The NORD entry emphasizes that the syndrome presents at birth with multiple malformations, including facial differences, enlarged head circumference, low muscle tone, global developmental delay, congenital heart disease, and sometimes epilepsy.[1] Orphanet has registered Shashi-Pena syndrome under ORPHA:689408 and notes that its summary is under development, reflecting the recent recognition and limited epidemiologic data.[6] Taken together, this body of evidence supports classification of SHAPNS as a well-defined but extremely rare Mendelian disorder with a recognizable phenotype and a shared molecular etiology centered on *ASXL2* haploinsufficiency.[1][6][9][13]

### 1.2. Key Identifiers and Ontology Mapping

Shashi-Pena syndrome is associated with several standardized disease identifiers across major biomedical databases, facilitating cross-resource integration. The Online Mendelian Inheritance in Man (OMIM) database lists SHAPNS under entry number 617190, denoted as “SHASHI-PENA SYNDROME; SHAPNS.”[5][13] Orphanet assigns the identifier ORPHA:689408 to Shashi-Pena syndrome, acknowledging its status as a rare disease with ongoing data curation.[6] The Monarch Initiative, which harmonizes multiple ontologies, maps Shashi-Pena syndrome to MONDO:0014963, thereby providing a cross-ontology disease concept accessible via the MONDO ontology and linking to associated phenotypes and genes.[12] These identifiers, including OMIM:617190, ORPHA:689408, and MONDO:0014963, anchor SHAPNS within standardized disease taxonomies useful for knowledge bases, clinical decision support, and computational analyses.[5][6][12]

In addition to disease-level ontologies, Shashi-Pena syndrome is linked to MeSH and SNOMED CT concepts in broader categories of “Congenital Abnormalities,” “Neurodevelopmental Disorders,” and “Epigenetic Diseases,” although specific MeSH headings uniquely labeled “Shashi-Pena syndrome” are not yet widely indexed given the syndrome’s recent delineation and rarity.[5][7] ICD-10 and ICD-11 do not, at present, contain a unique code specific to SHAPNS, and affected individuals are typically coded under broader categories such as Q99.9 (Chromosomal abnormality, unspecified), Q87 (Other specified congenital malformation syndromes), or F88 (Other disorders of psychological development), depending on national coding practices.[5][1] For internal ontology mapping, Shashi-Pena syndrome can be annotated as a Mendelian disorder using the “Mendelian disease” category within MONDO and as an “autosomal dominant disease” concept, alongside mapping to the Human Phenotype Ontology (HPO) terms for its core clinical features, which are detailed below.[12][7] 

### 1.3. Synonyms and Alternative Names

Because Shashi-Pena syndrome has emerged relatively recently in the medical literature, a limited but important set of synonyms and alternative names is in use. The syndrome is most often referred to as “Shashi-Pena syndrome,” reflecting the names of Vandana Shashi and Loren Peña, the physicians who led the original description of affected individuals through the Undiagnosed Diseases Network.[8][13] Frequently used abbreviations include “SHAPNS” and “SPS,” which are common in clinical and patient advocacy documents.[8][9][10] The Ma’ayan Lab Harmonizome resource, which aggregates functional gene associations, lists “SHAPNS” as a synonym for the gene-centered phenotype associated with *ASXL2* truncating variants, reinforcing usage of this acronym in computational biology contexts.[4] In some contexts, SHAPNS is described simply as “ASXL2-related syndrome” or “ASXL2-related Shashi-Pena syndrome,” particularly in molecular reports emphasizing the gene rather than the eponymous name.[11][14]

These naming conventions coexist with a broader category of “ASXL-related disorders,” a term that encompasses Bohring-Opitz syndrome (*ASXL1*), Shashi-Pena syndrome (*ASXL2*), and Bainbridge-Ropers syndrome (*ASXL3*).[8][15] Within this grouping, SHAPNS is sometimes labeled “ASXL2-associated neurodevelopmental syndrome” in mechanistic and review articles, especially those focusing on functional roles of ASXL proteins in development and cancer.[15][13] For ontology-based knowledge bases, the principal preferred label should be “Shashi-Pena syndrome,” with recognized synonyms “SHAPNS,” “SPS,” and “ASXL2-related Shashi-Pena syndrome,” and cross-reference to “ASXL-related disorders” as a broader disease family concept.[4][8][13]

### 1.4. Source of Information: Patient-Level vs Aggregated Disease-Level Resources

Current knowledge of Shashi-Pena syndrome arises from a combination of individual patient case reports and small series in the medical literature, aggregated disease-level resources such as OMIM, NORD, and GeneReviews, and patient advocacy registries managed by organizations like the ASXL Rare Research Endowment (ARRE) Foundation.[1][8][9][11][13][16] The initial description by Shashi et al. in 2016 was based on six unrelated individuals identified through the Undiagnosed Diseases Network, representing a deeply phenotyped cohort with extensive genetic analysis, imaging, and longitudinal follow-up.[13] Subsequent clinical case reports and series, including a newborn with an ASXL2 truncating variant, a Chinese individual with a novel nonsense variant and premature death, a family with balanced translocation disrupting *ASXL2*, and an adolescent with overgrowth and dental anomalies, have added nuance and expanded the clinical spectrum.[3][9][11][14]

Aggregated resources such as OMIM and GeneReviews synthesize these case-level data into structured disease descriptions, summarizing cardinal features, inheritance patterns, genetic testing recommendations, and management considerations.[5][16] NORD and ARRE provide accessible summaries aimed at patients and families, integrating medical literature with patient-reported experiences and registry-based estimates of prevalence and clinical variability.[1][8][10] According to NORD, as of 2023, approximately 23 individuals with SHAPNS have been identified in the medical literature; ARRE estimates that 50–60 people have been diagnosed globally when including individuals known to patient organizations but not yet reported formally in peer-reviewed publications.[1][10] These numbers highlight the reliance on both published case series and advocacy-driven registries for characterizing ultra-rare disorders such as SHAPNS. As more individuals are recognized through exome sequencing, it is expected that disease-level resources will increasingly reflect a broader and more representative phenotype distribution, but current knowledge remains heavily shaped by a relatively small set of intensively documented cases.[1][9][11][13][16]

## 2. Etiology

### 2.1. Primary Disease Causal Factors

The primary causal factor in Shashi-Pena syndrome is germline heterozygous disruption of the *ASXL2* gene, most commonly through truncating sequence variants and more rarely through structural chromosomal rearrangements that interrupt gene integrity or reduce expression.[1][9][11][13][14] ASXL2 (additional sex combs like transcriptional regulator 2), encoded at chromosome 2p23.3, is one of three mammalian ASXL family members that function as epigenetic scaffolding proteins, interacting with Polycomb group (PcG) and Trithorax group (TrxG) complexes to regulate histone methylation and transcriptional programs essential for embryonic development and body patterning.[4][15][14] The seminal AJHG study by Shashi et al. identified de novo truncating variants in *ASXL2* in six unrelated individuals, and concluded that “de novo truncating variants in ASXL2 underlie a neurodevelopmental syndrome with a clinically recognizable phenotype,” establishing a causal relationship between *ASXL2* loss-of-function and the SHAPNS phenotype.[13]

Most reported pathogenic variants in SHAPNS are nonsense or frameshift variants predicted to lead to premature termination of the protein, typically within the middle or C-terminal exons, and are classified as loss-of-function alleles according to ACMG/AMP criteria.[3][11][13][14] For example, Yuan et al. identified a heterozygous de novo truncating c.1792C>T (p.Gln598*) variant in exon 11 of *ASXL2* in a newborn presenting with typical SHAPNS features; trio whole-exome sequencing confirmed the variant’s de novo origin and pathogenic status.[11] Another report described a Chinese patient harboring a novel heterozygous nonsense variant (c.2485G>T, p.Gly829*) associated with Shashi-Pena syndrome, representing the first documented case of premature death linked to SHAPNS in a Chinese demographic.[3] A Neurology Genetics study identified SHAPNS in three members of a Chinese family with a balanced translocation t(2;11)(p23.3;q22.1) that disrupted *ASXL2*, demonstrating that complex structural variants can also cause the syndrome by reducing *ASXL2* mRNA expression.[14] Collectively, these findings demonstrate that SHAPNS is mechanistically rooted in *ASXL2* haploinsufficiency rather than missense gain-of-function, with *ASXL2* acting as a dosage-sensitive gene in neurodevelopment.[13][14][15]

Environmental, infectious, or purely mechanistic non-genetic etiologies have not been implicated as primary causes of Shashi-Pena syndrome. All reported individuals either harbor de novo germline *ASXL2* variants or segregating structural rearrangements affecting *ASXL2*, and no cases have been attributed to environmental exposures or acquired somatic mutations alone.[1][3][11][13][14] Nevertheless, the epigenetic regulatory function of ASXL2 suggests that external environmental factors could modulate phenotypic expression via downstream pathways, although direct evidence for such gene–environment interactions in SHAPNS is currently lacking.[15] 

### 2.2. Genetic Risk Factors: Causal Variants, Susceptibility Loci, and Modifier Genes

The principal genetic risk factor for Shashi-Pena syndrome is the presence of a heterozygous pathogenic variant in *ASXL2*, usually truncating, with high penetrance for the core phenotype.[1][9][11][13][14] Germline de novo variants account for the majority of reported cases; NORD emphasizes that all *ASXL2* variants described in the literature to date were de novo, meaning neither parent carries the variant, though ARRE notes rare instances of inherited variants in families documented through patient advocacy channels.[1][8][10] In the balanced translocation family reported by Neurology Genetics, three affected members (proband, father, grandmother) carried a complex chromosomal rearrangement t(2;11)(p23.3;q22.1) that disrupted *ASXL2* and led to decreased mRNA expression, indicating autosomal dominant transmission of a structural variant with SHAPNS phenotype.[14] Similarly, the Mol Syndromol case of a 15-year-old with overgrowth and minor neurodevelopmental features harbored a novel heterozygous *ASXL2* variant identified through molecular diagnostics.[9]

Variant classification according to ACMG/AMP guidelines in ClinVar and GeneReviews generally designates these truncating variants as pathogenic or likely pathogenic, given their predicted loss-of-function effect, absence in population databases such as gnomAD, and consistent genotype–phenotype correlation.[13][16] The Gene Mutation database cited in the SciDirect case report lists 12 different *ASXL2* mutations, 11 of which are associated with neurodevelopmental disorders, indicating a concentration of pathogenic alleles in exons critical for ASXL2 interaction with histone-modifying enzymes.[3] Allele frequency data in gnomAD and ExAC for these specific truncating variants are typically zero, consistent with strong purifying selection against *ASXL2* haploinsufficiency in the general population; ASXL2 is considered highly constrained, with loss-of-function variants essentially absent in large population cohorts.[4][15]

To date, no susceptibility loci or modifier genes have been definitively identified that alter risk of SHAPNS in the absence of *ASXL2* disruption. The small number of cases and strong Mendelian penetrance limit the ability to detect common variants modulating disease risk. However, the clinical variability observed among individuals with similar truncating variants suggests that genetic modifiers may influence expressivity, particularly in domains such as overgrowth, seizure frequency, and cognitive outcome.[9][11] In mice, postnatal deletion of *Asxl2* produces hematopoietic defects and cytopenias more severe than those seen with *Asxl1* deletion, implying that tissue-specific genetic backgrounds and interacting transcription factors may modulate phenotypic consequences of *ASXL2* loss.[15] No specific human modifier genes have been proposed for SHAPNS, though candidate pathways include those encoding Polycomb complex proteins (e.g., EZH2) and Trithorax group members (e.g., MLL family), which interact with ASXL2 in chromatin regulation.[15]

### 2.3. Environmental Risk Factors and Lifestyle Influences

Given the clearly established Mendelian etiology centered on *ASXL2* haploinsufficiency, Shashi-Pena syndrome is not currently considered to be driven by environmental risk factors such as toxins, radiation, or infectious agents.[1][3][11][13][14] No epidemiologic studies have suggested increased incidence in populations with particular environmental exposures, and the few reported familial cases are best explained by inherited chromosomal rearrangements rather than shared environmental triggers.[14] Nonetheless, environment may shape clinical trajectory and severity, particularly through interactions with metabolic or endocrine pathways; for example, nutritional status and access to medical care could influence outcomes related to hypoglycemia, feeding difficulties, and growth, but these are secondary modifiers rather than primary causes.[1][11][16]

Lifestyle factors such as smoking, diet, alcohol consumption, and exercise have not been studied in relation to SHAPNS risk or severity, and their contribution remains speculative. The syndrome manifests in infancy and childhood, typically due to constitutional germline variants; lifestyle factors of the proband play little role in initial disease onset, although parental exposures may theoretically have minor effects on germline mutation risk, a question that is largely unexplored and likely negligible compared to stochastic mutational processes.[1][13][14] Within the context of disease management, lifestyle adaptations—such as dietary optimization, physical therapy, and behavioral interventions—are relevant for quality of life but do not alter the underlying genetic etiology.[1][10][16] 

### 2.4. Protective Factors and Gene–Environment Interactions

No genetic protective variants or alleles have been reported that reduce risk of Shashi-Pena syndrome or mitigate its severity in carriers of pathogenic *ASXL2* variants. Given the rarity of the disorder and the near-complete penetrance of core features reported in most cases, the identification of protective alleles would require large cohorts and systematic genotype–phenotype correlation analyses, which are currently unavailable.[1][9][11][13] Similarly, environmental factors that confer protection, such as particular diets or exposures that could attenuate epigenetic dysregulation downstream of ASXL2 loss, have not been documented in clinical case series or experimental models.[15]

Gene–environment interactions in SHAPNS remain speculative but conceptually plausible, especially in light of ASXL2’s role as an epigenetic regulator responsive to cellular signaling. The ASXL family integrates PcG and TrxG activities that respond to developmental cues and metabolic states; thus, it is reasonable to hypothesize that environmental influences such as nutritional status, endocrine milieu, or stress hormones could shape the epigenetic landscape in ASXL2-deficient tissues.[15] Murine *Asxl2* models reveal systemic phenotypes including lipodystrophy, insulin resistance, and reduced bone mineral density, indicating that metabolic environment interacts with ASXL2-dependent transcriptional programs.[15] In humans, the recurrent observation of episodic hypoglycemia and feeding difficulties in SHAPNS suggests altered metabolic regulation, potentially modifiable by careful dietary management; however, direct evidence for specific gene–environment interaction mechanisms is lacking, and no controlled interventional studies have been conducted.[1][9][11][16]

At present, therefore, the etiologic landscape of Shashi-Pena syndrome is dominated by a single, strong genetic causal factor—*ASXL2* haploinsufficiency—with minimal evidence for non-genetic risk factors, protective factors, or well-characterized gene–environment interactions. Future studies leveraging larger registries and multi-omics datasets may reveal modifiers and interactions, but current knowledge supports modeling SHAPNS as a predominantly monogenic, highly penetrant disorder for the purposes of disease knowledge bases.[1][9][11][13][15][16]

## 3. Phenotypes

### 3.1. Overall Clinical Spectrum and Core Features

The phenotype of Shashi-Pena syndrome encompasses a broad range of symptoms, clinical signs, physical manifestations, behavioral changes, and occasional laboratory abnormalities, which together form a recognizable syndrome with substantial inter-individual variability.[1][9][11][13][16] Key clinical domains include craniofacial features (macrocephaly, facial differences), neurodevelopmental impairment (global developmental delay, intellectual disability, speech delay), neuromuscular findings (hypotonia, seizures), metabolic disturbances (episodic hypoglycemia), congenital heart disease, distinctive cutaneous lesions (glabellar nevus flammeus or simplex), orthopedic complications, oral and dental anomalies, behavioral and sensory challenges, and gastrointestinal issues such as constipation.[1][9][10][11][17] NORD summarizes that characteristics present at birth include facial differences, enlarged head circumference, a birthmark above the bridge of the nose, low muscle tone, and global developmental delay, with epilepsy occurring in some but not all affected individuals.[1] The ARRE Foundation similarly highlights common features including large head, wide-set eyes, low-set ears, birthmarks, hypotonia, developmental delay, difficulty controlling blood sugar, orthopedic complications, heart defects, behavioral and sensory challenges, constipation, and seizures, while stressing wide variation in features and abilities among individuals.[10]

Human Phenotype Ontology (HPO) terms that map to these features include macrocephaly (HP:0000256), glabellar nevus flammeus (often subsumed under capillary malformation or “nevus flammeus,” HP:0001050), hypertelorism (HP:0000316), arched eyebrows (potentially HP:0002553 for abnormal eyebrow morphology), prominent eyes (HP:0000520), developmental delay (HP:0001263), intellectual disability (HP:0001249), neonatal hypotonia (HP:0001319), seizures (HP:0001250), hypoglycemia (HP:0001943), congenital heart disease (HP:0001627), cerebral atrophy (HP:0002059), overgrowth (HP:0001513), dental anomalies (such as malocclusion, HP:0000324), constipation (HP:0002019), and behavioral abnormalities (HP:0000708).[7][9][11][17] Age of symptom onset for most features is neonatal or early infancy, as macrocephaly, facial differences, hypotonia, feeding difficulties, and hypoglycemia are typically evident shortly after birth.[1][11][16] Neurodevelopmental delay becomes apparent over the first few years of life, and seizures may emerge in infancy or childhood; dental anomalies and behavioral challenges are most evident in later childhood or adolescence.[9][11][17] Symptom severity is variable across individuals, ranging from mild neurodevelopmental impairment with normal cognition in some to moderate or severe intellectual disability and refractory epilepsy in others.[9][13][16] Symptom progression is generally non-progressive in terms of malformations, but neurodevelopmental manifestations and behavioral patterns can evolve over time, and metabolic or cardiac complications may emerge episodically.[1][9][11][16]

The quality of life impact of SHAPNS is significant, as core features affect daily functioning, independence, and participation in education and social activities. Developmental delay and hypotonia can limit motor skills, communication, and academic performance; seizures and hypoglycemia pose acute health risks and require ongoing monitoring; congenital heart disease may necessitate cardiology follow-up and occasional interventions; and behavioral challenges and sensory sensitivities can affect family dynamics and social integration.[1][10][16] However, individual trajectories vary widely: ARRE notes that “the features and abilities of people with Shashi-Pena Syndrome varies greatly. We do not yet know why there is a broad spectrum of features and abilities,” reflecting both variable expressivity and incomplete penetrance of certain features.[10][9][11] As more data accumulate, quality of life assessments using instruments such as EQ-5D or SF-36 could provide quantitative measures, but such studies have not yet been systematically performed in SHAPNS cohorts.[1][10][16]

### 3.2. Neurodevelopmental and Neurological Phenotypes

Neurodevelopmental impairment is among the most prominent phenotypic domains in Shashi-Pena syndrome. Global developmental delay is reported in the majority of individuals, affecting motor, language, and cognitive milestones.[1][9][11][13][16] Intellectual disability is common, usually in the mild to moderate range, although Mol Syndromol describes a 15-year-old patient with “minor neurodevelopmental problems” and overgrowth, indicating that cognitive impairment can be surprisingly mild in some cases.[9] Speech delay and language deficits are frequently reported, with some individuals achieving functional language and others remaining nonverbal or using augmentative communication.[1][9][11][13] Hypotonia is consistently described in neonatal and early childhood periods and may persist, contributing to motor delay, gait abnormalities, and fatigue.[1][9][11][13]

Seizures represent a major neurologic phenotype, though not universally present. NORD notes that “certain features such as epilepsy occur in some affected individuals, but not all,” indicating incomplete penetrance.[1] Reported seizure types include generalized tonic-clonic seizures, focal seizures, and infantile spasms, with variable response to antiepileptic medications.[1][9][11][13] In the Yuan newborn case, seizures and cerebral atrophy were part of the clinical presentation, consistent with prior reports emphasizing neurologic manifestations.[11] EEG findings are not exhaustively detailed in the available literature, but abnormal cerebral activity is often implied by seizure presence. Cerebral atrophy on neuroimaging has been observed in several individuals, suggesting an underlying structural basis for neurologic symptoms, though the extent and pattern of brain involvement remain incompletely characterized.[11][13]

HPO terms relevant to these neurodevelopmental and neurologic features include global developmental delay (HP:0001263), intellectual disability (HP:0001249), speech delay (HP:0000750), hypotonia (HP:0001252), seizures (HP:0001250), cerebral atrophy (HP:0002059), and abnormal EEG (HP:0002353).[7][11][13] Age of onset for developmental delay and hypotonia is infancy; seizures may begin in infancy or childhood, and cerebral atrophy is detectable via imaging when performed.[11][13] Symptom severity ranges from mild developmental delay with no seizures to severe intellectual disability with refractory epilepsy; progression in neurodevelopmental impairment is often stabilizing rather than degenerative, though cognitive and behavioral challenges may become more apparent with age as developmental expectations increase.[1][9][11][16] Quality of life impact is high, as neurodevelopmental impairments affect autonomy, learning, and social relationships, and seizures impose significant medical and psychosocial burdens.[1][10][16]

From a mechanistic perspective, these neurodevelopmental features are consistent with ASXL2’s role in brain development and epigenetic regulation of neuronal gene expression. ASXL2 interacts with Polycomb repressive complex 2 to control H3K27me3 deposition at select targets; disruption of this regulatory network could alter expression of HOX genes and other developmental transcription factors influencing brain patterning, synapse formation, and neuronal maturation.[15][14] In *Asxl2* knockout mice, alterations of the axial skeleton and congenital heart malformations are prominent, but specific neurodevelopmental phenotypes have not been fully reported, highlighting a need for focused neurobehavioral characterization.[15] Clinical observations in SHAPNS provide strong evidence that ASXL2 is essential for normal brain development in humans, and that its haploinsufficiency leads to a spectrum of neurodevelopmental impairment and epilepsy.[13][14]

### 3.3. Craniofacial, Growth, and Dermatologic Phenotypes

Craniofacial features and growth abnormalities are central to the clinical recognition of Shashi-Pena syndrome. Macrocephaly, defined as an occipitofrontal circumference significantly above age- and sex-adjusted norms, is a near-universal feature and often presents at birth.[1][9][11][13][16] Facial differences, including hypertelorism (widely spaced eyes), arched eyebrows, prominent eyes, low-set ears, and midface hypoplasia, contribute to a distinctive facial gestalt recognizable to experienced clinicians.[1][9][11][13] A glabellar nevus flammeus or nevus simplex—a reddish capillary birthmark above the bridge of the nose—is highlighted as a characteristic finding in NORD and multiple case reports, often persisting as a subtle mark beyond infancy.[1][9][11] ARRE similarly emphasizes birthmarks as part of the phenotype, noting that people with SHAPNS often have large heads and wide-set eyes.[10]

Growth phenotypes in SHAPNS are variable. While macrocephaly is consistent, stature and weight may range from normal to overgrowth, with Mol Syndromol specifically describing “marked postnatal overgrowth without advanced bone age” in a 15-year-old patient, leading authors to propose inclusion of SHAPNS among overgrowth disorders with macrocephaly.[9] Some individuals demonstrate normal growth parameters, whereas others exhibit tall stature and increased weight relative to age norms, with no evidence of precocious skeletal maturation.[9][11] Murine *Asxl2* gene-trap mutants exhibit reduced body weight and lipodystrophy, underscoring potential differences between murine and human phenotypic expression of ASXL2 deficiency and suggesting tissue- and species-specific influences on growth outcomes.[15]

Cutaneous manifestations beyond the glabellar nevus flammeus are less systematically described but may include other capillary malformations, pigmentary anomalies, or birthmarks on the face and body.[1][9][10] HPO terms relevant to craniofacial and growth features include macrocephaly (HP:0000256), hypertelorism (HP:0000316), arched eyebrows (HP:0002553), prominent eyes (HP:0000520), low-set ears (HP:0000369), glabellar nevus flammeus (mapped under capillary malformation, HP:0001050), facial dysmorphism (HP:0001999), overgrowth (HP:0001513), and abnormal growth velocity (HP:0001507).[7][9][11] Age of onset for these features is congenital; macrocephaly and facial gestalt are present at birth, and overgrowth can emerge postnatally, especially during childhood.[9][11][16] Severity varies: macrocephaly may be mild or pronounced; facial features may be subtle or striking; overgrowth may be moderate or severe. These phenotypes can have psychosocial impacts related to body image and social perception, but their direct functional impact is often less than that of neurodevelopmental features.[1][10]

The causal chain from ASXL2 loss-of-function to craniofacial and growth phenotypes likely involves misregulation of HOX clusters and other developmental genes controlling cranial vault formation, facial morphogenesis, and endocrine signaling. ASXL family proteins regulate the balance of PcG and TrxG activities, modulating gene expression patterns that specify anterior–posterior and dorsal–ventral axis identity.[15][14] In *Asxl2* knockout mice, alterations of the axial skeleton and congenital heart malformations reflect disrupted body patterning; analogous mechanisms in humans may contribute to macrocephaly and facial dysmorphism in SHAPNS.[15][13] Overgrowth could result from altered regulation of growth factor signaling pathways, such as IGF or mTOR, influenced by epigenetic changes in ASXL2-deficient tissues, although direct evidence for specific pathways in SHAPNS remains to be fully elucidated.[9][15]

### 3.4. Metabolic, Endocrine, and Cardiovascular Phenotypes

Metabolic and endocrine abnormalities, particularly episodic hypoglycemia and difficulty controlling blood sugar, are prominent in Shashi-Pena syndrome and contribute to acute clinical morbidity.[1][9][10][11][16] NORD and ARRE both highlight hypoglycemia as a recurrent feature; Yuan et al. emphasize that “SHAPNS is a rare autosomal dominant disorder characterized by hypoglycemia, neonatal feeding difficulties, minor congenital heart disease, hypotonia, seizures, cerebral atrophy, developmental disabilities, macrocephaly and a typical facial appearance,” capturing the metabolic and cardiac components of the syndrome.[11] Hypoglycemia episodes often occur in the neonatal period or infancy, requiring careful monitoring and sometimes intravenous glucose or dietary adjustments to maintain euglycemia and prevent neurologic damage.[1][11][16] These episodes may be related to altered insulin sensitivity or endocrine regulation, although specific hormonal profiles have not been systematically analyzed in published cases.[11][15]

Congenital heart disease is another important phenotype in SHAPNS, though typically described as minor congenital heart disease rather than complex structural defects.[1][11][15] Yuan’s newborn case report noted minor congenital heart disease in the affected infant, consistent with prior observations in other individuals.[11] Murine *Asxl2* gene-trap mutants exhibit congenital heart malformations and reductions in bulk H3K27me3 levels in cardiac tissue, indicating that ASXL2 plays a crucial role in cardiogenesis and epigenetic regulation of cardiac gene expression.[15] Cardiovascular phenotypes in humans may include atrial septal defects, ventricular septal defects, or valve anomalies, though detailed cardiac imaging data are limited in the SHAPNS literature.[1][11] Cardiology follow-up is recommended to assess and manage these findings, and NORD notes that treatment includes cardiology follow-up for congenital heart disease.[1]

HPO terms relevant to these metabolic and cardiovascular features include hypoglycemia (HP:0001943), neonatal feeding difficulties (HP:0008872), congenital heart disease (HP:0001627), and possibly specific structural defects (e.g., atrial septal defect, HP:0001631; ventricular septal defect, HP:0001629).[7][11] Age of onset for hypoglycemia and feeding difficulties is neonatal or infancy; congenital heart disease is present at birth and detected via echocardiography.[1][11][16] Symptom severity ranges from mild, easily managed hypoglycemia to recurrent, severe episodes requiring hospitalization; cardiac defects may be hemodynamically insignificant or require surgical or interventional correction.[1][11] Quality of life impact depends on severity but can be substantial in cases with frequent hypoglycemia or significant cardiac involvement, as these conditions increase hospitalization risks and impose restrictions on physical activity and diet.[1][10][16]

Mechanistically, metabolic phenotypes may reflect systemic consequences of altered ASXL2 function in adipose tissue, liver, and endocrine organs. *Asxl2* knockout mice exhibit lipodystrophy and insulin resistance, suggesting that ASXL2 is involved in adipogenesis and metabolic homeostasis.[15] A study noted that ASXL1 and ASXL2 play opposite roles in adipogenesis via reciprocal regulation of peroxisome proliferator-activated receptor γ (PPARγ), a key transcription factor in adipocyte differentiation and insulin sensitivity, indicating that ASXL2 loss could impair PPARγ-mediated metabolic regulation and contribute to hypoglycemia and insulin dysregulation.[15] In SHAPNS, the interplay between ASXL2 haploinsufficiency and endocrine pathways may result in episodic hypoglycemia, particularly under stress or illness conditions, though detailed biochemical profiling in human patients is needed to substantiate these hypotheses.[11][15]

### 3.5. Oral, Dental, Gastrointestinal, Orthopedic, and Behavioral Phenotypes

Recent literature has highlighted oral and dental anomalies as part of the Shashi-Pena syndrome phenotype. A 2023 article titled “Oral findings and healthcare management in Shashi-Pena syndrome” describes SHAPNS as “a newly recognized and rare neurodevelopmental disorder with unique phenotypic features” and focuses on dental anomalies and oral health management in affected individuals.[17] Mol Syndromol’s 2025 case report notes dental anomalies in a 15-year-old patient with overgrowth and minor neurodevelopmental features, reinforcing dental issues as a recurring but under-recognized component of SHAPNS.[9] These anomalies may include abnormal tooth size, shape, positioning, malocclusion, and susceptibility to caries or periodontal disease, though detailed HPO mapping is still emerging.[9][17] Relevant HPO terms include abnormal tooth morphology (HP:0000164), malocclusion (HP:0000324), and other specific dental phenotypes.[7][17] Age of onset is childhood and adolescence, when permanent dentition emerges, and symptom severity can range from mild cosmetic differences to functional impairment requiring orthodontic or surgical intervention.[9][17]

Gastrointestinal manifestations such as constipation are reported by ARRE as common features in SHAPNS, likely related to hypotonia, autonomic dysfunction, or medication side effects.[10] Feeding difficulties in infancy, noted in Yuan’s newborn case and other reports, may reflect hypotonia, oral–motor incoordination, or anatomical factors.[1][11] HPO terms include constipation (HP:0002019), feeding difficulties (HP:0008872), and potentially gastroesophageal reflux (HP:0002020) if present.[7][11][10] Age of onset is infancy for feeding difficulties and early childhood for constipation; severity varies widely, and quality of life impact can be notable, particularly when chronic constipation causes pain, behavioral issues, or secondary complications.[1][10][16]

Orthopedic complications are mentioned by ARRE as features in some individuals, including musculoskeletal abnormalities and motor challenges associated with hypotonia and altered body patterning.[10] In *Asxl2* murine models, axial skeleton alterations and low bone mineral density suggest that ASXL2 plays a role in bone development and homeostasis, providing a mechanistic basis for orthopedic issues in SHAPNS.[15] HPO terms may include axial skeleton abnormalities (HP:0000925), low bone mineral density (HP:0004349), and motor delay (HP:0001270).[7][15] Age of onset is childhood, and severity can range from mild postural abnormalities to more complex orthopedic conditions impacting mobility and pain.[10][15]

Behavioral and sensory challenges are reported by ARRE and implied in clinical descriptions, encompassing social difficulties, anxiety, attention deficits, sensory hypersensitivity, and possibly autism spectrum traits.[10][1][9] HPO terms include behavioral abnormality (HP:0000708), autism (HP:0000717), and sensory hypersensitivity (HP:0000724), although formal psychiatric diagnoses have not been extensively documented in SHAPNS cohorts.[7][10] Age of onset is childhood, often emerging as cognitive and social demands increase, and severity spans from mild behavioral quirks to significant neuropsychiatric impairment requiring multidisciplinary support.[1][10][16] The quality of life impact of behavioral and sensory issues can be substantial, affecting family dynamics and educational inclusion, but supportive therapies, structured environments, and individualized educational plans may ameliorate these challenges.[1][10][16]

In summary, Shashi-Pena syndrome presents a wide-ranging phenotype affecting multiple organ systems, with core neurodevelopmental, craniofacial, metabolic, and cardiac features, complemented by dental, gastrointestinal, orthopedic, and behavioral manifestations. Phenotypic expressivity is highly variable, and some individuals may lack certain hallmark features such as developmental delay or epilepsy, as noted by Mol Syndromol’s atypical case, underscoring the need for flexible diagnostic criteria and gene-based confirmation.[9][11][13][16]

## 4. Genetic and Molecular Information

### 4.1. Causal Gene: ASXL2

ASXL2 (additional sex combs like transcriptional regulator 2) is the sole gene currently known to cause Shashi-Pena syndrome when disrupted in a heterozygous, germline manner.[1][9][11][13][14] ASXL2 is part of the ASXL gene family, which includes ASXL1 and ASXL3, orthologs of the *Drosophila* Additional sex combs (*Asx*) gene that regulate the balance between Trithorax group (TrxG) and Polycomb group (PcG) function.[15][14] The NCBI Gene ID for human ASXL2 is 55252, and the Ma’ayan Lab Harmonizome entry notes that ASXL2 has 6,223 functional associations spanning molecular, disease, and phenotypic categories, highlighting its extensive involvement in diverse biological processes.[4] OMIM lists ASXL2 under entry 612991 and links it to Shashi-Pena syndrome (OMIM 617190), while GeneReviews identifies ASXL2 as the causative gene for SHAPNS.[5][16][13]

Structurally, ASXL2 encodes a large nuclear protein containing conserved domains such as the ASX homology (ASXH) region and a plant homeodomain (PHD) finger at the C-terminus, which interact with histone tails and chromatin-modifying complexes.[15][14] ASXL2 interacts with Polycomb repressive complex 2 (PRC2), facilitating its binding at select genomic targets and influencing H3K27 trimethylation (H3K27me3), a hallmark repressive modification associated with PcG-mediated gene silencing.[15] It also interfaces with TrxG complexes, balancing activation and repression of developmental genes, including HOX clusters, which regulate body patterning.[15][14] As a scaffolding protein, ASXL2 coordinates recruitment of histone methyltransferases, demethylases, and transcription factors to specific genomic loci, making it a critical mediator of epigenetic regulation during embryonic development and organogenesis.[15][4]

ASXL2’s critical role in development is underscored by murine models, where *Asxl2* knockout or gene-trap mutants exhibit partially embryonic lethality, axial skeleton transformations, reduced body weight, congenital heart malformations, low bone mineral density, osteopetrosis, lipodystrophy, insulin resistance, and hematopoietic defects.[15] These phenotypes demonstrate that ASXL2 loss affects multiple organ systems, consistent with the multisystem presentation of SHAPNS in humans.[1][9][11][15] GO terms associated with ASXL2 include chromatin binding (GO:0003682), regulation of transcription, DNA-templated (GO:0006355), histone methyltransferase complex binding (GO:0035092), and developmental process (GO:0032502), reflecting its molecular and biological roles.[4][15]

### 4.2. Pathogenic Variant Spectrum and Functional Classification

Pathogenic variants causing Shashi-Pena syndrome are predominantly heterozygous truncating variants in *ASXL2*, including nonsense, frameshift, and splice-site changes, as well as structural variants such as balanced translocations that disrupt gene integrity.[1][3][9][11][13][14] The original AJHG study reported de novo truncating variants, including nonsense and frameshift mutations, in six unrelated individuals, all located within exons encoding functional domains and predicted to result in premature termination and loss-of-function of ASXL2.[13] Yuan et al. identified a heterozygous de novo truncating variant c.1792C>T (p.Gln598*) in exon 11 of *ASXL2*, in a newborn with classic SHAPNS features, and classified it as pathogenic based on ACMG criteria and de novo occurrence.[11] The SciDirect report described a novel heterozygous nonsense variant c.2485G>T (p.Gly829*) in ASXL2 in a Chinese patient, noting that this case represented the first instance of premature death linked to SHAPNS in this population and adding to the mutation spectrum.[3]

Structural variants affecting *ASXL2* include the complex balanced translocation t(2;11)(p23.3;q22.1) reported in Neurology Genetics, which divides *ASXL2* into two parts and decreases its mRNA expression.[14] Using long-read sequencing, RNA-seq, and qPCR, the authors demonstrated that the translocation disrupted ASXL2 expression and concluded that “a complex rearrangement of the chromosomes decreased the mRNA expression of ASXL2 in the patients and led to a rare autosomal-dominant neurodevelopmental syndrome, Shashi-Pena syndrome.”[14] This finding broadens the pathogenic mechanism from truncating point mutations to structural rearrangements and highlights the importance of considering chromosomal abnormalities involving *ASXL2* in undiagnosed neurodevelopmental syndromes.

Variant classification under ACMG/AMP guidelines generally places these truncating and disruptive variants in the “pathogenic” or “likely pathogenic” category due to strong evidence for loss-of-function, de novo occurrence, absence from population databases, and consistent phenotype association.[13][16] The Gene Mutation database cited in the SciDirect case lists 12 *ASXL2* mutations, with 11 associated with neurodevelopmental disorders, underscoring the strong genotype–phenotype correlation.[3] Germline origin is typical; most variants are de novo, though the balanced translocation family illustrates inherited structural variants.[14][1] No recurrent hotspot missense variants or gain-of-function alleles have been linked to SHAPNS, in contrast to some other epigenetic regulator disorders where missense mutations in catalytic domains are pathogenic.[15]

Population allele frequencies of pathogenic *ASXL2* variants in gnomAD, ExAC, and 1000 Genomes are essentially zero, consistent with strong constraint against ASXL2 loss-of-function in healthy populations.[4][15] ASXL2’s intolerance to truncating variation supports its dosage sensitivity and the pathogenicity of haploinsufficient states. Somatic variants in *ASXL2* have been observed in certain cancers, where ASXL proteins are altered, but these are not implicated in congenital SHAPNS, which requires germline disruption.[15] COSMIC and TCGA data indicate that ASXL2 can be somatically mutated in malignancies, and ASXL2 has been implicated in leukemogenesis in combination with RUNX1-ETO, but these somatic events reflect oncogenesis rather than the congenital syndrome.[15]

Functional consequences of SHAPNS-associated variants are best characterized as loss-of-function through nonsense-mediated decay or truncated protein lacking essential domains. The cancer-focused ASXL review notes that “Additional sex combs-like 2 is required for polycomb repressive complex 2 binding at select targets,” and that ASXL2 gene-trap mutants show reduced bulk H3K27me3 levels in cardiac tissue, indicating impaired PRC2 recruitment.[15] Loss-of-function ASXL2 variants in SHAPNS are likely to reduce PRC2 binding and H3K27me3 at developmental loci, leading to dysregulated gene expression and abnormal development. There is no evidence that these variants exert dominant-negative or gain-of-function effects; haploinsufficiency appears to be the primary mechanism.[13][15] 

### 4.3. Epigenetic Roles and Molecular Pathways

ASXL2 is an epigenetic scaffolding protein that coordinates PcG and TrxG activities, linking it to fundamental epigenetic pathways in development and disease. The ASXL proteins, including ASXL1, ASXL2, and ASXL3, are mammalian homologs of *Drosophila* Asx, which regulates the balance between trithorax-mediated gene activation and Polycomb-mediated gene repression.[15][14] ASXL2 interacts with PRC2, facilitating its binding at specific targets and maintaining H3K27me3, thereby repressing expression of key developmental genes.[15] Loss of ASXL2 in mice leads to reduction in bulk H3K27me3 in cardiac tissue and other epigenetic alterations, confirming its role in PcG recruitment.[15] In hematopoiesis, conditional *Asxl2* deletion via Mx1-cre results in cytopenias and impaired hematopoietic stem and progenitor cell self-renewal, associated with reduced H3K4me1, a mark linked to enhancers, further demonstrating ASXL2’s broad influence on histone modifications.[15]

From a pathway standpoint, ASXL2 participates in chromatin organization and histone modification (GO:0016585, chromatin remodeling; GO:0031060, regulation of histone methylation), HOX gene regulation (GO:0009952, anterior/posterior pattern specification), heart development (GO:0007507), skeletal system development (GO:0001501), and adipogenesis (GO:0045444).[15][4] It also interacts with RUNX1-ETO in leukemogenesis, indicating involvement in transcriptional complexes regulating hematopoietic differentiation and oncogenic transformation.[15] In SHAPNS, these pathways are likely disrupted in a tissue-specific manner, leading to developmental anomalies in brain, heart, skeleton, and metabolic tissues.[1][9][11][13][15]

At the chromosomal level, structural variants affecting *ASXL2*, such as the t(2;11)(p23.3;q22.1) translocation, result in complex rearrangements that reduce ASXL2 mRNA expression. Neurology Genetics reports that this balanced translocation divides *ASXL2* into two parts; RNA-seq and qPCR demonstrate decreased ASXL2 expression, and the authors conclude that this structural variant is the pathogenic mechanism underlying SHAPNS in the affected family.[14] DECIPHER and other structural variant databases may record similar rearrangements, underscoring the need to consider chromosomal breakpoints at 2p23.3 in undiagnosed neurodevelopmental cases.[14][7]

Epigenomic resources such as ENCODE and Roadmap Epigenomics provide contextual data on ASXL2 binding sites and histone modification patterns, although specific ASXL2 ChIP-seq datasets may be limited. Nonetheless, the general epigenetic roles of PcG/TrxG complexes and their regulation of developmentally important genes inform mechanistic models of SHAPNS, in which ASXL2 haploinsufficiency leads to misregulated chromatin states and aberrant expression of gene networks controlling organogenesis and neurodevelopment.[15][4]

### 4.4. Structural Genomic Features and Molecular Profiling

Given the rarity of Shashi-Pena syndrome, large-scale molecular profiling studies (transcriptomics, proteomics, metabolomics, lipidomics) specific to SHAPNS are not yet available. However, structural genomic data from individual cases, particularly the Neurology Genetics balanced translocation study, provide insight into genomic mechanisms.[14] Long-read sequencing using Oxford Nanopore Technology identified 102 balanced translocations and 145 inversions affecting *ASXL2* at an average of 15× coverage in the translocation family, revealing complex structural variation in the genomic region.[14] RNA-seq and qPCR showed decreased *ASXL2* expression, linking structural disruption to transcript-level consequences and clinical phenotype.[14]

In general, genomic structural features of *ASXL2* include exons encoding functional domains such as ASXH and PHD, intronic regions susceptible to breakpoints, and promoter elements regulating tissue-specific expression. UCSC Genome Browser and Ensembl can provide detailed maps of *ASXL2* structure, but SHAPNS-specific analyses are limited to case-level studies.[4][14] Transcriptomic consequences of ASXL2 haploinsufficiency likely include altered expression of HOX genes, cardiac development genes, and metabolic regulators; these predictions are supported by mouse models but not yet directly validated in SHAPNS patient tissues.[15]

Proteomics data for ASXL2 interactions reveal binding partners in PcG and TrxG complexes, as well as potential interactions with transcription factors such as RUNX1-ETO, but disease-specific proteomic signatures in SHAPNS remain unexplored.[15] Metabolomics and lipidomics signatures may be altered due to lipodystrophy and insulin resistance observed in *Asxl2* knockout mice, suggesting potential changes in fatty acid metabolism, adipokine levels, and glucose homeostasis, but human SHAPNS studies are lacking.[15] Integration of multi-omics data (genomics, epigenomics, transcriptomics, proteomics, metabolomics) in future SHAPNS cohorts would be valuable for elucidating systemic pathways affected by ASXL2 loss and identifying biomarkers for diagnosis and prognosis.

In summary, the genetic and molecular landscape of Shashi-Pena syndrome is dominated by germline heterozygous truncating and structural variants in *ASXL2*, leading to loss-of-function of an epigenetic scaffolding protein that coordinates PcG/TrxG-mediated chromatin regulation. This molecular defect cascades into widespread developmental gene misregulation, affecting multiple organ systems and giving rise to the complex phenotype observed in SHAPNS.[13][14][15][1][9][11][16]

## 5. Environmental Information

### 5.1. Non-genetic Contributing Factors

Shashi-Pena syndrome is fundamentally a genetic disorder, and no non-genetic environmental factors such as toxins, radiation, pollution, or occupational exposures have been implicated as causative contributors.[1][3][11][13][14] The syndrome manifests in individuals with germline *ASXL2* disruption, and no cases have been reported in which environmental exposures alone produced a SHAPNS phenotype absent genetic lesions. Consequently, environmental factors are viewed primarily as modifiers of symptom severity or clinical course rather than initiators of disease.

CTD and related environmental toxicology databases do not list Shashi-Pena syndrome as an environmentally linked condition, and there is no indication of increased incidence in populations exposed to specific chemicals or radiation.[1][15] The congenital onset of SHAPNS, with features evident at birth and a clear Mendelian pattern, further supports the primacy of genetic etiology over environmental causation.[1][11][16] 

### 5.2. Lifestyle Factors and Infectious Agents

Lifestyle factors such as smoking, alcohol consumption, diet, and exercise have not been associated with risk of Shashi-Pena syndrome, which arises early in life due to germline variants. Parental lifestyle factors may play indirect roles in general pregnancy outcomes but are not known to specifically influence the occurrence of de novo *ASXL2* variants or structural rearrangements.[1][13][14] Given the ultra-rare nature of SHAPNS, epidemiologic studies linking lifestyle patterns to disease risk are impractical with current case numbers, and there is no evidence-based rationale for specific lifestyle recommendations to prevent SHAPNS.

Similarly, infectious agents—bacteria, viruses, fungi, parasites—have not been implicated in causing or triggering SHAPNS.[1][3][11][13][14] The absence of any infectious clusters or temporal patterns reinforces the genetic origin. Nonetheless, infections may exacerbate existing symptoms, particularly hypoglycemia, seizures, or cardiac strain, and standard infection prevention measures are important in clinical management but not specific to SHAPNS.[1][16]

### 5.3. Environmental Modulation of Phenotypic Expression

Although environmental factors do not cause Shashi-Pena syndrome, they may modulate phenotypic expression and clinical outcomes. Nutritional status can influence growth trajectories, hypoglycemia severity, and overall health; high-quality nutrition and careful monitoring of blood glucose may reduce metabolic crises and improve developmental progress.[1][11][16] Access to physical therapy, occupational therapy, and speech therapy can ameliorate hypotonia, motor delay, and speech deficits, indirectly mitigating the functional impact of ASXL2 haploinsufficiency.[1][10][16] Environmental enrichment and supportive educational settings may positively affect behavioral and cognitive outcomes, suggesting that gene–environment interactions at the level of neuronal plasticity could shape long-term trajectories.[1][10]

From a mechanistic standpoint, ASXL2’s role in epigenetic regulation suggests that environmental stimuli influencing chromatin states—such as stress, nutrition, and endocrine signals—could modulate gene expression patterns in ASXL2-deficient cells, potentially altering severity of phenotypes.[15] However, direct evidence for such interactions in SHAPNS is lacking, and no specific environmental interventions have been validated as modifiers of disease progression. Clinical management therefore focuses on symptomatic care and general health optimization rather than targeted environmental modulation of ASXL2-related pathways.[1][16]

Overall, current data support a view of Shashi-Pena syndrome as a predominantly genetic condition with minimal established environmental or lifestyle contributions to disease risk, though environment can influence symptom severity and quality of life through generic health effects.[1][3][11][13][14][15][16]

## 6. Mechanism and Pathophysiology

### 6.1. Molecular Pathways and Upstream Mechanisms

The pathophysiology of Shashi-Pena syndrome can be conceptualized as a cascade originating from ASXL2 haploinsufficiency, progressing through epigenetic dysregulation, altered developmental gene expression, and downstream tissue-level anomalies. ASXL2’s primary molecular role is to serve as an epigenetic scaffolding protein that interacts with PcG and TrxG complexes, particularly PRC2, to regulate histone methylation and transcription of developmental genes.[15][14] In normal development, ASXL2 facilitates PRC2 binding at specific genomic targets, promoting H3K27me3 and repression of genes whose expression must be tightly controlled, such as HOX clusters and genes involved in body axis patterning, organogenesis, and differentiation.[15][4]

Loss-of-function mutations in *ASXL2* reduce its ability to recruit PRC2 and maintain appropriate H3K27me3 levels. In *Asxl2* gene-trap mutant mice, reductions in bulk H3K27me3 in cardiac tissue are observed, confirming disrupted PcG-mediated repression.[15] Conditional *Asxl2* deletion in hematopoietic cells results in altered H3K4me1 levels and impaired hematopoietic stem and progenitor cell function, indicating that ASXL2 also influences enhancer-associated marks and TrxG-related pathways.[15] These epigenetic changes are upstream mechanisms that cause misregulation of gene expression, leading to inappropriate activation or repression of developmental programs.

Pathways likely affected include HOX gene regulation (GO:0009952), heart development (GO:0007507), skeletal system development (GO:0001501), neurogenesis (GO:0022008), adipogenesis (GO:0045444), and metabolic processes such as insulin signaling (GO:0032868).[15][4] ASXL2 also interacts with RUNX1-ETO, an oncogenic fusion protein in leukemia, suggesting that ASXL2 plays a role in transcriptional complexes governing hematopoietic differentiation and proliferation.[15] While this is more relevant to cancer, it underscores the broad involvement of ASXL2 in transcriptional control.

Given these upstream mechanisms, ASXL2 haploinsufficiency can be modeled as causing a global shift in chromatin state, leading to aberrant expression patterns across multiple tissues. In the brain, altered expression of genes involved in neuronal proliferation, migration, and synaptogenesis may result in macrocephaly, cerebral atrophy, and neurodevelopmental deficits.[13][11] In the heart, dysregulated expression of cardiac developmental genes may produce congenital heart malformations.[11][15] In adipose tissue and metabolic organs, changes in PPARγ regulation and related pathways could cause lipodystrophy and insulin resistance, as seen in mice, and episodic hypoglycemia in humans.[15][11] These mechanisms constitute the upstream molecular basis of SHAPNS.

### 6.2. Cellular Processes and Protein Dysfunction

At the cellular level, ASXL2 dysfunction leads to aberrant chromatin organization, transcriptional dysregulation, and altered cell differentiation and proliferation. ASXL2 localizes to the nucleus, where it binds chromatin and interacts with histone methyltransferase complexes. Loss-of-function results in reduced binding to chromatin targets, decreased recruitment of PRC2, and altered histone modification landscapes, particularly H3K27me3 and H3K4me1.[15] Consequently, genes that should be repressed in certain developmental contexts may remain inappropriately active, while others may be insufficiently activated, disrupting cellular differentiation programs.

Cellular processes impacted include neuronal differentiation and maturation in the central nervous system, cardiomyocyte differentiation in the heart, osteoblast and chondrocyte differentiation in bone, adipocyte differentiation in adipose tissue, and hematopoietic lineage commitment in bone marrow.[15][13][11] GO terms relevant to these processes include regulation of transcription, DNA-templated (GO:0006355), chromatin organization (GO:0006325), cell differentiation (GO:0030154), neurogenesis (GO:0022008), and cardiac muscle cell differentiation (GO:0055007).[4][15] CL ontology terms for affected cell types include neuron (CL:0000540), cardiomyocyte (CL:0000746), osteoblast (CL:0000062), adipocyte (CL:0000136), and hematopoietic stem cell (CL:0000037).

Protein dysfunction in SHAPNS arises from truncated ASXL2 proteins that lack critical domains, such as the PHD finger, or from reduced protein levels due to nonsense-mediated decay. These truncated or absent proteins cannot perform normal scaffolding functions, leading to defective recruitment of PcG/TrxG complexes.[13][15] There is no evidence that truncated proteins exert dominant-negative effects by sequestering binding partners; instead, loss-of-function and haploinsufficiency appear to be the primary mechanisms.[13][15]

Autophagy, apoptosis, and cell cycle dysregulation may also be secondarily affected, as epigenetic regulators like ASXL2 influence expression of cell-cycle genes and stress response pathways. However, specific data on these processes in SHAPNS are limited, and most mechanistic insight derives from *Asxl2* knockout mice and in vitro studies.[15] In cancer contexts, ASXL proteins are altered and associated with oncogenesis, supporting the idea that ASXL2 affects proliferation and survival pathways, but direct extrapolation to SHAPNS requires caution.[15]

### 6.3. Tissue-Level Pathophysiology and Organ System Effects

The downstream tissue-level consequences of ASXL2 dysfunction manifest as the organ system phenotypes seen in Shashi-Pena syndrome. In the central nervous system, epigenetic misregulation leads to macrocephaly, cerebral atrophy, and neurodevelopmental impairment. Macrocephaly may reflect increased proliferation of neuronal or glial precursors during early brain development, while cerebral atrophy detected on imaging may correspond to subsequent abnormalities in neuronal survival or synaptic maintenance.[13][11] Clinically, these structural changes correlate with developmental delay, hypotonia, and seizures, indicating that altered brain architecture and connectivity underlie functional deficits.[1][9][11][16]

In the heart, ASXL2-dependent PcG regulation of cardiac development genes is crucial for proper morphogenesis. Murine *Asxl2* gene-trap mutants exhibit congenital heart malformations, and reduced H3K27me3 in cardiac tissue suggests dysregulated gene expression.[15] In SHAPNS, minor congenital heart disease likely arises from similar mechanisms, including subtle defects in septation or valve formation, leading to atrial or ventricular septal defects and other anomalies.[11][1] These cardiac manifestations may be clinically mild but contribute to the multisystem nature of SHAPNS and justify cardiology follow-up.[1][11]

In skeletal tissues, axial skeleton transformations in *Asxl2* knockout mice implicate ASXL2 in skeletal patterning, which could relate to orthopedic complications in SHAPNS, such as spinal or limb abnormalities.[15][10] Reduced bone mineral density in mice suggests potential risk for osteopenia or fractures in humans, although such features are not yet widely reported in SHAPNS cohorts.[15] 

In metabolic tissues, lipodystrophy and insulin resistance in *Asxl2* mutant mice point to an important role for ASXL2 in adipogenesis and metabolic homeostasis. These murine phenotypes align with human SHAPNS manifestations of episodic hypoglycemia and difficulty controlling blood sugar, suggesting that ASXL2 haploinsufficiency disrupts endocrine regulation of glucose and lipid metabolism.[11][15] The interplay between adipocyte differentiation, liver metabolism, and pancreatic hormone secretion likely contributes to metabolic instability in SHAPNS.

In oral and craniofacial tissues, ASXL2-mediated epigenetic regulation of craniofacial development pathways shapes facial morphology and dental patterning. Dental anomalies and oral findings described in SHAPNS likely reflect disrupted differentiation of odontoblasts and craniofacial mesenchyme, though specific molecular pathways remain to be elucidated.[9][17]

### 6.4. Biochemical and Metabolic Abnormalities

Biochemical abnormalities in Shashi-Pena syndrome center on hypoglycemia and potentially insulin dysregulation. Hypoglycemia episodes suggest an imbalance between glucose utilization and availability, which could result from increased insulin action, reduced glycogen stores, impaired gluconeogenesis, or altered endocrine signaling.[1][11] CHEBI ontology entries relevant to these processes include glucose (CHEBI:17234), insulin (CHEBI:15996), and glycogen (CHEBI:28087). Although detailed endocrine evaluations are sparse, episodic hypoglycemia in SHAPNS may reflect ASXL2’s role in metabolic gene regulation, as indicated by murine models showing insulin resistance and lipodystrophy.[15]

Other laboratory abnormalities, such as cytopenias, are reported in *Asxl2* conditional knockout mice, but similar hematologic findings have not been widely described in human SHAPNS patients.[15] Liver function tests, lipid profiles, and other metabolic panels have not been systematically reported, limiting insight into biochemical changes beyond hypoglycemia. As more individuals are evaluated with comprehensive laboratory assessments, additional biochemical phenotypes may emerge.

### 6.5. Epigenetic Changes and Multi-Omics Integration

Epigenetic changes in ASXL2-deficient tissues include decreased H3K27me3 at PRC2 target genes and altered H3K4me1 at enhancers, as demonstrated in murine models.[15] These modifications correspond to changes in chromatin accessibility and gene expression, which could be detailed through ChIP-seq and RNA-seq in future SHAPNS studies. ENCODE and Roadmap Epigenomics datasets provide generic maps of these marks, but disease-specific data are not yet available.

Multi-omics integration, combining genomic, epigenomic, transcriptomic, proteomic, and metabolomic data in SHAPNS, has not yet been undertaken due to the ultra-rare nature of the syndrome and the small number of cases. However, the Neurology Genetics study exemplifies structural genomics and transcriptomics integration by linking balanced translocation breakpoints to decreased *ASXL2* mRNA expression.[14] Similar approaches in additional patients could reveal consistent patterns of pathway dysregulation, identify biomarkers, and refine mechanistic models. Given ASXL2’s widespread functional associations, such multi-omics studies would likely reveal perturbations across developmental, metabolic, and signaling networks.[4][15]

In summary, the pathophysiology of Shashi-Pena syndrome involves upstream loss-of-function of ASXL2, leading to epigenetic dysregulation at PRC2 and TrxG targets, altered developmental gene expression, and downstream abnormalities in brain, heart, skeletal, metabolic, and oral tissues. This cascade spans molecular, cellular, tissue, and organ levels, producing the complex clinical phenotype observed in SHAPNS.[13][14][15][1][9][11][16]

## 7. Anatomical Structures Affected

### 7.1. Organ-Level Involvement and Body Systems

Shashi-Pena syndrome affects multiple organ systems, reflecting the broad developmental role of ASXL2. Primary organs directly involved include the brain, heart, craniofacial structures, skeletal system, metabolic organs (liver, adipose tissue, pancreas), and dentition.[1][9][11][13][15][17] The central nervous system, including the cerebral cortex, subcortical structures, and cerebellum, is implicated through macrocephaly, cerebral atrophy, developmental delay, and seizures.[11][13] UBERON ontology terms relevant to these structures include brain (UBERON:0000955), cerebral cortex (UBERON:0000956), and cerebellum (UBERON:0002037). The cardiovascular system is affected via congenital heart disease, involving structures such as the atria, ventricles, septa, and valves; UBERON terms include heart (UBERON:0000948), cardiac ventricle (UBERON:0002073), and cardiac valve (UBERON:0002133).[11][15]

Craniofacial structures, including skull, facial bones, eyes, ears, and skin, are involved in macrocephaly, facial dysmorphism, hypertelorism, prominent eyes, low-set ears, and glabellar nevus flammeus. UBERON terms include skull (UBERON:0003129), face (UBERON:0001444), orbit (UBERON:0001683), and skin (UBERON:0002097).[1][9][11] Skeletal structures beyond the cranial vault may be affected by axial skeleton abnormalities, suggested by murine *Asxl2* models, though human data are limited.[15] UBERON:0004288 (vertebral column) and UBERON:0008896 (skeleton) are relevant.

Metabolic organs, particularly liver (UBERON:0002107), adipose tissue (UBERON:0001013), and pancreas (UBERON:0001264), may be functionally involved in hypoglycemia and metabolic dysregulation, based on murine data and human episodes of hypoglycemia.[11][15] Oral and dental structures, including teeth (UBERON:0001091), gums (UBERON:0001836), and jaw bones (UBERON:0001685), are affected by dental anomalies described in SHAPNS.[9][17]

Secondary organ involvement includes gastrointestinal tract (UBERON:0001043) in constipation and feeding difficulties, musculoskeletal system in orthopedic complications, and endocrine organs such as pituitary and adrenal glands if hormonal pathways are perturbed.[1][10][11][15] Body systems involved therefore include nervous, cardiovascular, skeletal, metabolic, endocrine, gastrointestinal, and integumentary systems.

### 7.2. Tissue and Cell-Level Involvement

At the tissue level, SHAPNS affects nervous tissue (neurons, glia), cardiac muscle tissue, skeletal bone tissue, adipose tissue, and epithelial and connective tissues in craniofacial and oral regions.[15][11][9][17] Nervous tissue involvement accounts for developmental delay, seizures, and cerebral atrophy; CL terms include neuron (CL:0000540) and glial cell (CL:0000125). Cardiac muscle tissue involvement manifests as congenital heart disease, with affected cardiomyocytes (CL:0000746) and cardiac fibroblasts shaping structural defects.[11][15]

Skeletal tissue involvement is suggested by axial skeleton transformations in *Asxl2* knockout mice, where osteoblasts (CL:0000062) and chondrocytes (CL:0000132) are likely affected, potentially corresponding to orthopedic complications in humans.[15][10] Adipose tissue involvement, evidenced by lipodystrophy and insulin resistance in mice, implies altered adipocyte function (CL:0000136), with consequences for metabolic homeostasis.[15] Oral tissues include odontoblasts (CL:0000664), ameloblasts (CL:0000672), and periodontal fibroblasts, corresponding to dental anomalies in SHAPNS.[9][17]

Epithelial and connective tissues in the skin, particularly facial skin at the glabella, are involved in capillary malformations such as nevus flammeus, with vascular endothelial cells (CL:0000096) and pericytes contributing to the lesion.[1][9] Gastrointestinal tissue involvement includes smooth muscle cells and enteric neurons in the gut wall, associated with constipation and motility issues.[10][1] Hematopoietic tissue involvement is suggested by murine *Asxl2* conditional knockout models but not yet clearly observed in human SHAPNS, though ASXL2’s role in hematopoietic stem cells indicates potential risk for subtle hematologic abnormalities.[15]

### 7.3. Subcellular Localization and Cellular Components

At the subcellular level, ASXL2 localizes to the nucleus (GO:0005634), where it interacts with chromatin (GO:0000785), PRC2 complexes (GO:0035098, PRC2 complex), and other nuclear proteins.[15][4] ASXL2’s PHD finger domain binds histone tails, positioning it at nucleosomes and enabling regulation of histone methylation. Loss-of-function alters nuclear chromatin organization, affecting compartments such as euchromatin and heterochromatin domains.

Other subcellular components indirectly involved include mitochondria (GO:0005739) in energy metabolism and hypoglycemia-related brain and muscle function, endoplasmic reticulum (GO:0005783) in protein processing, and lysosomes (GO:0005764) in autophagy and cell stress responses, though these are more generic than specific to SHAPNS.[11][15] Nuclear localization of ASXL2 underscores that SHAPNS pathophysiology arises from altered gene expression rather than primary defects in organelles like mitochondria or lysosomes.

### 7.4. Localization and Lateralization

Anatomical localization of SHAPNS phenotypes is generally symmetrical rather than lateralized. Macrocephaly affects the entire cranial vault; facial dysmorphism is bilateral; congenital heart defects involve central cardiac structures; and cerebral atrophy, when present, is often generalized or diffuse.[11][13] The glabellar nevus flammeus is midline, localized to the central forehead between the eyebrows.[1][9] Dental anomalies affect multiple teeth and arches rather than unilateral segments.[9][17]

Thus, lateralization patterns are minimal; SHAPNS is best characterized by midline and bilateral anomalies reflecting global developmental gene regulation defects, rather than unilateral or focal lesions. This supports the concept of ASXL2 as a systemic epigenetic regulator whose disruption affects global developmental processes and symmetrically patterned structures.[15][13]

## 8. Temporal Development and Natural History

### 8.1. Onset and Early Development

Shashi-Pena syndrome is a congenital disorder, with typical age of onset at birth or in the neonatal period. Macrocephaly, facial differences, hypotonia, feeding difficulties, and glabellar nevus flammeus are evident at or shortly after birth.[1][11][13][16] Neonatal hypoglycemia may be recognized within the first days to weeks of life, and minor congenital heart disease is present at birth but may be detected later depending on cardiac evaluation.[11][1] The onset pattern is primarily chronic and insidious rather than acute; while hypoglycemia episodes can be acute, the underlying developmental anomalies are structural and persistent.

Developmental delays become apparent over infancy and early childhood, as milestones for motor, language, and cognition are not achieved at typical ages.[1][9][11][16] Seizures may begin in infancy or childhood, sometimes triggered by infections or metabolic stress.[11][13] Behavioral and sensory challenges emerge over childhood as cognitive and social demands increase. Dental anomalies manifest in mid-childhood to adolescence as permanent teeth erupt.[9][17]

### 8.2. Disease Progression and Course Pattern

The progression of Shashi-Pena syndrome is generally non-progressive with respect to congenital malformations; macrocephaly, facial dysmorphism, and congenital heart defects remain relatively stable in morphology over time.[1][11][16] However, functional manifestations such as developmental delay, intellectual disability, behavioral challenges, and seizures can evolve. Developmental trajectories may show gradual skill acquisition, with some individuals achieving significant improvements through therapy, while others plateau at lower levels of functional independence.[1][9][16]

Disease course patterns include episodic hypoglycemia and seizures, progressive or fluctuating behavioral challenges, and stable or slowly evolving orthopedic complications. Seizure frequency may change with age and treatment; hypoglycemia episodes may become less frequent as dietary management and endocrine maturation occur.[1][11][16] There is no evidence of a degenerative neurodegenerative course; cerebral atrophy may reflect developmental anomalies rather than ongoing degeneration.[11][13]

Disease duration is lifelong; SHAPNS is not self-limited. Individuals continue to live with developmental, behavioral, and medical challenges throughout childhood and adulthood, though outcomes vary widely and some may achieve relatively independent lives, especially in milder cases.[9][10][16] The Mol Syndromol case of a 15-year-old with minor neurodevelopmental features and overgrowth demonstrates that some SHAPNS individuals can have relatively mild lifelong impacts.[9] 

### 8.3. Remission Patterns and Critical Periods

Remission in SHAPNS is not typical for congenital structural anomalies, but episodic manifestations such as seizures and hypoglycemia can remit or be controlled with treatment. Seizures may reach partial or complete remission under antiepileptic regimens; hypoglycemia episodes may decrease as endocrine systems mature and management optimizes.[1][11][16] Behavioral and sensory challenges can improve with therapy and environmental adaptation.

Critical periods in SHAPNS include the neonatal period, when hypoglycemia and feeding difficulties pose acute risks; infancy and early childhood, when developmental interventions can substantially influence motor and cognitive trajectories; and school age, when educational support and behavioral management are crucial for long-term functional outcomes.[1][10][16] Early diagnosis via genetic testing enables anticipatory guidance and timely initiation of therapies, making early life a particularly important window for intervention.

There is limited longitudinal data on adulthood in SHAPNS; as more individuals reach adulthood, critical periods related to transition to adult care, employment, and independent living will become clearer. Current knowledge is dominated by pediatric cases, reflecting the recent recognition of the syndrome and limited natural history data.[1][9][11][13][16]

## 9. Inheritance and Population Characteristics

### 9.1. Epidemiology: Prevalence and Incidence

Shashi-Pena syndrome is extremely rare, qualifying as an ultra-rare disorder within the ASXL-related group. NORD states that the prevalence and incidence of SHAPNS are unknown, and notes that as of 2023, there have been 23 identified cases in the medical literature.[1] ARRE estimates that there are approximately 50–60 people diagnosed with SHAPNS globally, including individuals known through patient registries but not yet published in peer-reviewed literature.[10] These numbers underscore the ultra-rare status of SHAPNS, with prevalence likely far below 1 per 100,000 and incidence measured in single digits per year worldwide.

Orphanet recognizes Shashi-Pena syndrome under ORPHA:689408, consistent with its rare disease classification, but does not yet provide quantitative prevalence or incidence figures due to insufficient data.[6] There are no national registry data or Global Burden of Disease estimates specific to SHAPNS, given its rarity and recent recognition. As exome sequencing becomes more widespread, additional cases may be identified, potentially increasing observed prevalence and incidence, but SHAPNS will remain an ultra-rare disorder relative to common conditions.[1][9][11][13]

### 9.2. Inheritance Pattern, Penetrance, and Expressivity

Shashi-Pena syndrome follows an autosomal dominant pattern of inheritance, with heterozygous pathogenic variants in *ASXL2* sufficient to cause disease.[1][11][13][14][16] NORD notes that the condition is thought to be inherited in an autosomal dominant manner, although most reported individuals have de novo variants and no affected parent is known to have reproduced.[1] In the Neurology Genetics balanced translocation family, autosomal dominant transmission of the structural variant affecting *ASXL2* was documented across three generations, confirming the inheritance pattern.[14] GeneReviews emphasizes that once an *ASXL2* pathogenic variant has been identified in an affected family member, the recurrence risk to offspring is 50% for each pregnancy.[16][1]

Penetrance of the core SHAPNS phenotype appears high in individuals carrying pathogenic *ASXL2* variants, but certain features such as epilepsy, overgrowth, and dental anomalies show incomplete penetrance.[1][9][11][13] For example, Mol Syndromol reports a patient manifesting an atypical presentation of SHAPNS with minor neurodevelopmental problems, marked postnatal overgrowth, and dental anomalies, but without developmental delay or epilepsy, illustrating variable expressivity.[9] ARRE notes that features and abilities vary greatly among individuals, and that the reasons for this broad spectrum are not yet known.[10] This variability suggests that expressivity is variable, while penetrance of some combination of features is high.

Genetic anticipation has not been reported in SHAPNS; there is no indication of increasing severity or earlier onset in successive generations, consistent with the absence of repeat expansion mechanisms.[1][14][16] Germline mosaicism could theoretically explain recurrence of de novo variants in families, but no such cases have been documented; recurrence risk due to parental mosaicism is assumed to be low.[1][16] Founder effects are not apparent, as reported cases originate from diverse ethnic and geographic backgrounds, including American, European, and Chinese patients.[3][11][13][14] Carrier frequency in the general population is extremely low, given the absence of pathogenic *ASXL2* truncating variants in population databases and the ultra-rare nature of SHAPNS.[4][1][15]

### 9.3. Population Demographics and Geographic Distribution

Affected individuals with Shashi-Pena syndrome have been reported across multiple ethnic and geographic backgrounds. The original AJHG series included six unrelated individuals identified through the Undiagnosed Diseases Network in the United States, suggesting that SHAPNS occurs sporadically in diverse populations.[13] Yuan’s newborn case and the Neurology Genetics balanced translocation family represent Chinese patients, indicating presence of SHAPNS in East Asian populations.[11][14] The SciDirect report describes another Chinese patient with a novel nonsense variant and premature death, further supporting SHAPNS in this demographic.[3] Mol Syndromol’s case arises from a European setting, likely Western Europe, based on journal context.[9]

Sex ratio among reported cases is not systematically documented, but there is no indication of sex-linked inheritance or strong sex bias; both males and females are affected, consistent with autosomal dominant transmission.[1][13][14] Age distribution of affected individuals spans neonates (Yuan’s newborn), children (original cases), adolescents (Mol Syndromol’s 15-year-old), and adults (Neurology Genetics family), though the majority of published cases focus on pediatric ages due to early diagnosis and clinical features.[11][13][9][14]

Geographic distribution of specific *ASXL2* variants is limited by small numbers. Some variants may be unique to individual families or populations, such as the c.2485G>T (p.Gly829*) variant in the Chinese patient, but there is insufficient evidence to label them as founder mutations.[3] Overall, SHAPNS appears globally distributed at very low frequency, with no known endemic areas or regional concentration beyond chance clustering in reported studies.[1][3][11][13][14]

## 10. Diagnostics

### 10.1. Clinical Evaluation and Laboratory Tests

Diagnosis of Shashi-Pena syndrome begins with clinical suspicion based on characteristic features and is confirmed by genetic testing for *ASXL2* variants. Clinically, physicians assess macrocephaly, facial gestalt, glabellar nevus flammeus, hypotonia, developmental delay, seizures, hypoglycemia, congenital heart disease, and other features.[1][9][11][13][16] Physical examination, neurologic assessment, developmental evaluation, and dysmorphology analysis are key components.

Laboratory tests include blood glucose monitoring to detect and manage hypoglycemia, standard metabolic panels, and endocrine evaluations as indicated.[1][11][16] LOINC codes for glucose measurement (e.g., 2345-7, glucose [Mass/volume] in serum or plasma) and related tests can be mapped for diagnostic coding. Cardiac evaluation involves echocardiography (RadLex imaging codes), ECG, and potentially cardiac MRI for detailed structural assessment.[11][1] Neurologic evaluation may include EEG to characterize seizure patterns and brain MRI to visualize macrocephaly, cerebral atrophy, and other structural anomalies.[11][13] Gastrointestinal evaluation can address constipation and feeding difficulties, while dental assessment identifies anomalies requiring management.[9][17]

Biopsy, histopathology, and immunohistochemistry are not routinely used for SHAPNS diagnosis, as the syndrome is primarily diagnosed via genetic testing and clinical features. Pathology findings specific to SHAPNS have not been described; tissue-level abnormalities are inferred from imaging and clinical presentation rather than direct histologic analysis.[11][13]

### 10.2. Genetic Testing Approaches

Genetic testing is central to diagnosis of Shashi-Pena syndrome. Whole exome sequencing (WES) has been instrumental in identifying *ASXL2* truncating variants in undiagnosed neurodevelopmental cases, including the original AJHG series and subsequent case reports.[13][11][3] Trio WES—sequencing the proband and both parents—is particularly useful for detecting de novo variants, as demonstrated by Yuan et al.’s newborn case, where trio WES revealed a heterozygous de novo c.1792C>T (p.Gln598*) variant in *ASXL2*.[11] GeneReviews and NORD note that DNA-based testing targeting *ASXL2* is used to diagnose SHAPNS, either via WES or single-gene analysis.[1][16]

Single gene testing of *ASXL2* using Sanger sequencing or targeted NGS can identify known or novel variants in suspected cases, particularly when clinical features strongly suggest SHAPNS.[16][13] Gene panels for neurodevelopmental disorders, macrocephaly syndromes, or overgrowth disorders often include *ASXL2*, enabling detection in broader genetic evaluations.[9][11] Chromosomal microarray (CMA) may identify large deletions involving *ASXL2*, but balanced translocations or subtle structural rearrangements may be missed; thus, karyotyping and long-read sequencing are necessary for detecting complex translocations like t(2;11)(p23.3;q22.1).[14] The Neurology Genetics study highlights the role of karyotyping in identifying balanced translocations, followed by long-read sequencing to characterize breakpoints and RNA-seq/qPCR to assess gene expression changes.[14]

FISH (fluorescence in situ hybridization) could theoretically be used to detect specific chromosomal rearrangements affecting *ASXL2*, but such assays have not yet been standardized for SHAPNS. Mitochondrial DNA testing, repeat expansion testing, and other specialized genetic tests are not relevant to SHAPNS, given its autosomal nuclear gene etiology.[1][13][14]

Whole genome sequencing (WGS) holds potential for comprehensive detection of point mutations, structural variants, and regulatory region changes affecting *ASXL2*, particularly in undiagnosed cases with SHAPNS-like phenotypes but negative WES findings. WGS can capture non-coding variants and balanced rearrangements not seen on CMA, improving diagnostic yield.[14][16] However, WGS is not yet routinely deployed specifically for SHAPNS diagnosis but may be used in broader diagnostic pipelines for undiagnosed neurodevelopmental disorders.

### 10.3. Omics-Based Diagnostics and Biomarkers

Beyond DNA-based testing, omics-based diagnostics for Shashi-Pena syndrome remain largely theoretical due to the small number of cases. RNA sequencing and transcriptomic profiling, as used in the Neurology Genetics study, can document decreased *ASXL2* expression in cases with structural variants, supporting pathogenic interpretations.[14] Proteomics and metabolomics have not been applied in SHAPNS cohorts, and no specific circulating biomarkers have been identified as diagnostic indicators.

Potential biomarkers include decreased ASXL2 mRNA or protein levels in peripheral blood or tissues, altered H3K27me3 or H3K4me1 patterns, and misexpression of HOX or developmental genes, but these remain research concepts rather than clinical tools.[15] Liquid biopsy approaches are not relevant given the congenital nature of SHAPNS and the lack of tumor involvement. FDA biomarker databases do not list SHAPNS-specific biomarkers.

### 10.4. Clinical Criteria, Differential Diagnosis, and Screening

Standardized diagnostic criteria for Shashi-Pena syndrome have not yet been formalized by professional societies, given the very small number of cases, but consensus clinical features include macrocephaly, developmental delay/intellectual disability, hypotonia, seizures, hypoglycemia, distinctive facial features with glabellar nevus flammeus, and minor congenital heart disease.[1][9][11][13][16] GeneReviews provides a clinical synopsis and genetically confirmed cases, serving as de facto criteria.[16][5]

Differential diagnosis includes other macrocephaly and overgrowth syndromes (e.g., Sotos syndrome, PTEN-related disorders), other ASXL-related disorders (Bohring-Opitz and Bainbridge-Ropers syndromes), and broader neurodevelopmental syndromes with facial dysmorphism and cardiac anomalies.[13][9][11] Distinguishing features include the specific facial gestalt with glabellar nevus flammeus, combination of hypoglycemia and minor congenital heart disease, and ASXL2 pathogenic variant. DECIPHER and DynaMed can facilitate differential diagnosis by cross-referencing phenotypes and genes.[7][14]

Screening for Shashi-Pena syndrome in asymptomatic populations is not currently performed, given its rarity and the absence of defining biochemical markers. Newborn screening programs do not include SHAPNS. However, cascade genetic testing for relatives of individuals with inherited *ASXL2* variants, such as the balanced translocation family, may be recommended to identify carriers and provide counseling.[14][16] Carrier screening in the general population is not warranted due to extremely low carrier frequency and lack of established panels including *ASXL2* for recessive traits.

## 11. Outcome and Prognosis

### 11.1. Survival, Mortality, and Life Expectancy

Data on survival and mortality in Shashi-Pena syndrome are limited, but available reports suggest that many individuals can survive into childhood and adolescence, with variable morbidity. The SciDirect case report mentions a Chinese patient with SHAPNS who experienced premature death, representing the first documented instance of premature mortality linked to SHAPNS in a Chinese demographic.[3] The cause of death is not elaborated in the abstract but may be related to seizures, hypoglycemia, cardiac complications, or other systemic issues.

Most other published cases, including the original AJHG cohort, Yuan’s newborn, and Mol Syndromol’s adolescent, do not report early mortality; these individuals survived through childhood and adolescence, albeit with significant developmental and medical challenges.[13][11][9] ARRE’s estimate of 50–60 diagnosed individuals globally suggests that many live years beyond diagnosis, though detailed survival statistics and life expectancy estimates are unavailable.[10] Orphanet does not currently provide life expectancy data for SHAPNS due to insufficient evidence.[6]

Absence of longitudinal data and systematic natural history studies hampers precise estimation of life expectancy. Nonetheless, given the congenital nature and potential for serious complications such as epilepsy, hypoglycemia, and heart disease, cautious assumption is that SHAPNS may modestly reduce life expectancy in some cases, particularly if complications are not optimally managed, while individuals with milder phenotypes may achieve near-normal lifespan.[3][9][11][13][16]

### 11.2. Morbidity, Disability, and Quality of Life

Morbidity in Shashi-Pena syndrome is substantial, driven by neurodevelopmental impairment, seizures, metabolic instability, cardiac defects, orthopedic and dental issues, and behavioral challenges. Disability outcomes include delays in motor and language development, cognitive limitations, and difficulties in daily living tasks. The International Classification of Functioning (ICF) framework would categorize limitations in body functions (neuromuscular, cognitive, metabolic), activities (mobility, communication, self-care), and participation (education, social integration).[1][10][16]

Quality of life is variably affected; families and patient advocacy organizations report significant challenges, but also highlight resilience and diverse abilities among individuals. EQ-5D and SF-36 instruments have not been systematically applied, but domains likely affected include mobility, self-care, usual activities, pain/discomfort (e.g., due to constipation or orthopedic issues), and anxiety/depression related to chronic illness.[1][10][16] PROMIS pediatric measures would be relevant for assessing physical function, fatigue, and psychosocial health in SHAPNS.

Recovery potential depends on domain. Developmental interventions can improve motor skills, communication, and cognitive function, but intellectual disability may persist, limiting complete recovery.[1][9][16] Seizures can sometimes be controlled with antiepileptic drugs; hypoglycemia can be managed with dietary and endocrine support, reducing acute morbidity.[11][16] Dental interventions can ameliorate oral health; orthopedic therapies can address musculoskeletal complications.[9][17] Behavioral therapies and supportive education can enhance social participation and quality of life.[1][10][16]

Prognostic factors likely include severity of neurodevelopmental impairment, frequency and control of seizures, degree of hypoglycemia, extent of cardiac involvement, availability of early interventions, and family support. However, formal prognostic models and biomarkers specific to SHAPNS have not been developed; prognostic assessment is currently individualized and based on clinical experience.[1][9][11][13][16]

## 12. Treatment and Management

### 12.1. Pharmacotherapy and Symptomatic Medications

There are currently no FDA-approved disease-modifying therapies for Shashi-Pena syndrome; treatment is targeted to individual symptoms and consists of supportive care.[1][16] NORD notes that treatment is tailored to specific manifestations, including developmental therapies and cardiology follow-up for congenital heart disease.[1] GeneReviews similarly emphasizes symptomatic management.[16]

Pharmacologic treatments focus on seizure control, management of hypoglycemia, and treatment of associated conditions. Antiepileptic drugs such as levetiracetam, valproic acid, or other agents may be used for seizure prophylaxis and control, following standard epilepsy guidelines (NCIT terms such as “Anticonvulsant Agent,” NCIT:C307). Hypoglycemia management involves glucose supplementation, dietary modifications to ensure stable carbohydrate intake, and potential use of endocrine therapies if hormonal abnormalities are identified.[11][16] NCIT terms for supportive metabolic therapies include “Glucose Supplement” (NCIT:C47233).

Other medications may address constipation (laxatives), gastroesophageal reflux (proton pump inhibitors), behavioral challenges (e.g., anxiolytics), and sleep disturbances, though these are general pediatric medications rather than SHAPNS-specific.[1][10][16] Cardiovascular medications may be needed for specific heart defects or rhythm disturbances, but minor congenital heart disease often requires monitoring rather than aggressive pharmacotherapy.[11][1]

Pharmacogenomics considerations have not been specifically studied in SHAPNS; there is no evidence that ASXL2 variants significantly alter drug metabolism pathways. Nonetheless, care should be taken in dosing, given developmental and metabolic differences in affected children.

### 12.2. Advanced Therapeutics and Experimental Approaches

Advanced therapeutics such as gene therapy, cell therapy, RNA-based therapies, targeted molecular therapies, and immunotherapies have not yet been applied to Shashi-Pena syndrome, and no clinical trials specifically targeting *ASXL2* or SHAPNS are registered in ClinicalTrials.gov as of the latest reports.[1][16] The ultra-rare nature of SHAPNS and its complex epigenetic mechanism pose challenges for gene therapy design.

Conceptually, gene replacement or gene editing approaches using viral vectors or CRISPR-Cas systems could restore ASXL2 function in affected tissues, potentially ameliorating developmental anomalies if applied early in development. However, practical barriers include timing (prenatal or neonatal delivery), tissue targeting (brain, heart, skeletal), risk of off-target effects, and ethical considerations. RNA-based therapies, such as antisense oligonucleotides, are less applicable because SHAPNS is caused by loss-of-function rather than toxic gain-of-function transcripts.[13][15]

Immunotherapies are not relevant, as SHAPNS does not involve autoimmune mechanisms. Targeted therapies directed at downstream pathways, such as modulation of mTOR or IGF signaling in overgrowth, could theoretically influence growth phenotypes, but no such interventions have been tested in SHAPNS.[9][15] At present, advanced therapeutics are speculative and not part of standard care.

### 12.3. Surgical and Interventional Procedures

Surgical interventions may be required for specific complications in Shashi-Pena syndrome. Cardiac surgery or catheter-based interventions may be necessary for congenital heart defects that are hemodynamically significant, following standard pediatric cardiology protocols.[11][1] NCIT terms include “Cardiac Surgery” (NCIT:C48920) and “Cardiac Catheterization” (NCIT:C49997). Orthopedic surgery may be indicated for skeletal deformities or contractures, though such procedures have not been widely reported in SHAPNS cases.[10][15]

Dental and maxillofacial interventions, including orthodontics, tooth extraction, and corrective surgery, may be needed for dental anomalies and jaw misalignment, as described in oral findings and healthcare management for SHAPNS.[17] NCIT terms for dental interventions include “Orthodontic Procedure” (NCIT:C15378). Gastrointestinal surgeries are unlikely unless complications such as severe constipation lead to structural issues.

These surgical interventions are not specific to SHAPNS but address associated malformations and functional impairments. Timing and outcomes depend on individual pathology and general pediatric surgical guidelines.[1][11][17]

### 12.4. Supportive Care and Rehabilitation

Supportive and rehabilitative care are central to Shashi-Pena syndrome management. Physical therapy (NCIT:C28253) addresses hypotonia, motor delay, and coordination; occupational therapy helps with fine motor skills, daily living activities, and sensory integration; and speech therapy focuses on language development and communication skills.[1][10][16] Early initiation of these therapies in infancy and early childhood can significantly improve motor and cognitive outcomes.

Nutritional support is critical for managing feeding difficulties and hypoglycemia, involving dietitian-guided plans to ensure adequate caloric intake and stable blood glucose. Behavioral therapies and psychological support address behavioral challenges, sensory sensitivities, and family coping.[1][10][16] Educational interventions, including individualized education plans (IEPs), accommodations, and special education services, help optimize learning and social integration.[1][10]

Cardiology follow-up and routine surveillance of heart defects, as recommended by NORD, ensure timely detection and management of cardiac complications.[1] Gastroenterology consultation may be necessary for chronic constipation or feeding issues. Dental care focusing on preventive measures, orthodontic evaluation, and treatment of anomalies is important for oral health and function.[9][17]

### 12.5. Treatment Outcomes and Personalized Medicine

Treatment outcomes in Shashi-Pena syndrome are heterogeneous. Some individuals respond well to seizure medications and have infrequent episodes; others experience refractory epilepsy. Hypoglycemia can often be controlled with diet and monitoring, reducing hospitalizations.[11][1][16] Developmental therapies can lead to significant gains in motor and language skills, though intellectual disability may persist.[1][9][16] Behavioral interventions can improve social functioning and reduce disruptive behaviors.[10]

Side effects and adverse events from treatments follow general patterns for pediatric medications (e.g., sedation from antiepileptics, gastrointestinal side effects from laxatives) and are not unique to SHAPNS. Pharmacovigilance using FAERS and MedWatch is standard but does not highlight SHAPNS-specific issues.

Personalized medicine approaches in SHAPNS could involve genotype-guided prognosis and management. For example, individuals with structural *ASXL2* variants might be monitored more closely for Hematologic or cardiac phenotypes, given murine data; those with milder truncating variants might be anticipated to have less severe neurodevelopmental impairment. However, current case numbers are insufficient to robustly correlate specific variants with outcomes, and personalized medicine remains largely conceptual.[3][9][11][13][15]

## 13. Prevention and Genetic Counseling

### 13.1. Primary, Secondary, and Tertiary Prevention

Primary prevention of Shashi-Pena syndrome through environmental or lifestyle modifications is not feasible, given its genetic etiology and de novo mutation patterns. There are no vaccines or prophylactic medications that prevent *ASXL2* mutations.[1][13][16] However, genetic counseling and reproductive planning can reduce recurrence risk in families with known *ASXL2* variants.

Secondary prevention focuses on early detection and intervention to mitigate severity of manifestations. Early diagnosis via genetic testing enables prompt initiation of developmental therapies, seizure management, hypoglycemia monitoring, and cardiac surveillance, thereby reducing complications and improving outcomes.[1][11][16] Newborn screening does not currently include SHAPNS, but high-risk infants (e.g., those with macrocephaly and hypoglycemia) might be prioritized for early genetic evaluation, serving as a form of targeted secondary prevention.

Tertiary prevention aims to prevent complications and disability in individuals with SHAPNS. This includes long-term management of seizures, hypoglycemia, cardiac defects, constipation, orthopedic issues, and behavioral challenges, as well as psychosocial support to minimize social isolation and psychiatric comorbidities.[1][10][16] Tertiary prevention is implemented through multidisciplinary care teams and ongoing follow-up.

### 13.2. Genetic Counseling, Prenatal and Preimplantation Diagnosis

Genetic counseling is essential for families affected by Shashi-Pena syndrome. GeneReviews notes that once an *ASXL2* pathogenic variant has been identified in an affected family member, prenatal and preimplantation genetic testing are possible.[16] Counselors discuss inheritance patterns, recurrence risks, variant effects, and reproductive options. For de novo variants, recurrence risk is low but non-zero due to potential parental germline mosaicism; for inherited variants, such as balanced translocations, recurrence risk is 50%.[1][14][16]

Prenatal testing via chorionic villus sampling or amniocentesis can detect known familial *ASXL2* variants in the fetus, allowing informed decisions and early planning.[16] Preimplantation genetic diagnosis (PGD) enables selection of embryos without the pathogenic variant in assisted reproductive technologies. NCIT terms for these interventions include “Prenatal Genetic Testing” (NCIT:C17956) and “Preimplantation Genetic Diagnosis” (NCIT:C18189).

Carrier screening in the general population is not recommended, but targeted testing of at-risk relatives in families with inherited *ASXL2* variants is advisable.[14][16] Genetic counseling encompasses discussions of psychosocial implications, ethical considerations, and support resources, including patient advocacy organizations like ARRE.[10][16]

### 13.3. Public Health and Environmental Interventions

Public health interventions specific to Shashi-Pena syndrome are not currently implemented, given its rarity. Health education may include information for clinicians on recognizing SHAPNS and referring patients for genetic testing, thereby reducing diagnostic delay.[1][13][16] Broader environmental interventions, such as reducing exposure to toxins or improving nutrition, are generic and not targeted to SHAPNS.

Vector control, sanitation, and immunization strategies are irrelevant to SHAPNS, as it is not infectious or environmentally driven. Public health emphasis remains on supporting rare disease networks, genetic services, and inclusion of SHAPNS in rare disease registries to facilitate research and care coordination.[1][6][10][16]

## 14. Other Species and Natural Disease

### 14.1. ASXL2 Orthologs and Comparative Biology

Orthologous genes for ASXL2 exist in multiple species, including mice (*Asxl2*), where NCBI Gene IDs and model organism databases catalog gene-targeted mutants.[15] ASXL2 orthologs in *Drosophila* correspond to Additional sex combs (Asx), which regulates PcG and TrxG balance, and in other vertebrates as part of the conserved ASXL family.[15] These orthologs share domains and functions related to chromatin regulation and developmental gene expression, underscoring evolutionary conservation of ASXL2 mechanisms.

Comparative biology studies highlight similarities and differences in ASXL2 function across species. In mice, *Asxl2* knockout or gene-trap mutants exhibit axial skeleton transformations, congenital heart malformations, reduced body weight, osteopetrosis, low bone mineral density, lipodystrophy, insulin resistance, and hematopoietic defects.[15] These phenotypes overlap with human SHAPNS manifestations (congenital heart disease, metabolic issues, orthopedic complications) but differ in growth (reduced body weight in mice vs overgrowth or normal growth in humans), illustrating species-specific phenotypic outcomes of ASXL2 loss.[9][11][15]

### 14.2. Natural Disease in Animals and Zoonotic Potential

No naturally occurring Shashi-Pena-like syndrome has been described in companion animals or livestock, and OMIA does not list an animal disease directly equivalent to SHAPNS. Animal models of *Asxl2* loss are induced genetic models rather than spontaneous diseases.[15] Veterinary relevance is therefore primarily in the context of research animals rather than clinical veterinary practice.

Shashi-Pena syndrome is not transmissible and has no zoonotic potential. ASXL2 mutations do not spread between species, and cross-species susceptibility is limited to experimental gene-targeted models. Transmission is strictly genetic within human families, and there is no infectious agent to consider.[1][13][14][15]

### 14.3. Comparative Pathology and Evolutionary Conservation

Comparative pathology between human SHAPNS and murine *Asxl2* models illustrates conserved roles of ASXL2 in developmental processes, including axial skeleton patterning, cardiac morphogenesis, and metabolic regulation.[15] Evolutionary conservation of ASXL2’s domains and interactions with PcG/TrxG complexes supports the assumption that core mechanisms of epigenetic regulation are preserved across vertebrates. HomoloGene and Alliance of Genome Resources data would show conserved ASXL2 orthologs and phenotypes, though SHAPNS-specific mapping is not yet available.

Differences in phenotypic expression, such as reduced body weight in mice versus macrocephaly and overgrowth in humans, indicate that species-specific contexts (genetic backgrounds, developmental trajectories, environmental conditions) modulate outcomes of ASXL2 loss. This emphasizes the importance of cautious extrapolation from animal models to human disease, while still leveraging their mechanistic insights.[15][9][11]

## 15. Model Organisms

### 15.1. Mouse Models of Asxl2 Deficiency

Mouse models of *Asxl2* deficiency are critical for understanding the mechanistic underpinnings of Shashi-Pena syndrome. Several types of models have been described, including gene-trap constitutive knockout models (*Asxl2Gt(AQ0356)*) and conditional knockout models (*Mx1*-cre *Asxl2*^fl/fl^).[15] These models provide insight into the role of Asxl2 in embryonic development, cardiac morphogenesis, skeletal patterning, hematopoiesis, bone metabolism, and adipogenesis.

Gene-trap *Asxl2* mutants exhibit partially embryonic lethality, axial skeleton transformations, reduced body weight, congenital heart malformations, low bone mineral density, osteopetrosis, lipodystrophy, and insulin resistance.[15] These phenotypes demonstrate that Asxl2 is essential for normal development of the skeleton, heart, and metabolic tissues. Epigenetic analyses show reduction in bulk H3K27me3 levels in cardiac tissue, confirming Asxl2’s role in PRC2 recruitment and histone methylation.[15]

Conditional *Asxl2* knockout in hematopoietic cells using *Mx1*-cre results in cytopenias, impaired hematopoietic stem and progenitor cell self-renewal, and reduced H3K4me1 levels, indicating Asxl2’s importance in hematopoietic homeostasis and enhancer regulation.[15] These hematopoietic phenotypes have not yet been observed in human SHAPNS but may inspire targeted evaluations in patients.

Model organism databases such as MGI and IMPC catalog these *Asxl2* models, including phenotypic annotations and available strains for research. Phenotype recapitulation in these models is partial; they capture cardiac, skeletal, and metabolic aspects of ASXL2 deficiency but not the full spectrum of human neurodevelopmental and craniofacial features seen in SHAPNS. Nonetheless, they are invaluable for mechanistic studies and preclinical exploration.[15]

### 15.2. Model Limitations and Applications

Limitations of *Asxl2* mouse models include differences in growth trajectories (reduced body weight vs human macrocephaly/overgrowth), incomplete representation of cognitive and behavioral phenotypes, and species-specific gene regulatory networks. Mouse brains may not fully model human neurodevelopment, especially higher cognitive functions, limiting translational relevance for intellectual disability and behavioral challenges.[15][9][11]

However, these models offer strong platforms for studying developmental epigenetics, cardiac morphogenesis, skeletal patterning, and metabolic regulation. Applications include testing hypotheses on PcG/TrxG balance, analyzing gene expression networks downstream of Asxl2, and evaluating potential therapeutic strategies targeting epigenetic modifiers or metabolic pathways. For example, modulating PRC2 activity or PPARγ function in mice could reveal pathways amenable to pharmacologic intervention in SHAPNS.[15]

Future models, such as human induced pluripotent stem cell (iPSC) lines with *ASXL2* loss-of-function, brain organoids, and CRISPR-edited human cell lines, could provide more accurate human-specific insights into neuronal and craniofacial development. These cellular models would allow single-cell and spatial transcriptomics, functional genomics screens, and multi-omics integration to dissect mechanisms in SHAPNS at high resolution.

In summary, *Asxl2* mouse models recapitulate key aspects of ASXL2 deficiency and are crucial for mechanistic research, but they do not fully reproduce the human SHAPNS phenotype, necessitating complementary human cell-based models and careful translational interpretation.[15][9][11][13]

## Conclusion

Shashi-Pena syndrome is an ultra-rare, autosomal dominant neurodevelopmental and multiple malformation syndrome caused by germline heterozygous disruption of the epigenetic regulator *ASXL2*. It presents at birth with macrocephaly, distinctive craniofacial features including glabellar nevus flammeus, hypotonia, developmental delay or intellectual disability, hypoglycemia, minor congenital heart disease, seizures, and a range of additional manifestations affecting dental, gastrointestinal, orthopedic, and behavioral domains, with substantial inter-individual variability. The disorder is mechanistically rooted in ASXL2 haploinsufficiency, leading to impaired recruitment of Polycomb repressive complex 2, altered histone methylation (e.g., H3K27me3, H3K4me1), and dysregulated developmental gene expression across multiple tissues. Murine *Asxl2* models confirm ASXL2’s roles in cardiac morphogenesis, skeletal patterning, metabolic regulation, and hematopoiesis, providing a mechanistic framework that aligns with many human SHAPNS features, though species-specific differences exist.

Diagnostically, Shashi-Pena syndrome is recognized by its clinical gestalt and confirmed through genetic testing, primarily whole exome sequencing or targeted *ASXL2* analysis. Structural chromosomal rearrangements such as balanced translocations disrupting *ASXL2* highlight the need for comprehensive genomic evaluation, including karyotyping and long-read sequencing in some cases. There are no disease-specific biomarkers or standardized diagnostic criteria yet, but gene-based diagnosis and careful phenotyping allow accurate classification. Epidemiologically, SHAPNS is extremely rare, with approximately 23 individuals reported in the medical literature as of 2023 and an estimated 50–60 diagnosed globally, and displays high penetrance with variable expressivity of specific features like epilepsy and overgrowth.

Management of SHAPNS is symptomatic and multidisciplinary, encompassing seizure control, hypoglycemia management, cardiology follow-up, developmental and behavioral therapies, dental and orthopedic care, and psychosocial support. There are no disease-modifying pharmacologic or gene-based therapies at present. Genetic counseling is essential, with prenatal and preimplantation genetic testing available once a familial *ASXL2* variant is identified. Future research priorities include expanding case series to better define the natural history and phenotypic spectrum, performing multi-omics profiling to elucidate downstream pathways and identify biomarkers, refining model organisms and human cellular models for mechanistic studies, and exploring potential targeted interventions at the level of epigenetic modifiers or metabolic pathways. Integration of SHAPNS into rare disease registries, ontologies (MONDO:0014963, OMIM:617190, ORPHA:689408), and knowledge bases will facilitate improved diagnosis, research coordination, and ultimately more effective care for individuals affected by this complex and intriguing epigenetic neurodevelopmental syndrome.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 96 |
| Resolved | 87 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 5 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0004288` (1 mention) - the report calls it "vertebral column"; UBERON calls it **skeleton**
- `UBERON:0008896` (1 mention) - the report calls it "skeleton"; UBERON calls it **post-hyoid pharyngeal arch**
- `NCIT:C48920` (1 mention) - the report calls it "Cardiac Surgery"; NCIT calls it **Quantile**
- `NCIT:C49997` (1 mention) - the report calls it "Cardiac Catheterization"; NCIT calls it **Imager Device**
- `NCIT:C17956` (1 mention) - the report calls it "Prenatal Genetic Testing"; NCIT calls it **Cytochrome P450 19A1**
- `NCIT:C18189` (1 mention) - the report calls it "Preimplantation Genetic Diagnosis"; NCIT calls it **Pathology**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000724` (1 mention) - HP does not contain this term
- `NCIT:C47233` (1 mention), reported as "Glucose Supplement" - NCIT does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016585` (obsolete chromatin remodeling complex) (1 mention)
- `GO:0031060` (obsolete regulation of histone methylation) (1 mention)
- `CL:0000664` (obsolete closable valve cell) (1 mention) - replaced by `CL:1000147`
- `CL:0000672` (obsolete tracheary element) (1 mention) - replaced by `PO:0000290`
- `NCIT:C17956` (Cytochrome P450 19A1) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15378` (1 mention) - the report calls it "Orthodontic Procedure"; NCIT calls it **Boron Neutron Capture Therapy**, and lists "Neutron capture therapy (procedure)" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.