---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T07:47:59.173570'
end_time: '2026-10-15T07:52:07.399283'
duration_seconds: 248.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IFIH1-Related Type 1 Interferonopathy
  mondo_id: MONDO:0700262
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 57
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 25
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - DOI:10.1007/s12688-026-00957-1
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 89
  verified: 84
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 16
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: UBERON:0002048
    reported_labels:
    - Lung/pulmonary vasculature
    ontology_label: lung
  - term_id: UBERON:0000970
    reported_labels:
    - Eye/anterior chamber
    ontology_label: eye
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0039528
    ontology_label: GO_0039528
    replaced_by: GO:0002753
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IFIH1-Related Type 1 Interferonopathy
- **MONDO ID:** MONDO:0700262 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IFIH1-Related Type 1 Interferonopathy** covering all of the
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

# IFIH1-Related Type 1 Interferonopathy  
**Disease-knowledge-base research report — evidence reviewed through 15 October 2026**

## Executive summary

**IFIH1-related type 1 interferonopathy (MONDO:0700262)** is a rare, autosomal-dominant Mendelian immune-dysregulation disorder caused principally by heterozygous germline **gain-of-function (GOF) variants in IFIH1**, encoding the cytosolic double-stranded-RNA sensor MDA5. It is best understood as one continuous, variably penetrant disease spectrum encompassing **Aicardi–Goutières syndrome type 7 (AGS7)**, neuroregression/spastic-dystonic and spastic-paraparetic phenotypes, **Singleton–Merten syndrome type 1 (SMS1)**, lupus-like or organ-predominant inflammation, and clinically asymptomatic carriers with an elevated interferon signature. The ClinGen/GenCC-style 2024 evaluation classifies the IFIH1–disease relationship as **definitive** and deliberately “lumps” AGS7 and SMS1 under MONDO:0700262. [GenCC submission, 23 August 2024, URL](https://thegencc.org/submissions/SGC-107465.2) [64][69]

The largest dedicated cohort comprised **74 variant-positive people from 51 families with 27 likely pathogenic variants**. Ten carriers (**13.5%**) were clinically asymptomatic, including seven older than 50 years, demonstrating incomplete penetrance; nevertheless, nearly all tested variants or carriers showed elevated type-I-interferon signaling. [Rice et al., *Human Mutation*, published online 14 January 2020, PMID: **31898846**](https://pubmed.ncbi.nlm.nih.gov/31898846/) [31][39]

> **Key primary-literature quote:** “We identified 74 individuals from 51 families segregating a total of 27 likely pathogenic mutations in IFIH1.” [PMID: 31898846] [31]

There is **no approved disease-specific curative therapy**. Off-label JAK1/2 inhibition—particularly baricitinib or ruxolitinib—is the leading targeted strategy. It can suppress the interferon signature and improve inflammatory, skin, systemic, and sometimes developmental outcomes, but reversal of established brain injury is uncertain and infections and cytopenias are important risks. [Vanderver et al., *NEJM*, 3 September 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7495410/) [155]

---

# 1. Disease information

## 1.1 Definition and scope

IFIH1-related type 1 interferonopathy is a **monogenic autoinflammatory/autoimmune disorder of innate nucleic-acid sensing**. Constitutively or excessively active MDA5 produces inappropriate type-I-interferon signaling in the absence of an adequate viral threat. The resulting phenotype ranges from prenatal or infantile encephalopathy to later spastic paraparesis, vascular/dental/skeletal calcific disease, isolated inflammatory manifestations, or biochemical nonpenetrance.

The umbrella concept is preferable to treating AGS7 and SMS1 as unrelated disorders because:

1. both result from monoallelic IFIH1 GOF;
2. neurological, cutaneous, skeletal, dental, and vascular phenotypes overlap;
3. the same variant may produce markedly different disease within a family; and
4. elevated interferon-stimulated gene expression is a shared biological feature. [33][64]

## 1.2 Identifiers and names

| Resource | Identifier/name | Interpretation or URL |
|---|---|---|
| MONDO | **MONDO:0700262 — IFIH1-related type 1 interferonopathy** | Umbrella disease entity; [GenCC](https://thegencc.org/submissions/SGC-107465.2) [64] |
| MONDO | MONDO:0014367 — Aicardi–Goutières syndrome 7 | Neurological subphenotype [65] |
| OMIM disease | **615846 — Aicardi–Goutières syndrome 7** | AD IFIH1 GOF disease; [OMIM](https://omim.org/entry/615846) [61] |
| OMIM disease | **182250 — Singleton–Merten syndrome 1** | AD IFIH1 GOF disease; [OMIM](https://omim.org/entry/182250) [62] |
| OMIM gene | **606951 — IFIH1** | Gene record [10] |
| Orphanet | **ORPHA:51 — Aicardi–Goutières syndrome** | Genetically heterogeneous umbrella AGS entry [73] |
| Orphanet | **ORPHA:85191 — Singleton–Merten dysplasia** | Calcific/dental/skeletal presentation [62][63] |
| ICD-10 | No unique IFIH1 code; AGS generally coded under rare/other specified neurological or genetic disease; SMS may map to **Q78.8** | Q78.8 = other specified osteochondrodysplasias [63] |
| ICD-11 | No uniquely specific IFIH1 code identified; SMS mapping **LD24.KY** | “Other specified osteochondrodysplasias” mapping reported by Orphanet [63] |
| MeSH | No dedicated IFIH1-interferonopathy descriptor | Use *Aicardi-Goutières Syndrome*, *Interferon Type I*, *IFIH1 protein, human*, and relevant phenotype headings |
| MedGen | C3888244 — AGS7 | [NCBI MedGen](https://ncbi.nlm.nih.gov/medgen/C3888244/) [65] |

**Synonyms:** IFIH1 gain-of-function disease; MDA5 gain-of-function disease; MDA5-associated interferonopathy; IFIH1-associated autoinflammation; AGS7; Aicardi–Goutières syndrome due to IFIH1; Singleton–Merten syndrome 1; IFIH1-related Singleton–Merten dysplasia.

## 1.3 Evidence granularity

This report is based primarily on **aggregated disease-level resources and published cohorts**, supplemented by individual case reports and pedigrees. It is not derived from a single patient’s EHR. A 2024 real-world/natural-history analysis included 19 IFIH1-positive patients among 167 molecularly diagnosed AGS patients, but those data concern genetically heterogeneous AGS and should not automatically be generalized to every IFIH1 carrier. [138]

---

# 2. Etiology

## 2.1 Primary cause

The established cause is a **heterozygous constitutional GOF variant in IFIH1**. Most confirmed variants are missense substitutions in or near the MDA5 helicase/ATP- and RNA-interacting regions. A 2024 report expanded the mechanism to an in-frame deletion, **p.Glu794del**, showing that not every pathogenic GOF allele is missense. [MDA5 p.Glu794del report, 2 October 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11447049/) [76]

GOF can result from:

- increased affinity for endogenous or viral dsRNA;
- constitutive or reduced-threshold signaling;
- impaired ATP hydrolysis;
- slower MDA5 filament disassembly;
- prolonged MAVS activation.

## 2.2 Genetic risk factors

| Factor | Evidence and interpretation |
|---|---|
| Pathogenic IFIH1 GOF allele | Necessary primary causal factor in established cases |
| De novo occurrence | Common in severe infantile AGS-like disease; 22 of the 27 cohort variants occurred de novo in at least one patient [39] |
| Familial AD inheritance | Produces a 50% transmission risk per conception, but not a 50% certainty of clinical disease because penetrance is incomplete |
| Variant location/function | Most disease alleles cluster around helicase ATP/RNA-binding structures; functional assay evidence is more reliable than in-silico prediction |
| Modifier alleles | Suspected, not established; implied by severe intrafamilial variability and unaffected carriers |
| Parental mosaicism | Documented: paternal mosaic IFIH1 mutation caused affected siblings, supporting recurrence risk above the usual de novo baseline [Neurology Genetics, 19 December 2019](https://www.neurology.org/doi/10.1212/NXG.0000000000000384) [29] |

Common IFIH1 polymorphisms influence polygenic autoimmunity and antiviral responses, but these susceptibility associations are **not equivalent** to monogenic GOF interferonopathy. Conversely, monoallelic or biallelic loss-of-function can predispose to viral disease/immunodeficiency and should not be classified as the same mechanism. [44]

## 2.3 Environmental and infectious risk factors

No toxin, diet, occupation, smoking exposure, alcohol exposure, or lifestyle behavior is established as a primary cause.

**Infection or dsRNA exposure is a biologically plausible disease modifier.** In an MDA5-R822Q mouse model, poly(I:C), a synthetic dsRNA analogue, sharply exacerbated inflammation and mortality; deleting MAVS or IFNAR prevented this enhancement. This is strong model-organism evidence for gene–immune-trigger interaction but not proof that a particular human virus initiates disease. [121][126]

Clinical neuroregression can occur after apparently normal development and may appear temporally associated with febrile illness, but published evidence does not establish one infectious agent as necessary or sufficient.

## 2.4 Protective factors

No validated environmental protective factor exists.

Potential genetic/biological protection is inferred from:

- alleles that reduce MDA5 signaling, known to protect against some autoimmune phenotypes in population studies;
- unidentified modifier genes in unaffected GOF carriers;
- intact negative regulators of MDA5–MAVS and IFNAR signaling.

These are mechanistic hypotheses, not clinically actionable protective genotypes. Routine deliberate infection avoidance beyond standard care, special diets, or supplements have not been proven to prevent onset.

---

# 3. Phenotypes

Phenotypic frequency estimates are limited by ascertainment bias toward pediatric neurological disease. In the 74-person cohort, at least 20 had unequivocal rapid neuroregression, ten were clinically asymptomatic, and six symptomatic patients had died. Imaging findings were not systematically recorded, so precise percentages are unavailable. [39]

## 3.1 Phenotype catalogue

| Phenotype type | Manifestation and suggested HPO term | Onset/course/frequency | Functional and quality-of-life effect |
|---|---|---|---|
| Symptom/sign | Developmental delay — **HP:0001263** | Congenital or infantile; common in AGS-like cases; variable severity | Dependence for mobility, feeding, communication and self-care |
| Symptom/sign | Developmental regression — **HP:0002376** | Acute/subacute, usually infancy; at least 20/74 carriers had unequivocal rapid regression; seven regressed after age 1 following normal development [39] | Loss of motor, language and adaptive skills |
| Sign | Spasticity — **HP:0001257**; spastic paraparesis — **HP:0002313** | Infantile through adolescent onset; may progress slowly; one cohort patient began at 13 years | Gait impairment, contractures, wheelchair need |
| Sign | Dystonia — **HP:0001332** | Often follows neuroregression; variable | Pain, abnormal posture, impaired hand use and ambulation |
| Sign | Axial hypotonia — **HP:0008936** | Usually infantile, often preceding later spasticity | Poor head/trunk control |
| Symptom | Irritability — **HP:0000737** | Often prominent during active infantile encephalopathy | Sleep and feeding disruption; caregiver burden |
| Sign | Acquired/progressive microcephaly — **HP:0000252/HP:0000253** | Slowing of head growth after inflammatory neurological injury | Correlates with severe neurodevelopmental morbidity |
| Imaging | Intracranial/basal-ganglia calcification — **HP:0002514** | Congenital or childhood; sometimes present without neurological signs | Diagnostic clue; direct daily-life impact depends on associated injury |
| Imaging | Cerebral white-matter abnormality/leukodystrophy — **HP:0002500** | Variable; unilateral disease has occurred | Motor, cognitive or visual consequences; may be clinically silent |
| Imaging | Cerebral atrophy — **HP:0002059** | Often develops after encephalopathic phase | Usually indicates irreversible structural injury |
| Laboratory | Elevated interferon-stimulated gene expression — **HP:0032155** (type-I IFN signature; confirm current HPO label) | Persistent or fluctuating; present even in many asymptomatic carriers | Biomarker, not itself a patient-reported symptom |
| Laboratory | CSF lymphocytosis — **HP:0200149** | More likely during early active disease | Indicates neuroinflammation |
| Laboratory | Elevated CSF interferon-α / neopterin | Often early, not universal | Diagnostic rather than direct functional impact |
| Skin | Chilblains/perniosis — **HP:0009710** | Episodic, cold-sensitive; AGS-wide estimate up to 40%, but IFIH1-specific rate unavailable [166] | Pain, ulceration and reduced hand/foot use |
| Skin | Psoriasiform dermatitis — **HP:0003765** | Chronic or fluctuating; uncommon | Pruritus, pain and psychosocial burden |
| Immune | Sterile fever — **HP:0001945** | Episodic, particularly active phase | Fatigue, discomfort and hospitalization |
| Immune | Lupus-like disease/autoimmunity — **HP:0002725** | Uncommon but established within spectrum | Organ-specific morbidity, medication burden |
| Hepatic | Elevated transaminases/hepatitis — **HP:0002910/HP:0012115** | Congenital systemic disease or isolated childhood liver presentation | Ranges from laboratory finding to hepatic dysfunction |
| Dental | Delayed tooth eruption — **HP:0000684** | Childhood; core SMS feature | Feeding, speech, appearance and dental-prosthetic burden |
| Dental | Premature loss of permanent teeth — **HP:0006480** | Childhood/adolescence; progressive | Major chewing, speech and psychosocial effects |
| Skeletal | Osteopenia/osteoporosis — **HP:0000938/HP:0000939** | Childhood onward in SMS | Fracture risk, pain, reduced activity |
| Skeletal | Acro-osteolysis — **HP:0001171** | Progressive | Hand/foot deformity and reduced dexterity |
| Skeletal | Widened medullary cavities of phalanges | Childhood | Radiographic hallmark; variable functional effect |
| Cardiovascular | Aortic calcification — **HP:0004963** | Childhood or puberty; progressive | Stenosis, surgery risk, potentially early death |
| Cardiovascular | Aortic/mitral-valve calcification — **HP:0004382** or appropriate valve-specific HPO term | Progressive SMS manifestation | Heart failure, arrhythmia or intervention risk |
| Cardiopulmonary | Pulmonary hypertension — **HP:0002092** | Rare but serious; found postmortem in one cohort death | Exercise limitation and mortality risk |
| Eye | Glaucoma — **HP:0000501** | Less frequent SMS manifestation | Progressive visual loss |
| Endocrine | Hypothyroidism — **HP:0000821** | Uncommon | Fatigue, growth and developmental effects |
| Carrier state | Clinical nonpenetrance — **HP:0003828** | 10/74 carriers (13.5%); seven older than 50 years [31] | No overt impairment despite genotype; biomarker may remain abnormal |

The core SMS phenotype comprises aortic/valvular calcification, delayed eruption and abnormal root formation, early permanent-tooth loss, osteoporosis and acro-osteolysis; glaucoma, psoriasis, muscle weakness and joint laxity are less consistent. [167][179]

No disease-specific validated EQ-5D, SF-36 or PROMIS dataset was found. Quality-of-life effects must therefore be inferred from neurological dependence, communication impairment, recurrent inflammatory symptoms, dental loss, cardiopulmonary disease and caregiver burden.

---

# 4. Genetic and molecular information

## 4.1 Gene and protein

| Attribute | Value |
|---|---|
| Gene | **IFIH1**, interferon induced with helicase C domain 1 |
| HGNC | **HGNC:18873** |
| NCBI Gene | **64135** |
| Ensembl | **ENSG00000115267** |
| OMIM | **606951** |
| Locus | **2q24.2** |
| GRCh38 interval | chr2:162,267,074–162,318,684, reverse strand |
| Protein | MDA5; interferon-induced helicase C-domain-containing protein 1 |
| UniProt | **Q9BYX4** |
| Principal transcript used in 2020 cohort | NM_022168.2; current clinical reporting should use the laboratory-specified current MANE transcript |
| Main compartments | Cytosol; signaling complex associated with mitochondrial MAVS; reported nuclear localization during apoptosis |

These identifiers are supported by NCBI Gene and UniProt. [46][47][49]

## 4.2 Pathogenic variant spectrum

All variants in the landmark cohort were germline/constitutional and heterozygous. Population frequencies were absent or ultra-rare. **Do not infer benignity solely from computational prediction:** six of 27 variants, 22%, were called benign by multiple in-silico tools despite functional/biomarker evidence of GOF. [31]

| Variant (NM_022168.2) | Protein | Reported population frequency in cohort paper | Principal reported phenotype(s) |
|---|---|---:|---|
| c.992C>G | p.Thr331Arg | Absent | AGS–SMS overlap; SMS |
| c.992C>T | p.Thr331Ile | Absent | SMS |
| c.1009A>G | p.Arg337Gly | Absent | Neuroregression |
| c.1165G>A | p.Gly389Arg | Absent | AGS, spastic paraparesis, nonpenetrance |
| c.1178A>T | p.Asp393Val | Absent | Neuroregression |
| c.1178A>C | p.Asp393Ala | Absent | AGS |
| c.1331A>G | p.Glu444Gly | Absent | Severe AGS |
| c.1347C>G | p.Asn449Lys | Absent | Spastic paraparesis |
| c.1465G>A | p.Ala489Thr | Absent | Chilblains, AGS–SMS, SMS |
| c.1483G>A | p.Gly495Arg | Absent | Spastic paraparesis, lupus-like disease |
| c.1747A>G | p.Ile583Val | Absent | AGS |
| c.2156C>T | p.Ala719Val | Absent | AGS |
| c.2159G>A | p.Arg720Gln | Absent | AGS or spastic paraparesis |
| c.2317G>C | p.Glu773Gln | Absent | Neuroregression |
| c.2335C>T | p.Arg779Cys | Absent | AGS, lupus-like disease, paraparesis, nonpenetrance |
| c.2336G>A | p.Arg779His | 1/244,230 alleles | AGS, neuroregression, paraparesis, nonpenetrance |
| c.2336G>T | p.Arg779Leu | Absent | AGS |
| c.2342G>A | p.Gly781Glu | Absent | Neuroregression or paraparesis |
| c.2404A>G | p.Asn802Asp | Absent | Neuroregression |
| c.2407A>T | p.Ile803Phe | Absent | AGS |
| c.2465G>A | p.Arg822Gln | 6/244,096 alleles | SMS; spastic-dystonic/calcification phenotype |
| c.2471G>A | p.Arg824Lys | Absent | Neuroregression or isolated liver disease |
| c.2486C>G | p.Thr829Ser | Absent | AGS |
| c.2544T>G | p.Asp848Glu | Absent | Paraparesis/calcification or nonpenetrance |
| c.2561T>A | p.Met854Lys | Absent | AGS–SMS overlap |
| c.2866A>G | p.Ile956Val | Absent | Paraparesis/calcification or nonpenetrance |
| c.2936T>G | p.Leu979Trp | Absent | Severe AGS |
| Later expansion | p.Glu794del | Ultra-rare/novel | AGS-like disease; first reported in-frame-deletion GOF mechanism [76] |

Full cohort source: [Rice et al., PMID: 31898846](https://pmc.ncbi.nlm.nih.gov/articles/PMC7457149/) [39].

**ACMG interpretation:** classifications vary by ClinVar submitter and date. A rare missense or in-frame variant should generally require segregation/de novo evidence, a compatible phenotype, blood interferon signature and preferably a validated IFNβ reporter, RNA-binding, ATPase or filament assay. A negative family history is weak counter-evidence because both de novo disease and nonpenetrance are common.

## 4.3 Other genomic features

- **Structural variants/chromosomal abnormalities:** no recurrent CNV, translocation, inversion or aneuploidy is established as the characteristic cause.
- **Somatic disease:** the recognized disorder is germline; postzygotic parental mosaicism is relevant to recurrence. Disease-causing somatic-only IFIH1 GOF is not established as a major category.
- **Epigenetics:** no reproducible disease-specific methylation episignature or causal chromatin defect has been validated.
- **Modifier genes:** none conclusively identified.
- **Anticipation/founder effect:** no evidence for repeat-associated anticipation or a major founder allele.
- **Consanguinity:** not a risk factor for dominant GOF disease, although it is relevant when considering recessive AGS genes or IFIH1 loss-of-function immunodeficiency.

---

# 5. Environmental information

| Domain | Current evidence |
|---|---|
| Toxins/radiation/pollution | No established causal association |
| Smoking/alcohol/diet/exercise | No demonstrated effect on penetrance or progression |
| Temperature | Cold can precipitate or worsen chilblains but does not cause the genetic disorder |
| Viral infection | Wild-type MDA5 is a viral-dsRNA sensor; infection is a plausible flare trigger, but no specific pathogen is required |
| Vaccination | No evidence that routine vaccination causes IFIH1 disease; individual risk assessment is appropriate during immunosuppression |
| Synthetic dsRNA | Poly(I:C) markedly exacerbates disease in MDA5-GOF models, supporting trigger sensitivity [81][121] |

The correct knowledge-base representation is therefore **genetic cause with possible infection/innate-immune-stimulation modifiers**, not a communicable or environmentally acquired disease.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **A heterozygous IFIH1 GOF variant leads to** an MDA5 receptor with increased RNA affinity, increased basal activity, impaired ATP-driven turnover, or reduced filament disassembly.
2. **Abnormally stable or readily formed MDA5–dsRNA filaments lead to** excessive oligomerization of MDA5 CARD domains.
3. **CARD oligomerization leads to** persistent activation of mitochondrial antiviral-signaling protein **MAVS** on the outer mitochondrial membrane.
4. **MAVS activation leads to** recruitment of TBK1/IKKε and activation of IRF3/IRF7, with a parallel NF-κB inflammatory branch. [Reactome R-HSA-168928](https://reactome.org/content/detail/R-HSA-168928) [58]
5. **IRF3/IRF7 and NF-κB activation leads to** inappropriate transcription and secretion of IFN-β, IFN-α and inflammatory cytokines.
6. **Type-I IFN binding to IFNAR1/IFNAR2 leads to** JAK1/TYK2 activation and STAT1/STAT2–IRF9 signaling.
7. **JAK–STAT signaling leads to** sustained expression of interferon-stimulated genes including IFI27, IFI44L, IFIT1, ISG15, RSAD2 and SIGLEC1.
8. **Sustained interferon signaling leads to** immune-cell activation, endothelial and tissue inflammation, altered cell survival and developmental neurotoxicity.
9. **In the central-nervous-system branch, chronic prenatal/infantile inflammation leads to** white-matter injury, calcification and cerebral atrophy, resulting in developmental delay, regression, dystonia and spasticity. The exact cell-autonomous contribution of neurons versus glia is partly inferred rather than fully demonstrated in human tissue.
10. **In the vascular–skeletal–dental branch, chronic MDA5/IFN inflammation leads to** dysregulated mineralization and remodeling, resulting in aortic/valvular calcification, osteopenia, acro-osteolysis and abnormal tooth roots/loss. The intermediate mineralization mechanisms remain incompletely resolved.
11. **In systemic branches, immune dysregulation leads to** chilblains, psoriasis-like disease, hepatitis, lupus-like autoimmunity, thyroid disease, pulmonary vascular disease or organ-limited inflammation.
12. **Modifier genes and immune exposures are inferred to alter** threshold and tissue distribution, producing incomplete penetrance and extreme variable expressivity.

## 6.2 Upstream and downstream processes

**Upstream:** MDA5 RNA recognition, ATP binding/hydrolysis and filament dynamics.  
**Intermediate:** MAVS, TBK1/IKKε, IRF3/7, NF-κB, IFN secretion.  
**Downstream:** IFNAR–JAK1/TYK2–STAT1/2–IRF9, ISG expression, chronic inflammation and tissue injury.

Suggested GO biological-process terms:

- GO:0009615 response to virus
- GO:0003725 double-stranded RNA binding
- GO:0039528 cytoplasmic pattern-recognition receptor signaling pathway in response to virus
- GO:0032481 positive regulation of type I interferon production
- GO:0060337 type I interferon signaling pathway
- GO:0045087 innate immune response
- GO:0006954 inflammatory response
- GO:0002250 adaptive immune response
- GO:0043065 positive regulation of apoptotic process, where experimentally supported
- GO:0001503 ossification/mineralization-related processes for the SMS branch, presently less direct

Suggested GO cellular-component terms:

- GO:0005829 cytosol
- GO:0005739 mitochondrion
- GO:0005741 mitochondrial outer membrane
- GO:0005634 nucleus
- GO:0031514 motile cilium is **not** a primary compartment and should not be assigned.

## 6.3 Cells implicated

| Cell type | Suggested CL term | Evidence/status |
|---|---|---|
| Microglial cell | **CL:0000129** | Likely CNS effector of interferon-mediated inflammation; partly inferred from AGS biology |
| Astrocyte | **CL:0000127** | Likely contributes to white-matter and cytokine responses; human IFIH1-specific evidence limited |
| Neuron | **CL:0000540** | Injured downstream; degree of cell-autonomous MDA5 toxicity uncertain |
| Oligodendrocyte | **CL:0000128** | Relevant to white-matter injury; mechanism incompletely demonstrated |
| Monocyte | **CL:0000576** | Peripheral innate immune/ISG-signature source |
| Macrophage | **CL:0000235** | Model evidence of expansion and inflammatory infiltration |
| Dendritic cell | **CL:0000451** | Expanded in MDA5-GOF mouse models; type-I-IFN amplification |
| T cell | **CL:0000084** | Downstream adaptive immune activation |
| Regulatory T cell | **CL:0000815** | Cell-specific MDA5-G821S expression can cause Treg loss and lethal autoimmunity in mice [130] |
| Vascular endothelial cell | **CL:0000115** | Plausible vascular-injury target; direct causal hierarchy not fully established |
| Osteoblast/osteoclast | **CL:0000062 / CL:0000092** | Likely altered in skeletal remodeling; definitive human cell-level data limited |

## 6.4 Molecular profiling and advanced technologies

The validated clinical transcriptomic feature is the **whole-blood ISG signature**. In the 2020 cohort, 109/117 measurements from 51 mutation-positive people were elevated; 16 samples from seven clinically unaffected carriers were also positive. The six-gene score used **IFI27, IFI44L, IFIT1, ISG15, RSAD2 and SIGLEC1**. [39]

No validated disease-specific human:

- single-cell atlas,
- spatial-transcriptomic map,
- proteomic signature,
- metabolomic or lipidomic signature,
- or integrated multi-omic clinical classifier

was identified. The absence of these data should be encoded as “not established,” rather than as a negative finding.

---

# 7. Anatomical structures affected

| Scale | Structure | Suggested ontology term | Typical disease |
|---|---|---|---|
| Organ | Brain | UBERON:0000955 | AGS-like neuroinflammation |
| Region | Basal ganglia | UBERON:0002420 | Calcification |
| Tissue | Cerebral white matter | UBERON:0002437 | Leukodystrophy/white-matter lesions |
| Organ | Spinal cord/corticospinal tracts | UBERON:0002240 | Spastic paraparesis, sometimes normal MRI |
| Organ | Skin | UBERON:0002097 | Chilblains, psoriasiform lesions |
| Organ | Liver | UBERON:0002107 | Hepatitis, transaminitis or isolated disease |
| Structure | Aorta | UBERON:0000947 | Progressive calcification/stenosis |
| Structure | Aortic and mitral valves | UBERON:0002137 and valve-specific child terms | Calcification |
| Organ | Heart | UBERON:0000948 | Valvular disease, model myocarditis/fibrosis |
| Organ | Lung/pulmonary vasculature | UBERON:0002048 | Rare pulmonary hypertension |
| Tissue | Bone | UBERON:0002481 | Osteopenia, acro-osteolysis |
| Structure | Phalanges | UBERON:0001435 or specific digit-bone terms | Acro-osteolysis, widened marrow cavities |
| Organ | Tooth/periodontium | UBERON:0001091 | Delayed eruption, short roots, resorption and tooth loss |
| Organ | Eye/anterior chamber | UBERON:0000970 | Glaucoma in SMS |
| Organ | Thyroid gland | UBERON:0002046 | Occasional hypothyroidism |

Neurological disease is generally bilateral/diffuse, but unilateral white-matter disease is documented; therefore lateralization is variable rather than defining. [39]

---

# 8. Temporal development

- **Prenatal/congenital severe disease:** five of six deaths in the 74-person cohort involved severe AGS evident at or shortly after birth, implying prenatal inflammation.
- **Classic postnatal AGS pattern:** apparently normal early development followed by subacute irritability, fever and loss of milestones in infancy.
- **Later regression:** seven patients lost skills after age one despite normal prior development.
- **Spastic-paraparetic pattern:** insidious, slowly progressive childhood or adolescent disease; onset as late as 13 years was documented.
- **SMS pattern:** dental and skeletal abnormalities evolve in childhood; aortic/valvular calcification may progress through childhood or puberty.
- **Clinically silent state:** can persist beyond age 50 despite a pathogenic allele and sometimes elevated ISGs.

The active encephalopathic phase may be followed by relative neurological stabilization, but fixed disability remains. Spastic paraparesis and vascular/skeletal disease may continue to progress. Spontaneous molecular remission is not characterized. Earlier suppression of interferon signaling is biologically more likely to prevent injury than to reverse calcification, atrophy or established leukodystrophy.

---

# 9. Inheritance and population

| Characteristic | Current knowledge |
|---|---|
| Inheritance | Autosomal dominant, monoallelic GOF |
| Recurrence if a parent is heterozygous | 50% transmission probability per pregnancy |
| De novo disease | Common, particularly severe AGS presentations |
| Penetrance | Incomplete: 10/74 carriers, 13.5%, asymptomatic in the largest cohort [31] |
| Expressivity | Extremely variable, including within the same family |
| Sex ratio | No reliable sex bias established |
| Anticipation | Not demonstrated |
| Germline mosaicism | Possible; paternal somatic/germline mosaicism documented [29] |
| Founder effects | None established |
| Carrier frequency | Not reliably measurable; pathogenic alleles individually ultra-rare |
| Consanguinity | Not etiologically relevant to dominant GOF, except in differential diagnoses |
| Prevalence/incidence | Unknown; no robust cases-per-100,000 estimate |
| Geography/ethnicity | Worldwide cases; no confirmed high-risk ancestry |

More than 500 AGS patients of all molecular subtypes have been described, but this is not an IFIH1 prevalence estimate. [136] In one Italian molecular cohort IFIH1 accounted for 11–12% of AGS, versus approximately 3% in an earlier international cohort; this variation likely reflects ascertainment and small samples rather than true geographic prevalence. [141]

---

# 10. Diagnostics

## 10.1 Practical diagnostic pathway

1. **Recognize the spectrum:** congenital-infection-like disease without infection, infantile neuroregression, unexplained spastic-dystonia/paraparesis, intracranial calcification/leukodystrophy, chilblains, or early aortic/dental/skeletal disease.
2. **Exclude urgent acquired mimics**, particularly congenital or CNS infection.
3. **Measure a peripheral-blood type-I-interferon signature**, preferably before immunosuppression and repeated if suspicion remains high.
4. **Perform molecular testing** using an interferonopathy/AGS panel or exome/genome sequencing.
5. **Confirm and phase the variant** by parental testing; assess low-level mosaicism if recurrence or sibling disease is unexplained.
6. **Use functional validation** for novel/VUS alleles: IFNβ reporter assay, basal/poly(I:C)-stimulated signaling, RNA binding, ATPase activity or filament turnover.
7. **Stage organ involvement** with brain imaging, cardiac/vascular, dental, ophthalmic and laboratory assessment.

## 10.2 Clinical tests

| Test | Expected finding/use |
|---|---|
| Blood six-gene ISG panel | Elevated IFI27, IFI44L, IFIT1, ISG15, RSAD2 and SIGLEC1; highly useful but not perfectly sensitive or specific |
| CSF cell count | Lymphocytosis, especially early |
| CSF IFN-α and neopterin | May be elevated; normal values do not exclude disease [22] |
| CBC | Thrombocytopenia in congenital disease; cytopenias may also reflect treatment |
| Liver enzymes/thyroid tests/urinalysis | Screen systemic involvement and differential diagnoses |
| Autoantibodies/complement | Indicated where lupus-like disease is suspected |
| Brain CT | Most sensitive routine test for intracranial/basal-ganglia calcification |
| Brain MRI | White-matter disease, atrophy, developmental abnormalities; may be normal in spastic paraparesis |
| Echocardiography | Valve calcification/stenosis, ventricular function, pulmonary pressure |
| ECG | Baseline and cardiac surveillance |
| CT or vascular imaging | Define aortic calcification when SMS phenotype suspected |
| Dental panoramic imaging | Eruption, roots, alveolar bone and resorption |
| Skeletal radiography/DXA | Acro-osteolysis, marrow-cavity widening, osteopenia |
| Ophthalmology | Glaucoma screening |
| EEG | If seizures or episodic altered awareness; no disease-specific electrophysiological signature |
| Skin biopsy | Nonspecific inflammatory/vasculopathic findings; not diagnostic |
| Brain biopsy | Not recommended for routine diagnosis |

## 10.3 Genetic testing modalities

| Modality | Utility |
|---|---|
| Interferonopathy/AGS panel | Preferred when phenotype and IFN signature are suggestive; include IFIH1, TREX1, RNASEH2A/B/C, SAMHD1, ADAR, RNU7-1, LSM11 and relevant phenocopy genes |
| Single-gene IFIH1 sequencing | Appropriate for a highly characteristic familial phenotype or known family variant |
| Trio WES | Effective for detecting de novo coding GOF variants |
| WGS | Useful after negative panel/WES, for noncoding, mosaic and structural possibilities; still requires functional interpretation |
| CNV analysis/CMA | Low expected yield for the canonical disorder but useful in unexplained developmental disease |
| Karyotype/FISH | Not routine |
| mtDNA testing | Only if mitochondrial differential remains |
| Repeat-expansion testing | Not indicated for the canonical disorder |
| RNA sequencing | Research/adjunctive utility; blood ISG qPCR/NanoString is presently more established |
| Prenatal/PGT testing | Feasible when a familial pathogenic variant is known |

A **normal parental phenotype does not establish that a familial variant is benign**. Test both parents molecularly and, if indicated, assess their interferon signatures.

## 10.4 Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| Other genetic AGS subtypes | Usually TREX1, RNASEH2A/B/C, SAMHD1, ADAR, RNU7-1 or LSM11; often recessive except selected TREX1/ADAR mechanisms |
| DDX58-related atypical Singleton–Merten syndrome | RIG-I rather than MDA5; overlapping calcific/dental phenotype |
| STING-associated vasculopathy (SAVI) | Severe early vasculitic skin and lung disease; TMEM173 variants |
| CANDLE/PRAAS | Lipodystrophy, panniculitis, proteasome-gene defects |
| Congenital infection/TORCH | Positive pathogen testing; AGS often mimics infection but cultures/PCR are negative |
| Genetic leukodystrophies | Usually no persistent type-I-IFN signature |
| Cerebral palsy | Nonprogressive injury; does not explain IFN signature, chilblains or familial calcification |
| Hereditary spastic paraplegia | Can closely mimic IFIH1 paraparesis; test interferon signature and IFIH1 |
| Familial brain calcification | Calcification without typical inflammatory signature or systemic AGS/SMS manifestations |
| Monogenic SLE | Overlap is genuine; IFIH1 GOF can itself produce lupus-like disease |
| Primary immunodeficiency from IFIH1 loss of function | Recurrent/severe RNA-virus infection rather than GOF interferonopathy |

No universally accepted stand-alone clinical diagnostic criteria exist; diagnosis is clinicomolecular.

## 10.5 Screening

- No population or newborn screening program exists.
- **Cascade testing** is recommended for first-degree relatives once a pathogenic variant is found.
- Test apparently unaffected relatives because of incomplete penetrance.
- Surveillance is preferable to assuming lifelong safety in a genotype-positive relative.
- Reproductive options include prenatal diagnosis and PGT-M after genetic counseling.

---

# 11. Outcomes and prognosis

No reliable 5- or 10-year survival statistic is available.

In the largest IFIH1 cohort, **six symptomatic patients died**: five had severe disease apparent at or soon after birth, and one developed regression at 15 months and died at age 16 from sudden cardiorespiratory arrest with pulmonary hypertension found at autopsy. [39][143]

Important morbidity includes:

- severe intellectual and motor disability;
- dystonia, spasticity and contractures;
- feeding and communication impairment;
- visual impairment;
- progressive dental loss;
- osteoporosis and skeletal deformity;
- aortic or valve stenosis/calcification;
- chronic skin disease;
- autoimmune organ disease;
- treatment-related infection and cytopenia.

**Poor prognostic indicators:** prenatal/congenital presentation, early rapid regression, severe microcephaly, extensive atrophy/white-matter disease, cardiopulmonary disease, and delayed control of active inflammation.

**Relatively favorable indicators:** later isolated paraparesis, preserved cognition, absence of structural CNS injury and sustained response to pathway-directed therapy. These are descriptive rather than validated predictors.

The blood ISG score is a **pharmacodynamic biomarker**, but its quantitative value as a long-term prognostic marker is not established; asymptomatic carriers may have persistently high scores.

---

# 12. Treatment

## 12.1 Treatment status and algorithm

There is no approved IFIH1-corrective treatment and no evidence-based surgical cure. A reasonable expert pathway is:

1. document active disease and baseline ISG score;
2. treat urgent organ complications;
3. consider early JAK-pathway inhibition for progressive neurological, cutaneous or systemic inflammation;
4. provide multidisciplinary rehabilitation and organ-specific surveillance;
5. monitor CBC, liver and renal function, lipids, infections and IFN signature;
6. continue cardiac, dental, ophthalmic and bone surveillance even if inflammatory symptoms improve.

## 12.2 Pharmacological and supportive interventions

| Intervention | Mechanism/use | Evidence and outcomes | Suggested NCIT term |
|---|---|---|---|
| **Baricitinib** | Oral JAK1/JAK2 inhibitor; blocks signaling downstream of IFNAR | In an open-label expanded-access AGS cohort of 35, doses were 0.1–0.6 mg/kg/day; reduced skin inflammation and some patients gained milestones. Risks included thrombocytosis, leukopenia and infection. Cohort was genetically heterogeneous and included eight IFIH1 cases in one review summary. [18][155] | NCIT:C127012, Baricitinib |
| **Ruxolitinib** | JAK1/JAK2 inhibitor | Individual IFIH1 cases showed reduced blood/CSF inflammatory markers, improved motor scores or developmental gains; two siblings with paternal mosaic disease had marked ISG-score reduction on 0.5–0.75 mg/kg. Evidence remains uncontrolled. [18][29] | NCIT:C77861, Ruxolitinib |
| Tofacitinib | JAK1/JAK3-predominant inhibitor | Case-level interferonopathy evidence; little IFIH1-specific outcome evidence | NCIT:C95829, Tofacitinib |
| Corticosteroids | Broad anti-inflammatory therapy | May transiently improve fever/irritability; chronic neurological efficacy poor and toxicity substantial | NCIT:C211, Corticosteroid |
| IV immunoglobulin | Immunomodulation | Temporary benefit reported in an IFIH1 child before/around JAK therapy; not established disease modification | NCIT:C270, Intravenous Immunoglobulin |
| Antispasticity therapy | Baclofen, botulinum toxin, benzodiazepines as clinically indicated | Symptomatic; no IFIH1-specific trials | NCIT intervention terms for individual agents |
| Antidystonia/antiepileptic therapy | Individualized | Symptom control only | Drug-specific NCIT term |
| Bisphosphonate/bone-health therapy | Osteoporosis/fracture management | No controlled SMS1 evidence; specialist-directed | NCIT:C1599, Bisphosphonate |
| Dental rehabilitation | Periodontal treatment, prosthetics/implants where feasible | Essential for function; progressive alveolar/root loss complicates management | NCIT:C15329, Dental Procedure |
| Cardiac/vascular intervention | Valve replacement or treatment of stenosis where indicated | Organ-directed; no standardized IFIH1 outcome series | NCIT:C80473 or procedure-specific term |
| PT/OT/speech/feeding therapy | Prevent contracture, preserve mobility and communication; augmentative communication | Standard supportive care, although disease-specific trials absent | NCIT:C15311 Rehabilitation Therapy; NCIT:C15903 Physical Therapy |

Before and during JAK inhibition, screen for tuberculosis and hepatitis as locally recommended, update non-live vaccines where possible, and monitor infection, CBC, hepatic/renal function and thrombosis risk. Live-vaccine decisions require specialist assessment.

## 12.3 Clinical trials

| Trial | Intervention and population | Status/relevance |
|---|---|---|
| **NCT03921554** | Baricitinib in AGS; primary outcome change/stability on AGS scale at 52 weeks; secondary ISG and GMFM-88 outcomes | Directly relevant, genetically heterogeneous AGS [153] |
| **NCT01724580** | Compassionate-use baricitinib for interferonopathies including AGS | Generated expanded-access experience [162] |
| **NCT04517253** | Japanese adults/children with NNS/CANDLE, SAVI or AGS; individualized baricitinib, approximately 6–8 mg daily in AGS arm | Long-term, multi-disease study [151] |
| **NCT06898372** | Retrospective Italian multicenter comparison of JAK1/2-treated and untreated AGS/related interferonopathy patients | Began 2025; planned approximately 24 participants [152] |

No IFIH1-directed gene replacement, CRISPR editing, ASO, siRNA or cell therapy is in established clinical use. Because disease is dominant GOF, successful genetic therapy would likely require allele-specific silencing or correction rather than simple gene addition.

---

# 13. Prevention

## Primary prevention

The occurrence of a de novo mutation cannot currently be prevented by lifestyle modification. For known familial disease:

- genetic counseling;
- PGT-M;
- chorionic-villus or amniotic-fluid prenatal diagnosis;
- donor gametes or other reproductive options

can reduce recurrence according to family preferences.

## Secondary prevention

- Cascade-test relatives.
- Establish baseline neurological, cardiac, dental, bone, eye and laboratory status.
- Repeat ISG measurement and organ surveillance where appropriate.
- Treat active inflammation early, before fixed CNS or vascular injury develops.

## Tertiary prevention

- contracture, aspiration and pressure-injury prevention;
- nutrition and swallowing management;
- infection precautions during JAK inhibition;
- dental hygiene and periodontal follow-up;
- fracture prevention and vitamin-D/calcium adequacy;
- serial echocardiography and vascular assessment;
- glaucoma surveillance;
- psychosocial, educational and communication support.

Routine vaccination remains important, particularly before immunosuppression. There is no IFIH1-specific vaccine or antimicrobial prophylaxis. Live vaccines may be contraindicated or deferred during significant JAK inhibition according to local guidance.

---

# 14. Other species and natural disease

No well-validated naturally occurring companion-animal or livestock equivalent caused by spontaneous IFIH1 GOF was identified in OMIA. The disorder is not infectious and has **no zoonotic or cross-species transmission risk**.

| Species | Taxon | Orthologue/resource | Relevance |
|---|---:|---|---|
| Human | NCBI Taxon 9606 | IFIH1, NCBI Gene 64135 | Natural disease |
| Mouse, *Mus musculus* | 10090 | Ifih1, NCBI Gene **71586**, MGI:1918836 | Experimental GOF and knockout models [91] |
| Zebrafish, *Danio rerio* | 7955 | ifih1, ZFIN-linked orthologue | Transgenic p.Arg742His model corresponding to human p.Arg779His |
| Rat, *Rattus norvegicus* | 10116 | Ifih1 orthologue | Conserved antiviral sensing; no established natural IFIH1 syndrome |
| Pig, *Sus scrofa* | 9823 | IFIH1, NCBI Gene **100101927** | Conserved innate antiviral sensor [48] |

MDA5-dependent dsRNA sensing is evolutionarily conserved among jawed vertebrates, but species differ in interferon development, ligand exposure and tissue response. Consequently, animal models often reproduce systemic inflammation better than human neurological disability.

---

# 15. Model organisms

| Model | Construction | Recapitulated features | Limitations and applications |
|---|---|---|---|
| **Ifih1 G821S/+ mouse** | ENU-induced constitutively active MDA5 missense variant | Systemic IFN signature, growth retardation, early death, lupus-like nephritis, dermatitis, autoantibodies, liver/skin inflammation and skeletal abnormalities [127][128] | CNS phenotype is subtle relative to severe human AGS; useful for systemic autoimmunity, bone disease and pathway dissection |
| **Human MDA5-R822Q BAC-transgenic mouse** | Human SMS-associated p.Arg822Gln transgene | Cardiac inflammation/fibrosis, enlarged aortic valve, aortic calcification, mild skeletal abnormalities and adaptive immune activation [121][126] | Transgene dosage may not reproduce human heterozygosity; limited neurophenotype |
| R822Q plus poly(I:C) mouse | Synthetic dsRNA challenge | Exacerbated inflammation and mortality; rescue on Mavs-null or Ifnar-null backgrounds | Strong trigger may exceed physiological viral exposure; excellent causal test of MDA5→MAVS→IFNAR dependence |
| MDA5-G821S Treg-specific mouse | Conditional GOF in regulatory T cells | Treg apoptosis/loss and lethal systemic autoimmunity | Cell-restricted model, not full human disease; identifies immune-cell contribution [130] |
| **Tg(ifih1 p.Arg742His) zebrafish** | Overexpressed zebrafish mutant corresponding to human p.Arg779His | Systemic inflammation and enhanced IFN signature after suboptimal poly(I:C); visible **nfkb:eGFP** and **isg15:eGFP** reporter activation [106][112] | Overexpression rather than endogenous knock-in; fish neuroanatomy and adaptive immunity differ |
| Zebrafish drug-screening model | Same model treated with compounds | Baricitinib reduced inflammation and ISG expression | Preclinical pharmacodynamic evidence, not proof of human clinical efficacy [107] |
| HEK293T IFNβ-reporter system | Expression of wild-type or mutant IFIH1, ± poly(I:C) | Measures basal and ligand-induced IFNβ promoter activation | Artificial expression and non-native cell context; useful for VUS functional classification |
| Purified-protein/structural systems | RNA binding, ATPase and filament assays | Tests increased RNA affinity, reduced ATP hydrolysis or slower disassembly | Does not reproduce tissue-level disease |
| Patient-derived cells/iPSCs | Fibroblasts, blood cells or neural progenitor systems | Can assess endogenous ISG response and drug suppression | Few IFIH1-specific standardized lines; cellular phenotype may depend on differentiation and baseline IFN state |

> **2023 model-paper quote:** RNA sequencing of mutant zebrafish “revealed a systemic inflammation and IFN signature upon a suboptimal poly I:C induction compared with wild-type larvae.” [Bernal-Bermúdez et al., *Frontiers in Immunology*, 24 November 2023, PMID: **38077314**] [106]

Model resources include MGI/IMSR/MMRRC for mouse alleles—mouse Ifih1 is MGI:1918836 and an Ifih1 resource is listed by MMRRC—and ZFIN for zebrafish lines and publications. [56][96][120]

---

# Evidence appraisal and knowledge gaps

## High-confidence conclusions

- Definitive causal relationship between monoallelic IFIH1 GOF and MONDO:0700262.
- AD inheritance with frequent de novo occurrence.
- Mechanistic activation of MDA5–MAVS–type-I-IFN signaling.
- Very broad expressivity and incomplete penetrance.
- Blood ISG expression is a strong diagnostic and pharmacodynamic biomarker.
- AGS7 and SMS1 represent overlapping ends of one disease spectrum.

## Moderate-confidence conclusions

- Viral or dsRNA stimulation can modify severity.
- Early JAK inhibition can improve inflammatory disease and perhaps permit developmental gains.
- Specific neural and mineralizing cell populations mediate tissue injury.

## Major unresolved questions

- True population prevalence, incidence and sex ratio.
- Why some carriers remain well despite persistent IFN signaling.
- Robust genotype–phenotype correlations.
- Optimal JAK inhibitor, dose, initiation age and treatment duration.
- Whether pre-symptomatic treatment prevents CNS or vascular damage.
- Disease-specific quality-of-life and long-term survival data.
- Human single-cell/spatial maps and validated proteomic/metabolomic biomarkers.
- Safe allele-specific RNA or genome-directed therapy.

The most important practical interpretation is that **a rare IFIH1 variant must be evaluated in the joint context of phenotype, inheritance, interferon signature and functional signaling—not by computational pathogenicity prediction alone**.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1007/s12688-026-00957-1` (1 mention) - Januskinase-Inhibitoren bei Interferonopathien
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `ifih1`, `gof`, `established`, `ags`, `variant`, `mda5`, `dental`, `phenotype`, `inflammation`, `cohort`, `signaling`, `interferon`, `gene`, `signature`, `ifn`, `calcification`, `inflammatory`, `infection`, `skeletal`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 89 |
| Resolved | 84 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 25 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002048` (1 mention) - the report calls it "Lung/pulmonary vasculature"; UBERON calls it **lung**
- `UBERON:0000970` (1 mention) - the report calls it "Eye/anterior chamber"; UBERON calls it **eye**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0039528` (GO_0039528) (1 mention) - replaced by `GO:0002753`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0014367` (1 mention) - the report calls it "Aicardi–Goutières syndrome 7"; MONDO calls it **Aicardi-Goutieres syndrome 7**
- `CL:0000115` (1 mention) - the report calls it "Vascular endothelial cell"; CL calls it **endothelial cell**
- `UBERON:0002420` (1 mention) - the report calls it "Basal ganglia"; UBERON calls it **basal ganglion**, and lists "basal ganglia" among its other names
- `UBERON:0002240` (1 mention) - the report calls it "Spinal cord/corticospinal tracts"; UBERON calls it **spinal cord**, and lists "spinal cord structure" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0002481` (1 mention) - the report calls it "Bone"; UBERON calls it **bone tissue**, and lists "bone" among its other names
- `UBERON:0001091` (1 mention) - the report calls it "Tooth/periodontium"; UBERON calls it **calcareous tooth**, and lists "tooth" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.